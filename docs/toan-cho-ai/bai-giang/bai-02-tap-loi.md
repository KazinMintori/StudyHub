---
course: toan-cho-ai
lecture: bai-02-tap-loi
section: lecture
title: "Các bài toán tối ưu lồi"
prerequisites: ["tap-loi", "ham-loi", "chuan", "ma-tran-psd"]
lessonStatus: ready
description: "Nhận diện các dạng tối ưu lồi, cải dạng tương đương và phân biệt xấp xỉ với nới lỏng."
---

Ta đã biết thế nào là tập lồi và hàm lồi. Bây giờ câu hỏi là: một mô hình viết trên giấy có cung cấp được chứng nhận tính lồi không? Bài này tập đọc cấu trúc trước khi chọn thuật toán. Cùng một bài toán có thể hiện ra khó hoặc dễ tùy cách biểu diễn.

Sau bài, bạn có thể kiểm dạng chuẩn, nhận diện LP/QP/SOCP/SDP, thêm biến phụ có giải thích, và phân biệt một nghiệm của bài nới lỏng với nghiệm của bài gốc.

**Cách học:** mục 1–2 là tuyến chính; mục 3 cho phép cải dạng; mục 4–5 để đọc các mô hình mở rộng. Nếu tên nón còn lạ, đọc định nghĩa ngắn ở mục 4 rồi quay lại ví dụ. Nội dung tập lồi của phiên bản cũ đã được bố trí ở [Bài 01](./bai-01-nhap-mon-toi-uu.md) và [đọc thêm hình học](../doc-them/hinh-hoc-tap-loi.md); địa chỉ bài này được giữ để các liên kết cũ còn hoạt động.

## 1. Dạng chuẩn đòi điều gì?

Theo *Convex Optimization*, dạng chuẩn là

$$\begin{aligned}\text{minimize}\quad &f_0(x)\\
\text{subject to}\quad &f_i(x)\le0,\quad i=1,\ldots,m,\\&Ax=b,
\end{aligned}$$

với $f_0,f_i$ lồi, và các đẳng thức affine. Miền chung của các hàm cũng được xét. **Affine** nghĩa là dạng $a^Tx+b$; đẳng thức có thể chuyển hằng số sang vế phải.

Ba bước kiểm: mục tiêu có lồi không; các hàm ở vế trái của dấu $\le0$ có lồi không; đẳng thức có affine không. Miền khả thi lồi là hệ quả: tập mức dưới của hàm lồi là lồi, rồi lấy giao với các tập affine.

Đừng chỉ nhìn tên hàm. Ràng buộc $x^2\le1$ mô tả đoạn $[-1,1]$ và đúng dạng lồi. Ràng buộc $x^2\ge1$ đổi thành $1-x^2\le0$: vế trái lõm, miền gồm hai đoạn rời nhau. Ràng buộc $x^2=1$ là đẳng thức phi affine và cho hai điểm rời nhau.

### 1.1 Miền lồi và biểu diễn chuẩn là hai câu hỏi

Ràng buộc $x^3\le0$ tương đương $x\le0$, một miền lồi. Nhưng $x^3$ không lồi trên toàn $\mathbb R$, nên biểu thức ban đầu chưa chứng nhận dạng chuẩn. Cải dạng về $x\le0$ mới làm cấu trúc hiện rõ. Ta không gọi biểu thức ban đầu là chuẩn chỉ vì miền cuối cùng lồi.

<details><summary>Tự kiểm: min −log x với x≥1 có phải bài toán lồi?</summary>

Có. $-\log x$ lồi trên $x>0$, ràng buộc là $1-x\le0$ affine. Tuy nhiên mục tiêu đi tới $-\infty$ khi $x\to\infty$, nên không có nghiệm tối ưu hữu hạn. “Lồi” không bảo đảm bài toán có nghiệm.

</details>

## 2. LP và QP: nhận dạng bằng mục tiêu và miền

