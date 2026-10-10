---
course: toan-cho-ai
lecture: bai-01-nhap-mon-toi-uu
topic: ham-loi
section: topic
title: "Hàm lồi và bất đẳng thức dây cung"
description: "Định nghĩa hàm lồi, lồi nghiêm ngặt, lõm và affine cùng ý nghĩa hình học của dây cung. Vì sao miền xác định phải lồi, cách kiểm tra tính lồi bằng cách hạn chế lên đường thẳng, mở rộng giá trị và hàm chỉ thị của một tập."
---

Các bài học trước đã trang bị cho ta bức tranh hình học toàn cảnh về **tập lồi**: Miền không gian mà đoạn thẳng nối hai điểm bất kỳ không bao giờ chệch ra ngoài. Tuy nhiên, một bài toán tối ưu hoàn chỉnh luôn bao gồm miền khả thi và hàm mục tiêu. Câu hỏi tiếp theo mang tính quyết định: Một **hàm số lồi** (convex function) cần được định nghĩa như thế nào để toàn bộ những tính chất tối ưu hoàn mỹ của tập lồi được kế thừa trọn vẹn?

Trọng tâm câu trả lời nằm ở công cụ hình học trực quan: Khảo sát vị trí tương đối giữa đồ thị hàm số và đoạn thẳng dây cung nối hai điểm bất kỳ. Sau khi phân tích định nghĩa và bản chất giải tích của từng giả thiết, ta sẽ tiếp cận kỹ thuật hạn chế hàm số lên một đường thẳng, chuyển hóa bài toán tối ưu đa chiều về các bài toán một chiều đơn giản. Cuối bài là kỹ thuật mở rộng miền giá trị và hàm chỉ thị, công cụ đại số giúp tích hợp trọn vẹn miền ràng buộc vào bên trong hàm mục tiêu.

## 1. Định nghĩa

> **Định nghĩa.** Hàm số $f : \mathbb{R}^n \to \mathbb{R}$ được gọi là **hàm lồi** (convex function) nếu miền xác định $\operatorname{dom} f$ là một tập lồi trong $\mathbb{R}^n$, và với mọi cặp điểm $x, y \in \operatorname{dom} f$ cùng mọi hệ số $\theta \in [0, 1]$, ta luôn có bất đẳng thức dây cung:
> $$f(\theta x + (1 - \theta) y) \le \theta f(x) + (1 - \theta) f(y).$$

Hai vế của bất đẳng thức mô tả hai quá trình tính toán hoàn toàn khác nhau:
- Vế trái thực hiện **tổ hợp các đầu vào trước rồi mới tính giá trị hàm**: Lấy điểm trung gian $z = \theta x + (1-\theta)y$ trên đoạn nối $x$ và $y$, sau đó tính $f(z)$.
- Vế phải thực hiện **tính giá trị hàm tại hai đầu mút trước rồi mới lấy tổ hợp giá trị**: Lấy trung bình gia quyền của hai số thực $f(x)$ và $f(y)$.

Hàm lồi là hàm số mà giá trị tính sau khi trộn đầu vào không bao giờ vượt quá giá trị trộn sau khi tính hàm.

Về mặt hình học, xét hai điểm $A(x, f(x))$ và $B(y, f(y))$ trên đồ thị của $f$. Đoạn thẳng nối $A$ và $B$ được gọi là **dây cung** (chord). Dây cung đi qua điểm $(z,\ \theta f(x) + (1-\theta) f(y))$ nằm ngay phía trên điểm tọa độ $z$. Bất đẳng thức dây cung khẳng định: Tại mọi điểm $z$ nằm giữa $x$ và $y$, đồ thị hàm số luôn nằm **phía dưới hoặc tiếp xúc** với dây cung. Trực giác trực quan giống như một lòng chảo ngửa: Căng một sợi chỉ nối hai điểm bất kỳ trên vành chảo, sợi chỉ luôn lơ lửng phía trên lòng chảo.

<FunctionLab type="chord" />

