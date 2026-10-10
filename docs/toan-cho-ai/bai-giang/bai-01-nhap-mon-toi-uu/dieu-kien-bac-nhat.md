---
course: toan-cho-ai
lecture: bai-01-nhap-mon-toi-uu
topic: dieu-kien-bac-nhat
section: topic
title: "Điều kiện bậc nhất: Tiếp tuyến nằm dưới đồ thị"
description: "Điều kiện bậc nhất của hàm lồi khả vi và ý nghĩa của tiếp tuyến như một cận dưới toàn cục: Điểm dừng là cực tiểu toàn cục, cận dưới cho giá trị tối ưu, các bất đẳng thức cổ điển và độ phân kỳ KL, gradient loại bỏ nửa không gian, gradient đơn điệu, lồi nghiêm ngặt và dưới đạo hàm."
---

Hãy hình dung bạn đứng trên sườn đồi giữa một màn sương dày. Bạn chỉ đo được hai thứ: Độ cao chỗ mình đứng và độ dốc của mặt đất ngay dưới chân. Với một địa hình bất kỳ, hai con số ấy gần như không nói lên điều gì về những nơi ở xa, vì ngay sau mỏm đá trước mặt có thể là một thung lũng sâu hơn hẳn. Nhưng nếu biết trước địa hình có dạng một cái bát khổng lồ, câu chuyện thay đổi hoàn toàn. Từ độ cao và độ dốc tại đúng một điểm duy nhất, ta dựng được một mặt phẳng mà toàn bộ cái bát đều nằm phía trên mặt phẳng đó.

Đó là nội dung cốt lõi của điều kiện bậc nhất, một trong những tính chất nền tảng nhất của hàm lồi trong tối ưu hóa. Bản chất nằm ở chỗ: Một thuật toán tối ưu thông thường chỉ đo đạc được thông tin cục bộ, bao gồm giá trị hàm và gradient tại điểm hiện hành. Đối với hàm lồi, thông tin cục bộ đó lại cho phép ta rút ra kết luận chắc chắn trên toàn bộ miền xác định. Bài giảng này phát biểu điều kiện, làm sáng tỏ các hệ quả thực tiễn, phân tích từng bước chứng minh chặt chẽ, và mở rộng sang trường hợp hàm không khả vi tại các điểm gãy thông qua khái niệm dưới đạo hàm.

## 1. Phát biểu

> **Định lý.** Giả sử $f$ khả vi, nghĩa là $\operatorname{dom} f$ là tập mở và gradient $\nabla f$ tồn tại tại mọi điểm của nó. Khi đó $f$ lồi khi và chỉ khi $\operatorname{dom} f$ lồi và
> $$f(y) \ge f(x) + \nabla f(x)^T (y - x) \quad \text{với mọi } x, y \in \operatorname{dom} f.$$

Cố định $x$ và xem vế phải như một hàm của $y$. Đó là một hàm affine, đồng thời chính là xấp xỉ Taylor bậc nhất của $f$ quanh $x$: Biểu thức này khớp với $f$ cả về giá trị lẫn về đạo hàm tại $x$. Khi $n = 1$, đồ thị của nó là tiếp tuyến tại $(x, f(x))$. Khi $n \ge 2$, đó là siêu phẳng tiếp xúc với đồ thị. Bất đẳng thức khẳng định rằng xấp xỉ bậc nhất của một hàm lồi **không bao giờ đánh giá vượt mức**: Tiếp tuyến tại bất kỳ điểm nào cũng luôn nằm dưới toàn bộ đồ thị.

Chữ "toàn bộ" là điểm mấu chốt tạo nên khác biệt. Với mọi hàm khả vi, xấp xỉ bậc nhất đều tốt khi $y$ đủ gần $x$. Nhưng chỉ với hàm lồi, xấp xỉ đó mới là một **cận dưới toàn cục**, đúng với mọi $y$ trong miền xác định dù $y$ ở xa $x$ đến đâu.

<FunctionLab type="tangent" />

Trong mô phỏng, với $x^2$, $e^x$, $-\log x$ hay $x \log x$, bạn trượt $x_0$ đi đâu thì tiếp tuyến cũng nằm dưới đồ thị. Với $x^3$, chỉ cần đặt $x_0 < 0$ là tiếp tuyến cắt lên trên đồ thị ở phía bên phải. Hàm $1/x^2$ đáng xem kỹ hơn: Trên nửa trục chứa $x_0$, tiếp tuyến vẫn nằm dưới đồ thị, nhưng ở nửa trục bên kia nó vượt lên trên đồ thị trên cả một khoảng. Miền xác định không lồi, nên điều kiện bậc nhất không còn được bảo toàn. Cần lưu ý rằng giả thiết về tính lồi của miền xác định là điều kiện tiên quyết không thể bỏ qua.

