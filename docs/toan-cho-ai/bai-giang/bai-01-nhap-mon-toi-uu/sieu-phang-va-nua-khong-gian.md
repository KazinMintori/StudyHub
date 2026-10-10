---
course: toan-cho-ai
lecture: bai-01-nhap-mon-toi-uu
topic: sieu-phang-va-nua-khong-gian
section: topic
title: "Siêu phẳng và nửa không gian"
description: "Siêu phẳng như tập nghiệm của một phương trình tuyến tính, vector pháp tuyến và độ lệch, biểu diễn x₀ + a⊥, nửa không gian và pháp tuyến hướng ra ngoài, khoảng cách có dấu, quan hệ chứa giữa hai nửa không gian và nửa không gian Voronoi."
---

Một phương trình tuyến tính duy nhất, chẳng hạn $3x_1 + 4x_2 = 10$, có thể được đọc theo hai cách. Người làm đại số thấy một ràng buộc giữa hai ẩn và đi tìm nghiệm. Người làm hình học thấy một đường thẳng trong mặt phẳng. Trong $\mathbb{R}^3$, phương trình $3x_1 + 4x_2 + x_3 = 10$ là một mặt phẳng, và trong $\mathbb{R}^n$ nó là một **siêu phẳng**: Một "mặt phẳng" có số chiều $n - 1$, mỏng hơn không gian chứa nó đúng một chiều.

Siêu phẳng và nửa không gian là những viên gạch nhỏ nhất của hình học lồi. Đa diện được ghép từ nửa không gian, tập lồi đóng bất kỳ là giao của các nửa không gian chứa nó, và định lý siêu phẳng phân tách ở cuối phần hình học nói rằng hai tập lồi rời nhau luôn ngăn được bằng một siêu phẳng. Nội dung này giúp người học giải mã toàn diện các đặc trưng hình học của một siêu phẳng trực tiếp từ phương trình đại số: Xác định hướng vuông góc, khoảng cách tới gốc tọa độ và vị trí tương đối của một điểm bất kỳ.

## 1. Định nghĩa và cách đọc thứ nhất

> **Định nghĩa.** Một **siêu phẳng** là tập có dạng $\{x : a^T x = b\}$, trong đó $a \in \mathbb{R}^n$, $a \ne 0$ và $b \in \mathbb{R}$.

Về mặt giải tích, siêu phẳng là tập nghiệm của một phương trình tuyến tính không tầm thường, nên theo chủ đề về tập affine, nó là một tập affine. Điều kiện $a \ne 0$ loại bỏ phương trình suy biến $0 = b$, vốn vô nghiệm khi $b \ne 0$ và nhận mọi điểm làm nghiệm khi $b = 0$.

Về mặt hình học, ta có cách diễn giải trực quan thứ nhất: Siêu phẳng là **tập các điểm có cùng tích vô hướng $b$ với vector $a$**. Để thấy cách diễn giải này nói lên điều gì, hãy nhớ rằng $\tfrac{a^T x}{\|a\|_2}$ là độ dài có dấu của hình chiếu của $x$ lên đường thẳng theo hướng $a$. Vì thế phương trình $a^T x = b$ có nghĩa là "hình chiếu của $x$ lên trục theo hướng $a$ luôn ở cùng một vị trí $\tfrac{b}{\|a\|_2}$". Tất cả những điểm có cùng hình chiếu như vậy tạo thành một siêu phẳng **vuông góc với $a$**, đi qua điểm nằm trên trục đó cách gốc một khoảng có dấu bằng $\tfrac{b}{\|a\|_2}$.

Vector $a$ được gọi là **vector pháp tuyến** của siêu phẳng, còn hằng số $b$ quyết định độ lệch của siêu phẳng so với gốc. Hai cách biến đổi phương trình mang lại hai hiệu ứng hình học khác biệt cần được phân biệt rạch ròi: Nhân cả $a$ và $b$ với cùng một số khác 0 thì siêu phẳng **không đổi** do phương trình mới tương đương; còn nếu chỉ thay đổi $b$ và giữ nguyên $a$, siêu phẳng sẽ **tịnh tiến song song** theo hướng pháp tuyến $a$.

