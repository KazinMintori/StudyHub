---
course: toan-cho-ai
lecture: bai-02-tap-loi
topic: can-chebyshev-va-chernoff
section: topic
title: "Cận xác suất Chebyshev, Chernoff và tối ưu hóa ma trận"
description: "Thiết lập các cận xác suất đuôi tồi tệ nhất khi chỉ biết kỳ vọng và hiệp phương sai, chuyển bài toán Chebyshev nhiều chiều thành quy hoạch nửa xác định SDP, cận Chernoff qua hàm liên hợp lồi và ứng dụng quản lý rủi ro."
---

Trong các hệ thống học máy an toàn, tài chính định lượng và mạng viễn thông, việc ước tính xác suất xảy ra biến cố cực đoan (chẳng hạn như xác suất lỗi hệ thống vượt ngưỡng hay tổn thất danh mục đầu tư chạm đáy rủi ro) là bài toán sinh tử. Tuy nhiên, trong thực tế ta hiếm khi nắm được toàn bộ hàm phân phối xác suất mà thường chỉ ước lượng được các đặc trưng số cơ bản: Vector kỳ vọng $\mu = \mathbb{E}[X]$ và ma trận hiệp phương sai $\Sigma = \operatorname{Cov}(X)$.

Câu hỏi đặt ra là: Trong số mọi phân phối xác suất khả dĩ có cùng kỳ vọng $\mu$ và hiệp phương sai $\Sigma$, xác suất lớn nhất để $X$ rơi vào vùng nguy hiểm là bao nhiêu? Tối ưu hóa lồi cung cấp một lời giải hoàn chỉnh thông qua sự kết hợp giữa lý thuyết đối ngẫu và Quy hoạch nửa xác định (SDP).

## 1. Bản chất tối ưu hóa của các cận xác suất cổ điển

Xét biến ngẫu nhiên thực $X$. Bất đẳng thức Markov khẳng định rằng với mọi biến ngẫu nhiên không âm $X \ge 0$ và hằng số $a > 0$:

$$
\mathbb{P}(X \ge a) \le \frac{\mathbb{E}[X]}{a}.
$$

Bản chất của bất đẳng thức này là một bài toán tìm chặn trên của hàm chỉ thị: Hàm bậc thang $\mathbf{1}_{\{x \ge a\}}$ được chặn trên bởi hàm tuyến tính $f(x) = \frac{x}{a}$ với mọi $x \ge 0$. Do tính chất đơn điệu của kỳ vọng:

$$
\mathbb{P}(X \ge a) = \mathbb{E}\big[\mathbf{1}_{\{x \ge a\}}\big] \le \mathbb{E}[f(X)] = \frac{\mathbb{E}[X]}{a}.
$$

Tương tự, bất đẳng thức Chebyshev cổ điển áp dụng hàm toàn phương để chặn trên hàm chỉ thị:

$$
\mathbf{1}_{\{|x - \mu| \ge k \sigma\}} \le \frac{(x - \mu)^2}{k^2 \sigma^2} \implies \mathbb{P}(|X - \mu| \ge k \sigma) \le \frac{1}{k^2}.
$$

Dưới lăng kính tối ưu hóa, việc tìm cận xác suất chặt nhất cho một biến cố $X \in \mathcal{C}$ chính là bài toán tìm một hàm chặn trên $f(x) \ge \mathbf{1}_{\mathcal{C}}(x)$ sao cho kỳ vọng $\mathbb{E}[f(X)]$ đạt giá trị nhỏ nhất có thể.

## 2. Cận Chebyshev nhiều chiều và Quy hoạch nửa xác định (SDP)

Xét vector ngẫu nhiên $X \in \mathbb{R}^n$ có kỳ vọng $\mathbb{E}[X] = \mu$ và ma trận hiệp phương sai $\operatorname{Cov}(X) = \Sigma \succ 0$. Đặt ma trận mô-men bậc hai:

$$
M = \mathbb{E}[X X^T] = \Sigma + \mu \mu^T.
$$

Ta muốn tìm chặn trên chặt nhất cho xác suất $X$ rơi ra ngoài một tập lồi an toàn $\mathcal{S}$ (chẳng hạn một tập ellipsoid hoặc đa diện):

$$
p_{\max} = \sup_{X \sim (\mu, \Sigma)} \mathbb{P}(X \notin \mathcal{S}).
$$

Để chặn trên hàm chỉ thị $\mathbf{1}_{\{x \notin \mathcal{S}\}}$, ta xét họ hàm toàn phương tổng quát:

$$
f(x) = x^T P x + 2 q^T x + r, \qquad P \in \mathbb{S}^n, \; q \in \mathbb{R}^n, \; r \in \mathbb{R}.
$$

Hàm $f(x)$ là một cận trên hợp lệ của hàm chỉ thị khi và chỉ khi:
1. $f(x) \ge 1$ với mọi $x \notin \mathcal{S}$.
2. $f(x) \ge 0$ với mọi $x \in \mathcal{S}$ (và do đó $f(x) \ge 0$ với mọi $x \in \mathbb{R}^n$).

Khi điều kiện $f(x) \ge 0, \forall x$ được thỏa mãn, ma trận $P$ bắt buộc phải là nửa xác định dương: $P \succeq 0$. Kỳ vọng của hàm toàn phương $f(X)$ được tính tường minh qua các mô-men đã biết:

$$
\begin{aligned}
\mathbb{E}[f(X)] &= \mathbb{E}\big[\operatorname{tr}(P X X^T) + 2 q^T X + r\big] \\
&= \operatorname{tr}(P M) + 2 q^T \mu + r \\
&= \operatorname{tr}(P \Sigma) + \mu^T P \mu + 2 q^T \mu + r.
\end{aligned}
$$

Bài toán tìm cận Chebyshev nhiều chiều chặt nhất quy về việc cực tiểu hóa biểu thức tuyến tính này theo các biến quyết định $(P, q, r)$:

$$
\begin{aligned}
\text{minimize}\quad & \operatorname{tr}(P \Sigma) + \mu^T P \mu + 2 q^T \mu + r \\
\text{subject to}\quad & P \succeq 0, \\
& x^T P x + 2 q^T x + r \ge 1, \quad \forall x \notin \mathcal{S}.
\end{aligned}
$$

Khi tập an toàn $\mathcal{S}$ là một hình cầu hoặc ellipsoid $\mathcal{S} = \{x \mid (x - x_0)^T A (x - x_0) \le 1\}$, ràng buộc $f(x) \ge 1$ ngoài $\mathcal{S}$ có thể chuyển hóa thành một Bất đẳng thức Ma trận Tuyến tính (LMI) nhờ Bổ đề S-procedure: Tồn tại $\lambda \ge 0$ sao cho:

$$
\begin{bmatrix} P & q \\ q^T & r - 1 \end{bmatrix} - \lambda \begin{bmatrix} A & -A x_0 \\ -x_0^T A & x_0^T A x_0 - 1 \end{bmatrix} \succeq 0.
$$

Đây chính là một bài toán Quy hoạch nửa xác định (SDP) chuẩn tắc, giải được với độ chính xác tùy ý trong thời gian đa thức.

## 3. Cận Chernoff và Hàm liên hợp lồi (Convex Conjugate)

Khi ta có thêm thông tin về hàm sinh mô-men (Moment Generating Function) $M_X(\lambda) = \mathbb{E}[e^{\lambda X}]$, cận Chernoff cung cấp một cận trên suy giảm theo hàm mũ, chặt hơn rất nhiều so với cận đa thức của Chebyshev.

Với tham số $\lambda > 0$, áp dụng bất đẳng thức Markov cho biến ngẫu nhiên dương $e^{\lambda X}$:

$$
\mathbb{P}(X \ge t) = \mathbb{P}(e^{\lambda X} \ge e^{\lambda t}) \le \frac{\mathbb{E}[e^{\lambda X}]}{e^{\lambda t}} = \exp\big(- (\lambda t - \log \mathbb{E}[e^{\lambda X}])\big).
$$

Đặt $\psi(\lambda) = \log \mathbb{E}[e^{\lambda X}]$ là hàm sinh mô-men logarit (Cumulant Generating Function). Bất đẳng thức trên đúng với mọi $\lambda > 0$, do đó ta có thể tối ưu hóa tham số $\lambda$ để thu được cận chặt nhất:

$$
\mathbb{P}(X \ge t) \le \exp\left( - \sup_{\lambda > 0} (\lambda t - \psi(\lambda)) \right).
$$

Biểu thức $\sup_{\lambda} (\lambda t - \psi(\lambda))$ chính là **biến đổi Legendre–Fenchel (hàm liên hợp lồi $\psi^*(t)$)** của hàm $\psi(\lambda)$. Vì hàm $\psi(\lambda)$ luôn lồi theo $\lambda$ (chứng minh thông qua bất đẳng thức Cauchy–Schwarz hoặc Jensen), bài toán tìm cận Chernoff chặt nhất là bài toán tối ưu lồi một chiều khả giải hoàn toàn.

