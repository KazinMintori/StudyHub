---
course: toan-cho-ai
lecture: bai-02-tap-loi
topic: khu-rang-buoc-va-toi-uu-tung-phan
section: topic
title: "Khử ràng buộc đẳng thức và tối ưu theo từng nhóm biến"
description: "Tham số hóa tập nghiệm của Ax = b để khử ràng buộc đẳng thức, ví dụ kết hợp ba phép đo theo nghịch đảo phương sai, khi nào không nên khử, thêm biến và ràng buộc đẳng thức, cực tiểu hóa theo một nhóm biến với phần bù Schur và hệ số chặn của hồi quy tuyến tính, cùng bảng các phép biến đổi giữ tính lồi."
---

Một ràng buộc đẳng thức tuyến tính như $x_1 + x_2 + x_3 = 1$ trông như một điều kiện phải canh chừng suốt quá trình giải. Thực ra nó còn là một thông tin: Nó nói rằng chỉ có hai trong ba biến được tự do, biến còn lại bị xác định. Dùng thông tin ấy, ta có thể bỏ hẳn ràng buộc và giải một bài toán ít biến hơn, không còn ràng buộc nào.

Trang này trình bày hai phép biến đổi cùng một tinh thần: **Khử ràng buộc đẳng thức** bằng cách tham số hóa tập nghiệm của nó, và **tối ưu theo từng nhóm biến**, tức giải trước phần dễ của bài toán rồi mới giải phần còn lại. Cả hai đều cho bài toán tương đương theo nghĩa của [chủ đề trước](./bai-toan-tuong-duong.md). Ta sẽ xem chúng giữ tính lồi ra sao, và cả cái giá phải trả khi dùng chúng.

## 1. Tham số hóa tập nghiệm của một hệ tuyến tính

Giả sử bài toán lồi có ràng buộc đẳng thức $Ax = b$, với $A \in \mathbb{R}^{p \times n}$. Nếu hệ vô nghiệm thì bài toán bất khả thi và không còn gì để làm. Nếu hệ có nghiệm, gọi $x_0$ là một nghiệm bất kỳ và $F \in \mathbb{R}^{n \times k}$ là một ma trận có không gian ảnh bằng đúng không gian hạch của $A$, tức $\mathcal{R}(F) = \mathcal{N}(A)$. Khi đó mọi nghiệm của $Ax = b$ có dạng

$$
x = Fz + x_0, \qquad z \in \mathbb{R}^k .
$$

Lý do rất đơn giản: Hiệu của hai nghiệm nằm trong hạch của $A$, và mọi vector trong hạch đều viết được thành $Fz$. Có thể chọn $F$ có các cột độc lập, khi đó $k = n - \operatorname{rank} A$. Thay vào bài toán, ta được

$$
\begin{aligned}
\text{minimize}\quad & f_0(Fz + x_0)\\
\text{subject to}\quad & f_i(Fz + x_0) \le 0, \quad i = 1, \ldots, m,
\end{aligned}
$$

theo biến $z$, không còn ràng buộc đẳng thức nào và ít hơn $\operatorname{rank} A$ biến. Từ nghiệm $z^\star$ ta lấy lại $x^\star = Fz^\star + x_0$. Ngược lại, mọi nghiệm $x^\star$ của bài toán gốc đều khả thi, nên viết được thành $Fz + x_0$ với một $z$ nào đó, và $z$ ấy là nghiệm của bài toán mới.

Tính lồi được giữ nguyên, vì hợp của một hàm lồi với một ánh xạ affine là hàm lồi. Đây là lý do sách nói rằng về nguyên tắc, ta có thể chỉ cần nghiên cứu những bài toán lồi không có ràng buộc đẳng thức.

## 2. Ví dụ: Kết hợp ba phép đo

Ba cảm biến cùng đo một đại lượng, cho ba kết quả không chệch, độc lập, với phương sai lần lượt là 1, 2 và 3. Ta muốn lấy trung bình có trọng số $x_1, x_2, x_3$ của ba kết quả. Để ước lượng vẫn không chệch, các trọng số phải cộng lại bằng 1. Phương sai của ước lượng tổng hợp là $x_1^2 + 2x_2^2 + 3x_3^2$, nên bài toán là

