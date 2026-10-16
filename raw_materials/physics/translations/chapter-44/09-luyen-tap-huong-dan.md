Trong các bài tập, ký hiệu d, h, min và yr lần lượt chỉ ngày, giờ, phút và năm. Tốc độ đếm tính theo phút được viết bằng đơn vị $\mathrm{min^{-1}}$. Năng lượng liên kết riêng tính bằng MeV trên mỗi nuclôn.

## Luyện tập hướng dẫn

Nhóm 12 bài tập sau rèn luyện phương pháp tính toán định lượng cho ba chủ đề của vật lý hạt và vũ trụ học. Chủ đề đầu tiên là cyclotron và chuyển động của hạt tích điện trong từ trường. Hai chủ đề tiếp theo là ngưỡng tạo hạt trong va chạm tương đối tính và mối liên hệ giữa định luật Hubble với hiệu ứng Doppler.

Các hằng số vật lý sử dụng trong tính toán:
- Tốc độ ánh sáng trong chân không: $c = 2{,}998 \times 10^8\,\mathrm{m/s}$
- Hằng số Planck: $h = 6{,}626 \times 10^{-34}\,\mathrm{J\cdot s}$
- Hằng số Planck rút gọn: $\hbar = 1{,}055 \times 10^{-34}\,\mathrm{J\cdot s}$
- Điện tích nguyên tố: $e = 1{,}602 \times 10^{-19}\,\mathrm{C}$
- Năng lượng nghỉ proton: $m_p c^2 \approx 938{,}3\,\mathrm{MeV}$ (khối lượng $m_p \approx 1{,}673 \times 10^{-27}\,\mathrm{kg}$)
- Năng lượng nghỉ neutron: $m_n c^2 \approx 939{,}6\,\mathrm{MeV}$ (khối lượng $m_n \approx 1{,}675 \times 10^{-27}\,\mathrm{kg}$)
- Năng lượng nghỉ electron: $m_e c^2 \approx 0{,}511\,\mathrm{MeV}$ (khối lượng $m_e \approx 9{,}109 \times 10^{-31}\,\mathrm{kg}$)
- Hằng số Hubble danh định: $H_0 \approx 68\,\mathrm{(km/s)/Mpc}$ (tương đương $2{,}2 \times 10^{-18}\,\mathrm{s}^{-1}$)
- Đơn vị khoảng cách: $1\,\mathrm{pc} \approx 3{,}086 \times 10^{16}\,\mathrm{m}$ (khoảng $3{,}26\,\mathrm{ly}$), $1\,\mathrm{Mpc} = 10^6\,\mathrm{pc}$

---

### VP44.1.1

Trong một máy gia tốc cyclotron, bán kính quỹ đạo cực đại của proton là $0{,}800\,\mathrm{m}$. Từ trường trong máy có độ lớn $0{,}600\,\mathrm{T}$. Hãy xác định:
(a) Tần số của điện áp xoay chiều đặt vào hai cực Dee.
(b) Động năng cực đại của proton theo đơn vị $\mathrm{MeV}$.
(c) Tốc độ cực đại của proton theo phân số của tốc độ ánh sáng $c$.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Bán kính cực đại: $R = 0{,}800\,\mathrm{m}$.
- Cảm ứng từ: $B = 0{,}600\,\mathrm{T}$.
- Hạt proton: Điện tích $q = +e$, khối lượng $m = 1{,}673 \times 10^{-27}\,\mathrm{kg}$.
- Cần tính: Tần số cyclotron $f$, động năng cực đại $K_{\max}$ theo $\mathrm{MeV}$, và tỉ số $v_{\max}/c$.

**Hướng đi:**
- Lực từ Lorentz đóng vai trò lực hướng tâm giúp hạt chuyển động tròn đều: $qvB = mv^2/R$.
- Tần số quay cyclotron không phụ thuộc vào bán kính khi hạt chuyển động phi tương đối tính: $f = \frac{qB}{2\pi m}$.
- Tốc độ cực đại đạt được tại mép ngoài cực Dee: $v_{\max} = 2\pi f R = \frac{qBR}{m}$.
- Động năng của proton: $K = \frac{1}{2} m v_{\max}^2 = \frac{q^2 B^2 R^2}{2m}$, sau đó đổi sang đơn vị $\mathrm{MeV}$.

**Lời giải chi tiết:**

