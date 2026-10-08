---
course: toan-cho-ai
lecture: bai-01-nhap-mon-toi-uu
topic: phep-toan-giu-tinh-loi-cua-ham
section: topic
title: "Các phép toán giữ tính lồi của hàm"
description: "Bộ quy tắc lắp ghép hàm lồi: tổng có trọng số không âm, hợp với ánh xạ affine, max và supremum theo từng điểm, hàm lồi như bao trên của các hàm affine, quy tắc hợp hàm với điều kiện đơn điệu của mở rộng giá trị, cực tiểu hóa theo một phần biến và hàm Huber, phối cảnh của hàm, cùng những phép toán làm mất tính lồi."
---

Chủ đề trước cho ta một "bảng" các hàm lồi cơ bản. Chủ đề này cho các "quy tắc" lắp ghép chúng, giống như quy tắc tổng, tích, hợp của đạo hàm. Nhờ những quy tắc này, để biết hàm mất mát $\frac1m\sum_i \log\big(1 + e^{-y_i x_i^T w}\big) + \lambda\|w\|_2^2$ có lồi theo $w$ hay không, ta không cần tính Hessian: chỉ cần đọc biểu thức từ trong ra ngoài và kiểm tra mỗi bước dùng một quy tắc hợp lệ.

Nhưng khác với đạo hàm, không phải phép toán nào cũng giữ được tính lồi. Tích, thương, hiệu, min và phần lớn các phép hợp hàm đều có thể phá nó. Vì vậy học các quy tắc ở đây cũng là học chỗ nào phải dừng lại kiểm tra giả thiết. Nội dung bám theo §3.2 của sách.

## 1. Hai quy tắc nền: tổng không âm và hợp với ánh xạ affine

**Tổng có trọng số không âm.** Nếu $f_1, \dots, f_m$ lồi và $w_1, \dots, w_m \ge 0$ thì $w_1 f_1 + \cdots + w_m f_m$ lồi. Nói cách khác, tập các hàm lồi là một **nón lồi**, đúng khái niệm ở phần tập lồi. Quy tắc mở rộng sang tổng vô hạn và tích phân: nếu $f(x, y)$ lồi theo $x$ với mỗi $y$, và $w(y) \ge 0$, thì $\int w(y) f(x, y)\,dy$ lồi theo $x$. Đó là lý do **kỳ vọng** của một hàm mất mát lồi theo tham số, lấy trên phân phối của dữ liệu, vẫn lồi theo tham số.

Điều kiện "không âm" là thật sự cần: $x^2 - 2x^2 = -x^2$ là hiệu của hai hàm lồi nhưng lõm.

**Hợp với ánh xạ affine.** Nếu $f$ lồi thì $g(x) = f(Ax + b)$ lồi. Quy tắc này giải thích vì sao gần như mọi hàm mất mát trong học máy tuyến tính đều lồi theo tham số. Dữ liệu $x_i$ cố định, nên $w \mapsto x_i^T w$ là ánh xạ tuyến tính, và ta chỉ cần hàm bên ngoài lồi:

- $\|Aw - b\|_2^2$ là bình phương chuẩn hợp với một ánh xạ affine.
- $\log\big(1 + e^{-y_i x_i^T w}\big)$ là hàm softplus, lồi ở chủ đề điều kiện bậc nhất, hợp với ánh xạ tuyến tính $w \mapsto -y_i x_i^T w$.
- $\log \sum_k e^{a_k^T w + b_k}$ là log-sum-exp hợp với một ánh xạ affine.

Cộng các số hạng của từng điểm dữ liệu với trọng số $1/m$ và cộng thêm một chuẩn để điều chuẩn, ta được hàm mất mát của hồi quy tuyến tính, hồi quy logistic, hồi quy softmax, tất cả đều lồi theo $w$.

## 2. Max, supremum, và hàm lồi như bao trên của các hàm affine

