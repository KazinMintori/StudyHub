---
course: toan-cho-ai
lecture: on-luyen
topic: khong-gian-va-ma-tran
section: topic
title: "Không gian Euclid, chuẩn và ma trận đối xứng"
description: "Phương án tối ưu, chuẩn p, hình cầu, điểm trong và biên, ma trận, trị riêng, hàm affine và dạng toàn phương."
---

Các câu “gần nghiệm”, “nằm trong miền” và “độ cong không âm” đều cần một cách diễn đạt toán học cụ thể. Chuẩn xác định khoảng cách, hình cầu xác định lân cận, còn ma trận đối xứng giúp đọc độ cong qua trị riêng.

## 1. Nhắc lại bài toán và sự tồn tại nghiệm

Với $f:\mathbb R^n\to\mathbb R$ và $D\subseteq\mathbb R^n$, xét min $f(x)$ trên $x\in D$. Một phương án tối ưu toàn cục $x^\star$ phải thỏa

$$
\begin{aligned}
&x^\star \in D, \\
f(y) &\ge f(x^\star),\quad\forall y\in D.
\end{aligned}
$$

Phương án tối ưu địa phương chỉ yêu cầu so sánh với các điểm khả thi trong một hình cầu đủ nhỏ quanh nó. Dạng miền thường dùng gồm mọi $x\in\mathbb R^n$ thỏa

$$
\begin{aligned}
f_i(x) &\le 0,\quad i=1,\ldots,m, \\
h_j(x) &= 0,\quad j=1,\ldots,p.
\end{aligned}
$$

Khi $m=p=0$ và hàm xác định trên toàn không gian, đây là bài không ràng buộc trên $\mathbb R^n$.

Ví dụ $f(x)=-1/x$ trên $D=(0,1)$ không có giá trị nhỏ nhất hữu hạn, vì hàm tiến tới $-\infty$ khi $x\to0^+$. Viết lại miền thành $[0,1]$ không tự giải quyết được vấn đề: Biểu thức không xác định tại 0. Muốn dùng định lý hàm liên tục đạt cực trị trên tập compact, phải có cả miền compact lẫn tính liên tục trên toàn miền. Ví dụ này giữ rõ sự khác nhau giữa điều kiện về miền và điều kiện về hàm.

## 2. Chuẩn của vector

Vector $x$ có $n$ tọa độ, viết dưới dạng cột $(x_1,\ldots,x_n)^T$. Chuẩn là một số không âm biểu thị độ lớn và thỏa ba tính chất: Bằng không chỉ tại vector không, đồng nhất theo trị tuyệt đối của hệ số nhân và bất đẳng thức tam giác.

Với $1\le p<\infty$, chuẩn $p$ là

$$
\begin{aligned}
\|x\|_p &= (|x_1|^p+\cdots+|x_n|^p)^{1/p} \\
&= \left(\sum_{i=1}^{n}|x_i|^p\right)^{1/p}.
\end{aligned}
$$

Ba trường hợp cần dùng là

$$
\begin{aligned}
\|x\|_1 &= |x_1|+\cdots+|x_n|, \\
\|x\|_2 &= \sqrt{x_1^2+\cdots+x_n^2}, \\
\|x\|_\infty &= \max\{|x_1|,\ldots,|x_n|\}.
\end{aligned}
$$

Chuẩn vô cùng là tọa độ có trị tuyệt đối lớn nhất. Nó được định nghĩa riêng, không thay số vô cùng vào biểu thức $1/p$. Với $x=(3,-4)$, ba chuẩn trên lần lượt là 7, 5 và 4. Cùng một vector nhưng mỗi chuẩn nhấn mạnh một kiểu độ lớn khác nhau.

<NormBallLab />

Các quả cầu đơn vị của chuẩn 1, chuẩn 2 và chuẩn vô cùng trong mặt phẳng có dạng hình thoi, đĩa tròn và hình vuông. Hình tròn chỉ đặc trưng cho chuẩn Euclid, không phải mọi chuẩn.

## 3. Hình cầu, điểm trong và điểm biên

Với tâm $x$ và bán kính $r>0$, hình cầu mở và đóng là

$$
\begin{aligned}
B(x,r) &= \{y:\|y-x\|<r\}, \\
\overline B(x,r) &= \{y:\|y-x\|\le r\}.
\end{aligned}
$$

Trong một chiều với chuẩn trị tuyệt đối, hình cầu mở là khoảng $(x-r,x+r)$. Khoảng có hai đầu $a<b$ có tâm $c=(a+b)/2$ và bán kính $(b-a)/2$. Trong hai chiều với chuẩn Euclid, đó là đĩa tròn, gồm cả phần diện tích bên trong, không chỉ đường tròn biên.

