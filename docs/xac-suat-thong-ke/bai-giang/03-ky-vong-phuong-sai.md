---
course: xac-suat-thong-ke
lecture: 03-ky-vong-phuong-sai
section: lecture
title: "Kỳ vọng, phương sai & mẫu dữ liệu"
prerequisites: ["ky-vong", "phuong-sai", "mau-tong-the"]
lessonStatus: ready
description: "Kỳ vọng như điểm tựa thăng bằng, phương sai và độ lệch chuẩn, tính chất tuyến tính, bậc tự do và lý do chia n-1 trong phương sai mẫu."
---

Khi đối diện với một biến ngẫu nhiên, ta không thể biết chắc ở lượt thử tiếp theo giá trị nào sẽ xuất hiện. Nhưng đằng sau sự hỗn loạn bề ngoài đó luôn tồn tại những quy luật dài hạn: Các giá trị có xu hướng hội tụ quanh một "trọng tâm" nào? Mức độ phân tán, co cụm quanh trọng tâm đó rộng hay hẹp? Và khi ta chỉ có trong tay một tập dữ liệu mẫu hữu hạn, làm thế nào để ước lượng chuẩn xác các tham số chưa biết của toàn bộ tổng thể?

Bài học này sẽ trang bị hai đặc trưng số quan trọng bậc nhất của lý thuyết xác suất: **Kỳ vọng** (Expected Value - đo xu thế trung tâm) và **Phương sai** (Variance - đo độ phân tán rủi ro), cùng chiếc cầu nối từ lý thuyết sang thống kê thực nghiệm thông qua **phương sai mẫu hiệu chỉnh $n-1$**.

## 1. Kỳ vọng: Điểm tựa thăng bằng của phân phối xác suất

Trong vật lý, khối tâm hay trọng tâm của một vật thể là điểm cân bằng lực. Trong toán học xác suất, **kỳ vọng** chính là trọng tâm của toàn bộ phân phối xác suất.

Nếu ta tưởng tượng trục số là một thanh đòn bẩy không trọng lượng, trên đó ta đặt các quả cân có khối lượng $P(X = x)$ tại các vị trí tọa độ $x$, thì kỳ vọng $\mathbb{E}[X]$ chính là vị trí đặt điểm tựa duy nhất giúp thanh đòn bẩy thăng bằng hoàn hảo.

### 1.1. Định nghĩa hình thức

1. **Với biến ngẫu nhiên rời rạc:**
   Giả sử $X$ nhận các giá trị $x_1, x_2, \ldots$ với xác suất tương ứng $p_i = P(X = x_i)$. Kỳ vọng là tổng tích các giá trị với trọng số xác suất:
   $$\mathbb{E}[X] = \sum_i x_i P(X = x_i) = \sum_i x_i p_i,$$
   với điều kiện chuỗi hội tụ tuyệt đối: $\sum_i |x_i| p_i < \infty$.

2. **Với biến ngẫu nhiên liên tục:**
   Giả sử $X$ có hàm mật độ xác suất $f(x)$. Kỳ vọng là tích phân trọng số:
   $$\mathbb{E}[X] = \int_{-\infty}^{+\infty} x f(x) \, dx,$$
   với điều kiện $\int_{-\infty}^{+\infty} |x| f(x) \, dx < \infty$.

::: warning Cảnh báo bẫy ngộ nhận: Kỳ vọng có nhất thiết là một giá trị có thể nhận?
Hoàn toàn không! Đây là một ngộ nhận rất phổ biến. 

Xét ví dụ tung một con xúc xắc 6 mặt cân bằng:
$$\mathbb{E}[X] = 1 \cdot \frac{1}{6} + 2 \cdot \frac{1}{6} + 3 \cdot \frac{1}{6} + 4 \cdot \frac{1}{6} + 5 \cdot \frac{1}{6} + 6 \cdot \frac{1}{6} = \frac{21}{6} = 3{,}5.$$