**Max theo từng điểm.** Nếu $f_1, \dots, f_m$ lồi thì $f(x) = \max\{f_1(x), \dots, f_m(x)\}$ lồi. Cách thấy nhanh nhất là qua epigraph: điểm $(x, t)$ nằm trên đồ thị của max khi và chỉ khi nó nằm trên đồ thị của từng $f_i$, nên $\operatorname{epi} f = \bigcap_i \operatorname{epi} f_i$, giao của các tập lồi.

Lập luận bằng epigraph không quan tâm có bao nhiêu hàm, nên quy tắc mở rộng sang **supremum** của một họ vô hạn: nếu $f(x, y)$ lồi theo $x$ với mỗi $y \in \mathcal{A}$ thì $g(x) = \sup_{y \in \mathcal{A}} f(x, y)$ lồi theo $x$. Sách đưa ra một loạt ví dụ chỉ cần quy tắc này:

- **Hàm tuyến tính từng khúc** $\max_i (a_i^T x + b_i)$ (Ví dụ 3.5). Hàm mất mát hinge $\max\{0,\ 1 - y\, x^T w\}$ là trường hợp hai khúc.
- **Tổng $r$ thành phần lớn nhất** của $x$ (Ví dụ 3.6), là max của mọi tổng $r$ thành phần khác nhau. Với $x = (3, -1, 4, 1, 5)$ và $r = 2$, đó là max của $\binom{5}{2} = 10$ hàm tuyến tính, bằng $5 + 4 = 9$.
- **Hàm tựa** $S_C(x) = \sup_{y \in C} x^T y$ của một tập $C$ (Ví dụ 3.7), là supremum của các hàm tuyến tính, nên lồi dù $C$ có lồi hay không.
- **Trị riêng lớn nhất** $\lambda_{\max}(X) = \sup_{\|y\|_2 = 1} y^T X y$ của ma trận đối xứng (Ví dụ 3.10). Mỗi $y^T X y$ tuyến tính theo $X$, nên $\lambda_{\max}$ lồi. Thử bằng số: $\lambda_{\max}$ của $\operatorname{diag}(1, 0)$ và của $\operatorname{diag}(0, 1)$ đều bằng 1, còn của trung bình $\tfrac12 I$ chỉ bằng $0.5$.

**Mọi hàm lồi đều là supremum của các hàm affine.** Ví dụ trên gợi ý một cách chứng minh tính lồi: viết hàm thành supremum của một họ hàm affine. Sách chỉ ra rằng, ngoài một điều kiện kỹ thuật, cách này luôn làm được. Với $f$ lồi và $\operatorname{dom} f = \mathbb{R}^n$,

$$
f(x) = \sup\{\, g(x) : g \text{ affine},\ g(z) \le f(z) \text{ với mọi } z \,\}.
$$

Lý do: tại mỗi $x$, epigraph lồi có một siêu phẳng tựa tại $(x, f(x))$, và siêu phẳng đó không thể thẳng đứng, nên nó là đồ thị của một hàm affine nằm dưới $f$ và chạm $f$ tại $x$. Khi $f$ khả vi, đó chính là tiếp tuyến. Hàm lồi là **bao trên** của các tiếp tuyến của nó.

<EnvelopeLab />

Mô phỏng cho thấy max của $k$ tiếp tuyến tiến dần tới hàm khi $k$ tăng. Với $x^2$ và các tiếp điểm cách nhau $h$, hai tiếp tuyến kề nhau cắt nhau ở giữa, và sai số lớn nhất bằng $h^2/4$. Tăng gấp đôi số tiếp tuyến thì sai số giảm khoảng bốn lần. Mô hình "max các tiếp tuyến" luôn nằm **dưới** hàm thật, và đây là ý tưởng của các phương pháp mặt phẳng cắt: mỗi lần tính gradient, thêm một tiếp tuyến vào mô hình.

## 3. Hợp hàm: khi nào $h(g(x))$ lồi

Quy tắc hợp hàm là quy tắc khó nhất, và cũng hay bị dùng sai nhất. Để tìm ra nó, sách xét trường hợp một biến, $h$ và $g$ khả vi hai lần trên toàn $\mathbb{R}$. Đạo hàm bậc hai của $f = h \circ g$ là