$$
\text{minimize}\quad x_1^2 + 2x_2^2 + 3x_3^2 \qquad \text{subject to}\quad x_1 + x_2 + x_3 = 1 .
$$

Chọn $x_0 = (1, 0, 0)$ và tham số hóa $x_2 = z_1$, $x_3 = z_2$, $x_1 = 1 - z_1 - z_2$. Bài toán thành cực tiểu không ràng buộc

$$
g(z) = (1 - z_1 - z_2)^2 + 2z_1^2 + 3z_2^2 .
$$

Cho hai đạo hàm riêng bằng 0, ta được hệ $3z_1 + z_2 = 1$ và $z_1 + 4z_2 = 1$, với nghiệm $z_1 = \tfrac{3}{11}$, $z_2 = \tfrac{2}{11}$. Vậy các trọng số tối ưu là

$$
x^\star = \left(\tfrac{6}{11},\ \tfrac{3}{11},\ \tfrac{2}{11}\right),
$$

và phương sai nhỏ nhất bằng $\tfrac{6}{11} \approx 0.545$, nhỏ hơn cả phương sai của cảm biến tốt nhất. Các trọng số tỉ lệ với $1, \tfrac12, \tfrac13$, tức tỉ lệ nghịch với phương sai: Cảm biến càng nhiễu càng được tin ít. Quy tắc trọng số theo nghịch đảo phương sai này là một kết quả kinh điển của thống kê, và ở đây nó rơi ra từ một phép khử biến.

Mô phỏng dưới đây cho thấy điều tương tự với một hàm hai biến. Đường thẳng $a^Tx = b$ được tham số hóa bởi một số $z$, và bài toán có ràng buộc trở thành bài toán cực tiểu một parabol.

<EliminationLab />

Mô phỏng còn cho thấy một điều sẽ trở thành trung tâm của Lecture 03. Tại nghiệm, gradient của $f$ vuông góc với đường ràng buộc, tức $\nabla f(x^\star) = \nu a$ với một số $\nu$ nào đó. Con số $\nu$ ấy chính là **nhân tử Lagrange** của ràng buộc đẳng thức.

## 3. Khi nào không nên khử

Nếu khử ràng buộc luôn được, vì sao người ta vẫn giữ chúng? Sách trả lời: Phép khử có thể làm bài toán khó hiểu hơn và phá hỏng cấu trúc mà thuật toán cần, đặc biệt là tính thưa khi số biến rất lớn.

Ví dụ trên cho thấy điều đó ở quy mô nhỏ. Hessian của hàm mục tiêu gốc theo $x$ là ma trận đường chéo $\operatorname{diag}(2, 4, 6)$, nhưng Hessian của $g$ theo $z$ là

$$
\nabla^2 g = \begin{bmatrix} 6 & 2 \\ 2 & 8 \end{bmatrix},
$$

không còn đường chéo nữa. Với $n$ biến và ràng buộc $\mathbf{1}^Tx = 1$, khử $x_n = 1 - x_1 - \cdots - x_{n-1}$ biến Hessian đường chéo thành một ma trận đường chéo cộng một ma trận hạng một mà mọi phần tử đều khác 0. Với $n$ cỡ một triệu, như khi tối ưu trên một phân phối xác suất có rất nhiều trạng thái, ma trận đường chéo lưu được dễ dàng, còn ma trận dày thì không. Phép khử còn phá vỡ tính đối xứng giữa các biến, vì một biến bị chọn ra để "chịu" ràng buộc. Vì thế phương pháp Newton cho bài toán có ràng buộc đẳng thức ở Lecture 04 giữ nguyên ràng buộc và xử lý nó trực tiếp bằng hệ Newton–KKT.

## 4. Thêm biến và ràng buộc đẳng thức

Chiều ngược lại cũng hữu ích. Khi một hàm có dạng $f_i(A_ix + b_i)$, ta có thể đặt biến mới $y_i = A_ix + b_i$ và viết

$$
\begin{aligned}
\text{minimize}\quad & f_0(y_0)\\
\text{subject to}\quad & f_i(y_i) \le 0, \quad i = 1, \ldots, m,\\
& y_i = A_ix + b_i, \quad i = 0, \ldots, m .
\end{aligned}
$$

