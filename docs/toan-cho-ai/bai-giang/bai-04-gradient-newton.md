---
course: toan-cho-ai
lecture: bai-04-gradient-newton
section: lecture
title: "Tối ưu không ràng buộc và ràng buộc đẳng thức"
prerequisites: ["gradient", "hessian", "ma-tran-psd", "he-phuong-trinh", "kkt"]
lessonStatus: ready
description: "Tách hướng khỏi độ dài bước, thực hiện phương pháp gradient và Newton, rồi lập hệ Newton–KKT và đánh giá phần dư."
---

Các bài học trước đã trang bị cho chúng ta hệ thống điều kiện toán học để nhận diện và chứng nhận một nghiệm tối ưu. Bài học này chuyển giao trọng tâm từ lý thuyết nhận diện sang câu hỏi thuật toán tính toán: Bắt đầu từ một điểm khởi tạo bất kỳ trong không gian, làm thế nào để xây dựng một dãy điểm lặp hội tụ nhanh chóng và vững chắc về nghiệm tối ưu toàn cục?

Quá trình tìm đường trong không gian tối ưu hóa đòi hỏi thuật toán phải đưa ra ba quyết định độc lập tại mỗi bước lặp:
1. **Chọn hướng di chuyển** (Descent Direction): Đi theo vector nào để hàm mục tiêu suy giảm?
2. **Chọn độ dài bước** (Step Size / Learning Rate): Di chuyển bao xa theo hướng đã chọn để không bị vọt qua đáy thung lũng?
3. **Tiêu chí dừng** (Stopping Criteria): Khi nào mức độ tiệm cận nghiệm đã đủ tin cậy để dừng tính toán?

Để quan sát sâu sắc cơ chế này, chúng ta sẽ khảo sát xuyên suốt hàm mục tiêu toàn phương hai chiều:
$$
f(x, y) = \frac{1}{2}(x^2 + 10y^2),
$$
với điểm khởi tạo tại $(2, 2)$. Độ cong địa hình theo phương $y$ gấp đúng 10 lần theo phương $x$, tạo nên một "hẻm núi hẹp" (ill-conditioned ravine) điển hình — nơi bộc lộ toàn bộ điểm mạnh và điểm yếu của các thuật toán tối ưu.

---

## 1. Hướng giảm và Độ dài bước di chuyển

Tại điểm hiện tại $z \in \mathbb{R}^n$, thuật toán cập nhật vị trí mới theo quy tắc:

$$
z^+ = z + t d,
$$

trong đó $d \in \mathbb{R}^n$ là vector hướng di chuyển và $t > 0$ là độ dài bước (hệ số bước).

Đạo hàm định hướng của hàm số $f$ dọc theo tia $t \mapsto f(z + td)$ tại $t = 0$ được tính bằng tích vô hướng $\nabla f(z)^T d$. Một vector $d$ được gọi là **hướng giảm** (descent direction) nếu tích vô hướng này âm:

$$
\nabla f(z)^T d < 0.
$$

Khi điều kiện này thỏa mãn, giải tích bảo đảm rằng luôn tồn tại một bước nhảy $t > 0$ đủ nhỏ sao cho $f(z + td) < f(z)$. Cần phân biệt rõ: độ dời thực tế trong không gian là vector $td$, và khoảng cách hình học di chuyển là $t\|d\|_2$.

Thuật toán **Gradient Descent** (Phương pháp dốc đứng) lựa chọn hướng di chuyển trực tiếp ngược chiều gradient: $d = -\nabla f(z)$. Khi gradient khác 0, ta có:

$$
\nabla f(z)^T d = -\|\nabla f(z)\|_2^2 < 0.
$$

Do đó, ngược chiều gradient luôn là một hướng giảm hợp lệ. Tuy nhiên, định lý giải tích chỉ bảo đảm hàm số giảm khi bước nhảy $t$ "đủ nhỏ". Nếu bước nhảy quá dài, hàm số hoàn toàn có thể bùng nổ mất kiểm soát.

