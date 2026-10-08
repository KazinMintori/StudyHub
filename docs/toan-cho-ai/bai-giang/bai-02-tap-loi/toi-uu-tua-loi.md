---
course: toan-cho-ai
lecture: bai-02-tap-loi
topic: toi-uu-tua-loi
section: topic
title: "Hàm tựa lồi và phương pháp chia đôi"
description: "Hàm tựa lồi định nghĩa qua tập mức dưới, các ví dụ logarit, hàm đơn điệu, hàm phân tuyến tính và tỉ số khoảng cách, bất đẳng thức Jensen biến thể, những điều đúng với hàm lồi nhưng sai với hàm tựa lồi, biểu diễn tập mức bằng họ hàm lồi và phương pháp chia đôi giải bài toán tựa lồi bằng một dãy bài toán khả thi lồi."
---

Rất nhiều đại lượng ta muốn tối ưu là một tỉ số: chi phí trên mỗi đơn vị sản phẩm, lợi nhuận trên vốn bỏ ra, khoảng cách tới nơi cần phục vụ so với khoảng cách tới nguồn gây nhiễu. Tỉ số hiếm khi là hàm lồi. Thế nhưng ở nhiều tỉ số, tập các phương án đạt một mức cho trước, chẳng hạn mọi vị trí có tỉ số khoảng cách không quá 0.3, lại là một tập lồi. Những hàm có tính chất này được gọi là **hàm tựa lồi**.

Trang này trả lời hai câu hỏi. Hàm tựa lồi giữ lại được những gì của hàm lồi và mất những gì? Và nếu chỉ biết mọi tập mức dưới đều lồi, ta có giải bài toán một cách đáng tin cậy được không? Câu trả lời cho câu thứ hai là có, bằng một thuật toán rất đơn giản: thay vì cực tiểu trực tiếp, ta hỏi đi hỏi lại câu "có phương án nào đạt mức $t$ không?" và chia đôi khoảng chứa đáp án sau mỗi câu hỏi.

## 1. Định nghĩa và ví dụ

Một hàm $f : \mathbb{R}^n \to \mathbb{R}$ là **tựa lồi** nếu miền xác định và mọi tập mức dưới

$$
S_\alpha = \{x \in \operatorname{dom} f : f(x) \le \alpha\}, \qquad \alpha \in \mathbb{R},
$$

đều là tập lồi. Hàm $f$ là **tựa lõm** nếu $-f$ tựa lồi, tức mọi tập mức trên $\{x : f(x) \ge \alpha\}$ đều lồi, và **tựa tuyến tính** nếu vừa tựa lồi vừa tựa lõm. Mọi hàm lồi đều tựa lồi, vì [tập mức dưới của hàm lồi](../bai-01-nhap-mon-toi-uu/epigraph-tap-muc-duoi-jensen.md) luôn lồi, nhưng điều ngược lại sai.

Trên trục số, tập mức dưới lồi nghĩa là một khoảng, nên hàm tựa lồi liên tục trên $\mathbb{R}$ là hàm **đơn đỉnh** theo nghĩa rộng: hoặc không tăng, hoặc không giảm, hoặc không tăng cho tới một điểm rồi không giảm sau điểm đó. Một vài ví dụ cho thấy họ hàm này rộng đến mức nào:

- $\log x$ trên $(0, \infty)$ là hàm lõm, nhưng tựa tuyến tính, vì mọi tập mức đều là khoảng.
- Phần nguyên trên $\lceil x \rceil$ không liên tục, nhưng tựa tuyến tính vì đơn điệu.
- $x^3$ trên $\mathbb{R}$ đơn điệu nên tựa tuyến tính, dù không lồi cũng không lõm.
- Hàm **phân tuyến tính** $\dfrac{a^Tx + b}{c^Tx + d}$ trên miền $c^Tx + d > 0$ tựa tuyến tính. Tập mức dưới mức $\alpha$ gồm các điểm thỏa đồng thời $c^Tx + d > 0$ và $a^Tx + b \le \alpha(c^Tx + d)$, tức giao của một nửa không gian mở và một nửa không gian đóng.
- Tích $x_1x_2$ trên $\mathbb{R}^2_+$ không lồi cũng không lõm, nhưng tựa lõm, vì tập $\{x \succeq 0 : x_1x_2 \ge \alpha\}$ với $\alpha > 0$ là vùng nằm trên một nhánh hyperbol, một tập lồi.
- **Tỉ số khoảng cách** $\|x - a\|_2 / \|x - b\|_2$ tựa lồi trên nửa không gian gồm các điểm gần $a$ hơn $b$. Mục 3 sẽ cho thấy tập mức dưới của nó là những hình cầu.

