---
course: toan-cho-ai
lecture: bai-01-nhap-mon-toi-uu
topic: chuan-va-non-chuan
section: topic
title: "Quả cầu chuẩn và nón chuẩn"
description: "Bốn tiên đề của chuẩn và các chuẩn ℓ1, ℓ2, ℓ∞, ℓp, chuẩn bậc hai. Vì sao quả cầu chuẩn lồi và liên hệ của điều đó với bất đẳng thức tam giác. Nón chuẩn, nón bậc hai, mẹo nâng chiều, và vì sao góc nhọn của quả cầu ℓ1 tạo ra nghiệm thưa."
---

Trong hình học Euclid cổ điển, khoảng cách giữa hai điểm luôn được đo bằng thước thẳng theo đường chim bay. Thế nhưng trong tối ưu hóa và học máy, ta cần định lượng kích thước của vector theo nhiều góc độ khác nhau: Tổng giá trị tuyệt đối đo "tổng chi phí tài nguyên biến động", giá trị tuyệt đối lớn nhất đo "kịch bản rủi ro tồi tệ nhất", còn chuẩn Euclid đo "mức năng lượng vật lý". Mỗi cách đo đạc đó tạo nên một quả cầu đơn vị với hình dáng hình học đặc trưng riêng biệt: Hình thoi, hình tròn, hay hình vuông.

Chủ đề này tập trung giải đáp hai câu hỏi nền tảng:
1. Vì sao quả cầu của **mọi** chuẩn toán học hợp lệ bắt buộc phải là một tập lồi, và vì sao tính lồi chính là ranh giới phân định một chuẩn thực thụ với các biểu thức đo lường phi chuẩn?
2. Làm thế nào để biến bán kính của quả cầu thành một biến số tối ưu, và vì sao kỹ thuật nâng chiều đó lại dẫn tới cấu trúc nón bậc hai, một trong những công cụ mạnh mẽ nhất của quy hoạch lồi hiện đại?

## 1. Định nghĩa chuẩn và các họ chuẩn quen thuộc

Một **chuẩn** (norm) trên không gian vector $\mathbb{R}^n$ là một hàm số $\|\cdot\| \colon \mathbb{R}^n \to \mathbb{R}$ thỏa mãn trọn vẹn bốn tiên đề toán học sau:

1. **Tính không âm**: Ta luôn có $\|x\| \ge 0$ với mọi vector $x \in \mathbb{R}^n$.
2. **Tính xác định**: Ta có $\|x\| = 0$ khi và chỉ khi vector $x = 0$.
3. **Tính thuần nhất tuyệt đối**: Ta có $\|\alpha x\| = |\alpha|\, \|x\|$ với mọi số thực vô hướng $\alpha \in \mathbb{R}$ và mọi vector $x \in \mathbb{R}^n$.
4. **Bất đẳng thức tam giác**: Ta có $\|x + y\| \le \|x\| + \|y\|$ với mọi vector $x, y \in \mathbb{R}^n$.

Ba tính chất đầu tiên xác lập hành vi tự nhiên của một thước đo độ dài: Vector không là đối tượng duy nhất có độ dài bằng 0, và khi kéo dãn vector lên bao nhiêu lần thì độ dài tăng lên bấy nhiêu lần. Tiên đề thứ tư, bất đẳng thức tam giác, khẳng định rằng đường đi thẳng nối trực tiếp hai điểm luôn là con đường ngắn nhất, không thể dài hơn đường đi vòng qua một điểm trung gian. Đây cũng chính là tính chất quyết định tính lồi của hình học không gian.

Các chuẩn xuất hiện phổ biến nhất trong tối ưu hóa thuộc họ chuẩn $\ell_p$ với tham số $p \ge 1$:

$$
\|x\|_p = \left(\sum_{i=1}^n |x_i|^p\right)^{1/p} = \left(|x_1|^p + |x_2|^p + \dots + |x_n|^p\right)^{1/p} ,
$$

trong đó ba trường hợp đặc biệt được ứng dụng rộng rãi nhất gồm:
- **Chuẩn $\ell_1$** (tổng khoảng cách Manhattan):
  $$
  \|x\|_1 = \sum_{i=1}^n |x_i| = |x_1| + |x_2| + \dots + |x_n| .
  $$
