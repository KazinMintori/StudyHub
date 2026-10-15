---
course: toan-cho-ai
lecture: bai-01-nhap-mon-toi-uu
topic: cac-ham-loi-quen-thuoc
section: topic
title: "Những hàm lồi thường gặp"
description: "Bảng các hàm lồi và lõm cơ bản cùng cách chứng minh: Lũy thừa, mũ, logarit, entropy âm, chuẩn, hàm max, log-sum-exp và softmax, trung bình nhân, log det, entropy và phân phối đều. Chọn công cụ chứng minh phù hợp cho từng loại hàm."
---

Khi học giải tích, ta không tính lại mọi thứ từ định nghĩa giới hạn. Ta ghi nhớ một bảng đạo hàm của các hàm cơ bản, rồi vận dụng các quy tắc tổng, tích, hợp để xử lý những biểu thức phức tạp. Với bài toán khảo sát tính lồi cũng vậy. Dưới đây là bảng tra cứu chuẩn mực gồm những hàm lồi và lõm cốt lõi trong học máy, mỗi hàm đều đi kèm lập luận toán học chặt chẽ. Bài học tiếp theo sẽ cung cấp các quy tắc bảo toàn tính lồi khi phối hợp chúng.

Ở các chủ đề trước, ta đã trang bị ba công cụ phân tích: Định nghĩa hình học bằng dây cung, điều kiện đạo hàm bậc hai (Hessian), và phương pháp hạn chế lên đường thẳng. Mỗi ví dụ dưới đây được chọn lọc nhằm minh họa đúng phạm vi hiệu quả của từng công cụ. Hiểu rõ vì sao một công cụ phù hợp với một dạng hàm cụ thể cũng quan trọng không kém việc ghi nhớ kết quả.

## 1. Hàm một biến

Đối với hàm một biến khả vi hai lần, ta chỉ cần khảo sát dấu của đạo hàm bậc hai $f''(x)$:

- **Hàm mũ**: Hàm số $e^{ax}$ lồi trên $\mathbb{R}$ với mọi $a \in \mathbb{R}$, bởi vì $f''(x) = a^2 e^{ax} \ge 0$.
- **Lũy thừa**: Hàm số $x^a$ trên miền $\mathbb{R}_{++}$ lồi khi $a \ge 1$ hoặc $a \le 0$, và lõm khi $0 \le a \le 1$. Đạo hàm bậc hai là $f''(x) = a(a-1)x^{a-2}$, và vì $x^{a-2} > 0$ trên $\mathbb{R}_{++}$, dấu của $f''$ phụ thuộc hoàn toàn vào dấu của tích $a(a-1)$.
- **Lũy thừa của trị tuyệt đối**: Hàm số $|x|^p$ với $p \ge 1$ lồi trên toàn bộ $\mathbb{R}$.
- **Logarit**: Hàm số $\log x$ lõm trên $\mathbb{R}_{++}$, bởi vì $f''(x) = -1/x^2 < 0$.
- **Entropy âm**: Hàm số $x \log x$ lồi trên $\mathbb{R}_{++}$, và vẫn duy trì tính lồi trên $\mathbb{R}_+$ khi gán giá trị liên tục tại 0 là $0 \log 0 = 0$. Tại đây $f'(x) = \log x + 1$ và $f''(x) = 1/x > 0$.

Dòng về lũy thừa chứa nhiều thông tin nhất, và mô phỏng sau cho phép người học khảo sát toàn bộ họ hàm qua thanh trượt tương tác.

<PowerLab />

Hai giá trị $a = 0$ và $a = 1$ là hai "bản lề": Tại đó $x^a$ là hằng số hoặc tuyến tính, vừa lồi vừa lõm, và khi $a$ đi qua chúng, hàm đổi từ lồi sang lõm hay ngược lại. Hai hàm $1/x$ (ứng với $a = -1$) và $x^2$ cùng lồi, dù một hàm giảm và một hàm tăng. Tính lồi nói về **độ cong**, không nói về chiều biến thiên.

Điều kiện $p \ge 1$ trong dòng thứ ba không thể bỏ. Với $p = 0.5$, hàm $|x|^{0.5}$ tại trung điểm $0.5$ của đoạn $[0, 1]$ có giá trị $\sqrt{0.5} \approx 0.707$, trong khi dây cung cho $\tfrac12(0 + 1) = 0.5$. Đồ thị vượt lên trên dây cung, nên hàm không lồi.

