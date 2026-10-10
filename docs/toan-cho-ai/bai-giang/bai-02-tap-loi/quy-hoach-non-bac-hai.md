---
course: toan-cho-ai
lecture: bai-02-tap-loi
topic: quy-hoach-non-bac-hai
section: topic
title: "Quy hoạch nón bậc hai và LP bền vững"
description: "Ràng buộc nón bậc hai và vì sao nó lồi, quy hoạch nón bậc hai cùng quan hệ với LP và QCQP, cảnh báo khi bình phương hai vế, LP bền vững với hệ số bất định trong ellipsoid, ràng buộc xác suất với hệ số Gauss, ràng buộc hyperbolic và cách viết nhiều bài toán chứa chuẩn Euclid thành SOCP."
---

Một ràng buộc tuyến tính $a^Tx \le b$ giả định rằng ta biết chính xác vector $a$. Trong thực tế, $a$ thường là một ước lượng: Hàm lượng dinh dưỡng của thực phẩm, năng suất của một máy, hệ số của một mô hình học từ dữ liệu. Nếu muốn ràng buộc đúng với **mọi** giá trị có thể của $a$ trong một vùng bất định hình ellipsoid, ràng buộc tuyến tính ấy biến thành một ràng buộc có chứa chuẩn Euclid. Lớp bài toán chứa những ràng buộc như thế được gọi là **quy hoạch nón bậc hai** (second-order cone program, SOCP).

Trang này định nghĩa SOCP, chỉ ra nó nằm ở đâu so với LP và QCQP, rồi xem hai nguồn sinh ra nó trong sách: LP bền vững và ràng buộc xác suất.

## 1. Ràng buộc nón bậc hai

Một ràng buộc có dạng

$$
\|Ax + b\|_2 \le c^Tx + d,
$$

với $A \in \mathbb{R}^{k \times n}$, được gọi là **ràng buộc nón bậc hai**. Tên gọi đến từ việc nó đòi hỏi vector $(Ax + b,\ c^Tx + d) \in \mathbb{R}^{k+1}$ nằm trong nón bậc hai

$$
\mathcal{K} = \{(y, t) \in \mathbb{R}^{k+1} : \|y\|_2 \le t\},
$$

chính là [nón chuẩn](../bai-01-nhap-mon-toi-uu/chuan-va-non-chuan.md) của chuẩn Euclid. Vì $\mathcal{K}$ là tập lồi và ánh xạ $x \mapsto (Ax + b, c^Tx + d)$ là affine, tập các $x$ thỏa ràng buộc là ảnh ngược của một tập lồi qua ánh xạ affine, nên lồi. Một **SOCP** cực tiểu một hàm tuyến tính với các ràng buộc như vậy:

$$
\begin{aligned}
\text{minimize}\quad & f^Tx\\
\text{subject to}\quad & \|A_ix + b_i\|_2 \le c_i^Tx + d_i, \quad i = 1, \ldots, m,\\
& Fx = g .
\end{aligned}
$$

Hai trường hợp riêng cho thấy SOCP chứa những lớp đã biết. Khi mọi $A_i = 0$, vế trái là một hằng số không âm $\|b_i\|_2$, và ràng buộc trở thành một bất đẳng thức tuyến tính: SOCP thành LP. Khi mọi $c_i = 0$, vế phải là hằng số $d_i$, và bình phương hai vế cho một ràng buộc toàn phương lồi: SOCP thành QCQP. SOCP còn tổng quát hơn cả hai.

**Đừng bình phương một cách vô tư.** Bình phương hai vế của $\|Ax + b\|_2 \le c^Tx + d$ cho $\|Ax + b\|_2^2 \le (c^Tx + d)^2$, nhưng hai ràng buộc không tương đương. Ràng buộc gốc buộc ngầm $c^Tx + d \ge 0$, còn ràng buộc bình phương thì không. Ví dụ một biến: $|x| \le -1$ vô nghiệm, nhưng $x^2 \le 1$ có cả đoạn nghiệm $[-1, 1]$. Hơn nữa, $(c^Tx + d)^2$ là hàm lồi, nên ràng buộc bình phương có dạng "lồi ≤ lồi", không phải dạng chuẩn lồi. Cách viết nón bậc hai giữ được cả tính lồi lẫn điều kiện dấu.

