const express = require('express');
const cors = require('cors');
const fs = require('fs');
const path = require('path');
const { exec } = require('child_process');
const { parseCardLine, serializeCardLine } = require('./parser');
const { Pool } = require('pg');

const app = express();
const PORT = process.env.PORT || 3001;

app.use(cors());
app.use(express.json());

// Path definitions — Multi-language support
const workspaceRoot = path.resolve(__dirname, '../../../');
const LANG = process.env.STUDY_LANG || 'korean';
const VAULT_MAP = {
  korean: 'MD_korea_learning',
  english: 'MD_english_learning'
};

let cacheDir = path.resolve(workspaceRoot, '.superpowers');
try {
  if (!fs.existsSync(cacheDir)) {
    fs.mkdirSync(cacheDir, { recursive: true });
  }
} catch (e) {
  cacheDir = path.resolve('/tmp', '.superpowers');
  if (!fs.existsSync(cacheDir)) {
    fs.mkdirSync(cacheDir, { recursive: true });
  }
}

function getVaultPathForLang(lang) {
  const activeVault = VAULT_MAP[lang] || VAULT_MAP.korean;
  let targetPath = path.resolve(workspaceRoot, activeVault);
  try {
    if (!fs.existsSync(targetPath)) {
      targetPath = path.resolve(__dirname, '../', activeVault);
    }
  } catch (e) {
    targetPath = path.resolve(__dirname, '../', activeVault);
  }
  return targetPath;
}

// PostgreSQL Pool configuration (Supabase integration)
const DATABASE_URL = process.env.DATABASE_URL;
let dbPool = null;

if (DATABASE_URL) {
  console.log('Connecting to PostgreSQL database (Supabase Cloud)...');
  dbPool = new Pool({
    connectionString: DATABASE_URL,
    ssl: { rejectUnauthorized: false } // Required for hosting solutions like Render + Supabase
  });

  // Initialize table
  dbPool.query(`
    CREATE TABLE IF NOT EXISTS card_progress (
      word TEXT NOT NULL,
      lang TEXT NOT NULL,
      due VARCHAR(10) NOT NULL,
      interval INTEGER NOT NULL,
      ease INTEGER NOT NULL,
      streak INTEGER NOT NULL,
      updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
      PRIMARY KEY (word, lang)
    );
  `).then(() => {
    console.log('PostgreSQL database table card_progress initialized.');
  }).catch(err => {
    console.error('Failed to initialize database table:', err);
  });
} else {
  console.log('Running in Offline Mode (DATABASE_URL not set). Updates will be written to local Markdown files.');
}

// Fetch overriding progress from DB
async function getDBCardProgressMap(lang) {
  if (!dbPool) return {};
  try {
    const res = await dbPool.query('SELECT word, due, interval, ease, streak FROM card_progress WHERE lang = $1', [lang]);
    const map = {};
    res.rows.forEach(row => {
      map[row.word] = {
        due: row.due,
        interval: row.interval,
        ease: row.ease,
        streak: row.streak
      };
    });
    return map;
  } catch (err) {
    console.error('Failed to query card progress from database:', err);
    return {};
  }
}

// Ensure cache directory exists
// Cache directory is ensured in the boot configuration block

// In-memory queue of modified files for batch commits
let modifiedFilesQueue = new Set();

// Load or initialize cache for dynamic language
function loadCache(lang = 'korean') {
  const activeCachePath = path.resolve(cacheDir, `.study-cache-${lang}.json`);
  if (fs.existsSync(activeCachePath)) {
    try {
      return JSON.parse(fs.readFileSync(activeCachePath, 'utf8'));
    } catch (e) {
      console.error(`Failed to parse cache file for ${lang}, initializing clean cache:`, e);
    }
  }
  return { files: {} };
}

// Save cache atomically for dynamic language
function saveCache(cache, lang = 'korean') {
  const activeCachePath = path.resolve(cacheDir, `.study-cache-${lang}.json`);
  const tmpCachePath = activeCachePath + '.tmp';
  try {
    fs.writeFileSync(tmpCachePath, JSON.stringify(cache, null, 2), 'utf8');
    fs.renameSync(tmpCachePath, activeCachePath);
  } catch (e) {
    console.error(`Failed to save cache atomically for ${lang}:`, e);
  }
}

