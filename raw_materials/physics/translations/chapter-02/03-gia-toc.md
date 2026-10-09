<!-- Nguồn: mục 2.3, trang in 40–44, trang PDF 60–64; công thức 2.4–2.6, Ví dụ 2.2–2.3, Hình 2.10–2.14, Bảng 2.3–2.4, câu hỏi và đáp án. -->

## 2.3. Gia tốc trung bình và gia tốc tức thời

Vận tốc mô tả vị trí thay đổi theo thời gian, còn **gia tốc** mô tả vận tốc thay đổi theo thời gian. Gia tốc cũng là vector. Trong chuyển động thẳng, thành phần khác không của nó chỉ theo đường ấy. Trong đời thường, “có gia tốc” thường được hiểu là nhanh dần. Trong vật lý, nó bao gồm mọi biến thiên vận tốc: vật nhanh dần hoặc chậm dần đều có gia tốc.

### Gia tốc trung bình

Xét chất điểm trên trục $x$. Tại $t_1$, nó ở $P_1$ và có thành phần vận tốc tức thời $v_{1x}$. Tại $t_2$ muộn hơn, nó ở $P_2$ và có $v_{2x}$. Độ biến thiên vận tốc là $\Delta v_x=v_{2x}-v_{1x}$ trong khoảng $\Delta t=t_2-t_1$.

**Gia tốc trung bình** là vector có thành phần $x$, ký hiệu $a_{\mathrm{av}-x}$, bằng độ biến thiên vận tốc chia thời gian:

$$a_{\mathrm{av}-x}=\frac{\Delta v_x}{\Delta t}
=\frac{v_{2x}-v_{1x}}{t_2-t_1}.\tag{2.4}$$

Trong chuyển động thẳng theo $x$, thường gọi ngắn đây là gia tốc trung bình. Chương 3 sẽ xét các thành phần khác. Nếu vận tốc bằng mét trên giây và thời gian bằng giây, gia tốc có đơn vị mét trên giây mỗi giây, viết $\mathrm{m/s^2}$ và đọc là mét trên giây bình phương.

::: warning Không lẫn vận tốc với gia tốc
Vận tốc mô tả vị trí biến thiên, cho biết nhanh chậm và hướng chuyển động. Gia tốc mô tả vận tốc biến thiên, cho biết tốc độ và hướng thay đổi thế nào. Một điểm khác là ta có thể cảm nhận gia tốc nhưng không trực tiếp cảm nhận vận tốc không đổi. Ngồi trong xe gia tốc về trước và nhanh dần, bạn cảm thấy bị đẩy ra sau ghế. Khi xe có gia tốc về sau và chậm dần, bạn cảm thấy bị đẩy về trước. Nếu vận tốc giữ nguyên, không có gia tốc, bạn không có các cảm giác ấy. Chương 4 sẽ giải thích.
:::

### Ví dụ 2.2 — Gia tốc trung bình

::: exercise Đề bài trong sách
Một phi hành gia rời tàu trên quỹ đạo để thử thiết bị cơ động cá nhân mới. Người ấy chuyển động trên đường thẳng; đồng đội trên tàu đo vận tốc mỗi $2.0\,\mathrm s$, bắt đầu ở $t=1.0\,\mathrm s$:

| Thời gian, s | Vận tốc x, m/s | Thời gian, s | Vận tốc x, m/s |
| --- | --- | --- | --- |
| $1.0$ | $0.8$ | $9.0$ | $-0.4$ |
| $3.0$ | $1.2$ | $11.0$ | $-1.0$ |
| $5.0$ | $1.6$ | $13.0$ | $-1.6$ |
| $7.0$ | $1.2$ | $15.0$ | $-0.8$ |

Tìm gia tốc trung bình và cho biết tốc độ tăng hay giảm trên các khoảng: **(a)** $1.0$–$3.0\,\mathrm s$; **(b)** $5.0$–$7.0\,\mathrm s$; **(c)** $9.0$–$11.0\,\mathrm s$; **(d)** $13.0$–$15.0\,\mathrm s$.
:::

