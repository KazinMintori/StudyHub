<!-- Nguồn: mục 9.4, trang in 282–287, trang PDF 302–307. -->

## 9.4. Động năng trong chuyển động quay

Một vật rắn quay là một tập hợp các phần tử khối lượng đang chuyển động, do đó vật rắn sở hữu động năng. Động năng quay này có thể được biểu diễn qua tốc độ góc của vật và một đại lượng vật lý mới: Momen quán tính. Momen quán tính phụ thuộc vào tổng khối lượng của vật cũng như cách phân bố khối lượng đó đối với trục quay.

Để xây dựng biểu thức động năng, ta xem vật rắn gồm vô số hạt nhỏ có khối lượng $m_1, m_2, \dots$ nằm ở các khoảng cách vuông góc tương ứng $r_1, r_2, \dots$ so với trục quay. Ta đánh chỉ số hạt bằng ký hiệu $i$: Phần tử thứ $i$ có khối lượng $m_i$ và khoảng cách vuông góc tới trục quay là $r_i$. Các hạt này không nhất thiết phải cùng nằm trong một mặt phẳng.

Khi vật rắn quay quanh một trục cố định với tốc độ góc $\omega$, mọi hạt trong vật đều chuyển động tròn quanh trục đó với cùng tốc độ góc $\omega$. Tốc độ dài $v_i$ của hạt thứ $i$ liên hệ với khoảng cách $r_i$ qua hệ thức:

$$
v_i = r_i \omega
$$

Các hạt ở khoảng cách khác nhau sẽ có tốc độ dài khác nhau. Động năng của hạt thứ $i$ được xác định bởi:

$$
K_i = \frac{1}{2} m_i v_i^2 = \frac{1}{2} m_i r_i^2 \omega^2
$$

Tổng động năng $K$ của toàn bộ vật rắn bằng tổng động năng $K_i$ của từng phần tử:

$$
K = \sum_i K_i
$$

Thay biểu thức động năng của từng phần tử $K_i = \frac{1}{2} m_i v_i^2$:

$$
K = \sum_i \frac{1}{2} m_i v_i^2
$$

Với mỗi phần tử, tốc độ dài $v_i = r_i \omega$. Thay vào biểu thức động năng:

$$
K = \sum_i \frac{1}{2} m_i r_i^2 \omega^2
$$

Đưa thừa số chung $\frac{1}{2} \omega^2$ ra ngoài dấu tổng:

$$
K = \frac{1}{2} \left( \sum_i m_i r_i^2 \right) \omega^2
$$

Biểu thức trong dấu ngoặc đơn thu được bằng cách nhân khối lượng của từng hạt với bình phương khoảng cách vuông góc từ hạt đó đến trục quay, rồi cộng tất cả các tích lại. Đại lượng này được gọi là **momen quán tính** của vật đối với trục quay đã chọn, ký hiệu là $I$:

$$
I = m_1 r_1^2 + m_2 r_2^2 + \dots
$$

Dạng viết gọn qua ký hiệu tổng lấy theo toàn bộ các phần tử của vật:

$$
I = \sum_i m_i r_i^2 \tag{9.16}
$$

Sử dụng định nghĩa này, biểu thức động năng quay của vật rắn nhận dạng:

$$
K = \frac{1}{2} I \omega^2 \tag{9.17}
$$

Trong hệ đơn vị quốc tế SI, khối lượng có đơn vị $\mathrm{kg}$ và khoảng cách có đơn vị $\mathrm m$, vì vậy đơn vị của momen quán tính là kilôgam mét vuông, ký hiệu là $\mathrm{kg\cdot m^2}$.

Động năng quay $K = \frac{1}{2} I \omega^2$ không phải là một dạng năng lượng mới. Đây chính là tổng động năng tịnh tiến của toàn bộ các phần tử cấu tạo nên vật rắn. Biểu thức này có cấu trúc tương tự như biểu thức động năng tịnh tiến $K = \frac{1}{2} m v^2$: Tốc độ góc $\omega$ tương ứng với tốc độ dài $v$, và momen quán tính $I$ đóng vai trò tương đương với khối lượng quán tính $m$. Momen quán tính đặc trưng cho mức độ quán tính của vật đối với chuyển động quay: Giá trị $I$ càng lớn thì vật càng khó thay đổi trạng thái quay.

