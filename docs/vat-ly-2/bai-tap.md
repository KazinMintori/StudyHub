---
title: Bài tập ôn luyện - Vật lý 2
description: Tuyển tập bài tập tính toán định luật Gauss, định luật Biot-Savart, cảm ứng điện từ Faraday, sóng điện từ và giao thoa quang học.
---

# Bài tập ôn luyện: Vật lý 2

Hệ thống bài tập môn Vật lý 2 (Điện - Từ - Quang sóng) được biên soạn theo khung lý thuyết giải tích vật lý đại cương, phục vụ ôn tập kiểm tra giữa kỳ và thi kết thúc học phần.

---

## Phần 1. Điện trường tĩnh & Định luật Gauss

### Bài 1.1: Ứng dụng Định luật Gauss tính điện trường của khối cầu tích điện đều
Một quả cầu điện môi bán kính $R$ được tích điện đều với mật độ điện tích khối $\rho = \text{const}$. Tổng điện tích của khối cầu là $Q = \rho \cdot \frac{4}{3}\pi R^3$. Đặt quả cầu trong chân không (hằng số điện môi $\varepsilon_0$).

1. Viết biểu thức Định luật Gauss dạng tích phân cho điện trường $\vec{E}$:
   $$\oint_{S} \vec{E} \cdot d\vec{A} = \frac{Q_{\text{in}}}{\varepsilon_0}$$
2. Chọn mặt Gauss phù hợp và tính cường độ điện trường $E(r)$ tại điểm nằm **bên ngoài** quả cầu ($r \ge R$).
3. Tính cường độ điện trường $E(r)$ tại điểm nằm **bên trong** quả cầu ($r < R$).
4. Tính hiệu điện thế (điện thế) $V(r)$ tại tâm quả cầu ($r = 0$) so với mốc điện thế ở vô cùng ($V(\infty) = 0$).

#### Lời giải gợi ý
1. Định luật Gauss: Điện thông qua một mặt kín $S$ tỷ lệ thuận với tổng đại số điện tích nằm bên trong mặt kín đó.

2. Với $r \ge R$ (Bên ngoài khối cầu):
   - Do tính đối xứng cầu, vector cường độ điện trường $\vec{E}$ hướng theo phương bán kính ra xa tâm và có độ lớn không đổi tại mọi điểm trên mặt cầu Gauss bán kính $r$.
   - Thông lượng điện:
     $$\Phi_E = \oint_S E \, dA = E(r) \cdot 4\pi r^2$$
   - Điện tích bên trong mặt Gauss: $Q_{\text{in}} = Q$.
   - Theo định luật Gauss:
     $$E(r) \cdot 4\pi r^2 = \frac{Q}{\varepsilon_0} \implies E(r) = \frac{Q}{4\pi \varepsilon_0 r^2} = \frac{\rho R^3}{3\varepsilon_0 r^2}$$

3. Với $r < R$ (Bên trong khối cầu):
   - Mặt cầu Gauss bán kính $r < R$ chỉ chứa phần điện tích:
     $$Q_{\text{in}} = \rho \cdot \frac{4}{3}\pi r^3 = Q \left(\frac{r}{R}\right)^3$$
   - Áp dụng Gauss:
     $$E(r) \cdot 4\pi r^2 = \frac{\rho \cdot \frac{4}{3}\pi r^3}{\varepsilon_0} \implies E(r) = \frac{\rho r}{3\varepsilon_0} = \frac{Q r}{4\pi \varepsilon_0 R^3}$$
   - Nhận xét: Điện trường bên trong khối cầu tỷ lệ bậc nhất với khoảng cách $r$ tới tâm.

4. Điện thế tại tâm $V(0)$:
   $$V(0) - V(\infty) = \int_0^\infty E(r) \, dr = \int_0^R E_{\text{in}}(r) \, dr + \int_R^\infty E_{\text{out}}(r) \, dr$$
   $$= \int_0^R \frac{Q r}{4\pi \varepsilon_0 R^3} \, dr + \int_R^\infty \frac{Q}{4\pi \varepsilon_0 r^2} \, dr = \frac{Q}{4\pi \varepsilon_0 R^3} \left[ \frac{r^2}{2} \right]_0^R + \frac{Q}{4\pi \varepsilon_0 R} = \frac{Q}{8\pi \varepsilon_0 R} + \frac{Q}{4\pi \varepsilon_0 R} = \frac{3Q}{8\pi \varepsilon_0 R}$$

