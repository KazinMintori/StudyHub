---
course: xac-suat-thong-ke
lecture: 02-bien-ngau-nhien
section: lecture
title: "Biến ngẫu nhiên & phân phối"
prerequisites: ["bien-ngau-nhien", "to-hop", "tich-phan"]
lessonStatus: ready
description: "Bản chất biến ngẫu nhiên, phân biệt rời rạc và liên tục, hàm khối xác suất PMF, hàm mật độ PDF và hàm phân phối tích lũy CDF."
---

Trong đời sống, kết quả của một hiện tượng ngẫu nhiên xuất hiện dưới vô vàn hình thái: một đồng xu rơi xuống mặt ngửa hay mặt sấp, một con xúc xắc lăn ra số chấm từ 1 đến 6, thời gian bạn phải chờ chuyến xe buýt kế tiếp, hay số lượng truy cập máy chủ tiếp nhận trong một phần nghìn giây. Làm thế nào để toán học hóa những hiện tượng đa dạng đó vào cùng một hệ thống tính toán nhất quán?

Giải pháp kinh điển của lý thuyết xác suất là phát minh ra khái niệm **biến ngẫu nhiên (Random Variable)**: một cỗ máy ánh xạ gán mỗi kết cục thực tế thành một con số cụ thể. Khi các kết cục đã trở thành số thực, **quy luật phân phối xác suất** sẽ cung cấp bức tranh toàn cảnh về việc các con số đó xuất hiện với khả năng nhiều hay ít.

## 1. Bản chất của biến ngẫu nhiên: Chiếc cầu nối từ biến cố sang con số

Dù mang tên là "biến", nhưng trong toán học hiện đại, biến ngẫu nhiên thực chất là một **hàm số**.

Cho một phép thử ngẫu nhiên với không gian mẫu $\Omega$. Một **biến ngẫu nhiên** $X$ là một ánh xạ từ không gian mẫu vào tập số thực $\mathbb{R}$:

$$X: \Omega \to \mathbb{R}.$$

Với mỗi kết cục sơ cấp $\omega \in \Omega$, hàm số $X$ gán cho nó một giá trị số thực $x = X(\omega)$.

::: example Ví dụ trực quan: Tung 3 đồng xu cân bằng
Xét phép thử tung 3 đồng xu cân bằng độc lập. Không gian mẫu gồm $2^3 = 8$ kết cục:
$$\Omega = \{NNN, NNS, NSN, NSS, SNN, SNS, SSN, SSS\}.$$

Nếu ta quan tâm đến "số mặt ngửa xuất hiện", ta định nghĩa biến ngẫu nhiên $X$ đếm số mặt $N$. Khi đó:
- $X(SSS) = 0$
- $X(NSS) = X(SNS) = X(SSN) = 1$
- $X(NNS) = X(NSN) = X(SNN) = 2$
- $X(NNN) = 3$

Tập giá trị mà $X$ có thể nhận là $\{0, 1, 2, 3\}$. Khi ta viết ký hiệu $P(X = 2)$, bản chất toán học là ta đang đo xác suất của tập con các kết cục:
$$P(X = 2) = P(\{\omega \in \Omega : X(\omega) = 2\}) = P(\{NNS, NSN, SNN\}) = \frac{3}{8}.$$
:::

Dựa vào tập giá trị mà $X$ có thể nhận, ta chia biến ngẫu nhiên thành hai thế giới riêng biệt:
1. **Biến ngẫu nhiên rời rạc (Discrete):** Tập giá trị nhận được là hữu hạn hoặc vô hạn đếm được (chẳng hạn $\{0, 1, 2, \ldots\}$).
2. **Biến ngẫu nhiên liên tục (Continuous):** Tập giá trị lấp đầy một khoảng hoặc toàn bộ trục số thực $\mathbb{R}$.

## 2. Biến ngẫu nhiên rời rạc và Hàm khối xác suất (PMF)

Quy luật phân phối của một biến ngẫu nhiên rời rạc $X$ được mô tả đầy đủ bởi **hàm khối xác suất (Probability Mass Function - PMF)**, ký hiệu là $p(x)$:

$$p(x) = P(X = x).$$

Hai điều kiện bắt buộc của một PMF hợp lệ:
1. $p(x) \ge 0$ với mọi giá trị $x$.
2. Tổng xác suất trên toàn bộ các giá trị có thể nhận phải bằng 1:
   $$\sum_{x} p(x) = 1.$$

