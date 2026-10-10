---
course: toan-cho-ai
lecture: bai-01-nhap-mon-toi-uu
topic: qua-cau-va-ellipsoid
section: topic
title: "Quả cầu và ellipsoid"
description: "Quả cầu Euclid với hai cách biểu diễn và chứng minh tính lồi. Ellipsoid từ ma trận xác định dương, bán trục theo vector riêng, dạng ảnh affine của quả cầu đơn vị, ellipsoid suy biến, thể tích và liên hệ với phân phối Gauss."
---

Quả cầu là tập lồi mà ai cũng hình dung được: Mọi điểm cách tâm không quá một khoảng $r$. Ellipsoid là quả cầu bị kéo dãn theo một số hướng và nén theo những hướng khác. Hai hình này xuất hiện trong tối ưu thường xuyên hơn bạn nghĩ. Ràng buộc "tham số không được lệch quá xa giá trị ban đầu" theo chuẩn Euclid là một quả cầu. Vùng tin cậy của một ước lượng thống kê, đường đồng mức của một hàm bậc hai lồi, và vùng mà phương pháp Newton tin rằng xấp xỉ bậc hai còn đúng thì đều là ellipsoid.

Ngoài định nghĩa, ellipsoid còn đáng học vì một lý do khác: Đây là nơi đầu tiên ta thấy một **ma trận** mang một **hình dạng hình học** rõ ràng: Các trị riêng của ma trận là bình phương độ dài các bán trục, còn các vector riêng chỉ hướng của chúng. Hiểu được mối liên hệ này, bạn sẽ "nhìn thấy" được ma trận hiệp phương sai, Hessian và ma trận xác định dương ở mọi chương sau. Bạn cần biết trị riêng và vector riêng của ma trận đối xứng, và khái niệm ma trận xác định dương.

## 1. Quả cầu Euclid

> **Định nghĩa.** **Quả cầu Euclid** tâm $x_c$ bán kính $r > 0$ là
> $$B(x_c, r) = \{x : \|x - x_c\|_2 \le r\} = \{x : (x - x_c)^T (x - x_c) \le r^2\}.$$

Trong đó $\|u\|_2 = (u^T u)^{1/2}$ là chuẩn Euclid. Quả cầu gồm mọi điểm cách tâm không quá $r$, kể cả những điểm trên mặt cầu. Có một cách viết thứ hai mà ta sẽ dùng rất nhiều:

$$
B(x_c, r) = \{x_c + r u : \|u\|_2 \le 1\}.
$$

Cách viết này nói rằng muốn tới một điểm của quả cầu, ta xuất phát từ tâm và đi theo một vector $ru$ có độ dài không quá $r$. Hai cách viết mô tả cùng một tập nhưng phục vụ hai việc khác nhau. Cách thứ nhất là một **ràng buộc**: Cho một điểm $x$, nó cho biết cách kiểm tra $x$ có thuộc quả cầu không. Cách thứ hai là một **tham số hóa**: Nó cho biết cách sinh ra mọi điểm của quả cầu từ quả cầu đơn vị. Bạn sẽ gặp lại sự đối ngẫu "kiểm tra hay sinh ra" này với đa diện ở một chủ đề sau.

Quả cầu Euclid là tập lồi. Lấy $x_1, x_2 \in B(x_c, r)$ và $0 \le \theta \le 1$. Viết $x_c = \theta x_c + (1 - \theta)x_c$ để tách đúng hai phần:

$$
\begin{aligned}
\|\theta x_1 + (1-\theta) x_2 - x_c\|_2 &= \|\theta (x_1 - x_c) + (1 - \theta)(x_2 - x_c)\|_2\\
&\le \theta \|x_1 - x_c\|_2 + (1 - \theta)\|x_2 - x_c\|_2 \le r .
\end{aligned}
$$

