# Đặc tả Thiết kế: MD_english_learning Wiki

**Ngày tạo**: 2026-06-21
**Trạng thái**: Đã phê duyệt
**Mục tiêu**: Xây dựng hệ thống tri thức học tiếng Anh (Obsidian Wiki) cho người Việt, kế thừa kiến trúc sư phạm từ `language-wiki` tiếng Hàn và tính tổ chức hệ thống từ `academic-wiki`.

---

## 1. Tổng quan Dự án

### 1.1 Bối cảnh
Dự án mở rộng hệ thống ôn tập ngôn ngữ hiện có (tiếng Hàn `MD_korea_learning`) sang tiếng Anh. Nguồn dữ liệu đầu vào là 18 tệp PDF trong thư mục `pdf english/`, bao gồm:
- **Từ vựng nền tảng**: VIE-4000 Essential English Words 1 & 2 (có giải nghĩa tiếng Việt)
- **Từ vựng IELTS chuyên sâu**: 12 cuốn A&M IELTS Cambridge Cam 8-18 Boost your vocabulary
- **Kỹ năng viết & giao tiếp**: Hướng dẫn viết câu IELTS, 101 câu thoại, cụm từ học thuật, đọc hiểu
- **Nền tảng band 4-5**: Mindset for IELTS 4.0-5.0

### 1.2 Nguyên tắc cốt lõi
1. **Ngôn ngữ giải thích**: Tiếng Việt (cho người Việt học tiếng Anh)
2. **Phương pháp đọc PDF**: Đọc trực tiếp bằng công cụ `view_file` hoặc `markitdown`, KHÔNG viết code trích xuất
3. **Tương thích study-app**: Giữ nguyên cú pháp flashcard `::` để ứng dụng React ôn tập hiện có có thể tái sử dụng
4. **Cấu trúc thư mục**: Nhất quán với `MD_korea_learning` để dễ bảo trì và mở rộng

---

## 2. Cấu trúc Thư mục

```
MD_english_learning/
├── AGENTS.md                              ← Hiến pháp bảo trì wiki tiếng Anh
├── wiki/
│   ├── index.md                           ← Mục lục trung tâm kết nối toàn bộ
│   ├── log.md                             ← Nhật ký hoạt động append-only
│   ├── concepts/
│   │   ├── vocabulary/                    ← Từ vựng theo chủ đề
│   │   │   ├── v-01-people-feelings.md         ← 4000 Essential Words — Chủ đề 1
│   │   │   ├── v-02-daily-activities.md        ← 4000 Essential Words — Chủ đề 2
│   │   │   ├── ...
│   │   │   ├── v-ielts-cam08.md                ← Từ vựng IELTS Cambridge 8
│   │   │   ├── v-ielts-cam09.md                ← Từ vựng IELTS Cambridge 9
│   │   │   ├── ...
│   │   │   ├── v-ielts-cam18-test1.md          ← Từ vựng IELTS Cambridge 18 Test 1
│   │   │   └── v-ielts-mindset-4-5.md          ← Từ vựng IELTS Mindset 4.0-5.0
│   │   └── grammar/                      ← Ngữ pháp tiếng Anh
│   │       ├── g-01-tenses-overview.md         ← Tổng quan thì
│   │       ├── g-02-articles-a-an-the.md       ← Mạo từ
│   │       ├── g-03-prepositions.md            ← Giới từ
│   │       ├── g-04-conditionals.md            ← Câu điều kiện
│   │       ├── g-05-passive-voice.md           ← Câu bị động
│   │       ├── g-06-relative-clauses.md        ← Mệnh đề quan hệ
│   │       └── ...                             ← Ngữ pháp rút từ tài liệu IELTS Writing
│   ├── situations/                        ← Hội thoại giao tiếp (từ 101 câu thoại)
│   │   ├── s-01-greetings-introductions.md
│   │   ├── s-02-at-restaurant-ordering.md
│   │   ├── s-03-asking-directions.md
│   │   ├── s-04-shopping.md
│   │   ├── s-05-hotel-check-in.md
│   │   └── ...
│   ├── exam_prep/                         ← Luyện thi IELTS
│   │   ├── ielts-writing-guide.md              ← Cấu trúc viết Task 1 & 2
│   │   ├── ielts-academic-phrases.md           ← Cụm từ học thuật band 7+
│   │   ├── ielts-reading-comprehension.md      ← Chiến lược đọc hiểu
│   │   └── ielts-vocabulary-strategies.md      ← Phương pháp học từ vựng IELTS
│   └── queries/                           ← Lưu câu trả lời động
```

