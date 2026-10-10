---
course: toan-cho-ai
lecture: bai-01-nhap-mon-toi-uu
topic: tinh-loi-trong-mo-hinh-hoc-may
section: topic
title: "Nhận diện tính lồi trong mô hình học máy"
description: "Huấn luyện như ước lượng hợp lý cực đại và ba mô hình nhiễu ứng với bình phương tối thiểu, chuẩn ℓ1 và chuẩn ℓ∞, hồi quy logistic lồi theo tham số và hiện tượng không có nghiệm khi dữ liệu tách được, mạng nơ-ron không lồi vì đối xứng hoán vị, lồi theo từng khối và câu hỏi lồi theo biến nào, kèm một quy trình nhận diện tính lồi."
---

Chủ đề cuối của chương trả lời câu hỏi mà một người học AI quan tâm nhất: Những bài toán huấn luyện nào là bài toán lồi, và vì sao? Tất cả công cụ đã có sẵn. Ta biết các hàm lồi cơ bản, biết các quy tắc lắp ghép, biết rằng với bài toán lồi, mọi cực tiểu cục bộ là toàn cục. Việc còn lại là học cách **nhìn** một mô hình học máy bằng con mắt của tối ưu lồi.

Điểm mấu chốt nằm ở một câu hỏi tưởng như hiển nhiên: Lồi theo biến nào? Khi huấn luyện, dữ liệu là hằng số, còn tham số mới là biến. Một hàm mất mát có thể lồi theo tham số dù nó phi tuyến đến đâu theo dữ liệu, và ngược lại, một đổi biến khéo có thể biến bài toán không lồi thành lồi. Ta sẽ đi từ các mô hình tuyến tính, qua hồi quy logistic và mạng nơ-ron hai tầng, tới một quy trình nhận diện dùng được hằng ngày.

## 1. Huấn luyện là ước lượng hợp lý cực đại

Rất nhiều hàm mất mát trong học máy không được chọn tùy tiện, mà sinh ra từ một mô hình xác suất. Giả sử dữ liệu tuân theo một phân phối $p_\theta$ phụ thuộc tham số $\theta$. **Ước lượng hợp lý cực đại** (Maximum Likelihood Estimation - MLE) chọn $\theta$ làm cực đại log-likelihood $l(\theta) = \log p_\theta(\text{dữ liệu})$. Theo nguyên lý tối ưu, bài toán ước lượng này là bài toán lồi khi log-likelihood $l(\theta)$ là một hàm lõm theo tham số $\theta$ và tập các ràng buộc đặt lên $\theta$ là tập lồi.

Xét mô hình đo tuyến tính với $m$ quan sát: Phương trình $y_i = a_i^T x + v_i$ với $i = 1, \dots, m$, trong đó $x \in \mathbb{R}^n$ là vector tham số cần ước lượng và các thành phần nhiễu $v_i$ độc lập, cùng phân phối với hàm mật độ xác suất $p(v)$. Do tính độc lập, hàm hợp lý chung là tích các mật độ $\prod_{i=1}^m p(y_i - a_i^T x)$, dẫn đến log-likelihood có dạng tổng tường minh:

$$
l(x) = \sum_{i=1}^m \log p(y_i - a_i^T x) = \log p(y_1 - a_1^T x) + \log p(y_2 - a_2^T x) + \dots + \log p(y_m - a_m^T x).
$$

Nếu $\log p$ là một hàm lõm (tức mật độ $p$ là **log-lõm**), thì mỗi số hạng $\log p(y_i - a_i^T x)$ là phép hợp của hàm lõm với hàm affine theo $x$, do đó tổng $l(x)$ là hàm lõm và bài toán ước lượng trở thành bài toán lồi. Bài toán cực tiểu hàm mất mát tương đương là cực tiểu $-\log p$ áp lên từng phần dư $r_i = y_i - a_i^T x$. Xét ba trường hợp phân phối nhiễu kinh điển sau:

| Mô hình nhiễu | Mật độ $p(z)$ tỉ lệ với | Bài toán ước lượng tương đương |
| --- | --- | --- |
| Gauss | $e^{-z^2/2\sigma^2}$ | cực tiểu $\|Ax - y\|_2^2$, bình phương tối thiểu |
| Laplace | $e^{-\lvert z\rvert/a}$ | cực tiểu $\|Ax - y\|_1$ |
| Đều trên $[-a, a]$ | hằng số trên đoạn | tìm $x$ với $\|Ax - y\|_\infty \le a$ |

Ba cách khớp đường thẳng ở chủ đề về hai lớp bài toán kinh điển hóa ra là ba giả thiết khác nhau về nhiễu. Bảng này cũng giải thích vì sao chuẩn $\ell_1$ bền vững với điểm ngoại lai: Mật độ Laplace có đuôi dày hơn mật độ Gauss, tức coi phần dư lớn là chuyện có thể xảy ra, nên ước lượng tương ứng không cố bẻ cong nghiệm để giảm một phần dư lớn. Ngược lại, mọi hàm phạt lồi $\phi$ áp lên phần dư đều có thể đọc như ước lượng hợp lý cực đại với mật độ nhiễu tỉ lệ với $e^{-\phi(z)}$.

## 2. Hồi quy logistic: Phi tuyến theo dữ liệu, lồi theo tham số

Mô hình logistic dự đoán xác suất để nhãn bằng 1 là $p = \sigma(a^T u + b)$, với $\sigma(t) = 1/(1 + e^{-t})$. Hàm sigmoid uốn cong theo $u$, vậy mà bài toán ước lượng $(a, b)$ là bài toán lồi. Cách thấy nhanh nhất là đọc hàm mất mát từ trong ra ngoài như ở chủ đề các phép toán giữ tính lồi. Đặt $z_i = a^T u_i + b$, một hàm **affine** của tham số $(a, b)$. Log-likelihood là

$$
l(a, b) = \sum_{i:\, y_i = 1} \log \sigma(z_i) + \sum_{i:\, y_i = 0} \log\big(1 - \sigma(z_i)\big).
$$

Vì $\log\sigma(z) = -\log(1 + e^{-z})$ và $\log(1 - \sigma(z)) = -\log(1 + e^{z})$, mỗi số hạng là âm của hàm softplus, một hàm lõm, hợp với hàm affine $z_i$ của tham số. Do đó $l(a, b)$ là hàm lõm, và bài toán cực đại hóa nó (hoặc cực tiểu hóa âm log-likelihood) chính là một bài toán tối ưu lồi. Viết với nhãn $s_i = \pm 1$, ta cực tiểu hàm lồi

$$
L(a, b) = \frac1m \sum_{i=1}^m \log\big(1 + e^{-s_i (a^T u_i + b)}\big).
$$

Hessian của $L$ cũng có một dạng đẹp. Với $\tilde u_i = (u_i, 1)$ và $p_i = \sigma(z_i)$,

$$
\nabla^2 L = \frac1m \sum_{i=1}^m p_i (1 - p_i)\, \tilde u_i \tilde u_i^T \succeq 0 .
$$

Hệ số $p_i(1 - p_i)$ là phương sai của một biến Bernoulli với xác suất $p_i$, và mỗi số hạng là một ma trận nửa xác định dương hạng một. Đây là cùng một cấu trúc "Hessian là một phương sai" đã gặp với log-sum-exp.

<LogisticLab />

Với dữ liệu chồng lấn, mô phỏng cho thấy hàm mất mát là một cái bát duy nhất, với nghiệm $(a, b) \approx (1.188,\ -2.673)$ và giá trị nhỏ nhất xấp xỉ $0.528$. Không có thung lũng thứ hai nào, đúng như định lý cục bộ và toàn cục dự báo.