### 2.1. Các phân phối rời rạc kinh điển

Trong thực tế kỹ thuật và đời sống, phần lớn các bài toán đếm đều quy về bốn họ phân phối nền tảng:

1. **Phân phối Bernoulli** $\text{Bernoulli}(p)$:
   Mô hình hóa một phép thử nhị phân duy nhất (thành công hoặc thất bại, đúng hoặc sai, click chuột hoặc không click). $X$ nhận giá trị 1 với xác suất $p$, và nhận giá trị 0 với xác suất $1 - p$:
   $$P(X = 1) = p, \quad P(X = 0) = 1 - p.$$

2. **Phân phối Nhị thức (Binomial)** $\text{Bin}(n, p)$:
   $X$ đếm số lần thành công trong $n$ phép thử Bernoulli độc lập, mỗi phép thử có cùng xác suất thành công $p$. Công thức PMF:
   $$P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}, \quad k = 0, 1, \ldots, n.$$

   ::: derivation Mở rộng bước suy luận của công thức nhị thức
   Tại sao lại có sự xuất hiện của hệ số tổ hợp $\binom{n}{k}$?
   
   Một chuỗi cụ thể gồm đúng $k$ lần thành công và $n - k$ lần thất bại (ví dụ: $k$ lần đầu thành công, $n-k$ lần sau thất bại) có xác suất xảy ra là $p^k(1-p)^{n-k}$ (do tính độc lập giữa các lần thử).
   
   Tuy nhiên, $k$ lần thành công có thể nằm rải rác ở bất kỳ vị trí nào trong $n$ lần thử. Số cách chọn ra $k$ vị trí trong tổng số $n$ vị trí chính là tổ hợp $\binom{n}{k} = \frac{n!}{k!(n-k)!}$. Vì các chuỗi này xung khắc nhau, ta cộng xác suất của tất cả các chuỗi lại để thu được công thức tổng quát.
   :::

3. **Phân phối Poisson** $\text{Poisson}(\lambda)$:
   Mô hình hóa số lần một biến cố hiếm xảy ra trong một khoảng thời gian hoặc không gian liên tục cố định (ví dụ: số yêu cầu gửi tới máy chủ web trong 1 giây, số lỗi chính tả trên 1 trang sách, số cuộc gọi tới tổng đài cấp cứu trong 1 giờ).
   $$P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!}, \quad k = 0, 1, 2, \ldots$$
   với tham số $\lambda > 0$ là tốc độ xảy ra trung bình trong khoảng quan sát.

4. **Phân phối Hình học (Geometric)** $\text{Geom}(p)$:
   $X$ đếm số phép thử độc lập cần thực hiện cho đến khi xuất hiện **lần thành công đầu tiên**. Muốn thành công ở lần thứ $k$, bắt buộc $k-1$ lần trước đó phải thất bại:
   $$P(X = k) = (1-p)^{k-1}p, \quad k = 1, 2, 3, \ldots$$

## 3. Biến ngẫu nhiên liên tục: Mật độ không phải là xác suất

Khi chuyển sang các đại lượng đo lường vật lý (như thời gian, khoảng cách, nhiệt độ, trọng lượng), ta bước vào thế giới của biến ngẫu nhiên liên tục. Ở đây, một hiện tượng phản trực giác xuất hiện: **xác suất để biến ngẫu nhiên nhận đúng một giá trị cụ thể bất kỳ luôn bằng 0**.

$$P(X = x_0) = 0 \quad \text{với mọi } x_0 \in \mathbb{R}.$$

Để hiểu điều này, hãy tưởng tượng thời gian bạn chờ một chuyến tàu điện là ngẫu nhiên trong khoảng từ 0 đến 10 phút. Khoảng $[0, 10]$ chứa vô số điểm số thực không thể đếm xuể (như $3{,}14159265\ldots$ phút). Khả năng chiếc tàu đến vào đúng tích tắc chính xác tuyệt đối đến vô hạn chữ số thập phân đó là 1 chia cho vô cùng, tức bằng 0.

