---
course: toan-cho-ai
lecture: bai-06-phuong-phap-thich-nghi
section: lecture
title: "Các phương pháp tối ưu trong học sâu"
prerequisites: ["gradient", "hessian", "ky-vong", "phuong-sai"]
lessonStatus: ready
description: "Cơ chế thích nghi từng tọa độ của AdaGrad, RMSProp và Adam; đối chiếu Newton, Gradient liên hợp (CG) và BFGS; phương pháp luận so sánh optimizer."
---

Một trong những thách thức lớn nhất khi huấn luyện mạng nơ-ron sâu là: **Các tham số khác nhau thường đòi hỏi tốc độ cập nhật hoàn toàn khác nhau**. Trong các mô hình ngôn ngữ lớn (LLM) hay hệ thống gợi ý, các đặc trưng hiếm (rare tokens/features) chỉ xuất hiện vài lần trong hàng triệu mẫu dữ liệu, khiến gradient của chúng rất nhỏ và thưa thớt. Ngược lại, các từ nối hay đặc trưng phổ biến xuất hiện liên tục với gradient dồn dập. Nếu ép toàn bộ mô hình dùng chung một tốc độ học $\eta$, các tham số hiếm sẽ hầu như không kịp học, trong khi các tham số phổ biến lại dao động dữ dội.

Lớp thuật toán tối ưu thích nghi (Adaptive Optimization), tiêu biểu là AdaGrad, RMSProp và Adam, giải quyết bài toán này bằng cách tự động gán cho mỗi tham số một tốc độ học riêng biệt, biến thiên linh hoạt theo lịch sử biến động của gradient.

Song song với đó, các phương pháp xấp xỉ bậc hai như **Gradient liên hợp (Conjugate Gradient - CG)** và **Quasi-Newton (BFGS, L-BFGS)** khai thác thông tin độ cong của ma trận Hessian mà không cần lưu trữ ma trận đạo hàm bậc hai khổng lồ trong bộ nhớ.

---

## 1. AdaGrad: Thích nghi hóa theo Tổng bình phương Gradient

Thuật toán **AdaGrad** (Duchi et al., 2011) khởi xướng ý tưởng: Các tọa độ nào nhận gradient lớn trong quá khứ cần giảm tốc độ học lại để tránh dao động; ngược lại, các tọa độ nào ít nhận gradient cần được tăng bước nhảy để nhanh chóng bắt kịp.

Khởi tạo bộ tích lũy $s_0 = 0$, tại mỗi bước $t$, AdaGrad cập nhật:

$$
s_t = s_{t-1} + g_t \odot g_t, \qquad \theta_{t+1} = \theta_t - \eta \frac{g_t}{\sqrt{s_t} + \varepsilon},
$$

trong đó:
- $\odot$ là phép nhân từng phần tử (Hadamard product).
- Phép chia vector và căn bậc hai được thực hiện độc lập trên từng tọa độ.
- $\varepsilon > 0$ (thường chọn $10^{-8}$) là số thực nhỏ ngăn lỗi chia cho 0.

### Cơ chế tự điều tiết của AdaGrad
Thành phần $s_{t, i} = \sum_{\tau=1}^t g_{\tau, i}^2$ lưu giữ tổng bình phương của toàn bộ gradient mà tham số thứ $i$ đã nhận từ đầu quá trình huấn luyện. Tốc độ học hiệu dụng của tham số thứ $i$ trở thành:

$$
\eta_{\mathrm{eff}, i} = \frac{\eta}{\sqrt{s_{t, i}} + \varepsilon}.
$$

- Tham số nào có gradient dồn dập: Đại lượng $s_{t, i}$ tăng vọt, $\eta_{\mathrm{eff}, i}$ tự động co nhỏ lại.
- Tham số nào có gradient thưa thớt: Đại lượng $s_{t, i}$ tăng chậm, $\eta_{\mathrm{eff}, i}$ giữ ở mức cao, giúp tham số đón nhận các bước cập nhật lớn mỗi khi có tín hiệu.

::: example Theo dõi bước nhảy trên một tọa độ đơn lẻ
Xét một tham số nhận chuỗi gradient thử nghiệm $g_1 = 2$, $g_2 = 2$ với tốc độ học $\eta = 0.1$ (tạm bỏ qua $\varepsilon$):
- **Bước 1**:
  - Tích lũy: $s_1 = 0 + 2^2 = 4$.
  - Bước cập nhật: $\Delta\theta_1 = -0.1 \cdot \frac{2}{\sqrt{4}} = -0.1 \cdot 1 = -0.1$.
- **Bước 2**:
  - Tích lũy: $s_2 = 4 + 2^2 = 8$.
  - Bước cập nhật:
    $$
    \Delta\theta_2 = -0.1 \cdot \frac{2}{\sqrt{8}} = -0.1 \cdot \frac{2}{2\sqrt{2}} = -\frac{0.1}{\sqrt{2}} \approx -0.07071.
    $$

Bước nhảy đã tự động giảm từ $0.1$ xuống xấp xỉ $0.07071$ dù gradient ở hai bước là hoàn toàn như nhau.
:::

**Nhược điểm chí tử của AdaGrad trong học sâu**: Vì $s_t$ là tổng dồn tích lũy của các số hạng không âm ($g_t^2 \ge 0$), $s_t$ tăng đơn điệu theo thời gian. Sau hàng chục nghìn bước lặp, mẫu số trở nên quá lớn khiến tốc độ học hiệu dụng suy giảm tiệm cận về 0 ("đóng băng" tham số) trước khi mạng kịp hội tụ.

---

## 2. RMSProp: Trung bình trượt hàm mũ của Bình phương Gradient

Để khắc phục hiện tượng suy giảm bước nhảy vĩnh viễn của AdaGrad, Geoffrey Hinton (trong bài giảng Coursera kinh điển năm 2012) đề xuất thuật toán **RMSProp**.

Thay vì cộng dồn toàn bộ lịch sử từ thuở sơ khai, RMSProp chỉ ghi nhớ quá khứ gần thông qua **trung bình trượt hàm mũ (Exponential Moving Average - EMA)**:

$$
v_t = \beta v_{t-1} + (1 - \beta) g_t \odot g_t, \qquad \theta_{t+1} = \theta_t - \eta \frac{g_t}{\sqrt{v_t} + \varepsilon},
$$

với hệ số suy giảm thường chọn $\beta = 0.9$.

Ý nghĩa toán học: Triển khai đệ quy của $v_t$ cho thấy:
$$
v_t = (1 - \beta) \sum_{\tau=1}^t \beta^{t-\tau} g_\tau^2.
$$
Các gradient cách hiện tại $k$ bước chỉ còn đóng góp một trọng số suy giảm theo lũy thừa $(1 - \beta)\beta^k$. Thuật toán có một "cửa sổ bộ nhớ hữu hạn" xấp xỉ $\frac{1}{1 - \beta}$ bước gần nhất (với $\beta = 0.9$, cửa sổ khoảng 10 bước). Nhờ đó, mẫu số không còn bị tăng vô hạn, cho phép mô hình tiếp tục học bền bỉ xuyên suốt quá trình huấn luyện dài hạn.

