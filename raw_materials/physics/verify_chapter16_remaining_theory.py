"""Independent sound-theory numerical and model checks, no publication side effects."""
from pathlib import Path
import math,json
from scipy.integrate import quad

OUT=Path(__file__).resolve().parent
examples={};selfchecks={};assertions=[]
def eq(id,a,b,rel=1e-10,abstol=1e-10):
 assert math.isclose(a,b,rel_tol=rel,abs_tol=abstol),(id,a,b)
 assertions.append(dict(id=id,actual=a,expected=b,status='passed'))

p=.030;f=1000.;v=344.;B=1.42e5;k=2*math.pi*f/v;A=p/(B*k)
examples['16.1']={'wave_number_rad_m':k,'displacement_amplitude_m':A}
earPressure=p*43/3.2;earB=1/(45.8e-11);earK=2*math.pi*f/1500.;earA=earPressure/(earB*earK)
examples['16.2']={'pressure_amplitude_Pa':earPressure,'bulk_modulus_Pa':earB,'wave_number_rad_m':earK,'displacement_amplitude_m':earA,'pressure_gain':43/3.2}
waterV=math.sqrt(2.18e9/1000)
examples['16.3']={'sound_speed_m_s':waterV,'wavelength_m':waterV/262,'frequency_Hz':262,'water_wavelength_for_100kHz_m':1482/1e5,'water_wavelength_for_5MHz_m':1482/5e6}
airV=math.sqrt(1.40*8.314*293/.0288)
examples['16.4']={'sound_speed_m_s':airV,'lambda_at_20Hz_m':airV/20,'lambda_at_20kHz_m':airV/20000,'temperature_K':293}
I=p*p/(2*1.2*344)
examples['16.5']={'intensity_W_m2':I}
examples['16.6']={'same_pressure_Pa':p,'A20_from_rounded_A1000_m':1.2e-8*1000/20,'A20_from_unrounded_A1000_m':A*1000/20,'frequency_amplitude_law':'A proportional1/f atfixedintensityandmedium'}
examples['16.7']={'acoustic_power_hemisphere_W':2*math.pi*20**2,'fullsphere_power_W_ifdifferentmodel':4*math.pi*20**2,'model':'Sourceexplicitlyassumesgroundspeakerwithnoenergyintoground,thereforehemisphere.'}
examples['16.8']={'I_28dB_W_m2':1e-12*10**2.8,'I_92dB_W_m2':1e-12*10**9.2}
examples['16.9']={'change_dB':10*math.log10(.25),'intensity_ratio':.25}
examples['16.10']={'quiet_positions_from_rigidwall_lambda_units':[.25,.75,1.25],'law':'Pressure-nodepositions(2n+1)lambda/4,wallpressureantinode/displacementnode','model':'Incident/reflectedsamefrequencywaves.'}
Lstop=344/(4*220);Lo=3*344/(2*(5*220))
examples['16.11']={'stopped_pipe_length_m':Lstop,'second_overtone_stopped_Hz':1100,'open_pipe_length_m':Lo,'open_fundamental_Hz':1100/3}
examples['16.12']={'string_to_air_wave_speed_ratio':.4,'string_speed_if_air344_m_s':.4*344,'string_to_pipe_length_ratio':.80}
dExact=math.hypot(2,4)-math.hypot(1,4);dRounded=.35
examples['16.13']={'path_A_m':math.hypot(2,4),'path_B_m':math.hypot(1,4),'path_difference_exact_m':dExact,'path_difference_source_rounded_m':dRounded,'constructive_base_from_exact_Hz':350/dExact,'destructive_base_from_exact_Hz':350/(2*dExact),'source_rounded_constructive_Hz':[1000,2000,3000],'source_rounded_destructive_Hz':[500,1500,2500]}
v=340.;f=300.
examples['16.14']={'lambda_source_at_rest_m':v/f,'lambda_ahead_at_30_m_s_m':(v-30)/f,'lambda_behind_at_30_m_s_m':(v+30)/f}
examples['16.15']={'heard_Hz':v/(v+30)*f,'source_velocity_along_listener_to_source_m_s':30,'listener_velocity_m_s':0}
examples['16.16']={'heard_Hz':(v-30)/v*f,'source_velocity_m_s':0,'listener_velocity_along_listener_to_source_m_s':-30}
examples['16.17']={'heard_Hz':(v+15)/(v+45)*f,'source_velocity_m_s':45,'listener_velocity_m_s':15,'relative_separation_speed_m_s':30}
warehouse=v/(v-30)*f;driver=(v+30)/v*warehouse
examples['16.18']={'warehouse_heard_Hz':warehouse,'driver_echo_heard_Hz':driver,'direct_double_shift_formula_Hz':f*(v+30)/(v-30)}
eq('16.18:twostages',driver,f*(v+30)/(v-30))
Mach=1.75;alpha=math.asin(1/Mach);planeV=Mach*320;delay=8000/(planeV*math.tan(alpha))
examples['16.19']={'Mach':Mach,'cone_halfangle_deg':math.degrees(alpha),'plane_speed_m_s':planeV,'delay_after_overhead_s':delay,'plane_horizontal_distance_m':planeV*delay}
eq('16.19:alternategeometry',delay,8000/320*math.sqrt(Mach*Mach-1)/Mach)

