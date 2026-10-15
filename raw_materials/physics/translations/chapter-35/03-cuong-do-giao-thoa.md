## 35.3. Cường độ trong các hệ vân giao thoa

Ở mục 35.2, chúng ta đã xác định được vị trí của các cực đại (vân sáng) và cực tiểu (vân tối) trong hệ vân giao thoa hai khe. Bây giờ, mục tiêu của bài học này là tìm biểu thức định lượng xác định cường độ ánh sáng tại mọi điểm bất kỳ trên màn quan sát.

### Giản đồ vectơ pha cho hai nguồn sóng

Để tính cường độ ánh sáng, trước hết ta phải xác định trường điện từ tổng hợp tại điểm quan sát $P$. Giả sử hai sóng ánh sáng phát ra từ hai khe có cùng phương phân cực dọc theo trục $y$, cùng tần số góc $\omega$, và cùng biên độ điện trường $E$. Khoảng cách từ hai khe tới điểm quan sát $P$ rất lớn so với khoảng cách giữa hai khe, do đó biên độ của hai sóng khi tới $P$ xấp xỉ bằng nhau.

Điện trường tức thời do từng khe tạo ra tại điểm $P$ có thể viết dưới dạng:

$$
\begin{aligned}
E_1(t) &= E \cos(\omega t + \phi)
\end{aligned}
$$

$$
\begin{aligned}
E_2(t) &= E \cos \omega t
\end{aligned}
$$

Trong đó: Ký hiệu $\phi$ là độ lệch pha giữa hai sóng khi truyền tới điểm $P$.

Để tìm điện trường tổng hợp $E_P(t) = E_1(t) + E_2(t)$, ta áp dụng phương pháp giản đồ vectơ pha (phasor diagram), như biểu diễn ở Hình 35.9.

![Hình 35.9: Giản đồ vectơ pha cho sự chồng chập tại điểm P của hai sóng có cùng biên độ E và lệch pha nhau một góc φ. Toàn bộ hệ vectơ pha quay ngược chiều kim đồng hồ với tốc độ góc ω. Sóng tổng hợp có biên độ EP phụ thuộc vào góc lệch pha φ giữa hai sóng thành phần.](../img/young-35/hinh-35-09.png)

Mỗi dao động điều hòa được biểu diễn bằng một vectơ quay (vectơ pha) có độ dài bằng biên độ $E$. Hai vectơ pha này quay ngược chiều kim đồng hồ quanh gốc tọa độ $O$ với cùng tốc độ góc $\omega$. Góc hợp giữa hai vectơ pha bằng đúng độ lệch pha $\phi$.

Hình chiếu của từng vectơ pha lên trục ngang cho điện trường tức thời của sóng tương ứng. Tổng hai hình chiếu cho trường tức thời tổng hợp. Vectơ tổng hợp có độ dài bằng biên độ tổng hợp $E_P$. Xét tam giác tạo bởi hai vectơ pha và vectơ tổng hợp, góc đối diện với cạnh $E_P$ là $\pi - \phi$. Theo định lý hàm số cosin trong tam giác:

$$
\begin{aligned}
E_P^2 &= E^2 + E^2 \\
&\quad - 2 E^2 \cos(\pi - \phi) \\
&= 2 E^2 (1 + \cos \phi)
\end{aligned}
$$

Áp dụng công thức lượng giác hạ bậc $1 + \cos\phi = 2\cos^2(\phi/2)$, ta thu được biểu thức bình phương biên độ điện trường tổng hợp:

$$
\begin{aligned}
E_P^2 &= 4 E^2 \cos^2\frac{\phi}{2}
\end{aligned}
$$

Lấy căn bậc hai, biên độ của điện trường tổng hợp tại điểm $P$ là:

$$
\begin{aligned}
E_P &= 2 E \left|\cos\frac{\phi}{2}\right|
\end{aligned}
\tag{35.7}
$$

### Biểu thức cường độ ánh sáng

Cường độ ánh sáng $I$ là mật độ thông lượng năng lượng trung bình theo thời gian của sóng điện từ, được xác định qua vectơ Poynting trung bình $S_\text{av}$:

$$
\begin{aligned}
I &= S_{\rm av}\\
&=\frac{E_P^2}{2\mu_0c}\\
&=\frac12\sqrt{\frac{\epsilon_0}{\mu_0}}E_P^2\\
&=\frac12\epsilon_0cE_P^2
\end{aligned}
\tag{35.8}
$$

