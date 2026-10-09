---
course: toan-cho-ai
lecture: bai-01-nhap-mon-toi-uu
topic: da-dien-va-don-hinh
section: topic
title: "Đa diện và đơn hình"
description: "Đa diện là giao hữu hạn nửa không gian và siêu phẳng, ký hiệu Ax ⪯ b, đơn hình và độc lập affine, đơn hình xác suất, cách viết một đơn hình thành hệ bất đẳng thức, và hai cách mô tả đa diện bằng ràng buộc hoặc bằng đỉnh."
---

Quy hoạch tuyến tính, bài toán quen thuộc nhất của tối ưu, có miền khả thi được mô tả bằng một danh sách bất đẳng thức tuyến tính. Mỗi bất đẳng thức cắt bỏ một nửa không gian, và phần còn lại sau khi cắt hết là một **đa diện**. Hiểu hình dạng của đa diện, nó có những đỉnh nào, có bị chặn không, có rỗng không, là hiểu được nửa câu chuyện của quy hoạch tuyến tính.

Trang này cũng giới thiệu **đơn hình**, loại đa diện đơn giản nhất: đoạn thẳng, tam giác, tứ diện và các "anh em" nhiều chiều của chúng. Đơn hình xác suất, tập mọi phân phối xác suất trên hữu hạn kết quả, là đơn hình mà bạn gặp mỗi ngày trong học máy mà có khi không để ý. Cuối trang là một câu hỏi tinh tế hơn: một đa diện có thể mô tả bằng các mặt hoặc bằng các đỉnh, và hai cách mô tả đó có thể chênh nhau về kích thước tới mức hàm mũ.

## 1. Đa diện

> **Định nghĩa.** Một **đa diện** là tập nghiệm của một số hữu hạn bất đẳng thức và đẳng thức tuyến tính:
> $$\mathcal{P} = \{x : a_j^T x \le b_j,\ j = 1, \ldots, m,\quad c_j^T x = d_j,\ j = 1, \ldots, p\}.$$

Nói cách khác, đa diện là giao của hữu hạn nửa không gian và siêu phẳng. Vì mỗi nửa không gian và mỗi siêu phẳng đều lồi, và giao của các tập lồi là lồi, nên **mọi đa diện đều lồi**. Hình 2.11 trong sách vẽ một đa diện là giao của năm nửa mặt phẳng, mỗi nửa mặt phẳng có một pháp tuyến hướng ra ngoài $a_j$.

Ta dùng một cách viết ma trận cô đọng:

$$
\mathcal{P} = \{x : Ax \preceq b,\ Cx = d\},
$$

trong đó các hàng của $A$ là $a_1^T, \ldots, a_m^T$, các hàng của $C$ là $c_1^T, \ldots, c_p^T$, và ký hiệu $u \preceq v$ giữa hai vector nghĩa là $u_i \le v_i$ **với từng thành phần** $i$. Ký hiệu này khác với dấu $\le$ giữa hai số. Hai vector $u = (1, 3)$ và $v = (2, 2)$ chẳng hạn không thỏa cả $u \preceq v$ lẫn $v \preceq u$, vì thành phần thứ nhất của $u$ nhỏ hơn còn thành phần thứ hai lại lớn hơn. Chủ đề về bất đẳng thức tổng quát sẽ biến nhận xét nhỏ này thành một lý thuyết.

Nhiều tập quen thuộc là đa diện: tập affine (chỉ có đẳng thức), tia, đoạn thẳng, nửa không gian, và **góc phần tư không âm** $\mathbb{R}^n_+ = \{x : x \succeq 0\}$. Góc phần tư không âm vừa là đa diện vừa là nón, nên được gọi là **nón đa diện**.

Một đa diện có thể không bị chặn, chẳng hạn một nửa không gian, và có thể rỗng, khi các ràng buộc mâu thuẫn. Đa diện bị chặn đôi khi được gọi là **đa đỉnh** (polytope). Sách lưu ý rằng các tác giả khác nhau dùng hai từ này theo những quy ước ngược nhau, nên khi đọc tài liệu khác, hãy kiểm tra định nghĩa của họ.

