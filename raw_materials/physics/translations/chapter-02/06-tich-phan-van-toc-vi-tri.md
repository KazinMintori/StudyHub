<!-- Nguồn: mục 2.6, trang in 53–55, trang PDF 73–75; đầy đủ cách suy ra tích phân, công thức 2.15–2.18, Hình 2.26–2.29, Ví dụ 2.9 và câu hỏi. -->

## 2.6. Tìm vận tốc và vị trí bằng tích phân

Mục này dành cho người đã biết một ít tích phân. Mục 2.4 xét trường hợp gia tốc không đổi. Khi gia tốc thay đổi, như thường gặp, các công thức của mục ấy không còn dùng được. Tuy vậy, nếu biết vị trí theo thời gian, vẫn đạo hàm $v_x=dx/dt$ để tìm vận tốc. Nếu biết vận tốc theo thời gian, vẫn dùng $a_x=dv_x/dt$ để tìm gia tốc.

![Hình 2.26 nguyên tác: người lái đạp hết bàn đạp ga của ô tô](img/young-02/hinh-2-26.png)

**Hình 2.26:** Đạp hết bàn đạp ga không tạo gia tốc cố định: tốc độ càng cao, xe càng chậm tăng thêm tốc độ. Theo ví dụ điển hình trong sách, xe thường cần thời gian gấp đôi để tăng từ $50$ lên $100\,\mathrm{km/h}$ so với từ $0$ lên $50\,\mathrm{km/h}$.

Nhiều tình huống chưa biết vị trí và vận tốc theo thời gian, nhưng biết gia tốc. Cần tìm vị trí, vận tốc từ hàm $a_x(t)$ như thế nào?

![Hình 2.27 nguyên tác: máy bay chở khách có hệ thống dẫn đường quán tính](img/young-02/hinh-2-27.png)

**Hình 2.27:** Hệ thống dẫn đường quán tính, INS, trên máy bay đường dài theo dõi gia tốc. Biết vị trí và vận tốc đầu trước khi cất cánh, INS dùng số liệu gia tốc để tính vị trí và vận tốc trong suốt chuyến bay.

### Độ biến thiên vận tốc là tích phân của gia tốc

Hình 2.28 là đồ thị gia tốc không cố định. Chia khoảng từ $t_1$ tới $t_2$ thành nhiều khoảng nhỏ, mỗi khoảng điển hình dài $\Delta t$, gia tốc trung bình trong đó là $a_{\mathrm{av}-x}$. Theo (2.4):

$$\Delta v_x=a_{\mathrm{av}-x}\Delta t.$$

Về hình học, đó là diện tích dải tô cao $a_{\mathrm{av}-x}$, rộng $\Delta t$, tức diện tích dưới đường cong trong khoảng nhỏ. Tổng độ biến thiên vận tốc bằng tổng những độ biến thiên nhỏ, nên được biểu diễn bằng toàn bộ diện tích dưới đồ thị gia tốc từ $t_1$ tới $t_2$. Mục 2.4 đã cho kết quả này khi gia tốc cố định.

Khi mọi khoảng nhỏ tiến tới không và số khoảng tăng lên, gia tốc trung bình trên khoảng từ $t$ tới $t+\Delta t$ tiến tới gia tốc tức thời $a_x(t)$. Tổng diện tích trở thành tích phân. Nếu $v_{1x}$, $v_{2x}$ là vận tốc tại hai đầu:

$$\begin{aligned}
v_{2x}-v_{1x}&=\int_{v_{1x}}^{v_{2x}}dv_x\\
&=\int_{t_1}^{t_2}a_x\,dt.
\end{aligned}\tag{2.15}$$

Độ biến thiên vận tốc là tích phân theo thời gian của gia tốc.

![Hình 2.28 nguyên tác: dải diện tích trên đồ thị gia tốc biến thiên](img/young-02/hinh-2-28.png)

