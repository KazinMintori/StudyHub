---
course: toan-cho-ai
lecture: on-luyen
topic: dao-ham-va-cuc-tri
section: topic
title: "Đạo hàm, gradient, Hessian và cực trị"
description: "Đạo hàm qua giới hạn, giá trị trung bình, Taylor, Fermat, đạo hàm riêng, Hessian và điều kiện cực tiểu."
---

Một đạo hàm bằng không có đủ để kết luận đã tìm thấy cực tiểu không? Để trả lời, cần phân biệt điều kiện cần, điều kiện đủ và phạm vi địa phương của mỗi kết luận.

## 1. Đạo hàm và định lý giá trị trung bình

Với hàm một biến khả vi tại $x$,

$$
f'(x)=\lim_{h\to0}\frac{f(x+h)-f(x)}h.
$$

Đạo hàm đo tốc độ thay đổi khi bước $h$ tiến về không. Nếu $f$ liên tục trên đoạn nối $x_0$ với $x$ và khả vi trong khoảng giữa hai điểm, định lý giá trị trung bình cho một $z$ nằm giữa chúng sao cho

$$
\frac{f(x)-f(x_0)}{x-x_0} = f'(z).
$$

Tương đương,

$$
f(x)=f(x_0)+f'(z)(x-x_0).
$$

Công thức phân số giả sử $x\ne x_0$. Đây là một đẳng thức tại một điểm trung gian, không phải khẳng định đạo hàm không đổi trên cả khoảng.

## 2. Taylor bậc hai

Nếu $f$ có đạo hàm bậc hai liên tục trên một lân cận của đoạn xét, tồn tại $z$ nằm giữa $x_0$ và $x$ sao cho

$$
f(x)=f(x_0)+f'(x_0)(x-x_0)+\frac12 f''(z)(x-x_0)^2.
$$

Số hạng bậc nhất dự đoán xu hướng, còn số hạng bậc hai đo phần sai lệch do độ cong. Khi viết xấp xỉ bậc hai tại $x_0$, ta thay $f''(z)$ bằng $f''(x_0)$ và phải hiểu đó là xấp xỉ, trừ trường hợp hàm toàn phương.

## 3. Cực tiểu địa phương và Fermat

Điểm $x_0$ là cực tiểu địa phương nếu tồn tại $\varepsilon>0$ sao cho

$$
|x-x_0|<\varepsilon\Longrightarrow f(x)\ge f(x_0).
$$

Với bài có miền $D$, chỉ xét những $x\in D$. Cực tiểu toàn cục so sánh với mọi điểm khả thi, còn cực tiểu địa phương chỉ so sánh trong một lân cận.

**Định lý Fermat.** Nếu $x_0$ là điểm trong của miền xác định, $f$ khả vi tại đó và có cực trị địa phương, thì $f'(x_0)=0$.

Điều kiện điểm trong là thiết yếu. Bài min $x$ trên $[0,1]$ đạt tại 0 nhưng đạo hàm bằng 1. Chiều ngược lại của Fermat cũng sai. Chẳng hạn, $f(x)=x^3$ có đạo hàm bằng không tại 0 nhưng không có cực trị ở đó.

Nếu $f'(x_0)=0$ và $f''(x_0)>0$, với $f$ thuộc $C^2$ gần $x_0$, thì $x_0$ là cực tiểu nghiêm địa phương. Hessian một chiều dương giữ số hạng bậc hai dương với mọi dịch chuyển nhỏ khác không. Nếu $f''(x_0)=0$, phép kiểm này chưa kết luận được, như khi so sánh $x^4$ và $-x^4$.

## 4. Đạo hàm riêng và gradient

Với $f:\mathbb R^n\to\mathbb R$, đạo hàm riêng thứ $i$ giữ các tọa độ khác cố định. Tại $a=(a_1,\ldots,a_n)^T$,

$$
\frac{\partial f}{\partial x_i}(a)
=\lim_{t\to0}\frac{f(a+t e_i)-f(a)}t,
$$

