## 36.3. Phân bố cường độ sáng trong hệ vân nhiễu xạ một khe

Ta có thể thiết lập biểu thức định lượng cho sự phân bố cường độ sáng trong hệ vân nhiễu xạ một khe bằng phương pháp cộng giản đồ vectơ pha (phasor addition), tương tự như phương pháp đã áp dụng trong giao thoa hai khe.

![Hình 36.8: Sử dụng giản đồ vectơ pha để tìm biên độ điện trường tổng hợp EP trong nhiễu xạ một khe. Mỗi vectơ pha biểu diễn dao động điện trường phát ra từ một dải hẹp bên trong khe. (a) Sóng phẳng truyền tới khe hẹp có bề rộng a và lan truyền tới điểm P trên màn quan sát ở xa. (b) Tại tâm O của hệ vân (θ = 0), các vectơ pha từ toàn bộ các dải đều cùng pha, tạo nên biên độ cực đại E₀. (c) Tại điểm P lệch khỏi tâm, giữa các dải liền kề xuất hiện độ lệch pha, chuỗi vectơ pha uốn cong thành một đa giác có dây cung là EP và tổng độ lệch pha giữa hai mép khe là β. (d) Trong giới hạn khe được chia thành vô số dải vi phân cực hẹp, đường đa giác trở thành một cung tròn bán kính R = E₀/β.](../img/young-36/hinh-36-08.png)

Xét một mặt sóng phẳng tại khe hẹp có bề rộng $a$. Ta chia bề rộng khe thành một số lượng lớn gồm $N$ dải hẹp song song có bề rộng bằng nhau. Mỗi dải đóng vai trò là một nguồn sóng thứ cấp Huygens phát sóng hình sin tới điểm $P$ trên màn quan sát ở rất xa, hợp với trục trung tâm một góc $\theta$ (Hình 36.8a).

Biên độ điện trường dao động điều hòa phát ra từ mỗi dải được biểu diễn bằng một vectơ pha. Vectơ tổng của toàn bộ các vectơ pha tại điểm $P$ có độ dài chính là biên độ điện trường tổng hợp $E_P$ tại điểm đó. Cường độ sáng $I$ tại $P$ tỷ lệ thuận với bình phương biên độ điện trường: $I \propto E_P^2$.

Tại điểm $O$ trên màn tương ứng với tâm của hệ vân ($\theta = 0$):
- Do khoảng cách từ mọi dải trên khe tới $O$ chênh lệch không đáng kể khi $x \gg a$, các sóng thứ cấp tới $O$ hoàn toàn cùng pha với nhau.
- Các vectơ pha cùng hướng dọc theo một đường thẳng như Hình 36.8b.
- Tổng chiều dài của chuỗi vectơ pha này là biên độ điện trường cực đại tại tâm, ký hiệu là $E_0$.

Tại một điểm $P$ bất kỳ ứng với góc lệch $\theta \neq 0$:
- Do sự khác biệt về đường đi, giữa hai dải liền kề xuất hiện một độ lệch pha nhất định.
- Chuỗi các vectơ pha uốn cong lại thành một đường đa giác như Hình 36.8c.
- Biên độ điện trường tổng hợp $E_P$ chính là độ dài của dây cung nối điểm đầu của vectơ pha thứ nhất với điểm cuối của vectơ pha thứ $N$.
- Góc $\beta$ là tổng độ lệch pha giữa sóng phát ra từ mép trên cùng và sóng phát ra từ mép dưới cùng của khe khi tới điểm $P$.

Trong giới hạn khi số dải $N \to \infty$ và bề rộng mỗi dải tiến về không, chuỗi các vectơ pha trở thành một cung tròn đều liên tục có độ dài cung đúng bằng $E_0$ (Hình 36.8d). Gọi $C$ là tâm của cung tròn và $R$ là bán kính cong:
- Góc ở tâm chắn cung tròn có độ dài $E_0$ đúng bằng góc $\beta$ (tính theo radian), do đó:

$$
\begin{aligned}
E_0 &= R \beta\\
R &= \frac{E_0}{\beta}
\end{aligned}
$$

