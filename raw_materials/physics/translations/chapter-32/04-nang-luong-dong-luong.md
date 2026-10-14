## 32.4. Năng lượng và động lượng trong sóng điện từ

Sóng điện từ mang theo năng lượng trong quá trình lan truyền. Ánh sáng Mặt Trời sưởi ấm Trái Đất là minh chứng quen thuộc nhất. Lò vi sóng, đài phát thanh và laser dùng trong phẫu thuật mắt đều hoạt động dựa trên sự truyền tải năng lượng của sóng điện từ. Để tính năng lượng nhận được và công suất truyền, ta cần liên hệ chúng với độ lớn và hướng của các trường.

Từ biểu thức mật độ năng lượng của điện trường và từ trường trong chân không, mật độ năng lượng tổng cộng $u$ tại vùng không gian có điện trường $\vec{E}$ và từ trường $\vec{B}$ được xác định bởi:

$$
\begin{aligned}
u &= \frac{1}{2}\epsilon_0 E^2 + \frac{1}{2\mu_0} B^2
\end{aligned}
\tag{32.23}
$$

Đối với một sóng phẳng chạy lan truyền trong chân không, độ lớn điện trường và từ trường liên hệ với nhau qua tốc độ ánh sáng $c$:

$$
\begin{aligned}
B &= \frac{E}{c} \\
&= \sqrt{\epsilon_0 \mu_0} E
\end{aligned}
\tag{32.24}
$$

Thay hệ thức này vào biểu thức mật độ năng lượng:

$$
\begin{aligned}
u &= \frac{1}{2}\epsilon_0 E^2 \\
&\quad + \frac{1}{2\mu_0} (\sqrt{\epsilon_0 \mu_0} E)^2 \\
&= \frac{1}{2}\epsilon_0 E^2 + \frac{1}{2}\epsilon_0 E^2 \\
&= \epsilon_0 E^2
\end{aligned}
\tag{32.25}
$$

Mặt khác, vì $E = cB = B/\sqrt{\epsilon_0 \mu_0}$, ta cũng có thể viết:

$$
\begin{aligned}
u &= \frac{B^2}{\mu_0}
\end{aligned}
$$

Kết quả này cho thấy một tính chất quan trọng: Đối với một sóng phẳng chạy trong chân không, mật độ năng lượng của thành phần điện trường bằng đúng mật độ năng lượng của thành phần từ trường tại cùng một vị trí: $u_E = u_B = \frac{1}{2}\epsilon_0 E^2 = B^2/(2\mu_0)$. Tuy nhiên, điều này không đúng cho trường điện từ tổng quát hoặc sóng dừng, nơi điện trường và từ trường có thể có biên độ độc lập hoặc lệch pha nhau. Do độ lớn $E$ biến thiên theo vị trí và thời gian, mật độ năng lượng $u$ của sóng điện từ cũng phụ thuộc vào tọa độ không gian và thời gian.

### Dòng năng lượng điện từ và vector Poynting

Một sóng chạy điện từ vận chuyển năng lượng từ vùng không gian này sang vùng không gian khác. Tốc độ truyền năng lượng được mô tả qua công suất truyền qua một đơn vị diện tích vuông góc với phương truyền sóng.

Xét một mặt phẳng cố định vuông góc với trục $x$, trùng với mặt sóng tại một thời điểm xác định. Sau khoảng thời gian $dt$, mặt sóng tiến về phía trước một đoạn $dx = c\,dt$. Xét một phần diện tích $A$ trên mặt phẳng cố định này. Để đến vị trí mới, năng lượng trong khối trụ đáy $A$ và chiều dài $c\,dt$ phải đi xuyên qua diện tích $A$. Do đó, lượng năng lượng chứa trong khối trụ cũng là lượng đã truyền qua mặt trong thời gian $dt$. Thể tích của khối trụ này là $dV = A c\,dt$, và năng lượng điện từ chứa bên trong là:

$$
\begin{aligned}
dU &= u\,dV \\
&= (\epsilon_0 E^2)(A c\,dt)
\end{aligned}
$$

![Hình 32.17: Mặt sóng tại thời điểm dt sau khi đi qua mặt phẳng cố định diện tích A.](../img/young-32/hinh-32-17.png)

