---
course: toan-cho-ai
lecture: bai-03-doi-ngau-lagrange
section: lecture
title: "Đối ngẫu Lagrange"
prerequisites: ["ham-loi", "gradient", "he-phuong-trinh"]
lessonStatus: ready
description: "Tự tính Lagrangian, hàm đối ngẫu và khoảng cách đối ngẫu; dùng Slater và KKT để chứng nhận nghiệm."
---

Khi tìm kiếm lời giải cho một bài toán tối ưu có ràng buộc, làm thế nào để chúng ta biết chắc chắn rằng mình không thể tìm được một phương án nào tốt hơn nữa? Việc tìm ra một điểm khả thi có chi phí thấp mới chỉ là một nửa câu chuyện; nửa còn lại đòi hỏi một **chứng nhận cận dưới không thể đánh bại**. Nếu ta chứng minh được rằng chi phí thực tế không bao giờ có thể thấp hơn một ngưỡng $d^*$, và đồng thời ta tìm được một phương án đạt đúng ngưỡng $d^*$ đó, thì điểm khả thi ấy chắc chắn là nghiệm tối ưu toàn cục.

Lý thuyết **Đối ngẫu Lagrange (Lagrangian Duality)** chính là cỗ máy toán học tạo ra những chứng nhận cận dưới như vậy. Bằng cách biến các ràng buộc cứng thành các khoản "chi phí phạt mềm" tích hợp vào hàm mục tiêu, đối ngẫu Lagrange mở ra một bài toán song hành phản chiếu bài toán gốc. Không chỉ cung cấp công cụ chứng minh nghiệm, lý thuyết này còn mang ý nghĩa kinh tế học sâu sắc về "giá bóng" (shadow price) của tài nguyên và khai sinh ra hệ điều kiện Karush–Kuhn–Tucker (KKT) — đỉnh cao của giải tích tối ưu có ràng buộc.

---

## 1. Hàm Lagrangian và Bản chất dấu của các nhân tử

Xét bài toán tối ưu chuẩn tắc với biến $x \in \mathbb{R}^n$, gồm $m$ ràng buộc bất đẳng thức và $p$ ràng buộc đẳng thức:

$$
\begin{aligned}
\min_{x} \quad & f_0(x) \\
\text{sao cho} \quad & f_i(x) \le 0, \quad i = 1, \ldots, m, \\
& h_j(x) = 0, \quad j = 1, \ldots, p.
\end{aligned}
$$

Ý tưởng cốt lõi của Joseph-Louis Lagrange là nới lỏng các ràng buộc bằng cách đưa chúng trực tiếp vào hàm mục tiêu thông qua phép tổ hợp tuyến tính. Hàm **Lagrangian** $L: \mathbb{R}^n \times \mathbb{R}^m \times \mathbb{R}^p \to \mathbb{R}$ được định nghĩa là:

$$
L(x, \lambda, \nu) = f_0(x) + \sum_{i=1}^m \lambda_i f_i(x) + \sum_{j=1}^p \nu_j h_j(x),
$$

trong đó:
- $\lambda = (\lambda_1, \ldots, \lambda_m)^T \in \mathbb{R}^m$ là vector **nhân tử Lagrange** gắn với các bất đẳng thức.
- $\nu = (\nu_1, \ldots, \nu_p)^T \in \mathbb{R}^p$ là vector **nhân tử Lagrange** gắn với các đẳng thức.

Tại sao ta bắt buộc phải áp đặt điều kiện không âm $\lambda_i \ge 0$ cho các bất đẳng thức? 

Hãy quan sát: Với một điểm khả thi bất kỳ $\widetilde x$ của bài toán gốc, ta luôn có $f_i(\widetilde x) \le 0$. Nếu chọn $\lambda_i \ge 0$, tích $\lambda_i f_i(\widetilde x)$ luôn không dương. Mặt khác, vì $h_j(\widetilde x) = 0$, số hạng $\nu_j h_j(\widetilde x)$ triệt tiêu hoàn toàn bất kể dấu của $\nu_j$. Do đó, với mọi điểm khả thi $\widetilde x$ và với mọi bộ nhân tử thỏa mãn $\lambda \succeq 0$, ta có bất đẳng thức:

$$
L(\widetilde x, \lambda, \nu) = f_0(\widetilde x) + \sum_{i=1}^m \underbrace{\lambda_i f_i(\widetilde x)}_{\le 0} + \sum_{j=1}^p \underbrace{\nu_j h_j(\widetilde x)}_{= 0} \le f_0(\widetilde x).
$$

Nói cách khác, trên miền khả thi gốc, hàm Lagrangian luôn đánh giá thấp hơn hoặc bằng chi phí thực tế. 

Từ bất đẳng thức này, ta định nghĩa **hàm đối ngẫu Lagrange** (Lagrange dual function) $g(\lambda, \nu)$ bằng cách lấy cận dưới đúng (infimum) của Lagrangian theo toàn bộ không gian biến $x \in \mathcal{D}$:

$$
g(\lambda, \nu) = \inf_{x \in \mathcal{D}} L(x, \lambda, \nu) = \inf_{x \in \mathcal{D}} \left( f_0(x) + \sum_{i=1}^m \lambda_i f_i(x) + \sum_{j=1}^p \nu_j h_j(x) \right).
$$

Lưu ý rằng phép lấy infimum này là bài toán không ràng buộc theo biến $x$ (chỉ giữ lại miền xác định ngầm $\mathcal{D}$). Vì giá trị nhỏ nhất của một hàm trên toàn không gian luôn nhỏ hơn hoặc bằng giá trị của nó tại một điểm khả thi cụ thể $\widetilde x$, ta thu được chuỗi bất đẳng thức nền tảng:

$$
\boxed{g(\lambda, \nu) \le L(\widetilde x, \lambda, \nu) \le f_0(\widetilde x).}
$$

Vì bất đẳng thức trên nghiệm đúng với **mọi** điểm khả thi $\widetilde x$, ta suy ra $g(\lambda, \nu)$ luôn nhỏ hơn hoặc bằng giá trị tối ưu toàn cục $p^*$ của bài toán gốc:

$$
g(\lambda, \nu) \le p^* \quad \forall \lambda \succeq 0, \, \forall \nu.
$$

Đặc tính này được gọi là **Định lý Đối ngẫu yếu (Weak Duality)**. Điều kỳ diệu là định lý đối ngẫu yếu luôn đúng cho **mọi bài toán tối ưu**, hoàn toàn không đòi hỏi hàm mục tiêu hay các miền ràng buộc phải có tính lồi.

---

## 2. Tính toán hàm đối ngẫu trên một bài toán cụ thể

Để thấy rõ cơ chế vận hành, ta xét bài toán tối ưu một chiều:

$$
\min_{x \in \mathbb{R}} \quad f_0(x) = (x - 2)^2 \quad \text{sao cho} \quad x \le 1.
$$

Viết lại ràng buộc dưới dạng chuẩn $f_1(x) = x - 1 \le 0$. Hàm Lagrangian với nhân tử $\lambda \ge 0$ là:

$$
L(x, \lambda) = (x - 2)^2 + \lambda(x - 1).
$$

Để tìm hàm đối ngẫu $g(\lambda)$, ta coi $\lambda$ là hằng số cố định và tìm cực tiểu của $L(x, \lambda)$ theo $x$ trên $\mathbb{R}$. Đạo hàm theo $x$:

$$
\frac{\partial L}{\partial x} = 2(x - 2) + \lambda = 0 \iff x(\lambda) = 2 - \frac{\lambda}{2}.
$$

Vì đạo hàm bậc hai $\frac{\partial^2 L}{\partial x^2} = 2 > 0$, hàm số đạt cực tiểu toàn cục duy nhất tại $x(\lambda) = 2 - \lambda/2$. Thay giá trị $x(\lambda)$ này ngược lại vào Lagrangian:

$$
\begin{aligned}
g(\lambda) &= \left(2 - \frac{\lambda}{2} - 2\right)^2 + \lambda\left(2 - \frac{\lambda}{2} - 1\right) \\
&= \frac{\lambda^2}{4} + \lambda\left(1 - \frac{\lambda}{2}\right) \\
&= \lambda - \frac{\lambda^2}{4}.
\end{aligned}
$$

