# Báo Cáo Thẩm Định Độc Lập Bài Tập 20.32–20.62 (Vật Lý 1 — Chương 20)

- **Ngày thực hiện**: 2026-10-23
- **Đối tượng rà soát**: Toàn bộ 31 bài tập từ 20.32 đến 20.62 trong tệp `raw_materials/physics/translations/chapter-20/12-bai-tap-032-062.md`
- **Tài liệu nguồn chuẩn đối sánh**: Giáo trình *Young & Freedman: University Physics with Modern Physics* (15th Edition), tệp `raw_materials/physics/source/young-freedman-15.pdf`, các trang PDF 693–696 (trang in 674–677).
- **Phạm vi tác vụ**: Thẩm định vật lý và nguồn độc lập theo kế hoạch `docs/agy-plans/2026-10-23-physics1-ch20-parent-e-review.md`. Không thực hiện sửa đổi các tệp ngoài phạm vi sở hữu được phân công. Tệp duy nhất được tạo/sửa: `raw_materials/physics/reviews/physics1-ch20-parent-e-review-20261023.md`.

---

## 1. Tóm Tắt Kết Quả Thẩm Định (Executive Summary)

Quá trình rà soát độc lập toàn diện từng ý, từng dữ kiện số học và lập luận vật lý của 31 bài tập (từ 20.32 đến 20.62) đối chiếu trực tiếp với văn bản PDF gốc cho thấy:
- **Số bài ĐẠT (PASS)**: 30 bài (20.32, 20.33, 20.34, 20.35, 20.36, 20.37, 20.38, 20.39, 20.40, 20.41, 20.42, 20.43, 20.45, 20.46, 20.47, 20.48, 20.49, 20.50, 20.51, 20.52, 20.53, 20.54, 20.55, 20.56, 20.57, 20.58, 20.59, 20.60, 20.61, 20.62).
- **Số bài KHÔNG ĐẠT (FAIL)**: 01 bài (Bài 20.44).
- **Số bài CHƯA XÁC ĐỊNH (UNCERTAIN)**: 0 bài (toàn bộ 31 bài đã được kiểm tra chi tiết 100%).
- *Lưu ý*: Tuân thủ nghiêm ngặt yêu cầu không tính toán hay công bố tỷ lệ phần trăm độ chính xác tổng hợp; không chấp nhận mã kiểm thử có sẵn làm bằng chứng độc lập.

---

## 2. Phân Tích Chuyên Sâu Các Trọng Điểm Vật Lý & Khái Niệm

### 2.1. Bài 20.42: Hiện tượng đổi dấu nhiệt lượng trên nhánh tuyến tính $c \to a$ và phân biệt nhiệt hấp thụ thực
- **Bối cảnh đề bài**: Chu trình tam giác của khí lý tưởng đơn nguyên tử ($C_V = \frac{3}{2}R, C_p = \frac{5}{2}R$):
  - $a \to b$: Nở đẳng áp ở $p_a = 3{,}00 \times 10^5\,\mathrm{Pa}$, thể tích từ $0{,}500\,\mathrm{m^3}$ đến $0{,}800\,\mathrm{m^3}$.
  - $b \to c$: Hạ áp đẳng tích ở $V_b = 0{,}800\,\mathrm{m^3}$, áp suất từ $3{,}00 \times 10^5\,\mathrm{Pa}$ xuống $1{,}00 \times 10^5\,\mathrm{Pa}$.
  - $c \to a$: Đoạn thẳng tuyến tính trong giản đồ $p$-$V$ đưa hệ từ $(0{,}800\,\mathrm{m^3}, 1{,}00 \times 10^5\,\mathrm{Pa})$ về lại $(0{,}500\,\mathrm{m^3}, 3{,}00 \times 10^5\,\mathrm{Pa})$.
- **Phân tích toán - nhiệt động học dọc theo đoạn $c \to a$**:
  Phương trình đường thẳng $c \to a$ có dạng:
  $$p(V) = p_c + \frac{p_a - p_c}{V_a - V_c}(V - V_c) = 10^5 - \frac{2 \times 10^5}{0{,}3}(V - 0{,}8) = \frac{19}{3} \times 10^5 - \frac{2}{3} \times 10^6 V$$
  Hệ số góc $\frac{dp}{dV} = -\frac{2}{3} \times 10^6\,\mathrm{Pa/m^3}$.
  Nhiệt lượng vi phân đối với khí đơn nguyên tử là:
  $$dQ = dU + dW = \frac{3}{2}(p\,dV + V\,dp) + p\,dV = \frac{5}{2}p\,dV + \frac{3}{2}V\,dp = \left[ \frac{5}{2}p(V) + \frac{3}{2}V \frac{dp}{dV} \right] dV$$
  Xét hệ số $\frac{dQ}{dV}$:
  $$\frac{dQ}{dV} = \frac{5}{2}\left( \frac{19}{3} \times 10^5 - \frac{2}{3} \times 10^6 V \right) + \frac{3}{2}V\left( -\frac{2}{3} \times 10^6 \right) = \frac{95}{6} \times 10^5 - \frac{8}{3} \times 10^6 V$$
  Hệ số này triệt tiêu tại thể tích tới hạn:
  $$V_* = \frac{95 \times 10^5}{6} \times \frac{3}{8 \times 10^6} = \frac{95}{160} = 0{,}59375\,\mathrm{m^3}$$
  Áp suất tương ứng tại điểm này là:
  $$p_* = 10^5 - \frac{2}{3} \times 10^6 (0{,}59375 - 0{,}8) = 2{,}375 \times 10^5\,\mathrm{Pa}$$
- **Ý nghĩa đổi dấu nhiệt lượng**:
  Vì chiều biến đổi đi từ $c$ về $a$, thể tích giảm ($dV < 0$):
  - Khi $V$ giảm từ $0{,}800\,\mathrm{m^3}$ về $V_* = 0{,}59375\,\mathrm{m^3}$: Tại đây $V > V_* \implies \frac{dQ}{dV} < 0$, kết hợp với $dV < 0$ cho $dQ > 0$ (khí hấp thụ nhiệt lượng).
    $$Q_{c \to *} = \int_{0{,}8}^{0{,}59375} \left( \frac{5}{2}p + \frac{3}{2}V \frac{dp}{dV} \right) dV = +56718{,}75\,\mathrm J \approx +56{,}72\,\mathrm{kJ}$$
  - Khi $V$ tiếp tục giảm từ $V_* = 0{,}59375\,\mathrm{m^3}$ về $0{,}500\,\mathrm{m^3}$: Tại đây $V < V_* \implies \frac{dQ}{dV} > 0$, kết hợp với $dV < 0$ cho $dQ < 0$ (khí tỏa nhiệt lượng).
    $$Q_{* \to a} = \int_{0{,}59375}^{0{,}5} \left( \frac{5}{2}p + \frac{3}{2}V \frac{dp}{dV} \right) dV = -11718{,}75\,\mathrm J \approx -11{,}72\,\mathrm{kJ}$$
  - Nhiệt ròng của toàn bộ nhánh $c \to a$ là:
    $$Q_{ca,\mathrm{net}} = Q_{c \to *} + Q_{* \to a} = 56718{,}75 - 11718{,}75 = +45000\,\mathrm J = +45{,}0\,\mathrm{kJ}$$
