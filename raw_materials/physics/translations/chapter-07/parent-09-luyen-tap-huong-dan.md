## Luyện tập có hướng dẫn (Guided Practice)

Các bài toán dưới đây được phát triển từ các ví dụ trọng tâm trong chương, nhằm rèn luyện tư duy vận dụng định luật bảo toàn cơ năng và định lý công và động năng trong các tình huống biến đổi thực tế.

---

### VP7.2.1 - Ném bóng chày theo phương thẳng đứng

Một quả bóng chày có khối lượng $0{,}145\,\mathrm{kg}$ được ném thẳng đứng lên trên từ tay người ném với tốc độ ban đầu $12{,}0\,\mathrm{m/s}$. Bỏ qua lực cản của không khí. Xác định độ cao của quả bóng so với vị trí rời tay khi:
(a) Tốc độ hướng lên của quả bóng bằng một nửa tốc độ ban đầu.
(b) Động năng của quả bóng bằng một nửa động năng ban đầu.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**

- Khối lượng quả bóng: $m = 0{,}145\,\mathrm{kg}$.

- Vận tốc ban đầu: $v_0 = 12{,}0\,\mathrm{m/s}$.

- Bỏ qua lực cản không khí. Gia tốc trọng trường $g = 9{,}80\,\mathrm{m/s^2}$.

- Tìm độ cao $y_a$ khi $v = v_0 / 2$ và độ cao $y_b$ khi $K = K_0 / 2$.

**Hướng đi:**

- Khi bỏ qua lực cản không khí, trọng lực là lực thế duy nhất tác dụng lên quả bóng. Do đó, cơ năng toàn phần của hệ gồm quả bóng và Trái Đất được bảo toàn trong suốt quá trình chuyển động.

- Chọn mốc thế năng trọng trường tại vị trí quả bóng rời tay ($y_0 = 0$). Cơ năng ban đầu của bóng hoàn toàn ở dạng động năng:
$$
E_0 = \frac{1}{2}mv_0^2
$$

- Tại vị trí có độ cao $y$, cơ năng gồm cả động năng và thế năng trọng trường:
$$
E = \frac{1}{2}mv^2 + mgy
$$

- Áp dụng định luật bảo toàn cơ năng $E = E_0$ cho từng phần để tìm độ cao tương ứng.

**Lời giải:**

(a) Độ cao khi tốc độ bằng một nửa tốc độ ban đầu:

- Vận tốc tại độ cao này là $v = v_0 / 2 = 6{,}00\,\mathrm{m/s}$.

- Bảo toàn cơ năng giữa vị trí ném và độ cao $y_a$:
$$
\frac{1}{2}mv_0^2 = \frac{1}{8}mv_0^2 + mgy_a
$$

- Triệt tiêu khối lượng $m$ ở hai vế và rút gọn:
$$
\begin{aligned}
gy_a &= \frac{1}{2}v_0^2 - \frac{1}{8}v_0^2 \\
&= \frac{3}{8}v_0^2.
\end{aligned}
$$

- Độ cao $y_a$ cần tìm:
$$
\begin{aligned}
y_a &= \frac{3v_0^2}{8g} \\
&= \frac{3(12{,}0)^2}{8(9{,}80)} \\
&= \frac{432}{78{,}4} \\
&\approx 5{,}51\,\mathrm{m}.
\end{aligned}
$$

(b) Độ cao khi động năng bằng một nửa động năng ban đầu:

- Điều kiện đề bài: $K_b = \frac{1}{2}K_0$.

- Theo định luật bảo toàn cơ năng, độ giảm động năng đúng bằng độ tăng thế năng trọng trường:
$$
\begin{aligned}
\Delta U &= K_0 - K_b \\
&= \frac{1}{2}K_0.
\end{aligned}
$$

- Vì $\frac{1}{2}K_0 = \frac{1}{4}mv_0^2$, biểu thức thế năng trở thành:
$$
mgy_b = \frac{1}{4}mv_0^2
$$

- Suy ra độ cao $y_b$:
$$
\begin{aligned}
y_b &= \frac{v_0^2}{4g} \\
&= \frac{(12{,}0)^2}{4(9{,}80)} \\
&= \frac{144}{39{,}2} \\
&\approx 3{,}67\,\mathrm{m}.
\end{aligned}
$$

Nhận xét: Vì động năng tỉ lệ với bình phương vận tốc, khi vận tốc giảm một nửa thì động năng đã giảm đi ba phần tư, do đó bóng đạt được $y_b < y_a$.

</details>

---

### VP7.2.2 - Ném đá lên cao và biểu thức vận tốc tổng quát

Một hòn đá có khối lượng $m$ được tung thẳng đứng lên trên. Bỏ qua lực cản của không khí. Hòn đá đạt độ cao cực đại $h$ so với vị trí rời tay. Xác định tốc độ của hòn đá theo $g$ và $h$ khi nó ở độ cao:
(a) $y = h/4$.
(b) $y = 3h/4$.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**

- Khối lượng vật: $m$.

- Độ cao cực đại: $h$.

- Bỏ qua lực cản không khí.

- Tìm tốc độ $v$ tại các độ cao $y = h/4$ và $y = 3h/4$.

**Hướng đi:**

- Bỏ qua lực cản không khí nên cơ năng toàn phần được bảo toàn.

- Tại đỉnh quỹ đạo ($y = h$), tốc độ của hòn đá tức thời bằng không, cơ năng của vật hoàn toàn chuyển thành thế năng cực đại:
$$
E = mgh
$$