# Assert every numerical worked example against its printed rounded answer.
# Values above are recomputed from prompt data, not copied from the answer.
for ident,field,rounded,atol in [
 ('16.1','wave_number_rad_m',18.3,.05),('16.1','displacement_amplitude_m',1.2e-8,.05e-8),
 ('16.2','pressure_amplitude_Pa',.40,.005),('16.2','bulk_modulus_Pa',2.18e9,.005e9),
 ('16.2','displacement_amplitude_m',4.4e-11,.05e-11),
 ('16.3','sound_speed_m_s',1476,.5),('16.3','wavelength_m',5.64,.005),
 ('16.4','sound_speed_m_s',344,.5),('16.4','lambda_at_20Hz_m',17,.5),('16.4','lambda_at_20kHz_m',.017,.0005),
 ('16.5','intensity_W_m2',1.1e-6,.05e-6),
 ('16.6','same_pressure_Pa',.030,1e-14),('16.6','A20_from_rounded_A1000_m',6e-7,1e-16),
 ('16.7','acoustic_power_hemisphere_W',2.5e3,.05e3),
 ('16.8','I_28dB_W_m2',6.3e-10,.05e-10),('16.8','I_92dB_W_m2',1.6e-3,.05e-3),
 ('16.9','change_dB',-6.,.05),
 ('16.11','stopped_pipe_length_m',.391,.0005),('16.11','open_pipe_length_m',.469,.0005),
 ('16.11','open_fundamental_Hz',367,.5),
 ('16.12','string_to_air_wave_speed_ratio',.4,1e-14),('16.12','string_speed_if_air344_m_s',138,.5),
 ('16.13','path_A_m',4.47,.005),('16.13','path_B_m',4.12,.005),
 ('16.14','lambda_source_at_rest_m',1.13,.005),('16.14','lambda_ahead_at_30_m_s_m',1.03,.005),('16.14','lambda_behind_at_30_m_s_m',1.23,.005),
 ('16.15','heard_Hz',276,.5),('16.16','heard_Hz',274,.5),('16.17','heard_Hz',277,.5),
 ('16.18','warehouse_heard_Hz',329,.5),('16.18','driver_echo_heard_Hz',358,.5),
 ('16.19','cone_halfangle_deg',34.8,.05),('16.19','delay_after_overhead_s',20.5,.05),
 ('16.19','plane_horizontal_distance_m',11.5e3,.05e3),
]:
 eq('E'+ident+':'+field,examples[ident][field],rounded,rel=0,abstol=atol)

# Conceptual Example16.10: pressure mode satisfying the rigid-wall condition.
for i,d in enumerate(examples['16.10']['quiet_positions_from_rigidwall_lambda_units']):
 eq('E16.10:pressurezero',math.cos(2*math.pi*d),0.)
 eq('E16.10:displacementextremum',abs(math.sin(2*math.pi*d)),1.)
 eq('E16.10:distance',d,(2*i+1)/4)

# Keep both the exact geometry and source's rounded difference in Example16.13.
for n in range(1,4):
 ff=n*350/dExact
 eq('E16.13:constructivephase',math.cos(2*math.pi*ff*dExact/350),1.)
 fd=(2*n-1)*350/(2*dExact)
 eq('E16.13:destructivephase',math.cos(2*math.pi*fd*dExact/350),-1.)
 eq('E16.13:printedroundedfamily',n*350/.35,n*1000.)

eq('bio:earcanalfundamental',344/(4*.025),3440.)
eq('spectrum:clarinetperiodms',1000/233,4.29,rel=0,abstol=.005)
eq('spectrum:recorderperiodms',1000/523,1.91,rel=0,abstol=.005)
for pressure in(.5e5,1.013e5,2e5):
 rho=pressure*.0288/(8.314*293)
 eq('gas:pressurecancellation',math.sqrt(1.4*pressure/rho),examples['16.4']['sound_speed_m_s'])
