---
course: toan-cho-ai
lecture: bai-01-nhap-mon-toi-uu
topic: sieu-phang-phan-tach-va-tua
section: topic
title: "Siêu phẳng phân tách và siêu phẳng tựa"
description: "Định lý siêu phẳng phân tách và chứng minh bằng cặp điểm gần nhất, phân tách nghiêm ngặt, tập lồi đóng là giao các nửa không gian chứa nó, định lý lựa chọn cho hệ bất đẳng thức chặt, siêu phẳng tựa, và ý nghĩa với phân loại tuyến tính."
---

Hãy đặt hai hòn đá lồi, chẳng hạn hai viên sỏi tròn, lên mặt bàn sao cho chúng không chạm nhau. Bạn luôn có thể luồn một tờ giấy phẳng vào giữa để ngăn chúng ra. Nhưng nếu một hòn đá có hình lưỡi liềm ôm lấy hòn kia, thì không tờ giấy phẳng nào làm được việc đó, dù hai hòn đá vẫn không chạm nhau. Điều khác biệt giữa hai tình huống chính là tính lồi.

Định lý siêu phẳng phân tách biến trực giác ấy thành một mệnh đề toán học chính xác, và là một trong những cột trụ giải tích của toàn bộ lý thuyết tối ưu hóa. Lý thuyết đối ngẫu Lagrange, hệ điều kiện tối ưu Karush-Kuhn-Tucker (KKT), bổ đề Farkas, các định lý về giải pháp thay thế, và bài toán phân loại tuyến tính trong học máy đều bắt nguồn trực tiếp từ định lý này. Ta sẽ phát biểu định lý, chứng minh trong trường hợp hình học mẫu mực nhất, rồi mở rộng sang các hệ quả nền tảng.

## 1. Định lý siêu phẳng phân tách

> **Định lý.** Cho $C$ và $D$ là hai tập hợp lồi khác rỗng, rời nhau trong $\mathbb{R}^n$ ($C \cap D = \varnothing$). Khi đó tồn tại vector pháp tuyến $a \ne 0$ và số thực $b$ sao cho:
> $$a^T x \le b \ \text{ với mọi } x \in C, \qquad a^T x \ge b \ \text{ với mọi } x \in D.$$

Nói cách khác, dạng affine $a^T x - b$ không dương trên toàn bộ tập $C$ và không âm trên toàn bộ tập $D$. Siêu phẳng $\mathcal{H} = \{x \in \mathbb{R}^n : a^T x = b\}$ được gọi là **siêu phẳng phân tách** (separating hyperplane) của $C$ và $D$: Hai tập hợp nằm về hai phía đối diện của siêu phẳng, có thể tiếp xúc với siêu phẳng nhưng không bao giờ cắt xuyên qua.

Ba lưu ý sư phạm cần khắc sâu khi phân tích định lý:
1. Tính lồi là điều kiện bắt buộc: Ví dụ hai tập hợp dạng lưỡi liềm lồng vào nhau cho thấy nếu thiếu tính lồi, định lý phân tách sẽ sụp đổ hoàn toàn dù hai tập không giao nhau.
2. Dấu bất đẳng thức trong kết luận là không ngặt ($\le$ và $\ge$): Hai tập hợp vẫn có thể cùng chạm vào siêu phẳng phân tách tại các điểm biên.
3. Định lý mang tính tồn tại: Tuy nhiên, trong nhiều trường hợp giải tích cụ thể, chứng minh dưới đây cho ta một thuật toán hình học tường minh để dựng siêu phẳng phân cách.

<SeparationLab type="sets" />

## 2. Chứng minh trong trường hợp tồn tại cặp điểm gần nhất

Ta bắt đầu bằng việc chứng minh định lý trong trường hợp trực quan nhất: Khi hai tập hợp sở hữu một cặp điểm gần nhau nhất. Giả sử khoảng cách Euclid giữa hai tập lồi:

$$
\operatorname{dist}(C, D) = \inf\{\|u - v\|_2 : u \in C,\ v \in D\}
$$

