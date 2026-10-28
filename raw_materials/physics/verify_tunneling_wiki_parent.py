"""Check the opaque-barrier approximation against exact rectangular-barrier transmission."""
import math
count=0
for ratio in[.1,.4,.5,.9]:
 G=16*ratio*(1-ratio)
 assert 0<G<=4
 for scaledWidth in[5.,8.,12.]:
  exact=1/(1+math.sinh(scaledWidth)**2/(4*ratio*(1-ratio)))
  approximate=G*math.exp(-2*scaledWidth)
  assert abs(approximate/exact-1)<.0001
  count+=1
print('PASS',count,'exact-versus-asymptotic assertions in the declared opaque rectangular-barrier domain.')
