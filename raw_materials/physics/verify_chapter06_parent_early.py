"""Independent numerical and structural checks for Physics 1, exercises 6.1–6.49.

Inputs transcribed from visually inspected PDF pages 213–216 (printed 193–196).
No public content is written by this script.
"""
from pathlib import Path
import json
import math
import re
from scipy.integrate import quad

ROOT = Path(__file__).resolve().parents[2]
g = 9.80
sin = lambda deg: math.sin(math.radians(deg))
cos = lambda deg: math.cos(math.radians(deg))
r = {}
r['6.1'] = dict(push_J=2.4*1.5, friction_J=-.6*1.5, normal_J=0, gravity_J=0, net_J=(2.4-.6)*1.5)
r['6.2'] = dict(car_horizontal_J=1350*5000, car_inclined_J=1350*5000*cos(35), truck_horizontal_J=-1350*5000, truck_inclined_J=-1350*5000*cos(35), gravity_J=0)
r['6.3'] = dict(normal_N=30*g, push_N=.25*30*g, push_J=.25*30*g*4.5, friction_J=-.25*30*g*4.5, net_J=0)
F4=.25*30*g/(cos(30)-.25*sin(30))
r['6.4'] = dict(push_N=F4, normal_N=30*g+F4*sin(30), push_J=F4*4.5*cos(30), friction_J=-F4*4.5*cos(30), net_J=0)
r['6.5'] = dict(height_m=2.75*cos(30), gravity_J=-75*g*2.75*cos(30))
r['6.6'] = dict(one_tug_J=1.8e6*750*cos(14), total_J=2*1.8e6*750*cos(14))
r['6.7'] = dict(tension_N=12, friction_N=12, hanging_gravity_J=12*.75, hanging_tension_J=-12*.75, tabletop_tension_J=12*.75, tabletop_friction_J=-12*.75, net_each_J=0)
r['6.8'] = dict(work_J=30*(-9)+(-40)*(-3))
r['6.9'] = dict(direct_m=math.hypot(.4,.3), friction_N=4.8/math.hypot(.4,.3), broken_path_work_J=-4.8/math.hypot(.4,.3)*(.4+.3))
r['6.10'] = dict(normal_N=12*g*cos(53), friction_J=-.4*12*g*cos(53)*2, gravity_J=12*g*sin(53)*2, normal_J=0, net_J=12*g*2*(sin(53)-.4*cos(53)))
r['6.11'] = dict(angle_deg=0, force_factor=4)
r['6.12'] = dict(friction_N=10*g*sin(36.9), friction_J=10*g*sin(36.9)*5.5, gravity_J=-10*g*sin(36.9)*5.5, normal_J=0)
r['6.13'] = dict(angle_deg=173, work_J=48*12*cos(173), component_check_J=(-48*cos(61))*(12*sin(22))+(-48*sin(61))*(12*cos(22)))
r['6.14'] = dict(sx_m=48*cos(240), sy_m=48*sin(240), work_J=(-68)*48*cos(240)+36*48*sin(240))
r['6.15'] = dict(Fx_N=30*cos(37), Fy_N=30*sin(37), a_J=30*cos(37)*5, b_J=-30*sin(37)*6, c_J=-30*cos(37)*2+30*sin(37)*4)
r['6.16'] = dict(a_J=.5*1.5*(1.25**2-3.21**2), b_m_s=math.sqrt(1.25**2-2*.750/1.5), c_m_s=math.sqrt(1.25**2+2*.750/1.5))
r['6.17'] = dict(kinetic_J=.5*70*32**2, speed_double_factor=4)
r['6.18'] = dict(a_J=.5*.145*30**2, b_J=.5*.145*(30**2-20**2), difference_J=.5*.145*20**2)
r['6.19'] = dict(kinetic_J=.5*1.4e8*(12e3)**2, megaton_J=1e6*4.184e9, ratio=(.5*1.4e8*(12e3)**2)/(1e6*4.184e9))
r['6.20'] = dict(gravity_J=4.8*g*18, kinetic_J=4.8*g*18, speed_m_s=math.sqrt(2*g*18))
r['6.21'] = dict(time_half_work_factor=4)
r['6.22'] = dict(stop_m=5**2/(2*.220*g), speed_end_m_s=math.sqrt(5**2-2*.220*g*2.9), vertical_height_m=12**2/(2*g))
r['6.23'] = dict(formula='v_min = sqrt(2*g*h*(1+mu_k*cot(alpha)))', domain='h>=0, 0<alpha<=pi/2, mu_k>=0')
r['6.24'] = dict(launch_m_s=math.sqrt(25**2+2*g*15), maximum_height_m=15+25**2/(2*g))
r['6.25'] = dict(force_N=.5*12*(6**2-4**2)/2.5)
r['6.26'] = dict(distance_m=.5*.420*(6**2-2**2)/40)
r['6.27'] = dict(a_m_s=math.sqrt(2*36*1.2/4.3), b_m_s=math.sqrt(2*(36-.3*4.3*g)*1.2/4.3))
r['6.28'] = dict(height_m=1.35*sin(36.9), speed_m_s=math.sqrt(2*g*1.35*sin(36.9)))
r['6.29'] = dict(b_to_a_speed=2, final_to_initial_speed=math.sqrt((27-18)/27))
r['6.30'] = dict(work_J=.5*30*(5.62**2-3.9**2))
r['6.31'] = dict(formula='d=v0**2/(2*mu_k*g)', mu_double=.5, speed_double=4, both_double=2)
k32=2*12/.03**2
r['6.32'] = dict(k_N_m=k32, stretch_force_N=k32*.03, compression_J=.5*k32*.04**2, compression_force_N=k32*.04)
r['6.33'] = dict(bottom_tension_N=8.5*g, middle_tension_N=2*8.5*g, top_tension_N=3*8.5*g, bottom_length_m=.12+8.5*g/7800, middle_length_m=.12+2*8.5*g/7800, top_length_m=.12+3*8.5*g/7800)
r['6.34'] = dict(a_J=.5*8*10, b_J=.5*4*10, c_J=.5*12*10)
r['6.35'] = dict(a_m_s=math.sqrt(2*40/10), b_m_s=math.sqrt(2*60/10))
r['6.36'] = dict(extension_m=15/300, length_m=.240+15/300, work_J=.5*300*(15/300)**2)
r['6.37'] = dict(max_compression_m=3*math.sqrt(6/7500))
k38=2*80/.2**2
r['6.38'] = dict(combined_k_N_m=k38, a_force_N=k38*.2, b_additional_J=.5*k38*(.4**2-.2**2), b_max_force_N=k38*.4)
d39=.086
d_exact=(-.47*.1*g+math.sqrt((.47*.1*g)**2+20*.1*1.5**2))/20
dmax=.6*.1*g/20
r['6.39'] = dict(a_mu_s_rounded=20*d39/(.1*g), exact_stop_m=d_exact, a_mu_s_unrounded=20*d_exact/(.1*g), b_max_extension_m=dmax, b_max_initial_speed_m_s=math.sqrt(20*dmax**2/.1+2*.47*g*dmax))
r['6.40'] = dict(work_J=.5*200*.025**2, speed_m_s=math.sqrt(200*.025**2/4))
# E6.41 has area +2 J on 0..2, +2 J on 2..3, zero on 3..4,
# -1 J on 4..6, zero on 6..7. Reversing limits reverses the work.
r['6.41'] = dict(a_J=4, b_J=0, c_J=-1, d_J=3, e_J=-1)
r['6.42'] = dict(a_m_s=math.sqrt(2*4/2), b_m_s=math.sqrt(2*4/2), c_m_s=math.sqrt(2*3/2))
r['6.43'] = dict(k_N_m=4000, a_work_J=.5*4000*.375**2, b_work_J=.5*4000*(.375**2-.2**2), a_speed_m_s=math.sqrt(4000*.375**2/70), b_speed_m_s=math.sqrt(4000*(.375**2-.2**2)/70))
r['6.44'] = dict(compression_m=math.sqrt(2*.09*g*1.8*sin(40)/640), kinetic_J=.09*g*sin(40)*(1.8-.8))
r['6.45'] = dict(work_J=18*14-.530/2*14**2, speed_m_s=math.sqrt(2*(18*14-.530/2*14**2)/6))
r['6.46'] = dict(force_N=5.4*5, speed_m_s=2.8*5, power_W=5.4*5*2.8*5)
r['6.47'] = dict(energy_J=100*3600, speed_m_s=math.sqrt(2*100*3600/70))
r['6.48'] = dict(run_s=5/10*3600, walk_s=5/3*3600, run_J=700*5/10*3600, walk_J=290*5/3*3600, extra_walk_J=290*5/3*3600-700*5/10*3600)
bag_J=30*4.4482216152605*4*.3048
r['6.49'] = dict(work_per_bag_J=bag_J, power_W_per_bag_count=bag_J/300, power_hp_per_bag_count=bag_J/300/746, assumed_25_bags_W=25*bag_J/300, assumed_25_bags_hp=25*bag_J/300/746)

