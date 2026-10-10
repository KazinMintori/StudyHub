---
course: toan-cho-ai
lecture: bai-01-nhap-mon-toi-uu
topic: chuan-va-non-chuan
section: topic
title: "Quả cầu chuẩn và nón chuẩn"
description: "Bốn tiên đề của chuẩn và các chuẩn ℓ1, ℓ2, ℓ∞, ℓp, chuẩn bậc hai. Vì sao quả cầu chuẩn lồi và liên hệ của điều đó với bất đẳng thức tam giác. Nón chuẩn, nón bậc hai, mẹo nâng chiều, và vì sao góc nhọn của quả cầu ℓ1 tạo ra nghiệm thưa."
---

Ở chủ đề trước, "khoảng cách" luôn là khoảng cách Euclid, đo bằng thước thẳng. Nhưng trong tối ưu và học máy, ta thường đo độ lớn của vector theo những cách khác. Tổng giá trị tuyệt đối các thành phần đo "tổng lượng thay đổi", thành phần lớn nhất đo "trường hợp tệ nhất", còn chuẩn Euclid đo "năng lượng". Mỗi cách đo cho một hình dạng quả cầu khác nhau: Hình thoi, hình tròn, hình vuông.

Có hai câu hỏi dẫn đường cho phần này. Thứ nhất, vì sao quả cầu của **mọi** chuẩn đều lồi, và vì sao chính tính lồi ấy là điều phân biệt một chuẩn thật sự với một công thức trông giống chuẩn. Thứ hai, làm thế nào để biến bán kính của quả cầu thành một biến, và vì sao mẹo đó lại sinh ra một trong những nón quan trọng nhất của tối ưu: Nón bậc hai.

## 1. Chuẩn là gì

Một **chuẩn** (norm) trên $\mathbb{R}^n$ là một hàm số $\|\cdot\| : \mathbb{R}^n \to \mathbb{R}$ thỏa mãn trọn vẹn bốn tiên đề toán học sau:

1. Tính không âm: Ta luôn có $\|x\| \ge 0$ với mọi vector $x$.
2. Tính xác định: Ta có $\|x\| = 0$ khi và chỉ khi $x = 0$.
3. Tính thuần nhất tuyệt đối: Ta có $\|\alpha x\| = |\alpha|\, \|x\|$ với mọi số thực $\alpha$ và vector $x$.
4. Bất đẳng thức tam giác: Ta có $\|x + y\| \le \|x\| + \|y\|$ với mọi vector $x, y$.

Ba tính chất đầu nói rằng chuẩn hành xử như một "độ dài": Chỉ vector 0 có độ dài 0, và kéo dài vector gấp đôi thì độ dài gấp đôi. Tính chất thứ tư nói rằng đi đường vòng qua một điểm trung gian không bao giờ ngắn hơn đi thẳng. Như ta sẽ thấy ở mục 3, tính chất thứ tư mới là tính chất có nội dung hình học sâu nhất.

Những chuẩn quen thuộc nhất là họ chuẩn $\ell_p$ với $p \ge 1$:

$$
\|x\|_p = \left(|x_1|^p + |x_2|^p + \cdots + |x_n|^p\right)^{1/p},
$$

trong đó ba trường hợp đặc biệt có tên riêng: $\|x\|_1 = \sum_i |x_i|$, chuẩn Euclid $\|x\|_2 = \sqrt{\sum_i x_i^2}$, và $\|x\|_\infty = \max_i |x_i|$, chính là giới hạn của $\|x\|_p$ khi $p \to \infty$. Với $x = (1, -2, 2)$, ta có $\|x\|_1 = 5$, $\|x\|_2 = 3$ và $\|x\|_\infty = 2$.

