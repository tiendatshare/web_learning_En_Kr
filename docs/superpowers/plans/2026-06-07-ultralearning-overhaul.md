# Ultralearning Overhaul Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Rebuild all 24 vocabulary files (8 tầng) + 50 grammar files (6 tầng) + 1 Ultralearning Roadmap using 11 proven scientific learning methods, targeting TOPIK 5 in 6 months.

**Architecture:** A massive Python generator script (`generate_ultralearning_v5.py`) reads the existing vocabulary database (`generate_ultimate_vocabulary.py` core_topics dict), enriches each entry with 4-tier neural networks, antonyms/synonyms at every tier, mnemonics, Active Recall quizzes, Feynman explanations, TOPIK patterns, and grammar links — then writes 24 markdown files. A separate script (`generate_grammar_v2.py`) rebuilds all 50 grammar files with 6-tier pedagogical structure. Finally, `ultralearning_roadmap.md` is hand-crafted.

**Tech Stack:** Python 3.12, Markdown/Obsidian, existing `generate_ultimate_vocabulary.py` as data source

**Source Spec:** `docs/superpowers/specs/2026-06-07-ultralearning-overhaul-design.md`

---

## File Structure

### Files to Create:
- `scratch/generate_vocab_v5.py` — Master vocabulary generator (8-tier output)
- `scratch/generate_grammar_v2.py` — Master grammar generator (6-tier output)
- `scratch/verify_overhaul.py` — Verification script
- `MD_korea_learning/ultralearning_roadmap.md` — 6-month TOPIK 5 roadmap

### Files to Modify:
- `MD_korea_learning/wiki/concepts/vocabulary/v-*.md` (24 files) — Regenerate with 8 tiers
- `MD_korea_learning/wiki/concepts/grammar/g-*.md` (50 files) — Regenerate with 6 tiers
- `MD_korea_learning/wiki/index.md` — Update links
- `MD_korea_learning/AGENTS.md` — Update rules

### Data Preservation:
- `scratch/generate_ultimate_vocabulary.py` — Read-only source (core_topics, readings, essay_sentences)

---

### Task 1: Create Master Vocabulary Generator Script (Phase 1 — Data Layer)

**Files:**
- Create: `scratch/generate_vocab_v5.py`

This is the largest task. The script contains a comprehensive database for all 24 topics with enriched data for each word including: 4-tier neural network associations, antonyms, synonyms, irregular conjugations, mnemonics, TOPIK level tags, grammar links, Active Recall questions, Feynman explanations, situational challenges, and TOPIK patterns.

- [ ] **Step 1: Create the script skeleton with the data structure and import system**

The script must:
1. Import the `core_topics` dict from the existing `generate_ultimate_vocabulary.py`
2. Define an enrichment layer (`ENRICHMENT_DB`) that maps each topic to its additional data:
   - `neural_trees`: List of root words, each containing 4 tiers of associations with antonyms/synonyms at each tier
   - `feynman`: A Feynman explanation paragraph for the topic
   - `mnemonics`: Keyword-method memory hacks for difficult words
   - `active_recall`: List of 3+ quiz questions with hidden answers
   - `grammar_links`: Related grammar files
   - `situational_challenge`: Mini role-play scenarios
   - `topik_pattern`: A TOPIK-style mock question
3. Define the markdown template for 8 tiers
4. Iterate over all 24 topics and generate complete `.md` files

```python
#!/usr/bin/env python3
"""
Ultralearning Vocabulary Generator v5
Generates 24 vocabulary files with 8-Tier Cognitive Architecture:
  1. Flashcard Hub (Spaced Repetition + Leitner)
  2. Neural Network 4-Tier Recursive (Semantic Mapping)
  3. Feynman Zone
  4. Active Recall Arena
  5. Mnemonic Lab
  6. Grammar Link Bridge
  7. Situational Challenge
  8. TOPIK Pattern Recognition
"""
import os, sys, json
sys.stdout.reconfigure(encoding='utf-8')

# Paths
VOCAB_DIR = r"t:\Topik\giao trình kyung hee\MD_korea_learning\wiki\concepts\vocabulary"
SCRATCH = r"C:\Users\BLACK NET\.gemini\antigravity-ide\brain\b7cc4267-0e99-4bec-ac2d-6fcb3c408e31\scratch"

# Import existing data
sys.path.insert(0, SCRATCH)
from generate_ultimate_vocabulary import core_topics
```

