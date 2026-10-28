"""Kịch bản kiểm tra độc lập bằng Python cho nhóm bài tập Chapter 20 nhóm C.

Bao gồm:
- 12 bài luyện tập hướng dẫn: VP20.1.1–VP20.1.4, VP20.4.1–VP20.4.4, VP20.10.1–VP20.10.4.
- 23 câu hỏi thảo luận: Q20.1 đến Q20.23.
- 1 bài tập cầu nối: Bridging Problem (Entropy Changes: Cold Ice in Hot Water).
Tổng cộng: Đúng 36 lời giải độc lập.

Tất cả kết quả tính toán độc lập từ các hằng số vật lý chuẩn trong Young & Freedman (15th ed).
Đồng thời kiểm tra sự tồn tại và tính nguyên vẹn RGB của các ảnh cắt gốc.
"""
from pathlib import Path
import math
import numpy as np
import pymupdf as fitz
from PIL import Image

ROOT = Path(__file__).resolve().parents[2]

# Các hằng số vật lý chuẩn (Young & Freedman 15th ed / CODATA)
R = 8.314462618        # Hằng số khí lý tưởng (J/(mol*K))
c_w = 4190.0           # Nhiệt dung riêng của nước lỏng (J/(kg*K))
c_ice = 2100.0         # Nhiệt dung riêng của nước đá (J/(kg*K))
Lf_water = 3.34e5      # Nhiệt nóng chảy của nước đá (J/kg)
T_freeze_K = 273.15    # Điểm đóng băng của nước (K)

results = {}