## 2. Thông tin cục bộ cho kết luận toàn cục

### Điểm dừng là cực tiểu toàn cục

Nếu $\nabla f(x) = 0$ thì vế phải của bất đẳng thức chỉ còn $f(x)$, nên $f(y) \ge f(x)$ với mọi $y$. Vậy với hàm lồi khả vi, **mọi điểm dừng đều là điểm cực tiểu toàn cục**. Một thuật toán chỉ cần tìm chỗ gradient triệt tiêu, và khi tìm được thì có thể dừng mà không phải lo còn thung lũng nào sâu hơn ở đâu đó.

Thiếu tính lồi, kết luận này có thể sai theo nhiều cách. Hàm $x^3$ có đạo hàm bằng 0 tại gốc, nhưng gốc không phải cực tiểu, kể cả cực tiểu cục bộ. Hàm $x^2 - x^4/4$ cũng có đạo hàm bằng 0 tại gốc, và lần này gốc là cực tiểu cục bộ, vậy mà $f(3) = -11.25$ nhỏ hơn hẳn $f(0) = 0$. Trong cả hai trường hợp, tiếp tuyến nằm ngang tại gốc đều cắt đồ thị ở đâu đó.

### Một cận dưới đo được cho giá trị tối ưu

Hệ quả thứ hai ít được nhắc tới hơn, nhưng rất thực tế. Giả sử ta cực tiểu hàm lồi $f$ trên tập $C$ và đang đứng ở một điểm $x \in C$ chưa chắc tối ưu. Lấy cực tiểu theo $y \in C$ ở cả hai vế của điều kiện bậc nhất, ta được

$$
p^\star = \min_{y \in C} f(y) \ \ge\ f(x) + \min_{y \in C} \nabla f(x)^T (y - x).
$$

Vế phải là cực tiểu của một hàm **tuyến tính** trên $C$, việc này thường dễ hơn nhiều so với bài toán gốc, chẳng hạn khi $C$ là một hình hộp. Như vậy chỉ với giá trị và gradient tại điểm hiện tại, ta có cả cận trên $f(x)$ lẫn một cận dưới cho $p^\star$, và biết chắc rằng mình kém tối ưu không quá hiệu của hai cận đó.

::: example Một chứng nhận chỉ cần một lần tính gradient
Cực tiểu $f(y) = (y_1 - 1)^2 + 2(y_2 + 0.5)^2$ trên hình vuông $C = [0, 2] \times [0, 2]$. Tại $x = (1, 0.2)$, ta có $f(x) = 2 \cdot 0.7^2 = 0.98$ và $\nabla f(x) = (0,\ 2.8)$. Hàm tuyến tính $2.8(y_2 - 0.2)$ đạt nhỏ nhất trên $C$ khi $y_2 = 0$, với giá trị $-0.56$. Do đó

$$
0.42 = 0.98 - 0.56 \ \le\ p^\star \ \le\ 0.98 .
$$

Ta chưa biết $p^\star$, nhưng đã biết điểm hiện tại kém tối ưu không quá $0.56$. Để đối chiếu, nghiệm thật là $y^\star = (1, 0)$ với $p^\star = 2 \cdot 0.5^2 = 0.5$, nằm đúng trong khoảng vừa tìm. Nếu đứng ở một điểm xa nghiệm như $(2, 2)$ thì cận dưới thu được là $-10.5$, vẫn đúng nhưng rất lỏng. Điểm hiện tại càng gần nghiệm thì cận càng chặt.
:::

Một cận dưới kiểm chứng được cho $p^\star$ là thứ cho phép thuật toán tự biết khi nào nên dừng. Ở phần đối ngẫu của môn học, bạn sẽ gặp lại đúng tinh thần này dưới một hình thức tổng quát hơn nhiều.

## 3. Nhiều bất đẳng thức quen thuộc chỉ là một tiếp tuyến

Viết điều kiện bậc nhất cho vài hàm một biến quen thuộc tại một điểm chọn khéo, ta thu được ngay những bất đẳng thức mà ở phổ thông thường phải chứng minh riêng từng cái:

- $e^x$ lồi và tiếp tuyến tại 0 là $1 + y$, nên $e^y \ge 1 + y$ với mọi $y$.
- $\log x$ lõm và tiếp tuyến tại 1 là $y - 1$. Với hàm lõm, tiếp tuyến nằm **trên** đồ thị, nên $\log y \le y - 1$ với mọi $y > 0$.
- $t^p$ với $p \ge 1$ lồi trên $\mathbb{R}_+$, và tiếp tuyến tại $t = 1$ cho $t^p \ge 1 + p(t - 1)$. Đặt $t = 1 + u$ ta được bất đẳng thức Bernoulli $(1 + u)^p \ge 1 + pu$ với $u \ge -1$.

Mỗi dòng chỉ là câu "tiếp tuyến nằm dưới (hoặc trên) đồ thị" được viết ra cho một hàm cụ thể. Dấu bằng xảy ra tại tiếp điểm, và với những hàm lồi nghiêm ngặt như $e^x$ thì chỉ tại tiếp điểm.

Cách nhìn này mang lại một ứng dụng rất đẹp trong học máy. Xét hàm entropy âm $f(v) = \sum_{i=1}^n v_i \log v_i$, đây là một hàm lồi trên $\mathbb{R}^n_{++}$ với gradient từng thành phần $\nabla f(v)_i = \log v_i + 1$. Khoảng cách theo phương thẳng đứng giữa đồ thị của $f$ tại $u$ và siêu phẳng tiếp xúc tại $v$ được xác định bởi:

$$
\begin{aligned}
f(u) - f(v) - \nabla f(v)^T (u - v) &= \sum_{i=1}^n \left( u_i \log \frac{u_i}{v_i} - u_i + v_i \right) \\
&= \left(u_1 \log \frac{u_1}{v_1} - u_1 + v_1\right) + \dots + \left(u_n \log \frac{u_n}{v_n} - u_n + v_n\right).
\end{aligned}
$$

Vế phải chính là **độ phân kỳ Kullback–Leibler** $D_{\mathrm{kl}}(u, v)$ tổng quát. Áp dụng điều kiện bậc nhất, ta kết luận ngay $D_{\mathrm{kl}}(u, v) \ge 0$, và vì entropy âm là hàm lồi nghiêm ngặt, dấu bằng chỉ xảy ra khi và chỉ khi $u = v$. Đây chính là bất đẳng thức thông tin kinh điển trong lý thuyết thông tin, và hình học của tiếp tuyến mang lại một minh chứng trực quan sinh động.

Khi $u = p$ và $v = q$ là hai phân phối xác suất rời rạc, tức $\sum_{i=1}^n p_i = \sum_{i=1}^n q_i = 1$, các số hạng $-p_i + q_i$ triệt tiêu lẫn nhau khi lấy tổng, dẫn tới công thức quen thuộc $D_{\mathrm{kl}}(p, q) = \sum_{i=1}^n p_i \log (p_i / q_i)$. Biểu diễn lại theo entropy chéo:

$$
\underbrace{-\sum_{i=1}^n p_i \log q_i}_{\text{entropy chéo}} = \underbrace{-\sum_{i=1}^n p_i \log p_i}_{\text{entropy}} + D_{\mathrm{kl}}(p, q).
$$

Như vậy, với dữ liệu có phân phối thực tế $p$ cố định, entropy chéo luôn lớn hơn hoặc bằng entropy của chính phân phối đó, và đạt cực tiểu khi và chỉ khi $q = p$. Đó là lý do hàm mất mát entropy chéo có xu hướng kéo phân phối dự đoán của mô hình tiệm cận về phân phối thực nghiệm của dữ liệu. Với hai phân phối $p = (0.5, 0.3, 0.2)$ và $q = (0.4, 0.4, 0.2)$, entropy chéo xấp xỉ $1.0549$, entropy xấp xỉ $1.0297$, và hiệu số giữa chúng bằng đúng $D_{\mathrm{kl}}(p, q) \approx 0.0253$.

## 4. Phân tích các bước chứng minh

Lời chứng minh được xây dựng bằng cách khảo sát trường hợp một biến trước, sau đó vận dụng kỹ thuật hạn chế lên đường thẳng từ chủ đề trước để tổng quát hóa lên không gian nhiều chiều. Mỗi bước biến đổi đều gắn liền với một ý nghĩa hình học rõ ràng.

**Lồi suy ra tiếp tuyến nằm dưới.** Lấy $x, y$ trong miền xác định và $0 < t \le 1$. Điểm $x + t(y - x)$ nằm trên đoạn thẳng nối từ $x$ tới $y$, do đó tính lồi của hàm số cho:

$$
f(x + t(y - x)) \le (1 - t) f(x) + t f(y).
$$