Bạn có thể tự ghép một đa diện trong mặt phẳng từ các nửa mặt phẳng trong mô phỏng sau. Các đường nét đứt là biên của từng ràng buộc, phần tô là giao của chúng.

<PolyhedronLab />

Hãy để ý cột "chặt" bên cạnh mỗi đỉnh. Trong mặt phẳng, mỗi đỉnh của đa diện có ít nhất hai ràng buộc chặt, và hai đường biên đó cắt nhau đúng tại đỉnh. Nhận xét này mở rộng thành định nghĩa đại số của đỉnh ở Lecture 07: trong $\mathbb{R}^n$, một đỉnh là điểm khả thi tại đó có $n$ ràng buộc chặt với các pháp tuyến độc lập tuyến tính.

## 2. Đơn hình

Trước khi định nghĩa đơn hình, ta cần một khái niệm độc lập phù hợp với tổ hợp affine.

> **Định nghĩa.** Các điểm $v_0, v_1, \ldots, v_k \in \mathbb{R}^n$ được gọi là **độc lập affine** nếu các vector $v_1 - v_0, \ldots, v_k - v_0$ độc lập tuyến tính.

Ba điểm độc lập affine nghĩa là chúng không thẳng hàng, bốn điểm độc lập affine nghĩa là chúng không đồng phẳng. Để ý rằng định nghĩa đo các hiệu so với $v_0$, đúng với tinh thần "không phụ thuộc gốc tọa độ" của tổ hợp affine. Đổi vai trò của $v_0$ với một điểm khác cũng không làm thay đổi kết luận.

> **Định nghĩa.** Với $k + 1$ điểm độc lập affine $v_0, \ldots, v_k$, **đơn hình** xác định bởi chúng là bao lồi
> $$C = \operatorname{conv}\{v_0, \ldots, v_k\} = \{\theta_0 v_0 + \cdots + \theta_k v_k : \theta \succeq 0,\ \mathbf{1}^T \theta = 1\}.$$

Ở đây $\mathbf{1}$ là vector toàn số 1, nên $\mathbf{1}^T\theta = \theta_0 + \cdots + \theta_k$. Đơn hình này có chiều affine $k$, nên còn được gọi là đơn hình $k$ chiều trong $\mathbb{R}^n$. Đơn hình 1 chiều là một đoạn thẳng, đơn hình 2 chiều là một tam giác (kể cả phần trong), đơn hình 3 chiều là một tứ diện.

Hai đơn hình đặc biệt có tên riêng:

- **Đơn hình đơn vị** xác định bởi $0, e_1, \ldots, e_n$, tức tập $\{x : x \succeq 0,\ \mathbf{1}^T x \le 1\}$. Nó có chiều $n$.
- **Đơn hình xác suất** xác định bởi $e_1, \ldots, e_n$, tức tập $\{x : x \succeq 0,\ \mathbf{1}^T x = 1\}$. Nó có chiều $n - 1$, và mỗi điểm của nó là một phân phối xác suất trên $n$ kết quả, với $x_i$ là xác suất của kết quả thứ $i$.

Đơn hình xác suất có mặt ở khắp nơi trong học máy. Đầu ra của tầng softmax trong một bộ phân loại $n$ lớp là một điểm của nó, chính xác hơn là một điểm trong nội tương đối của nó. Trọng số của một mô hình hỗn hợp, hay trọng số chú ý (attention) trong mô hình Transformer, cũng là những điểm của đơn hình xác suất. Một đỉnh $e_i$ là phân phối "chắc chắn kết quả $i$", còn trọng tâm $\tfrac1n \mathbf{1}$ là phân phối đều, "hoàn toàn không biết gì".

## 3. Viết một đơn hình thành hệ bất đẳng thức

