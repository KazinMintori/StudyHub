---
course: toan-cho-ai
lecture: bai-01-nhap-mon-toi-uu
topic: dieu-kien-bac-hai
section: topic
title: "Điều kiện bậc hai và độ cong"
description: "Điều kiện Hessian nửa xác định dương, độ cong theo từng hướng và trị riêng, vì sao điều kiện đúng, hàm bậc hai và bình phương tối thiểu với đặc trưng cộng tuyến, hàm x²/y, lồi nghiêm ngặt, lồi mạnh và số điều kiện quyết định tốc độ của phương pháp gradient."
---

Điều kiện bậc nhất so sánh hàm với các tiếp tuyến của nó, và để dùng được, ta vẫn phải xét từng cặp điểm $x, y$. Nếu hàm có đạo hàm bậc hai, câu chuyện gọn hơn nhiều. Tính lồi trở thành một phép kiểm tra **tại từng điểm**: Tại mỗi $x$, ma trận Hessian phải nửa xác định dương. Đây là công cụ được dùng nhiều nhất khi cần nhận diện một hàm lồi cụ thể.

Nhưng Hessian còn cho biết nhiều hơn một câu trả lời có hoặc không. Nó đo độ cong của hàm theo từng hướng, cho biết hàm có dạng cái bát, cái máng hay cái yên ngựa quanh mỗi điểm, và các trị riêng của nó quyết định một thuật toán như phương pháp gradient chạy nhanh hay chậm. Lần lượt từng vai trò ấy sẽ được làm rõ dưới đây.

## 1. Phát biểu

> **Định lý.** Giả sử $f$ khả vi hai lần, nghĩa là $\operatorname{dom} f$ mở và Hessian $\nabla^2 f$ tồn tại tại mọi điểm của nó. Khi đó $f$ lồi khi và chỉ khi $\operatorname{dom} f$ lồi và
> $$\nabla^2 f(x) \succeq 0 \quad \text{với mọi } x \in \operatorname{dom} f.$$

Với hàm một biến, điều kiện là $f''(x) \ge 0$ trên một khoảng, tức đạo hàm $f'$ không giảm. Điều kiện này không mới: Nó là tính đơn điệu của gradient ở chủ đề trước, phát biểu lại qua đạo hàm của đạo hàm. Dưới góc nhìn hình học, điều kiện $\nabla^2 f(x) \succeq 0$ phản ánh việc đồ thị hàm số luôn có **độ cong hướng lên** tại $x$. Tương tự, $f$ lõm khi và chỉ khi miền xác định lồi và $\nabla^2 f(x) \preceq 0$ tại mọi điểm.

Hai cụm từ "mọi điểm" và "miền lồi" đều có ý nghĩa tiên quyết. Hàm $1/x^2$ có $f''(x) = 6/x^4 > 0$ tại mọi điểm thuộc miền xác định, nhưng miền xác định gồm hai khoảng mở rời nhau $(-\infty, 0) \cup (0, \infty)$, không phải là một tập lồi, nên hàm số không lồi. Ở chiều ngược lại, một hàm có Hessian nửa xác định dương gần như khắp nơi, chỉ cần vi phạm trên một dải hẹp, cũng đủ làm mất tính lồi toàn cục, như mô phỏng ở mục 2 sẽ làm sáng tỏ.

## 2. Độ cong theo một hướng

Đặt $g(t) = f(x + tv)$, hàm hạn chế của $f$ lên đường thẳng qua $x$ theo hướng $v$. Áp dụng quy tắc dây chuyền hai lần:

$$
g'(t) = \nabla f(x + tv)^T v, \qquad g''(t) = v^T \nabla^2 f(x + tv)\, v .
$$

Tại $t = 0$, ta được $g''(0) = v^T \nabla^2 f(x) v$. Vậy dạng toàn phương của Hessian đo **độ cong của đồ thị khi đi qua $x$ theo hướng $v$**. Điều kiện $\nabla^2 f(x) \succeq 0$ nói rằng không có đường thẳng nào qua $x$ mà dọc theo nó đồ thị cong xuống.

