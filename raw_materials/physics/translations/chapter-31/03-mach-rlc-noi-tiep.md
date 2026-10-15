## 31.3. Mạch RLC nối tiếp

Điện trở, cuộn cảm và tụ điện thường cùng xuất hiện trong mạch điện tử. Làm thế nào cộng điện áp của chúng khi các điện áp đạt cực đại vào những thời điểm khác nhau?

Ta xét mạch RLC nối tiếp với nguồn xoay chiều. Khác mạch RLC tự do đã học, mạch này liên tục nhận năng lượng từ nguồn hình sin.

![Hình 31.13: Mạch RLC nối tiếp và hai giản đồ pha khi cảm kháng lớn hơn hoặc nhỏ hơn dung kháng.](../img/young-31/hinh-31-13.png)

### Cộng điện áp bằng vector pha

Vì ba phần tử nối tiếp, dòng tức thời ở mọi điểm là như nhau. Chọn dòng làm mốc:

$$
i=I\cos\omega t.
$$

Trong Hình 31.13a, điện áp nguồn và điện áp ba phần tử được đặt tên theo các đầu mạch:

$$
\begin{aligned}
v &= v_{ad}, \\
v_R &= v_{ab}, \\
v_L &= v_{bc}, \\
v_C &= v_{cd}.
\end{aligned}
$$

Theo định luật vòng Kirchhoff, tại mỗi thời điểm:

$$
v=v_R+v_L+v_C.
$$

Ba vector pha điện áp có độ dài

$$
\begin{aligned}
V_R &= IR, \\
V_L &= IX_L, \\
V_C &= IX_C.
\end{aligned}
$$

Vector $V_R$ cùng hướng vector dòng. Vector $V_L$ sớm hơn 90 độ, còn $V_C$ trễ hơn 90 độ. Do đó hai vector cuộn cảm và tụ luôn cùng phương, ngược chiều.

Hình chiếu của tổng các vector bằng tổng hình chiếu của từng vector. Vì hình chiếu cho điện áp tức thời, vector điện áp nguồn chính là tổng vector ba điện áp. Khi đặt đuôi các vector tại cùng một điểm, phần dọc phương vuông góc dòng là $V_L-V_C$.

Áp dụng định lý Pythagoras:

$$
\begin{aligned}
V^2 &= V_R^2+(V_L-V_C)^2, \\
&= I^2R^2 +I^2(X_L-X_C)^2.
\end{aligned}
$$

Vì $I$ và $V$ là các biên độ không âm:

$$
V=I\sqrt{R^2+(X_L-X_C)^2}.\tag{31.20}
$$

### Trở kháng

**Trở kháng** $Z$ của mạch được xác định bằng tỉ số biên độ điện áp toàn mạch và biên độ dòng. Với mạch RLC nối tiếp:

$$
Z=\sqrt{R^2+(X_L-X_C)^2}.\tag{31.21}
$$

Do đó

$$
V=IZ.\tag{31.22}
$$

Trở kháng có đơn vị ôm. Công thức (31.22) định nghĩa tỉ số biên độ cho mạng điện xoay chiều đang xét. Công thức căn bậc hai ở (31.21) chỉ áp dụng trực tiếp cho mạch RLC nối tiếp, không phải mọi mạng RLC.

Để thấy rõ tần số tham gia thế nào, đặt

$$
X=\omega L-\frac1{\omega C}.
$$

Khi đó biểu thức đầy đủ là

$$
\begin{aligned}
Z &= \sqrt{R^2+X^2}, \\
X &= \omega L-\frac1{\omega C}.\tag{31.23}
\end{aligned} \tag{31.23}
$$

Với cùng biên độ nguồn $V$, dòng $I=V/Z$ thay đổi theo tần số. Trong các nhánh song song chịu cùng điện áp, nhánh có trở kháng nhỏ hơn có biên độ dòng lớn hơn.

