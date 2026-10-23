## Luyện tập hướng dẫn

Nhóm 12 bài luyện tập sau củng cố kỹ năng vận dụng động học và động lực học chuyển động quay của vật rắn quanh một trục cố định: Mối liên hệ giữa các đại lượng góc, gia tốc tiếp tuyến và hướng tâm, mômen quán tính của các vật thể đồng chất, cùng định lý động năng và bảo toàn cơ năng trong hệ quay.

---

### VP9.3.1

Một chi tiết máy ban đầu quay với tốc độ góc $0{,}500\,\mathrm{rad/s}$. Chuyển động quay nhanh dần với gia tốc góc không đổi $2{,}50\,\mathrm{rad/s^2}$. Chi tiết máy đã quay được một góc bằng bao nhiêu khi tốc độ góc đạt $3{,}25\,\mathrm{rad/s}$? Đưa ra câu trả lời theo:
(a) Radian.
(b) Độ.
(c) Số vòng quay.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Tốc độ góc ban đầu: $\omega_0 = 0{,}500\,\mathrm{rad/s}$.
- Gia tốc góc không đổi: $\alpha = 2{,}50\,\mathrm{rad/s^2}$.
- Tốc độ góc cuối: $\omega = 3{,}25\,\mathrm{rad/s}$.
- Cần tìm: Góc quay $\Delta\theta$ theo đơn vị (a) $\mathrm{rad}$, (b) độ ($^\circ$), (c) vòng ($\mathrm{rev}$).

**Hướng đi:**
- Vì gia tốc góc $\alpha$ không đổi, ta áp dụng hệ thức độc lập với thời gian trong chuyển động quay:
$$
\omega^2 = \omega_0^2 + 2\alpha\Delta\theta
$$
- Chuyển đổi góc quay từ radian sang độ và số vòng quay thông qua các hệ số tỉ lệ hình học: $1\,\mathrm{rev} = 2\pi\,\mathrm{rad} = 360^\circ$.

**Lời giải chi tiết:**

(a) Tính góc quay theo đơn vị radian:
Từ phương trình động học chuyển động quay biến đổi đều:
$$
\Delta\theta = \frac{\omega^2 - \omega_0^2}{2\alpha}
$$

Thay các giá trị đã cho:
$$
\begin{aligned}
\Delta\theta &= \frac{(3{,}25)^2 - (0{,}500)^2}{2(2{,}50)} \\
&= \frac{10{,}5625 - 0{,}250}{5{,}00} \\
&= \frac{10{,}3125}{5{,}00} \\
&= 2{,}0625\,\mathrm{rad} \\
&\approx 2{,}06\,\mathrm{rad}.
\end{aligned}
$$

(b) Chuyển đổi sang đơn vị độ:
Áp dụng hệ số chuyển đổi $1\,\mathrm{rad} = \frac{180^\circ}{\pi}$:
$$
\begin{aligned}
\Delta\theta &= 2{,}0625\,\mathrm{rad} \times \frac{180^\circ}{\pi} \\
&\approx 118{,}17^\circ \\
&\approx 118^\circ.
\end{aligned}
$$

(c) Chuyển đổi sang số vòng quay:
Áp dụng hệ số chuyển đổi $1\,\mathrm{rev} = 2\pi\,\mathrm{rad}$:
$$
\begin{aligned}
\Delta\theta &= \frac{2{,}0625}{2\pi} \\
&\approx 0{,}32826\,\mathrm{rev} \\
&\approx 0{,}328\,\mathrm{rev}.
\end{aligned}
$$

Kiểm tra: Góc quay xấp xỉ một phần ba vòng tròn ($0{,}328 \times 360^\circ \approx 118^\circ$), hoàn toàn khớp với kết quả theo độ.

</details>

---

### VP9.3.2

Rôto của một máy bay trực thăng đang tăng tốc độ góc với gia tốc góc không đổi. Tại thời điểm $t = 0$, rôto đang quay với tốc độ góc $1{,}25\,\mathrm{rad/s}$. Từ $t = 0$ đến $t = 2{,}00\,\mathrm{s}$, rôto quay được một góc $8{,}00\,\mathrm{rad}$.
(a) Gia tốc góc của rôto bằng bao nhiêu?
(b) Từ $t = 0$ đến $t = 4{,}00\,\mathrm{s}$, rôto quay được một góc bằng bao nhiêu radian?

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Tốc độ góc ban đầu: $\omega_0 = 1{,}25\,\mathrm{rad/s}$.
- Tại $t_1 = 2{,}00\,\mathrm{s}$: Góc quay $\theta_1 = 8{,}00\,\mathrm{rad}$.
- Cần tìm: (a) Gia tốc góc $\alpha$; (b) Góc quay $\theta_2$ tại $t_2 = 4{,}00\,\mathrm{s}$.

**Hướng đi:**
- Áp dụng phương trình góc quay theo thời gian cho chuyển động quay biến đổi đều:
$$
\theta(t) = \omega_0 t + \frac{1}{2}\alpha t^2
$$
- Sử dụng dữ kiện tại $t_1 = 2{,}00\,\mathrm{s}$ để giải phương trình bậc nhất tìm gia tốc góc $\alpha$.
- Thay giá trị $\alpha$ vừa tìm được vào phương trình tọa độ góc tại $t_2 = 4{,}00\,\mathrm{s}$.

**Lời giải chi tiết:**

(a) Tìm gia tốc góc của rôto:
Biểu thức góc quay tại thời điểm $t_1 = 2{,}00\,\mathrm{s}$ là:
$$
\theta_1 = \omega_0 t_1 + \frac{1}{2}\alpha t_1^2
$$