---

## 3. Ánh xạ PDF → Đầu ra Wiki

### 3.1 Nhóm Từ vựng Nền tảng (2 tệp)

| Tệp PDF | Đầu ra | Ghi chú |
|---|---|---|
| `VIE-4000 essential english words 1.pdf` | Nhiều file `v-01-*.md` đến `v-XX-*.md` | Chia theo chủ đề/unit trong sách, mỗi unit tạo 1 file |
| `VIE-4000 essential english words 2.pdf` | Tiếp tục `v-XX-*.md` | Nối tiếp từ cuốn 1 |

### 3.2 Nhóm Từ vựng IELTS (12 tệp)

| Tệp PDF | Đầu ra | Ghi chú |
|---|---|---|
| `A&M IELTS - Cam 8 - Boost your vocabulary.pdf` | `v-ielts-cam08.md` | Từ vựng theo Reading/Listening passages |
| `A&M IELTS - Cam 9 - Boost your vocabulary.pdf` | `v-ielts-cam09.md` | ... |
| `A&M IELTS - Cam 10 - Boost your vocabulary.pdf` | `v-ielts-cam10.md` | ... |
| `A&M IELTS - Cam 11 - Boost your vocabulary.pdf` | `v-ielts-cam11.md` | ... |
| `A&M IELTS - Cam 12 - Boost your vocabulary.pdf` | `v-ielts-cam12.md` | ... |
| `A&M IELTS - Cam 13 - Boost your vocabulary.pdf` | `v-ielts-cam13.md` | ... |
| `A&M IELTS - Cam 14 - Boost your vocabulary.pdf.pdf` | `v-ielts-cam14.md` | ... |
| `A&M IELTS - Cam 15 - Boost your vocabulary_version2024.pdf` | `v-ielts-cam15.md` | ... |
| `A&M IELTS - Cam 17 - Boost your vocabulary.pdf` | `v-ielts-cam17.md` | ... |
| `A&M IELTS_Special Version_...cambridge IELTS 16 (1).pdf` | `v-ielts-cam16.md` | ... |
| `A&M IELTS - TEST1_Cam 18 - Boost your vocabulary.pdf` | `v-ielts-cam18-test1.md` | ... |
| `A&M IELTS - Mindset for IELTS 4.0-5.0 - Boost your vocabulary.pdf` | `v-ielts-mindset-4-5.md` | Band 4-5 nền tảng |

### 3.3 Nhóm Giao tiếp (1 tệp)

| Tệp PDF | Đầu ra | Ghi chú |
|---|---|---|
| `101 câu thoại.pdf` | Nhiều file `s-01-*.md` đến `s-XX-*.md` | Chia theo chủ đề hội thoại |

### 3.4 Nhóm Kỹ năng IELTS (3 tệp)

| Tệp PDF | Đầu ra | Ghi chú |
|---|---|---|
| `A&M IELTS - Hướng dẫn viết câu IELTS Writing.pdf` | `exam_prep/ielts-writing-guide.md` + `grammar/g-*.md` | Cấu trúc câu + ngữ pháp rút ra |
| `Highlight-academic-phrases...ver.2.2.2023.pdf` | `exam_prep/ielts-academic-phrases.md` | Cụm từ học thuật band 7+ |
| `Boost your comprehension_Cambridge_IELTS_11...pdf` | `exam_prep/ielts-reading-comprehension.md` | Chiến lược đọc hiểu |

---

## 4. Định dạng Nội dung (kế thừa từ tiếng Hàn)

### 4.1 Định dạng Từ vựng (`v-*.md`)