là một số dương ngặt, và tồn tại hai điểm $c \in C$, $d \in D$ đạt đúng khoảng cách cực tiểu này: $\|c - d\|_2 = \operatorname{dist}(C, D) > 0$. Giả thiết này luôn được thỏa mãn khi $C$ và $D$ là hai tập đóng và ít nhất một trong hai tập bị chặn (tập compact).

**Dựng siêu phẳng phân tách.** Chọn vector pháp tuyến $a = d - c$ và hệ số tự do $b = \tfrac{\|d\|_2^2 - \|c\|_2^2}{2}$. Hàm affine tương ứng nhận biểu diễn:

$$
f(x) = a^T x - b = (d - c)^T \left(x - \tfrac12(d + c)\right).
$$

Về hình học, siêu phẳng $f(x) = 0$ vuông góc với đoạn thẳng $[c, d]$ và đi qua chính xác trung điểm $\tfrac{1}{2}(c + d)$, tức là **siêu phẳng trung trực** của đoạn thẳng nối hai điểm gần nhất.

**Chứng minh $f(u) \ge 0$ với mọi $u \in D$.** Giả sử phản chứng tồn tại điểm $u \in D$ sao cho $f(u) < 0$. Khai triển hàm affine tại $u$:

$$
f(u) = (d - c)^T(u - d) + \tfrac12 \|d - c\|_2^2 ,
$$

do đó điều kiện $f(u) < 0$ kéo theo bất đẳng thức góc tù: $(d - c)^T(u - d) < 0$. Xét điểm biến thiên $d(t) = d + t(u - d)$ nằm trên đoạn thẳng nối $d$ và $u$ với $t \in [0, 1]$. Tính đạo hàm của bình phương khoảng cách từ $d(t)$ tới điểm $c$ tại $t = 0$:

$$
\left.\frac{d}{dt} \|d + t(u - d) - c\|_2^2 \right|_{t=0} = 2(d - c)^T(u - d) < 0 .
$$

Đạo hàm nhận giá trị âm chứng tỏ khi dịch chuyển một đoạn nhỏ từ $d$ về phía $u$, khoảng cách tới $c$ sẽ giảm nghiêm ngặt. Với tham số $t > 0$ đủ nhỏ, điểm $d(t)$ nằm gần $c$ hơn so với điểm $d$. Vì tập $D$ lồi và chứa cả $d, u$ nên điểm $d(t)$ bắt buộc phải thuộc $D$. Điều này mâu thuẫn trực tiếp với giả thiết $d$ là điểm của $D$ gần tập $C$ nhất.

Lập luận tương tự cho phép khẳng định $f(x) \le 0$ với mọi $x \in C$.

Điểm mấu chốt sử dụng tính lồi nằm ở chỗ: Đoạn thẳng nối $d$ và $u$ phải nằm trọn trong $D$. Khi không tồn tại cặp điểm đạt khoảng cách cực tiểu (chẳng hạn hai tập mở hoặc không bị chặn), người ta sử dụng kỹ thuật tịnh tiến bằng cách xét tập hiệu Minkowski $C - D = \{x - y : x \in C,\ y \in D\}$. Tập $C - D$ là một tập lồi không chứa gốc tọa độ, quy bài toán về việc phân tách gốc tọa độ $0$ khỏi một tập lồi.

## 3. Điều kiện phân tách nghiêm ngặt

Siêu phẳng trung trực dựng ở mục trên thỏa mãn điều kiện ngặt mạnh hơn: Cụ thể là $a^T x < b$ với mọi $x \in C$ và $a^T x > b$ với mọi $x \in D$. Trạng thái này được gọi là **phân tách nghiêm ngặt** (strict separation). Tuy nhiên, không phải mọi cặp tập lồi đóng rời nhau đều có thể phân tách nghiêm ngặt, ngay cả khi hai tập đều đóng nhưng không bị chặn.

Chẳng hạn trong $\mathbb{R}^2$, xét hai tập hợp:

$$
C = \{(x_1, x_2) : x_2 \le 0\}, \qquad D = \{(x_1, x_2) : x_1 > 0,\ x_1 x_2 \ge 1\}.
$$

Cả hai tập đều lồi, đóng và không giao nhau. Tuy nhiên khi hoành độ $x_1 \to \infty$, tung độ $1/x_1 \to 0$, khoảng cách giữa hai tập tiệm cận về 0. Siêu phẳng duy nhất có thể phân tách chúng là trục hoành $x_2 = 0$. Đường thẳng này tiếp xúc trực tiếp với biên của $C$, do đó không thể phân tách nghiêm ngặt.

Trường hợp nền tảng luôn bảo đảm phân tách nghiêm ngặt là: **Một điểm nằm ngoài một tập lồi đóng**. Nếu $C$ là tập lồi đóng và $x_0 \notin C$, thì luôn tồn tại một hình cầu mở $B(x_0, \varepsilon)$ không giao với $C$. Khi đó siêu phẳng phân tách hình cầu mở này và tập $C$ sẽ phân tách nghiêm ngặt điểm $x_0$ khỏi $C$.

Hệ quả hình học: **Mọi tập lồi đóng $C \subseteq \mathbb{R}^n$ đều bằng giao của tất cả các nửa không gian đóng chứa nó**. Thật vậy, giả sử tồn tại điểm $x_0$ thuộc phần giao của mọi nửa không gian nhưng $x_0 \notin C$. Áp dụng định lý phân tách nghiêm ngặt, tồn tại một nửa không gian đóng chứa trọn $C$ nhưng không chứa $x_0$, mâu thuẫn với giả thiết $x_0$ thuộc phần giao. Kết quả khẳng định: Cấu trúc bên trong của một tập lồi đóng được xác định hoàn toàn bởi các mặt phẳng bao bọc bên ngoài.

## 4. Chiều ngược lại và định lý về giải pháp thay thế

Chiều ngược của định lý phân tách ("tồn tại siêu phẳng phân tách thì hai tập phải rời nhau") nói chung không đúng nếu không bổ sung điều kiện tô-pô. Chẳng hạn hai tập suy biến $C = D = \{0\}$ trong $\mathbb{R}$ cùng nằm trên siêu phẳng $x = 0$, thỏa mãn điều kiện phân tách nhưng chúng trùng nhau. Tuy nhiên, nếu ít nhất một trong hai tập là **tập mở**, chiều ngược lại hoàn toàn chính xác.

Tổng hợp lại, ta có định lý tương đương: Hai tập lồi, trong đó ít nhất một tập là tập mở, rời nhau **khi và chỉ khi** tồn tại một siêu phẳng phân tách chúng.

Ta có ứng dụng trực tiếp vào giải quyết hệ bất đẳng thức tuyến tính: Hệ bất đẳng thức ngặt $Ax \prec b$ (với ma trận $A \in \mathbb{R}^{m \times n}$) vô nghiệm khi và chỉ khi tập affine $\{b - Ax : x \in \mathbb{R}^n\}$ không giao với nón mở các số dương $\mathbb{R}^m_{++}$. Áp dụng định lý phân tách cho hai tập lồi này, ta thu được kết quả: **Hệ $Ax \prec b$ vô nghiệm khi và chỉ khi tồn tại vector $\lambda \in \mathbb{R}^m$ thỏa mãn đồng thời:**

$$
\lambda \ne 0, \qquad \lambda \succeq 0, \qquad A^T \lambda = 0, \qquad \lambda^T b \le 0 .
$$

Hai hệ trên tạo thành một **cặp giải pháp thay thế** (theorem of alternatives): Với bất kỳ bộ dữ liệu $A, b$ nào, đúng một và chỉ một trong hai hệ có nghiệm khả thi. Ý nghĩa thực tiễn là: Để chứng minh một bài toán tối ưu hoặc một hệ ràng buộc vô nghiệm, ta không cần phải duyệt qua không gian nghiệm vô hạn, mà chỉ cần cung cấp một vector chứng chỉ $\lambda$ (certificate of infeasibility).