assert len(r)==49 and list(r)==[f'6.{i}' for i in range(1,50)]
assert math.isclose(r['6.13']['work_J'],r['6.13']['component_check_J'],abs_tol=1e-9)
assert r['6.14']['work_J'] > 0
assert r['6.15']['c_J'] > 0
assert math.isclose(F4*cos(30),.25*(30*g+F4*sin(30)),abs_tol=1e-10)
assert r['6.27']['b_m_s'] < r['6.27']['a_m_s']
assert r['6.39']['a_mu_s_unrounded']> .6
assert math.isclose(.5*.1*r['6.39']['b_max_initial_speed_m_s']**2,.5*20*dmax**2+.47*.1*g*dmax)
assert r['6.44']['compression_m'] < .8
assert math.isclose(r['6.41']['e_J'], -(2-1))

# Independent quadrature of visually transcribed graph segments checks the
# geometry-based work values, including the reversed limits in 6.41(e).
def fx34(x):
    return 1.25*x if x <= 8 else 2.5*(12-x)
def fx41(x):
    if x < 2: return x
    if x < 3: return 2.0
    if x < 4: return 0.0
    if x < 6: return -.5*(x-4)
    return 0.0
quadrature={}
for key,a,b in [('a',0,8),('b',8,12),('c',0,12)]:
    val=quad(fx34,a,b,points=[8] if a<8<b else None)[0]
    assert math.isclose(val,r['6.34'][key+'_J'],abs_tol=1e-10)
    quadrature['6.34'+key]=val
