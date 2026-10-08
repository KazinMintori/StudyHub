---
course: toan-cho-ai
lecture: bai-03-doi-ngau-lagrange
section: lecture
title: "Đối ngẫu Lagrange"
prerequisites: ["ham-loi", "gradient", "he-phuong-trinh"]
lessonStatus: ready
description: "Tự tính Lagrangian, hàm đối ngẫu và khoảng cách đối ngẫu; dùng Slater và KKT để chứng nhận nghiệm."
---

Tìm được một điểm khả thi có giá trị hàm mục tiêu nhỏ chưa đủ để kết luận điểm đó tối ưu, vì vẫn có thể tồn tại một điểm khả thi khác tốt hơn. Một cách chứng nhận là xây dựng cận dưới đúng cho mọi nghiệm của bài toán cực tiểu. Nếu giá trị của một điểm khả thi bằng cận dưới ấy, không điểm nào có thể tốt hơn. Đối ngẫu Lagrange tạo ra các cận dưới như vậy bằng cách đưa các ràng buộc vào hàm mục tiêu với những hệ số thích hợp.

Ta tiếp tục bài $\min(x-2)^2$ với $x\le1$ từ Bài 01. Ví dụ này tự đặt. Lý thuyết dựa vào chương 5 của *Convex Optimization*.

Sau khi học xong, bạn sẽ tính được hàm đối ngẫu bằng cách lấy infimum theo biến gốc trước, xác minh được bốn nhóm điều kiện KKT, và dùng khoảng cách đối ngẫu để định lượng mức chưa tối ưu của một điểm khả thi.

Lần đọc đầu nên dừng sau mục 3, khi bạn đã tự tính được một hàm đối ngẫu và hiểu vì sao nó cho cận dưới. Mục 4 trình bày điều kiện Slater, còn mục 5–6 tổ chức các kết quả thành bốn nhóm điều kiện KKT. Không cần học thuộc tên các nhóm trước khi hiểu mỗi nhóm loại trừ sai sót nào.

## 1. Lagrangian và dấu của các nhân tử

Giả sử bài cực tiểu $f_0(x)$ có $m$ bất đẳng thức $f_i(x)\le0$ và $p$ đẳng thức $h_j(x)=0$. Ta cộng vào mục tiêu một số hạng cho mỗi ràng buộc. Viết đầy đủ:

$$
\begin{aligned}
L(x,\lambda,\nu)=f_0(x)
&+\lambda_1f_1(x)+\cdots+\lambda_mf_m(x)\\
&+\nu_1h_1(x)+\cdots+\nu_ph_p(x).
\end{aligned}
$$

Đó là **Lagrangian**, thường viết gọn thành

$$L(x,\lambda,\nu)=f_0(x)+\sum_{i=1}^m\lambda_i f_i(x)+\sum_{j=1}^p\nu_jh_j(x).$$

Chỉ số $i$ chạy qua các bất đẳng thức. $j$ chạy qua các đẳng thức. Mỗi tổng được xem là 0 nếu nhóm ràng buộc tương ứng rỗng. Sau khi phạm vi đã rõ, ta có thể viết $\sum_i$ hoặc $\sum_j$.

$\lambda_i$ là nhân tử cho bất đẳng thức. $\nu_j$ cho đẳng thức. Ta chọn $\lambda_i\ge0$. Tại một điểm khả thi $\widetilde x$, mỗi số $\lambda_i f_i(\widetilde x)\le0$ và mỗi $\nu_j h_j(\widetilde x)=0$. Vì vậy

$$L(\widetilde x,\lambda,\nu)\le f_0(\widetilde x).$$

Đẳng thức không đòi $\nu_j\ge0$: nhân với số 0 vẫn bằng 0 khi $\nu_j$ âm, bằng 0 hoặc dương. Dấu của nhân tử gắn với quy ước $f_i\le0$. Nếu đổi quy ước phải đổi tương ứng.

Giữ nhân tử cố định và lấy cận dưới theo $x$ trong miền chung $D$ của các hàm:

$$g(\lambda,\nu)=\inf_{x\in D}L(x,\lambda,\nu).$$

Ta không giữ các ràng buộc tường minh $f_i\le0,h_j=0$ trong phép infimum này. Chúng đã nằm trong Lagrangian. Các điều kiện miền xác định, như $x>0$ cho log, vẫn phải giữ.

