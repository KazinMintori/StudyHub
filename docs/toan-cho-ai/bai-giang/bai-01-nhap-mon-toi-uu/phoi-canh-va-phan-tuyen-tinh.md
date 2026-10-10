---
course: toan-cho-ai
lecture: bai-01-nhap-mon-toi-uu
topic: phoi-canh-va-phan-tuyen-tinh
section: topic
title: "Phép phối cảnh và hàm phân tuyến tính"
description: "Phép phối cảnh P(z, t) = z/t và cách hiểu bằng máy ảnh lỗ kim, vì sao nó biến đoạn thẳng thành đoạn thẳng nhưng đổi tỉ lệ, ảnh và ảnh ngược của tập lồi, hàm phân tuyến tính, cách nhìn xạ ảnh và ví dụ xác suất có điều kiện."
---

Phép biến đổi affine giữ tính lồi vì nó giữ nguyên đoạn thẳng và tỉ lệ trên đoạn thẳng. Một câu hỏi tự nhiên là: Có phép biến đổi **phi tuyến** nào vẫn giữ tính lồi không? Câu trả lời là có, và ví dụ quan trọng nhất đến từ một thiết bị rất cũ: Máy ảnh lỗ kim. Nhìn một vật lồi qua một lỗ kim, ảnh thu được trên màn vẫn lồi, dù kích thước và tỉ lệ đã bị bóp méo theo khoảng cách.

Trang này nghiên cứu phép biến đổi ấy, gọi là **phép phối cảnh**, cùng họ hàm rộng hơn được xây từ nó là **hàm phân tuyến tính**. Bài học sâu nhất ở đây là sự khác nhau giữa hai điều tưởng giống nhau: Giữ đoạn thẳng và giữ tỉ lệ trên đoạn thẳng. Tính lồi chỉ cần điều thứ nhất.

## 1. Phép phối cảnh

> **Định nghĩa.** **Phép phối cảnh** $P : \mathbb{R}^{n+1} \to \mathbb{R}^n$ được định nghĩa bởi $P(z, t) = z/t$, với miền xác định $\operatorname{dom} P = \mathbb{R}^n \times \mathbb{R}_{++}$, tức là chỉ những điểm có tọa độ cuối $t > 0$.

Bằng lời, phép phối cảnh chia vector cho thành phần cuối để thành phần đó bằng 1, rồi bỏ thành phần đó đi. Chẳng hạn $P(6, 4, 2) = (3, 2)$. Mọi điểm trên cùng một tia xuất phát từ gốc (trong nửa không gian $t > 0$) có cùng ảnh: $P(2, 2) = P(3, 3) = 1$. Như vậy phép phối cảnh "quên" khoảng cách tới gốc và chỉ giữ lại hướng.

Một mô hình trực quan kinh điển giúp làm sáng tỏ phép phối cảnh là mô hình máy ảnh lỗ kim (pinhole camera). Một máy ảnh lỗ kim trong không gian $\mathbb{R}^3$ gồm một mặt chắn sáng nằm ngang $x_3 = 0$ có một lỗ nhỏ tại gốc tọa độ, và một màn ảnh thu nhận nằm ngang $x_3 = -1$. Một vật thể tại vị trí $x$ nằm phía trên mặt chắn ($x_3 > 0$) sẽ tạo ảnh tại điểm $-(x_1/x_3,\ x_2/x_3,\ 1)$ trên màn ảnh, bởi vì tia sáng truyền thẳng qua lỗ kim. Bỏ đi thành phần cao độ cuối luôn bằng $-1$, vị trí ảnh của $x$ chính là $-P(x)$. Khi vật thể càng ra xa (tức tọa độ chiều sâu $x_3$ càng lớn), kích thước ảnh càng thu nhỏ và hội tụ về tâm màn ảnh, hoàn toàn khớp với trải nghiệm thị giác thực tế.

## 2. Đoạn thẳng biến thành đoạn thẳng, nhưng tỉ lệ thay đổi