- Tại độ cao bất kỳ $y$, cơ năng là tổng động năng và thế năng:
$$
E = \frac{1}{2}mv^2 + mgy
$$

- Đồng nhất hai biểu thức cơ năng giúp xác định trực tiếp tốc độ $v$ mà không cần tính qua vận tốc ban đầu.

**Lời giải:**

(a) Tốc độ tại độ cao $y = h/4$:

- Áp dụng bảo toàn cơ năng:
$$
\frac{1}{2}mv^2 + mg\left(\frac{h}{4}\right) = mgh
$$

- Chuyển vế và triệt tiêu khối lượng $m$:
$$
\begin{aligned}
\frac{1}{2}v^2 &= gh - \frac{1}{4}gh \\
&= \frac{3}{4}gh.
\end{aligned}
$$

- Suy ra tốc độ:
$$
v = \sqrt{\frac{3gh}{2}}
$$

(b) Tốc độ tại độ cao $y = 3h/4$:

- Tương tự, tại vị trí $y = 3h/4$:
$$
\frac{1}{2}mv^2 + mg\left(\frac{3h}{4}\right) = mgh
$$

- Rút gọn động năng riêng phần:
$$
\begin{aligned}
\frac{1}{2}v^2 &= gh - \frac{3}{4}gh \\
&= \frac{1}{4}gh.
\end{aligned}
$$

- Suy ra tốc độ:
$$
v = \sqrt{\frac{gh}{2}}
$$

</details>

---

### VP7.2.3 - Ném bóng tennis có lực cản không khí

Một quả bóng tennis có khối lượng $0{,}0570\,\mathrm{kg}$ được ném thẳng đứng lên trên với tốc độ ban đầu $15{,}0\,\mathrm{m/s}$. Lực cản của không khí không thể bỏ qua, khiến quả bóng chỉ đạt độ cao cực đại là $8{,}00\,\mathrm{m}$.
(a) Cơ năng toàn phần của quả bóng giảm đi một lượng bằng bao nhiêu từ lúc rời tay đến khi đạt độ cao cực đại?
(b) Độ lớn của lực cản không khí trung bình tác dụng lên quả bóng là bao nhiêu?

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**

- Khối lượng bóng tennis: $m = 0{,}0570\,\mathrm{kg}$.

- Vận tốc ban đầu: $v_0 = 15{,}0\,\mathrm{m/s}$.

- Độ cao cực đại thực tế: $h = 8{,}00\,\mathrm{m}$.

- Tìm độ giảm cơ năng $\Delta E_{\mathrm{mech}}$ và độ lớn lực cản trung bình $f_{\mathrm{air}}$.

**Hướng đi:**

- Lực cản không khí là lực không thế (không bảo toàn) và luôn sinh công âm khi vật đi lên.

- Định lý công và cơ năng phát biểu rằng độ biến thiên cơ năng toàn phần của hệ bằng công của các lực không thế:
$$
W_{\mathrm{other}} = E_2 - E_1
$$

- Với $E_1 = \frac{1}{2}mv_0^2$ (chọn mốc thế năng tại điểm ném) và $E_2 = mgh$ (tại đỉnh độ cao vận tốc bằng không).

- Công của lực cản trung bình ngược chiều chuyển động dọc theo quãng đường $h$ là $W_{\mathrm{other}} = -f_{\mathrm{air}} h$.

**Lời giải:**

(a) Độ biến thiên và độ giảm của cơ năng:

- Cơ năng ban đầu của quả bóng:
$$
\begin{aligned}
E_1 &= \frac{1}{2}mv_0^2 \\
&= \frac{1}{2}(0{,}0570)(15{,}0)^2 \\
&= 6{,}4125\,\mathrm{J}.
\end{aligned}
$$

- Cơ năng tại vị trí cao nhất:
$$
\begin{aligned}
E_2 &= mgh \\
&= 0{,}0570(9{,}80)(8{,}00) \\
&= 4{,}4688\,\mathrm{J}.
\end{aligned}
$$

- Độ biến thiên cơ năng của quả bóng:
$$
\begin{aligned}
\Delta E &= E_2 - E_1 \\
&= 4{,}4688 - 6{,}4125 \\
&= -1{,}9437\,\mathrm{J}.
\end{aligned}
$$

- Cơ năng toàn phần giảm đi một lượng:
$$
|\Delta E| \approx 1{,}94\,\mathrm{J}
$$

(b) Độ lớn lực cản trung bình của không khí:

- Lực cản hướng ngược chiều dịch chuyển, công thực hiện:
$$
W_{\mathrm{air}} = -f_{\mathrm{air}} h
$$

- Theo định lý công và cơ năng, $W_{\mathrm{air}} = \Delta E$:
$$
-f_{\mathrm{air}} h = -1{,}9437\,\mathrm{J}
$$

- Độ lớn lực cản trung bình:
$$
\begin{aligned}
f_{\mathrm{air}} &= \frac{1{,}9437}{8{,}00} \\
&\approx 0{,}243\,\mathrm{N}.
\end{aligned}
$$

</details>

---

### VP7.2.4 - Đỡ bóng chuyền rơi xuống