Điểm $x\in D$ là **điểm trong** nếu một hình cầu mở đủ nhỏ quanh nó nằm trọn trong $D$. Một điểm là **điểm biên** nếu mọi hình cầu mở quanh nó đều chạm cả $D$ lẫn phần bù của $D$. Điểm biên không nhất thiết thuộc $D$: Hai đầu của một khoảng mở là điểm biên nhưng không nằm trong khoảng.

Trong hình miền cong trên bảng, hình cầu ở giữa nằm hoàn toàn trong miền mô tả điểm trong. Hình cầu quanh chỗ tiếp giáp phải cắt ra ngoài mô tả điểm biên. Đây là lý do định lý Fermat cần giả thiết điểm trong.

## 4. Ma trận và đa thức đặc trưng

Một ma trận $A\in\mathbb R^{m\times n}$ có $m$ hàng, $n$ cột và phần tử $a_{ij}$ ở hàng $i$, cột $j$. Chẳng hạn,

$$
A=\begin{bmatrix}
a_{11}&a_{12}&\cdots&a_{1n}\\
a_{21}&a_{22}&\cdots&a_{2n}\\
\vdots&\vdots&&\vdots\\
a_{m1}&a_{m2}&\cdots&a_{mn}
\end{bmatrix}.
$$

Với ma trận vuông đối xứng thực, $A^T=A$. Đa thức đặc trưng theo quy ước của buổi học là

$$
\chi_A(t)=\det(A-tI_n).
$$

Nghiệm của đa thức là các trị riêng của $A$. Với $A$ đối xứng thực, tất cả trị riêng đều thực và có đủ $n$ trị riêng khi tính cả bội. Quy ước $\det(tI-A)$ cũng thông dụng, nhưng khác biểu thức trên bởi hệ số $(-1)^n$. Hai đa thức vẫn có cùng nghiệm.

## 5. Hàm affine

Một hàm vô hướng affine có dạng

$$
\begin{aligned}
\ell(x) &= a_1x_1 + \dots + a_nx_n + b\\
&= a^Tx + b.
\end{aligned}
$$

Nếu $b=0$, đây là ánh xạ tuyến tính. Phân biệt này giúp đọc mô hình hồi quy có hệ số chặn và các ràng buộc đẳng thức của bài toán lồi.

## 6. Dạng toàn phương và hệ số chéo

Với $A$ đối xứng, dạng toàn phương là $Q(x)=x^TAx$. Trong ba chiều, khai triển thành

$$
Q(x) = a_{11}x_1^2 + a_{22}x_2^2 + a_{33}x_3^2 + 2a_{12}x_1x_2 + 2a_{13}x_1x_3 + 2a_{23}x_2x_3.
$$

Hệ số 2 xuất hiện vì cả vị trí $(i,j)$ và $(j,i)$ cùng đóng góp vào tích chéo. Trong $n$ chiều,

$$
Q(x)=\sum_{i=1}^{n}a_{ii}x_i^2+2\sum_{i=1}^{n-1}\sum_{j=i+1}^{n}a_{ij}x_ix_j.
$$

Tổng kép chạy qua các cặp chỉ số $i<j$, tức mỗi cặp khác nhau chỉ được đếm một lần trước khi nhân 2. Dạng ba chiều phía trên đã chỉ rõ từng số hạng của cách viết rút gọn.

## 7. Xác định dương và nửa xác định dương

Với ma trận đối xứng thực:

- $A$ xác định dương, viết $A\succ0$, nếu $x^TAx>0$ với mọi $x\ne0$.
- $A$ nửa xác định dương, viết $A\succeq0$, nếu $x^TAx\ge0$ với mọi $x$.

Nhờ chéo hóa trực giao, tồn tại $U$ trực giao và các trị riêng $\lambda_1,\ldots,\lambda_n$ sao cho $A=U\operatorname{diag}(\lambda_i)U^T$. Đặt $z=U^Tx$, ta có

$$
\begin{aligned}
x^TAx &= \lambda_1z_1^2+\cdots+\lambda_nz_n^2 \\
&= \sum_{i=1}^{n}\lambda_i z_i^2.
\end{aligned}
$$

Vì vậy PD tương đương mọi trị riêng dương, còn PSD tương đương mọi trị riêng không âm. Không dùng riêng dấu từng phần tử hoặc riêng dấu định thức để suy ra kết luận này.

## 8. Bài tập tự luyện

::: exercise Đọc hệ số của dạng toàn phương
Viết ma trận đối xứng $A$ cho $Q(x,y)=2x^2+2xy+y^2$, rồi kiểm tính dương bằng cách hoàn thành bình phương.
:::

::: solution
Ma trận là $A=\begin{bmatrix}2&1\\1&1\end{bmatrix}$. Phần tử ngoài đường chéo là 1 vì hai vị trí cùng tạo hệ số $2xy$. Ta có $Q=(x+y)^2+x^2$, dương với mọi $(x,y)\ne(0,0)$. Do đó $A\succ0$.
:::
