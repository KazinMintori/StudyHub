## Bài tập nâng cao 34.104–34.107

::: exercise 34.104
Gương cầu có quang sai cầu vì các tia song song trục nhưng đi xa trục không cùng hội tụ chính xác tại một điểm. Gương paraboloid khắc phục điều đó cho chùm song song trục. Xét tiết diện $y=ax^2$, $a>0$ có đơn vị nghịch đảo độ dài, quay quanh trục $y$ tạo mặt gương. Tia tới song song trục, chạm gương tại $x=r$.

(a) Tìm hệ số góc tiếp tuyến tại điểm tới. (b) Tìm hệ số góc pháp tuyến nét đứt. (c) Tìm góc $\phi$. (d) Dùng lượng giác tìm góc $\alpha$ theo $\phi$. (e) Tìm khoảng $b$ theo $a,r$. Có thể dùng các đồng nhất thức:

$$
\begin{aligned}
\tan(\theta-\pi/2)&=-\cot\theta,\\
\cot(2\theta)&=\frac{\cot^2\theta-1}{2\cot\theta}.
\end{aligned}
$$

(f) Tìm khoảng tiêu điểm $f$ theo $a$ và chứng minh nó không phụ thuộc khoảng tia tới $r$.

![Hình P34.104: Tia song song trục phản xạ tại tiết diện parabol. Tiếp tuyến, pháp tuyến và các góc cho phép xác định tiêu điểm.](img/young-34/hinh-p34-104.png)
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Điểm tới $P=(r,ar^2)$, tia đi từ trên xuống. Tiêu điểm cần tìm trên trục $y$.

**Hướng đi:**

- Đạo hàm của parabol cho hệ số góc tiếp tuyến. Hai đường vuông góc có tích hệ số góc bằng $-1$.
- Định luật phản xạ làm góc lệch của tia phụ thuộc hai lần góc của tiếp tuyến.
- Tìm tung độ giao của tia phản xạ với trục và kiểm tra sự triệt tiêu của $r$.

(a) Hệ số góc tiếp tuyến:

$$
k_t=\left.\frac{dy}{dx}\right|_{x=r}=2ar.
$$

(b) Với $r\ne0$, hệ số góc pháp tuyến:

$$
k_n=-\frac1{2ar}.
$$

(c) Góc giữa tiếp tuyến và phương ngang bằng góc giữa pháp tuyến và phương thẳng đứng:

$$
\phi=\arctan(2ar).
$$

(d) Từ hai góc phản xạ bằng nhau:

$$
\alpha=2\phi-\frac\pi2.
$$

Góc $\alpha$ được dùng có dấu trong phép tính tiếp theo.

(e):

$$
\begin{aligned}
\tan\alpha&=-\cot(2\phi)\\
&=\frac{\tan^2\phi-1}{2\tan\phi}\\
&=\frac{4a^2r^2-1}{4ar},\\
b&=r\tan\alpha\\
&=ar^2-\frac1{4a}.
\end{aligned}
$$

Khi $b$ tính ra âm, đường tia cắt trục phía trên điểm tới. Không ép $b$ luôn dương rồi đổi dấu trong hình học.

(f) Tung độ tiêu điểm:

$$
\begin{aligned}
f&=ar^2-b\\
&=\frac1{4a}.
\end{aligned}
$$

Kết quả không phụ thuộc $r$, nên mọi tia của chùm song song trục đều đi qua cùng tiêu điểm. Tia đúng trên trục là trường hợp giới hạn đối xứng. Kết luận này chính xác cho gương parabol và chùm song song trục, không cần xấp xỉ góc nhỏ.
:::

::: exercise 34.105
(a) Với thấu kính có tiêu cự $f$, tìm khoảng cách nhỏ nhất giữa vật và ảnh thật của nó. (b) Vẽ khoảng vật–ảnh thật theo khoảng vật tới kính. Đồ thị có phù hợp kết quả câu (a) không?
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Xét vật thật và ảnh thật qua kính hội tụ $f>0$, với $s>f$. Khoảng vật–ảnh $D=s+s'$.

**Hướng đi:**

- Loại $s'$ bằng phương trình thấu kính để biểu diễn $D$ theo một biến.
- Dùng đạo hàm tìm điểm cực tiểu trong miền $s>f$.
- Đổi sang biến không thứ nguyên để một đồ thị áp dụng cho mọi $f>0$.

