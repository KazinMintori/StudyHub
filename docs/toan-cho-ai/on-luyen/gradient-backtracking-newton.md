---
course: toan-cho-ai
lecture: on-luyen
topic: gradient-backtracking-newton
section: topic
title: "Gradient, backtracking và hướng Newton"
description: "Hướng giảm, đường mức, learning rate, thuật toán gradient, Armijo, hai vòng thử bước đầy đủ, quét lưới và hướng Newton."
---

Biết hướng đi xuống chưa đủ để chọn được điểm tiếp theo. Bước quá dài có thể đi qua vùng thấp rồi leo lên phía bên kia. Ta cần tách hai quyết định: Hướng đi và độ dài bước.

## 1. Hướng giảm

Giả sử $f$ khả vi tại $x$ và $\nabla f(x)\ne0$. Một hướng $d$ có

$$
\nabla f(x)^Td<0
$$

là hướng giảm theo đạo hàm bậc nhất. Vì

$$
\begin{aligned}
f(x+td) &= f(x)+t\nabla f(x)^Td+o(t), \\
&\frac{o(t)}t \to0\quad(t\to0^+),
\end{aligned}
$$

nên $f(x+td)<f(x)$ với $t>0$ đủ nhỏ. Khi gradient và $d$ đều khác không, tích vô hướng âm tương đương góc giữa chúng lớn hơn $\pi/2$.

Chọn $d=-\nabla f(x)$ thì

$$
\nabla f(x)^Td=-\|\nabla f(x)\|_2^2<0.
$$

Trong các hướng có chuẩn Euclid bằng 1, hướng gradient âm đã chuẩn hóa cho tốc độ giảm bậc nhất lớn nhất. Phát biểu “dốc nhất” phụ thuộc chuẩn dùng để giới hạn độ lớn hướng.

## 2. Đường mức và đường lặp

Đường mức là tập các điểm thỏa $f(x)=c$. Gradient vuông góc với đường mức tại một điểm trơn có gradient khác không. Trong hình đường mức của buổi học, các điểm $x_0,x_1,x_2,x_3$ lần lượt đi vào các mức mục tiêu thấp hơn về phía nghiệm.

Đường lặp có thể gấp khúc, vì gradient được tính lại tại mỗi điểm. Một hình vẽ đi vào tâm minh họa ý tưởng giảm, nhưng không thay cho chứng minh hội tụ của một thuật toán cụ thể.

## 3. Thuật toán gradient

Chọn điểm đầu $x_0$ và dung sai $\varepsilon>0$. Với $k=0,1,2,\ldots$:

1. Tính $g_k=\nabla f(x_k)$.
2. Nếu $\|g_k\|_2<\varepsilon$, dừng.
3. Đặt $d_k=-g_k$ và tìm bước $t_k>0$.
4. Cập nhật $x_{k+1}=x_k+t_kd_k$.

Bước $t_k$ còn được gọi là tốc độ học, hay learning rate. Chuẩn gradient nhỏ chỉ chứng nhận gần điểm dừng theo tiêu chuẩn đang dùng. Với bài phi lồi, điểm dừng có thể là cực tiểu, cực đại hoặc điểm yên ngựa. Thuật toán ở đây là không ràng buộc. Nếu có miền $D$, còn phải bảo đảm bước mới khả thi hoặc dùng phương pháp chiếu, phương pháp xử lý ràng buộc thích hợp.

## 4. Backtracking Armijo

Chọn $\alpha\in(0,1/2)$ và $\beta\in(0,1)$. Bắt đầu với $t=1$. Nếu chưa thỏa

$$
f(x+td)\le f(x)+\alpha t\nabla f(x)^Td,
$$

thì thay $t$ bằng $\beta t$ rồi thử lại. Nếu hàm có miền xác định hạn chế, một bước ra ngoài miền cũng phải bị loại. Bất đẳng thức Armijo yêu cầu một phần cố định của mức giảm mà xấp xỉ tuyến tính dự đoán.

Với hướng gradient âm, điều kiện trở thành

$$
f(x+td)\le f(x)-\alpha t\|\nabla f(x)\|_2^2.
$$

Vì $d$ là hướng giảm và $\alpha<1$, các bước dương đủ nhỏ sẽ thỏa khi điểm hiện tại nằm trong miền mở và hàm khả vi. Hệ số $\beta<1$ khiến dãy bước thử tiến về không, nên backtracking dừng sau hữu hạn lần trong các điều kiện này.

::: info Phân biệt Armijo và Wolfe
Lưu ý: Vòng lặp được trình bày ở đây kiểm tra điều kiện giảm đủ Armijo. Điều kiện Wolfe hoàn chỉnh còn bao gồm thêm điều kiện độ cong liên quan đến gradient tại điểm mới.
:::

## 5. Ví dụ đầy đủ hai vòng lặp

Xét

$$
\begin{aligned}
f(x,y) &= x^2+2y^2, \\
x_0 &= (2,1), \\
\alpha &= 0.1,\quad\beta=0.5.
\end{aligned}
$$

Hessian là $\operatorname{diag}(2,4)\succ0$, nên nghiệm duy nhất là $(0,0)$ và giá trị tối ưu bằng không.

### Vòng thứ nhất

Tại $x_0=(2,1)$, giá trị mục tiêu là 6, gradient $g_0=(4,4)$, hướng $d_0=(-4,-4)$ và $\|g_0\|_2^2=32$. Mỗi bước thử có điểm mới $(2-4t,1-4t)$.

