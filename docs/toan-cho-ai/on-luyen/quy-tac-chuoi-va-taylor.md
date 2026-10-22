---
course: toan-cho-ai
lecture: on-luyen
topic: quy-tac-chuoi-va-taylor
section: topic
title: "Quy tắc chuỗi và Taylor nhiều biến"
description: "Sai số xấp xỉ, hàm hợp, quy tắc chuỗi, đường cong, đạo hàm dọc đường thẳng và Taylor bậc một, bậc hai."
---

Thuật toán tối ưu cần biết điều gì xảy ra khi đi từ $x$ sang $x+h$. Thay vì biến đổi trực tiếp một hàm nhiều biến, ta theo dõi giá trị mục tiêu dọc một đường đi có một tham số. Quy tắc chuỗi biến thao tác này thành một bài đạo hàm một biến.

## 1. Xấp xỉ nghiệm và khoảng cách

Với bài min $f(x)$ trên $D$, giả sử tồn tại nghiệm $x^\star$. Một điểm $x\in D$ xấp xỉ nghiệm theo khoảng cách với dung sai $\varepsilon>0$ nếu

$$
\|x-x^\star\|_2\le\varepsilon.
$$

Khoảng cách Euclid được tính bằng

$$
\begin{aligned}
\|x-y\|_2^2 &= (x_1-y_1)^2+\cdots+(x_n-y_n)^2, \\
\|x-y\|_2 &= \left(\sum_{i=1}^{n}(x_i-y_i)^2\right)^{1/2}.
\end{aligned}
$$

Một thuật toán lặp chọn $x_0$, rồi tạo $x_1,x_2,\ldots$. Khi viết $x_k\to x^\star$, ta khẳng định khoảng cách đến nghiệm tiến về không, điều phải được chứng minh dưới giả thiết phù hợp, không tự có từ việc các giá trị mục tiêu giảm.

Vì chưa biết $x^\star$, tiêu chuẩn khoảng cách thường không kiểm trực tiếp được. Chuẩn gradient nhỏ là một tiêu chuẩn dừng khác. Không đồng nhất sai số nghiệm, sai số mục tiêu và chuẩn gradient nếu chưa có quan hệ định lượng giữa chúng.

## 2. Công thức một biến với điểm trung gian

Định lý giá trị trung bình cho

$$
\begin{aligned}
f(x+h) &= f(x)+f'(x+\theta_1h)h, \\
&0 <\theta_1<1.
\end{aligned}
$$

Công thức đúng với cả $h>0$ và $h<0$, vì $x+\theta_1h$ luôn nằm giữa hai đầu. Nếu hàm thuộc $C^2$ trên một lân cận của đoạn, Taylor bậc hai cho

$$
\begin{aligned}
f(x+h) &= f(x)+f'(x)h+\frac12f''(x+\theta_2h)h^2, \\
&0 <\theta_2<1.
\end{aligned}
$$

Hai điểm trung gian $\theta_1,\theta_2$ có thể khác nhau.

## 3. Quy tắc chuỗi một biến

Cho $f:\mathbb R\to\mathbb R$ và $g:\mathbb R\to\mathbb R$. Chuỗi ánh xạ là

$$
x\longmapsto f(x)\longmapsto g(f(x)).
$$

Nếu các hàm khả vi tại các điểm tương ứng,

$$
(g\circ f)'(x)=g'(f(x))f'(x).
$$

Đạo hàm của hàm ngoài được lấy tại **đầu ra của hàm trong**. Bỏ vị trí đánh giá này là một lỗi ký hiệu có thể làm tính sai.

## 4. Hàm trong có nhiều thành phần

Cho $F:\mathbb R^n\to\mathbb R^m$ và $g:\mathbb R^m\to\mathbb R$. Viết

$$
\begin{aligned}
F(x) &= (F_1(x),\ldots,F_m(x)), \\
G(x) &= (g\circ F)(x) \\
&= g(F_1(x),\ldots,F_m(x)).
\end{aligned}
$$

Với hai thành phần của hàm trong, đạo hàm theo $x_i$ là

$$
\frac{\partial G}{\partial x_i}(x) = \frac{\partial g}{\partial y_1}(F(x)) \frac{\partial F_1}{\partial x_i}(x) + \frac{\partial g}{\partial y_2}(F(x)) \frac{\partial F_2}{\partial x_i}(x).
$$

Mỗi số hạng đi qua một nhánh trung gian. Cộng tất cả $m$ nhánh cho công thức tổng quát

$$
\frac{\partial G}{\partial x_i}(x) = \sum_{j=1}^{m} \frac{\partial g}{\partial y_j}(F(x)) \frac{\partial F_j}{\partial x_i}(x).
$$

