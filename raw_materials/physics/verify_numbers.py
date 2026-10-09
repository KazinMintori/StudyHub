"""Tính lại dữ kiện của hai môn Vật lý theo Young & Freedman, ấn bản 15.

Chạy từ gốc repo: python -I raw_materials/physics/verify_numbers.py
Mỗi khóa cNN là chương nguồn; các giá trị được dùng trong ví dụ và bài tập.
"""
from math import pi, sqrt, sin, cos, asin, log, exp, radians
import json

g, R, k = 9.8, 8.314, 9e9
h, c, e, me = 6.62607015e-34, 299792458, 1.602176634e-19, 9.1093837e-31
eps0, mu0, kb = 8.8541878128e-12, 1.25663706212e-6, 1.380649e-23

def calculate():
    n = {}
    def put(ch, **values):
        n[f'c{ch:02}'] = values
    put(1, speed=72/3.6, norm=sqrt(3**2+4**2), dot=3*4+4*(-3))
    put(2, x=2*3+0.5*4*3**2, v=2+4*3, stop=20**2/(2*5), fall=sqrt(2*19.6/g))
    put(3, time=2*20*sin(radians(30))/g, range=20**2*sin(radians(60))/g, height=(20*sin(radians(30)))**2/(2*g), centripetal=10**2/20)
    put(4, a=(10-2)/2, weight=2*g, normal=2*g, elevator=60*(g+2))
    put(5, friction=0.2*2*g, a=(10-0.2*2*g)/2, min_mu=10**2/(50*g), incline=g*sin(radians(30)))
    put(6, work=10*3*cos(radians(60)), v=sqrt(2*15/2), spring_work=0.5*200*0.1**2, power=100*2)
    put(7, v=sqrt(2*g*5), spring=sqrt(2*2*g*0.1/200), final=sqrt(2*(g*5-0.2*g*3)))
    put(8, v=(2*3+1*0)/3, kinetic_before=0.5*2*3**2, kinetic_after=0.5*3*2**2, impulse=0.2*(10-(-10)), elastic_v1=(2-1)/(2+1)*3, elastic_v2=2*2/(2+1)*3)
    put(9, omega=2*3, theta=0.5*2*3**2, inertia=0.5*2*0.2**2, energy=0.5*(0.5*2*0.2**2)*10**2, rim=10*0.2)
    put(10, alpha=(5*0.2)/(0.5*2*0.2**2), rolling=sqrt(2*g*1/(1+0.5)), final_omega=2*3/0.5, precession=1*g*0.1/(0.02*100))
    put(11, support_right=(100*2+200*3)/4, support_left=300-(100*2+200*3)/4, elongation=1000*2/(2e-4*2e11))
    put(12, gauge=1000*g*2, buoyancy=1000*g*0.002, v2=2*4, pressure_drop=0.5*1000*(8**2-2**2), poiseuille_ratio=2**4)
    put(13, orbit=sqrt(3.986004418e14/7e6), period=2*pi*7e6/sqrt(3.986004418e14/7e6), escape=sqrt(2*3.986004418e14/7e6), gravity=3.986004418e14/7e6**2)
    put(14, omega=sqrt(200/2), period=2*pi/sqrt(200/2), vmax=0.1*sqrt(200/2), energy=0.5*200*0.1**2, pendulum=2*pi*sqrt(1/g))
    put(15, speed=sqrt(100/0.01), f1=sqrt(100/0.01)/(2*1), f3=3*sqrt(100/0.01)/2, power=0.5*0.01*(2*pi*50)**2*0.002**2*100)
    put(16, level=10*log(1e-6/1e-12,10), observed=500*343/(343-20), beat=abs(442-440), open_f=343/(2*0.5), closed_f=343/(4*0.5))
    put(17, final_temp=(0.2*80+0.3*20)/0.5, heat=0.2*4186*(44-80), melt=0.1*3.34e5, expand=12e-6*2*50)
    put(18, volume=R*300/1e5, rms=sqrt(3*R*300/0.028), internal=1.5*R*300, mono_cv=1.5*R, diatomic_cv=2.5*R)
    put(19, isothermal_work=R*300*log(2), isochoric_heat=1.5*R*100, adiabatic_temp=300*(0.5)**(2/3))
    put(20, efficiency=1-300/500, work=1000*(1-300/500), rejected=1000*300/500, cop=300/(500-300), entropy=100*(1/300-1/500))
    put(21, field=k*2e-6/0.3**2, force=-1e-6*(k*2e-6/0.3**2), dipole=k*2e-6*0.04/1**3)
    put(22, sphere=k*1e-9/0.1**2, inside=k*1e-9*0.05/0.1**3, flux=1e-9/eps0, plane=1e-6/(2*eps0))
    put(23, potential=k*2e-6/0.3, delta_u=(-1e-6)*(-100), field=-(2*3*2+4), work=-(-1e-6)*(-100))
    put(24, parallel_plate=eps0*0.01/0.001, charge=eps0*0.01/0.001*100, energy=0.5*eps0*0.01/0.001*100**2, series=2*3/(2+3), parallel=2+3)
    put(25, current=12/(5+1), terminal=12-12/6, load_power=(12/6)**2*5, internal_power=(12/6)**2*1, drift=1/(8.5e28*e*1e-6))
    put(26, parallel=6*3/(6+3), current=12/(4+2), v_parallel=2*2, time_constant=1e4*100e-6, charged=12*(1-exp(-1)), energy=0.5*100e-6*12**2)
    put(27, force=e*1e6*0.1, radius=me*1e6/(e*0.1), frequency=e*0.1/(2*pi*me), wire=2*0.3*0.5, torque=10*2*0.01*0.5)
    put(28, wire=mu0*10/(2*pi*0.05), loop=mu0*10/(2*0.05), solenoid=mu0*1000*2, force_length=mu0*10*10/(2*pi*0.05))
    put(29, emf=50*0.01*0.2/0.1, current=(50*0.01*0.2/0.1)/10, motional=0.5*0.2*3, displacement=eps0*0.01*1e6)
    put(30, tau=0.2/10, current=12/10*(1-exp(-1)), energy=0.5*0.2*(12/10)**2, omega=1/sqrt(0.2*5e-6), period=2*pi*sqrt(0.2*5e-6))
    put(31, xl=2*pi*50*0.1, xc=1/(2*pi*50*100e-6), impedance=sqrt(20**2+(2*pi*50*0.1-1/(2*pi*50*100e-6))**2), resonance=1/(2*pi*sqrt(0.1*100e-6)), secondary=220*1/10)
    n['c31']['current']=100/n['c31']['impedance']; n['c31']['power']=n['c31']['current']**2*20
    put(32, magnetic=100/c, intensity=0.5*eps0*c*100**2, radiation_pressure=0.5*eps0*100**2, wavelength=c/100e6)
    put(33, refracted=asin(sin(radians(30))/1.5)*180/pi, critical=asin(1/1.5)*180/pi, malus=100*cos(radians(60))**2)
    put(34, image=1/(1/0.1-1/0.3), magnification=-(1/(1/0.1-1/0.3))/0.3, virtual=1/(1/0.1-1/0.05), magnifier=0.25/0.05)
    put(35, fringe=600e-9*2/0.0005, film=550e-9/(4*1.5), mirror_shift=10*600e-9/2)
    put(36, angle=asin(500e-9/0.0001)*180/pi, width=2*2*500e-9/0.0001, resolution=1.22*550e-9/0.1, grating=asin(500e-9/(1/(600e3)))*180/pi)
    put(37, gamma=1/sqrt(1-0.8**2), lab_time=2/sqrt(1-0.8**2), contracted=10*sqrt(1-0.8**2), composition=(0.8+0.8)/(1+0.8*0.8), kinetic=(1/sqrt(1-0.8**2)-1)*0.511)
    put(38, photon=h*c/(400e-9)/e, kinetic=h*c/(400e-9)/e-2, cutoff=h*c/(2*e)*1e9, compton=h/(me*c)*1e12, min_xray=h*c/(20000*e)*1e9)
    put(39, wavelength=h/sqrt(2*me*150*e)*1e9, transition=13.6*(1/2**2-1/3**2), balmer=h*c/(13.6*(1/2**2-1/3**2)*e)*1e9, wien=2.897771955e-3/5800*1e9)
    put(40, ground=h**2/(8*me*(1e-9)**2)/e, second=4*h**2/(8*me*(1e-9)**2)/e, gap=3*h**2/(8*me*(1e-9)**2)/e, center_probability=0.5+1/pi)
    put(41, count_n2=2*2**2, orbital_n2=2**2, zeeman=(e*h/(4*pi*me))*1/e, box_ratio=3)
    put(42, rotational_ratio=2*(2+1)/(1*(1+1)), thermal_ev=kb*300/e, carrier_ratio=exp(-1.1*e/(2*kb*300))/exp(-1.1*e/(2*kb*400)))
    put(43, remaining=1/2**3, decay=log(2)/(5*24*3600), activity=log(2)/(5*24*3600)*1e12, binding=0.030*931.494, per_nucleon=0.030*931.494/4)
    put(44, recession=70*100, redshift=0.02*c/1000, hubble_age=(3.085677581491367e19/70)/(365.25*24*3600)/1e9, proton_charge=2*(2/3)-1/3, neutron_charge=2/3-2/3)
    assert n['c01']['norm']==5 and n['c01']['dot']==0
    assert n['c08']['kinetic_before']-n['c08']['kinetic_after']==3
    assert n['c11']['support_right']+n['c11']['support_left']==300
    assert abs(n['c17']['final_temp']-44)<1e-12
    assert abs(n['c20']['work']+n['c20']['rejected']-1000)<1e-12
    assert abs(n['c25']['load_power']+n['c25']['internal_power']-12*n['c25']['current'])<1e-12
    assert n['c40']['second']/n['c40']['ground']==4
    assert abs(n['c44']['proton_charge']-1)<1e-12 and n['c44']['neutron_charge']==0
    return n

if __name__ == '__main__':
    print(json.dumps(calculate(),ensure_ascii=False,indent=2))
