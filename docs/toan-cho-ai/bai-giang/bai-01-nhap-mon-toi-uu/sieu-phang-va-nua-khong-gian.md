---
course: toan-cho-ai
lecture: bai-01-nhap-mon-toi-uu
topic: sieu-phang-va-nua-khong-gian
section: topic
title: "Siêu phẳng và nửa không gian"
description: "Siêu phẳng như tập nghiệm của một phương trình tuyến tính, vector pháp tuyến và độ lệch, biểu diễn x₀ + a⊥, nửa không gian và pháp tuyến hướng ra ngoài, khoảng cách có dấu, quan hệ chứa giữa hai nửa không gian và nửa không gian Voronoi."
---

Một phương trình tuyến tính duy nhất, chẳng hạn $3x_1 + 4x_2 = 10$, có thể được tiếp cận theo hai góc nhìn bổ trợ cho nhau. Người làm đại số nhìn thấy một ràng buộc giữa hai ẩn số và tìm cách xác định tập nghiệm. Người làm hình học nhìn thấy một đường thẳng chia đôi mặt phẳng tọa độ. Trong không gian ba chiều $\mathbb{R}^3$, phương trình $3x_1 + 4x_2 + x_3 = 10$ xác định một mặt phẳng. Tổng quát hóa lên không gian $n$ chiều $\mathbb{R}^n$, phương trình đó xác định một **siêu phẳng**: Một không gian affine có số chiều đúng bằng $n - 1$, nghĩa là mỏng hơn không gian bao quanh nó đúng một chiều tự do.

Siêu phẳng và nửa không gian là những viên gạch nền móng sơ cấp nhất của hình học lồi và tối ưu hóa. Mọi tập đa diện lồi đều được kiến tạo từ giao của một số hữu hạn các nửa không gian. Mọi tập lồi đóng bất kỳ đều có thể biểu diễn như giao của vô số nửa không gian chứa nó. Hơn thế nữa, định lý siêu phẳng phân tách khẳng định rằng hai tập lồi rời nhau luôn luôn có thể ngăn cách bằng một siêu phẳng phù hợp. Bài học này giúp bạn đọc giải mã trọn vẹn mọi đặc trưng hình học của siêu phẳng và nửa không gian trực tiếp từ phương trình đại số: Xác định phương pháp tuyến, tính khoảng cách có dấu tới một điểm bất kỳ, nhận diện cấu trúc trực giao và phân tích quan hệ bao hàm hình học.

## 1. Định nghĩa và cách đọc thứ nhất: Tích vô hướng cố định

Ta bắt đầu bằng định nghĩa chuẩn mực của siêu phẳng trong không gian Euclid:

> **Định nghĩa.** Một **siêu phẳng** trong $\mathbb{R}^n$ là tập hợp các điểm có dạng:
> $$
> H = \{x \in \mathbb{R}^n \mid a^T x = b\}
> $$
> trong đó $a \in \mathbb{R}^n$ là vector khác không ($a \ne 0$) và $b \in \mathbb{R}$ là một hằng số thực.

Về mặt giải tích, siêu phẳng là tập nghiệm của một phương trình tuyến tính duy nhất không suy biến. Theo định lý về tập affine đã nghiên cứu ở bài trước, siêu phẳng chính là một tập affine có số chiều $n - 1$. Điều kiện tiên quyết $a \ne 0$ loại bỏ phương trình tầm thường $0^T x = b$: Nếu $b \ne 0$ thì phương trình vô nghiệm (tập rỗng), còn nếu $b = 0$ thì phương trình nhận toàn bộ không gian $\mathbb{R}^n$ làm nghiệm. Cả hai trường hợp suy biến đó đều không tạo nên cấu trúc siêu phẳng.

Về mặt hình học, phương trình $a^T x = b$ mang một ý nghĩa trực quan: Siêu phẳng là **tập hợp tất cả các điểm có cùng tích vô hướng $b$ với vector pháp tuyến $a$**. Nhớ lại định nghĩa phép chiếu vuông góc trong đại số tuyến tính: Hình chiếu của vector vị trí $x$ lên trục đường thẳng đi qua gốc tọa độ theo phương vector đơn vị $\tfrac{a}{\|a\|_2}$ có độ dài mang dấu đúng bằng:

$$
\operatorname{proj}_a(x) = \frac{a^T x}{\|a\|_2} = \frac{b}{\|a\|_2}
$$

Điều này cho thấy phương trình $a^T x = b$ khẳng định rằng: Dù điểm $x$ nằm ở bất kỳ đâu trên siêu phẳng, hình chiếu vuông góc của nó lên phương vector $a$ luôn rơi đúng vào một vị trí cố định trên trục đó, cách gốc tọa độ một đại lượng có dấu bằng $\tfrac{b}{\|a\|_2}$. Tập hợp tất cả các điểm trong không gian có chung hình chiếu như vậy tạo thành một mặt phẳng $(n - 1)$ chiều **vuông góc với vector $a$**.

Vector $a$ được gọi là **vector pháp tuyến** (normal vector) của siêu phẳng, còn đại lượng $b$ quyết định độ dịch chuyển (offset) của siêu phẳng so với gốc tọa độ. Hai phép biến đổi phương trình sau đây mang hai hiệu ứng hình học hoàn toàn khác nhau cần được phân biệt sáng rõ:

1. **Nhân hai vế với một hằng số thực khác không $\alpha \ne 0$**: Phương trình $(\alpha a)^T x = \alpha b$ hoàn toàn tương đương với phương trình ban đầu. Do đó siêu phẳng hình học **không thay đổi**.
2. **Giữ nguyên vector pháp tuyến $a$ và thay đổi giá trị $b$**: Siêu phẳng mới có phương trình $a^T x = b'$ sẽ **tịnh tiến song song** với siêu phẳng ban đầu dọc theo phương của vector pháp tuyến $a$.

::: example Xác định các yếu tố hình học của một siêu phẳng trong mặt phẳng
Xét phương trình đường thẳng $3x_1 + 4x_2 = 10$ trong mặt phẳng $\mathbb{R}^2$. Ở đây ta có vector pháp tuyến $a = (3, 4)$ và hằng số lệch $b = 10$.

Độ dài chuẩn Euclid của vector pháp tuyến là:

$$
\|a\|_2 = \sqrt{3^2 + 4^2} = \sqrt{9 + 16} = 5
$$

Khoảng cách từ gốc tọa độ $O = (0, 0)$ tới đường thẳng là:

$$
d(O, H) = \frac{|b|}{\|a\|_2} = \frac{10}{5} = 2
$$

Điểm $x_0$ nằm trên đường thẳng và gần gốc tọa độ nhất chính là hình chiếu vuông góc của gốc tọa độ lên đường thẳng:

$$
x_0 = \frac{b}{\|a\|_2^2}\, a = \frac{10}{25} (3, 4) = \frac{2}{5} (3, 4) = (1.2,\ 1.6)
$$

Thử lại phương trình đường thẳng: $3(1.2) + 4(1.6) = 3.6 + 6.4 = 10$, hoàn toàn chính xác. Khoảng cách từ gốc tọa độ tới điểm $x_0$ là $\sqrt{1.2^2 + 1.6^2} = \sqrt{1.44 + 2.56} = 2$.

Vector chỉ phương của đường thẳng là bất kỳ vector $d = (d_1, d_2) \ne 0$ nào vuông góc với $a$, nghĩa là $a^T d = 3d_1 + 4d_2 = 0$. Một lựa chọn thuận tiện là $d = (4, -3)$ hoặc $d = (-4, 3)$.
:::

## 2. Cách đọc thứ hai: Điểm cơ sở cộng không gian con trực giao

Góc nhìn thứ hai làm sáng tỏ cấu trúc affine của siêu phẳng bằng cách liên kết nó với khái niệm phần bù trực giao.

Lấy một điểm tùy ý $x_0$ thuộc siêu phẳng $H$, nghĩa là thỏa mãn $a^T x_0 = b$. Khi đó, với mọi điểm $x \in \mathbb{R}^n$, ta có chuỗi biến đổi tương đương:

$$
a^T x = b \iff a^T x = a^T x_0 \iff a^T(x - x_0) = 0
$$

Đẳng thức cuối cùng phát biểu rằng: Vector hiệu $x - x_0$, nối từ điểm mốc $x_0$ tới điểm $x$, phải vuông góc với vector pháp tuyến $a$.

Gọi $a^\perp$ là **phần bù trực giao** (orthogonal complement) của vector $a$, tập hợp mọi vector trong $\mathbb{R}^n$ trực giao với $a$:

$$
a^\perp = \{v \in \mathbb{R}^n \mid a^T v = 0\}
$$

Vì $a \ne 0$, tập hợp $a^\perp$ là một không gian con vector của $\mathbb{R}^n$ có số chiều đúng bằng $n - 1$. Từ đó ta thu được biểu diễn hình học tương đương của siêu phẳng:

$$
\{x \in \mathbb{R}^n \mid a^T x = b\} = x_0 + a^\perp = \{x_0 + v \mid v \in a^\perp\}
$$

Biểu diễn này khẳng định cấu trúc chuẩn tắc của một tập affine: Siêu phẳng chính là không gian con vector $a^\perp$ có số chiều $n - 1$ được tịnh tiến đi một đoạn bằng vector $x_0$. Dù ta chọn điểm mốc $x_0$ nào trên siêu phẳng, không gian con dẫn xuất $a^\perp$ vẫn hoàn toàn duy nhất.

## 3. Nửa không gian và pháp tuyến hướng ra ngoài

Một siêu phẳng chia toàn bộ không gian $\mathbb{R}^n$ thành hai phần đối xứng qua biên. Mỗi phần đó được gọi là một nửa không gian.

> **Định nghĩa.** Một **nửa không gian đóng** (closed halfspace) trong $\mathbb{R}^n$ là tập hợp có dạng:
> $$
> \{x \in \mathbb{R}^n \mid a^T x \le b\}
> $$
> với $a \ne 0$ và $b \in \mathbb{R}$. Nửa không gian mở tương ứng thu được bằng cách thay dấu bất đẳng thức thành dấu nhỏ hơn ngặt: $\{x \in \mathbb{R}^n \mid a^T x < b\}$.

### Tính lồi của nửa không gian

Nửa không gian là một tập lồi nhưng không phải là một tập affine. Ta chứng minh tính lồi trực tiếp từ định nghĩa: Lấy hai điểm bất kỳ $x_1, x_2$ thuộc nửa không gian, nghĩa là $a^T x_1 \le b$ và $a^T x_2 \le b$. Với mọi hệ số $\theta \in [0, 1]$, ta tính tích vô hướng của tổ hợp lồi:

$$
\begin{aligned}
&a^T (\theta x_1 + (1 - \theta) x_2) = \theta a^T x_1 + (1 - \theta) a^T x_2\\
&\quad \le \theta b + (1 - \theta) b = b
\end{aligned}
$$

Trong chuỗi biến đổi trên, bước áp dụng bất đẳng thức đòi hỏi điều kiện $\theta \ge 0$ và $1 - \theta \ge 0$ để giữ nguyên chiều của bất đẳng thức. Do đó tổ hợp lồi luôn thuộc nửa không gian, chứng tỏ tập hợp này lồi. Trái lại, nếu cho phép $\theta$ nhận giá trị tùy ý ngoài đoạn $[0, 1]$, chẳng hạn chọn $\theta = 2$, thì $1 - \theta = -1 < 0$ và bất đẳng thức bị đảo chiều, khiến điểm tương ứng có thể rơi ra ngoài nửa không gian. Điều này lý giải vì sao nửa không gian không phải là tập affine.

### Trực giác hình học về pháp tuyến hướng ra ngoài

Tại sao vector $a$ được gọi là **pháp tuyến hướng ra ngoài** (outward normal) của nửa không gian $\{x \mid a^T x \le b\}$?

Hãy quan sát chiều biến thiên của hàm tuyến tính $f(x) = a^T x$. Bắt đầu từ một điểm $x$ nằm trên biên của nửa không gian (tức $a^T x = b$), nếu ta di chuyển theo phương vector $a$ một đoạn có độ dài $t > 0$, điểm mới là $x + t a$. Giá trị của hàm số tại điểm mới trở thành:

$$
a^T(x + t a) = a^T x + t a^T a = b + t \|a\|_2^2 > b
$$