Còn một họ chuẩn nữa cần nhớ: **Chuẩn bậc hai** $\|x\|_P = \sqrt{x^T P x}$ với $P \succ 0$. Quả cầu đơn vị của nó là $\{x : x^T P x \le 1\}$, chính là ellipsoid với ma trận $P^{-1}$ ở chủ đề trước. Nói cách khác, mỗi ellipsoid có tâm ở gốc là quả cầu đơn vị của một chuẩn.

Lưu ý về quy ước ký hiệu: Trong bài giảng này và toàn bộ môn học, ký hiệu $\|\cdot\|$ khi không kèm chỉ số dưới được hiểu là **một chuẩn bất kỳ**, không mặc định thu hẹp ở chuẩn Euclid. Mọi kết luận viết với $\|\cdot\|$ đều có giá trị tổng quát cho mọi chuẩn hợp lệ.

## 2. Quả cầu chuẩn luôn lồi

> **Mệnh đề.** Với mọi chuẩn $\|\cdot\|$, mọi tâm $x_c$ và mọi $r \ge 0$, **quả cầu chuẩn** $\{x : \|x - x_c\| \le r\}$ là tập lồi.

Chứng minh y hệt quả cầu Euclid, vì chứng minh đó chỉ dùng bất đẳng thức tam giác và tính thuần nhất, hai tính chất mà mọi chuẩn đều có. Với $\|x_1 - x_c\| \le r$, $\|x_2 - x_c\| \le r$ và $0 \le \theta \le 1$,

$$
\|\theta x_1 + (1-\theta)x_2 - x_c\| \le \theta\|x_1 - x_c\| + (1-\theta)\|x_2 - x_c\| \le r .
$$

Trong mặt phẳng, ba quả cầu đơn vị quen thuộc có ba hình dạng đặc trưng: Tập $\{|x_1| + |x_2| \le 1\}$ là một hình thoi với bốn đỉnh trên hai trục tọa độ, tập $\{x_1^2 + x_2^2 \le 1\}$ là hình tròn, và tập $\{\max(|x_1|, |x_2|) \le 1\}$ là hình vuông. Mô phỏng trực quan cho phép trượt giá trị $p$ liên tục và quan sát hình thoi phình dần thành hình tròn rồi tiến tới hình vuông.

<NormBallLab />

Hình cũng cho thấy một chuỗi bất đẳng thức đáng nhớ. Quả cầu $\ell_1$ nằm trong quả cầu $\ell_2$, quả cầu $\ell_2$ nằm trong quả cầu $\ell_\infty$. Vì quả cầu nhỏ hơn ứng với chuẩn lớn hơn, ta có $\|x\|_\infty \le \|x\|_2 \le \|x\|_1$. Ngược lại, các chuẩn này không thể chênh nhau quá nhiều: $\|x\|_1 \le \sqrt{n}\,\|x\|_2 \le n\,\|x\|_\infty$. Với $x = (1, -2, 2)$, chuỗi này là $2 \le 3 \le 5 \le 3\sqrt3 \approx 5.2 \le 6$.

## 3. Vì sao $p < 1$ không cho một chuẩn

Biểu thức $\left(\sum_{i=1}^n |x_i|^p\right)^{1/p}$ vẫn hoàn toàn xác định với $0 < p < 1$. Vậy vì sao trong toán học người ta chỉ công nhận nó là chuẩn khi $p \ge 1$? Khi trượt $p$ xuống dưới 1 trong mô phỏng, trực giác hình học hiện lên rõ ràng: "Quả cầu" bị lõm vào giữa bốn đỉnh và **không còn lồi**. Với $p = \tfrac12$, hai điểm $(1, 0)$ và $(0, 1)$ có "độ dài" bằng 1, nhưng trung điểm $(\tfrac12, \tfrac12)$ có giá trị $(\sqrt{0.5} + \sqrt{0.5})^2 = 2 > 1$.

