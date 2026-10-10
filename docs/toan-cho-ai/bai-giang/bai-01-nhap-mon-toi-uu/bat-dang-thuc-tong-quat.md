---
course: toan-cho-ai
lecture: bai-01-nhap-mon-toi-uu
topic: bat-dang-thuc-tong-quat
section: topic
title: "Nón chính quy và bất đẳng thức tổng quát"
description: "Bốn điều kiện của nón chính quy và vai trò của từng điều kiện, bất đẳng thức tổng quát x ⪯_K y, các ví dụ theo từng thành phần, thứ tự ma trận và đa thức không âm, các tính chất còn giữ và tính chất bị mất, phần tử nhỏ nhất và phần tử tối thiểu."
---

Trên trục số, hai số bất kỳ luôn so sánh được: Hoặc $a \le b$, hoặc $b \le a$. Thói quen này mạnh đến mức ta ít khi nghĩ về nó. Nhưng hãy thử so sánh hai mô hình học máy, một mô hình có độ chính xác 92% và thời gian dự đoán 30 ms, một mô hình có độ chính xác 89% và thời gian 8 ms. Mô hình nào "tốt hơn"? Không có câu trả lời nếu không nói thêm ta coi trọng tiêu chí nào. Khi đại lượng cần so sánh là một vector, khái niệm "nhỏ hơn" không còn hiển nhiên.

Ta sẽ xây dựng một khái niệm "nhỏ hơn" cho vector và ma trận, dựa hoàn toàn vào hình học của nón. Ý tưởng rất gọn: Chọn một nón $K$ làm "tập các vector không âm", rồi định nghĩa $x \preceq y$ khi $y - x$ không âm theo nghĩa đó. Ta sẽ thấy những điều kiện nào trên nón làm cho phép so sánh hành xử giống phép so sánh trên trục số, và những thói quen nào của trục số phải bỏ. Cuối bài là hai khái niệm nền tảng trong tối ưu đa mục tiêu: Phần tử **nhỏ nhất** và phần tử **tối thiểu**.

## 1. Nón chính quy

> **Định nghĩa.** Một nón $K \subseteq \mathbb{R}^n$ là **nón chính quy** (proper cone) nếu nó thỏa mãn đồng thời bốn điều kiện:
> 1. $K$ lồi.
> 2. $K$ đóng.
> 3. $K$ **đặc** (solid), tức là có phần trong khác rỗng ($\operatorname{int} K \ne \emptyset$).
> 4. $K$ **nhọn** (pointed), tức là không chứa đường thẳng nào đi qua gốc. Tương đương: Nếu $x \in K$ và $-x \in K$ thì $x = 0$.

Mỗi điều kiện có một vai trò hình học xác định trong phép so sánh mà ta sắp xây dựng. Tính lồi bảo đảm việc cộng hai bất đẳng thức cùng chiều luôn hợp lệ. Tính đóng bảo đảm bất đẳng thức được bảo toàn qua phép lấy giới hạn dãy số. Tính đặc bảo đảm tồn tại những cặp phần tử được so sánh ngặt. Tính nhọn bảo đảm nếu $x \preceq y$ và $y \preceq x$ đồng thời xảy ra thì bắt buộc $x = y$. Bảng dưới đây minh họa rõ nét điều gì sẽ xảy ra khi một tập hợp thiếu đi từng điều kiện:

| Nón trong $\mathbb{R}^2$ | Lồi | Đóng | Đặc | Nhọn |
| --- | --- | --- | --- | --- | --- |
| Góc phần tư $\mathbb{R}^2_+$ | Có | Có | Có | Có |
| Tia $\{(u, 0) : u \ge 0\}$ | Có | Có | Không | Có |
| Nửa mặt phẳng $\{(u, v) : v \ge 0\}$ | Có | Có | Có | Không |
| $\{0\} \cup \{(u, v) : u > 0,\ v > 0\}$ | Có | Không | Có | Có |
| Hợp hai trục tọa độ | Không | Có | Không | Không |

