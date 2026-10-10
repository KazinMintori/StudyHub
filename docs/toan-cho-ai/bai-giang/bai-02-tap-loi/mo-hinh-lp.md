---
course: toan-cho-ai
lecture: bai-02-tap-loi
topic: mo-hinh-lp
section: topic
title: "Những bài toán trở thành LP"
description: "Ba mô hình bài toán trông có vẻ phi tuyến nhưng thực chất quy về quy hoạch tuyến tính: Tâm Chebyshev của đa diện với lập luận Cauchy–Schwarz, cực tiểu hàm tuyến tính từng khúc bằng dạng epigraph, và cận chặt cho kỳ vọng khi chỉ biết một phần phân phối, kèm so sánh với bất đẳng thức Markov và Cantelli."
---

Sức mạnh của quy hoạch tuyến tính không nằm ở chỗ nhiều bài toán được phát biểu sẵn dưới dạng LP, mà ở chỗ rất nhiều bài toán **không trông giống LP chút nào** lại có thể quy về LP một cách hoàn toàn tự nhiên. Tìm hình tròn lớn nhất nằm trong một đa giác là một bài toán hình học về khoảng cách. Cực tiểu một hàm có góc nhọn là một bài toán không khả vi. Tìm xác suất lớn nhất của một biến cố khi chỉ biết vài thông tin về phân phối là một bài toán xác suất. Cả ba dạng bài này đều chuyển hóa thành LP.

Bài giảng này khảo sát ba mô hình tiêu biểu ấy. Điều quan trọng cần nắm vững không phải là việc ghi nhớ máy móc từng công thức, mà là hai thao tác tư duy cốt lõi lặp lại trong cả ba: Thay một điều kiện "với mọi" bằng giá trị lớn nhất của nó, và tách một giá trị lớn nhất thành nhiều bất đẳng thức tuyến tính.

## 1. Tâm Chebyshev của một đa diện

Cho đa diện $\mathcal{P} = \{x \in \mathbb{R}^n : a_i^Tx \le b_i,\ i = 1, \ldots, m\}$. Ta muốn tìm hình cầu Euclid lớn nhất nằm trong $\mathcal{P}$. Tâm của hình cầu ấy được gọi là **tâm Chebyshev** của đa diện: Điểm nằm sâu nhất bên trong, xa biên nhất. Biểu diễn hình cầu bằng tâm $x_c$ và bán kính $r$:

$$
\mathcal{B} = \{x_c + u : \|u\|_2 \le r\}.
$$

Biến của bài toán là $x_c$ và $r$, và ta muốn cực đại $r$ với điều kiện $\mathcal{B} \subseteq \mathcal{P}$.

Điều kiện "hình cầu nằm trong một nửa không gian" là một điều kiện "với mọi": Với mọi $u$ có $\|u\|_2 \le r$, ta cần $a_i^T(x_c + u) \le b_i$. Điều kiện này đúng khi và chỉ khi nó đúng với $u$ làm vế trái lớn nhất. Theo bất đẳng thức Cauchy–Schwarz, $a_i^Tu \le \|a_i\|_2\|u\|_2 \le r\|a_i\|_2$, với dấu bằng khi $u$ cùng hướng với $a_i$, nên

$$
\sup\{a_i^Tu : \|u\|_2 \le r\} = r\|a_i\|_2 .
$$

Vậy hình cầu nằm trong nửa không gian thứ $i$ khi và chỉ khi $a_i^Tx_c + r\|a_i\|_2 \le b_i$, một bất đẳng thức **tuyến tính** theo $(x_c, r)$, vì $\|a_i\|_2$ chỉ là một con số tính từ dữ liệu. Tâm Chebyshev là nghiệm của LP

$$
\begin{aligned}
\text{maximize}\quad & r\\
\text{subject to}\quad & a_i^Tx_c + r\|a_i\|_2 \le b_i, \quad i = 1, \ldots, m .
\end{aligned}
$$

Một vô hạn điều kiện, ứng với mọi điểm của hình cầu, đã được thay bằng đúng một bất đẳng thức cho mỗi cạnh. Đây là thao tác thứ nhất của trang này.

Xét ví dụ minh họa: Ngũ giác cho bởi $x_1 \ge 0$, $x_2 \ge 0$, $x_1 + 2x_2 \le 8$, $3x_1 + x_2 \le 12$ và $-x_1 + x_2 \le 3$, có năm đỉnh $(0, 0)$, $(4, 0)$, $(3.2, 2.4)$, $(\tfrac23, \tfrac{11}{3})$ và $(0, 3)$. Giải LP, ta được tâm $x_c = (r, r)$ với