Bạn đỡ một quả bóng chuyền có khối lượng $0{,}270\,\mathrm{kg}$ đang rơi thẳng đứng xuống với tốc độ $7{,}50\,\mathrm{m/s}$. Để hãm dừng quả bóng, tay bạn cùng quả bóng hạ xuống một đoạn thẳng đứng $0{,}150\,\mathrm{m}$.
(a) Hai tay bạn đã thực hiện một công bằng bao nhiêu lên quả bóng trong quá trình hãm dừng nó?
(b) Độ lớn lực trung bình (coi như không đổi) mà tay bạn tác dụng lên quả bóng là bao nhiêu?

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**

- Khối lượng quả bóng: $m = 0{,}270\,\mathrm{kg}$.

- Tốc độ ban đầu: $v_1 = 7{,}50\,\mathrm{m/s}$.

- Quãng đường hãm: $d = 0{,}150\,\mathrm{m}$.

- Trạng thái cuối: Bóng dừng lại ($v_2 = 0$).

- Tìm công do tay thực hiện $W_{\mathrm{hands}}$ và lực tác dụng $F_{\mathrm{hands}}$.

**Hướng đi:**

- Lực do bàn tay tác dụng lên bóng là ngoại lực không thế. Áp dụng định lý công và cơ năng:
$$
W_{\mathrm{hands}} = E_2 - E_1
$$

- Chọn mốc thế năng trọng trường tại vị trí thấp nhất khi bóng dừng hẳn ($y_2 = 0$). Khi bắt đầu chạm tay, bóng ở độ cao $y_1 = d = 0{,}150\,\mathrm{m}$.

- Lực do bàn tay hướng lên trên để hãm chuyển động, ngược chiều với độ dời đi xuống của bóng, nên sinh công âm:
$$
W_{\mathrm{hands}} = -F_{\mathrm{hands}} d
$$

**Lời giải:**

(a) Công do tay thực hiện lên bóng:

- Cơ năng ban đầu khi bóng chạm tay gồm động năng và thế năng:
$$
\begin{aligned}
K_1 &= \frac{1}{2}(0{,}270)(7{,}50)^2 \\
&= 7{,}5938\,\mathrm{J}, \\
U_1 &= 0{,}270(9{,}80)(0{,}150) \\
&= 0{,}3969\,\mathrm{J}.
\end{aligned}
$$

- Tổng cơ năng ban đầu:
$$
\begin{aligned}
E_1 &= K_1 + U_1 \\
&= 7{,}5938 + 0{,}3969 \\
&= 7{,}9907\,\mathrm{J}.
\end{aligned}
$$

- Cơ năng ở trạng thái dừng hẳn ($v_2 = 0, y_2 = 0$):
$$
E_2 = 0
$$

- Công do tay thực hiện lên quả bóng:
$$
\begin{aligned}
W_{\mathrm{hands}} &= E_2 - E_1 \\
&= -7{,}99065\,\mathrm{J} \\
&\approx -7{,}99\,\mathrm{J}.
\end{aligned}
$$

(b) Độ lớn lực hãm trung bình do tay tác dụng:

- Vì lực hãm ngược chiều chuyển động nên $W_{\mathrm{hands}} = -F_{\mathrm{hands}} d$.

- Độ lớn của lực trung bình:
$$
\begin{aligned}
F_{\mathrm{hands}} &= \frac{|W_{\mathrm{hands}}|}{d} \\
&= \frac{7{,}99065}{0{,}150} \\
&\approx 53{,}3\,\mathrm{N}.
\end{aligned}
$$

</details>

---

### VP7.5.1 - Miếng bơ trượt trong bát kim loại bán cầu

Một chiếc bát kim loại nhẵn bóng, trơn láng hoàn toàn và không có ma sát, có dạng bán cầu bán kính $0{,}150\,\mathrm{m}$. Đặt một miếng bơ nhỏ có khối lượng $5{,}00 \times 10^{-3}\,\mathrm{kg}$ tại mép bát rồi thả nhẹ cho trượt xuống đáy.
(a) Tốc độ của miếng bơ khi chạm đáy bát là bao nhiêu?
(b) Tại đáy bát, lực do thành bát tác dụng lên miếng bơ là bao nhiêu? So sánh lực này với trọng lượng của miếng bơ.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**

- Bán kính bát bán cầu: $R = 0{,}150\,\mathrm{m}$.

- Khối lượng miếng bơ: $m = 5{,}00 \times 10^{-3}\,\mathrm{kg}$.

- Thả từ trạng thái nghỉ tại mép bát ($v_0 = 0$). Bỏ qua ma sát.

- Tìm tốc độ tại đáy $v$, lực pháp tuyến $N$ và tỉ số $N / mg$.

**Hướng đi:**

- Bỏ qua ma sát, lực pháp tuyến của thành bát luôn vuông góc với phương tiếp tuyến của quỹ đạo chuyển động nên không sinh công. Cơ năng toàn phần của miếng bơ được bảo toàn.

- Độ giảm thế năng trọng trường chuyển hóa hoàn toàn thành động năng tại đáy bát.

- Tại đáy bát, miếng bơ chuyển động tròn theo cung cong bán kính $R$. Hợp lực tác dụng lên bơ đóng vai trò lực hướng tâm hướng về tâm bát. Áp dụng định luật II Newton tại điểm thấp nhất.

**Lời giải:**

(a) Tốc độ của miếng bơ tại đáy:

- Chọn mốc thế năng trọng trường tại đáy bát ($y = 0$). Tại mép bát, độ cao là $y = R$.

- Bảo toàn cơ năng từ mép bát xuống đáy:
$$
mgR = \frac{1}{2}mv^2
$$