Bởi vì $\|a\|_2^2 > 0$, giá trị tăng ngặt và điểm mới lập tức vi phạm điều kiện $a^T x \le b$, nghĩa là rơi ra ngoài nửa không gian. Ngược lại, nếu di chuyển theo hướng đối nghịch $-a$, giá trị giảm xuống $b - t \|a\|_2^2 < b$, điểm lặn sâu hơn vào miền trong của nửa không gian. Như vậy, vector $a$ luôn chỉ thẳng từ miền trong ra miền ngoài, do đó mang tên gọi pháp tuyến hướng ra ngoài.

Nếu chọn một điểm $x_0$ nằm trên biên siêu phẳng ($a^T x_0 = b$), ta có thể viết lại nửa không gian dưới dạng tích vô hướng của hiệu vector:

$$
\{x \in \mathbb{R}^n \mid a^T(x - x_0) \le 0\}
$$

Biểu thức này đem lại một hình ảnh hình học sinh động: Nửa không gian bao gồm điểm mốc $x_0$ cùng tất cả các điểm $x$ sao cho vector hướng $x - x_0$ tạo với vector pháp tuyến $a$ một **góc tù hoặc góc vuông** ($\cos \angle(a, x - x_0) \le 0$). Những điểm tạo góc nhọn với vector $a$ đều nằm ở nửa không gian bên ngoài.

<HyperplaneLab type="halfspace" />

## 4. Khoảng cách có dấu và ý nghĩa trong học máy

Trong hình học giải tích và các bài toán tối ưu, đại lượng sau đây đóng vai trò nền tảng:

$$
\operatorname{dist}_{\text{signed}}(x, H) = \frac{a^T x - b}{\|a\|_2}
$$

Đại lượng này được gọi là **khoảng cách có dấu** (signed distance) từ điểm $x$ tới siêu phẳng $H = \{z \mid a^T z = b\}$:
- **Độ lớn** $|\operatorname{dist}_{\text{signed}}(x, H)|$ biểu diễn khoảng cách hình học Euclid ngắn nhất từ $x$ tới siêu phẳng.
- **Dấu** của đại lượng này chỉ rõ vị trí tương đối của $x$: Dấu dương nghĩa là $x$ nằm ở phía ngoài (phía mà vector pháp tuyến $a$ hướng tới), dấu âm nghĩa là $x$ nằm ở phía trong (nửa không gian $\{z \mid a^T z \le b\}$), và bằng $0$ nghĩa là $x$ nằm chính xác trên siêu phẳng.

### Chứng minh công thức khoảng cách

Gọi $x_0$ là một điểm bất kỳ thuộc siêu phẳng ($a^T x_0 = b$). Điểm $x$ bất kỳ trong không gian có thể phân tích duy nhất thành tổng của hình chiếu vuông góc lên siêu phẳng và thành phần trực giao:

$$
x - x_0 = v_\parallel + v_\perp, \quad \text{với } v_\parallel \in a^\perp \text{ và } v_\perp = \lambda \frac{a}{\|a\|_2}
$$

Nhân vô hướng hai vế với vector đơn vị pháp tuyến $\tfrac{a}{\|a\|_2}$:

$$
\frac{a^T(x - x_0)}{\|a\|_2} = \frac{a^T v_\parallel}{\|a\|_2} + \lambda \frac{a^T a}{\|a\|_2^2} = 0 + \lambda = \lambda
$$

Do $a^T x_0 = b$, hệ số độ dài $\lambda$ chính là:

$$
\lambda = \frac{a^T x - b}{\|a\|_2}
$$

Khoảng cách Euclid từ $x$ tới siêu phẳng chính là độ dài của thành phần trực giao $\|v_\perp\|_2 = |\lambda| = \frac{|a^T x - b|}{\|a\|_2}$.

::: example Tính toán khoảng cách có dấu
Xét lại siêu phẳng $3x_1 + 4x_2 = 10$ với $a = (3, 4)$, $b = 10$, $\|a\|_2 = 5$. Ta kiểm tra khoảng cách có dấu của ba điểm:

1. **Điểm $P = (4, 2)$**:
   $$
   \operatorname{dist}_{\text{signed}}(P, H) = \frac{3(4) + 4(2) - 10}{5} = \frac{12 + 8 - 10}{5} = \frac{10}{5} = +2
   $$
   Kết quả mang dấu dương, cho thấy điểm $P$ cách siêu phẳng 2 đơn vị chiều dài và nằm về phía vector $a$ chỉ tới (nằm ngoài nửa không gian $\{x \mid 3x_1 + 4x_2 \le 10\}$).
2. **Gốc tọa độ $O = (0, 0)$**:
   $$
   \operatorname{dist}_{\text{signed}}(O, H) = \frac{3(0) + 4(0) - 10}{5} = \frac{-10}{5} = -2
   $$
   Kết quả mang dấu âm, cho thấy gốc tọa độ nằm trong nửa không gian $\{x \mid 3x_1 + 4x_2 \le 10\}$, cách biên đúng 2 đơn vị.
3. **Điểm $R = (1.2, 1.6)$**:
   $$
   \operatorname{dist}_{\text{signed}}(R, H) = \frac{3(1.2) + 4(1.6) - 10}{5} = \frac{3.6 + 6.4 - 10}{5} = 0
   $$
   Điểm $R$ nằm ngay trên siêu phẳng.
:::

### Khoảng cách giữa hai siêu phẳng song song

Cho hai siêu phẳng song song có cùng vector pháp tuyến $a$:

$$
H_1 = \{x \mid a^T x = b_1\} \quad \text{và} \quad H_2 = \{x \mid a^T x = b_2\}
$$

Lấy một điểm $x_1 \in H_1$, khoảng cách có dấu từ $x_1$ tới $H_2$ là $\tfrac{a^T x_1 - b_2}{\|a\|_2} = \tfrac{b_1 - b_2}{\|a\|_2}$. Từ đó suy ra khoảng cách hình học giữa hai siêu phẳng song song là:

$$
\operatorname{dist}(H_1, H_2) = \frac{|b_1 - b_2|}{\|a\|_2}
$$