```markdown
# Từ vựng Chủ đề: [Tên chủ đề]

> Nguồn: [Tên sách PDF]
> Tổng số từ: [N] | IELTS Band: [nếu có]

---

## Phần 1: Bảng Flashcard Spaced Repetition

- abandon /əˈbændən/ :: từ bỏ, bỏ rơi | #IELTS-6
- abundant /əˈbʌndənt/ :: dồi dào, phong phú | #IELTS-6
- ...

## Phần 2: Chunking Progression (Phát triển Cụm từ)

### abandon /əˈbændən/
- **Từ đơn**: abandon → từ bỏ
- **Collocations**: abandon hope → từ bỏ hy vọng
- **Câu hoàn chỉnh**: They had to abandon the project due to lack of funding.
  → Họ phải từ bỏ dự án vì thiếu kinh phí.

## Phần 3: Mạng Liên tưởng Nơ-ron (Neural Association Network)

### abandon
- 🔄 **Đồng nghĩa**: desert, forsake, give up
- ⚡ **Trái nghĩa**: keep, maintain, continue
- 🔗 **Word Family**: abandonment (n.), abandoned (adj.)
- 🎯 **Collocations phổ biến**: abandon + hope/plan/project/child
- 🇻🇳 **Văn hóa ứng dụng**: Thường gặp trong bài đọc IELTS chủ đề xã hội

## Phần 4: Bài tập Đọc Ứng dụng

[Đoạn văn tiếng Anh có sử dụng các từ vựng trong bài]
→ Dịch xen kẽ: They (Họ) decided (quyết định) to abandon (từ bỏ) the project (dự án)...
```

### 4.2 Định dạng Ngữ pháp (`g-*.md`)

```markdown
# [Cấu trúc ngữ pháp tiếng Anh]

## Giải thích của Giáo viên
[Giải thích tiếng Việt dễ hiểu]

## Công thức & Bảng chia
[Bảng công thức]

## ⚠️ Bẫy Lỗi sai & So sánh
[So sánh các cấu trúc dễ nhầm]

## Ví dụ Ứng dụng
[Câu ví dụ song ngữ Anh-Việt]

## Liên kết Từ vựng
[[v-*.md]] — các file từ vựng sử dụng cấu trúc này
```

### 4.3 Định dạng Hội thoại Giao tiếp (`s-*.md`)

```markdown
# Tình huống: [Tên tình huống]

## Hội thoại mẫu

**A**: Excuse me, could you help me? /ɪkˈskjuːz miː, kʊd juː hɛlp miː/
→ Xin lỗi, bạn có thể giúp tôi không?

**B**: Sure, what do you need? /ʃʊr, wɒt duː juː niːd/
→ Tất nhiên, bạn cần gì?

## Từ vựng Bổ trợ
- excuse :: xin lỗi (khi muốn hỏi ai đó)
- help :: giúp đỡ

## Biến thể Tình huống
[Các cách nói khác cho cùng tình huống]
```

### 4.4 Định dạng Luyện thi IELTS (`exam_prep/*.md`)

```markdown
# [Tên tài liệu luyện thi]

## Chiến lược làm bài
[Mẹo và kỹ thuật]

## Cấu trúc câu Band 7+
[Các mẫu câu học thuật]

## Từ vựng chủ đề theo Passage
[Flashcard :: cho từng passage]

## Bài tập Thực hành
[Câu hỏi mẫu + đáp án có giải thích]
```

---

## 5. AGENTS.md — Hiến pháp Wiki Tiếng Anh

Tệp `AGENTS.md` sẽ quy định:
1. Kiến trúc hệ thống (cây thư mục)
2. Quy trình cập nhật & tiến hóa wiki khi người dùng đặt câu hỏi
3. Quy chuẩn định dạng nội dung bắt buộc (flashcard `::`, phiên âm IPA, dịch xen kẽ)
4. Nhật ký hoạt động (`log.md`)
5. Liên kết chéo [[wikilinks]] giữa các trang

---

## 6. Tích hợp vào Study-app (Chi tiết kỹ thuật)

Ứng dụng study-app hiện tại (`language-wiki/study-app/`) đang hardcode cho tiếng Hàn. Để hỗ trợ cả tiếng Anh, cần thay đổi ở **3 tầng**: Server API, Client UI, và Launcher.

### 6.1 Server API — Hỗ trợ đa ngôn ngữ (`server/index.js`)

**Hiện tại** (dòng 16):
```js
const vaultPath = path.resolve(workspaceRoot, 'MD_korea_learning');
```