::: example Bước nhảy quá trớn trong hẻm núi hẹp
Tại điểm khởi đầu $(2, 2)$, giá trị hàm mục tiêu là $f(2, 2) = \frac{1}{2}(2^2 + 10 \cdot 2^2) = 22$.
Vector gradient là $\nabla f(2, 2) = (2, 20)^T$, do đó hướng gradient descent là $d = (-2, -20)^T$.
- Nếu chọn bước nhảy dài $t = 1$: Điểm mới là $z^+ = (2 - 2, 2 - 20) = (0, -18)$. Giá trị mất mát mới vọt lên $f(0, -18) = \frac{1}{2}(0 + 10 \cdot 18^2) = 1620$. Hướng đi hoàn toàn đúng, nhưng bước nhảy quá trớn đã khiến thuật toán rơi vào thảm họa phân kỳ!
- Nếu chọn bước nhảy cẩn trọng $t = 0.15$: Điểm mới là $z^+ = (2 - 0.3, 2 - 3.0) = (1.7, -1.0)$. Giá trị mất mát giảm xuống còn $f(1.7, -1.0) = \frac{1}{2}(1.7^2 + 10 \cdot (-1)^2) = 6.445 < 22$.
:::

<MathLab type="optimizer" initial-method="gd">

```js
const gradient = ([x,y], kappa) => [x, kappa*y];
const next = point.map((x,i) => x-rate*gradient(point,kappa)[i]);
```

</MathLab>

Xét phương trình cập nhật từng tọa độ với tốc độ học cố định $\eta > 0$:

$$
x_{k+1} = (1 - \eta) x_k, \qquad y_{k+1} = (1 - 10\eta) y_k.
$$

Để chuỗi điểm lặp hội tụ về gốc tọa độ $(0, 0)$, cả hai hệ số co giãn đều phải có trị tuyệt đối nhỏ hơn 1:
$$
|1 - \eta| < 1 \iff 0 < \eta < 2, \qquad |1 - 10\eta| < 1 \iff 0 < \eta < 0.2.
$$

Giao của hai điều kiện đòi hỏi bước nhảy bắt buộc phải thỏa mãn $0 < \eta < 0.2$. Giới hạn này bị quyết định hoàn toàn bởi phương có độ cong lớn nhất ($\lambda_{\max} = 10$). Nếu chọn $\eta = 0.2$, tọa độ $y$ sẽ dao động đổi dấu vĩnh viễn giữa $2$ và $-2$ mà không bao giờ suy giảm.

---

## 2. Tìm kiếm bước bằng thuật toán Backtracking

Trong thực tế tính toán, việc dò tìm độ dài bước tối ưu chính xác (exact line search) đòi hỏi giải một bài toán tối ưu phụ một chiều rất tốn kém. Thay vào đó, kỹ thuật **Backtracking Line Search** (dựa trên điều kiện Armijo) tìm kiếm một bước nhảy "đủ tốt" một cách nhanh chóng.

Thuật toán chọn hai tham số: $\alpha \in (0, 0.5)$ (hệ số giảm chấp nhận được) và $\beta \in (0, 1)$ (hệ số thu nhỏ bước). Bắt đầu với bước thử tối đa $t = 1$, ta liên tục co ngắn bước $t \leftarrow \beta t$ cho tới khi điểm thử nằm trong miền xác định và thỏa mãn **điều kiện Armijo**:

$$
f(z + t d) \le f(z) + \alpha t \nabla f(z)^T d.
$$

Ý nghĩa của bất đẳng thức: Vì $\nabla f(z)^T d < 0$, vế phải là đường thẳng xấp xỉ bậc nhất nghiêng xuống nhưng có độ dốc chỉ bằng một phần $\alpha$ so với độ dốc thực tế. Điều kiện yêu cầu hàm mục tiêu phải thực sự giảm ít nhất một tỷ lệ $\alpha$ so với mức giảm kỳ vọng tuyến tính.

