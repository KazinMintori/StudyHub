---
course: toan-cho-ai
lecture: bai-05-toi-uu-huan-luyen
section: lecture
title: "Các phương pháp tối ưu trong huấn luyện mô hình học sâu"
prerequisites: ["gradient", "quy-tac-chuoi", "ky-vong", "phuong-sai"]
lessonStatus: ready
description: "Phân biệt hàm mục tiêu thực nghiệm với khả năng khái quát hóa; làm chủ Mini-batch SGD, Momentum, Nesterov và nguyên lý khởi tạo Glorot."
---

Ở Bài 04, chúng ta giả định rằng tại mỗi bước lặp, thuật toán luôn tính toán được gradient chính xác tuyệt đối của toàn bộ hàm mục tiêu. Thế nhưng khi bước vào thế giới học sâu hiện đại, giả định đó lập tức vấp phải bức tường thực tế: Các tập dữ liệu huấn luyện (từ thị giác máy tính đến các mô hình ngôn ngữ lớn) thường chứa hàng triệu, thậm chí hàng nghìn tỷ mẫu dữ liệu. Việc duyệt qua toàn bộ dữ liệu chỉ để thực hiện một bước cập nhật tham số duy nhất là điều hoàn toàn bất khả thi về mặt tài nguyên và thời gian.

Để vượt qua giới hạn này, kỹ nghệ học sâu vận hành dựa trên nguyên lý tối ưu hóa ngẫu nhiên (stochastic optimization) then chốt: Thay vì tính toán gradient chính xác trên toàn bộ tập dữ liệu (Full-batch), ta ước lượng gradient thông qua một **lô dữ liệu nhỏ (mini-batch)** được lấy mẫu ngẫu nhiên. Bước chuyển dịch này kéo theo hàng loạt câu hỏi cốt lõi:
- Làm sao bảo đảm gradient trên lô nhỏ phản ánh đúng xu hướng suy giảm chung của toàn bộ dữ liệu?
- Làm thế nào để kiểm soát và chế ngự phương sai nhiễu ngẫu nhiên sinh ra từ việc lấy mẫu?
- Cơ chế quán tính (Momentum) và kỹ thuật nhìn trước (Nesterov) giúp thuật toán vượt qua các thung lũng hẹp và điểm yên ngựa ra sao?
- Tại sao việc khởi tạo trọng số ngẫu nhiên lại quyết định sự sống còn của dòng chảy tín hiệu trong các mạng nơ-ron sâu?

---

## 1. Hàm mục tiêu thực nghiệm và Ranh giới Khái quát hóa

Trong học máy có giám sát, ta có một tập huấn luyện gồm $N$ mẫu dữ liệu $D = \{(x_i, y_i)\}_{i=1}^N$. Với vector tham số mô hình $\theta \in \mathbb{R}^d$ và hàm mất mát trên mẫu thứ $i$ là $\ell_i(\theta) = \ell(f_\theta(x_i), y_i)$, hàm mục tiêu huấn luyện được định nghĩa bằng **mất mát thực nghiệm trung bình (Empirical Risk)**:

$$
J(\theta) = \frac{1}{N} \sum_{i=1}^N \ell_i(\theta) = \frac{\ell_1(\theta) + \ell_2(\theta) + \cdots + \ell_N(\theta)}{N}.
$$

Nếu áp dụng kỹ thuật điều chuẩn (regularization), ta cộng thêm số hạng phạt độ phức tạp $\rho R(\theta)$ (với hệ số phạt $\rho > 0$). Gradient của hàm mục tiêu theo tham số $\theta$ được tính bằng thuật toán lan truyền ngược (backpropagation), về bản chất là việc áp dụng quy tắc chuỗi giải tích trên đồ thị tính toán của mạng nơ-ron.

Ở đây, chúng ta cần phân biệt rạch ròi giữa hai mục tiêu hoàn toàn khác nhau:
1. **Bài toán tối ưu (Optimization)**: Tìm bộ tham số $\theta$ để cực tiểu hóa hàm mất mát thực nghiệm $J(\theta)$ trên dữ liệu đã biết trong tập huấn luyện.
2. **Khả năng khái quát hóa (Generalization)**: Đo lường chất lượng dự đoán của mô hình trên phân phối dữ liệu thực tế chưa từng xuất hiện trong quá trình huấn luyện.

Một thuật toán tối ưu hội tụ hoàn hảo về điểm có mất mát bằng 0 trên tập huấn luyện hoàn toàn không đồng nghĩa với việc mô hình sẽ hoạt động tốt trên thực tế vì mô hình có thể rơi vào bẫy học vẹt (overfitting). Do đó, trong thực hành ta luôn chia tách dữ liệu thành:
- **Tập huấn luyện (Training set)**: Dùng trực tiếp để tính gradient và cập nhật tham số.
- **Tập xác thực (Validation set)**: Dùng để tinh chỉnh siêu tham số và theo dõi hiện tượng overfitting.
- **Tập kiểm thử (Test set)**: Giữ độc lập tuyệt đối cho lần đánh giá năng lực cuối cùng.

---

## 2. Gradient ước lượng từ Lô nhỏ (Mini-batch Gradient)

Do phép lấy đạo hàm có tính tuyến tính, gradient của hàm mất mát thực nghiệm bằng trung bình cộng các gradient trên từng mẫu:

$$
\nabla J(\theta) = \frac{1}{N} \sum_{i=1}^N \nabla \ell_i(\theta).
$$

Thay vì tính tổng trên toàn bộ $N$ mẫu, tại mỗi bước lặp ta chọn ngẫu nhiên một **lô nhỏ (mini-batch)** gồm $B$ mẫu ($B \ll N$), ký hiệu tập chỉ số là $\mathcal{B} = \{I_1, I_2, \ldots, I_B\}$. Vector **gradient lô nhỏ** được tính bằng:

$$
g_B(\theta) = \frac{1}{B} \sum_{j=1}^B \nabla \ell_{I_j}(\theta).
$$

### Tính không chệch và Phương sai của ước lượng
Nếu các chỉ số $I_j$ được lấy mẫu ngẫu nhiên đều trên tập $\{1, \ldots, N\}$, kỳ vọng có điều kiện của gradient lô nhỏ thỏa mãn:

$$
\mathbb{E}[g_B(\theta) \mid \theta] = \frac{1}{B} \sum_{j=1}^B \mathbb{E}[\nabla \ell_{I_j}(\theta)] = \frac{1}{B} \sum_{j=1}^B \nabla J(\theta) = \nabla J(\theta).
$$

Đẳng thức này khẳng định $g_B(\theta)$ là một **ước lượng không chệch (unbiased estimator)** của gradient toàn bộ tập dữ liệu.

Tuy nhiên, ước lượng này đi kèm với **phương sai ngẫu nhiên**. Giả sử phương sai của gradient trên một mẫu đơn lẻ là $\sigma_g^2$. Khi lấy trung bình trên $B$ mẫu độc lập, phương sai của gradient lô nhỏ giảm tỉ lệ nghịch với kích thước lô:

$$
\operatorname{Var}(g_B(\theta)) = \frac{\sigma_g^2}{B}.
$$

