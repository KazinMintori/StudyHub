---
course: toan-cho-ai
lecture: on-luyen
topic: mo-hinh-va-hoi-quy
section: topic
title: "Mô hình tối ưu và hồi quy tuyến tính"
description: "Biến quyết định, miền khả thi, nghiệm tối ưu, học có giám sát, hàm mất mát, hồi quy affine, phép chiếu và phương trình chuẩn."
---

Khi điều chỉnh một mô hình dự đoán, điều gì được thay đổi và điều gì phải giữ cố định? Câu hỏi này phân biệt dữ liệu với biến quyết định. Nếu chưa xác định rõ hai vai trò ấy, ta chưa có một bài toán tối ưu hoàn chỉnh.

## 1. Biến, mục tiêu và ràng buộc

Một quyết định nhiều thành phần được biểu diễn bằng vector cột

$$
x=\begin{bmatrix}x_1\\x_2\\\vdots\\x_n\end{bmatrix}
\in\mathbb R^n.
$$

Cho hàm mục tiêu $f$ và các hàm ràng buộc $f_i$, đều nhận đầu vào trong $\mathbb R^n$ và trả về một số thực. Các ngưỡng $b_1,\ldots,b_m$ là dữ liệu cố định. Bài toán là

$$
\begin{aligned}
&\min_x f(x),\\
&f_i(x)\le b_i,\quad i=1,\ldots,m.
\end{aligned}
$$

Miền khả thi $D$ gồm tất cả các điểm thỏa đồng thời các ràng buộc. Một $x\in D$ là **phương án khả thi**. Điểm $x^\star$ là **phương án tối ưu** nếu

$$
\begin{aligned}
&x^\star \in D,\\
&f(x^\star) \le f(x),\quad\forall x\in D.
\end{aligned}
$$

Giá trị nhỏ nhất khi đạt được là $f_{\min}=f(x^\star)$. Nếu chưa biết có đạt nghiệm hay không, dùng cận dưới đúng $p^\star=\inf_{x\in D}f(x)$. Chẳng hạn, min $x$ trên $x>0$ có cận dưới bằng không nhưng không có điểm khả thi đạt cận ấy.

Trong quy hoạch nguyên, biến phải có tọa độ nguyên, nên miền được thay bằng $D\cap\mathbb Z^n$. Hạn chế này thay đổi những quyết định được phép chọn, không chỉ thay đổi cách tính.

## 2. Học có giám sát và hàm mất mát

Để tránh nhầm miền khả thi với tập dữ liệu, ký hiệu tập dữ liệu bằng $\mathcal D$:

$$
\begin{aligned}
&\mathcal D = \{(x_1,y_1),\ldots,(x_N,y_N)\},\\
&x_i \in \mathbb R^d,\quad y_i\in\mathbb R^k.
\end{aligned}
$$

Mỗi $x_i$ là một đầu vào có $d$ đặc trưng, còn $y_i$ là đầu ra đích có $k$ thành phần. Nhiệm vụ là tìm hàm dự đoán từ $\mathbb R^d$ sang $\mathbb R^k$. Khi chọn một họ mô hình $f_a$, vector tham số $a\in\mathbb R^p$ quyết định mô hình cụ thể.

Hàm mất mát $\ell$ nhận dự đoán và đầu ra đích, rồi đo mức sai lệch. Một lựa chọn là khoảng cách Euclid. Với hai đầu ra $u,v\in\mathbb R^k$,

$$
\begin{aligned}
&\ell(u,v) = \|u-v\|_2,\\
&\ell(u,v)^2 = (u_1-v_1)^2+\cdots+(u_k-v_k)^2.
\end{aligned}
$$

Đặt $\ell_i(a)=\ell(f_a(x_i),y_i)$ là mất mát ở quan sát thứ $i$. Hàm mục tiêu trên tập huấn luyện là trung bình mất mát. Viết trước các số hạng rồi mới dùng ký hiệu tổng:

$$
\begin{aligned}
&L(a,\mathcal D) = \frac{\ell_1(a)+\cdots+\ell_N(a)}{N}\\
&\quad =\frac1N\sum_{i=1}^{N}\ell(f_a(x_i),y_i).
\end{aligned}
$$

Như vậy, huấn luyện là tìm $a$ làm $L$ nhỏ nhất. Dữ liệu và họ mô hình được giữ cố định. Chỉ tham số được điều chỉnh. Ký hiệu $\arg\min_a L$ chỉ tập các tham số đạt giá trị nhỏ nhất, khác với $\min_a L$ là một giá trị số.

## 3. Hồi quy affine với đầu ra vô hướng

Xét $k=1$. Mô hình tuyến tính có hệ số chặn được viết

$$
\begin{aligned}
&a = (a_0,a_1,\ldots,a_d)^T,\\
&f_a(x) = a_0+a_1x_1+\cdots+a_dx_d\\
&\quad =a_0+\sum_{j=1}^{d}a_jx_j.
\end{aligned}
$$

Tên gọi hồi quy tuyến tính nói đến tính tuyến tính theo các hệ số. Khi $a_0\ne0$, ánh xạ theo đầu vào là affine. Nếu muốn viết một tích vô hướng duy nhất, thêm tọa độ 1 vào đầu vào.

