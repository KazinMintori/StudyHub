## 2.3. Gia tốc trung bình và tức thời

Vận tốc mô tả sự thay đổi vị trí theo thời gian. **Gia tốc** mô tả sự thay đổi vận tốc theo thời gian. Đây cũng là đại lượng vector. Trong chuyển động thẳng, chỉ thành phần theo đường thẳng ấy có thể khác không.

Trong lời nói hằng ngày, gia tốc thường gắn với nhanh dần. Trong vật lý, mọi sự thay đổi vận tốc đều liên quan đến gia tốc, kể cả khi vật chậm dần.

### Gia tốc trung bình

Tại thời điểm $t_1$, chất điểm có vận tốc $v_{1x}$. Tại thời điểm sau $t_2$, vận tốc là $v_{2x}$. Độ biến thiên vận tốc bằng giá trị cuối trừ giá trị đầu. Thành phần x của gia tốc trung bình là:

$$
a_{\mathrm{av}-x}=\frac{\Delta v_x}{\Delta t}=\frac{v_{2x}-v_{1x}}{t_2-t_1}.
\tag{2.4}
$$

Nếu vận tốc tính bằng m/s và thời gian bằng s, gia tốc có đơn vị m/s², đọc là mét trên giây bình phương.

::: warning Vận tốc và gia tốc mô tả hai sự thay đổi khác nhau
Vận tốc cho biết vị trí thay đổi ra sao, còn gia tốc cho biết vận tốc thay đổi ra sao. Người ngồi trên xe tăng tốc về phía trước cảm thấy như bị đẩy ra sau ghế. Khi xe chậm lại, người ấy cảm thấy như bị đẩy về phía trước. Chuyển động với vận tốc không đổi không gây hai cảm giác đó. Chương 4 sẽ giải thích chúng.
:::

### Ví dụ 2.2: Gia tốc trung bình

Một phi hành gia rời tàu đang bay trên quỹ đạo để thử thiết bị cơ động cá nhân. Khi cô chuyển động trên đường thẳng, đồng đội trên tàu đo vận tốc sau mỗi 2,0 s, bắt đầu từ $t=1{,}0\,\mathrm s$:

| Thời điểm, đơn vị s | Vận tốc theo trục x, đơn vị m/s |
| --- | --- |
| 1,0 | +0,8 |
| 3,0 | +1,2 |
| 5,0 | +1,6 |
| 7,0 | +1,2 |
| 9,0 | −0,4 |
| 11,0 | −1,0 |
| 13,0 | −1,6 |
| 15,0 | −0,8 |

Tìm gia tốc trung bình và cho biết tốc độ tăng hay giảm trong từng khoảng: (a) 1,0–3,0 s. (b) 5,0–7,0 s. (c) 9,0–11,0 s. (d) 13,0–15,0 s.

![Hình 2.10: Đồ thị vận tốc theo thời gian ở trên và các gia tốc trung bình ở dưới của phi hành gia](img/young-02/hinh-2-10.png)

::: solution Lời giải
Mỗi khoảng kéo dài 2,0 s. Dùng (2.4), lấy vận tốc cuối trừ vận tốc đầu rồi chia thời gian. Muốn xét nhanh hay chậm, so sánh độ lớn vận tốc ở hai mốc.

(a) Độ biến thiên vận tốc là $+0{,}4\,\mathrm{m/s}$:

$$
\begin{aligned}
a_{\mathrm{av}-x}&=\frac{+0{,}4\,\mathrm{m/s}}{2{,}0\,\mathrm s}\\
&=+0{,}2\,\mathrm{m/s^2}.
\end{aligned}
$$

Tốc độ tăng từ 0,8 m/s lên 1,2 m/s.

(b) Độ biến thiên vận tốc là $-0{,}4\,\mathrm{m/s}$:

$$
\begin{aligned}
a_{\mathrm{av}-x}&=\frac{-0{,}4\,\mathrm{m/s}}{2{,}0\,\mathrm s}\\
&=-0{,}2\,\mathrm{m/s^2}.
\end{aligned}
$$

