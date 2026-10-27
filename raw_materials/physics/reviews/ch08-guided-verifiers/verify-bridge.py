from pathlib import Path
import re,json,math,hashlib,xml.etree.ElementTree as ET,numpy as np
ROOT=Path(__file__).resolve().parents[4];B=ROOT;OUT=ROOT/"qa/physics1-remaining/ch08-guided-recomputed";OUT.mkdir(parents=True,exist_ok=True);checks=[]
def ck(label,a,b,tol=1e-8):
 assert np.allclose(a,b,atol=tol,rtol=tol),(label,a,b);checks.append({'check':label,'actual':np.asarray(a).tolist(),'expected':np.asarray(b).tolist()})
def st(label,c):
 assert c,label;checks.append({'check':label,'passed':True})
p=ROOT/'raw_materials/physics/translations/chapter-08/parent-16-bai-tap-cau-noi.md';text=p.read_text('utf8');prompt,solution=text.split('<details>',1)
st('11actualsourceguideitemsbeforeclosedbox',re.findall(r'^(\d+)\. ',prompt,re.M)==list(map(str,range(1,12))))
st('11correspondingsolutionsteps',re.findall(r'^#### (\d+)\.',solution,re.M)==list(map(str,range(1,12))))
st('all6sourceparts',all('('+x+')'in prompt for x in 'abcdef'))
st('exactoneclosedsolution',text.count('<details>')==text.count('</details>')==1 and'<details open'not in text)
st('threepedagogicalstages',all(text.count(s)==1 for s in ['**Tóm tắt đề bài:**','**Hướng đi:**','**Lời giải:**']))
mA,mB,mC=.6,1.8,1.2;uA=np.array([4.,0]);uB=np.array([2.,0]);uC=np.zeros(2);vB1=np.array([3.,0]);vA1=(mA*uA+mB*uB-mB*vB1)/mA
ck('Aafterfirst',vA1,[1,0]);ck('firstmomentum',mA*vA1+mB*vB1,mA*uA+mB*uB)
Ki1=(mA*(uA@uA)+mB*(uB@uB))/2;Kf1=(mA*(vA1@vA1)+mB*(vB1@vB1))/2;ck('firstelastic',Kf1,Ki1);ck('firstactualkineticenergy',Ki1,8.4)
theta=math.radians(19);vB2=np.array([2*math.cos(theta),2*math.sin(theta)]);vC2=np.linalg.solve([[mC,0],[0,mC]],mB*vB1-mB*vB2)
ck('secondmomentumvector',mB*vB2+mC*vC2,mB*vB1);ck('Ccomponents',vC2,[1.6634442732020498,-.9767044633714702]);ck('Cspeed',np.linalg.norm(vC2),1.928988973223654)
JB=mB*(vB2-vB1);ck('impulseOnB',JB,[-1.9961331278424594,1.1720453560457642]);ck('Newtonthirdlawimpulses',JB,-mC*(vC2-uC));ck('impulsemagnitude',np.linalg.norm(JB),2.3147867678683847)
ck('Cangle',math.degrees(math.atan2(vC2[1],vC2[0])),-30.41966255878202);ck('impulseangle',math.degrees(math.atan2(JB[1],JB[0])),149.58033744121798)
Kf2=(mB*(vB2@vB2)+mC*(vC2@vC2))/2;Ki2=mB*(vB1@vB1)/2;ck('secondinitialenergy',Ki2,8.1);ck('secondfinalenergy',Kf2,5.832599075291068);st('secondinelastic',Kf2<Ki2)
M=mA+mB+mC;cm0=(mA*uA+mB*uB)/M;cm1=(mA*vA1+mB*vB1)/M;cm2=(mA*vA1+mB*vB2+mC*vC2)/M;ck('CMallstages',[cm0,cm1,cm2],[[5/3,0]]*3)
for angle in [5,19,30,60]:
 vb=np.array([2*math.cos(math.radians(angle)),2*math.sin(math.radians(angle))]);vc=(mB*vB1-mB*vb)/mC;imp=mB*(vb-vB1);ck('impulseandCmomentumopposite'+str(angle),imp,-mC*vc)
rows=json.loads((ROOT/'raw_materials/physics/translations/chapter-08/parent-guided-discussion-solution-image-manifest.json').read_text('utf8'))['assets'];st('oneactual3statediagram',len(rows)==1)
for row in rows:
 svg=ET.parse(ROOT/row['publicFile']).getroot();st('diagramSHA',hashlib.sha256((ROOT/row['publicFile']).read_bytes().replace(b'\r\n',b'\n')).hexdigest()==row['sha256']);st('all9objectstates',len(row['arrows'])==9)
 expectedStates=[[uA,uB,uC],[vA1,vB1,uC],[vA1,vB2,vC2]]
 for item in row['arrows']:
  i=item['state'];j='ABC'.index(item['object']);ck('sourcevelocity'+str((i,j)),item['velocityMps'],expectedStates[i][j]);lines=[x for x in svg.findall('.//{*}line')if x.get('data-state')==str(i)and x.get('data-object')==item['object']]
  if item['arrowDrawn']:
   st('actualarrowexists'+str((i,j)),len(lines)==1);n=lines[0];actual=np.array([float(n.get('x2'))-float(n.get('x1')),float(n.get('y2'))-float(n.get('y1'))]);ck('actualSVGvelocityvector'+str((i,j)),actual,np.array(expectedStates[i][j])*[30,-30],tol=1e-6)
  else:st('initiallystationarynoinventedarrow'+str((i,j)),not lines and np.linalg.norm(expectedStates[i][j])==0)
for value in ['1{,}00','8{,}40','1{,}93','2{,}31','5{,}83','1{,}67','149{,}6']:st('computedanswerinactualfragment'+value,value in text)
r={'status':'passed-private-bridge-source-numerics-geometry','sourceUnits':1,'actualSourceGuideItems':11,'checks':len(checks),'sourcePDFPage':282,'solutionDiagrams':1,'fragmentSHA256':hashlib.sha256(p.read_bytes()).hexdigest(),'records':checks,'scopeLimit':'Onlyonechapter8bridgeproposal;VP12/Q26/numbered109 andwhole148acceptance separate.'}
(OUT/'numeric-bridge.json').write_bytes((json.dumps(r,ensure_ascii=False,indent=2)+'\n').encode('utf8'));print(json.dumps({k:r[k]for k in ['status','sourceUnits','actualSourceGuideItems','checks','solutionDiagrams']},ensure_ascii=False))
