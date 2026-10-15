---
course: toan-cho-ai
lecture: bai-01-nhap-mon-toi-uu
topic: non-loi
section: topic
title: "Nón và nón lồi"
description: "Nón, nón lồi, tổ hợp nón và bao nón, đặt cạnh nhau với bốn loại tổ hợp tuyến tính, affine, lồi và nón. Các ví dụ cơ bản và bài toán kiểm tra một vector có thuộc một nón hay không."
---

Các chủ đề trước đã giới thiệu cho chúng ta hai cách hạn chế tự nhiên lên tổ hợp tuyến tính tổng quát $\sum_{i=1}^k \theta_i x_i$. Nếu ta đòi hỏi tổng các trọng số phải bằng 1 ($\sum_{i=1}^k \theta_i = 1$), ta thu được tổ hợp affine và cấu trúc không gian affine phẳng. Nếu ta đòi hỏi thêm các trọng số không được âm ($\theta_i \ge 0$), ta thu được tổ hợp lồi và cấu trúc tập lồi. Vẫn còn một khả năng tổ hợp thứ tư mang tính đối ngẫu hình học sâu sắc mà chúng ta chưa khảo sát: Giữ nguyên điều kiện **hệ số không âm** ($\theta_i \ge 0$) nhưng **bỏ hoàn toàn** điều kiện ràng buộc tổng bằng 1.

Lựa chọn đại số dường như giản đơn này dẫn thẳng tới một đối tượng hình học nền tảng của toán học tối ưu: Khái niệm **nón** (cone) và **nón lồi** (convex cone). Nón lồi không chỉ là một dạng tập lồi đặc biệt mà còn là chiếc chìa khóa vạn năng mở ra lý thuyết bất đẳng thức tổng quát, nón đối ngẫu (dual cone), quy hoạch nón bậc hai (SOCP) và quy hoạch nửa xác định dương (SDP). Bài học này giúp bạn đọc nắm vững trực giác hình học của nón, phân biệt rạch ròi bốn loại tổ hợp toán học, giải quyết bài toán kiểm tra vector thuộc nón và nhận diện các ứng dụng hiện đại trong học máy.

## 1. Nón: Tập khép kín với phép phóng to không âm

Ta bắt đầu bằng định nghĩa hình học sơ cấp của nón trong không gian Euclid:

> **Định nghĩa.** Một tập hợp $C \subseteq \mathbb{R}^n$ được gọi là một **nón** (cone), hay tập thuần nhất không âm (nonnegative homogeneous set), nếu với mọi điểm $x \in C$ và với mọi hệ số vô hướng không âm $\theta \ge 0$, ta luôn có:
> $$
> \theta x \in C
> $$

Về mặt hình học trực quan, định nghĩa trên khẳng định rằng: Cứ khi nào một điểm $x$ thuộc nón, thì toàn bộ **tia thẳng** (ray) xuất phát từ gốc tọa độ $O$ đi qua điểm $x$ cũng phải nằm trọn vẹn bên trong nón.

Một nón khác rỗng luôn luôn chứa gốc tọa độ, vì ta luôn có thể chọn hệ số $\theta = 0$, cho ra $0 \cdot x = 0 \in C$. Hình ảnh trực quan sinh động nhất trong đời sống là một chùm sáng phát ra từ một ngọn đèn pin đặt tại gốc tọa độ: Mỗi tia sáng phát đi là một tia của nón, và toàn bộ vùng không gian được chiếu sáng vô tận chính là một nón hình học.

Cần lưu ý rằng định nghĩa nón sơ cấp **chưa hề đòi hỏi tính lồi**. Trong thực tế hình học, có vô số nón không lồi:
- Hợp của hai trục tọa độ vuông góc trong mặt phẳng $\mathbb{R}^2$: $K = \{(x_1, x_2) \mid x_1 x_2 = 0\}$. Phóng to một điểm trên trục tọa độ với $\theta \ge 0$ vẫn cho ra một điểm trên trục tọa độ, do đó đây là một nón. Tuy nhiên, tập này không lồi: Điểm $(1, 0) \in K$ và điểm $(0, 1) \in K$, nhưng trung điểm $(\tfrac{1}{2}, \tfrac{1}{2})$ rõ ràng không nằm trên bất kỳ trục tọa độ nào.
- Góc phần tư thứ nhất hợp với góc phần tư thứ ba: $K' = \{x \in \mathbb{R}^2 \mid x_1 x_2 \ge 0\}$.

Bởi vì tính lồi là linh hồn của các bài toán giải được hiệu quả, ta dành sự quan tâm đặc biệt cho lớp đối tượng giao thoa giữa hai cấu trúc này:

> **Định nghĩa.** Một tập hợp $C \subseteq \mathbb{R}^n$ được gọi là một **nón lồi** (convex cone) nếu nó vừa là một nón, vừa là một tập lồi. Điều này tương đương với mệnh đề: Với mọi cặp điểm $x_1, x_2 \in C$ và với mọi cặp hệ số không âm $\theta_1, \theta_2 \ge 0$, ta luôn có:
> $$
> \theta_1 x_1 + \theta_2 x_2 \in C
> $$