::: example Chứng chỉ vô nghiệm cho hệ một biến
Xét hệ bất đẳng thức $x < 1$ và $-x < -1$ (tức $x > 1$). Viết dưới dạng chuẩn $Ax \prec b$ với ma trận $A = \begin{bmatrix} 1 \\ -1 \end{bmatrix}$ và vector $b = \begin{bmatrix} 1 \\ -1 \end{bmatrix}$. Chọn vector $\lambda = (1, 1)^T$, ta dễ dàng kiểm tra: $\lambda \ne 0$, $\lambda \succeq 0$, $A^T \lambda = 1 - 1 = 0$ và $\lambda^T b = 1 - 1 = 0 \le 0$.

Cơ chế hoạt động của chứng chỉ: Lấy tổ hợp tuyến tính các bất đẳng thức với trọng số $\lambda$ dẫn tới $\lambda^T A x < \lambda^T b \iff 0 < 0$, tạo ra một mâu thuẫn số học tuyệt đối.
:::

## 5. Siêu phẳng tựa

Định lý phân tách có một phiên bản giới hạn khi tập thứ hai thu về một điểm biên duy nhất:

> **Định nghĩa.** Cho tập hợp $C \subseteq \mathbb{R}^n$ và điểm $x_0$ thuộc biên của $C$. Nếu tồn tại vector $a \ne 0$ sao cho $a^T x \le a^T x_0$ với mọi $x \in C$, thì siêu phẳng $\mathcal{H} = \{x \in \mathbb{R}^n : a^T x = a^T x_0\}$ được gọi là một **siêu phẳng tựa** (supporting hyperplane) của $C$ tại điểm $x_0$.

Về mặt trực giác, siêu phẳng tựa tiếp xúc với tập $C$ tại điểm biên $x_0$ và giữ toàn bộ tập $C$ nằm trọn vẹn ở một phía của nó. Khi biên trơn khả vi tại $x_0$, siêu phẳng tựa trùng khớp với mặt phẳng tiếp diện. Khi $x_0$ là một điểm góc nhọn hoặc điểm kỳ dị, tồn tại một hình nón gồm vô số siêu phẳng tựa tựa vào điểm đó.

> **Định lý siêu phẳng tựa.** Nếu $C$ là một tập lồi khác rỗng thì tại mọi điểm $x_0$ nằm trên biên của $C$ luôn tồn tại ít nhất một siêu phẳng tựa.

Chứng minh dựa vào việc áp dụng định lý phân tách giữa điểm biên $\{x_0\}$ và phần trong tương đối $\operatorname{relint} C$. Chiều ngược lại cũng đúng dưới giả thiết tô-pô: Một tập đóng có phần trong khác rỗng là tập lồi khi và chỉ khi nó có siêu phẳng tựa tại mọi điểm biên.

<SeparationLab type="support" />

Siêu phẳng tựa là chìa khóa hình học giải bài toán tối ưu tuyến tính trên tập lồi: Bài toán tìm cực đại của dạng tuyến tính $a^T x$ trên tập $C$ tương đương với việc tịnh tiến siêu phẳng có pháp tuyến $a$ theo hướng đó cho đến khi nó trở thành siêu phẳng tựa tiếp xúc với tập $C$ tại điểm $x_0$. Điểm tiếp xúc $x_0$ chính là nghiệm tối ưu toàn cục. Đây cũng là lý do vì sao trong hồi quy Lasso (chuẩn $\ell_1$), siêu phẳng mức tiếp xúc với quả cầu $\ell_1$ tại các đỉnh trên trục tọa độ, tạo ra các nghiệm thưa (sparse solutions).

## 6. Phân loại tuyến tính và máy vector hỗ trợ (SVM)

