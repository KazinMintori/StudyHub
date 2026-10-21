"""Import the new Drive answer files without modifying the original exam banks."""
from pathlib import Path
import hashlib,json,re

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'raw_materials/xu-ly-du-lieu/exam'
manifest=json.loads((BASE/'essay-source-manifest.json').read_text(encoding='utf-8'))
output=BASE/'essay-solutions'
output.mkdir(exist_ok=True)
total=0
for source in manifest['files']:
    path=BASE/source['path']
    data=path.read_bytes()
    assert len(data)==source['bytes'] and hashlib.sha256(data).hexdigest()==source['sha256'],path
    text=data.decode('utf-8-sig').replace('\r\n','\n').replace('\r','\n')
    heads=list(re.finditer(r'^###\s+(B\d+-(?:MR|R)?\d+)\s*$',text,re.M))
    items=[]
    for i,m in enumerate(heads):
        end=heads[i+1].start() if i+1<len(heads) else len(text)
        body=text[m.end():end].strip()
        assert body and not re.search(r'Hướng dẫn chấm|Ý cần đạt|Điểm tối đa',body,re.I),m[1]
        items.append({'id':m[1],'markdown':body})
    bank=json.loads((BASE/f'banks/bai-{source["lesson"]}.json').read_text(encoding='utf-8'))
    expected=[q['id'] for q in bank['questions'] if q['kind']=='essay']
    assert [x['id'] for x in items]==expected,(source['lesson'],expected,[x['id'] for x in items])
    result={'lesson':source['lesson'],'sourceFile':source['path'],'sourceSha256':source['sha256'],'items':items}
    (output/f'bai-{source["lesson"]}.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    total+=len(items)
    print(f'{source["lesson"]}: {len(items)} essays')
assert total==184,total
print('PASS all 184 updated essay answers mapped exactly once')
