---
course: toan-cho-ai
lecture: bai-02-tap-loi
section: lecture
title: "Các bài toán tối ưu lồi"
prerequisites: ["tap-loi", "ham-loi", "chuan", "ma-tran-psd"]
lessonStatus: ready
description: "Nhận diện các dạng tối ưu lồi, cải dạng tương đương và phân biệt xấp xỉ với nới lỏng."
---

Ta đã có định nghĩa tập lồi và hàm lồi. Bước tiếp theo là nhận ra cấu trúc ấy trong một bài toán được viết bằng công thức. Cách đặt dấu bất đẳng thức, dạng của hàm mục tiêu và phép đổi biến đều có thể làm tính lồi hiện ra rõ ràng hoặc bị che khuất. Vì vậy, bài này tập trung vào cách đọc và cải dạng mô hình trước khi chọn thuật toán giải.

Sau khi học xong, bạn sẽ xác định được một mô hình có ở dạng chuẩn lồi hay không, nhận diện được LP, QP, SOCP và SDP, giải thích được vai trò của biến phụ, và phân biệt nghiệm của bài toán nới lỏng với nghiệm hợp lệ của bài toán ban đầu.

Ở lần đọc đầu, hãy học mục 1–2 để nắm dạng chuẩn, LP và QP. Sau đó đọc mục 3 về biến phụ. Mục 4 giới thiệu các bài toán trên nón và có thể để lại cho lượt đọc sau. Mục 5 cần đọc trước khi dùng một bài toán gần đúng hoặc bài toán nới lỏng để suy luận về bài toán ban đầu. Kiến thức về tập lồi nằm ở [Bài 01](./bai-01-nhap-mon-toi-uu.md). Phần hình học sâu hơn được đặt trong [bài đọc thêm](../doc-them/hinh-hoc-tap-loi.md).

## 1. Dạng chuẩn của bài toán tối ưu lồi

Theo *Convex Optimization*, dạng chuẩn là

$$\begin{aligned}\text{minimize}\quad &f_0(x)\\
\text{subject to}\quad &f_i(x)\le0,\quad i=1,\ldots,m,\\&Ax=b,
\end{aligned}$$

với $f_0,f_i$ lồi, và các đẳng thức affine. Miền chung của các hàm cũng được xét. **Affine** nghĩa là dạng $a^Tx+b$. Đẳng thức có thể chuyển hằng số sang vế phải.

Để nhận diện dạng chuẩn, lần lượt xét ba câu hỏi. Hàm mục tiêu có lồi không? Mỗi hàm ở vế trái của dấu $\le0$ có lồi không? Các ràng buộc đẳng thức có affine không? Khi cả ba điều kiện được thỏa mãn, miền khả thi là giao của các tập mức dưới lồi và các tập affine, nên cũng là một tập lồi.

Đừng chỉ nhìn tên hàm. Ràng buộc $x^2\le1$ mô tả đoạn $[-1,1]$ và đúng dạng lồi. Ràng buộc $x^2\ge1$ đổi thành $1-x^2\le0$: vế trái lõm, miền gồm hai đoạn rời nhau. Ràng buộc $x^2=1$ là đẳng thức phi affine và cho hai điểm rời nhau.

### 1.1 Miền lồi chưa đủ để biểu thức ở dạng chuẩn

Ràng buộc $x^3\le0$ tương đương $x\le0$, một miền lồi. Nhưng $x^3$ không lồi trên toàn $\mathbb R$, nên biểu thức ban đầu chưa chứng nhận dạng chuẩn. Cải dạng về $x\le0$ mới làm cấu trúc hiện rõ. Ta không gọi biểu thức ban đầu là chuẩn chỉ vì miền cuối cùng lồi.

<details><summary>Thử trả lời: Bài toán $\min -\log x$ với $x\ge 1$ có phải là bài toán lồi không?</summary>

