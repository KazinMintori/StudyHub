---
course: toan-cho-ai
lecture: bai-01-nhap-mon-toi-uu
topic: hai-lop-bai-toan-kinh-dien
section: topic
title: "Bình phương tối thiểu và quy hoạch tuyến tính"
description: "Hai họ bài toán giải được một cách hoàn toàn tin cậy: Bình phương tối thiểu với hệ phương trình chuẩn và hình học phép chiếu, quy hoạch tuyến tính với hình học đa diện, chứng nhận tối ưu và biến phụ, rồi tối ưu lồi như sự tổng quát hóa của cả hai."
---

Ở chủ đề trước, ta đã nắm vững cách thiết lập mô hình bài toán tối ưu. Câu hỏi tiếp theo là: Thiết lập xong rồi thì giải bằng cách nào? Câu trả lời từ thực tiễn tính toán: Bài toán tối ưu tổng quát **khó giải một cách đáng ngạc nhiên**, kể cả khi mọi hàm số mục tiêu và ràng buộc đều trơn như đa thức. Những phương pháp giải tổng quát luôn phải đối mặt với sự đánh đổi: Hoặc thời gian chạy quá lâu, hoặc không thể bảo đảm tìm ra nghiệm tối ưu.

Thế nhưng có những ngoại lệ quan trọng: Các họ bài toán mà khoa học tính toán đã có thuật toán giải quyết quy mô lớn, tốc độ cực nhanh và bảo chứng nghiệm toàn cục chắc chắn. Bài giảng này giới thiệu hai họ bài toán kinh điển nhất là **bình phương tối thiểu** và **quy hoạch tuyến tính**, đồng thời chỉ rõ rằng cả hai đều là trường hợp riêng của một cấu trúc bao trùm rộng lớn: **Tối ưu lồi**. Nắm vững bản chất vì sao hai họ bài toán này giải được chính là chìa khóa thấu suốt vì sao toàn bộ nền tảng toán học cho AI đều xoay quanh tính lồi.

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

Từ góc nhìn hình học này, ta nhận thấy một đặc trưng bản chất quan trọng: Vector dự đoán tối ưu $Ax^\star$, tức hình chiếu của $b$, luôn duy nhất. Nhưng bộ tham số $x^\star$ tạo ra nó chỉ duy nhất khi các cột của $A$ độc lập tuyến tính. Nếu có hai đặc trưng trùng nhau, chẳng hạn nhiệt độ đo bằng độ C và cùng nhiệt độ đó đổi sang độ F, thì có vô số cách chia trọng số giữa chúng mà vẫn cho cùng một dự đoán. Tập các nghiệm khi đó là một tập affine, đúng như chủ đề "Đường thẳng, đoạn thẳng và tập affine" đã mô tả.

::: example Khớp một đường thẳng qua ba điểm
Dữ liệu tự đặt gồm ba cặp $(t_i, y_i) = (0, 1), (1, 2), (2, 4)$. Mô hình $y = at + c$ có hai tham số $x = (a, c)$, nên

$$
A = \begin{bmatrix} 0 & 1 \\ 1 & 1 \\ 2 & 1 \end{bmatrix}, \qquad b = \begin{bmatrix} 1 \\ 2 \\ 4 \end{bmatrix}, \qquad A^T A = \begin{bmatrix} 5 & 3 \\ 3 & 3 \end{bmatrix}, \qquad A^T b = \begin{bmatrix} 10 \\ 7 \end{bmatrix}.
$$

Hệ chuẩn là $5a + 3c = 10$ và $3a + 3c = 7$. Lấy phương trình đầu trừ phương trình sau được $2a = 3$, nên $a^\star = \tfrac32$ và $c^\star = \tfrac56$. Vector dự đoán là $Ax^\star = (\tfrac56, \tfrac73, \tfrac{23}{6})$ và phần dư là $r = Ax^\star - b = (-\tfrac16, \tfrac13, -\tfrac16)$.