![Hình 2.10 nguyên tác: đồ thị vận tốc theo thời gian và các giá trị gia tốc trung bình của phi hành gia](img/young-02/hinh-2-10.png)

**Hình 2.10:** Phần trên là đồ thị $v_x$–$t$, phần dưới biểu diễn gia tốc trung bình trong bốn khoảng. Độ dốc đoạn nối hai đầu mỗi khoảng bằng gia tốc trung bình trong khoảng ấy. Các khoảng (a), (b), (c), (d) được đánh dấu tương ứng.

::: solution Lời giải của sách
**Xác định và thiết lập.** Dùng (2.4) tính gia tốc từ độ biến thiên vận tốc. Tốc độ là độ lớn vận tốc tức thời, nên xét giá trị tuyệt đối vận tốc để biết nhanh hay chậm.

Trên phần trên Hình 2.10, độ dốc đoạn nối hai đầu mỗi khoảng bằng $\Delta v_x/\Delta t$. Từ trái sang phải, bốn độ dốc có dấu dương, âm, âm, dương. Hai độ dốc sau lớn hơn về giá trị tuyệt đối so với hai độ dốc đầu.

**Thực hiện.**

**(a)**
$$a_{\mathrm{av}-x}=\frac{1.2-0.8}{3.0-1.0}\,\mathrm{m/s^2}=0.2\,\mathrm{m/s^2}.$$
Tốc độ tăng từ $0.8$ lên $1.2\,\mathrm{m/s}$.

**(b)**
$$a_{\mathrm{av}-x}=\frac{1.2-1.6}{7.0-5.0}\,\mathrm{m/s^2}=-0.2\,\mathrm{m/s^2}.$$
Tốc độ giảm từ $1.6$ xuống $1.2\,\mathrm{m/s}$.

**(c)**
$$a_{\mathrm{av}-x}=\frac{-1.0-(-0.4)}{11.0-9.0}\,\mathrm{m/s^2}=-0.3\,\mathrm{m/s^2}.$$
Tốc độ tăng từ $0.4$ lên $1.0\,\mathrm{m/s}$.

**(d)**
$$a_{\mathrm{av}-x}=\frac{-0.8-(-1.6)}{15.0-13.0}\,\mathrm{m/s^2}=0.4\,\mathrm{m/s^2}.$$
Tốc độ giảm từ $1.6$ xuống $0.8\,\mathrm{m/s}$. Phần dưới Hình 2.10 vẽ các kết quả gia tốc.

**Đánh giá.** Dấu và độ lớn tương đối phù hợp dự đoán từ đồ thị. Ở các khoảng (a), (c), gia tốc trung bình cùng dấu vận tốc đầu nên phi hành gia nhanh lên. Ở (b), (d), hai dấu ngược nhau nên chậm lại. Gia tốc dương làm nhanh dần khi vận tốc dương, nhưng làm chậm dần khi vận tốc âm. Gia tốc âm làm nhanh dần khi vận tốc âm, nhưng làm chậm dần khi vận tốc dương.

**Ý chính của ví dụ:** Tính gia tốc trung bình bằng vận tốc cuối trừ đầu, rồi chia khoảng thời gian.
:::

### Gia tốc tức thời

Ta định nghĩa gia tốc tức thời bằng cách tương tự vận tốc tức thời. Với xe đua Grand Prix đi trên đường thẳng ở Hình 2.11, muốn xác định gia tốc tại $P_1$, đưa $P_2$ càng gần $P_1$ để tính gia tốc trung bình trên khoảng thời gian càng ngắn. Giới hạn là:

$$a_x=\lim_{\Delta t\to0}\frac{\Delta v_x}{\Delta t}
=\frac{dv_x}{dt}.\tag{2.5}$$

Đây là thành phần $x$ của gia tốc, hay gia tốc tức thời theo $x$, bằng tốc độ biến thiên tức thời của vận tốc. Trong chuyển động thẳng, các thành phần khác bằng không. Từ đây, từ “gia tốc” không kèm “trung bình” được hiểu là tức thời.

