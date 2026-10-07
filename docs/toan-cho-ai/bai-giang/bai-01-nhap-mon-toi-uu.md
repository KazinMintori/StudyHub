---
course: toan-cho-ai
lecture: bai-01-nhap-mon-toi-uu
section: lecture
title: "Giới thiệu tối ưu, tập lồi và hàm lồi"
prerequisites: ["vector", "tich-vo-huong", "gradient", "hessian", "ma-tran-psd"]
lessonStatus: ready
description: "Từ lựa chọn khả thi đến tập lồi, hàm lồi và chứng nhận tối ưu toàn cục; minh họa bằng chương trình."
---

Ở Bài 00, ta tìm được tham số làm loss nhỏ nhất bằng cách khai triển một bình phương. Với nhiều tham số và nhiều ràng buộc, khai triển có thể không đủ gọn. Bài này tìm một cấu trúc cho phép chứng nhận nghiệm: tính lồi của miền và của hàm mục tiêu.

Sau bài, bạn có thể viết biến–mục tiêu–ràng buộc, phân biệt tập lồi với hàm lồi, và chỉ ra điều kiện nào làm một điểm dừng trở thành nghiệm toàn cục.

**Ba điểm dừng:** mục 1 cho mô hình; mục 2–3 cho hình học; mục 4–6 cho chứng nhận nghiệm. Đọc Bài 00 nếu các phép nhân $x^Ty$, $v^THv$ còn chưa rõ. Phần [hình học bổ sung](../doc-them/hinh-hoc-tap-loi.md) giữ các khái niệm nón, phối cảnh và Pareto để đọc sau khi đã nắm tuyến chính.

## 1. Chọn điều gì, chấm bằng gì, giới hạn ở đâu?

Ta dùng ví dụ một chiều tự đặt: muốn $x$ gần 2, nhưng chỉ được chọn $x\le1$:

$$\begin{aligned}\text{minimize}\quad &(x-2)^2\\\text{subject to}\quad &x\le1.\end{aligned}$$

Biến là $x$, mục tiêu là $f_0(x)=(x-2)^2$, ràng buộc là $f_1(x)=x-1\le0$. Miền khả thi $C=(-\infty,1]$ chứa các lựa chọn hợp lệ. Điểm $x=2$ cho loss 0 nhưng không khả thi. Điểm $x=0$ khả thi nhưng chưa tốt nhất; $x=1$ có loss nhỏ hơn.

Tổng quát, bài toán tối ưu có mục tiêu $f_0$, bất đẳng thức $f_i(x)\le0$ và đẳng thức $h_j(x)=0$. Miền chung còn phải nằm trong miền xác định của các hàm: chẳng hạn $\log x$ yêu cầu $x>0$.

**Nghiệm tối ưu** $x^*$ phải khả thi và thỏa $f_0(x^*)\le f_0(y)$ với mọi $y$ khả thi. **Giá trị tối ưu** là

$$p^*=\inf_{x\in C}f_0(x).$$

$\inf$ là cận dưới lớn nhất, không nhất thiết có điểm đạt được. Ba trường hợp cần nhận ra trước khi giải:

| Bài toán | Điều xảy ra |
| --- | --- |
| $\min x^2$, $x\ge2$, $x\le1$ | Miền rỗng: không khả thi. |
| $\min(-x)$, $x\in\mathbb R$ | Không bị chặn dưới: $p^*=-\infty$. |
| $\min x$, $x>0$ | $p^*=0$ nhưng không có điểm đạt cận. |

Đổi $\max q(x)$ thành $\min[-q(x)]$ giữ nghiệm và đổi dấu giá trị tối ưu. Dữ liệu cố định như 2 và 1 trong ví dụ không trở thành biến quyết định.

<details><summary>Tự kiểm: x=1 có tối ưu chỉ vì khả thi không?</summary>

Không. Còn phải so với mọi $x\le1$. Ở ví dụ này $2-x\ge1$, nên $(x-2)^2\ge1$, với dấu bằng tại $x=1$. Lập luận này mới chứng nhận nghiệm.

</details>

## 2. Tập lồi: pha hai lựa chọn hợp lệ có còn hợp lệ?

Với $x,y\in\mathbb R^n$, điểm $z=\theta x+(1-\theta)y$, $0\le\theta\le1$, đi trên đoạn nối. Ta gọi đây là **tổ hợp lồi**. Hai trọng số không âm và cộng thành 1.

