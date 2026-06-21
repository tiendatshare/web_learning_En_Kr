# 🧠 Đại Tu Hệ Thống Học Tiếng Hàn — Kiến Trúc "Ultralearning 7+6 Tầng Nhận thức"

> **Mục tiêu tối thượng**: TOPIK 5 trong 6 tháng
> **Ngày tạo**: 2026-06-07
> **Trạng thái**: Đang chờ duyệt

---

## 1. Bối cảnh & Động lực

### 1.1 Vấn đề hiện tại
Hệ thống Obsidian Wiki hiện tại có **24 file vocabulary** và **50 file grammar** nhưng:

1. **Vocabulary**: Mạng liên tưởng vẫn là "1 suy 3" (chỉ mở rộng 3 từ/từ gốc), thiếu trái nghĩa/đồng nghĩa trong bảng chính, thiếu mạng đệ quy nhiều tầng.
2. **Grammar**: Bảng chia đuôi sai cấu trúc (ví dụ `가명사 + 은는` vô nghĩa), phần so sánh quá sơ sài, hội thoại không gắn với ngữ pháp đang học.
3. **Thiếu hoàn toàn**: Feynman explanation, Active Recall quiz, Mnemonics, TOPIK pattern recognition, Difficulty tags.

### 1.2 Phương pháp khoa học được tích hợp (11 phương pháp)

| # | Phương pháp | Nguồn gốc | Áp dụng cho |
|---|------------|-----------|-------------|
| 1 | Spaced Repetition (Leitner) | Ebbinghaus Forgetting Curve | Vocab `::` cards |
| 2 | Active Recall / Retrieval Practice | Roediger & Karpicke (2006) | Quiz tự kiểm tra |
| 3 | Semantic Mapping / Word Association Network | Cognitive Psychology | Mạng nơ-ron đệ quy |
| 4 | Feynman Technique | Richard Feynman | Giải thích đơn giản |
| 5 | Elaborative Interrogation | Dunlosky et al. (2013) | Tự hỏi "Tại sao?" |
| 6 | Keyword Method / Mnemonics | Atkinson & Raugh (1975) | Mẹo ghi nhớ siêu tốc |
| 7 | Dual Coding | Paivio (1986) | Hình ảnh + từ |
| 8 | Interleaving | Kornell & Bjork (2008) | Trộn chủ đề khi ôn |
| 9 | Contextual Learning | Nation (2001) | Từ trong câu/bài |
| 10 | Directness | Scott Young - Ultralearning | Thực hành trực tiếp |
| 11 | Corrective Feedback | Scott Young - Ultralearning | Phân tích lỗi sai |

---

## 2. Kiến trúc File Vocabulary Mới — "8 Tầng Nhận thức"

Mỗi file `v-XX-*.md` sẽ có cấu trúc sau:

### Tầng 1: 🎴 Flashcard Hub (Spaced Repetition + Leitner)
```
- 봄 (bom) :: mùa xuân | #TOPIK-1 | ⚔️ ↔ 가을 (thu) | 🔄 ≈ 봄철 (mùa xuân)
```
**Thay đổi so với hiện tại:**
- ✅ Thêm **tag TOPIK level** (`#TOPIK-1`, `#TOPIK-3`, `#TOPIK-5`)
- ✅ Thêm **trái nghĩa** (`⚔️ ↔`) ngay trong thẻ
- ✅ Thêm **đồng nghĩa** (`🔄 ≈`) ngay trong thẻ
- ✅ Giữ nguyên format `::` tương thích Obsidian SR + Anki export

