---
course: toan-cho-ai
lecture: bai-01-nhap-mon-toi-uu
topic: da-dien-va-don-hinh
section: topic
title: "Đa diện và đơn hình"
description: "Đa diện là giao hữu hạn nửa không gian và siêu phẳng, ký hiệu Ax ⪯ b, đơn hình và độc lập affine, đơn hình xác suất, cách viết một đơn hình thành hệ bất đẳng thức, và hai cách mô tả đa diện bằng ràng buộc hoặc bằng đỉnh."
---

Quy hoạch tuyến tính, bài toán kinh điển và phổ biến bậc nhất của tối ưu hóa, có miền khả thi luôn được mô tả bằng một hệ các bất đẳng thức tuyến tính. Mỗi bất đẳng thức tương đương với việc cắt gọt không gian bằng một nửa không gian đóng, và phần giao còn lại sau khi áp đặt toàn bộ các ràng buộc chính là một **đa diện**. Thấu hiểu hình học của đa diện, xác định cấu trúc các đỉnh cực biên, kiểm tra tính bị chặn và tính khả thi là chìa khóa giải mã toàn bộ bản chất của quy hoạch tuyến tính.

Bài học này cũng giới thiệu **đơn hình**, cấu trúc đa diện nguyên thủy nhất: Đoạn thẳng, tam giác, tứ diện và các hình học tổng quát trong không gian nhiều chiều. Đặc biệt, đơn hình xác suất, tập hợp của mọi phân phối xác suất trên một không gian biến cố rời rạc hữu hạn, là đối tượng toán học xuất hiện liên tục trong học máy và trí tuệ nhân tạo. Cuối bài, ta sẽ đối chiếu hai cách mô tả đa diện: Bằng hệ ràng buộc nửa không gian (H-representation) hoặc bằng tập đỉnh và hướng cực biên (V-representation), cùng sự bùng nổ hàm mũ về độ phức tạp khi chuyển đổi giữa chúng.

## 1. Đa diện

> **Định nghĩa.** Một **đa diện** (polyhedron) là tập nghiệm của một số hữu hạn bất đẳng thức và đẳng thức tuyến tính:
> $$\mathcal{P} = \{x \in \mathbb{R}^n : a_j^T x \le b_j,\ j = 1, \ldots, m,\quad c_j^T x = d_j,\ j = 1, \ldots, p\}.$$

Nói cách khác, đa diện là giao của một số hữu hạn các nửa không gian đóng và siêu phẳng. Vì mỗi nửa không gian và mỗi siêu phẳng đều là tập lồi, đồng thời giao của một họ tùy ý các tập lồi luôn là một tập lồi, nên **mọi đa diện đều là tập lồi**. Hình ảnh trực quan của một đa diện chính là phần giao nhau của các nửa không gian, trong đó mỗi nửa không gian được phân định bởi một pháp tuyến $a_j$ hướng ra ngoài.

Ta thường sử dụng dạng biểu diễn ma trận cô đọng:

$$
\mathcal{P} = \{x \in \mathbb{R}^n : Ax \preceq b,\ Cx = d\},
$$

trong đó các hàng của ma trận $A \in \mathbb{R}^{m \times n}$ lần lượt là $a_1^T, \ldots, a_m^T$, các hàng của $C \in \mathbb{R}^{p \times n}$ là $c_1^T, \ldots, c_p^T$, và ký hiệu $u \preceq v$ giữa hai vector thể hiện quan hệ so sánh **trên từng thành phần**: Cụ thể $u_i \le v_i$ với mọi $i = 1, \dots, m$. Ký hiệu này khác biệt căn bản với dấu so sánh trên trục số thực: Hai vector $u = (1, 3)^T$ và $v = (2, 2)^T$ hoàn toàn không thể so sánh được theo thứ tự này vì $u_1 < v_1$ nhưng $u_2 > v_2$.