## 2. Chuẩn và hàm max: Dùng định nghĩa

Hai hàm tiếp theo không khả vi ở mọi nơi, nên điều kiện bậc hai không dùng được. May là định nghĩa cho lời chứng minh chỉ trong một dòng.

**Mọi chuẩn đều lồi.** Với chuẩn $\|\cdot\|$ và $0 \le \theta \le 1$, bất đẳng thức tam giác rồi tính thuần nhất cho

$$
\|\theta x + (1-\theta) y\| \le \|\theta x\| + \|(1-\theta) y\| = \theta \|x\| + (1 - \theta)\|y\|.
$$

**Hàm max lồi.** Với $f(x) = \max_i x_i$, mỗi thành phần $\theta x_i + (1-\theta) y_i$ không vượt quá $\theta \max_j x_j + (1 - \theta) \max_j y_j$. Lấy max theo $i$ ở vế trái, ta được $f(\theta x + (1-\theta)y) \le \theta f(x) + (1-\theta) f(y)$.

Hai lập luận này cho thấy một quy luật: Khi hàm được định nghĩa bằng những phép toán "thô" như trị tuyệt đối, max, chuẩn, định nghĩa thường là con đường ngắn nhất. Hàm mất mát hinge $\max\{0,\ 1 - z\}$ của máy vector hỗ trợ và hàm ReLU $\max\{0, x\}$ đều thuộc loại này. Chủ đề sau sẽ tổng quát hóa thành quy tắc "max của các hàm lồi là hàm lồi".

## 3. Log-sum-exp: Hàm max được làm trơn

Hàm max có các góc nhọn tại những điểm có từ hai thành phần bằng nhau trở lên, và những điểm góc nhọn không khả vi này gây trở ngại cho các thuật toán tối ưu dựa trên đạo hàm. Hàm **log-sum-exp**

$$
f(x) = \log\Big(\sum_{i=1}^n e^{x_i}\Big) = \log\big(e^{x_1} + e^{x_2} + \cdots + e^{x_n}\big)
$$

được xem là một phiên bản làm trơn (smooth approximation) của hàm max. Do bất đẳng thức kép hiển nhiên $e^{\max_i x_i} \le \sum_{i=1}^n e^{x_i} \le n\, e^{\max_i x_i}$, lấy logarit tự nhiên ba vế ta thu được:

$$
\max_i x_i \ \le\ f(x) \ \le\ \max_i x_i + \log n .
$$

Bất đẳng thức bên phải đạt dấu bằng khi và chỉ khi mọi thành phần bằng nhau. Với $x = (2, 2, 2)$, $f(x) = 2 + \log 3 \approx 3.099$. Khi có một thành phần vượt trội, $f(x)$ tiến sát về giá trị cực đại: Chẳng hạn với $x = (3, 1, 0)$, $f(x) \approx 3.170$, chỉ chênh lệch nhẹ so với $\max_i x_i = 3$.

Để điều chỉnh linh hoạt độ trơn, ta đưa thêm tham số **nhiệt độ nghịch đảo** $\beta > 0$:

$$
f_\beta(x) = \frac{1}{\beta}\log\Big(\sum_{i=1}^n e^{\beta x_i}\Big), \qquad \max_i x_i \le f_\beta(x) \le \max_i x_i + \frac{\log n}{\beta}.
$$

Với $x = (3, 1, 0)$, khoảng cách $f_\beta(x) - 3$ bằng khoảng $0.170$ khi $\beta = 1$, giảm xuống $0.0103$ khi $\beta = 2$ và chỉ còn dưới $10^{-5}$ khi $\beta = 5$. Gradient của $f_\beta$ là một vector xác suất quen thuộc:

$$
\frac{\partial f_\beta}{\partial x_i} = \frac{e^{\beta x_i}}{\sum_{j=1}^n e^{\beta x_j}} = \operatorname{softmax}(\beta x)_i .
$$

Mỗi thành phần của gradient đều không âm và tổng của chúng đúng bằng 1. Khi $\beta \to \infty$, phân phối softmax sẽ tập trung hầu hết trọng số vào thành phần lớn nhất, hoàn toàn khớp với dưới đạo hàm của hàm max.

<SoftmaxLab />