Định luật này giải thích vì sao kích thước lô $B$ đóng vai trò chiếc van điều tiết giữa độ chính xác và tốc độ tính toán:
- Tăng kích thước lô $B$ làm giảm phương sai, gradient ít bị nhiễu hơn, cho phép bước đi ổn định hơn.
- Nhưng khi $B$ tăng quá lớn, chi phí tính toán tăng tuyến tính trong khi phương sai chỉ giảm với tốc độ căn bậc hai ($1/\sqrt{B}$), dẫn tới hiệu suất biên giảm dần. 
- Thú vị hơn, trong học sâu, chính sự dao động ngẫu nhiên của các lô nhỏ vừa phải ($B \in [32, 256]$) lại hoạt động như một cơ chế điều chuẩn ngầm, giúp mô hình thoát khỏi các hố cực tiểu cục bộ nhọn (sharp minima) và định vị các cực tiểu phẳng (flat minima) có tính khái quát hóa bền bỉ hơn!

::: example Quan sát nhiễu ngẫu nhiên trên mô hình một tham số
Xét tập dữ liệu cực nhỏ gồm hai mẫu có nhãn $b_1 = 0$ và $b_2 = 2$.
Mô hình đưa ra dự đoán đơn tham số $\theta$ với hàm mất mát bình phương $\ell_i(\theta) = \frac{1}{2}(\theta - b_i)^2$.
Hàm mục tiêu trên toàn bộ tập dữ liệu là:
$$
\begin{aligned}
J(\theta) &= \frac{1}{2}\left[\frac{1}{2}(\theta - 0)^2 + \frac{1}{2}(\theta - 2)^2\right] \\
&= \frac{1}{4}(2\theta^2 - 4\theta + 4) = \frac{1}{2}(\theta - 1)^2 + \frac{1}{2}.
\end{aligned}
$$

Gradient toàn phần là $\nabla J(\theta) = \theta - 1$. Nghiệm tối ưu thực sự là $\theta^* = 1$.
- Tại $\theta = 0$: Gradient mẫu 1 là $\nabla\ell_1(0) = 0 - 0 = 0$. Gradient mẫu 2 là $\nabla\ell_2(0) = 0 - 2 = -2$. Gradient toàn phần là $\nabla J(0) = -1$.
  Nếu cập nhật với tốc độ học $\eta = 0.1$:
  - Cập nhật full-batch: $\theta^+ = 0 - 0.1(-1) = 0.1$.
  - Nếu gặp riêng mẫu 1: $\theta^+ = 0 - 0.1(0) = 0$ (đứng yên).
  - Nếu gặp riêng mẫu 2: $\theta^+ = 0 - 0.1(-2) = 0.2$.
  Trung bình cập nhật của hai mẫu độc lập đúng bằng $0.1$.
- Tại điểm tối ưu $\theta = 1$: Gradient toàn phần triệt tiêu hoàn toàn ($\nabla J(1) = 0$). Thế nhưng gradient của từng mẫu đơn lẻ lần lượt là $\nabla\ell_1(1) = 1$ và $\nabla\ell_2(1) = -1$. Do đó, một bước SGD với tốc độ học cố định sẽ tiếp tục nhảy lệch khỏi điểm tối ưu thay vì dừng lại!
:::

<details><summary>Câu hỏi đào sâu: Tại điểm cực tiểu toàn cục $\theta = 1$, nếu bước cập nhật bốc phải mẫu $b = 0$ với $\eta = 0.1$, hàm mất mát toàn phần sẽ biến thiên ra sao?</summary>

Tại $\theta = 1$, giá trị mất mát toàn phần là $J(1) = 0.5$. Nếu gặp mẫu $b = 0$, gradient là $1 - 0 = 1$, điểm mới trở thành $\theta^+ = 1 - 0.1(1) = 0.9$. Giá trị mất mát mới là:
$$J(0.9) = \frac{1}{2}(0.9 - 1)^2 + 0.5 = 0.505 > 0.5.$$ 

Mất mát đã **tăng lên**! Điều này cho thấy tính không chệch của gradient chỉ là một bảo đảm về mặt kỳ vọng thống kê; nó tuyệt đối không bảo đảm rằng hàm mục tiêu sẽ giảm sau từng bước cập nhật ngẫu nhiên đơn lẻ.

</details>

---

## 3. Thuật toán Stochastic Gradient Descent (SGD)

Thuật toán **Stochastic Gradient Descent (SGD)** cập nhật tham số tại bước thứ $t$ theo quy tắc:

$$
\theta_{t+1} = \theta_t - \eta_t g_{B_t}(\theta_t),
$$

trong đó $\eta_t > 0$ là tốc độ học tại bước $t$, và $g_{B_t}(\theta_t)$ là gradient tính trên lô nhỏ $B_t$.

Một **epoch** được định nghĩa là một chu trình hoàn chỉnh duyệt qua toàn bộ tập dữ liệu huấn luyện. Trong thực hành, người ta xáo trộn ngẫu nhiên (shuffle) tập dữ liệu ở đầu mỗi epoch, sau đó chia thành các lô nhỏ liên tiếp không hoàn lại.

Vì gradient lô nhỏ luôn chứa thành phần nhiễu ngẫu nhiên, thuật toán không thể hội tụ về điểm dừng nếu giữ nguyên tốc độ học cố định $\eta$. Để bảo đảm sự hội tụ tiệm cận, lịch trình giảm tốc độ học (learning rate schedule) phải thỏa mãn **điều kiện Robbins–Monro**:

$$
\sum_{t=1}^\infty \eta_t = \infty \quad \text{và} \quad \sum_{t=1}^\infty \eta_t^2 < \infty.
$$

Điều kiện thứ nhất bảo đảm bước đi đủ dài để đi tới nghiệm dù xuất phát từ bất kỳ đâu; điều kiện thứ hai bảo đảm phương sai tích lũy của nhiễu bị triệt tiêu dần khi tiệm cận nghiệm.

Đoạn mã Python mô phỏng chính xác thuật toán SGD trên mô hình đơn tham số:

```python
def sgd_scalar(theta, targets, rate, draws):
    history = [theta]
    for i in draws:  # chỉ số lấy mẫu được cung cấp để tái lập
        gradient = theta-targets[i]
        theta -= rate*gradient
        history.append(theta)
    return history

print(sgd_scalar(0.0, [0.0, 2.0], 0.1, [0, 1, 0, 1]))
# [0.0, 0.0, 0.2, 0.18, 0.362]
```

---

## 4. Cơ chế Quán tính: Momentum và Trạng thái Vận tốc

Khi bề mặt hàm mất mát có dạng hẻm núi hẹp (độ cong theo một số hướng lớn hơn gấp nhiều lần các hướng khác), SGD sẽ dao động mạnh qua lại giữa hai sườn dốc và di chuyển rất chậm chạp dọc theo đáy thung lũng.

Thuật toán **Momentum** mượn ý tưởng trực quan từ cơ học cổ điển: Coi tham số như một hòn bi có khối lượng lăn trên bề mặt thế năng mất mát. Hòn bi tích lũy vận tốc theo thời gian, giúp nó vượt qua các gờ nhấp nhô và giữ đà lao nhanh dọc theo hướng dốc chính.

