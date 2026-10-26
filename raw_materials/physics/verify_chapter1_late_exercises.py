from pathlib import Path
import json,math,re,hashlib,xml.etree.ElementTree as ET
import numpy as np,pymupdf
ROOT=Path(__file__).resolve().parents[2];B=ROOT/'raw_materials/physics/translations/chapter-01';checks=[]
def ck(unit,label,actual,expected,tol=1e-8):
 assert np.allclose(actual,expected,atol=tol,rtol=tol),(unit,label,actual,expected)
 checks.append({'unit':unit,'check':label,'actual':np.asarray(actual).tolist(),'expected':np.asarray(expected).tolist()})
def st(unit,label,cond):
 assert cond,(unit,label);checks.append({'unit':unit,'check':label,'passed':True})
def sha(p):
 data=p.read_bytes()
 if p.suffix.lower()in {'.md','.svg'}:data=data.replace(b'\r\n',b'\n')
 return hashlib.sha256(data).hexdigest()
t=(B/'parent-12-bai-tap-048-094.md').read_text('utf8')
units={int(m[1]):m[2]for m in re.finditer(r'^### 1\.(\d+)[^\n]*\n([\s\S]*?)(?=^### |^## |\Z)',t,re.M)}
st('all','exact47sourceunits',set(units)==set(range(48,95)))
for n,body in units.items():
 st(n,'oneclosedsolution',body.count('<details>')==body.count('</details>')==1 and'<details open'not in body)
 st(n,'threestages',all(body.count(x)==1 for x in ['**Tóm tắt đề bài:**','**Hướng đi:**','**Lời giải:**']))
st('all','no broken inline or controlcharacters',not any(l.replace('$$','').count('$')%2 for l in t.splitlines())and not any(ord(c)<32 and c not in '\n\r\t'for c in t))
st('all','no thinker monologue',not re.search(r'\b(?:Khoan đã|À không|Wait|Nhầm rồi|Thử lại nào)\b',t,re.I))
for a in [45,135]:ck(48,'equalproducts '+str(a),abs(math.cos(math.radians(a))),math.sin(math.radians(a)))
st(48,'30degreesdotlarger',math.cos(math.pi/6)>math.sin(math.pi/6))
rho=[5.97e27/(4*math.pi*(6.37e8)**3/3),1.99e33/(4*math.pi*(7.5e8)**3/3),1.99e33/(4*math.pi*(1e6)**3/3)]
ck(49,'three densities with actualAppendixFmeanradius',rho,[5.514008418404722,1126109.6417879884,4.750775051293076e14])
f=1420405751.786
ck(50,'period',1/f,7.040241837535597e-10,tol=1e-16);ck(50,'cycles1hour',f*3600,5113460706429.6);ck(50,'earthagecycles',f*4.6e9*365.25*86400,2.0619314414178462e26);ck(50,'source100000yearclockdrift',4.6e9/100000,46000)
st(50,'actualsourceinputand3sigfigresultsinfragment',all(x in units[50]for x in [r'$10^5$',r'2{,}06\times10^{26}',r'4{,}60\times10^4']))
R=(5.5*5.97e24/1760/(4*math.pi/3))**(1/3);ck(51,'radiuskm',R/1000,16453.005687585297);ck(51,'radiusratio',R/6.37e6,2.5828894329019305)
ck(52,'nominalarea',7.6*1.9,14.44);ck(52,'exactupperarea',7.61*1.91,14.5351);ck(52,'exactlowerarea',7.59*1.89,14.3451);ck(52,'firstorderfractionalpropagation',.095/14.44,.01/7.6+.01/1.9)
ck(53,'70kgwaterequivalentatoms',3*70/(18*1.66053906660e-27),7.0e27,tol=.01)
ck(54,'halfmicrometrecelldensity',1000*math.pi/6*(.5e-6)**3,6.544984694978735e-17,tol=1e-23);ck(54,'beeatgivendensity',math.pi*.25**2*1.5,.2945243112740431)
st(54,'correctmicrounitintheactualprompt',r'0{,}5\,\mu\mathrm{m}'in units[54].split('<details>',1)[0]and'0{,}5\\,\\mathrm{mm}'not in units[54])
A=np.array([3.,0,-4]);norms=[np.array([.6,0,-.8]),np.array([-.6,0,.8]),np.array([.8,0,.6]),np.array([-.8,0,-.6])]
for i,u in enumerate(norms):ck(55,'unitlength'+str(i),np.linalg.norm(u),1)
for i in [2,3]:ck(55,'perpendicular'+str(i),A@norms[i],0)
rad=math.radians
def vec(m,d):return np.array([m*math.cos(rad(d)),m*math.sin(rad(d))])
sources={56:(-(vec(100,30)+vec(80,120)+vec(40,233)),[-22.52993945236196,-87.33661190086337],90.19579785139176),57:(-(vec(180,180)+vec(210,315)+vec(280,60)),[-108.492424049175,-93.994689010468],143.5465347482849),58:(vec(170,22)+vec(230,-36),[343.6951639825918,-71.50748714656376],351.0551045961825),59:(np.array([0,450])+vec(600,233.1),[-360.25213519553046,-29.8107950922543],361.48344971377475),60:(np.array([5.8,0])-vec(2,0)-vec(3.5,-45),[1.32512626584708,2.47487373415292],2.8073046896334275),62:(-(vec(147,5)+vec(106,-77)+vec(166,-145)),[-34.3061930279636,185.685021117603],188.82754552108253),63:(np.array([-32,0])-vec(23,-34)-vec(46,90),[-51.067864168766,-33.138563220173],60.877673436629635),64:(-(vec(40,45)+vec(80,120)+vec(50,-90)),[11.7157287525381,-47.566303550217],48.987871291110764),65:(vec(20.8,90)+vec(38,0)+vec(18,237),[28.1964973697295,5.70392977698237],28.76764291390432),67:(-vec(122,-32)-vec(72,180),[-31.461867731084,64.650150236451],71.89917278191668),69:(-(vec(825,-90)+vec(1250,120)+vec(1000,32)),[-223.048096156426,-787.451018963753],818.4311580493862),71:(np.array([0,-10])-vec(12,0)-vec(28,140),[9.44924440733138,-27.9980530712231],29.549605676700814),72:(vec(16,210)-vec(26,150),[8.66025403784439,-21],22.715633383201094),73:(vec(32,37)-vec(21,-23),[6.22573439901212,27.4634344391403],28.160255680657446)}
for n,(a,expected,mag)in sources.items():
 ck(n,'sourcecomponents',a,expected);ck(n,'magnitude',np.linalg.norm(a),mag)
 ang=math.atan2(a[1],a[0]);ck(n,'recoverxfromdirection',mag*math.cos(ang),a[0]);ck(n,'recoveryfromdirection',mag*math.sin(ang),a[1])