::: warning Bẫy thi phổ biến: Hai phương trình chưa chuẩn hóa vector pháp tuyến
Khi tính khoảng cách giữa hai siêu phẳng, bắt buộc phải đưa hai phương trình về cùng một vector pháp tuyến $a$. Nếu một phương trình là $2x_1 - 2x_2 = 6$ và phương trình kia là $-4x_1 + 4x_2 = 8$, ta phải chia phương trình thứ hai cho $-2$ để đưa về $2x_1 - 2x_2 = -4$. Khi đó $a = (2, -2)$, $\|a\|_2 = \sqrt{8} = 2\sqrt{2}$, và khoảng cách là $\tfrac{|6 - (-4)|}{2\sqrt{2}} = \tfrac{10}{2\sqrt{2}} = \tfrac{5\sqrt{2}}{2}$. Nếu giữ nguyên hệ số mà áp dụng máy móc, kết quả tính toán sẽ hoàn toàn sai lệch.
:::

### Ý nghĩa trong học máy và máy vector hỗ trợ (SVM)

Trong các bài toán phân loại tuyến tính của học máy, mô hình phân loại nhị phân tính toán một hàm số điểm tuyến tính:

$$
s(x) = w^T x + b
$$

và dự đoán nhãn của mẫu dữ liệu dựa trên dấu của điểm số này. Ranh giới quyết định (decision boundary) ngăn cách hai lớp dữ liệu chính là siêu phẳng $\{x \mid w^T x + b = 0\}$.

Khoảng cách có dấu từ điểm dữ liệu $x$ tới ranh giới quyết định chính là:

$$
\gamma(x) = \frac{w^T x + b}{\|w\|_2}
$$

Đại lượng này được gọi là **biên hình học** (geometric margin). Giá trị điểm số $s(x) = w^T x + b$ được gọi là **biên hàm số** (functional margin). Nếu ta nhân toàn bộ trọng số $w$ và hệ số chặn $b$ với một hằng số dương lớn, chẳng hạn 100, thì ranh giới quyết định hoàn toàn không đổi, nhưng biên hàm số bị thổi phồng lên 100 lần. Do đó, biên hàm số không phản ánh đúng độ chắc chắn tin cậy của dự đoán.

Trái lại, biên hình học $\gamma(x)$ hoàn toàn bất biến trước phép co giãn hệ số. Ý tưởng cốt lõi của máy vector hỗ trợ (Support Vector Machine - SVM) là tìm siêu phẳng phân loại tối đa hóa khoảng cách hình học tới điểm dữ liệu gần ranh giới nhất:

$$
\max_{w, b} \; \frac{1}{\|w\|_2} \min_{i} \left[ y_i (w^T x_i + b) \right]
$$

Bằng cách cố định biên hàm số của các điểm gần nhất bằng 1, bài toán tối ưu trên được quy về bài toán quy hoạch toàn phương lồi chính tắc: Tối thiểu hóa $\tfrac{1}{2} \|w\|_2^2$.

## 5. Quan hệ chứa giữa hai nửa không gian

Một câu hỏi mang tính nền tảng cho lý thuyết đối ngẫu là: Khi nào một nửa không gian bị chứa hoàn toàn bên trong một nửa không gian khác?

> **Mệnh đề.** Cho hai vector pháp tuyến khác không $a \ne 0$ và $\tilde{a} \ne 0$. Khi đó:
> $$
> \{x \in \mathbb{R}^n \mid a^T x \le b\} \subseteq \{x \in \mathbb{R}^n \mid \tilde{a}^T x \le \tilde{b}\}
> $$
> khi và chỉ khi tồn tại một hằng số dương $\lambda > 0$ sao cho:
> $$
> \tilde{a} = \lambda a \quad \text{và} \quad \tilde{b} \ge \lambda b
> $$
> Hai nửa không gian trùng nhau khi và chỉ khi $\tilde{a} = \lambda a$ và $\tilde{b} = \lambda b$ với $\lambda > 0$.

### Chứng minh chi tiết từng bước

Ta chứng minh mệnh đề theo hai chiều suy luận chặt chẽ:

**Chiều thuận ($\Leftarrow$):** Giả sử tồn tại $\lambda > 0$ thỏa mãn $\tilde{a} = \lambda a$ và $\tilde{b} \ge \lambda b$. Với mọi điểm $x$ thuộc nửa không gian thứ nhất, ta có $a^T x \le b$. Nhân hai vế với số dương $\lambda > 0$, chiều bất đẳng thức được giữ nguyên:

$$
\lambda (a^T x) \le \lambda b \implies (\lambda a)^T x \le \lambda b \implies \tilde{a}^T x \le \lambda b \le \tilde{b}
$$

Như vậy $\tilde{a}^T x \le \tilde{b}$, chứng tỏ $x$ thuộc nửa không gian thứ hai.

**Chiều đảo ($\Rightarrow$):** Giả sử nửa không gian thứ nhất nằm trong nửa không gian thứ hai. Ta cần chứng minh ba khẳng định:

1. **Vector $\tilde{a}$ phải cùng phương với vector $a$**: Giả sử phản chứng rằng $\tilde{a}$ không cùng phương với $a$. Khi đó hình chiếu của $\tilde{a}$ lên không gian trực giao $a^\perp$ là một vector $d \ne 0$, thỏa mãn đồng thời $a^T d = 0$ và $\tilde{a}^T d \ne 0$. Đổi dấu $d$ nếu cần, ta luôn có thể giả định $\tilde{a}^T d > 0$. Chọn một điểm $x_0$ nằm trên biên của nửa không gian thứ nhất ($a^T x_0 = b$). Xét tia di chuyển $x_t = x_0 + t d$ với $t \ge 0$. Ta có:
   $$
   a^T x_t = a^T x_0 + t a^T d = b + 0 = b \le b, \quad \forall t \ge 0
   $$
   Nghĩa là toàn bộ tia $x_t$ nằm trọn trong nửa không gian thứ nhất. Tuy nhiên, giá trị đối với nửa không gian thứ hai là:
   $$
   \tilde{a}^T x_t = \tilde{a}^T x_0 + t \tilde{a}^T d
   $$
   Vì $\tilde{a}^T d > 0$, khi cho $t \to +\infty$, giá trị $\tilde{a}^T x_t$ tăng vô hạn và sẽ vượt quá ngưỡng $\tilde{b}$. Điều này dẫn tới tồn tại điểm thuộc nửa không gian thứ nhất nhưng không thuộc nửa không gian thứ hai, mâu thuẫn với giả thiết bao hàm. Do đó bắt buộc phải có $\tilde{a} = \lambda a$ với một số thực $\lambda \ne 0$.
