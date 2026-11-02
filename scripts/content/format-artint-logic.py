"""Render long logic programs as wrapping symbolic code, preserving tokens.

Input comes from the MathJax width audit. This changes presentation only, with
the original TeX retained in the local QA audit for independent comparison.
"""
from pathlib import Path
import html
import json
import re

root = Path(__file__).resolve().parents[2]
report = json.loads((root / 'qa/artint3e/math-source.json').read_text(encoding='utf-8'))
commands = dict(leftarrow='←', rightarrow='→', leftrightarrow='↔', wedge='∧', land='∧',
                vee='∨', neg='¬', forall='∀', exists='∃', mapsto='↦', longmapsto='↦',
                langle='⟨', rangle='⟩', ldots='…', dots='…', to='→', sim='∼', phi='φ',
                pi='π', times='×', implies='⇒', neq='≠', models='⊨', sigma='σ',
                mid='|', cup='∪', subseteq='⊆', **{'in':'∈'})

def symbolic(tex):
    t = re.sub(r'\\(?:begin|end)\{(?:aligned|array)\}', '', tex)
    t = re.sub(r'\\(?:mathit|mathbf|mathrm|text|mbox)\{([^{}]*)\}', r'\1', t)
    t = re.sub(r'\\(?:Big|big|left|right)\b', '', t)
    t = re.sub(r'\\(?:quad|qquad|;)\b', ' ', t)
    t = t.replace(r'\\', '\n').replace('&', '')
    t = t.replace(r'\{', '⦃').replace(r'\}', '⦄').replace(r'\_', '_')
    t = re.sub(r'_\{([^{}]+)\}', r'_\1', t)
    for key, value in commands.items():
        t = re.sub(r'\\' + key + r'(?![A-Za-z])', lambda _: value, t)
    t = t.replace('{', '').replace('}', '').replace('⦃', '{').replace('⦄', '}')
    t = t.replace('~', ' ').replace(r'\;', ' ').replace(r'\,', ' ').replace('\\ ', ' ')
    t = t.replace(r'\not⊨', '⊭')
    if '\\' in t:
        raise ValueError(f'Unconverted command: {t}')
    return t.strip()

changed = 0
for issue in report['issues']:
    if issue['kind'] not in ['inline-width', 'display-width']:
        raise ValueError(issue)
    p = root / issue['file']
    text = p.read_text(encoding='utf-8')
    tex = issue['tex']
    tag = 'code' if issue['kind'] == 'inline-width' else 'span'
    classes = 'logic-expression' + (' logic-block' if tag == 'span' else '')
    rendered = '<' + tag + ' class="' + classes + '">' + html.escape(symbolic(tex)).replace('\n', '&#10;') + '</' + tag + '>'
    if tag == 'code':
        text, count = text.replace('$' + tex + '$', rendered), text.count('$' + tex + '$')
    else:
        lines = tex.strip().splitlines()
        pattern = r'\$\$\s*' + r'\s*\n[ \t]*'.join(re.escape(line.strip()) for line in lines) + r'\s*\$\$'
        text, count = re.subn(pattern, lambda _: rendered, text)
    if count:
        p.write_text(text, encoding='utf-8')
        changed += count
print(f'Formatted {changed} long symbolic expressions as wrapping logic code.')
