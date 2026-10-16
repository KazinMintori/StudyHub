## Bài tập cầu nối: Độ bão hòa trong quá trình sản xuất 128I

### Bài tập cầu nối

Trong một thí nghiệm, đồng vị iot $^{128}\mathrm{I}$ được tạo ra bằng cách chiếu xạ một mẫu $^{127}\mathrm{I}$ bằng một chùm neutron, tạo ra $1{,}50 \times 10^6$ hạt nhân $^{128}\mathrm{I}$ mỗi giây. Ban đầu trong mẫu không có hạt nhân $^{128}\mathrm{I}$ nào. Hạt nhân $^{128}\mathrm{I}$ phân rã theo cơ chế phát xạ $\beta^-$ với chu kỳ bán rã $25{,}0\,\mathrm{min}$.
(a) Hạt nhân $^{128}\mathrm{I}$ phân rã thành nuclide nào?
(b) Nuclide đó có thể phân rã ngược lại thành $^{128}\mathrm{I}$ thông qua phát xạ $\beta^+$ hay không? Tại sao có hoặc tại sao không?
(c) Sau khi mẫu được chiếu xạ trong một thời gian dài, số lượng nguyên tử $^{128}\mathrm{I}$ tối đa có thể có mặt trong mẫu là bao nhiêu? Hoạt độ phóng xạ tối đa có thể tạo ra là bao nhiêu? (Trạng thái dừng này được gọi là sự bão hòa).
(d) Tìm biểu thức xác định số nguyên tử $^{128}\mathrm{I}$ có mặt trong mẫu theo thời gian.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Tốc độ sinh hạt nhân $^{128}\mathrm{I}$ do chùm neutron: $R = 1{,}50 \times 10^6\,\mathrm{s^{-1}}$.
- Điều kiện ban đầu tại $t = 0$: $N(0) = 0$.
- Chu kỳ bán rã của $^{128}\mathrm{I}$: $T_{1/2} = 25{,}0\,\mathrm{min} = 1500\,\mathrm{s}$.
- Cần xác định: Nuclide con của phân rã $\beta^-$, khả năng xảy ra phân rã $\beta^+$ đảo ngược, số lượng hạt nhân cực đại $N_{\max}$ và hoạt độ bão hòa $A_{\max}$, biểu thức $N(t)$ theo thời gian cùng kiểm tra giới hạn thời gian dài.

**Hướng đi:**

Áp dụng đầy đủ 8 chỉ dẫn phương pháp luận của bài toán cầu nối:
- **Xác định và thiết lập bài toán**:
  1. *Quy luật phân rã beta và điều kiện năng lượng*: Khảo sát biến đổi của $Z$, $N$, $A$ trong phân rã $\beta^-$ và $\beta^+$, xác định điều kiện tự phát của từng quá trình.
  2. *Phương trình vi phân cân bằng*: Thiết lập $\mathrm{d}N/\mathrm{d}t$ từ hiệu số giữa tốc độ sinh $R$ và tốc độ phân rã $\lambda N$, phân tích trạng thái dừng khi hai tốc độ cân bằng nhau.
  3. *Hệ biến mục tiêu*: Liệt kê các đại lượng đã biết và chưa biết cho từng phần của bài toán.
- **Thực hiện giải toán**:
  4. *Xác định nuclide con*: Tính $Z'$ và $N'$ từ định luật bảo toàn điện tích và số nucleon để nhận diện nguyên tố hóa học.
  5. *Đánh giá tính khả dĩ của phân rã ngược*: So sánh năng lượng phân rã và rào cản ngưỡng $2 m_e$ để kết luận về khả năng xảy ra phân rã $\beta^+$.
  6. *Tính toán trạng thái bão hòa*: Giải điều kiện dừng $\mathrm{d}N/\mathrm{d}t = 0$ để tìm số hạt cực đại $N_{\max}$ và hoạt độ bão hòa $A_{\max}$.
  7. *Tích phân giải phương trình động học*: Giải phương trình vi phân biến thiên số hạt $N(t)$ bằng phương pháp tách biến, sử dụng sự tương đồng toán học với quá trình nạp điện cho tụ điện (Mục 26.4).