::: example Tính toán bước đầu với RMSProp
Khởi tạo $v_0 = 0$, gặp gradient $g_1 = 2$, hệ số $\beta = 0.9$, $\eta = 0.1$:
- $v_1 = 0.9(0) + (1 - 0.9)(2^2) = 0.4$.
- Bước cập nhật:
  $$
  \Delta\theta_1 = -0.1 \cdot \frac{2}{\sqrt{0.4}} \approx -0.1 \cdot \frac{2}{0.63245} \approx -0.31623.
  $$
Bước nhảy ban đầu này lớn hơn so với AdaGrad ($-0.1$) vì trạng thái khởi tạo $v_1 = 0.4$ còn nhỏ.
:::

---

## 3. Adam: Sự kết hợp hoàn hảo giữa Momentum và RMSProp

Thuật toán **Adam (Adaptive Moment Estimation)** do Diederik Kingma và Jimmy Ba công bố năm 2014, hiện là thuật toán tối ưu hóa mặc định và phổ biến bậc nhất trong toàn bộ nền kỹ nghệ AI.

Adam kết hợp sức mạnh của cả hai trường phái:
- **Moment bậc nhất** (First Moment - quán tính như Momentum): Ước lượng kỳ vọng của gradient có dấu để làm mượt hướng đi.
- **Moment bậc hai** (Second Moment - thang đo như RMSProp): Ước lượng phương sai không định tâm của bình phương gradient để co giãn bước đi.

### Thuật toán Adam chuẩn tắc
Khởi tạo $m_0 = 0$, $v_0 = 0$, tại mỗi bước $t = 1, 2, \ldots$:

$$
\begin{aligned}
m_t &= \beta_1 m_{t-1} + (1 - \beta_1) g_t, \\
v_t &= \beta_2 v_{t-1} + (1 - \beta_2) g_t \odot g_t, \\
\widehat m_t &= \frac{m_t}{1 - \beta_1^t}, \qquad \widehat v_t = \frac{v_t}{1 - \beta_2^t}, \\
\theta_{t+1} &= \theta_t - \eta \frac{\widehat m_t}{\sqrt{\widehat v_t} + \varepsilon}.
\end{aligned}
$$

Trong đó:
- $m_t$: Ước lượng moment bậc nhất (quán tính gradient).
- $v_t$: Ước lượng moment bậc hai (thang đo bình phương gradient).
- $\widehat m_t, \widehat v_t$: Các moment đã được hiệu chỉnh chệch (bias-corrected).

Các siêu tham số tiêu chuẩn: $\beta_1 = 0.9$, $\beta_2 = 0.999$, $\varepsilon = 10^{-8}$.

### 3.1 Bản chất toán học của Phép Hiệu chỉnh Chệch (Bias Correction)
Tại sao ta bắt buộc phải chia cho $(1 - \beta_1^t)$ và $(1 - \beta_2^t)$?
Vì ta khởi tạo các trạng thái ban đầu bằng 0 ($m_0 = 0, v_0 = 0$), trong những bước lặp đầu tiên, giá trị của $m_t$ và $v_t$ bị "kéo lệch" nghiêm trọng về phía 0.

Xét kỳ vọng của $m_t$:
$$
m_t = (1 - \beta_1) \sum_{i=1}^t \beta_1^{t-i} g_i.
$$
Lấy kỳ vọng hai vế (giả sử kỳ vọng của gradient là hằng số $\mathbb{E}[g_i] = \mathbb{E}[g]$):
$$
\mathbb{E}[m_t] = \mathbb{E}[g] (1 - \beta_1) \sum_{i=1}^t \beta_1^{t-i} = \mathbb{E}[g] (1 - \beta_1) \frac{1 - \beta_1^t}{1 - \beta_1} = \mathbb{E}[g] (1 - \beta_1^t).
$$

Rõ ràng $\mathbb{E}[m_t] \ne \mathbb{E}[g]$ do tồn tại thừa số $(1 - \beta_1^t) < 1$. Đặc biệt với $\beta_2 = 0.999$, tại bước $t = 1$, thừa số này chỉ bằng $1 - 0.999 = 0.001$, khiến $v_1$ nhỏ hơn giá trị thực tế tới 1000 lần! 

Do đó, phép chia cho $1 - \beta^t$ là bắt buộc để triệt tiêu độ lệch khởi tạo:
$$
\mathbb{E}[\widehat m_t] = \frac{\mathbb{E}[m_t]}{1 - \beta_1^t} = \mathbb{E}[g].
$$
Khi số bước $t$ tăng lớn ($t \to \infty$), số hạng $\beta^t \to 0$, thừa số $1 - \beta^t \to 1$, và phép hiệu chỉnh chệch tự động trở về giá trị gốc.

### 3.2 Từng bước tính toán số học của Adam
Xét chuỗi gradient thử nghiệm $g_1 = 2$, $g_2 = 1$ với các tham số chuẩn $\beta_1 = 0.9$, $\beta_2 = 0.999$, $\eta = 0.1$:

| Đại lượng trạng thái | Bước 1 ($t = 1$) | Bước 2 ($t = 2$) |
| :--- | :---: | :---: |
| $m_t$ | $0.1(2) = 0.2$ | $0.9(0.2) + 0.1(1) = 0.28$ |
| $v_t$ | $0.001(2^2) = 0.004$ | $0.999(0.004) + 0.001(1^2) = 0.004996$ |
| Hệ số hiệu chỉnh $1 - \beta_1^t$ | $1 - 0.9^1 = 0.1$ | $1 - 0.9^2 = 1 - 0.81 = 0.19$ |
| Hệ số hiệu chỉnh $1 - \beta_2^t$ | $1 - 0.999^1 = 0.001$ | $1 - 0.999^2 \approx 0.001999$ |
| $\widehat m_t$ đã hiệu chỉnh | $\frac{0.2}{0.1} = 2$ | $\frac{0.28}{0.19} = \frac{28}{19} \approx 1.47368$ |
| $\widehat v_t$ đã hiệu chỉnh | $\frac{0.004}{0.001} = 4$ | $\frac{0.004996}{0.001999} = \frac{4996}{1999} \approx 2.49925$ |
| Độ dời cập nhật $\Delta\theta_t$ | $-0.1 \cdot \frac{2}{\sqrt{4}} = -0.1$ | $-0.1 \cdot \frac{1.47368}{\sqrt{2.49925}} \approx -0.09322$ |

<MathLab type="optimizer" initial-method="adam">

```js
m = beta1*m + (1-beta1)*g;
v = beta2*v + (1-beta2)*g*g;
const mHat = m/(1-beta1**t), vHat = v/(1-beta2**t);
theta -= rate*mHat/(Math.sqrt(vHat)+epsilon);
```

</MathLab>

---

## 4. Giải hệ Newton bằng Phương pháp Gradient liên hợp (Conjugate Gradient)