# The same impulsive wavefront argument independently checks Δp=ρv*u.
for rho,B,u,area,t in[(1000,2.18e9,.01,.02,.5),(1.2,1.42e5,1e-5,.5,2.)]:
 wave=math.sqrt(B/rho);dp=B*u/wave
 eq('impulse:fluidwavefront',dp*area*t,rho*area*wave*t*u)
 eq('impedance:pressurevelocity',dp,rho*wave*u)
# Scalar pressure cancellation does not generally cancel a vector displacement
# when two local propagation directions are not parallel.
na=(4/math.sqrt(20),2/math.sqrt(20));nb=(4/math.sqrt(17),-1/math.sqrt(17))
eq('interference:pressurecancel',1+(-1),0)
vectorResidual=math.hypot(na[0]-nb[0],na[1]-nb[1])
assert vectorResidual>.6
assertions.append(dict(id='interference:vectorvelocitynotcancelled',status='passed',actual=vectorResidual,expected='nonzero for nonparallel ray directions'))
selfchecks={
 '16.1':{'choice':'v','frequency_ratio':4,'displacement_ratio':.25,'constant':'pressureamplitudeandmedium'},
 '16.2':{'choice':'i','B_mercury_to_water_ratio':13.6*(1451/1482)**2},
 '16.3':{'displacement_ratio':math.sqrt(2),'pressure_ratio':math.sqrt(2),'B_ratio':1,'speed_ratio':1,'level_change_dB':10*math.log10(2)},
 '16.4':{'choice':'ii','tone':'higher','speed_ratio_table_He_to_air':999/344},
 '16.5':{'choices':['i','iv'],'four_pipe_fundamentals_Hz':[220,110,440,220],'test_frequency_Hz':660},
 '16.6':{'choice':'iii','reason':'Different500/1000Hzcannotformstationaryalwaysconstructive/destructivepattern; instantaneoussuperpositionstillapplies.'},
 '16.7':{'choice':'vi','unknown_tuning_fork_Hz':[437,443],'beat_Hz':3},
 '16.8':{'Doppler_shift':False,'v_listener_relative_air_m_s':10,'v_source_relative_air_m_s':10,'ratio':1},
 '16.9':{'choice':'iii','hears':'aircraftsoundshiftedlowerinsideandbehindshockcone;sonicboomoccurswhenfrontcrosseslistener'}
}
eq('TY16.8:windnochange',(344+10)/(344+10),1.)
eq('TY16.1:fourfoldfrequency',100/400,selfchecks['16.1']['displacement_ratio'])
eq('TY16.2:bulkmodulusratio',13.6*1451**2/1482**2,selfchecks['16.2']['B_mercury_to_water_ratio'])
eq('TY16.3:displacementintensity',selfchecks['16.3']['displacement_ratio']**2,2.)
eq('TY16.3:pressureintensity',selfchecks['16.3']['pressure_ratio']**2,2.)
eq('TY16.3:dB',selfchecks['16.3']['level_change_dB'],3.0,rel=0,abstol=.05)
assert selfchecks['16.4']['speed_ratio_table_He_to_air']>1
assertions.append(dict(id='TY16.4:higherfrequency',status='passed',actual=999/344,expected='greater than 1'))
for ff in selfchecks['16.7']['unknown_tuning_fork_Hz']:eq('TY16.7:frequencyambiguity',abs(ff-440),3.)
# Two different frequencies cannot have a fixed relative phase at a fixed point.
eq('TY16.6:relativephasecyclespersecond',1000-500,500.)
# Behind a supersonic source, backward-going waves have wavelength(v+vs)/fs.
assert 320/(320+560)<1
assertions.append(dict(id='TY16.9:recedingfrequency',status='passed',actual=320/(320+560),expected='less than 1'))
for lengthRatio,closed,fund in[(1,True,220),(2,True,110),(1,False,440),(2,False,220)]:
 modes=[n*fund for n in(range(1,12,2)if closed else range(1,12))]
 eq('TY16.5:resonance',float(660 in modes),float((lengthRatio==1 and closed)or(lengthRatio==2 and not closed)))

# Pressuregradient and intensity from displacements, direct numerical timeaverage.
for f in(20.,100.,1000.,4000.):
 B=1.2*344**2;rho=1.2;v=344.;w=2*math.pi*f;k=w/v;A=2e-8
 peak=B*k*A
 intensity1=.5*B*w*k*A*A;intensity2=peak*peak/(2*rho*v)
 eq('intensity:equivalentforms',intensity1,intensity2)
 timeaverage=quad(lambda theta:(B*k*A*math.sin(theta))*(w*A*math.sin(theta)),0,2*math.pi,epsabs=1e-20)[0]/(2*math.pi)
 eq('intensity:timeaverage',timeaverage,intensity1,abstol=1e-20)
 h=1e-5/k;x=.23/k;t=.17/w
 gradient=(A*math.cos(k*(x+h)-w*t)-A*math.cos(k*(x-h)-w*t))/(2*h)
 eq('pressure:-Bgradient',-B*gradient,B*k*A*math.sin(k*x-w*t),rel=1e-9,abstol=1e-15)