![Hình 9.14: Thiết bị thí nghiệm quay tự do quanh một trục thẳng đứng. Bằng cách di chuyển hai quả nặng vào gần hoặc ra xa trục quay, ta có thể thay đổi momen quán tính của hệ.](../img/young-09/b-hinh-9-14.png)

### Ứng dụng sinh học: Momen quán tính của cánh chim

Khi chim vỗ cánh, cánh quay lên và xuống quanh khớp vai. Chim ruồi có cánh nhỏ với momen quán tính nhỏ, nên có thể thay đổi chuyển động cánh nhanh. Tần số đập cánh được nêu trong ví dụ sinh học này có thể lên tới khoảng 70 nhịp mỗi giây.

Trái lại, kền kền Andes (*Vultur gryphus*) có đôi cánh lớn và momen quán tính lớn, nên khó đổi chuyển động cánh nhanh như chim ruồi. Khi cất cánh, nó đập cánh khoảng một nhịp mỗi giây. Phần lớn thời gian, nó lượn và giữ đôi cánh tương đối ổn định.

![Ứng dụng 9.4a: Chim ruồi có cánh nhỏ với momen quán tính nhỏ, phù hợp với chuyển động đập cánh nhanh.](../img/young-09/b-ung-dung-01.png)

![Ứng dụng 9.4: Kền kền Andes có đôi cánh lớn với momen quán tính lớn. Khi cất cánh, nó đập cánh chậm hơn chim ruồi và thường lượn với đôi cánh giữ gần như cố định.](../img/young-09/b-ung-dung-02.png)

### Momen quán tính của vật phân bố khối lượng liên tục

Đối với các vật thể có khối lượng phân bố liên tục như khối trụ, quả cầu hoặc thanh kim loại, ta không thể chia vật thành một vài chất điểm rời rạc. Khi đó, phép tính tổng trong phương trình (9.16) chuyển thành phép tính tích phân trên toàn bộ thể tích của vật:

$$
I = \int r^2\, dm
$$

Trong đó: $dm$ là phần tử khối lượng vô cùng nhỏ, và $r$ là khoảng cách vuông góc từ phần tử $dm$ đến trục quay. Ta sẽ nghiên cứu chi tiết phương pháp tính tích phân này trong mục 9.6.

::: warning Lưu ý quan trọng: Momen quán tính phụ thuộc vào vị trí và phương của trục quay
Momen quán tính của một vật rắn không phải là một hằng số duy nhất gắn liền với vật. Giá trị của $I$ phụ thuộc chặt chẽ vào vị trí đặt trục quay và phương định hướng của trục đó trong không gian. Khi nói đến momen quán tính của một vật, ta luôn phải chỉ rõ trục quay đang xét là trục nào.
:::

::: example Ví dụ 9.6: Momen quán tính đối với các trục quay khác nhau
Một chi tiết máy gồm ba đĩa nhỏ nối với nhau bằng các thanh giằng có khối lượng không đáng kể (Hình 9.15). Khối lượng các đĩa lần lượt là $m_A = 0{,}30\,\mathrm{kg}$, $m_B = 0{,}10\,\mathrm{kg}$ và $m_C = 0{,}20\,\mathrm{kg}$. Các thanh giằng tạo thành một tam giác vuông với các cạnh $A B = 0{,}50\,\mathrm m$, $A C = 0{,}40\,\mathrm m$ và $B C = 0{,}30\,\mathrm m$.

a. Tính momen quán tính của vật thể đối với trục quay 1 đi qua tâm của đĩa A và vuông góc với mặt phẳng hình vẽ.

b. Tính momen quán tính của vật thể đối với trục quay 2 đi qua tâm của hai đĩa B và C.

c. Tính động năng của vật thể nếu nó quay quanh trục 1 với tốc độ góc $\omega = 4{,}0\,\mathrm{rad/s}$.

![Hình 9.15: Chi tiết máy gồm ba đĩa nhỏ liên kết bằng các thanh nhẹ, tạo thành tam giác vuông có các cạnh 0,30 m, 0,40 m và 0,50 m.](../img/young-09/b-hinh-9-15.png)