::: example Quá trình co bước Backtracking từng nấc
Tại điểm $z = (2, 2)$, chọn $\alpha = 0.1$ và $\beta = 0.5$. Tích vô hướng độ dốc là $g^T d = 2(-2) + 20(-20) = -404$.
Ngưỡng chấp nhận Armijo là: $f(z) + \alpha t (g^T d) = 22 - 40.4 t$.

| Bước thử $t$ | Điểm thử nghiệm | $f(z + td)$ | Ngưỡng Armijo $22 - 40.4t$ | Quyết định |
| :---: | :---: | :---: | :---: | :---: |
| $1$ | $(0, -18)$ | $1620$ | $-18.4$ | Từ chối |
| $1/2$ | $(1, -8)$ | $320.5$ | $1.8$ | Từ chối |
| $1/4$ | $(1.5, -3)$ | $46.125$ | $11.9$ | Từ chối |
| $1/8$ | $(1.75, -0.5)$ | $2.78125$ | $16.95$ | **Chấp nhận** |

Tại $t = 1/8$, giá trị thực tế $2.78125$ thấp hơn hẳn ngưỡng $16.95$, thuật toán dừng tìm kiếm và chọn độ dài bước $t = 1/8$.
:::

Đoạn mã Python hiện thực hóa giải thuật Backtracking chuẩn xác:

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

<details><summary>Câu hỏi đào sâu: Nếu hàm mục tiêu chứa logarit (như hàm rào cản nội thất), điều gì xảy ra nếu điểm thử nghiệm rơi ra ngoài miền xác định?</summary>

Nếu điểm thử nghiệm $z + td$ rơi ra ngoài miền xác định ($\operatorname{dom} f$), biểu thức $f(trial)$ sẽ sinh ra lỗi toán học (như $\log(x)$ với $x \le 0$). Do đó, điều kiện kiểm tra miền `in_domain(trial)` bắt buộc phải được đánh giá trước bằng toán tử ngắn mạch (short-circuit evaluation). Nếu điểm thử không thuộc miền xác định, thuật toán phải co ngắn bước $t$ ngay lập tức mà không cố gắng tính toán giá trị hàm mục tiêu.

</details>

---

## 3. Phương pháp Newton và Mô hình xấp xỉ bậc hai

Tại sao Gradient Descent thường di chuyển ziczac rất chậm chạp trong các hẻm núi hẹp? Vì Gradient Descent là một phương pháp bậc nhất: nó coi địa hình mọi hướng đều dốc phẳng như nhau và hoàn toàn mù tịt về độ cong.

**Phương pháp Newton** khắc phục triệt để nhược điểm này bằng cách sử dụng thông tin độ cong của ma trận Hessian $H = \nabla^2 f(z)$. Tại điểm hiện tại, phương pháp Newton dựng một mô hình xấp xỉ Taylor bậc hai theo vector độ dời $d$:

$$
q(d) = f(z) + g^T d + \frac{1}{2} d^T H d,
$$

trong đó $g = \nabla f(z)$ và $H = \nabla^2 f(z) \succ 0$.

Để tìm cực tiểu của chiếc paraboloid xấp xỉ này, ta lấy đạo hàm theo $d$ và cho triệt tiêu:

$$
\nabla_d q(d) = g + H d = 0 \iff \boxed{H d = -g.}
$$

Vector nghiệm $d = -H^{-1} g$ được gọi là **hướng Newton** (Newton step). Trong cài đặt thuật toán số, ta không bao giờ đảo ma trận $H^{-1}$ mà luôn giải hệ phương trình tuyến tính $H d = -g$ bằng các phép phân rã Cholesky hoặc LU để bảo đảm tính ổn định số học.

Vì ma trận Hessian dương xác định ($H \succ 0$), ta có:

$$
g^T d = -g^T H^{-1} g < 0 \quad (\text{khi } g \ne 0).
$$

Điều này chứng minh hướng Newton luôn luôn là một hướng giảm hợp lệ!

