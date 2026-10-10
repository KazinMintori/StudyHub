## 2.3. Gia tốc trung bình và gia tốc tức thời

Nếu vận tốc mô tả tốc độ thay đổi của tọa độ vị trí theo thời gian, thì **gia tốc** (*acceleration*) mô tả tốc độ thay đổi của chính vận tốc theo thời gian.

Trong ngôn ngữ giao tiếp hằng ngày, người ta thường dùng từ "gia tốc" hay "tăng tốc" với hàm ý chuyển động nhanh dần lên, còn khi xe hãm phanh thì gọi là "giảm tốc". Nhưng trong cơ học vật lý chuẩn tắc, khái niệm **gia tốc** bao trùm mọi sự biến thiên của vector vận tốc: Dù vật chạy nhanh lên, chạy chậm lại, hay đổi hướng chuyển động, vật thể đó đều đang có gia tốc!

---

### Gia tốc trung bình (Average Acceleration)

Xét một chất điểm chuyển động dọc theo trục $Ox$. Tại thời điểm $t_1$, chất điểm có vận tốc tức thời $v_{1x}$; tại thời điểm $t_2$, vận tốc biến thiên thành $v_{2x}$. Độ biến thiên vận tốc là $\Delta v_x = v_{2x} - v_{1x}$ trong khoảng thời gian $\Delta t = t_2 - t_1$.

Thành phần **gia tốc trung bình** trên đoạn thời gian đó được định nghĩa là:

$$a_{\mathrm{av}-x} = \frac{\Delta v_x}{\Delta t} = \frac{v_{2x} - v_{1x}}{t_2 - t_1}.\tag{2.4}$$

Nếu vận tốc tính bằng mét trên giây ($\mathrm{m/s}$) và thời gian tính bằng giây ($\mathrm s$), đơn vị của gia tốc là mét trên giây chia cho giây, tức **mét trên giây bình phương** ($\mathrm{m/s^2}$). Ý nghĩa vật lý của đơn vị này rất trực quan: Một gia tốc $2\,\mathrm{m/s^2}$ nghĩa là cứ sau mỗi giây trôi qua, vận tốc của vật lại tăng thêm $2\,\mathrm{m/s}$.

::: warning Cảm nhận sinh lý học về gia tốc và vận tốc
Hệ tiền đình của cơ thể con người không thể trực tiếp cảm nhận vận tốc không đổi, nhưng lại cực kỳ nhạy cảm với gia tốc! Khi bạn ngồi trên một chiếc máy bay phản lực đang bay bằng đều đặn ở tốc độ $900\,\mathrm{km/h}$, bạn cảm thấy êm ái y như đang ngồi trong phòng khách. Nhưng khi máy bay bắt đầu gầm rú lấy đà cất cánh trên đường băng (gia tốc hướng về phía trước), lưng bạn bị ép chặt vào thành ghế; và khi máy bay phanh gấp lúc hạ cánh, dây an toàn ghì chặt ngực bạn về phía trước. Gia tốc chính là đại lượng gắn liền trực tiếp với lực quán tính tác dụng lên cơ thể.
:::

---

### Ví dụ 2.2 — Gia tốc trung bình

::: exercise Bài toán
Một phi hành gia rời khoang tàu con thoi để thử nghiệm thiết bị đẩy cơ động cá nhân (MMU) trong không gian. Người ấy di chuyển trên một đường thẳng; hệ thống radar trên tàu mẹ đo thành phần vận tốc $v_x$ của phi hành gia sau mỗi $2.0\,\mathrm s$:

| Thời điểm $t$ ($\mathrm s$) | Vận tốc $v_x$ ($\mathrm{m/s}$) | Thời điểm $t$ ($\mathrm s$) | Vận tốc $v_x$ ($\mathrm{m/s}$) |
| :--- | :--- | :--- | :--- |
| $1.0$ | $+0.8$ | $9.0$ | $-0.4$ |
| $3.0$ | $+1.2$ | $11.0$ | $-1.0$ |
| $5.0$ | $+1.6$ | $13.0$ | $-1.6$ |
| $7.0$ | $+1.2$ | $15.0$ | $-0.8$ |