Vì infimum không lớn hơn giá trị ở $\widetilde x$,

$$\boxed{g(\lambda,\nu)\le L(\widetilde x,\lambda,\nu)\le f_0(\widetilde x).}$$

Điều này đúng với mọi điểm khả thi, nên $g\le p^*$. Đây là **đối ngẫu yếu**, không cần bài gốc lồi. Nếu L không bị chặn dưới, $g=-\infty$. Cận ấy đúng nhưng không hữu ích.

## 2. Tính hàm đối ngẫu trong một ví dụ

Với ràng buộc $x-1\le0$,

$$L(x,\lambda)=(x-2)^2+\lambda(x-1),\qquad\lambda\ge0.$$

Để tính $g$, coi $\lambda$ là số cố định. Đạo hàm theo $x$:

$$2(x-2)+\lambda=0\quad\Rightarrow\quad x(\lambda)=2-\lambda/2.$$

Hessian theo $x$ bằng 2, nên điểm này cực tiểu L trên toàn $\mathbb R$. Thế lại:

$$g(\lambda)=\lambda-\frac{\lambda^2}4.$$

**Bài đối ngẫu** là cực đại cận dưới này:

$$\max_{\lambda\ge0}g(\lambda).$$

Ta có $g'(\lambda)=1-\lambda/2$, nên $\lambda^*=2$, $g(2)=1$. Nghiệm gốc $x^*=1$ cũng cho $f_0(1)=1$. Cận dưới và ứng viên gặp nhau. Cả hai tối ưu.

<MathLab type="dual">

```js
const g = lambda => lambda-lambda*lambda/4; // lambda >= 0
const gap = 1-g(lambda); // x=1 khả thi, f(1)=1
```

</MathLab>

Mô phỏng cơ chế cận dưới ở §5.1.3 và Hình 5.1 của sách bằng bài toán tự đặt. Đổi $\lambda$ để thấy cận có thể còn xa nghiệm. Khi $\lambda=0$, điểm cực tiểu L là 2, không khả thi cho bài gốc. Việc cực tiểu L không tự thu hồi nghiệm khả thi.

## 3. Tính lõm của hàm đối ngẫu

Với một $x$ cố định, $L(x,\lambda,\nu)$ là affine theo các nhân tử. Hàm $g$ lấy infimum của cả họ hàm affine ấy. Để xác định đúng chiều bất đẳng thức, gọi hai bộ nhân tử là $u,v$ và lấy $0\le\theta\le1$:

$$\begin{aligned}
g(\theta u+(1-\theta)v)
&=\inf_x[\theta L(x,u)+(1-\theta)L(x,v)]\\
&\ge\theta\inf_xL(x,u)+(1-\theta)\inf_xL(x,v).
\end{aligned}$$

Mỗi giá trị bên trong infimum không nhỏ hơn vế phải, nên lấy infimum vẫn giữ cận. Đây là bất đẳng thức hàm lõm. Vì vậy bài cực đại $g$ trên miền nhân tử khả thi là bài tối ưu lồi, kể cả khi bài gốc không lồi. Điều này không bảo đảm cận chạm $p^*$.

<details><summary>Thử trả lời: Bài toán đối ngẫu cực tiểu hay cực đại hàm g, và vì sao?</summary>

Cực đại: mọi giá trị $g$ hợp lệ đều là cận dưới. Ta muốn cận lớn nhất, gần giá trị tối ưu gốc nhất. Cực tiểu g chỉ làm cận yếu đi.

</details>

## 4. Điều kiện Slater và đối ngẫu mạnh

Gọi $d^*$ là giá trị tối ưu đối ngẫu. Đối ngẫu yếu cho $d^*\le p^*$. Khi $d^*=p^*$, ta có **đối ngẫu mạnh**. Lồi chưa tự bảo đảm đẳng thức này trong mọi trường hợp.

Với bài lồi dạng chuẩn, **điều kiện Slater** yêu cầu tồn tại $\bar x\in\operatorname{relint}D$ sao cho

$$f_i(\bar x)<0\ \forall i,\qquad A\bar x=b.$$

Nội tương đối $\operatorname{relint}D$ là phần trong của miền khi nhìn trong không gian affine nhỏ nhất chứa nó. Một đoạn nằm trên đường trong $\mathbb R^2$ có nội hai chiều rỗng nhưng có nội tương đối là phần giữa hai đầu mút. Cần khái niệm này khi miền sống trong một không gian thấp chiều.

