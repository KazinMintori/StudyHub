---
course: toan-cho-ai
lecture: bai-01-nhap-mon-toi-uu
topic: ham-loi
section: topic
title: "Hàm lồi và bất đẳng thức dây cung"
description: "Định nghĩa hàm lồi, lồi nghiêm ngặt, lõm và affine cùng ý nghĩa hình học của dây cung. Vì sao miền xác định phải lồi, cách kiểm tra tính lồi bằng cách hạn chế lên đường thẳng, mở rộng giá trị và hàm chỉ thị của một tập."
---

Phần hình học vừa qua nói về **tập lồi**: những miền mà đoạn thẳng nối hai điểm bất kỳ không bao giờ đi ra ngoài. Nhưng ngoài miền khả thi, một bài toán tối ưu còn có hàm mục tiêu. Câu hỏi tiếp theo vì vậy rất tự nhiên: một **hàm** "lồi" thì nên được hiểu thế nào, để những điều tốt đẹp của tập lồi truyền sang được bài toán tối ưu?

Câu trả lời của sách dùng lại đúng công cụ quen thuộc là đoạn thẳng, nhưng đặt nó lên đồ thị của hàm. Sau định nghĩa và ý nghĩa của từng điều kiện trong đó, ta học kỹ thuật hạn chế hàm lên một đường thẳng, cách biến một câu hỏi nhiều chiều thành nhiều câu hỏi một chiều. Phần cuối là một mẹo ký hiệu giúp biến ràng buộc thành một phần của hàm mục tiêu.

## 1. Định nghĩa

> **Định nghĩa.** Hàm $f : \mathbb{R}^n \to \mathbb{R}$ là **lồi** nếu miền xác định $\operatorname{dom} f$ là một tập lồi, và với mọi $x, y \in \operatorname{dom} f$ cùng mọi $\theta$ thỏa $0 \le \theta \le 1$,
> $$f(\theta x + (1 - \theta) y) \le \theta f(x) + (1 - \theta) f(y).$$

Hai vế của bất đẳng thức làm hai việc khác nhau, và nhầm lẫn giữa chúng là lỗi hay gặp khi mới học. Vế trái **trộn các đầu vào trước** rồi mới tính hàm: lấy điểm $z = \theta x + (1-\theta)y$ trên đoạn nối $x$ với $y$, rồi tính $f(z)$. Vế phải **tính hàm trước** rồi mới trộn các giá trị: tính $f(x)$ và $f(y)$, rồi lấy trung bình có trọng số của hai con số đó. Hàm lồi là hàm mà "trộn trước rồi tính" không bao giờ cho kết quả lớn hơn "tính trước rồi trộn".

Về hình học, đặt hai điểm $(x, f(x))$ và $(y, f(y))$ trên đồ thị. Đoạn thẳng nối chúng, gọi là **dây cung**, đi qua điểm $(z,\ \theta f(x) + (1-\theta) f(y))$ phía trên $z$. Bất đẳng thức nói rằng tại mọi $z$ giữa $x$ và $y$, đồ thị nằm **dưới hoặc chạm** dây cung (Hình 3.1 trong sách). Một cái bát úp ngửa có hình dạng đó: căng một sợi chỉ giữa hai điểm trên thành bát, sợi chỉ luôn nằm phía trên lòng bát.

<FunctionLab type="chord" />

Mô phỏng cho bạn chọn hàm, chọn hai điểm $a, b$ và trượt $\theta$. Với các hàm $x^2$, $|x|$, $e^x$, $-\log x$, đoạn thẳng nhỏ nối đồ thị với dây cung luôn màu xanh. Với $x^3$ hay $0.3x^2 + \sin(1.5x)$, bạn sẽ tìm được những cặp $a, b$ làm đồ thị vượt lên trên dây cung. Hãy nhớ sự bất đối xứng quen thuộc từ tập lồi: một vi phạm là đủ để bác bỏ, còn để chứng minh thì phải lập luận cho mọi cặp điểm và mọi $\theta$.

::: example Chứng minh tính lồi của x² bằng định nghĩa
Với $f(x) = x^2$, hiệu giữa vế phải và vế trái là

