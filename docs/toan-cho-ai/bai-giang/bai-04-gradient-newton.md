---
course: toan-cho-ai
lecture: bai-04-gradient-newton
section: lecture
title: "Tối ưu không ràng buộc và ràng buộc đẳng thức"
prerequisites: ["gradient", "hessian", "ma-tran-psd", "he-phuong-trinh", "kkt"]
lessonStatus: ready
description: "Tách hướng khỏi độ dài bước, thực hiện phương pháp gradient và Newton, rồi lập hệ Newton–KKT và đánh giá phần dư."
---

Các bài trước cho ta điều kiện để nhận biết nghiệm tối ưu. Bài này chuyển sang câu hỏi tính toán: bắt đầu từ một điểm cho trước, làm thế nào tạo ra một dãy điểm tiến dần tới nghiệm? Mỗi lần cập nhật phải giải quyết ba việc riêng: chọn hướng, chọn độ dài bước và quyết định khi nào dừng. Dù đôi khi được viết trong một dòng mã, ba việc này dựa trên những lập luận khác nhau.

Ví dụ xuyên suốt tự đặt là $f(x,y)=\tfrac12(x^2+10y^2)$, khởi đầu $(2,2)$. Độ cong theo $y$ gấp 10 lần theo $x$, nên nó giúp nhìn rõ vì sao một tốc độ học chung có thể khó chọn.

Sau khi học xong, bạn sẽ theo dõi được từng bước của phương pháp gradient, tự thực hiện tìm kiếm bước bằng backtracking, tính hướng Newton bằng cách giải hệ tuyến tính, và lập hệ Newton–KKT cho bài toán có ràng buộc đẳng thức. Lần đọc đầu nên dừng sau mục 3. Mục 4 về self-concordance và mục 5–6 về ràng buộc có thể học trong một lượt riêng.

## 1. Hướng giảm và độ dài bước

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

Mô phỏng tái hiện cơ chế đường đồng mức và phép cập nhật ở §9.3 bằng một hàm toàn phương tự đặt. Với $\kappa=10$, lần lượt thử $\eta=0.15$, $0.20$ và $0.25$. Hãy quan sát từng tọa độ cùng giá trị hàm mục tiêu; các điểm vượt ra ngoài vùng vẽ được báo riêng.

Trong mô hình này,

$$x_{k+1}=(1-\eta)x_k,\qquad y_{k+1}=(1-10\eta)y_k.$$

Để mọi điểm đầu đều hội tụ về 0, cả hai hệ số phải có trị tuyệt đối nhỏ hơn 1: $0<\eta<0.2$. Tại $\eta=0.2$, tọa độ $y$ đổi dấu nhưng giữ độ lớn. Đây là kết luận của ví dụ, không phải tốc độ học dùng chung cho mọi hàm.

## 2. Tìm kiếm bước bằng backtracking

Chọn $0<\alpha<1/2$, $0<\beta<1$. Bắt đầu $t=1$, rồi lặp $t\leftarrow\beta t$ cho tới khi điểm mới nằm trong miền và

$$f(z+td)\le f(z)+\alpha t\nabla f(z)^Td.$$

Vế phải yêu cầu bước thử đạt được một phần $\alpha$ của mức giảm do mô hình bậc nhất dự đoán. Vì $\nabla f^Td<0$, vế phải nhỏ hơn giá trị hiện tại. Tính khả vi và điều kiện hướng giảm bảo đảm bất đẳng thức sẽ đúng khi $t$ đủ nhỏ. Nếu hàm chứa log hoặc phép chia, trước hết phải xác nhận điểm thử vẫn nằm trong miền xác định.

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

<details><summary>Thử trả lời: Nếu điểm thử nằm ngoài miền xác định của log, có thể tính giá trị hàm mục tiêu trước không?</summary>

Không. Trước hết phải xét điều kiện miền; nếu điểm thử không hợp lệ thì thu nhỏ bước, rồi mới tính giá trị hàm mục tiêu. Đoạn mã trên dùng thứ tự đánh giá ngắn mạch để tránh gọi $f$ tại một điểm ngoài miền xác định.

