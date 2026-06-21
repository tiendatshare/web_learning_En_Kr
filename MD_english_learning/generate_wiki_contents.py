# -*- coding: utf-8 -*-
import os
import sys
from pathlib import Path

# Set default encoding to UTF-8
if sys.platform == 'win32':
    os.environ['PYTHONUTF8'] = '1'

output_base = Path(r"T:\Topik\giao trình kyung hee\MD_english_learning\wiki")
vocab_dir = output_base / "concepts" / "vocabulary"
grammar_dir = output_base / "concepts" / "grammar"
situations_dir = output_base / "situations"
exam_prep_dir = output_base / "exam_prep"

# Ensure dirs exist
vocab_dir.mkdir(parents=True, exist_ok=True)
grammar_dir.mkdir(parents=True, exist_ok=True)
situations_dir.mkdir(parents=True, exist_ok=True)
exam_prep_dir.mkdir(parents=True, exist_ok=True)

# 1. Generate Vocabulary files (v-04 to v-12)
vocab_files_data = {
    "v-04-adventure-discovery": {
        "title": "Từ vựng Nền tảng: Unit 4 — Phiêu lưu & Khám phá",
        "source": "4000 Essential English Words 1 — Units 16-20",
        "level": "A2-B1 (Pre-Intermediate)",
        "cards": [
            ("actual", "/ˈæktʃuəl/", "thực tế, thực sự", "5"),
            ("amaze", "/əˈmeɪz/", "làm kinh ngạc", "5"),
            ("charge", "/tʃɑːdʒ/", "tính phí, sạc điện", "5"),
            ("comfort", "/ˈkʌmfət/", "sự thoải mái, an ủi", "5"),
            ("contact", "/ˈkɒntækt/", "liên lạc, tiếp xúc", "5"),
            ("customer", "/ˈkʌstəmər/", "khách hàng", "5"),
            ("deliver", "/dɪˈlɪvər/", "giao hàng", "5"),
            ("earn", "/ɜːn/", "kiếm tiền, giành được", "5"),
            ("gate", "/ɡeɪt/", "cổng", "4"),
            ("include", "/ɪnˈkluːd/", "bao gồm", "5"),
            ("manage", "/ˈmænɪdʒ/", "quản lý, xoay xở", "5"),
            ("mystery", "/ˈmɪstəri/", "bí ẩn", "6"),
            ("occur", "/əˈkɜːr/", "xảy ra", "6"),
            ("opposite", "/ˈɒpəzɪt/", "đối diện, ngược lại", "5"),
            ("plate", "/pleɪt/", "đĩa", "4"),
            ("receive", "/rɪˈsiːv/", "nhận được", "5"),
            ("reward", "/rɪˈwɔːd/", "phần thưởng", "5"),
            ("set", "/set/", "thiết lập, bộ", "4"),
            ("steal", "/stiːl/", "ăn trộm", "4"),
            ("thief", "/θiːf/", "kẻ trộm", "5"),
        ],
        "chunking": [
            ("amaze", "amaze", "làm kinh ngạc", "be amazed by", "We were amazed by (bị kinh ngạc bởi) the beautiful sunset (cảnh hoàng hôn đẹp)."),
            ("manage", "manage", "quản lý, xoay xở", "manage to do sth", "She managed to open (xoay xở mở được) the heavy gate (cánh cổng nặng)."),
        ],
        "neural": [
            ("amaze", "astonish, surprise, astound", "bore, tire", "amazement (n.), amazing (adj.)", "amaze + audience/people"),
            ("mystery", "secret, puzzle, enigma", "clarity, truth", "mysterious (adj.), mysteriously (adv.)", "solve a mystery"),
        ],
        "reading": (
            "The story (Câu chuyện) of a young girl (về một cô gái trẻ) who loved adventure (người yêu thích phiêu lưu) "
            "and managed (và đã xoay xở) to solve a mystery (giải quyết một điều bí ẩn) in the forest. "
            "She discovered (Cô ấy đã phát hiện) that the actual (thực tế) gate (cánh cổng) to the castle (dẫn vào lâu đài) "
            "was hidden (được giấu) on the opposite side (ở phía đối diện) of the lake. "
            "She received (Cô ấy đã nhận được) a great reward (một phần thưởng lớn) for her bravery (vì lòng dũng cảm)."
        )
    },
    "v-05-lifestyle-characters": {
        "title": "Từ vựng Nền tảng: Unit 5 — Lối sống & Nhân vật",
        "source": "4000 Essential English Words 1 — Units 21-25",
        "level": "A2-B1 (Pre-Intermediate)",
        "cards": [
            ("volunteer", "/ˌvɒlənˈtɪər/", "tình nguyện viên", "5"),
            ("clerk", "/klɑːk/", "thư ký, nhân viên bán hàng", "5"),
            ("pain", "/peɪn/", "sự đau đớn", "5"),
            ("locate", "/ləʊˈkeɪt/", "xác định vị trí", "5"),
            ("root", "/ruːt/", "rễ cây, gốc rễ", "5"),
            ("brain", "/breɪn/", "não bộ", "5"),
            ("hero", "/ˈhɪərəʊ/", "anh hùng", "5"),
            ("enter", "/ˈentər/", "đi vào", "4"),
            ("although", "/ɔːlˈðəʊ/", "mặc dù", "4"),
            ("strength", "/streŋθ/", "sức mạnh", "5"),
            ("refuse", "/rɪˈfjuːz/", "từ chối", "5"),
            ("attempt", "/əˈtempt/", "cố gắng, nỗ lực", "5"),
            ("operation", "/ˌɒpəˈreɪʃn/", "hoạt động, ca phẫu thuật", "6"),
            ("inform", "/ɪnˈfɔːm/", "thông báo", "5"),
            ("peaceful", "/ˈpiːsfl/", "yên bình", "5"),
            ("leave", "/liːv/", "rời đi, để lại", "4"),
            ("early", "/ˈɜːli/", "sớm", "4"),
            ("career", "/kəˈrɪər/", "sự nghiệp", "5"),
            ("various", "/ˈveəriəs/", "đa dạng, nhiều", "5"),
            ("else", "/els/", "khác, nữa", "4"),
        ],
        "chunking": [
            ("refuse", "refuse", "từ chối", "refuse to do sth", "He refused to leave (từ chối rời đi) the peaceful room (căn phòng yên bình)."),
            ("attempt", "attempt", "cố gắng", "make an attempt to", "She made an attempt to (đã nỗ lực để) enter the career (bước vào sự nghiệp)."),
        ],
        "neural": [
            ("refuse", "decline, reject, turn down", "accept, agree, consent", "refusal (n.)", "refuse an offer/invitation"),
            ("strength", "power, energy, force", "weakness, fragility", "strengthen (v.), strong (adj.)", "physical/mental strength"),
        ],
        "reading": (
            "Although (Mặc dù) he was only a clerk (anh ấy chỉ là một thư ký), he volunteered (đã tình nguyện) "
            "to help the doctors (giúp đỡ các bác sĩ) in a difficult operation (trong một ca phẫu thuật khó khăn). "
            "His bravery (Sự dũng cảm của anh) made him a local hero (biến anh thành người anh hùng địa phương). "
            "He refused (Anh ấy đã từ chối) to take any money (nhận bất kỳ khoản tiền nào) and preferred to see (và muốn nhìn thấy) "
            "patients live a peaceful life (bệnh nhân sống một cuộc sống yên bình)."
        )
    },
    "v-06-lessons-conclusions": {
        "title": "Từ vựng Nền tảng: Unit 6 — Bài học & Kết luận",
        "source": "4000 Essential English Words 1 — Units 26-30",
        "level": "A2-B1 (Pre-Intermediate)",
        "cards": [
            ("direct", "/dəˈrekt/", "trực tiếp, hướng dẫn", "5"),
            ("description", "/dɪˈskrɪpʃn/", "sự miêu tả", "5"),
            ("exam", "/ɪɡˈzæm/", "kỳ thi", "4"),
            ("example", "/ɪɡˈzɑːmpl/", "ví dụ", "4"),
            ("limit", "/ˈlɪmɪt/", "giới hạn", "5"),
            ("local", "/ˈləʊkl/", "địa phương", "5"),
            ("magical", "/ˈmædʒɪkl/", "kỳ diệu", "5"),
            ("mail", "/meɪl/", "thư từ", "4"),
            ("novel", "/ˈnɒvl/", "tiểu thuyết, mới mẻ", "5"),
            ("outline", "/ˈaʊtlaɪn/", "dàn ý, phác thảo", "5"),
            ("poet", "/ˈpəʊɪt/", "nhà thơ", "5"),
            ("print", "/prɪnt/", "in ấn", "4"),
            ("scene", "/siːn/", "cảnh tượng, hiện trường", "5"),
            ("sheet", "/ʃiːt/", "tờ (giấy), ga trải giường", "4"),
            ("silly", "/ˈsɪli/", "ngớ ngẩn", "4"),
            ("store", "/stɔːr/", "cửa hàng, lưu trữ", "4"),
            ("suffer", "/ˈsʌfər/", "chịu đựng, đau khổ", "5"),
            ("technology", "/tekˈnɒlədʒi/", "công nghệ", "5"),
            ("coach", "/kəʊtʃ/", "huấn luyện viên, xe khách", "5"),
            ("control", "/kənˈtrəʊl/", "kiểm soát", "5"),
        ],
        "chunking": [
            ("suffer", "suffer", "chịu đựng", "suffer from", "Many people suffer from (chịu đựng từ) stress (sự căng thẳng)."),
            ("control", "control", "kiểm soát", "under control", "Everything is under control (mọi thứ đang trong tầm kiểm soát) now."),
        ],
        "neural": [
            ("direct", "straight, immediate", "indirect, devious", "direction (n.), directly (adv.)", "direct contact/link"),
            ("control", "command, rule, regulate", "yield, submit", "controller (n.)", "lose control, in control"),
        ],
        "reading": (
            "The poet (Nhà thơ) wrote a novel (đã viết một cuốn tiểu thuyết) about local technology (về công nghệ địa phương). "
            "He printed (Anh ấy đã in) the draft (bản thảo) on a sheet of paper (trên một tờ giấy). "
            "He gave a direct description (đưa ra một miêu tả trực tiếp) of how people suffer (về cách mọi người đau khổ) "
            "when they cannot control (khi họ không thể kiểm soát) their own lives (cuộc sống của chính họ)."
        )
    },
    "v-07-skills-talents": {
        "title": "Từ vựng Trung cấp: Unit 7 — Kỹ năng & Tài năng",
        "source": "4000 Essential English Words 2 — Units 1-5",
        "level": "B1-B2 (Intermediate)",
        "cards": [
            ("anxious", "/ˈæŋkʃəs/", "lo lắng", "5"),
            ("awful", "/ˈɔːfl/", "kinh khủng", "5"),
            ("consist", "/kənˈsɪst/", "bao gồm (consist of)", "5"),
            ("desire", "/dɪˈzaɪər/", "khao khát, thèm muốn", "6"),
            ("eager", "/ˈiːɡər/", "hăm hở, hăng hái", "5"),
            ("household", "/ˈhaʊshəʊld/", "hộ gia đình", "5"),
            ("intent", "/ɪnˈtent/", "ý định", "6"),
            ("landscape", "/ˈlændskeɪp/", "phong cảnh", "5"),
            ("lift", "/lɪft/", "nâng lên, thang máy", "4"),
            ("load", "/ləʊd/", "gánh nặng, vật nặng", "5"),
            ("lung", "/lʌŋ/", "phổi", "5"),
            ("motion", "/ˈməʊʃn/", "sự chuyển động", "5"),
            ("pace", "/peɪs/", "nhịp độ, tốc độ", "5"),
            ("polite", "/pəˈlaɪt/", "lịch sự", "5"),
            ("possess", "/pəˈzes/", "sở hữu", "6"),
            ("rapidly", "/ˈræpɪdli/", "nhanh chóng", "5"),
            ("remark", "/rɪˈmɑːk/", "nhận xét", "6"),
            ("seek", "/siːk/", "tìm kiếm", "6"),
            ("shine", "/ʃaɪn/", "tỏa sáng", "4"),
            ("spill", "/spɪl/", "làm tràn, đổ ra", "5"),
        ],
        "chunking": [
            ("anxious", "anxious", "lo lắng", "be anxious about", "She was anxious about (lo lắng về) the exam result (kết quả thi)."),
            ("seek", "seek", "tìm kiếm", "seek information", "They seek information (tìm kiếm thông tin) about the landscape (phong cảnh)."),
        ],
        "neural": [
            ("anxious", "worried, concerned, nervous", "calm, relaxed, peaceful", "anxiety (n.), anxiously (adv.)", "anxious about/for"),
            ("possess", "own, have, hold", "lose, lack", "possession (n.), possessive (adj.)", "possess skills/qualities"),
        ],
        "reading": (
            "She was eager (Cô ấy đã hăng hái) to possess (sở hữu) the skills (những kỹ năng) "
            "needed for the household (cần thiết cho hộ gia đình). "
            "Rapidly (Nhanh chóng), she learned the motion (cô ấy đã học được chuyển động) of lifting heavy loads (của việc nâng vật nặng). "
            "Her polite remarks (Những lời nhận xét lịch sự của cô) made everyone pleased (làm mọi người hài lòng)."
        )
    },
    "v-08-environment-nature": {
        "title": "Từ vựng Trung cấp: Unit 8 — Môi trường & Tự nhiên",
        "source": "4000 Essential English Words 2 — Units 6-10",
        "level": "B1-B2 (Intermediate)",
        "cards": [
            ("climate", "/ˈklaɪmət/", "khí hậu", "5"),
            ("decline", "/dɪˈklaɪn/", "suy giảm", "6"),
            ("ecosystem", "/ˈiːkəʊsɪstəm/", "hệ sinh thái", "6"),
            ("fossil", "/ˈfɒsl/", "hóa thạch", "6"),
            ("geological", "/ˌdʒiːəˈlɒdʒɪkl/", "thuộc địa chất", "7"),
            ("massive", "/ˈmæsɪv/", "to lớn, khổng lồ", "6"),
            ("carbon", "/ˈkɑːbən/", "các-bon", "6"),
            ("cycle", "/ˈsaɪkl/", "chu kỳ", "5"),
            ("dense", "/dens/", "dày đặc, đông đúc", "6"),
            ("layer", "/ˈleɪər/", "tầng, lớp", "5"),
            ("oxygen", "/ˈɒksɪdʒən/", "ô-xy", "5"),
            ("release", "/rɪˈliːs/", "thải ra, giải phóng", "6"),
            ("shift", "/ʃɪft/", "sự dịch chuyển, ca làm", "5"),
            ("soil", "/sɔɪl/", "đất trồng", "5"),
            ("source", "/sɔːs/", "nguồn", "5"),
            ("temperature", "/ˈtemprətʃər/", "nhiệt độ", "5"),
            ("threat", "/θret/", "mối đe dọa", "5"),
            ("tropical", "/ˈtrɒpɪkl/", "nhiệt đới", "5"),
            ("vegetation", "/ˌvedʒəˈteɪʃn/", "thảm thực vật", "7"),
            ("acid", "/ˈæsɪd/", "a-xít", "6"),
        ],
        "chunking": [
            ("decline", "decline", "suy giảm", "sharp decline in", "There is a sharp decline in (sự suy giảm mạnh về) forest areas (diện tích rừng)."),
            ("release", "release", "thải ra", "release carbon dioxide", "Factories release carbon dioxide (các nhà máy thải khí CO2) into the atmosphere (vào bầu khí quyển)."),
        ],
        "neural": [
            ("decline", "decrease, drop, diminish", "increase, rise, grow", "decline (n.)", "decline an offer, decline in numbers"),
            ("massive", "huge, gigantic, enormous", "tiny, small", "massively (adv.)", "massive scale/impact"),
        ],
        "reading": (
            "Climate change (Biến đổi khí hậu) is a massive threat (là mối đe dọa khổng lồ) to the tropical ecosystem (đối với hệ sinh thái nhiệt đới). "
            "The decline (Sự suy giảm) in vegetation (thảm thực vật) affects the soil quality (ảnh hưởng đến chất lượng đất). "
            "Burning fossil fuels (Đốt nhiên liệu hóa thạch) releases carbon (thải khí các-bon) and raises the temperature (và làm tăng nhiệt độ) of the earth."
        )
    },
    "v-09-society-culture": {
        "title": "Từ vựng Trung cấp: Unit 9 — Xã hội & Văn hóa",
        "source": "4000 Essential English Words 2 — Units 11-15",
        "level": "B1-B2 (Intermediate)",
        "cards": [
            ("alliance", "/əˈlaɪəns/", "liên minh", "6"),
            ("civilization", "/ˌsɪvəlaɪˈzeɪʃn/", "nền văn minh", "6"),
            ("culture", "/ˈkʌltʃər/", "văn hóa", "5"),
            ("custom", "/ˈkʌstəm/", "phong tục", "5"),
            ("empire", "/ˈempaɪər/", "đế chế", "6"),
            ("historic", "/hɪˈstɒrɪk/", "mang tính lịch sử", "6"),
            ("origin", "/ˈɒrɪdʒɪn/", "nguồn gốc", "5"),
            ("practice", "/ˈpræktɪs/", "thực hành, lệ thường", "5"),
            ("ritual", "/ˈrɪtʃuəl/", "nghi lễ", "6"),
            ("society", "/səˈsaɪəti/", "xã hội", "5"),
            ("tradition", "/trəˈdɪʃn/", "truyền thống", "5"),
            ("value", "/ˈvæljuː/", "giá trị", "5"),
            ("ancestral", "/ænˈsestrəl/", "thuộc tổ tiên", "6"),
            ("artifact", "/ˈɑːtɪfækt/", "cổ vật, hiện vật", "6"),
            ("heritage", "/ˈherɪtɪdʒ/", "di sản", "6"),
            ("indigenous", "/ɪnˈdɪdʒənəs/", "bản địa", "7"),
            ("legend", "/ˈledʒənd/", "truyền thuyết", "5"),
            ("myth", "/mɪθ/", "thần thoại", "5"),
            ("tribe", "/traɪb/", "bộ tộc, bộ lạc", "5"),
            ("customary", "/ˈkʌstəməri/", "theo phong tục", "6"),
        ],
        "chunking": [
            ("heritage", "heritage", "di sản", "cultural heritage", "We must protect (chúng ta phải bảo vệ) our cultural heritage (di sản văn hóa của mình)."),
            ("indigenous", "indigenous", "bản địa", "indigenous people", "The custom of indigenous people (phong tục của người bản địa) is historic (mang tính lịch sử)."),
        ],
        "neural": [
            ("heritage", "legacy, inheritance", "none", "inherit (v.)", "cultural/natural heritage"),
            ("indigenous", "native, local, aboriginal", "foreign, alien", "indigenously (adv.)", "indigenous population/culture"),
        ],
        "reading": (
            "Every society (Mỗi xã hội) has its own culture (có nền văn hóa riêng) and customs (và các phong tục). "
            "The indigenous tribe (Bộ lạc bản địa) preserved (đã gìn giữ) their ancestral rituals (các nghi lễ của tổ tiên). "
            "Artifacts (Cổ vật) from the historic empire (từ đế chế lịch sử) show the values (cho thấy những giá trị) "
            "and heritage (và di sản) that they passed down (mà họ truyền lại)."
        )
    },
    "v-10-technology-innovation": {
        "title": "Từ vựng Trung cấp: Unit 10 — Công nghệ & Sáng tạo",
        "source": "4000 Essential English Words 2 — Units 16-20",
        "level": "B1-B2 (Intermediate)",
        "cards": [
            ("accelerate", "/əkˈseləreɪt/", "tăng tốc, thúc đẩy", "6"),
            ("calculate", "/ˈkælkjʊleɪt/", "tính toán", "5"),
            ("device", "/dɪˈvaɪs/", "thiết bị", "5"),
            ("dynamic", "/daɪˈnæmɪk/", "năng động, động lực", "6"),
            ("input", "/ˈɪnpʊt/", "đầu vào", "5"),
            ("output", "/ˈaʊtpʊt/", "đầu ra", "5"),
            ("process", "/ˈprəʊses/", "quy trình, xử lý", "5"),
            ("network", "/ˈnetwɜːk/", "mạng lưới", "5"),
            ("digital", "/ˈdɪdʒɪtl/", "kỹ thuật số", "5"),
            ("virtual", "/ˈvɜːtʃuəl/", "ảo, thực tế ảo", "6"),
            ("program", "/ˈprəʊɡræm/", "chương trình", "4"),
            ("platform", "/ˈplætfɔːm/", "nền tảng", "5"),
            ("code", "/kəʊd/", "mã, mật mã", "5"),
            ("run", "/rʌn/", "chạy, điều hành", "4"),
            ("technology", "/tekˈnɒlədʒi/", "công nghệ", "5"),
            ("user", "/ˈjuːzər/", "người dùng", "4"),
            ("automate", "/ˈɔːtəmeɪt/", "tự động hóa", "6"),
            ("efficiency", "/ɪˈfɪʃnsi/", "hiệu suất, sự hiệu quả", "6"),
            ("implement", "/ˈɪmplɪment/", "triển khai", "6"),
            ("optimize", "/ˈɒptɪmaɪz/", "tối ưu hóa", "6"),
        ],
        "chunking": [
            ("optimize", "optimize", "tối ưu hóa", "optimize performance", "We can optimize performance (chúng ta có thể tối ưu hóa hiệu suất) of the device (của thiết bị)."),
            ("implement", "implement", "triển khai", "implement a system", "They decided to implement (họ đã quyết định triển khai) a new digital platform (một nền tảng số mới)."),
        ],
        "neural": [
            ("optimize", "maximize, improve, enhance", "worsen, impair", "optimization (n.), optimal (adj.)", "optimize resources/processes"),
            ("efficiency", "effectiveness, productivity", "waste, inefficiency", "efficient (adj.), efficiently (adv.)", "improve/increase efficiency"),
        ],
        "reading": (
            "Modern technology (Công nghệ hiện đại) has accelerated (đã thúc đẩy) the process of digital automation (quy trình tự động hóa kỹ thuật số). "
            "By implementing smart devices (Bằng cách triển khai các thiết bị thông minh), "
            "we optimize the network output (chúng ta tối ưu hóa đầu ra của mạng) and increase overall efficiency (và tăng hiệu suất toàn diện)."
        )
    },
    "v-11-business-economy": {
        "title": "Từ vựng Trung cấp: Unit 11 — Kinh doanh & Kinh tế",
        "source": "4000 Essential English Words 2 — Units 21-25",
        "level": "B1-B2 (Intermediate)",
        "cards": [
            ("asset", "/ˈæset/", "tài sản", "6"),
            ("capital", "/ˈkæpɪtl/", "vốn, thủ đô", "5"),
            ("budget", "/ˈbʌdʒɪt/", "ngân sách", "5"),
            ("cost", "/kɒst/", "chi phí", "4"),
            ("debt", "/det/", "khoản nợ", "5"),
            ("income", "/ˈɪnkʌm/", "thu nhập", "5"),
            ("market", "/ˈmɑːkɪt/", "thị trường", "4"),
            ("profit", "/ˈprɒfɪt/", "lợi nhuận", "5"),
            ("revenue", "/ˈrevənjuː/", "doanh thu", "6"),
            ("risk", "/rɪsk/", "rủi ro", "4"),
            ("value", "/ˈvæljuː/", "giá trị", "5"),
            ("wealth", "/welθ/", "sự giàu có, của cải", "5"),
            ("finance", "/ˈfaɪnæns/", "tài chính", "5"),
            ("financial", "/faɪˈnænʃl/", "thuộc tài chính", "5"),
            ("fund", "/fʌnd/", "quỹ, tài trợ", "5"),
            ("invest", "/ɪnˈvest/", "đầu tư", "5"),
            ("investment", "/ɪnˈvestmənt/", "khoản đầu tư", "5"),
            ("management", "/ˈmænɪdʒmənt/", "sự quản lý", "5"),
            ("commercial", "/kəˈmɜːʃl/", "thuộc thương mại", "5"),
            ("customer", "/ˈkʌstəmər/", "khách hàng", "5"),
        ],
        "chunking": [
            ("invest", "invest", "đầu tư", "invest in stocks", "It is wise (thật khôn ngoan) to invest in education (đầu tư vào giáo dục)."),
            ("revenue", "revenue", "doanh thu", "generate revenue", "New products help (các sản phẩm mới giúp) generate revenue (tạo ra doanh thu) rapidly (nhanh chóng)."),
        ],
        "neural": [
            ("revenue", "income, proceeds, turnover", "expenditure, loss", "none", "annual/total revenue"),
            ("asset", "property, wealth, possession", "liability, debt", "none", "valuable asset, liquid assets"),
        ],
        "reading": (
            "Managing a business budget (Quản lý ngân sách kinh doanh) requires balancing costs and income (đòi hỏi sự cân bằng chi phí và thu nhập). "
            "To increase profit (Để tăng lợi nhuận), companies must invest capital (các công ty phải đầu tư vốn) "
            "into commercial assets (vào các tài sản thương mại) while minimizing financial risks (trong khi giảm thiểu rủi ro tài chính)."
        )
    },
    "v-12-history-literature": {
        "title": "Từ vựng Trung cấp: Unit 12 — Lịch sử & Văn học",
        "source": "4000 Essential English Words 2 — Units 26-30",
        "level": "B1-B2 (Intermediate)",
        "cards": [
            ("author", "/ˈɔːθər/", "tác giả", "5"),
            ("document", "/ˈdɒkjʊmənt/", "tài liệu, tư liệu", "5"),
            ("history", "/ˈhɪstəri/", "lịch sử", "4"),
            ("literature", "/ˈlɪtrətʃər/", "văn học", "5"),
            ("read", "/riːd/", "đọc", "4"),
            ("source", "/sɔːs/", "nguồn, tư liệu gốc", "5"),
            ("text", "/tekst/", "văn bản", "4"),
            ("write", "/raɪt/", "viết", "4"),
            ("book", "/bʊk/", "sách", "4"),
            ("chapter", "/ˈtʃæptər/", "chương", "4"),
            ("context", "/ˈkɒntekst/", "ngữ cảnh, bối cảnh", "5"),
            ("style", "/staɪl/", "phong cách", "5"),
            ("subject", "/ˈsʌbdʒɪkt/", "chủ đề, môn học", "4"),
            ("theme", "/θiːm/", "chủ đề (văn học)", "6"),
            ("title", "/ˈtaɪtl/", "tiêu đề, danh hiệu", "4"),
            ("academic", "/ˌækəˈdemɪk/", "thuộc học thuật", "5"),
            ("formal", "/ˈfɔːml/", "trang trọng", "5"),
            ("essay", "/ˈeseɪ/", "bài luận", "5"),
            ("paper", "/ˈpeɪpər/", "giấy, bài báo cáo", "4"),
            ("research", "/rɪˈsɜːtʃ/", "nghiên cứu", "5"),
        ],
        "chunking": [
            ("context", "context", "ngữ cảnh", "historical context", "To understand the text (để hiểu được văn bản), consider its historical context (hãy xem xét bối cảnh lịch sử của nó)."),
            ("academic", "academic", "học thuật", "academic writing", "Academic writing (Viết học thuật) requires a formal style (đòi hỏi một phong cách trang trọng)."),
        ],
        "neural": [
            ("context", "background, setting, circumstances", "none", "contextual (adj.), contextualize (v.)", "in context, out of context"),
            ("academic", "scholarly, educational", "practical, non-academic", "academy (n.), academically (adv.)", "academic career/achievement"),
        ],
        "reading": (
            "The author researched (Tác giả đã nghiên cứu) many historical documents (nhiều tài liệu lịch sử) "
            "to write this book on classic literature (để viết cuốn sách này về văn học cổ điển). "
            "Each chapter (Mỗi chương) explores a unique theme (khám phá một chủ đề độc đáo) "
            "within the academic context (trong bối cảnh học thuật) of the nineteenth century (của thế kỷ 19)."
        )
    }
}

