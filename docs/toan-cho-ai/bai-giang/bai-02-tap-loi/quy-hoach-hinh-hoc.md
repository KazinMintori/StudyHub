---
course: toan-cho-ai
lecture: bai-02-tap-loi
topic: quy-hoach-hinh-hoc
section: topic
title: "Quy hoạch hình học"
description: "Monomial và posynomial cùng các phép toán khép kín, quy hoạch hình học dạng chuẩn và các mở rộng, phép đổi biến logarit đưa GP về dạng lồi qua log-sum-exp, ví dụ thiết kế áp phích có lề, cân bằng ma trận theo chuẩn Frobenius và bài toán bán kính phổ Perron–Frobenius."
---

Có những bài toán không lồi trong biến gốc của chúng, nhưng trở thành lồi khi ta đo mọi đại lượng theo **thang logarit**. Quy hoạch hình học (geometric program, GP) là lớp bài toán quan trọng nhất thuộc loại này. Nó xuất hiện tự nhiên trong thiết kế kỹ thuật, nơi các đại lượng như kích thước, công suất, thời gian trễ thường dương và liên hệ với nhau qua những tích và lũy thừa.

Trang này định nghĩa các khối dựng của GP, cho thấy phép đổi biến $y = \log x$ biến GP thành một bài toán lồi, và làm hai ví dụ: Thiết kế một tấm áp phích có lề, và cân bằng một ma trận.

## 1. Monomial và posynomial

Một hàm $f : \mathbb{R}^n_{++} \to \mathbb{R}$ có dạng

$$
f(x) = c\,x_1^{a_1}x_2^{a_2}\cdots x_n^{a_n}, \qquad c > 0,\ a_i \in \mathbb{R},
$$

được gọi là một **monomial**. Số mũ có thể là số thực bất kỳ, kể cả phân số hay số âm, nhưng hệ số $c$ phải dương. Đây là chỗ khác với nghĩa của chữ "đơn thức" trong đại số, nơi số mũ phải là số nguyên không âm, và sách lưu ý điều đó. Một tổng hữu hạn các monomial,

$$
f(x) = \sum_{k=1}^K c_k\,x_1^{a_{1k}}x_2^{a_{2k}}\cdots x_n^{a_{nk}}, \qquad c_k > 0,
$$

được gọi là một **posynomial**. Chẳng hạn $3x_1^{0.5}x_2^{-1}$ là monomial, $x_1 + 2x_1x_2 + x_2^{-1}$ là posynomial, còn $x_1 - x_2$ không phải posynomial vì có hệ số âm.

Các phép toán khép kín là điều làm hai lớp hàm này dễ dùng. Tổng, tích và tích với hằng số dương của các posynomial là posynomial. Tích và thương của các monomial là monomial. Chia một posynomial cho một monomial được một posynomial. Chẳng hạn $(x_1 + x_2)^2 = x_1^2 + 2x_1x_2 + x_2^2$ là posynomial, và $(x_1 + x_2)/(x_1x_2) = x_2^{-1} + x_1^{-1}$ cũng vậy.

## 2. Quy hoạch hình học

Một **quy hoạch hình học** ở dạng chuẩn là bài toán

$$
\begin{aligned}
\text{minimize}\quad & f_0(x)\\
\text{subject to}\quad & f_i(x) \le 1, \quad i = 1, \ldots, m,\\
& h_i(x) = 1, \quad i = 1, \ldots, p,
\end{aligned}
$$

với $f_0, \ldots, f_m$ là posynomial và $h_1, \ldots, h_p$ là monomial. Miền của bài toán là $\mathbb{R}^n_{++}$, nên điều kiện $x \succ 0$ luôn được ngầm hiểu.

Nhiều ràng buộc trông khác dạng chuẩn vẫn đưa về được nhờ các phép toán khép kín. Ràng buộc "posynomial $\le$ monomial", $f(x) \le h(x)$, viết thành $f(x)/h(x) \le 1$. Ràng buộc "monomial $=$ monomial" viết thành thương của chúng bằng 1. Cực đại một monomial tương đương cực tiểu nghịch đảo của nó, cũng là một monomial. Sách cho một ví dụ: Bài toán cực đại $x/y$ với $2 \le x \le 3$, $x^2 + 3y/z \le \sqrt y$ và $x/y = z^2$ đưa được về GP dạng chuẩn

