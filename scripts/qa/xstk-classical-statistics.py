"""QA Numerical Verification Script for XSTK Classical Statistics Track (Lessons 36-44).
Verifies all worked examples, exercises, test statistics, p-values, quantiles,
and confidence intervals across the entire statistics track.
"""
import math
import sys
import itertools
import numpy as np
from scipy import stats

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def test_lesson_36():
    print("Testing Lesson 36: Phân phối mẫu chính xác...")
    # Example 1: Sample mean normal probability
    # n = 16, mu = 100, sigma = 16 => SE = 4
    se1 = 16 / math.sqrt(16)
    assert se1 == 4.0
    p1 = stats.norm.cdf(104, 100, 4) - stats.norm.cdf(96, 100, 4)
    assert abs(p1 - 0.682689) < 1e-4

    # Example 2: Unbiased sample variance S^2
    data2 = [12, 15, 14, 11, 18]
    x_bar2 = sum(data2) / len(data2)
    assert x_bar2 == 14.0
    ss2 = sum((x - x_bar2)**2 for x in data2)
    assert ss2 == 30.0
    s2 = ss2 / (len(data2) - 1)
    assert s2 == 7.5
    s = math.sqrt(s2)
    assert abs(s - 2.73861) < 1e-4

    # Example 3: Chi-square sample variance
    # n = 10, sigma^2 = 25, df = 9
    # P(S^2 > 40) = P(chi^2(9) > 9 * 40 / 25 = 14.4)
    p3 = 1 - stats.chi2.cdf(14.4, df=9)
    assert abs(p3 - 0.10878) < 1e-4

    # Example 4: Student t-distribution
    # n = 9, x_bar = 52.4, mu0 = 50, s = 3.6 => SE = 3.6 / 3 = 1.2
    # t = (52.4 - 50) / 1.2 = 2.0
    t4 = (52.4 - 50) / (3.6 / 3)
    assert abs(t4 - 2.0) < 1e-9
    p4 = 1 - stats.t.cdf(2.0, df=8)
    assert abs(p4 - 0.04034) < 1e-4

    # Example 5: Fisher F-distribution
    # F(10, 15)
    f_crit5 = stats.f.ppf(0.95, 10, 15)
    assert abs(f_crit5 - 2.5437) < 1e-3
    f_inv5 = stats.f.ppf(0.05, 10, 15)
    f_recip = 1 / stats.f.ppf(0.95, 15, 10)
    assert abs(f_inv5 - f_recip) < 1e-6
    assert abs(f_inv5 - 0.3515) < 1e-3

    # Exercise 1: P(X_bar > 83), n = 25, mu = 80, sigma = 10
    se_ex1 = 10 / math.sqrt(25)
    z_ex1 = (83 - 80) / se_ex1
    assert z_ex1 == 1.5
    p_ex1 = 1 - stats.norm.cdf(1.5)
    assert abs(p_ex1 - 0.066807) < 1e-4

    # Exercise 2: S^2 for [5, 7, 8, 12]
    d_ex2 = [5, 7, 8, 12]
    assert np.var(d_ex2, ddof=1) == 26 / 3

    # Exercise 3: Chi-square quantile
    q_ex3 = stats.chi2.ppf(0.95, df=12)
    assert abs(q_ex3 - 21.0261) < 1e-3

    # Exercise 4: Student t quantile df=15
    t_ex4 = stats.t.ppf(0.95, df=15)
    assert abs(t_ex4 - 1.75305) < 1e-3

    # Exercise 5: F(8, 8) quantile
    f_ex5 = stats.f.ppf(0.95, 8, 8)
    assert abs(f_ex5 - 3.4381) < 1e-3
    print("Lesson 36 passed!")

