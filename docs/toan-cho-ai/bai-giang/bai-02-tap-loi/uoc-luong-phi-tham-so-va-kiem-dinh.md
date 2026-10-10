---
course: toan-cho-ai
lecture: bai-02-tap-loi
topic: uoc-luong-phi-tham-so-va-kiem-dinh
section: topic
title: "Ước lượng phi tham số và thiết kế bộ phát hiện"
description: "Ước lượng hàm mật độ cực đại likelihood với ràng buộc hình dạng, phân phối cực đại entropy dưới ràng buộc mô-men, lý thuyết kiểm định giả thuyết thống kê và thiết kế bộ phát hiện tối ưu minimax qua quy hoạch tuyến tính."
---

Trong học máy và phân tích dữ liệu, việc áp đặt một phân phối tham số cố định (chẳng hạn như phân phối chuẩn Gauss) đôi khi phản ánh sai lệch bản chất dữ liệu, dẫn tới những quyết định sai lầm trong các hệ thống phát hiện gian lận, chẩn đoán y khoa hay radar. Khi không có lý do vững chắc để chọn một họ phân phối cụ thể, phương pháp phi tham số (nonparametric) cho phép hàm phân phối tự do thích ứng với dữ liệu, chỉ chịu sự ràng buộc bởi các tính chất định tính như tính đơn điệu, tính lõm logarit hay các mô-men thống kê quan sát được.

Chủ đề này khảo sát các bài toán tối ưu lồi trong ước lượng mật độ phi tham số, bài toán cực đại hóa entropy thông tin của Boltzmann–Gibbs, và phương pháp thiết kế bộ phát hiện tối ưu (detector design) theo tiêu chuẩn Minimax và Neyman–Pearson.

## 1. Ước lượng mật độ phi tham số (Nonparametric Density Estimation)

Xét biến ngẫu nhiên $X$ nhận giá trị trong một tập hữu hạn các trạng thái rời rạc $\{x_1, x_2, \dots, x_n\}$ với phân phối xác suất tương ứng $p = (p_1, \dots, p_n)^T$, trong đó $p_i = \mathbb{P}(X = x_i)$. Điều kiện tiên quyết là $p$ phải thuộc đơn hình xác suất:

$$
p \succeq 0, \qquad \mathbf{1}^T p = \sum_{i=1}^n p_i = 1.
$$

Giả sử ta quan sát được một mẫu độc lập gồm $m$ giá trị, trong đó trạng thái $x_k$ xuất hiện với tần số $m_k$ (với $\sum_{k=1}^n m_k = m$). Hàm log-likelihood của mẫu dữ liệu là:

$$
\ell(p) = \sum_{k=1}^n m_k \log p_k.
$$

Vì hàm logarit lõm, $\ell(p)$ là một hàm lõm nghiêm ngặt trên tập xác định $p \succ 0$. Bài toán cực đại hóa log-likelihood tương đương với cực tiểu hóa hàm lồi $-\ell(p)$.

### Ràng buộc hình dạng tiên nghiệm
Nếu không có thêm ràng buộc nào, nghiệm cực đại log-likelihood chỉ đơn giản là phân phối tần suất thực nghiệm $p_k^* = m_k / m$. Tuy nhiên, phương pháp phi tham số thể hiện sức mạnh vượt trội khi ta lồng ghép các giả thiết hình thái vật lý:

1. **Ràng buộc đơn điệu (Monotonicity)**: Nếu biết trước xác suất giảm dần theo độ lớn của biến cố (chẳng hạn thời gian chờ đợi hỏng hóc của linh kiện), ta áp đặt hệ ràng buộc:
   $$
   p_1 \ge p_2 \ge \dots \ge p_n \ge 0.
   $$
   Đây là một tập các bất đẳng thức tuyến tính, dẫn đến bài toán ước lượng Grenander nổi tiếng, có thể giải chính xác bằng Quy hoạch tuyến tính hoặc thuật toán hồ chứa đẳng trương (Isotonic regression).

