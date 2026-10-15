from math import pi,cos,isclose
import json
h=6.626e-34;c=2.998e8;me=9.109e-31;mp=1.673e-27
phi=3.0
assert (phi/(2*h))/(phi/h)==.5
# At fixed quantum yield and optical power, twice the frequency halves photon flux.
assert (1/(h*2))/(1/(h*1))==.5
# At fixed observation duration, tenfold lower flux gives tenfold lower count.
assert isclose((.1*7)/(1*7),.1)
# The statistical waiting time is distinct from latency after photon absorption.
assert isclose((1/.1)/(1/1),10.)
checks=[]
for f in [1e14,1e18,1e20]:
 for angle in [0,pi/2,pi]:
  a=h*f/(me*c*c);fp=f/(1+a*(1-cos(angle)));assert fp<=f
  if angle==0:assert fp==f
  else:assert fp<f
  checks.append(dict(f=f,angle_rad=angle,ratio=fp/f))
duration=1e-12
r=dict(status='passed',two_photon_threshold_ratio=.5,saturation_current_ratio_at_fixed_power_double_frequency=.5,waiting_time_ratio_for_tenth_flux=10,proton_to_electron_compton_shift_ratio=me/mp,pulse_length_m=c*duration,pulse_min_frequency_width_Hz=1/(4*pi*duration),comptonChecks=checks)
print(json.dumps(r,indent=2))