Hàm đối ngẫu $g(\lambda) = \lambda - \frac{\lambda^2}{4}$ cung cấp một cận dưới cho giá trị tối ưu gốc với mỗi giá trị $\lambda \ge 0$:
- Thử với $\lambda = 0$: $g(0) = 0 \le p^*$. Điểm cực tiểu tương ứng là $x(0) = 2$ (không khả thi cho bài toán gốc).
- Thử với $\lambda = 1$: $g(1) = 1 - 0.25 = 0.75 \le p^*$.
- Thử với $\lambda = 4$: $g(4) = 4 - 4 = 0 \le p^*$.

Rõ ràng, mục tiêu của ta là tìm cận dưới chặt chẽ nhất, tức là giải **bài toán đối ngẫu Lagrange**:

$$
\max_{\lambda \ge 0} \quad g(\lambda) = \lambda - \frac{\lambda^2}{4}.
$$

Đạo hàm của hàm đối ngẫu là $g'(\lambda) = 1 - \frac{\lambda}{2} = 0 \iff \lambda^* = 2 \ge 0$. 

Giá trị tối ưu đối ngẫu đạt được là:
$$
d^* = g(\lambda^*) = 2 - \frac{2^2}{4} = 1.
$$

Quay trở lại bài toán gốc: Nghiệm khả thi rõ ràng là $x^* = 1$, cho giá trị mục tiêu $f_0(x^*) = (1 - 2)^2 = 1$. 

Như vậy, ta có $p^* = d^* = 1$. Cận dưới đối ngẫu đã chạm đúng giá trị tối ưu gốc, chứng nhận tuyệt đối rằng $x^* = 1$ là nghiệm tối ưu toàn cục.

---

## 3. Tính lõm tự nhiên của hàm đối ngẫu

Một trong những tính chất toán học đẹp đẽ nhất của lý thuyết đối ngẫu là: **Hàm đối ngẫu $g(\lambda, \nu)$ luôn là hàm lõm (concave), bất kể bài toán gốc có lồi hay không**.

Để chứng minh điều này, hãy nhìn vào dạng của Lagrangian: với mỗi điểm $x$ cố định, biểu thức
$$
(\lambda, \nu) \mapsto L(x, \lambda, \nu) = f_0(x) + \sum_{i=1}^m \lambda_i f_i(x) + \sum_{j=1}^p \nu_j h_j(x)
$$
là một hàm affine (tuyến tính cộng hằng số) theo biến $(\lambda, \nu)$. 

Hàm đối ngẫu $g(\lambda, \nu) = \inf_{x \in \mathcal{D}} L(x, \lambda, \nu)$ chính là infimum của một họ các hàm affine. Vì mỗi hàm affine vừa lồi vừa lõm, infimum của một họ các hàm affine luôn là một **hàm lõm**.

Ta kiểm chứng trực tiếp bằng định nghĩa tính lõm: Với hai bộ nhân tử bất kỳ $u = (\lambda_1, \nu_1)$, $v = (\lambda_2, \nu_2)$ và $\theta \in [0, 1]$:

$$
\begin{aligned}
g(\theta u + (1 - \theta) v) &= \inf_{x \in \mathcal{D}} L(x, \theta u + (1 - \theta) v) \\
&= \inf_{x \in \mathcal{D}} \left[ \theta L(x, u) + (1 - \theta) L(x, v) \right] \\
&\ge \theta \inf_{x \in \mathcal{D}} L(x, u) + (1 - \theta) \inf_{x \in \mathcal{D}} L(x, v) \\
&= \theta g(u) + (1 - \theta) g(v).
\end{aligned}
$$

Bất đẳng thức trên khẳng định $g$ là hàm lõm. Do đó:
> Bài toán đối ngẫu $\max_{\lambda \succeq 0, \nu} g(\lambda, \nu) \equiv \min_{\lambda \succeq 0, \nu} -g(\lambda, \nu)$ **luôn luôn là một bài toán tối ưu lồi**, ngay cả khi bài toán gốc là một bài toán phi lồi NP-hard vô cùng hiểm hóc!

<details><summary>Câu hỏi đào sâu: Tại sao bài toán đối ngẫu luôn tìm giá trị cực đại của g chứ không phải cực tiểu?</summary>

