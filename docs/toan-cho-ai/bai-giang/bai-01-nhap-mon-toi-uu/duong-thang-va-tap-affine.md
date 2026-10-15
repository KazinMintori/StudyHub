---
course: toan-cho-ai
lecture: bai-01-nhap-mon-toi-uu
topic: duong-thang-va-tap-affine
section: topic
title: "Đường thẳng, đoạn thẳng và tập affine"
description: "Tham số hóa đường thẳng bằng θ, tập affine, tổ hợp affine, ý nghĩa của điều kiện tổng hệ số bằng 1, cấu trúc không gian con tịnh tiến, tập nghiệm của Ax = b và bao affine."
---

Ở bậc phổ thông, đường thẳng trong mặt phẳng thường được làm quen qua phương trình đại số quen thuộc $y = ax + b$. Cách biểu diễn này trực quan khi vẽ đồ thị hàm số, tuy nhiên lại bộc lộ hai hạn chế lớn khi bước vào lĩnh vực tối ưu hóa và trí tuệ nhân tạo. Thứ nhất, nó hoàn toàn bất lực trước các đường thẳng đứng vuông góc với trục hoành, bởi khi đó hệ số góc $a$ tiến tới vô cực. Thứ hai, cách tiếp cận này bị trói buộc chặt chẽ trong không gian hai chiều $\mathbb{R}^2$. Trong học máy hiện đại, không gian tham số của một mô hình học sâu thường chứa hàng triệu hoặc hàng tỷ chiều, nơi ta không thể dùng phương trình hai biến để khảo sát quỹ đạo tham số.

Chính vì vậy, ta cần một phương pháp mô tả đường thẳng, đoạn thẳng và các cấu trúc phẳng hoạt động nhất quán trên không gian $\mathbb{R}^n$ với số chiều tùy ý. Phương pháp này xuất phát từ một trực giác vật lý hết sức gần gũi: Chọn một điểm xuất phát làm mốc, định hướng nhìn về một điểm thứ hai, sau đó di chuyển một quãng đường theo hướng đó. Tư duy hình học này dẫn trực tiếp tới khái niệm **tập affine**. Khái niệm này làm sáng tỏ cấu trúc hình học của tập nghiệm hệ phương trình tuyến tính, đồng thời giải mã lý do vì sao điều kiện "tổng các trọng số bằng 1" lại xuất hiện xuyên suốt trong giải tích lồi và học máy.

Để tiếp thu bài học một cách tự nhiên và trọn vẹn nhất, kiến thức nền tảng cần nhớ là các phép toán vector cơ bản gồm phép cộng vector, phép nhân vô hướng với một số thực, cùng khái niệm không gian con tuyến tính (về mặt hình học, đó là các đường thẳng, mặt phẳng hoặc siêu phẳng đi qua gốc tọa độ).

## 1. Điểm chạy trên đường thẳng và tham số hóa hình học

Giả sử ta xét hai điểm phân biệt $x_1, x_2 \in \mathbb{R}^n$. Với mỗi số thực $\theta \in \mathbb{R}$, ta lập biểu thức:

$$
y = \theta x_1 + (1-\theta)\,x_2 .
$$

Khi tham số $\theta$ quét qua toàn bộ trục số thực $\mathbb{R}$, tập hợp các điểm $y$ vạch nên trọn vẹn đường thẳng duy nhất đi qua hai điểm $x_1$ và $x_2$. Ta có thể kiểm tra ngay hai mốc tọa độ đặc biệt:
- Khi $\theta = 0$, điểm thu được chính là $y = 0 \cdot x_1 + 1 \cdot x_2 = x_2$.
- Khi $\theta = 1$, điểm thu được chính là $y = 1 \cdot x_1 + 0 \cdot x_2 = x_1$.

Để hiểu rõ bản chất chuyển động học của điểm $y$, ta gom nhóm các số hạng chứa $\theta$:

$$
y = x_2 + \theta\,(x_1 - x_2).
$$

Biểu thức trên mô tả một hành trình chuyển động rất rõ ràng:
1. Điểm xuất phát ban đầu là vị trí mốc $x_2$.
2. Vector chỉ phương dẫn đường là hiệu hai vector $x_1 - x_2$, tức vector có hướng từ vị trí $x_2$ hướng thẳng tới vị trí $x_1$.
3. Tham số $\theta$ đóng vai trò là hệ số khuếch đại, xác định tỉ lệ khoảng cách tương đối mà ta di chuyển dọc theo vector định hướng đó.

Từ góc nhìn này, ý nghĩa của các khoảng giá trị $\theta$ hiện lên rất cụ thể:
- Với $\theta = \tfrac{1}{2}$, điểm $y = x_2 + \tfrac{1}{2}(x_1 - x_2) = \tfrac{x_1 + x_2}{2}$ dừng lại chính xác tại trung điểm của hai vị trí.
- Với $\theta = \tfrac{1}{3}$, điểm $y$ cách vị trí mốc $x_2$ một phần ba độ dài quãng đường tiến về phía $x_1$.
- Khi $0 \le \theta \le 1$, điểm $y$ luôn nằm trọn vẹn trên **đoạn thẳng** đóng nối giữa $x_1$ và $x_2$.
- Khi $\theta > 1$, điểm $y$ vượt qua mốc $x_1$, tiến xa về phía phần kéo dài của đoạn thẳng.
- Khi $\theta < 0$, đại lượng $\theta (x_1 - x_2)$ đảo chiều, khiến điểm $y$ lùi về phía sau của điểm mốc $x_2$.

Ý tưởng cốt lõi ở đây là: Cùng một dạng biểu thức toán học, nhưng khi ta thay đổi miền xác định của các hệ số trọng số, ta sẽ thu được các đối tượng hình học hoàn toàn khác nhau. Giữ nguyên tổng hệ số bằng 1 nhưng cho $\theta \in \mathbb{R}$ ta được đường thẳng, giới hạn $\theta \in [0, 1]$ ta được đoạn thẳng, và nếu cho $\theta \ge 0$ ta sẽ thu được một tia. Đây là nguyên lý tư duy nền tảng dẫn dắt từ tập affine tới tập lồi và nón lồi.

::: example Tính toán chi tiết tọa độ điểm chạy trên đường thẳng
Xét hai điểm cụ thể trong mặt phẳng $\mathbb{R}^2$: Điểm $x_1 = (4, 3)$ và điểm $x_2 = (1, 1)$.

**Bước 1: Xác định vector chỉ phương và phương trình tham số**
Vector dịch chuyển từ $x_2$ sang $x_1$ là:

$$
v = x_1 - x_2 = (4 - 1,\; 3 - 1) = (3, 2).
$$

Phương trình tham số của đường thẳng đi qua $x_1$ và $x_2$ có dạng:

$$
y(\theta) = (1, 1) + \theta(3, 2) = (1 + 3\theta,\; 1 + 2\theta).
$$

**Bước 2: Khảo sát các điểm cụ thể tương ứng với từng miền giá trị của $\theta$**
- Với $\theta = \tfrac{1}{3}$: Tọa độ là $y = (2,\; \tfrac{5}{3})$. Điểm này nằm bên trong đoạn thẳng nối $x_1$ và $x_2$, cách $x_2$ đúng một phần ba chiều dài đoạn thẳng.
- Với $\theta = 2$: Tọa độ là $y = (7, 5)$. Điểm này nằm trên phần kéo dài vượt qua điểm $x_1$.
- Với $\theta = -1$: Tọa độ là $y = (-2, -1)$, xác định từ $1 + 3(-1) = -2$ và $1 + 2(-1) = -1$. Điểm này nằm ở phần kéo dài lùi về phía sau điểm $x_2$.

**Bước 3: Kiểm tra một điểm bất kỳ có nằm trên đường thẳng hay không**
- Xét điểm $M(10, 7)$: Ta thiết lập hệ phương trình tìm tham số $\theta$:
  $$
  \begin{cases}
  1 + 3\theta = 10 \implies 3\theta = 9 \implies \theta = 3 \\
  1 + 2\theta = 7 \implies 2\theta = 6 \implies \theta = 3
  \end{cases}
  $$
  Cả hai tọa độ đều cho cùng một giá trị $\theta = 3$. Do đó, điểm $M(10, 7)$ thuộc đường thẳng, ứng với vị trí $\theta = 3$.
- Xét điểm $N(5, 4)$: Ta giải hệ điều kiện:
  $$
  \begin{cases}
  1 + 3\theta = 5 \implies \theta = \tfrac{4}{3} \\
  1 + 2\theta = 4 \implies \theta = \tfrac{3}{2}
  \end{cases}
  $$
  Vì $\tfrac{4}{3} \ne \tfrac{3}{2}$, hai phương trình đưa ra hai đòi hỏi mâu thuẫn về cùng một tham số $\theta$. Kết luận: Điểm $N(5, 4)$ không nằm trên đường thẳng đi qua $x_1$ và $x_2$.
