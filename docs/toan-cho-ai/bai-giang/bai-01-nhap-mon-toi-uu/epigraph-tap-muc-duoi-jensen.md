---
course: toan-cho-ai
lecture: bai-01-nhap-mon-toi-uu
topic: epigraph-tap-muc-duoi-jensen
section: topic
title: "Epigraph, tập mức dưới và bất đẳng thức Jensen"
description: "Ba cây cầu nối hàm lồi với tập lồi và xác suất: tập mức dưới lồi và chiều ngược sai, epigraph lồi khi và chỉ khi hàm lồi cùng mẹo viết bài toán ở dạng epigraph, bất đẳng thức Jensen với kỳ vọng, nhiễu, phương sai và cận dưới ELBO, các bất đẳng thức AM–GM và Hölder."
---

Đến đây ta có hai thế giới song song: tập lồi ở phần II của chương, và hàm lồi ở vài chủ đề vừa qua. Ở đây ta dựng ba cây cầu giữa chúng. Cây cầu thứ nhất đi từ hàm sang tập: các tập mức dưới của một hàm lồi là tập lồi. Cây cầu thứ hai đi theo cả hai chiều: một hàm lồi khi và chỉ khi miền nằm phía trên đồ thị của nó, gọi là epigraph, là một tập lồi. Cây cầu thứ ba nối hàm lồi với xác suất: bất đẳng thức Jensen.

Mỗi cây cầu cho ta một cách mới để nhìn và để chứng minh. Ta sẽ dùng epigraph để viết lại bài toán tối ưu, dùng Jensen để thấy vì sao phương sai không âm, vì sao thêm nhiễu không làm giảm một hàm lồi, và vì sao những bất đẳng thức như AM–GM hay Hölder thật ra chỉ là một.

## 1. Tập mức dưới

> **Định nghĩa.** Tập mức dưới mức $\alpha$ của hàm $f$ là $C_\alpha = \{x \in \operatorname{dom} f : f(x) \le \alpha\}$.

Nếu $f$ lồi thì mọi tập mức dưới đều lồi, với mọi $\alpha$. Lời chứng minh đi thẳng từ định nghĩa: nếu $x, y \in C_\alpha$ thì

$$
f(\theta x + (1-\theta) y) \le \theta f(x) + (1-\theta) f(y) \le \theta\alpha + (1 - \theta)\alpha = \alpha .
$$

Bằng hình ảnh, cắt đồ thị của một cái bát bằng một mặt phẳng nằm ngang ở độ cao $\alpha$, phần đáy bát nằm dưới mặt cắt chiếu xuống thành một miền lồi.

Chiều ngược lại **sai**, và ví dụ của sách rất gọn: $-e^x$ lõm nghiêm ngặt, vậy mà mọi tập mức dưới $\{x : -e^x \le \alpha\}$ đều là một khoảng, nên lồi. Ở chủ đề điều kiện bậc nhất, hàm $-\exp(-x_1^2 - 2x_2^2)$ cũng có mọi tập mức dưới là ellipse dù không lồi. Những hàm có mọi tập mức dưới lồi được gọi là tựa lồi, một lớp rộng hơn hàm lồi.

<FunctionLab type="epigraph" />

Trong mô phỏng, vạch xanh trên trục hoành là tập mức dưới. Kéo thanh trượt $\alpha$ với $x^2$ hay $e^x$, vạch xanh luôn là một khoảng liền. Với $0.3x^2 + \sin(1.5x)$, có những mức $\alpha$ mà tập mức dưới tách thành hai khoảng rời nhau, và đó là một bằng chứng không lồi. Với $-e^x$ và $x^3$, tập mức dưới luôn là một khoảng, dù cả hai hàm đều không lồi trên $\mathbb{R}$.

