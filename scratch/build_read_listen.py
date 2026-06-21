import os

OUT_DIR = r"t:\Topik\giao trình kyung hee\MD_korea_learning\wiki\exam_prep"

def get_reading_content(level):
    if level == 1:
        title = "Đề Thi Trắc Nghiệm Đọc Hiểu KTHP Số 1 (VỪA - KHỞI ĐỘNG)"
        q1 = "저는 축구를 좋아합니다. 주말에 공원에서 축구를 합니다."
        q1_opts = "① 장소   ② 직업   ③ 취미   ④ 나이"
        q1_ans = "③ 취미 (Sở thích). Không có bẫy."
        
        q10_text = "저는 오늘 백화점에 갔습니다. 모자를 샀습니다. 모자가 만 오천 원이었습니다. 그리고 식당에서 비빔밥을 먹었습니다."
        q10_opts = "① 저는 오늘 모자를 샀습니다.\n② 모자는 15,000원입니다.\n③ 식당에서 옷을 샀습니다.\n④ 밥을 먹었습니다."
        q10_ans = "③ (Câu sai: Ở nhà hàng thì ăn cơm, không phải mua quần áo)."

    elif level == 2:
        title = "Đề Thi Trắc Nghiệm Đọc Hiểu KTHP Số 2 (KHÓ - CÓ BẪY PHỦ ĐỊNH)"
        q1 = "영화관에 갔습니다. 표가 너무 비쌉니다. 그래서 영화를 안 봤습니다. 카페에서 커피를 마셨습니다."
        q1_opts = "① 쇼핑   ② 주말   ③ 영화   ④ 병원"
        q1_ans = "③ 영화 (Chủ đề là đi xem phim nhưng KHÔNG XEM vì vé đắt. Bẫy: Mua cà phê chỉ là phụ)."
        
        q10_text = "어제 명동에서 바지를 샀습니다. 바지가 아주 예뻤습니다. 하지만 너무 비쌌습니다. 그래서 구두는 안 샀습니다."
        q10_opts = "① 명동에서 쇼핑을 했습니다.\n② 바지가 싸고 예뻤습니다.\n③ 구두를 안 샀습니다.\n④ 바지가 비쌌습니다."
        q10_ans = "② (Câu sai: Bẫy từ trái nghĩa 싸다 (Rẻ) và 비싸다 (Đắt). Trong bài nói 바지가 비쌌습니다, đáp án lại bảo 싸고 예뻤습니다 là sai)."

    else:
        title = "Đề Thi Trắc Nghiệm Đọc Hiểu KTHP Số 3 (SIÊU KHÓ - BẪY LIÊN HOÀN)"
        q1 = "내일은 동생 생일입니다. 백화점은 우체국에서 멀고 옷이 비쌉니다. 그래서 저는 은행 옆에 있는 시장에 갈 겁니다."
        q1_opts = "① 선물   ② 위치   ③ 약속   ④ 주말"
        q1_ans = "② 위치 (Nói về khoảng cách xa gần 멀다, và vị trí 우체국에서, 은행 옆에. Đây là đoạn văn hỏi đường/vị trí bị giấu dưới lớp vỏ mua sắm)."
        
        q10_text = "저는 오늘 식당에 갔습니다. 불고기를 먹고 싶었습니다. 하지만 불고기가 안 맵고 맛없었습니다. 그래서 비빔밥을 먹었습니다. 비빔밥은 조금 매웠지만 아주 맛있었습니다."
        q10_opts = "① 불고기가 매웠습니다.\n② 비빔밥이 맛없었습니다.\n③ 오늘 불고기를 먹었습니다.\n④ 비빔밥이 조금 매웠습니다."
        q10_ans = "①, ②, ③ đều sai. ④ (Câu đúng: 비빔밥이 조금 매웠습니다. Bẫy liên hoàn: Phải chú ý từ nối 하지만 (Nhưng mà) và 그래서 (Vì thế) để biết tác giả CHƯA ăn Bulgogi mà ĂN Bibimbap)."

    content = f"""# 📖 {title}

> [!IMPORTANT] 💎 BÍ KÍP 80/20 (PARETO HACK)
> Cấp độ {level}/3. Bộ đề này sử dụng công nghệ Debate để giả lập các bẫy thực tế trong TOPIK 1.
> Luyện kỹ khả năng dò tìm từ trái nghĩa (싸다 vs 비싸다) và câu phủ định (안/못).

---

## 🎯 PHẦN 1: TÌM CHỦ ĐỀ
*무엇에 대한 이야기입니까? (Đoạn văn sau nói về cái gì?)*

**1.** {q1}
{q1_opts}

---

## 🚨 PHẦN 2: TÌM CÂU SAI / ĐÚNG
*(Chọn câu KHÔNG ĐÚNG - 맞지 않는 것, hoặc câu ĐÚNG - 맞는 것)*

> {q10_text}

**10. 이 글의 내용과 맞는/맞지 않는 것을 고르십시오.**
{q10_opts}

*(Đây là bản mô phỏng Rút gọn tập trung vào Câu hỏi Bẫy. Trong phòng thi thực tế sẽ có thêm 23 câu tương tự form này).*

---

<details>
<summary><b>👉 XEM ĐÁP ÁN & GIẢI THÍCH (BẢN SONG NGỮ)</b></summary>

### 📝 ĐÁP ÁN
1. {q1_ans}
10. {q10_ans}

*(Ghi chú Debate: Tại cấp độ {level}, hệ thống cố tình cài cắm các bẫy liên quan đến Hư từ, Trái nghĩa và Phủ định. Đọc kỹ phần giải thích để né bẫy ngày mai).*
</details>
"""
    return content


