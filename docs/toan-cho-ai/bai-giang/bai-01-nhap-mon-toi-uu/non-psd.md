---
course: toan-cho-ai
lecture: bai-01-nhap-mon-toi-uu
topic: non-psd
section: topic
title: "Nón các ma trận nửa xác định dương"
description: "Không gian các ma trận đối xứng, nón S₊ⁿ và Sⁿ₊₊, chứng minh tính nón lồi, biểu diễn như giao vô hạn nửa không gian, điều kiện cho ma trận 2×2, những cái bẫy khi kiểm tra tính nửa xác định dương và vai trò của ma trận hiệp phương sai, ma trận Gram."
---

Cho tới giờ, các "điểm" của ta luôn là vector. Trang này đi thêm một bước mà lần đầu gặp có thể thấy lạ: Coi mỗi **ma trận đối xứng** là một điểm trong một không gian, rồi hỏi tập các ma trận nửa xác định dương có hình dạng gì. Câu trả lời là một nón lồi, và nó trông rất giống nón kem của chủ đề trước khi nhìn trong không gian ba chiều.

Vì sao phải quan tâm tới hình học của một tập ma trận? Vì trong tối ưu và học máy, rất nhiều đối tượng cần tìm chính là ma trận: Ma trận hiệp phương sai trong thống kê, ma trận kernel trong các phương pháp kernel, ma trận khoảng cách trong học metric. Ràng buộc "ma trận này phải nửa xác định dương" xuất hiện ở khắp nơi, và việc tập nghiệm của nó là một nón lồi là lý do những bài toán đó vẫn giải được. Lecture 02 sẽ gọi chúng là quy hoạch nửa xác định.

Bạn cần nhớ định nghĩa ma trận nửa xác định dương, trị riêng của ma trận đối xứng, và nón lồi từ các chủ đề trước.

## 1. Ma trận như một điểm

Ký hiệu $\mathbb{S}^n$ là tập các ma trận đối xứng thực cỡ $n \times n$:

$$
\mathbb{S}^n = \{X \in \mathbb{R}^{n \times n} : X = X^T\}.
$$

Cộng hai ma trận đối xứng hay nhân một ma trận đối xứng với một số đều cho ma trận đối xứng, nên $\mathbb{S}^n$ là một không gian vector. Số chiều của nó là $\tfrac{n(n+1)}{2}$, vì một ma trận đối xứng được xác định hoàn toàn bởi các phần tử trên và trên đường chéo. Với $n = 2$, mỗi ma trận

$$
X = \begin{bmatrix} x & y \\ y & z \end{bmatrix}
$$

ứng với đúng một bộ ba số $(x, y, z) \in \mathbb{R}^3$. Vì vậy $\mathbb{S}^2$ "chính là" $\mathbb{R}^3$, và ta có thể vẽ các tập ma trận $2 \times 2$ như những hình trong không gian ba chiều. Với $n = 3$, không gian $\mathbb{S}^3$ có 6 chiều, ta không vẽ được nữa, nhưng mọi khái niệm hình học như đoạn thẳng, tổ hợp lồi, nón vẫn dùng được y nguyên.

## 2. Ba tập ma trận và ký hiệu

Ta dùng ba ký hiệu song song với các tập số $\mathbb{R}$, $\mathbb{R}_+$ (số không âm) và $\mathbb{R}_{++}$ (số dương):

- $\mathbb{S}^n$: Mọi ma trận đối xứng.
- $\mathbb{S}^n_+ = \{X \in \mathbb{S}^n : X \succeq 0\}$: Các ma trận **nửa xác định dương** (PSD), tức $z^T X z \ge 0$ với mọi $z \in \mathbb{R}^n$.
- $\mathbb{S}^n_{++} = \{X \in \mathbb{S}^n : X \succ 0\}$: Các ma trận **xác định dương** (PD), tức $z^T X z > 0$ với mọi $z \ne 0$.

Sự song song này có cơ sở cụ thể. Một ma trận đối xứng là PSD khi và chỉ khi mọi trị riêng của nó không âm, và PD khi và chỉ khi mọi trị riêng dương. Nói cách khác, $X \succeq 0$ nghĩa là "các trị riêng của $X$ đều thuộc $\mathbb{R}_+$". Ma trận đối xứng giống như một "số" có nhiều trị riêng, và PSD nghĩa là "số" ấy không âm theo mọi hướng.

