# -*- coding: utf-8 -*-
import os
import sys
import re
import json
import time
import urllib.request
import urllib.parse
from pathlib import Path

# Force UTF-8 for console output on Windows
try:
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')
except Exception:
    pass

# Setup Workspace Paths
WORKSPACE_ROOT = Path(r"T:\Topik\giao trình kyung hee")
ENGLISH_VOCAB_DIR = WORKSPACE_ROOT / "MD_english_learning" / "wiki" / "concepts" / "vocabulary"
KOREAN_VOCAB_DIR = WORKSPACE_ROOT / "MD_korea_learning" / "wiki" / "concepts" / "vocabulary"
KOREAN_VAULT = WORKSPACE_ROOT / "MD_korea_learning"

CACHE_PATH = WORKSPACE_ROOT / ".translation_cache.json"
translation_cache = {}

def load_translation_cache():
    global translation_cache
    if CACHE_PATH.exists():
        try:
            with open(CACHE_PATH, "r", encoding="utf-8") as f:
                translation_cache = json.load(f)
            print(f"Loaded {len(translation_cache)} translations from cache.")
        except Exception as e:
            print(f"Error loading cache: {e}")
            translation_cache = {}

def save_translation_cache():
    try:
        with open(CACHE_PATH, "w", encoding="utf-8") as f:
            json.dump(translation_cache, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"Error saving cache: {e}")

def translate(text, sl, tl):
    text = text.strip()
    if not text:
        return ""
    cache_key = f"{sl}->{tl}:{text}"
    if cache_key in translation_cache:
        return translation_cache[cache_key]
        
    url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl={sl}&tl={tl}&dt=t&q={urllib.parse.quote(text)}"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=5) as response:
            data = json.loads(response.read().decode('utf-8'))
            translation = "".join([part[0] for part in data[0] if part[0]])
            translation_cache[cache_key] = translation.strip()
            save_translation_cache()
            return translation.strip()
    except Exception as e:
        return ""

def batch_translate(texts, sl, tl, batch_size=50):
    uncached_texts = []
    for t in texts:
        t = t.strip()
        if not t:
            continue
        cache_key = f"{sl}->{tl}:{t}"
        if cache_key not in translation_cache:
            uncached_texts.append(t)
            
    if not uncached_texts:
        return
        
    uncached_texts = list(set(uncached_texts))
    print(f"Batch translating {len(uncached_texts)} new items from {sl} to {tl}...")
    
    for i in range(0, len(uncached_texts), batch_size):
        batch = uncached_texts[i:i+batch_size]
        joined_text = "\n".join(batch)
        url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl={sl}&tl={tl}&dt=t&q={urllib.parse.quote(joined_text)}"
        
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=10) as response:
                data = json.loads(response.read().decode('utf-8'))
                translated_parts = [part[0] for part in data[0] if part[0]]
                translated_joined = "".join(translated_parts)
                
                translated_lines = [line.strip() for line in translated_joined.split("\n")]
                
                if len(translated_lines) == len(batch):
                    for src, tgt in zip(batch, translated_lines):
                        cache_key = f"{sl}->{tl}:{src}"
                        translation_cache[cache_key] = tgt
                else:
                    print(f"  Line count mismatch in batch ({len(translated_lines)} vs {len(batch)}). Falling back to individual translation.")
                    for src in batch:
                        translate(src, sl, tl)
                        
            save_translation_cache()
            time.sleep(0.5)
        except Exception as e:
            print(f"Batch translation failed for range {i}-{i+batch_size}: {e}")
            for src in batch:
                translate(src, sl, tl)

def get_dict_info(word):
    word_encoded = urllib.parse.quote(word)
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word_encoded}"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=5) as response:
            data = json.loads(response.read().decode('utf-8'))
            return data[0]
    except Exception:
        return None

def get_datamuse(word, rel_type):
    word_encoded = urllib.parse.quote(word)
    url = f"https://api.datamuse.com/words?{rel_type}={word_encoded}&max=5"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=5) as response:
            return json.loads(response.read().decode('utf-8'))
    except Exception:
        return []