Tính tựa lồi có một dạng bất đẳng thức Jensen riêng: $f$ tựa lồi khi và chỉ khi miền của nó lồi và

$$
f(\theta x + (1 - \theta)y) \le \max\{f(x), f(y)\}, \qquad 0 \le \theta \le 1 .
$$

Giá trị trên một đoạn thẳng không vượt quá giá trị lớn hơn ở hai đầu mút. So với hàm lồi, vế phải là giá trị lớn nhất chứ không phải trung bình có trọng số, nên điều kiện yếu hơn hẳn.

## 2. Những điều không còn đúng

Ba tính chất quen thuộc của hàm lồi mất đi khi chuyển sang hàm tựa lồi, và cả ba đều quan trọng khi thiết kế thuật toán.

**Đạo hàm bằng 0 không còn đủ.** Hàm $x^3$ tựa lồi và có $f'(0) = 0$, nhưng $x = 0$ chẳng phải cực tiểu, vì hàm giảm mãi về $-\infty$ khi $x$ giảm. Với hàm lồi khả vi, gradient bằng 0 là đủ để kết luận tối ưu. Với hàm tựa lồi thì không.

**Cực tiểu cục bộ có thể không toàn cục.** Một hàm tựa lồi có thể có một đoạn nằm ngang trên phần đang giảm của nó. Mọi điểm bên trong đoạn ấy là cực tiểu cục bộ, vì hàm không đổi quanh đó, nhưng hàm còn giảm tiếp ở phía sau. Chủ đề [cực tiểu cục bộ và toàn cục](../bai-01-nhap-mon-toi-uu/cuc-bo-va-toan-cuc.md) của Lecture 01 đã đưa ra một ví dụ như thế. Định lý "cục bộ là toàn cục" là đặc quyền của bài toán lồi.

**Tổng không còn giữ tính chất.** Hàm $x^3$ và hàm $-3x$ đều đơn điệu, nên đều tựa lồi, nhưng tổng $x^3 - 3x$ có một cực đại cục bộ tại $x = -1$ và một cực tiểu cục bộ tại $x = 1$. Tập mức dưới mức 0 của nó là $(-\infty, -\sqrt3] \cup [0, \sqrt3]$, hai khoảng rời nhau, nên tổng không tựa lồi. Điều này có hệ quả thực tế: cộng một số hạng điều chuẩn lồi vào một hàm mục tiêu tựa lồi có thể làm mất tính tựa lồi.

Một số phép toán vẫn giữ được tính tựa lồi. Giá trị lớn nhất có trọng số không âm của các hàm tựa lồi là tựa lồi, vì tập mức dưới của nó là giao các tập mức dưới. Hợp $h \circ g$ tựa lồi khi $g$ tựa lồi và $h$ không giảm. Hợp với một ánh xạ affine hay phân tuyến tính cũng giữ tính tựa lồi.

## 3. Biểu diễn tập mức bằng một họ hàm lồi

Để giải bài toán, ta cần mô tả tập mức dưới của $f$ bằng những bất đẳng thức mà máy tính xử lý được. Ta tìm một họ hàm lồi $\phi_t$, đánh chỉ số theo $t \in \mathbb{R}$, sao cho

$$
f(x) \le t \iff \phi_t(x) \le 0,
$$

và với mỗi $x$, giá trị $\phi_t(x)$ không tăng theo $t$. Một họ như vậy luôn tồn tại về mặt lý thuyết, chẳng hạn hàm chỉ thị của tập mức dưới, nhưng ta cần một họ có công thức gọn.

Trường hợp quan trọng nhất là tỉ số của một hàm lồi và một hàm lõm. Giả sử $p$ lồi, $p(x) \ge 0$, còn $q$ lõm và $q(x) > 0$ trên một tập lồi. Khi đó $f = p/q$ tựa lồi, và với $t \ge 0$,

$$
\frac{p(x)}{q(x)} \le t \iff p(x) - t\,q(x) \le 0 .
$$

Hàm $\phi_t = p - tq$ lồi, vì $p$ lồi và $-tq$ lồi khi $t \ge 0$, và nó không tăng theo $t$ vì $q > 0$. Phép nhân chéo ở đây hợp lệ chính vì mẫu số dương.

