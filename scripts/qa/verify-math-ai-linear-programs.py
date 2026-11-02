"""Independent exact certificates for the LP lecture and examples."""
from fractions import Fraction as F
from pathlib import Path
from itertools import product
import json
V=[(F(1,2),F(1,2)),(F(7,2),F(1,2)),(F(9,2),F(11,5)),(F(14,5),F(19,5)),(F(4,5),F(3))]
assert [sum(p) for p in V]==[F(1),F(4),F(67,10),F(33,5),F(19,5)]
normal=(F(8,5),F(17,10))
values=[sum(x*c for x,c in zip(p,normal)) for p in V]
assert values==[F(33,20),F(129,20),F(547,50),F(547,50),F(319,50)]
assert max(values)==F(547,50)
triangle=[(-2,0),(4,0),(1,3)]
assert [x-2*y for x,y in triangle]==[-2,4,-5]
for delta in [F(0),F(1,3),F(10)]:
 u,v,x2,s1,s2=1+delta,delta,F(3),F(0),F(0)
 assert u-v+x2+s1==4 and -u+v+x2+s2==2 and u-v-2*x2==-5
positive=[(2,2),(3,1),(3,3)];negative=[(0,0),(1,0),(0,F(3,2))]
assert all((6*x+4*y-13)/7>=1 for x,y in positive)
assert all((6*x+4*y-13)/7<=-1 for x,y in negative)
assert 2**30==1073741824
assert 2*2+2+3==9 and 3+1==4
cube_cases=[]
for c in [(1,2,3),(1,2,0),(1,0,0),(0,0,0),(-1,1,-1)]:
 vals=[sum(ci*xi for ci,xi in zip(c,p)) for p in product([0,1],repeat=3)]
 best=min(vals);count=vals.count(best)
 assert count==2**sum(ci==0 for ci in c)
 assert best==sum(min(ci,0) for ci in c)
 cube_cases.append({'c':c,'value':best,'optimal_vertices':count,'optimal_dimension':sum(ci==0 for ci in c)})
report={'scope':'Independent exact LP examples; no browser claims','pentagon_values':list(map(str,values)),'split_variable_optimum':-5,'classification_margin_minimum':1,'cube_cases':cube_cases,'cube_vertices_dimension_30':2**30}
Path('qa/math-ai-visuals/linear-programs-numerical.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print('PASS: LP conversion, pentagon supporting edge, classifier inequalities, cube optimum dimensions and vertex count.')