$$
r = 6 - 2\sqrt5 \approx 1.528 .
$$

Hình tròn tiếp xúc với ba cạnh $x_1 = 0$, $x_2 = 0$ và $x_1 + 2x_2 = 8$. Thật vậy, khoảng cách từ $(r, r)$ tới đường $x_1 + 2x_2 = 8$ là $\tfrac{8 - 3r}{\sqrt5}$, và đặt nó bằng $r$ cho đúng $r = \tfrac{8}{3 + \sqrt5} = 6 - 2\sqrt5$. Hai ràng buộc còn lại không chặt, nên có thể dịch chúng một chút mà nghiệm không đổi. Trong mặt phẳng, LP có ba biến, nên ở một đỉnh của miền khả thi trong $\mathbb{R}^3$ thường có đúng ba ràng buộc chặt: Hình tròn lớn nhất thường chạm đúng ba cạnh.

<ChebyshevCenterLab />

Tâm Chebyshev có một ý nghĩa thực tế sâu sắc. Nếu đa diện mô tả những thông số thiết kế chấp nhận được, thì tâm Chebyshev là thiết kế **chịu được sai lệch tốt nhất (robust design)**: Mọi sai lệch có độ lớn nhỏ hơn $r$ theo bất kỳ hướng nào đều vẫn giữ thiết kế trong vùng chấp nhận được. Điểm này khác trọng tâm diện tích của đa giác. Với ngũ giác trên, trọng tâm ở khoảng $(1.682, 1.501)$, gần cạnh $x_2 = 0$ hơn tâm Chebyshev.

## 2. Cực tiểu hàm tuyến tính từng khúc

Một hàm lồi tuyến tính từng khúc luôn viết được thành giá trị lớn nhất của các hàm affine,

$$
f(x) = \max_{i = 1, \ldots, m}\,(a_i^Tx + b_i),
$$

như [chủ đề về phép toán giữ tính lồi](../bai-01-nhap-mon-toi-uu/phep-toan-giu-tinh-loi-cua-ham.md) của Lecture 01 đã chỉ ra. Cực tiểu $f$ là bài toán không khả vi, vì hàm có góc tại những nơi hai mảnh gặp nhau. Dạng epigraph biến nó thành một LP. Trước hết, bài toán tương đương với cực tiểu $t$ với điều kiện $\max_i(a_i^Tx + b_i) \le t$. Sau đó, tách giá trị lớn nhất thành $m$ điều kiện:

$$
\begin{aligned}
\text{minimize}\quad & t\\
\text{subject to}\quad & a_i^Tx + b_i \le t, \quad i = 1, \ldots, m .
\end{aligned}
$$

Đây là thao tác thứ hai: "Giá trị lớn nhất không vượt quá $t$" đúng khi và chỉ khi "từng giá trị không vượt quá $t$".

Ví dụ một biến: Xét hàm $f(x) = \max\{-x + 3,\ 0.5x,\ 2x - 5\}$. LP tương ứng là cực tiểu $t$ với $-x + 3 \le t$, $0.5x \le t$, $2x - 5 \le t$. Đường giảm $-x + 3$ và đường tăng chậm $0.5x$ cắt nhau tại $x = 2$ với giá trị 1, còn đường $2x - 5$ chỉ vượt lên trên $0.5x$ khi $x > \tfrac{10}{3}$. Nghiệm là $x^\star = 2$, $t^\star = 1$. Tại nghiệm, hai ràng buộc đầu chặt và ràng buộc thứ ba còn dư. Các bài toán khớp dữ liệu theo chuẩn $\ell_1$ hay $\ell_\infty$ ở Lecture 01 là những trường hợp riêng của mô hình này.

## 3. Cận chặt cho kỳ vọng khi chỉ biết một phần phân phối

Đây là một bài toán rất thú vị trong xác suất thống kê. Giả sử biến ngẫu nhiên $x$ chỉ nhận các giá trị rời rạc $u_1, \ldots, u_n$ đã biết, nhưng phân phối xác suất $p_i = \operatorname{prob}(x = u_i)$ thì chưa biết cụ thể. Vector phân phối $p$ chỉ cần thỏa mãn $p \succeq 0$ và điều kiện chuẩn hóa $\sum_{i=1}^n p_i = p_1 + p_2 + \dots + p_n = 1$. Điểm mấu chốt là mọi kỳ vọng:

$$
\mathbb{E}[f(x)] = \sum_{i=1}^n p_i f(u_i) = p_1 f(u_1) + \dots + p_n f(u_n)
$$