**Dùng tập mức dưới để chứng minh một tập là lồi.** Kết quả vừa chứng minh cho một cách nhận ra tập lồi rất gọn. Muốn chứng minh tập $S$ lồi, ta cố viết nó thành $\{x : f(x) \le \alpha\}$ với $f$ lồi, hoặc $\{x : g(x) \ge \alpha\}$ với $g$ lõm, vì tập mức trên của hàm lõm cũng lồi. Chẳng hạn, ràng buộc $\|w\|_2 \le r$ trong học máy là tập mức dưới của một chuẩn, nên lồi. Ví dụ 3.3 của sách còn tinh tế hơn: tập các vector $x \in \mathbb{R}^n_+$ có trung bình nhân ít nhất bằng $\alpha$ lần trung bình cộng, với $0 \le \alpha \le 1$, là tập mức trên mức 0 của hàm lõm $G(x) - \alpha A(x)$, nên lồi.

Một hệ quả có ý nghĩa thực tế: nếu hàm mất mát huấn luyện $L(w)$ lồi theo tham số $w$, thì tập các mô hình "đủ tốt" $\{w : L(w) \le \varepsilon\}$ là tập lồi. Lấy trung bình tham số của hai mô hình đủ tốt luôn cho một mô hình đủ tốt. Với mạng nơ-ron, hàm mất mát không lồi, và trung bình tham số của hai mạng huấn luyện độc lập có thể cho một mạng rất tệ.

## 2. Epigraph: hàm lồi chính là tập lồi

> **Định nghĩa.** Epigraph của $f$ là tập $\operatorname{epi} f = \{(x, t) : x \in \operatorname{dom} f,\ f(x) \le t\}$, một tập con của $\mathbb{R}^{n+1}$.

Tiền tố "epi" nghĩa là "phía trên": epigraph gồm đồ thị và mọi điểm nằm phía trên nó (Hình 3.5 trong sách). Kết quả nối hai thế giới là:

> $f$ lồi khi và chỉ khi $\operatorname{epi} f$ là tập lồi.

Hai chiều đều ngắn. Nếu $f$ lồi và $(x, t), (y, s)$ thuộc epigraph, thì

$$
f(\theta x + (1-\theta) y) \le \theta f(x) + (1-\theta) f(y) \le \theta t + (1-\theta) s,
$$

nên điểm $(\theta x + (1-\theta)y,\ \theta t + (1-\theta)s)$ cũng thuộc epigraph. Ngược lại, nếu epigraph lồi, lấy hai điểm $(x, f(x))$ và $(y, f(y))$ của nó, tổ hợp lồi của chúng thuộc epigraph, và đó chính là bất đẳng thức dây cung. Tương tự, $f$ lõm khi và chỉ khi **hypograph** $\{(x, t) : t \le f(x)\}$ lồi.

Hãy so sánh với đồ thị: đồ thị của một hàm lồi không affine thì không phải tập lồi. Đồ thị của $x^2$ chứa $(-1, 1)$ và $(1, 1)$ nhưng không chứa trung điểm $(0, 1)$, điểm này nằm hẳn phía trên đồ thị. Phải "đổ đầy" phần phía trên thì mới được một tập lồi.

**Điều kiện bậc nhất nhìn từ epigraph.** Điều kiện $f(y) \ge f(x) + \nabla f(x)^T (y - x)$ có thể viết lại thành: với mọi $(y, t) \in \operatorname{epi} f$,

$$
\begin{bmatrix} \nabla f(x) \\ -1 \end{bmatrix}^T \left( \begin{bmatrix} y \\ t \end{bmatrix} - \begin{bmatrix} x \\ f(x) \end{bmatrix} \right) \le 0 .
$$

Đây đúng là định nghĩa của một **siêu phẳng tựa** của tập lồi $\operatorname{epi} f$ tại điểm biên $(x, f(x))$, với pháp tuyến $(\nabla f(x), -1)$ (Hình 3.6). Tiếp tuyến của hàm lồi chỉ là siêu phẳng tựa của epigraph, và điều kiện bậc nhất là định lý siêu phẳng tựa ở chủ đề trước, áp dụng cho một tập lồi đặc biệt.

**Dùng epigraph để chứng minh tính lồi.** Ví dụ 3.4 của sách dùng epigraph cho hàm $x^2/y$ và tổng quát của nó. Với $y > 0$, theo phần bù Schur,

$$
\frac{x^2}{y} \le t \iff \begin{bmatrix} y & x \\ x & t \end{bmatrix} \succeq 0 .
$$