Biến đổi đại số để rút ra $\alpha$:
$$
\alpha = \frac{2(\theta_1 - \omega_0 t_1)}{t_1^2}
$$

Thay các giá trị số vào biểu thức:
$$
\begin{aligned}
\alpha &= \frac{2(8{,}00-2{,}50)}{(2{,}00)^2} \\
&= \frac{2(8{,}00 - 2{,}50)}{4{,}00} \\
&= \frac{11{,}00}{4{,}00} \\
&= 2{,}75\,\mathrm{rad/s^2}.
\end{aligned}
$$

(b) Tính góc quay từ $t = 0$ đến $t_2 = 4{,}00\,\mathrm{s}$:
Thay $\omega_0 = 1{,}25\,\mathrm{rad/s}$ và $\alpha = 2{,}75\,\mathrm{rad/s^2}$ vào phương trình góc quay:
$$
\begin{aligned}
\theta_2 &= \omega_0t+\frac12\alpha t^2 \\
&= 5{,}00+22{,}00 \\
&= 5{,}00 + 22{,}00 \\
&= 27{,}0\,\mathrm{rad}.
\end{aligned}
$$

Kiểm tra: Vì chuyển động quay nhanh dần đều, góc quay trong $2{,}00\,\mathrm{s}$ tiếp theo ($\theta_2 - \theta_1 = 19{,}0\,\mathrm{rad}$) lớn hơn nhiều so với $8{,}00\,\mathrm{rad}$ trong $2{,}00\,\mathrm{s}$ đầu tiên, phù hợp với tính chất tăng tốc.

</details>

---

### VP9.3.3

Đá mài của một người thợ kim hoàn quay chậm dần đều từ $185\,\mathrm{rad/s}$ xuống $105\,\mathrm{rad/s}$ trong khi quay được $16{,}0$ vòng. Quá trình hãm tốc độ này diễn ra trong bao lâu?

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Tốc độ góc ban đầu: $\omega_0 = 185\,\mathrm{rad/s}$.
- Tốc độ góc sau: $\omega = 105\,\mathrm{rad/s}$.
- Góc quay: $16{,}0$ vòng, tương ứng $\Delta\theta=32{,}0\pi\,\mathrm{rad}$.
- Cần tìm: Thời gian hãm tốc $t$.

**Hướng đi:**
- Với gia tốc góc không đổi, vận tốc góc trung bình bằng trung bình cộng của vận tốc góc đầu và vận tốc góc cuối:
$$
\omega_{\mathrm{tb}} = \frac{\omega_0 + \omega}{2}
$$
- Do đó góc quay liên hệ trực tiếp với thời gian thông qua hệ thức:
$$
\Delta\theta = \omega_{\mathrm{tb}} t = \frac{\omega_0 + \omega}{2} t
$$
- Từ đây ta giải trực tiếp tìm $t$ mà không cần tính trung gian gia tốc góc $\alpha$.

**Lời giải chi tiết:**

Biến đổi hệ thức góc quay theo vận tốc góc trung bình để biểu diễn thời gian:
$$
t = \frac{2\Delta\theta}{\omega_0 + \omega}
$$

Đổi góc quay sang đơn vị radian:
$$
\begin{aligned}
\Delta\theta &= 16{,}0 \times 2\pi\,\mathrm{rad} \\
&= 32{,}0\pi\,\mathrm{rad}
\end{aligned}
$$

Thay các giá trị số vào biểu thức:
$$
\begin{aligned}
t &= \frac{2(32{,}0\pi)}{185 + 105} \\
&= \frac{64{,}0\pi}{290} \\
&= \frac{32\pi}{145} \\
&\approx 0{,}6934\,\mathrm{s} \\
&\approx 0{,}693\,\mathrm{s}.
\end{aligned}
$$

Gia tốc góc trong quá trình hãm được xác định bởi:

$$
\begin{aligned}
\alpha&=\frac{\omega-\omega_0}{t}\\
&\approx-115{,}4\,\mathrm{rad/s^2}.
\end{aligned}
$$

Thay vào hệ thức độc lập với thời gian cũng cho góc quay tương ứng:

$$
\begin{aligned}
\Delta\theta&=\frac{\omega^2-\omega_0^2}{2\alpha}\\
&\approx100{,}5\,\mathrm{rad}.
\end{aligned}
$$

</details>

---

### VP9.3.4

Một chiếc đĩa quay quanh trục đi qua tâm và vuông góc với mặt phẳng đĩa. Trên mặt đĩa có vẽ một đoạn thẳng nối từ trục quay ra mép đĩa. Tại thời điểm $t = 0$, đoạn thẳng này nằm dọc theo trục $x$ và chiếc đĩa đang quay với vận tốc góc dương $\omega_{0z}$. Chiếc đĩa có gia tốc góc dương không đổi $\alpha_z$. Hỏi tại thời điểm nào sau $t = 0$, đoạn thẳng trên đĩa đã quay được một góc $\theta$?

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** $\theta_0=0$, $\omega_{0z}>0$, $\alpha_z>0$ không đổi. Tìm $t>0$ ứng với góc $\theta>0$.

**Hướng đi:**
- Dùng phương trình góc quay có gia tốc góc không đổi, rồi giải phương trình bậc hai theo thời gian.
- Chọn nghiệm dương vì cần thời điểm sau lúc bắt đầu. Dùng tốc độ góc cuối làm ký hiệu phụ để biểu thức nghiệm gọn và rõ.

**Lời giải chi tiết:**

Phương trình góc quay:

$$
\theta=\omega_{0z}t+\frac12\alpha_zt^2.
$$

Nhân với $2$ rồi chuyển vế:

$$
\alpha_zt^2+2\omega_{0z}t-2\theta=0.
$$

