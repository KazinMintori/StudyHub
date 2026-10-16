"""Trích xuất hình ảnh và sinh biểu đồ minh họa giải toán cho Chapter 41 (nhóm D)."""
from pathlib import Path
import hashlib
import pymupdf as fitz
from PIL import Image
import numpy as np
import scipy.constants as const
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
CROPS = {
    'hinh-p41-57': (1425, (359, 74, 575, 270)),
}
SCALE = 3
OUT = ROOT / 'docs/vat-ly-2/bai-giang/img/young-41'

def prepare_solution_plots():
    """Tạo 10 biểu đồ trực quan hóa số liệu và hàm giải tích cho lời giải nhóm D."""
    plt.rcParams.update({
        'font.family': 'DejaVu Sans',
        'font.size': 14,
        'svg.fonttype': 'none',
        'svg.hashsalt': 'StudyHub-physics41-d'
    })

    def save(fig, name):
        svg = OUT / (name + '.svg')
        fig.savefig(svg, bbox_inches='tight', facecolor='white', metadata={'Date': None})
        svg.write_text('\n'.join(line.rstrip() for line in svg.read_text(encoding='utf-8').splitlines()) + '\n', encoding='utf-8')
        plt.close(fig)

    # 1. loi-giai-d-01: Hiệu ứng Zeeman thường cho bước chuyển 2p -> 1s (Bài 41.24)
    fig, ax = plt.subplots(figsize=(8, 4.8))
    # Mức 2p không có từ trường và có từ trường
    ax.hlines(y=2.5, xmin=0.5, xmax=2.0, color='#64748b', lw=2.5, label='Không từ trường')
    ax.text(0.3, 2.5, '2p', va='center', ha='right', fontweight='bold')

    # Mức 2p khi có B: m_l = +1, 0, -1
    ax.hlines(y=3.2, xmin=3.0, xmax=4.5, color='#2563eb', lw=2)
    ax.text(4.6, 3.2, r'$m_l = +1$', va='center')
    ax.hlines(y=2.5, xmin=3.0, xmax=4.5, color='#2563eb', lw=2)
    ax.text(4.6, 2.5, r'$m_l = 0$', va='center')
    ax.hlines(y=1.8, xmin=3.0, xmax=4.5, color='#2563eb', lw=2)
    ax.text(4.6, 1.8, r'$m_l = -1$', va='center')

    # Mức 1s (m_l = 0)
    ax.hlines(y=0.2, xmin=0.5, xmax=2.0, color='#64748b', lw=2.5)
    ax.text(0.3, 0.2, '1s', va='center', ha='right', fontweight='bold')
    ax.hlines(y=0.2, xmin=3.0, xmax=4.5, color='#0f172a', lw=2)
    ax.text(4.6, 0.2, r'$m_l = 0$', va='center')

    # Ba bước chuyển
    ax.annotate('', xy=(3.3, 0.25), xytext=(3.3, 3.15),
                arrowprops=dict(arrowstyle='->', color='#dc2626', lw=1.8))
    ax.text(3.3, 0.7, r'$\lambda_1 < \lambda_0$', color='#dc2626', ha='center', fontsize=14)

    ax.annotate('', xy=(3.75, 0.25), xytext=(3.75, 2.45),
                arrowprops=dict(arrowstyle='->', color='#16a34a', lw=1.8))
    ax.text(3.75, 1.1, r'$\lambda_2 = \lambda_0$', color='#16a34a', ha='center', fontsize=14)

    ax.annotate('', xy=(4.2, 0.25), xytext=(4.2, 1.75),
                arrowprops=dict(arrowstyle='->', color='#2563eb', lw=1.8))
    ax.text(4.2, 0.7, r'$\lambda_3 > \lambda_0$', color='#2563eb', ha='center', fontsize=14)

    ax.set(xlim=(0, 6), ylim=(-0.2, 3.8), title='Tách mức Zeeman thường và ba vạch dịch chuyển (2p → 1s)')
    ax.axis('off')
    save(fig, 'loi-giai-d-01')

    # 2. loi-giai-d-02: Năng lượng tương tác spin trong từ trường ngoài (Bài 41.27, 41.28)
    B_vals = np.linspace(0, 3.0, 100)
    mu_B_val = 5.788e-5 # eV/T
    fig, ax = plt.subplots(figsize=(7.5, 4.5))
    ax.plot(B_vals, mu_B_val * B_vals * 1e4, label=r'Spin hướng xuống ($m_s = -1/2$): $U = +\mu_B B$', color='#dc2626', lw=2)
    ax.plot(B_vals, -mu_B_val * B_vals * 1e4, label=r'Spin hướng lên ($m_s = +1/2$): $U = -\mu_B B$', color='#2563eb', lw=2)
    ax.axhline(0, color='#64748b', lw=0.8, ls='--')
    ax.set(xlabel='Độ lớn B của từ trường hướng âm trục z (T)', ylabel=r'Năng lượng tương tác spin $U$ ($10^{-4}$ eV)',
           title='Tách mức spin electron khi từ trường hướng âm trục z')
    ax.legend(fontsize=14, loc='upper center', bbox_to_anchor=(0.5,-0.22))
    ax.grid(alpha=0.2)
    save(fig, 'loi-giai-d-02')

    # 3. loi-giai-d-03: Hiệu ứng xuyên sâu và điện tích hạt nhân hiệu dụng Kali (Bài 41.34)
    states = ['4s (l=0)', '4p (l=1)', '4d (l=2)']
    zeff_vals = 4 * np.sqrt(np.array([4.339, 2.73, 0.94]) / 13.6)
    fig, ax = plt.subplots(figsize=(7, 4.5))
    bars = ax.bar(states, zeff_vals, color=['#2563eb', '#0891b2', '#0d9488'], width=0.55)
    ax.axhline(1.0, color='#dc2626', ls='--', lw=1.5, label='Chắn hoàn toàn bởi 18 e lõi (Z_eff = 1)')
    for bar in bars:
        h = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., h + 0.04, f'{h:.2f}', ha='center', va='bottom', fontweight='bold')
    ax.set(ylabel='Điện tích hiệu dụng $Z_{\\mathrm{eff}}$', ylim=(0, 2.7),
           title='Điện tích hiệu dụng các trạng thái n = 4 của Kali')
    ax.legend(fontsize=14, loc='upper center', bbox_to_anchor=(0.5,-0.22))
    ax.grid(axis='y', alpha=0.2)
    save(fig, 'loi-giai-d-03')

    # 4. loi-giai-d-04: Đồ thị định luật Moseley cho tia X K_alpha (Bài 41.37)
    Z_arr = np.array([20, 27, 48])
    labels_elem = ['Ca (Z=20)', 'Co (Z=27)', 'Cd (Z=48)']
    E_arr = (Z_arr - 1)**2 * 10.204e-3 # keV
    sqrt_f = (Z_arr - 1) * np.sqrt(0.75 * 13.606 * const.e / const.h) / 1e8 # 10^8 Hz^(1/2)
    Z_plot = np.linspace(15, 52, 100)
    sqrt_f_line = (Z_plot - 1) * np.sqrt(0.75 * 13.606 * const.e / const.h) / 1e8
    fig, ax = plt.subplots(figsize=(7.5, 4.8))
    ax.plot(Z_plot, sqrt_f_line, color='#2563eb', lw=2, label=r'Định luật Moseley: $\sqrt{f} \propto (Z - 1)$')
    ax.scatter(Z_arr, sqrt_f, color='#dc2626', s=60, zorder=4, label='Số liệu Ca, Co, Cd')
    for z, sf, name in zip(Z_arr, sqrt_f, labels_elem):
        ax.text(z, sf - 0.9, name, ha='center', fontsize=14, fontweight='bold', color='#0f172a')
    ax.set(xlabel='Số hiệu nguyên tử Z', ylabel=r'$\sqrt{f}$ ($10^8\ \mathrm{Hz}^{1/2}$)',
           title=r'Đồ thị tuyến tính Moseley cho vạch phát xạ $K_\alpha$')
    ax.legend(fontsize=14, loc='upper left')
    ax.grid(alpha=0.2)
    save(fig, 'loi-giai-d-04')

    # 5. loi-giai-d-05: Mật độ xác suất xuyên tâm P(r) cho 1s và 2p hydro (Bài 41.50, 41.51)
    r_a0 = np.linspace(0, 14, 500)
    P_1s = 4.0 * (r_a0**2) * np.exp(-2.0 * r_a0)
    P_2p = (1.0 / 24.0) * (r_a0**4) * np.exp(-r_a0)
    fig, ax = plt.subplots(figsize=(8, 4.6))
    ax.plot(r_a0, P_1s, label='Trạng thái 1s (cực đại tại $r = a_0$)', color='#2563eb', lw=2)
    ax.plot(r_a0, P_2p, label=r'Trạng thái 2p (cực đại tại $r = 4a_0$)', color='#d97706', lw=2)
    ax.axvline(1.0, color='#2563eb', ls=':', lw=1.2)
    ax.axvline(4.0, color='#d97706', ls=':', lw=1.2)
    ax.set(xlabel=r'Khoảng cách $r / a_0$', ylabel=r'Xác suất xuyên tâm $a_0 P(r)$',
           title='Vị trí xác suất lớn nhất trùng khớp bán kính Bohr')
    ax.legend(fontsize=14, loc='upper center', bbox_to_anchor=(0.5,-0.22))
    ax.grid(alpha=0.2)
    save(fig, 'loi-giai-d-05')

    # 6. loi-giai-d-06: Khớp tuyến tính thực nghiệm ESR f vs B (Bài 41.63)
    B_pts = np.array([0.51, 0.74, 1.03, 1.52, 2.02, 2.48, 2.97])
    lam_pts_mm = np.array([21.4, 14.3, 10.7, 7.14, 5.35, 4.28, 3.57])
    f_pts_GHz = (const.c / (lam_pts_mm * 1e-3)) / 1e9
    slope_fit, intercept_fit = np.polyfit(B_pts, f_pts_GHz, 1)
    B_grid = np.linspace(0.4, 3.1, 100)
    fig, ax = plt.subplots(figsize=(7.5, 4.8))
    ax.plot(B_grid, slope_fit * B_grid + intercept_fit, color='#2563eb', lw=2,
            label=f'Khớp tuyến tính: $f = {slope_fit:.2f} B {intercept_fit:+.2f}$ GHz')
    ax.scatter(B_pts, f_pts_GHz, color='#dc2626', s=55, zorder=4, label='7 điểm số liệu thực nghiệm')
    ax.set(xlabel='Từ trường ngoài B (T)', ylabel='Tần số hấp thụ f (GHz)',
           title='Cộng hưởng spin electron (ESR): Tần số f theo từ trường B')
    ax.legend(fontsize=14, loc='upper left')
    ax.grid(alpha=0.2)
    save(fig, 'loi-giai-d-06')

    # 7. loi-giai-d-07: Năng lượng ion hóa và Z_eff dãy kim loại kiềm (Bài 41.65)
    elem_names = ['Li', 'Na', 'K', 'Rb', 'Cs', 'Fr']
    Z_nums = [3, 11, 19, 37, 55, 87]
    E_ion_eV = [5.391, 5.139, 4.341, 4.177, 3.894, 3.938]
    Z_eff_vals = [1.259, 1.844, 2.259, 2.771, 3.210, 3.766]
    fig, ax1 = plt.subplots(figsize=(8, 4.8))
    color1 = '#2563eb'
    ax1.plot(Z_nums, E_ion_eV, marker='o', color=color1, lw=2, label='Năng lượng ion hóa (eV)')
    ax1.set_xlabel('Số hiệu nguyên tử Z')
    ax1.set_ylabel('Năng lượng ion hóa (eV)', color=color1)
    ax1.tick_params(axis='y', labelcolor=color1)
    ax1.set_ylim(3.0, 6.0)

    for z, e_val, name in zip(Z_nums, E_ion_eV, elem_names):
        ax1.text(z, e_val + 0.15, name, ha='center', fontsize=14, fontweight='bold', color=color1)

    ax2 = ax1.twinx()
    color2 = '#d97706'
    ax2.plot(Z_nums, Z_eff_vals, marker='s', color=color2, lw=2, ls='--', label=r'Điện tích hiệu dụng $Z_{\mathrm{eff}}$')
    ax2.set_ylabel(r'Điện tích hạt nhân hiệu dụng $Z_{\mathrm{eff}}$', color=color2)
    ax2.tick_params(axis='y', labelcolor=color2)
    ax2.set_ylim(0.5, 4.5)

    ax1.set_title('Xu hướng ion hóa và hiệu ứng chắn của dãy kim loại kiềm')
    ax1.grid(alpha=0.2)
    save(fig, 'loi-giai-d-07')

    # 8. loi-giai-d-08: Phổ năng lượng 2N electron trong dao động tử điều hòa 1D (Bài 41.68)
    fig, ax = plt.subplots(figsize=(7, 5))
    k_levels = 5
    for k in range(k_levels):
        y = k + 0.5
        ax.hlines(y=y, xmin=0.2, xmax=0.8, color='#0f172a', lw=2.5)
        # 2 electron: spin up and down
        ax.annotate('', xy=(0.4, y + 0.25), xytext=(0.4, y - 0.25),
                    arrowprops=dict(arrowstyle='->', color='#2563eb', lw=2.5))
        ax.annotate('', xy=(0.6, y - 0.25), xytext=(0.6, y + 0.25),
                    arrowprops=dict(arrowstyle='->', color='#dc2626', lw=2.5))
        ax.text(0.85, y, f'$k = {k},\\ E_{k} = ({k} + 1/2)\\hbar\\omega$', va='center', fontsize=14)
    ax.text(0.5, 5.2, '... Tiếp tục điền 2 electron mỗi mức đến k = N - 1 ...', ha='center', fontsize=14, style='italic')
    ax.set(xlim=(0, 1.4), ylim=(0, 5.6), title=r'Điền 2N fermion vào dao động tử: Tổng $E = N^2 \hbar\omega$')
    ax.axis('off')
    save(fig, 'loi-giai-d-08')


    # 9. Directions of forces in the stated two-electron ring model.
    fig, ax = plt.subplots(figsize=(8,5))
    angle=np.linspace(0,2*np.pi,300)
    ax.plot(np.cos(angle),np.sin(angle),'--',color='#94a3b8',lw=1.8)
    ax.scatter([0],[0],s=130,color='#dc2626',zorder=4,label='Hạt nhân (+2e)')
    ax.scatter([-1,1],[0,0],s=110,color='#2563eb',zorder=4,label='Electron (−e)')
    ax.text(0,-.23,'+2e',ha='center',color='#dc2626',fontsize=14)
    ax.text(-1,.18,r'$e_1$',ha='center',color='#2563eb',fontsize=14)
    ax.text(1,.18,r'$e_2$',ha='center',color='#2563eb',fontsize=14)
    ax.annotate('',xy=(.25,0),xytext=(.96,0),
                arrowprops=dict(arrowstyle='->',color='#dc2626',lw=2.5))
    ax.annotate('',xy=(1.65,0),xytext=(1.04,0),
                arrowprops=dict(arrowstyle='->',color='#059669',lw=2.5))
    ax.text(.52,.17,r'$F_{\mathrm{hút}}$',ha='center',color='#dc2626',fontsize=14)
    ax.text(1.58,.17,r'$F_{\mathrm{đẩy}}$',ha='center',color='#059669',fontsize=14)
    ax.text(.25,-1.28,'Hướng lực lên electron bên phải, mũi tên không theo tỷ lệ',ha='center',fontsize=14,color='#475569')
    ax.set(xlim=(-1.6,2.1),ylim=(-1.4,1.3),aspect='equal')
    ax.axis('off');ax.legend(loc='upper center',bbox_to_anchor=(.5,-.02),fontsize=14)
    ax.set_title('Mô hình hai electron đối nhau trên quỹ đạo tròn của heli',fontsize=16,pad=16)
    save(fig,'loi-giai-d-09')

    # 10. loi-giai-d-10: Các mức năng lượng bị chiếm của Titanium trong hộp lập phương (Bài tập cầu nối)
    fig, ax = plt.subplots(figsize=(8, 5.2))
    levels = [
        (3, 2, 20.1, r'$E_{1,1,1} = 20{,}1$ eV (2 e)'),
        (6, 6, 40.2, r'$E_{2,1,1} = 40{,}2$ eV (6 e)'),
        (9, 6, 60.3, r'$E_{2,2,1} = 60{,}3$ eV (6 e)'),
        (11, 6, 73.7, r'$E_{3,1,1} = 73{,}7$ eV (6 e)'),
        (12, 2, 80.4, r'$E_{2,2,2} = 80{,}4$ eV (2 e)')
    ]
    for k, n_e, e_val, lbl in levels:
        ax.hlines(y=e_val, xmin=1.0, xmax=3.5, color='#0f172a', lw=2.2)
        ax.text(3.7, e_val, lbl, va='center', fontsize=14)

    # Mũi tên chuyển mức (2,2,2) -> (1,1,1)
    ax.annotate('', xy=(1.8, 20.5), xytext=(1.8, 80.0),
                arrowprops=dict(arrowstyle='->', color='#dc2626', lw=2.5))
    ax.text(2.0, 50.0, 'Photon\n'+r'$\Delta E = 60{,}3\,\mathrm{eV}$', color='#dc2626', ha='left', va='center', fontsize=14)

    ax.set(xlim=(0, 6.2), ylim=(10, 90), ylabel='Năng lượng E (eV)',
           title='5 mức năng lượng bị chiếm bởi 22 electron của Titan trong hộp lập phương')
    ax.grid(axis='y', alpha=0.2)
    ax.set_xticks([])
    save(fig, 'loi-giai-d-10')

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
        print(r)
    prepare_solution_plots()
    print('Generated 10 solution plots successfully.')

if __name__ == '__main__':
    main()
