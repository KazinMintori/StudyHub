---
course: toan-cho-ai
lecture: bai-02-tap-loi
topic: quy-hoach-tuyen-tinh
section: topic
title: "Quy hoạch tuyến tính: Các dạng viết và hình học của nghiệm"
description: "Dạng tổng quát của quy hoạch tuyến tính, hình học của nghiệm trên đa diện với bốn khả năng có nghiệm duy nhất, có cả một tập nghiệm, không bị chặn và bất khả thi, dạng chuẩn và dạng bất đẳng thức, cách chuyển một LP bất kỳ về dạng chuẩn bằng biến bù và tách biến tự do, cùng vì sao không thể liệt kê đỉnh."
---

Quy hoạch tuyến tính là dạng bài toán tối ưu được ứng dụng rộng rãi nhất trong thực tế, từ lập kế hoạch sản xuất, điều phối vận tải tới phân bổ ngân sách. [Lecture 01](../bai-01-nhap-mon-toi-uu/hai-lop-bai-toan-kinh-dien.md) đã giới thiệu LP qua một ví dụ hai biến và một chứng nhận tối ưu. Bài giảng này xem xét LP một cách hệ thống và bài bản: Các dạng biểu diễn chuẩn tắc, vị trí nghiệm trên miền khả thi hình học, và bản chất biến đổi giúp đưa mọi bài toán LP về cùng một dạng duy nhất.

## 1. Dạng tổng quát

Khi hàm mục tiêu và mọi hàm ràng buộc đều affine, bài toán được gọi là một **quy hoạch tuyến tính** (linear program, LP). Dạng tổng quát của nó là

$$
\begin{aligned}
\text{minimize}\quad & c^Tx + d\\
\text{subject to}\quad & Gx \preceq h,\\
& Ax = b,
\end{aligned}
$$

với $G \in \mathbb{R}^{m \times n}$ và $A \in \mathbb{R}^{p \times n}$. Ký hiệu $\preceq$ là bất đẳng thức theo từng thành phần. LP hiển nhiên là bài toán lồi.

Hằng số $d$ không làm thay đổi nghiệm, nên người ta thường bỏ nó đi, nhưng nhớ rằng nó vẫn làm thay đổi giá trị tối ưu. Bài toán cực đại một hàm affine trên cùng loại ràng buộc cũng được gọi là LP, vì cực đại $c^Tx + d$ tương đương cực tiểu $-c^Tx - d$. Trong thực tế tối ưu hóa, ta cũng thường mở rộng định nghĩa: Một bài toán có thể đưa về LP bằng các phép biến đổi tương đương cũng được xem là LP, dù ban đầu nó chưa xuất hiện ở dạng chuẩn tắc. Bài toán khớp dữ liệu theo sai số tệ nhất ở Lecture 01 là một ví dụ như vậy.

## 2. Hình học của nghiệm

Miền khả thi của một LP là một [đa diện](../bai-01-nhap-mon-toi-uu/da-dien-va-don-hinh.md) $\mathcal{P}$, giao của hữu hạn nửa không gian và siêu phẳng. Các tập mức $\{x : c^Tx = k\}$ của hàm mục tiêu là những siêu phẳng song song, cùng vuông góc với $c$. Giảm $k$ nghĩa là tịnh tiến siêu phẳng theo hướng $-c$. Vì thế nghiệm tối ưu là điểm của $\mathcal{P}$ nằm **xa nhất theo hướng $-c$**: Ta đẩy siêu phẳng mức theo hướng $-c$ cho tới khi nó sắp rời khỏi đa diện.

Hình ảnh này cho thấy ngay bốn khả năng có thể xảy ra.

- **Nghiệm duy nhất tại một đỉnh.** Đây là trường hợp thường gặp khi $c$ không vuông góc với cạnh nào của đa diện.
- **Cả một cạnh, hay một mặt, là tập nghiệm.** Điều này xảy ra khi $c$ vuông góc với cạnh hay mặt đó và nó nằm ở phía xa nhất theo hướng $-c$.
- **Không bị chặn dưới.** Nếu đa diện kéo dài vô hạn theo một hướng $r$ với $c^Tr < 0$, thì đi theo hướng $r$ làm giá trị giảm mãi, và $p^\star = -\infty$.
- **Bất khả thi.** Đa diện rỗng, và $p^\star = +\infty$.

