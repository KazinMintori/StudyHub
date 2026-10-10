---
course: toan-cho-ai
lecture: bai-01-nhap-mon-toi-uu
topic: phep-toan-giu-tinh-loi
section: topic
title: "Các phép toán giữ tính lồi của tập"
description: "Giao của một họ tập lồi bất kỳ, ảnh và ảnh ngược qua ánh xạ affine, phép chiếu, tổng Minkowski, đa diện và tập nghiệm LMI như ảnh ngược, nón hyperbolic, ellipsoid, và ràng buộc bền vững trong học máy."
---

Đến đây ta đã có một bộ sưu tập các tập lồi cơ bản: Tập affine, nửa không gian, quả cầu chuẩn, ellipsoid, đa diện, nón bậc hai, nón PSD. Nhưng miền khả thi của một bài toán thật hiếm khi trông giống hệt một trong số đó. Nó thường là một thứ phức tạp hơn, chẳng hạn $\{x : \|Ax - b\|_2 \le r,\ Cx \preceq d\}$, hay tệ hơn, một tập được định nghĩa bằng vô hạn ràng buộc.

Chứng minh tính lồi trực tiếp từ định nghĩa bằng cách kiểm tra mọi cặp điểm cho từng tập hợp phức tạp là một quy trình nặng nề và rất dễ sơ suất. Ta sử dụng một phương pháp đại số thanh lịch hơn: **Giải tích các tập lồi** (calculus of convex sets): Thiết lập tính lồi của tập hợp cần xét bằng cách chứng minh nó được tạo thành từ các tập lồi cơ bản thông qua những phép toán bảo toàn tính lồi. Tương tự như trong giải tích cổ điển, ta không chứng minh hàm $e^{x^2 + \sin x}$ khả vi bằng định nghĩa giới hạn của số gia, mà áp dụng các quy tắc đạo hàm của tổng, tích và hàm hợp. Hai phép toán cơ bản nhất, giữ vai trò chủ đạo trong bài học này, là phép lấy giao và biến đổi affine.

## 1. Giao của các tập lồi

> **Mệnh đề.** Nếu $S_\alpha$ là tập lồi với mọi chỉ số $\alpha$ thuộc một tập chỉ số $\mathcal{A}$ tùy ý, thì giao $\bigcap_{\alpha \in \mathcal{A}} S_\alpha$ cũng là một tập lồi.

Chứng minh rất ngắn gọn: Nếu hai điểm $x_1, x_2$ cùng thuộc phần giao, thì chúng bắt buộc phải thuộc từng tập $S_\alpha$ với mọi $\alpha \in \mathcal{A}$. Do từng $S_\alpha$ là tập lồi, toàn bộ đoạn thẳng nối hai điểm đó nằm trọn trong từng $S_\alpha$, và vì thế nằm trọn trong phần giao. Điểm cốt lõi là tập chỉ số $\mathcal{A}$ có thể mang lực lượng **vô hạn**, thậm chí vô hạn không đếm được, mà lập luận logic vẫn bảo toàn nguyên vẹn. Cần ghi nhận rằng không gian con tuyến tính, tập affine và nón lồi cũng khép kín dưới phép giao tùy ý.

Về mặt tối ưu hóa, phép giao tương ứng với hành động **bổ sung thêm ràng buộc**: Mỗi ràng buộc mới tương đương với việc thu hẹp miền khả thi bằng phần giao với một tập lồi mới. Nhờ đó, tập đa diện (giao của hữu hạn các nửa không gian đóng và siêu phẳng) luôn lồi. Tương tự, nón ma trận nửa xác định dương $\mathbb{S}^n_+$ (giao của vô hạn các nửa không gian dạng $\{X \in \mathbb{S}^n : z^T X z \ge 0\}$ ứng với mọi vector $z \in \mathbb{R}^n$) chắc chắn là một tập lồi.

Một ví dụ giải tích sâu sắc thể hiện rõ nét sức mạnh của phép giao vô hạn: Xét tập hợp

$$
S = \left\{x \in \mathbb{R}^m : |p_x(t)| \le 1 \text{ với mọi } |t| \le \frac{\pi}{3}\right\}, \qquad p_x(t) = \sum_{k=1}^{m} x_k \cos(kt) .
$$