:::

Mô phỏng tương tác dưới đây minh họa trực quan vị trí tương đối giữa hai điểm và đường thẳng đi qua chúng. Bạn có thể kéo thả hai điểm mốc $x_1, x_2$ hoặc điều chỉnh thanh trượt $\theta$ để quan sát chuyển động của điểm $y$:

<AffineLab type="line" />

Cách xây dựng phương trình tham số này không phụ thuộc vào số chiều không gian. Với hai vector trọng số trong không gian tham số $1000$ chiều $\mathbb{R}^{1000}$, biểu thức $\theta w_1 + (1-\theta) w_2$ vẫn mô tả chính xác đường thẳng nối giữa hai cấu hình mạng nơ-ron. Trong nghiên cứu tối ưu hóa học sâu, các nhà khoa học thường dùng lát cắt tuyến tính một chiều này (linear interpolation) để đo đạc sự biến thiên của hàm mất mát khi di chuyển từ điểm khởi tạo ngẫu nhiên tới điểm tối ưu cục bộ.

## 2. Định nghĩa tập affine: Tập khép kín với mọi đường thẳng

Sau khi đã hiểu cách kẻ một đường thẳng từ hai điểm cho trước, ta lật ngược lại vấn đề: Xét một tập hợp $C \subseteq \mathbb{R}^n$, liệu tập hợp đó có đặc tính hình học nào để mọi đường thẳng nối hai điểm bất kỳ của nó đều bị "giữ trọn" bên trong hay không?

> **Định nghĩa.** Tập hợp $C \subseteq \mathbb{R}^n$ được gọi là một **tập affine** nếu với mọi cặp điểm $x_1, x_2 \in C$ và với mọi số thực $\theta \in \mathbb{R}$, điểm kết hợp sau luôn thuộc về $C$:
> $$
> \theta x_1 + (1-\theta)\,x_2 \in C.
> $$

Về mặt hình học trực quan, một tập là affine khi và chỉ khi: Nếu chọn hai điểm phân biệt bất kỳ nằm trong tập hợp, thì toàn bộ đường thẳng vô hạn đi qua hai điểm đó (kéo dài mãi mãi về cả hai phía) phải nằm lọt hoàn toàn trong tập hợp đó.

Định nghĩa này bao hàm hai lượng từ "với mọi" mang tính chuẩn mực toán học:
1. **Với mọi cặp điểm**: Chỉ cần tìm ra một cặp điểm duy nhất trong tập hợp mà đường thẳng đi qua chúng bị chệch ra ngoài tập hợp dù chỉ một điểm, tập hợp đó lập tức mất đi tính chất affine.
2. **Với mọi số thực $\theta$**: Điểm kết hợp phải nằm trong tập hợp không chỉ khi $0 \le \theta \le 1$ (phần đoạn thẳng ở giữa), mà còn phải đúng với cả những giá trị $\theta$ rất lớn hoặc nhận giá trị âm (hai đầu kéo dài).

Các tập hợp affine quen thuộc trong thực tế bao gồm:
- Một điểm đơn lẻ $\{x_0\}$: Khi $x_1 = x_2 = x_0$, biểu thức $\theta x_0 + (1-\theta) x_0 = x_0$ luôn thuộc tập hợp với mọi $\theta$. Đây là tập affine có số chiều bằng $0$.
- Tập rỗng $\emptyset$: Thỏa mãn định nghĩa một cách tự nhiên theo logic hình thức, vì không tồn tại cặp điểm nào vi phạm điều kiện.
- Một đường thẳng bất kỳ trong không gian: Có số chiều bằng $1$.
- Một mặt phẳng bất kỳ trong $\mathbb{R}^3$: Có số chiều bằng $2$.
- Toàn bộ không gian $\mathbb{R}^n$: Luôn chứa mọi đường thẳng nối các phần tử của nó.

Ngược lại, bảng dưới đây phân tích cặn kẽ các tập hợp không thỏa mãn tính chất affine cùng phản ví dụ số học minh họa:

| Tập hợp $C$ | Vì sao không phải là tập affine? | Phản ví dụ số học cụ thể |
| :--- | :--- | :--- |
| Đoạn thẳng $[x_1, x_2]$ với $x_1 \ne x_2$ | Bị giới hạn ở hai đầu mút, không chứa phần kéo dài vô hạn. | Chọn $\theta = 2$, điểm thu được là $2x_1 - x_2$. Điểm này vượt ra ngoài mút $x_1$ nên không thuộc đoạn thẳng. |
| Tia $\{x_0 + \theta v : \theta \ge 0\}$ với $v \ne 0$ | Bị chặn ở gốc xuất phát $x_0$, không thể lùi về phía ngược lại. | Lấy hai điểm $x_0$ (ứng với $\theta = 0$) và $x_0 + v$ (ứng với $\theta = 1$). Với tham số $\theta = -1$, điểm $x_0 - v$ lọt ra ngoài tia. |
| Đường tròn $x_1^2 + x_2^2 = 1$ | Là đường cong khép kín, không chứa bất kỳ đoạn thẳng thẳng tắp nào. | Lấy hai điểm đối xứng $(1, 0)$ và $(-1, 0)$ trên đường tròn. Tại $\theta = \tfrac{1}{2}$, trung điểm là gốc $(0, 0)$ có $0^2 + 0^2 = 0 \ne 1$, không thuộc đường tròn. |
| Hợp của hai đường thẳng song song | Không chứa các đường chéo nối từ đường thẳng này sang đường thẳng kia. | Lấy $x_1$ thuộc đường thẳng thứ nhất và $x_2$ thuộc đường thẳng thứ hai. Trung điểm $\tfrac{x_1+x_2}{2}$ nằm ở dải không gian rỗng ở giữa hai đường thẳng. |

::: tip Câu hỏi kiểm tra trực giác
Xét hợp của hai trục tọa độ trong mặt phẳng $\mathbb{R}^2$: $C = \{(x_1, x_2) : x_1 x_2 = 0\}$. Tập hợp gồm hai đường thẳng cắt nhau vuông góc tại gốc tọa độ này có phải là tập affine hay không?
:::

<details><summary>Xem phân tích chi tiết</summary>

**Trả lời**: Không phải là tập affine.

**Chứng minh bằng phản ví dụ**:
- Lấy điểm $A(1, 0)$ nằm trên trục hoành (thỏa mãn $1 \cdot 0 = 0 \implies A \in C$).
- Lấy điểm $B(0, 1)$ nằm trên trục tung (thỏa mãn $0 \cdot 1 = 0 \implies B \in C$).
- Lấy trung điểm ứng với trọng số $\theta = \tfrac{1}{2}$:
  $$
  M = \tfrac{1}{2} A + \tfrac{1}{2} B = \left(\tfrac{1}{2},\; \tfrac{1}{2}\right).
  $$
- Tích tọa độ tại điểm $M$ là $\tfrac{1}{2} \cdot \tfrac{1}{2} = \tfrac{1}{4} \ne 0$. Do đó, điểm $M$ không thuộc trục hoành cũng không thuộc trục tung, nghĩa là $M \notin C$.

**Bài học sư phạm**: Dù hai đường thẳng cùng đi qua gốc tọa độ, việc hợp chúng lại không thể tạo thành một tập affine, bởi đoạn thẳng nối chéo giữa hai nhánh luôn rơi vào vùng không gian nằm ngoài cả hai đường thẳng.
</details>

## 3. Tổ hợp affine của nhiều điểm và tọa độ trọng tâm

Định nghĩa tập affine ban đầu chỉ đề cập tới cặp hai điểm. Trong thực tế tính toán tối ưu và hình học tính toán, ta thường xuyên làm việc với các hệ thống gồm nhiều điểm đồng thời, chẳng hạn trọng tâm của một cụm dữ liệu $\tfrac{1}{k}\sum_{i=1}^k x_i$.

> **Định nghĩa.** Một điểm $y$ được gọi là một **tổ hợp affine** của $k$ điểm $x_1, x_2, \dots, x_k \in \mathbb{R}^n$ nếu nó được biểu diễn dưới dạng:
> $$
> y = \theta_1 x_1 + \theta_2 x_2 + \cdots + \theta_k x_k = \sum_{i=1}^k \theta_i x_i,
> $$
> trong đó các hệ số số thực $\theta_i \in \mathbb{R}$ thỏa mãn ràng buộc chuẩn hóa:
> $$
> \sum_{i=1}^k \theta_i = \theta_1 + \theta_2 + \cdots + \theta_k = 1.
> $$

