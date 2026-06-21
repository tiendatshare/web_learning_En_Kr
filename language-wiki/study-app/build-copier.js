const fs = require('fs');
const path = require('path');

function copyFolderSync(from, to) {
  if (!fs.existsSync(from)) return;
  if (!fs.existsSync(to)) {
    fs.mkdirSync(to, { recursive: true });
  }
  fs.readdirSync(from).forEach(element => {
    const fromPath = path.join(from, element);
    const toPath = path.join(to, element);
    if (fs.lstatSync(fromPath).isDirectory()) {
      copyFolderSync(fromPath, toPath);
    } else {
      fs.copyFileSync(fromPath, toPath);
    }
  });
}

// Copy Korean Wiki
const fromKorean = path.resolve(__dirname, '../../MD_korea_learning/wiki');
const toKorean = path.resolve(__dirname, './MD_korea_learning/wiki');
console.log(`Copying Korean wiki from ${fromKorean} to ${toKorean}...`);
copyFolderSync(fromKorean, toKorean);

// Copy English Wiki
const fromEnglish = path.resolve(__dirname, '../../MD_english_learning/wiki');
const toEnglish = path.resolve(__dirname, './MD_english_learning/wiki');
console.log(`Copying English wiki from ${fromEnglish} to ${toEnglish}...`);
copyFolderSync(fromEnglish, toEnglish);

console.log('Build copying complete!');