**Khi dữ liệu tách được, nghiệm biến mất.** Với tám điểm mà bốn điểm đầu có nhãn 0 và bốn điểm sau có nhãn 1, mọi ngưỡng giữa $u = 2$ và $u = 2.5$ đều phân loại đúng hết. Đi theo hướng $(a, b) = t\,(1, -2.25)$, ngưỡng $-b/a = 2.25$ giữ nguyên còn đường sigmoid dốc dần, và hàm mất mát giảm mãi: Xấp xỉ $0.344$ khi $t = 1$, $0.092$ khi $t = 4$, $0.0045$ khi $t = 16$, nhưng không bao giờ bằng 0. Bài toán lồi, có cận dưới bằng 0, mà không có nghiệm, đúng tình huống "gradient không bao giờ bằng 0" ở chủ đề điều kiện bậc nhất. Thêm điều chuẩn $\tfrac{\lambda}{2}\|(a, b)\|_2^2$ với $\lambda > 0$ làm hàm lồi mạnh, và nghiệm xuất hiện trở lại: Với $\lambda = 0.05$, nghiệm là $(a, b) \approx (0.954,\ -1.705)$.

## 3. Mạng nơ-ron hai tầng không lồi

Giờ xét một mạng nơ-ron nhỏ nhất có thể: Một đầu vào vô hướng, hai nơ-ron ẩn dùng hàm ReLU, không có hệ số tự do:

$$
f_\theta(x) = v_1 \max\{0,\ w_1 x\} + v_2 \max\{0,\ w_2 x\}, \qquad \theta = (w_1, v_1, w_2, v_2).
$$

Dữ liệu gồm hai điểm $(x, y) = (-1, 1)$ và $(1, 1)$, và hàm mất mát là sai số bình phương trung bình. Tham số $\theta_A = (1, 1, -1, 1)$ cho $f(x) = \max\{0, x\} + \max\{0, -x\} = |x|$, khớp hoàn hảo cả hai điểm, nên $L(\theta_A) = 0$. Đổi chỗ hai nơ-ron ẩn, tức đổi vai $(w_1, v_1)$ với $(w_2, v_2)$, ta được $\theta_B = (-1, 1, 1, 1)$, vẫn biểu diễn đúng hàm $|x|$, nên $L(\theta_B) = 0$.

Nếu $L$ lồi theo $\theta$, trung điểm $\tfrac12(\theta_A + \theta_B) = (0, 1, 0, 1)$ phải có $L \le 0$. Nhưng tại đó $w_1 = w_2 = 0$, mạng xuất ra hằng số 0, và $L = 1$. Đi dọc đoạn thẳng từ $\theta_A$ tới $\theta_B$, hàm mất mát lần lượt bằng $0$, $0.25$, $1$, $0.25$, $0$ tại năm điểm chia đều. Hàm mất mát có hai cực tiểu toàn cục tách rời với một "bướu" ở giữa, hình ảnh đặc trưng của bài toán không lồi.

Lập luận này không phụ thuộc vào ví dụ cụ thể. Trong mọi mạng có từ hai nơ-ron ẩn trở lên trong một tầng, đổi chỗ hai nơ-ron cùng với các trọng số vào và ra của chúng cho một tham số khác mà mạng tính đúng cùng một hàm. Nếu một nghiệm tốt dùng hai nơ-ron khác nhau thật sự, thì trung bình của nó với bản hoán vị làm hai nơ-ron trùng nhau, thường làm mất khả năng biểu diễn. **Đối xứng hoán vị** khiến hàm mất mát của mạng nơ-ron gần như không bao giờ lồi, bất kể hàm mất mát theo đầu ra lồi đến đâu. Chỗ hỏng nằm ở bước hợp hàm: Đầu ra của mạng không còn là hàm affine của tham số, vì tham số của hai tầng nhân với nhau.

## 4. Lồi theo từng khối và lồi theo biến nào