Không lồi và vi phạm bất đẳng thức tam giác là hai mặt của cùng một hiện tượng. Cụ thể, xét phản ví dụ số học: $\|(1, 0) + (0, 1)\|_{1/2} = (1 + 1)^2 = 4$, lớn hơn tổng $\|(1, 0)\|_{1/2} + \|(0, 1)\|_{1/2} = 2$. Tổng quát hơn, có một mối liên hệ hai chiều đẹp đẽ:

- Nếu hàm $\|\cdot\|$ thỏa ba tính chất đầu, thì bất đẳng thức tam giác đúng **khi và chỉ khi** quả cầu đơn vị $\{x : \|x\| \le 1\}$ lồi.
- Ngược lại, mỗi tập lồi, đóng, bị chặn, đối xứng qua gốc và chứa gốc ở phần trong là quả cầu đơn vị của đúng một chuẩn, cho bởi $\|x\| = \inf\{t > 0 : x/t \in B\}$.

Chiều thứ nhất chứng minh không khó. Giả sử quả cầu đơn vị $B$ lồi, và lấy $x, y \ne 0$. Hai vector $\tfrac{x}{\|x\|}$ và $\tfrac{y}{\|y\|}$ thuộc $B$. Đặt $\theta = \tfrac{\|x\|}{\|x\| + \|y\|} \in [0, 1]$, ta có

$$
\frac{x + y}{\|x\| + \|y\|} = \theta \frac{x}{\|x\|} + (1 - \theta)\frac{y}{\|y\|} \in B ,
$$

nên $\left\|\tfrac{x + y}{\|x\| + \|y\|}\right\| \le 1$, và dùng tính thuần nhất thì được $\|x + y\| \le \|x\| + \|y\|$. Chiều thứ hai là nội dung của **hàm Minkowski**, ta chỉ phát biểu. Kết luận của cả hai chiều có thể tóm thành một câu: Chuẩn và tập lồi đối xứng là hai cách nói về cùng một thứ. Đây là ví dụ đầu tiên trong môn học cho thấy tính lồi nằm ngay trong định nghĩa của khái niệm "độ dài", chứ không phải một điều kiện kỹ thuật gắn thêm từ bên ngoài.

## 4. Góc của quả cầu $\ell_1$ và nghiệm thưa

Hình dạng của quả cầu chuẩn không phải chuyện thẩm mỹ, nó quyết định nghiệm của bài toán tối ưu. Xét bài toán tìm điểm gần $y = (2, 1)$ nhất trong một quả cầu đơn vị:

$$
\text{minimize}\quad \|x - y\|_2^2 \quad \text{subject to}\quad \|x\| \le 1 .
$$

Với quả cầu Euclid, nghiệm là $\tfrac{y}{\|y\|_2} = (0.894, 0.447)$: Cả hai thành phần đều khác 0. Với quả cầu $\ell_1$, nghiệm là $(1, 0)$, đúng một đỉnh của hình thoi, với thành phần thứ hai **bằng 0**. Hình ảnh giải thích vì sao: Các đường đồng mức của $\|x - y\|_2^2$ là những hình tròn đồng tâm tại $y$, và hình tròn nhỏ nhất chạm vào hình thoi thường chạm ở một đỉnh nhọn, vì đỉnh "nhô ra" về phía $y$ nhiều nhất. Các đỉnh của quả cầu $\ell_1$ nằm trên các trục tọa độ, tức là ở những điểm có nhiều thành phần bằng 0.

Hiện tượng nghiệm rơi vào đỉnh giải thích vì sao chuẩn $\ell_1$ được dùng để tìm **nghiệm thưa** trong thống kê và học máy, chẳng hạn trong hồi quy LASSO, nơi người ta muốn mô hình chỉ dùng một số ít đặc trưng. Cần nói cẩn thận: "Thường chạm ở đỉnh" là một cách hình dung, không phải định lý. Có những vị trí của $y$ mà nghiệm nằm trên một cạnh và không thưa. Nhưng các vùng của $y$ cho nghiệm ở đỉnh chiếm phần lớn, và chúng càng lớn khi số chiều tăng.