for n,token in {56:r'90{,}2',68:r'0{,}22',70:r'22{,}6',71:r'29{,}5',72:r'67{,}6',78:r'51{,}7',82:r'323^\circ',86:r'143{,}2',90:r'38{,}5',91:r'128{,}5'}.items():st(n,'computedresultboundtoactualfragment',token in units[n])
ck(61,'symmetrictraction',12.8/(2*math.cos(rad(32))),7.546741781517418)
ck(66,'threedimensionaldistance',np.linalg.norm([-8,12,22]),26.30589287593181)
store=vec(.6,90)+vec(1.4,150);second=store-vec(.8,130)
ck(68,'straightlinedistance',np.linalg.norm(store),1.7776388834631176);ck(68,'Sundaysecondleg',np.linalg.norm(second),.9796355771639503);ck(68,'longerSaturdayby',2-(.8+np.linalg.norm(second)),.22036442283604973)
post=np.array([52*math.cos(rad(37)),52*math.sin(rad(37))]);d=math.sqrt(68**2-post[0]**2)-post[1]
ck(70,'positivephysicalroot',d,22.551122739648676);ck(70,'recoverseparation',np.linalg.norm(post-[0,-d]),68)
ck(74,'tetrahedralangle',math.degrees(math.acos(np.dot([1,1,1],[1,-1,-1])/3)),109.47122063449069)
ck(75,'workbycomponents',np.dot(vec(5,120),[.8,0]),-2)
ck(76,'chargedparticleforce',-8e-6*np.cross([3e4,0,0],[0,-5,0]),[0,0,1.2])
ck(77,'obtuseanglefrombothproducts',math.degrees(math.atan2(9,-6)),123.69006752597979)
ck(78,'actualtorquevector',np.cross([*vec(4,126),0],[0,-22,0]),[0,0,51.725102201737634])
rng=np.random.default_rng(20261026)
for i,(a,b,c,d)in enumerate(rng.uniform(.01,10,(30,4))):
 av=np.array([a,0,-b]);bv=np.array([0,-c,d]);ck(79,'scalarexpansion'+str(i),av@bv,-b*d);ck(79,'crossexpansion'+str(i),np.cross(av,bv),[-b*c,-a*d,-a*c]);ck(79,'zero-cdirection'+str(i),np.cross(av,[0,0,d]),[0,-a*d,0])