Không có mặt xúc xắc nào mang $3{,}5$ chấm. Nhưng nếu bạn gieo con xúc xắc 1 triệu lần rồi chia trung bình số chấm thu được, con số ấy sẽ áp sát $3{,}5$. Kỳ vọng phản ánh giá trị trung bình tích lũy dài hạn, không phải kết quả của một lần thử đơn lẻ.
:::

### 1.2. Tính chất tuyến tính: Vũ khí tính toán tối thượng

Kỳ vọng sở hữu một tính chất toán học cực kỳ thanh lịch và mạnh mẽ: **Tính tuyến tính**. Với hai biến ngẫu nhiên bất kỳ $X, Y$ và các hằng số $a, b, c \in \mathbb{R}$:

$$\mathbb{E}[aX + bY + c] = a\mathbb{E}[X] + b\mathbb{E}[Y] + c.$$

::: tip Điểm vi diệu của tính tuyến tính
Tính tuyến tính của kỳ vọng **luôn luôn đúng cho dù $X$ và $Y$ có độc lập với nhau hay không**!

Trong thực tế, khi đối diện với các bài toán đếm phức tạp (như số cặp trùng nhau, số chu trình trong đồ thị), người ta thường không tính trực tiếp phân phối của tổng, mà phân rã thành tổng của các biến chỉ số (indicator variables), tính kỳ vọng của từng biến chỉ số rồi cộng lại.
:::

## 2. Phương sai và Độ lệch chuẩn: Đo lường mức độ biến thiên

Kỳ vọng cho biết trung tâm của dữ liệu, nhưng chưa đủ để mô tả hành vi của biến ngẫu nhiên.

Hãy so sánh hai kênh đầu tư:
- Kênh A: Trả chắc chắn 10 triệu đồng mỗi tháng ($P(X = 10) = 1$).
- Kênh B: Tung đồng xu, ngửa nhận 20 triệu, sấp mất trắng 0 đồng ($P(Y = 20) = 0{,}5; P(Y = 0) = 0{,}5$).

Cả hai kênh đều có kỳ vọng lợi nhuận là 10 triệu đồng: $\mathbb{E}[X] = \mathbb{E}[Y] = 10$. Nhưng rõ ràng mức độ rủi ro, dao động của Kênh B là hoàn toàn khác biệt so với Kênh A. Đại lượng đo lường sự dao động quanh tâm đó chính là **phương sai**.

### 2.1. Định nghĩa và công thức tính toán

**Phương sai (Variance)** của $X$, ký hiệu là $\operatorname{Var}(X)$ hoặc $\sigma^2$, đo lường kỳ vọng của bình phương độ lệch giữa $X$ và giá trị trung tâm $\mathbb{E}[X]$:

$$\operatorname{Var}(X) = \mathbb{E}\left[(X - \mathbb{E}[X])^2\right].$$

Khai triển biểu thức đại số:
$$\begin{aligned}
\operatorname{Var}(X) &= \mathbb{E}\left[X^2 - 2X\mathbb{E}[X] + (\mathbb{E}[X])^2\right] \\
&= \mathbb{E}[X^2] - 2\mathbb{E}[X]\mathbb{E}[X] + (\mathbb{E}[X])^2 \\
&= \mathbb{E}[X^2] - (\mathbb{E}[X])^2.
\end{aligned}$$

Đây là công thức thực hành phổ biến nhất: **Phương sai bằng kỳ vọng của bình phương trừ đi bình phương của kỳ vọng**.

### 2.2. Độ lệch chuẩn (Standard Deviation)

Vì phương sai lấy bình phương độ lệch, nên đơn vị đo của phương sai bị bình phương lên (chẳng hạn $\text{triệu đồng}^2$), khiến ta khó so sánh trực tiếp với giá trị trung bình.

Để đưa đại lượng đo độ phân tán về cùng thứ nguyên và cùng đơn vị đo với biến ban đầu, ta lấy căn bậc hai của phương sai, gọi là **độ lệch chuẩn**:

$$\sigma = \sqrt{\operatorname{Var}(X)}.$$

### 2.3. Tính chất của phương sai khi đổi thang đo

