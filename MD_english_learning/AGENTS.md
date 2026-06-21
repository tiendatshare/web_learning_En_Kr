# AGENTS.md — Quy tắc duy trì và tự động hóa English Learning LLM Wiki

Tệp này quy định luật hoạt động và bảo trì hệ thống học liệu tiếng Anh. Mọi Agent AI (bao gồm Antigravity và các subagent) khi làm việc với hệ thống này phải tuân thủ nghiêm ngặt các hướng dẫn dưới đây.

---

## 1. Kiến trúc Hệ thống (System Architecture)

```
MD_english_learning/
├── AGENTS.md                 ← Quy tắc bảo trì này (Bản hiến pháp của Wiki)
├── wiki/                     ← Thư viện tri thức (LLM viết, người đọc)
│   ├── index.md              ← Bản đồ mục lục trung tâm: liên kết toàn bộ tài liệu
│   ├── log.md                ← Append-only: ghi lại mọi hoạt động cập nhật/truy vấn
│   ├── concepts/             ← Các trang tri thức độc lập:
│   │   ├── vocabulary/
│   │   │   ├── v-*.md        ← File từ vựng theo chủ đề (Ví dụ: v-01-people-feelings.md)
│   │   │   └── v-ielts-*.md  ← File từ vựng IELTS theo Cambridge (Ví dụ: v-ielts-cam08.md)
│   │   └── grammar/
│   │       └── g-*.md        ← File ngữ pháp (Ví dụ: g-01-tenses-overview.md)
│   ├── situations/           ← Hội thoại giao tiếp thực tế
│   │   └── s-*.md            ← File tình huống (Ví dụ: s-01-greetings.md)
│   ├── exam_prep/            ← Tài liệu luyện thi IELTS
│   │   └── ielts-*.md        ← Chiến lược, cấu trúc, cụm từ band cao
│   └── queries/              ← File lưu câu trả lời/bài tập động
│       └── q-*.md            ← Câu trả lời cho câu hỏi mở rộng của người học
```

---

## 2. Quy trình Cập nhật & Tiến hóa Wiki khi người dùng đặt câu hỏi

Khi người học đặt câu hỏi mở rộng hoặc yêu cầu bài tập mới (ví dụ: *"Giải thích thêm cách dùng Present Perfect"* hoặc *"Cho tôi 5 câu dịch Việt-Anh về chủ đề Travel"*):

1. **Đọc Mục lục (`wiki/index.md`)**: Xác định các file ngữ pháp (`g-*.md`), từ vựng (`v-*.md`), hoặc tình huống (`s-*.md`) liên quan đến câu hỏi.
2. **Đọc tệp Tri thức liên quan**: Đọc chi tiết nội dung các tệp đã xác định ở bước 1 để lấy ngữ cảnh và dữ liệu gốc.
3. **Sinh câu trả lời Sư phạm**:
   - Giải thích cặn kẽ dưới góc độ giáo viên, bằng **tiếng Việt**.
   - Biên soạn bài tập/câu ví dụ có kèm **Phiên âm IPA** và **Dịch nghĩa tiếng Việt** cho các câu tiếng Anh.
4. **Lưu trữ câu trả lời**:
   - Ghi câu trả lời thành một file markdown mới trong thư mục `wiki/queries/` với định dạng tên `q-<tên-chủ-đề-ngắn-tiếng-viet-khong-dau>.md`.
5. **Thiết lập Liên kết hai chiều (Backlinks)**:
   - Thêm liên kết `[[wiki/queries/q-*.md]]` vào phần "Xem thêm / Bài tập mở rộng" của các file tri thức liên quan ở thư mục `concepts/`.
6. **Cập nhật Mục lục (`wiki/index.md`)**: Thêm đường link của câu hỏi mới vào phần `## Recent Queries` của tệp index.
7. **Ghi nhận lịch sử (`wiki/log.md`)**: Ghi nhận hoạt động truy vấn.

---

## 3. Quy chuẩn Định dạng nội dung bắt buộc