Ma trận bên phải phụ thuộc affine vào $(x, y, t)$, và điều kiện nửa xác định dương nghĩa là ma trận nằm trong nón PSD, một tập lồi. Vậy epigraph là ảnh ngược của một tập lồi qua một ánh xạ affine, nên lồi, và hàm lồi. So với việc tính Hessian ở chủ đề điều kiện bậc hai, lời chứng minh này không cần đạo hàm nào. Thử bằng số: với $(x, y) = (1, 2)$, ta có $x^2/y = 0.5$. Ma trận $\begin{bmatrix} 2 & 1 \\ 1 & 0.5 \end{bmatrix}$ nửa xác định dương, còn $\begin{bmatrix} 2 & 1 \\ 1 & 0.4 \end{bmatrix}$ thì không, đúng như $0.5 \le 0.5$ còn $0.5 > 0.4$.

**Dạng epigraph của bài toán tối ưu.** Mẹo dùng nhiều nhất của epigraph là trong mô hình hóa: cực tiểu $f(x)$ tương đương với cực tiểu một biến mới $t$ dưới ràng buộc $f(x) \le t$. Hàm mục tiêu trở thành tuyến tính, và toàn bộ độ phức tạp chuyển vào một ràng buộc lồi. Bạn đã thấy mẹo này ở chủ đề về hai lớp bài toán kinh điển: cực tiểu sai số lớn nhất $\max_i |r_i|$ được viết lại thành cực tiểu $t$ với $-t \le r_i \le t$, và nhờ vậy trở thành một quy hoạch tuyến tính. Sách gọi đây là dạng epigraph của bài toán (§4.1.3).

## 3. Bất đẳng thức Jensen

Bất đẳng thức dây cung $f(\theta x + (1-\theta) y) \le \theta f(x) + (1-\theta) f(y)$ đôi khi được gọi là bất đẳng thức Jensen. Bằng quy nạp, nó mở rộng cho tổ hợp lồi của $k$ điểm:

$$
f(\theta_1 x_1 + \cdots + \theta_k x_k) \le \theta_1 f(x_1) + \cdots + \theta_k f(x_k), \qquad \theta_i \ge 0,\ \textstyle\sum_i \theta_i = 1 .
$$

Đọc $\theta_i$ như xác suất để một biến ngẫu nhiên $X$ nhận giá trị $x_i$, ta được dạng xác suất, dạng quan trọng nhất:

$$
f(\mathbf{E}\,X) \le \mathbf{E}\, f(X)
$$

với mọi biến ngẫu nhiên $X$ nhận giá trị trong miền xác định của hàm lồi $f$, miễn là các kỳ vọng tồn tại. Hàm lồi của giá trị trung bình không vượt trung bình của hàm. Sách nhận xét rằng bất đẳng thức này **đặc trưng** cho tính lồi: nếu $f$ không lồi, luôn có một biến ngẫu nhiên hai giá trị làm nó sai.

<FunctionLab type="jensen" />

Mô phỏng đặt ba điểm với ba xác suất. Điểm vàng là $f(\mathbf{E}\,X)$, vòng tròn rỗng là $\mathbf{E}\,f(X)$, và vòng tròn luôn nằm trên với hàm lồi. Vòng tròn rỗng luôn nằm trong vùng tô màu, bao lồi của ba điểm trên đồ thị, vì nó là một tổ hợp lồi của chúng. Với $-x^2$, chiều bất đẳng thức đảo lại.

### Phương sai là khoảng cách Jensen

Áp dụng Jensen cho $f(x) = x^2$:

$$
\mathbf{E}\,X^2 - (\mathbf{E}\,X)^2 \ge 0 .
$$

Vế trái chính là phương sai của $X$. Vậy "phương sai không âm" là bất đẳng thức Jensen cho hàm bình phương, và khoảng cách Jensen ở đây đo đúng độ phân tán. Với $X$ phân phối đều trên $\{1, 2, 3, 4\}$, ta có $\mathbf{E}\,X^2 = 7.5$, $(\mathbf{E}\,X)^2 = 6.25$, và hiệu $1.25$ đúng bằng phương sai.