Tỉ số khoảng cách cần một họ khác, vì $\|x - a\| - t\|x - b\|$ là hiệu của hai hàm lồi và không lồi. Ta bình phương trước: với $0 < t < 1$,

$$
\frac{\|x - a\|_2}{\|x - b\|_2} \le t \iff \phi_t(x) = \|x - a\|_2^2 - t^2\|x - b\|_2^2 \le 0 .
$$

Phép bình phương hợp lệ vì cả hai vế không âm. Hàm $\phi_t$ là hàm toàn phương với hệ số của $\|x\|^2$ bằng $1 - t^2 > 0$, nên lồi, và nó không tăng theo $t$. Tập $\{\phi_t \le 0\}$ là một hình tròn, giới hạn bởi một đường tròn Apollonius:

$$
\text{tâm}\ \ \frac{a - t^2 b}{1 - t^2}, \qquad \text{bán kính}\ \ \frac{t\,\|a - b\|_2}{1 - t^2}.
$$

Hàm tỉ số này thật sự không lồi. Đi dọc một tia xuất phát từ $a$, tỉ số tăng từ 0 và tiến dần tới 1 khi điểm đi ra xa, mà một hàm lồi bị chặn trên dọc một tia thì không thể tăng. Chẳng hạn với $a = (0, 0)$ và $b = (4, 0)$, ở độ cao $x_2 = 8$ trên trục tung tỉ số là khoảng 0.894, ở độ cao 100 là khoảng 0.999, còn ở độ cao 54, trung điểm của hai vị trí ấy, tỉ số là khoảng 0.997, cao hơn trung bình 0.947 của hai đầu. Đồ thị vượt lên trên dây cung.

## 4. Phương pháp chia đôi

Gọi $p^\star$ là giá trị tối ưu của bài toán tựa lồi. Với một mức $t$, xét bài toán khả thi

$$
\text{find}\ x \qquad \text{subject to}\quad \phi_t(x) \le 0,\quad x \in X .
$$

Đây là một bài toán khả thi lồi. Nếu nó có nghiệm thì $p^\star \le t$, và nghiệm ấy là một phương án có giá trị không quá $t$. Nếu nó vô nghiệm thì mọi phương án đều có giá trị lớn hơn $t$, nên $p^\star \ge t$. Mỗi câu hỏi "có hay không" vì thế cắt đôi phần trục số còn nghi ngờ, và Thuật toán 4.1 của sách khai thác đúng điều đó.

> **Thuật toán chia đôi.** Cho $l \le p^\star \le u$ và sai số $\varepsilon > 0$. Lặp lại: đặt $t = (l + u)/2$, giải bài toán khả thi tại mức $t$. Nếu khả thi, đặt $u = t$, nếu không, đặt $l = t$. Dừng khi $u - l \le \varepsilon$.

Khoảng $[l, u]$ luôn chứa $p^\star$, và độ dài của nó giảm một nửa sau mỗi lần lặp. Sau $k$ lần lặp, độ dài là $2^{-k}(u - l)$, nên thuật toán dừng sau đúng $\lceil \log_2((u - l)/\varepsilon) \rceil$ lần.

Hãy áp dụng cho một ví dụ tự đặt. Cần đặt một bộ phát tín hiệu trong vùng $X = [-1, 1.5] \times [1, 3]$ sao cho nó gần người dùng ở $a = (0, 0)$ và xa nguồn nhiễu ở $b = (4, 0)$, theo nghĩa tỉ số $\|x - a\|/\|x - b\|$ nhỏ nhất. Cả vùng $X$ nằm trong nửa mặt phẳng $x_1 \le 2$, nơi hàm tỉ số tựa lồi. Trên $X$ tỉ số luôn nhỏ hơn 1, nên ta xuất phát từ $[l, u] = [0, 1]$. Với $\varepsilon = 0.01$, cần $\lceil \log_2 100 \rceil = 7$ lần. Lần đầu thử $t = 0.5$: hình tròn khá lớn và chạm $X$, nên $p^\star \le 0.5$. Lần hai thử $t = 0.25$, vẫn chạm. Lần ba thử $t = 0.125$, hình tròn quá nhỏ, nên $p^\star \ge 0.125$. Sau bảy lần, $p^\star$ bị kẹp trong $[0.2344, 0.2422]$.

