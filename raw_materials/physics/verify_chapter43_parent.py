"""Independent chapter43 source-case calculations. This does not accept worker drafts."""
from pathlib import Path
import json,math,importlib.util
from PIL import Image
import pymupdf
ROOT=Path(__file__).resolve().parents[2]
Q=ROOT/'qa/physics/chapter43'
def close(value,expected,rel=3e-3):
 assert math.isclose(value,expected,rel_tol=rel,abs_tol=1e-13 if expected==0 else 0.0),(value,expected)
 return value
def main():
 result={};u=1.66e-27;c=2.998e8;ev=1.602176634e-19;year=3.156e7
 r=1.2e-15*56**(1/3);m=56*u;v=4*math.pi*r**3/3
 result['43.1']=dict(radius=close(r,4.59e-15),mass=close(m,9.296e-26),volume=close(v,4.053e-43),density=close(m/v,2.293e17),cube1cmMass=m/v*1e-6)
 de=2*2.7928*3.152e-8*2.30;f=de/4.136e-15
 result['43.2']=dict(energy_eV=close(de,4.049e-7),frequency=close(f,9.79e7),wavelength=close(c/f,3.06))
 mh=1.007825;mn=1.008665;ni=61.928345;free=28*mh+34*mn;dm=free-ni;eb=dm*931.5
 result['43.3']=dict(freeMass_u=free,massDefect_u=close(dm,.585365),binding_MeV=close(eb,545.3),bindingPerNucleon=close(eb/62,8.795))
 terms=[15.75*62,-17.80*62**(2/3),-.7100*28*27/62**(1/3),-23.69*(62-56)**2/62,39*62**(-4/3)]
 model=sum(terms);mass=free-model/931.5
 result['43.4']=dict(totalEnergyTerms_MeV=terms,binding_MeV=close(model,548.5),estimatedMass_u=close(mass,61.925,1e-5),relativeBindingError=(model/eb-1),sourcePrintedTotal=548.5)
 # Recoil shares energy and has the same momentum, not the same velocity.
 q=(226.025410-222.017578-4.002603)*931.5
 ka=q*222.017578/(222.017578+4.002603);kr=q-ka
 close(ka,4.785);close(kr,.0863,5e-3)
 assert math.isclose(ka*4.002603,kr*222.017578,rel_tol=1e-12)
 result['43.5']=dict(Q_MeV=q,alphaK_MeV=ka,recoilK_MeV=kr)
 qb=(59.933817-59.930786)*931.5
 result['43.6']=dict(neutralMassDifference_u=59.933817-59.930786,Q_MeV=close(qb,2.823));assert qb>0
 dmec=56.936291-56.935394;qec=dmec*931.5;qp=(dmec-.001097)*931.5
 assert qec>0 and qp<0
 result['43.7']=dict(massDifference_u=close(dmec,.000897),electronCaptureQ_MeV=qec,betaPlusQ_MeV=qp)
 half=272*86400;lam=math.log(2)/half;activity=2e-6*3.70e10;n=activity/lam;ratio=math.exp(-lam*year)
 result['43.8']=dict(halfLife_s=half,meanLife_s=half/math.log(2),lambda_s=lam,activity_Bq=activity,nuclei=close(n,2.51e12),activityAfterYear_microCi=close(2*ratio,.788,3e-3))
 lc=math.log(2)/(5730*year);n14=.255/lc;allc=6.022e23/12.011;frac=n14/allc;ratio=(174/3600)/(.5*.255);age=-math.log(ratio)/lc/year
 result['43.9']=dict(carbonFraction=close(frac,1.33e-12),carbonPercent=100*frac,initialDecaysPerHour=.5*.255*3600,activityRatio=ratio,age_years=close(age,8020))
 dose=.40e-3;energy=dose*1.2;photons=energy/(50e3*ev)
 result['43.10']=dict(equivalent_mrem=close(dose/1e-5,40),absorbed_mrad=close(dose/1e-5,40),absorbed_mGy=.4,energy_J=close(energy,4.8e-4),photons=close(photons,6e10),energyAtRBE20=energy/20)
 q1=(mh+7.016003-2*4.002603)*931.5;q2=(4.002603+14.003074-16.999132-mh)*931.5
 threshold=-q2*(1+4.002603/14.003074)
 result['43.11']=dict(exoQ_MeV=close(q1,17.35),endoQ_MeV=close(q2,-1.192),labThreshold_MeV=close(threshold,1.533))
 assert threshold>-q2
 ef=200e6*1.6e-19;rate=3000e6/ef;daily=rate*86400*235*1.66e-27
 result['43.12']=dict(fissionsPerSecond=rate,massPerSecond_kg=rate*235*u,massPerDay_kg=close(daily,3.2,2e-2),thermalPower_W=3e9)
 qfus=(2*2.014102-3.016049-mh)*931.5
 result['43.13']=dict(deltaMass_u=2*2.014102-3.016049-mh,Q_MeV=close(qfus,4.03),channel='D+D -> T+p, actual source Example43.13')
 result['selfchecks']=dict(volumeFactor=2,radiusMassFactor=2**3,PuToAmNRatio=(5*6560)/(4.45*7370),neutronAdvantage='No Coulomb repulsion',heavyFusionCounterexample='Must compare actual total binding, not fusion name alone')
 assert abs(result['selfchecks']['PuToAmNRatio']-1)<2e-4
 close(math.exp(-math.log(2)*2),.25)
 # Mathematical survival expectation and mean for exponential decay.
 from scipy.integrate import quad
 close(quad(lambda t:t*math.exp(-t),0,math.inf)[0],1,1e-10)
 spec=importlib.util.spec_from_file_location('parent_assets',ROOT/'scripts/prepare-physics43-parent-assets.py')
 assets=importlib.util.module_from_spec(spec);spec.loader.exec_module(assets)
 pixels=[]
 with pymupdf.open(assets.SOURCE) as pdf:
  for name,page,rect in assets.SPECS:
   fresh=pdf[page-1].get_pixmap(matrix=pymupdf.Matrix(3,3),clip=pymupdf.Rect(rect),alpha=False)
   with Image.open(assets.OUTPUT/name) as im:
    rgb=im.convert('RGB');assert rgb.size==(fresh.width,fresh.height) and rgb.tobytes()==fresh.samples,name
   pixels.append(dict(name=name,pdfPage=page,rect=rect,width=fresh.width,height=fresh.height,status='exact-RGB-match'))
 Q.mkdir(exist_ok=True)
 out=dict(status='passed',scope='Independent calculations for 13 actual source examples and five parent image crops, not full chapter acceptance',cases=result,images=pixels)
 (Q/'parent-numeric-and-pixels.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
 print(f'Passed{len(result)-1}actualsourceexamples,5RGBcrops,decay/recoil/threshold model identities.')
if __name__=='__main__':main()
