# -*- coding: utf-8 -*-
import os

ROOT_DIR = r"t:\Topik\giao trình kyung hee\MD_korea_learning"

def fix_typos():
    count = 0
    for root, dirs, files in os.walk(ROOT_DIR):
        if ".obsidian" in root:
            continue
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                
                if "지 mal다" in content:
                    content = content.replace("지 mal다", "지 말다")
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(content)
                    count += 1
    print(f"Fixed typo in {count} files.")

if __name__ == "__main__":
    fix_typos()
