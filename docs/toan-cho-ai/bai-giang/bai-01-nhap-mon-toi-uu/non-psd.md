---
course: toan-cho-ai
lecture: bai-01-nhap-mon-toi-uu
topic: non-psd
section: topic
title: "Nón các ma trận nửa xác định dương"
description: "Không gian các ma trận đối xứng, nón S₊ⁿ và Sⁿ₊₊, chứng minh tính nón lồi, biểu diễn như giao vô hạn nửa không gian, điều kiện cho ma trận 2×2, những cái bẫy khi kiểm tra tính nửa xác định dương và vai trò của ma trận hiệp phương sai, ma trận Gram."
---

Trong các chủ đề trước, mỗi "điểm" trong không gian luôn là một vector cột hữu hạn chiều. Bài học này đưa ta tới một bước chuyển tư duy trừu tượng quan trọng: Xem mỗi **ma trận đối xứng** là một điểm đơn lẻ trong một không gian vector nhiều chiều, và khảo sát cấu trúc hình học của tập hợp các ma trận nửa xác định dương. Tập hợp này tạo thành một nón lồi đóng, và khi quan sát trong không gian ba chiều, nó mang hình dáng của một nón kem uốn lượn tuyệt đẹp.

Tại sao tối ưu hóa và học máy lại đặt trọng tâm vào hình học của một tập hợp các ma trận? Bởi vì rất nhiều đối tượng quyết định then chốt trong học máy chính là các ma trận: Ma trận hiệp phương sai trong mô hình xác suất, ma trận kernel trong máy vector hỗ trợ (SVM), ma trận Hessian đo độ cong của hàm mất mát, hay ma trận metric trong học biểu diễn. Ràng buộc "ma trận này phải nửa xác định dương" xuất hiện ở mọi nhánh của trí tuệ nhân tạo, và việc tập hợp các ma trận đó tạo thành một nón lồi là nền tảng toán học bảo đảm các bài toán này có thể giải được hiệu quả thông qua quy hoạch nửa xác định (SDP).

Kiến thức nền tảng bao gồm định nghĩa ma trận nửa xác định dương, phép phân tích phổ của ma trận đối xứng thực và khái niệm nón lồi.

## 1. Ma trận đối xứng như một điểm trong không gian

Ký hiệu $\mathbb{S}^n$ là tập hợp tất cả các ma trận thực đối xứng kích thước $n \times n$:

$$
\mathbb{S}^n = \{X \in \mathbb{R}^{n \times n} \mid X = X^T\} .
$$

Các phép toán cộng hai ma trận đối xứng và nhân một ma trận đối xứng với một số thực luôn tạo ra một ma trận đối xứng. Do đó, $\mathbb{S}^n$ là một không gian vector thực. Số chiều của không gian này là:

$$
\dim \mathbb{S}^n = \frac{n(n+1)}{2} ,
$$

bởi vì một ma trận đối xứng được xác định duy nhất qua các phần tử nằm trên đường chéo chính và các phần tử nằm phía trên đường chéo chính.

Xét trường hợp $n = 2$: Mỗi ma trận đối xứng $2 \times 2$ có dạng:

$$
X = \begin{bmatrix} x & y \\ y & z \end{bmatrix}
$$

được tham số hóa duy nhất bởi bộ ba số thực $(x, y, z) \in \mathbb{R}^3$. Vì vậy, không gian $\mathbb{S}^2$ đẳng cấu trực tiếp với không gian tọa độ $\mathbb{R}^3$, cho phép ta dựng hình và trực quan hóa các tập ma trận $2 \times 2$ như những vật thể hình học 3D quen thuộc. Khi $n = 3$, không gian $\mathbb{S}^3$ có số chiều bằng $\tfrac{3 \cdot 4}{2} = 6$; dù không thể vẽ trực tiếp trong không gian mắt nhìn, mọi quy luật hình học về đoạn thẳng, tổ hợp lồi và nón đều giữ nguyên hiệu lực toán học.

Tích vô hướng chuẩn mực trên không gian ma trận $\mathbb{S}^n$ là **tích vô hướng Frobenius** (hay vết):