Để không bao giờ nhầm lẫn ở bước này, ta chú ý quan sát: Tia trong mặt phẳng không chứa bất kỳ hình tròn mở nào nên thiếu tính đặc, dù nó vẫn có nội tương đối. Nửa mặt phẳng thiếu tính nhọn vì chứa trọn vẹn cả trục hoành là một đường thẳng đi qua gốc tọa độ. Tập hợp thứ tư không đóng vì thiếu hai nửa trục dương là các điểm giới hạn của dãy điểm trong tập.

## 2. Bất đẳng thức tổng quát

> **Định nghĩa.** Với một nón chính quy $K$, **bất đẳng thức tổng quát** $\preceq_K$ được định nghĩa bởi:
> $$x \preceq_K y \iff y - x \in K .$$
> Bất đẳng thức **chặt** (ngặt) $\prec_K$ được định nghĩa bởi:
> $$x \prec_K y \iff y - x \in \operatorname{int} K .$$

Ta cũng viết $y \succeq_K x$ thay cho $x \preceq_K y$. Khi $K = \mathbb{R}_+$, nón các số thực không âm trên trục số, quan hệ $\preceq_K$ trùng khớp hoàn toàn với phép so sánh $\le$ quen thuộc và $\prec_K$ chính là $<$. Như vậy bất đẳng thức tổng quát bao hàm bất đẳng thức số học thông thường như một trường hợp đặc biệt.

Định nghĩa này sở hữu một trực giác hình học trực quan: Biểu thức $x \preceq_K y$ đồng nghĩa với việc điểm $y$ nằm trong nón $K$ được tịnh tiến tới đỉnh $x$, tức là $y \in x + K$. Với $K = \mathbb{R}^2_+$, tập $x + K$ chính là góc phần tư phía trên bên phải xuất phát từ đỉnh $x$, do đó $x \preceq y$ mang ý nghĩa "$y$ nằm chếch về phía trên và bên phải của $x$".

Ba ví dụ kinh điển về bất đẳng thức tổng quát:

- **Thứ tự theo từng thành phần**: Với $K = \mathbb{R}^n_+$, biểu thức $x \preceq_K y$ nghĩa là $x_i \le y_i$ với mọi chỉ số $i = 1, \dots, n$, còn $x \prec_K y$ nghĩa là $x_i < y_i$ với mọi $i$. Thứ tự này xuất hiện liên tục trong tối ưu hóa và máy học đến mức ta thường lược bỏ chỉ số $K$ và viết gọn là $x \preceq y$, như trong hệ ràng buộc đa diện $Ax \preceq b$.
- **Thứ tự ma trận (thứ tự Loewner)**: Với $K = \mathbb{S}^n_+$, biểu thức $X \preceq Y$ nghĩa là hiệu $Y - X$ là ma trận nửa xác định dương, còn $X \prec Y$ nghĩa là $Y - X$ xác định dương. Phần trong của $\mathbb{S}^n_+$ trong không gian vector các ma trận đối xứng $\mathbb{S}^n$ chính là nón $\mathbb{S}^n_{++}$, nên hai định nghĩa hoàn toàn tương thích.
- **Đa thức không âm**: Xét tập hợp các vector hệ số của những đa thức không âm trên đoạn $[0, 1]$:

  $$
  K = \{c \in \mathbb{R}^n : c_1 + c_2 t + \cdots + c_n t^{n-1} \ge 0 \text{ với mọi } t \in [0, 1]\}.
  $$

  Đây là một nón chính quy, và quan hệ $c \preceq_K d$ khẳng định đa thức ứng với $c$ không vượt quá giá trị của đa thức ứng với $d$ tại mọi điểm trên $[0, 1]$. Nón $K$ chứa cả những vector có thành phần âm: Chẳng hạn $c = (1, -1)$ sinh ra đa thức $1 - t \ge 0$ với mọi $t \in [0, 1]$.