## 3. $\mathbb{S}^n_+$ là một nón lồi

> **Mệnh đề.** $\mathbb{S}^n_+$ là một nón lồi: Nếu $A, B \in \mathbb{S}^n_+$ và $\theta_1, \theta_2 \ge 0$ thì $\theta_1 A + \theta_2 B \in \mathbb{S}^n_+$.

Chứng minh đi thẳng từ định nghĩa, không cần tới trị riêng. Với mọi $z \in \mathbb{R}^n$,

$$
z^T (\theta_1 A + \theta_2 B) z = \theta_1\, z^T A z + \theta_2\, z^T B z \ge 0,
$$

vì cả hai số hạng là tích của một số không âm với một số không âm. Mọi việc nằm ở đẳng thức đầu: Biểu thức $z^T X z$ **tuyến tính theo $X$** khi $z$ cố định. Ta không cần biết trị riêng của $\theta_1 A + \theta_2 B$, một thứ khó tính hơn nhiều.

Cùng nhận xét ấy cho một cách nhìn thứ hai (Ví dụ 2.7 trong sách). Với mỗi $z \ne 0$ cố định, tập $\{X \in \mathbb{S}^n : z^T X z \ge 0\}$ là một **nửa không gian** trong $\mathbb{S}^n$, vì vế trái là một hàm tuyến tính khác 0 của $X$. Thật vậy, $z^T X z = \operatorname{tr}(X z z^T) = \sum_{i,j} X_{ij} z_i z_j$. Do đó

$$
\mathbb{S}^n_+ = \bigcap_{z \ne 0} \{X \in \mathbb{S}^n : Z^T X z \ge 0\}
$$

là giao của **vô số** nửa không gian, nên lồi. Khác với đa diện, ở đây cần vô hạn nửa không gian, mỗi hướng $z$ một cái. Đó là lý do biên của $\mathbb{S}^n_+$ cong chứ không phẳng từng mảnh, và ràng buộc PSD thật sự mạnh hơn mọi hệ hữu hạn bất đẳng thức tuyến tính.

## 4. Nhìn tận mắt nón PSD trong $\mathbb{S}^2$

Với ma trận $2 \times 2$, điều kiện PSD có dạng rất cụ thể (Ví dụ 2.6 trong sách):

$$
\begin{bmatrix} x & y \\ y & z \end{bmatrix} \succeq 0 \iff x \ge 0,\quad z \ge 0,\quad xz \ge y^2 .
$$

Vì sao đúng ba điều kiện này? Ma trận có hai trị riêng $\lambda_1, \lambda_2$ với $\lambda_1 + \lambda_2 = x + z$ (vết) và $\lambda_1 \lambda_2 = xz - y^2$ (định thức). Hai số thực đều không âm khi và chỉ khi tích của chúng không âm và tổng của chúng không âm. Điều kiện tích là $xz \ge y^2$. Khi đó $xz \ge 0$, nên $x$ và $z$ cùng dấu (hoặc một số bằng 0), và điều kiện tổng $x + z \ge 0$ buộc cả hai không âm. Ngược lại, $x, z \ge 0$ và $xz \ge y^2$ hiển nhiên cho tổng và tích không âm.

Biên của nón là mặt $xz = y^2$ với $x, z \ge 0$. Đổi sang các trục $u = \tfrac{x + z}{\sqrt2}$, $w = \tfrac{x - z}{\sqrt2}$ (một phép xoay 45° trong mặt phẳng $(x, z)$), điều kiện $xz \ge y^2$ trở thành $\tfrac{u^2 - w^2}{2} \ge y^2$, tức $\sqrt{w^2 + 2y^2} \le u$. Như vậy nón PSD trong $\mathbb{S}^2$ là một nón "kem" có trục là đường chéo $x = z$, với lát cắt ngang là những hình ellipse. Mô phỏng dưới đây vẽ nó theo hệ trục đã xoay, giống Hình 2.12 trong sách.

<Cone3DLab type="psd" />

Mô phỏng tiếp theo nhìn cùng một ma trận theo cách khác. Thay vì xem $X$ như một điểm trong $\mathbb{R}^3$, ta vẽ giá trị $v^T X v$ theo mọi hướng đơn vị $v$. Ma trận PSD là ma trận không có hướng nào cho giá trị âm.

<PsdLab />