2. **Hệ số $\lambda$ phải mang dấu dương ($\lambda > 0$)**: Giả sử $\lambda < 0$. Chọn một điểm $x_0$ trên biên và xét đường đi $x_t = x_0 - t a$ với $t \ge 0$. Ta có:
   $$
   a^T x_t = a^T x_0 - t \|a\|_2^2 = b - t \|a\|_2^2 \le b
   $$
   nghĩa là $x_t$ luôn thuộc nửa không gian thứ nhất. Thế nhưng giá trị ở nửa không gian thứ hai là:
   $$
   \tilde{a}^T x_t = \lambda a^T x_t = \lambda (b - t \|a\|_2^2) = \lambda b + t (-\lambda) \|a\|_2^2
   $$
   Vì $\lambda < 0$, đại lượng $-\lambda > 0$, do đó khi $t \to +\infty$ thì biểu thức này tiến tới $+\infty$, vượt qua ngưỡng $\tilde{b}$. Mâu thuẫn này khẳng định $\lambda > 0$.
3. **Ngưỡng biên phải thỏa mãn $\tilde{b} \ge \lambda b$**: Vì $\tilde{a} = \lambda a$ với $\lambda > 0$, giá trị lớn nhất của hàm mục tiêu $\tilde{a}^T x = \lambda a^T x$ trên nửa không gian $\{x \mid a^T x \le b\}$ đạt được chính xác tại biên $a^T x = b$, với giá trị cực đại bằng $\lambda b$. Để mọi điểm trong miền này thỏa mãn $\tilde{a}^T x \le \tilde{b}$, giá trị cực đại đó bắt buộc phải không vượt quá $\tilde{b}$, nghĩa là $\lambda b \le \tilde{b}$.

::: example Kiểm tra quan hệ chứa giữa hai nửa không gian
Xét hai nửa không gian trong $\mathbb{R}^2$:

$$
H_1 = \{x \in \mathbb{R}^2 \mid 2x_1 + 3x_2 \le 6\} \quad \text{và} \quad H_2 = \{x \in \mathbb{R}^2 \mid 4x_1 + 6x_2 \le 15\}
$$

Ở đây ta có $a = (2, 3)$, $b = 6$ và $\tilde{a} = (4, 6)$, $\tilde{b} = 15$.

Quan sát thấy $\tilde{a} = 2a$, do đó hệ số tỷ lệ là $\lambda = 2 > 0$. Kiểm tra điều kiện ngưỡng biên:

$$
\lambda b = 2 \cdot 6 = 12 \le 15 = \tilde{b}
$$

Cả hai điều kiện đều được thỏa mãn, do đó $H_1 \subseteq H_2$. Biên của $H_2$ là đường thẳng song song với biên của $H_1$ nhưng bị tịnh tiến lùi xa ra phía ngoài một khoảng hình học:

$$
\frac{\tilde{b} - \lambda b}{\|\tilde{a}\|_2} = \frac{15 - 12}{\sqrt{4^2 + 6^2}} = \frac{3}{\sqrt{52}} \approx 0.416
$$
:::

Bài học rút ra từ mệnh đề này là: Một bất đẳng thức tuyến tính chỉ có thể là hệ quả của một bất đẳng thức tuyến tính khác khi và chỉ khi nó là một **bội số dương** của bất đẳng thức ban đầu, kèm theo việc có thể nới lỏng thêm vế phải. Đây chính là trường hợp cơ sở của bổ đề Farkas trong lý thuyết đối ngẫu quy hoạch tuyến tính.

## 6. Nửa không gian Voronoi

Một ứng dụng hình học đẹp đẽ của nửa không gian xuất hiện trong bài toán phân chia không gian theo khoảng cách: Cho hai điểm phân biệt $p, q \in \mathbb{R}^n$, tập hợp tất cả các điểm nằm gần $p$ hơn hoặc bằng khoảng cách tới $q$ có cấu trúc hình học như thế nào?

Biểu diễn điều kiện khoảng cách Euclid bằng công thức toán học:

$$
\|z - p\|_2 \le \|z - q\|_2
$$

Vì hai vế đều là các số thực không âm, bất đẳng thức trên tương đương với việc bình phương hai vế:

$$
\|z - p\|_2^2 \le \|z - q\|_2^2
$$

Khai triển tường minh bình phương độ dài qua tích vô hướng:

$$
(z - p)^T (z - p) \le (z - q)^T (z - q)
$$

Khai triển từng số hạng đại số:

$$
z^T z - 2 p^T z + p^T p \le z^T z - 2 q^T z + q^T q
$$

Quan sát bước biến đổi mang tính quyết định: Số hạng bậc hai $z^T z$ xuất hiện ở cả hai vế với cùng hệ số dương, do đó **triệt tiêu hoàn toàn**. Bất đẳng thức trở thành:

$$
-2 p^T z + \|p\|_2^2 \le -2 q^T z + \|q\|_2^2
$$

Chuyển các số hạng chứa biến $z$ sang vế trái và các hằng số sang vế phải:

$$
2 (q - p)^T z \le \|q\|_2^2 - \|p\|_2^2
$$

Chia cả hai vế cho 2, ta thu được:

$$
(q - p)^T z \le \frac{\|q\|_2^2 - \|p\|_2^2}{2}
$$

Đây chính là phương trình của một **nửa không gian đóng** với vector pháp tuyến hướng ra ngoài là $a = q - p$ (vector chỉ hướng từ $p$ sang $q$) và hằng số biên $b = \tfrac{\|q\|_2^2 - \|p\|_2^2}{2}$.

Biên của nửa không gian này là siêu phẳng $(q - p)^T z = \tfrac{\|q\|_2^2 - \|p\|_2^2}{2}$. Ta kiểm tra xem trung điểm $m = \tfrac{p + q}{2}$ của đoạn thẳng nối $p$ và $q$ có thuộc siêu phẳng này không:

$$
(q - p)^T m = (q - p)^T \left( \frac{p + q}{2} \right) = \frac{(q - p)^T (q + p)}{2} = \frac{q^T q - p^T p}{2} = \frac{\|q\|_2^2 - \|p\|_2^2}{2}
$$

