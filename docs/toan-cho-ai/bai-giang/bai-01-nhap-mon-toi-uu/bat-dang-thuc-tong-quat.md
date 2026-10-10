---
course: toan-cho-ai
lecture: bai-01-nhap-mon-toi-uu
topic: bat-dang-thuc-tong-quat
section: topic
title: "Nón chính quy và bất đẳng thức tổng quát"
description: "Bốn điều kiện của nón chính quy và vai trò của từng điều kiện, bất đẳng thức tổng quát x ⪯_K y, các ví dụ theo từng thành phần, thứ tự ma trận và đa thức không âm, các tính chất còn giữ và tính chất bị mất, phần tử nhỏ nhất và phần tử tối thiểu."
---

Trên trục số, hai số bất kỳ luôn so sánh được: Hoặc $a \le b$, hoặc $b \le a$. Thói quen này mạnh đến mức ta ít khi nghĩ về nó. Nhưng hãy thử so sánh hai mô hình học máy, một mô hình có độ chính xác 92% và thời gian dự đoán 30 ms, một mô hình có độ chính xác 89% và thời gian 8 ms. Mô hình nào "tốt hơn"? Không có câu trả lời nếu không nói thêm ta coi trọng tiêu chí nào. Khi đại lượng cần so sánh là một vector, khái niệm "nhỏ hơn" không còn hiển nhiên.

Ta sẽ xây dựng một khái niệm "nhỏ hơn" cho vector và ma trận, dựa hoàn toàn vào hình học của nón. Ý tưởng rất gọn: Chọn một nón $K$ làm "tập các vector không âm", rồi định nghĩa $x \preceq y$ khi $y - x$ không âm theo nghĩa đó. Ta sẽ thấy những điều kiện nào trên nón làm cho phép so sánh hành xử giống phép so sánh trên trục số, và những thói quen nào của trục số phải bỏ. Cuối trang là hai khái niệm sẽ dùng mãi trong tối ưu đa mục tiêu: Phần tử **nhỏ nhất** và phần tử **tối thiểu**.

## 1. Nón chính quy

> **Định nghĩa.** Một nón $K \subseteq \mathbb{R}^n$ là **nón chính quy** (proper cone) nếu nó thỏa đồng thời bốn điều kiện:
> 1. $K$ lồi.
> 2. $K$ đóng.
> 3. $K$ **đặc** (solid), tức là có phần trong khác rỗng.
> 4. $K$ **nhọn** (pointed), tức là không chứa đường thẳng nào. Tương đương: Nếu $x \in K$ và $-x \in K$ thì $x = 0$.

Mỗi điều kiện có một nhiệm vụ riêng trong phép so sánh mà ta sắp định nghĩa. Lồi bảo đảm cộng hai bất đẳng thức được. Đóng bảo đảm bất đẳng thức được giữ khi qua giới hạn. Đặc bảo đảm có những cặp được so sánh "chặt". Nhọn bảo đảm $x \preceq y$ và $y \preceq x$ kéo theo $x = y$. Bảng dưới đây cho thấy điều gì xảy ra khi thiếu một điều kiện:

| Nón trong $\mathbb{R}^2$ | Lồi | Đóng | Đặc | Nhọn |
| --- | --- | --- | --- | --- |
| Góc phần tư $\mathbb{R}^2_+$ | Có | Có | Có | Có |
| Tia $\{(u, 0) : u \ge 0\}$ | Có | Có | Không | Có |
| Nửa mặt phẳng $\{(u, v) : v \ge 0\}$ | Có | Có | Có | Không |
| $\{0\} \cup \{(u, v) : u > 0,\ v > 0\}$ | Có | Không | Có | Có |
| Hợp hai trục tọa độ | Không | Có | Không | Không |

Ví dụ thứ hai thiếu phần trong: Một tia trong mặt phẳng không chứa hình tròn nào, dù nó có nội tương đối. Ví dụ thứ ba thiếu tính nhọn vì chứa trọn trục hoành. Ví dụ thứ tư không đóng vì thiếu hai nửa trục dương, là giới hạn của các điểm trong tập.

## 2. Bất đẳng thức tổng quát

> **Định nghĩa.** Với một nón chính quy $K$, **bất đẳng thức tổng quát** $\preceq_K$ được định nghĩa bởi
> $$x \preceq_K y \iff y - x \in K .$$
> Bất đẳng thức **chặt** $\prec_K$ được định nghĩa bởi $x \prec_K y \iff y - x \in \operatorname{int} K$.