## 5. Nón chuẩn: Biến bán kính thành biến

Một quả cầu chuẩn có bán kính $r$ cố định. Nếu muốn coi bán kính là một biến, ta xét tập trong không gian lớn hơn một chiều:

> **Định nghĩa.** **Nón chuẩn** gắn với chuẩn $\|\cdot\|$ là $C = \{(x, t) : \|x\| \le t\} \subseteq \mathbb{R}^{n+1}$.

Đúng như tên gọi, $C$ là một nón lồi. Nó là nón vì nếu $\|x\| \le t$ và $\theta \ge 0$ thì $\|\theta x\| = \theta\|x\| \le \theta t$. Nó lồi vì với $(x, t), (y, s) \in C$ và $\theta \in [0, 1]$, bất đẳng thức tam giác cho $\|\theta x + (1-\theta) y\| \le \theta t + (1 - \theta)s$. Lát cắt của nón tại độ cao $t = c \ge 0$ chính là quả cầu chuẩn bán kính $c$, nên nón chuẩn là "chồng" tất cả các quả cầu chuẩn với bán kính tăng dần theo độ cao.

Với chuẩn Euclid, nón chuẩn được gọi là **nón bậc hai** (second-order cone), và nó còn có tên nón Lorentz hay **nón kem** vì hình dạng của nó trong $\mathbb{R}^3$:

$$
\mathcal{Q} = \{(x, t) \in \mathbb{R}^{n+1} : \|x\|_2 \le t\}.
$$

Điểm $(3, 4, 5)$ nằm đúng trên biên của $\mathcal{Q} \subseteq \mathbb{R}^3$ vì $\sqrt{9 + 16} = 5$. Ta cũng có thể biểu diễn nón bậc hai bằng bất đẳng thức bậc hai $x^T x - t^2 \le 0$ kết hợp với điều kiện không âm $t \ge 0$. Tên gọi "nón bậc hai" bắt nguồn từ chính dạng toàn phương này. Điều kiện $t \ge 0$ mang tính quyết định: Thiếu nó, tập nghiệm $\{x^T x \le t^2\}$ sẽ bao gồm cả phần nón đối xứng ngược phía dưới và đánh mất hoàn toàn tính lồi.

<Cone3DLab type="soc" />

Vì sao nâng chiều lại có ích? Một ràng buộc như $\|Ax + b\|_2 \le c^T x + d$, trong đó vế phải là một hàm affine của biến, trông không giống quả cầu nào cả, vì "bán kính" thay đổi theo $x$. Nhưng nó nói đúng một điều: Điểm $(Ax + b,\ c^T x + d)$ thuộc nón bậc hai. Tập các $x$ thỏa điều kiện là ảnh ngược của nón bậc hai qua một ánh xạ affine, và như chủ đề về các phép toán giữ tính lồi sẽ cho thấy, ảnh ngược affine của một tập lồi là lồi. Những bài toán có ràng buộc loại này được gọi là quy hoạch nón bậc hai (SOCP), một họ bài toán lồi giải được hiệu quả mà Lecture 02 sẽ giới thiệu.

Nón chuẩn của $\ell_1$ và $\ell_\infty$ là những đa diện, vì các quả cầu $\ell_1$, $\ell_\infty$ có hữu hạn mặt phẳng. Nón bậc hai thì không: Biên tròn của nó cần vô số siêu phẳng tựa. Đó là lý do SOCP thật sự rộng hơn quy hoạch tuyến tính.

## 6. Những câu hỏi để đào sâu

**Câu 1.** Tập $\{x \in \mathbb{R}^2 : \|x\|_{1/2} \le 1\}$ không lồi. Nó có tính chất yếu hơn nào không? Chẳng hạn, đoạn nối gốc tọa độ với một điểm bất kỳ của tập có nằm trong tập không?