- **Đối chiếu với văn bản bài soạn**:
  Văn bản bài soạn trong `12-bai-tap-032-062.md` đã nhận diện chính xác hiện tượng đổi dấu nhiệt lượng nội tại của nhánh $c \to a$, tính đúng điểm $V_* = 0{,}5938\,\mathrm{m^3}$, tách bạch rõ ràng giữa:
  1. Cách tính kinh điển xem xét gộp theo nhánh: Mẫu số nhiệt hấp thụ là $Q_H = Q_{ab} + Q_{ca,\mathrm{net}} = 225\,\mathrm{kJ} + 45\,\mathrm{kJ} = 270\,\mathrm{kJ}$, cho $\eta = \frac{30}{270} = 11{,}1\%$.
  2. Cách tính nhiệt động học thực tế (nhiệt nhận thực sự): $Q_{H,\mathrm{thực}} = Q_{ab} + Q_{c \to *} = 225\,\mathrm{kJ} + 56{,}72\,\mathrm{kJ} = 281{,}72\,\mathrm{kJ}$, cho $\eta_{\mathrm{thực}} = \frac{30}{281{,}72} = 10{,}65\%$.
  Lập luận và số học hoàn toàn chuẩn xác.

---

### 2.2. Bài 20.49: Ranh giới hệ số làm lạnh (COP) — Chu trình đa nhiệt độ so với nguồn lạnh đơn
- **Bối cảnh đề bài**: Chu trình máy lạnh chạy bằng $0{,}850\,\mathrm{mol}\,\mathrm{H_2}$ (khí hai nguyên tử, $C_V = \frac{5}{2}R$):
  - $a \to b$: Nở đẳng nhiệt ở $T_a$ từ $(0{,}0300\,\mathrm{m^3}, 0{,}700\,\mathrm{atm})$ tới $V_b = 0{,}100\,\mathrm{m^3}$, $p_b = 0{,}210\,\mathrm{atm}$, $T_a = T_b = 301{,}1\,\mathrm K$.
  - $b \to c$: Tăng áp đẳng tích ở $V = 0{,}100\,\mathrm{m^3}$ từ $0{,}210\,\mathrm{atm}$ lên $p_c = 0{,}700\,\mathrm{atm}$, nhiệt độ tăng vọt lên $T_c = 1003{,}6\,\mathrm K \approx 1004\,\mathrm K$.
  - $c \to a$: Nén đẳng áp ở $p = 0{,}700\,\mathrm{atm}$ từ $0{,}100\,\mathrm{m^3}$ về $0{,}0300\,\mathrm{m^3}$, hạ nhiệt từ $1004\,\mathrm K$ về $301{,}1\,\mathrm K$.
- **Cân bằng năng lượng**:
  - $W_{ab} = Q_{ab} = nRT_a \ln(V_b/V_a) = +2561{,}8\,\mathrm J$.
  - $W_{bc} = 0$, $Q_{bc} = \Delta U_{bc} = \frac{5}{2}V_b(p_c - p_b) = +12412{,}3\,\mathrm J$.
  - $W_{ca} = p_a(V_a - V_c) = -4964{,}9\,\mathrm J$, $\Delta U_{ca} = -12412{,}3\,\mathrm J$, $Q_{ca} = -17377{,}2\,\mathrm J$.
  - Công ròng chu trình nhận vào: $|W_{\mathrm{net}}| = |2561{,}8 + 0 - 4964{,}9| = 2403{,}1\,\mathrm J$.
- **Phân tích ranh giới hệ nhiệt động**:
  - Trong cách hiểu quy ước của bài tập sách giáo khoa (tổng nhiệt lượng môi chất nhận vào được gộp thành tải lạnh):
    $$Q_{\mathrm{in, total}} = Q_{ab} + Q_{bc} = 2561{,}8 + 12412{,}3 = 14974{,}1\,\mathrm J \implies K = \frac{14974{,}1}{2403{,}1} = 6{,}231$$
  - Trong thực tế nhiệt động học kỹ thuật của tủ lạnh: Nhánh $bc$ tăng nhiệt độ từ $301\,\mathrm K$ lên tận $1004\,\mathrm K$. Nhiệt nhận ở nhiệt độ cao hơn nhiều so với môi trường không thể là nhiệt lấy từ buồng lạnh cần bảo quản! Nếu chỉ xét tải làm lạnh đẳng nhiệt thực thụ lấy từ nguồn lạnh ở nhánh $ab$:
    $$K_{\mathrm{iso}} = \frac{Q_{ab}}{|W_{\mathrm{net}}|} = \frac{2561{,}8}{2403{,}1} = 1{,}066$$
  Bài soạn đã trình bày tường minh cả hai góc nhìn, chỉ rõ sự khác biệt giữa quy ước gộp nhánh của sách giáo trình và ranh giới vật lý thực tế của ngăn lạnh.

---

### 2.3. Bài 20.52: Điện trở đốt nóng thực tế ở trạng thái dừng so với nguồn nhiệt lý tưởng
- **Bối cảnh đề bài**: Đun $250\,\mathrm{cm^3}$ nước ($0{,}250\,\mathrm{kg}$, $c_w = 4190\,\mathrm{J/(kg\cdot K)}$) từ $20^\circ\mathrm C$ ($293{,}15\,\mathrm K$) lên $78^\circ\mathrm C$ ($351{,}15\,\mathrm K$) bằng dây điện trở giữ không đổi ở $120^\circ\mathrm C$ ($393{,}15\,\mathrm K$).
- **Nhiệt lượng truyền**:
  $$Q = mc_w(78 - 20) = 0{,}250 \times 4190 \times 58 = 60755\,\mathrm J$$
- **Biến thiên entropy của nước**:
  $$\Delta S_w = mc_w \ln\left(\frac{351{,}15}{293{,}15}\right) = 0{,}250 \times 4190 \times 0{,}180536 = +189{,}11\,\mathrm{J/K}$$
- **Bản chất của phần cấp nhiệt (Điện trở vs Nguồn nhiệt lý tưởng)**:
  1. *Nếu xem dây đốt là một nguồn nhiệt lý tưởng (Ideal Heat Reservoir)* ở nhiệt độ không đổi $T_H = 393{,}15\,\mathrm K$:
     Nguồn mất nhiệt lượng $Q$, entropy biến thiên:
     $$\Delta S_H = -\frac{Q}{T_H} = -\frac{60755}{393{,}15} = -154{,}53\,\mathrm{J/K}$$
     Tổng biến thiên entropy của hệ (nước + nguồn nhiệt):
     $$\Delta S_{\mathrm{hệ}} = 189{,}11 - 154{,}53 = +34{,}58\,\mathrm{J/K} > 0$$
  2. *Nếu xem xét điện trở thực tế được nuôi bởi nguồn điện (Real Electrically Powered Resistor)*:
     Dây điện trở hoạt động ở trạng thái dừng (steady state): Nhiệt độ, cấu trúc mạng tinh thể, nội năng và các hàm trạng thái của bản thân điện trở không hề thay đổi giữa thời điểm đầu và cuối quá trình. Vì entropy $S$ là một hàm trạng thái (state function):
     $$\Delta S_{\mathrm{điện\ trở}} = S_{\mathrm{cuối}} - S_{\mathrm{đầu}} = 0$$
     Trong lòng điện trở, công điện chất lượng cao biến thành nhiệt tỏa ra, sinh ra dòng entropy với tốc độ $\frac{\dot Q}{T_H}$. Lượng entropy này lập tức được truyền ra ngoài theo dòng nhiệt mà không tích lũy trong điện trở.
     Nếu hệ cô lập bao gồm: Nguồn điện ngoài (không đổi entropy vì cấp công thuần túy) + điện trở dừng + cốc nước, tổng entropy sinh ra trong vũ trụ là:
     $$\Delta S_{\mathrm{vũ\ trụ}} = \Delta S_w + 0 + 0 = +189{,}11\,\mathrm{J/K}$$
  Bài soạn đã phân biệt xuất sắc giữa mô hình sách giáo khoa (nguồn nhiệt lý tưởng nhận định lượng $-154{,}5\,\mathrm{J/K}$) và nguyên lý hàm trạng thái của điện trở thực ($\Delta S = 0$).

