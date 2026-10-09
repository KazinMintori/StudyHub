---
course: toan-cho-ai
lecture: bai-00-on-tap-nen-tang
section: lecture
title: "Ôn tập nền tảng toán học cho AI"
prerequisites: ["ham-so", "dao-ham", "tap-hop"]
lessonStatus: ready
description: "Tính dự đoán bằng ma trận, gradient và độ cong; nối nhiễu Gauss với bình phương tối thiểu."
---

Mọi mô hình trí tuệ nhân tạo, từ hồi quy tuyến tính cổ điển đến các mạng nơ-ron sâu, đều vận hành quanh một cơ chế cốt lõi: ánh xạ dữ liệu thành dự đoán, đo sai số bằng hàm mất mát, và lần theo đạo hàm để tinh chỉnh tham số. Khi mô hình dự đoán chệch hướng, ta cần biết chính xác tham số nào phải thay đổi, thay đổi bao nhiêu và theo chiều nào.

Bài học mở đầu này ôn lại ba trụ cột toán học nền tảng sẽ đồng hành cùng chúng ta xuyên suốt môn học:
1. **Đại số ma trận**: Công cụ biểu diễn đồng thời nhiều dự đoán một cách cô đọng và tận dụng năng lực tính toán song song.
2. **Giải tích đa biến (Gradient & Hessian)**: Chiếc la bàn chỉ hướng dốc nhất để hạ thấp hàm mất mát và tấm gương phản chiếu độ cong địa hình tối ưu.
3. **Mô hình xác suất**: Cội nguồn lý thuyết giải thích vì sao tiêu chuẩn sai số bình phương tối thiểu xuất hiện tự nhiên từ giả thiết nhiễu Gauss.

Toàn bộ công thức và biến đổi giải tích sẽ được hiện thực hóa trên một tập dữ liệu nhỏ gọn, giúp bạn tự tay kiểm chứng từng bước biến đổi đại số mà không bị phân tâm bởi quy mô dữ liệu.

---

## 1. Biểu diễn dự đoán bằng phép nhân ma trận

Xét bài toán học có giám sát đơn giản: ta muốn xây dựng một mô hình tuyến tính đơn tham số để dự đoán biến mục tiêu $\widehat b_i$ từ đầu vào $a_i$ theo quy tắc $\widehat b_i = a_i w$. 

Giả sử ta thu thập được ba quan sát thực nghiệm sau:

| Quan sát $i$ | Đầu vào $a_i$ | Đầu ra thực tế $b_i$ |
| :---: | :---: | :---: |
| 1 | 1 | 1 |
| 2 | 2 | 2 |
| 3 | 3 | 2 |

Ở đây, các cặp $(a_i, b_i)$ là dữ liệu thực nghiệm đã cố định. Trọng số $w \in \mathbb{R}$ là tham số tự do mà chúng ta có quyền điều chỉnh để mô hình khớp dữ liệu nhất có thể. Chẳng hạn, nếu thử chọn $w = 1$, mô hình đưa ra ba dự đoán lần lượt là $1, 2, 3$. Hai dự đoán đầu khớp hoàn toàn với thực tế, nhưng ở quan sát thứ ba, mô hình dự đoán vượt giá trị thực tế một đơn vị ($\widehat b_3 - b_3 = 3 - 2 = 1$).

Thay vì viết ba phương trình rời rạc bằng vòng lặp tuần tự, trong kỹ nghệ AI ta gom toàn bộ đầu vào thành ma trận một cột và đầu ra thành một vector cột:

$$
A = \begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix}, \quad
b = \begin{bmatrix} 1 \\ 2 \\ 2 \end{bmatrix}, \quad
\widehat b = A w, \quad
r = A w - b.
$$

- **Vector** $b, \widehat b, r \in \mathbb{R}^3$ là các danh sách số có thứ tự, trong đó mỗi phần tử đại diện cho một mẫu dữ liệu.
- **Ma trận** $A \in \mathbb{R}^{3 \times 1}$ là bảng số gồm 3 hàng và 1 cột.
- **Vector phần dư** $r = \widehat b - b$ phản ánh độ lệch giữa dự đoán và nhãn thực tế. Ta quy ước dấu phần dư là dự đoán trừ đi quan sát. Sự nhất quán về quy ước dấu này là điều kiện tiên quyết để tính đúng chiều của gradient sau này.

Trong bài toán tổng quát với $m$ quan sát và $n$ đặc trưng, ma trận dữ liệu có kích thước $A \in \mathbb{R}^{m \times n}$, vector trọng số $w \in \mathbb{R}^n$, còn nhãn thực tế và phần dư là các vector trong không gian $m$ chiều: $b, r \in \mathbb{R}^m$. Hàng thứ $i$ của ma trận $A$ (ký hiệu $a_i^T$) chứa đựng toàn bộ thông tin đặc trưng của mẫu thứ $i$, và tích vô hướng $a_i^T w$ sinh ra đúng giá trị dự đoán cho mẫu đó.