Vì vậy, với biến liên tục, ta không thể định nghĩa xác suất tại một điểm. Thay vào đó, ta sử dụng **hàm mật độ xác suất (Probability Density Function - PDF)**, ký hiệu là $f(x)$. Xác suất chỉ có ý nghĩa khi xét trên một **khoảng** $[a, b]$, và được tính bằng diện tích hình thang cong dưới đường mật độ:

$$P(a \le X \le b) = \int_a^b f(x) \, dx.$$

Hai điều kiện bắt buộc của một PDF:
1. $f(x) \ge 0$ với mọi $x \in \mathbb{R}$.
2. Toàn bộ diện tích dưới đường cong mật độ trên toàn trục số phải bằng 1:
   $$\int_{-\infty}^{+\infty} f(x) \, dx = 1.$$

::: warning Cảnh báo bẫy ngộ nhận: Giá trị mật độ f(x) hoàn toàn có thể lớn hơn 1
Nhiều người lầm tưởng rằng vì xác suất không được vượt quá 1 nên $f(x)$ cũng phải $\le 1$. Đây là ngộ nhận sai lầm!

$f(x)$ đo **mật độ xác suất** (xác suất trên một đơn vị độ dài), giống như khối lượng riêng trong vật lý. Nếu một biến ngẫu nhiên nhận giá trị tập trung dày đặc trong một khoảng cực hẹp, mật độ tại đó sẽ rất cao. 

Ví dụ, nếu $X$ phân phối đều trên khoảng $[0; 0{,}1]$, thì mật độ bắt buộc phải là $f(x) = \frac{1}{0{,}1 - 0} = 10$ trên khoảng đó để đảm bảo diện tích tích phân bằng 1. Điều bị giới hạn trong đoạn $[0, 1]$ là **diện tích tích phân** $P(a \le X \le b)$, không phải giá trị của hàm mật độ $f(x)$.
:::

### 3.1. Các phân phối liên tục tiêu biểu

1. **Phân phối Đều (Uniform)** $U[a, b]$:
   Khả năng rơi vào các khoảng có độ dài bằng nhau là như nhau. Hàm mật độ là một đường nằm ngang bằng phẳng:
   $$f(x) = \begin{cases} \frac{1}{b - a} & \text{khi } a \le x \le b \\ 0 & \text{ngược lại} \end{cases}$$

2. **Phân phối Chuẩn (Normal / Gaussian)** $\mathcal{N}(\mu, \sigma^2)$:
   Được mệnh danh là "chiếc chuông vĩ đại của tự nhiên", xuất hiện ở khắp mọi nơi từ chiều cao con người, sai số đo lường đến biến động giá tài chính:
   $$f(x) = \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{(x - \mu)^2}{2\sigma^2}}.$$
   Đồ thị đối xứng qua kỳ vọng $\mu$, độ rộng được kiểm soát bởi độ lệch chuẩn $\sigma$. 
   
   Một quy tắc thực nghiệm người ta hay dùng trong thực tế để ước lượng nhanh phân phối chuẩn là **quy tắc $68 - 95 - 99{,}7$**:
   - Khoảng $[\mu - \sigma, \mu + \sigma]$ chứa khoảng $68{,}27\%$ xác suất.
   - Khoảng $[\mu - 2\sigma, \mu + 2\sigma]$ chứa khoảng $95{,}45\%$ xác suất.
   - Khoảng $[\mu - 3\sigma, \mu + 3\sigma]$ chứa khoảng $99{,}73\%$ xác suất.

## 4. Hàm phân phối tích lũy (CDF): Chiếc cầu nối vạn năng

Vì biến rời rạc dùng PMF (phép cộng) còn biến liên tục dùng PDF (phép tích phân), toán học cần một công cụ thống nhất cho cả hai thế giới. Đó chính là **hàm phân phối tích lũy (Cumulative Distribution Function - CDF)**, ký hiệu là $F(x)$:

$$F(x) = P(X \le x), \quad \forall x \in \mathbb{R}.$$

$F(x)$ cho biết xác suất tích lũy để biến ngẫu nhiên $X$ nhận giá trị nhỏ hơn hoặc bằng một ngưỡng $x$ nào đó.