Một lưu ý bản chất về thứ tự ma trận: Thứ tự ma trận không phải là phép so sánh theo từng phần tử số học. Với $X = I$ và $Y = \begin{bmatrix} 2 & -1 \\ -1 & 2 \end{bmatrix}$, ta có $Y - X = \begin{bmatrix} 1 & -1 \\ -1 & 1 \end{bmatrix} \succeq 0$, do đó $X \preceq Y$, cho dù phần tử ở vị trí $(1, 2)$ của $X$ là $0$, vẫn lớn hơn $-1$ của $Y$. Ý nghĩa chuẩn xác của $X \preceq Y$ là dạng toàn phương $z^T X z \le z^T Y z$ với **mọi** hướng vector $z \in \mathbb{R}^n$.

## 3. Những tính chất còn giữ được

Bất đẳng thức tổng quát thừa hưởng một hệ thống tính chất đại số và giải tích phong phú từ bốn điều kiện của nón chính quy. Với quan hệ $\preceq_K$:

- Tính cộng được: Nếu $x \preceq_K y$ và $u \preceq_K v$ thì $x + u \preceq_K y + v$.
- Tính bắc cầu: Nếu $x \preceq_K y$ và $y \preceq_K z$ thì $x \preceq_K z$.
- Nhân với đại lượng vô hướng không âm: Nếu $x \preceq_K y$ và $\alpha \ge 0$ thì $\alpha x \preceq_K \alpha y$.
- Tính phản xạ: Ta luôn có $x \preceq_K x$ với mọi $x$.
- Tính phản đối xứng: Nếu $x \preceq_K y$ và $y \preceq_K x$ thì bắt buộc $x = y$.
- Tính bảo toàn qua giới hạn: Nếu các dãy thỏa mãn $x_i \preceq_K y_i$ với mọi $i$, đồng thời $x_i \to x$ và $y_i \to y$ khi $i \to \infty$, thì $x \preceq_K y$.

Mỗi tính chất nêu trên đều được chứng minh trực tiếp từ một điều kiện cấu thành nên nón chính quy. Tính cộng được và tính bắc cầu bắt nguồn từ việc nón $K$ khép kín với phép cộng: Cụ thể là $(y - x) + (v - u) \in K$ và $(z - y) + (y - x) \in K$. Tính phản xạ xuất phát từ sự kiện $0 \in K$. Tính phản đối xứng đòi hỏi tính nhọn: Cả $y - x \in K$ lẫn $x - y \in K$ buộc hiệu $y - x$ phải bằng $0$. Tính bảo toàn qua giới hạn được đảm bảo nhờ tính đóng của $K$. Bất đẳng thức chặt cũng sở hữu các tính chất tương tự, chẳng hạn $x \prec_K y$ và $u \preceq_K v$ kéo theo $x + u \prec_K y + v$, và quan trọng hơn: Nếu $x \prec_K y$ thì với mọi nhiễu $u, v$ đủ nhỏ, ta vẫn duy trì được $x + u \prec_K y + v$. Tính chất này khẳng định bất đẳng thức chặt luôn bền vững trước các dao động nhỏ, bắt nguồn từ việc phần trong $\operatorname{int} K$ là một tập mở.

## 4. Thói quen phải bỏ: Không phải mọi cặp đều so sánh được

Trên trục số thực, hai số bất kỳ luôn so sánh được với nhau, tạo thành một **thứ tự toàn phần** (linear order). Trái lại, bất đẳng thức tổng quát trên không gian nhiều chiều nói chung chỉ là một **thứ tự bộ phận** (partial order): Tồn tại những cặp phần tử không thể so sánh được với nhau. Với $K = \mathbb{R}^2_+$, xét hai vector $x = (1, 4)$ và $y = (2, 3)$, ta nhận thấy $y - x = (1, -1) \notin \mathbb{R}^2_+$ và $x - y = (-1, 1) \notin \mathbb{R}^2_+$, do đó không có $x \preceq y$ mà cũng chẳng có $y \preceq x$.

