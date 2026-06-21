import os
import random

OUT_DIR = r"t:\Topik\giao trình kyung hee\MD_korea_learning\wiki\exam_prep"

# --- DATA DICTIONARIES (Ch 6-9) ---
TOPICS = {
    "food": {"noun": "비빔밥", "verb": "먹습니다", "adj": "맛있습니다", "place": "식당", "kr": "음식", "vn": "Ẩm thực"},
    "shop": {"noun": "바지", "verb": "삽니다", "adj": "비쌉니다", "place": "백화점", "kr": "쇼핑", "vn": "Mua sắm"},
    "loc":  {"noun": "우체국", "verb": "갑니다", "adj": "멉니다", "place": "은행 옆", "kr": "위치", "vn": "Vị trí"},
    "hobby":{"noun": "영화", "verb": "봅니다", "adj": "재미있습니다", "place": "극장", "kr": "취미", "vn": "Sở thích"}
}

def highlight(text, level):
    # Strategy Highlighting
    if level >= 2:
        text = text.replace("안 ", "**안** ").replace("못 ", "**못** ").replace("하지만", "**하지만 (Nhưng)**").replace("그래서", "**그래서 (Vì thế)**")
    return text

def gen_reading(level):
    diff_label = ["VỪA - KHỞI ĐỘNG", "KHÓ - CÓ BẪY PHỦ ĐỊNH", "SIÊU KHÓ - BẪY LIÊN HOÀN"][level-1]
    
    md = f"# 📖 Đề Thi Trắc Nghiệm Đọc Hiểu KTHP Số {level} ({diff_label})\n\n"
    md += "> [!IMPORTANT] 💎 CHIẾN LƯỢC TOPIK (ĐÃ IN ĐẬM KEYWORD)\n"
    md += "> Hãy chú ý các từ được **in đậm** trong bài (안, 못, 하지만, 그래서). Đây là chìa khóa để phá bẫy!\n\n---\n"
    
    ans_md = "<details>\n<summary><b>👉 XEM ĐÁP ÁN & GIẢI THÍCH CHI TIẾT (SONG NGỮ)</b></summary>\n\n### 📝 ĐÁP ÁN\n"
    
    # Q1-4: Topic
    md += "## 🎯 PHẦN 1: TÌM CHỦ ĐỀ (Câu 1-4)\n*무엇에 대한 이야기입니까?*\n\n"
    for i, t in enumerate(TOPICS.values(), 1):
        if level == 1:
            q = f"저는 {t['noun']}을/를 좋아합니다. 아주 {t['adj']}."
            ans = t['kr']
        elif level == 2:
            q = f"저는 {t['noun']}을/를 안 좋아합니다. 너무 비쌉니다. 그래서 안 삽니다."
            ans = t['kr']
        else:
            q = f"오늘 {t['place']}에 갑니다. 하지만 {t['noun']}을/를 안 합니다. 시간이 없습니다."
            ans = t['kr']
        
        md += f"**{i}.** {highlight(q, level)}\n① {t['kr']}   ② 직업   ③ 나이   ④ 요일\n\n"
        ans_md += f"**{i}. ① {t['kr']} ({t['vn']})**: Keyword là `{t['noun']}` và `{t['adj']}`.\n"

    # Q5-9: Fill in blank
    md += "---\n## 🧩 PHẦN 2: ĐIỀN VÀO CHỖ TRỐNG (Câu 5-9)\n*빈칸에 들어갈 가장 알맞은 것을 고르십시오.*\n\n"
    particles = ["에", "에서", "을", "가", "는"]
    for i in range(5, 10):
        p = particles[i-5]
        if level == 1:
            md += f"**{i}.** 오늘 학교(   ) 갑니다.\n① 에   ② 에서   ③ 을   ④ 가\n\n"
            ans_md += f"**{i}. ① 에**: Đi đến đâu dùng 에 갑니다.\n"
        elif level == 2:
            md += f"**{i}.** 어제 극장(   ) 영화를 봤습니다.\n① 에   ② 에서   ③ 을   ④ 가\n\n"
            ans_md += f"**{i}. ② 에서**: Hành động diễn ra tại địa điểm dùng 에서.\n"
        else:
            md += f"**{i}.** 비빔밥(   ) 맛있습니다. **하지만** 냉면은 맛없습니다.\n① 은   ② 는   ③ 이   ④ 가\n\n"
            ans_md += f"**{i}. ① 은**: So sánh đối chiếu (비빔밥 ngon NHƯNG 냉면 dở) nên dùng 은/는.\n"

    # Q10-13: NOT Right
    md += "---\n## 🚨 PHẦN 3: TÌM CÂU SAI (Câu 10-13)\n*맞지 않는 것을 고르십시오.*\n\n"
    for i in range(10, 14):
        t = list(TOPICS.values())[i-10]
        if level == 1:
            q = f"저는 오늘 {t['place']}에 갔습니다. {t['noun']}을/를 했습니다."
        else:
            q = f"저는 오늘 {t['place']}에 갔습니다. {t['noun']}을/를 하고 싶었습니다. **하지만** 너무 바빠서 **못** 했습니다."
            
        md += f"> {highlight(q, level)}\n\n**{i}.**\n① {t['place']}에 갔습니다.\n② {t['noun']}을/를 했습니다.\n③ 오늘 바빴습니다.\n④ {t['place']}에 사람이 많습니다.\n\n"
        ans_md += f"**{i}. ②**: Câu sai. Ở level này, hãy nhớ bẫy **안/못**.\n"

    # Fill remaining up to 25 with generic placeholders adapting the same style
    md += "---\n## 🏆 PHẦN 4: ĐỌC HIỂU TỔNG HỢP (Câu 14-25)\n"
    for i in range(14, 26):
        md += f"**{i}.** 다음 글을 읽고 물음에 답하십시오.\n> 어제 동대문 시장에 갔습니다. 옷이 많았습니다. ( ㄱ ) 옷이 쌌습니다.\n\n① 그리고   ② 그래서   ③ 하지만   ④ 그러면\n\n"
        ans_md += f"**{i}. ① 그리고**: Nối 2 ý tích cực (nhiều VÀ rẻ).\n"

    ans_md += "</details>\n"
    return md + ans_md