- [ ] **Step 2: Define the ENRICHMENT_DB for ALL 24 topics**

This is the critical data layer. For EACH of the 24 topics, define:

```python
ENRICHMENT_DB = {
    "v-01-adverbs-fundamentals": {
        "neural_trees": [
            {
                "root": "보통",
                "root_pron": "bo-thông",
                "root_meaning": "thông thường",
                "topik_level": 1,
                "tiers": [
                    {  # Tier 1
                        "words": [
                            ("대개", "dae-gae", "đại khái/thông thường"),
                            ("평소", "phyơng-xo", "bình thường/ngày thường"),
                            ("일반적으로", "il-ban-jơk-ư-ro", "một cách thông thường"),
                        ],
                        "antonyms": [("특별히", "thưk-byơl-hi", "đặc biệt")],
                        "synonyms": [("보통으로", "bo-thông-ư-ro", "một cách bình thường")],
                    },
                    {  # Tier 2
                        "words": [
                            ("평범하다", "phyơng-bơm-ha-da", "bình phàm/tầm thường"),
                            ("흔하다", "hưn-ha-da", "phổ biến/thường thấy"),
                        ],
                        "antonyms": [("특이하다", "thưk-i-ha-da", "đặc biệt/kỳ lạ")],
                        "synonyms": [("일상적이다", "il-xang-jơk-i-da", "mang tính thường nhật")],
                    },
                    # ... Tier 3, Tier 4
                ],
                "conjugation": "Trạng từ — không chia đuôi. Dùng trực tiếp trước động từ/tính từ.",
            },
            # ... more root words
        ],
        "feynman": "Trạng từ giống như gia vị...",
        "mnemonics": [
            ("보통", "bo-thông", "BỎ THÔNG thường", "BỎ thói THÔNG thường = bình thường!"),
            # ...
        ],
        "active_recall": [
            {
                "type": "elaborative",
                "question": "Tại sao 벌써 và 이미 đều dịch là 'đã' nhưng KHÁC nhau?",
                "answer": "벌써 = ngạc nhiên/bất ngờ (đã...rồi sao?!). 이미 = trung lập (đã hoàn tất).",
            },
            # ...
        ],
        "grammar_links": [
            ("항상 + V", "g-07-동사-형용사 + ㅂ니다-습니다 & ㅂ니까-습니까 (Đuôi câu trang trọng)"),
            # ...
        ],
        "situational_challenge": {
            "situation": "Đồng nghiệp hỏi: '주말에 보통 뭐 해요?' (Cuối tuần bạn thường làm gì?)",
            "hint": "보통 집에서 쉬어요. 가끔 친구를 만나요. 그리고 자주 한국어를 공부해요.",
        },
        "topik_pattern": {
            "type": "듣기",
            "question": "남자: 주말에 뭐 해요?\n여자: ________________",
            "options": ["① 보통 집에서 쉬어요.", "② 네, 학생이에요.", "③ 사과를 좋아해요.", "④ 도서관에 있어요."],
            "answer": "①",
            "explanation": "Câu hỏi về thói quen cuối tuần → đáp án phải chứa trạng từ tần suất.",
        },
    },
    # ... 23 more topics
}
```

**CRITICAL**: Each topic MUST have:
- ≥ 5 neural trees (root words) with 4 tiers each
- ≥ 3 active recall questions
- ≥ 5 mnemonics
- ≥ 3 grammar links
- 1 situational challenge
- 1 TOPIK pattern