Xét bài toán học máy phân loại nhị phân với hai tập điểm dữ liệu $\{x_1, \ldots, x_N\}$ (nhãn dương) và $\{y_1, \ldots, y_M\}$ (nhãn âm). Ta tìm kiếm một siêu phẳng phân lớp $f(x) = a^T x - b = 0$ sao cho $f(x_i) > 0$ và $f(y_j) < 0$. Câu trả lời giải tích bắt nguồn trực tiếp từ định lý phân tách: **Hai tập dữ liệu phân tách được bằng một siêu phẳng tuyến tính khi và chỉ khi hai bao lồi của chúng không giao nhau**, tức là:

$$
\operatorname{conv}\{x_1, \ldots, x_N\} \cap \operatorname{conv}\{y_1, \ldots, y_M\} = \varnothing .
$$

Trường hợp kinh điển minh họa cho sự vi phạm điều kiện này là bài toán logic XOR: Lớp thứ nhất gồm hai điểm $(0, 0)$ và $(1, 1)$, lớp thứ hai gồm hai điểm $(1, 0)$ và $(0, 1)$. Hai bao lồi tương ứng chính là hai đường chéo của hình vuông đơn vị, và chúng giao nhau tại tâm $(\tfrac12, \tfrac12)$. Do đó không tồn tại bất kỳ hàm tuyến tính nào có thể phân tách hai lớp điểm này, đặt ra yêu cầu phải sử dụng các đặc trưng phi tuyến hoặc kiến trúc mạng nơ-ron nhiều tầng.

Khi hai lớp dữ liệu phân tách tuyến tính được, một hướng tiếp cận tự nhiên là tìm siêu phẳng phân cách đạt **độ mở lề lớn nhất** (maximum margin), tức khoảng cách từ siêu phẳng tới các điểm dữ liệu gần nhất ở cả hai phía đạt cực đại. Bề rộng của lề tối ưu bằng đúng **khoảng cách Euclid giữa hai bao lồi**. Siêu phẳng phân cách tối ưu chính là mặt phẳng trung trực của đoạn thẳng nối hai điểm gần nhất giữa hai bao lồi, hoàn toàn trùng khớp với cách dựng trong chứng minh ở mục 2. Đây chính là bản chất toán học của thuật toán Support Vector Machine (SVM) lề cứng.

<SeparationLab type="data" />

Trong mô hình SVM, chỉ những điểm dữ liệu nằm trên biên của lề (các điểm cực biên của bao lồi quyết định khoảng cách giữa hai tập) mới có trọng số Lagrange khác không. Chúng được gọi là các **vector hỗ trợ** (support vectors), trong khi các điểm dữ liệu nằm sâu bên trong cụm hoàn toàn không ảnh hưởng tới vị trí của ranh giới phân lớp.

## 7. Những câu hỏi để đào sâu

**Câu 1.** Định lý phân tách có còn đúng không nếu chỉ một trong hai tập hợp là tập lồi? Hãy nêu một ví dụ phản chứng cụ thể.

<details><summary>Xem lời giải thích</summary>

Định lý sẽ không còn đúng. Xét trong $\mathbb{R}^2$, chọn tập lồi $C$ là hình tròn đơn vị đóng $\{x : \|x\|_2 \le 1\}$ và tập không lồi $D$ là hình vành khăn $\{x : 2 \le \|x\|_2 \le 3\}$. Rõ ràng hai tập hợp này không giao nhau. Tuy nhiên, vì vành khăn $D$ bao bọc hoàn toàn hình tròn $C$ theo mọi hướng không gian, bất kỳ đường thẳng nào để $C$ nằm trọn về một phía đều cắt qua vành khăn $D$. Do đó không tồn tại bất kỳ siêu phẳng phân tách nào. Định lý bắt buộc **cả hai** tập hợp đều phải là tập lồi.

</details>

**Câu 2.** Trong chứng minh ở mục 2, nếu ta đổi dấu vector pháp tuyến thành $a = c - d$, siêu phẳng phân tách thay đổi như thế nào?

<details><summary>Xem lời giải thích</summary>