![Hình 31.14: Khi chạm vào quả cầu plasma, điện dung tạo bởi tay và mặt trong quả cầu làm thay đổi trở kháng, khiến các dải phát sáng tập trung về phía ngón tay.](../img/young-31/hinh-31-14.png)

Trong quả cầu chứa khí, nguồn tạo điện áp xoay chiều giữa điện cực trung tâm và bề mặt. Tay và mặt trong quả cầu đóng vai trò hai bản tụ qua thành thủy tinh. Đường mạch qua vị trí ngón tay có trở kháng thấp hơn nên dòng trong khí tập trung về phía ấy.

### Góc pha của điện áp nguồn

Góc $\phi$ trong giản đồ là góc của điện áp nguồn so với dòng. Trong tam giác vector:

$$
\begin{aligned}
\tan\phi &= \frac{V_L-V_C}{V_R} \\
&= \frac{X_L-X_C}{R} \\
&= \frac{\omega L-1/(\omega C)}R.\tag{31.24}
\end{aligned} \tag{31.24}
$$

Với $R>0$, chọn góc trong khoảng từ $-\pi/2$ đến $\pi/2$. Nếu dòng là $I\cos\omega t$, điện áp nguồn là

$$
v=V\cos(\omega t+\phi).\tag{31.25}
$$

- Khi $X_L>X_C$, góc pha dương và điện áp nguồn sớm hơn dòng.
- Khi $X_L<X_C$, góc pha âm và điện áp nguồn trễ hơn dòng.
- Khi $X_L=X_C$, góc pha bằng không và điện áp nguồn cùng pha dòng.

Vì hai điện kháng phụ thuộc tần số, góc pha cũng phụ thuộc tần số. Với $R=0$ và điện kháng tổng khác không, góc pha là $+\pi/2$ hoặc $-\pi/2$. Trường hợp lý tưởng $R=0$, $X_L=X_C$ cần xét riêng vì công thức dòng hữu hạn $I=V/Z$ không còn cho trạng thái ổn định hữu hạn.

### Ứng dụng: Đo thành phần cơ thể bằng trở kháng

![Ứng dụng 31.3: Các điện cực đưa tín hiệu xoay chiều nhỏ vào cơ thể để đo biên độ và pha của đáp ứng điện.](../img/young-31/ung-dung-31-do-thanh-phan-co-the.png)

Trong phép đo trở kháng sinh học được minh họa, các điện cực tạo điện áp xoay chiều nhỏ ở tần số 50 kHz. Thiết bị đo biên độ và góc pha của dòng đáp ứng. Hai đại lượng phụ thuộc lượng nước và mỡ dọc đường dòng đi qua, nên cung cấp thông tin về thành phần cơ thể.

Ở đây cần đo cả biên độ lẫn pha. Chỉ lấy tỉ số một điện áp tức thời với một dòng tức thời sẽ không xác định đúng trở kháng.

### Khi thiếu một phần tử

Các biểu thức nối tiếp vẫn áp dụng với quy ước thích hợp. Bỏ điện trở thì đặt $R=0$. Bỏ cuộn cảm thì đặt $L=0$.

Bỏ tụ có nghĩa nối hai đầu vị trí tụ bằng dây, làm điện áp ở đó bằng không. Vì vậy phải đặt $X_C=0$, tương đương giới hạn $C\to\infty$. Đặt $C=0$ sẽ mô tả một trường hợp hoàn toàn khác vì dung kháng khi ấy tiến tới vô hạn.

### Dùng giá trị hiệu dụng

Mọi dòng và điện áp ở đây đều hình sin cùng tần số. Chia các biên độ cho $\sqrt2$ không làm đổi các tỉ số giữa chúng. Từ $V=IZ$:

$$
V_{\mathrm{rms}}=I_{\mathrm{rms}}Z.\tag{31.26}
$$

Tương tự:

$$
\begin{aligned}
V_{R,\mathrm{rms}} &= I_{\mathrm{rms}}R, \\
V_{L,\mathrm{rms}} &= I_{\mathrm{rms}}X_L, \\
V_{C,\mathrm{rms}} &= I_{\mathrm{rms}}X_C.
\end{aligned}
$$

Cần dùng nhất quán biên độ hoặc hiệu dụng trong cùng một phép tính. Phân tích mạch RLC song song dùng nguyên lý tương tự nhưng cộng các vector dòng, như Bài 31.54.

### Cách phân tích một mạch xoay chiều

1. Vẽ mạch, đánh dấu các đầu điện áp, chiều dòng và mọi đại lượng đã biết. Xác định rõ cần tìm biên độ, hiệu dụng hay giá trị tức thời.
2. Đổi tần số sang tần số góc $\omega=2\pi f$ khi dùng cảm kháng và dung kháng.
3. Giữ quan hệ pha của từng phần tử. Điện trở cùng pha dòng, cuộn cảm sớm 90 độ, tụ trễ 90 độ.
4. Dùng Kirchhoff tại từng thời điểm. Mạch nối tiếp có cùng dòng, mạch song song có cùng điện áp hai đầu các nhánh.
5. Khi cần biên độ nguồn, cộng các vector pha. Không cộng số học điện trở với các điện kháng để tạo trở kháng.
6. Đối chiếu dấu góc pha với $X_L-X_C$. Cảm kháng lớn hơn phải cho điện áp cuộn lớn hơn điện áp tụ và góc pha dương. Dung kháng lớn hơn phải cho góc pha âm.

::: example Ví dụ 31.4: Biên độ và pha của mạch RLC
Với mạch Hình 31.13a, cho $R=300\,\Omega$, $L=60\,\mathrm{mH}$, $C=0{,}50\,\mu\mathrm F$, biên độ nguồn $V=50\,\mathrm V$ và $\omega=10\,000\,\mathrm{rad/s}$.

Tìm $X_L$, $X_C$, $Z$, biên độ dòng, góc pha và biên độ điện áp trên từng phần tử.

**Nhận dạng và chuẩn bị:** Từ tần số góc tìm hai điện kháng. Dùng chúng để tìm trở kháng và dòng, rồi dựng tam giác pha để xác định góc và từng điện áp.

**Lời giải:** Hai điện kháng:

$$
\begin{aligned}
X_L &= \omega L=600\,\Omega, \\
X_C &= \frac1{\omega C}=200\,\Omega.
\end{aligned}
$$

Trở kháng:

$$
\begin{aligned}
Z &= \sqrt{R^2+(X_L-X_C)^2} \\
&= \sqrt{300^2+400^2}\,\Omega \\
&= 500\,\Omega.
\end{aligned}
$$

Biên độ dòng:

$$
I=\frac{50\,\mathrm V}{500\,\Omega}=0{,}10\,\mathrm A.
$$

Góc pha:

$$
\begin{aligned}
\phi &= \arctan\frac{400}{300} \\
&\approx 53^\circ.
\end{aligned}
$$

Điện áp trên các phần tử:

$$
\begin{aligned}
V_R &= IR=30\,\mathrm V, \\
V_L &= IX_L=60\,\mathrm V, \\
V_C &= IX_C=20\,\mathrm V.
\end{aligned}
$$

**Đánh giá:** Cảm kháng lớn hơn dung kháng nên điện áp nguồn sớm dòng khoảng 53 độ. Biên độ nguồn 50 V không bằng tổng số học 30 V, 60 V và 20 V.

Trong tam giác pha, hai cạnh vuông là 30 V và 40 V, cạnh huyền là 50 V. Đây là tam giác có tỉ lệ 3, 4, 5. Điện áp cuộn có thể có biên độ lớn hơn điện áp nguồn vì điện áp tụ triệt tiêu một phần nó trong tổng vector.
:::

