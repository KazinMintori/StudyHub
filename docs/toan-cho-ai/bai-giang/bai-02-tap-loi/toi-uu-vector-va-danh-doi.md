---
course: toan-cho-ai
lecture: bai-02-tap-loi
topic: toi-uu-vector-va-danh-doi
section: topic
title: "Tối ưu vector, điểm Pareto và đường đánh đổi"
description: "Bài toán tối ưu với hàm mục tiêu nhận giá trị vector so sánh theo một nón, điểm tối ưu và ví dụ ước lượng không chệch tốt nhất, điểm Pareto, vô hướng hóa và cách hiểu hình học qua siêu phẳng tựa, bài toán đa mục tiêu và phân tích đánh đổi, bình phương tối thiểu có điều chuẩn với ridge và lasso, danh mục đầu tư theo lợi suất và rủi ro."
---

Khi huấn luyện một mô hình, ta muốn sai số trên dữ liệu nhỏ, nhưng cũng muốn các tham số không quá lớn để mô hình không học thuộc dữ liệu. Khi chọn một danh mục đầu tư, ta muốn lợi suất cao và rủi ro thấp. Hai mục tiêu ấy thường mâu thuẫn: Cải thiện mục tiêu này phải trả giá bằng mục tiêu kia. Lúc đó "phương án tốt nhất" không còn là một điểm, mà là cả một tập các phương án mà không phương án nào thắng phương án nào trên mọi mặt.

Bài học này trình bày phương pháp giải quyết những bài toán như thế: **Tối ưu vector** với hàm mục tiêu nhận giá trị vector, khái niệm **điểm Pareto**, và kỹ thuật **vô hướng hóa** biến bài toán nhiều mục tiêu thành một họ bài toán thông thường. Ví dụ trung tâm là bình phương tối thiểu có điều chuẩn, nền tảng của ridge và lasso trong học máy.

## 1. Bài toán tối ưu vector

Bài toán tối ưu vector có dạng

$$
\begin{aligned}
\text{minimize (theo } K\text{)}\quad & f_0(x)\\
\text{subject to}\quad & f_i(x) \le 0, \quad i = 1, \ldots, m,\\
& h_i(x) = 0, \quad i = 1, \ldots, p,
\end{aligned}
$$

với $f_0 : \mathbb{R}^n \to \mathbb{R}^q$ nhận giá trị vector và $K \subseteq \mathbb{R}^q$ là một nón chính quy dùng để so sánh các giá trị mục tiêu. Viết $f_0(x) \preceq_K f_0(y)$ nghĩa là $x$ tốt bằng hoặc tốt hơn $y$. Điều làm tối ưu vector khác hẳn tối ưu thông thường là hai giá trị mục tiêu **có thể không so sánh được**: Có thể không có $f_0(x) \preceq_K f_0(y)$, cũng không có $f_0(y) \preceq_K f_0(x)$. Với hai số thực, điều đó không bao giờ xảy ra. Bài toán là lồi nếu $f_0$ lồi theo nón $K$, các $f_i$ lồi và các $h_i$ affine.

Đối tượng trung tâm là **tập các giá trị đạt được**

$$
\mathcal{O} = \{f_0(x) : X \text{ khả thi}\} \subseteq \mathbb{R}^q .
$$

## 2. Điểm tối ưu và điểm Pareto

Nếu $\mathcal{O}$ có một [phần tử nhỏ nhất](../bai-01-nhap-mon-toi-uu/bat-dang-thuc-tong-quat.md), tức một giá trị $f_0(x^\star)$ tốt bằng hoặc tốt hơn mọi giá trị đạt được, thì $x^\star$ là **tối ưu**. Về hình học, điều đó có nghĩa là $\mathcal{O} \subseteq f_0(x^\star) + K$: Mọi giá trị đạt được đều nằm trong vùng "kém hơn hoặc bằng" của $f_0(x^\star)$. Trường hợp này hiếm, nhưng có một ví dụ nổi tiếng trong lý thuyết ước lượng thống kê. Trong mô hình đo $y = Ax + v$ với nhiễu có trung bình 0 và hiệp phương sai $I$, mọi bộ ước lượng tuyến tính không chệch $\hat x = Fy$ với $FA = I$ có ma trận hiệp phương sai sai số $FF^T$. So sánh các ma trận này theo nón PSD, bộ ước lượng bình phương tối thiểu $F^\star = (A^TA)^{-1}A^T$ là tối ưu: Bất đẳng thức ma trận $FF^T \succeq F^\star F^{\star T}$ thỏa mãn với mọi $F$ khả thi. Đó là định lý Gauss–Markov.