Kiểm tra điều kiện vuông góc: Tích của $r$ với cột thứ nhất là $0\cdot(-\tfrac16) + 1\cdot\tfrac13 + 2\cdot(-\tfrac16) = 0$, với cột thứ hai là $-\tfrac16 + \tfrac13 - \tfrac16 = 0$. Tổng bình phương phần dư là $\tfrac1{36} + \tfrac19 + \tfrac1{36} = \tfrac16$. Không đường thẳng nào cho tổng nhỏ hơn.
:::

### 1.3 Hai biến thể thường gặp
Để mô hình bình phương tối thiểu linh hoạt và thích ứng tốt hơn với dữ liệu thực tế, ta thường trang bị hai kỹ thuật nền tảng: Thứ nhất là **bình phương tối thiểu có trọng số**, cực tiểu $\sum_{i=1}^k w_i (a_i^T x - b_i)^2$ với các trọng số $w_i > 0$. Trọng số lớn thể hiện ta quan tâm nhiều hơn tới sai số của quan sát đó, chẳng hạn khi quan sát ấy có độ tin cậy đo lường cao hơn. Thứ hai là **kỹ thuật điều chuẩn (regularization)**, bổ sung vào hàm mục tiêu một số hạng phạt độ lớn của vector tham số:

$$
\sum_{i=1}^{k} (a_i^T x - b_i)^2 + \rho \sum_{j=1}^{n} x_j^2, \qquad \rho > 0 .
$$

Số hạng phạt giữ cho $x$ không quá lớn, và tham số $\rho$ do người dùng chọn để cân bằng giữa hai mong muốn: Khớp dữ liệu và giữ tham số nhỏ. Với $\rho > 0$, hệ chuẩn trở thành $(A^T A + \rho I)x = A^T b$, và ma trận $A^T A + \rho I$ luôn khả nghịch. Vì vậy nghiệm luôn duy nhất, kể cả khi các cột của $A$ phụ thuộc tuyến tính. Trong học máy, cách làm này được gọi là hồi quy ridge.

Bình phương tối thiểu còn có một cách hiểu thống kê sâu sắc: Nếu dữ liệu được sinh ra bởi mô hình tuyến tính cộng nhiễu Gauss độc lập cùng phương sai, thì nghiệm bình phương tối thiểu chính là ước lượng hợp lý cực đại (MLE). Kỹ thuật điều chuẩn cũng có cách hiểu tương tự, tương ứng với việc ta áp đặt một phân phối tiên nghiệm Gauss (Gaussian prior) lên vector tham số (ước lượng MAP).

Nhận ra một bài toán bình phương tối thiểu khá đơn giản: Chỉ cần quan sát thấy hàm mục tiêu là một hàm bậc hai, rồi kiểm tra ma trận toàn phương đi kèm có nửa xác định dương hay không. Ngày nay, việc giải bài toán bình phương tối thiểu được xem là một **công nghệ đã hoàn thiện và trưởng thành (mature technology)**, theo nghĩa người dùng không cần bận tâm đến từng chi tiết vi mô của thuật toán giải bên dưới mà vẫn có thể tin cậy vào kết quả đầu ra. Độ phức tạp tính toán thực tế xấp xỉ tỉ lệ với $\mathcal{O}(n^2 k)$ phép tính.

## 2. Quy hoạch tuyến tính

### 2.1 Bài toán

Lớp thứ hai là **quy hoạch tuyến tính** (linear program, viết tắt LP), trong đó cả hàm mục tiêu và mọi hàm ràng buộc đều tuyến tính:

$$
\begin{aligned}
\text{minimize}\quad & c^T x\\
\text{subject to}\quad & a_i^T x \le b_i, \quad i = 1, \ldots, m .
\end{aligned}
$$