**Vì sao log-sum-exp lồi: Một cách nhìn trực quan bằng phương sai.** Đặt vector xác suất $p = \operatorname{softmax}(x)$. Tính đạo hàm thêm một lần, ma trận Hessian của $f$ có dạng:

$$
\nabla^2 f(x) = \operatorname{diag}(p) - p p^T .
$$

Với mọi vector hướng $v \in \mathbb{R}^n$, dạng toàn phương tương ứng được khai triển thành:

$$
\begin{aligned}
v^T \nabla^2 f(x)\, v &= \sum_{i=1}^n p_i v_i^2 - \Big(\sum_{i=1}^n p_i v_i\Big)^2 \\
&= \sum_{i=1}^n p_i \Big(v_i - \sum_{j=1}^n p_j v_j\Big)^2 \ge 0 .
\end{aligned}
$$

Vế phải chính là **phương sai** của một biến ngẫu nhiên rời rạc nhận giá trị $v_i$ với xác suất tương ứng $p_i$. Vì phương sai không bao giờ âm, ma trận Hessian luôn nửa xác định dương và $f$ là hàm lồi. Lập luận này tương đương với bất đẳng thức Cauchy–Schwarz $(\sum_i p_i v_i)^2 \le \sum_i p_i v_i^2$ (do $\sum_i p_i = 1$). Cách nhìn qua phương sai còn cho thấy điều kiện để độ cong triệt tiêu: Phương sai bằng 0 khi và chỉ khi biến ngẫu nhiên là hằng số, tức mọi $v_i$ bằng nhau hay $v = c(1, \dots, 1)$. Đây là lý do dọc theo hướng đường chéo $(1, \dots, 1)$, hàm log-sum-exp tăng tuyến tính và có độ cong bằng 0.

**Liên hệ với hàm mất mát entropy chéo.** Một mô hình phân loại $n$ lớp xuất ra vector logit $z$. Với mẫu có nhãn đúng là lớp $y$, hàm mất mát entropy chéo (cross-entropy loss) được định nghĩa:

$$
L(z) = -\log \operatorname{softmax}(z)_y = \log \sum_{j=1}^n e^{z_j} - z_y .
$$

Biểu thức này chính là hàm log-sum-exp trừ đi một hàm tuyến tính $z_y$, do đó $L$ lồi theo vector logit $z$. Gradient của nó bằng $\operatorname{softmax}(z) - e_y$. Chẳng hạn với $z = (2, 1, -1)$ và nhãn đúng là lớp thứ nhất ($y = 1$), ta tính được $L \approx 0.349$ và $\operatorname{softmax}(z) \approx (0.705,\ 0.260,\ 0.035)$. Thành phần thứ $y$ của gradient bằng $p_y - 1$, luôn âm vì $p_y < 1$, nên gradient không bao giờ triệt tiêu hoàn toàn và $L$ không đạt điểm cực tiểu tại hữu hạn: Tăng logit $z_y$ thêm 10 sẽ kéo $L$ xuống khoảng $1.9 \times 10^{-5}$, nhưng không bao giờ đạt đúng 0.

## 4. Trung bình nhân: Một hàm lõm thuần nhất

**Trung bình nhân**: Hàm trung bình nhân $f(x) = (x_1 x_2 \cdots x_n)^{1/n}$ là một hàm lõm trên miền $\mathbb{R}^n_{++}$. Ta có thể chứng minh tính lõm của nó thông qua ma trận Hessian kết hợp bất đẳng thức Cauchy–Schwarz, tương tự cấu trúc lập luận của hàm log-sum-exp. Chẳng hạn khi thử nghiệm bằng số: Ta có $f(1, 4) = 2$ và $f(4, 1) = 2$, trong khi tại trung điểm $(2.5,\ 2.5)$ thì $f(2.5, 2.5) = 2.5 \ge 2$, hoàn toàn phù hợp với chiều bất đẳng thức của hàm lõm.

Trung bình nhân có chung một đặc tính hình học với chuẩn và hàm $x^2/y$: Đó là tính **thuần nhất bậc một**, $f(tx) = t f(x)$ với mọi $t > 0$. Dọc theo mỗi tia xuất phát từ gốc tọa độ, đồ thị là một đường thẳng. Một hàm thuần nhất bậc một vì thế không bao giờ lồi nghiêm ngặt hay lõm nghiêm ngặt, và độ cong của nó được quyết định hoàn toàn bởi các phương cắt ngang qua các tia.

