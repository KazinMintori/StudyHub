"""Independent end-problem identities, source quantum-number tests and cosmological travel."""
from pathlib import Path
import math,json
import numpy as np
from scipy.integrate import quad
ROOT=Path(__file__).resolve().parents[2];Q=ROOT/'qa/physics/chapter44'
def main():
 data={};c=299792458.
 mk=493.7;mmu=105.7;s=mk/mmu
 beta=(s*s-1)/(s*s+1);gamma=1/math.sqrt(1-beta*beta)
 emu=(mk*mk+mmu*mmu)/(2*mk);enu=(mk*mk-mmu*mmu)/(2*mk)
 assert math.isclose(emu+enu,mk,rel_tol=1e-13)
 assert math.isclose(gamma*mmu,emu,rel_tol=1e-13) and math.isclose(gamma*mmu*beta,enu,rel_tol=1e-13)
 data['44.54']=dict(correctKaonValence='u anti-s, not u anti-d',massRatio=s,antimuonBeta=beta,antimuonEnergy_MeV=emu,neutrinoEnergy_MeV=enu)
 theta=math.pi/3;rdot=.001;cc=.00635;r0=500;seconds_year=3.156e7
 emission_time=4*seconds_year;re=r0+rdot*emission_time;distance=re*theta;separation_speed=rdot*theta;hub=rdot/re
 travel=(re/rdot)*math.expm1(theta*rdot/cc);arrival_radius=re+rdot*travel
 integral,error=quad(lambda t:cc/(re+rdot*t),0,travel,epsabs=1e-12)
 assert math.isclose(integral,theta,rel_tol=1e-12)
 assert math.isclose(separation_speed,hub*distance,rel_tol=1e-12)
 wavelength=1e-9*arrival_radius/re
 assert travel>distance/cc and wavelength>1e-9
 data['44.55']=dict(year_s=seconds_year,emissionTime_s=emission_time,emissionRadius_m=re,arcDistance_m=distance,separationSpeed_m_s=separation_speed,BubbleParameter_s=hub,flightTime_s=travel,flightTime_year=travel/seconds_year,arrivalTime_sinceCreation_s=emission_time+travel,arrivalRadius_m=arrival_radius,receivedWavelength_nm=wavelength/1e-9,integratedAngle=integral)
 # Check general source44.56 by a Lorentz boost, independently of its algebraic derivation.
 cases=[]
 for projectile_mass,target_mass,v0 in [(1,1,.2),(1,3,.8),(3,1,.9),(.1,9,.99),(20,.2,.999)]:
  g0=1/math.sqrt(1-v0*v0);em=projectile_mass*g0;plab=em*v0;elab=em+target_mass
  bcm=plab/elab;gcm=1/math.sqrt(1-bcm*bcm)
  vprime=(v0-bcm)/(1-v0*bcm);target_vprime=-bcm
  # Transform individual four-vectors and compare to invariant total energy.
  ep=gcm*(em-bcm*plab);pp=gcm*(plab-bcm*em)
  et=gcm*target_mass;pt=-gcm*bcm*target_mass
  expected=math.sqrt(projectile_mass**2+target_mass**2+2*target_mass*em)
  assert abs(pp+pt)<1e-10 and math.isclose(ep+et,expected,rel_tol=1e-11)
  assert math.isclose(pp/ep,vprime,rel_tol=1e-12) and math.isclose(pt/et,target_vprime,rel_tol=1e-12)
  cases.append(dict(m=projectile_mass,M=target_mass,v0_over_c=v0,vcm_over_c=bcm,CMenergy=ep+et))
 data['44.56']=dict(scope='Units c=1 for five independent Lorentz-boost cases; written proof still requires full algebra',cases=cases)
 # Source PET passage is a mathematical model, no clinical recommendation.
 arrival_difference=.06/c;percent=100*math.exp(-.1*20)
 assert arrival_difference<10e-9 and math.isclose(percent,13.53352832366127,rel_tol=1e-13)
 data['MCAT']=dict(photonEnergy_MeV=.511,arrivalDifference_ns=arrival_difference/1e-9,survivingPercent=percent)
 # Actual Lambda0 rest decay, keep relativistic two-body kinematics for the pion.
 parent=1116.;neutron=939.6;pion=135.
 en=(parent*parent+neutron*neutron-pion*pion)/(2*parent);epi=parent-en
 momentum=math.sqrt(en*en-neutron*neutron);kn=en-neutron;kpi=epi-pion;q=parent-neutron-pion
 assert math.isclose(epi*epi-momentum*momentum,pion*pion,rel_tol=1e-11)
 assert math.isclose(kn+kpi,q,rel_tol=1e-13)
 data['Bridge']=dict(parentRest_MeV=parent,neutronRest_MeV=neutron,pionRest_MeV=pion,neutronK_MeV=kn,pionK_MeV=kpi,neutronFraction=kn/q,pionFraction=kpi/q,sourceFigureScaleFactorRatio=.12,detectedPionDecayPhoton_MeV=(pion/2)*.12)
 assert abs(kn-5.78)<.02 and abs(kpi-35.62)<.02 and math.isclose((pion/2)*.12,8.1,rel_tol=1e-13)
 # Preserve deliberately forbidden reaction givens, including bars and the positron in44.23(d).
 # Tuple Le,Lmu,Ltau. Actual alternatives are not corrected into allowed decays.
 leptons={'mum':(0,1,0),'em':(1,0,0),'ep':(-1,0,0),'nue':(1,0,0),'anue':(-1,0,0),'numu':(0,1,0),'anumu':(0,-1,0),'taum':(0,0,1),'nutau':(0,0,1),'pip':(0,0,0),'gamma':(0,0,0),'n':(0,0,0),'p':(0,0,0)}
 def total(names):return tuple(sum(leptons[n][i] for n in names) for i in range(3))
 source=[(['mum'],['em','nue','anumu']),(['taum'],['em','anue','nutau']),(['pip'],['ep','gamma']),(['n'],['p','ep','anue'])]
 checks=[]
 for before,after in source:
  b=total(before);a=total(after);checks.append(dict(before=b,after=a,conserved=b==a))
 assert [x['conserved'] for x in checks]==[False,True,False,False]
 data['44.23']=checks
 # Actual44.25(d) is d cbar; Q/e=-1, B=0, S=0, C=-1.
 quarks={'u':(2/3,1/3,0,0),'d':(-1/3,1/3,0,0),'s':(-1/3,1/3,-1,0),'c':(2/3,1/3,0,1),'b':(-1/3,1/3,0,0)}
 def totals(names):return tuple(sum((-1 if n.startswith('a') else 1)*quarks[n[-1]][i] for n in names) for i in range(4))
 combinations=[['u','d','s'],['c','au'],['d','d','d'],['d','ac']]
 vals=[totals(x) for x in combinations]
 assert np.allclose(vals[-1],[-1,0,0,-1],atol=1e-13,rtol=0)
 data['44.25']=dict(combinations=combinations,quantumNumbers_QBSC=vals)
 Q.mkdir(exist_ok=True)
 (Q/'independent-end-numeric.json').write_text(json.dumps(dict(status='passed',scope='Selected source end problems and quantum-number alternatives; not whole85solution acceptance',cases=data),ensure_ascii=False,indent=2),encoding='utf-8')
 print('Passed kaon,expanding-universeflight,Lorentzboosts,PET,relativisticBridgeandactualreactionbars.')
if __name__=='__main__':main()