Bước bất đẳng thức đầu dùng bất đẳng thức tam giác và tính thuần nhất của chuẩn (cần $\theta \ge 0$ và $1 - \theta \ge 0$), bước sau dùng giả thiết hai điểm nằm trong quả cầu. Mẹo "viết tâm thành tổ hợp lồi của chính nó" có vẻ vụn vặt, nhưng nó là bước quyết định: Không có nó, ta không tách được hiệu thành tổng hai số hạng mà mỗi số hạng chỉ chứa một điểm.

## 2. Ellipsoid từ một ma trận xác định dương

> **Định nghĩa.** Một **ellipsoid** là tập có dạng
> $$\mathcal{E} = \{x : (x - x_c)^T P^{-1} (x - x_c) \le 1\},$$
> trong đó $P = P^T \succ 0$ là một ma trận đối xứng xác định dương và $x_c \in \mathbb{R}^n$ là **tâm**.

Ma trận $P$ quyết định ellipsoid trải rộng bao xa theo từng hướng tính từ tâm. Quả cầu bán kính $r$ là trường hợp $P = r^2 I$, vì khi đó $(x - x_c)^T P^{-1}(x - x_c) = \tfrac{\|x - x_c\|_2^2}{r^2}$.

Để thấy hình dạng của $\mathcal{E}$, ta dùng phân tích phổ của ma trận đối xứng. Viết $P = Q \Lambda Q^T$ với $Q$ trực giao có các cột là vector riêng $q_1, \ldots, q_n$, và $\Lambda = \operatorname{diag}(\lambda_1, \ldots, \lambda_n)$ với các trị riêng $\lambda_i > 0$. Khi đó $P^{-1} = Q \Lambda^{-1} Q^T$. Đặt $y = Q^T(x - x_c)$, tức là tọa độ của $x - x_c$ trong hệ trục mới dọc theo các vector riêng. Điều kiện của ellipsoid trở thành

$$
y^T \Lambda^{-1} y = \frac{y_1^2}{\lambda_1} + \frac{y_2^2}{\lambda_2} + \cdots + \frac{y_n^2}{\lambda_n} \le 1 .
$$

Đây là phương trình của một ellipsoid có các trục song song với hệ trục mới, mà bạn đã gặp ở phổ thông dưới dạng $\tfrac{x^2}{a^2} + \tfrac{y^2}{b^2} \le 1$. Đọc ra ngay: **Bán trục thứ $i$ nằm dọc vector riêng $q_i$ và dài $\sqrt{\lambda_i}$**. Trị riêng lớn cho trục dài, trị riêng nhỏ cho trục ngắn. Phép đổi biến $y = Q^T(x - x_c)$ chỉ dời tâm về gốc rồi xoay hệ trục, nên không làm méo hình.

Hãy dừng lại ở kết luận này một chút, vì nó biến một ma trận thành một hình dạng. Các phần tử của $P$, chẳng hạn $P_{12}$, không có ý nghĩa hình học riêng lẻ nào rõ ràng: Đổi hệ trục là chúng thay đổi hết. Còn các trị riêng và vector riêng thì gắn với chính hình ellipsoid, không phụ thuộc cách ta đặt trục tọa độ.

::: example Một ellipse nghiêng
Lấy $x_c = (1, -1)$ và $P = \begin{bmatrix} 5 & 3 \\ 3 & 5 \end{bmatrix}$. Ma trận này có trị riêng $8$ với vector riêng $\tfrac{1}{\sqrt2}(1, 1)$ và trị riêng $2$ với vector riêng $\tfrac{1}{\sqrt2}(-1, 1)$. Vậy ellipse có bán trục dài $\sqrt 8 = 2\sqrt2 \approx 2.83$ nằm theo đường chéo $(1, 1)$, và bán trục ngắn $\sqrt 2 \approx 1.41$ nằm theo hướng vuông góc.

Kiểm tra bằng định nghĩa. Ta có $P^{-1} = \tfrac{1}{16}\begin{bmatrix} 5 & -3 \\ -3 & 5 \end{bmatrix}$. Đầu bán trục dài là $x_c + 2\sqrt2 \cdot \tfrac{1}{\sqrt2}(1,1) = (3, 1)$, với $x - x_c = (2, 2)$ và