Khởi tạo vector vận tốc $v_0 = 0$, tại mỗi bước ta cập nhật theo quy tắc:

$$
v_{t+1} = \mu v_t - \eta g_t, \qquad \theta_{t+1} = \theta_t + v_{t+1},
$$

trong đó $\mu \in [0, 1)$ là hệ số ma sát quán tính (thường chọn $\mu = 0.9$).

Ý nghĩa của hệ số $\mu$:
- Nếu các vector gradient ở các bước liên tiếp cùng hướng, số hạng vận tốc sẽ tích lũy theo cấp số nhân:
  $$v \approx -\frac{\eta}{1 - \mu} g.$$
  Với $\mu = 0.9$, bước nhảy thực tế dọc theo hướng ổn định sẽ được khuếch đại gấp 10 lần!
- Nếu các vector gradient liên tục đổi dấu (như dao động giữa hai sườn dốc hẹp), các số hạng sẽ triệt tiêu lẫn nhau trong tổng vận tốc, giúp dập tắt dao động ziczac.

::: example Tính toán định lượng hai bước lặp Momentum
Xét hàm số $J(\theta) = \frac{1}{2}(\theta - 1)^2 + \frac{1}{2}$, gradient là $g(\theta) = \theta - 1$.
Khởi tạo $\theta_0 = 0$, $v_0 = 0$, tốc độ học $\eta = 0.1$, hệ số quán tính $\mu = 0.9$.
- **Bước 1**:
  - Gradient: $g_0 = 0 - 1 = -1$.
  - Vận tốc mới: $v_1 = 0.9(0) - 0.1(-1) = 0.1$.
  - Cập nhật vị trí: $\theta_1 = 0 + 0.1 = 0.1$.
- **Bước 2**:
  - Gradient: $g_1 = 0.1 - 1 = -0.9$.
  - Vận tốc mới:
    $$v_2 = 0.9(0.1) - 0.1(-0.9) = 0.09 + 0.09 = 0.18.$$
  - Cập nhật vị trí: $\theta_2 = 0.1 + 0.18 = 0.28$.

Để so sánh: Gradient Descent thuần túy ở bước 2 chỉ đạt tới $\theta_2 = 0.19$. Nhờ tích lũy quán tính từ bước 1 ($0.09$), Momentum đã đẩy vị trí tiến xa hơn đáng kể hướng về phía nghiệm $\theta^* = 1$.
:::

---

## 5. Nesterov Accelerated Gradient (NAG): Kỹ thuật Nhìn trước

Mặc dù Momentum thông thường tăng tốc rất tốt, nhược điểm của nó là có thể tích lũy quán tính quá lớn và lao vọt qua đáy thung lũng trước khi kịp hãm phanh.

**Nesterov Accelerated Gradient (NAG)** giải quyết điều này bằng một cơ chế thông minh: Tính toán gradient tại **vị trí nhìn trước (lookahead point)** thay vì tại vị trí hiện tại.

Quy tắc cập nhật Nesterov:
1. Dự phóng vị trí tương lai theo quán tính thuần túy: $\widetilde\theta_t = \theta_t + \mu v_t$.
2. Đo độ dốc địa hình tại điểm dự phóng: $g_t = \nabla J(\widetilde\theta_t)$.
3. Cập nhật vận tốc và vị trí:
   $$v_{t+1} = \mu v_t - \eta g_t, \qquad \theta_{t+1} = \theta_t + v_{t+1}.$$

Sự khác biệt cốt tử giữa Momentum và Nesterov nằm ở **vị trí lấy đạo hàm**:
- Momentum thông thường: Tính gradient tại điểm đang đứng $\theta_t$, rồi mới cộng quán tính $\mu v_t$.
- Nesterov: Nhảy một bước thử theo quán tính tới $\widetilde\theta_t$, quan sát xem phía trước dốc lên hay dốc xuống để tự động "nhấn phanh" hãm đà nếu sắp lao qua đỉnh đối diện!

::: example Kiểm chứng bước Nesterov trên cùng bài toán
Với bài toán $J(\theta) = \frac{1}{2}(\theta - 1)^2 + \frac{1}{2}$, khởi tạo $\theta_0 = 0, v_0 = 0, \eta = 0.1, \mu = 0.9$:
- Bước 1: Vì $v_0 = 0$, điểm nhìn trước trùng điểm hiện tại $\widetilde\theta_0 = 0$. Kết quả thu được $v_1 = 0.1, \theta_1 = 0.1$ (giống Momentum).
- Bước 2:
  - Điểm nhìn trước: $\widetilde\theta_1 = \theta_1 + \mu v_1 = 0.1 + 0.9(0.1) = 0.19$.
  - Gradient tại điểm nhìn trước: $g_1 = \nabla J(0.19) = 0.19 - 1 = -0.81$.
  - Vận tốc mới:
    $$v_2 = 0.9(0.1) - 0.1(-0.81) = 0.09 + 0.081 = 0.171.$$
  - Cập nhật vị trí: $\theta_2 = 0.1 + 0.171 = 0.271$.

Ta thấy vận tốc Nesterov ($0.171$) nhỏ hơn một chút so với Momentum thông thường ($0.18$) vì nó đã phát hiện ra rằng quán tính đang đưa điểm tới gần đáy hơn, từ đó tự động hiệu chỉnh bước đi chính xác và mượt mà hơn.
:::

<MathLab type="optimizer" initial-method="momentum">

```js
const lookahead = point.map((x,i) => x+mu*velocity[i]);
const g = gradient(lookahead);
velocity = velocity.map((v,i) => mu*v-rate*g[i]);
point = point.map((x,i) => x+velocity[i]);
```

</MathLab>

---

## 6. Khởi tạo Trọng số và Nguyên lý Bảo toàn Phương sai Glorot (Xavier)

Trước khi thuật toán tối ưu hóa bắt đầu bước đi đầu tiên, bài toán đặt ra là: **Nên khởi tạo các trọng số của mạng nơ-ron như thế nào?**

Nếu ta khởi tạo toàn bộ trọng số của một tầng ẩn bằng 0:
- Tất cả các nơ-ron trong tầng đó sẽ nhận tín hiệu đầu vào giống nhau và sinh ra đầu ra giống hệt nhau.
- Trong pha lan truyền ngược, tất cả các nơ-ron sẽ nhận cùng một gradient, dẫn tới việc chúng được cập nhật cùng một giá trị như nhau ở mọi bước lặp.
- Mạng nơ-ron hoàn toàn mất khả năng học các đặc trưng đa dạng, hiện tượng này được gọi là **sự sụp đổ đối xứng (symmetry trap)**.

Để phá vỡ đối xứng, ta bắt buộc phải khởi tạo trọng số ngẫu nhiên. Nhưng ngẫu nhiên với phương sai bao nhiêu?
- Nếu phương sai quá lớn: Tín hiệu kích hoạt sẽ phóng đại theo cấp số nhân qua các tầng, dẫn tới hiện tượng **bùng nổ gradient (exploding gradients)**.
- Nếu phương sai quá nhỏ: Tín hiệu kích hoạt sẽ suy giảm dần về 0 khi đi sâu vào mạng, dẫn tới hiện tượng **triệt tiêu gradient (vanishing gradients)**.

