"""Independent checks of GP beam and Perron examples, not a structural-design solver."""
from pathlib import Path
from fractions import Fraction as F
import json
import numpy as np

beams=[]
for widths,heights in [([F(1),F(1)],[F(1),F(1)]),([F(1),F(2)],[F(1),F(1)]),([F(1),F(1)],[F(1),F(2)])]:
    v=[F(0)]*3;y=[F(0)]*3
    for j in [1,0]:
        i=j+1;denom=1000*widths[j]*heights[j]**3
        v[j]=12*(i-F(1,2))/denom+v[j+1]
        y[j]=6*(i-F(1,3))/denom+v[j+1]+y[j+1]
    explicit=sum(4*F(3*i*i-3*i+1,1000)/(widths[i-1]*heights[i-1]**3) for i in [1,2])
    assert y[0]==explicit
    volume=sum(w*h for w,h in zip(widths,heights))
    stress=[6*(i+1)/(widths[i]*heights[i]**2) for i in [0,1]]
    beams.append({'widths':list(map(str,widths)),'heights':list(map(str,heights)),'volume':str(volume),'tip_deflection':str(y[0]),'tip_slope':str(v[0]),'stress':list(map(str,stress))})
assert [row['tip_deflection'] for row in beams]==['4/125','9/500','3/400']
perron=[]
for t in [.25,.5,1,2,3,4]:
    A=np.array([[t,1],[1,1/t]])/4
    eigen=np.linalg.eigvals(A);radius=float(max(abs(eigen)))
    assert np.isclose(radius,(t+1/t)/4)
    assert np.allclose(A@np.array([t,1]),radius*np.array([t,1]))
    assert radius>=.5-1e-10
    for r in [.25,.5,1,2,4]:
        v=np.array([r,1]);ratios=A@v/v;bound=float(max(ratios))
        assert np.all(A@v<=bound*v+1e-10) and bound>=radius-1e-10
    perron.append({'t':t,'radius':radius,'unit_vector_bound':float(max(A@np.ones(2)))})
assert np.isclose(perron[3]['radius'],.625) and np.isclose(perron[3]['unit_vector_bound'],.75)
assert max(abs(np.linalg.eigvals([[2,1],[1,2]])))==3
out=Path('qa/math-ai-visuals/gp-applications-numerical.json')
out.write_text(json.dumps({'beam':beams,'perron':perron,'status':'passed'},indent=2),encoding='utf-8')
print('PASS: beam recurrence, exact comparison values, Perron eigenpairs and certificate bounds')