$$
\langle X, Y \rangle = \operatorname{tr}(XY) = \sum_{i=1}^n \sum_{j=1}^n X_{ij} Y_{ij} .
$$

Tích vô hướng này tạo nên chuẩn Frobenius $\|X\|_F = \sqrt{\operatorname{tr}(X^2)} = \sqrt{\sum_{i,j} X_{ij}^2}$, đóng vai trò chuẩn Euclid tự nhiên trên không gian các ma trận đối xứng.

## 2. Các tập hợp ma trận đối xứng và ký hiệu

Tương tự như cấu trúc các tập số thực $\mathbb{R}$, tập số không âm $\mathbb{R}_+$ và tập số dương $\mathbb{R}_{++}$, ta phân loại không gian $\mathbb{S}^n$ thành ba tập hợp cơ bản:

- $\mathbb{S}^n$: Không gian toàn phần gồm mọi ma trận đối xứng cỡ $n \times n$.
- $\mathbb{S}^n_+ = \{X \in \mathbb{S}^n \mid X \succeq 0\}$: Tập các ma trận **nửa xác định dương** (Positive Semidefinite - PSD), tức thỏa mãn $z^T X z \ge 0$ với mọi vector $z \in \mathbb{R}^n$.
- $\mathbb{S}^n_{++} = \{X \in \mathbb{S}^n \mid X \succ 0\}$: Tập các ma trận **xác định dương** (Positive Definite - PD), tức thỏa mãn $z^T X z > 0$ với mọi vector $z \ne 0$.

Mối liên hệ tương đương thông qua phân tích phổ:
- Một ma trận đối xứng thuộc $\mathbb{S}^n_+$ khi và chỉ khi toàn bộ các trị riêng của nó không âm: $\lambda_i(X) \ge 0, \forall i = 1, \dots, n$.
- Một ma trận đối xứng thuộc $\mathbb{S}^n_{++}$ khi và chỉ khi toàn bộ các trị riêng của nó dương chặt: $\lambda_i(X) > 0, \forall i = 1, \dots, n$.

Nói cách khác, điều kiện $X \succeq 0$ phản ánh rằng ma trận hành xử như một "số không âm đa chiều", không làm đổi chiều bất kỳ vector nào khi tính dạng toàn phương $z^T X z$.

## 3. Bản chất nón lồi và tính chất nón chính quy của $\mathbb{S}^n_+$

> **Mệnh đề.** $\mathbb{S}^n_+$ là một nón lồi: Nếu $A, B \in \mathbb{S}^n_+$ và các hệ số $\theta_1, \theta_2 \ge 0$, thì tổ hợp nón $\theta_1 A + \theta_2 B \in \mathbb{S}^n_+$.

Chứng minh mệnh đề này bắt nguồn trực tiếp từ tính chất tuyến tính của dạng toàn phương mà không cần thông qua các trị riêng. Với mọi vector thử $z \in \mathbb{R}^n$:

$$
\begin{aligned}
z^T (\theta_1 A + \theta_2 B) z &= \theta_1\, z^T A z + \theta_2\, z^T B z\\
&\ge 0 ,
\end{aligned}
$$

bởi vì $z^T A z \ge 0$ và $z^T B z \ge 0$ theo giả thiết, kết hợp với các trọng số $\theta_1, \theta_2 \ge 0$. Đẳng thức trên chứng minh rằng: Khi cố định vector $z$, ánh xạ $X \mapsto z^T X z$ là một hàm **tuyến tính** theo ma trận $X$.

Nhận xét này mang lại một góc nhìn hình học sâu sắc: Với mỗi vector $z \ne 0$ cố định, dạng toàn phương có thể viết qua tích vô hướng Frobenius:

$$
\begin{aligned}
z^T X z &= \operatorname{tr}(z^T X z)\\
&= \operatorname{tr}(X z z^T)\\
&= \langle z z^T, X \rangle .
\end{aligned}
$$

Biểu thức $\langle z z^T, X \rangle \ge 0$ xác định một **nửa không gian đóng** đi qua gốc tọa độ trong không gian $\mathbb{S}^n$ với vector pháp tuyến ngoài là ma trận hạng một $-z z^T$. Do đó, nón $\mathbb{S}^n_+$ có thể biểu diễn dưới dạng phần giao:

$$
\begin{aligned}
\mathbb{S}^n_+ &= \bigcap_{z \ne 0} \{X \in \mathbb{S}^n \mid z^T X z \ge 0\}\\
&= \bigcap_{z \ne 0} \{X \in \mathbb{S}^n \mid \langle z z^T, X \rangle \ge 0\} .
\end{aligned}
$$

Đây là phần giao của **vô số** nửa không gian đóng. Do đó, $\mathbb{S}^n_+$ tự động là một tập lồi và đóng. Khác với đa diện (vốn chỉ là giao của hữu hạn nửa không gian), biên của nón $\mathbb{S}^n_+$ là một mặt cong trơn từng phần, tạo nên sự phong phú vượt bậc của hình học quy hoạch nửa xác định.

Hơn thế nữa, $\mathbb{S}^n_+$ là một **nón chính quy** (proper cone), thỏa mãn đủ bốn tiêu chí:
1. **Lồi**: Đóng kín với các tổ hợp nón.
2. **Đóng**: Chứa toàn bộ các điểm giới hạn của nó.
3. **Nhọn (pointed)**: Chứa không chứa bất kỳ đường thẳng đầy đủ nào. Thật vậy, nếu $X \in \mathbb{S}^n_+$ và $-X \in \mathbb{S}^n_+$, thì với mọi $z$ ta có $z^T X z \ge 0$ và $-z^T X z \ge 0 \implies z^T X z = 0$, kéo theo toàn bộ trị riêng của $X$ bằng 0, tức $X = 0$.
4. **Phần trong khác rỗng**: Phần trong topo của nón trong không gian $\mathbb{S}^n$ chính là tập các ma trận xác định dương: $\operatorname{int}(\mathbb{S}^n_+) = \mathbb{S}^n_{++}$.

Là một nón chính quy, $\mathbb{S}^n_+$ thiết lập một **thứ tự riêng phần suy rộng** (generalized inequality) trên không gian các ma trận đối xứng: Ký hiệu $A \preceq B$ (hoặc $B \succeq A$) mang nghĩa là $B - A \in \mathbb{S}^n_+$.

## 4. Hình học trực quan của nón PSD trong không gian $\mathbb{S}^2$

Với các ma trận đối xứng kích thước $2 \times 2$, điều kiện nửa xác định dương được cụ thể hóa bằng hệ bất đẳng thức vô hướng:

$$
\begin{bmatrix} x & y \\ y & z \end{bmatrix} \succeq 0 \iff x \ge 0,\quad z \ge 0,\quad xz \ge y^2 .
$$

Cơ sở toán học: Ma trận có hai trị riêng $\lambda_1, \lambda_2$ với tổng bằng vết $\lambda_1 + \lambda_2 = x + z$ và tích bằng định thức $\lambda_1 \lambda_2 = xz - y^2$. Hai số thực không âm khi và chỉ khi tích của chúng không âm và tổng của chúng không âm. Bất đẳng thức $xz \ge y^2$ kéo theo $xz \ge 0$, buộc $x$ và $z$ cùng dấu; kết hợp với $x + z \ge 0$ dẫn tới $x \ge 0$ và $z \ge 0$.

Đường biên của nón được xác định bởi phương trình mặt cong $xz = y^2$ với $x \ge 0, z \ge 0$. Thực hiện phép đổi biến xoay hệ tọa độ 45° trong mặt phẳng $(x, z)$:

$$
\begin{aligned}
u &= \frac{x + z}{\sqrt{2}},\quad w\\
&= \frac{x - z}{\sqrt{2}}\\
&\iff x = \frac{u + w}{\sqrt{2}},\quad z\\
&= \frac{u - w}{\sqrt{2}} .
\end{aligned}
$$

Khi đó, tích tọa độ trở thành:

$$
\begin{aligned}
xz &= \frac{u^2 - w^2}{2}\\
&\ge y^2\\
&\iff w^2 + 2y^2 \le u^2\\
&\iff \sqrt{w^2 + 2y^2} \le u .
\end{aligned}
$$