## 2. LP bền vững

Xét một LP dạng bất đẳng thức, cực tiểu $c^Tx$ với $a_i^Tx \le b_i$, nhưng mỗi vector $a_i$ chỉ được biết là nằm trong một ellipsoid

$$
\mathcal{E}_i = \{\bar a_i + P_iu : \|u\|_2 \le 1\},
$$

với tâm $\bar a_i$ là giá trị danh nghĩa và ma trận $P_i$ mô tả độ bất định. Ta đòi hỏi mỗi ràng buộc đúng với mọi $a_i \in \mathcal{E}_i$. Đây là một điều kiện "với mọi", và cũng như với [tâm Chebyshev](./mo-hinh-lp.md), ta thay nó bằng giá trị lớn nhất:

$$
\sup\{a_i^Tx : A_i \in \mathcal{E}_i\} = \bar a_i^Tx + \sup\{u^TP_i^Tx : \|u\|_2 \le 1\} = \bar a_i^Tx + \|P_i^Tx\|_2 ,
$$

trong đó đẳng thức cuối là bất đẳng thức Cauchy–Schwarz, đạt khi $u$ cùng hướng với $P_i^Tx$. Vậy LP bền vững là SOCP

$$
\begin{aligned}
\text{minimize}\quad & c^Tx\\
\text{subject to}\quad & \bar a_i^Tx + \|P_i^Tx\|_2 \le b_i, \quad i = 1, \ldots, m .
\end{aligned}
$$

Số hạng $\|P_i^Tx\|_2$ có một cách hiểu đáng nhớ: Nó đóng vai một **số hạng điều chuẩn**, ngăn $x$ lớn theo những hướng mà hệ số còn nhiều bất định. Một nghiệm bền vững là một nghiệm thận trọng: Nó chấp nhận giá trị mục tiêu kém hơn một chút để đổi lấy sự an toàn trước sai số của dữ liệu.

Ví dụ tự đặt: Cực đại $x_1 + 2x_2$ với năm ràng buộc $x_1 \le 3$, $x_2 \le 2$, $x_1 + x_2 \le 4$, $-x_1 \le 1$, $-x_2 \le 1$. Nghiệm danh nghĩa là $(2, 2)$ với giá trị 6. Bây giờ giả sử mỗi vector hệ số chỉ biết nằm trong hình tròn bán kính $\rho$ quanh giá trị danh nghĩa, tức $P_i = \rho I$, và ràng buộc bền vững là $\bar a_i^Tx + \rho\|x\|_2 \le b_i$. Với $\rho = 0.2$, nghiệm bền vững là $(2,\ 1.5)$ với giá trị 5. Kiểm tra trực tiếp: $\|(2, 1.5)\|_2 = 2.5$, nên hai ràng buộc $x_2 \le 2$ và $x_1 + x_2 \le 4$ trở thành $1.5 + 0.5 = 2$ và $3.5 + 0.5 = 4$, cùng chặt. Còn nghiệm danh nghĩa $(2, 2)$ có $\rho\|x\|_2 \approx 0.566$, nên trong trường hợp xấu nhất nó vượt cả hai ràng buộc ấy khoảng 0.566.

<RobustLPLab />

## 3. Ràng buộc xác suất

Có thể nhìn LP bền vững từ góc độ thống kê. Giả sử $a_i$ là vector ngẫu nhiên Gauss với trung bình $\bar a_i$ và hiệp phương sai $\Sigma_i$, và ta chỉ đòi hỏi ràng buộc đúng với xác suất ít nhất $\eta$:

$$
\operatorname{prob}(a_i^Tx \le b_i) \ge \eta .
$$

Với $x$ cố định, $u = a_i^Tx$ là biến Gauss với trung bình $\bar u = \bar a_i^Tx$ và độ lệch chuẩn $\sigma = \|\Sigma_i^{1/2}x\|_2$. Gọi $\Phi$ là hàm phân phối của Gauss chuẩn, ràng buộc trở thành $\Phi\big((b_i - \bar u)/\sigma\big) \ge \eta$, tức