Mô phỏng dưới đây cho phép người học tùy ý xoay vector $c$ và quan sát trực quan các trạng thái khả thi của bài toán.

<LPDirectionLab />

Nhận xét "nghiệm nằm ở một đỉnh" cần được phát biểu cẩn thận. Đúng là nếu đa diện có ít nhất một đỉnh và LP có giá trị tối ưu hữu hạn, thì có một nghiệm tối ưu là đỉnh. Nhưng có những đa diện không có đỉnh nào, chẳng hạn một dải $\{x \in \mathbb{R}^2 : -1 \le x_1 - x_2 \le 1\}$, và LP trên đó vẫn có thể có nghiệm. Kết quả về đỉnh là nền tảng của phương pháp đơn hình, thuật toán đi từ đỉnh này sang đỉnh kề tốt hơn, mà Lecture 07 sẽ trình bày.

## 3. Dạng chuẩn và dạng bất đẳng thức

Hai trường hợp riêng của LP gặp nhiều đến mức có tên riêng. **LP dạng chuẩn** chỉ có ràng buộc đẳng thức và điều kiện không âm của biến:

$$
\text{minimize}\quad c^Tx \qquad \text{subject to}\quad Ax = b,\quad x \succeq 0 .
$$

**LP dạng bất đẳng thức** không có ràng buộc đẳng thức nào:

$$
\text{minimize}\quad c^Tx \qquad \text{subject to}\quad Ax \preceq b .
$$

Hai dạng phục vụ hai mục đích khác nhau. Dạng bất đẳng thức gần với hình học, vì mỗi hàng của $A$ là một nửa không gian. Dạng chuẩn gần với đại số, vì nó làm việc với hệ phương trình $Ax = b$, và đó là dạng mà phương pháp đơn hình dùng.

## 4. Đưa một LP bất kỳ về dạng chuẩn

Hai bước là đủ. Bước thứ nhất thêm [biến bù](./bai-toan-tuong-duong.md) $s \succeq 0$ cho các bất đẳng thức, biến $Gx \preceq h$ thành $Gx + s = h$. Bước thứ hai xử lý những biến không có điều kiện dấu: Viết mỗi biến tự do thành hiệu của hai biến không âm, $x = x^+ - x^-$ với $x^+, x^- \succeq 0$. Kết quả là bài toán

$$
\begin{aligned}
\text{minimize}\quad & c^Tx^+ - c^Tx^- + d\\
\text{subject to}\quad & Gx^+ - Gx^- + s = h,\\
& Ax^+ - Ax^- = b,\\
& x^+ \succeq 0,\quad x^- \succeq 0,\quad s \succeq 0,
\end{aligned}
$$

đúng dạng chuẩn với biến $(x^+, x^-, s)$.

Hãy làm một ví dụ tự đặt. Xét bài toán cực tiểu $x_1 - 2x_2$ với $x_1 + x_2 \le 4$, $-x_1 + x_2 \le 2$ và $x_2 \ge 0$, trong đó $x_1$ không có điều kiện dấu. Miền khả thi là tam giác có ba đỉnh $(-2, 0)$, $(4, 0)$ và $(1, 3)$, cho các giá trị $-2$, $4$ và $-5$, nên nghiệm là $(1, 3)$ với giá trị $-5$. Đưa về dạng chuẩn, ta đặt $x_1 = u - v$ với $u, v \ge 0$, thêm hai biến bù $s_1, s_2 \ge 0$, và được

$$
\begin{aligned}
\text{minimize}\quad & u - v - 2x_2\\
\text{subject to}\quad & u - v + x_2 + s_1 = 4,\\
& -u + v + x_2 + s_2 = 2,\\
& u,\ v,\ x_2,\ s_1,\ s_2 \ge 0 .
\end{aligned}
$$

Bài toán có năm biến không âm và hai phương trình. Nghiệm của nó là $u = 1$, $v = 0$, $x_2 = 3$, $s_1 = s_2 = 0$, với cùng giá trị $-5$. Hai biến bù bằng 0 cho biết hai ràng buộc đầu chặt tại nghiệm, đúng với việc đỉnh $(1, 3)$ là giao của hai đường thẳng ấy.

