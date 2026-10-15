---
course: toan-cho-ai
lecture: on-luyen
topic: doi-ngau-lagrange
section: topic
title: "Đối ngẫu Lagrange và điều kiện Slater"
description: "Bài toán gốc, hàm đối ngẫu, tính lõm, đối ngẫu yếu và mạnh, Slater, cách tính infimum và hai ví dụ có chứng nhận."
---

Một điểm khả thi cho biết ta có thể đạt một giá trị mục tiêu nào đó. Muốn chứng minh không điểm nào tốt hơn, ta cần một cận dưới. Đối ngẫu Lagrange tìm chính cận dưới ấy bằng cách chọn các trọng số của ràng buộc.

## 1. Bài toán gốc và hàm đối ngẫu

Với bài min $f(x)$ dưới các ràng buộc $f_i(x)\le0$ và $h_j(x)=0$, gọi bài ban đầu là **bài toán gốc**, hay primal. Lagrangian đã được [khai triển đầy đủ](./dieu-kien-kkt.md) là

$$
L(x,\mu,\lambda)=f(x)+\sum_{i=1}^{m}\mu_i f_i(x)+\sum_{j=1}^{p}\lambda_j h_j(x).
$$

Giữ cố định các nhân tử rồi lấy cận dưới đúng theo $x$:

$$
g(\mu,\lambda)=\inf_{x\in\mathcal X}L(x,\mu,\lambda).
$$

Ở đây $\mathcal X$ là miền xác định chung của các hàm, không phải miền đã ép thỏa tất cả ràng buộc. Khi các hàm xác định trên toàn $\mathbb R^n$, infimum được lấy trên toàn không gian ấy. Hàm $L$ có tổng cộng $n+m+p$ biến vô hướng, nhưng phép infimum chỉ tối ưu theo $n$ biến gốc.

## 2. Đối ngẫu yếu

Với $x$ khả thi và $\mu\ge0$ theo từng thành phần,

$$
g(\mu,\lambda)\le L(x,\mu,\lambda)\le f(x).
$$

Vì vậy mỗi bộ nhân tử khả thi cung cấp một cận dưới cho mọi giá trị mục tiêu khả thi. Bài toán đối ngẫu là chọn cận tốt nhất:

$$
\begin{aligned}
&\max_{\mu,\lambda}g(\mu,\lambda),\\
&\mu_i\ge0,\quad i=1,\ldots,m,\\
&\lambda\in\mathbb R^p.
\end{aligned}
$$

Gọi $p^\star$ là infimum bài gốc và $d^\star$ là supremum bài đối ngẫu. **Đối ngẫu yếu** phát biểu $d^\star\le p^\star$. Kết quả này không cần bài gốc lồi. Dấu $\mu\ge0$ nghĩa là mọi thành phần không âm, hoàn toàn không có nghĩa mọi thành phần bằng không.

## 3. Vì sao hàm đối ngẫu lõm?

Với $x$ cố định, $L$ là affine theo bộ nhân tử $u=(\mu,\lambda)$. Cho hai bộ $u,v$ và $t\in[0,1]$,

$$
\begin{aligned}
g(tu + (1 - t)v) &= \inf_x [tL(x, u) + (1 - t)L(x, v)] \\
&\ge t\inf_x L(x, u) + (1 - t)\inf_x L(x, v) \\
&= tg(u) + (1 - t)g(v).
\end{aligned}
$$

Bất đẳng thức nằm theo chiều này vì từng $L(x,u)\ge\inf_zL(z,u)$. Do đó $g$ lõm, hay tương đương $-g$ lồi, trên miền hữu hiệu nơi hàm nhận giá trị hữu hạn. Infimum có thể bằng $-\infty$ tại một số bộ nhân tử.

## 4. Đối ngẫu mạnh và Slater

**Đối ngẫu mạnh** nghĩa là $p^\star=d^\star$. Điều kiện Slater là một điều kiện đủ cho kết luận này trong bài toán lồi.

Giả sử $f,f_i$ lồi và $h_j$ affine. Slater yêu cầu một điểm $\bar x$ trong nội tương đối của miền chung thỏa

$$
\begin{aligned}
f_i(\bar x) &< 0, \quad i = 1, \dots, m, \\
h_j(\bar x) &= 0, \quad j = 1, \dots, p.
\end{aligned}
$$