$$
\bar a_i^Tx + \Phi^{-1}(\eta)\,\|\Sigma_i^{1/2}x\|_2 \le b_i .
$$

Khi $\eta \ge \tfrac12$, hệ số $\Phi^{-1}(\eta) \ge 0$, và đây là một ràng buộc nón bậc hai. Khi $\eta < \tfrac12$, hệ số âm, vế trái là một hàm affine trừ đi một chuẩn, hàm lõm, và ràng buộc không còn lồi. Đòi hỏi độ tin cậy cao lại cho bài toán dễ, còn đòi hỏi độ tin cậy thấp lại cho bài toán khó, một điều thoạt nghe rất ngược đời.

Ví dụ một biến: Hàm lượng một chất trong mỗi đơn vị nguyên liệu là biến Gauss với trung bình 2 và độ lệch chuẩn 0.3, và tổng hàm lượng trong $x$ đơn vị không được vượt quá 10 với xác suất ít nhất 95%. Với $\Phi^{-1}(0.95) \approx 1.645$, ràng buộc là $2x + 1.645 \times 0.3\,x \le 10$, tức $x \le 4.01$. Nếu bỏ qua bất định và dùng giá trị trung bình, ta cho phép $x$ tới 5, nhưng khi đó xác suất vi phạm là đúng 50%. Một mô phỏng Monte Carlo với hai triệu mẫu xác nhận xác suất thỏa ràng buộc tại $x = 4.01$ là khoảng 0.95.

## 4. Ràng buộc hyperbolic và những biểu thức khác

Nhiều ràng buộc không trông giống nón bậc hai vẫn viết lại được thành nón bậc hai. Một đồng nhất thức hữu ích, là bài tập 4.26 của sách: Với $y, z \ge 0$,

$$
x^Tx \le yz \iff \left\|\begin{bmatrix} 2x \\ y - z \end{bmatrix}\right\|_2 \le y + z .
$$

Chứng minh chỉ là khai triển. Bình phương vế phải trừ bình phương vế trái là $(y + z)^2 - (y - z)^2 - 4x^Tx$, rút gọn thành $4(yz - x^Tx)$, và cả hai vế đều không âm khi $y, z \ge 0$. Nhờ đó, ràng buộc $\tfrac{\|x\|_2^2}{y} \le t$ với $y > 0$, chẳng hạn khi một hàm mục tiêu chứa tỉ số giữa bình phương sai số và một phương sai cần ước lượng, là một ràng buộc nón bậc hai.

Một số bài toán quen thuộc khác cũng là SOCP. Cực tiểu $\|Ax - b\|_2$ là cực tiểu $t$ với $\|Ax - b\|_2 \le t$. Cực tiểu tổng các chuẩn $\sum_i \|A_ix + b_i\|_2$ là cực tiểu $\sum_i t_i$ với $\|A_ix + b_i\|_2 \le t_i$. Sách còn trình bày bài toán **mặt cực tiểu**: Tìm mặt có diện tích nhỏ nhất căng trên một khung cho trước. Sau khi rời rạc hóa, diện tích là tổng các chuẩn Euclid của những vector gradient xấp xỉ, nên bài toán cũng là SOCP.

## 5. Những câu hỏi để đào sâu

**Câu 1.** Nếu thay vùng bất định hình ellipsoid bằng một hình hộp, tức mỗi thành phần $a_{ij}$ nằm trong $[\bar a_{ij} - \delta, \bar a_{ij} + \delta]$, thì LP bền vững trở thành bài toán gì?

<details><summary>Xem lời giải thích</summary>

Giá trị lớn nhất của $a^Tx$ trên hình hộp là $\bar a^Tx + \delta\|x\|_1$, đạt khi mỗi $a_j$ lệch về phía cùng dấu với $x_j$. Chẳng hạn với $\bar a = (1, 2)$, $\delta = 0.1$ và $x = (3, -1)$, giá trị lớn nhất là $1 + 0.1 \times 4 = 1.4$. Ràng buộc bền vững $\bar a^Tx + \delta\|x\|_1 \le b$ chứa chuẩn $\ell_1$, và viết được thành các bất đẳng thức tuyến tính bằng biến phụ $|x_j| \le s_j$. Vậy LP bền vững với hộp bất định vẫn là một LP. Hình dạng của vùng bất định quyết định lớp bài toán: Hộp cho LP, ellipsoid cho SOCP. Đây là một ví dụ của nguyên tắc chung: Giá trị lớn nhất của $a^Tx$ trên một hình cầu chuẩn là chuẩn đối ngẫu của $x$.