Chọn mất mát bình phương $\ell(u,v)=(u-v)^2$. Đặt sai số dự đoán ở quan sát thứ $i$ là $r_i$. Khi đó

$$
\begin{aligned}
&r_i = a_0+\sum_{j=1}^{d}a_jx_{ij}-y_i,\\
&L(a,\mathcal D) = \frac1N\sum_{i=1}^{N}r_i^2.
\end{aligned}
$$

Ở đây $x_{ij}$ là đặc trưng thứ $j$ của quan sát thứ $i$. Mỗi số hạng là bình phương sai số của một quan sát. Tổng bên trong dự đoán đã được khai triển ở công thức mô hình.

## 4. Ma trận thiết kế

Đặt ma trận $X$ có $N$ hàng và $d+1$ cột, hàng thứ $i$ là $(1,x_i^T)$. Khai triển cấu trúc này:

$$
X=\begin{bmatrix}
1&x_{11}&\cdots&x_{1d}\\
1&x_{21}&\cdots&x_{2d}\\
\vdots&\vdots&&\vdots\\
1&x_{N1}&\cdots&x_{Nd}
\end{bmatrix}.
$$

Gom các đầu ra vào $y=(y_1,\ldots,y_N)^T$. Tích ma trận $Xa$ là vector dự đoán, vì hàng thứ $i$ cho

$$
(Xa)_i=a_0+a_1x_{i1}+\cdots+a_dx_{id}.
$$

Đặt phần dư $r=Xa-y$. Từ định nghĩa chuẩn Euclid,

$$
\begin{aligned}
&L(a,\mathcal D) = \frac{r_1^2+\cdots+r_N^2}{N}\\
&\quad =\frac1N\sum_{i=1}^{N}r_i^2\\
&\quad =\frac1N\|Xa-y\|_2^2.
\end{aligned}
$$

Vì bình phương là hàm tăng trên các số không âm và $N>0$, cực tiểu hóa $L$ tương đương cực tiểu hóa $\|Xa-y\|_2$. Hai bài có cùng tập nghiệm, nhưng giá trị mục tiêu khác nhau.

## 5. Phép chiếu và phương trình chuẩn

Mọi vector dự đoán có dạng $Xa$, nên nằm trong không gian cột $W=\operatorname{Col}(X)$. Viết các cột là $X_0,\ldots,X_d$ thì

$$
Xa=a_0X_0+a_1X_1+\cdots+a_dX_d.
$$

Bài toán tìm điểm $\widehat y\in W$ gần $y$ nhất. Hình học của nghiệm là phép chiếu trực giao

$$
\widehat y=\operatorname{proj}_{W}(y).
$$

Vector từ dự đoán tới dữ liệu vuông góc với $W$. Vì thế $X^T(y-Xa)=0$, tương đương **phương trình chuẩn**

$$
X^TXa=X^Ty.
$$

Cũng có thể tính gradient của $L$:

$$
\nabla_a L=\frac2N X^T(Xa-y).
$$

Hessian là $2X^TX/N$, luôn nửa xác định dương. Do đó phương trình chuẩn đủ để chứng nhận tối ưu. Nếu $X$ có hạng cột đầy đủ thì $X^TX$ khả nghịch và hệ số tối ưu duy nhất. Nếu các cột phụ thuộc, dự đoán tối ưu vẫn duy nhất nhưng hệ số có thể không duy nhất. Trong tính toán số, có thể dùng QR hoặc SVD để giải bình phương tối thiểu, tránh hình thành nghịch đảo một cách trực tiếp.

::: example Mở từng bước của một hồi quy nhỏ
Lấy ba quan sát $(0,1)$, $(1,2)$ và $(2,2)$, dùng mô hình $a_0+a_1x$. Đây là ví dụ bổ sung để đọc được phương trình chuẩn.

$$
\begin{aligned}
&X = \begin{bmatrix}1&0\\&1 1\\&1 2\end{bmatrix},\\
&y = \begin{bmatrix}1\\&2\\&2\end{bmatrix},\\
&X^TX = \begin{bmatrix}3&3\\&3 5\end{bmatrix},\\
&X^Ty = \begin{bmatrix}5\\&6\end{bmatrix}.
\end{aligned}
$$

Giải hệ được $a_0=7/6$, $a_1=1/2$. Phần dư là $(1/6,-1/3,1/6)^T$. Tổng phần dư bằng không và tích vô hướng với cột đặc trưng cũng bằng không. Mất mát trung bình là $1/18$.
:::

## 6. Câu hỏi ôn lại

::: exercise Không gian dự đoán và hệ số
Nếu hai cột của $X$ giống nhau, vì sao không thể kết luận hệ số hồi quy duy nhất? Dự đoán tối ưu có còn duy nhất không?
:::

::: solution
Nếu hai cột giống nhau, tăng một hệ số một lượng $t$ rồi giảm hệ số kia cùng lượng ấy không thay đổi $Xa$. Vì thế có thể có nhiều hệ số cho cùng dự đoán. Tuy nhiên, phép chiếu trực giao lên không gian con $W$ là duy nhất, nên vector dự đoán tối ưu vẫn duy nhất.
:::

Đọc tiếp [quy hoạch tuyến tính](./quy-hoach-tuyen-tinh.md) để thấy một kiểu hình học tối ưu khác: Nghiệm xuất hiện tại biên của miền khả thi.


