---
course: toan-cho-ai
lecture: bai-01-nhap-mon-toi-uu
topic: phep-toan-giu-tinh-loi
section: topic
title: "Các phép toán giữ tính lồi của tập"
description: "Giao của một họ tập lồi bất kỳ, ảnh và ảnh ngược qua ánh xạ affine, phép chiếu, tổng Minkowski, đa diện và tập nghiệm LMI như ảnh ngược, nón hyperbolic, ellipsoid, và ràng buộc bền vững trong học máy."
---

Đến đây ta đã có một bộ sưu tập các tập lồi cơ bản: Tập affine, nửa không gian, quả cầu chuẩn, ellipsoid, đa diện, nón bậc hai, nón PSD. Nhưng miền khả thi của một bài toán thật hiếm khi trông giống hệt một trong số đó. Nó thường là một thứ phức tạp hơn, chẳng hạn $\{x : \|Ax - b\|_2 \le r,\ Cx \preceq d\}$, hay tệ hơn, một tập được định nghĩa bằng vô hạn ràng buộc.

Chứng minh tính lồi bằng định nghĩa cho từng tập như vậy thì vừa mệt vừa dễ sai. Sách đề xuất một cách làm khác, mà tác giả gọi là **phép tính của các tập lồi**: Chỉ ra rằng tập cần xét được lắp ghép từ các tập lồi cơ bản bằng những phép toán đã biết là giữ tính lồi. Giống như ta không chứng minh $e^{x^2 + \sin x}$ khả vi bằng định nghĩa đạo hàm, mà dùng quy tắc tổng, tích và hợp hàm. Hai phép toán quan trọng nhất, cũng là nội dung chính ở đây, là lấy giao và biến đổi affine.

## 1. Giao của các tập lồi

> **Mệnh đề.** Nếu $S_\alpha$ lồi với mọi $\alpha$ thuộc một tập chỉ số $\mathcal{A}$ bất kỳ, thì $\bigcap_{\alpha \in \mathcal{A}} S_\alpha$ lồi.

Lý do chỉ có một dòng: Nếu $x_1, x_2$ thuộc giao, thì chúng thuộc từng $S_\alpha$, nên đoạn nối chúng nằm trong từng $S_\alpha$, do đó nằm trong giao. Điều đáng chú ý là tập chỉ số $\mathcal{A}$ có thể **vô hạn**, thậm chí không đếm được, và lập luận vẫn y nguyên. Sách nhận xét rằng không gian con, tập affine và nón lồi cũng khép kín với phép giao bất kỳ.

Phép giao tương ứng với việc **thêm ràng buộc**: Mỗi ràng buộc mới cắt miền khả thi bằng một tập nữa. Vì thế đa diện, giao của hữu hạn nửa không gian và siêu phẳng, là lồi. Nón PSD, giao của vô số nửa không gian $\{X : z^T X z \ge 0\}$, cũng là lồi, như ta đã thấy ở chủ đề trước.

Ví dụ 2.8 trong sách cho thấy sức mạnh của "giao vô hạn" rõ nhất. Xét

$$
S = \{x \in \mathbb{R}^m : |p_x(t)| \le 1 \text{ với mọi } |t| \le \pi/3\}, \qquad p_x(t) = \sum_{k=1}^{m} x_k \cos kt .
$$

Mỗi vector $x$ xác định một đa thức lượng giác $p_x(t)$, và $S$ gồm những $x$ mà đa thức tương ứng không vượt khỏi dải $[-1, 1]$ trên đoạn $|t| \le \pi/3$. Thoạt nhìn, tập này có vẻ rất phức tạp: Muốn biết $x \in S$ hay không, phải kiểm tra vô số giá trị $t$. Nhưng với mỗi $t$ **cố định**, điều kiện $-1 \le (\cos t, \ldots, \cos mt)^T x \le 1$ là một **dải** giữa hai siêu phẳng song song, một tập lồi. Vì vậy $S$ là giao của vô số dải, nên lồi, mà không cần biết hình dạng cụ thể của nó.

<SlabLab />