- Đường phân giác kẻ từ tâm $C$ vuông góc với dây cung $AB = E_P$ sẽ chia góc ở tâm thành hai góc bằng nhau $\beta/2$ và chia đôi dây cung. Từ tam giác vuông, ta có:

$$
\begin{aligned}
\frac{E_P}{2} &= R \sin\frac{\beta}{2}\\
E_P &= 2 R \sin\frac{\beta}{2}\\
&= 2 \left(\frac{E_0}{\beta}\right) \sin\frac{\beta}{2}
\end{aligned}
$$

Rút gọn biểu thức, ta nhận được phương trình cho điện trường tổng hợp tại góc $\theta$:

$$
E_P = E_0 \frac{\sin(\beta/2)}{\beta/2}
\tag{36.4}
$$

Trong đó: Biên độ dao động điện trường thực tế luôn luôn là một đại lượng không âm, bằng độ lớn tuyệt đối $|E_P| = E_0 \left|\frac{\sin(\beta/2)}{\beta/2}\right|$. Biểu thức $E_0 \frac{\sin(\beta/2)}{\beta/2}$ trong phương trình (36.4) đóng vai trò là hệ số biên độ có dấu: Khi đại lượng này mang giá trị âm, điều đó thể hiện pha dao động của sóng điện trường tổng hợp bị lệch thêm một góc $\pi$ radian, trong khi biên độ dao động của sóng luôn mang giá trị không âm.

Vì cường độ sáng tỷ lệ thuận với bình phương biên độ điện trường, gọi $I_0$ là cường độ sáng tại tâm cực đại chính ($\beta = 0$), ta có **hàm phân bố cường độ sáng của nhiễu xạ một khe**:

$$
I = I_0 \left[\frac{\sin(\beta/2)}{\beta/2}\right]^2
\tag{36.5}
$$

Để liên hệ góc pha $\beta$ với góc lệch $\theta$, ta quan sát Hình 36.5: Hiệu đường đi giữa hai tia sáng phát ra từ hai mép ngoài cùng của khe có bề rộng $a$ là $\Delta r = a\sin\theta$. Vì độ lệch pha bằng $\frac{2\pi}{\lambda}$ nhân với hiệu đường đi, ta có:

$$
\beta = \frac{2\pi}{\lambda} a \sin\theta
\tag{36.6}
$$

Thay $\frac{\beta}{2} = \frac{\pi a}{\lambda}\sin\theta$ vào phương trình (36.5), ta thu được biểu thức cường độ sáng theo góc $\theta$:

$$
I = I_0 \left[\frac{\sin\left(\frac{\pi a}{\lambda}\sin\theta\right)}{\frac{\pi a}{\lambda}\sin\theta}\right]^2
\tag{36.7}
$$

![Hình 36.9: Phần (a): Đồ thị phân bố cường độ sáng theo góc lệch θ trong nhiễu xạ một khe. Các giá trị m = ±1, ±2, ±3 đánh dấu vị trí các cực tiểu theo phương trình (36.8). Phần lớn năng lượng tập trung tại đỉnh cực đại trung tâm giữa m = -1 và m = 1. (b) Ảnh chụp sóng nước truyền qua một khe hẹp thể hiện hiện tượng nhiễu xạ tương tự như sóng ánh sáng: Chỉ có các gợn sóng nhiễu xạ nằm trong vùng cực đại trung tâm là quan sát rõ, các sóng ở góc lớn hơn có biên độ quá nhỏ.](../img/young-36/hinh-36-09.png)

### Xác định vị trí các cực tiểu và cực đại cường độ

**1. Vị trí các cực tiểu cường độ (vân tối)**:
Từ phương trình (36.5), cường độ $I = 0$ khi tử số triệt tiêu:

$$
\begin{aligned}
\sin\frac{\beta}{2} &= 0\\
\frac{\beta}{2} &= m\pi\\
\beta &= 2m\pi
\end{aligned}
$$

Trong đó: Giá trị $m = \pm 1, \pm 2, \pm 3, \dots$ là các số nguyên khác không. Kết hợp với phương trình (36.6), ta thu lại điều kiện vân tối quen thuộc:

$$
\begin{aligned}
&\frac{2\pi}{\lambda} a \sin\theta = 2m\pi, \\
&a \sin\theta = m \lambda, \\
&\sin\theta = \frac{m\lambda}{a}.
\end{aligned}
\tag{36.8}
$$

Tại $\beta = 0$ (tức $\theta = 0$), biểu thức có dạng vô định $0/0$. Khử dạng vô định bằng quy tắc giới hạn:

$$
\begin{aligned}
\lim_{\beta \to 0} \frac{\sin(\beta/2)}{\beta/2} &= 1\\
&\implies I = I_0
\end{aligned}
$$

Do đó, $\beta = 0$ tương ứng với đỉnh cực đại trung tâm chứ không phải cực tiểu.

**2. Vị trí các cực đại cường độ phụ**:
Lấy đạo hàm của phương trình (36.5) theo $\beta$ và cho bằng không:

$$
\begin{aligned}
\frac{dI}{d\beta} &= 0\\
&\implies \tan\frac{\beta}{2} = \frac{\beta}{2}
\end{aligned}
$$

Phương trình siêu việt này phải được giải bằng phương pháp số:
- Nghiệm $\beta = 0$ cho cực đại trung tâm chính với $I = I_0$.
- Trên thực tế không có cực đại nào ở gần $\beta = \pm\pi$. Các cực đại phụ đầu tiên ở hai bên của cực đại trung tâm (gần $\beta = \pm 3\pi$) thực tế xuất hiện tại $\beta \approx \pm 2{,}860\pi$. Các cực đại phụ thứ hai (gần $\beta = \pm 5\pi$) thực tế xuất hiện tại $\beta \approx \pm 4{,}918\pi$, và tiếp tục như vậy. Sai số của phương trình xấp xỉ (36.9) sẽ tiến về không trong giới hạn $m$ lớn, tức là đối với các cực đại cường độ ở xa tâm hệ vân.

Vị trí các cực đại phụ gần sát với các số lẻ lần của $\pi$ với $m = 1, 2, 3, \dots$:

$$
\beta \approx \pm (2m + 1)\pi
\tag{36.9}
$$

Thay các giá trị xấp xỉ từ phương trình (36.9) vào phương trình (36.5), ta thu được chuỗi cường độ xấp xỉ của các cực đại phụ:

$$
I_m \approx \frac{I_0}{\left(m + \frac{1}{2}\right)^2 \pi^2}
\tag{36.10}
$$

Trong đó: Đại lượng $I_m$ là cường độ của cực đại phụ thứ $m$, còn $I_0$ là cường độ của cực đại trung tâm. Phương trình (36.10) cho chuỗi giá trị cường độ xấp xỉ là $0{,}0450 I_0$, $0{,}0162 I_0$, $0{,}0083 I_0, \dots$ Các giá trị cường độ thực tế tương ứng của các cực đại phụ là $0{,}0472 I_0$, $0{,}0165 I_0$, $0{,}0083 I_0, \dots$

Cường độ các cực đại phụ giảm đi rất nhanh khi ra xa tâm. Ngay cả cực đại phụ thứ nhất cũng chỉ có cường độ chưa đầy $5\%$ so với cực đại trung tâm.

### Sự phụ thuộc của bề rộng dải cực đại vào tỷ số $a/\lambda$

![Hình 36.10: Hệ vân nhiễu xạ một khe phụ thuộc chặt chẽ vào tỷ số giữa bề rộng khe a và bước sóng λ. (a) Khi a = λ, cực đại trung tâm mở rộng tới 180°, không xuất hiện vân tối nào trên màn. (b) Khi a = 5λ, đỉnh trung tâm hẹp lại và xuất hiện các cực tiểu đầu tiên tại ±11,5°. (c) Khi a = 8λ, hệ vân trở nên rất sắc nét và tập trung trong góc hẹp.](../img/young-36/hinh-36-10.png)

Trong xấp xỉ góc nhỏ, vị trí góc của cực tiểu đầu tiên ($\beta/2 = \pi$) là:

$$
\theta_1 = \frac{\lambda}{a}
\tag{36.11}
$$