Các hệ số $\theta_i$ ở đây hoàn toàn được phép nhận giá trị âm, miễn là tổng đại số của toàn bộ $k$ hệ số bằng đúng $1$. Khi $k = 2$, biểu thức này quay trở về đúng dạng $\theta_1 x_1 + \theta_2 x_2$ với $\theta_1 + \theta_2 = 1$, tức $\theta x_1 + (1-\theta)x_2$.

Định lý nền tảng dưới đây khẳng định rằng: Tính chất khép kín trên từng cặp hai điểm là hoàn toàn đủ để bảo đảm tính khép kín trên mọi tổ hợp hữu hạn điểm.

::: proof Định lý: Tập affine chứa trọn mọi tổ hợp affine của các phần tử của nó
Giả sử $C$ là một tập affine. Ta chứng minh bằng phương pháp quy nạp toán học theo số lượng điểm $k$.

**Bước cơ sở**:
- Với $k = 1$: Biểu thức chỉ có một hệ số duy nhất $\theta_1 = 1$, điểm $y = 1 \cdot x_1 = x_1 \in C$. Khẳng định đúng.
- Với $k = 2$: Đây chính là định nghĩa gốc của tập affine. Khẳng định đúng.

**Bước quy nạp**:
Giả sử mệnh đề đúng với mọi tổ hợp của $k - 1$ điểm ($k \ge 3$). Xét một tổ hợp affine bất kỳ của $k$ điểm thuộc $C$:
$$
y = \sum_{i=1}^k \theta_i x_i = \theta_1 x_1 + \theta_2 x_2 + \cdots + \theta_k x_k, \qquad \sum_{i=1}^k \theta_i = 1.
$$

Vì tổng $k$ hệ số bằng $1$ và $k \ge 3$, không thể xảy ra trường hợp mọi hệ số đều bằng $1$. Ta có thể đổi thứ tự đánh số các điểm nếu cần thiết để đảm bảo hệ số cuối cùng $\theta_k \ne 1$, đồng nghĩa với việc $1 - \theta_k \ne 0$.

Bây giờ, ta áp dụng kỹ thuật phân rã gom nhóm đại số:
$$
\begin{aligned}
y &= \sum_{i=1}^{k-1} \theta_i x_i + \theta_k x_k \\
&= (1 - \theta_k) \sum_{i=1}^{k-1} \frac{\theta_i}{1 - \theta_k} x_i + \theta_k x_k .
\end{aligned}
$$

Hãy kiểm tra tổng các hệ số mới bên trong dấu tổng thu gọn:
$$
\sum_{i=1}^{k-1} \frac{\theta_i}{1 - \theta_k} = \frac{1}{1 - \theta_k} \sum_{i=1}^{k-1} \theta_i = \frac{1 - \theta_k}{1 - \theta_k} = 1.
$$

Biểu thức $\sum_{i=1}^{k-1} \frac{\theta_i}{1 - \theta_k} x_i$ chính là một tổ hợp affine của $k - 1$ điểm thuộc $C$. Theo giả thiết quy nạp, điểm trung gian này là một điểm hợp lệ $z \in C$. Khi đó:
$$
y = (1 - \theta_k) z + \theta_k x_k .
$$

Đây chính là tổ hợp affine của hai điểm $z \in C$ và $x_k \in C$. Theo định nghĩa tập affine, điểm $y$ bắt buộc phải thuộc về $C$. Theo nguyên lý quy nạp toán học, định lý được chứng minh hoàn tất cho mọi $k \ge 1$.
:::

### 3.1 Tọa độ trọng tâm (Barycentric Coordinates)

Trong không gian hai chiều $\mathbb{R}^2$, nếu ba điểm $p_1, p_2, p_3$ không thẳng hàng (tạo thành một tam giác không suy biến), thì mọi điểm $y \in \mathbb{R}^2$ trên mặt phẳng đều được biểu diễn duy nhất dưới dạng một tổ hợp affine:

$$
y = \theta_1 p_1 + \theta_2 p_2 + \theta_3 p_3, \qquad \theta_1 + \theta_2 + \theta_3 = 1.
$$

Bộ ba số thực duy nhất $(\theta_1, \theta_2, \theta_3)$ này được gọi là **tọa độ trọng tâm** của điểm $y$ đối với tam giác $p_1 p_2 p_3$.

::: example Thiết lập hệ phương trình tính tọa độ trọng tâm
Trong mặt phẳng $\mathbb{R}^2$, xét tam giác vuông tại gốc với ba đỉnh:
$A = (0, 0)$, $B = (4, 0)$, $C = (0, 4)$.

**Trường hợp 1: Tính tọa độ trọng tâm của điểm $M(1, 1)$ nằm trong tam giác**
Ta cần tìm bộ ba $(\theta_1, \theta_2, \theta_3)$ thỏa mãn phương trình vector và phương trình tổng chuẩn hóa:
$$
\theta_1 \begin{bmatrix} 0 \\ 0 \end{bmatrix} + \theta_2 \begin{bmatrix} 4 \\ 0 \end{bmatrix} + \theta_3 \begin{bmatrix} 0 \\ 4 \end{bmatrix} = \begin{bmatrix} 1 \\ 1 \end{bmatrix}, \qquad \theta_1 + \theta_2 + \theta_3 = 1.
$$

Khai triển thành hệ ba phương trình bậc nhất ba ẩn số:
$$
\begin{cases}
4\theta_2 = 1 \\
4\theta_3 = 1 \\
\theta_1 + \theta_2 + \theta_3 = 1
\end{cases}
\implies
\begin{cases}
\theta_2 = \tfrac{1}{4} \\
\theta_3 = \tfrac{1}{4} \\
\theta_1 = 1 - \tfrac{1}{4} - \tfrac{1}{4} = \tfrac{1}{2}
\end{cases}
$$

Kết quả: Tọa độ trọng tâm của điểm $M(1, 1)$ là $(\tfrac{1}{2},\; \tfrac{1}{4},\; \tfrac{1}{4})$.
- Vì cả ba hệ số đều dương ngặt ($\theta_1 > 0, \theta_2 > 0, \theta_3 > 0$), điểm $M$ nằm lọt hoàn toàn bên trong tam giác $ABC$.

**Trường hợp 2: Tính tọa độ trọng tâm của điểm $P(3, 3)$ nằm ngoài tam giác**
Thiết lập hệ phương trình tìm tọa độ trọng tâm cho $P(3, 3)$:
$$
\begin{cases}
4\theta_2 = 3 \implies \theta_2 = \tfrac{3}{4} \\
4\theta_3 = 3 \implies \theta_3 = \tfrac{3}{4} \\
\theta_1 + \theta_2 + \theta_3 = 1 \implies \theta_1 = 1 - \tfrac{3}{4} - \tfrac{3}{4} = -\tfrac{1}{2}
\end{cases}
$$

Kết quả: Tọa độ trọng tâm của điểm $P(3, 3)$ là $(-\tfrac{1}{2},\; \tfrac{3}{4},\; \tfrac{3}{4})$.
- Dù tổng ba hệ số vẫn bảo toàn bằng $1$, hệ số $\theta_1$ ứng với đỉnh $A$ nhận giá trị âm ($-\tfrac{1}{2} < 0$).
- Dấu âm này mang ý nghĩa hình học sâu sắc: Điểm $P$ đã vượt qua cạnh đối diện $BC$, nằm ở phía đối nghịch hoàn toàn với đỉnh $A$.
:::

Mô phỏng tương tác dưới đây cho phép bạn kéo thả điểm kiểm tra trong mặt phẳng tam giác. Hãy quan sát cách các hệ số trọng tâm biến đổi dấu khi điểm vượt qua các đường kéo dài của ba cạnh tam giác:

<AffineLab type="combination" />

Trong đồ họa máy tính (Computer Graphics), các bộ xử lý đồ họa (GPU) dùng chính tọa độ trọng tâm để nội suy màu sắc (shading) và tọa độ chất liệu (texture mapping). Khi ba đỉnh tam giác mang ba thuộc tính màu khác nhau, mỗi điểm ảnh bên trong tam giác sẽ có màu sắc là tổ hợp affine $\theta_1 C_1 + \theta_2 C_2 + \theta_3 C_3$, đảm bảo quá trình pha trộn màu sắc diễn ra mượt mà và liên tục.

## 4. Vì sao điều kiện bắt buộc phải là tổng các hệ số bằng 1?

Đến đây, một câu hỏi sư phạm then chốt cần được giải đáp: Tại sao trong tổ hợp affine, tổng các hệ số trọng số bắt buộc phải bằng đúng 1 mà không thể là một con số nào khác?

