---
course: toan-cho-ai
lecture: bai-01-nhap-mon-toi-uu
topic: sieu-phang-phan-tach-va-tua
section: topic
title: "Siêu phẳng phân tách và siêu phẳng tựa"
description: "Định lý siêu phẳng phân tách và chứng minh bằng cặp điểm gần nhất, phân tách nghiêm ngặt, tập lồi đóng là giao các nửa không gian chứa nó, định lý lựa chọn cho hệ bất đẳng thức chặt, siêu phẳng tựa, và ý nghĩa với phân loại tuyến tính."
---

Hãy đặt hai hòn đá lồi, chẳng hạn hai viên sỏi tròn, lên mặt bàn sao cho chúng không chạm nhau. Bạn luôn có thể luồn một tờ giấy phẳng vào giữa để ngăn chúng ra. Nhưng nếu một hòn đá có hình lưỡi liềm ôm lấy hòn kia, thì không tờ giấy phẳng nào làm được việc đó, dù hai hòn đá vẫn không chạm nhau. Điều khác biệt giữa hai tình huống chính là tính lồi.

Định lý siêu phẳng phân tách biến trực giác ấy thành một mệnh đề chính xác, và nó là một trong những kết quả quan trọng nhất của toàn bộ chương. Lý thuyết đối ngẫu ở Lecture 03, điều kiện tối ưu KKT, bổ đề Farkas, các định lý lựa chọn, và cả câu hỏi "khi nào dữ liệu phân loại được bằng một đường thẳng" đều là hệ quả của nó, theo cách này hay cách khác. Ta phát biểu định lý, chứng minh nó trong trường hợp dễ hình dung nhất, rồi rút ra những hệ quả quan trọng.

## 1. Định lý siêu phẳng phân tách

> **Định lý.** Cho $C$ và $D$ là hai tập lồi khác rỗng, rời nhau ($C \cap D = \varnothing$). Khi đó tồn tại $a \ne 0$ và $b$ sao cho
> $$a^T x \le b \ \text{ với mọi } x \in C, \qquad a^T x \ge b \ \text{ với mọi } x \in D.$$

Nói cách khác, hàm affine $a^T x - b$ không dương trên $C$ và không âm trên $D$. Siêu phẳng $\{x : a^T x = b\}$ được gọi là **siêu phẳng phân tách** của $C$ và $D$: Hai tập nằm ở hai phía của nó, có thể chạm vào nó nhưng không vượt qua.

Đọc kỹ phát biểu, có ba điều đáng để ý. Thứ nhất, cả hai tập đều phải lồi: Hình lưỡi liềm ở đầu trang cho thấy thiếu tính lồi thì định lý sai. Thứ hai, kết luận dùng dấu $\le$ và $\ge$ chứ không phải dấu chặt, nên hai tập có thể cùng chạm siêu phẳng. Thứ ba, định lý chỉ khẳng định **tồn tại**, không nói siêu phẳng là duy nhất hay cách tìm nó. Tuy vậy, chứng minh dưới đây lại cho một cách dựng rất cụ thể.

<SeparationLab type="sets" />

## 2. Chứng minh khi có cặp điểm gần nhất

Sách chứng minh định lý trong một trường hợp đặc biệt, rồi để phần tổng quát làm bài tập. Giả sử khoảng cách Euclid giữa hai tập,

$$
\operatorname{dist}(C, D) = \inf\{\|u - v\|_2 : U \in C,\ v \in D\},
$$

là dương, và có hai điểm $c \in C$, $d \in D$ đạt khoảng cách đó: $\|c - d\|_2 = \operatorname{dist}(C, D)$. Điều kiện này đúng chẳng hạn khi $C$ và $D$ đóng và một trong hai tập bị chặn.

**Dựng siêu phẳng.** Đặt $a = d - c$ và $b = \tfrac{\|d\|_2^2 - \|c\|_2^2}{2}$. Hàm affine tương ứng là

$$
f(x) = a^T x - b = (d - c)^T \left(x - \tfrac12(d + c)\right).
$$

Siêu phẳng $f(x) = 0$ vuông góc với đoạn $[c, d]$ và đi qua trung điểm của nó, tức là **đường trung trực** của đoạn nối hai điểm gần nhất. Trong mô phỏng, đó là đường màu tím.

**Chứng minh $f \ge 0$ trên $D$.** Giả sử ngược lại, có $u \in D$ với $f(u) < 0$. Viết lại