Không viết $\partial g/\partial x_i$ nếu $g$ thực sự nhận các biến $y_j$. Hàm hợp $G$ mới nhận biến $x_i$.

## 5. Đạo hàm dọc một đường cong

Cho đường cong khả vi $\varphi:I\to\mathbb R^n$,

$$
\varphi(t)=(\varphi_1(t),\ldots,\varphi_n(t)).
$$

Hàm $f\circ\varphi$ trả về mục tiêu tại từng vị trí trên đường đi. Khi $n=2$,

$$
\frac{d}{dt}f(\varphi(t))=f_{x_1}(\varphi(t))\varphi_1'(t)+f_{x_2}(\varphi(t))\varphi_2'(t).
$$

Trong $n$ chiều, công thức là

$$
\begin{aligned}
\frac{d}{dt}f(\varphi(t)) &= \sum_{i=1}^{n}f_{x_i}(\varphi(t))\varphi_i'(t)\\
&= \nabla f(\varphi(t))^T\varphi'(t).
\end{aligned}
$$

Gradient đo mức nhạy của mục tiêu với từng tọa độ, còn $\varphi_i'$ đo tốc độ thay đổi của tọa độ ấy. Tổng các đóng góp cho tốc độ thay đổi mục tiêu dọc đường.

## 6. Hạn chế lên đường thẳng

Cố định $x,h\in\mathbb R^n$ và đặt

$$
\begin{aligned}
\varphi(t) &= x+th, \\
g(t) &= f(x+th).
\end{aligned}
$$

Các tọa độ của đường là $x_i+th_i$ và đạo hàm của chúng bằng $h_i$. Do đó

$$
\begin{aligned}
g'(t) &= \sum_{i=1}^{n}f_{x_i}(x+th)h_i\\
&= \nabla f(x+th)^Th.
\end{aligned}
$$

Nếu $f\in C^2$, lấy đạo hàm lần nữa được

$$
\begin{aligned}
g''(t) &= \sum_{i=1}^{n}\sum_{j=1}^{n} f_{x_jx_i}(x+th)h_ih_j\\
&= h^T\nabla^2f(x+th)h.
\end{aligned}
$$

Để thấy rõ tổng kép, trong hai chiều nó gồm bốn số hạng:

$$
g''(t) = f_{x_1x_1}h_1^2 + f_{x_2x_1}h_1h_2 + f_{x_1x_2}h_2h_1 + f_{x_2x_2}h_2^2.
$$

Các đạo hàm trên đều được đánh giá tại $x+th$. Vì Hessian đối xứng, hai số hạng hỗn hợp có thể gộp. Ma trận $A$ được viết trong khai triển trên bảng chính là Hessian tại điểm dọc đường, không phải một ma trận hằng tùy ý.

## 7. Taylor nhiều biến

Áp dụng giá trị trung bình cho $g$ trên $[0,1]$:

$$
\begin{aligned}
g(1) &= g(0)+g'(\theta_1), \\
f(x+h) &= f(x)+\nabla f(x+\theta_1h)^Th.
\end{aligned}
$$

Đây là công thức bậc một có điểm trung gian. Taylor bậc hai cho

$$
f(x+h)=f(x)+\nabla f(x)^Th+\frac12h^T\nabla^2f(x+\theta_2h)h.
$$

Các đoạn đang xét phải nằm trong miền xác định, cùng các điều kiện khả vi liên tục tương ứng. Nếu thay $h$ bằng $td$,

$$
f(x+td)=f(x)+t\nabla f(x)^Td+\frac{t^2}{2}d^T\nabla^2f(x+\theta td)d.
$$

Số hạng bậc nhất tỷ lệ với $t$, còn số hạng bậc hai tỷ lệ với $t^2$. Vì vậy khi $t>0$ đủ nhỏ, dấu của tích $\nabla f(x)^Td$ quyết định việc mục tiêu tăng hay giảm nếu tích này khác không.

## 8. Bài tập tự luyện

::: exercise Tính dọc đường trước khi dùng ma trận
Cho $f(x,y)=x^2+2y^2$, điểm $(2,1)$ và hướng $h=(-4,-4)$. Khai triển trực tiếp $g(t)=f((2,1)+th)$ rồi so sánh $g'(0)$ và $g''(t)$ với công thức gradient, Hessian.
:::

::: solution
Khai triển được

$$
\begin{aligned}
g(t) &= (2-4t)^2+2(1-4t)^2 \\
&= 6-32t+48t^2, \\
g'(0) &= -32,\quad g''(t)=96.
\end{aligned}
$$

Gradient tại $(2,1)$ là $(4,4)^T$, nên tích với $h$ bằng $-32$. Hessian là ma trận chéo với hai phần tử 2 và 4, nên $h^THh=2\cdot16+4\cdot16=96$. Hai cách khớp nhau.
:::