Trong mô phỏng tương tác trên, đối với các hàm lồi như $x^2$, $|x|$, $e^x$, $-\ln x$, đoạn thẳng nối từ đồ thị lên dây cung luôn mang màu xanh dương (đồ thị nằm dưới dây cung). Ngược lại, với các hàm không lồi như $x^3$ hay $0.3x^2 + \sin(1.5x)$, ta dễ dàng tìm được những cặp điểm $a, b$ làm đồ thị võng ngược lên phía trên dây cung. Để bác bỏ tính lồi, chỉ cần chỉ ra duy nhất một cặp điểm vi phạm; nhưng để khẳng định tính lồi, ta phải chứng minh bất đẳng thức đúng với mọi cặp điểm và mọi hệ số $\theta \in [0, 1]$.

::: example Chứng minh tính lồi của hàm bậc hai f(x) = x² bằng định nghĩa
Với hàm $f(x) = x^2$ trên $\mathbb{R}$, ta xét hiệu số giữa vế phải và vế trái:

$$
\theta x^2 + (1 - \theta) y^2 - \big(\theta x + (1-\theta) y\big)^2 = \theta(1 - \theta)(x - y)^2 .
$$

Đẳng thức trên được kiểm chứng dễ dàng bằng khai triển đại số: Sử dụng các biến đổi $\theta - \theta^2 = \theta(1-\theta)$ và $(1-\theta) - (1-\theta)^2 = \theta(1-\theta)$, vế trái được viết lại thành:

$$
\begin{aligned}
&\theta x^2 + (1-\theta)y^2 - \theta^2 x^2 - 2\theta(1-\theta)xy - (1-\theta)^2 y^2 \\
&\quad = \theta(1-\theta)\,\big(x^2 - 2xy + y^2\big) = \theta(1-\theta)(x - y)^2.
\end{aligned}
$$

Vì $\theta \in [0, 1]$ nên $\theta(1-\theta) \ge 0$, và bình phương $(x - y)^2 \ge 0$, do đó hiệu số luôn không âm. Biểu thức này còn cho ta biết chính xác khoảng cách độ cao từ đồ thị tới dây cung tại điểm $z$ đúng bằng $\theta(1-\theta)(x-y)^2$.
:::

## 2. Những điều kiện giải tích cốt lõi

- **Miền xác định bắt buộc phải là tập lồi**: Đây là điều kiện tiên quyết mang tính sống còn. Nếu $\operatorname{dom} f$ không lồi, tồn tại cặp điểm $x, y \in \operatorname{dom} f$ sao cho điểm trung gian $z = \theta x + (1-\theta) y$ rơi ra ngoài miền xác định, khiến vế trái $f(z)$ không xác định. Xét hàm số $f(x) = 1/x^2$ trên miền $\mathbb{R} \setminus \{0\}$: Mặc dù đạo hàm cấp hai $f''(x) = 6/x^4 > 0$ tại mọi $x \ne 0$, hàm số này **không phải là hàm lồi** vì miền xác định của nó bị đứt gãy tại gốc tọa độ. Khi chọn $a < 0 < b$, đoạn thẳng $[a, b]$ đi qua điểm gián đoạn $0$.
- **Hàm lồi nghiêm ngặt (Strictly convex)**: Hàm $f$ được gọi là lồi nghiêm ngặt nếu bất đẳng thức dây cung trở thành bất đẳng thức ngặt ($<$) với mọi $x \ne y$ và $\theta \in (0, 1)$. Về hình học, đồ thị nằm hoàn toàn phía dưới dây cung, chỉ chạm dây cung tại đúng hai đầu mút. Hàm $x^2$ là hàm lồi nghiêm ngặt vì tích $\theta(1-\theta)(x-y)^2 > 0$ khi $x \ne y$ và $\theta \in (0, 1)$. Ngược lại, hàm giá trị tuyệt đối $|x|$ hay hàm kích hoạt ReLU $\max\{0, x\}$ là các hàm lồi nhưng không lồi nghiêm ngặt, vì trên các miền đơn điệu chúng suy biến thành đường thẳng, nơi dây cung trùng khít với đồ thị.
- **Hàm lõm và hàm affine**: Hàm số $f$ được gọi là **hàm lõm** (concave function) nếu $-f$ là hàm lồi, tương đương với việc đồ thị luôn nằm phía trên mọi dây cung (như một lòng chảo úp). Đối với hàm affine $f(x) = a^T x + b$, bất đẳng thức dây cung luôn trở thành đẳng thức với mọi $\theta$. Do đó mọi hàm affine vừa là hàm lồi vừa là hàm lõm. Đặc biệt, ta có khẳng định giải tích đảo: Một hàm số vừa lồi vừa lõm khi và chỉ khi nó là một hàm affine.
- **Tính liên tục tự nhiên**: Một định lý giải tích cơ bản khẳng định rằng: Mọi hàm lồi đều liên tục trên phần trong tương đối của miền xác định, và chỉ có thể gián đoạn tại biên tương đối. Một hàm lồi không thể xuất hiện các bước nhảy gián đoạn ở giữa miền xác định, bởi bất kỳ bước nhảy nào cũng sẽ làm đồ thị vượt lên trên dây cung nối hai điểm lân cận.