Phân tích phổ cho thấy độ cong thay đổi thế nào khi xoay hướng. Theo định lý phổ cho ma trận đối xứng thực, ta có thể khai triển tường minh ma trận Hessian thành:

$$
\nabla^2 f(x) = \sum_{i=1}^n \lambda_i q_i q_i^T = \lambda_1 q_1 q_1^T + \lambda_2 q_2 q_2^T + \dots + \lambda_n q_n q_n^T
$$

với $\{q_1, q_2, \dots, q_n\}$ là hệ vector riêng trực chuẩn ứng với các trị riêng $\lambda_1 \le \lambda_2 \le \dots \le \lambda_n$. Với vector hướng đơn vị $\|v\|_2 = 1$, ta biểu diễn $v$ qua cơ sở trực chuẩn $v = \sum_{i=1}^n (q_i^T v) q_i$. Khi đó dạng toàn phương trở thành:

$$
\begin{aligned}
v^T \nabla^2 f(x)\, v &= \sum_{i=1}^n \lambda_i \,(q_i^T v)^2 = \lambda_1 (q_1^T v)^2 + \dots + \lambda_n (q_n^T v)^2, \\
\sum_{i=1}^n (q_i^T v)^2 &= (q_1^T v)^2 + \dots + (q_n^T v)^2 = \|v\|_2^2 = 1 .
\end{aligned}
$$

Độ cong theo hướng $v$ chính là một tổ hợp lồi (trung bình có trọng số) của các trị riêng với các trọng số không âm $(q_i^T v)^2 \ge 0$ có tổng bằng 1. Vì vậy, độ cong luôn nằm giữa trị riêng nhỏ nhất $\lambda_1$ và trị riêng lớn nhất $\lambda_n$, đồng thời đạt hai giá trị biên đó đúng khi $v$ là vector riêng tương ứng. Ma trận Hessian nửa xác định dương khi và chỉ khi trị riêng nhỏ nhất không âm ($\lambda_{\min} \ge 0$), tức hướng "cong ít nhất" cũng không hề cong xuống.

Với hàm hai biến, dấu của hai trị riêng cho ta bốn hình dạng cơ bản của đồ thị quanh một điểm:

| Hai trị riêng | Hình dạng quanh $x$ | Tương thích với tính lồi |
| --- | --- | --- |
| cùng dương | cái bát, cong lên theo mọi hướng | có |
| một dương, một bằng 0 | cái máng, phẳng dọc một hướng | có |
| một dương, một âm | cái yên ngựa | không |
| cùng âm | cái bát úp | không |

<HessianMapLab />

Mô phỏng tô đỏ những điểm mà Hessian có trị riêng âm. Với $(x_1^2 - 1)^2 + x_2^2$, Hessian là $\operatorname{diag}(12x_1^2 - 4,\ 2)$, nên vùng đỏ đúng là dải $|x_1| < 1/\sqrt3 \approx 0.577$. Ngoài dải ấy hàm cong lên theo mọi hướng, vậy mà chỉ dải hẹp này thôi đã đủ làm hàm mất tính lồi. Với $0.4(x_1^2 + x_2^2) + \cos(2x_1)$, vùng đỏ gồm dải giữa $|x_1| < 0.685$ và hai mép $|x_1| > 2.457$ của khung nhìn. Hàm $x_1^2 + 3x_1x_2 + x_2^2$ thì đỏ khắp khung, dù cả hai phần tử trên đường chéo của Hessian đều dương: Ma trận $\begin{bmatrix} 2 & 3 \\ 3 & 2 \end{bmatrix}$ có trị riêng $5$ và $-1$, và theo hướng $(1, -1)$ đồ thị cong xuống.