::: example Sức mạnh vượt trội của bước Newton trên hàm toàn phương
Với hàm $f(x, y) = \frac{1}{2}(x^2 + 10y^2)$ tại điểm $(2, 2)$:
Ma trận Hessian là $H = \begin{bmatrix} 1 & 0 \\ 0 & 10 \end{bmatrix}$, vector gradient là $g = \begin{bmatrix} 2 \\ 20 \end{bmatrix}$.

Giải hệ phương trình Newton $Hd = -g$:
$$
\begin{bmatrix} 1 & 0 \\ 0 & 10 \end{bmatrix} \begin{bmatrix} d_x \\ d_y \end{bmatrix} = \begin{bmatrix} -2 \\ -20 \end{bmatrix} \implies \begin{bmatrix} d_x \\ d_y \end{bmatrix} = \begin{bmatrix} -2 \\ -2 \end{bmatrix}.
$$

Thực hiện bước cập nhật đầy đủ ($t = 1$):
$$
z^+ = \begin{bmatrix} 2 \\ 2 \end{bmatrix} + \begin{bmatrix} -2 \\ -2 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}.
$$

Chỉ đúng một bước duy nhất, phương pháp Newton đã nhảy thẳng tới nghiệm tối ưu toàn cục $(0, 0)$! Phương pháp Newton đã tự động chia nhỏ bước nhảy theo trục $y$ (chia cho 10) và giữ nguyên bước nhảy theo trục $x$ (chia cho 1), loại bỏ hoàn toàn hiện tượng dao động ziczac.
:::

### 3.1 Tiêu chí dừng và Đại lượng Newton Decrement
Trong phương pháp Newton, đại lượng **Newton decrement** được định nghĩa là:

$$
\lambda(z) = \sqrt{g^T H^{-1} g} = \sqrt{d^T H d}.
$$

Đại lượng này mang những ý nghĩa hình học và tính toán đặc biệt:
1. Số $\frac{\lambda(z)^2}{2}$ chính là mức độ suy giảm mục tiêu mà mô hình bậc hai dự đoán:
   $$f(z) - \inf_d q(d) = \frac{1}{2} \lambda(z)^2.$$
2. $\lambda(z)$ là một đại lượng **bất biến với phép đổi tọa độ affine** ($z = Ay$). Đây là ưu thế tuyệt đối của phương pháp Newton so với Gradient Descent (vốn phụ thuộc nặng nề vào hệ trục tọa độ).
3. Tiêu chí dừng tự nhiên: Khi $\frac{1}{2}\lambda(z)^2 \le \epsilon$, ta dừng thuật toán với bảo đảm chắc chắn rằng sai số mục tiêu không vượt quá $\epsilon$.

---

## 4. Hàm tự tương hợp (Self-concordant Functions)

Một thách thức kinh điển của giải tích tối ưu truyền thống là tốc độ hội tụ của phương pháp Newton thường phụ thuộc vào các hằng số độ cong không xác định trong từng hệ tọa độ. Yurii Nesterov và Arkadi Nemirovski đã giải quyết triệt để vấn đề này qua lý thuyết **Hàm tự tương hợp (Self-concordant Functions)**.

Một hàm lồi một biến khả vi ba lần được gọi là tự tương hợp nếu nó thỏa mãn bất đẳng thức:

$$
|f'''(x)| \le 2 [f''(x)]^{3/2} \quad \forall x \in \operatorname{dom} f.
$$

Vế trái đo lường tốc độ biến thiên của độ cong (đạo hàm bậc ba), còn vế phải là thang đo độ cong tại chính điểm khảo sát. Bất đẳng thức này phát biểu rằng: **độ cong của hàm số không được phép thay đổi quá đột ngột so với bản thân độ cong tại điểm đó**.

Đối với hàm nhiều biến, hàm $f$ được gọi là tự tương hợp nếu hàm một biến thu hẹp $t \mapsto f(z + tv)$ là tự tương hợp trên mọi đường thẳng đi qua miền xác định.
- Hàm toàn phương lồi là tự tương hợp vì đạo hàm bậc ba triệt tiêu: $f'''(x) = 0$.
- Hàm rào cản logarit $f(x) = -\log x$ với $x > 0$ là tự tương hợp:
  $$f''(x) = \frac{1}{x^2}, \quad f'''(x) = -\frac{2}{x^3} \implies |f'''(x)| = \frac{2}{x^3} = 2 \left(\frac{1}{x^2}\right)^{3/2} = 2 [f''(x)]^{3/2}.$$