## 3. Tiêu chuẩn kiểm tra tính lồi trên từng đường thẳng

Định nghĩa hàm lồi chỉ dựa vào đoạn thẳng nối hai điểm bất kỳ. Do đó, toàn bộ thông tin về tính lồi của hàm đa biến $f : \mathbb{R}^n \to \mathbb{R}$ đều được phản ánh trọn vẹn trên các đường thẳng 1 chiều cắt qua miền xác định. Ta hệ thống hóa nguyên lý này thành tiêu chuẩn hạn chế trên đường thẳng:

> **Mệnh đề (Tiêu chuẩn hạn chế trên đường thẳng).** Hàm số $f$ là hàm lồi khi và chỉ khi với mọi điểm $x \in \operatorname{dom} f$ và mọi hướng vector $v \in \mathbb{R}^n$, hàm số một biến
> $$g(t) = f(x + tv)$$
> là hàm lồi trên miền xác định $\{t \in \mathbb{R} : x + tv \in \operatorname{dom} f\}$.

Chứng minh:
- Chiều thuận: Đoạn thẳng trên trục $t$ tương ứng trực tiếp với đoạn thẳng của $f$ trên đường thẳng $x + tv$. Miền của $g$ là giao của một đường thẳng với tập lồi $\operatorname{dom} f$ nên là một khoảng lồi trong $\mathbb{R}$.
- Chiều nghịch: Mọi cặp điểm $x, y \in \operatorname{dom} f$ đều nằm trên đường thẳng đi qua $x$ với hướng $v = y - x$. Bất đẳng thức dây cung của $f$ cho cặp điểm $x, y$ chính là bất đẳng thức dây cung của hàm một biến $g(t)$ tại hai điểm $t = 0$ và $t = 1$.

Tiêu chuẩn này có giá trị ứng dụng thực tiễn to lớn: Nó chuyển hóa việc kiểm tra tính lồi của hàm đa biến phức tạp về việc khảo sát đạo hàm cấp hai của hàm một biến theo tham số $t$. Kỹ thuật này sẽ được dùng để chứng minh tính lõm của hàm $\log\det X$ trên nón ma trận đối xứng xác định dương.

<Restrict2DLab />

Trong mô phỏng 2D trên: Với hàm yên ngựa $f(x_1, x_2) = x_1^2 - x_2^2$, hàm hạn chế $g(t)$ cong lên khi đường thẳng nghiêng về trục hoành nhưng cong xuống khi nghiêng về trục tung. Chỉ cần tồn tại duy nhất một hướng đường thẳng làm $g(t)$ cong xuống là đủ để bác bỏ tính lồi của $f$.

## 4. Mở rộng giá trị và hàm chỉ thị của tập lồi

Để tránh việc lặp lại điều kiện ràng buộc "với mọi $x \in \operatorname{dom} f$", giải tích lồi sử dụng quy ước mở rộng miền giá trị: **Hàm mở rộng** $\tilde f : \mathbb{R}^n \to \mathbb{R} \cup \{+\infty\}$ của hàm lồi $f$ được định nghĩa bởi:

$$
\tilde f(x) = \begin{cases} f(x), & \text{nếu } x \in \operatorname{dom} f, \\ +\infty, & \text{nếu } x \notin \operatorname{dom} f. \end{cases}
$$

Miền xác định gốc được khôi phục dễ dàng qua tập mức: $\operatorname{dom} f = \{x \in \mathbb{R}^n : \tilde f(x) < +\infty\}$. Với quy ước số học mở rộng ($a + \infty = +\infty$ và $0 \cdot \infty = 0$), bất đẳng thức dây cung áp dụng tự nhiên cho mọi $x, y \in \mathbb{R}^n$: Nếu một trong hai điểm nằm ngoài $\operatorname{dom} f$, vế phải bằng $+\infty$ và bất đẳng thức hiển nhiên nghiệm đúng. Trong toàn bộ môn học, ta mặc định mọi hàm lồi đều được mở rộng tự nhiên như vậy.

Một ứng dụng nền tảng của kỹ thuật này là **hàm chỉ thị** (indicator function) của một tập hợp $C \subseteq \mathbb{R}^n$:

$$
I_C(x) = \begin{cases} 0, & \text{nếu } x \in C, \\ +\infty, & \text{nếu } x \notin C. \end{cases}
$$

Hàm chỉ thị $I_C$ là hàm lồi khi và chỉ khi tập hợp $C$ là tập lồi. Hàm chỉ thị cho phép chuyển đổi một bài toán tối ưu có ràng buộc thành bài toán tối ưu không ràng buộc tương đương: Bài toán cực tiểu hóa hàm mục tiêu $f(x)$ trên tập khả thi $C$ hoàn toàn đồng nhất với bài toán cực tiểu hóa không ràng buộc của hàm mục tiêu tổng hợp $f(x) + I_C(x)$ trên toàn bộ không gian $\mathbb{R}^n$.

Bất kỳ nghiệm thử nào vi phạm ràng buộc ($x \notin C$) đều bị phạt với chi phí vô hạn $+\infty$. Trong học máy, khi thay thế hình phạt vô hạn tuyệt đối này bằng một hàm phạt hữu hạn liên tục (như $\tfrac{\rho}{2}\|x\|_2^2$ hay $\rho\|x\|_1$), ta thu được các bài toán điều chuẩn (regularization) kinh điển như Ridge Regression hay Lasso.

## 5. Những câu hỏi để đào sâu

**Câu 1.** Một sinh viên lập luận: "Hàm $f(x) = x^3$ là hàm lồi, bởi vì nhánh đồ thị bên phải của nó cong lên phía trên." Lập luận này đúng ở điểm nào và sai lầm bản chất ở điểm nào?

<details><summary>Xem lời giải thích</summary>

Lập luận trên đúng một phần: Khi thu hẹp trên nửa trục không âm $\mathbb{R}_+ = [0, +\infty)$, đạo hàm cấp hai $f''(x) = 6x \ge 0$, do đó $f(x) = x^3$ là một hàm lồi trên miền $[0, +\infty)$.

Sai lầm bản chất là việc kết luận nó lồi trên toàn bộ trục số $\mathbb{R}$. Chọn hai điểm $x = -2$, $y = 0$ và $\theta = \tfrac{1}{2}$: Điểm giữa là $z = -1$ có giá trị hàm $f(-1) = -1$. Trong khi đó giá trị trên dây cung là $\tfrac{1}{2}(-8) + \tfrac{1}{2}(0) = -4$. Ta nhận thấy $f(z) = -1 > -4$, vi phạm hoàn toàn bất đẳng thức dây cung. Tính lồi là thuộc tính của một **cặp đôi** gồm hàm số và miền xác định cụ thể của nó.

</details>

**Câu 2.** Nếu $f$ là hàm lồi và hằng số $c > 0$, hàm số $f(cx)$ có lồi không? Các hàm $f(x) + c$, $f(x + c)$ thì sao? Trường hợp $c \cdot f(x)$ với $c < 0$ thì sao?

<details><summary>Xem lời giải thích</summary>