Đặt $\Omega$ là tốc độ góc cuối thỏa hệ thức:

$$
\Omega^2=\omega_{0z}^2+2\alpha_z\theta.
$$

Lấy căn dương cho $\Omega$. Biệt thức của phương trình bậc hai bằng $\Delta=4\Omega^2$. Hai nghiệm:

$$
t_\pm=\frac{-\omega_{0z}\pm\Omega}{\alpha_z}.
$$

Vì $\Omega>\omega_{0z}>0$, nghiệm dấu cộng dương và nghiệm dấu trừ âm. Thời gian cần tìm:

$$
t=\frac{\Omega-\omega_{0z}}{\alpha_z}.
$$

Để xét giới hạn gia tốc góc tiến về không, nhân cả tử và mẫu với $\Omega+\omega_{0z}$. Dùng định nghĩa của $\Omega$ thu được dạng tương đương:

$$
t=\frac{2\theta}{\Omega+\omega_{0z}}.
$$

Khi $\alpha_z\to0$, ta có $\Omega\to\omega_{0z}$, nên $t\to\theta/\omega_{0z}$, đúng với chuyển động quay đều.

</details>

---

### VP9.5.1

Ngay sau khi một đĩa than (bán kính $0{,}152\,\mathrm{m}$) bắt đầu quay trên bàn quay, vận tốc góc của đĩa đạt $1{,}60\,\mathrm{rad/s}$ và đang tăng với tốc độ $8{,}00\,\mathrm{rad/s^2}$. Tại thời điểm này, đối với một điểm nằm ở mép đĩa, hãy xác định:
(a) Thành phần gia tốc tiếp tuyến.
(b) Thành phần gia tốc hướng tâm.
(c) Độ lớn của gia tốc toàn phần.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Bán kính đĩa: $r = 0{,}152\,\mathrm{m}$.
- Vận tốc góc tức thời: $\omega = 1{,}60\,\mathrm{rad/s}$.
- Gia tốc góc tức thời: $\alpha = 8{,}00\,\mathrm{rad/s^2}$.
- Cần tìm: Tại mép đĩa ($r = 0{,}152\,\mathrm{m}$): (a) $a_{\mathrm{tan}}$; (b) $a_{\mathrm{rad}}$; (c) $a = |\vec{a}|$.

**Hướng đi:**
- Điểm trên mép vật rắn chuyển động tròn có hai thành phần gia tốc vuông góc với nhau:
  - Thành phần tiếp tuyến $a_{\mathrm{tan}} = r\alpha$ biểu thị tốc độ biến thiên về độ lớn của vận tốc dài.
  - Thành phần hướng tâm $a_{\mathrm{rad}} = r\omega^2$ biểu thị tốc độ biến thiên về hướng của vận tốc dài.
- Độ lớn gia tốc toàn phần được tính bằng định lý Pythagoras:
$$
a = \sqrt{a_{\mathrm{tan}}^2 + a_{\mathrm{rad}}^2}
$$

**Lời giải chi tiết:**

(a) Thành phần gia tốc tiếp tuyến:
$$
\begin{aligned}
a_{\mathrm{tan}} &= r\alpha \\
&= (0{,}152)(8{,}00) \\
&= 1{,}216\,\mathrm{m/s^2} \\
&\approx 1{,}22\,\mathrm{m/s^2}.
\end{aligned}
$$

(b) Thành phần gia tốc hướng tâm (pháp tuyến):
$$
\begin{aligned}
a_{\mathrm{rad}} &= r\omega^2 \\
&= (0{,}152)(1{,}60)^2 \\
&= (0{,}152)(2{,}56) \\
&= 0{,}38912\,\mathrm{m/s^2} \\
&\approx 0{,}389\,\mathrm{m/s^2}.
\end{aligned}
$$

(c) Độ lớn gia tốc toàn phần:
Vì hai vector thành phần vuông góc với nhau:
$$
\begin{aligned}
a &= \sqrt{a_{\mathrm{tan}}^2 + a_{\mathrm{rad}}^2} \\
&= \sqrt{1{,}47866 + 0{,}15141} \\
&= \sqrt{1{,}63007} \\
&\approx 1{,}2767\,\mathrm{m/s^2} \\
&\approx 1{,}28\,\mathrm{m/s^2}.
\end{aligned}
$$

Gia tốc hợp với phương tiếp tuyến một góc $\phi$, thỏa mãn:

$$
\tan\phi=\frac{a_{\mathrm{rad}}}{a_{\mathrm{tan}}}.
$$

Thay hai thành phần đã tính được cho $\phi\approx17{,}7^\circ$.

</details>

---

### VP9.5.2

Một nữ siêu anh hùng vung chiếc búa thần phía trên đầu trong một mặt phẳng nằm ngang. Đầu búa chuyển động tròn trên quỹ đạo bán kính $1{,}50\,\mathrm{m}$ với tốc độ góc $6{,}00\,\mathrm{rad/s}$. Trong khi vẫn vung búa, cô bắt đầu bay thẳng đứng lên cao với tốc độ không đổi $2{,}00\,\mathrm{m/s}$.
(a) Tốc độ của đầu búa đối với mặt đất bằng bao nhiêu?
(b) Gia tốc (độ lớn và hướng) của đầu búa là gì?

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Bán kính quỹ đạo tròn nằm ngang: $r = 1{,}50\,\mathrm{m}$.
- Tốc độ góc quay nằm ngang: $\omega = 6{,}00\,\mathrm{rad/s}$.
- Tốc độ nâng thẳng đứng không đổi: $v_z = 2{,}00\,\mathrm{m/s}$.
- Cần tìm: (a) Tốc độ toàn phần $v$ đối với mặt đất; (b) Vector gia tốc $\vec{a}$ (độ lớn và hướng).