def test_lesson_37():
    print("Testing Lesson 37: Ước lượng điểm...")
    # Example 1: MOM Poisson
    d1 = [2, 4, 1, 3, 5, 3]
    lambda_mom = sum(d1) / len(d1)
    assert lambda_mom == 3.0

    # Example 2: MOM Uniform(0, theta)
    d2 = [2, 5, 8, 9]
    theta_mom = 2 * (sum(d2) / len(d2))
    assert theta_mom == 12.0

    # Example 3: MLE Exponential
    d3 = [0.5, 1.2, 0.8, 1.5]
    lambda_mle = len(d3) / sum(d3)
    assert lambda_mle == 1.0

    # Example 4: Normal sigma^2 MLE vs S^2
    d4 = [10, 12, 14, 16, 18]
    n4 = len(d4)
    xbar4 = sum(d4) / n4
    ss4 = sum((x - xbar4)**2 for x in d4)
    assert ss4 == 40.0
    sigma2_mle = ss4 / n4
    s2_unbiased = ss4 / (n4 - 1)
    assert sigma2_mle == 8.0
    assert s2_unbiased == 10.0

    # Example 5: Uniform(0, theta) MLE
    d5 = [3.2, 7.8, 5.4, 8.9]
    theta_mle = max(d5)
    assert theta_mle == 8.9

    # Exercise 1: MSE comparison
    # n = 9, mu = 2
    # Var(T1) = 1/9, Bias(T1) = 0 => MSE(T1) = 1/9 = 0.1111...
    # T2 = 0.9 * X_bar => Bias = -0.2 => Bias^2 = 0.04
    # Var(T2) = 0.81 * (1/9) = 0.09 => MSE(T2) = 0.13
    mse_t1 = 1 / 9
    mse_t2 = 0.04 + 0.81 * (1 / 9)
    assert abs(mse_t1 - 0.11111) < 1e-4
    assert abs(mse_t2 - 0.13) < 1e-9
    assert mse_t1 < mse_t2

    # Exercise 2: Gamma MOM
    # xbar = 6, central sample moment m2 = 12 (denominator n).
    # Gamma uses the rate beta: beta = 6/12, alpha = 36/12.
    beta_ex2 = 6.0 / 12.0
    alpha_ex2 = 36.0 / 12.0
    assert beta_ex2 == 0.5
    assert alpha_ex2 == 3.0

    # Exercise 3: Bernoulli MLE
    p_ex3 = 14 / 20
    var_p_ex3 = 0.7 * 0.3 / 20
    assert p_ex3 == 0.7
    assert abs(var_p_ex3 - 0.0105) < 1e-6

    # Exercise 4: Unbiased uniform estimator
    n_ex4 = 4
    x_max = 8.0
    theta_unb = (n_ex4 + 1) / n_ex4 * x_max
    assert theta_unb == 10.0
    print("Lesson 37 passed!")

def test_lesson_38():
    print("Testing Lesson 38: Tính đủ và hiệu quả...")
    # Example 4: Poisson Fisher information
    # I(lambda) = 1/lambda, CRLB = lambda / n
    # For lambda = 4, n = 10 => CRLB = 0.4
    crlb_pois = 4.0 / 10
    assert crlb_pois == 0.4

    # Exercise 2: Bernoulli Fisher information
    # I(p) = 1 / (p*(1-p)), CRLB = p*(1-p)/n
    p = 0.4
    n = 25
    crlb_bern = (p * (1 - p)) / n
    assert abs(crlb_bern - 0.0096) < 1e-6

    # Exercise 5: Relative efficiency of median vs mean in Normal
    # ARE = 2 / pi approx 0.636619
    are = 2 / math.pi
    assert abs(are - 0.63662) < 1e-4
    print("Lesson 38 passed!")