Mô phỏng cho $m = 2$ minh họa đúng Hình 2.13 và 2.14 của sách. Hình bên phải còn cho thấy một điều thú vị: Đa thức của trung điểm hai điểm là trung bình của hai đa thức, vì $p_x(t)$ tuyến tính theo $x$. Nếu hai đa thức đều nằm trong dải $[-1, 1]$, thì trung bình của chúng cũng vậy. Đó chính là tính lồi của $S$, nhìn từ phía các hàm.

Một lời cảnh báo thực tế: Muốn **kiểm tra** $x \in S$ trên máy tính, ta thường thử trên một lưới hữu hạn các giá trị $t$. Thử trên lưới chỉ cho một tập lớn hơn $S$, vì vi phạm có thể nằm giữa hai điểm lưới. Mô phỏng dùng 121 điểm $t$ nên chỉ là một xấp xỉ từ bên ngoài.

Sách còn nêu một chiều ngược lại rất sâu sắc, mà ta sẽ chứng minh ở chủ đề về siêu phẳng phân tách: **Mọi tập lồi đóng là giao của tất cả các nửa không gian chứa nó**. Nói cách khác, mọi tập lồi đóng đều thu được bằng cách lấy giao các nửa không gian, và đó là **cách duy nhất** để tạo ra chúng.

## 2. Ảnh và ảnh ngược qua ánh xạ affine

Nhắc lại, hàm $f : \mathbb{R}^n \to \mathbb{R}^m$ là affine nếu $f(x) = Ax + b$ với $A \in \mathbb{R}^{m \times n}$, $b \in \mathbb{R}^m$.

> **Mệnh đề.** Nếu $S \subseteq \mathbb{R}^n$ lồi và $f(x) = Ax + b$, thì **ảnh** $f(S) = \{f(x) : x \in S\}$ lồi. Nếu $C \subseteq \mathbb{R}^m$ lồi, thì **ảnh ngược** $f^{-1}(C) = \{x : f(x) \in C\}$ lồi.

Cả hai chứng minh dựa vào một đẳng thức mà ta đã gặp ở chủ đề về tập affine: Hàm affine giữ nguyên tổ hợp affine, nên

$$
f(\theta x_1 + (1 - \theta) x_2) = \theta f(x_1) + (1 - \theta) f(x_2).
$$

Với ảnh: Hai điểm của $f(S)$ có dạng $y_1 = f(x_1)$, $y_2 = f(x_2)$ với $x_1, x_2 \in S$. Tổ hợp $\theta y_1 + (1-\theta)y_2$ bằng $f(\theta x_1 + (1-\theta) x_2)$, và vì $S$ lồi nên điểm $\theta x_1 + (1-\theta)x_2$ thuộc $S$. Vậy tổ hợp thuộc $f(S)$. Với ảnh ngược: Nếu $f(x_1), f(x_2) \in C$, thì

$$
f(\theta x_1 + (1-\theta)x_2) = \theta f(x_1) + (1-\theta) f(x_2) \in C
$$

vì $C$ lồi, nên $\theta x_1 + (1-\theta)x_2 \in f^{-1}(C)$.

Hai chi tiết đáng nhấn mạnh. Thứ nhất, **không cần $A$ khả nghịch**, thậm chí không cần $A$ vuông. Ký hiệu $f^{-1}(C)$ chỉ tập các đầu vào được đưa vào $C$, không phải hàm ngược. Chẳng hạn với $f(x) = 2x_1 - x_2$ và $C = [0, 3]$, ảnh ngược là dải $\{x \in \mathbb{R}^2 : 0 \le 2x_1 - x_2 \le 3\}$, dù $f$ không có hàm ngược. Thứ hai, mệnh đề chỉ nói về ánh xạ **affine**. Ảnh ngược của một tập lồi qua ánh xạ phi tuyến nói chung không lồi: Ảnh ngược của đoạn $[1, 4]$ qua $f(x) = x^2$ là $[-2, -1] \cup [1, 2]$.