let memoryCaches = { korean: null, english: null };
let lastSyncTimes = { korean: 0, english: 0 };
const CACHE_TTL_MS = 5000;

// Incremental cache sync by reading mtime of vocabulary markdown files dynamically
function syncCache(lang = 'korean') {
  const now = Date.now();
  if (memoryCaches[lang] && (now - lastSyncTimes[lang] < CACHE_TTL_MS)) {
    return memoryCaches[lang];
  }

  const cache = loadCache(lang);
  const activeVaultPath = getVaultPathForLang(lang);
  const vocabDir = path.resolve(activeVaultPath, 'wiki/concepts/vocabulary');
  
  if (!fs.existsSync(vocabDir)) {
    console.error(`Vocabulary directory does not exist: ${vocabDir}`);
    return cache;
  }

  const files = fs.readdirSync(vocabDir).filter(f => f.endsWith('.md') && !f.startsWith('_'));
  let cacheUpdated = false;

  files.forEach(file => {
    const filePath = path.resolve(vocabDir, file);
    const relativePath = `${VAULT_MAP[lang]}/wiki/concepts/vocabulary/${file}`;
    const stats = fs.statSync(filePath);
    const mtime = stats.mtimeMs;

    const cachedFile = cache.files[relativePath];
    if (!cachedFile || cachedFile.mtime !== mtime) {
      const content = fs.readFileSync(filePath, 'utf8');
      const lines = content.split(/\r?\n/);
      const cards = [];

      lines.forEach((line, index) => {
        const parsed = parseCardLine(line);
        if (parsed) {
          cards.push({
            lineIndex: index,
            word: parsed.word,
            pronunciation: parsed.pronunciation,
            meaning: parsed.meaning,
            sr: parsed.sr
          });
        }
      });

      cache.files[relativePath] = {
        mtime,
        cards,
        fullContent: content
      };
      cacheUpdated = true;
    }
  });

  if (cacheUpdated) {
    saveCache(cache, lang);
  }
  memoryCaches[lang] = cache;
  lastSyncTimes[lang] = now;
  return cache;
}

// Perform git commit batching
function runGitBatchCommit() {
  if (modifiedFilesQueue.size === 0) return;

  const filesToCommit = Array.from(modifiedFilesQueue);
  modifiedFilesQueue.clear();

  // Escape space paths for Windows cmd
  const quotedFiles = filesToCommit.map(f => `"${path.resolve(workspaceRoot, f)}"`).join(' ');
  const gitCommand = `git add ${quotedFiles} && git commit -m "study: sync spaced repetition progress"`;

  console.log(`Executing batch commit for: ${filesToCommit.join(', ')}`);
  exec(gitCommand, { cwd: workspaceRoot }, (err, stdout, stderr) => {
    if (err) {
      console.error('Failed to commit batch:', err);
      // Re-queue files in case of temporary failure
      filesToCommit.forEach(f => modifiedFilesQueue.add(f));
    } else {
      console.log('Batch commit succeeded:', stdout);
    }
  });
}

// Schedule batch commits every 10 minutes
setInterval(runGitBatchCommit, 10 * 60 * 1000);

// API: Get all due cards
app.get('/api/cards/due', async (req, res) => {
  try {
    const lang = req.query.lang || 'korean';
    const cache = syncCache(lang);
    const todayStr = new Date().toISOString().split('T')[0];
    const dueCards = [];

    // Fetch database progress overrides if active
    const dbProgressMap = await getDBCardProgressMap(lang);

    Object.keys(cache.files).forEach(relPath => {
      const fileData = cache.files[relPath];
      fileData.cards.forEach(card => {
        const activeSr = dbProgressMap[card.word] || card.sr || { due: null, interval: 1, ease: 250, streak: 0 };
        const isDue = !activeSr.due || activeSr.due <= todayStr;
        if (isDue) {
          // Provide cognitive context sections
          // Find paragraphs related to the word in the full markdown file
          const paragraphContext = extractWordContext(card.word, fileData.fullContent, lang);

          dueCards.push({
            filePath: relPath,
            word: card.word,
            pronunciation: card.pronunciation,
            meaning: card.meaning,
            sr: activeSr,
            cognitiveData: {
              phonetics: `Phát âm gợi ý: ${card.pronunciation}`,
              hanja: paragraphContext.hanja || (lang === 'korean' ? "Không tìm thấy thông tin gốc Hán-Hàn." : "Không có thông tin từ nguyên."),
              dialogue: paragraphContext.dialogue || (lang === 'korean' ? "Không có kịch bản đàm thoại mẫu." : "Không có ngữ cảnh hội thoại mẫu.")
            }
          });
        }
      });
    });

    res.json({
      totalDue: dueCards.length,
      cards: dueCards
    });
  } catch (err) {
    console.error('Error fetching due cards:', err);
    res.status(500).json({ error: 'Failed to retrieve due cards' });
  }
});