Trừ $f(x)$ ở cả hai vế rồi chia cho $t > 0$:

$$
\frac{f(x + t(y - x)) - f(x)}{t} \le f(y) - f(x).
$$

Cho $t \to 0$, vế trái tiến tới đạo hàm theo hướng $f'(x)(y - x)$, và ta thu được bất đẳng thức $f(y) \ge f(x) + f'(x)(y - x)$. Về mặt hình học, vế trái là độ dốc của một dây cung rất ngắn xuất phát từ $x$, nhân với khoảng dịch chuyển $y - x$. Tính lồi bảo đảm rằng dây cung ngắn có độ dốc không vượt quá dây cung dài hơn cùng xuất phát từ $x$ về cùng một phía. Tiếp tuyến là giới hạn của những dây cung ngắn dần, do đó nó nằm dưới mọi dây cung, và hệ quả là nằm dưới toàn bộ đồ thị.

Hiện tượng "độ dốc dây cung tăng dần" trở nên rất sáng rõ khi kiểm tra bằng số cụ thể: Với $f(x) = e^x$ và ba điểm $0 < 1 < 2$, dây cung nối từ 0 tới 1 có độ dốc $e - 1 \approx 1.718$, dây cung từ 0 tới 2 có độ dốc $(e^2 - 1)/2 \approx 3.195$, còn dây cung từ 1 tới 2 có độ dốc $e^2 - e \approx 4.671$. Cả ba giá trị này đều nằm giữa $f'(0) = 1$ và $f'(2) \approx 7.389$, xếp theo đúng thứ tự tăng dần từ trái sang phải. Tính chất đơn điệu của độ dốc dây cung là đặc trưng phổ quát cho mọi hàm lồi một biến.

**Tiếp tuyến nằm dưới suy ra lồi.** Lấy $z = \theta x + (1 - \theta) y$ và áp dụng giả thiết tại $z$ hai lần:

$$
f(x) \ge f(z) + f'(z)(x - z), \qquad f(y) \ge f(z) + f'(z)(y - z).
$$

Nhân bất đẳng thức đầu với $\theta$, bất đẳng thức sau với $1 - \theta$ rồi cộng lại. Vì $\theta(x - z) + (1 - \theta)(y - z) = 0$, các số hạng chứa đạo hàm triệt tiêu, chỉ còn $\theta f(x) + (1 - \theta) f(y) \ge f(z)$, chính là định nghĩa của hàm lồi. Hình ảnh ở đây cũng rõ: Tiếp tuyến tại $z$ nằm dưới cả hai điểm $(x, f(x))$ và $(y, f(y))$, nên dây cung nối hai điểm ấy nằm trên tiếp tuyến. Tại $z$, tiếp tuyến chạm đồ thị, vì vậy dây cung nằm trên đồ thị tại $z$.

**Lên nhiều chiều.** Với $x, y \in \operatorname{dom} f$, đặt $g(t) = f(x + t(y - x))$. Theo quy tắc dây chuyền, $g'(t) = \nabla f(x + t(y - x))^T (y - x)$. Nếu $f$ lồi thì $g$ lồi, và trường hợp một biến cho $g(1) \ge g(0) + g'(0)$, tức đúng bất đẳng thức cần chứng minh. Chiều ngược lại cũng đi qua $g$: Giả thiết cho $g$ thỏa điều kiện bậc nhất một biến tại mọi cặp điểm, nên $g$ lồi trên mọi đường thẳng, và $f$ lồi.

## 5. Mỗi gradient loại bỏ nửa không gian

Đọc điều kiện bậc nhất theo một cách khác. Nếu $\nabla f(x)^T (y - x) \ge 0$ thì $f(y) \ge f(x) + \nabla f(x)^T (y - x) \ge f(x)$. Nói cách khác:

> Với $f$ lồi khả vi, mọi điểm $y$ tốt hơn $x$, tức $f(y) < f(x)$, đều nằm trong nửa không gian mở $\{y : \nabla f(x)^T (y - x) < 0\}$.

Chỉ một lần tính gradient, ta loại được cả nửa không gian còn lại khỏi vùng tìm kiếm. Về hình học, siêu phẳng đi qua $x$ với pháp tuyến $\nabla f(x)$ là một **siêu phẳng tựa** của tập mức dưới $\{y : f(y) \le f(x)\}$ tại $x$, đúng khái niệm ở chủ đề [siêu phẳng phân tách và siêu phẳng tựa](./sieu-phang-phan-tach-va-tua.md). Tập mức dưới nằm trọn một phía, còn gradient chỉ ra phía bên kia.