Thường thì $\mathcal{O}$ không có phần tử nhỏ nhất, và ta dùng khái niệm yếu hơn. Một điểm khả thi $x$ là **tối ưu Pareto** nếu $f_0(x)$ là một phần tử tối thiểu của $\mathcal{O}$: Mọi điểm khả thi $y$ tốt bằng hoặc tốt hơn $x$ đều có cùng giá trị mục tiêu với $x$. Nói cách khác, không thể cải thiện một mặt mà không làm xấu đi một mặt khác. Tập các giá trị Pareto nằm trên biên của $\mathcal{O}$, ở phía "tốt" của nó.

## 3. Vô hướng hóa

Cách tiêu chuẩn để tìm điểm Pareto là chọn một vector trọng số $\lambda \succ_{K^*} 0$, tức dương ngặt theo [nón đối ngẫu](../bai-01-nhap-mon-toi-uu/non-doi-ngau.md), và giải bài toán thông thường

$$
\text{minimize}\quad \lambda^Tf_0(x) \qquad \text{subject to các ràng buộc cũ.}
$$

Mọi nghiệm của bài toán này là một điểm Pareto. Lời chứng minh ngắn: Nếu $x$ không Pareto, có $y$ khả thi với $f_0(y) \preceq_K f_0(x)$ và $f_0(y) \ne f_0(x)$. Khi đó $f_0(x) - f_0(y)$ thuộc $K$ và khác 0, nên $\lambda^T(f_0(x) - f_0(y)) > 0$ vì $\lambda$ dương ngặt theo nón đối ngẫu. Vậy $\lambda^Tf_0(y) < \lambda^Tf_0(x)$, mâu thuẫn với việc $x$ là nghiệm.

Về hình học, $x$ là nghiệm của bài toán vô hướng hóa khi và chỉ khi siêu phẳng $\{u : \lambda^Tu = \lambda^Tf_0(x)\}$ là một [siêu phẳng tựa](../bai-01-nhap-mon-toi-uu/sieu-phang-phan-tach-va-tua.md) của $\mathcal{O}$ tại $f_0(x)$: Toàn bộ $\mathcal{O}$ nằm về một phía của nó. Vì vậy, ngoài một điểm Pareto, vô hướng hóa còn cho cả một nửa không gian các giá trị không thể đạt được. Khi $\mathcal{O}$ không lồi, có những điểm Pareto nằm ở chỗ "lõm" của biên mà không siêu phẳng tựa nào chạm tới, và vô hướng hóa bỏ sót chúng. Với bài toán **lồi**, điều này không xảy ra theo nghĩa sau: Mọi điểm Pareto đều là nghiệm của bài toán vô hướng hóa với một trọng số $\lambda \succeq_{K^*} 0$ khác 0 nào đó. Cần cẩn thận ở chỗ khi $\lambda$ có thành phần bằng 0, không phải mọi nghiệm đều Pareto.

## 4. Bài toán đa mục tiêu và đường đánh đổi

Khi $K = \mathbb{R}^q_+$, ta có bài toán **đa mục tiêu**, với $q$ mục tiêu riêng $F_1, \ldots, F_q$. Điểm $x$ trội hơn $y$ nếu $F_i(x) \le F_i(y)$ với mọi $i$ và ít nhất một bất đẳng thức chặt. Điểm Pareto là điểm không bị điểm khả thi nào trội hơn. Tập các giá trị Pareto được gọi là mặt đánh đổi tối ưu, hay **đường đánh đổi** khi có hai mục tiêu.

