"""Prepare licensed IAI regex exercises and retain their original public tests."""
import json
import re
import tempfile
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE_URL = 'https://github.com/uet-iai-course/programming-for-data-processing/blob/main/2627-1/notebooks/lab-07-regex.ipynb'
FOLDER = ROOT / 'raw_materials/xu-ly-du-lieu/practice'


def main():
    cache = Path(tempfile.gettempdir()) / 'studyhub-data-sources/iai-notebook-lab-07-regex.txt'
    sections = re.split(r'(?=^## Câu [0-9]+\.)', cache.read_text(encoding='utf-8'), flags=re.M)[1:]
    solutions = json.loads((FOLDER / 'regex-solutions.json').read_text(encoding='utf-8'))
    assert len(sections) == len(solutions) == 20
    markdown = ['## Thực hành biểu thức chính quy\n',
                'Mỗi bài nhận đầu vào là `str` hoặc `None`. Các chữ số trong mẫu phải thuộc ASCII, trừ phần ký tự trắng được nêu riêng. Không tự xóa khoảng trắng hay đổi hoa thường trước khi kiểm tra. Hãy giữ đúng kiểu kết quả và thử lời giải trên các trường hợp biên.\n',
                'Các bài sử dụng miền đầu vào giản lược của từng đề. Không dùng lookaround hoặc tham chiếu ngược. Với HTML, email hay URL ngoài miền đó, cần dùng bộ phân tích phù hợp.\n']
    test_program = ['"""IAI regex public tests, adapted under CC BY-NC-SA 4.0.\nSource: ' + SOURCE_URL + '\nOnly solution patterns and neutral explanations were added.\n"""\nimport re\nfrom contextlib import redirect_stdout\nfrom io import StringIO\nTOTAL = 0\n']
    ledger = []
    for section, item in zip(sections, solutions):
        title = section.splitlines()[0].removeprefix('## ')
        number = int(re.search(r'Câu (\d+)\.', title)[1])
        assert number == item['number']
        statement = section.split('### Đoạn văn đầu vào')[0].split('\n', 1)[1]
        statement = re.sub(r'\*\*5 điểm\*\*\s*', '', statement)
        statement = re.sub(r'[,;]?\s*[Nn]ộp\b.*?(?:\.(?=\s|$)|$)', '.', statement, flags=re.S)
        # All technical input/return rules precede the submission instruction.
        statement = statement.strip()
        statement = re.sub(r';\s*([a-zà-ỹ])', lambda m: '. ' + m[1].upper(), statement)
        statement = re.sub(r';\s*', '. ', statement)
        statement = re.sub(r'(?<=:)\s+([a-zà-ỹ])', lambda m: ' ' + m[1].upper(), statement)
        blocks = re.findall(r'^```python\n(.*?)^```', section, re.M | re.S)
        code = blocks[0].replace('PATTERN = r""', 'PATTERN = r"' + item['pattern'] + '"')
        code = re.sub(r'    if text is None: return (.+)', r'    if text is None:\n        return \1', code)
        tests = blocks[1]
        namespace = {}
        with redirect_stdout(StringIO()):
            exec(compile(code + '\n' + tests, f'regex-{number}', 'exec'), namespace)
        cases = len(namespace['CASES'])
        markdown.extend([f'### Regex {number}. {title.split(". ", 1)[1]}\n',
                         f'::: exercise Regex {number}\n{statement}\n:::\n',
                         '::: solution\n```python\n' + code.strip() + '\n```\n\n' + item['explanation'] + '\n:::\n'])
        test_program.extend([f'\n# Exercise {number}: {title}\n', code, '\nwith redirect_stdout(StringIO()):\n',
                             '\n'.join('    ' + line for line in tests.splitlines()), f'\nTOTAL += {cases + 1}\n'])
        ledger.append({'sourceNotebook':'lab-07-regex', 'sourceHeading':title, 'chapter':'7',
                       'destinationHeading':f'Regex {number}. {title.split(". ", 1)[1]}',
                       'status':'included', 'testCases':cases, 'passageTests':1})
    test_program.append('\nprint(f"Regex: 20 exercises, {TOTAL} original public tests passed")\n')
    (FOLDER / 'regex.md').write_text('\n'.join(markdown) + '\n', encoding='utf-8')
    (ROOT / 'scripts/verify-data-practice-regex.py').write_text(''.join(test_program), encoding='utf-8')
    (FOLDER / 'regex-ledger.json').write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print('Prepared and verified 20 regex exercises')


if __name__ == '__main__':
    main()