trong đó $e_i$ có tọa độ thứ $i$ bằng 1 và các tọa độ khác bằng 0. Vector $a+t e_i$ chính là $a$ sau khi thay $a_i$ bằng $a_i+t$.

Gom các đạo hàm riêng thành vector cột

$$
\nabla f(x)=\begin{bmatrix}
\partial f/\partial x_1\\
\partial f/\partial x_2\\
\vdots\\
\partial f/\partial x_n
\end{bmatrix}.
$$

Chỉ tồn tại các đạo hàm riêng chưa đủ để bảo đảm khả vi. Khi dùng gradient để xấp xỉ tuyến tính, ta giả sử $f$ khả vi, chẳng hạn $f\in C^1$ gần điểm xét.

::: example Tính riêng từng tọa độ
Cho $f(x,y,z)=x^2+xy+xz$. Khi lấy đạo hàm theo $x$, hai biến còn lại được giữ cố định:

$$
\begin{aligned}
f_x &= 2x+y+z, \\
f_y &= x, \\
f_z &= x.
\end{aligned}
$$

Do đó $\nabla f=(2x+y+z,x,x)^T$.
:::

## 5. Đạo hàm hỗn hợp và Hessian

Đạo hàm riêng bậc hai là đạo hàm của một đạo hàm riêng:

$$
\frac{\partial^2 f}{\partial x_i\partial x_j}
=\frac{\partial}{\partial x_i}
\left(\frac{\partial f}{\partial x_j}\right).
$$

Nếu $f\in C^2$ gần điểm xét thì có thể đổi thứ tự đạo hàm hỗn hợp. Hessian $H=\nabla^2 f$ là ma trận $n\times n$ với phần tử

$$
H_{ij}=\frac{\partial^2 f}{\partial x_i\partial x_j}.
$$

Mỗi hàng ghi đạo hàm của các thành phần gradient theo một tọa độ. Với ví dụ trên,

$$
\nabla^2 f=\begin{bmatrix}2&1&1\\1&0&0\\1&0&0\end{bmatrix}.
$$

Chẳng hạn, $f_{xx}=2$, $f_{yx}=1$ và $f_{zy}=0$. Tính đối xứng của ma trận phù hợp với điều kiện $C^2$.

## 6. Điều kiện cực tiểu nhiều biến

Giả sử $f\in C^2$ gần điểm trong $x_0$.

- Nếu $x_0$ là cực tiểu địa phương thì $\nabla f(x_0)=0$ và $\nabla^2f(x_0)\succeq0$.
- Nếu $\nabla f(x_0)=0$ và $\nabla^2f(x_0)\succ0$ thì $x_0$ là cực tiểu nghiêm địa phương.

Ma trận PSD có thể có hướng độ cong bằng không. Vì thế PSD tại một điểm dừng chưa đủ cho kết luận cực tiểu. Hơn nữa, điều kiện PD tại một điểm chỉ cho kết luận địa phương. Muốn dùng tính lồi để kết luận toàn cục phải kiểm Hessian trên cả miền thích hợp.

## 7. Bài tập kết nối hai buổi

::: exercise Bài toán ba biến
Xét bài toán tìm giá trị nhỏ nhất trên $\mathbb R^3$ của

$$
F(x,y,z)=2x^2+2xy+y^2+xz+2z^2+\cos x.
$$

Trước hết tính gradient và suy ra $y,z$ theo $x$ tại một điểm dừng.
:::

::: solution
Ta có

$$
\nabla F=\begin{bmatrix}
4x+2y+z-\sin x\\2x+2y\\x+4z
\end{bmatrix}.
$$

Hai phương trình cuối cho $y=-x$ và $z=-x/4$. Thay vào phương trình đầu, ta được $\sin x=7x/4$. Đến đây ta đã hoàn thành bước tính đạo hàm và tạo ứng viên. Tuy nhiên, việc chứng nhận tối ưu toàn cục cần kiến thức về tính lồi ở Ôn luyện 2. Lời giải đầy đủ nằm ở [bài toán có cos](./bai-tap-cos.md), sau chủ đề tính lồi.
:::