Cách đọc một đường cong đánh đổi hai mục tiêu (đường biên Pareto): Hai đầu mút cho giá trị nhỏ nhất có thể của từng mục tiêu khi bỏ qua mục tiêu kia. Giao với một đường thẳng đứng $F_1 = \alpha$ cho biết $F_2$ phải lớn đến đâu để đạt $F_1 \le \alpha$. Độ dốc tại một điểm cho tỉ lệ đánh đổi cục bộ. Một điểm có độ cong lớn, nơi muốn giảm thêm một chút ở mục tiêu này phải tăng rất nhiều ở mục tiêu kia, là **khuỷu** của đường cong, và trong nhiều ứng dụng đó là một thỏa hiệp tốt.

Khi vô hướng hóa bằng tổng có trọng số:

$$
\sum_{i=1}^q \lambda_i F_i(x) = \lambda_1 F_1(x) + \cdots + \lambda_q F_q(x) \quad (\lambda_i \ge 0),
$$

tỉ số $\lambda_i/\lambda_j$ đóng vai một **tỉ giá** giữa hai mục tiêu: Giảm $F_i$ một lượng $\alpha$ được xem ngang bằng tăng $F_j$ một lượng $(\lambda_i/\lambda_j)\alpha$. Tăng trọng số của một mục tiêu sẽ cho một điểm Pareto mới tốt hơn về mục tiêu đó. Tại những chỗ đường đánh đổi trơn, $\lambda$ chính là pháp tuyến hướng vào trong của nó. Ý tưởng cực tiểu tổng có trọng số rồi điều chỉnh các trọng số chính là hạt nhân cốt lõi dẫn vào lý thuyết đối ngẫu (Duality), đề tài trọng tâm của Lecture 03.

## 5. Bình phương tối thiểu có điều chuẩn

Với $A \in \mathbb{R}^{m \times n}$ và $b \in \mathbb{R}^m$, ta muốn $x$ vừa khớp dữ liệu, tức $F_1(x) = \|Ax - b\|_2^2$ nhỏ, vừa không lớn, tức $F_2(x) = \|x\|_2^2$ nhỏ. Vô hướng hóa với trọng số $(1, \mu)$, ta cực tiểu $\|Ax - b\|_2^2 + \mu\|x\|_2^2$, một hàm toàn phương có nghiệm

$$
x(\mu) = (A^TA + \mu I)^{-1}A^Tb .
$$

Đây là **điều chuẩn Tikhonov**, mà học máy gọi là **ridge regression**. Ma trận $A^TA + \mu I$ dương xác định với mọi $\mu > 0$, nên nghiệm luôn tồn tại và duy nhất, kể cả khi $A$ có các cột phụ thuộc. Khi $\mu$ chạy từ 0 tới $\infty$, $x(\mu)$ vạch ra toàn bộ đường đánh đổi, trừ hai đầu mút: Giới hạn $\mu \to 0$ cho nghiệm bình phương tối thiểu chuẩn nhỏ nhất $A^\dagger b$, còn $\mu \to \infty$ cho $x = 0$.

Xét ví dụ với $A$ có các hàng $(1, 2)$, $(2, 1)$, $(1, 1)$, $(3, 1)$ và $b = (3, 1, 2, 4)$. Nghiệm bình phương tối thiểu là $x \approx (0.707,\ 1.049)$ với $F_1 \approx 2.93$ và $F_2 \approx 1.60$. Với $\mu = 1$, nghiệm là $(0.75,\ 0.875)$: Sai số $F_1$ tăng nhẹ lên khoảng 3.05, đổi lại $F_2$ giảm còn khoảng 1.33. Với $\mu = 10$, nghiệm $(0.607,\ 0.479)$ có $F_2 \approx 0.60$ nhưng $F_1 \approx 6.27$. Đoạn đầu của đường đánh đổi khá phẳng: Giảm $F_2$ từ 1.60 xuống 1.33 chỉ tốn khoảng 0.12 đơn vị $F_1$. Càng về sau, mỗi đơn vị $F_2$ giảm thêm càng đắt.

