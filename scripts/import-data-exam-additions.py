"""Import new Drive banks without replacing existing questions or answer keys."""
import argparse
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / 'raw_materials/xu-ly-du-lieu/exam'
HEADING = re.compile(r'^#{2,6}\s+(?:Đáp án\s+)?(B\d+-T[NL]-\d+)\s*$')


def display_payloads(markdown):
    """Make actual JSON data readable without changing the original source text."""
    result, fence = [], False
    decoder = json.JSONDecoder()
    for line in markdown.splitlines():
        if line.startswith('```'):
            fence = not fence
            result.append(line)
            continue
        if fence:
            result.append(line)
            continue
        pieces = re.split(r'(`[^`]*`)', line)
        for index in range(0, len(pieces), 2):
            text, cursor, output = pieces[index], 0, ''
            while cursor < len(text):
                start = text.find('{', cursor)
                if start < 0:
                    output += text[cursor:]
                    break
                try:
                    obj, end = decoder.raw_decode(text[start:])
                except ValueError:
                    output += text[cursor:start + 1]
                    cursor = start + 1
                    continue
                if not isinstance(obj, dict):
                    output += text[cursor:start + 1]
                    cursor = start + 1
                    continue
                raw = text[start:start + end]
                prefix, suffix = text[:start].strip(), text[start + end:].strip()
                if not prefix and not suffix:
                    output = '\n```json\n' + json.dumps(obj, ensure_ascii=False, indent=2) + '\n```\n'
                    cursor = len(text)
                elif re.fullmatch(r'\d+\.', prefix) and not suffix:
                    output = '\nJSON ' + prefix[:-1] + ':\n\n```json\n' + json.dumps(obj, ensure_ascii=False, indent=2) + '\n```\n'
                    cursor = len(text)
                else:
                    output += text[cursor:start] + '`' + raw + '`'
                    cursor = start + end
            pieces[index] = output
        result.append(''.join(pieces))
    return '\n'.join(result)


def sections(text):
    headings, offset, fence = [], 0, False
    for line in text.splitlines(keepends=True):
        if line.startswith('```'):
            fence = not fence
        if not fence and re.match(r'^#{1,6} ', line):
            headings.append((offset, offset + len(line), line.strip()))
        offset += len(line)
    result = {}
    for index, (_, end, heading) in enumerate(headings):
        match = HEADING.fullmatch(heading)
        if not match:
            continue
        identifier = match[1]
        assert identifier not in result, identifier
        stop = headings[index + 1][0] if index + 1 < len(headings) else len(text)
        result[identifier] = re.sub(r'\n---\s*$', '', text[end:stop].strip()).strip()
    return result


def clean_answer(text):
    """Keep substantive answers, removing scoring and authoring metadata only."""
    text = re.split(r'^\*\*Kỹ năng:', text, maxsplit=1, flags=re.M)[0]
    lines, output, fence, grading = text.splitlines(), [], False, False
    for line in lines:
        if not fence and re.match(r'^\*\*(?:Chấm|Mức |Thời gian|Nguồn)', line):
            grading = True
        if grading and re.match(r'^\*\*(?:Hiểu nhầm cần sửa|Lời giải)', line):
            grading = False
        if not grading:
            output.append(line)
        if line.startswith('```'):
            fence = not fence
    result = '\n'.join(output).strip()
    result = re.sub(r'^\*\*Đáp án tối thiểu (?:được )?chấp nhận:\*\*\s*', '', result)
    result = re.sub(r'^\*\*(?:Lời giải|Hiểu nhầm cần sửa):\*\*\s*', '', result, flags=re.M)
    result = result.replace('language: str không có giá trị mặc định', '`language: str` không có giá trị mặc định')
    result = result.replace('R13 chỉ ra bản đầy đủ có id cho từng đánh giá.', 'Bảng đầy đủ có cột id cho từng đánh giá.')
    result = result.replace('Lab dùng mixed/[]/und cho rỗng/vô nghĩa;', 'Quy ước của bài dùng `mixed`, danh sách rỗng và `und` cho văn bản rỗng hoặc vô nghĩa.')
    return re.sub(r'\n{3,}', '\n\n', result).strip()