Một cách người ta hay dùng trong thực tế để không bao giờ nhầm lẫn chiều khi nhân ma trận là quy tắc **"khớp ở giữa, nở hai đầu"**: khi nhân ma trận kích thước $(m \times k)$ với ma trận kích thước $(k \times n)$, hai chỉ số ở giữa bắt buộc phải trùng nhau để các phép nhân tích vô hướng thực hiện được, và kết quả thu được sẽ có kích thước chính là hai đầu ngoài cùng $(m \times n)$. Trong kỹ nghệ học sâu, tư duy ma trận hóa này (vectorization) giúp thuật toán chạy nhanh hơn hàng trăm lần trên phần cứng GPU/TPU so với các vòng lặp tuần tự.

<details><summary>Câu hỏi đào sâu: Nếu ma trận dữ liệu A có 5 hàng và 2 cột thì w và Aw có bao nhiêu thành phần?</summary>

Theo quy tắc phối hợp kích thước, $w$ bắt buộc phải là vector cột có 2 thành phần ($w \in \mathbb{R}^{2 \times 1}$) để khớp với 2 cột đặc trưng của $A$. Khi đó, tích $Aw$ sẽ là vector có kích thước $(5 \times 2) \times (2 \times 1) = (5 \times 1)$, tức gồm 5 thành phần, tương ứng với 5 giá trị dự đoán cho 5 quan sát.

</details>

---

## 2. Tích vô hướng, chuẩn vector và độ lớn của phần dư

Làm thế nào để đo lường mức độ "chệch" tổng thể của toàn bộ vector phần dư $r$? Để làm được điều này, ta cần đến các khái niệm độ dài và chuẩn trong không gian vector.

Với hai vector bất kỳ $u = (u_1, \ldots, u_n)^T$ và $v = (v_1, \ldots, v_n)^T$, **tích vô hướng** (inner product) được định nghĩa bằng tổng các tích của từng cặp thành phần tương ứng:

$$
u^T v = u_1 v_1 + u_2 v_2 + \cdots + u_n v_n = \sum_{j=1}^n u_j v_j.
$$

Ký hiệu $T$ biểu thị phép chuyển vị, biến một vector cột thành vector hàng. Cần phân biệt rõ: $u^T v$ là một đại lượng vô hướng (scalar, số thực), trong khi $u v^T$ lại tạo ra một ma trận kích thước $n \times n$ (outer product). Hai cấu trúc này hoàn toàn khác biệt và không được hoán đổi cho nhau.

**Chuẩn Euclid** (chuẩn $L_2$) đo khoảng cách hình học thẳng hàng từ gốc tọa độ tới điểm $u$:

$$
\|u\|_2 = \sqrt{u_1^2 + \cdots + u_n^2} = \sqrt{u^T u}.
$$

Từ chuẩn Euclid, ta xây dựng **hàm mất mát bình phương tối thiểu** (least squares loss function) cho mô hình:

$$
f(w) = \frac{1}{2} \|Aw - b\|_2^2 = \frac{1}{2} \sum_{i=1}^m r_i^2.
$$

Bình phương mỗi phần dư $r_i^2$ đảm bảo rằng mọi sai lệch — dù âm hay dương — đều đóng góp một lượng không âm vào tổng mất mát. Sai số càng lớn thì hình phạt tăng càng nhanh.

Hệ số $\frac{1}{2}$ phía trước đóng vai trò làm gọn biểu thức giải tích: khi lấy đạo hàm theo $w$, số mũ 2 hạ xuống triệt tiêu với phân số $\frac{1}{2}$, giúp công thức đạo hàm không còn thừa hệ số 2. Vì $\frac{1}{2} > 0$, phép nhân với hằng số dương này không làm thay đổi vị trí của điểm cực tiểu $w^*$.

::: example So sánh định lượng giữa hai giá trị tham số
Xét tập dữ liệu 3 điểm ở mục 1:
- Thử với $w = 1$: Vector phần dư là $r = (0, 0, 1)^T$. Mất mát tương ứng:
  $$f(1) = \frac{1}{2}(0^2 + 0^2 + 1^2) = \frac{1}{2} = 0.5.$$
- Thử với $w = \frac{1}{2}$: Vector phần dư là $r = (-\frac{1}{2}, -1, -\frac{1}{2})^T$. Mất mát tương ứng:
  $$
  \begin{aligned}
  f\left(\frac{1}{2}\right) &= \frac{1}{2}\left[\left(-\frac{1}{2}\right)^2 + (-1)^2 + \left(-\frac{1}{2}\right)^2\right] \\
  &= \frac{1}{2}\left(\frac{1}{4} + 1 + \frac{1}{4}\right) = \frac{3}{4} = 0.75.
  \end{aligned}
  $$

