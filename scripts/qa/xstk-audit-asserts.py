import math
import sys
from fractions import Fraction
from scipy import stats

# Exact checks for the examples reformatted during the final mobile review.
assert sum([8, 11, 7, 7, 8, 11]) == 52
assert sum([9, 6, 10, 7, 9]) == 41
assert sum([12, 15, 16, 18, 20, 22, 25, 28, 30]) == 186
assert Fraction(2, math.comb(4, 2)) == Fraction(1, 3)
assert abs(stats.chi2.sf(28.08, 8) - 0.0004592737267965611) < 1e-15
assert abs(math.comb(500, 10) / math.comb(1000, 10) - 0.0009331878021844999) < 1e-15
for false_positive_cost, false_negative_cost in [(1, 1), (1, 2), (1, 100)]:
    low_threshold = 50 * false_positive_cost + 20 * false_negative_cost
    high_threshold = 10 * false_positive_cost + 40 * false_negative_cost
    assert (high_threshold < low_threshold) == (false_negative_cost < 2 * false_positive_cost)
assert math.sqrt(1 + 4) < math.sqrt(1) + math.sqrt(4)
assert math.sqrt(0 + 4) == math.sqrt(0) + math.sqrt(4)

sys.stdout.reconfigure(encoding='utf-8')

def test_lesson_04_07_summary_and_correlation():
    print("Testing Lesson 04 & 07: Descriptive stats & Pearson correlation...")
    x = [1, 2, 3, 4, 5]
    y = [2, 3, 5, 6, 9]
    n = len(x)

    mean_x = sum(x) / n
    mean_y = sum(y) / n
    assert mean_x == 3.0, f"Expected mean_x=3.0, got {mean_x}"
    assert mean_y == 5.0, f"Expected mean_y=5.0, got {mean_y}"

    ss_x = sum((xi - mean_x) ** 2 for xi in x)
    ss_y = sum((yi - mean_y) ** 2 for yi in y)
    assert ss_x == 10.0, f"Expected ss_x=10.0, got {ss_x}"
    assert ss_y == 30.0, f"Expected ss_y=30.0, got {ss_y}"

    s_x = math.sqrt(ss_x / (n - 1))
    s_y = math.sqrt(ss_y / (n - 1))
    assert abs(s_x - math.sqrt(2.5)) < 1e-9
    assert abs(s_y - math.sqrt(7.5)) < 1e-9

    ss_xy = sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y))
    assert ss_xy == 17.0, f"Expected ss_xy=17.0, got {ss_xy}"

    r = ss_xy / math.sqrt(ss_x * ss_y)
    assert abs(r - 17.0 / math.sqrt(300)) < 1e-9
    assert abs(r - 0.9815) < 1e-4, f"Expected r ~ 0.9815, got {r}"
    print("  PASS: Lesson 04 & 07 assertions verified.")

def test_lesson_09_10_probability_foundations():
    print("Testing Lesson 09 & 10: Probability rules & Sally Clark case...")
    # American roulette: 18 red, 18 black, 2 green (total 38)
    p_red = 18 / 38
    p_black = 18 / 38
    p_green = 2 / 38
    assert p_red + p_black + p_green == 1.0
    assert abs(p_red - 9/19) < 1e-9

    # Sally Clark: Independent SIDS fallacy
    p_single_sids = 1 / 8543
    p_independent_two = p_single_sids ** 2
    assert abs(p_independent_two - 1 / (8543 ** 2)) < 1e-15
    assert abs(p_independent_two - 1 / 72982849) < 1e-15
    print("  PASS: Lesson 09 & 10 assertions verified.")

def test_lesson_11_12_random_variables_and_distributions():
    print("Testing Lesson 11 & 12: Discrete distributions PMF & CDF...")
    # Binomial PMF: n=3, p=0.5
    # P(X=k) = C(3, k) * 0.5^3
    def binom_coeff(n, k):
        return math.comb(n, k)

    p_heads_3 = [binom_coeff(3, k) * (0.5 ** 3) for k in range(4)]
    assert p_heads_3 == [1/8, 3/8, 3/8, 1/8]
    assert sum(p_heads_3) == 1.0

    # Poisson PMF: lambda = 2.0
    lam = 2.0
    def poisson_pmf(k, lam):
        return (lam ** k * math.exp(-lam)) / math.factorial(k)
    p_poi_0 = poisson_pmf(0, lam)
    p_poi_1 = poisson_pmf(1, lam)
    p_poi_2 = poisson_pmf(2, lam)
    assert abs(p_poi_0 - math.exp(-2.0)) < 1e-9
    assert abs(p_poi_1 - 2.0 * math.exp(-2.0)) < 1e-9
    assert abs(p_poi_2 - 2.0 * math.exp(-2.0)) < 1e-9
    print("  PASS: Lesson 11 & 12 assertions verified.")