Đây không phải là một khiếm khuyết toán học, mà là sự phản ánh trung thực bản chất đa chiều của thế giới thực. Xét ví dụ ở đầu bài về hai mô hình phân lớp với vector "(tỷ lệ lỗi, độ trễ)": Một mô hình là $(8\%, 30\text{ ms})$ và mô hình kia là $(11\%, 8\text{ ms})$. Rõ ràng hai mô hình không thể so sánh hơn kém một cách tuyệt đối nếu không áp đặt một hàm mục tiêu tổng hợp.

Hệ quả cốt lõi của tính thứ tự bộ phận là khái niệm "giá trị nhỏ nhất" phân rã thành hai khái niệm hoàn toàn riêng biệt.

## 5. Phần tử nhỏ nhất và phần tử tối thiểu

> **Định nghĩa.** Cho tập hợp $S$ và một bất đẳng thức tổng quát $\preceq_K$.
> - Điểm $x \in S$ là **phần tử nhỏ nhất** (minimum element) của $S$ nếu $x \preceq_K y$ với mọi phần tử $y \in S$.
> - Điểm $x \in S$ là **phần tử tối thiểu** (minimal element) của $S$ nếu với mọi $y \in S$, điều kiện $y \preceq_K x$ chỉ xảy ra khi $y = x$.

Để phân biệt rõ ràng hai khái niệm: Phần tử nhỏ nhất phải áp đảo và "nhỏ hơn hoặc bằng" **mọi** phần tử còn lại trong tập hợp. Trong khi đó, phần tử tối thiểu chỉ cần **không bị phần tử nào khác nhỏ hơn nó** (không ai đánh bại được nó). Do đó, phần tử nhỏ nhất nếu tồn tại thì luôn là duy nhất (nhờ tính phản đối xứng), còn phần tử tối thiểu thì có thể có rất nhiều, thậm chí vô số.

Hai khái niệm này có biểu diễn hình học rất sáng sủa:

$$
\begin{aligned}
x \text{ là phần tử nhỏ nhất} &\iff S \subseteq x + K, \\
x \text{ là phần tử tối thiểu} &\iff (x - K) \cap S = \{x\}.
\end{aligned}
$$

Tập $x + K$ bao gồm mọi điểm lớn hơn hoặc bằng $x$, nên điều kiện thứ nhất diễn giải rằng: Toàn bộ tập $S$ nằm trọn vẹn ở phía trên hình nón xuất phát từ $x$. Tập $x - K$ bao gồm mọi điểm nhỏ hơn hoặc bằng $x$, do đó điều kiện thứ hai khẳng định: Phía dưới $x$ không còn chứa bất kỳ điểm nào khác của $S$. Khi xét $K = \mathbb{R}_+$ trên trục số, hai khái niệm này hợp nhất làm một và trở về giá trị nhỏ nhất thông thường.

<OrderLab type="order" />

Trong mô phỏng tương tác trên, mỗi điểm đại diện cho một phương án thiết kế hệ thống với hai tiêu chí đánh giá đều cần tối thiểu hóa. Các điểm $A, B, C, F$ là các phần tử tối thiểu: Không tồn tại phương án nào khác vượt trội hơn chúng ở cả hai chỉ số đồng thời. Các điểm $D, E, G$ bị các điểm khác chi phối (bị trội). Tập hợp này không có phần tử nhỏ nhất, bởi vì không có phương án duy nhất nào vừa đạt độ trễ thấp nhất lại vừa có tỷ lệ lỗi nhỏ nhất. Trong bài toán tối ưu đa mục tiêu (multi-objective optimization), các phần tử tối thiểu được gọi là **nghiệm tối ưu Pareto**, và quỹ tích của chúng hợp thành **biên Pareto** (Pareto frontier).