Bất đẳng thức kinh điển giữa trung bình cộng và trung bình nhân (AM-GM):

$$
(x_1 x_2 \cdots x_n)^{1/n} \le \frac{x_1 + x_2 + \cdots + x_n}{n}
$$

chính là một hệ quả trực tiếp của tính lõm của hàm $\log$. Với $x = (1, 4, 16)$, trung bình nhân bằng 4, nhỏ hơn hẳn trung bình cộng bằng 7.

## 5. Log det: Khi biến là một ma trận

Hàm $f(X) = \log\det X$ trên tập các ma trận đối xứng xác định dương $\mathbb{S}^n_{++}$ là hàm lõm. Do việc tính toán ma trận Hessian của hàm theo biến ma trận rất phức tạp, ta vận dụng công cụ hạn chế hàm lên một đường thẳng $X = Z + tV$ với $Z \succ 0$ và $V$ là ma trận đối xứng. Đặt $g(t) = \log\det(Z + tV)$ và phân tích $Z = Z^{1/2} Z^{1/2}$:

$$
g(t) = \log\det\Big(Z^{1/2}\big(I + t\, Z^{-1/2} V Z^{-1/2}\big) Z^{1/2}\Big) = \log\det Z + \sum_{i=1}^n \log(1 + t\lambda_i),
$$

trong đó $\lambda_i$ là các trị riêng của ma trận đối xứng $Z^{-1/2} V Z^{-1/2}$. Bước biến đổi này sử dụng hai tính chất đại số cơ bản: Định thức của tích bằng tích các định thức, và ma trận $I + tW$ có các trị riêng là $1 + t\lambda_i$ khi $W$ có các trị riêng $\lambda_i$. Khi đó $g(t)$ là tổng của các hàm logarit một biến, và:

$$
g''(t) = -\sum_{i=1}^n \frac{\lambda_i^2}{(1 + t\lambda_i)^2} \le 0 .
$$

Do $g''(t) \le 0$ trên mọi đường thẳng, hàm $\log\det$ là hàm lõm. Phép chứng minh này là một minh chứng tiêu biểu cho sức mạnh của phương pháp hạn chế lên đường thẳng: Biến một bài toán ma trận phức tạp thành bài toán khảo sát các hàm một biến quen thuộc.

::: example Log det dọc một đường thẳng cụ thể
Lấy $Z = I$ cỡ $2 \times 2$ và $V = \begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix}$, ma trận có hai trị riêng $\pm\sqrt2$. Khi đó:

$$
g(t) = \log(1 + \sqrt2\, t) + \log(1 - \sqrt2\, t) = \log(1 - 2t^2),
$$

xác định khi $|t| < 1/\sqrt2 \approx 0.707$, đúng bằng khoảng mà ma trận $I + tV$ còn giữ được tính xác định dương. Tại $t = \pm 0.5$, $g(t) = \log 0.5 \approx -0.693$, còn tại trung điểm $t = 0$, $g(0) = 0 \ge -0.693$, thỏa mãn đúng chiều của hàm lõm. Độ cong tại 0 là $g''(0) = -\sum_i \lambda_i^2 = -4$.
:::

Hàm log det xuất hiện trong nhiều ứng dụng tối ưu quan trọng. Thể tích của hình ellipsoid $\{x : (x - x_c)^T P^{-1}(x - x_c) \le 1\}$ tỉ lệ thuận với $(\det P)^{1/2}$, nên các bài toán tìm ellipsoid bao nhỏ nhất hay ellipsoid nội tiếp lớn nhất đều dẫn về bài toán tối ưu hàm $\log\det$. Một ví dụ kinh điển khác đến từ thống kê và học máy: Khi ước lượng ma trận hiệp phương sai $\Sigma$ của một phân phối chuẩn Gauss đa biến bằng phương pháp hợp lý cực đại, hàm log-likelihood không lõm theo $\Sigma$. Tuy nhiên, khi đổi biến sang ma trận độ chính xác $S = \Sigma^{-1}$, bài toán chuyển thành cực đại hóa $\tfrac{N}{2}\big(\log\det S - \operatorname{tr}(SY)\big)$ (với $Y$ là ma trận hiệp phương sai mẫu), đây là một hàm lõm theo $S$. Cùng một bài toán tối ưu có thể không lồi ở hệ biến ban đầu nhưng trở thành lồi ở một hệ biến phù hợp, và việc lựa chọn đúng hệ biểu diễn là nghệ thuật mô hình hóa toán học.