Năng lượng truyền qua một đơn vị diện tích trong một đơn vị thời gian trong chân không được ký hiệu là $S$:

$$
\begin{aligned}
S &= \frac{1}{A} \frac{dU}{dt} \\
&= \epsilon_0 c E^2
\end{aligned}
\tag{32.26}
$$

Sử dụng hệ thức $c = 1/\sqrt{\epsilon_0 \mu_0}$ và $B = E/c$, ta biến đổi được các dạng biểu diễn tương đương của $S$ trong chân không:

$$
\begin{aligned}
S &= \frac{EB}{\mu_0} \\
&= \sqrt{\frac{\epsilon_0}{\mu_0}} E^2 \\
&= \frac{c B^2}{\mu_0}
\end{aligned}
\tag{32.27}
$$

Đơn vị SI của $S$ là joule trên giây trên mét vuông ($\mathrm{J/(s\cdot m^2)}$), tương đương watt trên mét vuông ($\mathrm{W/m^2}$).

Để biểu diễn đồng thời cả độ lớn và hướng truyền của dòng năng lượng, nhà vật lý người Anh John Poynting đã đưa ra khái niệm vector Poynting $\vec{S}$:

$$
\begin{aligned}
\vec{S} &= \frac{1}{\mu_0} \vec{E} \times \vec{B}
\end{aligned}
\tag{32.28}
$$

Đối với sóng phẳng lan truyền theo một chiều trong chân không, điện trường $\vec{E}$ và từ trường $\vec{B}$ vuông góc với nhau và vuông góc với phương truyền sóng, do đó tích có hướng $\vec{E} \times \vec{B}$ chỉ đúng theo chiều lan truyền của sóng. Độ lớn của $\vec{S}$ chính là $S = EB/\mu_0$, đặc trưng cho thông lượng năng lượng tức thời trên một đơn vị diện tích vuông góc với tia sóng.

![Hình 32.18: Tấm pin năng lượng mặt trời trên mái nhà đặt nghiêng hướng thẳng về phía Mặt Trời để đón vuông góc vector Poynting.](../img/young-32/hinh-32-18.png)

Công suất thuần $P$ đi ra khỏi một mặt kín bằng tích phân của vector Poynting trên mặt đó. Vector diện tích hướng ra ngoài, nên dòng năng lượng đi vào đóng góp với dấu âm:

$$
\begin{aligned}
P &= \oint \vec{S} \cdot d\vec{A}
\end{aligned}
$$

### Cường độ của sóng điện từ hình sin

Với sóng điện từ hình sin lan truyền theo chiều dương trục $x$ trong chân không:

$$
\begin{aligned}
\vec{E}(x, t) &= \hat{\jmath} E_{\max} \\
&\quad \times \cos(kx - \omega t), \\
\vec{B}(x, t) &= \hat{k} B_{\max} \\
&\quad \times \cos(kx - \omega t)
\end{aligned}
$$

Thay hai biểu thức này vào định nghĩa vector Poynting:

$$
\begin{aligned}
\vec{S}(x, t) &= \frac{1}{\mu_0} \vec{E} \times \vec{B} \\
&= \frac{1}{\mu_0} [\hat{\jmath} E_{\max}] \\
&\quad \times [\hat{k} B_{\max}] \\
&\quad \times \cos^2(kx - \omega t) \\
&= \hat{\imath} \frac{E_{\max} B_{\max}}{\mu_0} \\
&\quad \times \cos^2(kx - \omega t)
\end{aligned}
$$

Vì $\hat{\jmath} \times \hat{k} = \hat{\imath}$ và $\cos^2(kx - \omega t) \ge 0$, vector Poynting $\vec{S}(x, t)$ hướng theo chiều dương trục $x$ khi khác không. Tại các thời điểm hai trường bằng không, vector này cũng bằng không. Đặt góc pha dao động $\Phi = kx - \omega t$, thành phần đại số theo phương $x$ là:

$$
\begin{aligned}
S_x(x, t) &= \frac{E_{\max} B_{\max}}{\mu_0} \\
&\quad \times \cos^2 \Phi \\
&= \frac{E_{\max} B_{\max}}{2\mu_0} \\
&\quad \times [1 + \cos 2\Phi]
\end{aligned}
$$