Câu trả lời nằm ở sự phân biệt bản chất vật lý giữa một **vị trí (điểm)** và một **độ dời (vector)**:
- Một **điểm** là một vị trí cụ thể trong không gian (chẳng hạn vị trí địa lý của Hà Nội). Điểm không thể tự cộng với điểm: "Hà Nội cộng Thành phố Hồ Chí Minh" là một biểu thức vô nghĩa trong vật lý.
- Một **vector** là một độ dời (chẳng hạn di chuyển 100 km về hướng Nam). Ta hoàn toàn có thể cộng hai độ dời để tạo thành một độ dời tổng hợp, hoặc nhân độ dời với một số thực để tăng độ dài quãng đường.

Vị trí của một điểm trên hệ trục tọa độ phụ thuộc hoàn toàn vào vị trí ta chọn đặt gốc tọa độ $O$. Nếu một phép tính hình học phụ thuộc vào việc người vẽ bản đồ đặt gốc $O$ ở đâu, phép tính đó sẽ không có ý nghĩa khách quan.

Giả sử ta thực hiện tịnh tiến gốc tọa độ đi một vector dời $c \in \mathbb{R}^n$. Khi đó, tọa độ của mỗi điểm $x_i$ trong hệ tọa độ mới sẽ chuyển thành $x_i + c$. Xét một tổ hợp tuyến tính tùy ý $\sum_{i=1}^k \theta_i x_i$:

$$
\sum_{i=1}^k \theta_i (x_i + c) = \sum_{i=1}^k \theta_i x_i + \left(\sum_{i=1}^k \theta_i\right) c .
$$

Hãy so sánh kết quả này với tọa độ của một điểm thực sự: Khi tịnh tiến gốc, một điểm thực sự phải dịch chuyển đúng một lượng bằng $c$. Do đó, để tổ hợp điểm $\sum_{i=1}^k \theta_i x_i$ giữ nguyên vị trí hình học nội tại (không bị bóp méo hay trôi dạt theo việc chọn gốc tọa độ), hệ số trước vector tịnh tiến $c$ bắt buộc phải bằng 1:

$$
\sum_{i=1}^k \theta_i = 1.
$$

Nếu tổng các hệ số là một số $s \ne 1$, vị trí tính ra sẽ bị dời đi một đoạn $s \cdot c \ne c$. Điểm tính ra sẽ chạy tán loạn mỗi khi ta chọn một gốc tọa độ khác. Điều này khẳng định: **Tổ hợp affine là dạng tổ hợp duy nhất giữa các điểm bảo toàn tính bất biến đối với hệ quy chiếu**.

Mô phỏng dưới đây cho phép bạn tự do kéo dời vị trí gốc tọa độ $O$. Điểm màu tím biểu diễn tổ hợp affine (tổng hệ số bằng 1) đứng yên bất biến trong không gian, trong khi điểm màu đỏ (tổng hệ số khác 1) bị kéo lê theo vị trí của gốc:

<AffineLab type="origin" />

Một cách nhìn đại số tương đương là biến đổi tổ hợp affine thành dạng "một điểm mốc cộng với tổ hợp tuyến tính các vector độ dời":

$$
\begin{aligned}
\sum_{i=1}^k \theta_i x_i &= \theta_1 x_1 + \theta_2 x_2 + \cdots + \theta_k x_k \\
&= (1 - \theta_2 - \cdots - \theta_k) x_1 + \theta_2 x_2 + \cdots + \theta_k x_k \\
&= x_1 + \theta_2 (x_2 - x_1) + \theta_3 (x_3 - x_1) + \cdots + \theta_k (x_k - x_1).
\end{aligned}
$$

Mỗi hiệu số $x_i - x_1$ là một vector độ dời từ mốc $x_1$ tới mốc $x_i$, hoàn toàn không phụ thuộc vào gốc tọa độ. Do đó, biểu thức "đứng ở điểm $x_1$, di chuyển theo một tổ hợp tuyến tính của các vector độ dời" là một thao tác hình học chuẩn xác và độc lập tuyệt đối với mọi hệ tọa độ.

## 5. Cấu trúc hình học: Mỗi tập affine là một không gian con được tịnh tiến

Từ các ví dụ về điểm, đường thẳng, mặt phẳng, ta nhận thấy tập affine luôn mang một hình thái hình học chung: Chúng là các cấu trúc "phẳng", không có độ cong, nhưng có thể không đi qua gốc tọa độ. Định lý sau đây mô tả chính xác mối liên hệ đại số giữa tập affine và không gian con tuyến tính.

> **Định lý.** Cho $C \subseteq \mathbb{R}^n$ là một tập affine khác rỗng, và chọn một điểm mốc tùy ý $x_0 \in C$. Khi đó:
> 1. Tập hợp sai số dịch chuyển về gốc:
>    $$
>    V = C - x_0 = \{x - x_0 \mid x \in C\}
>    $$
>    là một không gian con tuyến tính của $\mathbb{R}^n$.
> 2. Tập affine ban đầu được khôi phục bằng phép tịnh tiến không gian con $V$ theo vector $x_0$:
>    $$
>    C = V + x_0 = \{v + x_0 \mid v \in V\}.
>    $$

::: proof Chứng minh tính chất không gian con của V = C − x₀
Để chứng minh $V$ là một không gian con tuyến tính, ta cần chứng minh $V$ khép kín đối với mọi tổ hợp tuyến tính: Lấy hai vector tùy ý $v_1, v_2 \in V$ và hai số thực bất kỳ $\alpha, \beta \in \mathbb{R}$, ta phải chứng tỏ $\alpha v_1 + \beta v_2 \in V$.

Theo định nghĩa của tập $V$, vì $v_1, v_2 \in V$ nên tồn tại hai điểm $x_1, x_2 \in C$ sao cho:
$$
\begin{aligned}
v_1 &= x_1 - x_0 \implies x_1 = v_1 + x_0 \in C, \\
v_2 &= x_2 - x_0 \implies x_2 = v_2 + x_0 \in C.
\end{aligned}
$$

Xét biểu thức tịnh tiến của tổ hợp cần kiểm tra:
$$
\begin{aligned}
(\alpha v_1 + \beta v_2) + x_0 &= \alpha (x_1 - x_0) + \beta (x_2 - x_0) + x_0 \\
&= \alpha x_1 + \beta x_2 + (1 - \alpha - \beta) x_0 .
\end{aligned}
$$

Quan sát ba hệ số trọng số của ba điểm $x_1, x_2, x_0 \in C$:
$$
\alpha + \beta + (1 - \alpha - \beta) = 1.
$$

Tổng ba hệ số bằng đúng $1$, do đó vế phải chính là một tổ hợp affine của ba điểm thuộc $C$. Vì $C$ là tập affine, điểm này bắt buộc phải thuộc về $C$. Ta đặt điểm đó là $x_3 \in C$:
$$
(\alpha v_1 + \beta v_2) + x_0 = x_3 \in C \implies \alpha v_1 + \beta v_2 = x_3 - x_0 \in V.
$$

Như vậy, $V$ khép kín với mọi phép cộng vector và phép nhân vô hướng. Kết luận: Không gian $V = C - x_0$ là một không gian con tuyến tính hoàn chỉnh.
:::

::: example Minh họa cụ thể phép tịnh tiến đường thẳng về không gian con
Trong mặt phẳng $\mathbb{R}^2$, xét đường thẳng:
$$
C = \{(x_1, x_2) : 2x_1 - 3x_2 = 6\}.
$$

Đường thẳng này không đi qua gốc tọa độ vì $2(0) - 3(0) = 0 \ne 6$.

**Bước 1: Chọn điểm mốc thứ nhất $x_0 = (3, 0) \in C$**
Xét tập dịch chuyển $V_1 = C - x_0$:
$$
v = x - x_0 = (x_1 - 3,\; x_2 - 0) \implies x_1 = v_1 + 3, \quad x_2 = v_2.
$$
Thay vào phương trình xác định của $C$:
$$
2(v_1 + 3) - 3v_2 = 6 \implies 2v_1 + 6 - 3v_2 = 6 \implies 2v_1 - 3v_2 = 0.
$$
Như vậy, $V_1 = \{(v_1, v_2) : 2v_1 - 3v_2 = 0\}$. Đây là một đường thẳng đi qua gốc tọa độ, tức là một không gian con một chiều sinh bởi vector chỉ phương $(3, 2)$.

**Bước 2: Chọn điểm mốc thứ hai $x_0' = (0, -2) \in C$**
Xét tập dịch chuyển $V_2 = C - x_0'$:
$$
v = x - x_0' = (x_1 - 0,\; x_2 - (-2)) \implies x_1 = v_1, \quad x_2 = v_2 - 2.
$$
Thay vào phương trình của $C$:
$$
2v_1 - 3(v_2 - 2) = 6 \implies 2v_1 - 3v_2 + 6 = 6 \implies 2v_1 - 3v_2 = 0.
$$
Ta thấy $V_2$ hoàn toàn trùng khớp với $V_1$.
:::