---

### 2.4. Bài 20.58: Sự mâu thuẫn dữ kiện số học trong chu trình Diesel ($r = 21{,}0, T_a = 300\,\mathrm K, T_c = 950\,\mathrm K$)
- **Mô hình chu trình Diesel**:
  - $a \to b$: Nén đoạn nhiệt từ $V_a$ đến $V_b = V_a / r$. Nhiệt độ sau nén:
    $$T_b = T_a r^{\gamma - 1}$$
  - $b \to c$: Đốt cháy cấp nhiệt đẳng áp ở $p_b = p_c$, thể tích dãn từ $V_b$ đến $V_c$. Tỷ số cắt (cutoff ratio) là $\rho = \frac{V_c}{V_b} = \frac{T_c}{T_b}$.
  - Nhiệt cấp vào hệ trong quá trình cháy đẳng áp:
    $$Q_H = n C_p (T_c - T_b)$$
- **Kiểm tra dữ kiện bài toán**:
  - Đề bài cho $T_a = 300\,\mathrm K$, $\gamma = 1{,}40$, $r = 21{,}0$.
  - Tính nhiệt độ $T_b$ ở cuối quá trình nén đoạn nhiệt:
    $$T_b = 300 \times 21{,}0^{0{,}40} = 300 \times 3{,}37976 = 1013{,}93\,\mathrm K \approx 1014\,\mathrm K$$
  - Đề bài lại cho nhiệt độ tại $c$ là $T_c = 950\,\mathrm K$!
- **Mâu thuẫn vật lý nghiêm trọng**:
  - Vì $T_c = 950\,\mathrm K < T_b = 1014\,\mathrm K$, tỷ số cắt $\rho = \frac{950}{1014} = 0{,}9369 < 1$.
  - Thể tích tại $c$ nhỏ hơn thể tích tại $b$ ($V_c < V_b$), và nhiệt lượng trao đổi ở nhánh đẳng áp mang dấu âm ($Q_{bc} = n C_p (950 - 1014) < 0$): Khí bị làm nguội và nén thêm thay vì giãn nở sinh công do cháy nhiên liệu!
  - Nếu thay máy móc $\rho = 0{,}9369$ vào công thức đại số kinh điển của hiệu suất Diesel:
    $$\eta_{\mathrm{hình\ thức}} = 1 - \frac{1}{r^{\gamma-1}} \left[ \frac{\rho^\gamma - 1}{\gamma(\rho - 1)} \right] = 1 - \frac{1}{3{,}37976} \times \frac{0{,}9369^{1{,}4} - 1}{1{,}4(0{,}9369 - 1)} \approx 70{,}79\%$$
  - Giá trị $70{,}79\%$ này hoàn toàn phi vật lý vì tiền đề cấp nhiệt dương của động cơ nhiệt bị vi phạm.
  - Điều kiện để chu trình Diesel nhận nhiệt ($T_c > T_b$) với $T_a = 300\,\mathrm K, T_c = 950\,\mathrm K$ là:
    $$r < \left(\frac{T_c}{T_a}\right)^{\frac{1}{\gamma - 1}} = \left(\frac{950}{300}\right)^{2{,}5} \approx 17{,}84$$
  Việc bài soạn vạch rõ mâu thuẫn dữ kiện này và cảnh báo không được thừa nhận con số $70{,}79\%$ làm hiệu suất hợp lệ là một phát hiện chuẩn mực về mặt khoa học.

---

### 2.5. Bài 20.44: Thâm hụt dữ liệu nguồn nghiêm trọng (FAIL) và Giá trị hiệu chỉnh
- **Sai lệch trong bài soạn**:
  Trong văn bản bài soạn (`12-bai-tap-032-062.md`, dòng 348–375), người soạn đã tự ý đảo lộn dữ kiện và câu hỏi:
  - Tự đặt nhiệt độ nước sông tăng từ $18{,}0^\circ\mathrm C$ lên $18{,}5^\circ\mathrm C$ và yêu cầu tính lưu lượng sông (thu được $716\,\mathrm{m^3/s}$).
  - **Bỏ sót hoàn toàn câu (d) của đề gốc**: Tính khối lượng khí oxy hòa tan thoát ra mỗi giây khi nước bị nung nóng.
  - Tự bịa thêm câu (e) về độ tăng entropy của nước sông.
- **Dữ kiện thực tế từ sách giáo trình gốc (Trang PDF 694, trang in 675)**:
  - Nhà máy nhiệt điện than công suất phát điện $P = 1000\,\mathrm{MW} = 1{,}00 \times 10^9\,\mathrm W$.
  - Hiệu suất nhiệt toàn phần $e = 40\% = 0{,}40$.
  - Than anthracit có nhiệt cháy $L_c = 2{,}65 \times 10^7\,\mathrm{J/kg}$.
  - Lưu lượng dòng chảy của sông được **CHO TRƯỚC** là $\dot V = 37{,}0\,\mathrm{m^3/s}$.
  - Nồng độ oxy hòa tan trong nước sông được **CHO TRƯỚC** là $C_{\mathrm O_2} = 1{,}0 \times 10^{-5}\,\mathrm{g/cm^3}$.
- **Lời giải độc lập và giá trị đúng chuẩn theo sách gốc**:
  - **Câu (a)**: Tốc độ nhiệt cấp vào nhà máy:
    $$\dot Q_H = \frac{P}{e} = \frac{1000\,\mathrm{MW}}{0{,}40} = 2500\,\mathrm{MW} = 2{,}50 \times 10^9\,\mathrm W$$
  - **Câu (b)**: Khối lượng than tiêu thụ mỗi ngày (chạy liên tục 24 giờ = $86400\,\mathrm s$):
    $$m_{\mathrm{than}} = \frac{\dot Q_H \times 86400\,\mathrm s}{L_c} = \frac{2{,}50 \times 10^9 \times 86400}{2{,}65 \times 10^7} = 8{,}1509 \times 10^6\,\mathrm{kg/ngày} \approx 8{,}15 \times 10^6\,\mathrm{kg/ngày}$$
  - **Câu (c)**: Tốc độ thải nhiệt ra môi trường và độ tăng nhiệt độ của dòng sông:
    $$\dot Q_C = \dot Q_H - P = 2500\,\mathrm{MW} - 1000\,\mathrm{MW} = 1500\,\mathrm{MW} = 1{,}50 \times 10^9\,\mathrm W$$
    Lưu lượng khối lượng của dòng sông ($\rho_w = 1000\,\mathrm{kg/m^3}$):
    $$\dot m = \dot V \rho_w = 37{,}0\,\mathrm{m^3/s} \times 1000\,\mathrm{kg/m^3} = 3{,}70 \times 10^4\,\mathrm{kg/s}$$
    Độ tăng nhiệt độ của nước sông ($c_w = 4190\,\mathrm{J/(kg\cdot K)}$):
    $$\Delta T = \frac{\dot Q_C}{\dot m c_w} = \frac{1{,}50 \times 10^9\,\mathrm W}{3{,}70 \times 10^4\,\mathrm{kg/s} \times 4190\,\mathrm{J/(kg\cdot K)}} = \frac{1{,}50 \times 10^9}{1{,}5503 \times 10^8} = 9{,}676\,\mathrm{C^\circ} \approx 9{,}68\,\mathrm{C^\circ} \text{ (hoặc } 9{,}7\,\mathrm{C^\circ})$$
  - **Câu (d)**: Khối lượng oxy hòa tan giải phóng ra mỗi giây:
    Nồng độ oxy hòa tan: $1{,}0 \times 10^{-5}\,\mathrm{g/cm^3} = 10\,\mathrm{g/m^3} = 0{,}010\,\mathrm{kg/m^3}$.
    Tốc độ thoát khí oxy:
    $$\dot m_{\mathrm O_2} = C_{\mathrm O_2} \dot V = (1{,}0 \times 10^{-5}\,\mathrm{g/cm^3}) \times (37{,}0 \times 10^6\,\mathrm{cm^3/s}) = 370\,\mathrm{g/s} = 0{,}370\,\mathrm{kg/s}$$