### Chứng minh tính tương đương của định nghĩa

Ta kiểm tra tính tương đương logic giữa hai phát biểu:

- **Chiều thuận ($\Rightarrow$)**: Giả sử $C$ khép kín với mọi tổ hợp $\theta_1 x_1 + \theta_2 x_2$ có hệ số không âm:
  1. Chọn $\theta_2 = 0$, ta có $\theta_1 x_1 \in C$ với mọi $\theta_1 \ge 0$, chứng minh $C$ là một nón.
  2. Chọn thêm điều kiện $\theta_1 + \theta_2 = 1$, ta có $\theta_1 x_1 + (1 - \theta_1) x_2 \in C$ với mọi $\theta_1 \in [0, 1]$, chứng minh $C$ là một tập lồi.
- **Chiều đảo ($\Leftarrow$)**: Giả sử $C$ là một nón và đồng thời là một tập lồi. Lấy $x_1, x_2 \in C$ và $\theta_1, \theta_2 \ge 0$:
  - Nếu $\theta_1 = \theta_2 = 0$, thì $\theta_1 x_1 + \theta_2 x_2 = 0 \in C$.
  - Nếu $\theta_1 + \theta_2 > 0$, ta thực hiện phép biến đổi đại số tách tổng trọng số:
    $$
    \theta_1 x_1 + \theta_2 x_2 = (\theta_1 + \theta_2) \left( \frac{\theta_1}{\theta_1 + \theta_2} x_1 + \frac{\theta_2}{\theta_1 + \theta_2} x_2 \right)
    $$
    Biểu thức trong dấu ngoặc đơn là một tổ hợp lồi của $x_1, x_2$ vì các trọng số $\tfrac{\theta_1}{\theta_1 + \theta_2}$ và $\tfrac{\theta_2}{\theta_1 + \theta_2}$ đều không âm và có tổng đúng bằng 1. Vì $C$ là tập lồi, điểm trong ngoặc thuộc $C$. Tiếp theo, vì $C$ là một nón và số nhân $(\theta_1 + \theta_2) > 0$ là không âm, tích vô hướng của toàn bộ biểu thức vẫn thuộc $C$.

Về mặt hình học, tập hợp tất cả các tổ hợp $\theta_1 x_1 + \theta_2 x_2$ với $\theta_1, \theta_2 \ge 0$ sinh bởi hai vector độc lập tuyến tính trong mặt phẳng tạo thành một **hình quạt vô hạn** (infinite wedge hay pie slice) có đỉnh đặt tại gốc tọa độ, hai mép biên là hai tia thẳng đi qua $x_1$ và $x_2$. Khác biệt căn bản với đoạn thẳng giới hạn của tập lồi, hình quạt này trải rộng vô tận ra xa vì không có bất kỳ rào cản nào giới hạn độ lớn của các hệ số $\theta_1, \theta_2$.

<ConeLab type="conic" />

## 2. Tổ hợp nón và bao nón

Mở rộng từ hai điểm sang một số hữu hạn các điểm, ta thiết lập định nghĩa tổ hợp nón chuẩn mực:

> **Định nghĩa.** Cho $k$ điểm $x_1, \ldots, x_k \in \mathbb{R}^n$. Một điểm $y$ có dạng:
> $$
> y = \sum_{i=1}^k \theta_i x_i = \theta_1 x_1 + \theta_2 x_2 + \dots + \theta_k x_k
> $$
> với tất cả các trọng số không âm ($\theta_i \ge 0, \forall i = 1, \ldots, k$) được gọi là một **tổ hợp nón** (conic combination), hay tổ hợp tuyến tính không âm.
> 
> **Bao nón** (conic hull) của một tập hợp $S \subseteq \mathbb{R}^n$, ký hiệu là $\operatorname{cone} S$, là tập hợp tất cả các tổ hợp nón của các điểm thuộc $S$:
> $$
> \operatorname{cone} S = \left\{ \sum_{i=1}^k \theta_i x_i \;\middle|\; x_i \in S, \; \theta_i \ge 0, \; k \ge 1 \right\}
> $$

Tương tự như bao lồi và bao affine, một tập hợp là nón lồi khi và chỉ khi nó chứa mọi tổ hợp nón của các điểm thuộc tập đó. Bao nón $\operatorname{cone} S$ luôn luôn là một nón lồi, và nó chính là **nón lồi nhỏ nhất chứa $S$**.

### Hiện tượng nón bùng nổ: Gốc tọa độ bị bao quanh

Trong mặt phẳng $\mathbb{R}^2$, bao nón của hai vector độc lập tuyến tính là một hình quạt có góc mở nhỏ hơn $180^\circ$. Khi ta thêm vào vector thứ ba, điều gì sẽ xảy ra?

Nếu các vector được phân bố sao cho gốc tọa độ $O$ nằm trọn vẹn bên trong bao lồi của các điểm đầu mút, thì bao nón của chúng sẽ **bùng nổ thành toàn bộ không gian** $\mathbb{R}^n$.

::: example Bao nón của ba vector bao quanh gốc tọa độ
Trong mặt phẳng $\mathbb{R}^2$, xét ba vector:

$$
v_1 = (1, 0), \quad v_2 = (-1, 1), \quad v_3 = (-1, -1)
$$

Gốc tọa độ $O = (0, 0)$ là một tổ hợp lồi của ba vector này:

$$
\frac{1}{2} v_1 + \frac{1}{4} v_2 + \frac{1}{4} v_3 = \frac{1}{2}(1, 0) + \frac{1}{4}(-1, 1) + \frac{1}{4}(-1, -1) = (0, 0)
$$

với các trọng số không âm $\theta_1 = 0.5$, $\theta_2 = 0.25$, $\theta_3 = 0.25$ có tổng bằng 1.

Ta chứng minh rằng $\operatorname{cone}\{v_1, v_2, v_3\} = \mathbb{R}^2$: Lấy một vector tùy ý $u = (a, b) \in \mathbb{R}^2$.
- Nếu $b \ge 0$: Ta có thể phân tích $u$ theo hai vector $v_1$ và $v_2$. Phương trình $\alpha v_1 + \beta v_2 = (a, b)$ tương đương với $\alpha(1, 0) + \beta(-1, 1) = (a, b)$, cho nghiệm $\beta = b \ge 0$ và $\alpha = a + \beta = a + b$. Nếu $\alpha \ge 0$, ta đã có tổ hợp nón của $v_1, v_2$. Nếu $\alpha < 0$, ta cộng thêm một lượng dương của biểu thức triệt tiêu $2v_1 + v_2 + v_3 = 0$ để đưa tất cả các hệ số về trạng thái không âm.
- Tổng quát hơn: Vì $v_2$ và $v_3$ có hướng ngược lại với $v_1$ và trải đều hai phía trục tung, ba vector này tạo thành một tập sinh dương (positive spanning set) của $\mathbb{R}^2$. Bất kỳ vector nào trong mặt phẳng cũng biểu diễn được thành tổ hợp với các hệ số không âm $\theta_1, \theta_2, \theta_3 \ge 0$.

Hiện tượng này hoàn toàn không xảy ra đối với bao lồi: Bao lồi $\operatorname{conv}\{v_1, v_2, v_3\}$ chỉ là một tam giác hữu hạn khép kín, trong khi bao nón $\operatorname{cone}\{v_1, v_2, v_3\}$ mở rộng thành toàn bộ mặt phẳng vô hạn.
:::

## 3. Bốn loại tổ hợp toán học đặt cạnh nhau

Đến đây, bức tranh tổng thể về các loại tổ hợp trong đại số tuyến tính và hình học lồi đã hoàn thành trọn vẹn. Việc đặt bốn loại tổ hợp cạnh nhau giúp người học nắm bắt cấu trúc phân loại có hệ thống:

| Loại tổ hợp | Điều kiện ràng buộc trên các hệ số $\theta_i$ | Bao của hai điểm $x_1, x_2$ độc lập tuyến tính | Cấu trúc hình học khép kín tương ứng |
| :--- | :--- | :--- | :--- |
| **Tuyến tính** (Linear) | Không có ràng buộc ($\theta_i \in \mathbb{R}$) | Mặt phẳng qua gốc chứa $x_1, x_2$ | Không gian con vector |
| **Affine** | Tổng bằng 1 ($\sum_i \theta_i = 1$) | Đường thẳng đi qua $x_1, x_2$ | Tập affine |
| **Nón** (Conic) | Không âm ($\theta_i \ge 0$) | Hình quạt vô hạn đỉnh tại gốc, mép qua $x_1, x_2$ | Nón lồi |
| **Lồi** (Convex) | Tổng bằng 1 và không âm ($\sum_i \theta_i = 1, \theta_i \ge 0$) | Đoạn thẳng nối hai đầu mút $[x_1, x_2]$ | Tập lồi |

Mỗi dòng dưới trong bảng mang nhiều ràng buộc đại số hơn dòng trên, ngoại trừ hai dòng giữa (Affine và Nón) không so sánh được với nhau do một bên ràng buộc tổng và một bên ràng buộc dấu.

Từ bảng phân loại chuẩn mực này, ta suy ra ngay cây quan hệ bao hàm giữa các đối tượng hình học:
1. Mọi không gian con vector đều đồng thời là tập affine và là nón lồi.
2. Mọi tập affine đều là tập lồi.
3. Mọi nón lồi đều là tập lồi.
4. Mọi chiều suy luận ngược lại đều không đúng: Một đoạn thẳng là tập lồi nhưng không phải tập affine và không phải là nón; một tia xuất phát từ gốc tọa độ là nón lồi nhưng không phải tập affine; một mặt phẳng không đi qua gốc tọa độ là tập affine nhưng không phải là nón.

Khi đối diện với bất kỳ bài toán hình học hay biểu thức biến đổi nào, bạn chỉ cần đặt ra hai câu hỏi then chốt:
- **Câu hỏi 1**: Các hệ số có bị cấm mang giá trị âm không?
- **Câu hỏi 2**: Tổng của các hệ số có bắt buộc phải bằng 1 không?

Hai câu trả lời "Có" hoặc "Không" sẽ định danh chính xác 100% cấu trúc hình học tương ứng trong bảng trên.

## 4. Các nón cơ bản trong tối ưu hóa

