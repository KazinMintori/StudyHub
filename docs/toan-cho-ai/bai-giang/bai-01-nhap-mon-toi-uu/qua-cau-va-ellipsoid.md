---
course: toan-cho-ai
lecture: bai-01-nhap-mon-toi-uu
topic: qua-cau-va-ellipsoid
section: topic
title: "Quả cầu và ellipsoid"
description: "Quả cầu Euclid với hai cách biểu diễn và chứng minh tính lồi. Ellipsoid từ ma trận xác định dương, bán trục theo vector riêng, dạng ảnh affine của quả cầu đơn vị, ellipsoid suy biến, thể tích và liên hệ với phân phối Gauss."
---

Quả cầu Euclid là tập lồi trực quan nhất: Tập hợp mọi điểm có khoảng cách tới tâm không vượt quá bán kính $r$. Ellipsoid là hình ảnh biến dạng affine của quả cầu khi bị kéo dãn hoặc nén dọc theo các phương trực giao độc lập. Hai cấu trúc hình học này xuất hiện với tần suất dày đặc trong tối ưu hóa và học máy: Ràng buộc "tham số không được lệch quá xa giá trị khởi tạo" theo chuẩn Euclid tạo thành một quả cầu; miền tin cậy của một ước lượng thống kê, đường đồng mức của một hàm mục tiêu toàn phương lồi, hay vùng tin cậy trong phương pháp Newton đều mang hình dạng của một ellipsoid.

Bên cạnh vai trò làm miền ràng buộc, ellipsoid còn mang một giá trị sư phạm đặc biệt: Đây là nơi đầu tiên ta thấy một **ma trận đại số** chuyển hóa thành một **hình dạng hình học** rõ ràng. Các trị riêng của ma trận quyết định bình phương độ dài các bán trục, còn các vector riêng chỉ rõ phương hướng của các trục đó trong không gian. Nắm vững mối liên hệ này giúp người học hình dung trực quan bản chất của ma trận hiệp phương sai, ma trận Hessian và ma trận xác định dương trong các giải thuật học máy nâng cao.

Kiến thức nền tảng bao gồm phép phân tích phổ của ma trận đối xứng thực và khái niệm ma trận xác định dương.

## 1. Quả cầu Euclid

> **Định nghĩa.** **Quả cầu Euclid** đóng có tâm tại $x_c \in \mathbb{R}^n$ và bán kính $r > 0$ được định nghĩa là tập hợp:
> $$
> B(x_c, r) = \{x \in \mathbb{R}^n \mid \|x - x_c\|_2 \le r\} = \{x \in \mathbb{R}^n \mid (x - x_c)^T (x - x_c) \le r^2\} .
> $$

Trong đó $\|u\|_2 = \sqrt{u^T u} = \sqrt{\sum_{i=1}^n u_i^2}$ là chuẩn Euclid thông thường. Quả cầu bao gồm mọi điểm cách tâm không quá khoảng cách $r$, kể cả mặt cầu biên. Ngoài dạng bất đẳng thức trên, quả cầu còn có cách biểu diễn tham số hóa tương đương:

$$
B(x_c, r) = \{x_c + r u \mid \|u\|_2 \le 1\} .
$$

Biểu diễn này cho thấy: Để chạm tới một điểm bất kỳ trong quả cầu, ta xuất phát từ tâm $x_c$ và tịnh tiến theo một vector $ru$ có độ dài không vượt quá $r$. Hai cách viết này mô tả cùng một đối tượng hình học nhưng phục vụ hai mục đích bổ trợ nhau:
- **Dạng kiểm tra ràng buộc**: Cho một điểm $x$, dạng bất đẳng thức $\|x - x_c\|_2 \le r$ cho phép kiểm tra ngay lập tức xem $x$ có thuộc quả cầu hay không.
- **Dạng tham số hóa sinh điểm**: Dạng $x_c + ru$ cho phép sinh ra toàn bộ các điểm của quả cầu từ quả cầu đơn vị.

Sự bổ trợ giữa hai góc nhìn "kiểm tra ràng buộc" và "tham số hóa sinh điểm" là một sợi chỉ đỏ xuyên suốt lý thuyết tập lồi và quy hoạch đa diện.