$$
f''(x) = h''(g(x))\, g'(x)^2 + h'(g(x))\, g''(x).
$$

Số hạng đầu không âm khi $h$ lồi. Số hạng sau là tích của **độ dốc của $h$** và **độ cong của $g$**. Muốn nó không âm, độ dốc và độ cong phải cùng dấu. Từ đó ra bốn quy tắc:

| $h$ | Chiều đơn điệu của $h$ | $g$ | Kết luận về $f = h \circ g$ |
| --- | --- | --- | --- |
| lồi | không giảm | lồi | lồi |
| lồi | không tăng | lõm | lồi |
| lõm | không giảm | lõm | lõm |
| lõm | không tăng | lồi | lõm |

Dòng đầu được dùng nhiều nhất. Nó cho ngay $e^{g(x)}$ lồi khi $g$ lồi, và $g(x)^p$ lồi khi $g$ lồi, không âm và $p \ge 1$. Dòng thứ hai cho $1/g(x)$ lồi và $-\log g(x)$ lồi khi $g$ lõm và dương, nên hàm rào chắn logarit $-\sum_i \log(b_i - a_i^T x)$ lồi trên miền $a_i^T x < b_i$. Dòng thứ ba cho $\log g(x)$ lõm khi $g$ lõm và dương (Ví dụ 3.13).

**Vì sao không bỏ được điều kiện đơn điệu.** Lấy $h(u) = u^2$, lồi nhưng không đơn điệu, và $g(x) = x^2 - 1$, lồi. Hàm hợp $(x^2 - 1)^2$ là hàm giếng đôi đã gặp ở chủ đề điều kiện bậc hai, có $f''(0) = -4 < 0$. Lấy $h = \exp$, lồi và tăng, nhưng $g(x) = -x^2$ lõm thay vì lồi: hàm hợp $e^{-x^2}$ là đường chuông, cong xuống ở giữa.

**Đơn điệu phải hiểu cho mở rộng giá trị.** Khi $h$ không xác định trên toàn $\mathbb{R}$, điều kiện "$h$ không giảm" phải áp dụng cho mở rộng giá trị $\tilde h$, hàm bằng $+\infty$ ngoài miền xác định của hàm lồi $h$. Điều này buộc miền của $h$ phải kéo dài vô tận về phía âm. Hàm $u^{3/2}$ trên $\mathbb{R}_+$ lồi và tăng trên miền của nó, nhưng $\tilde h(-1) = \infty > \tilde h(1) = 1$, nên nó không thỏa điều kiện (Ví dụ 3.12). Hợp nó với $g(x) = x^2 - 1$ cho hàm xác định trên $|x| \ge 1$, một miền gồm hai mảnh rời nhau, nên không thể lồi. Ghi chú 3.3 của sách đưa một ví dụ cùng kiểu.

<CompositionLab />

Hãy để ý tình huống $h = u^2$ với $g = |x|$: không quy tắc nào áp dụng vì $u^2$ không đơn điệu, vậy mà $|x|^2 = x^2$ vẫn lồi. Bốn quy tắc là **điều kiện đủ**. Khi chúng im lặng, ta chưa kết luận được gì và phải dùng công cụ khác.

**Hợp với hàm nhiều biến.** Quy tắc mở rộng cho $f(x) = h(g_1(x), \dots, g_k(x))$: $f$ lồi nếu $h$ lồi, không giảm theo từng đối số, và mọi $g_i$ lồi. Chẳng hạn $\log \sum_i e^{g_i(x)}$ lồi khi mọi $g_i$ lồi, vì log-sum-exp lồi và tăng theo từng đối số (Ví dụ 3.14).

## 4. Cực tiểu hóa theo một phần biến

Max của các hàm lồi luôn lồi. Min thì nói chung không. Nhưng có một dạng cực tiểu hóa đặc biệt giữ được tính lồi:

> Nếu $f(x, y)$ lồi **đồng thời** theo $(x, y)$ và $C$ là tập lồi khác rỗng, thì $g(x) = \inf_{y \in C} f(x, y)$ lồi theo $x$, với điều kiện $g(x) > -\infty$.