## 6. Entropy và phân phối đều

Với phân phối xác suất $p = (p_1, \dots, p_n)$, **entropy** $H(p) = -\sum_i p_i \log p_i$ là tổng của các hàm lõm $-p_i \log p_i$, nên lõm. Entropy đo mức độ bất định: Phân phối dồn hết vào một kết quả có entropy 0, còn phân phối đều có entropy lớn nhất bằng $\log n$.

Tính lõm cho một lời chứng minh rất gọn của khẳng định cuối, chỉ dùng tính đối xứng. Lấy một phân phối $p$ bất kỳ và xét mọi hoán vị của nó. Vì $H$ không thay đổi khi đổi chỗ các thành phần, mọi hoán vị có cùng entropy $H(p)$. Trung bình cộng của tất cả các hoán vị là phân phối đều $u$, vì mỗi thành phần $p_i$ xuất hiện ở mỗi vị trí với tần suất như nhau. Tính lõm cho entropy của trung bình lớn hơn hoặc bằng trung bình các entropy:

$$
H(u) \ \ge\ \frac{1}{n!}\sum_{\sigma} H(p_\sigma) = H(p).
$$

Với $p = (0.5, 0.3, 0.2)$, sáu hoán vị có trung bình đúng bằng $(\tfrac13, \tfrac13, \tfrac13)$, và quả thật $H(p) \approx 1.030 < \log 3 \approx 1.099$. Lập luận này dùng được cho mọi hàm lõm và đối xứng, không chỉ cho entropy. Trong học tăng cường, người ta thường cộng thêm entropy của chiến lược hành động (policy) vào hàm mục tiêu để khuyến khích tác tử khám phá nhiều hành động thay vì sớm dồn hết xác suất vào một hành động duy nhất.

## 7. Chọn công cụ nào

| Loại hàm | Công cụ thường hợp nhất | Ví dụ trên trang này |
| --- | --- | --- |
| Một biến, khả vi hai lần | Dấu của $f''$ | $x^a$, $e^{ax}$, $x\log x$ |
| Có max, trị tuyệt đối, chuẩn | Định nghĩa với dây cung | chuẩn, $\max_i x_i$ |
| Nhiều biến, Hessian có dạng đẹp | Điều kiện Hessian, thường kèm Cauchy–Schwarz hoặc một cách nhìn xác suất | log-sum-exp, trung bình nhân, $x^2/y$ |
| Biến là ma trận | Hạn chế lên đường thẳng | $\log\det X$ |
| Ghép từ các hàm trên | Các phép toán giữ tính lồi (chủ đề sau) | entropy chéo, hinge |

## 8. Những câu hỏi để đào sâu

**Câu 1.** Bảng ở mục 1 nói $x^3$ lồi trên $\mathbb{R}_{++}$. Vì sao không phát biểu luôn "trên $\mathbb{R}$"? Và với $a = 2.5$, hàm $x^a$ có xác định trên $x < 0$ không?

<details><summary>Xem lời giải thích</summary>

$x^3$ không lồi trên $\mathbb{R}$, vì $f''(x) = 6x < 0$ khi $x < 0$, như câu hỏi đầu tiên của chủ đề hàm lồi đã chỉ ra bằng một dây cung. Còn với số mũ không nguyên như $2.5$, biểu thức $x^{2.5}$ không có nghĩa trên số thực khi $x < 0$. Vì vậy ta phát biểu toàn bộ họ hàm lũy thừa $x^a$ trên $\mathbb{R}_{++}$, nơi mọi số mũ thực đều có nghĩa và dấu của $f''$ phụ thuộc duy nhất vào dấu của tích số $a(a - 1)$. Nếu muốn một hàm lồi trên toàn $\mathbb{R}$, ta dùng $|x|^p$ với $p \ge 1$.

</details>

**Câu 2.** Trong học máy, cộng cùng một hằng số $c$ vào mọi logit không làm thay đổi xác suất softmax. Hiện tượng này liên quan thế nào tới Hessian của log-sum-exp?

<details><summary>Xem lời giải thích</summary>