### Tầng 2: 🧠 Mạng Nơ-ron Đệ quy 4 Tầng (Semantic Mapping)
```
🌳 Từ gốc: 계절 (mùa)
├── 🟢 Tầng 1: 봄 (xuân) / 여름 (hè) / 가을 (thu) / 겨울 (đông)
│   ├── ⚔️ Trái nghĩa: 봄 ↔ 가을 | 여름 ↔ 겨울
│   └── 🔄 Đồng nghĩa: 봄 ≈ 봄철 | 겨울 ≈ 겨울철
├── 🟡 Tầng 2: 덥다 (nóng) / 춥다 (lạnh) / 따뜻하다 (ấm) / 시원하다 (mát)
│   ├── ⚔️ Trái nghĩa: 덥다 ↔ 춥다 | 따뜻하다 ↔ 시원하다
│   └── 🔄 Đồng nghĩa: 덥다 ≈ 무덥다 | 시원하다 ≈ 선선하다
├── 🟠 Tầng 3: 쾌적하다 (dễ chịu) / 불쾌하다 (khó chịu) / 선선하다 (hơi mát)
│   └── ⚔️ Trái nghĩa: 쾌적하다 ↔ 불쾌하다
└── 🔴 Tầng 4: 에어컨 (điều hòa) / 히터 (máy sưởi) / 우산 (ô/dù)
    └── 🧠 Liên quan: hành động ứng phó với thời tiết
```
**Thay đổi so với hiện tại:**
- ✅ Mở rộng từ 2-3 từ cốt lõi → **TẤT CẢ từ gốc** trong file đều có mạng đệ quy
- ✅ 4 tầng liên tưởng (thay vì 1 tầng "1 suy 3")
- ✅ Trái nghĩa + Đồng nghĩa ở **MỌI tầng**, không chỉ tầng 1
- ✅ Hiển thị dạng cây (tree) trực quan

### Tầng 3: 💡 Feynman Zone (Giải thích Đơn giản)
```
### 💡 Feynman: Giải thích "계절" cho trẻ 5 tuổi
> Hàn Quốc có 4 mùa giống Việt Nam nhưng RÕ RÀNG hơn nhiều.
> - 봄 (xuân): hoa nở, dị ứng phấn hoa 꽃가루
> - 여름 (hè): nóng kinh khủng, mồ hôi 땀 chảy, phải bật 에어컨
> - 가을 (thu): lá đỏ 단풍 đẹp nhất năm, trời cao 천고마비
> - 겨울 (đông): tuyết 눈 rơi, lạnh -15°C, mặc 4 lớp áo
>
> 💎 GHI NHỚ: Hàn Quốc = 4 mùa cực đoan. Việt Nam 2 mùa mưa/nắng.
```

### Tầng 4: ❓ Active Recall Arena (Tự Hỏi Tự Trả Lời)
```
> [!QUESTION] 🧪 Câu 1: Elaborative Interrogation
> **Tại sao** người Hàn nói "천고마비" (trời cao ngựa béo) khi mô tả mùa thu?
> %%ANSWER: Vì mùa thu Hàn Quốc trời rất trong xanh (cao) và thức ăn phong phú
> nên ngựa ăn nhiều (béo). Thành ngữ gốc Hán.%%

> [!QUESTION] 🧪 Câu 2: So sánh
> **So sánh**: 덥다 và 무덥다 — khác nhau thế nào? Khi nào dùng từ nào?
> %%ANSWER: 덥다 = nóng (chung). 무덥다 = oi bức/nóng ẨM (humidity cao).
> Dùng 무덥다 khi trời vừa nóng vừa ẩm, thường vào 장마 (mùa mưa).%%
```
**Lưu ý:** Dùng `%%...%%` (Obsidian comment) để ẩn đáp án → bạn TỰ suy nghĩ trước khi click mở.

### Tầng 5: 🎯 Mnemonic Lab (Mẹo Ghi nhớ Siêu tốc)
```
### 🎯 Mẹo ghi nhớ (Keyword Method)
| Từ Hàn | Phiên âm | Liên tưởng âm Việt | Câu chuyện ghi nhớ |
|--------|---------|-------------------|-------------------|
| 겨울 | gyơ-ul | "giơ ủ" | Mùa đông lạnh quá, GIƠI tay ra ỦI nóng! |
| 따뜻하다 | tta-ttưt-ha-da | "tạt tất" | Trời ẤM ÁP, TẠT nước TẤT cả ra ngoài chơi! |
| 우산 | u-xan | "ủ xàn" | Trời mưa, ÚP SÀN = cầm Ô CHE! |
```