- [ ] **Step 3: Define the markdown template renderer**

```python
def render_vocabulary_file(topic_key, topic_data, enrichment):
    """Render a complete 8-tier vocabulary markdown file."""
    lines = []
    
    # Header
    lines.append(f"# Từ vựng Chủ đề: {topic_data['title']}")
    lines.append(f"\n{topic_data['desc']}\n")
    lines.append("* Quay lại Mục lục chính: [[index.md]]")
    lines.append("* Xem Cẩm nang Ngữ pháp: [[../../grammar_guide.md]]\n---\n")
    
    # TIER 1: Flashcard Hub
    lines.append("## 🎴 1. Flashcard Hub — Spaced Repetition (Leitner)")
    lines.append("> [!TIP]")
    lines.append("> Plugin **Obsidian Spaced Repetition** + **Anki Export** tương thích.\n")
    for tree in enrichment["neural_trees"]:
        topik_tag = f"#TOPIK-{tree['topik_level']}"
        antonym_str = " / ".join([f"{a[0]} ({a[2]})" for a in tree["tiers"][0].get("antonyms", [])])
        synonym_str = " / ".join([f"{s[0]} ({s[2]})" for s in tree["tiers"][0].get("synonyms", [])])
        card = f"- {tree['root']} ({tree['root_pron']}) :: {tree['root_meaning']}"
        card += f" | {topik_tag}"
        if antonym_str:
            card += f" | ⚔️ ↔ {antonym_str}"
        if synonym_str:
            card += f" | 🔄 ≈ {synonym_str}"
        lines.append(card)
    
    # TIER 2: Neural Network 4-Tier
    lines.append("\n---\n")
    lines.append("## 🧠 2. Mạng Nơ-ron Đệ quy 4 Tầng (Neural Word Association Network)")
    # ... render each tree with 4 tiers, antonyms/synonyms at each tier
    
    # TIER 3: Feynman Zone
    lines.append("\n---\n")
    lines.append("## 💡 3. Feynman Zone — Giải thích Siêu đơn giản")
    lines.append(enrichment["feynman"])
    
    # TIER 4: Active Recall Arena
    # TIER 5: Mnemonic Lab
    # TIER 6: Grammar Link Bridge
    # TIER 7: Situational Challenge
    # TIER 8: TOPIK Pattern Recognition
    
    # PRESERVED: Reading passages from original data
    if "readings" in topic_data:
        # ... preserve original readings
        pass
    
    return "\n".join(lines)
```

- [ ] **Step 4: Write the main execution loop and run**

```python
if __name__ == "__main__":
    os.makedirs(VOCAB_DIR, exist_ok=True)
    for topic_key, topic_data in core_topics.items():
        enrichment = ENRICHMENT_DB.get(topic_key, {})
        if not enrichment:
            print(f"WARNING: No enrichment for {topic_key}")
            continue
        md = render_vocabulary_file(topic_key, topic_data, enrichment)
        filepath = os.path.join(VOCAB_DIR, f"{topic_key}.md")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(md)
        print(f"✅ {topic_key}: Generated")
    print(f"\nTotal: {len(core_topics)} files generated")
```

Run: `python scratch/generate_vocab_v5.py`
Expected: 24 files generated, each with 8 tiers

- [ ] **Step 5: Verify vocabulary output structure**

Run: `python scratch/verify_overhaul.py --vocab`
Expected: All 24 files pass structural validation (8 headings, flashcard count, neural tree count)

- [ ] **Step 6: Commit vocabulary milestone**

```bash
git add MD_korea_learning/wiki/concepts/vocabulary/
git commit -m "feat(vocab): rebuild 24 files with 8-tier Ultralearning architecture"
```

---

### Task 2: Create Master Grammar Generator Script

**Files:**
- Create: `scratch/generate_grammar_v2.py`