Bốn tính chất nền tảng của CDF:
1. **Tính không giảm:** Nếu $x_1 \le x_2$ thì $F(x_1) \le F(x_2)$.
2. **Giới hạn tiệm cận:** $\lim_{x \to -\infty} F(x) = 0$ và $\lim_{x \to +\infty} F(x) = 1$.
3. **Tính liên tục bên phải:** $\lim_{t \to x^+} F(t) = F(x)$.
4. **Công thức tính xác suất trên nửa khoảng:** Với mọi $a < b$:
   $$P(a < X \le b) = F(b) - F(a).$$

::: tip Lưu ý về dấu bằng ở biên
- Đối với **biến ngẫu nhiên liên tục**: Vì xác suất tại từng điểm bằng 0 ($P(X = a) = P(X = b) = 0$), nên việc lấy dấu bằng hay không ở biên không làm thay đổi kết quả:
  $$P(a \le X \le b) = P(a < X \le b) = P(a \le X < b) = P(a < X < b) = F(b) - F(a).$$
- Đối với **biến ngẫu nhiên rời rạc**: Dấu bằng ở biên có ý nghĩa quyết định! Đồ thị CDF của biến rời rạc có dạng bậc thang gián đoạn tại các điểm có xác suất dương:
  $$P(a \le X \le b) = F(b) - F(a^-) = F(b) - F(a) + P(X = a).$$
:::

## 5. Quy trình 4 bước lựa chọn mô hình phân phối

Khi đứng trước một bài toán phân tích dữ liệu thực tế, làm thế nào để chọn đúng phân phối? Đây là quy trình tư duy từng bước:

1. **Xác định rõ định nghĩa của biến $X$ và đơn vị đo:** $X$ đang đếm số lượng sự kiện, đo thời gian, hay ghi nhận tỷ lệ?
2. **Xác định miền giá trị:** Rời rạc (đếm được $\{0, 1, 2, \ldots\}$) hay liên tục (trên một khoảng $[a, b]$ hoặc toàn bộ $\mathbb{R}$)?
3. **Kiểm tra các giả định vật lý của mô hình:**
   - Số phép thử có cố định không? Các phép thử có độc lập không? $\to$ Phân phối Nhị thức.
   - Các sự kiện có xảy ra ngẫu nhiên độc lập theo thời gian với tốc độ trung bình không đổi không? $\to$ Phân phối Poisson.
   - Hiện tượng có chịu tác động tổng hòa của nhiều yếu tố ngẫu nhiên nhỏ độc lập không? $\to$ Phân phối Chuẩn (theo Định lý giới hạn trung tâm).
4. **Viết rõ biến cố dưới dạng bất đẳng thức toán học rồi mới áp dụng công thức tính toán.**

## 6. Bài tập tự luyện

### Bài 1. Khảo sát biến ngẫu nhiên rời rạc và hàm phân phối tích lũy

::: exercise
Một hộp chứa 5 quả cầu trắng và 3 quả cầu đen. Ta rút ngẫu nhiên không hoàn lại 3 quả cầu. Gọi $X$ là số quả cầu trắng rút được.

1. Xác định tập các giá trị có thể nhận của $X$.
2. Lập bảng phân phối xác suất (PMF) của $X$.
3. Viết biểu thức hàm phân phối tích lũy $F(x)$ của $X$.
4. Tính xác suất $P(1 \le X \le 2)$.
:::

::: hint
Số cách rút 3 quả từ 8 quả là $\binom{8}{3}$. Dùng quy tắc tổ hợp để đếm số cách chọn $k$ quả trắng và $3-k$ quả đen.
:::

::: solution
1. Vì có tối đa 3 quả đen, nên ngay cả khi rút hết 3 quả đen thì vẫn có thể có 0 quả trắng. Mặt khác, chỉ rút 3 quả nên tối đa có 3 quả trắng. Vậy tập giá trị của $X$ là $\{0, 1, 2, 3\}$.

2. Tổng số cách chọn 3 quả cầu từ 8 quả: $\binom{8}{3} = \frac{8 \times 7 \times 6}{6} = 56$.
   - $P(X = 0) = \frac{\binom{5}{0}\binom{3}{3}}{56} = \frac{1 \times 1}{56} = \frac{1}{56}$.
   - $P(X = 1) = \frac{\binom{5}{1}\binom{3}{2}}{56} = \frac{5 \times 3}{56} = \frac{15}{56}$.
   - $P(X = 2) = \frac{\binom{5}{2}\binom{3}{1}}{56} = \frac{10 \times 3}{56} = \frac{30}{56}$.
   - $P(X = 3) = \frac{\binom{5}{3}\binom{3}{0}}{56} = \frac{10 \times 1}{56} = \frac{10}{56}$.

   Kiểm tra tổng xác suất: $\frac{1 + 15 + 30 + 10}{56} = \frac{56}{56} = 1$ (chuẩn hóa chính xác).

