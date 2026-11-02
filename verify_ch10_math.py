import re
import glob
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# Tập ký tự chữ thường tiếng Việt đầy đủ để tránh bắt nhầm chữ hoa Đ (U+0110)
VN_LOWER = "a-zàáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđ"

def check_file(path):
    content = open(path, encoding='utf-8').read()
    lines = content.split('\n')
    errors = []
    warnings = []

    # Xác định phạm vi frontmatter
    frontmatter_end_line = 0
    if len(lines) > 0 and lines[0].strip() == '---':
        for idx in range(1, len(lines)):
            if lines[idx].strip() == '---':
                frontmatter_end_line = idx + 1
                break

    in_math_block = False
    in_code_block = False

    # 1. Kiểm tra inline math dài (> 38ex)
    for i, line in enumerate(lines, 1):
        if i <= frontmatter_end_line:
            continue
        stripped = line.strip()
        if stripped.startswith('```'):
            in_code_block = not in_code_block
            continue
        if stripped == '$$':
            in_math_block = not in_math_block
            continue
        if in_code_block or in_math_block:
            continue

        inline_matches = re.findall(r'(?<!\$)\$(?!\$)(.*?)(?<!\$)\$(?!\$)', line)
        for m in inline_matches:
            if len(m) > 38:
                warnings.append(f"Line {i}: Inline math dài ({len(m)} ký tự > 38ex): ${m}$")

    # 2. Kiểm tra \vert{} hoặc \Vert{}
    if r'\vert{' in content or r'\Vert{' in content:
        errors.append("Phát hiện \\vert{} hoặc \\Vert{} - phải dùng |...| hoặc \\|...\\|")

    # 3. Kiểm tra ngắt dòng sau dấu bằng kiểu '= \\'
    if re.search(r'=\s*\\\\', content):
        errors.append("Phát hiện ngắt dòng ngay sau dấu bằng '= \\\\'")

    # 4. Kiểm tra ngắt dòng tại toán tử cộng trừ rớt số hạng: '+ \\' hoặc '- \\'
    if re.search(r'[+\-*/]\s*\\\\', content):
        errors.append("Phát hiện ngắt dòng tại toán tử cộng/trừ/nhân/chia trước '\\\\'")

    # 5. Kiểm tra viết thường sau dấu hai chấm trong văn xuôi
    in_math_block = False
    in_code_block = False
    for i, line in enumerate(lines, 1):
        if i <= frontmatter_end_line:
            continue
        stripped = line.strip()
        if stripped.startswith('```'):
            in_code_block = not in_code_block
            continue
        if stripped == '$$':
            in_math_block = not in_math_block
            continue
        if in_code_block or in_math_block:
            continue
        if stripped.startswith('http') or stripped.startswith('|'):
            continue

        # Tìm dấu hai chấm kèm chữ thường ngay sau (có khoảng trắng)
        m = re.search(rf':\s+([{VN_LOWER}])', line)
        if m:
            char = m.group(1)
            pos = m.start()
            prefix = line[:pos]
            dollar_count = prefix.count('$')
            backtick_count = prefix.count('`')
            if dollar_count % 2 == 0 and backtick_count % 2 == 0:
                warnings.append(f"Line {i}: Sau dấu hai chấm viết thường '{char}': ...{line[max(0, pos-15):min(len(line), pos+25)]}...")

    # 6. Kiểm tra $$ nằm trên dòng riêng
    for i, line in enumerate(lines, 1):
        if i <= frontmatter_end_line:
            continue
        stripped = line.strip()
        if '$$' in stripped and stripped != '$$':
            if not stripped.startswith('|'):
                warnings.append(f"Line {i}: Ký hiệu '$$' không nằm trên dòng riêng: {line}")

    return errors, warnings

files = glob.glob('docs/ai-nen-tang-tac-tu/bai-giang/10-hoc-may-trong-dieu-kien-bat-dinh*.md') + \
        glob.glob('docs/ai-nen-tang-tac-tu/bai-giang/10-hoc-may-trong-dieu-kien-bat-dinh/*.md')

total_err = 0
total_warn = 0

print(f"Kiểm tra {len(files)} tệp trong Chương 10:")
for f in sorted(files):
    errs, warns = check_file(f)
    if errs or warns:
        print(f"\n[!] {f}:")
        for e in errs:
            print(f"  - LỖI: {e}")
        for w in warns:
            print(f"  - CẢNH BÁO: {w}")
    else:
        print(f"  [OK] {f}")
    total_err += len(errs)
    total_warn += len(warns)

print(f"\nTổng kết: {len(files)} files, {total_err} lỗi, {total_warn} cảnh báo.")
if total_err > 0:
    sys.exit(1)
