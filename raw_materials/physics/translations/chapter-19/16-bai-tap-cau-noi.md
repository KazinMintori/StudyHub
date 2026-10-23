### Bài tập cầu nối: Công thực hiện bởi khí van der Waals

Phương trình trạng thái van der Waals mô tả gần đúng hành vi của chất khí ở áp suất cao thông qua các biến hiệu dụng:

$$
\begin{aligned}
&p_{\text{eff}} = p + \frac{an^2}{V^2}, \\
&V_{\text{eff}} = V - nb, \\
&p_{\text{eff}} V_{\text{eff}} = nRT.
\end{aligned}
$$

Trong đó $a$ và $b$ là các hằng số thực nghiệm có giá trị đặc trưng cho từng loại khí. Khi $a = b = 0$, phương trình trở về phương trình trạng thái khí lý tưởng. Xét quá trình đủ chậm để khí đi qua các trạng thái cân bằng, với $V>nb$ trên toàn bộ khoảng tích phân.

(a) Hãy thiết lập biểu thức tổng quát tính công thực hiện bởi chất khí tuân theo phương trình trạng thái van der Waals trong quá trình giãn nở đẳng nhiệt từ thể tích $V_1$ đến thể tích $V_2$.

(b) Đối với khí etan ($\text{C}_2\text{H}_6$), các hằng số van der Waals là:

$$
a = 0{,}554\,\text{J}\cdot\text{m}^3/\text{mol}^2
$$

$$
b = 6{,}38 \times 10^{-5}\,\text{m}^3/\text{mol}
$$

Tính công $W$ do $1{,}80\text{ mol}$ khí etan thực hiện khi giãn nở từ thể tích ban đầu $V_1 = 2{,}00 \times 10^{-3}\text{ m}^3$ đến thể tích cuối $V_2 = 4{,}00 \times 10^{-3}\text{ m}^3$ ở nhiệt độ không đổi $T = 300\text{ K}$. Thực hiện phép tính theo hai cách:
1. Sử dụng phương trình trạng thái van der Waals.
2. Sử dụng phương trình trạng thái khí lý tưởng.

(c) Trong hai mô hình phương trình trạng thái trên, công $W$ tính theo mô hình nào lớn hơn? Giải thích nguyên nhân vật lý của sự khác biệt này.

![Hình 19.22: Quá trình giãn nở đẳng nhiệt của chất khí.](./img/young-19/c-fig-19-22.png)

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**

- Lượng chất: $n = 1{,}80\text{ mol}$.
- Nhiệt độ đẳng nhiệt: $T = 300\text{ K}$.
- Thể tích ban đầu: $V_1 = 2{,}00 \times 10^{-3}\text{ m}^3$.
- Thể tích cuối: $V_2 = 4{,}00 \times 10^{-3}\text{ m}^3$.
- Hằng số van der Waals của etan:
  - $a = 0{,}554\,\text{J}\cdot\text{m}^3/\text{mol}^2$.
  - $b = 6{,}38 \times 10^{-5}\,\text{m}^3/\text{mol}$.
- Hằng số khí lý tưởng: $R = 8{,}314\,\text{J}/(\text{mol}\cdot\text{K})$.
- Cần tìm:
  - Biểu thức giải tích tổng quát của $W$.
  - Giá trị công $W_{\text{vdW}}$ theo mô hình van der Waals.
  - Giá trị công $W_{\text{ideal}}$ theo mô hình khí lý tưởng.
  - So sánh $W_{\text{ideal}}$ với $W_{\text{vdW}}$ và phân tích vai trò của hai tham số $a, b$.

**Hướng đi:**

- Nhận diện và thiết lập (Bước 1): Ý nghĩa vật lý của hai tham số van der Waals:
  - Hằng số $b$ hiệu chỉnh thể tích riêng bị chiếm bởi chính các phân tử khí. Thể tích không gian thực sự còn lại cho các phân tử chuyển động tự do giảm xuống còn $V_{\text{eff}} = V - nb$.
  - Hằng số $a$ đặc trưng cho lực hút tương hỗ giữa các phân tử khí gần nhau. Lực hút này kéo các phân tử về phía lòng khối khí, làm giảm áp suất va chạm lên thành bình một lượng bằng $a n^2 / V^2$.
- Nhận diện và thiết lập (Bước 2): Đối với chất khí tổng quát, công trong quá trình biến đổi thể tích từ $V_1$ đến $V_2$ luôn được tính bằng tích phân:

