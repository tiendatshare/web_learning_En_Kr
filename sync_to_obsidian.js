const fs = require('fs');
const path = require('path');
const { Pool } = require('pg');

// Cấu hình Database URL trực tiếp từ thông tin của bạn
const DATABASE_URL = "postgresql://postgres:tientiendat2002%40@db.niqoiuzhycepgphjbedq.supabase.co:5432/postgres";

const VAULT_MAP = {
  korean: 'MD_korea_learning',
  english: 'MD_english_learning'
};

const workspaceRoot = __dirname;

// Parser Helpers
function parseCardLine(line) {
  if (!line.includes('::')) return null;
  const prefixMatch = line.match(/^([ \t]*[-\*\+][ \t]*)/);
  if (!prefixMatch) return null;
  const prefix = prefixMatch[1];
  const cleanLine = line.substring(prefix.length).trim();
  
  const parts = cleanLine.split('::');
  const left = parts[0].trim();
  const right = parts[1].trim();
  
  let word = left;
  let pronunciation = "";
  
  const pMatchAsterisk = left.match(/(.+?)\s*\(\*\*(.+?)\*\*\)/);
  if (pMatchAsterisk) {
    word = pMatchAsterisk[1].trim();
    pronunciation = pMatchAsterisk[2].trim();
  } else {
    const pMatchSimple = left.match(/(.+?)\s*\((.+?)\)/);
    if (pMatchSimple) {
      word = pMatchSimple[1].trim();
      pronunciation = pMatchSimple[2].trim();
    } else {
      const pMatchSlash = left.match(/(.+?)\s*\/([^\/]+)\//);
      if (pMatchSlash) {
        word = pMatchSlash[1].trim();
        pronunciation = pMatchSlash[2].trim();
      }
    }
  }
  
  word = word.replace(/^[-\*\s\+]+/, '').trim();
  let meaning = right;
  
  if (right.includes('<!--')) {
    const commentParts = right.split('<!--');
    meaning = commentParts[0].trim();
  }
  
  // Clean tags from meaning
  meaning = meaning.replace(/\s*\|\s*#[A-Za-z0-9_-]+\s*/g, '').trim();
  meaning = meaning.replace(/\*\*/g, '').trim();
  
  return { prefix, word, pronunciation, meaning };
}

function serializeCardLine(card, sr) {
  const { prefix, word, pronunciation, meaning } = card;
  const cleanPrefix = prefix || '- ';
  let left = `${word}`;
  if (pronunciation) {
    left += ` (**${pronunciation}**)`;
  }
  let right = meaning;
  if (sr && sr.due) {
    right += ` <!-- sr: due ${sr.due} interval ${sr.interval} ease ${sr.ease} streak ${sr.streak} -->`;
  }
  return `${cleanPrefix}${left} :: ${right}`;
}

async function sync() {
  console.log('🔄 Đang kết nối tới Supabase Cloud để tải tiến trình...');
  const pool = new Pool({
    connectionString: DATABASE_URL,
    ssl: { rejectUnauthorized: false }
  });

  try {
    // 1. Tải toàn bộ tiến trình từ cơ sở dữ liệu
    const res = await pool.query('SELECT word, lang, due, interval, ease, streak FROM card_progress');
    console.log(`📥 Đã tải thành công ${res.rowCount} bản ghi tiến trình từ Cloud.`);

    // Group progress by language
    const progressMap = { korean: {}, english: {} };
    res.rows.forEach(row => {
      const lang = row.lang === 'english' ? 'english' : 'korean';
      progressMap[lang][row.word] = {
        due: row.due,
        interval: row.interval,
        ease: row.ease,
        streak: row.streak
      };
    });

    // 2. Tiến hành duyệt qua từng vault ngôn ngữ để đồng bộ
    for (const lang of Object.keys(VAULT_MAP)) {
      const vaultFolder = VAULT_MAP[lang];
      const vocabDir = path.resolve(workspaceRoot, vaultFolder, 'wiki/concepts/vocabulary');

      if (!fs.existsSync(vocabDir)) {
        console.log(`⚠️ Thư mục từ vựng ${vaultFolder} không tồn tại ở local. Bỏ qua.`);
        continue;
      }

      console.log(`📂 Đang đồng bộ hóa thư mục: ${vaultFolder}...`);
      const files = fs.readdirSync(vocabDir).filter(f => f.endsWith('.md'));
      let updatedFilesCount = 0;
      let updatedCardsCount = 0;

      files.forEach(file => {
        const filePath = path.resolve(vocabDir, file);
        const content = fs.readFileSync(filePath, 'utf8');
        const lines = content.split(/\r?\n/);
        let isModified = false;

        for (let i = 0; i < lines.length; i++) {
          const parsed = parseCardLine(lines[i]);
          if (parsed) {
            const dbSr = progressMap[lang][parsed.word];
            if (dbSr) {
              // Cập nhật lại dòng thẻ nhớ
              const newLine = serializeCardLine(parsed, dbSr);
              if (lines[i].trim() !== newLine.trim()) {
                lines[i] = newLine;
                isModified = true;
                updatedCardsCount++;
              }
            }
          }
        }

        if (isModified) {
          const tempFile = filePath + '.tmp';
          fs.writeFileSync(tempFile, lines.join('\n'), 'utf8');
          fs.renameSync(tempFile, filePath);
          updatedFilesCount++;
        }
      });

      console.log(`✅ Đồng bộ thành công ${vaultFolder}: Cập nhật ${updatedCardsCount} thẻ nhớ trên ${updatedFilesCount} tệp.`);
    }

  } catch (err) {
    console.error('❌ Lỗi đồng bộ hóa:', err);
  } finally {
    await pool.end();
    console.log('🏁 Tiến trình đồng bộ hoàn tất.');
  }
}

sync();
