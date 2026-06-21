# -*- coding: utf-8 -*-
"""Batch convert all English PDFs to Markdown using markitdown."""
import os
import sys
from pathlib import Path

# Fix Windows console encoding
if sys.platform == 'win32':
    os.environ.setdefault('PYTHONUTF8', '1')

from markitdown import MarkItDown

pdf_dir = Path(r"T:\Topik\giao trình kyung hee\pdf english")
output_base = Path(r"T:\Topik\giao trình kyung hee\MD_english_learning\wiki")

# Output mapping: PDF filename -> (output_subdir, output_filename)
pdf_map = {
    "VIE-4000 essential english words 1.pdf": ("concepts/vocabulary", "_raw_4000words1.md"),
    "VIE-4000 essential english words 2.pdf": ("concepts/vocabulary", "_raw_4000words2.md"),
    "101 câu thoại.pdf": ("situations", "_raw_101conversations.md"),
    "A&M IELTS - Cam 8 - Boost your vocabulary.pdf": ("concepts/vocabulary", "_raw_ielts_cam08.md"),
    "A&M IELTS - Cam 9 - Boost your vocabulary.pdf": ("concepts/vocabulary", "_raw_ielts_cam09.md"),
    "A&M IELTS - Cam 10- Boost your vocabulary.pdf": ("concepts/vocabulary", "_raw_ielts_cam10.md"),
    "A&M IELTS - Cam 11 - Boost your vocabulary.pdf": ("concepts/vocabulary", "_raw_ielts_cam11.md"),
    "A&M IELTS - Cam 12 - Boost your vocabulary.pdf": ("concepts/vocabulary", "_raw_ielts_cam12.md"),
    "A&M IELTS - Cam 13 - Boost your vocabulary.pdf": ("concepts/vocabulary", "_raw_ielts_cam13.md"),
    "A&M IELTS - Cam 14 - Boost your vocabulary.pdf.pdf": ("concepts/vocabulary", "_raw_ielts_cam14.md"),
    "A&M IELTS - Cam 15 - Boost your vocabulary_version2024.pdf": ("concepts/vocabulary", "_raw_ielts_cam15.md"),
    "A&M IELTS_Special Version_ Boost your vocabulary cambridge IELTS 16 (1).pdf": ("concepts/vocabulary", "_raw_ielts_cam16.md"),
    "A&M IELTS - Cam 17 - Boost your vocabulary.pdf": ("concepts/vocabulary", "_raw_ielts_cam17.md"),
    "A&M IELTS - TEST1_Cam 18 -Boost your vocabulary.pdf": ("concepts/vocabulary", "_raw_ielts_cam18.md"),
    "A&M IELTS - Mindset for IELTS 4.0 -5.0 - Boost your vocabulary.pdf": ("concepts/vocabulary", "_raw_ielts_mindset45.md"),
    "A&M IELTS - Hướng dẫn viết câu IELTS Writing.pdf": ("exam_prep", "_raw_ielts_writing.md"),
    "Highlight-academic-phrases-in-examiners-essays_DinhThang_AM_ver.2.2.2023.pdf": ("exam_prep", "_raw_academic_phrases.md"),
    "Boost your comprehension_Cambridge_IELTS_11_Dinh_Thang_19082019.pdf": ("exam_prep", "_raw_comprehension.md"),
}

md = MarkItDown()
total = len(pdf_map)
done = 0
errors = []

for pdf_name, (subdir, out_name) in pdf_map.items():
    pdf_path = pdf_dir / pdf_name
    out_path = output_base / subdir / out_name
    
    done += 1
    print(f"[{done}/{total}] Converting: {pdf_name}")
    
    if not pdf_path.exists():
        print(f"  ERROR: File not found: {pdf_path}")
        errors.append(pdf_name)
        continue
    
    try:
        result = md.convert(str(pdf_path))
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(result.text_content, encoding='utf-8')
        size_kb = len(result.text_content) / 1024
        print(f"  OK: {size_kb:.1f} KB written to {out_name}")
    except Exception as e:
        print(f"  ERROR: {e}")
        errors.append(pdf_name)

print(f"\n{'='*50}")
print(f"Done: {done - len(errors)}/{total} converted successfully")
if errors:
    print(f"Errors ({len(errors)}):")
    for e in errors:
        print(f"  - {e}")
