import os
import sys
import re
import glob

sys.stdout.reconfigure(encoding='utf-8')

book_kw = re.compile(r'\b(sách|nguyên tác|bản dịch|theo Boyd|Boyd & Vandenberghe|trong sách)\b', re.IGNORECASE)
ai_kw = re.compile(r'\b(kỳ diệu|vô cùng|cực kỳ|ma thuật|vi diệu)\b', re.IGNORECASE)

files = glob.glob("docs/toan-cho-ai/bai-giang/**/*.md", recursive=True)
files = sorted(list(set(files)))

print(f"{'File':<60} | {'Sách':<6} | {'AI':<6} | {'Colon Lower':<12}")
print("-" * 90)

total_book = 0
total_ai = 0
total_colon = 0

for filepath in files:
    if not os.path.isfile(filepath):
        continue
    with open(filepath, 'r', encoding='utf-8') as fp:
        lines = fp.readlines()

    book_cnt = 0
    ai_cnt = 0
    colon_cnt = 0

    in_code = False
    in_math = False
    in_frontmatter = False

    for i, line in enumerate(lines):
        raw = line.strip()
        if i == 0 and raw == '---':
            in_frontmatter = True
            continue
        if in_frontmatter:
            if raw == '---':
                in_frontmatter = False
            continue
        if raw.startswith('```'):
            in_code = not in_code
            continue
        if raw.startswith('$$'):
            in_math = not in_math
            continue
        if in_code or in_math:
            continue

        clean_line = re.sub(r'(ngân sách|danh sách)', '', raw, flags=re.IGNORECASE)
        if clean_line.startswith('- **Stephen Boyd') or clean_line.startswith('- S. Boyd') or clean_line.startswith('- Stephen Boyd'):
            continue

        if book_kw.search(clean_line):
            book_cnt += 1

        if ai_kw.search(raw):
            ai_cnt += 1

        if not (raw.startswith('<') or 'style=' in raw or 'viewBox=' in raw):
            no_math = re.sub(r'\$[^\$]+\$', '', raw)
            no_math = re.sub(r'&[a-zA-Z0-9_]+;', '', no_math)
            m_colon = re.search(r':\s+([a-zàáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđ])', no_math)
            if m_colon and not raw.startswith(':::') and not re.search(r'(https?|file|C):', raw):
                colon_cnt += 1

    fname = os.path.basename(filepath)
    prefix = filepath.split('/')[-2] if '/' in filepath else filepath.split('\\')[-2]
    disp = f"{prefix}/{fname}" if prefix != "bai-giang" else fname
    print(f"{disp:<60} | {book_cnt:<6} | {ai_cnt:<6} | {colon_cnt:<12}")

    total_book += book_cnt
    total_ai += ai_cnt
    total_colon += colon_cnt

print("-" * 90)
print(f"{'TỔNG CỘNG':<60} | {total_book:<6} | {total_ai:<6} | {total_colon:<12}")