- **Đánh giá kết quả**:
  8. *Kiểm tra tính nhất quán và giới hạn thời gian*: So sánh nghiệm $N(t)$ ở giới hạn thời gian dài $t \to \infty$ với trạng thái dừng ở Bước 6, và xác định khoảng thời gian cụ thể được coi là "thời gian dài".

**Lời giải chi tiết:**

**Bước 1: Quy luật phân rã beta và điều kiện năng lượng**
Trong một phân rã beta trừ ($\beta^-$), một neutron trong hạt nhân biến đổi thành một proton. Đồng thời, phát ra một electron và một antineutrino electron. Do đó:
- Số khối $A$ không thay đổi ($\Delta A = 0$).
- Số proton tăng thêm 1 đơn vị ($Z \to Z + 1$).
- Số neutron giảm đi 1 đơn vị ($N \to N - 1$).

Điều kiện để phân rã $\beta^-$ xảy ra tự phát là khối lượng nguyên tử của hạt nhân mẹ phải lớn hơn khối lượng nguyên tử của hạt nhân con: $m(X) > m(Y)$.

Ngược lại, trong phân rã beta cộng ($\beta^+$), một proton biến đổi thành một neutron, phát ra một positron và một neutrino electron ($Z \to Z - 1$, $N \to N + 1$). Điều kiện năng lượng để phân rã $\beta^+$ xảy ra tự phát là khối lượng nguyên tử hạt nhân mẹ phải lớn hơn khối lượng nguyên tử hạt nhân con ít nhất bằng hai lần khối lượng nghỉ của electron:
$$
m(X) - m(Y) > 2 m_e
$$

Nếu hiệu khối lượng nhỏ hơn $2 m_e$, phản ứng sẽ thu năng lượng và không thể xảy ra tự phát.

**Bước 2: Thiết lập phương trình cân bằng vi phân**
Số hạt nhân $^{128}\mathrm{I}$ trong mẫu chịu ảnh hưởng đồng thời bởi hai quá trình:
- Quá trình tạo thành do chùm neutron chiếu xạ với tốc độ không đổi $R = 1{,}50 \times 10^6\,\mathrm{s^{-1}}$.
- Quá trình phân rã phóng xạ với tốc độ phân rã tức thời $\lambda N(t)$.

Phương trình vi phân mô tả tốc độ biến thiên tổng cộng của số hạt nhân $N(t)$ trong mẫu là:
$$
\frac{\mathrm{d}N}{\mathrm{d}t} = R - \lambda N
$$

Ở trạng thái dừng (bão hòa), tốc độ sinh bằng đúng tốc độ phân rã. Điều này khiến số hạt nhân trong mẫu không còn thay đổi theo thời gian.

**Bước 3: Xác định các biến mục tiêu**
- Biến trạng thái: Hàm số $N(t)$ biểu thị số lượng hạt nhân $^{128}\mathrm{I}$ tại thời điểm $t$.
- Các đại lượng cần tìm:
  - Hạt nhân con của phân rã $\beta^-$.
  - Khả năng phân rã $\beta^+$ ngược lại.
  - Số hạt nhân cực đại $N_{\max}$ và hoạt độ bão hòa $A_{\max}$.
  - Dạng giải tích của hàm $N(t)$.

**Bước 4: Xác định nuclide con (Phần a)**
Hạt nhân $^{128}\mathrm{I}$ có $Z = 53$ và $A = 128$. Số neutron ban đầu là:
$$
N_{\mathrm{n}} = 128 - 53 = 75
$$

Khi phân rã $\beta^-$, số khối $A = 128$ giữ nguyên, số proton trở thành $Z' = 53 + 1 = 54$, và số neutron trở thành $N' = 75 - 1 = 74$. Nguyên tố có số hiệu nguyên tử $Z = 54$ trong bảng tuần hoàn là Xenon ($\mathrm{Xe}$). Vậy hạt nhân con tạo thành là $^{128}_{54}\mathrm{Xe}$.

Phương trình phân rã hạt nhân là:
$$
^{128}_{53}\mathrm{I} \to {^{128}_{54}\mathrm{Xe}} + \mathrm{e}^- + \bar{\nu}_e
$$

**Bước 5: Khảo sát khả năng phân rã beta cộng đảo ngược (Phần b)**
Để hạt nhân $^{128}_{54}\mathrm{Xe}$ có thể phân rã ngược lại thành $^{128}_{53}\mathrm{I}$ bằng phát xạ $\beta^+$, phản ứng giả định phải là:
$$
^{128}_{54}\mathrm{Xe} \to {^{128}_{53}\mathrm{I}} + \mathrm{e}^+ + \nu_e
$$