Kết hợp với điều kiện $u \ge 0$, bất đẳng thức này mô tả một **nón bậc hai elip** (elliptic second-order cone) trong không gian 3D $(u, w, y)$. Trục đối xứng của nón là tia $u \ge 0, w = 0, y = 0$ (tức đường phân giác $x = z \ge 0, y = 0$, tương ứng với các ma trận vô hướng $x I$). Các lát cắt vuông góc với trục đối xứng (tức tại $u = c > 0$) là những hình ellipse phẳng $w^2 + 2y^2 \le c^2$.

Mô phỏng 3D dưới đây tái hiện trực quan nón PSD trong không gian tọa độ $\mathbb{S}^2$.

<Cone3DLab type="psd" />

Mô phỏng tiếp theo khảo sát cùng một ma trận theo góc nhìn dạng toàn phương: Vẽ giá trị $v^T X v$ khi vector đơn vị $v$ quét qua toàn bộ đường tròn đơn vị. Ma trận thuộc $\mathbb{S}^2_+$ khi và chỉ khi không có bất kỳ hướng nào làm dạng toàn phương nhận giá trị âm.

<PsdLab />

Cực tiểu của dạng toàn phương trên mặt cầu đơn vị chính là trị riêng nhỏ nhất của ma trận:

$$
\min_{\|v\|_2 = 1} v^T X v = \lambda_{\min}(X) .
$$

Do đó, $X \succeq 0$ khi và chỉ khi giá trị hàm mục tiêu nhỏ nhất $\lambda_{\min}(X) \ge 0$.

## 5. Những bẫy tư duy phổ biến khi kiểm tra tính nửa xác định dương

Khái niệm nửa xác định dương gắn liền với **dạng toàn phương và phổ trị riêng**, không tương đương với dấu của từng phần tử độc lập. Dưới đây là ba cái bẫy thường gặp:

1. **Mọi phần tử không âm không bảo đảm tính PSD**:
   Xét ma trận $X = \begin{bmatrix} 1 & 2 \\ 2 & 1 \end{bmatrix}$. Tất cả các phần tử đều dương, nhưng định thức là $\det X = 1 - 4 = -3 < 0$, cho hai trị riêng là $3$ và $-1$. Chọn vector $z = (1, -1)$, ta có $z^T X z = 1 - 4 + 1 = -2 < 0$, chứng minh ma trận không PSD.
2. **Ma trận PSD hoàn toàn có thể chứa các phần tử âm ngoài đường chéo**:
   Xét ma trận $X = \begin{bmatrix} 1 & -1 \\ -1 & 1 \end{bmatrix}$. Các phần tử ngoài đường chéo là số âm, nhưng dạng toàn phương:
   $$
   \begin{aligned}
   z^T X z &= z_1^2 - 2z_1 z_2 + z_2^2\\
   &= (z_1 - z_2)^2\\
   &\ge 0
   \end{aligned}
   $$
   với mọi vector $z$. Ma trận này thuộc $\mathbb{S}^2_+$ với hai trị riêng là $0$ và $2$.
3. **Đường chéo không âm và định thức không âm là chưa đủ khi $n \ge 3$**:
   Xét ma trận:
   $$
   X = \begin{bmatrix} 0 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 1 & 0 \end{bmatrix} .
   $$
   Đường chéo toàn số 0, định thức bằng 0, nhưng khối ma trận con góc dưới bên phải có định thức $-1$. Thật vậy, với vector $z = (0, 1, -1)$, ta có $z^T X z = -2 < 0$.
   > **Lưu ý quan trọng**: Tiêu chuẩn Sylvester (chỉ kiểm tra các định thức con chính dẫn đầu góc trên bên trái) chỉ áp dụng cho ma trận xác định dương ($X \succ 0$). Để kiểm tra tính nửa xác định dương ($X \succeq 0$), ta bắt buộc phải kiểm tra **toàn bộ mọi định thức con chính** ở tất cả các vị trí, hoặc tính trực tiếp trị riêng nhỏ nhất.

Trong tính toán thực tế trên máy tính, giải thuật kiểm tra tin cậy và tối ưu nhất là thực hiện **phân tích Cholesky** ($X = L L^T$): Giải thuật sẽ hoàn tất thành công nếu ma trận xác định dương và báo lỗi dừng ngay khi gặp phần tử không hợp lệ.