### Tầng 6: 🔗 Grammar Link Bridge (Cầu nối Ngữ pháp)
```
### 🔗 Ngữ pháp hay đi kèm chủ đề này
- 날씨가 추워요 → Dùng [[g-12-동사-형용사 + 아-어요]] + [[g-16-ㅂ 불규칙]]
- 겨울보다 여름이 더 좋아요 → Dùng [[g-32-명사 + 보다]] (so sánh)
- 비가 오니까 우산을 가져가세요 → Dùng [[g-48-동사-형용사 + (으)니까 1]]
```

### Tầng 7: 🎭 Situational Challenge (Thử thách Giao tiếp)
```
### 🎭 Thử thách: TỰ nghĩ câu trả lời TRƯỚC khi xem đáp án!
> **Tình huống**: Bạn đang ở Seoul vào tháng 7. Đồng nghiệp hỏi:
> "오늘 날씨가 어때요?" (Hôm nay thời tiết thế nào?)
>
> 🎤 **Bạn trả lời**: ___________
>
> %%GỢI Ý: 오늘 아주 더워요. 습도도 높아요. 에어컨을 켜 주세요.
> (Hôm nay rất nóng. Độ ẩm cũng cao. Xin hãy bật điều hòa.)%%
```

### Tầng 8: 📝 TOPIK Pattern Recognition (Nhận dạng đề thi)
```
### 📝 Dạng đề TOPIK sử dụng từ vựng này
> **[TOPIK I - 듣기]** Nghe và chọn đáp án đúng:
> 여자: 오늘 날씨가 어때요?
> 남자: ________________
> ① 네, 날씨가 아주 추워요. ② 네, 커피를 마셔요.
> ③ 아니요, 학교에 가요. ④ 네, 한국 사람이에요.
>
> %%ĐÁP ÁN: ① — Vì câu hỏi về thời tiết, đáp án phải liên quan đến 날씨.%%
```

---

## 3. Kiến trúc File Grammar Mới — "6 Tầng Sư phạm"

Mỗi file `g-XX-*.md` sẽ có cấu trúc sau:

### Tầng 1: 💡 Feynman Explanation (Giải thích Siêu đơn giản)
```
## 💡 1. Feynman: Hiểu trong 30 giây
> **은/는** giống như khi bạn nói "CÒN tôi thì..." trong tiếng Việt.
> Nó ĐÁNH DẤU chủ đề bạn đang nói đến, đặc biệt khi SO SÁNH 2 thứ.
>
> 🎯 Công thức siêu đơn giản:
> - "A는 X. B는 Y." = "A thì X. CÒN B thì Y."
> - Ví dụ: "커피는 좋아요. 맥주는 싫어요." = "Cà phê thì thích. CÒN bia thì ghét."
```

### Tầng 2: 📐 Visual Formula (Công thức Trực quan + Bảng chia)
```
## 📐 2. Công thức & Bảng chia đuôi

### Quy tắc kết hợp:
| Điều kiện | Dùng | Ví dụ |
|-----------|------|-------|
| Danh từ kết thúc bằng **phụ âm** (받침) | **은** | 학생 + 은 → 학생은 |
| Danh từ kết thúc bằng **nguyên âm** (không 받침) | **는** | 나 + 는 → 나는 |

### Ví dụ thực tế:
| Câu Hàn | Phiên âm | Dịch xen kẽ | Nghĩa |
|---------|---------|-------------|-------|
| 저는 학생이에요. | jơ-nưn hak-saeng-i-e-yo | 저(tôi)+는(thì) 학생(sinh viên)+이에요(là) | Tôi thì là sinh viên. |
| 한국은 춥고, 베트남은 더워요. | han-guk-ưn chup-go, bê-thư-nam-ưn dơ-wơ-yo | 한국(Hàn)+은(thì) 춥고(lạnh và), 베트남(VN)+은(thì) 더워요(nóng) | Hàn thì lạnh, còn VN thì nóng. |
```