Slater là điều kiện đủ cho đối ngẫu mạnh. Khi giá trị tối ưu gốc hữu hạn, điều kiện này còn bảo đảm bài toán đối ngẫu đạt nghiệm. Đối với các bất đẳng thức affine, sách nêu một phiên bản Slater yếu hơn, không bắt buộc mọi bất đẳng thức affine phải thỏa chặt. Trong bài này ta dùng phiên bản đủ ở trên và không coi Slater là điều kiện cần.

Ví dụ mở đầu có $\bar x=0$ thỏa $x-1=-1<0$. Các hàm hữu hạn trên toàn $\mathbb R$, nên nội tương đối không tạo hạn chế thêm. Đối ngẫu mạnh phù hợp với phép tính $p^*=d^*=1$.

## 5. Bốn nhóm điều kiện KKT

Giả sử mục tiêu và các hàm bất đẳng thức khả vi. Đẳng thức affine. Các điều kiện **Karush–Kuhn–Tucker (KKT)** gồm:

| Nhóm | Công thức | Điều cần xác minh |
| --- | --- | --- |
| Khả thi gốc | $f_i(x)\le0$, $Ax=b$ | $x$ có hợp lệ không? |
| Khả thi đối ngẫu | $\lambda_i\ge0$ | Có giữ được cận dưới không? |
| Bù trừ | $\lambda_i f_i(x)=0$ | Số hạng bất đẳng thức nào còn đóng góp? |
| Dừng | $\nabla f_0(x)+\sum_i\lambda_i\nabla f_i(x)+A^T\nu=0$ | $x$ có cực tiểu Lagrangian không? |

Trong **bài lồi**, KKT đủ cho tối ưu. Lý do: $L$ lồi theo $x$ khi các nhân tử không âm. Dừng cho $x$ cực tiểu L. Khả thi và bù trừ cho $L(x)=f_0(x)$. Vậy $g=f_0(x)$ và khoảng cách đối ngẫu bằng 0.

Nếu bài lồi khả vi thỏa Slater và có nghiệm gốc đạt, KKT cũng cần: mỗi nghiệm có một bộ nhân tử phù hợp. Với bài không lồi, dừng của L chưa bảo đảm cực tiểu toàn cục, nên không dùng KKT như chứng nhận toàn cục.

::: example Đối chiếu bốn điều kiện trong ví dụ một chiều
Tại $x^*=1$, $\lambda^*=2$:

1. $x^*-1=0\le0$.
2. $\lambda^*=2\ge0$.
3. $2(1-1)=0$.
4. $2(1-2)+2=0$.

Không có đẳng thức nên không có $\nu$. Ràng buộc chặt vì $f_1(x^*)=0$. Nhân tử 2 cân bằng gradient $-2$ của mục tiêu.
:::

Bù trừ chỉ cho hai khả năng: ràng buộc không chặt thì nhân tử bằng 0. Nhân tử dương thì ràng buộc chặt. Ràng buộc chặt vẫn có thể có nhân tử 0. Không đảo các mệnh đề ấy.

## 6. Một ví dụ hai chiều với đẳng thức

Tự đặt bài

$$\min_{x,y}\frac12[(x-2)^2+y^2],\qquad x+y=1.$$

Lagrangian $L=\tfrac12[(x-2)^2+y^2]+\nu(x+y-1)$. Nhân tử $\nu$ không bị giới hạn dấu. Điều kiện dừng cho $x=2-\nu$, $y=-\nu$. Đẳng thức cho $2-2\nu=1$, nên

$$\nu^*=\frac{1}{2},\quad x^*=\frac{3}{2},\quad y^*=-\frac{1}{2},\quad p^*=\frac{1}{4}.$$

Nghiệm có $y<0$ vẫn hợp lệ vì bài chưa đặt ràng buộc không âm. Tự thêm $y\ge0$ sẽ đổi bài toán.

Tính đối ngẫu cho $g(\nu)=\nu-\nu^2$. Tại $\nu=\frac{1}{2}$, $g=\frac{1}{4}$ bằng mục tiêu. Bài này là trường hợp cụ thể của QP có đẳng thức ở Ví dụ 5.1. Số liệu tự đặt. Dạng hệ tổng quát là

