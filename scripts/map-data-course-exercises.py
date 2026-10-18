"""Link each numbered IAI slide exercise to one stable in-chapter anchor."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FOLDER = ROOT / 'raw_materials/xu-ly-du-lieu'

MAPPING = {
    3: ('bai-03-numpy', {i: i for i in range(1, 7)}),
    4: ('bai-04-lam-quen-pandas', {i: i for i in range(1, 6)}),
    6: ('bai-06-ket-noi-truy-xuat-du-lieu', {i: i for i in range(1, 4)}),
    7: ('bai-10-lam-sach-du-lieu', {i: i for i in range(1, 4)}),
    8: ('bai-08-du-lieu-thoi-gian', {i: i for i in range(1, 4)}),
    10: ('bai-10-lam-sach-du-lieu', {1: 4, 2: 5, 3: 6}),
}
EXTRA = {
    (5, 1): ('bai-04-lam-quen-pandas', 6),
    (5, 2): ('bai-04-lam-quen-pandas', 7),
    (5, 3): ('bai-10-tong-hop-theo-nhom', 1),
    (5, 4): ('bai-08-ghep-bang-chuyen-dang', 1),
}


def main():
    inventory = json.loads((FOLDER / 'source-inventory.json').read_text(encoding='utf-8'))
    mapped = []
    for record in inventory['records']:
        if record['source'] != 'iai':
            continue
        lecture = record['lecture']
        for exercise in record['exercises']:
            number = int(re.search(r'Bài tập\s+(\d+)', exercise['title'])[1])
            if (lecture, number) in EXTRA:
                slug, target_number = EXTRA[(lecture, number)]
            else:
                slug, lookup = MAPPING[lecture]
                target_number = lookup[number]
            notes = ROOT / 'docs/xu-ly-du-lieu/bai-giang' / (slug + '.md')
            text = notes.read_text(encoding='utf-8')
            target = re.search(r'^::: exercise\s+((?:Bài tập\s+)?' + str(target_number) + r'(?=[.:\s]).*)$', text, re.M)
            assert target, f'Missing destination for IAI {lecture}/{number}: {notes}'
            anchor = f'iai-{lecture:02}-bai-{number}'
            marker = f'<span id="{anchor}"></span>'
            if marker not in text:
                text = text[:target.start()] + marker + '\n\n' + text[target.start():]
                notes.write_text(text, encoding='utf-8')
            mapped.append({'sourceLecture': lecture, 'sourceExercise': number, 'sourceTitle': exercise['title'],
                           'sourceUrl': record['url'] + ('#' + exercise['anchor'] if exercise['anchor'] else ''),
                           'lesson': slug, 'destinationTitle': target[1],
                           'destinationUrl': f'/xu-ly-du-lieu/bai-giang/{slug}.html#{anchor}'})
    assert len(mapped) == 27
    (FOLDER / 'exercise-map.json').write_text(json.dumps(mapped, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print('Mapped all 27 numbered IAI slide exercises to stable chapter anchors')


if __name__ == '__main__':
    main()