Giá trị đúng là $p^\star = \sqrt5 - 2 \approx 0.2361$, đạt tại $x^\star = (2 - \sqrt5,\ 1) \approx (-0.236,\ 1)$ trên cạnh dưới của $X$. Ở đúng mức này, hình tròn Apollonius có tâm $(-0.236, 0)$ và bán kính bằng 1, nên nó tiếp xúc với cạnh $x_2 = 1$ tại đúng điểm $x^\star$.

<BisectionLab />

Điều đáng chú ý là thuật toán không bao giờ tính giá trị hay đạo hàm của $f$. Nó chỉ cần một công cụ trả lời được câu hỏi khả thi của một bài toán lồi, và công cụ ấy có sẵn cho mọi lớp bài toán lồi ở các chủ đề sau. Cái giá phải trả là ta giải nhiều bài toán thay vì một, nhưng số lần chỉ tăng theo logarit của độ chính xác: muốn sai số $10^{-6}$ trên một khoảng dài 10 thì cũng chỉ cần 24 lần.

## 5. Điều kiện tối ưu bậc nhất cho bài toán tựa lồi

Với hàm mục tiêu tựa lồi khả vi trên miền khả thi lồi $X$, sách đưa ra một điều kiện đủ: nếu $x \in X$ và

$$
\nabla f_0(x)^T(y - x) > 0 \quad \text{với mọi } y \in X \setminus \{x\},
$$

thì $x$ tối ưu. So với [điều kiện tối ưu của bài toán lồi](../bai-01-nhap-mon-toi-uu/dieu-kien-toi-uu.md), có hai khác biệt. Điều kiện này chỉ đủ chứ không cần, và nó đòi hỏi bất đẳng thức chặt, nên gradient phải khác 0. Ví dụ $x^3$ cho thấy vì sao: tại $x = 0$ gradient bằng 0, mọi bất đẳng thức không chặt đều thỏa, nhưng điểm ấy không tối ưu.

## 6. Những câu hỏi để đào sâu

**Câu 1.** Hàm $\operatorname{card}(x)$ đếm số thành phần khác 0 của $x \in \mathbb{R}^n$. Nó có tựa lồi không? Điều này nói gì về bài toán chọn đặc trưng thưa trong học máy?

<details><summary>Xem lời giải thích</summary>

Không. Với $n = 2$, tập mức dưới $\{x : \operatorname{card}(x) \le 1\}$ là hợp của hai trục tọa độ. Hai điểm $(1, 0)$ và $(0, 1)$ thuộc tập, nhưng trung điểm $(\tfrac12, \tfrac12)$ có hai thành phần khác 0, nên tập không lồi. Vì vậy ràng buộc "dùng nhiều nhất $k$ đặc trưng" không đưa được về một bài toán tựa lồi, và bài toán chọn tập đặc trưng tốt nhất nói chung là bài toán tổ hợp khó. Đây là lý do người ta thay số đặc trưng bằng chuẩn $\ell_1$, một hàm lồi, như chủ đề [tối ưu vector](./toi-uu-vector-va-danh-doi.md) sẽ bàn. Thú vị là sách chỉ ra rằng $\operatorname{card}$ tựa lõm trên $\mathbb{R}^n_+$, nhưng tính chất ấy không giúp gì cho bài toán cực tiểu.

</details>

**Câu 2.** Trong phương pháp chia đôi, nếu bộ giải bài toán khả thi đôi khi trả lời sai, chẳng hạn vì sai số số học khi hình tròn chỉ vừa chạm miền khả thi, thì điều gì xảy ra?

<details><summary>Xem lời giải thích</summary>

Một câu trả lời sai đẩy khoảng $[l, u]$ sang nhầm nửa, và từ đó trở đi khoảng không còn chứa $p^\star$. Thuật toán không tự phát hiện được lỗi, vì nó không bao giờ quay lại kiểm tra các mức cũ. Có điều, những câu hỏi khó trả lời nhất là những câu có $t$ rất gần $p^\star$, nên một lỗi như thế chỉ làm sai lệch ở mức cỡ sai số của bộ giải. Vì vậy nên dừng chia đôi khi $\varepsilon$ còn lớn hơn sai số của bộ giải, và giữ lại điểm khả thi tìm được ở lần "khả thi" gần nhất, vì điểm đó là bằng chứng chắc chắn rằng $p^\star \le u$.

</details>

