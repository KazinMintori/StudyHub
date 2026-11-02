import re
import glob
import os
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
    frontmatter_dict = {}
    if len(lines) > 0 and lines[0].strip() == '---':
        for idx in range(1, len(lines)):
            if lines[idx].strip() == '---':
                frontmatter_end_line = idx + 1
                break
            parts = lines[idx].split(':', 1)
            if len(parts) == 2:
                frontmatter_dict[parts[0].strip()] = parts[1].strip()

    # Kiểm tra frontmatter bắt buộc
    if 'course' not in frontmatter_dict:
        errors.append("Thiếu trường 'course' trong frontmatter")
    if 'lecture' not in frontmatter_dict:
        errors.append("Thiếu trường 'lecture' trong frontmatter")
    if 'section' not in frontmatter_dict:
        errors.append("Thiếu trường 'section' trong frontmatter")
    if frontmatter_dict.get('section') == 'topic' and 'topic' not in frontmatter_dict:
        errors.append("Trang chủ đề (section: topic) nhưng thiếu trường 'topic' trong frontmatter")

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
        if stripped.startswith('http') or stripped.startswith('|') or stripped.startswith(':::') or stripped.startswith('>'):
            continue

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

    # 7. Kiểm tra cụm từ vi phạm chủ quyền bài giảng
    sovereignty_phrases = [
        "nội dung lấy từ", "lấy từ slide", "bài tập lấy từ", "ví dụ do người soạn",
        "ảnh lấy từ sách", "ảnh nguyên gốc sách", "hình trong sách", "dữ liệu này từ",
        "theo sách", "sách dùng", "nguyên tác", "bản dịch của", "tiến độ bản dịch"
    ]
    for i, line in enumerate(lines, 1):
        if i <= frontmatter_end_line:
            continue
        lower_line = line.lower()
        for phrase in sovereignty_phrases:
            if phrase in lower_line:
                errors.append(f"Line {i}: Vi phạm chủ quyền bài giảng: '{phrase}'")

    return errors, warnings

if __name__ == '__main__':
    base_dir = os.path.dirname(os.path.abspath(__file__))
    pattern1 = os.path.join(base_dir, 'docs/ai-nen-tang-tac-tu/bai-giang/13-hoc-tang-cuong*.md')
    pattern2 = os.path.join(base_dir, 'docs/ai-nen-tang-tac-tu/bai-giang/13-hoc-tang-cuong/*.md')
    files = sorted(glob.glob(pattern1) + glob.glob(pattern2))

    print(f"Kiểm tra {len(files)} tệp trong Chương 13:")
    total_errors = 0
    total_warnings = 0

    for f in files:
        errs, warns = check_file(f)
        total_errors += len(errs)
        total_warnings += len(warns)
        rel_f = os.path.relpath(f, base_dir)
        status = "OK" if len(errs) == 0 and len(warns) == 0 else f"{len(errs)} lỗi, {len(warns)} cảnh báo"
        print(f"  {rel_f}: {status}")
        for e in errs:
            print(f"    [LỖI] {e}")
        for w in warns:
            print(f"    [CẢNH BÁO] {w}")

    print(f"\nTổng kết: {total_errors} lỗi, {total_warnings} cảnh báo.")
    if total_errors > 0:
        sys.exit(1)