**Cố định một tầng, phần còn lại có thể lồi.** Trong mạng ở mục 3, nếu giữ nguyên $w_1, w_2$ thì $f_\theta(x)$ là hàm **tuyến tính** theo $(v_1, v_2)$, với các "đặc trưng" $\max\{0, w_1 x\}$ và $\max\{0, w_2 x\}$ cố định. Hàm mất mát khi đó là bình phương tối thiểu theo $(v_1, v_2)$, một bài toán lồi. Đây là lý do huấn luyện riêng tầng cuối trên những đặc trưng đã có, như khi tinh chỉnh đầu ra của một mạng đã huấn luyện sẵn, là bài toán lồi. Nhưng như chủ đề các phép toán giữ tính lồi đã cảnh báo, lồi theo từng khối không suy ra lồi đồng thời, và tối ưu luân phiên từng khối có thể dừng ở điểm không tối ưu.

**Đổi biến có thể tạo ra hoặc phá đi tính lồi.** Muốn khớp một số dương $c$ với giá trị đo được 2 bằng sai số bình phương, ta có thể viết $c = e^\theta$ để bảo đảm $c > 0$. Theo biến $c$, hàm mất mát $(c - 2)^2$ lồi. Theo biến $\theta$, hàm $(e^\theta - 2)^2$ có đạo hàm bậc hai $4e^\theta(e^\theta - 1)$, âm khi $\theta < 0$, nên không lồi. Chẳng hạn, tại trung điểm $-1.5$ của đoạn $[-3, 0]$, hàm bằng khoảng $3.157$, lớn hơn trung bình $2.402$ của hai đầu mút. Cùng một mô hình, cùng một dữ liệu, chỉ khác cách đặt tham số. Ví dụ ngược chiều đã gặp ở chủ đề các hàm lồi thường gặp: Log-likelihood Gauss không lõm theo ma trận hiệp phương sai $R$, nhưng lõm theo ma trận nghịch đảo $R^{-1}$. Phép đổi biến affine thì luôn giữ tính lồi, còn phép đổi biến phi tuyến thì phải kiểm tra lại từ đầu.

## 5. Quy trình nhận diện tính lồi

Gom lại, khi gặp một bài toán huấn luyện, bạn có thể đi qua các bước sau.

1. **Xác định biến.** Viết rõ đâu là tham số, đâu là dữ liệu và siêu tham số cố định.
2. **Xem đầu ra của mô hình phụ thuộc tham số thế nào.** Nếu nó là hàm affine của tham số, như hồi quy tuyến tính, logistic, softmax, máy vector hỗ trợ tuyến tính, thì bài toán có cơ hội lồi. Nếu tham số nhân với nhau, như các tầng của mạng nơ-ron hay hai nhân tử của một phân tích ma trận, hãy chuẩn bị cho một bài toán không lồi và tìm đối xứng để chứng minh nhanh.
3. **Kiểm tra hàm mất mát theo đầu ra.** Bình phương, trị tuyệt đối, Huber, hinge, logistic, entropy chéo theo logit đều lồi theo đầu ra, nên hợp với một đầu ra affine vẫn lồi.
4. **Kiểm tra điều chuẩn và ràng buộc.** Chuẩn và bình phương chuẩn lồi. Ràng buộc phải viết được bằng bất đẳng thức của hàm lồi và đẳng thức affine.
5. **Nghĩ tới chuyện tồn tại và duy nhất.** Bài toán lồi vẫn có thể không có nghiệm, như hồi quy logistic trên dữ liệu tách được, hoặc có vô số nghiệm, như đặc trưng cộng tuyến. Điều chuẩn lồi mạnh giải quyết cả hai.

