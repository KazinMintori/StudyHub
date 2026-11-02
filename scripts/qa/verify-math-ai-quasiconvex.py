"""Independent exact/numerical certificates for the quasiconvex lecture."""
from fractions import Fraction as F
from pathlib import Path
from math import sqrt,ceil,log2,exp
import json

def phi(point,t):
 return sum(value*value for value in point)-t*t*((point[0]-4)**2+sum(value*value for value in point[1:]))
def box_trial(t,dimension):
 center=-4*t*t/(1-t*t)
 point=[max(F(-1),min(F(3,2),center)),F(1)]+([F(0)] if dimension==3 else [])
 return phi(point,t)<=0,point

histories={}
for dimension in [2,3]:
 lo,hi=F(0),F(1);history=[]
 witness=[F(0),F(1)]+([F(0)] if dimension==3 else [])
 for _ in range(7):
  t=(lo+hi)/2;ok,point=box_trial(t,dimension)
  if ok:hi=t;witness=point
  else:lo=t
  assert phi(witness,hi)<=0
  history.append({'level':str(t),'feasible':ok,'lower':str(lo),'upper':str(hi),'witness':list(map(str,witness))})
 assert (lo,hi)==(F(15,64),F(31,128))
 histories[str(dimension)]=history

exact=sqrt(5)-2
assert abs(-4*exact**2/(1-exact**2)-(2-sqrt(5)))<1e-14
assert abs(4*exact/(1-exact**2)-1)<1e-14
chord=[y/sqrt(16+y*y) for y in [8,100,54]]
assert chord[2]>(chord[0]+chord[1])/2
assert ceil(log2(10/1e-6))==24
assert max(0,ceil(log2(.001/.01)))==0
for value in [F(-2),F(-1),F(0),F(1),F(2)]:
 polynomial=value**3-3*value
 assert (polynomial<=0)==(value<=-sqrt(3) or 0<=value<=sqrt(3))
assert F(28,29)-F(27,28)==F(1,812)
# A nonattained optimum need not make inf(p-p* q) equal to zero.
# f(x)=(x+1)/x on x>0 has infimum 1, while p-q is identically 1.
assert all((x+1)/x>1 and (x+1)-x==1 for x in [F(1),F(10),F(100)])
report={'scope':'Independent mathematical examples, not browser QA','bisection':histories,'distance_ratio_optimum':exact,'nonconvex_chord':chord,'iterations_10_to_1e-6':24,'edge_case_already_short_bracket':0}
Path('qa/math-ai-visuals/quasiconvex-numerical.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print('PASS: exact R2/R3 feasibility certificates, saved upper witnesses, chord counterexample and iteration bounds.')