def test_lesson_39():
    print("Testing Lesson 39: Khoảng tin cậy tham số...")
    # Example 1: One-sample t CI
    # n = 16, x_bar = 22.5, s = 4.0, alpha = 0.05, df = 15
    t_crit1 = stats.t.ppf(0.975, df=15)
    se1 = 4.0 / math.sqrt(16)
    me1 = t_crit1 * se1
    ci1_low = 22.5 - me1
    ci1_high = 22.5 + me1
    assert abs(t_crit1 - 2.13145) < 1e-4
    assert abs(ci1_low - 20.36855) < 1e-4
    assert abs(ci1_high - 24.63145) < 1e-4

    # Example 2: Paired t CI
    diffs = [3.0, 5.0, 2.0, 4.0, 6.0, 4.0]
    n2 = len(diffs)
    d_bar = sum(diffs) / n2
    assert d_bar == 4.0
    s_d = np.std(diffs, ddof=1)
    assert abs(s_d - math.sqrt(2.0)) < 1e-6
    se2 = s_d / math.sqrt(n2)
    t_crit2 = stats.t.ppf(0.975, df=n2-1)
    assert abs(t_crit2 - 2.57058) < 1e-4
    me2 = t_crit2 * se2
    assert abs(me2 - 1.48413) < 1e-4
    assert abs((d_bar - me2) - 2.51587) < 1e-4
    assert abs((d_bar + me2) - 5.48413) < 1e-4

    # Example 3: Welch two-sample t CI
    n_a, xbar_a, s_a = 10, 82.0, 6.0
    n_b, xbar_b, s_b = 12, 75.0, 4.0
    diff3 = xbar_a - xbar_b
    assert diff3 == 7.0
    v_a = s_a**2 / n_a # 3.6
    v_b = s_b**2 / n_b # 16 / 12 = 1.333333
    se3 = math.sqrt(v_a + v_b)
    df_welch = (v_a + v_b)**2 / (v_a**2 / (n_a - 1) + v_b**2 / (n_b - 1))
    assert abs(df_welch - 15.196) < 1e-2
    df3 = int(math.floor(df_welch))
    assert df3 == 15
    t_crit3 = stats.t.ppf(0.975, df=df3)
    assert abs(t_crit3 - 2.13145) < 1e-4
    me3 = t_crit3 * se3
    assert abs(me3 - 4.7342) < 1e-3
    assert abs((diff3 - me3) - 2.2658) < 1e-3
    assert abs((diff3 + me3) - 11.7342) < 1e-3

    # Example 4: Wald vs Wilson proportion CI
    n4 = 40
    p_hat4 = 6 / 40 # 0.15
    z = 1.96
    se_wald = math.sqrt(p_hat4 * (1 - p_hat4) / n4)
    me_wald = z * se_wald
    wald_low = p_hat4 - me_wald
    wald_high = p_hat4 + me_wald
    assert abs(wald_low - 0.03934) < 1e-4
    assert abs(wald_high - 0.26066) < 1e-4

    denom = 1 + z**2 / n4
    center_wilson = (p_hat4 + z**2 / (2 * n4)) / denom
    margin_wilson = (z * math.sqrt(p_hat4 * (1 - p_hat4) / n4 + z**2 / (4 * n4**2))) / denom
    wilson_low = center_wilson - margin_wilson
    wilson_high = center_wilson + margin_wilson
    assert abs(wilson_low - 0.0706) < 1e-3
    assert abs(wilson_high - 0.2907) < 1e-3

    # Example 5: Ratio of variances F CI
    # n1 = 10, s1^2 = 24, n2 = 12, s2^2 = 10
    ratio = 24.0 / 10.0
    f_high = stats.f.ppf(0.975, 9, 11)
    f_low = stats.f.ppf(0.025, 9, 11)
    assert abs(f_high - 3.5879) < 1e-3
    assert abs(f_low - 0.2556) < 1e-3
    ci_f_low = ratio / f_high
    ci_f_high = ratio / f_low
    assert abs(ci_f_low - 0.6689) < 1e-3
    assert abs(ci_f_high - 9.389) < 1e-2

    # Exercise 1: Sample size for mean
    # E = 1.5, sigma = 6.0, z = 1.96
    n_mean_req = (1.96 * 6.0 / 1.5)**2
    assert math.ceil(n_mean_req) == 62

    # Exercise 2: Sample size for proportion
    # E = 0.03, p = 0.5, z = 1.96
    n_prop_req = 1.96**2 * 0.25 / 0.03**2
    assert math.ceil(n_prop_req) == 1068

    # Exercise 3: Variance chi-square CI
    # n = 15, s^2 = 18.5, df = 14
    chi2_hi = stats.chi2.ppf(0.975, 14)
    chi2_lo = stats.chi2.ppf(0.025, 14)
    assert abs(chi2_hi - 26.1189) < 1e-3
    assert abs(chi2_lo - 5.6287) < 1e-3
    ci_var_low = 14 * 18.5 / chi2_hi
    ci_var_high = 14 * 18.5 / chi2_lo
    assert abs(ci_var_low - 9.916) < 1e-2
    assert abs(ci_var_high - 46.013963952) < 1e-8
    print("Lesson 39 passed!")