(a):

$$
\begin{aligned}
s'&=\frac{fs}{s-f},\\
D(s)&=s+\frac{fs}{s-f},\\
\frac{dD}{ds}&=1-\frac{f^2}{(s-f)^2}.
\end{aligned}
$$

Điểm dừng trong miền $s>f$ là $s=2f$. Đạo hàm âm khi $f<s<2f$ và dương khi $s>2f$, nên đây là cực tiểu toàn cục:

$$
D_{\min}=4f.
$$

Tại đó $s'=2f$ và phóng đại $m=-1$.

(b) Đặt $u=s/f>1$:

$$
\frac Df=u+\frac{u}{u-1}.
$$

![Đồ thị khoảng vật–ảnh theo khoảng vật, chuẩn hóa bằng tiêu cự. Nhánh có tiệm cận tại s/f bằng1 và đạt cực tiểu tại điểm(2,4).](img/young-34/loi-giai-34-105.svg)

Đồ thị giảm từ vô cực đến điểm $(2,4)$ rồi tăng trở lại, phù hợp phép tính đạo hàm. Điều kiện vật thật là thiết yếu khi viết $D=s+s'$.
:::

::: exercise 34.106
Bút chì dài $16{,}0\,\mathrm{cm}$ nghiêng $45{,}0^\circ$. Tâm bút $C$ cách trục quang $15{,}0\,\mathrm{cm}$ phía trên và cách thấu kính hội tụ $45{,}0\,\mathrm{cm}$ về trái. Kính có tiêu cự $20{,}0\,\mathrm{cm}$. Hai đầu $A,B$ lần lượt là đầu tẩy và đầu nhọn như hình. Hình không theo tỉ lệ. Giả sử áp dụng được mô hình cận trục và kính đủ lớn để thu các chùm tia cần xét.

(a) Tìm vị trí ảnh của $A,B,C$. (b) Tìm chiều dài ảnh, tức khoảng giữa ảnh $A$ và ảnh $B$. (c) Vẽ hình biểu diễn hướng của ảnh.

![Hình P34.106: Bút chì nghiêng, đầu A ở bên trái và thấp hơn đầu B. Điểm C là tâm bút.](img/young-34/hinh-p34-106.png)
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Kính ở $x=0$, chiều dương sang phải. Vật có tâm $C=(-45,15)\,\mathrm{cm}$. Nửa chiều dài bút bằng $8\,\mathrm{cm}$.

**Hướng đi:**

- Tính riêng tọa độ hai đầu vì chúng không ở cùng khoảng vật.
- Mỗi điểm có khoảng ảnh riêng từ phương trình thấu kính và độ cao riêng từ phóng đại.
- Tính khoảng cách Euclid giữa hai ảnh đầu bút, rồi lấy tỉ số độ chênh độ cao và tọa độ để xác định hướng.

Hình chiếu của nửa bút lên mỗi trục:

$$
\delta=\frac8{\sqrt2}=5{,}65685\,\mathrm{cm}.
$$

(a) Với mỗi điểm có tọa độ vật $(-s,y)$:

$$
\begin{aligned}
x'&=\frac{20s}{s-20},\\
y'&=-\frac{x'}s\,y.
\end{aligned}
$$

Kết quả tọa độ ảnh, tính bằng centimet:

| Điểm ảnh | $x'$ | $y'$ |
| --- | --- | --- |
| $A'$ | 33,0477 | −6,09531 |
| $B'$ | 40,6792 | −21,3583 |
| $C'$ | 36,0000 | −12,0000 |

Ở đây $A$ có $s_A=45+\delta$, $y_A=15-\delta$, còn $B$ có $s_B=45-\delta$, $y_B=15+\delta$. Cả ba khoảng ảnh đều dương nên ảnh nằm bên phải kính.

(b):