$$
f(u) = (d - c)^T(u - d) + \tfrac12 \|d - c\|_2^2 ,
$$

nên $f(u) < 0$ kéo theo $(d - c)^T(u - d) < 0$. Bây giờ xét điểm $d + t(u - d)$ trên đoạn nối $d$ với $u$. Đạo hàm của bình phương khoảng cách từ điểm đó tới $c$ tại $t = 0$ là

$$
\frac{d}{dt}\, \|d + t(u - d) - c\|_2^2 \Big|_{t=0} = 2(d - c)^T(u - d) < 0 .
$$

Đạo hàm âm nghĩa là khi đi một chút từ $d$ về phía $u$, ta tiến gần $c$ hơn. Với $t > 0$ đủ nhỏ (và $t \le 1$), điểm $d + t(u - d)$ gần $c$ hơn $d$. Nhưng $D$ lồi và chứa $d$, $u$, nên điểm đó thuộc $D$. Điều này mâu thuẫn với việc $d$ là điểm của $D$ gần $C$ nhất. Phần $f \le 0$ trên $C$ chứng minh tương tự, bằng cách đổi vai trò $C$ và $D$.

Hãy để ý chính xác chỗ dùng tính lồi: Điểm $d + t(u - d)$ phải thuộc $D$. Nếu $D$ không lồi, có thể có một điểm $u \in D$ nằm "vòng ra phía trước" siêu phẳng mà đoạn nối $d$ với $u$ lại rời khỏi $D$. Đó đúng là tình huống hình lưỡi liềm. Chứng minh tổng quát, khi cặp điểm gần nhất không tồn tại, dùng một mẹo khác: Tập $C - D = \{x - y : x \in C,\ y \in D\}$ lồi và không chứa 0, nên chỉ cần tách 0 khỏi một tập lồi (Bài tập 2.22 trong sách).

## 3. Khi nào tách được một cách nghiêm ngặt

Siêu phẳng dựng ở mục 2 thật ra thỏa điều kiện mạnh hơn: $a^T x < b$ trên $C$ và $a^T x > b$ trên $D$. Ta gọi đó là **phân tách nghiêm ngặt**. Nhưng không phải cặp tập lồi rời nhau nào cũng tách nghiêm ngặt được, kể cả khi cả hai đều đóng (Bài tập 2.23 trong sách). Chẳng hạn trong $\mathbb{R}^2$, lấy

$$
C = \{(x_1, x_2) : X_2 \le 0\}, \qquad D = \{(x_1, x_2) : X_1 > 0,\ x_1 x_2 \ge 1\}.
$$

Cả hai tập đều lồi, đóng và rời nhau. Nhưng khi $x_1 \to \infty$, các điểm $(x_1, 1/x_1)$ của $D$ tiến sát trục hoành tùy ý, nên khoảng cách giữa hai tập bằng 0. Đường thẳng duy nhất tách chúng là trục hoành, và nó chạm $C$, nên không tách nghiêm ngặt. Ở đây cặp điểm gần nhất không tồn tại, nên chứng minh ở mục 2 không áp dụng được.

Trường hợp quan trọng nhất có phân tách nghiêm ngặt là **một điểm và một tập lồi đóng** (Ví dụ 2.20). Nếu $C$ lồi, đóng và $x_0 \notin C$, thì có một hình cầu nhỏ $B(x_0, \varepsilon)$ không giao $C$, và tách hình cầu đó khỏi $C$ cho ta một siêu phẳng tách nghiêm ngặt $x_0$ khỏi $C$.

Từ đó suy ra một kết quả mà ta đã hứa từ chủ đề về các phép toán giữ tính lồi: **Mọi tập lồi đóng $C$ đều là giao của tất cả các nửa không gian chứa nó**. Thật vậy, gọi $S$ là giao đó. Hiển nhiên $C \subseteq S$. Nếu có $x \in S$ mà $x \notin C$, thì có một nửa không gian chứa $C$ nhưng không chứa $x$, nên $x \notin S$, mâu thuẫn. Kết quả này là cơ sở của một ý tưởng xuyên suốt môn học: Một tập lồi đóng được mô tả hoàn toàn bởi các bất đẳng thức tuyến tính mà nó thỏa. Lý thuyết đối ngẫu, về bản chất, là việc khai thác cách mô tả "từ bên ngoài" này.

## 4. Chiều ngược lại và một định lý lựa chọn