::: example Đọc một siêu phẳng trong mặt phẳng
Xét $3x_1 + 4x_2 = 10$, tức $a = (3, 4)$ và $b = 10$. Vì $\|a\|_2 = 5$, đường thẳng vuông góc với $(3, 4)$ và cách gốc $\tfrac{10}{5} = 2$. Điểm của đường thẳng gần gốc nhất là

$$
x_0 = \frac{b}{\|a\|_2^2}\, a = \frac{10}{25}(3, 4) = (1.2,\ 1.6),
$$

và quả thật $3 \cdot 1.2 + 4 \cdot 1.6 = 3.6 + 6.4 = 10$. Một vector chỉ phương của đường thẳng là $d = (4, -3)$, vì $a^T d = 12 - 12 = 0$.
:::

## 2. Cách đọc thứ hai: Một điểm cộng với mọi hướng vuông góc

Chọn một điểm bất kỳ $x_0$ trên siêu phẳng, tức một điểm có $a^T x_0 = b$. Khi đó $a^T x = b$ tương đương với $a^T x = a^T x_0$, hay

$$
a^T (x - x_0) = 0 .
$$

Phương trình cuối nói rằng vector $x - x_0$, đi từ $x_0$ tới $x$, vuông góc với $a$. Gọi $a^{\perp} = \{v : a^T v = 0\}$ là **phần bù trực giao** của $a$, tập mọi vector vuông góc với $a$. Ta được

$$
\{x : A^T x = b\} = x_0 + a^{\perp}.
$$

Đây đúng là cấu trúc "không gian con được tịnh tiến" của mọi tập affine: Không gian con đi kèm là $a^{\perp}$, có số chiều $n - 1$, và điểm tịnh tiến là $x_0$. Hình minh họa hình học thể hiện rõ điều này: Từ một điểm $x_0$ trên siêu phẳng, mọi vector $x - x_0$ nằm trong siêu phẳng đều trực giao với pháp tuyến $a$.

## 3. Nửa không gian

Một siêu phẳng chia $\mathbb{R}^n$ thành hai nửa.

> **Định nghĩa.** Một **nửa không gian đóng** là tập có dạng $\{x : a^T x \le b\}$ với $a \ne 0$, tức là tập nghiệm của một bất đẳng thức tuyến tính không tầm thường.

Nửa không gian lồi nhưng không affine. Tính lồi suy ra trực tiếp: Nếu $a^T x_1 \le b$, $a^T x_2 \le b$ và $\theta \in [0, 1]$, thì

$$
a^T(\theta x_1 + (1-\theta)x_2) = \theta a^T x_1 + (1-\theta) a^T x_2 \le \theta b + (1 - \theta) b = b,
$$

trong đó bước bất đẳng thức cần $\theta \ge 0$ và $1 - \theta \ge 0$. Nó không affine vì với $\theta$ lớn, điểm $\theta x_1 + (1-\theta)x_2$ có thể vượt qua biên.

Nửa không gian $a^T x \le b$ nằm về phía **ngược** với hướng của $a$. Lý do là khi đi theo hướng $a$, giá trị $a^T x$ tăng, nên muốn giữ $a^T x \le b$ ta phải ở phía $-a$. Vì vậy ta gọi $a$ là **pháp tuyến hướng ra ngoài** (outward normal) của nửa không gian $\{a^T x \le b\}$. Ngược lại, nửa không gian $\{a^T x \ge b\}$ mở rộng theo hướng $a$.