// API: Submit card review results (SM-2 Algorithm)
app.post('/api/cards/review', async (req, res) => {
  const { filePath, word, rating } = req.body;
  if (!filePath || !word || !rating) {
    return res.status(400).json({ error: 'Missing required parameters' });
  }

  try {
    const lang = filePath.includes('MD_english_learning') ? 'english' : 'korean';
    const cache = loadCache(lang);
    const relPath = filePath.replace(/\\/g, '/');
    const fileData = cache.files[relPath];

    if (!fileData) {
      return res.status(404).json({ error: 'File not found in cache' });
    }

    const cardIndex = fileData.cards.findIndex(c => c.word === word);
    if (cardIndex === -1) {
      return res.status(404).json({ error: 'Card not found in file data' });
    }

    const card = fileData.cards[cardIndex];
    
    // Fetch override database progress if active
    const dbProgressMap = await getDBCardProgressMap(lang);
    const activeSr = dbProgressMap[word] || card.sr || { due: null, interval: 1, ease: 250, streak: 0 };
    
    // SM-2 calculations
    let interval = 1;
    let ease = activeSr.ease || 250;
    let streak = activeSr.streak || 0;

    if (rating === 'again') {
      interval = 0; // immediate review queue
      ease = Math.max(130, ease - 20);
      streak = 0;
    } else if (rating === 'hard') {
      interval = Math.max(1, Math.round(activeSr.interval * 1.2));
      ease = Math.max(130, ease - 15);
      streak += 1;
    } else if (rating === 'good') {
      interval = Math.max(3, Math.round(activeSr.interval * 2.5));
      streak += 1;
    } else if (rating === 'easy') {
      interval = Math.max(7, Math.round(activeSr.interval * 4.0));
      ease += 15;
      streak += 1;
    }

    const today = new Date();
    if (interval > 0) {
      today.setDate(today.getDate() + interval);
    }
    const dueStr = today.toISOString().split('T')[0];

    const newSr = {
      due: dueStr,
      interval,
      ease,
      streak
    };

    // Update in-memory cache data
    card.sr = newSr;

    // Database Mode: Write to Supabase and respond immediately
    if (dbPool) {
      try {
        await dbPool.query(`
          INSERT INTO card_progress (word, lang, due, interval, ease, streak, updated_at)
          VALUES ($1, $2, $3, $4, $5, $6, NOW())
          ON CONFLICT (word, lang)
          DO UPDATE SET due = EXCLUDED.due, interval = EXCLUDED.interval, ease = EXCLUDED.ease, streak = EXCLUDED.streak, updated_at = NOW();
        `, [word, lang, dueStr, interval, ease, streak]);
        return res.json({ success: true, updatedSr: newSr });
      } catch (dbErr) {
        console.error('Failed to save progress to PostgreSQL database:', dbErr);
        return res.status(500).json({ error: 'Failed to write progress to cloud database' });
      }
    }

    // Offline Mode: Apply updates directly to the Markdown file atomically
    const fullAbsPath = path.resolve(workspaceRoot, relPath);
    if (!fs.existsSync(fullAbsPath)) {
      return res.status(404).json({ error: 'Physical file not found on disk' });
    }

    const content = fs.readFileSync(fullAbsPath, 'utf8');
    const lines = content.split(/\r?\n/);
    
    // We match the target card line by word
    let cardLineUpdated = false;
    for (let i = 0; i < lines.length; i++) {
      const parsed = parseCardLine(lines[i]);
      if (parsed && parsed.word === word) {
        parsed.sr = newSr;
        lines[i] = serializeCardLine(parsed);
        cardLineUpdated = true;
        break;
      }
    }

    if (!cardLineUpdated) {
      return res.status(500).json({ error: 'Failed to match card word during serialization' });
    }

    const newContent = lines.join('\n');
    
    // Atomic Write
    const tempFile = fullAbsPath + '.tmp';
    fs.writeFileSync(tempFile, newContent, 'utf8');
    fs.renameSync(tempFile, fullAbsPath);

    // Update file stats inside the cache index to match the new modified time
    const updatedStats = fs.statSync(fullAbsPath);
    fileData.mtime = updatedStats.mtimeMs;
    fileData.fullContent = newContent;

    saveCache(cache, lang);

    // Queue file for git batch commit
    modifiedFilesQueue.add(relPath);

    res.json({ success: true, updatedSr: newSr });
  } catch (err) {
    console.error('Error submitting review:', err);
    res.status(500).json({ error: 'Internal server error during review submission' });
  }
});

