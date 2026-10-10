---
course: toan-cho-ai
lecture: bai-01-nhap-mon-toi-uu
topic: hai-lop-bai-toan-kinh-dien
section: topic
title: "Bình phương tối thiểu và quy hoạch tuyến tính"
description: "Hai lớp bài toán giải được một cách đáng tin cậy: Bình phương tối thiểu với hệ phương trình chuẩn và hình học phép chiếu, quy hoạch tuyến tính với hình học đa diện, chứng nhận tối ưu và biến phụ, rồi tối ưu lồi như sự tổng quát hóa của cả hai."
---

Ở chủ đề trước, ta đã viết được một bài toán tối ưu cho đúng. Câu hỏi tiếp theo là: Viết xong rồi thì giải bằng cách nào? Sách trả lời thẳng thắn rằng bài toán tối ưu tổng quát **khó giải một cách đáng ngạc nhiên**, kể cả khi mọi hàm đều trơn như đa thức. Những phương pháp tổng quát phải chấp nhận một sự đánh đổi, hoặc chạy rất lâu, hoặc có thể không tìm ra nghiệm.

Thế nhưng có vài ngoại lệ quan trọng: Những lớp bài toán mà ta có thuật toán giải được cả bài lớn, nhanh và gần như chắc chắn. Trang này giới thiệu hai ngoại lệ nổi tiếng nhất là **bình phương tối thiểu** và **quy hoạch tuyến tính**, rồi chỉ ra rằng cả hai đều là trường hợp riêng của một lớp rộng hơn: **Tối ưu lồi**. Hiểu được điều gì khiến hai lớp này dễ là cách tốt nhất để hiểu vì sao cả môn học xoay quanh tính lồi.

Bạn cần biết phép nhân ma trận, gradient của hàm nhiều biến và dạng $\|Ax - b\|_2^2$ đã gặp ở Lecture 00.

## 1. Bình phương tối thiểu

### 1.1 Bài toán và hệ phương trình chuẩn

Bài toán **bình phương tối thiểu** (least squares) không có ràng buộc, và hàm mục tiêu là tổng bình phương của các biểu thức dạng $a_i^T x - b_i$:

$$
\text{minimize}\quad f_0(x) = \|Ax - b\|_2^2 = \sum_{i=1}^{k} (a_i^T x - b_i)^2 .
$$

Ở đây $A \in \mathbb{R}^{k \times n}$ có các hàng $a_1^T, \ldots, a_k^T$, thường với $k \ge n$, và $x \in \mathbb{R}^n$ là biến. Trong ngữ cảnh khớp dữ liệu, mỗi hàng của $A$ là một quan sát, $a_i^T x$ là giá trị mô hình dự đoán cho quan sát thứ $i$, và $a_i^T x - b_i$ là phần dư của quan sát đó. Bình phương làm cho sai số dương và sai số âm không triệt tiêu nhau, đồng thời phạt sai số lớn nặng hơn hẳn sai số nhỏ.

Để tìm nghiệm, ta đặt gradient bằng 0. Khai triển $f_0(x) = x^T A^T A x - 2 b^T A x + b^T b$, gradient là $\nabla f_0(x) = 2A^T A x - 2A^T b$, nên điều kiện $\nabla f_0(x) = 0$ trở thành

$$
A^T A\, x = A^T b .
$$

Hệ này được gọi là **hệ phương trình chuẩn**. Khi các cột của $A$ độc lập tuyến tính, ma trận $A^T A$ khả nghịch và nghiệm duy nhất là $x^\star = (A^T A)^{-1} A^T b$. Công thức đóng này là thứ hiếm có trong tối ưu, nhưng ta chưa nên dùng nó một cách máy móc vì hai lẽ. Thứ nhất, đặt gradient bằng 0 chỉ tìm ra điểm dừng, và ta còn phải giải thích vì sao điểm dừng này là cực tiểu toàn cục. Thứ hai, khi lập trình, người ta giải hệ bằng các phân tích ma trận như QR thay vì tính nghịch đảo tường minh, vì cách sau kém ổn định về số.