Trong phương pháp Newton, ta phải giải hệ phương trình $H d = -g$. Khi mô hình có $n = 10^8$ tham số, ma trận Hessian $H$ có kích thước $10^8 \times 10^8$, hoàn toàn không thể khởi tạo hay lưu trữ trên bất kỳ siêu máy tính nào.

Làm sao giải hệ $Hz = b$ (với $b = -g$) mà không cần lưu ma trận $H$? Câu trả lời là **Phương pháp Gradient liên hợp (Conjugate Gradient - CG)**.

CG chỉ đòi hỏi một thao tác tính duy nhất: **Tính tích ma trận - vector $H v$** (thao tác này có thể thực hiện nhanh chóng qua phép vi phân tự động cấp hai mà không cần lập ma trận $H$).

Với ma trận $H$ đối xứng dương xác định ($H \succ 0$), khởi tạo $z_0$, phần dư $r_0 = b - H z_0$, và hướng liên hợp đầu tiên $p_0 = r_0$:

$$
\begin{aligned}
\alpha_k &= \frac{r_k^T r_k}{p_k^T H p_k}, & z_{k+1} &= z_k + \alpha_k p_k, \\
r_{k+1} &= r_k - \alpha_k H p_k, & \gamma_k &= \frac{r_{k+1}^T r_{k+1}}{r_k^T r_k}, \\
p_{k+1} &= r_{k+1} + \gamma_k p_k.
\end{aligned}
$$

Đặc tính toán học nổi bật của CG: Các hướng tìm kiếm $p_0, p_1, \ldots$ trực giao với nhau qua ma trận $H$ ($p_i^T H p_j = 0$ với mọi $i \ne j$). Trong số học chính xác, thuật toán CG giải đúng nghiệm của hệ $n$ chiều trong **tối đa không quá $n$ bước lặp**.

::: example Minh họa CG giải hệ tuyến tính hai chiều
Cho $H = \begin{bmatrix} 1 & 0 \\ 0 & 2 \end{bmatrix}$ và $b = \begin{bmatrix} 1 \\ 1 \end{bmatrix}$. Khởi tạo $z_0 = (0, 0)^T$.
- Phần dư ban đầu: $r_0 = b - Hz_0 = (1, 1)^T$, hướng tìm kiếm $p_0 = (1, 1)^T$.
- Tích ma trận-vector: $Hp_0 = \begin{bmatrix} 1 \\ 2 \end{bmatrix}$. 
  Mẫu số: $p_0^T H p_0 = 1(1) + 1(2) = 3$. Tử số: $r_0^T r_0 = 1^2 + 1^2 = 2$.
  Bước nhảy: $\alpha_0 = \frac{2}{3}$.
  Vị trí mới: $z_1 = z_0 + \alpha_0 p_0 = \left(\frac{2}{3}, \frac{2}{3}\right)^T$.
  Phần dư mới:
  $$
  r_1 = r_0 - \alpha_0 H p_0 = \begin{bmatrix} 1 \\ 1 \end{bmatrix} - \frac{2}{3}\begin{bmatrix} 1 \\ 2 \end{bmatrix} = \left(\frac{1}{3}, -\frac{1}{3}\right)^T.
  $$
- Hệ số góc Gram-Schmidt: $\gamma_0 = \frac{r_1^T r_1}{r_0^T r_0} = \frac{2/9}{2} = \frac{1}{9}$.
  Hướng liên hợp mới:
  $$
  p_1 = r_1 + \gamma_0 p_0 = \begin{bmatrix} 1/3 \\ -1/3 \end{bmatrix} + \frac{1}{9}\begin{bmatrix} 1 \\ 1 \end{bmatrix} = \left(\frac{4}{9}, -\frac{2}{9}\right)^T.
  $$
  Kiểm tra tính liên hợp: $p_0^T H p_1 = \begin{bmatrix}1 & 1\end{bmatrix} \begin{bmatrix} 4/9 \\ -4/9 \end{bmatrix} = 0$ (liên hợp hoàn hảo!).
- Bước 2: $\alpha_1 = \frac{3}{4}$, vị trí mới đạt đúng nghiệm: $z_2 = \left(1, \frac{1}{2}\right)^T$, thỏa mãn $H z_2 = b$.
:::

---

## 5. Phương pháp Quasi-Newton: BFGS và Điều kiện Secant

Một hướng tiếp cận khác để khai thác độ cong mà không phải tính đạo hàm bậc hai là **Phương pháp Quasi-Newton (Tựa Newton)**. Ý tưởng: Tích lũy thông tin độ cong từ chuỗi các vector dịch chuyển vị trí $s_k = \theta_{k+1} - \theta_k$ và biến thiên gradient $y_k = g_{k+1} - g_k$.

Theo định lý giá trị trung bình, ta có $y_k \approx H s_k \iff H^{-1} y_k \approx s_k$.
Thuật toán **BFGS (Broyden–Fletcher–Goldfarb–Shanno)** xấp xỉ trực tiếp ma trận Hessian nghịch đảo $M_k \approx H_k^{-1}$ thỏa mãn **điều kiện secant**:

$$
M_{k+1} y_k = s_k.
$$

Công thức cập nhật nghịch đảo BFGS:

$$
M_{k+1} = (I - \rho_k s_k y_k^T) M_k (I - \rho_k y_k s_k^T) + \rho_k s_k s_k^T,
$$

với hệ số chuẩn hóa $\rho_k = \frac{1}{y_k^T s_k}$. Nếu $y_k^T s_k > 0$ (điều kiện độ cong), ma trận $M_{k+1}$ được bảo đảm luôn đối xứng dương xác định ($M_{k+1} \succ 0$).

Để giải phóng bộ nhớ khi số chiều lớn, biến thể **L-BFGS (Limited-memory BFGS)** chỉ lưu trữ $m$ cặp vector $(s, y)$ gần nhất (thường $m \in [5, 20]$), cho phép tính toán hướng tựa Newton $d = -M g$ với chi phí bộ nhớ tuyến tính $O(m \cdot n)$ thay vì $O(n^2)$.

---

## 6. Phương pháp luận Thiết kế Thực nghiệm So sánh Optimizer

Khi so sánh các thuật toán tối ưu trong nghiên cứu khoa học AI, một sai lầm rất phổ biến là kết luận vội vã rằng thuật toán A "vượt trội" thuật toán B chỉ dựa trên một vài biểu đồ huấn luyện ngẫu nhiên.

Một phép so sánh khoa học chuẩn mực đòi hỏi tuân thủ nghiêm ngặt các nguyên tắc sau:
1. **Kiểm soát biến độc lập**: Giữ cố định kiến trúc mô hình, tập dữ liệu, phương pháp tiền xử lý và hạt giống ngẫu nhiên (random seed).
2. **Quy chuẩn tinh chỉnh siêu tham số**: Không thể so sánh một optimizer đã được dò siêu tham số kỹ lưỡng (learning rate, weight decay) với một optimizer dùng thông số mặc định. Mỗi thuật toán phải được quét siêu tham số công bằng trên tập xác thực (validation set).
3. **Báo cáo đa chiều**: Không đánh đồng số bước lặp (iterations) với thời gian thực tế. Một bước Newton hay L-BFGS tốn nhiều phép tính hơn một bước SGD hàng chục lần. Báo cáo bắt buộc phải phân tách:
   - Mất mát theo số bước lặp (cho thấy hiệu quả lý thuyết).
   - Mất mát theo thời gian thực (wall-clock time, cho thấy hiệu quả phần cứng).
   - Khả năng khái quát hóa trên tập kiểm thử (test accuracy/loss).