Vì phản ứng phân rã $\beta^-$ thuận xảy ra tự phát, năng lượng giải phóng là dương ($Q_{\beta^-} > 0$), đồng nghĩa với việc khối lượng nguyên tử mẹ phải lớn hơn hạt nhân con:
$$
m_{\mathrm{I}} > m_{\mathrm{Xe}}
$$

Để phản ứng phân rã $\beta^+$ ngược lại có thể xảy ra tự phát, điều kiện năng lượng đòi hỏi khối lượng nguyên tử $^{128}\mathrm{Xe}$ phải lớn hơn khối lượng $^{128}\mathrm{I}$ ít nhất bằng hai lần khối lượng electron:
$$
m_{\mathrm{Xe}} - m_{\mathrm{I}} > 2 m_e
$$

Tuy nhiên, vì $m_{\mathrm{Xe}} < m_{\mathrm{I}}$, hiệu khối lượng phản ứng mang dấu âm:
$$
\Delta m = m_{\mathrm{Xe}} - m_{\mathrm{I}} - 2 m_e
$$

Do $\Delta m < 0$, kéo theo năng lượng phân rã ngược mang giá trị âm:
$$
Q_{\beta^+} = \Delta m \cdot c^2 < 0
$$

Quá trình phân rã ngược này là phản ứng thu năng lượng (endoergic) và bị cấm tuyệt đối theo định luật bảo toàn năng lượng. Hạt nhân $^{128}\mathrm{Xe}$ hoàn toàn không thể tự phát phân rã ngược lại thành $^{128}\mathrm{I}$ bằng phát xạ $\beta^+$.
(Khối lượng thực tế tra cứu từ bảng đồng vị là $m(^{128}\mathrm{Xe}) = 127{,}903531\,\mathrm{u}$ và $m(^{128}\mathrm{I}) = 127{,}904587\,\mathrm{u}$, cho độ hụt khối $\Delta m \approx -0{,}002153\,\mathrm{u} < 0$).

**Bước 6: Xác định trạng thái bão hòa (Phần c)**
Tại trạng thái bão hòa (steady state), số hạt nhân $^{128}\mathrm{I}$ đạt giá trị dừng không đổi. Do đó, đạo hàm theo thời gian triệt tiêu:
$$
\frac{\mathrm{d}N}{\mathrm{d}t} = 0
$$

Thay vào phương trình vi phân:
$$
R - \lambda N_{\max} = 0
$$
$$
N_{\max} = \frac{R}{\lambda}
$$

Hằng số phân rã của $^{128}\mathrm{I}$ được tính từ chu kỳ bán rã:
$$
\lambda = \frac{\ln 2}{T_{1/2}}
$$

Thay số với chu kỳ $T_{1/2} = 1500\,\mathrm{s}$:
$$
\lambda = \frac{\ln 2}{1500\,\mathrm{s}}
$$
$$
\lambda \approx 4{,}621 \times 10^{-4}\,\mathrm{s^{-1}}
$$

Số nguyên tử $^{128}\mathrm{I}$ cực đại có mặt trong mẫu khi đạt bão hòa là:
$$
N_{\max} = \frac{1{,}50 \times 10^6}{4{,}621 \times 10^{-4}}
$$
$$
N_{\max} \approx 3{,}25 \times 10^9
$$

Hoạt độ phóng xạ của mẫu tại trạng thái bão hòa bằng:
$$
A_{\max} = \lambda N_{\max} = R
$$
$$
A_{\max} = 1{,}50 \times 10^6\,\mathrm{Bq}
$$

Hoạt độ phóng xạ cực đại đạt được chính bằng tốc độ bắn phá tạo thành hạt nhân mới từ chùm neutron.

**Bước 7: Giải phương trình vi phân tìm N(t) (Phần d)**
Phương trình vi phân $\mathrm{d}N/\mathrm{d}t + \lambda N = R$ có cấu trúc toán học tương tự như phương trình nạp điện cho tụ điện qua điện trở trong mạch $RC$ (Mục 26.4), trong đó số lượng hạt nhân $N(t)$ đóng vai trò tương đương điện tích tụ điện $q(t)$, tốc độ sinh $R$ tương đương dòng nạp giới hạn $\mathcal{E}/R_{\mathrm{c}}$, và hằng số phân rã $\lambda$ đóng vai trò tương đương nghịch đảo thời hằng $1/(RC)$.