Trong giải tích lồi và các thuật toán học máy, có bốn họ nón lồi đóng vai trò then chốt:

### 1. Góc phần tư không âm (Nonnegative Orthant)

Góc phần tư không âm trong không gian $n$ chiều được định nghĩa là:

$$
\mathbb{R}^n_+ = \{x \in \mathbb{R}^n \mid x_i \ge 0, \; \forall i = 1, \dots, n\}
$$

Đây là nón lồi sơ cấp và quen thuộc nhất: Tổng của hai vector có các tọa độ không âm là một vector không âm, và tích của một vector không âm với một số thực $\theta \ge 0$ vẫn là một vector không âm. Nón này sinh ra quan hệ thứ tự thành phần thông thường $x \preceq y \iff y - x \in \mathbb{R}^n_+$, nền tảng của quy hoạch tuyến tính (LP).

### 2. Nửa không gian đi qua gốc tọa độ

Xét nửa không gian đóng có phương trình $a^T x \le b$ với $a \ne 0$:
- Nếu $b = 0$, tập hợp $\{x \mid a^T x \le 0\}$ là một **nón lồi**, vì nếu $a^T x \le 0$ thì $a^T(\theta x) = \theta (a^T x) \le 0$ với mọi $\theta \ge 0$.
- Nếu $b \ne 0$ (chẳng hạn $b = 1$), tập hợp $\{x \mid a^T x \le 1\}$ là một tập lồi nhưng **tuyệt đối không phải là nón**: Lấy điểm $x$ thỏa $a^T x = 1 \le 1$, nhân với $\theta = 2 \ge 0$ cho ra $a^T(2x) = 2 > 1$, điểm mới rơi ra ngoài tập hợp.

### 3. Nón chuẩn và nón bậc hai (Second-Order Cone / Lorentz Cone)

Cho một chuẩn vector bất kỳ $\|\cdot\|$ trên $\mathbb{R}^n$. **Nón chuẩn** tương ứng trong không gian $\mathbb{R}^{n+1}$ là tập hợp:

$$
C = \{(x, t) \in \mathbb{R}^n \times \mathbb{R} \mid \|x\| \le t\}
$$

Chứng minh tính lồi và tính nón của $C$:
- Tính chất nón: Nếu $\|x\| \le t$ và $\theta \ge 0$, thì $\|\theta x\| = \theta \|x\| \le \theta t$, do đó $\theta(x, t) \in C$.
- Tính lồi: Lấy $(x_1, t_1), (x_2, t_2) \in C$ và $\theta \in [0, 1]$. Theo bất đẳng thức tam giác:
  $$
  \|\theta x_1 + (1 - \theta) x_2\| \le \theta \|x_1\| + (1 - \theta) \|x_2\| \le \theta t_1 + (1 - \theta) t_2
  $$
  Do đó tổ hợp lồi thuộc $C$.

Khi chuẩn được sử dụng là chuẩn Euclid $\|\cdot\|_2$, nón chuẩn được gọi là **nón bậc hai** (Second-Order Cone), hay còn gọi là **nón Lorentz** hoặc **nón kem** (ice-cream cone):

$$
\mathcal{Q}^{n+1} = \{(x, t) \in \mathbb{R}^n \times \mathbb{R} \mid \|x\|_2 \le t\}
$$

Trong không gian ba chiều $\mathbb{R}^3$, điều kiện trên viết thành $\sqrt{x_1^2 + x_2^2} \le x_3$, tạo nên một chiếc nón tròn xoay có trục thẳng đứng dọc theo trục $x_3$. Đây là đối tượng nghiên cứu của quy hoạch nón bậc hai (SOCP).

### 4. Nón nửa xác định dương (Positive Semidefinite Cone)

Trong không gian các ma trận đối xứng kích thước $n \times n$ ký hiệu là $\mathbb{S}^n$, tập hợp tất cả các ma trận nửa xác định dương:

$$
\mathbb{S}^n_+ = \{X \in \mathbb{S}^n \mid X \succeq 0\} = \{X \in \mathbb{S}^n \mid z^T X z \ge 0, \; \forall z \in \mathbb{R}^n\}
$$

tạo thành một nón lồi có số chiều $\tfrac{n(n+1)}{2}$. Nếu $A, B \in \mathbb{S}^n_+$ và $\theta_1, \theta_2 \ge 0$, thì với mọi $z \in \mathbb{R}^n$:

$$
z^T (\theta_1 A + \theta_2 B) z = \theta_1 (z^T A z) + \theta_2 (z^T B z) \ge 0
$$

Nón này là trái tim của quy hoạch nửa xác định dương (SDP).

## 5. Bài toán kiểm tra một vector có thuộc một nón không?

Cho một họ $k$ vector cột $a_1, \ldots, a_k \in \mathbb{R}^m$ và một vector truy vấn $b \in \mathbb{R}^m$. Bài toán hình học đặt ra là: Làm thế nào để kiểm tra vector $b$ có thuộc bao nón $\operatorname{cone}\{a_1, \ldots, a_k\}$ hay không?