Khi ta thay đổi độ mở của nón trong mô phỏng: Nếu nón hẹp lại, số cặp điểm so sánh được sẽ giảm đi, dẫn đến số lượng phần tử tối thiểu tăng lên. Ngược lại, khi nón mở rộng ra, nhiều cặp điểm trở nên so sánh được, số phần tử tối thiểu giảm dần, và có thể dẫn tới sự xuất hiện của một phần tử nhỏ nhất duy nhất.

Xét một mô hình hình học trực quan về thứ tự ma trận thông qua các tập ellipsoid: Mỗi ma trận đối xứng xác định dương $A \succ 0$ tương ứng với một hình ellipsoid có tâm tại gốc tọa độ $\mathcal{E}_A = \{x \in \mathbb{R}^n : x^T A^{-1} x \le 1\}$. Người ta chứng minh được rằng $A \preceq B$ khi và chỉ khi $\mathcal{E}_A \subseteq \mathcal{E}_B$. Giả sử ta xét tập $S$ gồm các ma trận sinh ra những ellipsoid bao quanh một tập điểm dữ liệu cho trước trong bài toán bọc dữ liệu. Tập hợp này không tồn tại phần tử nhỏ nhất, bởi vì hai hình ellipsoid cùng bao bọc tập điểm có thể mở rộng theo các hướng vuông góc nhau mà không hình nào chứa trọn hình nào. Một ellipsoid được gọi là tối thiểu nếu không tồn tại ellipsoid nào khác trong họ vừa bao bọc tập điểm lại vừa nằm lọt thỏm bên trong nó.

## 6. Những câu hỏi để đào sâu

**Câu 1.** Trong $\mathbb{R}^2$ với thứ tự theo từng thành phần, tập $S_1 = \{(u, v) : u \ge 1,\ v \ge 2\}$ có phần tử nhỏ nhất không? Tập $S_2 = \{(u, v) : u + v \ge 4,\ u \ge 0,\ v \ge 0\}$ thì sao?

<details><summary>Xem lời giải thích</summary>

Tập $S_1$ có phần tử nhỏ nhất là $(1, 2)$, bởi vì mọi điểm $(u, v) \in S_1$ đều thỏa mãn $u \ge 1$ và $v \ge 2$, tức là nằm trọn trong $(1, 2) + \mathbb{R}^2_+$. Điểm này cũng là phần tử tối thiểu duy nhất của tập. Ngược lại, tập $S_2$ không có phần tử nhỏ nhất, vì hai điểm $(4, 0)$ và $(0, 4)$ đều thuộc $S_2$ nhưng không tồn tại điểm nào trong $S_2$ nhỏ hơn hoặc bằng cả hai (điểm như vậy buộc phải có $u \le 0$ và $v \le 0$). Mọi điểm trên đoạn thẳng $\{u + v = 4,\ u \ge 0,\ v \ge 0\}$ đều là phần tử tối thiểu. Chẳng hạn điểm $(2, 2)$ là tối thiểu vì bất kỳ điểm $(u, v) \in S_2$ thỏa mãn $(u, v) \preceq (2, 2)$ đều dẫn đến $u + v \le 4$, kết hợp với điều kiện $u + v \ge 4$ suy ra $u = 2$ và $v = 2$.

</details>

**Câu 2.** Thuật ngữ "tối thiểu" dễ khiến người học liên tưởng đến "cực tiểu địa phương" (local minimum). Hai khái niệm này khác nhau như thế nào về bản chất?

<details><summary>Xem lời giải thích</summary>