$$\begin{bmatrix}P&A^T\\A&0\end{bmatrix}
\begin{bmatrix}x^*\\\nu^*\end{bmatrix}
=\begin{bmatrix}-q\\b\end{bmatrix}.$$

Bài 04 dùng cùng cấu trúc để tính bước Newton khi mục tiêu không chỉ là một hàm toàn phương cố định.

## 7. Khoảng cách đối ngẫu và độ nhạy

Với $x$ khả thi gốc và $(\lambda,\nu)$ khả thi đối ngẫu,

$$0\le f_0(x)-p^*\le f_0(x)-g(\lambda,\nu).$$

Vế phải là **khoảng cách đối ngẫu** của cặp đang có. Nó cho cận trên của độ thiếu tối ưu mà không cần biết $p^*$. Tại $x=0$, $\lambda=2$ trong ví dụ một chiều, $f_0=4$, $g=1$, nên khoảng cách bằng 3. Điểm ấy đúng là kém tối ưu 3.

Nếu thay ràng buộc bằng $x\le b$, gần $b=1$ và còn $b<2$, nghiệm là $x=b$, giá trị $(b-2)^2$. Đạo hàm theo $b$ tại 1 là $-2=-\lambda^*$. Cho thêm một lượng nhỏ giới hạn làm giá trị tối ưu giảm với tốc độ xấp xỉ 2. Diễn giải độ nhạy cần điều kiện tính khả vi của hàm giá trị. Không coi nhân tử là dự báo chính xác cho mọi thay đổi lớn.

## Bài tập tự luyện

::: exercise 1. Tính trước theo biến gốc
Với $\min x^2$, $x\ge1$, viết ràng buộc dạng $\le0$ rồi tính $g(\lambda)$.
:::
::: solution
Dùng $1-x\le0$. $L=x^2+\lambda(1-x)$ cực tiểu tại $x=\lambda/2$, nên $g=\lambda-\\frac{lambda^2}{4}$, $\lambda\ge0$. Đối ngẫu đạt tại $\lambda=2$, cho $g=1$ và thu hồi $x=1$ khả thi.
:::

::: exercise 2. Nhân tử bằng 0 tại biên
Với $\min x^2$, $x\le0$, hãy xác minh các điều kiện KKT tại $x=0$, $\lambda=0$.
:::
::: solution
Khả thi $x=0$. Nhân tử không âm. Bù trừ $0\cdot0=0$. Dừng $2x+\lambda=0$. Ràng buộc chặt dù nhân tử bằng 0. Đây là phản ví dụ cho suy luận “ràng buộc chặt thì nhân tử dương”.
:::

::: exercise 3. Chứng nhận QP hồi quy
Với QP ở Bài 02, $f'(w)=14w-11$, $w\le1/2$. Tìm nhân tử tại $w=\frac{1}{2}$.
:::
::: solution
Ràng buộc $w-\frac{1}{2}\le0$, dừng $14(\frac{1}{2})-11+\lambda=0$ cho $\lambda=4$. Nhân tử dương và ràng buộc chặt nên đủ bốn nhóm KKT. Bài lồi, vậy $w=\frac{1}{2}$ tối ưu. Không cần đoán nghiệm từ thuật toán.
:::

## Tóm tắt

Đối ngẫu yếu đến từ dấu của nhân tử và phép infimum. Slater là một điều kiện đủ để cận tốt nhất chạm giá trị gốc. KKT gồm những điều kiện có vai trò riêng. Trong bài lồi, chúng nối cực tiểu Lagrangian với nghiệm khả thi. Khoảng cách đối ngẫu cho biết cặp nghiệm hiện tại còn cách tối ưu nhiều nhất bao nhiêu.

## Nguồn và đọc thêm

- *Convex Optimization*, §5.1 (tr. 215–222), §5.2.1–5.2.3 (tr. 223–228), §5.5.1–5.5.3 (tr. 241–245), Ví dụ 5.1 (tr. 244–245), §5.6 về nhiễu và độ nhạy.
- Mô phỏng cận dưới dựa vào cơ chế của Hình 5.1, dữ liệu tự đặt. Tất cả ví dụ số và bài tập tự biên soạn đã được tính lại.

[Bài 02](./bai-02-tap-loi.md) · [Bài 04 — Gradient và Newton](./bai-04-gradient-newton.md).