Ta có $f(z + c\mathbf{1}) = f(z) + c$, nên dọc hướng $\mathbf{1} = (1, \dots, 1)$ hàm log-sum-exp tuyến tính và Hessian có trị riêng 0 theo hướng đó. Theo cách nhìn phương sai, $v = \mathbf{1}$ cho biến ngẫu nhiên hằng số, phương sai 0. Gradient $\operatorname{softmax}(z)$ vì thế không đổi khi đi dọc hướng này. Hệ quả thực tế: Vector logit chỉ được xác định sai khác một hằng số cộng. Nếu tối ưu trực tiếp theo logit, hàm mất mát có cả một đường thẳng các điểm tương đương, giống cái máng của hai đặc trưng cộng tuyến ở chủ đề trước.

</details>

**Câu 3.** Hàm $\min_i x_i$ có lồi không? Còn hàm $-\log\big(e^{-x_1} + \cdots + e^{-x_n}\big)$?

<details><summary>Xem lời giải thích</summary>

$\min_i x_i = -\max_i(-x_i)$ là âm của một hàm lồi hợp với phép biến đổi tuyến tính, nên **lõm**, không lồi. Với $x = (0, 1)$ và $y = (1, 0)$, ta có $\min x = \min y = 0$, nhưng trung điểm $(0.5,\ 0.5)$ cho $\min = 0.5 > 0$. Đồ thị nằm trên dây cung. Tương tự, $-\log\sum_i e^{-x_i} = -f(-x)$ với $f$ là log-sum-exp, nên đó là một hàm lõm, phiên bản trơn của min, nằm giữa $\min_i x_i - \log n$ và $\min_i x_i$.

</details>

**Câu 4.** Lập luận đối xứng ở mục 6 dùng hai tính chất của entropy: Lõm và đối xứng. Nếu bỏ đi một trong hai, kết luận "phân phối đều là tốt nhất" còn đúng không?

<details><summary>Xem lời giải thích</summary>

Không còn bảo đảm. Bỏ tính đối xứng: Hàm lõm $g(p) = \log p_1$ trên đơn hình đạt lớn nhất tại $p = (1, 0, \dots, 0)$ chứ không tại phân phối đều. Bỏ tính lõm: Hàm đối xứng $\sum_i p_i^2$ là hàm lồi, và nó đạt **nhỏ nhất** tại phân phối đều, còn lớn nhất tại các đỉnh của đơn hình. Lập luận đối xứng chỉ chạy được khi cả hai tính chất cùng có mặt, và nó cho ta một mẹo dùng được lâu dài: Với bài toán lõm và đối xứng, hãy thử nghiệm đối xứng trước.

</details>

## 9. Bài tập tự luyện

::: exercise 1. Phân loại nhanh
Mỗi hàm sau lồi, lõm, hay không thuộc loại nào? (a) $x^{-1/2}$ trên $\mathbb{R}_{++}$. (b) $x^{1.5}$ trên $\mathbb{R}_{++}$. (c) $-x^{0.3}$ trên $\mathbb{R}_{++}$. (d) $|x|^{0.5}$ trên $\mathbb{R}$. (e) $\max\{x_1,\ 2x_2,\ -x_1 - x_2\}$ trên $\mathbb{R}^2$.
:::

::: solution
(a) Lồi, vì $a(a - 1) = (-0.5)(-1.5) = 0.75 > 0$. (b) Lồi, vì $1.5 \cdot 0.5 = 0.75 > 0$. (c) $x^{0.3}$ lõm vì $0.3 \cdot (-0.7) < 0$, nên $-x^{0.3}$ lồi. (d) Không lồi: Tại trung điểm $0.5$ của đoạn $[0, 1]$, hàm bằng $0.707$ còn dây cung bằng $0.5$. Nó cũng không lõm: Tại trung điểm $0$ của đoạn $[-1, 1]$, hàm bằng $0$ còn dây cung bằng $1$, nên đồ thị nằm dưới dây cung. (e) Lồi, vì với mọi $x, y$ và $\theta \in [0, 1]$, mỗi hàm tuyến tính trong ngoặc tại $\theta x + (1-\theta) y$ không vượt quá $\theta f(x) + (1 - \theta) f(y)$, theo đúng lập luận của hàm max ở mục 2.
:::

::: exercise 2. Nhiệt độ và độ chính xác của log-sum-exp
Cho $x = (3, 1, 0)$. (a) Theo cận $\log n / \beta$, cần $\beta$ tối thiểu bao nhiêu để chắc chắn $f_\beta(x) - \max_i x_i \le 0.01$? (b) Thực tế, với $\beta = 2$ khoảng cách đã bằng bao nhiêu? Vì sao cận ở câu (a) lỏng với vector này?
:::

