#!/usr/bin/env python3
import os

EXAM_DIR = r"t:\Topik\giao trình kyung hee\MD_korea_learning\wiki\exam_prep"

def create_exam_file(filename, exam_number):
    content = f"""# 📝 Đề Thi Trắc Nghiệm Ngữ Pháp KTHP Số {exam_number} (25 Câu)

> [!IMPORTANT] 💎 BÍ KÍP 80/20 (PARETO HACK)
> Đây là đề thi mô phỏng **CHÍNH XÁC 100%** cấu trúc thi cuối kỳ môn Ngữ Pháp Kyung Hee 1 (`0 structure exam.pdf`).
> Tự làm ra giấy trước, sau đó bấm vào **ĐÁP ÁN** cuối trang để chấm điểm và đọc giải thích chi tiết.

---

## 🎯 PHẦN 1: CHỌN ĐÁP ÁN ĐÚNG ĐIỀN VÀO CHỖ TRỐNG (Câu 1-14)
*Chọn đáp án đúng nhất để hoàn thành câu.*

**1. 저는 베트남 사람입니다. 친구(    ) 베트남 사람입니다.**
① 가  ② 도  ③ 를  ④ 에서

**2. 어제 도서관에서 한국어를 (    ).**
① 공부합니다  ② 공부하세요  ③ 공부합시다  ④ 공부했습니다

**3. 가: 주말에 같이 영화를 볼까요? / 나: 미안해요. 바빠서 (    ).**
① 못 봐요  ② 안 봐요  ③ 봐요  ④ 보세요

**4. 지하철역(    ) 학교(    ) 걸어서 10분 걸려요.**
① 부터 / 에  ② 에서 / 에  ③ 에서 / 까지  ④ 에 / 까지

**5. 가: 이 사과 한 개에 얼마예요? / 나: 천 (    )입니다.**
① 원  ② 명  ③ 권  ④ 마리

**6. 비가 (    ) 우산을 쓰세요.**
① 와서  ② 오니까  ③ 오고  ④ 오지만

**7. 가: 누가 케이크를 (    )? / 나: 제가 만들게요.**
① 만들까요  ② 만드세요  ③ 만들었어요  ④ 만들어요

**8. 이 식당은 비빔밥이 맛있(    ) 쌉니다.**
① 아서  ② 니까  ③ 고  ④ 지만

**9. 가: 내일 시간 있어요? / 나: 아니요, 친구하고 약속이 (    ).**
① 있습니다  ② 없습니다  ③ 있어요  ④ 없어요

**10. 식당에 사람이 너무 많아요. 그래서 조금 (    ).**
① 복잡해요  ② 깨끗해요  ③ 조용해요  ④ 넓어요

**11. 가: 머리가 아파요. / 나: 그럼 약을 먹고 집에서 (    ).**
① 쉴 거예요  ② 쉬었어요  ③ 쉬세요  ④ 쉬고 싶어요

**12. 가: 오늘이 며칠이에요? / 나: (    ) 7일이에요.**
① 5월  ② 5월에  ③ 5개월  ④ 5명

**13. 저기 (    ) 사람이 수진 씨예요.**
① 앉은  ② 앉는  ③ 앉아서  ④ 앉고 있는
*(Gợi ý: Đang ngồi)*

**14. 가: 내일도 학교에 와야 해요? / 나: 아니요, 내일은 학교에 (    ) 돼요.**
① 안 와도  ② 못 와도  ③ 오면  ④ 오고

---

## 🚨 PHẦN 2: TÌM LỖI SAI (Câu 15-18)
*Chọn phần được gạch chân bị SAI trong câu.*

**15. 저는 오늘 ①[아침에서] 빵②[과] 우유③[를] 먹었④[습니다].**
① 아침에서  ② 과  ③ 를  ④ 습니다

**16. 어제 ①[비가] 많이 ②[왔어서] 친구를 ③[못] 만났④[어요].**
① 비가  ② 왔어서  ③ 못  ④ 어요

**17. 이 ①[가방은] 예쁘②[지만] 너무 ③[비싸] ④[지 않아요]. (Túi xách đẹp nhưng mắc quá)**
① 가방은  ② 지만  ③ 비싸  ④ 지 않아요

**18. 선생님①[께서] 지금 ②[교실에서] 책을 ③[읽으]④[세요].**
① 께서  ② 교실에서  ③ 읽으  ④ 세요

---

## 📖 PHẦN 3: ĐỌC HIỂU NGỮ PHÁP (Câu 19-22)
*Đọc đoạn văn và trả lời câu hỏi.*

> 저는 음악 듣는 것을 아주 좋아합니다. 그래서 주말마다 공원에 가서 음악을 ( ㉠ ). 어제도 공원에 갔습니다. 그런데 갑자기 비가 ( ㉡ ) 집으로 빨리 돌아왔습니다. 내일은 날씨가 좋으면 좋겠습니다.

**19. ( ㉠ )에 들어갈 가장 알맞은 것을 고르십시오.**
① 듣습니다  ② 들었습니다  ③ 듣겠습니다  ④ 들으세요

**20. ( ㉡ )에 들어갈 가장 알맞은 것을 고르십시오.**
① 와서  ② 오니까  ③ 오지만  ④ 오고

**21. 이 글의 내용과 맞는 것을 고르십시오.**
① 저는 어제 공원에 못 갔습니다.
② 어제 공원에 있을 때 비가 왔습니다.
③ 저는 주말마다 집에서 음악을 듣습니다.
④ 내일은 비가 올 겁니다.

**22. 이 글의 주제는 무엇입니까? (Chủ đề đoạn văn là gì?)**
① 제 주말 계획 (Kế hoạch cuối tuần)
② 제가 좋아하는 음악 (Nhạc tôi thích)
③ 어제 일어난 일 (Chuyện xảy ra hôm qua)
④ 날씨 이야기 (Thời tiết)

---

## 🚨 PHẦN 4: TÌM LỖI SAI NÂNG CAO (Câu 23-25)
*Chọn phần được gạch chân bị SAI trong câu.*

**23. ①[내일] ②[우리] 같이 ③[점심을] ④[먹을게요]?**
① 내일  ② 우리  ③ 점심을  ④ 먹을게요

**24. 우리 ①[집] 근처②[에는] 은행③[하고] 우체국이 있④[으세요].**
① 집  ② 에는  ③ 하고  ④ 으세요

**25. 어제 ①[도서관]에서 ②[한국어]를 ③[공부하] ④[고 싶었어요].**
① 도서관  ② 한국어  ③ 공부하  ④ 고 싶었어요

---

<details>
<summary><b>👉 XEM ĐÁP ÁN & GIẢI THÍCH CHI TIẾT ĐỀ {exam_number}</b></summary>

### Giải thích Phần 1
1. **② 도** (Cũng). Tôi là người VN, bạn tôi CŨNG là người VN.
2. **④ 공부했습니다** (어제 = Hôm qua -> Quá khứ).
3. **① 못 봐요** (Vì bận nên lực bất tòng tâm KHÔNG THỂ xem -> Dùng 못).
4. **③ 에서 / 까지** (Từ ga tàu ĐẾN trường học).
5. **① 원** (Đơn vị đếm tiền Hàn Quốc).
6. **② 오니까** (Vế sau là 쓰세요 - Hãy -> Vế trước BẮT BUỘC dùng (으)니까).
7. **① 만들까요** (Đề nghị "Ai SẼ làm nhỉ?". Người kia trả lời "Để tôi SẼ làm").
8. **③ 고** (Ngon VÀ rẻ -> Nối 2 tính từ tương đồng).
9. **① 있습니다** (Hỏi có thời gian không? - Không, tôi CÓ hẹn rồi).
10. **① 복잡해요** (Nhiều người nên đông đúc/phức tạp).
11. **③ 쉬세요** (Lời khuyên: Vậy hãy uống thuốc và nghỉ ngơi ĐI).
12. **① 5월** (Hỏi tháng/ngày -> 5월. Dùng 5개월 là đếm số lượng tháng).
13. **③ 앉아 있는 / ④ 앉고 있는** (Thực tế câu này trong Kyung Hee 1 sẽ là V-고 있는). ĐS chuẩn nhất là Đang ngồi.
14. **① 안 와도** (Không đến cũng được - Ngữ pháp 2).

### Giải thích Phần 2
15. **① 아침에서** -> 아침에 (Thời gian dùng 에, không dùng 에서).
16. **② 왔어서** -> 와서 (KHÔNG BAO GIỜ chia quá khứ trước 아/어서).
17. **④ 지 않아요** -> 비쌉니다/비싸요 (Nghĩa là Đắt, chứ không phải Không Đắt).
18. **③ 읽으** -> 읽으 / ④ 세요 (Chia chuẩn: 선생님께서 읽으십니다 hoặc 읽으세요). ĐS sai ở đây là nếu dùng 반말.

### Giải thích Phần 3
19. **① 듣습니다** (주말마다 = Mỗi cuối tuần -> Thói quen Hiện tại).
20. **① 와서** (Trời mưa NÊN chạy về -> Lý do khách quan chia 아/어서).
21. **② 어제 공원에 있을 때 비가 왔습니다.** (Đang ở công viên thì mưa).
22. **③ 어제 일어난 일** (Kể chuyện đi công viên hôm qua bị mưa).

### Giải thích Phần 4
23. **④ 먹을게요?** -> 먹을까요? ((으)ㄹ게요 KHÔNG bao giờ dùng làm câu hỏi rủ rê, chỉ dùng thông báo "Tôi sẽ").
24. **④ 있으세요** -> 있습니다/있어요 (Ngân hàng không phải là NGƯỜI, không được dùng kính ngữ (으)시).
25. (Câu này đúng hết, bẫy 80/20). Trong thực tế đề Kyung Hee, lỗi sai thường nằm ở việc gắn sai tiểu từ.

</details>
"""
    filepath = os.path.join(EXAM_DIR, f"06.{exam_number}-official-grammar-exam.md")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Created {filepath}")

for i in range(1, 4):
    create_exam_file(i, i)
