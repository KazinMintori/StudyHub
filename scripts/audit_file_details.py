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

book_kw = re.compile(r'\b(sách|nguyên tác|bản dịch|theo Boyd|Boyd & Vandenberghe|trong sách|lấy từ giáo trình|theo giáo trình|lấy từ slide|do người soạn thêm|ảnh lấy từ)\b', re.IGNORECASE)

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

    # Em dash in prose
    if not raw.startswith('|') and not raw.startswith('#') and not raw.startswith(':::') and not raw.startswith('<!--'):
        if '—' in no_math:
            print(f"[EM_DASH] Dòng {lno}: {raw}")

    # Math vert syntax check
    if r'\vert{' in raw or r'\Vert{' in raw:
        print(f"[MATH_VERT] Dòng {lno}: Dùng \\vert{{}} hoặc \\Vert{{}}, hãy đổi sang |...| hoặc \\lVert ... \\rVert: {raw}")

    # Thinking aloud in solutions
    if re.search(r'\b(khoan đã|à không|nhầm rồi|thử lại nào|ý tôi là)\b', raw, re.IGNORECASE):
        print(f"[THINKING_ALOUD] Dòng {lno}: {raw}")

    # Fabricated error frequency
    if re.search(r'\b(rất phổ biến|cực kỳ phổ biến|đa số sinh viên|phần lớn sinh viên|bẫy thi cử)\b', raw, re.IGNORECASE):
        print(f"[ERROR_FREQUENCY] Dòng {lno}: {raw}")