![Hình 2.11 nguyên tác: xe Grand Prix ở hai vị trí trên đường thẳng](img/young-02/hinh-2-11.png)

**Hình 2.11:** Xe tại $P_1$, $P_2$ có tốc độ $v_1$, $v_2$ và các thành phần vận tốc $v_{1x}$, $v_{2x}$. Gốc O và trục x được đánh dấu.

### Ví dụ 2.3 — Gia tốc trung bình và tức thời

::: exercise Đề bài trong sách
Vận tốc $x$ của xe ở Hình 2.11 được cho bởi:

$$v_x=60\,\mathrm{m/s}+(0.50\,\mathrm{m/s^3})t^2.$$

**(a)** Tìm độ biến thiên vận tốc từ $t_1=1.0\,\mathrm s$ tới $t_2=3.0\,\mathrm s$.

**(b)** Tìm gia tốc trung bình trên khoảng ấy.

**(c)** Tìm gia tốc tức thời tại $t_1=1.0\,\mathrm s$ bằng cách lần lượt lấy $\Delta t=0.1$, $0.01$, $0.001\,\mathrm s$.

**(d)** Lập biểu thức gia tốc tức thời theo thời gian, rồi tìm $a_x$ tại $t=1.0$ và $3.0\,\mathrm s$.
:::

::: solution Lời giải của sách
**Xác định và thiết lập.** Ví dụ tương tự Ví dụ 2.1: ở đó lấy độ biến thiên vị trí chia thời gian để tìm vận tốc trung bình, rồi đạo hàm vị trí để tìm vận tốc tức thời. Ở đây dùng (2.4) cho độ biến thiên vận tốc chia thời gian và (2.5) cho đạo hàm vận tốc.

**Thực hiện (a).** Trước khi dùng (2.4), tính vận tốc ở hai thời điểm:

$$
\begin{aligned}
v_{1x}&=60\,\mathrm{m/s}+(0.50\,\mathrm{m/s^3})(1.0\,\mathrm s)^2=60.5\,\mathrm{m/s},\\
v_{2x}&=60\,\mathrm{m/s}+(0.50\,\mathrm{m/s^3})(3.0\,\mathrm s)^2=64.5\,\mathrm{m/s}.
\end{aligned}
$$

Do đó $\Delta v_x=64.5-60.5=4.0\,\mathrm{m/s}$.

**(b)** Khoảng thời gian $2.0\,\mathrm s$ cho:

$$a_{\mathrm{av}-x}=\frac{4.0\,\mathrm{m/s}}{2.0\,\mathrm s}
=2.0\,\mathrm{m/s^2}.$$

Vận tốc và gia tốc trung bình đều dương, nên xe nhanh dần trong khoảng này.

**(c)** Với $\Delta t=0.1\,\mathrm s$, thời điểm cuối mới $t_2=1.1\,\mathrm s$:

$$v_{2x}=60\,\mathrm{m/s}+(0.50\,\mathrm{m/s^3})(1.1\,\mathrm s)^2
=60.605\,\mathrm{m/s}.$$

Vì $\Delta v_x=0.105\,\mathrm{m/s}$, ta có:

$$a_{\mathrm{av}-x}=\frac{0.105\,\mathrm{m/s}}{0.1\,\mathrm s}
=1.05\,\mathrm{m/s^2}.$$

Làm tương tự với $0.01$ và $0.001\,\mathrm s$, kết quả lần lượt $1.005$ và $1.0005\,\mathrm{m/s^2}$. Chúng tiến tới $1.0\,\mathrm{m/s^2}$ khi khoảng thời gian giảm, nên đó là gia tốc tức thời tại $1.0\,\mathrm s$.

**(d)**

$$
\begin{aligned}
a_x&=\frac{dv_x}{dt}
=\frac{d}{dt}[60\,\mathrm{m/s}+(0.50\,\mathrm{m/s^3})t^2]\\
&=(0.50\,\mathrm{m/s^3})(2t)
=(1.0\,\mathrm{m/s^3})t.
\end{aligned}
$$

