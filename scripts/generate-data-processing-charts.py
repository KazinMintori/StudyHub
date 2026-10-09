"""Generate StudyHub's original, synthetic data-processing figures."""
from pathlib import Path
import re
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

ROOT = Path(__file__).resolve().parents[1]
FIGURES = ROOT / "docs/xu-ly-du-lieu/bai-giang/img"
PREVIEWS = ROOT / "qa/data-processing-figures"
plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 14,
    "axes.titlesize": 15, "axes.labelsize": 14,
    "xtick.labelsize": 14, "ytick.labelsize": 14,
    "figure.facecolor": "white", "axes.facecolor": "white",
    "text.color": "#30273c", "axes.labelcolor": "#30273c",
    "svg.fonttype": "path", "svg.hashsalt": "studyhub-data-processing",
})
PURPLE = "#6d4ab1"

def save(fig, lesson, name):
    folder = FIGURES / lesson
    folder.mkdir(parents=True, exist_ok=True)
    PREVIEWS.mkdir(parents=True, exist_ok=True)
    fig.tight_layout()
    target = folder / f"{name}.svg"
    fig.savefig(target, metadata={"Date": None, "Creator": "StudyHub"})
    svg = target.read_text(encoding="utf-8")
    svg = re.sub(r'<svg([^>]*?)width="[^"]+" height="[^"]+"', r'<svg\1width="100%"', svg, count=1)
    target.write_text(svg, encoding="utf-8")
    fig.savefig(PREVIEWS / f"{name}.png", dpi=150)
    plt.close(fig)
    print(target.relative_to(ROOT))

fig, ax = plt.subplots(figsize=(6.6, 4.2))
bars = ax.bar(["Sách", "Vở", "Bút"], [12, 8, 5], color=PURPLE, width=.6)
ax.bar_label(bars, padding=5)
ax.set(title="Số lượng bán theo nhóm", xlabel="Nhóm hàng", ylabel="Số sản phẩm", ylim=(0, 15))
save(fig, "lec-12", "ban-theo-nhom")

prices = np.array([10, 12, 14, 16, 20, 20, 24, 28, 30, 36])
freq, edges = np.histogram(prices, bins=[0, 10, 20, 30, 40])
assert freq.tolist() == [0, 4, 4, 2]
fig, ax = plt.subplots(figsize=(6.6, 4.2))
ax.hist(prices, bins=edges, color=PURPLE, edgecolor="white", linewidth=2)
ax.set(title="Phân phối giá", xlabel="Giá (nghìn đồng)", ylabel="Số mặt hàng", xticks=edges, yticks=[0, 1, 2, 3, 4, 5], ylim=(0, 5))
save(fig, "lec-12", "phan-phoi-gia")

fig, axes = plt.subplots(1, 2, figsize=(9.5, 4.5))
for ax in axes:
    bars = ax.bar(["A", "B"], [98, 100], color=PURPLE, width=.55)
    ax.bar_label(bars, padding=4)
    ax.set_ylabel("Số sản phẩm")
axes[0].set(ylim=(0, 112), title="Trục từ 0")
axes[1].set(ylim=(97, 101), yticks=[97, 98, 99, 100, 101], title="Trục từ 97")
fig.suptitle("Cùng dữ liệu: chênh lệch 2 sản phẩm", fontsize=16)
save(fig, "lec-13", "so-sanh-truc")

data = pd.DataFrame({"nhom": ["A"] * 5 + ["B"] * 5, "gia": [10, 12, 14, 16, 100, 20, 22, 24, 26, 28]})
fig, ax = plt.subplots(figsize=(6.6, 4.5))
sns.boxplot(data=data, x="nhom", y="gia", whis=1.5, ax=ax, color="#d9c8f0")
sns.stripplot(data=data, x="nhom", y="gia", ax=ax, color="#49366b", jitter=False, size=7)
ax.set(title="Giá và từng quan sát", xlabel="Nhóm (mỗi nhóm có 5 quan sát)", ylabel="Giá (nghìn đồng)")
save(fig, "lec-13", "boxplot")

fig, ax = plt.subplots(figsize=(7, 4.6))
for label, values, color, marker in [("Nhóm A", [8, 7], PURPLE, "o"), ("Nhóm B", [4, 3], "#007c78", "s"), ("Chung", [4.8, 6.2], "#9a4c11", "D")]:
    ax.plot(["Trước", "Sau"], values, label=label, marker=marker, color=color, linewidth=2.5)
    for i, value in enumerate(values):
        ax.annotate(f"{value:g}", (i, value), xytext=(8, 7), textcoords="offset points", color=color)
ax.set(title="Giá từng nhóm giảm, trung bình chung tăng", ylabel="Giá trung bình (nghìn đồng)", ylim=(2, 9), xlim=(-.18, 1.38))
ax.legend(loc="upper right", frameon=False, fontsize=12)
ax.text(.04, .03, "Tỷ trọng nhóm A: 20% → 80%", transform=ax.transAxes, fontsize=14)
save(fig, "lec-14", "co-cau-nhom")