(a) Tần số của điện áp xoay chiều đặt vào các cực Dee:
Tần số cyclotron của proton trong từ trường $B = 0{,}600\,\mathrm{T}$:
$$
\begin{aligned}
f &= \frac{qB}{2\pi m} \\
&\approx 9{,}15 \times 10^6\,\mathrm{Hz} \\
&= 9{,}15\,\mathrm{MHz}.
\end{aligned}
$$
với $q = 1{,}602 \times 10^{-19}\,\mathrm{C}$ và $m = 1{,}673 \times 10^{-27}\,\mathrm{kg}$.

(b) Động năng cực đại của proton khi ra khỏi cực Dee:
Tốc độ cực đại tại bán kính $R = 0{,}800\,\mathrm{m}$:
$$
\begin{aligned}
v_{\max} &= \frac{qBR}{m} \\
&\approx 4{,}60 \times 10^7\,\mathrm{m/s}.
\end{aligned}
$$
Động năng cực đại tương ứng:
$$
\begin{aligned}
K_{\max} &= \frac{q^2 B^2 R^2}{2m} \\
&\approx 1{,}77 \times 10^{-12}\,\mathrm{J}.
\end{aligned}
$$
Đổi sang đơn vị $\mathrm{MeV}$ với $1\,\mathrm{MeV} = 1{,}602 \times 10^{-13}\,\mathrm{J}$:
$$
K_{\max} \approx 11{,}0\,\mathrm{MeV}.
$$

(c) Tốc độ cực đại của proton tính theo $c$:
Với $c = 2{,}998 \times 10^8\,\mathrm{m/s}$:
$$
\frac{v_{\max}}{c} \approx 0{,}153.
$$
Như vậy, tốc độ cực đại là $0{,}153c$. Vì $v \approx 0{,}15c$, hiệu ứng tương đối tính làm tăng khối lượng dưới $1{,}2\%$, việc dùng gần đúng cơ học cổ điển hoàn toàn hợp lý.

</details>

---

### VP44.1.2

Một máy gia tốc cyclotron tại phòng thí nghiệm TRIUMF ở Vancouver, Canada, có cảm ứng từ $0{,}460\,\mathrm{T}$. Máy được sử dụng để gia tốc các ion hydro âm ($\mathrm{H}^-$) có điện tích $-e$ và khối lượng $1{,}67 \times 10^{-27}\,\mathrm{kg}$. Hãy xác định:
(a) Bán kính quỹ đạo của ion khi chúng đạt tốc độ $6{,}00 \times 10^6\,\mathrm{m/s}$.
(b) Tần số góc trong chuyển động của các ion.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Cảm ứng từ: $B = 0{,}460\,\mathrm{T}$.
- Hạt ion hydro âm $\mathrm{H}^-$: Điện tích $q = -e$, khối lượng $m = 1{,}67 \times 10^{-27}\,\mathrm{kg}$.
- Tốc độ khảo sát: $v = 6{,}00 \times 10^6\,\mathrm{m/s}$.
- Cần tính: Bán kính quỹ đạo $R$ và tần số góc $\omega$.

**Hướng đi:**
- Lực từ Lorentz cung cấp gia tốc hướng tâm: $|q|vB = mv^2/R$.
- Bán kính quỹ đạo được xác định bởi: $R = \frac{mv}{|q|B}$.
- Tần số góc chuyển động tròn đều: $\omega = \frac{v}{R} = \frac{|q|B}{m}$. Dấu âm của điện tích chỉ ảnh hưởng đến chiều quay chứ không làm đổi tần số góc.

**Lời giải chi tiết:**

(a) Bán kính quỹ đạo của ion $\mathrm{H}^-$ khi đạt tốc độ $v = 6{,}00 \times 10^6\,\mathrm{m/s}$:
Với độ lớn điện tích $|q| = e = 1{,}602 \times 10^{-19}\,\mathrm{C}$:
$$
\begin{aligned}
R &= \frac{mv}{|q|B} \\
&\approx 0{,}136\,\mathrm{m}.
\end{aligned}
$$

(b) Tần số góc trong chuyển động của ion:
Áp dụng công thức tần số góc cyclotron:
$$
\begin{aligned}
\omega &= \frac{|q|B}{m} \\
&\approx 4{,}41 \times 10^7\,\mathrm{rad/s}.
\end{aligned}
$$