Nhiều tập hợp quen thuộc trong giải tích và đại số tuyến tính là đa diện: Tập affine (chỉ chứa các ràng buộc đẳng thức), tia, đoạn thẳng, nửa không gian đóng, và **nón phần tư không âm** $\mathbb{R}^n_+ = \{x \in \mathbb{R}^n : x \succeq 0\}$. Nón phần tư không âm vừa mang cấu trúc nón vừa là đa diện nên được gọi là **nón đa diện** (polyhedral cone).

Một đa diện có thể không bị chặn (chẳng hạn như một nửa không gian) và có thể rỗng khi hệ ràng buộc xảy ra mâu thuẫn. Một đa diện bị chặn được gọi là **đa đỉnh** (polytope). Trong y văn tối ưu hóa, các tác giả đôi khi dùng hai thuật ngữ đa diện (polyhedron) và đa đỉnh (polytope) theo những quy ước hoán đổi cho nhau, do đó việc đối chiếu định nghĩa giả thiết luôn là bước cẩn trọng cần thiết.

Mô phỏng tương tác dưới đây biểu diễn một đa diện trong mặt phẳng 2D được tạo thành từ giao của các nửa mặt phẳng. Các đường biên nét đứt đại diện cho các siêu phẳng ràng buộc, và miền tô màu là phần giao khả thi:

<PolyhedronLab />

Một trực giác hình học then chốt được thể hiện ở trạng thái các ràng buộc: Trong mặt phẳng $\mathbb{R}^2$, mỗi đỉnh của đa diện luôn có ít nhất hai ràng buộc đạt đẳng thức (ràng buộc chặt, active constraints), và hai đường thẳng biên cắt nhau chính xác tại đỉnh đó. Nguyên lý này tổng quát hóa thành định nghĩa đại số của đỉnh (basic feasible solution) trong không gian $\mathbb{R}^n$: Một điểm khả thi là một đỉnh khi và chỉ khi tồn tại ít nhất $n$ ràng buộc chặt với các vector pháp tuyến độc lập tuyến tính.

## 2. Đơn hình

Trước khi định nghĩa đơn hình, ta cần một khái niệm độc lập hình học tương thích với không gian affine.

> **Định nghĩa.** Tập hợp các điểm $v_0, v_1, \ldots, v_k \in \mathbb{R}^n$ được gọi là **độc lập affine** (affinely independent) nếu các vector hiệu $v_1 - v_0, \ldots, v_k - v_0$ độc lập tuyến tính trong không gian vector $\mathbb{R}^n$.

Ý nghĩa hình học: Ba điểm độc lập affine nghĩa là chúng không thẳng hàng (tạo thành một tam giác thực sự), bốn điểm độc lập affine nghĩa là chúng không đồng phẳng (tạo thành một tứ diện thực sự). Định nghĩa đo các vector hiệu so với mốc $v_0$, hoàn toàn độc lập với việc chọn gốc tọa độ. Việc thay thế $v_0$ bằng bất kỳ điểm nào khác trong tập điểm đều dẫn đến kết luận tương đương.

> **Định nghĩa.** Với $k + 1$ điểm độc lập affine $v_0, \dots, v_k$, **đơn hình** (simplex) xác định bởi chúng là bao lồi của các điểm này:
> $$C = \operatorname{conv}\{v_0, \ldots, v_k\} = \left\{\sum_{i=0}^k \theta_i v_i : \theta_i \ge 0,\ \sum_{i=0}^k \theta_i = \theta_0 + \theta_1 + \cdots + \theta_k = 1\right\}.$$

Đơn hình này có số chiều affine đúng bằng $k$, nên được gọi là một đơn hình $k$-chiều trong $\mathbb{R}^n$. Cụ thể: Đơn hình 1-chiều là một đoạn thẳng nối hai điểm, đơn hình 2-chiều là một tam giác đặc nối ba điểm, đơn hình 3-chiều là một khối tứ diện nối bốn điểm.

Hai họ đơn hình giữ vai trò nền tảng đặc biệt:

- **Đơn hình đơn vị** (Unit simplex): Được xác định bởi gốc tọa độ cùng các vector cơ sở chính tắc $\{0, e_1, \ldots, e_n\}$, biểu diễn dưới dạng tập hợp $\{x \in \mathbb{R}^n : x \succeq 0,\ \mathbf{1}^T x \le 1\}$. Đơn hình này có số chiều bằng $n$.
- **Đơn hình xác suất** (Probability simplex): Được xác định bởi các vector cơ sở chính tắc $\{e_1, \ldots, e_n\}$, biểu diễn dưới dạng tập hợp $\Delta^n = \{x \in \mathbb{R}^n : x \succeq 0,\ \mathbf{1}^T x = \sum_{i=1}^n x_i = 1\}$. Đơn hình này có số chiều affine bằng $n - 1$, và mỗi điểm $x \in \Delta^n$ tương ứng với một phân phối xác suất rời rạc trên $n$ biến cố, với $x_i là xác suất của biến cố thứ $i$.

Đơn hình xác suất là cấu trúc hình học trung tâm trong học máy: Đầu ra xác suất của hàm Softmax trong mạng nơ-ron phân loại đa lớp là một điểm nằm trong phần trong tương đối của đơn hình xác suất. Trọng số phân bổ của mô hình hỗn hợp Gaussian (GMM), hay các trọng số Attention trong kiến trúc Transformer, đều là các phần tử của đơn hình xác suất. Mỗi đỉnh $e_i$ biểu thị một quyết định tuyệt đối (xác suất 100% cho lớp $i$), trong khi trọng tâm $\tfrac{1}{n} \mathbf{1}$ biểu thị trạng thái hoàn toàn ngẫu nhiên và bất định (phân phối đều với entropy cực đại).

## 3. Chuyển đổi biểu diễn đơn hình sang hệ bất đẳng thức

Định nghĩa đơn hình xuất phát từ góc nhìn tập đỉnh (tổ hợp lồi). Tuy nhiên, vì đơn hình là một đa diện, nó hoàn toàn có thể được biểu diễn tường minh dưới dạng một hệ bất đẳng thức và đẳng thức tuyến tính. Ta hoàn toàn có thể chuyển đổi biểu diễn này bằng một lập luận đổi biến affine mẫu mực:

Mọi điểm $x$ thuộc đơn hình đều có dạng $x = \theta_0 v_0 + \theta_1 v_1 + \cdots + \theta_k v_k$. Thay thế $\theta_0 = 1 - \sum_{i=1}^k \theta_i$, ta thu được biểu thức tương đương:

$$
x = v_0 + \sum_{i=1}^k \theta_i (v_i - v_0) = v_0 + By, \qquad y = (\theta_1, \ldots, \theta_k)^T,
$$

với ma trận $B = \begin{bmatrix} v_1 - v_0 & \cdots & v_k - v_0 \end{bmatrix} \in \mathbb{R}^{n \times k}$. Điều kiện đối với vector $\theta$ quy về $y \succeq 0$ và $\mathbf{1}^T y \le 1$ (do $\theta_0 = 1 - \mathbf{1}^T y \ge 0$). Do các điểm độc lập affine, ma trận $B$ có các cột độc lập tuyến tính, tức hạng $\operatorname{rank}(B) = k$. Khi đó tồn tại một ma trận không suy biến $A = \begin{bmatrix} A_1 \\ A_2 \end{bmatrix} \in \mathbb{R}^{n \times n}$ sao cho $AB = \begin{bmatrix} I_k \\ 0 \end{bmatrix}$.

Nhân cả hai vế của $x = v_0 + By$ với $A$ từ bên trái, ta phân rã thành hai hệ phương trình: $A_1 x = A_1 v_0 + y$ và $A_2 x = A_2 v_0$. Từ phương trình thứ nhất ta rút ra $y = A_1 (x - v_0)$. Thay biểu thức này vào các điều kiện của $y$, ta nhận được hệ điều kiện cần và đủ để $x$ thuộc đơn hình như sau:

$$
A_2 x = A_2 v_0, \qquad A_1 x \succeq A_1 v_0, \qquad \mathbf{1}^T A_1 x \le 1 + \mathbf{1}^T A_1 v_0 .
$$

Hệ trên hoàn toàn bao gồm các đẳng thức và bất đẳng thức tuyến tính theo biến $x$. Ràng buộc $A_2 x = A_2 v_0$ định vị điểm $x$ nằm trọn vẹn trong không gian con affine $k$-chiều sinh bởi đơn hình, trong khi các bất đẳng thức bảo đảm các tọa độ trọng tâm (barycentric coordinates) đều không âm và có tổng không vượt quá 1.

::: example Chuyển đổi biểu diễn tam giác trong mặt phẳng và không gian
Xét tam giác trong $\mathbb{R}^2$ với ba đỉnh $v_0 = (1, 1)^T$, $v_1 = (3, 1)^T$ và $v_2 = (1, 4)^T$. Ma trận vector hiệu là $B = \begin{bmatrix} 2 & 0 \\ 0 & 3 \end{bmatrix}$. Vì $B$ khả nghịch nên ta chọn ngay $A = A_1 = B^{-1} = \begin{bmatrix} 1/2 & 0 \\ 0 & 1/3 \end{bmatrix}$, và không xuất hiện thành phần $A_2$.

Điều kiện $y = B^{-1}(x - v_0) \succeq 0$ dẫn tới $x_1 \ge 1$ và $x_2 \ge 1$. Điều kiện $\mathbf{1}^T y \le 1$ tương đương với $\tfrac{x_1 - 1}{2} + \tfrac{x_2 - 1}{3} \le 1 \iff 3x_1 + 2x_2 \le 11$. Ta thu được hệ ba bất đẳng thức mô tả trọn vẹn tam giác.

Xét tiếp tam giác trong $\mathbb{R}^3$ có các đỉnh $v_0 = (0, 0, 1)^T$, $v_1 = (1, 0, 1)^T$ và $v_2 = (0, 1, 1)^T$. Ma trận $B = \begin{bmatrix} 1 & 0 \\ 0 & 1 \\ 0 & 0 \end{bmatrix}$ có hạng bằng 2. Chọn ma trận biến đổi $A = I_3$, trong đó $A_1$ gồm hai hàng đầu và $A_2 = \begin{bmatrix} 0 & 0 & 1 \end{bmatrix}$. Khi đó hệ thu được gồm: Phương trình mặt phẳng $x_3 = 1$, cùng các bất đẳng thức $x_1 \ge 0$, $x_2 \ge 0$ và $x_1 + x_2 \le 1$.
:::

## 4. Hai cách mô tả đa diện: Đối ngẫu H-representation và V-representation

Bao lồi của một tập hợp hữu hạn điểm $\operatorname{conv}\{v_1, \ldots, v_k\}$ luôn là một đa diện bị chặn (polytope). Ta có một kết quả mở rộng quan trọng: Tập hợp

$$
\left\{\sum_{i=1}^k \theta_i v_i : \sum_{i=1}^m \theta_i = 1,\ \theta_i \ge 0,\ i = 1, \ldots, k\right\}, \qquad m \le k,
$$

chính là tổng Minkowski của bao lồi của $v_1, \ldots, v_m$ và bao nón (conical hull) của $v_{m+1}, \ldots, v_k$. Tập hợp này luôn là một đa diện. Ngược lại, ta có định lý nền tảng: **Mọi đa diện đều viết được dưới dạng bao lồi của hữu hạn điểm cộng bao nón của hữu hạn hướng cực biên**. Đây chính là nội dung của **Định lý Minkowski–Weyl**.

Do đó, mỗi đa diện đều sở hữu hai lăng kính toán học:
1. **Mô tả bằng nửa không gian (H-representation)**: Biểu diễn qua hệ ràng buộc $Ax \preceq b,\ Cx = d$. Cách tiếp cận này trả lời tức thì câu hỏi: "Làm thế nào để kiểm tra một điểm cho trước có thuộc đa diện hay không?" (chỉ cần nhân ma trận và kiểm tra dấu).
2. **Mô tả bằng đỉnh và tia cực biên (V-representation)**: Biểu diễn qua các đỉnh và hướng suy biến. Cách tiếp cận này trả lời câu hỏi: "Làm thế nào để sinh ra toàn bộ các điểm thuộc đa diện?" (lấy tổ hợp lồi và tổ hợp nón).