| Mô hình | Lồi theo tham số? | Lý do chính |
| --- | --- | --- |
| Hồi quy tuyến tính, ridge, Lasso | có | mất mát lồi hợp với đầu ra affine, cộng chuẩn |
| Hồi quy logistic và softmax | có | softplus và log-sum-exp hợp với đầu ra affine |
| Máy vector hỗ trợ tuyến tính | có | hinge là max của hai hàm affine |
| Hồi quy Poisson với hàm liên kết mũ | có | $\mu = e^{a^T u + b}$, log-likelihood lõm theo $(a, b)$ |
| Mạng nơ-ron từ hai nơ-ron ẩn | không | đối xứng hoán vị, tham số các tầng nhân nhau |
| Phân tích ma trận $UV^T$ | không đồng thời, có theo từng nhân tử | tích của hai nhóm tham số |

Khi bài toán không lồi, những gì học trong chương vẫn hữu ích. Gần một cực tiểu cục bộ có Hessian xác định dương, hàm mất mát cư xử như một hàm lồi, nên các phân tích cục bộ vẫn dùng được. Nhiều thuật toán cho bài toán không lồi chia nhỏ thành các bài toán con lồi, như tối ưu từng khối. Và đôi khi ta thay bài toán không lồi bằng một bài toán lồi gần với nó, một kỹ thuật gọi là nới lỏng lồi, mà các chương sau sẽ gặp lại.

## 6. Những câu hỏi để đào sâu

**Câu 1.** Hàm mất mát của hồi quy logistic có lồi theo dữ liệu $u_i$ không? Điều đó có quan trọng không?

<details><summary>Xem lời giải thích</summary>

Nói chung là không, nhưng điều đó không quan trọng. Khi huấn luyện, $u_i$ là hằng số, ta không tối ưu theo nó. Tính lồi là tính chất của hàm theo **biến của bài toán tối ưu**, và ở đây biến là $(a, b)$. Câu hỏi "lồi theo dữ liệu" chỉ có ý nghĩa trong những bài toán mà ta tối ưu theo dữ liệu, chẳng hạn khi tìm một đầu vào gây nhầm lẫn cho mô hình đã huấn luyện xong. Khi đó vai trò đổi ngược, tham số là hằng số và đầu vào là biến.

</details>

**Câu 2.** Bỏ hàm ReLU đi, mạng hai tầng chỉ còn là một hàm tuyến tính $f(x) = W_2 W_1 x$, cùng lớp hàm với hồi quy tuyến tính. Hàm mất mát bình phương có lồi theo cặp tham số $(W_1, W_2)$ không?

<details><summary>Xem lời giải thích</summary>

Không, và lập luận hoán vị vẫn dùng được. Lấy đầu vào hai chiều, hai nơ-ron ẩn, và dữ liệu gồm hai điểm $e_1 = (1, 0)$ với nhãn 1, $e_2 = (0, 1)$ với nhãn 2, tức hàm cần học là $x_1 + 2x_2$. Tham số $W_1 = I$, $W_2 = (1, 2)$ cho tích $W_2 W_1 = (1, 2)$, khớp hoàn hảo. Đổi chỗ hai nơ-ron ẩn được $W_1' = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}$, $W_2' = (2, 1)$, có cùng tích $(1, 2)$, nên cũng khớp hoàn hảo. Trung điểm có $W_1$ với mọi phần tử bằng $0.5$ và $W_2 = (1.5, 1.5)$, cho tích $(1.5, 1.5)$, dự đoán $1.5$ ở cả hai điểm, và mất mát trung bình $0.25 > 0$. Điều thú vị là nếu lấy biến là tích $W = W_2 W_1$, bài toán là bình phương tối thiểu theo $W$, hoàn toàn lồi. Tính không lồi ở đây không đến từ lớp hàm, mà đến từ **cách đặt tham số**, đúng tinh thần của câu hỏi "lồi theo biến nào" ở mục 4.

</details>

**Câu 3.** Vì sao điều chuẩn $\ell_2$ làm hồi quy logistic có nghiệm duy nhất, kể cả khi dữ liệu tách được?

<details><summary>Xem lời giải thích</summary>