def test_lesson_40():
    print("Testing Lesson 40: Kiểm định tham số...")
    # Example 1: Two-sided z-test
    # mu0 = 100, sigma = 15, n = 36, xbar = 105.2
    se1 = 15 / math.sqrt(36)
    z1 = (105.2 - 100) / se1
    assert abs(z1 - 2.08) < 1e-9
    p1 = 2 * (1 - stats.norm.cdf(z1))
    assert abs(p1 - 0.03752) < 1e-4

    # Example 2: One-sided t-test
    # n = 10, xbar = 2.3, s = 2.5
    se2 = 2.5 / math.sqrt(10)
    t2 = 2.3 / se2
    assert abs(t2 - 2.9093) < 1e-3
    p2 = 1 - stats.t.cdf(t2, df=9)
    assert abs(p2 - 0.00868) < 1e-4

    # Example 3: Neyman-Pearson MP test
    # mu0 = 0, mu1 = 2, sigma = 1, alpha = 0.05
    c3 = stats.norm.ppf(0.95)
    assert abs(c3 - 1.64485) < 1e-4
    power3 = 1 - stats.norm.cdf(c3 - 2.0)
    assert abs(power3 - 0.63876) < 1e-4

    # Example 4: Two proportions pooled test
    # n1 = 120, x1 = 36, n2 = 150, x2 = 30
    p1_hat = 36 / 120 # 0.30
    p2_hat = 30 / 150 # 0.20
    p_pool = (36 + 30) / (120 + 150) # 66 / 270 = 0.244444
    se_pool = math.sqrt(p_pool * (1 - p_pool) * (1/120 + 1/150))
    z4 = (p1_hat - p2_hat) / se_pool
    assert abs(z4 - 1.8998) < 1e-3
    p4 = 2 * (1 - stats.norm.cdf(z4))
    assert abs(p4 - 0.05745) < 1e-4

    # Exercise 1: Sample size for power = 0.80, alpha = 0.05
    # mu1 - mu0 = 3, sigma = 6
    z_a = stats.norm.ppf(0.95)
    z_b = stats.norm.ppf(0.80)
    n_req = ((z_a + z_b) * 6.0 / 3.0)**2
    assert math.ceil(n_req) == 25

    # Exercise 2: Variance chi-square test
    # n = 20, s^2 = 1.8, sigma0^2 = 1.0
    chi2_stat = 19 * 1.8 / 1.0
    assert abs(chi2_stat - 34.2) < 1e-9
    p_chi2 = 1 - stats.chi2.cdf(34.2, df=19)
    assert abs(p_chi2 - 0.01740408008) < 1e-10
    print("Lesson 40 passed!")

def test_lesson_41():
    print("Testing Lesson 41: Kiểm định Chi bình phương...")
    # Example 1: Mendel goodness of fit
    obs1 = [95, 25, 28, 12]
    exp1 = [90, 30, 30, 10]
    chi2_val1, p_val1 = stats.chisquare(obs1, f_exp=exp1)
    assert abs(chi2_val1 - 1.6444) < 1e-3
    assert abs(p_val1 - 0.6493) < 1e-3

    # Example 2: 2x3 contingency table
    table2 = np.array([[30, 20, 10], [20, 30, 40]])
    chi2_val2, p_val2, dof2, exp2 = stats.chi2_contingency(table2, correction=False)
    assert dof2 == 2
    assert abs(chi2_val2 - 16.6667) < 1e-3
    assert abs(p_val2 - 0.00024) < 1e-4
    cramer_v = math.sqrt(chi2_val2 / (150 * min(2-1, 3-1)))
    assert abs(cramer_v - 0.3333) < 1e-3

    # Example 4: Fisher exact test
    table4 = [[3, 1], [1, 5]]
    odds, p_fisher_two = stats.fisher_exact(table4, alternative='two-sided')
    odds, p_fisher_less = stats.fisher_exact(table4, alternative='greater')
    # Hypergeometric P(X=3) = 24/210, P(X=4) = 1/210 => sum = 25/210 = 0.119047
    assert abs(p_fisher_less - 25/210) < 1e-5

    # Exercise 1: Die balance
    obs_die = [15, 28, 17, 22, 18, 20]
    chi2_die, p_die = stats.chisquare(obs_die)
    assert abs(chi2_die - 5.30) < 1e-6
    assert abs(p_die - 0.3802) < 1e-3

    # Exercise 2: 2x2 table phi
    table_ex2 = np.array([[40, 10], [20, 30]])
    chi2_ex2, _, _, _ = stats.chi2_contingency(table_ex2, correction=False)
    assert abs(chi2_ex2 - 16.6667) < 1e-3
    phi = math.sqrt(chi2_ex2 / 100)
    assert abs(phi - 0.4082) < 1e-3
    print("Lesson 41 passed!")

def test_lesson_42():
    print("Testing Lesson 42: Phân tích phương sai ANOVA...")
    # Example 1: One-way ANOVA
    g1 = [6, 8, 7, 7]
    g2 = [8, 9, 10, 9]
    g3 = [10, 11, 11, 12]
    f_val, p_val = stats.f_oneway(g1, g2, g3)
    assert abs(f_val - 24.0) < 1e-6
    assert abs(p_val - 0.000247) < 1e-5

    # Sums of squares
    all_y = g1 + g2 + g3
    grand_mean = np.mean(all_y)
    assert grand_mean == 9.0
    ssb = 4 * ((np.mean(g1) - 9)**2 + (np.mean(g2) - 9)**2 + (np.mean(g3) - 9)**2)
    assert ssb == 32.0
    ssw = sum((y - np.mean(g1))**2 for y in g1) + \
          sum((y - np.mean(g2))**2 for y in g2) + \
          sum((y - np.mean(g3))**2 for y in g3)
    assert ssw == 6.0
    sst = sum((y - grand_mean)**2 for y in all_y)
    assert sst == 38.0
    assert ssb + ssw == sst

    # F critical
    f_crit = stats.f.ppf(0.95, 2, 9)
    assert abs(f_crit - 4.2565) < 1e-3

    # Tukey HSD q critical for k=3, df=9
    # studentized range quantile for alpha=0.05
    q_crit = stats.studentized_range.ppf(0.95, 3, 9)
    assert abs(q_crit - 3.9486) < 1e-3
    hsd = q_crit * math.sqrt((6.0 / 9) / 4)
    assert abs(hsd - 1.6119) < 1e-3

    # Exercise 2: FWER
    fwer = 1 - (1 - 0.05)**6
    assert abs(fwer - 0.2649) < 1e-3

    # Exercise 4: Eta-squared
    eta2 = ssb / sst
    assert abs(eta2 - 32 / 38) < 1e-6
    print("Lesson 42 passed!")