Cùng phép tính ấy cho ra phân tích độ lệch và phương sai trong học máy. Gọi $\hat y$ là dự đoán của một mô hình, ngẫu nhiên theo dữ liệu huấn luyện, và $y$ là giá trị đúng. Áp dụng đẳng thức trên cho $X = \hat y - y$:

$$
\mathbf{E}\,(\hat y - y)^2 = (\mathbf{E}\,\hat y - y)^2 + \operatorname{Var}(\hat y).
$$

Sai số bình phương trung bình bằng bình phương độ lệch cộng phương sai, và phương sai chính là khoảng cách Jensen. Với $\hat y$ nhận ba giá trị $2.5$, $3.5$, $4$ đồng khả năng và $y = 3$, sai số trung bình là $0.5$, gồm bình phương độ lệch $1/9 \approx 0.111$ và phương sai $7/18 \approx 0.389$.

### Thêm nhiễu không làm giảm hàm lồi

Ghi chú 3.2 của sách rút ra một hệ quả gọn: nếu $z$ là một vector ngẫu nhiên có trung bình 0, thì

$$
\mathbf{E}\, f(x + z) \ge f(x).
$$

Lý do: $\mathbf{E}\,(x + z) = x$, và Jensen cho $f(x) = f(\mathbf{E}(x + z)) \le \mathbf{E}\, f(x + z)$. Thêm nhiễu cân bằng vào đầu vào của một hàm lồi không bao giờ làm nó giảm đi **tính trung bình**. Với $f(x) = x^2$ và nhiễu $\pm 1$ đồng khả năng, $\mathbf{E}(1.5 + z)^2 = 3.25 = 1.5^2 + 1$, lớn hơn đúng bằng phương sai của nhiễu. Nếu bạn đang ở điểm cực tiểu của một hàm lồi, rung lắc ngẫu nhiên chỉ có thể làm giá trị trung bình xấu đi.

### Cận dưới ELBO trong học máy

Với hàm lõm, Jensen đảo chiều: $\mathbf{E}\, g(X) \le g(\mathbf{E}\,X)$. Áp dụng cho $g = \log$, ta được một trong những bất đẳng thức được dùng nhiều nhất của học máy hiện đại. Trong một mô hình có biến ẩn $z$, xác suất của dữ liệu $p(x) = \sum_z p(x, z)$ thường không tính được. Chọn một phân phối $q(z)$ bất kỳ có $q(z) > 0$ ở mọi nơi $p(x, z) > 0$, rồi viết

$$
\log p(x) = \log \mathbf{E}_{z \sim q}\left[\frac{p(x, z)}{q(z)}\right] \ \ge\ \mathbf{E}_{z \sim q}\left[\log \frac{p(x, z)}{q(z)}\right].
$$

Vế phải gọi là **cận dưới bằng chứng** (evidence lower bound, ELBO). Thay vì cực đại $\log p(x)$, các phương pháp suy luận biến phân, trong đó có mô hình tự mã hóa biến phân (VAE), cực đại cận dưới này. Jensen còn cho biết khi nào cận chặt: khi biến ngẫu nhiên $p(x, z)/q(z)$ là hằng số, tức $q(z)$ đúng bằng phân phối hậu nghiệm $p(z \mid x)$.

::: example ELBO trên một mô hình hai trạng thái
Biến ẩn $z \in \{0, 1\}$ với $p(z) = (0.5, 0.5)$, và $p(x \mid z) = (0.2, 0.6)$. Khi đó $p(x) = 0.4$ và $\log p(x) \approx -0.916$. Phân phối hậu nghiệm là $p(z \mid x) = (0.25, 0.75)$. Với $q = (0.5, 0.5)$, ELBO $\approx -1.060$. Với $q = (0.1, 0.9)$, ELBO $\approx -0.989$. Với $q = (0.25, 0.75)$, ELBO bằng đúng $-0.916$. Mọi giá trị đều không vượt $\log p(x)$, và dấu bằng xảy ra đúng tại hậu nghiệm.
:::

## 4. Một lý thuyết về bất đẳng thức

Sách nhận xét rằng tính lồi cùng bất đẳng thức Jensen có thể làm nền cho cả một lý thuyết về bất đẳng thức. Hai ví dụ cho thấy điều đó.