Cường độ bức xạ $I$ của sóng được định nghĩa là độ lớn của vector Poynting trung bình theo thời gian: $I = |\langle \vec{S} \rangle| = S_{\text{av}}$. Đối với sóng chạy đơn hướng, do giá trị trung bình theo thời gian của hàm $\cos 2\Phi$ bằng không, cường độ sóng là:

$$
\begin{aligned}
I = S_{\text{av}} &= \frac{E_{\max} B_{\max}}{2\mu_0} \\
&= \frac{E_{\max}^2}{2\mu_0 c} \\
&= \frac{1}{2} \sqrt{\frac{\epsilon_0}{\mu_0}} E_{\max}^2 \\
&= \frac{1}{2} \epsilon_0 c E_{\max}^2
\end{aligned}
\tag{32.29}
$$

Như vậy, cường độ sóng hình sin bằng một nửa giá trị cực đại tức thời của vector Poynting. Đối với sóng truyền theo chiều âm trục $x$, vector Poynting hướng dọc theo $-x$, nhưng độ lớn và cường độ trung bình vẫn có dạng giống hệt.

Xét môi trường điện môi tuyến tính, đồng nhất, đẳng hướng, không tán sắc và không tiêu tán năng lượng. Các biểu thức trên được mở rộng bằng cách thay $\epsilon_0$ bằng $\epsilon=K\epsilon_0$ và $\mu_0$ bằng $\mu=K_{\mathrm m}\mu_0$. Đồng thời thay $c$ bằng tốc độ pha $v=1/\sqrt{\epsilon\mu}$ trong môi trường. Khi đó, mật độ năng lượng từ trường là $u_B = B^2/(2\mu)$. Đối với sóng phẳng chạy trong môi trường điện môi lý tưởng này, mật độ năng lượng của điện trường và từ trường vẫn bằng nhau.

::: info Ứng dụng y học: Phẫu thuật laser
Trong những thủ thuật phù hợp, tia laser được dùng như một dao mổ có độ chính xác cao và có thể hạn chế chảy máu. Tia laser có thể tiếp cận và loại bỏ các khối u với tổn hại tối thiểu cho các mô lành lân cận, chẳng hạn như trong ca phẫu thuật não được mô tả ở đây. Công suất phát của chùm laser thường dưới 40 W, nhỏ hơn công suất của một bóng đèn thông thường. Tuy nhiên, công suất này được tập trung vào một vết có đường kính chỉ từ 0,1 mm đến 2,0 mm, do đó cường độ của ánh sáng (bằng giá trị trung bình của vector Poynting) có thể lên tới $5 \times 10^9\,\mathrm{W/m^2}$.
:::

![Ứng dụng 32: Phẫu thuật não bằng chùm tia laser, tập trung năng lượng vào một vết hội tụ cực nhỏ để loại bỏ khối u mà ít gây tổn thương cho mô lành kế cận.](../img/young-32/ung-dung-32-song-trong-chat-lieu.png)

::: warning Phân biệt vector Poynting tức thời và cường độ bức xạ
Tại một điểm bất kỳ trong không gian, độ lớn của vector Poynting biến thiên tuần hoàn theo thời gian. Do đó, tốc độ tức thời mà năng lượng sóng điện từ truyền tới một bề mặt không phải là một hằng số cố định. Mắt người và các thiết bị đo thông thường cảm nhận ánh sáng từ Mặt Trời, bóng đèn hoặc máy quét mã hàng trong cửa hàng như một dòng năng lượng liên tục, ổn định là bởi tần số dao động của sóng ánh sáng rất cao (khoảng $5 \times 10^{14}\,\mathrm{Hz}$ đối với ánh sáng nhìn thấy). Cơ quan thị giác chỉ tiếp nhận giá trị trung bình theo thời gian của dòng năng lượng, tức là cường độ bức xạ $I = |\langle \vec{S} \rangle| = S_{\text{av}}$.
:::

### Dòng động lượng điện từ và áp suất bức xạ

Bên cạnh năng lượng, sóng điện từ còn mang động lượng $p$. Mật độ động lượng, tức động lượng $dp$ chứa trong một đơn vị thể tích $dV$, có độ lớn:

$$
\begin{aligned}
\frac{dp}{dV} &= \frac{EB}{\mu_0 c^2} \\
&= \frac{S}{c^2}
\end{aligned}
\tag{32.30}
$$

Động lượng này là đặc tính nội tại của trường điện từ, không gắn liền với khối lượng nghỉ của các hạt vật chất theo cơ học cổ điển thông thường.

Khi sóng truyền qua một diện tích $A$ trong khoảng thời gian $dt$, thể tích quét qua là $dV = A c\,dt$. Thay thể tích này vào biểu thức trên, ta tìm được tốc độ truyền động lượng trên một đơn vị diện tích:

$$
\begin{aligned}
\frac{1}{A} \frac{dp}{dt} &= \frac{S}{c} \\
&= \frac{EB}{\mu_0 c}
\end{aligned}
\tag{32.31}
$$

Xét sóng tới vuông góc với bề mặt nhận. Theo định luật II Newton, tốc độ truyền động lượng $dp/dt$ cho một bề mặt hấp thụ hoàn toàn chính là lực tác dụng lên bề mặt đó. Lực trung bình tác dụng lên một đơn vị diện tích được gọi là áp suất bức xạ, ký hiệu là $p_{\text{rad}}$. Chỉ số rad phân biệt áp suất với động lượng $p$:

Đối với bề mặt hấp thụ hoàn toàn sóng điện từ:

$$
\begin{aligned}
p_{\text{rad}} &= \frac{S_{\text{av}}}{c} \\
&= \frac{I}{c}
\end{aligned}
\tag{32.32}
$$

Nếu bề mặt phản xạ lý tưởng, sóng bị dội ngược trở lại theo phương cũ. Độ biến thiên động lượng của sóng tăng gấp đôi, kéo theo áp suất bức xạ tác dụng lên bề mặt phản xạ cũng tăng gấp đôi:

$$
\begin{aligned}
p_{\text{rad}} &= \frac{2 S_{\text{av}}}{c} \\
&= \frac{2I}{c}
\end{aligned}
\tag{32.33}
$$

Chẳng hạn, chùm bức xạ Mặt Trời trực tiếp chiếu tới tầng trên của khí quyển Trái Đất có cường độ trung bình vào khoảng $1{,}4\,\mathrm{kW/m^2}$. Áp suất bức xạ tác dụng lên bề mặt hấp thụ hoàn toàn là:

$$
\begin{aligned}
p_{\text{rad}} &= \frac{I}{c} \\
&= \frac{1{,}4 \times 10^3\,\mathrm{W/m^2}}{3{,}00 \times 10^8\,\mathrm{m/s}} \\
&\approx 4{,}7 \times 10^{-6}\,\mathrm{Pa}
\end{aligned}
$$

Với bề mặt phản xạ hoàn toàn, áp suất bức xạ đạt khoảng $9{,}4 \times 10^{-6}\,\mathrm{Pa}$. Áp suất này rất nhỏ, chỉ cỡ $10^{-10}\,\mathrm{atm}$, nhưng hoàn toàn có thể đo đạc chính xác bằng các thiết bị vi cân nhạy cảm.

![Hình 32.20: Cụm sao phát sáng mãnh liệt ở trung tâm đám mây khí liên sao tạo ra áp suất bức xạ và gió hạt thổi dạt vật chất xung quanh, trong khoảng một triệu năm đã khoét rỗng một bong bóng có đường kính 70 năm ánh sáng.](../img/young-32/hinh-32-20.png)

Bên trong các ngôi sao khổng lồ có độ sáng và khối lượng lớn hơn nhiều lần so với Mặt Trời, áp suất bức xạ đạt giá trị khổng lồ, bổ sung đáng kể cho áp suất chất khí để chống lại lực hút hấp dẫn, giữ cho ngôi sao không bị co sụp. Trong môi trường liên sao, áp suất bức xạ từ các cụm sao trẻ mãnh liệt có thể thổi dạt các đám mây bụi khí xung quanh, khoét nên những khoảng trống rộng hàng chục năm ánh sáng.