Ta cũng viết $y \succeq_K x$ thay cho $x \preceq_K y$. Khi $K = \mathbb{R}_+$, nón các số không âm trên trục số, $\preceq_K$ đúng là $\le$ quen thuộc và $\prec_K$ đúng là $<$. Như vậy bất đẳng thức tổng quát chứa bất đẳng thức thông thường như một trường hợp riêng.

Định nghĩa có một cách đọc hình học: $x \preceq_K y$ nghĩa là $y$ nằm trong nón $K$ được dời tới đỉnh $x$, tức $y \in x + K$. Với $K = \mathbb{R}^2_+$, tập $x + K$ là góc phần tư phía trên bên phải của $x$, nên $x \preceq y$ nghĩa là "$y$ nằm phía trên và bên phải $x$".

Ba ví dụ chính trong sách:

- **Theo từng thành phần** (Ví dụ 2.14). Với $K = \mathbb{R}^n_+$, $x \preceq_K y$ nghĩa là $x_i \le y_i$ với mọi $i$, còn $x \prec_K y$ nghĩa là $x_i < y_i$ với mọi $i$. Thứ tự này xuất hiện thường xuyên đến mức ta bỏ chỉ số $K$ và viết $x \preceq y$, như đã dùng trong ký hiệu đa diện $Ax \preceq b$.
- **Thứ tự ma trận** (Ví dụ 2.15). Với $K = \mathbb{S}^n_+$, $X \preceq Y$ nghĩa là $Y - X$ nửa xác định dương, còn $X \prec Y$ nghĩa là $Y - X$ xác định dương. Phần trong của $\mathbb{S}^n_+$ trong không gian $\mathbb{S}^n$ là $\mathbb{S}^n_{++}$, nên hai định nghĩa khớp nhau.
- **Đa thức không âm** (Ví dụ 2.16). Xét tập các vector hệ số của những đa thức không âm trên $[0, 1]$,

  $$
  K = \{c \in \mathbb{R}^n : C_1 + c_2 t + \cdots + c_n t^{n-1} \ge 0 \text{ với mọi } t \in [0, 1]\}.
  $$

  Đây là một nón chính quy, và $c \preceq_K d$ nghĩa là đa thức của $c$ không vượt đa thức của $d$ tại mọi điểm của $[0, 1]$. Nón $K$ chứa cả những vector có thành phần âm: $c = (1, -1)$ cho đa thức $1 - t \ge 0$ trên $[0, 1]$.

Ví dụ thứ hai đáng dừng lại. Thứ tự ma trận không phải thứ tự theo từng phần tử. Với $X = I$ và $Y = \begin{bmatrix} 2 & -1 \\ -1 & 2 \end{bmatrix}$, ta có $Y - X = \begin{bmatrix} 1 & -1 \\ -1 & 1 \end{bmatrix} \succeq 0$, nên $X \preceq Y$, dù phần tử ở vị trí $(1, 2)$ của $X$ là $0$, lớn hơn $-1$ của $Y$. Ý nghĩa đúng của $X \preceq Y$ là $z^T X z \le z^T Y z$ với **mọi** hướng $z$.

## 3. Những tính chất còn giữ được

Sách liệt kê các tính chất mà bất đẳng thức tổng quát thừa hưởng từ bốn điều kiện của nón chính quy. Với $\preceq_K$:

- Cộng được: Nếu $x \preceq_K y$ và $u \preceq_K v$ thì $x + u \preceq_K y + v$.
- Bắc cầu: Nếu $x \preceq_K y$ và $y \preceq_K z$ thì $x \preceq_K z$.
- Nhân với số không âm: Nếu $x \preceq_K y$ và $\alpha \ge 0$ thì $\alpha x \preceq_K \alpha y$.
- Phản xạ: $x \preceq_K x$.
- Phản đối xứng: Nếu $x \preceq_K y$ và $y \preceq_K x$ thì $x = y$.
- Giữ qua giới hạn: Nếu $x_i \preceq_K y_i$ với mọi $i$, $x_i \to x$ và $y_i \to y$, thì $x \preceq_K y$.

Mỗi tính chất là một dòng chứng minh từ một điều kiện của nón. Tính cộng được và tính bắc cầu đến từ việc $K$ khép kín với phép cộng: $(y - x) + (v - u) \in K$ và $(z - y) + (y - x) \in K$. Tính phản xạ đến từ $0 \in K$. Tính phản đối xứng dùng tính nhọn: $y - x \in K$ và $x - y \in K$ buộc $y - x = 0$. Tính giữ qua giới hạn dùng tính đóng. Bất đẳng thức chặt cũng có các tính chất tương tự, chẳng hạn $x \prec_K y$ và $u \preceq_K v$ kéo theo $x + u \prec_K y + v$, và quan trọng hơn: Nếu $x \prec_K y$ thì với $u, v$ đủ nhỏ, vẫn có $x + u \prec_K y + v$. Tính chất cuối nói rằng bất đẳng thức chặt "bền" với nhiễu nhỏ, nhờ phần trong của $K$ là tập mở.

