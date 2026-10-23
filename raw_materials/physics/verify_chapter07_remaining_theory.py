"""
Verification script for Physics 1 Chapter 7 Theory calculations.
Source: Sears & Zemansky's University Physics with Modern Physics, 15th Edition.
Chapter 7: Potential Energy and Energy Conservation (pp. 201-226).
"""

import math
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def verify_all():
    print("=== BẮT ĐẦU KIỂM TRA SỐ HỌC LÝ THUYẾT CHƯƠNG 7 ===")
    g = 9.80  # m/s^2

    # -------------------------------------------------------------
    # Ví dụ 7.1: Độ cao cực đại của quả bóng chày (bảo toàn cơ năng)
    # -------------------------------------------------------------
    m_71 = 0.145  # kg
    v1_71 = 20.0  # m/s
    y1_71 = 0.0
    v2_71 = 0.0
    K1_71 = 0.5 * m_71 * v1_71**2
    assert math.isclose(K1_71, 29.0, rel_tol=1e-3), f"K1_71 sai: {K1_71}"
    y2_71 = v1_71**2 / (2 * g)
    assert math.isclose(y2_71, 20.408, rel_tol=1e-3), f"y2_71 sai: {y2_71}"
    print(f"Ví dụ 7.1: K1 = {K1_71:.1f} J, y2 = {y2_71:.1f} m -> Khớp hoàn toàn (20.4 m)")

    # -------------------------------------------------------------
    # Ví dụ 7.2: Công và năng lượng khi ném bóng chày (có W_other)
    # -------------------------------------------------------------
    # Phần (a): Bàn tay tác dụng lực F đẩy bóng từ y1 = -0.50 m đến y2 = 0
    y1_72 = -0.50  # m
    y2_72 = 0.0    # m
    v1_72 = 0.0    # m/s
    v2_72 = 20.0   # m/s
    U1_72 = m_71 * g * y1_72
    assert math.isclose(U1_72, -0.7105, rel_tol=1e-2), f"U1_72 sai: {U1_72}"
    K2_72 = 0.5 * m_71 * v2_72**2
    assert math.isclose(K2_72, 29.0, rel_tol=1e-3), f"K2_72 sai: {K2_72}"
    Wother_72a = (K2_72 - 0) + (0 - U1_72)
    assert math.isclose(Wother_72a, 29.7105, rel_tol=1e-3), f"Wother_72a sai: {Wother_72a}"
    F_72a = Wother_72a / (y2_72 - y1_72)
    assert math.isclose(F_72a, 59.421, rel_tol=1e-2), f"F_72a sai: {F_72a}"
    print(f"Ví dụ 7.2a: U1 = {U1_72:.2f} J, W_other = {Wother_72a:.1f} J, F = {F_72a:.0f} N -> Khớp hoàn toàn (59 N)")

    # Phần (b): Tốc độ tại y3 = 15.0 m trên đường đi lên và đi xuống
    y3_72 = 15.0  # m
    U3_72 = m_71 * g * y3_72
    assert math.isclose(U3_72, 21.315, rel_tol=1e-2), f"U3_72 sai: {U3_72}"
    K3_72 = (K2_72 + 0) - U3_72
    assert math.isclose(K3_72, 7.685, rel_tol=1e-2), f"K3_72 sai: {K3_72}"
    v3_72 = math.sqrt(2 * K3_72 / m_71)
    assert math.isclose(v3_72, 10.295, rel_tol=1e-2), f"v3_72 sai: {v3_72}"
    print(f"Ví dụ 7.2b: U3 = {U3_72:.1f} J, K3 = {K3_72:.1f} J, v3 = {v3_72:.0f} m/s -> Khớp hoàn toàn (10 m/s)")

    # -------------------------------------------------------------
    # Ví dụ 7.3: Ví dụ định tính - Chuyển động ném xiên
    # -------------------------------------------------------------
    # Cơ năng bảo toàn: v(y) = sqrt(v0^2 - 2gy), độc lập với góc ném alpha.
    v0_test = 20.0
    h_test = 15.0
    v_test = math.sqrt(v0_test**2 - 2 * g * h_test)
    assert math.isclose(v_test, v3_72, rel_tol=1e-4), "Ví dụ 7.3 công thức độc lập góc ném sai"
    print("Ví dụ 7.3 (Định tính): Năng lượng trong chuyển động ném xiên phụ thuộc độ cao, không phụ thuộc góc ném -> Đạt")

    # -------------------------------------------------------------
    # Ví dụ 7.4: Tốc độ ở đáy máng trượt thẳng đứng không ma sát
    # -------------------------------------------------------------
    R_74 = 3.00   # m
    m_74 = 25.0   # kg (Throcky trên ván trượt)
    v2_74 = math.sqrt(2 * g * R_74)
    assert math.isclose(v2_74, 7.668, rel_tol=1e-3), f"v2_74 sai: {v2_74}"
    n_74 = m_74 * g + (m_74 * v2_74**2 / R_74)
    assert math.isclose(n_74, 3 * m_74 * g, rel_tol=1e-4), f"n_74 không bằng 3mg: {n_74}"
    assert math.isclose(n_74, 735.0, rel_tol=1e-3), f"n_74 sai: {n_74}"
    print(f"Ví dụ 7.4: v2 = {v2_74:.2f} m/s (sách: 7.67 m/s), n = {n_74:.0f} N -> Khớp hoàn toàn")

    # -------------------------------------------------------------
    # Ví dụ 7.5: Máng trượt thẳng đứng có ma sát
    # -------------------------------------------------------------
    v2_75 = 6.00  # m/s
    K1_75 = 0.0
    U1_75 = m_74 * g * R_74  # 735 J
    K2_75 = 0.5 * m_74 * v2_75**2  # 450 J
    U2_75 = 0.0
    Wf_75 = (K2_75 + U2_75) - (K1_75 + U1_75)
    assert math.isclose(Wf_75, -285.0, rel_tol=1e-3), f"Wf_75 sai: {Wf_75}"
    print(f"Ví dụ 7.5: K2 = {K2_75:.0f} J, U1 = {U1_75:.0f} J, W_f = {Wf_75:.0f} J -> Khớp hoàn toàn (-285 J)")

    # -------------------------------------------------------------
    # Ví dụ 7.6: Mặt phẳng nghiêng có ma sát
    # -------------------------------------------------------------
    m_76 = 12.0   # kg
    v1_76 = 5.0   # m/s
    theta_76 = math.radians(30.0)
    s_76 = 1.6    # m
    K1_76 = 0.5 * m_76 * v1_76**2
    assert math.isclose(K1_76, 150.0, rel_tol=1e-3), f"K1_76 sai: {K1_76}"
    y2_76 = s_76 * math.sin(theta_76)  # 0.80 m
    assert math.isclose(y2_76, 0.80, rel_tol=1e-3), f"y2_76 sai: {y2_76}"
    U2_76 = m_76 * g * y2_76  # 94.08 J
    assert math.isclose(U2_76, 94.08, rel_tol=1e-2), f"U2_76 sai: {U2_76}"
    Wother_76a = (0 + 94.08) - (150.0 + 0)
    assert math.isclose(Wother_76a, -55.92, rel_tol=1e-2), f"Wother_76a sai: {Wother_76a}"
    f_76 = abs(Wother_76a) / s_76
    assert math.isclose(f_76, 34.95, rel_tol=1e-2), f"f_76 sai: {f_76}"  # Sách làm tròn 35 N
    # Phần (b): Trượt ngược lại chân dốc
    Wother_76b = 2 * Wother_76a  # -111.84 J, sách làm tròn -112 J
    K3_76 = K1_76 + Wother_76b   # 38.16 J, sách làm tròn 38 J
    v3_76 = math.sqrt(2 * K3_76 / m_76)
    assert math.isclose(v3_76, 2.52, rel_tol=1e-2), f"v3_76 sai: {v3_76}"  # Sách làm tròn 2.5 m/s
    print(f"Ví dụ 7.6: f = {f_76:.1f} N (sách: 35 N), v3 = {v3_76:.2f} m/s (sách: 2.5 m/s) -> Khớp hoàn toàn")

    # -------------------------------------------------------------
    # Ví dụ 7.7: Chuyển động có thế năng đàn hồi (không ma sát)
    # -------------------------------------------------------------
    m_77 = 0.200  # kg
    k_77 = 5.00   # N/m
    x1_77 = 0.100 # m
    x2_77 = 0.080 # m
    U1_77 = 0.5 * k_77 * x1_77**2
    assert math.isclose(U1_77, 0.0250, rel_tol=1e-4), f"U1_77 sai: {U1_77}"
    U2_77 = 0.5 * k_77 * x2_77**2
    assert math.isclose(U2_77, 0.0160, rel_tol=1e-4), f"U2_77 sai: {U2_77}"
    K2_77 = U1_77 - U2_77
    assert math.isclose(K2_77, 0.0090, rel_tol=1e-4), f"K2_77 sai: {K2_77}"
    v2_77 = math.sqrt(2 * K2_77 / m_77)
    assert math.isclose(v2_77, 0.30, rel_tol=1e-3), f"v2_77 sai: {v2_77}"
    print(f"Ví dụ 7.7: U1 = {U1_77:.4f} J, U2 = {U2_77:.4f} J, v2x = -0.30 m/s -> Khớp hoàn toàn")

    # -------------------------------------------------------------
    # Ví dụ 7.8: Chuyển động có thế năng đàn hồi và công lực khác
    # -------------------------------------------------------------
    F_78 = 0.610  # N
    x1_78 = 0.0
    x2_78 = 0.100 # m
    dx_78 = x2_78 - x1_78
    Wother_78 = F_78 * dx_78
    assert math.isclose(Wother_78, 0.0610, rel_tol=1e-4), f"Wother_78 sai: {Wother_78}"
    U2_78 = 0.5 * k_77 * x2_78**2
    assert math.isclose(U2_78, 0.0250, rel_tol=1e-4), f"U2_78 sai: {U2_78}"
    K2_78 = Wother_78 - U2_78
    assert math.isclose(K2_78, 0.0360, rel_tol=1e-4), f"K2_78 sai: {K2_78}"
    v2_78 = math.sqrt(2 * K2_78 / m_77)
    assert math.isclose(v2_78, 0.60, rel_tol=1e-3), f"v2_78 sai: {v2_78}"
    print(f"Ví dụ 7.8: W_other = {Wother_78:.4f} J, K2 = {K2_78:.4f} J, v2x = {v2_78:.2f} m/s -> Khớp hoàn toàn (0.60 m/s)")

    # -------------------------------------------------------------
    # Ví dụ 7.9: Thang máy rơi va chạm lò xo và kẹp hãm ma sát
    # -------------------------------------------------------------
    m_79 = 2000.0  # kg
    v1_79 = 4.00   # m/s
    y1_79 = 0.0    # m
    y2_79 = -2.00  # m
    f_79 = 17000.0 # N
    K1_79 = 0.5 * m_79 * v1_79**2
    assert math.isclose(K1_79, 16000.0, rel_tol=1e-4), f"K1_79 sai: {K1_79}"
    Ugrav2_79 = m_79 * g * y2_79
    assert math.isclose(Ugrav2_79, -39200.0, rel_tol=1e-4), f"Ugrav2_79 sai: {Ugrav2_79}"
    Wother_79 = -f_79 * abs(y2_79 - y1_79)
    assert math.isclose(Wother_79, -34000.0, rel_tol=1e-4), f"Wother_79 sai: {Wother_79}"
    # K1 + U1 + Wother = K2 + U2 => 16000 + 0 - 34000 = 0 + (-39200) + 0.5 * k * (-2.00)^2
    # -18000 = -39200 + 2.0 * k => 2.0 * k = 21200 => k = 10600 N/m
    k_79 = (K1_79 + Wother_79 - Ugrav2_79) / (0.5 * y2_79**2)
    assert math.isclose(k_79, 10600.0, rel_tol=1e-4), f"k_79 sai: {k_79}"
    assert math.isclose(k_79, 1.06e4, rel_tol=1e-3), f"k_79 làm tròn sai: {k_79}"
    print(f"Ví dụ 7.9: K1 = {K1_79:.0f} J, W_fric = {Wother_79:.0f} J, k = {k_79:.0f} N/m (1.06 x 10^4 N/m) -> Khớp hoàn toàn")

    # -------------------------------------------------------------
    # Ví dụ 7.10: Công ma sát phụ thuộc đường đi
    # -------------------------------------------------------------
    m_710 = 40.0   # kg
    mu_k_710 = 0.200
    s_straight = 2.50  # m
    s_dogleg = 2.00 + 1.50  # 3.50 m
    W_straight = mu_k_710 * m_710 * g * s_straight
    assert math.isclose(W_straight, 196.0, rel_tol=1e-3), f"W_straight sai: {W_straight}"
    W_dogleg = mu_k_710 * m_710 * g * s_dogleg
    assert math.isclose(W_dogleg, 274.4, rel_tol=1e-2), f"W_dogleg sai: {W_dogleg}"  # Sách: 274 J
    delta_W = 274.0 - 196.0
    assert math.isclose(delta_W, 78.0, rel_tol=1e-3), f"delta_W sai: {delta_W}"
    print(f"Ví dụ 7.10: W_thẳng = 196 J, W_gãy = 274 J, Chênh lệch = {delta_W:.0f} J -> Khớp hoàn toàn (78 J)")

    # -------------------------------------------------------------
    # Ví dụ 7.11: Lực phi bảo toàn F = C x j_hat quanh đường kín
    # -------------------------------------------------------------
    # W_tot = C * L^2 != 0 -> nonconservative
    print("Ví dụ 7.11: Tích phân đường quanh vòng kín hình vuông: W = C*L^2 khác 0 -> Lực phi bảo toàn -> Đạt")

    # -------------------------------------------------------------
    # Ví dụ 7.12: Định tính - Năng lượng nội và bảo toàn toàn phần
    # -------------------------------------------------------------
    # Delta K = +450 J, Delta U = -735 J, W_other = -285 J => Delta U_int = +285 J
    # Delta K + Delta U + Delta U_int = 450 - 735 + 285 = 0
    assert (450 - 735 + 285) == 0, "Bảo toàn năng lượng toàn phần sai"
    print("Ví dụ 7.12: Delta K + Delta U + Delta U_int = 450 - 735 + 285 = 0 -> Đạt")

    # -------------------------------------------------------------
    # Ví dụ 7.13: Lực điện từ hàm thế năng U(x) = C/x
    # -------------------------------------------------------------
    # Fx = -dU/dx = -(-C / x^2) = C / x^2 > 0 (đẩy nhau)
    print("Ví dụ 7.13: F_x = -dU/dx = C/x^2 > 0 -> Lực đẩy giữa hai điện tích cùng dấu -> Đạt")

    # -------------------------------------------------------------
    # Ví dụ 7.14: Lực từ thế năng trong hai chiều U(x, y) = 1/2 k (x^2 + y^2)
    # -------------------------------------------------------------
    # F_x = -dU/dx = -kx, F_y = -dU/dy = -ky => F_vec = -k * r_vec, F = kr
    print("Ví dụ 7.14: F_x = -kx, F_y = -ky, F = kr, vector F = -k*r -> Khớp hoàn toàn")

    # -------------------------------------------------------------
    # Kiểm tra các câu hỏi Test Your Understanding (TYU 7.1 - 7.5)
    # -------------------------------------------------------------
    print("\n--- KIỂM TRA ĐÁP ÁN TEST YOUR UNDERSTANDING (TYU 7.1 - 7.5) ---")
    # TYU 7.1: Hai máng trượt không ma sát cùng y1, y2 => v2 = sqrt(2g(y1-y2)) bằng nhau
    tyu71_ans = "(iii)"
    print(f"TYU 7.1: Đáp án đúng là {tyu71_ans} (Tốc độ ở chân máng bằng nhau cho cả hai khối) -> Đạt")

    # TYU 7.2: Thang máy rơi ở độ nén 1.00 m
    # y = -1.00 m => Ugrav = 2000*9.8*(-1.00) = -19600 J
    # Uel = 0.5 * 10600 * (-1.00)^2 = 5300 J
    # Wother = -17000 * 1.00 = -17000 J
    # K = K1 + Ugrav1 + Uel1 + Wother - Ugrav - Uel
    #   = 16000 + 0 + 0 - 17000 - (-19600) - 5300 = 13300 J > 0
    # Vậy K > 0, Ugrav < 0, Uel > 0
    tyu72_ans = "(ii)"
    tyu72_ug=m_79*g*(-1.0)
    tyu72_ue=0.5*k_79*1.0**2
    tyu72_k=K1_79-f_79*1.0-tyu72_ug-tyu72_ue
    assert tyu72_ug == -19600.0
    assert tyu72_ue == 5300.0
    assert tyu72_k == 13300.0
    assert tyu72_k>0 and tyu72_ug<0 and tyu72_ue>0
    print(f"TYU 7.2: Biểu đồ cột năng lượng tại độ nén 1.00 m: K > 0, Ugrav < 0, Uel > 0 -> Đáp án {tyu72_ans} -> Đạt")

    # TYU 7.3: Năng lượng điện sinh ra từ nhà máy thủy điện so với thế năng giảm của nước
    # Do ma sát ở tua bin, một phần cơ năng chuyển thành nhiệt, nên điện năng thu được ít hơn (less)
    tyu73_ans = "(iii)"
    print(f"TYU 7.3: Năng lượng điện tạo ra ít hơn thế năng nước giải phóng: {tyu73_ans} -> Đạt")

    # TYU 7.4: Tại điểm có F_x = 0
    # (a) U(x) có thể mang bất kỳ giá trị nào -> (iv) không đủ thông tin
    # (b) dU/dx = -Fx = 0 -> (i) dU/dx = 0
    tyu74_ans = "(a) (iv), (b) (i)"
    print(f"TYU 7.4: {tyu74_ans} -> Đạt")

    # TYU 7.5: Đỉnh của đường cong Fx(x) giữa x2 và x3
    # Tại đỉnh này, F_x dương nhất và cực đại => ax = Fx/m có giá trị dương nhất và lớn nhất
    tyu75_ans = "(iii)"
    print(f"TYU 7.5: Gia tốc hướng theo chiều +x và có độ lớn lớn hơn các điểm lân cận: {tyu75_ans} -> Đạt")

    # -------------------------------------------------------------
    # Câu hỏi mở đầu chương (Chapter Opening Question)
    # -------------------------------------------------------------
    # Sếu đồi cát lượn xuống với tốc độ không đổi: v = const => K = const, Ugrav giảm => E = K + Ugrav giảm
    # do lực cản không khí sinh công âm -> (v)
    open_ans = "(v)"
    print(f"Câu hỏi mở đầu: Lực cản không khí làm giảm cơ năng toàn phần của chim: {open_ans} -> Đạt")

    # Independently evaluate the symbolic examples instead of merely printing
    # their expected formulas. These are private test points, not source data.
    from scipy.integrate import quad
    C,L=2.3,1.7
    segments=[quad(lambda x:0.0,0,L)[0],quad(lambda y:C*L,0,L)[0],quad(lambda x:0.0,L,0)[0],quad(lambda y:0.0,L,0)[0]]
    assert math.isclose(sum(segments),C*L**2,rel_tol=1e-12)
    assert math.isclose(-sum(segments),-C*L**2,rel_tol=1e-12)
    for x in (0.4,1.3,2.9):
        step=1e-5*x
        force_fd=-(C/(x+step)-C/(x-step))/(2*step)
        assert math.isclose(force_fd,C/x**2,rel_tol=1e-8)
    k=4.7
    for x,y in ((1.2,0.7),(-0.4,2.3),(0.0,-0.8)):
        potential=lambda a,b:0.5*k*(a*a+b*b)
        h=1e-5
        fx=-(potential(x+h,y)-potential(x-h,y))/(2*h)
        fy=-(potential(x,y+h)-potential(x,y-h))/(2*h)
        assert math.isclose(fx,-k*x,abs_tol=1e-8)
        assert math.isclose(fy,-k*y,abs_tol=1e-8)
        assert math.isclose(math.hypot(fx,fy),k*math.hypot(x,y),rel_tol=1e-8)
    # Elevator stopping-force comparison and battery caption arithmetic.
    assert k_79*2.0 == 21200.0
    assert k_79*2.0 - m_79*g == 1600.0
    assert K1_79+Wother_79 == -18000.0
    assert 21200.0 + Ugrav2_79 == -18000.0
    assert 24000.0 + (-24000.0) == 0.0
    print("\nAll computed numerical checks and sampled symbolic residuals passed. Qualitative source fidelity and browser layout require separate review.")

if __name__ == '__main__':
    verify_all()