Cả ba hàm $f(cx)$, $f(x) + c$ và $f(x + c)$ đều là các hàm lồi:
- Hàm $f(cx)$ và $f(x + c)$ là phép hợp của hàm lồi $f$ với một ánh xạ affine của biến $x$. Vì ánh xạ affine bảo toàn tổ hợp lồi của các điểm, tính lồi được giữ nguyên.
- Hàm $f(x) + c$ chỉ đơn thuần cộng cùng một hằng số $c$ vào cả hai vế của bất đẳng thức dây cung ($\theta c + (1-\theta)c = c$).

Trái lại, khi $c < 0$, hàm số $c f(x)$ trở thành một **hàm lõm**, bởi vì việc nhân cả hai vế của bất đẳng thức với một số âm sẽ làm đảo chiều hoàn toàn bất đẳng thức.

</details>

**Câu 3.** Hàm số $f(x) = \min\{x^2, 1\}$ có phải là hàm lồi trên $\mathbb{R}$ không? Hãy kiểm tra bằng một dây cung cụ thể.

<details><summary>Xem lời giải thích</summary>

Hàm số này không phải là hàm lồi. Chọn hai điểm $x = 0$ và $y = 2$ cùng hệ số $\theta = \tfrac{1}{2}$: Điểm giữa $z = 1$ có giá trị hàm $f(1) = \min\{1^2, 1\} = 1$. Giá trị trên dây cung tương ứng là $\tfrac{1}{2}f(0) + \tfrac{1}{2}f(2) = \tfrac{1}{2}(0) + \tfrac{1}{2}(1) = 0.5$. Ta có $f(1) = 1 > 0.5$, vi phạm bất đẳng thức dây cung.

Về hình học, đồ thị là một đường parabol bị cắt cụt ở ngưỡng trần 1, tạo ra hai góc uốn lõm tại $x = \pm 1$. Phép lấy giá trị nhỏ nhất ($\min$) của hai hàm lồi nói chung phá hủy tính lồi, trong khi phép lấy giá trị lớn nhất ($\max$) luôn bảo toàn tính lồi.

</details>

**Câu 4.** Sử dụng hàm chỉ thị, hãy viết bài toán tối ưu có ràng buộc $\min \|x\|_2^2$ với điều kiện $Ax = b$ thành bài toán không ràng buộc. Hàm mục tiêu mới có tính chất gì?

<details><summary>Xem lời giải thích</summary>

Bài toán được viết lại thành: $\min_{x \in \mathbb{R}^n} \left(\|x\|_2^2 + I_C(x)\right)$, trong đó tập khả thi $C = \{x \in \mathbb{R}^n : Ax = b\}$.

Hàm mục tiêu mới là tổng của hai hàm lồi (hàm bình phương chuẩn $\|x\|_2^2$ lồi ngặt và hàm chỉ thị $I_C$ lồi do tập affine $C$ lồi), do đó nó là một hàm lồi mở rộng. Tuy nhiên, hàm số này không khả vi trên toàn không gian và nhận giá trị $+\infty$ tại mọi điểm nằm ngoài $C$.

</details>

## 6. Bài tập tự luyện

::: exercise 1. Chứng minh tính lồi của hàm giá trị tuyệt đối bằng định nghĩa
Chứng minh rằng hàm số $f(x) = |x|$ là hàm lồi trên $\mathbb{R}$ trực tiếp từ định nghĩa. Hàm số này có lồi nghiêm ngặt hay không?
:::

::: solution
Với mọi $x, y \in \mathbb{R}$ và mọi hệ số $\theta \in [0, 1]$, áp dụng bất đẳng thức tam giác của giá trị tuyệt đối ta có:

$$
|\theta x + (1-\theta)y| \le |\theta x| + |(1-\theta)y| = \theta|x| + (1-\theta)|y|,
$$

trong đó đẳng thức thứ hai đúng vì $\theta \ge 0$ và $1-\theta \ge 0$. Do đó $f(x) = |x|$ là một hàm lồi.

