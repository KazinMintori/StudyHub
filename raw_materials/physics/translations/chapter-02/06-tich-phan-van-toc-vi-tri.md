## 2.6. Xác định vận tốc và vị trí bằng tích phân

Các phương trình ở Mục 2.4 được thiết lập với giả thiết gia tốc không đổi. Khi gia tốc biến thiên, ta không thể dùng trực tiếp những phương trình đó. Chẳng hạn, đạp hết bàn đạp ga không làm ô tô có gia tốc không đổi. Tốc độ càng lớn thì xe càng tăng thêm tốc độ chậm hơn.

![Hình 2.26: Một ô tô điển hình cần thời gian tăng tốc từ 50 km/h lên 100 km/h dài gấp đôi thời gian tăng từ 0 lên 50 km/h](img/young-02/hinh-2-26.png)

Các quan hệ đạo hàm vẫn đúng khi gia tốc biến thiên. Nếu biết vị trí theo thời gian, ta tìm vận tốc bằng:

$$
v_x=\frac{dx}{dt}.
$$

Nếu biết vận tốc theo thời gian, ta tìm gia tốc bằng:

$$
a_x=\frac{dv_x}{dt}.
$$

Tuy nhiên, có những tình huống gia tốc là hàm đã biết, còn vị trí và vận tốc chưa biết. Muốn tìm hai đại lượng ấy từ gia tốc, ta thực hiện quá trình ngược với phép đạo hàm, tức phép tích phân. Phần này sử dụng kiến thức tích phân một biến.

### Ứng dụng: Hệ thống dẫn đường quán tính

![Hình 2.27: Hệ thống dẫn đường quán tính theo dõi gia tốc của máy bay đường dài để tính vận tốc và vị trí từ các điều kiện ban đầu](img/young-02/hinh-2-27.png)

Hệ thống dẫn đường quán tính (inertial navigation system, INS) theo dõi gia tốc máy bay. Khi biết vị trí và vận tốc ban đầu trước lúc cất cánh, hệ thống dùng dữ liệu gia tốc để tính vận tốc và vị trí trong suốt chuyến bay.

Phép tích phân thứ nhất cho độ biến thiên vận tốc. Phép tích phân tiếp theo cho độ biến thiên vị trí. Vì thế, cả dữ liệu gia tốc lẫn các điều kiện ban đầu đều cần thiết.

### Từ các khoảng thời gian nhỏ đến tích phân gia tốc

Xét đồ thị gia tốc theo thời gian ở Hình 2.28. Chia khoảng từ $t_1$ đến $t_2$ thành nhiều khoảng nhỏ. Trong một khoảng có độ dài Δt, gọi gia tốc trung bình là $a_{\mathrm{av}-x}$. Theo định nghĩa:

$$
\Delta v_x=a_{\mathrm{av}-x}\Delta t.
$$

![Hình 2.28: Diện tích có dấu dưới đồ thị gia tốc theo thời gian cho độ biến thiên vận tốc](img/young-02/hinh-2-28.png)

Diện tích dải hình chữ nhật có chiều cao bằng gia tốc trung bình và chiều rộng bằng Δt cho độ biến thiên vận tốc trong khoảng ấy. Toàn bộ độ biến thiên vận tốc là:

$$
\Delta v_x=v_{2x}-v_{1x}.
$$

Nó bằng tổng các phần đóng góp. Gọi $\delta_i$ là độ biến thiên vận tốc trong khoảng nhỏ thứ i. Với N khoảng nhỏ:

$$
\begin{aligned}
\Delta v_x
&=\delta_1+\delta_2+\dots+\delta_N\\
&=\sum_{i=1}^{N}\delta_i.
\end{aligned}
$$

Chỉ số i chạy từ 1 đến N, mỗi số hạng là độ biến thiên vận tốc trong một khoảng nhỏ. Khi các khoảng thời gian tiến tới không và số khoảng tăng lên, gia tốc trung bình tiến tới gia tốc tức thời. Tổng diện tích tiến tới tích phân:

$$
\begin{aligned}
v_{2x}-v_{1x}&=\int_{v_{1x}}^{v_{2x}}dv_x\\
&=\int_{t_1}^{t_2}a_x(t)\,dt.
\end{aligned}
\tag{2.15}
$$

Độ biến thiên vận tốc bằng tích phân gia tốc theo thời gian. Phần dưới đồ thị ở phía trên trục thời gian đóng góp dương, còn phần ở phía dưới đóng góp âm. Trong trường hợp gia tốc không đổi, kết quả trở về diện tích hình chữ nhật ở Mục 2.4.