- [ ] **Step 1: Create grammar database with 6-tier data for all 50 grammar units**

The script must contain accurate data for each grammar:
1. Feynman explanation (simple Vietnamese)
2. Correct conjugation table with real examples
3. Detailed contrast with similar grammar
4. Vietnamese-specific common mistakes
5. Active Recall quiz (3+ questions)
6. Real-life dialogues USING that specific grammar

```python
#!/usr/bin/env python3
"""
Ultralearning Grammar Generator v2
Generates 50 grammar files with 6-Tier Pedagogical Architecture:
  1. Feynman Explanation
  2. Visual Formula + Conjugation Table
  3. Contrast Lab
  4. Common Mistake ER (Vietnamese-specific)
  5. Active Recall Quiz
  6. Real-Life Dialogues
"""
import os, sys
sys.stdout.reconfigure(encoding='utf-8')

GRAMMAR_DIR = r"t:\Topik\giao trình kyung hee\MD_korea_learning\wiki\concepts\grammar"

GRAMMAR_DB = {
    1: {
        "filename": "g-01-명사 + 입니다-입니까 (Là - Có phải là không)",
        "structure": "명사 + 입니다/입니까",
        "meaning": "Là / Có phải là không",
        "tags": ["grammar", "copula", "formal"],
        "related_grammar": [],
        "vocab_associations": ["v-16-occupations-workplace", "v-22-countries-nationalities"],
        "feynman": """
> **입니다/입니까** giống hệt chữ "LÀ" trong tiếng Việt, nhưng ở dạng LỊCH SỰ NHẤT.
> 
> Tưởng tượng bạn đang phỏng vấn xin việc:
> - "Tôi **LÀ** sinh viên." → 저는 학생**입니다**. (khẳng định)
> - "Bạn **LÀ** sinh viên **PHẢI KHÔNG**?" → 학생**입니까**? (hỏi)
>
> 🎯 **Nhớ**: 입니다 = là (nói). 입니까 = là không? (hỏi).
> ⚠️ CHỈ dùng với DANH TỪ. Không dùng với động từ/tính từ!
""",
        "conjugation_table": [
            # (điều_kiện, dùng, ví_dụ_từ, ví_dụ_kết_hợp, phiên_âm, lưu_ý)
            ("Danh từ (bất kỳ)", "입니다", "학생 (sinh viên)", "학생입니다", "hak-saeng-im-ni-da", "Khẳng định"),
            ("Danh từ (bất kỳ)", "입니까", "선생님 (giáo viên)", "선생님입니까?", "xơn-saeng-nim-im-ni-kka", "Nghi vấn"),
        ],
        "contrast": {
            "compare_with": "이에요/예요",
            "table": [
                ("Mức độ lịch sự", "Trang trọng nhất (격식체)", "Lịch sự thân mật (비격식체)"),
                ("Dùng khi", "Phỏng vấn, thuyết trình, quân đội, tin tức", "Nói chuyện với bạn bè lớn tuổi, đồng nghiệp"),
                ("Ví dụ", "학생입니다", "학생이에요"),
                ("Phủ định", "학생이 아닙니다", "학생이 아니에요"),
            ],
        },
        "common_mistakes": [
            {
                "wrong": "좋다입니다",
                "right": "좋습니다 (dùng -ㅂ니다 cho tính từ)",
                "why": "입니다 CHỈ gắn sau DANH TỪ. Tính từ 좋다 phải dùng -ㅂ니다.",
            },
            {
                "wrong": "가다입니다",
                "right": "갑니다 (dùng -ㅂ니다 cho động từ)",
                "why": "입니다 CHỈ gắn sau DANH TỪ. Động từ 가다 phải dùng -ㅂ니다.",
            },
        ],
        "active_recall": [
            {
                "question": "Điền vào chỗ trống: '저는 회사원___.' (Tôi là nhân viên công ty.)",
                "answer": "입니다 — Vì 회사원 là danh từ, dùng 입니다 ở thể trang trọng.",
            },
            {
                "question": "Tại sao KHÔNG nói '예쁘다입니다'?",
                "answer": "Vì 예쁘다 là TÍNH TỪ, không phải danh từ. Tính từ dùng 예쁩니다 (-ㅂ니다).",
            },
            {
                "question": "'학생입니까?' và '학생이에요?' khác nhau thế nào?",
                "answer": "입니까 = trang trọng (formal). 이에요 = thân mật lịch sự (casual polite).",
            },
        ],
        "dialogues": [
            {
                "situation": "Phỏng vấn xin việc",
                "lines": [
                    ("A (면접관)", "이름이 뭡니까?", "i-rưm-i mwơm-ni-kka?", "이름(tên)+이(tiểu từ) 뭡니까(là gì)?", "Tên bạn là gì?"),
                    ("B (지원자)", "저는 응우옌 흐엉입니다.", "jơ-nưn ưng-u-yên hư-ơng-im-ni-da.", "저(tôi)+는(thì) 응우옌 흐엉(Nguyễn Hương)+입니다(là).", "Tôi là Nguyễn Hương."),
                    ("A", "직업이 뭡니까?", "jik-ơp-i mwơm-ni-kka?", "직업(nghề nghiệp)+이(tiểu từ) 뭡니까(là gì)?", "Nghề nghiệp là gì?"),
                    ("B", "저는 엔지니어입니다.", "jơ-nưn en-ji-ni-ơ-im-ni-da.", "저(tôi)+는(thì) 엔지니어(kỹ sư)+입니다(là).", "Tôi là kỹ sư."),
                ],
            },
        ],
    },
    # ... 49 more grammar units with complete data
}
```