Tập $C$ **lồi** nếu với mọi $x,y\in C$ và mọi $\theta\in[0,1]$, $z$ vẫn thuộc $C$. Chữ “mọi” quyết định định nghĩa: một đoạn nối tốt chưa chứng minh cả tập lồi; một đoạn nối xấu đủ bác bỏ.

<MathLab type="segment">

```js
const z = A.map((a, i) => theta*a + (1-theta)*B[i]);
// 0 <= theta <= 1: đoạn nối. Ngoài khoảng này: cả đường thẳng.
```

</MathLab>

Mô phỏng tái hiện quan hệ của Hình 2.1, *Convex Optimization*, tr. 22, bằng tọa độ tự đặt $A=(-1,1)$, $B=(2,-1)$. Hãy đưa $\theta$ ra ngoài $[0,1]$: điểm vẫn nằm trên đường nhưng rời đoạn. Một **tập affine** phải giữ mọi tổ hợp đó với $\theta\in\mathbb R$, nên đòi hỏi mạnh hơn tập lồi.

### 2.1 Chứng minh một ràng buộc tạo miền lồi

Với nửa không gian $C=\{x:a^Tx\le b\}$, lấy $x,y\in C$. Khi $0\le\theta\le1$,

$$a^Tz=\theta a^Tx+(1-\theta)a^Ty\le\theta b+(1-\theta)b=b.$$

Ta đã dùng tính tuyến tính để đưa phép pha ra ngoài tích, rồi dùng trọng số không âm để giữ chiều bất đẳng thức. Tập nghiệm $Ax=b$ là affine: cùng phép tính cho dấu bằng, kể cả khi $\theta$ âm.

Giao các tập lồi là lồi, vì đoạn nối phải thỏa từng điều kiện một. Do đó **đa diện** $\{x:Ax\preceq b\}$, tức một hệ hữu hạn bất đẳng thức theo từng thành phần, là lồi. Ký hiệu $\preceq$ ở đây so từng tọa độ.

### 2.2 Chuẩn và ảnh affine

Quả cầu chuẩn $\{x:\|x\|\le r\}$ với $r\ge0$ là lồi. Bất đẳng thức tam giác và tính thuần nhất của chuẩn cho

$$\|\theta x+(1-\theta)y\|\le\theta\|x\|+(1-\theta)\|y\|\le r.$$

Đường tròn $x_1^2+x_2^2=1$ không lồi: trung điểm $(1,0)$ và $(-1,0)$ là $(0,0)$, không thỏa đẳng thức. Hình tròn đặc thay dấu bằng bằng $\le$ thì lồi. Đổi dấu ràng buộc làm đổi miền.

Ảnh và ảnh ngược của một tập lồi qua $F(x)=Ax+b$ đều lồi. Với ảnh ngược, nếu $F(x),F(y)\in C$, thì $F(z)=\theta F(x)+(1-\theta)F(y)\in C$. Không cần $A$ khả nghịch. Đây là cách đọc miền $\|Ax-b\|\le r$.

<details><summary>Tự kiểm: hợp của [−2,−1] và [1,2] có lồi không?</summary>

Không. Hai điểm $-1,1$ thuộc hợp nhưng trung điểm 0 không thuộc. Phép giao giữ tính lồi; phép hợp nói chung không giữ.

</details>

## 3. Hàm lồi: pha đầu vào hay pha giá trị?

Hai thao tác khác nhau là tính $f(\theta x+(1-\theta)y)$ và tính $\theta f(x)+(1-\theta)f(y)$. **Hàm lồi** có miền lồi và thỏa

$$\boxed{f(\theta x+(1-\theta)y)\le\theta f(x)+(1-\theta)f(y)}$$

với mọi $x,y$ trong miền và $0\le\theta\le1$. Trên hình, đồ thị nằm dưới dây cung nối hai điểm của đồ thị. Hàm **lõm** có bất đẳng thức đảo chiều; tương đương $-f$ lồi.

<MathLab type="chord">

```js
const z = theta*a + (1-theta)*b;
const onCurve = f(z);
const onChord = theta*f(a) + (1-theta)*f(b);
```

</MathLab>

Mô phỏng quan hệ trong Hình 3.1, sách tr. 67, bằng $f(x)=x^2$, $a=-1$, $b=2$. Tại $\theta=1/2$, đầu vào pha là $z=1/2$, giá trị hàm là $1/4$, còn dây cung cao $5/2$. Thử $-x^2$ để thấy chiều bất đẳng thức đổi. Thử các điểm hữu hạn là minh họa, không thay định nghĩa với lượng từ “mọi”.