$$
(2,2)\, P^{-1} (2,2)^T = \tfrac{1}{16}(20 - 12 - 12 + 20) = 1,
$$

nên điểm này nằm đúng trên biên. Điểm $(2, 0)$ cho $x - x_c = (1, 1)$ và giá trị $\tfrac{1}{4} < 1$, nằm bên trong.
:::

Trong mô phỏng dưới đây, bạn chỉnh trực tiếp hai trị riêng và góc của trục thứ nhất. Các phần tử của $P$ (hiện trong khung kết quả) thay đổi liên tục khi xoay, trong khi hình dạng và độ dài bán trục thì không.

<EllipsoidLab />

## 3. Ellipsoid là ảnh của quả cầu đơn vị

Cách biểu diễn thứ hai của ellipsoid là

$$
\mathcal{E} = \{x_c + A u : \|u\|_2 \le 1\},
$$

với $A$ là ma trận vuông khả nghịch. Nó nói rằng ellipsoid là ảnh của quả cầu đơn vị qua ánh xạ affine $u \mapsto x_c + Au$: Lấy quả cầu tròn, biến dạng tuyến tính bằng $A$, rồi dời tâm tới $x_c$.

Hai cách biểu diễn khớp nhau khi $P = AA^T$. Thật vậy, với $x = x_c + Au$,

$$
\begin{aligned}
(x - x_c)^T P^{-1}(x - x_c) &= u^T A^T (A A^T)^{-1} A u \\
&= u^T A^T (A^T)^{-1} A^{-1} A u \\
&= u^T u = \|u\|_2^2,
\end{aligned}
$$

nên điều kiện $\|u\|_2 \le 1$ đúng là điều kiện $(x - x_c)^T P^{-1}(x - x_c) \le 1$. Một lỗi dễ mắc là đồng nhất $A$ với $P$. Quan hệ đúng là $P = AA^T$, tức là $A$ đóng vai trò "căn bậc hai" của $P$. Ta có thể chọn $A = P^{1/2}$, căn bậc hai đối xứng xác định dương của $P$, và hoàn toàn có thể giả sử $A$ đối xứng xác định dương mà không mất tính tổng quát. Lý do là nhiều ma trận $A$ khác nhau cho cùng một ellipsoid: Thay $A$ bằng $AQ$ với $Q$ trực giao bất kỳ, quả cầu đơn vị $\{Qu\}$ vẫn là chính nó, và $(AQ)(AQ)^T = AA^T$ vẫn bằng $P$.

Trong mô phỏng, điểm vàng là $Au$ với $u$ chạy trên đường tròn đơn vị nét đứt. Khi $u$ đi một vòng, $Au$ đi đúng một vòng quanh biên ellipse. Đó là cách nhìn "sinh ra", trong khi định nghĩa ở mục 2 là cách nhìn "kiểm tra".

Biểu diễn thứ hai cho ta thêm một điều mà biểu diễn thứ nhất không cho. Nếu $A$ nửa xác định dương nhưng **suy biến**, tập $\{x_c + Au : \|u\|_2 \le 1\}$ vẫn được định nghĩa, chỉ là bị "ép dẹt" theo những hướng $A$ triệt tiêu. Khái niệm này được gọi là **ellipsoid suy biến**, có chiều affine bằng hạng của $A$. Trong mặt phẳng, một ellipsoid suy biến với $A$ hạng 1 là một đoạn thẳng. Ellipsoid suy biến vẫn là tập lồi, nhưng không viết được dưới dạng thứ nhất, vì $P = AA^T$ không khả nghịch. Bạn có thể kéo $\lambda_2$ về 0 trong mô phỏng để thấy điều đó.

## 4. Thể tích và định thức

Biểu diễn $\mathcal{E} = x_c + A\,B(0, 1)$ cho một hệ quả đẹp về kích thước. Một ánh xạ tuyến tính $A$ nhân thể tích của mọi tập với $|\det A|$. Vì vậy