### Ví dụ: Phân phối chuẩn chuẩn hóa $X \sim \mathcal{N}(0, 1)$
Hàm sinh mô-men logarit là:

$$
\psi(\lambda) = \log \mathbb{E}[e^{\lambda X}] = \frac{\lambda^2}{2}.
$$

Hàm liên hợp lồi:

$$
\psi^*(t) = \sup_{\lambda > 0} \left(\lambda t - \frac{\lambda^2}{2}\right) = \frac{t^2}{2} \quad (\text{đạt tại } \lambda^* = t).
$$

Từ đó thu được cận đuôi Chernoff chuẩn mực cho phân phối Gauss:

$$
\mathbb{P}(X \ge t) \le e^{-t^2 / 2}, \qquad \forall t > 0.
$$

## 4. Bài tập tự luyện

::: exercise 1. Cận Chernoff tối ưu cho biến ngẫu nhiên Poisson
Cho biến ngẫu nhiên $X$ tuân theo phân phối Poisson với tham số $\mu > 0$: Hàm xác suất $\mathbb{P}(X = k) = \frac{\mu^k e^{-\mu}}{k!}$ với $k = 0, 1, 2, \dots$.
1. Tính hàm sinh mô-men logarit $\psi(\lambda) = \log \mathbb{E}[e^{\lambda X}]$.
2. Tìm hàm liên hợp lồi $\psi^*(t)$ với $t > \mu$.
3. Thiết lập cận Chernoff cho xác suất đuôi $\mathbb{P}(X \ge t)$ và so sánh với cận Chebyshev khi $t$ lớn.
:::

::: solution
1. **Tính hàm sinh mô-men logarit**:
   Hàm sinh mô-men:
   $$
   M_X(\lambda) = \mathbb{E}[e^{\lambda X}] = \sum_{k=0}^\infty e^{\lambda k} \frac{\mu^k e^{-\mu}}{k!} = e^{-\mu} \sum_{k=0}^\infty \frac{(\mu e^\lambda)^k}{k!} = e^{-\mu} e^{\mu e^\lambda} = \exp\big(\mu(e^\lambda - 1)\big).
   $$
   Hàm sinh mô-men logarit:
   $$
   \psi(\lambda) = \log M_X(\lambda) = \mu (e^\lambda - 1).
   $$

2. **Tìm hàm liên hợp lồi $\psi^*(t)$**:
   Với $t > \mu$:
   $$
   \psi^*(t) = \sup_{\lambda > 0} \big(\lambda t - \mu(e^\lambda - 1)\big).
   $$
   Lấy đạo hàm theo $\lambda$ và cho bằng 0:
   $$
   t - \mu e^\lambda = 0 \implies e^\lambda = \frac{t}{\mu} \implies \lambda^* = \log\left(\frac{t}{\mu}\right).
   $$
   Vì $t > \mu$, ta có $\lambda^* > 0$. Thay vào biểu thức liên hợp:
   $$
   \begin{aligned}
   \psi^*(t) &= t \log\left(\frac{t}{\mu}\right) - \mu\left(\frac{t}{\mu} - 1\right) \\
   &= t \log\left(\frac{t}{\mu}\right) - t + \mu.
   \end{aligned}
   $$

3. **Thiết lập cận Chernoff**:
   Xác suất đuôi bị chặn bởi:
   $$
   \mathbb{P}(X \ge t) \le \exp\big(-\psi^*(t)\big) = \exp\left( - \left[t \log\left(\frac{t}{\mu}\right) - t + \mu\right] \right) = \frac{e^{-\mu} (e \mu)^t}{t^t}.
   $$
   So sánh: Cận Chebyshev chỉ suy giảm theo bậc hai $\frac{\operatorname{Var}(X)}{(t - \mu)^2} = \frac{\mu}{(t - \mu)^2} = O(t^{-2})$, trong khi cận Chernoff suy giảm theo tốc độ giai thừa / hàm mũ siêu tốc $O((e\mu/t)^t)$, cho độ chính xác vượt trội khi đánh giá các sự kiện hiếm.
:::

::: exercise 2. Bất đẳng thức Cantelli (Chebyshev một phía)
Cho biến ngẫu nhiên $X$ có $\mathbb{E}[X] = 0$ và $\operatorname{Var}(X) = \sigma^2$. Với $a > 0$, ta muốn tìm chặn trên cho xác suất một phía $\mathbb{P}(X \ge a)$.
1. Xét hàm toàn phương $f(x) = \frac{(x + u)^2}{(a + u)^2}$ với tham số $u > 0$. Chứng minh rằng $f(x) \ge 1$ với mọi $x \ge a$ và $f(x) \ge 0$ với mọi $x \in \mathbb{R}$.
2. Tính kỳ vọng $\mathbb{E}[f(X)]$ theo $u, a, \sigma$.
3. Cực tiểu hóa $\mathbb{E}[f(X)]$ theo biến $u > 0$ để suy ra bất đẳng thức Cantelli: $\mathbb{P}(X \ge a) \le \frac{\sigma^2}{\sigma^2 + a^2}$.
:::

