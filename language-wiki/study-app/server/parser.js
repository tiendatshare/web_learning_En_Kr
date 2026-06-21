const fs = require('fs');

function parseCardLine(line) {
  if (!line.includes('::')) return null;
  
  // Extract leading prefix (must start with a bullet point to be a card)
  const prefixMatch = line.match(/^([ \t]*[-\*\+][ \t]*)/);
  if (!prefixMatch) return null;
  const prefix = prefixMatch[1];
  const cleanLine = line.substring(prefix.length).trim();
  
  const parts = cleanLine.split('::');
  const left = parts[0].trim();
  const right = parts[1].trim();
  
  // Extract word and pronunciation from left side
  let word = left;
  let pronunciation = "";
  let pronType = "asterisk";
  
  const pMatchAsterisk = left.match(/(.+?)\s*\(\*\*(.+?)\*\*\)/);
  if (pMatchAsterisk) {
    word = pMatchAsterisk[1].trim();
    pronunciation = pMatchAsterisk[2].trim();
    pronType = "asterisk";
  } else {
    const pMatchSimple = left.match(/(.+?)\s*\((.+?)\)/);
    if (pMatchSimple) {
      word = pMatchSimple[1].trim();
      pronunciation = pMatchSimple[2].trim();
      pronType = "simple";
    } else {
      const pMatchSlash = left.match(/(.+?)\s*\/([^\/]+)\//);
      if (pMatchSlash) {
        word = pMatchSlash[1].trim();
        pronunciation = pMatchSlash[2].trim();
        pronType = "slash";
      }
    }
  }
  
  // Clean word from any stray formatting
  word = word.replace(/^[-\*\s\+]+/, '').trim();
  
  // Parse right side comments and tags
  let rightNoComments = right.replace(/<!--[\s\S]*?-->/g, '').trim();
  
  // Extract tag like "| #TOPIK-1" or "| #IELTS-7"
  const tagMatch = rightNoComments.match(/\|\s*(#[A-Za-z0-9_-]+)/);
  const tag = tagMatch ? tagMatch[1] : null;
  
  let meaning = rightNoComments;
  if (tag) {
    meaning = meaning.replace(/\|\s*(#[A-Za-z0-9_-]+)/, '').trim();
  }
  // Strip markdown bold markers from meaning
  meaning = meaning.replace(/\*\*/g, '').trim();
  
  // Scan all comments
  const comments = [];
  const commentRegex = /<!--\s*([\s\S]*?)\s*-->/g;
  let match;
  while ((match = commentRegex.exec(right)) !== null) {
    comments.push(match[1].trim());
  }
  
  let sr = null;
  let cognitive = null;
  
  comments.forEach(comment => {
    if (comment.startsWith('sr:')) {
      const dueMatch = comment.match(/due\s+(\d{4}-\d{2}-\d{2})/);
      const intervalMatch = comment.match(/interval\s+(\d+)/);
      const easeMatch = comment.match(/ease\s+(\d+)/);
      const streakMatch = comment.match(/streak\s+(\d+)/);
      
      sr = {
        due: dueMatch ? dueMatch[1] : null,
        interval: intervalMatch ? parseInt(intervalMatch[1], 10) : 1,
        ease: easeMatch ? parseInt(easeMatch[1], 10) : 250,
        streak: streakMatch ? parseInt(streakMatch[1], 10) : 0
      };
    } else if (comment.startsWith('cognitive:')) {
      try {
        const jsonStr = comment.substring('cognitive:'.length).trim();
        cognitive = JSON.parse(jsonStr);
      } catch (e) {
        // Silently catch manual editing formatting errors
      }
    }
  });
  
  return { prefix, word, pronunciation, pronType, meaning, tag, sr, cognitive };
}

function serializeCardLine(card) {
  const { prefix, word, pronunciation, pronType, meaning, tag, sr, cognitive } = card;
  const cleanPrefix = prefix || '- ';
  let left = `${word}`;
  if (pronunciation) {
    if (pronType === 'slash') {
      left += ` /${pronunciation}/`;
    } else if (pronType === 'simple') {
      left += ` (${pronunciation})`;
    } else {
      left += ` (**${pronunciation}**)`;
    }
  }
  let right = meaning;
  if (tag) {
    right += ` | ${tag}`;
  }
  if (sr && sr.due) {
    right += ` <!-- sr: due ${sr.due} interval ${sr.interval} ease ${sr.ease} streak ${sr.streak} -->`;
  }
  if (cognitive) {
    right += ` <!-- cognitive: ${JSON.stringify(cognitive)} -->`;
  }
  return `${cleanPrefix}${left} :: ${right}`;
}

module.exports = { parseCardLine, serializeCardLine };

