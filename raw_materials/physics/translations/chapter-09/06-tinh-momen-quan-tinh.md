<!-- Nguồn: mục 9.6, trang in 289–290, trang PDF 309–310. -->

## 9.6. Tính toán momen quán tính

Khi một vật rắn là một hệ phân bố khối lượng liên tục, chẳng hạn như một khối trụ đặc hay một quả cầu đồng tính, ta không thể xem vật là tập hợp của một vài chất điểm rời rạc. Trong trường hợp này, phép tính tổng các tích khối lượng với bình phương khoảng cách định nghĩa momen quán tính trong phương trình (9.16) chuyển thành phép tính tích phân.

Giả sử ta chia vật thể thành vô số phần tử khối lượng $dm$ rất nhỏ. Mỗi phần tử nhỏ đến mức mọi điểm thuộc phần tử đó đều có cùng khoảng cách vuông góc $r$ tới trục quay. Khi đó, momen quán tính của vật được xác định bởi:

$$
I = \int r^2\, dm \tag{9.20}
$$

Để tính tích phân này, ta cần biểu diễn khoảng cách $r$ và phần tử khối lượng $dm$ qua cùng một biến số tích phân. Khi vật thể có dạng hình học một chiều như thanh mảnh, ta chọn tọa độ $x$ dọc theo chiều dài của thanh và biểu diễn phần tử khối lượng qua vi phân chiều dài $dx$.

Đối với một vật thể ba chiều, cách thuận tiện nhất là biểu diễn phần tử khối lượng $dm$ qua phần tử thể tích $dV$ và khối lượng riêng $\rho$ của vật thể. Khối lượng riêng là khối lượng trên một đơn vị thể tích, tức là $\rho = \frac{dm}{dV}$. Từ đây ta có $dm = \rho\, dV$. Khi đó phương trình (9.20) được viết lại thành:

$$
I = \int r^2 \rho\, dV
$$

Biểu thức này cho thấy momen quán tính của một vật phụ thuộc vào sự biến thiên của khối lượng riêng bên trong thể tích của nó (Hình 9.22). Nếu vật thể là đồng tính, khối lượng riêng $\rho$ là một hằng số tại mọi vị trí và có thể đưa ra ngoài dấu tích phân:

$$
I = \rho \int r^2\, dV \tag{9.21}
$$

Để tính toán tích phân trong phương trình (9.21), ta biểu diễn phần tử thể tích $dV$ qua các vi phân tọa độ thích hợp với hình dạng của vật. Phần tử thể tích $dV$ luôn phải được lựa chọn sao cho mọi điểm bên trong nó đều có cùng khoảng cách vuông góc $r$ tới trục quay. Cận tích phân được xác định bởi kích thước hình học của vật thể.

![Hình 9.22: Thông qua việc đo lường các biến thiên nhỏ trong quỹ đạo của các vệ tinh, các nhà địa vật lý có thể xác định momen quán tính của Trái Đất. Dữ liệu cho thấy khối lượng riêng của Trái Đất ở phần lõi lớn hơn rất nhiều so với các tầng lớp vỏ bên ngoài.](../img/young-09/b-hinh-9-22.png)

::: example Ví dụ 9.10: Hình trụ rỗng hoặc đặc quay quanh trục đối xứng
Một khối trụ rỗng đồng tính có khối lượng riêng $\rho$, chiều dài $L$, bán kính trong $R_1$ và bán kính ngoài $R_2$ (Hình 9.23). Sử dụng phương pháp tích phân, hãy xác định momen quán tính của khối trụ này đối với trục đối xứng của nó.

![Hình 9.23: Xác định momen quán tính của một hình trụ rỗng đồng tính quay quanh trục đối xứng của nó.](../img/young-09/b-hinh-9-23.png)

**Tóm tắt:**
- Hình trụ rỗng đồng tính có khối lượng riêng $\rho$, chiều dài $L$.
- Bán kính trong $R_1$, bán kính ngoài $R_2$.
- Cần tìm: Momen quán tính $I$ đối với trục đối xứng.

**Hướng đi:**
- Chọn phần tử thể tích là một vỏ trụ mỏng có bán kính $r$, bề dày $dr$ và chiều dài $L$.
- Mọi điểm trên vỏ trụ này đều cách trục quay một khoảng xấp xỉ bằng $r$.
- Tính phần tử khối lượng $dm = \rho\, dV$ của vỏ trụ.
- Lấy tích phân $I = \int r^2\, dm$ với biến $r$ chạy từ bán kính trong $R_1$ đến bán kính ngoài $R_2$.
- Biến đổi biểu thức thu được theo tổng khối lượng $M$ của hình trụ.

**Lời giải:**