**Tóm tắt:**
- Khối lượng: $m_A = 0{,}30\,\mathrm{kg}$, $m_B = 0{,}10\,\mathrm{kg}$, $m_C = 0{,}20\,\mathrm{kg}$.
- Kích thước: $A B = 0{,}50\,\mathrm m$, $A C = 0{,}40\,\mathrm m$, $B C = 0{,}30\,\mathrm m$. Vì $0{,}30^2 + 0{,}40^2 = 0{,}50^2$ nên tam giác vuông tại đỉnh C.
- Tốc độ góc ở câu c: $\omega = 4{,}0\,\mathrm{rad/s}$.

**Hướng đi:**
- Ta xem ba đĩa nhỏ là các chất điểm tập trung tại tâm đĩa, và các thanh nối có khối lượng bằng không.
- Đối với mỗi trục quay, xác định khoảng cách vuông góc từ từng đĩa đến trục đó, rồi áp dụng định nghĩa $I = \sum_i m_i r_i^2$.
- Sau khi có momen quán tính $I_1$, áp dụng hệ thức $K = \frac{1}{2} I_1 \omega^2$ để tính động năng quay.

**Lời giải:**

a. Xét trục quay 1 đi qua tâm đĩa A và vuông góc với mặt phẳng:
Đĩa A nằm ngay trên trục quay 1, do đó khoảng cách $r_A = 0$. Khoảng cách từ đĩa B đến trục 1 là $r_B = A B = 0{,}50\,\mathrm m$. Khoảng cách từ đĩa C đến trục 1 là $r_C = A C = 0{,}40\,\mathrm m$. Áp dụng định nghĩa momen quán tính:

$$
I_1 = I_B + I_C
$$

Trong đó phần đóng góp của từng đĩa là:

$$
\begin{aligned}
I_B &= m_B r_B^2 \\
&= (0{,}10)(0{,}50)^2
\end{aligned}
$$

$$
\begin{aligned}
I_C &= m_C r_C^2 \\
&= (0{,}20)(0{,}40)^2
\end{aligned}
$$

Cộng hai thành phần:

$$
\begin{aligned}
I_1 &= 0{,}025 + 0{,}032 \\
&= 0{,}057\,\mathrm{kg\cdot m^2}
\end{aligned}
$$

b. Xét trục quay 2 đi qua tâm hai đĩa B và C:
Cả hai đĩa B và C đều nằm trên trục quay 2, vì thế $r_B = 0$ và $r_C = 0$. Khoảng cách từ đĩa A đến trục 2 là đoạn thẳng vuông góc hạ từ A xuống đường thẳng BC. Vì tam giác vuông tại C, khoảng cách này chính là cạnh $A C = 0{,}40\,\mathrm m$. Momen quán tính đối với trục 2 là:

$$
\begin{aligned}
I_2 &= m_A r_A^2 \\
&= (0{,}30)(0{,}40)^2 \\
&= 0{,}048\,\mathrm{kg\cdot m^2}
\end{aligned}
$$

c. Động năng quay khi vật quay quanh trục 1 với tốc độ góc $\omega = 4{,}0\,\mathrm{rad/s}$:

$$
\begin{aligned}
K_1 &= \frac{1}{2} I_1 \omega^2 \\
&= \frac{1}{2} (0{,}057)(4{,}0)^2 \\
&= 0{,}456\,\mathrm J \approx 0{,}46\,\mathrm J
\end{aligned}
$$

**Nhận xét:**
Momen quán tính đối với trục 2 ($0{,}048\,\mathrm{kg\cdot m^2}$) nhỏ hơn đối với trục 1 ($0{,}057\,\mathrm{kg\cdot m^2}$). Điều này cho thấy việc làm cho chi tiết máy quay quanh trục 2 dễ dàng hơn nhiều so với quay quanh trục 1.
:::

::: warning Lưu ý: Sai lầm khi gom toàn bộ khối lượng về khối tâm
Tuyệt đối không được tính momen quán tính của một vật bằng cách giả định toàn bộ khối lượng tập trung tại khối tâm rồi nhân với bình phương khoảng cách từ khối tâm đến trục quay. Cách làm này hoàn toàn sai bản chất vật lý.

Ví dụ: Một thanh mảnh đồng tính có chiều dài $L$ và khối lượng $M$, quay quanh trục vuông góc đi qua một đầu thanh, có momen quán tính chính xác là $I = \frac{1}{3} M L^2$ (trường hợp b trong Bảng 9.2). Nếu gom toàn bộ khối lượng về khối tâm ở vị trí $L/2$, ta sẽ thu được kết quả sai lệch nghiêm trọng là $M (L/2)^2 = \frac{1}{4} M L^2$.
:::