$$
\begin{aligned}
\operatorname{vol}(\mathcal{E}) &= |\det A| \cdot \operatorname{vol}(B(0,1)) \\
&= \sqrt{\det P}\, \cdot \operatorname{vol}(B(0,1)) \\
&= \sqrt{\lambda_1 \lambda_2 \cdots \lambda_n}\, \cdot \operatorname{vol}(B(0,1)).
\end{aligned}
$$

Trong mặt phẳng, diện tích ellipse là $\pi \sqrt{\lambda_1 \lambda_2}$. Với ví dụ ở mục 2, diện tích là $\pi\sqrt{8 \cdot 2} = 4\pi$. Định thức của $P$ đo "độ lớn" của ellipsoid, và đó là lý do $\log\det$ xuất hiện trong các bài toán tìm ellipsoid nhỏ nhất bao một tập điểm khi giải các bài toán tối ưu hình học. Hàm $\log\det$ cũng là một ví dụ quan trọng ở chủ đề về các hàm lồi thường gặp.

## 5. Ellipsoid trong thống kê và học máy

Mật độ của phân phối Gauss nhiều chiều $\mathcal{N}(\mu, \Sigma)$, đã gặp ở Lecture 00, tỉ lệ với $\exp\!\left(-\tfrac12 (x - \mu)^T \Sigma^{-1} (x - \mu)\right)$. Mật độ không đổi khi đại lượng $(x - \mu)^T \Sigma^{-1}(x - \mu)$ không đổi, nên các **đường đồng mức của mật độ Gauss là các ellipsoid** có tâm $\mu$ và ma trận $c\,\Sigma$. Bán trục dài nằm theo hướng dữ liệu biến thiên nhiều nhất, tức vector riêng ứng với trị riêng lớn nhất của ma trận hiệp phương sai. Đó cũng là ý tưởng của phân tích thành phần chính (PCA).

Đại lượng $\sqrt{(x - \mu)^T \Sigma^{-1}(x - \mu)}$ được gọi là **khoảng cách Mahalanobis** từ $x$ tới $\mu$. Nó đo khoảng cách bằng "đơn vị độ lệch chuẩn theo từng hướng". Chẳng hạn với $\mu = 0$ và $\Sigma = \operatorname{diag}(4, 1)$, điểm $(2, 1)$ có khoảng cách Mahalanobis bình phương $\tfrac{4}{4} + \tfrac{1}{1} = 2$. Theo hướng thứ nhất, độ lệch 2 chỉ bằng một độ lệch chuẩn, nên nó "không xa" như con số 2 gợi ý.

Một điểm cần nói rõ: Việc đường đồng mức là ellipsoid là một tính chất hình học của mật độ Gauss, chứ không phải lý do để coi mọi dữ liệu thật đều có dạng ellipsoid. Dữ liệu có nhiều cụm hay có đuôi dài thì vùng tập trung của nó trông khác hẳn.

## 6. Những câu hỏi để đào sâu

**Câu 1.** Tập $\{x \in \mathbb{R}^2 : x^T M x \le 1\}$ với $M = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}$ có phải ellipsoid không? Nó có lồi không?

<details><summary>Xem lời giải thích</summary>

Điều kiện là $2x_1 x_2 \le 1$, tức $x_1 x_2 \le \tfrac12$. Tập này chứa cả hai trục tọa độ nên không bị chặn, vì vậy không phải ellipsoid. Nó cũng không lồi: Hai điểm $(1, \tfrac12)$ và $(\tfrac12, 1)$ đều cho $x_1 x_2 = \tfrac12$, nhưng trung điểm $(\tfrac34, \tfrac34)$ cho $\tfrac{9}{16} > \tfrac12$, nằm ngoài tập. Ma trận $M$ có hai trị riêng $1$ và $-1$, tức là không xác định dương. Điều kiện $P \succ 0$ trong định nghĩa ellipsoid chính là để loại những trường hợp như thế.

</details>