Rõ ràng $f(1) < f(\frac{1}{2})$, nghĩa là $w = 1$ khớp dữ liệu tốt hơn $w = \frac{1}{2}$. Tuy nhiên, việc thử từng giá trị rời rạc như vậy không thể khẳng định $w = 1$ đã là nghiệm tối ưu toàn cục. Muốn tìm nghiệm tối ưu giữa vô hạn số thực, ta phải viện đến giải tích: đi tìm nơi mà đạo hàm triệt tiêu.
:::

Ngoài chuẩn $L_2$, trong học máy chúng ta còn thường xuyên bắt gặp hai chuẩn quan trọng khác:

$$
\begin{aligned}
\|u\|_1 &= \sum_{j=1}^n |u_j| = |u_1| + \cdots + |u_n|, \\
\|u\|_\infty &= \max_{1 \le j \le n} |u_j|.
\end{aligned}
$$

Chẳng hạn với vector $u = (3, -4)^T$, ta có $\|u\|_1 = |3| + |-4| = 7$, $\|u\|_2 = \sqrt{3^2 + (-4)^2} = 5$, và $\|u\|_\infty = \max(3, 4) = 4$. Mỗi chuẩn phản ánh một mục tiêu phạt sai số khác nhau: chuẩn $L_1$ thúc đẩy nghiệm thưa (như trong hồi quy Lasso), chuẩn $L_2$ phạt nặng các sai số lớn và khả vi trơn tru khắp nơi, còn chuẩn $L_\infty$ kiểm soát kịch bản sai lệch lớn nhất.

---

## 3. Gradient: La bàn chỉ hướng trong không gian tham số

Với hàm một biến, đạo hàm $f'(w)$ cho biết độ biến thiên xấp xỉ bậc nhất: khi dịch chuyển một bước vi phân $d$, hàm số thay đổi xấp xỉ $f(w+d) \approx f(w) + f'(w)d$. 

Khi mô hình có nhiều tham số ($w \in \mathbb{R}^n$), ta gom toàn bộ các đạo hàm riêng theo từng biến thành vector **gradient**:

$$
\nabla f(w) = \begin{bmatrix} \frac{\partial f}{\partial w_1} \\ \vdots \\ \frac{\partial f}{\partial w_n} \end{bmatrix} \in \mathbb{R}^n.
$$

Đạo hàm riêng $\frac{\partial f}{\partial w_j}$ đo lường mức độ biến thiên của mất mát khi chỉ riêng trọng số $w_j$ nhích nhẹ, còn tất cả các trọng số khác được giữ cố định nguyên vẹn.

Ta suy diễn từng bước công thức gradient cho hàm mất mát tổng bình phương $f(w) = \frac{1}{2} \sum_{i=1}^m r_i^2$. Thành phần phần dư thứ $i$ được viết cụ thể là:

$$
r_i = \sum_{k=1}^n A_{ik} w_k - b_i.
$$

Lấy đạo hàm riêng của phần dư $r_i$ theo tham số $w_j$, chỉ có số hạng chứa $w_j$ (với hệ số $A_{ij}$) là biến đổi, do đó:

$$
\frac{\partial r_i}{\partial w_j} = A_{ij}.
$$

Áp dụng quy tắc chuỗi giải tích cho hàm mất mát $f(w)$:

$$
\frac{\partial f}{\partial w_j} = \sum_{i=1}^m r_i \frac{\partial r_i}{\partial w_j} = \sum_{i=1}^m A_{ij} r_i.
$$

Biểu thức vế phải chính là tích vô hướng giữa cột thứ $j$ của ma trận $A$ (hay hàng thứ $j$ của ma trận chuyển vị $A^T$) với vector phần dư $r$. Khi ghép toàn bộ $n$ đạo hàm riêng lại với nhau, ta thu được kết quả cô đọng:

$$
\boxed{\nabla f(w) = A^T r = A^T (Aw - b).}
$$

Kiểm tra tính tương thích về chiều ma trận: $A^T$ có kích thước $n \times m$, nhân với vector phần dư $r$ có kích thước $m \times 1$. Theo quy tắc khớp chiều, tích này cho ra đúng một vector kích thước $n \times 1$ — hoàn toàn tương thích với số chiều của vector tham số $w$.

Ý nghĩa hình học của gradient: **Vector gradient $\nabla f(w)$ luôn chỉ về hướng hàm số tăng nhanh nhất (dốc nhất)**. Do đó, khi mục tiêu là hạ thấp sai số, hướng di chuyển tự nhiên là ngược chiều gradient: hướng $- \nabla f(w)$. Đây là nguyên lý khai sinh thuật toán **Gradient Descent** trong huấn luyện mô hình học máy.