<GradientCutLab />

Hai hệ quả của hình ảnh này sẽ theo bạn suốt môn học.

- **Hướng giảm.** Đi từ $x$ theo hướng $\Delta x$ chỉ có thể làm $f$ giảm nếu $\nabla f(x)^T \Delta x < 0$, tức $\Delta x$ tạo góc nhọn với $-\nabla f(x)$. Lập luận này là nền tảng để định nghĩa hướng giảm của các phương pháp tối ưu không ràng buộc. Phương pháp gradient chọn chính $\Delta x = -\nabla f(x)$, hướng mà theo xấp xỉ bậc nhất làm $f$ giảm nhanh nhất trong các hướng có cùng độ dài.
- **Thu hẹp vùng chứa nghiệm.** Nếu nghiệm nằm trong một vùng đã biết, mỗi gradient cắt vùng đó làm đôi và giữ lại một nửa. Lặp lại, vùng chứa nghiệm co dần. Đây là ý tưởng của các phương pháp mặt phẳng cắt.

Trong mô phỏng, hàm $-\exp(-x_1^2 - 2x_2^2)$ không phải hàm lồi, vậy mà phép loại bỏ nửa không gian vẫn luôn nghiệm đúng. Điều mà phép loại bỏ thật sự đòi hỏi chỉ là tính lồi của mọi tập mức dưới. Những hàm số có tính chất này được gọi là hàm **tựa lồi**. Có thể chứng minh được rằng một hàm khả vi là tựa lồi khi và chỉ khi hệ thức $f(y) \le f(x)$ kéo theo $\nabla f(x)^T (y - x) \le 0$. Điều kiện bậc nhất của hàm lồi mạnh hơn hẳn: Biểu thức không chỉ cho biết điểm tốt hơn nằm ở phía nào, mà còn định lượng được $f(y)$ lớn hơn $f(x)$ ít nhất bao nhiêu. Cũng vì yếu hơn nên với hàm tựa lồi, gradient triệt tiêu không còn bảo đảm là điểm cực tiểu toàn cục. Chẳng hạn hàm $x^3$ là hàm đơn điệu nên tựa lồi trên $\mathbb{R}$, nhưng đạo hàm triệt tiêu tại gốc không tạo nên cực tiểu.

## 6. Gradient của hàm lồi là đơn điệu

Viết điều kiện bậc nhất hai lần, một lần đứng ở $x$ nhìn sang $y$, một lần đứng ở $y$ nhìn sang $x$:

$$
f(y) \ge f(x) + \nabla f(x)^T (y - x), \qquad f(x) \ge f(y) + \nabla f(y)^T (x - y).
$$

Cộng hai bất đẳng thức rồi chuyển vế, ta được

$$
\big(\nabla f(y) - \nabla f(x)\big)^T (y - x) \ge 0 .
$$

Khi $n = 1$, bất đẳng thức này nói $f'$ là hàm không giảm, điều quen thuộc với hàm lồi một biến. Khi $n \ge 2$, nó nói rằng khi di chuyển từ $x$ tới $y$, thành phần của gradient theo hướng di chuyển không giảm. Bất đẳng thức này phát biểu lại hình ảnh "đi dọc một đường thẳng, độ dốc tăng dần" của hàm hạn chế $g(t)$, mà không cần nhắc tới đường thẳng nào. Một ánh xạ $\psi$ thỏa mãn $(\psi(y) - \psi(x))^T (y - x) \ge 0$ với mọi $x, y$ được gọi là ánh xạ **đơn điệu** trong giải tích phi tuyến.

Chiều ngược lại không đúng khi $n \ge 2$: Không phải ánh xạ đơn điệu nào cũng là gradient của một hàm. Phép quay $\psi(x) = (-x_2, x_1)$ thỏa $(\psi(y) - \psi(x))^T (y - x) = 0$ với mọi $x, y$, nên đơn điệu. Nhưng nếu $\psi = \nabla f$ thì ma trận Jacobian của $\psi$ phải là Hessian của $f$, tức đối xứng, trong khi Jacobian của phép quay là $\begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}$.

## 7. Lồi nghiêm ngặt, hàm lõm và những điểm gãy