![Minh họa bài VP44.1.2: Bán kính quỹ đạo của ion hydro âm trong từ trường cyclotron.](./img/young-44/loi-giai-c-01.svg)

</details>

---

### VP44.1.3

Chiếc máy gia tốc cyclotron đầu tiên được chế tạo vào năm 1930 có đường kính $11{,}4\,\mathrm{cm}$ và được dùng để gia tốc các ion hydro âm (điện tích $-e$, khối lượng $1{,}67 \times 10^{-27}\,\mathrm{kg}$) đến động năng $80{,}0\,\mathrm{keV}$. Hãy xác định:
(a) Độ lớn cảm ứng từ đã sử dụng.
(b) Tần số của điện áp xoay chiều đặt vào hai cực Dee.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Đường kính $d = 11{,}4\,\mathrm{cm}$, suy ra bán kính $R = 0{,}0570\,\mathrm{m}$.
- Ion $\mathrm{H}^-$: Điện tích $q = -e$, khối lượng $m = 1{,}67 \times 10^{-27}\,\mathrm{kg}$.
- Động năng cuối: $K = 80{,}0\,\mathrm{keV}$, tương đương $1{,}282 \times 10^{-14}\,\mathrm{J}$.
- Cần tính: Cảm ứng từ $B$ và tần số cyclotron $f$.

**Hướng đi:**
- Biểu diễn động năng qua cảm ứng từ và bán kính quỹ đạo cực đại: $K = \frac{q^2 B^2 R^2}{2m}$.
- Từ động năng và bán kính, suy ra độ lớn cảm ứng từ cần thiết: $B = \frac{\sqrt{2mK}}{|q|R}$.
- Tần số dao động của hiệu điện thế gia tốc: $f = \frac{|q|B}{2\pi m}$.

**Lời giải chi tiết:**

(a) Xác định cảm ứng từ $B$:
Động năng quy đổi sang đơn vị jun là:
$$
K \approx 1{,}282 \times 10^{-14}\,\mathrm{J}.
$$
Từ công thức động năng quay trong cyclotron:
$$
\begin{aligned}
B &= \frac{\sqrt{2mK}}{|q|R} \\
&\approx 0{,}717\,\mathrm{T}.
\end{aligned}
$$

(b) Tần số của điện áp xoay chiều:
Tần số điện áp xoay chiều đồng bộ với chuyển động của ion:
$$
\begin{aligned}
f &= \frac{|q|B}{2\pi m} \\
&\approx 10{,}9\,\mathrm{MHz}.
\end{aligned}
$$

</details>

---

### VP44.1.4

Một máy gia tốc cyclotron được dùng để gia tốc hạt alpha (điện tích $+2e$, khối lượng $6{,}64 \times 10^{-27}\,\mathrm{kg}$). Tần số của điện áp xoay chiều đặt vào hai cực Dee là $5{,}80\,\mathrm{MHz}$. Hãy xác định:
(a) Độ lớn cảm ứng từ cần sử dụng.
(b) Động năng (tính theo đơn vị $\mathrm{MeV}$) của hạt alpha khi bán kính quỹ đạo tròn đạt $0{,}650\,\mathrm{m}$.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Hạt alpha: $q = +2e$, khối lượng $m = 6{,}64 \times 10^{-27}\,\mathrm{kg}$.
- Tần số cyclotron: $f = 5{,}80\,\mathrm{MHz}$, tức $5{,}80 \times 10^6\,\mathrm{Hz}$.
- Bán kính khảo sát: $R = 0{,}650\,\mathrm{m}$.
- Cần tính: Cảm ứng từ $B$ và động năng $K$ theo $\mathrm{MeV}$.

**Hướng đi:**
- Tần số cyclotron $f = \frac{qB}{2\pi m}$ cho phép xác định trực tiếp cảm ứng từ: $B = \frac{2\pi m f}{q}$.
- Tốc độ của hạt tại bán kính $R$ là $v = 2\pi f R$.
- Động năng của hạt alpha: $K = \frac{1}{2} m v^2$, sau đó đổi sang đơn vị $\mathrm{MeV}$.

**Lời giải chi tiết:**

(a) Xác định cảm ứng từ $B$:
Từ công thức tần số cyclotron:
$$
\begin{aligned}
B &= \frac{2\pi m f}{q} \\
&\approx 0{,}756\,\mathrm{T}.
\end{aligned}
$$
với $q = +2e \approx 3{,}204 \times 10^{-19}\,\mathrm{C}$.