</details>

**Câu 2.** Trong ví dụ ràng buộc xác suất, nếu chỉ đòi hỏi xác suất thỏa ràng buộc là 10% thì sao? Vì sao bài toán lại trở nên không lồi?

<details><summary>Xem lời giải thích</summary>

Với $\eta = 0.1$, $\Phi^{-1}(0.1) \approx -1.28 < 0$, và ràng buộc là $\bar a^Tx - 1.28\,\|\Sigma^{1/2}x\|_2 \le b$. Vế trái là affine trừ một chuẩn, nên lõm, và tập các $x$ thỏa ràng buộc nói chung không lồi. Trực giác như sau. Với độ tin cậy thấp, ta được phép "đánh cược" rằng sai số sẽ có lợi cho mình, và có nhiều cách đặt cược rời rạc nhau: Đi theo một hướng mà sai số có thể kéo $a^Tx$ xuống, hoặc theo một hướng khác. Hợp của những lựa chọn ấy không lồi. Với độ tin cậy cao, ta phải phòng thủ theo mọi hướng, và yêu cầu phòng thủ là một giao, một tập lồi. Trong một chiều, như ví dụ nguyên liệu với $x \ge 0$, ràng buộc vẫn chỉ là một đoạn, nên điều này chỉ lộ ra từ hai chiều trở lên.

</details>

**Câu 3.** LP bền vững cho nghiệm $(2, 1.5)$ với giá trị 5, thấp hơn nghiệm danh nghĩa 6. Có phải lúc nào cũng nên dùng nghiệm bền vững không?

<details><summary>Xem lời giải thích</summary>

Không hẳn. Nghiệm bền vững tối ưu cho trường hợp **xấu nhất** trong vùng bất định, và cái giá là giá trị kém đi 1 đơn vị, tức khoảng 17%, ngay cả khi hệ số thật đúng bằng giá trị danh nghĩa. Nếu vùng bất định được chọn quá rộng, nghiệm sẽ quá thận trọng. Nếu vi phạm ràng buộc chỉ gây thiệt hại nhỏ, ràng buộc xác suất với $\eta$ vừa phải có thể hợp lý hơn. Lựa chọn giữa danh nghĩa, bền vững và xác suất là một quyết định mô hình hóa, phụ thuộc vào hậu quả của việc vi phạm, không phải một câu hỏi toán học có đáp án duy nhất.

</details>

**Câu 4.** Trong mô phỏng, mỗi ràng buộc ban đầu là một đường thẳng, nhưng biên của miền khả thi bền vững lại cong. Độ cong ấy đến từ đâu?

<details><summary>Xem lời giải thích</summary>

Biên của ràng buộc bền vững thứ $i$ là tập $\{x : \bar a_i^Tx + \rho\|x\|_2 = b_i\}$. Chuyển vế và bình phương cho thấy đó là một đường conic, một nhánh của hyperbol, parabol hay ellipse tùy theo $\rho$ so với $\|\bar a_i\|_2$. Về hình học, miền bền vững là giao của vô số nửa mặt phẳng $\{a^Tx \le b_i\}$, mỗi nửa ứng với một vector $a$ trong hình tròn bất định. Giao của vô số nửa mặt phẳng với pháp tuyến biến thiên liên tục cho một biên cong, giống như hình tròn là giao của vô số nửa mặt phẳng tiếp xúc với nó.

</details>

## 6. Bài tập tự luyện

::: exercise 1. Viết thành SOCP
Viết bài toán cực tiểu $\|Ax - b\|_2 + \lambda\|x\|_2$, với $\lambda > 0$, thành một SOCP.
:::