Mô phỏng sau cho bạn chỉnh trực tiếp $A$ và $b$. Hãy để ý điểm vàng: Nó chia đoạn $[p, q]$ theo tỉ lệ $\theta$, và ảnh của nó chia đoạn $[f(p), f(q)]$ theo đúng tỉ lệ ấy.

<AffineImageLab />

Những trường hợp đặc biệt quen thuộc của ảnh affine:

- **Co giãn và tịnh tiến**: $\alpha S = \{\alpha x : x \in S\}$ và $S + a = \{x + a : x \in S\}$ lồi.
- **Phép chiếu**: Nếu $S \subseteq \mathbb{R}^m \times \mathbb{R}^n$ lồi, thì tập $T$ gồm những $x_1$ sao cho $(x_1, x_2) \in S$ với một $x_2$ nào đó cũng lồi. Hình chiếu là "bóng" của tập trên một số tọa độ. Bóng của một quả cầu là một hình tròn, bóng của một khối lập phương có thể là hình vuông hay lục giác tùy hướng chiếu, nhưng luôn lồi.
- **Tổng Minkowski**: $S_1 + S_2 = \{x + y : x \in S_1,\ y \in S_2\}$ lồi khi $S_1, S_2$ lồi. Lý do: Tích Descartes $S_1 \times S_2$ lồi, và $S_1 + S_2$ là ảnh của nó qua ánh xạ tuyến tính $(x, y) \mapsto x + y$. Tổng của hình vuông $[-1, 1]^2$ với hình tròn bán kính $r$ là hình vuông bo tròn bốn góc, "phình" ra một khoảng $r$ theo mọi hướng.

## 3. Những tập quen thuộc nhìn như ảnh ngược

Sức mạnh của ảnh ngược nằm ở chỗ nó cho phép **đọc lại** những tập trông lạ thành những tập đã biết.

**Đa diện** (Ví dụ 2.9). Tập $\{x : Ax \preceq b,\ Cx = d\}$ là ảnh ngược của $\mathbb{R}^m_+ \times \{0\}$ qua ánh xạ affine $f(x) = (b - Ax,\ d - Cx)$. Điều kiện $f(x) \in \mathbb{R}^m_+ \times \{0\}$ nói đúng rằng $b - Ax \succeq 0$ và $d - Cx = 0$.

**Tập nghiệm của bất đẳng thức ma trận tuyến tính** (Ví dụ 2.10). Một điều kiện có dạng

$$
A(x) = x_1 A_1 + \cdots + x_n A_n \preceq B, \qquad A_i, B \in \mathbb{S}^m,
$$

được gọi là **bất đẳng thức ma trận tuyến tính** (LMI) theo $x$. Dấu $\preceq$ ở đây là thứ tự giữa các ma trận đối xứng: $A(x) \preceq B$ nghĩa là $B - A(x) \succeq 0$. Tập nghiệm của nó là ảnh ngược của nón PSD qua ánh xạ affine $x \mapsto B - A(x)$, nên lồi. Hãy so với bất đẳng thức tuyến tính thông thường $x_1 a_1 + \cdots + x_n a_n \le b$: LMI là phiên bản trong đó các hệ số $a_i$ và vế phải $b$ được thay bằng ma trận.

::: example Một hình tròn viết bằng một LMI
Xét $\begin{bmatrix} 1 + x_1 & x_2 \\ x_2 & 1 - x_1 \end{bmatrix} \succeq 0$. Đây là một LMI với $B = I$, $A_1 = \begin{bmatrix} -1 & 0 \\ 0 & 1 \end{bmatrix}$, $A_2 = \begin{bmatrix} 0 & -1 \\ -1 & 0 \end{bmatrix}$. Theo điều kiện PSD của ma trận $2 \times 2$, nó tương đương $1 + x_1 \ge 0$, $1 - x_1 \ge 0$ và $(1 + x_1)(1 - x_1) \ge x_2^2$, tức $x_1^2 + x_2^2 \le 1$ (hai điều kiện đầu tự động đúng khi điều kiện thứ ba đúng). Vậy tập nghiệm là hình tròn đơn vị. Một ràng buộc "cong" như hình tròn có thể viết thành một ràng buộc **tuyến tính theo $x$**, chỉ cần cho phép các hệ số là ma trận. Đây là ý tưởng nền tảng của quy hoạch nửa xác định.
:::