## 4. Thói quen phải bỏ: Không phải mọi cặp đều so sánh được

Trên trục số, hai số luôn so sánh được, và người ta gọi đó là một **thứ tự tuyến tính** (hay toàn phần). Bất đẳng thức tổng quát nói chung chỉ là **thứ tự bộ phận**: Có những cặp không so sánh được. Với $K = \mathbb{R}^2_+$, hai vector $x = (1, 4)$ và $y = (2, 3)$ cho $y - x = (1, -1) \notin \mathbb{R}^2_+$ và $x - y = (-1, 1) \notin \mathbb{R}^2_+$, nên không có $x \preceq y$ và cũng không có $y \preceq x$.

Đây không phải khiếm khuyết của định nghĩa, mà là phản ánh trung thực của thực tế. Hai mô hình ở đầu trang, với vector "(lỗi, thời gian)" là $(8\%, 30)$ và $(11\%, 8)$, không so sánh được theo từng thành phần. Một phép so sánh buộc mọi cặp phải so sánh được sẽ phải ngầm áp đặt một cách quy đổi giữa lỗi và thời gian.

Hệ quả quan trọng nhất là khái niệm "giá trị nhỏ nhất" tách thành hai khái niệm khác nhau.

## 5. Phần tử nhỏ nhất và phần tử tối thiểu

> **Định nghĩa.** Cho tập $S$ và một bất đẳng thức tổng quát $\preceq_K$.
> - $x \in S$ là **phần tử nhỏ nhất** (minimum element) của $S$ nếu $x \preceq_K y$ với mọi $y \in S$.
> - $x \in S$ là **phần tử tối thiểu** (minimal element) của $S$ nếu với $y \in S$, $y \preceq_K x$ chỉ xảy ra khi $y = x$.

Phần tử nhỏ nhất phải "thắng" **mọi** phần tử khác. Phần tử tối thiểu chỉ cần **không bị** phần tử nào khác "thắng". Phần tử nhỏ nhất, nếu có, là duy nhất (nhờ tính phản đối xứng), còn phần tử tối thiểu thì có thể có rất nhiều.

Hai khái niệm này có biểu diễn hình học rất cô đọng:

$$
\begin{aligned}
x \text{ là phần tử nhỏ nhất} &\iff S \subseteq x + K, \\
x \text{ là phần tử tối thiểu} &\iff (x - K) \cap S = \{x\}.
\end{aligned}
$$

Tập $x + K$ gồm mọi điểm lớn hơn hoặc bằng $x$, nên điều kiện thứ nhất nói "cả tập $S$ nằm ở phía trên $x$". Tập $x - K$ gồm mọi điểm nhỏ hơn hoặc bằng $x$, nên điều kiện thứ hai nói "phía dưới $x$ không có điểm nào khác của $S$". Với $K = \mathbb{R}_+$ trên trục số, hai khái niệm trùng nhau và trùng với giá trị nhỏ nhất quen thuộc.

<OrderLab type="order" />

Với dữ liệu mặc định trong mô phỏng, mỗi điểm là một cấu hình của một hệ thống, với hai tiêu chí đều muốn nhỏ. Các điểm $A, B, C, F$ là tối thiểu: Không cấu hình nào khác tốt hơn hoặc bằng chúng ở cả hai tiêu chí. Các điểm $D, E, G$ bị trội. Không có phần tử nhỏ nhất, vì không cấu hình nào tốt nhất ở cả hai tiêu chí cùng lúc. Trong tối ưu đa mục tiêu, phần tử tối thiểu được gọi là **tối ưu Pareto**, và tập các phần tử tối thiểu là **biên Pareto**. Chủ đề tiếp theo, về nón đối ngẫu, sẽ cho một cách tìm chúng bằng tối ưu một tổng có trọng số.

Hãy thử xoay hai vector sinh của nón trong mô phỏng. Khi nón hẹp lại, ít cặp điểm so sánh được hơn, và số phần tử tối thiểu tăng lên. Khi nón rộng ra, nhiều cặp so sánh được hơn, phần tử tối thiểu ít đi, và có khi xuất hiện một phần tử nhỏ nhất. Nón càng rộng, thứ tự càng "quyết đoán".