::: solution
Thêm hai biến $t_1, t_2$ và viết: Cực tiểu $t_1 + \lambda t_2$ với $\|Ax - b\|_2 \le t_1$ và $\|x\|_2 \le t_2$. Hai ràng buộc là ràng buộc nón bậc hai theo $(x, t_1, t_2)$, hàm mục tiêu tuyến tính. Bài toán tương đương bài toán gốc vì tại nghiệm, cả hai ràng buộc đều chặt: Nếu $t_1 > \|Ax - b\|_2$, giảm $t_1$ sẽ giảm hàm mục tiêu.
:::

::: exercise 2. Ràng buộc xác suất
Một xe tải chở $x$ thùng hàng, mỗi thùng nặng trung bình 50 kg với độ lệch chuẩn 4 kg, các thùng độc lập và phân phối Gauss. Tải trọng tối đa là 2000 kg. Tìm $x$ lớn nhất để xác suất quá tải không quá 5%, bỏ qua yêu cầu $x$ nguyên.
:::

::: hint
Tổng khối lượng có trung bình $50x$ và độ lệch chuẩn $4\sqrt{x}$, không phải $4x$, vì các thùng độc lập.
:::

::: solution
Ràng buộc là $50x + 1.645 \times 4\sqrt{x} \le 2000$. Đặt $s = \sqrt x$, ta có $50s^2 + 6.58s - 2000 \le 0$, cho $s \le \tfrac{-6.58 + \sqrt{6.58^2 + 400000}}{100} \approx 6.259$, tức $x$ không vượt quá khoảng $39.18$. Nếu bỏ qua bất định, ta cho phép 40 thùng, và khi đó xác suất quá tải là 50%. Lưu ý độ lệch chuẩn của tổng tăng theo $\sqrt x$ vì các thùng độc lập, khác với ví dụ nguyên liệu ở mục 3, nơi cả $x$ đơn vị dùng chung một hệ số ngẫu nhiên.
:::

::: exercise 3. Kiểm tra đồng nhất thức
Với $x = (1, 2)$, $y = 2$, $z = 3$, kiểm tra cả hai vế của đồng nhất thức hyperbolic ở mục 4.
:::

::: solution
Vế trái: $x^Tx = 5 \le yz = 6$, đúng. Vế phải: Vector $(2x, y - z) = (2, 4, -1)$ có chuẩn $\sqrt{21} \approx 4.583$, không vượt quá $y + z = 5$, cũng đúng. Hai vế cùng đúng, và hiệu bình phương $25 - 21 = 4 = 4(yz - x^Tx)$, khớp với chứng minh.
:::

## Tóm tắt

Ràng buộc nón bậc hai $\|Ax + b\|_2 \le c^Tx + d$ lồi vì nó là ảnh ngược của nón chuẩn Euclid qua một ánh xạ affine. SOCP cực tiểu hàm tuyến tính với các ràng buộc như vậy, và chứa LP cùng QCQP như trường hợp riêng. Không được bình phương hai vế khi chưa giữ điều kiện vế phải không âm.

SOCP xuất hiện tự nhiên khi dữ liệu bất định. Đòi một ràng buộc tuyến tính đúng với mọi hệ số trong một ellipsoid cho thêm một số hạng chuẩn $\|P^Tx\|_2$, đóng vai điều chuẩn và làm miền khả thi co lại thành một miền có biên cong. Đòi ràng buộc đúng với xác suất $\eta \ge \tfrac12$ khi hệ số là Gauss cho một ràng buộc cùng dạng với hệ số $\Phi^{-1}(\eta)$. Đồng nhất thức hyperbolic cho phép viết thêm nhiều biểu thức khác thành nón bậc hai.

## Nguồn và đọc thêm

- S. Boyd, L. Vandenberghe, *Convex Optimization*, §4.4.2 (tr. 156–160) về SOCP, LP bền vững, LP với ràng buộc xác suất, Ví dụ 4.8 và bài toán mặt cực tiểu. Bài tập 4.26 về ràng buộc hyperbolic.
- Ví dụ LP năm ràng buộc với hình tròn bất định, mô phỏng, ví dụ nguyên liệu, ví dụ hộp bất định, các câu hỏi và bài tập do người soạn bổ sung. Mọi con số đã được tính lại bằng chương trình, ràng buộc xác suất được kiểm thêm bằng mô phỏng Monte Carlo.