## 6. Sự hiện diện phổ quát của ma trận PSD trong học máy

Ma trận nửa xác định dương xuất hiện tự nhiên tại trung tâm của các mô hình học máy:

### Ma trận hiệp phương sai
Cho vector ngẫu nhiên $x \in \mathbb{R}^n$, ma trận hiệp phương sai $\Sigma = \operatorname{Cov}(x) = \mathbb{E}[(x - \mu)(x - \mu)^T]$ luôn thuộc $\mathbb{S}^n_+$. Lý do: Với mọi vector $v \in \mathbb{R}^n$, đại lượng toàn phương:

$$
v^T \Sigma v = \operatorname{Var}(v^T x) \ge 0 ,
$$

chính là phương sai của biến ngẫu nhiên vô hướng thu được khi chiếu dữ liệu lên phương $v$. Vì phương sai không bao giờ âm, ma trận hiệp phương sai luôn luôn nửa xác định dương.

### Ma trận Gram và hàm Kernel
Trong các phương pháp kernel (như SVM Kernel, Gaussian Process), ma trận Gram xác định bởi $K_{ij} = k(x_i, x_j) = \phi(x_i)^T \phi(x_j)$ luôn thuộc $\mathbb{S}^m_+$ với mọi tập mẫu dữ liệu. Thật vậy, với mọi vector trọng số $v \in \mathbb{R}^m$:

$$
\begin{aligned}
v^T K v &= \sum_{i=1}^m \sum_{j=1}^m v_i v_j \phi(x_i)^T \phi(x_j)\\
&= \left\|\sum_{i=1}^m v_i \phi(x_i)\right\|_2^2\\
&\ge 0 .
\end{aligned}
$$

Định lý Mercer khẳng định: Một hàm hai biến $k(x, y)$ là một kernel hợp lệ khi và chỉ khi mọi ma trận Gram sinh ra từ nó đều thuộc nón $\mathbb{S}^m_+$.

### Ma trận Hessian của hàm lồi
Một hàm khả vi liên tục hai lần $f \colon \mathbb{R}^n \to \mathbb{R}$ là hàm lồi khi và chỉ khi ma trận Hessian của nó nửa xác định dương tại mọi điểm: $\nabla^2 f(x) \succeq 0, \forall x$. Chẳng hạn với hàm mất mát bình phương tuyến tính $f(w) = \|X w - y\|_2^2$, ma trận Hessian là $\nabla^2 f(w) = 2 X^T X$, chính là một ma trận Gram có dạng toàn phương $2\|X z\|_2^2 \ge 0$.

## 7. Những câu hỏi để đào sâu

**Câu 1.** Ma trận đơn vị $I$ nằm ở đâu trong nón $\mathbb{S}^n_+$: Nằm trên biên hay nằm trong phần trong? Còn ma trận chiếu $P = \operatorname{diag}(1, 0)$ thì sao?

<details><summary>Xem lời giải thích</summary>

Ma trận đơn vị $I$ có toàn bộ các trị riêng bằng 1 > 0, do đó $I \in \mathbb{S}^n_{++}$, tức nằm sâu trong phần trong của nón. Mọi ma trận đối xứng đủ gần $I$ đều giữ nguyên tính xác định dương. Ma trận đơn vị nằm chính xác trên trục đối xứng của nón vì nó đẳng hướng theo mọi phương. Ngược lại, ma trận $P = \operatorname{diag}(1, 0)$ có một trị riêng bằng 0, do đó $P$ nằm trên biên của nón $\mathbb{S}^2_+$: Chỉ cần một độ lệch âm rất nhỏ ở phần tử thứ hai trên đường chéo là đủ đẩy ma trận ra khỏi nón PSD. Phần trong của nón $\mathbb{S}^n_+$ chính là tập các ma trận xác định dương $\mathbb{S}^n_{++}$.

</details>

**Câu 2.** Tích của hai ma trận thuộc $\mathbb{S}^n_+$ có luôn thuộc $\mathbb{S}^n_+$ hay không? Xét ví dụ với hai ma trận $A = \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}$ và $B = \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix}$.