::: example Tìm tham số tối ưu cho mô hình một chiều
Áp dụng công thức trên vào dữ liệu cụ thể ở đầu bài:
$$
\begin{aligned}
f(w) &= \frac{1}{2} \left[ (w - 1)^2 + (2w - 2)^2 + (3w - 2)^2 \right] \\
&= \frac{1}{2} \left( 14w^2 - 22w + 9 \right) \\
&= 7w^2 - 11w + \frac{9}{2}.
\end{aligned}
$$

Đạo hàm bậc nhất:
$$
f'(w) = 14w - 11.
$$

Để tìm điểm dừng (stationary point), ta giải phương trình đạo hàm triệt tiêu $f'(w) = 0$:
$$
14w - 11 = 0 \iff w^* = \frac{11}{14}.
$$

Tại điểm dừng $w^* = \frac{11}{14}$:
- Vector dự đoán: $\widehat b = \left(\frac{11}{14}, \frac{22}{14}, \frac{33}{14}\right)^T = \left(\frac{11}{14}, \frac{11}{7}, \frac{33}{14}\right)^T$.
- Vector phần dư:
  $$r = \widehat b - b = \left(-\frac{3}{14}, -\frac{6}{14}, \frac{5}{14}\right)^T = \left(-\frac{3}{14}, -\frac{3}{7}, \frac{5}{14}\right)^T.$$
- Giá trị mất mát tối ưu:
  $$
  \begin{aligned}
  f(w^*) &= \frac{1}{2} \left[ \left(-\frac{3}{14}\right)^2 + \left(-\frac{6}{14}\right)^2 + \left(\frac{5}{14}\right)^2 \right] \\
  &= \frac{1}{2} \cdot \frac{9 + 36 + 25}{196} = \frac{1}{2} \cdot \frac{70}{196} = \frac{5}{28} \approx 0.1786.
  \end{aligned}
  $$

Giá trị này nhỏ hơn mức $f(1) = 0.5$ và $f(0.5) = 0.75$ mà ta đã tính thử trước đó. Nhưng liệu điểm dừng $w^* = 11/14$ có chắc chắn là điểm cực tiểu toàn cục, hay chỉ là điểm dừng cục bộ? Để trả lời điều đó, ta cần kiểm tra độ cong địa hình thông qua đạo hàm bậc hai.
:::

<details><summary>Câu hỏi đào sâu: Tại w = 1, đạo hàm nhận giá trị âm hay dương? Muốn giảm hàm mất mát thì nên tăng hay giảm w?</summary>

Ta có $f'(1) = 14(1) - 11 = 3 > 0$. Vì đạo hàm dương, hàm số đang có xu hướng tăng khi $w$ tăng. Do đó, muốn giảm mất mát, ta phải đi ngược chiều đạo hàm, tức là cần **giảm** $w$. Kết quả này hoàn toàn khớp với việc nghiệm tối ưu $w^* = 11/14 \approx 0.786 < 1$.

</details>

---

## 4. Ma trận Hessian và độ cong theo các hướng

Nếu gradient cung cấp thông tin xấp xỉ bậc nhất (độ dốc của mặt phẳng tiếp diện), thì ma trận **Hessian** $H = \nabla^2 f(w)$ cung cấp thông tin xấp xỉ bậc hai — phản ánh độ cong địa hình của hàm mục tiêu:

$$
f(w + d) \approx f(w) + \nabla f(w)^T d + \frac{1}{2} d^T H d.
$$

Số hạng toàn phương $d^T H d$ thể hiện độ cong của hàm số khi ta dịch chuyển theo hướng vector $d$.
- Nếu $d^T H d > 0$: địa hình uốn cong lên trên theo hướng $d$ (giống đáy thung lũng hay chiếc bát ngửa).
- Nếu $d^T H d < 0$: địa hình uốn cong xuống dưới (giống đỉnh đồi).
- Nếu $d^T H d = 0$: địa hình phẳng theo hướng $d$.

Với hàm mất mát bình phương $f(w) = \frac{1}{2}\|Aw - b\|_2^2$, lấy đạo hàm bậc hai của biểu thức gradient $\nabla f(w) = A^TAw - A^Tb$, ta thu được ma trận Hessian hằng số:

$$
H = \nabla^2 f(w) = A^T A.
$$

Để hiểu ý nghĩa hình học của ma trận này, ta kiểm tra dạng toàn phương với một hướng dịch chuyển $d \in \mathbb{R}^n$ bất kỳ:

$$
d^T H d = d^T (A^T A) d = (A d)^T (A d) = \|A d\|_2^2 \ge 0.
$$

Vì chuẩn Euclid của một vector luôn không âm ($\|Ad\|_2^2 \ge 0$), dạng toàn phương $d^THd$ **không bao giờ âm với mọi vector $d$**.

