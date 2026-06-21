# Lập Kế Hoạch Triển Khai: Language Learning Wiki & Study App

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Xây dựng plugin language-wiki hỗ trợ học ngoại ngữ (tiếng Hàn) kết hợp Web App ôn tập ngắt quãng (SM-2), đề thi trắc nghiệm chẩn đoán lỗi và chế độ luyện nói (STT).

**Architecture:** Thiết kế Monorepo chạy ở local với API Server (Express.js) giao tiếp trực tiếp với cơ sở dữ liệu Markdown trong Obsidian, phối hợp cùng máy chủ MCP tích hợp để điều phối các tác vụ hệ thống (Lock, Git, OCR).

**Tech Stack:** React (Vite, TailwindCSS/Vanilla CSS), Node.js (Express, ws), Python (Script phụ trợ), Git, Web Speech API (TTS/STT).

---

### Task 1: Khởi tạo Cấu trúc Plugin & Lệnh Command
**Files:**
*   Create: `language-wiki/plugin.json`
*   Create: `language-wiki/commands/wiki.md`
*   Create: `language-wiki/skills/wiki/SKILL.md`

- [ ] **Step 1: Khởi tạo tệp manifest của plugin**
    Tạo tệp `language-wiki/plugin.json`:
    ```json
    {
      "name": "language-wiki",
      "version": "1.0.0",
      "description": "Language learning wiki plugin with spaced repetition, STT and exam modules.",
      "author": { "name": "User" },
      "license": "MIT"
    }
    ```
- [ ] **Step 2: Đăng ký lệnh điều hành CLI**
    Tạo tệp `language-wiki/commands/wiki.md`:
    ```markdown
    # Lệnh điều hành /language-wiki:wiki
    Cú pháp:
    - `/language-wiki:wiki init <name>`
    - `/language-wiki:wiki ingest <path>`
    - `/language-wiki:wiki compile`
    - `/language-wiki:wiki study`
    - `/language-wiki:wiki query "<question>"`
    - `/language-wiki:wiki lint`
    - `/language-wiki:wiki snapshot <label>`
    ```
- [ ] **Step 3: Khởi tạo SKILL.md hướng dẫn Agent**
    Tạo tệp `language-wiki/skills/wiki/SKILL.md` để cấu hình quy trình Agent tự đọc và tự viết từ vựng, ngữ pháp.
- [ ] **Step 4: Commit**
    ```bash
    git add language-wiki/plugin.json language-wiki/commands/wiki.md language-wiki/skills/wiki/SKILL.md
    git commit -m "feat: initialize language-wiki plugin structures"
    ```

---

### Task 2: Quản lý Advisory Lockfile & Tự tìm kiếm tài liệu (Auto-Sourcing)
**Files:**
*   Create: `language-wiki/scripts/lock-manager.py`
*   Create: `language-wiki/language_wiki_mcp/index.js`
*   Create: `language-wiki/language_wiki_mcp/package.json`

- [ ] **Step 1: Tạo Script quản lý khóa đồng thì**
    Tạo tệp `language-wiki/scripts/lock-manager.py` dùng để quản lý lockfile chống xung đột:
    ```python
    import os, sys, json, psutil
    lock_path = sys.argv[1]
    op = sys.argv[2]
    if os.path.exists(lock_path):
        with open(lock_path, 'r') as f:
            data = json.load(f)
        if psutil.pid_exists(data['pid']):
            print(f"Error: LockHeld by {data['operation']}")
            sys.exit(1)
    with open(lock_path, 'w') as f:
        json.dump({"pid": os.getpid(), "operation": op}, f)
    ```
- [ ] **Step 2: Tạo package.json cho máy chủ MCP**
    Tạo tệp `language-wiki/language_wiki_mcp/package.json`:
    ```json
    {
      "name": "language-wiki-mcp",
      "version": "1.0.0",
      "dependencies": {
        "@modelcontextprotocol/sdk": "^1.0.1",
        "express": "^4.19.2"
      }
    }
    ```