Hai hàm còn lại, $\log(e^{x_1} + e^{x_2})$ và $x_1^2/x_2$, không có điểm đỏ nào, nhưng mỗi điểm đều có một hướng với độ cong bằng 0. Ta sẽ trở lại với chúng ở mục 5.

## 3. Vì sao điều kiện đúng

Để chứng minh định lý này một cách chặt chẽ, ý tưởng trung tâm là quy bài toán nhiều biến về bài toán một biến quen thuộc thông qua kỹ thuật hạn chế lên đường thẳng. Phép chứng minh gồm hai mắt xích sau:

**Một biến.** Với hàm $g$ khả vi hai lần trên một khoảng, $g'' \ge 0$ tương đương với $g'$ không giảm. Mà $g'$ không giảm thì $g$ lồi: Lập luận trong bài tập về hàm softplus ở chủ đề trước áp dụng nguyên vẹn, vì nó chỉ dùng tính đơn điệu của đạo hàm để suy ra điều kiện bậc nhất. Ngược lại, $g$ lồi thì $g'$ không giảm theo tính đơn điệu của gradient, nên $g'' \ge 0$.

**Nhiều biến.** $f$ lồi khi và chỉ khi mọi hàm hạn chế $g(t) = f(x + tv)$ lồi. Theo trường hợp một biến, điều này tương đương với $g''(t) = v^T \nabla^2 f(x + tv) v \ge 0$ với mọi $x$, mọi $v$ và mọi $t$ hợp lệ. Vì mỗi điểm $z$ của miền xác định đều có dạng $x + tv$ với $x = z$ và $t = 0$, điều kiện đó chính là $v^T \nabla^2 f(z) v \ge 0$ với mọi $z$ và mọi $v$, tức $\nabla^2 f(z) \succeq 0$ tại mọi điểm.

## 4. Hàm bậc hai và bình phương tối thiểu

Với hàm bậc hai tổng quát $f(x) = \tfrac12 x^T P x + q^T x + r$, trong đó $P$ đối xứng, ma trận Hessian bằng $P$ tại mọi điểm. Do đó $f$ lồi khi và chỉ khi $P \succeq 0$, và lồi nghiêm ngặt khi và chỉ khi $P \succ 0$. Với hàm bậc hai, điều kiện bậc hai chính xác theo cả hai chiều, kể cả ở phần "nghiêm ngặt".

Hàm mất mát bình phương tối thiểu là trường hợp then chốt trong học máy. Khai triển

$$
\|Aw - b\|_2^2 = w^T A^T A\, w - 2 b^T A w + b^T b ,
$$

ta thấy Hessian bằng $2A^T A$. Ma trận này luôn nửa xác định dương vì $v^T A^T A v = \|Av\|_2^2 \ge 0$, nên bình phương tối thiểu **luôn** là bài toán lồi. Nó lồi nghiêm ngặt khi và chỉ khi $Av \ne 0$ với mọi $v \ne 0$, tức các cột của $A$ độc lập tuyến tính. Khi hai đặc trưng tỉ lệ với nhau, điều này không còn đúng, và hệ quả nhìn thấy được ngay trên nghiệm.

::: example Hai đặc trưng cộng tuyến và tác dụng của điều chuẩn ridge
Lấy $A = \begin{bmatrix} 1 & 2 \\ 2 & 4 \\ 3 & 6 \end{bmatrix}$, trong đó cột thứ hai gấp đôi cột thứ nhất, và $b = (1, 2, 2)$. Ta có $A^T A = \begin{bmatrix} 14 & 28 \\ 28 & 56 \end{bmatrix}$ với trị riêng $70$ và $0$. Hướng có độ cong bằng 0 là $(2, -1)$, vì $A(2, -1) = 0$: Tăng $w_1$ thêm 2 và giảm $w_2$ đi 1 không làm thay đổi dự đoán.

