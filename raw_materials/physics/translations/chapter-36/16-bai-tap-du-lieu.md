## Bài tập dữ liệu 36.62–36.64

::: exercise 36.62
Một bạn học cho rằng bề rộng cực đại trung tâm của nhiễu xạ một khe tỉ lệ nghịch bề rộng khe. Bạn thấy nhận xét này trái trực giác nên đo để kiểm tra. Chiếu laser đơn sắc bước sóng $\lambda$ qua khe rộng a và đo bề rộng w của cực đại trung tâm trên màn cách khe $1{,}50\,\mathrm m$. Bề rộng w được đo giữa hai cực tiểu đầu ở hai phía tâm. Số đo như sau:

| a ($\mu\mathrm m$) | w ($\mathrm m$) |
| --- | --- |
| 0,78 | 2,68 |
| 0,91 | 2,09 |
| 1,04 | 1,73 |
| 1,82 | 0,89 |
| 3,12 | 0,51 |
| 5,20 | 0,30 |
| 7,80 | 0,20 |
| 10,40 | 0,15 |
| 15,60 | 0,10 |

(a) Nếu w tỉ lệ nghịch a thì aw phải không đổi. Vẽ đồ thị aw theo a và giải thích vì sao aw không cố định khi a nhỏ. (b) Dùng đồ thị tìm bước sóng laser. (c) Cực tiểu đầu ở góc nào khi (i) $a=0{,}78\,\mu\mathrm m$, (ii) $a=15{,}60\,\mu\mathrm m$?
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Tất cả chín cặp đo đều cần được dùng. Tính nghịch đảo đơn giản là gần đúng góc nhỏ, trong khi các khe nhỏ nhất tạo bề rộng màn cùng cỡ khoảng màn.

**Hướng đi:**

- Tính từng tích aw và vẽ theo a.
- Dùng $w=2R\tan\theta_1$ với $\sin\theta_1=\lambda/a$ để kiểm tra giới hạn của gần đúng.
- Đọc mức tiệm cận của aw ở a lớn để suy $\lambda\approx aw/(2R)$.

(a) Theo thứ tự tăng của a, các tích aw, tính theo $10^{-6}\,\mathrm{m^2}$, là:

$$
\begin{aligned}
aw&=2{,}0904,\ 1{,}9019,\\
&\quad1{,}7992,\ 1{,}6198,\\
&\quad1{,}5912,\ 1{,}5600,\\
&\quad1{,}5600,\ 1{,}5600,\\
&\quad1{,}5600.
\end{aligned}
$$

![Lời giải 36.62: Đồ thị dùng đủ chín cặp đo, cho thấy tích aw tiến tới một giá trị không đổi ở khe rộng hơn.](img/young-36/loi-giai-36-62.svg)

Đặt $u=\lambda/a$. Giữ hình học màn phẳng cho:

$$
\begin{aligned}
w&=2R\frac{u}{\sqrt{1-u^2}},\\
aw&=\frac{2R\lambda}{\sqrt{1-u^2}}.
\end{aligned}
$$

Khi a lớn so với bước sóng, u nhỏ và mẫu số gần một, nên aw gần không đổi. Khi a giảm, góc cực tiểu lớn, tang không còn gần bằng sin và mẫu số nhỏ đi. Vì vậy, aw tăng ở những khe nhỏ nhất, đúng với số đo.

(b) Bốn điểm a lớn nhất cho mức gần $aw=1{,}56\times10^{-6}\,\mathrm{m^2}$. Suy ra:

$$
\begin{aligned}
\lambda&\approx\frac{1{,}56\times10^{-6}}{2(1{,}50)}\,\mathrm m\\
&=520\,\mathrm{nm}.
\end{aligned}
$$

Các điểm khe nhỏ không bị loại bỏ. Chúng thể hiện chính sự sai khác của mô hình góc nhỏ, còn phần tiệm cận của cùng đồ thị dùng để đọc bước sóng.

(c) Dùng $\theta_1=\arcsin(\lambda/a)$:

- (i) $\theta_1=41{,}8^\circ$.
- (ii) $\theta_1=1{,}91^\circ$.

Hai phía màn có các góc đối dấu. Góc lớn ở trường hợp (i) giải thích vì sao không được áp dụng tính tỉ lệ nghịch đơn giản cho mọi hàng số đo.
:::

