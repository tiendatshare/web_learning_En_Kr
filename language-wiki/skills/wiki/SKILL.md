---
name: wiki
description: >-
  Language Learning Wiki — persistent, compounding knowledge base for language learning (Korean) inside
  an Obsidian vault. Use when the user says "/language-wiki:wiki", "wiki init",
  "wiki ingest", "wiki compile", "wiki study", "wiki discover", or "wiki exam".
argument-hint: init <name> | ingest <path> | compile | study | discover --level <level> [--grammar <grammar>] [--vocab <topic>] | exam --generate
---

# Language Learning Wiki Skill

Persistent, compounding knowledge base for language learning (Korean) inside an Obsidian vault.
Design spec: `docs/superpowers/specs/2026-06-21-language-learning-wiki-design.md`
Implementation plan: `docs/superpowers/plans/2026-06-21-language-learning-wiki-plan.md`

## 🛠️ CLI Command Implementation Guide

### 1. `init <name>`
- Create directory structure under target `<name>` (default: `MD_korea_learning`):
  - `raw/extracts/`
  - `wiki/concepts/grammar/`
  - `wiki/concepts/vocabulary/`
  - `wiki/situations/`
  - `wiki/queries/`
  - `wiki/exams/`
- Run `git init` inside target directory.
- Create `CLAUDE.md` and `.gitignore`.
- Perform initial commit: `git commit -m "init: language learning wiki root"`.

### 2. `ingest <path>`
- Accept image (`.png`, `.jpg`) or PDF.
- Run python OCR extraction to extract text.
- Save text to `raw/extracts/<basename>.md` with frontmatter containing `source-sha`, `extracted-at`, and `extract-status: complete`.

### 3. `compile`
- Read raw extracts from `raw/extracts/`.
- Perform LLM-driven cognitive processing (do not write Python semantic processing regexes):
  - Strip nominal particles from vocabulary tables.
  - Automatically analyze pronunciation rules for a sound-spelling map with Vietnamese phonetic guides.
  - Parse Hán-Tự / Hanja roots tree.
  - Design reflection shadowing micro-dialogues.
  - Bidirectional link vocabulary and grammar concept pages.
- Create official files:
  - `wiki/concepts/grammar/g-*.md`
  - `wiki/concepts/vocabulary/v-*.md`
- Synchronize main index dashboard `wiki/index.md`.
- Commit changes: `git commit -m "compile: generate language concepts"`.

### 4. `study`
- Verify local port is free.
- Run Vite local development server (`npm run dev`) and local Express API server (`node server/index.js`) concurrently using `concurrently`.
- Open browser at `http://localhost:5173`.

### 5. `discover --level <level> [--grammar <grammar>] [--vocab <topic>]`
- Scrape external dictionary/web references via Parallel Web Search or Naver API.
- Download target grammar explanation or vocabulary sheet.
- Store raw fetched data into `raw/extracts/scraped-<name>.md` to make it ready for the `compile` stage.

### 6. `exam --generate`
- Scan existing concepts database.
- Draft a 25-question TOPIK-style midterm or final exam.
- Save to `wiki/exams/exam-topik-<hash>.md` containing multiple choice questions, timer settings, and grammar diagnostic rules linking back to target `g-*.md` files.