<details><summary>Xem lời giải thích</summary>

Tích của hai ma trận PSD nói chung không phải là ma trận PSD, thậm chí không đối xứng. Với hai ma trận đã cho: Tích là $AB = \begin{bmatrix} 1 & 1 \\ 0 & 0 \end{bmatrix}$, một ma trận không đối xứng nên không thuộc không gian $\mathbb{S}^2$. Nón $\mathbb{S}^n_+$ đóng kín đối với phép cộng và phép nhân vô hướng không âm, nhưng không đóng kín đối với phép nhân ma trận thông thường. Phép biến đổi hợp lệ giữ tính đối xứng và bảo toàn tính PSD là phép liên hợp $B^T A B$: Nếu $A \succeq 0$, thì với mọi vector $z$ ta có $z^T (B^T A B) z = (Bz)^T A (Bz) \ge 0$, suy ra $B^T A B \succeq 0$ với mọi ma trận $B$.

</details>

**Câu 3.** Tìm tất cả các giá trị tham số $t \in \mathbb{R}$ sao cho ma trận $X(t) = \begin{bmatrix} 2 & t \\ t & 8 \end{bmatrix} \succeq 0$. Tập hợp các giá trị $t$ tìm được có hình dạng gì, và vì sao tính chất đó không phải là sự ngẫu nhiên?

<details><summary>Xem lời giải thích</summary>

Áp dụng điều kiện cho ma trận $2 \times 2$: Ta cần $2 \ge 0$, $8 \ge 0$ và định thức không âm:

$$
\begin{aligned}
16 - t^2 &\ge 0\\
&\iff t^2 \le 16\\
&\iff -4 \le t\\
&\le 4 .
\end{aligned}
$$

Tập hợp các giá trị $t$ hợp lệ là đoạn đóng $[-4, 4]$, một tập lồi trong $\mathbb{R}$. Kết quả này không phải ngẫu nhiên: Ánh xạ $t \mapsto X(t)$ là một ánh xạ affine từ $\mathbb{R}$ vào $\mathbb{S}^2$, và tập các giá trị $t$ chính là ảnh ngược của nón lồi $\mathbb{S}^2_+$ qua ánh xạ affine đó. Ảnh ngược affine của một tập lồi luôn luôn là một tập lồi. Hai đầu mút $t = \pm 4$ ứng với ma trận suy biến nằm trên biên của nón.

</details>

**Câu 4.** Nếu ma trận $X \succeq 0$, liệu có đúng là mọi phần tử trên đường chéo đều không âm, và ta luôn có $|X_{ij}| \le \sqrt{X_{ii} X_{jj}}$ với mọi cặp chỉ số $i, j$ hay không?

<details><summary>Xem lời giải thích</summary>

Khẳng định này hoàn toàn đúng. Với mỗi chỉ số $i$, chọn vector cơ sở đơn vị $e_i$, ta có $e_i^T X e_i = X_{ii} \ge 0$. Với hai chỉ số phân biệt $i$ và $j$, xét ma trận con đối xứng kích thước $2 \times 2$ tạo bởi hai hàng và hai cột đó: $\begin{bmatrix} X_{ii} & X_{ij} \\ X_{ij} & X_{jj} \end{bmatrix}$. Ma trận con này có dạng $W^T X W$ với $W = [e_i \ e_j]$, do đó cũng là ma trận PSD. Áp dụng điều kiện định thức cho ma trận $2 \times 2$ ta thu được:

$$
\begin{aligned}
X_{ii} X_{jj} - X_{ij}^2 &\ge 0\\
&\iff X_{ij}^2 \le X_{ii} X_{jj}\\
&\iff |X_{ij}| \le \sqrt{X_{ii} X_{jj}} .
\end{aligned}
$$

Trong thống kê, bất đẳng thức này chính là điều kiện hệ số tương quan tuyến tính luôn nằm trong đoạn $[-1, 1]$.

</details>

## 8. Bài tập tự luyện