Bởi vì mỗi giá trị $g(\lambda, \nu)$ đóng vai trò là một cận dưới của giá trị tối ưu gốc $p^*$ ($g \le p^*$). Cận dưới càng lớn thì càng áp sát giá trị thực tế $p^*$, tức là thông tin chứng nhận càng chặt chẽ. Cực tiểu hóa một cận dưới sẽ đẩy nó về $-\infty$, hoàn toàn vô giá trị cho việc ước lượng nghiệm.

</details>

---

## 4. Điều kiện Slater và Đối ngẫu mạnh (Strong Duality)

Khoảng chênh lệch giữa giá trị tối ưu gốc và giá trị tối ưu đối ngẫu được gọi là **khoảng cách đối ngẫu (duality gap)**:

$$
\Delta = p^* - d^* \ge 0.
$$

Khi khoảng cách này triệt tiêu, tức $p^* = d^*$, ta nói bài toán thỏa mãn **Đối ngẫu mạnh (Strong Duality)**. 

Bài toán lồi có tự động bảo đảm đối ngẫu mạnh hay không? Câu trả lời là: Chưa chắc, cần thêm một điều kiện chính quy nhẹ nhàng về miền ràng buộc. Điều kiện phổ biến và quan trọng nhất là **Điều kiện Slater**:

> **Định lý Slater**: Xét bài toán tối ưu lồi dạng chuẩn (hàm mục tiêu $f_0$ và các ràng buộc bất đẳng thức $f_i$ đều lồi, ràng buộc đẳng thức là affine $Ax = b$). Nếu tồn tại một điểm $\bar x$ thuộc phần trong tương đối của miền xác định ($\bar x \in \operatorname{relint}\mathcal{D}$) thỏa mãn chặt các bất đẳng thức:
> $$
> f_i(\bar x) < 0 \quad \forall i = 1, \ldots, m, \qquad A\bar x = b,
> $$
> thì bài toán đạt đối ngẫu mạnh ($p^* = d^*$). Hơn nữa, nếu giá trị tối ưu $p^*$ hữu hạn, nghiệm đối ngẫu $(\lambda^*, \nu^*)$ chắc chắn tồn tại và đạt cận.

Một điểm $\bar x$ thỏa mãn $f_i(\bar x) < 0$ được gọi là một **điểm khả thi ngặt (strictly feasible point)**. Trong ví dụ một chiều ở mục 2, bài toán có $f_1(x) = x - 1 \le 0$. Điểm $\bar x = 0$ cho $f_1(0) = -1 < 0$, do đó điều kiện Slater được thỏa mãn lập tức, giải thích vì sao ta thu được $p^* = d^* = 1$.

Nếu tất cả các ràng buộc bất đẳng thức đều là hàm affine ($f_i(x) = c_i^T x - d_i$), điều kiện Slater được nới lỏng: ta chỉ cần bài toán khả thi ($f_i(x) \le 0$) mà không cần bất đẳng thức ngặt $< 0$. Đây là lý do vì sao trong Quy hoạch tuyến tính (LP), đối ngẫu mạnh luôn được bảo đảm khi bài toán có miền khả thi khác rỗng và bị chặn.

---

## 5. Bốn nhóm điều kiện Karush–Kuhn–Tucker (KKT)

Giả sử các hàm $f_0, f_1, \ldots, f_m$ và $h_1, \ldots, h_p$ đều khả vi. Hệ điều kiện **Karush–Kuhn–Tucker (KKT)** là tập hợp các phương trình và bất đẳng thức liên kết nghiệm gốc $x^*$ và nghiệm đối ngẫu $(\lambda^*, \nu^*)$:

| Nhóm điều kiện | Biểu thức toán học | Ý nghĩa hình học & Bản chất |
| :--- | :--- | :--- |
| **1. Khả thi gốc** (Primal Feasibility) | $f_i(x^*) \le 0, \; i=1,\ldots,m$<br>$h_j(x^*) = 0, \; j=1,\ldots,p$ | Điểm $x^*$ phải là một phương án hợp lệ, nằm trọn vẹn trong miền ràng buộc. |
| **2. Khả thi đối ngẫu** (Dual Feasibility) | $\lambda_i^* \ge 0, \; i=1,\ldots,m$ | Nhân tử không âm, bảo đảm hình phạt cho hành vi vi phạm luôn cùng chiều tăng chi phí. |
| **3. Bù trừ** (Complementary Slackness) | $\lambda_i^* f_i(x^*) = 0, \; i=1,\ldots,m$ | Hoặc ràng buộc không chặt ($f_i < 0 \implies \lambda_i^* = 0$), hoặc ràng buộc chặt ($f_i = 0$). |
| **4. Triệt tiêu gradient** (Stationarity) | $\nabla_x L(x^*, \lambda^*, \nu^*) = 0$ | Gradient hàm mục tiêu cân bằng với các lực cản pháp tuyến của mặt ràng buộc. |