<details><summary>Xem lời giải thích</summary>

Có. Biểu thức $\left(\sum_i |x_i|^p\right)^{1/p}$ vẫn thuần nhất với mọi $p > 0$, nên nếu $x$ thuộc tập thì $\theta x$ cũng thuộc tập với mọi $\theta \in [0, 1]$. Một tập có tính chất "mọi đoạn nối từ một điểm cố định tới các điểm của tập đều nằm trong tập" được gọi là tập hình sao đối với điểm đó. Mọi tập lồi chứa gốc đều hình sao đối với gốc, nhưng tập hình sao chưa chắc lồi. Quả cầu $\ell_{1/2}$ là ví dụ điển hình.

</details>

**Câu 2.** Trong mô phỏng, quả cầu $\ell_p$ luôn đi qua bốn điểm $(\pm 1, 0)$ và $(0, \pm 1)$ với mọi $p$. Vì sao? Với $p$ nào thì quả cầu đi qua điểm $(\tfrac12, \tfrac12)$?

<details><summary>Xem lời giải thích</summary>

Với $x = (1, 0)$, ta có $\|x\|_p = (1^p + 0)^{1/p} = 1$ với mọi $p$, nên bốn điểm đó luôn trên biên. Điểm $(\tfrac12, \tfrac12)$ nằm trên biên khi $2 \cdot (\tfrac12)^p = 1$, tức $(\tfrac12)^{p} = \tfrac12$, nghĩa là $p = 1$. Với $p > 1$, điểm này nằm bên trong. Với $p < 1$, nó nằm bên ngoài, đúng là chỗ quả cầu bị lõm.

</details>

**Câu 3.** Ellipsoid $\{x : (x - x_c)^T P^{-1}(x - x_c) \le 1\}$ và quả cầu chuẩn có phải là hai loại tập hoàn toàn khác nhau không?

<details><summary>Xem lời giải thích</summary>

Không hẳn. Ellipsoid đó chính là quả cầu bán kính 1, tâm $x_c$, của chuẩn bậc hai $\|z\|_{P^{-1}} = \sqrt{z^T P^{-1} z}$. Vì vậy mọi ellipsoid không suy biến đều là một quả cầu chuẩn. Điều ngược lại sai: Quả cầu $\ell_1$ hay $\ell_\infty$ có góc nhọn nên không phải ellipsoid. Ellipsoid là những quả cầu của các chuẩn "đến từ một tích vô hướng".

</details>

**Câu 4.** Tập $\{(x, t) : \|x\|_2^2 \le t\}$ có lồi không? Nó có phải nón không? So sánh với nón bậc hai.

<details><summary>Xem lời giải thích</summary>

Tập này là epigraph của hàm $\|x\|_2^2$, một hàm lồi, nên lồi (chủ đề về epigraph sẽ chứng minh điều này). Nhưng nó không phải nón: Điểm $(x, t) = (1, 1)$ thuộc tập, còn $2\cdot(1, 1) = (2, 2)$ thì không, vì $4 > 2$. Lát cắt tại độ cao $t$ của nó là quả cầu bán kính $\sqrt t$, nên nó có hình một cái bát parabol chứ không phải hình nón. Nón bậc hai dùng $\|x\|_2$ chứ không dùng $\|x\|_2^2$, và chính tính thuần nhất bậc một của chuẩn làm cho nó thành nón.

</details>

## 7. Bài tập tự luyện

::: exercise 1. So sánh các chuẩn
Với $x = (2, -1, 0, 2)$, tính $\|x\|_1$, $\|x\|_2$, $\|x\|_\infty$ và kiểm tra chuỗi $\|x\|_\infty \le \|x\|_2 \le \|x\|_1 \le \sqrt{n}\, \|x\|_2$.
:::