Định nghĩa đơn hình là một mô tả bằng đỉnh. Nhưng đơn hình là một đa diện, nên nó cũng phải viết được bằng bất đẳng thức và đẳng thức. Sách trình bày cách làm điều đó, và lập luận này đáng học vì nó minh họa một kỹ thuật đổi biến hay gặp.

Mọi điểm của đơn hình có dạng $x = \theta_0 v_0 + \theta_1 v_1 + \cdots + \theta_k v_k$. Vì $\theta_0 = 1 - \theta_1 - \cdots - \theta_k$, ta viết lại

$$
x = v_0 + \theta_1 (v_1 - v_0) + \cdots + \theta_k (v_k - v_0) = v_0 + By, \qquad y = (\theta_1, \ldots, \theta_k),
$$

với $B = \begin{bmatrix} v_1 - v_0 & \cdots & v_k - v_0 \end{bmatrix} \in \mathbb{R}^{n \times k}$. Điều kiện trên $\theta$ trở thành $y \succeq 0$ và $\mathbf{1}^T y \le 1$, vì $\theta_0 = 1 - \mathbf{1}^T y \ge 0$. Do độc lập affine, $B$ có hạng $k$. Khi đó tồn tại một ma trận khả nghịch $A = \begin{bmatrix} A_1 \\ A_2 \end{bmatrix}$ sao cho $AB = \begin{bmatrix} I \\ 0 \end{bmatrix}$. Nhân $x = v_0 + By$ với $A$ từ bên trái được hai phương trình $A_1 x = A_1 v_0 + y$ và $A_2 x = A_2 v_0$. Phương trình thứ nhất cho $y = A_1 (x - v_0)$, nên $x$ thuộc đơn hình khi và chỉ khi

$$
A_2 x = A_2 v_0, \qquad A_1 x \succeq A_1 v_0, \qquad \mathbf{1}^T A_1 x \le 1 + \mathbf{1}^T A_1 v_0 .
$$

Đây là một hệ đẳng thức và bất đẳng thức tuyến tính theo $x$. Phần $A_2 x = A_2 v_0$ nói rằng $x$ phải nằm trong bao affine của đơn hình, còn phần bất đẳng thức nói rằng tọa độ trọng tâm của $x$ không âm.

::: example Một tam giác trong mặt phẳng và một tam giác nằm trong R³
Với $v_0 = (1, 1)$, $v_1 = (3, 1)$ và $v_2 = (1, 4)$ trong $\mathbb{R}^2$, ta có $B = \begin{bmatrix} 2 & 0 \\ 0 & 3 \end{bmatrix}$, khả nghịch, nên lấy $A = A_1 = B^{-1}$ và không cần $A_2$. Điều kiện $y = B^{-1}(x - v_0) \succeq 0$ cho $x_1 \ge 1$ và $x_2 \ge 1$. Điều kiện $\mathbf{1}^T y \le 1$ cho $\tfrac{x_1 - 1}{2} + \tfrac{x_2 - 1}{3} \le 1$, tức $3x_1 + 2x_2 \le 11$. Kiểm tra: $v_1$ cho $9 + 2 = 11$ và $v_2$ cho $3 + 8 = 11$, đều nằm trên cạnh đối diện $v_0$.

Với tam giác trong $\mathbb{R}^3$ có đỉnh $v_0 = (0, 0, 1)$, $v_1 = (1, 0, 1)$, $v_2 = (0, 1, 1)$, ta có $B = \begin{bmatrix} 1 & 0 \\ 0 & 1 \\ 0 & 0 \end{bmatrix}$ có hạng 2. Chọn $A = I_3$, với $A_1$ gồm hai hàng đầu và $A_2 = (0, 0, 1)$, thì $AB = \begin{bmatrix} I \\ 0 \end{bmatrix}$. Hệ thu được là $x_3 = 1$, $x_1 \ge 0$, $x_2 \ge 0$ và $x_1 + x_2 \le 1$. Phương trình $x_3 = 1$ chính là mặt phẳng chứa tam giác.
:::