**Nón hyperbolic** (Ví dụ 2.11). Với $P \in \mathbb{S}^n_+$ và $c \in \mathbb{R}^n$, tập

$$
\{x : X^T P x \le (c^T x)^2,\ c^T x \ge 0\}
$$

là ảnh ngược của nón bậc hai $\{(z, t) : z^T z \le t^2,\ t \ge 0\}$ qua ánh xạ affine $x \mapsto (P^{1/2}x,\ c^T x)$, nên lồi. Điều kiện $c^T x \ge 0$ không được bỏ. Với $P = I$ trong $\mathbb{R}^2$ và $c = (0, 2)$, tập là $\{x_1^2 + x_2^2 \le 4x_2^2,\ x_2 \ge 0\}$, tức $|x_1| \le \sqrt3\, x_2$, một hình quạt hướng lên. Bỏ điều kiện $x_2 \ge 0$ thì tập gồm thêm hình quạt đối xứng hướng xuống, và hợp của hai hình quạt không lồi.

**Ellipsoid** (Ví dụ 2.12). Ellipsoid $\{x : (x - x_c)^T P^{-1}(x - x_c) \le 1\}$ là ảnh của quả cầu đơn vị qua $u \mapsto P^{1/2}u + x_c$, và cũng là ảnh ngược của quả cầu đơn vị qua $x \mapsto P^{-1/2}(x - x_c)$. Hai cách nhìn này đúng là hai cách biểu diễn ellipsoid ở chủ đề trước.

## 4. Giao vô hạn trong học máy: Ràng buộc bền vững

Giao của vô số tập lồi xuất hiện tự nhiên mỗi khi một ràng buộc phải đúng **với mọi** khả năng của một đại lượng không chắc chắn. Xét một bộ phân loại tuyến tính $w$ mà ta muốn phân loại đúng điểm dữ liệu $x$ với nhãn dương một cách "an toàn", theo nghĩa $w^T(x + \delta) \ge 1$ với **mọi** nhiễu $\delta$ thỏa $\|\delta\|_\infty \le \varepsilon$. Với mỗi $\delta$ cố định, đây là một nửa không gian theo $w$. Tập các $w$ thỏa ràng buộc là giao của vô số nửa không gian, nên lồi.

Hơn nữa, giao vô hạn này có một mô tả gọn. Giá trị nhỏ nhất của $w^T \delta$ trên quả cầu $\|\delta\|_\infty \le \varepsilon$ là $-\varepsilon \|w\|_1$, đạt khi $\delta_i = -\varepsilon\, \operatorname{sign}(w_i)$. Vì vậy ràng buộc "đúng với mọi nhiễu" tương đương với một ràng buộc duy nhất:

$$
w^T x - \varepsilon \|w\|_1 \ge 1 .
$$

Đây là ý tưởng cơ bản của tối ưu bền vững, và cũng là một cách đơn giản để nghĩ về tính chống chịu nhiễu đối kháng của mô hình tuyến tính. Chương 4 của sách trình bày bài toán LP bền vững theo đúng tinh thần này.

## 5. Những câu hỏi để đào sâu

**Câu 1.** Hình chiếu của một tập **không** lồi có thể lồi không? Còn ảnh ngược của một tập không lồi qua ánh xạ affine thì sao?

<details><summary>Xem lời giải thích</summary>

Hình chiếu của tập không lồi có thể lồi. Đường tròn $\{x_1^2 + x_2^2 = 1\}$ không lồi, nhưng hình chiếu của nó lên trục hoành là đoạn $[-1, 1]$, một tập lồi. Vì vậy "hình chiếu lồi" không cho phép kết luận ngược về tập ban đầu. Ảnh ngược thì tinh tế hơn: Nếu $f$ toàn ánh, chẳng hạn $f(x) = x_1$, thì ảnh ngược của tập không lồi $\{-1, 1\}$ là hai đường thẳng $x_1 = \pm 1$, không lồi. Nhưng nếu $f$ là hàm hằng, ảnh ngược của mọi tập chứa giá trị hằng đó là cả không gian. Không có quy tắc chung, chỉ có quy tắc một chiều: Tập lồi cho ảnh và ảnh ngược lồi.

