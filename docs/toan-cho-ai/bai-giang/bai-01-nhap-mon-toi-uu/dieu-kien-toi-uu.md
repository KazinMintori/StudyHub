---
course: toan-cho-ai
lecture: bai-01-nhap-mon-toi-uu
topic: dieu-kien-toi-uu
section: topic
title: "Điều kiện tối ưu bậc nhất trên miền lồi"
description: "Tiêu chuẩn tối ưu ∇f₀(x)ᵀ(y − x) ≥ 0 cho bài toán lồi khả vi và ý nghĩa siêu phẳng tựa, lời chứng minh hai chiều, ba trường hợp riêng: Không ràng buộc, ràng buộc đẳng thức với nhân tử Lagrange, ràng buộc không âm với điều kiện bù, cùng phép chiếu và phương pháp gradient có chiếu."
---

Khi không có ràng buộc, điều kiện tối ưu quen thuộc là gradient bằng 0. Nhưng phần lớn bài toán thực tế có ràng buộc, và khi nghiệm nằm trên biên của miền khả thi, gradient tại đó thường **khác 0**. Cực tiểu $x$ trên đoạn $[1, 2]$ đạt tại $x = 1$, nơi đạo hàm bằng 1. Vậy làm sao kiểm chứng một điểm trên biên là tối ưu?

Với bài toán lồi khả vi, câu trả lời là một bất đẳng thức duy nhất, và nó có một ý nghĩa hình học rất gọn: Tại nghiệm, mặt phẳng vuông góc với gradient phải tựa vào miền khả thi. Sau khi phát biểu và chứng minh tiêu chuẩn đó, ta xem nó biến thành gì trong ba tình huống hay gặp nhất. Chương sau về đối ngẫu sẽ khai triển những trường hợp này thành điều kiện KKT tổng quát.

## 1. Tiêu chuẩn tối ưu

> **Định lý.** Xét bài toán lồi với hàm mục tiêu $f_0$ khả vi và miền khả thi $X$. Điểm $x$ là nghiệm tối ưu khi và chỉ khi $x \in X$ và
> $$\nabla f_0(x)^T (y - x) \ge 0 \quad \text{với mọi } y \in X.$$

Đọc từng phần của bất đẳng thức. Vector $y - x$ là hướng đi từ $x$ tới một điểm khả thi $y$. Đại lượng $\nabla f_0(x)^T (y - x)$ là đạo hàm theo hướng của $f_0$ khi bắt đầu đi theo hướng đó. Tiêu chuẩn nói: Tại nghiệm, **không có hướng khả thi nào làm $f_0$ giảm ngay từ bước đầu tiên**. Mọi hướng đi vào miền khả thi đều làm $f_0$ tăng, hoặc ít nhất là không giảm, theo xấp xỉ bậc nhất.

Về hình học, nếu $\nabla f_0(x) \ne 0$, tiêu chuẩn khẳng định toàn bộ tập khả thi $X$ nằm trọn trong nửa không gian $\{y : \nabla f_0(x)^T (y - x) \ge 0\}$. Siêu phẳng đi qua $x$ với pháp tuyến $\nabla f_0(x)$ chính là một **siêu phẳng tựa** của $X$ tại $x$, trong khi $-\nabla f_0(x)$ (hướng suy giảm nhanh nhất của $f_0$) chỉ thẳng ra bên ngoài miền khả thi. Đồng thời, siêu phẳng ấy cũng tựa vào tập mức dưới $\{y : f_0(y) \le f_0(x)\}$, tương tự như phân tích ở chủ đề điều kiện bậc nhất. Do đó tại điểm nghiệm tối ưu, miền khả thi và tập mức dưới tiếp xúc nhau tại đúng điểm $x$, và tồn tại một siêu phẳng phân tách chúng.

<OptimalityLab />

Trong mô phỏng, vùng đỏ là tập các điểm khả thi $y$ với $\nabla f_0(x)^T (y - x) < 0$, tức những nơi mà đi về phía đó thì $f_0$ giảm ngay. Kéo $x$ dọc theo biên về phía vòng tròn rỗng, vùng đỏ co lại, và đúng lúc nó biến mất, đường mức vàng qua $x$ chỉ chạm đa giác tại một điểm. Khi kéo tâm $c$ vào trong đa giác, nghiệm là chính $c$, gradient tại đó bằng 0, và tiêu chuẩn trở thành điều kiện quen thuộc.