(b) Động năng của hạt alpha tại bán kính $R = 0{,}650\,\mathrm{m}$:
Tốc độ của hạt alpha tại vị trí này:
$$
\begin{aligned}
v &= 2\pi f R \\
&\approx 2{,}37 \times 10^7\,\mathrm{m/s}.
\end{aligned}
$$
Động năng tương ứng:
$$
\begin{aligned}
K &= \frac{1}{2} m v^2 \\
&\approx 1{,}86 \times 10^{-12}\,\mathrm{J}.
\end{aligned}
$$
Đổi sang đơn vị $\mathrm{MeV}$:
$$
K \approx 11{,}6\,\mathrm{MeV}.
$$

</details>

---

### VP44.3.1

Một proton có động năng $K$ va chạm với một proton đang đứng yên. Sau va chạm, hai proton ban đầu vẫn tồn tại và tạo thêm một hạt eta-phẩy ($\eta'$) có năng lượng nghỉ $958\,\mathrm{MeV}$. Để phản ứng này có thể xảy ra:
(a) Năng lượng khả dụng tối thiểu trong hệ quy chiếu khối tâm là bao nhiêu?
(b) Động năng $K$ của proton tới phải có giá trị tối thiểu bằng bao nhiêu?

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Hạt tới: Proton có động năng $K$, khối lượng nghỉ $m_p c^2 \approx 938\,\mathrm{MeV}$.
- Hạt bia: Proton đứng yên trong phòng thí nghiệm.
- Phản ứng: $p + p \to p + p + \eta'$ với năng lượng nghỉ $m_{\eta'} c^2 = 958\,\mathrm{MeV}$.
- Cần tính: Năng lượng khả dụng tối thiểu $E_{\mathrm{cm},\min}$ và động năng ngưỡng $K_{\min}$.