Hàm $L(a, b) + \tfrac{\lambda}{2}\|(a, b)\|_2^2$ có Hessian $\succeq \lambda I$, nên lồi mạnh. Hàm lồi mạnh tăng ít nhất như một parabol khi tham số chạy ra xa, nên mọi tập mức dưới đều bị chặn, và cực tiểu đạt được. Tính lồi nghiêm ngặt cho nghiệm duy nhất. Về trực giác, điều chuẩn "đánh thuế" độ lớn của tham số, nên không còn lợi khi cho đường sigmoid dốc mãi. Trong mô phỏng, tăng $\lambda$ làm nghiệm lùi về gần gốc và đường cong xác suất thoải hơn.

</details>

**Câu 4.** Nếu hàm mất mát của mạng nơ-ron không lồi, vì sao phương pháp gradient vẫn thường tìm được những tham số tốt trong thực tế?

<details><summary>Xem lời giải thích</summary>

Đây là một câu hỏi nghiên cứu còn mở, và chương này không có câu trả lời đầy đủ. Điều chương này cho ta là ngôn ngữ để đặt câu hỏi cho đúng: Hàm mất mát có nhiều cực tiểu cục bộ không, các cực tiểu có tốt ngang nhau không, các điểm dừng tồi có phải chủ yếu là điểm yên ngựa mà phương pháp gradient có nhiễu dễ thoát ra không. Đối xứng hoán vị ở mục 3 cho thấy các cực tiểu toàn cục thường đến thành từng nhóm tương đương nhau, nên "nhiều cực tiểu" chưa chắc là điều xấu. Nhưng mọi khẳng định mạnh hơn đều cần giả thiết riêng về kiến trúc và dữ liệu.

</details>

## 7. Bài tập tự luyện

::: exercise 1. Hồi quy Poisson
Số sự kiện $y_i \in \{0, 1, 2, \dots\}$ được mô hình hóa bằng phân phối Poisson với trung bình $\mu_i = e^{a^T u_i + b}$. (a) Viết log-likelihood theo $(a, b)$, bỏ các hằng số không phụ thuộc tham số. (b) Chứng minh nó lõm. (c) Nếu thay vì hàm liên kết mũ, ta dùng trực tiếp trung bình affine $\mu_i = a^T u_i + b$, log-likelihood có còn lõm không, và cần thêm điều kiện gì về miền xác định?
:::

::: solution
(a) Xác suất của $y_i$ là $e^{-\mu_i}\mu_i^{y_i}/y_i!$, nên log-likelihood là $\sum_i \big(y_i \log\mu_i - \mu_i\big)$ cộng hằng số. Với $\mu_i = e^{z_i}$ và $z_i = a^T u_i + b$, nó trở thành $\sum_i \big(y_i z_i - e^{z_i}\big)$. (b) $y_i z_i$ là hàm affine của tham số, còn $-e^{z_i}$ là âm của một hàm lồi hợp với hàm affine, nên lõm. Tổng là hàm lõm. (c) Với $\mu_i = a^T u_i + b$, log-likelihood trở thành $\sum_{i=1}^m \big(y_i \log(a^T u_i + b) - (a^T u_i + b)\big)$. Vì $y_i \ge 0$, mỗi số hạng $y_i\log(\cdot)$ là phép hợp giữa hàm lõm $\log$ với hàm affine nhân hệ số không âm, còn $-(a^T u_i + b)$ là hàm affine, do đó từng số hạng đều lõm và tổng vẫn là một hàm lõm. Điều kiện bổ sung nằm ở miền xác định: Ta cần $a^T u_i + b > 0$ với mọi mẫu $i$ có $y_i > 0$. Miền xác định này là một tập lồi vì nó là giao của các nửa không gian mở.
:::

::: exercise 2. Đối xứng hoán vị bằng số
Với mạng và dữ liệu ở mục 3, tính hàm mất mát tại các điểm $\theta(t) = (1 - t)\theta_A + t\theta_B$ với $t = 0.25$ và $t = 0.5$. Tại $t = 0.25$, mạng tính hàm gì?
:::