Viết lại với một điểm $x_0$ trên biên, nửa không gian là $\{x : a^T(x - x_0) \le 0\}$. Cách viết này đem lại một hình ảnh trực quan sinh động: Nửa không gian gồm $x_0$ cộng với mọi vector tạo với $a$ một **góc tù hoặc góc vuông**. Một điểm $x$ mà vector $x - x_0$ tạo góc nhọn với $a$ thì nằm ngoài.

Biên của nửa không gian $\{a^T x \le b\}$ là siêu phẳng $\{a^T x = b\}$. Bỏ biên đi, ta được **nửa không gian mở** $\{a^T x < b\}$, chính là phần trong của nửa không gian đóng.

<HyperplaneLab type="halfspace" />

## 4. Khoảng cách có dấu và ý nghĩa của giá trị $a^T x - b$

Trong mô phỏng, con số được tính cho điểm thử $x$ là $\tfrac{a^T x - b}{\|a\|_2}$. Đây là **khoảng cách có dấu** từ $x$ tới siêu phẳng: Trị tuyệt đối của nó là khoảng cách thông thường, còn dấu cho biết $x$ ở phía nào.

Để thấy vì sao, gọi $x_0$ là một điểm bất kỳ trên siêu phẳng. Khoảng cách từ $x$ tới siêu phẳng là độ dài hình chiếu của $x - x_0$ lên hướng pháp tuyến đơn vị $\tfrac{a}{\|a\|_2}$, bởi vì thành phần của $x - x_0$ dọc theo siêu phẳng không làm thay đổi khoảng cách. Độ dài có dấu của hình chiếu đó là

$$
\frac{a^T(x - x_0)}{\|a\|_2} = \frac{a^T x - a^T x_0}{\|a\|_2} = \frac{a^T x - b}{\|a\|_2}.
$$

Với siêu phẳng $3x_1 + 4x_2 = 10$ ở ví dụ trên, điểm $(4, 2)$ cho $\tfrac{12 + 8 - 10}{5} = 2$: Nó cách đường thẳng 2 đơn vị, về phía $a$ chỉ tới. Gốc tọa độ cho $\tfrac{0 - 10}{5} = -2$: Cũng cách 2 đơn vị, nhưng ở phía bên kia.

Công thức này cũng áp dụng trực tiếp để tính khoảng cách giữa hai siêu phẳng song song $\{a^T x = b_1\}$ và $\{a^T x = b_2\}$. Lấy một điểm trên siêu phẳng thứ nhất, khoảng cách có dấu của nó tới siêu phẳng thứ hai là $\tfrac{b_1 - b_2}{\|a\|_2}$. Vậy hai siêu phẳng cách nhau $\tfrac{|b_1 - b_2|}{\|a\|_2}$. Hãy bật siêu phẳng thứ hai trong mô phỏng và đối chiếu.

Giá trị $a^T x - b$, chưa chia cho $\|a\|_2$, cũng có tên riêng trong học máy. Một bộ phân loại tuyến tính tính **điểm số** $s(x) = w^T x + b$ và gán nhãn theo dấu của nó. Ranh giới quyết định $\{x : w^T x + b = 0\}$ là một siêu phẳng, và $\tfrac{s(x)}{\|w\|_2}$ là khoảng cách có dấu từ điểm dữ liệu tới ranh giới. Điểm số lớn về trị tuyệt đối nghĩa là điểm nằm xa ranh giới. Tuy vậy, chỉ so sánh điểm số thì chưa đủ để nói về độ "chắc chắn" của mô hình: Nhân $w$ và $b$ với 10 thì ranh giới y nguyên nhưng mọi điểm số lớn gấp 10. Khoảng cách hình học mới không phụ thuộc vào cách viết phương trình. Ý tưởng chọn siêu phẳng sao cho khoảng cách tới điểm dữ liệu gần nhất là lớn nhất chính là gốc rễ của máy vector hỗ trợ (SVM).

## 5. Khi nào một nửa không gian chứa một nửa không gian khác?

