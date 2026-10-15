"""Verify the opening question's relative aperture scales without adding unprovided optical inputs."""
from pathlib import Path
import json,math
root=Path(__file__).resolve().parents[2]
human_given_m=16e-3;fly_lens_m=20e-6;fly_eye_m=1e-3
# With equal wavelengths, the circular-aperture angular scale is inverse diameter.
ratio=human_given_m/fly_lens_m
assert math.isclose(ratio,800)
assert fly_lens_m<fly_eye_m<human_given_m
q=root/'qa/physics/chapter36';q.mkdir(parents=True,exist_ok=True)
(q/'opening-data-checks.json').write_text(json.dumps(dict(status='passed',choice='i',givenHumanScaleM=human_given_m,flySingleLensM=fly_lens_m,flyWholeEyeM=fly_eye_m,relativeDiffractionScale=ratio,model='Use given comparison scales and individual lens aperture. Do not infer biological acuity from whole-eye diameter or claim an actual16mm human pupil.'),indent=2),encoding='utf-8')
print('Opening aperture-scale comparison passed.')