Việc chọn cách mô tả có hệ quả tính toán mang tính sống còn trong thực tế. Hãy quan sát quả cầu chuẩn $\ell_\infty$ trong $\mathbb{R}^n$:

$$
\{x \in \mathbb{R}^n : |x_i| \le 1,\ i = 1, \ldots, n\}.
$$

- Theo H-representation: Chỉ cần đúng $2n$ bất đẳng thức tuyến tính dạng $\pm e_i^T x \le 1$.
- Theo V-representation: Đòi hỏi toàn bộ $2^n$ đỉnh cực biên, gồm tất cả các vector có tọa độ nhận giá trị $\pm 1$. Với số chiều $n = 50$, một bên là 100 bất đẳng thức rất gọn nhẹ, trong khi bên kia đòi hỏi lưu trữ hơn $10^{15}$ đỉnh.

Ngược lại, hãy quan sát quả cầu chuẩn $\ell_1$ (khối bát diện đều nhiều chiều - cross-polytope):
- Theo V-representation: Chỉ có đúng $2n$ đỉnh cực biên là $\pm e_i$.
- Theo H-representation: Để mô tả trực tiếp các mặt ngoài, ta cần tới $2^n$ bất đẳng thức tuyến tính dạng $s^T x \le 1$ với mọi vector dấu $s \in \{-1, 1\}^n$.

Sự tương phản này mang lại một bài học trực giác sâu sắc trong tối ưu hóa: Một bài toán có thể rất đơn giản ở biểu diễn này nhưng lại bùng nổ độ phức tạp theo hàm mũ ở biểu diễn kia. Trong lập mô hình học máy, lựa chọn cấu trúc biểu diễn phù hợp quyết định ranh giới giữa một thuật toán giải trong một giây và một bài toán hoàn toàn không thể giải quyết.

## 5. Những câu hỏi để đào sâu

**Câu 1.** Một hình tròn đóng trong $\mathbb{R}^2$ có phải là một đa diện không? Nó có thể biểu diễn như giao của các nửa mặt phẳng hay không?

<details><summary>Xem lời giải thích</summary>

Hình tròn đóng là giao của **vô hạn** các nửa mặt phẳng đóng, chẳng hạn họ các nửa mặt phẳng $\{x \in \mathbb{R}^2 : u^T x \le 1\}$ với mọi vector đơn vị $\|u\|_2 = 1$. Tuy nhiên, nó không phải là một đa diện, bởi vì định nghĩa của đa diện bắt buộc số lượng nửa không gian tham gia phép giao phải là **hữu hạn**. Biên của một đa diện luôn gồm các đoạn thẳng hoặc diện phẳng, trong khi biên của hình tròn có độ cong dương tại mọi điểm.

</details>

**Câu 2.** Một đa diện có thể không có bất kỳ đỉnh nào không? Nếu có, điều kiện cấu trúc nào giải thích hiện tượng này?

<details><summary>Xem lời giải thích</summary>

Hoàn toàn có thể. Một nửa không gian đóng, một dải vô hạn $\{x \in \mathbb{R}^2 : 0 \le x_1 \le 1\}$ hay một đường thẳng đều là các đa diện nhưng không có đỉnh nào. Đặc điểm chung của chúng là đều chứa trọn vẹn ít nhất một đường thẳng vô hạn đi qua không gian. Người ta chứng minh được rằng: Một đa diện không rỗng có ít nhất một đỉnh khi và chỉ khi nó không chứa bất kỳ đường thẳng vô hạn nào. Kết quả này là tiền đề trọng yếu cho phương pháp Đơn hình (Simplex algorithm) trong quy hoạch tuyến tính.

