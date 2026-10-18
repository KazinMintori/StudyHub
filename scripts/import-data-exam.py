"""Import every identified question and answer without rewriting its source text."""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'raw_materials/xu-ly-du-lieu/exam/source'
OUT = ROOT / 'raw_materials/xu-ly-du-lieu/exam/banks'
OUT.mkdir(parents=True, exist_ok=True)
HEADING = re.compile(r'^(#{2,5})\s+(B\d+-(?:MR|R)?\d+)\b([^\n]*)$', re.M)
OPTION = re.compile(r'^(?:\*\*)?([A-D])[.)](?:\*\*)?[ \t]+', re.M)


def sections(text):
    result = {}
    fence = None
    headers = []
    offset = 0
    for line in text.splitlines(keepends=True):
        boundary = re.match(r'^\s{0,3}(`{3,}|~{3,})(.*)', line)
        if boundary:
            if fence and boundary[1][0] == fence[0] and len(boundary[1]) >= len(fence) and not boundary[2].strip():
                fence = None
            elif not fence:
                fence = boundary[1]
        elif not fence and re.match(r'^#{1,6}\s', line):
            headers.append((offset, offset + len(line), line.strip()))
        offset += len(line)
    for index, (start, end, label) in enumerate(headers):
        match = HEADING.fullmatch(label)
        if not match:
            continue
        identifier = match[2]
        assert identifier not in result, identifier
        boundary = headers[index + 1][0] if index + 1 < len(headers) else len(text)
        body = text[end:boundary].strip()
        result[identifier] = {'body': body, 'suffix': match[3], 'line': text[:start].count('\n') + 1}
    return result


records = []
for number in range(1, 9):
    question_file = next(SOURCE.glob(f'Bai{number}_*cau_hoi.md'))
    answer_file = next(SOURCE.glob(f'Bai{number}_Dap_an*.md'))
    qtext, atext = [p.read_text(encoding='utf-8') for p in [question_file, answer_file]]
    questions, answers = sections(qtext), sections(atext)
    expected = int(re.search(r'_(\d+)_cau_hoi', question_file.name)[1])
    assert len(questions) == expected, (number, len(questions), expected)
    assert questions.keys() == answers.keys(), (number, questions.keys() ^ answers.keys())
    rows = []
    for identifier, section in questions.items():
        body = section['body']
        # Only labels outside code fences are answer alternatives.
        fences = [(m.start(), m.end()) for m in re.finditer(r'^```[^\n]*\n.*?^```\s*$', body, re.M | re.S)]
        options = [m for m in OPTION.finditer(body) if not any(a <= m.start() < b for a, b in fences)]
        table_options = list(re.finditer(r'^\|\s*([A-D])\s*\|([^\n]+)\|\s*$', body, re.M))
        if not options and [m[1] for m in table_options] == list('ABCD'):
            table_start = body.rfind('\n\n', 0, table_options[0].start()) + 2
            table_header = body[table_start:table_options[0].start()].splitlines()[0]
            labels = [v.strip() for v in table_header.strip('| ').split('|')][1:]
        else:
            table_options = []
        letters = [m[1] for m in options]
        assert not letters or letters == list('ABCD'), (identifier, letters)
        kind = 'quiz' if options or table_options else 'essay'
        answer = answers[identifier]
        answer_mark = re.search(r'—\s*([A-D])\b', answer['suffix'])
        if not answer_mark:
            answer_mark = re.search(r'^\*\*(?:Đáp án[:\s]+)?([A-D])(?:[.\s]|\*\*)', answer['body'], re.M)
        if not answer_mark:
            answer_mark = re.search(r'\b([A-D])\s+đúng\b', answer['body'])
        key = answer_mark[1] if answer_mark else None
        assert kind == 'essay' or key in list('ABCD'), (identifier, answer['body'][:250])
        choices = []
        for option in table_options:
            values = [v.strip() for v in option[2].split('|')]
            assert len(values) == len(labels), identifier
            markdown = '\n\n'.join(f'{label}: {value}' for label, value in zip(labels, values))
            choices.append({'key': option[1], 'markdown': markdown})
        for i, option in enumerate(options):
            end = options[i + 1].start() if i + 1 < len(options) else len(body)
            choices.append({'key': option[1], 'markdown': body[option.end():end].strip()})
        prompt = body[:options[0].start()].strip() if options else body[:table_start].strip() if table_options else body
        rows.append({
            'id': identifier, 'kind': kind,
            'group': 'regex' if re.search(r'-R\d', identifier) else 'extension' if '-MR' in identifier else 'core',
            'promptMarkdown': prompt, 'options': choices, 'correctKey': key if kind == 'quiz' else None,
            'answerMarkdown': answer['body'],
            'source': {'questionFile': question_file.name, 'questionLine': section['line'],
                       'answerFile': answer_file.name, 'answerLine': answer['line'],
                       'questionSha256': hashlib.sha256(body.encode()).hexdigest(),
                       'answerSha256': hashlib.sha256(answer['body'].encode()).hexdigest()},
        })
    bank = {'lesson': f'{number:02d}', 'sourceTitle': qtext.splitlines()[0].lstrip('# '),
            'questions': rows}
    target = OUT / f'bai-{number:02d}.json'
    target.write_text(json.dumps(bank, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    records.append({'lesson': bank['lesson'], 'questions': len(rows), 'quiz': sum(q['kind']=='quiz' for q in rows),
                    'essay': sum(q['kind']=='essay' for q in rows), 'sourceQuestionIds': list(questions),
                    'importedQuestionIds': [q['id'] for q in rows]})
(OUT.parent/'coverage.json').write_text(json.dumps(records, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps([{k:v for k,v in r.items() if not k.endswith('Ids')} for r in records], ensure_ascii=False, indent=2))