Lý do điểm dừng là cực tiểu toàn cục sẽ được làm rõ ở các chủ đề về hàm lồi. Ta có thể thấy trước ý chính: Hessian của $f_0$ là $2A^T A$, và với mọi vector $v$, $v^T(2A^T A)v = 2\|Av\|_2^2 \ge 0$. Một hàm bậc hai có Hessian nửa xác định dương thì "cong lên" theo mọi hướng, nên điểm dừng của nó không thể là đỉnh đồi hay điểm yên ngựa.

### 1.2 Bức tranh hình học: Phép chiếu vuông góc

Công thức $A^T A x = A^T b$ có một ý nghĩa hình học rất đẹp, và nó giải thích vì sao bình phương tối thiểu lại "tự nhiên" đến thế. Khi $x$ chạy khắp $\mathbb{R}^n$, vector dự đoán $Ax$ chạy khắp **không gian cột** của $A$, tức tập $\{Ax : x \in \mathbb{R}^n\}$. Đó là một không gian con của $\mathbb{R}^k$. Vector dữ liệu $b$ nói chung nằm ngoài không gian ấy, vì không có mô hình nào khớp hoàn hảo dữ liệu thật.

Cực tiểu $\|Ax - b\|_2$ nghĩa là tìm điểm của không gian cột **gần $b$ nhất** theo khoảng cách Euclid. Hình học phổ thông cho ta câu trả lời: Hạ đường vuông góc. Điểm gần nhất là hình chiếu vuông góc của $b$, và phần dư $Ax^\star - b$ vuông góc với cả không gian cột, tức vuông góc với từng cột của $A$. Viết điều kiện vuông góc ấy cho từng cột, ta được đúng $A^T(Ax^\star - b) = 0$. Như vậy hệ phương trình chuẩn không phải một mẹo đại số, nó là điều kiện "phần dư vuông góc với mọi hướng mà mô hình có thể đi".

Từ góc nhìn này còn rút ra một điều tinh tế. Vector dự đoán tốt nhất $Ax^\star$, là hình chiếu của $b$, luôn duy nhất. Nhưng bộ tham số $x^\star$ tạo ra nó chỉ duy nhất khi các cột của $A$ độc lập tuyến tính. Nếu có hai đặc trưng trùng nhau, chẳng hạn nhiệt độ đo bằng độ C và cùng nhiệt độ đó đổi sang độ F, thì có vô số cách chia trọng số giữa chúng mà vẫn cho cùng một dự đoán. Tập các nghiệm khi đó là một tập affine, đúng như chủ đề "Đường thẳng, đoạn thẳng và tập affine" đã mô tả.

::: example Khớp một đường thẳng qua ba điểm
Dữ liệu tự đặt gồm ba cặp $(t_i, y_i) = (0, 1), (1, 2), (2, 4)$. Mô hình $y = at + c$ có hai tham số $x = (a, c)$, nên

$$
A = \begin{bmatrix} 0 & 1 \\ 1 & 1 \\ 2 & 1 \end{bmatrix}, \qquad b = \begin{bmatrix} 1 \\ 2 \\ 4 \end{bmatrix}, \qquad A^T A = \begin{bmatrix} 5 & 3 \\ 3 & 3 \end{bmatrix}, \qquad A^T b = \begin{bmatrix} 10 \\ 7 \end{bmatrix}.
$$

Hệ chuẩn là $5a + 3c = 10$ và $3a + 3c = 7$. Lấy phương trình đầu trừ phương trình sau được $2a = 3$, nên $a^\star = \tfrac32$ và $c^\star = \tfrac56$. Vector dự đoán là $Ax^\star = (\tfrac56, \tfrac73, \tfrac{23}{6})$ và phần dư là $r = Ax^\star - b = (-\tfrac16, \tfrac13, -\tfrac16)$.

Kiểm tra điều kiện vuông góc: Tích của $r$ với cột thứ nhất là $0\cdot(-\tfrac16) + 1\cdot\tfrac13 + 2\cdot(-\tfrac16) = 0$, với cột thứ hai là $-\tfrac16 + \tfrac13 - \tfrac16 = 0$. Tổng bình phương phần dư là $\tfrac1{36} + \tfrac19 + \tfrac1{36} = \tfrac16$. Không đường thẳng nào cho tổng nhỏ hơn.
:::

### 1.3 Hai biến thể thường gặp