$$
\begin{aligned}
\text{minimize}\quad & x^{-1}y\\
\text{subject to}\quad & 2x^{-1} \le 1,\quad \tfrac13 x \le 1,\\
& x^2y^{-1/2} + 3y^{1/2}z^{-1} \le 1,\\
& xy^{-1}z^{-2} = 1 .
\end{aligned}
$$

## 3. Đổi sang thang logarit

GP không lồi trong biến $x$: Một posynomial như $\sqrt{x_1} + \sqrt{x_2}$ là hàm lõm, và tập $\{x : \sqrt{x_1} + \sqrt{x_2} \le 2\}$ không lồi. Đổi biến $y_i = \log x_i$, tức $x_i = e^{y_i}$. Một monomial trở thành

$$
c\,e^{a_1y_1}\cdots e^{a_ny_n} = e^{a^Ty + b}, \qquad b = \log c,
$$

hàm mũ của một hàm affine, và một posynomial trở thành tổng các hàm mũ của những hàm affine, $\sum_k e^{a_k^Ty + b_k}$. Bước thứ hai là lấy logarit của hàm mục tiêu và của mỗi ràng buộc, một phép biến đổi tăng ngặt nên giữ nguyên tập nghiệm và giữ đúng chiều bất đẳng thức. Ta được **GP dạng lồi**

$$
\begin{aligned}
\text{minimize}\quad & \log\sum_{k=1}^{K_0} e^{a_{0k}^Ty + b_{0k}}\\
\text{subject to}\quad & \log\sum_{k=1}^{K_i} e^{a_{ik}^Ty + b_{ik}} \le 0, \quad i = 1, \ldots, m,\\
& g_i^Ty + h_i = 0, \quad i = 1, \ldots, p .
\end{aligned}
$$

Mỗi hàm $\log\sum_k e^{a_k^Ty + b_k}$ là hàm [log-sum-exp](../bai-01-nhap-mon-toi-uu/cac-ham-loi-quen-thuoc.md) hợp với một ánh xạ affine, nên lồi. Mỗi ràng buộc monomial $h_i(x) = 1$ trở thành $\log h_i = 0$, một phương trình affine. Vậy GP dạng lồi là một bài toán lồi ở dạng chuẩn. Đáng chú ý là phép biến đổi không cần tính toán gì: Dữ liệu của hai dạng hoàn toàn như nhau, chỉ cách viết hàm là khác.

Về hình học, một đoạn thẳng trong biến $y$ ứng với đường $x(\theta) = p^{1-\theta}q^{\theta}$ trong biến $x$, tính theo từng thành phần. Trung điểm của đoạn ấy là **trung bình nhân** $\sqrt{pq}$ chứ không phải trung bình cộng. Tính lồi trong biến $\log x$ vì thế có nghĩa là: Tập chứa trung bình nhân của hai điểm bất kỳ của nó.

<GPLab />

Nếu mọi posynomial trong GP chỉ có một số hạng, tức đều là monomial, thì sau khi lấy logarit, mọi hàm đều affine và GP dạng lồi là một LP. Vì vậy có thể xem GP là một mở rộng của quy hoạch tuyến tính.

## 4. Ví dụ: Thiết kế một tấm áp phích

Ví dụ tự đặt. Một tấm áp phích cần phần chữ có diện tích ít nhất $600\ \text{cm}^2$, với lề trái và lề phải mỗi bên 2 cm, lề trên và lề dưới mỗi bên 3 cm. Gọi $w, h$ là chiều rộng và chiều cao của phần chữ. Ta muốn tốn ít giấy nhất:

$$
\text{minimize}\quad (w + 4)(h + 6) \qquad \text{subject to}\quad wh \ge 600 .
$$

