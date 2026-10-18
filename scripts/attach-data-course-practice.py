"""Attach chapter practice through canonical includes and the existing exercise tab."""
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'raw_materials/xu-ly-du-lieu'
PRACTICE = SOURCE / 'practice'
NOTES = ROOT / 'docs/xu-ly-du-lieu/bai-giang'


def main():
    contract = json.loads((SOURCE / 'authoring-contract.json').read_text(encoding='utf-8'))
    extras = {'7': ['regex.md'], '9': ['visual-reading.md'], '13': ['aggregation-figure.md']}
    for entry in contract['lessons']:
        file = NOTES / (entry['slug'] + '.md')
        text = file.read_text(encoding='utf-8')
        assert 'lecture-notes-content' not in text, f'Already attached: {file}'
        match = re.match(r'^(---\s*\n.*?\n---\s*\n)(.*)$', text, re.S)
        assert match
        front, body = match.groups()
        if 'hasChapterExercises:' not in front:
            front = front.replace('lessonStatus: ready\n', 'lessonStatus: ready\nhasChapterExercises: true\n')
        refs = re.search(r'^## Tài liệu tham khảo\s*\n', body, re.M)
        assert refs, f'Missing references: {file}'
        content, references = body[:refs.start()].strip(), body[refs.end():].strip()
        headings = list(re.finditer(r'^## (.+)$', content, re.M))
        section = next((i for i, h in enumerate(headings) if re.search(r'Bài tập|Thực hành|Luyện tập', h[1], re.I)), None)
        exercises = ''
        if section is not None:
            start = headings[section].start()
            end = headings[section + 1].start() if section + 1 < len(headings) else len(content)
            exercises = content[start:end].strip()
            content = (content[:start] + content[end:]).strip()
        paths = sorted(PRACTICE.glob(f'*-chapter-{entry["chapter"]}.md'))
        paths += [PRACTICE / name for name in extras.get(entry['chapter'], [])]
        for path in paths:
            assert path.is_file()
            relative = '../../../' + path.relative_to(ROOT).as_posix()
            exercises += '\n\n<!--@include: ' + relative + '-->\n'
        assert exercises.strip(), f'No exercises: {file}'
        attribution = ''
        if paths:
            attribution = ('\n\n- IAI, [Lập trình xử lý dữ liệu, học liệu và notebook]'
                           '(https://courses.iaidev.com/programming-for-data-processing/2627-1/). '
                           'Các đề thực hành đã được biên tập cách diễn đạt và bổ sung lời giải, '
                           'giữ [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). '
                           '[Giấy phép học liệu](https://github.com/uet-iai-course/programming-for-data-processing/blob/main/LICENSE).')
        if entry['chapter'] == '7':
            attribution += ('\n- [RegexOne](https://regexone.com/), các chủ đề luyện biểu thức chính quy. '
                            '[Bộ đề và ca thử IAI](https://github.com/uet-iai-course/programming-for-data-processing/blob/main/2627-1/notebooks/lab-07-regex.ipynb).')
        reference_section = '## Tài liệu tham khảo\n\n' + references + attribution + '\n'
        output = (front + '\n<div class="lecture-notes-content">\n\n' + content + '\n\n' + reference_section +
                  '\n</div>\n\n<div class="lecture-exercises-content" aria-label="Bài tập của chương">\n\n' +
                  exercises.strip() + '\n\n' + reference_section + '\n</div>\n')
        file.write_text(output, encoding='utf-8')
        module = ROOT / 'src/content/courses/xu-ly-du-lieu/lectures' / entry['slug'] / 'lesson.mjs'
        js = 'import {lesson} from ' + json.dumps(module.as_uri()) + '; console.log(JSON.stringify(lesson))'
        result = subprocess.run(['node', '--input-type=module', '-e', js], capture_output=True, text=True, encoding='utf-8', check=True)
        lesson = json.loads(result.stdout)
        lesson['hasChapterExercises'] = True
        module.write_text('export const lesson = ' + json.dumps(lesson, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print('Attached authored exercises and practice to all 15 chapter bundles')


if __name__ == '__main__':
    main()
