# Đặc tả Thiết kế Hệ thống Học liệu Động: Kyung Hee 1 LLM Wiki

Tài liệu này xác lập thiết kế kiến trúc, cấu trúc lưu trữ, quy trình xử lý dữ liệu và kịch bản tự động hóa cho hệ thống **Kyung Hee Level 1 Beginner Grammar — LLM Wiki** được triển khai dưới dạng một Obsidian Vault động, tự tiến hóa theo phản hồi của người học.

---

## 🗺️ 1. Bản đồ Tri thức & Danh sách 50 Ngữ pháp
Hệ thống học liệu được xây dựng quanh **50 đơn vị học tập ngữ pháp** cốt lõi được trích xuất trực tiếp từ giáo trình *Kyung Hee Korean Beginner 1 Grammar*:

| STT | Cấu trúc Ngữ pháp tiếng Hàn | Ý nghĩa sơ lược (tiếng Việt) | Trang sách |
| :--- | :--- | :--- | :--- |
| 1 | 명사 입니다, 명사 입니까? | Là... / Có phải là... không? (Trang trọng) | 14 |
| 2 | 명사 은/는 1 | Tiểu từ chủ đề (Giới thiệu bản thân) | 18 |
| 3 | 명사 이에요/예요 | Là... (Lịch sự thân mật) | 22 |
| 4 | 명사 이/가 | Tiểu từ chủ ngữ | 27 |
| 5 | 명사 의 | Tiểu từ sở hữu (Của...) | 32 |
| 6 | 명사 이/가 아니다 | Không phải là... | 37 |
| 7 | 동사 습/ㅂ니다, 동사 습/ㅂ니까? | Đuôi câu động/tính từ trang trọng | 42 |
| 8 | 명사 을/를 | Tiểu từ tân ngữ | 46 |
| 9 | 이/그/저 명사 | Định từ chỉ định (Đây/Đó/Kia) | 51 |
| 10 | 한자어 수 | Hệ số Hán-Hàn (Số đếm) | 55 |
| 11 | 고유어 수 | Hệ số thuần Hàn (Số đếm) | 59 |
| 12 | 동사 아/어요 | Đuôi câu động/tính từ lịch sự thân mật | 63 |
| 13 | 명사 에 1 | Tiểu từ chỉ vị trí (Có ở... / Không có ở...) | 68 |
| 14 | 명사 하고 | Liên từ nối danh từ (Và / Cùng với) | 73 |
| 15 | 단위 명사 | Danh từ chỉ đơn vị (Counters) | 77 |
| 16 | ㅂ 불규칙 | Bất quy tắc của phụ âm cuối `ㅂ` | 82 |
| 17 | 명사 은/는 2 | Tiểu từ chủ đề (Dùng so sánh, đối chiếu) | 86 |
| 18 | 안 동사, 동사 지 않다 | Phủ định của động/tính từ (Không...) | 91 |
| 19 | 명사 에서 | Tiểu từ chỉ vị trí xảy ra hành động (Tại...) | 95 |
| 20 | 동사 고 1 | Liên từ nối vế câu (Và...) | 99 |
| 21 | 명사 에 2 | Tiểu từ chỉ thời gian (Vào lúc...) | 103 |
| 22 | 명사 도 | Tiểu từ chỉ sự tương đồng (Cũng...) | 107 |
| 23 | 동사 았/었- | Thì quá khứ | 111 |
| 24 | 동작동사 고 2 | Liên từ chỉ thứ tự hành động (Làm A rồi làm B) | 115 |
| 25 | 동작동사 고 싶다 | Mong muốn của ngôi thứ nhất/hai (Muốn...) | 119 |
| 26 | 동작동사 고 싶어 하다 | Mong muốn của ngôi thứ ba (Muốn...) | 123 |
| 27 | 동작동사 (으)세요, (으)하십시오 | Đuôi câu mệnh lệnh lịch sự / Yêu cầu | 127 |
| 28 | 명사 (으)로 1 | Chỉ hướng chuyển động (Hướng về phía...) | 131 |
| 29 | 명사 에게/한테/께 | Cho ai đó / Tới ai đó (Dative) | 135 |
| 30 | 으 탈락 | Biến âm/giản lược nguyên âm `ㅡ` | 139 |
| 31 | 동사 지만 | Liên từ nối hai vế tương phản (Nhưng...) | 144 |
| 32 | 명사 보다 | Cấu trúc so sánh (Hơn...) | 149 |
| 33 | 명사 만 | Tiểu từ giới hạn (Chỉ...) | 153 |
| 34 | 명사 (으)로 2 | Chỉ phương tiện, công cụ, cách thức (Bằng...) | 157 |
| 35 | 명사 에서/부터 ... 까지 | Từ... đến... (Khoảng cách / Thời gian) | 161 |
| 36 | 동작동사 아/어서 1 | Liên từ chỉ trình tự thời gian liên kết chặt chẽ | 165 |
| 37 | 동사 (으)시- | Kính ngữ đối với chủ ngữ | 169 |
| 38 | 명사 에게(서)/한테(서)/께 | Từ ai đó (Nhận được hành động từ...) | 174 |
| 39 | 동사 (으)ㄹ 겁니다/거예요 | Thì tương lai / Dự đoán | 179 |
| 40 | (으)ㄹ까요?, (으)ㅂ시다 | Đuôi câu rủ rê, đề nghị cùng làm gì | 183 |
| 41 | 못 동사, 동사 지 못하다 | Phủ định khả năng (Không thể...) | 188 |
| 42 | 동작동사 겠- 1 | Ý chí, dự định của người nói (Sẽ...) | 194 |
| 43 | ㄹ 탈락 | Giản lược/bất quy tắc của phụ âm cuối `ㄹ` | 199 |
| 44 | 동작동사 (으)ㄹ 수 있다/없다 | Có thể / Không thể làm gì | 204 |
| 45 | 동사 아/어서 2 | Liên từ chỉ nguyên nhân - kết quả (Vì... nên) | 208 |
| 46 | 동작동사 지 말다 | Mệnh lệnh phủ định (Đừng làm...) | 213 |
| 47 | 동작동사 (으)ㄹ게요 | Lời hứa, cam kết của người nói | 218 |
| 48 | 동사 (으)니까 1 | Liên từ chỉ nguyên nhân (Vì... nên - mang tính chủ quan) | 223 |
| 49 | 동작동사 고 있다 | Thì hiện tại tiếp diễn (Đang...) | 228 |
| 50 | 명사 과/와 | Liên từ nối danh từ (Và / Với) | 234 |

