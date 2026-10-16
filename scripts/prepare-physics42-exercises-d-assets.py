"""Trích xuất hình ảnh gốc và đồ thị lời giải cho nhóm bài tập Chapter 42 nhóm D."""
from pathlib import Path
import hashlib
import pymupdf as fitz
from PIL import Image
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'docs/vat-ly-2/bai-giang/img/young-42'
SCALE = 3

# Tọa độ cắt ảnh gốc trên PDF Young & Freedman 15th Edition
# (Trang PDF 1-based = trang in + 20)
CROPS = {
    'hinh-p42-38': (1458, (80, 498, 250, 616)),
    'hinh-p42-49': (1459, (215, 333, 335, 396)),
    'hinh-p42-50': (1459, (395, 75, 565, 180)),
    'hinh-p42-52': (1460, (105, 75, 225, 180)),
    'hinh-doan-van-diot': (1460, (355, 385, 525, 495)),
}

def save_svg(fig, name):
    svg_path = OUT / f'{name}.svg'
    fig.savefig(svg_path, bbox_inches='tight', facecolor='white', metadata={'Date': None})
    svg_path.write_text('\n'.join(line.rstrip() for line in svg_path.read_text(encoding='utf-8').splitlines()) + '\n', encoding='utf-8')
    plt.close(fig)