Câu hỏi này tưởng như chỉ là một mệnh đề giải tích thuần túy, nhưng câu trả lời lại là khuôn mẫu căn bản cho các lập luận đối ngẫu sâu sắc về sau.

> **Mệnh đề.** Với $a \ne 0$ và $\tilde a \ne 0$, ta có $\{x : a^T x \le b\} \subseteq \{x : \tilde a^T x \le \tilde b\}$ khi và chỉ khi tồn tại $\lambda > 0$ sao cho $\tilde a = \lambda a$ và $\tilde b \ge \lambda b$. Hai nửa không gian bằng nhau khi và chỉ khi $\tilde a = \lambda a$ và $\tilde b = \lambda b$ với một $\lambda > 0$.

Chiều "nếu" là một phép nhân. Nếu $a^T x \le b$ thì $\tilde a^T x = \lambda a^T x \le \lambda b \le \tilde b$, trong đó bước nhân giữ chiều bất đẳng thức vì $\lambda > 0$.

Chiều "chỉ nếu" thú vị hơn, vì nó cho thấy khi nào một bất đẳng thức tuyến tính là hệ quả của một bất đẳng thức khác. Giả sử có quan hệ chứa. Nếu $\tilde a$ không cùng phương với $a$, ta tìm được một hướng $d$ với $a^T d = 0$ nhưng $\tilde a^T d \ne 0$ (chẳng hạn hình chiếu của $\tilde a$ lên $a^{\perp}$, vốn khác 0). Đi từ một điểm của nửa không gian thứ nhất theo hướng $\pm d$, ta ở lại nửa không gian đó mãi mãi vì $a^T x$ không đổi, trong khi $\tilde a^T x$ tăng không giới hạn theo một trong hai chiều. Như vậy có điểm thuộc nửa không gian thứ nhất mà không thuộc nửa không gian thứ hai, mâu thuẫn. Do đó $\tilde a = \lambda a$. Nếu $\lambda < 0$, đi theo hướng $-a$ thì $a^T x$ giảm nên ta ở lại nửa không gian thứ nhất, nhưng $\tilde a^T x = \lambda a^T x$ tăng vô hạn, lại mâu thuẫn. Vậy $\lambda > 0$. Cuối cùng, giá trị lớn nhất của $\tilde a^T x = \lambda a^T x$ trên nửa không gian thứ nhất là $\lambda b$, đạt trên biên, nên quan hệ chứa buộc $\lambda b \le \tilde b$.

Kết luận đáng nhớ là: Một bất đẳng thức tuyến tính chỉ suy ra được một bất đẳng thức tuyến tính khác khi bất đẳng thức sau là **bội dương** của bất đẳng thức trước, có thể nới thêm vế phải. Ở chủ đề về hai dạng bài toán kinh điển, ta đã chứng nhận nghiệm một LP bằng tổ hợp không âm của nhiều ràng buộc. Mệnh đề này là trường hợp một ràng buộc của cùng ý tưởng, và bổ đề Farkas ở chủ đề về siêu phẳng phân tách sẽ là trường hợp nhiều ràng buộc tổng quát.

## 6. Nửa không gian Voronoi

Cho hai điểm khác nhau $p$ và $q$. Tập các điểm gần $p$ hơn gần $q$ (theo khoảng cách Euclid) có hình dạng gì? Trực giác hình học phổ thông nói đó là nửa mặt phẳng giới hạn bởi đường trung trực của đoạn $pq$. Công cụ đại số tuyến tính xác nhận điều đó tổng quát trong mọi số chiều. Bình phương hai vế của $\|z - p\|_2 \le \|z - q\|_2$ rồi khai triển:

$$
z^T z - 2p^T z + p^T p \le z^T z - 2 q^T z + q^T q \iff (q - p)^T z \le \frac{\|q\|_2^2 - \|p\|_2^2}{2}.
$$

