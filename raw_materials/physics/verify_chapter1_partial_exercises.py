"""Independent recomputation for the82accepted chapter1 exercise units.

Scope is explicitly partial: Remaining numbered1.48–1.94 and wholechapter
publication gates are separate. Does not modify textbook, images or sources.
"""
from pathlib import Path
import json,math,re,hashlib
import numpy as np,pymupdf
ROOT=Path(__file__).resolve().parents[2]
def sha256_asset(path):
 data=path.read_bytes()
 if path.suffix.lower()in {'.md','.svg'}:data=data.replace(b'\r\n',b'\n')
 return hashlib.sha256(data).hexdigest()
def verify_numbered():
 records=[];units={}
 def ck(n,name,actual,expected,tol=1e-6):
  ok=bool(np.allclose(actual,expected,rtol=tol,atol=tol));assert ok,(n,name,actual,expected)
  row={'unit':f'1.{n}','label':name,'actual':np.asarray(actual).tolist(),'expected':np.asarray(expected).tolist(),'tolerance':tol,'passed':True};records.append(row);units.setdefault(n,[]).append(row)
 def st(n,name,value):
  assert value,(n,name);row={'unit':f'1.{n}','label':name,'passed':True};records.append(row);units.setdefault(n,[]).append(row)
 rad=math.radians
 polar=lambda r,a:np.array([r*math.cos(rad(a)),r*math.sin(rad(a))])
 direction=lambda a:math.degrees(math.atan2(a[1],a[0]))%360
 vecangle=lambda a,b:math.degrees(math.acos(np.clip(np.dot(a,b)/np.linalg.norm(a)/np.linalg.norm(b),-1,1)))
 ck(1,'mile kilometres',5280*12*.0254/1000,1.609344)
 ck(1,'kilometre feet',1000/.3048,3280.839895013123)
 ck(2,'bottle cubic inches',.473*1000/2.54**3,28.86423188799133)
 ck(3,'light time ns per foot',.3048/299792458*1e9,1.016703362163973)
 ck(4,'gold density SI',19.3*1e-3/(.01**3),19300)
 ck(5,'gigasecond years under365day convention',1e9/(365*86400),31.709791983764585)
 ck(6,'60mph inft/s',60*5280/3600,88)
 ck(6,'32ft/s2 inSI',32*.3048,9.7536)
 ck(6,'water density',1.*1e-3/.01**3,1000)
 eff=55*1.609344/3.785411784
 ck(7,'km per litre',eff,23.38390390914259,tol=1e-4)
 ck(7,'fuel litres',1500/eff,64.15,tol=.001)
 ck(7,'tank equivalents',1500/eff/45,1.426,tol=.001)
 ck(8,'magnesium micrograms per day',410*1000,410000)
 ck(8,'lysine grams in one day',12*75/1000,.9)
 ck(8,'tablet equivalents arithmetic',.003*1000/2,1.5)
 ck(8,'selenium mg per day',.000070*1000,.070)
 ck(9,'volume m3',60/19500,.003076923076923077)
 ck(9,'sphere radius metres',(3*60/19500/(4*math.pi))**(1/3),.09022827957982588)
 ck(10,'bacterium sphere volume cm3',4/3*math.pi*1e-4**3,4.188790204786391e-12)
 ck(10,'bacterium sphere area mm2',4*math.pi*1e-3**2,1.2566370614359172e-5)
 for label,actual,expected in [('area mm2',12*5.98,71.76),('width/length',5.98/12,.49833333333333335),('perimeter mm',2*(12+5.98),35.96),('difference mm',12-5.98,6.02),('length/width',12/5.98,2.0066889632107023)]:ck(11,label,actual,expected)
 ck(12,'cylinder volume mm3',math.pi*.36**2*121,49.26519935653369)
 ck(13,'year seconds',365.24*86400,31556736)
 ck(13,'pi-year percent error',abs(math.pi*1e7-365.24*86400)/(365.24*86400)*100,.44621048292848486)
 st(14,'22/7 six significant digits differ from pi',format(22/7,'.6g')!=format(math.pi,'.6g'))
 st(14,'355/113 six significant digits agree',format(355/113,'.6g')==format(math.pi,'.6g'))
 st(14,'355/113 seven significant digits agree',format(355/113,'.7g')==format(math.pi,'.7g'))
 st(14,'355/113 eight significant digits differ',format(355/113,'.8g')!=format(math.pi,'.8g'))
 ck(15,'200cm metres',200/100,2.)
 ck(15,'200mm metres',200/1000,.2)
 ck(15,'200months years',200/12,16.666666666666668)
 ck(16,'assumed population model gallons per day',330e6*2/3*1e4/20/365,301369863.01369864)
 ck(17,'assumed pile volume',1.7*.5*.2,.17)
 ck(17,'gold mass grams',1.7*.5*.2*1e6*19.3,3281000)
 ck(17,'source-price value dollars',1.7*.5*.2*1e6*19.3*40,131240000)
 air=4*500e-6*15*365*24*60
 ck(18,'cumulative inhaled air m3',air,15768)
 ck(18,'sphere diameter m',(6*air/math.pi)**(1/3),31.11152357354783,tol=.001)
 ck(19,'drop count under assumed diameter2mm',1000/(4/3*math.pi*.1**3),238732.414637843)
 beats=70*60*24*365.25*80
 ck(20,'assumed lifetime beats',beats,2945376000.)
 ck(20,'source stroke volume gallons',beats*50/1000/3.785411784,38904558.17363222,tol=.001)
 route=np.array([0.,2.6])+np.array([4.,0])+polar(3.1,45)
 for n in [21,28]:
  ck(n,'route resultant components km',route,[6.192031021678297,4.792031021678297])
  ck(n,'route resultant magnitude km',np.linalg.norm(route),7.829808032732693,tol=.001)
  ck(n,'north of east degrees',direction(route),37.73662745536043,tol=.001)
 A=polar(8,-90);BV=polar(15,60);C=polar(12,205);D=polar(10,143)
 for n in [22,29]:
  for label,v,m,a in [('A+B',A+BV,9.008546114203707,33.63916434485466),('A-B',A-BV,22.291166753564196,250.3385379655683)]:
   ck(n,label+' magnitude',np.linalg.norm(v),m,tol=.001);ck(n,label+' direction',direction(v),a,tol=.001)
  st(n,'opposite differences have equal length',np.isclose(np.linalg.norm(A-BV),np.linalg.norm(BV-A)))
 back=-(np.array([-180.,0])+polar(210,315)+polar(280,60))
 ck(23,'closing displacement components m',back,[-108.49242404917493,-93.99468901046783])
 ck(23,'closing displacement magnitude m',np.linalg.norm(back),143.546,tol=.001)
 ck(23,'south of west degrees',direction(back)-180,40.905,tol=.001)
 for a,e in [([2,-1],333.4349488),([2,1],26.5650512),([-2,1],153.4349488),([-2,-1],206.5650512)]:ck(24,'quadrant for'+str(a),direction(a),e)
 for n in [25,35]:
  for name,v,w in [('A',A,[0,-8]),('B',BV,[7.5,12.99038105676658]),('C',C,[-10.875693444439799,-5.071419140888393]),('D',D,[-7.986355100472928,6.018150231520484])]:ck(n,name+' components',v,w)
 amp=16/math.sin(rad(34))
 ck(26,'magnitude',amp,28.61266639930518,tol=.001);ck(26,'y component',-amp*math.cos(rad(34)),-23.721552060448174,tol=.001)
 amp=9.6/math.cos(rad(32))
 ck(27,'magnitude',amp,11.32011267295173,tol=.001);ck(27,'x component',-amp*math.sin(rad(32)),-5.998745778329544,tol=.001)
 for v,m,a in [([-8.6,5.2],10.0498756,148.8407),([-9.7,-2.45],10.004624,194.175),([7.75,-2.7],8.206856,340.792)]:ck(30,'magnitude'+str(v),np.linalg.norm(v),m,tol=.001);ck(30,'direction'+str(v),direction(v),a,tol=.001)
 v=np.array([-2.2,3.25-1.5]);ck(31,'result components',v,[-2.2,1.75]);ck(31,'magnitude',np.linalg.norm(v),2.811138559374119,tol=.001);ck(31,'north of west',180-direction(v),38.50065372034544,tol=.001)
 v=np.array([0.,-12])-polar(8,127)
 ck(32,'B components',v,[4.814520185216386,-18.389084080378344]);ck(32,'B magnitude',np.linalg.norm(v),19.009,tol=.001);ck(32,'B direction',direction(v),284.674,tol=.001)
 a=polar(2.8,60);b=polar(1.9,-60)
 for label,v,m,ang in [('sum',a+b,2.476893215281266,18.34816552681794),('difference',a-b,4.095119046458887,83.69122115670999)]:ck(33,label+' magnitude',np.linalg.norm(v),m,tol=.001);ck(33,label+' angle',direction(v),ang,tol=.001)
 for label,a,b in [('a',[5,-6.3],[5,-6.3]),('b',[-9.91,11.2],[-9.91,11.2]),('c',[-15,22.4],[-15,22.4]),('d',5*np.array([4,-6]),[20,-30])]:ck(34,'unit basis components '+label,a,b)
 a=np.array([4.,7]);b=np.array([5.,-2])
 ck(36,'A magnitude',np.linalg.norm(a),math.sqrt(65));ck(36,'B magnitude',np.linalg.norm(b),math.sqrt(29));ck(36,'difference',a-b,[-1,9]);ck(36,'difference magnitude',np.linalg.norm(a-b),math.sqrt(82));ck(36,'difference direction',direction(a-b),96.34019174590992)
 a=polar(3.6,70);b=polar(2.4,210);v=3*a-4*b
 ck(37,'combination components',v,[12.007901666822883,14.948680304487809],tol=.001);ck(37,'combination norm',np.linalg.norm(v),19.175,tol=.001);ck(37,'combination direction',direction(v),51.222,tol=.001)
 for v,e in [([-3,6],116.565051177078),([7,2],15.945395900922854),([4,8],63.43494882292201)]:ck(38,'angle'+str(v),direction(v),e)
 a=np.array([-2,3,4]);b=np.array([3,1,-3]);ck(39,'A norm',np.linalg.norm(a),math.sqrt(29));ck(39,'B norm',np.linalg.norm(b),math.sqrt(19));ck(39,'A-B',a-b,[-5,2,7]);ck(39,'difference norm',np.linalg.norm(a-b),math.sqrt(78));ck(39,'opposite difference norm',np.linalg.norm(b-a),np.linalg.norm(a-b))
 a=np.array([4.,7]);b=np.array([5.,-2]);ck(40,'dot',a@b,6);ck(40,'angle',vecangle(a,b),math.degrees(math.atan2(43,6)))
 ck(41,'A dot B',A@BV,-103.92304845413264);ck(41,'B dot C',BV@C,-147.44736797201853);ck(41,'A dot C',A@C,40.57135312710715)
 cross=lambda a,b:np.cross(np.r_[a,0.],np.r_[b,0.])
 ck(42,'A cross B',cross([4,7],[5,-2]),[0,0,-43])
 for a,b,e in [([-2,6],[2,-3],164.74488129694222),([3,5],[10,6],28.07248693585296),([-4,2],[7,14],90)]:ck(43,'angle'+str(a),vecangle(a,b),e)
 ck(44,'A cross B cm2',cross(polar(2.8,60),polar(1.9,-60)),[0,0,-4.607255148133214])
 ck(45,'A cross D m2',cross(A,D),[0,0,-63.890840803783424])
 a=polar(3.6,70);b=polar(2.4,210);ck(46,'dot m2',a@b,-6.618623988547972);ck(46,'cross m2',cross(a,b),[0,0,5.553685063854701])
 ck(47,'unique B with zero x component',np.cross([-8,0,0],[0,-2,0]),[0,0,16]);st(47,'parallel alternative cannot give nonzero cross',np.linalg.norm(np.cross([-8,0,0],[-2,0,0]))==0)
 return records

