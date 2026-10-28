import math
decayConstant=.2;halfLife=math.log(2)/decayConstant
for count in range(5):
 assert math.isclose(math.exp(-decayConstant*count*halfLife),2.**(-count),rel_tol=1e-12)
print('PASS5consecutive-half-life landmarks shown in Figure43.8.')