## 2. Lời chứng minh

**Điều kiện đủ.** Giả sử $x \in X$ thỏa tiêu chuẩn. Với mọi $y \in X$, điều kiện bậc nhất của hàm lồi cho

$$
f_0(y) \ge f_0(x) + \nabla f_0(x)^T (y - x) \ge f_0(x).
$$

Vậy $x$ tối ưu. Chiều này chỉ dùng tính lồi của $f_0$.

**Điều kiện cần.** Giả sử $x$ tối ưu nhưng có $y \in X$ với $\nabla f_0(x)^T (y - x) < 0$. Xét các điểm $z(t) = x + t(y - x)$ với $t \in [0, 1]$. Chúng nằm trên đoạn nối hai điểm khả thi, nên khả thi vì $X$ lồi. Đạo hàm của $f_0(z(t))$ tại $t = 0$ bằng $\nabla f_0(x)^T (y - x) < 0$, nên với $t > 0$ đủ nhỏ, $f_0(z(t)) < f_0(x)$. Đó là một điểm khả thi tốt hơn $x$, mâu thuẫn. Chiều này dùng tính lồi của $X$ để bảo đảm có thể "nhích" về phía $y$ mà không ra khỏi miền.

## 3. Ba trường hợp riêng

### Không ràng buộc

Khi $X = \operatorname{dom} f_0$ là tập mở, mọi điểm đủ gần $x$ đều khả thi. Lấy $y = x - t\nabla f_0(x)$ với $t > 0$ nhỏ, tiêu chuẩn cho $-t\|\nabla f_0(x)\|_2^2 \ge 0$, nên $\nabla f_0(x) = 0$. Ta trở lại điều kiện quen thuộc, giờ là cả điều kiện cần lẫn đủ.

Xét hàm bậc hai lồi dạng toàn phương $f_0(x) = \tfrac12 x^T P x + q^T x + r$ với $P \succeq 0$. Điều kiện dừng $\nabla f_0(x) = Px + q = 0$ là một hệ phương trình tuyến tính, dẫn đến ba trường hợp cấu trúc hình học tương ứng:

- $P \succ 0$, cái bát: Nghiệm duy nhất $x^\star = -P^{-1} q$.
- $P$ suy biến và $q$ thuộc không gian cột của $P$, cái máng có đáy nằm ngang: Vô số nghiệm, tạo thành một tập affine.
- $P$ suy biến và $q$ không thuộc không gian cột của $P$, cái máng có đáy nghiêng: Không có nghiệm, và $f_0$ giảm về $-\infty$ dọc đáy máng.

Ví dụ với $P = \operatorname{diag}(2, 0)$. Với $q = (-2, 0)$, $f_0 = x_1^2 - 2x_1$, mọi điểm $(1, x_2)$ đều là nghiệm. Với $q = (-2, 1)$, $f_0 = x_1^2 - 2x_1 + x_2$, cho $x_2 \to -\infty$ thì $f_0 \to -\infty$.

### Chỉ có ràng buộc đẳng thức

Xét bài toán cực tiểu $f_0(x)$ với $Ax = b$ trong đó $A \in \mathbb{R}^{p \times n}$ và $b \in \mathbb{R}^p$. Mọi điểm khả thi có dạng $y = x + v$ với $v$ thuộc không gian không $\mathcal{N}(A)$. Tiêu chuẩn trở thành $\nabla f_0(x)^T v \ge 0$ với mọi $v \in \mathcal{N}(A)$. Nhưng nếu $v$ thuộc không gian con này thì $-v$ cũng vậy, nên bất đẳng thức đúng cho cả $v$ lẫn $-v$, nghĩa là $\nabla f_0(x)^T v = 0$. Gradient phải **vuông góc** với $\mathcal{N}(A)$, tức thuộc không gian hàng $\mathcal{R}(A^T)$. Viết thành công thức:

$$
Ax = b, \qquad \nabla f_0(x) + A^T \nu = 0 \iff \nabla f_0(x) + \sum_{i=1}^p \nu_i a_i = 0 \ \text{ với một vector } \nu \in \mathbb{R}^p,
$$

với $a_i^T$ là hàng thứ $i$ của ma trận $A$. Ta vừa tìm lại điều kiện **nhân tử Lagrange** cổ điển, lần này chỉ bằng lập luận hình học. Vector $\nu$ là nhân tử Lagrange, và chương đối ngẫu sẽ cho nó một ý nghĩa sâu hơn.

::: example Phân bổ một đơn vị với chi phí bình phương
Cực tiểu $x_1^2 + 2x_2^2 + 3x_3^2$ với $x_1 + x_2 + x_3 = 1$. Ở đây $A = (1, 1, 1)$, nên điều kiện là $(2x_1,\ 4x_2,\ 6x_3) + \nu(1, 1, 1) = 0$, tức $2x_1 = 4x_2 = 6x_3 = -\nu$. Vậy $x$ tỉ lệ với $(\tfrac12, \tfrac14, \tfrac16)$, và chuẩn hóa cho tổng bằng 1 được $x^\star = (\tfrac{6}{11}, \tfrac{3}{11}, \tfrac{2}{11})$ với $\nu = -\tfrac{12}{11}$ và giá trị tối ưu $\tfrac{6}{11}$. Thành phần càng "đắt" thì nhận càng ít, và tại nghiệm, **chi phí biên** $\partial f_0 / \partial x_i$ của mọi thành phần bằng nhau, cùng bằng $\tfrac{12}{11}$. Nếu chi phí biên còn chênh lệch, chuyển một chút từ thành phần đắt sang thành phần rẻ sẽ giảm tổng chi phí mà vẫn giữ tổng bằng 1.
:::

### Ràng buộc không âm

Xét bài toán cực tiểu $f_0(x)$ với ràng buộc không âm $x \succeq 0$ (tức $x_i \ge 0$ với mọi $i = 1, \dots, n$). Tiêu chuẩn tối ưu đòi hỏi $\nabla f_0(x)^T (y - x) \ge 0$ với mọi $y \succeq 0$. Do hàm tuyến tính theo $y$ là $\nabla f_0(x)^T y = \sum_{i=1}^n \big(\nabla f_0(x)\big)_i y_i$ phải bị chặn dưới trên toàn bộ nón không âm $\{y \in \mathbb{R}^n : y_i \ge 0\}$, ta suy ra $\nabla f_0(x) \succeq 0$. Chọn thử điểm $y = 0 \in X$, ta thu được $-\nabla f_0(x)^T x \ge 0$, tương đương $\nabla f_0(x)^T x \le 0$. Khai triển tích vô hướng này:

$$
\nabla f_0(x)^T x = \sum_{i=1}^n x_i \big(\nabla f_0(x)\big)_i \le 0.
$$

Vì cả $x_i \ge 0$ lẫn $\big(\nabla f_0(x)\big)_i \ge 0$ với mọi $i = 1, \dots, n$, mỗi số hạng $x_i \big(\nabla f_0(x)\big)_i$ đều không âm. Để tổng của chúng không dương ($\le 0$), bắt buộc từng số hạng riêng lẻ phải triệt tiêu về 0. Ta đúc kết toàn bộ điều kiện thành hệ thức:

$$
x \succeq 0, \qquad \nabla f_0(x) \succeq 0, \qquad x_i \,\big(\nabla f_0(x)\big)_i = 0 \quad \text{với mọi } i = 1, \dots, n.
$$

Điều kiện cuối gọi là **điều kiện bù**: Với mỗi $i = 1, \dots, n$, hoặc $x_i = 0$, hoặc đạo hàm riêng theo $x_i$ bằng 0. Đọc theo từng tọa độ: Nếu biến $x_i$ nằm hẳn trong miền ($x_i > 0$), nó được tự do dịch chuyển cả hai phía, nên đạo hàm theo nó phải bằng 0 như bài toán không ràng buộc. Nếu $x_i$ bị chặn ở biên 0, đạo hàm theo nó chỉ cần không âm: Hàm muốn $x_i$ giảm tiếp xuống dưới 0, nhưng ràng buộc không cho.