## 4. Hai cách mô tả một đa diện

Bao lồi của hữu hạn điểm $\operatorname{conv}\{v_1, \ldots, v_k\}$ luôn là một đa diện bị chặn. Sách nêu một mở rộng: tập

$$
\{\theta_1 v_1 + \cdots + \theta_k v_k : \theta_1 + \cdots + \theta_m = 1,\ \theta_i \ge 0,\ i = 1, \ldots, k\}, \qquad m \le k,
$$

là bao lồi của $v_1, \ldots, v_m$ cộng với bao nón của $v_{m+1}, \ldots, v_k$, và nó là một đa diện. Điều ngược lại cũng đúng, dù sách không chứng minh: **mọi đa diện đều viết được dưới dạng "bao lồi của hữu hạn điểm cộng bao nón của hữu hạn hướng"**. Kết quả này thường được gọi là định lý Minkowski–Weyl. Như vậy mỗi đa diện có hai cách mô tả. Cách mô tả bằng ràng buộc $Ax \preceq b$ trả lời câu hỏi "làm sao kiểm tra một điểm có thuộc đa diện". Cách mô tả bằng đỉnh và hướng trả lời câu hỏi "làm sao sinh ra mọi điểm của đa diện". Đó đúng là sự đối ngẫu "kiểm tra hay sinh ra" mà ta đã gặp với quả cầu.

Sách nhấn mạnh rằng việc chọn cách mô tả có hệ quả thực tế rất lớn, bằng ví dụ quả cầu $\ell_\infty$ trong $\mathbb{R}^n$:

$$
\{x : |x_i| \le 1,\ i = 1, \ldots, n\} .
$$

Mô tả bằng ràng buộc chỉ cần $2n$ bất đẳng thức $\pm e_i^T x \le 1$. Mô tả bằng bao lồi cần ít nhất $2^n$ đỉnh, là mọi vector có các thành phần bằng $\pm 1$. Với $n = 50$, một bên là 100 bất đẳng thức, bên kia là hơn $10^{15}$ đỉnh. Với quả cầu $\ell_1$ thì ngược lại: nó có đúng $2n$ đỉnh $\pm e_i$, nhưng viết bằng bất đẳng thức tuyến tính theo cách trực tiếp cần $2^n$ bất đẳng thức $s^T x \le 1$ với $s \in \{-1, 1\}^n$.

Hai ví dụ này cho thấy một điều sâu sắc: một đa diện có thể "đơn giản" theo cách mô tả này nhưng "phức tạp" theo cách kia. Khi lập mô hình, chọn đúng cách mô tả đôi khi là sự khác nhau giữa một bài toán giải trong một giây và một bài toán không thể viết ra.

## 5. Những câu hỏi để đào sâu

**Câu 1.** Hình tròn đặc có phải là một đa diện không? Nó có là giao của các nửa mặt phẳng không?

<details><summary>Xem lời giải thích</summary>

Hình tròn là giao của **vô số** nửa mặt phẳng, chẳng hạn mọi nửa mặt phẳng $\{x : u^T x \le 1\}$ với $u$ là vector đơn vị. Nhưng nó không phải đa diện, vì đa diện chỉ dùng hữu hạn nửa không gian, nên biên của nó gồm hữu hạn đoạn thẳng, còn biên của hình tròn cong ở mọi điểm. Kết quả "mọi tập lồi đóng là giao của các nửa không gian chứa nó" sẽ được chứng minh ở chủ đề về siêu phẳng phân tách. Đa diện là trường hợp đặc biệt khi chỉ cần hữu hạn nửa không gian.

</details>

**Câu 2.** Một đa diện có thể không có đỉnh nào không? Nếu có, hãy cho ví dụ và giải thích điều gì ngăn nó có đỉnh.

<details><summary>Xem lời giải thích</summary>