</details>

**Câu 3.** Ba vector $(1, 0, 0)^T$, $(0, 1, 0)^T$, $(1, 1, 0)^T$ có độc lập affine không? Bốn điểm $(0,0,0)^T$, $(1, 0, 0)^T$, $(0, 1, 0)^T$, $(1, 1, 0)^T$ thì sao?

<details><summary>Xem lời giải thích</summary>

Với ba điểm đầu, chọn mốc $v_0 = (1, 0, 0)^T$: Hai vector hiệu là $(-1, 1, 0)^T$ và $(0, 1, 0)^T$ rõ ràng độc lập tuyến tính, do đó ba điểm này độc lập affine. Chúng tạo thành ba đỉnh của một tam giác.

Với bốn điểm sau, chọn mốc $v_0 = 0$: Ba vector hiệu $(1,0,0)^T$, $(0,1,0)^T$, $(1,1,0)^T$ phụ thuộc tuyến tính vì vector thứ ba bằng tổng hai vector đầu. Do đó bốn điểm này không độc lập affine. Chúng là bốn đỉnh của một hình vuông phẳng, và bao lồi của chúng không phải là một đơn hình mà là một đa diện 2 chiều thông thường.

</details>

**Câu 4.** Trong bài toán phân loại đa lớp, vì sao trọng tâm $\tfrac{1}{n}\mathbf{1}$ của đơn hình xác suất được xem là trạng thái "vô thiên lệch" nhất?

<details><summary>Xem lời giải thích</summary>

Trọng tâm của đơn hình xác suất hội tụ ba tính chất hình học và thông tin tối ưu:
1. Về hình học: Nó là trung bình cộng đối xứng của toàn bộ $n$ đỉnh cực biên.
2. Về khoảng cách: Nó là điểm thuộc đơn hình xác suất gần gốc tọa độ nhất theo chuẩn Euclid, tức nghiệm duy nhất của bài toán $\min \|p\|_2^2$ với ràng buộc $\mathbf{1}^T p = 1,\ p \succeq 0$.
3. Về lý thuyết thông tin: Nó là phân phối tối đa hóa hàm Entropy $H(p) = -\sum_{i=1}^n p_i \ln p_i$, đại diện cho trạng thái bất định hoàn toàn khi mô hình không có bất kỳ bằng chứng định kiến nào.

</details>

## 6. Bài tập tự luyện

::: exercise 1. Tìm đỉnh của đa diện
Tìm toàn bộ các đỉnh của đa diện sau trong $\mathbb{R}^2$:

$$
\mathcal{P} = \{x \in \mathbb{R}^2 : x_1 \ge 0,\ x_2 \ge 0,\ x_1 + 2x_2 \le 6,\ 2x_1 + x_2 \le 6\}
$$

và chỉ rõ các ràng buộc chặt tại từng đỉnh.
:::

::: solution
Ta giải phương trình giao điểm của từng cặp ràng buộc biên độc lập và kiểm tra tính khả thi:
- Giao của $x_1 = 0$ và $x_2 = 0$ cho đỉnh $(0, 0)$.
- Giao của $x_2 = 0$ và $2x_1 + x_2 = 6$ cho đỉnh $(3, 0)$.
- Giao của $x_1 = 0$ và $x_1 + 2x_2 = 6$ cho đỉnh $(0, 3)$.
- Giao của hai ràng buộc $x_1 + 2x_2 = 6$ và $2x_1 + x_2 = 6$ cho nghiệm $(2, 2)$, điểm này thỏa mãn cả hai ràng buộc không âm nên là một đỉnh khả thi.

Các giao điểm khác như $(6, 0)$ hay $(0, 6)$ vi phạm các ràng buộc còn lại nên bị loại. Đa diện có đúng bốn đỉnh gồm: $(0, 0)$, $(3, 0)$, $(2, 2)$, $(0, 3)$, mỗi đỉnh đều được xác định bởi đúng hai ràng buộc chặt độc lập.
:::