$$
\theta x^2 + (1 - \theta) y^2 - \big(\theta x + (1-\theta) y\big)^2 = \theta(1 - \theta)(x - y)^2 .
$$

Đẳng thức này kiểm tra được bằng khai triển. Dùng $\theta - \theta^2 = \theta(1-\theta)$ và $(1-\theta) - (1-\theta)^2 = \theta(1-\theta)$, vế trái bằng

$$
\begin{aligned}
&\theta x^2 + (1-\theta)y^2 - \theta^2 x^2 - 2\theta(1-\theta)xy - (1-\theta)^2 y^2 \\
&\quad = \theta(1-\theta)\,\big(x^2 - 2xy + y^2\big).
\end{aligned}
$$

Vì $\theta \in [0, 1]$ nên $\theta(1-\theta) \ge 0$, và hiệu không âm. Đẳng thức còn cho biết nhiều hơn: khoảng cách giữa dây cung và đồ thị tại $z$ bằng đúng $\theta(1-\theta)(x-y)^2$. Chẳng hạn với $x = -2$, $y = 1$, $\theta = \tfrac13$, ta có $z = 0$, $f(z) = 0$, giá trị trên dây cung là $\tfrac13 \cdot 4 + \tfrac23 \cdot 1 = 2$, và quả thật $\tfrac13 \cdot \tfrac23 \cdot 9 = 2$.
:::

## 2. Những điều kiện nhỏ có hệ quả lớn

**Miền xác định phải lồi.** Điều kiện này không phải hình thức. Nếu $\operatorname{dom} f$ không lồi, điểm $z = \theta x + (1-\theta) y$ có thể nằm ngoài miền, và vế trái của bất đẳng thức không có nghĩa. Hàm $f(x) = 1/x^2$ trên miền $x \ne 0$ là ví dụ của sách (Ghi chú 3.1): trên mỗi nửa trục, nó cong lên, đạo hàm bậc hai luôn dương, nhưng nó **không** phải hàm lồi vì miền xác định gồm hai mảnh rời nhau. Trong mô phỏng ở trên, chọn hàm $1/x^2$ với $a < 0 < b$ để thấy đoạn $[a, b]$ đi qua điểm 0, nơi hàm không xác định.

**Lồi nghiêm ngặt.** Hàm $f$ là **lồi nghiêm ngặt** nếu bất đẳng thức là chặt ($<$) mỗi khi $x \ne y$ và $0 < \theta < 1$. Về hình học, đồ thị nằm **hẳn** dưới mọi dây cung, chỉ chạm ở hai đầu mút. Hàm $x^2$ lồi nghiêm ngặt, vì hiệu $\theta(1-\theta)(x-y)^2$ dương khi $x \ne y$ và $0 < \theta < 1$. Hàm $|x|$ thì lồi nhưng không nghiêm ngặt: trên nửa trục dương nó là một đường thẳng, nên dây cung trùng với đồ thị.

**Lõm và affine.** Hàm $f$ là **lõm** nếu $-f$ lồi, tức đồ thị nằm trên mọi dây cung, như cái bát úp sấp. Với hàm affine $f(x) = a^T x + b$, bất đẳng thức trở thành đẳng thức với mọi $\theta$, vì hàm affine giữ nguyên tổ hợp affine. Vì vậy mọi hàm affine vừa lồi vừa lõm. Sách nêu thêm chiều ngược lại: hàm nào vừa lồi vừa lõm thì phải là affine. Không có hàm "cong" nào thỏa cả hai chiều bất đẳng thức.

**Tính liên tục.** Sách nhắc một kết quả mà ta không chứng minh: hàm lồi luôn liên tục trên nội tương đối của miền xác định, và chỉ có thể gián đoạn trên biên tương đối. Hàm bằng 0 trên khoảng mở $(0, 1)$ và bằng 1 tại hai đầu mút $0$, $1$ là một hàm lồi trên $[0, 1]$, gián đoạn đúng tại hai đầu mút. Hàm lồi không thể có "bước nhảy" ở giữa miền, vì một bước nhảy sẽ làm đồ thị vượt lên trên một dây cung nào đó.

## 3. Kiểm tra tính lồi trên từng đường thẳng