Chiều ngược của định lý phân tách, "có siêu phẳng phân tách thì hai tập rời nhau", sai nếu không thêm điều kiện. Hai tập $C = D = \{0\}$ trong $\mathbb{R}$ được tách bởi siêu phẳng $x = 0$ (cả hai đều nằm trên nó), nhưng chúng trùng nhau. Tuy nhiên, nếu một trong hai tập là **mở**, chiều ngược đúng. Lý do: Một hàm affine không dương trên tập mở $C$ phải âm trên $C$, vì nếu nó bằng 0 tại một điểm của $C$ thì nó dương tại những điểm lân cận theo hướng $a$. Ghép lại, sách có kết quả: Hai tập lồi, ít nhất một tập mở, rời nhau **khi và chỉ khi** có siêu phẳng phân tách.

Kết quả này cho một ứng dụng đẹp (Ví dụ 2.21). Hệ bất đẳng thức tuyến tính chặt $Ax \prec b$, với $A \in \mathbb{R}^{m \times n}$, vô nghiệm khi và chỉ khi tập affine $\{b - Ax : x \in \mathbb{R}^n\}$ không giao với tập mở $\mathbb{R}^m_{++}$. Áp dụng kết quả vừa nêu rồi rút gọn, sách thu được: **$Ax \prec b$ vô nghiệm khi và chỉ khi tồn tại $\lambda \in \mathbb{R}^m$ với**

$$
\lambda \ne 0, \qquad \lambda \succeq 0, \qquad A^T \lambda = 0, \qquad \lambda^T b \le 0 .
$$

Hai hệ này được gọi là một **cặp lựa chọn** (alternatives): Với mọi dữ liệu $A, b$, đúng một trong hai hệ có nghiệm. Ý nghĩa thực tế rất lớn. Muốn chứng minh một hệ bất đẳng thức **vô nghiệm**, ta không cần thử mọi $x$. Chỉ cần đưa ra một vector $\lambda$ thỏa hệ lựa chọn, một "giấy chứng nhận" mà ai cũng kiểm tra được bằng vài phép nhân.

::: example Một chứng nhận vô nghiệm nhỏ
Hệ $x < 1$ và $-x < -1$ (tức $x > 1$) rõ ràng vô nghiệm. Viết dưới dạng $Ax \prec b$ với $A = \begin{bmatrix} 1 \\ -1 \end{bmatrix}$ và $b = (1, -1)$. Vector $\lambda = (1, 1)$ thỏa $\lambda \ne 0$, $\lambda \succeq 0$, $A^T \lambda = 1 - 1 = 0$ và $\lambda^T b = 1 - 1 = 0 \le 0$. Cách đọc chứng nhận: Cộng hai bất đẳng thức với trọng số $\lambda$ được $\lambda^T A x < \lambda^T b$, tức $0 < 0$, một mâu thuẫn. Mọi chứng nhận vô nghiệm theo kiểu này đều làm đúng một việc: Tìm một tổ hợp không âm của các bất đẳng thức để vế trái triệt tiêu còn vế phải không dương.
:::

## 5. Siêu phẳng tựa

Định lý phân tách có một "người anh em" dành cho một tập và một điểm trên biên của nó.

> **Định nghĩa.** Cho $C \subseteq \mathbb{R}^n$ và $x_0$ thuộc biên của $C$. Nếu có $a \ne 0$ sao cho $a^T x \le a^T x_0$ với mọi $x \in C$, thì siêu phẳng $\{x : a^T x = a^T x_0\}$ được gọi là **siêu phẳng tựa** của $C$ tại $x_0$.

Về hình học, siêu phẳng tựa đi qua $x_0$ và để cả tập $C$ ở một phía, giống như một tấm thước kê sát mép một vật mà không cắt vào nó. Khi biên trơn tại $x_0$, siêu phẳng tựa chính là tiếp tuyến. Khi $x_0$ là một góc nhọn, có cả một chùm siêu phẳng tựa.

> **Định lý siêu phẳng tựa.** Nếu $C$ lồi và khác rỗng, thì tại mọi điểm $x_0$ trên biên của $C$ đều có ít nhất một siêu phẳng tựa.

Chứng minh suy ra từ định lý phân tách, theo hai trường hợp. Nếu phần trong của $C$ khác rỗng, tách tập lồi $\{x_0\}$ khỏi tập lồi $\operatorname{int} C$ (chúng rời nhau vì $x_0$ nằm trên biên). Nếu phần trong rỗng, $C$ nằm trong một tập affine có số chiều nhỏ hơn $n$, như ta đã thấy ở chủ đề về nội tương đối, và mọi siêu phẳng chứa tập affine đó là một siêu phẳng tựa "tầm thường". Chiều ngược một phần cũng đúng: Một tập đóng, có phần trong khác rỗng và có siêu phẳng tựa tại mọi điểm biên thì lồi (Bài tập 2.27).