**Câu 2.** Một ellipsoid trong $\mathbb{R}^2$ có bán trục $3$ và $1$. Nếu nhân ma trận $P$ với $4$, ellipsoid thay đổi thế nào? Nếu thay $P$ bằng $P^2$ thì sao?

<details><summary>Xem lời giải thích</summary>

Nhân $P$ với 4 nhân mọi trị riêng với 4, nên mọi bán trục nhân với $\sqrt 4 = 2$: Ellipsoid phóng to gấp đôi mà giữ hình dạng, bán trục thành $6$ và $2$. Thay $P$ bằng $P^2$ thì trị riêng bình phương lên, từ $9$ và $1$ thành $81$ và $1$, nên bán trục thành $9$ và $1$. Hình bị kéo dãn mạnh hơn theo trục dài. Tỉ số giữa hai bán trục, $\sqrt{\lambda_{\max}/\lambda_{\min}}$, liên quan tới **số điều kiện** của ma trận, và ellipsoid càng dẹt thì phương pháp gradient càng chạy chậm, như Lecture 04 sẽ cho thấy.

</details>

**Câu 3.** Giao của hai ellipsoid có lồi không? Nó có nhất thiết là một ellipsoid không?

<details><summary>Xem lời giải thích</summary>

Giao luôn lồi, vì giao của hai tập lồi là lồi. Nhưng nó nói chung không phải ellipsoid. Giao của hai hình tròn bằng nhau cắt nhau là một hình "thấu kính" có hai góc nhọn, mà ellipse thì không có góc. Điều này cho thấy họ các ellipsoid không khép kín với phép giao, trong khi họ các tập lồi thì có. Đây là một lý do khiến tối ưu lồi làm việc với "tập lồi" nói chung, chứ không với một họ hình cụ thể.

</details>

**Câu 4.** Vì sao nhiều ma trận $A$ khác nhau cho cùng một ellipsoid $\{x_c + Au : \|u\|_2 \le 1\}$, trong khi ma trận $P$ ở dạng thứ nhất lại xác định duy nhất?

<details><summary>Xem lời giải thích</summary>

Quả cầu đơn vị không thay đổi khi xoay hay lật bằng một ma trận trực giao $Q$, nên $A$ và $AQ$ sinh ra cùng một tập. Dạng thứ nhất thì mô tả tập bằng một hàm toàn phương $(x - x_c)^T P^{-1}(x - x_c)$, và một ellipsoid không suy biến xác định duy nhất tâm cùng hàm toàn phương đó, nên $P$ duy nhất. Quan hệ $P = AA^T$ "quên đi" phép xoay $Q$, đúng như $AQ(AQ)^T = AA^T$. Hiện tượng này xuất hiện cả trong thống kê: Nhiều cách biến đổi nhiễu trắng thành cùng một phân phối Gauss, chẳng hạn bằng phân tích Cholesky hay bằng căn bậc hai đối xứng của ma trận hiệp phương sai.

</details>

## 7. Bài tập tự luyện

::: exercise 1. Đọc hình dạng từ ma trận
Cho ellipsoid $\{x \in \mathbb{R}^2 : (x - x_c)^T P^{-1}(x - x_c) \le 1\}$ với $x_c = (2, 1)$ và $P = \operatorname{diag}(9, 4)$. Tìm bán trục, viết lại điều kiện dưới dạng không có ma trận, và tìm điểm có hoành độ lớn nhất của ellipsoid.
:::

::: solution
Vì ma trận $P$ có dạng đường chéo nên các vector riêng chính là hai trục tọa độ, trị riêng $9$ và $4$, cho bán trục $3$ theo phương ngang và $2$ theo phương đứng. Điều kiện là $\tfrac{(x_1 - 2)^2}{9} + \tfrac{(x_2 - 1)^2}{4} \le 1$. Điểm có hoành độ lớn nhất là đầu bán trục ngang bên phải, $(2 + 3, 1) = (5, 1)$.
:::