Cả trang dựa vào phép tính sau. Lấy hai điểm $x = (\tilde x, x_{n+1})$ và $y = (\tilde y, y_{n+1})$ với $x_{n+1} > 0$ và $y_{n+1} > 0$. Với $0 \le \theta \le 1$, ta tính ảnh của điểm trên đoạn nối chúng:

$$
P(\theta x + (1 - \theta) y) = \frac{\theta \tilde x + (1-\theta) \tilde y}{\theta x_{n+1} + (1-\theta) y_{n+1}} .
$$

Mẹo là viết mỗi $\tilde x$ thành $x_{n+1} \cdot P(x)$ và mỗi $\tilde y$ thành $y_{n+1} \cdot P(y)$. Khi đó vế phải bằng

$$
\frac{\theta x_{n+1}}{\theta x_{n+1} + (1-\theta) y_{n+1}} P(x) + \frac{(1-\theta) y_{n+1}}{\theta x_{n+1} + (1-\theta) y_{n+1}} P(y) = \mu P(x) + (1 - \mu) P(y),
$$

với

$$
\mu = \frac{\theta x_{n+1}}{\theta x_{n+1} + (1-\theta) y_{n+1}} \in [0, 1].
$$

Vậy ảnh của điểm ứng với tỉ lệ $\theta$ trên đoạn $[x, y]$ là điểm ứng với tỉ lệ **khác** $\mu$ trên đoạn $[P(x), P(y)]$. Hai chi tiết quyết định nằm trong công thức của $\mu$. Thứ nhất, mẫu số dương vì cả $x_{n+1}$ và $y_{n+1}$ dương, nên $\mu$ xác định và thuộc $[0, 1]$. Thứ hai, $\mu$ tăng đơn điệu theo $\theta$, đi từ 0 khi $\theta = 0$ tới 1 khi $\theta = 1$. Do đó khi $\theta$ quét hết đoạn $[x, y]$, $\mu$ quét hết đoạn $[P(x), P(y)]$, và ta có $P([x, y]) = [P(x), P(y)]$.

Hai tỉ lệ $\theta$ và $\mu$ chỉ trùng nhau khi $x_{n+1} = y_{n+1}$, tức là hai điểm "cách máy ảnh" như nhau. Điểm gần hơn (tọa độ cuối nhỏ hơn) chiếm phần lớn hơn trên ảnh. Người vẽ tranh biết hiện tượng phối cảnh này từ lâu: Một con đường thẳng chạy ra xa trông như thu hẹp lại, và những đoạn bằng nhau ở xa trông ngắn hơn những đoạn ở gần.

::: example Trung điểm không còn là trung điểm
Với $u = (1, 1)$ và $v = (6, 3)$ trong $\mathbb{R}^2$, ta có $P(u) = 1$ và $P(v) = 2$. Trung điểm $\tfrac12(u + v) = (3.5, 2)$ có ảnh $\tfrac{3.5}{2} = 1.75$, trong khi trung điểm của hai ảnh là $1.5$. Công thức cho $\mu = \tfrac{0.5 \cdot 1}{0.5 \cdot 1 + 0.5 \cdot 3} = \tfrac14$, và quả thật $\tfrac14 \cdot 1 + \tfrac34 \cdot 2 = 1.75$. Điểm $v$ ở xa hơn ($t = 3$) nhưng lại "kéo" ảnh của trung điểm về phía nó, vì phần đoạn thẳng gần $v$ bị nén lại khi chiếu.
:::

<PerspectiveLab />

## 3. Phép phối cảnh giữ tính lồi

Từ kết quả "đoạn thẳng thành đoạn thẳng", tính lồi của ảnh suy ra ngay. Nếu $C$ lồi và nằm trong $\operatorname{dom} P$, lấy hai điểm $P(x), P(y)$ của $P(C)$ với $x, y \in C$. Đoạn $[P(x), P(y)]$ là ảnh của đoạn $[x, y]$, mà đoạn $[x, y] \subseteq C$ vì $C$ lồi. Vậy đoạn $[P(x), P(y)] \subseteq P(C)$, tức $P(C)$ lồi. Về mặt trực giác hình học: Một vật thể lồi khi quan sát qua máy ảnh lỗ kim luôn cho một ảnh thu được là một tập lồi.