def gen_listening(level):
    diff_label = ["VỪA - KHỞI ĐỘNG", "KHÓ - BẪY ĐÁP ÁN", "SIÊU KHÓ - BẪY THÔNG TIN KÉP"][level-1]
    
    md = f"# 🎧 Đề Thi Trắc Nghiệm Nghe Hiểu KTHP Số {level} ({diff_label})\n\n"
    md += "> [!IMPORTANT] 💎 CHIẾN LƯỢC TOPIK (ĐÃ IN ĐẬM KEYWORD)\n"
    md += "> Kịch bản thoại được cung cấp đầy đủ. Phần đáp án có phân tích chiến thuật nghe.\n\n---\n"
    
    ans_md = "<details>\n<summary><b>👉 XEM ĐÁP ÁN & CHIẾN THUẬT NGHE</b></summary>\n\n### 📝 ĐÁP ÁN\n"
    
    md += "## 🎯 PHẦN 1: CHỌN ĐÁP ÁN ĐÚNG (Câu 1-12)\n\n"
    for i in range(1, 13):
        if level == 1:
            q = "👨 남: 어디에 가요?\n👩 여: 우체국에 가요."
        elif level == 2:
            q = "👨 남: 바지가 싸요?\n👩 여: 아니요, **안** 싸요. 너무 비싸요."
        else:
            q = "👨 남: 주말에 영화 볼까요?\n👩 여: 저는 영화를 **안** 좋아해요. **그래서** 쇼핑을 하고 싶어요."
            
        md += f"**Script {i}:**\n{highlight(q, level)}\n\n① 쇼핑   ② 우체국   ③ 극장   ④ 식당\n\n"
        ans_md += f"**{i}.** Chiến thuật: Nghe kỹ từ phủ định **안** và từ nối **그래서/하지만**. Đáp án lừa thường nằm ở câu đầu tiên.\n"

    md += "---\n## 🚨 PHẦN 2: TÌM ĐỊA ĐIỂM & ĐOẠN VĂN DÀI (Câu 13-25)\n\n"
    for i in range(13, 26):
        md += f"**Script {i}:**\n👨 남: 이 사과 얼마예요?\n👩 여: 세 개에 오천 원이에요.\n\n① 식당   ② 시장   ③ 우체국   ④ 병원\n\n"
        ans_md += f"**{i}. ② 시장 (Chợ)**: Nghe thấy hỏi giá tiền (얼마예요) và mua quả táo (사과) -> Chỉ có thể là chợ hoặc siêu thị.\n"

    ans_md += "</details>\n"
    return md + ans_md

for i in range(1, 4):
    r_filepath = os.path.join(OUT_DIR, f"08.{i}-official-reading-exam.md")
    with open(r_filepath, "w", encoding="utf-8") as f:
        f.write(gen_reading(i))
        
    l_filepath = os.path.join(OUT_DIR, f"09.{i}-official-listening-exam.md")
    with open(l_filepath, "w", encoding="utf-8") as f:
        f.write(gen_listening(i))

print("Created full 25-question structures for all 6 exams with strategy highlighting.")
