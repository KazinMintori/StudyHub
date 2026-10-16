"""Trích xuất hình ảnh và tạo các đồ thị giải pháp SVG cho nhóm bài tập Chapter 41 nhóm C."""
from pathlib import Path
import math
import numpy as np
import pymupdf as fitz
from PIL import Image
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
CROPS = {
    'hinh-tham-chieu-hop': (1381, (34, 545, 195, 672)),
}
SCALE = 3
OUT = ROOT / 'docs/vat-ly-2/bai-giang/img/young-41'


def crop_images():
    """Trích xuất ảnh gốc từ PDF với độ phân giải cao và lưu đúng vị trí."""
    doc = fitz.open(ROOT / 'raw_materials/physics/source/young-freedman-15.pdf')
    OUT.mkdir(parents=True, exist_ok=True)
    for name, (page_idx, rect_coords) in CROPS.items():
        page = doc[page_idx]
        rect = fitz.Rect(rect_coords)
        pix = page.get_pixmap(clip=rect, dpi=72 * SCALE)
        target = OUT / f"{name}.png"
        pix.save(target)
        print(f"Đã xuất ảnh: {target.relative_to(ROOT)} ({pix.width}x{pix.height})")


def generate_svgs():
    """Tạo 10 đồ thị giải pháp SVG khoa học, chính xác, font >= 14."""
    plt.rcParams.update({
        'font.family': 'DejaVu Sans',
        'font.size': 14,
        'svg.fonttype': 'none',
        'svg.hashsalt': 'StudyHub-physics41-c',
    })

    def save_plot(fig, name):
        svg_path = OUT / f"{name}.svg"
        fig.savefig(svg_path, bbox_inches='tight', facecolor='white', metadata={'Date': None})
        svg_text = svg_path.read_text(encoding='utf-8')
        clean_text = '\n'.join(line.rstrip() for line in svg_text.splitlines()) + '\n'
        svg_path.write_text(clean_text, encoding='utf-8')
        plt.close(fig)
        print(f"Đã tạo SVG: {svg_path.relative_to(ROOT)}")

    # 1. loi-giai-c-01.svg: Mật độ xác suất 1D |psi(x)|^2 cho nx=2 (VP41.1.1)
    fig, ax = plt.subplots(figsize=(7.5, 4.4))
    x = np.linspace(0, 1, 500)
    psi2 = 2.0 * np.sin(2.0 * np.pi * x)**2
    ax.plot(x, psi2, color='#2563eb', lw=2.4, label=r'$P(x) = \frac{2}{L}\sin^2(2\pi x/L)$')
    # Shade region 0 <= x <= 1/3
    mask = x <= (1.0 / 3.0)
    ax.fill_between(x[mask], psi2[mask], color='#3b82f6', alpha=0.25, label=r'Miền tích phân $0 \leq x \leq L/3$ ($P \approx 0{,}402$)')
    ax.axvline(0.5, color='#dc2626', ls='--', lw=1.8, label=r'Mặt phẳng nút $x = L/2$ ($P(x)=0$)')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 2.3)
    ax.set_xticks([0, 1/4, 1/3, 1/2, 2/3, 3/4, 1])
    ax.set_xticklabels(['$0$', '$L/4$', '$L/3$', '$L/2$', '$2L/3$', '$3L/4$', '$L$'], fontsize=14)
    ax.set_xlabel('Tọa độ x theo cạnh hộp L', fontsize=14)
    ax.set_ylabel(r'Mật độ xác suất $P(x) \cdot L$', fontsize=14)
    ax.set_title('Phân bố xác suất 1D trạng thái $n_x = 2$ và mặt phẳng nút', fontsize=15, pad=12)
    ax.legend(fontsize=14, loc='upper center', bbox_to_anchor=(0.5,-0.22))
    ax.grid(alpha=0.25)
    save_plot(fig, 'loi-giai-c-01')

    # 2. loi-giai-c-02.svg: Mô hình vector mômen động lượng quỹ đạo l=2 (VP41.4.2)
    fig, ax = plt.subplots(figsize=(7.2, 5.0))
    l = 2
    L_mag = math.sqrt(l * (l + 1))  # sqrt(6) ~ 2.449
    ax.axvline(0, color='#64748b', lw=1.2, ls=':')
    ax.axhline(0, color='#64748b', lw=1.2, ls=':')
    ax.annotate('', xy=(0, 3.0), xytext=(0, -3.0),
                arrowprops=dict(arrowstyle='->', color='#334155', lw=1.5))
    ax.text(0.12, 2.9, '+z (trục lượng tử hóa)', fontsize=14, color='#334155')
    ax.text(0.12, -2.9, '-z', fontsize=14, color='#334155')

    colors = ['#10b981', '#3b82f6', '#6366f1', '#f59e0b', '#dc2626']
    mls = [2, 1, 0, -1, -2]
    for ml, col in zip(mls, colors):
        cos_th = ml / L_mag
        sin_th = math.sqrt(max(0.0, 1.0 - cos_th**2))
        ax.annotate('', xy=(sin_th * L_mag, ml), xytext=(0, 0),
                    arrowprops=dict(arrowstyle='->', color=col, lw=2.2))
        ax.plot([0, sin_th * L_mag], [ml, ml], color=col, ls='--', lw=1.0)
        label_text = f'$m_l = {ml:+d}$' if ml != 0 else '$m_l = 0$'
        if ml == -2:
            label_text += r' ($\theta_{\min,-z} = 35{,}3^\circ$)'
        ax.text(sin_th * L_mag + 0.08, ml - 0.05, label_text, fontsize=14, color=col)

    ax.set_xlim(-0.5, 3.2)
    ax.set_ylim(-3.2, 3.2)
    ax.set_aspect('equal')
    ax.set_title(r'Định hướng lượng tử hóa của $\vec{L}$ với $l=2$ ($L = \sqrt{6}\,\hbar$)', fontsize=15, pad=12)
    ax.set_xlabel(r'Hình chiếu vuông góc $L_\perp / \hbar$', fontsize=14)
    ax.set_ylabel(r'Hình chiếu $L_z / \hbar$', fontsize=14)
    ax.grid(alpha=0.2)
    save_plot(fig, 'loi-giai-c-02')

    # 3. loi-giai-c-03.svg: Hàm xác suất xuyên tâm P(r) hydro 1s và các miền (VP41.4.4)
    fig, ax = plt.subplots(figsize=(7.8, 4.6))
    r_a = np.linspace(0, 6, 600)
    P_r = 4.0 * (r_a**2) * np.exp(-2.0 * r_a)
    ax.plot(r_a, P_r, color='#2563eb', lw=2.4, label=r'$P(r) = \frac{4r^2}{a^3}e^{-2r/a}$')

    # Shade 0 to 2a
    m1 = r_a <= 2.0
    ax.fill_between(r_a[m1], P_r[m1], color='#3b82f6', alpha=0.22, label=r'$0 \leq r \leq 2a$ ($P \approx 0{,}762$)')
    ax.axvline(1.0, color='#059669', ls=':', lw=1.8, label=r'Đỉnh cực đại tại $r = a$')
    ax.axvline(2.0, color='#64748b', ls='--', lw=1.2)
    ax.axvline(4.0, color='#dc2626', ls='--', lw=1.2, label=r'Mốc $r = 4a$ ($P(r \geq 4a) \approx 0{,}0138$)')

    ax.set_xlim(0, 6)
    ax.set_ylim(0, 0.6)
    ax.set_xlabel('Khoảng cách r theo bán kính Bohr a', fontsize=14)
    ax.set_ylabel(r'Phân bố xác suất xuyên tâm $P(r) \cdot a$', fontsize=14)
    ax.set_title('Phân bố xác suất xuyên tâm của electron trạng thái $1s$ hydro', fontsize=15, pad=12)
    ax.legend(fontsize=14, loc='upper center', bbox_to_anchor=(0.5,-0.22))
    ax.grid(alpha=0.25)
    save_plot(fig, 'loi-giai-c-03')


    # Qualitative level diagrams: exaggerate fine splitting, label it explicitly.
    for name, title, labels, delta, wavelengths in [
        ('loi-giai-c-04', 'Vạch đôi của kali: Chuyển mức 4p xuống 4s',
         [r'$4p_{3/2}$', r'$4p_{1/2}$', r'$4s_{1/2}$'],
         r'$\Delta E = 7{,}16\,\mathrm{meV}$',
         [r'$766{,}490\,\mathrm{nm}$', r'$769{,}896\,\mathrm{nm}$']),
        ('loi-giai-c-05', 'Cấu trúc tinh tế hydro: Chuyển từ n = 3 xuống n = 2',
         [r'$n=3,\ j=3/2$', r'$n=3,\ j=1/2$', r'$n=2,\ j=1/2$'],
         r'$\Delta E = 1{,}34\times10^{-5}\,\mathrm{eV}$',
         [r'Từ $j=3/2$', r'Từ $j=1/2$']),
    ]:
        fig, ax = plt.subplots(figsize=(9, 5))
        upper, lower, ground = 3.5, 2.9, .7
        for y, label, color in zip([upper,lower,ground], labels, ['#2563eb','#1d4ed8','#059669']):
            ax.hlines(y=y,xmin=1.7,xmax=5.2,color=color,lw=3)
            ax.text(5.35,y,label,va='center',fontsize=14,color=color)
        ax.annotate('',xy=(1.35,upper),xytext=(1.35,lower),
                    arrowprops=dict(arrowstyle='<->',color='#dc2626',lw=1.6))
        ax.text(3.55,4.0,delta,color='#dc2626',ha='center',fontsize=14)
        for x, top, color in [(2.5,upper,'#7c3aed'),(4.25,lower,'#d97706')]:
            ax.annotate('',xy=(x,ground+.05),xytext=(x,top-.05),
                        arrowprops=dict(arrowstyle='->',color=color,lw=2))
        ax.text(2.35,2.05,wavelengths[0],ha='right',fontsize=14,color='#7c3aed')
        ax.text(4.4,1.45,wavelengths[1],ha='left',fontsize=14,color='#d97706')
        if name.endswith('05'):
            ax.text(3.55,.2,r'$\Delta\lambda\approx4{,}66\times10^{-3}\,\mathrm{nm}$',ha='center',fontsize=14)
        else:
            ax.text(3.55,.2,r'$B_{\mathrm{eff}}\approx61{,}8\,\mathrm{T}$',ha='center',fontsize=14)
        ax.text(4.5,-.25,'Giản đồ định tính, độ tách mức được phóng đại',ha='center',fontsize=14,color='#475569')
        ax.set(xlim=(0,9),ylim=(-.4,4.4));ax.axis('off')
        ax.set_title(title,fontsize=16,pad=16)
        save_plot(fig,name)

    # 6. loi-giai-c-06.svg: Phân bố mật độ xác suất 2D trạng thái (2,2,1) (41.4)
    fig, ax = plt.subplots(figsize=(6.8, 5.8))
    x_grid = np.linspace(0, 1, 200)
    y_grid = np.linspace(0, 1, 200)
    X, Y = np.meshgrid(x_grid, y_grid)
    Z = (np.sin(2.0 * np.pi * X) * np.sin(2.0 * np.pi * Y))**2
    c = ax.contourf(X, Y, Z, levels=25, cmap='Blues')
    cbar = fig.colorbar(c, ax=ax, fraction=0.046, pad=0.04)
    cbar.ax.tick_params(labelsize=12)
    cbar.set_label(r'$|\psi(x,y,L/2)|^2$ (đơn vị tùy ý)', fontsize=14)

    # 4 maxima points
    max_pts = [(0.25, 0.25), (0.75, 0.25), (0.25, 0.75), (0.75, 0.75)]
    for px, py in max_pts:
        ax.plot(px, py, 'o', color='#dc2626', markersize=8)
        ax.text(px, py + 0.04, f'({px*4:.0f}L/4, {py*4:.0f}L/4)', color='#991b1b',
                fontsize=14, ha='center', weight='bold')

    ax.axvline(0.5, color='#475569', ls='--', lw=1.2)
    ax.axhline(0.5, color='#475569', ls='--', lw=1.2)
    ax.set_xticks([0, 0.25, 0.5, 0.75, 1.0])
    ax.set_yticks([0, 0.25, 0.5, 0.75, 1.0])
    ax.set_xticklabels(['$0$', '$L/4$', '$L/2$', '$3L/4$', '$L$'], fontsize=14)
    ax.set_yticklabels(['$0$', '$L/4$', '$L/2$', '$3L/4$', '$L$'], fontsize=14)
    ax.set_xlabel('Tọa độ x theo cạnh L', fontsize=14)
    ax.set_ylabel('Tọa độ y theo cạnh L', fontsize=14)
    ax.set_title('Bốn đỉnh cực đại xác suất của trạng thái $(n_x, n_y, n_z) = (2, 2, 1)$', fontsize=15, pad=12)
    save_plot(fig, 'loi-giai-c-06')

    # 7. loi-giai-c-07.svg: Góc lượng tử hóa cho l=2 đối với trục +z (41.10 / 41.12)
    fig, ax = plt.subplots(figsize=(7.5, 5.0))
    theta_degs = [35.3, 65.9, 90.0, 114.1, 144.7]
    mls_7 = [2, 1, 0, -1, -2]
    colors_7 = ['#2563eb', '#3b82f6', '#10b981', '#f59e0b', '#dc2626']

    ax.annotate('', xy=(0, 2.8), xytext=(0, -2.8),
                arrowprops=dict(arrowstyle='->', color='#1e293b', lw=1.8))
    ax.text(0.08, 2.7, '+z', fontsize=14, weight='bold', color='#1e293b')

    for ml, th, col in zip(mls_7, theta_degs, colors_7):
        rad = math.radians(th)
        vx = math.sin(rad) * 2.45
        vy = math.cos(rad) * 2.45
        ax.annotate('', xy=(vx, vy), xytext=(0, 0),
                    arrowprops=dict(arrowstyle='->', color=col, lw=2.2))
        ax.text(vx + 0.1, vy - 0.05, f'$m_l = {ml:+d}$ ($\\theta = {th}^\\circ$)' if ml != 0 else f'$m_l = 0$ ($\\theta = {th}^\\circ$)',
                fontsize=14, color=col)

    ax.set_xlim(-0.5, 3.4)
    ax.set_ylim(-3.0, 3.0)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title(r'Góc giữa vector $\vec{L}$ và trục $+z$ cho trạng thái $l=2$ ($L = \sqrt{6}\,\hbar$)', fontsize=15, pad=12)
    save_plot(fig, 'loi-giai-c-07')

    # 8. loi-giai-c-08.svg: Xác suất tìm thấy electron hydro 1s theo hai miền (41.18)
    fig, ax = plt.subplots(figsize=(7.5, 4.5))
    r_a = np.linspace(0, 4.5, 500)
    P_r = 4.0 * (r_a**2) * np.exp(-2.0 * r_a)
    ax.plot(r_a, P_r, color='#1e293b', lw=2.2)

    # Shade r < 0.5a
    m_half = r_a <= 0.5
    ax.fill_between(r_a[m_half], P_r[m_half], color='#f59e0b', alpha=0.35, label=r'$r < a/2$ ($P \approx 8{,}03\%$)')

    # Shade 0.5a <= r <= a
    m_between = (r_a >= 0.5) & (r_a <= 1.0)
    ax.fill_between(r_a[m_between], P_r[m_between], color='#2563eb', alpha=0.35, label=r'$a/2 \leq r \leq a$ ($P \approx 24{,}30\%$)')

    ax.axvline(0.5, color='#d97706', ls='--', lw=1.4)
    ax.axvline(1.0, color='#2563eb', ls='--', lw=1.4)
    ax.set_xlim(0, 4.5)
    ax.set_ylim(0, 0.6)
    ax.set_xticks([0, 0.5, 1.0, 1.5, 2.0, 3.0, 4.0])
    ax.set_xticklabels(['$0$', '$a/2$', '$a$', '$1{,}5a$', '$2a$', '$3a$', '$4a$'], fontsize=14)
    ax.set_xlabel('Khoảng cách r theo bán kính Bohr a', fontsize=14)
    ax.set_ylabel(r'Phân bố xác suất $P(r) \cdot a$', fontsize=14)
    ax.set_title(r'So sánh xác suất trong hai miền $r < a/2$ và $a/2 \leq r \leq a$', fontsize=15, pad=12)
    ax.legend(fontsize=14, loc='upper center', bbox_to_anchor=(0.5,-0.22))
    ax.grid(alpha=0.25)
    save_plot(fig, 'loi-giai-c-08')

    # 9. loi-giai-c-09.svg: So sánh đỉnh cực đại đơn của 3d và 4f (41.20)
    fig, ax = plt.subplots(figsize=(7.8, 4.6))
    r_nm = np.linspace(0, 1.6, 600)
    a_nm = 0.0529177
    r_over_a = r_nm / a_nm

    # n=3, l=2: peak at 9a = 0.476 nm
    P3d = (r_over_a**6) * np.exp(-2.0 * r_over_a / 3.0)
    P3d = P3d / np.max(P3d)
    ax.plot(r_nm, P3d, color='#2563eb', lw=2.4, label=r'Trạng thái $3d$: đỉnh tại $r = 9a \approx 0{,}476\,\mathrm{nm}$')
    ax.axvline(9.0 * a_nm, color='#2563eb', ls=':', lw=1.5)

    # n=4, l=3: peak at 16a = 0.847 nm
    P4f = (r_over_a**8) * np.exp(-2.0 * r_over_a / 4.0)
    P4f = P4f / np.max(P4f)
    ax.plot(r_nm, P4f, color='#dc2626', lw=2.4, label=r'Trạng thái $4f$: đỉnh tại $r = 16a \approx 0{,}847\,\mathrm{nm}$')
    ax.axvline(16.0 * a_nm, color='#dc2626', ls=':', lw=1.5)

    ax.set_xlim(0, 1.6)
    ax.set_ylim(0, 1.15)
    ax.set_xlabel('Khoảng cách r (nm)', fontsize=14)
    ax.set_ylabel('Phân bố xuyên tâm (chuẩn hóa đỉnh = 1)', fontsize=14)
    ax.set_title(r'Vị trí một đỉnh cực đại xuyên tâm của các trạng thái $l = n - 1$', fontsize=15, pad=12)
    ax.legend(fontsize=14, loc='upper center', bbox_to_anchor=(0.5,-0.22))
    ax.grid(alpha=0.25)
    save_plot(fig, 'loi-giai-c-09')

    # 10. loi-giai-c-10.svg: Tách mức Zeeman trạng thái d (l=2) (41.22c)
    fig, ax = plt.subplots(figsize=(7.5, 5.0))
    # B = 0 level
    ax.hlines(y=2.5, xmin=0.8, xmax=2.0, colors='#475569', lw=3.2)
    ax.text(1.4, 2.7, 'Không có từ trường (B = 0)\n' + r'Suy biến bậc 5 ($m_l = 0, \pm 1, \pm 2$)',
            fontsize=14, color='#475569', ha='center', va='bottom')

    # B > 0 levels: 5 equidistant levels
    y_levels = [3.7, 3.1, 2.5, 1.9, 1.3]
    mls_10 = [+2, +1, 0, -1, -2]
    cols_10 = ['#dc2626', '#f59e0b', '#10b981', '#3b82f6', '#2563eb']

    for y, ml, col in zip(y_levels, mls_10, cols_10):
        ax.hlines(y=y, xmin=3.2, xmax=4.4, colors=col, lw=2.8)
        label = f'$m_l = {ml:+d}$' if ml != 0 else '$m_l = 0$'
        if ml == -2:
            label += r' (mức thấp nhất)'
        ax.text(4.5, y, label, fontsize=14, color=col, va='center')
        ax.plot([2.0, 3.2], [2.5, y], color='#94a3b8', ls=':', lw=1.0)

    # delta E brace
    ax.annotate('', xy=(3.0, 3.7), xytext=(3.0, 3.1),
                arrowprops=dict(arrowstyle='<->', color='#b91c1c', lw=1.5))
    ax.text(2.9, 3.4, r'$\Delta E = \mu_B B$' + '\n' + r'$\approx 4{,}63 \times 10^{-5}\,\mathrm{eV}$',
            fontsize=14, color='#b91c1c', ha='right', va='center')

    ax.set_xlim(0.2, 6.2)
    ax.set_ylim(0.8, 4.3)
    ax.axis('off')
    ax.set_title(r'Sơ đồ tách mức năng lượng Zeeman cho trạng thái $d$ ($l = 2$) trong từ trường', fontsize=15, pad=14)
    save_plot(fig, 'loi-giai-c-10')


if __name__ == '__main__':
    crop_images()
    generate_svgs()
    print("Hoàn thành chuẩn bị toàn bộ tài nguyên hình ảnh nhóm C.")