::: solution
1. **Kiểm tra tính chất hàm chặn trên**:
   - Khi $x \ge a$: Vì $u > 0$, ta có $x + u \ge a + u > 0$. Suy ra $(x + u)^2 \ge (a + u)^2$, do đó $f(x) \ge 1$.
   - Với mọi $x \in \mathbb{R}$: Là bình phương chia bình phương, $f(x) \ge 0$.
   Như vậy $f(x) \ge \mathbf{1}_{\{x \ge a\}}$ trên toàn trục thực.

2. **Tính kỳ vọng**:
   $$
   \mathbb{E}[f(X)] = \frac{\mathbb{E}[(X + u)^2]}{(a + u)^2} = \frac{\mathbb{E}[X^2] + 2u\mathbb{E}[X] + u^2}{(a + u)^2}.
   $$
   Vì $\mathbb{E}[X] = 0$ và $\mathbb{E}[X^2] = \sigma^2$:
   $$
   g(u) = \mathbb{E}[f(X)] = \frac{\sigma^2 + u^2}{(a + u)^2}.
   $$

3. **Cực tiểu hóa theo $u$**:
   Lấy đạo hàm của $g(u)$ theo $u$:
   $$
   g'(u) = \frac{2u(a + u)^2 - (\sigma^2 + u^2) \cdot 2(a + u)}{(a + u)^4} = \frac{2\big[u(a + u) - (\sigma^2 + u^2)\big]}{(a + u)^3} = \frac{2(a u - \sigma^2)}{(a + u)^3}.
   $$
   Đặt $g'(u) = 0$:
   $$
   a u - \sigma^2 = 0 \implies u^* = \frac{\sigma^2}{a} > 0.
   $$
   Thay $u^*$ vào biểu thức $g(u)$:
   $$
   a + u^* = a + \frac{\sigma^2}{a} = \frac{a^2 + \sigma^2}{a},
   $$
   $$
   \sigma^2 + (u^*)^2 = \sigma^2 + \frac{\sigma^4}{a^2} = \sigma^2 \left(1 + \frac{\sigma^2}{a^2}\right) = \frac{\sigma^2(a^2 + \sigma^2)}{a^2}.
   $$
   Do đó:
   $$
   g(u^*) = \frac{\frac{\sigma^2(a^2 + \sigma^2)}{a^2}}{\frac{(a^2 + \sigma^2)^2}{a^2}} = \frac{\sigma^2}{a^2 + \sigma^2} = \frac{\sigma^2}{\sigma^2 + a^2}.
   $$
   Đây chính là bất đẳng thức Cantelli kinh điển. So với Chebyshev hai phía $\frac{\sigma^2}{a^2}$, cận một phía Cantelli luôn chặt hơn vì mẫu số có thêm đại lượng $\sigma^2$.
:::

::: exercise 3. Đánh giá rủi ro danh mục đầu tư qua cận Chebyshev nhiều chiều
Xét vector tỉ suất sinh lời của hai tài sản $R = (R_1, R_2)^T$ có vector kỳ vọng $\mu = (0{,}1, \; 0{,}15)^T$ và ma trận hiệp phương sai $\Sigma = \begin{bmatrix} 0{,}04 & 0{,}01 \\ 0{,}01 & 0{,}09 \end{bmatrix}$. Một nhà đầu tư phân bổ danh mục theo tỷ trọng $w = (0{,}6, \; 0{,}4)^T$.
1. Tính kỳ vọng $\mu_p = w^T \mu$ và phương sai $\sigma_p^2 = w^T \Sigma w$ của tỷ suất sinh lời danh mục.
2. Dùng bất đẳng thức Cantelli để tìm chặn trên cho xác suất danh mục bị thua lỗ (tức $R_p \le 0$).
3. Nêu cách phát biểu bài toán phân bổ danh mục tối ưu $w$ để cực tiểu hóa cận xác suất thua lỗ này.
:::

