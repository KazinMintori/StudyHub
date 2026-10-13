---
course: toan-cho-ai
lecture: on-luyen
topic: tinh-loi-va-toi-uu
section: topic
title: "Tập lồi, hàm lồi và nghiệm tối ưu"
description: "Đường và đoạn thẳng, tính lồi, Jensen, Hessian, miền khả thi lồi, chứng minh cực tiểu địa phương là toàn cục và điều kiện gradient."
---

Kiểm tra một lân cận nhỏ thường dễ hơn so sánh với cả miền. Tính lồi cho phép nối hai việc ấy: Một đoạn thẳng mang thông tin từ điểm bất kỳ về gần điểm đang xét.

## 1. Đạo hàm dùng trong tiêu chuẩn lồi

Với hàm một biến khả vi, đạo hàm là độ dốc tiếp tuyến. Định lý Fermat nói cực trị tại điểm trong kéo theo đạo hàm bằng không. Nếu thêm đạo hàm bậc hai dương tại điểm dừng thì có cực tiểu nghiêm địa phương.

Định lý giá trị trung bình và Taylor được viết

$$
\begin{aligned}
&f(x) = f(x_0)+f'(c_1)(x-x_0),\\
&f(x) = f(x_0)+f'(x_0)(x-x_0)+\frac12f''(c_2)(x-x_0)^2.
\end{aligned}
$$

Các điểm $c_1,c_2$ nằm giữa hai đầu mút và không nhất thiết bằng nhau. Cần tính liên tục và khả vi trên đoạn như đã nêu ở [đạo hàm và cực trị](./dao-ham-va-cuc-tri.md).

Trong nhiều biến, gradient gom các đạo hàm riêng. Nếu $f\in C^2$, Hessian đối xứng vì các đạo hàm hỗn hợp có thể đổi thứ tự. Tại cực tiểu trong miền, gradient phải bằng không và Hessian PSD. Hessian PD tại một điểm dừng đủ cho cực tiểu nghiêm địa phương. Những điều kiện này chưa nói hàm lồi trên cả miền.

## 2. Đường thẳng, đoạn thẳng và tập lồi

Qua hai điểm khác nhau $x,y\in\mathbb R^n$, đường thẳng có biểu diễn

$$
\begin{aligned}
&z(t) = x+t(y-x)\\
&\quad =(1-t)x+ty,\quad t\in\mathbb R.
\end{aligned}
$$

Giới hạn $0\le t\le1$ tạo đoạn nối hai điểm. Tại $t=0$ ta ở $x$, tại $t=1$ ta ở $y$. Hai trọng số không âm và cộng thành 1, nên điểm tổ hợp không vượt ra ngoài hai đầu mút.

Tập $D$ là lồi nếu chứa toàn bộ đoạn nối của mọi cặp điểm thuộc nó. Có thể viết bằng $(1-t)x+ty$ hoặc $tx+(1-t)y$, vì thay $t$ bằng $1-t$ không thay tập các điểm trên đoạn.

<ConvexSetLab />

Đĩa tròn và đa giác lồi chứa đoạn nối mọi cặp điểm. Miền có chỗ lõm có thể chứa hai đầu mút nhưng bỏ sót một phần đoạn ở giữa. Một cặp như vậy đủ để bác bỏ tính lồi. Ngược lại, kiểm được vài cặp không chứng minh tính lồi vì định nghĩa yêu cầu mọi cặp.

## 3. Hàm lồi và affine

Hàm $f:D\to\mathbb R$ là lồi khi $D$ lồi và

$$
f(tx+(1-t)y)\le tf(x)+(1-t)f(y)
$$

với mọi $x,y\in D$, mọi $t\in[0,1]$. Vế phải là độ cao dây cung, vế trái là độ cao đồ thị tại điểm cùng tọa độ tổ hợp.

Hàm affine $\ell(x)=a^Tx+b$ thỏa đẳng thức

$$
\ell(tx+(1-t)y)=t\ell(x)+(1-t)\ell(y).
$$

Vì thế hàm affine vừa lồi vừa lõm. Điều này giải thích tại sao dấu của hệ số tuyến tính không ảnh hưởng tính lồi của LP.

## 4. Jensen cho nhiều điểm

Từ hai điểm có thể mở rộng tới $k$ điểm $x_1,\ldots,x_k\in D$. Các trọng số phải thỏa

$$
\begin{aligned}
&\alpha_i \ge 0,\quad i=1,\ldots,k,\\
&\sum_{i=1}^{k}\alpha_i = \alpha_1+\cdots+\alpha_k=1.
\end{aligned}
$$