def load_raw_definitions(raw_filepath):
    defs = {}
    if not raw_filepath.exists():
        return defs
    try:
        with open(raw_filepath, "r", encoding="utf-8") as f:
            for line in f:
                if "=" in line:
                    parts = line.split("=", 1)
                    word = parts[0].strip().lower()
                    definition = parts[1].strip()
                    defs[word] = definition
    except Exception:
        pass
    return defs

def parse_card_line(line):
    if "::" not in line:
        return None
    match = re.match(r"^([ \t]*[-\*\+][ \t]*)", line)
    if not match:
        return None
    prefix = match.group(1)
    clean_line = line[len(prefix):].strip()
    
    parts = clean_line.split("::")
    left = parts[0].strip()
    right = parts[1].strip()
    
    word = left
    pronunciation = ""
    pron_type = "asterisk"
    
    match_ast = re.match(r"(.+?)\s*\(\*\*(.+?)\*\*\)", left)
    if match_ast:
        word = match_ast.group(1).strip()
        pronunciation = match_ast.group(2).strip()
        pron_type = "asterisk"
    else:
        match_simple = re.match(r"(.+?)\s*\((.+?)\)", left)
        if match_simple:
            word = match_simple.group(1).strip()
            pronunciation = match_simple.group(2).strip()
            pron_type = "simple"
        else:
            match_slash = re.match(r"(.+?)\s*/([^/]+)/", left)
            if match_slash:
                word = match_slash.group(1).strip()
                pronunciation = match_slash.group(2).strip()
                pron_type = "slash"
                
    word = re.sub(r"^[-\*\s\+]+", "", word).strip()
    right_no_comments = re.sub(r"<!--[\s\S]*?-->", "", right).strip()
    
    match_tag = re.search(r"\|\s*(#[A-Za-z0-9_-]+)", right_no_comments)
    tag = match_tag.group(1) if match_tag else None
    
    meaning = right_no_comments
    if tag:
        meaning = meaning.replace(match_tag.group(0), "").strip()
    meaning = meaning.replace("**", "").strip()
    
    comments = re.findall(r"<!--\s*([\s\S]*?)\s*-->", right)
    sr_comment = None
    cognitive_comment = None
    
    for c in comments:
        c = c.strip()
        if c.startswith("sr:"):
            sr_comment = c
        elif c.startswith("cognitive:"):
            cognitive_comment = c
            
    return {
        "prefix": prefix,
        "word": word,
        "pronunciation": pronunciation,
        "pron_type": pron_type,
        "meaning": meaning,
        "tag": tag,
        "sr_comment": sr_comment,
        "cognitive_comment": cognitive_comment
    }

def serialize_card_line(card, cognitive_data=None):
    prefix = card["prefix"]
    word = card["word"]
    pronunciation = card["pronunciation"]
    pron_type = card["pron_type"]
    meaning = card["meaning"]
    tag = card["tag"]
    sr_comment = card["sr_comment"]
    
    left = word
    if pronunciation:
        if pron_type == "slash":
            left += f" /{pronunciation}/"
        elif pron_type == "simple":
            left += f" ({pronunciation})"
        else:
            left += f" (**{pronunciation}**)"
            
    right = meaning
    if tag:
        right += f" | {tag}"
    if sr_comment:
        right += f" <!-- {sr_comment} -->"
        
    cog = cognitive_data if cognitive_data is not None else card["cognitive_comment"]
    if cog:
        if isinstance(cog, dict):
            cog_str = json.dumps(cog, ensure_ascii=False)
            right += f" <!-- cognitive: {cog_str} -->"
        else:
            right += f" <!-- {cog} -->"
            
    return f"{prefix}{left} :: {right}"