1. **Cộng hằng số không làm đổi phương sai:**
   $$\operatorname{Var}(X + c) = \operatorname{Var}(X).$$
   Nếu mọi điểm dữ liệu đều tăng thêm $c$ đơn vị, toàn bộ phân phối dịch chuyển sang phải $c$ đơn vị; khoảng cách tương đối giữa các điểm với trung tâm mới hoàn toàn giữ nguyên, do đó độ phân tán không đổi.

2. **Nhân với hằng số phóng đại phương sai theo bậc hai:**
   $$\operatorname{Var}(aX) = a^2 \operatorname{Var}(X) \implies \sigma(aX) = |a|\sigma(X).$$

3. **Phương sai của tổng hai biến ngẫu nhiên:**
   $$\operatorname{Var}(X + Y) = \operatorname{Var}(X) + \operatorname{Var}(Y) + 2\operatorname{Cov}(X, Y),$$
   trong đó hiệp phương sai giữa $X$ và $Y$ được định nghĩa bởi:
   $$\operatorname{Cov}(X, Y) = \mathbb{E}[(X - \mathbb{E}[X])(Y - \mathbb{E}[Y])].$$
   
   Chỉ khi $X$ và $Y$ **độc lập** (hoặc không tương quan, $\operatorname{Cov}(X, Y) = 0$), phương sai của tổng mới bằng tổng các phương sai:
   $$\operatorname{Var}(X + Y) = \operatorname{Var}(X) + \operatorname{Var}(Y).$$

## 3. Từ lý thuyết tổng thể sang thực tế mẫu dữ liệu

Trong nghiên cứu thực nghiệm, ta hiếm khi biết được phân phối lý thuyết và các tham số thực sự $(\mu, \sigma^2)$ của toàn bộ tổng thể. Ta chỉ có trong tay một mẫu ngẫu nhiên gồm $n$ quan sát độc lập: $x_1, x_2, \ldots, x_n$.

### 3.1. Trung bình mẫu (Sample Mean)

Để ước lượng kỳ vọng tổng thể $\mu$, ta dùng trung bình số học của mẫu:

$$\bar{x} = \frac{1}{n} \sum_{i=1}^n x_i.$$

Trung bình mẫu $\bar{X}$ là một **ước lượng không chệch (unbiased estimator)** của $\mu$, vì kỳ vọng của nó bằng đúng giá trị thực: $\mathbb{E}[\bar{X}] = \mu$.

### 3.2. Phương sai mẫu hiệu chỉnh: Bí mật đằng sau việc chia cho n - 1

Để ước lượng phương sai tổng thể $\sigma^2$, công thức trực giác đầu tiên ta nghĩ đến là lấy trung bình bình phương độ lệch quanh $\bar{x}$:

$$\frac{1}{n}\sum_{i=1}^n (x_i - \bar{x})^2.$$

Thế nhưng, các nhà thống kê phát hiện ra rằng công thức trên bị chệch: Nó luôn **đánh giá thấp (underestimate)** phương sai thực sự của tổng thể! 

Công thức đúng chuẩn để ước lượng không chệch là **phương sai mẫu hiệu chỉnh**, ký hiệu là $s^2$:

$$s^2 = \frac{1}{n - 1} \sum_{i=1}^n (x_i - \bar{x})^2, \quad n > 1.$$

::: derivation Mở bước khó: Tại sao lại chia cho n - 1 (Hiệu chỉnh Bessel)?
Có hai cách hiểu trực giác sâu sắc cho bước hiệu chỉnh này:

1. **Tâm dao động bị dịch chuyển:**
   Phương sai thực sự $\sigma^2$ đo độ phân tán quanh trung bình tổng thể $\mu$: $\frac{1}{n}\sum (x_i - \mu)^2$. Nhưng vì $\mu$ chưa biết, ta buộc phải dùng trung bình mẫu $\bar{x}$ để thay thế. 
   
   Về mặt hình học, $\bar{x}$ là điểm làm cho tổng bình phương khoảng cách $\sum (x_i - c)^2$ đạt giá trị nhỏ nhất tuyệt đối. Do đó, các quan sát mẫu luôn nằm gần $\bar{x}$ hơn là nằm gần $\mu$. Việc đo quanh $\bar{x}$ vô tình làm tổng bình phương độ lệch bị thu nhỏ lại. Để bù đắp cho sự thiếu hụt này, ta phải giảm mẫu số từ $n$ xuống $n-1$.