---

## Bài tập tự luyện

::: exercise 1. Bản chất của Trung bình bình phương vs Bình phương trung bình
Giả sử một tham số dao động qua lại và nhận hai giá trị gradient liên tiếp là $g_1 = 2$ và $g_2 = -2$.
1. Tính trung bình cộng của gradient và trung bình cộng của bình phương gradient.
2. Điều gì sẽ xảy ra nếu ta dùng bình phương của trung bình cộng để ước lượng thang đo độ lớn $v$?
:::
::: solution
1. - Trung bình cộng của gradient: $\bar g = \frac{2 + (-2)}{2} = 0$.
   - Trung bình cộng của bình phương gradient: $\overline{g^2} = \frac{2^2 + (-2)^2}{2} = \frac{4 + 4}{2} = 4$.
2. Nếu dùng bình phương của trung bình cộng: $(\bar g)^2 = 0^2 = 0$.
   Toàn bộ thông tin về mức độ dao động mạnh mẽ của gradient bị triệt tiêu hoàn toàn! Việc chia cho một đại lượng bằng 0 sẽ khiến bước cập nhật phát nổ. Do đó, việc lưu giữ trung bình của các bình phương ($g \odot g$) là điều kiện sống còn để đo lường độ lớn dao động địa hình.
:::

::: exercise 2. Phân tích bước khởi đầu của Adam
Xét tham số nhận gradient bước đầu tiên $g_1 = -3$. Các siêu tham số là $\beta_1 = 0.9$, $\beta_2 = 0.999$, $\eta = 0.1$.
Hãy tính toán các trạng thái $m_1, v_1, \widehat m_1, \widehat v_1$ và xác định dấu của bước cập nhật $\Delta\theta_1$.
:::
::: solution
- $m_1 = (1 - \beta_1) g_1 = 0.1(-3) = -0.3$.
- $v_1 = (1 - \beta_2) g_1^2 = 0.001(9) = 0.009$.
- Hiệu chỉnh chệch:
  $$\widehat m_1 = \frac{m_1}{1 - \beta_1^1} = \frac{-0.3}{0.1} = -3.$$
  $$\widehat v_1 = \frac{v_1}{1 - \beta_2^1} = \frac{0.009}{0.001} = 9.$$
- Bước cập nhật:
  $$\Delta\theta_1 = -\eta \frac{\widehat m_1}{\sqrt{\widehat v_1} + \varepsilon} \approx -0.1 \cdot \frac{-3}{\sqrt{9}} = -0.1 \cdot \frac{-3}{3} = +0.1 > 0.$$
Dấu của gradient âm được lưu giữ hoàn hảo trong $m_1$, giúp tham số di chuyển theo chiều dương để hạ thấp hàm mất mát.
:::

::: exercise 3. Tại sao Adam không thể thay thế ma trận Hessian đầy đủ?
Cho hàm số có ma trận Hessian đầy đủ chứa tương quan chéo: $H = \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}$ và vector gradient $g = \begin{bmatrix} 1 \\ 0 \end{bmatrix}$.
1. Giải hệ phương trình Newton $Hd = -g$ để tìm hướng Newton chính xác.
2. So sánh kết quả trên với hướng cập nhật nếu chỉ co giãn độc lập theo từng phần tử đường chéo (như triết lý của Adam/RMSProp).
:::
::: solution
1. Hướng Newton chính xác: Giải hệ phương trình:
   $$\begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix} \begin{bmatrix} d_1 \\ d_2 \end{bmatrix} = \begin{bmatrix} -1 \\ 0 \end{bmatrix} \iff \begin{cases} 2d_1 + d_2 = -1 \\ d_1 + 2d_2 = 0 \end{cases} \implies \begin{cases} d_1 = -2/3 \\ d_2 = 1/3 \end{cases}.$$
   Hướng Newton là $d = \left(-\frac{2}{3}, \frac{1}{3}\right)^T$. Tọa độ thứ hai được điều chỉnh một lượng dương $+1/3$ nhờ thông tin tương quan chéo $H_{12} = 1$.
2. Nếu chỉ co giãn theo đường chéo: Vector bước đi là:
   $$
   -\operatorname{diag}(H)^{-1} g = \begin{bmatrix} -1/2 & 0 \\ 0 & -1/2 \end{bmatrix} \begin{bmatrix} 1 \\ 0 \end{bmatrix} = \begin{bmatrix} -1/2 \\ 0 \end{bmatrix}.
   $$
   Tọa độ thứ hai hoàn toàn không được cập nhật ($d_2 = 0$). Điều này chứng minh rằng các thuật toán thích nghi từng tọa độ như Adam hay RMSProp chỉ xấp xỉ đường chéo của Hessian, hoàn toàn không thể nắm bắt được tương quan xoay trục giữa các biến trong không gian tham số.
:::

::: exercise 4. Phân tích toán học cơ chế hiệu chỉnh chệch (Bias Correction) của Adam
Thuật toán Adam khởi tạo các vector moment bậc nhất và bậc hai bằng $0$: $m_0 = 0$, $v_0 = 0$.
Quy tắc cập nhật trung bình trượt hàm mũ tại bước $t \ge 1$:
$$
m_t = \beta_1 m_{t-1} + (1 - \beta_1) g_t, \qquad v_t = \beta_2 v_{t-1} + (1 - \beta_2) g_t^2,
$$
với $\beta_1 = 0{,}9$, $\beta_2 = 0{,}999$.
1. Khai triển đệ quy để biểu diễn $m_t$ thành tổ hợp tuyến tính của các gradient quá khứ $\{g_1, \dots, g_t\}$.
2. Giả sử gradient thực tế có kỳ vọng không đổi $\mathbb{E}[g_i] = \mu$ với mọi $i$. Chứng minh rằng:
   $$
   \mathbb{E}[m_t] = (1 - \beta_1^t) \mu.
   $$
   Từ đó suy ra công thức hiệu chỉnh chệch: $\widehat{m}_t = \frac{m_t}{1 - \beta_1^t}$.
3. Xét bước lặp đầu tiên $t = 1$: Nếu không có cơ chế hiệu chỉnh chệch, bước nhảy của Adam bị suy giảm một lượng bằng bao nhiêu? Giải thích tại sao việc thiếu hiệu chỉnh chệch khiến các bước lặp đầu bị đóng băng.
:::

::: solution
1. **Khai triển đệ quy moment bậc nhất**:
   Tại bước $t = 1$: $m_1 = (1 - \beta_1) g_1$.
   Tại bước $t = 2$:
   $$
   m_2 = \beta_1 m_1 + (1 - \beta_1) g_2 = \beta_1(1 - \beta_1) g_1 + (1 - \beta_1) g_2.
   $$
   Bằng quy nạp toán học, tại bước $t$ bất kỳ:
   $$
   m_t = (1 - \beta_1) \sum_{i=1}^t \beta_1^{t - i} g_i.
   $$

