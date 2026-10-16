"""Independent checks for draft chapter42 opening/summary, not release approval."""
from pathlib import Path
import json
import numpy as np
from scipy.integrate import quad
from scipy.constants import hbar,h,e,m_e,k
root=Path(__file__).resolve().parents[2]
rows={}
def close(label,a,b,rtol=1e-10,atol=0):
    assert np.allclose(a,b,rtol=rtol,atol=atol),(label,a,b)
close('Venus Celsius rounding',round(735-273.15),462)
close('Venus Fahrenheit rounding',round((735-273.15)*9/5+32),863)
rows['sourceOpening']=dict(kelvin=735,celsius=735-273.15,fahrenheit=(735-273.15)*9/5+32,co2Percent=96.5)
m1=2.326e-26;m2=2.656e-26;r=1.154e-10
mr=m1*m2/(m1+m2);I=mr*r*r
x1=m2*r/(m1+m2);x2=m1*r/(m1+m2)
close('reduced inertia equals explicit two masses',I,m1*x1*x1+m2*x2*x2)
close('center of mass',m1*x1,m2*x2)
rot=[l*(l+1)*hbar*hbar/(2*I) for l in range(3)]
close('rotational spacing relation',rot[2],3*rot[1])
rows['molecularSummary']=dict(reducedMass=mr,inertia=I,rotationalMEV=[v/e*1000 for v in rot])
N=1e23;V=1e-6
kF=(3*np.pi**2*N/V)**(1/3);EF=hbar*hbar*kF*kF/(2*m_e)
A=(2*m_e)**1.5*V/(2*np.pi**2*hbar**3)
count=A*EF**1.5*quad(lambda t:np.sqrt(t),0,1)[0]
Etot=A*EF**2.5*quad(lambda t:t**1.5,0,1)[0]
close('density of states includes two spins',count,N)
close('mean electron energy',Etot/N,3*EF/5)
close('Fermi wavevector relation',kF**3/(3*np.pi**2),N/V)
rows['freeElectronSummary']=dict(number=N,volumeM3=V,EFj=EF,meanEnergyJ=Etot/N,recoveredStates=count)
for T in [80,293,800]:
    f=lambda d:1/(np.exp(d/(k*T))+1)
    close('occupation at Fermi',f(0),.5)
    close('Fermi electron hole symmetry',f(k*T)+f(-k*T),1)
    assert f(k*T)<f(0)<f(-k*T)
    IS=1e-9
    close('diode zero-bias current',IS*np.expm1(0),0)
    assert IS*np.expm1(e*.05/(k*T))>0
rows['thermalSummary']=dict(checkedTemperaturesK=[80,293,800],fermiHalfOccupation=.5)
if __name__=='__main__':
    q=root/'qa/physics/chapter42';q.mkdir(exist_ok=True)
    (q/'parent-numeric.json').write_text(json.dumps(dict(status='passed',scope='Opening and summary draft only',results=rows),indent=2),encoding='utf-8')
    print('Chapter42draftopening/summarynumericandnormalizationcheckspassed.')