Khai triển hàm mục tiêu cho posynomial $wh + 6w + 4h + 24$, và ràng buộc viết thành $600\,w^{-1}h^{-1} \le 1$, nên đây là một GP. Trong biến $(w, h)$, hàm mục tiêu không lồi, vì Hessian của $(w + 4)(h + 6)$ là $\begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}$, có một trị riêng âm. Trong biến $u = \log w$, $v = \log h$, ràng buộc trở thành nửa mặt phẳng $u + v \ge \log 600$, và hàm mục tiêu là log-sum-exp của bốn hàm affine.

Nghiệm có thể tìm tay. Tại nghiệm, ràng buộc chặt, nên $h = 600/w$, và hàm mục tiêu thành $600 + 6w + \tfrac{2400}{w} + 24$, nhỏ nhất khi $6w = \tfrac{2400}{w}$, tức $w = 20$ và $h = 30$. Diện tích giấy là $24 \times 36 = 864\ \text{cm}^2$. Kết quả có một cách đọc đẹp: Tỉ lệ $h/w = 30/20$ đúng bằng tỉ lệ giữa lề trên dưới và lề trái phải, $3/2$. Nếu chọn phần chữ hình vuông cạnh $\sqrt{600} \approx 24.5$, ta tốn khoảng $869\ \text{cm}^2$, nhiều hơn khoảng 0.6%.

## 5. Ví dụ: Cân bằng một ma trận

Sách đưa ra một ví dụ tính toán. Cho ma trận $M \in \mathbb{R}^{n \times n}$, ta muốn đổi thang các tọa độ bằng một ma trận chéo $D = \operatorname{diag}(d)$ với $d \succ 0$, sao cho ma trận mới $DMD^{-1}$ "nhỏ", đo bằng bình phương chuẩn Frobenius

$$
\|DMD^{-1}\|_F^2 = \sum_{i, j} M_{ij}^2\,\frac{d_i^2}{d_j^2} .
$$

Đây là một posynomial theo $d$, nên bài toán là một GP không ràng buộc, với các số mũ chỉ là 0, 2 và $-2$. Phép đổi thang này làm các phần tử của ma trận có độ lớn gần nhau hơn, một điều có lợi cho nhiều thuật toán số.

Ví dụ tự đặt với $M = \begin{bmatrix} 1 & 4 \\ 1 & 1 \end{bmatrix}$. Các phần tử chéo không đổi khi đổi thang, nên chỉ cần cực tiểu $16r^2 + r^{-2}$ theo $r = d_1/d_2$. Nghiệm là $r^2 = \tfrac14$, tức $r = \tfrac12$, và ma trận mới là $\begin{bmatrix} 1 & 2 \\ 2 & 1 \end{bmatrix}$, với hai phần tử ngoài đường chéo bằng nhau. Bình phương chuẩn Frobenius giảm từ 19 xuống 10.

Sách còn một ví dụ sâu hơn: Bán kính phổ của một ma trận dương, tức trị riêng Perron–Frobenius, có thể được cực tiểu bằng GP khi các phần tử của ma trận là posynomial của những tham số thiết kế. Sách áp dụng nó cho một mô hình quần thể vi khuẩn, nơi ta chọn nồng độ hai loại thuốc để quần thể suy giảm nhanh nhất.

## 6. Những câu hỏi để đào sâu

**Câu 1.** Giả sử ta cho phép hệ số âm, chẳng hạn ràng buộc $x_1 - x_2 \le 1$. Phép đổi biến logarit còn dùng được không, và điều kiện $c > 0$ thật ra đóng vai trò gì?

<details><summary>Xem lời giải thích</summary>

Bước lấy logarit cần các hàm dương. Một monomial với $c > 0$ dương trên $\mathbb{R}^n_{++}$, nên lấy log được, và kết quả là affine. Với hệ số âm, tổng $x_1 - x_2$ có thể âm hoặc bằng 0, và không có cách viết nó thành log-sum-exp. Những bài toán cho phép hệ số âm được gọi là signomial program, và nói chung không lồi theo bất kỳ phép đổi biến đơn giản nào. Hệ số dương không phải chi tiết kỹ thuật: Chính nó làm mỗi số hạng trở thành một hàm mũ của hàm affine, và tổng các hàm như thế mới cho log-sum-exp.

