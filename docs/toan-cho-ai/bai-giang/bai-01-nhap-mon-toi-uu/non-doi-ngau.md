---
course: toan-cho-ai
lecture: bai-01-nhap-mon-toi-uu
topic: non-doi-ngau
section: topic
title: "Nón đối ngẫu và lựa chọn Pareto"
description: "Định nghĩa và hình học của nón đối ngẫu, các nón tự đối ngẫu, đối ngẫu của nón chuẩn và chuẩn đối ngẫu, các tính chất K** = K, bất đẳng thức đối ngẫu, và cách tìm phần tử tối thiểu bằng cực tiểu một tổng có trọng số."
---

Ở chủ đề trước, ta thấy một tập lồi đóng được mô tả hoàn toàn bởi các nửa không gian chứa nó. Với một **nón**, câu chuyện còn gọn hơn: một nón lồi đóng được mô tả bởi các nửa không gian **có biên đi qua gốc** chứa nó. Mỗi nửa không gian như vậy có dạng $\{x : y^T x \ge 0\}$ và được xác định bởi một vector $y$. Tập tất cả những vector $y$ "nhìn" toàn bộ nón từ cùng một phía là một nón mới, gọi là **nón đối ngẫu**.

Nón đối ngẫu là cầu nối giữa hình học của chương này và lý thuyết đối ngẫu ở Lecture 03. Nó cũng trả lời một câu hỏi rất thực tế về các bài toán nhiều tiêu chí: nếu không có phương án nào tốt nhất ở mọi tiêu chí, làm sao tìm được những phương án "không bị trội"? Câu trả lời là cộng các tiêu chí với những trọng số dương, và nón đối ngẫu giải thích chính xác khi nào cách làm đó đúng.

## 1. Định nghĩa và hình học

> **Định nghĩa.** Cho $K$ là một nón. Tập
> $$K^* = \{y : x^T y \ge 0 \ \text{ với mọi } x \in K\}$$
> được gọi là **nón đối ngẫu** của $K$.

Mỗi vector $y \in K^*$ tạo với mọi vector của $K$ một góc không quá $90°$. Theo đúng tên gọi, $K^*$ là một nón, và nó **luôn lồi, kể cả khi $K$ không lồi**. Lý do: với mỗi $x \in K$ cố định, tập $\{y : x^T y \ge 0\}$ là một nửa không gian theo $y$, và $K^*$ là giao của tất cả các nửa không gian đó.

Sách đưa ra cách đọc hình học (Hình 2.22): $y \in K^*$ khi và chỉ khi nửa không gian $\{x : y^T x \ge 0\}$, có pháp tuyến hướng vào trong là $y$, chứa trọn nón $K$. Nói cách khác, $-y$ là pháp tuyến của một siêu phẳng tựa của $K$ tại gốc. Trong mô phỏng sau, vùng nhạt là nửa mặt phẳng $\{x : y^T x \ge 0\}$. Kéo vector $y$ quanh gốc và quan sát: $y$ thuộc vùng xanh, tức $K^*$, đúng khi nửa mặt phẳng nhạt chứa trọn nón tím $K$.

<ConeLab type="dual" />

Với một nón sinh bởi hữu hạn vector, chỉ cần kiểm tra các vector sinh. Nếu $K = \operatorname{cone}\{v_1, \ldots, v_k\}$ thì $y \in K^*$ khi và chỉ khi $y^T v_i \ge 0$ với mọi $i$, vì mọi phần tử của $K$ là tổ hợp không âm của các $v_i$. Chẳng hạn với $K = \operatorname{cone}\{(2, 1), (1, 3)\}$, ta có

$$
K^* = \{y : 2y_1 + y_2 \ge 0,\ y_1 + 3y_2 \ge 0\} = \operatorname{cone}\{(-1, 2),\ (3, -1)\}.
$$

Hai vector sinh của $K^*$ vuông góc với hai vector sinh của $K$: $(-1, 2)$ vuông góc với $(2, 1)$, còn $(3, -1)$ vuông góc với $(1, 3)$. Đây là quy tắc chung trong mặt phẳng: mỗi tia biên của $K^*$ vuông góc với một tia biên của $K$, và hướng vào phía của $K$.