Nội tương đối là phần trong khi nhìn trong không gian affine nhỏ nhất chứa miền. Nếu miền chung là toàn $\mathbb R^n$, điều kiện này trở về cách hiểu điểm trong thông thường. Với giá trị tối ưu hữu hạn, Slater cho đối ngẫu mạnh và sự đạt nghiệm đối ngẫu. Khi nghiệm gốc cũng đạt, KKT là điều kiện cần và đủ cho tối ưu dưới các giả thiết khả vi tương ứng.

Slater là điều kiện đủ, không phải phép kiểm cần và đủ cho mọi bài. Khi không tìm được điểm Slater, chưa thể suy ra có khoảng cách đối ngẫu dương.

## 5. Cách tính hàm đối ngẫu

Một cách làm thường dùng là giải $\nabla_x L=0$ rồi thay nghiệm vào $L$. Tuy nhiên, bước này đúng để tính infimum chỉ khi điểm dừng thật sự cực tiểu hóa $L$ theo $x$.

Với $L$ lồi khả vi theo $x$, điểm dừng là cực tiểu toàn cục. Nếu $L$ không lồi, phải xét các điểm dừng, biên miền và khả năng không bị chặn dưới. Không được lấy tùy ý một điểm dừng để gọi là giá trị $g$.

## 6. Ví dụ một biến

Xét min $x^2$ với $x\ge1$. Viết ràng buộc $1-x\le0$ và dùng nhân tử $\lambda\ge0$ cho bất đẳng thức duy nhất. Trong ví dụ này, ký hiệu $\lambda$ đóng vai trò của $\mu$ trong dạng tổng quát.

$$
\begin{aligned}
L(x,\lambda) &= x^2+\lambda(1-x), \\
\frac{\partial L}{\partial x} &= 2x-\lambda=0, \\
x(\lambda) &= \lambda/2.
\end{aligned}
$$

Hessian theo $x$ bằng 2 nên điểm dừng là cực tiểu duy nhất. Thay vào được

$$
\begin{aligned}
g(\lambda) &= \frac{\lambda^2}{4} + \lambda\left(1 - \frac{\lambda}{2}\right) \\
&= \lambda - \frac{\lambda^2}{4} \\
&= 1 - \frac{(\lambda - 2)^2}{4}.
\end{aligned}
$$

Vì $\lambda\ge0$, đối ngẫu đạt cực đại 1 tại $\lambda^\star=2$. Bài gốc đạt 1 tại $x^\star=1$, nên hai giá trị bằng nhau. Điểm $x=2$ thỏa nghiêm ràng buộc, xác nhận Slater.

## 7. Ví dụ hai biến

Xét min $x_1^2+x_2^2$ với $x_1+x_2\ge1$. Dùng ký hiệu $s\ge0$ cho nhân tử để tránh nhầm với vector đầu ra $y$ của hồi quy. Trên bảng nhân tử này được viết là $y$.

$$
\begin{aligned}
L(x_1,x_2,s) &= x_1^2+x_2^2+s(1-x_1-x_2), \\
2x_1-s &= 0,\quad2x_2-s=0.
\end{aligned}
$$

Hai tọa độ cực tiểu Lagrangian đều bằng $s/2$. Do đó

$$
g(s) = s-\frac{s^2}{2} = \frac12-\frac{(s-1)^2}{2}.
$$

Đối ngẫu đạt $d^\star=1/2$ tại $s^\star=1$. Thu hồi nghiệm $x^\star=(1/2,1/2)$, có $p^\star=1/2$. Điểm $(1,1)$ thỏa nghiêm ràng buộc nên Slater áp dụng.

## 8. Bài tập tự luyện

::: exercise Vì sao một bộ nhân tử chứng nhận được nghiệm?
Trong ví dụ hai biến, hãy viết một đẳng thức hoàn thành bình phương của $L(x_1,x_2,1)$ rồi dùng nó để chứng minh mọi điểm khả thi có mục tiêu ít nhất $1/2$.
:::

::: solution
Ta có

$$
L(x_1,x_2,1) = (x_1-1/2)^2+(x_2-1/2)^2+1/2 \ge 1/2.
$$

Tại điểm khả thi, $L\le f$. Vì vậy $f\ge1/2$. Điểm $(1/2,1/2)$ đạt cận nên tối ưu.
:::
