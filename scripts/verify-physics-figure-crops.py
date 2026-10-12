"""Check excessive exterior white margins on newly prepared source figures.

This checks crop framing only. It does not verify labels, topology or source
completeness; those require the separate visual source review.
"""
from pathlib import Path
import json,sys
from PIL import Image,ImageChops
root=Path(__file__).resolve().parents[1]
chapters=sys.argv[1:] or ['26']
results=[];failures=[]
for chapter in chapters:
    folder=root/f'docs/vat-ly-2/bai-giang/img/young-{chapter}'
    for p in sorted(folder.glob('*.png')):
        im=Image.open(p).convert('RGB')
        difference=ImageChops.difference(im,Image.new('RGB',im.size,'white'))
        bounds=difference.getbbox()
        assert bounds,f'Empty figure: {p.name}'
        x0,y0,x1,y1=bounds
        margins=[x0,y0,im.width-x1,im.height-y1]
        item={'chapter':chapter,'file':p.name,'pixels':list(im.size),'outerWhiteMargins':margins}
        results.append(item)
        if max(margins)>24:failures.append(item)
qa=root/'qa/physics';qa.mkdir(parents=True,exist_ok=True)
(qa/'figure-crop-framing.json').write_text(json.dumps({'scope':'Exterior whitespace only; visual source review required separately','results':results,'failures':failures},indent=2)+'\n',encoding='utf8')
assert not failures,json.dumps(failures,ensure_ascii=False)
print(f'Passed exterior crop-framing check for {len(results)} PNG figures.')