Lý thuyết tự tương hợp bảo đảm rằng phương pháp Newton với backtracking sẽ hội tụ về nghiệm sau một số hữu hạn các bước lặp độc lập với hệ tọa độ, đặt nền móng lý thuyết vững chắc cho các thuật toán điểm trong (interior-point methods) hiện đại.

---

## 5. Hướng Newton khi có Ràng buộc Đẳng thức

Xét bài toán tối ưu với ràng buộc đẳng thức affine:

$$
\min_z \quad f(z) \quad \text{sao cho} \quad A z = b.
$$

Nếu điểm hiện tại $z$ đã khả thi ($Az = b$), thì để điểm mới $z + d$ tiếp tục khả thi, vector hướng di chuyển $d$ bắt buộc phải thỏa mãn:

$$
A(z + d) = b \iff A d = 0.
$$

Nghĩa là hướng di chuyển phải nằm trọn trong không gian hạch (null space) của ma trận ràng buộc $A$. Cực tiểu hóa mô hình bậc hai $q(d) = f(z) + g^T d + \frac{1}{2} d^T H d$ dưới điều kiện $Ad = 0$ dẫn đến hệ phương trình KKT:

$$
\boxed{\begin{bmatrix} H & A^T \\ A & 0 \end{bmatrix} \begin{bmatrix} d \\ w \end{bmatrix} = \begin{bmatrix} -g \\ 0 \end{bmatrix},}
$$

trong đó $w$ là vector nhân tử Lagrange gắn với ràng buộc đẳng thức của bài toán con bậc hai.

::: example Tìm bước Newton trên bài toán có ràng buộc đẳng thức
Xét bài toán: $\min \frac{1}{2}[(x - 2)^2 + y^2]$ với ràng buộc $x + y = 1$.
Giả sử ta xuất phát từ điểm khả thi $z = (1, 0)^T$ (thỏa mãn $1 + 0 = 1$).
Ma trận Hessian là $H = I$, gradient tại điểm này là $g = (1 - 2, 0)^T = (-1, 0)^T$, và ma trận ràng buộc $A = \begin{bmatrix} 1 & 1 \end{bmatrix}$.

Hệ phương trình Newton-KKT:
$$
\begin{bmatrix} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 1 & 1 & 0 \end{bmatrix} \begin{bmatrix} d_x \\ d_y \\ w \end{bmatrix} = \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix}.
$$

Giải hệ phương trình tuyến tính:
- $d_x + w = 1 \implies d_x = 1 - w$,
- $d_y + w = 0 \implies d_y = -w$,
- $d_x + d_y = 0 \implies (1 - w) - w = 0 \implies w = \frac{1}{2}$.

Suy ra hướng di chuyển: $d_x = \frac{1}{2}$, $d_y = -\frac{1}{2}$.
Thực hiện bước cập nhật đầy đủ:
$$
z^+ = \begin{bmatrix} 1 \\ 0 \end{bmatrix} + \begin{bmatrix} 1/2 \\ -1/2 \end{bmatrix} = \begin{bmatrix} 3/2 \\ -1/2 \end{bmatrix}.
$$

Điểm mới đạt đúng nghiệm tối ưu toàn cục đã được chứng minh ở Bài 03!
:::

---

## 6. Bước Newton–KKT từ một Điểm Khởi tạo Chưa Khả thi (Infeasible Start)

Nếu ta không có sẵn một điểm khả thi thỏa mãn $Az = b$ thì sao? Ta có thể bắt đầu thuật toán từ một điểm $z$ bất kỳ và để phương pháp Newton đồng thời giải quyết hai nhiệm vụ: **tiến tới nghiệm tối ưu** và **khắc phục sai số ràng buộc**.