Sách nêu hai kỹ thuật làm bình phương tối thiểu linh hoạt hơn mà vẫn giữ được bản chất "giải được". Thứ nhất là **bình phương tối thiểu có trọng số**, cực tiểu $\sum_{i} w_i (a_i^T x - b_i)^2$ với các trọng số $w_i > 0$. Trọng số lớn nghĩa là ta quan tâm nhiều hơn tới sai số của quan sát đó, chẳng hạn vì quan sát ấy được đo chính xác hơn. Thứ hai là **điều chuẩn** (regularization), cộng thêm vào hàm mục tiêu một số hạng phạt độ lớn của tham số:

$$
\sum_{i=1}^{k} (a_i^T x - b_i)^2 + \rho \sum_{j=1}^{n} x_j^2, \qquad \rho > 0 .
$$

Số hạng phạt giữ cho $x$ không quá lớn, và tham số $\rho$ do người dùng chọn để cân bằng giữa hai mong muốn: Khớp dữ liệu và giữ tham số nhỏ. Với $\rho > 0$, hệ chuẩn trở thành $(A^T A + \rho I)x = A^T b$, và ma trận $A^T A + \rho I$ luôn khả nghịch. Vì vậy nghiệm luôn duy nhất, kể cả khi các cột của $A$ phụ thuộc tuyến tính. Trong học máy, cách làm này được gọi là hồi quy ridge.

Bình phương tối thiểu còn có một cách hiểu thống kê mà Lecture 00 đã trình bày: Nếu dữ liệu được tạo ra bởi mô hình tuyến tính cộng nhiễu Gauss độc lập cùng phương sai, thì nghiệm bình phương tối thiểu chính là ước lượng hợp lý cực đại. Điều chuẩn cũng có cách hiểu tương tự, khi ta gán cho tham số một phân phối tiên nghiệm.

Nhận ra một bài toán bình phương tối thiểu khá dễ: Chỉ cần thấy hàm mục tiêu là một hàm bậc hai, rồi kiểm tra dạng toàn phương đi kèm nửa xác định dương. Sách gọi việc giải bình phương tối thiểu là một **công nghệ trưởng thành**, theo nghĩa người dùng không cần biết chi tiết thuật toán vẫn dùng được một cách đáng tin cậy. Chi phí tính toán xấp xỉ tỉ lệ với $n^2 k$, với một hằng số đã biết.

## 2. Quy hoạch tuyến tính

### 2.1 Bài toán

Lớp thứ hai là **quy hoạch tuyến tính** (linear program, viết tắt LP), trong đó cả hàm mục tiêu và mọi hàm ràng buộc đều tuyến tính:

$$
\begin{aligned}
\text{minimize}\quad & c^T x\\
\text{subject to}\quad & a_i^T x \le b_i, \quad i = 1, \ldots, m .
\end{aligned}
$$

Các vector $c, a_1, \ldots, a_m \in \mathbb{R}^n$ và các số $b_1, \ldots, b_m$ là dữ liệu. Khác với bình phương tối thiểu, LP **không có công thức nghiệm đóng**. Bù lại, có những thuật toán rất hiệu quả: Phương pháp đơn hình của Dantzig và các phương pháp điểm trong mà ta sẽ gặp sau. Sách mô tả độ phức tạp thực tế vào khoảng $n^2 m$ phép tính khi $m \ge n$, với hằng số kém xác định hơn so với bình phương tối thiểu. LP cũng được xem là một công nghệ trưởng thành.

### 2.2 Bức tranh hình học: Đẩy một đường mức qua một đa giác

Mỗi ràng buộc $a_i^T x \le b_i$ cắt không gian làm đôi và giữ lại một nửa. Miền khả thi là giao của các nửa đó, một **đa diện**, trong mặt phẳng là một đa giác lồi. Hàm mục tiêu $c^T x$ có các đường mức $c^T x = \text{hằng số}$ là những đường thẳng song song. Giải LP trong mặt phẳng giống như đẩy một chiếc thước kẻ theo hướng làm giá trị tốt lên, cho tới khi thước chỉ còn chạm đa giác ở mép. Chỗ chạm cuối cùng thường là một đỉnh, và cũng có thể là cả một cạnh nếu thước song song với cạnh ấy.