Khái niệm phần tử tối thiểu hoàn toàn không phụ thuộc vào khái niệm lân cận hay khoảng cách metric. Nó được xác định thông qua việc so sánh trên **toàn bộ** tập hợp, nhưng dựa trên một thứ tự bộ phận, do đó nhiều phần tử có thể đồng thời cùng không bị bất kỳ phần tử nào khác chi phối. Trong khi đó, cực tiểu địa phương là khái niệm giải tích so sánh giá trị hàm số với các điểm nằm trong một hình cầu lân cận. Vì vậy thuật ngữ tiếng Anh "minimal element" không bao giờ được hiểu là cực tiểu địa phương.

</details>

**Câu 3.** Vì sao điều kiện "nhọn" lại mang tính quyết định đối với tính phản đối xứng? Hãy tìm hai vector phân biệt $x \ne y$ thỏa mãn cả $x \preceq_K y$ lẫn $y \preceq_K x$ khi $K$ là nửa mặt phẳng $\{(u, v) : v \ge 0\}$.

<details><summary>Xem lời giải thích</summary>

Chọn $x = (0, 0)$ và $y = (1, 0)$. Ta nhận thấy hiệu $y - x = (1, 0) \in K$ và $x - y = (-1, 0) \in K$, bởi vì cả hai vector đều có tung độ $v = 0 \ge 0$. Do đó ta có đồng thời $x \preceq_K y$ và $y \preceq_K x$ dù $x \ne y$. Nguyên nhân là nửa mặt phẳng chứa toàn bộ trục hoành, vốn là một đường thẳng đi qua gốc tọa độ. Theo phương của đường thẳng này, khái niệm "lớn hơn" và "nhỏ hơn" bị triệt tiêu sự phân định. Điều kiện nón nhọn chính là rào cản ngăn chặn triệt để hiện tượng suy biến này.

</details>

**Câu 4.** Với thứ tự ma trận, tập hợp $\{X \in \mathbb{S}^2 : X \succeq I\}$ có phần tử nhỏ nhất không? Tập hợp $\{X \in \mathbb{S}^2 : X_{11} \ge 1,\ X_{22} \ge 1\}$ thì sao?

<details><summary>Xem lời giải thích</summary>

Tập thứ nhất có phần tử nhỏ nhất là ma trận đơn vị $I$, vì theo đúng định nghĩa mọi phần tử $X$ của tập đều thỏa mãn $I \preceq X$. Tập thứ hai không tồn tại phần tử nhỏ nhất. Nó chứa các ma trận dạng $\begin{bmatrix} 1 & a \\ a & 1 \end{bmatrix}$ với mọi tham số $a \in \mathbb{R}$. Một phần tử nhỏ nhất giả định $M$ phải thỏa mãn $M \preceq \begin{bmatrix} 1 & a \\ a & 1 \end{bmatrix}$ với mọi $a$. Chọn vector thử $z = (1, -1)^T$, điều kiện trên đòi hỏi $z^T M z \le 2 - 2a$ phải đúng với mọi số thực $a$, điều này bất khả thi khi $a$ nhận giá trị dương tùy ý lớn. Ràng buộc cục bộ trên các phần tử đường chéo là không đủ mạnh để tạo ra một cận dưới toàn cục theo thứ tự ma trận.

</details>

## 7. Bài tập tự luyện

::: exercise 1. Kiểm tra nón chính quy
Tập $K = \{(x_1, x_2) : x_1 \ge |x_2|\}$ có phải là nón chính quy không? Với thứ tự $\preceq_K$, hãy so sánh hai vector $x = (1, 0)$ và $y = (3, 1)$.
:::

::: solution
Tập $K$ là giao của hai nửa mặt phẳng đóng $x_1 - x_2 \ge 0$ và $x_1 + x_2 \ge 0$ có bờ đi qua gốc tọa độ, do đó $K$ là một nón lồi và đóng. Điểm $(1, 0)$ chứa một hình tròn mở bán kính $\tfrac12$ nằm trọn trong $K$, chứng tỏ $K$ có điểm trong, tức là $K$ đặc. Nếu $x \in K$ và $-x \in K$ thì $x_1 \ge |x_2|$ và $-x_1 \ge |x_2|$, cộng vế theo vế ta được $0 \ge 2|x_2|$, kéo theo $x_2 = 0$, từ đó suy ra $x_1 = 0$. Như vậy $K$ nhọn, và là một nón chính quy hợp thức.