**Quy hoạch tuyến tính (LP)** có mục tiêu và ràng buộc affine:

$$\min c^Tx+d\quad\text{sao cho }Gx\preceq h,\ Ax=b.$$

Hằng số $d$ không đổi nghiệm; nó vẫn đổi giá trị tối ưu. Ký hiệu vector $\preceq$ ở đây là bất đẳng thức từng thành phần.

**Quy hoạch toàn phương (QP)** cho mục tiêu

$$\frac12x^TPx+q^Tx+r,\qquad P=P^T\succeq0,$$

và ràng buộc affine. $P$ PSD là điều kiện cho QP lồi. Nếu ràng buộc bất đẳng thức cũng là các hàm toàn phương lồi, ta có QCQP, không còn là QP theo định nghĩa này.

::: example Cùng loss hồi quy, thêm một giới hạn
Từ Bài 00, $f(w)=7w^2-11w+9/2$, nên trong dạng QP $P=14$, $q=-11$, $r=9/2$. Thêm $w\le1/2$ cho QP lồi.

Nghiệm không ràng buộc $11/14$ vượt giới hạn. Trên $w\le1/2$, đạo hàm $14w-11\le-4<0$, nên tăng $w$ luôn giảm loss cho đến biên. Nghiệm là $w^*=1/2$, $p^*=3/4$.

Đây là nghiệm tại biên với gradient khác 0. Bài 03 sẽ chứng nhận nó bằng nhân tử Lagrange.
:::

### 2.1 Điều chuẩn vẫn có thể giữ tính lồi

Ridge dùng $\tfrac12\|Aw-b\|_2^2+\tfrac\rho2\|w\|_2^2$, $\rho\ge0$. Hessian là $A^TA+\rho I$. Nếu $\rho>0$, với mọi $d\ne0$,

$$d^T(A^TA+\rho I)d=\|Ad\|_2^2+\rho\|d\|_2^2>0.$$

Trong bài không ràng buộc này, mục tiêu toàn phương PD có nghiệm duy nhất. Lasso dùng chuẩn 1 thay chuẩn 2 bình phương; vẫn lồi nhưng có thể không khả vi. “Không trơn” và “không lồi” là hai thuộc tính khác nhau.

## 3. Thêm biến phụ có thật sự giữ bài toán?

Xét bài $\min_x\max_i f_i(x)$. Thêm biến $t$:

$$\min_{x,t}t\quad\text{sao cho }f_i(x)\le t\ \forall i.$$

Với một $x$, mọi $t$ khả thi đều không nhỏ hơn $\max_i f_i(x)$, và chọn $t$ bằng maximum luôn khả thi. Vì vậy tối ưu theo $t$ trả lại đúng mục tiêu cũ. Đây là **cải dạng tương đương**, không chỉ là một hình trông giống nhau. Nếu các $f_i$ lồi, các hàm $f_i(x)-t$ cũng lồi.

::: example Khớp dữ liệu theo sai số tệ nhất
$\min_w\|Aw-b\|_\infty$ tương đương

$$\min_{w,t}t,\qquad -t\mathbf1\preceq Aw-b\preceq t\mathbf1.$$

$\mathbf1$ là vector toàn 1. Hai bất đẳng thức cho mỗi phần dư $r_i$ ép $-t\le r_i\le t$, tức $|r_i|\le t$. Các ràng buộc affine nên đây là LP, dù mục tiêu cũ chứa chuẩn và maximum.
:::

Với chuẩn 1, thêm $u_i$ sao cho $-u_i\le r_i\le u_i$, rồi cực tiểu $\sum_i u_i$. Tại tối ưu, có thể lấy $u_i=|r_i|$. Không cần thêm $u_i\ge0$: hai bất đẳng thức đã suy ra điều đó.