for fname, data in vocab_files_data.items():
    fpath = vocab_dir / f"{fname}.md"
    cards_str = "\n".join([f"- {word} {ipa} :: {meaning} | #IELTS-{tag}" for word, ipa, meaning, tag in data["cards"]])
    chunk_str = ""
    for word, w_eng, w_vie, col, sentence in data["chunking"]:
        chunk_str += f"### {word}\n- **Từ đơn**: {w_eng} → {w_vie}\n- **Collocations**: {col}\n- **Câu hoàn chỉnh**: {sentence}\n\n"
    neural_str = ""
    for word, syn, ant, family, col in data["neural"]:
        neural_str += f"### {word}\n- 🔄 **Đồng nghĩa**: {syn}\n- ⚡ **Trái nghĩa**: {ant}\n- 🔗 **Word Family**: {family}\n- 🎯 **Collocations**: {col}\n\n"

    content = f"""# {data['title']}

> Nguồn: {data['source']}
> Tổng số từ: {len(data['cards'])} từ | Trình độ: {data['level']}

---

## Phần 1: Bảng Flashcard Spaced Repetition

{cards_str}

---

## Phần 2: Chunking Progression (Phát triển Cụm từ)

{chunk_str}
---

## Phần 3: Mạng Liên tưởng Nơ-ron (Neural Association Network)

{neural_str}
---

## Phần 4: Bài tập Đọc Ứng dụng — Dịch xen kẽ

{data['reading']}

---

## Liên kết Wiki
- [[index]] — Quay lại Mục lục
"""
    fpath.write_text(content, encoding='utf-8')
    print(f"Generated: {fpath.name}")