Mỗi vector $x \in \mathbb{R}^m$ xác định một đa thức lượng giác $p_x(t)$, và tập $S$ bao gồm toàn bộ các vector $x$ sao cho đồ thị đa thức tương ứng không vượt ra ngoài dải $[-1, 1]$ trên đoạn $[-\pi/3, \pi/3]$. Thoạt nhìn, việc xác minh tính lồi trực tiếp là bất khả thi vì đòi hỏi kiểm tra liên tục trên vô số giá trị $t$. Tuy nhiên, với mỗi giá trị $t$ **cố định**, điều kiện biên $-1 \le (\cos t, \ldots, \cos mt) x \le 1$ định nghĩa một **dải phẳng** (slab) kẹp giữa hai siêu phẳng song song, vốn là một tập lồi đóng. Vì vậy, tập $S$ thực chất là giao của vô số dải phẳng lồi, do đó $S$ chắc chắn là một tập lồi.

<SlabLab />

Mô phỏng tương tác phía trên minh họa cấu trúc hình học của tập nghiệm dải song song. Bản chất tính lồi của $S$ phản ánh tính tuyến tính của hàm: Đa thức ứng với trung điểm hai vector chính là trung bình cộng của hai đa thức tương ứng $p_{(x+y)/2}(t) = \tfrac{1}{2}p_x(t) + \tfrac{1}{2}p_y(t)$. Nếu cả hai đa thức thành phần đều nằm trọn trong dải $[-1, 1]$, đồ thị trung bình cộng chắc chắn cũng nằm trong dải đó.

Đặc biệt, ta có một định lý đối ngẫu hình học sâu sắc: **Mọi tập lồi đóng trong $\mathbb{R}^n$ đều là giao của toàn bộ các nửa không gian đóng chứa nó**. Nói cách khác, phép lấy giao các nửa không gian chính là cơ chế phổ quát duy nhất để kiến tạo nên mọi tập lồi đóng.

## 2. Ảnh và ảnh ngược qua ánh xạ affine

Nhắc lại rằng ánh xạ $f : \mathbb{R}^n \to \mathbb{R}^m$ được gọi là affine nếu nó có dạng $f(x) = Ax + b$ với $A \in \mathbb{R}^{m \times n}$ và $b \in \mathbb{R}^m$.

> **Mệnh đề.** Nếu $S \subseteq \mathbb{R}^n$ là tập lồi và $f(x) = Ax + b$, thì **ảnh** $f(S) = \{f(x) : x \in S\}$ là tập lồi trong $\mathbb{R}^m$. Ngược lại, nếu $C \subseteq \mathbb{R}^m$ là tập lồi, thì **ảnh ngược** $f^{-1}(C) = \{x \in \mathbb{R}^n : f(x) \in C\}$ là tập lồi trong $\mathbb{R}^n$.

Chứng minh cho cả hai chiều đều bắt nguồn từ tính chất bất biến của ánh xạ affine đối với tổ hợp lồi:

$$
f(\theta x_1 + (1 - \theta) x_2) = \theta f(x_1) + (1 - \theta) f(x_2), \qquad \forall \theta \in [0, 1].
$$

- Đối với tập ảnh: Lấy hai điểm tùy ý $y_1, y_2 \in f(S)$, tồn tại $x_1, x_2 \in S$ sao cho $y_1 = f(x_1)$ và $y_2 = f(x_2)$. Khi đó tổ hợp lồi $\theta y_1 + (1-\theta)y_2 = f(\theta x_1 + (1-\theta) x_2)$. Vì $S$ lồi nên $\theta x_1 + (1-\theta)x_2 \in S$, kéo theo tổ hợp lồi này thuộc $f(S)$.
- Đối với tập ảnh ngược: Lấy hai điểm $x_1, x_2 \in f^{-1}(C)$, tức $f(x_1), f(x_2) \in C$. Khi đó:

  $$
  f(\theta x_1 + (1-\theta)x_2) = \theta f(x_1) + (1-\theta) f(x_2) \in C
  $$

  bởi vì $C$ là tập lồi. Do đó $\theta x_1 + (1-\theta)x_2 \in f^{-1}(C)$.