</details>

## 3. Phương pháp Newton và mô hình bậc hai

Đặt $g=\nabla f(z)$, $H=\nabla^2f(z)$. Mô hình bậc hai theo độ dời $d$ là

$$q(d)=f(z)+g^Td+\frac12d^THd.$$

Nếu $H\succ0$, cực tiểu mô hình có đạo hàm $g+Hd=0$. Ta **giải hệ**

$$\boxed{Hd=-g.}$$

Viết $d=-H^{-1}g$ giúp diễn giải, nhưng khi lập trình nên giải hệ. Vì $H^{-1}\succ0$, $g^Td=-g^TH^{-1}g<0$ khi $g\ne0$, nên đây là hướng giảm. Sau đó vẫn cần tìm kiếm bước nếu hàm gốc khác mô hình toàn phương.

::: example Một bước cho hàm toàn phương
Với $H=\operatorname{diag}(1,10)$, $g=(2,20)$, Newton cho $d=(-2,-2)$. Bước đầy đủ đến $(0,0)$, giá trị 0. Nó chia ảnh hưởng gradient theo độ cong của từng hướng.

Chọn Newton trong mô phỏng để thấy đường đi. Kết quả một bước là do Hessian hằng và mô hình toàn phương chính xác; không khái quát nó cho mọi hàm.
:::

Nếu $H$ suy biến, hệ có thể không có nghiệm duy nhất. Nếu $H$ bất định, hướng thu được từ hệ có thể làm hàm tăng. Ngoài bài toán lồi, việc thêm $\rho I$ để hiệu chỉnh độ cong là một lựa chọn của thuật toán; thao tác này không chứng minh rằng hàm mất mát ban đầu là lồi.

### 3.1 Tiêu chí dừng

Chuẩn gradient nhỏ cho biết phần dư của điều kiện dừng nhỏ; nó chưa tự cho một khoảng cách nhỏ tới nghiệm. Muốn suy ra cận sai số mục tiêu cần thêm thông tin. **Lồi mạnh** với hằng số $m>0$ nghĩa là, trên miền đang xét,

$$f(y)\ge f(z)+\nabla f(z)^T(y-z)+\frac m2\|y-z\|_2^2.$$

Hàm bị ép nằm trên xấp xỉ bậc nhất thêm một bình phương có độ cong tối thiểu $m$. Với bài không ràng buộc có nghiệm, cực tiểu vế phải theo $y$ cho $f(z)-p^*\le\|g\|_2^2/(2m)$. Nếu không biết $m$, không biến chuẩn gradient thành một cận số chắc chắn. Hàm minh họa có Hessian $\operatorname{diag}(1,10)$ nên có thể lấy $m=1$.

Newton dùng **Newton decrement** $\lambda(z)=\sqrt{g^TH^{-1}g}$ khi $H\succ0$. Số $\lambda^2/2$ là mức giảm của mô hình toàn phương. Nó gần sai số thật khi mô hình tốt; các bảo đảm toàn cục cần những giả thiết như ở mục tiếp theo.

## 4. Hàm tự tương hợp (self-concordant)

Theo thuật ngữ của sách, hàm lồi một biến ba lần khả vi là **tự tương hợp** (self-concordant) nếu

$$|f'''(x)|\le2[f''(x)]^{3/2}\quad\forall x\in\operatorname{dom}f.$$

Vế trái đo độ cong thay đổi nhanh đến đâu; vế phải so nó với thang độ cong tại chính điểm ấy. Trong nhiều chiều, yêu cầu này áp dụng cho hàm $t\mapsto f(z+tv)$ trên mọi đường trong miền.

Ví dụ $f(x)=-\log x$, $x>0$, có $f''=1/x^2$ và $f'''=-2/x^3$. Hai vế cùng bằng $2/x^3$. Hàm toàn phương lồi cũng thỏa vì đạo hàm bậc ba bằng 0.