def get_listening_content(level):
    if level == 1:
        title = "Đề Thi Trắc Nghiệm Nghe Hiểu KTHP Số 1 (VỪA - KHỞI ĐỘNG)"
        q5 = "👨 남: 주말에 보통 뭐 해요? (Cuối tuần thường làm gì?)"
        q5_opts = "① 주말이에요.   ② 친구를 만나요.   ③ 토요일이에요.   ④ 도서관에 없어요."
        q5_ans = "② 친구를 만나요. (Gặp bạn). Hỏi làm gì -> Trả lời hành động."

    elif level == 2:
        title = "Đề Thi Trắc Nghiệm Nghe Hiểu KTHP Số 2 (KHÓ - CÓ BẪY ĐÁP ÁN)"
        q5 = "👩 여: 우체국이 어디에 있어요? (Bưu điện ở đâu?)"
        q5_opts = "① 우표를 사요.   ② 은행 옆에 있어요.   ③ 우체국이 커요.   ④ 내일 가요."
        q5_ans = "② 은행 옆에 있어요. (Ở cạnh ngân hàng). Bẫy cực gắt: Hỏi Ở ĐÂU, nhưng đáp án ① (Mua tem) cố tình lừa người nghe không tập trung vào từ để hỏi 어디."

    else:
        title = "Đề Thi Trắc Nghiệm Nghe Hiểu KTHP Số 3 (SIÊU KHÓ - BẪY THÔNG TIN KÉP)"
        q5 = "👨 남: 이 구두 얼마예요? (Đôi giày này bao nhiêu tiền?)\n👩 여: 5만 원이에요. \n👨 남: 너무 비싸요. 그럼 저 운동화는요? (Đắt quá. Vậy còn đôi giày thể thao kia?)\n👩 여: 3만 원이에요."
        q5_opts = "Câu hỏi: 남자는 무엇을 샀습니까? (Người nam đã mua cái gì?)\n① 구두 (5만 원)   ② 운동화 (3만 원)   ③ 옷 (3만 원)   ④ 안 샀습니다."
        q5_ans = "② 운동화. (Bẫy thông tin kép: Audio đọc 2 mức giá và 2 món đồ. Người nam chê đôi giày da quá đắt (비싸요) nên chuyển sang hỏi mua đôi thể thao (운동화))."

    content = f"""# 🎧 {title}

> [!IMPORTANT] 💎 BÍ KÍP 80/20 (PARETO HACK)
> Cấp độ {level}/3. **Shadowing Reading**: Tự đọc to Script trong 3 giây và khoanh đáp án. 

---

## 🧩 PHẦN 1: NGHE VÀ TRẢ LỜI CÂU HỎI

**Script Câu 5-8:**
{q5}

{q5_opts}

---

<details>
<summary><b>👉 XEM ĐÁP ÁN & GIẢI THÍCH CHI TIẾT</b></summary>

### 📝 BẢN DỊCH SONG NGỮ & GIẢI THÍCH
**Đáp án:**
{q5_ans}

*(Ghi chú Debate: Tại cấp độ {level}, việc Nghe không đơn thuần là nghe hiểu từ vựng, mà là cuộc chiến loại trừ Đáp án Bẫy).*
</details>
"""
    return content


for i in range(1, 4):
    r_filepath = os.path.join(OUT_DIR, f"08.{i}-official-reading-exam.md")
    with open(r_filepath, "w", encoding="utf-8") as f:
        f.write(get_reading_content(i))
        
    l_filepath = os.path.join(OUT_DIR, f"09.{i}-official-listening-exam.md")
    with open(l_filepath, "w", encoding="utf-8") as f:
        f.write(get_listening_content(i))

print("Created 3 Reading exams and 3 Listening exams with difficulty progression (Normal -> Hard -> Super Hard).")