- Suy ra tốc độ tại đáy:
$$
\begin{aligned}
v &= \sqrt{2gR} \\
&= \sqrt{2(9{,}80)(0{,}150)} \\
&= \sqrt{2{,}94} \\
&\approx 1{,}71\,\mathrm{m/s}.
\end{aligned}
$$

(b) Lực do lòng bát tác dụng lên miếng bơ:

- Tại đáy bát, các lực tác dụng gồm trọng lực $\vec{P}$ hướng xuống và lực pháp tuyến $\vec{N}$ hướng thẳng đứng lên trên.

- Phương trình định luật II Newton theo phương hướng tâm:
$$
N - mg = \frac{mv^2}{R}
$$

- Thay biểu thức $v^2 = 2gR$ vào phương trình:
$$
\begin{aligned}
N &= mg + \frac{m(2gR)}{R} \\
&= mg + 2mg \\
&= 3mg.
\end{aligned}
$$

- Tính giá trị số:
$$
\begin{aligned}
N &= 3(5{,}00 \times 10^{-3})(9{,}80) \\
&= 0{,}147\,\mathrm{N}.
\end{aligned}
$$

- So sánh với trọng lượng $P = mg$:
Lực pháp tuyến gấp đúng $3{,}00$ lần trọng lượng của miếng bơ.

</details>

---

### VP7.5.2 - Vận động viên trượt ván trên rãnh cong

Một vận động viên trượt ván cùng ván trượt (tổng khối lượng $40{,}0\,\mathrm{kg}$) đang chuyển động với tốc độ $9{,}30\,\mathrm{m/s}$ tại điểm thấp nhất của một rãnh cong.
(a) Nếu bỏ qua ma sát, độ cao thẳng đứng cực đại mà cô ấy có thể trượt lên hai bên sườn rãnh là bao nhiêu? Kết quả này có phụ thuộc vào hình dạng rãnh trượt không?
(b) Trong thực tế do có ma sát, độ cao cực đại đo được chỉ là $3{,}50\,\mathrm{m}$. Lực ma sát đã thực hiện một công bằng bao nhiêu lên hệ?

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**

- Tổng khối lượng: $m = 40{,}0\,\mathrm{kg}$.

- Vận tốc tại đáy rãnh: $v = 9{,}30\,\mathrm{m/s}$.

- (a) Bỏ qua ma sát: Tìm độ cao cực đại $h_{\mathrm{max}}$ và phân tích sự phụ thuộc hình dạng.

- (b) Độ cao thực tế $h = 3{,}50\,\mathrm{m}$: Tính công ma sát $W_f$.

**Hướng đi:**

- Khi không có ma sát, lực pháp tuyến không sinh công, toàn bộ động năng tại đáy chuyển đổi thành thế năng trọng trường tại vị trí cao nhất.

- Trọng lực là lực thế, công của trọng lực chỉ phụ thuộc vào độ chênh lệch độ cao giữa điểm đầu và điểm cuối mà không phụ thuộc vào quỹ đạo hình học của rãnh.

- Khi có ma sát, áp dụng định lý công và cơ năng: Công của lực ma sát bằng độ biến thiên cơ năng toàn phần.

**Lời giải:**

(a) Độ cao cực đại khi không có ma sát:

- Bảo toàn cơ năng giữa đáy rãnh ($y = 0$) và điểm dừng cực đại ($v = 0$):
$$
\frac{1}{2}mv^2 = mgh_{\mathrm{max}}
$$

- Rút gọn khối lượng $m$:
$$
\begin{aligned}
h_{\mathrm{max}} &= \frac{v^2}{2g} \\
&= \frac{(9{,}30)^2}{2(9{,}80)} \\
&= \frac{86{,}49}{19{,}60} \\
&\approx 4{,}41\,\mathrm{m}.
\end{aligned}
$$

- Kết quả này hoàn toàn không phụ thuộc vào hình dạng của rãnh trượt, vì công của trọng lực chỉ phụ thuộc độ cao thẳng đứng, còn phản lực của sườn rãnh luôn vuông góc với quỹ đạo nên công bằng không.

(b) Công của lực ma sát trong điều kiện thực tế:

- Cơ năng ban đầu tại đáy rãnh:
$$
\begin{aligned}
E_1 &= \frac{1}{2}mv^2 \\
&= \frac{1}{2}(40{,}0)(9{,}30)^2 \\
&= 1729{,}8\,\mathrm{J}.
\end{aligned}
$$

- Cơ năng tại độ cao thực tế $h = 3{,}50\,\mathrm{m}$:
$$
\begin{aligned}
E_2 &= mgh \\
&= 40{,}0(9{,}80)(3{,}50) \\
&= 1372{,}0\,\mathrm{J}.
\end{aligned}
$$

- Công của lực ma sát:
$$
\begin{aligned}
W_f &= E_2 - E_1 \\
&= 1372{,}0 - 1729{,}8 \\
&\approx -358\,\mathrm{J}.
\end{aligned}
$$

</details>

---

### VP7.5.3 - Con lắc đơn và lực căng dây

Một con lắc đơn gồm quả cầu nhỏ khối lượng $0{,}250\,\mathrm{kg}$ gắn vào đầu một sợi dây nhẹ dài $1{,}20\,\mathrm{m}$. Khi con lắc dao động qua lại, góc lệch cực đại mà dây treo tạo với phương thẳng đứng là $34{,}0^\circ$. Bỏ qua mọi ma sát và lực cản. Tại điểm thấp nhất của quỹ đạo, xác định:
(a) Động năng của quả cầu.
(b) Lực căng của sợi dây.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**