Các vector $c, a_1, \ldots, a_m \in \mathbb{R}^n$ và các số $b_1, \ldots, b_m$ là dữ liệu bài toán. Khác với bình phương tối thiểu, LP **không có công thức nghiệm đóng**. Bù lại, khoa học tính toán sở hữu những thuật toán đặc biệt hiệu quả: Phương pháp đơn hình (Simplex) của George Dantzig và các phương pháp điểm trong (Interior-point methods). Độ phức tạp tính toán thực tế của các thuật toán LP hiện đại thường rơi vào khoảng $\mathcal{O}(n^2 m)$ phép tính khi $m \ge n$. Tương tự như bình phương tối thiểu, quy hoạch tuyến tính cũng được xếp vào nhóm công nghệ tối ưu hóa đã hoàn thiện và trưởng thành.

### 2.2 Bức tranh hình học: Đẩy một đường mức qua một đa giác

Mỗi ràng buộc $a_i^T x \le b_i$ cắt không gian làm đôi và giữ lại một nửa. Miền khả thi là giao của các nửa đó, một **đa diện**, trong mặt phẳng là một đa giác lồi. Hàm mục tiêu $c^T x$ có các đường mức $c^T x = \text{hằng số}$ là những đường thẳng song song. Giải LP trong mặt phẳng giống như đẩy một chiếc thước kẻ theo hướng làm giá trị tốt lên, cho tới khi thước chỉ còn chạm đa giác ở mép. Chỗ chạm cuối cùng thường là một đỉnh, và cũng có thể là cả một cạnh nếu thước song song với cạnh ấy.

Mô phỏng dưới đây cho phép người học thay đổi hệ số của hàm mục tiêu $\max\ c_1 x + c_2 y$ trên đa giác $\{x + y \le 4,\ x \le 2,\ x \ge 0,\ y \ge 0\}$. Hãy xác định một cặp hệ số khiến nghiệm tối ưu không duy nhất.

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

Có những bài toán thoạt nhìn không phải LP nhưng hoàn toàn có thể biến đổi tương đương thành một bài toán LP chuẩn tắc. Một ví dụ tiêu biểu và xuất hiện liên tục trong thực tế là **xấp xỉ Chebyshev (Chebyshev approximation)**:

$$
\text{minimize}\quad \max_{i = 1, \ldots, k} |a_i^T x - b_i| .
$$

Hàm mục tiêu đo phần dư **lớn nhất** thay vì tổng bình phương phần dư, và nó không khả vi ở những điểm mà hai phần dư lớn nhất bằng nhau. Mẹo biến đổi cốt lõi ở đây là bổ sung một biến phụ $t$ đóng vai trò làm chặn trên cho mọi phần dư:

$$
\begin{aligned}
\text{minimize}\quad & t\\
\text{subject to}\quad & a_i^T x - b_i \le t, \quad -(a_i^T x - b_i) \le t, \quad i = 1, \ldots, k .
\end{aligned}
$$

Hai bất đẳng thức cuối cùng tương đương với điều kiện $|a_i^T x - b_i| \le t$ với mọi $i$, tức $t$ không nhỏ hơn phần dư lớn nhất. Khi đưa vào bài toán cực tiểu hóa, biến $t$ sẽ bị kéo ghì xuống đúng bằng giá trị phần dư lớn nhất tại nghiệm, do đó hai bài toán có cùng nghiệm $x^\star$. Bài toán mới hoàn toàn tuyến tính theo vector biến mở rộng $(x, t)$. Kỹ thuật tư duy này áp dụng tương tự cho bài toán tổng trị tuyệt đối $\sum_{i=1}^k |a_i^T x - b_i|$ (chuẩn $\ell_1$), với mỗi phần dư được kẹp bởi một biến phụ riêng $t_i$. Đây là một bài học mẫu mực về nghệ thuật mô hình hóa: Những kỹ sư và nhà nghiên cứu giàu kinh nghiệm luôn nhận ra ngay cách làm phẳng các hàm không khả vi bằng các ràng buộc tuyến tính.