Phép tách $x = x^+ - x^-$ có một điểm đáng chú ý: Nó không duy nhất. Cộng cùng một số dương vào cả $x^+$ lẫn $x^-$ không đổi $x$. Câu 2 ở cuối trang cho thấy vì sao điều này không gây hại.

## 5. Ví dụ: Bài toán khẩu phần

Một ví dụ kinh điển mở đầu cho LP là **bài toán khẩu phần (Diet Problem)**. Có $n$ loại thực phẩm, mỗi đơn vị thực phẩm $j$ có giá $c_j$ và chứa lượng $a_{ij}$ của chất dinh dưỡng $i$. Một khẩu phần lành mạnh cần ít nhất $b_i$ đơn vị chất $i$, với $m$ chất. Gọi $x_j \ge 0$ là lượng thực phẩm $j$ được dùng, khẩu phần rẻ nhất là nghiệm của

$$
\text{minimize}\quad c^Tx \qquad \text{subject to}\quad Ax \succeq b,\quad x \succeq 0 .
$$

Mô hình này linh hoạt hơn vẻ ngoài của nó. Yêu cầu một lượng chính xác của một chất cho một ràng buộc đẳng thức. Giới hạn lượng tối đa, chẳng hạn của muối, cho thêm một bất đẳng thức theo chiều ngược lại. Giới hạn lượng một loại thực phẩm cho một cận trên của biến. Tất cả đều giữ bài toán là LP. Cái mô hình không làm được là những yêu cầu như "dùng nhiều nhất ba loại thực phẩm", vì đếm số biến khác 0 không phải một hàm affine, thậm chí không phải hàm tựa lồi, như [chủ đề trước](./toi-uu-tua-loi.md) đã chỉ ra.

## 6. Vì sao không thể chỉ thử các đỉnh

Nếu nghiệm luôn nằm ở một đỉnh, sao không liệt kê mọi đỉnh rồi chọn đỉnh tốt nhất? Nguyên nhân là số đỉnh có thể bùng nổ theo cấp số nhân. Hình lập phương $[0, 1]^n$ chỉ cần $2n$ bất đẳng thức để mô tả, nhưng có $2^n$ đỉnh. Với $n = 30$, đó là 60 bất đẳng thức và hơn một tỉ đỉnh. Một đa diện mô tả bằng $m$ bất đẳng thức trong $\mathbb{R}^n$ có thể có tới cỡ $\binom{m}{n}$ đỉnh, vì mỗi đỉnh được xác định bởi $n$ ràng buộc chặt. Các thuật toán thực tế, như phương pháp đơn hình hay phương pháp điểm trong, tránh việc liệt kê này bằng cách đi có định hướng trên đa diện hoặc xuyên qua bên trong nó.

## 7. Những câu hỏi để đào sâu

**Câu 1.** Một LP có thể có đúng hai nghiệm tối ưu không?

<details><summary>Xem lời giải thích</summary>

Không. Tập nghiệm của một bài toán lồi là tập lồi, nên nếu $x$ và $y$ đều là nghiệm thì mọi điểm trên đoạn nối chúng cũng là nghiệm. Vậy một LP có không nghiệm, đúng một nghiệm, hoặc vô số nghiệm. Với LP, tập nghiệm còn là một mặt của đa diện: Một đỉnh, một cạnh, hay một mặt có số chiều lớn hơn. Đó là lý do trong mô phỏng, giữa hai hướng $c$ có hai đỉnh tối ưu khác nhau luôn có một hướng làm cả cạnh nối chúng tối ưu.

</details>

**Câu 2.** Trong phép tách $x = x^+ - x^-$, có thể xảy ra trường hợp tại nghiệm của bài toán dạng chuẩn, cả $x_i^+$ lẫn $x_i^-$ đều dương không? Điều đó có làm hỏng phép biến đổi không?

<details><summary>Xem lời giải thích</summary>

Có thể. Nếu $(x^+, x^-, s)$ là nghiệm thì $(x^+ + \delta e_i, x^- + \delta e_i, s)$ với $\delta > 0$ cũng khả thi và cho cùng giá trị, nên cũng là nghiệm. Phép biến đổi không hỏng, vì ta luôn lấy lại được $x = x^+ - x^-$ với đúng giá trị tối ưu, và đó là tất cả những gì định nghĩa tương đương đòi hỏi. Hơn nữa, tại các nghiệm là đỉnh của bài toán dạng chuẩn, không bao giờ có cả hai cùng dương: Cột của $x_i^+$ và cột của $x_i^-$ trong ma trận ràng buộc đối dấu nhau, tức phụ thuộc tuyến tính, nên không thể cùng là biến cơ sở. Phương pháp đơn hình, vốn chỉ đi qua các đỉnh, vì vậy luôn trả về $\min\{x_i^+, x_i^-\} = 0$.