### Phân tích bảo toàn phương sai của Xavier Glorot & Yoshua Bengio (2010)
Xét một nơ-ron tuyến tính tính tổng trọng số $z = \sum_{i=1}^{n_{\mathrm{in}}} W_i x_i$. Giả sử các đầu vào $x_i$ và trọng số $W_i$ độc lập thống kê với nhau, có kỳ vọng bằng 0 và phương sai lần lượt là $\operatorname{Var}(x)$ và $\operatorname{Var}(W)$.

Phương sai của tổ hợp tuyến tính là:

$$
\operatorname{Var}(z) = \sum_{i=1}^{n_{\mathrm{in}}} \operatorname{Var}(W_i x_i) = n_{\mathrm{in}} \operatorname{Var}(W) \operatorname{Var}(x).
$$

Để phương sai của tín hiệu không bị phóng đại hay triệt tiêu khi truyền xuôi qua tầng ($\operatorname{Var}(z) = \operatorname{Var}(x)$), ta cần:

$$
\operatorname{Var}(W) = \frac{1}{n_{\mathrm{in}}}.
$$

Mặt khác, trong pha lan truyền ngược, để bảo toàn phương sai của gradient truyền từ tầng sau ($n_{\mathrm{out}}$ nơ-ron) về tầng trước, phân tích tương tự đòi hỏi:

$$
\operatorname{Var}(W) = \frac{1}{n_{\mathrm{out}}}.
$$

Không thể đồng thời thỏa mãn cả hai điều kiện khi $n_{\mathrm{in}} \ne n_{\mathrm{out}}$. Glorot & Bengio đề xuất giải pháp dung hòa bằng trung bình điều hòa của hai đại lượng:

$$
\boxed{\operatorname{Var}(W) = \frac{2}{n_{\mathrm{in}} + n_{\mathrm{out}}}.}
$$

Nếu khởi tạo theo phân phối đều đối xứng $W \sim U[-a, a]$, vì phân phối đều có phương sai $\operatorname{Var}(W) = \frac{a^2}{3}$, ta thu được cận biên độ:

$$
\frac{a^2}{3} = \frac{2}{n_{\mathrm{in}} + n_{\mathrm{out}}} \implies a = \sqrt{\frac{6}{n_{\mathrm{in}} + n_{\mathrm{out}}}}.
$$

Chẳng hạn với một tầng có 4 đầu vào ($n_{\mathrm{in}} = 4$) và 2 đầu ra ($n_{\mathrm{out}} = 2$):
- Biên độ phân phối đều: $a = \sqrt{\frac{6}{4 + 2}} = \sqrt{1} = 1$.
- Trọng số được lấy mẫu từ $W \sim U[-1, 1]$ với phương sai $\operatorname{Var}(W) = \frac{1^2}{3} = \frac{1}{3}$.

---

## Bài tập tự luyện

::: exercise 1. Tính toán gradient lô nhỏ
Xét bài toán một tham số với hai mẫu $b_1 = 0$ và $b_2 = 2$, hàm mất mát $\ell_i(\theta) = \frac{1}{2}(\theta - b_i)^2$.
Tại điểm $\theta = 0.5$:
1. Tính gradient của từng mẫu riêng biệt $\nabla\ell_1(0.5)$ và $\nabla\ell_2(0.5)$.
2. Tính gradient của lô chứa cả hai mẫu và so sánh với đạo hàm toàn phần $J'(0.5)$.
:::
::: solution
1. Gradient từng mẫu:
   - Mẫu 1: $\nabla\ell_1(0.5) = 0.5 - 0 = 0.5$.
   - Mẫu 2: $\nabla\ell_2(0.5) = 0.5 - 2 = -1.5$.
2. Gradient của lô hai mẫu:
   $$g_B(0.5) = \frac{0.5 + (-1.5)}{2} = \frac{-1.0}{2} = -0.5.$$
   Đạo hàm toàn phần:
   $$J(\theta) = \frac{1}{2}(\theta - 1)^2 + \frac{1}{2} \implies J'(0.5) = 0.5 - 1 = -0.5.$$
   Hai kết quả trùng khớp hoàn hảo. Chú ý: Nếu cộng các gradient mà quên chia cho kích thước lô $B = 2$, ta sẽ thu được $-1.0$, làm sai lệch thang đo của bước cập nhật.
:::

::: exercise 2. Thực hiện bước thứ ba của thuật toán Momentum
Tiếp tục ví dụ ở mục 4: Tại cuối bước 2, ta có $\theta_2 = 0.28$ và $v_2 = 0.18$.
Hãy tính toán chi tiết bước lặp thứ 3 với gradient toàn phần, tốc độ học $\eta = 0.1$ và hệ số quán tính $\mu = 0.9$.
:::
::: solution
- Tính gradient tại vị trí hiện tại $\theta_2 = 0.28$:
  $$g_2 = \theta_2 - 1 = 0.28 - 1 = -0.72.$$
- Cập nhật vận tốc mới $v_3$:
  $$v_3 = \mu v_2 - \eta g_2 = 0.9(0.18) - 0.1(-0.72) = 0.162 + 0.072 = 0.234.$$
- Cập nhật vị trí mới $\theta_3$:
  $$\theta_3 = \theta_2 + v_3 = 0.28 + 0.234 = 0.514.$$
Vận tốc tiếp tục tăng từ $0.18$ lên $0.234$, giúp đẩy tham số vượt qua mốc giữa đường ($0.5$) chỉ sau 3 bước lặp.
:::

::: exercise 3. Tính toán tham số khởi tạo Glorot cho tầng ẩn
Một tầng ẩn trong mạng nơ-ron sâu nhận 8 đầu vào ($n_{\mathrm{in}} = 8$) và kết nối tới 4 nơ-ron ở tầng kế tiếp ($n_{\mathrm{out}} = 4$).
1. Xác định phương sai khởi tạo Glorot cho ma trận trọng số của tầng này.
2. Nếu dùng phân phối đều $U[-a, a]$, hãy tính giá trị cận biên $a$.
:::
::: solution
1. Phương sai Glorot chuẩn hóa:
   $$\operatorname{Var}(W) = \frac{2}{n_{\mathrm{in}} + n_{\mathrm{out}}} = \frac{2}{8 + 4} = \frac{2}{12} = \frac{1}{6} \approx 0.1667.$$
2. Biên độ phân phối đều:
   $$a = \sqrt{\frac{6}{n_{\mathrm{in}} + n_{\mathrm{out}}}} = \sqrt{\frac{6}{12}} = \sqrt{\frac{1}{2}} = \frac{1}{\sqrt{2}} \approx 0.7071.$$
Trọng số của tầng này cần được lấy mẫu ngẫu nhiên từ phân phối $U[-0.7071, 0.7071]$.
:::