Một ma trận đối xứng thỏa mãn $d^T H d \ge 0$ với mọi $d$ được gọi là ma trận **nửa xác định dương** (Positive Semidefinite, ký hiệu $H \succeq 0$). Nếu dạng toàn phương nghiêm ngặt dương ($d^T H d > 0$) với mọi $d \ne 0$, ma trận được gọi là **dương xác định** (Positive Definite, ký hiệu $H \succ 0$).

Ma trận Hessian $H = A^TA$ luôn ít nhất là nửa xác định dương ($H \succeq 0$). Điều này chứng minh rằng bề mặt mất mát của bài toán bình phương tối thiểu luôn là một mặt lồi paraboloid hướng lên trên, không bao giờ có độ cong âm ở bất kỳ điểm nào.

Trong ví dụ một tham số ở trên, $H = A^T A = 1^2 + 2^2 + 3^2 = 14 > 0$. Khai triển Taylor bậc hai quanh điểm dừng $w^* = \frac{11}{14}$ trở thành một đẳng thức:

$$
f(w) = \frac{5}{28} + 7 \left( w - \frac{11}{14} \right)^2.
$$

Vì số hạng bình phương $7(w - 11/14)^2 \ge 0$ và chỉ triệt tiêu khi $w = w^*$, ta có chứng nhận toán học rằng $w^* = 11/14$ là điểm cực tiểu toàn cục duy nhất của bài toán.

Một nhầm lẫn thường gặp khi mới học là nhìn vào dấu của từng phần tử để đoán tính xác định dương của ma trận:
- Ma trận $\begin{bmatrix} 1 & 2 \\ 2 & 1 \end{bmatrix}$ có toàn bộ các phần tử đều dương, nhưng với hướng lệch $d = (1, -1)^T$, ta có $d^T H d = \begin{bmatrix}1 & -1\end{bmatrix} \begin{bmatrix}-1 \\ 1\end{bmatrix} = -2 < 0$. Ma trận này không nửa xác định dương.
- Ngược lại, ma trận $\begin{bmatrix} 1 & -1 \\ -1 & 1 \end{bmatrix}$ chứa các phần tử âm, nhưng dạng toàn phương của nó là:
  $$d^T H d = d_1^2 - 2d_1d_2 + d_2^2 = (d_1 - d_2)^2 \ge 0 \quad \forall d,$$
  do đó nó là ma trận nửa xác định dương (PSD).

<details><summary>Câu hỏi đào sâu: Vì sao ma trận $A^TA$ luôn là PSD nhưng chưa chắc đã là PD? Điều kiện nào của dữ liệu A sẽ bảo đảm tính PD?</summary>

$A^TA$ luôn PSD vì $d^T(A^TA)d = \|Ad\|_2^2 \ge 0$. Tuy nhiên, để là PD ($H \succ 0$), ta cần $\|Ad\|_2^2 > 0$ với mọi $d \ne 0$. Nếu tồn tại một hướng $d \ne 0$ sao cho $Ad = 0$ (nghĩa là các cột của ma trận $A$ phụ thuộc tuyến tính, hay ma trận bị thiếu hạng cột - rank-deficient), thì độ cong theo hướng đó bằng 0. Khi đó bài toán có vô số nghiệm tối ưu (mặt đáy hình máng phẳng). 

Để $A^TA$ dương xác định ($H \succ 0$), điều kiện cần và đủ là các cột của ma trận đặc trưng $A$ phải độc lập tuyến tính, tức $A$ đủ hạng cột ($\text{rank}(A) = n$). Khi đó nghiệm cực tiểu toàn cục được bảo đảm là duy nhất.

</details>

---

## 5. Mật độ xác suất và Phân phối chuẩn Gauss

Tại sao trong thực tế người ta lại chọn chuẩn bình phương $\|Aw - b\|_2^2$ để tối ưu mà không phải chuẩn mũ 3 hay mũ 4? Để trả lời thấu đáo câu hỏi này, ta cần xem xét bài toán qua lăng kính của lý thuyết xác suất và thống kê.

Với một biến ngẫu nhiên liên tục $Z$ có hàm mật độ xác suất $p(z)$, xác suất để $Z$ rơi vào một khoảng $[a, b]$ được tính bằng tích phân của mật độ:

$$
P(a \le Z \le b) = \int_a^b p(z) \, dz.
$$

Lưu ý rằng giá trị hàm mật độ $p(z)$ tại một điểm không phải là xác suất sinh ra đúng điểm đó (đối với biến liên tục, xác suất tại một điểm đơn lẻ luôn bằng 0). Hai đặc trưng quan trọng của phân phối là **kỳ vọng** $\mathbb{E}[Z] = \int z p(z) dz$ (trọng tâm phân phối) và **phương sai** $\text{Var}(Z) = \mathbb{E}[(Z - \mathbb{E}[Z])^2]$ (mức độ phân tán quanh trọng tâm).