::: example Ví dụ 32.3: Năng lượng trong sóng phi sin
Xét một sóng điện từ phẳng phi sin lan truyền trong chân không có điện trường đều sau mặt sóng với độ lớn $E = 100\,\mathrm{V/m} = 100\,\mathrm{N/C}$. Hãy xác định độ lớn từ trường $B$, mật độ năng lượng $u$ và tốc độ truyền năng lượng trên một đơn vị diện tích $S$.

**Nhận dạng và chuẩn bị:** Sau mặt sóng, các trường $\vec{E}$ và $\vec{B}$ đều có độ lớn không đổi theo không gian, trong khi phía trước mặt sóng thì hai trường đều triệt tiêu. Sử dụng hệ thức liên hệ biên độ trường trong chân không $B = E/c$, công thức mật độ năng lượng $u = \epsilon_0 E^2$ và định nghĩa độ lớn vector Poynting $S = EB/\mu_0$. Không áp dụng công thức của sóng hình sin vì đây là sóng phi sin.

**Lời giải:**

Từ hệ thức trường:

$$
\begin{aligned}
B &= \frac{E}{c} \\
&= \frac{100\,\mathrm{V/m}}{3{,}00 \times 10^8\,\mathrm{m/s}} \\
&= 3{,}33 \times 10^{-7}\,\mathrm{T}
\end{aligned}
$$

Với $\epsilon_0 = 8{,}85 \times 10^{-12}\,\mathrm{C^2/(N\cdot m^2)}$ và $E = 100\,\mathrm{N/C}$, mật độ năng lượng của trường điện từ sau mặt sóng là:

$$
\begin{aligned}
u &= \epsilon_0 E^2 \\
&= (8{,}85 \times 10^{-12}) \\
&\quad \times (100)^2 \\
&= 8{,}85 \times 10^{-8}\,\mathrm{J/m^3}
\end{aligned}
$$

Với $\mu_0 = 4\pi \times 10^{-7}\,\mathrm{T\cdot m/A}$, độ lớn vector Poynting đặc trưng cho tốc độ truyền năng lượng là:

$$
\begin{aligned}
S &= \frac{EB}{\mu_0} \\
&= \frac{100 \times (3{,}33 \times 10^{-7})}{4\pi \times 10^{-7}} \\
&= 26{,}5\,\mathrm{W/m^2}
\end{aligned}
$$

**Đánh giá:** Ta kiểm tra lại kết quả của $S$ thông qua biểu thức $S = \epsilon_0 c E^2$:

$$
\begin{aligned}
S &= \epsilon_0 c E^2 \\
&= (8{,}85 \times 10^{-12}) \\
&\quad \times (3{,}00 \times 10^8)(100)^2 \\
&= 26{,}5\,\mathrm{W/m^2}
\end{aligned}
$$

Hai cách tính cho kết quả hoàn toàn trùng khớp. Phía trước mặt sóng, điện trường và từ trường đều bằng không nên mật độ năng lượng và vector Poynting tại đó triệt tiêu hoàn toàn. Nơi nào không có trường, nơi đó không tồn tại năng lượng trường.
:::

::: example Ví dụ 32.4: Năng lượng trong sóng hình sin
Một trạm phát thanh trên mặt đất phát sóng hình sin với công suất trung bình tổng cộng $50{,}0\,\mathrm{kW}$. Giả thiết máy phát bức xạ đồng đều về mọi hướng trong nửa không gian phía trên mặt đất. Đây là sự lý tưởng hóa, vì phân bố bức xạ của ăng-ten thực thường phụ thuộc hướng. Hãy tìm biên độ điện trường $E_{\max}$ và biên độ từ trường $B_{\max}$ mà một vệ tinh thu được ở khoảng cách $100\,\mathrm{km}$ tính từ ăng-ten phát.

![Hình 32.19: Đài phát thanh phát sóng vào bán cầu phía trên mặt đất.](../img/young-32/hinh-32-19.png)