Mô phỏng dưới đây cho bạn đổi hệ số của mục tiêu $\max\ c_1 x + c_2 y$ trên đa giác $\{x + y \le 4,\ x \le 2,\ x \ge 0,\ y \ge 0\}$. Hãy tìm một cặp hệ số khiến nghiệm không duy nhất.

<MathLab type="lp" />

Nhận xét "nghiệm nằm ở một đỉnh" đúng cho những đa diện có đỉnh và khi giá trị tối ưu hữu hạn. Nó là nền tảng của phương pháp đơn hình, vốn đi từ đỉnh này sang đỉnh kề tốt hơn. Lecture 07 sẽ trở lại với câu hỏi khi nào điều đó được bảo đảm.

### 2.3 Chứng nhận một nghiệm LP mà không cần thử mọi điểm

Xét bài toán cực đại $5x_1 + 4x_2$ với $x_1 + x_2 \le 6$, $2x_1 + x_2 \le 9$ và $x_1, x_2 \ge 0$, dữ liệu tự đặt. Đa giác khả thi có bốn đỉnh $(0, 0)$, $(4.5, 0)$, $(3, 3)$ và $(0, 6)$, cho các giá trị 0, 22.5, 27 và 24, nên điểm $(3, 3)$ cho giá trị lớn nhất trong các đỉnh. Nhưng làm sao **chứng minh** không điểm khả thi nào cho giá trị lớn hơn 27, mà không phải dựa vào nhận xét về đỉnh?

Ý tưởng là cộng các ràng buộc lại với những hệ số không âm. Nhân ràng buộc thứ nhất với 3 và ràng buộc thứ hai với 1 rồi cộng lại:

$$
3\,(x_1 + x_2) + 1 \cdot (2x_1 + x_2) = 5x_1 + 4x_2 \le 3 \cdot 6 + 1 \cdot 9 = 27 .
$$

Hệ số được chọn sao cho vế trái đúng bằng hàm mục tiêu. Hai hệ số phải không âm, vì nhân một bất đẳng thức với số âm sẽ đảo chiều nó. Vậy với **mọi** điểm khả thi, giá trị mục tiêu không vượt quá 27, và điểm $(3, 3)$ đạt đúng 27, nên nó tối ưu. Cặp hệ số $(3, 1)$ là một **chứng nhận tối ưu**: Ai cũng kiểm tra được nó chỉ bằng vài phép nhân.

Cách tìm cặp hệ số ấy cũng là một LP, được gọi là bài toán đối ngẫu. Đây là hạt mầm của lý thuyết đối ngẫu Lagrange ở Lecture 03, nơi ý tưởng "cộng các ràng buộc với trọng số không âm để được một cận" được mở rộng cho mọi bài toán lồi.

### 2.4 Biến một bài toán không trơn thành LP

Có những bài toán thoạt nhìn không phải LP nhưng biến đổi được thành LP. Ví dụ tiêu biểu trong sách là **xấp xỉ Chebyshev**:

$$
\text{minimize}\quad \max_{i = 1, \ldots, k} |a_i^T x - b_i| .
$$

Hàm mục tiêu đo phần dư **lớn nhất** thay vì tổng bình phương phần dư, và nó không khả vi ở những điểm mà hai phần dư lớn nhất bằng nhau. Mẹo là thêm một biến $t$ đóng vai trò cận trên cho mọi phần dư:

$$
\begin{aligned}
\text{minimize}\quad & t\\
\text{subject to}\quad & a_i^T x - b_i \le t, \quad -(a_i^T x - b_i) \le t, \quad i = 1, \ldots, k .
\end{aligned}
$$

Hai bất đẳng thức cuối cùng nói $|a_i^T x - b_i| \le t$ với mọi $i$, tức $t$ không nhỏ hơn phần dư lớn nhất. Khi cực tiểu hóa, $t$ bị đẩy xuống đúng bằng phần dư lớn nhất, nên hai bài toán có cùng nghiệm $x$. Bài toán mới tuyến tính theo các biến $(x, t)$. Cùng một mẹo áp dụng cho tổng trị tuyệt đối $\sum_i |a_i^T x - b_i|$, với mỗi phần dư một biến phụ riêng. Sách nhận xét rằng người đã quen LP nhận ra ngay các biến đổi này, còn người chưa quen thì khó đoán được một hàm không khả vi lại giải được dễ dàng như vậy.