Hàm mất mát là một cái máng. Phương trình chuẩn $A^T A w = A^T b = (11, 22)$ rút về một phương trình $w_1 + 2w_2 = 11/14$, nên **mọi** điểm trên đường thẳng này đều tối ưu, với cùng tổng bình phương sai số $5/14 \approx 0.357$. Bộ giải trả về điểm nào là tùy cách nó được cài đặt, và các hệ số riêng lẻ không còn ý nghĩa diễn giải.

Thêm điều chuẩn ridge $\lambda \|w\|_2^2$, Hessian trở thành $2(A^T A + \lambda I)$ với trị riêng $2(70 + \lambda)$ và $2\lambda$, cả hai dương. Cái máng được uốn thành cái bát, và nghiệm trở nên duy nhất. Với $\lambda = 1$, giải $(A^T A + I) w = A^T b$ được $w = (11/71,\ 22/71) \approx (0.155,\ 0.310)$. Khi $\lambda$ giảm dần về 0, nghiệm ridge tiến về $(11/70,\ 22/70)$, điểm có chuẩn nhỏ nhất trên đường nghiệm.
:::

## 5. Cái máng xoay quanh gốc: Hàm $x^2/y$

Hàm hai biến $f(x, y) = x^2 / y$ trên nửa mặt phẳng $y > 0$ đem lại một hình ảnh trực quan rõ nét về ma trận Hessian suy biến. Tính trực tiếp,

$$
\nabla^2 f(x, y) = \frac{2}{y^3} \begin{bmatrix} y^2 & -xy \\ -xy & x^2 \end{bmatrix} = \frac{2}{y^3} \begin{bmatrix} y \\ -x \end{bmatrix} \begin{bmatrix} y \\ -x \end{bmatrix}^T \succeq 0 .
$$

Ma trận có dạng $c\,uu^T$ với $c > 0$, nên nửa xác định dương, và hàm lồi. Nhưng hạng của nó bằng 1, và hướng có độ cong bằng 0 là $(x, y)$, vuông góc với $u = (y, -x)$. Hướng $(x, y)$ chính là hướng của tia đi từ gốc qua điểm đang xét. Lý do hình học: Ta có $f(tx, ty) = t\, f(x, y)$ với mọi $t > 0$, nên dọc mỗi tia xuất phát từ gốc tọa độ, hàm số tăng tuyến tính và hoàn toàn không cong. Đồ thị là một cái máng mà đáy máng xoay quanh gốc tọa độ. Trong mô phỏng ở mục 2, chọn hàm $x_1^2/x_2$ và kéo điểm $x$ đi khắp nửa mặt phẳng trên để thấy vạch nét đứt luôn chỉ thẳng về gốc.

Hàm $\log(e^{x_1} + e^{x_2})$ có hiện tượng tương tự theo một kiểu khác. Dọc hướng $(1, 1)$, ta có $f(x + t(1, 1)) = f(x) + t$, tăng tuyến tính, nên Hessian luôn suy biến theo hướng đó. Trong bài tiếp theo, ta sẽ tính ma trận Hessian của hàm log-sum-exp ở dạng tổng quát.

## 6. Lồi nghiêm ngặt và những điều điều kiện bậc hai không nói

Nếu $\nabla^2 f(x) \succ 0$ tại mọi $x$ thì $f$ lồi nghiêm ngặt. Chiều ngược lại **không đúng**: Chẳng hạn hàm $f(x) = x^4$ lồi nghiêm ngặt nhưng $f''(0) = 0$. Lồi nghiêm ngặt chỉ cấm đồ thị chứa một đoạn thẳng, và một hàm có đạo hàm bậc hai bằng 0 tại vài điểm rời rạc vẫn không chứa đoạn thẳng nào. Với $x^4$, dây cung nối $(-1, 1)$ và $(1, 1)$ nằm ở độ cao 1, còn đồ thị tại 0 có độ cao 0.