# 2. Generate IELTS Vocabulary files
ielts_files_data = {
    "v-ielts-cam09": {
        "title": "Từ vựng IELTS: Cambridge IELTS 9 — Boost Your Vocabulary",
        "source": "A&M IELTS — Boost your vocabulary (Cambridge IELTS 9)",
        "cards": [
            ("synthetic", "/sɪnˈθetɪk/", "nhân tạo, do con người chế tạo (artificial, man-made)", "6"),
            ("dye", "/daɪ/", "thuốc nhuộm, màu nhuộm (color, pigment)", "6"),
            ("curiosity", "/ˌkjuəriˈɒsəti/", "sự tò mò, lòng hiếu kỳ", "5"),
            ("prompt", "/prɒmpt/", "thúc đẩy, gợi ý (encourage, stimulate)", "5"),
            ("stumble across", "/ˈstʌmbl əˈkrɒs/", "tình cờ bắt gặp, phát hiện ngẫu nhiên", "6"),
            ("run-down", "/rʌn daʊn/", "xuống cấp, tồi tàn", "6"),
            ("solidify", "/səˈlɪdɪfaɪ/", "củng cố, làm cho chắc chắn", "6"),
            ("devotion", "/dɪˈvəʊʃn/", "sự tận tụy, cống hiến", "6"),
            ("perceive", "/pəˈsiːv/", "nhận thức, cảm nhận", "6"),
            ("eminent", "/ˈemɪnənt/", "nổi tiếng, lỗi lạc (famous, prominent)", "7"),
            ("breakthrough", "/ˈbreɪkθruː/", "bước đột phá", "6"),
            ("viable", "/ˈvaɪəbl/", "khả thi, có thể thành công", "6"),
            ("surpass", "/səˈpɑːs/", "vượt qua, trội hơn", "6"),
            ("substitute", "/ˈsʌbstɪtjuːt/", "vật thay thế, thay thế", "5"),
        ],
        "reading": (
            "William Henry Perkin stumbled across (tình cờ phát hiện) a run-down (xuống cấp) laboratory "
            "in his house. His scientific curiosity prompted (thúc đẩy sự tò mò khoa học của anh) him to experiment. "
            "He made a major breakthrough (bước đột phá lớn) by inventing the first synthetic (nhân tạo) dye (thuốc nhuộm)."
        )
    },
    "v-ielts-cam10": {
        "title": "Từ vựng IELTS: Cambridge IELTS 10 — Boost Your Vocabulary",
        "source": "A&M IELTS — Boost your vocabulary (Cambridge IELTS 10)",
        "cards": [
            ("innovative", "/ˈɪnəveɪtɪv/", "sáng tạo, đổi mới (creative)", "6"),
            ("incentive", "/ɪnˈsentɪv/", "sự khuyến khích, động lực", "6"),
            ("industrialize", "/ɪnˈdʌstriəlaɪz/", "công nghiệp hóa", "6"),
            ("urbanization", "/ˌɜːbənaɪˈzeɪʃn/", "đô thị hóa", "6"),
            ("sustain", "/səˈsteɪn/", "duy trì, chống đỡ", "6"),
            ("subsequent", "/ˈsʌbsɪkwənt/", "xảy ra sau, tiếp theo", "6"),
            ("regulate", "/ˈreɡjʊleɪt/", "điều chỉnh, quy định", "6"),
            ("distinction", "/dɪˈstɪŋkʃn/", "sự khác biệt, nét độc đáo", "6"),
            ("crucial", "/ˈkruːʃl/", "quan trọng, then chốt", "6"),
            ("flourish", "/ˈflʌrɪʃ/", "phát triển mạnh mẽ, hưng thịnh", "6"),
        ],
        "reading": (
            "Urbanization (Đô thị hóa) and industrialization (công nghiệp hóa) occurred in Britain. "
            "It was crucial (rất quan trọng) to sustain (duy trì) clean water resources. "
            "Subsequent regulations (Các quy định tiếp theo) helped local industries flourish (phát triển mạnh mẽ)."
        )
    },
    "v-ielts-cam11": {
        "title": "Từ vựng IELTS: Cambridge IELTS 11 — Boost Your Vocabulary",
        "source": "A&M IELTS — Boost your vocabulary (Cambridge IELTS 11)",
        "cards": [
            ("crop", "/krɒp/", "vụ mùa, cây trồng", "5"),
            ("scarcity", "/ˈskeəsəti/", "sự khan hiếm", "6"),
            ("agricultural", "/ˌæɡrɪˈkʌltʃərəl/", "thuộc nông nghiệp", "5"),
            ("irrigation", "/ˌɪrɪˈɡeɪʃn/", "sự tưới tiêu, hệ thống tưới", "6"),
            ("drought", "/draʊt/", "hạn hán", "6"),
            ("deplete", "/dɪˈpliːt/", "làm suy yếu, làm cạn kiệt", "6"),
            ("infrastructure", "/ˈɪnfrəstrʌktʃər/", "cơ sở hạ tầng", "6"),
            ("consumption", "/kənˈsʌmpʃn/", "sự tiêu thụ", "5"),
            ("reclaim", "/rɪˈcleɪm/", "cải tạo, thu hồi", "6"),
            ("sustainable", "/səˈsteɪnəbl/", "bền vững", "6"),
        ],
        "reading": (
            "Drought (Hạn hán) caused water scarcity (gây ra sự khan hiếm nước) in many agricultural regions (vùng nông nghiệp). "
            "Deficient irrigation infrastructure (Cơ sở hạ tầng tưới tiêu kém) depleted (làm cạn kiệt) the groundwater. "
            "Sustainable water consumption (Tiêu thụ nước bền vững) is now needed (hiện đang rất cần thiết)."
        )
    },
    "v-ielts-cam12": {
        "title": "Từ vựng IELTS: Cambridge IELTS 12 — Boost Your Vocabulary",
        "source": "A&M IELTS — Boost your vocabulary (Cambridge IELTS 12)",
        "cards": [
            ("automation", "/ˌɔːtəˈmeɪʃn/", "sự tự động hóa", "6"),
            ("redundancy", "/rɪˈdʌndənsi/", "sự dư thừa, sa thải do thừa nhân sự", "6"),
            ("cognitive", "/ˈkɒɡnətɪv/", "thuộc nhận thức", "6"),
            ("monopolize", "/məˈnɒpəlaɪz/", "độc chiếm, độc quyền", "7"),
            ("algorithm", "/ˈælɡərɪðəm/", "thuật toán", "6"),
            ("prediction", "/prɪˈdɪkʃn/", "sự dự đoán", "5"),
            ("enhance", "/ɪnˈhɑːns/", "nâng cao, cải thiện", "6"),
            ("artificial intelligence", "/ˌɑːtɪˈfɪʃl ɪnˈtelɪɡəns/", "trí tuệ nhân tạo (AI)", "6"),
            ("expertise", "/ˌekspɜːˈtiːz/", "chuyên môn", "6"),
            ("adapt", "/əˈdæpt/", "thích nghi, phỏng theo", "5"),
        ],
        "reading": (
            "Automation (Sự tự động hóa) and artificial intelligence (trí tuệ nhân tạo) are transforming jobs. "
            "Algorithms (Các thuật toán) can now make accurate predictions (dự đoán chính xác). "
            "Workers must adapt (phải thích nghi) and enhance their cognitive expertise (nâng cao chuyên môn nhận thức của họ)."
        )
    },
    "v-ielts-cam13": {
        "title": "Từ vựng IELTS: Cambridge IELTS 13 — Boost Your Vocabulary",
        "source": "A&M IELTS — Boost your vocabulary (Cambridge IELTS 13)",
        "cards": [
            ("sediment", "/ˈsedɪmənt/", "phù sa, cặn, trầm tích", "7"),
            ("delta", "/ˈdeltə/", "đồng bằng châu thổ", "6"),
            ("barrier", "/ˈbæriər/", "rào cản, chướng ngại vật", "5"),
            ("displace", "/dɪsˈpleɪs/", "di dời, thay thế", "6"),
            ("coastal", "/ˈkəʊstl/", "thuộc duyên hải, bờ biển", "5"),
            ("erosion", "/ɪˈrəʊʒn/", "sự xói mòn", "6"),
            ("divert", "/daɪˈvɜːt/", "chuyển hướng", "6"),
            ("deposit", "/dɪˈpɒzɪt/", "lắng đọng, gửi tiền", "5"),
            ("salinity", "/səˈlɪnəti/", "độ mặn", "7"),
            ("nutrient", "/ˈnjuːtriənt/", "chất dinh dưỡng", "6"),
        ],
        "reading": (
            "Dams divert river flow (Các con đập chuyển hướng dòng chảy sông) and trap sediment (giữ lại phù sa). "
            "Without sediment deposits (Nếu không có sự lắng đọng phù sa), the delta (đồng bằng châu thổ) "
            "suffers from coastal erosion (chịu sự xói mòn bờ biển), and salinity levels rise (độ mặn tăng lên)."
        )
    },
    "v-ielts-cam14": {
        "title": "Từ vựng IELTS: Cambridge IELTS 14 — Boost Your Vocabulary",
        "source": "A&M IELTS — Boost your vocabulary (Cambridge IELTS 14)",
        "cards": [
            ("spatial", "/ˈspeɪʃl/", "thuộc không gian", "6"),
            ("navigate", "/ˈnævɪɡeɪt/", "định vị, hướng đi", "6"),
            ("neurological", "/ˌnjʊərəˈlɒdʒɪkl/", "thuộc thần kinh", "7"),
            ("perception", "/pəˈsepʃn/", "sự nhận thức, cảm giác", "6"),
            ("sensory", "/ˈsensəri/", "thuộc giác quan", "6"),
            ("stimulate", "/ˈstɪmjʊleɪt/", "kích thích", "6"),
            ("landmark", "/ˈlændmɑːk/", "cột mốc, điểm định hướng", "6"),
            ("orientation", "/ˌɔːriənˈteɪʃn/", "sự định hướng", "6"),
            ("internal map", "/ɪnˈtɜːnl mæp/", "bản đồ nội tâm, sơ đồ tư duy", "6"),
            ("evolutionary", "/ˌiːvəˈluːʃnəri/", "thuộc tiến hóa", "7"),
        ],
        "reading": (
            "Animals navigate (động vật định vị hướng đi) using sensory cues (các tín hiệu giác quan). "
            "Their neurological system (Hệ thống thần kinh của chúng) creates an internal map (tạo ra một bản đồ nội tâm) "
            "based on landmarks (dựa trên các cột mốc). This spatial perception (nhận thức không gian này) is evolutionary (mang tính tiến hóa)."
        )
    },
    "v-ielts-cam15": {
        "title": "Từ vựng IELTS: Cambridge IELTS 15 — Boost Your Vocabulary",
        "source": "A&M IELTS — Boost your vocabulary (Cambridge IELTS 15)",
        "cards": [
            ("subsistence", "/səbˈsɪstəns/", "sự đủ ăn đủ sống, tự cấp tự túc", "7"),
            ("commercialization", "/kəˌmɜːʃəlaɪˈzeɪʃn/", "sự thương mại hóa", "6"),
            ("commodity", "/kəˈmɒdəti/", "hàng hóa", "6"),
            ("infrastructure", "/ˈɪnfrəstrʌktʃər/", "cơ sở hạ tầng", "6"),
            ("cooperative", "/kəʊˈɒpərətɪv/", "hợp tác xã, hợp tác", "5"),
            ("yield", "/jiːld/", "sản lượng, lợi nhuận", "6"),
            ("fluctuation", "/ˌflʌktʃuˈeɪʃn/", "sự dao động, biến động", "6"),
            ("poverty", "/ˈpɒvəti/", "sự nghèo đói", "5"),
            ("market access", "/ˈmɑːkɪt ˈækses/", "tiếp cận thị trường", "6"),
            ("supply chain", "/səˈplaɪ tʃeɪn/", "chuỗi cung ứng", "6"),
        ],
        "reading": (
            "Subsistence farming (Canh tác tự cấp tự túc) is shifted (được chuyển đổi) to commercialization (thương mại hóa). "
            "Small cooperatives (Các hợp tác xã nhỏ) improve market access (cải thiện sự tiếp cận thị trường). "
            "However, price fluctuations (tuy nhiên, sự biến động giá cả) in commodities (ở các mặt hàng) cause poverty (gây ra nghèo đói)."
        )
    },
    "v-ielts-cam16": {
        "title": "Từ vựng IELTS: Cambridge IELTS 16 — Boost Your Vocabulary",
        "source": "A&M IELTS — Boost your vocabulary (Cambridge IELTS 16)",
        "cards": [
            ("biodiverse", "/ˌbaɪəʊdaɪˈvɜːs/", "đa dạng sinh học", "6"),
            ("restoration", "/ˌrestəˈreɪʃn/", "sự phục hồi, khôi phục", "6"),
            ("conservationist", "/ˌkɒnsəˈveɪʃənɪst/", "nhà bảo tồn thiên nhiên", "6"),
            ("habitat loss", "/ˈhæbɪtæt lɒs/", "mất môi trường sống", "6"),
            ("endangered species", "/ɪnˈdeɪndʒəd ˈspiːʃiːz/", "loài có nguy cơ tuyệt chủng", "6"),
            ("rewilding", "/ˌriːˈwaɪldɪŋ/", "tái hoang dã, phục hồi thiên nhiên hoang sơ", "7"),
            ("corridor", "/ˈkɒrɪdɔːr/", "hành lang (sinh học/đường đi)", "6"),
            ("predator", "/ˈpredətər/", "thú săn mồi", "6"),
            ("ecosystem service", "/ˈiːkəʊsɪstəm ˈsɜːvɪs/", "dịch vụ hệ sinh thái", "7"),
            ("indigenous", "/ɪnˈdɪdʒənəs/", "bản địa", "7"),
        ],
        "reading": (
            "Rewilding (Tái hoang dã) aims to reverse habitat loss (nhằm mục đích đảo ngược việc mất môi trường sống). "
            "Conservationists create biological corridors (Các nhà bảo tồn tạo ra các hành lang sinh học) "
            "for endangered species (cho các loài nguy cơ tuyệt chủng) to travel and connect ecosystems."
        )
    },
    "v-ielts-cam17": {
        "title": "Từ vựng IELTS: Cambridge IELTS 17 — Boost Your Vocabulary",
        "source": "A&M IELTS — Boost your vocabulary (Cambridge IELTS 17)",
        "cards": [
            ("archaeologist", "/ˌɑːkiˈɒlədʒɪst/", "nhà khảo cổ học", "6"),
            ("relic", "/ˈrelɪk/", "di tích, di vật", "6"),
            ("excavate", "/ˈekskəveɪt/", "khai quật", "7"),
            ("civilization", "/ˌsɪvəlaɪˈzeɪʃn/", "nền văn minh", "6"),
            ("predecessor", "/ˈpriːdɪsesər/", "người/vật tiền nhiệm, tổ tiên", "6"),
            ("monument", "/ˈmɒnjʊmənt/", "đài tưởng niệm, công trình lớn", "6"),
            ("inscription", "/ɪnˈskrɪpʃn/", "chữ khắc, văn khắc", "6"),
            ("chronological", "/ˌkrɒnəˈlɒdʒɪkl/", "theo thứ tự thời gian", "6"),
            ("dynasty", "/ˈdɪnəsti/", "triều đại", "6"),
            ("heritage", "/ˈherɪtɪdʒ/", "di sản", "6"),
        ],
        "reading": (
            "Archaeologists excavated (Các nhà khảo cổ học đã khai quật) the ancient monument (công trình cổ đại). "
            "They found stone relics (Họ tìm thấy các di vật bằng đá) with detailed inscriptions (với các chữ khắc chi tiết). "
            "This helped put the dynasty (giúp đặt triều đại) in chronological order (theo thứ tự thời gian)."
        )
    },
    "v-ielts-cam18": {
        "title": "Từ vựng IELTS: Cambridge IELTS 18 — Boost Your Vocabulary",
        "source": "A&M IELTS — Boost your vocabulary (Cambridge IELTS 18)",
        "cards": [
            ("sustainability", "/səˌsteɪnəˈbɪləti/", "sự bền vững", "6"),
            ("biodegradable", "/ˌbaɪəʊdɪˈɡreɪdəbl/", "có thể phân hủy sinh học", "6"),
            ("microplastics", "/ˌmaɪkrəʊˈplæstɪks/", "hạt vi nhựa", "7"),
            ("toxin", "/ˈtɒksɪn/", "chất độc", "6"),
            ("accumulation", "/əˌkjuːmjʊˈleɪʃn/", "sự tích tụ, tích lũy", "6"),
            ("pollutant", "/pəˈluːtənt/", "chất gây ô nhiễm", "6"),
            ("regulation", "/ˌreɡjʊˈleɪʃn/", "quy định, luật lệ", "5"),
            ("alternative", "/ɔːlˈtɜːnətɪv/", "giải pháp thay thế", "5"),
            ("recycle", "/ˌriːˈsaɪkl/", "tái chế", "5"),
            ("consumer", "/kənˈsjuːmər/", "người tiêu dùng", "5"),
        ],
        "reading": (
            "Consumer goods (Hàng hóa tiêu dùng) generate waste. We need biodegradable alternatives (chúng ta cần các giải pháp phân hủy sinh học) "
            "to prevent the accumulation of microplastics (để ngăn chặn sự tích tụ hạt vi nhựa). "
            "Strict regulations (Các quy định nghiêm ngặt) against pollutants (chống lại chất gây ô nhiễm) are required."
        )
    },
    "v-ielts-mindset45": {
        "title": "Từ vựng IELTS: Mindset for IELTS 4.0-5.0 — Boost Your Vocabulary",
        "source": "A&M IELTS — Boost your vocabulary (Mindset for IELTS 4.0-5.0)",
        "cards": [
            ("leisure", "/ˈleʒər/", "thời gian rảnh rỗi, thư giãn", "5"),
            ("facility", "/fəˈsɪləti/", "cơ sở vật chất, tiện ích", "5"),
            ("accommodation", "/əˌkɒməˈdeɪʃn/", "chỗ ở, nơi lưu trú", "5"),
            ("transportation", "/ˌtrænspɔːˈteɪʃn/", "giao thông vận tải", "5"),
            ("destination", "/ˌdestɪˈneɪʃn/", "điểm đến", "5"),
            ("sightseeing", "/ˈsaɪtsiːɪŋ/", "tham quan ngắm cảnh", "4"),
            ("attraction", "/əˈtrækʃn/", "điểm thu hút, sự hút khách", "5"),
            ("itinerary", "/aɪˈtɪnərəri/", "lịch trình chuyến đi", "6"),
            ("budget", "/ˈbʌdʒɪt/", "ngân sách", "5"),
            ("experience", "/ɪkˈspɪəriəns/", "trải nghiệm, kinh nghiệm", "5"),
        ],
        "reading": (
            "Our travel itinerary (Lịch trình chuyến đi của chúng tôi) includes sightseeing (bao gồm tham quan ngắm cảnh) "
            "at the city's main attractions (tại các điểm thu hút khách chính của thành phố). "
            "We booked affordable accommodation (Chúng tôi đã đặt chỗ ở giá rẻ) to match our tight budget (để hợp với ngân sách hạn hẹp)."
        )
    }
}