**AM–GM.** Hàm $-\log x$ lồi. Jensen với $k$ điểm và trọng số bằng nhau cho

$$
-\log\Big(\frac{x_1 + \cdots + x_n}{n}\Big) \le -\frac{\log x_1 + \cdots + \log x_n}{n},
$$

và lấy mũ hai vế được $(x_1 \cdots x_n)^{1/n} \le (x_1 + \cdots + x_n)/n$. Với $X$ đều trên $\{1, 2, 3, 4\}$, trung bình nhân xấp xỉ $2.213$ còn trung bình cộng bằng $2.5$. Với trọng số tùy ý, cùng lập luận cho dạng có trọng số $a^\theta b^{1-\theta} \le \theta a + (1-\theta) b$ với $a, b \ge 0$ và $0 \le \theta \le 1$.

**Hölder.** Với $p > 1$ và $1/p + 1/q = 1$,

$$
\sum_i x_i y_i \le \Big(\sum_i |x_i|^p\Big)^{1/p} \Big(\sum_i |y_i|^q\Big)^{1/q} .
$$

Lời chứng minh của sách chỉ là AM–GM có trọng số với một lựa chọn khéo: đặt $a = |x_i|^p / \sum_j |x_j|^p$, $b = |y_i|^q / \sum_j |y_j|^q$, $\theta = 1/p$, rồi cộng theo $i$. Vế phải sau khi cộng bằng $1/p + 1/q = 1$, và bất đẳng thức hiện ra. Khi $p = q = 2$, ta được bất đẳng thức Cauchy–Schwarz. Kiểm tra với $x = (1, 2, 3)$, $y = (3, 1, 2)$, $p = 3$, $q = 1.5$: vế trái bằng $11$, vế phải xấp xỉ $3.302 \times 4.335 \approx 14.31$. Với $p = q = 2$, vế phải bằng $\sqrt{14} \cdot \sqrt{14} = 14$.

Bất đẳng thức Hölder là lý do chuẩn $\ell_p$ và chuẩn $\ell_q$ đối ngẫu với nhau khi $1/p + 1/q = 1$, đúng như cặp $\ell_1$ và $\ell_\infty$ ở chủ đề nón đối ngẫu.

## 5. Những câu hỏi để đào sâu

**Câu 1.** Một bạn lập luận: "Hàm $f$ có mọi tập mức dưới lồi, và $f$ khả vi, nên điểm có $\nabla f(x) = 0$ là cực tiểu toàn cục." Lập luận này sai ở đâu?

<details><summary>Xem lời giải thích</summary>

Tập mức dưới lồi chỉ cho tính tựa lồi, và với hàm tựa lồi, gradient bằng 0 không bảo đảm cực tiểu toàn cục. Hàm $x^3$ có mọi tập mức dưới là một nửa trục $(-\infty, \alpha^{1/3}]$, nên tựa lồi, và $f'(0) = 0$, nhưng gốc không phải cực tiểu. Điều kiện bậc nhất "gradient bằng 0 suy ra cực tiểu toàn cục" cần tính lồi thật sự, tức cần tiếp tuyến nằm dưới toàn bộ đồ thị, chứ không chỉ cần các tập mức dưới lồi.

</details>

**Câu 2.** Hàm $\max\{f_1, f_2\}$ của hai hàm lồi có lồi không? Hãy trả lời chỉ bằng epigraph, không viết bất đẳng thức nào.

<details><summary>Xem lời giải thích</summary>

Có. Điểm $(x, t)$ nằm trên đồ thị của $\max\{f_1, f_2\}$ khi và chỉ khi nó nằm trên đồ thị của cả $f_1$ lẫn $f_2$. Vậy $\operatorname{epi} \max\{f_1, f_2\} = \operatorname{epi} f_1 \cap \operatorname{epi} f_2$, giao của hai tập lồi, nên lồi. Lập luận này dùng được cho max của bao nhiêu hàm cũng được, kể cả vô hạn, và nó là nội dung của quy tắc "supremum theo từng điểm" ở chủ đề tiếp theo. Ngược lại, $\operatorname{epi} \min\{f_1, f_2\}$ là **hợp** của hai epigraph, thường không lồi.

</details>