Về hình học, epigraph của $g$ là hình chiếu của epigraph của $f$ lên các tọa độ $(x, t)$, và hình chiếu của một tập lồi là tập lồi. Hãy nhìn một cái bát trong không gian $(x, y, t)$ từ phía trục $y$: bóng của nó là một cái bát trong mặt phẳng $(x, t)$.

Chữ "đồng thời" là điều kiện cốt lõi. Hàm $f(x, y) = y^2 - xy$ lồi theo $y$ với mỗi $x$ cố định, và tuyến tính theo $x$ với mỗi $y$ cố định. Nhưng Hessian $\begin{bmatrix} 0 & -1 \\ -1 & 2 \end{bmatrix}$ có định thức $-1$, nên $f$ không lồi đồng thời. Cực tiểu theo $y$ đạt tại $y = x/2$ và cho $g(x) = -x^2/4$, một hàm **lõm**.

Ba ví dụ quen thuộc:

- **Khoảng cách tới một tập lồi** $\operatorname{dist}(x, S) = \inf_{y \in S} \|x - y\|$ lồi, vì $\|x - y\|$ lồi đồng thời theo $(x, y)$ (Ví dụ 3.16). Với tập không lồi thì không còn đúng: khoảng cách tới $\{-1, 1\}$ bằng 1 tại $x = 0$, nhưng bằng 0 tại $x = \pm 1$.
- **Phần bù Schur** (Ví dụ 3.15). Cực tiểu dạng toàn phương lồi $x^T A x + 2x^T B y + y^T C y$ theo $y$ cho $x^T (A - BC^{-1}B^T) x$ khi $C \succ 0$, nên ma trận $A - BC^{-1}B^T$ nửa xác định dương. Lập luận này chứng minh được một chiều của tiêu chuẩn phần bù Schur đã dùng ở chủ đề về epigraph, mà không cần một phép tính ma trận nào.
- **Hàm Huber.** Cực tiểu theo biến phụ $s$ của hàm lồi đồng thời $\tfrac12 (r - s)^2 + |s|$ cho

$$
\phi(r) = \min_s \Big( \tfrac12 (r - s)^2 + |s| \Big) = \begin{cases} \tfrac12 r^2 & |r| \le 1, \\ |r| - \tfrac12 & |r| > 1. \end{cases}
$$

Đây là hàm phạt Huber của hồi quy bền vững: phạt bình phương với sai số nhỏ và phạt tuyến tính với sai số lớn, nên một điểm dữ liệu ngoại lai không kéo nghiệm đi quá xa. Ta biết ngay nó lồi mà không cần xét hai nhánh. Cách đọc biến phụ $s$ cũng thú vị: $s$ là phần sai số được "tha" cho một mức phạt tuyến tính, còn phần còn lại $r - s$ bị phạt bình phương. Kiểm tra bằng số: tại $r = 3$, giá trị nhỏ nhất bằng $2.5$, đạt tại $s = 2$.

## 5. Phối cảnh của hàm

Với $f : \mathbb{R}^n \to \mathbb{R}$, **phối cảnh** của $f$ là hàm $g(x, t) = t\, f(x/t)$ với $t > 0$. Nếu $f$ lồi thì $g$ lồi (§3.2.6). Lời chứng minh của sách dùng epigraph và phép phối cảnh của tập ở chủ đề phối cảnh: $(x, t, s) \in \operatorname{epi} g$ khi và chỉ khi $(x/t, s/t) \in \operatorname{epi} f$, nên epigraph của $g$ là ảnh ngược của một tập lồi qua phép phối cảnh.