---

## 📂 2. Cấu trúc Tổ chức Tệp tin (File Architecture)
Tất cả các tệp của hệ thống được quản lý bên dưới thư mục `/MD/`:

```text
/t:/Topik/giao trình kyung hee/MD/
├── docs/
│   └── specs/
│       └── 2026-05-27-kyunghee-grammar-study-guide-design.md ← Tệp đặc tả này
├── AGENTS.md                 ← Bản hiến pháp tự động hóa của LLM
├── wiki/
│   ├── index.md              ← Dashboard trung tâm (Bản đồ tri thức)
│   ├── log.md                ← Nhật ký hệ thống ghi lại mọi cập nhật/truy vấn
│   ├── concepts/             ← Thư mục chứa các tệp tri thức
│   │   ├── g-*.md            ← Ngữ pháp của giáo viên (50 tệp)
│   │   └── v-*.md            ← Từ vựng theo chủ đề (ví dụ: v-weather.md, v-daily.md)
│   └── queries/              ← Nhật ký câu hỏi & bài tập động từ người học (q-*.md)
```

---

## 📝 3. Đặc tả Định dạng Nội dung (Content Specifications)

### A. Tệp Ngữ pháp Giáo viên (`wiki/concepts/g-*.md`)
Đảm bảo tính sư phạm rõ ràng, dễ hiểu của một giáo viên tiếng Hàn:
1. **Tiêu đề**: Rõ ràng, mô tả cấu trúc, cách dịch cơ bản.
2. **Ngữ cảnh Sử dụng**: Mô tả hoàn cảnh người Hàn thường dùng cấu trúc này.
3. **Teacher's Notes (Mẹo học tập)**:
   - Các lỗi sai học viên Việt Nam thường mắc phải.
   - Chú ý đặc biệt về nối âm hoặc biến âm khi kết hợp đuôi từ.
4. **Bảng quy tắc chia đuôi từ**: Chia rõ ràng theo phụ âm/nguyên âm cuối.
5. **Liên kết Thực tế**: So sánh chéo với các cấu trúc tương đồng (ví dụ: so sánh `-으니까` và `-아서`).

### B. Tệp Từ vựng theo Chủ đề (`wiki/concepts/v-*.md`)
Tập trung vào 3 cấu phần cốt lõi:

#### 1. Flashcard Table
| Tiếng Hàn | Phiên âm tiếng Việt | Nghĩa tiếng Việt | Trạng thái nhớ |
| :--- | :--- | :--- | :--- |
| `[Từ vựng]` | `[Phiên âm mô tả âm thực tế]` | `[Nghĩa tiếng Việt]` | `[ ] Chưa nhớ / [ ] Đã nhớ` |

*Ví dụ thực tế*:
- `선생님` $\rightarrow$ `xơn-xeng-nim`
- `같이` $\rightarrow$ `ga-t-xi` (biến âm của `티` gặp `이` biến thành `치`)
- `비가 오다` $\rightarrow$ `bi-ga o-da`

#### 2. Chunking & Sentence Progression (Lan tỏa kiến thức)
Phát triển năng lực viết câu thông qua cụm từ (chunking):
$$\text{Từ đơn (비)} \rightarrow \text{Cụm từ (비가 오다)} \rightarrow \text{Câu áp dụng ngữ pháp (오늘 비가 오고 있습니다)}$$

#### 3. Đoạn văn dịch xen kẽ (Interlinear Gloss Translation)
Đoạn văn hoàn chỉnh viết bằng tiếng Hàn, trong đó mỗi từ hoặc cụm từ được kèm theo nghĩa tiếng Việt nằm trong ngoặc đơn ngay sau từ đó. Phương pháp này giúp người học hiểu trật tự cú pháp và từ vựng cùng một lúc mà không cần bản dịch cả câu thô sơ:
- *Mẫu*: `오늘 (hôm nay) 날씨가 (thời tiết) 아주 (rất) 좋습니다 (tốt).`

---

## 🔄 4. Quy chế Tự động hóa & Tự cập nhật (compounding)
Hệ thống **không phải là tài liệu tĩnh**. Nó tự động mở rộng theo thời gian thông qua các câu hỏi truy vấn của người học:

1. **Trình truy cập Chỉ mục (Index-First Flow)**:
   - Khi người học đặt câu hỏi (ví dụ: *"So sánh bất quy tắc ㅂ và ㄹ"*), LLM sẽ quét `wiki/index.md` và ripgrep tìm các trang khái niệm liên quan.
2. **Lưu câu trả lời vào `wiki/queries/`**:
   - Câu trả lời chi tiết kèm theo ví dụ chuẩn định dạng sẽ được lưu thành file `wiki/queries/q-*.md`.
3. **Cập nhật log và liên kết**:
   - Tự động append log vào `wiki/log.md`.
   - Cập nhật mục lục `wiki/index.md` và tạo liên kết hai chiều chéo trong các file concepts để người học có thể nhấp chuột liên kết khi ôn tập.