- **Chuẩn Euclid $\ell_2$**:
  $$
  \|x\|_2 = \sqrt{\sum_{i=1}^n x_i^2} = \sqrt{x_1^2 + x_2^2 + \dots + x_n^2} .
  $$
- **Chuẩn cực đại $\ell_\infty$** (chuẩn Chebyshev, ứng với giới hạn khi $p \to \infty$):
  $$
  \|x\|_\infty = \max_{1 \le i \le n} |x_i| = \max\{|x_1|, |x_2|, \dots, |x_n|\} .
  $$

Xét vector $x = (1, -2, 2) \in \mathbb{R}^3$, các chuẩn tương ứng cho kết quả cụ thể: $\|x\|_1 = |1| + |-2| + |2| = 5$, $\|x\|_2 = \sqrt{1^2 + (-2)^2 + 2^2} = \sqrt{9} = 3$, và $\|x\|_\infty = \max\{1, 2, 2\} = 2$.

Một họ chuẩn quan trọng khác là **chuẩn bậc hai** $\|x\|_P = \sqrt{x^T P x}$ gắn với ma trận đối xứng xác định dương $P \succ 0$. Quả cầu đơn vị của chuẩn bậc hai là $\{x \in \mathbb{R}^n \mid x^T P x \le 1\}$, chính là một ellipsoid tâm tại gốc tọa độ với ma trận định hình $P^{-1}$. Như vậy, mỗi ellipsoid không suy biến tâm tại gốc đều là quả cầu đơn vị của một chuẩn bậc hai tương ứng.

Quy ước ký hiệu: Ký hiệu $\|\cdot\|$ khi không kèm chỉ số dưới được hiểu là một chuẩn hợp lệ bất kỳ trên $\mathbb{R}^n$. Mọi định lý phát biểu với $\|\cdot\|$ đều có giá trị tổng quát cho toàn bộ các chuẩn toán học.

## 2. Quả cầu chuẩn luôn là tập lồi

> **Mệnh đề.** Với mọi chuẩn $\|\cdot\|$, mọi tâm $x_c \in \mathbb{R}^n$ và mọi bán kính $r \ge 0$, **quả cầu chuẩn** đóng
> $$
> B(x_c, r) = \{x \in \mathbb{R}^n \mid \|x - x_c\| \le r\}
> $$
> luôn là một tập lồi.

Chứng minh mệnh đề này hoàn toàn tương tự như trường hợp quả cầu Euclid, bởi suy luận chỉ đòi hỏi bất đẳng thức tam giác và tính thuần nhất tuyệt đối của chuẩn. Lấy hai điểm bất kỳ $x_1, x_2 \in B(x_c, r)$ và hệ số $\theta \in [0, 1]$, ta có:

$$
\begin{aligned}
\|\theta x_1 + (1-\theta)x_2 - x_c\| &= \|\theta (x_1 - x_c) + (1-\theta)(x_2 - x_c)\| \\
&\le \|\theta (x_1 - x_c)\| + \|(1-\theta)(x_2 - x_c)\| \\
&= \theta \|x_1 - x_c\| + (1-\theta)\|x_2 - x_c\| \\
&\le \theta r + (1-\theta)r = r .
\end{aligned}
$$

Trong mặt phẳng $\mathbb{R}^2$, ba quả cầu đơn vị quen thuộc mang ba hình thái hình học đặc trưng:
- Quả cầu $\ell_1$ là hình thoi có bốn đỉnh nằm trên hai trục tọa độ: $\{x \in \mathbb{R}^2 \mid |x_1| + |x_2| \le 1\}$.
- Quả cầu $\ell_2$ là hình tròn trơn hoàn hảo: $\{x \in \mathbb{R}^2 \mid x_1^2 + x_2^2 \le 1\}$.
- Quả cầu $\ell_\infty$ là hình vuông có các cạnh song song với các trục tọa độ: $\{x \in \mathbb{R}^2 \mid \max(|x_1|, |x_2|) \le 1\}$.

Mô phỏng trực quan dưới đây cho phép thay đổi tham số $p$ liên tục và quan sát quá trình biến dạng hình học: Hình thoi phình dần thành hình tròn rồi tiệm cận tới hình vuông.

<NormBallLab />

