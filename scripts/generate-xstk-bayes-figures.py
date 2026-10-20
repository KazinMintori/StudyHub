"""Verify the Bayes lesson examples and reproduce its three scientific figures."""
from pathlib import Path
from fractions import Fraction
import math
import sys
from io import BytesIO
import numpy as np
from scipy import integrate, stats
from xstk_figure_style import configure_matplotlib, polish_svg, PALETTE


def verify():
    assert Fraction(8, 10) * Fraction(1, 10) / (
        Fraction(8, 10) * Fraction(1, 10) + Fraction(2, 10) * Fraction(9, 10)
    ) == Fraction(4, 13)
    assert math.isclose(integrate.quad(lambda p: 20*p**3*(1-p), 0, 1)[0], 1)
    assert math.isclose(stats.beta.mean(4, 2), 2/3)
    assert math.isclose(stats.beta.var(4, 2), 2/63)
    assert math.isclose(stats.beta.sf(.5, 4, 2), 13/16)
    assert np.allclose(stats.beta.ppf([.025, .975], 4, 2), [.2835820641, .9472550495])
    predictive = np.array([1/7, 8/21, 10/21])
    assert np.allclose(stats.betabinom.pmf([0, 1, 2], 2, 4, 2), predictive)
    assert math.isclose(predictive.sum(), 1)
    assert math.isclose(stats.betabinom.mean(2, 4, 2), 4/3)
    assert math.isclose(stats.betabinom.var(2, 4, 2), 32/63)
    assert math.isclose(stats.gamma.mean(8, scale=1/5), 1.6)
    assert math.isclose(stats.gamma.var(8, scale=1/5), .32)
    assert np.allclose(stats.gamma.ppf([.025, .975], 8, scale=1/5), [.69076644, 2.88453507])
    p_zero = integrate.quad(lambda rate: math.exp(-rate)*stats.gamma.pdf(rate, 8, scale=1/5), 0, np.inf)[0]
    assert math.isclose(p_zero, (5/6)**8, rel_tol=1e-10)
    # Exercise 1, posterior Beta(3,2); Exercise 2, Beta(7,3).
    assert math.isclose(stats.beta.mean(3, 2), .6)
    assert math.isclose(stats.beta.sf(.5, 3, 2), 11/16)
    assert math.isclose(stats.beta.mean(7, 3), .7)
    assert Fraction(7*8, 10*11) == Fraction(28, 55)
    assert math.isclose(stats.betabinom.pmf(2, 2, 7, 3), 28/55)
    # Exercise 3, prior Gamma(3,2), 5 events in 4 hours.
    assert math.isclose(stats.gamma.mean(8, scale=1/6), 4/3)
    assert math.isclose(stats.gamma.var(8, scale=1/6), 2/9)
    grid = np.linspace(0, 1, 1001)
    assert math.isclose(grid[np.argmax(stats.beta.pdf(grid, 4, 2))], .75)
    assert np.allclose(stats.beta.cdf(grid, 4, 2), 5*grid**4-4*grid**5)
    print("PASS: Bayes likelihood normalization, posterior moments, quantiles, predictions and exercises.")


def draw():
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    configure_matplotlib()
    output = Path(__file__).resolve().parents[1] / "docs/xac-suat-thong-ke/bai-giang/img/co-dien-bayes"
    output.mkdir(parents=True, exist_ok=True)
    blue, orange = PALETTE["primary"], PALETTE["copper"]
    def save(fig, filename):
        data = BytesIO()
        fig.savefig(data, format="svg", metadata={"Date": None})
        (output / filename).write_text(polish_svg(data.getvalue().decode("utf-8")), encoding="utf-8")
    def legend(ax):
        ax.legend(loc="lower center", bbox_to_anchor=(.5, 1.04), borderaxespad=0)

    x = np.linspace(0, 1, 501)
    fig, ax = plt.subplots(figsize=(6.6, 4.8), layout="constrained")
    ax.plot(x, stats.beta.pdf(x, 1, 1), "--", color=orange, label="Tiên nghiệm Beta(1, 1)")
    ax.plot(x, stats.beta.pdf(x, 4, 2), color=blue, linewidth=2.4, label="Hậu nghiệm Beta(4, 2)")
    lo, hi = stats.beta.ppf([.025, .975], 4, 2)
    ax.fill_between(x, stats.beta.pdf(x, 4, 2), where=(x >= lo) & (x <= hi), color=blue, alpha=.13)
    ax.set(xlabel="Xác suất thành công θ", ylabel="Mật độ", xlim=(0, 1), ylim=(0, 2.6))
    legend(ax)
    ax.grid(axis="y", alpha=.18)
    save(fig, "beta-tien-nghiem-hau-nghiem.svg")
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(6.6, 4.8), layout="constrained")
    k = np.arange(3)
    ax.bar(k-.18, [1/7, 8/21, 10/21], width=.34, color=blue, label="Tích phân hậu nghiệm")
    ax.bar(k+.18, stats.binom.pmf(k, 2, 2/3), width=.34, color=orange, label="Thay θ bằng 2/3")
    ax.set(xlabel="Số thành công trong hai lần tiếp theo", ylabel="Xác suất", xticks=k, ylim=(0, .65))
    legend(ax)
    ax.grid(axis="y", alpha=.18)
    ax.set_axisbelow(True)
    save(fig, "du-doan-tich-phan-va-thay-so.svg")
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(6.6, 4.8), layout="constrained")
    rate = np.linspace(0, 4.5, 501)
    ax.plot(rate, stats.gamma.pdf(rate, 2, scale=1/2), "--", color=orange, label="Tiên nghiệm Gamma(2, 2)")
    ax.plot(rate, stats.gamma.pdf(rate, 8, scale=1/5), color=blue, linewidth=2.4, label="Hậu nghiệm Gamma(8, 5)")
    ax.set(xlabel="Cường độ λ (sự kiện/giờ)", ylabel="Mật độ", xlim=(0, 4.5), ylim=(0, .95))
    legend(ax)
    ax.grid(axis="y", alpha=.18)
    save(fig, "gamma-poisson-cap-nhat.svg")
    plt.close(fig)
    print(f"Generated 3 SVG figures in {output}")


if __name__ == "__main__":
    verify()
    if "--check" not in sys.argv:
        draw()