</details>

**Câu 3.** Cho hai nhóm điểm trong mặt phẳng, nhóm dương gồm $(2, 2)$, $(3, 1)$, $(3, 3)$ và nhóm âm gồm $(0, 0)$, $(1, 0)$, $(0, 1.5)$. Làm thế nào kiểm tra có một đường thẳng tách hai nhóm hay không bằng một LP?

<details><summary>Xem lời giải thích</summary>

Tìm $(a, b) \in \mathbb{R}^2 \times \mathbb{R}$ với $a^Tx_i - b \ge 1$ cho mọi điểm dương và $a^Tx_j - b \le -1$ cho mọi điểm âm. Mọi điều kiện đều tuyến tính theo $(a, b)$, nên đây là một bài toán khả thi LP với ba biến và sáu bất đẳng thức. Hằng số 1 không làm mất tính tổng quát: Nếu có một đường thẳng tách chặt, nhân $(a, b)$ với một số dương đủ lớn sẽ cho khoảng cách 1. Với dữ liệu này, một bộ giải LP trả về chẳng hạn $a = (\tfrac67, \tfrac47)$ và $b = \tfrac{13}{7}$, tức đường thẳng $6x_1 + 4x_2 = 13$ tách hai nhóm. Đây là bài toán phân lớp tuyến tính ở dạng đơn giản nhất. Khi hai nhóm không tách được, LP bất khả thi, và người ta chuyển sang cực tiểu tổng các vi phạm, một ý tưởng dẫn tới máy vector hỗ trợ.

</details>

**Câu 4.** Bài toán cực tiểu $x_1 - x_2$ trên dải $\{-1 \le x_1 - x_2 \le 1\}$ có nghiệm không? Nó minh họa điều gì về nhận xét "nghiệm nằm ở đỉnh"?

<details><summary>Xem lời giải thích</summary>

Có. Hàm mục tiêu không nhỏ hơn $-1$ trên dải, và đạt $-1$ trên cả đường thẳng $x_1 - x_2 = -1$, nên $p^\star = -1$ và tập nghiệm là một đường thẳng vô hạn. Dải không có đỉnh nào, vì không điểm nào của nó là giao của hai ràng buộc chặt độc lập. Vậy LP vẫn có thể có nghiệm khi đa diện không có đỉnh, và lúc đó không có "nghiệm là đỉnh" nào cả. Định lý về đỉnh cần giả thiết đa diện có ít nhất một đỉnh, điều tương đương với việc nó không chứa trọn một đường thẳng.

</details>

**Câu 5.** Trong mô phỏng, với đa diện không bị chặn, có những hướng $c$ làm bài toán không bị chặn dưới. Hãy mô tả chính xác tập các hướng $c$ làm bài toán có giá trị tối ưu hữu hạn.

<details><summary>Xem lời giải thích</summary>

Đa diện có dạng $\operatorname{conv}\{v_1, v_2, v_3\} + \operatorname{cone}\{r_a, r_b\}$. Trên phần bị chặn, hàm tuyến tính luôn đạt giá trị nhỏ nhất. Trên mỗi tia $v + \tau r$, giá trị là $c^Tv + \tau c^Tr$, bị chặn dưới khi và chỉ khi $c^Tr \ge 0$. Vậy bài toán có giá trị hữu hạn khi và chỉ khi $c^Tr_a \ge 0$ và $c^Tr_b \ge 0$, tức $c$ thuộc [nón đối ngẫu](../bai-01-nhap-mon-toi-uu/non-doi-ngau.md) của nón sinh bởi hai tia. Kết quả này đúng cho mọi đa diện khác rỗng: LP có giá trị hữu hạn khi và chỉ khi $c$ nằm trong nón đối ngẫu của nón lùi xa của đa diện. Đây là một trong những chỗ hình học của nón đối ngẫu ở Lecture 01 được dùng trực tiếp.