<SeparationLab type="support" />

Siêu phẳng tựa cho một cách giải bài toán tối ưu tuyến tính trên tập lồi. Cực đại $a^T x$ trên $C$ tương đương tìm siêu phẳng tựa với pháp tuyến $a$: Giá trị lớn nhất là $a^T x_0$, đạt tại điểm tựa $x_0$. Chẳng hạn, trên quả cầu Euclid đơn vị, cực đại $x_1 + 2x_2$ đạt tại $x_0 = \tfrac{1}{\sqrt5}(1, 2)$ với giá trị $\sqrt5$. Trên quả cầu $\ell_1$ đơn vị, cực đại $2x_1 + x_2$ đạt tại đỉnh $(1, 0)$ với giá trị $2$. Tại đỉnh ấy, mọi pháp tuyến nằm giữa $(1, 1)$ và $(1, -1)$ đều cho một siêu phẳng tựa, và $(2, 1)$ là một trong số đó. Nhận xét "nghiệm của bài toán tuyến tính nằm ở chỗ siêu phẳng tựa chạm tập" là nền tảng hình học của quy hoạch tuyến tính, và cũng là lý do quả cầu $\ell_1$ cho nghiệm thưa.

## 6. Phân loại tuyến tính nhìn từ định lý phân tách

Cho hai lớp dữ liệu $\{x_1, \ldots, x_N\}$ và $\{y_1, \ldots, y_M\}$. Ta muốn tìm một hàm affine $f(x) = a^T x - b$ dương trên lớp thứ nhất và âm trên lớp thứ hai, tức là một bộ phân loại tuyến tính. Khi nào điều đó làm được? Sách trả lời ở §8.6.1 bằng đúng định lý ta vừa học: **Hai lớp điểm phân biệt được bằng một hàm affine khi và chỉ khi bao lồi của chúng không giao nhau**.

Ví dụ kinh điển cho chiều "không" là bài toán XOR: Lớp thứ nhất gồm $(0, 0)$ và $(1, 1)$, lớp thứ hai gồm $(1, 0)$ và $(0, 1)$. Hai bao lồi là hai đường chéo của hình vuông, cắt nhau tại $(\tfrac12, \tfrac12)$. Điểm chung đó là trung bình của mỗi lớp, và một hàm affine dương trên cả lớp thứ nhất thì cũng dương tại trung bình của chúng, đồng thời âm tại trung bình của lớp thứ hai, mâu thuẫn. Đây là lý do một mô hình tuyến tính không học được XOR, và cần thêm đặc trưng phi tuyến hoặc thêm tầng ẩn.

Khi hai lớp tách được, có vô số đường tách. Sách đề xuất chọn đường có **lề lớn nhất**, tức là dải phân cách dày nhất, và chỉ ra rằng bề rộng tối ưu của dải bằng đúng **khoảng cách giữa hai bao lồi**. Đường tách tốt nhất là đường trung trực của đoạn nối hai điểm gần nhất của hai bao lồi, đúng như cách dựng trong chứng minh ở mục 2. Đó là ý tưởng hình học đằng sau máy vector hỗ trợ (SVM) với lề cứng. Mô phỏng dưới đây cho bạn kéo các điểm dữ liệu và xem đường tách lề lớn nhất thay đổi thế nào.

<SeparationLab type="data" />

Chỉ vài điểm gần ranh giới quyết định vị trí đường tách. Kéo một điểm ở xa ranh giới, đường tách không đổi, chừng nào điểm đó không trở thành một đỉnh của bao lồi nằm gần lớp kia nhất. Những điểm quyết định ấy chính là các "vector hỗ trợ" trong tên gọi của SVM.

## 7. Những câu hỏi để đào sâu

**Câu 1.** Định lý phân tách có đúng nếu chỉ một trong hai tập lồi không? Hãy dựng một phản ví dụ với $C$ lồi và $D$ không lồi.

<details><summary>Xem lời giải thích</summary>