Định nghĩa hai vector phần dư của hệ KKT:
- **Phần dư đối ngẫu** (Dual residual): $r_{\mathrm{dual}} = \nabla f(z) + A^T \nu$.
- **Phần dư gốc** (Primal residual): $r_{\mathrm{pri}} = A z - b$.

Tuyến tính hóa hệ phương trình KKT quanh điểm hiện tại $(z, \nu)$ dẫn tới hệ phương trình **Newton–KKT khởi tạo không khả thi**:

$$
\begin{bmatrix} H & A^T \\ A & 0 \end{bmatrix} \begin{bmatrix} d \\ \Delta\nu \end{bmatrix} = -\begin{bmatrix} r_{\mathrm{dual}} \\ r_{\mathrm{pri}} \end{bmatrix}.
$$

Khối phương trình phía dưới $Ad = -r_{\mathrm{pri}} = b - Az$ bảo đảm rằng sau một bước cập nhật đầy đủ ($t = 1$), điểm mới sẽ thỏa mãn ràng buộc đẳng thức một cách hoàn hảo:
$$
A(z + d) - b = Az + Ad - b = Az + (b - Az) - b = 0.
$$

Lưu ý rằng khi xuất phát từ điểm chưa khả thi, hàm mục tiêu $f(z)$ có thể tăng trong một số bước đầu tiên (để đưa nghiệm về vùng hợp lệ). Do đó, tiêu chuẩn tìm kiếm bước Backtracking trong trường hợp này không đo bằng sự suy giảm của riêng hàm mục tiêu $f$, mà đo bằng **sự suy giảm của chuẩn toàn bộ phần dư**: $\|(r_{\mathrm{dual}}, r_{\mathrm{pri}})\|_2$.

---

## Bài tập tự luyện

::: exercise 1. Xác định ngưỡng bước nhảy hội tụ
Cho hàm mục tiêu $f(x, y) = \frac{1}{2}(2x^2 + 8y^2)$.
Tìm khoảng giá trị của tốc độ học cố định $\eta > 0$ để thuật toán Gradient Descent hội tụ về điểm cực tiểu toàn cục từ mọi điểm xuất phát.
:::
::: solution
Ma trận Hessian của hàm số là $H = \begin{bmatrix} 2 & 0 \\ 0 & 8 \end{bmatrix}$. 
Phương trình cập nhật Gradient Descent theo từng tọa độ:
$$x_{k+1} = (1 - 2\eta) x_k, \qquad y_{k+1} = (1 - 8\eta) y_k.$$
Để dãy hội tụ về 0, điều kiện cần và đủ là các hệ số co giãn có trị tuyệt đối nhỏ hơn 1:
- $|1 - 2\eta| < 1 \iff 0 < \eta < 1$,
- $|1 - 8\eta| < 1 \iff 0 < \eta < \frac{1}{4}$.
Giao của hai điều kiện là: $0 < \eta < \frac{1}{4} = 0.25$.
:::

::: exercise 2. Thực hiện một bước lặp Newton một chiều
Xét hàm số $f(x) = x^4 + x^2$ với điểm khởi tạo hiện tại $x = 1$.
1. Tính hướng di chuyển Newton $d$ và điểm mới $x^+$ sau bước cập nhật đầy đủ.
2. Điểm mới có đạt đúng nghiệm tối ưu toàn cục không? Giải thích nguyên nhân.
:::
::: solution
1. Đạo hàm bậc nhất: $f'(x) = 4x^3 + 2x \implies g = f'(1) = 4(1)^3 + 2(1) = 6$.
   Đạo hàm bậc hai: $f''(x) = 12x^2 + 2 \implies H = f''(1) = 12(1)^2 + 2 = 14 > 0$.
   Hướng Newton: $d = -H^{-1} g = -\frac{6}{14} = -\frac{3}{7}$.
   Điểm cập nhật mới: $x^+ = x + d = 1 - \frac{3}{7} = \frac{4}{7} \approx 0.5714$.