def test_lesson_43():
    print("Testing Lesson 43: Suy luận hồi quy tuyến tính...")
    x = np.array([1, 2, 3, 4, 5])
    y = np.array([2, 3, 5, 4, 6])
    n = len(x)

    x_bar = np.mean(x)
    y_bar = np.mean(y)
    assert x_bar == 3.0 and y_bar == 4.0

    s_xx = np.sum((x - x_bar)**2)
    s_yy = np.sum((y - y_bar)**2)
    s_xy = np.sum((x - x_bar) * (y - y_bar))
    assert s_xx == 10.0 and s_yy == 10.0 and s_xy == 9.0

    beta1 = s_xy / s_xx
    beta0 = y_bar - beta1 * x_bar
    assert abs(beta1 - 0.90) < 1e-9 and abs(beta0 - 1.30) < 1e-9

    y_hat = beta0 + beta1 * x
    residuals = y - y_hat
    rss = np.sum(residuals**2)
    assert abs(rss - 1.90) < 1e-9

    s_e2 = rss / (n - 2)
    assert abs(s_e2 - 1.90 / 3) < 1e-9
    s_e = math.sqrt(s_e2)
    assert abs(s_e - 0.79582) < 1e-4

    se_beta1 = s_e / math.sqrt(s_xx)
    assert abs(se_beta1 - 0.25166) < 1e-4
    t_stat = beta1 / se_beta1
    assert abs(t_stat - 3.576) < 1e-3
    p_slope = 2 * (1 - stats.t.cdf(t_stat, df=3))
    assert abs(p_slope - 0.0374) < 1e-3

    t_crit = stats.t.ppf(0.975, df=3)
    assert abs(t_crit - 3.18245) < 1e-4

    ci_slope_low = beta1 - t_crit * se_beta1
    ci_slope_high = beta1 + t_crit * se_beta1
    assert abs(ci_slope_low - 0.0991) < 1e-3
    assert abs(ci_slope_high - 1.7009) < 1e-3

    # Confidence interval for E(Y|X=3)
    se_mean_3 = s_e * math.sqrt(1/n + (3 - x_bar)**2 / s_xx)
    me_mean_3 = t_crit * se_mean_3
    assert abs(me_mean_3 - 1.1326) < 1e-3
    assert abs((4.0 - me_mean_3) - 2.8674) < 1e-3
    assert abs((4.0 + me_mean_3) - 5.1326) < 1e-3

    # Prediction interval for Y_new at X=3
    se_pred_3 = s_e * math.sqrt(1 + 1/n + (3 - x_bar)**2 / s_xx)
    me_pred_3 = t_crit * se_pred_3
    assert abs(me_pred_3 - 2.7744) < 1e-3
    assert abs((4.0 - me_pred_3) - 1.2256) < 1e-3
    assert abs((4.0 + me_pred_3) - 6.7744) < 1e-3

    # Exercise 1: Intercept SE
    se_beta0 = s_e * math.sqrt(1/n + x_bar**2 / s_xx)
    assert abs(se_beta0 - 0.83467) < 1e-4
    me_beta0 = t_crit * se_beta0
    assert abs(me_beta0 - 2.6563) < 1e-3
    assert abs((1.30 - me_beta0) - (-1.3563)) < 1e-3
    assert abs((1.30 + me_beta0) - 3.9563) < 1e-3
    print("Lesson 43 passed!")