def prepare_solution_plots():
    """Tạo 10 đồ thị bổ trợ giải thích lời giải từ dữ liệu và hàm vật lý giải tích thực tế."""
    plt.rcParams.update({
        'font.family': 'DejaVu Sans',
        'font.size': 14,
        'svg.fonttype': 'none',
        'svg.hashsalt': 'StudyHub-physics42'
    })

    # 1. loi-giai-d-01: Phân bố số lượng phân tử theo mức quay CO (Bài 42.35 & 42.36)
    fig, ax = plt.subplots(figsize=(7.5, 4.5))
    l_vals = np.arange(0, 31)
    beta = 0.0092587
    ratio = (2 * l_vals + 1) * np.exp(-beta * l_vals * (l_vals + 1))
    ax.plot(l_vals, ratio, color='#2563eb', lw=2.2, label=r'Phân bố Boltzmann $n_l / n_0$')
    ax.scatter([7], [ratio[7]], color='#dc2626', s=70, zorder=4, label=r'Cực đại tại $l = 7$ ($n_7/n_0 \approx 8{,}93$)')
    ax.set(xlabel=r'Số lượng tử quay $l$', ylabel=r'Tỉ số $n_l / n_0$',
           title=r'Phân bố trạng thái quay của CO ở $T = 300\,\mathrm{K}$')
    ax.grid(alpha=0.25)
    ax.legend(fontsize=12, loc='upper right')
    save_svg(fig, 'loi-giai-d-01')

    # 2. loi-giai-d-02: Tuyến tính hóa số liệu Fermi-Dirac (Bài 42.47)
    fig, ax = plt.subplots(figsize=(7.5, 4.5))
    E_data = np.array([3.0, 2.5, 2.0, 1.5, 1.0, 0.5])
    f_data = np.array([0.064, 0.173, 0.390, 0.661, 0.856, 0.950])
    x_data = np.log(1.0 / f_data - 1.0)
    slope, intercept = np.polyfit(x_data, E_data, 1)
    x_grid = np.linspace(-3.2, 3.0, 100)
    ax.scatter(x_data, E_data, color='#dc2626', s=60, zorder=3, label='Số liệu đo')
    ax.plot(x_grid, slope * x_grid + intercept, color='#2563eb', lw=2,
            label=rf'Khớp tuyến tính: $E = {slope:.3f}x + {intercept:.2f}\,\mathrm{{eV}}$')
    ax.axhline(intercept, color='#64748b', ls=':', lw=1.2, label=r'$E_F \approx 1{,}80\,\mathrm{eV}$')
    ax.set(xlabel=r'$\ln[1/f(E) - 1]$', ylabel=r'Năng lượng $E$ (eV)',
           title='Xác định mức Fermi và nhiệt độ của chất dẫn điện')
    ax.grid(alpha=0.25)
    ax.legend(fontsize=11, loc='upper left')
    save_svg(fig, 'loi-giai-d-02')

    # 3. loi-giai-d-03: Dạng sóng xén điện áp mạch chỉnh lưu nửa chu kỳ (Bài 42.49)
    fig, ax = plt.subplots(figsize=(7.5, 4.5))
    t = np.linspace(0, 2, 500)
    v_in = 5.0 * np.sin(2 * np.pi * t)
    v_max = 0.60
    v_out = np.where(v_in > v_max, v_max, np.where(v_in > 0, v_in, v_in))
    ax.plot(t, v_in, '--', color='#64748b', lw=1.8, label=r'Điện áp vào $V_{\mathrm{in}}(t) = 5\sin(\omega t)\,\mathrm{V}$')
    ax.plot(t, v_out, color='#2563eb', lw=2.4, label=r'Điện áp ra $V_{\mathrm{out}}(t)$ (bị xén tại $0{,}60\,\mathrm{V}$)')
    ax.axhline(v_max, color='#dc2626', ls=':', lw=1.2, label=r'Ngưỡng ghim $V_{\max} = 0{,}60\,\mathrm{V}$')
    ax.set(xlabel=r'Thời gian chuẩn hóa $t/T$', ylabel='Điện áp (V)',
           title=r'Đáp ứng của diode chỉnh lưu với tín hiệu vào biên độ $5\,\mathrm{V}$')
    ax.grid(alpha=0.25)
    ax.legend(fontsize=11, loc='lower right')
    save_svg(fig, 'loi-giai-d-03')

    # 4. loi-giai-d-04: Điện trường trong vùng nghèo p-n (Bài 42.50)
    fig, ax = plt.subplots(figsize=(7.5, 4.5))
    x_p = np.linspace(-275, 0, 200)
    x_n = np.linspace(0, 55, 200)
    E_p = -(4.253e6 / 275.0) * (x_p + 275) / 1e6
    E_n = -(4.253e6 / 55.0) * (55.0 - x_n) / 1e6
    ax.plot(x_p, E_p, color='#2563eb', lw=2.4, label=r'Phía p: $-a_p \leq x \leq 0$')
    ax.plot(x_n, E_n, color='#059669', lw=2.4, label=r'Phía n: $0 \leq x \leq a_n$')
    ax.axvline(0, color='#64748b', ls='--', lw=1)
    ax.scatter([0], [-4.253], color='#dc2626', s=60, zorder=4, label=r'$E_x(0) \approx -4{,}25 \times 10^6\,\mathrm{V/m}$')
    ax.set(xlabel=r'Tọa độ $x$ (nm)', ylabel=r'Điện trường $E_x$ ($10^6\,\mathrm{V/m}$)',
           title=r'Phân bố điện trường $E_x(x)$ trong vùng nghèo (hướng sang trái)')
    ax.grid(alpha=0.25)
    ax.legend(fontsize=11, loc='lower left')
    save_svg(fig, 'loi-giai-d-04')

    # 5. loi-giai-d-05: Điện thế tĩnh điện trong vùng nghèo p-n (Bài 42.50)
    fig, ax = plt.subplots(figsize=(7.5, 4.5))
    V_p = 0.5 * (4.253 / 275.0) * (x_p + 275)**2 / 275.0 * 275.0 * 1e-3  # check integration
    # V(x) = e*N_A/(2*eps) * (x + a_p)^2. At x=0, V(0) = 0.585 V
    V_p = 0.5848 * ((x_p + 275.0) / 275.0)**2
    # Phía n: V(x) = V(0) + e*N_D/eps * (a_n*x - x^2/2)
    # At x = a_n = 55 nm, V(a_n) = Vb = 0.702 V
    V_n = 0.5848 + (0.7018 - 0.5848) * (2.0 * (x_n / 55.0) - (x_n / 55.0)**2)
    ax.plot(x_p, V_p, color='#2563eb', lw=2.4, label=r'Phía p: Parabol lồi')
    ax.plot(x_n, V_n, color='#059669', lw=2.4, label=r'Phía n: Parabol lõm')
    ax.axhline(0.7018, color='#dc2626', ls=':', lw=1.2, label=r'Thế rào $V_b \approx 0{,}702\,\mathrm{V}$')
    ax.axvline(0, color='#64748b', ls='--', lw=1)
    ax.set(xlabel=r'Tọa độ $x$ (nm)', ylabel='Điện thế $V(x)$ (V)',
           title=r'Phân bố điện thế tĩnh điện $V(x)$ qua chuyển tiếp p-n')
    ax.grid(alpha=0.25)
    ax.legend(fontsize=11, loc='upper left')
    save_svg(fig, 'loi-giai-d-05')

    # 6. loi-giai-d-06: Mode dao động kéo dãn bất đối xứng CO2 (Bài 42.51)
    fig, ax = plt.subplots(figsize=(7.5, 4.5))
    tau = np.linspace(0, 2, 400)
    X_O = np.cos(2 * np.pi * tau)
    X_C = -(8.0 / 3.0) * X_O
    ax.plot(tau, X_O, color='#2563eb', lw=2.2, label=r'Độ lệch 2 nguyên tử O: $X_{\mathrm{O}}(t)$')
    ax.plot(tau, X_C, color='#dc2626', lw=2.2, label=r'Độ lệch nguyên tử C: $X_{\mathrm{C}}(t) = -\frac{8}{3} X_{\mathrm{O}}(t)$')
    ax.axhline(0, color='#64748b', lw=0.8)
    ax.set(xlabel=r'Thời gian chuẩn hóa $t / T$', ylabel='Độ dịch chuyển tương đối',
           title=r'Dao động mode kéo dãn bất đối xứng của $\mathrm{CO}_2$ (Bảo toàn khối tâm)')
    ax.grid(alpha=0.25)
    ax.legend(fontsize=11, loc='upper right')
    save_svg(fig, 'loi-giai-d-06')

    # 7. loi-giai-d-07: Phổ hấp thụ dao động - quay khí bí ẩn N2 (Bài 42.52)
    fig, ax = plt.subplots(figsize=(8, 4.5))
    E_lines = np.array([0.28803, 0.28852, 0.28951, 0.29000, 0.29050])
    labels = [r'$P(2)$', r'$P(1)\to l=0$', r'$R(0)\leftarrow l=0$', r'$R(1)$', r'$R(2)$']
    for e_val, lbl in zip(E_lines, labels):
        ax.axvline(e_val * 1e3, ymin=0.1, ymax=0.9, color='#2563eb', lw=2.2)
        ax.text(e_val * 1e3, 0.93, lbl, ha='center', fontsize=11, rotation=0)
    ax.axvline(289.014, color='#dc2626', ls='--', lw=1.5, label=r'Tần số cơ bản $\hbar\omega \approx 289{,}01\,\mathrm{meV}$ (vắng mặt)')
    ax.annotate('', xy=(288.523 * 1e3, 0.5), xytext=(289.506 * 1e3, 0.5),
                arrowprops=dict(arrowstyle='<->', color='#b45309', lw=1.5))
    ax.text(289.014 * 1e3, 0.53, r'Khoảng trống $4B \approx 0{,}98\,\mathrm{meV}$', ha='center', fontsize=11, color='#b45309')
    ax.set(xlabel='Năng lượng photon (meV)', ylabel='Cường độ tương đối',
           xlim=(287.5, 291.0), ylim=(0, 1.1), yticks=[],
           title=r'Cấu trúc vạch hấp thụ nhánh P và nhánh R của phân tử $\mathrm{N}_2$')
    ax.grid(alpha=0.25, axis='x')
    ax.legend(fontsize=11, loc='lower left')
    save_svg(fig, 'loi-giai-d-07')

    # 8. loi-giai-d-08: Áp suất và môđun khối khí electron thoái hóa (Bài 42.53 & 42.54)
    fig, ax = plt.subplots(figsize=(7.5, 4.5))
    n_dense = np.linspace(1e28, 2e29, 300)
    p_deg = (3.0**(2/3) * np.pi**(4/3) * (1.05457e-34)**2 / (5 * 9.10938e-31)) * (n_dense**(5/3))
    B_deg = (5.0 / 3.0) * p_deg
    ax.plot(n_dense / 1e28, p_deg / 1e10, color='#2563eb', lw=2.2, label=r'Áp suất thoái hóa $p(n)$')
    ax.plot(n_dense / 1e28, B_deg / 1e10, color='#059669', lw=2.2, label=r'Môđun khối $B(n) = \frac{5}{3}p$')
    n_Cu = 8.45
    p_Cu = (3.0**(2/3) * np.pi**(4/3) * (1.05457e-34)**2 / (5 * 9.10938e-31)) * ((8.45e28)**(5/3)) / 1e10
    ax.scatter([n_Cu], [p_Cu], color='#dc2626', s=60, zorder=4, label=r'Đồng: $p \approx 3{,}81 \times 10^{10}\,\mathrm{Pa}$')
    ax.scatter([n_Cu], [5/3 * p_Cu], color='#b45309', s=60, zorder=4, label=r'Đồng: $B \approx 6{,}34 \times 10^{10}\,\mathrm{Pa}$')
    ax.set(xlabel=r'Nồng độ electron $n$ ($10^{28}\,\mathrm{m}^{-3}$)', ylabel=r'Áp suất / Môđun khối ($10^{10}\,\mathrm{Pa}$)',
           title='Khí electron tự do thoái hóa lượng tử ở nhiệt độ thấp')
    ax.grid(alpha=0.25)
    ax.legend(fontsize=11, loc='upper left')
    save_svg(fig, 'loi-giai-d-08')

    # 9. loi-giai-d-09: Cảm biến nhiệt độ diode MCAT 42.56-42.58
    fig, ax = plt.subplots(figsize=(7.5, 4.5))
    T_C = np.linspace(25, 150, 200)
    # V(T) = V_25 + S * (T - 25) with S = -2.0 mV/°C
    V_T = 0.770 - 0.0020 * (T_C - 25)
    ax.plot(T_C, V_T, color='#2563eb', lw=2.4, label=r'Điện áp ở dòng không đổi $I = 100\,\mathrm{mA}$')
    ax.scatter([25, 150], [0.770, 0.520], color='#dc2626', s=60, zorder=4)
    ax.annotate(r'$25^\circ\mathrm{C}: 0{,}77\,\mathrm{V}$', xy=(25, 0.770), xytext=(35, 0.78), fontsize=11)
    ax.annotate(r'$150^\circ\mathrm{C}: 0{,}52\,\mathrm{V}$', xy=(150, 0.520), xytext=(120, 0.54), fontsize=11)
    ax.set(xlabel=r'Nhiệt độ $T$ ($^\circ\mathrm{C}$)', ylabel='Điện áp thuận $V$ (V)',
           title=r'Đặc tuyến cảm biến nhiệt độ diode: Độ nhạy $S = -2{,}0\,\mathrm{mV/^\circ C}$')
    ax.grid(alpha=0.25)
    ax.legend(fontsize=11, loc='upper right')
    save_svg(fig, 'loi-giai-d-09')

    # 10. loi-giai-d-10: Bài tập cầu nối HF -> InSb
    fig, ax = plt.subplots(figsize=(8, 4.6))
    # Năng lượng dải bán dẫn InSb: Valence band top Ev = 0, Conduction band Ec = 0.230 eV
    ax.axhspan(-0.1, 0.0, color='#93c5fd', alpha=0.4, label='Dải hóa trị InSb (đầy electron)')
    ax.axhspan(0.230, 0.65, color='#fed7aa', alpha=0.4, label='Dải dẫn InSb (trống)')
    ax.axhline(0.0, color='#1e40af', lw=1.5, ls='-')
    ax.axhline(0.230, color='#c2410c', lw=1.5, ls='-')
    ax.axhline(0.115, color='#64748b', lw=1.2, ls=':', label=r'Mức Fermi $E_F = 0{,}115\,\mathrm{eV}$')
    # Electron hấp thụ photon photon_E = 0.508 eV
    ax.annotate('', xy=(0.5, 0.508), xytext=(0.5, 0.0),
                arrowprops=dict(arrowstyle='->', color='#dc2626', lw=2.2))
    ax.text(0.53, 0.25, r'Hấp thụ photon $\mathrm{HF}$' + '\n' + r'$E_{\mathrm{ph}} = 0{,}508\,\mathrm{eV}$',
            color='#dc2626', fontsize=12, va='center')
    ax.scatter([0.5], [0.508], color='#dc2626', s=70, zorder=5)
    ax.text(0.53, 0.508, r'Trạng thái cuối: $E = E_c + 0{,}278\,\mathrm{eV}$' + '\n' + r'$f(E) \approx 1{,}8 \times 10^{-25}$',
            fontsize=11, va='center')
    ax.set(xlim=(0.2, 0.9), ylim=(-0.08, 0.62), xticks=[],
           ylabel='Năng lượng (eV)',
           title='Quang kích thích electron InSb bởi photon phân tử HF')
    ax.grid(alpha=0.2, axis='y')
    ax.legend(fontsize=11, loc='lower left')
    save_svg(fig, 'loi-giai-d-10')

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    rows = []
    pdf_path = ROOT / 'raw_materials/physics/source/young-freedman-15.pdf'
    with fitz.open(pdf_path) as pdf:
        for stem, (page, clip) in CROPS.items():
            pix = pdf[page - 1].get_pixmap(matrix=fitz.Matrix(SCALE, SCALE), clip=fitz.Rect(clip), alpha=False)
            p = OUT / f'{stem}.png'
            pix.save(p)
            with Image.open(p) as im:
                assert im.size == (pix.width, pix.height) and im.convert('RGB').tobytes() == pix.samples
            sha = hashlib.sha256(p.read_bytes()).hexdigest()
            rows.append(dict(stem=stem, pdfPage=page, clip=clip, scale=SCALE, pixelMatch=True, sha256=sha, size=(pix.width, pix.height)))
    print(f'Extracted {len(rows)} figures successfully:')
    for r in rows:
        print(r)
    prepare_solution_plots()
    print('Reproduced ten solution plots from numerical functions and physical formulas.')

if __name__ == '__main__':
    main()