Ảnh ngược cũng giữ tính lồi. Với $C \subseteq \mathbb{R}^n$ lồi,

$$
P^{-1}(C) = \{(x, t) \in \mathbb{R}^{n+1} : X/t \in C,\ t > 0\}
$$

là tập lồi. Chứng minh dùng đúng mẹo ở mục 2 theo chiều ngược lại: Với $(x, t), (y, s) \in P^{-1}(C)$ và $\theta \in [0, 1]$,

$$
\frac{\theta x + (1 - \theta) y}{\theta t + (1 - \theta) s} = \mu \frac{x}{t} + (1 - \mu) \frac{y}{s}, \qquad \mu = \frac{\theta t}{\theta t + (1 - \theta) s} \in [0, 1],
$$

nên điểm này thuộc $C$ vì là tổ hợp lồi của hai điểm thuộc $C$. Một cách hình dung: Tập $P^{-1}(C)$ là hợp của mọi tia từ gốc đi qua tập $C$ đặt ở độ cao $t = 1$, tức là **nón** sinh bởi $C$ (bỏ đi gốc tọa độ). Tập ảnh ngược này sẽ xuất hiện lại khi ta nói về phối cảnh của một hàm ở chủ đề về các phép toán giữ tính lồi của hàm.

Phép phối cảnh **không** phải hàm affine, và nó cũng không giữ mọi thứ mà hàm affine giữ. Nó giữ đoạn thẳng nhưng không giữ trung điểm, không giữ tỉ lệ, và tất nhiên không giữ khoảng cách. Tính lồi sống sót chỉ vì tính lồi không cần tới những thứ đó.

## 4. Hàm phân tuyến tính

Ghép một hàm affine với phép phối cảnh, ta được một họ hàm rộng hơn.

> **Định nghĩa.** Cho $A \in \mathbb{R}^{m \times n}$, $b \in \mathbb{R}^m$, $c \in \mathbb{R}^n$, $d \in \mathbb{R}$. Hàm
> $$f(x) = \frac{Ax + b}{c^T x + d}, \qquad \operatorname{dom} f = \{x : c^T x + d > 0\},$$
> được gọi là **hàm phân tuyến tính** (linear-fractional, hay projective function).

Tử số là một vector, mẫu số là một số vô hướng. Hàm này là hợp $f = P \circ g$ của ánh xạ affine $g(x) = (Ax + b,\ c^T x + d)$ với phép phối cảnh. Khi $c = 0$ và $d > 0$, miền xác định là cả $\mathbb{R}^n$ và $f$ là một hàm affine, nên hàm affine là trường hợp riêng của hàm phân tuyến tính. Hàm một biến $1/x$ trên $x > 0$ cũng là hàm phân tuyến tính, với $A = 0$, $b = 1$, $c = 1$, $d = 0$.

Vì cả hai thành phần đều giữ tính lồi, hàm phân tuyến tính cũng vậy. Nếu $C$ lồi và nằm trong $\operatorname{dom} f$, thì $f(C)$ lồi: Ánh xạ affine biến $C$ thành một tập lồi nằm trong nửa không gian có tọa độ cuối dương, rồi phép phối cảnh giữ tính lồi. Tương tự, nếu $C$ lồi thì $f^{-1}(C)$ lồi.

