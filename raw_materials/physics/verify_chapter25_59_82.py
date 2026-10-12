"""Independent numerical checks for Chapter 25 problems 59–82."""
from math import exp, isclose, log, pi

rho_cu = 1.72e-8

# 25.59–25.60: radial/axial integral limits.
rho, h, r1, r2 = 2.4e-8, 0.12, 0.010, 0.025
R59 = rho * h / (pi * r1 * r2)
R59_near_cylinder = rho*h/(pi*r1*(r1*(1+1e-8)))
R59_cylinder = rho*h/(pi*r1**2)
assert isclose(R59_near_cylinder, R59_cylinder, rel_tol=1e-7)
a, b, rho60, Vab = 0.020, 0.080, 1.5, 12.0
R60 = rho60 / (4 * pi) * (1 / a - 1 / b)
J60 = lambda r: Vab / (4 * pi * R60 * r**2)
gap60 = 1e-8
R60_narrow = rho60/(4*pi)*gap60/(a*(a+gap60))
R60_flat = rho60*gap60/(4*pi*a**2)
assert isclose(R60_narrow, R60_flat, rel_tol=1e-6)

# 25.61: battery charge and discharge measurements.
r61 = (10.20 - 8.40) / (1.50 + 3.50)
emf61 = 8.40 + 1.50 * r61
assert isclose(r61, 0.36) and isclose(emf61, 8.94)

# 25.62: both printed batteries have their positive terminal at the left.
I62 = (8.00 - 4.00) / 24.0
Vad62 = 6.0 * I62 + (4.0 + 0.5 * I62) + 9.0 * I62
Vbc62 = 4.00 + 0.50 * I62
I62c = (8.00 - 4.00 - 10.30) / 24.50
Vbc62c = 4.00 + 0.50 * I62c
assert isclose(I62, 1/6) and isclose(Vad62, 6.5833333333333)
assert isclose(Vbc62, 4.0833333333333) and isclose(Vbc62c, 3.8714285714286)

# 25.63–25.64: body model and current limiting.
R63 = 5.0 * 1.6 / (pi * (0.10/2)**2)
V63, P63 = 0.100 * R63, 0.100**2 * R63
I64 = 14_000 / 12_000
P64 = I64**2 * 10_000
r64_min = 14_000 / 0.001 - 10_000

# 25.65: yearly energy cost, assuming 365 days per year.
cost65_bulb = 0.075 * 24 * 365 * 0.120
cost65_fridge = 0.400 * 8 * 365 * 0.120

# 25.66: copper cable.
R66 = 220.0**2 / 90.0
A66 = rho_cu * 1500 / R66
d66 = (4*A66/pi)**0.5
E66 = 220.0 / 1500

# 25.67: integrate rho(x)=rho0+beta*x^2.
L67, rad67, rho0, rhoL, I67 = 1.50, 0.0110, 2.25e-8, 8.50e-8, 1.75
A67 = pi*rad67**2
beta = (rhoL-rho0)/L67**2
R67 = L67/A67*(rho0+(rhoL-rho0)/3)
Emid67 = (rho0+beta*(L67/2)**2)*I67/A67
Rleft67 = (rho0*(L67/2)+beta*(L67/2)**3/3)/A67
Rright67 = R67-Rleft67

# 25.68: three years at four hours per day, including whole replacement bulbs.
hours68 = 3*365*4
n_bulbs_inc = (hours68+750-1)//750
cost_cfl = 11.00 + 0.023*hours68*0.080
cost_inc = 0.75*n_bulbs_inc + 0.100*hours68*0.080
save68 = cost_inc-cost_cfl
R_cfl = 120.0**2/23.0

# 25.69: saline-water cylinder is the steady-current branch; distilled
# water acts as a capacitor in parallel.
r_can, L_can, R_series, emf69, I69 = 0.050, 0.030, 15.0, 10.0, 0.484
R_salt = emf69/I69-R_series
area_can = pi*r_can**2
rho_salt = R_salt*area_can/L_can
salinity69 = 6.30/rho_salt
V_can = I69*R_salt
C_pure = 80.4*8.8541878128e-12*area_can/L_can
Q_pure = C_pure*V_can
P_salt = I69**2*R_salt
I_half = emf69/(2*R_series)
R_salt_half = emf69/I_half-R_series
salinity_half = 6.30/(R_salt_half*area_can/L_can)
assert isclose(salinity69, 4.25, rel_tol=0.01)
assert isclose(Q_pure, 510e-12, rel_tol=0.02)
assert isclose(P_salt, 1.33, rel_tol=0.02)
assert isclose(salinity_half, 1.60, rel_tol=0.01)

# 25.70–25.71: capacitors are open branches at the final DC state.
V70 = 18e-3/3e-3
Q2_70 = 6e-3*V70
R1_70 = (72.0-V70)/(V70/2.0)
V71 = 36e-3/9e-3
emf71 = V71 + V71/6.0*4.0
assert isclose(Q2_70, 36e-3) and isclose(R1_70, 22.0)
assert isclose(emf71, 20/3)

# 25.72: graph line Vab = emf - rI.
emf72, r72 = 36.0, 2.0
V80 = 0.8*emf72
R80 = V80/((emf72-V80)/r72)
assert isclose(R80, 8.0)

# 25.73: quadratic least-squares fit to the supplied non-ohmic V(I) data.
IA, VA = [0.5,1.0,2.0,4.0], [2.55,3.11,3.77,4.58]
S=[sum(x**k for x in IA) for k in range(5)]
SV=[sum(x**k*y for x,y in zip(IA,VA)) for k in range(3)]
M=[[S[4],S[3],S[2],SV[2]],[S[3],S[2],S[1],SV[1]],[S[2],S[1],S[0],SV[0]]]
for c in range(3):
    z=M[c][c]
    for j in range(c,4): M[c][j]/=z
    for i in range(3):
        if i!=c:
            z=M[i][c]
            for j in range(c,4): M[i][j]-=z*M[c][j]