Quả cầu Euclid luôn là một tập lồi. Lấy hai điểm bất kỳ $x_1, x_2 \in B(x_c, r)$ và hệ số $\theta \in [0, 1]$. Bằng cách biểu diễn tâm $x_c = \theta x_c + (1 - \theta)x_c$, ta tách hiệu thành hai thành phần độc lập:

$$
\begin{aligned}
\|\theta x_1 + (1-\theta) x_2 - x_c\|_2 &= \|\theta (x_1 - x_c) + (1 - \theta)(x_2 - x_c)\|_2 \\
&\le \|\theta (x_1 - x_c)\|_2 + \|(1 - \theta)(x_2 - x_c)\|_2 \\
&= \theta \|x_1 - x_c\|_2 + (1 - \theta)\|x_2 - x_c\|_2 \\
&\le \theta r + (1 - \theta) r = r .
\end{aligned}
$$

Bất đẳng thức đầu tiên sử dụng bất đẳng thức tam giác của chuẩn; đẳng thức tiếp theo dựa vào tính thuần nhất tuyệt đối kết hợp điều kiện $\theta \ge 0$ và $1 - \theta \ge 0$; bất đẳng thức cuối cùng tận dụng giả thiết hai điểm ban đầu thuộc quả cầu. Kỹ thuật biểu diễn tâm $x_c$ thành tổ hợp lồi của chính nó là mấu chốt để tách hiệu vector thành tổng hai số hạng độc lập.

## 2. Ellipsoid từ ma trận đối xứng xác định dương

> **Định nghĩa.** Một **ellipsoid** trong $\mathbb{R}^n$ là tập hợp có dạng:
> $$
> \mathcal{E} = \{x \in \mathbb{R}^n \mid (x - x_c)^T P^{-1} (x - x_c) \le 1\} ,
> $$
> trong đó $P \in \mathbb{S}^n_{++}$ ($P = P^T \succ 0$) là một ma trận đối xứng xác định dương và $x_c \in \mathbb{R}^n$ là **tâm** của ellipsoid.

Ma trận $P$ quyết định mức độ trải rộng và phương hướng của ellipsoid trong không gian. Quả cầu Euclid bán kính $r$ là trường hợp riêng khi chọn $P = r^2 I$, bởi khi đó ma trận nghịch đảo là $P^{-1} = \tfrac{1}{r^2} I$ và bất đẳng thức trở thành $\tfrac{1}{r^2} \|x - x_c\|_2^2 \le 1$.

Để hiểu rõ hình dạng hình học của $\mathcal{E}$, ta sử dụng phân tích phổ (spectral decomposition) của ma trận đối xứng thực. Ma trận $P$ có thể khai triển thành:

$$
P = Q \Lambda Q^T = \sum_{i=1}^n \lambda_i q_i q_i^T ,
$$

trong đó $Q = [q_1 \ \dots \ q_n]$ là ma trận trực giao ($Q^T Q = I$) chứa các vector riêng trực chuẩn $q_i$, và $\Lambda = \operatorname{diag}(\lambda_1, \dots, \lambda_n)$ là ma trận đường chéo chứa các trị riêng dương $\lambda_i > 0$. Khi đó, ma trận nghịch đảo có dạng:

$$
P^{-1} = Q \Lambda^{-1} Q^T = \sum_{i=1}^n \frac{1}{\lambda_i} q_i q_i^T .
$$

Đặt $y = Q^T(x - x_c)$ là tọa độ của vector sai lệch $x - x_c$ trong hệ cơ sở trực chuẩn gồm các vector riêng $q_1, \dots, q_n$. Điều kiện xác định ellipsoid trở thành:

$$
y^T \Lambda^{-1} y = \sum_{i=1}^n \frac{y_i^2}{\lambda_i} = \frac{y_1^2}{\lambda_i} + \frac{y_2^2}{\lambda_2} + \dots + \frac{y_n^2}{\lambda_n} \le 1 .
$$