---

## 3. Bảng Bằng Chứng Chi Tiết Từng Mục Thẩm Định (20.32–20.62)

| Mã bài | Trang PDF | Dòng / Tiêu đề trong file | Dữ kiện gốc từ sách (Source Facts) | Kết quả tính độc lập & Đánh giá sư phạm | Kết luận | Ghi chú & Giá trị hiệu chỉnh |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **20.32** | 693 (tr. 674) | Dòng 1–20 (`### 20.32`) | $P = 80\,\mathrm W$, 20% sinh công cơ học/chức năng sống, 80% thành nhiệt; $T_{\mathrm{trong}} = 37^\circ\mathrm C$, da lạnh hơn $7\,\mathrm{C^\circ}$ ($30^\circ\mathrm C$). | Dòng nhiệt truyền $64\,\mathrm W$ từ $310{,}15\,\mathrm K$ ra $303{,}15\,\mathrm K$. $\dot S = 64(1/303{,}15 - 1/310{,}15) = +4{,}765 \times 10^{-3}\,\mathrm{J/(K\cdot s)}$. | **PASS** | Nhận diện đúng ranh giới sinh entropy nội tại của cơ thể. |
| **20.33** | 693 (tr. 674) | Dòng 21–42 (`### 20.33`) | Chu trình Carnot, $Q_H = 410\,\mathrm J$, $T_H = 135^\circ\mathrm C$ ($408{,}15\,\mathrm K$), $e = 22{,}0\%$. Bơm giếng sâu $h = 35{,}0\,\mathrm m$. | (a) $W = 90{,}2\,\mathrm J$; (b) $Q_C = 319{,}8\,\mathrm J$; (c) $T_C = 318{,}4\,\mathrm K$ ($45{,}2^\circ\mathrm C$); (d) $\Delta S_{\mathrm{world}} = 0\,\mathrm{J/K}$; (e) $m = 90{,}2/(9{,}8 \times 35) = 0{,}2630\,\mathrm{kg}$. | **PASS** | Đầy đủ 5 câu hỏi (a)–(e), số liệu khớp hoàn toàn. |
| **20.34** | 693 (tr. 674) | Dòng 43–82 (`### 20.34`) | $0{,}350\,\mathrm{mol}$ khí hai nguyên tử ($\gamma = 1{,}40$); $1 \to 2$ đẳng tích, $2 \to 3$ đoạn nhiệt, $3 \to 1$ đẳng áp $1{,}00\,\mathrm{atm}$; $T_1 = 300\,\mathrm K, T_2 = 600\,\mathrm K, T_3 = 492\,\mathrm K$. | (a) $p_1 = p_3 = 1{,}00\,\mathrm{atm}$, $p_2 = 2{,}00\,\mathrm{atm}$, $V_1 = V_2 = 0{,}008616\,\mathrm{m^3}$, $V_3 = 0{,}01414\,\mathrm{m^3}$, $T_3 = 492{,}2\,\mathrm K$; (b) Bảng $Q, W, \Delta U$ chuẩn xác; (c) $W_{\mathrm{net}} = 224{,}9\,\mathrm J$; (d) $Q_{\mathrm{net}} = 224{,}9\,\mathrm J$; (e) $e = 10{,}31\%$, $e_{\mathrm{Carnot}} = 50{,}0\%$. | **PASS** | Đầy đủ 5 ý (a)–(e), phân tích khí hai nguyên tử chính xác. |
| **20.35** | 693 (tr. 674) | Dòng 83–108 (`### 20.35`) | Năng lượng mỡ $9{,}3\,\mathrm{kcal/g}$ ($1\,\mathrm{kcal} = 4186\,\mathrm J$), 80% thành nhiệt; $2{,}50\,\mathrm g$ bơ; $T_{\mathrm{trong}} = 37^\circ\mathrm C$, da $30^\circ\mathrm C$. | $Q = 2{,}50 \times 9{,}3 \times 4186 \times 0{,}80 = 77859{,}6\,\mathrm J$. $\Delta S = Q(1/303{,}15 - 1/310{,}15) = +5{,}797\,\mathrm{J/K} > 0$ (tăng). | **PASS** | Khớp cả độ lớn và dấu, làm rõ phạm vi truyền nhiệt. |
| **20.36** | 693 (tr. 674) | Dòng 109–138 (`### 20.36`) | $n$ mol khí hai nguyên tử đi qua chu trình chữ nhật $1 \to 2 \to 3 \to 4 \to 1$ ($V_0 \to 2V_0$, $p_0 \to 2p_0$). | $W = p_0V_0$; $Q_{\mathrm{in}} = Q_{12} + Q_{23} = \frac{5}{2}p_0V_0 + 7p_0V_0 = \frac{19}{2}p_0V_0$; $e = \frac{p_0V_0}{(19/2)p_0V_0} = \frac{2}{19} \approx 10{,}53\%$. | **PASS** | Nhận diện đúng cả hai nhánh nhận nhiệt $12$ và $23$. |
| **20.37** | 693 (tr. 674) | Dòng 139–176 (`### 20.37`) | $1{,}00\,\mathrm{mol}$ khí hai nguyên tử; Hình P20.37: $a(0{,}010\,\mathrm{m^3}, 2 \times 10^5\,\mathrm{Pa})$, $b(0{,}005\,\mathrm{m^3}, 4 \times 10^5\,\mathrm{Pa})$, $c(0{,}010\,\mathrm{m^3}, 4 \times 10^5\,\mathrm{Pa})$. | (a) $p_aV_a = p_bV_b = 2000\,\mathrm J$; (b) $ab$ tỏa nhiệt, $bc$ nhận, $ca$ tỏa; (c) $T_a = T_b = 240{,}5\,\mathrm K, T_c = 481{,}1\,\mathrm K$; (d) Bảng $Q, W, \Delta U$, $W_{\mathrm{net}} = Q_{\mathrm{net}} = 613{,}7\,\mathrm J$; (e) $e = 8{,}767\%$. | **PASS** | Đầy đủ các bước và chứng minh đẳng nhiệt. |
| **20.38** | 693 (tr. 674) | Dòng 177–205 (`### 20.38`) | Cốc 1 pint chứa đá và nước ở $0^\circ\mathrm C$, không khí bếp $22{,}2^\circ\mathrm C$ ($295{,}35\,\mathrm K$); sáng hôm sau toàn bộ tan thành nước $22{,}2^\circ\mathrm C$. | Ước lượng $0{,}20\,\mathrm L$ đá ($0{,}1834\,\mathrm{kg}$), $0{,}20\,\mathrm L$ nước ($0{,}2000\,\mathrm{kg}$). (a) $\Delta S_{\mathrm{cốc}} = 349{,}8\,\mathrm{J/K}$; (b) $\Delta S_{\mathrm{air}} = -328{,}1\,\mathrm{J/K}$; (c) $\Delta S_{\mathrm{total}} = +21{,}64\,\mathrm{J/K} > 0$ (tăng). | **PASS** | Các giả định ước lượng hợp lý và chặt chẽ. |
| **20.39** | 693 (tr. 674) | Dòng 206–236 (`### 20.39`) | $2{,}00\,\mathrm{mol}$ heli (đơn nguyên tử); $T_{\max} = 327^\circ\mathrm C$ ($600{,}15\,\mathrm K$); $bc$ đẳng nhiệt; $p_a = p_c = 1{,}00 \times 10^5\,\mathrm{Pa}, p_b = 3{,}00 \times 10^5\,\mathrm{Pa}$. | $T_a = 200{,}05\,\mathrm K$. (a) $Q_{\mathrm{in}} = 2{,}094 \times 10^4\,\mathrm J$, $Q_{\mathrm{out}} = 1{,}663 \times 10^4\,\mathrm J$; (b) $W_{\mathrm{net}} = 4311\,\mathrm J$, $e = 20{,}58\%$; (c) $e_{\mathrm{Carnot}} = 66{,}67\% > 20{,}58\%$. | **PASS** | Khớp hoàn toàn các giá trị tích phân và trạng thái. |
| **20.40** | 694 (tr. 675) | Dòng 237–254 (`### 20.40`) | Động cơ Carnot cơ thể người: Miệng $37{,}0^\circ\mathrm C$, da $30{,}0^\circ\mathrm C$. Nâng hộp $2{,}50\,\mathrm{kg}$ lên $1{,}20\,\mathrm m$. Kẹo $350\,\mathrm{kcal}$, 80% thành nhiệt. | (a) $e_{\max} = 2{,}257\%$; (b) $W = 29{,}4\,\mathrm J$, $Q_H = 1303\,\mathrm J$; (c) $1$ thanh cấp $1172080\,\mathrm J$, cần $N = 0{,}001111$ thanh. | **PASS** | Lập luận vật lý chính xác, đổi đơn vị chuẩn. |
| **20.41** | 694 (tr. 675) | Dòng 255–274 (`### 20.41`) | OTEC Hawaii: Nước mặt $27^\circ\mathrm C$, nước sâu $6^\circ\mathrm C$. Công suất $210\,\mathrm{kW}$. Nước sâu ra ở $10^\circ\mathrm C$. | (a) $e_{\max} = 6{,}997\%$; (b) $\dot Q_H = 3{,}001 \times 10^6\,\mathrm W$, $\dot Q_C = 2{,}791 \times 10^6\,\mathrm W$; (c) $\dot m = 5{,}996 \times 10^5\,\mathrm{kg/h}$ và $5{,}996 \times 10^5\,\mathrm{L/h}$. | **PASS** | Đầy đủ các đơn vị yêu cầu $\mathrm{kg/h}$ và $\mathrm{L/h}$. |
| **20.42** | 694 (tr. 675) | Dòng 275–312 (`### 20.42`) | Khí đơn nguyên tử, chu trình tam giác $a(0{,}5\,\mathrm{m^3}, 3 \times 10^5\,\mathrm{Pa})$, $b(0{,}8\,\mathrm{m^3}, 3 \times 10^5\,\mathrm{Pa})$, $c(0{,}8\,\mathrm{m^3}, 10^5\,\mathrm{Pa})$, $ca$ đoạn thẳng. | (a) Bảng từng nhánh; (b) Chu trình $W = Q = 3 \times 10^4\,\mathrm J$; (c) $ca$ đổi dấu tại $V_* = 0{,}5938\,\mathrm{m^3}$, $Q_{ca,+} = 56{,}72\,\mathrm{kJ}$, $e_{\mathrm{thực}} = 10{,}65\%$ vs $e_{\mathrm{gộp}} = 11{,}1\%$. | **PASS** | Phân tích sâu sắc sự đổi dấu nhiệt lượng trên nhánh $ca$. |
| **20.43** | 694 (tr. 675) | Dòng 313–347 (`### 20.43`) | Oxy ($C_V = \frac{5}{2}R$), $2{,}00\,\mathrm{atm}, 4{,}00\,\mathrm L, 300\,\mathrm K$. Bốn quá trình: (i) đẳng áp đến $450\,\mathrm K$, (ii) đẳng tích đến $250\,\mathrm K$, (iii) đẳng nhiệt về $4{,}00\,\mathrm L$, (iv) đẳng tích về $300\,\mathrm K$. | (a) Tọa độ 4 trạng thái; (b) Bảng $Q, W$; (c) $W_{\mathrm{net}} = 131{,}4\,\mathrm J$; (d) $Q_{\mathrm{in}} = 1756\,\mathrm J$, $e = 7{,}48\%$. | **PASS** | Đầy đủ tọa độ trạng thái và các đại lượng từng nhánh. |
| **20.44** | 694 (tr. 675) | Dòng 348–375 (`### 20.44`) | Nhà máy than $1000\,\mathrm{MW}$, $e = 40\%$, than $2{,}65 \times 10^7\,\mathrm{J/kg}$. Sông có lưu lượng **$37{,}0\,\mathrm{m^3/s}$**. Oxy hòa tan **$1{,}0 \times 10^{-5}\,\mathrm{g/cm^3}$**. | Đề bài tự ý sửa dữ kiện: Đảo ngược hỏi lưu lượng sông với $\Delta T = 0{,}5\,\mathrm{C^\circ}$, bỏ sót hoàn toàn ý (d) tính oxy giải phóng ($370\,\mathrm{g/s}$), tự thêm ý (e). | **FAIL** | **Cần thay thế toàn bộ (c), (d)**: $\dot Q_C = 1500\,\mathrm{MW}$, $\Delta T_{\mathrm{sông}} = 9{,}68\,\mathrm{C^\circ}$, $\dot m_{\mathrm O_2} = 370\,\mathrm{g/s}$. |
| **20.45** | 694 (tr. 675) | Dòng 376–398 (`### 20.45`) | Hai động cơ Carnot ghép tầng: Động cơ 1 ($T_H \to T'$), động cơ 2 nhận nhiệt thải ($T' \to T_C$). Tính hiệu suất hệ ghép. | $W_{\mathrm{tot}} = W_1 + W_2 = Q_H(1 - T_C/T_H) \implies e = 1 - T_C/T_H = e_{\mathrm{original}}$. Hiệu suất bằng đúng động cơ đơn. | **PASS** | Lập luận logic và chặt chẽ, chứng minh rõ ràng. |
| **20.46** | 694 (tr. 675) | Dòng 399–418 (`### 20.46`) | Ước lượng mpg; $120\,\mathrm{MJ/gal}$, xe chạy $40\,\mathrm{mph}$, $3000\,\mathrm{rpm}$. Động cơ $e = 20\%$. (a) mpg; (b) năng lượng nổ mỗi chu kỳ; (c) công suất (W); (d) hp. | Ước lượng $30\,\mathrm{mpg}$. (b) Động cơ 4 kỳ: $f = 25\,\mathrm{Hz}$, $Q = 1778\,\mathrm J/\text{chu kỳ}$; (c) $P = 8889\,\mathrm W$; (d) $P = 11{,}92\,\mathrm{hp}$. | **PASS** | Làm rõ giả định động cơ 4 kỳ (2 vòng/chu kỳ). |
| **20.47** | 694 (tr. 675) | Dòng 419–455 (`### 20.47`) | VW Passat 6 xi lanh, $r = 10{,}6$, bore $82{,}5\,\mathrm{mm}$, stroke $86{,}4\,\mathrm{mm}$, $p_a = 8{,}50 \times 10^4\,\mathrm{Pa}, T_a = 300\,\mathrm K, Q = 200\,\mathrm J/\text{xi lanh}$, $C_V = 20{,}5\,\mathrm{J/(mol\cdot K)}, \gamma = 1{,}40$. | (a) $V_{\mathrm{disp}} = 2{,}771\,\mathrm L$; (b) $V_{\max} = 510{,}0\,\mathrm{cm^3}, V_{\min} = 48{,}11\,\mathrm{cm^3}, n = 0{,}01738\,\mathrm{mol}$; (c) Trạng thái $b, c, d$; (d) $e_{\mathrm{Otto}} = 61{,}11\%, e_{\mathrm{Carnot}} = 77{,}49\%$. | **PASS** | Tính toán hình học động cơ và nhiệt động cực kỳ chuẩn xác. |
| **20.48** | 694 (tr. 675) | Dòng 456–481 (`### 20.48`) | (a) Ước lượng phòng; (b) Khí STP $22{,}4\,\mathrm L/mol$, tìm số mol; (c) Số phân tử; (d) Số trạng thái vi mô $N^N$, tính $S = k_B \ln(N^N)$. | Chọn phòng $30\,\mathrm{m^3}$. (b) $n = 1339\,\mathrm{mol}$; (c) $N = 8{,}065 \times 10^{26}$; (d) $S = k_B N \ln N = 6{,}899 \times 10^5\,\mathrm{J/K}$. | **PASS** | Đi kèm phân tích giới hạn thống kê vi mô. |
| **20.49** | 694 (tr. 675) | Dòng 482–506 (`### 20.49`) | Máy lạnh $0{,}850\,\mathrm{mol}\,\mathrm{H_2}$, Hình P20.49. $ab$ đẳng nhiệt. $a(0{,}03\,\mathrm{m^3}, 0{,}7\,\mathrm{atm})$, $b(0{,}1\,\mathrm{m^3})$, $c(0{,}1\,\mathrm{m^3}, 0{,}7\,\mathrm{atm})$. COP? | $W_{\mathrm{vào}} = 2403\,\mathrm J$. $K_{\mathrm{gộp}} = (Q_{ab} + Q_{bc})/W_{\mathrm{vào}} = 6{,}231$. $K_{\mathrm{iso}} = Q_{ab}/W_{\mathrm{vào}} = 1{,}066$. Phân biệt rõ ranh giới lạnh. | **PASS** | Thấu đáo cả về góc nhìn giáo trình và nhiệt động học thực tế. |
| **20.50** | 694 (tr. 675) | Dòng 507–526 (`### 20.50`) | Người $A = 1{,}85\,\mathrm{m^2}$, da $30{,}0^\circ\mathrm C$, phòng $20{,}0^\circ\mathrm C$, bức xạ thuần túy, độ phát xạ $1{,}00$. Tốc độ tăng entropy phòng? | $H_{\mathrm{net}} = \sigma A(303{,}15^4 - 293{,}15^4) = 111{,}2\,\mathrm W$. $\dot S_{\mathrm{room}} = 111{,}2 / 293{,}15 = +0{,}3795\,\mathrm{J/(K\cdot s)}$. | **PASS** | Áp dụng đúng định luật Stefan–Boltzmann và nhiệt độ nguồn nhận. |
| **20.51** | 695 (tr. 676) | Dòng 527–569 (`### 20.51`) | Hai vật $m_1, c_1, T_1$ và $m_2, c_2, T_2 > T_1$. (a) Chứng minh công thức $\Delta S$ và bảo toàn năng lượng; (b) Chứng minh $\Delta S$ cực đại khi $T = T'$; (c) Ý nghĩa hỗn loạn. | (a) Thiết lập vi phân tích phân; (b) Ràng buộc năng lượng cho $dT'/dT = -C_1/C_2$, $d\Delta S/dT = C_1(1/T - 1/T') = 0 \iff T = T'$, $d^2\Delta S/dT^2 < 0$; (c) Số vi trạng thái cực đại. | **PASS** | Đạo hàm giải tích và lập luận điều kiện biên hoàn hảo. |
| **20.52** | 695 (tr. 676) | Dòng 570–597 (`### 20.52`) | $250\,\mathrm{cm^3}$ nước $20^\circ\mathrm C \to 78^\circ\mathrm C$, điện trở giữ $120^\circ\mathrm C$. (a) $\Delta S_w$; (b) $\Delta S_{\mathrm{elem}}$; (c) $\Delta S_{\mathrm{sys}}$; (d) Thuận nghịch hay không? | $Q = 60755\,\mathrm J$. (a) $\Delta S_w = 189{,}1\,\mathrm{J/K}$; (b) Nguồn lý tưởng $-154{,}5\,\mathrm{J/K}$ vs Điện trở dừng $0\,\mathrm{J/K}$; (c) Hệ lý tưởng $34{,}57\,\mathrm{J/K}$ vs Điện trở thực $189{,}1\,\mathrm{J/K}$; (d) Bất thuận nghịch. | **PASS** | Tách bạch xuất sắc giữa mô hình nguồn lý tưởng và điện trở thực. |
| **20.53** | 695 (tr. 676) | Dòng 598–621 (`### 20.53`) | Động cơ bốn nhà sáng chế A, B, C, D với các cặp nhiệt độ và hiệu suất công bố: A (47/177°C, 21%), B (17/197°C, 35%), C (-33/247°C, 56%), D (37/137°C, 20%). | $e_{\max}$: A ($28{,}88\%$), B ($38{,}29\%$), C ($53{,}83\%$), D ($24{,}38\%$). C bất khả thi ($56\% > 53{,}83\%$). Tỷ lệ: B ($0{,}914$) > D ($0{,}820$) > A ($0{,}727$). | **PASS** | Đầy đủ 3 câu (a), (b), (c), xếp hạng chính xác. |
| **20.54** | 695 (tr. 676) | Dòng 622–647 (`### 20.54`) | Định nghĩa $K = \mathrm{COP}$. EER tính theo $\mathrm{Btu/(W\cdot h)}$. (a) Quan hệ EER-$K$; (b) EER Carnot giữa $95^\circ\mathrm F$ và $80^\circ\mathrm F$; (c) EER $10{,}9$, $Q_C = 1{,}9 \times 10^{10}\,\mathrm J$, giá $15{,}3\,\mathrm{cents/(kW\cdot h)}$; (d) Đổi sang EER $14{,}6$. | (a) $\mathrm{EER} = 3{,}412 K$; (b) $\mathrm{EER}_{\mathrm{Carnot}} = 122{,}8$; (c) Chi phí $\$252{,}8$; (d) Tiết kiệm $\$64{,}06$. | **PASS** | Chuyển đổi đơn vị Anh-Mỹ sang SI hoàn toàn chính xác. |
| **20.55** | 695 (tr. 676) | Dòng 648–681 (`### 20.55`) | $4{,}00\,\mathrm{mol}$ argon (đơn nguyên tử), Hình P20.55, $T_a = 250\,\mathrm K, T_b = 300\,\mathrm K, T_c = 380\,\mathrm K, T_d = 316{,}7\,\mathrm K$. | (a) $e = 4{,}848\%$; (b) Tăng gấp đôi số mol: $e = 4{,}848\%$ (không đổi); (c) Gấp đôi thể tích $c, d$: $e = 6{,}259\%$; (d) $e(T_d) = \frac{0{,}2 T_d - 50}{3{,}0 T_d - 675}$, tiệm cận $1/15 = 6{,}67\%$. | **PASS** | Đầy đủ 4 ý (a)–(d), biểu thức tiệm cận chính xác. |
| **20.56** | 695 (tr. 676) | Dòng 682–709 (`### 20.56`) | Động cơ Stirling lý tưởng: Dãn $T_H$, nén $T_C$. (a) Chứng minh $p_c/p_d = p_b/p_a = \mathrm{CR}$; (b) Công dãn; (c) Công nén; (d) $1\,\mathrm{mol}$ heli, $\mathrm{CR} = 10$, $100^\circ\mathrm C$ và $20^\circ\mathrm C$, $100\,\mathrm{Hz}$. | (a) Tỷ số thể tích; (b) $W_{\mathrm{nở}} = nRT_H \ln(\mathrm{CR})$; (c) $W_{\mathrm{nén}} = -nRT_C \ln(\mathrm{CR})$; (d) $W_{\mathrm{net}} = 1531{,}6\,\mathrm J \implies P = 153{,}2\,\mathrm{kW}$. | **PASS** | Khớp công thức đại số và công suất phát ra. |
| **20.57** | 696 (tr. 677) | Dòng 710–739 (`### 20.57`) | Sinh vật sporon Tralfamadore, chu trình Carnot, $\gamma = 1{,}30$. Nén đoạn nhiệt giảm nửa thể tích, đạt $r = 8{,}0\,\mathrm{cm}, p = 20{,}3\,\mathrm{kPa}$. Dãn về $123\,\mathrm K$, áp suất dư 0. Nén bán kính giảm 3 lần về $V_{\mathrm{trigger}}$. | (a) $T_H = 123 \times 2^{0{,}30} = 151{,}4\,\mathrm K$; (b) $V_d = 54 V_c \implies p_{\mathrm{mt}} = 305{,}3\,\mathrm{Pa}$; (c) $e = 18{,}77\%, W = 1000\,\mathrm{J/phút} \implies Q_{\mathrm{in}} = 5326\,\mathrm{J/phút}$; (d) $Q_{\mathrm{out}} = 4326\,\mathrm{J/phút}$. | **PASS** | Xử lý xuất sắc mối quan hệ lập phương bán kính thể tích cầu. |
| **20.58** | 696 (tr. 677) | Dòng 740–778 (`### 20.58`) | Chu trình Diesel khí lý tưởng: (a) Lập công thức $e(r, T_a, T_c, \gamma)$; (b) Tính với $T_a = 300\,\mathrm K, T_c = 950\,\mathrm K, \gamma = 1{,}40, r = 21{,}0$. | (a) Biểu thức chuẩn $e$; (b) Nén cho $T_b = 1014\,\mathrm K > T_c = 950\,\mathrm K \implies \rho = 0{,}9369 < 1$, vi phạm điều kiện cấp nhiệt dương. Cần $r < 17{,}84$. Thay số máy móc ra $70{,}79\%$ là phi vật lý. | **PASS** | Phân tích mâu thuẫn dữ kiện số học sắc sảo, không lặp lại sai lầm máy móc. |
| **20.59** | 696 (tr. 677) | Dòng 787–806 (`### 20.59`) | Bài đọc hiểu OTEC: Nước mặt $27^\circ\mathrm C$, hiệu suất Carnot $6{,}5\%$. Cần lấy nước sâu ở độ sâu nào? | $T_C = 300{,}15(1 - 0{,}065) = 280{,}64\,\mathrm K = 7{,}49^\circ\mathrm C$. Đọc đồ thị tại $7{,}5^\circ\mathrm C$ cho độ sâu khoảng $400\,\mathrm m$. Chọn **(b)**. | **PASS** | Đọc đồ thị chính xác, giải thích bước chuyển nhiệt độ. |
| **20.60** | 696 (tr. 677) | Dòng 807–826 (`### 20.60`) | Nhà máy $10\,\mathrm{MW}$, $e = 6{,}5\%$. Độ biến thiên entropy của amoniac hóa hơi mỗi giây tại $27^\circ\mathrm C$? | $\dot Q_H = 10^7 / 0{,}065 = 1{,}5385 \times 10^8\,\mathrm W$. $\dot S = \dot Q_H / 300{,}15 = 5{,}126 \times 10^5\,\mathrm{J/(K\cdot s)} \approx +5 \times 10^5\,\mathrm{J/(K\cdot s)}$. Chọn **(b)**. | **PASS** | Khớp phương án trắc nghiệm chuẩn của đề bài. |
| **20.61** | 696 (tr. 677) | Dòng 827–846 (`### 20.61`) | So sánh độ biến thiên entropy của nước ấm và nước lạnh trong một chu trình Carnot lý tưởng. | Chu trình thuận nghịch: $\Delta S_{\mathrm{world}} = -Q_H/T_H + Q_C/T_C = 0 \implies \Delta S_H = -\Delta S_C$. Nước ấm giảm đúng bằng nước lạnh tăng. Chọn **(d)**. | **PASS** | Khớp định luật II nhiệt động học cho chu trình thuận nghịch. |
| **20.62** | 696 (tr. 677) | Dòng 847–865 (`### 20.62`) | Nhà máy phát $10\,\mathrm{MW}$, thải $165\,\mathrm{MW}$ nhiệt vào nước lạnh. Hiệu suất thực tế? | $\dot Q_H = 10 + 165 = 175\,\mathrm{MW} \implies e = 10 / 175 = 5{,}71\%$. Chọn **(a)**. | **PASS** | Khớp phương án trắc nghiệm, tránh bẫy chia cho $165\,\mathrm{MW}$. |

---

## 4. Tổng Hợp Thâm Hụt Nguồn & Đề Xuất Hiệu Chỉnh (Discrepancy Remediation)

### Bài duy nhất không đạt: Bài 20.44
- **Vị trí lỗi**: Tệp `raw_materials/physics/translations/chapter-20/12-bai-tap-032-062.md`, dòng 348–375.
- **Bản chất lỗi**:
  - Không tuân thủ dữ kiện gốc của giáo trình: Đề bài gốc cung cấp lưu lượng sông $\dot V = 37{,}0\,\mathrm{m^3/s}$ và hỏi độ tăng nhiệt độ $\Delta T$ của dòng sông, nhưng bài soạn lại giả định $\Delta T = 0{,}5\,\mathrm{C^\circ}$ và đi tìm lưu lượng dòng chảy ($716\,\mathrm{m^3/s}$).
  - Bỏ sót hoàn toàn câu hỏi (d) của đề bài gốc về tốc độ giải phóng khí oxy hòa tan ra môi trường (với nồng độ cho trước $1{,}0 \times 10^{-5}\,\mathrm{g/cm^3}$).
  - Tự ý bổ sung câu hỏi (e) về entropy không có trong sách gốc.
- **Khuyến nghị văn bản thay thế chuẩn mực cho Bài 20.44**:
  Người phụ trách biên tập tệp bài giảng cần thay thế nội dung câu (c) và (d) trong `12-bai-tap-032-062.md` bằng nội dung chuẩn xác sau:
  > **Đề bài hiệu chỉnh**:
  > Nhà máy nhiệt điện than phát 1000 MW điện hữu ích ở hiệu suất nhiệt toàn phần 40%. (a) Tốc độ cấp nhiệt cho nhà máy? (b) Than anthracit có nhiệt cháy $2{,}65 \times 10^7\,\mathrm{J/kg}$. Vận hành liên tục ở mức công suất này thì mỗi ngày nhà máy tiêu thụ bao nhiêu kg than? (c) Nhiệt lượng thải ra môi trường với tốc độ bao nhiêu, và nếu nhiệt lượng này được cuốn đi bởi một dòng sông có lưu lượng $37{,}0\,\mathrm{m^3/s}$ thì nước sông tăng thêm bao nhiêu độ? (d) Nước sông thông thường chứa $1{,}0 \times 10^{-5}\,\mathrm g$ oxy hòa tan trên mỗi $\mathrm{cm^3}$ nước. Nếu toàn bộ lượng oxy này bị giải phóng khi nước bị làm nóng bởi nhà máy, mỗi giây có bao nhiêu oxy thoát ra?
  >
  > **Lời giải hiệu chỉnh**:
  > (a) $\dot Q_H = \frac{P}{e} = \frac{1000 \times 10^6}{0{,}40} = 2{,}50 \times 10^9\,\mathrm W$.
  > (b) Năng lượng cần cấp trong 1 ngày ($86400\,\mathrm s$): $E = 2{,}50 \times 10^9 \times 86400 = 2{,}16 \times 10^{14}\,\mathrm J$. Khối lượng than tiêu thụ: $m = \frac{2{,}16 \times 10^{14}}{2{,}65 \times 10^7} = 8{,}15 \times 10^6\,\mathrm{kg/ngày}$ ($8150$ tấn/ngày).
  > (c) Tốc độ thải nhiệt ra sông: $\dot Q_C = \dot Q_H - P = 1{,}50 \times 10^9\,\mathrm W$. Lưu lượng khối lượng nước sông: $\dot m = 37{,}0\,\mathrm{m^3/s} \times 1000\,\mathrm{kg/m^3} = 3{,}70 \times 10^4\,\mathrm{kg/s}$. Độ tăng nhiệt độ của dòng sông ($c_w = 4190\,\mathrm{J/(kg\cdot K)}$):
  > $$\Delta T = \frac{\dot Q_C}{\dot m c_w} = \frac{1{,}50 \times 10^9}{3{,}70 \times 10^4 \times 4190} = 9{,}68\,\mathrm{C^\circ}$$
  > (d) Lưu lượng thể tích của dòng sông là $37{,}0 \times 10^6\,\mathrm{cm^3/s}$. Tốc độ oxy hòa tan thoát ra môi trường mỗi giây:
  > $$\dot m_{\mathrm O_2} = (1{,}0 \times 10^{-5}\,\mathrm{g/cm^3}) \times (37{,}0 \times 10^6\,\mathrm{cm^3/s}) = 370\,\mathrm{g/s} = 0{,}370\,\mathrm{kg/s}$$

---

## 5. Giả Thiết Mô Hình & Miền Giá Trị Bất Định (Assumptions & Uncertainties)

1. **Khí lý tưởng và nhiệt dung phân tử**:
   - Đối với heli và agon: Xem là khí đơn nguyên tử lý tưởng với $C_V = \frac{3}{2}R, C_p = \frac{5}{2}R, \gamma = \frac{5}{3} \approx 1{,}667$.
   - Đối với oxy, hydro và không khí: Xem là khí hai nguyên tử lý tưởng ở nhiệt độ phòng với $C_V = \frac{5}{2}R, C_p = \frac{7}{2}R, \gamma = 1{,}40$, bỏ qua dao động phân tử ở dải nhiệt độ này.
   - Đối với khí froklom (Bài 20.57): Tỷ số nhiệt dung được đề bài quy định riêng là $\gamma = 1{,}30$.
2. **Khối lượng riêng và nhiệt dung của nước**:
   - $\rho_w = 1000\,\mathrm{kg/m^3}$ ($1\,\mathrm L = 1\,\mathrm{kg}$, $1\,\mathrm{cm^3} = 1\,\mathrm g$).
   - $c_w = 4190\,\mathrm{J/(kg\cdot K)}$ (theo chuẩn Ví dụ 20.10 trong giáo trình Young & Freedman).
   - $L_f = 334000\,\mathrm{J/kg}$ cho nhiệt nóng chảy của nước đá; $L_c = 2{,}65 \times 10^7\,\mathrm{J/kg}$ cho nhiệt cháy của than anthracit.
3. **Các bài toán ước lượng (Fermi Estimates)**:
   - Bài 20.38 (Cốc nước đá): Ước lượng thể tích cốc 1 pint ($\approx 0{,}473\,\mathrm L$) chia thành $0{,}20\,\mathrm L$ đá và $0{,}20\,\mathrm L$ nước lỏng. Kết quả số học phụ thuộc vào tỷ lệ chọn ban đầu, nhưng dấu $\Delta S_{\mathrm{total}} > 0$ là bất biến.
   - Bài 20.46 (Mức tiết kiệm nhiên liệu): Ước lượng $30\,\mathrm{mpg}$, xe chạy động cơ 4 kỳ (cần 2 vòng quay trục khuỷu cho 1 chu kỳ sinh công của mỗi xi lanh, tức tần số chu kỳ của động cơ là $3000 / (60 \times 2) = 25\,\mathrm{Hz}$).
   - Bài 20.48 (Kích thước phòng): Ước lượng thể tích phòng $30\,\mathrm{m^3}$ ($4\,\mathrm m \times 3\,\mathrm m \times 2{,}5\,\mathrm m$).
4. **Đọc đồ thị Bài 20.59**:
   - Nhiệt độ nguồn lạnh tính được từ hiệu suất Carnot $6{,}5\%$ là $T_C = 7{,}49^\circ\mathrm C$. Trên đồ thị phân bố nhiệt độ đại dương theo độ sâu, đường đẳng nhiệt $7{,}5^\circ\mathrm C$ cắt đồ thị ở độ sâu khoảng $400\,\mathrm m$, ứng với phương án (b).

---

## 6. Lệnh Kiểm Tra Xác Minh & Trạng Thái Môi Trường (Commands & Results)

1. **Kiểm tra trạng thái Git (Git status)**:
   - Lệnh: `git status --short`
   - Kết quả: Không có thay đổi nào trên các tệp ngoài phạm vi sở hữu. Chỉ có tệp báo cáo mới `raw_materials/physics/reviews/physics1-ch20-parent-e-review-20261023.md`.
2. **Kiểm tra định dạng diff (Git diff check)**:
   - Lệnh: `git diff --check`
   - Kết quả: Mã thoát 0, không có trailing whitespace hay xung đột dòng.
3. **Mã Python tính toán độc lập trong bộ nhớ**:
   - Trình thông dịch: `C:/Users/Ai/miniconda3/python.exe -B -X utf8`
   - Thư viện sử dụng: `pymupdf` (đọc văn bản PDF gốc), `numpy`, `scipy.integrate` (tính tích phân số học đổi dấu nhánh $c \to a$ bài 20.42).
   - Mã kiểm thử có sẵn `raw_materials/physics/verify_priority_ch20_numbered.py` chỉ được đọc như một tài liệu tham chiếu tĩnh, không thực thi để tránh ghi đè dữ liệu ra ngoài phạm vi sở hữu được giao.

---

## 7. Kết Luận Cuối Cùng & Danh Sách Tệp Tác Động (Final Status)

- **Trạng thái thẩm định**: **HOÀN THÀNH (COMPLETE)**.
- **Tệp duy nhất thuộc quyền sở hữu & đã tạo mới**:
  `raw_materials/physics/reviews/physics1-ch20-parent-e-review-20261023.md`
- **Các tệp được giữ nguyên vẹn 100% (Immutable)**:
  - `raw_materials/physics/translations/chapter-20/12-bai-tap-032-062.md`
  - `raw_materials/physics/source/young-freedman-15.pdf`
  - `docs/agy-plans/2026-10-23-physics1-ch20-parent-e-review.md`
  - `raw_materials/physics/verify_priority_ch20_numbered.py`
  - Toàn bộ cây thư mục mã nguồn và tài liệu học liệu còn lại.
- **Khóa cản / Lỗi phân quyền**: Không có. Quyền miễn trừ tác vụ giới hạn của người dùng được tôn trọng và tuân thủ chặt chẽ.