for key,a,b in [('a',0,3),('b',3,4),('c',4,7),('d',0,7),('e',7,2)]:
    points=[x for x in [2,3,4,6] if min(a,b)<x<max(a,b)]
    val=quad(fx41,a,b,points=points)[0]
    assert math.isclose(val,r['6.41'][key+'_J'],abs_tol=1e-10)
    quadrature['6.41'+key]=val
assert math.isclose(quad(lambda x:18-.530*x,0,14)[0],r['6.45']['work_J'])
for alpha in [10,25,45,80,90]:
    for mu in [0,.1,.7]:
        height=3.25
        distance=height/sin(alpha)
        speed=math.sqrt(2*g*height*(1+mu*cos(alpha)/sin(alpha)))
        assert math.isclose(.5*speed**2,g*height+mu*g*cos(alpha)*distance)

out={'source':{'pdf':'young-freedman-15.pdf','pdf_pages':[213,214,215,216],'printed_pages':[193,194,195,196]},'g_m_s2':g,'count':49,'results':r,'quadrature_crosschecks':quadrature,'parametric_energy_crosschecks':{'6.23':15},'assertions':'All passed'}
fragment=ROOT/'raw_materials/physics/translations/chapter-06/parent-11-bai-tap-001-049.md'
if fragment.exists():
    t=fragment.read_text(encoding='utf-8')
    ids=re.findall(r'^### 6\.(\d+)\b',t,re.M)
    out['fragment_checks']={'ids':[int(i) for i in ids], 'details_open':t.count('<details>'),'details_closed':t.count('</details>'),'literal_newline_sequences':t.count('\\n'),'bad_control_chars':[(i,ord(c)) for i,c in enumerate(t) if ord(c)<32 and c not in '\n\r\t']}
    if len(ids)==49:
        assert [int(i) for i in ids]==list(range(1,50))
        assert t.count('<details>')==t.count('</details>')==49
        assert t.count('Tóm tắt đề bài')==t.count('Hướng đi')==t.count('Lời giải')==49
        assert '\\n' not in t
        assert '<details open' not in t
        assert not out['fragment_checks']['bad_control_chars']
print(json.dumps(out,ensure_ascii=False,indent=2))