Thay biểu thức $E_P^2$ từ phương trình (35.7) vào phương trình (35.8):

$$
\begin{aligned}
I &= 2 \epsilon_0 c E^2 \cos^2\frac{\phi}{2}
\end{aligned}
\tag{35.9}
$$

Khi hai sóng tới cùng pha ($\phi = 0, \pm 2\pi, \pm 4\pi, \dots$), hàm cosin đạt độ lớn bằng $1$, và cường độ đạt giá trị cực đại $I_0$:

$$
\begin{aligned}
I_0 &= 2 \epsilon_0 c E^2
\end{aligned}
$$

Nhận xét: Cường độ của sóng do một nguồn đơn lẻ phát ra truyền tới $P$ là $I_1 = \frac{1}{2}\epsilon_0 c E^2$. Như vậy, cực đại giao thoa có cường độ $I_0 = 4 I_1$, lớn gấp bốn lần cường độ của từng nguồn riêng lẻ.

Thay $I_0$ vào phương trình (35.9), ta thu được công thức tổng quát xác định cường độ ánh sáng theo độ lệch pha:

$$
\begin{aligned}
I &= I_0 \cos^2\frac{\phi}{2}
\end{aligned}
\tag{35.10}
$$

### Liên hệ giữa độ lệch pha và hiệu đường đi

Độ lệch pha $\phi$ giữa hai sóng xuất phát cùng pha tỉ lệ thuận với hiệu khoảng cách truyền sóng $r_2 - r_1$. Một bước sóng $\lambda$ tương ứng với góc pha $2\pi\,\mathrm{rad}$. Do đó ta có tỉ lệ:

$$
\begin{aligned}
\frac{\phi}{2\pi} &= \frac{r_2 - r_1}{\lambda}
\end{aligned}
$$

Suy ra biểu thức của độ lệch pha:

$$
\begin{aligned}
\phi &= \frac{2\pi}{\lambda} (r_2 - r_1) \\
&= k (r_2 - r_1)
\end{aligned}
\tag{35.11}
$$

Trong đó: Đại lượng $k = \frac{2\pi}{\lambda}$ là **số sóng** (wave number).

Nếu sóng ánh sáng truyền trong một môi trường trong suốt có chiết suất $n$, bước sóng $\lambda$ và số sóng $k$ trong môi trường liên hệ với các giá trị trong chân không $\lambda_0$ và $k_0$ bởi:

$$
\begin{aligned}
\lambda &= \frac{\lambda_0}{n} \\
k &= n k_0
\end{aligned}
\tag{35.12}
$$

Khi điểm $P$ nằm ở khoảng cách rất xa hai khe so với khoảng cách giữa hai khe ($R \gg d$), theo phương trình (35.3) hiệu đường đi là $r_2 - r_1 = d\sin\theta$. Khi đó độ lệch pha trở thành:

$$
\begin{aligned}
\phi &= k d \sin \theta \\
&= \frac{2\pi d}{\lambda} \sin \theta
\end{aligned}
\tag{35.13}
$$

Thay phương trình (35.13) vào phương trình (35.10), ta thu được biểu thức cường độ ánh sáng phụ thuộc vào góc lệch $\theta$:

$$
\begin{aligned}
I &= I_0 \cos^2\left(\frac{1}{2} k d \sin \theta\right) \\
&= I_0 \cos^2\left(\frac{\pi d}{\lambda} \sin \theta\right)
\end{aligned}
\tag{35.14}
$$

Cường độ đạt cực đại $I = I_0$ khi biểu thức trong dấu cosin bằng $m\pi$, tức là $\frac{\pi d}{\lambda}\sin\theta = m\pi \implies d\sin\theta = m\lambda$. Kết quả này hoàn toàn trùng khớp với điều kiện vân sáng ở phương trình (35.4).

Trái lại, cường độ triệt tiêu bằng không khi biểu thức trong dấu cosin bằng $\left(m + \frac{1}{2}\right)\pi$, tức là $d\sin\theta = \left(m + \frac{1}{2}\right)\lambda$, đúng với điều kiện vân tối ở phương trình (35.5).

Trên màn quan sát phẳng ở góc nhỏ, ta áp dụng gần đúng $\sin\theta \approx \frac{y}{R}$. Thay vào phương trình (35.14), ta được phân bố cường độ theo tọa độ $y$ trên màn:

$$
\begin{aligned}
I &= I_0 \cos^2\left(\frac{k d y}{2 R}\right) \\
&= I_0 \cos^2\left(\frac{\pi d y}{\lambda R}\right)
\end{aligned}
\tag{35.15}
$$

