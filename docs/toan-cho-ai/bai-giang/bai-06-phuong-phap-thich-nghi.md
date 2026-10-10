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

Lớp thuật toán tối ưu thích nghi (Adaptive Optimization) — dẫn đầu bởi AdaGrad, RMSProp và Adam — giải quyết bài toán này bằng cách tự động gán cho mỗi tham số một tốc độ học riêng biệt, biến thiên linh hoạt theo lịch sử biến động của gradient.

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

- Tham số nào có gradient dồn dập: $s_{t, i}$ tăng vọt, $\eta_{\mathrm{eff}, i}$ tự động co nhỏ lại.
- Tham số nào có gradient thưa thớt: $s_{t, i}$ tăng chậm, $\eta_{\mathrm{eff}, i}$ giữ ở mức cao, giúp tham số đón nhận các bước cập nhật lớn mỗi khi có tín hiệu.

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

Tính chất kỳ diệu của CG: Các hướng tìm kiếm $p_0, p_1, \ldots$ trực giao với nhau qua ma trận $H$ ($p_i^T H p_j = 0$ với mọi $i \ne j$). Trong số học chính xác, thuật toán CG giải đúng nghiệm của hệ $n$ chiều trong **tối đa không quá $n$ bước lặp**.

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

---

## Tóm tắt cốt lõi

1. **AdaGrad**: Khởi xướng cơ chế chia nhỏ tốc độ học theo tổng bình phương gradient dồn tích, phù hợp với dữ liệu thưa nhưng dễ bị tắt dần bước nhảy.
2. **RMSProp**: Thay thế tổng dồn tích bằng trung bình trượt hàm mũ (EMA), tạo ra cửa sổ bộ nhớ hữu hạn giúp duy trì khả năng học lâu dài.
3. **Adam**: Kết hợp tinh hoa của Momentum (hướng đi) và RMSProp (độ dài bước), tích hợp cơ chế hiệu chỉnh chệch khởi tạo chuẩn xác.
4. **Conjugate Gradient & BFGS**: Cung cấp công cụ xấp xỉ bậc hai siêu việt, giải phóng thuật toán khỏi gánh nặng tính toán và lưu trữ ma trận Hessian khổng lồ.

---

## Tài liệu tham khảo và Đọc thêm

Dành cho bạn đọc muốn nghiên cứu chuyên sâu về các thuật toán tối ưu thích nghi:
- **Diederik P. Kingma & Jimmy Ba** (2014), *Adam: A Method for Stochastic Optimization*, ICLR. Bài báo kinh điển đặt nền móng cho thuật toán Adam và cơ chế hiệu chỉnh chệch.
- **John Duchi, Elad Hazan & Yoram Singer** (2011), *Adaptive Subgradient Methods for Online Learning and Stochastic Optimization*, JMLR. Nguồn gốc của thuật toán AdaGrad và giải tích subgradient thích nghi.
- **Jonathan Richard Shewchuk**, *An Introduction to the Conjugate Gradient Method Without the Agonizing Pain*, Carnegie Mellon University. Tài liệu nhập môn trực quan và sâu sắc nhất về phương pháp Gradient liên hợp.

Tiếp theo: [Bài 07 — Quy hoạch tuyến tính và Quy hoạch động Bellman](./bai-07-quy-hoach-tuyen-tinh-va-dong.md).