aa,bb,cc=[M[i][3] for i in range(3)]
lo,hi=2.0,4.0
for _ in range(100):
    mid=(lo+hi)/2
    if aa*mid**2+bb*mid+cc<4: lo=mid
    else: hi=mid
I_A_4=(lo+hi)/2
P_A_4=4*I_A_4
P_B_4=4**2/3.88
assert isclose(P_A_4,9.4,rel_tol=0.01)
assert isclose(P_B_4,4.12,rel_tol=0.005)

# 25.74: choose smallest wire gauge carrying 35 A; compare copper losses.
I74, L74 = 4200/120, 42.0
table={14:(.163,18),12:(.205,25),10:(.259,30),8:(.326,40),
       6:(.412,60),5:(.462,65),4:(.519,85)}
gauge=max(g for g,(_,imax) in table.items() if imax>=I74)
def wire_loss(g):
    dcm,_=table[g]
    area=pi*(dcm/100/2)**2
    return I74**2*rho_cu*L74/area
P8,P6=wire_loss(8),wire_loss(6)
save74=(P8-P6)*12*365/1000*0.11
assert gauge==8

# 25.75: radial cylindrical shell resistor.
rho75=6800*2*pi*.0100/log(.00300/.00150)
assert isclose(rho75,616,rel_tol=0.01)

# 25.76: filament temperature depends linearly on current.
rho0_76,L76,d76,alpha=5.25e-8,.580,46e-6,.0045
R0_76=rho0_76*L76/(pi*(d76/2)**2)
def bulb_current(V):
    lo,hi=0.0,2.0
    for _ in range(100):
        I=(lo+hi)/2
        R=R0_76*(1+alpha*2500*I)
        if I*R<V: lo=I
        else: hi=I
    return (lo+hi)/2
I120,I60=bulb_current(120),bulb_current(60)
Rhot=120/I120
E120,E60=120*I120*60,60*I60*60

# 25.77: exponentially varying resistivity rod, analytic integral.
L77,A77,rho0_77,V0=1.50,pi*(.0110)**2,2.25e-8,12.0
R77=rho0_77*L77*(1-exp(-1))/A77
I77=V0/R77
E0_77,Eend_77=rho0_77*I77/A77,rho0_77*exp(-1)*I77/A77
Vhalf_77=V0*(exp(-.5)-exp(-1))/(1-exp(-1))

# 25.78: maximum power theorem and requested numerical loads.
E78,r78=64.0,4.0
P78=[E78**2*R/(R+r78)**2 for R in (2.0,4.0,6.0)]
assert isclose(P78[1],E78**2/(4*r78))

# 25.79–25.82: spider-web data and charge polarization.
lengths=[5,7,9,11,13,9,7,5]
resistance_gohm=[9,19,41,63,102,76,50,24]
area_ratio=(13/5)*(9/102)
I81=9/9e9
assert isclose(area_ratio,.2294,rel_tol=.001) and isclose(I81,1e-9)

print(f"25.59 R={R59:.5g} ohm; 25.60 R={R60:.5g} ohm, J(4 cm)={J60(.04):.5g} A/m^2")
print(f"25.61 r={r61:.5g} ohm, emf={emf61:.5g} V")
print(f"25.62 Vad={Vad62:.5g} V, Vbc={Vbc62:.5g} V, Vbc after insertion={Vbc62c:.5g} V")
print(f"25.63 R={R63:.5g} ohm, V={V63:.5g} V, P={P63:.5g} W; 25.64 I={I64:.5g} A, Pbody={P64:.5g} W, rint_min={r64_min:.5g} ohm")
print(f"25.65 annual costs={cost65_bulb:.4g}, {cost65_fridge:.4g}; 25.66 diameter={d66*1000:.5g} mm, E={E66:.5g} V/m")
print(f"25.67 R={R67:.5g} ohm, Emid={Emid67:.5g} V/m, halves={Rleft67:.5g}/{Rright67:.5g} ohm")
print(f"25.68 costs CFL/inc={cost_cfl:.5g}/{cost_inc:.5g}, saving={save68:.5g}, R_CFL={R_cfl:.5g} ohm")
print(f"25.69 salt R/rho/salinity={R_salt:.5g}/{rho_salt:.5g}/{salinity69:.5g}, Qcap={Q_pure:.5g} C, Pwater={P_salt:.5g} W, half-power salinity={salinity_half:.5g} ppt")
print(f"25.70 Q2={Q2_70:.5g} C, R1={R1_70:.5g} ohm; 25.71 emf={emf71:.5g} V")
print(f"25.72 emf={emf72:.5g} V, r={r72:.5g} ohm, R80={R80:.5g} ohm")
print(f"25.73 estimated power A/B={P_A_4:.5g}/{P_B_4:.5g} W; 25.74 gauge={gauge}, losses={P8:.5g}/{P6:.5g} W, saving={save74:.5g}/year")
print(f"25.75 rho={rho75:.5g} ohm m; 25.76 R20={R0_76:.5g} ohm, I120={I120:.5g} A, Rhot={Rhot:.5g} ohm, energy/min={E120:.5g}/{E60:.5g} J")
print(f"25.77 R={R77:.5g} ohm, I={I77:.5g} A, E endpoints={E0_77:.5g}/{Eend_77:.5g} V/m, V(L/2)={Vhalf_77:.5g} V")
print(f"25.78 powers for R=2,4,6 ohm: {P78}; 25.80 area ratio={area_ratio:.5g}; 25.81 I={I81:.5g} A")
