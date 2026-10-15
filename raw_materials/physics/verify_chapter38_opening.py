from fractions import Fraction
import json
# Positive constant hc cancels in the energy comparison. Test the reciprocal
# inequality without assigning any invented wavelength to the source's instruments.
for short,long in [(1,2),(3,5),(100,101),(400,700),(750,1500)]:
 assert 0<short<long
 assert Fraction(1,short)>Fraction(1,long)
 assert Fraction(long,short)>1
print(json.dumps(dict(status='passed',sourceQuestionAnswer='i headlamp',verifiedRelation='At fixed hc>0, shorter wavelength means greater photon energy.',inventedInstrumentWavelengths=False),indent=2))