**Lồi nghiêm ngặt.** Hàm khả vi $f$ lồi nghiêm ngặt khi và chỉ khi $\operatorname{dom} f$ lồi và $f(y) > f(x) + \nabla f(x)^T (y - x)$ với mọi $x \ne y$. Tiếp tuyến khi đó chỉ chạm đồ thị tại đúng một điểm. Hệ quả: Một hàm lồi nghiêm ngặt có **nhiều nhất một** điểm cực tiểu, vì tại điểm cực tiểu $x^\star$ gradient bằng 0, và bất đẳng thức chặt cho $f(y) > f(x^\star)$ với mọi $y \ne x^\star$. Nhưng "nhiều nhất một" khác với "có đúng một". Hàm $e^x$ lồi nghiêm ngặt, có cận dưới đúng là 0, vậy mà không đạt được cận đó ở đâu cả, vì đạo hàm $e^x$ luôn dương.

**Hàm lõm.** Mọi chiều bất đẳng thức đều đảo ngược: Hàm số $f$ lõm khi và chỉ khi $f(y) \le f(x) + \nabla f(x)^T (y - x)$, tức tiếp tuyến nằm trên toàn bộ đồ thị. Bất đẳng thức $\log y \le y - 1$ ở mục 3 là một ví dụ tiêu biểu.

**Khi không có đạo hàm.** Hàm $|x|$ lồi nhưng không khả vi tại 0, nên ở đó không có tiếp tuyến. Thay vào đó, mọi đường thẳng qua gốc với độ dốc $g \in [-1, 1]$ đều nằm dưới đồ thị, vì $|y| \ge g y$ với mọi $y$. Một số $g$ như vậy gọi là một **dưới đạo hàm** (subgradient) của $f$ tại 0. Tổng quát, $g$ là dưới đạo hàm của $f$ tại $x$ nếu

$$
f(y) \ge f(x) + g^T (y - x) \quad \text{với mọi } y,
$$

tức là điều kiện bậc nhất với $g$ thay cho gradient. Tại điểm khả vi, dưới đạo hàm duy nhất là gradient. Tại điểm gãy, có cả một tập dưới đạo hàm. Trong mô phỏng ở mục 1, chọn hàm $|x|$ và đặt $x_0 = 0$ để kéo thanh trượt độ dốc và thấy điều này. Khái niệm mở rộng này đặc biệt cần thiết cho những hàm số xuất hiện thường xuyên trong học máy như hàm kích hoạt ReLU $\max\{0, x\}$, hàm mất mát hinge $\max\{0, 1 - z\}$ trong máy vector hỗ trợ (SVM) và chuẩn $\ell_1$ trong hồi quy Lasso. Điều kiện tối ưu "gradient triệt tiêu" $\nabla f(x) = 0$ khi đó được thay thế bằng "vector không là một dưới đạo hàm", tức $0 \in \partial f(x)$. Với hàm $|x|$, điều kiện này nghiệm đúng tại gốc vì $0 \in [-1, 1]$, và gốc tọa độ chính là điểm cực tiểu toàn cục.

## 8. Những câu hỏi để đào sâu

**Câu 1.** Tại một điểm $x$ cụ thể, bất đẳng thức $f(y) \ge f(x) + \nabla f(x)^T (y - x)$ đúng với mọi $y$. Như vậy đã đủ để kết luận $f$ lồi chưa?

<details><summary>Xem lời giải thích</summary>

Chưa đủ. Định lý đòi bất đẳng thức đúng tại **mọi** $x$, chứ không phải tại một điểm. Hàm giếng đôi $f(x) = (x^2 - 1)^2$ có $f(1) = 0$ và $f'(1) = 0$, nên tiếp tuyến tại 1 là đường $y = 0$, nằm dưới toàn bộ đồ thị vì $f \ge 0$. Thế nhưng $f''(0) = -4 < 0$, nên hàm không lồi. Tổng quát hơn, tại điểm cực tiểu toàn cục của một hàm khả vi bất kỳ, tiếp tuyến nằm ngang luôn nằm dưới đồ thị. Tính lồi đòi hỏi điều đó ở cả những điểm "xấu" như đỉnh đồi giữa hai giếng.

</details>

**Câu 2.** Một hàm lồi khả vi trên $\mathbb{R}^n$ có gradient khác 0 tại mọi điểm. Bạn kết luận được gì về bài toán cực tiểu hóa nó?

<details><summary>Xem lời giải thích</summary>