Không đúng. Lấy $C$ là hình tròn đơn vị và $D$ là vành khăn $\{x : 2 \le \|x\|_2 \le 3\}$. Hai tập rời nhau, $C$ lồi còn $D$ thì không. Mọi đường thẳng đi qua hình tròn $C$ hoặc để $C$ ở một phía đều có phần của vành khăn ở cả hai phía, vì vành khăn bao quanh $C$ theo mọi hướng. Vậy không có siêu phẳng phân tách. Định lý cần **cả hai** tập lồi.

</details>

**Câu 2.** Trong chứng minh ở mục 2, nếu thay $a = d - c$ bằng $a = c - d$ thì siêu phẳng có còn tách hai tập không? Vai trò của $C$ và $D$ thay đổi thế nào?

<details><summary>Xem lời giải thích</summary>

Đổi dấu $a$ (và $b$) không đổi siêu phẳng, chỉ đổi chiều của hàm affine: Khi đó $a^T x - b \ge 0$ trên $C$ và $\le 0$ trên $D$. Siêu phẳng vẫn tách, chỉ là "phía dương" đổi sang tập kia. Đây là lý do định lý thường được phát biểu "tồn tại $a \ne 0$" mà không nói $a$ chỉ về phía nào: Hai lựa chọn dấu cho cùng một siêu phẳng.

</details>

**Câu 3.** Có thể có hai tập lồi đóng rời nhau, cả hai đều không bị chặn, mà vẫn tách nghiêm ngặt được không? Ví dụ ở mục 3 cho thấy điều gì là thiếu?

<details><summary>Xem lời giải thích</summary>

Có. Hai nửa mặt phẳng $\{x_2 \le 0\}$ và $\{x_2 \ge 1\}$ đều đóng, không bị chặn, và được tách nghiêm ngặt bởi đường $x_2 = \tfrac12$. Điều thiếu trong ví dụ ở mục 3 không phải tính bị chặn, mà là **khoảng cách dương**: Các điểm của nhánh hyperbol tiến sát trục hoành tùy ý. Khi khoảng cách giữa hai tập dương và có cặp điểm đạt khoảng cách, chứng minh ở mục 2 cho ngay phân tách nghiêm ngặt. Điều kiện "một tập bị chặn" chỉ là một cách thuận tiện để bảo đảm có cặp điểm như vậy.

</details>

**Câu 4.** Trong bài toán XOR, nếu thêm đặc trưng thứ ba $x_3 = x_1 x_2$, hai lớp có tách được bằng một siêu phẳng trong $\mathbb{R}^3$ không? Hãy tìm một siêu phẳng cụ thể.

<details><summary>Xem lời giải thích</summary>

Bốn điểm trở thành $(0, 0, 0)$ và $(1, 1, 1)$ cho lớp thứ nhất, $(1, 0, 0)$ và $(0, 1, 0)$ cho lớp thứ hai. Hàm $f(x) = x_1 + x_2 - 2x_3 - \tfrac12$ cho giá trị $-\tfrac12$ và $-\tfrac12$ trên lớp thứ nhất, $\tfrac12$ và $\tfrac12$ trên lớp thứ hai. Vậy siêu phẳng $x_1 + x_2 - 2x_3 = \tfrac12$ tách hai lớp. Trong không gian đặc trưng mới, hai bao lồi không còn giao nhau. Đây là ý tưởng cơ bản của việc ánh xạ dữ liệu sang không gian đặc trưng lớn hơn trước khi dùng một bộ phân loại tuyến tính.

</details>

## 8. Bài tập tự luyện

::: exercise 1. Dựng siêu phẳng phân tách
Cho hai hình tròn $C = \{x : \|x - (0, 0)\|_2 \le 1\}$ và $D = \{x : \|x - (4, 3)\|_2 \le 2\}$. Tìm cặp điểm gần nhất, rồi viết siêu phẳng phân tách theo cách dựng ở mục 2.
:::

::: hint
Cặp điểm gần nhất nằm trên đoạn nối hai tâm.
:::

::: solution
Hai tâm cách nhau $\sqrt{16 + 9} = 5$, lớn hơn tổng bán kính $3$, nên hai hình tròn rời nhau. Vector đơn vị từ tâm $C$ tới tâm $D$ là $u = (0.8, 0.6)$. Cặp điểm gần nhất là $c = 1 \cdot u = (0.8, 0.6)$ và $d = (4, 3) - 2u = (2.4, 1.8)$, cách nhau 2. Khi đó $a = d - c = (1.6, 1.2)$ và $b = \tfrac{\|d\|_2^2 - \|c\|_2^2}{2} = \tfrac{9 - 1}{2} = 4$. Siêu phẳng phân tách là $1.6x_1 + 1.2x_2 = 4$, hay $4x_1 + 3x_2 = 10$. Kiểm tra: Tâm $(0, 0)$ cho $0 < 10$ và tâm $(4, 3)$ cho $25 > 10$.
:::