Để không bao giờ nhầm lẫn ở bước này, ta chú ý: Phép lấy ảnh ngược $f^{-1}(C)$ chỉ đòi hỏi tính lồi của tập đích $C$ và tính affine của ánh xạ $f$, hoàn toàn không yêu cầu ma trận biến đổi $A$ phải khả nghịch hay vuông. Ký hiệu $f^{-1}(C)$ biểu thị tập các tiền ảnh (pre-image). Hơn nữa, tính chất này chỉ đúng với ánh xạ **affine**: Ảnh ngược của một tập lồi qua một hàm phi tuyến nói chung hoàn toàn không lồi (chẳng hạn ảnh ngược của đoạn lồi $[1, 4]$ qua hàm bậc hai $f(x) = x^2$ là hợp của hai đoạn rời nhau $[-2, -1] \cup [1, 2]$).

<AffineImageLab />

Các phép biến đổi hình học quan trọng là trường hợp đặc biệt của ảnh và ảnh ngược affine:

- **Co giãn và tịnh tiến**: Phép phóng đại $\alpha S = \{\alpha x : x \in S\}$ và phép dịch chuyển vector $S + a = \{x + a : x \in S\}$ luôn bảo toàn tính lồi.
- **Phép chiếu tọa độ** (Projection): Nếu $S \subseteq \mathbb{R}^m \times \mathbb{R}^n$ là tập lồi, thì hình chiếu của nó:

$$
T = \{x_1 \in \mathbb{R}^m : \exists x_2 \in \mathbb{R}^n \text{ sao cho } (x_1, x_2) \in S\}
$$

cũng là một tập lồi. Hình chiếu chính là "bóng" của tập hợp lên không gian con tọa độ.
- **Tổng Minkowski**: Tổng của hai tập lồi $S_1 + S_2 = \{x + y : x \in S_1,\ y \in S_2\}$ luôn là một tập lồi. Lý do: Tích Descartes $S_1 \times S_2$ là tập lồi, và $S_1 + S_2$ chính là ảnh của nó qua ánh xạ affine tuyến tính $(x, y) \mapsto x + y$.

## 3. Nhận diện các tập lồi nâng cao qua lăng kính ảnh ngược

Sức mạnh thực sự của phép lấy ảnh ngược là biến đổi các miền ràng buộc phức tạp về các cấu trúc hình nón hoặc hình cầu chuẩn quen thuộc:

- **Đa diện**: Tập hợp $\{x \in \mathbb{R}^n : Ax \preceq b,\ Cx = d\}$ chính là ảnh ngược của nón lồi $\mathbb{R}^m_+ \times \{0\}$ qua ánh xạ affine $f(x) = (b - Ax,\ d - Cx)$.
- **Tập nghiệm của bất đẳng thức ma trận tuyến tính (LMI)**: Một điều kiện ràng buộc có dạng
  $$
  A(x) = x_1 A_1 + \cdots + x_n A_n \preceq B, \qquad A_i, B \in \mathbb{S}^m,
  $$
  được gọi là một bất đẳng thức ma trận tuyến tính (Linear Matrix Inequality - LMI). Ký hiệu ma trận $A(x) \preceq B$ tương đương với $B - A(x) \succeq 0$. Tập nghiệm của LMI chính là ảnh ngược của nón nửa xác định dương $\mathbb{S}^m_+$ qua ánh xạ affine $x \mapsto B - A(x)$, do đó luôn luôn là một tập lồi. Đây là dạng ràng buộc tổng quát bao trùm toàn bộ họ bài toán quy hoạch nửa xác định (SDP).

::: example Biểu diễn hình tròn bằng một ràng buộc ma trận tuyến tính LMI
Xét bất đẳng thức ma trận: $\begin{bmatrix} 1 + x_1 & x_2 \\ x_2 & 1 - x_1 \end{bmatrix} \succeq 0$. Đây là một LMI cấp 2 theo hai biến số $(x_1, x_2)$. Theo tiêu chuẩn Sylvester cho ma trận cấp 2, điều kiện nửa xác định dương tương đương với: $1 + x_1 \ge 0$, $1 - x_1 \ge 0$ và định thức không âm $(1 + x_1)(1 - x_1) - x_2^2 \ge 0$, tức $x_1^2 + x_2^2 \le 1$.

Tập nghiệm chính là hình tròn đơn vị đóng. Một miền cong phi tuyến đã được tuyến tính hóa hoàn hảo dưới dạng ma trận.
:::