### Ý nghĩa cốt tử của Điều kiện bù trừ (Complementary Slackness)
Đẳng thức $\lambda_i^* f_i(x^*) = 0$ là trái tim của tối ưu hóa có ràng buộc. Nó dẫn tới hai kịch bản loại trừ lẫn nhau:
- Nếu $f_i(x^*) < 0$ (ràng buộc không chặt, điểm tối ưu nằm an toàn bên trong miền): nhân tử bắt buộc phải bằng 0 ($\lambda_i^* = 0$). Nghĩa là ràng buộc này không hề cản trở mục tiêu tối ưu, nới lỏng nó thêm cũng không mang lại lợi ích gì.
- Nếu $\lambda_i^* > 0$ (nhân tử dương ngặt): ràng buộc bắt buộc phải chặt ($f_i(x^*) = 0$). Điểm tối ưu đang bị "ép sát" vào đường biên bởi ràng buộc này.

> Trong thuật toán máy vector hỗ trợ (Support Vector Machines - SVM) của AI, điều kiện bù trừ giải thích trọn vẹn vì sao mô hình chỉ phụ thuộc vào một số ít điểm dữ liệu nằm sát biên phân chia (các vector hỗ trợ - Support Vectors có $\lambda_i^* > 0$), trong khi hàng triệu điểm dữ liệu nằm sâu bên trong đều có $\lambda_i^* = 0$ và bị triệt tiêu hoàn toàn khỏi mô hình dự đoán!

### Vai trò của KKT trong Bài toán lồi vs Phi lồi
- **Với bài toán tối ưu lồi khả vi thỏa điều kiện Slater**: Hệ điều kiện KKT là **điều kiện cần và đủ** cho tối ưu toàn cục. Bất kỳ cặp điểm $(x^*, (\lambda^*, \nu^*))$ nào thỏa mãn bốn nhóm KKT đều được chứng nhận chắc chắn là nghiệm tối ưu toàn cục duy nhất.
- **Với bài toán phi lồi**: KKT chỉ là **điều kiện cần** cho điểm cực trị cục bộ. Một điểm thỏa mãn KKT có thể là cực tiểu cục bộ, cực đại cục bộ, hoặc một điểm yên ngựa.

::: example Kiểm chứng bốn điều kiện KKT trên bài toán một chiều
Với bài toán $\min (x-2)^2$ thỏa $x \le 1$, ta đã tìm được $x^* = 1$ và $\lambda^* = 2$:
1. Khả thi gốc: $f_1(x^*) = 1 - 1 = 0 \le 0$ (thỏa mãn).
2. Khả thi đối ngẫu: $\lambda^* = 2 \ge 0$ (thỏa mãn).
3. Bù trừ: $\lambda^* f_1(x^*) = 2 \cdot (1 - 1) = 0$ (thỏa mãn).
4. Triệt tiêu gradient: 
   $$\nabla L(x^*, \lambda^*) = 2(x^* - 2) + \lambda^* = 2(1 - 2) + 2 = 0 \quad (\text{thỏa mãn}).$$
Cả bốn điều kiện KKT đều được nghiệm đúng hoàn hảo.
:::

---

## 6. Bài toán hai chiều có ràng buộc đẳng thức

Xét bài toán tối ưu hình học hai chiều:

$$
\min_{x, y \in \mathbb{R}} \quad \frac{1}{2} \left[ (x - 2)^2 + y^2 \right] \quad \text{sao cho} \quad x + y = 1.
$$

Đây là bài toán tìm khoảng cách ngắn nhất từ điểm $(2, 0)$ tới đường thẳng $x + y = 1$.