Kết quả trên chứng minh một tính chất cơ bản: **Không gian con $V$ hoàn toàn độc lập với việc lựa chọn điểm mốc $x_0 \in C$**. Nếu chọn một điểm mốc khác $x_0' \in C$, hiệu $u = x_0' - x_0$ là một vector nằm trong $V$, và phép dời một không gian con bởi một vector của chính nó không làm thay đổi không gian con đó.

Vì không gian con $V$ đi kèm với $C$ là duy nhất, ta định nghĩa **số chiều của tập affine** $C$ chính là số chiều của không gian con $V$:
$$
\dim(C) = \dim(V).
$$
- Một điểm đơn lẻ có số chiều bằng $0$.
- Một đường thẳng có số chiều bằng $1$.
- Một mặt phẳng có số chiều bằng $2$.

Hệ quả trực tiếp: **Một tập affine là một không gian con khi và chỉ khi nó chứa gốc tọa độ $0$**. Khi tập affine không chứa gốc tọa độ, nó đơn thuần là một không gian con bị đẩy lệch song song khỏi vị trí gốc.

## 6. Biểu diễn đại số: Tập nghiệm của hệ phương trình tuyến tính

Mối liên hệ giữa tập affine và không gian con dẫn thẳng tới ví dụ trung tâm của toàn bộ lý thuyết tối ưu hóa: Hệ phương trình tuyến tính $Ax = b$.

Cho ma trận $A \in \mathbb{R}^{m \times n}$ và vector vế phải $b \in \mathbb{R}^m$. Tập hợp tất cả các nghiệm:

$$
C = \{x \in \mathbb{R}^n : Ax = b\}
$$

luôn luôn là một tập affine.

**Kiểm chứng trực tiếp bằng định nghĩa**:
Lấy hai nghiệm tùy ý $x_1, x_2 \in C$, tức $Ax_1 = b$ và $Ax_2 = b$. Với mọi hệ số $\theta \in \mathbb{R}$, ta nhân ma trận $A$ với tổ hợp affine của hai nghiệm:

$$
\begin{aligned}
A\big(\theta x_1 + (1-\theta)x_2\big) &= \theta A x_1 + (1-\theta) A x_2 \\
&= \theta b + (1-\theta) b \\
&= \big(\theta + (1-\theta)\big) b = 1 \cdot b = b .
\end{aligned}
$$

Vì tích với ma trận $A$ luôn cho ra kết quả bằng $b$, điểm $\theta x_1 + (1-\theta)x_2$ luôn là một nghiệm hợp lệ của hệ phương trình, tức thuộc $C$. Do đó, tập nghiệm $C$ là một tập affine.

Không gian con tuyến tính đi kèm với tập nghiệm $C$ chính là **không gian hạt nhân (null space / kernel)** của ma trận $A$:

$$
\mathcal{N}(A) = \{v \in \mathbb{R}^n : Av = 0\}.
$$

Nếu hệ phương trình có ít nhất một nghiệm riêng $x_0$ (thỏa mãn $Ax_0 = b$), thì mọi nghiệm của hệ đều biểu diễn dưới dạng:

$$
x = x_0 + v, \qquad v \in \mathcal{N}(A).
$$

Mệnh đề đại số quen thuộc "Nghiệm tổng quát của hệ không thuần nhất bằng một nghiệm riêng cộng với nghiệm tổng quát của hệ thuần nhất" thực chất là một phát biểu hình học: Tập nghiệm là không gian con $\mathcal{N}(A)$ được tịnh tiến song song một đoạn bằng vector $x_0$.

::: example Giải và tham số hóa tập nghiệm của một siêu phẳng trong không gian 3D
Xét phương trình mặt phẳng trong $\mathbb{R}^3$:
$$
x_1 + 2x_2 + 3x_3 = 6.
$$

Ma trận hệ số là $A = \begin{bmatrix} 1 & 2 & 3 \end{bmatrix} \in \mathbb{R}^{1 \times 3}$ và $b = 6$.

**Bước 1: Tìm một nghiệm riêng $x_0$**
Chọn các biến tự do $x_2 = 0, x_3 = 0$, ta tính được ngay $x_1 = 6$. Ta có nghiệm riêng $x_0 = (6, 0, 0)$. Hoặc ta có thể chọn $x_0 = (1, 1, 1)$ vì $1(1) + 2(1) + 3(1) = 6$. Cả hai lựa chọn đều hoàn toàn chuẩn xác.

**Bước 2: Tìm cơ sở của không gian nghiệm thuần nhất $\mathcal{N}(A)$**
Xét phương trình thuần nhất $x_1 + 2x_2 + 3x_3 = 0$, ta rút ra $x_1 = -2x_2 - 3x_3$.
Đặt hai biến tự do $x_2 = s$ và $x_3 = t$ ($s, t \in \mathbb{R}$):
$$
\begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} = \begin{bmatrix} -2s - 3t \\ s \\ t \end{bmatrix} = s \begin{bmatrix} -2 \\ 1 \\ 0 \end{bmatrix} + t \begin{bmatrix} -3 \\ 0 \\ 1 \end{bmatrix}.
$$

Hai vector chỉ phương cơ sở là $v_1 = (-2, 1, 0)$ và $v_2 = (-3, 0, 1)$. Hai vector này độc lập tuyến tính và sinh ra không gian con hai chiều $\mathcal{N}(A)$.

**Bước 3: Biểu diễn hình học của tập nghiệm**
Toàn bộ tập nghiệm $C$ được mô tả dưới dạng tịnh tiến:
$$
C = \left\{(1, 1, 1) + s(-2, 1, 0) + t(-3, 0, 1) \;\middle|\; s, t \in \mathbb{R}\right\}.
$$
Đây là một mặt phẳng hai chiều trong không gian $\mathbb{R}^3$, song song với mặt phẳng đi qua gốc tọa độ có phương trình $x_1 + 2x_2 + 3x_3 = 0$.
:::

Mô phỏng sau minh họa trực quan sự phân tách của một tập nghiệm thành vector nghiệm riêng $x_0$ và không gian nghiệm thuần nhất $\mathcal{N}(A)$:

<AffineLab type="solutions" />

Định lý đảo của đại số tuyến tính cũng khẳng định: **Mọi tập affine khác rỗng trong $\mathbb{R}^n$ đều có thể biểu diễn dưới dạng tập nghiệm của một hệ phương trình tuyến tính $Ax = b$**. Như vậy, "tập affine" trong hình học và "tập nghiệm của hệ phương trình tuyến tính" trong đại số là hai cách diễn đạt cho cùng một thực thể toán học.

### 6.1 Ứng dụng trong học máy: Hiện tượng thừa tham số (Overparameterization)

Trong học máy hiện đại, đặc biệt là với các mạng nơ-ron sâu, số lượng tham số $n$ thường vượt xa số lượng mẫu dữ liệu huấn luyện $m$ ($n \gg m$).

Giả sử ta xét mô hình hồi quy tuyến tính với ma trận dữ liệu $X \in \mathbb{R}^{m \times n}$ (mỗi hàng là một vector đặc trưng của một mẫu) và vector nhãn mục tiêu $y \in \mathbb{R}^m$. Tập hợp các bộ trọng số khớp hoàn hảo với toàn bộ tập dữ liệu huấn luyện (đạt sai số huấn luyện bằng 0) chính là tập nghiệm của hệ phương trình:

$$
C = \{w \in \mathbb{R}^n : Xw = y\}.
$$

Khi các hàng của ma trận dữ liệu $X$ độc lập tuyến tính, hệ phương trình thiếu xác định này có vô số nghiệm. Tập nghiệm $C$ là một tập affine có số chiều bằng $n - m \ge 1$.

Một câu hỏi mang tính bản chất: **Thuật toán tối ưu hóa sẽ chọn nghiệm nào trong vô số nghiệm khả thi đó?**

Xét trường hợp cụ thể: Huấn luyện mô hình hai tham số $w_1, w_2$ trên một mẫu dữ liệu duy nhất có vector đặc trưng $x = (1, 1)$ và nhãn mục tiêu $y = 2$.
Phương trình khớp dữ liệu là:
$$
w_1 \cdot 1 + w_2 \cdot 1 = 2 \implies w_1 + w_2 = 2.
$$
Tập nghiệm là một đường thẳng trong mặt phẳng tham số $\mathbb{R}^2$.

Hàm mất mát bình phương:
$$
L(w) = \tfrac{1}{2}(w_1 + w_2 - 2)^2.
$$
Gradient của hàm mất mát tại điểm $w$:
$$
\nabla L(w) = (w_1 + w_2 - 2) \begin{bmatrix} 1 \\ 1 \end{bmatrix}.
$$

