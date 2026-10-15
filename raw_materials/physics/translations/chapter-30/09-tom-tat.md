## Tổng kết chương

---

### 1. Hiện tượng hỗ cảm (Mutual Inductance)

Khi dòng điện $i_1$ biến thiên trong cuộn dây 1, từ thông do nó sinh ra gửi qua cuộn dây 2 biến thiên theo thời gian, làm xuất hiện một suất điện động cảm ứng $\mathcal E_2$ trong cuộn dây 2. Ngược lại, khi dòng điện $i_2$ trong cuộn 2 biến thiên, nó cũng gây ra suất điện động cảm ứng $\mathcal E_1$ trong cuộn 1:

$$
\begin{aligned}
\mathcal E_2 &= -M\frac{di_1}{dt} \\
\mathcal E_1 &= -M\frac{di_2}{dt}
\end{aligned} \tag{30.4}
$$

Khi hình học và độ từ thẩm không đổi trong mô hình tuyến tính, $M$ là hằng số và đối xứng giữa hai mạch. Nếu hai mạch có số vòng $N_1,N_2$, hỗ cảm liên hệ với từ thông trung bình mỗi vòng:

$$
M = \frac{N_2 \Phi_{B2}}{i_1} = \frac{N_1 \Phi_{B1}}{i_2} \tag{30.5}
$$

Trong hệ đơn vị SI, đơn vị của hệ số hỗ cảm là henry ($1\text{ H} = 1\text{ Wb/A} = 1\ \Omega\cdot\text{s}$).

![Tóm tắt 30.1: Hiện tượng hỗ cảm giữa hai cuộn dây có số vòng N1 và N2.](img/young-30/tom-tat-30-01-ho-cam.png)


---

### 2. Hiện tượng tự cảm và Cuộn cảm (Self-Inductance)

Một dòng điện biến thiên $i$ trong bất kỳ mạch điện nào cũng sinh ra từ trường biến thiên xuyên qua chính mạch đó, dẫn đến một suất điện động tự cảm $\mathcal E$ xuất hiện ngay trong mạch. Độ tự cảm $L$ phụ thuộc hoàn toàn vào cấu trúc hình học của mạch và vật liệu từ tính xung quanh nó.

Đối với một cuộn dây gồm $N$ vòng, độ tự cảm $L$ được định nghĩa theo tỷ số giữa tổng từ thông móc vòng $N\Phi_B$ và cường độ dòng điện $i$:

$$
L = \frac{N\Phi_B}{i} \tag{30.6}
$$

Theo định luật Faraday, suất điện động tự cảm luôn tỉ lệ thuận với tốc độ biến thiên của dòng điện và có xu hướng chống lại sự biến thiên ấy:

$$
\mathcal E = -L\frac{di}{dt} \tag{30.7}
$$

Cuộn cảm là linh kiện mạch điện được thiết kế chủ động để cung cấp một độ tự cảm đáng kể, thường có dạng ống dây quấn nhiều vòng. Đơn vị đo của độ tự cảm trong hệ SI cũng là henry ($1\text{ H}$).

![Tóm tắt 30.2: Hiện tượng tự cảm sinh ra suất điện động tự cảm chống lại sự biến thiên dòng điện trong cuộn cảm.](img/young-30/tom-tat-30-02-tu-cam.png)

---

### 3. Năng lượng từ trường (Magnetic-Field Energy)

Một cuộn cảm có độ tự cảm $L$ mang dòng điện cường độ $I$ sẽ tích trữ một năng lượng $U$ trong từ trường do nó thiết lập. Năng lượng từ trường này chính bằng công mà nguồn điện phải thực hiện để thắng suất điện động tự cảm trong quá trình tăng dòng từ không đến $I$:

$$
U = \frac{1}{2}LI^2 \tag{30.9}
$$

Năng lượng từ trường phân bố trong không gian có từ trường với mật độ năng lượng $u$ (năng lượng trên một đơn vị thể tích). Trong môi trường chân không, mật độ năng lượng từ trường tỉ lệ thuận với bình phương độ lớn của cảm ứng từ:

$$
u = \frac{B^2}{2\mu_0} \tag{30.10}
$$

Trong vật liệu tuyến tính có độ từ thẩm $\mu$ không đổi, mật độ năng lượng tương ứng là:

$$
u = \frac{B^2}{2\mu} \tag{30.11}
$$

Các biểu thức không bị giới hạn bởi hình học ống dây dùng để suy ra chúng. Tuy nhiên, dạng dùng một độ từ thẩm hằng đòi hỏi mô hình vật liệu tuyến tính đã nêu.

![Tóm tắt 30.3: Năng lượng tích trữ trong từ trường của cuộn cảm và mật độ năng lượng từ trường trong không gian.](img/young-30/tom-tat-30-03-nang-luong-tu-truong.png)