Ba tiêu chí đo sai số cho ba nghiệm khác nhau, và sự khác nhau đó không phải chuyện kỹ thuật mà là chuyện ta muốn gì. Mô phỏng sau đặt ba đường thẳng tối ưu cạnh nhau trên cùng dữ liệu.

<FitLab />

Thử kéo một điểm thật xa khỏi các điểm còn lại. Đường bình phương tối thiểu bị kéo theo rõ rệt, vì bình phương làm một sai số lớn trở nên rất lớn. Đường ℓ₁ gần như không đổi: Nó chịu được vài quan sát bất thường. Còn đường ℓ∞ lo cho trường hợp xấu nhất nên lại bị điểm bất thường chi phối mạnh nhất. Chọn tiêu chí là chọn mô hình, và lựa chọn đó phải đến từ hiểu biết về dữ liệu, không phải từ việc tiêu chí nào dễ tính hơn.

## 3. Tối ưu lồi: Điểm chung của hai lớp bài toán

Bây giờ ta có thể nêu lớp bài toán là chủ đề của cả môn học. Một **bài toán tối ưu lồi** có dạng

$$
\begin{aligned}
\text{minimize}\quad & f_0(x)\\
\text{subject to}\quad & f_i(x) \le b_i, \quad i = 1, \ldots, m,
\end{aligned}
$$

trong đó các hàm $f_0, \ldots, f_m$ đều **lồi**, nghĩa là với mọi $x, y$ và mọi $\alpha, \beta \ge 0$ có $\alpha + \beta = 1$,

$$
f_i(\alpha x + \beta y) \le \alpha f_i(x) + \beta f_i(y).
$$

Hãy so sánh với điều kiện tuyến tính $f_i(\alpha x + \beta y) = \alpha f_i(x) + \beta f_i(y)$, vốn phải đúng với **mọi** $\alpha, \beta \in \mathbb{R}$. Điều kiện lồi yếu hơn ở hai chỗ: Dấu bằng được thay bằng dấu $\le$, và chỉ cần đúng với những cặp $\alpha, \beta$ không âm có tổng bằng 1. Vì vậy mọi hàm tuyến tính đều lồi, mọi LP đều là bài toán tối ưu lồi, và tối ưu lồi là một sự tổng quát hóa của quy hoạch tuyến tính. Bình phương tối thiểu cũng là bài toán lồi, vì hàm $\|Ax - b\|_2^2$ thỏa bất đẳng thức trên (chủ đề về hàm lồi sẽ chứng minh điều này).

Tối ưu lồi nói chung không có công thức nghiệm đóng, nhưng có những phương pháp rất hiệu quả. Trong thực tế tính toán, các phương pháp điểm trong thường giải xong trong khoảng 10 đến 100 bước lặp, mỗi bước tốn cỡ $\max\{n^3, n^2 m, F\}$ phép tính, với $F$ là chi phí tính đạo hàm bậc nhất và bậc hai của các hàm. Ngày nay, tối ưu lồi tổng quát đã phát triển vượt bậc và trở thành công nghệ cốt lõi trong kỹ nghệ tính toán khoa học hiện đại.

Một triết lý sâu sắc trong tối ưu hiện đại: Nếu bạn đưa được một bài toán thực tế về dạng bài toán tối ưu lồi, thì gần như bạn đã giải quyết xong nó. Cái khó của tối ưu lồi vì vậy không nằm ở khâu giải, mà nằm ở khâu **nhận ra** và **biến đổi** bài toán về dạng lồi. Nhận ra một bài toán bình phương tối thiểu thì dễ, nhận ra một hàm lồi thì khó hơn nhiều, và số mẹo biến đổi cũng nhiều hơn LP. Phần lớn chương này được dành để luyện đúng kỹ năng nhận diện ấy.

## 4. Khi bài toán không lồi

Bài toán có hàm mục tiêu hoặc hàm ràng buộc không tuyến tính mà cũng không biết có lồi hay không được gọi chung là **tối ưu phi tuyến**. Với lớp tổng quát này, khoa học tính toán hiện nay chưa có một phương pháp vạn năng nào giải tối ưu trong thời gian đa thức. Người ta đi theo hai hướng, mỗi hướng một sự đánh đổi.