Biểu thức này chính là phương trình chuẩn tắc của một ellipsoid quen thuộc trong hình học giải tích. Từ đây ta rút ra kết luận hình học căn bản: **Bán trục thứ $i$ của ellipsoid nằm dọc theo phương của vector riêng $q_i$ và có độ dài bằng $\sqrt{\lambda_i}$**. Trị riêng lớn ứng với bán trục dài, còn trị riêng nhỏ ứng với bán trục ngắn. Phép biến đổi tọa độ $y = Q^T(x - x_c)$ chỉ gồm hai thao tác hình học bảo toàn khoảng cách: Tịnh tiến tâm về gốc tọa độ và xoay hệ trục theo ma trận trực giao $Q$.

Các phần tử riêng lẻ của ma trận $P$, chẳng hạn $P_{12}$, không phản ánh trực tiếp một đặc tính hình học độc lập nào vì chúng thay đổi khi ta đổi hệ trục tọa độ. Ngược lại, các trị riêng và vector riêng gắn liền với hình dạng thực của ellipsoid và bất biến đối với các phép quay hệ quy chiếu.

::: example Xác định các bán trục của một ellipse nghiêng
Xét ellipse trong $\mathbb{R}^2$ có tâm $x_c = (1, -1)$ và ma trận:

$$
P = \begin{bmatrix} 5 & 3 \\ 3 & 5 \end{bmatrix} .
$$

Đa thức đặc trưng của ma trận:

$$
\det(P - \lambda I) = (5 - \lambda)^2 - 9 = \lambda^2 - 10\lambda + 16 = 0 ,
$$

cho hai trị riêng $\lambda_1 = 8$ và $\lambda_2 = 2$. Các vector riêng đơn vị tương ứng là $q_1 = \tfrac{1}{\sqrt2}(1, 1)$ và $q_2 = \tfrac{1}{\sqrt2}(-1, 1)$.

Như vậy, ellipse có bán trục lớn nằm dọc theo đường phân giác $(1, 1)$ với độ dài bán trục là:

$$
a = \sqrt{\lambda_1} = \sqrt{8} = 2\sqrt{2} \approx 2.83 ,
$$

và bán trục nhỏ nằm theo hướng trực giao $(-1, 1)$ với độ dài bán trục là:

$$
b = \sqrt{\lambda_2} = \sqrt{2} \approx 1.41 .
$$

Để kiểm tra bằng định nghĩa, ma trận nghịch đảo là $P^{-1} = \tfrac{1}{16}\begin{bmatrix} 5 & -3 \\ -3 & 5 \end{bmatrix}$. Đỉnh của bán trục lớn là:

$$
x = x_c + a q_1 = (1, -1) + 2\sqrt{2} \cdot \tfrac{1}{\sqrt2}(1, 1) = (3, 1) .
$$

Vector độ lệch là $x - x_c = (2, 2)$, và giá trị dạng toàn phương là:

$$
(x - x_c)^T P^{-1} (x - x_c) = \begin{bmatrix} 2 & 2 \end{bmatrix} \left(\frac{1}{16}\begin{bmatrix} 5 & -3 \\ -3 & 5 \end{bmatrix}\right) \begin{bmatrix} 2 \\ 2 \end{bmatrix} = \frac{1}{16}(20 - 12 - 12 + 20) = 1 ,
$$

chứng minh điểm này nằm chính xác trên biên của ellipse.
:::

Người học có thể trực tiếp tương tác với mô phỏng dưới đây để quan sát sự thay đổi của hai bán trục và góc nghiêng của ellipse khi điều chỉnh các trị riêng của ma trận $P$.

<EllipsoidLab />

## 3. Ellipsoid dưới dạng ảnh affine của quả cầu đơn vị

Dạng biểu diễn thứ hai của ellipsoid dựa trên phép biến đổi affine:

$$
\mathcal{E} = \{x_c + A u \mid \|u\|_2 \le 1\} ,
$$

trong đó $A \in \mathbb{R}^{n \times n}$ là một ma trận không suy biến. Biểu diễn này khẳng định rằng: Một ellipsoid là ảnh của quả cầu đơn vị thông qua ánh xạ affine $u \mapsto x_c + Au$. Ta lấy một quả cầu tròn hoàn hảo, kéo dãn và xoay bằng phép biến đổi tuyến tính $A$, rồi tịnh tiến tâm tới vị trí $x_c$.

Hai cách biểu diễn này hoàn toàn tương đương khi liên hệ qua đẳng thức $P = AA^T$. Thật vậy, với mỗi điểm $x = x_c + Au$, dạng toàn phương tương ứng là:

$$
\begin{aligned}
(x - x_c)^T P^{-1} (x - x_c) &= (Au)^T (AA^T)^{-1} (Au) \\
&= u^T A^T (A^T)^{-1} A^{-1} A u \\
&= u^T I u = \|u\|_2^2 .
\end{aligned}
$$

Do đó, điều kiện $\|u\|_2 \le 1$ tương đương chính xác với điều kiện $(x - x_c)^T P^{-1} (x - x_c) \le 1$.

Cần tránh nhầm lẫn giữa ma trận $A$ và ma trận $P$: Quan hệ chuẩn xác là $P = AA^T$, tức $A$ đóng vai trò như một "căn bậc hai" của ma trận $P$. Cụ thể, ta luôn có thể chọn $A = P^{1/2} = Q \Lambda^{1/2} Q^T$, là căn bậc hai đối xứng xác định dương duy nhất của $P$. Khi $u$ chạy qua các vector cơ sở trực chuẩn $e_i$, điểm ảnh $A e_i$ tạo thành đúng các bán trục $\sqrt{\lambda_i} q_i$.

Hơn nữa, ma trận $A$ biểu diễn ellipsoid không phải là duy nhất: Với bất kỳ ma trận trực giao $U$ nào ($UU^T = I$), ma trận tích $\tilde{A} = AU$ cũng xác định cùng một ellipsoid, bởi quả cầu đơn vị bất biến qua phép quay ($\|U u\|_2 = \|u\|_2$), và ta có $\tilde{A}\tilde{A}^T = (AU)(U^T A^T) = AA^T = P$.

### Ellipsoid suy biến và liên hệ với nội tương đối
Nếu ma trận $A$ có hạng $\operatorname{rank}(A) = k < n$, ánh xạ $u \mapsto x_c + Au$ sẽ nén quả cầu $n$ chiều vào một không gian con affine có số chiều bằng $k$. Tập hợp thu được vẫn được gọi là một **ellipsoid suy biến** (degenerate ellipsoid).

Ellipsoid suy biến là một tập lồi, nhưng nó không thể biểu diễn dưới dạng nghịch đảo $(x - x_c)^T P^{-1}(x - x_c) \le 1$ vì ma trận $P = AA^T$ không khả nghịch. Xét trong không gian toàn phần $\mathbb{R}^n$, ellipsoid suy biến có phần trong topo thông thường bằng rỗng ($\operatorname{int} \mathcal{E} = \emptyset$). Tuy nhiên, chiều affine của nó bằng đúng $k$, và nó sở hữu một **nội tương đối** khác rỗng $\operatorname{relint} \mathcal{E} \ne \emptyset$ nằm trong không gian con affine $x_c + \operatorname{range}(A)$. Đây là một minh họa mẫu mực cho vai trò của nội tương đối đã khảo sát ở bài học trước.

## 4. Thể tích của ellipsoid và hàm Log-Determinant

Biểu diễn tham số $\mathcal{E} = x_c + A\,B(0, 1)$ mang lại một công thức giải tích đẹp mắt để tính thể tích. Phép biến đổi tuyến tính $A$ làm thay đổi thể tích của mọi tập hợp theo một tỷ số bằng $|\det A|$. Do đó, thể tích của ellipsoid $\mathcal{E}$ trong $\mathbb{R}^n$ được tính theo công thức:

$$
\begin{aligned}
\operatorname{vol}(\mathcal{E}) &= |\det A| \cdot \operatorname{vol}(B(0, 1)) \\
&= \sqrt{\det(AA^T)} \cdot \operatorname{vol}(B(0, 1)) \\
&= \sqrt{\det P} \cdot \operatorname{vol}(B(0, 1)) \\
&= \left(\prod_{i=1}^n \lambda_i\right)^{1/2} \cdot \operatorname{vol}(B(0, 1)) = \sqrt{\lambda_1 \lambda_2 \dots \lambda_n} \cdot \operatorname{vol}(B(0, 1)) .
\end{aligned}
$$

Trong mặt phẳng $\mathbb{R}^2$, thể tích chính là diện tích hình ellipse: $S = \pi \sqrt{\lambda_1 \lambda_2} = \pi a b$. Với ví dụ ở mục 2, diện tích ellipse là $\pi \sqrt{8 \cdot 2} = 4\pi$.