Có. $-\log x$ lồi trên $x>0$, ràng buộc là $1-x\le0$ affine. Tuy nhiên mục tiêu đi tới $-\infty$ khi $x\to\infty$, nên không có nghiệm tối ưu hữu hạn. “Lồi” không bảo đảm bài toán có nghiệm.

</details>

## 2. Quy hoạch tuyến tính và quy hoạch toàn phương

**Quy hoạch tuyến tính (LP)** có mục tiêu và ràng buộc affine:

$$\min c^Tx+d\quad\text{sao cho }Gx\preceq h,\ Ax=b.$$

Hằng số $d$ không đổi nghiệm. Nó vẫn đổi giá trị tối ưu. Ký hiệu vector $\preceq$ ở đây là bất đẳng thức từng thành phần.

**Quy hoạch toàn phương (QP)** cho mục tiêu

$$\frac12x^TPx+q^Tx+r,\qquad P=P^T\succeq0,$$

và ràng buộc affine. $P$ PSD là điều kiện cho QP lồi. Nếu ràng buộc bất đẳng thức cũng là các hàm toàn phương lồi, ta có QCQP, không còn là QP theo định nghĩa này.

::: example Thêm một giới hạn vào bài toán hồi quy
Từ Bài 00, $f(w)=7w^2-11w+\frac{9}{2}$, nên trong dạng QP $P=14$, $q=-11$, $r=\frac{9}{2}$. Thêm $w\le1/2$ cho QP lồi.

Nghiệm không ràng buộc $\frac{11}{14}$ vượt quá giới hạn. Trên miền $w\le1/2$, đạo hàm thỏa $14w-11\le-4<0$, nên hàm mục tiêu giảm khi $w$ tăng cho tới điểm biên. Vì vậy nghiệm là $w^*=\frac{1}{2}$ và $p^*=\frac{3}{4}$.

Đây là nghiệm tại biên với gradient khác 0. Bài 03 sẽ chứng nhận nó bằng nhân tử Lagrange.
:::

### 2.1 Điều chuẩn vẫn có thể giữ tính lồi

Ridge dùng $\tfrac12\|Aw-b\|_2^2+\tfrac\rho2\|w\|_2^2$, $\rho\ge0$. Hessian là $A^TA+\rho I$. Nếu $\rho>0$, với mọi $d\ne0$,

$$d^T(A^TA+\rho I)d=\|Ad\|_2^2+\rho\|d\|_2^2>0.$$

Trong bài không ràng buộc này, mục tiêu toàn phương PD có nghiệm duy nhất. Lasso dùng chuẩn 1 thay chuẩn 2 bình phương. Vẫn lồi nhưng có thể không khả vi. “Không trơn” và “không lồi” là hai thuộc tính khác nhau.

## 3. Cải dạng bài toán bằng biến phụ

Với $m$ hàm $f_1,\ldots,f_m$, mục tiêu lấy giá trị lớn nhất là $\max\{f_1(x),\ldots,f_m(x)\}$, thường viết gọn $\max_{1\le i\le m}f_i(x)$ hoặc $\max_i f_i(x)$ khi phạm vi đã rõ. Xét bài $\min_x\max_i f_i(x)$. Thêm biến $t$:

$$\min_{x,t}t\quad\text{sao cho }f_i(x)\le t\ \forall i.$$

Với một $x$, mọi $t$ khả thi đều không nhỏ hơn $\max_i f_i(x)$, và chọn $t$ đúng bằng giá trị lớn nhất ấy luôn khả thi. Vì vậy tối ưu theo $t$ trả lại đúng mục tiêu cũ. Đây là **cải dạng tương đương**, không chỉ là hai công thức trông gần giống nhau. Nếu các $f_i$ lồi, các hàm $f_i(x)-t$ cũng lồi.

::: example Khớp dữ liệu theo sai số tệ nhất
$\min_w\|Aw-b\|_\infty$ tương đương