**Hướng đi:**
- Chuyển động của đầu búa là sự kết hợp độc lập giữa hai chuyển động: Chuyển động tròn đều trong mặt phẳng nằm ngang $xy$ và chuyển động tịnh tiến đều theo phương thẳng đứng $z$.
- Vector vận tốc toàn phần gồm thành phần tiếp tuyến nằm ngang $v_{\mathrm{horiz}} = r\omega$ và thành phần thẳng đứng $v_z$. Tốc độ là độ lớn của vector vận tốc tổng hợp.
- Do chuyển động thẳng đứng có tốc độ không đổi ($a_z = 0$) và chuyển động quay tròn có tốc độ góc không đổi ($\alpha = 0 \implies a_{\mathrm{tan}} = 0$), gia tốc duy nhất của đầu búa là gia tốc hướng tâm trong mặt phẳng nằm ngang.

**Lời giải chi tiết:**

(a) Tính tốc độ của đầu búa đối với mặt đất:
Thành phần vận tốc tiếp tuyến theo phương ngang:
$$
\begin{aligned}
v_{\mathrm{horiz}} &= r\omega \\
&= (1{,}50)(6{,}00) \\
&= 9{,}00\,\mathrm{m/s}
\end{aligned}
$$

Vì phương chuyển động tròn nằm trong mặt phẳng ngang vuông góc với phương thẳng đứng:
$$
\begin{aligned}
v &= \sqrt{v_{\mathrm{horiz}}^2 + v_z^2} \\
&= \sqrt{(9{,}00)^2 + (2{,}00)^2} \\
&= \sqrt{81{,}00 + 4{,}00} \\
&= \sqrt{85{,}00} \\
&\approx 9{,}2195\,\mathrm{m/s} \\
&\approx 9{,}22\,\mathrm{m/s}.
\end{aligned}
$$

(b) Xác định gia tốc của đầu búa:
- Theo phương thẳng đứng: Vận tốc $v_z = 2{,}00\,\mathrm{m/s}$ không đổi, do đó $a_z = 0$.
- Theo phương tiếp tuyến trong mặt phẳng ngang: Tốc độ góc $\omega = 6{,}00\,\mathrm{rad/s}$ không đổi, dẫn đến gia tốc góc $\alpha = 0$ và $a_{\mathrm{tan}} = r\alpha = 0$.
- Theo phương pháp tuyến trong mặt phẳng ngang: Đầu búa có gia tốc hướng tâm hướng vào tâm quỹ đạo quay:
$$
\begin{aligned}
a &= a_{\mathrm{rad}} \\
&= r\omega^2 \\
&= (1{,}50)(6{,}00)^2 \\
&= (1{,}50)(36{,}0) \\
&= 54{,}0\,\mathrm{m/s^2}.
\end{aligned}
$$

Hướng của gia tốc: Nằm trong mặt phẳng quỹ đạo ngang và luôn hướng thẳng vào trục quay (hướng tâm).

</details>

---

### VP9.5.3

Nếu độ lớn gia tốc của đầu cánh quạt vượt quá một giá trị ngưỡng $a_{\max}$, đầu cánh quạt sẽ bị gãy. Giả sử cánh quạt có bán kính $r$, ban đầu đứng yên và bắt đầu quay với gia tốc góc có độ lớn không đổi $\alpha$. Hỏi tại tốc độ góc $\omega$ bằng bao nhiêu thì đầu cánh quạt sẽ bị gãy?

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Cánh quạt bán kính $r$, bắt đầu quay từ trạng thái nghỉ với gia tốc góc $\alpha = \mathrm{const}$.
- Ngưỡng gia tốc gãy: $a_{\max}$.
- Cần tìm: Tốc độ góc $\omega$ tại thời điểm độ lớn gia tốc toàn phần đạt ngưỡng $a = a_{\max}$.

**Hướng đi:**
- Điểm đầu mút cánh quạt chuyển động tròn có hai thành phần gia tốc vuông góc:
  - Gia tốc tiếp tuyến: $a_{\mathrm{tan}} = r\alpha$.
  - Gia tốc hướng tâm: $a_{\mathrm{rad}} = r\omega^2$.
- Độ lớn gia tốc toàn phần tại mỗi thời điểm là:
$$
\begin{aligned}
a &= \sqrt{a_{\mathrm{tan}}^2 + a_{\mathrm{rad}}^2} \\
&= \sqrt{(r\alpha)^2 + (r\omega^2)^2}
\end{aligned}
$$
- Cho $a = a_{\max}$ và giải phương trình đại số để tìm $\omega$.

**Lời giải chi tiết:**

Biểu diễn độ lớn gia tốc toàn phần của điểm đầu mút:
$$
\begin{aligned}
a &= \sqrt{r^2\alpha^2 + r^2\omega^4} \\
&= r\sqrt{\alpha^2 + \omega^4}
\end{aligned}
$$

Thiết lập điều kiện giới hạn tại thời điểm gãy $a = a_{\max}$:
$$
r\sqrt{\alpha^2 + \omega^4} = a_{\max}
$$

Chia cả hai vế cho $r$ rồi bình phương:
$$
\alpha^2 + \omega^4 = \left(\frac{a_{\max}}{r}\right)^2
$$

Chuyển vế để cô lập $\omega^4$:
$$
\omega^4 = \frac{a_{\max}^2}{r^2} - \alpha^2
$$

Lấy căn bậc bốn hai vế (với điều kiện $a_{\max} > r\alpha$ để cánh quạt không bị gãy ngay tại thời điểm ban đầu do gia tốc tiếp tuyến thuần túy):
$$
\omega = \left(\frac{a_{\max}^2}{r^2} - \alpha^2\right)^{1/4}
$$

