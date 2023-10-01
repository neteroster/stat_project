const fs = require('fs');
const path = require('path');
const crypto = require('crypto');

const LANGS = ['python', 'javascript', 'cpp', 'java', 'go', 'rust'];

const LANGS_EXTENSION = {
    'python': ['py'],
    'javascript': ['js'],
    'cpp': ['cpp', 'h', 'hpp', 'cxx'],
    'java': ['java'],
    'go': ['go'],
    'rust': ['rs']
}

const SOURCE_DIR = 'C:/Users/neter/Downloads/Stat/proj/repos';
const TARGET_DIR = 'C:/Users/neter/Downloads/Stat/proj/raw_source';

function walkDirRecursive(dir, callback) {
    fs.readdirSync(dir).forEach(f => {
        const dirPath = path.join(dir, f);
        const isDir = fs.statSync(dirPath).isDirectory();

        isDir ? walkDirRecursive(dirPath, callback) : callback(path.join(dir, f));
    });
}

function lineCount(file) {
    return fs.readFileSync(file).toString().split('\n').length;
}

function codeStats(dir) {
    let stats = {
        total: 0,
        files: Object.fromEntries(LANGS.map(l => [l, 0])),
        lines: Object.fromEntries(LANGS.map(l => [l, 0]))
    };

    walkDirRecursive(dir, f => {
        const ext = f.split('.').pop();
        const lang = Object.keys(LANGS_EXTENSION).find(l => LANGS_EXTENSION[l].includes(ext));

        if (lang) {
            stats.total++;
            stats.files[lang]++;
            stats.lines[lang] += lineCount(f);
        }
    });

    return stats;
}

function initTargetDir() {
    LANGS.forEach(l => {
        const langDir = path.join(TARGET_DIR, l);

        if (!fs.existsSync(langDir)) {
            fs.mkdirSync(langDir);
        }
    });
}

function copySource(srcDir, destDir) {
    walkDirRecursive(srcDir, f => {
        const ext = f.split('.').pop();
        const lang = Object.keys(LANGS_EXTENSION).find(l => LANGS_EXTENSION[l].includes(ext));

        if (!lang) { return; }

        const sha = crypto.createHash('sha256').update(fs.readFileSync(f)).digest('hex');
        const target = path.join(destDir, lang, lang + '_' + sha);

        if (!fs.existsSync(target)) {
            fs.copyFileSync(f, target);
        }
        
    });
}

console.log(codeStats("C:/Users/neter/Downloads/Stat/proj/merged"));
