---
course: toan-cho-ai
lecture: on-luyen
topic: dieu-kien-kkt
section: topic
title: "Lagrangian và điều kiện KKT"
description: "Lagrangian, ràng buộc chặt, LICQ, bốn nhóm điều kiện KKT, điều kiện cần và điều kiện đủ trong bài toán lồi."
---

Ở nghiệm nằm trên biên, gradient mục tiêu thường không bằng không. Ta không thể đi theo mọi hướng vì một số hướng rời miền khả thi. Điều kiện KKT mô tả cách các gradient ràng buộc cân bằng gradient mục tiêu tại nghiệm.

## 1. Chuẩn hóa bài toán và dấu nhân tử

Xét bài toán khả vi

$$
\begin{aligned}
&\min_x f(x),\\
&f_i(x)\le0,\quad i=1,\ldots,m,\\
&h_j(x)=0,\quad j=1,\ldots,p.
\end{aligned}
$$

Đưa mọi bất đẳng thức về dấu $\le0$ trước khi lập Lagrangian. Ví dụ, $x_i\ge0$ được viết thành $-x_i\le0$. Nếu không thống nhất dấu từ đầu, dấu nhân tử và điều kiện dừng sẽ bị đảo.

Lagrangian bổ sung các ràng buộc vào mục tiêu với trọng số:

$$
\begin{aligned}
L(x,\mu,\lambda)&=f(x)+\mu_1f_1(x)+\cdots+\mu_mf_m(x)+\lambda_1h_1(x)+\cdots+\lambda_ph_p(x)\\
&=f(x)+\sum_{i=1}^{m}\mu_i f_i(x)+\sum_{j=1}^{p}\lambda_j h_j(x).
\end{aligned}
$$

Nhân tử bất đẳng thức phải thỏa $\mu_i\ge0$. Nhân tử đẳng thức $\lambda_j$ là số thực tự do. Tại một điểm khả thi, mọi số hạng $\mu_i f_i(x)$ không dương và các số hạng đẳng thức bằng không. Đây cũng là cơ sở của cận dưới đối ngẫu.

## 2. Ràng buộc chặt và điều kiện không suy biến

Một ràng buộc bất đẳng thức **chặt** tại $x$ nếu $f_i(x)=0$. Đặt

$$
J(x)=\{i\in\{1,\ldots,m\}:f_i(x)=0\}.
$$

Điều kiện độc lập tuyến tính của các gradient ràng buộc, gọi tắt là **LICQ**, yêu cầu họ vector

$$
\begin{gathered}
\nabla h_1(x),\ldots,\nabla h_p(x),\\
\{\nabla f_i(x):i\in J(x)\}
\end{gathered}
$$

độc lập tuyến tính. Độc lập nghĩa là chỉ tổ hợp tuyến tính với mọi hệ số bằng không mới cho vector không.

LICQ là một điều kiện đủ về độ chính quy để suy ra KKT tại cực tiểu địa phương. Nó không phải điều kiện cần cho bản thân sự tồn tại nghiệm tối ưu. Nếu LICQ không thỏa, nghiệm vẫn có thể tồn tại và đôi khi vẫn thỏa KKT.

## 3. Bốn nhóm điều kiện KKT

Nếu $x^\star$ là cực tiểu địa phương và LICQ thỏa tại đó, tồn tại $\mu,\lambda$ sao cho bốn nhóm sau cùng đúng.

**Điều kiện dừng.** Gradient theo biến gốc của Lagrangian bằng không:

$$
\begin{aligned}
0&=\nabla_x L(x^\star,\mu,\lambda)\\
&=\nabla f(x^\star)\\
&\quad+\sum_{i=1}^{m}\mu_i\nabla f_i(x^\star)\\
&\quad+\sum_{j=1}^{p}\lambda_j\nabla h_j(x^\star).
\end{aligned}
$$

Các tổng ở đây là tổng có trọng số của từng gradient, cùng cấu trúc đã khai triển trong Lagrangian. Với hai bất đẳng thức và một đẳng thức, chúng là $\mu_1\nabla f_1+\mu_2\nabla f_2+\lambda_1\nabla h_1$.

**Khả thi gốc.** Điểm xét phải thỏa mọi $f_i(x^\star)\le0$ và $h_j(x^\star)=0$.

**Khả thi đối ngẫu.** Mọi $\mu_i\ge0$. Không đặt điều kiện dấu lên $\lambda_j$.

**Bù trừ.** Với từng $i=1,\ldots,m$,

$$
\mu_i f_i(x^\star)=0.
$$

Nếu ràng buộc không chặt thì $f_i(x^\star)<0$, buộc $\mu_i=0$. Chiều ngược lại không đúng: Một ràng buộc chặt có thể có nhân tử bằng không. Chính điều này xảy ra tại ngưỡng $r=2$ trong [bài KKT theo tham số](./kkt-co-tham-so.md).

## 4. Khi nào KKT đủ?

Giả sử mục tiêu $f$ và các $f_i$ lồi, các $h_j$ affine, mọi hàm khả vi trên miền mở lồi chung. Bất kỳ bộ $(x^\star,\mu,\lambda)$ thỏa KKT đều chứng nhận $x^\star$ là nghiệm tối ưu toàn cục.

::: proof Từ điều kiện dừng đến cận dưới
Với $\mu\ge0$, Lagrangian là hàm lồi theo $x$: Nó là tổng hàm lồi với các hệ số không âm và các hàm affine. Điều kiện dừng cho biết $x^\star$ cực tiểu hóa Lagrangian trên miền chung.

Cho $y$ khả thi bất kỳ. Ta có

$$
\begin{aligned}
f(y)&\ge L(y,\mu,\lambda)\\
&\ge L(x^\star,\mu,\lambda)\\
&=f(x^\star).
\end{aligned}
$$

Dòng cuối dùng khả thi gốc và bù trừ. Vì $y$ tùy ý, kết luận là toàn cục.
:::

Tính đủ này không cần LICQ. Vai trò của LICQ ở phần trước là giúp suy ra sự tồn tại nhân tử từ một cực tiểu địa phương. Trong bài toán phi lồi, bốn nhóm KKT nói chung chỉ là bộ điều kiện cần dưới giả thiết chính quy, chưa đủ cho tối ưu.

## 5. Bài tập tự luyện

::: exercise Nhân tử nào phải bằng không?
Một ứng viên có $f_1(x)<0$, $f_2(x)=0$ và $h_1(x)=0$. Từ bù trừ suy ra được điều gì về $\mu_1$, $\mu_2$ và $\lambda_1$?
:::

::: solution
Phải có $\mu_1=0$. Nhân tử $\mu_2$ có thể bằng không hoặc dương, nhưng phải không âm. Nhân tử $\lambda_1$ không bị hạn chế dấu. Những giá trị cụ thể còn phải được xác định bằng điều kiện dừng.
:::