::: exercise 4. Phân tích thống kê: Kỳ vọng, hiệp phương sai và nhiễu của gradient mini-batch
Cho tập dữ liệu huấn luyện gồm $N$ mẫu quan sát $\{z_1, \dots, z_N\}$. Hàm mất mát thực nghiệm trên toàn bộ tập dữ liệu là:
$$
f(\theta) = \frac{1}{N} \sum_{i=1}^N \ell(\theta, z_i).
$$
Tại mỗi bước lặp, thuật toán Mini-batch SGD chọn ngẫu nhiên đồng đều không hoàn lại một tập chỉ số $B \subset \{1, \dots, N\}$ gồm $|B| = m$ mẫu ($1 \le m \le N$), và tính gradient xấp xỉ:
$$
g_B(\theta) = \frac{1}{m} \sum_{i \in B} \nabla_\theta \ell(\theta, z_i).
$$
1. Chứng minh rằng $g_B(\theta)$ là một ước lượng không chệch của gradient toàn thể $\nabla f(\theta)$: $\mathbb{E}[g_B(\theta)] = \nabla f(\theta)$.
2. Giả sử gradient của từng mẫu đơn lẻ có ma trận hiệp phương sai bị chặn: $\operatorname{Cov}\big(\nabla \ell(\theta, z_i)\big) \preceq \sigma^2 I$. Trong trường hợp lấy mẫu độc lập có hoàn lại, hãy tính ma trận hiệp phương sai của $g_B(\theta)$ theo kích thước lô $m$.
3. Nêu ý nghĩa của tỉ số tín hiệu trên nhiễu (SNR) của gradient: Tại sao khi tăng kích thước lô $m$ lên 4 lần thì độ lệch chuẩn của nhiễu chỉ giảm đi 2 lần?
:::

::: solution
1. **Tính không chệch của gradient mini-batch**:
   Đặt biến ngẫu nhiên chỉ thị $I_i = \mathbb{I}(i \in B)$.
   Xác suất để một mẫu thứ $i$ bất kỳ lọt vào lô kích thước $m$ là:
   $$
   \mathbb{P}(i \in B) = \frac{m}{N} \implies \mathbb{E}[I_i] = \frac{m}{N}.
   $$
   Gradient mini-batch được viết lại dưới dạng:
   $$
   g_B(\theta) = \frac{1}{m} \sum_{i=1}^N I_i \nabla \ell(\theta, z_i).
   $$
   Lấy kỳ vọng toán học theo phân phối chọn mẫu:
   $$
   \begin{aligned}
   \mathbb{E}[g_B(\theta)] &= \frac{1}{m} \sum_{i=1}^N \mathbb{E}[I_i] \nabla \ell(\theta, z_i) \\
   &= \frac{1}{m} \sum_{i=1}^N \left(\frac{m}{N}\right) \nabla \ell(\theta, z_i) \\
   &= \frac{1}{N} \sum_{i=1}^N \nabla \ell(\theta, z_i) = \nabla f(\theta).
   \end{aligned}
   $$
   Đẳng thức này khẳng định $g_B(\theta)$ là một ước lượng không chệch của gradient chân thực.

2. **Ma trận hiệp phương sai của gradient**:
   Khi các mẫu trong lô được rút độc lập có hoàn lại (i.i.d.), các biến ngẫu nhiên $\nabla \ell(\theta, z_i)$ là độc lập cùng phân phối.
   Hiệp phương sai của tổng các biến độc lập bằng tổng các hiệp phương sai:
   $$
   \begin{aligned}
   \operatorname{Cov}\big(g_B(\theta)\big) &= \operatorname{Cov}\left(\frac{1}{m} \sum_{i \in B} \nabla \ell(\theta, z_i)\right) \\
   &= \frac{1}{m^2} \sum_{i \in B} \operatorname{Cov}\big(\nabla \ell(\theta, z_i)\big) \\
   &\preceq \frac{1}{m^2} \big(m \sigma^2 I\big) = \frac{\sigma^2}{m} I.
   \end{aligned}
   $$
   Phương sai của vector gradient tỷ lệ nghịch chính xác với kích thước lô $m$.

3. **Ý nghĩa của tỉ số tín hiệu trên nhiễu (SNR)**:
   Tín hiệu định hướng của gradient là vector kỳ vọng $\|\nabla f(\theta)\|_2$, trong khi độ lớn của nhiễu ngẫu nhiên được đo bằng độ lệch chuẩn:
   $$
   \text{Độ lệch chuẩn nhiễu} = \sqrt{\operatorname{Tr}(\operatorname{Cov})} \propto \frac{\sigma}{\sqrt{m}}.
   $$
   Tỉ số tín hiệu trên nhiễu tăng theo quy luật căn bậc hai $\sqrt{m}$:
   $$
   \text{SNR} = \frac{\|\nabla f(\theta)\|_2}{\sigma / \sqrt{m}} \propto \sqrt{m}.
   $$
   Do đó, muốn giảm một nửa biên độ dao động ngẫu nhiên của bước nhảy gradient, ta bắt buộc phải tăng gấp bốn lần chi phí tính toán của mỗi lô ($m \to 4m$). Đây chính là nguyên nhân kinh tế và tính toán khiến các kích thước lô vừa phải ($m \in [32, 256]$) trở thành tiêu chuẩn vàng trong huấn luyện học sâu thực tế.
:::

::: exercise 5. Bất đẳng thức bước giảm (Descent Lemma) và tốc độ hội tụ của SGD
Cho hàm mục tiêu $f: \mathbb{R}^d \to \mathbb{R}$ khả vi và có gradient thỏa mãn điều kiện Lipschitz với hằng số $L > 0$:
$$
\|\nabla f(x) - \nabla f(y)\|_2 \le L \|x - y\|_2 \quad \forall x, y \in \mathbb{R}^d.
$$
1. Bổ đề giảm bước (Descent Lemma): Chứng minh rằng với mọi $x, y \in \mathbb{R}^d$, ta luôn có bất đẳng thức bậc hai chặn trên:
   $$
   f(y) \le f(x) + \nabla f(x)^T (y - x) + \frac{L}{2}\|y - x\|_2^2.
   $$
2. Xét bước cập nhật hạ gradient ngẫu nhiên: $\theta_{t+1} = \theta_t - \eta g_t$, với $\mathbb{E}[g_t \mid \theta_t] = \nabla f(\theta_t)$ và $\mathbb{E}[\|g_t\|_2^2 \mid \theta_t] \le G^2$. Chứng minh rằng:
   $$
   \mathbb{E}[f(\theta_{t+1}) \mid \theta_t] \le f(\theta_t) - \eta \left(1 - \frac{\eta L}{2}\right) \|\nabla f(\theta_t)\|_2^2 + \frac{\eta^2 L G^2}{2}.
   $$
3. Nếu chọn tốc độ học cố định $\eta < \frac{2}{L}$, hãy giải thích tại sao SGD không hội tụ về điểm dừng chính xác $\nabla f(\theta) = 0$ mà chỉ dao động quanh một quả cầu sai số phụ thuộc vào phương sai nhiễu $G^2$.
:::