- [ ] **Step 2: Define the markdown template renderer for grammar**

```python
def render_grammar_file(unit_num, data):
    """Render a complete 6-tier grammar markdown file."""
    lines = []
    
    # YAML frontmatter
    lines.append("---")
    lines.append(f"type: grammar")
    lines.append(f"unit: {unit_num}")
    lines.append(f"structure: \"{data['structure']}\"")
    lines.append(f"meaning: \"{data['meaning']}\"")
    lines.append(f"tags: {data['tags']}")
    # ...
    lines.append("---\n")
    
    # Title
    lines.append(f"# Ngữ pháp Unit {unit_num}: {data['structure']} ({data['meaning']})\n")
    lines.append("* Quay lại Mục lục chính: [[wiki/index.md]]")
    lines.append("* Quay lại Danh mục Ngữ pháp: [[grammar_guide.md]]\n---\n")
    
    # TIER 1: Feynman
    lines.append("## 💡 1. Feynman — Hiểu trong 30 giây")
    lines.append(data["feynman"])
    
    # TIER 2: Visual Formula
    lines.append("\n---\n")
    lines.append("## 📐 2. Công thức & Bảng chia đuôi\n")
    # ... render conjugation table
    
    # TIER 3: Contrast Lab
    # TIER 4: Common Mistake ER
    # TIER 5: Active Recall Quiz
    # TIER 6: Real-Life Dialogues
    
    return "\n".join(lines)
```

- [ ] **Step 3: Execute grammar generation and verify**

Run: `python scratch/generate_grammar_v2.py`
Expected: 50 files generated, each with 6 tiers

- [ ] **Step 4: Commit grammar milestone**

```bash
git add MD_korea_learning/wiki/concepts/grammar/
git commit -m "feat(grammar): rebuild 50 files with 6-tier Ultralearning architecture"
```

---

### Task 3: Create Ultralearning Roadmap

**Files:**
- Create: `MD_korea_learning/ultralearning_roadmap.md`

- [ ] **Step 1: Write the 6-month TOPIK 5 roadmap**