Đây là cách phân bổ tổng trọng số 100% cho các điểm, không có trọng số âm. Bất đẳng thức Jensen là

$$
f(\alpha_1x_1+\cdots+\alpha_kx_k)\le\alpha_1f(x_1)+\cdots+\alpha_kf(x_k).
$$

Ký hiệu gọn tương ứng là

$$
f\left(\sum_{i=1}^{k}\alpha_i x_i\right)\le\sum_{i=1}^{k}\alpha_i f(x_i).
$$

Có thể chứng minh bằng quy nạp: Gom $k-1$ điểm đầu thành một điểm bình quân có tổng trọng số $1-\alpha_k$, rồi áp dụng tính lồi hai điểm. Nếu $\alpha_k=1$, các trọng số khác bằng không và hai vế bằng nhau.

## 5. Tiêu chuẩn Hessian

Nếu $f\in C^2$ trên một miền mở lồi, thì $f$ lồi khi và chỉ khi

$$
\nabla^2 f(x)\succeq0\quad\forall x\in D.
$$

Để hiểu điều kiện này, hạn chế hàm lên đường $x+th$. Đạo hàm bậc hai dọc đường là $h^T\nabla^2 f(x+th)h$. Hessian PSD làm độ cong trên mọi đường không âm, đưa bài nhiều biến về tiêu chuẩn lồi một biến.

Phải giữ lượng từ “mọi điểm”. Hessian PSD chỉ tại một ứng viên không chứng minh toàn hàm lồi.

## 6. Miền khả thi của bài toán lồi

Giả sử các $f_i$ lồi và các $h_j$ affine. Với hai điểm khả thi $x,y$ và $z=(1-t)x+ty$,

$$
\begin{aligned}
&f_i(z) \le (1-t)f_i(x)+tf_i(y)\\
&\quad \le0,\\
&h_j(z) = (1-t)h_j(x)+th_j(y)\\
&\quad =0.
\end{aligned}
$$

Do đó $z$ khả thi và miền lồi. Nếu mục tiêu $f$ cũng lồi, bài toán là tối ưu lồi. Không thể thay “đẳng thức affine” bằng “đẳng thức hàm lồi” một cách tùy ý, vì tập mức bằng của hàm lồi không nhất thiết lồi.

## 7. Cực tiểu địa phương là toàn cục

> **Định lý.** Nếu $D$ lồi và $f$ lồi trên $D$, mọi cực tiểu địa phương của min $f$ trên $D$ đều là nghiệm tối ưu toàn cục.

::: proof Đưa điểm bất kỳ về gần cực tiểu
Cho $x$ là cực tiểu địa phương và $y\in D$ bất kỳ. Nếu $y=x$ thì không cần chứng minh. Nếu $y\ne x$, chọn $t\in(0,1)$ đủ nhỏ để $z=x+t(y-x)$ nằm trong lân cận nơi $x$ tối ưu địa phương.

Tính lồi của miền cho $z\in D$. Tối ưu địa phương và tính lồi của hàm lần lượt cho

$$
\begin{aligned}
&f(x) \le f(z)\\
&\quad \le(1-t)f(x)+tf(y).
\end{aligned}
$$

Trừ $(1-t)f(x)$ rồi chia cho $t>0$ được $f(x)\le f(y)$. Vì $y$ tùy ý, $x$ tối ưu toàn cục. Lập luận không giả sử trước kết luận cần chứng minh.
:::

## 8. Gradient bằng không trong bài không ràng buộc

Với hàm lồi khả vi trên $\mathbb R^n$, mặt phẳng tiếp tuyến là cận dưới:

$$
f(y)\ge f(x)+\nabla f(x)^T(y-x).
$$

Nếu $\nabla f(x)=0$, vế phải bằng $f(x)$ với mọi $y$, nên $x$ tối ưu toàn cục. Điều này không tự bảo đảm duy nhất. Hàm hằng có gradient bằng không ở mọi điểm và mọi điểm đều tối ưu. Lồi nghiêm trên miền lồi cho nhiều nhất một nghiệm.

## 9. Bài tập tự luyện

::: exercise Đẳng thức phi tuyến
Hàm $h(x)=x^2$ lồi. Tập nghiệm $h(x)=1$ có lồi không? Điều này giải thích yêu cầu affine của ràng buộc đẳng thức như thế nào?
:::

::: solution
Tập nghiệm là $\{-1,1\}$. Trung điểm 0 không thuộc tập vì $h(0)=0$. Vì vậy tập không lồi. Bản thân hàm ràng buộc lồi không đủ để tập nghiệm đẳng thức lồi, trong khi đẳng thức affine luôn bảo toàn tổ hợp affine của các điểm nghiệm.
:::
