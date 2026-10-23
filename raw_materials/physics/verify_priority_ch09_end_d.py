"""Parent review of the actual end problems 9.1–9.48.

Checks real numerical calculations, geometric identities, published solution
structure and fresh PDF crop pixels. It does not certify translation coverage
or browser layout; those are separate review steps.
"""
from pathlib import Path
import contextlib,hashlib,importlib.util,io,json,math,re,runpy
import numpy as np
from PIL import Image
import pymupdf
ROOT=Path(__file__).resolve().parents[2]
Q=ROOT/'qa/physics1-priority';Q.mkdir(parents=True,exist_ok=True)
source=ROOT/'raw_materials/physics/translations/chapter-09/11-bai-tap-001-048.md'
text=source.read_text(encoding='utf-8')
headings=list(re.finditer(r'^### 9\.(\d+)\s.+$',text,re.M))
assert [int(m[1]) for m in headings]==list(range(1,49))
for i,m in enumerate(headings):
 block=text[m.end():headings[i+1].start() if i+1<len(headings) else len(text)]
 assert block.count('<details>')==block.count('</details>')==1,m[1]
 assert '<summary>Xem lời giải chi tiết</summary>' in block,m[1]
 assert '<details open' not in block
 assert '**Tóm tắt đề bài:**' in block and '**Hướng đi:**' in block,m[1]
 assert block.index('**Tóm tắt đề bài:**')<block.index('**Hướng đi:**')<block.index('**Lời giải:**'),m[1]
 assert len(block.split('<details>')[0].strip())>60,m[1]
with contextlib.redirect_stdout(io.StringIO()):
 worker=runpy.run_path(str(ROOT/'raw_materials/physics/verify_chapter09_exercises_d.py'))
assert set(worker['results'])=={f'9.{i}' for i in range(1,49)}
ledger={k:v for k,v in worker['results'].items()}
def close(a,b):assert math.isclose(a,b,rel_tol=1e-10,abs_tol=1e-10),(a,b)
# Independent derivative/integral checks of time-varying angular motion.
for t in [0,.5,2,4.2]:
 h=1e-5
 close((2.75+1.5*(t+h)**2-(2.75+1.5*(t-h)**2))/(2*h),3*t)
theta=lambda t:250*t-20*t*t-1.5*t**3
stop=worker['t_6a'];close(250-40*stop-4.5*stop**2,0)
close(theta(stop)/(2*math.pi),worker['rev_6c'])
assert 0<worker['t_26_g']<8
close(.2*(400-50*worker['t_26_g'])**2,9.8)
# Symbolic claims previously represented only by strings are checked by
# explicit distances and energy equality over nontrivial parameter choices.
for m,L in [(.3,.7),(2,3),(7,.08)]:
 positions=np.array([0,L/2,L])
 Ia=sum(m*(positions-L/2)**2);Ib=sum(m*(positions-L/4)**2)
 close(Ia,.5*m*L*L);close(Ib,11*m*L*L/16)
 close(Ib,Ia+3*m*(L/4)**2)
for M,R,w in [(2,.3,4),(5,2,.7),(.08,.04,20)]:
 Is=.4*M*R*R;Id=.5*M*R*R
 close(Id/Is,1.25)
 Ih=2*M*R*R/3;wh=math.sqrt(3/5)*w
 close(.5*Ih*wh**2,.5*Is*w**2)
 I=.5*M*R*R
 close((.5*I*w*w)/(.5*M*(R*w)**2),.5)
# V-bending: element distance from the normal axis equals its position along
# each arm for both the straight and folded geometries.
for angle in [math.pi/3,math.pi/2,math.pi]:
 s=np.linspace(0,.3,10001)
 x=s*np.cos(angle/2);y=s*np.sin(angle/2)
 close(2*np.trapezoid((.4/.6)*(x*x+y*y),s),.01200000006)
# All figure pixels must match an independently rerendered source crop.
asset=ROOT/'scripts/prepare-physics1-09-exercises-d-assets.py'
spec=importlib.util.spec_from_file_location('parent_ch09_d_assets',asset)
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
images=[]
with pymupdf.open(ROOT/'raw_materials/physics/source/young-freedman-15.pdf') as pdf:
 for stem,(page,rect) in module.CROPS.items():
  file=ROOT/f'docs/vat-ly-1/bai-giang/img/young-09/{stem}.png'
  pix=pdf[page-1].get_pixmap(matrix=pymupdf.Matrix(module.SCALE,module.SCALE),clip=pymupdf.Rect(rect),alpha=False)
  with Image.open(file) as saved:
   assert saved.convert('RGB').size==(pix.width,pix.height)
   assert saved.convert('RGB').tobytes()==pix.samples,stem
  images.append(dict(stem=stem,pdfPage=page,bounds=rect,sha256=hashlib.sha256(file.read_bytes()).hexdigest(),rgbMatches=True))
report=dict(status='passed',scope='Actual numerical results, geometric identities, solution structure and fresh crop RGB; source prose and browser reviewed separately',prompts=48,closedSolutions=48,symbolicCases='Numerically checked with explicit geometry/energy',results=ledger,images=images)
(Q/'ch09-end-d-verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(dict(status=report['status'],prompts=48,closedSolutions=48,crops=len(images))))