**Câu 3.** Không phải tỉ số nào cũng chỉ dừng ở mức tựa lồi. Hãy chứng minh rằng chi phí trung bình $f(x) = \dfrac{x_1^2 + 2x_2^2 + 1}{x_1 + x_2}$ là một hàm lồi trên miền $x_1 + x_2 > 0$.

<details><summary>Xem lời giải thích</summary>

Viết tử số thành bình phương chuẩn của một vector phụ thuộc affine vào $x$: $x_1^2 + 2x_2^2 + 1 = \|u\|_2^2$ với $u = (x_1,\ \sqrt2\,x_2,\ 1)$. Mẫu số $s = x_1 + x_2$ cũng affine. Hàm $(u, s) \mapsto \|u\|_2^2 / s$ trên $s > 0$ là phép [phối cảnh](../bai-01-nhap-mon-toi-uu/phep-toan-giu-tinh-loi-cua-ham.md) của hàm lồi $\|u\|_2^2$, nên lồi đồng thời theo $(u, s)$. Hợp với một ánh xạ affine giữ tính lồi, nên $f$ lồi. Một kiểm tra bằng số cũng xác nhận Hessian của $f$ nửa xác định dương ở mọi điểm thử trên miền đó. Bài học là trước khi dùng công cụ cho hàm tựa lồi, hãy thử xem tỉ số có phải một hàm lồi trá hình không, vì bài toán lồi có nhiều công cụ hơn hẳn.

</details>

**Câu 4.** Hàm phân tuyến tính vừa tựa lồi vừa tựa lõm. Như vậy bài toán cực đại một hàm phân tuyến tính trên đa diện có dễ không?

<details><summary>Xem lời giải thích</summary>

Có. Cực đại $f$ tương đương cực tiểu $-f$, và $-f$ cũng là một hàm phân tuyến tính, nên cũng tựa lồi. Phương pháp chia đôi áp dụng được cho cả hai chiều. Chủ đề [quy hoạch phân tuyến tính](./quy-hoach-phan-tuyen-tinh.md) còn chỉ ra một cách tốt hơn: một phép đổi biến đưa bài toán về đúng một LP, không cần chia đôi. Đây là điểm khác với hàm lồi thông thường, nơi cực đại một hàm lồi trên đa diện có thể rất khó.

</details>

**Câu 5.** Với $f = p/q$, một bạn đề xuất cực tiểu $p(x) - t\,q(x)$ với một $t$ cố định thay cho $f$. Đề xuất này đúng ở chỗ nào và thiếu ở chỗ nào?

<details><summary>Xem lời giải thích</summary>

Đề xuất đúng ở chỗ: với $t = p^\star$, giá trị nhỏ nhất của $p - p^\star q$ trên miền khả thi bằng 0 và đạt đúng tại nghiệm của bài toán gốc, vì $p(x) - p^\star q(x) \ge 0$ trên miền với dấu bằng khi $f(x) = p^\star$. Chỗ thiếu là ta không biết trước $p^\star$. Với một $t$ khác, cực tiểu của $p - tq$ cho một điểm khác. Phương pháp chia đôi chính là một cách tìm $t$ đúng. Cũng có những thuật toán hội tụ nhanh hơn, cập nhật $t$ bằng giá trị $f$ tại nghiệm vừa tìm được thay vì lấy trung điểm.

</details>

## 7. Bài tập tự luyện

::: exercise 1. Nhận diện hàm tựa lồi
Với mỗi hàm sau, hãy cho biết nó có tựa lồi trên miền đã cho không, và nếu có thì vì sao: (a) $f(x) = \dfrac{x^2 + 4}{x}$ trên $x > 0$. (b) $f(x) = e^{-x^2}$ trên $\mathbb{R}$. (c) $f(x) = -e^{-x^2}$ trên $\mathbb{R}$. (d) $f(x_1, x_2) = \max\{x_1 / x_2,\ x_2 / x_1\}$ trên $\mathbb{R}^2_{++}$.
:::

::: solution
(a) Tựa lồi, vì là tỉ số của hàm lồi không âm $x^2 + 4$ và hàm tuyến tính dương $x$. Thực ra hàm $x + 4/x$ còn lồi. (b) Không tựa lồi: tập mức dưới mức $\tfrac12$ là hai nửa đường thẳng $|x| \ge \sqrt{\log 2}$, không lồi. Hàm này tựa lõm, vì nó tăng rồi giảm. (c) Tựa lồi, vì nó giảm rồi tăng, dù không lồi khi $|x|$ lớn. (d) Tựa lồi, vì là giá trị lớn nhất của hai hàm phân tuyến tính, mỗi hàm tựa lồi trên miền dương.
:::