Định nghĩa hàm lồi chỉ dùng đến hai điểm và đoạn nối chúng. Do đó mọi thông tin về tính lồi của $f$ đều nằm trên các đường thẳng đi qua miền xác định. Sách phát biểu điều này thành một tiêu chuẩn:

> **Mệnh đề.** $f$ lồi khi và chỉ khi với mọi $x \in \operatorname{dom} f$ và mọi hướng $v$, hàm một biến $g(t) = f(x + tv)$ lồi trên miền $\{t : x + tv \in \operatorname{dom} f\}$.

Chiều "chỉ khi" đúng vì đoạn thẳng của $g$ trên trục $t$ là đoạn thẳng của $f$ trên đường $x + tv$, và miền của $g$ là giao của một đường thẳng với tập lồi $\operatorname{dom} f$, nên là một khoảng. Chiều "khi" đúng vì mọi cặp điểm $x, y$ của miền nằm trên đường thẳng qua $x$ theo hướng $v = y - x$, và bất đẳng thức của $f$ cho cặp đó chính là bất đẳng thức của $g$ cho cặp $t = 0$, $t = 1$.

Tiêu chuẩn này biến một câu hỏi nhiều chiều thành vô số câu hỏi một chiều, mà hàm một biến thì ta biết nhiều cách kiểm tra, chẳng hạn bằng đạo hàm bậc hai. Sách sẽ dùng kỹ thuật này để chứng minh $\log\det X$ lõm ở chủ đề về các hàm thường gặp. Mô phỏng sau cho bạn chọn một hàm hai biến, kéo một đường thẳng qua miền, và xem đồ thị của hàm hạn chế $g(t)$ ở bên phải.

<Restrict2DLab />

Với $x_1^2 - x_2^2$, hàm hạn chế cong lên khi đường thẳng gần trục hoành và cong xuống khi gần trục tung. Chỉ cần một đường thẳng cho $g$ cong xuống là đủ kết luận $f$ không lồi. Với $\log(e^{x_1} + e^{x_2})$, hướng $(1, 1)$ cho một hàm hạn chế **tuyến tính**: dọc hướng đó hàm tăng đều mà không cong chút nào. Hàm vẫn lồi, vì lồi chỉ đòi "không cong xuống", không đòi "cong lên ngặt".

## 4. Mở rộng giá trị và hàm chỉ thị

Viết đi viết lại "với mọi $x \in \operatorname{dom} f$" khá phiền. Sách dùng một quy ước giúp gọn ký hiệu: **mở rộng giá trị** của hàm lồi $f$ là hàm $\tilde f : \mathbb{R}^n \to \mathbb{R} \cup \{+\infty\}$ cho bởi

$$
\tilde f(x) = \begin{cases} f(x) & x \in \operatorname{dom} f,\\ +\infty & x \notin \operatorname{dom} f. \end{cases}
$$

Ta lấy lại miền xác định bằng $\operatorname{dom} f = \{x : \tilde f(x) < \infty\}$. Với quy ước số học "$\infty$ cộng gì cũng là $\infty$", bất đẳng thức định nghĩa trở thành $\tilde f(\theta x + (1-\theta)y) \le \theta \tilde f(x) + (1-\theta) \tilde f(y)$ với mọi $x, y$ và $0 < \theta < 1$: nếu một trong hai điểm nằm ngoài miền thì vế phải bằng $\infty$ và bất đẳng thức hiển nhiên đúng. Quy ước này cũng tự động xử lý miền xác định của tổng: $\tilde f_1 + \tilde f_2$ bằng $\infty$ ở mọi điểm nằm ngoài một trong hai miền, nên miền của tổng là giao của hai miền. Từ đây trở đi, sách và môn học ngầm hiểu mọi hàm lồi đều được mở rộng như vậy.

Một ví dụ đặc biệt quan trọng là **hàm chỉ thị** của một tập lồi $C$ (Ví dụ 3.1):

$$
\tilde I_C(x) = \begin{cases} 0 & x \in C,\\ +\infty & x \notin C. \end{cases}
$$