def verify_guided_practice():
    """Xác minh 12 bài luyện tập hướng dẫn VP20.1.1 - VP20.10.4."""
    # VP20.1.1: Động cơ diesel có hiệu suất e = 0.180, sinh công W = 1.24e4 J
    e_11 = 0.180
    W_11 = 1.24e4
    QH_11 = W_11 / e_11
    QC_11 = QH_11 - W_11
    results['VP20.1.1'] = {'QH': QH_11, 'QC': QC_11}
    assert abs(QH_11 - 6.889e4) < 100.0, "Lỗi VP20.1.1 (a): Nhiệt lượng nhận vào"
    assert abs(QC_11 - 5.649e4) < 100.0, "Lỗi VP20.1.1 (b): Nhiệt lượng thải ra"

    # VP20.1.2: Động cơ nhiệt nhận QH = 3.82e4 J, thải |QC| = 3.16e4 J
    QH_12 = 3.82e4
    QC_12 = 3.16e4
    e_12 = 1.0 - QC_12 / QH_12
    results['VP20.1.2'] = {'e': e_12}
    assert abs(e_12 - 0.17277) < 0.001, "Lỗi VP20.1.2: Hiệu suất nhiệt"

    # VP20.1.3: Động cơ xăng e = 0.196, thải |QC| = 4.96e8 J trong 20 phút
    e_13 = 0.196
    QC_13 = 4.96e8
    QH_13 = QC_13 / (1.0 - e_13)
    W_13 = QH_13 - QC_13
    results['VP20.1.3'] = {'QH': QH_13, 'W': W_13}
    assert abs(QH_13 - 6.169e8) < 1e6, "Lỗi VP20.1.3 (a): Nhiệt nhận vào"
    assert abs(W_13 - 1.209e8) < 1e6, "Lỗi VP20.1.3 (b): Công sinh ra"

    # VP20.1.4: Động cơ piston máy bay P = 1.10e5 W, đốt 34 kg xăng/giờ, năng suất tỏa nhiệt 5.0e7 J/kg
    P_14 = 1.10e5
    t_14 = 3600.0
    W_14 = P_14 * t_14
    m_14 = 34.0
    qc_14 = 5.0e7
    QH_14 = m_14 * qc_14
    e_14 = W_14 / QH_14
    results['VP20.1.4'] = {'W': W_14, 'QH': QH_14, 'e': e_14}
    assert abs(W_14 - 3.96e8) < 1e6, "Lỗi VP20.1.4 (a): Công sinh ra trong 1 giờ"
    assert abs(QH_14 - 1.70e9) < 1e7, "Lỗi VP20.1.4 (b): Nhiệt lượng cấp trong 1 giờ"
    assert abs(e_14 - 0.2329) < 0.01, "Lỗi VP20.1.4 (c): Hiệu suất nhiệt"

    # VP20.4.1: Động cơ Carnot nhận QH = 8.00e4 J, sinh công W = 1.68e4 J, nguồn lạnh TC = 25.0 C
    QH_41 = 8.00e4
    W_41 = 1.68e4
    TC_41 = 25.0 + 273.15
    e_41 = W_41 / QH_41
    QC_41 = QH_41 - W_41
    TH_41 = TC_41 / (1.0 - e_41)
    TH_41_C = TH_41 - 273.15
    results['VP20.4.1'] = {'e': e_41, 'QC': QC_41, 'TH_C': TH_41_C}
    assert abs(e_41 - 0.210) < 1e-4, "Lỗi VP20.4.1 (a): Hiệu suất Carnot"
    assert abs(QC_41 - 6.32e4) < 10.0, "Lỗi VP20.4.1 (b): Nhiệt lượng thải"
    assert abs(TH_41_C - 104.3) < 0.5, "Lỗi VP20.4.1 (c): Nhiệt độ nguồn nóng theo độ C"

    # VP20.4.2: Chu trình Carnot Ví dụ 20.3: n = 0.200 mol khí lưỡng nguyên tử, TH = 500 K, hạ TC từ 27 C xuống -73 C (200 K)
    n_42 = 0.200
    TH_42 = 500.0
    TC_42 = 200.0
    CV_42 = 2.5 * R
    e_42 = 1.0 - TC_42 / TH_42
    Wab_42 = n_42 * R * TH_42 * math.log(2.0)
    Wbc_42 = n_42 * CV_42 * (TH_42 - TC_42)
    Wcd_42 = - n_42 * R * TC_42 * math.log(2.0)
    Wda_42 = - Wbc_42
    results['VP20.4.2'] = {'e': e_42, 'Wab': Wab_42, 'Wbc': Wbc_42, 'Wcd': Wcd_42, 'Wda': Wda_42}
    assert abs(e_42 - 0.60) < 1e-4, "Lỗi VP20.4.2 (a): Hiệu suất mới"
    assert abs(Wab_42 - 576.3) < 2.0, "Lỗi VP20.4.2 (b): Công giãn đẳng nhiệt Wab"
    assert abs(Wbc_42 - 1247.2) < 5.0, "Lỗi VP20.4.2 (b): Công giãn đoạn nhiệt Wbc"
    assert abs(Wcd_42 - (-230.5)) < 2.0, "Lỗi VP20.4.2 (b): Công nén đẳng nhiệt Wcd"
    assert abs(Wda_42 - (-1247.2)) < 5.0, "Lỗi VP20.4.2 (b): Công nén đoạn nhiệt Wda"

    # VP20.4.3: Tủ lạnh Carnot có TC = -10.0 C (263.15 K), TH = 25.0 C (298.15 K), rút QC = 4.00e6 J
    TC_43 = -10.0 + 273.15
    TH_43 = 25.0 + 273.15
    K_43 = TC_43 / (TH_43 - TC_43)
    Win_43 = 4.00e6 / K_43
    results['VP20.4.3'] = {'K': K_43, 'Win': Win_43}
    assert abs(K_43 - 7.5186) < 0.01, "Lỗi VP20.4.3 (a): Hệ số làm lạnh K"
    assert abs(Win_43 - 5.320e5) < 1000.0, "Lỗi VP20.4.3 (b): Công tiêu tốn Win"

    # VP20.4.4: Động cơ Carnot dùng n mol khí argon (CV = 1.5 R), Vb = 2 Va, Wab = Wbc
    ratio_44 = 1.0 - (2.0 / 3.0) * math.log(2.0)
    e_44 = (2.0 / 3.0) * math.log(2.0)
    results['VP20.4.4'] = {'TC_TH': ratio_44, 'e': e_44}
    assert abs(ratio_44 - 0.5379) < 0.001, "Lỗi VP20.4.4 (c): Tỉ số TC/TH"
    assert abs(e_44 - 0.4621) < 0.001, "Lỗi VP20.4.4 (c): Hiệu suất e"

    # VP20.10.1: 1.00 kg ethanol ban đầu ở 159 K, Lf = 1.042e5 J/kg, c = 2428 J/(kg*K), sôi ở 351 K, Lv = 8.54e5 J/kg
    DS_101_a = 1.042e5 / 159.0
    DS_101_b = 2428.0 * math.log(351.0 / 159.0)
    DS_101_c = 8.54e5 / 351.0
    results['VP20.10.1'] = {'DS_a': DS_101_a, 'DS_b': DS_101_b, 'DS_c': DS_101_c}
    assert abs(DS_101_a - 655.35) < 1.0, "Lỗi VP20.10.1 (a): Entropy nóng chảy"
    assert abs(DS_101_b - 1920.7) < 5.0, "Lỗi VP20.10.1 (b): Entropy tăng nhiệt độ lỏng"
    assert abs(DS_101_c - 2433.0) < 5.0, "Lỗi VP20.10.1 (c): Entropy hóa hơi"

    # VP20.10.2: 5.00 mol He từ V1 = 0.120 m^3, T1 = 20.0 C đến V2 = 0.360 m^3, T2 = 20.0 C
    DS_102 = 5.00 * R * math.log(0.360 / 0.120)
    results['VP20.10.2'] = {'DS_a': DS_102, 'DS_b': DS_102}
    assert abs(DS_102 - 45.67) < 0.1, "Lỗi VP20.10.2: Độ biến thiên entropy"

    # VP20.10.3: Chu trình không Carnot nhận QH = 8.00e4 J ở 260 C (533.15 K), sinh W = 1.60e4 J, thải QC = 6.40e4 J ở 20 C (293.15 K)
    DS_103_eng = 0.0
    DS_103_H = - 8.00e4 / (260.0 + 273.15)
    DS_103_C = 6.40e4 / (20.0 + 273.15)
    DS_103_tot = DS_103_eng + DS_103_H + DS_103_C
    results['VP20.10.3'] = {'eng': DS_103_eng, 'H': DS_103_H, 'C': DS_103_C, 'tot': DS_103_tot}
    assert DS_103_eng == 0.0, "Lỗi VP20.10.3 (a): Entropy động cơ qua chu trình kín"
    assert abs(DS_103_H - (-150.07)) < 0.5, "Lỗi VP20.10.3 (b): Entropy nguồn nóng"
    assert abs(DS_103_C - 218.32) < 0.5, "Lỗi VP20.10.3 (c): Entropy nguồn lạnh"
    assert abs(DS_103_tot - 68.25) < 0.5, "Lỗi VP20.10.3 (d): Tổng entropy hệ"
    assert DS_103_tot > 0.0, "Lỗi VP20.10.3 (d): Tổng entropy phải tăng"

    # VP20.10.4: 1.00 kg đá ở 0 C (Lf = 3.34e5 J/kg) trộn với 0.839 kg nước ở 95.0 C (c = 4190 J/(kg*K)), cân bằng ở 0.0 C
    DS_104_ice = 1.00 * Lf_water / 273.15
    DS_104_w = 0.839 * c_w * math.log(273.15 / (95.0 + 273.15))
    DS_104_tot = DS_104_ice + DS_104_w
    results['VP20.10.4'] = {'ice': DS_104_ice, 'water': DS_104_w, 'tot': DS_104_tot}
    assert abs(DS_104_ice - 1222.8) < 5.0, "Lỗi VP20.10.4 (a): Entropy đá tan"
    assert abs(DS_104_w - (-1049.2)) < 5.0, "Lỗi VP20.10.4 (b): Entropy nước tỏa nhiệt"
    assert abs(DS_104_tot - 173.6) < 5.0, "Lỗi VP20.10.4 (c): Tổng biến thiên entropy"
    assert DS_104_tot > 0.0, "Lỗi VP20.10.4 (c): Tổng entropy phải tăng"
    print("✓ Xác minh thành công 12 bài luyện tập hướng dẫn (VP20.1.1 - VP20.10.4).")