$$\min_{w,t}t,\qquad -t\mathbf1\preceq Aw-b\preceq t\mathbf1.$$

$\mathbf1$ là vector có mọi thành phần bằng 1. Hai bất đẳng thức áp dụng cho mỗi phần dư $r_i$ cho $-t\le r_i\le t$, tương đương $|r_i|\le t$. Các ràng buộc mới đều affine, nên bài toán sau cải dạng là một LP dù biểu thức ban đầu chứa chuẩn và phép lấy giá trị lớn nhất.
:::

Với $m$ phần dư, chuẩn 1 là $|r_1|+\cdots+|r_m|$. Thêm $u_i$ sao cho $-u_i\le r_i\le u_i$, rồi cực tiểu $u_1+\cdots+u_m=\sum_{i=1}^m u_i$. Chỉ số $i$ chạy qua các phần dư. Tại tối ưu, có thể lấy $u_i=|r_i|$. Không cần thêm $u_i\ge0$: hai bất đẳng thức đã suy ra điều đó.

Để chứng minh hai cách viết tương đương, cần chỉ ra đủ hai chiều: từ một nghiệm khả thi của bài toán cũ, tạo được biến phụ hợp lệ. Và từ một nghiệm khả thi của bài toán mới, thu hồi được đối tượng ban đầu với cùng giá trị mục tiêu. Nếu thiếu một chiều, phép biến đổi có thể chỉ là một phép nới lỏng.

## 4. Các bài toán tối ưu trên nón

### 4.1 SOCP: chuẩn ở một vế, affine ở vế còn lại

**Nón bậc hai** là $K=\{(u,t):\|u\|_2\le t\}$. Quy hoạch nón bậc hai (SOCP) có mục tiêu affine và các ràng buộc

$$\|A_ix+b_i\|_2\le c_i^Tx+d_i,$$

cùng đẳng thức affine. Ràng buộc đã ép vế phải không âm. Không bình phương hai vế tùy ý nếu chưa giữ điều kiện đó: $|x|\le-1$ vô nghiệm nhưng $x^2\le1$ có nghiệm.

Minimize $\|Aw-b\|_2$ có thể viết $\min t$ với $\|Aw-b\|_2\le t$, một SOCP. Minimize bình phương chuẩn cũng có cùng nghiệm, vì bình phương tăng trên $[0,\infty)$, nhưng giá trị tối ưu không giống nhau.

### 4.2 SDP: điểm trong miền là một ma trận

Cho các ma trận đối xứng cùng kích thước $F_0,F_1,\ldots,F_n$ và vector biến $x=(x_1,\ldots,x_n)$. Khi đó

$$
\begin{aligned}
F(x)&=F_0+x_1F_1+\cdots+x_nF_n\\
&=F_0+\sum_{i=1}^n x_iF_i.
\end{aligned}
$$

Mỗi số $x_i$ nhân với một ma trận cố định $F_i$. Dấu $+$ cộng các ma trận theo từng phần tử. Điều kiện $F(x)\succeq0$ là một **bất đẳng thức ma trận tuyến tính**. Miền lồi vì nón PSD lồi và $F$ affine. **SDP** cực tiểu mục tiêu affine với các ràng buộc loại này và đẳng thức affine.

Ví dụ tự đặt $\begin{bmatrix}t&x\\x&1\end{bmatrix}\succeq0$ tương đương $t\ge x^2$. Ta thấy một epigraph toàn phương có thể được viết bằng ma trận. Đây là so dạng toàn phương, không phải bắt từng phần tử ma trận không âm.

### 4.3 GP: đổi biến trước khi gọi là lồi

Trong quy hoạch hình học, biến $x_i>0$. Một **monomial** là tích có dạng

$$
c\,x_1^{a_1}x_2^{a_2}\cdots x_n^{a_n}
=c\prod_{i=1}^n x_i^{a_i},\qquad c>0.
$$