Viết lại phương trình dưới dạng tách biến:
$$
\frac{\mathrm{d}N}{N - R/\lambda} = -\lambda\,\mathrm{d}t
$$

Lấy tích phân hai vế từ thời điểm ban đầu $t = 0$ (khi $N = 0$) đến thời điểm $t$:
$$
\ln\left(1 - \frac{\lambda N}{R}\right) = -\lambda t
$$

Lấy hàm mũ hai vế:
$$
1 - \frac{\lambda N}{R} = \mathrm{e}^{-\lambda t}
$$

Suy ra biểu thức số hạt nhân $^{128}\mathrm{I}$ theo thời gian:
$$
N(t) = \frac{R}{\lambda}\left(1 - \mathrm{e}^{-\lambda t}\right)
$$

Biểu thức này mô tả sự tích tụ hạt nhân tiến tới bão hòa với giá trị cực đại $N_{\max} \approx 3{,}25 \times 10^9$ và hằng số phân rã $\lambda \approx 4{,}62 \times 10^{-4}\,\mathrm{s^{-1}}$.

![Đồ thị hàm số N(t) tích lũy số hạt nhân 128I tiến tới bão hòa](./img/young-43/loi-giai-d-08.svg)

**Bước 8: Đánh giá và kiểm tra giới hạn thời gian**
Kiểm tra tính nhất quán của nghiệm $N(t)$:
- Khi $t = 0$: $N(0) = \frac{R}{\lambda}(1 - 1) = 0$, hoàn toàn phù hợp với điều kiện ban đầu của bài toán.
- Khi thời gian nhỏ ($t \ll 1/\lambda$): Áp dụng khai triển xấp xỉ $\mathrm{e}^{-\lambda t} \approx 1 - \lambda t$, ta thu được $N(t) \approx \frac{R}{\lambda}(\lambda t) = R t$. Trong giai đoạn đầu, sự phân rã chưa đáng kể và số hạt nhân tăng tuyến tính theo thời gian với tốc độ sinh $R$.
- Khi thời gian rất lớn ($t \to \infty$): Số hạng $\mathrm{e}^{-\lambda t} \to 0$, khi đó $N(t) \to R/\lambda = N_{\max}$. Kết quả này hoàn toàn đồng nhất với giá trị bão hòa tìm được từ phân tích trạng thái dừng ở Bước 6.

Để xác định khoảng thời gian được coi là "thời gian dài":
- Sau khoảng $5$ chu kỳ bán rã ($t = 5 T_{1/2} = 125\,\mathrm{min}$, khoảng hơn $2\,\mathrm{h}$):
$$
\mathrm{e}^{-\lambda t} = \left(\frac{1}{2}\right)^5 = \frac{1}{32}
$$
Lượng hạt nhân đã đạt $(1 - 1/32) \approx 96{,}9\%$ giá trị bão hòa.
- Sau $7$ chu kỳ bán rã ($t = 7 T_{1/2} = 175\,\mathrm{min} \approx 2{,}9\,\mathrm{h}$), mẫu đạt trên $99{,}2\%$ giá trị bão hòa.

Vì vậy, trong điều kiện thí nghiệm này, một khoảng thời gian dài hơn khoảng $2$ đến $3$ giờ được coi là "thời gian dài", khi đó mẫu thực tế đã đạt trạng thái bão hòa hoàn toàn.

**Kết luận:**
(a) Hạt nhân con là $^{128}_{54}\mathrm{Xe}$.
(b) Không thể phân rã ngược lại thành $^{128}\mathrm{I}$ vì phản ứng ngược là thu năng lượng ($Q < 0$).
(c) $N_{\max} \approx 3{,}25 \times 10^9$ nguyên tử. $A_{\max} = 1{,}50 \times 10^6\,\mathrm{Bq}$.
(d) $N(t) = \frac{R}{\lambda}(1 - \mathrm{e}^{-\lambda t})$, với $N_{\max} \approx 3{,}25 \times 10^9$ và $\lambda \approx 4{,}62 \times 10^{-4}\,\mathrm{s^{-1}}$.

</details>