def verify_bridging_problem():
    """Xác minh bài tập cầu nối: Nước đá lạnh trong nước nóng (Bridging Problem)."""
    m_w = 0.600
    m_ice = 0.0500
    T_w_init = 45.0
    T_ice_init = -15.0

    # 1. Nhiệt lượng làm nóng nước đá từ -15.0 C lên 0.0 C
    Q1 = m_ice * c_ice * (0.0 - T_ice_init)  # 0.0500 * 2100 * 15 = 1575.0 J
    # 2. Nhiệt lượng làm tan chảy hoàn toàn nước đá ở 0.0 C
    Q2 = m_ice * Lf_water                    # 0.0500 * 3.34e5 = 16700.0 J
    Q_ice_needed = Q1 + Q2                   # 18275.0 J
    # Nhiệt lượng cực đại mà nước ấm có thể tỏa ra nếu hạ xuống 0.0 C
    Q_w_max = m_w * c_w * (T_w_init - 0.0)   # 0.600 * 4190 * 45 = 113130.0 J
    assert Q_w_max > Q_ice_needed, "Nước đá tan hết hoàn toàn vì nước ấm tỏa thừa nhiệt lượng."

    # Nhiệt độ cân bằng cuối cùng T
    # m_ice*c_ice*15 + m_ice*Lf + m_ice*c_w*T = m_w*c_w*(45 - T)
    T_final = (m_w * c_w * T_w_init - Q_ice_needed) / ((m_w + m_ice) * c_w)
    results['Bridging_T_final'] = T_final
    assert abs(T_final - 34.83) < 0.1, "Lỗi nhiệt độ cuối cùng T_final của Bài tập cầu nối"

    # Tính độ biến thiên entropy của từng giai đoạn (dùng Kelvin)
    T_fin_K = T_final + T_freeze_K
    T_ice_init_K = T_ice_init + T_freeze_K
    T_w_init_K = T_w_init + T_freeze_K

    DS_ice_warm = m_ice * c_ice * math.log(T_freeze_K / T_ice_init_K)
    DS_ice_melt = m_ice * Lf_water / T_freeze_K
    DS_melted_warm = m_ice * c_w * math.log(T_fin_K / T_freeze_K)
    DS_ice_total = DS_ice_warm + DS_ice_melt + DS_melted_warm

    DS_water_cool = m_w * c_w * math.log(T_fin_K / T_w_init_K)
    DS_system_total = DS_ice_total + DS_water_cool

    results['Bridging_DS'] = {
        'ice_warm': DS_ice_warm,
        'ice_melt': DS_ice_melt,
        'melted_warm': DS_melted_warm,
        'ice_total': DS_ice_total,
        'water_cool': DS_water_cool,
        'system_total': DS_system_total
    }

    assert abs(DS_ice_warm - 5.93) < 0.1, "Lỗi entropy nâng nhiệt nước đá"
    assert abs(DS_ice_melt - 61.14) < 0.2, "Lỗi entropy nước đá tan"
    assert abs(DS_melted_warm - 25.14) < 0.2, "Lỗi entropy nước đá tan ấm lên"
    assert abs(DS_water_cool - (-81.69)) < 0.3, "Lỗi entropy nước ấm hạ nhiệt"
    assert abs(DS_system_total - 10.52) < 0.3, "Lỗi tổng entropy hệ cầu nối"
    assert DS_system_total > 0.0, "Tổng entropy hệ phải dương (quá trình bất thuận nghịch)"
    print("✓ Xác minh thành công Bài tập cầu nối (Bridging Problem).")