Như vậy siêu phẳng biên chính là **siêu phẳng trung trực** của đoạn thẳng $pq$: Đi qua trung điểm $m$ và vuông góc với đoạn nối hai điểm.

::: example Tính toán nửa không gian Voronoi với số liệu cụ thể
Cho hai điểm trong mặt phẳng $\mathbb{R}^2$: Điểm $p = (1, 2)$ và điểm $q = (5, 6)$.

Tính các đại lượng thành phần:
- Vector hiệu: $q - p = (5 - 1, 6 - 2) = (4, 4)$.
- Chuẩn bình phương: $\|p\|_2^2 = 1^2 + 2^2 = 5$, và $\|q\|_2^2 = 5^2 + 6^2 = 25 + 36 = 61$.
- Vế phải: $\tfrac{\|q\|_2^2 - \|p\|_2^2}{2} = \tfrac{61 - 5}{2} = \tfrac{56}{2} = 28$.

Bất đẳng thức xác định nửa không gian các điểm gần $p$ hơn $q$ là:

$$
4 z_1 + 4 z_2 \le 28 \iff z_1 + z_2 \le 7
$$

Trung điểm của đoạn $pq$ là $m = \left(\tfrac{1 + 5}{2}, \tfrac{2 + 6}{2}\right) = (3, 4)$. Thử vào biên: $3 + 4 = 7$, nằm chính xác trên đường trung trực.

Thử một điểm kiểm tra $z = (2, 1)$:
- Giá trị vế trái: $2 + 1 = 3 \le 7$, thỏa mãn bất đẳng thức.
- Khoảng cách tới $p$:
  $$
  \|z - p\|_2 = \sqrt{(2-1)^2 + (1-2)^2} = \sqrt{2} \approx 1.414
  $$
- Khoảng cách tới $q$:
  $$
  \|z - q\|_2 = \sqrt{(2-5)^2 + (1-6)^2} = \sqrt{34} \approx 5.831
  $$
- So sánh: $\sqrt{2} < \sqrt{34}$, điểm $z$ quả thật nằm gần $p$ hơn $q$.
:::

<HyperplaneLab type="voronoi" />

### Hệ quả: Biểu đồ Voronoi và phân cụm dữ liệu

Nếu ta có một tập hợp gồm $K + 1$ điểm mốc dữ liệu $x_0, x_1, \ldots, x_K$, tập hợp tất cả các điểm trong không gian nằm gần $x_0$ hơn tất cả các điểm còn lại được xác định bởi hệ bất đẳng thức:

$$
V(x_0) = \bigcap_{i=1}^K \left\{ z \in \mathbb{R}^n \;\middle|\; (x_i - x_0)^T z \le \frac{\|x_i\|_2^2 - \|x_0\|_2^2}{2} \right\}
$$

Vì là giao của $K$ nửa không gian đóng, tập hợp $V(x_0)$ là một **tập đa diện lồi**, được gọi là **ô Voronoi** (Voronoi cell) của điểm $x_0$. Toàn bộ không gian $\mathbb{R}^n$ được phân hoạch thành các ô Voronoi lồi không chồng lấn.

Kết quả hình học này giải thích trực quan cơ chế hoạt động của hai thuật toán kinh điển trong học máy:
1. **Thuật toán phân loại láng giềng gần nhất (1-Nearest Neighbor)**: Gán nhãn cho một điểm truy vấn mới theo nhãn của điểm huấn luyện gần nó nhất, thực chất là xác định điểm mới rơi vào ô Voronoi của điểm dữ liệu nào.
2. **Thuật toán phân cụm k-means**: Tại bước gán cụm (assignment step), mỗi mẫu dữ liệu được phân vào tâm cụm gần nhất. Điều này tương đương với việc chia không gian thành các miền Voronoi tạo bởi $k$ tâm cụm hiện tại.

## 7. Siêu phẳng trong không gian hàm và ma trận

Khái niệm siêu phẳng không hề giới hạn trong không gian vector tọa độ $\mathbb{R}^n$, mà mở rộng tự nhiên sang mọi không gian vector hữu hạn hoặc vô hạn chiều có trang bị tích vô hướng:

- **Không gian các phân phối xác suất**: Xét một biến ngẫu nhiên rời rạc nhận $n$ giá trị phân biệt $v_1, \ldots, v_n$ với phân phối xác suất tương ứng $p = (p_1, \ldots, p_n)$. Ràng buộc đòi hỏi kỳ vọng của một hàm số $g(X)$ phải bằng một giá trị mong muốn $c$:
  $$
  \mathbb{E}[g(X)] = \sum_{i=1}^n p_i g(v_i) = c
  $$
  Đây là một phương trình tuyến tính theo vector phân phối $p$, do đó tập hợp tất cả các phân phối xác suất thỏa mãn ràng buộc kỳ vọng này tạo thành một siêu phẳng trong không gian phân phối xác suất.
- **Không gian ma trận đối xứng $\mathbb{S}^n$**: Với tích vô hướng Frobenius $\langle A, X \rangle = \operatorname{tr}(AX)$, ràng buộc tuyến tính:
  $$
  \operatorname{tr}(AX) = b
  $$
  xác định một siêu phẳng trong không gian các ma trận đối xứng. Những siêu phẳng này tạo nên các ràng buộc đẳng thức trong quy hoạch nửa xác định dương (Semidefinite Programming - SDP) mà chúng ta sẽ khảo sát ở Lecture 02.

## 8. Những câu hỏi để đào sâu

**Câu 1.** Hai phương trình $2x_1 - x_2 = 3$ và $-4x_1 + 2x_2 = -6$ mô tả cùng một đường thẳng trong mặt phẳng. Vậy hai bất đẳng thức $2x_1 - x_2 \le 3$ và $-4x_1 + 2x_2 \le -6$ có mô tả cùng một nửa mặt phẳng không?

<details><summary>Xem lời giải thích</summary>

Không. Bất đẳng thức thứ hai thu được bằng cách nhân bất đẳng thức thứ nhất với hệ số âm $\alpha = -2$. Khi nhân với một số âm, chiều của bất đẳng thức bị đảo ngược:

$$
-4x_1 + 2x_2 \le -6 \iff 2x_1 - x_2 \ge 3
$$