Đồ thị của $x^2$ không phải tập lồi: trung điểm hai điểm trên đồ thị có thể nằm phía trên. Tập **epigraph** $\{(x,t):t\ge f(x)\}$ gồm toàn bộ miền phía trên đồ thị mới là tập lồi khi và chỉ khi $f$ lồi.

## 4. Làm sao kiểm tính lồi mà không thử mọi dây cung?

### 4.1 Gradient tạo một cận dưới toàn cục

Giả sử $f$ khả vi trên miền mở lồi. Khi đó $f$ lồi khi và chỉ khi

$$f(y)\ge f(x)+\nabla f(x)^T(y-x)\quad\text{với mọi }x,y\text{ trong miền}.$$

Vế phải là xấp xỉ bậc nhất tại $x$. Với hàm bất kỳ, nó chỉ gần đúng khi $y$ gần $x$; tính lồi làm nó thành cận dưới ở mọi $y$.

Để thấy bước quyết định, đặt $x_t=x+t(y-x)$, $0<t\le1$. Tính lồi cho $f(x_t)\le(1-t)f(x)+tf(y)$. Chuyển vế và chia cho $t>0$:

$$f(y)\ge f(x)+\frac{f(x+t(y-x))-f(x)}t.$$

Cho $t\downarrow0$, thương tiến tới đạo hàm theo hướng $y-x$, bằng $\nabla f(x)^T(y-x)$. Đây là chỗ tính lồi nối thông tin cục bộ với kết luận toàn cục.

### 4.2 Hessian không âm theo mọi hướng

Nếu $f$ hai lần khả vi trên miền mở lồi, thì $f$ lồi khi và chỉ khi $\nabla^2f(x)\succeq0$ ở mọi $x$. Miền lồi vẫn là điều kiện riêng: $1/x^2$ trên $\mathbb R\setminus\{0\}$ có đạo hàm bậc hai dương nhưng miền không lồi.

Với $f(x)=\tfrac12x^TPx+q^Tx+r$, $P=P^T$, Hessian bằng $P$. Vì vậy $P\succeq0$ chứng nhận tính lồi. Loss hồi quy ở Bài 00 có $P=A^TA$ nên lồi. Với $|x|$, hàm lồi dù không khả vi ở 0; khi đó không dùng phép kiểm đạo hàm tại điểm ấy.

### 4.3 Ghép những hàm đã biết

Tổng có trọng số không âm của các hàm lồi vẫn lồi. Hợp với ánh xạ affine $f(Ax+b)$ giữ tính lồi. Maximum của hữu hạn hàm lồi cũng lồi. Ví dụ $\|Ax-b\|_\infty$ là maximum của các biểu thức affine $\pm(a_i^Tx-b_i)$.

Không suy rằng mọi hợp hai hàm lồi đều lồi: $g(u)=(u-1)^2$ và $h(x)=x^2$ đều lồi, nhưng $g(h(x))=(x^2-1)^2$ có đạo hàm bậc hai tại 0 bằng $-4$.

## 5. Vì sao nghiệm cục bộ của bài toán lồi là toàn cục?

Xét cực tiểu hàm lồi $f$ trên miền lồi $C$. “Cục bộ” nghĩa là không có điểm khả thi tốt hơn trong một lân cận đủ nhỏ; “toàn cục” xét mọi điểm khả thi.

Giả sử $x^*$ tối ưu cục bộ nhưng có $y\in C$ với $f(y)<f(x^*)$. Pha một lượng nhỏ $t$ của $y$ vào $x^*$:

$$z=(1-t)x^*+ty\in C,$$

$$f(z)\le(1-t)f(x^*)+tf(y)<f(x^*).$$

Với $t>0$ đủ nhỏ, $z$ ở trong lân cận của $x^*$, trái với tối ưu cục bộ. Tập lồi được dùng để $z$ khả thi; hàm lồi được dùng để $f(z)$ nhỏ hơn. Thiếu một trong hai bước thì chứng minh không còn.

### 5.1 Gradient bằng 0: đủ khi nào?

Không ràng buộc, với $f$ khả vi lồi trên miền mở lồi, $\nabla f(x^*)=0$ kéo theo

$$f(y)\ge f(x^*)+0=f(x^*)\quad\forall y.$$

Nếu bỏ tính lồi, $f(x)=-x^2$ có đạo hàm 0 tại 0 nhưng đó là cực đại. Nếu có ràng buộc, nghiệm có thể có gradient khác 0: ví dụ mở đầu đạt tại $x^*=1$, nhưng $f'(1)=-2$.