2. **Mất một bậc tự do (Degrees of Freedom):**
   Trong mẫu gồm $n$ số, luôn tồn tại ràng buộc tất yếu:
   $$\sum_{i=1}^n (x_i - \bar{x}) = 0.$$
   Ràng buộc này có nghĩa là: Nếu bạn đã biết $n - 1$ độ lệch đầu tiên, độ lệch thứ $n$ hoàn toàn bị xác định, không còn tự do thay đổi nữa. Ta đã "tiêu tốn" 1 bậc tự do để ước lượng $\bar{x}$. Do đó, thông tin thực tế về độ biến thiên chỉ còn lại $n - 1$ bậc tự do độc lập.
:::

## 4. Luật số lớn và Định lý giới hạn trung tâm

Khi kích thước mẫu $n$ tăng dần, mối liên hệ giữa mẫu và tổng thể trở nên kỳ diệu thông qua hai định lý nền tảng:

1. **Luật số lớn (Law of Large Numbers - LLN):**
   Khi kích thước mẫu $n$ tiến ra vô cùng, trung bình mẫu $\bar{X}_n$ sẽ hội tụ về kỳ vọng lý thuyết $\mu$ với xác suất bằng 1. Đây là lý do các sòng bạc luôn có lãi trong dài hạn, và các công ty bảo hiểm định giá được rủi ro.

2. **Định lý giới hạn trung tâm (Central Limit Theorem - CLT):**
   Cho dù các biến ngẫu nhiên ban đầu có phân phối theo hình thù kỳ dị nào đi chăng nữa, thì khi kích thước mẫu $n$ đủ lớn (thường $n \ge 30$), **trung bình mẫu $\bar{X}$ luôn xấp xỉ phân phối chuẩn**:
   $$\bar{X} \sim \mathcal{N}\left(\mu, \frac{\sigma^2}{n}\right).$$
   
   Sai số chuẩn của trung bình mẫu là:
   $$SE = \frac{\sigma}{\sqrt{n}}.$$
   Muốn giảm sai số của ước lượng đi một nửa, ta phải tăng kích thước mẫu lên gấp 4 lần ($2^2 = 4$).

## 5. Bài tập tự luyện

### Bài 1. Tính toán kỳ vọng, phương sai và biến đổi tuyến tính

::: exercise
Cho biến ngẫu nhiên rời rạc $X$ có bảng phân phối xác suất như sau:
$$P(X = 1) = 0{,}1; \quad P(X = 2) = 0{,}2; \quad P(X = 3) = 0{,}3; \quad P(X = 4) = 0{,}4.$$

1. Tính kỳ vọng $\mathbb{E}[X]$ và $\mathbb{E}[X^2]$.
2. Tính phương sai $\operatorname{Var}(X)$ và độ lệch chuẩn $\sigma_X$.
3. Đặt $Y = 3X - 5$. Không lập lại bảng phân phối của $Y$, hãy tính $\mathbb{E}[Y]$ và $\operatorname{Var}(Y)$.
:::

::: hint
Dùng công thức định nghĩa $\mathbb{E}[X] = \sum x_i p_i$, sau đó dùng $\operatorname{Var}(X) = \mathbb{E}[X^2] - (\mathbb{E}[X])^2$. Áp dụng tính chất tuyến tính của kỳ vọng và phương sai khi đổi thang đo cho biến $Y$.
:::

