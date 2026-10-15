---
course: toan-cho-ai
lecture: on-luyen
topic: kkt-co-tham-so
section: topic
title: "Giải KKT theo tham số và tập ràng buộc chặt"
description: "Giải trọn bài toán ba biến không âm có tổng bằng r, xét các trường hợp bù trừ, ngưỡng r=2 và nhân tử Lagrange."
---

Khi một biến phải trả thêm chi phí tuyến tính, ta có nên phân bổ nguồn lực vào biến ấy ngay từ đầu không? Bài toán sau cho một câu trả lời có ngưỡng rõ ràng.

## 1. Đề bài

Cho $r>0$ cố định. Tìm

$$
\begin{aligned}
&\min_{x_1,x_2,x_3}P(x),\\
&P(x) = x_3+\frac12(x_1^2+x_2^2+x_3^2),\\
&x_1+x_2+x_3=r,\\
&x_1,x_2,x_3\ge0.
\end{aligned}
$$

Ba số hạng bình phương phạt phân bổ quá lớn vào một tọa độ. Riêng tọa độ thứ ba còn trả thêm chi phí $x_3$. Mục tiêu có Hessian $I_3$, nên lồi nghiêm. Miền khả thi là một đơn hình đóng, bị chặn và khác rỗng. Vì thế nghiệm tồn tại và duy nhất.

## 2. Lagrangian và hệ KKT

Viết các bất đẳng thức thành $-x_i\le0$. Lagrangian là

$$
L = x_3 + \frac{1}{2}(x_1^2 + x_2^2 + x_3^2) - \mu_1x_1 - \mu_2x_2 - \mu_3x_3 + \lambda(x_1 + x_2 + x_3 - r).
$$

Hệ KKT gồm

$$
\begin{aligned}
x_1-\mu_1+\lambda &= 0, \\
x_2-\mu_2+\lambda &= 0, \\
1+x_3-\mu_3+\lambda &= 0, \\
\mu_1x_1 &= \mu_2x_2=\mu_3x_3 = 0, \\
x_1+x_2+x_3 &= r, \\
x_i &\ge 0,\quad\mu_i \ge 0.
\end{aligned}
$$

Chỉ số ở dòng cuối chạy từ 1 đến 3. Ta giải hệ bằng cách xét tọa độ nào bằng không, rồi kiểm dấu nhân tử.

## 3. Các trường hợp bị loại

Không thể có cả ba tọa độ bằng không vì tổng bằng $r>0$.

Nếu chỉ $x_1>0$, ta có $x_1=r$ và $\mu_1=0$, nên $\lambda=-r$. Phương trình thứ hai cho $\mu_2=-r<0$, trái dấu yêu cầu. Trường hợp chỉ $x_2>0$ bị loại tương tự. Nếu chỉ $x_3>0$, phương trình thứ ba cho $\lambda=-1-r$, dẫn tới $\mu_1=\lambda<0$.

Nếu $x_1,x_3>0$ nhưng $x_2=0$, bù trừ cho $\mu_1=\mu_3=0$. Khi đó $\lambda=-x_1<0$ và $\mu_2=\lambda<0$. Trường hợp $x_2,x_3>0$ bị loại tương tự. Như vậy chỉ còn hai khả năng: Hai tọa độ đầu dương, tọa độ thứ ba bằng không, hoặc cả ba dương.

## 4. Nhánh thứ nhất: Tọa độ thứ ba bằng không

Cho $x_1,x_2>0$ và $x_3=0$. Bù trừ cho $\mu_1=\mu_2=0$. Từ điều kiện dừng và tổng nguồn lực,

$$
\begin{aligned}
x_1 &= x_2 = -\lambda, \\
x_1+x_2 &= r, \\
x_1 &= x_2 = \frac r2, \\
\lambda &= -\frac r2, \\
\mu_3 &= 1+\lambda=\frac{2-r}{2}.
\end{aligned}
$$

Điều kiện $\mu_3\ge0$ tương đương $0<r\le2$. Vì bài toán lồi, bộ KKT này chứng nhận

$$
\begin{aligned}
x^\star &= (r/2,r/2,0), \\
\mu_1 &= \mu_2 = 0, \\
\mu_3 &= (2-r)/2, \\
\lambda &= -r/2.
\end{aligned}
$$

Ở ngưỡng $r=2$, ràng buộc $x_3\ge0$ vẫn chặt nhưng nhân tử $\mu_3=0$. Đây là ví dụ trực tiếp bác bỏ suy luận “ràng buộc chặt thì nhân tử dương”.

## 5. Nhánh thứ hai: Cả ba tọa độ dương

Bù trừ cho $\mu_1=\mu_2=\mu_3=0$. Khi đó

$$
\begin{aligned}
x_1 &= x_2 = -\lambda, \\
x_3 &= -1-\lambda, \\
-3\lambda-1 &= r, \\
\lambda &= -\frac{r+1}{3}.
\end{aligned}
$$

Suy ra

$$
\begin{aligned}
x_1 &= x_2 = \frac{r+1}{3}, \\
x_3 &= \frac{r-2}{3}.
\end{aligned}
$$

Nhánh này có cả ba tọa độ dương khi $r>2$. Công thức vẫn đúng ở $r=2$ và khớp nhánh trước. Các nhân tử là $(0,0,0,-(r+1)/3)$.

::: info Kiểm tra mẫu số của nhân tử
Lưu ý: Thay vào phương trình dừng và ràng buộc đẳng thức $x_1+x_2+x_3=r$ cho ta $-3\lambda-1=r$, suy ra nhân tử đúng là $\lambda=-(r+1)/3$ với mẫu số 3 (tránh nhầm với mẫu số 2 trong các phép tính nháp trung gian).
:::

## 6. Giá trị tối ưu và ý nghĩa của ngưỡng

Thay nghiệm vào mục tiêu, với $0<r\le2$ ta được

$$
P^\star(r)=\frac{r^2}{4}.
$$

Với $r\ge2$, giá trị tối ưu là

$$
P^\star(r)=\frac{r^2+2r-2}{6}.
$$

Khi nguồn lực ít, chi phí tăng thêm của tọa độ thứ ba khiến nó chưa được sử dụng. Hai tọa độ đầu chia đều nguồn lực. Khi nguồn lực tăng tới ngưỡng, chi phí cận biên của hai tọa độ đầu đạt mức đủ cao để tọa độ thứ ba bắt đầu tham gia. Sau ngưỡng, lượng tăng thêm được chia đều cho cả ba tọa độ.

## 7. Bài tập tự luyện

::: exercise Kiểm chứng tại hai giá trị tham số
Tính nghiệm và các nhân tử khi $r=1$ và $r=3$. Kiểm tra đủ bốn nhóm KKT.
:::

::: solution
Với $r=1$, nghiệm là $(1/2,1/2,0)$, các nhân tử bất đẳng thức là $(0,0,1/2)$ và $\lambda=-1/2$. Giá trị mục tiêu là $1/4$.

Với $r=3$, nghiệm là $(4/3,4/3,1/3)$, các nhân tử bất đẳng thức bằng không và $\lambda=-4/3$. Giá trị mục tiêu là $13/6$. Trong cả hai trường hợp, tổng tọa độ đúng bằng $r$, các tích bù trừ bằng không và ba phương trình dừng đều thỏa.
:::