Hàm Lagrangian với nhân tử tự do $\nu \in \mathbb{R}$:
$$
L(x, y, \nu) = \frac{1}{2} (x - 2)^2 + \frac{1}{2} y^2 + \nu (x + y - 1).
$$

Điều kiện dừng (triệt tiêu gradient theo $x$ và $y$):
$$
\begin{aligned}
\frac{\partial L}{\partial x} &= (x - 2) + \nu = 0 \implies x = 2 - \nu, \\
\frac{\partial L}{\partial y} &= y + \nu = 0 \implies y = -\nu.
\end{aligned}
$$

Thay $x$ và $y$ vào phương trình ràng buộc đẳng thức $x + y = 1$:
$$
(2 - \nu) + (-\nu) = 1 \iff 2 - 2\nu = 1 \iff \nu^* = \frac{1}{2}.
$$

Từ đó thu được tọa độ nghiệm tối ưu:
$$
x^* = 2 - \frac{1}{2} = \frac{3}{2}, \qquad y^* = -\frac{1}{2}.
$$

Giá trị hàm mục tiêu tối ưu:
$$
\begin{aligned}
p^* &= \frac{1}{2} \left[ \left(\frac{3}{2} - 2\right)^2 + \left(-\frac{1}{2}\right)^2 \right] \\
&= \frac{1}{2} \left( \frac{1}{4} + \frac{1}{4} \right) = \frac{1}{4} = 0.25.
\end{aligned}
$$

Hàm đối ngẫu Lagrange tính theo $\nu$:
$$
\begin{aligned}
g(\nu) &= \inf_{x, y} L(x, y, \nu) \\
&= \frac{1}{2}(-\nu)^2 + \frac{1}{2}(-\nu)^2 + \nu(2 - \nu - \nu - 1) \\
&= \nu^2 + \nu(1 - 2\nu) = \nu - \nu^2.
\end{aligned}
$$

Cực đại hóa hàm đối ngẫu: $g'(\nu) = 1 - 2\nu = 0 \iff \nu^* = \frac{1}{2}$, và giá trị tối ưu đối ngẫu là:
$$
d^* = g\left(\frac{1}{2}\right) = \frac{1}{2} - \frac{1}{4} = \frac{1}{4} = p^*.
$$

Đối ngẫu mạnh xảy ra chính xác. Trong dạng ma trận tổng quát của bài toán Quy hoạch toàn phương (QP) với ràng buộc đẳng thức, hệ phương trình KKT quy về hệ tuyến tính khối:

$$
\begin{bmatrix} P & A^T \\ A & 0 \end{bmatrix} \begin{bmatrix} x^* \\ \nu^* \end{bmatrix} = \begin{bmatrix} -q \\ b \end{bmatrix}.
$$

Đây chính là hệ phương trình Newton-KKT mà chúng ta sẽ dùng ở Bài 04 để giải các bài toán tối ưu phi tuyến có ràng buộc đẳng thức.

---

## 7. Khoảng cách đối ngẫu và Độ nhạy nhân tử (Shadow Price)

Với bất kỳ điểm khả thi gốc $x$ và bộ nhân tử khả thi đối ngẫu $(\lambda, \nu)$, ta luôn kẹp được giá trị tối ưu chưa biết $p^*$:

$$
g(\lambda, \nu) \le p^* \le f_0(x).
$$

Hiệu số $\eta = f_0(x) - g(\lambda, \nu) \ge 0$ được gọi là **khoảng cách đối ngẫu (duality gap)**. Ý nghĩa thực tiễn to lớn của khoảng cách đối ngẫu: nó cung cấp một **tiêu chuẩn dừng thuật toán** chính xác tuyệt đối. Khi một thuật toán tối ưu tạo ra một cặp nghiệm $(x^{(k)}, (\lambda^{(k)}, \nu^{(k)}))$ thỏa mãn $f_0(x^{(k)}) - g(\lambda^{(k)}, \nu^{(k)}) \le \epsilon$, ta biết chắc chắn rằng nghiệm hiện tại chỉ cách nghiệm tối ưu thực tế không quá $\epsilon$, dù không hề biết trước giá trị $p^*$.