### Tầng 3: ⚖️ Contrast Lab (So sánh Chi tiết)
```
## ⚖️ 3. So sánh với ngữ pháp dễ nhầm

### 은/는 vs 이/가 — Phân biệt CHI TIẾT:
| Tiêu chí | 은/는 (chủ đề) | 이/가 (chủ ngữ) |
|----------|---------------|----------------|
| Chức năng | Đánh dấu chủ đề đang nói | Đánh dấu ai/cái gì LÀM hành động |
| Sắc thái | So sánh, đối chiếu | Thông tin MỚI, nhấn mạnh |
| Ví dụ | 저**는** 학생이에요 (TÔI thì là SV) | 제**가** 학생이에요 (CHÍNH TÔI là SV) |
| Khi nào | Giới thiệu bản thân, so sánh | Trả lời "AI?", nhấn mạnh |
```

### Tầng 4: 🚨 Common Mistake ER (Lỗi sai Người Việt hay mắc)
```
## 🚨 4. Lỗi sai thường gặp của NGƯỜI VIỆT

> [!WARNING]
> **Lỗi #1**: Dùng 은/는 khi cần 이/가
> - ❌ "누가 학생이에요?" → "저**는** 학생이에요" (SAI — vì đang trả lời "AI?")
> - ✅ "누가 학생이에요?" → "제**가** 학생이에요" (ĐÚNG — nhấn mạnh "chính tôi")
>
> **Lỗi #2**: Quên 은/는 khi so sánh
> - ❌ "한국 추워요. 베트남 더워요." (thiếu tiểu từ)
> - ✅ "한국**은** 추워요. 베트남**은** 더워요." (có 은 → rõ ràng so sánh)
>
> **Tại sao người Việt hay sai?** Vì tiếng Việt không có tiểu từ chủ đề/chủ ngữ.
> Ta nói "Tôi là sinh viên" không cần đánh dấu gì. Tiếng Hàn BẮT BUỘC phải có.
```

### Tầng 5: ❓ Active Recall Quiz (Tự Kiểm tra)
```
## ❓ 5. Tự kiểm tra (Active Recall)

> [!QUESTION] Câu 1: Điền 은 hoặc 는
> "사과___ 좋아요. 바나나___ 싫어요."
> %%ĐÁP ÁN: 사과**는** 좋아요. 바나나**는** 싫어요.
> (Táo thì thích. Chuối thì ghét.) — Dùng 는 vì 사과 kết thúc nguyên âm.%%

> [!QUESTION] Câu 2: 은/는 hay 이/가?
> A: "누가 일본 사람이에요?" B: "미나 ___ 일본 사람이에요."
> %%ĐÁP ÁN: 미나**가** — Vì đang trả lời câu hỏi "AI?" → dùng 이/가 nhấn mạnh.%%
```

### Tầng 6: 🎭 Real-Life Dialogues (Hội thoại Gắn với Ngữ pháp)
```
## 🎭 6. Hội thoại thực tế SỬ DỤNG ngữ pháp 은/는

### 🎬 Tình huống: Giới thiệu quê hương (so sánh)
- **A**: 고향이 어디예요?
  - *gô-hyang-i ơ-di-ye-yo?*
  - 고향(quê)+이(tiểu từ) 어디(đâu)+예요(là)?
- **B**: 저**는** 호치민에서 왔어요. 한국**은** 추운데 베트남**은** 따뜻해요.
  - *jơ-**nưn** hô-chi-min-e-xơ wa-ssơ-yo. han-guk-**ưn** chu-un-de bê-thư-nam-**ưn** tta-ttưt-hae-yo.*
  - 저(tôi)+**는**(thì) 호치민(HCM)+에서(từ) 왔어요(đến). 한국(Hàn)+**은**(thì) 추운데(lạnh mà) 베트남(VN)+**은**(thì) 따뜻해요(ấm áp).
```