Có. Một nửa mặt phẳng, một dải $\{x : 0 \le x_1 \le 1\}$ hay một đường thẳng đều là đa diện không có đỉnh. Điều chung giữa chúng là đều chứa trọn một đường thẳng. Có thể chứng minh rằng một đa diện khác rỗng có ít nhất một đỉnh khi và chỉ khi nó không chứa đường thẳng nào. Kết quả này quan trọng cho quy hoạch tuyến tính, vì phương pháp đơn hình đi từ đỉnh này sang đỉnh khác, và Lecture 07 sẽ dùng lại nó.

</details>

**Câu 3.** Ba vector $(1, 0, 0)$, $(0, 1, 0)$, $(1, 1, 0)$ có độc lập affine không? Bốn điểm $(0,0,0)$, $(1, 0, 0)$, $(0, 1, 0)$, $(1, 1, 0)$ thì sao?

<details><summary>Xem lời giải thích</summary>

Với ba điểm đầu, lấy $v_0 = (1, 0, 0)$: hai hiệu $(-1, 1, 0)$ và $(0, 1, 0)$ độc lập tuyến tính, nên ba điểm độc lập affine. Chúng không thẳng hàng, tạo thành một tam giác. Với bốn điểm sau, lấy $v_0 = 0$: ba hiệu $(1,0,0)$, $(0,1,0)$, $(1,1,0)$ phụ thuộc tuyến tính vì vector thứ ba là tổng hai vector đầu. Vậy bốn điểm không độc lập affine. Chúng là bốn đỉnh của một hình vuông nằm trong mặt phẳng $x_3 = 0$, và bao lồi của chúng không phải đơn hình.

</details>

**Câu 4.** Trong bài toán phân loại $n$ lớp, mô hình đưa ra một phân phối $p$ trên đơn hình xác suất. Phân phối "an toàn nhất" khi không biết gì là trọng tâm $\tfrac1n\mathbf{1}$. Theo nghĩa nào trọng tâm là điểm "ở giữa nhất" của đơn hình?

<details><summary>Xem lời giải thích</summary>

Có ít nhất ba nghĩa. Nó là trung bình cộng của $n$ đỉnh, tức tổ hợp lồi với các trọng số bằng nhau. Nó là điểm của đơn hình gần gốc tọa độ nhất theo chuẩn Euclid, vì cực tiểu $\|p\|_2^2$ với $\mathbf{1}^T p = 1$ cho nghiệm $p = \tfrac1n\mathbf{1}$. Và nó là phân phối có entropy lớn nhất, nghĩa là "ít thông tin nhất", điều mà ta sẽ chứng minh bằng tính lõm của entropy ở chủ đề về các hàm lồi thường gặp. Ba nghĩa này trùng nhau nhờ tính đối xứng của đơn hình.

</details>

## 6. Bài tập tự luyện

::: exercise 1. Tìm đỉnh
Tìm mọi đỉnh của đa diện

$$
\{x \in \mathbb{R}^2 : x_1 \ge 0,\ x_2 \ge 0,\ x_1 + 2x_2 \le 6,\ 2x_1 + x_2 \le 6\}
$$

và chỉ ra các ràng buộc chặt tại mỗi đỉnh.
:::

::: solution
Giải từng cặp ràng buộc ở dạng đẳng thức rồi giữ những giao điểm khả thi. $x_1 = 0, x_2 = 0$ cho $(0, 0)$. $x_2 = 0$ với $2x_1 + x_2 = 6$ cho $(3, 0)$. $x_1 = 0$ với $x_1 + 2x_2 = 6$ cho $(0, 3)$. Hai ràng buộc chéo $x_1 + 2x_2 = 6$, $2x_1 + x_2 = 6$ cho $(2, 2)$. Các giao điểm còn lại, như $(6, 0)$ hay $(0, 6)$, vi phạm một ràng buộc khác nên không phải đỉnh. Vậy có bốn đỉnh $(0,0)$, $(3, 0)$, $(2, 2)$, $(0, 3)$, mỗi đỉnh có đúng hai ràng buộc chặt.
:::