Theo định nghĩa, $b \in \operatorname{cone}\{a_1, \ldots, a_k\}$ khi và chỉ khi tồn tại các hệ số $\theta_1, \dots, \theta_k \ge 0$ sao cho $\sum_{i=1}^k \theta_i a_i = b$. Viết dưới dạng ma trận:

$$
A \theta = b, \quad \theta \succeq 0
$$

trong đó $A = [a_1 \ a_2 \ \dots \ a_k] \in \mathbb{R}^{m \times k}$ là ma trận ghép các cột, và $\theta \succeq 0$ biểu thị vector $\theta$ có toàn bộ các thành phần không âm.

Đây chính là một **bài toán tìm điểm khả thi** (feasibility problem) trong quy hoạch tuyến tính. Ta thấy một sự thống nhất tuyệt đẹp giữa hình học và đại số: Câu hỏi hình học "Vector $b$ có nằm trong hình quạt nón không?" hoàn toàn tương đương với câu hỏi đại số "Hệ phương trình tuyến tính $A\theta = b$ có nghiệm không âm không?".

::: example Kiểm tra nghiệm không âm bằng phương pháp khử đại số
Trong mặt phẳng $\mathbb{R}^2$, cho hai vector $a_1 = (2, 1)$ và $a_2 = (1, 3)$.
Ta kiểm tra hai vector truy vấn $b = (4, 7)$ và $b' = (4, -1)$:

1. **Khảo sát vector $b = (4, 7)$**:
   Thiết lập hệ phương trình $\theta_1(2, 1) + \theta_2(1, 3) = (4, 7)$:
   $$
\begin{aligned}
2\theta_1 + \theta_2 &= 4 \\
\theta_1 + 3\theta_2 &= 7
\end{aligned}
$$
   Nhân phương trình thứ hai với 2 rồi trừ đi phương trình thứ nhất:
   $$
   2(\theta_1 + 3\theta_2) - (2\theta_1 + \theta_2) = 14 - 4 \iff 5\theta_2 = 10 \iff \theta_2 = 2
   $$
   Thay ngược lại vào phương trình thứ nhất: $2\theta_1 + 2 = 4 \implies \theta_1 = 1$.
   Cả hai hệ số đều không âm: Cụ thể là $\theta_1 = 1 \ge 0$ và $\theta_2 = 2 \ge 0$. Do đó $b$ thuộc bao nón của $a_1, a_2$.
2. **Khảo sát vector $b' = (4, -1)$**:
   Thiết lập hệ phương trình:
   $$
\begin{aligned}
2\theta_1 + \theta_2 &= 4 \\
\theta_1 + 3\theta_2 &= -1
\end{aligned}
$$
   Nhân phương trình thứ hai với 2 rồi trừ phương trình thứ nhất:
   $$
   5\theta_2 = -2 - 4 = -6 \iff \theta_2 = -\frac{6}{5} = -1.2
   $$
   Vì $a_1$ và $a_2$ độc lập tuyến tính ($\det = 2 \cdot 3 - 1 \cdot 1 = 5 \ne 0$), hệ phương trình có nghiệm duy nhất. Nghiệm duy nhất này có $\theta_2 = -1.2 < 0$, vi phạm điều kiện không âm. Do đó $b'$ không thuộc bao nón.
:::

Nếu một vector $b$ không thuộc nón, làm sao ta có thể cung cấp một chứng chỉ toán học gọn gàng để khẳng định điều đó mà không cần giải thích dài dòng? Câu trả lời chính là một **siêu phẳng phân tách** đi qua gốc tọa độ ngăn cách $b$ khỏi toàn bộ nón. Định lý đảm bảo sự tồn tại của siêu phẳng này chính là **Bổ đề Farkas**, nội dung mà chúng ta sẽ khám phá sâu hơn ở bài học về siêu phẳng phân tách.

## 6. Khái niệm nón nhọn và nón chính quy

Trong lý thuyết thứ tự và đối ngẫu, người ta quan tâm tới hai thuộc tính hình học quan trọng của nón:

### Nón nhọn (Pointed Cone)

> **Định nghĩa.** Một nón lồi $K$ được gọi là **nhọn** (pointed) nếu nó không chứa bất kỳ đường thẳng đầy đủ nào đi qua gốc tọa độ. Nói theo ngôn ngữ đại số:
> $$
> x \in K \quad \text{và} \quad -x \in K \implies x = 0
> $$
> nghĩa là $K \cap (-K) = \{0\}$.

Ví dụ minh họa:
- Góc phần tư không âm $\mathbb{R}^n_+$ là một nón nhọn: Nếu $x \ge 0$ và $-x \ge 0$ thì bắt buộc $x = 0$.
- Nửa không gian qua gốc $\{x \in \mathbb{R}^2 \mid x_2 \ge 0\}$ là một nón lồi nhưng **không nhọn**, vì nó chứa toàn bộ trục hoành (đường thẳng $x_2 = 0$). Tại đây vector $(1, 0)$ và vector đối $(-1, 0)$ đều cùng thuộc tập hợp.

### Nón chính quy (Proper Cone)