def verify_guided():
 records=[]
 def check(unit,label,actual,expected,tol=1e-9):
  ok=bool(np.allclose(actual,expected,rtol=tol,atol=tol));assert ok,(unit,label,actual,expected)
  records.append({'unit':unit,'check':label,'actual':np.asarray(actual).tolist(),'expected':np.asarray(expected).tolist(),'passed':ok})
 def structural(unit,label,ok):
  assert ok,(unit,label);records.append({'unit':unit,'check':label,'passed':True})
 deg=math.radians;angle=lambda v:math.degrees(math.atan2(v[1],v[0]))%360
 A=np.array([72.4*math.sin(deg(32)),72.4*math.cos(deg(32))]);BV=np.array([-57.3*math.cos(deg(36)),-57.3*math.sin(deg(36))]);C=np.array([0.,-17.8])
 for unit,v,mag,theta,quadrant in [
  ('VP1.7.1',-(A+BV+C),12.7,309,4),('VP1.7.2',A-BV+C,115,42.4,1),
  ('VP1.7.3',A+BV+2*C,11.2,225,3),('VP1.7.4',np.array([-38*math.sin(deg(37)),38*math.cos(deg(37))])-A,68.7,207,3)]:
  check(unit,'magnitude from unrounded polar input',np.linalg.norm(v),mag,tol=.004)
  check(unit,'direction measured counterclockwise',angle(v),theta,tol=.004)
  check(unit,'quadrant',int(angle(v)//90+1),quadrant)
 u=np.array([5*math.cos(deg(-36.9)),5*math.sin(deg(-36.9))]);v=np.array([-6.4*math.sin(deg(20)),6.4*math.cos(deg(20))])
 check('VP1.10.1','Ax Ay',u,[4.,-3.],tol=.001)
 check('VP1.10.1','Bx By',v,[-2.19,6.01],tol=.002)
 check('VP1.10.1','dot product',u@v,-26.8,tol=.002)
 check('VP1.10.1','polar/Cartesian dot agreement',u@v,5*6.4*math.cos(deg(146.9)))
 u=np.array([6.5*math.cos(deg(55)),6.5*math.sin(deg(55))]);v=np.array([4.8,-8.4])
 check('VP1.10.2','dot product',u@v,-26.8,tol=.002)
 check('VP1.10.2','angle',math.degrees(math.acos((u@v)/np.linalg.norm(u)/np.linalg.norm(v))),115,tol=.004)
 u=np.array([-5.,3,0]);v=np.array([2.5,4,-1.5])
 check('VP1.10.3','dot product',u@v,-.5)
 check('VP1.10.3','angle',math.degrees(math.acos((u@v)/np.linalg.norm(u)/np.linalg.norm(v))),91,tol=.001)
 Fy=(26-(-12)*4)/5;u=np.array([-12.,Fy]);v=np.array([4.,5.])
 check('VP1.10.4','Fy',Fy,14.8)
 check('VP1.10.4','work residual',u@v,26)
 check('VP1.10.4','angle',math.degrees(math.acos((u@v)/np.linalg.norm(u)/np.linalg.norm(v))),77.7,tol=.001)
 Fmax=425/math.cos(deg(35));W=Fmax*1.5*math.sin(deg(35))
 check('bridge','maximum normal component',Fmax*math.cos(deg(35)),425)
 check('bridge','maximum weight',Fmax,518.8292002236188)
 check('bridge','work both projections',W,Fmax*1.5*math.cos(deg(55)))
 check('bridge','work',W,446.38230560869)
 check('Q1.3','chosen example height cm',1.72*100,172)
 check('Q1.3','chosen example weight N',65*9.8,637)
 check('Q1.4','microgram as fraction kilogram',1e-6*1e-3/1,1e-9)
 check('Q1.4','ten-year drift at fixed rate',10*1e-9,1e-8)
 check('Q1.6','mean thickness mm',50/500,.1)
 check('Q1.6','reading contribution mm',.5/500,.001)
 check('Q1.10','first norm',np.linalg.norm([1,1,1]),math.sqrt(3))
 check('Q1.10','second norm',np.linalg.norm([3,-2]),math.sqrt(13))
 check('Q1.11','north to south displacement m',np.array([0.,-500])-np.array([0.,500]),[0,-1000])
 check('Q1.11','complete lap displacement',[0.,500]-np.array([0.,500]),[0,0])
 check('Q1.21','percent overshoot',10/890000*100,.0011235955056179776)
 u=np.array([1.,0,0]);v=np.array([1.,1,0]);w=np.array([0.,1,1])
 left=np.cross(u,np.cross(v,w));right=np.cross(np.cross(u,v),w)
 check('Q1.23','first parenthesization',left,[0,-1,-1])
 check('Q1.23','second parenthesization',right,[-1,0,0])
 structural('Q1.23','both nonzero, different norms and directions',np.linalg.norm(left)!=np.linalg.norm(right) and np.linalg.norm(np.cross(left,right))>0)
 u=np.array([1.,0,0]);v=np.array([0.,1,0]);w=u
 check('Q1.23','special equal case left',np.cross(u,np.cross(v,w)),[0,1,0])
 check('Q1.23','special equal case right',np.cross(np.cross(u,v),w),[0,1,0])
 check('Q1.26','nonzero counterexample norm',np.linalg.norm([4,-4]),math.sqrt(32))
 rng=np.random.default_rng(20261026)
 for i in range(40):
  a,b=rng.normal(size=(2,3));n=np.linalg.norm(a)
  check('Q1.19',f'self dot and norm sample{i}',a@a,n*n)
  check('Q1.19',f'self cross sample{i}',np.cross(a,a),[0,0,0])
  check('Q1.20',f'unit normalization sample{i}',np.linalg.norm(a/n),1)
  check('Q1.24',f'scalar triple orthogonality sample{i}',a@np.cross(a,b),0)
  structural('Q1.15',f'component bound sample{i}',n+1e-12>=np.max(np.abs(a)))

 return records

def main():
 raw=ROOT/'raw_materials/physics/translations/chapter-01'
 progress=json.loads((raw/'parent-exercise-progress.json').read_text(encoding='utf-8'))
 assert progress['status']=='partially-reviewed-not-ready'and progress['reviewedUnits']==82 and progress['expectedUnits']==129
 sha=sha256_asset
 assert sha(ROOT/'raw_materials/physics/source/young-freedman-15.pdf')==progress['sourcePDFSHA256']
 numbered=verify_numbered();guided=verify_guided();images=0;sourceUnits=0
 for row in progress['files']:
  p=raw/row['file'];assert sha(p)==row['sha256'],p
  text=p.read_text(encoding='utf-8');count=len(re.findall(r'^### (?:1\.\d+|VP1\.\d+\.\d+|Q1\.\d+|Bài tập cầu nối)',text,re.M))
  assert count==row['units']and text.count('<details>')==text.count('</details>')==count
  assert all(text.count(label)==count for label in ['**Tóm tắt đề bài:**','**Hướng đi:**','**Lời giải:**'])
  assert '<details open'not in text and not re.search(r'(?:source-image:|solution-image:|^:::)',text,re.M)
  sourceUnits+=count
 with pymupdf.open(ROOT/'raw_materials/physics/source/young-freedman-15.pdf')as pdf:
  for row in progress['originalImages']:
   p=ROOT/row['publicFile'];assert sha(p)==row['sha256']
   pix=pdf[row['page']-1].get_pixmap(matrix=pymupdf.Matrix(row['scale'],row['scale']),clip=pymupdf.Rect(row['rectangle']),alpha=False)
   actual=pymupdf.Pixmap(p);assert actual.samples==pix.samples and actual.width==pix.width and actual.height==pix.height
   images+=1
 manifest=json.loads((raw/'parent-solution-image-manifest.json').read_text(encoding='utf-8'))['assets']
 for row in manifest:assert sha(ROOT/row['publicFile'])==row['sha256']
 assert sourceUnits==82 and images==7 and len(manifest)==8
 print(json.dumps({'status':'passed-partial82units','sourceUnits':sourceUnits,'numberedChecks':len(numbered),'guidedNumericalChecks':len(guided),'exactOriginalCrops':images,'solutionDiagrams':len(manifest),'wholeChapterComplete':False,'pendingNumberedRange':'1.48–1.94'},ensure_ascii=False))
if __name__=='__main__':main()