Thuật toán Gradient Descent cập nhật theo công thức:
$$
w^{(k+1)} = w^{(k)} - \eta \nabla L(w^{(k)}) = w^{(k)} - \eta (w_1^{(k)} + w_2^{(k)} - 2) \begin{bmatrix} 1 \\ 1 \end{bmatrix}.
$$

Vector hiệu chỉnh ở mọi bước lặp luôn luôn cùng phương với vector $(1, 1)$, tức là vector hàng của ma trận dữ liệu $X$. Do đó:
- **Nếu khởi tạo từ gốc tọa độ $w^{(0)} = (0, 0)$**: Toàn bộ các bước cập nhật sẽ bị giam giữ trên đường phân giác $w_1 = w_2$. Khi thuật toán hội tụ, nghiệm tìm được phải vừa thuộc đường $w_1 = w_2$, vừa thuộc đường nghiệm $w_1 + w_2 = 2$. Nghiệm duy nhất thỏa mãn là $w^* = (1, 1)$. Đây chính là nghiệm có chuẩn Euclid nhỏ nhất $\|w\|_2$ trong toàn bộ tập nghiệm.
- **Nếu khởi tạo từ điểm $w^{(0)} = (2, -2)$**: Điểm khởi tạo nằm trên đường $w_1 - w_2 = 4$ vuông góc với $(1, 1)$. Thành phần hình chiếu này không bao giờ bị triệt tiêu bởi gradient, khiến thuật toán hội tụ về điểm $(3, -1)$.

Bài học sư phạm sâu sắc: Khi tập nghiệm là một tập affine nhiều chiều, hàm mất mát không đơn độc quyết định mô hình cuối cùng. Điểm khởi tạo và thuật toán tối ưu hóa đóng vai trò là cơ chế điều chuẩn ẩn (implicit regularization), trực tiếp quyết định nghiệm nào trong tập affine sẽ được lựa chọn.

## 7. Bao affine (Affine Hull)

Nếu một tập hợp $C \subseteq \mathbb{R}^n$ bất kỳ chưa phải là tập affine, ta có thể đặt câu hỏi: Không gian affine nhỏ nhất bao bọc lấy $C$ là gì?

> **Định nghĩa.** **Bao affine** của tập hợp $C \subseteq \mathbb{R}^n$, ký hiệu là $\operatorname{aff}(C)$, là tập hợp tất cả các tổ hợp affine có thể tạo thành từ các phần tử của $C$:
> $$
> \operatorname{aff}(C) = \left\{\sum_{i=1}^k \theta_i x_i \;\middle|\; x_i \in C, \ \sum_{i=1}^k \theta_i = 1, \ k \ge 1\right\}.
> $$

Bao affine $\operatorname{aff}(C)$ là tập affine nhỏ nhất chứa $C$, theo nghĩa: Nếu $S$ là một tập affine bất kỳ thỏa mãn $C \subseteq S$, thì bắt buộc $\operatorname{aff}(C) \subseteq S$.

::: example Phân tích bao affine của các tập hình học tiêu biểu
1. **Tập gồm hai điểm phân biệt $\{x_1, x_2\}$**:
   Bao affine là đường thẳng duy nhất đi qua hai điểm đó, có số chiều bằng $1$:
   $$
   \operatorname{aff}(\{x_1, x_2\}) = \{\theta x_1 + (1-\theta)x_2 \mid \theta \in \mathbb{R}\}.
   $$
2. **Đoạn thẳng nối hai điểm $[x_1, x_2]$**:
   Dù đoạn thẳng bị chặn ở hai đầu mút, mọi tổ hợp affine tự do của các điểm trên đoạn thẳng sẽ kéo dài vô hạn về hai phía, tạo thành trọn vẹn đường thẳng chứa đoạn thẳng đó: $\operatorname{aff}([x_1, x_2]) = \operatorname{aff}(\{x_1, x_2\})$.
3. **Đường tròn đơn vị $S^1 = \{(x_1, x_2) \in \mathbb{R}^2 \mid x_1^2 + x_2^2 = 1\}$**:
   Đường tròn là đường cong một chiều. Tuy nhiên, không có bất kỳ đường thẳng một chiều nào có thể chứa trọn vẹn đường tròn. Cứ lấy ba điểm trên đường tròn, tổ hợp affine của chúng sẽ quét qua toàn bộ mặt phẳng. Do đó: $\operatorname{aff}(S^1) = \mathbb{R}^2$, có số chiều bằng $2$.
4. **Tập ba vector đơn vị chuẩn tắc trong $\mathbb{R}^3$**:
   Xét tập $\{e_1, e_2, e_3\}$ với các vector $e_1 = (1,0,0)$, $e_2 = (0,1,0)$, $e_3 = (0,0,1)$.
   Mọi tổ hợp affine có dạng $\theta_1 e_1 + \theta_2 e_2 + \theta_3 e_3 = (\theta_1, \theta_2, \theta_3)$ với $\theta_1 + \theta_2 + \theta_3 = 1$.
   Do đó, bao affine chính là mặt phẳng:
   $$
   \operatorname{aff}(\{e_1, e_2, e_3\}) = \{(x_1, x_2, x_3) \in \mathbb{R}^3 \mid x_1 + x_2 + x_3 = 1\}.
   $$
   Mặt phẳng này có số chiều bằng $2$. Đây cũng chính là không gian nền tự nhiên chứa đơn hình xác suất (probability simplex) của ba biến cố rời rạc.
:::

Bao affine đóng vai trò là "không gian nền tự nhiên" của một tập hợp. Một hình vuông phẳng đặt trong không gian ba chiều $\mathbb{R}^3$ hoàn toàn không có điểm trong topo theo nghĩa quả cầu 3D (phần trong rỗng), nhưng khi xét trong không gian nền tự nhiên là bao affine của nó (mặt phẳng 2D chứa hình vuông), nó sở hữu một phần trong trọn vẹn gọi là **phần trong tương đối (relative interior)**.

## 8. Hàm affine: Ánh xạ bảo toàn cấu trúc affine

Đi cùng với tập affine là lớp hàm số bảo toàn cấu trúc này:

> **Định nghĩa.** Một ánh xạ $f: \mathbb{R}^n \to \mathbb{R}^m$ được gọi là **hàm affine** nếu nó được biểu diễn dưới dạng:
> $$
> f(x) = Ax + b,
> $$
> trong đó $A \in \mathbb{R}^{m \times n}$ là một ma trận và $b \in \mathbb{R}^m$ là một vector hằng số.

Đặc tính đại số quan trọng nhất của hàm affine là nó **bảo toàn hoàn toàn các tổ hợp affine**. Thật vậy, với mọi tập hợp điểm $x_1, \dots, x_k$ và mọi bộ trọng số thỏa mãn $\sum_{i=1}^k \theta_i = 1$:

$$
\begin{aligned}
f &\left(\sum_{i=1}^k \theta_i x_i\right) = A\left(\sum_{i=1}^k \theta_i x_i\right) + b \\
&= \sum_{i=1}^k \theta_i A x_i + 1 \cdot b \\
&= \sum_{i=1}^k \theta_i A x_i + \left(\sum_{i=1}^k \theta_i\right) b \\
&= \sum_{i=1}^k \theta_i (A x_i + b) = \sum_{i=1}^k \theta_i f(x_i).
\end{aligned}
$$

::: example Minh họa tính bảo toàn tổ hợp affine qua hàm số cụ thể
Xét hàm số $f: \mathbb{R} \to \mathbb{R}$ xác định bởi $f(x) = 2x + 3$ (ở đây $A = 2, b = 3$).

Lấy hai điểm $x_1 = 1, x_2 = 5$. Giá trị hàm số tại hai điểm là:
$$
f(x_1) = 2(1) + 3 = 5, \qquad f(x_2) = 2(5) + 3 = 13.
$$

- **Trường hợp 1: Chọn tổ hợp affine với $\theta_1 = \tfrac{1}{4}, \theta_2 = \tfrac{3}{4}$ (tổng bằng 1)**:
  Tọa độ điểm tổ hợp là $x = \tfrac{1}{4}(1) + \tfrac{3}{4}(5) = 4$.
  Giá trị hàm số tại điểm tổ hợp: $f(4) = 2(4) + 3 = 11$.
  Tổ hợp các giá trị hàm số:
  $$
  \tfrac{1}{4} f(x_1) + \tfrac{3}{4} f(x_2) = \tfrac{1}{4}(5) + \tfrac{3}{4}(13) = \tfrac{44}{4} = 11.
  $$
  Hai kết quả trùng khớp hoàn toàn: $f(\tfrac{1}{4} x_1 + \tfrac{3}{4} x_2) = \tfrac{1}{4} f(x_1) + \tfrac{3}{4} f(x_2)$.