Công thức trên chỉ ra rằng đại lượng $\det P$ phản ánh trực tiếp bình phương thể tích của ellipsoid. Để tối ưu hóa kích thước ellipsoid (chẳng hạn bài toán tìm ellipsoid bao có thể tích nhỏ nhất chứa một tập điểm cho trước, gọi là bài toán Loewner-John), người ta thường tối thiểu hóa hàm mục tiêu:

$$
\log \operatorname{vol}(\mathcal{E}) = \frac{1}{2} \log \det P + \text{const} .
$$

Hàm $\log \det P^{-1}$ hoặc $-\log \det P$ là một hàm lồi trên nón các ma trận xác định dương, tạo tiền đề cho các thuật toán tối ưu lồi hiệu quả trong hình học tính toán.

## 5. Ellipsoid trong phân phối Gauss và khoảng cách Mahalanobis

Hàm mật độ xác suất của phân phối chuẩn nhiều chiều $\mathcal{N}(\mu, \Sigma)$ với vector kỳ vọng $\mu \in \mathbb{R}^n$ và ma trận hiệp phương sai $\Sigma \succ 0$ có dạng:

$$
p(x) = \frac{1}{(2\pi)^{n/2} \sqrt{\det \Sigma}} \exp\left(-\frac{1}{2} (x - \mu)^T \Sigma^{-1} (x - \mu)\right) .
$$

Mật độ xác suất $p(x)$ nhận giá trị không đổi khi và chỉ khi đại lượng toàn phương ở số mũ nhận giá trị không đổi. Do đó, **các đường đồng mức mật độ của phân phối Gauss chính là các ellipsoid** có tâm tại $\mu$ và ma trận định hình tỷ lệ thuận với $\Sigma$:

$$
\mathcal{E}_c = \{x \in \mathbb{R}^n \mid (x - \mu)^T \Sigma^{-1} (x - \mu) \le c\} .
$$

Trục dài nhất của ellipsoid mật độ nằm dọc theo vector riêng ứng với trị riêng lớn nhất của $\Sigma$, đại diện cho phương có độ biến động (phương sai) lớn nhất của dữ liệu. Đây chính là nền tảng hình học của phương pháp phân tích thành phần chính (PCA).

Đại lượng xuất hiện trong số mũ được gọi là **khoảng cách Mahalanobis** từ điểm $x$ tới kỳ vọng $\mu$:

$$
d_M(x, \mu) = \sqrt{(x - \mu)^T \Sigma^{-1} (x - \mu)} .
$$

Khoảng cách Mahalanobis đo khoảng cách hình học đã được chuẩn hóa theo độ lệch chuẩn dọc theo từng phương. Xét trường hợp $\mu = 0$ và $\Sigma = \operatorname{diag}(4, 1)$: Điểm $(2, 1)$ có khoảng cách Euclid là $\sqrt{2^2 + 1^2} = \sqrt{5} \approx 2.24$, nhưng bình phương khoảng cách Mahalanobis chỉ là:

$$
d_M^2 = \frac{2^2}{4} + \frac{1^2}{1} = 1 + 1 = 2 .
$$

Dọc theo trục thứ nhất, độ lệch bằng 2 đúng bằng một độ lệch chuẩn ($\sigma_1 = \sqrt{4} = 2$), nên về mặt thống kê điểm này không hề nằm xa tâm như cảm nhận từ khoảng cách Euclid thuần túy.

## 6. Những câu hỏi để đào sâu

**Câu 1.** Tập hợp $\{x \in \mathbb{R}^2 \mid x^T M x \le 1\}$ với $M = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}$ có phải là một ellipsoid hay không? Tập này có lồi không?

<details><summary>Xem lời giải thích</summary>

