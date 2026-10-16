"""Independent source-sensitive arithmetic for draft chapter42; no release acceptance."""
from pathlib import Path
import json
import numpy as np
from scipy.constants import h,hbar,c,e,m_e,k,epsilon_0,Avogadro
from scipy.integrate import quad
root=Path(__file__).resolve().parents[2]
rows={};checks=0
def close(label,a,b,rtol=1e-10,atol=0):
    global checks
    assert np.allclose(a,b,rtol=rtol,atol=atol),(label,a,b)
    checks+=1
def record(label,**data):rows[label]=data

# Source distinguishes the ionic point-charge approximation from the molecular
# potential minimum and the energy cost of creating separated ions.
Uc=-e*e/(4*np.pi*epsilon_0*.24e-9)/e
binding=5.7-1.525
close('source binding rounding',round(binding,1),4.2)
assert -6.01<Uc<-5.99
record('42.1',pointChargeEV=Uc,molecularMinimumEV=-5.7,sourceIonCreationEV=1.525,
       molecularBindingEV=binding,notPointChargeMinusCost=abs(Uc)-1.525)

mC=1.993e-26;mO=2.656e-26;rCO=.1128e-9
mu=mC*mO/(mC+mO);I=mu*rCO*rCO
rot=np.array([l*(l+1)*hbar*hbar/(2*I)/e for l in range(3)])
close('rotor first intervals',rot[2]-rot[1],2*(rot[1]-rot[0]))
record('42.2',reducedMass=mu,inertia=I,energiesMEV=(1000*rot).tolist(),
       emittedWavelengthM=h*c/((rot[2]-rot[1])*e))
ph=np.array([.2690-.000479,.2690+.000479])
record('42.3',sourceVibrationalEV=.2690,sourceRotationalIncreaseEV=.000479,
       photonEV=ph.tolist(),wavelengthMicrometres=(h*c/(ph*e)*1e6).tolist())
close('ro-vibration energy accounting',ph.sum(),2*.2690)
ln2=quad(lambda x:1/(1+x),0,1)[0]
close('alternating Coulomb sum',ln2,np.log(2))
record('42.4',alternatingSum=ln2,taggedIonCoefficient=2*ln2,
       totalPairEnergyPerIonCoefficient=ln2,mechanicalEquilibriumNotEstablishedBySignAlone=True)
record('42.5',germaniumGapEV=.67,maximumWavelengthM=h*c/(.67*e))
for T in [80,300,800]:
    offsets=k*T*np.log(np.array([99,1/99]))
    occ=1/(np.exp(offsets/(k*T))+1)
    close('actual Example42.6 occupations',occ,[.01,.99])
record('42.6',energyOffsetsInKT=[float(np.log(99)),float(-np.log(99))])

n=8.45e28
EF=hbar*hbar/(2*m_e)*(3*np.pi*np.pi*n)**(2/3)
coefficient=(2*m_e)**1.5/(2*np.pi*np.pi*hbar**3)
recovered=coefficient*EF**1.5*quad(lambda x:np.sqrt(x),0,1)[0]
close('DOS includes factor2 from energy integral',recovered,n)
mean=coefficient*EF**2.5*quad(lambda x:x**1.5,0,1)[0]/n
close('mean kinetic energy',mean,3*EF/5)
record('42.7',density=n,EFj=EF,EFeV=EF/e,fermiSpeed=np.sqrt(2*EF/m_e),
       recoveredDensity=recovered)
record('42.8',meanEV=mean/e,classicalMeanEV=1.5*k*293/e,
       classicalRmsSpeed=np.sqrt(3*k*293/m_e))
probability={}
for Eg in [.200,1.00,5.00]:
    vals=[1/(np.exp(Eg*e/(2*k*T))+1) for T in [300,310]]
    assert 0<vals[0]<vals[1]<.5
    probability[str(Eg)]=dict(probabilities=vals,ratio=vals[1]/vals[0])
record('42.9',gaps=probability,assumption='Fermi level exactly at midgap')