Hai nửa mặt phẳng này nằm về hai phía đối lập nhau qua cùng một đường thẳng biên $2x_1 - x_2 = 3$. Giao của hai nửa mặt phẳng này chính là đường thẳng biên. Câu hỏi này nhấn mạnh mệnh đề ở mục 5: Một nửa không gian chỉ được bảo toàn nguyên vẹn khi ta nhân phương trình với một hệ số **dương** ($\lambda > 0$).

</details>

**Câu 2.** Trong không gian ba chiều $\mathbb{R}^3$, giao của hai siêu phẳng không song song có hình dạng gì? Giao của ba siêu phẳng có thể tạo nên những cấu trúc hình học nào?

<details><summary>Xem lời giải thích</summary>

Giao của hai siêu phẳng không song song trong $\mathbb{R}^3$ là một đường thẳng, tương ứng với tập nghiệm của một hệ hai phương trình tuyến tính độc lập có một biến tự do.

Giao của ba siêu phẳng trong $\mathbb{R}^3$ có thể rơi vào một trong các trường hợp sau:
1. **Một điểm duy nhất**: Khi ba vector pháp tuyến độc lập tuyến tính, hệ có nghiệm duy nhất.
2. **Một đường thẳng**: Khi ba mặt phẳng cùng đi qua một trục chung (chẳng hạn các cánh cửa cùng gắn vào một bản lề trục đứng).
3. **Mặt phẳng**: Khi cả ba phương trình tương đương nhau.
4. **Tập rỗng**: Khi có ít nhất hai mặt phẳng song song không trùng nhau, hoặc khi ba mặt phẳng cắt nhau từng đôi một theo ba đường thẳng song song, tạo thành một hình lăng trụ rỗng ruột không có điểm chung cho cả ba.

Trong mọi trường hợp có nghiệm, giao luôn là một tập affine.

</details>

**Câu 3.** Trong bài toán khoảng cách Voronoi, nếu ta thay khoảng cách Euclid bằng khoảng cách chuẩn Manhattan $\|z - p\|_1 = |z_1 - p_1| + |z_2 - p_2|$, tập hợp các điểm gần $p$ hơn $q$ có còn là một nửa không gian nữa không?

<details><summary>Xem lời giải thích</summary>

Nói chung là không. Cơ chế triệt tiêu số hạng bậc hai $z^T z$ là một đặc tính riêng có của chuẩn Euclid nhờ đẳng thức hình bình hành và phép khai triển bình phương vô hướng.

Với chuẩn Manhattan $\ell_1$, bất đẳng thức khoảng cách:

$$
|z_1 - p_1| + |z_2 - p_2| \le |z_1 - q_1| + |z_2 - q_2|
$$

chứa các hàm giá trị tuyệt đối. Do đó đường biên ngăn cách giữa hai điểm là một **đường gấp khúc** gồm nhiều đoạn thẳng ghép lại với các hệ số góc khác nhau trong từng góc phần tư tọa độ. Tập hợp thu được không còn là một nửa mặt phẳng tuyến tính phẳng. Tính chất "phẳng" của ranh giới Voronoi là một đặc quyền riêng của chuẩn Euclid.

</details>

**Câu 4.** Để kiểm tra một điểm $x$ nằm ở phía nào của siêu phẳng $a^T x = b$, người ta có thể chỉ xét dấu của tích vô hướng $a^T x$ được không? Lối suy nghĩ này gặp bẫy sai lầm nào trong thực tế?

<details><summary>Xem lời giải thích</summary>

Lối suy nghĩ đó hoàn toàn sai lầm vì đã bỏ quên hằng số lệch $b$. Vị trí tương đối của điểm $x$ so với siêu phẳng được quyết định bởi dấu của đại lượng hiệu $a^T x - b$, chứ không phải dấu của $a^T x$.

Việc chỉ xét dấu của $a^T x$ chỉ đúng trong trường hợp đặc biệt khi $b = 0$, nghĩa là siêu phẳng đi qua gốc tọa độ. Trong học máy, đây là lỗi kinh điển khi lập trình viên quên cộng hệ số chặn (bias term $b$) vào mô hình phân loại tuyến tính.

</details>

## 9. Bài tập tự luyện

::: exercise 1. Xác định các tham số hình học của siêu phẳng
Cho siêu phẳng trong không gian ba chiều $\mathbb{R}^3$:

$$
H = \{x \in \mathbb{R}^3 \mid x_1 - 2x_2 + 2x_3 = 6\}
$$

Hãy tìm:
1. Vector pháp tuyến đơn vị của siêu phẳng.
2. Khoảng cách ngắn nhất từ gốc tọa độ $O = (0, 0, 0)$ tới siêu phẳng.
3. Tọa độ điểm $x_0$ trên siêu phẳng nằm gần gốc tọa độ nhất.
4. Khoảng cách có dấu từ điểm $P = (1, 1, 1)$ tới siêu phẳng và kết luận điểm $P$ thuộc nửa không gian nào.
:::

::: solution
1. Vector pháp tuyến là $a = (1, -2, 2)$. Độ dài chuẩn Euclid:
   $$
   \|a\|_2 = \sqrt{1^2 + (-2)^2 + 2^2} = \sqrt{1 + 4 + 4} = \sqrt{9} = 3
   $$
   Vector pháp tuyến đơn vị là:
   $$
   u = \frac{a}{\|a\|_2} = \left(\frac{1}{3},\ -\frac{2}{3},\ \frac{2}{3}\right)
   $$
2. Khoảng cách ngắn nhất từ gốc tọa độ tới siêu phẳng là:
   $$
   d(O, H) = \frac{|b|}{\|a\|_2} = \frac{|6|}{3} = 2
   $$
3. Điểm gần gốc tọa độ nhất trên siêu phẳng là hình chiếu của gốc tọa độ:
   $$
   x_0 = \frac{b}{\|a\|_2^2}\, a = \frac{6}{9} (1, -2, 2) = \frac{2}{3} (1, -2, 2) = \left(\frac{2}{3},\ -\frac{4}{3},\ \frac{4}{3}\right)
   $$
   Kiểm tra phương trình: $\tfrac{2}{3} - 2(-\tfrac{4}{3}) + 2(\tfrac{4}{3}) = \tfrac{2 + 8 + 8}{3} = \tfrac{18}{3} = 6$.