2. **Kỳ vọng toán học và cơ chế hiệu chỉnh**:
   Lấy kỳ vọng toán học hai vế với giả thiết $\mathbb{E}[g_i] = \mu$:
   $$
   \begin{aligned}
   \mathbb{E}[m_t] &= (1 - \beta_1) \sum_{i=1}^t \beta_1^{t - i} \mathbb{E}[g_i] \\
   &= (1 - \beta_1) \mu \sum_{i=1}^t \beta_1^{t - i}.
   \end{aligned}
   $$
   Tổng cấp số nhân với công bội $\beta_1$:
   $$
   \sum_{i=1}^t \beta_1^{t - i} = 1 + \beta_1 + \beta_1^2 + \dots + \beta_1^{t-1} = \frac{1 - \beta_1^t}{1 - \beta_1}.
   $$
   Thay vào biểu thức kỳ vọng:
   $$
   \mathbb{E}[m_t] = (1 - \beta_1) \mu \left(\frac{1 - \beta_1^t}{1 - \beta_1}\right) = (1 - \beta_1^t) \mu.
   $$
   Vì $\beta_1 < 1$, ta có $1 - \beta_1^t < 1$, chứng minh rằng $m_t$ bị chệch nghiêm trọng về phía gốc tọa độ $0$.
   Để thu được một ước lượng không chệch ($\mathbb{E}[\widehat{m}_t] = \mu$), ta chia $m_t$ cho đúng hệ số co cụm $1 - \beta_1^t$:
   $$
   \widehat{m}_t = \frac{m_t}{1 - \beta_1^t}.
   $$
   Chứng minh hoàn toàn tương tự cho moment bậc hai: $\widehat{v}_t = \frac{v_t}{1 - \beta_2^t}$.

3. **Tác động tại bước lặp đầu tiên $t = 1$**:
   - Với moment bậc nhất: $1 - \beta_1^1 = 1 - 0{,}9 = 0{,}1$. Không có hiệu chỉnh, $m_1 = 0{,}1 g_1$ bị thu nhỏ 10 lần.
   - Với moment bậc hai: $1 - \beta_2^1 = 1 - 0{,}999 = 0{,}001$. Không có hiệu chỉnh, $v_1 = 0{,}001 g_1^2$ bị thu nhỏ 1000 lần.
   
   Tỉ số cập nhật của Adam khi không hiệu chỉnh:
   $$
   \frac{m_1}{\sqrt{v_1}} = \frac{0{,}1 g_1}{\sqrt{0{,}001 g_1^2}} = \frac{0{,}1}{\sqrt{0{,}001}} \frac{g_1}{|g_1|} = \frac{0{,}1}{0{,}0316} \operatorname{sgn}(g_1) \approx 3{,}16 \operatorname{sgn}(g_1).
   $$
   Trong khi tỉ số đã hiệu chỉnh:
   $$
   \frac{\widehat{m}_1}{\sqrt{\widehat{v}_1}} = \frac{g_1}{\sqrt{g_1^2}} = \operatorname{sgn}(g_1) = 1 \operatorname{sgn}(g_1).
   $$
   Nếu không có hiệu chỉnh chệch, độ lệch giữa bậc một và bậc hai làm biến dạng thang đo bước nhảy ban đầu. Đặc biệt trong các tầng sâu khi gradient rất nhỏ, $v_t$ bị kéo sát về 0 làm mẫu số mất ổn định số học, hoặc ngược lại làm các bước lặp đầu bị co giật mạnh trước khi bước vào quỹ đạo ổn định.
:::

::: exercise 5. So sánh động lực học suy giảm bước học: AdaGrad vs RMSProp
Xét bài toán tối ưu với một tham số có gradient không đổi tại mỗi bước lặp: Giả sử $g_t = c > 0$ với mọi $t \ge 1$.
1. Với thuật toán AdaGrad: $G_t = \sum_{i=1}^t g_i^2 = t c^2$. Tính bước nhảy $\Delta \theta_t^{\text{Ada}} = \frac{\eta}{\sqrt{G_t}} g_t$ và chứng minh tổng quãng đường di chuyển $\sum_{t=1}^T \Delta \theta_t^{\text{Ada}}$ tăng trưởng theo tốc độ $O(\sqrt{T})$, dẫn tới hiện tượng triệt tiêu bước học (learning rate dying).
2. Với thuật toán RMSProp: Biến tích lũy $v_t = \beta v_{t-1} + (1 - \beta) g_t^2$ với $\beta \in (0, 1)$ và $v_0 = 0$.
   - Tìm biểu thức giải tích của $v_t$ và giới hạn dừng khi $t \to \infty$.
   - Tính bước nhảy ổn định $\Delta \theta_t^{\text{RMS}}$ khi $t$ lớn.
3. Giải thích tại sao RMSProp duy trì được khả năng thích nghi và học tập liên tục trong không gian tối ưu phi lồi của học sâu.
:::

::: solution
1. **Động lực học của AdaGrad**:
   Tổng bình phương gradient tích lũy tại bước $t$:
   $$
   G_t = \sum_{i=1}^t c^2 = t c^2.
   $$
   Độ dài bước nhảy tại bước $t$ (bỏ qua $\epsilon > 0$ rất nhỏ):
   $$
   \Delta \theta_t^{\text{Ada}} = \frac{\eta}{\sqrt{t c^2}} c = \frac{\eta}{\sqrt{t}}.
   $$
   Tổng quãng đường tham số đi được sau $T$ bước lặp:
   $$
   S_T = \sum_{t=1}^T \Delta \theta_t^{\text{Ada}} = \eta \sum_{t=1}^T \frac{1}{\sqrt{t}}.
   $$
   Theo định lý tích phân so sánh:
   $$
   \int_1^T \frac{1}{\sqrt{t}} \, \mathrm{d}t = \big[2\sqrt{t}\big]_1^T = 2\sqrt{T} - 2.
   $$
   Do đó $S_T = O(\sqrt{T})$.
   Độ dài bước nhảy suy giảm theo $1/\sqrt{t} \to 0$. Khi $T$ lớn, bước nhảy trở nên nhỏ tới mức gần như đóng băng hoàn toàn. Nếu mô hình gặp một vùng đồi dốc ở giai đoạn đầu, $G_t$ tích lũy quá lớn khiến thuật toán kiệt sức và không bao giờ thoát ra được các thung lũng phẳng sau đó.