**Câu 3.** Jensen nói $\mathbf{E}\,f(X) \ge f(\mathbf{E}\,X)$ cho $f$ lồi. Một nhà đầu tư dùng điều này để nói: "Vì $e^x$ lồi, lợi nhuận trung bình $\mathbf{E}\,e^{X}$ lớn hơn $e^{\mathbf{E}X}$, nên càng biến động càng có lợi." Phân tích lập luận này.

<details><summary>Xem lời giải thích</summary>

Bất đẳng thức đúng: với $X$ đều trên $\{1, 2, 3, 4\}$, $\mathbf{E}\,e^X \approx 21.20$ trong khi $e^{\mathbf{E}X} \approx 12.18$. Nhưng kết luận "biến động càng có lợi" chỉ đúng nếu điều ta quan tâm là **trung bình** của $e^X$. Nếu điều ta quan tâm là một hàm lõm của của cải, như logarit, thì Jensen đi theo chiều ngược lại và biến động gây thiệt. Bài học tổng quát: Jensen cho biết nhiễu tác động theo chiều nào **tùy vào độ cong** của hàm mà ta lấy trung bình. Với hàm lồi, trung bình được lợi từ nhiễu, với hàm lõm thì bị thiệt.

</details>

**Câu 4.** Trong ví dụ ELBO, vì sao ELBO với $q = (0.1, 0.9)$ lại tốt hơn với $q = (0.5, 0.5)$, dù $(0.5, 0.5)$ chính là phân phối tiên nghiệm $p(z)$?

<details><summary>Xem lời giải thích</summary>

Biến đổi trực tiếp cho thấy khoảng cách giữa $\log p(x)$ và ELBO đúng bằng $D_{\mathrm{kl}}(q,\ p(\cdot \mid x))$, độ phân kỳ KL từ $q$ tới hậu nghiệm, đại lượng mà chủ đề điều kiện bậc nhất đã chứng minh là không âm. Hậu nghiệm là $(0.25, 0.75)$. Phân phối $(0.1, 0.9)$ lệch về cùng phía với hậu nghiệm, còn $(0.5, 0.5)$ thì không nhìn dữ liệu chút nào. Tính ra, $\log p(x) - \text{ELBO}$ bằng khoảng $0.144$ với $q = (0.5, 0.5)$ và $0.073$ với $q = (0.1, 0.9)$, đúng bằng hai độ phân kỳ KL tương ứng.

</details>

## 6. Bài tập tự luyện

::: exercise 1. Một tập mức dưới
Chứng minh tập $S = \{x \in \mathbb{R}^2 : x_1^2 + 2x_2^2 + e^{x_1} \le 3\}$ là tập lồi và khác rỗng. Tìm khoảng mà $S$ chiếm trên trục $x_1$ (giải số).
:::

::: solution
Hàm $f(x) = x_1^2 + 2x_2^2 + e^{x_1}$ là tổng của các hàm lồi, nên lồi, và $S$ là tập mức dưới mức 3 của nó, nên lồi. Điểm $(0, 0)$ cho $f = 1 \le 3$, nên $S$ khác rỗng. Trên trục $x_1$ (tức $x_2 = 0$), điều kiện là $x_1^2 + e^{x_1} \le 3$. Giải số phương trình $x_1^2 + e^{x_1} = 3$ được hai nghiệm $x_1 \approx -1.677$ và $x_1 \approx 0.834$, nên $S$ cắt trục $x_1$ theo đoạn $[-1.677,\ 0.834]$. Đoạn này lệch về bên trái vì $e^{x_1}$ tăng nhanh khi $x_1 > 0$.
:::

::: exercise 2. Epigraph của 1/x như một điều kiện ma trận
Chứng minh rằng với $x > 0$, $1/x \le t$ khi và chỉ khi $\begin{bmatrix} x & 1 \\ 1 & t \end{bmatrix} \succeq 0$. Từ đó suy ra $1/x$ lồi trên $\mathbb{R}_{++}$ mà không cần đạo hàm.
:::

