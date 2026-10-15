import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

IGNORE_DIRS = {'.git', 'node_modules', '.vitepress/cache', '.vitepress/dist', 'brain', 'qa'}

broken_ops_issues = []
misaligned_eq_issues = []
unnecessary_aligned_issues = []
break_after_eq_issues = []

def mask_nested_environments(text):
    # Mask \begin{...}...\end{...}
    pattern = r'\\begin\{(?:bmatrix|pmatrix|vmatrix|matrix|cases|array)\}.*?\\end\{(?:bmatrix|pmatrix|vmatrix|matrix|cases|array)\}'
    while re.search(pattern, text, re.DOTALL):
        text = re.sub(pattern, ' __NESTED_ENV__ ', text, flags=re.DOTALL)
    # Mask subscripts like _{i=1}
    text = re.sub(r'_[{][^{}]*=[^{}]*[}]', ' __SUB_EQ__ ', text)
    # Mask \text{...}
    text = re.sub(r'\\text\{[^{}]*\}', ' __TEXT__ ', text)
    # Mask parens like (X = 1)
    text = re.sub(r'\([^(^)]*=[^(^)]*\)', ' __PAREN_EQ__ ', text)
    return text

for root, dirs, files in os.walk('.'):
    dirs[:] = [d for d in dirs if d not in IGNORE_DIRS and not d.startswith('.')]
    
    for f in sorted(files):
        if f.endswith('.md'):
            path = os.path.join(root, f).replace('\\', '/')
            if not (path.startswith('./docs/') or path.startswith('./raw_materials/')):
                continue
                
            with open(path, 'r', encoding='utf-8', errors='ignore') as fp:
                content = fp.read()
            
            for match in re.finditer(r'\$\$(.*?)\$\$', content, re.DOTALL):
                block = match.group(1)
                start_line = content[:match.start()].count('\n') + 1
                
                # Check for line break right after =
                if re.search(r'=\s*\\\\', block):
                    break_after_eq_issues.append((path, start_line, block.strip()))
                
                aligned_matches = re.finditer(r'\\begin\{aligned\}(.*?)\\end\{aligned\}', block, re.DOTALL)
                for am in aligned_matches:
                    inner = am.group(1).strip()
                    masked_inner = mask_nested_environments(inner)
                    
                    raw_lines = [l.strip() for l in masked_inner.split(r'\\')]
                    lines = [l for l in raw_lines if l and not l.isspace()]
                    
                    # Check 1: broken operator before =
                    for l_idx, line in enumerate(lines):
                        if l_idx > 0:
                            if re.match(r'^\s*&?\s*[\+\-\u00b1\u2213\u00d7\u00b7]', line):
                                if not re.search(r'[=<>]|\\le|\\ge|\\approx|\\sim|\\equiv', line):
                                    broken_ops_issues.append((path, start_line, line, inner))
                                    break
                    
                    # Check 2: misaligned '=' signs
                    for l_idx, line in enumerate(lines):
                        # Detect & placed inside parens, e.g. P(Y &= 2) or P(Y &\ge 1)
                        if re.search(r'\([^\)]*&[^\)]*\)', am.group(1).split('\\\\')[l_idx]):
                            misaligned_eq_issues.append((path, start_line, f"& inside parens: {am.group(1).split(r'\\\\')[l_idx].strip()}", inner))
                            break

                        if '=' in line and '&' in line:
                            eq_pos = line.find('=')
                            amp_pos = line.find('&')
                            if amp_pos > eq_pos:
                                misaligned_eq_issues.append((path, start_line, f"& after = in line: {line}", inner))
                                break
                        elif '=' in line and '&' not in line and len(lines) > 1:
                            has_other_amp = any('&' in other for other in lines)
                            if has_other_amp:
                                misaligned_eq_issues.append((path, start_line, f"missing & on line with =: {line}", inner))
                                break
                    
                    # Check 3: Short simple equations broken unnecessarily
                    clean_inner = re.sub(r'[\s&]', '', inner).replace(r'\\', '')
                    if len(lines) == 2 and len(clean_inner) < 55:
                        first_line = lines[0].strip()
                        second_line = lines[1].strip()
                        # e.g. A &= B \\ &= C or A &= B \\ C &= D
                        if first_line.endswith(',') or second_line.startswith('&='):
                            unnecessary_aligned_issues.append((path, start_line, inner, block.strip()))
                        elif first_line.startswith(r'\phi') or first_line.startswith('2d') or first_line.startswith('d\\sin'):
                            unnecessary_aligned_issues.append((path, start_line, inner, block.strip()))

print("=== 1. Broken Operators Across Lines (e.g. &+ or &- without relation) ===")
print(f"Total: {len(broken_ops_issues)}")
for path, line_no, line, block in broken_ops_issues[:20]:
    print(f"{path}:{line_no} -> {line}")

print("\n=== 2. Line break immediately after '=' (e.g. = \\\\) ===")
print(f"Total: {len(break_after_eq_issues)}")
for path, line_no, block in break_after_eq_issues[:20]:
    print(f"{path}:{line_no} -> {block[:60]}")

print("\n=== 3. Misaligned '=' Signs in Aligned Environments ===")
print(f"Total: {len(misaligned_eq_issues)}")
for path, line_no, detail, block in misaligned_eq_issues[:20]:
    print(f"{path}:{line_no} -> {detail}")

print("\n=== 4. Unnecessary Aligned on Short Equations (< 55 chars) ===")
print(f"Total: {len(unnecessary_aligned_issues)}")
for path, line_no, inner, block in unnecessary_aligned_issues[:30]:
    print(f"{path}:{line_no} -> {inner.replace(chr(10), ' ')}")