Hai ví dụ của sách cho thấy quy tắc này mạnh đến đâu. Phối cảnh của $x^T x$ là $x^T x / t$, tổng quát hóa của hàm $x^2/y$ (Ví dụ 3.18). Phối cảnh của $-\log x$ là $t\log(t/x)$, gọi là **entropy tương đối**, lồi đồng thời theo $(x, t)$ (Ví dụ 3.19). Cộng theo các thành phần, độ phân kỳ $D_{\mathrm{kl}}(p, q) = \sum_i p_i \log(p_i / q_i)$ lồi **đồng thời** theo cặp $(p, q)$. Với $p_1 = (0.7, 0.3)$, $q_1 = (0.4, 0.6)$, $p_2 = (0.2, 0.8)$, $q_2 = (0.5, 0.5)$, trung bình hai giá trị KL xấp xỉ $0.188$, còn cặp trung bình $(\bar p, \bar q)$ có $\bar p = \bar q = (0.45, 0.55)$ nên KL bằng 0, đúng chiều của tính lồi.

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

Ghép các quy tắc lại, ta có một quy trình kiểm tra tính lồi chỉ bằng cách đọc biểu thức. Các thư viện tối ưu như CVXPY cài đặt đúng tinh thần này dưới tên **lập trình lồi có kỷ luật** (disciplined convex programming): mỗi biểu thức được phân tích thành cây, và tính lồi được suy ra từ lá lên gốc bằng các quy tắc vừa học.

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

Kết luận: $L$ lồi theo $w$. Ta không cần tính một đạo hàm nào, và lập luận vẫn đúng dù $\|w\|_1$ không khả vi.
:::

## 8. Những câu hỏi để đào sâu

**Câu 1.** Tổng của một hàm lồi và một hàm lõm có thể là gì?

<details><summary>Xem lời giải thích</summary>

Có thể là bất cứ thứ gì. $x^2 + (-x^2) = 0$ là affine. $x^2 + (-2x^2) = -x^2$ là lõm. $2x^2 + (-x^2) = x^2$ là lồi. Còn $x^4 + (-x^2)$ không lồi cũng không lõm: đạo hàm bậc hai $12x^2 - 2$ âm gần gốc và dương khi $|x|$ lớn. Một trường hợp đặc biệt luôn an toàn là khi hàm lõm thật ra là affine, vì hàm affine vừa lồi vừa lõm.

</details>

**Câu 2.** $\lambda_{\max}(X)$ lồi theo ma trận đối xứng $X$. Còn trị riêng nhỏ nhất $\lambda_{\min}(X)$ thì sao?

<details><summary>Xem lời giải thích</summary>

$\lambda_{\min}(X) = \inf_{\|y\|_2 = 1} y^T X y$ là infimum của một họ hàm tuyến tính theo $X$, nên **lõm**. Quy tắc "supremum của các hàm lồi là lồi" có bản sao "infimum của các hàm lõm là lõm". Ví dụ với hai ma trận ở mục 2: $\lambda_{\min}$ của $\operatorname{diag}(1, 0)$ và $\operatorname{diag}(0, 1)$ đều bằng 0, còn của trung bình $\tfrac12 I$ bằng $0.5 \ge 0$, đúng chiều lõm. Hệ quả: điều kiện $\lambda_{\min}(X) \ge \alpha$ xác định một tập lồi, vì đó là tập mức trên của một hàm lõm.

</details>

**Câu 3.** Quy tắc cực tiểu hóa từng phần đòi $f$ lồi đồng thời. Trong phương pháp tối ưu luân phiên, người ta lần lượt cực tiểu theo $x$ rồi theo $y$, mỗi bước là một bài toán lồi. Điều này có bảo đảm tìm được cực tiểu toàn cục không?

<details><summary>Xem lời giải thích</summary>

Không, nếu $f$ chỉ lồi theo từng khối biến mà không lồi đồng thời. Mỗi bước giải đúng một bài toán lồi, nên $f$ không tăng, nhưng dãy lặp có thể dừng tại một điểm mà thay đổi riêng $x$ hay riêng $y$ đều không làm $f$ giảm, trong khi thay đổi đồng thời cả hai thì làm được. Với $f(x, y) = xy$ trên hình vuông $[-1, 1]^2$, điểm $(0, 0)$ là một ví dụ. Giữ $y = 0$ thì mọi $x$ cho cùng giá trị 0, giữ $x = 0$ thì mọi $y$ cũng cho giá trị 0, nên gốc đã tối ưu theo từng khối và một thuật toán luân phiên có thể đứng yên ở đó mãi. Trong khi đó, giá trị nhỏ nhất $-1$ đạt tại $(1, -1)$, và đi tới đó cần thay đổi cả hai biến cùng lúc.