### Bảng 9.2: Momen quán tính của một số vật thể đồng tính quen thuộc

Bảng 9.2 tổng hợp momen quán tính của các vật thể đồng tính có dạng hình học đối xứng quay quanh các trục chuẩn. Mọi vật thể trong bảng đều có khối lượng $M$ phân bố đều khắp thể tích.

![Bảng 9.2: Momen quán tính của một số vật thể đồng tính có dạng hình học quen thuộc.](../img/young-09/b-bang-9-02.png)

<div class="lecture-data-table">

| Dạng hình học của vật thể | Vị trí và phương của trục quay | Biểu thức momen quán tính |
| --- | --- | --- |
| <span class="table-cell-label">Dạng hình học của vật thể</span> **(a) Thanh mảnh chiều dài $L$** | <span class="table-cell-label">Vị trí và phương của trục quay</span> Trục vuông góc đi qua tâm thanh | <span class="table-cell-label">Biểu thức momen quán tính</span> $I = \frac{1}{12} M L^2$ |
| <span class="table-cell-label">Dạng hình học của vật thể</span> **(b) Thanh mảnh chiều dài $L$** | <span class="table-cell-label">Vị trí và phương của trục quay</span> Trục vuông góc đi qua một đầu thanh | <span class="table-cell-label">Biểu thức momen quán tính</span> $I = \frac{1}{3} M L^2$ |
| <span class="table-cell-label">Dạng hình học của vật thể</span> **(c) Tấm chữ nhật kích thước $a \times b$** | <span class="table-cell-label">Vị trí và phương của trục quay</span> Trục vuông góc với tấm đi qua tâm | <span class="table-cell-label">Biểu thức momen quán tính</span> $I = \frac{1}{12} M (a^2 + b^2)$ |
| <span class="table-cell-label">Dạng hình học của vật thể</span> **(d) Tấm mỏng chữ nhật cạnh $a$** | <span class="table-cell-label">Vị trí và phương của trục quay</span> Trục nằm trong mặt phẳng dọc theo mép | <span class="table-cell-label">Biểu thức momen quán tính</span> $I = \frac{1}{3} M a^2$ |
| <span class="table-cell-label">Dạng hình học của vật thể</span> **(e) Trụ rỗng bán kính trong $R_1$, ngoài $R_2$** | <span class="table-cell-label">Vị trí và phương của trục quay</span> Trục đối xứng của hình trụ | <span class="table-cell-label">Biểu thức momen quán tính</span> $I = \frac{1}{2} M (R_1^2 + R_2^2)$ |
| <span class="table-cell-label">Dạng hình học của vật thể</span> **(f) Trụ đặc bán kính $R$** | <span class="table-cell-label">Vị trí và phương của trục quay</span> Trục đối xứng của hình trụ | <span class="table-cell-label">Biểu thức momen quán tính</span> $I = \frac{1}{2} M R^2$ |
| <span class="table-cell-label">Dạng hình học của vật thể</span> **(g) Trụ rỗng thành mỏng bán kính $R$** | <span class="table-cell-label">Vị trí và phương của trục quay</span> Trục đối xứng của hình trụ | <span class="table-cell-label">Biểu thức momen quán tính</span> $I = M R^2$ |
| <span class="table-cell-label">Dạng hình học của vật thể</span> **(h) Khối cầu đặc bán kính $R$** | <span class="table-cell-label">Vị trí và phương của trục quay</span> Trục đi qua tâm khối cầu | <span class="table-cell-label">Biểu thức momen quán tính</span> $I = \frac{2}{5} M R^2$ |
| <span class="table-cell-label">Dạng hình học của vật thể</span> **(i) Vỏ cầu mỏng bán kính $R$** | <span class="table-cell-label">Vị trí và phương của trục quay</span> Trục đi qua tâm quả cầu | <span class="table-cell-label">Biểu thức momen quán tính</span> $I = \frac{2}{3} M R^2$ |

</div>

### Chiến lược giải bài toán 9.1: Năng lượng trong chuyển động quay