Hàm này lồi vì $C$ lồi. Nó cho phép viết một bài toán có ràng buộc thành bài toán không ràng buộc: cực tiểu $f$ trên $C$ **chính là** cực tiểu $f + \tilde I_C$ trên toàn không gian, vì mọi điểm ngoài $C$ có giá trị $+\infty$ và không bao giờ được chọn. Ràng buộc trở thành một phần của hàm mục tiêu, với "giá phạt" bằng $+\infty$ cho việc vi phạm. Ý tưởng này có họ hàng gần trong học máy: thay giá phạt $+\infty$ bằng một giá phạt hữu hạn, chẳng hạn $\rho \|x\|_2^2$, ta được điều chuẩn, một "ràng buộc mềm".

## 5. Những câu hỏi để đào sâu

**Câu 1.** Một bạn khẳng định: "Hàm $f(x) = x^3$ lồi, vì đồ thị của nó cong lên ở bên phải gốc." Bạn ấy đúng một phần ở chỗ nào, và sai ở chỗ nào?

<details><summary>Xem lời giải thích</summary>

Đúng một phần: trên miền $x \ge 0$, $f''(x) = 6x \ge 0$ và hàm $x^3$ với miền $\mathbb{R}_+$ là lồi. Sai ở chỗ coi nó lồi trên $\mathbb{R}$. Lấy $x = -2$, $y = 0$, $\theta = \tfrac12$: $f(-1) = -1$, trong khi dây cung cho $\tfrac12(-8) + \tfrac12 \cdot 0 = -4$, và $-1 > -4$. Tính lồi là tính chất của **cặp** hàm và miền xác định. Cùng một công thức có thể lồi trên miền này mà không lồi trên miền khác.

</details>

**Câu 2.** Nếu $f$ lồi và $c > 0$ là một hằng số, hàm $f(cx)$ có lồi không? Hàm $f(x) + c$, $f(x + c)$ thì sao? Còn $c \cdot f(x)$ với $c < 0$?

<details><summary>Xem lời giải thích</summary>

Ba hàm $f(cx)$, $f(x) + c$ và $f(x + c)$ đều lồi. Hàm $f(cx)$ và $f(x + c)$ là hợp của $f$ với một phép biến đổi affine của $x$, mà phép biến đổi affine mang đoạn thẳng thành đoạn thẳng nên dây cung vẫn nằm trên đồ thị. Hàm $f(x) + c$ chỉ cộng cùng một hằng số vào hai vế của bất đẳng thức, vì $\theta c + (1-\theta) c = c$. Còn $c f(x)$ với $c < 0$ là một hàm **lõm**: nhân hai vế của bất đẳng thức với số âm làm đảo chiều. Chủ đề về các phép toán giữ tính lồi của hàm sẽ hệ thống hóa những quy tắc này.

</details>

**Câu 3.** Hàm $f(x) = \min\{x^2, 1\}$ có lồi không? Hãy trả lời bằng cách tìm một dây cung, rồi giải thích bằng hình dạng của đồ thị.

<details><summary>Xem lời giải thích</summary>

Không lồi. Với $x = 0$ và $y = 2$, $\theta = \tfrac12$: $f(1) = 1$, còn dây cung cho $\tfrac12 \cdot 0 + \tfrac12 \cdot 1 = \tfrac12 < 1$. Đồ thị là parabol bị "cắt ngọn" ở độ cao 1, tạo ra hai chỗ gãy lõm vào tại $x = \pm 1$. Hàm chặn trên một hàm lồi bằng một hằng số thường phá tính lồi, vì lấy **min** của hai hàm lồi không giữ tính lồi. Ngược lại, lấy **max** của hai hàm lồi thì giữ.

</details>

**Câu 4.** Dùng hàm chỉ thị, viết bài toán "cực tiểu $\|x\|_2^2$ với điều kiện $Ax = b$" thành một bài toán không ràng buộc. Hàm mục tiêu mới có lồi không, và nó có khả vi không?

<details><summary>Xem lời giải thích</summary>

Bài toán tương đương là cực tiểu $\|x\|_2^2 + \tilde I_C(x)$ trên $\mathbb{R}^n$, với $C = \{x : Ax = b\}$. Hàm mới lồi vì là tổng của hai hàm lồi ($C$ là tập affine, nên lồi). Nhưng nó không khả vi, thậm chí không hữu hạn ở ngoài $C$. Cách viết này hữu ích cho lý thuyết, còn khi tính toán, người ta thường giữ ràng buộc ở dạng tường minh hoặc thay hàm chỉ thị bằng một hàm phạt trơn.

