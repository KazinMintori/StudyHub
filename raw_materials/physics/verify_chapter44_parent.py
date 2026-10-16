"""Independent source examples and parent crops, not whole-chapter acceptance."""
from pathlib import Path
import math,json,importlib.util
from PIL import Image
import pymupdf
ROOT=Path(__file__).resolve().parents[2];Q=ROOT/'qa/physics/chapter44'
def close(value,expected,rel=3e-3):
 assert math.isclose(value,expected,rel_tol=rel,abs_tol=1e-13 if expected==0 else 0.0),(value,expected)
 return value
def main():
 c=2.998e8;e=1.602e-19;h=6.626e-34;hb=h/(2*math.pi);mp=1.673e-27;data={}
 r=.5;b=1.5;v=e*b*r/mp;f=e*b/(2*math.pi*mp);k=.5*mp*v*v/e/1e6
 data['44.1']=dict(radius_m=r,B_T=b,frequency_Hz=close(f,23e6,1e-2),K_MeV=close(k,27,1e-2),beta=close(v/c,.24,1e-2))
 m=938.;pion=135.;kt=2*pion+pion*pion/(2*m);wm=2*m+pion
 assert math.isclose(wm**2,2*m*(kt+2*m),rel_tol=1e-12)
 data['44.2']=dict(protonRest_MeV=m,pionRest_MeV=pion,labThreshold_MeV=close(kt,280),colliderEachK_MeV=pion/2)
 data['44.3']={str(beam):dict(available_GeV=close(math.sqrt(2*.938*(beam+.938)),target),ultrarelApprox_GeV=math.sqrt(2*.938*beam)) for beam,target in [(800,38.7),(980,42.9)]}
 # Quantum number tuples are (Q/e,B,Le,Lmu,Ltau,S).
 particles={'p':(1,1,0,0,0,0),'n':(0,1,0,0,0,0),'ap':(-1,-1,0,0,0,0),'an':(0,-1,0,0,0,0),
 'ep':(1,0,-1,0,0,0),'em':(-1,0,1,0,0,0),'mup':(1,0,0,-1,0,0),'mum':(-1,0,0,1,0,0),
 'nue':(0,0,1,0,0,0),'anue':(0,0,-1,0,0,0),'numu':(0,0,0,1,0,0),'anumu':(0,0,0,-1,0,0),
 'pim':(-1,0,0,0,0,0),'pi0':(0,0,0,0,0,0)}
 def total(names):return tuple(sum(particles[name][i] for name in names) for i in range(6))
 lepton_cases=[(['mup'],['ep','nue','anumu'],True),(['pim'],['mum','anumu'],True),(['pi0'],['mum','ep','nue'],False)]
 vals=[]
 for before,after,expected in lepton_cases:
  a=total(before);b=total(after);ok=a[2:5]==b[2:5];assert ok==expected;vals.append(dict(before=a,after=b,leptonConserved=ok))
 data['44.4']=vals
 a=total(['n','p']);good=total(['n','p','p','ap']);bad=total(['n','p','an']);assert a[1]==good[1] and a[1]!=bad[1]
 data['44.5']=dict(beforeB=a[1],allowedAfterB=good[1],forbiddenAfterB=bad[1])
 data['44.6']=dict(finalRestBudget_MeV=4*m,beamTotal_MeV=7*m,beamK_MeV=close(6*m,5628),scope='p+p fixed target -> p+p+p+antip')
 # Valence quark charges, baryon numbers and strangeness, with antiparticle signs.
 quarks={'u':(2/3,1/3,0),'d':(-1/3,1/3,0),'s':(-1/3,1/3,-1)}
 def qsum(names):return tuple(sum((-1 if name.startswith('a') else 1)*quarks[name[-1]][i] for name in names) for i in range(3))
 sigma=qsum(['u','u','s']);alambda=qsum(['au','ad','as'])
 for actual,expected in zip(sigma,(1,1,-1)):close(actual,expected,1e-10)
 for actual,expected in zip(alambda,(0,-1,1)):close(actual,expected,1e-10)
 data['44.7']=dict(SigmaPlus_QBS=sigma,AntiLambda_QBS=alambda)
 ratio=414/393;beta=(ratio**2-1)/(ratio**2+1);rounded=(1.053**2-1)/(1.053**2+1)
 data['44.8']=dict(lambdaRatio=ratio,z=ratio-1,beta=beta,velocity_m_s=beta*c,velocityUsingSourceRoundedRatio=close(rounded*c,1.55e7,4e-3))
 rm=1.55e7/6.8e4
 data['44.9']=dict(sourceInputSpeed_m_s=1.55e7,sourceAssumedHubble_m_s_Mpc=6.8e4,distance_Mpc=rm,distance_pc=rm*1e6,distance_ly=rm*1e6*3.26)
 kev=8.617e-5;er=1.5*kev*290;es=1.5*kev*5800
 data['44.10']=dict(roomMean_eV=close(er,.0375),sunMean_eV=close(es,.75),roughTemperatures_K={str(value):value/1e-4 for value in [13.6,.511e6,938e6]},scope='3kT/2 is classical nonrel translational model; high-energy conversions are order-of-magnitude scales')
 nh=14-2;nhe=1;mh=nh;mhe=4*nhe;totalm=mh+mhe
 data['44.11']=dict(initialProtons=14,initialNeutrons=2,finalHydrogenNuclei=nh,finalHeliumNuclei=nhe,hydrogenMassFraction=close(mh/totalm,.75),heliumMassFraction=close(mhe/totalm,.25))
 scale=3000/2.725
 data['44.12']=dict(scaleRatio=close(scale,1100,1e-3),volumeRatio=scale**3,presentWien_m=2.9e-3/2.725,thenWien_m=2.9e-3/3000)
 G=6.674e-11;hbc=1.054571817e-34;cex=299792458.
 lp=math.sqrt(hbc*G/cex**3);tp=lp/cex;rhoc=3*(2.2e-18)**2/(8*math.pi*G)
 close(lp,1.616e-35);close(tp,5.39e-44);assert math.isclose(4.9+26.1+69,100,rel_tol=1e-14)
 linac_lambda=h*c/(50e9*e)
 close(linac_lambda/1e-15,.0248)
 six_tons_daily=6000/mp/(1e28*3.156e7)*86400
 close(six_tons_daily,1,2e-2)
 data['otherScales']=dict(PlanckLength_m=lp,PlanckTime_s=tp,sourceModelCriticalDensity_kg_m3=rhoc,sourceFractionsTotal=100,heuristicYukawaRange_fm=197.3/130,linac50GeV_deBroglie_fm=linac_lambda/1e-15,sixTonsProtonsDailyDecaysIfLifetime1e28y=six_tons_daily)
 spec=importlib.util.spec_from_file_location('parent_assets',ROOT/'scripts/prepare-physics44-parent-assets.py');assets=importlib.util.module_from_spec(spec);spec.loader.exec_module(assets)
 images=[]
 with pymupdf.open(assets.SOURCE) as pdf:
  for name,page,rect in assets.SPECS:
   fresh=pdf[page-1].get_pixmap(matrix=pymupdf.Matrix(3,3),clip=pymupdf.Rect(rect),alpha=False)
   with Image.open(assets.OUTPUT/name) as im:
    rgb=im.convert('RGB');assert rgb.size==(fresh.width,fresh.height) and rgb.tobytes()==fresh.samples,name
   images.append(dict(name=name,pdfPage=page,rect=rect,width=fresh.width,height=fresh.height,status='exact-RGB-match'))
 Q.mkdir(exist_ok=True)
 result=dict(status='passed',scope=f'12 actual source example cases and{len(images)} parent crops; does not accept whole chapter or worker drafts',cases=data,images=images)
 (Q/'parent-numeric-and-pixels.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
 print(f'Passed12sourceExamples,quantumnumbertotals,cosmologicalscalesand{len(images)}RGBcrops.')
if __name__=='__main__':main()