def build_english_sentence_index():
    print("Building English sentence index from raw files...")
    sentence_index = {}
    if not ENGLISH_VOCAB_DIR.exists():
        return sentence_index
    for filename in os.listdir(ENGLISH_VOCAB_DIR):
        if filename.startswith("_raw_") and filename.endswith(".md"):
            filepath = ENGLISH_VOCAB_DIR / filename
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()
                
                lines = content.splitlines()
                passage_lines = []
                for line in lines:
                    line = line.strip()
                    if not line or "=" in line or line.startswith("#") or line.startswith("BOOST YOUR") or line.startswith("Tài liệu") or line.startswith("Biên tập"):
                        continue
                    if line.isdigit():
                        continue
                    passage_lines.append(line)
                    
                passage_text = " ".join(passage_lines)
                raw_sentences = re.split(r'(?<=[.!?])\s+', passage_text)
                
                for s in raw_sentences:
                    s = s.strip()
                    if not s:
                        continue
                    s = re.sub(r'\s+', ' ', s)
                    words = s.split()
                    if len(words) < 5 or len(words) > 40:
                        continue
                    
                    for w in words:
                        clean_w = re.sub(r'^[^\w]+|[^\w]+$', '', w).lower()
                        if clean_w:
                            if clean_w not in sentence_index:
                                sentence_index[clean_w] = s
                            else:
                                current_len = len(sentence_index[clean_w].split())
                                if abs(len(words) - 15) < abs(current_len - 15):
                                    sentence_index[clean_w] = s
            except Exception as e:
                print(f"Error indexing {filename}: {e}")
    return sentence_index

def build_korean_sentence_index():
    print("Building Korean sentence index from situations, grammar guides, and vocabulary topics...")
    sentence_index = {}
    if not KOREAN_VAULT.exists():
        return sentence_index
        
    situations_dir = KOREAN_VAULT / "wiki" / "situations"
    if situations_dir.exists():
        for filename in os.listdir(situations_dir):
            if filename.endswith(".md"):
                filepath = situations_dir / filename
                try:
                    with open(filepath, "r", encoding="utf-8") as f:
                        for line in f:
                            if "|" in line and "**" in line:
                                parts = [p.strip() for p in line.split("|")]
                                if len(parts) >= 5:
                                    kr = parts[2].replace("**", "").replace("*", "").strip()
                                    vi = parts[4].replace("**", "").replace("*", "").strip()
                                    if kr and vi and not kr.startswith("Nhân vật") and not kr.startswith("Korean"):
                                        sentence_index[kr] = vi
                except Exception as e:
                    print(f"Error parsing situation {filename}: {e}")
                    
    concepts_dir = KOREAN_VAULT / "wiki" / "concepts"
    if concepts_dir.exists():
        for root, dirs, files in os.walk(concepts_dir):
            for file in files:
                if file.endswith(".md") and not file.startswith("_"):
                    filepath = Path(root) / file
                    try:
                        with open(filepath, "r", encoding="utf-8") as f:
                            for line in f:
                                if "::" in line:
                                    continue
                                match = re.match(r"^[ \t]*[-\*\+][ \t]*([^(\n]+?)\s*\(([^)\n]+)\)", line)
                                if match:
                                    kr = match.group(1).strip()
                                    vi = match.group(2).strip()
                                    kr = kr.replace("**", "").replace("*", "").strip()
                                    if any('\uac00' <= char <= '\ud7a3' for char in kr):
                                        sentence_index[kr] = vi
                    except Exception as e:
                        pass
    return sentence_index