Sách có một ví dụ đẹp về thứ tự ma trận (Ví dụ 2.18). Mỗi ma trận $A \succ 0$ ứng với một ellipsoid tâm ở gốc $\mathcal{E}_A = \{x : x^T A^{-1} x \le 1\}$, và có thể chứng minh $A \preceq B$ khi và chỉ khi $\mathcal{E}_A \subseteq \mathcal{E}_B$. Xét tập $S$ các ma trận ứng với những ellipsoid chứa một số điểm cho trước. Tập này không có phần tử nhỏ nhất, vì hai ellipsoid chứa cùng các điểm có thể không lồng vào nhau. Một ellipsoid là tối thiểu nếu không có ellipsoid nào khác chứa các điểm mà lại nằm gọn trong nó.

## 6. Những câu hỏi để đào sâu

**Câu 1.** Trong $\mathbb{R}^2$ với thứ tự theo từng thành phần, tập $S_1 = \{(u, v) : u \ge 1,\ v \ge 2\}$ có phần tử nhỏ nhất không? Tập $S_2 = \{(u, v) : u + v \ge 4,\ u \ge 0,\ v \ge 0\}$ thì sao?

<details><summary>Xem lời giải thích</summary>

$S_1$ có phần tử nhỏ nhất là $(1, 2)$, vì mọi điểm của $S_1$ có $u \ge 1$ và $v \ge 2$, tức là nằm trong $(1, 2) + \mathbb{R}^2_+$. Đó cũng là phần tử tối thiểu duy nhất. $S_2$ không có phần tử nhỏ nhất, vì $(4, 0)$ và $(0, 4)$ đều thuộc $S_2$ mà không điểm nào của $S_2$ nhỏ hơn hoặc bằng cả hai (điểm đó phải có $u \le 0$ và $v \le 0$). Mọi điểm trên đoạn $\{u + v = 4,\ u, v \ge 0\}$ đều là phần tử tối thiểu. Chẳng hạn $(2, 2)$ tối thiểu vì một điểm $(u, v) \preceq (2, 2)$ của $S_2$ phải có $u + v \le 4$, và kết hợp với $u + v \ge 4$ thì $u = v = 2$.

</details>

**Câu 2.** Chữ "tối thiểu" dễ khiến ta nghĩ phần tử tối thiểu là một kiểu "cực tiểu cục bộ", tốt nhất trong một vùng lân cận. Hai khái niệm này khác nhau ở đâu?

<details><summary>Xem lời giải thích</summary>

Phần tử tối thiểu không liên quan tới "lân cận" hay khoảng cách. Nó so sánh với **mọi** phần tử của tập, chỉ là theo một thứ tự bộ phận, nên nhiều phần tử có thể cùng không bị ai thắng. Cực tiểu cục bộ thì so sánh giá trị của một hàm với các điểm ở gần. Vì vậy "minimal element" không được dịch thành "cực tiểu địa phương": Hai khái niệm thuộc hai thế giới khác nhau.

</details>

**Câu 3.** Vì sao điều kiện "nhọn" lại cần cho tính phản đối xứng? Hãy tìm hai vector khác nhau $x \ne y$ thỏa cả $x \preceq_K y$ và $y \preceq_K x$ khi $K$ là nửa mặt phẳng $\{(u, v) : v \ge 0\}$.

<details><summary>Xem lời giải thích</summary>

Lấy $x = (0, 0)$ và $y = (1, 0)$. Ta có $y - x = (1, 0) \in K$ và $x - y = (-1, 0) \in K$, vì cả hai có $v = 0 \ge 0$. Vậy $x \preceq_K y$ và $y \preceq_K x$ mà $x \ne y$. Nửa mặt phẳng chứa trục hoành, một đường thẳng qua gốc, và theo hướng của đường thẳng đó, "lớn hơn" và "nhỏ hơn" trở thành một. Tính nhọn loại bỏ đúng tình huống này.

</details>

**Câu 4.** Với thứ tự ma trận, tập $\{X \in \mathbb{S}^2 : X \succeq I\}$ có phần tử nhỏ nhất không? Tập $\{X \in \mathbb{S}^2 : X_{11} \ge 1,\ X_{22} \ge 1\}$ thì sao?

<details><summary>Xem lời giải thích</summary>