**Nhận dạng và chuẩn bị:** Bài toán cho công suất trung bình tổng cộng $P$. Cường độ sóng $I$ là công suất trung bình truyền qua một đơn vị diện tích. Bức xạ phân bố đều trên mặt bán cầu bán kính $R = 100\,\mathrm{km} = 1{,}00 \times 10^5\,\mathrm{m}$. Cường độ $I$ bằng giá trị trung bình $S_{\text{av}}$ của vector Poynting. Từ đó, dùng công thức $I = E_{\max}^2 / (2\mu_0 c)$ để xác định $E_{\max}$, rồi suy ra $B_{\max} = E_{\max}/c$.

**Lời giải:**

Diện tích mặt bán cầu bán kính $R = 1{,}00 \times 10^5\,\mathrm{m}$ là:

$$
\begin{aligned}
A &= 2\pi R^2 \\
&= 2\pi (1{,}00 \times 10^5\,\mathrm{m})^2 \\
&= 6{,}28 \times 10^{10}\,\mathrm{m^2}
\end{aligned}
$$

Toàn bộ công suất bức xạ đi qua diện tích mặt này, do đó cường độ sóng tại vị trí vệ tinh là:

$$
\begin{aligned}
I &= \frac{P}{A} \\
&= \frac{50{,}0 \times 10^3\,\mathrm{W}}{6{,}28 \times 10^{10}\,\mathrm{m^2}} \\
&= 7{,}96 \times 10^{-7}\,\mathrm{W/m^2}
\end{aligned}
$$

Vì $I = S_{\text{av}} = E_{\max}^2 / (2\mu_0 c)$, biên độ điện trường thu được là:

$$
\begin{aligned}
E_{\max} &= \sqrt{2\mu_0 c S_{\text{av}}} \\
&= [2 (4\pi \times 10^{-7}) \\
&\quad \times (3{,}00 \times 10^8) \\
&\quad \times (7{,}96 \times 10^{-7})]^{1/2} \\
&= 2{,}45 \times 10^{-2}\,\mathrm{V/m}
\end{aligned}
$$

Biên độ từ trường tương ứng:

$$
\begin{aligned}
B_{\max} &= \frac{E_{\max}}{c} \\
&= \frac{2{,}45 \times 10^{-2}\,\mathrm{V/m}}{3{,}00 \times 10^8\,\mathrm{m/s}} \\
&= 8{,}17 \times 10^{-11}\,\mathrm{T}
\end{aligned}
$$

**Đánh giá:** Biên độ điện trường $2{,}45 \times 10^{-2}\,\mathrm{V/m}$ nằm trong khoảng đo đạc thông thường của các thiết bị điện tử, nhưng biên độ từ trường $8{,}17 \times 10^{-11}\,\mathrm{T}$ là một giá trị rất bé. Vì vậy, phần lớn các bộ thu sóng vô tuyến trong thực tế được thiết kế để cảm ứng theo thành phần điện trường của sóng, ngoại trừ các ăng-ten vòng thu chuyên dụng bắt tín hiệu từ thông biến thiên.
:::

::: example Ví dụ 32.5: Công suất và áp suất từ ánh sáng Mặt Trời
Một vệ tinh nhân tạo quay quanh Trái Đất mang các tấm pin mặt trời có tổng diện tích $4{,}0\,\mathrm{m^2}$. Giả sử chùm bức xạ Mặt Trời chiếu vuông góc với bề mặt các tấm pin và bị hấp thụ hoàn toàn. Hãy tính công suất bức xạ trung bình mà các tấm pin hấp thụ và độ lớn của lực áp suất bức xạ trung bình tác dụng lên hệ tấm pin.

![Hình 32.21: Tấm pin năng lượng mặt trời trên vệ tinh nhân tạo quay quanh Trái Đất.](../img/young-32/hinh-32-21.png)

**Nhận dạng và chuẩn bị:** Bài toán liên kết giữa cường độ bức xạ, công suất, áp suất bức xạ và lực cơ học. Ngoài tầng khí quyển, cường độ bức xạ Mặt Trời trực tiếp là $I = 1{,}4 \times 10^3\,\mathrm{W/m^2}$. Khi chùm tia chiếu vuông góc và bị hấp thụ hoàn toàn, áp suất bức xạ là $p_{\text{rad}} = I/c$. Lấy các giá trị này nhân với diện tích bề mặt $A = 4{,}0\,\mathrm{m^2}$ để tìm công suất và lực tổng cộng.

**Lời giải:**