| Bước $t$ | Điểm thử | $f$ tại điểm thử | Cận Armijo | Kết quả |
| --- | --- | --- | --- | --- |
| $1$ | $(-2,-3)$ | $22$ | $2.8$ | Loại |
| $1/2$ | $(0,-1)$ | $2$ | $4.4$ | Nhận |

Dòng đầu so $22$ với $6-0.1\cdot32=2.8$. Dòng thứ hai so $2$ với $6-0.1\cdot(1/2)\cdot32=4.4$. Bước được nhận là $t_0=1/2$, nên $x_1=(0,-1)$.

### Vòng thứ hai

Tính lại tại $x_1$: Giá trị mục tiêu là 2, gradient $g_1=(0,-4)$, hướng $d_1=(0,4)$ và $\|g_1\|_2^2=16$. Khởi động lại bước thử từ 1.

| Bước $t$ | Điểm thử | $f$ tại điểm thử | Cận Armijo | Kết quả |
| --- | --- | --- | --- | --- |
| $1$ | $(0,3)$ | $18$ | $0.4$ | Loại |
| $1/2$ | $(0,1)$ | $2$ | $1.2$ | Loại |
| $1/4$ | $(0,0)$ | $0$ | $1.6$ | Nhận |

Vậy $t_1=1/4$ và $x_2=(0,0)$. Gradient bằng không nên thuật toán dừng. Mục tiêu giảm từ 6 xuống 2 rồi xuống 0.

::: warning Đọc đúng dòng thử bước thứ hai
Ảnh B4-22 có một số giá trị nháp được viết xen ở các bước khác nhau. Với $t=1$, điểm thử là $(0,3)$ và mục tiêu phải bằng 18. Giá trị 2 và cận 1.2 thuộc bước $t=1/2$. Bảng phía trên giữ đủ các lần thử và tách rõ từng giá trị.
:::

<MathLab type="optimizer" />

Mô phỏng dùng một hàm toàn phương khác và bước học có thể điều chỉnh. Nó giúp so hướng gradient với Newton và quan sát bước quá lớn, còn các số của ví dụ ôn luyện đã được tính riêng trong hai bảng.

## 6. Vì sao không quét hết một lưới?

Trong một chiều, ta có thể lấy $m$ vị trí trong một đoạn $[a,b]$ và so giá trị mục tiêu. Cách này không tự tìm đúng cực tiểu nằm giữa hai điểm lưới. Muốn có sai số bảo đảm, cần thêm tính chất của hàm và độ mịn lưới.

Trong nhiều chiều, miền hộp có dạng

$$
[a_1,b_1]\times\cdots\times[a_n,b_n].
$$

Nếu mỗi trục có $m$ lựa chọn, tổng số điểm là tích

$$
\underbrace{m\cdot m\cdots m}_{n\text{ factors}}=m^n.
$$

Chỉ hai lựa chọn trên mỗi trục đã tạo $2^{64}$ điểm khi có 64 chiều và $2^{100}$ điểm khi có 100 chiều. Giá trị chính xác lần lượt là 18446744073709551616 và 1267650600228229401496703205376. Đây là sự bùng nổ số tổ hợp theo số chiều mà hình lưới trên bảng minh họa. Các phương pháp dùng đạo hàm khai thác cấu trúc cục bộ để tránh liệt kê toàn bộ lưới.

## 7. Hướng Newton

Taylor bậc hai tại điểm hiện tại tạo mô hình theo dịch chuyển $d$:

$$
\begin{aligned}
q(d) &= f(x)+\nabla f(x)^Td+\frac12d^THd, \\
H &= \nabla^2f(x).
\end{aligned}
$$

Nếu $H\succ0$, mô hình có cực tiểu duy nhất tại nghiệm của

$$
Hd=-\nabla f(x).
$$

Dạng biểu thức là $d=-H^{-1}\nabla f(x)$. Trong triển khai, giải hệ tuyến tính thay vì tính ma trận nghịch đảo. Với gradient khác không,

$$
\nabla f(x)^Td=-\nabla f(x)^TH^{-1}\nabla f(x)<0,
$$

nên hướng Newton là hướng giảm. Với Hessian không PD, tính khả nghịch riêng nó chưa đủ bảo đảm tính giảm.

Trong ví dụ $f=x^2+2y^2$, hệ Newton tại $(2,1)$ cho $d=(-2,-1)$. Bước đầy đủ $t=1$ đến ngay $(0,0)$. Đây là tính chất của hàm toàn phương PD, không phải bảo đảm một bước cho mọi hàm trơn.

## 8. Bài tập tự luyện

::: exercise Hướng đúng nhưng bước sai
Vì sao $d_0=(-4,-4)$ là hướng giảm tại $(2,1)$ nhưng bước $t=1$ làm mục tiêu tăng từ 6 lên 22?
:::

::: solution
Tích gradient với hướng bằng $-32$, nên bước đủ nhỏ sẽ giảm. Tuy nhiên, dọc hướng này mục tiêu là $6-32t+48t^2$. Tại $t=1$, số hạng độ cong lớn hơn mức giảm bậc nhất. Vì vậy hướng giảm không bảo đảm mọi bước dương đều giảm. Backtracking kiểm giá trị thật rồi thu bước đến khi đạt điều kiện giảm đủ.
:::