Tập thứ nhất có phần tử nhỏ nhất là $I$, vì theo định nghĩa mọi phần tử $X$ của nó thỏa $I \preceq X$. Tập thứ hai không có phần tử nhỏ nhất. Nó chứa $\begin{bmatrix} 1 & a \\ a & 1 \end{bmatrix}$ với mọi $a$, và một phần tử nhỏ nhất $M$ phải thỏa $M \preceq \begin{bmatrix} 1 & a \\ a & 1 \end{bmatrix}$ với mọi $a$. Lấy $z = (1, -1)$: Điều kiện đó đòi $z^T M z \le 2 - 2a$ với mọi $a$, không thể đúng khi $a$ lớn. Ràng buộc chỉ trên đường chéo không đủ để có một phần tử "nhỏ hơn mọi thứ" theo thứ tự ma trận.

</details>

## 7. Bài tập tự luyện

::: exercise 1. Kiểm tra nón chính quy
Tập $K = \{(x_1, x_2) : x_1 \ge |x_2|\}$ có phải nón chính quy không? Với thứ tự $\preceq_K$, so sánh $x = (1, 0)$ và $y = (3, 1)$.
:::

::: solution
$K$ là giao của hai nửa mặt phẳng $x_1 - x_2 \ge 0$ và $x_1 + x_2 \ge 0$ có biên qua gốc, nên là nón lồi và đóng. Điểm $(1, 0)$ có một hình tròn nhỏ bán kính $\tfrac12$ nằm trong $K$, nên $K$ đặc. Nếu $x \in K$ và $-x \in K$ thì $x_1 \ge |x_2|$ và $-x_1 \ge |x_2|$, cộng lại được $0 \ge 2|x_2|$, nên $x_2 = 0$, rồi $x_1 = 0$. Vậy $K$ nhọn, và là nón chính quy. Với $x = (1, 0)$, $y = (3, 1)$: $y - x = (2, 1)$ và $2 \ge 1$, nên $x \preceq_K y$. Thậm chí $2 > 1$ nên $y - x \in \operatorname{int} K$ và $x \prec_K y$.
:::

::: exercise 2. Phần tử tối thiểu của một tập hữu hạn
Với thứ tự theo từng thành phần trong $\mathbb{R}^2$, tìm mọi phần tử tối thiểu và phần tử nhỏ nhất (nếu có) của tập sáu điểm

$$
S = \{(3, 5),\ (4, 2),\ (2, 6),\ (5, 1),\ (4, 4),\ (6, 6)\}.
$$
:::

::: solution
$(4, 4)$ bị $(4, 2)$ trội vì $(4, 2) \preceq (4, 4)$ và hai điểm khác nhau. $(6, 6)$ bị trội bởi nhiều điểm, chẳng hạn $(3, 5)$. Bốn điểm còn lại $(3, 5)$, $(4, 2)$, $(2, 6)$, $(5, 1)$ không bị điểm nào trội, nên là phần tử tối thiểu. Không có phần tử nhỏ nhất, vì $(2, 6)$ và $(5, 1)$ không so sánh được mà cả hai đều thuộc $S$: Một phần tử nhỏ nhất phải nhỏ hơn hoặc bằng cả hai, tức là có hoành độ không quá 2 và tung độ không quá 1, mà không điểm nào của $S$ như vậy.
:::

## Tóm tắt

Một nón chính quy là nón lồi, đóng, có phần trong khác rỗng và không chứa đường thẳng. Nó sinh ra bất đẳng thức tổng quát $x \preceq_K y \iff y - x \in K$, với bản chặt dùng phần trong của $K$. Thứ tự theo từng thành phần, thứ tự ma trận và thứ tự giữa các đa thức trên một đoạn đều là những trường hợp riêng. Bất đẳng thức tổng quát giữ được tính cộng, bắc cầu, nhân với số không âm, phản xạ, phản đối xứng và tính đóng qua giới hạn, mỗi tính chất đến từ một điều kiện của nón.

Điều bị mất là tính so sánh được của mọi cặp. Vì vậy khái niệm "nhỏ nhất" tách đôi: Phần tử nhỏ nhất thắng mọi phần tử khác và là duy nhất nếu có, còn phần tử tối thiểu chỉ cần không bị phần tử nào thắng và có thể có nhiều. Với thứ tự theo từng thành phần, phần tử tối thiểu chính là lựa chọn tối ưu Pareto.

## Nguồn và đọc thêm

- S. Boyd, L. Vandenberghe, *Convex Optimization*, §2.4 (tr. 43–46), Ví dụ 2.14–2.18, Hình 2.17 và 2.18, Bài tập 2.30.
- Ví dụ các cấu hình với hai tiêu chí, bảng các nón thiếu từng điều kiện, các câu hỏi và bài tập do người soạn bổ sung. Mọi con số đã được tính lại bằng chương trình.