Ví dụ: Cực tiểu $(x_1 - 1)^2 + (x_2 + 2)^2$ với $x \succeq 0$. Không ràng buộc, nghiệm sẽ là $(1, -2)$, nhưng $x_2 = -2$ vi phạm ràng buộc. Ứng viên $x = (1, 0)$ có $\nabla f_0(x) = (0,\ 4)$. Kiểm tra: $x \succeq 0$, gradient $\succeq 0$, và $x_1 \cdot 0 = 0$, $x_2 \cdot 4 = 0$. Cả ba điều kiện thỏa, nên $(1, 0)$ tối ưu.

## 4. Phép chiếu và phương pháp gradient có chiếu

Tiêu chuẩn tối ưu còn có một cách viết dẫn thẳng tới một thuật toán. Gọi $\Pi_X(z)$ là **phép chiếu Euclid** của $z$ lên tập lồi đóng $X$, tức điểm của $X$ gần $z$ nhất theo chuẩn Euclid. Phép chiếu là nghiệm của bài toán lồi cực tiểu $\tfrac12\|y - z\|_2^2$ trên $X$, nên theo chính tiêu chuẩn vừa học, $p = \Pi_X(z)$ khi và chỉ khi

$$
(p - z)^T (y - p) \ge 0 \quad \text{với mọi } y \in X .
$$

Giờ lấy $z = x - t\nabla f_0(x)$ với $t > 0$. Điểm $x$ là hình chiếu của $z$ khi và chỉ khi $t\,\nabla f_0(x)^T (y - x) \ge 0$ với mọi $y \in X$, đúng là tiêu chuẩn tối ưu. Vậy:

> $x$ là nghiệm tối ưu khi và chỉ khi $x = \Pi_X\big(x - t\nabla f_0(x)\big)$ với một (và khi đó mọi) $t > 0$.

Nghiệm là **điểm bất động** của phép "đi một bước gradient rồi chiếu về miền khả thi". Điều này gợi ý ngay **phương pháp gradient có chiếu**: Lặp $x^{(k+1)} = \Pi_X\big(x^{(k)} - t\nabla f_0(x^{(k)})\big)$. Nếu dãy dừng lại, nó dừng đúng tại nghiệm. Trong mô phỏng ở mục 1, dòng cuối của bảng kết quả cho thấy một bước như vậy đẩy $x$ đi bao xa, và khoảng cách đó bằng 0 đúng khi $x$ tối ưu. Trong học máy, phương pháp này được dùng khi tham số phải nằm trong một tập đơn giản, chẳng hạn ràng buộc chuẩn $\|w\|_2 \le r$, mà phép chiếu chỉ là co vector về độ dài $r$ khi nó dài hơn.

## 5. Những câu hỏi để đào sâu

**Câu 1.** Với nghiệm $x$ nằm hẳn bên trong miền khả thi, tiêu chuẩn tối ưu trở thành gì? Còn nếu miền khả thi là một tập affine?

<details><summary>Xem lời giải thích</summary>

Nếu $x$ nằm trong phần trong của $X$, mọi hướng $v$ đều khả thi với bước đủ nhỏ, kể cả $v$ và $-v$, nên tiêu chuẩn buộc $\nabla f_0(x)^T v = 0$ với mọi $v$, tức $\nabla f_0(x) = 0$. Với tập affine, các hướng khả thi là cả một không gian con, nên lập luận tương tự cho gradient vuông góc với không gian con đó, như trường hợp ràng buộc đẳng thức ở mục 3. Hai trường hợp này cho thấy điều kiện chỉ thật sự là một **bất đẳng thức** khi nghiệm nằm trên biên của một tập có "góc", như mặt của đa diện hay biên của nón không âm.

</details>

**Câu 2.** Phát biểu "tại nghiệm của bài toán có ràng buộc, gradient phải vuông góc với biên" đúng khi nào và sai khi nào?

<details><summary>Xem lời giải thích</summary>

