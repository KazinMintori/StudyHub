---
course: toan-cho-ai
lecture: bai-01-nhap-mon-toi-uu
topic: phep-toan-giu-tinh-loi-cua-ham
section: topic
title: "Các phép toán giữ tính lồi của hàm"
description: "Bộ quy tắc lắp ghép hàm lồi: Tổng có trọng số không âm, hợp với ánh xạ affine, max và supremum theo từng điểm, hàm lồi như bao trên của các hàm affine, quy tắc hợp hàm với điều kiện đơn điệu của mở rộng giá trị, cực tiểu hóa theo một phần biến và hàm Huber, phối cảnh của hàm, cùng những phép toán làm mất tính lồi."
---

Chủ đề trước cho ta một "bảng" các hàm lồi cơ bản. Chủ đề này cho các "quy tắc" lắp ghép chúng, tương tự như quy tắc tính đạo hàm cho tổng, tích, hợp. Nhờ những quy tắc này, để kiểm tra một hàm mất mát thực tế như $\frac1m\sum_{i=1}^m \log\big(1 + e^{-y_i x_i^T w}\big) + \lambda\|w\|_2^2$ có lồi theo $w$ hay không, ta không cần phải vất vả tính ma trận Hessian: Chỉ cần đọc biểu thức từ trong ra ngoài và kiểm tra từng mắt xích xem có tuân thủ các quy tắc bảo toàn tính lồi hay không.

Tuy nhiên, khác với đạo hàm, không phải phép toán thông thường nào cũng bảo toàn tính lồi. Phép nhân, phép chia, phép trừ, phép lấy min và phần lớn các phép hợp hàm đều có thể phá vỡ hoàn toàn tính lồi. Vì vậy, việc nắm vững các quy tắc dưới đây cũng đồng nghĩa với việc nhận diện chính xác các ranh giới toán học cần cảnh giác.

## 1. Hai quy tắc nền: Tổng không âm và hợp với ánh xạ affine

**Tổng có trọng số không âm**: Nếu các hàm $f_1, \dots, f_m$ đều lồi và các trọng số $w_1, \dots, w_m \ge 0$, thì tổ hợp tuyến tính không âm:

$$
f(x) = \sum_{i=1}^m w_i f_i(x) = w_1 f_1(x) + w_2 f_2(x) + \dots + w_m f_m(x)
$$

là một hàm lồi. Nói cách khác, tập hợp các hàm lồi tạo thành một **nón lồi** (convex cone). Quy tắc này mở rộng tự nhiên sang tổng vô hạn và tích phân: Nếu $f(x, y)$ lồi theo biến $x$ với mỗi $y$, và hàm trọng số $w(y) \ge 0$, thì tích phân $\int w(y) f(x, y)\,dy$ vẫn lồi theo $x$. Đây chính là lý do vì sao **kỳ vọng toán học** của một hàm mất mát lồi lấy theo phân phối dữ liệu vẫn giữ nguyên tính lồi theo tham số mô hình.

Điều kiện trọng số "không âm" là thật sự cần thiết: Xét hiệu $x^2 - 2x^2 = -x^2$, đây là hiệu của hai hàm lồi nhưng kết quả thu được lại là một hàm lõm.

**Hợp với ánh xạ affine**: Nếu hàm $f$ lồi thì hàm hợp $g(x) = f(Ax + b)$ cũng là hàm lồi. Quy tắc cơ bản này lý giải vì sao hầu như mọi hàm mất mát trong các mô hình học máy tuyến tính đều lồi theo tham số: Khi dữ liệu huấn luyện $x_i$ cố định, ánh xạ $w \mapsto x_i^T w$ là một ánh xạ tuyến tính, do đó ta chỉ cần kiểm tra xem hàm mất mát bên ngoài có lồi hay không:

- $\|Aw - b\|_2^2$ là bình phương chuẩn Euclid hợp với một ánh xạ affine.
- $\log\big(1 + e^{-y_i x_i^T w}\big)$ là hàm softplus (đã biết là lồi) hợp với ánh xạ tuyến tính $w \mapsto -y_i x_i^T w$.
- $\log \sum_{k=1}^K e^{a_k^T w + b_k}$ là hàm log-sum-exp lồi hợp với ánh xạ affine.

