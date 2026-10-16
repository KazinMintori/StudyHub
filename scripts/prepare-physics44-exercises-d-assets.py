"""Trích xuất hình ảnh gốc và đồ thị giải thích cho nhóm bài tập Chapter 44 nhóm D."""
from pathlib import Path
import hashlib
import pymupdf as fitz
from PIL import Image
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'docs/vat-ly-2/bai-giang/img/young-44'
SCALE = 3

# Tọa độ cắt ảnh gốc trên PDF Young & Freedman 15th Edition
# (Trang PDF 1-based: trang 1544 và trang 1530)
CROPS = {
    'hinh-p44-55': (1544, (172, 274, 296, 388)),
    'hinh-tham-chieu-d-1': (1530, (36, 362, 192, 504)),
}

def save_svg(fig, name):
    svg_path = OUT / f'{name}.svg'
    fig.savefig(svg_path, bbox_inches='tight', pad_inches=0.3, facecolor='white', metadata={'Date': None})
    svg_path.write_text('\n'.join(line.rstrip() for line in svg_path.read_text(encoding='utf-8').splitlines()) + '\n', encoding='utf-8')
    plt.close(fig)

def prepare_solution_plots():
    """Tạo 8 đồ thị bổ trợ giải thích lời giải từ dữ liệu và mô hình vật lý chính xác."""
    plt.rcParams.update({
        'font.family': 'DejaVu Sans',
        'font.size': 14,
        'axes.labelsize': 14,
        'axes.titlesize': 14,
        'xtick.labelsize': 14,
        'ytick.labelsize': 14,
        'legend.fontsize': 14,
        'svg.fonttype': 'none',
        'svg.hashsalt': 'StudyHub-physics44-d'
    })

    # 1. loi-giai-d-01: Sơ đồ decuplet baryon spin 3/2 gồm 2 đồ thị (a) và (b) (Bài 44.53)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15.5, 6.2))
    particles = [
        # S = 0
        (-1, 0, r'$\Delta^-$', 'ddd', 1232),
        (0, 0, r'$\Delta^0$', 'udd', 1232),
        (1, 0, r'$\Delta^+$', 'uud', 1232),
        (2, 0, r'$\Delta^{++}$', 'uuu', 1232),
        # S = -1
        (-1, -1, r'$\Sigma^{*-}$', 'dds', 1385),
        (0, -1, r'$\Sigma^{*0}$', 'uds', 1385),
        (1, -1, r'$\Sigma^{*+}$', 'uus', 1385),
        # S = -2
        (-1, -2, r'$\Xi^{*-}$', 'dss', 1530),
        (0, -2, r'$\Xi^{*0}$', 'uss', 1530),
        # S = -3
        (-1, -3, r'$\Omega^-$', 'sss', 1672)
    ]

    for ax, mode, panel_title in [
        (ax1, 'mass', r'(a) Đồ thị $S$ theo $Q$ và khối lượng thực nghiệm'),
        (ax2, 'quark', r'(b) Đồ thị $S$ theo $Q$ và cấu tạo ba quark ($u, d, s$)')
    ]:
        for q, s, name, qk, m in particles:
            color = '#dc2626' if name == r'$\Omega^-$' else '#2563eb'
            ax.scatter([q], [s], color=color, s=140, zorder=4)
            ax.text(q, s + 0.16, name, ha='center', va='bottom', fontsize=14, fontweight='bold', color=color)
            if mode == 'mass':
                sub_txt = f'{m} MeV'
            else:
                sub_txt = f'({qk})'
            ax.text(q, s - 0.18, sub_txt, ha='center', va='top', fontsize=14, color='#334155')

        # Đường lưới nối tam giác decuplet
        ax.plot([-1, 2], [0, 0], color='#94a3b8', lw=1.2, ls='--')
        ax.plot([-1, 1], [-1, -1], color='#94a3b8', lw=1.2, ls='--')
        ax.plot([-1, 0], [-2, -2], color='#94a3b8', lw=1.2, ls='--')
        ax.plot([-1, -1], [0, -3], color='#94a3b8', lw=1.2, ls=':')
        ax.plot([2, -1], [0, -3], color='#94a3b8', lw=1.2, ls=':')

        ax.set_xlabel(r'Điện tích $Q$ ($e$)', fontsize=14)
        ax.set_ylabel(r'Độ lạ $S$', fontsize=14)
        ax.set_title(panel_title, fontsize=14, pad=12)
        ax.set_xticks([-1, 0, 1, 2])
        ax.set_yticks([-3, -2, -1, 0])
        ax.set_xlim(-1.6, 2.6)
        ax.set_ylim(-3.7, 0.7)
        ax.grid(alpha=0.25)

    fig.tight_layout()
    save_svg(fig, 'loi-giai-d-01')

    # 2. loi-giai-d-02: Đồ thị tuyến tính cyclotron K_max vs B^2 (Bài 44.51)
    fig, ax = plt.subplots(figsize=(8.5, 5.2))
    B_arr = np.array([0.10, 0.20, 0.30, 0.40])
    B2_arr = B_arr**2
    K_arr = np.array([0.068, 0.270, 0.608, 1.080])
    slope_fit, intercept_fit = np.polyfit(B2_arr, K_arr, 1)
    B2_grid = np.linspace(0, 0.18, 100)
    ax.scatter(B2_arr, K_arr, color='#dc2626', s=80, zorder=4, label='Số liệu đo thực nghiệm')
    ax.plot(B2_grid, slope_fit * B2_grid + intercept_fit, color='#2563eb', lw=2.2,
            label=rf'Khớp tuyến tính: $K_{{\max}} = {slope_fit:.2f} B^2\,\mathrm{{MeV}}$')
    # Điểm dự đoán tại B = 0.25 T (B^2 = 0.0625 T^2)
    K_pred = slope_fit * 0.0625 + intercept_fit
    ax.scatter([0.0625], [K_pred], color='#059669', s=90, marker='s', zorder=5,
               label=rf'Tại $B = 0,25\,\mathrm{{T}}$: $K_{{\max}} \approx {K_pred:.3f}\,\mathrm{{MeV}}$')
    ax.set_xlabel(r'$B^2$ ($\mathrm{T}^2$)', fontsize=14)
    ax.set_ylabel(r'Động năng cực đại $K_{\max}$ (MeV)', fontsize=14)
    ax.set_title(r'Đồ thị $K_{\max}$ theo $B^2$ và xác định bán kính cyclotron $R \approx 0{,}375\,\mathrm{m}$', fontsize=14, pad=10)
    ax.grid(alpha=0.25)
    ax.legend(fontsize=14, loc='upper left')
    fig.tight_layout()
    save_svg(fig, 'loi-giai-d-02')

    # 3. loi-giai-d-03: Bán kính vũ trụ R(t) và khoảng cách Nibiru - Xibalba (Bài 44.55)
    fig, ax = plt.subplots(figsize=(8.5, 5.2))
    t_years = np.linspace(0, 6, 200)
    R_t = 0.500 + (1.00e-3 * 3.15576e7 / 1e3) * t_years # km
    D_t = R_t * (np.pi / 3.0) # km
    ax.plot(t_years, R_t, color='#2563eb', lw=2.2, label=r'Bán kính vũ trụ $R(t)$')
    ax.plot(t_years, D_t, color='#d97706', lw=2.2, label=r'Khoảng cách mặt cầu $D(t) = R(t)\theta$')
    # Điểm tại t = 4 năm
    R_4 = 0.500 + (1.00e-3 * 3.15576e7 / 1e3) * 4.0
    D_4 = R_4 * (np.pi / 3.0)
    ax.scatter([4], [D_4], color='#dc2626', s=80, zorder=4,
               label=rf'Tại $t = 4$ năm: $D \approx {D_4:.1f}\,\mathrm{{km}}$')
    ax.set_xlabel('Thời gian từ lúc tạo lập (năm)', fontsize=14)
    ax.set_ylabel('Khoảng cách (km)', fontsize=14)
    ax.set_title(r'Sự dãn nở của vũ trụ bong bóng 2D và khoảng cách Nibiru – Xibalba', fontsize=14, pad=10)
    ax.grid(alpha=0.25)
    ax.legend(fontsize=14, loc='upper left')
    fig.tight_layout()
    save_svg(fig, 'loi-giai-d-03')

    # 4. loi-giai-d-04: Actual relativistic two-body decay in problem44.48.
    fig, ax = plt.subplots(figsize=(8.5, 5.2))
    parent, daughter, pion = 1322.0, 1116.0, 139.6
    kinetic_daughter = (parent**2 + daughter**2 - pion**2)/(2*parent) - daughter
    total = parent - daughter - pion
    energies = [kinetic_daughter, total-kinetic_daughter]
    ax.bar([r'Lambda $\Lambda^0$', r'Pion $\pi^-$'], energies, color=['#2563eb','#dc2626'])
    for i, energy in enumerate(energies):
        ax.text(i,energy+2,f'{energy:.2f} MeV ({100*energy/total:.2f}%)',ha='center',fontsize=14)
    ax.set_ylim(0,75)
    ax.set_xlabel('Sản phẩm phân rã',fontsize=14)
    ax.set_ylabel('Động năng (MeV)', fontsize=14)
    ax.set_title(r'Phân chia động năng tương đối tính: $\Xi^-\to\Lambda^0+\pi^-$',fontsize=14,pad=10)
    ax.grid(alpha=0.25)
    fig.tight_layout()
    save_svg(fig, 'loi-giai-d-04')

    # 5. loi-giai-d-05: Giản đồ bảo toàn động lượng phân rã Sigma- -> pi- + n (Bài 44.49)
    fig, ax = plt.subplots(figsize=(8.5, 5.2))
    ax.annotate('', xy=(6.807, 0), xytext=(0, 0),
                arrowprops=dict(arrowstyle='->', color='#2563eb', lw=2.5))
    ax.text(3.4, 0.4, r'$\vec{p}_{\Sigma}$ ($680{,}7\,\mathrm{MeV}/c$)', color='#2563eb', ha='center', fontsize=14, fontweight='bold')
    ax.annotate('', xy=(0, 1.525), xytext=(0, 0),
                arrowprops=dict(arrowstyle='->', color='#dc2626', lw=2.5))
    ax.text(-0.3, 0.8, r'$\vec{p}_{\pi}$ ($152{,}5\,\mathrm{MeV}/c$)', color='#dc2626', ha='right', fontsize=14, fontweight='bold')
    ax.annotate('', xy=(6.807, -1.525), xytext=(0, 0),
                arrowprops=dict(arrowstyle='->', color='#059669', lw=2.5))
    ax.text(3.8, -1.2, r'$\vec{p}_n = \vec{p}_{\Sigma} - \vec{p}_{\pi}$ ($\theta \approx -12{,}6^\circ$)',
            color='#059669', ha='center', fontsize=14, fontweight='bold')
    ax.plot([6.807, 6.807], [0, -1.525], color='#94a3b8', ls=':', lw=1.2)
    ax.plot([0, 6.807], [-1.525, -1.525], color='#94a3b8', ls=':', lw=1.2)
    ax.set_xlabel(r'$p_x$ ($100\,\mathrm{MeV}/c$)', fontsize=14)
    ax.set_ylabel(r'$p_y$ ($100\,\mathrm{MeV}/c$)', fontsize=14)
    ax.set_title(r'Giản đồ vector động lượng phân rã $\Sigma^- \to \pi^- + n$ trong mặt phẳng $xy$', fontsize=14, pad=10)
    ax.set_xlim(-1.5, 8.0)
    ax.set_ylim(-2.2, 2.2)
    ax.grid(alpha=0.25)
    fig.tight_layout()
    save_svg(fig, 'loi-giai-d-05')

    # 6. loi-giai-d-06: Góc bay theta theo động năng pion trong K0 -> pi+ + pi- (Bài 44.50)
    fig, ax = plt.subplots(figsize=(8.5, 5.2))
    K_vals = np.linspace(150, 400, 200) # MeV
    E_K_vals = K_vals + 497.7
    p_K_vals = np.sqrt(E_K_vals**2 - 497.7**2)
    E_pi_vals = E_K_vals / 2.0
    p_pi_vals = np.sqrt(E_pi_vals**2 - 139.6**2)
    cos_theta = p_K_vals / (2.0 * p_pi_vals)
    valid = np.abs(cos_theta) <= 1.0
    theta_deg = np.arccos(cos_theta[valid]) * 180.0 / np.pi
    ax.plot(K_vals[valid], theta_deg, color='#2563eb', lw=2.2, label=r'Góc mở $\theta(K_K)$')
    # Điểm tại K = 225 MeV
    ax.scatter([225], [38.17], color='#dc2626', s=90, zorder=5,
               label=r'Tại $K_K = 225\,\mathrm{MeV}$: $\theta \approx 38{,}2^\circ$')
    ax.set_xlabel(r'Động năng của $K^0$ (MeV)', fontsize=14)
    ax.set_ylabel(r'Góc lệch $\theta$ so với trục $+x$ (độ)', fontsize=14)
    ax.set_title(r'Góc phát xạ đối xứng $\theta$ của pion theo động năng meson $K^0$', fontsize=14, pad=10)
    ax.grid(alpha=0.25)
    ax.legend(fontsize=14, loc='upper right')
    fig.tight_layout()
    save_svg(fig, 'loi-giai-d-06')

    # 7. loi-giai-d-07: Định luật suy giảm bức xạ PET qua mô sinh học (Bài 44.59)
    fig, ax = plt.subplots(figsize=(8.5, 5.2))
    x_cm = np.linspace(0, 35, 200)
    transmission = np.exp(-0.10 * x_cm) * 100.0 # phần trăm
    ax.plot(x_cm, transmission, color='#2563eb', lw=2.2, label=r'Tỉ lệ truyền qua: $N/N_0 = \mathrm{e}^{-0{,}1x}$')
    # Điểm tại x = 20 cm
    ax.scatter([20], [np.exp(-2.0) * 100.0], color='#dc2626', s=90, zorder=5,
               label=r'Tại $x = 20\,\mathrm{cm}$: $N/N_0 \approx 13{,}5\%$ (làm tròn $14\%$)')
    ax.axvline(20, color='#64748b', ls=':', lw=1.2)
    ax.axhline(np.exp(-2.0) * 100.0, color='#64748b', ls=':', lw=1.2)
    ax.set_xlabel('Bề dày mô sinh học $x$ (cm)', fontsize=14)
    ax.set_ylabel('Tỉ lệ photon còn lại (%)', fontsize=14)
    ax.set_title(r'Sự suy giảm chùm photon hủy cặp electron–positron trong chụp ảnh PET', fontsize=14, pad=10)
    ax.grid(alpha=0.25)
    ax.legend(fontsize=14, loc='upper right')
    fig.tight_layout()
    save_svg(fig, 'loi-giai-d-07')

    # 8. loi-giai-d-08: Năng lượng photon dịch chuyển đỏ theo hệ số dãn nở vũ trụ (Bài tập cầu nối)
    fig, ax = plt.subplots(figsize=(8.5, 5.2))
    scale_factor = np.linspace(0.05, 1.0, 200) # R(t) / R_0
    E_photon = 67.5 * scale_factor # MeV
    ax.plot(scale_factor, E_photon, color='#2563eb', lw=2.2,
            label=r'Năng lượng quan sát: $E_{\mathrm{obs}} = E_{\mathrm{emit}} \cdot \frac{R(t)}{R_0}$')
    ax.scatter([0.12], [67.5 * 0.12], color='#dc2626', s=90, zorder=5,
               label=r'Thiên hà Hình 44.20 ($R/R_0 = 12\%$): $E_{\mathrm{obs}} = 8{,}1\,\mathrm{MeV}$')
    ax.scatter([1.0], [67.5], color='#059669', s=90, zorder=5,
               label=r'Lúc phát xạ tại chỗ ($R/R_0 = 100\%$): $E_{\mathrm{emit}} = 67{,}5\,\mathrm{MeV}$')
    ax.set_xlabel(r'Hệ số dãn nở vũ trụ lúc phát xạ $R(t) / R_0$', fontsize=14)
    ax.set_ylabel(r'Năng lượng photon ghi nhận trên Trái Đất (MeV)', fontsize=14)
    ax.set_title(r'Dịch chuyển đỏ vũ trụ làm giảm năng lượng photon phân rã $\pi^0 \to 2\gamma$', fontsize=14, pad=10)
    ax.grid(alpha=0.25)
    ax.legend(fontsize=14, loc='upper left')
    fig.tight_layout()
    save_svg(fig, 'loi-giai-d-08')

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    rows = []
    with fitz.open(ROOT / 'raw_materials/physics/source/young-freedman-15.pdf') as pdf:
        for stem, (page, clip) in CROPS.items():
            pix = pdf[page - 1].get_pixmap(matrix=fitz.Matrix(SCALE, SCALE), clip=fitz.Rect(clip), alpha=False)
            p = OUT / (stem + '.png')
            pix.save(p)
            with Image.open(p) as im:
                assert im.size == (pix.width, pix.height) and im.convert('RGB').tobytes() == pix.samples
            sha = hashlib.sha256(p.read_bytes()).hexdigest()
            rows.append(dict(stem=stem, pdfPage=page, clip=clip, scale=SCALE, pixelMatch=True, sha256=sha, size=(pix.width, pix.height)))
    print(f'Extracted {len(rows)} figures successfully:')
    for r in rows:
        print(f"  - {r['stem']}: page {r['pdfPage']}, size {r['size']}, sha256={r['sha256'][:16]}...")

    prepare_solution_plots()
    print('Generated 8 solution plots (loi-giai-d-01.svg -> loi-giai-d-08.svg).')

if __name__ == '__main__':
    main()