</details>

**Câu 4.** Vì sao hàm mất mát hinge trung bình $\frac1m\sum_i \max\{0,\ 1 - y_i x_i^T w\}$ lồi, nhưng hàm "đếm số điểm phân loại sai" $\frac1m \sum_i \mathbf{1}[y_i x_i^T w \le 0]$ thì không?

<details><summary>Xem lời giải thích</summary>

Hinge là max của hai hàm affine theo $w$, nên lồi, và trung bình của các hàm lồi là lồi. Hàm đếm sai dùng hàm bậc thang $\mathbf{1}[u \le 0]$, không lồi: với $u = -1$ và $u = 1$, hàm bằng 1 và 0, trung điểm $u = 0$ cho giá trị 1, lớn hơn trung bình $0.5$. Đó là lý do người ta tối ưu hinge hay mất mát logistic thay cho tỉ lệ lỗi: chúng là những **cận trên lồi** của hàm đếm sai. Với $u = y\, x^T w$, ta có $\max\{0, 1 - u\} \ge \mathbf{1}[u \le 0]$ với mọi $u$.

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
Hàm $\tfrac12 (r - s)^2 + \delta|s|$ lồi đồng thời theo $(r, s)$: số hạng đầu là bình phương của hàm tuyến tính $r - s$, số hạng sau là $\delta$ lần trị tuyệt đối. Theo quy tắc cực tiểu hóa từng phần, $\phi_\delta$ lồi. Để tính, cực tiểu theo $s$: nếu $|r| \le \delta$ thì $s = 0$ và $\phi_\delta(r) = \tfrac12 r^2$. Nếu $|r| > \delta$ thì $s = r - \delta\operatorname{sign}(r)$, phần dư $r - s$ có độ lớn $\delta$, và $\phi_\delta(r) = \tfrac12\delta^2 + \delta(|r| - \delta) = \delta|r| - \tfrac12\delta^2$. Với $\delta = 1$: $\phi(0.5) = 0.125$ và $\phi(3) = 3 - 0.5 = 2.5$, khớp với giá trị cực tiểu tính bằng số.
:::

## Tóm tắt

Tính lồi được giữ bởi tổng có trọng số không âm, hợp với ánh xạ affine, max và supremum theo từng điểm, cực tiểu hóa theo một phần biến của một hàm lồi đồng thời, và phép phối cảnh. Mọi hàm lồi là bao trên của các hàm affine nằm dưới nó, nên viết một hàm thành supremum của các hàm affine là một cách chứng minh tính lồi rất hiệu quả.

Quy tắc hợp hàm đòi độ dốc của hàm ngoài và độ cong của hàm trong phải "cùng chiều", và chiều đơn điệu phải hiểu cho mở rộng giá trị. Các quy tắc chỉ là điều kiện đủ. Hiệu, tích, min, hợp hàm thiếu đơn điệu và tính lồi theo từng biến riêng rẽ đều có thể phá tính lồi. Đọc một hàm mất mát từ trong ra ngoài bằng các quy tắc này cho phép kết luận nó lồi mà không cần tính đạo hàm.

## Nguồn và đọc thêm

- S. Boyd, L. Vandenberghe, *Convex Optimization*, §3.2 (tr. 79–90): các Ví dụ 3.5–3.7, 3.10, 3.12–3.16, 3.18, 3.19, Ghi chú 3.3 và Hình 3.7.
- Hai mô phỏng, ví dụ hàm Huber như một bài cực tiểu hóa từng phần, phản ví dụ $y^2 - xy$ và bảng các phép toán làm mất tính lồi do người soạn bổ sung. Ví dụ đọc hàm mất mát logistic, các câu hỏi và bài tập cũng do người soạn viết. Mọi con số đã được tính lại bằng chương trình.
