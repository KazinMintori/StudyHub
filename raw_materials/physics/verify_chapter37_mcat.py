from math import sqrt,isclose
import json
c=3.00e8/1e6
beta=180/c
gamma=1/sqrt(1-beta*beta)
length=60/gamma
historical_mass=20000*gamma
rest_energy=8.2e-14/1e12
assert isclose(length,48)
assert isclose(historical_mass,25000)
assert isclose(rest_energy,8.2e-26)
assert isclose(gamma,1.25)
# Energy and mass have different SI dimensions. Only K=mc^2 would give gamma=2.
beta_if_rest_energy=sqrt(3)/2
assert isclose(beta_if_rest_energy*c,259.8076211353316)
print(json.dumps(dict(status='passed',alternate_c_m_s=c,answers={'37.71':'c','37.72':'d','37.73':'b','37.74':'d'},length_m=length,historical_relativistic_mass_kg=historical_mass,rest_energy_J=rest_energy,conditional_speed_if_energy_instead_of_mass=beta_if_rest_energy*c),indent=2))