**Sau khi sửa**:
```js
// Đọc ngôn ngữ từ biến môi trường hoặc query parameter
const LANG = process.env.STUDY_LANG || 'korean';
const VAULT_MAP = {
  korean: 'MD_korea_learning',
  english: 'MD_english_learning'
};
const vaultPath = path.resolve(workspaceRoot, VAULT_MAP[LANG] || VAULT_MAP.korean);
```

**Thêm API endpoint chuyển ngôn ngữ**:
```js
// GET /api/language — trả về ngôn ngữ hiện tại
app.get('/api/language', (req, res) => {
  res.json({ language: LANG, vault: VAULT_MAP[LANG] });
});

// POST /api/language/switch — chuyển đổi ngôn ngữ (restart server với biến mới)
app.post('/api/language/switch', (req, res) => {
  const { language } = req.body;
  if (!VAULT_MAP[language]) return res.status(400).json({ error: 'Unsupported language' });
  // Ghi biến môi trường vào file tạm để launcher đọc khi restart
  fs.writeFileSync(path.resolve(cacheDir, '.current-lang'), language, 'utf8');
  res.json({ message: `Switched to ${language}. Please restart the app.`, restart: true });
});
```

**Cache tách riêng theo ngôn ngữ**:
```js
// Mỗi ngôn ngữ có cache file riêng để không xung đột
const cachePath = path.resolve(cacheDir, `.study-cache-${LANG}.json`);
```

### 6.2 Client UI — Nút chuyển đổi ngôn ngữ (`src/App.jsx`)

**Thêm state quản lý ngôn ngữ**:
```jsx
const [currentLang, setCurrentLang] = useState('korean');

useEffect(() => {
  // Lấy ngôn ngữ hiện tại từ server khi mount
  fetch(`${API_BASE}/api/language`)
    .then(res => res.json())
    .then(data => setCurrentLang(data.language));
}, []);
```

**Thêm nút chuyển đổi vào header** (cạnh tiêu đề):
```jsx
<header>
  <div style={{ display: 'flex', alignItems: 'center', gap: '1rem' }}>
    <h1>{currentLang === 'korean' ? '🇰🇷 TOPIK' : '🇬🇧 IELTS'} Language Learning Wiki</h1>
    <button 
      className="btn btn-secondary"
      onClick={switchLanguage}
      title="Chuyển ngôn ngữ"
    >
      {currentLang === 'korean' ? '🇬🇧 English' : '🇰🇷 한국어'}
    </button>
  </div>
  {/* ... tab buttons giữ nguyên ... */}
</header>
```

**TTS chuyển giọng theo ngôn ngữ**:
```jsx
// Trong VocabLearner.jsx — hàm phát âm
const speak = (text) => {
  const utterance = new SpeechSynthesisUtterance(text);
  utterance.lang = currentLang === 'korean' ? 'ko-KR' : 'en-US';
  utterance.rate = 0.85;
  speechSynthesis.speak(utterance);
};
```

### 6.3 Launcher — `run-study-app.bat` hỗ trợ chọn ngôn ngữ

**Thêm menu chọn ngôn ngữ khi khởi động**:
```batch
echo Chon ngon ngu hoc:
echo   [1] Tieng Han (Korean - TOPIK)
echo   [2] Tieng Anh (English - IELTS)
set /p LANG_CHOICE="Nhap so (1 hoac 2): "
if "%LANG_CHOICE%"=="2" (
    set STUDY_LANG=english
    echo Dang khoi dong che do hoc Tieng Anh...
) else (
    set STUDY_LANG=korean
    echo Dang khoi dong che do hoc Tieng Han...
)
```

Biến `STUDY_LANG` được truyền xuống `npm run server` để server đọc `process.env.STUDY_LANG`.

### 6.4 Parser — Tương thích cú pháp (`server/parser.js`)

Parser hiện tại đã hỗ trợ cú pháp flashcard `::` dùng chung cho cả hai ngôn ngữ:
```
- word /IPA/ :: nghĩa tiếng Việt | #TAG
```