và mọi xác suất $\operatorname{prob}(x \in S) = \sum_{u_i \in S} p_i$ đều là **hàm tuyến tính của vector xác suất $p$**. Vì vậy những hiểu biết có sẵn, chẳng hạn cận trên và cận dưới của một vài kỳ vọng, là những ràng buộc tuyến tính trên $p$. Cận nhỏ nhất và lớn nhất có thể của một kỳ vọng khác chính là nghiệm của hai bài toán LP theo biến $p$.

Ví dụ: Xét biến ngẫu nhiên $x$ nhận giá trị trong tập rời rạc $\{0, 1, 2, 3, 4\}$, và ta chỉ biết thông tin kỳ vọng $\mathbb{E}[x] = 1$. Xác suất $\operatorname{prob}(x \ge 3)$ lớn nhất có thể là bao nhiêu? LP cực đại $p_3 + p_4$ với các ràng buộc $\sum_{k=0}^4 p_k = 1$, $\sum_{k=0}^4 k\,p_k = 1$, $p \succeq 0$ cho giá trị tối ưu $\tfrac13$, đạt tại phân phối dồn $\tfrac23$ khối lượng vào 0 và $\tfrac13$ vào 3. Con số $\tfrac13$ chính là cận của **bất đẳng thức Markov**, $\operatorname{prob}(x \ge 3) \le \tfrac{\mathbb{E}[x]}{3}$, và LP cho thấy cận ấy là chặt nhất không thể cải thiện nếu chỉ dùng duy nhất thông tin này.

Bây giờ ta biết thêm thông tin bậc hai $\mathbb{E}[x^2] = 2$, nghĩa là phương sai $\operatorname{Var}(x) = \mathbb{E}[x^2] - (\mathbb{E}[x])^2 = 2 - 1 = 1$. Bổ sung thêm một ràng buộc tuyến tính $\sum_{k=0}^4 k^2 p_k = 2$, bài toán LP cho xác suất lớn nhất là $\tfrac16$, đạt tại phân phối $(\tfrac13, \tfrac12, 0, \tfrac16, 0)$. Bất đẳng thức Cantelli một phía cho cận $\tfrac{\sigma^2}{\sigma^2 + 2^2} = 0.2$, nhưng cận ấy dành cho mọi phân phối bất kỳ trên trục số thực. Muốn đạt được 0.2 thì phân phối phải đặt khối lượng tại điểm 0.5, vốn không thuộc tập giá trị rời rạc cho phép. Khi biết thêm $x$ chỉ nhận giá trị nguyên từ 0 tới 4, LP trả về cận chặt hơn, và đó là cận tối ưu tuyệt đối với thông tin đã có, vì nó đạt được bởi một phân phối cụ thể.

## 4. Lập kế hoạch qua nhiều giai đoạn

Trong thực tế tối ưu hóa, mô hình quy hoạch tuyến tính còn xử lý rất tự nhiên yếu tố biến thiên theo thời gian (Dynamic LP). Xét bài toán lập kế hoạch kinh tế đa giai đoạn: Một nền kinh tế có $n$ ngành, mức độ hoạt động của ngành $j$ ở giai đoạn $t$ là $x_j(t) \ge 0$. Hoạt động sản xuất vừa tiêu thụ vừa tạo ra hàng hóa theo tỉ lệ với mức hoạt động, và lượng tiêu thụ ở giai đoạn sau không được vượt lượng sản xuất ở giai đoạn trước. Hàng hóa dư ra ở mỗi giai đoạn là một biến bù, và mục tiêu là cực đại tổng giá trị chiết khấu của hàng hóa dư. Mọi quan hệ giữa các biến đều tuyến tính, nên toàn bộ kế hoạch qua $N$ giai đoạn là một bài toán LP dạng chuẩn. Ý tưởng "biến cho từng thời điểm, ràng buộc liên kết các thời điểm liền nhau" sẽ trở lại ở Lecture 07, khi so sánh LP với quy hoạch động.

## 5. Những câu hỏi để đào sâu

**Câu 1.** Nếu thay hình cầu Euclid bằng hình vuông song song với các trục, tức hình cầu chuẩn $\ell_\infty$, thì bài toán tìm hình vuông lớn nhất nằm trong đa diện còn là LP không?

<details><summary>Xem lời giải thích</summary>

Còn. Lập luận giữ nguyên, chỉ thay $\sup\{a^Tu : \|u\|_\infty \le r\}$ bằng $r\|a\|_1$, vì giá trị lớn nhất đạt khi mỗi thành phần $u_j = r\,\operatorname{sign}(a_j)$. Ràng buộc trở thành $a_i^Tx_c + r\|a_i\|_1 \le b_i$, vẫn tuyến tính. Tổng quát, với một chuẩn bất kỳ, hệ số của $r$ là [chuẩn đối ngẫu](../bai-01-nhap-mon-toi-uu/non-doi-ngau.md) của $a_i$, nên bài toán luôn là LP, chỉ khác cách tính hệ số từ dữ liệu.