- Khối lượng vật: $m = 0{,}250\,\mathrm{kg}$.

- Chiều dài dây treo: $L = 1{,}20\,\mathrm{m}$.

- Biên độ góc: $\theta_{\mathrm{max}} = 34{,}0^\circ$.

- Bỏ qua ma sát.

- Tìm động năng $K$ và lực căng dây $T$ tại điểm thấp nhất.

**Hướng đi:**

- Lực căng dây luôn vuông góc với vận tốc của vật nên công của lực căng bằng không. Cơ năng toàn phần của con lắc được bảo toàn.

- Độ giảm thế năng trọng trường khi đi từ góc lệch cực đại về vị trí cân bằng chuyển hóa thành động năng tại điểm thấp nhất.

- Tại điểm thấp nhất, quả cầu chuyển động tròn quanh điểm treo. Viết phương trình định luật II Newton theo phương hướng tâm thẳng đứng để tìm lực căng dây.

**Lời giải:**

(a) Động năng tại vị trí thấp nhất:

- Độ chênh lệch độ cao giữa vị trí biên và vị trí cân bằng:
$$
\Delta y = L(1 - \cos\theta_{\mathrm{max}})
$$

- Với $\theta_{\mathrm{max}} = 34{,}0^\circ$, ta có $\cos 34{,}0^\circ \approx 0{,}82904$:
$$
\begin{aligned}
\Delta y &= 1{,}20(1 - 0{,}82904) \\
&= 1{,}20(0{,}17096) \\
&\approx 0{,}20515\,\mathrm{m}.
\end{aligned}
$$

- Bảo toàn cơ năng cho động năng tại đáy:
$$
\begin{aligned}
K &= mg\Delta y \\
&= 0{,}250(9{,}80)(0{,}20515) \\
&\approx 0{,}503\,\mathrm{J}.
\end{aligned}
$$

(b) Lực căng dây tại điểm thấp nhất:

- Phương trình định luật II Newton tại điểm thấp nhất:
$$
T - mg = \frac{mv^2}{L}
$$

- Vì động năng là $K = \frac{1}{2}mv^2$, số hạng hướng tâm là $\frac{mv^2}{L} = \frac{2K}{L}$:
$$
T = mg + \frac{2K}{L}
$$

- Với trọng lượng $mg = 2{,}450\,\mathrm{N}$ và số hạng hướng tâm:
$$
\frac{2K}{L} = \frac{2(0{,}5026)}{1{,}20} \approx 0{,}838\,\mathrm{N}
$$

- Lực căng dây tại đáy:
$$
\begin{aligned}
T &= 2{,}450 + 0{,}838 \\
&\approx 3{,}29\,\mathrm{N}.
\end{aligned}
$$

</details>

---

### VP7.5.4 - Tàu lượn siêu tốc trên vòng tròn thẳng đứng có ma sát

Bạn đang thử nghiệm một toa tàu lượn siêu tốc có khối lượng $m$ chuyển động tròn theo phương thẳng đứng với bán kính $R$. Toa xe bắt đầu từ điểm thấp nhất của vòng tròn (điểm A) với động năng ban đầu $K_i$. Khi toa xe lên tới đỉnh cao nhất của vòng tròn (điểm B), động năng của nó còn lại là $\frac{1}{4}K_i$, đồng thời thế năng trọng trường tăng thêm một lượng bằng $\frac{1}{2}K_i$.
(a) Tìm tốc độ của toa xe tại điểm A theo $g$ và $R$.
(b) Lực ma sát đã thực hiện một công bằng bao nhiêu lên toa xe khi nó di chuyển từ A đến B, tính theo $m, g$ và $R$?
(c) Xác định độ lớn của lực ma sát (coi là không đổi trong suốt chuyển động) theo $m$ và $g$.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**

- Chuyển động tròn đứng bán kính $R$.

- Tại đáy A: Động năng $K_i$.

- Tại đỉnh B: Động năng $K_f = \frac{1}{4}K_i$, thế năng tăng $\Delta U_g = \frac{1}{2}K_i$.

- Tìm tốc độ $v_A$, công ma sát $W_f$, và độ lớn lực ma sát $f$.

**Hướng đi:**

- Độ chênh lệch độ cao giữa đáy và đỉnh vòng tròn đường kính $2R$ là $2R$, từ đó xác định độ tăng thế năng trọng trường tường minh theo $m, g, R$.

- Đồng nhất độ tăng thế năng này với biểu thức $\frac{1}{2}K_i$ để tìm động năng $K_i$ và tốc độ $v_A$.

- Dùng định lý công và cơ năng để tìm công của lực ma sát.

- Quãng đường toa xe đi từ A đến B là nửa chu vi vòng tròn $s = \pi R$. Từ công của lực ma sát không đổi suy ra độ lớn lực ma sát.

**Lời giải:**

(a) Tốc độ của toa xe tại điểm A:

- Độ cao giữa điểm B và điểm A là $y_B - y_A = 2R$. Do đó:
$$
\Delta U_g = mg(2R) = 2mgR
$$

- Theo giả thiết đề bài, $\Delta U_g = \frac{1}{2}K_i$:
$$
\begin{aligned}
\frac{1}{2}K_i &= 2mgR \\
\implies K_i &= 4mgR.
\end{aligned}
$$