---

## 4. Ultralearning Roadmap — File Chiến lược Tổng

File `ultralearning_roadmap.md` đặt tại `MD_korea_learning/` sẽ chứa:

### 4.1 Lộ trình 6 tháng (Scott Young Framework)
- **Tháng 1-2**: Metalearning + Foundation (TOPIK I vocabulary + 50 grammar)
- **Tháng 2-3**: Drill + Directness (Speaking practice + Writing)
- **Tháng 3-4**: Retrieval + Feedback (TOPIK mock tests + Error correction)
- **Tháng 4-5**: Interleaving + Overlearning (Mix all topics, tăng tốc)
- **Tháng 5-6**: TOPIK 5 Simulation + Retention (Full mock exams)

### 4.2 Lịch trình hàng ngày mẫu
- 🌅 Sáng (30 phút): Spaced Repetition cards (Obsidian/Anki)
- 🌞 Trưa (15 phút): Active Recall quiz
- 🌆 Chiều (45 phút): Feynman + Grammar deep dive
- 🌙 Tối (30 phút): Situational Challenge + TOPIK mock

### 4.3 Checklist Milestone
- [ ] Tuần 1-4: Hoàn thành 50 grammar + 500 từ cơ bản
- [ ] Tuần 5-8: TOPIK I mock test ≥ 120/200
- [ ] Tuần 9-12: Hoàn thành TOPIK II vocabulary (2000 từ)
- [ ] Tuần 13-16: TOPIK II 읽기 mock ≥ 60/100
- [ ] Tuần 17-20: TOPIK II 듣기 mock ≥ 60/100
- [ ] Tuần 21-24: TOPIK 5 simulation ≥ 190/300

---

## 5. Phạm vi thực thi

### 5.1 Files cần tạo/sửa
| Loại | Số lượng | Hành động |
|------|---------|-----------|
| Vocabulary files (`v-*.md`) | 24 files | Tái tạo hoàn toàn với 8 tầng |
| Grammar files (`g-*.md`) | 50 files | Tái tạo hoàn toàn với 6 tầng |
| Ultralearning Roadmap | 1 file | Tạo mới |
| Index.md | 1 file | Cập nhật links |
| AGENTS.md | 1 file | Cập nhật rules |

### 5.2 Dữ liệu bảo tồn
- ✅ Phần Reading/Listening passages từ Kyung Hee (Part 4 cũ)
- ✅ Vietnamese phonetic system (phiên âm thuần Việt)
- ✅ Obsidian `::` card format
- ✅ Wikilink cross-references

### 5.3 Constraints
- Tên file giữ nguyên (không đổi path)
- Windows-safe filenames (không ký tự đặc biệt)
- Tương thích Anki export
- File không quá 2000 dòng (để Obsidian không lag)

---

## 6. Tiêu chí Thành công

| # | Tiêu chí | Đo lường |
|---|---------|---------|
| 1 | Mỗi file vocabulary có đủ 8 tầng | Kiểm tra cấu trúc heading |
| 2 | Mỗi file grammar có đủ 6 tầng | Kiểm tra cấu trúc heading |
| 3 | Mạng nơ-ron đệ quy 4 tầng cho MỌI từ gốc | Đếm tree nodes |
| 4 | Trái nghĩa + Đồng nghĩa ở mọi tầng | Grep `⚔️` và `🔄` |
| 5 | TOPIK tags trên mọi flashcard | Grep `#TOPIK-` |
| 6 | Active Recall quiz ≥ 3 câu/file | Đếm `[!QUESTION]` |
| 7 | Mnemonics cho ≥ 50% từ gốc | Đếm bảng Mnemonic |
| 8 | 0 broken wikilinks | Chạy link checker |
| 9 | Bảo tồn 100% Reading/Listening passages | So sánh trước/sau |
| 10 | Ultralearning Roadmap hoàn chỉnh | Review thủ công |