</details>

## 6. Bài tập tự luyện

::: exercise 1. Chứng minh bằng định nghĩa
Chứng minh $f(x) = |x|$ lồi trên $\mathbb{R}$ bằng định nghĩa. Nó có lồi nghiêm ngặt không?
:::

::: solution
Với mọi $x, y$ và $\theta \in [0, 1]$,

$$
|\theta x + (1-\theta)y| \le |\theta x| + |(1-\theta)y| = \theta|x| + (1-\theta)|y|,
$$

trong đó bước đầu là bất đẳng thức tam giác và bước sau dùng $\theta \ge 0$, $1-\theta \ge 0$. Hàm không lồi nghiêm ngặt: với $x = 1$, $y = 2$ và $\theta = \tfrac12$, hai vế đều bằng $1.5$, dù $x \ne y$ và $0 < \theta < 1$.
:::

::: exercise 2. Tìm một dây cung vi phạm
Chứng minh $f(x) = \sin x$ trên $[0, 2\pi]$ không lồi và không lõm, bằng cách chỉ ra hai dây cung thích hợp.
:::

::: solution
Không lồi: với $x = 0$, $y = \pi$, $\theta = \tfrac12$, ta có $f(\tfrac\pi2) = 1$, còn dây cung cho $\tfrac12(0 + 0) = 0 < 1$. Không lõm: với $x = \pi$, $y = 2\pi$, $\theta = \tfrac12$, ta có $f(\tfrac{3\pi}{2}) = -1$, còn dây cung cho $0 > -1$, nên đồ thị nằm dưới dây cung, trái với tính lõm. Trên $[0, \pi]$ thì $\sin x$ lõm, và trên $[\pi, 2\pi]$ thì lồi.
:::

::: exercise 3. Hạn chế lên đường thẳng
Cho $f(x_1, x_2) = x_1 x_2$ trên $\mathbb{R}^2$. Tính $g(t) = f(x + tv)$ với $x = (0, 0)$ và $v = (1, -1)$, rồi kết luận về tính lồi của $f$. Với $v = (1, 1)$ thì sao?
:::

::: solution
Với $v = (1, -1)$: $g(t) = (t)(-t) = -t^2$, một hàm lõm nghiêm ngặt, nên $f$ không lồi. Với $v = (1, 1)$: $g(t) = t^2$, lồi. Hàm $x_1 x_2$ có Hessian $\begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}$ với trị riêng $\pm 1$: theo hướng của vector riêng ứng với $+1$ thì cong lên, theo hướng ứng với $-1$ thì cong xuống. Đó là hình dạng của một cái yên ngựa.
:::

## Tóm tắt

Hàm $f$ lồi khi miền xác định lồi và đồ thị nằm dưới mọi dây cung: trộn đầu vào trước rồi tính hàm không bao giờ lớn hơn tính hàm trước rồi trộn giá trị. Lồi nghiêm ngặt đòi bất đẳng thức chặt, lõm nghĩa là $-f$ lồi, và chỉ hàm affine vừa lồi vừa lõm. Miền xác định lồi là điều kiện thật sự cần, như ví dụ $1/x^2$ cho thấy.

Một hàm lồi khi và chỉ khi nó lồi trên mọi đường thẳng cắt miền xác định, nên câu hỏi nhiều chiều quy được về câu hỏi một chiều. Quy ước mở rộng giá trị cho hàm bằng $+\infty$ ngoài miền xác định, và hàm chỉ thị của một tập lồi biến ràng buộc thành một phần của hàm mục tiêu.

## Nguồn và đọc thêm

- S. Boyd, L. Vandenberghe, *Convex Optimization*, §3.1.1–3.1.2 (tr. 67–69), Hình 3.1 và Ví dụ 3.1. Ví dụ hàm $1/x^2$ là Ghi chú 3.1 ở §3.1.4 (tr. 71).
- Ví dụ hàm cắt ngọn $\min\{x^2, 1\}$, các mô phỏng, câu hỏi và bài tập do người soạn bổ sung. Mọi con số đã được tính lại bằng chương trình.