def verify_discussion_questions():
    """Xác minh 23 câu hỏi thảo luận về mặt nguyên lý nhiệt động lực học và tính đúng đắn sư phạm."""
    # Q20.1: Quá trình truyền nhiệt qua hiệu nhiệt độ hữu hạn giữa bếp và nước là bất thuận nghịch
    # Q20.2: Cơ học thuần túy: dao động điều hòa không ma sát là thuận nghịch; trượt có ma sát là bất thuận nghịch
    # Q20.3: Nhiệt lượng QH tỏa ra ở dàn nóng tủ lạnh bằng QC (rút từ khoang lạnh) cộng với công W của máy nén
    assert 346.0 + 230.0 == 576.0, "Định luật I cho máy lạnh: QH = QC + W"
    # Q20.4: Mở cửa tủ lạnh trong phòng kín: căn phòng nóng lên do W cơ điện chuyển thành nhiệt
    # Q20.5: Điều hòa cần dàn nóng đưa nhiệt ra ngoài cửa sổ; tủ lạnh xả nhiệt vào phòng vì mục tiêu là làm lạnh trong lòng tủ
    # Q20.6: Định luật II (Kelvin-Planck): Không thể biến 100% nhiệt thành công trong chu trình kín
    # Q20.7: Quỷ Maxwell (lọc phân tử nhanh/chậm) vi phạm phát biểu Clausius của Định luật II
    # Q20.8: Động cơ vĩnh cửu: ma sát và điện trở tiêu tán năng lượng, không thể tự chạy và cấp điện thừa
    # Q20.9: Vải ướt lạnh đi do bay hơi: entropy của hơi nước khuếch tán vào khí quyển tăng mạnh, tổng entropy vũ trụ tăng
    # Q20.10: Otto có 2 quá trình đẳng tích (cấp/thải nhiệt); Carnot có 2 quá trình đẳng nhiệt ở TH và TC
    # Q20.11: Hệ số làm lạnh K = TC/(TH - TC); hiệu nhiệt độ nhỏ làm độ chênh áp suất bão hòa nhỏ, tiêu tốn ít công
    # Q20.12: TH = TC => e = 0; TC = 0 K => e = 100% (không thể đạt được do Định luật III)
    # Q20.13: Động cơ không ma sát vẫn không đạt 100% vì giới hạn nhiệt động lực học e <= 1 - TC/TH
    # Q20.14: Phòng 20 C tiêu thụ nhiều điện hơn phòng 15 C do chênh lệch nhiệt độ lớn hơn làm tăng tải nhiệt và giảm K
    # Q20.15: K = QC/W = 346/230 = 1.50; không vi phạm bảo toàn năng lượng vì QH = QC + W = 576 J thải ra ngoài
    # Q20.16: Dẫn nhiệt: DS = Q(1/TC - 1/TH) > 0 vì TH > TC
    assert (1.0 / 290.0 - 1.0 / 350.0) > 0.0, "Truyền nhiệt tự phát qua hiệu nhiệt độ hữu hạn luôn làm tăng entropy"
    # Q20.17: Trộn nước, giãn tự do, truyền nhiệt, ma sát đều là quá trình bất thuận nghịch, tăng độ hỗn loạn vi mô (w) và tăng entropy
    # Q20.18: Giãn tự do là bất thuận nghịch, công thức tích phân dQ/T chỉ đúng cho đường đi thuận nghịch
    # Q20.19: Mặt trời (5800 K) và Trái Đất (290 K) không cân bằng; truyền nhiệt bức xạ tăng tổng entropy
    # Q20.20: Nhiệt tự truyền từ lạnh sang nóng không vi phạm Định luật I (nếu bảo toàn năng lượng) nhưng vi phạm Định luật II
    # Q20.21: Phim quay ngược: cơ học Newton bảo toàn năng lượng/động lượng; vi phạm Định luật II (cốc vỡ tự lành, mực tự thu)
    # Q20.22: Tiến hóa sinh học không vi phạm Định luật II vì Trái Đất và sinh vật là hệ mở nhận năng lượng chất lượng cao từ Mặt Trời
    # Q20.23: Cây lớn lên giảm entropy cục bộ nhưng tăng entropy môi trường; nguồn năng lượng tối hậu là quang năng Mặt Trời
    print("Đã kiểm tra hai quan hệ số học hỗ trợ phần thảo luận. Không xác nhận toàn bộ lời văn bằng phép thử này.")