Ba tiêu chí đo sai số cho ba nghiệm khác nhau, và sự khác nhau đó không phải chuyện kỹ thuật mà là chuyện ta muốn gì. Mô phỏng sau đặt ba đường thẳng tối ưu cạnh nhau trên cùng dữ liệu.

<FitLab />

Thử kéo một điểm thật xa khỏi các điểm còn lại. Đường bình phương tối thiểu bị kéo theo rõ rệt, vì bình phương làm một sai số lớn trở nên rất lớn. Đường ℓ₁ gần như không đổi: Nó chịu được vài quan sát bất thường. Còn đường ℓ∞ lo cho trường hợp xấu nhất nên lại bị điểm bất thường chi phối mạnh nhất. Chọn tiêu chí là chọn mô hình, và lựa chọn đó phải đến từ hiểu biết về dữ liệu, không phải từ việc tiêu chí nào dễ tính hơn.

## 3. Tối ưu lồi: Điểm chung của hai lớp bài toán

Bây giờ ta có thể phát biểu họ bài toán là chủ đề trọng tâm của toàn bộ môn học. Một **bài toán tối ưu lồi** có dạng

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

Một triết lý sâu sắc trong tối ưu hiện đại: Khi đưa được một bài toán thực tế về dạng bài toán tối ưu lồi, bài toán đó về cơ bản coi như đã giải quyết xong. Cái khó của tối ưu lồi vì vậy không nằm ở khâu giải, mà nằm ở khâu **nhận ra** và **biến đổi** bài toán về dạng lồi. Nhận ra một bài toán bình phương tối thiểu thì dễ, nhận ra một hàm lồi thì khó hơn nhiều, và số mẹo biến đổi cũng nhiều hơn LP. Phần lớn chương này được dành để luyện đúng kỹ năng nhận diện ấy.

## 4. Khi bài toán không lồi và vai trò trợ lực của tối ưu lồi

Bài toán có hàm mục tiêu hoặc hàm ràng buộc không tuyến tính mà cũng không bảo đảm tính lồi được gọi chung là **tối ưu phi tuyến (nonconvex optimization)**. Với lớp bài toán tổng quát này, khoa học tính toán hiện nay chưa có một phương pháp vạn năng nào có thể tìm ra nghiệm tối ưu toàn cục trong thời gian đa thức. Khi đối mặt với địa hình phi lồi hiểm trở với vô số cực tiểu cục bộ và điểm yên ngựa, người ta thường đứng trước hai sự lựa chọn mang tính đánh đổi:

- **Tối ưu cục bộ (Local optimization)**: Chấp nhận từ bỏ tham vọng tìm nghiệm toàn cục để tập trung tìm một điểm tối ưu cục bộ khả thi. Các thuật toán này đạt tốc độ tính toán nhanh, xử lý được các mô hình quy mô hàng triệu biến và chỉ đòi hỏi hàm số khả vi. Tuy nhiên, kết quả phụ thuộc rất nhạy vào điểm xuất phát, thuật toán không thể đo lường xem điểm tìm được còn cách nghiệm toàn cục bao xa, và rất dễ mắc kẹt trong các bẫy cực tiểu cục bộ nông. Huấn luyện mạng nơ-ron sâu là ví dụ điển hình của trường phái này: Hàm mất mát phi lồi được tối ưu bằng các biến thể của phương pháp hạ gradient ngẫu nhiên (SGD, Adam).
- **Tối ưu toàn cục (Global optimization)**: Tìm kiếm nghiệm tối ưu toàn cục thực sự của bài toán. Cái giá phải trả là thời gian tính toán tăng theo hàm mũ theo số biến và số ràng buộc trong trường hợp xấu nhất. Phương pháp này chỉ khả thi với các bài toán có số lượng biến khiêm tốn (vài chục đến vài trăm biến) nhưng đòi hỏi độ an toàn tuyệt đối, chẳng hạn như chứng nhận vận hành hệ thống điều khiển hàng không vũ trụ hay thiết kế mạng lưới năng lượng trọng yếu.