2. **Ràng buộc lõm logarit (Log-concavity)**: Nhiều phân phối thực tế (Gauss, Laplace, Exponential, Logistic) đều có hàm mật độ lõm logarit. Trên lưới đều $x_{k+1} - x_k = h$, tính lõm logarit của phân phối rời rạc được đặc tả bởi:
   $$
   p_k^2 \ge p_{k-1} p_{k+1} \iff 2 \log p_k \ge \log p_{k-1} + \log p_{k+1}, \quad \forall k = 2, \dots, n-1.
   $$
   Bằng cách đổi biến $y_k = \log p_k$, hệ ràng buộc này trở thành các bất đẳng thức tuyến tính $2 y_k - y_{k-1} - y_{k+1} \ge 0$, và bài toán ước lượng chuyển hóa thành quy hoạch lồi đối với vector $y$.

## 2. Phân phối cực đại Entropy (Maximum Entropy Distributions)

Nguyên lý cực đại entropy của Jaynes khẳng định: Khi chỉ biết một số thông tin hạn chế về một phân phối xác suất (chẳng hạn như kỳ vọng hoặc phương sai), phân phối khách quan và trung thực nhất chính là phân phối tối đa hóa độ hỗn loạn thông tin (Shannon entropy), không thiên vị bất kỳ giả định ngầm nào khác.

Độ đo entropy của phân phối rời rạc $p$ được định nghĩa là:

$$
H(p) = -\sum_{i=1}^n p_i \log p_i.
$$

Xét bài toán cực đại hóa entropy dưới các ràng buộc mô-men thực nghiệm $\mathbb{E}[f_j(X)] = \alpha_j$ với $j = 1, \dots, k$:

$$
\begin{aligned}
\text{minimize}\quad & \sum_{i=1}^n p_i \log p_i \\
\text{subject to}\quad & \sum_{i=1}^n p_i f_j(x_i) = \alpha_j, \quad j = 1, \dots, k, \\
& \sum_{i=1}^n p_i = 1, \\
& p \succeq 0.
\end{aligned}
$$

Thiết lập hàm Lagrangian với nhân tử $\nu_0$ cho ràng buộc tổng xác suất và $\nu \in \mathbb{R}^k$ cho các ràng buộc mô-men:

$$
L(p, \nu_0, \nu) = \sum_{i=1}^n p_i \log p_i + \nu_0 \left(\sum_{i=1}^n p_i - 1\right) + \sum_{j=1}^k \nu_j \left(\sum_{i=1}^n p_i f_j(x_i) - \alpha_j\right).
$$

Lấy đạo hàm riêng theo $p_i$ và đặt bằng 0:

$$
\frac{\partial L}{\partial p_i} = \log p_i + 1 + \nu_0 + \sum_{j=1}^k \nu_j f_j(x_i) = 0.
$$

Suy ra dạng giải tích của phân phối nghiệm tối ưu:

$$
p_i^* = \exp\left(-(1 + \nu_0) - \sum_{j=1}^k \nu_j f_j(x_i)\right) = \frac{1}{Z(\nu)} \exp\left(-\sum_{j=1}^k \nu_j f_j(x_i)\right),
$$

trong đó $Z(\nu) = \sum_{i=1}^n \exp\left(-\sum_{j=1}^k \nu_j f_j(x_i)\right)$ là hàm phân giải (partition function). Nghiệm cực đại entropy luôn tự nhiên thuộc **họ hàm mũ (Exponential Family)** hay phân phối Boltzmann–Gibbs, đóng vai trò nền tảng trong vật lý thống kê và mô hình sinh ngẫu nhiên của AI.

## 3. Thiết kế bộ phát hiện và Kiểm định giả thuyết (Detector Design)

Trong bài toán xử lý tín hiệu và chẩn đoán, ta cần quyết định xem một quan sát đo đạc $y \in \{1, \dots, m\}$ xuất phát từ giả thuyết nào trong hai giả thuyết:
- $H_1$: Tín hiệu thực sự xuất hiện (hoặc người bệnh có khối u).
- $H_2$: Chỉ có tạp âm nền (hoặc người hoàn toàn khỏe mạnh).

Phân phối xác suất của quan sát $y$ dưới mỗi giả thuyết được cho bởi hai vector xác suất đã biết:

$$
p_j = \mathbb{P}(y \mid H_j), \qquad j = 1, 2.
$$

Một **bộ phát hiện ngẫu nhiên hóa (randomized detector)** được đặc tả bởi ma trận $T \in \mathbb{R}^{2 \times m}$, trong đó $T_{iy}$ là xác suất bộ phát hiện quyết định chọn giả thuyết $H_i$ khi quan sát được giá trị $y$. Vì $T$ là phân phối có điều kiện:

$$
T_{1y} + T_{2y} = 1, \qquad T_{1y} \ge 0, \quad T_{2y} \ge 0, \quad \forall y = 1, \dots, m.
$$

### Xác suất lỗi
- **Xác suất báo động giả (False alarm probability)**: Quyết định $H_1$ khi thực tế là $H_2$:
  $$
  P_{\text{fa}} = \sum_{y=1}^m T_{1y} p_{2}(y) = T_1 p_2.
  $$
- **Xác suất bỏ sót (Miss probability)**: Quyết định $H_2$ khi thực tế là $H_1$:
  $$
  P_{\text{m}} = \sum_{y=1}^m T_{2y} p_{1}(y) = T_2 p_1 = 1 - T_1 p_1.
  $$

### Bộ phát hiện Minimax
Nếu không biết trước xác suất tiên nghiệm của các giả thuyết, một tiêu chuẩn thiết kế an toàn là tối thiểu hóa xác suất lỗi tồi tệ nhất (Minimax error):

$$
\text{minimize}\quad \max\{ P_{\text{fa}}, P_{\text{m}} \}.
$$

Đặt biến phụ $t$ qua kỹ thuật epigraph, bài toán đưa trực tiếp về Quy hoạch tuyến tính (LP):

$$
\begin{aligned}
\text{minimize}\quad & t \\
\text{subject to}\quad & \sum_{y=1}^m T_{1y} p_2(y) \le t, \\
& 1 - \sum_{y=1}^m T_{1y} p_1(y) \le t, \\
& 0 \le T_{1y} \le 1, \quad y = 1, \dots, m.
\end{aligned}
$$

### Bộ phát hiện Neyman–Pearson
Trong thực tế y tế hoặc an ninh quốc phòng, ta thường khống chế xác suất báo động giả dưới một ngưỡng an toàn $\alpha$ (ví dụ: $\alpha = 0{,}05$), đồng thời tối đa hóa xác suất phát hiện đúng $P_{\text{d}} = 1 - P_{\text{m}}$:

$$
\begin{aligned}
\text{maximize}\quad & \sum_{y=1}^m T_{1y} p_1(y) \\
\text{subject to}\quad & \sum_{y=1}^m T_{1y} p_2(y) \le \alpha, \\
& 0 \le T_{1y} \le 1, \quad y = 1, \dots, m.
\end{aligned}
$$

Đây là bài toán LP thuần túy đối với các biến $T_{1y}$, và điều kiện tối ưu đối ngẫu của nó dẫn chính xác tới bổ đề Neyman–Pearson kinh điển: So sánh tỉ số hợp lý (likelihood ratio) $p_1(y) / p_2(y)$ với một ngưỡng quyết định.

## 4. Bài tập tự luyện

::: exercise 1. Phân phối cực đại Entropy trên ba trạng thái
Xét biến ngẫu nhiên rời rạc $X$ nhận các giá trị trong tập $\{-1, 0, 1\}$ với phân phối $p = (p_1, p_2, p_3)^T$. Ta biết kỳ vọng toán học $\mathbb{E}[X] = 0{,}2$.
1. Thiết lập bài toán cực đại hóa entropy thông tin dưới ràng buộc kỳ vọng và tổng xác suất bằng 1.
2. Tìm dạng biểu thức của các xác suất $p_1^*, p_2^*, p_3^*$ theo tham số đối ngẫu $\nu$.
3. Giải phương trình đối ngẫu để tìm chính xác giá trị số học của vector xác suất tối ưu $p^*$.
:::