def enrich_english_word(word, sentence_index):
    word_lower = word.lower()
    ex = ""
    vi = ""
    
    if word_lower in sentence_index:
        ex = sentence_index[word_lower]
        vi = translate(ex, "en", "vi")
        
    dict_info = get_dict_info(word)
    pos = ""
    syns = []
    ants = []
    
    if dict_info:
        meanings = dict_info.get("meanings", [])
        if meanings:
            pos_en = meanings[0].get("partOfSpeech", "")
            pos_map = {
                "noun": "danh từ", "verb": "động từ", "adjective": "tính từ",
                "adverb": "trạng từ", "conjunction": "liên từ", "preposition": "giới từ",
                "pronoun": "đại từ", "interjection": "thán từ"
            }
            pos = pos_map.get(pos_en.lower(), pos_en)
            
            if not ex:
                for m in meanings:
                    for d in m.get("definitions", []):
                        if d.get("example"):
                            ex = d["example"]
                            vi = translate(ex, "en", "vi")
                            break
                    if ex:
                        break
        
        for m in meanings:
            for s in m.get("synonyms", []): syns.append(s)
            for a in m.get("antonyms", []): ants.append(a)
            
    if len(syns) < 3:
        for item in get_datamuse(word, "rel_syn"): syns.append(item["word"])
    if len(ants) < 3:
        for item in get_datamuse(word, "rel_ant"): ants.append(item["word"])
        
    rel_words = [item["word"] for item in get_datamuse(word, "rel_trg")]
    
    syns = list(set(syns))[:3]
    ants = list(set(ants))[:3]
    rel_words = list(set(rel_words))[:4]
    
    syn_str = ", ".join(syns)
    ant_str = ", ".join(ants)
    
    rel_formatted = []
    for rw in rel_words:
        rel_formatted.append(rw)
        
    if not ex:
        ex = f"We can use the word '{word}' in our daily communications."
        vi = translate(ex, "en", "vi")
        
    return {
        "ex": ex,
        "vi": vi,
        "pos": pos,
        "syn": syn_str,
        "ant": ant_str,
        "rel": ", ".join(rel_formatted)
    }

def build_enriched_cognitive_data(word, details, is_english):
    if is_english:
        return {} # Enriched inside file-by-file logic below
    else: # Korean
        clean_word = details["clean_word"]
        ex = details["ex"]
        vi = details.get("vi", "")
        
        if not ex and "english_fallback_example" in details:
            english_ex = details["english_fallback_example"]
            ex = translate(english_ex, "en", "ko")
            vi = translate(english_ex, "en", "vi")
        elif ex and not vi:
            vi = translate(ex, "ko", "vi")
            
        pos = details["pos"]
        if not pos:
            pos = "động từ/tính từ" if clean_word.endswith("다") else "danh từ"
            
        syn_kr_list = []
        ant_kr_list = []
        rel_kr_list = []
        
        for s in details.get("syn_en", []):
            s_ko = translate(s, "en", "ko")
            s_vi = translate(s, "en", "vi")
            if s_ko: syn_kr_list.append(f"{s_ko} ({s_vi})")
                
        for a in details.get("ant_en", []):
            a_ko = translate(a, "en", "ko")
            a_vi = translate(a, "en", "vi")
            if a_ko: ant_kr_list.append(f"{a_ko} ({a_vi})")
                
        for r in details.get("rel_en", []):
            r_ko = translate(r, "en", "ko")
            r_vi = translate(r, "en", "vi")
            if r_ko: rel_kr_list.append(f"{r_ko} ({r_vi})")
                
        return {
            "ex": ex,
            "vi": vi,
            "pos": pos,
            "syn": ", ".join(syn_kr_list),
            "ant": ", ".join(ant_kr_list),
            "rel": ", ".join(rel_kr_list)
        }