Mỗi vạch trong hình là giá trị của dạng toàn phương theo một hướng. Vạch dài nhất nằm theo vector riêng của trị riêng lớn nhất, vạch ngắn nhất (hoặc âm nhất) nằm theo vector riêng của trị riêng nhỏ nhất. Đó là một cách nhìn hình học của một sự kiện đại số: $\min_{\|v\|_2 = 1} v^T X v = \lambda_{\min}(X)$. Vì vậy $X \succeq 0$ khi và chỉ khi $\lambda_{\min}(X) \ge 0$.

## 5. Những cái bẫy khi kiểm tra tính nửa xác định dương

Điều kiện PSD nói về **dạng toàn phương**, không nói về từng phần tử. Vì vậy những phép kiểm tra trông hợp lý sau đây đều sai:

- **Mọi phần tử không âm không suy ra PSD.** Ma trận $\begin{bmatrix} 1 & 2 \\ 2 & 1 \end{bmatrix}$ có mọi phần tử dương nhưng có trị riêng $-1$. Với $z = (1, -1)$, $z^T X z = 1 - 4 + 1 = -2 < 0$.
- **PSD không đòi các phần tử không âm.** Ma trận $\begin{bmatrix} 1 & -1 \\ -1 & 1 \end{bmatrix}$ có phần tử âm nhưng $z^T X z = (z_1 - z_2)^2 \ge 0$, nên PSD, với trị riêng $0$ và $2$.
- **Đường chéo không âm và định thức không âm chưa đủ khi $n \ge 3$.** Ma trận $\begin{bmatrix} 0 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 1 & 0 \end{bmatrix}$ có đường chéo bằng 0, định thức bằng 0, các định thức con chính đầu tiên đều bằng 0, nhưng với $z = (0, 1, -1)$ thì $z^T X z = -2$. Tiêu chuẩn Sylvester dùng các định thức con chính **đầu** chỉ đúng cho xác định dương. Với nửa xác định dương, phải xét **mọi** định thức con chính, kể cả những định thức không nằm ở góc trên bên trái.

Cách kiểm tra đáng tin cậy là tính trị riêng nhỏ nhất, hoặc thử phân tích Cholesky. Trên máy tính, người ta thường chọn cách sau vì nó nhanh và báo lỗi ngay khi ma trận không xác định dương.

## 6. Vì sao ma trận PSD xuất hiện khắp nơi

Ba ví dụ dưới đây giải thích vì sao trong học máy, ma trận PSD gần như tự xuất hiện:

- **Ma trận hiệp phương sai** $\Sigma = \operatorname{Cov}(x)$ của một vector ngẫu nhiên luôn PSD. Lý do rất đẹp: Với mọi $v$, $v^T \Sigma v = \operatorname{Var}(v^T x) \ge 0$, vì phương sai của một biến ngẫu nhiên vô hướng không bao giờ âm. Dạng toàn phương của ma trận hiệp phương sai theo hướng $v$ chính là phương sai của dữ liệu khi chiếu lên hướng $v$.
- **Ma trận Gram** $K_{ij} = \phi(x_i)^T \phi(x_j)$, nền tảng của các phương pháp kernel, luôn PSD vì $v^T K v = \left\|\sum_i v_i \phi(x_i)\right\|_2^2 \ge 0$.
- **Hessian của hàm lồi** là PSD tại mọi điểm. Đó là nội dung của điều kiện bậc hai ở chủ đề về độ cong. Hàm mất mát bình phương tối thiểu có Hessian $2A^T A$, một ma trận Gram.

Vì $\mathbb{S}^n_+$ là nón lồi, ta có thể so sánh hai ma trận bằng cách xét hiệu của chúng: $X \preceq Y$ nghĩa là $Y - X \succeq 0$. Chẳng hạn $\Sigma_1 \preceq \Sigma_2$ nghĩa là theo **mọi** hướng, dữ liệu thứ nhất biến thiên không nhiều hơn dữ liệu thứ hai. Đây là một "bất đẳng thức giữa các ma trận", và chủ đề về bất đẳng thức tổng quát sẽ xây dựng nó một cách chặt chẽ.

## 7. Những câu hỏi để đào sâu

**Câu 1.** Ma trận đơn vị $I$ nằm ở đâu trong nón $\mathbb{S}^n_+$: Trên biên hay bên trong? Còn ma trận $\begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}$ thì sao?

<details><summary>Xem lời giải thích</summary>