Độ mở góc của dải sáng cực đại trung tâm ($2\theta_1 = 2\lambda/a$) tỷ lệ nghịch với bề rộng của khe:
- Khi bề rộng khe $a$ lớn hơn rất nhiều so với bước sóng $\lambda$ ($a \gg \lambda$): Góc $\theta_1 \approx 0$, chùm tia hầu như không bị loe rộng, sự truyền sáng tuân theo các định luật của quang hình học.
- Khi bề rộng khe $a$ bằng bước sóng $\lambda$ ($a = \lambda$): Ta có $\sin\theta_1 = \lambda/a = 1$, tương ứng góc $\theta_1 = 90^\circ$ nằm tiếp tuyến ngay trên mặt phẳng của khe, do đó không xuất hiện bất kỳ cực tiểu hữu hạn nào trên màn quan sát phía trước.
- Khi bề rộng khe $a$ nhỏ hơn bước sóng $\lambda$ ($a < \lambda$): Ta có $\sin\theta_1 = \lambda/a > 1$. Vì hàm sin không thể vượt quá 1, hoàn toàn không tồn tại góc $\theta$ thực nào thỏa mãn điều kiện cực tiểu.
- Do đó: Trong cả hai trường hợp $a \le \lambda$, dải sáng cực đại trung tâm lan tỏa ra toàn bộ góc $180^\circ$ phía sau khe và trên màn quan sát phía trước không hề xuất hiện hệ vân tối nào.

### Ứng dụng thực tế: Nhiễu xạ của sóng âm trong đời sống

Sóng âm trong tiếng nói con người có bước sóng cỡ $1\,\mathrm{m}$ hoặc lớn hơn. Một cánh cửa ra vào thông thường có bề rộng dưới $1\,\mathrm{m}$, dẫn tới điều kiện $a < \lambda$. Do đó, sóng âm truyền qua cửa mở sẽ bị nhiễu xạ lan rộng ra toàn bộ không gian phía sau, giúp người đứng khuất quanh góc tường vẫn có thể nghe rõ âm thanh.

![Hình 36.11: Sóng âm dùng trong tiếng nói có bước sóng dài (khoảng 1 m) nên dễ dàng bị nhiễu xạ uốn cong quanh đầu của người giảng viên. Trái lại, sóng ánh sáng có bước sóng cực ngắn nên hầu như không bị nhiễu xạ quanh vật cản lớn. Vì vậy ta có thể nghe thấy tiếng giảng viên khi người đó quay mặt vào bảng đen, nhưng không thể nhìn xuyên qua đầu người đó.](../img/young-36/hinh-36-11.png)

Hiện tượng tương tự xảy ra khi giảng viên quay mặt vào bảng đen giảng bài (Hình 36.11): Sóng âm dễ dàng nhiễu xạ vòng qua đầu giảng viên để truyền tới tai sinh viên trong lớp học. Trái lại, mắt thường không thể nhìn xuyên qua đầu giảng viên vì ánh sáng nhìn thấy có bước sóng chỉ khoảng $5 \times 10^{-7}\,\mathrm{m}$, quá nhỏ so với kích thước đầu người để tạo ra góc nhiễu xạ quan sát được.

### Ví dụ 36.2: Xác định cường độ sáng và bề rộng khe từ độ lệch pha

(a) Cường độ sáng tại tâm hệ vân nhiễu xạ một khe là $I_0$. Xác định cường độ sáng tại điểm trên hệ vân nơi sóng thứ cấp từ hai mép khe có độ lệch pha là $66\,\mathrm{rad}$.

(b) Nếu điểm này nằm cách cực đại trung tâm một góc $7{,}0^\circ$, bề rộng khe gấp bao nhiêu lần bước sóng?

**Nhận dạng bài toán**:
Bài toán cho biết độ lệch pha $\beta$ giữa hai sóng phát ra từ hai mép khe, yêu cầu tính cường độ sáng $I$ theo $I_0$, sau đó từ góc lệch $\theta$ tìm tỷ số giữa bề rộng khe $a$ và bước sóng $\lambda$.

**Chuẩn bị**:
- Phần (a): Cho $\beta = 66\,\mathrm{rad} \implies \beta/2 = 33\,\mathrm{rad}$. Áp dụng phương trình (36.5) để tìm $I$.
- Phần (b): Cho $\theta = 7{,}0^\circ$ và $\beta = 66\,\mathrm{rad}$. Áp dụng phương trình (36.6) để tìm tỷ số $a/\lambda$.

