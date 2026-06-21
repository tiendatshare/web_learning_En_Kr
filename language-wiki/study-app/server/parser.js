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
  
  const pMatchAsterisk = left.match(/(.+?)\s*\(\*\*(.+?)\*\*\)/);
  if (pMatchAsterisk) {
    word = pMatchAsterisk[1].trim();
    pronunciation = pMatchAsterisk[2].trim();
  } else {
    const pMatchSimple = left.match(/(.+?)\s*\((.+?)\)/);
    if (pMatchSimple) {
      word = pMatchSimple[1].trim();
      pronunciation = pMatchSimple[2].trim();
    } else {
      const pMatchSlash = left.match(/(.+?)\s*\/([^\/]+)\//);
      if (pMatchSlash) {
        word = pMatchSlash[1].trim();
        pronunciation = pMatchSlash[2].trim();
      }
    }
  }
  
  // Clean word from any stray formatting
  word = word.replace(/^[-\*\s\+]+/, '').trim();
  
  // Parse right side
  let meaning = right;
  let sr = null;

  // Strip trailing Obsidian tags like "| #TOPIK-1" or "| #TOPIK-2"
  meaning = meaning.replace(/\s*\|\s*#[A-Za-z0-9_-]+\s*/g, '').trim();
  // Strip markdown bold markers from meaning
  meaning = meaning.replace(/\*\*/g, '').trim();
  
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
      interval: intervalMatch ? parseInt(intervalMatch[1], 10) : 1,
      ease: easeMatch ? parseInt(easeMatch[1], 10) : 250,
      streak: streakMatch ? parseInt(streakMatch[1], 10) : 0
    };
  }
  
  return { prefix, word, pronunciation, meaning, sr };
}

function serializeCardLine(card) {
  const { prefix, word, pronunciation, meaning, sr } = card;
  const cleanPrefix = prefix || '- ';
  let left = `${word}`;
  if (pronunciation) {
    left += ` (**${pronunciation}**)`;
  }
  let right = meaning;
  if (sr && sr.due) {
    right += ` <!-- sr: due ${sr.due} interval ${sr.interval} ease ${sr.ease} streak ${sr.streak} -->`;
  }
  return `${cleanPrefix}${left} :: ${right}`;
}

module.exports = { parseCardLine, serializeCardLine };