::: exercise 2. Từ dạng ảnh sang dạng ràng buộc
Cho $\mathcal{E} = \{(1, 0) + Au : \|u\|_2 \le 1\}$ với $A = \begin{bmatrix} 2 & 0 \\ 1 & 1 \end{bmatrix}$. Tìm ma trận $P$ của dạng thứ nhất và kiểm tra rằng điểm $(3, 1)$ nằm trên biên.
:::

::: hint
Tính $P = AA^T$. Điểm $(3, 1)$ ứng với vector $u$ nào?
:::

::: solution
Ta có ma trận $P = AA^T = \begin{bmatrix} 2 & 0 \\ 1 & 1 \end{bmatrix}\begin{bmatrix} 2 & 1 \\ 0 & 1 \end{bmatrix} = \begin{bmatrix} 4 & 2 \\ 2 & 2 \end{bmatrix}$, có định thức $4 \ne 0$. Với $x = (3, 1)$, $x - x_c = (2, 1) = A u$ cho $2u_1 = 2$ và $u_1 + u_2 = 1$, tức $u = (1, 0)$, một vector đơn vị, nên $x$ nằm trên biên. Đối chiếu bằng dạng thứ nhất: Ma trận nghịch đảo $P^{-1} = \tfrac14 \begin{bmatrix} 2 & -2 \\ -2 & 4 \end{bmatrix}$ và

$$
(2, 1)\, P^{-1} (2, 1)^T = \tfrac14 (8 - 4 - 4 + 4) = 1.
$$
:::

::: exercise 3. Diện tích và khoảng cách Mahalanobis
Với $\Sigma = \begin{bmatrix} 5 & 3 \\ 3 & 5 \end{bmatrix}$ và $\mu = 0$, tính diện tích của ellipse $\{x : x^T \Sigma^{-1} x \le 1\}$ và khoảng cách Mahalanobis từ gốc tới hai điểm $(2, 2)$ và $(1, -1)$. Điểm nào "xa" gốc hơn theo nghĩa thống kê?
:::

::: solution
Trị riêng của $\Sigma$ là $8$ và $2$, nên diện tích là $\pi\sqrt{16} = 4\pi$. Với $\Sigma^{-1} = \tfrac{1}{16}\begin{bmatrix} 5 & -3 \\ -3 & 5 \end{bmatrix}$: Điểm $(2, 2)$ cho $\tfrac{1}{16}(20 - 12 - 12 + 20) = 1$, khoảng cách 1. Điểm $(1, -1)$ cho $\tfrac{1}{16}(5 + 3 + 3 + 5) = 1$, khoảng cách cũng là 1. Hai điểm cách gốc theo Euclid lần lượt $2\sqrt2$ và $\sqrt2$, nhưng theo Mahalanobis thì như nhau, vì điểm thứ nhất nằm theo hướng có độ lệch chuẩn $\sqrt8$, còn điểm thứ hai theo hướng có độ lệch chuẩn $\sqrt2$.
:::

## Tóm tắt

Quả cầu Euclid có hai cách viết: Dạng ràng buộc $\|x - x_c\|_2 \le r$ để kiểm tra một điểm, và dạng tham số $x_c + ru$ với $\|u\|_2 \le 1$ để sinh ra các điểm. Nó lồi nhờ bất đẳng thức tam giác và tính thuần nhất của chuẩn. Ellipsoid $\{(x - x_c)^T P^{-1}(x - x_c) \le 1\}$ với $P \succ 0$ có các bán trục nằm theo vector riêng của $P$ và dài bằng căn bậc hai trị riêng tương ứng. Nó cũng là ảnh $x_c + Au$ của quả cầu đơn vị với $P = AA^T$, và khi $A$ suy biến ta được ellipsoid suy biến có chiều affine bằng hạng của $A$.

Thể tích ellipsoid tỉ lệ với $\sqrt{\det P}$. Đường đồng mức của mật độ Gauss là các ellipsoid xác định bởi ma trận hiệp phương sai, và khoảng cách Mahalanobis đo khoảng cách theo hình dạng đó.

## Tài liệu tham khảo

- Stephen Boyd, Lieven Vandenberghe, *Convex Optimization*, Cambridge University Press.