**Điểm dừng:** bạn cần chỉ ra hai chiều: từ một nghiệm khả thi cũ, tạo biến phụ hợp lệ; từ một nghiệm khả thi mới, thu hồi đối tượng cũ và so giá trị. Bỏ một chiều có thể biến cải dạng thành nới lỏng.

## 4. Nón giúp viết những ràng buộc khác

### 4.1 SOCP: chuẩn ở một vế, affine ở vế còn lại

**Nón bậc hai** là $K=\{(u,t):\|u\|_2\le t\}$. Quy hoạch nón bậc hai (SOCP) có mục tiêu affine và các ràng buộc

$$\|A_ix+b_i\|_2\le c_i^Tx+d_i,$$

cùng đẳng thức affine. Ràng buộc đã ép vế phải không âm. Không bình phương hai vế tùy ý nếu chưa giữ điều kiện đó: $|x|\le-1$ vô nghiệm nhưng $x^2\le1$ có nghiệm.

Minimize $\|Aw-b\|_2$ có thể viết $\min t$ với $\|Aw-b\|_2\le t$, một SOCP. Minimize bình phương chuẩn cũng có cùng nghiệm, vì bình phương tăng trên $[0,\infty)$, nhưng giá trị tối ưu không giống nhau.

### 4.2 SDP: điểm trong miền là một ma trận

Với ma trận đối xứng, $F(x)=F_0+\sum_i x_iF_i\succeq0$ là một **bất đẳng thức ma trận tuyến tính**. Miền lồi vì nón PSD lồi và $F$ affine. **SDP** cực tiểu mục tiêu affine với các ràng buộc loại này và đẳng thức affine.

Ví dụ tự đặt $\begin{bmatrix}t&x\\x&1\end{bmatrix}\succeq0$ tương đương $t\ge x^2$. Ta thấy một epigraph toàn phương có thể được viết bằng ma trận. Đây là so dạng toàn phương, không phải bắt từng phần tử ma trận không âm.

### 4.3 GP: đổi biến trước khi gọi là lồi

Trong quy hoạch hình học, biến $x_i>0$. Một **monomial** có dạng $c\prod_i x_i^{a_i}$, $c>0$, số mũ thực; **posynomial** là tổng các monomial. GP dùng posynomial $\le1$, monomial $=1$ và mục tiêu posynomial.

Đặt $y_i=\log x_i$, tức $x_i=e^{y_i}$. Log monomial trở thành $\log c+\sum_i a_i y_i$ affine. Với posynomial $\sum_k c_k\prod_i x_i^{a_{ki}}$, log của nó trở thành

$$\log\sum_k\exp\left(\log c_k+\sum_i a_{ki}y_i\right).$$

Đây là **log-sum-exp** của các biểu thức affine. Để thấy vì sao hàm nền $h(z)=\log\sum_k e^{z_k}$ lồi, đặt $p_k=e^{z_k}/\sum_j e^{z_j}$. Các $p_k$ không âm, cộng thành 1. Hessian là $\operatorname{diag}(p)-pp^T$, nên với mọi hướng $v$,

$$v^T\nabla^2h\,v=\sum_kp_kv_k^2-\left(\sum_kp_kv_k\right)^2
=\sum_kp_k(v_k-\bar v)^2\ge0,\qquad\bar v=\sum_kp_kv_k.$$

Viết thành tổng bình phương có trọng số chứng nhận PSD. Hợp với biểu thức affine giữ tính lồi theo quy tắc ở Bài 01. Lấy log các vế dương giữ chiều bất đẳng thức và giữ thứ tự mục tiêu. Vì vậy GP được giải bằng một bài lồi trong biến $y$; không khẳng định mọi posynomial lồi trong biến $x$.

<details><summary>Tự kiểm: x·y≤1 với x,y>0 trở thành điều gì?</summary>

Đặt $u=\log x$, $v=\log y$, ta được $u+v\le0$. Ví dụ này là ràng buộc monomial; $xy$ không lồi đồng thời theo $x,y$ trên miền dương nhưng cải dạng log là affine.