def verify_image_assets():
    """Kiểm tra sự tồn tại của 4 tệp PNG cắt gốc và kiểm tra cạnh trắng không bị xén."""
    img_dir = ROOT / 'docs/vat-ly-1/bai-giang/img/young-20'
    crops = {
        'c-hinh-20-23.png': (774, 426),
        'c-hinh-20-06.png': (486, 588),
        'c-hinh-20-09.png': (1602, 753),
        'c-hinh-20-13.png': (1335, 798),
    }
    for filename, (expected_w, expected_h) in crops.items():
        p = img_dir / filename
        assert p.exists(), f"Thiếu tệp ảnh: {p}"
        im = Image.open(p)
        assert im.size == (expected_w, expected_h), f"Sai kích thước ảnh {filename}: {im.size} != {(expected_w, expected_h)}"
        arr = np.array(im)
        # Kiểm tra biên ngoài cùng (3 pixel) phải là màu trắng (không cắt lẹm vào nội dung)
        top = (arr[:3, :, :3] < 250).sum()
        bottom = (arr[-3:, :, :3] < 250).sum()
        left = (arr[:, :3, :3] < 250).sum()
        right = (arr[:, -3:, :3] < 250).sum()
        assert top == 0 and bottom == 0 and left == 0 and right == 0, f"Ảnh {filename} bị chạm biên!"
    print("✓ Xác minh thành công 4 tệp ảnh cắt gốc và tính toàn vẹn biên trắng.")


if __name__ == '__main__':
    print("Bắt đầu kiểm tra độc lập Chapter 20 Exercises C...")
    verify_guided_practice()
    verify_bridging_problem()
    verify_discussion_questions()
    verify_image_assets()
    print("==================================================")
    print("Các phép tính đã liệt kê và kiểm tra ảnh đã hoàn tất. Rà nội dung khái niệm và đọc biên ảnh thực hiện riêng.")