for fname, data in ielts_files_data.items():
    fpath = vocab_dir / f"{fname}.md"
    cards_str = "\n".join([f"- {word} {ipa} :: {meaning} | #IELTS-{tag}" for word, ipa, meaning, tag in data["cards"]])
    content = f"""# {data['title']}

> Nguồn: {data['source']}
> Tổng số từ: {len(data['cards'])} từ | Trình độ: IELTS Band 4.5-7.5

---

## Phần 1: Bảng Flashcard Spaced Repetition

{cards_str}

---

## Phần 2: Đọc hiểu Ứng dụng & Dịch xen kẽ

{data['reading']}

---

## Liên kết Wiki
- [[index]] — Quay lại Mục lục
"""
    fpath.write_text(content, encoding='utf-8')
    print(f"Generated: {fpath.name}")


# 3. Generate Situations files (s-01 to s-05) in Markdown Table Format
situations_data = {
    "s-01-greetings-introductions": {
        "title": "Tình huống Giao tiếp 1: Chào hỏi & Giới thiệu bản thân",
        "turns": [
            ("Sarah", "Hi! I'm Sarah. What's your name?", "/haɪ! aɪm ˈseərə. wɒts jɔː neɪm?/", "Xin chào! Tôi là Sarah. Bạn tên gì?"),
            ("Minh", "Hello, Sarah! My name is Minh. Nice to meet you!", "/həˈləʊ, ˈseərə! maɪ neɪm ɪz mɪŋ. naɪs tə miːt juː!/", "Chào, Sarah! Tên tôi là Minh. Rất vui được gặp bạn!"),
            ("Sarah", "Nice to meet you too, Minh! Where are you from?", "/naɪs tə miːt juː tuː, mɪŋ! weər ɑː juː frɒm?/", "Tôi cũng rất vui được gặp bạn, Minh! Bạn từ đâu đến?"),
            ("Minh", "I'm from Vietnam. I've been living here for about two years.", "/aɪm frɒm ˌviːetˈnæm. aɪv biːn ˈlɪvɪŋ hɪər fɔːr əˈbaʊt tuː jɪəz./", "Tôi đến từ Việt Nam. Tôi đã sống ở đây khoảng hai năm."),
            ("Sarah", "Oh, that's interesting! What do you do?", "/əʊ, ðæts ˈɪntrəstɪŋ! wɒt duː juː duː?/", "Ồ, thú vị quá! Bạn làm nghề gì?"),
            ("Minh", "I'm a software engineer. How about you?", "/aɪm ə ˈsɒftweər ˌendʒɪˈnɪər. haʊ əˈbaʊt juː?/", "Tôi là kỹ sư phần mềm. Còn bạn thì sao?"),
        ],
        "vocab": [
            ("introduce", "/ˌɪntrəˈdjuːs/", "giới thiệu", "5"),
            ("greeting", "/ˈɡriːtɪŋ/", "lời chào", "4"),
            ("occupation", "/ˌɒkjuˈpeɪʃn/", "nghề nghiệp", "6"),
        ]
    },
    "s-02-shopping-restaurant": {
        "title": "Tình huống Giao tiếp 2: Mua sắm & Nhà hàng",
        "turns": [
            ("Assistant", "Hello! Can I help you find anything today?", "/həˈləʊ! kæn aɪ help juː faɪnd ˈeniθɪŋ təˈdeɪ?/", "Xin chào! Tôi có thể giúp bạn tìm gì hôm nay không?"),
            ("Customer", "Yes, please. I'm looking for a blue sweater in medium.", "/jes, pliːz. aɪm ˈlʊkɪŋ fɔːr ə bluː ˈswetər ɪn ˈmiːdiəm./", "Vâng, làm ơn. Tôi đang tìm một chiếc áo len màu xanh dương cỡ vừa."),
            ("Assistant", "We have some over here. Would you like to try it on?", "/wiː hæv sʌm ˈəʊvə hɪər. wʊd juː laɪk tə traɪ ɪt ɒn?/", "Chúng tôi có một vài chiếc ở đằng này. Bạn có muốn thử không?"),
            ("Customer", "Yes, where are the fitting rooms?", "/jes, weər ɑː ðə ˈfɪtɪŋ ruːmz?/", "Có chứ, phòng thử đồ ở đâu vậy?"),
            ("Waiter", "Welcome to Green Bistro. Are you ready to order?", "/ˈwelkəm tə ɡriːn ˈbiːstrəʊ. ɑː juː ˈredi tuː ˈɔːdər?/", "Chào mừng đến Green Bistro. Bạn đã sẵn sàng gọi món chưa?"),
            ("Customer", "Yes, I'll have the grilled salmon with salad, please.", "/jes, aɪl hæv ðə ɡrɪld ˈsæmən wɪð ˈsæləd, pliːz./", "Vâng, cho tôi món cá hồi nướng kèm salad."),
        ],
        "vocab": [
            ("sweater", "/ˈswetər/", "áo len", "4"),
            ("fitting room", "/ˈfɪtɪŋ ruːm/", "phòng thử đồ", "5"),
            ("salmon", "/ˈsæmən/", "cá hồi", "5"),
        ]
    },
    "s-03-travel-transportation": {
        "title": "Tình huống Giao tiếp 3: Giao thông & Du lịch",
        "turns": [
            ("Tourist", "Excuse me, does this bus go to the museum?", "/ɪkˈskjuːz miː, dʌz ðɪs bʌs ɡəʊ tə ðə mjuːˈziːəm?/", "Xin lỗi, xe buýt này có đi đến bảo tàng không?"),
            ("Driver", "No, you need to take bus 14 from the opposite stop.", "/nəʊ, juː niːd tə teɪk bʌs fɔːˈtiːn frəm ðɪs ˈɒpəzɪt stɒp./", "Không, bạn cần đi xe buýt số 14 ở trạm đối diện."),
            ("Tourist", "Oh, I see. How often does that bus run?", "/əʊ, aɪ siː. haʊ ˈɒfn dʌz ðæt bʌs rʌn?/", "Ồ, tôi hiểu rồi. Xe buýt đó bao lâu chạy một chuyến?"),
            ("Driver", "Every fifteen minutes. You can buy a ticket on board.", "/ˈevri ˌfɪfˈtiːn ˈmɪnɪts. juː kæn baɪ ə ˈtɪkɪt ɒn bɔːd./", "Mỗi mười lăm phút. Bạn có thể mua vé trực tiếp trên xe."),
            ("Agent", "Can I see your passport and booking confirmation, please?", "/kæn aɪ siː jɔː ˈpɑːspɔːt ænd ˈbʊkɪŋ ˌkɒnfəˈmeɪʃn, pliːz?/", "Tôi có thể xem hộ chiếu và xác nhận đặt phòng của bạn không?"),
            ("Tourist", "Here they are. Is breakfast included in the room price?", "/hɪər ðeɪ ɑː. ɪz ˈbrekfəst ɪnˈkluːdɪd ɪn ðə ruːm praɪs?/", "Đây ạ. Bữa sáng có bao gồm trong giá phòng không?"),
        ],
        "vocab": [
            ("opposite", "/ˈɒpəzɪt/", "đối diện", "4"),
            ("ticket", "/ˈtɪkɪt/", "vé", "4"),
            ("passport", "/ˈpɑːspɔːt/", "hộ chiếu", "5"),
        ]
    },
    "s-04-health-hospital": {
        "title": "Tình huống Giao tiếp 4: Sức khỏe & Bệnh viện",
        "turns": [
            ("Patient", "Good morning, doctor. I have a terrible headache.", "/ɡʊd ˈmɔːnɪŋ, ˈdɒktər. aɪ hæv ə ˈterəbl ˈhedeɪk./", "Chào buổi sáng bác sĩ. Tôi bị đau đầu kinh khủng."),
            ("Doctor", "How long have you had this headache? Any fever?", "/haʊ lɒŋ hæv juː hæd ðɪs ˈhedeɪk? ˈeni ˈfiːvər?/", "Bạn bị đau đầu bao lâu rồi? Có sốt không?"),
            ("Patient", "It started yesterday. I feel a bit dizzy too.", "/ɪt ˈstɑːtɪd ˈjestədeɪ. aɪ fiːl ə bɪt ˈdɪzi tuː./", "Nó bắt đầu từ hôm qua. Tôi cũng cảm thấy hơi chóng mặt."),
            ("Doctor", "Let me check your blood pressure and temperature.", "/let miː tʃek jɔː blʌd ˈpreʃər ænd ˈtemprətʃər./", "Để tôi kiểm tra huyết áp và nhiệt độ của bạn."),
            ("Doctor", "You need to rest and take this medicine twice a day.", "/juː niːd tə rest ænd teɪk ðɪs ˈmedsn twaɪs ə deɪ./", "Bạn cần nghỉ ngơi và uống thuốc này hai lần một ngày."),
            ("Patient", "Thank you, doctor. When should I come back?", "/θæŋk juː, ˈdɒktər. wen ʃʊd aɪ kʌm bæk?/", "Cảm ơn bác sĩ. Khi nào tôi nên quay lại?"),
        ],
        "vocab": [
            ("headache", "/ˈhedeɪk/", "đau đầu", "4"),
            ("dizzy", "/ˈdɪzi/", "chóng mặt", "5"),
            ("medicine", "/ˈmedsn/", "thuốc", "4"),
        ]
    },
    "s-05-work-interview": {
        "title": "Tình huống Giao tiếp 5: Công việc & Phỏng vấn",
        "turns": [
            ("Interviewer", "Welcome to ABC Tech. Why do you want this job?", "/ˈwelkəm tə ˌeɪbiːˈsiː tek. waɪ duː juː wɒnt ðɪs dʒɒb?/", "Chào mừng đến với ABC Tech. Tại sao bạn muốn công việc này?"),
            ("Candidate", "I want to apply my software engineering skills in this team.", "/aɪ wɒnt tuː əˈplaɪ maɪ ˈsɒftweər ˌendʒɪˈnɪərɪŋ skɪlz ɪn ðɪs tiːm./", "Tôi muốn ứng dụng các kỹ năng kỹ thuật phần mềm của mình vào đội ngũ này."),
            ("Interviewer", "What are your strengths and weaknesses?", "/wɒt ɑː jɔː streŋθs ænd ˈwiːknəsɪz?/", "Điểm mạnh và điểm yếu của bạn là gì?"),
            ("Candidate", "My strength is communication. I'm learning to manage time better.", "/maɪ streŋθ ɪz kəˌmjuːnɪˈkeɪʃn. aɪm ˈlɪnɪŋ tə ˈmænɪdʒ taɪm ˈbetər./", "Điểm mạnh của tôi là giao tiếp. Tôi đang học cách quản lý thời gian tốt hơn."),
            ("Interviewer", "Great! Do you have any questions for us?", "/ɡreɪt! duː juː ˈeni ˈkwestʃənz fɔːr ʌs?/", "Tuyệt! Bạn có câu hỏi nào dành cho chúng tôi không?"),
            ("Candidate", "Yes, what is the training process like here?", "/jes, wɒt ɪz ðə ˈtreɪnɪŋ ˈprəʊses laɪk hɪər?/", "Vâng, quy trình đào tạo ở đây như thế nào ạ?"),
        ],
        "vocab": [
            ("apply", "/əˈplaɪ/", "nộp hồ sơ, ứng dụng", "5"),
            ("candidate", "/ˈkændɪdət/", "ứng viên", "6"),
            ("strength", "/streŋθ/", "điểm mạnh", "5"),
        ]
    }
}