Công suất trung bình hấp thụ bởi các tấm pin:

$$
\begin{aligned}
P &= I A \\
&= (1{,}4 \times 10^3\,\mathrm{W/m^2}) \\
&\quad \times (4{,}0\,\mathrm{m^2}) \\
&= 5{,}6 \times 10^3\,\mathrm{W} \\
&= 5{,}6\,\mathrm{kW}
\end{aligned}
$$

Áp suất bức xạ của ánh sáng Mặt Trời lên bề mặt hấp thụ hoàn toàn:

$$
\begin{aligned}
p_{\text{rad}} &= \frac{I}{c} \\
&= \frac{1{,}4 \times 10^3\,\mathrm{W/m^2}}{3{,}00 \times 10^8\,\mathrm{m/s}} \\
&= 4{,}7 \times 10^{-6}\,\mathrm{Pa}
\end{aligned}
$$

Lực áp suất bức xạ tổng cộng tác dụng lên toàn bộ diện tích tấm pin:

$$
\begin{aligned}
F &= p_{\text{rad}} A \\
&= (4{,}7 \times 10^{-6}\,\mathrm{N/m^2}) \\
&\quad \times (4{,}0\,\mathrm{m^2}) \\
&= 1{,}9 \times 10^{-5}\,\mathrm{N}
\end{aligned}
$$

**Đánh giá:** Công suất $5{,}6\,\mathrm{kW}$ hấp thụ được là đáng kể. Một phần chuyển thành điện để vận hành thiết bị trên vệ tinh. Phần còn lại làm nóng tấm pin, trực tiếp hoặc do hiệu suất chuyển đổi quang điện chưa đạt 100%. Ánh sáng Mặt Trời không phải một sóng hình sin đơn, nhưng quan hệ $P=IA$ vẫn áp dụng cho các giá trị trung bình. Ngược lại, lực áp suất bức xạ $1{,}9 \times 10^{-5}\,\mathrm{N}$ chỉ tương đương trọng lượng của một hạt muối nhỏ trên Trái Đất. Dù vậy, khi tác dụng bền bỉ trong nhiều năm tháng trên quỹ đạo không có lực cản khí quyển, lực nhỏ bé này có thể làm biến dạng quỹ đạo vệ tinh và cần được tính đến trong việc hiệu chỉnh quỹ đạo.
:::

### Câu hỏi tự kiểm 32.4

Hình 32.13 mô tả một bước sóng của sóng điện từ hình sin tại thời điểm $t = 0$. Xét bốn tọa độ:

- (i) $x = 0$.
- (ii) $x = \lambda/4$.
- (iii) $x = \lambda/2$.
- (iv) $x = 3\lambda/4$.

Hãy cho biết tại những vị trí nào thì:

(a) Mật độ năng lượng đạt giá trị cực đại?

(b) Mật độ năng lượng đạt giá trị cực tiểu?

(c) Độ lớn tức thời của vector Poynting đạt giá trị cực đại?

(d) Độ lớn tức thời của vector Poynting đạt giá trị cực tiểu?

<details><summary>Xem đáp án và giải thích</summary>

(a) Đáp án là (i) và (iii). Cả mật độ năng lượng $u = \epsilon_0 E^2$ và độ lớn vector Poynting $S = \epsilon_0 c E^2$ đều tỷ lệ thuận với $E^2$. Tại thời điểm $t = 0$, điện trường và từ trường có độ lớn cực đại tại các tọa độ $x = 0$ và $x = \lambda/2$. Chiều của vector không ảnh hưởng đến bình phương độ lớn.

(b) Đáp án là (ii) và (iv). Mật độ năng lượng đạt cực tiểu bằng không tại những điểm mà cả điện trường và từ trường đồng thời triệt tiêu, ứng với các vị trí $x = \lambda/4$ và $x = 3\lambda/4$.

(c) Đáp án là (i) và (iii). Độ lớn tức thời của vector Poynting đạt cực đại tại đúng các vị trí mà độ lớn của điện trường và từ trường đạt giá trị lớn nhất.

(d) Đáp án là (ii) và (iv). Độ lớn tức thời của vector Poynting triệt tiêu tại các vị trí mà điện trường và từ trường bằng không.

</details>