Một nón lồi $K \subseteq \mathbb{R}^n$ được gọi là **nón chính quy** (proper cone) nếu nó thỏa mãn đồng thời bốn điều kiện:
1. $K$ là tập lồi.
2. $K$ là tập đóng (closed) theo nghĩa topo.
3. $K$ có phần trong khác rỗng ($\operatorname{int} K \ne \emptyset$, hay còn gọi là nón đặc - solid cone).
4. $K$ là nón nhọn (pointed).

Nón chính quy là nền tảng để thiết lập các **bất đẳng thức tổng quát** (generalized inequalities) trên không gian vector, cho phép so sánh độ lớn giữa các vector tương tự như cách ta so sánh các số thực.

## 7. Ứng dụng của nón trong học máy

Khái niệm nón xuất hiện tự nhiên trong các bài toán học máy mà ở đó dữ liệu chỉ có thể tích lũy thêm thành phần chứ không thể trừ bớt:

1. **Phân rã ma trận không âm (Nonnegative Matrix Factorization - NMF)**:
   Trong nhiều ứng dụng xử lý ảnh và khai phá văn bản, dữ liệu có bản chất không âm (độ sáng pixel ảnh, tần suất xuất hiện của từ khóa). Thuật toán NMF xấp xỉ ma trận dữ liệu $X \approx W H$ với $W \ge 0, H \ge 0$. Mỗi mẫu dữ liệu (cột của $X$) được biểu diễn như một tổ hợp nón của các vector đặc trưng cơ sở (các cột của $W$):
   $$
   x_j = \sum_{i=1}^r h_{ij} w_i, \quad h_{ij} \ge 0
   $$
   Bởi vì các trọng số $h_{ij}$ không được âm, mô hình bị ép buộc phải học các bộ phận thành phần cục bộ mang tính trực quan (chẳng hạn mắt, mũi, miệng khi phân tích ảnh khuôn mặt). Toàn bộ không gian các mẫu biểu diễn được chính là bao nón của các thành phần cơ sở.
2. **Hàm kích hoạt ReLU trong mạng nơ-ron**:
   Hàm kích hoạt tuyến tính chỉnh lưu $\operatorname{ReLU}(z) = \max\{0, z\}$ luôn cho đầu ra thuộc góc phần tư không âm $\mathbb{R}^n_+$. Một tầng nơ-ron tiếp theo với các trọng số kết nối không âm sẽ sinh ra các vector đầu ra là tổ hợp nón của các đặc trưng tầng trước.
3. **Bộ phân loại tuyến tính không có hệ số chặn**:
   Một bộ phân loại tuyến tính không có bias term dự đoán nhãn dương khi $w^T x \ge 0$. Vùng quyết định nhãn dương là một nửa không gian qua gốc, tức là một nón lồi. Do đó nếu một điểm dữ liệu $x$ được gán nhãn dương, thì mọi điểm phóng to $\alpha x$ với $\alpha > 0$ cũng chắc chắn được gán nhãn dương.

## 8. Những câu hỏi để đào sâu

**Câu 1.** Một nón theo định nghĩa chuẩn tắc có bắt buộc phải chứa gốc tọa độ không? Tập hợp góc phần tư mở $K = \{x \in \mathbb{R}^2 \mid x_1 > 0, \; x_2 > 0\}$ có phải là một nón không?

<details><summary>Xem lời giải thích</summary>

Theo định nghĩa chuẩn tắc của giải tích lồi với hệ số $\theta \ge 0$, một nón khác rỗng bắt buộc phải chứa gốc tọa độ: Lấy điểm $x \in K$ bất kỳ và chọn $\theta = 0$, ta có $0 \cdot x = 0 \in K$.

Do đó, tập góc phần tư mở $K = \{x \in \mathbb{R}^2 \mid x_1 > 0, \; x_2 > 0\}$ không phải là một nón theo định nghĩa này: Chọn điểm $x = (1, 1) \in K$, nhưng với $\theta = 0$ ta có $\theta x = (0, 0) \notin K$. Cần lưu ý rằng một số tài liệu giải tích cổ điển dùng định nghĩa nón mở với $\theta > 0$. Trong chương trình StudyHub, ta tuân thủ tuyệt đối quy ước chuẩn mực $\theta \ge 0$.

</details>

**Câu 2.** Giao của hai nón lồi có luôn luôn là một nón lồi không? Tổng Minkowski $K_1 + K_2 = \{x + y \mid x \in K_1, \; y \in K_2\}$ của hai nón lồi thì sao?

<details><summary>Xem lời giải thích</summary>

Cả hai phép toán đều bảo toàn cấu trúc nón lồi:
1. **Phép giao**: Nếu $u, v \in K_1 \cap K_2$ và $\theta_1, \theta_2 \ge 0$, thì $\theta_1 u + \theta_2 v$ thuộc $K_1$ (do $K_1$ là nón lồi) và cũng thuộc $K_2$ (do $K_2$ là nón lồi). Do đó tổ hợp thuộc phần giao.
2. **Tổng Minkowski**: Lấy hai điểm thuộc tổng $u = x_1 + y_1$ và $v = x_2 + y_2$ với $x_1, x_2 \in K_1$ và $y_1, y_2 \in K_2$. Với mọi $\theta_1, \theta_2 \ge 0$:
   $$
   \theta_1 u + \theta_2 v = (\theta_1 x_1 + \theta_2 x_2) + (\theta_1 y_1 + \theta_2 y_2)
   $$
   Số hạng thứ nhất thuộc $K_1$ và số hạng thứ hai thuộc $K_2$, do đó tổng của chúng thuộc $K_1 + K_2$.