::: solution
1. **Chứng minh Descent Lemma**:
   Theo định lý cơ bản của giải tích vi tích phân:
   $$
   f(y) - f(x) = \int_0^1 \nabla f\big(x + \tau (y - x)\big)^T (y - x) \, \mathrm{d}\tau.
   $$
   Cộng và trừ số hạng $\nabla f(x)^T (y - x)$:
   $$
   f(y) - f(x) - \nabla f(x)^T (y - x) = \int_0^1 \Big[\nabla f\big(x + \tau (y - x)\big) - \nabla f(x)\Big]^T (y - x) \, \mathrm{d}\tau.
   $$
   Áp dụng bất đẳng thức Cauchy-Schwarz và tính chất Lipschitz của gradient:
   $$
   \begin{aligned}
   \left|f(y) - f(x) - \nabla f(x)^T (y - x)\right| &\le \int_0^1 \left\|\nabla f\big(x + \tau(y - x)\big) - \nabla f(x)\right\|_2 \|y - x\|_2 \, \mathrm{d}\tau \\
   &\le \int_0^1 L \tau \|y - x\|_2^2 \, \mathrm{d}\tau = L \|y - x\|_2^2 \left[\frac{\tau^2}{2}\right]_0^1 = \frac{L}{2}\|y - x\|_2^2.
   \end{aligned}
   $$
   Bỏ dấu giá trị tuyệt đối ta thu được bất đẳng thức bước giảm cần chứng minh.

2. **Kỳ vọng bước giảm của SGD**:
   Thay $x = \theta_t$ và $y = \theta_{t+1} = \theta_t - \eta g_t$ vào Descent Lemma:
   $$
   f(\theta_{t+1}) \le f(\theta_t) - \eta \nabla f(\theta_t)^T g_t + \frac{\eta^2 L}{2}\|g_t\|_2^2.
   $$
   Lấy kỳ vọng có điều kiện theo trạng thái hiện tại $\theta_t$:
   $$
   \begin{aligned}
   \mathbb{E}[f(\theta_{t+1}) \mid \theta_t] &\le f(\theta_t) - \eta \nabla f(\theta_t)^T \mathbb{E}[g_t \mid \theta_t] + \frac{\eta^2 L}{2}\mathbb{E}[\|g_t\|_2^2 \mid \theta_t] \\
   &= f(\theta_t) - \eta \|\nabla f(\theta_t)\|_2^2 + \frac{\eta^2 L}{2}\mathbb{E}[\|g_t\|_2^2 \mid \theta_t].
   \end{aligned}
   $$
   Tách $\mathbb{E}[\|g_t\|_2^2] = \|\nabla f(\theta_t)\|_2^2 + \sigma^2 \le G^2$:
   $$
   \mathbb{E}[f(\theta_{t+1}) \mid \theta_t] \le f(\theta_t) - \eta \left(1 - \frac{\eta L}{2}\right) \|\nabla f(\theta_t)\|_2^2 + \frac{\eta^2 L G^2}{2}.
   $$

3. **Phân tích quả cầu sai số của SGD**:
   Khi chọn tốc độ học cố định $\eta < 2/L$, hệ số giảm $c = \eta(1 - \eta L/2) > 0$.
   Tuy nhiên, luôn tồn tại số hạng nhiễu dương $\frac{\eta^2 L G^2}{2} > 0$.
   Hàm mục tiêu chỉ được bảo đảm giảm khi:
   $$
   \eta \left(1 - \frac{\eta L}{2}\right) \|\nabla f(\theta_t)\|_2^2 > \frac{\eta^2 L G^2}{2} \iff \|\nabla f(\theta_t)\|_2^2 > \frac{\eta L G^2}{2 - \eta L}.
   $$
   Khi mô hình tiến gần tới cực tiểu và gradient triệt tiêu dần, lực giảm của gradient bị áp đảo hoàn toàn bởi nhiễu ngẫu nhiên. Thuật toán không thể đứng yên mà sẽ dao động vĩnh viễn trong một lân cận bán kính $O(\sqrt{\eta G^2})$. Để hội tụ về đúng điểm dừng, ta bắt buộc phải giảm dần tốc độ học theo thời gian (learning rate decay, ví dụ $\eta_t = O(1/\sqrt{t})$).
:::

::: exercise 6. Cơ chế nhìn trước (Look-ahead) của Nesterov Accelerated Gradient (NAG)
Xét hàm toàn phương một chiều:
$$
f(\theta) = \frac{1}{2}\theta^2.
$$
Giả sử tại bước lặp hiện tại, vị trí là $\theta = 1$ và vận tốc quán tính tích lũy là $v = 1$. Tốc độ học là $\eta = 0{,}1$ và hệ số quán tính là $\mu = 0{,}9$.
1. Tính bước cập nhật theo thuật toán Polyak Heavy-Ball Momentum:
   - Tính gradient tại điểm hiện tại $g = f'(\theta)$.
   - Cập nhật vận tốc mới $v_{\text{Polyak}} = \mu v - \eta g$ và vị trí mới $\theta_{\text{Polyak}} = \theta + v_{\text{Polyak}}$.
2. Tính bước cập nhật theo thuật toán Nesterov Accelerated Gradient (NAG):
   - Tính vị trí nhìn trước $\theta_{\text{look}} = \theta + \mu v$.
   - Tính gradient tại vị trí nhìn trước $g_{\text{look}} = f'(\theta_{\text{look}})$.
   - Cập nhật vận tốc mới $v_{\text{NAG}} = \mu v - \eta g_{\text{look}}$ và vị trí mới $\theta_{\text{NAG}} = \theta + v_{\text{NAG}}$.
3. So sánh hai kết quả và giải thích cơ chế "hãm đà thông minh" của Nesterov giúp ngăn chặn hiện tượng trượt quá đà (overshooting).
:::

::: solution
1. **Thuật toán Polyak Momentum**:
   - Vị trí hiện tại: $\theta = 1$, vận tốc cũ $v = 1$.
   - Gradient tại vị trí hiện tại:
     $$
     g = f'(1) = 1.
     $$
   - Cập nhật vận tốc mới:
     $$
     v_{\text{Polyak}} = \mu v - \eta g = 0{,}9(1) - 0{,}1(1) = 0{,}9 - 0{,}1 = 0{,}8.
     $$
   - Cập nhật vị trí mới:
     $$
     \theta_{\text{Polyak}} = \theta + v_{\text{Polyak}} = 1 + 0{,}8 = 1{,}8.
     $$
   Nhận xét: Vị trí mới $\theta = 1{,}8$ bị đẩy ra xa cực tiểu $\theta^* = 0$ hơn so với vị trí ban đầu $\theta = 1$ do quán tính quá lớn.

2. **Thuật toán Nesterov (NAG)**:
   - Điểm nhìn trước (Look-ahead point):
     $$
     \theta_{\text{look}} = \theta + \mu v = 1 + 0{,}9(1) = 1{,}9.
     $$
   - Gradient tại điểm nhìn trước:
     $$
     g_{\text{look}} = f'(1{,}9) = 1{,}9.
     $$
   - Cập nhật vận tốc mới:
     $$
     v_{\text{NAG}} = \mu v - \eta g_{\text{look}} = 0{,}9(1) - 0{,}1(1{,}9) = 0{,}9 - 0{,}19 = 0{,}71.
     $$
   - Cập nhật vị trí mới:
     $$
     \theta_{\text{NAG}} = \theta + v_{\text{NAG}} = 1 + 0{,}71 = 1{,}71.
     $$