def import_bank(number, question_file, answer_file):
    questions = sections((BASE / 'source' / question_file).read_text(encoding='utf-8'))
    answers = sections((BASE / 'source' / answer_file).read_text(encoding='utf-8'))
    assert len(questions) == 90 and questions.keys() == answers.keys(), number
    rows = []
    for identifier, body in questions.items():
        fences = [(m.start(), m.end()) for m in re.finditer(r'^```[^\n]*\n.*?^```\s*$', body, re.M | re.S)]
        options = [m for m in re.finditer(r'^(?:\*\*)?([A-D])[.)](?:\*\*)?[ \t]+', body, re.M)
                   if not any(start <= m.start() < end for start, end in fences)]
        kind = 'quiz' if '-TN-' in identifier else 'essay'
        assert [m[1] for m in options] == (list('ABCD') if kind == 'quiz' else []), identifier
        key = re.search(r'\*\*Đáp án:\s*([A-D])[.\s]', answers[identifier]) if kind == 'quiz' else None
        assert kind == 'essay' or key, identifier
        choices = [{'key': match[1], 'markdown': body[match.end():options[i + 1].start() if i + 1 < len(options) else len(body)].strip()}
                   for i, match in enumerate(options)]
        rows.append({
            'id': identifier, 'kind': kind, 'group': 'core',
            'promptMarkdown': body[:options[0].start()].strip() if options else body,
            'options': choices, 'correctKey': key[1] if key else None,
            'answerMarkdown': clean_answer(answers[identifier]),
            'source': {'questionFile': question_file, 'answerFile': answer_file,
                       'questionSha256': hashlib.sha256(body.encode()).hexdigest(),
                       'answerSha256': hashlib.sha256(answers[identifier].encode()).hexdigest()},
        })
        formatted = display_payloads(rows[-1]['promptMarkdown'])
        if formatted != rows[-1]['promptMarkdown']:
            rows[-1]['displayPromptMarkdown'] = formatted
        if identifier == 'B11-TN-059':
            rows[-1]['promptContextMarkdown'] = 'Đã có `import re`.'
        if identifier == 'B10-TN-040':
            rows[-1]['promptContextMarkdown'] = 'Cột `rv["date"]` đã có kiểu datetime, không thiếu và không có thành phần giờ.'
    title=(BASE / 'source' / question_file).read_text(encoding='utf-8').splitlines()[0].lstrip('# ')
    return {'lesson': str(number), 'sourceTitle': title, 'questions': rows}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--inventory', type=Path, required=True)
    args = parser.parse_args()
    inventory = json.loads(args.inventory.read_text(encoding='utf-8'))
    manifest = {'version': 1, 'folderId': '1OXMdS5xJ57Shd4UrBnpuQz0sLjmyqrA8', 'checkedOn': '2026-11-06', 'lessons': []}
    for number, qfile, title in [
        (10, 'B10_CHI_DE.md', 'Kiểm tra và làm sạch dữ liệu Airbnb'),
        (11, 'B11_BO_CAU_HOI.md', 'Xử lý văn bản và kiểm chứng đầu ra mô hình ngôn ngữ'),
    ]:
        afile = f'B{number}_DAP_AN.md'
        bank = import_bank(number, qfile, afile)
        bank['title'] = title
        (BASE / f'banks/bai-{number}.json').write_text(json.dumps(bank, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        files = []
        remote_files = next(x['files'] for x in inventory if int(x['lesson']) == number)
        for name in [qfile, afile]:
            remote = next(x for x in remote_files if x['title'] == name)
            data = (BASE / 'source' / name).read_bytes()
            assert len(data) == int(remote['size']), (name, len(data), remote['size'])
            files.append({'file': name, 'id': remote['id'], 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest(), 'url': remote['url']})
        manifest['lessons'].append({'lesson': str(number), 'title': title, 'files': files,
                                    'sourceQuestionIds': list(sections((BASE / 'source' / qfile).read_text(encoding='utf-8'))),
                                    'quiz': 60, 'essay': 30})
    (BASE / 'additions-20261106.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print('Imported 180 distinct questions: 120 quiz and 60 essays')
