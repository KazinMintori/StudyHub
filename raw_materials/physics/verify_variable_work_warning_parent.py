import math
from scipy.integrate import quad
for stiffness in[2.,17.]:
 for start,end in[(0,.3),(.3,.1),(-.2,0)]:
  forceWork=quad(lambda displacement:-stiffness*displacement,start,end)[0]
  expected=.5*stiffness*(start*start-end*end)
  assert math.isclose(forceWork,expected,rel_tol=1e-10,abs_tol=1e-12)
print('PASS6force-integral assertions including extension, return and compression-release signs.')