def test_lesson_44():
    print("Testing Lesson 44: Phương pháp phi tham số...")
    # Example 1: Sign test
    # n = 9 non-zero diffs, k = 7 positive
    # Binomial(9, 0.5)
    p_sign = 2 * (1 - stats.binom.cdf(6, 9, 0.5))
    # P(K >= 7) = P(7) + P(8) + P(9) = (36 + 9 + 1) / 512 = 46 / 512 = 0.08984375
    # Two-sided p = 2 * 46 / 512 = 92 / 512 = 0.1796875
    assert abs(p_sign - 0.17969) < 1e-4

    # Example 2: Wilcoxon signed-rank test
    diffs = np.array([2, 5, -2, 4, 7, 3, -1, 6, 8])
    # T+ and T-
    res_wilc = stats.wilcoxon(diffs)
    # T- ranks: |-1| has rank 1, |-2| has rank 2.5 => T- = 3.5
    # T+ ranks: 45 - 3.5 = 41.5
    # W = 3.5
    assert res_wilc.statistic == 3.5

    # Example 3: Mann-Whitney U
    n1 = [12, 15, 18, 20]
    n2 = [8, 10, 11, 14, 16]
    res_mw = stats.mannwhitneyu(n1, n2, alternative='two-sided')
    assert res_mw.statistic == 17.0
    u_min = min(res_mw.statistic, len(n1)*len(n2) - res_mw.statistic)
    assert u_min == 3.0
    assert abs(res_mw.pvalue - 0.1111) < 1e-3

    # Example 4: Spearman rank correlation
    d_x = [1, 2, 3, 4, 5]
    d_y = [2, 1, 4, 5, 3]
    rho, p_rho = stats.spearmanr(d_x, d_y)
    assert abs(rho - 0.60) < 1e-6

    # Example 5: Kolmogorov-Smirnov test for Uniform(0, 1)
    sample_ks = [0.10, 0.25, 0.40, 0.70, 0.85]
    res_ks = stats.kstest(sample_ks, 'uniform')
    # D+ = max(i/5 - x_i) = max(0.2-0.1, 0.4-0.25, 0.6-0.4, 0.8-0.7, 1.0-0.85) = max(0.1, 0.15, 0.2, 0.1, 0.15) = 0.20
    # D- = max(x_i - (i-1)/5) = max(0.1-0, 0.25-0.2, 0.4-0.4, 0.7-0.6, 0.85-0.8) = max(0.1, 0.05, 0, 0.1, 0.05) = 0.10
    # D = 0.20
    assert abs(res_ks.statistic - 0.20) < 1e-6
    print("Lesson 44 passed!")

