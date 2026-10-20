"""Verify the numerical examples used by XSTK glossary entries."""
from fractions import Fraction
from itertools import product

joint = {xy: Fraction(1, 4) for xy in product((0, 1), repeat=2)}
assert sum(joint.values()) == 1
assert sum(Fraction(x + y, 2) * p for (x, y), p in joint.items()) == Fraction(1, 2)
assert sum((2, 4, 6)) / 3 == 4
x = (-1, 0, 1)
ex = sum(Fraction(t, 3) for t in x)
ey = sum(Fraction(t*t, 3) for t in x)
covariance = sum((t-ex) * (t*t-ey) / 3 for t in x)
assert covariance == 0
assert Fraction(1, 3) != Fraction(1, 3) * Fraction(2, 3)  # P(X=1,Y=1)
observations = (-2, 2)
mean_variance = sum(Fraction((a+b)**2, 16) for a,b in product(observations, repeat=2))
assert mean_variance == 2  # Var(mean)=Var(X)/2, requiring independence
p_hat = Fraction(3, 4)
likelihood = lambda p: p**3 * (1-p)
assert 3 / p_hat - 1 / (1-p_hat) == 0
assert all(likelihood(p_hat) >= likelihood(Fraction(i, 100)) for i in range(101))
assert 1 / (Fraction(1, 2) * Fraction(1, 2)) == 4  # Fisher information
assert 1 - Fraction(1, 5) == Fraction(4, 5)  # Power
assert Fraction(8, 20) == Fraction(2, 5)  # Conditional probability
assert Fraction(1, 10) / Fraction(1, 2) == Fraction(1, 5)
print('PASS: XSTK glossary joint probabilities, conditional means, covariance, sampling variance, Fisher information and power.')