::: exercise 1. Kiểm tra tính chất của ba ma trận đối xứng
Trong các ma trận sau, ma trận nào thuộc $\mathbb{S}^2_+$, ma trận nào thuộc $\mathbb{S}^2_{++}$:
- Ma trận $A = \begin{bmatrix} 4 & 2 \\ 2 & 1 \end{bmatrix}$.
- Ma trận $B = \begin{bmatrix} 3 & -1 \\ -1 & 2 \end{bmatrix}$.
- Ma trận $C = \begin{bmatrix} 1 & 3 \\ 3 & 4 \end{bmatrix}$.

Với ma trận không thuộc $\mathbb{S}^2_+$, hãy chỉ ra một vector $z$ làm cho dạng toàn phương nhận giá trị âm.
:::

::: solution
Kiểm tra từng ma trận theo điều kiện định thức và phần tử đường chéo:
- Với ma trận $A$: Phần tử đường chéo $4 > 0, 1 > 0$, định thức $\det A = 4 \cdot 1 - 2^2 = 0$. Vì các phần tử đường chéo dương và định thức bằng 0, ma trận $A$ thuộc $\mathbb{S}^2_+$ (PSD) nhưng không thuộc $\mathbb{S}^2_{++}$ (không PD, nằm trên biên). Vector $z = (1, -2)$ cho:

$$
z^T A z = 4 - 8 + 4 = 0 .
$$
- Với ma trận $B$: Phần tử $B_{11} = 3 > 0$, định thức $\det B = 3 \cdot 2 - (-1)^2 = 5 > 0$. Cả hai điều kiện đều dương chặt, do đó $B \in \mathbb{S}^2_{++}$ (nằm trong phần trong của nón).
- Với ma trận $C$: Định thức $\det C = 1 \cdot 4 - 3^2 = 4 - 9 = -5 < 0$. Vì định thức âm, ma trận $C$ không thuộc $\mathbb{S}^2_+$. Chọn vector riêng ứng với trị riêng âm, hoặc thử vector $z = (3, -1)$:
  $$
  \begin{aligned}
  z^T C z &= 1(3)^2 + 2 \cdot 3(3)(-1) + 4(-1)^2\\
  &= 9 - 18 + 4\\
  &= -5\\
  &< 0 .
  \end{aligned}
  $$
:::

::: exercise 2. Tính chất tổ hợp nón và hiện tượng bù trừ
Cho hai ma trận suy biến nằm trên biên của nón gồm ma trận $A = \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix}$ và ma trận $B = \begin{bmatrix} 1 & -1 \\ -1 & 1 \end{bmatrix}$. Kiểm tra xem $A, B \in \mathbb{S}^2_+$, tính ma trận tổng $A + B$ và ma trận tổ hợp $2A + 3B$, rồi giải thích vì sao hai ma trận này thuộc phần trong của nón mà không cần tính trị riêng.
:::

::: solution
- Với ma trận $A$: Định thức $\det A = 1 - 1 = 0$ và $A_{11} = 1 \ge 0$, nên $A \in \mathbb{S}^2_+$.
- Với ma trận $B$: Định thức $\det B = 1 - 1 = 0$ và $B_{11} = 1 \ge 0$, nên $B \in \mathbb{S}^2_+$.

Tính các ma trận:
- $A + B = \begin{bmatrix} 2 & 0 \\ 0 & 2 \end{bmatrix} = 2 I$.
- Ma trận tổ hợp $2A + 3B$:

$$
\begin{aligned}
2A + 3B &= \begin{bmatrix} 2 & 2 \\ 2 & 2 \end{bmatrix} + \begin{bmatrix} 3 & -3 \\ -3 & 3 \end{bmatrix}\\
&= \begin{bmatrix} 5 & -1 \\ -1 & 5 \end{bmatrix} .
\end{aligned}
$$

Cả hai ma trận này đều là tổ hợp nón với hệ số dương của hai ma trận thuộc $\mathbb{S}^2_+$, do đó tự động thuộc $\mathbb{S}^2_+$ theo tính chất nón lồi. Hơn nữa:
- Ma trận $A + B = 2I$ có định thức bằng 4 > 0, thuộc $\mathbb{S}^2_{++}$.
- Ma trận $2A + 3B$ có định thức $5 \cdot 5 - (-1)^2 = 24 > 0$ và phần tử đường chéo $5 > 0$, cũng thuộc $\mathbb{S}^2_{++}$.

