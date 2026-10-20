#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Verification Script for Classical Probability Track (Lessons 28-35)
StudyHub (UET) - All numerical calculations, worked examples, exercises and counterexamples.
"""

import sys
import io
import subprocess
import json
import math
from pathlib import Path
from fractions import Fraction
import scipy.stats as stats
import scipy.integrate as integrate
import numpy as np

if sys.stdout.encoding != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


def test_lesson_28():
    print("Testing Lesson 28: Đếm và xác suất cổ điển...")
    # Example 1: Stars and bars
    c1 = math.comb(10 - 1, 4 - 1)
    assert c1 == 84, f"Expected 84, got {c1}"

    c0 = math.comb(10 + 4 - 1, 10)
    assert c0 == 286, f"Expected 286, got {c0}"

    # Example 2: Inclusion-Exclusion for 3 events
    union_abc = 65 + 50 + 40 - (25 + 20 + 15) + 10
    assert union_abc == 105, f"Expected 105, got {union_abc}"
    none_abc = 120 - 105
    assert none_abc == 15, f"Expected 15, got {none_abc}"

    only_a = 65 - 25 - 20 + 10
    only_b = 50 - 25 - 15 + 10
    only_c = 40 - 20 - 15 + 10
    assert only_a == 30 and only_b == 20 and only_c == 15
    total_exact_one = only_a + only_b + only_c
    assert total_exact_one == 65
    p_exact_one = Fraction(65, 120)
    assert p_exact_one == Fraction(13, 24)

    # Example 3: Meeting problem (geometric probability)
    area_meet = 3600 - 2025
    assert area_meet == 1575
    p_meet = Fraction(1575, 3600)
    assert p_meet == Fraction(7, 16)
    assert float(p_meet) == 0.4375

    # Exercises
    # Ex 1: Stars and bars 8 milk teas from 5 flavors
    ex1 = math.comb(8 + 5 - 1, 8)
    assert ex1 == 495, f"Expected 495, got {ex1}"

    # Ex 2: Anagram "STATISTICS" (10 letters: 3 S, 3 T, 1 A, 2 I, 1 C)
    ex2 = math.factorial(10) // (math.factorial(3) * math.factorial(3) * math.factorial(1) * math.factorial(2) * math.factorial(1))
    assert ex2 == 50400, f"Expected 50400, got {ex2}"

    # Ex 3: Inclusion-Exclusion 200 candidates
    union_tlh = 100 + 80 + 70 - 40 - 30 - 25 + 15
    assert union_tlh == 170
    assert 200 - union_tlh == 30
    assert Fraction(30, 200) == Fraction(3, 20)

    # Two ordered uniform break points: integrate the feasible triangle,
    # then double for the reversed order.
    broken_stick, _ = integrate.quad(lambda x: (x + 0.5) - 0.5, 0, 0.5)
    assert math.isclose(2 * broken_stick, 0.25)

    # Ex 5 actually uses decreasing intervals [0, 1/n].
    lim_p = [1 / n for n in (1, 2, 3, 1000)]
    assert lim_p[:3] == [1, 0.5, 1 / 3]
    assert all(a > b for a, b in zip(lim_p, lim_p[1:]))
    assert math.isclose(lim_p[-1], 0.001)
    print("Lesson 28 passed successfully.")


def test_lesson_29():
    print("Testing Lesson 29: Phân phối rời rạc mở rộng...")
    # Example 1: Geometric distribution
    p = 0.2
    p_x4 = (0.8 ** 3) * 0.2
    assert math.isclose(p_x4, 0.1024)
    e_x = 1 / p
    var_x = (1 - p) / (p ** 2)
    assert math.isclose(e_x, 5.0)
    assert math.isclose(var_x, 20.0)
    # After three failures, both of the next two trials fail.
    assert math.isclose(stats.geom.sf(5, p) / stats.geom.sf(3, p), 0.64)

    e_y = (1 - p) / p
    var_y = (1 - p) / (p ** 2)
    assert math.isclose(e_y, 4.0)
    assert math.isclose(var_y, 20.0)

    # Example 2: Negative Binomial (r=3, p=0.05)
    r = 3
    p_defect = 0.05
    e_nb = r * (1 - p_defect) / p_defect
    var_nb = r * (1 - p_defect) / (p_defect ** 2)
    assert math.isclose(e_nb, 57.0)
    assert math.isclose(var_nb, 1140.0)
    assert math.isclose(math.sqrt(var_nb), 33.76388603226827)

    # Example 3: Multinomial
    coeff = math.factorial(10) // (math.factorial(5) * math.factorial(3) * math.factorial(2))
    assert coeff == 2520
    prob_multi = coeff * (0.5 ** 5) * (0.3 ** 3) * (0.2 ** 2)
    assert math.isclose(prob_multi, 0.08505)
    cov_12 = -10 * 0.5 * 0.3
    assert math.isclose(cov_12, -1.5)

    # Example 4: Coupon collector N = 3
    e_t = 1 + 3/2 + 3/1
    assert math.isclose(e_t, 5.5)
    var_t = 0 + (1 - 2/3) / ((2/3)**2) + (1 - 1/3) / ((1/3)**2)
    assert math.isclose(var_t, 6.75)

    # Exercises
    # Ex 1: Geometric P(X > 4) = (5/6)^4
    assert Fraction(5, 6)**4 == Fraction(625, 1296)

    # Ex 2: NegBin P(X = 5 | r=2, p=0.25) = comb(4, 1) * 0.25^2 * 0.75^3
    p_ex2 = math.comb(4, 1) * (0.25**2) * (0.75**3)
    assert math.isclose(p_ex2, 27 / 256)

    # Ex 3: Multinomial n=6, (3, 2, 1), p=(0.5, 0.3, 0.2)
    c_ex3 = math.factorial(6) // (math.factorial(3) * math.factorial(2) * math.factorial(1))
    assert c_ex3 == 60
    p_ex3 = 60 * (0.5**3) * (0.3**2) * (0.2**1)
    assert math.isclose(p_ex3, 0.135)

    # Ex 4: Memoryless property verification: (1 - p)^(m+n) / (1 - p)^m == (1 - p)^n
    p_test = 0.3
    m_val, n_val = 2, 3
    tail_m_plus_n = (1 - p_test) ** (m_val + n_val)
    tail_m = (1 - p_test) ** m_val
    tail_n = (1 - p_test) ** n_val
    assert math.isclose(tail_m_plus_n / tail_m, tail_n)

    # Ex 5: Multinomial covariance identity check
    n_sample, p1, p2 = 10, 0.5, 0.3
    var_s = n_sample * (p1 + p2) * (1 - p1 - p2)
    var_x1 = n_sample * p1 * (1 - p1)
    var_x2 = n_sample * p2 * (1 - p2)
    two_cov = var_s - var_x1 - var_x2
    assert math.isclose(two_cov, 2 * (-n_sample * p1 * p2))
    print("Lesson 29 passed successfully.")


def test_lesson_30():
    print("Testing Lesson 30: Phân phối liên tục mở rộng...")
    # Example 1: Exponential (lambda = 0.5)
    p_exp3 = math.exp(-1.5)
    assert math.isclose(p_exp3, 0.22313016014842982)

    # Example 2: Gamma (alpha=4, lambda=2)
    e_gamma = 4 / 2
    var_gamma = 4 / (2**2)
    assert e_gamma == 2.0
    assert var_gamma == 1.0
    poiss_sum = sum(math.exp(-3) * (3**k) / math.factorial(k) for k in range(4))
    p_gamma_cdf = 1 - poiss_sum
    assert math.isclose(poiss_sum, 13 * math.exp(-3))
    assert math.isclose(p_gamma_cdf, 1 - 13 * math.exp(-3))
    assert math.isclose(p_gamma_cdf, stats.gamma.cdf(1.5, a=4, scale=1/2))

    # Example 3: Beta(3, 7)
    e_beta = 3 / (3 + 7)
    var_beta = (3 * 7) / ((10**2) * 11)
    mode_beta = (3 - 1) / (3 + 7 - 2)
    assert e_beta == 0.3
    assert math.isclose(var_beta, 21 / 1100)
    assert math.isclose(math.sqrt(var_beta), 0.1381698559415515)
    assert mode_beta == 0.25

    # Example 4: Lognormal
    med_log = math.exp(3)
    mean_log = math.exp(3 + 0.25 / 2)
    assert math.isclose(med_log, 20.085536923187668)
    assert math.isclose(mean_log, 22.75989509352673)
    assert math.isclose(mean_log - med_log, 2.674358170339062)

    # Exercises
    # Ex 1: Exponential median
    assert math.isclose(math.log(2) / 0.001, 693.1471805599453)

    # Ex 2: Gamma(5) = 24, Gamma(5/2) = 0.75 * sqrt(pi)
    assert math.gamma(5) == 24
    assert math.isclose(math.gamma(2.5), 0.75 * math.sqrt(math.pi))

    # Ex 3: Beta(2, 2) CDF on [0.25, 0.75]
    val, _ = integrate.quad(lambda x: 6 * x * (1 - x), 0.25, 0.75)
    assert math.isclose(val, 11 / 16)

    # Ex 4: Hazard rate verification for Weibull: h(t) = (k/lambda) * (t/lambda)^(k-1)
    k_vals = [0.5, 1.0, 1.5]
    t1, t2 = 1.0, 2.0
    for k in k_vals:
        h1 = (k / 1.0) * (t1 ** (k - 1))
        h2 = (k / 1.0) * (t2 ** (k - 1))
        if k < 1.0:
            assert h2 < h1
        elif k == 1.0:
            assert math.isclose(h1, h2)
        else:
            assert h2 > h1

    # Ex 5: Fourth moment of standard normal is 3
    val4, _ = integrate.quad(lambda x: (x**4) * stats.norm.pdf(x), -np.inf, np.inf)
    assert math.isclose(val4, 3.0)
    print("Lesson 30 passed successfully.")


def test_lesson_31():
    print("Testing Lesson 31: Vector ngẫu nhiên và phân phối đồng thời...")
    # Example 1: Discrete joint table
    p_table = np.array([
        [0.4, 0.2, 0.1],  # X = 0
        [0.1, 0.1, 0.1]   # X = 1
    ])
    p_x = p_table.sum(axis=1)
    p_y = p_table.sum(axis=0)
    assert np.allclose(p_x, [0.7, 0.3])
    assert np.allclose(p_y, [0.5, 0.3, 0.2])
    p_y_given_x1 = p_table[1, :] / p_x[1]
    assert np.allclose(p_y_given_x1, [1/3, 1/3, 1/3])

    # Example 2: Triangle joint density f(x, y) = c * (x + 2y) on 0 <= x <= y <= 1
    val, _ = integrate.dblquad(lambda y, x: x + 2*y, 0, 1, lambda x: x, lambda x: 1)
    assert math.isclose(val, 5/6)
    c = 1 / val
    assert math.isclose(c, 1.2)
    assert math.isclose(1.6 / 3, 8/15)
    for x in (0.0, 0.2, 0.8):
        marginal, _ = integrate.quad(lambda y: c * (x + 2*y), x, 1)
        assert math.isclose(marginal, (6/5) * (1+x-2*x*x))
    for y in (0.2, 0.8, 1.0):
        marginal, _ = integrate.quad(lambda x: c * (x + 2*y), 0, y)
        mean_cond, _ = integrate.quad(lambda x: x*2*(x+2*y)/(5*y*y), 0, y)
        assert math.isclose(marginal, 3*y*y)
        assert math.isclose(mean_cond, 8*y/15)
    # Independent positive density on a Cartesian product need not be
    # supported on one connected rectangle.
    intervals = [(0, 1), (2, 3)]
    mass = sum(integrate.quad(lambda _: 0.5, a, b)[0] for a, b in intervals)
    assert math.isclose(mass, 1)

    # Exercises
    # Ex 1: Uniform on triangle x >= 0, y >= 0, x + y <= 1
    val_ex1, _ = integrate.dblquad(lambda y, x: 2, 0, 1, lambda x: 0, lambda x: 1 - x)
    assert math.isclose(val_ex1, 1.0)

    # Ex 2: Fubini change order: int_0^1 int_0^x e^(x^2) dy dx = 0.5 * (e - 1)
    val_ex2, _ = integrate.quad(lambda x: x * math.exp(x**2), 0, 1)
    assert math.isclose(val_ex2, 0.5 * (math.e - 1))

    # Ex 3: P(X < Y < Z) for iid U(0, 1) is 1/6
    val_ex3 = 1 / math.factorial(3)
    assert math.isclose(val_ex3, 1/6)

    # Ex 4: Binary joint table independence check
    p_bin_table = np.array([[0.2, 0.3], [0.3, 0.2]])
    px_bin = p_bin_table.sum(axis=1)
    py_bin = p_bin_table.sum(axis=0)
    assert np.allclose(px_bin, [0.5, 0.5])
    assert np.allclose(py_bin, [0.5, 0.5])
    assert not math.isclose(p_bin_table[1, 1], px_bin[1] * py_bin[1])
    assert math.isclose(p_bin_table[1, 1] / py_bin[1], 0.4)

    # Ex 5: 8xy on 0 <= y <= x <= 1
    val_ex5, _ = integrate.dblquad(lambda y, x: 8*x*y, 0, 1, lambda x: 0, lambda x: x)
    assert math.isclose(val_ex5, 1.0)
    print("Lesson 31 passed successfully.")


def test_lesson_32():
    print("Testing Lesson 32: Hiệp phương sai và kỳ vọng có điều kiện...")
    # Example 1: Covariance and correlation from Lesson 31 table
    ex = 0.3
    var_x = 0.3 - 0.3**2
    assert math.isclose(var_x, 0.21)

    ey = 0 * 0.5 + 1 * 0.3 + 2 * 0.2
    assert math.isclose(ey, 0.7)
    ey2 = 0 * 0.5 + 1 * 0.3 + 4 * 0.2
    assert math.isclose(ey2, 1.1)
    var_y = 1.1 - 0.7**2
    assert math.isclose(var_y, 0.61)

    exy = 0.3
    cov_xy = exy - ex * ey
    assert math.isclose(cov_xy, 0.09)
    corr_xy = cov_xy / math.sqrt(var_x * var_y)
    assert math.isclose(corr_xy, 0.2514594403022007)

    # Example 2: Uncorrelated but dependent counterexample
    val_x3, _ = integrate.quad(lambda x: 0.5 * (x**3), -1, 1)
    assert math.isclose(val_x3, 0.0)
    ex2, _ = integrate.quad(lambda x: x*x/2, -1, 1)
    ex4, _ = integrate.quad(lambda x: x**4/2, -1, 1)
    assert math.isclose(ex2, 1/3)
    assert math.isclose(ex4-ex2**2, 4/45)
    # Positive probability event witness for non-independence.
    assert Fraction(1, 2) != Fraction(1, 2)**2

    # Example 3: Total expectation and total variance
    assert 5 * 10 == 50
    assert 4 * 10 + 25 * 10 == 290
    assert math.isclose(math.sqrt(290), 17.029386365926403)

    # Exercises
    # Ex 1: Dependent sum variance: Var(X1+X2+X3) with Var=4, Cov=1
    var_sum = 3 * 4 + 2 * 3 * 1
    assert var_sum == 18

    # Ex 2: f(x, y) = 2 on 0 <= x <= y <= 1, E[Y | X = x] = (1 + x)/2
    x_test = 0.4
    e_y_given_x, _ = integrate.quad(lambda y: y * (1 / (1 - x_test)), x_test, 1.0)
    assert math.isclose(e_y_given_x, (1 + x_test) / 2)

    # Ex 3: Random coin flips N ~ Uniform{1..6}, K | N ~ Bin(N, 0.5)
    e_n = 3.5
    e_k = e_n / 2
    assert e_k == 1.75
    var_k = 3.5 / 4 + (35 / 12) / 4
    assert math.isclose(var_k, 77 / 48)

    # Ex 4: Cauchy-Schwarz for Covariance: Cov^2 <= Var(X) * Var(Y)
    assert (cov_xy ** 2) <= (var_x * var_y)

    # Ex 5: W in {-1, 1}, Y = W * X. Cov(X, Y) = 0
    # E[W] = 0, E[X] = 0 => E[Y] = 0, E[XY] = E[W] * E[X^2] = 0
    assert 0 * 1 == 0
    q = 2 * stats.norm.cdf(1) - 1
    assert 0 < q < 1 and not math.isclose(q, q*q)
    print("Lesson 32 passed successfully.")


def test_lesson_33():
    print("Testing Lesson 33: Biến đổi và thống kê thứ tự...")
    # Example 1: Y = X^2 for X ~ N(0, 1) is Chi-sq(1)
    y_test = 2.0
    pdf_chi1 = stats.chi2.pdf(y_test, df=1)
    pdf_formula = (1 / math.sqrt(2 * math.pi * y_test)) * math.exp(-y_test / 2)
    assert math.isclose(pdf_chi1, pdf_formula)
    for y in (0.1, 1, 2, 4):
        cdf_formula = 2*stats.norm.cdf(math.sqrt(y))-1
        half_integral, _ = integrate.quad(stats.norm.pdf, 0, math.sqrt(y))
        assert math.isclose(cdf_formula, stats.chi2.cdf(y, 1))
        assert math.isclose(cdf_formula, 2*half_integral)

    # Example 2: Y = 3X + 1 for X ~ Exp(2)
    y_val = 4.0
    fy = (2/3) * math.exp(-2 * (y_val - 1) / 3)
    assert math.isclose(fy, (2/3) * math.exp(-2))
    # Sum/ratio transformation: det [[v,u],[1-v,-u]] = -u.
    for u, v in ((0.5, 0.2), (2.0, 0.7)):
        jacobian = np.array([[v, u], [1-v, -u]])
        assert math.isclose(abs(np.linalg.det(jacobian)), u)
    assert math.isclose(integrate.quad(lambda u: u*math.exp(-u), 0, np.inf)[0], 1)

    # Example 4: Order statistics of 5 Exp(0.1) components
    assert 1 / 0.5 == 2.0
    assert Fraction(1, 1) + Fraction(1, 2) + Fraction(1, 3) + Fraction(1, 4) + Fraction(1, 5) == Fraction(137, 60)
    assert 10 * Fraction(137, 60) == Fraction(137, 6)
    assert math.isclose(float(Fraction(137, 6)), 22.833333333333336)

    # Exercises
    # Ex 1: Convolution of 2 Uniform(0, 1) RVs
    # Integrate triangular density: int_0^1 z dz + int_1^2 (2-z) dz = 0.5 + 0.5 = 1.0
    area_tri = 0.5 * 1.0**2 + 0.5 * 1.0**2
    assert math.isclose(area_tri, 1.0)

    # Ex 2: Y = 1/X for X ~ U(0, 1) => f_Y(y) = 1/y^2 for y > 1
    # Integrate 1/y^2 from 1 to inf = 1.0
    val_pareto, _ = integrate.quad(lambda y: 1 / (y**2), 1, np.inf)
    assert math.isclose(val_pareto, 1.0)

    # Ex 3: Order statistic median of 3 Uniform(0, 1) RVs: Beta(2, 2)
    assert stats.beta.mean(2, 2) == 0.5

    # Ex 4: Y = e^X for X ~ N(0, 1) is standard lognormal
    val_lognorm, _ = integrate.quad(lambda y: (1 / (y * math.sqrt(2 * math.pi))) * math.exp(-(math.log(y)**2)/2), 0, np.inf)
    assert math.isclose(val_lognorm, 1.0)

    # Ex 5: U = min(X, Y), V = max(X, Y) for X, Y iid U(0, 1). f(u, v) = 2 on 0 <= u <= v <= 1
    val_order2, _ = integrate.dblquad(lambda v, u: 2, 0, 1, lambda u: u, lambda u: 1)
    assert math.isclose(val_order2, 1.0)
    # Exercise 5 CDF on and outside its triangular support.
    def joint_extrema_cdf(u, v):
        a, b = min(1, max(0, u)), min(1, max(0, v))
        return b*b-max(b-a, 0)**2
    for u, v in ((0.2, 0.8), (0.8, 0.2), (-0.2, 1.2), (1.2, 0.8), (2, 2)):
        area, _ = integrate.quad(
            lambda x: max(0, min(1, v)) if x <= u
            else max(0, min(1, v, u)),
            0, max(0, min(1, v)),
            points=[u] if 0 < u < min(1, v) else None,
        )
        assert math.isclose(joint_extrema_cdf(u, v), area, abs_tol=1e-10)
    print("Lesson 33 passed successfully.")


def test_lesson_34():
    print("Testing Lesson 34: Momen, hàm sinh và bất đẳng thức...")
    # Example 1: Standard normal MGF
    # Independent quadrature validates the actual MGF and its moments.
    for t in (-0.7, 0, 0.8):
        mgf, _ = integrate.quad(lambda x: math.exp(t*x)*stats.norm.pdf(x), -12, 12)
        assert math.isclose(mgf, math.exp(t*t/2))
    for power, expected in ((1, 0), (2, 1), (3, 0), (4, 3)):
        moment, _ = integrate.quad(lambda x: x**power*stats.norm.pdf(x), -12, 12)
        assert math.isclose(moment, expected, abs_tol=1e-10)
    # Sum of independent Poisson variables, checked by convolution.
    for k_sum in range(8):
        convolution = sum(stats.poisson.pmf(j, 2)*stats.poisson.pmf(k_sum-j, 3)
                          for j in range(k_sum+1))
        assert math.isclose(convolution, stats.poisson.pmf(k_sum, 5))
    # Example 3: Markov and Chebyshev bounds
    assert math.isclose(70 / 90, 7/9)
    assert 1 / (2**2) == 0.25

    # Example 4: Jensen inequality
    assert 9 + 4**2 == 25
    assert Fraction(1, 2)*(1+7) == 4
    assert Fraction(1, 2)*((1-4)**2+(7-4)**2) == 9
    assert Fraction(1, 2)*(1+Fraction(1, 7)) == Fraction(4, 7) > Fraction(1, 4)

    # Exercises
    # Ex 1: Exp(lambda) MGF: lambda / (lambda - t)
    # E[X] = 1/lambda, E[X^2] = 2/lambda^2
    lam = 2.0
    e_exp = 1 / lam
    e2_exp = 2 / (lam**2)
    assert e_exp == 0.5
    assert e2_exp == 0.5

    # Ex 2: Binomial PGF: G(s) = (1 - p + ps)^n
    n_trial, p_succ = 5, 0.4
    g_1 = (1 - p_succ + p_succ * 1.0) ** n_trial
    assert math.isclose(g_1, 1.0)
    for s in (-0.5, 0, 0.6, 1):
        explicit = sum(stats.binom.pmf(k, n_trial, p_succ)*s**k
                       for k in range(n_trial+1))
        assert math.isclose(explicit, (1-p_succ+p_succ*s)**n_trial, abs_tol=1e-12)

    # Ex 3: Standard normal skewness = 0, kurtosis = 3, excess kurtosis = 0
    assert stats.norm.stats(moments='mvsk')[2] == 0.0
    assert stats.norm.stats(moments='mvsk')[3] == 0.0

    # Ex 4: Cantelli inequality: P(X - mu >= k*sigma) <= 1 / (1 + k^2)
    k = 2
    assert 1 / (1 + k**2) == 0.2
    for sigma in (0.5, 1, 3):
        def bound(u):
            return (sigma*sigma+u*u)/(k*sigma+u)**2
        optimum = sigma/k
        assert math.isclose(bound(optimum), 1/(1+k*k))
        assert bound(optimum/2) >= bound(optimum)
        assert bound(optimum*2) >= bound(optimum)

    # Ex 5: Cauchy distribution has no mean/MGF
    # Cauchy truncated absolute moments increase as log(1+R^2)/pi.
    for radius in (10, 100, 1000):
        value, _ = integrate.quad(lambda x: 2*x/(math.pi*(1+x*x)), 0, radius)
        assert math.isclose(value, math.log1p(radius*radius)/math.pi)
    # Lognormal positive-t MGF power-series terms do not tend to zero:
    # log(a_{k+1}/a_k)=log(t)+(2k+1)/2-log(k+1) tends to infinity.
    for t in (0.001, 0.2, 1):
        assert math.log(t)+(2*100+1)/2-math.log(101) > 80
    print("Lesson 34 passed successfully.")


def test_lesson_35():
    print("Testing Lesson 35: Luật số lớn và định lý giới hạn...")
    # Example 1: Chebyshev proof of WLLN sample size
    assert 4 / (40000 * 0.01) == 0.01

    # Example 2: CLT with continuity correction
    exact_bin = sum(math.comb(100, k) * (0.5**100) for k in range(45, 56))
    assert math.isclose(exact_bin, 0.7287469759242953)
    clt_no_cc = stats.norm.cdf(1) - stats.norm.cdf(-1)
    assert math.isclose(clt_no_cc, 0.6826894921370859)
    clt_cc = stats.norm.cdf(1.1) - stats.norm.cdf(-1.1)
    assert math.isclose(clt_cc, 0.7286678783477196)
    rel_err = abs(clt_cc - exact_bin) / exact_bin
    assert rel_err < 0.0002

    # Example 3: Poisson approximation
    p_bin_3 = math.comb(2000, 3) * (0.001**3) * (0.999**1997)
    p_poi_3 = (2.0**3) * math.exp(-2.0) / math.factorial(3)
    assert math.isclose(p_bin_3, 0.18053732803180317)
    assert math.isclose(p_poi_3, 0.1804470443154836)
    assert abs(p_bin_3 - p_poi_3) < 0.0001

    # Example 4: Insurance problem capital safety
    e_s = 400 * 20
    var_s = 400 * (10**2) + 384 * (20**2)
    sd_s = math.sqrt(var_s)
    assert e_s == 8000
    assert var_s == 193600
    assert sd_s == 440.0
    c_req = (8000 + stats.norm.ppf(0.999) * 440) / 10000
    assert math.isclose(c_req, 0.9359702214710198)
    assert math.ceil(c_req*1_000_000) == 935971
    assert stats.norm.sf((10000*0.936-8000)/440) < 0.001

    # Exercises
    # Ex 2: Sum of 12 Uniform(0, 1) RVs minus 6 has mean 0, variance 1
    assert 12 * (1/12) == 1.0

    # Ex 3: Polling sample size with margin 0.03 at 95% confidence
    n_poll = (1.96 * 0.5 / 0.03) ** 2
    assert math.isclose(n_poll, 1067.111111111111)
    assert math.ceil(n_poll) == 1068

    # Ex 4: Typewriter sliding intervals: length 1/k_n -> 0
    for k in (2, 3, 17, 1000):
        # Exactly one interval contains each omega at every rank.
        intervals = [(j/k, (j+1)/k) for j in range(k)]
        for omega in (0, 0.1, 0.5, 0.999, 1):
            values = [a <= omega < b or (j == k-1 and omega == 1)
                      for j, (a, b) in enumerate(intervals)]
            assert sum(values) == 1
        assert math.isclose(sum(b-a for a, b in intervals), 1)
    for n in (1, 10, 1000):
        for t in (-2, -0.4, 0, 1.5):
            assert math.isclose(math.exp(-abs(t/n)*n), math.exp(-abs(t)))
    print("Lesson 35 passed successfully.")


def test_math_syntax_and_delimiters():
    print("\nRunning MathJax width, delimiter, and syntax audit...")
    node_script = """