Thể tích của vỏ trụ mỏng xấp xỉ thể tích của một tấm phẳng có chiều dài $L$, bề dày $dr$ và chiều rộng bằng chu vi $2\pi r$:

$$
dV = 2\pi r L\, dr
$$

Khối lượng của phần tử vỏ trụ này là:

$$
dm = \rho\, dV = 2\pi \rho L r\, dr
$$

Áp dụng phương trình (9.20), momen quán tính của toàn khối trụ được xác định bằng cách lấy tích phân từ $r = R_1$ đến $r = R_2$:

$$
I = \int_{R_1}^{R_2} r^2 (2\pi \rho L r\, dr)
$$

Đưa các đại lượng không đổi ra ngoài dấu tích phân:

$$
I = 2\pi \rho L \int_{R_1}^{R_2} r^3\, dr
$$

Thực hiện phép tính tích phân:

$$
\begin{aligned}
I &= 2\pi \rho L \left[ \frac{r^4}{4} \right]_{R_1}^{R_2} \\
&= \frac{\pi \rho L}{2} (R_2^4 - R_1^4)
\end{aligned}
$$

Sử dụng hằng đẳng thức hiệu hai bình phương $a^2 - b^2 = (a - b)(a + b)$ cho thừa số bậc bốn:

$$
R_2^4-R_1^4=AB,
$$

Trong đó $A=R_2^2-R_1^2$ và $B=R_2^2+R_1^2$. Đây là hiệu hai bình phương của $R_2^2$ và $R_1^2$.

Ta biểu diễn kết quả này qua tổng khối lượng $M$ của hình trụ. Thể tích toàn phần của hình trụ rỗng là:

$$
V = \pi L (R_2^2 - R_1^2)
$$

Khối lượng toàn phần $M$ của khối trụ bằng khối lượng riêng nhân với thể tích:

$$
M = \rho V
$$

Thay biểu thức thể tích $V$ vào hệ thức khối lượng:

$$
M = \pi \rho L (R_2^2 - R_1^2)
$$

Từ hai kết quả trên, ta nhận thấy:

$$
\frac{\pi \rho L}{2} (R_2^2 - R_1^2) = \frac{1}{2} M
$$

Thay đại lượng này vào biểu thức của $I$, ta rút ra công thức:

$$
I = \frac{1}{2} M (R_1^2 + R_2^2)
$$

**Nhận xét:**

Kết quả này hoàn toàn trùng khớp với trường hợp (e) trong Bảng 9.2.

Trường hợp hình trụ đặc: Bán kính trong $R_1 = 0$ và bán kính ngoài $R_2 = R$. Momen quán tính có dạng:

$$
I = \frac{1}{2} M R^2
$$

Hệ thức này nghiệm đúng với trường hợp (f) trong Bảng 9.2.

Trường hợp vỏ trụ thành rất mỏng: Ta có $R_1 \approx R_2 = R$. Khi đó momen quán tính nhận giá trị:

$$
I = M R^2
$$

Kết quả này phù hợp với trường hợp (g) trong Bảng 9.2. Trực giác vật lý giải thích điều này rất tự nhiên: Toàn bộ khối lượng của vỏ trụ mỏng đều phân bố ở cùng khoảng cách $R$ so với trục quay, do đó:

$$
\begin{aligned}
I &= R^2 \int dm \\
&= M R^2
\end{aligned}
$$
:::

::: example Ví dụ 9.11: Khối cầu đồng tính bán kính R quay quanh trục đi qua tâm
Hãy tìm momen quán tính của một khối cầu đặc đồng tính có khối lượng riêng $\rho$ và bán kính $R$ đối với trục quay đi qua tâm của khối cầu (Hình 9.24).

![Hình 9.24: Xác định momen quán tính của một khối cầu đặc đồng tính quay quanh trục đi qua tâm của nó.](../img/young-09/b-hinh-9-24.png)

**Tóm tắt:**
- Khối cầu đặc đồng tính có bán kính $R$, khối lượng riêng $\rho$, tổng khối lượng $M$.
- Cần tìm: Momen quán tính $I$ đối với trục quay đi qua tâm.

**Hướng đi:**
- Chia khối cầu thành các lát cắt là những đĩa tròn mỏng vuông góc với trục quay.
- Mỗi đĩa tròn có bề dày $dx$ và nằm cách tâm quả cầu một khoảng $x$.
- Áp dụng kết quả đã biết của đĩa tròn đặc để tính vi phân momen quán tính $dI$ của từng đĩa.
- Tích phân theo biến tọa độ $x$ trên toàn bộ phạm vi của khối cầu.
- Biểu diễn kết quả qua khối lượng toàn phần $M$ của khối cầu.

**Lời giải:**

Bán kính $r$ của một đĩa tròn mỏng cách tâm một đoạn $x$ thỏa mãn định lý Pythagore:

$$
r = \sqrt{R^2 - x^2}
$$

Thể tích của đĩa tròn có bề dày $dx$ là:

$$
dV = \pi r^2\, dx
$$

Thay $r^2 = R^2 - x^2$ vào biểu thức thể tích:

$$
dV = \pi (R^2 - x^2)\, dx
$$

Khối lượng $dm$ của đĩa tròn bằng khối lượng riêng nhân thể tích:

$$
dm = \rho\, dV
$$

Do đó:

$$
dm = \pi \rho (R^2 - x^2)\, dx
$$

Theo kết quả của hình trụ đặc trong trường hợp (f) của Bảng 9.2, vi phân momen quán tính của đĩa tròn đối với trục đối xứng vuông góc là:

$$
dI = \frac{1}{2} r^2\, dm
$$

Thay $r^2 = R^2 - x^2$ và biểu thức $dm$:

$$
dI = \frac{\pi \rho}{2} (R^2 - x^2)^2\, dx
$$

Tích phân biểu thức này từ $x = 0$ đến $x = R$ cho ta momen quán tính của một nửa khối cầu. Do tính đối xứng, momen quán tính của toàn bộ khối cầu bằng hai lần tích phân này:

$$
I = 2 \int_0^R dI
$$

Thay biểu thức vi phân $dI$:

$$
I = \pi \rho \int_0^R (R^2 - x^2)^2\, dx
$$

Khai triển biểu thức $(R^2 - x^2)^2$ dưới dấu tích phân thành $R^4 - 2R^2 x^2 + x^4$, phép tính tích phân cho kết quả:

$$
\begin{aligned}
&\int_0^R (R^2 - x^2)^2\, dx \\
&= R^5 \left( 1 - \frac{2}{3} + \frac{1}{5} \right) \\
&= \frac{8}{15} R^5
\end{aligned}
$$

Do đó momen quán tính theo khối lượng riêng nhận giá trị:

$$
I = \frac{8\pi \rho R^5}{15}
$$

Thể tích của khối cầu là $V = \frac{4}{3} \pi R^3$. Khối lượng riêng của vật liệu tính theo khối lượng toàn phần $M$ là:

$$
\rho = \frac{M}{V} = \frac{3M}{4\pi R^3}
$$

Thay biểu thức của $\rho$ vào công thức momen quán tính:

$$
\begin{aligned}
I &= \left( \frac{8\pi R^5}{15} \right) \left( \frac{3M}{4\pi R^3} \right) \\
&= \frac{2}{5} M R^2
\end{aligned}
$$

**Nhận xét:**
- Kết quả thu được hoàn toàn trùng khớp với trường hợp (h) trong Bảng 9.2.
- Momen quán tính của một khối cầu đặc $I = \frac{2}{5} M R^2 = 0{,}40 M R^2$ nhỏ hơn so với momen quán tính của một khối trụ đặc có cùng khối lượng và cùng bán kính $I = \frac{1}{2} M R^2 = 0{,}50 M R^2$. Điều này là do ở khối cầu, phần lớn khối lượng phân bố tập trung ở vùng gần trục quay hơn so với khối trụ.
:::

### Kiểm tra hiểu biết mục 9.6

Hai khối trụ rỗng có cùng bán kính trong và cùng bán kính ngoài, đồng thời có khối lượng bằng nhau, nhưng có chiều dài khác nhau. Một khối trụ được làm từ gỗ có khối lượng riêng thấp và khối trụ kia được làm từ chì có khối lượng riêng cao. Khối trụ nào có momen quán tính lớn hơn đối với trục đối xứng của nó?

(i) Khối trụ gỗ.

(ii) Khối trụ chì.

(iii) Momen quán tính của hai khối trụ bằng nhau.

<details>
<summary>Xem lời giải thích</summary>

**Đáp án đúng là (iii).**

Theo kết quả đã dẫn xuất trong Ví dụ 9.10, momen quán tính của một khối trụ rỗng đối với trục đối xứng chỉ phụ thuộc vào khối lượng $M$, bán kính trong $R_1$ và bán kính ngoài $R_2$:

$$
I = \frac{1}{2} M (R_1^2 + R_2^2)
$$

Công thức này hoàn toàn không phụ thuộc vào chiều dài $L$ hay khối lượng riêng của vật liệu cấu tạo nên khối trụ. Momen quán tính chỉ phụ thuộc vào sự phân bố khối lượng theo phương hướng kính từ trục quay, chứ không phụ thuộc vào sự phân bố khối lượng dọc theo chiều dài của trục. Do cả hai khối trụ có cùng khối lượng và cùng các bán kính giới hạn, momen quán tính của chúng có giá trị bằng nhau.
</details>