- **Nón hyperbolic**: Cho ma trận $P \in \mathbb{S}^n_+$ và vector $c \in \mathbb{R}^n$. Tập hợp
  $$
  \{x \in \mathbb{R}^n : x^T P x \le (c^T x)^2,\ c^T x \ge 0\}
  $$
  chính là ảnh ngược của nón bậc hai chuẩn Lorentz $\{(z, t) : \|z\|_2 \le t,\ t \ge 0\}$ qua ánh xạ affine $x \mapsto (P^{1/2}x,\ c^T x)$, do đó luôn là một tập lồi. Điều kiện nửa không gian $c^T x \ge 0$ là bắt buộc để loại bỏ phần nón đối xứng hướng xuống phía dưới.
- **Tập Ellipsoid**: Khối ellipsoid đóng $\{x \in \mathbb{R}^n : (x - x_c)^T P^{-1}(x - x_c) \le 1\}$ có thể xem đồng thời là ảnh của hình cầu Euclid đơn vị qua ánh xạ affine $u \mapsto P^{1/2}u + x_c$, và là ảnh ngược của hình cầu Euclid qua ánh xạ $x \mapsto P^{-1/2}(x - x_c)$.

## 4. Giao vô hạn trong học máy: Mô hình tối ưu hóa bền vững

Trong học máy và lý thuyết điều khiển, các tham số mô hình thường xuyên phải đối mặt với nhiễu dữ liệu hoặc tấn công đối kháng. Khái niệm giao vô hạn cung cấp công cụ toán học trực tiếp để giải quyết bài toán này.

Xét một bộ phân loại tuyến tính $w$ cần phân loại chính xác điểm dữ liệu $x$ với nhãn dương một cách an toàn trước mọi nhiễu chặn: Đòi hỏi $w^T(x + \delta) \ge 1$ phải thỏa mãn với **mọi** vector nhiễu $\delta$ nằm trong hình cầu chuẩn vô hạn $\|\delta\|_\infty \le \varepsilon$. Với mỗi vector nhiễu $\delta$ cố định, ràng buộc trên định nghĩa một nửa không gian đóng theo biến $w$. Tập hợp các nghiệm $w$ khả thi chính là giao của vô hạn các nửa không gian, do đó bảo đảm tính lồi tuyệt đối.

Hơn thế nữa, bài toán giao vô hạn này có thể rút gọn tường minh: Giá trị nhỏ nhất của lượng dịch chuyển $w^T \delta$ dưới ràng buộc $\|\delta\|_\infty \le \varepsilon$ đạt được khi $\delta_i = -\varepsilon \operatorname{sign}(w_i)$, cho giá trị cực tiểu đúng bằng $-\varepsilon \|w\|_1$. Do đó, họ vô hạn các ràng buộc được quy gọn về một bất đẳng thức lồi duy nhất:

$$
w^T x - \varepsilon \|w\|_1 \ge 1 .
$$

Sự xuất hiện của số hạng điều chuẩn chuẩn $\ell_1$ (Lasso regularization) xuất phát một cách tự nhiên từ yêu cầu chống chịu nhiễu đối kháng tồi tệ nhất. Đây cũng là nguyên lý chuyển đổi bài toán tối ưu tuyến tính bền vững (Robust LP) thành bài toán quy hoạch nón bậc hai hoặc quy hoạch tuyến tính tương đương.

## 5. Những câu hỏi để đào sâu

**Câu 1.** Hình chiếu của một tập **không lồi** có thể trở thành một tập lồi được không? Ảnh ngược của một tập không lồi thì sao?

<details><summary>Xem lời giải thích</summary>

Hình chiếu của một tập không lồi hoàn toàn có thể là một tập lồi. Xét đường tròn một chiều $\{x \in \mathbb{R}^2 : x_1^2 + x_2^2 = 1\}$, tập này không lồi vì chỉ gồm đường biên rỗng ruột. Tuy nhiên, hình chiếu của nó lên trục hoành $x_1$ chính là đoạn thẳng đóng $[-1, 1]$, vốn là một tập lồi. Vì vậy, tính lồi của hình chiếu không cho phép suy ngược lại tính lồi của tập gốc.

Đối với ảnh ngược, nếu ánh xạ affine là toàn ánh, ảnh ngược của một tập không lồi thường không lồi. Tuy nhiên, nếu ánh xạ suy biến (chẳng hạn ánh xạ hằng số đưa mọi điểm về một giá trị duy nhất), ảnh ngược có thể trở thành toàn bộ không gian $\mathbb{R}^n$, do đó vẫn lồi. Quy tắc logic luôn mang tính một chiều: Tính lồi chỉ được bảo toàn xuôi theo chiều biến đổi affine.