Mô phỏng này còn làm sáng tỏ chuỗi bất đẳng thức hình học: Quả cầu $\ell_1$ nằm lọt trong quả cầu $\ell_2$, và quả cầu $\ell_2$ lại nằm lọt trong quả cầu $\ell_\infty$. Vì quả cầu nhỏ hơn đòi hỏi điều kiện ràng buộc ngặt nghèo hơn, ta thu được chuỗi bất đẳng thức chuẩn ngược chiều:

$$
\|x\|_\infty \le \|x\|_2 \le \|x\|_1 .
$$

Đồng thời, các chuẩn trên không gian hữu hạn chiều luôn tương đương và bị chặn lẫn nhau:

$$
\|x\|_1 \le \sqrt{n}\,\|x\|_2 \le n\,\|x\|_\infty .
$$

Với vector $x = (1, -2, 2) \in \mathbb{R}^3$, chuỗi bất đẳng thức này thể hiện bằng số học: $2 \le 3 \le 5 \le 3\sqrt{3} \approx 5.20 \le 6$.

## 3. Vì sao tham số $p < 1$ không tạo thành chuẩn

Biểu thức đại số $\left(\sum_{i=1}^n |x_i|^p\right)^{1/p}$ vẫn hoàn toàn tính toán được khi $0 < p < 1$. Vậy vì sao trong toán học người ta kiên quyết không công nhận nó là một chuẩn?

Khi giảm giá trị $p$ xuống dưới 1 trong mô phỏng, trực giác hình học bộc lộ ngay nguyên nhân: Các cạnh của quả cầu bị uốn cong lõm vào phía trong, khiến quả cầu **mất hoàn toàn tính lồi**. Với $p = \tfrac12$, xét hai điểm đơn vị $x = (1, 0)$ và $y = (0, 1)$: Hai điểm này có "độ dài" theo công thức bằng 1, nhưng trung điểm của chúng là $(\tfrac12, \tfrac12)$ lại có giá trị:

$$
\left(\sqrt{0.5} + \sqrt{0.5}\right)^2 = \left(2\sqrt{0.5}\right)^2 = 4 \cdot 0.5 = 2 > 1 .
$$

Trung điểm bị bật ra ngoài quả cầu, chứng minh tập hợp không lồi. Đồng thời, công thức này vi phạm nghiêm trọng bất đẳng thức tam giác:

$$
\|x + y\|_{1/2} = \|(1, 1)\|_{1/2} = 4 > 2 = \|(1, 0)\|_{1/2} + \|(0, 1)\|_{1/2} .
$$

Hiện tượng quả cầu không lồi và sự vi phạm bất đẳng thức tam giác là hai mặt tương đương của cùng một quy luật toán học:

> **Định lý.** Cho hàm số $\|\cdot\|$ thỏa mãn tính không âm, tính xác định và tính thuần nhất tuyệt đối. Khi đó, hàm số thỏa mãn bất đẳng thức tam giác **khi và chỉ khi** quả cầu đơn vị $B = \{x \in \mathbb{R}^n \mid \|x\| \le 1\}$ là một tập lồi.

Chứng minh chiều thuận: Giả sử quả cầu đơn vị $B$ là tập lồi. Lấy hai vector tùy ý $x, y \ne 0$. Hai vector chuẩn hóa $\tfrac{x}{\|x\|}$ và $\tfrac{y}{\|y\|}$ đều có chuẩn bằng 1, tức thuộc quả cầu $B$. Đặt hệ số tổ hợp lồi $\theta = \tfrac{\|x\|}{\|x\| + \|y\|} \in [0, 1]$, ta có:

$$
\frac{x + y}{\|x\| + \|y\|} = \theta \frac{x}{\|x\|} + (1 - \theta) \frac{y}{\|y\|} \in B .
$$

Vì điểm này thuộc $B$, chuẩn của nó không vượt quá 1:

$$
\left\|\frac{x + y}{\|x\| + \|y\|}\right\| \le 1 \iff \|x + y\| \le \|x\| + \|y\| .
$$

Chiều đảo lại được bảo đảm thông qua lý thuyết **hàm phiếm hàm Minkowski**: Mỗi tập hợp đóng, bị chặn, lồi, đối xứng qua gốc tọa độ và chứa gốc tọa độ trong phần trong đều xác định duy nhất một chuẩn thông qua biểu thức $\|x\| = \inf\{t > 0 \mid x/t \in B\}$.