Hãy xác định gia tốc trung bình và cho biết tốc độ của phi hành gia đang tăng hay giảm trên từng khoảng thời gian sau:  
**(a)** Từ $1.0\,\mathrm s$ đến $3.0\,\mathrm s$;  
**(b)** Từ $5.0\,\mathrm s$ đến $7.0\,\mathrm s$;  
**(c)** Từ $9.0\,\mathrm s$ đến $11.0\,\mathrm s$;  
**(d)** Từ $13.0\,\mathrm s$ đến $15.0\,\mathrm s$.
:::

![Hình 2.10: Đồ thị vận tốc theo thời gian và các giá trị gia tốc trung bình tương ứng](img/young-02/hinh-2-10.png)

::: solution Hướng dẫn giải
**Nhận diện và thiết lập:** 
Áp dụng công thức (2.4) để tính $a_{\mathrm{av}-x} = \frac{\Delta v_x}{\Delta t}$.
Để biết phi hành gia chuyển động nhanh dần hay chậm dần, ta so sánh độ lớn của vận tốc tức thời (tốc độ $v = |v_x|$).

**Thực thi:**
**(a)** Trong khoảng $1.0\,\mathrm s \to 3.0\,\mathrm s$ ($\Delta t = 2.0\,\mathrm s$):
$$a_{\mathrm{av}-x} = \frac{1.2 - 0.8}{3.0 - 1.0} = \frac{+0.4\,\mathrm{m/s}}{2.0\,\mathrm s} = +0.2\,\mathrm{m/s^2}.$$
Tốc độ tăng từ $0.8\,\mathrm{m/s}$ lên $1.2\,\mathrm{m/s}$ $\implies$ **nhanh dần** theo chiều dương.

**(b)** Trong khoảng $5.0\,\mathrm s \to 7.0\,\mathrm s$:
$$a_{\mathrm{av}-x} = \frac{1.2 - 1.6}{7.0 - 5.0} = \frac{-0.4\,\mathrm{m/s}}{2.0\,\mathrm s} = -0.2\,\mathrm{m/s^2}.$$
Tốc độ giảm từ $1.6\,\mathrm{m/s}$ xuống $1.2\,\mathrm{m/s}$ $\implies$ **chậm dần** theo chiều dương.

**(c)** Trong khoảng $9.0\,\mathrm s \to 11.0\,\mathrm s$:
$$a_{\mathrm{av}-x} = \frac{-1.0 - (-0.4)}{11.0 - 9.0} = \frac{-0.6\,\mathrm{m/s}}{2.0\,\mathrm s} = -0.3\,\mathrm{m/s^2}.$$
Tốc độ tăng từ $0.4\,\mathrm{m/s}$ lên $1.0\,\mathrm{m/s}$ ($|-1.0| > |-0.4|$) $\implies$ **nhanh dần theo chiều âm**!

**(d)** Trong khoảng $13.0\,\mathrm s \to 15.0\,\mathrm s$:
$$a_{\mathrm{av}-x} = \frac{-0.8 - (-1.6)}{15.0 - 13.0} = \frac{+0.8\,\mathrm{m/s}}{2.0\,\mathrm s} = +0.4\,\mathrm{m/s^2}.$$
Tốc độ giảm từ $1.6\,\mathrm{m/s}$ xuống $0.8\,\mathrm{m/s}$ ($|-0.8| < |-1.6|$) $\implies$ **chậm dần theo chiều âm**.