**Tối ưu cục bộ** từ bỏ mục tiêu tìm nghiệm toàn cục và chỉ tìm một điểm tối ưu cục bộ. Các phương pháp này nhanh, áp dụng được cho bài toán rất lớn và chỉ cần các hàm khả vi. Đổi lại, chúng cần một điểm xuất phát, kết quả có thể phụ thuộc mạnh vào điểm xuất phát đó, chúng không cho biết điểm tìm được còn cách nghiệm toàn cục bao xa, và thường nhạy với các tham số của thuật toán. Người ta thường ví tối ưu cục bộ là sự kết hợp tinh tế giữa nghệ thuật mò mẫm và kỹ thuật tính toán. Huấn luyện mạng nơ-ron sâu thuộc đúng loại này: Hàm mất mát thường không lồi theo các trọng số, và người ta chạy các biến thể của phương pháp gradient từ một điểm khởi tạo ngẫu nhiên.

**Tối ưu toàn cục** tìm nghiệm toàn cục thật sự, nhưng đánh đổi bằng thời gian: Trong trường hợp xấu nhất, chi phí tăng theo hàm mũ của số biến và số ràng buộc. Nó được dùng khi số biến nhỏ và việc chắc chắn có nghiệm tốt nhất đáng giá, chẳng hạn khi cần chứng nhận một hệ thống quan trọng an toàn trong trường hợp xấu nhất.

Sách chỉ ra một sự đảo vai thú vị giữa hai thế giới. Với tối ưu cục bộ, lập bài toán thì dễ, cái khó là giải. Với tối ưu lồi thì ngược lại: Lập được bài toán dạng lồi mới là cái khó, còn giải thì gần như đã là công nghệ. Tối ưu lồi cũng giúp ích cho cả bài toán không lồi, chẳng hạn để tìm điểm khởi tạo tốt hay để tính cận cho giá trị tối ưu.

## 5. Những câu hỏi để đào sâu

**Câu 1.** Trong ví dụ ba điểm ở mục 1.2, nếu thêm một điểm thứ tư $(1, 2)$ trùng với điểm thứ hai, nghiệm $a^\star, c^\star$ có thay đổi không? Hãy dự đoán trước, rồi giải thích bằng ngôn ngữ trọng số.

<details><summary>Xem lời giải thích</summary>

Có thay đổi. Thêm một bản sao của $(1,2)$ tương đương với việc nhân đôi trọng số của quan sát đó trong bình phương tối thiểu có trọng số. Đường thẳng mới sẽ bị kéo về phía $(1, 2)$. Cụ thể, $A^T A = \begin{bmatrix} 6 & 4 \\ 4 & 4 \end{bmatrix}$ và $A^T b = (12, 9)$, cho $a^\star = \tfrac32$ và $c^\star = \tfrac34$. Độ dốc không đổi (một sự trùng hợp của dữ liệu này) nhưng hệ số chặn giảm. Bài học là dữ liệu trùng lặp không "vô hại": Nó âm thầm thay đổi trọng số của bài toán.

</details>

**Câu 2.** Quy hoạch tuyến tính không có công thức nghiệm như bình phương tối thiểu. Điều đó có nghĩa là nó khó giải hơn không? Một bài toán có công thức nghiệm đóng có nhất thiết dễ giải hơn trên máy tính không?

<details><summary>Xem lời giải thích</summary>

Không nhất thiết. Công thức $(A^T A)^{-1} A^T b$ vẫn phải được tính bằng một thuật toán, với chi phí cỡ $n^2 k$. LP không có công thức nhưng có thuật toán giải đáng tin cậy với chi phí thực tế cỡ $n^2 m$. Điều quyết định độ khó trong thực tế là có thuật toán hiệu quả, đáng tin cậy hay không, chứ không phải có công thức hay không. Nhiều bài toán có "công thức" nhưng công thức đòi tính một số cực lớn hoặc kém ổn định số, còn nhiều bài toán không có công thức lại được giải rất tốt.

</details>