Bài toán có thêm biến và thêm ràng buộc, nhưng hàm mục tiêu và các ràng buộc bất đẳng thức giờ đây độc lập với nhau, vì chúng phụ thuộc vào những biến khác nhau. Các ràng buộc mới tuyến tính, nên tính lồi được giữ nguyên. Chẳng hạn bài toán cực tiểu $\|Ax - b\|_1$ có thể viết thành cực tiểu $\|y\|_1$ với $y = Ax - b$: Phần không trơn của bài toán, chuẩn $\ell_1$, giờ chỉ tác động lên một biến riêng, còn dữ liệu $A, b$ nằm hết trong một ràng buộc tuyến tính. Mục 5.7.1 của sách cho thấy cách viết này có thể làm hàm đối ngẫu, đối tượng chính của Lecture 03, dễ tính hơn hẳn.

## 5. Tối ưu theo từng nhóm biến

Với mọi hàm $f$ của hai nhóm biến, ta luôn có

$$
\inf_{x, y} f(x, y) = \inf_x \tilde f(x), \qquad \tilde f(x) = \inf_y f(x, y).
$$

Nói cách khác, có thể cực tiểu trước theo một nhóm biến, được một hàm của nhóm còn lại, rồi mới cực tiểu hàm đó. Khi các ràng buộc tách riêng theo từng nhóm, phép biến đổi này cho một bài toán tương đương ít biến hơn. Nó đặc biệt có giá trị khi bước cực tiểu theo $y$ có công thức đóng.

**Hàm toàn phương và phần bù Schur.** Ví dụ 4.4 của sách xét một hàm toàn phương lồi chặt, với ràng buộc chỉ đặt lên $x_1$. Lấy một ví dụ số nhỏ:

$$
f(x_1, x_2) = 3x_1^2 + 2x_1x_2 + 2x_2^2 .
$$

Với $x_1$ cố định, đạo hàm theo $x_2$ là $2x_1 + 4x_2$, triệt tiêu tại $x_2 = -\tfrac{x_1}{2}$. Thay vào, ta được $\tilde f(x_1) = \tfrac52 x_1^2$. Hệ số $\tfrac52 = 3 - 1 \cdot \tfrac12 \cdot 1$ chính là **phần bù Schur** của khối $P_{22} = 2$ trong ma trận $\begin{bmatrix} 3 & 1 \\ 1 & 2 \end{bmatrix}$. Nếu thêm ràng buộc $x_1 \ge 1$, bài toán gốc tương đương cực tiểu $\tfrac52 x_1^2$ với $x_1 \ge 1$, có nghiệm $x_1 = 1$, và ta lấy lại $x_2 = -\tfrac12$ từ công thức của bước đầu. Chủ đề [phần bù Schur](./phan-bu-schur-va-bai-toan-tri-rieng.md) ở cuối chương sẽ khai thác công thức này một cách tổng quát.

**Hệ số chặn của hồi quy tuyến tính.** Bài toán bình phương tối thiểu với một đặc trưng và hệ số chặn là cực tiểu $\sum_i (y_i - wu_i - c)^2$ theo $(w, c)$. Cố định $w$, đạo hàm theo $c$ bằng 0 khi $c = \bar y - w\bar u$, với $\bar u, \bar y$ là trung bình của dữ liệu. Thay vào, phần còn lại là

$$
\tilde f(w) = \sum_i \big((y_i - \bar y) - w(u_i - \bar u)\big)^2 ,
$$

tức bài toán hồi quy **không có hệ số chặn** trên dữ liệu đã trừ trung bình. Với dữ liệu tự đặt $u = (1, 2, 4, 7)$ và $y = (3, 4, 9, 14)$, ta có $\bar u = 3.5$, $\bar y = 7.5$, và $w^\star = \tfrac{40}{21} \approx 1.905$, rồi $c^\star = 7.5 - w^\star \cdot 3.5 = \tfrac56$. Lời giải trực tiếp bằng bình phương tối thiểu hai biến cho đúng kết quả ấy. Đây là lý do việc chuẩn hóa dữ liệu về trung bình 0 trước khi huấn luyện không làm mất gì: Hệ số chặn đã được tối ưu sẵn.