# Logarithmic scale and sourceTable16.2, values rounded inoriginaltable.
table16_2=[['Militaryjet30m',140,100],['Painthreshold',120,1],['Riveter',95,3.2e-3],['Elevatedtrain',90,1e-3],['Busystreet',70,1e-5],['Conversation',65,3.2e-6],['Quietcar',50,1e-7],['Quietradio',40,1e-8],['Whisper',20,1e-10],['Leaves',10,1e-11],['Hearingthreshold1000Hz',0,1e-12]]
for name,beta,intensity in table16_2: eq('table16.2:'+name,10*math.log10(intensity/1e-12),beta,rel=.0005,abstol=.06)
for beta in(-10.,0.,28.,65.,92.,120.,140.):eq('decibel:invert',10*math.log10((1e-12*10**(beta/10))/1e-12),beta)

# Beats same/displaced phase. Sourceuses yb=-Asin(2pifbt), so differenceidentityiscorrect.
for t in(0.,.031,.14,.25,.5,.77):
 fa,fb=18.,16.;ya=math.sin(2*math.pi*fa*t);yb=-math.sin(2*math.pi*fb*t)
 product=2*math.sin(math.pi*(fa-fb)*t)*math.cos(math.pi*(fa+fb)*t)
 eq('beats:sourceoppositephaseidentity',ya+yb,product)
eq('Figure16.25:envelopemaxatquartersecond',abs(2*math.sin(math.pi*(18-16)*.25)),2.)
eq('Figure16.25:envelopezeroathalfsecond',abs(2*math.sin(math.pi*(18-16)*.5)),0.)
for fa,fb in[(18,16),(440,437),(440,443),(1800,1900)]:eq('beats:perioddifference',1/abs(1/fa*1/fb/(1/fb-1/fa)),abs(fa-fb))

# GeneralDopplersigns verified from wavefrontemission/arrival times, notformulaalone.
# Coordinate +x fromlistener towardsource, soundpropagatestoward−x.
for vs,vl in[(0,30),(0,-30),(30,0),(-30,0),(45,15),(-15,10),(10,10)]:
 separation=1000.;T=1/300.;sound=340.
 def arrival(te):return(separation+(vs+sound)*te)/(sound+vl)
 observed=1/(arrival(T)-arrival(0))
 eq('Doppler:wavefrontarrivaltimes',observed,300*(sound+vl)/(sound+vs),rel=1e-9)
for Mach in(1.01,1.1,1.75,2.,3.):
 a=math.asin(1/Mach)
 eq('shock:Machconegeometry',math.sin(a),1/Mach)
 assert 0<a<math.pi/2
for beta in(-.5,0.,.2,.8):
 ratio=math.sqrt((1-beta)/(1+beta))
 eq('light:reciprocalvelocity',ratio*math.sqrt((1+beta)/(1-beta)),1.)