- Mặt khác, động năng tại A là $K_i = \frac{1}{2}mv_A^2$:
$$
\begin{aligned}
\frac{1}{2}mv_A^2 &= 4mgR \\
\implies v_A^2 &= 8gR \\
\implies v_A &= \sqrt{8gR}.
\end{aligned}
$$

(b) Công của lực ma sát từ điểm A đến điểm B:

- Áp dụng định lý biến thiên cơ năng:
$$
W_f = \Delta K + \Delta U_g
$$

- Thay các đại lượng theo $K_i$:
$$
\begin{aligned}
\Delta K &= K_f - K_i \\
&= \frac{1}{4}K_i - K_i \\
&= -\frac{3}{4}K_i.
\end{aligned}
$$

- Kết hợp với $\Delta U_g = \frac{1}{2}K_i$:
$$
\begin{aligned}
W_f &= -\frac{3}{4}K_i + \frac{1}{2}K_i \\
&= -\frac{1}{4}K_i.
\end{aligned}
$$

- Thay $K_i = 4mgR$:
$$
W_f = -\frac{1}{4}(4mgR) = -mgR
$$

(c) Độ lớn lực ma sát:

- Quãng đường chuyển động dọc theo nửa đường tròn là:
$$
s = \pi R
$$

- Vì lực ma sát luôn tiếp tuyến và ngược chiều vận tốc:
$$
W_f = -f s = -f(\pi R)
$$

- Đồng nhất với kết quả ở câu (b):
$$
\begin{aligned}
-f(\pi R) &= -mgR \\
\implies f &= \frac{mg}{\pi}.
\end{aligned}
$$

</details>

---

### VP7.9.1 - Xe đệm khí gắn lò xo không ma sát

Một xe đệm khí có khối lượng $0{,}240\,\mathrm{kg}$ nằm trên đường ray nằm ngang không ma sát, được gắn vào một lò xo nằm ngang có độ cứng $6{,}00\,\mathrm{N/m}$. Ban đầu lò xo (có đầu kia cố định) đang bị dãn một đoạn $0{,}100\,\mathrm{m}$ và xe đệm khí đang chuyển động với tốc độ $0{,}400\,\mathrm{m/s}$ theo hướng làm lò xo dãn thêm.
(a) Cơ năng toàn phần (động năng cộng thế năng đàn hồi) của hệ là bao nhiêu?
(b) Khi xe đệm khí dừng lại tức thời, lò xo bị dãn một khoảng bằng bao nhiêu?

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**

- Khối lượng xe: $m = 0{,}240\,\mathrm{kg}$.

- Độ cứng lò xo: $k = 6{,}00\,\mathrm{N/m}$.

- Trạng thái đầu: $x_1 = 0{,}100\,\mathrm{m}$, $v_1 = 0{,}400\,\mathrm{m/s}$.

- Bỏ qua ma sát.

- Tìm cơ năng toàn phần $E$ và độ dãn cực đại $x_2$.

**Hướng đi:**

- Bỏ qua ma sát trên ray nằm ngang, lực đàn hồi là lực thế duy nhất sinh công trong hệ. Cơ năng toàn phần gồm động năng của xe và thế năng đàn hồi của lò xo được bảo toàn.

- Tính cơ năng toàn phần tại thời điểm ban đầu từ $x_1$ và $v_1$.

- Tại vị trí xe dừng lại tức thời, vận tốc bằng không ($v_2 = 0$), toàn bộ cơ năng chuyển thành thế năng đàn hồi của lò xo.

**Lời giải:**

(a) Cơ năng toàn phần của hệ:

- Động năng của xe ở trạng thái đầu:
$$
\begin{aligned}
K_1 &= \frac{1}{2}mv_1^2 \\
&= \frac{1}{2}(0{,}240)(0{,}400)^2 \\
&= 0{,}0192\,\mathrm{J}.
\end{aligned}
$$

- Thế năng đàn hồi của lò xo:
$$
\begin{aligned}
U_1 &= \frac{1}{2}kx_1^2 \\
&= \frac{1}{2}(6{,}00)(0{,}100)^2 \\
&= 0{,}0300\,\mathrm{J}.
\end{aligned}
$$

- Cơ năng toàn phần của hệ:
$$
\begin{aligned}
E &= K_1 + U_1 \\
&= 0{,}0192 + 0{,}0300 \\
&= 0{,}0492\,\mathrm{J}.
\end{aligned}
$$

(b) Độ dãn của lò xo khi xe dừng lại tức thời:

- Khi xe dừng lại ($v_2 = 0$), động năng triệt tiêu:
$$
E = \frac{1}{2}kx_2^2
$$

- Độ dãn của lò xo khi đó:
$$
\begin{aligned}
x_2 &= \sqrt{\frac{2E}{k}} \\
&= \sqrt{\frac{2(0{,}0492)}{6{,}00}} \\
&= \sqrt{0{,}0164} \\
&\approx 0{,}128\,\mathrm{m}.
\end{aligned}
$$

</details>

---

### VP7.9.2 - Xe đệm khí gắn lò xo có ma sát