</details>

**Câu 2.** Trong ví dụ đa thức lượng giác, nếu đổi điều kiện thành "$|p_x(t)| \le 1$ với **ít nhất một** $t$ trong $[-\pi/3, \pi/3]$", tập mới có lồi không?

<details><summary>Xem lời giải thích</summary>

Tập mới là **hợp** của vô số dải chứ không phải giao, và nó không lồi. Lấy $m = 2$ cùng hai điểm $x = (3, 3)$ và $y = (3, -3)$. Điểm $x$ thuộc tập mới vì tại $t = \pi/3$, $p_x(\pi/3) = 3 \cdot 0.5 + 3 \cdot (-0.5) = 0$. Điểm $y$ cũng thuộc tập mới vì tại $t = 0$, $p_y(0) = 3 - 3 = 0$. Trung điểm của chúng là $(3, 0)$, với $p(t) = 3\cos t \ge 3 \cdot 0.5 = 1.5 > 1$ trên cả đoạn $[0, \pi/3]$, nên không thuộc tập mới. Đổi "với mọi" thành "tồn tại" biến giao thành hợp, và thường làm mất tính lồi.

</details>

**Câu 3.** Tổng Minkowski của hai đoạn thẳng không song song trong mặt phẳng là hình gì? Tổng của một tập với chính nó, $S + S$, có bằng $2S$ không?

<details><summary>Xem lời giải thích</summary>

Tổng của hai đoạn không song song là một hình bình hành. Chẳng hạn $[0, (1, 0)] + [0, (0, 1)]$ là hình vuông đơn vị. Với $S$ lồi, $S + S = 2S$: Mỗi phần tử $x + y$ của $S + S$ bằng $2 \cdot \tfrac{x + y}{2}$, và $\tfrac{x+y}{2} \in S$ do $S$ lồi. Với $S$ không lồi thì sai: $S = \{0, 1\}$ cho $S + S = \{0, 1, 2\}$ còn $2S = \{0, 2\}$. Đẳng thức $S + S = 2S$ thật ra đặc trưng cho các tập lồi trong một lớp khá rộng, một điều đáng suy nghĩ thêm.

</details>

**Câu 4.** Tập $\{x \in \mathbb{R}^n : \|Ax - b\|_2 \le c^T x + d\}$ lồi vì sao? Hãy chỉ ra tập lồi cơ bản và ánh xạ affine đang được dùng.

<details><summary>Xem lời giải thích</summary>

Tập này là ảnh ngược của nón bậc hai $\{(z, t) : \|z\|_2 \le t\}$ qua ánh xạ affine $x \mapsto (Ax - b,\ c^T x + d)$. Nón bậc hai lồi (chủ đề về chuẩn), ảnh ngược affine giữ tính lồi, nên tập lồi. Đây là dạng chung của một ràng buộc trong quy hoạch nón bậc hai. Thay vì chứng minh bằng định nghĩa, ta chỉ cần "nhận ra" cấu trúc, đúng tinh thần của phép tính tập lồi.

</details>

## 6. Bài tập tự luyện

::: exercise 1. Nhận diện phép toán
Với mỗi tập sau, chỉ ra nó được tạo từ các tập lồi cơ bản bằng phép toán nào, rồi kết luận nó lồi: (A) $\{x : \|Ax - b\|_2 \le r\}$ với $r \ge 0$, (b) $\{x : x \succeq 0,\ \mathbf{1}^T x = 1,\ \|x - u\|_\infty \le 0.1\}$, (c) $\{(x, y) \in \mathbb{R}^2 : |x| + |y - 1| \le 1\}$.
:::