**Đánh giá:** Lưu ý sâu sắc ở câu (c): Gia tốc mang dấu âm ($-0.3\,\mathrm{m/s^2}$) nhưng chuyển động lại là **nhanh dần**! Điều này khẳng định quy tắc vàng: Khi gia tốc và vận tốc cùng dấu, vật luôn chuyển động nhanh dần.
:::

---

### Gia tốc tức thời và Đạo hàm cấp hai của vị trí

Bằng cách cho khoảng thời gian $\Delta t$ tiến dần về $0$, tỷ số $\frac{\Delta v_x}{\Delta t}$ tiệm cận tới đạo hàm của vận tốc theo thời gian. Ta định nghĩa **thành phần gia tốc tức thời**:

$$a_x = \lim_{\Delta t \to 0} \frac{\Delta v_x}{\Delta t} = \frac{dv_x}{dt}.\tag{2.5}$$

Vì vận tốc vốn là đạo hàm bậc nhất của tọa độ vị trí ($v_x = \frac{dx}{dt}$), gia tốc chính là **đạo hàm bậc hai của tọa độ vị trí theo thời gian**:

$$a_x = \frac{d}{dt}\left(\frac{dx}{dt}\right) = \frac{d^2x}{dt^2}.\tag{2.6}$$

![Hình 2.11: Xe đua Grand Prix chuyển động với gia tốc biến thiên trên đường thẳng](img/young-02/hinh-2-11.png)

---

### Ví dụ 2.3 — Gia tốc trung bình và tức thời

::: exercise Bài toán
Vận tốc dọc theo trục $x$ của chiếc xe đua ở Hình 2.11 biến thiên theo thời gian theo phương trình:

$$v_x(t) = 60.0\,\mathrm{m/s} + (0.50\,\mathrm{m/s^3})t^2.$$

**(a)** Tính độ biến thiên vận tốc trong khoảng thời gian từ $t_1 = 1.0\,\mathrm s$ đến $t_2 = 3.0\,\mathrm s$.  
**(b)** Tính gia tốc trung bình của xe trong khoảng thời gian đó.  
**(c)** Tìm gia tốc tức thời tại $t_1 = 1.0\,\mathrm s$ bằng cách khảo sát giới hạn trên các khoảng thời gian $\Delta t$ nhỏ dần ($0.1\,\mathrm s$, $0.01\,\mathrm s$, $0.001\,\mathrm s$).  
**(d)** Thiết lập biểu thức giải tích của gia tốc tức thời bằng đạo hàm, từ đó tính $a_x$ tại $t = 1.0\,\mathrm s$ và $t = 3.0\,\mathrm s$.
:::

::: solution Hướng dẫn giải
**Nhận diện và thiết lập:**
Dùng công thức gia tốc trung bình (2.4) và đạo hàm gia tốc tức thời (2.5).

**Thực thi:**
**(a)** Vận tốc tại hai thời điểm:
$$v_{1x} = 60.0 + 0.50(1.0)^2 = 60.5\,\mathrm{m/s},$$
$$v_{2x} = 60.0 + 0.50(3.0)^2 = 60.0 + 0.50(9.0) = 64.5\,\mathrm{m/s}.$$
Độ biến thiên vận tốc:
$$\Delta v_x = v_{2x} - v_{1x} = 64.5\,\mathrm{m/s} - 60.5\,\mathrm{m/s} = +4.0\,\mathrm{m/s}.$$

**(b)** Gia tốc trung bình trong khoảng thời gian $\Delta t = 3.0 - 1.0 = 2.0\,\mathrm s$:
$$a_{\mathrm{av}-x} = \frac{\Delta v_x}{\Delta t} = \frac{4.0\,\mathrm{m/s}}{2.0\,\mathrm s} = +2.0\,\mathrm{m/s^2}.$$