::: solution
$\|x\|_1 = 2 + 1 + 0 + 2 = 5$, $\|x\|_2 = \sqrt{4 + 1 + 0 + 4} = 3$, $\|x\|_\infty = 2$. Với $n = 4$, $\sqrt{n}\,\|x\|_2 = 6$. Chuỗi là $2 \le 3 \le 5 \le 6$, đúng.
:::

::: exercise 2. Quả cầu ℓ1 là một đa diện
Viết quả cầu $\{x \in \mathbb{R}^2 : \|x\|_1 \le 1\}$ dưới dạng một hệ bất đẳng thức tuyến tính. Trong $\mathbb{R}^n$, cần bao nhiêu bất đẳng thức nếu viết theo cách tương tự?
:::

::: solution
$|x_1| + |x_2| \le 1$ tương đương bốn bất đẳng thức $\pm x_1 \pm x_2 \le 1$ với mọi cách chọn dấu, vì $|x_1| + |x_2| = \max_{s_1, s_2 = \pm 1}(s_1 x_1 + s_2 x_2)$. Trong $\mathbb{R}^n$, cách viết này cần $2^n$ bất đẳng thức $s^T x \le 1$ với $s \in \{-1, 1\}^n$. Ngược lại, quả cầu $\ell_\infty$ chỉ cần $2n$ bất đẳng thức $\pm x_i \le 1$. Chủ đề về đa diện sẽ cho thấy mỗi đa diện có hai cách mô tả với kích thước có thể chênh nhau rất xa.
:::

::: exercise 3. Một ràng buộc nón bậc hai
Viết tập $\{x \in \mathbb{R}^2 : \sqrt{(x_1 - 1)^2 + x_2^2} \le x_1 + 1\}$ dưới dạng ảnh ngược của nón bậc hai qua một ánh xạ affine. Điểm $(0, 0)$ và $(0, 2)$ có thuộc tập không?
:::

::: solution
Điều kiện nói rằng $(x_1 - 1,\ x_2,\ x_1 + 1)$ thuộc $\mathcal{Q} \subseteq \mathbb{R}^3$, tức tập là ảnh ngược của $\mathcal{Q}$ qua ánh xạ affine $x \mapsto (x_1 - 1, x_2, x_1 + 1)$. Với $(0, 0)$: Vế trái $\sqrt{1} = 1$, vế phải $1$, nên điểm nằm trên biên. Với $(0, 2)$: Vế trái $\sqrt{1 + 4} = \sqrt5 \approx 2.24$, vế phải $1$, nên điểm không thuộc tập. Bình phương hai vế (hợp lệ khi $x_1 + 1 \ge 0$) cho $x_2^2 \le 4x_1$, một miền parabol lồi.
:::

## Tóm tắt

Một chuẩn thỏa bốn tính chất, và quả cầu của mọi chuẩn đều lồi nhờ bất đẳng thức tam giác cùng tính thuần nhất. Ngược lại, với một hàm thuần nhất dương, bất đẳng thức tam giác tương đương với tính lồi của quả cầu đơn vị, nên công thức $\ell_p$ với $p < 1$ không phải chuẩn. Các quả cầu $\ell_1$, $\ell_2$, $\ell_\infty$ có hình thoi, hình tròn, hình vuông, lồng vào nhau theo chuỗi $\|x\|_\infty \le \|x\|_2 \le \|x\|_1$. Góc của quả cầu $\ell_1$ nằm trên các trục, là lý do chuẩn $\ell_1$ thường cho nghiệm thưa.

Nón chuẩn $\{(x, t) : \|x\| \le t\}$ là nón lồi, có các lát cắt ngang là quả cầu chuẩn. Với chuẩn Euclid ta được nón bậc hai, và mọi ràng buộc dạng $\|Ax + b\|_2 \le c^T x + d$ là ảnh ngược affine của nó.

## Tài liệu tham khảo

- Stephen Boyd, Lieven Vandenberghe, *Convex Optimization*, Cambridge University Press.