Một hệ quả đáng nhớ thấy ngay trong mô phỏng: **nón càng rộng thì nón đối ngẫu càng hẹp**. Chính xác hơn, nếu $K_1 \subseteq K_2$ thì $K_2^* \subseteq K_1^*$, vì điều kiện "không âm trên cả $K_2$" khó thỏa hơn "không âm trên $K_1$". Ở thái cực, nón $\{0\}$ có đối ngẫu là cả không gian, còn cả không gian có đối ngẫu là $\{0\}$.

## 2. Những nón tự đối ngẫu và một cặp nón không đối xứng

**Không gian con** (Ví dụ 2.22). Đối ngẫu của một không gian con $V$ là phần bù trực giao $V^\perp = \{y : v^T y = 0 \text{ với mọi } v \in V\}$. Thật vậy, nếu $y^T v \ge 0$ với mọi $v \in V$, thì áp dụng cho cả $-v$ được $y^T v \le 0$, nên $y^T v = 0$.

**Góc phần tư không âm** (Ví dụ 2.23). Ta có $(\mathbb{R}^n_+)^* = \mathbb{R}^n_+$, và một nón như vậy được gọi là **tự đối ngẫu**. Nếu $y \succeq 0$ thì $x^T y = \sum_i x_i y_i \ge 0$ với mọi $x \succeq 0$. Ngược lại, nếu $y \in (\mathbb{R}^n_+)^*$, chọn $x = e_i$ được $y_i \ge 0$ với mọi $i$.

**Nón PSD** (Ví dụ 2.24). Trong không gian $\mathbb{S}^n$ với tích vô hướng $\langle X, Y\rangle = \operatorname{tr}(XY) = \sum_{i,j} X_{ij} Y_{ij}$, nón $\mathbb{S}^n_+$ cũng tự đối ngẫu: $\operatorname{tr}(XY) \ge 0$ với mọi $X \succeq 0$ khi và chỉ khi $Y \succeq 0$. Chứng minh có hai chiều, và mỗi chiều dùng một ý đẹp:

- Nếu $Y \not\succeq 0$, có $q$ với $q^T Y q < 0$. Chọn $X = qq^T \succeq 0$, ta có $\operatorname{tr}(XY) = q^T Y q < 0$, nên $Y \notin (\mathbb{S}^n_+)^*$. Các ma trận hạng một $qq^T$ là những "phép thử" đủ mạnh.
- Nếu $X, Y \succeq 0$, phân tích $X = \sum_i \lambda_i q_i q_i^T$ với $\lambda_i \ge 0$. Khi đó $\operatorname{tr}(XY) = \sum_i \lambda_i\, q_i^T Y q_i \ge 0$.

**Nón chuẩn và chuẩn đối ngẫu** (Ví dụ 2.25). Với một chuẩn $\|\cdot\|$, **chuẩn đối ngẫu** được định nghĩa là $\|u\|_* = \sup\{u^T x : \|x\| \le 1\}$, tức giá trị lớn nhất của hàm tuyến tính $u^T x$ trên quả cầu đơn vị. Theo chủ đề về siêu phẳng tựa, đó là "độ cao" của siêu phẳng tựa với pháp tuyến $u$. Sách chứng minh rằng đối ngẫu của nón chuẩn $K = \{(x, t) : \|x\| \le t\}$ là nón của chuẩn đối ngẫu:

$$
K^* = \{(u, v) : \|u\|_* \le v\}.
$$

Đối ngẫu của chuẩn Euclid là chính nó, nên nón bậc hai tự đối ngẫu. Đối ngẫu của $\|\cdot\|_1$ là $\|\cdot\|_\infty$ và ngược lại, vì $\sup\{u^T x : \|x\|_1 \le 1\} = \max_i |u_i|$, đạt tại một đỉnh $\pm e_i$ của quả cầu $\ell_1$. Vì vậy nón $\ell_1$ và nón $\ell_\infty$ là đối ngẫu của nhau mà không cái nào tự đối ngẫu. Cặp này cũng giải thích một nhận xét ở chủ đề về đa diện: quả cầu $\ell_1$ có ít đỉnh và nhiều mặt, quả cầu $\ell_\infty$ có nhiều đỉnh và ít mặt, như thể đỉnh của bên này là mặt của bên kia.