def test_lesson_13_expectation_and_sd():
    print("Testing Lesson 13: Expectation, SD, Loaded Die & Chebyshev bounds...")
    # 1. Fair die
    faces = [1, 2, 3, 4, 5, 6]
    p_fair = 1 / 6
    mu_fair = sum(x * p_fair for x in faces)
    var_fair = sum((x - mu_fair) ** 2 * p_fair for x in faces)
    sd_fair = math.sqrt(var_fair)
    assert mu_fair == 3.5, f"Expected mu=3.5, got {mu_fair}"
    assert abs(var_fair - 35/12) < 1e-9, f"Expected var=35/12, got {var_fair}"
    assert abs(sd_fair - 1.7078) < 1e-4, f"Expected sd ~ 1.7078, got {sd_fair}"

    # 2. Weighted die with same mean 3.5 but smaller variance
    # P(X=1) = P(X=6) = 1/12; P(X=2) = P(X=5) = 2/12; P(X=3) = P(X=4) = 3/12
    p_weighted = {1: 1/12, 2: 2/12, 3: 3/12, 4: 3/12, 5: 2/12, 6: 1/12}
    assert sum(p_weighted.values()) == 1.0
    mu_weighted = sum(k * p for k, p in p_weighted.items())
    var_weighted = sum((k - mu_weighted) ** 2 * p for k, p in p_weighted.items())
    sd_weighted = math.sqrt(var_weighted)
    assert mu_weighted == 3.5, f"Expected mu_weighted=3.5, got {mu_weighted}"
    assert abs(var_weighted - 23/12) < 1e-9, f"Expected var_weighted=23/12, got {var_weighted}"
    assert abs(sd_weighted - 1.3844) < 1e-4, f"Expected sd_weighted ~ 1.3844, got {sd_weighted}"
    assert var_weighted < var_fair, "Weighted die must have smaller variance than fair die"

    # 3. 1-SD interval counterexample: Discrete two-point distribution
    # P(X = -1) = 0.5, P(X = +1) = 0.5
    # E(X) = 0, Var(X) = 1, SD(X) = 1
    # Open interval (mu - sd, mu + sd) = (-1, 1). Contains ZERO mass!
    p_2pt = {-1: 0.5, 1: 0.5}
    mu_2pt = sum(x * p for x, p in p_2pt.items())
    var_2pt = sum((x - mu_2pt) ** 2 * p for x, p in p_2pt.items())
    sd_2pt = math.sqrt(var_2pt)
    assert mu_2pt == 0.0 and sd_2pt == 1.0
    mass_strictly_inside_1_sd = sum(p for x, p in p_2pt.items() if (mu_2pt - sd_2pt) < x < (mu_2pt + sd_2pt))
    assert mass_strictly_inside_1_sd == 0.0, "Open 1-SD interval has 0% mass for 2-point distribution"
    print("  PASS: Lesson 13 assertions verified.")

def test_lesson_14_clt_and_square_root_law():
    print("Testing Lesson 14: Central Limit Theorem & Square Root Laws...")
    # Drunkard's walk: 30 steps with X_i in {-1, +1}
    n_steps = 30
    sd_single_step = 1.0
    sd_sum_30 = math.sqrt(n_steps) * sd_single_step
    assert abs(sd_sum_30 - math.sqrt(30)) < 1e-9
    assert abs(sd_sum_30 - 5.4772) < 1e-4

    # S_30 = 2*K - 30 where K ~ Binomial(30, 0.5)
    # S_30 > sqrt(30) <=> S_30 >= 6 <=> K >= 18
    p_exact = sum(math.comb(30, k) * (0.5**30) for k in range(18, 31))
    assert abs(p_exact - 0.1807973040) < 1e-9, f"Exact P(S_30 >= 6) expected 0.1807973040, got {p_exact}"

    # Continuity-corrected normal tail at cutoff 5:
    z_cc = 5.0 / math.sqrt(30)
    p_cc = 0.5 * math.erfc(z_cc / math.sqrt(2.0))
    assert abs(p_cc - 0.1806552143) < 1e-9, f"Continuity corrected normal tail expected 0.1806552143, got {p_cc}"

    # Uncorrected normal tail at cutoff sqrt(30):
    p_uncorr = 0.5 * math.erfc(1.0 / math.sqrt(2.0))
    assert abs(p_uncorr - 0.1586552539) < 1e-9, f"Uncorrected normal tail expected 0.1586552539, got {p_uncorr}"

    # Within 1 SD exact: -sqrt(30) < S_30 < sqrt(30) <=> S_30 in {-4, -2, 0, 2, 4} <=> K in 13..17
    p_within_1sd = sum(math.comb(30, k) * (0.5**30) for k in range(13, 18))
    assert abs(p_within_1sd - 0.6384053919) < 1e-9, f"Within 1 SD exact expected 0.6384053919, got {p_within_1sd}"

    # Dice sums vs averages:
    sd_die = math.sqrt(35 / 12)
    # Sum SE:
    se_s_50 = math.sqrt(50) * sd_die
    se_s_100 = math.sqrt(100) * sd_die
    assert abs(se_s_50 - 12.076) < 1e-3
    assert abs(se_s_100 - 17.078) < 1e-3
    assert se_s_50 < se_s_100, "Sum SE must increase with n"

    # Mean SE:
    se_mean_50 = sd_die / math.sqrt(50)
    se_mean_100 = sd_die / math.sqrt(100)
    assert abs(se_mean_50 - 0.2415) < 1e-4
    assert abs(se_mean_100 - 0.1708) < 1e-4
    assert se_mean_100 < se_mean_50, "Mean SE must decrease with n"
    print("  PASS: Lesson 14 assertions verified.")