::: solution
1. Tính kỳ vọng:
   $$\mathbb{E}[X] = 1(0{,}1) + 2(0{,}2) + 3(0{,}3) + 4(0{,}4) = 0{,}1 + 0{,}4 + 0{,}9 + 1{,}6 = 3{,}0.$$
   $$\mathbb{E}[X^2] = 1^2(0{,}1) + 2^2(0{,}2) + 3^2(0{,}3) + 4^2(0{,}4) = 0{,}1 + 0{,}8 + 2{,}7 + 6{,}4 = 10{,}0.$$

2. Tính phương sai và độ lệch chuẩn:
   $$\operatorname{Var}(X) = \mathbb{E}[X^2] - (\mathbb{E}[X])^2 = 10{,}0 - (3{,}0)^2 = 10{,}0 - 9{,}0 = 1{,}0.$$
   $$\sigma_X = \sqrt{\operatorname{Var}(X)} = \sqrt{1{,}0} = 1{,}0.$$

3. Áp dụng tính chất đổi thang đo cho $Y = 3X - 5$:
   - Kỳ vọng của $Y$:
     $$\mathbb{E}[Y] = \mathbb{E}[3X - 5] = 3\mathbb{E}[X] - 5 = 3(3{,}0) - 5 = 4{,}0.$$
   - Phương sai của $Y$:
     $$\operatorname{Var}(Y) = \operatorname{Var}(3X - 5) = 3^2 \operatorname{Var}(X) = 9 \times 1{,}0 = 9{,}0.$$
     Độ lệch chuẩn của $Y$ là $\sigma_Y = \sqrt{9{,}0} = 3{,}0$.
:::

### Bài 2. Đối chiếu phương sai mẫu chia n và chia n - 1

::: exercise
Một nhóm nghiên cứu ghi nhận một mẫu dữ liệu gồm $n = 5$ quan sát: $[2, 4, 6, 8, 10]$.

1. Tính trung bình mẫu $\bar{x}$.
2. Tính tổng bình phương các độ lệch so với trung bình mẫu $\sum_{i=1}^5 (x_i - \bar{x})^2$.
3. Tính phương sai mẫu nếu chia cho $n$.
4. Tính phương sai mẫu hiệu chỉnh $s^2$ (chia cho $n-1$). Giải thích vì sao $s^2$ luôn lớn hơn giá trị ở câu 3.
:::

::: solution
1. Trung bình mẫu:
   $$\bar{x} = \frac{2 + 4 + 6 + 8 + 10}{5} = \frac{30}{5} = 6{,}0.$$

2. Bảng tính độ lệch và bình phương độ lệch:
   - $(2 - 6)^2 = (-4)^2 = 16$
   - $(4 - 6)^2 = (-2)^2 = 4$
   - $(6 - 6)^2 = 0^2 = 0$
   - $(8 - 6)^2 = 2^2 = 4$
   - $(10 - 6)^2 = 4^2 = 16$

   Tổng bình phương độ lệch:
   $$\sum_{i=1}^5 (x_i - \bar{x})^2 = 16 + 4 + 0 + 4 + 16 = 40{,}0.$$

3. Phương sai mẫu chia cho $n$:
   $$\frac{1}{n}\sum_{i=1}^n (x_i - \bar{x})^2 = \frac{40}{5} = 8{,}0.$$

4. Phương sai mẫu hiệu chỉnh chia cho $n-1$:
   $$s^2 = \frac{1}{n - 1}\sum_{i=1}^n (x_i - \bar{x})^2 = \frac{40}{5 - 1} = \frac{40}{4} = 10{,}0.$$

   Giá trị $s^2 = 10{,}0$ lớn hơn $8{,}0$ vì mẫu số $n - 1 = 4$ nhỏ hơn $n = 5$. Về mặt bản chất thống kê, việc chia cho $n-1$ khuếch đại giá trị phương sai lên một tỷ lệ $\frac{n}{n-1} = \frac{5}{4} = 1{,}25$ lần để bù trừ cho việc $\bar{x}$ luôn nằm gần các điểm mẫu hơn trung bình thực sự $\mu$, đảm bảo ước lượng không bị chệch.
:::

[Xem tiếp: Hệ thống bài tập ôn luyện toàn diện](/xac-suat-thong-ke/bai-tap.md).
