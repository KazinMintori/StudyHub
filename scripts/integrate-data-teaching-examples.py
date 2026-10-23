"""Render verified Python examples beside their related lecture sections."""
import argparse
import hashlib
import html
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SOURCES = ROOT / 'raw_materials/xu-ly-du-lieu/worked-examples'
NOTES = ROOT / 'docs/xu-ly-du-lieu/bai-giang'
BLOCK = re.compile(r'\n<!-- worked-example:? ([\w-]+) -->\n.*?\n<!-- /worked-example -->\n', re.S)


def cell(value):
    if value is None:
        return '(thiếu)'
    if isinstance(value, bool):
        return '`True`' if value else '`False`'
    if isinstance(value, (list, dict)):
        value = json.dumps(value, ensure_ascii=False)
    text = html.escape(str(value), quote=False)
    for character in '|$`*_[]{}~\\':
        text = text.replace(character, f'&#{ord(character)};')
    return text.replace('\r', '').replace('\n', '<br>')


def table(output):
    columns, rows = output['columns'], output['rows']
    assert columns and all(len(row) == len(columns) for row in rows)
    content = '\n'.join([
        '| ' + ' | '.join(map(cell, columns)) + ' |',
        '| ' + ' | '.join('---' for _ in columns) + ' |',
        *('| ' + ' | '.join(map(cell, row)) + ' |' for row in rows),
    ])
    size = ' data-worked-table-wide' if len(columns) > 3 else ''
    return f'<div class="data-worked-table{size}">\n\n{content}\n\n</div>'


def render(section, result):
    code = section['code'].rstrip()
    assert result['status'] == 'passed', section['id']
    assert hashlib.sha256(section['code'].encode()).hexdigest() == result['codeSha256'], section['id']
    parts = [f'<!-- worked-example {section["id"]} -->',
             f'::: example {section["title"]}', section['purpose'],
             '```python\n' + code + '\n```', 'Kết quả khi chạy đoạn mã trên:']
    missing = False
    outputs = []
    for output in result['outputs']:
        if output['kind'] == 'text':
            text = output['text'].replace('\r', '')
            if outputs and outputs[-1]['kind'] == 'text':
                outputs[-1]['text'] += text
            else:
                outputs.append({'kind': 'text', 'text': text})
        else:
            outputs.append(output)
    for output in outputs:
        if output['kind'] == 'table':
            parts.append(table(output))
            missing |= any(None in row for row in output['rows'])
        elif output['kind'] == 'text' and output['text'].strip():
            text = output['text'].replace('\r', '').rstrip()
            # Text output is literal, never parsed as Markdown or Vue syntax.
            assert '```' not in text
            parts.append('```text\n' + text + '\n```')
    if missing:
        parts.append('Ô ghi “(thiếu)” biểu thị giá trị chưa được cung cấp hoặc chưa xác định.')
    for figure in result.get('assets', []):
        parts.append(f'![{section["title"]}]({figure})')
    if section.get('illustration'):
        parts.append(f'![{section["illustrationAlt"]}]({section["illustration"]})')
    parts.extend(section['explanation'])
    parts.extend([':::', '<!-- /worked-example -->'])
    return '\n\n'.join(parts) + '\n'


def integrate(source, original, results):
    clean = BLOCK.sub('', original)
    grouped = {}
    for section in source['sections']:
        grouped.setdefault(section['anchor'], []).append(section)
    edits = []
    lines = clean.splitlines(keepends=True)
    positions, offset = [], 0
    fence = False
    for line in lines:
        if re.match(r'^\s*(```|~~~)', line):
            fence = not fence
        if not fence and re.match(r'^#{2,6} ', line):
            positions.append((offset, line.rstrip('\r\n')))
        offset += len(line)
    for anchor, sections in grouped.items():
        matches = [i for i, (_, heading) in enumerate(positions) if heading == anchor]
        assert len(matches) == 1, (source['slug'], anchor, matches)
        index = matches[0]
        end = positions[index + 1][0] if index + 1 < len(positions) else len(clean)
        # Notes and exercises are separate tabs. Never cross their wrapper boundary.
        wrapper = clean.find('</div>', positions[index][0], end)
        if wrapper >= 0:
            end = wrapper
        block = '\n' + '\n'.join(render(s, results[s['id']]) for s in sections) + '\n'
        edits.append((end, block))
    for at, block in sorted(edits, reverse=True):
        clean = clean[:at].rstrip() + '\n' + block + clean[at:]
    return clean


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    parser.add_argument('--results', type=Path, help='Adopt independently executed output and export captured figures')
    args = parser.parse_args()
    if args.results:
        assert not args.check, 'Review new results before checking generated content'
        verified = []
        for result in json.loads(args.results.read_text(encoding='utf-8')):
            assert result['status'] == 'passed', result['id']
            item = {key: result[key] for key in ['id', 'slug', 'codeSha256', 'status', 'stdout', 'outputs', 'warnings', 'versions']}
            item['assets'] = []
            for index, svg in enumerate(result.get('figures', []), 1):
                relative = f'img/function-examples/generated/{result["id"]}-{index}.svg'
                asset = NOTES / relative
                asset.parent.mkdir(parents=True, exist_ok=True)
                assert '<svg ' in svg and '<script' not in svg
                asset.write_text('\n'.join(line.rstrip() for line in svg.splitlines()) + '\n', encoding='utf-8', newline='\n')
                item['assets'].append(relative)
            verified.append(item)
        (SOURCES / 'verified-results.json').write_text(json.dumps(verified, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    results = {r['id']: r for r in json.loads((SOURCES / 'verified-results.json').read_text(encoding='utf-8'))}
    count = 0
    for path in sorted(SOURCES.glob('*.json')):
        if path.name == 'verified-results.json':
            continue
        source = json.loads(path.read_text(encoding='utf-8'))
        target = NOTES / (source['slug'] + '.md')
        original = target.read_text(encoding='utf-8')
        updated = integrate(source, original, results)
        if args.check:
            assert updated == original, f'Stale generated examples: {target.name}'
        else:
            target.write_text(updated, encoding='utf-8', newline='\n')
        count += len(source['sections'])
    print(f'{count} verified examples {"checked" if args.check else "rendered"}')


if __name__ == '__main__':
    main()