for fname, data in situations_data.items():
    fpath = situations_dir / f"{fname}.md"
    
    # Dialog parsing INTO Markdown Table
    turns_str = "| Nhân vật | Câu nói tiếng Anh | Phiên âm | Bản dịch |\n| :--- | :--- | :--- | :--- |\n"
    for speaker, text, ipa, translation in data["turns"]:
        turns_str += f"| **{speaker}** | {text} | {ipa} | {translation} |\n"
        
    # Vocab parsing
    vocab_str = "\n".join([f"- {word} {ipa} :: {meaning} | #IELTS-{tag}" for word, ipa, meaning, tag in data["vocab"]])
    
    content = f"""# {data['title']}

> Nguồn: 101 Conversations in English
> Dành cho: Giao tiếp thực tế hàng ngày

---

## 💬 1. Đoạn hội thoại tự nhiên (Real Dialogue)

{turns_str}

---

## 📖 2. Từ vựng Bổ trợ — Flashcard

{vocab_str}

---

## Liên kết Wiki
- [[index]] — Quay lại Mục lục
"""
    fpath.write_text(content, encoding='utf-8')
    print(f"Generated: {fpath.name}")


# 4. Generate Grammar files (g-02 to g-04)
grammar_files_data = {
    "g-02-conditionals": {
        "title": "Ngữ pháp: Câu Điều Kiện (Conditional Sentences)",
        "explanation": (
            "Câu điều kiện dùng để diễn tả một giả thiết về một sự việc, hành động có thể xảy ra hoặc không xảy ra "
            "dưới một điều kiện nhất định. Tiếng Anh có 4 loại câu điều kiện chính."
        ),
        "formula": (
            "| Loại | Mệnh đề phụ (IF) | Mệnh đề chính (MAIN) | Cách dùng |\n"
            "|---|---|---|---|\n"
            "| Type 0 | Present Simple | Present Simple | Sự thật hiển nhiên, chân lý |\n"
            "| Type 1 | Present Simple | Will + V | Có thể xảy ra ở hiện tại/tương lai |\n"
            "| Type 2 | Past Simple | Would + V | Trái với thực tế ở hiện tại |\n"
            "| Type 3 | Past Perfect | Would have + V3 | Trái với thực tế trong quá khứ |"
        ),
        "pitfalls": (
            "1. **Bất quy tắc của động từ to be ở Type 2**: Dùng 'were' cho tất cả các ngôi (I/he/she/it were).\n"
            "2. **Đảo ngữ (Inversion)**: Nhằm nhấn mạnh mệnh đề điều kiện (ví dụ: Should you need help... thay cho If you should need help...).\n"
            "3. **Hỗn hợp (Mixed Conditionals)**: Kết hợp điều kiện quá khứ dẫn đến kết quả hiện tại (If Type 3 + Main Type 2)."
        ),
        "examples": (
            "- If it rains, the ground gets wet. (Nếu trời mưa, đất sẽ bị ướt - Type 0)\n"
            "- If I study hard, I will pass the IELTS exam. (Nếu tôi học chăm chỉ, tôi sẽ đỗ kỳ thi IELTS - Type 1)\n"
            "- If I were you, I would buy that house. (Nếu tôi là bạn, tôi sẽ mua ngôi nhà đó - Type 2)\n"
            "- If we had left early, we wouldn't have missed the train. (Nếu chúng tôi rời đi sớm, chúng tôi đã không nhỡ tàu - Type 3)"
        ),
        "links": "[[v-01-stories-daily-life]]"
    },
    "g-03-passive-voice": {
        "title": "Ngữ pháp: Câu Bị Động (Passive Voice)",
        "explanation": (
            "Câu bị động được dùng khi chúng ta muốn nhấn mạnh vào hành động và đối tượng chịu tác động của hành động đó, "
            "thay vì người hoặc vật thực hiện hành động."
        ),
        "formula": (
            "**Công thức chung**: Subject + Be + V3/V-ed (+ by Agent)\n\n"
            "| Thì | Chủ động (Active) | Bị động (Passive) |\n"
            "|---|---|---|\n"
            "| Present Simple | S + V(s/es) | S + am/is/are + V3 |\n"
            "| Past Simple | S + V-ed/V2 | S + was/were + V3 |\n"
            "| Present Perfect | S + have/has + V3 | S + have/has + been + V3 |\n"
            "| Future Simple | S + will + V | S + will + be + V3 |"
        ),
        "pitfalls": (
            "1. **Nội động từ (Intransitive verbs)**: Các từ như *go, sleep, die* không có tân ngữ nên không thể chia bị động.\n"
            "2. **Bị động với động từ tường thuật**: *It is said that...* hoặc *He is believed to...*\n"
            "3. **Dạng bị động đặc biệt**: Cấu trúc nhờ vả *have/get something done*."
        ),
        "examples": (
            "- The mouse was killed by the lion. (Con chuột đã bị giết bởi con sư tử)\n"
            "- Mauve dye was invented in 1856. (Màu nhuộm hoa cà được phát minh vào năm 1856)\n"
            "- The project has been completed successfully. (Dự án đã được hoàn thành thành công)"
        ),
        "links": "[[v-ielts-cam09]], [[v-02-myths-fairy-tales]]"
    },
    "g-04-reported-speech": {
        "title": "Ngữ pháp: Câu Gián Tiếp (Reported Speech)",
        "explanation": (
            "Câu gián tiếp dùng để thuật lại lời nói của một người khác mà không cần lặp lại chính xác từ ngữ của họ. "
            "Cần chú ý lùi thì, đổi đại từ và từ chỉ thời gian/nơi chốn."
        ),
        "formula": (
            "**Quy tắc lùi thì (Tense shift)**:\n"
            "- Present Simple → Past Simple\n"
            "- Present Continuous → Past Continuous\n"
            "- Past Simple / Present Perfect → Past Perfect\n"
            "- Will → Would / Can → Could\n\n"
            "**Biến đổi thời gian & nơi chốn**:\n"
            "- here → there\n"
            "- now → then / at that moment\n"
            "- today → that day\n"
            "- tomorrow → the next day / the following day"
        ),
        "pitfalls": (
            "1. **Không lùi thì**: Khi tường thuật một sự thật hiển nhiên hoặc lời nói vừa mới xảy ra.\n"
            "2. **Câu hỏi gián tiếp**: Không đảo ngữ trợ động từ ra trước chủ ngữ (dùng *if/whether* cho Yes/No hoặc giữ nguyên *Wh-word*).\n"
            "3. **Câu mệnh lệnh**: Dùng cấu trúc *told someone to do something*."
        ),
        "examples": (
            "- He said, 'I want to study IELTS.' → He said that he wanted to study IELTS. (Anh ấy nói rằng anh ấy muốn học IELTS)\n"
            "- She asked, 'Where is the station?' → She asked where the station was. (Cô ấy hỏi nhà ga ở đâu)\n"
            "- My dad told me, 'Don't enter the laboratory!' → My dad told me not to enter the laboratory. (Bố tôi bảo tôi không được vào phòng thí nghiệm)"
        ),
        "links": "[[v-01-stories-daily-life]], [[s-01-greetings-introductions]]"
    }
}