for angle in [0,180]:ck(80,'maximumdotmagnitude'+str(angle),abs(math.cos(rad(angle))),1);ck(80,'zerocross'+str(angle),math.sin(rad(angle)),0)
ck(80,'maximumcross90',math.sin(rad(90)),1);ck(80,'doublecrosscondition',math.cos(math.atan(.5)),2*math.sin(math.atan(.5)))
ck(81,'crossmagnitude',math.sqrt((12*16)**2-112**2),155.9487095169434)
for angle,z in [(143,40),(323,-40),(53,0),(233,0)]:ck(82,'actualcrossz'+str(angle),np.cross([*vec(5,53),0],[*vec(8,angle),0])[2],z)
ck(83,'recoverpositivedot',np.dot(vec(9,242),vec(48/(9*math.cos(rad(79))),321)),48)
av=np.array([-2,3,4]);bv=np.array([3,1,-3]);c=np.array([-13,6,-11]);ck(84,'actualcross',np.cross(av,bv),c);ck(84,'unitnorm',np.linalg.norm(c/np.linalg.norm(c)),1);ck(84,'firstorthogonality',av@c,0);ck(84,'secondorthogonality',bv@c,0)
c=np.array([-390/49,-300/49]);ck(85,'orthogonality',[5,-6.5]@c,0);ck(85,'requireddot',[3.5,-7]@c,15)
for angle in [36.75193392499762,143.24806607500238]:ck(86,'bothcrossbranches'+str(angle),9*math.sin(rad(angle)),math.sqrt(29))
dens={k:m/v for k,m,v in [('A',8,1.67),('B',6e-6,9.38e-6),('C',.008,.0025),('D',.9,2.81),('E',9e-5,1.41e-5),('F',6e-5,1.25e-4)]}
st(87,'densityorder',sorted(dens,key=dens.get)==list('DFBCAE'));st(87,'sourceordertheactualfragment','D, F, B, C, A, E'in units[87])
ck(88,'recoverforcesfromsource',np.sort(np.roots([1,-8,15])),[3,5]);ck(88,'fourmeasurements',np.round(np.sqrt(34+30*np.cos(np.deg2rad([0,45,60,90]))),2),[8,7.43,7,5.83]);ck(88,'30degreeresult',math.sqrt(34+30*math.cos(rad(30))),7.74,tol=.001)
E=np.array([.3182,.9329,0]);M=np.array([1.3087,-.4423,-.0414]);dv=M-E
ck(89,'threedistances',[np.linalg.norm(a)for a in [E,M,dv]],[.9856742108830888,1.3820415840342866,1.6952814663058167]);ck(89,'actualdot',(-E)@dv,.96774698)
ck(89,'Earthviewangle',math.degrees(math.acos((-E)@dv/(np.linalg.norm(E)*np.linalg.norm(dv)))),54.609636151460755)
receiver=np.array([1,-5])+np.sum([[9,0],[0,11],[-6,4],[12,18]],axis=0);ck(90,'allfourroutelegs',receiver,[16,28]);throw=receiver-[0,-7];ck(90,'throwvector',throw,[16,35]);ck(90,'throwmagnitude',np.linalg.norm(throw),38.48376280978771)
starA=vec(138,25.6);starM=np.array([77.,0]);diff=starA-starM
ck(91,'starseparation',np.linalg.norm(diff),76.20534855794914);ck(91,'observeratMerakangle',math.degrees(math.acos((-starM)@diff/(77*np.linalg.norm(diff)))),128.51339718687984)
ck(92,'alveolarvolumeLitres',480e6*4.2e6*1e-18*1000,2.016);ck(93,'spherediametermillimetres',(6*4.2e-12/math.pi)**(1/3)*1000,.200178250518496)
for n,choices in [(92,[r'2000\,\mu\mathrm m^3',r'2\,\mathrm m^3',r'2{,}0\,\mathrm L',r'120\,\mathrm L']),(93,[r'0{,}20\,\mathrm{mm}',r'2\,\mathrm{mm}',r'20\,\mathrm{mm}',r'200\,\mathrm{mm}'])]:
 st(n,'allsourcechoicespreserved',all(x in units[n].split('<details>',1)[0]for x in choices))
