---
course: toan-cho-ai
lecture: bai-04-gradient-newton
section: lecture
title: "Tối ưu không ràng buộc và ràng buộc đẳng thức"
prerequisites: ["gradient", "hessian", "ma-tran-psd", "he-phuong-trinh", "kkt"]
lessonStatus: ready
description: "Tách hướng và độ dài bước, chạy gradient và Newton, lập hệ Newton–KKT và kiểm phần dư."
---

Các bài trước cho điều kiện nghiệm; bài này tìm cách đi tới nghiệm bằng một dãy cập nhật. Ta phải chọn hướng, chọn độ dài bước và kiểm tiêu chí dừng. Ba quyết định ấy cần được phân biệt ngay cả khi chúng nằm trong một dòng code.

Ví dụ xuyên suốt tự đặt là $f(x,y)=\tfrac12(x^2+10y^2)$, khởi đầu $(2,2)$. Độ cong theo $y$ gấp 10 lần theo $x$, nên nó giúp nhìn rõ vì sao một tốc độ học chung có thể khó chọn.

Sau bài, bạn có thể truy vết gradient, tự thực hiện backtracking, tính bước Newton bằng giải hệ, và lập hệ cập nhật khi có đẳng thức. Đọc mục 1–3 trước; mục 4 về tự tương hợp và mục 5–6 về ràng buộc là hai cụm học tiếp riêng.

## 1. Hướng giảm không quyết định toàn bộ bước

Gọi điểm hiện tại là $z\in\mathbb R^n$, hướng là $d$ và hệ số bước là $t>0$:

$$z^+=z+td.$$

Đạo hàm theo đường $t\mapsto f(z+td)$ tại 0 là $\nabla f(z)^Td$. Nếu nó âm, $d$ là **hướng giảm**: một bước đủ nhỏ theo hướng ấy làm $f$ giảm. Độ dời thật là $td$; độ dài Euclid là $t\|d\|_2$, không phải $t$ trừ khi $d$ là vector đơn vị.

Gradient descent dùng $d=-\nabla f(z)$. Khi gradient khác 0, tích vô hướng bằng $-\|\nabla f(z)\|_2^2<0$. Tuy nhiên kết luận này chỉ đảm bảo các bước đủ nhỏ.

::: example Bước lớn làm hàm tăng
Tại $(2,2)$, $f=22$, $g=(2,20)$, $d=(-2,-20)$. Chọn $t=1$ đến $(0,-18)$, cho $f=1620$. Hướng giảm nhưng bước quá dài.

Chọn $t=0.15$ đến $(1.7,-1)$, cho $f=6.445$. Vẫn cùng một hướng, độ dài bước khác cho kết quả khác.
:::

<MathLab type="optimizer" initial-method="gd">

```js
const gradient = ([x,y], kappa) => [x, kappa*y];
const next = point.map((x,i) => x-rate*gradient(point,kappa)[i]);
```

</MathLab>

Mô phỏng tái hiện cơ chế đường đồng mức và cập nhật ở §9.3 bằng một hàm toàn phương tự đặt. Với $\kappa=10$, thử $\eta=0.15$, rồi $0.20$, rồi $0.25$. Quan sát từng tọa độ và loss; các điểm vượt vùng vẽ được báo riêng.

Trong mô hình này,

$$x_{k+1}=(1-\eta)x_k,\qquad y_{k+1}=(1-10\eta)y_k.$$

Để mọi điểm đầu đều hội tụ về 0, cả hai hệ số phải có trị tuyệt đối nhỏ hơn 1: $0<\eta<0.2$. Tại $\eta=0.2$, tọa độ $y$ đổi dấu nhưng giữ độ lớn. Đây là kết luận của ví dụ, không phải tốc độ học dùng chung cho mọi hàm.

## 2. Backtracking: giảm bước đến khi có bằng chứng

Chọn $0<\alpha<1/2$, $0<\beta<1$. Bắt đầu $t=1$, rồi lặp $t\leftarrow\beta t$ cho tới khi điểm mới nằm trong miền và

$$f(z+td)\le f(z)+\alpha t\nabla f(z)^Td.$$