Hàm số này không lồi nghiêm ngặt: Chọn $x = 1, y = 2$ và $\theta = \tfrac{1}{2}$, ta tính được $f(1.5) = 1.5$ và $\tfrac{1}{2}f(1) + \tfrac{1}{2}f(2) = 1.5$. Hai vế bằng nhau dù hai điểm phân biệt và $\theta \in (0, 1)$.
:::

::: exercise 2. Xác định dây cung vi phạm tính lồi và tính lõm
Chứng minh hàm số $f(x) = \sin x$ trên đoạn $[0, 2\pi]$ không phải là hàm lồi và cũng không phải là hàm lõm bằng cách chỉ ra các dây cung vi phạm tương ứng.
:::

::: solution
- Bác bỏ tính lồi: Chọn $x = 0, y = \pi$ và $\theta = \tfrac{1}{2}$. Ta có điểm giữa $z = \pi/2$ với $f(\pi/2) = \sin(\pi/2) = 1$. Giá trị dây cung là $\tfrac{1}{2}\sin(0) + \tfrac{1}{2}\sin(\pi) = 0$. Vì $1 > 0$ nên đồ thị nằm phía trên dây cung, vi phạm tính lồi.
- Bác bỏ tính lõm: Chọn $x = \pi, y = 2\pi$ và $\theta = \tfrac{1}{2}$. Ta có điểm giữa $z = 3\pi/2$ với $f(3\pi/2) = -1$. Giá trị dây cung là $\tfrac{1}{2}\sin(\pi) + \tfrac{1}{2}\sin(2\pi) = 0$. Vì $-1 < 0$ nên đồ thị nằm phía dưới dây cung, vi phạm tính lõm.
:::

::: exercise 3. Khảo sát tính lồi qua hạn chế trên đường thẳng
Cho hàm số hai biến $f(x_1, x_2) = x_1 x_2$ trên $\mathbb{R}^2$. Hãy tính hàm một biến $g(t) = f(x + tv)$ với điểm mốc $x = (0, 0)^T$ và hướng $v = (1, -1)^T$. Rút ra kết luận về tính lồi của $f$.
:::

::: solution
Với $x = (0, 0)^T$ và $v = (1, -1)^T$, điểm trên đường thẳng có tọa độ $x + tv = (t, -t)^T$. Hàm hạn chế nhận dạng:

$$
g(t) = f(t, -t) = (t)(-t) = -t^2 .
$$

Hàm số $g(t) = -t^2$ có đạo hàm cấp hai $g''(t) = -2 < 0$, do đó nó là một hàm lõm nghiêm ngặt trên $\mathbb{R}$. Theo tiêu chuẩn hạn chế trên đường thẳng, sự xuất hiện của một hướng làm hàm số lõm ngặt chứng minh rằng $f(x_1, x_2) = x_1 x_2$ không phải là hàm lồi trên $\mathbb{R}^2$. Ma trận Hessian của hàm số là $\begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}$, có hai giá trị riêng là $+1$ và $-1$, sinh ra bề mặt yên ngựa kinh điển.
:::

## Tóm tắt

Một hàm số là hàm lồi khi miền xác định của nó là một tập lồi và đồ thị hàm số nằm phía dưới hoặc tiếp xúc với mọi dây cung nối hai điểm bất kỳ. Hàm lồi nghiêm ngặt loại trừ các đoạn thẳng phẳng trên đồ thị. Hàm lõm là hàm có số đối là hàm lồi, và lớp hàm duy nhất vừa lồi vừa lõm chính là các hàm affine.

Tính lồi của một hàm đa biến tương đương với tính lồi của hàm một biến thu được khi hạn chế hàm số lên mọi đường thẳng cắt qua miền xác định. Kỹ thuật mở rộng giá trị với $+\infty$ và hàm chỉ thị của tập lồi cho phép quy đổi các bài toán tối ưu có ràng buộc về bài toán tối ưu không ràng buộc tương đương, đặt nền móng cho các thuật toán tối ưu hóa hiện đại.

## Tài liệu tham khảo
- Stephen Boyd, Lieven Vandenberghe, *Convex Optimization*, Cambridge University Press.