**Khác biệt duy nhất giữa tiếng Hàn và tiếng Anh**:
| Yếu tố | Tiếng Hàn | Tiếng Anh |
|---|---|---|
| Phiên âm | `(**ga-kkưm**)` — Phiên âm Việt tự nhiên | `/əˈbændən/` — Phiên âm IPA chuẩn |
| Tag | `#TOPIK-1` đến `#TOPIK-6` | `#IELTS-4` đến `#IELTS-9` |
| TTS voice | `ko-KR` | `en-US` |

Parser hiện tại (`parser.js` dòng 38-40) đã có regex strip `#TOPIK-*`, cần bổ sung thêm strip `#IELTS-*`:
```js
// Hiện tại:
meaning = meaning.replace(/\s*\|\s*#TOPIK-\d+/g, '');
// Bổ sung:
meaning = meaning.replace(/\s*\|\s*#(TOPIK|IELTS)-\d+/g, '');
```

### 6.5 Tóm tắt Thay đổi Code

| File | Thay đổi | Mức độ |
|---|---|---|
| `server/index.js` | Thêm `STUDY_LANG`, `VAULT_MAP`, API `/api/language`, cache tách riêng | Trung bình |
| `server/parser.js` | Bổ sung regex strip `#IELTS-*` | Nhỏ (1 dòng) |
| `src/App.jsx` | Thêm state `currentLang`, nút chuyển đổi 🇰🇷↔🇬🇧, tiêu đề động | Nhỏ |
| `src/components/VocabLearner.jsx` | TTS voice theo `currentLang` | Nhỏ (1 dòng) |
| `run-study-app.bat` | Thêm menu chọn ngôn ngữ, truyền biến `STUDY_LANG` | Nhỏ |


---

## 7. Quy trình Thực hiện

### Giai đoạn 1: Init (Khởi tạo cấu trúc)
1. Tạo cây thư mục `MD_english_learning/`
2. Viết `AGENTS.md`, `wiki/index.md`, `wiki/log.md`
3. Commit git

### Giai đoạn 2: Ingest — Đọc PDF & Sinh nội dung
Đọc trực tiếp 18 tệp PDF bằng `markitdown` hoặc `view_file`, trích xuất nội dung và sinh các trang wiki Markdown. Thứ tự ưu tiên:
1. **VIE-4000 Essential Words 1 & 2** → Từ vựng nền tảng `v-01` đến `v-XX`
2. **101 câu thoại** → Hội thoại giao tiếp `s-01` đến `s-XX`
3. **IELTS Cam 8-18** → Từ vựng IELTS `v-ielts-cam*`
4. **IELTS Writing + Phrases + Comprehension** → `exam_prep/` + `grammar/`

### Giai đoạn 3: Compile — Liên kết & Hoàn thiện
1. Xây dựng liên kết chéo [[wikilinks]] giữa các trang
2. Cập nhật `wiki/index.md` với mục lục đầy đủ
3. Kiểm tra tính toàn vẹn liên kết (lint)

### Giai đoạn 4: Verify — Kiểm tra chất lượng
1. Đếm tổng số từ vựng, hội thoại, ngữ pháp đã tạo
2. Kiểm tra cú pháp flashcard `::` tương thích study-app
3. Xác minh liên kết [[wikilinks]] không bị hỏng

---

## 8. Ràng buộc & Rủi ro

### Ràng buộc
- Đọc PDF trực tiếp, KHÔNG viết code trích xuất
- Giải thích bằng tiếng Việt
- Tên file canonical: ngắn gọn, dễ nhớ, tiếng Việt/Anh (ví dụ: `v-01-daily-life`, `v-ielts-cam18-test1`)
- Cú pháp flashcard `::` tương thích study-app

### Rủi ro
- **PDF scanned image**: Một số tệp PDF có thể là ảnh quét, không đọc được text trực tiếp → Dùng `view_file` để render từng trang và đọc bằng thị giác AI
- **Khối lượng lớn**: 18 tệp PDF, mỗi cuốn 50-200+ trang → Cần chia nhỏ thành nhiều bước thực thi tuần tự, có thể cần nhiều phiên làm việc
- **Trùng lặp từ vựng giữa các cuốn**: Từ vựng IELTS có thể lặp lại giữa Cam 8-18 → Cần cơ chế dedup hoặc ghi chú tần suất xuất hiện