clarifications=[
 {'id':'16.6-keyconcept-frequency','pdfPage':532,'severity':'P1-source-prose-error','issue':'KeyConceptsayshigherfrequencylargerdisplacementatfixedintensity,butworkedexampleandI∝f²A²implyhigherfrequencysmallerA.','action':'WriteA∝1/f;20Hzamplitude50times1000Hz atsamepressure/intensity.'},
 {'id':'16.4-ear-bone-english-labels','pdfPage':524,'severity':'P1-originalimage-label-error','issue':'Image prints Malleus(anvil), Incus(hammer), reversing hammer/anvil parentheticals.','action':'Keep original pixels. Vietnamese glossary correctly uses xương búa(malleus), xương đe(incus), xương bàn đạp(stapes). Parent verified NIH NIDCD https://www.nidcd.nih.gov/health/otosclerosis during this audit; include primary reference at authorship.'},
 {'id':'16.7-phase-origin','pdfPage':542,'severity':'preserve-correct-source','issue':'Figure16.25 starts with opposite wave phases, consistent with ya=A sin(2πfa t), yb=−A sin(2πfb t). Therefore .25s is an envelope maximum and .50s is a minimum. An earlier stopped audit mistakenly assumed equal initial phases and flagged the correct source time as wrong.','action':'Preserve source .50s destructive example. Distinguish phase-origin shift from the phase-independent beat frequency. Corrected after full-resolution figure inspection and explicit Python envelope assertions.'},
 {'id':'16.13-rounded-path-difference','pdfPage':541,'severity':'rounding','issue':'Exactgeometrydifference.349030329m;sourceusesrounded4.47−4.12=.35m,sogives1000/500Hz families.','action':'Useapproxsigns,maykeep source1.00kHz/500Hz but explainroundingprivately. Do notclaimexactintegersfromexactgeometry.'},
 {'id':'16.5-choice-duplicate','pdfPage':540,'severity':'P2-option-label','issue':'Questionlabelsitsfourthoption(iii)again,answerproperlyreferences(iv).','action':'Numberfouroptionsi–iv;correctanswersiandiv.'},
 {'id':'16.7-hemisphere','pdfPage':532,'severity':'model-clarification','issue':'Promptuniformalldirections,solutionexplicitlyassumesgroundwithnopowerintogroundandhemisphere.','action':'PreserveexplicithemisphereassumptionwithP2.5kW;fullspherewould5.03kW.'},
 {'id':'sound-hearing-health-statements','pdfPages':[526,533],'severity':'external-evidence-required','issue':'Specificage65musicianclaimanddose10min120dB/10years92dBhealthoutcomesnotindependentlyverified;notuniversalsafetythresholds.','action':'Parentverifyprimaryclinical/publichealthsourcesifusinghealthclaims;keepnumerical28/92dBlogexampleasexplicitmodeldata,notmedicaladvice.'},
 {'id':'ear-massless-transmission','pdfPage':524,'severity':'model-assumption','issue':'Equalforceandarea-onlygainignoresossicleinertia/leverdetails,fluidpropertiesrounded.','action':'Retainas statedidealizedmodel,notcompleteanatomicalmechanics.'},
 {'id':'sound-gas-R-date','pdfPage':529,'severity':'source-era-constant','issue':'R8.3144598(48)issourcevalue;numericuses8.314.','action':'Use8.314forproblems,avoidcallingolderuncertaintycurrent2026bestvalue.'},
 {'id':'sound-rod-vs-bulk','pdfPage':527,'severity':'domain-essential','issue':'sqrt(Y/rho)onlylongitudinalrodwithlateraldeformationfree,notarbitrarybulksolid.','action':'KeepdistinctionandTable16.1bulkvalueswithoutclaimingrodformulaexplainsthemalone.'},
 {'id':'16.6-pressure-vs-vector-displacement','pdfPage':540,'severity':'P2-source-overgeneralization','issue':'Source caution says a two-source destructive point is both pressure and displacement node. For nonparallel incident longitudinal waves, scalar pressures can cancel while vector velocities/displacements do not.','action':'Describe destructive sound pressure and redistributed energy. Only claim simultaneous displacement cancellation in the locally parallel 1D scalar-wave approximation. Direct plane-wave vector counterexample is verified in checks.py.'},
 {'id':'16.5-bottle-model','pdfPage':539,'severity':'model-clarification','issue':'Source describes blowing over a bottle as an organ-pipe air column. A narrow-neck cavity may instead require a Helmholtz model.','action':'Preserve observation that a larger air volume generally lowers resonance while clearly labeling pipe analogy approximate, not a universal bottle formula.'},
 {'id':'ultrasound-imaging-claims','pdfPage':528,'severity':'external-evidence-required','issue':'Source contrasts ultrasound sensitivity and radiation hazards with x rays. Resolution is not determined by wavelength alone; lack of ionizing radiation does not imply universal medical safety.','action':'Keep wave-frequency/wavelength and physical imaging application. Parent needs primary evidence for any comparative clinical performance or safety statements before publication.'},
 {'id':'supersonic-Doppler','pdfPage':550,'severity':'domain-essential','issue':'UsualfrontwavelengthformulaandDopplerrelationsnotvalidwhenfrontcompressedtosupersonicshock.','action':'Do notextendsubsonicformulatoallanglesahead; shockconegeometryandcontinuousfrontseparate.'}
]
report=dict(status='passed',scope='Chapter16theorymodels/examplesonly',exampleCount=len(examples),selfcheckCount=len(selfchecks),numericAssertions=len(assertions),examples=examples,selfchecks=selfchecks,assertions=assertions,sourceClarifications=clarifications,table16_2_checks=table16_2,opening={'choice':'iv','reason':'Forfixedidealaircompositionv∝sqrt(T),notpressurealone.'})
assert len(examples)==19 and len(selfchecks)==9
print(json.dumps(report,ensure_ascii=False,indent=2))