**Hướng đi:**
- Năng lượng khả dụng $E_{\mathrm{cm}}$ là tổng năng lượng trong hệ quy chiếu khối tâm.
- Tại ngưỡng tạo hạt, mọi hạt sinh ra đều đứng yên trong hệ khối tâm: $E_{\mathrm{cm},\min} = 2m_p c^2 + m_{\eta'} c^2$.
- Dùng bất biến tương đối tính: Đối với bia tĩnh, $E_{\mathrm{cm}}^2 = 2 m_p c^2 K + 4 m_p^2 c^4$.
- Giải phương trình tìm động năng ngưỡng $K_{\min}$.

**Lời giải chi tiết:**

(a) Năng lượng khả dụng tối thiểu trong hệ khối tâm:
Tại ngưỡng sinh hạt, toàn bộ các hạt sau va chạm đứng yên trong hệ khối tâm:
$$
\begin{aligned}
E_{\mathrm{cm}} &= 2m_p c^2 + m_{\eta'} c^2 \\
&= 2834\,\mathrm{MeV}.
\end{aligned}
$$
với $m_p c^2 = 938\,\mathrm{MeV}$ và $m_{\eta'} c^2 = 958\,\mathrm{MeV}$.

(b) Động năng tối thiểu $K_{\min}$ của proton tới:
Đặt $E_0 = 2 m_p c^2 = 1876\,\mathrm{MeV}$. Hệ thức năng lượng khả dụng với bia cố định là:
$$
E_{\mathrm{cm}}^2 = E_0 K + E_0^2
$$
Suy ra động năng ngưỡng:
$$
\begin{aligned}
K_{\min} &= \frac{E_{\mathrm{cm}}^2 - E_0^2}{E_0} \\
&\approx 2{,}41\,\mathrm{GeV}.
\end{aligned}
$$
với $E_{\mathrm{cm}} = 2834\,\mathrm{MeV}$.

![Minh họa bài VP44.3.1: Năng lượng khối tâm và động năng ngưỡng của proton bắn vào bia tĩnh.](./img/young-44/loi-giai-c-02.svg)

</details>

---

### VP44.3.2

Một proton có động năng $K$ va chạm với một proton đang đứng yên. Các hạt còn lại sau va chạm gồm một proton và một hạt delta-cộng ($\Delta^+$) có năng lượng nghỉ $1232\,\mathrm{MeV}$. Để phản ứng này xảy ra:
(a) Năng lượng khả dụng tối thiểu trong hệ quy chiếu khối tâm là bao nhiêu?
(b) Động năng $K$ của proton tới phải có giá trị tối thiểu bằng bao nhiêu?

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Hạt tới: Proton có động năng $K$, năng lượng nghỉ $m_p c^2 = 938\,\mathrm{MeV}$.
- Bia tĩnh: Proton đứng yên.
- Quá trình: $p + p \to p + \Delta^+$, với $m_{\Delta^+} c^2 = 1232\,\mathrm{MeV}$.
- Cần tính: Năng lượng khả dụng tối thiểu $E_{\mathrm{cm},\min}$ và động năng ngưỡng $K_{\min}$.

**Hướng đi:**
- Tại ngưỡng tạo hạt trong hệ khối tâm, hai hạt sinh ra đứng yên: $E_{\mathrm{cm},\min} = m_p c^2 + m_{\Delta^+} c^2$.
- Dùng hệ thức liên hệ năng lượng khả dụng với bia tĩnh: $E_{\mathrm{cm}}^2 = 2 m_p c^2 K + 4 m_p^2 c^4$.
- Rút ra động năng tối thiểu $K_{\min}$.

**Lời giải chi tiết:**

(a) Năng lượng khả dụng tối thiểu trong hệ khối tâm:
Tại ngưỡng phản ứng:
$$
\begin{aligned}
E_{\mathrm{cm}} &= m_p c^2 + m_{\Delta^+} c^2 \\
&= 2170\,\mathrm{MeV}.
\end{aligned}
$$

(b) Động năng tối thiểu $K_{\min}$ của proton tới:
Đặt $E_0 = 2 m_p c^2 = 1876\,\mathrm{MeV}$. Từ hệ thức năng lượng khả dụng:
$$
\begin{aligned}
K_{\min} &= \frac{E_{\mathrm{cm}}^2 - E_0^2}{E_0} \\
&\approx 634\,\mathrm{MeV}.
\end{aligned}
$$
với $E_{\mathrm{cm}} = 2170\,\mathrm{MeV}$.

</details>

---

### VP44.3.3

Một hạt pion âm ($\pi^-$) có năng lượng nghỉ $140\,\mathrm{MeV}$ và động năng $K$ va chạm với một proton đang đứng yên. Hạt duy nhất còn lại sau va chạm là hạt delta-không ($\Delta^0$) có năng lượng nghỉ $1232\,\mathrm{MeV}$. Để phản ứng này xảy ra:
(a) Năng lượng khả dụng tối thiểu trong hệ quy chiếu khối tâm là bao nhiêu?
(b) Động năng $K$ của pion tới phải có giá trị tối thiểu bằng bao nhiêu?

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Hạt tới: Pion âm $\pi^-$, $m_\pi c^2 = 140\,\mathrm{MeV}$, động năng $K$.
- Hạt bia: Proton đứng yên, $m_p c^2 = 938\,\mathrm{MeV}$.
- Quá trình: $\pi^- + p \to \Delta^0$, với $m_{\Delta^0} c^2 = 1232\,\mathrm{MeV}$.
- Cần tính: Năng lượng khả dụng tối thiểu $E_{\mathrm{cm},\min}$ và động năng ngưỡng $K_{\min}$.

**Hướng đi:**
- Trạng thái cuối chỉ gồm một hạt duy nhất $\Delta^0$. Tại ngưỡng, hạt này đứng yên trong hệ khối tâm: $E_{\mathrm{cm},\min} = m_{\Delta^0} c^2$.
- Áp dụng bất biến 4-động lượng cho va chạm pion trên bia proton đứng yên: $E_{\mathrm{cm}}^2 = 2 m_p c^2 K + M_0^2 c^4$ với $M_0 = m_p + m_\pi$.
- Giải phương trình bậc nhất đối với $K$ để tìm động năng ngưỡng.

**Lời giải chi tiết:**

(a) Năng lượng khả dụng tối thiểu trong hệ khối tâm:
Vì sản phẩm chỉ có một hạt $\Delta^0$, năng lượng khả dụng tối thiểu là:
$$
\begin{aligned}
E_{\mathrm{cm}} &= m_{\Delta^0} c^2 \\
&= 1232\,\mathrm{MeV}.
\end{aligned}
$$

(b) Động năng tối thiểu $K_{\min}$ của pion:
Tổng năng lượng nghỉ ban đầu là $M_0 c^2 = 1078\,\mathrm{MeV}$.
Hệ thức liên hệ năng lượng:
$$
E_{\mathrm{cm}}^2 = 2 m_p c^2 K + M_0^2 c^4
$$
Suy ra:
$$
\begin{aligned}
K_{\min} &= \frac{E_{\mathrm{cm}}^2 - M_0^2 c^4}{2 m_p c^2} \\
&\approx 190\,\mathrm{MeV}.
\end{aligned}
$$
với $2 m_p c^2 = 1876\,\mathrm{MeV}$.

</details>

---

### VP44.3.4

Máy va chạm Hadron Lớn (LHC) truyền cho mỗi proton năng lượng toàn phần $7\,\mathrm{TeV}$, tức $7{,}00 \times 10^3\,\mathrm{GeV}$.
(a) Nếu một proton có năng lượng này va chạm với một proton thứ hai đang đứng yên, năng lượng khả dụng là bao nhiêu?
(b) Sau va chạm, hai proton ban đầu vẫn tồn tại và tạo thêm một hạt trung hòa X. Khối lượng cực đại của hạt X có thể sinh ra là bao nhiêu?

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Năng lượng toàn phần chùm hạt: $E = 7000\,\mathrm{GeV}$.
- Hạt bia: Proton đứng yên, $m_p c^2 \approx 0{,}938\,\mathrm{GeV}$.
- Phản ứng sinh hạt: $p + p \to p + p + X$.
- Cần tính: Năng lượng khả dụng $E_{\mathrm{cm}}$ khi bắn vào bia tĩnh, và khối lượng nghỉ cực đại $m_X$ của hạt sinh ra.

**Hướng đi:**
- Áp dụng hệ thức năng lượng khả dụng với bia tĩnh: $E_{\mathrm{cm}}^2 = 2 m_p c^2 E + 2 (m_p c^2)^2$.
- Khối lượng cực đại của hạt X đạt được khi toàn bộ năng lượng khả dụng vượt quá năng lượng nghỉ của hai proton ban đầu: $E_{\mathrm{cm}} = 2 m_p c^2 + m_X c^2$.

**Lời giải chi tiết:**

(a) Năng lượng khả dụng với bia proton đứng yên:
Đặt $E_0 = m_p c^2 \approx 0{,}938\,\mathrm{GeV}$. Bình phương năng lượng khả dụng:
$$
E_{\mathrm{cm}}^2 = 2 E_0 E + 2 E_0^2
$$
Với $E = 7000\,\mathrm{GeV}$ và $m_p c^2 = 0{,}938\,\mathrm{GeV}$, suy ra:
$$
E_{\mathrm{cm}} \approx 115\,\mathrm{GeV}.
$$
Lưu ý sự tương phản: Một chùm proton $7\,\mathrm{TeV}$ bắn vào bia tĩnh chỉ tạo ra năng lượng khả dụng $115\,\mathrm{GeV}$. Trong khi đó, nếu cho hai chùm đối đầu nhau thì năng lượng khả dụng đạt tới $14\,\mathrm{TeV}$.

(b) Khối lượng cực đại của hạt X:
Tại ngưỡng tạo hạt:
$$
\begin{aligned}
m_X c^2 &= E_{\mathrm{cm}} - 2 m_p c^2 \\
&\approx 113\,\mathrm{GeV}.
\end{aligned}
$$
Do đó, khối lượng cực đại của hạt X là $113\,\mathrm{GeV}/c^2$.

</details>

---

### VP44.9.1

Vạch quang phổ đỏ của hiđro có bước sóng $656{,}3\,\mathrm{nm}$ khi nguyên tử hiđro đứng yên. Vạch này được quan sát thấy ở bước sóng $725\,\mathrm{nm}$ trong quang phổ của một thiên hà xa xôi. Hãy xác định:
(a) Độ dịch chuyển đỏ $z$.
(b) Tốc độ lùi xa của thiên hà theo phân số của tốc độ ánh sáng $c$.

![Minh họa bài VP44.9.1: Các đại lượng được dùng trong lời giải.](./img/young-44/loi-giai-c-03.svg)

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Bước sóng nguồn phát: $\lambda_0 = 656{,}3\,\mathrm{nm}$.
- Bước sóng quan sát: $\lambda = 725\,\mathrm{nm}$.
- Cần tính: Độ dịch chuyển đỏ $z$ và tỉ số tốc độ lùi xa $\beta = v/c$.

**Hướng đi:**
- Độ dịch chuyển đỏ $z$ được định nghĩa bằng tỉ số biến thiên bước sóng: $z = \frac{\lambda - \lambda_0}{\lambda_0}$.
- Áp dụng hệ thức hiệu ứng Doppler quang học tương đối tính: $1 + z = \sqrt{\frac{1+\beta}{1-\beta}}$.
- Rút ra vận tốc lùi xa tương đối tính: $\beta = \frac{(1+z)^2 - 1}{(1+z)^2 + 1}$.

**Lời giải chi tiết:**

(a) Xác định độ dịch chuyển đỏ $z$:
Áp dụng công thức định nghĩa độ dịch chuyển đỏ:
$$
\begin{aligned}
z &= \frac{\lambda - \lambda_0}{\lambda_0} \\
&\approx 0{,}105.
\end{aligned}
$$
với $\lambda = 725\,\mathrm{nm}$ và $\lambda_0 = 656{,}3\,\mathrm{nm}$.

(b) Tốc độ lùi xa của thiên hà:
Từ độ dịch chuyển đỏ, ta có $(1 + z)^2 \approx 1{,}2203$.
Tốc độ lùi xa $\beta = v/c$ được tính bởi:
$$
\begin{aligned}
\beta &= \frac{(1+z)^2 - 1}{(1+z)^2 + 1} \\
&\approx 0{,}0992.
\end{aligned}
$$
Như vậy, tốc độ lùi xa của thiên hà là $0{,}0992c$.

</details>

---

### VP44.9.2

Một vạch hấp thụ nổi bật trong quang phổ của Mặt Trời và nhiều thiên hà bắt nguồn từ ion canxi mang điện tích đơn ($\mathrm{Ca}^+$). Trong hệ quy chiếu nghỉ, vạch này có bước sóng tử ngoại là $396{,}9\,\mathrm{nm}$. Nếu một thiên hà đang lùi xa khỏi chúng ta với tốc độ $0{,}0711c$, hãy xác định:
(a) Bước sóng mà chúng ta sẽ quan sát thấy vạch quang phổ này.
(b) Độ dịch chuyển đỏ $z$.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Bước sóng nghỉ: $\lambda_0 = 396{,}9\,\mathrm{nm}$.
- Tốc độ lùi xa: $\beta = v/c = 0{,}0711$.
- Cần tính: Bước sóng quan sát $\lambda$ và độ dịch chuyển đỏ $z$.

**Hướng đi:**
- Áp dụng hệ thức Doppler tương đối tính cho sóng ánh sáng khi nguồn chuyển động ra xa máy thu: $\lambda = \lambda_0 \sqrt{\frac{1+\beta}{1-\beta}}$.
- Độ dịch chuyển đỏ liên hệ với tỉ số bước sóng qua: $z = \frac{\lambda}{\lambda_0} - 1$.

**Lời giải chi tiết:**

(a) Bước sóng quan sát được của vạch canxi:
Với $\beta = 0{,}0711$, hệ số dịch chuyển bước sóng Doppler là $\sqrt{\frac{1+\beta}{1-\beta}} \approx 1{,}0738$.
Bước sóng quan sát được trên Trái Đất:
$$
\begin{aligned}
\lambda &= \lambda_0 \sqrt{\frac{1+\beta}{1-\beta}} \\
&\approx 426\,\mathrm{nm}.
\end{aligned}
$$
Vạch phổ tử ngoại ban đầu bị dịch chuyển đỏ sang vùng ánh sáng nhìn thấy.

(b) Độ dịch chuyển đỏ $z$:
Từ định nghĩa:
$$
\begin{aligned}
z &= \frac{\lambda}{\lambda_0} - 1 \\
&\approx 0{,}0738.
\end{aligned}
$$

</details>

---

### VP44.9.3

Hãy tính khoảng cách (theo đơn vị parsec, $\mathrm{pc}$) đến:
(a) Một thiên hà có tốc độ lùi xa $0{,}0992c$.
(b) Một thiên hà có tốc độ lùi xa $0{,}0711c$.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Hằng số Hubble sử dụng: $H_0 = 68\,\mathrm{(km/s)/Mpc}$, tức $6{,}8 \times 10^4\,\mathrm{(m/s)/Mpc}$.
- Trường hợp (a): Tốc độ lùi xa $v_a = 0{,}0992c$.
- Trường hợp (b): Tốc độ lùi xa $v_b = 0{,}0711c$.
- Cần tính: Khoảng cách $d_a$ và $d_b$ theo đơn vị $\mathrm{pc}$.

**Hướng đi:**
- Áp dụng định luật Hubble ở miền vận tốc vừa phải: $v = H_0 d$.
- Khoảng cách đến thiên hà: $d = \frac{v}{H_0} = \frac{\beta c}{H_0}$.
- Đổi khoảng cách từ $\mathrm{Mpc}$ sang $\mathrm{pc}$ theo tỉ lệ $1\,\mathrm{Mpc} = 10^6\,\mathrm{pc}$.

**Lời giải chi tiết:**

(a) Khoảng cách đến thiên hà có tốc độ $v = 0{,}0992c$:
Tốc độ lùi xa của thiên hà:
$$
\begin{aligned}
v &= 0{,}0992c \\
&\approx 2{,}97 \times 10^4\,\mathrm{km/s}.
\end{aligned}
$$
Khoảng cách theo định luật Hubble:
$$
\begin{aligned}
d_a &= \frac{v}{H_0} \\
&\approx 4{,}4 \times 10^8\,\mathrm{pc}.
\end{aligned}
$$

(b) Khoảng cách đến thiên hà có tốc độ $v = 0{,}0711c$:
Tốc độ lùi xa:
$$
\begin{aligned}
v &= 0{,}0711c \\
&\approx 2{,}13 \times 10^4\,\mathrm{km/s}.
\end{aligned}
$$
Khoảng cách tương ứng:
$$
\begin{aligned}
d_b &= \frac{v}{H_0} \\
&\approx 3{,}1 \times 10^8\,\mathrm{pc}.
\end{aligned}
$$

</details>

---

### VP44.9.4

Quang phổ của siêu tân tinh loại Ia (một vụ nổ sao sáng đến mức có thể quan sát thấy ở các thiên hà xa xôi) có một vạch phát xạ của ion silic mang điện tích đơn. Các nhà thiên văn học quan sát thấy vạch phát xạ này ở bước sóng $615{,}0\,\mathrm{nm}$ trong phòng thí nghiệm, nhưng lại ở bước sóng $666\,\mathrm{nm}$ trong quang phổ của một siêu tân tinh loại Ia ở thiên hà xa xôi. Hãy xác định:
(a) Tốc độ lùi xa của thiên hà theo đơn vị $\mathrm{m/s}$.
(b) Khoảng cách đến thiên hà theo đơn vị $\mathrm{pc}$.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Bước sóng phòng thí nghiệm: $\lambda_0 = 615{,}0\,\mathrm{nm}$.
- Bước sóng quan sát từ thiên hà: $\lambda = 666\,\mathrm{nm}$.
- Cần tính: Tốc độ lùi xa $v$ (theo $\mathrm{m/s}$) và khoảng cách $d$ (theo $\mathrm{pc}$).

**Hướng đi:**
- Tính độ dịch chuyển đỏ: $z = \frac{\lambda - \lambda_0}{\lambda_0}$.
- Xác định tỉ số tốc độ tương đối tính: $\beta = \frac{(1+z)^2 - 1}{(1+z)^2 + 1}$, rồi tính $v = \beta c$.
- Tính khoảng cách theo định luật Hubble: $d = \frac{v}{H_0}$.

**Lời giải chi tiết:**

(a) Tốc độ lùi xa của thiên hà:
Độ dịch chuyển đỏ $z$ của vạch silic:
$$
\begin{aligned}
z &= \frac{\lambda - \lambda_0}{\lambda_0} \\
&\approx 0{,}0829.
\end{aligned}
$$
Từ đó, ta có $(1+z)^2 \approx 1{,}173$. Tỉ số tốc độ lùi xa:
$$
\begin{aligned}
\beta &= \frac{(1+z)^2 - 1}{(1+z)^2 + 1} \\
&\approx 0{,}0795.
\end{aligned}
$$
Tốc độ lùi xa theo $\mathrm{m/s}$:
$$
\begin{aligned}
v &= \beta c \\
&\approx 2{,}38 \times 10^7\,\mathrm{m/s}.
\end{aligned}
$$

(b) Khoảng cách đến thiên hà:
Áp dụng định luật Hubble:
$$
\begin{aligned}
d &= \frac{v}{H_0} \\
&\approx 3{,}5 \times 10^8\,\mathrm{pc}.
\end{aligned}
$$

</details>