Kết luận sâu sắc: Khái niệm "chuẩn" và khái niệm "tập lồi đối xứng có phần trong chứa gốc" thực chất là hai cách diễn đạt cho cùng một bản chất hình học. Tính lồi không phải là một điều kiện phụ trợ được thêm vào, mà là thuộc tính nội tại cốt lõi của khái niệm khoảng cách.

## 4. Góc nhọn của quả cầu $\ell_1$ và cơ chế sinh nghiệm thưa

Sự khác biệt hình học giữa quả cầu $\ell_1$ và quả cầu $\ell_2$ quyết định trực tiếp cấu trúc nghiệm trong các bài toán học máy. Xét bài toán hình chiếu điểm $y = (2, 1)$ lên quả cầu đơn vị:

$$
\begin{aligned}
&\quad \text{Cực tiểu hóa:}\quad \|x - y\|_2^2 \\
\text{Thỏa mãn:}\quad \|x\| &\le 1 .
\end{aligned}
$$

- Với quả cầu Euclid $\|x\|_2 \le 1$, nghiệm tối ưu là điểm chiếu vuông góc:
  $$
  x^* = \frac{y}{\|y\|_2} = \left(\frac{2}{\sqrt5}, \frac{1}{\sqrt5}\right) \approx (0.894, 0.447) ,
  $$
  trong đó cả hai tọa độ đều khác 0 (nghiệm đặc).
- Với quả cầu $\ell_1$, tức $|x_1| + |x_2| \le 1$, nghiệm tối ưu lại rơi chính xác vào đỉnh nhọn $x^* = (1, 0)$, nơi tọa độ thứ hai **triệt tiêu hoàn toàn về 0** (nghiệm thưa).

Cơ chế hình học giải thích hiện tượng này: Các đường đồng mức của hàm mục tiêu $\|x - y\|_2^2$ là những đường tròn đồng tâm mở rộng từ tâm $y$. Khi mở rộng đường tròn từ $y$ về phía quả cầu, điểm tiếp xúc đầu tiên giữa đường tròn và quả cầu $\ell_1$ hầu như luôn xảy ra tại một đỉnh nhọn của hình thoi, bởi các đỉnh này nhô ra xa nhất dọc theo các trục tọa độ. Tại các đỉnh trên trục tọa độ, các thành phần tọa độ ngoài trục đều bằng 0.

Hiện tượng nghiệm rơi vào đỉnh nhọn giải thích vì sao số hạng điều chuẩn $\ell_1$ (như trong hồi quy LASSO) có khả năng **lựa chọn đặc trưng tự động** và sinh ra nghiệm thưa (sparsity). Ngược lại, quả cầu $\ell_2$ có bề mặt cong trơn hoàn hảo nên điểm tiếp xúc hầu như không bao giờ rơi trúng trục tọa độ, giữ lại toàn bộ các đặc trưng của mô hình.

## 5. Nón chuẩn và kỹ thuật nâng chiều

Một quả cầu chuẩn gắn liền với một bán kính cố định $r$. Nếu ta xem bán kính là một biến số không âm $t \ge 0$, tập hợp tạo thành trong không gian $\mathbb{R}^{n+1}$ sẽ tạo nên một cấu trúc nón:

> **Định nghĩa.** **Nón chuẩn** (norm cone) gắn với chuẩn $\|\cdot\|$ trên $\mathbb{R}^n$ là tập hợp:
> $$
> C = \{(x, t) \in \mathbb{R}^{n+1} \mid \|x\| \le t\} .
> $$

$C$ là một nón lồi thực sự:
- Tính chất nón: Nếu $(x, t) \in C$ và $\alpha \ge 0$, tính thuần nhất cho $\|\alpha x\| = \alpha \|x\| \le \alpha t$, do đó $\alpha(x, t) \in C$.
- Tính lồi: Với hai điểm $(x, t), (y, s) \in C$ và hệ số $\theta \in [0, 1]$, bất đẳng thức tam giác cho:
  $$
  \|\theta x + (1-\theta) y\| \le \theta \|x\| + (1-\theta)\|y\| \le \theta t + (1-\theta)s .
  $$

Lát cắt ngang của nón tại mỗi độ cao $t = c \ge 0$ chính là quả cầu chuẩn bán kính $c$. Nón chuẩn là phép chồng xếp liên tục của các quả cầu chuẩn có kích thước giãn nở tịnh tiến theo độ cao $t$.

