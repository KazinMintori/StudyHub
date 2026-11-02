import re, glob, os, sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def check_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
        lines = content.splitlines()

    errors = []
    warnings = []

    in_code_block = False
    for idx, line in enumerate(lines, 1):
        if line.strip().startswith('```'):
            in_code_block = not in_code_block
            continue
        if in_code_block or line.strip().startswith('$$'):
            continue
        # match colon followed by space and lowercase letter
        # exclude math expressions ($...$), urls, code, and yaml keys
        if line.startswith('---') or line.startswith('topic:') or line.startswith('course:') or line.startswith('lecture:') or line.startswith('section:') or line.startswith('<!--'):
            continue
        # pattern: colon, space(s), lowercase vietnamese letter
        m = re.search(r':\s+([a-zàáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđ])', line)
        if m:
            # check if it is inside math ($...$) or inside a link [text](url)
            pos = m.start()
            prefix = line[:pos]
            dollar_count = prefix.count('$')
            if dollar_count % 2 == 0:
                # not inside math
                # check if inside inline code `...`
                tick_count = prefix.count('`')
                if tick_count % 2 == 0:
                    errors.append(f"Line {idx}: Lowercase letter after colon: '{line[pos:pos+6]}'")

    # 2. Check vert / Vert
    for idx, line in enumerate(lines, 1):
        if r'\vert{}' in line or r'\Vert{}' in line:
            errors.append(f"Line {idx}: Forbidden \\vert{{}} or \\Vert{{}}")

    # 3. Check inline math length (> 38ex)
    for idx, line in enumerate(lines, 1):
        # find $...$ but not $$...$$
        matches = re.finditer(r'(?<!\$)\$(?!\$)(.*?)(?<!\$)\$(?!\$)', line)
        for m in matches:
            expr = m.group(1)
            if len(expr) > 38 and not expr.strip().startswith('\\text{'):
                # warning or error
                warnings.append(f"Line {idx}: Inline math length {len(expr)} > 38: '${expr}$'")

    # 4. Check display math with hanging plus or minus
    for idx, line in enumerate(lines, 1):
        if re.search(r'(\+|\-|\*|\\cdot)\s*\\\\', line):
            errors.append(f"Line {idx}: Math line-break on operator before equals")

    return errors, warnings

files = sorted(glob.glob('tmp/artint3e-integration-20261102/docs/ai-nen-tang-tac-tu/bai-giang/09-suy-luan-trong-dieu-kien-bat-dinh/*.md'))
if not files:
    files = sorted(glob.glob('docs/ai-nen-tang-tac-tu/bai-giang/09-suy-luan-trong-dieu-kien-bat-dinh/*.md'))
total_errors = 0
total_warnings = 0

print(f"Checking {len(files)} files...")
for p in files:
    errs, warns = check_file(p)
    if errs or warns:
        print(f"=== {p} ===")
        for e in errs:
            print(f"  [ERROR] {e}")
            total_errors += 1
        for w in warns:
            print(f"  [WARN] {w}")
            total_warnings += 1
    else:
        print(f"OK: {p}")

print(f"\nTotal files checked: {len(files)}, Errors: {total_errors}, Warnings: {total_warnings}")