1. **Nhận diện khái niệm:** Phương pháp công và năng lượng rất hữu hiệu để tìm mối liên hệ giữa vị trí và vận tốc của vật rắn quay quanh trục cố định. Tuy nhiên, phương pháp năng lượng không trực tiếp cung cấp thông tin về thời gian chuyển động.
2. **Thiết lập:**
   - Xác định trạng thái ban đầu (điểm 1) và trạng thái cuối (điểm 2).
   - Chọn mốc thế năng trọng trường thích hợp.
   - Nếu có dây quấn quanh vật quay không trượt, sử dụng hệ thức liên hệ vận tốc dài và gia tốc tiếp tuyến: $v = r \omega$ và $a_{\text{tan}} = r \alpha$.
   - Tra cứu momen quán tính $I$ từ Bảng 9.2 hoặc áp dụng định lý trục song song (mục 9.5).
3. **Thực hiện:**
   - Viết biểu thức cơ năng ban đầu $E_1 = K_1 + U_1$, trong đó động năng quay có dạng $K = \frac{1}{2} I \omega^2$.
   - Viết biểu thức cơ năng cuối $E_2 = K_2 + U_2$.
   - Tính công của các lực không thế $W_{\text{other}}$ (nếu có lực kéo hoặc ma sát sinh công).
   - Áp dụng định luật biến thiên cơ năng tổng quát:

$$
E_1 + W_{\text{other}} = E_2
$$

4. **Đánh giá:** Kiểm tra tính hợp lý của kết quả theo các trường hợp giới hạn đặc biệt.

::: example Ví dụ 9.7: Dây cáp tháo cuộn khỏi khối trụ I
Một sợi dây cáp nhẹ không dãn được quấn quanh một khối trụ đặc có khối lượng $M = 50\,\mathrm{kg}$ và đường kính $D = 0{,}120\,\mathrm m$. Khối trụ quay quanh một trục nằm ngang cố định đi qua tâm với ổ bi không ma sát (Hình 9.16). Ta tác dụng một lực không đổi $F = 9{,}0\,\mathrm N$ kéo đầu tự do của dây đi một đoạn $s = 2{,}0\,\mathrm m$. Sợi dây không trượt trên bề mặt trụ khi tháo cuộn. Khối trụ ban đầu đứng yên. Hãy tìm tốc độ góc cuối cùng của khối trụ và tốc độ dài của sợi dây.

![Hình 9.16: Sợi dây cáp quấn quanh khối trụ đặc được kéo bởi lực 9,0 N trên quãng đường 2,0 m.](../img/young-09/b-hinh-9-16.png)

**Tóm tắt:**
- Khối lượng trụ: $M = 50\,\mathrm{kg}$.
- Đường kính: $D = 0{,}120\,\mathrm m$, suy ra bán kính $R = 0{,}060\,\mathrm m$.
- Lực kéo: $F = 9{,}0\,\mathrm N$, quãng đường kéo: $s = 2{,}0\,\mathrm m$.
- Trạng thái đầu: $\omega_1 = 0, K_1 = 0$.

**Hướng đi:**
- Dây cáp được giả thiết không khối lượng, do đó toàn bộ động năng của hệ nằm ở chuyển động quay của khối trụ.
- Lực kéo tác dụng làm sinh công đưa vào hệ: $W_{\text{other}} = F s$.
- Khối trụ đặc có momen quán tính $I = \frac{1}{2} M R^2$.
- Áp dụng định lý công và năng lượng để tìm tốc độ góc $\omega$, sau đó suy ra tốc độ dài của dây qua $v = R \omega$.

**Lời giải:**

Momen quán tính của khối trụ đặc:

$$
\begin{aligned}
I &= \frac{1}{2} M R^2 \\
&= \frac{1}{2} (50)(0{,}060)^2 \\
&= 0{,}090\,\mathrm{kg\cdot m^2}
\end{aligned}
$$

Công do lực kéo tác dụng lên hệ:

$$
\begin{aligned}
W_{\text{other}} &= F s \\
&= (9{,}0\,\mathrm N)(2{,}0\,\mathrm m) \\
&= 18\,\mathrm J
\end{aligned}
$$

Trục quay của khối trụ cố định nên thế năng trọng trường của nó không đổi: $U_1 = U_2 = 0$. Ban đầu khối trụ đứng yên nên $K_1 = 0$. Áp dụng định lý công và năng lượng:

$$
W_{\text{other}} = \frac{1}{2} I \omega^2
$$

Suy ra tốc độ góc cuối cùng của khối trụ:

$$
\begin{aligned}
\omega &= \sqrt{\frac{2 W_{\text{other}}}{I}} \\
&= \sqrt{\frac{2(18)}{0{,}090}} \\
&= 20\,\mathrm{rad/s}
\end{aligned}
$$

Tốc độ dài của sợi dây bằng tốc độ tiếp tuyến của mép ngoài khối trụ:

$$
\begin{aligned}
v &= R \omega \\
&= (0{,}060)(20) \\
&= 1{,}2\,\mathrm{m/s}
\end{aligned}
$$

**Nhận xét:**
Nếu khối lượng của sợi dây không thể bỏ qua, một phần công $18\,\mathrm J$ sẽ chuyển thành động năng của đoạn dây chuyển động. Khi đó động năng và tốc độ góc của khối trụ sẽ nhỏ hơn kết quả tính toán ở trên.
:::

::: example Ví dụ 9.8: Dây cáp tháo cuộn khỏi khối trụ II
Ta quấn một sợi dây cáp nhẹ không dãn quanh một khối trụ đặc có khối lượng $M$ và bán kính $R$. Khối trụ có thể quay không ma sát quanh một trục nằm ngang cố định. Đầu tự do của dây được buộc vào một vật nặng có khối lượng $m$. Thả cho vật nặng rơi từ trạng thái nghỉ ở độ cao $h$ so với sàn nhà (Hình 9.17). Khi vật rơi, dây cáp nhả ra mà không bị dãn hay trượt. Hãy tìm tốc độ của vật nặng và tốc độ góc của khối trụ ngay trước khi vật chạm sàn.

![Hình 9.17: Sơ đồ bài toán: (a) Ban đầu vật nặng ở độ cao h so với sàn; (b) Trạng thái cuối khi vật chuẩn bị chạm sàn.](../img/young-09/b-hinh-9-17.png)

**Tóm tắt:**
- Khối lượng: Khối trụ có khối lượng $M$, bán kính $R$; vật nặng có khối lượng $m$.
- Độ cao ban đầu: $h$, thả từ trạng thái nghỉ với $v_1 = 0$ và $\omega_1 = 0$.
- Dây không dãn và không trượt: $v = R \omega \implies \omega = v/R$.

**Hướng đi:**
- Dây cáp không có khối lượng và không trượt nên cơ năng của toàn hệ được bảo toàn: $W_{\text{other}} = 0$.
- Chọn mốc thế năng trọng trường tại mặt sàn ($y = 0$).
- Ban đầu toàn hệ đứng yên ở độ cao $h$: $K_1 = 0$, $U_1 = mgh$.
- Ngay trước khi chạm sàn: $U_2 = 0$. Động năng của hệ gồm động năng tịnh tiến của vật nặng và động năng quay của khối trụ.
- Thay $\omega = v/R$ và $I = \frac{1}{2} M R^2$, sau đó giải phương trình bảo toàn cơ năng để tìm $v$ và $\omega$.

**Lời giải:**

Động năng của hệ ở trạng thái cuối gồm hai thành phần:

$$
K_2 = \frac{1}{2} m v^2 + \frac{1}{2} I \omega^2
$$

Thành phần động năng quay của khối trụ, với $I = \frac{1}{2} M R^2$ và $\omega = v/R$:

$$
\begin{aligned}
K_{\text{rot}} &= \frac{1}{2} I \omega^2 \\
&= \frac{1}{4} M v^2
\end{aligned}
$$

Tổng động năng của toàn hệ khi đó là:

$$
\begin{aligned}
K_2 &= \frac{1}{2} m v^2 + \frac{1}{4} M v^2 \\
&= \frac{1}{2} \left( m + \frac{1}{2} M \right) v^2
\end{aligned}
$$

Áp dụng định luật bảo toàn cơ năng:

$$
mgh = \frac{1}{2} \left( m + \frac{1}{2} M \right) v^2
$$

Giải phương trình tìm tốc độ dài $v$ của vật rơi:

$$
v = \sqrt{\frac{2gh}{1 + M/(2m)}}
$$

Tốc độ góc của khối trụ tại thời điểm đó:

$$
\begin{aligned}
\omega &= \frac{v}{R} \\
&= \frac{1}{R} \sqrt{\frac{2gh}{1 + M/(2m)}}
\end{aligned}
$$