**(c)** Khảo sát tiệm cận khi $\Delta t \to 0$ quanh thời điểm $t_1 = 1.0\,\mathrm s$:
- Với $\Delta t = 0.1\,\mathrm s \implies t_2 = 1.1\,\mathrm s$:
  $$v_{2x} = 60 + 0.50(1.1)^2 = 60.605\,\mathrm{m/s} \implies a_{\mathrm{av}-x} = \frac{60.605 - 60.5}{0.1} = 1.05\,\mathrm{m/s^2}.$$
- Với $\Delta t = 0.01\,\mathrm s \implies t_2 = 1.01\,\mathrm s$:
  $$v_{2x} = 60 + 0.50(1.01)^2 = 60.51005\,\mathrm{m/s} \implies a_{\mathrm{av}-x} = \frac{60.51005 - 60.5}{0.01} = 1.005\,\mathrm{m/s^2}.$$
- Với $\Delta t = 0.001\,\mathrm s \implies t_2 = 1.001\,\mathrm s$:
  $$a_{\mathrm{av}-x} = \frac{\Delta v_x}{0.001} = 1.0005\,\mathrm{m/s^2}.$$

Khi $\Delta t \to 0$, gia tốc trung bình tiệm cận tới giá trị tức thời chính xác là **$1.0\,\mathrm{m/s^2}$**.

**(d)** Lấy đạo hàm trực tiếp của hàm vận tốc:
$$a_x(t) = \frac{dv_x}{dt} = \frac{d}{dt}\left[60.0 + 0.50t^2\right] = 0 + (0.50)(2t) = (1.0\,\mathrm{m/s^3})t.$$

Thay số:
- Tại $t = 1.0\,\mathrm s$: $a_x(1.0) = 1.0 \times 1.0 = +1.0\,\mathrm{m/s^2}$ (trùng khớp câu c).
- Tại $t = 3.0\,\mathrm s$: $a_x(3.0) = 1.0 \times 3.0 = +3.0\,\mathrm{m/s^2}$.

**Đánh giá:** Gia tốc của chiếc xe tăng tuyến tính theo thời gian (từ $1.0\,\mathrm{m/s^2}$ lên $3.0\,\mathrm{m/s^2}$). Giá trị gia tốc trung bình ($2.0\,\mathrm{m/s^2}$) nằm chính xác tại điểm giữa của khoảng thời gian khảo sát. Đạo hàm của gia tốc theo thời gian ($da/dt$) trong kỹ thuật cơ khí được gọi là *jerk* (độ giật), đại lượng quyết định độ êm ái khi xe tăng tốc.
:::

---

### Ý nghĩa hình học: Gia tốc trên đồ thị vận tốc – thời gian ($v-t$)

Tương tự như mối liên hệ giữa tọa độ và vận tốc:
1. **Gia tốc trung bình** trong khoảng $\Delta t$ là **hệ số góc (độ dốc) của đường cát tuyến** nối hai điểm tương ứng trên đồ thị $v_x - t$ (Hình 2.12).
2. **Gia tốc tức thời** tại thời điểm $t$ là **độ dốc của đường tiếp tuyến** với đồ thị $v_x - t$ tại thời điểm đó:
   $$a_x = \text{Độ dốc tiếp tuyến của đồ thị } v_x - t.$$

![Hình 2.12: Gia tốc tức thời là độ dốc của tiếp tuyến trên đồ thị vận tốc - thời gian](img/young-02/hinh-2-12.png)

---

### Quy tắc vàng xóa tan ngộ nhận: Dấu của tích số $v_x \cdot a_x$

::: warning Xóa tan ngộ nhận: Gia tốc âm KHÔNG ĐỒNG NGHĨA với chuyển động chậm dần!
Hàng triệu học sinh thường mang ngộ nhận: *"Cứ gia tốc âm là xe đang phanh chậm dần"*. Đây là một sai lầm bản chất!
Dấu của gia tốc $a_x$ chỉ đơn thuần cho biết vector gia tốc đang hướng theo chiều dương hay chiều âm của trục tọa độ đã chọn.

