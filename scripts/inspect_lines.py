import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

book_kw = re.compile(r'\b(sách|nguyên tác|bản dịch|theo Boyd|Boyd & Vandenberghe|trong sách)\b', re.IGNORECASE)
ai_kw = re.compile(r'\b(kỳ diệu|vô cùng|cực kỳ|ma thuật|vi diệu|tinh hoa|bức tranh toàn cảnh)\b', re.IGNORECASE)

filepath = sys.argv[1]
if not os.path.isfile(filepath):
    print("File not found:", filepath)
    sys.exit(1)

with open(filepath, 'r', encoding='utf-8') as fp:
    lines = fp.readlines()

in_code = False
in_math = False
in_frontmatter = False

print(f"=== CHI TIẾT FILE: {filepath} ===")
for i, line in enumerate(lines):
    raw = line.strip()
    lineno = i + 1
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

    # Bỏ qua toàn bộ dòng thẻ HTML / SVG thuần túy
    if raw.startswith('<') or raw.startswith('</') or 'style=' in raw or 'viewBox=' in raw or 'xmlns=' in raw or '<path' in raw or '<rect' in raw or '<circle' in raw or '<text' in raw or '<line' in raw:
        continue

    if '::: important' in raw:
        print(f"L{lineno} [IMPORTANT]: {raw}")

    clean_line = re.sub(r'(ngân sách|danh sách)', '', raw, flags=re.IGNORECASE)
    if not (clean_line.startswith('- **Stephen Boyd') or clean_line.startswith('- S. Boyd') or clean_line.startswith('- Stephen Boyd')):
        if book_kw.search(clean_line):
            print(f"L{lineno} [BOOK]: {raw}")

    if ai_kw.search(raw):
        print(f"L{lineno} [AI]: {raw}")

    if '—' in raw and not raw.startswith('|') and not raw.startswith('---'):
        print(f"L{lineno} [EMDASH]: {raw}")

    # Lọc bỏ HTML, code, math khỏi text
    no_html = re.sub(r'<[^>]+>', '', raw)
    no_ent = re.sub(r'&[a-zA-Z0-9_#]+;', '', no_html)
    no_math = re.sub(r'\$[^\$]+\$', '', no_ent)
    no_code = re.sub(r'`[^`]+`', '', no_math)

    if ';' in no_code and not raw.startswith('|'):
        print(f"L{lineno} [SEMI]: {raw}")

    m_colon = re.search(r':\s+([a-zàáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđ])', no_code)
    if m_colon and not raw.startswith(':::') and not re.search(r'(https?|file|C):', raw):
        print(f"L{lineno} [COLON_LOWER]: {raw}")