Điều kiện bậc hai cũng im lặng trước những hàm không khả vi hai lần, và trong học máy có không ít hàm như vậy: $|x|$, $\max\{x_1, \dots, x_n\}$, ReLU, chuẩn $\ell_1$. Với chúng, ta phải dùng định nghĩa, điều kiện bậc nhất với dưới đạo hàm, hoặc các phép toán giữ tính lồi ở chủ đề sau. Ngay cả chuẩn Euclid $\|x\|_2$ cũng không khả vi tại gốc, dù ở mọi điểm khác Hessian của nó nửa xác định dương, như Bài tập 3 sẽ cho thấy.

## 7. Độ cong cho biết bài toán dễ hay khó

Ngoài câu trả lời định tính lồi hay không, ma trận Hessian còn cung cấp thông tin định lượng thực tế: Độ lớn của các trị riêng trực tiếp quyết định tốc độ hội tụ của thuật toán tối ưu.

**Lồi mạnh**: Ta định nghĩa hàm số $f$ là **lồi mạnh** (strongly convex) trên tập $S$ nếu tồn tại hằng số $m > 0$ sao cho:

$$
\nabla^2 f(x) \succeq mI \quad \text{với mọi } x \in S .
$$

Khai triển Taylor bậc hai kèm phần dư khi đó đem lại một hàm chặn dưới tốt hơn hẳn tiếp diện bậc nhất:

$$
f(y) \ge f(x) + \nabla f(x)^T (y - x) + \frac{m}{2}\|y - x\|_2^2 .
$$

Về mặt hình học, tựa phía dưới đồ thị tại mỗi điểm $x$ giờ đây là cả một mặt paraboloit tròn xoay có độ cong $m$, tạo nên một chặn dưới chặt chẽ hơn nhiều so với mặt phẳng tiếp xúc. Cực tiểu hóa vế phải theo biến $y$ bằng cách giải điều kiện đạo hàm triệt tiêu $\nabla f(x) + m(y - x) = 0$, tức chọn $y = x - \frac{1}{m}\nabla f(x)$, ta thu được bất đẳng thức chặn dưới giá trị tối ưu toàn cục $p^\star$:

$$
p^\star \ge f(x) - \frac{1}{2m}\|\nabla f(x)\|_2^2 .
$$

Ý nghĩa thực tiễn của chặn dưới này rất sâu sắc: Với hàm lồi mạnh, bất cứ khi nào độ lớn gradient $\|\nabla f(x)\|_2$ nhỏ, điểm hiện tại chắc chắn đã nằm rất gần nghiệm tối ưu toàn cục $p^\star$. Đây là bảo chứng mà tính lồi thông thường không thể mang lại. Chẳng hạn hàm $e^x$ lồi nghiêm ngặt nhưng không lồi mạnh trên toàn bộ $\mathbb{R}$, bởi vì $f''(x) = e^x \to 0$ khi $x \to -\infty$. Tại miền đó gradient tiến sát về 0 nhưng bài toán thậm chí không hề đạt cực tiểu tại bất kỳ điểm hữu hạn nào.

**Số điều kiện**: Khi hàm số vừa lồi mạnh vừa có Hessian bị chặn trên bởi $M$ (tức $\nabla^2 f(x) \preceq MI$ với $M \ge m > 0$), tỉ số $\kappa = M/m \ge 1$ được gọi là **số điều kiện** (condition number). Đại lượng này đo lường độ lệch cong giữa các hướng, hay mức độ dẹt của các tập mức: Đường mức của một hàm bậc hai với hai trị riêng $m$ và $M$ là hình ellipse có tỉ số độ dài hai bán trục chính là $\sqrt{\kappa}$.

Xét mô hình tối ưu hàm bậc hai $f(x) = \tfrac12 (x_1^2 + \gamma x_2^2)$ bằng phương pháp gradient descent với bước nhảy tìm kiếm chính xác theo tia (exact line search). Khi xuất phát từ $(\gamma, 1)$, sau mỗi bước lặp $k$, khoảng cách sai số giá trị mục tiêu $f(x^{(k)}) - p^\star$ bị thu hẹp đúng một hệ số không đổi $\big((\gamma - 1)/(\gamma + 1)\big)^2$:

| $\gamma$ | Hệ số giảm sai số mỗi bước | Số bước để sai số giảm $10^6$ lần |
| --- | --- | --- |
| 10 | 0.669 | 35 |
| 100 | 0.961 | 346 |

Cùng là một cái bát, nhưng bát càng dẹt thì phương pháp gradient càng đi zíc zắc và càng chậm. Đây là một trong những lý do người ta chuẩn hóa thang đo của các đặc trưng trước khi huấn luyện mô hình: Đưa các đặc trưng về cùng thang đo thường làm Hessian của hàm mất mát bớt lệch giữa các hướng.

## 8. Những câu hỏi để đào sâu

**Câu 1.** Hàm $f(x) = \tfrac12 x^T P x$ với $P = \begin{bmatrix} 1 & 2 \\ 2 & 1 \end{bmatrix}$ có mọi phần tử của $P$ đều dương. Hàm có lồi không?

<details><summary>Xem lời giải thích</summary>

Không. Phần tử dương không có nghĩa là ma trận nửa xác định dương. $P$ có trị riêng $3$ và $-1$, với vector riêng ứng với $-1$ là $(1, -1)/\sqrt2$. Theo hướng đó, $v^T P v = \tfrac12(1 - 4 + 1) = -1 < 0$, đồ thị cong xuống, và $f$ là một cái yên ngựa. Điều ngược lại cũng đúng: Ma trận $\begin{bmatrix} 2 & -1 \\ -1 & 2 \end{bmatrix}$ có phần tử âm nhưng xác định dương.

</details>

**Câu 2.** Xét quy trình kiểm tra ma trận đối xứng $2 \times 2$ dạng $\begin{bmatrix} a & b \\ b & c \end{bmatrix}$ bằng hai điều kiện $a \ge 0$ và $ac - b^2 \ge 0$, rồi kết luận ma trận nửa xác định dương. Cách kiểm tra này tồn tại lỗ hổng nào?

<details><summary>Xem lời giải thích</summary>

Lỗ hổng xuất hiện khi $a = 0$. Xét ma trận $\begin{bmatrix} 0 & 0 \\ 0 & -1 \end{bmatrix}$, ma trận này thỏa mãn $a = 0 \ge 0$ và $ac - b^2 = 0 \ge 0$, nhưng với vector $v = (0, 1)$ thì $v^T X v = -1 < 0$. Đối với ma trận đối xứng cỡ $2 \times 2$, điều kiện cần và đủ để nửa xác định dương là cả **ba** bất đẳng thức $a \ge 0$, $c \ge 0$ và $ac - b^2 \ge 0$. Khi chỉ cần ma trận xác định dương ($X \succ 0$) thì hai điều kiện $a > 0$ và $ac - b^2 > 0$ là đủ, bởi vì khi đó $c > b^2/a \ge 0$ là hệ quả tất yếu. Sự khác biệt giữa "nửa xác định" và "xác định" ở đây là một cái bẫy kinh điển mà người học rất dễ mắc phải.

</details>

**Câu 3.** Hàm $e^x$ lồi nghiêm ngặt trên $\mathbb{R}$. Nó có lồi mạnh không, và câu trả lời liên quan gì tới chuyện phương pháp gradient có thể "dừng" ở đâu?

<details><summary>Xem lời giải thích</summary>

Không lồi mạnh, vì không có $m > 0$ nào để $e^x \ge m$ với mọi $x$. Cận $p^\star \ge f(x) - \|\nabla f(x)\|^2/(2m)$ vì thế không áp dụng được. Với $e^x$, tại $x = -10$ đạo hàm chỉ khoảng $4.5 \times 10^{-5}$, nhỏ đến mức một tiêu chí dừng kiểu "gradient đủ nhỏ" sẽ cho dừng, dù bài toán không có nghiệm và hàm vẫn còn giảm được nữa. Lồi mạnh là điều kiện bảo đảm rằng gradient nhỏ thật sự có nghĩa là gần tối ưu.