Một xe đệm khí có khối lượng $0{,}240\,\mathrm{kg}$ gắn với lò xo nằm ngang có độ cứng $6{,}00\,\mathrm{N/m}$. Có ma sát giữa xe và ray. Ban đầu lò xo dãn $0{,}100\,\mathrm{m}$ và xe chuyển động với tốc độ $0{,}400\,\mathrm{m/s}$ theo hướng làm lò xo dãn thêm. Xe đệm khí dừng lại tức thời khi lò xo dãn một đoạn $0{,}112\,\mathrm{m}$.
(a) Lực ma sát đã thực hiện một công bằng bao nhiêu lên xe khi độ dãn tăng từ $0{,}100\,\mathrm{m}$ lên $0{,}112\,\mathrm{m}$?
(b) Hệ số ma sát trượt giữa xe và ray là bao nhiêu?

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**

- Khối lượng: $m = 0{,}240\,\mathrm{kg}$, độ cứng: $k = 6{,}00\,\mathrm{N/m}$.

- Ban đầu: $x_1 = 0{,}100\,\mathrm{m}$, $v_1 = 0{,}400\,\mathrm{m/s}$.

- Khi dừng lại tức thời: $x_2 = 0{,}112\,\mathrm{m}$, $v_2 = 0$.

- Tìm công của lực ma sát $W_f$ và hệ số ma sát trượt $\mu_k$.

**Hướng đi:**

- Có ma sát nên cơ năng không bảo toàn. Độ biến thiên cơ năng toàn phần của hệ bằng công của lực ma sát:
$$
W_f = E_2 - E_1
$$

- Cơ năng ban đầu $E_1$ được tính từ $v_1$ và $x_1$. Cơ năng lúc sau $E_2$ hoàn toàn là thế năng đàn hồi ứng với độ dãn $x_2$.

- Lực ma sát trượt trên mặt phẳng nằm ngang có độ lớn $f_k = \mu_k mg$. Công ma sát liên hệ với quãng đường dịch chuyển $s = x_2 - x_1$ theo biểu thức $W_f = -f_k s$.

**Lời giải:**

(a) Công của lực ma sát:

- Cơ năng ban đầu của hệ (như đã tính ở bài VP7.9.1):
$$
E_1 = 0{,}0492\,\mathrm{J}
$$

- Cơ năng khi xe dừng lại tức thời tại $x_2 = 0{,}112\,\mathrm{m}$:
$$
\begin{aligned}
E_2 &= \frac{1}{2}kx_2^2 \\
&= \frac{1}{2}(6{,}00)(0{,}112)^2 \\
&= 3{,}00(0{,}012544) \\
&= 0{,}037632\,\mathrm{J}.
\end{aligned}
$$

- Công do lực ma sát thực hiện:
$$
\begin{aligned}
W_f &= E_2 - E_1 \\
&= 0{,}037632 - 0{,}0492 \\
&= -0{,}011568\,\mathrm{J} \\
&\approx -0{,}0116\,\mathrm{J}.
\end{aligned}
$$

(b) Hệ số ma sát trượt:

- Quãng đường xe trượt thêm là:
$$
\begin{aligned}
s &= x_2 - x_1 \\
&= 0{,}112 - 0{,}100 \\
&= 0{,}0120\,\mathrm{m}.
\end{aligned}
$$

- Độ lớn lực ma sát trượt:
$$
\begin{aligned}
f_k &= \frac{|W_f|}{s} \\
&= \frac{0{,}011568}{0{,}0120} \\
&= 0{,}964\,\mathrm{N}.
\end{aligned}
$$

- Hệ số ma sát trượt $\mu_k$:
$$
\begin{aligned}
\mu_k &= \frac{f_k}{mg} \\
&= \frac{0{,}964}{0{,}240(9{,}80)} \\
&= \frac{0{,}964}{2{,}352} \\
&\approx 0{,}410.
\end{aligned}
$$

</details>

---

### VP7.9.3 - Bắn vật thẳng đứng bằng lò xo

Một lò xo nhẹ đặt thẳng đứng có độ cứng $k$ gắn chặt đầu dưới vào mặt bàn. Ta nén lò xo xuống một đoạn $d$, đặt một vật khối lượng $m$ lên đỉnh lò xo rồi thả nhẹ từ trạng thái nghỉ. Lò xo đẩy vật lên cao và vật tiếp tục bay lên một đoạn phía trên vị trí đầu lò xo khi không biến dạng.
(a) Tìm tốc độ của vật ngay khi nó vừa rời khỏi lò xo.
(b) Tìm tổng khoảng cách thẳng đứng mà vật di chuyển được từ lúc thả đến khi đạt độ cao cực đại.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**

- Lò xo thẳng đứng có độ cứng $k$, độ nén ban đầu $d$.

- Khối lượng vật: $m$. Thả không vận tốc ban đầu.

- Tìm tốc độ $v$ khi vừa rời lò xo và tổng quãng đường bay lên $h_{\mathrm{total}}$.

**Hướng đi:**

- Bỏ qua lực cản không khí, hệ gồm vật, lò xo và Trái Đất chịu tác dụng của các lực thế (trọng lực và lực đàn hồi). Cơ năng toàn phần được bảo toàn.

- Chọn mốc tính thế năng trọng trường tại vị trí thả ban đầu ($y_1 = 0$).

- Lò xo rời khỏi vật khi lực nén trở về không, tức là lò xo trở lại chiều dài tự nhiên ban đầu ($y_2 = d$).

- Tại độ cao cực đại, vật tạm thời dừng lại ($v_3 = 0$).

**Lời giải:**

(a) Tốc độ của vật khi vừa rời khỏi lò xo:

- Trạng thái 1 (lúc thả): Vật đứng yên ($v_1 = 0$), lò xo nén $d$, chọn $y_1 = 0$:
$$
E_1 = \frac{1}{2}kd^2
$$

