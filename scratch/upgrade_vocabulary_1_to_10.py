# -*- coding: utf-8 -*-
import os
import re

# Cơ sở dữ liệu từ vựng cốt lõi "1 suy 10" chi tiết sư phạm
VOCAB_DATABASE_1_TO_10 = {
    # V-01 Trạng từ
    "보통": {
        "conjugation": "Không chia đuôi động từ trực tiếp (là trạng từ). Thường dùng làm trạng ngữ đứng trước động/tính từ.",
        "antonyms": "특별히 (theuk-byeol-hi): đặc biệt / 가끔 (ga-kkeum): thỉnh thoảng",
        "synonyms": "대개 (dae-gae): đại khái/thông thường / 일반적으로 (il-ban-jeok-eu-ro): một cách thông thường / 평소 (pyeong-so): ngày thường/bình thường",
        "phrases": "보통 주말에 (bo-tong ju-mal-e): thường vào cuối tuần / 평소대로 하다 (pyeong-so-dae-ro ha-da): làm như bình thường",
        "related": "주말 (cuối tuần), 습관 (thói quen), 자주 (thường xuyên), 일상 (hàng ngày), 일과 (lịch trình ngày)"
    },
    "조금": {
        "conjugation": "Là trạng từ chỉ mức độ. Dạng rút gọn thường dùng trong văn nói là 좀 (jom).",
        "antonyms": "많이 (man-i): nhiều / 매우 (mae-u): rất/cực kỳ / 아주 (a-ju): rất/quá",
        "synonyms": "약간 (yak-gan): hơi hơi/một ít / 요만큼 (yo-man-kheum): một chút này thôi",
        "phrases": "조금만 기다려 주세요 (jo-geum-man gi-da-ryeo ju-se-yo): xin vui lòng chờ một chút / 좀 도와주세요 (jom do-wa-ju-se-yo): hãy giúp tôi một chút",
        "related": "양 (lượng), 부족하다 (thiếu), 줄이다 (giảm bớt), 약간의 차이 (khác biệt nhỏ)"
    },
    "아주": {
        "conjugation": "Là trạng từ chỉ mức độ cực độ. Thường đi với tính từ để nhấn mạnh.",
        "antonyms": "조금 (jo-geum): một chút / 별로 (byeol-lo): không... lắm (đi với phủ định)",
        "synonyms": "매우 (mae-u): rất / 무척 (mu-cheok): vô cùng / 엄청 (eom-cheong): cực kỳ/quá chừng / 대단히 (dae-dan-hi): cực kỳ/rất",
        "phrases": "아주 좋습니다 (a-ju jop-seun-ni-da): rất tốt/đẹp / 무척 기쁩니다 (mu-cheok gi-ppeun-ni-da): vô cùng vui mừng",
        "related": "최고 (tốt nhất), 극도로 (cực kỳ), 감탄 (cảm thán),강조 (nhấn mạnh)"
    },
    "항상": {
        "conjugation": "Trạng từ chỉ tần suất tuyệt đối (100%). Không đứng độc lập làm vị ngữ.",
        "antonyms": "가끔 (ga-kkeum): thỉnh thoảng / 전혀 (jeon-hyeo): hoàn toàn không (đi với phủ định)",
        "synonyms": "늘 (neul): luôn luôn/hoài / 언제나 (eon-je-na): bất cứ lúc nào/luôn luôn / 평생 (pyeong-saeng): suốt đời",
        "phrases": "언제나 준비 완료 (eon-je-na jun-bi wan-ryo): luôn luôn chuẩn bị sẵn sàng / 늘 하던 대로 (neul ha-deon dae-ro): luôn làm như cũ",
        "related": "매일 (mỗi ngày), 규칙적 (mang tính quy tắc), 끊임없이 (liên tục không ngừng)"
    },
    "가끔": {
        "conjugation": "Trạng từ chỉ tần suất thấp. Có thể đứng đầu câu làm trạng ngữ.",
        "antonyms": "항상 (hang-sang): luôn luôn / 자주 (ja-ju): thường xuyên / 매일 (mae-il): mỗi ngày",
        "synonyms": "종종 (jong-jong): thỉnh thoảng/thường / 때때로 (ttae-ttae-ro): đôi khi/đôi lúc / 드물게 (deu-mul-ge): hiếm khi",
        "phrases": "가끔 생각이 나다 (ga-kkeum saeng-gak-i na-da): thỉnh thoảng lại nhớ về / 때때로 방문하다 (ttae-ttae-ro bang-mun-ha-da): thỉnh thoảng ghé thăm",
        "related": "특별한 날 (ngày đặc biệt), 예외 (ngoại lệ), 드문 일 (việc hiếm gặp)"
    },

    # V-03 Daily Activities
    "공부하다": {
        "conjugation": "공부해요 (하다 -> 해요). Chia thì quá khứ: 공부했어요. Kính ngữ: 공부하십니다 / 공부하세요.",
        "antonyms": "놀다 (nol-da): chơi / 쉬다 (swi-da): nghỉ ngơi",
        "synonyms": "배우다 (bae-u-da): học / 학습하다 (hak-seup-ha-da): học tập / 익히다 (ik-hi-da): luyện tập cho quen",
        "phrases": "열심히 공부하다 (yeol-sim-hi gong-bu-ha-da): học tập chăm chỉ / 책을 읽고 배우다 (chaek-eul il-go bae-u-da): đọc sách học hỏi",
        "related": "도서관 (thư viện), 학교 (trường học), 시험 (kỳ thi), 교과서 (sách giáo khoa), 숙제 (bài tập về nhà)"
    },
    "일하다": {
        "conjugation": "일해요 (하다 -> 해요). Quá khứ: 일했어요. Kính ngữ: 일하십니다 / 일하세요.",
        "antonyms": "쉬다 (swi-da): nghỉ ngơi / 퇴직하다 (thoe-jik-ha-da): nghỉ hưu",
        "synonyms": "근무하다 (geun-mu-ha-da): làm việc/trực / 직장 생활을 하다 (jik-jang saeng-hwal-eul ha-da): sinh hoạt công sở",
        "phrases": "늦게까지 일하다 (neut-ge-kka-ji il-ha-da): làm việc tới muộn / 돈을 벌다 (don-eul beol-da): kiếm tiền",
        "related": "회사 (công ty), 사무실 (văn phòng), 상사 (cấp trên), 동료 (đồng nghiệp), 야근 (làm ca đêm)"
    },
    "자다": {
        "conjugation": "자요 (가다 giống 자요 - nguyên âm 아). Kính ngữ đặc biệt: 주무시다 (ju-mu-si-da) -> 주무세요 / 주무십니다. Quá khứ: 잤어요.",
        "antonyms": "일어나다 (il-eo-na-da): thức dậy / 깨다 (kkae-da): tỉnh giấc",
        "synonyms": "취침하다 (chwi-chim-ha-da): đi ngủ (trang trọng) / 잠을 자다 (jam-eul ja-da): ngủ giấc ngủ",
        "phrases": "늦잠을 자다 (neut-jam-eul ja-da): ngủ nướng/ngủ trễ / 단잠을 자다 (dan-jam-eul ja-da): ngủ ngon giấc",
        "related": "침대 (giường), 이불 (chăn), 베개 (gối), 꿈 (giấc mơ), 피곤하다 (mệt mỏi)"
    },

    # V-04 School Study
    "지각하다": {
        "conjugation": "지각해요 (하다 -> 해요). Quá khứ: 지각했어요. Kính ngữ: 지각하십니다 / 지각하세요.",
        "antonyms": "조기 도착하다 (jo-gi do-chak-ha-da): đến sớm / 제시간에 오다 (je-si-gan-e o-da): đến đúng giờ",
        "synonyms": "늦다 (neut-da): trễ/muộn / 지체하다 (ji-che-ha-da): chậm trễ",
        "phrases": "학교에 늦게 가다 (hak-gyo-e neut-ge ga-da): đi học trễ / 제시간에 가지 못하다 (je-si-gan-e ga-ji mot-ha-da): không thể đi đúng giờ",
        "related": "늦잠 (ngủ nướng), 알람 (chuông báo), 버스를 놓치다 (lỡ xe buýt), 서두르다 (vội vã)"
    },
    "시험": {
        "conjugation": "Danh từ. Đi kèm động từ 치다 hoặc 보다 thành 시험을 치다 / 시험을 보다 (thi/làm bài kiểm tra).",
        "antonyms": "방학 (bang-hak): kỳ nghỉ hè/đông / 휴가 (hyu-ga): kỳ nghỉ",
        "synonyms": "테스트 (the-seu-theu): bài kiểm tra / 고사 (go-sa): kỳ thi cử / 평가 (pyeong-ga): đánh giá",
        "phrases": "시험을 보다 (si-heom-eul bo-da): làm bài thi / 시험에 합격하다 (si-heom-e hap-gyeok-ha-da): thi đỗ / 시험에 떨어지다 (si-heom-e tteo-reo-ji-da): thi trượt",
        "related": "공부 (học bài), 성적 (thành tích), 점수 (điểm số), 합격 (đỗ), 불합격 (trượt)"
    },
    "가르치다": {
        "conjugation": "가르쳐요 (치 + 어요 -> 쳐요). Quá khứ: 가르쳤어요. Kính ngữ: 가르치십니다 / 가르치세요.",
        "antonyms": "배우다 (bae-u-da): học / 공부하다 (gong-bu-ha-da): học bài",
        "synonyms": "지도하다 (ji-do-ha-da): chỉ dẫn/hướng dẫn / 교육하다 (gyo-yuk-ha-da): giáo dục",
        "phrases": "한국어를 가르치다 (han-guk-eo-r-ga-reu-chi-da): dạy tiếng Hàn / 지식을 전하다 (ji-sik-eul jeon-ha-da): truyền đạt tri thức",
        "related": "선생님 (giáo viên), 학생 (học sinh), 교실 (lớp học), 수업 (giờ học), 칠판 (bảng đen)"
    },

    # V-11 Health Hospital
    "아프다": {
        "conjugation": "아파요 (bất quy tắc 'ㅡ': Giản lược 'ㅡ', kết hợp với '-아요' vì âm tiết trước '아' có nguyên âm '아'). Quá khứ: 아팠어요. Kính ngữ: 아프십니다 / 편찮으시다 (pyeon-chan-eu-si-da - Kính ngữ đặc biệt của đau yếu).",
        "antonyms": "건강하다 (geon-gang-ha-da): khỏe mạnh / 낫다 (nat-da): khỏi bệnh",
        "synonyms": "병들다 (byeong-deul-da): mắc bệnh / 통증이 있다 (thong-jeung-i it-da): có triệu chứng đau",
        "phrases": "머리가 아프다 (meo-ri-ga a-feu-da): đau đầu / 몸이 안 좋다 (mom-i an jop-da): người không khỏe",
        "related": "병원 (bệnh viện), 약 (thuốc), 의사 (bác sĩ), 열이 나다 (bị sốt), 기침 (ho)"
    },
    "약": {
        "conjugation": "Danh từ. Đi kèm với động từ 먹다 thành 약을 먹다 (uống thuốc - tiếng Hàn dùng từ 'ăn' thuốc).",
        "antonyms": "독 (dok): chất độc / 병원균 (byeong-won-gyun): mầm bệnh",
        "synonyms": "약품 (yak-pum): dược phẩm / 치료제 (chi-ryo-je): chất điều trị",
        "phrases": "약국에서 약을 사다 (yak-guk-e-seo yak-eul sa-da): mua thuốc ở hiệu thuốc / 약을 먹다 (yak-eul meok-da): uống thuốc",
        "related": "약사 (dược sĩ), 약국 (tiệm thuốc), 처방전 (đơn thuốc), 물약 (thuốc nước), 알약 (thuốc viên)"
    },

    # V-02 Weather
    "춥다": {
        "conjugation": "추워요 (bất quy tắc 'ㅂ': 'ㅂ' biến thành '우' + '어요' -> '워요'). Quá khứ: 추웠어요. Gặp phụ âm: 춥고 (chup-go), 춥지만 (chup-ji-man).",
        "antonyms": "덥다 (deop-da): nóng",
        "synonyms": "쌀쌀하다 (ssal-ssal-ha-da): se se lạnh / 선선하다 (seon-seon-ha-da): mát mẻ",
        "phrases": "날씨가 아주 춥다 (nal-si-ga a-ju chup-da): thời tiết rất lạnh / 기온이 영하로 떨어지다 (gi-on-i yeong-ha-ro tteo-reo-ji-da): nhiệt độ giảm xuống dưới 0",
        "related": "겨울 (mùa đông), 눈 (tuyết), 얼음 (băng), 코트 (áo khoác), 난로 (lò sưởi)"
    },
    "덥다": {
        "conjugation": "더워요 (bất quy tắc 'ㅂ': 'ㅂ' biến thành '우' + '어요' -> '워요'). Quá khứ: 더웠어요. Gặp phụ âm: 덥고 (deop-go), 덥지만 (deop-ji-man).",
        "antonyms": "춥다 (chup-da): lạnh",
        "synonyms": "무덥다 (mu-deop-da): oi bức/nóng ẩm / 후끈하다 (hu-kkeun-ha-da): nóng hừng hực",
        "phrases": "더위를 타다 (deo-wi-r-tha-da): nhạy cảm với cái nóng / 에어컨을 켜다 (e-eo-kheon-eul kyeo-da): bật điều hòa",
        "related": "여름 (mùa hè), 땀 (mồ hôi), 해수욕장 (bãi tắm biển), 아이스크림 (kem), 선풍기 (quạt máy)"
    },

    # V-05 Family
    "바쁘다": {
        "conjugation": "바빠요 (bất quy tắc 'ㅡ': Giản lược 'ㅡ', kết hợp với '-아요' vì âm trước '바' có nguyên âm '아'). Quá khứ: 바빴어요. Gặp phụ âm: 바쁘고, 바쁘지만.",
        "antonyms": "한가하다 (han-ga-ha-da): rảnh rỗi / 여유롭다 (yeo-yu-rop-da): thong thả",
        "synonyms": "정신이 없다 (jeong-sin-i eop-da): bận tối mắt tối mũi / 분주하다 (bun-ju-ha-da): bận rộn tấp nập",
        "phrases": "할 일이 아주 많다 (hal il-i a-ju man-ta): có rất nhiều việc phải làm / 정신없이 바쁘다 (jeong-sin-eop-si ba-ppeu-da): bận tối tăm mặt mũi",
        "related": "시간이 없다 (không có thời gian), 회의 (cuộc họp), 마감일 (hạn chót - deadline), 야근 (làm thêm giờ)"
    }
}

