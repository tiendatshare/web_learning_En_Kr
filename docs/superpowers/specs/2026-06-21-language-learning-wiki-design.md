# Đặc Tả Thiết Kế: Language Learning Wiki Plugin & Study App (Bản Hoàn Thiện & Đầy Đủ)

**Ngày thiết kế:** 2026-06-21  
**Trạng thái:** Chờ phê duyệt triển khai  
**Tên Plugin:** `language-wiki`  
**Vị trí Plugin:** `t:\Topik\giao trình kyung hee\language-wiki\`  
**Vị trí Dữ liệu Wiki:** `t:\Topik\giao trình kyung hee\MD_korea_learning\`  

---

## 1. Mục Tiêu & Phạm Vi (Purpose and Scope)

Tài liệu này đặc tả thiết kế cho hệ thống **language-wiki** - một Claude Code/Antigravity Plugin được thiết kế để quản lý và tiến hóa cơ sở tri thức học ngoại ngữ (tiếng Hàn) tích hợp trong Obsidian, đồng bộ với ứng dụng học tập cục bộ (**Study App**).

### 1.1 Mục tiêu chính:
*   Chuyển đổi phương pháp học từ thụ động sang chủ động thông qua ôn tập viết và phản xạ tình huống nói (**Active Recall**).
*   Thực thi chu kỳ ôn tập ngắt quãng (**Spaced Repetition**) lưu trữ trực tiếp trong Obsidian.
*   Tích hợp bộ giả lập phòng thi (**Exam Mode**) chấm điểm tự động và chẩn đoán lỗi sai liên kết trực tiếp với các bài học ngữ pháp.
*   Tích hợp chế độ luyện nói nhập vai (**Speaking Mode**) sử dụng công nghệ Text-to-Speech (TTS) và Speech-to-Text (STT) của trình duyệt để kiểm tra phát âm thực tế của học viên.
*   Thiết lập cơ chế tự tìm kiếm tài liệu học tập (**Auto-Sourcing**) dựa trên lộ trình chuẩn khi học lên cao.

### 1.2 Các ràng buộc cốt lõi (Core Constraints):
*   **Không dùng code để lọc/di chuyển từ vựng:** Toàn bộ quá trình phân tích ngôn ngữ học, dịch thuật, viết phiên âm và phân loại cấu trúc được thực hiện hoàn toàn bởi trí tuệ của Agent (LLM) thông qua chỉ mục prompt, không viết script tự động lọc từ.
*   **Obsidian là nguồn sự thật duy nhất (Single Source of Truth):** Toàn bộ trạng thái ôn tập lưu trực tiếp trong các tệp Markdown dưới dạng mã chú thích ẩn của plugin Obsidian Spaced Repetition.

---

## 2. Kiến Trúc & Bố Cục Thư Mục (Architecture & Layout)

### 2.1 Cấu trúc thư mục dự án Plugin (`language-wiki/`)

```
language-wiki/                  ← Thư mục chính của Plugin
├── plugin.json                 ← Manifest khai báo Plugin với Antigravity IDE
├── commands/
│   └── wiki.md                 ← Khai báo lệnh `/language-wiki:wiki` và các tham số
├── skills/
│   └── wiki/
│       ├── SKILL.md            ← Quy tắc hướng dẫn Agent thực thi các lệnh thô
│       └── references/
│           ├── card-parser.md  ← Hướng dẫn regex phân tích cú pháp tệp tin
│           └── sm2-algorithm.md← Đặc tả toán học của thuật toán ôn tập
├── scripts/
│   ├── start-server.ps1        ← Script PowerShell khởi động Web App & API Server
│   └── lock-manager.py         ← Script python quản lý lockfile đồng thì
├── language_wiki_mcp/
│   ├── index.js                ← Điểm khởi chạy MCP Server (Node.js)
│   └── package.json            ← Định nghĩa các công cụ MCP (MCP Tools)
└── study-app/                  ← Ứng dụng giao diện Web App (React + Vite)
    ├── package.json
    ├── vite.config.js
    ├── server/                 ← API Server cục bộ (Express.js)
    │   ├── index.js            ← Các Endpoint nhận và xử lý sự kiện ôn tập/thi cử
    │   └── file-updater.js     ← Module chuyên trách ghi đè dòng Markdown
    └── src/
        ├── App.jsx             ← Giao diện chính (Dashboard, Học, Ôn tập, Luyện thi, Luyện nói)
        ├── components/         ← Độc thoại phản xạ, gõ từ vựng, check biến âm, đề thi
        └── services/           ← Browser TTS & STT Web Speech API