def test_remaining_examples():
    """Complete coverage, including exact tied-rank tests and all exercise numbers."""
    from scipy.integrate import quad
    # 36: both tails of the Student example and rounded cutoffs in exercises.
    assert abs(2 * stats.t.sf(2, 8) - .080516238) < 1e-8
    assert abs(stats.t.cdf(1.753, 15) - stats.t.cdf(-1.753, 15) - .9) < 1e-5
    assert abs(stats.f.sf(3.44, 8, 8) - .05) < 1e-4
    # Symmetric nonnormal example: uncorrelated mean/variance, but dependent.
    outcomes = np.array(list(itertools.product([-1., 1.], repeat=2)))
    means, variances = outcomes.mean(axis=1), outcomes.var(axis=1, ddof=1)
    assert abs(np.cov(means, variances, ddof=0)[0, 1]) < 1e-12
    assert np.all(variances[means == 0] == 2) and np.all(variances[means != 0] == 0)
    # 37: second uniform example, normal MLE standard deviation, MSE inequality.
    assert abs(2 * np.mean([3.2, 7.8, 5.4, 8.9]) - 12.65) < 1e-12
    assert abs(np.std([10, 12, 14, 16, 18], ddof=0) - math.sqrt(8)) < 1e-12
    for n in range(2, 101):
        assert abs(2 * (n - 1) / n**2 + (-1/n)**2 - (2*n-1)/n**2) < 1e-12
        assert (2*n-1)/n**2 < 2/(n-1)
    # 38: conditional Bernoulli Rao–Blackwell calculation for every total.
    n, p = 5, .4
    outcomes = np.array(list(itertools.product([0, 1], repeat=n)))
    totals = outcomes.sum(axis=1)
    for t in range(n+1):
        assert abs(outcomes[totals == t, 0].mean() - t/n) < 1e-12
    weights = p**totals * (1-p)**(n-totals)
    assert abs(np.dot(weights, (outcomes[:, 0]-p)**2) - p*(1-p)) < 1e-12
    assert abs(np.dot(weights, (totals/n-p)**2) - p*(1-p)/n) < 1e-12
    # Fisher information for the known-variance normal example and uniform variance.
    assert abs(stats.norm.expect(lambda x: ((x-2)/9)**2, loc=2, scale=3) - 1/9) < 1e-10
    n, theta = 4, 10.
    expected = quad(lambda x: (n+1)/n*x*n*x**(n-1)/theta**n, 0, theta)[0]
    variance = quad(lambda x: ((n+1)/n*x-theta)**2*n*x**(n-1)/theta**n, 0, theta)[0]
    assert abs(expected-theta) < 1e-10
    assert abs(variance-theta**2/(n*(n+2))) < 1e-10
    assert abs(math.pi/2 - 1.570796327) < 1e-9
    # 39 exercise 4: difference in proportions, then percentage points.
    margin = 1.96 * math.sqrt(.15*.85/300 + .06*.94/400)
    np.testing.assert_allclose([.09-margin, .09+margin], [.04337, .13663], atol=5e-5, rtol=0)
    np.testing.assert_allclose(100*np.array([.09-margin, .09+margin]), [4.337, 13.663], atol=.001, rtol=0)
    # 40: exact power after rounding up, both F-test critical values, paired t exercise.
    power25 = stats.norm.sf(stats.norm.isf(.05)-3*math.sqrt(25)/6)
    power24 = stats.norm.sf(stats.norm.isf(.05)-3*math.sqrt(24)/6)
    assert power25 >= .8 and power24 < .8
    assert abs(stats.f.isf(.025, 10, 15)-3.0601968514) < 1e-9
    assert abs(stats.f.ppf(.025, 10, 15)-.2839559299) < 1e-9
    assert abs(2*stats.f.sf(3, 10, 15)-.054071895) < 1e-8
    d = np.array([25, 32, 28, 35, 30])
    assert d.mean() == 30 and np.sum((d-30)**2) == 58
    assert abs(d.var(ddof=1)-14.5) < 1e-12
    t = 30/math.sqrt(14.5/5)
    assert abs(t-17.6166065854) < 1e-9
    assert abs(stats.t.sf(t, 4)-.0000304901863) < 1e-12
    # 41: group fitting degrees of freedom, 3x3 V, all relevant quantiles.
    assert 10-1-2 == 7
    assert (3-1)*(3-1) == 4
    assert abs(math.sqrt(18/(300*2))-.1732050808) < 1e-9
    assert abs(stats.chi2.isf(.05, 4)-9.487729037) < 1e-8
    assert abs(stats.chi2.isf(.05, 3)-7.814727903) < 1e-8
    assert abs(stats.chi2.isf(.05, 5)-11.070497694) < 1e-8
    # 42: every exercise and multiple-comparison example.
    assert math.comb(4, 2) == 6 and math.comb(10, 2) == 45
    assert math.comb(5, 2) == 10
    assert abs((1-.95**10)-.401263061) < 1e-9
    assert .05/10 == .005 and min(1, 10*.05) == .5
    assert abs(32/38-.842105263) < 1e-9
    assert 900-180 == 720 and 180/3/(720/36) == 3
    assert abs(stats.f.isf(.01, 3, 36)-4.377095621) < 1e-9
    assert [3-1, 4-1, (3-1)*(4-1), 3*4*(5-1)] == [2, 3, 6, 48]
    assert sum([2, 3, 6, 48]) == 3*4*5-1 == 59
    # 43: R2, adjusted R2, F=t2, extrapolation and hat matrix exercise.
    x, y = np.array([1.,2.,3.,4.,5.]), np.array([2.,3.,5.,4.,6.])
    design = np.column_stack([np.ones(5), x])
    b = np.linalg.lstsq(design, y, rcond=None)[0]
    residuals = y-design@b
    np.testing.assert_allclose(residuals, [-.2, -.1, 1, -.9, .2], atol=1e-12)
    rss = np.dot(residuals, residuals)
    assert abs(1-rss/10-.81) < 1e-12
    assert abs(1-(rss/10)*4/3-.7466666667) < 1e-9
    f = (10-rss)/(rss/3)
    t = b[1]/math.sqrt(rss/3/10)
    assert abs(f-t*t) < 1e-12 and abs(f-12.789473684) < 1e-9
    assert abs(math.sqrt(2.7/.2)-3.674234614) < 1e-9
    hat = design@np.linalg.inv(design.T@design)@design.T
    np.testing.assert_allclose(hat.T, hat, atol=1e-12)
    np.testing.assert_allclose(hat@hat, hat, atol=1e-12)
    np.testing.assert_allclose(hat@y, design@b, atol=1e-12)
    assert abs(np.trace(hat)-2) < 1e-12
    # 44: exact signed-rank p-value with the observed ties, using all 512 signs.
    d = np.array([2, 5, -2, 4, 7, 3, -1, 6, 8])
    ranks = stats.rankdata(abs(d))
    assert ranks[d<0].sum() == 3.5 and ranks[d>0].sum() == 41.5
    sums = np.array([np.dot(mask, ranks) for mask in itertools.product([0,1], repeat=9)])
    assert sum(sums <= 3.5) == 6 and sum(sums >= 41.5) == 6
    assert np.mean((sums <= 3.5)|(sums >= 41.5)) == 12/512
    assert abs(np.var(sums)-np.sum(ranks**2)/4) < 1e-12
    # Exact Mann–Whitney permutation tails, not a no-ties table approximation.
    values = [sum(c)-10 for c in itertools.combinations(range(1,10), 4)]
    assert len(values) == 126 and sum(u <= 3 for u in values) == 7
    assert sum(u >= 17 for u in values) == 7
    assert abs(stats.mannwhitneyu([12,15,18,20],[8,10,11,14,16],method='exact').pvalue-14/126) < 1e-12
    # Numerical ECDF example plus exact finite-n critical value.
    x = np.array([.10,.25,.40,.70,.85])
    np.testing.assert_allclose(np.arange(1,6)/5-x, [.1,.15,.2,.1,.15], atol=1e-12)
    np.testing.assert_allclose(x-np.arange(5)/5, [.1,.05,0,.1,.05], atol=1e-12)
    assert abs(stats.kstwo.isf(.05,5)-.563275198366) < 1e-12
    # Wilcoxon ties/zeros and equal-group Mann–Whitney exercises.
    d = np.array([-3,-1,0,2,2,4,5]); d = d[d != 0]
    r = stats.rankdata(abs(d))
    assert len(d) == 6 and r[d<0].sum() == 5 and r[d>0].sum() == 16
    assert 48-6*7/2 == 27 and 78-48 == 30 and 30-6*7/2 == 9
    assert abs(3/math.pi-.9549296586) < 1e-10
    # Figure-specific numerical captions, distinct from the main worked examples.
    assert 100/16 == 6.25
    assert 7/10 == .7 and 3 == len([2, 4, 8.5])
    assert abs(.4*.6/4-.06) < 1e-12
    assert abs(stats.chi2.ppf(.025,9)-2.7003895) < 1e-7
    assert abs(stats.chi2.ppf(.975,9)-19.0227678) < 1e-7
    assert abs(2*stats.norm.sf(2.3)-.02144822004) < 1e-10
    assert abs(stats.norm.cdf(stats.norm.isf(.05)-2.5)-.19623505998) < 1e-10
    q, _ = stats.chisquare([85,30,15,70], [80,35,15,70])
    assert abs(q-1.0267857143) < 1e-10
    _, _, _, expected = stats.chi2_contingency([[20,30,10],[30,10,20]], correction=False)
    np.testing.assert_allclose(expected, [[25,20,15],[25,20,15]], atol=1e-12)
    groups = np.array([[2,3,4],[4,5,6],[6,7,8]])
    ssb = sum(3*(g.mean()-groups.mean())**2 for g in groups)
    ssw = sum(sum((g-g.mean())**2) for g in groups)
    assert ssb == 24 and ssw == 6 and sum((groups.flatten()-5)**2) == 30
    assert stats.f_oneway(*groups).statistic == 12
    assert abs(stats.f.sf(4.5,3,20)-.01437324461) < 1e-10
    assert abs(stats.t.isf(.025,13)-2.160368656) < 1e-9
    normal_ks = stats.kstest([-1.2,-.4,.2,.8,1.5], 'norm')
    assert abs(normal_ks.statistic-.1881446014166) < 1e-12
    assert abs(stats.norm.cdf(.8)-.6-normal_ks.statistic) < 1e-12
    means = np.random.default_rng(20261020).normal(50,1.2,20)
    assert sum(abs(means-50) <= stats.norm.isf(.025)*1.2) == 18
    phat, z, n = 2/30, stats.norm.isf(.025), 30
    margin = z*math.sqrt(phat*(1-phat)/n)
    np.testing.assert_allclose([phat-margin,phat+margin],[-.02259402,.15592735],atol=1e-8)
    wilson = stats.binomtest(2,30).proportion_ci(method='wilson')
    np.testing.assert_allclose([wilson.low,wilson.high],[.01847702,.21323458],atol=1e-8)
    print('Remaining exercises, exact ties/permutations, all nine modules: passed!')

def main():
    test_lesson_36()
    test_lesson_37()
    test_lesson_38()
    test_lesson_39()
    test_lesson_40()
    test_lesson_41()
    test_lesson_42()
    test_lesson_43()
    test_lesson_44()
    test_remaining_examples()
    print("\nALL 9 LESSONS NUMERICAL TESTS PASSED SUCCESSFULLY!")

if __name__ == "__main__":
    main()