---

## Phần 2. Từ trường & Cảm ứng điện từ

### Bài 2.1: Định luật Biot–Savart & Định luật cảm ứng Faraday
1. Cho một dây dẫn thẳng dài vô hạn mang dòng điện không đổi $I_1$. Áp dụng định luật Ampere, tìm cảm ứng từ $B$ tại điểm cách dây một khoảng $r$.
2. Đặt một khung dây chữ nhật bằng đồng kích thước $a \times b$ (với cạnh $b$ song song với dây dẫn, khoảng cách từ dây đến cạnh gần nhất là $d$) trong cùng mặt phẳng với dây dẫn.
   Tính từ thông $\Phi_B$ xuyên qua khung dây:
   $$\Phi_B = \int_S \vec{B} \cdot d\vec{A}$$
3. Giả sử dòng điện trong dây dẫn biến thiên theo thời gian theo quy luật $I(t) = I_0 \sin(\omega t)$. Xác định suất điện động cảm ứng $\mathcal{E}_{\text{ind}}(t)$ xuất hiện trong khung dây theo định luật Faraday:
   $$\mathcal{E}_{\text{ind}} = -\frac{d\Phi_B}{dt}$$

#### Lời giải gợi ý
1. Áp dụng định luật Ampere với đường tròn bán kính $r$ đồng trục với dây dẫn:
   $$\oint \vec{B} \cdot d\vec{\ell} = B(r) \cdot 2\pi r = \mu_0 I_1 \implies B(r) = \frac{\mu_0 I_1}{2\pi r}$$

2. Từ thông qua khung dây:
   - Chia khung dây thành các dải hẹp có diện tích $dA = b \, dr$ cách dây khoảng $r \in [d, d + a]$.
   - Tích phân từ thông:
     $$\Phi_B = \int_d^{d+a} B(r) b \, dr = \int_d^{d+a} \frac{\mu_0 I_1}{2\pi r} b \, dr = \frac{\mu_0 I_1 b}{2\pi} \int_d^{d+a} \frac{dr}{r} = \frac{\mu_0 I_1 b}{2\pi} \ln\left(\frac{d + a}{d}\right)$$

3. Khi $I_1(t) = I_0 \sin(\omega t)$:
   $$\Phi_B(t) = \frac{\mu_0 b}{2\pi} \ln\left(\frac{d + a}{d}\right) I_0 \sin(\omega t)$$
   Suất điện động cảm ứng:
   $$\mathcal{E}_{\text{ind}}(t) = -\frac{d\Phi_B}{dt} = -\frac{\mu_0 b I_0 \omega}{2\pi} \ln\left(\frac{d + a}{d}\right) \cos(\omega t)$$

---

## Phần 3. Sóng điện từ & Vector Poynting

### Bài 3.1: Mật độ năng lượng và Vector Poynting
Một sóng điện từ phẳng hình sin truyền trong chân không dọc theo trục $Oz$ theo chiều dương. Điện trường của sóng được mô tả bởi:
$$\vec{E}(z, t) = E_0 \cos(kz - \omega t) \hat{i}$$

1. Xác định phương và biểu thức giải tích của vector cảm ứng từ $\vec{B}(z, t)$.
2. Tính mật độ năng lượng tức thời của trường điện từ:
   $$u = u_E + u_B = \frac{1}{2}\varepsilon_0 E^2 + \frac{1}{2\mu_0} B^2$$
3. Thiết lập biểu thức của vector Poynting $\vec{S} = \frac{1}{\mu_0} (\vec{E} \times \vec{B})$ và tính cường độ sóng trung bình $I = \langle |\vec{S}| \rangle$.

#### Lời giải gợi ý
1. Trong sóng điện từ truyền theo trục $+Oz$:
   - Vector $\vec{E}$, $\vec{B}$ và vector truyền sóng $\vec{k}$ tạo thành tam diện thuận.
   - Vì $\vec{E}$ dao động theo trục $Ox$ ($\hat{i}$), $\vec{B}$ phải dao động theo trục $Oy$ ($\hat{j}$).
   - Độ lớn: $B_0 = E_0 / c$ (với $c = 1/\sqrt{\varepsilon_0 \mu_0}$).
   $$\vec{B}(z, t) = \frac{E_0}{c} \cos(kz - \omega t) \hat{j}$$