```

### 2.2 Cấu trúc thư mục dữ liệu học tập (`MD_korea_learning/`)

```
MD_korea_learning/
├── .git/                       ← Git riêng của Wiki để snapshot tiến trình
├── .superpowers/
│   └── .study-cache.json       ← Tệp tin cache lưu trạng thái ôn tập siêu nhẹ (O(1))
├── raw/                        ← Dữ liệu thô (Bất biến đối với bước học)
│   ├── extracts/               ← Các bản OCR thô và dữ liệu cào tự động (.md)
│   └── sources/                ← File PDF gốc của giáo trình
├── wiki/                       ← Dữ liệu đã biên dịch (Do Agent quản lý)
│   ├── index.md                ← Bản đồ mục lục trung tâm
│   ├── concepts/
│   │   ├── grammar/            ← g-*.md (các bài học cấu trúc ngữ pháp)
│   │   └── vocabulary/         ← v-*.md (các bài học từ vựng dạng flashcard)
│   ├── situations/             ← s-*.md (các kịch bản hội thoại thực tế)
│   ├── exams/                  ← exam-*.md (các bộ đề thi giữa kỳ, cuối kỳ, đề thi TOPIK)
│   └── queries/                ← q-*.md (Các câu hỏi ngữ pháp mở rộng tự lưu)
├── CLAUDE.md                   ← Hiến pháp hướng dẫn cách Agent đọc/ghi dữ liệu
├── log.md                      ← Nhật ký ghi lịch sử ôn tập và compile
└── .lock                       ← Advisory lockfile chống xung đột tiến trình
```

---

## 3. Định Dạng Thực Thể (Entity Schemas)

### 3.1 Thực thể Đề thi (Exam Entity) — `wiki/exams/exam-*.md`
Đề thi lưu trữ các câu hỏi trắc nghiệm dưới dạng cú pháp JSON đính kèm trong Frontmatter và lời giải chi tiết ở phần Body để người dùng đọc lại trong Obsidian.

```markdown
---
type: exam
title: "Kyung Hee Sơ cấp 1 - Đề thi giữa kỳ"
level: topik-1
questions:
  - id: q01
    type: multiple-choice
    question: "저는 주말에 공원(    ) 운동을 합니다."
    options: ["에", "에서", "을", "는"]
    answer: 1 # Chỉ mục mảng, tức là "đáp án số 2 에서"
    grammar-link: "g-03-eo-seo"
    explanation: "Hành động diễn ra tại một địa điểm (운동 làm việc) cần điền tiểu từ 에서."
  - id: q02
    type: multiple-choice
    question: "책이 책상 (    ) 있습니다."
    options: ["위", "아래", "옆", "안"]
    answer: 0
    grammar-link: "g-05-wi-arae"
    explanation: "Sách ở trên bàn học, dùng tiểu từ vị trí 위."
created: 2026-06-21
updated: 2026-06-21
---
# Lời Giải Chi Tiết Đề Thi Giữa Kỳ

## Câu 1: 저는 주말 e 공원 에서 운동을 합니다.
*   **Đáp án đúng:** 에서
*   **Giải thích:** 에서 chỉ nơi diễn ra hành động. Chi tiết xem bài: [[g-03-eo-seo]]

## Câu 2: 책이 책상 위 있습니다.
*   **Đáp án đúng:** 위
*   **Giải thích:** Chỉ vị trí bên trên của vật thể. Chi tiết xem bài: [[g-05-wi-arae]]
```

### 3.2 Thực thể Từ vựng nâng cấp (Vocabulary) — `wiki/concepts/vocabulary/v-*.md`
Bổ sung thêm trường đồng nghĩa `synonyms` và các thuộc tính biến âm cụ thể.

```markdown
---
type: vocabulary
topic: "Home & Furniture"
created: 2026-06-21
updated: 2026-06-21
tags: [vocab/home, level/topik-1]
---
# Từ vựng Chủ đề: Nhà cửa & Đồ gia dụng

## 🎴 1. Flashcard Hub — Spaced Repetition
- 책상 (**chaek-sang**) :: bàn học/bàn làm việc | #TOPIK-1 | synonyms: ["탁자", "테이블"] <!-- sr: due 2026-06-24, interval 3, ease 250, streak 1 -->
- 침대 (**chim-dae**) :: giường ngủ | #TOPIK-1 <!-- sr: due 2026-06-21, interval 1, ease 230, streak 1 -->