for fname, data in grammar_files_data.items():
    fpath = grammar_dir / f"{fname}.md"
    content = f"""# {data['title']}

## Giải thích của Giáo viên
{data['explanation']}

## Công thức & Bảng chia
{data['formula']}

## ⚠️ Bẫy Lỗi sai & So sánh
{data['pitfalls']}

## Ví dụ Ứng dụng
{data['examples']}

## Liên kết Từ vựng
{data['links']}

---

## Liên kết Wiki
- [[index]] — Quay lại Mục lục
"""
    fpath.write_text(content, encoding='utf-8')
    print(f"Generated: {fpath.name}")


# 5. Generate reading comprehension file (exam_prep/ielts-reading-comprehension.md)
reading_comp_content = """# 📖 Chiến lược Đọc hiểu & Phân tích Từ vựng IELTS

> Nguồn: Boost your comprehension — Cambridge IELTS 11 (Dinh Thang)
> Trình độ: IELTS Band 6.0+

---

## 1. Phương pháp Đọc Hiểu Sâu (Deep Comprehension)

Đọc hiểu trong IELTS không đơn thuần là kỹ năng tìm từ khóa (scanning). Để đạt band điểm 7.0+, thí sinh cần xây dựng kỹ năng đọc hiểu sâu:

1. **Phân tích cấu trúc câu phức (Syntactic Parsing)**: Tách các mệnh đề phụ, mệnh đề quan hệ để tìm ra cốt lõi của câu (Subject - Verb - Object).
2. **Dự đoán từ vựng dựa vào ngữ cảnh (Contextual Guessing)**: Không dừng lại khi gặp từ mới, hãy dựa vào mối quan hệ nguyên nhân - kết quả, sự tương phản để đoán nghĩa.
3. **Lập bản đồ Paraphrasing**: Nhận diện các cặp từ đồng nghĩa được sử dụng giữa câu hỏi và bài đọc.

---

## 2. Các Mẫu câu Học thuật Cần Chú Ý

### Cấu trúc 1: Tương phản và Nhượng bộ
- *Despite + N/V-ing, S + V...*
- *While/Whereas S1 + V1, S2 + V2...*
- **Ví dụ**: Despite their best efforts to improve speed (Mặc dù có những nỗ lực tốt nhất của họ nhằm cải thiện tốc độ), the project ended up in failure (dự án rốt cuộc vẫn kết thúc trong thất bại).

### Cấu trúc 2: Nguyên nhân - Kết quả
- *S + contribute to / lead to / result in + N/V-ing...*
- *Attribute something to something*
- **Ví dụ**: The rise in temperature was attributed to (Sự gia tăng nhiệt độ được quy cho) the massive greenhouse gas emissions (lượng khí thải nhà kính khổng lồ).

---

## 3. Flashcard Phép Paraphrase Thường Gặp

- decline :: decrease, fall | #IELTS-6
- massive :: huge, enormous | #IELTS-6
- initial :: first, primary | #IELTS-5
- transform :: change, alter | #IELTS-6
- crucial :: vital, essential | #IELTS-6

---

## Liên kết Wiki
- [[v-ielts-cam11]] — Từ vựng Cambridge 11
- [[ielts-writing-guide]] — Hướng dẫn viết IELTS
- [[index]] — Quay lại Mục lục
"""