Giải thích hiện tượng: Ma trận $A$ suy biến triệt tiêu theo phương $z_A = (1, -1)$ ($z_A^T A z_A = 0$), trong khi ma trận $B$ suy biến triệt tiêu theo phương trực giao $z_B = (1, 1)$ ($z_B^T B z_B = 0$). Khi cộng lại, dạng toàn phương theo phương $z_A$ được bù đắp bởi $z_A^T B z_A = 4 > 0$, còn dạng toàn phương theo phương $z_B$ được bù đắp bởi $z_B^T A z_B = 4 > 0$. Sự bù trừ này giúp tổng của hai điểm nằm trên biên rơi sâu vào bên trong phần trong của nón.
:::

::: exercise 3. Số chiều và cấu trúc của nón con ma trận đường chéo
Trong không gian $\mathbb{S}^{10}$, có bao nhiêu tham số độc lập cần ước lượng cho một ma trận hiệp phương sai đầy đủ? Nếu áp dụng giả định ma trận hiệp phương sai là ma trận đường chéo, số tham số giảm còn bao nhiêu? Tập hợp các ma trận đường chéo với các phần tử không âm có phải là một nón lồi con của $\mathbb{S}^{10}_+$ hay không?
:::

::: solution
- Số chiều của không gian $\mathbb{S}^{10}$ là $\dim \mathbb{S}^{10} = \tfrac{10 \cdot 11}{2} = 55$. Do đó cần ước lượng 55 tham số độc lập cho một ma trận hiệp phương sai đầy đủ.
- Nếu ma trận có dạng đường chéo, số tham số cần ước lượng giảm xuống đúng bằng số phần tử đường chéo, tức 10 tham số.
- Tập các ma trận đường chéo có phần tử không âm $\mathcal{D}_+ = \{\operatorname{diag}(d_1, \dots, d_{10}) \mid d_i \ge 0, \forall i\}$ là một nón lồi (đẳng cấu với nón tọa độ $\mathbb{R}^{10}_+$). Vì mọi ma trận đường chéo có phần tử không âm đều có các trị riêng không âm, tập hợp $\mathcal{D}_+$ là một nón lồi con nằm trọn trong nón $\mathbb{S}^{10}_+$. Giả định ma trận đường chéo giúp giảm đáng kể độ phức tạp tính toán (từ 55 tham số xuống 10 tham số), đổi lại mô hình chấp nhận bỏ qua toàn bộ tương quan chéo giữa các biến ngẫu nhiên.
:::

## Tóm tắt

Không gian các ma trận đối xứng $\mathbb{S}^n$ có số chiều $\tfrac{n(n+1)}{2}$ và trang bị tích vô hướng Frobenius $\langle X, Y \rangle = \operatorname{tr}(XY)$. Tập hợp các ma trận nửa xác định dương $\mathbb{S}^n_+$ tạo thành một nón chính quy (lồi, đóng, nhọn và có phần trong khác rỗng $\mathbb{S}^n_{++}$). Nón này được biểu diễn như giao của vô số nửa không gian đóng $\{X \mid z^T X z \ge 0\}$, làm cho đường biên của nó mang tính chất trơn từng phần.

Trong không gian $\mathbb{S}^2$ (đẳng cấu với $\mathbb{R}^3$), nón $\mathbb{S}^2_+$ có hình dạng của một nón bậc hai elip có trục đối xứng dọc theo ma trận đơn vị $x = z$. Tính chất PSD phụ thuộc vào dạng toàn phương và phổ trị riêng, không phụ thuộc vào dấu của từng phần tử độc lập. Ma trận hiệp phương sai, ma trận Gram trong các phương pháp kernel và ma trận Hessian của hàm lồi đều thuộc nón PSD vì những lý do đại số và xác suất chặt chẽ. Nón $\mathbb{S}^n_+$ là nền tảng hình học của bất đẳng thức ma trận tuyến tính (LMI) và quy hoạch nửa xác định (SDP).

## Tài liệu tham khảo

- Stephen Boyd, Lieven Vandenberghe, *Convex Optimization*, Cambridge University Press.