Điều kiện "$C$ nằm trong miền xác định" là bắt buộc, và không phải chi tiết hình thức. Hàm $1/x$ biến đoạn $[1, 2]$ thành đoạn $[\tfrac12, 1]$, một tập lồi. Nhưng nếu áp nó lên tập $[-1, -\tfrac12] \cup [\tfrac12, 1]$, hay tệ hơn là một đoạn chứa $0$ như $[-1, 1]$ (bỏ điểm 0), ảnh thu được là hai nửa đường thẳng rời nhau. Mẫu số đổi dấu thì mọi lập luận về $\mu$ ở mục 2 sụp đổ, vì $\mu$ không còn nằm trong $[0, 1]$.

::: example Ảnh của một tam giác
Xét $f(x) = \dfrac{x}{x_1 + x_2 + 1}$ trên $\mathbb{R}^2$, với miền xác định $\{x : x_1 + x_2 + 1 > 0\}$. Xét tam giác có ba đỉnh là $(0, 0)$, $(2, 0)$ và $(0, 2)$, tam giác này nằm trọn trong miền xác định của hàm số. Ba đỉnh lần lượt có ảnh là $(0, 0)$, $(\tfrac23, 0)$ và $(0, \tfrac23)$. Vì đoạn thẳng biến thành đoạn thẳng và ba cạnh biến thành ba cạnh, nên ảnh thu được là một tam giác có ba đỉnh vừa tìm. Tuy nhiên, tỉ lệ khoảng cách bị thay đổi: Trung điểm $(1, 0)$ của cạnh đáy có ảnh là $(\tfrac12, 0)$, trong khi trung điểm của đoạn ảnh cạnh đáy là $(\tfrac13, 0)$.
:::

Dưới góc nhìn **hình học xạ ảnh** (projective geometry), ta có thể giải thích rõ nét bản chất của tên gọi "projective". Đồng nhất mỗi điểm $z \in \mathbb{R}^n$ với tia $\{t(z, 1) : t > 0\}$ trong $\mathbb{R}^{n+1}$. Khi đó hàm phân tuyến tính tương ứng với phép nhân ma trận $Q = \begin{bmatrix} A & b \\ c^T & d \end{bmatrix}$ lên tia ấy, rồi đọc lại điểm từ tia mới. Trong đồ họa máy tính và thị giác máy tính, cách viết này được gọi là **tọa độ thuần nhất** (homogeneous coordinates): Một điểm $(x, y)$ được lưu thành $(x, y, 1)$, và mọi phép chiếu phối cảnh của camera trở thành một phép nhân ma trận theo sau bởi một phép chia chuẩn hóa.

## 5. Xác suất có điều kiện là một hàm phân tuyến tính

Một ứng dụng sâu sắc của phép phân tuyến tính xuất hiện trực tiếp trong lý thuyết xác suất và suy diễn thống kê. Gọi $u \in \{1, \dots, n\}$ và $v \in \{1, \dots, m\}$ là hai biến ngẫu nhiên rời rạc, với phân phối xác suất đồng thời là ma trận các phần tử $p_{ij} = \operatorname{prob}(u = i, v = j)$. Khi đó, phân phối xác suất có điều kiện được tính bởi:

$$
f_{ij} = \operatorname{prob}(u = i \mid v = j) = \frac{p_{ij}}{\sum_{k=1}^{n} p_{kj}} = \frac{p_{ij}}{p_{1j} + p_{2j} + \dots + p_{nj}} .
$$

Tử số $p_{ij}$ là hàm tuyến tính theo $p$, và mẫu số $\sum_{k=1}^n p_{kj}$ cũng là hàm tuyến tính theo $p$, đồng thời mẫu số luôn dương khi $\operatorname{prob}(v = j) > 0$. Như vậy, ánh xạ biến đổi từ phân phối xác suất đồng thời sang phân phối xác suất có điều kiện là một hàm phân tuyến tính.
Hệ quả: Nếu $C$ là một tập lồi các phân phối đồng thời (chẳng hạn tập các phân phối thỏa mãn một số ràng buộc tuyến tính về kỳ vọng), thì tập các phân phối có điều kiện tương ứng cũng là một tập lồi.