Dạng toàn phương là $x^T M x = 2x_1 x_2 \le 1$, tương đương $x_1 x_2 \le \tfrac12$. Tập hợp này không bị chặn vì nó chứa toàn bộ hai trục tọa độ $x_1 = 0$ và $x_2 = 0$, do đó không phải là ellipsoid. Tập này cũng không lồi: Hai điểm $(1, \tfrac12)$ và $(\tfrac12, 1)$ đều thuộc tập vì tích tọa độ bằng $\tfrac12$, nhưng trung điểm của chúng là $(\tfrac34, \tfrac34)$ có tích tọa độ là $\tfrac{9}{16} > \tfrac12$, nằm ngoài tập. Ma trận $M$ có hai trị riêng là $1$ và $-1$, không xác định dương. Giả thiết $P \succ 0$ trong định nghĩa ellipsoid là điều kiện bắt buộc để bảo đảm tập hợp bị chặn và lồi.

</details>

**Câu 2.** Cho một ellipsoid trong $\mathbb{R}^2$ có các bán trục bằng $3$ và $1$. Nếu ta nhân ma trận $P$ với $4$, ellipsoid thay đổi ra sao? Nếu thay $P$ bằng $P^2$ thì hình dạng biến đổi thế nào?

<details><summary>Xem lời giải thích</summary>

Nhân ma trận $P$ với 4 làm mọi trị riêng tăng lên 4 lần, do đó các độ dài bán trục tăng lên $\sqrt{4} = 2$ lần: Ellipsoid phóng to gấp đôi mà vẫn giữ nguyên tỷ lệ hình học, bán trục mới là $6$ và $2$. Nếu thay $P$ bằng $P^2$, các trị riêng bị bình phương, từ $9$ và $1$ biến thành $81$ và $1$. Độ dài các bán trục mới trở thành $9$ và $1$. Tỷ số giữa bán trục lớn và bán trục nhỏ tăng từ $3$ lên $9$, làm hình dạng trở nên dẹt hơn rất nhiều. Tỷ số này liên quan mật thiết tới số điều kiện của ma trận, và các hàm mục tiêu có đường đồng mức ellipsoid càng dẹt sẽ khiến giải thuật hạ gradient hội tụ càng chậm.

</details>

**Câu 3.** Phần giao của hai ellipsoid có luôn là tập lồi không? Phần giao đó có nhất thiết là một ellipsoid không?

<details><summary>Xem lời giải thích</summary>

Phần giao của hai ellipsoid luôn là một tập lồi, bởi vì từng ellipsoid là tập lồi và phép giao bảo toàn tính lồi. Tuy nhiên, phần giao nói chung không phải là một ellipsoid. Giao của hai hình tròn bán kính bằng nhau có tâm lệch nhau tạo thành một hình dạng thấu kính có hai góc nhọn, trong khi đường biên của một ellipsoid luôn trơn và không có điểm gãy. Điều này cho thấy họ các ellipsoid không đóng kín đối với phép giao, và đó là lý do lý thuyết tối ưu hóa chọn làm việc với họ các tập lồi tổng quát thay vì chỉ giới hạn ở các ellipsoid.

</details>

**Câu 4.** Vì sao nhiều ma trận $A$ khác nhau có thể cùng biểu diễn một ellipsoid $\{x_c + Au \mid \|u\|_2 \le 1\}$, trong khi ma trận $P$ ở dạng nghịch đảo lại được xác định duy nhất?

<details><summary>Xem lời giải thích</summary>

Quả cầu đơn vị $\|u\|_2 \le 1$ bất biến qua mọi phép quay và phép phản xạ trực giao, nên hai ma trận $A$ và $A U$ (với $U$ trực giao) quét qua cùng một miền điểm trong không gian. Ngược lại, dạng nghịch đảo $(x - x_c)^T P^{-1} (x - x_c) \le 1$ mô tả tập hợp thông qua đường đồng mức mức 1 của một dạng toàn phương xác định dương. Một ellipsoid không suy biến xác định duy nhất phương trình toàn phương chuẩn tắc của nó, kéo theo ma trận nghịch đảo $P^{-1}$ và ma trận $P$ là duy nhất. Mối quan hệ $P = AA^T$ đã triệt tiêu hoàn toàn yếu tố góc xoay trực giao $U$, tương tự như trong thống kê khi nhiều phép biến đổi căn bậc hai ma trận đều sinh ra cùng một phân phối Gauss chuẩn tắc.

</details>

## 7. Bài tập tự luyện

::: exercise 1. Xác định hình dạng ellipsoid từ ma trận đường chéo
Cho ellipsoid tâm $x_c = (2, 1)$ với ma trận $P = \operatorname{diag}(9, 4)$:

$$
\mathcal{E} = \{x \in \mathbb{R}^2 \mid (x - x_c)^T P^{-1} (x - x_c) \le 1\} .
$$

Tìm độ dài các bán trục, viết lại phương trình dưới dạng tọa độ vô hướng, và xác định điểm có hoành độ lớn nhất của ellipsoid.
:::

::: solution
Vì ma trận $P$ là ma trận đường chéo, các vector riêng trùng với các trục tọa độ chính. Hai trị riêng là $\lambda_1 = 9$ và $\lambda_2 = 4$, cho bán trục lớn $a = \sqrt{9} = 3$ theo phương ngang và bán trục nhỏ $b = \sqrt{4} = 2$ theo phương đứng.

Phương trình vô hướng của ellipsoid là:

$$
\frac{(x_1 - 2)^2}{9} + \frac{(x_2 - 1)^2}{4} \le 1 .
$$

Điểm có hoành độ $x_1$ lớn nhất đạt được khi thành phần tung độ triệt tiêu, tức $x_2 = 1$. Khi đó $(x_1 - 2)^2 \le 9 \implies x_1 \le 2 + 3 = 5$. Tọa độ điểm cần tìm là $(5, 1)$.
:::

::: exercise 2. Chuyển đổi giữa dạng ảnh và dạng ràng buộc
Cho ellipsoid $\mathcal{E} = \{(1, 0) + Au \mid \|u\|_2 \le 1\}$ với ma trận:

$$
A = \begin{bmatrix} 2 & 0 \\ 1 & 1 \end{bmatrix} .
$$

Tìm ma trận $P$ ở dạng ràng buộc và kiểm tra xem điểm $x = (3, 1)$ có nằm trên biên của ellipsoid hay không.
:::

::: hint
Tính ma trận tích $P = AA^T$. Tìm vector $u$ thỏa mãn phương trình $Au = x - x_c$ và kiểm tra độ dài của nó.
:::

::: solution
Ma trận định hình là:

$$
P = AA^T = \begin{bmatrix} 2 & 0 \\ 1 & 1 \end{bmatrix} \begin{bmatrix} 2 & 1 \\ 0 & 1 \end{bmatrix} = \begin{bmatrix} 4 & 2 \\ 2 & 2 \end{bmatrix} .
$$

Định thức của $P$ là $\det P = 4 \cdot 2 - 2^2 = 4 > 0$. Với điểm $x = (3, 1)$, vector sai lệch từ tâm là $x - x_c = (3, 1) - (1, 0) = (2, 1)$. Hệ phương trình $Au = x - x_c$ tương đương:

$$
\begin{bmatrix} 2 & 0 \\ 1 & 1 \end{bmatrix} \begin{bmatrix} u_1 \\ u_2 \end{bmatrix} = \begin{bmatrix} 2 \\ 1 \end{bmatrix} \implies 2u_1 = 2 \implies u_1 = 1,\quad 1 + u_2 = 1 \implies u_2 = 0 .
$$

Vector nghiệm là $u = (1, 0)$, có chuẩn $\|u\|_2 = \sqrt{1^2 + 0^2} = 1$, do đó điểm $x$ nằm chính xác trên biên của ellipsoid.

Đối chiếu lại qua dạng nghịch đảo: Nghịch đảo của ma trận $P$ là $P^{-1} = \tfrac{1}{4}\begin{bmatrix} 2 & -2 \\ -2 & 4 \end{bmatrix}$. Giá trị dạng toàn phương:

$$
\begin{bmatrix} 2 & 1 \end{bmatrix} \left(\frac{1}{4}\begin{bmatrix} 2 & -2 \\ -2 & 4 \end{bmatrix}\right) \begin{bmatrix} 2 \\ 1 \end{bmatrix} = \frac{1}{4}(8 - 4 - 4 + 4) = 1 ,
$$

hoàn toàn khớp với kết quả kiểm tra tham số.
:::