**Phân phối chuẩn (Gauss)** một biến với kỳ vọng $\mu$ và phương sai $\sigma^2 > 0$ có hàm mật độ hình chuông:

$$
p(z) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp\left[ -\frac{(z - \mu)^2}{2\sigma^2} \right].
$$

Khi mở rộng sang vector ngẫu nhiên $Z \in \mathbb{R}^m$ với vector kỳ vọng $\mu \in \mathbb{R}^m$ và ma trận hiệp phương sai $\Sigma \in \mathbb{R}^{m \times m}$ đối xứng dương xác định ($\Sigma \succ 0$), hàm mật độ Gauss đa biến có dạng:

$$
p(z) = \frac{1}{(2\pi)^{m/2} \sqrt{\det\Sigma}} \exp\left[ -\frac{1}{2} (z - \mu)^T \Sigma^{-1} (z - \mu) \right].
$$

- Ma trận hiệp phương sai $\Sigma$ lưu giữ phương sai của từng thành phần trên đường chéo chính ($\Sigma_{ii} = \sigma_i^2$) và mức độ tương quan tuyến tính giữa các cặp thành phần ở các vị trí ngoài đường chéo ($\Sigma_{ij} = \text{Cov}(Z_i, Z_j)$).
- Định thức $\det\Sigma$ phản ánh thể tích của ellipsoid phân tán dữ liệu, đóng vai trò chuẩn hóa diện tích tích phân của hàm mật độ về đúng bằng 1.
- Trường hợp đặc biệt quan trọng: khi các thành phần sai số độc lập thống kê và có cùng phương sai $\sigma^2$, ma trận hiệp phương sai trở thành ma trận đường chéo $\Sigma = \sigma^2 I$. Lúc này, mật độ đa biến phân rã thành tích của $m$ mật độ Gauss độc lập: $p(z) = \prod_{i=1}^m p(z_i)$.

---

## 6. Nguồn gốc xác suất của Bài toán Bình phương tối thiểu

Giờ đây ta có thể nhìn thấy mối liên hệ trực tiếp giữa học máy và xác suất thống kê.

Giả sử trong thực tế, quá trình sinh dữ liệu tuân theo mô hình tuyến tính bị làm nhiễu:

$$
b_i = a_i^T w + \varepsilon_i, \qquad \varepsilon_i \overset{\text{độc lập, cùng phân phối}}{\sim} \mathcal{N}(0, \sigma^2).
$$

Nghĩa là nhãn thực tế $b_i$ là một biến ngẫu nhiên có kỳ vọng đúng bằng giá trị mô hình dự đoán $\mathbb{E}[b_i] = a_i^T w$, và bị sai lệch bởi một nhiễu ngẫu nhiên Gauss $\varepsilon_i$ không thiên vị (kỳ vọng bằng 0) với phương sai $\sigma^2$.

Theo mô hình này, mật độ xác suất có điều kiện của nhãn $b_i$ khi biết tham số $w$ là:

$$
p(b_i \mid w) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp\left[ -\frac{(b_i - a_i^T w)^2}{2\sigma^2} \right].
$$

Vì các quan sát độc lập với nhau, xác suất đồng thời (hàm **Likelihood** — hợp lý) của toàn bộ tập dữ liệu $b = (b_1, \ldots, b_m)^T$ bằng tích các mật độ thành phần:

$$
\begin{aligned}
L(w) &= p(b \mid w) = \prod_{i=1}^m p(b_i \mid w) \\
&= \left( \frac{1}{2\pi\sigma^2} \right)^{m/2} \exp\left[ -\frac{1}{2\sigma^2} \sum_{i=1}^m (a_i^T w - b_i)^2 \right].
\end{aligned}
$$

Triết lý ước lượng hợp lý cực đại (**Maximum Likelihood Estimation - MLE**): Ta muốn tìm bộ tham số $w$ sao cho khả năng quan sát được tập dữ liệu hiện có trong thực tế là lớn nhất. 

Để cực đại hóa một tích các hàm mũ, trong toán tối ưu người ta dùng phép biến đổi lấy **âm logarit tự nhiên** (Negative Log-Likelihood - NLL). Do hàm logarit đơn điệu tăng ngặt, việc cực đại hóa $L(w)$ hoàn toàn tương đương với việc cực tiểu hóa $-\log L(w)$:

$$
-\log p(b \mid w) = \frac{m}{2} \log(2\pi\sigma^2) + \frac{1}{2\sigma^2} \|Aw - b\|_2^2.
$$

Quan sát biểu thức trên:
- Số hạng đầu tiên $\frac{m}{2}\log(2\pi\sigma^2)$ là một hằng số không phụ thuộc vào tham số $w$.
- Hệ số $\frac{1}{2\sigma^2}$ là một số dương cố định.