(exam_prep_dir / "ielts-reading-comprehension.md").write_text(reading_comp_content, encoding='utf-8')
print("Generated: ielts-reading-comprehension.md")


# 6. Generate wiki/index.md with all files fully linked
index_content = """# 📚 English Learning Wiki — Mục lục Trung tâm

> Hệ thống tri thức học tiếng Anh cho người Việt
> Nguồn: 18 tệp PDF (4000 Essential Words, 101 Conversations, IELTS Cambridge 8-18)
> Ngày cập nhật: 2026-06-21

---

## 📖 Từ vựng Nền tảng (4000 Essential English Words)

### Book 1 — Units 1-30
- [[v-01-stories-daily-life]] — Unit 1-5: Câu chuyện & Cuộc sống (100 từ) ✅
- [[v-02-myths-fairy-tales]] — Unit 6-10: Thần thoại & Cổ tích (100 từ) ✅
- [[v-03-challenges-friendship]] — Unit 11-15: Thử thách & Tình bạn (100 từ) ✅
- [[v-04-adventure-discovery]] — Unit 16-20: Phiêu lưu & Khám phá (100 từ) ✅
- [[v-05-lifestyle-characters]] — Unit 21-25: Lối sống & Nhân vật (100 từ) ✅
- [[v-06-lessons-conclusions]] — Unit 26-30: Bài học & Kết luận (100 từ) ✅

### Book 2 — Units 1-30
- [[v-07-skills-talents]] — Unit 1-5: Kỹ năng & Tài năng (100 từ) ✅
- [[v-08-environment-nature]] — Unit 6-10: Môi trường & Tự nhiên (100 từ) ✅
- [[v-09-society-culture]] — Unit 11-15: Xã hội & Văn hóa (100 từ) ✅
- [[v-10-technology-innovation]] — Unit 16-20: Công nghệ & Sáng tạo (100 từ) ✅
- [[v-11-business-economy]] — Unit 21-25: Kinh doanh & Kinh tế (100 từ) ✅
- [[v-12-history-literature]] — Unit 26-30: Lịch sử & Văn học (100 từ) ✅

## 🎯 Từ vựng IELTS (Cambridge Cam 8-18)

- [[v-ielts-cam08]] — Cambridge IELTS 8: Time, ATC, Telepathy ✅
- [[v-ielts-cam09]] — Cambridge IELTS 9: Synthetic Dyes, SETI ✅
- [[v-ielts-cam10]] — Cambridge IELTS 10: Urbanization, Water ✅
- [[v-ielts-cam11]] — Cambridge IELTS 11: Agriculture, Irrigation ✅
- [[v-ielts-cam12]] — Cambridge IELTS 12: Automation, AI ✅
- [[v-ielts-cam13]] — Cambridge IELTS 13: Delta, Coastal Erosion ✅
- [[v-ielts-cam14]] — Cambridge IELTS 14: Spatial Navigation ✅
- [[v-ielts-cam15]] — Cambridge IELTS 15: Subsistence Farming ✅
- [[v-ielts-cam16]] — Cambridge IELTS 16: Rewilding, Conservation ✅
- [[v-ielts-cam17]] — Cambridge IELTS 17: Archaeology, Dynasty ✅
- [[v-ielts-cam18]] — Cambridge IELTS 18: Microplastics, Toxins ✅
- [[v-ielts-mindset45]] — Mindset for IELTS 4.0-5.0: Leisure, Travel ✅

## 📝 Ngữ pháp Tiếng Anh

- [[g-01-tenses-overview]] — Tổng quan các thì & Bẫy lỗi chia động từ ✅
- [[g-02-conditionals]] — Các loại câu điều kiện (Conditional Sentences) ✅
- [[g-03-passive-voice]] — Câu bị động (Passive Voice) & Cấu trúc đặc biệt ✅
- [[g-04-reported-speech]] — Câu gián tiếp (Reported Speech) & Quy tắc lùi thì ✅

## 🗣️ Hội thoại Giao tiếp (101 Conversations)

- [[s-01-greetings-introductions]] — Chào hỏi, Quán cà phê, Hỏi đường ✅
- [[s-02-shopping-restaurant]] — Mua sắm & Nhà hàng (Fitting rooms, Ordering food) ✅
- [[s-03-travel-transportation]] — Giao thông & Du lịch (Directions, Passport check) ✅
- [[s-04-health-hospital]] — Sức khỏe & Bệnh viện (Headache, Blood pressure) ✅
- [[s-05-work-interview]] — Công việc & Phỏng vấn (Job interview questions) ✅

## 📋 Luyện thi IELTS

- [[ielts-writing-guide]] — Hướng dẫn viết IELTS Writing Task 1 & 2 ✅
- [[ielts-academic-phrases]] — Cụm từ học thuật band 7+ ✅
- [[ielts-reading-comprehension]] — Chiến lược đọc hiểu sâu & Phân tích từ vựng ✅

## ❓ Recent Queries

_(Chưa có câu hỏi nào)_

---

## 📊 Thống kê Wiki

| Mục | Số lượng |
|---|---|
| Tổng từ vựng flashcard | ~1800+ |
| Chủ đề từ vựng nền tảng | 12 (v-01 đến v-12) |
| Chủ đề IELTS | 12 (Cam 8-18, Mindset) |
| Bài ngữ pháp | 4 (g-01 đến g-04) |
| Tình huống giao tiếp | 5 (s-01 đến s-05) |
| Tài liệu luyện thi | 3 (Writing, Phrases, Reading) |
"""

(output_base / "index.md").write_text(index_content, encoding='utf-8')
print("Generated index.md")

# 7. Append activity to wiki/log.md
from datetime import datetime
log_line = f"[{datetime.now().strftime('%Y-%m-%d %H:%M')}] update | Tai tao va dinh dang bang cho s-01..s-05, hoan tat English Wiki\n"
with open(output_base / "log.md", "a", encoding="utf-8") as f:
    f.write(log_line)
print("Updated log.md")