Khi chuẩn được chọn là chuẩn Euclid $\|\cdot\|_2$, nón chuẩn tương ứng được gọi là **nón bậc hai** (second-order cone - SOC), hay còn gọi là nón Lorentz hoặc **nón kem**:

$$
\mathcal{Q} = \{(x, t) \in \mathbb{R}^{n+1} \mid \|x\|_2 \le t\} .
$$

Điểm $(3, 4, 5) \in \mathbb{R}^3$ nằm chính xác trên biên của nón bậc hai vì $\sqrt{3^2 + 4^2} = 5$. Ta có thể biểu diễn nón bậc hai dưới dạng bất đẳng thức toàn phương $x^T x - t^2 \le 0$ kết hợp với điều kiện bán kính không âm $t \ge 0$. Điều kiện $t \ge 0$ mang tính quyết định: Nếu thiếu nó, tập nghiệm sẽ gồm hai nón đối đỉnh ngược hướng và đánh mất hoàn toàn tính lồi.

<Cone3DLab type="soc" />

### Kỹ thuật nâng chiều trong tối ưu hóa
Kỹ thuật nón hóa có ý nghĩa thực tiễn to lớn: Xét một ràng buộc phi tuyến tính có dạng:

$$
\|Ax + b\|_2 \le c^T x + d ,
$$

trong đó vế phải thay đổi phụ thuộc vào biến quyết định $x$. Ràng buộc này thoạt nhìn không phải là một quả cầu cố định. Thế nhưng, nó tương đương chính xác với điều kiện: Vector affine $(Ax + b,\ c^T x + d)$ nằm trong nón bậc hai $\mathcal{Q}$. Tập nghiệm của $x$ chính là ảnh ngược của nón lồi $\mathcal{Q}$ qua một ánh xạ affine, do đó luôn là một tập lồi.

Các bài toán tối ưu với các ràng buộc thuộc dạng này tạo thành họ **quy hoạch nón bậc hai** (Second-Order Cone Programming - SOCP). Vì nón bậc hai có biên cong trơn và sở hữu vô số siêu phẳng tựa, SOCP mở rộng vượt bậc khả năng mô hình hóa so với quy hoạch tuyến tính (LP), đồng thời vẫn giải được với độ phức tạp đa thức thông qua phương pháp điểm trong.

## 6. Những câu hỏi để đào sâu

**Câu 1.** Tập hợp $\{x \in \mathbb{R}^2 \mid \|x\|_{1/2} \le 1\}$ không phải là tập lồi. Liệu tập này có thỏa mãn một tính chất hình học yếu hơn nào không?

<details><summary>Xem lời giải thích</summary>

Tập hợp này là một tập hình sao đối với gốc tọa độ. Do công thức $\|x\|_{1/2}$ vẫn bảo toàn tính thuần nhất đối với số vô hướng dương, nên nếu điểm $x$ thuộc tập thì mọi điểm trên đoạn nối từ gốc tới $x$, tức $\theta x$ với $\theta \in [0, 1]$, cũng thuộc tập. Mọi tập lồi chứa gốc đều là tập hình sao đối với gốc, nhưng chiều ngược lại không đúng. Quả cầu $\ell_{1/2}$ là một ví dụ mẫu mực cho tập hình sao bị lõm và không lồi.

</details>

**Câu 2.** Trong mô phỏng, quả cầu đơn vị $\ell_p$ luôn đi qua bốn điểm $(\pm 1, 0)$ và $(0, \pm 1)$ với mọi giá trị $p > 0$. Vì sao? Với giá trị $p$ nào thì quả cầu đi qua điểm $(\tfrac12, \tfrac12)$?

<details><summary>Xem lời giải thích</summary>

Với vector cơ sở $e_1 = (1, 0)$, ta có $\|e_1\|_p = (|1|^p + |0|^p)^{1/p} = 1^{1/p} = 1$ với mọi $p > 0$. Do đó bốn điểm trên trục tọa độ luôn nằm trên biên của quả cầu đơn vị với mọi $p$. Điểm $(\tfrac12, \tfrac12)$ nằm trên biên quả cầu khi và chỉ khi $2 \cdot (\tfrac12)^p = 1$, tức $(\tfrac12)^{p-1} = 1$, dẫn tới $p = 1$. Khi $p > 1$, điểm này nằm hẳn bên trong quả cầu; còn khi $p < 1$, nó nằm ra ngoài quả cầu, chính là vị trí mà quả cầu bị lõm vào trong.