Cộng các số hạng tương ứng với từng mẫu dữ liệu với trọng số $1/m$ và cộng thêm thành phần điều chuẩn (regularization) bằng một chuẩn bất kỳ, ta thu được các hàm mất mát kinh điển của hồi quy tuyến tính, hồi quy logistic và hồi quy softmax, tất cả đều lồi toàn cục theo trọng số $w$.

## 2. Max, supremum, và hàm lồi như bao trên của các hàm affine

**Max theo từng điểm**: Nếu các hàm $f_1, \dots, f_m$ đều lồi thì hàm $f(x) = \max\{f_1(x), \dots, f_m(x)\}$ cũng là hàm lồi. Cách nhìn nhận trực quan nhất là thông qua biểu đồ trên (epigraph): Một điểm $(x, t)$ nằm trong epigraph của hàm max khi và chỉ khi nó nằm trong epigraph của từng hàm thành phần $f_i$, do đó $\operatorname{epi} f = \bigcap_{i=1}^m \operatorname{epi} f_i$. Vì giao của một họ các tập lồi luôn là một tập lồi, nên $\operatorname{epi} f$ lồi, kéo theo $f$ lồi.

Lập luận bằng epigraph không phụ thuộc vào số lượng hàm hữu hạn hay vô hạn, vì vậy quy tắc mở rộng trực tiếp sang phép lấy **supremum** của một họ vô hạn: Nếu hàm $f(x, y)$ lồi theo $x$ với mỗi $y \in \mathcal{A}$, thì hàm $g(x) = \sup_{y \in \mathcal{A}} f(x, y)$ là hàm lồi theo $x$. Một loạt các hàm số quan trọng trong học máy và tối ưu được chứng minh lồi chỉ bằng quy tắc này:

- **Hàm tuyến tính từng khúc**: Hàm $\max_{i=1}^m (a_i^T x + b_i)$ là hàm lồi. Hàm mất mát hinge $\max\{0,\ 1 - y\, x^T w\}$ trong máy vector hỗ trợ (SVM) là trường hợp cụ thể với hai khúc affine.
- **Tổng $r$ thành phần lớn nhất** của vector $x$: Được định nghĩa là max của mọi tổng gồm $r$ thành phần phân biệt. Chẳng hạn với $x = (3, -1, 4, 1, 5)$ và $r = 2$, đây là max của $\binom{5}{2} = 10$ hàm tuyến tính, cho kết quả $5 + 4 = 9$.
- **Hàm tựa** (support function): Hàm $S_C(x) = \sup_{y \in C} x^T y$ của một tập bất kỳ $C$. Đây là supremum của một họ hàm tuyến tính theo $x$, do đó luôn là hàm lồi bất kể tập $C$ có lồi hay không.
- **Trị riêng lớn nhất**: Đại lượng $\lambda_{\max}(X) = \sup_{\|y\|_2 = 1} y^T X y$ của ma trận đối xứng $X$. Với mỗi vector $y$ cố định, $y^T X y$ là hàm tuyến tính theo $X$, do đó $\lambda_{\max}(X)$ là hàm lồi. Thử nghiệm bằng số: Ta có $\lambda_{\max}$ của $\operatorname{diag}(1, 0)$ và của $\operatorname{diag}(0, 1)$ đều bằng 1, trong khi của ma trận trung bình $\tfrac12 I$ chỉ bằng $0.5 < 1$.

**Mọi hàm lồi đều là supremum của các hàm affine**: Tính chất trên gợi mở một phương pháp chứng minh tính lồi tổng quát: Biểu diễn hàm số dưới dạng supremum của một họ hàm affine. Thực tế, trừ một số trường hợp suy biến biên, mọi hàm lồi đều có thể biểu diễn theo cách này. Cụ thể, với hàm lồi $f$ có $\operatorname{dom} f = \mathbb{R}^n$:

$$
f(x) = \sup\{\, g(x) : g \text{ affine},\ g(z) \le f(z) \text{ với mọi } z \,\}.
$$