## 3. Các tính chất của nón đối ngẫu

Sách liệt kê các tính chất sau (Bài tập 2.31):

- $K^*$ đóng và lồi.
- $K_1 \subseteq K_2$ kéo theo $K_2^* \subseteq K_1^*$.
- Nếu $K$ có phần trong khác rỗng thì $K^*$ nhọn.
- Nếu bao đóng của $K$ nhọn thì $K^*$ có phần trong khác rỗng.
- $K^{**}$ là bao đóng của bao lồi của $K$. Đặc biệt, nếu $K$ lồi và đóng thì $K^{**} = K$.

Tính chất cuối là phiên bản "nón" của kết quả ở chủ đề trước: một nón lồi đóng được mô tả đầy đủ bởi các nửa không gian qua gốc chứa nó, và lấy đối ngẫu hai lần cho ta trở lại đúng nón ban đầu. Ghép các tính chất lại, **nếu $K$ là nón chính quy thì $K^*$ cũng là nón chính quy, và $K^{**} = K$**. Tính "đặc" và tính "nhọn" đổi chỗ cho nhau khi lấy đối ngẫu: nón không nhọn có đối ngẫu không đặc, và ngược lại. Bạn có thể thấy điều đó trong mô phỏng bằng cách kéo hai vector sinh của $K$ gần như ngược hướng: $K$ gần thành nửa mặt phẳng, không còn nhọn, và $K^*$ co lại gần thành một tia, không còn đặc.

## 4. Bất đẳng thức đối ngẫu: so sánh vector bằng mọi "phép đo dương"

Khi $K$ là nón chính quy, $K^*$ cũng sinh ra một bất đẳng thức tổng quát $\preceq_{K^*}$, gọi là **đối ngẫu** của $\preceq_K$. Hai bất đẳng thức liên hệ với nhau bởi:

$$
x \preceq_K y \iff \lambda^T x \le \lambda^T y \ \text{ với mọi } \lambda \succeq_{K^*} 0,
$$

$$
x \prec_K y \iff \lambda^T x < \lambda^T y \ \text{ với mọi } \lambda \succeq_{K^*} 0,\ \lambda \ne 0 .
$$

Đọc bằng lời: một bất đẳng thức giữa hai **vector** tương đương với vô số bất đẳng thức giữa các **số**, mỗi bất đẳng thức ứng với một cách "đo" $\lambda$ trong nón đối ngẫu. Với $K = \mathbb{R}^n_+$, điều này nói rằng $x \preceq y$ theo từng thành phần khi và chỉ khi mọi tổng có trọng số không âm của $x$ không vượt tổng tương ứng của $y$. Với thứ tự ma trận, $X \preceq Y$ khi và chỉ khi $\operatorname{tr}(ZX) \le \operatorname{tr}(ZY)$ với mọi $Z \succeq 0$. Đây là kỹ thuật chủ đạo trong các bài toán có bất đẳng thức tổng quát: chuyển một điều kiện về vector hay ma trận thành một họ điều kiện về số, rồi làm việc với các số.

Sách cũng mở rộng định lý lựa chọn của chủ đề trước sang bất đẳng thức tổng quát (Ví dụ 2.26): hệ $Ax \prec_K b$ vô nghiệm khi và chỉ khi có $\lambda \ne 0$ với $\lambda \succeq_{K^*} 0$, $A^T \lambda = 0$ và $\lambda^T b \le 0$. Vai trò của "trọng số không âm" giờ được đóng bởi các phần tử của nón đối ngẫu.

## 5. Tìm phần tử tối thiểu bằng tổng có trọng số

Ở chủ đề về bất đẳng thức tổng quát, ta đã thấy một tập có thể có nhiều phần tử tối thiểu và không có phần tử nhỏ nhất. Câu hỏi thực tế là làm sao **tìm** các phần tử tối thiểu. Nón đối ngẫu cho một câu trả lời rất tự nhiên: chọn một vector trọng số $\lambda$, rồi cực tiểu hóa một con số duy nhất $\lambda^T z$ trên tập $S$. Cách làm này được gọi là **vô hướng hóa**.