::: solution
1. **Thiết lập bài toán**:
   Biểu thức kỳ vọng: Ta có $\mathbb{E}[X] = p_3 - p_1 = 0{,}2$.
   Bài toán cực tiểu hóa hàm lồi:
   $$
   \begin{aligned}
   \text{minimize}\quad & p_1 \log p_1 + p_2 \log p_2 + p_3 \log p_3 \\
   \text{subject to}\quad & p_3 - p_1 = 0{,}2, \\
   & p_1 + p_2 + p_3 = 1, \\
   & p_1, p_2, p_3 \ge 0.
   \end{aligned}
   $$

2. **Dạng nghiệm theo tham số đối ngẫu**:
   Theo lý thuyết phân phối cực đại entropy:
   $$
   p_i^* \propto \exp(-\nu x_i) \implies p_1 = C e^{\nu}, \quad p_2 = C, \quad p_3 = C e^{-\nu},
   $$
   với hằng số chuẩn hóa $C = \frac{1}{e^\nu + 1 + e^{-\nu}}$.
   Đặt $u = e^{-\nu} > 0$, ta có:
   $$
   p_1 = \frac{1/u}{u + 1 + 1/u} = \frac{1}{u^2 + u + 1}, \quad p_2 = \frac{u}{u^2 + u + 1}, \quad p_3 = \frac{u^2}{u^2 + u + 1}.
   $$

3. **Giải tham số $u$**:
   Ràng buộc kỳ vọng: $p_3 - p_1 = 0{,}2 = 1/5$:
   $$
   \frac{u^2 - 1}{u^2 + u + 1} = \frac{1}{5} \implies 5(u^2 - 1) = u^2 + u + 1 \implies 4u^2 - u - 6 = 0.
   $$
   Phương trình bậc hai có biệt thức: $\Delta = (-1)^2 - 4(4)(-6) = 1 + 96 = 97$.
   Vì $u > 0$, ta chọn nghiệm dương:
   $$
   u = \frac{1 + \sqrt{97}}{8} \approx \frac{1 + 9{,}8489}{8} \approx 1{,}3561.
   $$
   Tính mẫu số:
   $$
   u^2 + u + 1 \approx (1{,}3561)^2 + 1{,}3561 + 1 \approx 1{,}8390 + 1{,}3561 + 1 = 4{,}1951.
   $$
   Các xác suất tối ưu:
   $$
   \begin{aligned}
   p_1^* &= \frac{1}{4{,}1951} \approx 0{,}2384, \\
   p_2^* &= \frac{1{,}3561}{4{,}1951} \approx 0{,}3233, \\
   p_3^* &= \frac{1{,}8390}{4{,}1951} \approx 0{,}4384.
   \end{aligned}
   $$
   Kiểm tra: Tổng các xác suất là $p_1 + p_2 + p_3 \approx 1{,}0001 \approx 1$, và độ lệch kỳ vọng là $p_3 - p_1 = 0{,}2000$.
:::

::: exercise 2. Thiết kế bộ phát hiện Neyman–Pearson nhị phân
Cho biến quan sát $y \in \{1, 2, 3\}$ với bảng phân phối xác suất dưới hai giả thuyết:
- Dưới $H_1$ (tín hiệu): $p_1 = (0{,}1, \; 0{,}3, \; 0{,}6)^T$.
- Dưới $H_2$ (nhiễu): $p_2 = (0{,}5, \; 0{,}4, \; 0{,}1)^T$.
Mục tiêu là thiết kế bộ phát hiện $T_1 = (T_{11}, T_{12}, T_{13})^T \in [0, 1]^3$ để tối đa hóa xác suất phát hiện đúng $P_{\text{d}} = T_1^T p_1$ với điều kiện xác suất báo động giả $P_{\text{fa}} = T_1^T p_2 \le 0{,}2$.
1. Tính tỉ số hợp lý $L(y) = p_1(y) / p_2(y)$ tại mỗi giá trị quan sát $y \in \{1, 2, 3\}$.
2. Viết bài toán Quy hoạch tuyến tính (LP) tường minh.
3. Giải bài toán để tìm bộ phát hiện tối ưu $T_1^*$ và tính xác suất phát hiện cực đại.
:::