</details>

**Câu 3.** Cho một đường tròn không đi qua gốc tọa độ trong mặt phẳng, chẳng hạn đường tròn tâm $I = (3, 0)$ bán kính $R = 1$. Bao nón của đường tròn này có hình dạng gì? Nếu đường tròn có tâm tại gốc tọa độ $O = (0, 0)$ thì sao?

<details><summary>Xem lời giải thích</summary>

Với đường tròn tâm $(3, 0)$ bán kính 1: Các tia thẳng xuất phát từ gốc tọa độ chạm vào đường tròn bị giới hạn bởi hai tiếp tuyến kẻ từ gốc. Góc nghiêng của tiếp tuyến so với trục hoành thỏa mãn $\sin \alpha = \tfrac{R}{OI} = \tfrac{1}{3} \implies \alpha \approx 19.47^\circ$. Do đó bao nón là một hình quạt vô hạn đối xứng qua trục hoành với góc mở tổng cộng xấp xỉ $38.94^\circ$.

Ngược lại, với đường tròn tâm tại gốc tọa độ $(0, 0)$ bán kính 1: Mọi hướng vector trong mặt phẳng đều có điểm giao cắt trên đường tròn. Do đó các tia thẳng xuất phát từ gốc tọa độ quét qua toàn bộ mọi hướng, biến bao nón thành toàn bộ mặt phẳng $\mathbb{R}^2$. Câu hỏi này nhấn mạnh một trực giác: Bao nón chỉ quan tâm tới các **phương hướng** của điểm dữ liệu chứ không phụ thuộc vào khoảng cách từ điểm tới gốc tọa độ.

</details>

**Câu 4.** Xét nhận định sau: "Nếu $K$ là một nón lồi và $K$ chứa ít nhất một đường thẳng đầy đủ đi qua gốc tọa độ, thì $K$ bắt buộc phải là một không gian con vector." Nhận định này đúng hay sai?

<details><summary>Xem lời giải thích</summary>

Nhận định trên là hoàn toàn sai lầm.

Phản ví dụ kinh điển là nửa mặt phẳng đóng trong $\mathbb{R}^2$:

$$
K = \{x \in \mathbb{R}^2 \mid x_2 \ge 0\}
$$

Tập hợp này là một nón lồi và chứa trọn vẹn toàn bộ trục hoành (đường thẳng $x_2 = 0$ đi qua gốc). Tuy nhiên $K$ không phải là một không gian con vector, vì nó không chứa điểm đối xứng $(0, -1)$ của điểm $(0, 1) \in K$. Nửa mặt phẳng chính là ví dụ tiêu biểu của một nón lồi không nhọn (non-pointed cone).

</details>

## 9. Bài tập tự luyện

::: exercise 1. Nhận diện nón và nón lồi
Trong các tập hợp sau đây, tập hợp nào là nón, tập hợp nào là nón lồi:
1. $K_1 = \{x \in \mathbb{R}^2 \mid x_1 \ge |x_2|\}$
2. $K_2 = \{x \in \mathbb{R}^2 \mid x_1 x_2 \ge 0\}$
3. $K_3 = \{x \in \mathbb{R}^2 \mid x_1 + x_2 \le 1\}$
4. $K_4 = \{x \in \mathbb{R}^3 \mid x_1^2 + x_2^2 \le x_3^2, \; x_3 \ge 0\}$
:::

::: solution
1. **Tập $K_1$ là nón lồi**:
   - Tính chất nón: Nếu $x_1 \ge |x_2|$ và $\theta \ge 0$, thì $\theta x_1 \ge \theta |x_2| = |\theta x_2|$, do đó $\theta x \in K_1$.
   - Tính lồi: Điều kiện $x_1 \ge |x_2|$ tương đương đồng thời với $x_1 - x_2 \ge 0$ và $x_1 + x_2 \ge 0$. Đây là giao của hai nửa mặt phẳng lồi đi qua gốc tọa độ, do đó $K_1$ là nón lồi.
2. **Tập $K_2$ là nón nhưng không lồi**:
   - Tính chất nón: Nếu $x_1 x_2 \ge 0$ và $\theta \ge 0$, thì $(\theta x_1)(\theta x_2) = \theta^2 (x_1 x_2) \ge 0$, do đó $K_2$ là một nón.
   - Tính không lồi: Tập $K_2$ là hợp của góc phần tư thứ nhất và góc phần tư thứ ba. Hai điểm $A = (1, 0)$ và $B = (0, -1)$ đều thuộc $K_2$, nhưng trung điểm của chúng là $M = (0.5, -0.5)$ có tích tọa độ $0.5 \times (-0.5) = -0.25 < 0 \notin K_2$.
3. **Tập $K_3$ không phải là nón**:
   Điểm $(1, 0) \in K_3$ (vì $1 + 0 = 1 \le 1$), nhưng với $\theta = 2 \ge 0$ ta có $\theta x = (2, 0)$ cho tổng $2 + 0 = 2 > 1 \notin K_3$. Tập này là một tập lồi (nửa mặt phẳng) nhưng không phải là nón.