**Câu 3.** Trong mẹo biến phụ của xấp xỉ Chebyshev, điều gì xảy ra nếu ta vô tình viết bài toán thành cực đại $t$ thay vì cực tiểu $t$? Mẹo "biến phụ làm cận trên" có dùng được cho bài toán cực đại $\max_i |a_i^T x - b_i|$ không?

<details><summary>Xem lời giải thích</summary>

Nếu cực đại $t$ với các ràng buộc $|a_i^T x - b_i| \le t$, thì $t$ có thể tăng vô hạn, bài toán không bị chặn trên và vô nghĩa. Mẹo chỉ đúng vì khi cực tiểu, $t$ bị ép sát xuống phần dư lớn nhất. Còn cực đại $\max_i |a_i^T x - b_i|$ là cực đại một hàm lồi, và ràng buộc "t nhỏ hơn hoặc bằng phần dư lớn nhất" không viết được bằng các bất đẳng thức tuyến tính theo hướng đúng. Bài toán đó nói chung khó, và nó không lồi. Mẹo biến phụ chỉ dùng được khi chiều tối ưu "ép" biến phụ về phía ràng buộc.

</details>

**Câu 4.** Trong chứng nhận tối ưu ở mục 2.3, vì sao các hệ số nhân với ràng buộc phải không âm, còn hệ số nhân với một ràng buộc đẳng thức (nếu có) thì được phép âm?

<details><summary>Xem lời giải thích</summary>

Nhân hai vế của một bất đẳng thức $g(x) \le b$ với số $\lambda < 0$ làm đảo chiều thành $\lambda g(x) \ge \lambda b$, nên không cộng được với các bất đẳng thức khác để ra một cận trên. Với số $\lambda \ge 0$ thì chiều được giữ nguyên. Còn một đẳng thức $h(x) = d$ nhân với số nào cũng vẫn là đẳng thức, nên hệ số của nó không bị ràng buộc dấu. Quy tắc dấu này sẽ xuất hiện lại y hệt trong Lagrangian ở Lecture 03: Nhân tử của bất đẳng thức phải không âm, nhân tử của đẳng thức thì tự do về dấu.

</details>

## 6. Bài tập tự luyện

::: exercise 1. Bình phương tối thiểu bằng tay
Khớp mô hình hằng số $y = c$ với bốn số liệu $1, 3, 4, 12$ theo tiêu chí bình phương tối thiểu. Viết $A$ và $b$, giải hệ chuẩn, rồi giải thích vì sao nghiệm là trung bình cộng của dữ liệu.
:::

::: solution
Mô hình chỉ có một tham số, nên $A = (1, 1, 1, 1)^T$ và $b = (1, 3, 4, 12)$. Hệ chuẩn là $A^T A\, c = A^T b$, tức $4c = 20$, nên $c^\star = 5$. Tổng quát, với $k$ số liệu, hệ chuẩn là $k c = \sum_i b_i$, cho $c^\star = \tfrac1k \sum_i b_i$: Trung bình cộng là hằng số gần dữ liệu nhất theo nghĩa bình phương. Số liệu 12 kéo trung bình lên 5, trong khi ba số còn lại đều nhỏ hơn 5.
:::

::: exercise 2. Cùng dữ liệu, tiêu chí khác
Với bốn số liệu $1, 3, 4, 12$, tìm mọi hằng số $c$ cực tiểu $|c - 1| + |c - 3| + |c - 4| + |c - 12|$, và tìm hằng số cực tiểu $\max_i |c - b_i|$. So sánh với kết quả bài 1.
:::

::: hint
Với tổng trị tuyệt đối, xét độ dốc của hàm trên từng khoảng giữa các số liệu. Với sai số lớn nhất, chỉ hai số liệu nhỏ nhất và lớn nhất quyết định.
:::

::: solution
Hàm $F(c) = \sum_i |c - b_i|$ có độ dốc bằng số số liệu nằm bên trái $c$ trừ số số liệu nằm bên phải. Trên khoảng $(3, 4)$ có hai số liệu ở mỗi bên, nên độ dốc bằng 0. Trước khoảng đó hàm giảm, sau khoảng đó hàm tăng, nên mọi $c \in [3, 4]$ đều tối ưu. Giá trị tối ưu là $F(3) = 2 + 0 + 1 + 9 = 12$, và cũng bằng $F(4) = 3 + 1 + 0 + 8 = 12$. Với sai số lớn nhất, ta cần $c$ cách đều 1 và 12, nên $c^\star = 6.5$ với sai số lớn nhất $5.5$. Ba tiêu chí cho ba câu trả lời: Trung bình 5, cả đoạn trung vị $[3, 4]$, và điểm giữa 6.5. Tiêu chí ℓ₁ ít bị số liệu 12 ảnh hưởng nhất, còn tiêu chí sai số lớn nhất bị nó chi phối nhiều nhất.
:::