$$
\begin{aligned}
\Delta x'&=7{,}63151\,\mathrm{cm},\\
\Delta y'&=-15{,}2630\,\mathrm{cm},\\
\ell'&=\sqrt{(\Delta x')^2+(\Delta y')^2}\\
&=17{,}0646\,\mathrm{cm}\\
&\approx17{,}1\,\mathrm{cm}.
\end{aligned}
$$

(c) Hai ảnh đầu bút và ảnh tâm cùng nằm trên đường:

$$
y'=60-2x'.
$$

Ảnh nghiêng xuống phía phải, hợp với chiều dương trục $x$ góc khoảng $-63{,}4^\circ$.

![Ảnh của bút chì được dựng từ ba điểm A′, B′, C′. Ảnh thật nằm dưới trục và nghiêng xuống về bên phải.](img/young-34/loi-giai-34-106.svg)

Ảnh tâm bút không nằm đúng trung điểm đoạn $A'B'$, vì độ phóng đại thay đổi theo vị trí dọc bút. Không dùng một độ phóng đại chung cho cả vật nghiêng.
:::

::: exercise 34.107
Người có mắt bình thường không thể lấy nét dưới nước khi nước tiếp xúc trực tiếp với mắt và không đeo mặt nạ hay kính bơi. (a) Vì sao? (b) Dùng mô hình mắt ở bài 34.52, tìm tiêu cự của kính bổ trợ, đo trong không khí, để người dưới nước nhìn rõ vật ở vô cực.

Kính có chiết suất $1{,}62$, đặt cách mắt $2{,}00\,\mathrm{cm}$ như kính gọng, với nước ở cả hai phía kính. Chú ý tiêu cự trong nước khác trong không khí. Mô hình mắt có môi trường trong chiết suất $1{,}40$, võng mạc cách giác mạc $2{,}60\,\mathrm{cm}$. Bán kính giác mạc được chọn như bài 34.52 để trong không khí mắt nhìn rõ vật cách $40{,}0\,\mathrm{cm}$. Dùng chiết suất nước $1{,}333$.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Giữ nguyên hình học mắt của bài 34.52 khi chuyển từ không khí sang nước. Kính bổ trợ có nước ở hai phía.

**Hướng đi:**

- Công suất mặt giác mạc phụ thuộc độ chênh chiết suất. Nước làm độ chênh này nhỏ đi.
- Tìm bán kính đúng từ bài 34.52, rồi tìm vị trí vật quang học mà giác mạc dưới nước cần nhận để hội tụ lên võng mạc.
- Kính bổ trợ phải tạo ảnh ở vị trí đó. Cuối cùng đổi tiêu cự trong nước sang tiêu cự đo trong không khí bằng công thức chế tạo thấu kính.

(a) Chiết suất nước gần chiết suất môi trường trong mắt hơn không khí. Giác mạc khúc xạ yếu đi, không đủ hội tụ chùm từ vật xa lên võng mạc. Kính bơi giữ một lớp không khí trước giác mạc, còn kính gọng ngập nước không có tác dụng giữ lớp ấy.

(b) Trước hết, từ điều kiện ở bài 34.52:

$$
\begin{aligned}
\frac{0{,}40}{R}&=\frac1{40{,}0}\\
&\quad+\frac{1{,}40}{2{,}60},\\
R&=0{,}709898\,\mathrm{cm}.
\end{aligned}
$$

Gọi $s_e$ là khoảng vật có dấu đối với giác mạc dưới nước:

$$
\begin{aligned}
\frac{1{,}333}{s_e}&=\frac{1{,}40-1{,}333}{R}\\
&\quad-\frac{1{,}40}{2{,}60},\\
s_e&=-3{,}00170\,\mathrm{cm}.
\end{aligned}
$$

Dấu âm cho biết tia vào giác mạc cần đang hội tụ về một điểm sau giác mạc khoảng $3{,}00\,\mathrm{cm}$. Kính cách mắt $2{,}00\,\mathrm{cm}$ về trước nên phải hội tụ chùm song song ở khoảng:

$$
\begin{aligned}
f_w&=2{,}00+3{,}00170\\
&=5{,}00170\,\mathrm{cm}.
\end{aligned}
$$

Gọi $n_g=1{,}62$, $n_w=1{,}333$. Với cùng hai mặt kính:

$$
\begin{aligned}
f_a&=f_w\frac{n_g/n_w-1}{n_g-1}\\
&=5{,}00170\\
&\quad\times\frac{1{,}62/1{,}333-1}{0{,}62}\\
&=+1{,}73691\,\mathrm{cm}\\
&\approx+1{,}74\,\mathrm{cm}.
\end{aligned}
$$

Đây là kính hội tụ với tiêu cự đo trong không khí. Không dùng trực tiếp $5{,}00\,\mathrm{cm}$ làm đáp số mà bỏ qua môi trường nước.
:::