Tốc độ giảm từ 1,6 m/s xuống 1,2 m/s.

(c) Vận tốc đổi từ −0,4 m/s thành −1,0 m/s, nên độ biến thiên bằng −0,6 m/s:

$$
\begin{aligned}
a_{\mathrm{av}-x}&=\frac{-0{,}6\,\mathrm{m/s}}{2{,}0\,\mathrm s}\\
&=-0{,}3\,\mathrm{m/s^2}.
\end{aligned}
$$

Tốc độ tăng từ 0,4 m/s lên 1,0 m/s dù cả vận tốc và gia tốc trung bình đều âm.

(d) Vận tốc đổi từ −1,6 m/s thành −0,8 m/s, nên độ biến thiên bằng +0,8 m/s:

$$
\begin{aligned}
a_{\mathrm{av}-x}&=\frac{+0{,}8\,\mathrm{m/s}}{2{,}0\,\mathrm s}\\
&=+0{,}4\,\mathrm{m/s^2}.
\end{aligned}
$$

Tốc độ giảm từ 1,6 m/s xuống 0,8 m/s.

Trên đồ thị vận tốc, các cát tuyến tương ứng có độ dốc lần lượt dương, âm, âm và dương. Độ lớn hai độ dốc cuối lớn hơn hai độ dốc đầu, phù hợp với kết quả tính.

Trong các khoảng đã xét, gia tốc trung bình cùng dấu vận tốc ban đầu đi kèm tốc độ tăng, còn trái dấu đi kèm tốc độ giảm. Dấu dương của gia tốc không tự có nghĩa là nhanh dần, dấu âm cũng không tự có nghĩa là chậm dần.
:::

### Gia tốc tức thời

Cho hai vị trí $P_2$ và $P_1$ của xe đua trong Hình 2.11 tiến gần nhau, rồi tính gia tốc trung bình trên những khoảng thời gian ngắn dần. Nếu vận tốc khả vi, giới hạn cho thành phần gia tốc tức thời:

$$
a_x=\lim_{\Delta t\to0}\frac{\Delta v_x}{\Delta t}=\frac{dv_x}{dt}.
\tag{2.5}
$$

![Hình 2.11: Xe đua tại hai vị trí trên đoạn đường thẳng, với các vận tốc tương ứng](img/young-02/hinh-2-11.png)

Trong chuyển động một chiều, các thành phần gia tốc còn lại bằng không. Từ đây, khi dùng từ “gia tốc” mà không nói “trung bình”, ta hiểu là gia tốc tức thời.

### Ví dụ 2.3: Gia tốc trung bình và tức thời

Vận tốc theo trục x của xe trong Hình 2.11 là:

$$
v_x=60\,\mathrm{m/s}+(0{,}50\,\mathrm{m/s^3})t^2.
$$

(a) Tìm độ biến thiên vận tốc từ $t_1=1{,}0\,\mathrm s$ đến $t_2=3{,}0\,\mathrm s$. (b) Tìm gia tốc trung bình trong khoảng ấy. (c) Tìm gia tốc tức thời tại 1,0 s bằng các khoảng $\Delta t$ bằng 0,1 s, 0,01 s và 0,001 s. (d) Lấy đạo hàm để tìm gia tốc theo thời gian, rồi tính tại 1,0 s và 3,0 s.

::: solution Lời giải
Đây là cách làm tương tự Ví dụ 2.1, nhưng thay sự biến thiên vị trí bằng sự biến thiên vận tốc. Dùng (2.4) cho gia tốc trung bình và (2.5) cho gia tốc tức thời.

(a) Khi thay thời gian tính bằng giây, vận tốc thu được theo m/s:

$$
\begin{aligned}
v_{1x}&=[60+0{,}50(1{,}0)^2]\,\mathrm{m/s}\\
&=60{,}5\,\mathrm{m/s},\\
v_{2x}&=[60+0{,}50(3{,}0)^2]\,\mathrm{m/s}\\
&=64{,}5\,\mathrm{m/s}.
\end{aligned}
$$

Độ biến thiên vận tốc là $64{,}5-60{,}5=4{,}0$ m/s.

(b) Khoảng thời gian bằng 2,0 s:

$$
a_{\mathrm{av}-x}=\frac{4{,}0\,\mathrm{m/s}}{2{,}0\,\mathrm s}=2{,}0\,\mathrm{m/s^2}.
$$

Vận tốc và gia tốc trung bình đều dương trong khoảng này, xe nhanh lên.

(c) Với $\Delta t=0{,}1\,\mathrm s$, mốc sau là 1,1 s và vận tốc sau bằng 60,605 m/s. Vận tốc đã tăng 0,105 m/s, nên:

$$
\begin{aligned}
a_{\mathrm{av}-x}&=\frac{0{,}105\,\mathrm{m/s}}{0{,}1\,\mathrm s}\\
&=1{,}05\,\mathrm{m/s^2}.
\end{aligned}
$$

Hai khoảng ngắn hơn cho:

| Khoảng thời gian, đơn vị s | Vận tốc sau, đơn vị m/s | Gia tốc trung bình, đơn vị m/s² |
| --- | --- | --- |
| 0,1 | 60,605 | 1,05 |
| 0,01 | 60,51005 | 1,005 |
| 0,001 | 60,5010005 | 1,0005 |

Các giá trị tiến tới 1,0 m/s². Ta giữ thêm chữ số để quan sát giới hạn.

(d) Đạo hàm hằng số bằng không, còn số hạng bậc hai cho:

$$
\begin{aligned}
a_x(t)&=\frac{dv_x}{dt}\\
&=0+2(0{,}50\,\mathrm{m/s^3})t\\
&=(1{,}0\,\mathrm{m/s^3})t.
\end{aligned}
$$

Tại 1,0 s, gia tốc bằng 1,0 m/s². Tại 3,0 s, gia tốc bằng 3,0 m/s². Cả hai khác gia tốc trung bình 2,0 m/s² vì gia tốc tức thời biến thiên. Tốc độ biến thiên của gia tốc theo thời gian đôi khi được gọi là độ giật (jerk).
:::

### Đọc gia tốc trên đồ thị vận tốc

Trên đồ thị vận tốc theo thời gian, độ dốc cát tuyến nối hai mốc bằng gia tốc trung bình giữa chúng. Khi hai mốc tiến gần nhau, độ dốc cát tuyến tiến tới độ dốc tiếp tuyến. Gia tốc tức thời bằng độ dốc tiếp tuyến tại mốc tương ứng.

![Hình 2.12: Cát tuyến cho gia tốc trung bình, còn tiếp tuyến cho gia tốc tức thời trên đồ thị vận tốc](img/young-02/hinh-2-12.png)

Các tiếp tuyến ở những mốc khác nhau có thể có độ dốc khác nhau, cho thấy gia tốc biến thiên theo thời gian.

### Bảng 2.3: Dấu của vận tốc và gia tốc

| Vận tốc theo trục x | Gia tốc theo trục x | Chuyển động |
| --- | --- | --- |
| Dương và tăng, trở nên dương hơn | Dương | Theo chiều dương, nhanh dần |
| Dương và giảm, trở nên ít dương hơn | Âm | Theo chiều dương, chậm dần |
| Âm và tăng, trở nên ít âm hơn | Dương | Theo chiều âm, chậm dần |
| Âm và giảm, trở nên âm hơn | Âm | Theo chiều âm, nhanh dần |

Khi vận tốc khác không, cùng dấu với gia tốc thì tốc độ tăng, còn trái dấu thì tốc độ giảm. Từ “giảm tốc” có thể gây nhầm nếu bị hiểu là gia tốc âm. Việc giảm tốc độ có thể ứng với gia tốc dương hoặc âm, tùy chiều chuyển động.