$\prod$ yêu cầu **nhân**, với $i$ chạy từ 1 đến $n$. Các số mũ $a_i$ là số thực. Với hai biến, tích chỉ là $c\,x_1^{a_1}x_2^{a_2}$. **Posynomial** là tổng hữu hạn các monomial, chẳng hạn $x_1+2x_2^2$. GP dùng posynomial $\le1$, monomial $=1$ và mục tiêu posynomial.

Đặt $y_i=\log x_i$, tức $x_i=e^{y_i}$. Log monomial trở thành $\log c+a_1y_1+\cdots+a_ny_n=\log c+\sum_{i=1}^n a_i y_i$, một hàm affine. Với posynomial gồm $K$ monomial, $\sum_{k=1}^K c_k\prod_{i=1}^n x_i^{a_{ki}}$, chỉ số $k$ chọn monomial và chỉ số $i$ chọn biến. Log của nó trở thành

$$\log\left[\sum_{k=1}^K\exp\left(\log c_k+\sum_{i=1}^n a_{ki}y_i\right)\right].$$

Với hai số hạng, hàm nền $h(z)=\log\sum_k e^{z_k}$ nghĩa là $h(z)=\log(e^{z_1}+e^{z_2})$. Trong trường hợp $K$ số hạng, tổng chạy qua $k=1,\ldots,K$.

Đây là **log-sum-exp** của các biểu thức affine. Để thấy vì sao hàm nền $h(z)=\log\sum_k e^{z_k}$ lồi, đặt $p_k=e^{z_k}/\sum_j e^{z_j}$. Các $p_k$ không âm, cộng thành 1. Hessian là $\operatorname{diag}(p)-pp^T$, nên với mọi hướng $v$,

$$v^T\nabla^2h\,v=\sum_kp_kv_k^2-\left(\sum_kp_kv_k\right)^2
=\sum_kp_k(v_k-\bar v)^2\ge0,\qquad\bar v=\sum_kp_kv_k.$$

Viết thành tổng bình phương có trọng số chứng nhận PSD. Hợp với biểu thức affine giữ tính lồi theo quy tắc ở Bài 01. Lấy log các vế dương giữ chiều bất đẳng thức và giữ thứ tự mục tiêu. Vì vậy GP được giải bằng một bài lồi trong biến $y$. Không khẳng định mọi posynomial lồi trong biến $x$.

<details><summary>Thử trả lời: Sau phép đổi biến log, ràng buộc $x\cdot y\le 1$ với x,$y>0$ trở thành gì?</summary>

Đặt $u=\log x$, $v=\log y$, ta được $u+v\le0$. Ví dụ này là ràng buộc monomial. $xy$ không lồi đồng thời theo $x,y$ trên miền dương nhưng cải dạng log là affine.

</details>

## 5. Cải dạng tương đương, xấp xỉ và nới lỏng

**Xấp xỉ** thay một đối tượng bằng đối tượng khác dễ tính hơn, chẳng hạn thay một hàm bằng khai triển tuyến tính quanh một điểm. Khi dùng xấp xỉ, phải nói rõ hai đối tượng gần nhau ở đâu và sai số được đo bằng đại lượng nào. Chỉ gọi một biểu thức là “xấp xỉ” chưa đủ để suy ra nó là cận trên hay cận dưới.

**Nới lỏng** mở rộng miền: $C\subseteq\widetilde C$. Giữ cùng mục tiêu trong bài min, ta có

$$\inf_{x\in\widetilde C}f(x)\le\inf_{x\in C}f(x).$$

Đây là cận dưới. Nghiệm ở miền rộng có thể không thỏa ràng buộc cũ. Trong bài max, chiều cận đổi.