### Tích phân vận tốc cho độ dời

Lập luận tương tự cho đồ thị vận tốc theo thời gian. Trong một khoảng nhỏ, độ dời bằng vận tốc trung bình nhân với độ dài khoảng thời gian:

$$
\Delta x=v_{\mathrm{av}-x}\Delta t.
$$

Cộng các độ dời và lấy giới hạn cho:

$$
\begin{aligned}
x_2-x_1&=\int_{x_1}^{x_2}dx\\
&=\int_{t_1}^{t_2}v_x(t)\,dt.
\end{aligned}
\tag{2.16}
$$

Độ dời bằng diện tích có dấu dưới đồ thị vận tốc theo thời gian. Đây cũng là kết quả đã dùng ở Mục 2.4 cho vận tốc biến thiên tuyến tính. Nếu vận tốc đổi dấu, tích phân cộng các phần có dấu, nên không bằng tổng quãng đường nói chung.

Chọn thời điểm đầu bằng 0. Gọi vận tốc đầu là $v_{0x}$ và tọa độ đầu là $x_0$. Hai công thức trở thành:

$$
v_x(t)=v_{0x}+\int_0^t a_x(u)\,du.
\tag{2.17}
$$

$$
x(t)=x_0+\int_0^t v_x(u)\,du.
\tag{2.18}
$$

Biến u là biến lấy tích phân, khác với cận trên t. Biết hàm gia tốc và vận tốc đầu cho phép xác định hàm vận tốc. Biết thêm tọa độ đầu thì có thể dùng hàm vận tốc ấy để xác định tọa độ tại mọi thời điểm thuộc miền mô hình.

### Ví dụ 2.9: Chuyển động với gia tốc thay đổi

::: exercise Ô tô của Sally
Sally lái xe trên đường cao tốc thẳng. Tại t = 0, xe chuyển động theo chiều dương với vận tốc 10 m/s và đi qua cột mốc ở tọa độ x = 50 m. Gia tốc giảm tuyến tính theo thời gian:

$$
a_x(t)=A-Bt.
$$

Các hệ số đã cho là:

$$
A=2{,}0\,\mathrm{m/s^2},
$$

$$
B=0{,}10\,\mathrm{m/s^3}.
$$

(a) Tìm vận tốc và tọa độ theo thời gian. (b) Vận tốc theo trục x lớn nhất lúc nào? (c) Vận tốc lớn nhất bằng bao nhiêu? (d) Xe ở đâu khi đạt vận tốc lớn nhất?
:::

::: solution Tích phân và xét cực đại vận tốc
Gia tốc phụ thuộc thời gian nên không dùng các phương trình gia tốc không đổi để mô tả toàn khoảng. Tích phân theo (2.17) cho vận tốc, sau đó dùng (2.18) cho tọa độ.

Hai hệ số A và B có đơn vị như đề bài. Các điều kiện đầu là $x_0$ = 50 m và $v_{0x}$ = 10 m/s.

(a) Dùng quy tắc nguyên hàm của lũy thừa với số mũ n khác −1:

$$
\int u^n\,du=\frac{u^{n+1}}{n+1}+C.
$$

Độ biến thiên vận tốc:

$$
\begin{aligned}
\Delta v_x&=\int_0^t(A-Bu)\,du\\
&=\left[Au-\frac12Bu^2\right]_0^t\\
&=At-\frac12Bt^2.
\end{aligned}
$$

Vận tốc là:

$$
v_x(t)=v_{0x}+At-\frac12Bt^2.
$$

Tiếp theo, lấy tích phân từng số hạng của vận tốc. Phần vận tốc đầu cho:

$$
\int_0^t v_{0x}\,du=v_{0x}t.
$$

Hai phần còn lại cho:

$$
\int_0^t Au\,du=\frac12At^2,
$$

$$
\int_0^t\left(-\frac12Bu^2\right)du=-\frac16Bt^3.
$$

Vì vậy, độ dời tính từ thời điểm đầu là:

$$
\Delta x=v_{0x}t+\frac12At^2-\frac16Bt^3.
$$

Tọa độ được xác định bằng:

$$
x(t)=x_0+\Delta x.
$$