### Tối ưu lồi trợ giúp bài toán phi lồi như thế nào?

Mặc dù tối ưu phi lồi là một bài toán khó, lý thuyết và thuật toán tối ưu lồi không hề đứng ngoài cuộc. Ngược lại, tối ưu lồi đóng vai trò là "bộ khung xương sống" cung cấp bốn cơ chế trợ lực nền tảng cho tối ưu phi lồi:

1. **Khởi tạo chất lượng cao cho tối ưu cục bộ (Convex initialization)**:
   Hiệu năng của các phương pháp tối ưu cục bộ phụ thuộc quyết định vào điểm xuất phát ban đầu $x^{(0)}$. Thay vì gieo xúc xắc ngẫu nhiên trong không gian nhiều chiều, người ta thường xây dựng một **bài toán xấp xỉ lồi (convex surrogate)** bằng cách lược bỏ các ràng buộc phi tuyến phức tạp hoặc thay hàm mục tiêu bằng một hàm lồi gần đúng. Nghiệm tối ưu toàn cục $x^\star_{\mathrm{lồi}}$ của bài toán xấp xỉ này được dùng làm điểm xuất phát cho thuật toán tối ưu cục bộ phi lồi. Điểm khởi tạo này đưa thuật toán vào ngay thung lũng tiềm năng chứa nghiệm tốt, giúp hạ gradient hội tụ nhanh chóng và tránh được các bẫy cục bộ kém chất lượng.

2. **Nới lỏng lồi và tính toán chặn dưới toàn cục (Convex relaxation & Global lower bounds)**:
   Bằng cách nới lỏng các ràng buộc rời rạc hoặc phi lồi thành các tập lồi chứa chúng (ví dụ: Ràng buộc nhị phân $x_i \in \{0, 1\}$ được nới lỏng thành đoạn lồi $x_i \in [0, 1]$, hoặc ràng buộc ma trận hạng một được nới lỏng thành nón ma trận nửa xác định dương trong SDP relaxation), ta thu được một bài toán tối ưu lồi nới lỏng. Do tập khả thi của bài toán lồi bao trọn tập khả thi của bài toán phi lồi, giá trị tối ưu của bài toán lồi luôn cung cấp một **ngưỡng chặn dưới toàn cục (global lower bound)** chắc chắn:
   $$
   p^\star_{\mathrm{lồi}} \le p^\star_{\mathrm{phi\ lồi}} \le f_0(x_{\mathrm{khả\ thi}}).
   $$
   Với bất kỳ nghiệm khả thi $x_{\mathrm{khả\ thi}}$ nào tìm được, khoảng cách $f_0(x_{\mathrm{khả\ thi}}) - p^\star_{\mathrm{lồi}}$ mang lại một **chứng chỉ giới hạn khoảng cách nghiệm (suboptimality certificate)**: Ta biết chắc chắn giải pháp hiện tại chỉ kém nghiệm toàn cục lý tưởng nhiều nhất là bao nhiêu, mang lại sự tự tin kỹ thuật mà không cần phải giải bài toán phi lồi đầy đủ.

3. **Cắt tỉa trong thuật toán nhánh và cận (Branch-and-Bound algorithms)**:
   Trong các thuật toán tối ưu toàn cục chính xác, không gian tìm kiếm được phân nhánh đệ quy thành các miền con nhỏ hơn. Tại mỗi nút của cây tìm kiếm, thuật toán giải một bài toán tối ưu lồi nới lỏng để xác định chặn dưới của miền con đó. Nếu chặn dưới này lớn hơn giá trị của nghiệm khả thi tốt nhất đã tìm thấy ở các nhánh khác, toàn bộ nhánh con đó lập tức bị **cắt tỉa (pruned)** mà không cần kiểm tra tiếp. Khả năng giải cực nhanh và chắc chắn của tối ưu lồi chính là động cơ then chốt giúp loại bỏ hàng tỷ nhánh vô vọng, thu hẹp đột phá không gian tìm kiếm.