- [ ] **Step 3: Thiết lập lệnh discover trong MCP Server**
    Tạo tệp `language-wiki/language_wiki_mcp/index.js` để định nghĩa công cụ `search_korean_resources` gọi Parallel Web Search và cào thông tin lý thuyết ngữ pháp/từ vựng thô lưu vào `raw/extracts/`.
- [ ] **Step 4: Commit**
    ```bash
    git add language-wiki/scripts/lock-manager.py language-wiki/language_wiki_mcp/
    git commit -m "feat: add lockfile and auto-sourcing mcp tools"
    ```

---

### Task 3: Phát triển Bộ phân tích cú pháp thẻ nhớ Markdown & Bộ nhớ đệm (Cache)
**Files:**
*   Create: `language-wiki/study-app/server/parser.js`
*   Create: `language-wiki/study-app/server/index.js`
*   Create: `language-wiki/study-app/package.json`

- [ ] **Step 1: Tạo tệp package.json khởi động song hành**
    Tạo tệp `language-wiki/study-app/package.json`:
    ```json
    {
      "name": "study-app",
      "scripts": {
        "dev": "vite",
        "server": "node server/index.js",
        "start": "concurrently \"npm run dev\" \"npm run server\""
      },
      "dependencies": {
        "express": "^4.19.2",
        "concurrently": "^8.2.2"
      }
    }
    ```
- [ ] **Step 2: Viết bộ phân tích cú pháp Parser Separation**
    Tạo tệp `language-wiki/study-app/server/parser.js` để đọc ghi file `.md` bằng cách tách `::` và `<!--`:
    ```javascript
    const fs = require('fs');
    function parseCardLine(line) {
      if (!line.includes('::')) return null;
      const parts = line.split('::');
      const left = parts[0].trim();
      const right = parts[1].trim();
      
      const wordMatch = left.match(/-\s*(.+?)\s*\(\*\*(.+?)\*\*\)/);
      if (!wordMatch) return null;
      
      const word = wordMatch[1];
      const pronunciation = wordMatch[2];
      
      let meaning = right;
      let sr = null;
      if (right.includes('<!--')) {
        const commentParts = right.split('<!--');
        meaning = commentParts[0].trim();
        const comment = commentParts[1].replace('-->', '').trim();
        const dueMatch = comment.match(/due\s+(\d{4}-\d{2}-\d{2})/);
        const intervalMatch = comment.match(/interval\s+(\d+)/);
        const easeMatch = comment.match(/ease\s+(\d+)/);
        const streakMatch = comment.match(/streak\s+(\d+)/);
        sr = {
          due: dueMatch ? dueMatch[1] : null,
          interval: intervalMatch ? parseInt(intervalMatch[1]) : 1,
          ease: easeMatch ? parseInt(easeMatch[1]) : 250,
          streak: streakMatch ? parseInt(streakMatch[1]) : 0
        };
      }
      return { word, pronunciation, meaning, sr };
    }
    module.exports = { parseCardLine };
    ```
- [ ] **Step 3: Lập trình API Server & Cơ chế Cache Ôn tập**
    Hoàn thiện tệp `language-wiki/study-app/server/index.js` hỗ trợ lưu bộ nhớ đệm `.study-cache.json` và thực hiện Atomic Write (ghi qua file `.tmp` trước khi đổi tên). Sử dụng cơ chế Batching để gom góp các hành động Git commit sau mỗi 10 phút hoặc khi kết thúc phiên.
- [ ] **Step 4: Commit**
    ```bash
    git add language-wiki/study-app/package.json language-wiki/study-app/server/
    git commit -m "feat: add robust card parser and express server index"
    ```

---

### Task 4: Xây dựng Giao diện Dashboard & Quizzer Ôn tập (Active Recall)
**Files:**
*   Create: `language-wiki/study-app/src/App.jsx`
*   Create: `language-wiki/study-app/src/components/ActiveRecallQuizzer.jsx`
*   Create: `language-wiki/study-app/src/index.css`

- [ ] **Step 1: Tạo giao diện nền tảng Premium Glassmorphism**
    Tạo tệp `language-wiki/study-app/src/index.css` định nghĩa phong cách màu tối cao cấp, các khối thẻ nổi blur.