**Thực hiện**:
(a) Tính giá trị hàm tại $\beta/2 = 33\,\mathrm{rad}$:

$$
\frac{\beta}{2} = 33\,\mathrm{rad}
$$

Thay vào phương trình (36.5):

$$
\begin{aligned}
I &= I_0 \left[\frac{\sin(33\,\mathrm{rad})}{33\,\mathrm{rad}}\right]^2\\
&= I_0 \left(\frac{0{,}9999}{33}\right)^2\\
&= 9{,}2 \times 10^{-4} I_0
\end{aligned}
$$

(b) Từ phương trình (36.6), ta biến đổi để tìm tỷ số $a/\lambda$:

$$
\begin{aligned}
\frac{a}{\lambda} &= \frac{\beta}{2\pi \sin\theta}\\
&= \frac{66\,\mathrm{rad}}{(2\pi\,\mathrm{rad})\sin 7{,}0^\circ}\\
&= \frac{66}{2\pi \times 0{,}12187}\\
&\approx 86
\end{aligned}
$$

Nếu dùng ánh sáng có bước sóng $\lambda = 550\,\mathrm{nm}$, bề rộng khe tương ứng là:

$$
\begin{aligned}
a &= 86 \times (550 \times 10^{-9}\,\mathrm{m})\\
&= 4{,}7 \times 10^{-5}\,\mathrm{m}\\
&= 0{,}047\,\mathrm{mm}
\end{aligned}
$$

Giá trị này xấp xỉ bằng $\frac{1}{20}\,\mathrm{mm}$.

**Đánh giá**:
Câu hỏi: Giá trị $\beta = 66\,\mathrm{rad}$ này tương ứng với điểm nào trong hệ vân nhiễu xạ?

<details><summary>Xem phân tích</summary>

Để xác định, ta nhận thấy giá trị $\beta = 66\,\mathrm{rad}$ xấp xỉ bằng $21\pi$. Đây là một bội số lẻ của $\pi$, có dạng $(2m + 1)\pi$ như trong phương trình (36.9) xác định các cực đại cường độ. Vì $21 = 2 \times 10 + 1$, giá trị $\beta = 66\,\mathrm{rad}$ tương ứng với một điểm nằm rất gần cực đại phụ thứ mười ($m = 10$). Vị trí này nằm xa ngoài phạm vi hiển thị của đồ thị Hình 36.9a (vốn chỉ vẽ các cực đại phụ tới $m = \pm 3$).

</details>

**Ý nghĩa vật lý**:
Cường độ sáng tại một điểm trong hệ vân nhiễu xạ phụ thuộc trực tiếp vào độ lệch pha $\beta$ giữa các sóng thứ cấp đến từ hai mép khe. Cường độ đạt giá trị lớn nhất tại tâm ($\beta = 0$) và triệt tiêu tại các điểm có $\beta = \pm 2\pi, \pm 4\pi, \pm 6\pi, \dots$

### Ví dụ 36.3: Tính cường độ sáng tại một điểm trên màn quan sát

Trong thí nghiệm ở Ví dụ 36.1, cường độ sáng tại tâm hệ vân là $I_0$. Xác định cường độ sáng tại một điểm trên màn cách tâm hệ vân $3{,}0\,\mathrm{mm}$.

**Nhận dạng bài toán**:
Bài toán yêu cầu tính cường độ sáng $I$ tại một vị trí $y$ cụ thể trên màn quan sát, dựa trên các thông số đã biết từ Ví dụ 36.1.

**Chuẩn bị**:
- Từ Ví dụ 36.1: Bề rộng khe $a = 2{,}4 \times 10^{-4}\,\mathrm{m}$, bước sóng $\lambda = 633\,\mathrm{nm} = 6{,}33 \times 10^{-7}\,\mathrm{m}$, khoảng cách tới màn $x = 6{,}0\,\mathrm{m}$.
- Tọa độ điểm quan sát trên màn: $y = 3{,}0\,\mathrm{mm} = 3{,}0 \times 10^{-3}\,\mathrm{m}$.
- Ta tính góc $\theta$ qua hình học: $\tan\theta = y/x$, sau đó áp dụng phương trình (36.7) để tính cường độ sáng $I$.