Thay $\|x\|_2^2$ bằng chuẩn $\ell_1$, ta có **lasso**, cực tiểu $\|Ax - b\|_2^2 + \mu\|x\|_1$. Chuẩn $\ell_1$ được sử dụng rộng rãi như một kỹ thuật đắc lực để tìm nghiệm thưa (sparse solution), vì số thành phần khác 0 của $x$ không lồi, như chủ đề [hàm tựa lồi](./toi-uu-tua-loi.md) đã chỉ ra, còn $\|x\|_1$ là xấp xỉ lồi hợp lý của nó. Với dữ liệu trên, lasso cho $x_2$ bằng **đúng 0** khi $\mu$ từ $\tfrac{86}{7} \approx 12.29$ trở lên, và cả $x$ bằng 0 khi $\mu \ge 38$. Ridge thì làm các thành phần co dần nhưng không bao giờ bằng đúng 0. Điều đáng chú ý là trên đoạn đầu của đường lasso, $x_1$ còn tăng lên trong khi $x_2$ giảm: Khi một đặc trưng bị phạt và co lại, đặc trưng tương quan với nó gánh thêm phần việc.

<TradeoffLab />

## 6. Danh mục đầu tư theo lợi suất và rủi ro

Bài toán Markowitz ở [chủ đề quy hoạch toàn phương](./quy-hoach-toan-phuong.md) thực chất là một bài toán hai mục tiêu: Cực tiểu theo $\mathbb{R}^2_+$ cặp $(-\bar p^Tx,\ x^T\Sigma x)$, tức âm lợi suất trung bình và phương sai, với $\mathbf{1}^Tx = 1$, $x \succeq 0$. Vô hướng hóa với trọng số $(1, \gamma)$ cho QP cực tiểu $-\bar p^Tx + \gamma\,x^T\Sigma x$, với $\gamma$ là mức ngại rủi ro.

Với hai tài sản A, B của chủ đề ấy, nghiệm có công thức. Viết $x = (x_1, 1 - x_1)$, đạo hàm bằng 0 cho $x_1 = \tfrac{0.06/\gamma + 0.008}{0.056}$, kẹp vào đoạn $[0, 1]$. Với $\gamma = 1$, nhà đầu tư ít ngại rủi ro dồn toàn bộ vào A, lợi suất 10% với độ lệch chuẩn 15%. Với $\gamma = 5$, tỉ lệ đặt vào A khoảng 35.7%, cho lợi suất khoảng 6.14% và độ lệch chuẩn khoảng 5.67%. Với $\gamma = 20$, tỉ lệ ấy giảm còn khoảng 19.6%, cho lợi suất khoảng 5.18% và độ lệch chuẩn khoảng 4.48%. Mỗi $\gamma$ cho một điểm Pareto, từ đó ta có thể vẽ toàn bộ đường đánh đổi lợi suất và rủi ro cho bài toán phân bổ tài sản.

## 7. Những câu hỏi để đào sâu

**Câu 1.** Vô hướng hóa với trọng số $\lambda = (1, 0)$ trong bài toán điều chuẩn cho nghiệm gì? Nghiệm ấy có luôn là điểm Pareto không?

<details><summary>Xem lời giải thích</summary>

Với $\lambda = (1, 0)$, ta chỉ cực tiểu $\|Ax - b\|_2^2$, bỏ qua $\|x\|$. Nếu $A$ có các cột độc lập, nghiệm duy nhất và là một đầu mút của đường đánh đổi, nên vẫn Pareto. Nếu các cột phụ thuộc, có cả một mặt phẳng các nghiệm bình phương tối thiểu, và chỉ nghiệm có chuẩn nhỏ nhất, $A^\dagger b$, là Pareto, vì các nghiệm khác có cùng $F_1$ nhưng $F_2$ lớn hơn. Đây là một lưu ý then chốt: Khi vector trọng số có thành phần bằng 0, không phải mọi nghiệm của bài toán vô hướng hóa đều tự động là điểm Pareto, mà bắt buộc phải kiểm tra thêm.

</details>

**Câu 2.** Trong mô phỏng, đường tựa $F_1 + \mu F_2 = \text{hằng số}$ chạm đám mây giá trị đạt được đúng tại điểm Pareto, và cả đám mây nằm về một phía của nó. Hãy chứng minh điều này từ định nghĩa của $x(\mu)$.

<details><summary>Xem lời giải thích</summary>