## 🧠 2. Bản đồ Âm - Chữ (Phonetic-to-Spelling Map)
*   **Spelling:** `같이` | **Phát âm thực tế:** `[가치] (ga-chi)`
    *   *Loại biến âm:* Vòm họng hóa (구개음화). Khi phụ âm cuối `ㅌ` gặp nguyên âm `이`, nó biến thành âm `치`.
*   **Spelling:** `책상` | **Phát âm thực tế:** `[책쌍] (chaek-ssang)`
    *   *Loại biến âm:* Trọng âm hóa (경음화). Phụ âm cuối `ㄱ` làm phụ âm đầu `ㅅ` của âm tiết sau biến thành âm căng `ㅆ`.

## 🀄 3. Cây gốc Hán-Hàn (Sino-Korean Root Tree)
### 🌳 Gốc Hán-Hàn: **실 (Thất - Phòng)**
*   거실 (Cư thất) → Phòng khách
*   교실 (Giáo thất) → Phòng học
*   화장실 (Hóa trang thất) → Nhà vệ sinh

## 🗣️ 4. Kịch bản Độc thoại Phản xạ (Output Shadowing Scenarios)
### Tình huống: Bật điều hòa vì phòng nóng
*   A: 방이 너무 더워요. (Phòng nóng quá.)
*   B: **에어컨을 켜야 해요.** (Tôi phải bật máy điều hòa.) ← Liên kết ngữ pháp: [[g-02-eo-ya-hada]] (Phải làm gì)
*   A: 네, 에어컨을 켜 주세요. (Vâng, hãy bật điều hòa giúp tôi.)
```

### 3.3 Thực thể Ngữ pháp (Grammar Concept) — `wiki/concepts/grammar/g-*.md`
```markdown
---
type: grammar
structure: "N + 도"
meaning: "Cũng"
created: 2026-06-21
updated: 2026-06-21
tags: [grammar/particle, level/topik-1]
---
# Ngữ pháp: N + 도 (Cũng)

## 📝 1. Giải thích & Chia Đuôi
*   Dùng sau danh từ để thể hiện sự tương đồng với một đối tượng khác đã nhắc tới.
*   Không phân biệt danh từ có phụ âm cuối (chim) hay không.
    *   가방 (Túi xách) + 도 → 가방도
    *   모자 (Mũ) + 도 → 모자do

## ⚖️ 2. Ma trận So sánh & Lưu ý lỗi sai
*   **Phân biệt `도` vs `은/는`:** `은/는` nhấn mạnh sự đối chiếu, so sánh giữa 2 đối tượng khác nhau. `도` nhấn mạnh sự đồng nhất, giống nhau.
*   *Lỗi sai kinh điển:* Không viết `가방이도` (Bỏ tiểu từ `이/ga` hoặc `을/를` khi kết hợp với `도`). 
    *   Đúng: Bag도 있어요. Sai: Bag이도 있어요.