::: solution
1. **Tính kỳ vọng và phương sai của danh mục**:
   - Kỳ vọng danh mục:
     $$
     \mu_p = w^T \mu = 0{,}6(0{,}1) + 0{,}4(0{,}15) = 0{,}06 + 0{,}06 = 0{,}12 \; (12\%).
     $$
   - Tích $w^T \Sigma$:
     $$
     w^T \Sigma = \begin{bmatrix} 0{,}6 & 0{,}4 \end{bmatrix} \begin{bmatrix} 0{,}04 & 0{,}01 \\ 0{,}01 & 0{,}09 \end{bmatrix} = \begin{bmatrix} 0{,}024 + 0{,}004 & 0{,}006 + 0{,}036 \end{bmatrix} = \begin{bmatrix} 0{,}028 & 0{,}042 \end{bmatrix}.
     $$
   - Phương sai danh mục:
     $$
     \sigma_p^2 = (w^T \Sigma) w = 0{,}028(0{,}6) + 0{,}042(0{,}4) = 0{,}0168 + 0{,}0168 = 0{,}0336.
     $$
     Độ lệch chuẩn: $\sigma_p = \sqrt{0{,}0336} \approx 0{,}1833 \; (18{,}33\%)$.

2. **Chặn trên xác suất thua lỗ**:
   Biến cố thua lỗ: $R_p \le 0 \iff -R_p \ge 0$.
   Biến ngẫu nhiên $Y = -R_p$ có kỳ vọng $\mathbb{E}[Y] = -\mu_p = -0{,}12$ và phương sai $\operatorname{Var}(Y) = \sigma_p^2 = 0{,}0336$.
   Khoảng cách lệch khỏi kỳ vọng:
   $$
   a = 0 - \mathbb{E}[Y] = 0 - (-0{,}12) = 0{,}12.
   $$
   Áp dụng bất đẳng thức Cantelli cho $Y$:
   $$
   \mathbb{P}(R_p \le 0) = \mathbb{P}(Y \ge 0) \le \frac{\sigma_p^2}{\sigma_p^2 + a^2} = \frac{0{,}0336}{0{,}0336 + (0{,}12)^2} = \frac{0{,}0336}{0{,}0336 + 0{,}0144} = \frac{0{,}0336}{0{,}0480} = 0{,}70 \; (70\%).
   $$

3. **Bài toán phân bổ danh mục tối ưu**:
   Để cực tiểu hóa cận xác suất thua lỗ $\frac{w^T \Sigma w}{w^T \Sigma w + (w^T \mu)^2}$, ta chú ý rằng biểu thức này là một hàm đơn điệu tăng theo đại lượng:
   $$
   \frac{w^T \Sigma w}{(w^T \mu)^2} = \left(\frac{\sqrt{w^T \Sigma w}}{w^T \mu}\right)^2 = \frac{1}{\text{Sharpe Ratio}^2}.
   $$
   Do đó, cực tiểu hóa cận xác suất thua lỗ Cantelli tương đương cực đại hóa chỉ số Sharpe $\frac{w^T \mu}{\| \Sigma^{1/2} w \|_2}$. Với chuẩn hóa $w^T \mu = 1$, bài toán quy về bài toán QP lồi tiêu chuẩn:
   $$
   \begin{aligned}
   \text{minimize}\quad & w^T \Sigma w \\
   \text{subject to}\quad & w^T \mu = 1, \\
   & \mathbf{1}^T w = c > 0, \quad w \succeq 0.
   \end{aligned}
   $$
   Đây là bài toán danh mục Markowitz cổ điển, kết nối trực tiếp lý thuyết cận xác suất với tối ưu hóa lồi thực hành.
:::

## Tóm tắt

Cận xác suất là công cụ toán học nền tảng giúp đưa ra các bảo đảm định lượng khi phân phối dữ liệu không được biết trọn vẹn. Bằng cách định dạng bài toán tìm cận xác suất như một bài toán đối ngẫu cực tiểu hóa kỳ vọng của hàm bao trên toàn phương, cận Chebyshev nhiều chiều được giải quyết tối ưu thông qua Quy hoạch nửa xác định (SDP). 

Bên cạnh đó, cận Chernoff khai thác thông tin hàm sinh mô-men logarit, chuyển hóa việc tìm cận đuôi hàm mũ thành phép biến đổi liên hợp lồi Legendre–Fenchel. Cả hai công cụ này đều đóng vai trò nòng cốt trong quản lý rủi ro hiện đại, từ tính toán giá trị rủi ro VaR trong kinh tế đến đánh giá độ tin cậy của các mô hình học máy an toàn.

## Tài liệu tham khảo

- Stephen Boyd, Lieven Vandenberghe, *Convex Optimization*, Cambridge University Press, Chapter 7: Statistical Estimation (§7.4).