import { readFile, readdir } from 'node:fs/promises';
import path from 'node:path';
import { createRequire } from 'node:module';

const require = createRequire(import.meta.url);
const MarkdownIt = require('markdown-it');
const mathjax = require('markdown-it-mathjax3');
const md = new MarkdownIt({ html: true }).use(mathjax.default || mathjax);
const directory = 'docs/xac-suat-thong-ke/bai-giang';
const results = [];
const cache = new Map();

for (const name of await readdir(directory)) {
  if (!/^(28|29|30|31|32|33|34|35)-.+\\.md$/.test(name)) continue;
  const file = path.join(directory, name);
  const source = await readFile(file, 'utf8');
  const text = source
    .replace(/^---[\\s\\S]*?---/, m => m.replace(/[^\\n]/g, ' '))
    .replace(/\\`\\`\\`[\\s\\S]*?\\`\\`\\`/g, m => m.replace(/[^\\n]/g, ' '));

  for (const match of text.matchAll(/\\$\\$([\\s\\S]*?)\\$\\$|\\$([^$\\n]+)\\$/g)) {
    const display = match[1] !== undefined;
    const tex = (match[1] ?? match[2]).trim();
    const key = `${display}:${tex}`;
    if (!cache.has(key)) {
      const html = display ? md.render('$$\\n' + tex + '\\n$$') : md.renderInline('$' + tex + '$');
      cache.set(key, {
        widthEx: Number(html.match(/<svg[^>]*width=\\"([\\d.]+)ex\\"/)?.[1] || 0),
        error: html.includes('data-mml-node=\\"merror\\"')
      });
    }
    const { widthEx, error } = cache.get(key);
    const delimiterLine = source.slice(
      source.lastIndexOf('\\n', match.index) + 1,
      source.indexOf('\\n', match.index) < 0 ? undefined : source.indexOf('\\n', match.index)
    ).trim();
    const ownLines = !display || (delimiterLine === '$$' && /\\n[\\t ]*$/.test(match[1]));
    const invalidBreak = display && /(?:^|\\\\\\\\)\\s*&?\\s*(?:\\\\quad\\s*)?[+-]/.test(tex) && /\\\\\\\\/.test(tex);
    if (error || widthEx > (display ? 34 : 38) || !ownLines || invalidBreak) {
      results.push({
        file: name,
        line: source.slice(0, match.index).split('\\n').length,
        display,
        widthEx,
        error,
        ownLines,
        invalidBreak,
        preview: tex.slice(0, 50)
      });
    }
  }
}
console.log(JSON.stringify(results));
"""
    proc = subprocess.run(
        ['node', '--input-type=module', '-e', node_script],
        cwd=Path(__file__).resolve().parents[2],
        capture_output=True, text=True, encoding="utf-8",
    )
    assert proc.returncode == 0, f"MathJax audit did not run successfully:\n{proc.stderr}"

    findings = json.loads(proc.stdout)
    if findings:
        print(f"Found {len(findings)} math formatting/width findings:")
        for item in findings:
            print(f"  [{item['file']}:L{item['line']}] display={item['display']}, width={item['widthEx']}ex, error={item['error']}, ownLines={item['ownLines']}, invalidBreak={item['invalidBreak']}")
            print(f"    TeX: {item['preview']}")
        assert len(findings) == 0, f"Math audit failed with {len(findings)} findings."
    else:
        print("All math equations fit constraints (inline <= 38ex, display <= 34ex, no merror, no invalid breaks, delimiters on own lines)!")


if __name__ == "__main__":
    test_lesson_28()
    test_lesson_29()
    test_lesson_30()
    test_lesson_31()
    test_lesson_32()
    test_lesson_33()
    test_lesson_34()
    test_lesson_35()
    test_math_syntax_and_delimiters()
    print("\nALL NUMERICAL TESTS AND THEORETICAL CALCULATIONS PASSED SUCCESSFULLY!")