Về tính lồi, sách khẳng định: Cực tiểu một hàm lồi đồng thời theo $(x, y)$ trên một nhóm biến cho một hàm lồi theo nhóm còn lại. Đó là phép toán [cực tiểu hóa theo một phần biến](../bai-01-nhap-mon-toi-uu/phep-toan-giu-tinh-loi-cua-ham.md) ở Lecture 01, nay được dùng như một phép biến đổi bài toán.

## 6. Phép biến đổi nào giữ tính lồi

Mục 4.2.4 của sách điểm lại các phép biến đổi của chủ đề trước và chủ đề này, và xét xem phép nào giữ được dạng chuẩn lồi.

| Phép biến đổi | Giữ tính lồi khi nào | Lý do |
| --- | --- | --- |
| Khử ràng buộc đẳng thức $Ax = b$ | luôn giữ | hợp của hàm lồi với ánh xạ affine $Fz + x_0$ |
| Thêm biến $y_i = A_ix + b_i$ | luôn giữ | ràng buộc mới tuyến tính |
| Thêm biến bù | chỉ cho bất đẳng thức affine | ràng buộc đẳng thức phải affine |
| Dạng epigraph | luôn giữ | $f_0(x) - t$ lồi theo $(x, t)$ |
| Cực tiểu theo một nhóm biến | khi $f_0$ lồi đồng thời theo mọi biến | cực tiểu hóa theo một phần biến giữ tính lồi |
| Đổi biến | không tự động | chỉ chắc chắn với đổi biến affine |

Dòng cuối là dòng dễ quên nhất. Đổi biến qua hàm mũ ở chủ đề trước làm một bài toán không lồi trở thành lồi, còn đổi biến $x = z^2$ thì làm một bài toán lồi mất tính lồi. Không có quy tắc chung, nên mỗi lần đổi biến phải kiểm tra lại.

## 7. Những câu hỏi để đào sâu

**Câu 1.** Ma trận $F$ trong phép tham số hóa $x = Fz + x_0$ không duy nhất. Đổi sang một ma trận $F'$ khác, cũng có $\mathcal{R}(F') = \mathcal{N}(A)$, thì nghiệm $x^\star$ và giá trị tối ưu có đổi không? Còn những gì có thể đổi?

<details><summary>Xem lời giải thích</summary>

Nghiệm $x^\star$ và giá trị tối ưu không đổi, vì cả hai cách tham số hóa đều mô tả đúng cùng một tập khả thi và cùng một hàm trên tập đó. Thứ thay đổi là biến $z$: Nếu các cột của $F$ và $F'$ đều độc lập thì $F' = FT$ với một ma trận khả nghịch $T$, và $z' = T^{-1}z$. Kéo theo đó, Hessian của hàm mới đổi thành $T^T(\nabla^2 g)T$, nên độ cong, số điều kiện và tốc độ của phương pháp gradient đều có thể khác. Chọn $F$ có các cột trực chuẩn là một lựa chọn tốt về mặt số học, vì khi đó phép tham số hóa không làm méo khoảng cách.

</details>

**Câu 2.** Trong ví dụ ba cảm biến, nếu thêm điều kiện mọi trọng số không âm thì nghiệm có đổi không? Còn nếu một cảm biến có phương sai rất lớn, chẳng hạn 1000?

<details><summary>Xem lời giải thích</summary>

Nghiệm không đổi, vì trọng số tối ưu tỉ lệ với nghịch đảo phương sai nên luôn dương: Điều kiện không âm thỏa sẵn, không chặt. Với phương sai 1000, trọng số của cảm biến ấy là $\tfrac{1/1000}{1 + 1/2 + 1/1000}$, khoảng $0.0007$. Cảm biến đó gần như bị bỏ qua, nhưng không bao giờ bị loại hẳn, vì mỗi phép đo độc lập dù nhiễu đến đâu vẫn mang thêm một chút thông tin. Trong mô hình này, trọng số chỉ bằng 0 khi phương sai lớn vô hạn.

</details>

**Câu 3.** Trong bước cực tiểu theo $x_2$ ở mục 5, ta cần $P_{22} = 2 > 0$. Nếu $P_{22} = 0$, chẳng hạn $f(x_1, x_2) = 3x_1^2 + 2x_1x_2$, chuyện gì xảy ra?

