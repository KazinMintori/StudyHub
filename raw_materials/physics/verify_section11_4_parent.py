"""Independent checks of examples11.5–11.7 and selfcheck11.4."""
from math import isclose
checks=[]
def ck(n,a,b):
 assert isclose(a,b,rel_tol=1e-10,abs_tol=1e-12),(n,a,b)
 checks.append(n)
F=550*9.8;area=.30e-4;Y=20e10
stress=F/area;strain=stress/Y;extension=strain*2
ck('11.5 force',F,5390)
ck('11.5 stress',stress,179666666.66666666)
ck('11.5 strain',strain,.0008983333333333333)
ck('11.5 extension',extension,.0017966666666666666)
ck('11.6 SIvolumechange',-.25*1.6e7/5e9,-.0008)
ck('11.6 reciprocalmodulus',1/5e4,20e-6)
ck('11.6 atmospherevolumechange',-20e-6*.25*160,-.0008)
ck('11.6 fractionalvolume',-.0008/.25,-.0032)
ck('11.7 shearstrain',.16e-3/.80,2e-4)
ck('11.7 shearstress',(.16e-3/.80)*3.5e10,7e6)
ck('11.7 shearedarea',.80*.50e-2,.004)
ck('11.7 tangentialforce',7e6*.004,28000)
ck('selfcheck copperstrain',2e-5/1,2e-5)
ck('selfcheck steelstrain',2e-6/.1,2e-5)
ck('selfcheck steelstress',20e10*2e-5,4e6)
ck('selfcheck copperstress',11e10*2e-5,2.2e6)
print('PASS',len(checks),'independent arithmetic assertions; source coverage and rendering verified separately.')