**Hình 2.28:** Đồ thị có trục đứng $a_x$, trục ngang $t$. Dải tô cao $a_{\mathrm{av}-x}$, rộng $\Delta t$, diện tích bằng $\Delta v_x$. Toàn bộ diện tích từ $t_1$ tới $t_2$ cho độ biến thiên vận tốc ròng.

Hai câu trong hình được dịch đầy đủ là: “Diện tích dải này bằng $\Delta v_x$, tức độ biến thiên vận tốc theo trục $x$ trong khoảng $\Delta t$” và “Tổng diện tích dưới đồ thị từ $t_1$ đến $t_2$ bằng độ biến thiên ròng của vận tốc theo trục $x$ giữa hai thời điểm ấy”. Nguyên tác in nhầm “đồ thị $x$–$t$” trong câu thứ hai; đúng theo trục của hình phải là đồ thị $a_x$–$t$.

### Độ dời là tích phân của vận tốc

Làm tương tự với đồ thị vận tốc. Nếu vị trí tại $t_1,t_2$ là $x_1,x_2$, trong khoảng nhỏ $\Delta t$, theo (2.2), độ dời $\Delta x=v_{\mathrm{av}-x}\Delta t$. Cộng các khoảng nhỏ và lấy giới hạn:

$$\begin{aligned}
x_2-x_1&=\int_{x_1}^{x_2}dx\\
&=\int_{t_1}^{t_2}v_x\,dt.
\end{aligned}\tag{2.16}$$

Độ dời là tích phân vận tốc theo thời gian, hay diện tích dưới đồ thị vận tốc giữa hai thời điểm. Kết quả khớp trường hợp đặc biệt ở mục 2.4 khi vận tốc theo (2.8).

Lấy $t_1=0$, $t_2=t$, vị trí và vận tốc đầu là $x_0,v_{0x}$, có thể viết:

$$v_x=v_{0x}+\int_0^t a_x\,dt,\tag{2.17}$$

$$x=x_0+\int_0^t v_x\,dt.\tag{2.18}$$

Biết hàm gia tốc và vận tốc đầu, dùng (2.17) tìm vận tốc tại mọi thời điểm. Sau đó, biết vị trí đầu, dùng (2.18) tìm vị trí.

### Ví dụ 2.9 — Chuyển động với gia tốc biến thiên

::: exercise Đề bài trong sách
Sally lái xe trên đường cao tốc thẳng. Tại $t=0$, cô đi theo $+x$ với $10\,\mathrm{m/s}$ và qua biển ở $x=50\,\mathrm m$. Gia tốc theo thời gian là:

$$a_x=2.0\,\mathrm{m/s^2}-(0.10\,\mathrm{m/s^3})t.$$

**(a)** Tìm vận tốc và vị trí theo thời gian.

**(b)** Khi nào vận tốc $x$ lớn nhất?

**(c)** Giá trị lớn nhất đó bằng bao nhiêu?

**(d)** Xe ở đâu khi đạt vận tốc ấy?
:::

::: solution Lời giải của sách
**Xác định và thiết lập.** Gia tốc biến thiên nên không dùng công thức cố định ở mục 2.4. Dùng (2.17) tìm hàm vận tốc, rồi (2.18) tìm hàm vị trí. Các hàm cho phép trả lời nhiều câu hỏi về chuyển động.

**Thực hiện (a).** $x_0=50\,\mathrm m$, $v_{0x}=10\,\mathrm{m/s}$. Với $n\ne-1$, nguyên hàm của $t^n$ là $t^{n+1}/(n+1)$. Vì vậy:

$$
\begin{aligned}
v_x&=10\,\mathrm{m/s}
+\int_0^t[2.0\,\mathrm{m/s^2}-(0.10\,\mathrm{m/s^3})t]dt\\
&=10\,\mathrm{m/s}+(2.0\,\mathrm{m/s^2})t
-\frac12(0.10\,\mathrm{m/s^3})t^2.
\end{aligned}
$$

Tiếp theo:

