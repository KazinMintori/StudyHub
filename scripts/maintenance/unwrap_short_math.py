import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

IGNORE_DIRS = {'.git', 'node_modules', '.vitepress/cache', '.vitepress/dist', 'brain', 'qa'}

def unwrap_short_aligned(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_crlf = '\r\n' in content
    text = content.replace('\r\n', '\n')
    
    modified = False

    def replace_block(match):
        nonlocal modified
        full_block = match.group(0)
        inner = match.group(1).strip()
        
        # Never touch complex environments
        if any(env in inner for env in ['matrix', 'cases', 'array', 'split', 'gather', '\\text']):
            return full_block
            
        lines = [l.strip() for l in inner.split(r'\\') if l.strip()]
        
        # Only 2 or 3 lines in an equality chain
        if not (2 <= len(lines) <= 3):
            return full_block
            
        # Check if line 0 has relation and following lines start with &= or &\le or &\ge or &\approx
        valid_continuation = all(
            l.startswith('&=') or l.startswith(r'&\le') or l.startswith(r'&\ge') or l.startswith(r'&\approx')
            for l in lines[1:]
        )
        if not (('=' in lines[0] or '<' in lines[0] or '>' in lines[0] or r'\le' in lines[0] or r'\ge' in lines[0]) and valid_continuation):
            return full_block

        # Build unwrapped single line
        parts = []
        first = lines[0].replace('&=', '=').replace(r'&\le', r'\le').replace(r'&\ge', r'\ge').replace(r'&\approx', r'\approx')
        first = re.sub(r'^\s*&', '', first)
        parts.append(first.strip())
        
        for l in lines[1:]:
            cleaned = re.sub(r'^\s*&=\s*', '= ', l)
            cleaned = re.sub(r'^\s*&\\le\s*', r'\\le ', cleaned)
            cleaned = re.sub(r'^\s*&\\ge\s*', r'\\ge ', cleaned)
            cleaned = re.sub(r'^\s*&\\approx\s*', r'\\approx ', cleaned)
            cleaned = re.sub(r'^\s*&', '', cleaned)
            parts.append(cleaned.strip())
            
        unwrapped = ' '.join(parts)
        unwrapped = re.sub(r'\s*=\s*', ' = ', unwrapped)
        unwrapped = re.sub(r'\s*\\le\s*', r' \\le ', unwrapped)
        unwrapped = re.sub(r'\s*\\ge\s*', r' \\ge ', unwrapped)
        unwrapped = re.sub(r'\s*\\approx\s*', r' \\approx ', unwrapped)
        
        # Max length threshold: 65 chars
        if len(unwrapped) <= 65 and '\n' not in unwrapped:
            modified = True
            return f"$$\n{unwrapped}\n$$"
            
        return full_block

    pattern = re.compile(r'\$\$\s*\\begin\{aligned\}(.*?)\\end\{aligned\}\s*\$\$', re.DOTALL)
    new_text = pattern.sub(replace_block, text)

    if modified:
        if original_crlf:
            new_text = new_text.replace('\n', '\r\n')
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_text)
        return True
    return False

def main():
    target_dirs = ['./docs', './raw_materials']
    count = 0
    for t_dir in target_dirs:
        for root, dirs, files in os.walk(t_dir):
            dirs[:] = [d for d in dirs if d not in IGNORE_DIRS and not d.startswith('.')]
            for f in sorted(files):
                if f.endswith('.md'):
                    path = os.path.join(root, f).replace('\\', '/')
                    if unwrap_short_aligned(path):
                        count += 1
                        print(f"Updated: {path}")

    print(f"\nTotal files updated: {count}")

if __name__ == '__main__':
    main()