Lý do: Tại mỗi $x$, epigraph lồi có một siêu phẳng tựa tại $(x, f(x))$, và siêu phẳng đó không thể thẳng đứng, nên nó là đồ thị của một hàm affine nằm dưới $f$ và chạm $f$ tại $x$. Khi $f$ khả vi, đó chính là tiếp tuyến. Hàm lồi là **bao trên** của các tiếp tuyến của nó.

<EnvelopeLab />

Mô phỏng cho thấy max của $k$ tiếp tuyến tiến dần tới hàm khi $k$ tăng. Với $x^2$ và các tiếp điểm cách nhau $h$, hai tiếp tuyến kề nhau cắt nhau ở giữa, và sai số lớn nhất bằng $h^2/4$. Tăng gấp đôi số tiếp tuyến thì sai số giảm khoảng bốn lần. Mô hình "max các tiếp tuyến" luôn nằm **dưới** hàm thật, và đây là ý tưởng của các phương pháp mặt phẳng cắt: Mỗi lần tính gradient, thêm một tiếp tuyến vào mô hình.

## 3. Hợp hàm: Khi nào $h(g(x))$ lồi

Quy tắc hợp hàm là quy tắc đòi hỏi sự chặt chẽ nhất, và cũng là nơi dễ mắc sai lầm nhất nếu áp dụng cơ học. Để tìm ra quy tắc này, ta xét trường hợp một biến với $h$ và $g$ khả vi hai lần trên toàn $\mathbb{R}$. Đạo hàm bậc hai của hàm hợp $f = h \circ g$ là:

$$
f''(x) = h''(g(x))\, g'(x)^2 + h'(g(x))\, g''(x).
$$

