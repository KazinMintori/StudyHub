"""Tạo đồ thị hồi quy cho bài tập 39.82."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'docs/vat-ly-2/bai-giang/img/young-39'
OUT.mkdir(parents=True, exist_ok=True)

plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 13, 'svg.fonttype': 'none'})

# Dữ liệu thực nghiệm Bài 39.82
Vac = np.array([106.3, 69.1, 49.9, 25.2, 16.9, 13.6])
theta_deg = np.array([20.4, 24.8, 30.2, 45.5, 59.1, 73.1])

x = 1.0 / np.sqrt(Vac)
y = np.sin(np.radians(theta_deg))
slope, intercept = np.polyfit(x, y, 1)

xlim = (0, 0.30)
ylim = (0, 1.05)
xx = np.linspace(*xlim, 200)

fig, ax = plt.subplots(figsize=(7.4, 4.7))
ax.plot(xx, slope * xx + intercept, color='#5743a1', lw=2, label=f'Đường hồi quy (độ dốc ≈ {slope:.3f} V^{{1/2}})')
ax.scatter(x, y, color='#177b8c', s=50, zorder=3, label='Sáu điểm đo thực nghiệm')
ax.set(
    xlim=xlim,
    ylim=ylim,
    xlabel=r'$X = 1 / \sqrt{V_{\mathrm{ac}}}\ (\mathrm{V}^{-1/2})$',
    ylabel=r'$Y = \sin\theta$',
)
ax.spines[['top', 'right']].set_visible(False)
ax.grid(alpha=0.25, linestyle='--')
ax.legend(fontsize=11, loc='upper left')
fig.tight_layout()

p = OUT / 'loi-giai-39-82.svg'
fig.savefig(p, facecolor='white')
plt.close(fig)

# Format SVG lines
p.write_text('\n'.join(line.rstrip() for line in p.read_text(encoding='utf-8').splitlines()) + '\n', encoding='utf-8')
print(f'Generated {p.name} with slope = {slope:.4f} V^(1/2), intercept = {intercept:.4f}')