Quy luật vật lý duy nhất quyết định một vật chuyển động nhanh dần hay chậm dần là **mối tương quan dấu giữa vận tốc $v_x$ và gia tốc $a_x$** (tức dấu của tích số $v_x \cdot a_x$):

1. **Khi $v_x$ và $a_x$ CÙNG DẤU ($v_x \cdot a_x > 0$): Chuyển động NHANH DẦN!**
   - $v_x > 0$ và $a_x > 0$: Vật đang tiến theo chiều dương và tăng tốc nhanh dần (Hình 2.13, điểm E).
   - $v_x < 0$ và $a_x < 0$: Vật đang chạy lùi theo chiều âm và gia tốc cũng hướng theo chiều âm; vận tốc ngày càng âm hơn $\implies$ tốc độ $|v_x|$ tăng lên $\implies$ **vật đang chạy lùi nhanh dần**!

2. **Khi $v_x$ và $a_x$ TRÁI DẤU ($v_x \cdot a_x < 0$): Chuyển động CHẬM DẦN!**
   - $v_x > 0$ và $a_x < 0$: Vật tiến theo chiều dương nhưng bị gia tốc hãm lại $\implies$ chậm dần (sắp dừng lại đổi chiều).
   - $v_x < 0$ và $a_x > 0$: Vật chạy lùi theo chiều âm nhưng gia tốc hướng theo chiều dương $\implies$ vận tốc bớt âm dần $\implies$ tốc độ $|v_x|$ giảm $\implies$ **vật đang chạy lùi chậm dần** (Hình 2.13, điểm A).
:::

### Bảng 2.3 — Tổng hợp tương quan dấu giữa vận tốc và gia tốc

| Trạng thái vận tốc $v_x$ | Dấu gia tốc $a_x$ | Tích $v_x \cdot a_x$ | Diễn biến chuyển động của chất điểm |
| :--- | :--- | :--- | :--- |
| Dương ($v_x > 0$) | Dương ($a_x > 0$) | $> 0$ | Tiến theo chiều dương, **nhanh dần**. |
| Dương ($v_x > 0$) | Âm ($a_x < 0$) | $< 0$ | Tiến theo chiều dương, **chậm dần**. |
| Âm ($v_x < 0$) | Dương ($a_x > 0$) | $< 0$ | Tiến theo chiều âm, **chậm dần**. |
| Âm ($v_x < 0$) | Âm ($a_x < 0$) | $> 0$ | Tiến theo chiều âm, **nhanh dần**. |

![Hình 2.13: Tương quan giữa đồ thị vận tốc v-t và trạng thái chuyển động tại các điểm A-E](img/young-02/hinh-2-13.png)

*Ứng dụng công nghệ — Cảm biến gia tốc MEMS trong đời sống:*
- **Điện thoại thông minh:** Bên trong mỗi smartphone đều có một chip cảm biến gia tốc vi cơ điện tử (MEMS) siêu nhỏ (cỡ micromét). Khi bạn xoay ngang điện thoại hay lắc cổ tay, gia tốc trọng trường tác động làm lệch các vi phiến silicon, thay đổi điện dung vi sai và ra lệnh cho hệ điều hành xoay hướng màn hình hoặc đếm từng bước chân bạn đi.
- **Túi khí ô tô an toàn:** Khi xảy ra va chạm trực diện, xe hơi giảm tốc đột ngột với gia tốc hãm cực lớn (thường vượt quá $-20g$ đến $-50g$, với $g \approx 9.8\,\mathrm{m/s^2}$). Cảm biến gia tốc MEMS phát hiện mức gia tốc âm dị thường này trong vòng chưa đầy $15\,\mathrm{ms}$ và kích hoạt ngòi nổ hóa học tạo khí nitrogen bơm phồng túi khí trước khi người lái kịp lao về phía trước!

---

### Gia tốc và độ cong của đồ thị vị trí – thời gian ($x-t$)

