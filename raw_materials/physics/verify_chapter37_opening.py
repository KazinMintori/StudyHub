"""Recompute chapter37 opening comparison from the stated velocities."""
from math import sqrt,isclose
import json

def gamma(beta):
 return 1/sqrt((1-beta)*(1+beta))

g1=gamma(.99000)
g2=gamma(.99995)
ratio=(g2-1)/(g1-1)
assert isclose(g1,7.088812050083354,rel_tol=1e-13)
assert isclose(g2,100.0012500234435,rel_tol=1e-11)
assert 16<ratio<16.4
print(json.dumps(dict(status='passed',beta1=.99000,beta2=.99995,gamma1=g1,gamma2=g2,kineticEnergyRatio=ratio,answer='v'),indent=2))