- **Trường hợp 2: Xét tổ hợp tuyến tính với $\alpha_1 = 1, \alpha_2 = 1$ (tổng bằng $2 \ne 1$)**:
  Điểm kết hợp: $x = 1(1) + 1(5) = 6$, cho giá trị hàm số:
  $$
  f(6) = 2(6) + 3 = 15.
  $$
  Tổng hai giá trị hàm số: $f(x_1) + f(x_2) = 5 + 13 = 18 \ne 15$.
  Đẳng thức bị phá vỡ vì hệ số tự do $b = 3$ bị nhân đôi ở vế phải thành $3 + 3 = 6$ thay vì $3$.
:::

Trong học sâu (Deep Learning), các tầng kết nối đầy đủ thường được gọi tên là `Linear Layer` (chẳng hạn `nn.Linear` trong PyTorch). Tuy nhiên, về mặt toán học chuẩn mực, phép biến đổi $y = Wx + b$ là một **ánh xạ affine**, và nó chỉ thực sự là ánh xạ tuyến tính thuần túy khi vector độ lệch (bias) triệt tiêu ($b = 0$).

Hệ quả hình học:
- Ảnh của một tập affine qua một hàm affine luôn luôn là một tập affine.
- Tập mức của một hàm affine nhận giá trị thực, $\{x \mid a^T x + c = 0\}$ với $a \ne 0$, là một tập affine có số chiều $n - 1$, được gọi là một **siêu phẳng**. Siêu phẳng chính là ranh giới phân định lớp (decision boundary) của các thuật toán phân loại tuyến tính như Logistic Regression và Support Vector Machines (SVM).

## 9. Các câu hỏi đào sâu tư duy

Mỗi câu hỏi dưới đây nhằm làm sáng tỏ một góc nhìn bản chất dễ gây ngộ nhận. Bạn hãy suy ngẫm kỹ trước khi mở phần lời giải.

**Câu 1.** Nếu trong công thức $\theta x_1 + (1-\theta)x_2$ ta chỉ cho phép $\theta \ge 0$, hình học của tập hợp điểm thu được là gì? Nó có phải là tập affine không?

<details><summary>Xem phân tích chi tiết</summary>

Viết lại dưới dạng chuyển động học: Biểu thức $y = x_2 + \theta(x_1 - x_2)$ với $\theta \ge 0$.
- Khi $\theta = 0$, điểm ở mốc $x_2$.
- Khi $\theta = 1$, điểm tới mốc $x_1$.
- Khi $\theta > 1$, điểm tiếp tục đi thẳng về phía trước theo hướng $x_1 - x_2$.
- Do $\theta \ge 0$, điểm không bao giờ được phép lùi về phía sau điểm $x_2$ (ứng với $\theta < 0$).

Tập hợp thu được là một **tia (ray)** xuất phát từ gốc $x_2$ và đi qua $x_1$. Tia này không phải là tập affine vì nó không chứa các điểm ở phần kéo dài lùi về phía sau của $x_2$.
</details>

**Câu 2.** Nếu một tập $C$ chứa toàn bộ đoạn thẳng nối hai điểm bất kỳ của nó, ta đã có thể kết luận $C$ là tập affine hay chưa?

<details><summary>Xem phân tích chi tiết</summary>

Chưa thể kết luận. Tập hợp chứa trọn vẹn đoạn thẳng nối hai điểm bất kỳ của nó được gọi là **tập lồi (convex set)**. Tập lồi chỉ đòi hỏi tính khép kín trên đoạn thẳng ứng với $\theta \in [0, 1]$, trong khi tập affine đòi hỏi tính khép kín trên toàn bộ đường thẳng kéo dài vô hạn với mọi $\theta \in \mathbb{R}$.

**Phản ví dụ**: Hình tròn đóng $C = \{(x_1, x_2) : x_1^2 + x_2^2 \le 1\}$ là tập lồi vì đoạn thẳng nối hai điểm trong hình tròn luôn nằm trong hình tròn. Nhưng lấy hai điểm $(0, 0)$ và $(0.5, 0)$ thuộc $C$, đường thẳng đi qua chúng sẽ đi qua điểm $(2, 0)$ (ứng với $\theta = 4$), điểm này nằm ngoài hình tròn. Mọi tập affine đều lồi, nhưng điều ngược lại không đúng.
</details>

**Câu 3.** Giao của một họ các tập affine có phải là tập affine không? Hợp của chúng thì sao?

<details><summary>Xem phân tích chi tiết</summary>

- **Giao của các tập affine**: Luôn là một tập affine (kể cả giao của vô hạn tập affine).
  *Chứng minh*: Giả sử $C = \bigcap_{i} C_i$ với mỗi $C_i$ là tập affine. Lấy hai điểm bất kỳ $x_1, x_2 \in C$. Khi đó $x_1, x_2 \in C_i$ với mọi $i$. Do mỗi $C_i$ là tập affine, toàn bộ đường thẳng $L = \{\theta x_1 + (1-\theta)x_2 : \theta \in \mathbb{R}\}$ đều nằm trong $C_i$ với mọi $i$. Do đó, đường thẳng $L$ nằm trong giao $C$.
  *Ý nghĩa đại số*: Giao của các tập affine tương ứng với việc ghép nối thêm các phương trình tuyến tính ràng buộc vào hệ phương trình ban đầu.
- **Hợp của các tập affine**: Nói chung **không** phải là tập affine. Hợp của hai trục tọa độ cắt nhau trong $\mathbb{R}^2$ là phản ví dụ kinh điển.
</details>

**Câu 4.** Tập các số hữu tỉ trong mặt phẳng $\mathbb{Q}^2$ chứa trung điểm của hai điểm bất kỳ của nó, và chứa cả điểm đối xứng $2x_1 - x_2$. Tập này có phải là tập affine trong $\mathbb{R}^2$ không?

<details><summary>Xem phân tích chi tiết</summary>

Không phải là tập affine.
Trung điểm tương ứng với $\theta = \tfrac{1}{2}$, điểm đối xứng tương ứng với $\theta = 2$. Việc lặp lại hai phép toán này chỉ sinh ra các tham số $\theta$ thuộc tập số hữu tỉ $\mathbb{Q}$.
Định nghĩa tập affine đòi hỏi tính khép kín với **mọi số thực $\theta \in \mathbb{R}$**.
Lấy hai điểm $x_1 = (1, 0) \in \mathbb{Q}^2$ và $x_2 = (0, 0) \in \mathbb{Q}^2$. Với tham số vô tỉ $\theta = \sqrt{2}$, điểm kết hợp là:
$$
y = \sqrt{2} (1, 0) + (1 - \sqrt{2}) (0, 0) = (\sqrt{2}, 0) \notin \mathbb{Q}^2.
$$
Ví dụ này khẳng định tầm quan trọng của trường số thực liên tục trong giải tích lồi.
</details>

## 10. Bài tập tự luyện có lời giải chi tiết

::: exercise 1. Tham số hóa và xác định vị trí tương đối trên đường thẳng
Trong không gian $\mathbb{R}^3$, cho hai điểm $x_1 = (2, -1, 3)$ và $x_2 = (0, 1, 1)$.
1. Viết phương trình tham số của đường thẳng đi qua $x_1, x_2$ theo tham số $\theta$.
2. Kiểm tra xem điểm $M(5, -4, 6)$ và điểm $N(1, 1, 2)$ có thuộc đường thẳng này không. Nếu có, hãy xác định điểm đó nằm trên đoạn $[x_2, x_1]$, phía sau $x_2$ hay vượt trước $x_1$.
:::

::: hint
Tính vector chỉ phương $x_1 - x_2$, thiết lập phương trình từng tọa độ theo $\theta$ rồi đối chiếu tính nhất quán của $\theta$.
:::

::: solution
**Lời giải từng bước**:

**Bước 1: Thiết lập phương trình tham số**
Vector dịch chuyển từ $x_2$ sang $x_1$ là:
$$
v = x_1 - x_2 = (2 - 0,\; -1 - 1,\; 3 - 1) = (2, -2, 2).
$$
Mọi điểm $y$ trên đường thẳng có phương trình tham số:
$$
y(\theta) = x_2 + \theta(x_1 - x_2) = (0 + 2\theta,\; 1 - 2\theta,\; 1 + 2\theta) = (2\theta,\; 1 - 2\theta,\; 1 + 2\theta).
$$

**Bước 2: Kiểm tra điểm $M(5, -4, 6)$**
Thiết lập hệ phương trình theo $\theta$:
$$
\begin{cases}
2\theta = 5 \implies \theta = \tfrac{5}{2} \\
1 - 2\theta = -4 \implies 2\theta = 5 \implies \theta = \tfrac{5}{2} \\
1 + 2\theta = 6 \implies 2\theta = 5 \implies \theta = \tfrac{5}{2}
\end{cases}
$$
Cả ba phương trình đều cho cùng một giá trị $\theta = \tfrac{5}{2} = 2.5$. Do đó, điểm $M$ thuộc đường thẳng.
Vì $\theta = 2.5 > 1$, điểm $M$ nằm ở phần kéo dài vượt qua điểm $x_1$.