</details>

**Câu 2.** Với hình chữ nhật $[0, 4] \times [0, 2]$, tâm Chebyshev có duy nhất không? Bán kính thì sao?

<details><summary>Xem lời giải thích</summary>

Bán kính lớn nhất là $1$ và duy nhất, vì nó là giá trị tối ưu của LP. Tâm thì không duy nhất: Mọi điểm $(t, 1)$ với $1 \le t \le 3$ đều là tâm của một hình tròn bán kính 1 nằm trong hình chữ nhật. Tập nghiệm của LP là cả đoạn thẳng ấy, đúng như một LP có thể có cả một cạnh làm tập nghiệm. Nếu cần một tâm duy nhất, chẳng hạn trung điểm $(2, 1)$, phải thêm một tiêu chí phụ, ví dụ cực tiểu khoảng cách tới trọng tâm trong số các tâm tối ưu.

</details>

**Câu 3.** Cực tiểu một hàm lồi tuyến tính từng khúc là LP. Còn cực đại nó trên một đa giác thì sao?

<details><summary>Xem lời giải thích</summary>

Không còn là LP, và nói chung khó hơn hẳn. Cực đại một hàm lồi trên một đa diện đạt tại một đỉnh, nhưng không có cách nào tránh việc so sánh nhiều đỉnh, vì hàm lồi không cho ta biết đỉnh nào xa hơn chỉ từ thông tin cục bộ. Về hình thức, điều kiện "$\max_i(a_i^Tx + b_i) \ge t$" là một phép "hoặc": Chỉ cần một trong các bất đẳng thức $a_i^Tx + b_i \ge t$ đúng. Một phép "hoặc" mô tả hợp của các nửa không gian, không phải giao, nên tập khả thi không còn lồi. Sự bất đối xứng giữa cực tiểu và cực đại một hàm lồi là một trong những bài học quan trọng nhất của môn học.

</details>

**Câu 4.** Trong ví dụ phân phối, vì sao có thể nói cận $\tfrac16$ là **chặt**, trong khi cận Cantelli $0.2$ thì không chặt cho bài toán này?

<details><summary>Xem lời giải thích</summary>

Cận $\tfrac16$ đạt được bởi một phân phối cụ thể, $(\tfrac13, \tfrac12, 0, \tfrac16, 0)$, thỏa mọi thông tin đã biết. Vì vậy không thể chứng minh một cận nhỏ hơn $\tfrac16$ chỉ từ thông tin ấy. Cận Cantelli đúng cho mọi phân phối có cùng trung bình và phương sai trên trục số, và nó đạt được bởi phân phối dồn $0.2$ vào điểm 3 và $0.8$ vào điểm 0.5. Phân phối ấy hợp lệ trên trục số nhưng vi phạm thông tin "$x$ chỉ nhận giá trị nguyên từ 0 tới 4". Mỗi bất đẳng thức xác suất cổ điển là đáp án của một LP như vậy với một tập thông tin nhất định. LP cho phép đưa thêm bất kỳ thông tin tuyến tính nào và luôn trả về cận tốt nhất ứng với thông tin đó.

</details>

**Câu 5.** Thêm cả hai ràng buộc $\mathbb{E}x = 1$, $\mathbb{E}x^2 = 2$, xác suất $\operatorname{prob}(x \ge 3)$ nhỏ nhất có thể là bao nhiêu? Kết quả này nói gì?

<details><summary>Xem lời giải thích</summary>

LP cực tiểu cho giá trị 0, đạt tại phân phối dồn $\tfrac12$ vào 0 và $\tfrac12$ vào 2, có trung bình 1 và $\mathbb{E}x^2 = 2$. Vậy với thông tin này, xác suất của biến cố có thể nằm bất kỳ đâu trong $[0, \tfrac16]$. Một khoảng rộng như thế là một câu trả lời trung thực: Thông tin đã có không đủ để kết luận chính xác, và mọi con số cụ thể trong khoảng ấy đều cần thêm giả định.

</details>

## 6. Bài tập tự luyện

::: exercise 1. Tâm Chebyshev của tam giác vuông
Tìm tâm Chebyshev và bán kính của tam giác có đỉnh $(0, 0)$, $(6, 0)$, $(0, 8)$. Viết LP trước, rồi giải bằng lập luận hình học.
:::