Do đó, bài toán tìm $w$ để cực đại hóa hàm hợp lý Likelihood quy về chính xác:

$$
\arg\min_w \left[ -\log p(b \mid w) \right] \equiv \arg\min_w \frac{1}{2} \|Aw - b\|_2^2.
$$

Tiêu chuẩn bình phương tối thiểu không phải là một công thức cảm tính được chọn ngẫu nhiên. Nó là hệ quả toán học trực tiếp của nguyên lý cực đại hóa hàm hợp lý dưới giả thiết sai số quan sát tuân theo phân phối chuẩn Gauss độc lập.

Nếu các sai số quan sát không có cùng phương sai hoặc có tương quan lẫn nhau (ma trận hiệp phương sai tổng quát $\Sigma \succ 0$), biểu thức NLL sẽ dẫn tới hàm mất mát bình phương có trọng số:

$$
f(w) = \frac{1}{2} (Aw - b)^T \Sigma^{-1} (Aw - b).
$$

Mỗi quan sát có độ không đảm bảo cao (phương sai lớn) sẽ tự động bị ma trận $\Sigma^{-1}$ giảm trọng số ảnh hưởng trong hàm mất mát.

<details><summary>Câu hỏi đào sâu: Nếu dữ liệu có nhiều điểm ngoại lai (outliers) cực đoan, điều gì sẽ xảy ra với hàm mất mát bình phương? Ta nên đổi sang mô hình xác suất nào?</summary>

Vì hàm mất mát $L_2$ phạt bình phương sai số ($r_i^2$), một điểm ngoại lai lệch gấp 10 lần sẽ bị phạt gấp $10^2 = 100$ lần. Mô hình sẽ bị kéo lệch đáng kể chỉ để thỏa hiệp với điểm nhiễu này. 

Để khắc phục, trong thực tế người ta thay giả thiết nhiễu Gauss bằng giả thiết nhiễu có đuôi nặng hơn, chẳng hạn như **phân phối Laplace** ($p(\varepsilon) \propto \exp(-|\varepsilon|/\beta)$). Khi lấy âm log của phân phối Laplace, số mũ rơi xuống thành trị tuyệt đối, dẫn tới hàm mất mát chuẩn $L_1$: $\sum |a_i^Tw - b_i|$. Hàm mất mát $L_1$ chỉ phạt tuyến tính theo sai số, mang lại khả năng chống chịu ngoại lai (robustness) bền bỉ hơn cho mô hình.

</details>

---

## Bài tập tự luyện

::: exercise 1. Rèn luyện phép nhân ma trận và kiểm tra kích thước
Cho ma trận dữ liệu $A = \begin{bmatrix} 1 & 2 \\ 0 & 1 \end{bmatrix}$, vector trọng số $w = \begin{bmatrix} 2 \\ -1 \end{bmatrix}$, và vector nhãn $b = \begin{bmatrix} 0 \\ 2 \end{bmatrix}$. 
Hãy tính vector dự đoán $\widehat b$, vector phần dư $r$, và giá trị hàm mất mát bình phương $f(w) = \frac{1}{2}\|r\|_2^2$.
:::
::: solution
- Vector dự đoán:
  $$
  \widehat b = Aw = \begin{bmatrix} 1 & 2 \\ 0 & 1 \end{bmatrix} \begin{bmatrix} 2 \\ -1 \end{bmatrix} = \begin{bmatrix} 1(2) + 2(-1) \\ 0(2) + 1(-1) \end{bmatrix} = \begin{bmatrix} 0 \\ -1 \end{bmatrix}.
  $$
- Vector phần dư:
  $$
  r = \widehat b - b = \begin{bmatrix} 0 \\ -1 \end{bmatrix} - \begin{bmatrix} 0 \\ 2 \end{bmatrix} = \begin{bmatrix} 0 \\ -3 \end{bmatrix}.
  $$
- Giá trị hàm mất mát:
  $$
  f(w) = \frac{1}{2} \|r\|_2^2 = \frac{1}{2} (0^2 + (-3)^2) = \frac{9}{2} = 4.5.
  $$
Vector phần dư có đúng 2 thành phần vì tập dữ liệu có $m = 2$ quan sát.
:::

::: exercise 2. Lần theo dấu vết Gradient
Với ma trận $A$, trọng số $w$ và nhãn $b$ ở Bài tập 1, hãy tính vector gradient $\nabla f(w) = A^T r$. Giải thích vì sao kết quả nhận được có 2 thành phần.
:::
::: solution
Chuyển vị của ma trận $A$ là $A^T = \begin{bmatrix} 1 & 0 \\ 2 & 1 \end{bmatrix}$.