Vế phải yêu cầu một phần $\alpha$ của mức giảm mà mô hình bậc nhất dự đoán. Vì $\nabla f^Td<0$, nó thấp hơn giá trị hiện tại. Hướng giảm và tính khả vi đảm bảo bất đẳng thức đúng khi $t$ đủ nhỏ; phải kiểm miền trước nếu có log hoặc phép chia.

::: example Theo dõi quá trình thu nhỏ
Ở điểm $(2,2)$, lấy $\alpha=0.1$, $\beta=0.5$. Tích $g^Td=-404$.

| $t$ | Điểm thử | $f$ mới | Cận cần thỏa $22-40.4t$ | Chấp nhận? |
| ---: | --- | ---: | ---: | --- |
| 1 | $(0,-18)$ | 1620 | −18.4 | Không |
| 1/2 | $(1,-8)$ | 320.5 | 1.8 | Không |
| 1/4 | $(1.5,-3)$ | 46.125 | 11.9 | Không |
| 1/8 | $(1.75,-0.5)$ | 2.78125 | 16.95 | Có |

Ta thu được $t=1/8$. Bảng tự tính lại theo cùng công thức; nó mô phỏng điều kiện ở Hình 9.1, tr. 465, không dùng dữ liệu ảnh của sách.
:::

```python
def backtrack(f, z, g, d, in_domain=lambda z: True,
              alpha=0.1, beta=0.5):
    slope = sum(a*b for a, b in zip(g, d))
    if slope >= 0:
        raise ValueError("Cần một hướng giảm")
    t = 1.0
    for _ in range(100):  # bảo vệ số học hữu hạn
        trial = [a+t*b for a, b in zip(z, d)]
        if in_domain(trial) and f(trial) <= f(z)+alpha*t*slope:
            return t, trial
        t *= beta
    raise RuntimeError("Không tìm được bước trong giới hạn lặp")
```

Backtracking khác tìm kiếm chính xác: nó tìm một bước giảm đủ, không nhất thiết cực tiểu hàm trên đường đã chọn.

<details><summary>Tự kiểm: nếu điểm thử làm log không xác định, có so loss trước được không?</summary>

Không. Kiểm điều kiện miền trước, thu nhỏ bước nếu vi phạm, rồi mới tính loss. Code trên dùng thứ tự đánh giá ngắn mạch để tránh gọi $f$ tại điểm ngoài miền.

</details>

## 3. Newton: dùng độ cong để chọn hướng

Đặt $g=\nabla f(z)$, $H=\nabla^2f(z)$. Mô hình bậc hai theo độ dời $d$ là

$$q(d)=f(z)+g^Td+\frac12d^THd.$$

Nếu $H\succ0$, cực tiểu mô hình có đạo hàm $g+Hd=0$. Ta **giải hệ**

$$\boxed{Hd=-g.}$$

Viết $d=-H^{-1}g$ giúp diễn giải, nhưng khi lập trình nên giải hệ. Vì $H^{-1}\succ0$, $g^Td=-g^TH^{-1}g<0$ khi $g\ne0$, nên đây là hướng giảm. Sau đó vẫn cần tìm kiếm bước nếu hàm gốc khác mô hình toàn phương.

::: example Một bước cho hàm toàn phương
Với $H=\operatorname{diag}(1,10)$, $g=(2,20)$, Newton cho $d=(-2,-2)$. Bước đầy đủ đến $(0,0)$, giá trị 0. Nó chia ảnh hưởng gradient theo độ cong của từng hướng.

Chọn Newton trong mô phỏng để thấy đường đi. Kết quả một bước là do Hessian hằng và mô hình toàn phương chính xác; không khái quát nó cho mọi hàm.
:::

Nếu $H$ suy biến, hệ có thể không có nghiệm duy nhất. Nếu $H$ bất định, hướng giải hệ có thể tăng hàm. Ngoài miền lồi, việc thêm $\rho I$ để sửa độ cong là một lựa chọn thuật toán cần được kiểm tra, không phải chứng minh loss đã lồi.

### 3.1 Dừng bằng đại lượng nào?

