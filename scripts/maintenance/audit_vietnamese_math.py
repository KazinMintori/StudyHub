import os
import re
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

VN_CHARS = (
    "àáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđ"
    "ÀÁẢÃẠĂẰẮẲẴẶÂẦẤẨẪẬÈÉẺẼẸÊỀẾỂỄỆÌÍỈĨỊÒÓỎÕỌÔỒỐỔỖỘƠỜỚỞỠỢÙÚỦŨỤƯỪỨỬỮỰỲÝỶỸỴĐ"
)
VN_SET = set(VN_CHARS)
VN_REGEX = re.compile(f"[{re.escape(VN_CHARS)}]")

def audit_markdown(text):
    results = []
    # Strip fenced code blocks
    lines = text.split('\n')
    clean_lines = []
    in_code = False
    for line in lines:
        if line.strip().startswith('```'):
            in_code = not in_code
            clean_lines.append('')
            continue
        if in_code:
            clean_lines.append('')
        else:
            clean_lines.append(line)

    clean_text = '\n'.join(clean_lines)

    # Strip inline code spans `...`
    clean_text = re.sub(r'`[^`\n]+`', lambda m: ' ' * len(m.group(0)), clean_text)

    # 1. Match display math $$ ... $$
    # KaTeX/MathJax display math: $$...$$
    for m in re.finditer(r'\$\$([\s\S]*?)\$\$', clean_text):
        content = m.group(1)
        chars = VN_SET.intersection(content)
        if chars:
            line_no = clean_text[:m.start()].count('\n') + 1
            results.append({
                'line': line_no,
                'type': 'display',
                'content': content.strip(),
                'chars': ''.join(sorted(chars))
            })

    # Replace display math with spaces of same length
    no_display = re.sub(r'\$\$([\s\S]*?)\$\$', lambda m: ' ' * len(m.group(0)), clean_text)

    # 2. Match inline math $ ... $ (excluding escaped \$ and currency $10)
    for m in re.finditer(r'(?<!\\)\$(?!\$)([^\$\n]+?)(?<!\\)\$', no_display):
        content = m.group(1)
        chars = VN_SET.intersection(content)
        if chars:
            line_no = no_display[:m.start()].count('\n') + 1
            results.append({
                'line': line_no,
                'type': 'inline',
                'content': content.strip(),
                'chars': ''.join(sorted(chars))
            })

    return results

def audit_js_file(text):
    results = []
    # In JS/MJS, ignore ${...} template expressions
    # Find all string literals (single quote, double quote, backtick)
    # Check if string contains math $$...$$ or $...$
    lines = text.split('\n')
    for line_idx, line in enumerate(lines, 1):
        # Remove ${...} from line so it doesn't look like $
        sanitized = re.sub(r'\$\{[^}]*\}', '', line)
        # Check display math in line
        # If line has $...$
        # Match display
        for m in re.finditer(r'\$\$([\s\S]*?)\$\$', sanitized):
            content = m.group(1)
            chars = VN_SET.intersection(content)
            if chars:
                results.append({'line': line_idx, 'type': 'display', 'content': content.strip(), 'chars': ''.join(sorted(chars))})
        # Mask display
        sanitized_no_disp = re.sub(r'\$\$[\s\S]*?\$\$', '', sanitized)
        # Match inline
        for m in re.finditer(r'(?<!\\)\$(?!\$)([^\$\n]+?)(?<!\\)\$', sanitized_no_disp):
            content = m.group(1)
            chars = VN_SET.intersection(content)
            if chars:
                results.append({'line': line_idx, 'type': 'inline', 'content': content.strip(), 'chars': ''.join(sorted(chars))})

    return results

def audit_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            text = f.read()
    except Exception:
        return []

    if filepath.endswith('.md'):
        return audit_markdown(text)
    elif filepath.endswith(('.mjs', '.js', '.vue')):
        return audit_js_file(text)
    return []

def main():
    target_dirs = ["docs", "raw_materials"]
    found_files = {}
    total_issues = 0

    for d in target_dirs:
        for root, dirs, files in os.walk(d):
            # prune ignored directories
            dirs[:] = [sub for sub in dirs if sub not in ['.git', 'node_modules', 'cache', 'dist']]
            for f in files:
                if f.endswith((".md", ".mjs", ".vue")):
                    fpath = os.path.join(root, f).replace("\\", "/")
                    res = audit_file(fpath)
                    if res:
                        found_files[fpath] = res
                        total_issues += len(res)

    print(f"Total files with VN in math: {len(found_files)}, total issues: {total_issues}")

    with open("scripts/maintenance/vietnamese_math_issues.json", "w", encoding="utf-8") as out:
        json.dump(found_files, out, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()