Vector gradient là:
$$
\nabla f(w) = A^T r = \begin{bmatrix} 1 & 0 \\ 2 & 1 \end{bmatrix} \begin{bmatrix} 0 \\ -3 \end{bmatrix} = \begin{bmatrix} 1(0) + 0(-3) \\ 2(0) + 1(-3) \end{bmatrix} = \begin{bmatrix} 0 \\ -3 \end{bmatrix}.
$$

Kết quả gradient có đúng 2 thành phần vì không gian tham số có $n = 2$ chiều ($w \in \mathbb{R}^2$). Mỗi thành phần của gradient cho biết tốc độ thay đổi của hàm mất mát theo từng tham số tương ứng ($\frac{\partial f}{\partial w_1} = 0$, $\frac{\partial f}{\partial w_2} = -3$). Nếu muốn giảm mất mát, ta cần tăng $w_2$ vì đạo hàm riêng của nó đang mang dấu âm.
:::

::: exercise 3. Khảo sát một hệ suy biến thiếu hạng (Rank-deficient)
Xét mô hình chỉ dự đoán tổng hai tham số $w_1 + w_2$ cho một quan sát duy nhất có nhãn $b = 1$. Hàm mất mát là $f(w) = \frac{1}{2}(w_1 + w_2 - 1)^2$.
Hỏi bài toán này có nghiệm tối ưu duy nhất hay không? Hãy phân tích tính chất ma trận Hessian để trả lời.
:::
::: solution
Ở bài toán này, ma trận dữ liệu chỉ gồm một hàng $A = \begin{bmatrix} 1 & 1 \end{bmatrix}$. 

Ma trận Hessian là:
$$
H = A^T A = \begin{bmatrix} 1 \\ 1 \end{bmatrix} \begin{bmatrix} 1 & 1 \end{bmatrix} = \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix}.
$$

Dạng toàn phương của Hessian là $d^T H d = (d_1 + d_2)^2 \ge 0$, do đó $H$ nửa xác định dương ($H \succeq 0$). Tuy nhiên, nếu ta chọn hướng dịch chuyển $d = (1, -1)^T \ne 0$, thì $d^T H d = (1 - 1)^2 = 0$. Điều này cho thấy Hessian không dương xác định ($H \not\succ 0$).

Hàm mất mát đạt giá trị nhỏ nhất bằng 0 tại mọi điểm nằm trên đường thẳng $w_1 + w_2 = 1$. Do đó bài toán có vô số nghiệm tối ưu, tạo thành một đáy thung lũng phẳng lỳ. Ví dụ này giúp chúng ta phân biệt rõ ràng giữa tính lồi (convex) và tính lồi ngặt (strictly convex) — nền tảng sẽ được phát triển toàn diện trong Bài 01.
:::

---

## Tóm tắt cốt lõi

1. **Biểu diễn ma trận**: Gom dữ liệu thành ma trận $A \in \mathbb{R}^{m \times n}$ giúp tính toán đồng thời mọi dự đoán $Aw$ và phần dư $r = Aw - b$, khai phóng sức mạnh xử lý song song của phần cứng AI.
2. **Gradient và Hướng giảm**: Gradient của hàm mất mát tổng bình phương là $\nabla f(w) = A^T(Aw - b)$. Di chuyển ngược chiều gradient là kim chỉ nam để tối ưu hóa tham số.
3. **Hessian và Độ cong**: Ma trận đạo hàm bậc hai $H = A^TA$ luôn nửa xác định dương ($H \succeq 0$), bảo đảm địa hình tối ưu luôn là một mặt paraboloid lồi hướng lên trên. Khi $A$ đủ hạng cột, nghiệm cực tiểu là duy nhất.
4. **Cội nguồn xác suất**: Tiêu chuẩn bình phương tối thiểu chính là hệ quả toán học trực tiếp của nguyên lý Cực đại hóa hợp lý (MLE) khi sai số tuân theo phân phối chuẩn Gauss.

---

## Tài liệu tham khảo và Đọc thêm

Dành cho bạn đọc muốn đào sâu nền tảng toán học đằng sau các thuật toán học máy:
- **Stephen Boyd & Lieven Vandenberghe**, *Convex Optimization*, Cambridge University Press. Đọc kỹ Phụ lục A về đại số tuyến tính, hình học giải tích và vi phân ma trận, cùng Chương 1.2 về mô hình hóa bài toán bình phương tối thiểu.
- **Daphne Koller & Nir Friedman**, *Probabilistic Graphical Models: Principles and Techniques*, MIT Press. Tham khảo về phân phối xác suất đa biến, tính độc lập thống kê và nguyên lý ước lượng hợp lý cực đại.

Tiếp theo: [Bài 01 — Nhập môn tối ưu hóa, Tập lồi và Hàm lồi](./bai-01-nhap-mon-toi-uu.md).