Số hạng $z^T z$ xuất hiện ở cả hai vế và triệt tiêu, nên điều kiện trở thành tuyến tính theo $z$. Đây là một nửa không gian với pháp tuyến hướng ra ngoài là $q - p$, tức chỉ từ $p$ sang $q$. Chẳng hạn với $p = (0, 0)$ và $q = (4, 2)$, ta được $4z_1 + 2z_2 \le 10$, tức $2z_1 + z_2 \le 5$. Điểm $z = (1, 1)$ cho $3 \le 5$, và quả thật nó cách $p$ khoảng $1.41$, cách $q$ khoảng $3.16$.

<HyperplaneLab type="voronoi" />

Kết quả nhỏ này có hệ quả lớn. Với $K + 1$ điểm $x_0, x_1, \ldots, x_K$, tập các điểm gần $x_0$ hơn mọi điểm khác là giao của $K$ nửa không gian như trên, nên là một đa diện, gọi là **miền Voronoi** (Voronoi region) của điểm $x_0$. Bộ phân loại láng giềng gần nhất, khi gán cho một điểm mới nhãn của điểm dữ liệu gần nó nhất, thực chất chia không gian thành các miền Voronoi. Bước gán cụm trong thuật toán k-means cũng vậy: Mỗi điểm thuộc về tâm cụm gần nhất, nên các cụm được ngăn cách bởi những siêu phẳng trung trực.

## 7. Siêu phẳng ở những nơi không ngờ tới

Siêu phẳng cũng xuất hiện ngoài không gian các vector tọa độ. Bất kỳ ràng buộc tuyến tính nào trên bất kỳ không gian vector nào cũng là một siêu phẳng. Hai ví dụ:

- Trong không gian các phân phối xác suất $p = (p_1, \ldots, p_n)$ của một biến ngẫu nhiên nhận các giá trị $a_1, \ldots, a_n$, ràng buộc "kỳ vọng của $f(x)$ bằng $c$" được viết là $\sum_{i=1}^{n} p_i f(a_i) = c$. Đây là một phương trình tuyến tính theo $p$, nên các phân phối thỏa ràng buộc nằm trên một siêu phẳng. Đó là lý do nhiều bài toán thống kê với ràng buộc về kỳ vọng lại thuộc họ bài toán lồi theo phân phối xác suất.
- Trong không gian các ma trận đối xứng, ràng buộc $\operatorname{tr}(AX) = b$ là tuyến tính theo $X$, nên định nghĩa một siêu phẳng của không gian ma trận. Ta sẽ gặp những siêu phẳng như vậy trong quy hoạch nửa xác định ở Lecture 02.

## 8. Những câu hỏi để đào sâu

**Câu 1.** Hai phương trình $2x_1 - x_2 = 3$ và $-4x_1 + 2x_2 = -6$ mô tả cùng một đường thẳng. Còn hai bất đẳng thức $2x_1 - x_2 \le 3$ và $-4x_1 + 2x_2 \le -6$ có mô tả cùng một nửa mặt phẳng không?

<details><summary>Xem lời giải thích</summary>

Không. Bất đẳng thức thứ hai thu được bằng cách nhân bất đẳng thức thứ nhất với hệ số âm $-2$, do đó chiều bất đẳng thức bị đảo ngược: Biến đổi tương đương chỉ ra $-4x_1 + 2x_2 \le -6 \iff 2x_1 - x_2 \ge 3$. Hai nửa mặt phẳng nằm về hai phía của cùng một đường biên, và giao của chúng chính là đường thẳng. Câu hỏi minh họa mệnh đề ở mục 5: Nửa không gian chỉ không đổi khi nhân với hệ số **dương**.

</details>

**Câu 2.** Trong $\mathbb{R}^3$, giao của hai siêu phẳng không song song là gì? Giao của ba siêu phẳng thì có thể là những tập nào?