Đúng khi nghiệm nằm ở chỗ biên trơn, chẳng hạn trên một cạnh của đa giác (không ở đỉnh) hay trên đường tròn: Khi đó siêu phẳng tựa duy nhất là tiếp tuyến của biên, nên $\nabla f_0(x)$ phải vuông góc với biên và hướng vào trong miền. Sai khi nghiệm nằm ở một đỉnh. Tại đỉnh, có cả một chùm siêu phẳng tựa, và $-\nabla f_0(x)$ chỉ cần nằm trong một "nón" các hướng chỉ ra ngoài, không cần vuông góc với cạnh nào. Đặt tâm $c$ của mô phỏng sao cho nghiệm rơi vào đỉnh $(2.2, 0.5)$ để thấy gradient nghiêng tự do trong một khoảng góc.

</details>

**Câu 3.** Trong ví dụ phân bổ, vì sao nhân tử $\nu = -\tfrac{12}{11}$ lại bằng đúng âm của chi phí biên chung? Hãy đoán xem giá trị tối ưu thay đổi ra sao nếu tổng cần phân bổ là $1 + \delta$ thay vì 1.

<details><summary>Xem lời giải thích</summary>

Điều kiện $\nabla f_0(x) + \nu \mathbf{1} = 0$ nói mọi đạo hàm riêng bằng $-\nu$, nên $-\nu$ là chi phí biên chung. Khi tổng tăng thêm $\delta$ nhỏ, cách rẻ nhất là chia phần tăng sao cho chi phí biên vẫn bằng nhau, và chi phí tăng xấp xỉ $(\text{chi phí biên}) \times \delta = \tfrac{12}{11}\delta$. Kiểm tra chính xác: Nghiệm với tổng $s$ là $s \cdot (\tfrac{6}{11}, \tfrac{3}{11}, \tfrac{2}{11})$ và giá trị tối ưu là $\tfrac{6}{11}s^2$, có đạo hàm theo $s$ tại $s = 1$ bằng $\tfrac{12}{11}$. Nhân tử Lagrange đo **độ nhạy** của giá trị tối ưu theo vế phải của ràng buộc, và chương đối ngẫu sẽ chứng minh điều này tổng quát.

</details>

**Câu 4.** Phương pháp gradient có chiếu cần tính $\Pi_X$ ở mỗi bước. Với những tập $X$ nào thì phép chiếu dễ, và với tập nào nó khó ngang bài toán gốc?

<details><summary>Xem lời giải thích</summary>

Phép chiếu có công thức đóng cho nhiều tập đơn giản: Hình hộp $\{l \preceq x \preceq u\}$ (kẹp từng tọa độ vào đoạn của nó), nón không âm (thay thành phần âm bằng 0), quả cầu Euclid (co vector về bán kính nếu nó dài quá), siêu phẳng và nửa không gian (một công thức tường minh). Đơn hình xác suất cần một thuật toán sắp xếp ngắn. Nhưng với một đa diện tổng quát $\{x : Ax \preceq b\}$ có nhiều ràng buộc, phép chiếu là một quy hoạch bậc hai, khó gần ngang bài toán gốc. Khi đó người ta chuyển sang những phương pháp khác, chẳng hạn các phương pháp dựa trên đối ngẫu.

</details>

## 6. Bài tập tự luyện

::: exercise 1. Kiểm chứng một nghiệm trên biên
Cực tiểu $f_0(x) = (x_1 - 2)^2 + (x_2 - 0.5)^2$ trên hình vuông $[0, 1]^2$. (a) Đoán nghiệm bằng hình học. (b) Kiểm chứng bằng tiêu chuẩn $\nabla f_0(x)^T (y - x) \ge 0$. (c) Kiểm chứng bằng điều kiện điểm bất động của phép chiếu với $t = 0.3$.
:::

::: solution
(a) Không ràng buộc, nghiệm là $(2, 0.5)$, nằm ngoài hình vuông về phía phải. Điểm gần nhất của hình vuông là $x = (1, 0.5)$. (b) Gradient tại $x$ là $\big(2(1 - 2),\ 2(0.5 - 0.5)\big) = (-2,\ 0)$. Với mọi $y \in [0, 1]^2$,

$$
\nabla f_0(x)^T (y - x) = -2(y_1 - 1) = 2(1 - y_1) \ge 0
$$