4. **Quy hoạch lồi tuần tự (Sequential Convex Programming - SCP)**:
   Nhiều bài toán phi tuyến phức tạp trong kỹ thuật robot và dẫn đường quỹ đạo được giải bằng cách xấp xỉ bài toán phi lồi thành một chuỗi các bài toán lồi kế tiếp nhau. Tại mỗi bước lặp $x^{(k)}$, thuật toán tuyến tính hóa các ràng buộc phi lồi hoặc lồi hóa cục bộ quanh điểm hiện tại (như trong phương pháp Convex-Concave Procedure - CCP), sau đó giải bài toán lồi cục bộ để bước sang điểm $x^{(k+1)}$. Quy trình này biến một bài toán phi lồi nan giải thành một chuỗi các bước giải lồi ổn định và hội tụ tin cậy.

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
Với bốn số liệu $1, 3, 4, 12$, tìm mọi hằng số $c$ cực tiểu hóa biểu thức $|c - 1| + |c - 3| + |c - 4| + |c - 12|$ (chuẩn $\ell_1$), và tìm hằng số cực tiểu hóa $\max_i |c - b_i|$ (chuẩn $\ell_\infty$). So sánh với kết quả bình phương tối thiểu ở Bài 1.
:::

::: hint
Với chuẩn $\ell_1$, ghép các cặp đối xứng từ ngoài vào trong và áp dụng bất đẳng thức tam giác $|x| + |y| \ge |x - y|$. Với chuẩn $\ell_\infty$, nhận xét rằng sai số lớn nhất chỉ phụ thuộc vào hai điểm mút cực trị $b_{\min}$ và $b_{\max}$.
:::

::: solution
### 1. Tìm mọi hằng số $c$ cực tiểu hóa $|c - 1| + |c - 3| + |c - 4| + |c - 12|$ (Chuẩn $\ell_1$)

Xét hàm số:

$$
f(c) = |c - 1| + |c - 3| + |c - 4| + |c - 12|.
$$

Áp dụng bất đẳng thức $|x| + |y| \ge |x - y|$ bằng cách ghép các cặp đối xứng từ ngoài vào trong:

- **Với cặp ngoài cùng**: Đổi dấu số hạng thứ hai và áp dụng bất đẳng thức tam giác:
  $$
  |c - 1| + |c - 12| = |c - 1| + |12 - c| \ge |(c - 1) + (12 - c)| = 11.
  $$
  Dấu bằng xảy ra khi $(c - 1)(12 - c) \ge 0 \iff 1 \le c \le 12$.

- **Với cặp bên trong**: Thực hiện tương tự cho hai số hạng giữa:
  $$
  |c - 3| + |c - 4| = |c - 3| + |4 - c| \ge |(c - 3) + (4 - c)| = 1.
  $$
  Dấu bằng xảy ra khi $(c - 3)(4 - c) \ge 0 \iff 3 \le c \le 4$.

Cộng hai bất đẳng thức trên theo từng vế:

$$
f(c) \ge 11 + 1 = 12.
$$

Dấu bằng xảy ra đồng thời khi và chỉ khi:

$$
\begin{cases}
1 \le c \le 12, \\
3 \le c \le 4,
\end{cases}
\iff 3 \le c \le 4.
$$

**Kết luận**: Mọi giá trị $c \in [3, 4]$ đều làm cực tiểu hóa biểu thức (với giá trị cực tiểu đúng bằng $12$). Đây chính là khoảng **trung vị (median)** của tập dữ liệu.

---

### 2. Tìm hằng số $c$ cực tiểu hóa $\max_i |c - b_i|$ (Chuẩn $\ell_\infty$)