Chuẩn gradient nhỏ cho biết phần dư của điều kiện dừng nhỏ; nó chưa tự cho một khoảng cách nhỏ tới nghiệm. Muốn suy ra cận sai số mục tiêu cần thêm thông tin. **Lồi mạnh** với hằng số $m>0$ nghĩa là, trên miền đang xét,

$$f(y)\ge f(z)+\nabla f(z)^T(y-z)+\frac m2\|y-z\|_2^2.$$

Hàm bị ép nằm trên xấp xỉ bậc nhất thêm một bình phương có độ cong tối thiểu $m$. Với bài không ràng buộc có nghiệm, cực tiểu vế phải theo $y$ cho $f(z)-p^*\le\|g\|_2^2/(2m)$. Nếu không biết $m$, không biến chuẩn gradient thành một cận số chắc chắn. Hàm minh họa có Hessian $\operatorname{diag}(1,10)$ nên có thể lấy $m=1$.

Newton dùng **Newton decrement** $\lambda(z)=\sqrt{g^TH^{-1}g}$ khi $H\succ0$. Số $\lambda^2/2$ là mức giảm của mô hình toàn phương. Nó gần sai số thật khi mô hình tốt; các bảo đảm toàn cục cần những giả thiết như ở mục tiếp theo.

## 4. Tự tương hợp: kiểm soát thay đổi của độ cong

Theo thuật ngữ của sách, hàm lồi một biến ba lần khả vi là **tự tương hợp** (self-concordant) nếu

$$|f'''(x)|\le2[f''(x)]^{3/2}\quad\forall x\in\operatorname{dom}f.$$

Vế trái đo độ cong thay đổi nhanh đến đâu; vế phải so nó với thang độ cong tại chính điểm ấy. Trong nhiều chiều, yêu cầu này áp dụng cho hàm $t\mapsto f(z+tv)$ trên mọi đường trong miền.

Ví dụ $f(x)=-\log x$, $x>0$, có $f''=1/x^2$ và $f'''=-2/x^3$. Hai vế cùng bằng $2/x^3$. Hàm toàn phương lồi cũng thỏa vì đạo hàm bậc ba bằng 0.

Điều kiện này phục vụ phân tích Newton mà không dựa vào các hằng số độ cong toàn cục trong hệ tọa độ hiện tại. Nó không nói mọi hàm lồi đều thỏa. Ta giữ định nghĩa và ví dụ trong tuyến chính; các cận số vòng lặp chi tiết nằm ở §9.6.3–9.6.4 để đọc sau khi đã chạy được thuật toán.

## 5. Có đẳng thức: hướng phải ở trong miền khả thi

Xét $\min f(z)$ với $Az=b$. Nếu $z$ đang khả thi, muốn $z+d$ khả thi thì $Ad=0$. Ta cực tiểu mô hình $q(d)$ dưới điều kiện này. KKT của bài con cho

$$\begin{bmatrix}H&A^T\\A&0\end{bmatrix}
\begin{bmatrix}d\\w\end{bmatrix}
=\begin{bmatrix}-g\\0\end{bmatrix}.$$

$w$ là nhân tử của bài con. Điều kiện đủ đơn giản để hệ khả nghịch là $H\succ0$ và $A$ đủ hạng hàng. Sách còn cho phép $H$ chỉ dương xác định trên các hướng thuộc không gian $Ad=0$.

::: example Hồi quy có một đẳng thức
Dùng bài ở Bài 03: $f(x,y)=\tfrac12[(x-2)^2+y^2]$, $x+y=1$. Khởi đầu khả thi $(1,0)$.

$H=I$, $g=(-1,0)$, $A=(1,1)$. Hệ gồm $d_x+w=1$, $d_y+w=0$, $d_x+d_y=0$. Suy ra $w=1/2$, $d=(1/2,-1/2)$. Cập nhật đến $(3/2,-1/2)$, đúng nghiệm đã chứng nhận.
:::

Hướng gradient thuần ở điểm này là $(1,0)$, không thỏa $Ad=0$. Cập nhật tùy ý theo nó sẽ phá đẳng thức. Ràng buộc phải tham gia cách chọn hướng.

## 6. Khởi đầu chưa khả thi: giảm phần dư KKT

Đặt $r_{\mathrm{pri}}=Az-b$, $r_{\mathrm{dual}}=\nabla f(z)+A^T\nu$. Muốn cả hai bằng 0, tuyến tính hóa hệ và giải

