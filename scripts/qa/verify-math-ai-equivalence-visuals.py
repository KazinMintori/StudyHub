"""Independent mathematical certificates for lifting and max-epigraph visuals."""
from fractions import Fraction as F
from itertools import product
import json,math
from pathlib import Path

def lifted(u):return 1-sum(x*x for x in u)
examples=[]
for a,b in [([F(-4,5)],[F(4,5)]),([F(-3,5),F(-2,5)],[F(3,5),F(2,5)]),([F(1)],[F(-1)])]:
 m=[(x+y)/2 for x,y in zip(a,b)]
 s=(lifted(a)+lifted(b))/2
 gap=lifted(m)-s
 assert all(lifted(u)>=0 for u in [a,b,m])
 assert gap==sum((x-y)**2 for x,y in zip(a,b))/4
 assert sum(x*x for x in m)+s-1==-gap
 examples.append({'a':list(map(str,a)),'b':list(map(str,b)),'mid_slack':str(s),'graph_slack':str(lifted(m)),'gap':str(gap)})
assert examples[0]['gap']=='16/25' and examples[1]['gap']=='13/25'
for numerator in range(-50,81):
 x=F(numerator,10)
 values=[x*x,(x-3)**2,2-x]
 lower=(values[0]+values[1])/2
 assert lower==(x-F(3,2))**2+F(9,4)
 assert max(values)>=lower>=F(9,4)
x=F(3,2);values=[x*x,(x-3)**2,2-x]
assert values==[F(9,4),F(9,4),F(1,2)]
assert [F(9,4)-v for v in values]==[0,0,F(7,4)]
assert max(values)==F(9,4)
slice_checks=0
for y in [F(-1),F(-1,2),F(0),F(2,5),F(1)]:
 for level in [F(0),F(2),F(9,4),F(5,2),F(5),F(14)]:
  t=level-y*y
  if t<0:interval=None
  else:
   root=math.sqrt(t)
   lo=max(-root,3-root,2-t);hi=min(root,3+root)
   interval=(lo,hi) if lo<=hi+1e-10 else None
  for numerator in range(-50,351):
   x=F(numerator,100)
   feasible=all(value+y*y<=level for value in [x*x,(x-3)**2,2-x])
   predicted=interval is not None and interval[0]-1e-10<=x<=interval[1]+1e-10
   assert feasible==predicted,(x,y,level,interval)
   slice_checks+=1
assert max(F(-1,2)**2,(F(-1,2)-3)**2,2-F(-1,2))+1==F(53,4)<14
report={'scope':'Exact arithmetic certificates; browser and visual QA are separate','slack_lifts':examples,'epigraph_optimum':{'x':'3/2','t':'9/4','slacks':['0','0','7/4']},'sampled_epigraph_points':131,'slice_membership_checks':slice_checks,'surface_height_on_displayed_box_maximum':'53/4 < 14'}
Path('qa/math-ai-visuals/equivalence-visuals-numerical.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print('PASS: lifting residuals and midpoint gaps in R2/R3; max epigraph lower bound, optimum and active constraints.')
