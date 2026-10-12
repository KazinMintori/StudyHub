"""Normalize solution headings and list the existing reasoning without losing text."""
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
folder = root / 'raw_materials/physics/translations/chapter-21'
count = 0
for p in folder.glob('*.md'):
    text = p.read_text(encoding='utf8')
    text = text.replace('r_{\\\\\nmax}', r'r_{\max}')
    text = text.replace('h_{\\\\\nmax}', r'h_{\max}')
    text = text.replace(r't_{\mathrm{trở'+'\\\\\n'+r'về}}', r't_{\mathrm{về}}')
    p.write_text(text, encoding='utf8')
    # Remove an empty final alignment cell, without touching TeX commands.
    text = re.sub(r'&(?=\\\\\n)', '', text)
    text = text.replace('**Tóm tắt đề bài.**', '**Tóm tắt đề bài:**')
    text = text.replace('::: solution Lời giải chi tiết', '::: solution Chi tiết')
    def reasoning(m):
        global count
        body = m[1].strip()
        if body.startswith('- '):
            return m[0]
        # Sentences are split only after prose punctuation followed by a capital.
        # Decimal points and inline math stay intact.
        pieces = re.split(r'(?<=[.!?])\s+(?=[A-ZÀ-ỴĐ])', body)
        count += 1
        return '**Hướng đi:**\n\n' + '\n'.join('- ' + s for s in pieces) + '\n'
    text = re.sub(r'\*\*Hướng đi:\*\*\s*([^\n]+)\n', reasoning, text)
    p.write_text(text, encoding='utf8')
print('Reasoning lists formatted:', count)

# A command broken across a line can still render as letters rather than fail.
for p in folder.glob('*.md'):
    text = p.read_text(encoding='utf8')
    for m in re.finditer(r'\$\$([\s\S]*?)\$\$', text):
        for line in m[1].splitlines():
            if re.match(r'\s*(?:min|max|ell|sim|mathrm|text|theta|alpha|varphi|times|frac|sqrt|hat|vec|tau|circ|pi|sigma|rho|lambda|varepsilon|Delta)\b', line):
                print('Suspicious command:', p.name, line)