2. **Động lực học của RMSProp**:
   Khai triển đệ quy với $g_i^2 = c^2$:
   $$
   \begin{aligned}
   v_t &= (1 - \beta) c^2 \sum_{i=1}^t \beta^{t - i} \\
   &= (1 - \beta) c^2 \left(\frac{1 - \beta^t}{1 - \beta}\right) = (1 - \beta^t) c^2.
   \end{aligned}
   $$
   Khi $t \to \infty$, vì $\beta \in (0, 1)$, số hạng $\beta^t \to 0$. Do đó:
   $$
   \lim_{t \to \infty} v_t = c^2.
   $$
   Bước nhảy ổn định khi $t$ lớn:
   $$
   \Delta \theta_t^{\text{RMS}} = \frac{\eta}{\sqrt{c^2}} c = \eta.
   $$
   Tổng quãng đường di chuyển sau $T$ bước:
   $$
   S_T \approx \sum_{t=1}^T \eta = \eta T = O(T).
   $$

3. **Ưu thế vượt trội của RMSProp**:
   Bằng cách thay thế phép cộng dồn lịch sử vô hạn bằng cửa sổ trượt trung bình mũ có độ dài hiệu dụng khoảng $\frac{1}{1 - \beta}$ bước (với $\beta = 0{,}9$, cửa sổ khoảng 10 bước), RMSProp "lãng quên" các gradient quá khứ xa xôi. Thuật toán duy trì tốc độ học hữu hạn ổn định, cho phép mô hình tiếp tục điều chỉnh linh hoạt khi cảnh quan tối ưu thay đổi từ vách núi dốc sang vùng lòng chảo phẳng.
:::

::: exercise 6. Phương pháp Gradient liên hợp (Conjugate Gradient) trên hàm toàn phương
Cho bài toán cực tiểu hóa hàm toàn phương lồi:
$$
f(x) = \frac{1}{2} x^T A x - b^T x,
$$
với ma trận đối xứng xác định dương $A = \begin{bmatrix} 3 & 1 \\ 1 & 2 \end{bmatrix}$ và vector $b = \begin{bmatrix} 5 \\ 5 \end{bmatrix}$. Khởi tạo từ $x^0 = (0, 0)^T$.
1. Bước 1: Tính gradient $g^0 = \nabla f(x^0)$ và chọn hướng đầu tiên $p^0 = -g^0$. Tìm bước nhảy tối ưu $\alpha_0 = \frac{(p^0)^T (-g^0)}{(p^0)^T A p^0}$ và điểm cập nhật $x^1$.
2. Bước 2: Tính gradient mới $g^1 = \nabla f(x^1)$. Xác định hệ số trực giao Gram-Schmidt liên hợp $\beta_1 = \frac{(g^1)^T A p^0}{(p^0)^T A p^0}$ để xây dựng hướng liên hợp thứ hai $p^1 = -g^1 + \beta_1 p^0$.
3. Kiểm tra tính liên hợp ma trận $(p^0)^T A p^1 = 0$, tính bước nhảy $\alpha_1$ và tìm nghiệm $x^2$. Kiểm chứng rằng $x^2$ chính là nghiệm tối ưu toàn cục chính xác $x^* = A^{-1} b$.
:::

::: solution
1. **Bước 1 của Conjugate Gradient**:
   Gradient của hàm toàn phương: $\nabla f(x) = A x - b$.
   Tại điểm khởi đầu $x^0 = (0, 0)^T$:
   $$
   g^0 = A x^0 - b = -b = \begin{bmatrix} -5 \\ -5 \end{bmatrix}.
   $$
   Hướng dốc nhất ban đầu:
   $$
   p^0 = -g^0 = \begin{bmatrix} 5 \\ 5 \end{bmatrix}.
   $$
   Tích vô hướng với ma trận $A$:
   $$
   A p^0 = \begin{bmatrix} 3 & 1 \\ 1 & 2 \end{bmatrix} \begin{bmatrix} 5 \\ 5 \end{bmatrix} = \begin{bmatrix} 15 + 5 \\ 5 + 10 \end{bmatrix} = \begin{bmatrix} 20 \\ 15 \end{bmatrix}.
   $$
   Mẫu số:
   $$
   (p^0)^T A p^0 = 5(20) + 5(15) = 100 + 75 = 175.
   $$
   Tử số: $(p^0)^T (-g^0) = \|p^0\|_2^2 = 5^2 + 5^2 = 50$.
   Độ dài bước nhảy tối ưu:
   $$
   \alpha_0 = \frac{50}{175} = \frac{2}{7}.
   $$
   Cập nhật điểm mới:
   $$
   x^1 = x^0 + \alpha_0 p^0 = \begin{bmatrix} 0 \\ 0 \end{bmatrix} + \frac{2}{7} \begin{bmatrix} 5 \\ 5 \end{bmatrix} = \begin{bmatrix} 10/7 \\ 10/7 \end{bmatrix}.
   $$

2. **Bước 2: Xây dựng hướng liên hợp**:
   Tính gradient tại điểm mới $x^1$:
   $$
   g^1 = A x^1 - b = \frac{10}{7} \begin{bmatrix} 4 \\ 3 \end{bmatrix} - \begin{bmatrix} 5 \\ 5 \end{bmatrix} = \begin{bmatrix} 40/7 - 35/7 \\ 30/7 - 35/7 \end{bmatrix} = \begin{bmatrix} 5/7 \\ -5/7 \end{bmatrix}.
   $$
   Tích vô hướng của $g^1$ với $p^0$: $(g^1)^T p^0 = \frac{5}{7}(5) + \left(-\frac{5}{7}\right)(5) = 0$ (gradient mới trực giao hoàn hảo với hướng trước).
   
   Xác định hệ số liên hợp $\beta_1$ theo công thức Polak-Ribière hoặc Fletcher-Reeves:
   $$
   \beta_1 = \frac{\|g^1\|_2^2}{\|g^0\|_2^2} = \frac{(5/7)^2 + (-5/7)^2}{5^2 + 5^2} = \frac{50/49}{50} = \frac{1}{49}.
   $$
   Hướng liên hợp mới:
   $$
   p^1 = -g^1 + \beta_1 p^0 = \begin{bmatrix} -5/7 \\ 5/7 \end{bmatrix} + \frac{1}{49} \begin{bmatrix} 5 \\ 5 \end{bmatrix} = \begin{bmatrix} -35/49 + 5/49 \\ 35/49 + 5/49 \end{bmatrix} = \begin{bmatrix} -30/49 \\ 40/49 \end{bmatrix}.
   $$
   Rút gọn tỉ lệ bằng cách nhân với $\frac{49}{10}$: Chọn vector hướng tương đương $p^1 = \begin{bmatrix} -3 \\ 4 \end{bmatrix}$.

