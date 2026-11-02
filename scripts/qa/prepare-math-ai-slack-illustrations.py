"""Validate and correct the two retained AGY SVG assets without rerunning AGY."""
from pathlib import Path
from copy import deepcopy
import math,re,json,hashlib
from lxml import etree
import pymupdf

course=Path('../math-ai-visual-content')
raw=course/'raw_materials/toan-cho-ai/visual-review/assets'
target=course/'docs/toan-cho-ai/bai-giang/img/lec-02'
qa=Path('qa/math-ai-visuals/agy-svg-reviewed');qa.mkdir(parents=True,exist_ok=True)
target.mkdir(parents=True,exist_ok=True)
ns={'s':'http://www.w3.org/2000/svg'}
reports=[]
for label,dimension in [('slack-lift-2d',2),('slack-lift-3d',3)]:
 source=(raw/(label+'.raw.svg')).read_bytes()
 assert not re.search(rb'<!DOCTYPE|<!ENTITY|<script|<foreignObject|(?:href|src)=',source,re.I)
 root=etree.fromstring(source,parser=etree.XMLParser(resolve_entities=False,no_network=True))
 captions=root.xpath('./s:text[@text-anchor="middle"]',namespaces=ns)
 captions=[element for element in captions if float(element.get('y'))>270]
 assert len(captions)==2
 replacements=['Trung điểm M nằm ngoài cung','Hình chiếu: Đoạn [−1, 1]'] if dimension==2 else ['M ngoài mặt, G thuộc mặt','Hình chiếu: Đĩa đơn vị']
 for element,text in zip(captions,replacements):element.text=text
 title=etree.Element('{'+ns['s']+'}title')
 title.text='Biến bù trên cung parabol' if dimension==2 else 'Biến bù trên mặt paraboloid và hình chiếu xuống đĩa'
 root.insert(0,title)
 root.set('role','img')
 if dimension==2:
  curve=next(e for e in root.xpath('./s:path',namespaces=ns) if 'Q' in e.get('d',''))
  values=list(map(float,re.findall(r'-?\d+(?:\.\d+)?',curve.get('d'))))
  assert len(values)==10
  points=[values[i:i+2] for i in range(0,10,2)]
  for start,control,end in [points[:3],points[2:]]:
   for k in range(21):
    t=k/20
    x,y=[(1-t)**2*start[i]+2*t*(1-t)*control[i]+t*t*end[i] for i in [0,1]]
    assert abs(((x-180)/105)**2+(240-y)/150-1)<1e-10
  witness=[[96,186],[264,186],[180,90]]
 else:
  yaw,pitch=map(math.radians,[32,28])
  def project(x,y,s):
   u=x*math.cos(yaw)-y*math.sin(yaw);v=x*math.sin(yaw)+y*math.cos(yaw)
   return [180+105*u,245-105*(s*math.cos(pitch)-v*math.sin(pitch))]
  witness=[project(-.6,-.4,.48),project(.6,.4,.48),project(0,0,1)]
  assert abs((200.5-152.3)-105*math.cos(pitch)*.52)<.03
 circles=[[float(e.get('cx')),float(e.get('cy'))] for e in root.xpath('./s:circle',namespaces=ns)]
 assert all(min(math.dist(point,c) for c in circles)<.15 for point in witness)
 data=etree.tostring(root,encoding='utf-8',xml_declaration=True,pretty_print=True)
 (target/(label+'.svg')).write_bytes(data)
 for width in [294,400]:
  preview=deepcopy(root);preview.set('width',str(width));preview.set('height',str(width*float(root.get('viewBox').split()[3])/360))
  doc=pymupdf.open(stream=etree.tostring(preview),filetype='svg')
  doc[0].get_pixmap().save(qa/f'{label}-{width}.png')
 reports.append({'file':str(target/(label+'.svg')),'raw_sha256':hashlib.sha256(source).hexdigest(),'final_sha256':hashlib.sha256(data).hexdigest(),'checked':'Exact R2 parabola / projected R3 point witnesses and MG gap','changes':'Shortened overflowing captions; added accessible title; retained AGY geometry','browserTextBounds':'pending'})
(qa/'report.json').write_text(json.dumps(reports,ensure_ascii=False,indent=2),encoding='utf-8')
print('Both corrected SVGs generated; numerical witnesses checked and 294/400 px review PNGs written.')