$I$ có mọi trị riêng bằng 1 > 0 nên xác định dương, và nằm bên trong nón: Mọi ma trận đối xứng đủ gần $I$ vẫn có trị riêng dương. Thật ra $I$ nằm trên trục của nón, vì nó "cân bằng" theo mọi hướng. Ma trận $\operatorname{diag}(1, 0)$ có một trị riêng bằng 0 nên nằm trên biên: Thêm một lượng âm rất nhỏ vào phần tử thứ hai trên đường chéo là đủ đưa nó ra ngoài nón. Phần trong của $\mathbb{S}^n_+$ (trong không gian $\mathbb{S}^n$) đúng là $\mathbb{S}^n_{++}$.

</details>

**Câu 2.** Tích của hai ma trận PSD có PSD không? Hãy thử với $A = \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}$ và $B = \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix}$.

<details><summary>Xem lời giải thích</summary>

$AB = \begin{bmatrix} 1 & 1 \\ 0 & 0 \end{bmatrix}$, không đối xứng, nên câu hỏi "có PSD không" theo định nghĩa của ta thậm chí không đặt ra được. Nón $\mathbb{S}^n_+$ khép kín với tổ hợp nón, nhưng không khép kín với phép nhân ma trận. Phép toán "an toàn" là $B^T A B$: Nếu $A \succeq 0$ thì $z^T B^T A B z = (Bz)^T A (Bz) \ge 0$, nên $B^T A B \succeq 0$ với mọi $B$.

</details>

**Câu 3.** Với những giá trị $t$ nào thì $\begin{bmatrix} 2 & t \\ t & 8 \end{bmatrix} \succeq 0$? Tập các $t$ đó có hình dạng gì, và vì sao điều đó không phải ngẫu nhiên?

<details><summary>Xem lời giải thích</summary>

Theo điều kiện $2 \times 2$: $2 \ge 0$, $8 \ge 0$ và $16 \ge t^2$, tức $-4 \le t \le 4$. Tập các $t$ là một đoạn thẳng, một tập lồi. Điều này không ngẫu nhiên: Ánh xạ $t \mapsto \begin{bmatrix} 2 & t \\ t & 8 \end{bmatrix}$ là affine, và tập các $t$ là ảnh ngược của nón lồi $\mathbb{S}^2_+$ qua ánh xạ đó. Chủ đề về các phép toán giữ tính lồi sẽ chứng minh ảnh ngược affine của tập lồi luôn lồi. Hai đầu mút $t = \pm 4$ cho ma trận suy biến, và ma trận xác định dương khi $|t| < 4$.

</details>

**Câu 4.** Nếu $X \succeq 0$, có đúng là mọi phần tử trên đường chéo của $X$ đều không âm, và $|X_{ij}| \le \sqrt{X_{ii} X_{jj}}$ không? Vì sao?

<details><summary>Xem lời giải thích</summary>

Đúng. Chọn $z = e_i$ cho $X_{ii} = e_i^T X e_i \ge 0$. Ma trận con $\begin{bmatrix} X_{ii} & X_{ij} \\ X_{ij} & X_{jj} \end{bmatrix}$ là $W^T X W$ với $W$ gồm hai cột $e_i, e_j$, nên cũng PSD, và điều kiện $2 \times 2$ cho $X_{ii} X_{jj} \ge X_{ij}^2$. Với ma trận hiệp phương sai, bất đẳng thức này chính là "hệ số tương quan nằm trong $[-1, 1]$". Đây là những điều kiện **cần**, không đủ, như ví dụ $3 \times 3$ ở mục 5 cho thấy.

</details>

## 8. Bài tập tự luyện

::: exercise 1. Kiểm tra ba ma trận
Ma trận nào dưới đây thuộc $\mathbb{S}^2_+$, ma trận nào thuộc $\mathbb{S}^2_{++}$: $A = \begin{bmatrix} 4 & 2 \\ 2 & 1 \end{bmatrix}$, $B = \begin{bmatrix} 3 & -1 \\ -1 & 2 \end{bmatrix}$, $C = \begin{bmatrix} 1 & 3 \\ 3 & 4 \end{bmatrix}$? Với ma trận không PSD, chỉ ra một vector $z$ làm $z^T X z < 0$.
:::