Việc đổi dấu vector pháp tuyến và hệ số tự do chỉ làm đảo ngược dấu của hàm affine mà không làm thay đổi vị trí hình học của siêu phẳng phân tách: Khi đó ta có $a^T x \ge b$ trên $C$ và $a^T x \le b$ trên $D$. Siêu phẳng vẫn phân tách trọn vẹn hai tập hợp. Điều này giải thích vì sao định lý chỉ khẳng định sự tồn tại của vector $a \ne 0$ mà không quy định chiều định hướng.

</details>

**Câu 3.** Liệu có thể phân tách nghiêm ngặt hai tập lồi đóng, rời nhau mà cả hai đều không bị chặn hay không?

<details><summary>Xem lời giải thích</summary>

Hoàn toàn có thể. Xét hai nửa mặt phẳng đóng $C = \{x \in \mathbb{R}^2 : x_2 \le 0\}$ và $D = \{x \in \mathbb{R}^2 : x_2 \ge 1\}$. Cả hai tập đều đóng, không bị chặn và rời nhau. Đường thẳng $x_2 = \tfrac{1}{2}$ phân tách nghiêm ngặt hai tập hợp này. Yếu tố cốt lõi để bảo đảm phân tách nghiêm ngặt không phải là tính bị chặn, mà là khoảng cách Euclid giữa hai tập phải dương ngặt $\operatorname{dist}(C, D) > 0$.

</details>

**Câu 4.** Trong bài toán XOR, nếu ta đưa thêm một đặc trưng phi tuyến bậc hai $x_3 = x_1 x_2$, dữ liệu có phân tách được bằng một siêu phẳng tuyến tính trong $\mathbb{R}^3$ không?

<details><summary>Xem lời giải thích</summary>

Hoàn toàn phân tách được. Sau khi chiếu vào $\mathbb{R}^3$, bốn điểm dữ liệu trở thành: Cụ thể gồm $(0, 0, 0)^T$ và $(1, 1, 1)^T$ cho lớp thứ nhất, $(1, 0, 0)^T$ và $(0, 1, 0)^T$ cho lớp thứ hai. Chọn hàm affine $f(x) = x_1 + x_2 - 2x_3 - \tfrac{1}{2}$, ta nhận thấy $f(x) = -\tfrac{1}{2} < 0$ trên toàn bộ lớp thứ nhất và $f(x) = \tfrac{1}{2} > 0$ trên toàn bộ lớp thứ hai. Siêu phẳng $x_1 + x_2 - 2x_3 = \tfrac{1}{2}$ phân tách hoàn hảo hai lớp dữ liệu. Đây chính là nguyên lý cốt lõi của phương pháp Kernel trong học máy.

</details>

## 8. Bài tập tự luyện

::: exercise 1. Dựng siêu phẳng phân tách giữa hai hình tròn
Cho hai hình tròn đóng trong mặt phẳng: Cụ thể là $C = \{x \in \mathbb{R}^2 : \|x\|_2 \le 1\}$ và $D = \{x \in \mathbb{R}^2 : \|x - (4, 3)^T\|_2 \le 2\}$. Hãy xác định cặp điểm gần nhất giữa hai tập và phương trình siêu phẳng phân tách tương ứng.
:::

::: solution
Khoảng cách giữa hai tâm là $\sqrt{4^2 + 3^2} = 5$, lớn hơn tổng hai bán kính $1 + 2 = 3$, do đó hai hình tròn rời nhau. Vector đơn vị hướng từ tâm của $C$ sang tâm của $D$ là $u = (0.8, 0.6)^T$.

Cặp điểm đạt khoảng cách cực tiểu giữa hai tập là:
- $c = 1 \cdot u = (0.8, 0.6)^T \in C$,
- $d = (4, 3)^T - 2u = (2.4, 1.8)^T \in D$.

Vector pháp tuyến là $a = d - c = (1.6, 1.2)^T$, và hệ số tự do là $b = \tfrac{\|d\|_2^2 - \|c\|_2^2}{2} = \tfrac{9 - 1}{2} = 4$. Phương trình siêu phẳng phân tách là $1.6x_1 + 1.2x_2 = 4$, tương đương với $4x_1 + 3x_2 = 10$.
:::