::: solution
(a) Cần $\log 3 / \beta \le 0.01$, tức $\beta \ge 100 \log 3 \approx 109.9$. (b) Với $\beta = 2$, $f_\beta(x) - 3 \approx 0.0103$, đã gần $0.01$. Cận $\log n / \beta$ đạt được chỉ khi mọi thành phần bằng nhau, lúc cả $n$ số hạng $e^{\beta x_i}$ đóng góp như nhau. Ở đây thành phần lớn nhất trội hơn các thành phần còn lại 2 đơn vị, nên $\sum_i e^{\beta x_i}$ gần như chỉ gồm số hạng $e^{3\beta}$, và khoảng cách thật là $\tfrac{1}{\beta}\log\big(1 + e^{-2\beta} + e^{-3\beta}\big)$, nhỏ hơn nhiều.
:::

::: exercise 3. Làm mềm nhãn cho entropy chéo
Thay nhãn one-hot bằng phân phối mục tiêu $q = (0.8,\ 0.1,\ 0.1)$, một kỹ thuật gọi là làm mềm nhãn. Hàm mất mát trở thành $L(z) = \log \sum_j e^{z_j} - q^T z$. (a) Chứng minh $L$ lồi. (b) Chứng minh mọi $z$ với $\operatorname{softmax}(z) = q$ đều là điểm cực tiểu, và chỉ ra một điểm như vậy. (c) Tính giá trị nhỏ nhất và so sánh với entropy của $q$. Vì sao hiện tượng "không có điểm cực tiểu" của nhãn one-hot biến mất?
:::

::: solution
(a) $L$ là log-sum-exp trừ một hàm tuyến tính, nên lồi. (b) $\nabla L(z) = \operatorname{softmax}(z) - q$, bằng 0 khi và chỉ khi $\operatorname{softmax}(z) = q$. Với hàm lồi khả vi, điểm dừng là cực tiểu toàn cục. Chẳng hạn $z^\star = (\log 0.8,\ \log 0.1,\ \log 0.1)$, hoặc bất kỳ $z^\star + c\mathbf{1}$, trong đó có $z = (\log 8,\ 0,\ 0) \approx (2.079,\ 0,\ 0)$. (c) Tại $z^\star = \log q$, ta có $\log\sum_j q_j = 0$, nên $L(z^\star) = -\sum_j q_j \log q_j = H(q) \approx 0.639$. Giá trị nhỏ nhất bằng đúng entropy của mục tiêu, khớp với kết luận "entropy chéo không nhỏ hơn entropy" ở chủ đề điều kiện bậc nhất. Với nhãn one-hot, mục tiêu có một thành phần bằng 1, mà softmax luôn có mọi thành phần dương, nên không bao giờ bằng được mục tiêu. Khi mọi $q_j > 0$, mục tiêu nằm trong phần trong của đơn hình và softmax chạm tới được, nên điểm cực tiểu tồn tại và hữu hạn.
:::

## Tóm tắt

Những hàm lồi cơ bản gồm $e^{ax}$, $x^a$ với $a \ge 1$ hoặc $a \le 0$ trên $\mathbb{R}_{++}$, $|x|^p$ với $p \ge 1$, $x \log x$, mọi chuẩn, hàm max, $x^2/y$ và log-sum-exp. Những hàm lõm cơ bản gồm $\log x$, $x^a$ với $0 \le a \le 1$, trung bình nhân, $\log\det X$ và entropy. Mỗi hàm có một công cụ chứng minh hợp với nó: Dấu $f''$ cho hàm một biến, định nghĩa cho các hàm có góc nhọn, Hessian kèm Cauchy–Schwarz cho log-sum-exp và trung bình nhân, hạn chế lên đường thẳng cho $\log\det$.

Log-sum-exp là phiên bản trơn của max, có gradient là softmax và Hessian là một ma trận hiệp phương sai, và nó là nền của hàm mất mát entropy chéo. Tính lõm cùng tính đối xứng cho thấy phân phối đều có entropy lớn nhất.

## Tài liệu tham khảo

- Stephen Boyd, Lieven Vandenberghe, *Convex Optimization*, Cambridge University Press.