::: exercise 2. Chứng nhận vô nghiệm
Chứng minh hệ $x_1 + x_2 < 1$, $x_1 > 1$, $x_2 > 0$ vô nghiệm bằng cách tìm một vector $\lambda$ thỏa hệ lựa chọn ở mục 4.
:::

::: solution
Viết hệ dưới dạng $Ax \prec b$: $x_1 + x_2 < 1$, $-x_1 < -1$, $-x_2 < 0$, tức $A = \begin{bmatrix} 1 & 1 \\ -1 & 0 \\ 0 & -1 \end{bmatrix}$ và $b = (1, -1, 0)$. Chọn $\lambda = (1, 1, 1)$: $A^T \lambda = (1 - 1 + 0,\ 1 + 0 - 1) = (0, 0)$ và $\lambda^T b = 1 - 1 + 0 = 0 \le 0$, cùng $\lambda \succeq 0$, $\lambda \ne 0$. Cộng ba bất đẳng thức được $0 < 0$, mâu thuẫn, nên hệ vô nghiệm.
:::

::: exercise 3. Siêu phẳng tựa của quả cầu ℓ∞
Tìm mọi siêu phẳng tựa của hình vuông $\{x \in \mathbb{R}^2 : \|x\|_\infty \le 1\}$ tại điểm $(1, 0.5)$ và tại đỉnh $(1, 1)$ (theo Bài tập 2.24 trong sách).
:::

::: solution
Điểm $(1, 0.5)$ nằm trong phần giữa cạnh phải $x_1 = 1$, nên siêu phẳng tựa duy nhất là $x_1 = 1$, với pháp tuyến $a = (1, 0)$ (sai khác một hệ số dương). Tại đỉnh $(1, 1)$, mọi $a = (\alpha, \beta)$ với $\alpha, \beta \ge 0$ không đồng thời bằng 0 đều cho siêu phẳng tựa $\alpha x_1 + \beta x_2 = \alpha + \beta$, vì trên hình vuông $\alpha x_1 + \beta x_2 \le \alpha + \beta$. Hai trường hợp biên của chùm này là hai cạnh $x_1 = 1$ và $x_2 = 1$.
:::

## Tóm tắt

Hai tập lồi khác rỗng rời nhau luôn được tách bởi một siêu phẳng, và khi có cặp điểm gần nhất, siêu phẳng đó là đường trung trực của đoạn nối hai điểm ấy. Tính lồi được dùng đúng ở bước kéo một điểm của tập về phía cặp điểm gần nhất. Phân tách nghiêm ngặt không phải lúc nào cũng có, nhưng luôn có giữa một điểm và một tập lồi đóng không chứa nó. Hệ quả là mọi tập lồi đóng bằng giao của các nửa không gian chứa nó.

Khi một tập là mở, có siêu phẳng phân tách tương đương với rời nhau, và điều đó cho các định lý lựa chọn: Một hệ bất đẳng thức chặt vô nghiệm khi và chỉ khi có một tổ hợp không âm của các bất đẳng thức dẫn tới mâu thuẫn. Tại mọi điểm biên của tập lồi có một siêu phẳng tựa, và đó là bức tranh hình học của tối ưu hàm tuyến tính trên tập lồi. Với dữ liệu, hai lớp tách được bằng một hàm affine khi và chỉ khi bao lồi của chúng không giao nhau, và đường tách có lề lớn nhất cách đều hai bao lồi.

## Nguồn và đọc thêm

- S. Boyd, L. Vandenberghe, *Convex Optimization*, §2.5 (tr. 46–51), Hình 2.19–2.21, Ví dụ 2.19–2.21, Bài tập 2.22–2.24 và 2.27. Phân loại tuyến tính và lề lớn nhất ở §8.6.1 (tr. 423–425).
- Ví dụ hai tập đóng không tách nghiêm ngặt được, ví dụ XOR với đặc trưng $x_1 x_2$, ví dụ siêu phẳng tựa trên quả cầu $\ell_1$ và $\ell_2$, các câu hỏi và bài tập 1, 2 do người soạn bổ sung. Mọi con số đã được tính lại bằng chương trình.