::: solution
1. **Tính tỉ số hợp lý $L(y)$**:
   - Tại $y = 1$: $L(1) = \frac{p_1(1)}{p_2(1)} = \frac{0{,}1}{0{,}5} = 0{,}2$.
   - Tại $y = 2$: $L(2) = \frac{p_1(2)}{p_2(2)} = \frac{0{,}3}{0{,}4} = 0{,}75$.
   - Tại $y = 3$: $L(3) = \frac{p_1(3)}{p_2(3)} = \frac{0{,}6}{0{,}1} = 6{,}0$.
   Thứ tự ưu tiên phát hiện theo mức độ tin cậy giảm dần: $y = 3$ (ưu tiên 1), $y = 2$ (ưu tiên 2), $y = 1$ (ưu tiên 3).

2. **Bài toán Quy hoạch tuyến tính**:
   $$
   \begin{aligned}
   \text{maximize}\quad & 0{,}1 T_{11} + 0{,}3 T_{12} + 0{,}6 T_{13} \\
   \text{subject to}\quad & 0{,}5 T_{11} + 0{,}4 T_{12} + 0{,}1 T_{13} \le 0{,}2, \\
   & 0 \le T_{11} \le 1, \\
   & 0 \le T_{12} \le 1, \\
   & 0 \le T_{13} \le 1.
   \end{aligned}
   $$

3. **Giải bài toán**:
   Đây là bài toán ba-lô liên tục (fractional knapsack): Ta ưu tiên gán giá trị lớn nhất cho biến có hiệu quả tỉ số $p_1(y)/p_2(y)$ cao nhất.
   - Chọn $T_{13} = 1$:
     - Ngân sách báo động giả đã dùng: $0{,}1 \times 1 = 0{,}1 \le 0{,}2$.
     - Ngân sách còn lại: $0{,}2 - 0{,}1 = 0{,}1$.
   - Tiếp tục xét $y = 2$ (tỉ số $0{,}75$):
     - Ta có thể tăng $T_{12}$ cho tới khi chạm trần ngân sách:
     $$
     0{,}4 T_{12} = 0{,}1 \implies T_{12} = \frac{0{,}1}{0{,}4} = 0{,}25.
     $$
   - Khi đó toàn bộ ngân sách báo động giả $0{,}2$ đã cạn kiệt, buộc phải đặt $T_{11} = 0$.
   
   Vậy bộ phát hiện Neyman–Pearson tối ưu là:
   $$
   T_1^* = \begin{bmatrix} 0 \\ 0{,}25 \\ 1 \end{bmatrix}.
   $$
   Ý nghĩa: Khi đo được $y = 3$, chắc chắn kết luận có tín hiệu ($T_{13} = 1$). Khi đo được $y = 2$, tung đồng xu ngẫu nhiên với xác suất $25\%$ kết luận có tín hiệu. Khi đo được $y = 1$, luôn kết luận chỉ là nhiễu ($T_{11} = 0$).
   
   Xác suất phát hiện tối đa đạt được:
   $$
   P_{\text{d}}^* = 0{,}1(0) + 0{,}3(0{,}25) + 0{,}6(1) = 0 + 0{,}075 + 0{,}6 = 0{,}675 \; (67{,}5\%).
   $$
:::

::: exercise 3. Ước lượng phân phối đơn điệu rời rạc (Grenander)
Xét biến ngẫu nhiên nhận giá trị trong $\{1, 2, 3\}$. Quan sát được tần số xuất hiện của ba giá trị lần lượt là $m = (1, 5, 4)$ trên tổng số 10 quan sát. Giả thiết rằng phân phối thực sự thỏa mãn tính đơn điệu không tăng: $p_1 \ge p_2 \ge p_3 \ge 0$.
1. Thiết lập bài toán tối ưu lồi cực đại hóa log-likelihood.
2. Kiểm tra xem nghiệm tự do không ràng buộc $p_{\text{emp}} = (0{,}1, 0{,}5, 0{,}4)$ có thỏa mãn ràng buộc đơn điệu không.
3. Tìm nghiệm tối ưu $p^*$ của bài toán.
:::