::: example Biến nhị phân được nới thành một đoạn
Bài gốc $\min(x-0.4)^2$ với $x\in\{0,1\}$ đạt ở 0, giá trị $0.16$. Nới thành $0\le x\le1$ cho nghiệm $0.4$, giá trị 0. Cận 0 hợp lệ, nhưng $0.4$ không phải quyết định khả thi của bài nhị phân.

Làm tròn về 0 cho một ứng viên gốc có giá trị $0.16$. Cận và ứng viên cung cấp khoảng $[0,0.16]$ cho giá trị tối ưu. Không được gọi nghiệm nới lỏng là nghiệm gốc.
:::

Muốn đánh giá một nghiệm, cần xem riêng phần dư của các đẳng thức, mức vi phạm của các bất đẳng thức, giá trị hàm mục tiêu và chứng nhận tối ưu. Một điểm cho giá trị hàm mục tiêu nhỏ nhưng vi phạm ràng buộc vẫn không phải nghiệm hợp lệ của mô hình.

## Bài tập tự luyện

::: exercise 1. Nhận dạng
$\min x^2+y^2$ với $x+y=1$, $x,y\ge0$ là LP, QP hay SOCP trong cách viết hiện tại?
:::
::: solution
QP: mục tiêu toàn phương với $P=2I\succ0$, ràng buộc affine. Có thể cải dạng khác nhưng cách viết hiện tại không phải LP vì mục tiêu không affine.
:::

::: exercise 2. Cải dạng trị tuyệt đối
Viết $\min_x |x-1|+2|x+1|$ thành LP và giải bằng cách chia ba miền $x\le-1$, $-1\le x\le1$, $x\ge1$.
:::
::: solution
Minimize $u+2v$ với $u\ge x-1$, $u\ge1-x$, $v\ge x+1$, $v\ge-x-1$. Trên ba miền, mục tiêu lần lượt là $-3x-1$, $x+3$, $3x+1$. Nó giảm tới $-1$, rồi tăng. Nghiệm $x=-1$ cho giá trị 2. Các biến phụ tối ưu là $u=2$, $v=0$.
:::

::: exercise 3. Xác định chiều của cận
Bỏ ràng buộc $x\le1/2$ khỏi QP ở mục 2. Cận dưới mới và một cận trên khả thi của bài có ràng buộc là bao nhiêu?
:::
::: solution
Nghiệm không ràng buộc cho cận dưới $\frac{5}{28}$. Chọn $w=\frac{1}{2}$ khả thi cho cận trên $\frac{3}{4}$. Khoảng cách là $\frac{3}{4}-\frac{5}{28}=\frac{4}{7}$. Để chứng nhận cận trên chính là tối ưu, dùng lập luận đơn điệu ở mục 2 hoặc KKT ở bài tiếp theo.
:::

## Tóm tắt

Dạng chuẩn lồi đặt điều kiện lên cả biểu thức và dấu ràng buộc. Biến phụ và đổi biến có thể làm cấu trúc hiện rõ. Phải chứng minh quan hệ với bài gốc. Nới lỏng tạo cận, còn nghiệm khả thi tạo ứng viên. Hai kết quả này phục vụ hai nhiệm vụ khác nhau.

## Nguồn và đọc thêm

- *Convex Optimization*, §4.1–4.2 (dạng chuẩn, tương đương), §4.3 (LP, tr. 146 trở đi), §4.4 (QP, SOCP, tr. 152–159), §4.5 (GP, tr. 160–166), §4.6 (SDP, tr. 167–173), §6.3 (điều chuẩn).
- Ví dụ số, cải dạng trị tuyệt đối và ví dụ nới lỏng nhị phân được tự biên soạn, tính lại bằng code. Những ràng buộc nón là định nghĩa từ sách. Không lấy nội dung bài giảng từ trang chỉ mục môn.

[Bài 01](./bai-01-nhap-mon-toi-uu.md) · [Bài 03 — Đối ngẫu Lagrange](./bai-03-doi-ngau-lagrange.md).