3. Biểu thức hàm phân phối tích lũy $F(x) = P(X \le x)$:
   $$F(x) = \begin{cases} 
   0 & \text{khi } x < 0 \\
   \frac{1}{56} & \text{khi } 0 \le x < 1 \\
   \frac{16}{56} = \frac{2}{7} & \text{khi } 1 \le x < 2 \\
   \frac{46}{56} = \frac{23}{28} & \text{khi } 2 \le x < 3 \\
   1 & \text{khi } x \ge 3
   \end{cases}$$

4. Xác suất $P(1 \le X \le 2)$:
   $$P(1 \le X \le 2) = P(X = 1) + P(X = 2) = \frac{15}{56} + \frac{30}{56} = \frac{45}{56} \approx 80{,}36\%.$$
:::

### Bài 2. Chuẩn hóa hàm mật độ và tính xác suất biến liên tục

::: exercise
Cho biến ngẫu nhiên liên tục $X$ có hàm mật độ xác suất dạng:
$$f(x) = \begin{cases} c(2x - x^2) & \text{khi } 0 \le x \le 2 \\ 0 & \text{ngược lại} \end{cases}$$

1. Tìm hằng số chuẩn hóa $c$ để $f(x)$ là một hàm mật độ xác suất hợp lệ.
2. Tìm hàm phân phối tích lũy $F(x)$.
3. Tính xác suất $P(0{,}5 \le X \le 1{,}5)$.
:::

::: hint
Điều kiện chuẩn hóa đòi hỏi tích phân của $f(x)$ trên miền $[0, 2]$ phải bằng 1. Sau khi tìm được $c$, tính tích phân trên đoạn $[0{,}5; 1{,}5]$.
:::

::: solution
1. Điều kiện để $f(x)$ là hàm mật độ xác suất: $\int_{-\infty}^{+\infty} f(x) \, dx = 1$:
   $$\int_0^2 c(2x - x^2) \, dx = c \left[ x^2 - \frac{x^3}{3} \right]_0^2 = c \left( 4 - \frac{8}{3} \right) = c \cdot \frac{4}{3} = 1 \implies c = \frac{3}{4}.$$

   Vì với $x \in [0, 2]$, $2x - x^2 = x(2-x) \ge 0$ và $c = \frac{3}{4} > 0$, nên $f(x) \ge 0$ trên toàn miền. Vậy $c = \frac{3}{4}$ thỏa mãn đầy đủ hai điều kiện của PDF.

2. Với $0 \le x \le 2$, hàm phân phối tích lũy là:
   $$F(x) = \int_0^x \frac{3}{4}(2t - t^2) \, dt = \frac{3}{4} \left[ t^2 - \frac{t^3}{3} \right]_0^x = \frac{3}{4}x^2 - \frac{1}{4}x^3.$$
   - Khi $x < 0$: $F(x) = 0$.
   - Khi $x > 2$: $F(x) = 1$.

3. Xác suất $P(0{,}5 \le X \le 1{,}5)$:
   $$P(0{,}5 \le X \le 1{,}5) = F(1{,}5) - F(0{,}5).$$

   Ta tính giá trị tại hai đầu mút:
   $$F(1{,}5) = \frac{3}{4}(1{,}5)^2 - \frac{1}{4}(1{,}5)^3 = \frac{27}{16} - \frac{27}{32} = \frac{27}{32}.$$
   $$F(0{,}5) = \frac{3}{4}(0{,}5)^2 - \frac{1}{4}(0{,}5)^3 = \frac{3}{16} - \frac{1}{32} = \frac{5}{32}.$$

   Do đó:
   $$P(0{,}5 \le X \le 1{,}5) = \frac{27}{32} - \frac{5}{32} = \frac{22}{32} = \frac{11}{16} = 0{,}6875.$$
:::

[Bài tiếp theo: Kỳ vọng, phương sai & mẫu dữ liệu](/xac-suat-thong-ke/bai-giang/03-ky-vong-phuong-sai.md).