Các hệ số A và B đã giữ đầy đủ đơn vị của các số hạng. Để tính số theo giây, gọi q = t/(1 s), V = $v_x$/(1 m/s) và X = x/(1 m). Các giá trị số theo đơn vị SI là:

$$
V=10+2{,}0q-0{,}050q^2,
$$

$$
X=50+10q+1{,}0q^2-\frac{q^3}{60}.
$$

Tại mỗi thời điểm, độ dốc của đồ thị vận tốc bằng gia tốc và độ dốc của đồ thị tọa độ bằng vận tốc.

(b) Vận tốc lớn nhất tại thời điểm nó ngừng tăng và bắt đầu giảm. Đạo hàm của vận tốc là gia tốc. Giải $a_x$ = 0:

$$
A-Bt=0,
$$

$$
t=\frac{A}{B}=20\,\mathrm s.
$$

Trước 20 s, gia tốc dương nên vận tốc tăng. Sau 20 s, gia tốc âm nên vận tốc giảm. Việc đổi dấu này xác nhận điểm đang xét là cực đại, thay vì chỉ dựa vào điều kiện đạo hàm bằng không.

(c) Tại t = 20 s, ta có At = 40 m/s và Bt²/2 = 20 m/s. Do đó:

$$
\begin{aligned}
v_{\max-x}&=(10+40-20)\,\mathrm{m/s}\\
&=30\,\mathrm{m/s}.
\end{aligned}
$$

(d) Các số hạng vị trí tại 20 s lần lượt là $x_0$ = 50 m, $v_{0x}$t = 200 m, At²/2 = 400 m và Bt³/6 = 400/3 m. Tổng ba phần dương bằng 650 m. Cộng theo dấu:

$$
\begin{aligned}
x&=\left(650-\frac{400}{3}\right)\,\mathrm m\\
&=\frac{1550}{3}\,\mathrm m\\
&\approx517\,\mathrm m.
\end{aligned}
$$

Đây là tọa độ so với gốc, còn độ dời từ cột mốc ban đầu bằng tọa độ này trừ 50 m.
:::

![Hình 2.29: Gia tốc đổi dấu tại 20 s, vận tốc đạt cực đại và đồ thị tọa độ đổi chiều lõm tại cùng thời điểm](img/young-02/hinh-2-29.png)

Đồ thị gia tốc nằm trên trục thời gian từ 0 đến 20 s rồi xuống dưới. Trong đoạn xe còn đi theo chiều dương, vận tốc và gia tốc cùng dấu trước 20 s nên xe nhanh dần. Sau 20 s, chúng trái dấu nên xe chậm dần cho tới khi dừng.

Đồ thị tọa độ có độ dốc dương lớn nhất tại 20 s. Đường cong lõm lên trước thời điểm ấy vì gia tốc dương, rồi lõm xuống vì gia tốc âm.

### Câu hỏi về Hình 2.29

::: exercise Xe dừng lại lúc nào
Nếu chuyển động trong Ví dụ 2.9 tiếp tục theo cùng quy luật, hãy chứng minh xe dừng lại tại thời điểm xấp xỉ 44,5 s.
:::

::: solution Giải thích
Xe dừng tức thời khi vận tốc bằng không. Với q = t/(1 s), phương trình vận tốc cho:

$$
10+2q-0{,}050q^2=0.
$$

Nhân với −20 rồi chuyển vế:

$$
q^2-40q-200=0.
$$

Hai nghiệm là:

$$
q=20\pm\sqrt{600}.
$$

Chỉ nghiệm dương thuộc khoảng sau t = 0:

$$
t=(20+\sqrt{600})\,\mathrm s\approx44{,}5\,\mathrm s.
$$

Kết luận dựa trên giả thiết quy luật gia tốc tiếp tục có hiệu lực đến thời điểm này.
:::

### Tự kiểm tra 2.6

::: exercise Đồ thị khi gia tốc tăng theo thời gian
Nếu gia tốc theo trục x của một vật chuyển động thẳng tăng theo thời gian, đồ thị vận tốc theo thời gian là: (i) Đường thẳng, (ii) Đường cong lõm lên hay (iii) Đường cong lõm xuống?
:::

::: solution Giải thích
Chọn (ii). Gia tốc bằng độ dốc tiếp tuyến của đồ thị vận tốc. Gia tốc tăng theo thời gian nghĩa là độ dốc tăng, nên đồ thị lõm lên. Không cần giả thiết gia tốc phải dương. Gia tốc âm nhưng đang tăng cũng cho độ dốc tăng.
:::