def test_lesson_16_confidence_intervals_and_fpc():
    print("Testing Lesson 16: CI definitions, SF food scores & Finite Population Correction...")
    # SF restaurant inspection sample:
    n = 100
    x_bar = 86.27
    s = 9.9
    se = s / math.sqrt(n)
    assert abs(se - 0.99) < 1e-9

    ci_95_low = x_bar - 1.96 * se
    ci_95_high = x_bar + 1.96 * se
    assert abs(ci_95_low - 84.3296) < 1e-4
    assert abs(ci_95_high - 88.2104) < 1e-4

    # FPC calculations:
    # Grimes: N = 400, n = 100
    fpc_grimes = math.sqrt((400 - 100) / (400 - 1))
    assert abs(fpc_grimes - math.sqrt(300 / 399)) < 1e-9
    assert abs(fpc_grimes - 0.8671) < 1e-4

    # Tranquility: N = 800, n = 100
    fpc_tranquility = math.sqrt((800 - 100) / (800 - 1))
    assert abs(fpc_tranquility - math.sqrt(700 / 799)) < 1e-9
    assert abs(fpc_tranquility - 0.9360) < 1e-4

    # Sample proportion CI: n=25, x=9
    p_hat = 9 / 25
    assert p_hat == 0.36
    se_prop = math.sqrt((p_hat * (1 - p_hat)) / 25)
    assert abs(se_prop - math.sqrt(0.36 * 0.64 / 25)) < 1e-9
    assert abs(se_prop - 0.096) < 1e-9
    ci_prop_low = p_hat - 1.96 * se_prop
    ci_prop_high = p_hat + 1.96 * se_prop
    assert abs(ci_prop_low - 0.1718) < 1e-4
    assert abs(ci_prop_high - 0.5482) < 1e-4
    print("  PASS: Lesson 16 assertions verified.")

def test_lesson_19_chi_square_and_benford():
    print("Testing Lesson 19: Chi-square test & Benford's law...")
    # Benford's Law: p_d = log10(1 + 1/d)
    p_benford = {d: math.log10(1 + 1/d) for d in range(1, 10)}
    assert abs(sum(p_benford.values()) - 1.0) < 1e-9
    assert abs(p_benford[1] - math.log10(2)) < 1e-9
    assert abs(p_benford[1] - 0.30103) < 1e-4
    assert abs(p_benford[9] - math.log10(10/9)) < 1e-9
    assert abs(p_benford[9] - 0.04576) < 1e-4

    # Expected counts for n=200 invoices:
    n_invoices = 200
    e_1 = n_invoices * p_benford[1]
    e_9 = n_invoices * p_benford[9]
    assert abs(e_1 - 60.2) < 0.1
    assert abs(e_9 - 9.15) < 0.1
    print("  PASS: Lesson 19 assertions verified.")