::: exercise 2. Chia đôi bằng tay
Dùng phương pháp chia đôi cho bài toán cực tiểu $f(x) = \dfrac{x^2 + 4}{x}$ trên đoạn $[3, 5]$. Viết bài toán khả thi tại mức $t$, chạy ba lần lặp từ $[l, u] = [4, 6]$, rồi so với nghiệm đúng.
:::

::: hint
Với $x > 0$, $f(x) \le t$ tương đương $x^2 - tx + 4 \le 0$. Tập nghiệm của bất phương trình bậc hai này là một đoạn, cần xem đoạn đó có chạm $[3, 5]$ không.
:::

::: solution
Bài toán khả thi tại mức $t$ là tìm $x \in [3, 5]$ với $x^2 - tx + 4 \le 0$. Khi $t \ge 4$, tập nghiệm là đoạn giữa hai nghiệm $\tfrac{t \pm \sqrt{t^2 - 16}}{2}$. Lần 1: $t = 5$, đoạn là $[1, 4]$, chạm $[3, 5]$, nên $u = 5$. Lần 2: $t = 4.5$, đoạn là khoảng $[1.219, 3.281]$, vẫn chạm, nên $u = 4.5$. Lần 3: $t = 4.25$, đoạn là khoảng $[1.407, 2.843]$, không chạm $[3, 5]$, nên $l = 4.25$. Sau ba lần, $p^\star \in [4.25, 4.5]$. Hàm $x + 4/x$ tăng trên $[3, 5]$ vì $x > 2$, nên nghiệm là $x^\star = 3$ với $p^\star = \tfrac{13}{3} \approx 4.333$, đúng nằm trong khoảng tìm được.
:::

::: exercise 3. Số lần lặp
Biết $p^\star$ nằm trong $[0, 10]$. Cần bao nhiêu lần chia đôi để biết $p^\star$ với sai số không quá $10^{-6}$? Nếu mỗi bài toán khả thi mất 0.2 giây thì tổng thời gian là bao nhiêu?
:::

::: solution
Số lần là $\lceil \log_2(10 / 10^{-6}) \rceil = \lceil \log_2 10^7 \rceil = 24$, vì $2^{23}$ khoảng $8.4 \times 10^6$, nhỏ hơn $10^7$, còn $2^{24}$ khoảng $1.68 \times 10^7$, lớn hơn $10^7$. Tổng thời gian khoảng $24 \times 0.2 = 4.8$ giây.
:::

## Tóm tắt

Hàm tựa lồi là hàm có mọi tập mức dưới lồi. Họ hàm này rộng hơn hàm lồi nhiều: nó chứa logarit, các hàm đơn điệu, hàm phân tuyến tính, tỉ số của hàm lồi với hàm lõm và tỉ số khoảng cách. Đổi lại, ba tính chất quan trọng bị mất: gradient bằng 0 không còn đủ, cực tiểu cục bộ có thể không toàn cục, và tổng của hai hàm tựa lồi có thể không tựa lồi.

Bài toán tựa lồi vẫn giải được một cách đáng tin cậy. Mô tả tập mức dưới bằng một họ hàm lồi $\phi_t$, ta biến câu hỏi "$p^\star \le t$ hay không" thành một bài toán khả thi lồi. Phương pháp chia đôi hỏi câu đó tại trung điểm của khoảng nghi ngờ, và sau $\lceil \log_2((u - l)/\varepsilon) \rceil$ lần thì xác định được $p^\star$ với sai số $\varepsilon$.

## Nguồn và đọc thêm

- S. Boyd, L. Vandenberghe, *Convex Optimization*, §3.4 (tr. 95–104) về hàm tựa lồi, các Ví dụ 3.29, 3.31, 3.32, 3.33, 3.35 và 3.38. §4.2.5 (tr. 144–146) về bài toán tựa lồi, điều kiện tối ưu (4.25) và Thuật toán 4.1.
- Ví dụ đặt bộ phát với tỉ số khoảng cách, mô phỏng, ví dụ $x^3 - 3x$, ví dụ chi phí trung bình lồi, các câu hỏi và bài tập do người soạn bổ sung. Mọi con số đã được tính lại bằng chương trình.