![Hình 35.10: Đồ thị phân bố cường độ trong hệ vân giao thoa từ hai khe hẹp giống nhau theo công thức (35.15). Trục hoành biểu diễn đồng thời tọa độ y trên màn, hiệu đường đi d sin θ, và độ lệch pha φ. Các đỉnh cực đại có cường độ bằng I 0 xuất hiện khi φ là bội số chẵn của π. Các cực tiểu có cường độ bằng không xuất hiện khi φ là bội số lẻ của π.](../img/young-35/hinh-35-10.png)

Đồ thị ở Hình 35.10 biểu diễn hàm $\cos^2$. Các vân sáng có bề rộng đều đặn, cường độ giảm trơn từ cực đại về không tại các vân tối. Toàn bộ các đỉnh cực đại đều có cùng cường độ $I_0$ nếu ta coi hai khe là nguồn điểm lý tưởng.

Trong ảnh chụp Hình 35.6, các vân ngoài yếu hơn vân giữa, trong khi mô hình Hình 35.10 cho các đỉnh bằng nhau. Nguyên nhân là mỗi khe có bề rộng hữu hạn, nên còn xuất hiện bao nhiễu xạ. Phần này được xét ở chương kế tiếp.

Giá trị trung bình của $\cos^2(\phi/2)$ qua một chu kỳ pha là $1/2$. Vì vậy, cường độ trung bình trên nhiều vân bằng $I_0/2$, tức tổng cường độ của hai chùm khi xét riêng. Những vân sáng nhận thêm đúng phần năng lượng giảm ở vùng khác, phù hợp bảo toàn năng lượng.

Nếu hai nguồn có độ lệch pha ban đầu $\phi_0$, ta cộng pha ấy vào phần pha do truyền:

$$
\phi=\frac{2\pi\Delta r}{\lambda}+\phi_0.
$$

### Ví dụ 35.3: Hệ anten phát sóng định hướng

Xét hai anten vô tuyến giống hệt nhau ở Ví dụ 35.2 nhưng khoảng cách giữa chúng được giảm xuống còn $d = 10{,}0\,\mathrm{m}$. Tần số phát sóng được tăng lên $f = 60{,}0\,\mathrm{MHz}$. Ở khoảng cách $700\,\mathrm{m}$ tính từ trung điểm hai anten theo hướng chính diện $\theta = 0^\circ$, cường độ đo được là $I_0 = 0{,}020\,\mathrm{W/m^2}$. Ở cùng khoảng cách $700\,\mathrm{m}$ đó, hãy xác định:

(a) Cường độ theo hướng $\theta = 4{,}0^\circ$.

(b) Hướng gần $\theta = 0^\circ$ nhất mà tại đó cường độ giảm còn một nửa giá trị cực đại ($I = I_0/2$).

(c) Các hướng mà cường độ sóng hoàn toàn triệt tiêu ($I = 0$).

**Nhận dạng bài toán**: Bài toán yêu cầu tính cường độ sóng vô tuyến phụ thuộc vào góc phương vị $\theta$ tại vùng trường xa ($700\,\mathrm{m} \gg 10{,}0\,\mathrm{m}$).

**Chuẩn bị**: Vì khoảng cách quan sát $700\,\mathrm{m}$ lớn hơn rất nhiều so với khoảng cách giữa hai anten $d = 10{,}0\,\mathrm{m}$, biên độ sóng truyền từ hai anten tới máy thu thực tế bằng nhau. Ta có thể áp dụng phương trình (35.14) để tính cường độ.

**Thực hiện**:

Bước sóng bức xạ của anten là:

$$
\begin{aligned}
\lambda &= \frac{c}{f} \\
&= \frac{3{,}00 \times 10^8\,\mathrm{m/s}}{60{,}0 \times 10^6\,\mathrm{Hz}} \\
&= 5{,}00\,\mathrm{m}
\end{aligned}
$$

Khoảng cách giữa hai anten là $d = 10{,}0\,\mathrm{m}$, gấp đúng hai lần bước sóng:

$$
\begin{aligned}
\frac{d}{\lambda} &= \frac{10{,}0\,\mathrm{m}}{5{,}00\,\mathrm{m}} \\
&= 2{,}00
\end{aligned}
$$

Khi đó phương trình cường độ (35.14) trở thành:

$$
\begin{aligned}
I &= I_0 \cos^2\left(\frac{\pi d}{\lambda} \sin \theta\right)
\end{aligned}
$$