Bài toán không có nghiệm, theo nghĩa cực tiểu không đạt được ở đâu cả. Nếu $x^\star$ là một điểm cực tiểu thì, vì miền xác định mở, gradient tại đó phải bằng 0, mâu thuẫn với giả thiết. Giá trị cận dưới vẫn có thể hữu hạn, như $e^x$ có cận dưới 0, hoặc bằng $-\infty$, như hàm tuyến tính $x_1$. Hàm $\log(e^{x_1} + e^{x_2})$ là một ví dụ hai chiều: Dọc hướng $(-1, -1)$ nó giảm mãi về $-\infty$. Trong học máy, hồi quy logistic trên dữ liệu tách được tuyến tính rơi vào đúng tình huống này: Hàm mất mát giảm mãi khi trọng số phình to, và không có nghiệm hữu hạn.

</details>

**Câu 3.** Với $f(x) = x^2$ đứng tại $x = 1$, phương pháp gradient đi tới $y = 1 - 2\eta$. Mô hình tuyến tính dự đoán $f(y) \approx 1 - 4\eta$. So sánh dự đoán với giá trị thật khi $\eta = 0.25$, $0.75$ và $1.2$. Bài học là gì?

<details><summary>Xem lời giải thích</summary>

| $\eta$ | $y$ | $f(y)$ thật | Mô hình tuyến tính dự đoán |
| --- | --- | --- | --- |
| 0.25 | 0.5 | 0.25 | 0 |
| 0.75 | −0.5 | 0.25 | −2 |
| 1.2 | −1.4 | 1.96 | −3.8 |

Lần nào mô hình tuyến tính cũng hứa nhiều hơn những gì thật sự xảy ra, và điều này không phải ngẫu nhiên. Điều kiện bậc nhất nói đúng rằng $f(y) \ge f(x) + \nabla f(x)^T (y - x)$, tức với hàm lồi, mức giảm thật không bao giờ vượt mức giảm mà xấp xỉ bậc nhất dự đoán. Với bước quá dài như $\eta = 1.2$, hàm còn tăng từ 1 lên 1.96. Vì thế các thuật toán thực tế phải kiểm soát độ dài bước. Phép tìm kiếm bước quay lui (backtracking line search) trong các thuật toán tối ưu thực tế chỉ chấp nhận độ dài bước $t$ khi mức giảm thực tế đạt ít nhất một tỷ lệ $\alpha \in (0, 0.5)$ của mức giảm dự đoán theo xấp xỉ tuyến tính, cụ thể là $f(x + t\Delta x) \le f(x) + \alpha t \nabla f(x)^T \Delta x$.

</details>

**Câu 4.** Tiếp tuyến của một hàm lồi tại $x$ có thể chạm đồ thị tại một điểm khác $x$ không?

<details><summary>Xem lời giải thích</summary>

Có thể, khi hàm affine trên một đoạn chứa $x$. Với $f(x) = |x|$ và $x = 1$, tiếp tuyến là đường $y = x$, trùng với đồ thị trên cả nửa trục $[0, \infty)$. Chỉ tính lồi nghiêm ngặt mới cấm điều này, vì khi đó bất đẳng thức là chặt với mọi $y \ne x$. Đây cũng là lý do một hàm lồi không nghiêm ngặt có thể có cả một đoạn điểm cực tiểu. Hàm $\max\{|x| - 1,\ 0\}$ là hàm mất mát $\varepsilon$-insensitive với $\varepsilon = 1$ của hồi quy vector hỗ trợ, trong đó sai số có độ lớn không quá $\varepsilon$ thì không bị phạt. Hàm này đạt cực tiểu bằng 0 trên cả đoạn $[-1, 1]$, và tiếp tuyến nằm ngang tại $x = 0$ trùng với đồ thị trên cả đoạn ấy.

</details>

## 9. Bài tập tự luyện

::: exercise 1. Bất đẳng thức từ tiếp tuyến
Dùng điều kiện bậc nhất cho một hàm thích hợp tại một điểm thích hợp để chứng minh: (a) $e^y \ge e\,y$ với mọi $y \in \mathbb{R}$, và (b) $y \log y \ge y - 1$ với mọi $y > 0$. Dấu bằng xảy ra khi nào?
:::

::: solution
(a) Hàm $e^x$ lồi, và tiếp tuyến tại $x = 1$ là $e + e(y - 1) = e\,y$, nên $e^y \ge e\,y$. Vì $e^x$ lồi nghiêm ngặt, dấu bằng chỉ xảy ra tại $y = 1$. (b) Hàm $f(x) = x \log x$ lồi trên $x > 0$ với $f(1) = 0$ và $f'(1) = \log 1 + 1 = 1$. Tiếp tuyến tại 1 là $y - 1$, nên $y \log y \ge y - 1$. Vì $f''(x) = 1/x > 0$, hàm lồi nghiêm ngặt và dấu bằng chỉ xảy ra tại $y = 1$.
:::

