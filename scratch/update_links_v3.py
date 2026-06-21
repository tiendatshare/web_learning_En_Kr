# -*- coding: utf-8 -*-
import os
import re

# Bảng ánh xạ tên file La-tinh cũ sang tên tiếng Hàn mới (không có đuôi .md)
GRAMMAR_LINK_MAPPING = {
    "g-01-myeongsa-imnida": "g-01-명사 + 입니다-입니까 (Là - Có phải là không)",
    "g-02-myeongsa-eun-neun-1": "g-02-명사 + 은-는 1 (Tiểu từ chủ đề - Giới thiệu)",
    "g-03-myeongsa-ieyo-yeyo": "g-03-명사 + 이에요-예요 (Là - Thân mật lịch sự)",
    "g-04-myeongsa-i-ga": "g-04-명사 + 이-가 (Tiểu từ chủ ngữ)",
    "g-05-myeongsa-ui": "g-05-명사 + 의 (Tiểu từ sở hữu)",
    "g-06-myeongsa-i-ga-anida": "g-06-명사 + 이-가 아니다 (Không phải là)",
    "g-07-va-bni-da-seumni-da": "g-07-동사-형용사 + ㅂ니다-습니다 & ㅂ니까-습니까 (Đuôi câu trang trọng)",
    "g-08-myeongsa-eul-leul": "g-08-명사 + 을-를 (Tiểu từ tân ngữ)",
    "g-09-i-geu-jeo-myeongsa": "g-09-이-그-저 + 명사 (Chỉ định từ)",
    "g-10-hanjaeo-su": "g-10-한자어 수 (Số đếm Hán-Hàn - Tiền, điện thoại, phút)",
    "g-11-goyueo-su": "g-11-고유어 수 (Số đếm Thuần Hàn - Tuổi, giờ, đếm vật)",
    "g-12-va-a-eo-yo": "g-12-동사-형용사 + 아-어요 (Đuôi câu thân mật lịch sự)",
    "g-13-myeongsa-e-1": "g-13-명사 + 에 1 (Tiểu từ vị trí - Trạng thái tồn tại)",
    "g-14-myeongsa-hago": "g-14-명사 + 하고 (Và - Cùng với)",
    "g-15-danwi-myeongsa": "g-15-단위 명사 (Danh từ chỉ đơn vị đếm)",
    "g-16-b-bulgyuchik": "g-16-ㅂ 불규칙 (Bất quy tắc phụ âm cuối ㅂ)",
    "g-17-myeongsa-eun-neun-2": "g-17-명사 + 은-는 2 (Tiểu từ chủ đề - So sánh-Đối chiếu)",
    "g-18-an-va-va-ji-anha": "g-18-안 + 동사-형용사 & 동사-형용사-지 않다 (Phủ định - Không)",
    "g-19-myeongsa-eseo": "g-19-명사 + 에서 (Tiểu từ vị trí xảy ra hành động)",
    "g-20-va-go-1": "g-20-동사-형용사 + 고 1 (Và - Liên kết song song)",
    "g-21-myeongsa-e-2": "g-21-명사 + 에 2 (Tiểu từ thời gian)",
    "g-22-myeongsa-do": "g-22-명사 + 도 (Cũng)",
    "g-23-va-at-eot": "g-23-동사-형용사 + 았-었 (Thì quá khứ)",
    "g-24-va-go-2": "g-24-동사 + 고 2 (Rồi - Trình tự hành động)",
    "g-25-va-go-sipda": "g-25-동사 + 고 싶다 (Muốn - Ngôi 1 & 2)",
    "g-26-va-go-sipeo-hada": "g-26-동사 + 고 싶어 하다 (Muốn - Ngôi 3)",
    "g-27-va-eu-seyo-eu-sipsio": "g-27-동사 + (으)세요 - (으)하십시오 (Mệnh lệnh lịch sự)",
    "g-28-myeongsa-eu-ro-1": "g-28-명사 + (으)로 1 (Chỉ hướng đi)",
    "g-29-myeongsa-ege-hante-kke": "g-29-명사 + 에게-한테-께 (Cho ai, tới ai)",
    "g-30-eu-tallak": "g-30-으 탈락 (Giản lược nguyên âm ㅡ)",
    "g-31-va-jiman": "g-31-동사-형용사 + 지만 (Nhưng - Đối lập)",
    "g-32-myeongsa-boda": "g-32-명사 + 보다 (So với... thì hơn)",
    "g-33-myeongsa-man": "g-33-명사 + 만 (Chỉ)",
    "g-34-myeongsa-eu-ro-2": "g-34-명사 + (으)로 2 (Phương tiện, cách thức, chất liệu)",
    "g-35-myeongsa-eseo-buteo-kkaji": "g-35-명사 + 에서-부터 ... 명사 + 까지 (Từ... đến...)",
    "g-36-va-a-eo-seo-1": "g-36-동사 + 아-어서 1 (Rồi - Liên kết trạng thái)",
    "g-37-va-eu-si": "g-37-동사-형용사 + (으)시 (Kính ngữ)",
    "g-38-myeongsa-ege-seo-hante-seo-kke": "g-38-명사 + 에게서-한테서 (Từ ai đó)",
    "g-39-va-eu-l-geomnida-geoyeyo": "g-39-동사-형용사 + (으)ㄹ 겁니다 - 거예요 (Thì tương lai - Dự đoán)",
    "g-40-va-eu-l-kka-yo-eu-b-sida": "g-40-동사 + (으)ㄹ까요 & (으)ㅂ시다 (Rủ rê, đề nghị)",
    "g-41-mot-va-va-ji-mothada": "g-41-못 + 동사 & 동사-지 못하다 (Không thể)",
    "g-42-va-get-1": "g-42-동사 + 겠 1 (Ý chí, cam kết trang trọng)",
    "g-43-l-tallak": "g-43-ㄹ 탈락 (Bất quy tắc phụ âm cuối ㄹ)",
    "g-44-va-eu-l-su-itta-eopda": "g-44-동사 + (으)ㄹ 수 있다-없다 (Có thể - Không thể)",
    "g-45-va-a-eo-seo-2": "g-45-동사-형용사 + 아-어서 2 (Vì... nên... - Lý do khách quan)",
    "g-46-va-ji-malda": "g-46-동사 + 지 말다 (Đừng làm gì)", # match exactly
    "g-47-va-eu-l-ge-yo": "g-47-동사 + (으)ㄹ게요 (Hứa hẹn, thông báo)",
    "g-48-va-eu-ni-kka-1": "g-48-동사-형용사 + (으)니까 1 (Vì... nên... - Lý do chủ quan)",
    "g-49-va-go-itta": "g-49-동사 + 고 있다 (Đang - Tiếp diễn)",
    "g-50-myeongsa-gwa-wa": "g-50-명사 + 과-와 (Và - Với - Trang trọng)"
}