<details><summary>Xem lời giải thích</summary>

Với $x_1 \ne 0$ cố định, hàm $3x_1^2 + 2x_1x_2$ tuyến tính theo $x_2$ với hệ số $2x_1 \ne 0$, nên giảm về $-\infty$ theo một chiều. Vậy $\tilde f(x_1) = -\infty$ với mọi $x_1 \ne 0$, và $\tilde f(0) = 0$. Bài toán gốc không bị chặn dưới, và bước cực tiểu theo từng nhóm biến cho thấy điều đó ngay. Điều này phù hợp với hình học: Ma trận $\begin{bmatrix} 3 & 1 \\ 1 & 0 \end{bmatrix}$ có định thức $-1 < 0$, nên có một trị riêng âm, và hàm toàn phương không lồi. Phần bù Schur chỉ được định nghĩa khi khối bị khử khả nghịch, và nó cho kết luận về tính xác định dương khi khối ấy dương xác định.

</details>

**Câu 4.** Thêm biến $y = Ax - b$ làm bài toán lớn hơn. Vì sao một bài toán lớn hơn lại có thể dễ giải hơn?

<details><summary>Xem lời giải thích</summary>

Vì độ khó nằm ở cấu trúc nhiều hơn là ở số biến. Trong cách viết mới, chuẩn $\ell_1$ chỉ tác động lên $y$ và tách được theo từng thành phần, nên các phép tính như cực tiểu hóa từng phần hay phép chiếu có công thức đóng cho từng $y_i$. Ma trận $A$ chỉ còn xuất hiện trong một ràng buộc tuyến tính, nơi đại số tuyến tính xử lý rất hiệu quả. Nhiều thuật toán hiện đại cho bài toán lớn, kể cả trong học máy, dựa đúng vào việc tách bài toán thành những phần mà mỗi phần dễ xử lý. Đây là hình ảnh ngược với mục 3: Ở đó khử biến làm mất cấu trúc, ở đây thêm biến làm lộ cấu trúc.

</details>

**Câu 5.** Hồi quy tuyến tính có điều chuẩn ridge thường không phạt hệ số chặn: Hàm mục tiêu là $\sum_i (y_i - wu_i - c)^2 + \lambda w^2$. Lập luận ở mục 5 còn đúng không?

<details><summary>Xem lời giải thích</summary>

Còn đúng. Số hạng phạt không chứa $c$, nên với $w$ cố định, bước cực tiểu theo $c$ vẫn cho $c = \bar y - w\bar u$. Phần còn lại là ridge không hệ số chặn trên dữ liệu đã trừ trung bình. Nếu ta phạt cả $c$ thì kết luận đổi: Khi đó $c$ bị kéo về 0 và không còn bằng $\bar y - w\bar u$, và kết quả phụ thuộc vào việc dữ liệu có được trừ trung bình hay không. Đó là lý do người ta thường không phạt hệ số chặn.

</details>

## 8. Bài tập tự luyện

::: exercise 1. Khử một ràng buộc
Giải bài toán cực tiểu $x_1^2 + x_2^2 + x_3^2$ với $x_1 + 2x_2 + 3x_3 = 14$ bằng cách khử $x_1$. Kiểm tra rằng nghiệm tỉ lệ với vector hệ số $(1, 2, 3)$ và giải thích điều đó bằng hình học.
:::

::: hint
Sau khi khử, cho hai đạo hàm riêng theo $x_2, x_3$ bằng 0 rồi giải hệ hai phương trình.
:::

::: solution
Khử $x_1 = 14 - 2x_2 - 3x_3$, hàm mục tiêu thành $(14 - 2x_2 - 3x_3)^2 + x_2^2 + x_3^2$. Đạo hàm theo $x_2$ và $x_3$ bằng 0 cho $-4(14 - 2x_2 - 3x_3) + 2x_2 = 0$ và $-6(14 - 2x_2 - 3x_3) + 2x_3 = 0$, tức $10x_2 + 12x_3 = 56$ và $12x_2 + 20x_3 = 84$. Giải ra $x_2 = 2$, $x_3 = 3$, rồi $x_1 = 14 - 4 - 9 = 1$. Nghiệm $(1, 2, 3)$ đúng bằng vector hệ số, với giá trị tối ưu 14. Về hình học, ta đang tìm điểm gần gốc nhất của một mặt phẳng, và điểm đó là chân đường vuông góc hạ từ gốc, nằm theo hướng pháp tuyến $(1, 2, 3)$.
:::

