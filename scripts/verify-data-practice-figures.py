"""Check numeric claims in the original figure-reading practice."""
import math
import numpy as np
import pandas as pd

counts = np.array([12, 8, 5])
assert counts.sum() == 25
np.testing.assert_allclose(counts / counts.sum() * 100, [48, 32, 20])
prices = np.array([10, 12, 14, 16, 20, 20, 24, 28, 30, 36])
assert np.histogram(prices, bins=[0, 10, 20, 30, 40])[0].tolist() == [0, 4, 4, 2]
assert math.isclose(100 * (100 - 98) / 98, 2.0408163265306123)
assert (100 - 97) / (98 - 97) == 3
a = pd.Series([10, 12, 14, 16, 100])
q1, median, q3 = a.quantile([.25, .5, .75])
assert (q1, median, q3) == (12, 14, 16)
lower, upper = q1 - 1.5 * (q3 - q1), q3 + 1.5 * (q3 - q1)
assert (lower, upper) == (6, 22)
inliers = a[a.between(lower, upper)]
assert (inliers.min(), inliers.max()) == (10, 16)
assert (20 * 8 + 80 * 4) / 100 == 4.8
assert (80 * 7 + 20 * 3) / 100 == 6.2
assert math.isclose(.2 * 7 + .8 * 3, 3.8)
print('Figure-reading practice: All numeric claims verified')