## 🧱 3. Ứng dụng Độc thoại Phản xạ
*   A: 저는 사과를 좋아해요. (Tôi thích táo.)
*   B: **저도 사과를 좋아해요.** (Tôi cũng thích táo.) ← Liên kết từ vựng: [[v-06-food-dining]] (Món ăn)
```

---

## 🛠️ 4. Quy Trình Điều Hành Lệnh Mở Rộng (CLI Commands)

### 4.1 Lệnh `init <name>`
1.  Quét kiểm tra sự tồn tại của thư mục mục tiêu tại `MD_korea_learning/`. Nếu đã tồn tại, báo lỗi và dừng.
2.  Tạo cây thư mục chuẩn: `raw/extracts/`, `wiki/concepts/grammar/`, `wiki/concepts/vocabulary/`, `wiki/situations/`, `wiki/queries/`.
3.  Tạo kho chứa git độc lập: `git init` bên trong thư mục.
4.  Viết file `CLAUDE.md` và `.gitignore` để cấu hình quy chuẩn cho Agent.
5.  Thực hiện commit khởi tạo: `git commit -m "init: language learning wiki root"`.

### 4.2 Lệnh `ingest <path>`
1.  Nhận diện tệp đầu vào (chấp nhận `.pdf`, `.png`, `.jpg`).
2.  Chạy mã nguồn OCR trích xuất văn bản thô (giữ nguyên cấu trúc nếu có).
3.  Lưu văn bản trích xuất được vào `raw/extracts/<tên_bài_học>.md` kèm theo frontmatter chứa mã băm `source-sha` và ngày trích xuất để chống trùng lặp.

### 4.3 Lệnh `compile` (Mấu chốt xử lý của Agent)
1.  **Đọc tệp tin thô:** Agent đọc toàn bộ file văn bản thô từ `raw/extracts/`.
2.  **Xử lý nhận thức (Cognitive Processing):**
    *   Lọc sạch tất cả các tiểu từ thừa (ví dụ: chuyển đổi từ bảng từ vựng `사과가` thành từ sạch `사과`).
    *   Tự động phân tích các bẫy biến âm để tạo ra **Bản đồ Âm - Chữ**.
    *   Tự động liên tưởng các từ cùng gốc để tạo ra **Cây gốc Hán-Hàn**.
    *   Thiết kế các kịch bản hội thoại tình huống ngắn cho **Độc thoại Phản xạ**, đồng thời thực hiện **liên kết chéo hai chiều** giữa từ vựng và ngữ pháp có liên quan (ví dụ: gắn link bài ngữ pháp vào câu thoại).
3.  **Tạo file chính thức:** Lưu vào thư mục `wiki/concepts/vocabulary/` hoặc `wiki/concepts/grammar/`.
4.  **Tạo liên kết chéo:** Quét và tự động thêm các wikilinks `[[tên-từ-vựng]]` vào các kịch bản tình huống `s-*.md` có liên quan.
5.  **Commit Git:** Ghi lại lịch sử biên dịch.

### 4.4 Lệnh `study` (Khởi động giao diện học tập)
1.  Kiểm tra cổng rỗi (ví dụ: `3000`).
2.  Khởi chạy song song React Frontend và Express Backend API Server cục bộ.
3.  Mở trình duyệt hiển thị đường link `http://localhost:3000`.

### 4.5 Lệnh `discover --level <level> [--grammar <grammar>] [--vocab <topic>]`
Tìm kiếm tài liệu ngoài tự động khi thiếu hụt tài liệu:
1.  Gửi truy vấn qua API Naver Dictionary hoặc Parallel Web Search đối với cấu trúc ngữ pháp/từ vựng yêu cầu.
2.  Tự động cào (scrape) các thông tin: Ý nghĩa, cách chia đuôi, 5 câu ví dụ thực tế và giải thích ngữ cảnh.
3.  Lưu trữ tệp tin thu được vào `raw/extracts/scraped-<name>.md` để chuẩn bị cho bước `compile`.

### 4.6 Lệnh `exam --generate`
1.  Quét các tệp ngữ pháp và từ vựng đã học trong Obsidian.
2.  Agent (LLM) tự động tổng hợp một đề thi thử trắc nghiệm 25 câu (dựa trên cấu trúc đề thi TOPIK thật).
3.  Tạo tệp Markdown mới tại `wiki/exams/exam-topik-<hash>.md`.

---

## 5. Thuật Toán & Cơ Chế Ôn Tập Ngắt Quãng

### 5.1 Xử lý tách dòng (Parser Separation) và đọc/ghi tệp Markdown:
Bộ phân tích cú pháp `parser.js` sẽ xử lý dòng tin cậy thay vì dùng một biểu thức chính quy (Regex) monolithic dễ vỡ:
1.  Tách dòng bằng ký tự ngăn cách thẻ nhớ `::`.
2.  Dòng bên trái `Left` (Từ gốc + phát âm): Tách từ tiếng Hàn và phiên âm tiếng Việt bằng regex: `/-\s*(.+?)\s*\(\*\*(.+?)\*\*\)/`.
3.  Dòng bên phải `Right` (Nghĩa tiếng Việt + metadata): 
    *   Tách phần nghĩa tiếng Việt và phần comment bằng cách tìm vị trí của `<!--`.
    *   Phần comment chứa metadata ôn tập được phân tích bằng regex nhỏ: `/due\s+(\d{4}-\d{2}-\d{2})|interval\s+(\d+)|ease\s+(\d+)|streak\s+(\d+)/g`.
    *   Trích xuất thêm danh sách từ đồng nghĩa bằng cách tìm cụm `synonyms: [...]` nếu có.