Điều kiện này phục vụ phân tích Newton mà không dựa vào các hằng số độ cong toàn cục trong hệ tọa độ hiện tại. Nó không nói mọi hàm lồi đều thỏa. Phần này chỉ giữ định nghĩa và một ví dụ; các cận số vòng lặp chi tiết ở §9.6.3–9.6.4 phù hợp cho lần đọc sau, khi bạn đã tự chạy được thuật toán.

## 5. Hướng Newton khi có ràng buộc đẳng thức

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

## 6. Bước Newton–KKT từ một điểm chưa khả thi

Đặt $r_{\mathrm{pri}}=Az-b$, $r_{\mathrm{dual}}=\nabla f(z)+A^T\nu$. Muốn cả hai bằng 0, tuyến tính hóa hệ và giải

$$\begin{bmatrix}H&A^T\\A&0\end{bmatrix}
\begin{bmatrix}d\\\Delta\nu\end{bmatrix}
=-\begin{bmatrix}r_{\mathrm{dual}}\\r_{\mathrm{pri}}\end{bmatrix}.$$

Khối dưới khác 0 sửa vi phạm đẳng thức. Sau bước đầy đủ, $A(z+d)-b=0$ vì đẳng thức tuyến tính; với bước thu nhỏ $t$, phần dư gốc là $(1-t)r_{\mathrm{pri}}$.

Ở khởi đầu chưa khả thi, Newton–KKT không nhất thiết giảm mục tiêu. Ví dụ khởi đầu $(2,0)$ có $f=0$ nhưng vi phạm $x+y=1$. Với $\nu=0$, bước $d=(-1/2,-1/2)$, $\Delta\nu=1/2$ tới nghiệm khả thi có $f=1/4$. Mục tiêu tăng, nhưng chuẩn phần dư KKT giảm từ 1 về 0.

Vì thế, tìm kiếm bước trong trường hợp này dựa trên chuẩn của toàn bộ vector phần dư và đồng thời giữ điểm trong miền xác định. Không thể áp dụng máy móc yêu cầu “hàm mục tiêu phải giảm” vốn dùng cho phương pháp bắt đầu từ một điểm khả thi.

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
Gradient chỉ phản ánh hàm mục tiêu. Điểm ấy không thỏa đẳng thức vì $r_{\mathrm{pri}}=1$. Do đó phải xét cả phần dư khả thi và phần dư của điều kiện dừng. Đây là lý do bài toán có ràng buộc cần tiêu chí dừng khác bài toán không ràng buộc.
:::

## Tóm tắt

Gradient cung cấp một hướng giảm cục bộ, còn tìm kiếm bước chọn độ dài di chuyển theo hướng đó. Phương pháp Newton dùng thêm mô hình bậc hai để điều chỉnh hướng theo độ cong. Khi có ràng buộc đẳng thức, hướng phải nằm trong không gian thỏa $Ad=0$, từ đó xuất hiện hệ Newton–KKT. Nếu điểm hiện tại chưa khả thi, mức tiến bộ được đo bằng phần dư của cả hệ chứ không chỉ bằng giá trị hàm mục tiêu. Mọi kết luận hội tụ đều phụ thuộc vào các giả thiết cụ thể đã nêu.

## Nguồn và đọc thêm

- *Convex Optimization*, §9.2–9.3 (tr. 463–474), §9.5 (tr. 484–495), §9.6 (tr. 496–507), §10.2–10.3 (tr. 525–541).
- Mô phỏng dùng hàm toàn phương tự đặt để tái hiện cơ chế hình đường đồng mức trong chương 9; bảng backtracking tái hiện quy tắc của Hình 9.1. Code không chép hình nguồn.
- Cận theo lồi mạnh: §9.1.2, biểu thức (9.9). Hệ Newton–KKT đối chiếu biểu thức (10.11) và (10.21).

[Bài 03](./bai-03-doi-ngau-lagrange.md) · [Bài 05 — Tối ưu huấn luyện](./bai-05-toi-uu-huan-luyen.md).