Với $d/\lambda = 2{,}00$, hàm cường độ trở thành:

$$
\begin{aligned}
I &= I_0 \\
&\quad \times \cos^2[(2{,}00\pi\,\mathrm{rad}) \sin \theta]
\end{aligned}
$$

(a) Khi $\theta = 4{,}0^\circ$:

$$
\begin{aligned}
\sin 4{,}0^\circ &\approx 0{,}06976
\end{aligned}
$$

Góc pha trong hàm cosin là:

$$
\begin{aligned}
\phi_0 &= 2{,}00\pi \sin 4{,}0^\circ \\
&\approx 0{,}4383\,\mathrm{rad}
\end{aligned}
$$

Thay vào biểu thức cường độ:

$$
\begin{aligned}
I &= I_0 \cos^2(0{,}4383\,\mathrm{rad}) \\
&\approx 0{,}82 I_0
\end{aligned}
$$

Thay số $I_0 = 0{,}020\,\mathrm{W/m^2}$:

$$
\begin{aligned}
I &= (0{,}82)(0{,}020\,\mathrm{W/m^2}) \\
&\approx 0{,}016\,\mathrm{W/m^2}
\end{aligned}
$$

(b) Cường độ $I = I_0/2$ khi hàm cosin nhận giá trị $\pm \frac{1}{\sqrt{2}}$. Góc nhỏ nhất thỏa mãn điều kiện này tương ứng với:

$$
\begin{aligned}
(2{,}00\pi\,\mathrm{rad}) \sin \theta &= \pm \frac{\pi}{4}\,\mathrm{rad}
\end{aligned}
$$

Suy ra:

$$
\begin{aligned}
\sin \theta &= \pm \frac{1}{8{,}00} \\
&= \pm 0{,}125
\end{aligned}
$$

Lấy hàm sin ngược, ta tìm được các góc:

$$
\begin{aligned}
\theta &= \pm 7{,}2^\circ
\end{aligned}
$$

(c) Cường độ hoàn toàn triệt tiêu ($I = 0$) khi biểu thức trong hàm cosin bằng một số bán nguyên lần của $\pi$:

$$
\begin{aligned}
2{,}00\pi \sin \theta &= \pm \frac{\pi}{2}, \\
&\quad \pm \frac{3\pi}{2}, \dots
\end{aligned}
$$

Chia cả hai vế cho $2{,}00\pi$:

$$
\begin{aligned}
\sin \theta &= \pm 0{,}250, \\
&\quad \pm 0{,}750, \dots
\end{aligned}
$$

Vì giá trị của hàm sin không thể vượt quá $1$, các nghiệm lớn hơn $1$ không có ý nghĩa vật lý. Ta nhận được hai cặp góc triệt tiêu:
- Với $\sin\theta = \pm 0{,}250$: Ta có $\theta = \pm 14{,}5^\circ$.
- Với $\sin\theta = \pm 0{,}750$: Ta có $\theta = \pm 48{,}6^\circ$.

**Đánh giá**: Ngoài hai hướng gần tâm nhất, còn có các hướng khác cho cường độ bằng nửa cực đại. Bạn có thể tự xác định và kiểm tra những góc ấy không?

<details><summary>Xem các góc bổ sung và kiểm tra</summary>

Điều kiện ở câu (b) để $I = I_0/2$, tức là $(2{,}00\pi\,\mathrm{rad})\sin\theta = \pm \frac{\pi}{4}\,\mathrm{rad}$, trên thực tế còn được thỏa mãn bởi các nghiệm khác của phương trình lượng giác:

$$
\begin{aligned}
2{,}00\pi \sin\theta &= \pm \frac{3\pi}{4}, \\
&\quad \pm \frac{5\pi}{4}, \\
&\quad \pm \frac{7\pi}{4}
\end{aligned}
$$

Tương ứng với các giá trị:

$$
\begin{aligned}
\sin\theta &= \pm 0{,}375, \\
&\quad \pm 0{,}625, \\
&\quad \pm 0{,}875
\end{aligned}
$$

Từ đó cho các góc phương vị khác:

$$
\begin{aligned}
\theta &= \pm 22{,}0^\circ, \pm 38{,}7^\circ, \pm 61{,}0^\circ
\end{aligned}
$$

