<!-- Chuyên đề: Chuyển động thẳng — Tích phân trong Động học -->

## 2.6. Xác định vận tốc và vị trí bằng phương pháp tích phân

Trong mục 2.4, chúng ta đã xây dựng bộ công thức động học cho trường hợp gia tốc không đổi. Tuy nhiên, trong thế giới thực, gia tốc cố định chỉ là trường hợp lý tưởng hóa đặc biệt. Phần lớn các chuyển động trong kỹ thuật và tự nhiên đều có gia tốc biến thiên liên tục theo thời gian:
- Khi một người lái xe đạp lút ga từ trạng thái đứng yên, lực cản của không khí và ma sát lăn tăng dần theo tốc độ khiến gia tốc của xe giảm dần (Hình 2.26). Một chiếc xe thông thường có thể chỉ mất $4\,\mathrm s$ để tăng tốc từ $0$ lên $50\,\mathrm{km/h}$, nhưng phải mất tới $8\,\mathrm s$ hoặc hơn để tăng tiếp từ $50$ lên $100\,\mathrm{km/h}$.
- Khi một tên lửa rời bệ phóng, khối lượng của nó giảm liên tục do tiêu thụ hàng tấn nhiên liệu mỗi giây, đồng thời lực cản khí quyển giảm dần khi lên cao, khiến gia tốc của tên lửa tăng vọt theo thời gian.

Trong những tình huống như vậy, toàn bộ các phương trình đại số của chuyển động biến đổi đều hoàn toàn mất hiệu lực. Lúc này, công cụ vi tích phân của Newton và Leibniz chính là chìa khóa duy nhất để giải mã quy luật chuyển động.

![Hình 2.26: Sự phụ thuộc của gia tốc vào tốc độ khi tăng ga ô tô](img/young-02/hinh-2-26.png)

**Hình 2.26:** Đạp hết bàn đạp ga không hề tạo ra một gia tốc không đổi. Tốc độ càng cao, lực cản không khí càng lớn và hiệu suất truyền lực của động cơ thay đổi, khiến gia tốc của xe suy giảm dần theo thời gian.

Nếu như phép tính đạo hàm cho phép ta đi từ vị trí sang vận tốc ($v_x = dx/dt$) và từ vận tốc sang gia tốc ($a_x = dv_x/dt$), thì phép tính tích phân chính là quá trình đảo ngược: Giúp ta khôi phục lại quy luật vận tốc và vị trí khi đã biết hàm số của gia tốc theo thời gian $a_x(t)$.

---

### Một đỉnh cao công nghệ: Hệ thống dẫn đường quán tính (INS)

Một trong những ứng dụng kỳ diệu nhất của tích phân động học trong thế giới hiện đại là **Hệ thống dẫn đường quán tính** (Inertial Navigation System — INS) trang bị trên máy bay thương mại đường dài (Hình 2.27), tàu ngầm hạt nhân lặn sâu dưới đáy đại dương và tên lửa hành trình. 

![Hình 2.27: Hệ thống dẫn đường quán tính (INS) trên máy bay đường dài](img/young-02/hinh-2-27.png)

**Hình 2.27:** Máy bay thương mại xuyên lục địa sử dụng hệ thống dẫn đường quán tính (INS). Dựa vào các cảm biến gia tốc kế (accelerometer) siêu nhạy, máy tính trên khoang thực hiện tích phân liên tục theo thời gian để xác định chính xác vận tốc và tọa độ của máy bay mà không phụ thuộc vào tín hiệu GPS bên ngoài.

Tàu ngầm quân sự khi lặn sâu hàng trăm mét dưới lớp băng Bắc Cực hoàn toàn bị cô lập khỏi sóng vô tuyến và tín hiệu vệ tinh GPS. Làm sao thủy thủ đoàn biết được vị trí của con tàu với sai số chỉ vài mét sau hàng ngàn hải lý hành trình? Câu trả lời là: Trước khi lặn, người ta nạp tọa độ xuất phát ($x_0$) và vận tốc ban đầu ($v_0$) vào máy tính. Trong suốt hải trình, các cảm biến gia tốc kế cực nhạy liên tục đo gia tốc $a(t)$. Máy tính thực hiện **tích phân lần thứ nhất** để tìm vận tốc $v(t)$, rồi thực hiện tiếp **tích phân lần thứ hai** để tìm vị trí $x(t)$ theo thời gian thực!