Kiểm tra: Nếu $\alpha = 0$ (cánh quạt quay đều), công thức trở về $\omega = \sqrt{a_{\max}/r}$, tức là $a_{\max} = r\omega^2$, hoàn toàn phù hợp với chuyển động tròn đều.

</details>

---

### VP9.5.4

Tại một thời điểm xác định, một bánh xe tuabin bán kính $R$ đang quay với tốc độ góc $\omega$ (tính theo $\mathrm{rad/s}$).
(a) Độ lớn gia tốc góc $\alpha$ (tính theo $\mathrm{rad/s^2}$) của bánh xe tại thời điểm này phải bằng bao nhiêu nếu vector gia tốc $\vec{a}$ của một điểm ở mép bánh xe tạo một góc đúng bằng $30^\circ$ với vector vận tốc $\vec{v}$ của điểm đó?
(b) Cũng tại thời điểm này, góc giữa $\vec{a}$ và $\vec{v}$ đối với một điểm nằm ở vị trí trung điểm giữa trục quay và mép bánh xe bằng bao nhiêu?

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Bánh xe tuabin bán kính $R$, tốc độ góc tức thời $\omega$.
- Tại mép bánh ($r = R$): Góc giữa $\vec{a}$ và $\vec{v}$ bằng $\beta = 30^\circ$.
- Cần tìm: (a) Gia tốc góc $\alpha$ theo $\omega$; (b) Góc $\beta'$ giữa $\vec{a}'$ và $\vec{v}'$ tại điểm $r' = R/2$.

**Hướng đi:**
- Vector vận tốc $\vec{v}$ của một điểm trong chuyển động tròn luôn nằm theo phương tiếp tuyến với quỹ đạo.
- Vector gia tốc $\vec{a} = \vec{a}_{\mathrm{tan}} + \vec{a}_{\mathrm{rad}}$ có thành phần $\vec{a}_{\mathrm{tan}}$ dọc theo phương tiếp tuyến (song song với $\vec{v}$ khi quay nhanh dần) và thành phần $\vec{a}_{\mathrm{rad}}$ vuông góc với tiếp tuyến (hướng vào tâm).
- Do đó, tam giác gia tốc là tam giác vuông, góc $\beta$ giữa $\vec{a}$ và $\vec{v}$ thỏa mãn:
$$
\tan\beta = \frac{a_{\mathrm{rad}}}{a_{\mathrm{tan}}}
$$

**Lời giải chi tiết:**

(a) Xác định gia tốc góc $\alpha$ tại thời điểm đang xét:
Với điểm trên mép bánh xe bán kính $R$:
$$
\begin{aligned}
&a_{\mathrm{tan}} = R\alpha, \\
&a_{\mathrm{rad}} = R\omega^2.
\end{aligned}
$$

Góc $\beta$ giữa vector gia tốc toàn phần $\vec{a}$ và vector vận tốc tiếp tuyến $\vec{v}$ thỏa mãn:
$$
\begin{aligned}
\tan\beta &= \frac{a_{\mathrm{rad}}}{a_{\mathrm{tan}}} \\
&= \frac{R\omega^2}{R\alpha} \\
&= \frac{\omega^2}{\alpha}
\end{aligned}
$$

Theo giả thiết $\beta = 30^\circ$, ta có:
$$
\tan 30^\circ = \frac{1}{\sqrt{3}}
$$

Thay vào phương trình:
$$
\frac{\omega^2}{\alpha} = \frac{1}{\sqrt{3}}
$$

Từ đó:

$$
\alpha = \sqrt{3}\omega^2
$$

(b) Tính góc giữa vector gia tốc và vận tốc tại trung điểm $r' = R/2$:
Tại vị trí $r' = R/2$, các thành phần gia tốc là:
$$
\begin{aligned}
a_{\mathrm{tan}}' &= r'\alpha \\
&= \left(\frac{R}{2}\right)\alpha, \\
a_{\mathrm{rad}}' &= r'\omega^2 \\
&= \left(\frac{R}{2}\right)\omega^2.
\end{aligned}
$$