3. **Bản chất cơ chế hãm đà của Nesterov**:
   - Polyak tính gradient tại điểm cũ ($\theta = 1$) nên chỉ nhận được lực kéo về là $0{,}1$, khiến vận tốc sau khi trừ vẫn còn rất lớn ($0{,}8$).
   - Nesterov chủ động phóng tầm mắt tới vị trí mà quán tính sẽ đưa hạt vật chất tới ($\theta_{\text{look}} = 1{,}9$). Tại đó, độ dốc vách núi dốc hơn nhiều ($g_{\text{look}} = 1{,}9$), sinh ra một lực phanh ngược chiều mạnh hơn ($0{,}19$).
   - Nhờ lực phanh này, vận tốc của Nesterov bị triệt tiêu bớt ($0{,}71 < 0{,}8$), giúp hạt vật chất dừng lại sớm hơn và giảm thiểu chấn động dao động quanh điểm cực tiểu.
:::

::: exercise 7. Khởi tạo He (Kaiming) cho hàm kích hoạt ReLU và sự bảo toàn phương sai
Xét một tầng tuyến tính trong mạng nơ-ron: $y = W x$, trong đó $x \in \mathbb{R}^{n_{\text{in}}}$ là đầu vào, $W \in \mathbb{R}^{n_{\text{out}} \times n_{\text{in}}}$ là ma trận trọng số, và các phần tử $W_{ij}$ độc lập cùng phân phối với kỳ vọng bằng $0$ và phương sai $\operatorname{Var}(W)$. Ngay sau đó là hàm kích hoạt phi tuyến ReLU: $z = \operatorname{ReLU}(y) = \max(0, y)$.
1. Giả sử biến ngẫu nhiên đối xứng $y_i$ có phân phối chuẩn $\mathcal{N}(0, \sigma_y^2)$. Chứng minh rằng:
   $$
   \mathbb{E}[z_i^2] = \frac{1}{2}\sigma_y^2.
   $$
2. Để bảo toàn phương sai của tín hiệu qua các tầng mạng sâu ($\operatorname{Var}(z_i) = \operatorname{Var}(x_j)$), hãy chứng minh công thức khởi tạo He (Kaiming):
   $$
   \operatorname{Var}(W) = \frac{2}{n_{\text{in}}}.
   $$
3. Giải thích tại sao nếu dùng công thức Glorot $\operatorname{Var}(W) = \frac{2}{n_{\text{in}} + n_{\text{out}}}$ cho mạng sâu dùng ReLU, phương sai tín hiệu sẽ bị triệt tiêu theo cấp số nhân qua từng tầng.
:::

::: solution
1. **Kỳ vọng bình phương qua hàm kích hoạt ReLU**:
   Biến ngẫu nhiên $y_i \sim \mathcal{N}(0, \sigma_y^2)$ có hàm mật độ xác suất đối xứng quanh $0$: $p(y) = p(-y)$.
   Biến đổi qua ReLU: $z_i = \max(0, y_i)$.
   Kỳ vọng bình phương được tính bằng tích phân:
   $$
   \mathbb{E}[z_i^2] = \int_{-\infty}^{+\infty} \max(0, y)^2 p(y) \, \mathrm{d}y = \int_0^{+\infty} y^2 p(y) \, \mathrm{d}y.
   $$
   Do tính đối xứng của hàm mật độ chuẩn:
   $$
   \int_0^{+\infty} y^2 p(y) \, \mathrm{d}y = \frac{1}{2} \int_{-\infty}^{+\infty} y^2 p(y) \, \mathrm{d}y = \frac{1}{2}\mathbb{E}[y_i^2] = \frac{1}{2}\sigma_y^2.
   $$
   Hàm kích hoạt ReLU triệt tiêu đúng một nửa năng lượng tín hiệu ở phần âm.

2. **Thiết lập công thức khởi tạo He (Kaiming)**:
   Xét thành phần thứ $i$ của đầu ra tuyến tính $y_i = \sum_{j=1}^{n_{\text{in}}} W_{ij} x_j$.
   Vì $W_{ij}$ và $x_j$ độc lập, kỳ vọng $\mathbb{E}[W_{ij}] = 0$:
   $$
   \operatorname{Var}(y_i) = \sum_{j=1}^{n_{\text{in}}} \operatorname{Var}(W_{ij} x_j) = n_{\text{in}} \operatorname{Var}(W) \mathbb{E}[x_j^2].
   $$
   Kế tiếp, qua tầng ReLU, theo kết quả câu 1:
   $$
   \mathbb{E}[z_i^2] = \frac{1}{2}\operatorname{Var}(y_i) = \frac{1}{2} n_{\text{in}} \operatorname{Var}(W) \mathbb{E}[x_j^2].
   $$
   Để năng lượng tín hiệu không bị co cụm hay bùng nổ qua từng tầng ($\mathbb{E}[z_i^2] = \mathbb{E}[x_j^2]$), ta cần hệ số nhân bằng đúng 1:
   $$
   \frac{1}{2} n_{\text{in}} \operatorname{Var}(W) = 1 \implies \operatorname{Var}(W) = \frac{2}{n_{\text{in}}}.
   $$
   Đây chính là công thức khởi tạo He (Kaiming Initialization) nổi tiếng.

3. **Hậu quả khi dùng nhầm khởi tạo Glorot cho ReLU**:
   Khởi tạo Glorot được thiết kế cho các hàm kích hoạt tuyến tính hoặc sigmoid/tanh đối xứng quanh gốc tọa độ, với giả định tín hiệu không bị mất năng lượng qua hàm kích hoạt ($\mathbb{E}[z^2] \approx \mathbb{E}[y^2]$), dẫn tới hệ số $\operatorname{Var}(W) \approx \frac{1}{n_{\text{in}}}$.
   Nếu áp dụng công thức này cho mạng ReLU:
   $$
   \mathbb{E}[z^2] = \frac{1}{2} n_{\text{in}} \left(\frac{1}{n_{\text{in}}}\right) \mathbb{E}[x^2] = \frac{1}{2}\mathbb{E}[x^2].
   $$
   Qua mỗi tầng mạng, phương sai của tín hiệu bị giảm đi một nửa. Qua $L = 50$ tầng tích chập hoặc tầng ẩn, năng lượng tín hiệu bị suy giảm theo tỉ lệ:
   $$
   \left(\frac{1}{2}\right)^{50} \approx 8{,}88 \times 10^{-16}.
   $$
   Tín hiệu lan truyền xuôi và gradient lan truyền ngược bị triệt tiêu hoàn toàn về 0, khiến mạng sâu không thể học được bất cứ điều gì.
:::