</details>

**Câu 4.** Trong ví dụ hai đặc trưng cộng tuyến ở mục 4, nếu chỉ cần dự đoán tốt trên dữ liệu đã có, việc nghiệm không duy nhất có gây hại gì không? Còn khi cần đọc ý nghĩa của từng hệ số thì sao?

<details><summary>Xem lời giải thích</summary>

Về dự đoán thì không hại: Mọi nghiệm trên đường $w_1 + 2w_2 = 11/14$ cho cùng vector dự đoán $Aw = \tfrac{11}{14}(1, 2, 3)$, nên cùng sai số. Nhưng khi đọc hệ số thì có vấn đề lớn. Nghiệm $(11/14,\ 0)$ nói chỉ đặc trưng thứ nhất quan trọng, nghiệm $(0,\ 11/28)$ nói chỉ đặc trưng thứ hai quan trọng, và cả hai đều tối ưu như nhau. Một thay đổi nhỏ trong dữ liệu có thể đẩy bộ giải từ nghiệm này sang nghiệm kia. Hessian suy biến báo trước điều đó, và điều chuẩn ridge là một cách chọn ra một nghiệm ổn định.

</details>

## 9. Bài tập tự luyện

::: exercise 1. Kiểm tra bằng Hessian
Hàm $f(x, y) = x^2 - 2xy + 4y^2 + e^x$ có lồi trên $\mathbb{R}^2$ không? Có lồi nghiêm ngặt không?
:::

::: solution
$\nabla^2 f = \begin{bmatrix} 2 + e^x & -2 \\ -2 & 8 \end{bmatrix}$. Phần tử đầu dương, và định thức bằng $8(2 + e^x) - 4 = 12 + 8e^x > 0$. Hai điều kiện $a > 0$ và định thức dương cho Hessian xác định dương tại mọi điểm, nên $f$ lồi nghiêm ngặt.
:::

::: exercise 2. Một hàm không lồi với hai cực tiểu toàn cục
Cho $f(x, y) = x^4 + y^4 - 4xy$. (a) Tính Hessian và tìm tập điểm mà Hessian nửa xác định dương. Tập đó có lồi không? (b) Tìm mọi điểm dừng và phân loại chúng. (c) Chỉ ra trực tiếp một dây cung vi phạm định nghĩa hàm lồi.
:::

::: solution
(a) $\nabla^2 f = \begin{bmatrix} 12x^2 & -4 \\ -4 & 12y^2 \end{bmatrix}$. Hai phần tử đường chéo luôn không âm, nên Hessian nửa xác định dương khi và chỉ khi $144x^2y^2 \ge 16$, tức $|xy| \ge 1/3$. Tập này gồm bốn miền nằm ngoài các nhánh hyperbol $xy = \pm 1/3$, không lồi, và không chứa gốc tọa độ. Vậy $f$ không lồi.

(b) $\nabla f = (4x^3 - 4y,\ 4y^3 - 4x) = 0$ cho $y = x^3$ và $x = y^3 = x^9$, nên $x \in \{0, 1, -1\}$. Ba điểm dừng là $(0, 0)$, $(1, 1)$ và $(-1, -1)$. Tại gốc, Hessian $\begin{bmatrix} 0 & -4 \\ -4 & 0 \end{bmatrix}$ có trị riêng $\pm 4$, đó là điểm yên ngựa. Tại $(\pm 1, \pm 1)$, Hessian $\begin{bmatrix} 12 & -4 \\ -4 & 12 \end{bmatrix}$ có trị riêng $8$ và $16$, đó là cực tiểu cục bộ với $f = -2$. Vì $f \to \infty$ khi $\|(x, y)\| \to \infty$, cực tiểu toàn cục tồn tại và phải là một điểm dừng, nên cả hai điểm $(1, 1)$ và $(-1, -1)$ đều là cực tiểu toàn cục.