---

### 4. Mạch R-L (R-L Circuits)

Trong một mạch điện chứa một điện trở thuần $R$, một cuộn cảm $L$ và một nguồn suất điện động, sự tăng hoặc giảm của cường độ dòng điện diễn ra theo quy luật hàm mũ theo thời gian do quán tính điện từ của cuộn cảm.

Hằng số thời gian $\tau$ của mạch R-L là khoảng thời gian cần thiết để dòng điện đạt khoảng $63{,}2\%$ giá trị dừng ổn định cực đại trong quá trình tăng dòng, hoặc giảm xuống còn $36{,}8\%$ giá trị ban đầu trong quá trình ngắt dòng:

$$
\tau = \frac{L}{R} \tag{30.16}
$$

Quy luật tăng dòng khi đóng mạch với nguồn suất điện động $\mathcal E$ có dạng:

$$
\begin{aligned}
i(t) &= \frac{\mathcal E}{R}\left(1 - e^{-(R/L)t}\right) \\
&= I\left(1 - e^{-t/\tau}\right)
\end{aligned}
$$

Quy luật suy giảm dòng qua điện trở khi ngắt nguồn khỏi mạch kín có dạng:

$$
i(t) = I_0 e^{-(R/L)t} = I_0 e^{-t/\tau}
$$

![Tóm tắt 30.4: Quá trình tăng dòng theo hàm mũ trong mạch R-L và ý nghĩa của hằng số thời gian tau.](img/young-30/tom-tat-30-04-mach-rl.png)

---

### 5. Mạch dao động L-C (L-C Circuits)

Một mạch điện kín gồm cuộn cảm có độ tự cảm $L$ mắc nối tiếp với tụ điện có điện dung $C$ (không có điện trở thuần) thực hiện các dao động điện từ điều hòa tuần hoàn.

Tần số góc dao động riêng $\omega$ của mạch L-C lý tưởng được xác định bởi:

$$
\omega = \sqrt{\frac{1}{LC}} \tag{30.22}
$$

Điện tích trên bản cực tụ điện và cường độ dòng điện trong mạch biến thiên điều hòa theo thời gian với độ lệch pha $\pi/2$ (với $i = dq/dt$):

$$
\begin{aligned}
q(t) &= Q\cos(\omega t + \phi) \\
i(t) &= -\omega Q\sin(\omega t + \phi)
\end{aligned}
$$

Dao động điện trong mạch L-C tương đương hoàn toàn với dao động cơ học điều hòa của con lắc lò xo lý tưởng. Cụ thể, điện tích $q$ đóng vai trò li độ $x$, còn dòng điện $i$ đóng vai trò vận tốc $v_x$. Đồng thời, độ tự cảm $L$ tương ứng với khối lượng $m$, và nghịch đảo điện dung $1/C$ tương ứng với độ cứng lò xo $k$.

Năng lượng toàn phần của mạch L-C được bảo toàn và chuyển hóa tuần hoàn qua lại giữa năng lượng từ trường trong cuộn cảm và năng lượng điện trường trong tụ điện:

$$
E = \frac{1}{2}Li^2 + \frac{q^2}{2C} = \frac{Q^2}{2C}
$$

![Tóm tắt 30.5: Dao động điện từ tuần hoàn trong mạch L-C lý tưởng với sự chuyển hóa qua lại giữa năng lượng điện trường và năng lượng từ trường.](img/young-30/tom-tat-30-05-mach-lc.png)

---

### 6. Mạch dao động nối tiếp L-R-C (L-R-C Series Circuits)

Khi mạch dao động chứa thêm điện trở thuần $R$, năng lượng điện từ của hệ thống bị tiêu tán liên tục thành nhiệt năng qua hiệu ứng Joule ($i^2 R$).

Khi điện trở thuần đủ nhỏ ($R^2 < 4L/C$), hệ thống rơi vào chế độ dao động tắt dần với biên độ điện tích giảm theo hàm mũ $e^{-(R/2L)t}$. Tần số góc dao động tắt dần $\omega'$ nhỏ hơn tần số góc riêng của mạch không có điện trở và được xác định bởi:

$$
\omega' = \sqrt{\frac{1}{LC} - \frac{R^2}{4L^2}} \tag{30.29}
$$

Khi $R$ đạt $R_{\text{th}}=2\sqrt{L/C}$, hệ tắt dần tới hạn. Khi $R$ vượt ngưỡng ấy, hệ quá tắt dần. Hai chế độ này không có dao động đổi chiều lặp lại. Với điều kiện đầu khác, một lần đổi dấu vẫn có thể xuất hiện.

![Tóm tắt 30.6: Đồ thị dao động tắt dần của điện tích theo thời gian trong mạch dao động nối tiếp L-R-C.](img/young-30/tom-tat-30-06-mach-rlc.png)