$$
\begin{aligned}
x&=50\,\mathrm m+\int_0^t[10\,\mathrm{m/s}+(2.0\,\mathrm{m/s^2})t\\
&\qquad-\tfrac12(0.10\,\mathrm{m/s^3})t^2]dt\\
&=50\,\mathrm m+(10\,\mathrm{m/s})t
+\frac12(2.0\,\mathrm{m/s^2})t^2\\
&\qquad-\frac16(0.10\,\mathrm{m/s^3})t^3.
\end{aligned}
$$

Hình 2.29 vẽ các hàm gia tốc, vận tốc, vị trí. Tại mỗi thời điểm, độ dốc đồ thị vận tốc bằng gia tốc, độ dốc đồ thị vị trí bằng vận tốc.

**(b)** Vận tốc lớn nhất khi ngừng tăng và bắt đầu giảm, tức $dv_x/dt=a_x=0$:

$$0=2.0\,\mathrm{m/s^2}-(0.10\,\mathrm{m/s^3})t,$$

$$t=\frac{2.0\,\mathrm{m/s^2}}{0.10\,\mathrm{m/s^3}}=20\,\mathrm s.$$

**(c)** Thay vào hàm vận tốc:

$$v_{\max-x}=10\,\mathrm{m/s}+(2.0\,\mathrm{m/s^2})(20\,\mathrm s)
-\frac12(0.10\,\mathrm{m/s^3})(20\,\mathrm s)^2
=30\,\mathrm{m/s}.$$

**(d)** Thay vào hàm vị trí:

$$
\begin{aligned}
x&=50\,\mathrm m+(10\,\mathrm{m/s})(20\,\mathrm s)
+\frac12(2.0\,\mathrm{m/s^2})(20\,\mathrm s)^2\\
&\quad-\frac16(0.10\,\mathrm{m/s^3})(20\,\mathrm s)^3
\approx517\,\mathrm m.
\end{aligned}
$$

**Đánh giá.** Gia tốc dương từ $0$ tới $20\,\mathrm s$, âm sau đó, bằng không lúc vận tốc đạt đỉnh. Xe nhanh dần trước thời điểm ấy vì vận tốc và gia tốc cùng dấu, rồi chậm dần sau đó khi chúng trái dấu, trong khoảng đồ thị đang xét.

Vì vận tốc cực đại ở $20\,\mathrm s$, đồ thị vị trí có độ dốc dương lớn nhất tại đó. Đường vị trí cong lên trước $20\,\mathrm s$ vì gia tốc dương, cong xuống sau đó vì gia tốc âm.

**Ý chính của ví dụ:** Biết gia tốc theo thời gian dù không cố định, có thể tích phân để tìm vận tốc và vị trí theo thời gian.
:::

![Hình 2.29 nguyên tác: ba đồ thị gia tốc, vận tốc và vị trí của xe Sally](img/young-02/hinh-2-29.png)

**Hình 2.29:** Từ trái sang phải là $a_x(t)$, $v_x(t)$, $x(t)$. Gia tốc dương trước $20\,\mathrm s$, âm sau; vận tốc tăng rồi giảm; vị trí cong lên rồi cong xuống. Trục thời gian ghi giây, các trục đứng lần lượt ghi $\mathrm{m/s^2}$, $\mathrm{m/s}$, $\mathrm m$. Câu hỏi kèm hình của sách: Nếu chuyển động tiếp tục theo các hàm này, bạn có thể chỉ ra xe dừng tại $t=44.5\,\mathrm s$ không?

### Câu hỏi kiểm tra hiểu mục 2.6

::: exercise Câu hỏi trong sách
Nếu gia tốc $a_x$ của vật chuyển động thẳng tăng theo thời gian, đồ thị $v_x$–$t$ là: **(i)** đường thẳng; **(ii)** cong lên; hay **(iii)** cong xuống?
:::

::: solution Đáp án của sách
Chọn **(ii)**. Gia tốc bằng độ dốc đồ thị vận tốc. Nếu gia tốc tăng, độ dốc tăng, nên đường cong hướng lên.
:::