2. Mật độ năng lượng:
   $$u_E = \frac{1}{2}\varepsilon_0 E_0^2 \cos^2(kz - \omega t)$$
   $$u_B = \frac{1}{2\mu_0} \frac{E_0^2}{c^2} \cos^2(kz - \omega t) = \frac{1}{2}\varepsilon_0 E_0^2 \cos^2(kz - \omega t) = u_E$$
   Tổng mật độ năng lượng tức thời:
   $$u(z, t) = \varepsilon_0 E_0^2 \cos^2(kz - \omega t)$$

3. Vector Poynting:
   $$\vec{S} = \frac{1}{\mu_0} (\vec{E} \times \vec{B}) = \frac{1}{\mu_0} \left[ E_0 \cos(kz - \omega t) \hat{i} \times \frac{E_0}{c} \cos(kz - \omega t) \hat{j} \right]$$
   $$= \frac{E_0^2}{\mu_0 c} \cos^2(kz - \omega t) \hat{k} = c \varepsilon_0 E_0^2 \cos^2(kz - \omega t) \hat{k}$$
   Cường độ sóng trung bình theo thời gian (với $\langle \cos^2 \theta \rangle = \frac{1}{2}$):
   $$I = \langle |\vec{S}| \rangle = \frac{1}{2} c \varepsilon_0 E_0^2$$

---

## Phần 4. Quang sóng & Giao thoa ánh sáng

### Bài 4.1: Thí nghiệm giao thoa khe Young
Trong thí nghiệm giao thoa ánh sáng Young, khoảng cách giữa hai khe là $a = 0.5$ mm, khoảng cách từ mặt phẳng chứa hai khe đến màn quan sát là $D = 2.0$ m. Nguồn sáng phát ra bức xạ đơn sắc có bước sóng $\lambda = 600$ nm ($6 \times 10^{-7}$ m).

1. Tính khoảng vân giao thoa $i$ trên màn quan sát:
   $$i = \frac{\lambda D}{a}$$
2. Xác định vị trí vân sáng bậc 4 và vân tối thứ 3 tính từ vân sáng trung tâm.
3. Người ta đặt ngay sau một trong hai khe một bản thủy tinh mỏng trong suốt có độ dày $e = 10$ $\mu$m và chiết suất $n = 1.5$.
   Hỏi hệ vân giao thoa sẽ dịch chuyển về phía nào và dịch chuyển một đoạn bằng bao nhiêu?

#### Lời giải gợi ý
1. Khoảng vân giao thoa:
   $$i = \frac{\lambda D}{a} = \frac{600 \times 10^{-9} \text{ m} \times 2.0 \text{ m}}{0.5 \times 10^{-3} \text{ m}} = 2.4 \times 10^{-3} \text{ m} = 2.4 \text{ mm}$$

2. Vị trí vân:
   - Vân sáng bậc 4: $x_{s4} = \pm 4 i = \pm 4 \times 2.4 = \pm 9.6$ mm.
   - Vân tối thứ 3: $x_{t3} = \pm (3 - 0.5) i = \pm 2.5 \times 2.4 = \pm 6.0$ mm.

3. Dịch chuyển của hệ vân khi chèn bản mỏng:
   - Hiệu quang lộ thêm vào do bản thủy tinh gây ra: $\Delta L = (n - 1)e$.
   - Vân trung tâm mới thỏa mãn hiệu quang lộ bằng 0:
     $$r_2 - r_1 = \frac{a x_0}{D} = \Delta L = (n - 1)e$$
   - Độ dịch chuyển của hệ vân:
     $$x_0 = \frac{D}{a} (n - 1) e = \frac{2.0}{0.5 \times 10^{-3}} (1.5 - 1) \times (10 \times 10^{-6}) = 4000 \times 0.5 \times 10^{-5} = 0.02 \text{ m} = 20 \text{ mm}$$
   - Hệ vân dịch chuyển về phía khe có đặt bản mỏng thủy tinh một khoảng $20$ mm (tương đương với việc dịch chuyển $\frac{20}{2.4} \approx 8.33$ khoảng vân).