The file must contain:
1. Scott Young's 9 Ultralearning Principles adapted for Korean
2. Month-by-month progression with specific milestones
3. Daily study schedule template
4. Weekly review checklist
5. TOPIK score targets per month
6. Links to all vocabulary and grammar files in recommended study order

- [ ] **Step 2: Commit roadmap**

```bash
git add MD_korea_learning/ultralearning_roadmap.md
git commit -m "feat: add Ultralearning 6-month TOPIK 5 roadmap"
```

---

### Task 4: Update Index and Verify Links

**Files:**
- Modify: `MD_korea_learning/wiki/index.md`
- Modify: `MD_korea_learning/AGENTS.md`
- Create: `scratch/verify_overhaul.py`

- [ ] **Step 1: Update index.md with new section for Ultralearning Roadmap**

Add a new prominent section linking to `ultralearning_roadmap.md` and verify all existing vocabulary/grammar links still work.

- [ ] **Step 2: Update AGENTS.md with new file structure rules**

Document the 8-tier vocabulary and 6-tier grammar structure so future AI agents maintain consistency.

- [ ] **Step 3: Create and run verification script**

```python
#!/usr/bin/env python3
"""Verify the Ultralearning overhaul completeness."""
import os, re, glob

VOCAB_DIR = r"t:\Topik\giao trình kyung hee\MD_korea_learning\wiki\concepts\vocabulary"
GRAMMAR_DIR = r"t:\Topik\giao trình kyung hee\MD_korea_learning\wiki\concepts\grammar"

# Check vocabulary files have all 8 tiers
VOCAB_TIERS = [
    "## 🎴 1.",  # Flashcard Hub
    "## 🧠 2.",  # Neural Network
    "## 💡 3.",  # Feynman
    "## ❓ 4.",  # Active Recall
    "## 🎯 5.",  # Mnemonic
    "## 🔗 6.",  # Grammar Link
    "## 🎭 7.",  # Situational
    "## 📝 8.",  # TOPIK Pattern
]

GRAMMAR_TIERS = [
    "## 💡 1.",  # Feynman
    "## 📐 2.",  # Visual Formula
    "## ⚖️ 3.",  # Contrast Lab
    "## 🚨 4.",  # Common Mistakes
    "## ❓ 5.",  # Active Recall
    "## 🎭 6.",  # Dialogues
]

errors = 0
for f in sorted(glob.glob(os.path.join(VOCAB_DIR, "v-*.md"))):
    content = open(f, encoding="utf-8").read()
    for tier in VOCAB_TIERS:
        if tier not in content:
            print(f"❌ {os.path.basename(f)}: Missing tier '{tier}'")
            errors += 1

for f in sorted(glob.glob(os.path.join(GRAMMAR_DIR, "g-*.md"))):
    content = open(f, encoding="utf-8").read()
    for tier in GRAMMAR_TIERS:
        if tier not in content:
            print(f"❌ {os.path.basename(f)}: Missing tier '{tier}'")
            errors += 1

if errors == 0:
    print("✅ All files pass structural validation!")
else:
    print(f"\n❌ {errors} issues found")
```

Run: `python scratch/verify_overhaul.py`
Expected: "All files pass structural validation!"

- [ ] **Step 4: Run existing broken link checker**

Run: `python scratch/check_broken_links.py`
Expected: 0 broken links

- [ ] **Step 5: Final commit**

```bash
git add -A
git commit -m "feat: complete Ultralearning overhaul - 24 vocab (8-tier) + 50 grammar (6-tier) + roadmap"
```

---

### Task 5: Update State Files

**Files:**
- Modify: `progress.txt`
- Modify: `init.json`
- Modify: `MEMORY.md`

- [ ] **Step 1: Update all tracking files**

Append to `progress.txt`, add T16 to `init.json`, update `MEMORY.md` hot context.

- [ ] **Step 2: Commit state updates**

```bash
git add progress.txt init.json MEMORY.md
git commit -m "chore: update state files for Ultralearning overhaul T16"
```