::: solution
$\theta(t) = (1 - 2t,\ 1,\ -1 + 2t,\ 1)$. Với $t = 0.25$, $\theta = (0.5, 1, -0.5, 1)$, và mạng tính

$$
f(x) = \max\{0,\ 0.5x\} + \max\{0,\ -0.5x\} = 0.5|x| .
$$

Tại $x = \pm 1$, $f = 0.5$, sai số bình phương mỗi điểm là $0.25$, nên $L = 0.25$. Với $t = 0.5$, $\theta = (0, 1, 0, 1)$, mạng xuất ra 0, và $L = 1$. Dọc đoạn $\theta_A \to \theta_B$, mạng tính $|1 - 2t| \cdot |x|$, co lại về 0 ở giữa rồi giãn ra lại, nên hàm mất mát có dạng $(1 - |1 - 2t|)^2$: Bằng 0 ở hai đầu và bằng 1 ở giữa.
:::

::: exercise 3. Đổi biến
Cho $g(\theta) = (e^\theta - 2)^2$. (a) Tìm tập các $\theta$ mà $g''(\theta) \ge 0$. (b) Chứng minh $g$ vẫn có duy nhất một điểm dừng và đó là cực tiểu toàn cục, dù $g$ không lồi. (c) Điều này có mâu thuẫn với nhận xét "không lồi thì có thể có cực tiểu cục bộ tồi" không?
:::

::: solution
(a) $g'(\theta) = 2(e^\theta - 2)e^\theta$ và $g''(\theta) = 4e^{2\theta} - 4e^\theta = 4e^\theta(e^\theta - 1)$, không âm khi và chỉ khi $\theta \ge 0$. (b) $g'(\theta) = 0$ khi và chỉ khi $e^\theta = 2$, tức $\theta = \log 2$, vì $e^\theta > 0$. Tại đó $g = 0 \le g(\theta)$ với mọi $\theta$, nên là cực tiểu toàn cục. (c) Không mâu thuẫn. Không lồi chỉ có nghĩa là mất **bảo đảm** tổng quát, chứ không có nghĩa là chắc chắn có cực tiểu cục bộ tồi. Ở đây $g = h \circ \exp$ với $h(c) = (c - 2)^2$ lồi và $\exp$ là một song ánh tăng từ $\mathbb{R}$ lên $(0, \infty)$, nên mọi tính chất "chỉ có một thung lũng" của $h$ được giữ nguyên, dù độ cong thì không. Những hàm như vậy thuộc lớp tựa lồi.
:::

## Tóm tắt

Khi huấn luyện, tham số là biến và dữ liệu là hằng số, nên tính lồi phải được xét theo tham số. Ước lượng hợp lý cực đại với mô hình tuyến tính và nhiễu có mật độ log-lõm là bài toán lồi, trong đó nhiễu Gauss, Laplace và đều lần lượt cho bình phương tối thiểu, chuẩn $\ell_1$ và chuẩn $\ell_\infty$. Hồi quy logistic phi tuyến theo dữ liệu nhưng lồi theo tham số, có Hessian là tổng các phương sai Bernoulli nhân ma trận hạng một, và không có nghiệm hữu hạn khi dữ liệu tách được nếu thiếu điều chuẩn.

Mạng nơ-ron không lồi vì tham số các tầng nhân với nhau, và đối xứng hoán vị cho một phản ví dụ chỉ bằng vài phép tính. Cố định một tầng thì phần còn lại có thể lồi, và một phép đổi biến phi tuyến có thể tạo ra hoặc phá đi tính lồi. Quy trình nhận diện đi từ việc xác định biến, xem đầu ra phụ thuộc tham số ra sao, kiểm tra hàm mất mát, điều chuẩn và ràng buộc, tới câu hỏi tồn tại và duy nhất nghiệm.

## Tài liệu tham khảo

- Stephen Boyd, Lieven Vandenberghe, *Convex Optimization*, Cambridge University Press.