2. Giá trị hàm số tại điểm mới là $f(4/7) = (4/7)^4 + (4/7)^2 = \frac{256}{2401} + \frac{16}{49} = \frac{1040}{2401} \approx 0.43315$. Giá trị này giảm đáng kể so với $f(1) = 2$, nhưng chưa triệt tiêu về 0 (nghiệm tối ưu thực tế là $x^* = 0$). 
   Nguyên nhân: Hàm số chứa số hạng bậc bốn $x^4$ nên không phải là hàm toàn phương thuần túy. Xấp xỉ bậc hai chỉ mang tính cục bộ, do đó thuật toán cần nhiều bước lặp để hội tụ về nghiệm.
:::

::: exercise 3. Đánh giá phần dư tại điểm xuất phát chưa khả thi
Trong mục 6, giả sử ta xuất phát từ điểm $(2, 0)$ với bài toán $\min \frac{1}{2}[(x - 2)^2 + y^2]$ thỏa $x + y = 1$.
Tại điểm này, gradient của hàm mục tiêu bằng $(0, 0)^T$. Tại sao thuật toán không thể dừng lại ở đây?
:::
::: solution
Mặc dù gradient hàm mục tiêu bằng 0 ($\nabla f(2, 0) = 0$), điểm $(2, 0)$ không thỏa mãn ràng buộc đẳng thức vì $x + y = 2 + 0 = 2 \ne 1$.
Phần dư gốc là $r_{\mathrm{pri}} = 2 - 1 = 1 \ne 0$. Vì vậy, điểm này không phải là một phương án khả thi. Trong bài toán tối ưu có ràng buộc, tiêu chí dừng bắt buộc phải kiểm tra đồng thời cả phần dư điều kiện dừng và phần dư khả thi của ràng buộc.
:::

---

## Tóm tắt cốt lõi

1. **Ba quyết định cốt tử**: Mỗi bước lặp tối ưu phân tách rạch ròi giữa chọn hướng di chuyển (bậc nhất hoặc bậc hai), chọn độ dài bước (Backtracking thỏa điều kiện Armijo), và tiêu chí dừng.
2. **Gradient Descent vs Newton**: Gradient Descent chỉ khai thác thông tin độ dốc nên di chuyển chậm chạp trên địa hình hẻm núi hẹp; phương pháp Newton tận dụng ma trận Hessian để điều chỉnh bước nhảy theo độ cong, đạt tốc độ hội tụ bậc hai gần nghiệm.
3. **Newton Decrement**: Đại lượng $\lambda(z) = \sqrt{g^TH^{-1}g}$ cung cấp thước đo bất biến affine cho khoảng cách tới nghiệm và tiêu chuẩn dừng đáng tin cậy.
4. **Hệ phương trình Newton-KKT**: Cho phép giải quyết bài toán có ràng buộc đẳng thức, đồng thời xử lý được cả trường hợp điểm khởi đầu chưa thỏa mãn ràng buộc (infeasible start).

---

## Tài liệu tham khảo và Đọc thêm

Dành cho bạn đọc muốn nghiên cứu chuyên sâu về các thuật toán tối ưu hóa số học:
- **Stephen Boyd & Lieven Vandenberghe**, *Convex Optimization*, Cambridge University Press. Đọc kỹ Chương 9 (Tối ưu hóa không ràng buộc: Gradient descent, tìm kiếm bước, phương pháp Newton, và hàm tự tương hợp) và Chương 10 (Phương pháp Newton với ràng buộc đẳng thức và hệ Newton-KKT).
- **Jorge Nocedal & Stephen J. Wright**, *Numerical Optimization*, Springer. Giáo trình kinh điển về các thuật toán tối ưu hóa số, phân tích hội tụ của điều kiện Wolfe, Armijo và phương pháp Quasi-Newton.

Tiếp theo: [Bài 05 — Tối ưu hóa trong Huấn luyện Học sâu: Mini-batch SGD và Momentum](./bai-05-toi-uu-huan-luyen.md).