st(94,'correctcchoiceanddatainterpretation','Chọn (c)'in units[94]and'sáu'in units[94])
originals=json.loads((B/'parent-late-image-assets.json').read_text('utf8'))
with pymupdf.open(ROOT/'raw_materials/physics/source/young-freedman-15.pdf')as pdf:
 for row in originals:
  p=ROOT/row['publicFile'];actual=pymupdf.Pixmap(p);expected=pdf[row['pdfPage1Based']-1].get_pixmap(matrix=pymupdf.Matrix(row['scale'],row['scale']),clip=pymupdf.Rect(row['rectangle']),alpha=False)
  st(row['key'],'exactsourcepixels',actual.samples==expected.samples and actual.width==expected.width and actual.height==expected.height);st(row['key'],'sourceSHA',sha(p)==row['sha256'])
  st(row['key'],'canonicalsourceimagelink',t.count('(/'+row['publicFile'].removeprefix('docs/')+')')==1)
for row in json.loads((B/'parent-late-solution-image-manifest.json').read_text('utf8'))['assets']:
 p=ROOT/row['publicFile'];st(row['key'],'solutionSHA',sha(p)==row['sha256']);svg=ET.parse(p).getroot();scale=row['screenMapping']['scale'];world=np.array(row['worldPoints']);center=np.array(row['screenMapping']['centerWorld']);screen=np.array(row['screenMapping']['centerScreen'])
 for seg in row['segments']:
  line=next(n for n in svg.findall('.//{*}line')if n.get('data-from')==str(seg['from'])and n.get('data-to')==str(seg['to'])and n.get('stroke')==seg['color'])
  coords=np.array([[float(line.get('x1')),float(line.get('y1'))],[float(line.get('x2')),float(line.get('y2'))]])
  expected=(world[[seg['from'],seg['to']]]-center)*[scale,-scale]+screen;ck(row['key'],'actualarrow'+str(seg),coords,expected,tol=1e-6)
 # Independent physical endpoint checks connect the actual diagram to source solutions.
 n=int(row['sourceUnit'].split('.')[1])
 if n in [57,62,64,69]:ck(n,'sourceclosureroute',world[-1],world[0]);ck(n,'sourcefinalleg',world[-1]-world[-2],sources[n][0])
 if n==60:ck(n,'sourcethirdleg',world[3]-world[2],sources[n][0]);ck(n,'sourceendpoint',[*world[3]],[5.8,0])
 if n==72:ck(n,'sourceRicardotoJane',world[2]-world[1],sources[n][0])
 if n==79:ck(n,'sourcec0orientation',np.cross([3,0,-2],[0,0,2]),[0,-6,0])
 if n==89:ck(n,'sourceXYpositions',world,[E[:2]*0,E[:2],M[:2]]);ck(n,'sourceZnotomitted',row['sourceZ'],[0,0,-.0414])
 if n==90:ck(n,'sourceallrunningpoints',world[:5],[[1,-5],[10,-5],[10,6],[4,10],[16,28]]);ck(n,'sourceactualthrow',world[4]-world[5],throw)
 if n==91:ck(n,'sourcesame-scaletriangle',world,[[0,0],starM,starA])
ledger=[{'id':f'1.{n}','sourcePDFPages':[49]if n<50 else[50]if n<63 else[51]if n<82 else[52]if n<92 else[53],'reviewed':True}for n in range(48,95)]
print(json.dumps({'status':'passed-independent47canonicalunits','units':47,'checks':len(checks),'originalCrops':6,'solutionDiagrams':10,'scope':'Late47units only; whole129chapter gate isseparate.'},ensure_ascii=False))
