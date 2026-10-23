<!-- Nguồn: mục 9.5, trang in 287–288, trang PDF 307–308. -->

## 9.5. Định lý trục song song

Trong mục 9.4, ta đã nhận thấy một vật rắn không chỉ có một giá trị momen quán tính duy nhất. Trên thực tế, một vật có vô số giá trị momen quán tính khác nhau, tương ứng với vô số trục quay có thể lựa chọn trong không gian. Tuy nhiên, giữa momen quán tính của vật đối với một trục đi qua khối tâm và momen quán tính đối với bất kỳ trục nào khác song song với trục ban đầu luôn tồn tại một mối liên hệ đơn giản: Đó là **định lý trục song song** (Hình 9.19).

Biểu thức toán học của định lý trục song song có dạng:

$$
I_P = I_{\mathrm{cm}} + M d^2 \tag{9.19}
$$

Trong đó:
- $I_P$ là momen quán tính của vật đối với trục quay đi qua điểm $P$ bất kỳ.
- $I_{\mathrm{cm}}$ là momen quán tính của vật đối với trục quay song song đi qua khối tâm.
- $M$ là tổng khối lượng của vật rắn.
- $d$ là khoảng cách vuông góc giữa hai trục quay song song nói trên.

![Hình 9.19: Định lý trục song song cho một chiếc gậy bóng chày có khối lượng M. Trục quay 1 đi qua khối tâm với momen quán tính Icm, trục quay 2 đi qua điểm P song song với trục 1 ở khoảng cách d, có momen quán tính IP = Icm + Md2.](../img/young-09/b-hinh-9-19.png)

### Chứng minh định lý trục song song

Để chứng minh định lý, ta xét hai trục quay cùng song song với trục tọa độ $z$: Một trục đi qua khối tâm và trục còn lại đi qua điểm $P$ (Hình 9.20).

Trước hết, ta cắt vật thể thành các lát cắt rất mỏng song song với mặt phẳng $x y$ và vuông góc với trục $z$. Chọn gốc tọa độ $O$ tại khối tâm của vật, khi đó tọa độ của khối tâm là:

$$
x_{\mathrm{cm}} = y_{\mathrm{cm}} = z_{\mathrm{cm}} = 0
$$

Trục quay đi qua khối tâm cắt lát mỏng tại gốc tọa độ $O$. Trục quay song song đi qua điểm $P$ cắt lát mỏng tại điểm có tọa độ $(a, b)$. Khoảng cách giữa hai trục song song là $d$, thỏa mãn hệ thức:

$$
d^2 = a^2 + b^2
$$

Xét một phần tử khối lượng $m_i$ bất kỳ trong lát mỏng có tọa độ $(x_i, y_i, z_i)$. Momen quán tính của lát mỏng đối với trục quay đi qua khối tâm (tại $O$) là:

$$
I_{\mathrm{cm}} = \sum_i m_i (x_i^2 + y_i^2)
$$

Tọa độ của phần tử $m_i$ đối với trục quay đi qua điểm $P$ là $(x_i - a, y_i - b)$. Bình phương khoảng cách từ phần tử $m_i$ đến trục quay qua $P$ ký hiệu là $r_i^2$:

$$
r_i^2 = (x_i - a)^2 + (y_i - b)^2
$$

Momen quán tính của lát mỏng đối với trục qua $P$ là:

$$
I_P = \sum_i m_i r_i^2
$$

Vì các cao độ $z_i$ đo vuông góc với mặt phẳng lát mỏng không xuất hiện trong các biểu thức khoảng cách, ta có thể mở rộng phép lấy tổng cho toàn bộ các phần tử cấu tạo nên vật thể. Khi khai triển các bình phương khoảng cách tọa độ, các số hạng bậc nhất chứa tọa độ khối tâm:

$$
\sum_i m_i x_i = 0
$$

$$
\sum_i m_i y_i = 0
$$

đều triệt tiêu do gốc tọa độ $O$ trùng với khối tâm của vật ($x_{\mathrm{cm}} = 0, y_{\mathrm{cm}} = 0$).

Số hạng bậc hai thứ nhất chính là momen quán tính đối với trục đi qua khối tâm $I_{\mathrm{cm}}$. Số hạng cuối cùng chứa tổng khối lượng toàn phần của vật $\sum_i m_i = M$. Kết hợp với hệ thức khoảng cách giữa hai trục song song $a^2 + b^2 = d^2$, ta thu được định lý trục song song:

$$
\begin{aligned}
I_P &= I_{\mathrm{cm}} + (a^2 + b^2) M \\
&= I_{\mathrm{cm}} + M d^2 \tag{9.19}
\end{aligned}
$$

Phương trình (9.19) đã được chứng minh đầy đủ cho vật thể ba chiều tổng quát.

![Hình 9.20: Phần tử khối lượng mi có tọa độ (xi, yi) đối với trục quay đi qua khối tâm (cm), và có tọa độ (xi - a, yi - b) đối với trục song song đi qua điểm P.](../img/young-09/b-hinh-9-20.png)