> **Mệnh đề (điều kiện đủ).** Nếu $\lambda \succ_{K^*} 0$ và $x$ cực tiểu $\lambda^T z$ trên $z \in S$, thì $x$ là phần tử tối thiểu của $S$.

Chứng minh rất ngắn. Giả sử $x$ không tối thiểu, tức có $z \in S$, $z \ne x$, với $z \preceq_K x$. Khi đó $x - z \in K \setminus \{0\}$, và vì $\lambda$ nằm trong phần trong của $K^*$, ta có $\lambda^T(x - z) > 0$, tức $\lambda^T z < \lambda^T x$. Điều này mâu thuẫn với việc $x$ cực tiểu $\lambda^T z$. Mệnh đề này **không cần $S$ lồi**.

Với $K = \mathbb{R}^n_+$, điều kiện $\lambda \succ_{K^*} 0$ nghĩa là mọi trọng số $\lambda_i$ **dương**. Sách diễn giải bằng ngôn ngữ kinh tế (Ví dụ 2.27): mỗi phương án sản xuất tiêu tốn một vector tài nguyên $x$ (lao động, nhiên liệu, ...), $\lambda_i$ là giá của tài nguyên thứ $i$, và $\lambda^T x$ là tổng chi phí. Phương án rẻ nhất theo một bảng giá dương bất kỳ chắc chắn là phương án **hiệu quả** theo nghĩa Pareto: không có phương án nào dùng ít hơn ở một tài nguyên mà không dùng nhiều hơn ở tài nguyên khác.

<OrderLab type="pareto" />

Chiều ngược lại thì tinh tế hơn, và có hai cái bẫy mà sách chỉ rõ:

- **Không phải phần tử tối thiểu nào cũng tìm được bằng trọng số dương.** Trong một tập hữu hạn, một điểm có thể tối thiểu mà nằm "lõm vào" so với các điểm tối thiểu khác. Chẳng hạn trong tập gồm $(3, 6)$, $(5, 4)$ và $(4, 5.4)$, điểm $(4, 5.4)$ không bị điểm nào trội, nhưng nó bằng trung điểm của hai điểm kia cộng thêm $(0, 0.4)$. Vì vậy với mọi $\lambda \succ 0$, giá trị $\lambda^T(4, 5.4)$ lớn hơn trung bình của hai giá trị kia, nên lớn hơn giá trị nhỏ nhất. Không trọng số dương nào chọn được nó.
- **Khi $S$ lồi, chiều ngược đúng nhưng chỉ với trọng số không âm.** Nếu $S$ lồi và $x$ tối thiểu, thì có $\lambda \succeq_{K^*} 0$, $\lambda \ne 0$, để $x$ cực tiểu $\lambda^T z$ trên $S$. Chứng minh dùng định lý siêu phẳng phân tách cho hai tập lồi $(x - K) \setminus \{x\}$ và $S$. Trọng số tìm được có thể nằm trên **biên** của $K^*$, chẳng hạn có một thành phần bằng 0, và không thể đòi nó dương ngặt. Ngược lại, một điểm cực tiểu $\lambda^T z$ với $\lambda$ trên biên của $K^*$ chưa chắc là tối thiểu (Hình 2.26 trong sách).

Còn **phần tử nhỏ nhất** có một đặc trưng gọn: $x$ là phần tử nhỏ nhất của $S$ khi và chỉ khi với **mọi** $\lambda \succ_{K^*} 0$, $x$ là điểm cực tiểu **duy nhất** của $\lambda^T z$ trên $S$. Một phần tử nhỏ nhất "thắng" theo mọi bảng giá dương.

Trong học máy, vô hướng hóa xuất hiện mỗi khi ta viết hàm mất mát dưới dạng tổng có trọng số của nhiều mục tiêu, chẳng hạn sai số trên dữ liệu cộng với $\rho$ lần độ phức tạp của mô hình. Mỗi giá trị $\rho > 0$ cho một mô hình nằm trên biên Pareto giữa "khớp dữ liệu" và "đơn giản". Khi bài toán lồi, đi qua mọi $\rho \ge 0$ (kể cả hai đầu mút) là đủ để quét hết biên đó. Khi bài toán không lồi, như huấn luyện mạng nơ-ron với nhiều mục tiêu, có thể có những điểm Pareto mà không trọng số nào tìm ra, đúng như ví dụ $(4, 5.4)$ ở trên.