- [ ] **Step 2: Viết linh hồn giao diện trắc nghiệm Active Recall**
    Tạo tệp `language-wiki/study-app/src/components/ActiveRecallQuizzer.jsx`. Tích hợp:
    *   Mức độ gõ **Trung bình (Medium)**: Hiện gợi ý độ dài từ `_ _`.
    *   Mức độ gõ **Khó (Hard)**: Bắt gõ chính xác 100% không gợi ý.
    *   Phát âm đối chiếu: Nút loa 1 đọc từng từ gốc thô, nút loa 2 đọc biến âm tự nhiên.
- [ ] **Step 3: Thiết lập Dashboard theo dõi tiến độ**
    Tạo tệp `language-wiki/study-app/src/App.jsx` làm màn hình trung tâm quản lý hàng đợi ưu tiên phiên học (Session Queue) để chèn thẻ bị *Again* quay lại kiểm tra sau 20 phút.
- [ ] **Step 4: Commit**
    ```bash
    git add language-wiki/study-app/src/
    git commit -m "feat: implement premium study app UI dashboard and quizzer"
    ```

---

### Task 5: Triển khai Chế độ Luyện Nói Đàm Thoại (Speaking Mode - STT)
**Files:**
*   Create: `language-wiki/study-app/src/components/SpeakingMode.jsx`
*   Modify: `language-wiki/study-app/src/App.jsx`

- [ ] **Step 1: Viết Component xử lý Nhận diện giọng nói STT**
    Tạo tệp `language-wiki/study-app/src/components/SpeakingMode.jsx`:
    ```javascript
    import React, { useState, useEffect } from 'react';
    export default function SpeakingMode({ dialogueScript }) {
      const [transcript, setTranscript] = useState('');
      const [isListening, setIsListening] = useState(false);
      let recognition;
      
      const startListening = () => {
        const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
        if (!SpeechRecognition) return alert("Trình duyệt không hỗ trợ nhận âm.");
        recognition = new SpeechRecognition();
        recognition.lang = 'ko-KR';
        recognition.onstart = () => setIsListening(true);
        recognition.onend = () => setIsListening(false);
        recognition.onresult = (event) => {
          setTranscript(event.results[0][0].transcript);
        };
        recognition.start();
      };
      
      return (
        <div className="speaking-container">
          <button onClick={startListening}>{isListening ? "Đang nghe..." : "Giữ để nói"}</button>
          <p>Từ ghi nhận được: {transcript}</p>
        </div>
      );
    }
    ```
- [ ] **Step 2: Nhúng Speaking Mode vào luồng hiển thị chính**
    Sửa tệp `language-wiki/study-app/src/App.jsx` để thêm tùy chọn chuyển đổi chế độ học đàm thoại tình huống `s-*.md`.
- [ ] **Step 3: Commit**
    ```bash
    git add language-wiki/study-app/src/components/SpeakingMode.jsx language-wiki/study-app/src/App.jsx
    git commit -m "feat: implement interactive STT speaking mode"
    ```

---

### Task 6: Lập trình Module Thi Cử & Chẩn đoán Lỗi Sai (Exam Simulator)
**Files:**
*   Create: `language-wiki/study-app/src/components/ExamSimulator.jsx`
*   Modify: `language-wiki/study-app/server/index.js`

- [ ] **Step 1: Tạo giao diện giả lập thi cử**
    Tạo tệp `language-wiki/study-app/src/components/ExamSimulator.jsx` tích hợp đồng hồ đếm ngược (Countdown Timer) và bảng câu hỏi trắc nghiệm TOPIK.
- [ ] **Step 2: API Chấm điểm và phân tích lỗ hổng kiến thức**
    Cấu hình thêm endpoint `POST /api/exams/submit` trong tệp `language-wiki/study-app/server/index.js` để tự động chấm điểm và trả về danh sách liên kết ngữ pháp `[[g-*.md]]` bị hỏng kiến thức để học viên mở lại trên Obsidian.
- [ ] **Step 3: Commit**
    ```bash
    git add language-wiki/study-app/src/components/ExamSimulator.jsx language-wiki/study-app/server/index.js
    git commit -m "feat: add exam simulator and grammar diagnostics"
    ```