// API: Manual end session trigger to execute batch commits immediately
app.post('/api/session/end', (req, res) => {
  try {
    runGitBatchCommit();
    res.json({ success: true, message: 'Batch commits pushed successfully' });
  } catch (e) {
    res.status(500).json({ error: e.message });
  }
});

// Helper function to extract cognitive text paragraphs (Hanja root & dialogues)
function extractWordContext(word, fullContent, lang = 'korean') {
  const result = { hanja: '', dialogue: '' };
  const lines = fullContent.split(/\r?\n/);

  if (lang === 'english') {
    let chunkingLines = [];
    let associationLines = [];
    let captureMode = null; // 'chunking' or 'association'
    
    for (let i = 0; i < lines.length; i++) {
      const line = lines[i].trim();
      
      // Identify sections
      if (line.includes('## Phần 2: Chunking Progression')) {
        captureMode = 'chunking';
        continue;
      }
      if (line.includes('## Phần 3: Mạng Liên tưởng')) {
        captureMode = 'association';
        continue;
      }
      if (line.startsWith('## ') && !line.includes('Phần 2') && !line.includes('Phần 3')) {
        captureMode = null;
        continue;
      }
      
      if (captureMode && line.startsWith('### ')) {
        const headerWord = line.replace('###', '').trim().toLowerCase();
        if (headerWord === word.toLowerCase()) {
          // Found the word block! Let's collect lines until next header or page break
          const block = [];
          for (let j = i + 1; j < lines.length; j++) {
            const blockLine = lines[j];
            if (blockLine.startsWith('###') || blockLine.startsWith('##') || blockLine.startsWith('---')) {
              break;
            }
            if (blockLine.trim()) {
              block.push(blockLine.trim());
            }
          }
          if (captureMode === 'chunking') {
            chunkingLines = block;
          } else if (captureMode === 'association') {
            associationLines = block;
          }
        }
      }
    }
    
    if (chunkingLines.length > 0) {
      result.dialogue = chunkingLines.join('\n');
    }
    if (associationLines.length > 0) {
      result.hanja = associationLines.join('\n');
    }
  } else {
    let currentSection = '';
    let matchingHanjaLines = [];
    let matchingDialogueLines = [];

    for (let line of lines) {
      if (line.startsWith('#')) {
        currentSection = line.toLowerCase();
      }
      
      // Look for Hanja explanations
      if (line.includes(word) && (line.includes('Hán') || line.includes('Gốc') || line.includes('gốc') || line.includes('hán'))) {
        matchingHanjaLines.push(line.trim());
      }
      
      // Look for dialogue lines or examples
      if (line.includes(word) && (line.includes('A:') || line.includes('B:') || line.includes(' thoại') || line.includes('Ví dụ'))) {
        matchingDialogueLines.push(line.trim());
      }
    }

    if (matchingHanjaLines.length > 0) {
      result.hanja = matchingHanjaLines.join('\n');
    }
    if (matchingDialogueLines.length > 0) {
      result.dialogue = matchingDialogueLines.join('\n');
    }
  }

  return result;
}

