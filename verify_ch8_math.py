import re
import os
import sys

# Set utf-8 output encoding
sys.stdout.reconfigure(encoding='utf-8')

DIR = os.path.join(os.path.dirname(__file__), 'docs/ai-nen-tang-tac-tu/bai-giang/08-mang-no-ron-va-hoc-sau')
ROOT_MD = os.path.join(os.path.dirname(__file__), 'docs/ai-nen-tang-tac-tu/bai-giang/08-mang-no-ron-va-hoc-sau.md')

def check_file(filepath):
    errors = []
    warnings = []
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    lines = content.split('\n')
    
    in_code_block = False
    in_math_block = False
    in_frontmatter = False
    frontmatter_count = 0
    
    for i, line in enumerate(lines, 1):
        stripped = line.strip()
        if stripped == '---':
            frontmatter_count += 1
            if frontmatter_count == 1:
                in_frontmatter = True
                continue
            elif frontmatter_count == 2:
                in_frontmatter = False
                continue
        if in_frontmatter:
            continue
            
        if stripped.startswith('```'):
            in_code_block = not in_code_block
            continue
        if stripped.startswith('$$'):
            in_math_block = not in_math_block
            continue
        if in_code_block or in_math_block:
            continue
            
        # Ignore comments
        if stripped.startswith('<!--'):
            continue
            
        # Clean line of inline code, inline math, URLs
        clean_line = re.sub(r'`[^`]*`', '', line)
        clean_line = re.sub(r'\$[^\$]*\$', '', clean_line)
        clean_line = re.sub(r'https?://\S+', '', clean_line)
        
        # Match ': ' followed by letter
        colon_matches = re.finditer(r':\s+([^\s\d\(\[\{])', clean_line)
        for m in colon_matches:
            char = m.group(1)
            if char.isalpha() and char.islower():
                errors.append(f"Line {i}: Lowercase letter after colon: '{m.group(0)}'")
            
        # Check forbidden phrases regarding textbook sovereignty
        forbidden = [
            "lấy từ giáo trình", "lấy từ slide", "bài tập lấy từ sách",
            "ảnh lấy từ sách", "hình trong sách", "theo sách", "sách dùng",
            "nguyên tác", "bản dịch của", "tiến độ bản dịch", "do người soạn"
        ]
        lower_line = line.lower()
        for f in forbidden:
            if f in lower_line:
                errors.append(f"Line {i}: Forbidden sovereignty violation phrase '{f}'")
                
        # Check vert
        if r'\vert{' in line or r'\Vert{' in line:
            errors.append(f"Line {i}: Forbidden \\vert{{}} or \\Vert{{}}")

    # Check display math length and breaking
    display_math_blocks = re.findall(r'\$\$(.*?)\$\$', content, re.DOTALL)
    for block in display_math_blocks:
        block_lines = [l.strip() for l in block.split('\n') if l.strip()]
        for bl in block_lines:
            if re.search(r'[+\-*/]\s*\\\\', bl):
                errors.append(f"Display math breaking at operator: {bl[:50]}")
            if re.search(r'=\s*\\\\', bl):
                errors.append(f"Display math breaking immediately after '=': {bl[:50]}")

    return errors, warnings

def main():
    target_files = []
    if os.path.exists(ROOT_MD):
        target_files.append(ROOT_MD)
    if os.path.exists(DIR):
        for f in sorted(os.listdir(DIR)):
            if f.endswith('.md'):
                target_files.append(os.path.join(DIR, f))
                
    total_errors = 0
    total_warnings = 0
    for tf in target_files:
        errs, warns = check_file(tf)
        relpath = os.path.relpath(tf, os.path.dirname(__file__))
        if errs or warns:
            print(f"=== {relpath} ===")
            for e in errs:
                print(f"  [ERROR] {e}")
                total_errors += 1
            for w in warns:
                print(f"  [WARN] {w}")
                total_warnings += 1
        else:
            print(f"OK: {relpath}")
            
    print(f"\nTotal files checked: {len(target_files)}, Errors: {total_errors}, Warnings: {total_warnings}")
    if total_errors > 0:
        sys.exit(1)

if __name__ == '__main__':
    main()