Số hạng đầu tiên luôn không âm khi $h$ lồi (do $g'(x)^2 \ge 0$). Số hạng thứ hai là tích của **độ dốc của $h$** và **độ cong của $g$**. Muốn số hạng này không âm, độ dốc và độ cong phải cùng dấu với nhau. Từ đó ta suy ra bốn quy tắc bảo toàn:

| $h$ | Chiều đơn điệu của $h$ | $g$ | Kết luận về $f = h \circ g$ |
| --- | --- | --- | --- |
| lồi | không giảm | lồi | lồi |
| lồi | không tăng | lõm | lồi |
| lõm | không giảm | lõm | lõm |
| lõm | không tăng | lồi | lõm |

Dòng đầu tiên là quy tắc được sử dụng thường xuyên nhất trong thực tế. Nó cho thấy ngay $e^{g(x)}$ lồi khi $g$ lồi, và $g(x)^p$ lồi khi $g$ lồi, không âm và $p \ge 1$. Dòng thứ hai giải thích vì sao $1/g(x)$ lồi và $-\log g(x)$ lồi khi $g$ lõm và nhận giá trị dương. Nhờ đó, hàm rào chắn logarit $-\sum_i \log(b_i - a_i^T x)$ lồi trên miền khả thi $a_i^T x < b_i$. Dòng thứ ba cho thấy $\log g(x)$ là hàm lõm khi $g$ lõm và nhận giá trị dương.

**Vì sao không thể bỏ điều kiện đơn điệu**: Xét hàm $h(u) = u^2$, đây là hàm lồi nhưng không đơn điệu trên $\mathbb{R}$, và hàm $g(x) = x^2 - 1$ lồi. Khi đó hàm hợp $(x^2 - 1)^2$ là hàm giếng đôi với $f''(0) = -4 < 0$, hoàn toàn không lồi. Tương tự, nếu lấy $h(u) = e^u$ lồi và tăng, nhưng chọn $g(x) = -x^2$ là hàm lõm, thì hàm hợp $e^{-x^2}$ là đường cong hình chuông Gauss, có độ cong úp xuống ở vùng đỉnh.

**Đơn điệu phải hiểu cho mở rộng giá trị**: Khi hàm $h$ không xác định trên toàn bộ $\mathbb{R}$, điều kiện "$h$ không giảm" bắt buộc phải thỏa mãn đối với hàm mở rộng giá trị $\tilde h$ (hàm được gán bằng $+\infty$ ngoài miền xác định của hàm lồi $h$). Điều này đòi hỏi miền xác định của $h$ phải kéo dài vô hạn về phía âm. Hàm $u^{3/2}$ trên $\mathbb{R}_+$ lồi và tăng trên miền của nó, nhưng $\tilde h(-1) = \infty > \tilde h(1) = 1$, nên nó không thỏa điều kiện đơn điệu toàn cục. Hợp nó với $g(x) = x^2 - 1$ cho hàm xác định trên $|x| \ge 1$, một miền gồm hai khoảng rời nhau $(-\infty, -1] \cup [1, \infty)$, do miền xác định không lồi nên hàm hợp không thể là hàm lồi.

<CompositionLab />

Một lưu ý quan trọng: Xét tình huống $h(u) = u^2$ và $g(x) = |x|$. Không quy tắc nào ở bảng trên áp dụng được vì $u^2$ không đơn điệu trên $\mathbb{R}$, tuy nhiên hàm hợp $|x|^2 = x^2$ vẫn là một hàm lồi. Bốn quy tắc trong bảng là **điều kiện đủ**. Khi giả thiết không thỏa mãn, ta chưa thể vội kết luận mà phải dùng công cụ định nghĩa hoặc giải tích trực tiếp.

**Hợp với hàm nhiều biến**: Quy tắc mở rộng tự nhiên cho hàm hợp $f(x) = h(g_1(x), \dots, g_k(x))$: Hàm $f$ lồi nếu $h$ lồi, không giảm theo từng đối số, và mọi hàm thành phần $g_i$ đều lồi. Chẳng hạn hàm $\log \sum_{i=1}^k e^{g_i(x)}$ lồi khi mọi $g_i$ lồi, bởi vì hàm log-sum-exp lồi và đồng biến theo từng đối số.

## 4. Cực tiểu hóa theo một phần biến

Phép lấy max của các hàm lồi luôn bảo toàn tính lồi, trong khi phép lấy min nói chung sẽ phá vỡ nó. Tuy nhiên, tồn tại một dạng cực tiểu hóa từng phần đặc biệt vẫn giữ nguyên tính lồi:

> Nếu hàm $f(x, y)$ lồi **đồng thời** theo cặp biến $(x, y)$ và tập $C$ là một tập lồi khác rỗng, thì hàm cực tiểu hóa $g(x) = \inf_{y \in C} f(x, y)$ là một hàm lồi theo $x$, với giả thiết $g(x) > -\infty$.

Về mặt hình học, epigraph của hàm $g$ chính là hình chiếu của epigraph của hàm $f$ lên không gian tọa độ $(x, t)$, mà hình chiếu của một tập lồi luôn là một tập lồi. Hãy tưởng tượng một cái bát parabol trong không gian $(x, y, t)$: Hình chiếu của nó xuống mặt phẳng $(x, t)$ vẫn là một đường cong dạng cái bát hướng lên.

Cần nhấn mạnh rằng điều kiện lồi "đồng thời" là then chốt. Xét hàm $f(x, y) = y^2 - xy$, hàm này lồi theo $y$ với mỗi $x$ cố định, và tuyến tính theo $x$ với mỗi $y$ cố định. Tuy nhiên, ma trận Hessian $\begin{bmatrix} 0 & -1 \\ -1 & 2 \end{bmatrix}$ có định thức bằng $-1 < 0$, nên $f$ không lồi đồng thời theo $(x, y)$. Khi giải bài toán cực tiểu hóa theo $y$ tại điểm dừng $y = x/2$, ta thu được $g(x) = -x^2/4$, đây lại là một hàm **lõm**.

Ba ví dụ ứng dụng quen thuộc:

- **Khoảng cách tới một tập lồi**: Hàm khoảng cách $\operatorname{dist}(x, S) = \inf_{y \in S} \|x - y\|$ là hàm lồi, bởi vì khoảng cách $\|x - y\|$ lồi đồng thời theo $(x, y)$ và tập $S$ lồi. Đối với tập $S$ không lồi, tính chất này bị phá vỡ: Khoảng cách tới tập rời rạc $\{-1, 1\}$ bằng 1 tại $x = 0$, nhưng bằng 0 tại $x = \pm 1$.
- **Phần bù Schur**: Cực tiểu hóa dạng toàn phương lồi $x^T A x + 2x^T B y + y^T C y$ theo biến $y$ cho biểu thức $x^T (A - BC^{-1}B^T) x$ khi $C \succ 0$, do đó ma trận phần bù Schur $A - BC^{-1}B^T$ luôn nửa xác định dương. Lập luận giải tích tối ưu này chứng minh một chiều của tiêu chuẩn phần bù Schur một cách trực tiếp mà không cần dùng đến các phép biến đổi ma trận khối phức tạp.
- **Hàm mất mát Huber**: Cực tiểu hóa theo biến phụ $s$ của hàm lồi đồng thời $\tfrac12 (r - s)^2 + |s|$ cho:

$$
\phi(r) = \min_s \Big( \tfrac12 (r - s)^2 + |s| \Big) = \begin{cases} \tfrac12 r^2 & |r| \le 1, \\ |r| - \tfrac12 & |r| > 1. \end{cases}
$$

Đây là hàm phạt Huber nổi tiếng trong hồi quy bền vững: Phạt bình phương với sai số nhỏ và phạt tuyến tính với sai số lớn, nhờ đó các điểm dị biệt (outlier) không làm lệch nghiệm tối ưu. Ta khẳng định ngay hàm Huber lồi mà không cần khảo sát đạo hàm trên từng nhánh. Cách hiểu biến phụ $s$ cũng rất trực quan: Biến $s$ là phần sai số được "tha" cho mức phạt tuyến tính nhẹ hơn, còn phần còn lại $r - s$ chịu mức phạt bình phương. Kiểm tra bằng số: Tại $r = 3$, giá trị nhỏ nhất bằng $2.5$, đạt được tại $s = 2$.

## 5. Phối cảnh của hàm

Với hàm số $f : \mathbb{R}^n \to \mathbb{R}$, **phép phối cảnh** của $f$ là hàm hai biến $g(x, t) = t\, f(x/t)$ xác định trên miền $t > 0$. Nếu $f$ lồi thì hàm phối cảnh $g$ cũng là hàm lồi. Để chứng minh định lý này, ta sử dụng epigraph và phép phối cảnh của tập hợp: Ta có $(x, t, s) \in \operatorname{epi} g$ khi và chỉ khi $(x/t, s/t) \in \operatorname{epi} f$, do đó epigraph của $g$ chính là ảnh ngược của epigraph của $f$ qua phép phối cảnh tập lồi.

Hai ứng dụng tiêu biểu làm nổi bật sức mạnh của phép toán phối cảnh:

- Phối cảnh của hàm toàn phương $x^T x$ là $x^T x / t$, dạng tổng quát hóa nhiều chiều của hàm $x^2/y$.
- Phối cảnh của hàm $-\log x$ là $t\log(t/x)$, đại lượng này được gọi là **entropy tương đối** (relative entropy), lồi đồng thời theo cặp biến $(x, t)$ trên miền $x > 0, t > 0$. Lấy tổng theo từng tọa độ, độ phân kỳ Kullback–Leibler (KL divergence) giữa hai phân phối xác suất rời rạc:

$$
D_{\mathrm{kl}}(p, q) = \sum_{i=1}^n p_i \log\frac{p_i}{q_i} = p_1 \log\frac{p_1}{q_1} + p_2 \log\frac{p_2}{q_2} + \dots + p_n \log\frac{p_n}{q_n}
$$

là một hàm lồi **đồng thời** theo cặp $(p, q)$. Chẳng hạn với $p_1 = (0.7, 0.3)$, $q_1 = (0.4, 0.6)$ và $p_2 = (0.2, 0.8)$, $q_2 = (0.5, 0.5)$, trung bình hai giá trị KL xấp xỉ $0.188$, trong khi tại cặp trung bình $(\bar p, \bar q)$ có $\bar p = \bar q = (0.45, 0.55)$ thì KL bằng 0, hoàn toàn phù hợp với tính lồi.

## 6. Những phép toán làm mất tính lồi

Bảng dưới gom những phép toán trông vô hại nhưng không giữ tính lồi, mỗi phép kèm một phản ví dụ đã kiểm tra.

| Phép toán | Phản ví dụ | Điều xảy ra |
| --- | --- | --- |
| Hiệu $f_1 - f_2$ | $x^2 - 2x^2 = -x^2$ | lõm |
| Tích $f_1 f_2$ | $x \cdot x^2 = x^3$ | tại $-0.5$, đồ thị cao hơn dây cung nối $-1$ và $0$ |
| Min theo từng điểm | $\min\{x^2,\ (x-2)^2\}$ | bằng 1 tại $x = 1$, cao hơn dây cung nối 0 và 2 |
| Hợp hàm khi $h$ không đơn điệu | $(x^2 - 1)^2$ | $f''(0) = -4$ |
| Lồi theo từng biến riêng rẽ | $f(x, y) = xy$ | trung điểm của $(1, -1)$ và $(-1, 1)$ cho 0, trung bình hai giá trị là $-1$ |
| Cực tiểu theo một biến khi không lồi đồng thời | $\inf_y (y^2 - xy) = -x^2/4$ | lõm |

Dòng "lồi theo từng biến riêng rẽ" đáng để tâm nhất. Một hàm có thể lồi theo $x$ khi giữ $y$ cố định, lồi theo $y$ khi giữ $x$ cố định, mà vẫn không lồi theo cặp $(x, y)$. Các mô hình học máy có tích của hai nhóm tham số, như phân tích ma trận thành tích hai ma trận hay mạng nơ-ron hai tầng, đều rơi vào tình huống này. Chủ đề cuối của chương sẽ trở lại với nó.

## 7. Đọc một hàm mất mát từ trong ra ngoài

Ghép các quy tắc lại, ta có một quy trình kiểm tra tính lồi chỉ bằng cách đọc biểu thức. Các thư viện tối ưu như CVXPY cài đặt đúng tinh thần này dưới tên **lập trình lồi có kỷ luật** (disciplined convex programming): Mỗi biểu thức được phân tích thành cây, và tính lồi được suy ra từ lá lên gốc bằng các quy tắc vừa học.

::: example Đọc hàm mất mát của hồi quy logistic có điều chuẩn
Xét hàm mất mát sau, với $\lambda \ge 0$:

$$
L(w) = \frac1m \sum_{i=1}^m \log\big(1 + e^{-y_i x_i^T w}\big) + \lambda \|w\|_1 .
$$

1. $w \mapsto -y_i x_i^T w$ là hàm tuyến tính của $w$, vì $x_i, y_i$ là dữ liệu cố định.
2. Softplus $u \mapsto \log(1 + e^u)$ lồi. Hợp với một hàm tuyến tính, $\log(1 + e^{-y_i x_i^T w})$ lồi theo $w$.
3. Trung bình của $m$ hàm lồi với trọng số $1/m \ge 0$ là hàm lồi.
4. $\|w\|_1$ là một chuẩn nên lồi, và nhân với $\lambda \ge 0$ vẫn lồi.
5. Tổng của hai hàm lồi là hàm lồi.

Kết luận: Hàm mất mát $L$ lồi theo $w$. Ta không cần tính một đạo hàm nào, và lập luận vẫn đúng dù $\|w\|_1$ không khả vi.
:::

## 8. Những câu hỏi để đào sâu

**Câu 1.** Tổng của một hàm lồi và một hàm lõm có thể là gì?

<details><summary>Xem lời giải thích</summary>

Có thể là bất cứ thứ gì. $x^2 + (-x^2) = 0$ là affine. $x^2 + (-2x^2) = -x^2$ là lõm. $2x^2 + (-x^2) = x^2$ là lồi. Còn $x^4 + (-x^2)$ không lồi cũng không lõm: Đạo hàm bậc hai $12x^2 - 2$ âm gần gốc và dương khi $|x|$ lớn. Một trường hợp đặc biệt luôn an toàn là khi hàm lõm thật ra là affine, vì hàm affine vừa lồi vừa lõm.

</details>

**Câu 2.** $\lambda_{\max}(X)$ lồi theo ma trận đối xứng $X$. Còn trị riêng nhỏ nhất $\lambda_{\min}(X)$ thì sao?

<details><summary>Xem lời giải thích</summary>

$\lambda_{\min}(X) = \inf_{\|y\|_2 = 1} y^T X y$ là infimum của một họ hàm tuyến tính theo $X$, nên **lõm**. Quy tắc "supremum của các hàm lồi là lồi" có bản sao "infimum của các hàm lõm là lõm". Ví dụ với hai ma trận ở mục 2: Ta có $\lambda_{\min}$ của $\operatorname{diag}(1, 0)$ và $\operatorname{diag}(0, 1)$ đều bằng 0, còn của trung bình $\tfrac12 I$ bằng $0.5 \ge 0$, đúng chiều lõm. Hệ quả: Điều kiện $\lambda_{\min}(X) \ge \alpha$ xác định một tập lồi, vì đó là tập mức trên của một hàm lõm.

</details>

**Câu 3.** Quy tắc cực tiểu hóa từng phần đòi $f$ lồi đồng thời. Trong phương pháp tối ưu luân phiên, người ta lần lượt cực tiểu theo $x$ rồi theo $y$, mỗi bước là một bài toán lồi. Điều này có bảo đảm tìm được cực tiểu toàn cục không?

<details><summary>Xem lời giải thích</summary>

Không, nếu $f$ chỉ lồi theo từng khối biến mà không lồi đồng thời. Mỗi bước giải đúng một bài toán lồi, nên $f$ không tăng, nhưng dãy lặp có thể dừng tại một điểm mà thay đổi riêng $x$ hay riêng $y$ đều không làm $f$ giảm, trong khi thay đổi đồng thời cả hai thì làm được. Với $f(x, y) = xy$ trên hình vuông $[-1, 1]^2$, điểm $(0, 0)$ là một ví dụ. Giữ $y = 0$ thì mọi $x$ cho cùng giá trị 0, giữ $x = 0$ thì mọi $y$ cũng cho giá trị 0, nên gốc đã tối ưu theo từng khối và một thuật toán luân phiên có thể đứng yên ở đó mãi. Trong khi đó, giá trị nhỏ nhất $-1$ đạt tại $(1, -1)$, và đi tới đó cần thay đổi cả hai biến cùng lúc.

</details>

**Câu 4.** Vì sao hàm mất mát hinge trung bình $\frac1m\sum_i \max\{0,\ 1 - y_i x_i^T w\}$ lồi, nhưng hàm "đếm số điểm phân loại sai" $\frac1m \sum_i \mathbf{1}[y_i x_i^T w \le 0]$ thì không?

<details><summary>Xem lời giải thích</summary>

Hinge là max của hai hàm affine theo $w$, nên lồi, và trung bình của các hàm lồi là lồi. Hàm đếm sai dùng hàm bậc thang $\mathbf{1}[u \le 0]$, không lồi: Với $u = -1$ và $u = 1$, hàm bằng 1 và 0, trung điểm $u = 0$ cho giá trị 1, lớn hơn trung bình $0.5$. Đó là lý do người ta tối ưu hinge hay mất mát logistic thay cho tỉ lệ lỗi: Chúng là những **cận trên lồi** của hàm đếm sai. Với $u = y\, x^T w$, ta có $\max\{0, 1 - u\} \ge \mathbf{1}[u \le 0]$ với mọi $u$.

</details>

## 9. Bài tập tự luyện

::: exercise 1. Đọc tính lồi bằng quy tắc
Dùng các quy tắc của trang này để chứng minh những hàm sau lồi trên miền đã cho, ghi rõ quy tắc ở mỗi bước. (a) $\|Ax - b\|_2^2 + \lambda\|x\|_1$ với $\lambda \ge 0$. (b) $\max_i |a_i^T x - b_i|$. (c) $-\log(1 - \|x\|_2^2)$ trên $\|x\|_2 < 1$. (d) $\log\big(e^{x_1} + e^{x_2} + e^{-x_1 - x_2}\big)$.
:::

::: solution
(a) $\|\cdot\|_2^2$ lồi, hợp với ánh xạ affine $x \mapsto Ax - b$ nên lồi. $\|x\|_1$ là chuẩn nên lồi, nhân $\lambda \ge 0$ vẫn lồi, và tổng hai hàm lồi là lồi. (b) Mỗi $|a_i^T x - b_i|$ là trị tuyệt đối hợp với hàm affine nên lồi, và max của các hàm lồi là lồi. (c) $g(x) = 1 - \|x\|_2^2$ lõm, dương trên miền đã cho. Hàm $h(u) = -\log u$ lồi và mở rộng giá trị của nó không tăng (bằng $+\infty$ khi $u \le 0$). Quy tắc thứ hai của bảng cho $h(g(x))$ lồi. (d) Log-sum-exp lồi, hợp với ánh xạ tuyến tính $x \mapsto (x_1,\ x_2,\ -x_1 - x_2)$ nên lồi.
:::

::: exercise 2. Khoảng cách tới một đoạn
Cho $S = [0, 1] \subset \mathbb{R}$. (a) Viết $\operatorname{dist}(x, S)$ thành max của ba hàm affine và suy ra nó lồi. (b) Đối chiếu với quy tắc cực tiểu hóa từng phần. (c) Vì sao $\operatorname{dist}(x, \{0, 1\})$, khoảng cách tới hai đầu mút, không lồi?
:::

::: solution
(a) Nếu $x < 0$, khoảng cách là $-x$. Nếu $0 \le x \le 1$, khoảng cách là 0. Nếu $x > 1$, khoảng cách là $x - 1$. Ba trường hợp gộp thành $\operatorname{dist}(x, S) = \max\{0,\ -x,\ x - 1\}$, max của ba hàm affine, nên lồi. (b) $|x - y|$ lồi đồng thời theo $(x, y)$ và $S$ lồi, nên $\inf_{y \in S}|x - y|$ lồi theo quy tắc ở mục 4, khớp với câu (a). (c) Tập $\{0, 1\}$ không lồi. Tại $x = 0.5$ khoảng cách bằng $0.5$, trong khi tại $x = 0$ và $x = 1$ khoảng cách bằng 0, nên đồ thị nằm trên dây cung.
:::

::: exercise 3. Huber với ngưỡng tùy ý
Với $\delta > 0$, tính $\phi_\delta(r) = \min_s \big(\tfrac12 (r - s)^2 + \delta |s|\big)$ và chứng minh $\phi_\delta$ lồi mà không dùng công thức tường minh. Với $\delta = 1$, kiểm tra lại giá trị tại $r = 0.5$ và $r = 3$.
:::

::: solution
Hàm $\tfrac12 (r - s)^2 + \delta|s|$ lồi đồng thời theo $(r, s)$: Số hạng đầu là bình phương của hàm tuyến tính $r - s$, số hạng sau là $\delta$ lần trị tuyệt đối. Theo quy tắc cực tiểu hóa từng phần, $\phi_\delta$ lồi. Để tính, cực tiểu theo $s$: Nếu $|r| \le \delta$ thì $s = 0$ và $\phi_\delta(r) = \tfrac12 r^2$. Nếu $|r| > \delta$ thì $s = r - \delta\operatorname{sign}(r)$, phần dư $r - s$ có độ lớn $\delta$, và $\phi_\delta(r) = \tfrac12\delta^2 + \delta(|r| - \delta) = \delta|r| - \tfrac12\delta^2$. Với $\delta = 1$: Ta có $\phi(0.5) = 0.125$ và $\phi(3) = 3 - 0.5 = 2.5$, khớp với giá trị cực tiểu tính bằng số.
:::

## Tóm tắt

Tính lồi được giữ bởi tổng có trọng số không âm, hợp với ánh xạ affine, max và supremum theo từng điểm, cực tiểu hóa theo một phần biến của một hàm lồi đồng thời, và phép phối cảnh. Mọi hàm lồi là bao trên của các hàm affine nằm dưới nó, nên viết một hàm thành supremum của các hàm affine là một cách chứng minh tính lồi rất hiệu quả.

Quy tắc hợp hàm đòi độ dốc của hàm ngoài và độ cong của hàm trong phải "cùng chiều", và chiều đơn điệu phải hiểu cho mở rộng giá trị. Các quy tắc chỉ là điều kiện đủ. Hiệu, tích, min, hợp hàm thiếu đơn điệu và tính lồi theo từng biến riêng rẽ đều có thể phá tính lồi. Đọc một hàm mất mát từ trong ra ngoài bằng các quy tắc này cho phép kết luận nó lồi mà không cần tính đạo hàm.

## Tài liệu tham khảo

- Stephen Boyd, Lieven Vandenberghe, *Convex Optimization*, Cambridge University Press.