(c) Trung điểm của hai cực tiểu là gốc tọa độ, với $f(0, 0) = 0$, trong khi trung bình của hai giá trị là $-2$. Đồ thị tại trung điểm nằm trên dây cung, trái với định nghĩa. Một hàm lồi không thể có hai cực tiểu toàn cục tách rời với một "bướu" ở giữa, vì tập các cực tiểu của hàm lồi là một tập lồi.
:::

::: exercise 3. Hessian của chuẩn Euclid
Cho $f(x) = \|x\|_2$ trên $\mathbb{R}^n$. (a) Với $x \ne 0$, chứng minh $\nabla f(x) = x / \|x\|_2$ và $\nabla^2 f(x) = \big(I - uu^T\big) / \|x\|_2$ với $u = x / \|x\|_2$. (b) Tìm các trị riêng của Hessian và hướng có độ cong bằng 0. Giải thích hướng đó bằng hình học. (c) Vì sao điều kiện bậc hai không đủ để kết luận $f$ lồi trên $\mathbb{R}^n$, và ta kết luận bằng cách nào?
:::

::: solution
(a) $\partial \|x\|_2 / \partial x_i = x_i / \|x\|_2$. Đạo hàm tiếp theo $x_j$ cho $\delta_{ij}/\|x\|_2 - x_i x_j / \|x\|_2^3$, tức $\nabla^2 f(x) = \big(I - xx^T/\|x\|_2^2\big)/\|x\|_2$. (b) $I - uu^T$ là phép chiếu lên siêu phẳng vuông góc với $u$, có trị riêng 1 (bội $n - 1$) và 0 (theo hướng $u$). Vậy Hessian có trị riêng $1/\|x\|_2$ bội $n - 1$ và trị riêng 0 theo hướng $x$. Lý do tương tự hàm $x^2/y$: Ta có $f(tx) = t f(x)$ với $t > 0$, nên dọc theo tia từ gốc tọa độ qua điểm $x$, hàm chuẩn tăng tuyến tính và hoàn toàn không cong. Đồ thị của $\|x\|_2$ là một mặt nón tròn xoay. (c) Gốc tọa độ thuộc miền xác định nhưng $f$ không khả vi tại đó, nên định lý không áp dụng trên toàn $\mathbb{R}^n$. Ta kết luận bằng định nghĩa: Bất đẳng thức tam giác và tính thuần nhất cho

$$
\|\theta x + (1-\theta)y\|_2 \le \theta\|x\|_2 + (1-\theta)\|y\|_2,
$$

như đã thực hiện ở chủ đề về chuẩn.
:::

## Tóm tắt

Hàm khả vi hai lần trên miền lồi là lồi khi và chỉ khi Hessian nửa xác định dương tại mọi điểm. Dạng toàn phương $v^T \nabla^2 f(x) v$ là độ cong của đồ thị khi đi qua $x$ theo hướng $v$, và nó là trung bình có trọng số của các trị riêng. Dấu các trị riêng cho biết quanh $x$ đồ thị là cái bát, cái máng, cái yên ngựa hay cái bát úp, và chỉ cần một vùng nhỏ có trị riêng âm là hàm mất tính lồi.

Bình phương tối thiểu luôn lồi vì Hessian $2A^TA \succeq 0$, nhưng chỉ lồi nghiêm ngặt khi các cột của $A$ độc lập. Đặc trưng cộng tuyến tạo ra cái máng và vô số nghiệm, còn điều chuẩn ridge uốn nó thành cái bát. Hessian xác định dương suy ra lồi nghiêm ngặt nhưng không ngược lại, như $x^4$ cho thấy. Cuối cùng, lồi mạnh và số điều kiện $M/m$ cho biết gradient nhỏ có nghĩa là gần tối ưu hay không, và phương pháp gradient chạy nhanh hay chậm.

## Tài liệu tham khảo

- Stephen Boyd, Lieven Vandenberghe, *Convex Optimization*, Cambridge University Press.