::: solution
$A$: $4 \ge 0$, $1 \ge 0$, $4 \cdot 1 - 4 = 0$, nên PSD nhưng không PD. Vector $z = (1, -2)$ cho $z^T A z = 4 - 8 + 4 = 0$. $B$: $3 > 0$ và $6 - 1 = 5 > 0$, nên PD. $C$: $4 - 9 = -5 < 0$, nên không PSD. Chọn $z = (3, -1)$: $z^T C z = 9 - 18 + 4 = -5 < 0$.
:::

::: exercise 2. Tổ hợp nón cụ thể
Cho $A = \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix}$ và $B = \begin{bmatrix} 1 & -1 \\ -1 & 1 \end{bmatrix}$. Kiểm tra $A, B \in \mathbb{S}^2_+$, tính $A + B$ và $2A + 3B$, rồi giải thích vì sao hai ma trận vừa tính PSD mà không cần tính trị riêng.
:::

::: solution
$A$: $1 \cdot 1 - 1 = 0$, PSD. $B$: $1 \cdot 1 - 1 = 0$, PSD. $A + B = \begin{bmatrix} 2 & 0 \\ 0 & 2 \end{bmatrix}$ và $2A + 3B = \begin{bmatrix} 5 & -1 \\ -1 & 5 \end{bmatrix}$. Cả hai là tổ hợp nón của hai ma trận PSD, nên PSD theo mệnh đề ở mục 3. Thú vị là $A$ và $B$ đều nằm trên biên của nón, nhưng $A + B$ lại nằm bên trong, vì $A$ "thiếu" theo hướng $(1, -1)$ còn $B$ "thiếu" theo hướng $(1, 1)$, và tổng của chúng bù cho nhau.
:::

::: exercise 3. Số chiều của Sⁿ
Một ma trận hiệp phương sai của dữ liệu 10 chiều có bao nhiêu số cần ước lượng độc lập? Nếu chỉ ước lượng một ma trận chéo thì còn bao nhiêu? Tập các ma trận chéo không âm có phải một nón con của $\mathbb{S}^{10}_+$ không?
:::

::: solution
$\mathbb{S}^{10}$ có số chiều $\tfrac{10 \cdot 11}{2} = 55$, nên có 55 số cần ước lượng. Ma trận chéo chỉ có 10 số. Tập các ma trận chéo với đường chéo không âm là một nón lồi (nó giống hệt $\mathbb{R}^{10}_+$), và mọi phần tử của nó đều PSD, nên nó là một nón con của $\mathbb{S}^{10}_+$. Giả định hiệp phương sai chéo là một cách giảm số tham số, đổi lại ta bỏ qua mọi tương quan giữa các thành phần.
:::

## Tóm tắt

Ma trận đối xứng cỡ $n \times n$ tạo thành không gian vector $\mathbb{S}^n$ có số chiều $\tfrac{n(n+1)}{2}$, và $\mathbb{S}^2$ đồng nhất với $\mathbb{R}^3$. Tập các ma trận PSD là một nón lồi, vì $z^T X z$ tuyến tính theo $X$. Nó cũng là giao của vô số nửa không gian, mỗi hướng $z$ một cái, nên biên của nó cong. Trong $\mathbb{S}^2$, điều kiện PSD là $x \ge 0$, $z \ge 0$, $xz \ge y^2$, và nón có dạng một nón kem với trục là đường chéo $x = z$.

PSD là điều kiện trên dạng toàn phương, không phải trên từng phần tử. Ma trận hiệp phương sai, ma trận Gram và Hessian của hàm lồi đều PSD vì những lý do có thể giải thích bằng một dòng. Sau trang này, bạn có thể kiểm tra một ma trận có PSD không, chỉ ra một hướng bác bỏ khi nó không PSD, và giải thích vì sao tập các tham số làm một ma trận affine trở nên PSD là một tập lồi.

## Nguồn và đọc thêm

- S. Boyd, L. Vandenberghe, *Convex Optimization*, §2.2.5 (tr. 34–35), Ví dụ 2.6 và Hình 2.12. Ví dụ 2.7 (tr. 36) về giao vô hạn nửa không gian. Phân tích phổ, tiêu chuẩn PSD và phần bù Schur ở phụ lục A.5.
- Các ví dụ về cái bẫy, ma trận $3 \times 3$, liên hệ với hiệp phương sai, ma trận Gram, các câu hỏi và bài tập do người soạn bổ sung. Mọi con số đã được tính lại bằng chương trình.