### A. Định dạng Từ vựng (`wiki/concepts/vocabulary/v-*.md`)
- **Tên file**: Bắt đầu bằng `v-` + số thứ tự (2 chữ số) + tên chủ đề (kebab-case). Ví dụ: `v-01-people-feelings.md`.
- **Flashcard Spaced Repetition**: Cú pháp `- word /IPA/ :: nghĩa tiếng Việt | #IELTS-6`
  - Dấu `::` phân tách từ và nghĩa (tương thích study-app parser)
  - Phiên âm IPA đặt trong `/ /` (ví dụ: `/əˈbændən/`)
  - Tag cấp độ IELTS: `#IELTS-4` đến `#IELTS-9`
- **Cấu trúc file**: Phải có các phần:
  1. **Bảng Flashcard Spaced Repetition** — Danh sách flashcard `::` đầy đủ
  2. **Chunking Progression** — Từ đơn → Cụm từ (Collocations) → Câu hoàn chỉnh
  3. **Mạng Liên tưởng Nơ-ron** — Đồng nghĩa, trái nghĩa, Word Family, Collocations phổ biến
  4. **Bài tập Đọc Ứng dụng** — Đoạn văn tiếng Anh dịch xen kẽ tiếng Việt

### B. Định dạng Từ vựng IELTS (`wiki/concepts/vocabulary/v-ielts-*.md`)
- **Tên file**: `v-ielts-camXX.md` hoặc `v-ielts-mindset-4-5.md`
- **Chia theo passage/test**: Mỗi passage có nhóm từ vựng riêng
- **Context sentence**: Câu ví dụ lấy từ passage gốc
- Flashcard `::` tương tự phần A

### C. Định dạng Ngữ pháp (`wiki/concepts/grammar/g-*.md`)
- **Tên file**: Bắt đầu bằng `g-` + số thứ tự (2 chữ số) + tên cấu trúc (kebab-case). Ví dụ: `g-01-tenses-overview.md`.
- **Cấu trúc**: Phải có phần "Giải thích của giáo viên", "Công thức & Bảng chia", "Bẫy Lỗi sai & So sánh", và "Liên kết Từ vựng ứng dụng".

### D. Định dạng Hội thoại (`wiki/situations/s-*.md`)
- **Tên file**: Bắt đầu bằng `s-` + số thứ tự (2 chữ số) + tên tình huống (kebab-case). Ví dụ: `s-01-greetings-introductions.md`.
- **Hội thoại song ngữ**: Câu tiếng Anh kèm phiên âm IPA + dịch tiếng Việt bên dưới
- **Từ vựng bổ trợ**: Flashcard `::` cho các từ khó trong hội thoại
- **Biến thể tình huống**: Các cách diễn đạt khác cho cùng ý

### E. Định dạng Luyện thi IELTS (`wiki/exam_prep/*.md`)
- **Tên file**: `ielts-writing-guide.md`, `ielts-academic-phrases.md`, v.v.
- **Cấu trúc**: Chiến lược làm bài → Cấu trúc câu Band 7+ → Từ vựng chủ đề → Bài tập thực hành

---

## 4. Nhật ký Hoạt động (`wiki/log.md`)
Mỗi lần có thao tác ghi/cập nhật, phải append một dòng vào tệp log với cú pháp:
`[YYYY-MM-DD HH:MM] <ingest|query|update> | <mô tả ngắn bằng tiếng Việt>`

---

## 5. Tương thích Study-app

### Cú pháp Flashcard
Giữ nguyên cú pháp `::` tương thích parser hiện có tại `language-wiki/study-app/server/parser.js`:
```
- word /IPA/ :: nghĩa tiếng Việt | #IELTS-6
```

### Spaced Repetition Metadata
Khi study-app ghi nhận tiến độ ôn tập, metadata SR được append vào cuối dòng flashcard dưới dạng HTML comment:
```
- abandon /əˈbændən/ :: từ bỏ, bỏ rơi | #IELTS-6 <!-- sr: due 2026-06-28 interval 7 ease 250 streak 3 -->
```

### TTS Voice
- Tiếng Anh sử dụng `en-US` (thay vì `ko-KR` của tiếng Hàn)
- Study-app tự động chuyển voice theo ngôn ngữ hiện tại