## 6. Những câu hỏi để đào sâu

**Câu 1.** Nón đối ngẫu của một nửa mặt phẳng $\{x \in \mathbb{R}^2 : a^T x \ge 0\}$ là gì? Của một tia $\{t v : t \ge 0\}$ là gì?

<details><summary>Xem lời giải thích</summary>

Với nửa mặt phẳng $\{a^T x \ge 0\}$, chỉ những $y$ cùng hướng với $a$ mới cho $y^T x \ge 0$ với mọi $x$ trong nửa mặt phẳng, nên đối ngẫu là tia $\{t a : t \ge 0\}$. Với tia $\{tv : t \ge 0\}$, điều kiện chỉ là $y^T v \ge 0$, nên đối ngẫu là nửa mặt phẳng $\{y : v^T y \ge 0\}$. Hai ví dụ là đối ngẫu của nhau, đúng như $K^{**} = K$. Nửa mặt phẳng đặc nhưng không nhọn, đối ngẫu của nó là tia, nhọn nhưng không đặc.

</details>

**Câu 2.** Để biết $y$ có thuộc $K^*$ không, chỉ thử $y^T x \ge 0$ với một vài vector $x$ trong $K$ có đủ không? Cách làm ấy đúng trong trường hợp nào?

<details><summary>Xem lời giải thích</summary>

Định nghĩa đòi $y^T x \ge 0$ với **mọi** $x \in K$, nên thử vài vector nói chung không đủ. Tuy nhiên, nếu $K$ được sinh bởi hữu hạn vector $v_1, \ldots, v_k$, thì chỉ cần thử đúng các vector sinh, vì $y^T(\sum_i \alpha_i v_i) = \sum_i \alpha_i\, y^T v_i \ge 0$ khi mọi $\alpha_i \ge 0$. Với nón PSD, các "vector sinh" là các ma trận hạng một $qq^T$, có vô số, và đó là lý do kiểm tra $Y \succeq 0$ cần một lập luận chứ không chỉ vài phép thử.

</details>

**Câu 3.** Trong ví dụ sản xuất, nếu một tài nguyên được cho miễn phí (giá bằng 0), phương án rẻ nhất có chắc là hiệu quả không?

<details><summary>Xem lời giải thích</summary>

Không chắc. Với giá $\lambda = (1, 0)$, mọi phương án có cùng lượng tài nguyên thứ nhất đều rẻ như nhau, bất kể chúng dùng bao nhiêu tài nguyên thứ hai. Chẳng hạn hai phương án $(2, 1)$ và $(2, 5)$ có cùng chi phí 2, nhưng $(2, 5)$ bị $(2, 1)$ trội. Nếu thuật toán trả về $(2, 5)$ thì nó trả về một phương án không hiệu quả. Vì thế mệnh đề ở mục 5 đòi trọng số nằm trong **phần trong** của $K^*$, tức mọi giá đều dương.

</details>

## 7. Bài tập tự luyện

::: exercise 1. Tính một nón đối ngẫu
Tìm nón đối ngẫu của $K = \operatorname{cone}\{(1, 0), (1, 2)\}$ trong $\mathbb{R}^2$. Vector $y = (1, -0.4)$ có thuộc $K^*$ không?
:::

::: solution
$y \in K^*$ khi và chỉ khi $y^T(1, 0) = y_1 \ge 0$ và $y^T(1, 2) = y_1 + 2y_2 \ge 0$. Vậy

$$
K^* = \{y : y_1 \ge 0,\ y_1 + 2y_2 \ge 0\} = \operatorname{cone}\{(0, 1), (2, -1)\}.
$$

Với $y = (1, -0.4)$: $y_1 = 1 \ge 0$ và $1 - 0.8 = 0.2 \ge 0$, nên $y \in K^*$.
:::

::: exercise 2. Chuẩn đối ngẫu
Với $u = (3, -1, 2)$, tính $\|u\|_*$ khi chuẩn gốc là $\|\cdot\|_1$, rồi khi chuẩn gốc là $\|\cdot\|_\infty$. Chỉ ra điểm $x$ đạt giá trị lớn nhất của $u^T x$ trong mỗi trường hợp.
:::

