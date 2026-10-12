---
course: toan-cho-ai
lecture: bai-08-tai-lieu-on-tap
topic: bai-tap-rang-buoc
section: topic
title: "Bài tập ràng buộc lồi và phi lồi"
description: "Hai bài tập ba biến: Mục tiêu bậc ba trên quả cầu cắt nửa không gian và mục tiêu bình phương với một đẳng thức, kèm lời giải."
---

Hai bài tập cùng có ràng buộc lồi nhưng sức mạnh của KKT khác nhau. Điểm khác biệt nằm ở hàm mục tiêu: Một bài có tổng lập phương, còn bài kia có tổng bình phương.

## 1. Bài tập mục tiêu bậc ba

::: exercise Lập hệ KKT và tìm nghiệm toàn cục
Xét

$$
\begin{aligned}
&\min_x(x_1^3+x_2^3+x_3^3),\\
&x_1^2+x_2^2+x_3^2\le4,\\
&x_1+x_2+x_3\le1.
\end{aligned}
$$

Viết Lagrangian, toàn bộ hệ KKT và xác định giá trị nhỏ nhất.
:::

::: solution
Hai ràng buộc đều là bất đẳng thức. Vì vậy cả $\mu$ lẫn $\lambda$ dưới đây đều không âm:

$$
\begin{aligned}
L&=x_1^3+x_2^3+x_3^3\\
&\quad+\mu(x_1^2+x_2^2+x_3^2-4)\\
&\quad+\lambda(x_1+x_2+x_3-1).
\end{aligned}
$$

Hệ KKT là

$$
\begin{aligned}
3x_i^2+2\mu x_i+\lambda&=0,\\
x_1^2+x_2^2+x_3^2&\le4,\\
x_1+x_2+x_3&\le1,\\
\mu(x_1^2+x_2^2+x_3^2-4)&=0,\\
\lambda(x_1+x_2+x_3-1)&=0,\\
\mu\ge0,\quad\lambda&\ge0.
\end{aligned}
$$

Điều kiện dừng áp dụng với từng $i=1,2,3$, tương ứng lần lượt với $x_1,x_2,x_3$. Mục tiêu không lồi trên toàn $\mathbb R^3$, nên chưa được kết luận tối ưu chỉ từ KKT.

Để tìm cận toàn cục, đặt $q=x_1^2+x_2^2+x_3^2\le4$. Với mỗi $i$, $|x_i|\le\sqrt q$, nên

$$
\begin{aligned}
x_1^3+x_2^3+x_3^3 &\ge -(|x_1|^3+|x_2|^3+|x_3|^3)\\
&\ge -\sqrt q\,(x_1^2+x_2^2+x_3^2)\\
&= -q^{3/2}\\
&\ge -8.
\end{aligned}
$$

Điểm $(-2,0,0)$ khả thi và đạt $-8$. Các hoán vị $(0,-2,0)$, $(0,0,-2)$ cũng đạt. Muốn có đẳng thức trong cận trên, chỉ được có một tọa độ khác không và tọa độ đó phải âm, nên đây là đủ ba nghiệm toàn cục.

Tại $(-2,0,0)$, lấy $\mu=3$, $\lambda=0$. Điều kiện dừng thứ nhất là $12-12=0$, hai điều kiện còn lại cũng thỏa. Ràng buộc quả cầu chặt, còn ràng buộc tổng không chặt.
:::

## 2. Một điểm KKT chưa phải nghiệm tối ưu

Gốc tọa độ thỏa KKT với $\mu=\lambda=0$, vì gradient mục tiêu bằng không và cả hai bất đẳng thức đều thỏa nghiêm. Tuy nhiên, mục tiêu tại gốc là 0, lớn hơn giá trị $-8$ vừa tìm.

Gốc thậm chí không là cực tiểu địa phương. Với $t>0$ đủ nhỏ, điểm $(-t,0,0)$ khả thi và cho mục tiêu $-t^3<0$. Đây là lý do phải phân biệt KKT cần trong bài phi lồi với KKT đủ trong bài lồi.

## 3. Bài tập tổng bình phương

::: exercise Ràng buộc nào chặt tại nghiệm?
Xét

$$
\begin{aligned}
&\min_x(x_1^2+x_2^2+x_3^2),\\
&x_1^2+x_2^2+3x_3\le\frac52,\\
&x_1+x_2+x_3=-2.
\end{aligned}
$$

Tìm nghiệm, giá trị tối ưu và nhân tử KKT.
:::

::: solution
Bắt đầu từ đẳng thức tổng. Bình phương tổng được khống chế bởi ba lần tổng bình phương:

$$
\begin{aligned}
(x_1+x_2+x_3)^2 &\le 3(x_1^2+x_2^2+x_3^2),\\
x_1^2+x_2^2+x_3^2 &\ge \frac43.
\end{aligned}
$$

Cận đạt khi ba tọa độ bằng nhau. Kết hợp tổng bằng $-2$, ứng viên là $x^\star=(-2/3,-2/3,-2/3)$. Kiểm bất đẳng thức:

$$
\begin{aligned}
x_1^{\star2}+x_2^{\star2}+3x_3^\star
&=\frac49+\frac49-2\\
&=-\frac{10}{9}<\frac52.
\end{aligned}
$$

Vậy ứng viên khả thi và đạt cận $4/3$. Vì mục tiêu lồi nghiêm trên miền lồi, nghiệm duy nhất.

Lagrangian là

$$
\begin{aligned}
L&=x_1^2+x_2^2+x_3^2\\
&\quad+\mu(x_1^2+x_2^2+3x_3-5/2)\\
&\quad+\lambda(x_1+x_2+x_3+2).
\end{aligned}
$$

Hệ KKT gồm

$$
\begin{aligned}
2(1+\mu)x_1+\lambda&=0,\\
2(1+\mu)x_2+\lambda&=0,\\
2x_3+3\mu+\lambda&=0,\\
\mu(x_1^2+x_2^2+3x_3-5/2)&=0,\\
\mu&\ge0,
\end{aligned}
$$

cùng hai ràng buộc gốc. Bất đẳng thức không chặt tại nghiệm nên $\mu=0$. Điều kiện dừng cho $\lambda=4/3$. Khác bài bậc ba, nhân tử $\lambda$ ở đây thuộc đẳng thức nên không bị hạn chế dấu.
:::

## 4. Câu hỏi đào sâu

::: exercise Kiểm miền trước khi dùng tính lồi
Vì sao việc hai ràng buộc của bài bậc ba đều lồi không đủ để gọi toàn bộ bài toán là tối ưu lồi?
:::

::: solution
Điều đó bảo đảm miền khả thi lồi. Bài toán tối ưu lồi còn yêu cầu mục tiêu lồi trên miền xét. Hessian của tổng lập phương là ma trận chéo có các phần tử $6x_1,6x_2,6x_3$, có thể âm tại điểm khả thi. Do đó mục tiêu không lồi trên miền này. Hướng dịch chuyển quanh một điểm có tọa độ âm cho thấy độ cong âm ngay trong miền.
:::