::: solution
(a) Ảnh ngược của quả cầu Euclid bán kính $r$ tâm 0 qua ánh xạ affine $x \mapsto Ax - b$. (b) Giao của đơn hình xác suất (một đa diện) với quả cầu $\ell_\infty$ tâm $u$ bán kính $0.1$, cả hai lồi. (c) Ảnh ngược của quả cầu $\ell_1$ đơn vị qua phép tịnh tiến $(x, y) \mapsto (x, y - 1)$, hay nói cách khác, quả cầu $\ell_1$ dời tâm tới $(0, 1)$.
:::

::: exercise 2. Một LMI hai biến
Mô tả tập $\left\{x \in \mathbb{R}^2 : \begin{bmatrix} x_1 & 1 \\ 1 & x_2 \end{bmatrix} \succeq 0\right\}$ bằng các bất đẳng thức thông thường và cho biết hình dạng của nó.
:::

::: solution
Theo điều kiện PSD $2 \times 2$: $x_1 \ge 0$, $x_2 \ge 0$ và $x_1 x_2 \ge 1$. Điều kiện cuối cùng cùng hai điều kiện đầu buộc $x_1, x_2 > 0$, nên tập là $\{x \in \mathbb{R}^2_{++} : x_1 x_2 \ge 1\}$, miền nằm phía trên nhánh hyperbol $x_2 = 1/x_1$ trong góc phần tư thứ nhất. Đây là tập lồi trong Bài tập 2.11 của sách, và bây giờ ta có thêm một lý do: Nó là tập nghiệm của một LMI.
:::

::: exercise 3. Ràng buộc bền vững một chiều
Với $x = (2, 1)$ và $\varepsilon = 0.5$, viết ràng buộc bền vững $w^T(x + \delta) \ge 1$ với mọi $\|\delta\|_\infty \le \varepsilon$ dưới dạng không còn $\delta$. Vector $w = (1, 1)$ có thỏa ràng buộc không? Còn $w = (1, -1)$?
:::

::: solution
Ràng buộc tương đương $w^T x - 0.5\|w\|_1 \ge 1$. Với $w = (1, 1)$: $w^T x = 3$ và $\|w\|_1 = 2$, nên vế trái bằng $3 - 1 = 2 \ge 1$, thỏa. Với $w = (1, -1)$: $w^T x = 1$ và $\|w\|_1 = 2$, nên vế trái bằng $1 - 1 = 0 < 1$, không thỏa. Nhiễu xấu nhất cho trường hợp sau là $\delta = (-0.5, 0.5)$, làm $w^T(x + \delta) = 1.5 - 1.5 = 0$.
:::

## Tóm tắt

Thay vì chứng minh tính lồi bằng định nghĩa, ta lắp ghép tập cần xét từ các tập lồi cơ bản bằng những phép toán giữ tính lồi. Giao của một họ tập lồi bất kỳ, kể cả vô hạn, là lồi, và mọi tập lồi đóng thật ra là giao của các nửa không gian chứa nó. Ảnh và ảnh ngược của tập lồi qua ánh xạ affine là lồi, không cần ma trận khả nghịch. Co giãn, tịnh tiến, chiếu và tổng Minkowski là những trường hợp riêng.

Nhìn qua lăng kính ảnh ngược, đa diện, tập nghiệm của LMI, nón hyperbolic và ellipsoid đều là những tập quen thuộc được "kéo về" bởi một ánh xạ affine. Ràng buộc phải đúng với mọi khả năng của một đại lượng không chắc chắn tạo ra một giao vô hạn, nên vẫn lồi, và đôi khi viết gọn được thành một ràng buộc duy nhất.

## Nguồn và đọc thêm

- S. Boyd, L. Vandenberghe, *Convex Optimization*, §2.3.1–2.3.2 (tr. 35–39), Ví dụ 2.7–2.12, Hình 2.13–2.14. LP bền vững ở §4.4.2.
- Ví dụ hình tròn viết bằng LMI, nón hyperbolic với $P = I$, ràng buộc bền vững cho bộ phân loại tuyến tính, các câu hỏi và bài tập do người soạn bổ sung. Mọi con số đã được tính lại bằng chương trình.