::: exercise 3. Tính diện tích ellipse và so sánh khoảng cách Mahalanobis
Cho ma trận hiệp phương sai $\Sigma = \begin{bmatrix} 5 & 3 \\ 3 & 5 \end{bmatrix}$ và vector kỳ vọng $\mu = 0$. Tính diện tích của hình ellipse $\{x \in \mathbb{R}^2 \mid x^T \Sigma^{-1} x \le 1\}$, đồng thời tính khoảng cách Mahalanobis từ gốc tọa độ tới hai điểm $x_A = (2, 2)$ và $x_B = (1, -1)$. Điểm nào nằm xa gốc tọa độ hơn theo quan điểm thống kê?
:::

::: solution
Ma trận $\Sigma$ có hai trị riêng là $\lambda_1 = 8$ và $\lambda_2 = 2$. Diện tích của hình ellipse là:

$$
S = \pi \sqrt{\lambda_1 \lambda_2} = \pi \sqrt{8 \cdot 2} = 4\pi .
$$

Ma trận nghịch đảo là $\Sigma^{-1} = \tfrac{1}{16}\begin{bmatrix} 5 & -3 \\ -3 & 5 \end{bmatrix}$.
- Với điểm $x_A = (2, 2)$:
  $$
  d_M^2(x_A, 0) = \frac{1}{16} \begin{bmatrix} 2 & 2 \end{bmatrix} \begin{bmatrix} 5 & -3 \\ -3 & 5 \end{bmatrix} \begin{bmatrix} 2 \\ 2 \end{bmatrix} = \frac{1}{16}(20 - 12 - 12 + 20) = 1 \implies d_M(x_A, 0) = 1 .
  $$
- Với điểm $x_B = (1, -1)$:
  $$
  d_M^2(x_B, 0) = \frac{1}{16} \begin{bmatrix} 1 & -1 \end{bmatrix} \begin{bmatrix} 5 & -3 \\ -3 & 5 \end{bmatrix} \begin{bmatrix} 1 \\ -1 \end{bmatrix} = \frac{1}{16}(5 + 3 + 3 + 5) = 1 \implies d_M(x_B, 0) = 1 .
  $$

Khoảng cách Euclid thông thường từ gốc tới hai điểm lần lượt là $\|x_A\|_2 = \sqrt{2^2 + 2^2} = 2\sqrt{2} \approx 2.83$ và $\|x_B\|_2 = \sqrt{1^2 + (-1)^2} = \sqrt{2} \approx 1.41$. Tuy nhiên, xét theo khoảng cách Mahalanobis, hai điểm này có khoảng cách hoàn toàn bằng nhau (đều bằng 1), vì điểm $x_A$ nằm dọc theo phương có độ phân tán lớn ($\sigma_1 = \sqrt{8}$), trong khi điểm $x_B$ nằm dọc theo phương có độ phân tán nhỏ ($\sigma_2 = \sqrt{2}$).
:::

## Tóm tắt

Quả cầu Euclid đóng sở hữu hai cách biểu diễn bổ trợ: Dạng bất đẳng thức khoảng cách dùng để kiểm tra ràng buộc và dạng tham số hóa dùng để sinh điểm. Tính lồi của quả cầu được thiết lập nhờ bất đẳng thức tam giác và tính thuần nhất tuyệt đối của chuẩn.

Ellipsoid xác định bởi ma trận đối xứng xác định dương $P \succ 0$ có các bán trục định hướng theo các vector riêng của $P$ với độ dài bằng căn bậc hai của các trị riêng tương ứng. Về mặt biến đổi hình học, ellipsoid là ảnh affine của quả cầu đơn vị qua ma trận $A$ thỏa mãn $P = AA^T$. Khi ma trận $A$ suy biến với hạng $k < n$, ta thu được ellipsoid suy biến có chiều affine bằng $k$ và sở hữu nội tương đối khác rỗng. Thể tích ellipsoid tỷ lệ với căn bậc hai định thức $\sqrt{\det P}$, tạo nền tảng cho việc tối ưu hàm $\log\det$. Trong thống kê và học máy, các đường đồng mức mật độ của phân phối Gauss là các ellipsoid, và khoảng cách Mahalanobis cung cấp thước đo khoảng cách đã chuẩn hóa theo cấu trúc hiệp phương sai của dữ liệu.

## Tài liệu tham khảo

- Stephen Boyd, Lieven Vandenberghe, *Convex Optimization*, Cambridge University Press.