::: exercise 8. Bất đẳng thức tập trung Chebyshev và Hoeffding trong kiểm soát sai số mini-batch
Khi huấn luyện mô hình phân loại trên tập dữ liệu kích thước lớn, ta dùng gradient lô nhỏ $g_m = \frac{1}{m}\sum_{i=1}^m X_i$ để xấp xỉ gradient toàn thể $\mu = \mathbb{E}[X_i]$. Giả sử mỗi thành phần của gradient đơn lẻ bị chặn trong đoạn $[-1, 1]$, và phương sai thành phần là $\sigma^2 = 0{,}25$.
1. Áp dụng Bất đẳng thức Chebyshev: Cần kích thước lô $m$ tối thiểu là bao nhiêu để xác suất sai số $|g_m - \mu| \ge 0{,}1$ không vượt quá $5\%$ ($\delta = 0{,}05$)?
2. Áp dụng Bất đẳng thức Hoeffding: Với cùng sai số $\epsilon = 0{,}1$ và độ tin cậy $95\%$ ($\delta = 0{,}05$), hãy tính kích thước lô $m$ theo cận hàm mũ.
3. So sánh hai kết quả và giải thích tại sao bất đẳng thức Hoeffding mang lại cận kích thước mẫu vượt trội hơn khi yêu cầu độ tin cậy cực cao ($\delta \to 0$).
:::

::: solution
1. **Áp dụng Bất đẳng thức Chebyshev**:
   Kỳ vọng của trung bình mẫu là $\mathbb{E}[g_m] = \mu$, và phương sai là $\operatorname{Var}(g_m) = \frac{\sigma^2}{m} = \frac{0{,}25}{m}$.
   Bất đẳng thức Chebyshev phát biểu rằng với mọi $\epsilon > 0$:
   $$
   \mathbb{P}(|g_m - \mu| \ge \epsilon) \le \frac{\operatorname{Var}(g_m)}{\epsilon^2} = \frac{\sigma^2}{m \epsilon^2}.
   $$
   Yêu cầu xác suất vi phạm không vượt quá $\delta = 0{,}05$:
   $$
   \frac{0{,}25}{m (0{,}1)^2} \le 0{,}05 \iff \frac{0{,}25}{0{,}01 m} \le 0{,}05 \iff \frac{25}{m} \le 0{,}05 \implies m \ge \frac{25}{0{,}05} = 500.
   $$
   Theo Chebyshev, cần kích thước lô ít nhất $m = 500$ mẫu.

2. **Áp dụng Bất đẳng thức Hoeffding**:
   Vì mỗi biến ngẫu nhiên $X_i$ bị chặn trong đoạn $[a_i, b_i] = [-1, 1]$, độ dài khoảng chặn là $b_i - a_i = 1 - (-1) = 2$.
   Bất đẳng thức Hoeffding cho biến ngẫu nhiên độc lập bị chặn:
   $$
   \mathbb{P}(|g_m - \mu| \ge \epsilon) \le 2 \exp\left(-\frac{2 m^2 \epsilon^2}{\sum_{i=1}^m (b_i - a_i)^2}\right) = 2 \exp\left(-\frac{2 m^2 \epsilon^2}{m \times 2^2}\right) = 2 \exp\left(-\frac{m \epsilon^2}{2}\right).
   $$
   Yêu cầu cận trên không vượt quá $\delta = 0{,}05$:
   $$
   2 \exp\left(-\frac{m (0{,}1)^2}{2}\right) \le 0{,}05 \iff \exp(-0{,}005 m) \le 0{,}025.
   $$
   Lấy logarit tự nhiên hai vế:
   $$
   -0{,}005 m \le \log(0{,}025) \approx -3{,}6889 \implies m \ge \frac{3{,}6889}{0{,}005} \approx 737{,}8.
   $$
   Làm tròn lên, ta cần $m \ge 738$ mẫu.

3. **So sánh bản chất của hai bất đẳng thức**:
   - Khi độ tin cậy ở mức thông thường ($\delta = 0{,}05$), Chebyshev có thể cho cận số học nhỏ hơn nếu phương sai thực tế $\sigma^2 = 0{,}25$ nhỏ hơn nhiều so với độ rộng khoảng chặn ($[-1, 1]$ có biên độ tối đa cho phép phương sai lên tới $1$).
   - Tuy nhiên, sự khác biệt then chốt nằm ở tốc độ suy giảm theo xác suất lỗi $\delta$:
     - Cận kích thước mẫu của Chebyshev tỷ lệ với $\frac{1}{\delta}$ (suy giảm dạng đa thức chậm). Nếu đòi hỏi $\delta = 10^{-6}$, Chebyshev đòi hỏi $m \ge \frac{25}{10^{-6}} = 25.000.000$ mẫu.
     - Cận kích thước mẫu của Hoeffding tỷ lệ với $\log(1/\delta)$ (suy giảm dạng hàm mũ). Với $\delta = 10^{-6}$, Hoeffding chỉ đòi hỏi $m \ge \frac{2 \log(2 \times 10^6)}{0{,}01} \approx \frac{2 \times 14{,}5}{0{,}01} = 2900$ mẫu.
   
   Bất đẳng thức Hoeffding khai thác triệt để phân phối đuôi mỏng hàm mũ (sub-Gaussian tails), tạo nền tảng vững chắc cho lý thuyết học thống kê (PAC learning) và cận khái quát hóa trong trí tuệ nhân tạo.
:::


---

## Tóm tắt cốt lõi

1. **Tối ưu hóa vs Khái quát hóa**: Cực tiểu hóa mất mát thực nghiệm trên tập huấn luyện là phương tiện; mục tiêu tối thượng của học máy là khả năng khái quát hóa trên dữ liệu thực tế chưa biết.
2. **Bản chất của Mini-batch SGD**: Gradient lô nhỏ là ước lượng không chệch với phương sai tỉ lệ nghịch với kích thước lô ($1/B$). Nhiễu ngẫu nhiên vừa là thách thức vừa là công cụ điều chuẩn hữu hiệu.
3. **Momentum và Nesterov**: Tích lũy quán tính giúp triệt tiêu dao động ziczac trong hẻm núi hẹp; Nesterov cải tiến vượt bậc bằng cách lấy gradient tại vị trí nhìn trước để chủ động hãm đà khi tới gần đáy.
4. **Khởi tạo Glorot**: Bảo toàn phương sai của dòng chảy tín hiệu lan truyền xuôi và gradient lan truyền ngược, ngăn chặn triệt để thảm họa bùng nổ hay triệt tiêu gradient.

---

## Tài liệu tham khảo và Đọc thêm

Dành cho người học muốn nghiên cứu chuyên sâu về tối ưu hóa trong học sâu:
- **Ian Goodfellow, Yoshua Bengio & Aaron Courville**, *Deep Learning*, MIT Press. Đọc kỹ Chương 8 (Tối ưu hóa trong huấn luyện mô hình học sâu: Các thách thức giải tích, thuật toán cơ bản, thuật toán với momentum, và chiến lược khởi tạo).
- **Xavier Glorot & Yoshua Bengio** (2010), *Understanding the difficulty of training deep feedforward neural networks*, AISTATS. Công trình nền tảng khai sinh phương pháp khởi tạo chuẩn hóa (Glorot / Xavier initialization).

Tiếp theo: [Bài 06: Các phương pháp tối ưu thích nghi: AdaGrad, RMSProp và Adam](./bai-06-phuong-phap-thich-nghi.md).