---

### Độ biến thiên vận tốc là tích phân của gia tốc

Xét một chuyển động có gia tốc $a_x(t)$ biến thiên liên tục theo thời gian như đồ thị ở Hình 2.28. Ta chia khoảng thời gian khảo sát từ $t_1$ đến $t_2$ thành vô số khoảng thời gian vi phân rất nhỏ $dt$. 

![Hình 2.28: Biểu diễn hình học của độ biến thiên vận tốc dưới dạng diện tích tích phân](img/young-02/hinh-2-28.png)

**Hình 2.28:** Đồ thị gia tốc theo thời gian $a_x - t$. Mỗi dải chữ nhật hẹp có bề rộng $dt$ và chiều cao $a_x$ có diện tích bằng $a_x dt = dv_x$, biểu diễn độ biến thiên vi phân của vận tốc. Tổng diện tích của tất cả các dải từ $t_1$ đến $t_2$ chính là tích phân xác định, đại diện cho độ biến thiên tổng cộng của vận tốc $\Delta v_x$.

Trong mỗi khoảng vi phân $dt$, gia tốc xem như không đổi, độ biến thiên vận tốc tương ứng là:

$$dv_x = a_x\, dt.$$

Lấy tích phân hai vế từ thời điểm $t_1$ (ứng với vận tốc $v_{1x}$) đến thời điểm $t_2$ (ứng với vận tốc $v_{2x}$):

$$
\begin{aligned}
v_{2x} - v_{1x} &= \int_{v_{1x}}^{v_{2x}} dv_x \\
&= \int_{t_1}^{t_2} a_x\, dt.
\end{aligned}
\tag{2.15}
$$

Ý nghĩa hình học trực quan của công thức (2.15) là: **Độ biến thiên vận tốc $\Delta v_x = v_{2x} - v_{1x}$ giữa hai thời điểm đúng bằng diện tích hình thang cong giới hạn bởi đường cong $a_x(t)$ và trục hoành thời gian từ $t_1$ đến $t_2$** (với phần diện tích nằm phía trên trục hoành mang dấu dương, phần nằm phía dưới mang dấu âm).

---

### Độ dời là tích phân của vận tốc

Hoàn toàn tương tự, xuất phát từ định nghĩa vận tốc tức thời $v_x = dx/dt$, ta có vi phân của độ dời trong khoảng thời gian $dt$ là $dx = v_x\, dt$. 

Tích phân hai vế từ thời điểm $t_1$ (tọa độ $x_1$) đến thời điểm $t_2$ (tọa độ $x_2$):

$$
\begin{aligned}
x_2 - x_1 &= \int_{x_1}^{x_2} dx \\
&= \int_{t_1}^{t_2} v_x\, dt.
\end{aligned}
\tag{2.16}
$$

**Độ dời $\Delta x = x_2 - x_1$ của chất điểm chính là diện tích hình thang cong giới hạn bởi đồ thị vận tốc $v_x(t)$ và trục hoành thời gian từ $t_1$ đến $t_2$**.

Nếu ta chọn thời điểm ban đầu là $t_1 = 0$ với các điều kiện ban đầu $x(0) = x_0$ và $v_x(0) = v_{0x}$, và xét thời điểm tổng quát $t_2 = t$, các công thức (2.15) và (2.16) trở thành dạng tường minh:

$$v_x(t) = v_{0x} + \int_0^t a_x(t')\, dt',\tag{2.17}$$

$$x(t) = x_0 + \int_0^t v_x(t')\, dt'.\tag{2.18}$$

*(Ở đây ta dùng biến tích phân hình thức $t'$ để phân biệt với cận trên $t$).*

::: tip Nhận xét về tính nhất quán của toán học
Nếu gia tốc là hằng số ($a_x = \text{const}$), từ (2.17) ta có ngay:
$$v_x(t) = v_{0x} + a_x \int_0^t dt' = v_{0x} + a_x t \quad \text{(khôi phục chính xác phương trình 2.8)}.$$
Thế kết quả này vào (2.18):
$$x(t) = x_0 + \int_0^t (v_{0x} + a_x t')\, dt' = x_0 + v_{0x}t + \frac{1}{2}a_x t^2 \quad \text{(khôi phục chính xác phương trình 2.12)}.$$
Điều này cho thấy các công thức biến đổi đều ở mục 2.4 chỉ là trường hợp riêng đơn giản nhất của bài toán tích phân tổng quát.
:::

---

### Ví dụ 2.9 — Chuyển động với gia tốc biến thiên tuyến tính

::: exercise Bài toán
Sally lái ô tô dọc theo một tuyến đường cao tốc thẳng tắp. Tại thời điểm ban đầu $t = 0$, xe chạy theo chiều dương của trục $x$ với vận tốc $10.0\,\mathrm{m/s}$ và vừa đi ngang qua cột mốc tọa độ $x = 50.0\,\mathrm m$. Do lực cản không khí tăng dần, gia tốc của ô tô suy giảm tuyến tính theo thời gian theo quy luật:

$$a_x(t) = 2.0\,\mathrm{m/s^2} - (0.10\,\mathrm{m/s^3})t.$$

**(a)** Hãy thiết lập phương trình vận tốc và vị trí của ô tô theo thời gian.
**(b)** Xác định thời điểm mà vận tốc của xe đạt giá trị cực đại.
**(c)** Vận tốc cực đại đó bằng bao nhiêu?
**(d)** Ô tô đang ở tọa độ nào tại thời điểm đạt vận tốc cực đại?
:::

::: solution Lời giải
**Nhận diện và Thiết lập:**
Gia tốc phụ thuộc vào thời gian nên đây là chuyển động biến đổi không đều. Ta phải sử dụng công thức tích phân (2.17) và (2.18).
Các điều kiện ban đầu đã cho:
- Tại $t = 0$: $x_0 = 50.0\,\mathrm m$, $v_{0x} = 10.0\,\mathrm{m/s}$.
- Biểu thức gia tốc: $a_x(t) = 2.0 - 0.10t$ (đơn vị SI).

**Triển khai tính toán:**

**(a) Tìm hàm vận tốc và vị trí:**
Áp dụng công thức tích phân (2.17):

$$
\begin{aligned}
v_x(t) &= v_{0x} + \int_0^t a_x(t')\, dt' \\
&= 10.0\,\mathrm{m/s} + \int_0^t \left( 2.0\,\mathrm{m/s^2} - 0.10\,\mathrm{m/s^3}\, t' \right) dt' \\
&= 10.0\,\mathrm{m/s} + (2.0\,\mathrm{m/s^2})t - \frac{1}{2}(0.10\,\mathrm{m/s^3})t^2 \\
&= 10.0 + 2.0t - 0.050t^2 \quad (\text{m/s}).
\end{aligned}
$$

Tiếp tục lấy tích phân hàm vận tốc theo công thức (2.18) để tìm vị trí $x(t)$:

$$
\begin{aligned}
x(t) &= x_0 + \int_0^t v_x(t')\, dt' \\
&= 50.0\,\mathrm m + \int_0^t \left( 10.0 + 2.0t' - 0.050{t'}^2 \right) dt' \\
&= 50.0 + 10.0t + \frac{1}{2}(2.0)t^2 - \frac{1}{3}(0.050)t^3 \\
&= 50.0 + 10.0t + 1.0t^2 - \frac{1}{60}t^3 \quad (\text{m}).
\end{aligned}
$$

**(b) Thời điểm vận tốc đạt cực đại:**
Một hàm số đạt cực trị khi đạo hàm của nó triệt tiêu. Vì $dv_x/dt = a_x$, nên vận tốc đạt cực đại đúng vào thời điểm gia tốc bằng 0:

$$a_x(t) = 2.0\,\mathrm{m/s^2} - (0.10\,\mathrm{m/s^3})t = 0 \implies t = \frac{2.0\,\mathrm{m/s^2}}{0.10\,\mathrm{m/s^3}} = 20.0\,\mathrm s.$$

*Ý nghĩa vật lý:* Trong $20\,\mathrm s$ đầu tiên, $a_x > 0$ và cùng dấu với $v_x$, nên ô tô chuyển động nhanh dần và vận tốc liên tục tăng. Sau thời điểm $t = 20\,\mathrm s$, gia tốc đổi dấu sang âm ($a_x < 0$), trở thành gia tốc hãm khiến vận tốc bắt đầu giảm. Do đó $t = 20.0\,\mathrm s$ chính là mốc vận tốc đạt đỉnh cao nhất.

**(c) Giá trị vận tốc cực đại:**
Thay $t = 20.0\,\mathrm s$ vào biểu thức vận tốc $v_x(t)$:

$$v_{\max-x} = 10.0 + 2.0(20.0) - 0.050(20.0)^2 = 10.0 + 40.0 - 20.0 = 30.0\,\mathrm{m/s} \quad (= 108\,\mathrm{km/h}).$$

**(d) Tọa độ của xe khi đạt vận tốc cực đại:**
Thay $t = 20.0\,\mathrm s$ vào biểu thức vị trí $x(t)$:

$$
\begin{aligned}
x(20.0\,\mathrm s) &= 50.0 + 10.0(20.0) + 1.0(20.0)^2 - \frac{1}{60}(20.0)^3 \\
&= 50.0 + 200.0 + 400.0 - \frac{8000}{60} \\
&= 650.0 - 133.3 \approx 517\,\mathrm m.
\end{aligned}
$$

Xe cách mốc ban đầu hơn nửa cây số.
:::

![Hình 2.29: Bộ ba đồ thị gia tốc, vận tốc và vị trí theo thời gian của ô tô](img/young-02/hinh-2-29.png)

**Hình 2.29:** Phân tích mối quan hệ giữa ba đồ thị $a_x(t)$, $v_x(t)$ và $x(t)$:
- Đồ thị gia tốc $a_x(t)$ là đường thẳng dốc xuống, cắt trục hoành tại $t = 20\,\mathrm s$.
- Đồ thị vận tốc $v_x(t)$ là parabol có bề lõm quay xuống, đạt đỉnh cực đại tại $t = 20\,\mathrm s$ với tiếp tuyến nằm ngang ($a_x = 0$).
- Đồ thị tọa độ $x(t)$ là đường cong bậc ba có độ dốc tăng dần từ $0$ đến $20\,\mathrm s$ (đoạn uốn lõm lên), đạt độ dốc lớn nhất tại $t = 20\,\mathrm s$, sau đó độ dốc giảm dần (đoạn uốn cong xuống). Điểm $t = 20\,\mathrm s$ chính là **điểm uốn** của đồ thị vị trí $x(t)$!

*Một câu hỏi tư duy thú vị:* Nếu chiếc xe tiếp tục chuyển động theo các quy luật trên thì sau bao lâu xe sẽ dừng hẳn tức thời? 
Xe dừng lại khi $v_x = 0$, tức là $10.0 + 2.0t - 0.050t^2 = 0 \iff t^2 - 40t - 200 = 0$. Phương trình cho nghiệm dương $t = 20 + \sqrt{600} \approx 44.5\,\mathrm s$. Vậy tại thời điểm $44.5\,\mathrm s$, chiếc xe sẽ tạm dừng lại trước khi bắt đầu lùi về sau!

---

### Câu hỏi kiểm tra hiểu bài

::: exercise Câu hỏi kiểm tra
Nếu gia tốc $a_x$ của một chất điểm chuyển động dọc theo trục $x$ luôn dương và tăng dần theo thời gian, thì hình dạng của đồ thị vận tốc $v_x$ theo thời gian sẽ là:
**(i)** Một đường thẳng dốc lên.
**(ii)** Một đường cong uốn lõm lên trên (độ dốc tăng dần).
**(iii)** Một đường cong uốn vồng xuống dưới (độ dốc giảm dần).
:::

::: solution Lời giải & Phân tích
**Chọn (ii): Đường cong uốn lõm lên trên.**
Hệ số góc (độ dốc) của tiếp tuyến tại mỗi điểm trên đồ thị vận tốc $v_x(t)$ chính là gia tốc tức thời $a_x = dv_x/dt$.
Nếu gia tốc $a_x > 0$ và liên tục tăng theo thời gian, điều đó có nghĩa là độ dốc của đồ thị vận tốc phải ngày càng dốc đứng hơn khi thời gian trôi đi. Hình dạng hình học của một đường có độ dốc tăng dần chính là đường cong uốn lõm lên trên. 
(Nếu gia tốc không đổi, đồ thị mới là đường thẳng dốc lên ứng với đáp án (i); nếu gia tốc giảm dần về 0, đồ thị mới là đường cong vồng xuống ứng với đáp án (iii)).
:::