Ở $1.0\,\mathrm s$, $a_x=1.0\,\mathrm{m/s^2}$; ở $3.0\,\mathrm s$, $a_x=3.0\,\mathrm{m/s^2}$.

**Đánh giá.** Không giá trị nào ở (d) bằng gia tốc trung bình của (b), vì gia tốc tức thời thay đổi theo thời gian. Tốc độ biến thiên gia tốc theo thời gian đôi khi được gọi là *jerk*.

**Ý chính của ví dụ:** Gia tốc tức thời, giới hạn gia tốc trung bình trên khoảng thời gian vô cùng ngắn, bằng đạo hàm vận tốc theo thời gian.
:::

### Gia tốc trên đồ thị vận tốc–thời gian

Tương tự cách đọc vận tốc ở mục 2.2, đồ thị vận tốc tức thời $v_x$ theo $t$ cho thông tin gia tốc, như Hình 2.12. Điểm $p_1$, $p_2$ tương ứng $P_1$, $P_2$ của Hình 2.11. Gia tốc trung bình $\Delta v_x/\Delta t$ bằng độ dốc dây cung $p_1p_2$.

Khi $P_2$ tiến về $P_1$, dây cung trên đồ thị tiến tới tiếp tuyến tại $p_1$. Vì vậy gia tốc tức thời bằng độ dốc tiếp tuyến trên đồ thị $v_x$–$t$. Các tiếp tuyến ở những điểm khác nhau trong Hình 2.12 có độ dốc khác nhau, nên gia tốc biến thiên theo thời gian.

![Hình 2.12 nguyên tác: độ dốc dây cung và tiếp tuyến trên đồ thị vận tốc](img/young-02/hinh-2-12.png)

**Hình 2.12:** Trục đứng là $v_x$, trục ngang là $t$. Độ tăng đứng $\Delta v_x=v_{2x}-v_{1x}$ và độ tăng ngang $\Delta t=t_2-t_1$ xác định gia tốc trung bình. Độ dốc tiếp tuyến tại một điểm xác định gia tốc tức thời ở điểm ấy.

::: warning Dấu gia tốc và dấu vận tốc
Chỉ dấu gia tốc chưa cho biết nhanh dần hay chậm dần. Phải so với dấu vận tốc: cùng dấu thì tốc độ tăng, trái dấu thì tốc độ giảm. Bảng 2.3 và Hình 2.13 minh họa quy tắc này.
:::

Từ “deceleration” đôi khi được dùng cho sự giảm tốc độ. Vì nó có thể ứng với gia tốc dương hoặc âm tùy vận tốc, sách tránh sử dụng từ này như một dấu xác định của gia tốc.

### Bảng 2.3 — Quy tắc dấu của gia tốc theo trục x

| Vận tốc x | Gia tốc x và diễn biến |
| --- | --- |
| Dương và tăng | Gia tốc dương; đi theo $+x$, nhanh dần. |
| Dương và giảm | Gia tốc âm; đi theo $+x$, chậm dần. |
| Âm và tăng, bớt âm | Gia tốc dương; đi theo $-x$, chậm dần. |
| Âm và giảm, càng âm | Gia tốc âm; đi theo $-x$, nhanh dần. |

Quy tắc dùng cho cả gia tốc trung bình và tức thời trong những khoảng và thời điểm tương ứng.

![Hình 2.13 nguyên tác: đồ thị vận tốc và sơ đồ vị trí, vận tốc, gia tốc tại các điểm A–E](img/young-02/hinh-2-13.png)

**Hình 2.13:** Trên đồ thị $v_x$–$t$, độ dốc bằng gia tốc. Độ dốc càng lớn về giá trị tuyệt đối, gia tốc theo chiều dương hoặc âm càng lớn. Sơ đồ chuyển động ở (b) ứng với một chất điểm khác chất điểm Hình 2.8:

- A: $v_x<0$, $a_x>0$, vật đi theo $-x$ và chậm dần.
- B: $v_x=0$, $a_x>0$, vật đứng yên tức thời và sắp đi theo $+x$.
- C: $v_x>0$, $a_x=0$, tốc độ tức thời không đổi.
- D: $v_x=0$, $a_x<0$, vật đứng yên tức thời và sắp đi theo $-x$.
- E: $v_x<0$, $a_x<0$, vật đi theo $-x$ và nhanh dần.

### Gia tốc trên đồ thị vị trí–thời gian

Vì $v_x=dx/dt$ và $a_x=dv_x/dt$, ta có:

$$a_x=\frac{dv_x}{dt}
=\frac{d}{dt}\left(\frac{dx}{dt}\right)
=\frac{d^2x}{dt^2}.\tag{2.6}$$

Gia tốc là đạo hàm bậc hai của vị trí theo thời gian. Đạo hàm bậc hai liên hệ với chiều cong của đồ thị. Nơi đồ thị $x$–$t$ cong lên, như A và E của Hình 2.14a, gia tốc dương và vận tốc tăng. Nơi cong xuống, như C, gia tốc âm và vận tốc giảm. Ở các điểm uốn B, D, nơi độ cong bằng không, gia tốc bằng không và vận tốc không thay đổi tức thời.

Quan sát chiều cong là cách thuận tiện để xác định dấu gia tốc. Nó kém thuận tiện hơn khi cần giá trị bằng số vì khó đo độ cong chính xác.

![Hình 2.14 nguyên tác: đồ thị vị trí của Hình 2.8 cùng sơ đồ vận tốc và gia tốc](img/young-02/hinh-2-14.png)

**Hình 2.14:** (a) Cùng đồ thị $x$–$t$ với Hình 2.8a. (b) Vị trí, vận tốc và gia tốc tại các thời điểm đánh dấu:

- A: $x<0$, $v_x>0$, $a_x>0$; đi theo $+x$ và nhanh dần.
- B: $x=0$, $v_x>0$, $a_x=0$; tốc độ tức thời không thay đổi.
- C: $x>0$, $v_x=0$, $a_x<0$; đứng yên tức thời, sắp đi theo $-x$.
- D: $x>0$, $v_x<0$, $a_x=0$; tốc độ tức thời không thay đổi.
- E: $x>0$, $v_x<0$, $a_x>0$; đi theo $-x$ và chậm dần.

Nhãn trong hình nhắc rằng chiều cong của đồ thị vị trí cho dấu gia tốc; độ cong càng lớn về mức dương hoặc âm thì gia tốc tương ứng càng lớn.

### Bảng 2.4 — Thông tin từ hai loại đồ thị

| Thông tin xét tại một thời điểm | Đồ thị x–t | Đồ thị vₓ–t |
| --- | --- | --- |
| Giá trị của đường đồ thị | Tọa độ $x$. | Vận tốc $v_x$. |
| Độ dốc | Vận tốc $v_x$. | Gia tốc $a_x$. |
| Chiều cong hoặc độ cong | Gia tốc $a_x$. | Cho biết gia tốc có đang thay đổi hay không. |

Bảng tập hợp những điều có thể đọc từ đồ thị của chất điểm chuyển động thẳng.

### Câu hỏi kiểm tra hiểu mục 2.3

::: exercise Câu hỏi trong sách
Xem lại đồ thị $x$–$t$ ở Hình 2.9.

**(a)** Điểm P, Q, R, S nào có $a_x>0$?

**(b)** Điểm nào có $a_x<0$?

**(c)** Điểm nào có vẻ có $a_x=0$?

**(d)** Ở mỗi điểm, vận tốc tăng, giảm hay không thay đổi?
:::

::: solution Đáp án của sách
**(a)** S, vì đồ thị cong lên.

**(b)** Q, vì đồ thị cong xuống.

**(c)** P và R, vì đồ thị không cong lên hoặc xuống ở đó.

**(d)** P: $a_x=0$, vận tốc không thay đổi tức thời. Q: $a_x<0$, vận tốc giảm từ dương tới không rồi âm. R: $a_x=0$, vận tốc không thay đổi tức thời. S: $a_x>0$, vận tốc tăng từ âm tới không rồi dương.
:::