### 5.2 Cơ chế Cache ôn tập (`.study-cache.json`) và Batch Commits:
*   **Đồng bộ mtime:** Khi chạy, API Server so sánh thời gian sửa đổi gần nhất (`mtime`) của các file `.md` với `.study-cache.json` để đồng bộ lại các thẻ bị chỉnh sửa thủ công trong Obsidian (O(1) đọc ghi).
*   **Gộp commit Git (Batch Commit):** 
    *   Hành động sửa file Markdown diễn ra ngay lập tức sau mỗi từ được ôn tập để đảm bảo an toàn dữ liệu.
    *   Hành động `git commit` sẽ được gộp lại và chỉ kích hoạt khi người dùng tắt Web App, hoặc sau mỗi 10 phút, hoặc khi gửi POST đến `/api/session/end`. Điều này bảo vệ tuổi thọ ổ đĩa SSD của học viên.
*   **Ghi file an toàn (Atomic Write):** Ghi nội dung sửa đổi vào một file `.tmp` trước, sau đó đổi tên ghi đè file chính thức để tránh trường hợp mất điện hay tắt app giữa chừng làm hỏng file.

### 5.3 Thuật toán Anki-like (SM-2):
Khi người dùng gõ câu trả lời và nhấn nút kiểm tra trên Web App, 4 nút lựa chọn mức độ ghi nhớ sẽ xuất hiện để cập nhật thông số khoảng lặp tiếp theo ($I_{new}$):

| Nút chọn | Trạng thái | Công thức tính khoảng lặp mới | Mô tả hành vi |
| :--- | :--- | :--- | :--- |
| 🔴 **Again** | Quên từ | $I_{new} = 0$ | Đưa từ vào hàng đợi ôn lại sau 20 phút trong bộ nhớ tạm của React. Ghi ngày `due` là hôm nay. |
| 🟡 **Hard** | Khó | $I_{new} = \max(1, I_{old} \times 1.2)$ | Nhớ mang máng, cần kiểm tra sớm. |
| 🟢 **Good** | Tốt | $I_{new} = \max(3, I_{old} \times 2.5)$ | Trả lời chính xác, giãn khoảng cách lặp. |
| 🔵 **Easy** | Dễ | $I_{new} = \max(7, I_{old} \times 4.0)$ | Thuộc lòng, giãn tối đa. |

---

## 6. Đặc Tả Chi Tiết API Backend (REST API JSON)

### 6.1 Lấy danh sách từ đến hạn ôn tập hôm nay
*   **Endpoint:** `GET /api/cards/due`
*   **Response JSON:**
```json
{
  "totalDue": 12,
  "cards": [
    {
      "filePath": "wiki/concepts/vocabulary/v-14-home-furniture.md",
      "word": "책상",
      "pronunciation": "chaek-sang",
      "meaning": "bàn học/bàn làm việc",
      "tag": "#TOPIK-1",
      "sr": {
        "due": "2026-06-21",
        "interval": 1,
        "ease": 250,
        "streak": 1
      },
      "cognitiveData": {
        "phonetics": "Phát âm thực tế: [책쌍] (chaek-ssang). Quy tắc: Trọng âm hóa.",
        "hanja": "Gốc Hán-Hàn: 책 (Sách) - 상 (Sương/Bàn). Mở rộng: 책장 (Tủ sách), 책방 (Hiệu sách).",
        "dialogue": "A: 책상이 tương thích với [[g-02-eo-ya-hada]] (Phải làm gì).\nB: Độc thoại mẫu: 책상을 정리해야 해요. (Tôi phải sắp xếp bàn học.)"
      }
    }
  ]
}
```

### 6.2 Cập nhật trạng thái sau khi ôn tập
*   **Endpoint:** `POST /api/cards/review`
*   **Request JSON:**
```json
{
  "filePath": "wiki/concepts/vocabulary/v-14-home-furniture.md",
  "word": "책상",
  "rating": 3
}
```
*(rating nhận giá trị: 1 = Again, 2 = Hard, 3 = Good, 4 = Easy)*
*   **Response JSON:**
```json
{
  "status": "success",
  "word": "책상",
  "nextReview": "2026-06-24",
  "newInterval": 3,
  "newEase": 250,
  "newStreak": 2
}
```

### 6.3 Nộp bài thi trắc nghiệm
*   **Endpoint:** `POST /api/exams/submit`
*   **Request JSON:**
```json
{
  "examId": "exam-midterm-level-1",
  "answers": {
    "q01": 1,
    "q02": 3
  }
}
```
*   **Response JSON:**
```json
{
  "score": 50.0,
  "results": [
    {
      "id": "q01",
      "isCorrect": true,
      "correctAnswer": 1,
      "userAnswer": 1
    },
    {
      "id": "q02",
      "isCorrect": false,
      "correctAnswer": 0,
      "userAnswer": 3,
      "grammarLink": "wiki/concepts/grammar/g-05-wi-arae.md",
      "explanation": "Sai. Đáp án đúng là 위. Lỗi sai về hướng vị trí. Vui lòng học lại bài [[g-05-wi-arae]]"
    }
  ]
}
```