### Ý nghĩa kinh tế: Nhân tử Lagrange là Độ nhạy biên (Shadow Price)
Xét bài toán khi ta nới lỏng ràng buộc từ $f_i(x) \le 0$ thành $f_i(x) \le u_i$. Gọi $p^*(u)$ là giá trị tối ưu của bài toán bị nhiễu theo vector $u$.

Dưới các điều kiện chính quy, đạo hàm riêng của giá trị tối ưu theo độ lệch ràng buộc thỏa mãn:

$$
\lambda_i^* = -\frac{\partial p^*(u)}{\partial u_i} \Bigg|_{u = 0}.
$$

Nhân tử Lagrange $\lambda_i^*$ đo lường tốc độ suy giảm của chi phí tối ưu khi ta nới lỏng thêm một đơn vị tài nguyên ở ràng buộc thứ $i$. Nếu $\lambda_i^* = 100$, điều đó có nghĩa là nếu ta mua thêm 1 đơn vị tài nguyên ở ràng buộc $i$, lợi ích tối ưu thu về sẽ tăng thêm xấp xỉ 100 đơn vị tiền tệ. Đây chính là khái niệm **giá bóng** (shadow price) trong kinh tế học quản trị.

---

## Bài tập tự luyện

::: exercise 1. Tính toán hàm đối ngẫu cho bài toán bình phương đơn giản
Xét bài toán tối ưu: $\min_x x^2$ với điều kiện $x \ge 1$.
1. Viết bài toán dưới dạng chuẩn và thiết lập hàm Lagrangian.
2. Tìm hàm đối ngẫu Lagrange $g(\lambda)$ và giải bài toán đối ngẫu để tìm $\lambda^*$.
:::
::: solution
1. Ràng buộc chuẩn: $f_1(x) = 1 - x \le 0$. Hàm Lagrangian với $\lambda \ge 0$:
   $$L(x, \lambda) = x^2 + \lambda(1 - x).$$
2. Để tìm $g(\lambda) = \inf_x L(x, \lambda)$, lấy đạo hàm theo $x$:
   $$\frac{\partial L}{\partial x} = 2x - \lambda = 0 \implies x(\lambda) = \frac{\lambda}{2}.$$
   Thay vào Lagrangian:
   $$g(\lambda) = \left(\frac{\lambda}{2}\right)^2 + \lambda\left(1 - \frac{\lambda}{2}\right) = \frac{\lambda^2}{4} + \lambda - \frac{\lambda^2}{2} = \lambda - \frac{\lambda^2}{4}.$$
   Bài toán đối ngẫu: $\max_{\lambda \ge 0} \left( \lambda - \frac{\lambda^2}{4} \right)$. Đạo hàm $1 - \frac{\lambda}{2} = 0 \iff \lambda^* = 2$. Giá trị đối ngẫu tối ưu là $d^* = g(2) = 2 - 1 = 1$. Nghiệm gốc thu hồi là $x^* = \lambda^*/2 = 1$, cho giá trị tối ưu $p^* = 1^2 = 1 = d^*$.
:::

::: exercise 2. Trường hợp nhân tử bằng 0 tại biên ràng buộc chặt
Xét bài toán tối ưu: $\min_x x^2$ với điều kiện $x \le 0$.
Hãy xác minh hệ điều kiện KKT tại điểm $x = 0$ và $\lambda = 0$. Ràng buộc này có chặt không?
:::
::: solution
- Khả thi gốc: $x = 0 \le 0$ (thỏa mãn).
- Khả thi đối ngẫu: $\lambda = 0 \ge 0$ (thỏa mãn).
- Bù trừ: $\lambda x = 0 \cdot 0 = 0$ (thỏa mãn).
- Triệt tiêu gradient: $\nabla L(0, 0) = 2x + \lambda = 2(0) + 0 = 0$ (thỏa mãn).

Tại nghiệm $x = 0$, ràng buộc $x \le 0$ là **chặt** vì $f_1(0) = 0$, tuy nhiên nhân tử Lagrange lại bằng 0 ($\lambda = 0$). Đây là một ví dụ điển hình chứng minh rằng chiều suy luận *"ràng buộc chặt thì nhân tử phải dương"* không phải lúc nào cũng đúng. Lý do: điểm cực tiểu không ràng buộc của hàm số vốn đã rơi đúng vào $x = 0$, do đó ràng buộc ở đây không hề tạo ra lực cản nào lên nghiệm.
:::