**Bước 3: Kiểm tra điểm $N(1, 1, 2)$**
Thiết lập hệ phương trình:
$$
\begin{cases}
2\theta = 1 \implies \theta = \tfrac{1}{2} \\
1 - 2\theta = 1 \implies 2\theta = 0 \implies \theta = 0
\end{cases}
$$
Hai phương trình mâu thuẫn về giá trị $\theta$. Do đó, điểm $N(1, 1, 2)$ không thuộc đường thẳng.
:::

::: exercise 2. Xác định cấu trúc tập nghiệm và số chiều
Cho hệ phương trình tuyến tính $Ax = b$ với:
$$
A = \begin{bmatrix} 1 & 1 & 0 & 0 \\ 0 & 1 & 1 & 0 \end{bmatrix} \in \mathbb{R}^{2 \times 4}, \qquad b = \begin{bmatrix} 2 \\ 3 \end{bmatrix}.
$$
1. Tìm một nghiệm riêng $x_0$ của hệ phương trình.
2. Xác định cơ sở của không gian nghiệm thuần nhất $\mathcal{N}(A)$.
3. Biểu diễn tập nghiệm dưới dạng không gian con tịnh tiến và xác định số chiều của tập nghiệm.
:::

::: solution
**Lời giải từng bước**:

**Bước 1: Tìm nghiệm riêng $x_0$**
Hệ phương trình tương đương:
$$
\begin{cases}
x_1 + x_2 = 2 \\
x_2 + x_3 = 3
\end{cases}
$$
Ta có thể chọn hai biến tự do $x_2 = 0$ và $x_4 = 0$. Khi đó:
$$
x_1 = 2 - 0 = 2, \qquad x_3 = 3 - 0 = 3.
$$
Ta thu được một nghiệm riêng: $x_0 = (2, 0, 3, 0)$.

**Bước 2: Tìm cơ sở của $\mathcal{N}(A)$**
Xét hệ thuần nhất $Ax = 0$:
$$
\begin{cases}
x_1 + x_2 = 0 \implies x_1 = -x_2 \\
x_2 + x_3 = 0 \implies x_3 = -x_2
\end{cases}
$$
Hai biến $x_2$ và $x_4$ hoàn toàn tự do. Đặt $x_2 = s$ và $x_4 = t$ ($s, t \in \mathbb{R}$):
$$
\begin{bmatrix} x_1 \\ x_2 \\ x_3 \\ x_4 \end{bmatrix} = \begin{bmatrix} -s \\ s \\ -s \\ t \end{bmatrix} = s \begin{bmatrix} -1 \\ 1 \\ -1 \\ 0 \end{bmatrix} + t \begin{bmatrix} 0 \\ 0 \\ 0 \\ 1 \end{bmatrix}.
$$
Hai vector chỉ phương cơ sở là $v_1 = (-1, 1, -1, 0)$ và $v_2 = (0, 0, 0, 1)$. Hai vector này độc lập tuyến tính và sinh ra không gian hạt nhân $\mathcal{N}(A)$.

**Bước 3: Biểu diễn hình học và số chiều**
Tập nghiệm của hệ phương trình là tập affine:
$$
C = \left\{(2, 0, 3, 0) + s(-1, 1, -1, 0) + t(0, 0, 0, 1) : s, t \in \mathbb{R}\right\}.
$$
Số chiều của tập nghiệm bằng số chiều của $\mathcal{N}(A)$:
$$
\dim(C) = n - \operatorname{rank}(A) = 4 - 2 = 2.
$$
Tập nghiệm là một mặt phẳng affine hai chiều trong không gian bốn chiều $\mathbb{R}^4$.
:::

::: exercise 3. Khảo sát bao affine và tính chất không gian con
Tìm bao affine của hai tập hợp sau và cho biết tập nào là không gian con tuyến tính:
1. Tập $S_1 = \{(1, 0, 0), (0, 1, 0), (0, 0, 1)\}$ trong $\mathbb{R}^3$.
2. Tập $S_2 = \{(1, 2),\; (3, 6)\} \subset \mathbb{R}^2$.
:::

::: solution
**Lời giải từng bước**:

**Xét tập $S_1$**:
Mọi tổ hợp affine của ba điểm thuộc $S_1$ có dạng:
$$
y = \theta_1 (1,0,0) + \theta_2 (0,1,0) + \theta_3 (0,0,1) = (\theta_1, \theta_2, \theta_3), \qquad \theta_1 + \theta_2 + \theta_3 = 1.
$$
Đặt $x_1 = \theta_1, x_2 = \theta_2, x_3 = \theta_3$, ta thấy tập hợp này chính là mặt phẳng:
$$
\operatorname{aff}(S_1) = \{(x_1, x_2, x_3) \in \mathbb{R}^3 \mid x_1 + x_2 + x_3 = 1\}.
$$
Mặt phẳng này không chứa gốc tọa độ $0 = (0, 0, 0)$ vì $0 + 0 + 0 = 0 \ne 1$.
Kết luận: Bao affine $\operatorname{aff}(S_1)$ là một tập affine hai chiều nhưng **không phải** là một không gian con tuyến tính.

**Xét tập $S_2$**:
Tập $S_2$ gồm hai điểm $p_1 = (1, 2)$ và $p_2 = (3, 6)$.
Vector chỉ phương là $p_2 - p_1 = (2, 4) = 2(1, 2)$.
Bao affine là đường thẳng đi qua hai điểm:
$$
y(\theta) = (1, 2) + \theta(2, 4) = (1 + 2\theta,\; 2 + 4\theta).
$$
Quan sát thấy tỉ số giữa hai tọa độ luôn thỏa mãn: $x_2 = 2x_1 \implies 2x_1 - x_2 = 0$.
Do đó:
$$
\operatorname{aff}(S_2) = \{(x_1, x_2) \in \mathbb{R}^2 \mid 2x_1 - x_2 = 0\}.
$$
Đường thẳng này đi qua gốc tọa độ $(0, 0)$ (ứng với $\theta = -0.5$).
Kết luận: Bao affine $\operatorname{aff}(S_2)$ là một tập affine một chiều và **chính là một không gian con tuyến tính** của $\mathbb{R}^2$.
:::

## Tóm tắt cốt lõi

1. **Phương trình đường thẳng & đoạn thẳng**: Đường thẳng đi qua $x_1, x_2$ được tham số hóa bằng $\theta x_1 + (1-\theta)x_2$ với $\theta \in \mathbb{R}$. Thu hẹp $\theta \in [0, 1]$ cho ta đoạn thẳng đóng.
2. **Tập affine**: Là tập hợp khép kín với mọi đường thẳng đi qua hai điểm bất kỳ của nó. Một tập affine chứa trọn mọi tổ hợp affine $\sum_{i=1}^k \theta_i x_i$ với tổng trọng số chuẩn hóa $\sum_{i=1}^k \theta_i = 1$.
3. **Ý nghĩa của điều kiện tổng bằng 1**: Là điều kiện cần và đủ để tổ hợp các vị trí điểm bất biến đối với phép tịnh tiến gốc tọa độ, phản ánh đúng bản chất vật lý độc lập với hệ quy chiếu.
4. **Cấu trúc không gian con tịnh tiến**: Mọi tập affine khác rỗng $C$ đều có dạng $C = V + x_0$, trong đó $V = C - x_0$ là một không gian con tuyến tính duy nhất. Tập affine là không gian con khi và chỉ khi nó chứa gốc tọa độ $0$.
5. **Tập nghiệm hệ tuyến tính**: Tập nghiệm của $Ax = b$ luôn là một tập affine với không gian con đi kèm là $\mathcal{N}(A)$. Ngược lại, mọi tập affine đều là tập nghiệm của một hệ phương trình tuyến tính thích hợp.
6. **Hàm affine**: Ánh xạ $f(x) = Ax + b$ bảo toàn tổ hợp affine, biến tập affine thành tập affine. Tầng tuyến tính trong học sâu là một hàm affine.

## Tài liệu tham khảo

- Stephen Boyd, Lieven Vandenberghe, *Convex Optimization*, Cambridge University Press.
- I. J. Goodfellow, O. Vinyals, A. M. Saxe, [*Qualitatively characterizing neural network optimization problems*](https://arxiv.org/abs/1412.6544), ICLR 2015.
- J. Frankle, [*Revisiting "Qualitatively Characterizing Neural Network Optimization Problems"*](https://arxiv.org/abs/2012.06898), 2020.