::: exercise 2. Đơn hình xác suất dưới dạng chuẩn
Viết đơn hình xác suất trong $\mathbb{R}^3$ dưới dạng $\{x : Ax \preceq b,\ Cx = d\}$, chỉ rõ $A, b, C, d$. Chiều affine của nó bằng bao nhiêu?
:::

::: solution
Các điều kiện $x_i \ge 0$ viết thành $-x_i \le 0$, nên $A = -I_3$ và $b = 0$. Điều kiện tổng bằng 1 cho $C = \begin{bmatrix} 1 & 1 & 1 \end{bmatrix}$ và $d = 1$. Chiều affine bằng 2, vì đơn hình nằm trong mặt phẳng $x_1 + x_2 + x_3 = 1$ và chứa ba điểm không thẳng hàng $e_1, e_2, e_3$.
:::

::: exercise 3. Tập nào là đa diện (theo Bài tập 2.8 trong sách)
Cho $a_1, a_2 \in \mathbb{R}^n$ và

$$
S = \{y_1 a_1 + y_2 a_2 : -1 \le y_1 \le 1,\ -1 \le y_2 \le 1\}.
$$

Tập $S$ có phải đa diện không? Gợi ý mô tả nó khi $n = 2$ và $a_1, a_2$ độc lập tuyến tính.
:::

::: solution
Có. $S$ là ảnh của hình vuông $[-1, 1]^2$ qua ánh xạ tuyến tính $y \mapsto y_1 a_1 + y_2 a_2$, nên bằng bao lồi của bốn điểm $\pm a_1 \pm a_2$, và bao lồi của hữu hạn điểm là đa diện. Khi $n = 2$ và $a_1, a_2$ độc lập, đặt $M = \begin{bmatrix} a_1 & a_2 \end{bmatrix}$ khả nghịch. Điểm $x$ thuộc $S$ khi và chỉ khi $y = M^{-1} x$ thỏa $-\mathbf{1} \preceq y \preceq \mathbf{1}$, tức là bốn bất đẳng thức tuyến tính $\pm (M^{-1}x)_i \le 1$. Đó là một hình bình hành có tâm tại gốc.
:::

## Tóm tắt

Đa diện là giao của hữu hạn nửa không gian và siêu phẳng, viết gọn là $\{x : Ax \preceq b,\ Cx = d\}$ với $\preceq$ là bất đẳng thức theo từng thành phần. Mọi đa diện đều lồi, có thể không bị chặn và có thể rỗng. Đơn hình là bao lồi của các điểm độc lập affine, gồm đoạn thẳng, tam giác, tứ diện và các tổng quát của chúng. Đơn hình xác suất là tập mọi phân phối xác suất trên hữu hạn kết quả, và đầu ra softmax nằm trong nội tương đối của nó.

Mỗi đơn hình viết được thành hệ đẳng thức và bất đẳng thức tuyến tính bằng phép đổi biến $x = v_0 + By$. Tổng quát hơn, mỗi đa diện có hai cách mô tả, bằng ràng buộc hoặc bằng đỉnh cùng hướng, và kích thước của hai cách mô tả có thể chênh nhau theo hàm mũ.

## Nguồn và đọc thêm

- S. Boyd, L. Vandenberghe, *Convex Optimization*, §2.2.4 (tr. 31–34), Hình 2.11, Ví dụ 2.4 và 2.5, biểu diễn (2.5)–(2.9), Bài tập 2.8.
- Định lý Minkowski–Weyl và điều kiện có đỉnh của đa diện: có thể xem D. Bertsimas, J. N. Tsitsiklis, *Introduction to Linear Optimization*, Athena Scientific, 1997, chương 2.
- Hai ví dụ tam giác, liên hệ với softmax và attention, các câu hỏi và bài tập 1, 2 do người soạn bổ sung. Mọi con số đã được tính lại bằng chương trình.