</details>

## 8. Bài tập tự luyện

::: exercise 1. Đếm biến sau khi chuyển dạng
Một LP có 4 biến, trong đó 2 biến không có điều kiện dấu và 2 biến có điều kiện không âm, cùng 3 bất đẳng thức và 1 đẳng thức. Sau khi chuyển về dạng chuẩn theo cách ở mục 4, bài toán có bao nhiêu biến và bao nhiêu phương trình?
:::

::: solution
Hai biến tự do mỗi biến tách thành hai, nên có $2 \times 2 + 2 = 6$ biến từ $x$. Ba bất đẳng thức cho thêm ba biến bù. Tổng cộng 9 biến không âm. Số phương trình là $3 + 1 = 4$: Ba phương trình từ các bất đẳng thức đã thêm biến bù và một đẳng thức có sẵn. Hai biến vốn đã có điều kiện không âm thì giữ nguyên, không cần tách.
:::

::: exercise 2. Giải bằng hình học
Trên ngũ giác có các đỉnh $(0.5, 0.5)$, $(3.5, 0.5)$, $(4.5, 2.2)$, $(2.8, 3.8)$, $(0.8, 3.0)$ của mô phỏng, (a) tìm nghiệm của bài toán cực đại $x_1 + x_2$. (b) Tìm một vector $c$ để bài toán cực đại $c^Tx$ có cả cạnh nối $(4.5, 2.2)$ và $(2.8, 3.8)$ làm tập nghiệm.
:::

::: solution
(a) Giá trị tại năm đỉnh là $1$, $4$, $6.7$, $6.6$ và $3.8$, nên nghiệm là đỉnh $(4.5, 2.2)$ với giá trị $6.7$. (b) Vector cạnh là $(2.8 - 4.5,\ 3.8 - 2.2) = (-1.7,\ 1.6)$. Vector $c$ phải vuông góc với nó và hướng ra ngoài ngũ giác, chẳng hạn $c = (1.6, 1.7)$. Khi đó hai đầu cạnh cùng cho giá trị $1.6 \times 4.5 + 1.7 \times 2.2 = 10.94$ và $1.6 \times 2.8 + 1.7 \times 3.8 = 10.94$, trong khi ba đỉnh còn lại cho $1.65$, $6.45$ và $6.38$, nên cả cạnh là tập nghiệm.
:::

::: exercise 3. Không bị chặn
Bài toán cực tiểu $-x_1 - x_2$ trên dải $\{x \in \mathbb{R}^2 : -1 \le x_1 - x_2 \le 1\}$ có nghiệm không? Chỉ ra một hướng $r$ chứng tỏ điều đó.
:::

::: solution
Không, bài toán không bị chặn dưới. Hướng $r = (1, 1)$ có $r_1 - r_2 = 0$, nên đi theo $r$ từ một điểm khả thi bất kỳ ta vẫn ở trong dải. Dọc hướng ấy, hàm mục tiêu thay đổi một lượng $c^Tr = -2 < 0$ trên mỗi đơn vị, nên giảm mãi về $-\infty$.
:::

## Tóm tắt

Quy hoạch tuyến tính cực tiểu một hàm affine trên một đa diện. Về hình học, nghiệm là điểm của đa diện xa nhất theo hướng $-c$, và có bốn khả năng: Nghiệm duy nhất tại một đỉnh, cả một mặt là tập nghiệm, bài toán không bị chặn dưới khi đa diện kéo dài theo một hướng làm giảm $c^Tx$, hoặc bất khả thi.

Mọi LP đều đưa được về dạng chuẩn $\min c^Tx$ với $Ax = b$, $x \succeq 0$, bằng cách thêm biến bù cho bất đẳng thức và tách mỗi biến tự do thành hiệu của hai biến không âm. Khi đa diện có đỉnh và giá trị tối ưu hữu hạn, luôn có một đỉnh tối ưu, nhưng số đỉnh có thể tăng theo hàm mũ, nên các thuật toán không liệt kê đỉnh mà đi có định hướng.

## Tài liệu tham khảo

- Stephen Boyd, Lieven Vandenberghe, *Convex Optimization*, Cambridge University Press.
- Dimitris Bertsimas, John N. Tsitsiklis, *Introduction to Linear Optimization*, Athena Scientific.