::: exercise 2. Nhát cắt của một gradient
Cho $f(x) = x_1^2 + 2x_2^2 - 2x_1 + 4x_2$ và điểm $x = (2, 1)$. (a) Tính $\nabla f(x)$ và viết nửa mặt phẳng chứa mọi điểm tốt hơn $x$. (b) Không tính $f$, hãy cho biết điểm $(-1, 2)$ có thể tốt hơn $x$ không. Câu hỏi tương tự cho $(3, 0)$. (c) Kiểm tra lại bằng cách tính $f$.
:::

::: solution
(a) $\nabla f(x) = (2x_1 - 2,\ 4x_2 + 4) = (2, 8)$. Mọi điểm tốt hơn thỏa $2(y_1 - 2) + 8(y_2 - 1) < 0$, tức $y_1 + 4y_2 < 6$. (b) Điểm $(-1, 2)$ cho $-1 + 8 = 7 \ge 6$, nằm ở nửa bị loại, nên chắc chắn không tốt hơn $x$. Điểm $(3, 0)$ cho $3 < 6$, nằm ở nửa còn lại, và nhát cắt không kết luận được gì: Điểm đó có thể tốt hơn hoặc không. (c) $f(x) = 4 + 2 - 4 + 4 = 6$, $f(-1, 2) = 1 + 8 + 2 + 8 = 19 \ge 6$, và $f(3, 0) = 9 - 6 = 3 < 6$. Vậy $(3, 0)$ thật sự tốt hơn. Nghiệm tối ưu $(1, -1)$ với $f = -3$ cũng nằm ở nửa được giữ lại, vì $1 - 4 = -3 < 6$.
:::

::: exercise 3. Softplus và sigmoid
Cho $f(x) = \log(1 + e^x)$, hàm softplus thường dùng như một phiên bản trơn của ReLU. (a) Chứng minh $f'(x) = \sigma(x)$ với $\sigma(x) = 1/(1 + e^{-x})$ là hàm sigmoid. (b) Dùng tính đơn điệu của $\sigma$ để chứng minh $f$ thỏa điều kiện bậc nhất, từ đó suy ra $f$ lồi.
:::

::: solution
(a) $f'(x) = e^x / (1 + e^x)$, chia cả tử và mẫu cho $e^x$ được $1/(e^{-x} + 1) = \sigma(x)$. (b) $\sigma$ tăng vì $e^{-x}$ giảm. Với $y > x$, ta có $\sigma(t) \ge \sigma(x)$ trên đoạn từ $x$ tới $y$, nên

$$
f(y) - f(x) = \int_x^y \sigma(t)\,dt \ge \sigma(x)(y - x).
$$

Với $y < x$, ta có $\sigma(t) \le \sigma(x)$ trên đoạn từ $y$ tới $x$, nên

$$
f(y) - f(x) = -\int_y^x \sigma(t)\,dt \ge -\sigma(x)(x - y) = \sigma(x)(y - x).
$$

Cả hai trường hợp cho $f(y) \ge f(x) + f'(x)(y - x)$, nên $f$ lồi. Hàm mất mát của hồi quy logistic được ghép từ chính những hàm này, như chủ đề cuối của chương sẽ chỉ ra.
:::

## Tóm tắt

Với hàm khả vi, $f$ lồi khi và chỉ khi miền xác định lồi và mọi tiếp tuyến, hay siêu phẳng tiếp xúc, nằm dưới toàn bộ đồ thị. Xấp xỉ bậc nhất của hàm lồi là một cận dưới toàn cục, nên thông tin tại một điểm cho kết luận trên toàn miền. Điểm dừng là cực tiểu toàn cục. Giá trị và gradient tại điểm hiện tại cho một cận dưới kiểm chứng được của $p^\star$. Mọi điểm tốt hơn đều nằm trong nửa không gian $\nabla f(x)^T (y - x) < 0$.

Nhiều bất đẳng thức cổ điển chỉ là tiếp tuyến của một hàm lồi hay lõm, và độ phân kỳ KL chính là khoảng cách từ entropy âm tới siêu phẳng tiếp xúc của nó. Gradient của hàm lồi là ánh xạ đơn điệu. Lồi nghiêm ngặt cho bất đẳng thức chặt và nhiều nhất một điểm cực tiểu. Tại điểm gãy, dưới đạo hàm thay vai trò của gradient.

## Tài liệu tham khảo

- Stephen Boyd, Lieven Vandenberghe, *Convex Optimization*, Cambridge University Press.