# Actual source junction geometry: p on the left, n on the right.
eps=11.7*epsilon_0;NA=1e16*1e6;ND=5e16*1e6;an=55e-9
ap=ND*an/NA;peak=e*ND*an/eps;barrier=peak*(ap+an)/2
close('junction neutrality',NA*ap,ND*an)
Ep=lambda x:-e*NA*(x+ap)/eps
En=lambda x:e*ND*(x-an)/eps
close('electric field continuity',Ep(0),En(0))
Vp=lambda x:e*NA*(x+ap)**2/(2*eps)
Vn=lambda x:Vp(0)+e*ND*(an*x-x*x/2)/eps
close('barrier from both independent constructions',Vn(an),barrier)
close('p-side field boundary',Ep(-ap),0,atol=1e-7)
close('n-side field boundary',En(an),0,atol=1e-7)
record('42.50',acceptorDensity=NA,donorDensity=ND,pDepthM=ap,nDepthM=an,
       fieldPeakVPerM=peak,barrierV=barrier)

u=1.6605e-27;MO=16*u;MC=12*u;spring=1860
Meff=MC*MO/(MC+2*MO);w=np.sqrt(spring/Meff)
# Direct mass-weighted eigensystem independently checks the antisymmetric mode.
K=spring*np.array([[1,-1,0],[-1,2,-1],[0,-1,1]],float)
M=np.diag([MO,MC,MO]);vector=np.array([1,-2*MO/MC,1])
close('CO2 mode satisfies all three Newton equations',K@vector,w*w*M@vector,atol=1e-11)
record('42.51',effectiveMass=Meff,angularFrequency=w,frequency=w/(2*np.pi))

# Keep the exact h,c values specifically requested for five-significant-figure
# photons. The data identify an inertia close to N2, but do not establish an
# allowed electric-dipole absorption spectrum for a homonuclear molecule.
hp=4.1357e-15;cp=2.9979e8
lam=np.array([4.2680,4.2753,4.2826,4.2972,4.3046])*1e-6
E=hp*cp/lam
gap=E[2]-E[3];Iobs=2*hbar*hbar/(gap*e)
hv=(E[2]+E[3])/2
candidates={'N2':(14,14,110),'CO':(12,16,118),'NO':(14,16,115)}
Icand={name:(a*b/(a+b))*u*(pm*1e-12)**2 for name,(a,b,pm) in candidates.items()}
best=min(Icand,key=lambda name:abs(Icand[name]-Iobs))
assert best=='N2'
record('42.52',photonEnergiesEV=E.tolist(),inferredVibrationEV=hv,inferredInertia=Iobs,
       candidateInertias=Icand,inertiaMatch=best,forceConstant=7*u*(hv*e/hbar)**2,
       physicalCaveat='Homonuclear N2 has no permanent electric dipole; line-position matching alone does not validate the stipulated ordinary dipole absorption model.')
p=2*n*EF/5;B=5*p/3
V=1.;N=n*V
energy=lambda volume:3*N/5*(hbar*hbar/(2*m_e))*(3*np.pi*np.pi*N/volume)**(2/3)
step=1e-5
close('pressure from energy derivative',-(energy(V+step)-energy(V-step))/(2*step),p,rtol=1e-9)
record('42.53-54',pressurePa=p,bulkModulusPa=B,measuredBulkModulusPa=1.4e11,
       electronFraction=B/1.4e11)
thresholdEF=.01*m_e*c*c
nlimit=(2*m_e*thresholdEF/hbar**2)**1.5/(3*np.pi*np.pi)
whiteN=6*(2e30/(1.99e-26))/(4*np.pi*(6000e3)**3/3)
record('42.55',relativityThresholdDensity=nlimit,copperDensity=n,
       whiteDwarfDensity=whiteN,whiteDwarfBeyondThreshold=bool(whiteN>nlimit))
assert n<nlimit<whiteN

muHF=1.67e-27*3.15e-26/(1.67e-27+3.15e-26);IHF=muHF*(.092e-9)**2
photon=(h*1.24e14-hbar*hbar/IHF)/e
delta=photon-.230
occupation=1/(np.exp((photon-.115)*e/(k*80))+1)
assert delta>0 and 0<occupation<1e-24
record('Bridge',reducedMass=muHF,inertia=IHF,photonEV=photon,aboveConductionEdgeEV=delta,
       occupancy=occupation,printedAnswerOccupancy=1.74e-25,
       caveat='Use computed inputs without forcing rounded printed answer or assuming high optical efficiency.')
if __name__=='__main__':
    out=root/'qa/physics/chapter42/independent-numeric.json'
    out.write_text(json.dumps(dict(status='passed',scope='Selected draft source cases only; not all95solutions or source acceptance',checks=checks,results=rows),ensure_ascii=False,indent=2),encoding='utf-8')
    print('Computed',len(rows),'source-sensitive cases;',checks,'independent equalities. Draft only.')