::: solution
1. **Thiết lập bài toán**:
   Hàm log-likelihood:
   $$
   \ell(p) = 1 \log p_1 + 5 \log p_2 + 4 \log p_3.
   $$
   Bài toán tối ưu lồi:
   $$
   \begin{aligned}
   \text{maximize}\quad & \log p_1 + 5 \log p_2 + 4 \log p_3 \\
   \text{subject to}\quad & p_1 \ge p_2, \\
   & p_2 \ge p_3, \\
   & p_3 \ge 0, \\
   & p_1 + p_2 + p_3 = 1.
   \end{aligned}
   $$

2. **Kiểm tra nghiệm thực nghiệm**:
   Nghiệm tần suất thực nghiệm là $p_{\text{emp}} = (0{,}1, 0{,}5, 0{,}4)$.
   Ta thấy $p_1 = 0{,}1 < p_2 = 0{,}5$, vi phạm nghiêm trọng ràng buộc đơn điệu $p_1 \ge p_2$. Do đó ràng buộc $p_1 \ge p_2$ bắt buộc phải chặt tại nghiệm tối ưu ($p_1 = p_2$).

3. **Tìm nghiệm tối ưu**:
   - Giả sử $p_1 = p_2 > p_3$:
     Đặt $p_1 = p_2 = q$. Khi đó $p_3 = 1 - 2q$.
     Điều kiện đơn điệu: $q \ge 1 - 2q \implies 3q \ge 1 \implies q \ge 1/3$.
     Hàm mục tiêu theo biến $q$:
     $$
     f(q) = \log q + 5 \log q + 4 \log(1 - 2q) = 6 \log q + 4 \log(1 - 2q).
     $$
     Lấy đạo hàm và cho bằng 0:
     $$
     f'(q) = \frac{6}{q} - \frac{8}{1 - 2q} = 0 \implies 6(1 - 2q) = 8q \implies 6 - 12q = 8q \implies 20q = 6 \implies q = \frac{3}{10} = 0{,}3.
     $$
     Tuy nhiên, với $q = 0{,}3$, ta có $p_3 = 1 - 2(0{,}3) = 0{,}4$. Khi đó $p_1 = p_2 = 0{,}3 < p_3 = 0{,}4$, lại vi phạm ràng buộc $p_2 \ge p_3$!
   - Như vậy cả hai ràng buộc đều phải chặt: $p_1 = p_2 = p_3$.
     Vì tổng bằng 1, nghiệm duy nhất khả thi trên biên là:
     $$
     p_1^* = p_2^* = p_3^* = \frac{1}{3} \approx 0{,}3333.
     $$
   - So sánh giá trị mục tiêu với trường hợp biên khác: Mọi cấu hình đơn điệu khác đều cho log-likelihood thấp hơn. Vậy phân phối tối ưu là phân phối đều: $p^* = (1/3, 1/3, 1/3)^T$. Hiện tượng "san bằng" này là đặc trưng kinh điển của hồi quy đẳng trương Grenander khi mẫu số liệu ở đầu quá nhỏ so với các mẫu phía sau.
:::

## Tóm tắt

Ước lượng phi tham số và kiểm định giả thuyết minh chứng cho tính linh hoạt của tối ưu hóa lồi khi tiếp cận các bài toán thống kê thực nghiệm. Không cần gò ép dữ liệu vào các giả định phân phối nhân tạo, các ràng buộc hình dạng định tính như tính đơn điệu hay tính lõm logarit định hình một không gian tìm kiếm lồi tự nhiên cho bài toán cực đại hóa log-likelihood. 

Nguyên lý cực đại entropy thiết lập phân phối xác suất khách quan nhất dựa trên các mô-men thực nghiệm, trong khi lý thuyết kiểm định giả thuyết Minimax và Neyman–Pearson chuyển hóa hoàn toàn bài toán ra quyết định phát hiện tối ưu thành các bài toán Quy hoạch tuyến tính (LP) khả giải một cách hiệu quả và tin cậy.

## Tài liệu tham khảo

- Stephen Boyd, Lieven Vandenberghe, *Convex Optimization*, Cambridge University Press, Chapter 7: Statistical Estimation (§§7.2–7.3).