Tang của góc $\beta'$ giữa $\vec{a}'$ và $\vec{v}'$ là:
$$
\begin{aligned}
\tan\beta' &= \frac{a_{\mathrm{rad}}'}{a_{\mathrm{tan}}'} \\
&= \frac{r'\omega^2}{r'\alpha} \\
&= \frac{\omega^2}{\alpha}
\end{aligned}
$$

Khoảng cách $r'$ triệt tiêu hoàn toàn khỏi tỉ số. Vì cả $\omega$ và $\alpha$ đều là đại lượng chung cho toàn bộ vật rắn tại thời điểm khảo sát, ta có:
$$
\begin{aligned}
\tan\beta' &= \frac{\omega^2}{\alpha} \\
&= \tan 30^\circ
\end{aligned}
$$

Từ đó:

$$
\beta' = 30^\circ
$$

Kết luận: Góc giữa vector gia tốc và vector vận tốc đồng nhất tại mọi điểm trên vật rắn (trừ các điểm nằm chính xác trên trục quay nơi vận tốc bằng $0$).

</details>

---

### VP9.8.1

Một hình trụ đặc đồng chất có khối lượng $12{,}0\,\mathrm{kg}$ và bán kính $0{,}250\,\mathrm{m}$ có thể quay không ma sát quanh trục đối xứng đi qua tâm. Bạn thực hiện một công $75{,}0\,\mathrm{J}$ lên hình trụ để tăng tốc độ góc của nó. Tốc độ góc cuối cùng của hình trụ bằng bao nhiêu nếu hình trụ:
(a) Bắt đầu quay từ trạng thái nghỉ.
(b) Ban đầu đang quay với tốc độ góc $12{,}0\,\mathrm{rad/s}$?

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Khối lượng hình trụ: $M = 12{,}0\,\mathrm{kg}$.
- Bán kính hình trụ: $R = 0{,}250\,\mathrm{m}$.
- Công thực hiện: $W = 75{,}0\,\mathrm{J}$.
- Cần tìm: Tốc độ góc cuối $\omega_2$ khi (a) $\omega_1 = 0$; (b) $\omega_1 = 12{,}0\,\mathrm{rad/s}$.

**Hướng đi:**
- Xác định mômen quán tính của hình trụ đặc quay quanh trục đối xứng:
$$
I = \frac{1}{2}MR^2
$$
- Áp dụng định lý động năng cho chuyển động quay: Công thực hiện lên vật rắn bằng độ biến thiên động năng quay:
$$
\begin{aligned}
W &= K_2 - K_1 \\
&= \frac{1}{2}I\omega_2^2 - \frac{1}{2}I\omega_1^2
\end{aligned}
$$
- Từ đó suy ra tốc độ góc cuối cùng:
$$
\omega_2 = \sqrt{\omega_1^2 + \frac{2W}{I}}
$$

**Lời giải chi tiết:**

Tính mômen quán tính của hình trụ đặc:
$$
\begin{aligned}
I &= \frac{1}{2}MR^2 \\
&= \frac{1}{2}(12{,}0)(0{,}250)^2 \\
&= 6{,}00 \times 0{,}0625 \\
&= 0{,}375\,\mathrm{kg\cdot m^2}.
\end{aligned}
$$

Số hạng biến thiên bình phương tốc độ góc do công $W$ gây ra là:
$$
\begin{aligned}
\frac{2W}{I} &= \frac{2(75{,}0)}{0{,}375} \\
&= \frac{150{,}0}{0{,}375} \\
&= 400{,}0\,\mathrm{rad^2/s^2}
\end{aligned}
$$

(a) Khi hình trụ quay từ trạng thái nghỉ ($\omega_1 = 0$):
$$
\begin{aligned}
\omega_2 &= \sqrt{0 + 400{,}0} \\
&= 20{,}0\,\mathrm{rad/s}
\end{aligned}
$$

(b) Khi ban đầu hình trụ đang quay với $\omega_1 = 12{,}0\,\mathrm{rad/s}$:
$$
\begin{aligned}
\omega_2 &= \sqrt{(12{,}0)^2 + 400{,}0} \\
&= \sqrt{144{,}0 + 400{,}0} \\
&= \sqrt{544{,}0} \\
&\approx 23{,}324\,\mathrm{rad/s} \\
&\approx 23{,}3\,\mathrm{rad/s}.
\end{aligned}
$$

Kiểm tra: Vì động năng phụ thuộc bậc hai vào tốc độ góc, cùng một lượng công $75{,}0\,\mathrm{J}$ ở câu (b) chỉ làm tốc độ góc tăng thêm $23{,}3 - 12{,}0 = 11{,}3\,\mathrm{rad/s}$, nhỏ hơn mức tăng $20{,}0\,\mathrm{rad/s}$ khi xuất phát từ trạng thái nghỉ.

</details>

---

### VP9.8.2

Một tấm phẳng hình vuông đồng chất có khối lượng $0{,}600\,\mathrm{kg}$ và các cạnh dài $0{,}150\,\mathrm{m}$. Tấm phẳng có thể quay không ma sát quanh trục đi qua tâm và vuông góc với mặt phẳng tấm. Bạn phải thực hiện một công bằng bao nhiêu lên tấm phẳng để thay đổi tốc độ góc của nó:
(a) Từ $0$ đến $40{,}0\,\mathrm{rad/s}$?
(b) Từ $40{,}0\,\mathrm{rad/s}$ đến $80{,}0\,\mathrm{rad/s}$?

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Tấm phẳng hình vuông: $M = 0{,}600\,\mathrm{kg}$, cạnh $a = b = 0{,}150\,\mathrm{m}$.
- Cần tìm: Công $W$ cần thực hiện khi tốc độ góc thay đổi:
  - (a) Từ $\omega_1 = 0$ đến $\omega_2 = 40{,}0\,\mathrm{rad/s}$.
  - (b) Từ $\omega_2 = 40{,}0\,\mathrm{rad/s}$ đến $\omega_3 = 80{,}0\,\mathrm{rad/s}$.

**Hướng đi:**
- Mômen quán tính của tấm chữ nhật cạnh $a, b$ quanh trục đi qua tâm vuông góc với bản mặt là:
$$
I = \frac{1}{12}M(a^2 + b^2)
$$
- Với tấm vuông cạnh $a$, công thức rút gọn thành $I = \frac{1}{6}Ma^2$.
- Theo định lý động năng, công cần thực hiện đúng bằng độ tăng động năng quay:
$$
\begin{aligned}
W &= \Delta K \\
&= \frac{1}{2}I(\omega_{\mathrm{sau}}^2 - \omega_{\mathrm{truoc}}^2)
\end{aligned}
$$

**Lời giải chi tiết:**

Tính mômen quán tính của tấm vuông:
$$
\begin{aligned}
I &= \frac{1}{6}Ma^2 \\
&= \frac{1}{6}(0{,}600)(0{,}150)^2 \\
&= 0{,}100 \times 0{,}0225 \\
&= 0{,}00225\,\mathrm{kg\cdot m^2} \\
&= 2{,}25 \times 10^{-3}\,\mathrm{kg\cdot m^2}.
\end{aligned}
$$

(a) Công để tăng tốc từ $0$ lên $40{,}0\,\mathrm{rad/s}$:
$$
\begin{aligned}
W_a &= \frac{1}{2}I(\omega_2^2 - \omega_1^2) \\
&= (0{,}001125)(1600) \\
&= 1{,}80\,\mathrm{J}.
\end{aligned}
$$

(b) Công để tăng tốc từ $40{,}0\,\mathrm{rad/s}$ lên $80{,}0\,\mathrm{rad/s}$:
$$
\begin{aligned}
W_b &= \frac{1}{2}I(\omega_3^2 - \omega_2^2) \\
&= (0{,}001125)(4800) \\
&= 5{,}40\,\mathrm{J}.
\end{aligned}
$$

Kiểm tra: Hiệu số bình phương ở câu (b) là $80^2 - 40^2 = 3(40^2)$, do đó công ở câu (b) gấp đúng ba lần công ở câu (a): $W_b=3W_a$, tức $5{,}40\,\mathrm J$.

</details>

---

### VP9.8.3

Một hình trụ rỗng đồng chất có khối lượng $2{,}00\,\mathrm{kg}$, bán kính trong $0{,}100\,\mathrm{m}$ và bán kính ngoài $0{,}200\,\mathrm{m}$ có thể quay không ma sát quanh một trục nằm ngang bán kính $0{,}100\,\mathrm{m}$ dọc theo trục hình trụ. Người ta quấn một sợi dây nhẹ, không dãn quanh mặt ngoài của hình trụ rồi buộc đầu tự do vào một khối pho mát có khối lượng $0{,}500\,\mathrm{kg}$. Khối pho mát được thả rơi từ trạng thái nghỉ ở độ cao $h$ so với sàn nhà.
(a) Nếu khối pho mát chuyển động đi xuống với tốc độ $4{,}00\,\mathrm{m/s}$ ngay trước khi chạm đất, độ cao $h$ bằng bao nhiêu?
(b) Tốc độ góc của hình trụ ngay trước khi khối pho mát chạm đất bằng bao nhiêu?

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Hình trụ rỗng: $M = 2{,}00\,\mathrm{kg}$, $R_1 = 0{,}100\,\mathrm{m}$, $R_2 = 0{,}200\,\mathrm{m}$.
- Dây quấn quanh mặt ngoài bán kính $R_2$.
- Khối pho mát: $m = 0{,}500\,\mathrm{kg}$, thả từ nghỉ ở độ cao $h$.
- Vận tốc khi chạm đất: $v = 4{,}00\,\mathrm{m/s}$.
- Gia tốc trọng trường: $g = 9{,}80\,\mathrm{m/s^2}$.
- Cần tìm: (a) Độ cao $h$; (b) Tốc độ góc cuối $\omega$ của hình trụ.

**Hướng đi:**
- Dây không dãn và không trượt trên mép ngoài hình trụ, nên tốc độ rơi của pho mát liên hệ chặt chẽ với tốc độ góc của hình trụ qua hệ thức liên kết: $v = R_2\omega$.
- Mômen quán tính của hình trụ rỗng có bán kính trong $R_1$ và bán kính ngoài $R_2$ là:
$$
I = \frac{1}{2}M(R_1^2 + R_2^2)
$$
- Hệ cơ học gồm khối pho mát và hình trụ không chịu ma sát cản trở, cơ năng được bảo toàn: Thế năng ban đầu của khối pho mát chuyển hóa thành động năng tịnh tiến của pho mát và động năng quay của hình trụ.

**Lời giải chi tiết:**

(b) Tính tốc độ góc của hình trụ ngay trước khi pho mát chạm đất:
Vì dây quấn ở vành ngoài bán kính $R_2 = 0{,}200\,\mathrm{m}$:
$$
\begin{aligned}
\omega &= \frac{v}{R_2} \\
&= \frac{4{,}00}{0{,}200} \\
&= 20{,}0\,\mathrm{rad/s}.
\end{aligned}
$$

(a) Tính độ cao $h$:
Mômen quán tính của hình trụ rỗng:
$$
\begin{aligned}
I &= \frac{1}{2}M(R_1^2 + R_2^2) \\
&= 0{,}0100+0{,}0400 \\
&= 0{,}0500\,\mathrm{kg\cdot m^2}.
\end{aligned}
$$

Động năng tịnh tiến của khối pho mát ngay trước khi chạm đất:
$$
\begin{aligned}
K_{\mathrm{trans}} &= \frac{1}{2}mv^2 \\
&= \frac{1}{2}(0{,}500)(4{,}00)^2 \\
&= 4{,}00\,\mathrm{J}
\end{aligned}
$$

Động năng quay của hình trụ tại thời điểm đó:
$$
\begin{aligned}
K_{\mathrm{rot}} &= \frac{1}{2}I\omega^2 \\
&= \frac{1}{2}(0{,}0500)(20{,}0)^2 \\
&= 10{,}00\,\mathrm{J}
\end{aligned}
$$

Tổng động năng của hệ là:
$$
\begin{aligned}
K_{\mathrm{tong}} &= K_{\mathrm{trans}} + K_{\mathrm{rot}} \\
&= 4{,}00 + 10{,}00 \\
&= 14{,}00\,\mathrm{J}
\end{aligned}
$$

Chọn mốc thế năng trọng trường tại mặt sàn. Áp dụng định luật bảo toàn cơ năng cho hệ từ trạng thái nghỉ:
$$
mgh = K_{\mathrm{tong}}
$$

Suy ra độ cao thả ban đầu:
$$
\begin{aligned}
h &= \frac{K_{\mathrm{tong}}}{mg} \\
&= \frac{14{,}00}{(0{,}500)(9{,}80)} \\
&= \frac{14{,}00}{4{,}90} \\
&\approx 2{,}8571\,\mathrm{m} \\
&\approx 2{,}86\,\mathrm{m}.
\end{aligned}
$$

Kiểm tra: Khối lượng hình trụ tương đối lớn làm phần lớn cơ năng ($10{,}00\,\mathrm{J}$ trong tổng số $14{,}00\,\mathrm{J}$, tức khoảng $71{,}4\%$) tích lũy dưới dạng động năng quay.

</details>

---

### VP9.8.4

Một ròng rọc có dạng hình trụ đặc đồng chất khối lượng $1{,}50\,\mathrm{kg}$ và bán kính $0{,}240\,\mathrm{m}$ có thể quay quanh một trục nằm ngang đi qua tâm ròng rọc. Giữa ròng rọc và trục quay có lực ma sát. Một sợi dây nhẹ không dãn được quấn quanh ròng rọc, đầu tự do gắn với một cuốn sách giáo khoa khối lượng $2{,}00\,\mathrm{kg}$. Cuốn sách được thả từ trạng thái nghỉ ở độ cao $0{,}900\,\mathrm{m}$ so với sàn. Ngay trước khi cuốn sách chạm sàn, tốc độ góc của ròng rọc đạt $10{,}0\,\mathrm{rad/s}$.
(a) Tốc độ của cuốn sách ngay trước khi chạm sàn bằng bao nhiêu?
(b) Lực ma sát ở trục quay đã thực hiện một công bằng bao nhiêu lên ròng rọc trong suốt thời gian cuốn sách rơi xuống sàn?

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Ròng rọc hình trụ đặc: $M = 1{,}50\,\mathrm{kg}$, bán kính $R = 0{,}240\,\mathrm{m}$.
- Cuốn sách: $m = 2{,}00\,\mathrm{kg}$, rơi từ nghỉ từ độ cao $h = 0{,}900\,\mathrm{m}$.
- Tốc độ góc cuối của ròng rọc: $\omega = 10{,}0\,\mathrm{rad/s}$.
- Cần tìm: (a) Tốc độ cuối $v$ của sách; (b) Công của lực ma sát $W_f$.

**Hướng đi:**
- Dây không dãn và không trượt cho liên hệ vận tốc dài và góc: $v = R\omega$.
- Ròng rọc là hình trụ đặc có mômen quán tính $I = \frac{1}{2}MR^2$.
- Vì có ma sát tiêu tán cơ năng tại ổ trục, ta áp dụng định lý biến thiên cơ năng tổng quát:
Ở đây $W$ là công của các lực ngoài khác đang xét.

$$
K_1+U_1+W=K_2+U_2
$$
với $W_{\mathrm{khac}} = W_f$ là công của lực ma sát.

**Lời giải chi tiết:**

(a) Tính tốc độ của cuốn sách ngay trước khi chạm sàn:
Do dây không trượt trên rãnh ròng rọc:
$$
\begin{aligned}
v &= R\omega \\
&= (0{,}240)(10{,}0) \\
&= 2{,}40\,\mathrm{m/s}.
\end{aligned}
$$

(b) Tính công của lực ma sát tại trục quay:
Mômen quán tính của ròng rọc hình trụ đặc:
$$
\begin{aligned}
I &= \frac{1}{2}MR^2 \\
&= \frac{1}{2}(1{,}50)(0{,}240)^2 \\
&= 0{,}750 \times 0{,}0576 \\
&= 0{,}0432\,\mathrm{kg\cdot m^2}.
\end{aligned}
$$

Động năng tịnh tiến của cuốn sách khi chạm sàn:
$$
\begin{aligned}
K_{\mathrm{sach}} &= \frac{1}{2}mv^2 \\
&= \frac{1}{2}(2{,}00)(2{,}40)^2 \\
&= 5{,}76\,\mathrm{J}
\end{aligned}
$$

Động năng quay của ròng rọc khi cuốn sách chạm sàn:
$$
\begin{aligned}
K_{\mathrm{rr}} &= \frac{1}{2}I\omega^2 \\
&= \frac{1}{2}(0{,}0432)(10{,}0)^2 \\
&= 2{,}16\,\mathrm{J}
\end{aligned}
$$

Tổng động năng cuối của hệ là:
$$
\begin{aligned}
K_2 &= K_{\mathrm{sach}} + K_{\mathrm{rr}} \\
&= 5{,}76 + 2{,}16 \\
&= 7{,}92\,\mathrm{J}
\end{aligned}
$$

Chọn mốc thế năng trọng trường tại mặt sàn. Thế năng ban đầu của hệ khi sách ở độ cao $h$:
$$
\begin{aligned}
U_1 &= mgh \\
&= (2{,}00)(9{,}80)(0{,}900) \\
&= 17{,}64\,\mathrm{J}
\end{aligned}
$$

Ban đầu hệ đứng yên nên $K_1 = 0$, khi chạm sàn thế năng $U_2 = 0$. Áp dụng định lý biến thiên cơ năng:
Với $\Delta K=K_2-K_1$ và $\Delta U=U_2-U_1$, phương trình năng lượng là:

$$
\Delta K+\Delta U=W_f
$$

Biến đổi để tìm công ma sát:
$$
\begin{aligned}
W_f &= K_2 - U_1 \\
&= 7{,}92 - 17{,}64 \\
&= -9{,}72\,\mathrm{J}.
\end{aligned}
$$

Kiểm tra: Dấu âm của công ($W_f = -9{,}72\,\mathrm{J}$) phản ánh đúng bản chất lực ma sát cản trở chuyển động quay, làm tiêu tán $9{,}72\,\mathrm{J}$ cơ năng của hệ thành nhiệt năng.

</details>