3. **Kiểm tra tính liên hợp và bước nhảy cuối**:
   Kiểm tra tính liên hợp $A$-trực giao:
   $$
   A p^1 = \begin{bmatrix} 3 & 1 \\ 1 & 2 \end{bmatrix} \begin{bmatrix} -3 \\ 4 \end{bmatrix} = \begin{bmatrix} -9 + 4 \\ -3 + 8 \end{bmatrix} = \begin{bmatrix} -5 \\ 5 \end{bmatrix}.
   $$
   Tích vô hướng:
   $$
   (p^0)^T A p^1 = \begin{bmatrix} 5 & 5 \end{bmatrix} \begin{bmatrix} -5 \\ 5 \end{bmatrix} = -25 + 25 = 0.
   $$
   Tính chất liên hợp được nghiệm đúng hoàn toàn.
   
   Bước nhảy $\alpha_1$:
   $$
   \alpha_1 = -\frac{(g^1)^T p^1}{(p^1)^T A p^1} = -\frac{\frac{5}{7}(-3) + \left(-\frac{5}{7}\right)(4)}{(-3)(-5) + 4(5)} = -\frac{-35/7}{15 + 20} = -\frac{-5}{35} = \frac{1}{7}.
   $$
   Cập nhật nghiệm $x^2$:
   $$
   x^2 = x^1 + \alpha_1 p^1 = \begin{bmatrix} 10/7 \\ 10/7 \end{bmatrix} + \frac{1}{7} \begin{bmatrix} -3 \\ 4 \end{bmatrix} = \begin{bmatrix} 10/7 - 3/7 \\ 10/7 + 4/7 \end{bmatrix} = \begin{bmatrix} 7/7 \\ 14/7 \end{bmatrix} = \begin{bmatrix} 1 \\ 2 \end{bmatrix}.
   $$
   Kiểm tra nghiệm giải tích của hệ phương trình tuyến tính $A x = b$:
   $$
   \begin{bmatrix} 3 & 1 \\ 1 & 2 \end{bmatrix} \begin{bmatrix} 1 \\ 2 \end{bmatrix} = \begin{bmatrix} 3(1) + 1(2) \\ 1(1) + 2(2) \end{bmatrix} = \begin{bmatrix} 5 \\ 5 \end{bmatrix} = b.
   $$
   Nghiệm chính xác tuyệt đối được tìm thấy sau đúng $n = 2$ bước lặp mà không cần tính toán nghịch đảo ma trận $A^{-1}$.
:::

::: exercise 7. Điều kiện cát tuyến và cập nhật xấp xỉ Hessian Quasi-Newton BFGS
Các phương pháp Quasi-Newton xấp xỉ ma trận Hessian nghịch đảo $H_k \approx (\nabla^2 f(x_k))^{-1}$ qua từng bước lặp mà không cần giải hệ phương trình tuyến tính.
Đặt độ dời tham số $s_k = x_{k+1} - x_k$ và độ biến thiên gradient $y_k = \nabla f(x_{k+1}) - \nabla f(x_k)$.
1. Thiết lập phương trình cát tuyến (Secant Equation) cho ma trận độ cong $B_{k+1} \approx \nabla^2 f(x_{k+1})$ và cho ma trận nghịch đảo $H_{k+1}$.
2. Điều kiện độ cong (Curvature Condition): Chứng minh rằng để ma trận xấp xỉ $B_{k+1}$ xác định dương ($B_{k+1} \succ 0$), điều kiện cần là $s_k^T y_k > 0$.
3. Công thức cập nhật BFGS cho nghịch đảo Hessian:
   $$
   H_{k+1} = (I - \rho_k s_k y_k^T) H_k (I - \rho_k y_k s_k^T) + \rho_k s_k s_k^T, \qquad \rho_k = \frac{1}{y_k^T s_k}.
   $$
   Chứng minh rằng nếu $H_k \succ 0$ và $y_k^T s_k > 0$, thì ma trận mới $H_{k+1}$ luôn tự động xác định dương ($H_{k+1} \succ 0$).
:::

::: solution
1. **Phương trình cát tuyến**:
   Theo khai triển Taylor của gradient quanh điểm $x_{k+1}$:
   $$
   \nabla f(x_k) \approx \nabla f(x_{k+1}) + \nabla^2 f(x_{k+1}) (x_k - x_{k+1}).
   $$
   Chuyển vế:
   $$
   \nabla f(x_{k+1}) - \nabla f(x_k) \approx \nabla^2 f(x_{k+1}) (x_{k+1} - x_k).
   $$
   Đặt $y_k = \nabla f(x_{k+1}) - \nabla f(x_k)$ và $s_k = x_{k+1} - x_k$, ta thu được phương trình cát tuyến:
   $$
   B_{k+1} s_k = y_k.
   $$
   Nhân cả hai vế với ma trận nghịch đảo $H_{k+1} = B_{k+1}^{-1}$, ta có phương trình cát tuyến cho ma trận nghịch đảo:
   $$
   H_{k+1} y_k = s_k.
   $$

2. **Điều kiện độ cong**:
   Nhân vế trái của phương trình cát tuyến với $s_k^T$:
   $$
   s_k^T B_{k+1} s_k = s_k^T y_k.
   $$
   Nếu $B_{k+1} \succ 0$ (xác định dương), thì với mọi vector khác không $s_k \ne 0$, dạng toàn phương bắt buộc phải dương:
   $$
   s_k^T B_{k+1} s_k > 0 \implies s_k^T y_k > 0.
   $$
   Điều này đồng nghĩa với việc gradient phải biến thiên cùng chiều với bước nhảy (hàm số có độ cong dương dọc theo hướng tìm kiếm).

3. **Chứng minh tính xác định dương của BFGS**:
   Lấy một vector bất kỳ $z \ne 0 \in \mathbb{R}^n$. Xét dạng toàn phương:
   $$
   z^T H_{k+1} z = z^T (I - \rho_k s_k y_k^T) H_k (I - \rho_k y_k s_k^T) z + \rho_k (z^T s_k)^2.
   $$
   Đặt vector $w = (I - \rho_k y_k s_k^T) z = z - \rho_k (s_k^T z) y_k$.
   Biểu thức trở thành:
   $$
   z^T H_{k+1} z = w^T H_k w + \rho_k (s_k^T z)^2.
   $$
   Vì $H_k \succ 0$, ta có $w^T H_k w \ge 0$. Hơn nữa $\rho_k = \frac{1}{y_k^T s_k} > 0$ nên số hạng thứ hai $\rho_k (s_k^T z)^2 \ge 0$.
   Do đó $z^T H_{k+1} z \ge 0$.
   
   Xét trường hợp dấu bằng triệt tiêu: Để $z^T H_{k+1} z = 0$, cả hai số hạng không âm đều phải bằng 0:
   - Số hạng thứ hai bằng 0 kéo theo $s_k^T z = 0$.
   - Khi $s_k^T z = 0$, vector $w$ trở thành $w = z - \rho_k (0) y_k = z$.
   - Thay vào số hạng thứ nhất: $w^T H_k w = z^T H_k z = 0$.
   - Vì $H_k \succ 0$, điều này buộc $z = 0$, mâu thuẫn với giả thiết $z \ne 0$.
   
   Vậy $z^T H_{k+1} z > 0$ với mọi $z \ne 0$. Ma trận cập nhật BFGS bảo toàn tính xác định dương vĩnh cửu.
:::