::: example Ví dụ 31.5: Các điện áp tức thời
Với mạch ở Ví dụ 31.4, tìm biểu thức theo thời gian của dòng, điện áp điện trở, cuộn cảm, tụ và nguồn.

**Nhận dạng và chuẩn bị:** Chọn $t=0$ khi dòng đạt cực đại. Dùng các biên độ đã tìm và giữ đúng độ lệch pha của từng điện áp.

**Lời giải:** Tất cả dao động với tần số góc $10\,000\,\mathrm{rad/s}$. Chu kỳ:

$$
\begin{aligned}
T &= \frac{2\pi}{\omega} \\
&\approx 6{,}3\times10^{-4}\,\mathrm s \\
&= 0{,}63\,\mathrm{ms}.
\end{aligned}
$$

Đặt $\theta=(10\,000\,\mathrm{rad/s})t$ để viết ngắn các biểu thức:

$$
\begin{aligned}
i &= (0{,}10\,\mathrm A)\cos\theta, \\
v_R &= (30\,\mathrm V)\cos\theta.
\end{aligned}
$$

Điện áp cuộn sớm dòng 90 độ:

$$
\begin{aligned}
v_L &= (60\,\mathrm V)\cos(\theta+\pi/2) \\
&= -(60\,\mathrm V)\sin\theta.
\end{aligned}
$$

Điện áp tụ trễ dòng 90 độ:

$$
\begin{aligned}
v_C &= (20\,\mathrm V)\cos(\theta-\pi/2) \\
&= (20\,\mathrm V)\sin\theta.
\end{aligned}
$$

Góc pha nguồn $\phi=\arctan(4/3)$, xấp xỉ $0{,}93\,\mathrm{rad}$, nên

$$
v=(50\,\mathrm V)\cos(\theta+\phi).
$$

![Hình 31.15: Đồ thị bốn điện áp trong mạch RLC, với điện áp nguồn bằng tổng ba điện áp thành phần tại mỗi thời điểm.](../img/young-31/hinh-31-15.png)

**Đánh giá:** Vì $\cos\phi=3/5$ và $\sin\phi=4/5$:

$$
\begin{aligned}
v &= (30\,\mathrm V)\cos\theta -(40\,\mathrm V)\sin\theta \\
&= v_R+v_L+v_C.
\end{aligned}
$$

Kirchhoff liên hệ các giá trị tức thời. Việc các biên độ không cộng số học không làm thay đổi định luật này. Trên đồ thị, dòng chưa được vẽ nhưng luôn cùng pha điện áp điện trở.
:::

### Câu hỏi tự kiểm 31.3

Xếp các mạch sau theo biên độ dòng từ lớn đến nhỏ, với cùng nguồn và tần số như Ví dụ 31.4:

(i) Mạch RLC của ví dụ. (ii) Bỏ cả tụ và cuộn cảm, chỉ còn điện trở. (iii) Bỏ điện trở và tụ, chỉ còn cuộn cảm. (iv) Bỏ điện trở và cuộn cảm, chỉ còn tụ.

<details><summary>Xem đáp án và giải thích</summary>

Thứ tự là (iv), (ii), (i), (iii). Các biên độ:

$$
\begin{aligned}
I_{\mathrm{(iv)}} &= \frac{50}{200}\,\mathrm A=0{,}25\,\mathrm A, \\
I_{\mathrm{(ii)}} &= \frac{50}{300}\,\mathrm A\approx0{,}17\,\mathrm A, \\
I_{\mathrm{(i)}} &= \frac{50}{500}\,\mathrm A=0{,}10\,\mathrm A, \\
I_{\mathrm{(iii)}} &= \frac{50}{600}\,\mathrm A\approx0{,}083\,\mathrm A.
\end{aligned}
$$

So sánh các trở kháng, không so sánh số phần tử. Nhiều phần tử hơn không tự động cho trở kháng lớn hơn, vì hai điện kháng có thể triệt tiêu nhau.

</details>