Điểm $x(\mu)$ cực tiểu $F_1 + \mu F_2$ trên mọi $x$, nên với mọi điểm đạt được $(F_1(y), F_2(y))$ ta có

$$
F_1(y) + \mu F_2(y) \ge F_1(x(\mu)) + \mu F_2(x(\mu)) .
$$

Điều này nói rằng mọi điểm của đám mây nằm trên hoặc phía trên đường thẳng $F_1 + \mu F_2 = c$ đi qua điểm Pareto. Hệ số góc của đường là $-1/\mu$, và nó cho tỉ giá cục bộ: Quanh điểm đó, giảm $F_2$ một đơn vị phải trả khoảng $\mu$ đơn vị $F_1$.

</details>

**Câu 3.** Lasso cho nghiệm có thành phần bằng đúng 0, còn ridge thì không. Hãy giải thích bằng hình học của hai quả cầu chuẩn.

<details><summary>Xem lời giải thích</summary>

Bài toán có điều chuẩn tương đương với cực tiểu $\|Ax - b\|_2^2$ trên một quả cầu chuẩn $\{\|x\| \le r\}$ với bán kính phù hợp. Các đường mức của $\|Ax - b\|_2^2$ là những ellipse. Nghiệm là chỗ ellipse nhỏ nhất chạm quả cầu. Quả cầu $\ell_2$ tròn, nên điểm chạm nói chung không nằm trên trục. Quả cầu $\ell_1$ là một hình vuông xoay có các đỉnh nằm trên trục, và một ellipse đang nở thường chạm đỉnh trước, nơi một tọa độ bằng 0. Nhìn qua [chủ đề quả cầu chuẩn](../bai-01-nhap-mon-toi-uu/chuan-va-non-chuan.md), các góc nhọn của quả cầu $\ell_1$ chính là nguồn gốc của tính thưa.

</details>

**Câu 4.** Nếu lựa chọn trọng số điều chuẩn $\mu$ bằng cách tìm giá trị cực tiểu hóa sai số trực tiếp trên tập dữ liệu huấn luyện, hệ quả thực nghiệm sẽ dẫn tới hiện tượng gì?

<details><summary>Xem lời giải thích</summary>

Vì trên dữ liệu huấn luyện, $F_1$ luôn nhỏ nhất khi $\mu \to 0$, tức không điều chuẩn gì cả. Đường đánh đổi chỉ cho biết những lựa chọn hiệu quả, không cho biết lựa chọn nào tốt cho mục đích thật, là dự đoán trên dữ liệu mới. Trong học máy, $\mu$ thường được chọn bằng cách đánh giá trên một tập dữ liệu kiểm định riêng. Lý thuyết tối ưu vector cho ta không gian lựa chọn, còn việc chọn điểm nào trên đường đánh đổi cần một tiêu chí nằm ngoài bài toán.

</details>

**Câu 5.** Trong bài toán hai mục tiêu $F_1 = (x - 3)^2$, $F_2 = x^2$ với $x \in \mathbb{R}$, những điểm nào là Pareto, và đường đánh đổi có phương trình gì?

<details><summary>Xem lời giải thích</summary>

Mọi $x \in [0, 3]$ đều Pareto: Dịch $x$ về phía 3 làm $F_1$ giảm nhưng $F_2$ tăng, và ngược lại. Ngoài đoạn ấy, chẳng hạn $x < 0$, điểm $x = 0$ trội hơn vì cả hai mục tiêu đều nhỏ hơn. Vô hướng hóa $(x - 3)^2 + \mu x^2$ cho $x(\mu) = \tfrac{3}{1 + \mu}$, chạy hết khoảng $(0, 3)$ khi $\mu$ chạy từ $\infty$ về 0. Trên đoạn $[0, 3]$, $|x - 3| + |x| = 3$, nên đường đánh đổi là $\sqrt{F_1} + \sqrt{F_2} = 3$, tức $F_2 = (3 - \sqrt{F_1})^2$ với $0 \le F_1 \le 9$, một đường cong lồi.

</details>

## 8. Bài tập tự luyện

::: exercise 1. Ridge bằng tay
Với $A = I_2$ và $b = (2, 1)$, tìm $x(\mu)$ của bài toán cực tiểu $\|x - b\|_2^2 + \mu\|x\|_2^2$, rồi tính $F_1$ và $F_2$ theo $\mu$.
:::