Ví dụ nhỏ sau cho thấy "đổi tỉ lệ" của mục 2 trong ngữ cảnh xác suất. Xét cột $v = 1$ của hai phân phối đồng thời: Phân phối thứ nhất có $p_{11} = 0.1$, $p_{21} = 0.3$, cho $f_{11} = \tfrac14$, còn phân phối thứ hai có $p_{11} = 0.4$, $p_{21} = 0.1$, cho $f_{11} = \tfrac45$. Trộn hai phân phối đồng thời với tỉ lệ $\tfrac12$, ta được $p_{11} = 0.25$, $p_{21} = 0.2$, và $f_{11} = \tfrac{0.25}{0.45} = \tfrac59$. Kết quả này **không phải** trung bình $\tfrac{21}{40}$ của hai xác suất có điều kiện, nhưng vẫn nằm giữa chúng, ứng với tỉ lệ $\mu = \tfrac49$. Phân phối nào có $\operatorname{prob}(v = 1)$ lớn hơn thì có tiếng nói lớn hơn, đúng như điểm "gần máy ảnh" ở mục 2.

## 6. Những câu hỏi để đào sâu

**Câu 1.** Ảnh của một đường thẳng (không đi qua gốc) nằm trong miền $t > 0$ qua phép phối cảnh là gì? Còn ảnh của một tia từ gốc?

<details><summary>Xem lời giải thích</summary>

Mọi điểm trên một tia từ gốc có cùng ảnh, nên ảnh của tia là **một điểm**. Một đường thẳng không qua gốc, nằm trọn trong miền $t > 0$, phải song song với siêu phẳng $t = 0$ (nếu không nó sẽ cắt $t = 0$). Khi đó tọa độ cuối không đổi trên đường thẳng, và phép phối cảnh chỉ là một phép co giãn, nên ảnh là một đường thẳng. Với một **nửa** đường thẳng đi lên ra xa, chẳng hạn $\{(s, 1 + s) : s \ge 0\}$, ảnh là $\{\tfrac{s}{1+s}\} = [0, 1)$, một đoạn không chứa đầu mút 1. Nửa đường thẳng vô hạn bị "co" lại thành một đoạn hữu hạn, như đường ray chạy tới đường chân trời.

</details>

**Câu 2.** Vì sao miền xác định của phép phối cảnh lại là $t > 0$ chứ không phải $t \ne 0$? Nếu cho phép $t < 0$, kết quả về tính lồi còn đúng không?

<details><summary>Xem lời giải thích</summary>

Nếu cho phép cả $t > 0$ lẫn $t < 0$, một đoạn thẳng có thể cắt qua $t = 0$, và ảnh của nó gồm hai nửa đường thẳng tách rời, không lồi. Chẳng hạn đoạn nối $(1, 1)$ và $(1, -1)$ trong $\mathbb{R}^2$: Ảnh các điểm $(1, t)$ là $1/t$, chạy từ $1$ tới $+\infty$ khi $t$ giảm về $0^+$, và từ $-\infty$ tới $-1$ khi $t$ đi từ $0^-$ về $-1$. Nếu chỉ dùng một phía, chẳng hạn $t < 0$, thì kết quả vẫn đúng bằng cùng lập luận, chỉ là quy ước chuẩn tắc trong tối ưu hóa chọn nửa không gian $t > 0$ để đồng nhất với chiều dương của khoảng cách. Điều quan trọng là mọi điểm của tập phải nằm cùng một phía.

</details>

**Câu 3.** Hàm $f(x) = \dfrac{x_1}{x_2}$ trên miền $x_2 > 0$ là phân tuyến tính. Tập $\{x : x_2 > 0,\ \tfrac{x_1}{x_2} \le 3\}$ có lồi không? Hãy trả lời bằng hai cách: Dùng ảnh ngược, và biến đổi trực tiếp.

<details><summary>Xem lời giải thích</summary>