4. **Tập $K_4$ là nón lồi**:
   Điều kiện $x_1^2 + x_2^2 \le x_3^2$ với $x_3 \ge 0$ tương đương với $\sqrt{x_1^2 + x_2^2} \le x_3$, nghĩa là $\|(x_1, x_2)\|_2 \le x_3$. Đây chính là nón bậc hai trong $\mathbb{R}^3$, đã được chứng minh là một nón lồi ở mục 4.
:::

::: exercise 2. Biểu diễn vector trong nón sinh bởi ba vector trong không gian
Trong không gian ba chiều $\mathbb{R}^3$, cho ba vector:
$$
a_1 = (1, 0, 1), \quad a_2 = (0, 1, 1), \quad a_3 = (1, 1, 0)
$$
1. Vector $b = (3, 1, 2)$ có thuộc bao nón $\operatorname{cone}\{a_1, a_2, a_3\}$ không?
2. Vector $b' = (2, 0, 0)$ có thuộc bao nón $\operatorname{cone}\{a_1, a_2, a_3\}$ không?
:::

::: solution
1. **Khảo sát vector $b = (3, 1, 2)$**:
   Thiết lập hệ phương trình $\theta_1 a_1 + \theta_2 a_2 + \theta_3 a_3 = b$:
   $$
\begin{aligned}
\theta_1 + \theta_3 &= 3 \\
\theta_2 + \theta_3 &= 1 \\
\theta_1 + \theta_2 &= 2
\end{aligned}
$$
   Cộng cả ba phương trình lại với nhau:
   $$
   2(\theta_1 + \theta_2 + \theta_3) = 3 + 1 + 2 = 6 \implies \theta_1 + \theta_2 + \theta_3 = 3
   $$
   Từ đó suy ra từng ẩn số:
   - $\theta_2 = 3 - (\theta_1 + \theta_3) = 3 - 3 = 0$.
   - $\theta_1 = 3 - (\theta_2 + \theta_3) = 3 - 1 = 2$.
   - $\theta_3 = 3 - (\theta_1 + \theta_2) = 3 - 2 = 1$.
   
   Cả ba hệ số đều không âm: $\theta_1 = 2 \ge 0, \theta_2 = 0 \ge 0, \theta_3 = 1 \ge 0$. Do đó vector $b$ thuộc bao nón.
2. **Khảo sát vector $b' = (2, 0, 0)$**:
   Thiết lập hệ phương trình:
   $$
\begin{aligned}
\theta_1 + \theta_3 &= 2 \\
\theta_2 + \theta_3 &= 0 \\
\theta_1 + \theta_2 &= 0
\end{aligned}
$$
   Cộng cả ba phương trình:
   $$
   2(\theta_1 + \theta_2 + \theta_3) = 2 \implies \theta_1 + \theta_2 + \theta_3 = 1
   $$
   Suy ra:
   - $\theta_2 = 1 - (\theta_1 + \theta_3) = 1 - 2 = -1$.
   - $\theta_1 = 1 - (\theta_2 + \theta_3) = 1 - 0 = 1$.
   - $\theta_3 = 1 - (\theta_1 + \theta_2) = 1 - 0 = 1$.
   
   Vì ma trận các cột có định thức khác không, hệ có nghiệm duy nhất. Nghiệm này có $\theta_2 = -1 < 0$, vi phạm điều kiện không âm. Do đó vector $b'$ không thuộc bao nón.
:::

## Tóm tắt

Nón là tập hợp khép kín với phép nhân với mọi số thực không âm ($\theta x \in C, \forall \theta \ge 0$). Nón lồi là nón đồng thời có tính lồi, tương đương với việc khép kín với mọi tổ hợp tuyến tính có hệ số không âm ($\theta_1 x_1 + \theta_2 x_2 \in C, \forall \theta_1, \theta_2 \ge 0$). Về mặt hình học trong mặt phẳng, bao nón của các vector là một hình quạt vô hạn có đỉnh tại gốc tọa độ, hoặc mở rộng thành toàn bộ không gian nếu gốc tọa độ nằm trong bao lồi của các điểm.

Bốn loại tổ hợp toán học (Tuyến tính, Affine, Nón, Lồi) được phân biệt rõ ràng qua hai câu hỏi: Hệ số có bị cấm âm không, và tổng hệ số có bắt buộc bằng 1 không. Bài toán kiểm tra một vector có thuộc bao nón hay không tương đương với một bài toán tìm điểm khả thi của quy hoạch tuyến tính. Các nón quan trọng như góc phần tư không âm, nón chuẩn, nón bậc hai và nón nửa xác định dương đóng vai trò nền tảng cho lý thuyết tối ưu hóa hiện đại và các thuật toán học máy.

## Tài liệu tham khảo

- Stephen Boyd, Lieven Vandenberghe, *Convex Optimization*, Cambridge University Press.
- D. D. Lee, H. S. Seung, *Learning the parts of objects by non-negative matrix factorization*, Nature 401 (1999), 788–791.