::: exercise 2. Đơn hình xác suất dưới dạng chuẩn ma trận
Hãy biểu diễn đơn hình xác suất trong không gian $\mathbb{R}^3$ dưới dạng chuẩn $\{x \in \mathbb{R}^3 : Ax \preceq b,\ Cx = d\}$, chỉ rõ cấu trúc của $A, b, C, d$. Số chiều affine của tập này bằng bao nhiêu?
:::

::: solution
Các ràng buộc không âm $x_i \ge 0$ được viết lại thành $-x_i \le 0$, do đó ta có $A = -I_3$ và $b = 0 \in \mathbb{R}^3$.

Ràng buộc tổng xác suất bằng 1 được biểu diễn bởi $C = \begin{bmatrix} 1 & 1 & 1 \end{bmatrix}$ và $d = 1$.

Chiều affine của đơn hình xác suất bằng $3 - 1 = 2$, vì tập hợp nằm trọn trong mặt phẳng 2 chiều $x_1 + x_2 + x_3 = 1$ và bao lồi chứa ba điểm độc lập affine $e_1, e_2, e_3$.
:::

::: exercise 3. Nhận dạng tập đa diện
Cho hai vector $a_1, a_2 \in \mathbb{R}^n$ và tập hợp:

$$
S = \{y_1 a_1 + y_2 a_2 : -1 \le y_1 \le 1,\ -1 \le y_2 \le 1\}.
$$

Tập hợp $S$ có phải là một đa diện hay không? Hãy mô tả cấu trúc của nó khi $n = 2$ và hai vector $a_1, a_2$ độc lập tuyến tính.
:::

::: solution
Tập $S$ chính là ảnh của hình vuông đơn vị $[-1, 1]^2$ qua ánh xạ tuyến tính $y \mapsto y_1 a_1 + y_2 a_2$. Do đó $S$ là bao lồi của bốn điểm cực biên $\pm a_1 \pm a_2$. Vì bao lồi của một tập hữu hạn điểm luôn là một đa diện, nên $S$ chắc chắn là một đa diện.

Khi $n = 2$ và $a_1, a_2$ độc lập tuyến tính, đặt ma trận khả nghịch $M = \begin{bmatrix} a_1 & a_2 \end{bmatrix} \in \mathbb{R}^{2 \times 2}$. Một điểm $x \in S$ khi và chỉ khi $y = M^{-1} x$ thỏa mãn $-\mathbf{1} \preceq y \preceq \mathbf{1}$, tương đương với hệ bốn bất đẳng thức tuyến tính: Cụ thể là $|(M^{-1} x)_1| \le 1$ và $|(M^{-1} x)_2| \le 1$. Về mặt hình học, đây là một hình bình hành đóng có tâm đối xứng tại gốc tọa độ.
:::

## Tóm tắt

Đa diện là tập nghiệm của một hệ hữu hạn các bất đẳng thức và đẳng thức tuyến tính, biểu diễn ma trận là $\{x : Ax \preceq b,\ Cx = d\}$. Mọi đa diện đều lồi, có thể bị chặn hoặc không bị chặn. Đơn hình là bao lồi của một tập điểm độc lập affine, bao gồm các cấu trúc hình học cơ bản như đoạn thẳng, tam giác và tứ diện. Đơn hình xác suất mô tả không gian của các phân phối rời rạc và là nền tảng của các hàm kích hoạt softmax và trọng số attention trong trí tuệ nhân tạo.

Định lý Minkowski–Weyl thiết lập sự tương đương giữa hai cách mô tả đa diện: Biểu diễn bằng nửa không gian (H-rep) và biểu diễn bằng đỉnh cực biên (V-rep). Chuyển đổi giữa hai biểu diễn này có thể dẫn đến sự bùng nổ kích thước theo hàm mũ, đòi hỏi sự lựa chọn thận trọng trong thiết kế mô hình toán học và thuật toán tối ưu.

## Tài liệu tham khảo
- Stephen Boyd, Lieven Vandenberghe, *Convex Optimization*, Cambridge University Press.