Cách thứ nhất: Tập là ảnh ngược của nửa đường thẳng lồi $(-\infty, 3]$ qua hàm phân tuyến tính $f$, nên lồi. Cách thứ hai: Vì $x_2 > 0$, nhân hai vế với $x_2$ không đổi chiều, nên điều kiện tương đương $x_1 \le 3x_2$, một nửa mặt phẳng. Giao với nửa mặt phẳng mở $x_2 > 0$ là một tập lồi. Cách thứ hai cho thấy một mẹo quan trọng trong quy hoạch phân tuyến tính: Khi mẫu số có dấu xác định, nhân chéo biến ràng buộc phân thức thành ràng buộc tuyến tính.

</details>

## 7. Bài tập tự luyện

::: exercise 1. Tính μ
Với $x = (2, 4)$ và $y = (6, 1)$ trong $\mathbb{R}^2$ (thành phần cuối là $t$), tính $P(x)$, $P(y)$, ảnh của điểm $\theta x + (1-\theta) y$ với $\theta = \tfrac13$, và giá trị $\mu$ tương ứng. Kiểm tra đẳng thức

$$
P(\theta x + (1 - \theta) y) = \mu P(x) + (1 - \mu) P(y).
$$
:::

::: solution
$P(x) = \tfrac24 = \tfrac12$ và $P(y) = 6$. Điểm $\tfrac13 x + \tfrac23 y = (\tfrac23 + 4,\ \tfrac43 + \tfrac23) = (\tfrac{14}{3}, 2)$ có ảnh $\tfrac{14}{3} \cdot \tfrac12 = \tfrac73$. Công thức cho $\mu = \tfrac{\frac13 \cdot 4}{\frac13 \cdot 4 + \frac23 \cdot 1} = \tfrac{4/3}{2} = \tfrac23$. Kiểm tra: Ta có $\tfrac23 \cdot \tfrac12 + \tfrac13 \cdot 6 = \tfrac13 + 2 = \tfrac73$, đúng.
:::

::: exercise 2. Ảnh ngược của một nửa không gian qua hàm phân tuyến tính
Cho $f(x) = \dfrac{Ax + b}{c^T x + d}$ với miền $c^T x + d > 0$, và $C = \{y : g^T y \le h\}$. Mô tả $f^{-1}(C)$ bằng các bất đẳng thức tuyến tính.
:::

::: solution
$x \in f^{-1}(C)$ khi và chỉ khi $c^T x + d > 0$ và $g^T \dfrac{Ax + b}{c^T x + d} \le h$. Nhân hai vế với số dương $c^T x + d$ được $g^T(Ax + b) \le h(c^T x + d)$, tức $(A^T g - hc)^T x \le hd - g^T b$. Vậy

$$
f^{-1}(C) = \{x : c^T x + d > 0,\ (A^T g - hc)^T x \le hd - g^T b\},
$$

giao của một nửa không gian mở và một nửa không gian đóng.
:::

## Tóm tắt

Phép phối cảnh $P(z, t) = z/t$ trên miền $t > 0$ chia cho tọa độ cuối rồi bỏ nó đi, giống ảnh tạo bởi máy ảnh lỗ kim. Nó biến đoạn thẳng thành đoạn thẳng, nhưng điểm ứng với tỉ lệ $\theta$ biến thành điểm ứng với tỉ lệ $\mu = \tfrac{\theta x_{n+1}}{\theta x_{n+1} + (1-\theta)y_{n+1}}$. Vì tính lồi chỉ cần đoạn thẳng chứ không cần tỉ lệ, ảnh và ảnh ngược của tập lồi qua phép phối cảnh đều lồi.

Hàm phân tuyến tính là hợp của một hàm affine với phép phối cảnh, nên cũng giữ tính lồi, với điều kiện tập đang xét nằm trọn trong miền mẫu số dương. Xác suất có điều kiện là một ví dụ: Ánh xạ từ phân phối đồng thời sang phân phối có điều kiện là phân tuyến tính.

## Tài liệu tham khảo

- Stephen Boyd, Lieven Vandenberghe, *Convex Optimization*, Cambridge University Press.