<details><summary>Xem lời giải thích</summary>

Giao của hai mặt phẳng không song song trong $\mathbb{R}^3$ là một đường thẳng, vì hệ hai phương trình độc lập có không gian nghiệm thuần nhất một chiều. Giao của ba mặt phẳng thì có ba khả năng:

- Một điểm, khi ba pháp tuyến độc lập tuyến tính,
- Một đường thẳng, khi cả ba mặt phẳng cùng giao nhau tại một trục đường thẳng duy nhất,
- Tập rỗng, chẳng hạn khi có hai mặt song song, hoặc khi ba mặt phẳng cắt nhau từng đôi một theo ba đường song song, tạo thành một lăng trụ tam giác rỗng ruột.

Trong mọi trường hợp, giao là một tập affine, vì nó là tập nghiệm của một hệ tuyến tính.

</details>

**Câu 3.** Trong bài toán Voronoi, nếu thay khoảng cách Euclid bằng khoảng cách $\|z - p\|_1$ thì tập các điểm gần $p$ hơn $q$ có còn là nửa không gian không? Thử với $p = (0, 0)$ và $q = (2, 1)$.

<details><summary>Xem lời giải thích</summary>

Nói chung là không. Mẹo triệt tiêu $z^T z$ chỉ hoạt động với chuẩn Euclid, vì nó dựa trên việc khai triển bình phương. Với chuẩn $\ell_1$, biên của tập $\{z : |z_1| + |z_2| \le |z_1 - 2| + |z_2 - 1|\}$ là một đường gấp khúc. Chẳng hạn trong vùng $0 \le z_1 \le 2$ và $0 \le z_2 \le 1$, điều kiện trở thành $z_1 + z_2 \le (2 - z_1) + (1 - z_2)$, tức $z_1 + z_2 \le 1.5$. Còn trong vùng $z_2 \ge 1$ và $0 \le z_1 \le 2$, điều kiện là $z_1 + z_2 \le (2 - z_1) + (z_2 - 1)$, tức $z_1 \le 0.5$. Hai mảnh biên có hướng khác nhau, nên tập không phải một nửa mặt phẳng. Tính "phẳng" của biên Voronoi là một đặc ân riêng của khoảng cách Euclid.

</details>

**Câu 4.** Để biết điểm $x$ nằm phía nào của siêu phẳng $\{x : a^T x = b\}$, chỉ so $a^T x$ với 0 có được không? Khi nào cách làm đó vẫn đúng?

<details><summary>Xem lời giải thích</summary>

Cách làm đó quên độ lệch $b$. Phía của $x$ được quyết định bởi dấu của $a^T x - b$, không phải dấu của $a^T x$. Cách làm chỉ đúng khi $b = 0$, tức siêu phẳng đi qua gốc. Trong học máy, lỗi tương tự là quên hệ số chặn của bộ phân loại tuyến tính. Đó cũng là lý do người ta hay gộp hệ số chặn vào $w$ bằng cách thêm một đặc trưng luôn bằng 1: Siêu phẳng trong không gian mở rộng khi đó luôn đi qua gốc.

</details>

## 9. Bài tập tự luyện

::: exercise 1. Đọc nhanh một siêu phẳng
Cho siêu phẳng $\{x \in \mathbb{R}^3 : x_1 - 2x_2 + 2x_3 = 6\}$. Tìm pháp tuyến, khoảng cách từ gốc tới siêu phẳng, điểm của siêu phẳng gần gốc nhất, và khoảng cách có dấu của điểm $(1, 1, 1)$.
:::