</details>

**Câu 2.** Trong ví dụ đa thức lượng giác, nếu thay đổi điều kiện thành "$|p_x(t)| \le 1$ với **ít nhất một** giá trị $t \in [-\pi/3, \pi/3]$", tập hợp mới có còn lồi không?

<details><summary>Xem lời giải thích</summary>

Tập hợp mới sẽ không còn lồi. Việc thay lượng từ "với mọi" bằng "tồn tại" tương đương với việc chuyển từ phép **giao** các tập hợp sang phép **hợp** các tập hợp: $S_{\text{mới}} = \bigcup_{t} S_t$. Hợp của các tập lồi nói chung không phải là một tập lồi. Chẳng hạn với $m = 2$, hai vector $x = (3, 3)^T$ và $y = (3, -3)^T$ đều thuộc tập mới vì đa thức của chúng triệt tiêu tại các điểm biên tương ứng. Tuy nhiên trung điểm của chúng là $(3, 0)^T$ có giá trị đa thức $p(t) = 3\cos t \ge 1.5 > 1$ tại mọi điểm trên đoạn xét, do đó không thuộc tập hợp, phá vỡ tính lồi.

</details>

**Câu 3.** Tổng Minkowski của hai đoạn thẳng không song song trong mặt phẳng là hình gì? Với tập lồi $S$, đẳng thức $S + S = 2S$ có luôn đúng không?

<details><summary>Xem lời giải thích</summary>

Tổng Minkowski của hai đoạn thẳng đóng không cùng phương trong mặt phẳng chính là một hình bình hành đóng.

Đối với tập hợp $S$, nếu $S$ là tập lồi thì ta luôn có đẳng thức $S + S = 2S$: Mọi phần tử $z \in S + S$ có dạng $z = x + y = 2(\tfrac{x+y}{2})$. Vì $S$ lồi nên trung điểm $\tfrac{x+y}{2} \in S$, suy ra $z \in 2S$. Ngược lại nếu $S$ không lồi thì đẳng thức này nói chung sai: Chẳng hạn với tập rời rạc $S = \{0, 1\}$, ta có $S + S = \{0, 1, 2\}$ trong khi $2S = \{0, 2\}$.

</details>

**Câu 4.** Vì sao miền ràng buộc dạng nón bậc hai $\{x \in \mathbb{R}^n : \|Ax - b\|_2 \le c^T x + d\}$ luôn là một tập lồi?

<details><summary>Xem lời giải thích</summary>

Tập hợp này là ảnh ngược của nón bậc hai Lorentz chuẩn $K = \{(z, t) \in \mathbb{R}^{m+1} : \|z\|_2 \le t\}$ qua ánh xạ affine $x \mapsto (Ax - b,\ c^T x + d)$. Vì nón Lorentz là một tập lồi, và phép lấy ảnh ngược qua ánh xạ affine luôn bảo toàn tính lồi, nên tập ràng buộc trên chắc chắn là một tập lồi. Đây chính là cấu trúc miền khả thi mẫu mực trong quy hoạch nón bậc hai (SOCP).

</details>

## 6. Bài tập tự luyện

::: exercise 1. Nhận diện phép toán bảo toàn tính lồi
Với mỗi tập hợp sau đây, hãy xác định các phép toán giữ tính lồi đã tạo ra nó từ các tập lồi cơ bản:
- Trường hợp (a): Tập nghiệm $\{x \in \mathbb{R}^n : \|Ax - b\|_2 \le r\}$ với bán kính $r \ge 0$.
- Trường hợp (b): Tập hợp các vector $x \in \mathbb{R}^n$ thỏa mãn $x \succeq 0$, $\mathbf{1}^T x = 1$ và $\|x - u\|_\infty \le 0.1$.
- Trường hợp (c): Miền phẳng $\{(x, y) \in \mathbb{R}^2 : |x| + |y - 1| \le 1\}$.
:::