</details>

**Câu 3.** Ellipsoid xác định dương $\{x \in \mathbb{R}^n \mid (x - x_c)^T P^{-1} (x - x_c) \le 1\}$ và quả cầu chuẩn có phải là hai cấu trúc hình học tách biệt không?

<details><summary>Xem lời giải thích</summary>

Không tách biệt. Mỗi ellipsoid không suy biến chính là quả cầu đơn vị tâm $x_c$ của chuẩn bậc hai $\|u\|_{P^{-1}} = \sqrt{u^T P^{-1} u}$. Do đó mọi ellipsoid đều là quả cầu của một chuẩn sinh bởi tích vô hướng. Chiều ngược lại không đúng: Quả cầu $\ell_1$ hay $\ell_\infty$ có các góc nhọn và cạnh phẳng, nên không thể biểu diễn dưới dạng một ellipsoid. Ellipsoid là lớp quả cầu trơn đặc biệt gắn liền với các phép biến đổi toàn phương.

</details>

**Câu 4.** Tập hợp $\{(x, t) \in \mathbb{R}^{n+1} \mid \|x\|_2^2 \le t\}$ có phải là tập lồi không? Tập này có phải là một nón không?

<details><summary>Xem lời giải thích</summary>

Tập hợp này là một tập lồi vì nó là epigraph của hàm toàn phương lồi $f(x) = \|x\|_2^2$. Tuy nhiên, nó không phải là một nón: Lấy điểm $(x, t) = (1, 1)$, điểm này thuộc tập vì $1^2 \le 1$. Nhưng khi nhân với hệ số vô hướng $\alpha = 2 > 0$, điểm $\alpha(x, t) = (2, 2)$ lại có $\|x\|_2^2 = 4 > 2 = t$, do đó không thuộc tập. Lát cắt ngang của tập này tại độ cao $t$ là quả cầu bán kính $\sqrt{t}$, tạo thành một hình paraboloid tròn xoay chứ không phải nón. Nón bậc hai đòi hỏi chuẩn bậc một $\|x\|_2 \le t$ để bảo đảm tính thuần nhất bậc một cần thiết cho cấu trúc nón.

</details>

## 7. Bài tập tự luyện

::: exercise 1. So sánh giá trị các chuẩn
Cho vector $x = (2, -1, 0, 2) \in \mathbb{R}^4$. Tính các chuẩn $\|x\|_1$, $\|x\|_2$, $\|x\|_\infty$ và kiểm chứng chuỗi bất đẳng thức kẹp $\|x\|_\infty \le \|x\|_2 \le \|x\|_1 \le \sqrt{n}\, \|x\|_2$.
:::

::: solution
Ta tính trực tiếp từng chuẩn:
- Chuẩn $\ell_1$: $\|x\|_1 = |2| + |-1| + |0| + |2| = 5$.
- Chuẩn $\ell_2$:
  $$
  \|x\|_2 = \sqrt{2^2 + (-1)^2 + 0^2 + 2^2} = \sqrt{4 + 1 + 0 + 4} = 3 .
  $$
- Chuẩn $\ell_\infty$: $\|x\|_\infty = \max\{|2|, |-1|, |0|, |2|\} = 2$.

Với số chiều $n = 4$, ta có $\sqrt{n}\,\|x\|_2 = \sqrt{4} \cdot 3 = 6$. Chuỗi bất đẳng thức kẹp trở thành:

$$
2 \le 3 \le 5 \le 6 ,
$$

hoàn toàn thỏa mãn.
:::

::: exercise 2. Biểu diễn quả cầu chuẩn ℓ1 qua hệ bất đẳng thức tuyến tính
Viết quả cầu đơn vị $\{x \in \mathbb{R}^2 \mid \|x\|_1 \le 1\}$ dưới dạng một hệ bất đẳng thức tuyến tính. Trong không gian $\mathbb{R}^n$, cần bao nhiêu bất đẳng thức tuyến tính để mô tả quả cầu $\ell_1$ theo cách tương tự?
:::

::: solution
Điều kiện $|x_1| + |x_2| \le 1$ tương đương với hệ bốn bất đẳng thức tuyến tính:

$$
x_1 + x_2 \le 1,\quad x_1 - x_2 \le 1,\quad -x_1 + x_2 \le 1,\quad -x_1 - x_2 \le 1 .
$$

Tổng quát trong $\mathbb{R}^n$, biểu thức chuẩn $\ell_1$ là $\max_{s \in \{-1, 1\}^n} s^T x \le 1$. Do đó cần $2^n$ bất đẳng thức tuyến tính để mô tả quả cầu $\ell_1$. Ngược lại, quả cầu $\ell_\infty$ trong $\mathbb{R}^n$ chỉ cần $2n$ bất đẳng thức tuyến tính độc lập ($-1 \le x_i \le 1$ với $i = 1, \dots, n$).
:::

::: exercise 3. Ràng buộc nón bậc hai và miền parabol
Xét tập hợp:

$$
S = \{x \in \mathbb{R}^2 \mid \sqrt{(x_1 - 1)^2 + x_2^2} \le x_1 + 1\} .
$$

Hãy viết tập $S$ dưới dạng ảnh ngược của nón bậc hai qua một ánh xạ affine. Hai điểm $x_A = (0, 0)$ và $x_B = (0, 2)$ có thuộc tập $S$ không?
:::

::: solution
Ràng buộc tương đương với điều kiện vector ba chiều $(x_1 - 1,\ x_2,\ x_1 + 1)$ nằm trong nón bậc hai $\mathcal{Q} \subseteq \mathbb{R}^3$. Do đó, tập $S$ là ảnh ngược của $\mathcal{Q}$ qua ánh xạ affine:

$$
x \mapsto \begin{bmatrix} 1 & 0 \\ 0 & 1 \\ 1 & 0 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} + \begin{bmatrix} -1 \\ 0 \\ 1 \end{bmatrix} .
$$

- Với điểm $x_A = (0, 0)$: Vế trái $\sqrt{(-1)^2 + 0^2} = 1$, vế phải $0 + 1 = 1$. Vì $1 \le 1$, điểm $x_A$ nằm trên biên của tập $S$.
- Với điểm $x_B = (0, 2)$: Vế trái $\sqrt{(-1)^2 + 2^2} = \sqrt{5} \approx 2.24$, vế phải $0 + 1 = 1$. Vì $\sqrt{5} > 1$, điểm $x_B$ nằm ngoài tập $S$.

Với điều kiện $x_1 + 1 \ge 0$, bình phương hai vế cho:

$$
(x_1 - 1)^2 + x_2^2 \le (x_1 + 1)^2 \iff x_1^2 - 2x_1 + 1 + x_2^2 \le x_1^2 + 2x_1 + 1 \iff x_2^2 \le 4x_1 ,
$$

chính là miền lồi giới hạn bởi đường parabol $x_1 \ge \tfrac{1}{4}x_2^2$.
:::

## Tóm tắt

Chuẩn toán học là thước đo độ dài vector thỏa mãn bốn tiên đề cơ bản. Quả cầu của mọi chuẩn hợp lệ luôn là một tập lồi nhờ bất đẳng thức tam giác và tính thuần nhất tuyệt đối. Ngược lại, tính lồi của quả cầu đơn vị tương đương với bất đẳng thức tam giác, giải thích vì sao biểu thức $\ell_p$ với $p < 1$ làm lõm quả cầu và không thể là chuẩn.

Các quả cầu $\ell_1$, $\ell_2$, $\ell_\infty$ lồng nhau theo chuỗi bất đẳng thức chuẩn. Các đỉnh nhọn của quả cầu $\ell_1$ nằm trên các trục tọa độ là cơ chế hình học dẫn tới sự xuất hiện của nghiệm thưa trong học máy.

Nón chuẩn $\{(x, t) \in \mathbb{R}^{n+1} \mid \|x\| \le t\}$ biến bán kính thành biến số tối ưu, tạo thành một nón lồi với các lát cắt ngang là các quả cầu chuẩn. Nón bậc hai tương ứng với chuẩn Euclid là công cụ nền tảng của quy hoạch nón bậc hai (SOCP), cho phép biểu diễn các ràng buộc khoảng cách phụ thuộc affine một cách hiệu quả và chặt chẽ.

## Tài liệu tham khảo

- Stephen Boyd, Lieven Vandenberghe, *Convex Optimization*, Cambridge University Press.