**Thực hiện**:
Góc nghiêng $\theta$ thỏa mãn:

$$
\begin{aligned}
\tan\theta &= \frac{y}{x}\\
&= \frac{3{,}0 \times 10^{-3}\,\mathrm{m}}{6{,}0\,\mathrm{m}}\\
&= 5{,}0 \times 10^{-4}
\end{aligned}
$$

Vì $\tan\theta$ rất nhỏ, ta có $\sin\theta \approx \tan\theta = 5{,}0 \times 10^{-4}$. Tính đại lượng $\beta/2$:

$$
\begin{aligned}
\frac{\beta}{2} &= \frac{\pi a \sin\theta}{\lambda}\\
&=\frac{\pi(2{,}4)(5{,}0)}{6{,}33}\times10^{-1}\\
&= 0{,}5955\\
&\approx 0{,}60\,\mathrm{rad}
\end{aligned}
$$

Thay vào phương trình tính cường độ (36.7):

$$
\begin{aligned}
I &= I_0 \left(\frac{\sin 0{,}60}{0{,}60}\right)^2\\
&= I_0 \left(\frac{0{,}5646}{0{,}60}\right)^2\\
&= 0{,}8856 I_0\\
&\approx 0{,}89 I_0
\end{aligned}
$$

**Đánh giá**:
Cường độ đạt mức cao tới $89\%$ so với $I_0$ chỉ có thể xảy ra bên trong dải sáng cực đại trung tâm. Kết quả này hoàn toàn khớp với thực tế: Ở Ví dụ 36.1, vân tối thứ nhất nằm cách tâm một khoảng $y_1 = 16\,\mathrm{mm}$, do đó điểm đang xét tại $y = 3{,}0\,\mathrm{mm}$ chắc chắn nằm sâu bên trong dải sáng cực đại trung tâm.

**Ý nghĩa vật lý**:
Khi ánh sáng truyền qua một khe hẹp, cường độ sáng tại góc lệch $\theta$ được xác định thông qua đại lượng $\frac{\pi a}{\lambda}\sin\theta$ (chính là một nửa độ lệch pha $\beta$). Cường độ cực đại tại tâm và giảm dần về không khi $\frac{\pi a}{\lambda}\sin\theta$ tiến tới $\pm \pi$.

### Câu hỏi tự kiểm tra 36.3

Bức xạ điện từ kết hợp truyền qua khe rộng $0{,}0100\,\mathrm{mm}$. Những bước sóng nào sau đây không cho điểm có cường độ bằng không trong hệ vân nhiễu xạ?

- (i) Ánh sáng lam bước sóng $500\,\mathrm{nm}$.
- (ii) Hồng ngoại bước sóng $10{,}6\,\mu\mathrm m$.
- (iii) Vi ba bước sóng $1{,}00\,\mathrm{mm}$.
- (iv) Tử ngoại bước sóng $50{,}0\,\mathrm{nm}$.

<details><summary>Xem đáp án và giải thích</summary>

Chọn (ii) và (iii). Khe rộng $10{,}0\,\mu\mathrm m$. Cực tiểu đầu đòi hỏi $\sin\theta=\lambda/a$, nên không có cực tiểu nếu $\lambda>a$.

Các tỉ số bước sóng với bề rộng khe lần lượt là:

$$
\begin{aligned}
(\lambda/a)_{\rm i}&=0{,}0500,\\
(\lambda/a)_{\rm ii}&=1{,}06,\\
(\lambda/a)_{\rm iii}&=100,\\
(\lambda/a)_{\rm iv}&=0{,}00500.
\end{aligned}
$$

Hai trường hợp (ii), (iii) đòi hỏi sin lớn hơn một, nên không có hướng cực tiểu. Hai trường hợp (i), (iv) có bước sóng nhỏ hơn bề rộng khe và có các cực tiểu. Ở đây không có lựa chọn nào bằng đúng bề rộng khe.

</details>
