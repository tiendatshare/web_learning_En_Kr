## Hot Context
Language Learning Wiki Plugin and Study App fully operational. Added English vocabulary database expansion consisting of 12 core 4000 Words books files (1,200 words) and 12 IELTS/Mindset files (8,697 words), bringing the total database size to 9,897 active recall flashcards. Optimized Express server to ignore raw `_raw_*.md` files in cache sync and API routing to prevent empty topic select issues.

## Learned Constraints
- PDF is a scanned image PDF. Extracted 100% of textbook words (17,031 raw occurrences) by rendering pages (16-293) and scanning using **Windows Native Media OCR via `winsdk`** in Python, avoiding external Tesseract-OCR dependencies and achieving a massive ~0.33s/page OCR speed.
- All files are securely placed under `t:\Topik\giao trình kyung hee\MD_korea_learning\` and `t:\Topik\giao trình kyung hee\MD_english_learning\`.
- Pronunciations use Vietnamese natural spellings (e.g. `xa-gwa`, `ga-t-xi`, `im-ni-da`) and chunking progressions are explicitly designed for Vietnamese native speakers.
- Paragraph translations are strictly interlinear and gloss-oriented.
- Vocabulary is organized as a Neural Word Association Network with Obsidian-friendly Spaced Repetition double colon (`::`) cards.
- Grammar file names on Windows cannot contain illegal characters: `\ / : * ? " < > |`. All `/` are replaced with `-` and `?` is removed.
- **Anti-Boilerplate & Auto-Debate Loop**: Whenever generating educational content, NEVER use generic placeholders like `(Ví dụ đúng)`. Content must be real. After drafting, the agent must silently run an internal 'Debate' to find pedagogical gaps (e.g., missing Pronunciation Rules, Irregular verbs, Cultural nuances) and automatically revise the content. Every grammar file must include `⚠️ Bẫy Biến Âm & Bất Quy Tắc`. Every vocab file must include `🇰🇷 Văn Hóa Ứng Dụng`. The agent loops autonomously without waiting for user permission.
- **Cache Key Path Consistency**: The Express study-app server stores cache keys as paths relative to `workspaceRoot` (e.g. `MD_korea_learning/wiki/concepts/vocabulary/v-01.md`). ALL endpoints that look up cache keys MUST use the same prefix format. Never construct cache keys with a different prefix than what `syncCache()` generates.
- **Không ghi đè mù quáng tài liệu thiết kế/kế hoạch (No Blind Overwriting of Specs/Plans)**: Khi cập nhật các tệp tin Spec (`docs/superpowers/specs/`) hoặc Plan (`docs/superpowers/plans/`), Agent BẮT BUỘC phải đọc nội dung tệp hiện tại bằng `view_file` trước để đối chiếu tất cả các mục/đặc tả cũ. Nghiêm cấm việc ghi đè toàn bộ tệp mới mà không chạy danh sách kiểm tra đối chiếu (merge checklist), tránh việc vô tình xóa mất các chi tiết kỹ thuật/sư phạm quan trọng đã được phê duyệt ở vòng trước.
- **Windows CMD Batch Redirection & Parsing Rules**: 
  - Trong các khối lệnh ngoặc đơn (như vòng lặp `for ... do ( ... )`), tuyệt đối tránh đặt dấu ngoặc đơn lồng trong chuỗi text hiển thị (ví dụ: `echo (PID: %%a)`), nếu không sẽ làm hỏng trình biên dịch.
  - Sử dụng `rem` thay vì `::` cho chú thích để tránh các lỗi nhảy nhãn lạ.
  - Sử dụng lệnh `ping 127.0.0.1 -n <giây+1> >nul` thay thế cho lệnh `timeout` để đảm bảo trễ hoạt động trơn tru trong môi trường console không tương tác (không hỗ trợ Input redirection).
- **Exclude Raw Files from Cache**: Raw files (`_raw_*.md`) do not contain Spaced Repetition flashcards and should be filtered out from synchronization and topics endpoints to prevent empty list renders on client.

## Architecture Decisions
- **Karpathy-Style LLM Wiki**: Separating concerns into `wiki/concepts/grammar/` (individual grammars `g-*.md`) and `wiki/concepts/vocabulary/` (vocabulary topics `v-*.md`), and `wiki/queries/` (dynamic answers to user questions), enabling compounding knowledge.
- **INDEX.md dashboard**: A single entry point mapping the 50 grammars, vocabulary topics, and filed queries.
- **AGENTS.md hiến pháp**: Establishes a permanent rule file so that future AI models and tools know exactly how to maintain and auto-update the wiki when the user asks questions.

## Wiki Index
- [[MD_korea_learning/wiki/index.md]] — Korean Index and Dashboard (Active ✅)
- [[MD_english_learning/wiki/index.md]] — English Index and Dashboard (Active ✅)
- [[MD_korea_learning/AGENTS.md]] — Wiki maintenance guidelines and automated update instructions (Active ✅)
- [[MD_korea_learning/grammar_guide.md]] — Functional Grammar Directory (Active ✅)
- [[MD_korea_learning/wiki/concepts/grammar/]] — 50 individual grammar concept files with Korean names (Active ✅)
- [[MD_korea_learning/wiki/concepts/vocabulary/]] — 24 Korean vocabulary files (Active ✅)
- [[MD_english_learning/wiki/concepts/vocabulary/]] — 24 English vocabulary files (12 fundamental topics + 12 IELTS topics with 9,897 cards) (Active ✅)
- [[MD_korea_learning/wiki/situations/s-01-shopping-clothes-weather.md]] to [[MD_korea_learning/wiki/situations/s-13-hair-salon-haircut.md]] — 13 Korean life situations (Active ✅)