![Hình 2.13: Đồ thị vận tốc và sơ đồ chuyển động minh họa dấu của vận tốc, gia tốc ở năm mốc](img/young-02/hinh-2-13.png)

Ở A, vận tốc âm và gia tốc dương, chất điểm chậm dần khi đi theo chiều âm. Tại B, vận tốc bằng không và gia tốc dương, chất điểm sắp chuyển động theo chiều dương. Tại C, vận tốc dương nhưng gia tốc bằng không, tốc độ không đổi tức thời.

Tại D, vận tốc bằng không và gia tốc âm, chất điểm sắp chuyển động theo chiều âm. Ở E, vận tốc và gia tốc đều âm nên chất điểm đi theo chiều âm và nhanh dần. Mỗi mốc cần được đọc từ cả vận tốc lẫn độ dốc, không từ một dấu đơn lẻ.

### Gia tốc trên đồ thị tọa độ

Vì vận tốc là đạo hàm của tọa độ, lấy đạo hàm thêm một lần cho:

$$
a_x=\frac{d}{dt}\left(\frac{dx}{dt}\right)=\frac{d^2x}{dt^2}.
\tag{2.6}
$$

Gia tốc là đạo hàm bậc hai của tọa độ theo thời gian. Đồ thị tọa độ lõm lên cho gia tốc dương và vận tốc theo trục x đang tăng. Đồ thị lõm xuống cho gia tốc âm và vận tốc đang giảm. Tại những điểm uốn được chỉ trong hình, gia tốc bằng không.

![Hình 2.14: Cùng một chuyển động được biểu diễn bằng đồ thị tọa độ và các vector vận tốc, gia tốc](img/young-02/hinh-2-14.png)

Ở A và E, đồ thị lõm lên nên gia tốc dương. Ở C, đồ thị lõm xuống nên gia tốc âm. Tại B và D, độ cong triệt tiêu nên gia tốc bằng không.

Hai điểm có cùng dấu gia tốc vẫn có thể biến đổi tốc độ khác nhau. A có vận tốc dương nên nhanh dần, còn E có vận tốc âm nên chậm dần. C dừng tức thời rồi chuyển động theo chiều âm. B và D có gia tốc bằng không tại mốc đang xét.

Quan sát chiều lõm thuận tiện để xác định dấu gia tốc. Tuy nhiên, khó đo chính xác độ cong trên hình để lấy giá trị gia tốc bằng số.

### Bảng 2.4: Thông tin từ hai loại đồ thị

| Đặc điểm tại một thời điểm | Đồ thị tọa độ theo thời gian | Đồ thị vận tốc theo thời gian |
| --- | --- | --- |
| Giá trị trên đồ thị | Tọa độ x | Vận tốc theo trục x |
| Độ dốc tiếp tuyến | Vận tốc theo trục x | Gia tốc theo trục x |
| Chiều lõm hoặc độ cong | Dấu gia tốc theo trục x | Gia tốc có đang biến thiên hay không |

### Tự kiểm tra 2.3

::: exercise Đọc gia tốc từ đồ thị tọa độ
Xét lại đồ thị ở Hình 2.9. (a) Trong các điểm P, Q, R và S, điểm nào có gia tốc theo trục x dương? (b) Điểm nào có gia tốc âm? (c) Điểm nào có gia tốc dường như bằng không? (d) Tại mỗi điểm, vận tốc đang tăng, giảm hay không đổi?
:::

::: solution Giải thích
(a) S có đồ thị lõm lên nên gia tốc dương. (b) Q có đồ thị lõm xuống nên gia tốc âm. (c) Tại P và R, đồ thị không cong lên hoặc cong xuống nên gia tốc dường như bằng không.

(d) Tại P và R, vận tốc không thay đổi tức thời. Tại Q, vận tốc giảm từ dương về không rồi sang âm. Tại S, vận tốc tăng từ âm về không rồi sang dương.
:::