</details>

**Câu 2.** Một posynomial có lồi theo biến gốc $x$ không?

<details><summary>Xem lời giải thích</summary>

Có khi có, có khi không. Hàm $x^{-1}$ trên $x > 0$ lồi, hàm $x^2$ lồi, nhưng $\sqrt x$ lõm và $x_1x_2$ không lồi cũng không lõm. Điều chắc chắn là sau phép đổi biến $x = e^y$, mọi posynomial đều trở thành tổng các hàm mũ của hàm affine, nên lồi theo $y$. Đó là lý do người ta nói GP "lồi trong biến logarit" chứ không lồi trong biến gốc. Mô phỏng với tập $\sqrt{x_1} + \sqrt{x_2} \le 2$ cho thấy một posynomial lõm có thể tạo ra một tập không lồi theo $x$.

</details>

**Câu 3.** Trong ví dụ áp phích, vì sao tỉ lệ cạnh của phần chữ tối ưu lại đúng bằng tỉ lệ lề? Hãy chứng minh cho lề tổng quát $a$ (mỗi bên trái, phải) và $b$ (mỗi bên trên, dưới), diện tích chữ $A$.

<details><summary>Xem lời giải thích</summary>

Với ràng buộc chặt $h = A/w$, hàm mục tiêu $(w + 2a)(A/w + 2b)$ bằng $A + 2bw + \tfrac{2aA}{w} + 4ab$. Phần phụ thuộc $w$ là $2bw + 2aA/w$, nhỏ nhất khi $2bw = 2aA/w$, tức $w^2 = aA/b$. Khi đó $h = A/w$ cho $h^2 = bA/a$, và $h/w = b/a$. Diện tích giấy là $A + 4\sqrt{abA} + 4ab = (\sqrt A + 2\sqrt{ab})^2$. Trực giác: Tại nghiệm, việc dời phần diện tích chữ từ chiều này sang chiều kia phải cân bằng giữa lượng giấy lề tiết kiệm được ở hai chiều, nên mỗi chiều của phần chữ tỉ lệ với lề của chiều ấy.

</details>

**Câu 4.** GP có biến ngầm điều kiện $x \succ 0$. Nếu một đại lượng thiết kế có thể bằng 0, chẳng hạn số lượng một linh kiện tùy chọn, thì làm thế nào?

<details><summary>Xem lời giải thích</summary>

Không đưa trực tiếp được vào GP, vì $\log 0$ không xác định và các số hạng với số mũ âm sẽ nổ ra vô hạn. Có hai cách thường gặp. Cách thứ nhất là đặt một cận dưới dương nhỏ, $x \ge \epsilon$, rồi kiểm tra xem nghiệm có dồn về cận ấy không. Nếu có, giá trị 0 có lẽ là tốt nhất. Cách thứ hai là xét riêng hai trường hợp có và không có đại lượng ấy, mỗi trường hợp là một GP. Bản thân việc lựa chọn "có hay không" là một quyết định rời rạc, nằm ngoài phạm vi của tối ưu lồi.

</details>

## 7. Bài tập tự luyện

::: exercise 1. Nhận diện
Hàm nào sau đây là monomial, posynomial, hay không phải cả hai, trên $\mathbb{R}^2_{++}$? (a) $0.5x_1^{-2}x_2^{3/4}$. (b) $(x_1 + 1)^3$. (c) $x_1^2 - x_1x_2$. (d) $\dfrac{x_1 + x_2^2}{3x_1x_2}$. (e) $\sqrt{x_1^2 + x_2^2}$.
:::

::: solution
(a) Monomial, hệ số $0.5 > 0$, số mũ thực tùy ý được phép. (b) Posynomial, vì khai triển cho $x_1^3 + 3x_1^2 + 3x_1 + 1$, toàn hệ số dương, trong đó số hạng 1 là monomial với mọi số mũ bằng 0. (c) Không, vì có hệ số âm. (d) Posynomial, vì là posynomial chia monomial: $\tfrac13 x_2^{-1} + \tfrac13 x_1^{-1}x_2$. (e) Không phải posynomial, vì căn của một tổng không viết được thành tổng hữu hạn các monomial. Tuy vậy ràng buộc $\sqrt{x_1^2 + x_2^2} \le t$ tương đương $t^{-2}x_1^2 + t^{-2}x_2^2 \le 1$, một ràng buộc posynomial.
:::

