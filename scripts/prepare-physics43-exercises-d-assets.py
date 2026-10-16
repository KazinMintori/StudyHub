"""Trích xuất hình ảnh và tạo đồ thị SVG cho bài tập Chapter 43 nhóm D."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'docs/vat-ly-2/bai-giang/img/young-43'
OUT.mkdir(parents=True, exist_ok=True)

def save_svg(fig, name):
    svg_path = OUT / f'{name}.svg'
    fig.savefig(svg_path, bbox_inches='tight', pad_inches=0.2, facecolor='white', metadata={'Date': None})
    svg_path.write_text('\n'.join(line.rstrip() for line in svg_path.read_text(encoding='utf-8').splitlines()) + '\n', encoding='utf-8')
    plt.close(fig)

def prepare_solution_plots():
    """Tạo 8 đồ thị SVG bổ trợ giải thích lời giải từ dữ liệu và phương trình vật lý thực tế."""
    plt.rcParams.update({
        'font.family': 'DejaVu Sans',
        'font.size': 14,
        'axes.labelsize': 14,
        'axes.titlesize': 14,
        'xtick.labelsize': 14,
        'ytick.labelsize': 14,
        'legend.fontsize': 14,
        'svg.fonttype': 'none',
        'svg.hashsalt': 'StudyHub-physics43-d'
    })

    # 1. loi-giai-d-01: Hoạt độ và liều hấp thụ tích lũy của Sr-90 (Bài 43.35)
    fig, ax = plt.subplots(figsize=(8.0, 5.0))
    t_yr = np.linspace(0, 60, 200)
    T_half = 29.0
    N0 = (1.0e-6 / 90.0) * 6.02214e23
    lam_yr = np.log(2) / T_half
    decayed = N0 * (1 - np.exp(-lam_yr * t_yr))
    dose_rad = (decayed * 1.1 * 1.60218e-13 / 50.0) * 100
    ax.plot(t_yr, dose_rad, color='#2563eb', lw=2.2, label=r'Liều tích lũy $D(t)$ (rad)')
    ax.scatter([1.0], [55.8], color='#dc2626', s=60, zorder=4, label=r'Sau 1 năm: $D \approx 55{,}8\,\mathrm{rad}$')
    ax.axhline(N0 * 1.1 * 1.60218e-13 / 50.0 * 100, color='#64748b', ls='--', lw=1.2, label=r'Giới hạn cực đại ($t \to \infty$)')
    ax.set_xlabel('Thời gian $t$ (năm)', fontsize=14)
    ax.set_ylabel('Liều hấp thụ tích lũy (rad)', fontsize=14)
    ax.set_title(r'Liều hấp thụ tích lũy từ $1{,}0\,\mu\mathrm{g}\,\,^{90}\mathrm{Sr}$ trong mô $50\,\mathrm{kg}$', fontsize=14)
    ax.grid(alpha=0.25)
    ax.legend(fontsize=14, loc='lower right')
    fig.tight_layout(pad=1.5)
    save_svg(fig, 'loi-giai-d-01')

    # 2. loi-giai-d-02: Mật độ thông lượng neutrino Mặt Trời theo khoảng cách (Bài 43.51)
    fig, ax = plt.subplots(figsize=(8.0, 5.0))
    d_au = np.linspace(0.4, 2.5, 200) # AU
    N_nu_total = 1.774e38 # s^-1
    flux_cm2 = N_nu_total / (4 * np.pi * (d_au * 1.50e13)**2)
    ax.plot(d_au, flux_cm2 / 1e10, color='#059669', lw=2.2, label=r'Thông lượng neutrino $\Phi(d)$')
    ax.scatter([1.0], [6.28], color='#dc2626', s=70, zorder=4, label=r'Tại Trái Đất ($1\,\mathrm{AU}$): $\Phi \approx 6{,}3 \times 10^{10}\,\mathrm{cm^{-2}\cdot s^{-1}}$')
    ax.set_xlabel('Khoảng cách tới Mặt Trời (AU)', fontsize=14)
    ax.set_ylabel(r'Thông lượng neutrino ($10^{10}\,\mathrm{cm^{-2}\cdot s^{-1}}$)', fontsize=14)
    ax.set_title('Phân bố thông lượng neutrino Mặt Trời theo khoảng cách', fontsize=14)
    ax.grid(alpha=0.25)
    ax.legend(fontsize=14, loc='upper right')
    fig.tight_layout(pad=1.5)
    save_svg(fig, 'loi-giai-d-02')

    # 3. loi-giai-d-03: Đồ thị tuyến tính v^2 theo 1/lambda cho tán xạ quang hạt nhân đơteri (Bài 43.68)
    fig, ax = plt.subplots(figsize=(8.0, 5.0))
    lam_data = np.array([3.50, 3.75, 4.00, 4.25, 4.50, 4.75, 5.00]) * 1e-13
    v_data = np.array([11.3, 10.2, 9.1, 8.1, 7.2, 6.1, 4.9]) * 1e6
    x_data = 1.0 / lam_data / 1e12 # đơn vị 10^12 m^-1
    y_data = (v_data / 1e6)**2 # đơn vị 10^12 m^2/s^2
    slope, intercept = np.polyfit(x_data, y_data, 1)
    x_grid = np.linspace(1.8, 3.0, 100)
    ax.scatter(x_data, y_data, color='#dc2626', s=60, zorder=4, label='Số liệu đo thực nghiệm')
    ax.plot(x_grid, slope * x_grid + intercept, color='#2563eb', lw=2,
            label=rf'Khớp thẳng: $v^2 = {slope:.2f}\lambda^{{-1}} {intercept:.1f}$')
    ax.set_xlabel(r'$1/\lambda$ ($10^{12}\,\mathrm{m^{-1}}$)', fontsize=14, labelpad=8)
    ax.set_ylabel(r'$v^2$ ($10^{12}\,\mathrm{m^2/s^2}$)', fontsize=14, labelpad=12)
    ax.set_title(r'Đồ thị $v^2$ theo $1/\lambda$ khi quang phân rã deuteron', fontsize=14)
    ax.grid(alpha=0.25)
    ax.legend(fontsize=14, loc='upper left')
    fig.subplots_adjust(left=0.18, bottom=0.15, right=0.95, top=0.92)
    save_svg(fig, 'loi-giai-d-03')

    # 4. loi-giai-d-04: Đồ thị bán logarit suy giảm hoạt độ mẫu y tế (Bài 43.69)
    fig, ax = plt.subplots(figsize=(8.0, 5.0))
    t_data = np.array([0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 4.0, 5.0, 6.0, 7.0])
    A_data = np.array([20000, 14800, 11000, 8130, 6020, 4460, 3300, 1810, 1000, 550, 300])
    lnA = np.log(A_data)
    slope_4, intercept_4 = np.polyfit(t_data, lnA, 1)
    t_grid = np.linspace(0, 7.5, 100)
    ax.scatter(t_data, lnA, color='#dc2626', s=55, zorder=4, label='Số liệu đo thực nghiệm')
    ax.plot(t_grid, slope_4 * t_grid + intercept_4, color='#2563eb', lw=2,
            label=rf'Khớp tuyến tính: $\ln A = {slope_4:.3f}t + {intercept_4:.2f}$')
    ax.set_xlabel('Thời gian $t$ (giờ)', fontsize=14)
    ax.set_ylabel(r'$\ln[A(t)\,\,(\mathrm{Bq})]$', fontsize=14)
    ax.set_title(r'Đồ thị bán logarit xác định chu kỳ bán rã đồng vị y tế ($T_{1/2} \approx 1{,}16\,\mathrm{h}$)', fontsize=14)
    ax.grid(alpha=0.25)
    ax.legend(fontsize=14, loc='upper right')
    fig.tight_layout(pad=1.5)
    save_svg(fig, 'loi-giai-d-04')

    # 5. loi-giai-d-05: Phân tích phân rã hai thành phần trong mẫu hỗn hợp (Bài 43.70)
    fig, ax = plt.subplots(figsize=(8.0, 5.0))
    t_mix = np.array([0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 12.0])
    A_mix = np.array([7500, 4120, 2570, 1790, 1350, 1070, 872, 596, 404, 288, 201, 140, 98, 68, 33])
    t_fine = np.linspace(0, 12.5, 200)
    A1_fine = 5000.0 * np.exp(-1.80 * t_fine)
    A2_fine = 2500.0 * np.exp(-0.361 * t_fine)
    Atot_fine = A1_fine + A2_fine
    ax.semilogy(t_fine, Atot_fine, color='#2563eb', lw=2.2, label=r'Tổng hoạt độ $A_1(t) + A_2(t)$')
    ax.semilogy(t_fine, A1_fine, '--', color='#d97706', lw=1.8, label=r'Nhanh ($T_{1/2} \approx 23\,\mathrm{min}$)')
    ax.semilogy(t_fine, A2_fine, ':', color='#059669', lw=2, label=r'Chậm ($T_{1/2} \approx 1{,}92\,\mathrm{h}$)')
    ax.scatter(t_mix, A_mix, color='#dc2626', s=50, zorder=5, label='Số liệu đo (15 điểm)')
    ax.set_xlabel('Thời gian $t$ (giờ)', fontsize=14)
    ax.set_ylabel('Hoạt độ $A$ (Bq, thang logarit)', fontsize=14)
    ax.set_title('Phân rã hỗn hợp hai thành phần: Đoạn đuôi và thành phần nhanh', fontsize=14)
    ax.grid(alpha=0.25, which='both')
    ax.legend(fontsize=14, loc='upper right')
    fig.tight_layout(pad=1.5)
    save_svg(fig, 'loi-giai-d-05')

    # 6. loi-giai-d-06: Hoạt độ xéc-măng và hoạt độ dầu bôi trơn theo thời gian thử nghiệm (Bài 43.71)
    fig, ax = plt.subplots(figsize=(8.0, 5.0))
    t_h = np.linspace(0, 1200, 200)
    T_half_h = 45.0 * 24.0 # 1080 h
    lam_fe = np.log(2) / T_half_h
    # Initial activity: 9.4 microCi = 9.4e-6 * 3.7e10 Bq = 347800 Bq
    A0_Bq = 9.4e-6 * 3.7e10
    w_gh = 4.58861e-5 # g/h
    # A_oil = (A0 / m_total) * w * t * exp(-lam*t)
    A_oil_Bq = (A0_Bq / 100.0) * w_gh * t_h * np.exp(-lam_fe * t_h)
    ax.plot(t_h, A_oil_Bq, color='#dc2626', lw=2.2, label=r'Hoạt độ dầu động cơ $A_{\mathrm{oil}}(t)$ (Bq)')
    ax.scatter([1000], [84], color='#2563eb', s=65, zorder=5, label=r'Tại $t = 1000\,\mathrm{h}$: $A_{\mathrm{oil}} = 84\,\mathrm{Bq}$')
    ax.axvline(1000, color='#64748b', ls=':', lw=1.2)
    ax.set_xlabel('Thời gian vận hành thử nghiệm $t$ (giờ)', fontsize=14)
    ax.set_ylabel('Hoạt độ tích tụ trong dầu (Bq)', fontsize=14)
    ax.set_title(r'Động học hoạt độ phóng xạ $^{59}\mathrm{Fe}$ trong dầu bôi trơn động cơ', fontsize=14)
    ax.grid(alpha=0.25)
    ax.legend(fontsize=14, loc='upper left')
    fig.tight_layout(pad=1.5)
    save_svg(fig, 'loi-giai-d-06')

    # 7. loi-giai-d-07: Chuỗi phân rã phóng xạ Bateman U-234 -> Th-230 -> Ra-226 (Bài 43.72)
    fig, ax = plt.subplots(figsize=(8.0, 5.0))
    t_kyr = np.linspace(0, 1000, 300) # nghìn năm
    T1_k = 246.0 # kyr
    T2_k = 75.4 # kyr
    l1 = np.log(2) / T1_k
    l2 = np.log(2) / T2_k
    N1 = np.exp(-l1 * t_kyr)
    N2 = (l1 / (l2 - l1)) * (np.exp(-l1 * t_kyr) - np.exp(-l2 * t_kyr))
    N3 = 1.0 - N1 - N2
    ax.plot(t_kyr, N1, color='#2563eb', lw=2.0, label=r'$N_1(t)/N_{10}$ ($^{234}\mathrm{U}$, $T_{1/2} = 246\,\mathrm{kyr}$)')
    ax.plot(t_kyr, N2, color='#d97706', lw=2.2, label=r'$N_2(t)/N_{10}$ ($^{230}\mathrm{Th}$, $T_{1/2} = 75{,}4\,\mathrm{kyr}$)')
    ax.plot(t_kyr, N3, color='#059669', lw=2.0, label=r'Tổng số hạt đã rời hai đồng vị đầu, chia $N_{10}$')
    ax.scatter([246.0], [0.1749], color='#dc2626', s=60, zorder=5, label=r'Tại $t = T_1$: $N_2/N_{10} \approx 0{,}175$')
    ax.set_xlabel('Thời gian $t$ ($10^3$ năm)', fontsize=14)
    ax.set_ylabel(r'Tỉ lệ số hạt $N(t)/N_{10}$', fontsize=14)
    ax.set_title(r'Động học chuỗi phân rã Bateman ($^{234}\mathrm{U} \to {^{230}\mathrm{Th}} \to {^{226}\mathrm{Ra}}$)', fontsize=14)
    ax.grid(alpha=0.25)
    ax.legend(fontsize=14, loc='center right')
    fig.tight_layout(pad=1.5)
    save_svg(fig, 'loi-giai-d-07')

    # 8. loi-giai-d-08: Động học bão hòa tạo thành I-128 (Bài tập cầu nối)
    fig, ax = plt.subplots(figsize=(8.0, 5.0))
    t_min = np.linspace(0, 180, 200) # phút
    T_half_min = 25.0
    lam_min = np.log(2) / T_half_min
    sat_frac = 1.0 - np.exp(-lam_min * t_min)
    A_MBq = 1.50 * sat_frac
    ax.plot(t_min, A_MBq, color='#2563eb', lw=2.2, label=r'Hoạt độ $A(t) = R(1 - \mathrm{e}^{-\lambda t})$')
    ax.axhline(1.50, color='#dc2626', ls='--', lw=1.4, label=r'Mức bão hòa $A_{\max} = 1{,}50 \times 10^6\,\mathrm{Bq}$')
    for n in [1, 2, 3, 4, 5]:
        t_n = n * 25.0
        frac_n = 1.0 - 0.5**n
        ax.scatter([t_n], [1.50 * frac_n], color='#d97706', s=45, zorder=4)
    ax.scatter([125.0], [1.50 * (1 - 0.5**5)], color='#d97706', s=55, zorder=5, label=r'Sau $5 T_{1/2}$: đạt $96{,}9\%$ bão hòa')
    ax.set_xlabel('Thời gian chiếu xạ $t$ (phút)', fontsize=14)
    ax.set_ylabel(r'Hoạt độ mẫu ($10^6\,\mathrm{Bq}$)', fontsize=14)
    ax.set_title(r'Đường cong bão hòa hoạt độ $^{128}\mathrm{I}$ dưới chùm neutron liên tục', fontsize=14)
    ax.grid(alpha=0.25)
    ax.legend(fontsize=14, loc='lower right')
    fig.tight_layout(pad=1.5)
    save_svg(fig, 'loi-giai-d-08')

if __name__ == '__main__':
    prepare_solution_plots()
    print('Generated 8 SVG solution plots successfully!')
