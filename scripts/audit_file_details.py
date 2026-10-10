import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

if len(sys.argv) < 2:
    print("Usage: python audit_file_details.py <filepath>")
    sys.exit(1)

filepath = sys.argv[1]

with open(filepath, 'r', encoding='utf-8') as fp:
    lines = fp.readlines()

print(f"=== Chi tiết file: {filepath} ===")

book_kw = re.compile(r'\b(sách|nguyên tác|bản dịch|theo Boyd|Boyd & Vandenberghe|trong sách)\b', re.IGNORECASE)

in_code = False
in_math = False
in_frontmatter = False

for i, line in enumerate(lines):
    lno = i + 1
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

    # Book kw
    if book_kw.search(clean_line):
        print(f"[BOOK] Dòng {lno}: {raw}")

    # Colon lowercase
    no_math = re.sub(r'\$[^\$]+\$', '', raw)
    no_math = re.sub(r'&[a-zA-Z0-9_]+;', '', no_math)
    m_colon = re.search(r':\s+([a-zàáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđ])', no_math)
    if m_colon and not raw.startswith(':::') and not re.search(r'(https?|file|C):', raw):
        print(f"[COLON_LOWER] Dòng {lno} (chữ '{m_colon.group(1)}'): {raw}")

    # AI emotive
    if re.search(r'\b(kỳ diệu|vô cùng|cực kỳ|ma thuật|vi diệu)\b', raw, re.IGNORECASE):
        print(f"[AI_EMOTIVE] Dòng {lno}: {raw}")