::: exercise 2. Cực tiểu theo từng nhóm biến
Cho $f(x, y) = x^2 + 4xy + 5y^2 - 2y$. (a) Với $x$ cố định, tìm $y$ cực tiểu và hàm $\tilde f(x)$. (b) Giải bài toán cực tiểu $f$ với ràng buộc $x \ge 1$.
:::

::: solution
(a) Đạo hàm theo $y$ là $4x + 10y - 2$, triệt tiêu tại $y = \tfrac{1 - 2x}{5}$. Thay vào, $\tilde f(x) = x^2 - \tfrac{(4x - 2)^2}{20}$, rút gọn thành $\tfrac15 x^2 + \tfrac45 x - \tfrac15$. Hệ số $\tfrac15$ của $x^2$ bằng $1 - \tfrac{2 \cdot 2}{5}$, đúng phần bù Schur của khối $5$ trong ma trận $\begin{bmatrix} 1 & 2 \\ 2 & 5 \end{bmatrix}$. (b) Hàm $\tilde f$ là parabol có đỉnh tại $x = -2$, nên trên $x \ge 1$ nó tăng, và nghiệm là $x = 1$ với $\tilde f(1) = \tfrac15 + \tfrac45 - \tfrac15 = \tfrac45$. Lấy lại $y = \tfrac{1 - 2}{5} = -\tfrac15$, và kiểm tra trực tiếp $f(1, -\tfrac15) = 1 - \tfrac45 + \tfrac15 + \tfrac25 = \tfrac45$.
:::

::: exercise 3. Hệ số chặn
Với dữ liệu $u = (0, 1, 2, 5)$ và $y = (1, 2, 2, 7)$, tìm $(w, c)$ cực tiểu $\sum_i (y_i - wu_i - c)^2$ bằng cách cực tiểu theo $c$ trước.
:::

::: solution
Trung bình $\bar u = 2$ và $\bar y = 3$. Dữ liệu đã trừ trung bình là $u - \bar u = (-2, -1, 0, 3)$ và $y - \bar y = (-2, -1, -1, 4)$. Khi đó $w^\star = \tfrac{4 + 1 + 0 + 12}{4 + 1 + 0 + 9} = \tfrac{17}{14}$, khoảng $1.214$, và $c^\star = \bar y - w^\star\bar u = 3 - \tfrac{17}{7} = \tfrac47$, khoảng $0.571$.
:::

## Tóm tắt

Ràng buộc $Ax = b$ có thể khử bằng cách viết mọi nghiệm thành $Fz + x_0$, với $F$ có ảnh bằng hạch của $A$. Bài toán mới tương đương, giữ tính lồi và ít biến hơn, nhưng có thể mất tính thưa và tính đối xứng, nên trong thực tế người ta thường giữ ràng buộc. Chiều ngược lại, thêm biến cùng ràng buộc đẳng thức tuyến tính giúp tách các phần của bài toán ra khỏi nhau.

Cực tiểu theo từng nhóm biến cho một bài toán tương đương ít biến hơn, và giữ tính lồi khi hàm mục tiêu lồi đồng thời. Với hàm toàn phương, bước cực tiểu cho phần bù Schur. Với hồi quy tuyến tính, nó cho thấy hệ số chặn tối ưu chính là phép trừ trung bình của dữ liệu.

## Nguồn và đọc thêm

- S. Boyd, L. Vandenberghe, *Convex Optimization*, §4.1.3 (tr. 132–134) về khử và thêm ràng buộc đẳng thức, tối ưu theo một phần biến, Ví dụ 4.4. §4.2.4 (tr. 142–144) về những phép biến đổi giữ tính lồi. Phần bù Schur ở §A.5.5.
- Ví dụ ba cảm biến, mô phỏng, ví dụ về Hessian dày sau khi khử, ví dụ hệ số chặn và dữ liệu, các câu hỏi và bài tập do người soạn bổ sung. Mọi con số đã được tính lại bằng chương trình.