- Trạng thái 2 (lúc rời lò xo): Vật ở độ cao $y_2 = d$, lò xo không biến dạng ($x_2 = 0$), tốc độ là $v$:
$$
E_2 = \frac{1}{2}mv^2 + mgd
$$

- Bảo toàn cơ năng $E_2 = E_1$:
$$
\frac{1}{2}mv^2 + mgd = \frac{1}{2}kd^2
$$

- Biến đổi để rút ra tốc độ $v$:
$$
\begin{aligned}
\frac{1}{2}mv^2 &= \frac{1}{2}kd^2 - mgd \\
\implies v^2 &= \frac{kd^2}{m} - 2gd \\
\implies v &= \sqrt{\frac{kd^2}{m} - 2gd}.
\end{aligned}
$$

(b) Tổng khoảng cách thẳng đứng vật đi được:

- Trạng thái 3 (độ cao cực đại): Vật đạt độ cao $h_{\mathrm{total}}$ so với vị trí ban đầu, tốc độ $v_3 = 0$:
$$
E_3 = mgh_{\mathrm{total}}
$$

- Bảo toàn cơ năng giữa trạng thái 1 và trạng thái 3:
$$
mgh_{\mathrm{total}} = \frac{1}{2}kd^2
$$

- Suy ra tổng khoảng cách thẳng đứng:
$$
h_{\mathrm{total}} = \frac{kd^2}{2mg}
$$

Giả thiết vật bay lên cao hơn đầu lò xo không biến dạng đòi hỏi $h_{\mathrm{total}} > d$, tức là $d > 2mg/k$. Điều kiện này cũng bảo đảm biểu thức tốc độ rời lò xo có giá trị thực và dương.

</details>

---

### VP7.9.4 - Khối trụ trượt trong ống thẳng đứng có ma sát

Một khối trụ khối lượng $m$ có thể trượt trong một ống thẳng đứng. Lực ma sát trượt giữa khối trụ và thành ống có độ lớn không đổi bằng $f$. Đầu trên của một lò xo nhẹ độ cứng $k$ được gắn vào nắp đỉnh ống, đầu dưới gắn vào đỉnh khối trụ. Ban đầu khối trụ đứng yên và lò xo ở trạng thái tự nhiên không biến dạng. Thả nhẹ cho khối trụ chuyển động. Khối trụ sẽ đi xuống một khoảng thẳng đứng bằng bao nhiêu trước khi dừng lại tức thời?

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**

- Khối trụ khối lượng $m$, trượt thẳng đứng trong ống.

- Lực ma sát trượt cản trở chuyển động có độ lớn không đổi $f$.

- Lò xo treo thẳng đứng độ cứng $k$, ban đầu không dãn.

- Tìm khoảng dịch chuyển thẳng đứng $y$ cho đến khi vật dừng lại tức thời lần đầu.

**Hướng đi:**

- Chọn chiều dương hướng thẳng đứng xuống dưới. Gốc tọa độ tại vị trí ban đầu của khối trụ ($y_1 = 0$).

- Ngoại lực không thế là lực ma sát trượt $f$, hướng thẳng đứng lên trên, ngược chiều dịch chuyển của khối trụ.

- Áp dụng định lý biến thiên cơ năng toàn phần của hệ:
$$
W_f = \Delta K + \Delta U_g + \Delta U_{\mathrm{el}}
$$

- Tại hai thời điểm đầu và dừng tức thời, động năng đều bằng không ($\Delta K = 0$).

- Chọn phương pháp năng lượng vì lực đàn hồi thay đổi theo vị trí, còn công của lực ma sát không đổi về độ lớn được tính trực tiếp từ quãng đường.

**Lời giải:**

- Trạng thái ban đầu: $y_1 = 0, v_1 = 0$, lò xo không biến dạng ($U_{\mathrm{el},1} = 0$).

- Trạng thái dừng lại tức thời: Khối trụ hạ xuống độ sâu $y$, tốc độ $v_2 = 0$.

- Độ biến thiên thế năng trọng trường:
$$
\Delta U_g = -mgy
$$

- Độ biến thiên thế năng đàn hồi của lò xo:
$$
\Delta U_{\mathrm{el}} = \frac{1}{2}ky^2
$$

- Công do lực ma sát thực hiện khi vật đi xuống đoạn $y$:
$$
W_f = -fy
$$

- Phương trình bảo toàn và chuyển hóa năng lượng:
$$
\begin{aligned}
\Delta U_g + \Delta U_{\mathrm{el}} &= W_f \\
-mgy + \frac{1}{2}ky^2 &= -fy.
\end{aligned}
$$

- Chuyển vế phương trình:
$$
\frac{1}{2}ky^2 = (mg - f)y
$$

- Vì khối trụ đã dịch chuyển một khoảng hữu hạn $y > 0$, ta chia hai vế cho $y$:
$$
\begin{aligned}
\frac{1}{2}ky &= mg - f \\
\implies y &= \frac{2(mg - f)}{k}.
\end{aligned}
$$

Lời giải xét trường hợp khối trụ bắt đầu trượt xuống như giả thiết của bài. Để nghiệm dừng lại khác vị trí thả có $y>0$, cần $mg>f$. Đề không cho ma sát nghỉ cực đại, vì vậy không thể dùng riêng độ lớn ma sát trượt $f$ để quyết định ngưỡng bắt đầu chuyển động.

</details>