vì $y_1 \le 1$. Tiêu chuẩn thỏa, nên $x$ tối ưu. (c) $x - 0.3\nabla f_0(x) = (1.6,\ 0.5)$. Chiếu lên hình vuông bằng cách kẹp từng tọa độ vào $[0, 1]$ được $(1,\ 0.5) = x$. Điểm bất động, đúng như dự báo.
:::

::: exercise 2. Chiếu lên đơn hình
Tìm điểm của đoạn $\{x \in \mathbb{R}^2 : x \succeq 0,\ x_1 + x_2 = 1\}$ gần $c = (1, 0.6)$ nhất, và kiểm chứng bằng tiêu chuẩn tối ưu.
:::

::: solution
Cực tiểu $(x_1 - 1)^2 + (x_2 - 0.6)^2$ trên đoạn. Thay $x_2 = 1 - x_1$ được $(x_1 - 1)^2 + (0.4 - x_1)^2$, nhỏ nhất khi $x_1 = 0.7$, nên $x = (0.7,\ 0.3)$, nằm trong đoạn. Kiểm chứng: $\nabla f_0(x) = 2(x - c) = (-0.6,\ -0.6)$. Với mọi $y$ trên đoạn,

$$
\nabla f_0(x)^T (y - x) = -0.6\big((y_1 + y_2) - (x_1 + x_2)\big) = -0.6\,(1 - 1) = 0 \ge 0 .
$$

Gradient vuông góc với đoạn, đúng như trường hợp ràng buộc đẳng thức, vì nghiệm không chạm hai đầu mút.
:::

::: exercise 3. Điều kiện bù
Cực tiểu $f_0(x) = x_1^2 + x_2^2 - 2x_1 + 6x_2$ với $x \succeq 0$. Tìm nghiệm và chỉ ra điều kiện bù tại từng tọa độ.
:::

::: solution
$\nabla f_0(x) = (2x_1 - 2,\ 2x_2 + 6)$. Thành phần thứ hai luôn dương khi $x_2 \ge 0$, nên điều kiện bù $x_2 (2x_2 + 6) = 0$ buộc $x_2 = 0$. Với tọa độ thứ nhất, thử $x_1 > 0$ thì cần $2x_1 - 2 = 0$, tức $x_1 = 1$. Ứng viên $x = (1, 0)$ có $\nabla f_0(x) = (0,\ 6) \succeq 0$, $x_1 \cdot 0 = 0$, $x_2 \cdot 6 = 0$, nên tối ưu, với giá trị $1 - 2 = -1$. Đọc theo từng tọa độ: Tọa độ $x_1$ nằm trong miền nên đạo hàm theo nó bằng 0, còn tọa độ $x_2$ bị chặn ở 0 và đạo hàm theo nó dương, nghĩa là hàm còn muốn giảm $x_2$ xuống âm nhưng ràng buộc không cho.
:::

## Tóm tắt

Với bài toán lồi có hàm mục tiêu khả vi, $x$ tối ưu khi và chỉ khi $x$ khả thi và $\nabla f_0(x)^T (y - x) \ge 0$ với mọi điểm khả thi $y$: Không hướng khả thi nào làm hàm giảm ngay từ đầu. Về hình học, siêu phẳng qua $x$ vuông góc với gradient tựa vào miền khả thi, và $-\nabla f_0(x)$ chỉ ra ngoài miền. Chiều đủ dùng tính lồi của hàm, chiều cần dùng tính lồi của miền.

Khi không có ràng buộc, tiêu chuẩn là $\nabla f_0(x) = 0$. Với ràng buộc $Ax = b$, nó là điều kiện nhân tử Lagrange $\nabla f_0(x) + A^T\nu = 0$. Với ràng buộc $x \succeq 0$, nó là gradient không âm cùng điều kiện bù. Cuối cùng, nghiệm chính là điểm bất động của phép đi một bước gradient rồi chiếu về miền, và đó là nền của phương pháp gradient có chiếu.

## Tài liệu tham khảo

- Stephen Boyd, Lieven Vandenberghe, *Convex Optimization*, Cambridge University Press.
