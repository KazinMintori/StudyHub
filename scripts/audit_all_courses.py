import os
import sys
import re
import glob

sys.stdout.reconfigure(encoding='utf-8')

book_kw = re.compile(r'\b(sách|nguyên tác|bản dịch|theo Boyd|Boyd & Vandenberghe|trong sách)\b', re.IGNORECASE)
ai_kw = re.compile(r'\b(kỳ diệu|vô cùng|cực kỳ|ma thuật|vi diệu|tinh hoa|bức tranh toàn cảnh)\b', re.IGNORECASE)

courses = [
    "docs/xu-ly-du-lieu",
    "docs/bieu-dien-tri-thuc",
    "docs/giai-thuat-du-lieu",
    "docs/xac-suat-thong-ke",
    "docs/dsa",
    "docs/toan-cho-ai"
]

target_course = sys.argv[1] if len(sys.argv) > 1 else None

for course in courses:
    if target_course and target_course not in course:
        continue
    files = sorted(glob.glob(f"{course}/**/*.md", recursive=True))
    if not files:
        continue

    print(f"\n=======================================================")
    print(f" KHẢO SÁT MÔN: {course} ({len(files)} files)")
    print(f"=======================================================")
    print(f"{'File':<55} | {'Sách':<5} | {'AI':<4} | {'ColLow':<6} | {'Semi':<5} | {'EmDash':<6} | {'Import':<6}")
    print("-" * 95)

    c_book = 0
    c_ai = 0
    c_colon = 0
    c_semi = 0
    c_dash = 0
    c_import = 0

    for filepath in files:
        with open(filepath, 'r', encoding='utf-8') as fp:
            lines = fp.readlines()

        book_cnt = 0
        ai_cnt = 0
        colon_cnt = 0
        semi_cnt = 0
        dash_cnt = 0
        import_cnt = 0

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

            if raw.startswith('<') or raw.startswith('</') or 'style=' in raw or 'viewBox=' in raw or 'xmlns=' in raw or '<path' in raw or '<rect' in raw or '<circle' in raw or '<text' in raw or '<line' in raw:
                continue

            if '::: important' in raw:
                import_cnt += 1

            clean_line = re.sub(r'(ngân sách|danh sách)', '', raw, flags=re.IGNORECASE)
            if clean_line.startswith('- **Stephen Boyd') or clean_line.startswith('- S. Boyd') or clean_line.startswith('- Stephen Boyd'):
                continue

            if book_kw.search(clean_line):
                book_cnt += 1

            if ai_kw.search(raw):
                ai_cnt += 1

            if '—' in raw and not raw.startswith('|') and not raw.startswith('---'):
                dash_cnt += raw.count('—')

            no_html = re.sub(r'<[^>]+>', '', raw)
            no_ent = re.sub(r'&[a-zA-Z0-9_#]+;', '', no_html)
            no_math = re.sub(r'\$[^\$]+\$', '', no_ent)
            no_code = re.sub(r'`[^`]+`', '', no_math)

            if ';' in no_code and not raw.startswith('|'):
                semi_cnt += no_code.count(';')

            m_colon = re.search(r':\s+([a-zàáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđ])', no_code)
            if m_colon and not raw.startswith(':::') and not re.search(r'(https?|file|C):', raw):
                colon_cnt += 1

        if book_cnt or ai_cnt or colon_cnt or semi_cnt or dash_cnt or import_cnt:
            rel = os.path.relpath(filepath, course)
            print(f"{rel:<55} | {book_cnt:<5} | {ai_cnt:<4} | {colon_cnt:<6} | {semi_cnt:<5} | {dash_cnt:<6} | {import_cnt:<6}")

        c_book += book_cnt
        c_ai += ai_cnt
        c_colon += colon_cnt
        c_semi += semi_cnt
        c_dash += dash_cnt
        c_import += import_cnt

    print("-" * 95)
    print(f"{'TỔNG ' + course:<55} | {c_book:<5} | {c_ai:<4} | {c_colon:<6} | {c_semi:<5} | {c_dash:<6} | {c_import:<6}")
