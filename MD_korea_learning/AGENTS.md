# AGENTS.md — Quy tắc duy trì và tự động hóa Kyung Hee LLM Wiki

Tệp này quy định luật hoạt động và bảo trì hệ thống học liệu động này. Mọi Agent AI (bao gồm Antigravity và các subagent) khi làm việc với hệ thống này phải tuân thủ nghiêm ngặt các hướng dẫn dưới đây.

---

## 1. Kiến trúc Hệ thống (System Architecture)

```
MD/
├── docs/
│   └── specs/                ← Đặc tả thiết kế dự án
├── AGENTS.md                 ← Quy tắc bảo trì này (Bản hiến pháp của Wiki)
├── wiki/                     ← Thư viện tri thức (LLM viết, người đọc)
│   ├── index.md              ← Bản đồ mục lục trung tâm: liên kết toàn bộ tài liệu
│   ├── log.md                ← Append-only: ghi lại mọi hoạt động cập nhật/truy vấn
│   ├── concepts/             ← Các trang tri thức độc lập:
│   │   ├── g-*.md            ← File ngữ pháp (Ví dụ: g-01-a-eo-yeo-ya-hada.md)
│   │   └── v-*.md            ← File từ vựng theo chủ đề (Ví dụ: v-weather.md)
│   └── queries/              ← File lưu câu trả lời/bài tập động theo câu hỏi của người học
```

---

## 2. Quy trình Cập nhật & Tiến hóa Wiki khi người dùng đặt câu hỏi

Khi người học đặt câu hỏi mở rộng hoặc yêu cầu bài tập mới (ví dụ: *"Giải thích thêm cách dùng bất quy tắc của ㄷ"* hoặc *"Cho tôi 5 câu dịch Việt-Hàn về chủ đề Thời tiết"*):

1. **Đọc Mục lục (`wiki/index.md`)**: Xác định các file ngữ pháp (`g-*.md`) hoặc từ vựng (`v-*.md`) liên quan đến câu hỏi.
2. **Đọc tệp Tri thức liên quan**: Đọc chi tiết nội dung các tệp đã xác định ở bước 1 để lấy ngữ cảnh và dữ liệu gốc.
3. **Sinh câu trả lời Sư phạm**:
   - Giải thích cặn kẽ dưới góc độ giáo viên.
   - Biên soạn bài tập/câu ví dụ có kèm **Phiên âm tiếng Việt** và **Dịch xen kẽ trong ngoặc đơn** cho các câu tiếng Hàn.
4. **Lưu trữ câu trả lời**:
   - Ghi câu trả lời thành một file markdown mới trong thư mục `wiki/queries/` với định dạng tên `q-<tên-chủ-đề-ngắn-tiếng-viet-khong-dau>.md`.
5. **Thiết lập Liên kết hai chiều (Backlinks)**:
   - Thêm liên kết `[[wiki/queries/q-*.md]]` vào phần "Xem thêm / Bài tập mở rộng" của các file tri thức liên quan ở thư mục `concepts/`.
6. **Cập nhật Mục lục (`wiki/index.md`)**: Thêm đường link của câu hỏi mới vào phần `## Recent Queries` của tệp index.
7. **Ghi nhận lịch sử (`wiki/log.md`)**: Ghi nhận hoạt động truy vấn.

---

## 3. Quy chuẩn Định dạng nội dung bắt buộc

### A. Định dạng Ngữ pháp (`wiki/concepts/g-*.md`)
- **Tên file**: Bắt đầu bằng `g-` + số thứ tự (2 chữ số) + tên cấu trúc (kebab-case). Ví dụ: `g-01-a-eo-yeo-ya-hada.md`.
- **Cấu trúc**: Phải có phần "Giải thích của giáo viên", "Bảng chia đuôi từ", "So sánh/Lưu ý đặc biệt", và "Liên kết Từ vựng ứng dụng".

### B. Định dạng Từ vựng (`wiki/concepts/v-*.md`)
- **Tên file**: Bắt đầu bằng `v-` + tên chủ đề (kebab-case). Ví dụ: `v-weather.md`.
- **Bảng Flashcard**: Bắt buộc phải có 4 cột: `Từ tiếng Hàn | Phiên âm tiếng Việt (Phát âm thực tế) | Nghĩa tiếng Việt | Trạng thái nhớ`.
- **Phát triển Cụm từ (Chunking)**: Phải có sơ đồ phát triển từ `Từ đơn` -> `Cụm từ` -> `Câu hoàn chỉnh`.
- **Đoạn văn dịch xen kẽ**: Phải viết đoạn văn bằng tiếng Hàn, ngay sau mỗi từ/cụm từ tiếng Hàn phải có phần dịch nghĩa tiếng Việt đặt trong ngoặc đơn. *Ví dụ*: `오늘 (hôm nay) 날씨가 (thời tiết) 아주 (rất) 좋습니다 (tốt).`

---

## 4. Nhật ký Hoạt động (`wiki/log.md`)
Mỗi lần có thao tác ghi/cập nhật, phải append một dòng vào tệp log với cú pháp:
`[YYYY-MM-DD HH:MM] <ingest|query|update> | <mô tả ngắn bằng tiếng Việt>`