::: hint
Cạnh huyền nằm trên đường $8x_1 + 6x_2 = 48$, có pháp tuyến dài $\|(8, 6)\|_2 = 10$.
:::

::: solution
Tam giác là $\{x_1 \ge 0,\ x_2 \ge 0,\ 8x_1 + 6x_2 \le 48\}$. LP là cực đại $r$ với $-x_{c,1} + r \le 0$, $-x_{c,2} + r \le 0$ và $8x_{c,1} + 6x_{c,2} + 10r \le 48$. Hình tròn lớn nhất là đường tròn nội tiếp, tiếp xúc cả ba cạnh. Hai ràng buộc đầu chặt cho $x_c = (r, r)$, và ràng buộc thứ ba chặt cho $8r + 6r + 10r = 48$, tức $r = 2$. Tâm là $(2, 2)$, khớp với công thức bán kính nội tiếp của tam giác vuông, $\tfrac{a + b - c}{2} = \tfrac{6 + 8 - 10}{2} = 2$.
:::

::: exercise 2. Hàm tuyến tính từng khúc hai biến
Hàm $f$ trên $\mathbb{R}^2$ là giá trị lớn nhất của ba hàm $x_1 + x_2 - 2$, $-x_1$ và $-x_2$. Viết LP để cực tiểu $f$ và tìm nghiệm.
:::

::: solution
LP là cực tiểu $t$ với $x_1 + x_2 - 2 \le t$, $-x_1 \le t$, $-x_2 \le t$. Cộng cả ba ràng buộc, mỗi ràng buộc với hệ số 1, ta được $-2 \le 3t$, tức $t \ge -\tfrac23$ với mọi điểm khả thi. Cận này đạt khi cả ba ràng buộc chặt: $x_1 = x_2 = \tfrac23$, và khi đó $x_1 + x_2 - 2 = -\tfrac23$. Vậy nghiệm là $x^\star = (\tfrac23, \tfrac23)$ với $f^\star = -\tfrac23$. Bộ hệ số $(1, 1, 1)$ là một chứng nhận tối ưu, cùng loại với chứng nhận của LP ở Lecture 01.
:::

::: exercise 3. Khi thông tin xác định hoàn toàn phân phối
Biến $x$ nhận giá trị trong $\{0, 1, 2\}$. (a) Chỉ biết $\mathbb{E}x = 0.5$, tìm $\operatorname{prob}(x = 2)$ lớn nhất có thể. (b) Biết thêm $\mathbb{E}x^2 = 0.7$, xác suất ấy có thể nằm trong khoảng nào?
:::

::: solution
(a) Cực đại $p_2$ với $p_0 + p_1 + p_2 = 1$, $p_1 + 2p_2 = 0.5$, $p \succeq 0$. Để $p_2$ lớn nhất, đặt $p_1 = 0$, được $p_2 = 0.25$ và $p_0 = 0.75$, đúng cận Markov $\tfrac{\mathbb{E}x}{2}$. (b) Hai phương trình $p_1 + 2p_2 = 0.5$ và $p_1 + 4p_2 = 0.7$ cho $p_2 = 0.1$, $p_1 = 0.3$, rồi $p_0 = 0.6$. Ba ràng buộc đẳng thức trên ba biến xác định hoàn toàn phân phối, nên cận dưới và cận trên trùng nhau: Xác suất đúng bằng 0.1.
:::

## Tóm tắt

Nhiều bài toán không trông giống LP lại là LP nhờ hai thao tác. Thao tác thứ nhất thay một điều kiện "với mọi điểm trong một tập" bằng giá trị lớn nhất trên tập đó, như khi điều kiện hình cầu nằm trong nửa không gian trở thành $a_i^Tx_c + r\|a_i\|_2 \le b_i$. Thao tác thứ hai tách "giá trị lớn nhất không vượt quá $t$" thành nhiều bất đẳng thức, như trong dạng epigraph của hàm tuyến tính từng khúc.

Tâm Chebyshev là điểm sâu nhất của đa diện và là nghiệm của một LP. Cực tiểu một hàm lồi tuyến tính từng khúc là LP, nhưng cực đại nó thì không. Khi phân phối của một biến ngẫu nhiên hữu hạn chưa biết, mọi kỳ vọng đều tuyến tính theo phân phối, nên cận chặt nhất cho một kỳ vọng từ những thông tin tuyến tính đã có là nghiệm của một LP, và bất đẳng thức Markov là một trường hợp riêng.

## Tài liệu tham khảo

- Stephen Boyd, Lieven Vandenberghe, *Convex Optimization*, Cambridge University Press.