# Tải danh sách file từ vựng cũ
def run_vocab_upgrade():
    base_dir = r"t:\Topik\giao trình kyung hee\MD_korea_learning\wiki\concepts"
    dest_dir = os.path.join(base_dir, "vocabulary")
    
    # Quét tất cả file v-*.md
    vocab_files = [f for f in os.listdir(base_dir) if f.startswith("v-") and f.endswith(".md")]
    
    success_count = 0
    for v_file in vocab_files:
        old_path = os.path.join(base_dir, v_file)
        new_path = os.path.join(dest_dir, v_file)
        
        with open(old_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Nâng cấp mạng lưới 1 suy 10 cho các từ cốt lõi có trong file
        # Ta sẽ quét qua phần "## 🔗 2. Mạng Nơ-ron Liên tưởng" cũ và thay thế bằng mạng 1 suy 10 sư phạm
        lines = content.split('\n')
        new_lines = []
        in_network_section = False
        skip_old_network = False
        
        for line in lines:
            # Khi phát hiện tiêu đề mạng liên tưởng cũ
            if "## 🔗 2. Mạng Nơ-ron Liên tưởng" in line:
                in_network_section = True
                new_lines.append(line)
                new_lines.append("")
                new_lines.append("Dưới đây là mạng lưới liên tưởng nơ-ron học sâu **1 suy 10** giúp kết nối từ trái nghĩa, từ đồng nghĩa, biến thể chia đuôi bất quy tắc `-아/어/여요`, cụm từ thay thế/diễn đạt tương đương và từ liên quan cùng trường từ vựng:")
                new_lines.append("")
                continue
                
            # Khi gặp phần bài tập Kyung Hee tiếp theo
            if in_network_section and ("## 💬 3. Bài tập" in line or "## 📖 3. Bài tập" in line or "## 💬 4. Bài tập" in line or "## 🎴 3. Bài tập" in line or line.startswith("---") and "Bài tập" in "".join(lines[lines.index(line):lines.index(line)+5])):
                in_network_section = False
                skip_old_network = False
                
            if in_network_section:
                # Bỏ qua nội dung cũ của phần mạng liên tưởng
                continue
                
            new_lines.append(line)
            
        # Tạo khối Mạng liên tưởng mới chất lượng cao 1 suy 10
        network_content = []
        found_any_core = False
        for core_word, info in VOCAB_DATABASE_1_TO_10.items():
            # Kiểm tra xem từ cốt lõi này có thuộc tệp từ vựng hiện tại không bằng cách tìm kiếm từ đó trong file
            if core_word in content:
                found_any_core = True
                network_content.append(f"### 🔑 Từ cốt lõi: **{core_word}**")
                network_content.append(f"- ⚙️ **Chia đuôi `-아/어/여요` & Bất quy tắc**: {info['conjugation']}")
                network_content.append(f"- ⚔️ **Từ trái nghĩa (Antonym)**: {info['antonyms']}")
                network_content.append(f"- 🔄 **Từ đồng nghĩa / Gần nghĩa (Synonym)**: {info['synonyms']}")
                network_content.append(f"- 🤝 **Cụm từ thay thế / Diễn đạt tương đương**: {info['phrases']}")
                network_content.append(f"- 🧠 **Các từ liên quan (Related Words)**: {info['related']}")
                network_content.append("")
                
        # Nếu không tìm thấy từ cốt lõi nào trong cơ sở dữ liệu mẫu, ta sinh mẫu tự động cho từ vựng trong file
        if not found_any_core:
            # Tìm các từ vựng từ danh sách thẻ ghi nhớ :: trong file
            card_words = []
            for line in lines:
                if "::" in line and not line.startswith(">") and not line.startswith("-"):
                    parts = line.split("::")
                    word = parts[0].strip().replace("- ", "")
                    # Lấy từ tiếng Hàn sạch
                    word_clean = re.sub(r'[^ㄱ-ㅎㅏ-ㅣ가-힣]', '', word)
                    if len(word_clean) >= 2:
                        card_words.append(word_clean)
            
            # Lấy tối đa 3 từ để sinh tự động
            for w in card_words[:3]:
                network_content.append(f"### 🔑 Từ cốt lõi: **{w}**")
                network_content.append(f"- ⚙️ **Chia đuôi `-아/어/여요` & Bất quy tắc**: Chia theo nguyên âm cuối của gốc từ (Hạ đuôi `아요/어요`).")
                network_content.append(f"- ⚔️ **Từ trái nghĩa (Antonym)**: Đang cập nhật từ trái nghĩa của từ '{w}'...")
                network_content.append(f"- 🔄 **Từ đồng nghĩa / Gần nghĩa (Synonym)**: Đang cập nhật từ đồng nghĩa...")
                network_content.append(f"- 🤝 **Cụm từ thay thế / Diễn đạt tương đương**: Dùng kết hợp cụm với động từ chính.")
                network_content.append(f"- 🧠 **Các từ liên quan (Related Words)**: Liên kết với chủ đề học liệu.")
                network_content.append("")
                
        # Chèn mạng liên tưởng mới vào vị trí thích hợp
        # Tìm chỉ số dòng của "## 🔗 2. Mạng Nơ-ron Liên tưởng" trong new_lines
        idx_to_insert = -1
        for i, line in enumerate(new_lines):
            if "## 🔗 2. Mạng Nơ-ron Liên tưởng" in line:
                idx_to_insert = i + 3 # Sau dòng mô tả
                break
                
        if idx_to_insert != -1:
            new_lines = new_lines[:idx_to_insert] + network_content + new_lines[idx_to_insert:]
            
        # Ghi nội dung mới vào file đích
        final_content = "\n".join(new_lines)
        
        # Sửa đường dẫn tham chiếu index.md và grammar_guide.md tương đối ở đầu file
        final_content = final_content.replace("[[wiki/index.md]]", "[[index.md]]")
        final_content = final_content.replace("[[grammar_guide.md]]", "[[../../grammar_guide.md]]")
        
        with open(new_path, "w", encoding="utf-8") as f:
            f.write(final_content)
            
        success_count += 1
        
    print(f"Vocabulary migration completed: upgraded {success_count} files.")

if __name__ == "__main__":
    run_vocab_upgrade()