Điều kiện đúng cho miền lồi $C$ và hàm khả vi lồi là $x^*\in C$ cùng với

$$\nabla f(x^*)^T(y-x^*)\ge0\quad\forall y\in C.$$

Trong ví dụ, $-2(y-1)\ge0$ khi $y\le1$. Mọi hướng tới điểm khả thi đều không làm xấp xỉ bậc nhất giảm. Bài 03 chuyển điều kiện này thành các phương trình KKT có thể kiểm được.

## 6. Tính duy nhất và ranh giới trong AI

Lồi **nghiêm** dùng dấu $<$ khi $x\ne y$, $0<\theta<1$. Nếu có hai nghiệm khác nhau trên miền khả thi lồi, trung điểm sẽ có giá trị nhỏ hơn giá trị tối ưu, vô lý. Vì vậy nhiều nhất một nghiệm. Nó vẫn không bảo đảm đạt nghiệm: $e^x$ lồi nghiêm trên $\mathbb R$ nhưng cận 0 chỉ đạt khi $x\to-\infty$.

Một mô hình tuyến tính theo tham số với loss bình phương là lồi. Một mô hình nhiều tầng có thể mất cấu trúc ấy. Ví dụ tự đặt $f(u,v)=(uv-1)^2$: hai điểm $(1,1)$ và $(-1,-1)$ có loss 0, trung điểm $(0,0)$ có loss 1. Bất đẳng thức dây cung bị vi phạm. Mỗi tầng tuyến tính riêng không có nghĩa loss lồi đồng thời theo tất cả trọng số.

## 7. Dùng cấu trúc này trong hai mô hình AI

Hai ví dụ sau kết nối kết quả với mô hình. Có thể đọc chúng ở lượt sau khi đã giải thích được điều kiện bậc nhất ở mục 5.

### 7.1 Điều khiển một bước là QP khi mô hình tuyến tính

Giả sử trạng thái hiện tại $s$ đã biết, hành động cần chọn là $u$, và trạng thái tiếp theo được mô hình hóa bằng $s^+=Fs+Bu$. Muốn gần trạng thái đích $r$ mà không dùng hành động quá lớn, chọn

$$\min_u\frac12\|Fs+Bu-r\|_2^2+\frac\rho2\|u\|_2^2,\qquad\rho\ge0.$$

Các ma trận $F,B$, các vector $s,r$ và $\rho$ là dữ liệu; $u$ mới là biến. Đây là bình phương tối thiểu cộng điều chuẩn, có Hessian $B^TB+\rho I\succeq0$. Giới hạn $-u_{\max}\preceq u\preceq u_{\max}$ với $u_{\max}\succeq0$ là affine, nên giữ bài toán lồi. Nó chưa mô tả một hệ thực nếu mô hình chuyển trạng thái không phù hợp; đây là ví dụ tự biên soạn từ cấu trúc QP của sách.

Một chiều, đặt $s=2$, $F=B=1$, $r=0$, $\rho=1$, $|u|\le1$. Mục tiêu $\tfrac12(2+u)^2+\tfrac12u^2$ có đạo hàm $2+2u$, nên $u^*=-1$, $s^+=1$, giá trị 1. Hành động không đạt ngay đích vì có cả chi phí hành động và giới hạn.

### 7.2 Hồi quy logistic: xác suất không tuyến tính, loss vẫn lồi

Với nhãn $b_i\in\{0,1\}$, đặt điểm số $z_i=a_i^Tw$ và xác suất dự đoán

$$p_i=\sigma(z_i)=\frac1{1+e^{-z_i}}.$$

Ta giả định các nhãn độc lập có điều kiện theo đầu vào và tham số. Một nhãn có likelihood $p_i^{b_i}(1-p_i)^{1-b_i}$. Lấy âm log và rút gọn cho loss

$$\ell_i(w)=\log(1+e^{a_i^Tw})-b_i a_i^Tw.$$

Đạo hàm theo điểm số là $\sigma(z_i)-b_i$; đạo hàm bậc hai là $\sigma(z_i)(1-\sigma(z_i))\ge0$. Dùng quy tắc chuỗi qua điểm số affine:

$$\nabla\ell_i=(p_i-b_i)a_i,\qquad
\nabla^2\ell_i=p_i(1-p_i)a_ia_i^T\succeq0.$$