Chúng ta có thể dễ dàng kiểm tra lại các giá trị này bằng cách thay ngược vào hàm cosin. Tuy nhiên, đưa những góc này vào phần đáp số của câu (b) là không chuẩn xác, bởi vì đề bài yêu cầu tìm góc gần phương $\theta = 0^\circ$ nhất mà tại đó cường độ bằng $I_0/2$. Những góc bổ sung này ứng với các búp sóng phụ ở hai bên sườn.

</details>

**Khái niệm cần nhớ**: Cường độ tại mỗi điểm trong hệ vân giao thoa hai nguồn phụ thuộc trực tiếp vào độ lệch pha $\phi$ giữa hai sóng tới. Cường độ đạt giá trị cực đại tại các điểm có độ lệch pha bằng một số chẵn lần $\pi$ ($0, \pm 2\pi, \pm 4\pi, \dots$), và triệt tiêu hoàn toàn tại các điểm có độ lệch pha bằng một số lẻ lần $\pi$ ($\pm \pi, \pm 3\pi, \dots$).

### Câu hỏi tự kiểm tra 35.3

Một thí nghiệm giao thoa hai khe sử dụng ánh sáng kết hợp có bước sóng $5{,}00 \times 10^{-7}\,\mathrm{m}$. Hãy xếp hạng các điểm sau đây trong hệ vân giao thoa theo thứ tự cường độ giảm dần, từ lớn nhất đến nhỏ nhất:
- (i) Điểm có khoảng cách tới khe này dài hơn khe kia một đoạn $4{,}00 \times 10^{-7}\,\mathrm{m}$.
- (ii) Điểm mà hai sóng ánh sáng truyền tới lệch pha nhau $4{,}00\,\mathrm{rad}$.
- (iii) Điểm có khoảng cách tới khe này dài hơn khe kia một đoạn $7{,}50 \times 10^{-7}\,\mathrm{m}$.
- (iv) Điểm mà hai sóng ánh sáng truyền tới lệch pha nhau $2{,}00\,\mathrm{rad}$.

<details><summary>Xem đáp án và giải thích</summary>

Thứ tự xếp hạng từ cao xuống thấp là (i), (iv), (ii), (iii).

Giải thích:

Đối với các trường hợp (i) và (iii), ta biết bước sóng $\lambda$ và hiệu đường đi $d\sin\theta = r_2 - r_1$. Do đó ta áp dụng phương trình (35.14):

$$
\begin{aligned}
I &= I_0 \cos^2\left(\frac{\pi d \sin \theta}{\lambda}\right)
\end{aligned}
$$

Đối với các trường hợp (ii) và (iv), ta biết trực tiếp độ lệch pha $\phi$. Do đó ta áp dụng phương trình (35.10):

$$
\begin{aligned}
I &= I_0 \cos^2\frac{\phi}{2}
\end{aligned}
$$

Tính toán cụ thể cho từng trường hợp:
- Điểm (i): Vì hiệu đường đi $\Delta r = 4{,}00 \times 10^{-7}\,\mathrm{m}$ cho tỉ số $\Delta r/\lambda = 0{,}800$:
  $$
  \begin{aligned}
  I &= I_0 \cos^2(0{,}800\pi\,\mathrm{rad}) \\
  &\approx 0{,}655 I_0
  \end{aligned}
  $$
- Điểm (ii):
  $$
  \begin{aligned}
  I &= I_0 \cos^2\left(\frac{4{,}00\,\mathrm{rad}}{2}\right) \\
  &= I_0 \cos^2(2{,}00\,\mathrm{rad}) \\
  &\approx 0{,}173 I_0
  \end{aligned}
  $$
- Điểm (iii): Vì hiệu đường đi $\Delta r = 7{,}50 \times 10^{-7}\,\mathrm{m}$ cho tỉ số $\Delta r/\lambda = 1{,}50$:
  $$
  \begin{aligned}
  I &= I_0 \cos^2(1{,}50\pi\,\mathrm{rad}) \\
  &= 0
  \end{aligned}
  $$
- Điểm (iv):
  $$
  \begin{aligned}
  I &= I_0 \cos^2\left(\frac{2{,}00\,\mathrm{rad}}{2}\right) \\
  &= I_0 \cos^2(1{,}00\,\mathrm{rad}) \\
  &\approx 0{,}292 I_0
  \end{aligned}
  $$

So sánh các giá trị cường độ:
$$
\begin{aligned}
0{,}655 I_0 &> 0{,}292 I_0 \\
&> 0{,}173 I_0 > 0
\end{aligned}
$$

Do đó thứ tự cường độ giảm dần là (i), (iv), (ii), (iii).

</details>