::: exercise 3. Viết một LP từ mô tả
Một cửa hàng pha hai loại hạt. Loại I giá 4 đơn vị tiền mỗi kg, chứa 3 g chất A và 1 g chất B mỗi kg. Loại II giá 3 đơn vị mỗi kg, chứa 1 g chất A và 2 g chất B. Hỗn hợp cần ít nhất 6 g chất A và 7 g chất B. Viết LP cực tiểu chi phí, rồi chứng minh $(x_1, x_2) = (1, 3)$ là nghiệm bằng cách tìm hai hệ số không âm như ở mục 2.3.
:::

::: solution
Bài toán là cực tiểu $4x_1 + 3x_2$ với $3x_1 + x_2 \ge 6$, $x_1 + 2x_2 \ge 7$, $x_1, x_2 \ge 0$. Điểm $(1, 3)$ khả thi vì $3 + 3 = 6$ và $1 + 6 = 7$, với chi phí $13$. Ta tìm hai hệ số $y_1, y_2 \ge 0$ sao cho $y_1(3x_1 + x_2) + y_2(x_1 + 2x_2)$ trùng với $4x_1 + 3x_2$. So sánh hệ số được hệ $3y_1 + y_2 = 4$, $y_1 + 2y_2 = 3$, cho $y_1 = y_2 = 1$, cả hai không âm. Vậy với mọi điểm khả thi,

$$
4x_1 + 3x_2 = (3x_1 + x_2) + (x_1 + 2x_2) \ge 6 + 7 = 13.
$$

Vì $(1, 3)$ đạt đúng 13, nó là nghiệm tối ưu. Lần này các ràng buộc có dạng $\ge$ và ta cực tiểu, nên tổ hợp không âm cho một cận dưới thay vì cận trên.
:::

## Tóm tắt

Bình phương tối thiểu và quy hoạch tuyến tính là hai lớp bài toán giải được một cách đáng tin cậy ngay cả khi rất lớn. Bình phương tối thiểu có công thức nghiệm qua hệ phương trình chuẩn, và hệ đó chính là điều kiện phần dư vuông góc với không gian cột. LP không có công thức nhưng có thuật toán hiệu quả, có bức tranh hình học là đẩy đường mức qua một đa diện, và có những chứng nhận tối ưu kiểm tra được bằng một tổ hợp không âm của các ràng buộc. Nhiều bài toán không trơn như xấp xỉ Chebyshev được đưa về LP nhờ biến phụ.

Tối ưu lồi chứa cả hai lớp đó như trường hợp riêng. Cái khó của nó nằm ở khâu nhận diện và biến đổi bài toán, chứ không ở khâu giải. Khi bài toán không lồi, ta phải chọn giữa tối ưu cục bộ nhanh nhưng không có bảo đảm và tối ưu toàn cục có bảo đảm nhưng rất tốn kém.

## Nguồn và đọc thêm

- S. Boyd, L. Vandenberghe, *Convex Optimization*, §1.1.2 (tr. 3–4), §1.2 (tr. 4–7) về bình phương tối thiểu, quy hoạch tuyến tính và xấp xỉ Chebyshev, §1.3 (tr. 7–8) về tối ưu lồi, §1.4 (tr. 9–10) về tối ưu cục bộ và toàn cục.
- Bài toán quy hoạch tuyến tính ở mục 2.3, dữ liệu ba điểm, số liệu của các bài tập, bài toán pha hạt, mô phỏng so sánh ba tiêu chí và các câu hỏi đào sâu do người soạn bổ sung. Mọi con số đã được tính lại bằng chương trình, và ba đường khớp trong mô phỏng được đối chiếu với bộ giải LP `scipy.optimize.linprog`.