Tổng các loss lồi vẫn lồi. Phi tuyến của $\sigma$ theo điểm số không đồng nghĩa loss không lồi theo $w$. Bias có thể gộp vào $w$ bằng cách thêm một đặc trưng luôn bằng 1; nó vẫn đi vào điểm số theo dạng affine.

Ví dụ tự đặt một tham số với $(a,b)=(-1,0),(1,1)$. Tại $w=0$, mỗi xác suất bằng $1/2$, tổng loss $2\log2\approx1.38629$, gradient tổng $-1$, Hessian $1/2$. Tăng $w$ tách hai nhãn rõ hơn. Nhưng loss $2\log(1+e^{-w})$ chỉ tiến về 0 khi $w\to+\infty$, không đạt nghiệm hữu hạn. Dữ liệu tách được cho thấy một bài lồi vẫn có thể không đạt nghiệm; thêm điều chuẩn dương sửa mô hình và tạo độ cong dương.

```python
import math

def logistic_loss_gradient_hessian(w, data):
    loss = gradient = hessian = 0.0
    for a, b in data:
        z = a*w
        p = 1/(1+math.exp(-z)) if z >= 0 else math.exp(z)/(1+math.exp(z))
        # softplus ổn định: tránh tính exp(z) khi z quá lớn
        loss += max(z, 0)+math.log1p(math.exp(-abs(z)))-b*z
        gradient += (p-b)*a
        hessian += p*(1-p)*a*a
    return loss, gradient, hessian

print(logistic_loss_gradient_hessian(0, [(-1, 0), (1, 1)]))
# (1.3862943611198906, -1.0, 0.5)
```

## Bài tập tự luyện

::: exercise 1. Chứng minh một miền
Chứng minh $C=\{(x,y):x+y\le3,\ x\ge0,\ y\ge0\}$ lồi. Có cần vẽ hình để chứng minh không?
:::
::: solution
Mỗi điều kiện là một nửa không gian: $x+y\le3$, $-x\le0$, $-y\le0$. Giao ba tập lồi là lồi. Hình giúp nhìn miền nhưng không cần cho chứng minh.
:::

::: exercise 2. Tách miền khỏi hàm
$f(x)=x^2$; miền khả thi $C=\{-1,1\}$. Đây có phải cực tiểu một hàm lồi trên miền lồi không?
:::
::: solution
Không. Hàm lồi trên $\mathbb R$, nhưng $C$ không lồi vì thiếu trung điểm 0. Hai điểm khả thi đều tối ưu với giá trị 1; không được áp dụng kết quả duy nhất dựa trên miền lồi.
:::

::: exercise 3. Chứng nhận tại biên
Giải $\min(x-3)^2$ với $x\le2$ bằng điều kiện bậc nhất trên miền.
:::
::: solution
Chọn $x^*=2$, $f'(2)=-2$. Với mọi $y\le2$, $-2(y-2)\ge0$. Hàm lồi và miền lồi nên điều kiện đủ; giá trị tối ưu là 1. Không đặt $f'(x)=0$ rồi chấp nhận $x=3$, vì điểm ấy không khả thi.
:::

## Tóm tắt

Miền lồi cho phép pha các điểm khả thi; hàm lồi kiểm soát giá trị sau khi pha. Hai điều kiện cùng tạo chứng nhận tối ưu toàn cục. Gradient bằng 0 chỉ là trường hợp không ràng buộc; tại biên phải kiểm các hướng khả thi. Tính duy nhất cần thêm điều kiện, và sự tồn tại vẫn phải xét riêng.

## Nguồn và đọc thêm

- Nguồn chính: *Convex Optimization*, chương 1, §2.1–2.3, §3.1–3.2, §4.2.2–4.2.3 (tr. 138–140), §4.4 về QP và §7.1 về hồi quy logistic (tr. 354–355). Định nghĩa và điều kiện được đối chiếu với bản PDF local.
- Hình 2.1 (tr. 22) và Hình 3.1 (tr. 67) được mô phỏng bằng code với tọa độ/hàm tự đặt; không sao chép ảnh hay văn bản hình.
- [Hình học tập lồi bổ sung](../doc-them/hinh-hoc-tap-loi.md): ellipsoid, nón, phối cảnh, siêu phẳng và thứ tự Pareto, nguồn chương 2.
- Các ví dụ số, phản ví dụ hai tầng và bài tập được tự biên soạn. Mục lục lecture theo trang môn; nội dung không lấy từ trang đó.

[Bài 00](./bai-00-on-tap-nen-tang.md) · [Bài 02 — Các bài toán tối ưu lồi](./bai-02-tap-loi.md).