::: solution
- Trường hợp (a): Là ảnh ngược của hình cầu đóng Euclid bán kính $r$ qua ánh xạ affine $x \mapsto Ax - b$.
- Trường hợp (b): Là giao của đơn hình xác suất (một đa diện lồi) với hình cầu chuẩn $\ell_\infty$ tâm tại $u$ bán kính $0.1$. Cả hai đều là tập lồi nên giao của chúng lồi.
- Trường hợp (c): Là ảnh ngược của hình cầu chuẩn $\ell_1$ tâm tại gốc tọa độ qua phép tịnh tiến affine $(x, y) \mapsto (x, y - 1)$, tức là hình thoi chuẩn $\ell_1$ được dời tâm tới điểm $(0, 1)$.
:::

::: exercise 2. Tập nghiệm của một LMI cấp hai
Hãy mô tả tường minh tập nghiệm của bất đẳng thức ma trận tuyến tính sau trong $\mathbb{R}^2$:

$$
\mathcal{S} = \left\{x \in \mathbb{R}^2 : \begin{bmatrix} x_1 & 1 \\ 1 & x_2 \end{bmatrix} \succeq 0\right\}
$$

và giải thích đặc tính hình học của nó.
:::

::: solution
Theo tiêu chuẩn ma trận đối xứng cấp 2 nửa xác định dương, điều kiện tương đương với:
$$
x_1 \ge 0, \qquad x_2 \ge 0, \qquad x_1 x_2 - 1 \ge 0 \iff x_1 x_2 \ge 1.
$$
Kết hợp lại, tập nghiệm chính là miền nằm phía trên nhánh hyperbol $x_2 \ge 1/x_1$ trong góc phần tư thứ nhất $\mathbb{R}^2_{++}$. Tập này là một tập lồi đóng, được kiến tạo như ảnh ngược của nón PSD qua ánh xạ affine ma trận.
:::

::: exercise 3. Ràng buộc tối ưu hóa bền vững
Cho điểm dữ liệu $x = (2, 1)^T$ và bán kính nhiễu không chắc chắn $\varepsilon = 0.5$. Hãy thiết lập ràng buộc bền vững tường minh đối với vector trọng số $w \in \mathbb{R}^2$ dưới điều kiện $w^T(x + \delta) \ge 1$ với mọi $\|\delta\|_\infty \le 0.5$. Kiểm tra tính khả thi của hai vector $w_1 = (1, 1)^T$ và $w_2 = (1, -1)^T$.
:::

::: solution
Ràng buộc bền vững tương đương với bất đẳng thức:
$$
w^T x - \varepsilon \|w\|_1 \ge 1 \iff 2w_1 + w_2 - 0.5 (|w_1| + |w_2|) \ge 1.
$$

- Với vector $w_1 = (1, 1)^T$: Ta có $w^T x = 2(1) + 1 = 3$ và $\|w\|_1 = 2$. Vế trái bằng $3 - 0.5(2) = 2 \ge 1$. Do đó $w_1$ thỏa mãn ràng buộc bền vững.
- Với vector $w_2 = (1, -1)^T$: Ta có $w^T x = 2(1) - 1 = 1$ và $\|w\|_1 = 2$. Vế trái bằng $1 - 0.5(2) = 0 < 1$. Do đó $w_2$ vi phạm ràng buộc bền vững. Vector nhiễu xấu nhất gây ra vi phạm là $\delta = (-0.5, 0.5)^T$.
:::

## Tóm tắt

Phép toán giữ tính lồi cung cấp một khuôn khổ đại số để xây dựng và kiểm tra tính lồi của các miền ràng buộc phức tạp mà không cần dùng đến định nghĩa sơ cấp. Phép giao của một họ tùy ý các tập lồi (kể cả họ vô hạn) luôn bảo toàn tính lồi, và mọi tập lồi đóng đều biểu diễn được dưới dạng giao của các nửa không gian đóng. Phép lấy ảnh và ảnh ngược qua ánh xạ affine luôn giữ nguyên tính lồi mà không đòi hỏi ma trận biến đổi phải khả nghịch.

Thông qua lăng kính ảnh ngược affine, các cấu trúc toán học nâng cao như tập đa diện, tập nghiệm của bất đẳng thức ma trận tuyến tính (LMI), nón hyperbolic và khối ellipsoid đều được quy về các nón lồi hoặc hình cầu chuẩn cơ bản. Trong học máy hiện đại, các bài toán tối ưu hóa bền vững trước nhiễu và tấn công đối kháng đều được mô hình hóa tự nhiên thông qua phép giao vô hạn các tập lồi.

## Tài liệu tham khảo
- Stephen Boyd, Lieven Vandenberghe, *Convex Optimization*, Cambridge University Press.