$$
W = \int_{V_1}^{V_2} p \, dV
$$

- Để thực hiện phép tính, cần rút áp suất $p$ theo biến thể tích $V$ từ phương trình trạng thái van der Waals ở nhiệt độ $T$ không đổi.
- Nhận diện và thiết lập (Bước 3): Đối với khí lý tưởng, tích phân đẳng nhiệt cho kết quả giải tích quen thuộc:

$$
W_{\text{ideal}} = nRT \ln(V_2 / V_1)
$$

**Lời giải chi tiết:**

Phần (a): Thiết lập biểu thức công tổng quát (Bước 4):

Từ phương trình trạng thái van der Waals:

$$
\begin{aligned}
p_{\text{eff}} &= p + \frac{an^2}{V^2} \\
p_{\text{eff}}(V - nb) &= nRT
\end{aligned}
$$

Chia cả hai vế cho $(V - nb)$ và chuyển vế, ta biểu diễn áp suất $p$ theo thể tích $V$:

$$
p = \frac{nRT}{V - nb} - \frac{an^2}{V^2}
$$

Công do chất khí thực hiện trong quá trình giãn nở đẳng nhiệt từ $V_1$ đến $V_2$ là:

$$
W = \int_{V_1}^{V_2} p \, dV
$$

Tách biểu thức thành hiệu hai tích phân thành phần:

$$
W = W_1 - W_2
$$

Với $W_1$ là công từ số hạng nhiệt phân tử:

$$
W_1 = \int_{V_1}^{V_2} \frac{nRT}{V - nb} \, dV
$$

$$
W_1 = nRT \left[ \ln(V - nb) \right]_{V_1}^{V_2}
$$

$$
W_1 = nRT \ln \frac{V_2 - nb}{V_1 - nb}
$$

Và $W_2$ là công từ số hạng lực hút tương hỗ:

$$
W_2 = \int_{V_1}^{V_2} \frac{an^2}{V^2} \, dV
$$

$$
W_2 = -an^2 \left[ \frac{1}{V} \right]_{V_1}^{V_2}
$$

$$
W_2 = -an^2 \left(\frac{1}{V_2} - \frac{1}{V_1}\right)
$$

Kết hợp lại, công toàn phần của khí van der Waals là:

$$
W = W_1 - W_2
$$

Kiểm tra tính tương thích: Khi cho $a = 0$ và $b = 0$, số hạng $W_1$ chuyển thành $nRT \ln(V_2 / V_1)$ và số hạng thứ hai triệt tiêu, biểu thức thu được trùng khớp chính xác với công của khí lý tưởng.

Phần (b): Tính toán bằng số cho khí etan:

Trường hợp (i): Tính theo phương trình van der Waals (Bước 5):

Tính số hạng hiệu chỉnh thể tích riêng $nb$:

$$
\begin{aligned}
nb &= 1{,}80 \times 6{,}38 \times 10^{-5} \\
&= 1{,}148 \times 10^{-4}\text{ m}^3
\end{aligned}
$$

Quy đổi ra cùng bậc độ lớn: $nb \approx 0{,}115 \times 10^{-3}\text{ m}^3$. Thể tích hiệu dụng ở hai trạng thái:

$$
V_1^{\prime} = V_1 - nb
$$

$$
V_1^{\prime} = 1{,}885 \times 10^{-3}\text{ m}^3
$$

$$
V_2^{\prime} = V_2 - nb
$$

$$
V_2^{\prime} = 3{,}885 \times 10^{-3}\text{ m}^3
$$

Tỷ số giãn nở thể tích hiệu dụng là:

$$
\frac{V_2^{\prime}}{V_1^{\prime}} = \frac{3{,}885}{1{,}885} \approx 2{,}061
$$

Tích số nhiệt năng $nRT$ với $n = 1{,}80\text{ mol}$, $T = 300\text{ K}$:

$$
nRT = 4489{,}6\text{ J}
$$

Giá trị của số hạng thứ nhất trong công van der Waals:

$$
\begin{aligned}
W_1 &= nRT \ln(V_2^{\prime} / V_1^{\prime}) \\
&= 4489{,}6 \times \ln(2{,}061) \\
&\approx 3247\text{ J}
\end{aligned}
$$

Tiếp theo, tính số hạng thứ hai do lực hút phân tử $a$:

$$
\begin{aligned}
an^2 &= 0{,}554 \times (1{,}80)^2 \\
&= 1{,}795\,\text{J}\cdot\text{m}^3
\end{aligned}
$$

Hiệu nghịch đảo thể tích giữa hai trạng thái với $V_1 = 2{,}00 \times 10^{-3}\text{ m}^3$ và $V_2 = 4{,}00 \times 10^{-3}\text{ m}^3$:

$$
\begin{aligned}
\frac{1}{V_2} - \frac{1}{V_1} &= 250 - 500 \\
&= -250\text{ m}^{-3}
\end{aligned}
$$

Giá trị của số hạng thứ hai là:

$$
\begin{aligned}
W_2^{\prime} &= an^2 \left(\frac{1}{V_2} - \frac{1}{V_1}\right) \\
&= 1{,}795 \times (-250) \\
&\approx -449\text{ J}
\end{aligned}
$$

Cộng hai thành phần để thu được công toàn phần của khí van der Waals:

$$
\begin{aligned}
W_{\text{vdW}} &= W_1 + W_2^{\prime} \\
&= 3247 - 449 \\
&= 2798\text{ J} \\
&\approx 2{,}80 \times 10^3\text{ J}
\end{aligned}
$$

Trường hợp (ii): Tính theo phương trình khí lý tưởng (Bước 6):

Với tỷ số thể tích lý tưởng $V_2 / V_1 = 2$, công thực hiện bởi khí lý tưởng ở cùng nhiệt độ $T = 300\text{ K}$:

$$
\begin{aligned}
W_{\text{ideal}} &= nRT \ln(V_2 / V_1) \\
&= 4489{,}6 \times \ln(2) \\
&\approx 3112\text{ J} \\
&\approx 3{,}11 \times 10^3\text{ J}
\end{aligned}
$$

Phần (c): Đánh giá và so sánh kết quả:

Độ chênh lệch giữa hai mô hình (Bước 7):

Chênh lệch công giữa khí lý tưởng và khí van der Waals là:

$$
\begin{aligned}
\Delta W &= W_{\text{ideal}} - W_{\text{vdW}} \\
&= 3112 - 2798 \\
&= 314\text{ J}
\end{aligned}
$$

Tỷ lệ chênh lệch tương đối đạt mức:

$$
\frac{\Delta W}{W_{\text{ideal}}} = \frac{314}{3112} \approx 10{,}1\%
$$

Sự khác biệt trên $10\%$ là rất đáng kể trong các tính toán kỹ thuật nhiệt và hóa công nghiệp. Ở áp suất cao và thể tích nhỏ, giả thiết khí lý tưởng dẫn đến sai số rõ rệt.

Phân tích ảnh hưởng của từng tham số van der Waals (Bước 8):

1. Vai trò của tham số $b$ (thể tích riêng phân tử):
   - Do các phân tử chiếm một phần không gian thực tế, khoảng trống khả dụng bị thu hẹp từ $V$ xuống $V - nb$.
   - Vì vậy tỷ số thể tích hiệu dụng tăng lên so với tỷ số thể tích hình học:

$$
\frac{V_2^{\prime}}{V_1^{\prime}} > \frac{V_2}{V_1}
$$

   - Hệ quả là số hạng chứa $b$ làm tăng công sinh ra thêm:

$$
3247 - 3112 = +135\text{ J}
$$

2. Vai trò của tham số $a$ (lực hút tương hỗ phân tử):
   - Lực hút giữa các phân tử cản trở sự phân tán và kéo các hạt lại gần nhau, làm giảm áp suất tác dụng lên mặt trong thành piston.
   - Khi thể tích tăng, chất khí phải thực hiện công cơ học để thắng lực hút tĩnh điện phân tử này, làm giảm công hữu ích sinh ra lên môi trường bên ngoài một lượng:

$$
W_2^{\prime} = -449\text{ J}
$$

3. So sánh mức độ chi phối:
   - Ảnh hưởng làm giảm công của lực hút phân tử ($|-449\text{ J}| = 449\text{ J}$) lớn hơn gấp ba lần so với ảnh hưởng làm tăng công của thể tích riêng phân tử ($+135\text{ J}$).
   - Do đó, hiệu ứng lực hút phân tử $a$ đóng vai trò chủ đạo, dẫn đến kết quả công thực hiện bởi khí van der Waals nhỏ hơn đáng kể so với khí lý tưởng:

$$
W_{\text{vdW}} < W_{\text{ideal}}
$$

</details>