::: solution
Với chuẩn gốc $\|\cdot\|_1$, chuẩn đối ngẫu là $\|u\|_\infty = 3$, đạt tại đỉnh $x = e_1 = (1, 0, 0)$ của quả cầu $\ell_1$. Với chuẩn gốc $\|\cdot\|_\infty$, chuẩn đối ngẫu là $\|u\|_1 = 3 + 1 + 2 = 6$, đạt tại đỉnh $x = (1, -1, 1)$ của hình lập phương, tức $x_i = \operatorname{sign}(u_i)$. Trong cả hai trường hợp, điểm tối ưu là một đỉnh của quả cầu, nơi siêu phẳng tựa với pháp tuyến $u$ chạm vào.
:::

::: exercise 3. Vô hướng hóa trên một tập hữu hạn
Cho các cấu hình $(2, 9)$, $(3, 6)$, $(5, 4)$, $(8, 3)$, $(6, 7)$, $(9, 8)$, hai tiêu chí đều muốn nhỏ. Tìm các phần tử tối thiểu. Với $\lambda = (1, 0.2)$, $(1, 1)$ và $(0.3, 1)$, điểm nào cực tiểu $\lambda^T z$? Kết quả với $\lambda = (1, 1)$ cho thấy điều gì?
:::

::: solution
$(6, 7)$ bị $(5, 4)$ trội, $(9, 8)$ bị nhiều điểm trội, nên các phần tử tối thiểu là $(2, 9)$, $(3, 6)$, $(5, 4)$, $(8, 3)$. Với $\lambda = (1, 0.2)$, các giá trị là $3.8, 4.2, 5.8, 8.6, 7.4, 10.6$, nên $(2, 9)$ được chọn. Với $\lambda = (1, 1)$, hai điểm $(3, 6)$ và $(5, 4)$ cùng cho giá trị 9 nhỏ nhất: đường mức $z_1 + z_2 = 9$ chạm cả cạnh nối hai điểm, nên nghiệm vô hướng hóa không duy nhất. Với $\lambda = (0.3, 1)$, các giá trị là $9.6, 6.9, 5.5, 5.4, 8.8, 10.7$, nên $(8, 3)$ được chọn. Mọi điểm được chọn đều là phần tử tối thiểu, đúng như mệnh đề ở mục 5.
:::

## Tóm tắt

Nón đối ngẫu $K^*$ gồm những vector tạo góc không quá $90°$ với mọi vector của $K$, tức những pháp tuyến của các nửa không gian qua gốc chứa $K$. Nó luôn lồi và đóng, nón càng rộng thì đối ngẫu càng hẹp, và với nón chính quy thì $K^*$ cũng chính quy và $K^{**} = K$. Góc phần tư không âm, nón PSD với tích vô hướng vết, và nón bậc hai là tự đối ngẫu, còn nón $\ell_1$ và nón $\ell_\infty$ đối ngẫu với nhau qua chuẩn đối ngẫu.

Một bất đẳng thức tổng quát tương đương với vô số bất đẳng thức số $\lambda^T x \le \lambda^T y$, mỗi $\lambda$ trong nón đối ngẫu. Cực tiểu tổng có trọng số $\lambda^T z$ với trọng số nằm trong phần trong của $K^*$ luôn cho một phần tử tối thiểu, nhưng không phải phần tử tối thiểu nào cũng tìm được theo cách đó. Khi tập lồi, mọi phần tử tối thiểu đều tìm được với một trọng số không âm khác 0.

## Nguồn và đọc thêm

- S. Boyd, L. Vandenberghe, *Convex Optimization*, §2.6 (tr. 51–58), Ví dụ 2.22–2.27, Hình 2.22–2.27, Bài tập 2.31. Chuẩn đối ngẫu ở phụ lục A.1.6.
- Ví dụ nón sinh bởi $(2, 1)$ và $(1, 3)$, ví dụ điểm tối thiểu không vô hướng hóa được, liên hệ với hàm mất mát có điều chuẩn, các câu hỏi và bài tập do người soạn bổ sung. Mọi con số đã được tính lại bằng chương trình.