4. Với điểm $P = (1, 1, 1)$, ta tính giá trị tích vô hướng:
   $$
   a^T P = 1(1) - 2(1) + 2(1) = 1 - 2 + 2 = 1
   $$
   Khoảng cách có dấu từ điểm $P$ tới siêu phẳng là:
   $$
   \operatorname{dist}_{\text{signed}}(P, H) = \frac{a^T P - b}{\|a\|_2} = \frac{1 - 6}{3} = -\frac{5}{3}
   $$
   Vì khoảng cách có dấu âm ($-\tfrac{5}{3} < 0$), điểm $P$ nằm ở nửa không gian $\{x \in \mathbb{R}^3 \mid x_1 - 2x_2 + 2x_3 \le 6\}$, cách siêu phẳng đúng $\tfrac{5}{3}$ đơn vị độ dài về phía đối diện với hướng của vector $a$.
:::

::: exercise 2. Khoảng cách giữa hai mặt phẳng song song
Tính khoảng cách hình học giữa hai siêu phẳng song song trong $\mathbb{R}^3$:

$$
H_1: 2x_1 + x_2 - 2x_3 = 4 \quad \text{và} \quad H_2: -4x_1 - 2x_2 + 4x_3 = 10
$$
:::

::: hint
Đưa hai phương trình về cùng một vector pháp tuyến trước khi áp dụng công thức khoảng cách.
:::

::: solution
Phương trình thứ hai có thể viết lại bằng cách chia cả hai vế cho $-2$:

$$
2x_1 + x_2 - 2x_3 = -5
$$

Bây giờ hai siêu phẳng đã có cùng vector pháp tuyến $a = (2, 1, -2)$ với $b_1 = 4$ và $b_2 = -5$.

Tính độ dài chuẩn của vector pháp tuyến:

$$
\|a\|_2 = \sqrt{2^2 + 1^2 + (-2)^2} = \sqrt{4 + 1 + 4} = \sqrt{9} = 3
$$

Khoảng cách giữa hai siêu phẳng song song là:

$$
\operatorname{dist}(H_1, H_2) = \frac{|b_1 - b_2|}{\|a\|_2} = \frac{|4 - (-5)|}{3} = \frac{9}{3} = 3
$$
:::

::: exercise 3. Miền Voronoi của ba điểm trong mặt phẳng
Trong mặt phẳng $\mathbb{R}^2$, cho ba điểm: $x_0 = (0, 0)$, $x_1 = (2, 0)$ và $x_2 = (0, 2)$. Hãy thiết lập hệ bất đẳng thức mô tả ô Voronoi $V(x_0)$ của điểm $x_0$ và giải thích đặc điểm hình học của miền này.
:::

::: solution
Ô Voronoi $V(x_0)$ gồm các điểm $z = (z_1, z_2)$ gần $x_0$ hơn cả $x_1$ và $x_2$:

1. **Điều kiện gần $x_0$ hơn $x_1$**:
   $$
   (x_1 - x_0)^T z \le \frac{\|x_1\|_2^2 - \|x_0\|_2^2}{2}
   $$
   Với $x_1 - x_0 = (2, 0)$, $\|x_1\|_2^2 = 4$, $\|x_0\|_2^2 = 0$, ta có:
   $$
   2z_1 + 0z_2 \le \frac{4 - 0}{2} = 2 \iff z_1 \le 1
   $$
2. **Điều kiện gần $x_0$ hơn $x_2$**:
   $$
   (x_2 - x_0)^T z \le \frac{\|x_2\|_2^2 - \|x_0\|_2^2}{2}
   $$
   Với $x_2 - x_0 = (0, 2)$, $\|x_2\|_2^2 = 4$, $\|x_0\|_2^2 = 0$, ta có:
   $$
   0z_1 + 2z_2 \le \frac{4 - 0}{2} = 2 \iff z_2 \le 1
   $$

Kết hợp hai điều kiện, ô Voronoi $V(x_0)$ là tập hợp:

$$
V(x_0) = \{z \in \mathbb{R}^2 \mid z_1 \le 1,\ z_2 \le 1\}
$$

Về mặt hình học, đây là một góc phần tư không bị chặn có đỉnh tại $(1, 1)$, mở rộng vô hạn về phía dưới và bên trái. Miền này không bị chặn vì điểm $x_0$ không bị các điểm dữ liệu khác bao bọc từ mọi phía.
:::

## Tóm tắt

Siêu phẳng $\{x \in \mathbb{R}^n \mid a^T x = b\}$ với $a \ne 0$ là một tập affine có số chiều $n - 1$, trực giao với vector pháp tuyến $a$ và cách gốc tọa độ một khoảng bằng $\tfrac{|b|}{\|a\|_2}$. Siêu phẳng có biểu diễn tương đương là $x_0 + a^\perp$, trong đó $x_0$ là một điểm mốc bất kỳ trên siêu phẳng và $a^\perp$ là phần bù trực giao của $a$.

Nửa không gian $\{x \in \mathbb{R}^n \mid a^T x \le b\}$ là một tập lồi nhưng không affine, trải rộng về phía ngược lại với hướng của vector pháp tuyến $a$. Vector $a$ đóng vai trò là pháp tuyến hướng ra ngoài, và nửa không gian bao gồm các vector tạo với $a$ một góc tù hoặc góc vuông.

Đại lượng $\tfrac{a^T x - b}{\|a\|_2}$ biểu diễn khoảng cách có dấu từ điểm $x$ tới siêu phẳng. Đây chính là biên hình học trong các mô hình phân loại tuyến tính và máy vector hỗ trợ (SVM). Một nửa không gian bị chứa trong một nửa không gian khác khi và chỉ khi bất đẳng thức thứ hai là một bội số dương của bất đẳng thức thứ nhất với ngưỡng biên được nới lỏng. Tập hợp các điểm nằm gần một điểm mốc hơn một điểm mốc khác theo khoảng cách Euclid là một nửa không gian trung trực, cấu thành nên các ô Voronoi lồi trong phân loại và phân cụm dữ liệu.

## Tài liệu tham khảo

- Stephen Boyd, Lieven Vandenberghe, *Convex Optimization*, Cambridge University Press.