def main():
    load_translation_cache()
    
    english_sentences = build_english_sentence_index()
    korean_sentences = build_korean_sentence_index()
    
    import argparse
    parser = argparse.ArgumentParser(description="Hybrid auto enrich vocabulary cards.")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing cognitive data.")
    parser.add_argument("--lang", choices=["all", "english", "korean"], default="all", help="Target language.")
    parser.add_argument("--limit-files", type=int, default=0, help="Limit files processed.")
    args = parser.parse_args()
    
    # Process English
    if args.lang in ["all", "english"] and ENGLISH_VOCAB_DIR.exists():
        print("\n=== STARTING ENGLISH ENRICHMENT ===")
        files = [f for f in ENGLISH_VOCAB_DIR.iterdir() if f.name.endswith(".md") and not f.name.startswith("_")]
        files.sort(key=lambda x: x.name)
        if args.limit_files > 0:
            files = files[:args.limit_files]
            
        for filepath in files:
            is_ielts = "ielts" in filepath.name or "mindset" in filepath.name
            print(f"\nProcessing English file: {filepath.name} (IELTS Mode: {is_ielts})")
            
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    lines = f.readlines()
            except Exception as e:
                print(f"Error reading {filepath.name}: {e}")
                continue
                
            cards = []
            for line in lines:
                card = parse_card_line(line)
                if card: cards.append(card)
                    
            if not cards: continue
                
            cards_to_enrich = []
            for card in cards:
                if card["cognitive_comment"] and not args.overwrite:
                    continue
                cards_to_enrich.append(card)
                
            if not cards_to_enrich:
                print(f"  All cards in {filepath.name} already enriched.")
                continue
                
            print(f"  Enriching {len(cards_to_enrich)} cards...")
            
            # If IELTS mode, use fast offline definition parsing + batch translation of sentences
            if is_ielts:
                raw_filename = filepath.name.replace("v-", "_raw_")
                raw_filepath = ENGLISH_VOCAB_DIR / raw_filename
                raw_defs = load_raw_definitions(raw_filepath)
                
                passage_sentences = []
                if raw_filepath.exists():
                    try:
                        with open(raw_filepath, "r", encoding="utf-8") as rf:
                            raw_content = rf.read()
                        raw_lines = raw_content.splitlines()
                        for rl in raw_lines:
                            rl = rl.strip()
                            if not rl or "=" in rl or rl.startswith("#") or rl.startswith("BOOST YOUR") or rl.startswith("Tài liệu") or rl.startswith("Biên tập"):
                                continue
                            if rl.isdigit(): continue
                            passage_sentences.append(rl)
                    except Exception:
                        pass
                passage_text = " ".join(passage_sentences)
                raw_sentences_list = re.split(r'(?<=[.!?])\s+', passage_text)
                
                enriched_data = {}
                sentences_to_translate = []
                
                local_vocab = {c["word"].lower(): c["meaning"] for c in cards}
                local_words = list(local_vocab.keys())
                
                for card in cards_to_enrich:
                    word = card["word"]
                    word_lower = word.lower()
                    
                    ex = ""
                    for s in raw_sentences_list:
                        s = s.strip()
                        if not s: continue
                        if re.search(rf"\b{re.escape(word_lower)}\b", s.lower()):
                            ex = s
                            break
                    if not ex:
                        if word_lower in english_sentences:
                            ex = english_sentences[word_lower]
                    if not ex:
                        ex = f"We can use the word '{word}' in our daily communications."
                        
                    sentences_to_translate.append(ex)
                    
                    pos = "danh từ"
                    syns = []
                    ants = []
                    
                    raw_def = raw_defs.get(word_lower, "")
                    if raw_def:
                        if raw_def.startswith("to "): pos = "động từ"
                        elif raw_def.endswith("ly"): pos = "trạng từ"
                        elif any(raw_def.endswith(suffix) for suffix in ["ful", "ive", "ous", "al", "able", "ible"]):
                            pos = "tính từ"
                            
                        parts = [p.strip() for p in raw_def.split(",")]
                        if len(parts) > 1:
                            syns = parts[1:4]
                            
                    rel_formatted = []
                    other_words = [w for w in local_words if w != word_lower]
                    import random
                    random.seed(hash(word_lower))
                    sampled = random.sample(other_words, min(3, len(other_words)))
                    for sw in sampled:
                        meaning_vi = local_vocab[sw]
                        meaning_vi = re.sub(r'\|.*', '', meaning_vi).strip()
                        rel_formatted.append(f"{sw} ({meaning_vi})")
                        
                    enriched_data[word] = {
                        "ex": ex,
                        "pos": pos,
                        "syn": ", ".join(syns),
                        "ant": ", ".join(ants),
                        "rel": ", ".join(rel_formatted)
                    }
                    
                batch_translate(sentences_to_translate, "en", "vi", batch_size=80)
                
                word_cognitive = {}
                for card in cards_to_enrich:
                    word = card["word"]
                    details = enriched_data[word]
                    ex = details["ex"]
                    vi = translate(ex, "en", "vi")
                    word_cognitive[word] = {
                        "ex": ex,
                        "vi": vi,
                        "pos": details["pos"],
                        "syn": details["syn"],
                        "ant": details["ant"],
                        "rel": details["rel"]
                    }
                    
            else: # Non-IELTS rich API mode
                enriched_data = {}
                to_translate = []
                for card in cards_to_enrich:
                    word = card["word"]
                    details = enrich_english_word(word, english_sentences)
                    enriched_data[word] = details
                    to_translate.append(details["ex"])
                    for rw in details["rel"].split(", "):
                        if rw.strip() and "(" not in rw:
                            to_translate.append(rw.strip())
                            
                batch_translate(to_translate, "en", "vi", batch_size=80)
                
                word_cognitive = {}
                for card in cards_to_enrich:
                    word = card["word"]
                    details = enriched_data[word]
                    ex = details["ex"]
                    vi = translate(ex, "en", "vi")
                    
                    rel_words = details["rel"].split(", ")
                    rel_formatted = []
                    for rw in rel_words:
                        rw = rw.strip()
                        if not rw: continue
                        if "(" in rw: rel_formatted.append(rw)
                        else:
                            rw_vi = translate(rw, "en", "vi")
                            if rw_vi: rel_formatted.append(f"{rw} ({rw_vi})")
                            else: rel_formatted.append(rw)
                                
                    word_cognitive[word] = {
                        "ex": ex,
                        "vi": vi,
                        "pos": details["pos"],
                        "syn": details["syn"],
                        "ant": details["ant"],
                        "rel": ", ".join(rel_formatted)
                    }
                    
            new_lines = []
            updated = 0
            for line in lines:
                card = parse_card_line(line)
                if card and card["word"] in word_cognitive:
                    cog_data = word_cognitive[card["word"]]
                    new_line = serialize_card_line(card, cog_data) + "\n"
                    new_lines.append(new_line)
                    updated += 1
                else:
                    new_lines.append(line)
                    
            if updated > 0:
                temp_path = filepath.with_suffix(".tmp")
                with open(temp_path, "w", encoding="utf-8") as f:
                    f.writelines(new_lines)
                if filepath.exists(): os.remove(filepath)
                os.rename(temp_path, filepath)
                print(f"  Saved {updated} enriched cards in {filepath.name}.")
                
    # Process Korean
    if args.lang in ["all", "korean"] and KOREAN_VOCAB_DIR.exists():
        print("\n=== STARTING KOREAN ENRICHMENT ===")
        files = [f for f in KOREAN_VOCAB_DIR.iterdir() if f.name.endswith(".md") and not f.name.startswith("_") and any(f"v-{num}-" in f.name for num in ["15", "16", "17", "18", "19", "20", "21", "22"])]
        files.sort(key=lambda x: x.name)
        if args.limit_files > 0:
            files = files[:args.limit_files]
            
        for filepath in files:
            print(f"\nProcessing Korean file: {filepath.name}")
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    lines = f.readlines()
            except Exception as e:
                print(f"Error reading {filepath.name}: {e}")
                continue
                
            cards = []
            for line in lines:
                card = parse_card_line(line)
                if card: cards.append(card)
                    
            if not cards: continue
                
            cards_to_enrich = []
            for card in cards:
                if card["cognitive_comment"] and not args.overwrite:
                    continue
                cards_to_enrich.append(card)
                
            if not cards_to_enrich:
                print(f"  All cards in {filepath.name} already enriched.")
                continue
                
            print(f"  Enriching {len(cards_to_enrich)} cards...")
            
            to_translate_ko_en = []
            to_translate_en_vi = []
            to_translate_ko_vi = []
            enriched_data = {}
            
            for card in cards_to_enrich:
                word = card["word"]
                clean_word = word.strip()
                ex = ""
                vi = ""
                for sent_kr, sent_vi in korean_sentences.items():
                    if clean_word in sent_kr:
                        ex = sent_kr
                        vi = sent_vi
                        break
                to_translate_ko_en.append(clean_word)
                enriched_data[word] = {
                    "clean_word": clean_word,
                    "ex": ex,
                    "vi": vi
                }
                
            batch_translate(to_translate_ko_en, "ko", "en", batch_size=80)
            
            to_translate_en_vi_extra = []
            to_translate_ko_vi_extra = []
            
            for card in cards_to_enrich:
                word = card["word"]
                details = enriched_data[word]
                clean_word = details["clean_word"]
                word_en = translate(clean_word, "ko", "en")
                
                pos = ""
                syn_en, ant_en, rel_en = [], [], []
                dict_info = None
                
                if word_en:
                    dict_info = get_dict_info(word_en)
                    if dict_info:
                        meanings = dict_info.get("meanings", [])
                        if meanings:
                            pos_en = meanings[0].get("partOfSpeech", "")
                            pos_map = {
                                "noun": "danh từ", "verb": "động từ", "adjective": "tính từ",
                                "adverb": "trạng từ", "conjunction": "liên từ", "preposition": "giới từ",
                                "pronoun": "đại từ", "interjection": "thán từ"
                            }
                            pos = pos_map.get(pos_en.lower(), pos_en)
                    
                    syn_en = [item["word"] for item in get_datamuse(word_en, "rel_syn")][:2]
                    ant_en = [item["word"] for item in get_datamuse(word_en, "rel_ant")][:2]
                    rel_en = [item["word"] for item in get_datamuse(word_en, "rel_trg")][:3]
                    
                ex = details["ex"]
                if not ex and word_en:
                    dict_example = ""
                    if dict_info:
                        for m in dict_info.get("meanings", []):
                            for d in m.get("definitions", []):
                                if d.get("example"):
                                    dict_example = d["example"]
                                    break
                            if dict_example: break
                    if not dict_example:
                        dict_example = f"Let's focus on the topic of {word_en}."
                    
                    to_translate_en_vi_extra.append(dict_example)
                    to_translate_ko_vi_extra.append(dict_example)
                    details["english_fallback_example"] = dict_example
                    
                for item in syn_en + ant_en + rel_en:
                    to_translate_en_vi_extra.append(item)
                    to_translate_ko_vi_extra.append(item)
                    
                details["pos"] = pos
                details["syn_en"] = syn_en
                details["ant_en"] = ant_en
                details["rel_en"] = rel_en
                
            if to_translate_en_vi_extra:
                batch_translate(to_translate_en_vi_extra, "en", "vi", batch_size=80)
            if to_translate_ko_vi_extra:
                batch_translate(to_translate_ko_vi_extra, "en", "ko", batch_size=80)
                
            ko_sents_to_vi = []
            for word, details in enriched_data.items():
                if details["ex"] and not details["vi"]:
                    ko_sents_to_vi.append(details["ex"])
            if ko_sents_to_vi:
                batch_translate(ko_sents_to_vi, "ko", "vi", batch_size=80)
                
            word_cognitive = {}
            for card in cards_to_enrich:
                word = card["word"]
                details = enriched_data[word]
                cog_data = build_enriched_cognitive_data(word, details, is_english=False)
                word_cognitive[word] = cog_data
                
            new_lines = []
            updated = 0
            for line in lines:
                card = parse_card_line(line)
                if card and card["word"] in word_cognitive:
                    cog_data = word_cognitive[card["word"]]
                    new_line = serialize_card_line(card, cog_data) + "\n"
                    new_lines.append(new_line)
                    updated += 1
                else:
                    new_lines.append(line)
                    
            if updated > 0:
                temp_path = filepath.with_suffix(".tmp")
                with open(temp_path, "w", encoding="utf-8") as f:
                    f.writelines(new_lines)
                if filepath.exists(): os.remove(filepath)
                os.rename(temp_path, filepath)
                print(f"  Saved {updated} enriched cards in {filepath.name}.")
                
    print("\nVocabulary enrichment completed successfully!")
    save_translation_cache()

if __name__ == "__main__":
    main()