::: exercise 8. Cơ chế làm mượt bề mặt mất mát của Batch Normalization
Trong mạng nơ-ron sâu, Batch Normalization (BN) chuẩn hóa một tập hợp các kích hoạt tiền phi tuyến $\{x_1, \dots, x_m\}$ trong một lô nhỏ kích thước $m$:
$$
\mu_B = \frac{1}{m} \sum_{i=1}^m x_i, \qquad \sigma_B^2 = \frac{1}{m} \sum_{i=1}^m (x_i - \mu_B)^2, \qquad \widehat{x}_i = \frac{x_i - \mu_B}{\sqrt{\sigma_B^2 + \varepsilon}}.
$$
Đầu ra cuối cùng được co dãn và dịch chuyển qua hai tham số học được $\gamma$ và $\beta$: $y_i = \gamma \widehat{x}_i + \beta$.
1. Chứng minh rằng đầu ra chuẩn hóa có kỳ vọng mẫu bằng $0$ và phương sai mẫu xấp xỉ bằng $1$: Biểu thức $\frac{1}{m}\sum_{i=1}^m \widehat{x}_i = 0$ và $\frac{1}{m}\sum_{i=1}^m \widehat{x}_i^2 = \frac{\sigma_B^2}{\sigma_B^2 + \varepsilon} \approx 1$.
2. Tính bất biến đối với thang đo trọng số (Scale Invariance): Giả sử $x = W u$. Nếu ma trận trọng số bị nhân với một hằng số dương $\alpha > 0$ ($W \to \alpha W$), hãy chứng minh rằng $\widehat{x}_i$ hoàn toàn không thay đổi.
3. Giải thích tại sao tính bất biến này ngăn chặn hiện tượng bùng nổ gradient và làm mượt bề mặt mất mát (Loss Landscape Smoothing), cho phép sử dụng tốc độ học lớn hơn đáng kể.
:::

::: solution
1. **Kiểm tra kỳ vọng và phương sai mẫu**:
   - Kỳ vọng mẫu của $\widehat{x}_i$:
     $$
     \frac{1}{m} \sum_{i=1}^m \widehat{x}_i = \frac{1}{m} \sum_{i=1}^m \frac{x_i - \mu_B}{\sqrt{\sigma_B^2 + \varepsilon}} = \frac{1}{\sqrt{\sigma_B^2 + \varepsilon}} \left(\frac{1}{m} \sum_{i=1}^m x_i - \mu_B\right) = \frac{\mu_B - \mu_B}{\sqrt{\sigma_B^2 + \varepsilon}} = 0.
     $$
   - Phương sai mẫu của $\widehat{x}_i$:
     $$
     \frac{1}{m} \sum_{i=1}^m \widehat{x}_i^2 = \frac{1}{m} \sum_{i=1}^m \frac{(x_i - \mu_B)^2}{\sigma_B^2 + \varepsilon} = \frac{\frac{1}{m}\sum_{i=1}^m (x_i - \mu_B)^2}{\sigma_B^2 + \varepsilon} = \frac{\sigma_B^2}{\sigma_B^2 + \varepsilon} \approx 1.
     $$

2. **Tính bất biến đối với phép co dãn trọng số**:
   Khi $W' = \alpha W$ với $\alpha > 0$, kích hoạt mới là $x'_i = \alpha x_i$.
   - Trung bình mẫu mới:
     $$
     \mu'_B = \frac{1}{m} \sum_{i=1}^m (\alpha x_i) = \alpha \mu_B.
     $$
   - Phương sai mẫu mới:
     $$
     {\sigma'_B}^2 = \frac{1}{m} \sum_{i=1}^m (\alpha x_i - \alpha \mu_B)^2 = \alpha^2 \sigma_B^2.
     $$
   - Đầu ra chuẩn hóa mới (bỏ qua $\varepsilon$ rất nhỏ):
     $$
     \widehat{x}'_i = \frac{\alpha x_i - \alpha \mu_B}{\sqrt{\alpha^2 \sigma_B^2}} = \frac{\alpha (x_i - \mu_B)}{\alpha \sigma_B} = \frac{x_i - \mu_B}{\sigma_B} = \widehat{x}_i.
     $$
   Đầu ra của tầng BN hoàn toàn bất biến đối với độ lớn của ma trận trọng số $W$.

3. **Cơ chế làm mượt bề mặt mất mát**:
   Theo quy tắc dây chuyền, gradient đối với ma trận trọng số co dãn:
   $$
   \nabla_{W'} \mathcal{L} = \frac{1}{\alpha} \nabla_W \mathcal{L}.
   $$
   Nếu trọng số $W$ có xu hướng tăng lớn trong quá trình huấn luyện, gradient của nó tự động co nhỏ lại theo tỉ lệ nghịch $1/\alpha$. Điều này triệt tiêu hoàn toàn khả năng bùng nổ gradient (exploding gradients).
   
   Nghiên cứu của Santurkar et al. (2018) đã chứng minh rằng lợi ích cốt lõi của BN không chỉ nằm ở việc giảm "internal covariate shift", mà chính là làm cho hàm mất mát thỏa mãn điều kiện Lipschitz với hằng số $L$ nhỏ hơn nhiều và ma trận Hessian ổn định hơn. Gradient ít bị biến động đột ngột theo các phương hướng không gian, cho phép người huấn luyện tự tin tăng tốc độ học lên gấp 5-10 lần mà không sợ thuật toán bị phân kỳ.
:::


---

## Tóm tắt cốt lõi

1. **AdaGrad**: Khởi xướng cơ chế chia nhỏ tốc độ học theo tổng bình phương gradient dồn tích, phù hợp với dữ liệu thưa nhưng dễ bị tắt dần bước nhảy.
2. **RMSProp**: Thay thế tổng dồn tích bằng trung bình trượt hàm mũ (EMA), tạo ra cửa sổ bộ nhớ hữu hạn giúp duy trì khả năng học lâu dài.
3. **Adam**: Kết hợp tinh hoa của Momentum (hướng đi) và RMSProp (độ dài bước), tích hợp cơ chế hiệu chỉnh chệch khởi tạo chuẩn xác.
4. **Conjugate Gradient & BFGS**: Cung cấp công cụ xấp xỉ bậc hai siêu việt, giải phóng thuật toán khỏi gánh nặng tính toán và lưu trữ ma trận Hessian khổng lồ.

---

## Tài liệu tham khảo và Đọc thêm

Dành cho người học muốn nghiên cứu chuyên sâu về các thuật toán tối ưu thích nghi:
- **Diederik P. Kingma & Jimmy Ba** (2014), *Adam: A Method for Stochastic Optimization*, ICLR. Bài báo kinh điển đặt nền móng cho thuật toán Adam và cơ chế hiệu chỉnh chệch.
- **John Duchi, Elad Hazan & Yoram Singer** (2011), *Adaptive Subgradient Methods for Online Learning and Stochastic Optimization*, JMLR. Nguồn gốc của thuật toán AdaGrad và giải tích subgradient thích nghi.
- **Jonathan Richard Shewchuk**, *An Introduction to the Conjugate Gradient Method Without the Agonizing Pain*, Carnegie Mellon University. Tài liệu nhập môn trực quan và sâu sắc nhất về phương pháp Gradient liên hợp.

Tiếp theo: [Bài 07: Quy hoạch tuyến tính và Quy hoạch động Bellman](./bai-07-quy-hoach-tuyen-tinh-va-dong.md).