# Thư mục gốc học liệu
ROOT_DIR = r"t:\Topik\giao trình kyung hee\MD_korea_learning"

def update_links_in_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    original_content = content
    
    # 1. Cập nhật các link dạng [[concepts/g-XX-name]] hoặc [[wiki/concepts/g-XX-name]]
    # Obsidian wikilink regex: [[link_target(|display_text)?]]
    def replacer(match):
        full_link = match.group(1)
        display_text = match.group(2) if match.group(2) else ""
        
        # Lấy tên file gốc từ target
        target_clean = full_link.split("/")[-1].replace(".md", "").strip()
        
        # Nếu đó là một link grammar
        if target_clean in GRAMMAR_LINK_MAPPING:
            new_target = GRAMMAR_LINK_MAPPING[target_clean]
            # Giữ nguyên nhãn hiển thị hoặc tự động thêm nhãn hiển thị nếu cần thiết
            if display_text:
                return f"[[{new_target}{display_text}]]"
            else:
                return f"[[{new_target}]]"
                
        # Nếu đó là một link vocabulary dạng [[concepts/v-XX]] hay [[wiki/concepts/v-XX]]
        if target_clean.startswith("v-") and any(ch.isdigit() for ch in target_clean):
            # Từ vựng giữ nguyên tên file La-tinh nhưng đã được chuyển vào vocabulary/
            # Obsidian có thể tự nhận diện, nhưng để an toàn và nhất quán, ta chỉ cần giữ nguyên target sạch v-XX-name
            if display_text:
                return f"[[{target_clean}{display_text}]]"
            else:
                return f"[[{target_clean}]]"
                
        return match.group(0)

    # Regex nhận diện [[wikilinks]]
    # Group 1: target link, Group 2: |display text
    pattern = r"\[\[([^\|\]]+)(\|[^\]]+)?\]\]"
    content = re.sub(pattern, replacer, content)
    
    # 2. Sửa các đường dẫn tương đối trực tiếp trong văn bản nếu có (như concepts/g-*.md hay concepts/v-*.md)
    # Ví dụ trong index.md có các đường dẫn file:// hoặc tương đương, hay link tương đối
    for old_g, new_g in GRAMMAR_LINK_MAPPING.items():
        content = content.replace(f"concepts/{old_g}.md", f"concepts/grammar/{new_g}.md")
        content = content.replace(f"concepts/{old_g}", f"concepts/grammar/{new_g}")
        
    # Từ vựng v-*.md sang concepts/vocabulary/v-*.md
    content = re.sub(r"concepts/(v-\d+[^.\n]*)", r"concepts/vocabulary/\1", content)
    
    if content != original_content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        return True
    return False

def run_link_update():
    updated_files = 0
    # Quét tất cả các file .md trong MD_korea_learning
    for root, dirs, files in os.walk(ROOT_DIR):
        # Bỏ qua thư mục .obsidian và các thư mục ẩn khác
        if ".obsidian" in root:
            continue
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                if update_links_in_file(file_path):
                    updated_files += 1
                    
    print(f"Link update completed: updated links in {updated_files} markdown files.")

if __name__ == "__main__":
    run_link_update()