$$\begin{bmatrix}H&A^T\\A&0\end{bmatrix}
\begin{bmatrix}d\\\Delta\nu\end{bmatrix}
=-\begin{bmatrix}r_{\mathrm{dual}}\\r_{\mathrm{pri}}\end{bmatrix}.$$

Khối dưới khác 0 sửa vi phạm đẳng thức. Sau bước đầy đủ, $A(z+d)-b=0$ vì đẳng thức tuyến tính; với bước thu nhỏ $t$, phần dư gốc là $(1-t)r_{\mathrm{pri}}$.

Ở khởi đầu chưa khả thi, Newton–KKT không nhất thiết giảm mục tiêu. Ví dụ khởi đầu $(2,0)$ có $f=0$ nhưng vi phạm $x+y=1$. Với $\nu=0$, bước $d=(-1/2,-1/2)$, $\Delta\nu=1/2$ tới nghiệm khả thi có $f=1/4$. Mục tiêu tăng, nhưng chuẩn phần dư KKT giảm từ 1 về 0.

Vì thế tìm kiếm bước của phương pháp này dùng chuẩn phần dư chung, đồng thời giữ điểm trong miền xác định. Không áp dụng máy móc phép kiểm “loss phải giảm” của phương pháp khởi đầu khả thi.

## Bài tập tự luyện

::: exercise 1. Khoảng bước
Với $f(x,y)=\tfrac12(2x^2+8y^2)$, tìm khoảng tốc độ học cố định để gradient hội tụ từ mọi điểm đầu.
:::
::: solution
Hai hệ số cập nhật là $1-2\eta$ và $1-8\eta$. Điều kiện trị tuyệt đối nhỏ hơn 1 cho $0<\eta<1$ và $0<\eta<1/4$. Giao là $0<\eta<1/4$.
:::

::: exercise 2. Newton một chiều
$f(x)=x^4+x^2$, điểm hiện tại $x=1$. Tính hướng Newton và giá trị sau bước đầy đủ. Có tới ngay nghiệm không?
:::
::: solution
$g=6$, $H=14$, $d=-3/7$, $x^+=4/7$. Giá trị mới $1040/2401\approx0.43315$, nhỏ hơn $f(1)=2$ nhưng chưa bằng 0. Hàm không toàn phương; không có bảo đảm một bước tới nghiệm.
:::

::: exercise 3. Phần dư tại điểm chưa khả thi
Trong mục 6, vì sao chuẩn gradient ở $(2,0)$ bằng 0 mà vẫn chưa thể dừng?
:::
::: solution
Gradient chỉ xét mục tiêu. Điểm ấy không thỏa đẳng thức: $r_{\mathrm{pri}}=1$. Phải kiểm cả phần dư gốc lẫn phần dư dừng. Đây là lý do tiêu chí dừng của bài ràng buộc khác bài không ràng buộc.
:::

## Tóm tắt

Gradient cho hướng giảm, tìm kiếm bước chọn hệ số, Newton dùng mô hình độ cong. Đẳng thức đổi không gian hướng và dẫn đến hệ KKT. Với điểm chưa khả thi, đo tiến bộ bằng phần dư của cả hệ thay vì chỉ loss. Mỗi bảo đảm hội tụ cần những điều kiện tương ứng, không đến từ tên thuật toán.

## Nguồn và đọc thêm

- *Convex Optimization*, §9.2–9.3 (tr. 463–474), §9.5 (tr. 484–495), §9.6 (tr. 496–507), §10.2–10.3 (tr. 525–541).
- Mô phỏng dùng hàm toàn phương tự đặt để tái hiện cơ chế hình đường đồng mức trong chương 9; bảng backtracking tái hiện quy tắc của Hình 9.1. Code không chép hình nguồn.
- Cận theo lồi mạnh: §9.1.2, biểu thức (9.9). Hệ Newton–KKT đối chiếu biểu thức (10.11) và (10.21).

[Bài 03](./bai-03-doi-ngau-lagrange.md) · [Bài 05 — Tối ưu huấn luyện](./bai-05-toi-uu-huan-luyen.md).
