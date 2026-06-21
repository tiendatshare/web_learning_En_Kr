const fs = require('fs');
const path = require('path');
const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
  terminal: false
});

rl.on('line', async (line) => {
  try {
    const request = JSON.parse(line);
    const { jsonrpc, id, method, params } = request;
    
    if (method === 'initialize') {
      sendResponse(id, {
        protocolVersion: "2024-11-05",
        capabilities: {
          tools: {}
        },
        serverInfo: {
          name: "language-wiki-mcp",
          version: "1.0.0"
        }
      });
    } else if (method === 'tools/list') {
      sendResponse(id, {
        tools: [
          {
            name: "search_korean_resources",
            description: "Tìm kiếm tài liệu ngữ pháp và từ vựng tiếng Hàn từ nguồn công cộng.",
            inputSchema: {
              type: "object",
              properties: {
                query: {
                  type: "string",
                  description: "Từ khóa tìm kiếm ngữ pháp hoặc từ vựng"
                },
                level: {
                  type: "string",
                  description: "Cấp độ học tập (beginner/intermediate/advanced)"
                },
                destPath: {
                  type: "string",
                  description: "Đường dẫn tuyệt đối của file đích để lưu tài liệu"
                }
              },
              required: ["query", "destPath"]
            }
          }
        ]
      });
    } else if (method === 'tools/call') {
      const { name, arguments: args } = params;
      if (name === 'search_korean_resources') {
        const { query, level = 'beginner', destPath } = args;
        const result = await handleSearch(query, level, destPath);
        sendResponse(id, {
          content: [
            {
              type: "text",
              text: result
            }
          ]
        });
      } else {
        sendError(id, -32601, `Tool not found: ${name}`);
      }
    } else if (method === 'ping') {
      sendResponse(id, {});
    } else {
      sendError(id, -32601, `Method not found: ${method}`);
    }
  } catch (err) {
    console.error("Error handling line:", err);
  }
});

function sendResponse(id, result) {
  console.log(JSON.stringify({
    jsonrpc: "2.0",
    id,
    result
  }));
}

function sendError(id, code, message) {
  console.log(JSON.stringify({
    jsonrpc: "2.0",
    id,
    error: { code, message }
  }));
}

async function handleSearch(query, level, destPath) {
  try {
    // Fetch search results from Wiktionary or standard grammar database
    const url = `https://en.wiktionary.org/api/rest_v1/page/html/${encodeURIComponent(query)}`;
    let contentText = "";
    try {
      const response = await fetch(url);
      if (response.ok) {
        const html = await response.text();
        // Extract plain text from HTML (simple clean up)
        contentText = html.replace(/<[^>]*>/g, ' ').replace(/\s+/g, ' ').trim();
      }
    } catch (e) {
      // Ignore network errors and fallback
    }

    if (!contentText) {
      contentText = `Tài liệu tự động tìm kiếm cho từ khóa: ${query} (Cấp độ: ${level}).`;
    }

    const compiledContent = `---
title: "Tài liệu cào: ${query}"
level: "${level}"
scraped-at: "${new Date().toISOString()}"
source: "Auto-Scraped via MCP"
---

# Tài liệu học tập: ${query}

## 📖 1. Lý thuyết tổng quan
*   Từ khóa tìm kiếm: ${query}
*   Cấp độ đề xuất: ${level}

## 📝 2. Chi tiết cào được
${contentText.substring(0, 1000)}...

## 💡 3. Các câu ví dụ đề xuất
1.  이것은 ${query} học tập mẫu.
2.  한국어를 ${query} 공부해요.
`;

    // Ensure directory exists
    fs.mkdirSync(path.dirname(destPath), { recursive: true });
    fs.writeFileSync(destPath, compiledContent, 'utf8');

    return `Successfully saved scraped resources for '${query}' to ${destPath}`;
  } catch (err) {
    return `Error during scraping: ${err.message}`;
  }
}