def test_lesson_23_simpsons_paradox_and_matching():
    print("Testing Lesson 23: Simpson's Paradox & Nearest Neighbor Distance...")
    # Euclidean distance matching
    # T1 = (3.5, 2.0, 80.0)
    # C1 = (3.4, 2.0, 82.0)
    # C2 = (3.0, 3.0, 75.0)
    # C3 = (3.8, 1.0, 90.0)
    d_t1_c1 = math.sqrt((3.5 - 3.4)**2 + (2.0 - 2.0)**2 + (80.0 - 82.0)**2)
    d_t1_c2 = math.sqrt((3.5 - 3.0)**2 + (2.0 - 3.0)**2 + (80.0 - 75.0)**2)
    d_t1_c3 = math.sqrt((3.5 - 3.8)**2 + (2.0 - 1.0)**2 + (80.0 - 90.0)**2)

    assert abs(d_t1_c1 - math.sqrt(4.01)) < 1e-9
    assert abs(d_t1_c1 - 2.0025) < 1e-4
    assert abs(d_t1_c2 - math.sqrt(26.25)) < 1e-9
    assert abs(d_t1_c2 - 5.1235) < 1e-4
    assert abs(d_t1_c3 - math.sqrt(101.09)) < 1e-9
    assert abs(d_t1_c3 - 10.0544) < 1e-4
    assert d_t1_c1 < d_t1_c2 < d_t1_c3, "C1 must be the nearest neighbor"

    # Simpson's Paradox
    # Tech: Method X = 80/100 (80%), Method Y = 180/250 (72%) -> X > Y
    # Econ: Method X = 120/300 (40%), Method Y = 30/100 (30%) -> X > Y
    p_x_tech = 80 / 100
    p_y_tech = 180 / 250
    assert p_x_tech == 0.80 and p_y_tech == 0.72 and p_x_tech > p_y_tech

    p_x_econ = 120 / 300
    p_y_econ = 30 / 100
    assert p_x_econ == 0.40 and p_y_econ == 0.30 and p_x_econ > p_y_econ

    # Combined:
    p_x_total = (80 + 120) / (100 + 300)
    p_y_total = (180 + 30) / (250 + 100)
    assert p_x_total == 200 / 400 == 0.50
    assert p_y_total == 210 / 350 == 0.60
    assert p_y_total > p_x_total, "Reversal must occur in aggregated data!"
    print("  PASS: Lesson 23 assertions verified.")

def test_lesson_24_25_regression_and_anova():
    print("Testing Lesson 24 & 25: OLS regression slope, intercept & ANOVA...")
    # x = [1, 2, 3, 4, 5], y = [2, 3, 5, 6, 9]
    # b1 = ss_xy / ss_x = 17 / 10 = 1.7
    # b0 = y_bar - b1 * x_bar = 5.0 - 1.7 * 3.0 = 5.0 - 5.1 = -0.1
    b1 = 17.0 / 10.0
    b0 = 5.0 - b1 * 3.0
    assert b1 == 1.7, f"Expected b1=1.7, got {b1}"
    assert abs(b0 - (-0.1)) < 1e-9, f"Expected b0=-0.1, got {b0}"

    # Residuals: y_i - (b0 + b1 * x_i)
    # y_hat: [1.6, 3.3, 5.0, 6.7, 8.4]
    # e_i:   [0.4, -0.3, 0.0, -0.7, 0.6]
    residuals = [2 - (b0 + b1 * 1), 3 - (b0 + b1 * 2), 5 - (b0 + b1 * 3), 6 - (b0 + b1 * 4), 9 - (b0 + b1 * 5)]
    assert abs(sum(residuals)) < 1e-9, "Sum of OLS residuals must equal zero"

    sse = sum(e ** 2 for e in residuals)
    sst = 30.0
    ssm = sst - sse
    r_squared = ssm / sst
    assert abs(r_squared - (17.0 / math.sqrt(300)) ** 2) < 1e-9
    assert abs(r_squared - 0.9633) < 1e-4
    print("  PASS: Lesson 24 & 25 assertions verified.")

def test_lesson_27_logistic_regression():
    print("Testing Lesson 27: Logistic odds and log-odds...")
    # Logistic function: p(x) = 1 / (1 + e^-(b0 + b1 * x))
    b0 = -2.0
    b1 = 0.5
    for x in [-2, 0, 2, 4]:
        logit = b0 + b1 * x
        p = 1 / (1 + math.exp(-logit))
        odds = p / (1 - p)
        assert abs(math.log(odds) - logit) < 1e-9, "Log-odds must match linear predictor"
    print("  PASS: Lesson 27 assertions verified.")

def main():
    print("=== STARTING XSTK AUDIT NUMERICAL & CONCEPTUAL ASSERT SUITE ===")
    test_lesson_04_07_summary_and_correlation()
    test_lesson_09_10_probability_foundations()
    test_lesson_11_12_random_variables_and_distributions()
    test_lesson_13_expectation_and_sd()
    test_lesson_14_clt_and_square_root_law()
    test_lesson_16_confidence_intervals_and_fpc()
    test_lesson_19_chi_square_and_benford()
    test_lesson_23_simpsons_paradox_and_matching()
    test_lesson_24_25_regression_and_anova()
    test_lesson_27_logistic_regression()
    print("\n=== ALL XSTK NUMERICAL & CONCEPTUAL TESTS PASSED SUCCESSFULLY! ===")

if __name__ == '__main__':
    main()