::: solution
Với $x > 0$, ma trận $2 \times 2$ đối xứng nửa xác định dương khi và chỉ khi $x \ge 0$, $t \ge 0$ và $xt - 1 \ge 0$. Vì $x > 0$, điều kiện cuối là $t \ge 1/x$, và nó kéo theo $t > 0$. Vậy epigraph của $1/x$ là $\{(x, t) : x > 0\}$ giao với ảnh ngược của nón PSD qua ánh xạ affine $(x, t) \mapsto \begin{bmatrix} x & 1 \\ 1 & t \end{bmatrix}$. Giao của hai tập lồi là tập lồi, nên epigraph lồi và $1/x$ lồi. Kiểm tra bằng số: $(x, t) = (2, 0.5)$ cho ma trận nửa xác định dương và đúng $1/2 \le 0.5$, còn $(2, 0.4)$ cho ma trận có định thức âm và đúng $0.5 > 0.4$.
:::

::: exercise 3. Ba khoảng cách Jensen
Cho $X$ phân phối đều trên $\{1, 2, 3, 4\}$. Tính khoảng cách Jensen $\mathbf{E}\,f(X) - f(\mathbf{E}\,X)$ cho (a) $f(x) = x^2$, (b) $f(x) = -\log x$, (c) $f(x) = e^x$. Khoảng cách nào lớn nhất, và điều đó nói gì về độ cong của ba hàm trên đoạn $[1, 4]$?
:::

::: solution
$\mathbf{E}\,X = 2.5$. (a) $7.5 - 6.25 = 1.25$, bằng phương sai. (b) $\mathbf{E}(-\log X) \approx -0.795$ và $-\log 2.5 \approx -0.916$, hiệu xấp xỉ $0.122$. (c) $\mathbf{E}\,e^X \approx 21.20$ và $e^{2.5} \approx 12.18$, hiệu xấp xỉ $9.02$. Khoảng cách của $e^x$ lớn nhất vì trên $[1, 4]$ độ cong $f''(x) = e^x$ của nó lớn hơn hẳn: từ $e \approx 2.7$ tới $e^4 \approx 54.6$, trong khi $x^2$ có độ cong không đổi bằng 2 và $-\log x$ có độ cong $1/x^2$ chỉ từ $1/16$ tới 1. Khi phân tán của $X$ nhỏ, khoảng cách Jensen xấp xỉ $\tfrac12 f''(\mathbf{E}\,X)\operatorname{Var}(X)$, nên độ cong càng lớn thì khoảng cách càng lớn.
:::

## Tóm tắt

Tập mức dưới của hàm lồi luôn lồi, nhưng chiều ngược lại sai: hàm có mọi tập mức dưới lồi chỉ là tựa lồi. Viết một tập thành tập mức dưới của một hàm lồi là cách nhanh để chứng minh nó lồi. Epigraph nối hai thế giới theo cả hai chiều: $f$ lồi khi và chỉ khi $\operatorname{epi} f$ lồi. Từ đó, tiếp tuyến là siêu phẳng tựa của epigraph, các hàm như $x^2/y$ được chứng minh lồi bằng phần bù Schur, và mọi bài toán tối ưu có thể viết ở dạng epigraph với hàm mục tiêu tuyến tính.

Bất đẳng thức Jensen $f(\mathbf{E}X) \le \mathbf{E}f(X)$ là dạng xác suất của tính lồi. Nó giải thích vì sao phương sai không âm, vì sao sai số bình phương tách thành độ lệch và phương sai, vì sao nhiễu trung bình 0 không làm giảm một hàm lồi, và vì sao ELBO là một cận dưới. AM–GM và Hölder cũng chỉ là Jensen cho hàm $-\log$.

## Nguồn và đọc thêm

- S. Boyd, L. Vandenberghe, *Convex Optimization*, §3.1.6–3.1.9 (tr. 75–78), Ví dụ 3.3 và 3.4, Hình 3.5 và 3.6, Ghi chú 3.2. Dạng epigraph của bài toán ở §4.1.3. Hàm tựa lồi ở §3.4.
- Ứng dụng vào trung bình tham số mô hình, phân tích độ lệch và phương sai, ví dụ ELBO hai trạng thái, các ví dụ số, câu hỏi và bài tập do người soạn bổ sung. Mọi con số đã được tính lại bằng chương trình.
