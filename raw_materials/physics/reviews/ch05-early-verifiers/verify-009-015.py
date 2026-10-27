from pathlib import Path
import hashlib, json, math, re, xml.etree.ElementTree as ET
import numpy as np
import pymupdf

ROOT=Path(__file__).resolve().parents[4];B=ROOT/'raw_materials/physics/translations/chapter-05';REVIEW_OUTPUT=ROOT/'qa/physics1-remaining/ch05-early-recomputed';REVIEW_OUTPUT.mkdir(parents=True,exist_ok=True)
R = B/'review-009-015'
P = B/'parent-11-bai-tap-001-059.md'
text = P.read_text(encoding='utf8')
checks = []

def yes(name, condition):
    assert condition, name
    checks.append(dict(name=name, passed=True))

def near(name, actual, expected, tol=1e-9):
    assert math.isclose(float(actual),float(expected),rel_tol=tol,abs_tol=tol),(name,actual,expected)
    checks.append(dict(name=name,actual=float(actual),expected=float(expected)))

g = 9.8
t = math.radians(19)
# Independent 2D equilibrium, with Cartesian physical force directions.
for case,direction,expectedF,expectedN in [
    ('a',[math.cos(t),math.sin(t)],574.3022244624245,1667.8947673571952),
    ('b',[1,0],607.3939098429696,1865.6428816132873)]:
    f,n = np.linalg.solve([[direction[0],-math.sin(t)],[direction[1],math.cos(t)]],[0,180*g])
    near('9'+case+' applied force',f,expectedF)
    near('9'+case+' normal force',n,expectedN)
    near('9'+case+' no work by normal in motion',np.dot([-n*math.sin(t),n*math.cos(t)],[-math.cos(t),-math.sin(t)]),0)

# Student and entire elevator each satisfy Newton II.
for reading,expected in [(450,-1.7818181818181815),(670,2.138181818181819),(0,-g)]:
    a = (reading-550)/(550/g)
    near('10 acceleration from scale '+str(reading),a,expected)
    cable=850*g+850*a
    near('10 whole system reaction '+str(reading),cable,850*g*reading/550,1e-8)
near('10 cable parta unrounded',850*g*450/550,6815.454545454545)
near('11 rocket thrust minus gravity produces4g',110250000-2.25e6*g,2.25e6*4*g)
for mass in [1,55,80]:
    near('11 astronaut contact5weights mass'+str(mass),5*mass*g-mass*g,mass*4*g)
near('11 shortest time from launch',331/(4*g),8.443877551020407)
near('12 initial acceleration includes entire mass',(1720-125*g)/125,3.96)
normal=21.76326530612245
near('12 PSU Newton II',normal-15.5,15.5/g*3.96)
yes('12 PSU normal greater than weight',normal>15.5)

# Signed kinematics, soil work including gravity, and impulse independently agree.
v = 311*1000/3600
d = 81/100
a = v*v/(2*d)
duration = v/a
ground = 210*(g+a)
near('13 SI speed',v,86.38888888888889)
near('13 acceleration upward',a,4606.814891022709)
near('13 dimensionless a/g',a/g,470.0831521451744)
near('13 actual ground force',ground,969489.127114769)
near('13 dimensionless F/w',ground/(210*g),471.0831521451744)
near('13 duration',duration,.018752411575562702)
near('13 impulse changes downward momentum',(ground-210*g)*duration,210*v,1e-8)
near('13 work balances kinetic energy',(ground-210*g)*d,.5*210*v*v,1e-8)
near('13 signed displacement',-v*duration+.5*a*duration**2,-d)

# Unknowns are (a,TA,TB); actual left-to-right masses 30,20,10.
acc,TA,TB = np.linalg.solve([[-30,0,1],[-20,1,-1],[10,1,0]],[0,0,190])
near('14 actual common acceleration',acc,190/60)
near('14 ropeA pulls50kg',TA,158.33333333333334)
near('14 ropeB pulls30kg',TB,95)
near('14 middle sled NewtonII',TA-TB,20*acc)
near('14 right sled NewtonII',190-TA,10*acc)
yes('14 A tension exceeds B',TA>TB)

# Unknowns are the upward brick acceleration, downward counterweight acceleration, T.
a1,a2,T = np.linalg.solve([[-15,0,1],[0,28,1],[1,-1,0]],[15*g,28*g,0])
near('15 acceleration of bricks',a1,2.9627906976744187)
near('15 inextensible rope',a1,a2)
near('15 same tension in both strands',T,191.4418604651163)
yes('15 both weight comparisons',15*g<T<28*g)
near('15 balanced masses limiting case',(15-15)*g/(15+15),0)

ns={'s':'http://www.w3.org/2000/svg'}
arrows=0
for number,expected in [(9,[3,3]),(11,[2,2]),(12,[2]),(15,[2,2])]:
    root=ET.parse(ROOT/f'docs/vat-ly-1/bai-giang/img/young-05/solution-s5-{number}-fbd.svg').getroot()
    panels=[p for p in root.findall('.//s:g',ns) if p.get('transform','').startswith('translate(')]
    yes(f'SVG{number} required number of body panels',len(panels)==len(expected))
    for i,(panel,count) in enumerate(zip(panels,expected)):
        lines=[x for x in panel.findall('s:line',ns) if x.get('marker-end')]
        yes(f'SVG{number}panel{i} actual force count',len(lines)==count)
        arrows+=len(lines)
        delta=np.array([[float(x.get('x2'))-float(x.get('x1')),float(x.get('y2'))-float(x.get('y1'))] for x in lines])
        if number==9:
            near('SVG9 balanced horizontal forces'+str(i),delta[:,0].sum(),0,2e-6)
            near('SVG9 balanced vertical forces'+str(i),delta[:,1].sum(),0,2e-6)
            near('SVG9 full vertical gravity'+str(i),delta[2,0],0)
            near('SVG9 full gravity scale'+str(i),delta[2,1],100)
            near('SVG9 normal perpendicular to incline'+str(i),np.dot(delta[1],[math.cos(t),-math.sin(t)]),0,2e-6)
            if i==0:
                near('SVG9 true19degree force angle',math.degrees(math.atan2(-delta[0,1],delta[0,0])),19,1e-6)
            else:near('SVG9 horizontal push',delta[0,1],0)
        elif number==11:
            near('SVG11 upward contact/thrust and downward weight ratio'+str(i),-delta[0,1]/delta[1,1],5)
            yes('SVG11 upward net acceleration'+str(i),delta[:,1].sum()<0)
        elif number==12:
            near('SVG12 contact/weight ratio',-delta[0,1]/delta[1,1],1+3.96/g,1e-7)
        else:
            near('SVG15 both equal upward tensions'+str(i),delta[0,1],-.4*T,1e-7)
            near('SVG15 actual gravitational force'+str(i),delta[1,1],.4*[15,28][i]*g)
            near('SVG15 resultant matches actual acceleration'+str(i),delta[:,1].sum(),.4*[-15*a1,28*a2][i],1e-6)
near('16 actual arrows across4 solution SVGs',arrows,16)

report={'status':'passed','scope':'Independent physical computations and actual SVG geometry; full source/crop/structure binding handled by canonical entrypoint.','checksCount':len(checks),'checks':checks}
(REVIEW_OUTPUT/'numeric-009-015.json').write_bytes((json.dumps(report,ensure_ascii=False,indent=2)+'\n').encode('utf8'))
print('PASS 009-015',len(checks),'physical/geometry checks.')