### Ý nghĩa vật lý của định lý trục song song

Phương trình (9.19) cho thấy: Vì đại lượng $M d^2$ luôn là một số dương khi $d > 0$, momen quán tính của một vật rắn đối với trục đi qua khối tâm luôn nhỏ hơn momen quán tính đối với bất kỳ trục nào khác song song với nó:

$$
I_P > I_{\mathrm{cm}} \quad (\text{với } d > 0)
$$

Nói cách khác, trong tất cả các trục song song với nhau, trục đi qua khối tâm là trục có momen quán tính nhỏ nhất. Do đó, việc làm cho một vật bắt đầu quay quanh trục đi qua khối tâm luôn tốn ít năng lượng nhất và dễ dàng nhất.

::: example Ví dụ 9.9: Sử dụng định lý trục song song
Một bộ phận trong cơ cấu cơ khí có khối lượng $M = 3{,}6\,\mathrm{kg}$ (Hình 9.21). Phép đo thực nghiệm cho thấy momen quán tính của bộ phận này đối với một trục quay đi qua điểm P, cách khối tâm một khoảng $d = 0{,}15\,\mathrm m$, có giá trị là $I_P = 0{,}132\,\mathrm{kg\cdot m^2}$. Hãy tính momen quán tính $I_{\mathrm{cm}}$ của bộ phận này đối với trục quay song song đi qua khối tâm.

![Hình 9.21: Xác định momen quán tính Icm qua phép đo momen quán tính IP đối với trục song song cách khối tâm 0,15 m.](../img/young-09/b-hinh-9-21.png)

**Tóm tắt:**
- Khối lượng: $M = 3{,}6\,\mathrm{kg}$.
- Khoảng cách giữa hai trục song song: $d = 0{,}15\,\mathrm m$.
- Momen quán tính đo được: $I_P = 0{,}132\,\mathrm{kg\cdot m^2}$.

**Hướng đi:**
- Áp dụng định lý trục song song $I_P = I_{\mathrm{cm}} + M d^2$.
- Biến đổi phương trình để tìm đại lượng mục tiêu $I_{\mathrm{cm}} = I_P - M d^2$.

**Lời giải:**

Từ định lý trục song song, ta biến đổi hệ thức:

$$
I_{\mathrm{cm}} = I_P - M d^2
$$

Tính đại lượng dịch chuyển trục $M d^2$:

$$
\begin{aligned}
M d^2 &= (3{,}6)(0{,}15)^2 \\
&= 0{,}081\,\mathrm{kg\cdot m^2}
\end{aligned}
$$

Thay vào biểu thức của $I_{\mathrm{cm}}$:

$$
\begin{aligned}
I_{\mathrm{cm}} &= 0{,}132 - 0{,}081 \\
&= 0{,}051\,\mathrm{kg\cdot m^2}
\end{aligned}
$$

**Nhận xét:**
Đúng như dự đoán lý thuyết, giá trị $I_{\mathrm{cm}} = 0{,}051\,\mathrm{kg\cdot m^2}$ nhỏ hơn đáng kể so với $I_P = 0{,}132\,\mathrm{kg\cdot m^2}$. Momen quán tính đối với trục đi qua khối tâm luôn là giá trị cực tiểu trong họ các trục song song.
:::

### Kiểm tra hiểu biết mục 9.5

Một cây cơ bi-a là một thanh gỗ đồng chất có dạng thon dần, với đường kính ở một đầu lớn hơn đường kính ở đầu kia. Hãy sử dụng định lý trục song song để xác định xem cây cơ bi-a có momen quán tính lớn hơn đối với trục quay vuông góc với chiều dài cây cơ khi trục đi qua:

(i) Đầu dày hơn.

(ii) Đầu mỏng hơn.

<details>
<summary>Xem lời giải thích</summary>

**Đáp án đúng là (ii).**

Vì cây cơ có đường kính lớn hơn ở đầu dày, phần lớn khối lượng của cây cơ tập trung lệch về phía đầu này. Do đó, khối tâm của cây cơ nằm gần đầu dày hơn so với đầu mỏng.

Momen quán tính đối với trục quay đi qua một điểm $P$ bất kỳ tại một trong hai đầu được xác định bởi định lý trục song song:

$$
I_P = I_{\mathrm{cm}} + M d^2
$$

Khoảng cách $d$ từ khối tâm đến đầu mỏng lớn hơn khoảng cách từ khối tâm đến đầu dày. Do số hạng $M d^2$ tỷ lệ với bình phương khoảng cách, khoảng cách $d$ lớn hơn sẽ đem lại momen quán tính $I_P$ lớn hơn. Vì vậy, momen quán tính của cây cơ đối với trục quay vuông góc đi qua đầu mỏng sẽ lớn hơn so với trục đi qua đầu dày.
</details>