::: exercise 2. Viết và giải một GP
Viết bài toán cực tiểu $x + y^2$ với $xy \ge 4$ và $x \le 3y$ thành GP dạng chuẩn và GP dạng lồi, rồi tìm nghiệm.
:::

::: hint
Ở nghiệm, ràng buộc $xy \ge 4$ phải chặt, vì nếu không ta có thể giảm $x$.
:::

::: solution
Dạng chuẩn: Cực tiểu $x + y^2$ với $4x^{-1}y^{-1} \le 1$ và $\tfrac13 xy^{-1} \le 1$. Với $u = \log x$, $v = \log y$, dạng lồi là cực tiểu $\log(e^u + e^{2v})$ với $\log 4 - u - v \le 0$ và $u - v - \log 3 \le 0$. Để giải, dùng ràng buộc chặt $x = 4/y$, cực tiểu $\tfrac4y + y^2$: Đạo hàm $-\tfrac{4}{y^2} + 2y = 0$ cho $y^3 = 2$, tức $y = 2^{1/3} \approx 1.260$ và $x = 4/y \approx 3.175$. Kiểm tra $x \le 3y \approx 3.780$, thỏa và không chặt. Giá trị tối ưu là $x + y^2 \approx 4.762$.
:::

::: exercise 3. Cân bằng ma trận
Cân bằng ma trận $M = \begin{bmatrix} 2 & 9 \\ 1 & 3 \end{bmatrix}$ theo chuẩn Frobenius như ở mục 5. Bình phương chuẩn Frobenius giảm từ bao nhiêu xuống bao nhiêu?
:::

::: solution
Cực tiểu $81r^2 + r^{-2}$ theo $r = d_1/d_2$: Nghiệm $r^2 = \tfrac19$, tức $r = \tfrac13$. Hai phần tử ngoài đường chéo trở thành $9 \cdot \tfrac13 = 3$ và $1 \cdot 3 = 3$, bằng nhau. Bình phương chuẩn Frobenius giảm từ $4 + 81 + 1 + 9 = 95$ xuống $4 + 9 + 9 + 9 = 31$.
:::

## Tóm tắt

Monomial là tích các lũy thừa thực của biến với hệ số dương, posynomial là tổng các monomial. Quy hoạch hình học cực tiểu một posynomial với các ràng buộc posynomial $\le 1$ và monomial $= 1$, trên miền $x \succ 0$. GP nói chung không lồi trong biến gốc, nhưng đổi biến $y = \log x$ rồi lấy logarit các hàm biến nó thành một bài toán lồi, với hàm log-sum-exp của các hàm affine và các ràng buộc đẳng thức affine. Trong biến gốc, tính lồi này có nghĩa là tập khả thi chứa trung bình nhân của hai điểm bất kỳ của nó.

GP xuất hiện trong thiết kế, như bài toán áp phích có nghiệm $w = 20$, $h = 30$ với tỉ lệ cạnh bằng tỉ lệ lề, và trong tính toán, như bài toán cân bằng ma trận theo chuẩn Frobenius. Khi mọi posynomial chỉ có một số hạng, GP dạng lồi là một LP.

## Nguồn và đọc thêm

- S. Boyd, L. Vandenberghe, *Convex Optimization*, §4.5 (tr. 160–167) về monomial, posynomial, GP dạng chuẩn và các mở rộng, GP dạng lồi, cân bằng ma trận theo chuẩn Frobenius, thiết kế dầm công-xôn và bài toán Perron–Frobenius với mô hình quần thể vi khuẩn.
- Ví dụ áp phích, mô phỏng, ví dụ cân bằng ma trận cỡ $2 \times 2$, các câu hỏi và bài tập do người soạn bổ sung. Mọi con số đã được tính lại bằng chương trình.