::: solution
Với $A = I$, $x(\mu) = \tfrac{1}{1 + \mu}b = \tfrac{1}{1 + \mu}(2, 1)$. Khi đó $F_1 = \|x - b\|_2^2 = \left(\tfrac{\mu}{1 + \mu}\right)^2\|b\|_2^2 = \tfrac{5\mu^2}{(1 + \mu)^2}$ và $F_2 = \tfrac{5}{(1 + \mu)^2}$. Hai mục tiêu thỏa $\sqrt{F_1} + \sqrt{F_2} = \sqrt5$, nên đường đánh đổi là $F_2 = (\sqrt5 - \sqrt{F_1})^2$. Với $\mu = 1$, $x = (1, 0.5)$ và $F_1 = F_2 = 1.25$.
:::

::: exercise 2. Danh mục theo mức ngại rủi ro
Với hai tài sản ở mục 6, mức ngại rủi ro $\gamma$ nhỏ nhất bao nhiêu thì nhà đầu tư bắt đầu giữ một phần tài sản B?
:::

::: solution
Nghiệm không kẹp là $x_1 = \tfrac{0.06/\gamma + 0.008}{0.056}$. Nhà đầu tư giữ một phần B khi $x_1 < 1$, tức $\tfrac{0.06}{\gamma} + 0.008 < 0.056$, hay $\tfrac{0.06}{\gamma} < 0.048$, nghĩa là $\gamma > 1.25$. Với $\gamma \le 1.25$, danh mục dồn toàn bộ vào A.
:::

::: exercise 3. Kiểm tra một điểm Pareto
Trong bài toán $F_1 = (x - 3)^2$, $F_2 = x^2$, trọng số $\mu$ nào cho điểm Pareto $x = 1$? Tại đó, giảm $F_2$ một đơn vị phải trả khoảng bao nhiêu đơn vị $F_1$?
:::

::: solution
Từ $x(\mu) = \tfrac{3}{1 + \mu} = 1$ suy ra $\mu = 2$. Tại $x = 1$, $F_1 = 4$ và $F_2 = 1$. Theo cách hiểu của đường tựa, tỉ giá cục bộ là $\mu = 2$: Giảm $F_2$ một đơn vị phải tăng $F_1$ khoảng 2 đơn vị. Kiểm tra trên đường cong $F_2 = (3 - \sqrt{F_1})^2$: Đạo hàm $\tfrac{dF_2}{dF_1} = -\tfrac{3 - \sqrt{F_1}}{\sqrt{F_1}} = -\tfrac{1}{2}$ tại $F_1 = 4$, nghĩa là mỗi đơn vị $F_1$ đổi được nửa đơn vị $F_2$, tức đúng tỉ giá 2 đổi 1.
:::

## Tóm tắt

Tối ưu vector so sánh các giá trị mục tiêu theo một nón, và vì vậy hai phương án có thể không so sánh được. Điểm tối ưu, tốt hơn mọi điểm khác trên mọi mặt, hiếm khi tồn tại. Định lý Gauss–Markov là một trường hợp hiếm ấy. Khái niệm thực dụng là điểm Pareto: Không thể cải thiện một mặt mà không làm xấu mặt khác.

Vô hướng hóa với trọng số dương ngặt theo nón đối ngẫu luôn cho điểm Pareto, và về hình học tương ứng với một siêu phẳng tựa của tập giá trị đạt được. Với bài toán lồi, quét các trọng số cho hầu hết, theo nghĩa chính xác ở mục 3, mọi điểm Pareto. Bình phương tối thiểu có điều chuẩn là ví dụ trung tâm: Ridge cho đường đánh đổi với nghiệm co dần về 0, lasso cho nghiệm có thành phần bằng đúng 0. Danh mục đầu tư Markowitz là một bài toán hai mục tiêu giữa lợi suất và rủi ro, với mức ngại rủi ro đóng vai trọng số.

## Tài liệu tham khảo

- Stephen Boyd, Lieven Vandenberghe, *Convex Optimization*, Cambridge University Press.