::: solution
Pháp tuyến $a = (1, -2, 2)$ với $\|a\|_2 = \sqrt{1 + 4 + 4} = 3$. Khoảng cách từ gốc là $\tfrac{6}{3} = 2$, và điểm gần gốc nhất là $x_0 = \tfrac{6}{9}(1, -2, 2) = (\tfrac23, -\tfrac43, \tfrac43)$. Kiểm tra: Ta có $\tfrac23 + \tfrac83 + \tfrac83 = 6$. Với $x = (1, 1, 1)$, $a^T x = 1 - 2 + 2 = 1$, nên khoảng cách có dấu là $\tfrac{1 - 6}{3} = -\tfrac53$. Điểm nằm cách siêu phẳng $\tfrac53$ đơn vị, về phía ngược với $a$, tức thuộc nửa không gian $a^T x \le 6$.
:::

::: exercise 2. Hai siêu phẳng song song
Tính khoảng cách giữa hai siêu phẳng $2x_1 + x_2 - 2x_3 = 4$ và $-4x_1 - 2x_2 + 4x_3 = 10$.
:::

::: hint
Trước tiên viết hai phương trình với cùng một vector pháp tuyến.
:::

::: solution
Chia phương trình thứ hai cho $-2$ được $2x_1 + x_2 - 2x_3 = -5$. Hai siêu phẳng có cùng $a = (2, 1, -2)$ với $\|a\|_2 = 3$, và $b_1 = 4$, $b_2 = -5$. Khoảng cách là $\tfrac{|4 - (-5)|}{3} = 3$. Nếu quên đưa về cùng pháp tuyến mà áp công thức với $b_2 = 10$, ta sẽ được kết quả sai.
:::

::: exercise 3. Miền Voronoi của ba điểm
Cho $x_0 = (0, 0)$, $x_1 = (2, 0)$, $x_2 = (0, 2)$. Viết miền Voronoi của $x_0$ dưới dạng $\{z : Az \preceq c\}$ và mô tả nó bằng lời.
:::

::: solution
Gần $x_0$ hơn $x_1$: Ta có $(x_1 - x_0)^T z \le \tfrac{\|x_1\|^2 - \|x_0\|^2}{2}$, tức $2z_1 \le 2$, hay $z_1 \le 1$. Gần $x_0$ hơn $x_2$: Ta có $2z_2 \le 2$, hay $z_2 \le 1$. Vậy miền Voronoi là $\{z : z_1 \le 1,\ z_2 \le 1\}$, với $A = I$ và $c = (1, 1)$. Đó là một góc phần tư được dịch tới đỉnh $(1, 1)$, gồm mọi điểm ở bên trái đường $z_1 = 1$ và bên dưới đường $z_2 = 1$. Miền này không bị chặn, vì $x_0$ không bị các điểm khác bao quanh.
:::

## Tóm tắt

Siêu phẳng $\{x : a^T x = b\}$ với $a \ne 0$ là tập affine có số chiều $n - 1$, vuông góc với pháp tuyến $a$, và cách gốc một khoảng $\tfrac{|b|}{\|a\|_2}$. Nó bằng $x_0 + a^{\perp}$ với $x_0$ là một điểm bất kỳ trên siêu phẳng. Nửa không gian $\{x : a^T x \le b\}$ là tập lồi không affine, nằm về phía ngược với $a$, và gồm những điểm mà vector từ $x_0$ tới chúng tạo với $a$ góc tù hoặc vuông.

Đại lượng $\tfrac{a^T x - b}{\|a\|_2}$ là khoảng cách có dấu từ $x$ tới siêu phẳng, và điểm số của một bộ phân loại tuyến tính chính là đại lượng này nhân với $\|w\|_2$. Một nửa không gian chứa nửa không gian khác khi và chỉ khi bất đẳng thức thứ hai là bội dương của bất đẳng thức thứ nhất với vế phải nới thêm. Tập các điểm gần một điểm hơn một điểm khác, theo khoảng cách Euclid, là một nửa không gian, và đó là nền tảng của miền Voronoi.

## Tài liệu tham khảo

- Stephen Boyd, Lieven Vandenberghe, *Convex Optimization*, Cambridge University Press.