Với hai điểm $x = (1, 0)$ và $y = (3, 1)$: Ta có hiệu $y - x = (2, 1)$. Vì $2 \ge |1| = 1$ nên $y - x \in K$, dẫn tới $x \preceq_K y$. Thậm chí vì $2 > 1$ nên $y - x \in \operatorname{int} K$, do đó ta có bất đẳng thức chặt $x \prec_K y$.
:::

::: exercise 2. Phần tử tối thiểu của một tập hữu hạn
Với thứ tự theo từng thành phần trong $\mathbb{R}^2$, hãy tìm toàn bộ phần tử tối thiểu và phần tử nhỏ nhất (nếu có) của tập hợp gồm sáu điểm sau:

$$
S = \{(3, 5),\ (4, 2),\ (2, 6),\ (5, 1),\ (4, 4),\ (6, 6)\}.
$$
:::

::: solution
Điểm $(4, 4)$ bị điểm $(4, 2)$ chi phối vì $(4, 2) \preceq (4, 4)$ và hai điểm phân biệt. Điểm $(6, 6)$ bị chi phối bởi nhiều điểm khác trong tập, chẳng hạn như $(3, 5)$. Bốn điểm còn lại gồm $(3, 5)$, $(4, 2)$, $(2, 6)$, $(5, 1)$ không bị bất kỳ điểm nào khác trong $S$ vượt trội, do đó chúng hợp thành tập các phần tử tối thiểu.

Tập $S$ không tồn tại phần tử nhỏ nhất, vì hai điểm $(2, 6)$ và $(5, 1)$ không so sánh được với nhau nhưng đều thuộc $S$: Một phần tử nhỏ nhất nếu tồn tại bắt buộc phải nhỏ hơn hoặc bằng cả hai điểm này, tức là phải có hoành độ không vượt quá 2 và tung độ không vượt quá 1, nhưng trong $S$ không có bất kỳ điểm nào thỏa mãn tiêu chí đó.
:::

## Tóm tắt

Một nón chính quy là nón lồi, đóng, có phần trong khác rỗng và không chứa đường thẳng đi qua gốc tọa độ. Nó thiết lập bất đẳng thức tổng quát $x \preceq_K y \iff y - x \in K$, với phiên bản bất đẳng thức chặt sử dụng phần trong của nón. Thứ tự theo từng thành phần, thứ tự ma trận nửa xác định dương và thứ tự giữa các đa thức không âm trên một đoạn đều là những trường hợp áp dụng kinh điển. Bất đẳng thức tổng quát bảo toàn trọn vẹn các tính chất đại số quen thuộc như tính cộng, bắc cầu, nhân vô hướng không âm, phản xạ, phản đối xứng và tính đóng qua giới hạn.

Điểm khác biệt căn bản so với trục số thực là tính thứ tự bộ phận: Các phần tử nhiều chiều có thể không so sánh được với nhau. Do đó, khái niệm "nhỏ nhất" phân rã thành phần tử nhỏ nhất (đánh bại toàn bộ tập hợp, duy nhất nếu tồn tại) và phần tử tối thiểu (không bị phần tử nào đánh bại, có thể xuất hiện nhiều phần tử cùng lúc). Trong tối ưu hóa đa mục tiêu, các phần tử tối thiểu định nghĩa chính xác tập nghiệm tối ưu Pareto.

## Tài liệu tham khảo
- Stephen Boyd, Lieven Vandenberghe, *Convex Optimization*, Cambridge University Press.