::: exercise 36.63
Bạn làm việc ở một công ty chế tạo kim loại và cần đo đường kính D của một lỗ tròn rất nhỏ trên bản kim loại mỏng, thẳng đứng. Chiếu ánh sáng kết hợp đơn sắc bước sóng $562\,\mathrm{nm}$ qua lỗ, đo bán kính r của vòng tối đầu trên màn cách lỗ một khoảng x như Hình 36.26. Bốn phép đo là:

| x ($\mathrm m$) | r ($\mathrm{cm}$) |
| --- | --- |
| 1,00 | 5,6 |
| 1,50 | 8,5 |
| 2,00 | 11,6 |
| 2,50 | 14,1 |

(a) Dùng từng cặp số đo để tính D. Vì có sai số đo, lấy trung bình bốn giá trị D làm kết quả báo cáo. (b) Với $x=1{,}00\,\mathrm m$, các vòng tối thứ hai và thứ ba có bán kính bao nhiêu?
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Phải tính cả bốn giá trị đường kính rồi lấy trung bình như đề yêu cầu, không thay bằng đường hồi quy khác.

**Hướng đi:**

- Dùng $\tan\theta_1=r/x$ và $D=1{,}22\lambda/\sin\theta_1$ cho từng lần đo.
- Lấy trung bình số học của bốn D.
- Dùng các hệ số 2,23 và 3,24 cho vòng tối thứ hai, thứ ba với đường kính trung bình.

(a) Mỗi cặp đo cho:

$$
D_i=\frac{1{,}22\lambda}{\sin[\arctan(r_i/x_i)]}.
$$

Các đường kính, tính theo micromet, lần lượt là:

$$
\begin{aligned}
D_1&=12{,}2628,\\
D_2&=12{,}1189,\\
D_3&=11{,}8412,\\
D_4&=12{,}1761.
\end{aligned}
$$

Khai triển phép trung bình:

$$
\begin{aligned}
\overline D&=\frac{D_1+D_2+D_3+D_4}{4}\\
&=12{,}0997\,\mu\mathrm m\\
&\approx12{,}1\,\mu\mathrm m.
\end{aligned}
$$

(b) Dùng đường kính trung bình vừa báo cáo:

$$
\begin{aligned}
\sin\theta_2&=2{,}23\lambda/\overline D,\\
\sin\theta_3&=3{,}24\lambda/\overline D.
\end{aligned}
$$

Tại khoảng màn $x=1{,}00\,\mathrm m$:

$$
\begin{aligned}
r_2&=x\tan\theta_2\approx10{,}4\,\mathrm{cm},\\
r_3&=x\tan\theta_3\approx15{,}2\,\mathrm{cm}.
\end{aligned}
$$

Các bán kính trên được dự đoán từ mô hình dùng trung bình của cả bốn phép đo, thay vì buộc mô hình đi đúng qua một số đo riêng có sai số.
:::

::: exercise 36.64
Một tấm kính được phủ lớp chắn sáng rất mỏng. Ở giữa lớp phủ có vết xước mảnh rộng $0{,}00125\,\mathrm{mm}$. Nhúng toàn bộ tấm kính vào chất lỏng. Chùm tia đơn sắc kết hợp có bước sóng trong không khí $612\,\mathrm{nm}$ tới vuông góc, truyền qua vết xước. Màn đặt trong chất lỏng, song song tấm kính và cách $30{,}0\,\mathrm{cm}$. Hai vân tối đầu ở hai phía tâm cách nhau $22{,}4\,\mathrm{cm}$. Tìm chiết suất chất lỏng.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Vết xước là khe truyền sáng trong lớp phủ. Bước sóng trong công thức nhiễu xạ là bước sóng trong chất lỏng.

**Hướng đi:**

- Dùng $\theta_1=\arctan[W/(2R)]$ vì bề rộng màn không nhỏ so với khoảng màn.
- Dùng $a\sin\theta_1=\lambda_0/n$ để giải theo n.

$$
\begin{aligned}
u&=\frac{0{,}224}{2(0{,}300)},\\
\theta_1&=\arctan u,\\
n&=\frac{\lambda_0}{a\sin\theta_1}\\
&=1{,}39984\\
&\approx1{,}40.
\end{aligned}
$$

Bước sóng trong chất lỏng tương ứng khoảng $437\,\mathrm{nm}$. Không thay sin của góc bằng tang ở đây, vì hệ vân mở rộng đáng kể trên màn.
:::