// API: List situations dynamically
app.get('/api/situations', (req, res) => {
  const lang = req.query.lang || 'korean';
  try {
    const activeVaultPath = getVaultPathForLang(lang);
    const situationsDir = path.resolve(activeVaultPath, 'wiki/situations');
    if (!fs.existsSync(situationsDir)) {
      return res.json({ situations: [] });
    }
    const files = fs.readdirSync(situationsDir).filter(f => f.endsWith('.md'));
    const situations = files.map(file => {
      const id = file.replace('.md', '');
      const filePath = path.resolve(situationsDir, file);
      const content = fs.readFileSync(filePath, 'utf8');
      
      // Extract title from first header
      const titleMatch = content.match(/^#\s*(.+)/);
      const title = titleMatch ? titleMatch[1].trim() : id;
      
      return { id, title };
    });
    res.json({ situations });
  } catch (err) {
    console.error('Error fetching situations:', err);
    res.status(500).json({ error: 'Failed to list situations' });
  }
});

// API: Get situation dialogue turns dynamically
app.get('/api/situations/:id', (req, res) => {
  const { id } = req.params;
  const lang = req.query.lang || 'korean';
  try {
    const activeVaultPath = getVaultPathForLang(lang);
    const filePath = path.resolve(activeVaultPath, `wiki/situations/${id}.md`);
    if (!fs.existsSync(filePath)) {
      return res.status(404).json({ error: 'Situation not found' });
    }
    const content = fs.readFileSync(filePath, 'utf8');
    const lines = content.split(/\r?\n/);
    const turns = [];
    
    for (let line of lines) {
      if (line.includes('|') && line.includes('**')) {
        const columns = line.split('|').map(c => c.trim());
        if (columns.length >= 5) {
          const speaker = columns[1].replace(/\*\*/g, '');
          const korean = columns[2];
          const pronunciation = columns[3].replace(/\*/g, '');
          const translation = columns[4];
          if (speaker && korean && translation && speaker !== 'Nhân vật') {
            turns.push({ speaker, korean, pronunciation, translation });
          }
        }
      }
    }
    
    res.json({ id, content, turns });
  } catch (err) {
    console.error('Error getting situation:', err);
    res.status(500).json({ error: 'Failed to parse situation' });
  }
});

const mockQuestions = [
  {
    id: 1,
    question: "지수___ 학생입니다. (Trí 씨 là học sinh. Ji-xu CŨNG là học sinh. Chọn tiểu từ thích hợp.)",
    options: ["가", "도", "를", "에"],
    correctIdx: 1,
    grammarLink: "g-22-명사 + 도 (Cũng).md",
    explanation: "Tiểu từ '도' đứng sau danh từ để biểu thị sự đồng nhất, nghĩa là 'cũng'. Loại bỏ '이/gа', '을/를' khi đi với '도'."
  },
  {
    id: 2,
    question: "저는 학교___ 갑니다. (Tôi đi ĐẾN trường. Chọn tiểu từ vị trí thích hợp.)",
    options: ["을", "에서", "에", "과"],
    correctIdx: 2,
    grammarLink: "g-13-명사 + 에 1 (Tiểu từ vị trí - Trạng thái tồn tại).md",
    explanation: "Tiểu từ '에' biểu thị đích hướng hành động đi/đến đâu đó (가다/오다)."
  },
  {
    id: 3,
    question: "날씨가 ________ 난방기를 켭니다. (VÌ thời tiết LẠNH NÊN tôi bật máy sưởi. Chọn hình thái chia thích hợp.)",
    options: ["춥고", "추워서", "추우면", "춥지만"],
    correctIdx: 1,
    grammarLink: "g-45-동사-형용사 + 아-어서 2 (Vì... nên... - Lý do khách quan).md",
    explanation: "Cấu trúc '-아/어서' chỉ nguyên nhân khách quan. '춥다' là bất quy tắc 'ㅂ', biến đổi thành '추워' + '서' -> '추워서'."
  },
  {
    id: 4,
    question: "저는 커피를 마시고 _________. (Tôi MUỐN uống cà phê. Chọn đuôi câu thể hiện mong muốn.)",
    options: ["싶습니다", "ㅂ니다", "어요", "세요"],
    correctIdx: 0,
    grammarLink: "g-25-동사 + 고 싶다 (Muốn - Ngôi 1 & 2).md",
    explanation: "Cấu trúc '-고 싶다' đi sau động từ để thể hiện ước muốn của người nói (ngôi thứ nhất) hoặc hỏi ước muốn (ngôi thứ hai)."
  },
  {
    id: 5,
    question: "이 책이 저 책________ 더 비쌉니다. (Sách này đắt HƠN sách kia. Chọn cấu trúc so sánh thích hợp.)",
    options: ["도", "로", "보다", "에게"],
    correctIdx: 2,
    grammarLink: "g-32-명사 + 보다 (So với... thì hơn).md",
    explanation: "Tiểu từ '보다' gắn vào sau danh từ làm chuẩn so sánh, nghĩa là 'so với... thì... hơn'."
  }
];

// API: Get mock exam questions
app.get('/api/exams/questions', (req, res) => {
  res.json({ questions: mockQuestions });
});

// API: Submit exam answers for grading & diagnostics
app.post('/api/exams/submit', (req, res) => {
  const { answers } = req.body;
  if (!answers) {
    return res.status(400).json({ error: 'Missing answers data' });
  }

  let correctCount = 0;
  const diagnostics = [];

  mockQuestions.forEach(q => {
    const userAnswer = answers[q.id];
    const isCorrect = userAnswer === q.correctIdx;
    
    if (isCorrect) {
      correctCount += 1;
    } else {
      diagnostics.push({
        questionId: q.id,
        question: q.question,
        userAnswer: q.options[userAnswer] !== undefined ? q.options[userAnswer] : 'Không chọn',
        correctAnswer: q.options[q.correctIdx],
        grammarLink: `[[${q.grammarLink}]]`,
        explanation: q.explanation
      });
    }
  });

  const score = Math.round((correctCount / mockQuestions.length) * 100);

  res.json({
    score,
    totalQuestions: mockQuestions.length,
    correctCount,
    diagnostics
  });
});

// API: List all vocabulary topics dynamically
app.get('/api/topics', (req, res) => {
  const lang = req.query.lang || 'korean';
  try {
    const activeVaultPath = getVaultPathForLang(lang);
    const vocabDir = path.resolve(activeVaultPath, 'wiki/concepts/vocabulary');
    if (!fs.existsSync(vocabDir)) return res.json({ topics: [] });
    const files = fs.readdirSync(vocabDir).filter(f => f.endsWith('.md') && !f.startsWith('_'));
    const topics = files.map(file => {
      const id = file.replace('.md', '');
      const filePath = path.resolve(vocabDir, file);
      const content = fs.readFileSync(filePath, 'utf8');
      const titleMatch = content.match(/^#\s*(.+)/);
      const title = titleMatch ? titleMatch[1].trim().replace(/\*\*/g, '') : id;
      return { id, title };
    });
    res.json({ topics });
  } catch (e) {
    console.error('Error listing topics:', e);
    res.status(500).json({ error: 'Failed to retrieve topics' });
  }
});

// API: Get cards filtered by specific vocabulary topic file dynamically
app.get('/api/cards/by-topic', async (req, res) => {
  const { topic } = req.query;
  const lang = req.query.lang || 'korean';
  if (!topic) return res.status(400).json({ error: 'Missing topic parameter' });
  
  try {
    const cache = syncCache(lang);
    const relPath = `${VAULT_MAP[lang]}/wiki/concepts/vocabulary/${topic}.md`;
    const fileData = cache.files[relPath];
    if (!fileData) {
      return res.status(404).json({ error: 'Topic not found in cache' });
    }

    // Fetch database progress overrides if active
    const dbProgressMap = await getDBCardProgressMap(lang);

    const cards = fileData.cards.map(card => {
      const activeSr = dbProgressMap[card.word] || card.sr || { due: null, interval: 1, ease: 250, streak: 0 };
      const paragraphContext = extractWordContext(card.word, fileData.fullContent, lang);
      return {
        filePath: relPath,
        word: card.word,
        pronunciation: card.pronunciation,
        meaning: card.meaning,
        sr: activeSr,
        cognitiveData: {
          phonetics: `Phát âm gợi ý: ${card.pronunciation}`,
          hanja: paragraphContext.hanja || (lang === 'korean' ? "Không tìm thấy thông tin gốc Hán-Hàn." : "Không có thông tin từ nguyên."),
          dialogue: paragraphContext.dialogue || (lang === 'korean' ? "Không có kịch bản đàm thoại mẫu." : "Không có ngữ cảnh hội thoại mẫu.")
        }
      };
    });

    res.json({ cards });
  } catch (e) {
    console.error('Error fetching cards by topic:', e);
    res.status(500).json({ error: 'Failed to retrieve cards for topic' });
  }
});

// API: Get current language with filesystem diagnostics
app.get('/api/language', (req, res) => {
  let diag = {};
  try {
    const activeVaultPath = getVaultPathForLang(LANG);
    diag = {
      __dirname,
      workspaceRoot,
      vaultPath: activeVaultPath,
      vaultPathExists: fs.existsSync(activeVaultPath),
      vocabDirExists: fs.existsSync(path.resolve(activeVaultPath, 'wiki/concepts/vocabulary')),
      taskFiles: fs.existsSync('/var/task') ? fs.readdirSync('/var/task') : [],
      mcdKoreanFiles: fs.existsSync(path.resolve(__dirname, '../MD_korea_learning')) ? fs.readdirSync(path.resolve(__dirname, '../MD_korea_learning')) : [],
    };
  } catch (err) {
    diag = { error: err.message };
  }
  res.json({ 
    language: LANG, 
    vault: VAULT_MAP[LANG], 
    availableLanguages: Object.keys(VAULT_MAP),
    diagnostics: diag 
  });
});

// API: Switch language (writes to file for launcher to read on restart)
app.post('/api/language/switch', (req, res) => {
  const { language } = req.body;
  if (!VAULT_MAP[language]) {
    return res.status(400).json({ error: `Unsupported language: ${language}. Available: ${Object.keys(VAULT_MAP).join(', ')}` });
  }
  try {
    fs.writeFileSync(path.resolve(cacheDir, '.current-lang'), language, 'utf8');
    res.json({ message: `Language switched to ${language}. Please restart the app to apply.`, restart: true });
  } catch (e) {
    res.status(500).json({ error: 'Failed to save language preference' });
  }
});

const crypto = require('crypto');
const { execFile } = require('child_process');

const ttsCacheDir = path.resolve(cacheDir, 'tts-cache');
if (!fs.existsSync(ttsCacheDir)) {
  fs.mkdirSync(ttsCacheDir, { recursive: true });
}

// API: Neural Text-to-Speech (AI Voice)
app.get('/api/tts', (req, res) => {
  const { text, lang } = req.query;
  if (!text) {
    return res.status(400).json({ error: 'Missing text parameter' });
  }

  const activeLang = lang || LANG;
  // Map language to Microsoft Edge Neural voices
  const voiceMap = {
    korean: 'ko-KR-SunHiNeural',
    english: 'en-US-AriaNeural'
  };
  const voice = voiceMap[activeLang] || voiceMap.korean;

  // Generate unique filename using md5 hash of text and voice
  const hash = crypto.createHash('md5').update(text + voice).digest('hex');
  const filePath = path.resolve(ttsCacheDir, `${hash}.mp3`);

  if (fs.existsSync(filePath)) {
    res.set('Content-Type', 'audio/mpeg');
    return res.sendFile(filePath);
  }

  // Generate via python script
  const scriptPath = path.resolve(__dirname, 'tts_generator.py');
  execFile('python', [scriptPath, text, voice, filePath], (err, stdout, stderr) => {
    if (err) {
      console.error('TTS Generation error:', err, stderr);
      return res.status(500).json({ error: 'Failed to generate neural speech audio' });
    }
    res.set('Content-Type', 'audio/mpeg');
    res.sendFile(filePath);
  });
});

if (require.main === module) {
  app.listen(PORT, () => {
    console.log(`Express API Server running on port ${PORT}`);
    console.log(`Language: ${LANG} | Vault: ${VAULT_MAP[LANG]}`);
  });
}

module.exports = app;