</details>

## 5. Xấp xỉ, nới lỏng và đánh giá nghiệm

**Xấp xỉ** thay đối tượng bằng một đối tượng gần hơn để tính: ví dụ tuyến tính hóa hàm. Cần nói gần ở đâu và kiểm sai số bằng gì. Không có cận một phía chỉ từ chữ “xấp xỉ”.

**Nới lỏng** mở rộng miền: $C\subseteq\widetilde C$. Giữ cùng mục tiêu trong bài min, ta có

$$\inf_{x\in\widetilde C}f(x)\le\inf_{x\in C}f(x).$$

Đây là cận dưới. Nghiệm ở miền rộng có thể không thỏa ràng buộc cũ. Trong bài max, chiều cận đổi.

::: example Biến nhị phân được nới thành một đoạn
Bài gốc $\min(x-0.4)^2$ với $x\in\{0,1\}$ đạt ở 0, giá trị $0.16$. Nới thành $0\le x\le1$ cho nghiệm $0.4$, giá trị 0. Cận 0 hợp lệ, nhưng $0.4$ không phải quyết định khả thi của bài nhị phân.

Làm tròn về 0 cho một ứng viên gốc có giá trị $0.16$. Cận và ứng viên cung cấp khoảng $[0,0.16]$ cho giá trị tối ưu; không được gọi nghiệm nới lỏng là nghiệm gốc.
:::

Muốn đánh giá một nghiệm, kiểm phần dư đẳng thức, độ vi phạm bất đẳng thức, giá trị mục tiêu và chứng nhận tối ưu riêng. Loss nhỏ mà vi phạm ràng buộc chưa phải một nghiệm tốt theo mô hình đã đặt.

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
Minimize $u+2v$ với $u\ge x-1$, $u\ge1-x$, $v\ge x+1$, $v\ge-x-1$. Trên ba miền, mục tiêu lần lượt là $-3x-1$, $x+3$, $3x+1$. Nó giảm tới $-1$, rồi tăng; nghiệm $x=-1$ cho giá trị 2. Các biến phụ tối ưu là $u=2$, $v=0$.
:::

::: exercise 3. Kiểm chiều cận
Bỏ ràng buộc $x\le1/2$ khỏi QP ở mục 2. Cận dưới mới và một cận trên khả thi của bài có ràng buộc là bao nhiêu?
:::
::: solution
Nghiệm không ràng buộc cho cận dưới $5/28$. Chọn $w=1/2$ khả thi cho cận trên $3/4$. Khoảng cách là $3/4-5/28=4/7$. Để chứng nhận cận trên chính là tối ưu, dùng lập luận đơn điệu ở mục 2 hoặc KKT ở bài tiếp theo.
:::

## Tóm tắt

Dạng chuẩn lồi đặt điều kiện lên cả biểu thức và dấu ràng buộc. Biến phụ và đổi biến có thể làm cấu trúc hiện rõ; phải chứng minh quan hệ với bài gốc. Nới lỏng tạo cận, còn nghiệm khả thi tạo ứng viên. Hai kết quả này phục vụ hai nhiệm vụ khác nhau.

## Nguồn và đọc thêm

- *Convex Optimization*, §4.1–4.2 (dạng chuẩn, tương đương), §4.3 (LP, tr. 146 trở đi), §4.4 (QP, SOCP, tr. 152–159), §4.5 (GP, tr. 160–166), §4.6 (SDP, tr. 167–173), §6.3 (điều chuẩn).
- Ví dụ số, cải dạng trị tuyệt đối và ví dụ nới lỏng nhị phân được tự biên soạn, tính lại bằng code. Những ràng buộc nón là định nghĩa từ sách; không lấy nội dung bài giảng từ trang chỉ mục môn.

[Bài 01](./bai-01-nhap-mon-toi-uu.md) · [Bài 03 — Đối ngẫu Lagrange](./bai-03-doi-ngau-lagrange.md).