Với tập số liệu $\{1, 3, 4, 12\}$, giá trị nhỏ nhất là $b_{\min} = 1$ và lớn nhất là $b_{\max} = 12$. Do đó:

$$
\max_i |c - b_i| = \max(|c - 1|, |c - 12|).
$$

Áp dụng tính chất $\max(x, y) \ge \frac{x + y}{2}$ với mọi $x, y \ge 0$:

$$
\begin{aligned}
\max(|c - 1|, |12 - c|) &\ge \frac{|c - 1| + |12 - c|}{2} \\
&\ge \frac{|(c - 1) + (12 - c)|}{2} = \frac{11}{2} = 5.5.
\end{aligned}
$$

Dấu bằng đạt được khi hai khoảng cách bằng nhau:

$$
|c - 1| = |12 - c| \iff c - 1 = 12 - c \iff 2c = 13 \iff c = 6.5.
$$

**Kết luận**: Hằng số cực tiểu hóa duy nhất là $c = 6.5$ (điểm chính giữa của hai đầu mút, hay **midrange** $\frac{1 + 12}{2}$), với giá trị cực tiểu là $5.5$.

---

### 3. So sánh với bài toán bình phương tối thiểu (Bài 1)

Ở Bài 1, bài toán tìm hằng số $c$ cực tiểu hóa tổng bình phương sai số $\sum_{i=1}^4 (c - b_i)^2$ (chuẩn $\ell_2$) cho nghiệm là **giá trị trung bình (mean)**:

$$
c_{\ell_2} = \bar{b} = \frac{1 + 3 + 4 + 12}{4} = 5.
$$

**So sánh tổng quan theo 3 chuẩn**:
- **Chuẩn $\ell_1$ (Tổng sai số tuyệt đối)**: Nghiệm tối ưu là cả đoạn trung vị $c \in [3, 4]$. Nghiệm không duy nhất do số lượng mẫu là chẵn ($N = 4$). Tiêu chí này có tính bền vững cao (robust), hoàn toàn không bị ảnh hưởng bởi giá trị ngoại lai $12$.
- **Chuẩn $\ell_2$ (Tổng bình phương sai số - Bài 1)**: Nghiệm tối ưu duy nhất là giá trị trung bình $c = 5$. Phép bình phương phạt rất nặng sai số lớn, vì vậy nghiệm bị kéo mạnh về phía điểm ngoại lai $12$.
- **Chuẩn $\ell_\infty$ (Sai số cực đại nhỏ nhất)**: Nghiệm tối ưu duy nhất là trung điểm của hai đầu mút $c = 6.5$. Tiêu chí này chỉ quan tâm tới tình huống xấu nhất (worst-case), do đó chịu sự chi phối hoàn toàn bởi giá trị cực biên lớn nhất $12$.
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

Bình phương tối thiểu và quy hoạch tuyến tính là hai họ bài toán giải được một cách hoàn toàn tin cậy ngay cả khi số chiều dữ liệu rất lớn. Bình phương tối thiểu có công thức nghiệm qua hệ phương trình chuẩn, và hệ đó chính là điều kiện phần dư vuông góc với không gian cột. LP không có công thức nhưng có thuật toán hiệu quả, có bức tranh hình học là đẩy đường mức qua một đa diện, và có những chứng nhận tối ưu kiểm tra được bằng một tổ hợp không âm của các ràng buộc. Nhiều bài toán không trơn như xấp xỉ Chebyshev được đưa về LP nhờ biến phụ.

Tối ưu lồi chứa cả hai lớp đó như trường hợp riêng. Cái khó của nó nằm ở khâu nhận diện và biến đổi bài toán, chứ không ở khâu giải. Khi bài toán không lồi, ta phải chọn giữa tối ưu cục bộ nhanh nhưng không có bảo đảm và tối ưu toàn cục có bảo đảm nhưng rất tốn kém.

## Tài liệu tham khảo

- Stephen Boyd, Lieven Vandenberghe, *Convex Optimization*, Cambridge University Press.