Vì gia tốc là đạo hàm bậc hai $a_x = \frac{d^2x}{dt^2}$, trong giải tích toán học, đạo hàm bậc hai phản ánh **chiều lõm (độ cong)** của đường cong đồ thị $x-t$ (Hình 2.14):
- **Đồ thị cong lõm lên trên (hình chiếc bát hứng nước):** $\frac{d^2x}{dt^2} > 0 \implies a_x > 0$ (gia tốc dương, độ dốc tiếp tuyến tăng dần từ trái sang phải).
- **Đồ thị cong lồi xuống dưới (hình chiếc bát úp ngược):** $\frac{d^2x}{dt^2} < 0 \implies a_x < 0$ (gia tốc âm, độ dốc tiếp tuyến giảm dần từ trái sang phải).
- **Điểm uốn (nơi đồ thị đổi chiều cong, tiếp tuyến đổi phía):** $a_x = 0$ (gia tốc tức thời triệt tiêu).

![Hình 2.14: Chiều cong của đồ thị x-t phản ánh trực tiếp dấu của gia tốc](img/young-02/hinh-2-14.png)

### Bảng 2.4 — Thông điệp vật lý từ hai loại đồ thị động học

| Đại lượng cần khảo sát | Đọc trên đồ thị $x-t$ | Đọc trên đồ thị $v_x-t$ |
| :--- | :--- | :--- |
| **Tọa độ vị trí ($x$)** | Giá trị của tung độ trên đồ thị. | Không đọc được trực tiếp (cần dùng tích phân diện tích). |
| **Vận tốc ($v_x$)** | **Độ dốc (hệ số góc)** của tiếp tuyến. | Giá trị của tung độ trên đồ thị. |
| **Gia tốc ($a_x$)** | **Chiều cong / độ lõm** của đồ thị ($d^2x/dt^2$). | **Độ dốc (hệ số góc)** của tiếp tuyến ($dv_x/dt$). |

---

### Câu hỏi kiểm tra hiểu biết mục 2.3

::: exercise Câu hỏi kiểm tra
Quan sát lại đồ thị $x-t$ ở Hình 2.9 (gồm bốn điểm P, Q, R, S):

**(a)** Điểm nào có gia tốc dương ($a_x > 0$)?  
**(b)** Điểm nào có gia tốc âm ($a_x < 0$)?  
**(c)** Những điểm nào có gia tốc xấp xỉ bằng không ($a_x \approx 0$)?  
**(d)** Tại mỗi điểm P, Q, R, S, vận tốc đang tăng, giảm hay tạm thời không đổi?
:::

::: solution Lời giải
Dựa vào chiều cong của đồ thị $x-t$:
- **(a) Điểm S có $a_x > 0$:** Tại lân cận điểm S, đồ thị có đáy cong hướng lõm lên trên (dạng parabol ngửa) $\implies$ đạo hàm bậc hai dương $\implies a_x > 0$.
- **(b) Điểm Q có $a_x < 0$:** Tại đỉnh Q, đồ thị cong úp xuống dưới (dạng parabol úp) $\implies$ đạo hàm bậc hai âm $\implies a_x < 0$.
- **(c) Điểm P và điểm R có $a_x \approx 0$:** Đây là các đoạn đồ thị tương đối thẳng hoặc là điểm uốn chuyển tiếp chiều cong, độ cong triệt tiêu $\implies a_x \approx 0$.
- **(d) Diễn biến vận tốc:**
  - Tại P: $a_x \approx 0 \implies$ vận tốc tức thời không đổi.
  - Tại Q: $a_x < 0 \implies$ vận tốc đang giảm liên tục (chuyển từ dương sang 0 rồi sang âm).
  - Tại R: $a_x \approx 0 \implies$ vận tốc tức thời không đổi.
  - Tại S: $a_x > 0 \implies$ vận tốc đang tăng liên tục (chuyển từ âm sang 0 rồi sang dương).
:::