::: exercise 3. Chứng nhận nghiệm KKT cho bài toán hồi quy có ràng buộc
Xét bài toán hồi quy ở Bài 02: hàm mất mát $f(w) = 7w^2 - 11w + \frac{9}{2}$ với ràng buộc $w \le \frac{1}{2}$.
Hãy thiết lập điều kiện KKT và tìm nhân tử Lagrange $\lambda^*$ để chứng nhận nghiệm $w^* = \frac{1}{2}$.
:::
::: solution
Viết lại ràng buộc dưới dạng chuẩn: $f_1(w) = w - \frac{1}{2} \le 0$.
Hàm Lagrangian: $L(w, \lambda) = 7w^2 - 11w + \frac{9}{2} + \lambda\left(w - \frac{1}{2}\right)$.
Điều kiện triệt tiêu gradient tại $w^* = \frac{1}{2}$:
$$
\begin{aligned}
f'(w^*) + \lambda &= 14w^* - 11 + \lambda \\
&= 14\left(\frac{1}{2}\right) - 11 + \lambda = -4 + \lambda = 0 \iff \lambda^* = 4.
\end{aligned}
$$
Kiểm tra bốn nhóm KKT:
1. Khả thi gốc: $w^* = \frac{1}{2} \le \frac{1}{2}$ (thỏa mãn).
2. Khả thi đối ngẫu: $\lambda^* = 4 \ge 0$ (thỏa mãn).
3. Bù trừ: $\lambda^* (w^* - \frac{1}{2}) = 4 \cdot 0 = 0$ (thỏa mãn).
4. Dừng: $f'(w^*) + \lambda^* = -4 + 4 = 0$ (thỏa mãn).

Vì bài toán gốc là bài toán tối ưu lồi ngặt và thỏa mãn điều kiện Slater, hệ điều kiện KKT chứng nhận tuyệt đối rằng $w^* = \frac{1}{2}$ là nghiệm tối ưu toàn cục duy nhất với chi phí $p^* = \frac{3}{4}$.
:::

---

## Tóm tắt cốt lõi

1. **Hàm Lagrangian và Đối ngẫu yếu**: Bằng cách ghép các ràng buộc với nhân tử $\lambda \succeq 0$, hàm đối ngẫu $g(\lambda, \nu) = \inf_x L(x, \lambda, \nu)$ luôn tạo ra một cận dưới không thể đánh bại: $g(\lambda, \nu) \le p^*$.
2. **Tính lõm của bài toán đối ngẫu**: Hàm đối ngẫu luôn luôn là hàm lõm, do đó bài toán cực đại hóa cận dưới luôn là bài toán tối ưu lồi, ngay cả khi bài toán gốc phi lồi.
3. **Điều kiện Slater và Đối ngẫu mạnh**: Đối với bài toán lồi, sự tồn tại của một điểm khả thi ngặt (Slater point) bảo đảm khoảng cách đối ngẫu triệt tiêu hoàn toàn ($p^* = d^*$).
4. **Hệ điều kiện KKT**: Bốn nhóm điều kiện (Khả thi gốc, Khả thi đối ngẫu, Bù trừ, Triệt tiêu gradient) tạo thành chiếc chìa khóa vạn năng để nhận diện và chứng nhận nghiệm tối ưu trong không gian có ràng buộc.

---

## Tài liệu tham khảo và Đọc thêm

Dành cho bạn đọc muốn nghiên cứu sâu lý thuyết đối ngẫu và ứng dụng trong khoa học dữ liệu:
- **Stephen Boyd & Lieven Vandenberghe**, *Convex Optimization*, Cambridge University Press. Đọc kỹ Chương 5 (Đối ngẫu Lagrange, điều kiện Slater, KKT, bài toán đối ngẫu định dạng ma trận, và phân tích độ nhạy).
- **Dimitri P. Bertsekas**, *Convex Optimization Theory*, Athena Scientific. Tài liệu xuất sắc về giải tích hình học của đối ngẫu, siêu phẳng tựa và các điều kiện chính quy nới lỏng.

Tiếp theo: [Bài 04 — Thuật toán Gradient Descent và Phương pháp Newton](./bai-04-gradient-newton.md).