---

## 7. Giao Diện Người Dùng (UI/UX) & Phát Âm TTS, Luyện Nói STT

### 7.1 Mức độ thử thách gõ chính tả (Graded Challenge Levels)
Để khắc phục việc học viên chưa quen gõ chữ tiếng Hàn, Web App hỗ trợ 2 mức độ thử thách ôn luyện tự động:
1.  **Thử thách Trung bình (Medium Challenge):** 
    *   Hiển thị nghĩa tiếng Việt + Loa đọc từ tiếng Hàn.
    *   Hiển thị độ dài từ và các gợi ý âm tiết trống (ví dụ: từ `책상` sẽ hiện dưới dạng `_ _` để chỉ ra từ có 2 âm tiết, hoặc tùy chọn hiển thị phụ âm đầu `ㅊ ㅅ`).
2.  **Thử thách Khó (Hard Challenge - Active Recall chuẩn):**
    *   Chỉ hiển thị nghĩa tiếng Việt + Loa đọc từ tiếng Hàn.
    *   Ô nhập liệu trống hoàn toàn, yêu cầu học viên phải tự gõ chính xác 100% chữ Hangul không có gợi ý.

### 7.2 Bộ phát âm TTS & Tương phản phát âm biến âm
*   Trình duyệt gọi trực tiếp bộ máy phát âm SpeechSynthesis của hệ thống bằng Web Speech API để tự động nói giọng Hàn Quốc bản địa chuẩn xác cho mọi từ vựng mới.
*   **Nút Loa so sánh (Contrastive Pronunciation):** Hỗ trợ 2 nút loa phát âm cạnh nhau cho các từ có bẫy biến âm:
    *   *Nút Loa 1 (Viết thế nào - Phát âm chữ gốc):* Đọc chậm từng âm tiết thô (ví dụ: `g-a-t-i` cho `같이`).
    *   *Nút Loa 2 (Đọc thế nào - Phát âm chuẩn bản ngữ):* Phát âm chuẩn biến âm tự nhiên (ví dụ: `gachi` cho `같이`).

### 7.3 Luyện nói đàm thoại (Interactive Speaking Mode)
*   **TTS đàm thoại:** Trình duyệt phát âm giọng nhân vật A.
*   **Nhận diện Speech-to-Text (STT):** Trình duyệt tự mở mic bằng API của trình duyệt:
```javascript
const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
recognition.lang = 'ko-KR'; // Lắng nghe tiếng Hàn
recognition.onresult = (event) => {
  const speechToTextResult = event.results[0][0].transcript;
  // Gửi text này lên backend để so sánh và chấm điểm
};
```
*   **Giao diện bong bóng hội thoại:** Hiển thị dưới dạng một khung chat đàm thoại thực tế. Người dùng nhấn nút Giữ để nói (Hold to Talk) để thực hành phát âm.

### 7.4 Luyện thi giả lập (Exam Mode Dashboard)
*   Hiển thị đồng hồ đếm ngược (Timer). Bảng điều hướng câu hỏi ở sidebar bên phải giúp người dùng dễ dàng nhảy đến câu chưa làm.
*   Báo cáo chi tiết sau khi nộp bài: Hiển thị biểu đồ chẩn đoán các chủ đề ngữ pháp bị sai nhiều nhất kèm theo hyperlink mở trực tiếp bài học đó trong Obsidian.

---

## 8. Cơ Chế Lockfile Bảo Vệ Đồng Thì (Concurrency)

Để bảo vệ tránh việc hai phiên làm việc hoặc hai tác vụ chỉnh sửa file Markdown cùng lúc gây mất mát dữ liệu, file `.lock` được đặt ở thư mục gốc của Wiki chứa cấu trúc:
```json
{
  "pid": 5831,
  "timestamp": 1706000000,
  "operation": "compile"
}
```
*   Mọi lệnh ghi file của API Server hoặc lệnh `compile` của Agent đều phải kiểm tra và khóa file `.lock`.
*   Nếu phát hiện file `.lock` đã được khóa bởi một PID đang hoạt động, tác vụ sẽ báo lỗi `LockHeld` và dừng lại an toàn.
*   Nếu PID trong file lock không còn tồn tại trong hệ thống (Stale Lock), Agent sẽ tự giải phóng và chiếm quyền ghi tệp tin.