**Nhận xét:**
- Nếu khối lượng hình trụ rất lớn so với vật nặng ($M \gg m$), mẫu số tiến tới vô cùng và tốc độ $v$ rất nhỏ.
- Ngược lại, nếu khối lượng hình trụ rất nhỏ so với vật nặng ($M \ll m$), tỉ số $M/(2m) \to 0$ và tốc độ $v \approx \sqrt{2gh}$, tiệm cận đúng với tốc độ của một vật rơi tự do hoàn toàn từ độ cao $h$.
:::

### Thế năng trọng trường của một vật thể mở rộng

Trong ví dụ 9.8, ta đã bỏ qua khối lượng của sợi dây cáp. Nếu khối lượng của sợi dây hoặc của một vật thể mở rộng bất kỳ không thể bỏ qua, ta cần xác định thế năng trọng trường của vật thể đó như thế nào?

Nếu gia tốc trọng trường $g$ có cùng độ lớn và phương chiều tại mọi điểm trên vật, thế năng trọng trường của toàn bộ vật thể có giá trị đúng bằng thế năng của một chất điểm mang toàn bộ khối lượng của vật đặt tại khối tâm. Chọn trục tọa độ $y$ hướng thẳng đứng lên trên, thế năng trọng trường $U$ của vật có khối lượng tổng cộng $M$ được xác định bởi:

$$
U = M g y_{\mathrm{cm}} \tag{9.18}
$$

Trong đó: $y_{\mathrm{cm}}$ là tung độ khối tâm của vật thể. Hệ thức này nghiệm đúng cho mọi vật thể mở rộng, dù vật có phải là vật rắn hay không (Hình 9.18).

Để chứng minh phương trình (9.18), ta chia vật thể thành các phần tử khối lượng nhỏ $m_i$. Phần tử thứ $i$ ở độ cao $y_i$ có thế năng $m_i g y_i$. Tổng thế năng của toàn vật là:

$$
\begin{aligned}
U &= \sum_i m_i g y_i \\
&= g \sum_i m_i y_i
\end{aligned}
$$

Theo định nghĩa tọa độ khối tâm:

$$
\sum_i m_i y_i = M y_{\mathrm{cm}}
$$

Thay biểu thức này vào tổng thế năng, ta thu được ngay:

$$
U = M g y_{\mathrm{cm}}
$$

![Hình 9.18: Kỹ thuật nhảy cao Fosbury flop giúp vận động viên uốn cong người qua xà, nhờ đó khối tâm cơ thể có thể đi bên dưới mức xà ngang. Kỹ thuật này đòi hỏi độ tăng thế năng trọng trường nhỏ hơn so với kiểu nhảy truyền thống.](../img/young-09/b-hinh-9-18.png)

### Kiểm tra hiểu biết mục 9.4

Giả sử khối trụ và vật nặng trong Ví dụ 9.8 có khối lượng bằng nhau, tức là $m = M$. Ngay trước khi vật nặng chạm sàn nhà, khẳng định nào sau đây là đúng về mối quan hệ giữa động năng tịnh tiến $K_{\text{vật}}$ của vật nặng và động năng quay $K_{\text{trụ}}$ của khối trụ?

(i) $K_{\text{vật}} > K_{\text{trụ}}$.

(ii) $K_{\text{vật}} < K_{\text{trụ}}$.

(iii) $K_{\text{vật}} = K_{\text{trụ}}$.

<details>
<summary>Xem lời giải thích</summary>

**Đáp án đúng là (i).**

Động năng tịnh tiến của vật nặng khi chạm sàn là:

$$
K_{\text{vật}} = \frac{1}{2} m v^2
$$

Động năng quay của khối trụ đặc tại thời điểm đó là:

$$
\begin{aligned}
K_{\text{trụ}} &= \frac{1}{2} I \omega^2 \\
&= \frac{1}{2} \left( \frac{1}{2} m R^2 \right) \frac{v^2}{R^2} \\
&= \frac{1}{4} m v^2
\end{aligned}
$$

So sánh hai giá trị:

$$
K_{\text{vật}} = \frac{1}{2} m v^2 = 2 K_{\text{trụ}}
$$

Vì vậy $K_{\text{vật}} > K_{\text{trụ}}$. Tổng động năng của cả hệ là $\frac{3}{4} m v^2$, trong đó vật nặng chiếm hai phần ba và khối trụ chiếm một phần ba.
</details>