::: exercise 2. Chứng chỉ vô nghiệm
Hãy chứng minh hệ bất đẳng thức $x_1 + x_2 < 1$, $x_1 > 1$, $x_2 > 0$ vô nghiệm bằng cách thiết lập một vector nhân tử Lagrange $\lambda$ theo định lý về giải pháp thay thế.
:::

::: solution
Viết lại hệ dưới dạng chuẩn $Ax \prec b$:
- $x_1 + x_2 < 1$,
- $-x_1 < -1$,
- $-x_2 < 0$.

Ma trận hệ số và vector vế phải là:
$$
A = \begin{bmatrix} 1 & 1 \\ -1 & 0 \\ 0 & -1 \end{bmatrix}, \qquad b = \begin{bmatrix} 1 \\ -1 \\ 0 \end{bmatrix}.
$$

Chọn vector nhân tử $\lambda = (1, 1, 1)^T \ge 0$. Ta kiểm tra:
$$
A^T \lambda = \begin{bmatrix} 1 - 1 + 0 \\ 1 + 0 - 1 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}, \qquad \lambda^T b = 1 - 1 + 0 = 0 \le 0.
$$
Nhân các bất đẳng thức với trọng số $\lambda$ và cộng lại, ta thu được bất đẳng thức mâu thuẫn $0 < 0$. Vậy hệ ràng buộc vô nghiệm.
:::

::: exercise 3. Siêu phẳng tựa của hình vuông chuẩn ℓ∞
Xác định toàn bộ các siêu phẳng tựa của hình vuông đơn vị $\{x \in \mathbb{R}^2 : \|x\|_\infty \le 1\}$ tại điểm biên $x_0 = (1, 0.5)^T$ và tại đỉnh cực biên $x_1 = (1, 1)^T$.
:::

::: solution
Tại điểm $x_0 = (1, 0.5)^T$ nằm trên cạnh phải $x_1 = 1$, siêu phẳng tựa là duy nhất và có phương trình $x_1 = 1$ (với vector pháp tuyến tỷ lệ với $(1, 0)^T$).

Tại đỉnh $x_1 = (1, 1)^T$, mọi vector pháp tuyến dạng $a = (\alpha, \beta)^T$ với $\alpha \ge 0, \beta \ge 0$ không đồng thời bằng 0 đều sinh ra một siêu phẳng tựa có phương trình $\alpha x_1 + \beta x_2 = \alpha + \beta$, vì trên toàn bộ hình vuông ta luôn có $\alpha x_1 + \beta x_2 \le \alpha + \beta$. Chùm siêu phẳng tựa này lấp đầy góc phần tư thứ nhất của không gian đối ngẫu.
:::

## Tóm tắt

Hai tập lồi khác rỗng rời nhau luôn tồn tại ít nhất một siêu phẳng phân tách chúng. Khi khoảng cách giữa hai tập đạt cực tiểu tại một cặp điểm, siêu phẳng phân tách chính là mặt phẳng trung trực của đoạn thẳng nối hai điểm đó. Mọi tập lồi đóng đều bằng giao của toàn bộ các nửa không gian đóng chứa nó, tạo nên nền tảng cho lý thuyết đối ngẫu.

Định lý về giải pháp thay thế cung cấp chứng chỉ đại số hữu hạn để xác minh tính vô nghiệm của hệ bất đẳng thức. Tại mọi điểm biên của một tập lồi luôn tồn tại siêu phẳng tựa, liên kết trực tiếp với nghiệm của bài toán quy hoạch tuyến tính. Trong học máy, hai tập dữ liệu phân tách tuyến tính được khi và chỉ khi hai bao lồi của chúng không giao nhau, và siêu phẳng lề cực đại của máy vector hỗ trợ (SVM) chính là siêu phẳng trung trực nối hai bao lồi.

## Tài liệu tham khảo
- Stephen Boyd, Lieven Vandenberghe, *Convex Optimization*, Cambridge University Press.

