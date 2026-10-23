## Bài tập Chương 4: Các định luật chuyển động của Newton (Phần 1: Bài 4.1 – 4.30)

---

### 4.1: Hợp lực của hai chú chó kéo cọc

*Độ khó: Mức 2.*

Hai chú chó kéo hai sợi dây nằm ngang buộc vào một chiếc cọc; góc giữa hai sợi dây là $60{,}0^\circ$. Nếu chú chó Rover tác dụng một lực $270\,\mathrm N$ và chú chó Fido tác dụng một lực $300\,\mathrm N$, hãy tìm độ lớn của hợp lực tác dụng lên cọc và góc hợp bởi hợp lực với sợi dây của Rover.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Lực kéo của Rover: $F_1 = 270\,\mathrm N$.
- Lực kéo của Fido: $F_2 = 300\,\mathrm N$.
- Góc giữa hai sợi dây: $\alpha = 60{,}0^\circ$.
- Cần tìm: Độ lớn hợp lực $R$ và góc $\theta$ hợp bởi hợp lực với sợi dây của Rover.

**Hướng đi:**
- Chọn trục tọa độ $Ox$ trùng với phương sợi dây của chú chó Rover. Khi đó, sợi dây của chú chó Fido hợp với trục $Ox$ một góc $60{,}0^\circ$.
- Phân tích từng lực thành các thành phần $x$ và $y$.
- Tính các thành phần của hợp lực: $R_x = F_{1x} + F_{2x}$ và $R_y = F_{1y} + F_{2y}$.
- Tính độ lớn $R = \sqrt{R_x^2 + R_y^2}$ và hướng $\theta = \arctan(R_y / R_x)$. Có thể kiểm tra lại độ lớn bằng định lý hàm số cosin trong tam giác lực.

**Lời giải chi tiết:**

Chọn hệ trục tọa độ vuông góc $Oxy$ trên mặt phẳng nằm ngang sao cho trục $Ox$ hướng dọc theo sợi dây của Rover:
1. **Phân tích các lực thành phần:**
- Lực do chú chó Rover tác dụng:
$$
F_{1x} = 270\,\mathrm N, \quad F_{1y} = 0
$$
- Lực do chú chó Fido tác dụng:
$$
\begin{aligned}
F_{2x} &= F_2 \cos(60{,}0^\circ) \\
&= 300(0{,}500) = 150\,\mathrm N
\end{aligned}
$$
$$
\begin{aligned}
F_{2y} &= F_2 \sin(60{,}0^\circ) \\
&= 300(0{,}8660) \approx 259{,}8\,\mathrm N
\end{aligned}
$$

2. **Các thành phần của hợp lực:**
$$
\begin{aligned}
R_x &= F_{1x} + F_{2x} \\
&= 270 + 150 = 420\,\mathrm N
\end{aligned}
$$
$$
R_y = F_{1y} + F_{2y} = 259{,}8\,\mathrm N
$$

3. **Độ lớn của hợp lực:**
$$
\begin{aligned}
R &= \sqrt{R_x^2 + R_y^2} \\
&= \sqrt{420^2 + 259{,}8^2} \\
&= \sqrt{176400 + 67500} \\
&= \sqrt{243900} \approx 494\,\mathrm N
\end{aligned}
$$

4. **Góc tạo với sợi dây của Rover:**
$$
\tan\theta = \frac{259{,}8}{420} \approx 0{,}6186
$$
Suy ra góc lệch:
$$
\theta \approx 31{,}8^\circ
$$

Kết luận: Hợp lực tác dụng lên chiếc cọc có độ lớn $494\,\mathrm N$ và lệch một góc $31{,}8^\circ$ so với phương dây kéo của Rover.

</details>

---

### 4.2: Ba lực kéo cứu hộ xe ô tô bị sa lầy

*Độ khó: Mức 1.*

Để kéo một chiếc xe SUV bị sa lầy trong bùn, các công nhân sử dụng ba sợi dây nằm ngang tạo ra các vector lực như mô tả trên Hình E4.2.
(a) Tìm các thành phần $x$ và $y$ của mỗi lực kéo trong ba lực kéo này.
(b) Sử dụng các thành phần vừa tìm được để xác định độ lớn và hướng của hợp lực của ba lực kéo đó.

![Hình E4.2: Các lực kéo giải cứu xe SUV bị sa lầy trong bùn.](/vat-ly-1/bai-giang/img/young-04/r-exercises-e4-2.png)

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Lực $\vec F_1$ có độ lớn $985\,\mathrm N$, nằm ở góc phần tư thứ I, hợp với trục $+x$ một góc $31^\circ$.
- Lực $\vec F_2$ có độ lớn $788\,\mathrm N$, nằm ở góc phần tư thứ II, hợp với trục $+y$ một góc $32^\circ$.
- Lực $\vec F_3$ có độ lớn $411\,\mathrm N$, nằm ở góc phần tư thứ III, hợp với trục $-x$ một góc $53^\circ$.
- Cần tìm: Các thành phần $(F_x, F_y)$ của từng lực, thành phần hợp lực $(R_x, R_y)$, độ lớn $R$ và hướng $\theta$.

**Hướng đi:**
- Xác định góc lượng giác của từng vector lực đối với hệ trục $Oxy$ chuẩn.
- Chiếu từng vector lên trục $Ox$ và $Oy$ bằng hàm lượng giác thích hợp, chú ý dấu của từng góc phần tư.
- Tính tổng các thành phần để có hợp lực: $R_x = \sum F_x$ và $R_y = \sum F_y$.
- Tính độ lớn $R = \sqrt{R_x^2 + R_y^2}$ và góc nghiêng $\theta = \arctan(R_y / R_x)$.

**Lời giải chi tiết:**

**(a) Các thành phần $x$ và $y$ của từng lực:**

1. **Lực kéo thứ nhất ($F_1 = 985\,\mathrm N$, góc $31^\circ$ so với trục $+x$):**
$$
\begin{aligned}
F_{1x} &= 985 \cos(31^\circ) \\
&\approx +844\,\mathrm N
\end{aligned}
$$
$$
\begin{aligned}
F_{1y} &= 985 \sin(31^\circ) \\
&\approx +507\,\mathrm N
\end{aligned}
$$

2. **Lực kéo thứ hai ($F_2 = 788\,\mathrm N$, lệch $32^\circ$ về phía bên trái trục $+y$):**
Vector nằm trong góc phần tư thứ II, do đó thành phần $x$ âm và thành phần $y$ dương:
$$
\begin{aligned}
F_{2x} &= -788 \sin(32^\circ) \\
&\approx -418\,\mathrm N
\end{aligned}
$$
$$
\begin{aligned}
F_{2y} &= 788 \cos(32^\circ) \\
&\approx +668\,\mathrm N
\end{aligned}
$$

3. **Lực kéo thứ ba ($F_3 = 411\,\mathrm N$, lệch $53^\circ$ xuống dưới trục $-x$):**
Vector nằm trong góc phần tư thứ III, do đó cả hai thành phần đều mang dấu âm:
$$
\begin{aligned}
F_{3x} &= -411 \cos(53^\circ) \\
&\approx -247\,\mathrm N
\end{aligned}
$$
$$
\begin{aligned}
F_{3y} &= -411 \sin(53^\circ) \\
&\approx -328\,\mathrm N
\end{aligned}
$$

**(b) Độ lớn và hướng của hợp lực:**

1. **Cộng các thành phần:**
$$
\begin{aligned}
R_x &= F_{1x} + F_{2x} + F_{3x} \\
&= 844{,}3 - 417{,}6 - 247{,}4 \\
&= +179{,}3\,\mathrm N \approx 179\,\mathrm N
\end{aligned}
$$
$$
\begin{aligned}
R_y &= F_{1y} + F_{2y} + F_{3y} \\
&= 507{,}3 + 668{,}3 - 328{,}2 \\
&= +847{,}4\,\mathrm N \approx 847\,\mathrm N
\end{aligned}
$$

2. **Độ lớn của hợp lực:**
$$
\begin{aligned}
R &= \sqrt{R_x^2 + R_y^2} \\
&= \sqrt{(179{,}3)^2 + (847{,}4)^2} \\
&= \sqrt{32148 + 718087} \\
&= \sqrt{750235} \approx 866\,\mathrm N
\end{aligned}
$$

3. **Hướng của hợp lực:**
Vì cả $R_x > 0$ và $R_y > 0$, hợp lực nằm ở góc phần tư thứ I:
$$
\tan\theta = \frac{847{,}4}{179{,}3} \approx 4{,}726
$$
Suy ra góc hợp với trục $+x$ hướng ngược chiều kim đồng hồ:
$$
\theta \approx 78^\circ
$$

</details>

---

### 4.3: Đai cố định xương hàm

*Độ khó: Mức 1. Ứng dụng sinh học (BIO).*

Do bị chấn thương ở hàm, một bệnh nhân phải đeo đai cố định (Hình E4.3) tạo ra lực tổng hợp hướng thẳng đứng lên trên có độ lớn $5{,}00\,\mathrm N$ tác dụng vào cằm. Lực căng là như nhau dọc theo toàn bộ sợi dây đai. Cần điều chỉnh lực căng của đai đến giá trị bằng bao nhiêu để tạo ra đúng lực nâng cần thiết này?

![Hình E4.3: Đai cố định hỗ trợ hàm dưới của bệnh nhân.](/vat-ly-1/bai-giang/img/young-04/r-exercises-e4-3.png)

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Góc mở giữa hai nhánh dây đai tại cằm: $\alpha = 75{,}0^\circ$.
- Lực nâng tổng hợp hướng thẳng đứng lên trên: $F_y = 5{,}00\,\mathrm N$.
- Lực căng trong hai nhánh đai bằng nhau: $T_1 = T_2 = T$.
- Cần tìm: Lực căng $T$ của dây đai.

**Hướng đi:**
- Nhận xét tính đối xứng: Trục thẳng đứng đi qua cằm chia góc $75{,}0^\circ$ thành hai nửa góc bằng nhau, mỗi nửa bằng $\theta = 75{,}0^\circ / 2 = 37{,}5^\circ$ so với phương thẳng đứng.
- Thành phần theo phương ngang của hai nhánh đai triệt tiêu lẫn nhau do đối xứng.
- Thành phần theo phương thẳng đứng hướng lên của mỗi nhánh đai là $T \cos\theta$.
- Tổng lực hướng lên là $2T \cos\theta = F_y$, từ đó giải ra lực căng $T$.

**Lời giải chi tiết:**

Góc hợp bởi mỗi nhánh dây đai với phương thẳng đứng là:
$$
\theta = \frac{75{,}0^\circ}{2} = 37{,}5^\circ
$$
Tổng lực theo phương thẳng đứng tác dụng lên cằm bằng tổng các thành phần thẳng đứng của hai nhánh dây:
$$
F_y = 2T \cos(37{,}5^\circ)
$$
Thay số với $F_y = 5{,}00\,\mathrm N$:
$$
5{,}00\,\mathrm N = 2T \cos(37{,}5^\circ)
$$
Suy ra lực căng của đai:
$$
\begin{aligned}
T &= \frac{5{,}00\,\mathrm N}{2 \cos(37{,}5^\circ)} \\
&= \frac{5{,}00\,\mathrm N}{2(0{,}79335)} \\
&= \frac{5{,}00}{1{,}5867} \approx 3{,}15\,\mathrm N
\end{aligned}
$$

Kết luận: Lực căng của đai cần được điều chỉnh ở mức $3{,}15\,\mathrm N$.

</details>

---

### 4.4: Kéo hòm hàng lên cầu dốc xe tải

*Độ khó: Mức 1.*

Một người đàn ông đang kéo một chiếc hòm lớn lên cầu dốc của xe tải chở đồ. Cầu dốc có góc nghiêng $20{,}0^\circ$ so với mặt đất nằm ngang, và người đàn ông kéo lên với một lực $\vec F$ có hướng hợp một góc $30{,}0^\circ$ so với mặt phẳng cầu dốc (Hình E4.4).
(a) Độ lớn lực kéo $F$ cần phải bằng bao nhiêu để thành phần lực $F_x$ song song với cầu dốc đạt giá trị $90{,}0\,\mathrm N$?
(b) Khi đó, thành phần lực $F_y$ vuông góc với mặt phẳng cầu dốc sẽ bằng bao nhiêu?

![Hình E4.4: Lực kéo hòm hàng theo phương nghiêng trên cầu dốc.](/vat-ly-1/bai-giang/img/young-04/r-exercises-e4-4.png)

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Góc nghiêng của cầu dốc so với mặt đất: $20{,}0^\circ$.
- Góc hợp bởi lực kéo $\vec F$ với mặt phẳng dốc: $\theta = 30{,}0^\circ$.
- Thành phần song song với mặt dốc: $F_x = 90{,}0\,\mathrm N$.
- Cần tìm: Độ lớn lực kéo $F$ và thành phần vuông góc với mặt dốc $F_y$.

**Hướng đi:**
- Chọn trục tọa độ sao cho trục $Ox$ song song với mặt phẳng cầu dốc và hướng lên trên, còn trục $Oy$ vuông góc với mặt phẳng cầu dốc và hướng lên trên.
- Khi đó, góc giữa vector lực $\vec F$ và trục $Ox$ chính là $\theta = 30{,}0^\circ$. Góc dốc $20{,}0^\circ$ của sàn xe là thông tin phụ trợ mô tả bối cảnh bài toán, không ảnh hưởng đến mối liên hệ lượng giác giữa $\vec F$ và hệ trục tọa độ gắn với mặt dốc.
- Áp dụng các định nghĩa hình chiếu lượng giác: $F_x = F \cos\theta$ và $F_y = F \sin\theta$.

**Lời giải chi tiết:**

**(a) Độ lớn lực kéo $F$:**

Theo định nghĩa hình chiếu lên trục $Ox$ song song với mặt dốc:
$$
F_x = F \cos(30{,}0^\circ)
$$
Suy ra độ lớn của lực kéo:
$$
\begin{aligned}
F &= \frac{F_x}{\cos(30{,}0^\circ)} \\
&= \frac{90{,}0\,\mathrm N}{\cos(30{,}0^\circ)} \\
&= \frac{90{,}0}{0{,}8660} \approx 104\,\mathrm N
\end{aligned}
$$

**(b) Thành phần vuông góc với mặt dốc $F_y$:**

Thành phần lực vuông góc với mặt dốc được xác định bởi:
$$
\begin{aligned}
F_y &= F \sin(30{,}0^\circ) \\
&= 103{,}92(0{,}500) \approx 52{,}0\,\mathrm N
\end{aligned}
$$
Hoặc tính trực tiếp thông qua $F_x$:
$$
\begin{aligned}
F_y &= F_x \tan(30{,}0^\circ) \\
&= \frac{90{,}0}{\sqrt{3}} \approx 52{,}0\,\mathrm N
\end{aligned}
$$

Kết luận: Độ lớn lực kéo cần tác dụng là $104\,\mathrm N$, và thành phần vuông góc với mặt dốc khi đó là $52{,}0\,\mathrm N$.

</details>

---

### 4.5: Hợp lực của hai lực đồng quy trên mặt phẳng

*Độ khó: Mức 1.*

Hai lực $\vec F_1$ và $\vec F_2$ cùng tác dụng vào một điểm. Độ lớn của lực $\vec F_1$ là $9{,}00\,\mathrm N$, có hướng ở góc phần tư thứ II và hợp một góc $60{,}0^\circ$ phía trên trục $x$. Độ lớn của lực $\vec F_2$ là $6{,}00\,\mathrm N$, có hướng ở góc phần tư thứ III và hợp một góc $53{,}1^\circ$ phía dưới trục $x$.
(a) Các thành phần $x$ và $y$ của hợp lực bằng bao nhiêu?
(b) Độ lớn của hợp lực bằng bao nhiêu?

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Lực $\vec F_1$: $F_1 = 9{,}00\,\mathrm N$, góc $60{,}0^\circ$ trên trục $-x$ (góc phần tư thứ II).
- Lực $\vec F_2$: $F_2 = 6{,}00\,\mathrm N$, góc $53{,}1^\circ$ dưới trục $-x$ (góc phần tư thứ III).
- Cần tìm: Thành phần $(R_x, R_y)$ và độ lớn $R$ của hợp lực.

**Hướng đi:**
- Chiếu các lực lên trục $Ox$ và $Oy$:
  - Trong góc phần tư thứ II: $F_{1x} = -F_1 \cos(60{,}0^\circ)$, $F_{1y} = +F_1 \sin(60{,}0^\circ)$.
  - Trong góc phần tư thứ III: $F_{2x} = -F_2 \cos(53{,}1^\circ)$, $F_{2y} = -F_2 \sin(53{,}1^\circ)$.
- Tính tổng các thành phần: $R_x = F_{1x} + F_{2x}$ và $R_y = F_{1y} + F_{2y}$.
- Tính độ lớn bằng định lý Pythagoras: $R = \sqrt{R_x^2 + R_y^2}$.

**Lời giải chi tiết:**

**(a) Các thành phần của hợp lực:**

1. **Chiếu lực $\vec F_1$:**
$$
\begin{aligned}
F_{1x} &= -9{,}00 \cos(60{,}0^\circ) \\
&= -4{,}50\,\mathrm N
\end{aligned}
$$
$$
\begin{aligned}
F_{1y} &= 9{,}00 \sin(60{,}0^\circ) \\
&\approx +7{,}794\,\mathrm N
\end{aligned}
$$

2. **Chiếu lực $\vec F_2$:**
$$
\begin{aligned}
F_{2x} &= -6{,}00 \cos(53{,}1^\circ) \\
&\approx -3{,}60\,\mathrm N
\end{aligned}
$$
$$
\begin{aligned}
F_{2y} &= -6{,}00 \sin(53{,}1^\circ) \\
&\approx -4{,}80\,\mathrm N
\end{aligned}
$$

3. **Cộng các thành phần của hợp lực:**
$$
\begin{aligned}
R_x &= F_{1x} + F_{2x} \\
&= -8{,}10\,\mathrm N
\end{aligned}
$$
$$
\begin{aligned}
R_y &= F_{1y} + F_{2y} \\
&\approx +3{,}00\,\mathrm N
\end{aligned}
$$

**(b) Độ lớn của hợp lực:**
$$
\begin{aligned}
R &= \sqrt{R_x^2 + R_y^2} \\
&= \sqrt{(-8{,}10)^2 + (3{,}00)^2} \\
&= \sqrt{65{,}61 + 9{,}00} \\
&= \sqrt{74{,}61} \approx 8{,}64\,\mathrm N
\end{aligned}
$$

Kết luận: Hợp lực có các thành phần $R_x = -8{,}10\,\mathrm N$, $R_y = +3{,}00\,\mathrm N$, và độ lớn bằng $8{,}64\,\mathrm N$.

</details>

---

## Mục 4.3: Định luật II Newton

### 4.6: Chuyển động của electron trong đèn hình tivi

*Độ khó: Mức 1.*

Một electron (khối lượng $m = 9{,}11 \times 10^{-31}\,\mathrm{kg}$) rời một đầu của ống đèn hình tivi với vận tốc ban đầu bằng không và chuyển động thẳng tới lưới gia tốc cách đó $1{,}80\,\mathrm{cm}$. Electron tới lưới gia tốc với tốc độ $3{,}00 \times 10^6\,\mathrm{m/s}$. Giả sử lực gia tốc là không đổi, hãy tính:
(a) Gia tốc của electron.
(b) Thời gian để electron bay tới lưới gia tốc.
(c) Hợp lực tác dụng lên electron theo đơn vị newton. Có thể bỏ qua lực hấp dẫn tác dụng lên electron.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Khối lượng electron: $m = 9{,}11 \times 10^{-31}\,\mathrm{kg}$.
- Vận tốc ban đầu: $v_{0x} = 0$.
- Quãng đường dịch chuyển: $d = 1{,}80\,\mathrm{cm} = 0{,}0180\,\mathrm m$.
- Vận tốc khi tới lưới: $v_x = 3{,}00 \times 10^6\,\mathrm{m/s}$.
- Cần tìm: Gia tốc $a_x$, thời gian $t$, và hợp lực tác dụng $F_{\mathrm{net}}$.

**Hướng đi:**
- Vì lực không đổi nên chuyển động là chuyển động thẳng biến đổi đều.
- Dùng công thức độc lập với thời gian: $v_x^2 - v_{0x}^2 = 2a_x d$ để tìm gia tốc $a_x$.
- Dùng phương trình vận tốc: $v_x = v_{0x} + a_x t$ để tìm thời gian bay $t$.
- Áp dụng định luật II Newton: $F_{\mathrm{net}} = m a_x$ để xác định hợp lực.

**Lời giải chi tiết:**

**(a) Gia tốc của electron:**
$$
v_x^2 = v_{0x}^2 + 2 a_x d
$$
Thay số với $v_{0x} = 0$:
$$
(3{,}00 \times 10^6)^2 = 2 a_x (0{,}0180)
$$
$$
9{,}00 \times 10^{12} = 0{,}0360 a_x
$$
Suy ra:
$$
\begin{aligned}
a_x &= \frac{9{,}00 \times 10^{12}}{0{,}0360} \\
&= 2{,}50 \times 10^{14}\,\mathrm{m/s^2}
\end{aligned}
$$

**(b) Thời gian để electron tới lưới gia tốc:**
$$
v_x = v_{0x} + a_x t \implies t = \frac{v_x}{a_x}
$$
Thay số:
$$
\begin{aligned}
t &= \frac{3{,}00 \times 10^6\,\mathrm{m/s}}{2{,}50 \times 10^{14}\,\mathrm{m/s^2}} \\
&= 1{,}20 \times 10^{-8}\,\mathrm s = 12{,}0\,\mathrm{ns}
\end{aligned}
$$

**(c) Hợp lực tác dụng lên electron:**

Áp dụng định luật II Newton:
$$
\begin{aligned}
F_{\mathrm{net}} &= m a_x \\
&=22{,}775\times10^{-17} \\
&\approx 2{,}28 \times 10^{-16}\,\mathrm N
\end{aligned}
$$

Kết luận: Gia tốc của electron là $2{,}50 \times 10^{14}\,\mathrm{m/s^2}$, thời gian bay là $12{,}0\,\mathrm{ns}$, và hợp lực tác dụng lên nó là $2{,}28 \times 10^{-16}\,\mathrm N$.

</details>

---

### 4.7: Lực ma sát hãm người trượt băng

*Độ khó: Mức 2.*

Một vận động viên trượt băng có khối lượng $68{,}5\,\mathrm{kg}$ đang chuyển động với vận tốc ban đầu $2{,}40\,\mathrm{m/s}$ trên mặt băng nằm ngang gồ ghề thì dừng lại đều sau khoảng thời gian $3{,}52\,\mathrm s$ do ma sát từ mặt băng. Hỏi lực ma sát mà mặt băng tác dụng lên người trượt băng có độ lớn bằng bao nhiêu và có hướng như thế nào?

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Khối lượng vận động viên: $m = 68{,}5\,\mathrm{kg}$.
- Vận tốc ban đầu: $v_{0x} = 2{,}40\,\mathrm{m/s}$.
- Vận tốc lúc dừng lại: $v_x = 0$.
- Thời gian hãm dừng: $t = 3{,}52\,\mathrm s$.
- Cần tìm: Lực ma sát $f$ tác dụng lên vận động viên.

**Hướng đi:**
- Xác định gia tốc của vận động viên từ công thức động học biến đổi đều: $a_x = (v_x - v_{0x}) / t$.
- Theo phương ngang chỉ có lực ma sát tác dụng, do đó lực ma sát đóng vai trò là hợp lực tác dụng lên vận động viên: $\sum F_x = -f = m a_x$.
- Từ đó tìm độ lớn và hướng của lực ma sát.

**Lời giải chi tiết:**

Chọn chiều dương là chiều chuyển động ban đầu của vận động viên trượt băng:
1. **Tính gia tốc của vận động viên:**
$$
\begin{aligned}
a_x &= \frac{v_x - v_{0x}}{t} \\
&= \frac{-2{,}40}{3{,}52} \approx -0{,}682\,\mathrm{m/s^2}
\end{aligned}
$$

2. **Tính lực ma sát theo định luật II Newton:**
$$
\sum F_x = -f = m a_x
$$
Suy ra độ lớn của lực ma sát:
$$
\begin{aligned}
f &= m |a_x| \\
&= (68{,}5\,\mathrm{kg})(0{,}6818\,\mathrm{m/s^2}) \\
&\approx 46{,}7\,\mathrm N
\end{aligned}
$$

Dấu âm của gia tốc cho thấy lực ma sát hướng ngược chiều với chiều chuyển động của người trượt băng.

Kết luận: Lực ma sát có độ lớn $46{,}7\,\mathrm N$ và có hướng ngược chiều chuyển động của vận động viên.

</details>

---

### 4.8: Cân trọng lượng và sức căng dây trong thang máy chuyển động

*Độ khó: Mức 2.*

Bạn bước vào một thang máy, đứng lên một chiếc cân và bấm nút đi lên. Bạn nhớ rằng trọng lượng bình thường của mình khi đứng yên là $625\,\mathrm N$. Hãy vẽ sơ đồ lực cho người và gói hàng.
(a) Khi thang máy chuyển động với gia tốc hướng lên trên có độ lớn $2{,}50\,\mathrm{m/s^2}$, chiếc cân sẽ chỉ giá trị bằng bao nhiêu?
(b) Nếu bạn đang cầm một gói hàng khối lượng $3{,}85\,\mathrm{kg}$ bằng một sợi dây nhẹ thẳng đứng, lực căng trong sợi dây này bằng bao nhiêu khi thang máy đang chuyển động với gia tốc như ở câu (a)?

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Trọng lượng tĩnh của người: $w = 625\,\mathrm N$, gia tốc trọng trường $g = 9{,}80\,\mathrm{m/s^2}$.
- Gia tốc của thang máy hướng lên: $a_y = +2{,}50\,\mathrm{m/s^2}$.
- Khối lượng gói hàng: $m_p = 3{,}85\,\mathrm{kg}$.
- Cần tìm: Số chỉ của cân $n$ và lực căng dây $T$.

**Hướng đi:**
- Số chỉ của cân chính là độ lớn phản lực pháp tuyến $n$ mà mặt cân tác dụng nâng đỡ bàn chân người.
- Khối lượng của người được xác định từ trọng lượng tĩnh: $m = w / g$.
- Viết phương trình định luật II Newton cho người: $\sum F_y = n - w = m a_y$, kéo theo $n = m(g + a_y)$.
- Viết phương trình định luật II Newton cho gói hàng: $\sum F_y = T - m_p g = m_p a_y$, kéo theo $T = m_p(g + a_y)$.

**Lời giải chi tiết:**

![Sơ đồ lực trong lời giải 4.8.](/vat-ly-1/bai-giang/img/young-04/parent-solution-4-8.svg)

**(a) Số chỉ của cân:**

Khối lượng của bạn là:
$$
m = \frac{625}{9{,}80} \approx 63{,}78\,\mathrm{kg}
$$
Chọn trục $Oy$ thẳng đứng hướng lên trên. Các lực tác dụng lên bạn gồm trọng lực $w$ hướng xuống và phản lực pháp tuyến $n$ từ mặt cân hướng lên. Áp dụng định luật II Newton:
$$
\sum F_y = n - w = m a_y
$$
Suy ra phản lực pháp tuyến:
$$
n = w + m a_y = m(g + a_y)
$$
Thay số:
$$
\begin{aligned}
n &= (63{,}78)(9{,}80 + 2{,}50) \\
&= 63{,}78(12{,}30) \approx 784\,\mathrm N
\end{aligned}
$$
Như vậy, số chỉ của cân khi thang máy tăng tốc đi lên là $784\,\mathrm N$ (lớn hơn trọng lượng tĩnh thực tế).

**(b) Lực căng trong sợi dây treo gói hàng:**

Các lực tác dụng lên gói hàng gồm trọng lực $w_p = m_p g$ hướng xuống và lực căng dây $T$ hướng lên. Áp dụng định luật II Newton cho gói hàng:
$$
\sum F_y = T - m_p g = m_p a_y
$$
Suy ra lực căng:
$$
T = m_p(g + a_y)
$$
Thay số:
$$
\begin{aligned}
T &= 3{,}85(9{,}80 + 2{,}50) \\
&= 3{,}85(12{,}30) \approx 47{,}4\,\mathrm N
\end{aligned}
$$

Kết luận: Chiếc cân sẽ chỉ $784\,\mathrm N$, và lực căng trong sợi dây treo gói hàng là $47{,}4\,\mathrm N$.

</details>

---

### 4.9: Kéo thùng hàng trên mặt ao đóng băng

*Độ khó: Mức 1.*

Một chiếc thùng nằm yên trên mặt ao đóng băng, đóng vai trò như một bề mặt nằm ngang không có ma sát. Nếu một người đánh cá tác dụng một lực nằm ngang có độ lớn $48{,}0\,\mathrm N$ vào chiếc thùng và làm cho nó thu được một gia tốc có độ lớn $2{,}20\,\mathrm{m/s^2}$, hãy tính khối lượng của chiếc thùng đó.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Lực nằm ngang tác dụng: $F = 48{,}0\,\mathrm N$.
- Gia tốc thu được: $a = 2{,}20\,\mathrm{m/s^2}$.
- Bề mặt nằm ngang không ma sát.
- Cần tìm: Khối lượng $m$ của chiếc thùng.

**Hướng đi:**
- Vì bề mặt không ma sát, theo phương ngang chỉ có duy nhất lực kéo $F$ tác dụng.
- Áp dụng trực tiếp định luật II Newton theo phương ngang: $\sum F_x = F = ma$.
- Giải ra khối lượng: $m = F / a$.

**Lời giải chi tiết:**

Theo định luật II Newton, gia tốc của vật liên hệ với hợp lực tác dụng và khối lượng quán tính của vật thông qua hệ thức:
$$
\sum F_x = m a_x \implies F = ma
$$
Suy ra khối lượng của chiếc thùng:
$$
m = \frac{48{,}0}{2{,}20} \approx 21{,}8\,\mathrm{kg}
$$

Kết luận: Khối lượng của chiếc thùng là $21{,}8\,\mathrm{kg}$.

</details>

---

### 4.10: Đẩy khối băng trên sàn nhẵn

*Độ khó: Mức 2.*

Một công nhân bến tàu tác dụng một lực nằm ngang không đổi bằng $80{,}0\,\mathrm N$ vào một khối băng trên một mặt sàn nằm ngang nhẵn bóng. Có thể bỏ qua lực ma sát. Khối băng bắt đầu chuyển động từ trạng thái nghỉ và đi được quãng đường $11{,}0\,\mathrm m$ trong $5{,}00\,\mathrm s$.
(a) Khối lượng của khối băng là bao nhiêu?
(b) Nếu người công nhân ngừng đẩy ở thời điểm hết $5{,}00\,\mathrm s$, khối băng sẽ đi thêm được một quãng đường bằng bao nhiêu trong $5{,}00\,\mathrm s$ tiếp theo?

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Lực đẩy không đổi: $F = 80{,}0\,\mathrm N$.
- Vận tốc ban đầu: $v_0 = 0$.
- Quãng đường đi được trong $5{,}00\,\mathrm s$ đầu tiên: $d_1 = 11{,}0\,\mathrm m$, $t_1 = 5{,}00\,\mathrm s$.
- Cần tìm: Khối lượng $m$ của khối băng và quãng đường $d_2$ đi được trong $t_2 = 5{,}00\,\mathrm s$ tiếp theo sau khi ngừng tác dụng lực.

**Hướng đi:**
- Trong giai đoạn đầu ($0 \le t \le 5{,}00\,\mathrm s$): Chuyển động thẳng biến đổi đều với vận tốc đầu bằng không. Từ phương trình $d_1 = \frac{1}{2} a t_1^2$ tìm được gia tốc $a$.
- Dùng định luật II Newton $F = ma$ để tìm khối lượng $m$.
- Xác định vận tốc của khối băng ở cuối giây thứ $5{,}00$: $v_1 = a t_1$.
- Trong giai đoạn hai ($5{,}00\,\mathrm s$ tiếp theo): Sau khi ngừng đẩy, hợp lực tác dụng lên khối băng bằng không. Theo định luật I Newton, khối băng sẽ chuyển động thẳng đều với vận tốc không đổi $v_1$. Do đó quãng đường là $d_2 = v_1 t_2$.

**Lời giải chi tiết:**

**(a) Khối lượng của khối băng:**

Phương trình chuyển động thẳng nhanh dần đều từ trạng thái nghỉ:
$$
d_1 = \frac{1}{2} a t_1^2
$$
Thay số với $d_1 = 11{,}0\,\mathrm m$ và $t_1 = 5{,}00\,\mathrm s$:
$$
11{,}0 = \frac{1}{2} a (5{,}00)^2 = 12{,}5 a
$$
Gia tốc của khối băng:
$$
a = \frac{11{,}0}{12{,}5} = 0{,}880\,\mathrm{m/s^2}
$$
Áp dụng định luật II Newton:
$$
m = \frac{80{,}0}{0{,}880} \approx 90{,}9\,\mathrm{kg}
$$

**(b) Quãng đường đi thêm trong $5{,}00\,\mathrm s$ tiếp theo:**

Vận tốc của khối băng ở thời điểm $t_1 = 5{,}00\,\mathrm s$ là:
$$
\begin{aligned}
v_1 &= a t_1 \\
&= 0{,}880(5{,}00) = 4{,}40\,\mathrm{m/s}
\end{aligned}
$$
Khi người công nhân ngừng đẩy, không còn lực nằm ngang nào tác dụng lên khối băng (vì bỏ qua ma sát). Theo định luật I Newton, khối băng duy trì chuyển động thẳng đều với vận tốc $v = 4{,}40\,\mathrm{m/s}$.

Quãng đường đi được trong $t_2 = 5{,}00\,\mathrm s$ tiếp theo là:
$$
\begin{aligned}
d_2 &= v_1 t_2 \\
&= 4{,}40(5{,}00) = 22{,}0\,\mathrm m
\end{aligned}
$$

Kết luận: Khối lượng của khối băng là $90{,}9\,\mathrm{kg}$, và nó sẽ đi thêm được $22{,}0\,\mathrm m$ trong $5{,}00\,\mathrm s$ tiếp theo.

</details>

---

### 4.11: Đẩy đĩa khúc côn cầu theo từng giai đoạn

*Độ khó: Mức 1.*

Một đĩa khúc côn cầu trên băng có khối lượng $0{,}160\,\mathrm{kg}$ đang đứng yên tại gốc tọa độ ($x = 0$) trên mặt sân băng nằm ngang không có ma sát. Tại thời điểm $t = 0$, một cầu thủ tác dụng một lực $0{,}250\,\mathrm N$ song song với trục $x$ lên đĩa; cô tiếp tục duy trì lực này cho đến thời điểm $t = 2{,}00\,\mathrm s$.
(a) Vị trí và tốc độ của đĩa tại thời điểm $t = 2{,}00\,\mathrm s$ bằng bao nhiêu?
(b) Nếu chính lực đó được tác dụng trở lại tại thời điểm $t = 5{,}00\,\mathrm s$ cho đến $t = 7{,}00\,\mathrm s$, vị trí và tốc độ của đĩa tại thời điểm $t = 7{,}00\,\mathrm s$ bằng bao nhiêu?

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Khối lượng đĩa: $m = 0{,}160\,\mathrm{kg}$.
- Vị trí và vận tốc ban đầu: $x(0) = 0$, $v(0) = 0$.
- Giai đoạn 1 ($0 \le t \le 2{,}00\,\mathrm s$): Tác dụng lực $F = 0{,}250\,\mathrm N$.
- Giai đoạn 2 ($2{,}00\,\mathrm s \le t \le 5{,}00\,\mathrm s$): Lực tác dụng $F = 0$.
- Giai đoạn 3 ($5{,}00\,\mathrm s \le t \le 7{,}00\,\mathrm s$): Tác dụng lại lực $F = 0{,}250\,\mathrm N$.
- Cần tìm: Tọa độ và vận tốc tại $t = 2{,}00\,\mathrm s$ và tại $t = 7{,}00\,\mathrm s$.

**Hướng đi:**
- Giai đoạn 1: Tính gia tốc $a_1 = F / m$. Dùng phương trình chuyển động biến đổi đều để tìm $x_1$ và $v_1$ tại $t = 2{,}00\,\mathrm s$.
- Giai đoạn 2: Lực bằng không nên đĩa chuyển động thẳng đều với vận tốc $v_1$ trong khoảng thời gian $\Delta t_2 = 3{,}00\,\mathrm s$. Tìm tọa độ $x_2$ tại $t = 5{,}00\,\mathrm s$.
- Giai đoạn 3: Lực tác dụng trở lại tạo ra cùng gia tốc $a_1$ trong khoảng thời gian $\Delta t_3 = 2{,}00\,\mathrm s$. Tính vận tốc $v_3$ và tọa độ $x_3$ tại $t = 7{,}00\,\mathrm s$.

**Lời giải chi tiết:**

**(a) Vị trí và tốc độ tại $t = 2{,}00\,\mathrm s$:**

Gia tốc trong giai đoạn đầu:
$$
a = \frac{0{,}250}{0{,}160} = 1{,}5625\,\mathrm{m/s^2}
$$
Tốc độ của đĩa tại $t = 2{,}00\,\mathrm s$:
$$
v_1 = 1{,}5625(2) \approx 3{,}12\,\mathrm{m/s}
$$
Vị trí của đĩa tại $t = 2{,}00\,\mathrm s$:
$$
\begin{aligned}
x_1 &= \frac{1}{2} a t_1^2 \\
&= \frac{1}{2}(1{,}5625)(4) \approx 3{,}12\,\mathrm m
\end{aligned}
$$

**(b) Vị trí và tốc độ tại $t = 7{,}00\,\mathrm s$:**

1. **Khoảng thời gian từ $t = 2{,}00\,\mathrm s$ đến $t = 5{,}00\,\mathrm s$ ($\Delta t_2 = 3{,}00\,\mathrm s$):**
Vì không có lực tác dụng, đĩa chuyển động thẳng đều với tốc độ không đổi $v = 3{,}125\,\mathrm{m/s}$. Vị trí của đĩa tại $t = 5{,}00\,\mathrm s$ là:
$$
\begin{aligned}
x_2 &= x_1 + v_1 \Delta t_2 \\
&= 3{,}125 + 3{,}125(3) \\
&= 12{,}50\,\mathrm m
\end{aligned}
$$

2. **Khoảng thời gian từ $t = 5{,}00\,\mathrm s$ đến $t = 7{,}00\,\mathrm s$ ($\Delta t_3 = 2{,}00\,\mathrm s$):**
Lực $F = 0{,}250\,\mathrm N$ được áp dụng trở lại, tạo ra gia tốc $a = 1{,}5625\,\mathrm{m/s^2}$.
Tốc độ tại $t = 7{,}00\,\mathrm s$:
$$
\begin{aligned}
v_3 &= v_1 + a \Delta t_3 \\
&= 3{,}125 + 1{,}5625(2) \\
&\approx 6{,}25\,\mathrm{m/s}
\end{aligned}
$$
Vị trí tại $t = 7{,}00\,\mathrm s$, với $\tau=2{,}00\,\mathrm s$ là thời gian tác dụng lực lần thứ hai:
$$
\begin{aligned}
x_3 &= x_2 + v_1\tau+\frac12a\tau^2 \\
&= 12{,}50 + 6{,}25 + 3{,}125 \\
&\approx 21{,}9\,\mathrm m
\end{aligned}
$$

Kết luận: Tại $t = 2{,}00\,\mathrm s$, vị trí là $3{,}12\,\mathrm m$ và tốc độ là $3{,}12\,\mathrm{m/s}$; tại $t = 7{,}00\,\mathrm s$, vị trí là $21{,}9\,\mathrm m$ và tốc độ là $6{,}25\,\mathrm{m/s}$.

</details>

---

### 4.12: Kéo kiện hàng trên sàn nhà kho

*Độ khó: Mức 1.*

Một kiện hàng có khối lượng $32{,}5\,\mathrm{kg}$ ban đầu đứng yên trên sàn nhà kho chịu tác dụng của một hợp lực nằm ngang có độ lớn $14{,}0\,\mathrm N$.
(a) Gia tốc được tạo ra bằng bao nhiêu?
(b) Kiện hàng đi được quãng đường bao xa trong thời gian $10{,}0\,\mathrm s$?
(c) Tốc độ của nó ở thời điểm cuối giây thứ $10{,}0$ là bao nhiêu?

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Khối lượng kiện hàng: $m = 32{,}5\,\mathrm{kg}$.
- Vận tốc ban đầu: $v_0 = 0$.
- Hợp lực nằm ngang: $F_{\mathrm{net}} = 14{,}0\,\mathrm N$.
- Thời gian: $t = 10{,}0\,\mathrm s$.
- Cần tìm: Gia tốc $a$, quãng đường $d$, và tốc độ $v$.

**Hướng đi:**
- Dùng định luật II Newton tính gia tốc: $a = F_{\mathrm{net}} / m$.
- Áp dụng các phương trình động học chuyển động thẳng biến đổi đều: $d = \frac{1}{2} a t^2$ và $v = a t$.

**Lời giải chi tiết:**

**(a) Gia tốc được tạo ra:**
$$
a = \frac{14{,}0}{32{,}5} \approx 0{,}431\,\mathrm{m/s^2}
$$

**(b) Quãng đường đi được trong $10{,}0\,\mathrm s$:**
$$
\begin{aligned}
d &= \frac{1}{2} a t^2 \\
&=\frac12(0{,}4308)(100)\\
&\approx21{,}5\,\mathrm m
\end{aligned}
$$

**(c) Tốc độ ở cuối giây thứ $10{,}0$:**
$$
v = 0{,}4308(10{,}0) \approx 4{,}31\,\mathrm{m/s}
$$

Kết luận: Gia tốc là $0{,}431\,\mathrm{m/s^2}$, quãng đường đi được là $21{,}5\,\mathrm m$, và tốc độ cuối là $4{,}31\,\mathrm{m/s}$.

</details>

---

### 4.13: Phân tích đồ thị gia tốc theo thời gian của xe đẩy thí nghiệm

*Độ khó: Mức 1.*

Một chiếc xe đẩy thí nghiệm có khối lượng $4{,}50\,\mathrm{kg}$ chuyển động thẳng dọc theo trục $x$. Đồ thị trên Hình E4.13 biểu diễn gia tốc của xe theo hàm của thời gian.
(a) Tìm hợp lực cực đại tác dụng lên xe đẩy. Hợp lực cực đại này xuất hiện trong khoảng thời gian nào?
(b) Trong những khoảng thời gian nào thì hợp lực tác dụng lên xe đẩy là không đổi?
(c) Hợp lực tác dụng lên xe đẩy bằng không tại những thời điểm nào?

![Hình E4.13: Đồ thị gia tốc theo thời gian của xe đẩy thí nghiệm.](/vat-ly-1/bai-giang/img/young-04/r-exercises-e4-13.png)

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Khối lượng xe: $m = 4{,}50\,\mathrm{kg}$.
- Đồ thị $a_x(t)$: Hình thang với $a_x$ tăng từ $0$ lên $10{,}0\,\mathrm{m/s^2}$ trong khoảng $[0, 2{,}0\,\mathrm s]$, giữ nguyên $10{,}0\,\mathrm{m/s^2}$ trong khoảng $[2{,}0\,\mathrm s, 4{,}0\,\mathrm s]$, và giảm về $0$ trong khoảng $[4{,}0\,\mathrm s, 6{,}0\,\mathrm s]$.
- Cần tìm: Hợp lực cực đại và thời điểm xuất hiện, các khoảng thời gian hợp lực không đổi, và thời điểm hợp lực bằng không.

**Hướng đi:**
- Theo định luật II Newton: $\sum F_x(t) = m a_x(t)$.
- Vì khối lượng $m > 0$ là hằng số, hợp lực $\sum F_x(t)$ có cùng quy luật biến thiên theo thời gian như gia tốc $a_x(t)$:
  - $F_{\mathrm{net}}$ đạt cực đại khi $a_x$ đạt cực đại.
  - $F_{\mathrm{net}}$ là hằng số khi $a_x$ là hằng số.
  - $F_{\mathrm{net}} = 0$ khi $a_x = 0$.

**Lời giải chi tiết:**

**(a) Hợp lực cực đại tác dụng lên xe:**

Quan sát đồ thị, gia tốc cực đại là $a_{\max} = 10{,}0\,\mathrm{m/s^2}$, duy trì liên tục từ $t = 2{,}0\,\mathrm s$ đến $t = 4{,}0\,\mathrm s$. Hợp lực cực đại tương ứng là:
$$
\begin{aligned}
F_{\mathrm{net, max}} &= m a_{\max} \\
&= 4{,}50(10) = 45{,}0\,\mathrm N
\end{aligned}
$$
Hợp lực cực đại này xuất hiện trong khoảng thời gian từ $2{,}0\,\mathrm s$ đến $4{,}0\,\mathrm s$.

**(b) Khoảng thời gian hợp lực là hằng số:**

Hợp lực là hằng số khi gia tốc không thay đổi theo thời gian.
Đồ thị biểu diễn đường nằm ngang tại $a_x = 10{,}0\,\mathrm{m/s^2}$ trong khoảng từ $2{,}0\,\mathrm s$ đến $4{,}0\,\mathrm s$.
Do đó, hợp lực không đổi trong khoảng thời gian giữa $2{,}0\,\mathrm s$ và $4{,}0\,\mathrm s$.

**(c) Thời điểm hợp lực bằng không:**

Hợp lực bằng không khi và chỉ khi gia tốc bằng không.
Từ đồ thị, $a_x = 0$ tại các thời điểm $t = 0$ và tại $t = 6{,}0\,\mathrm s$.

Kết luận:
- Hợp lực cực đại là $45{,}0\,\mathrm N$, xuất hiện trong khoảng giữa $2{,}0\,\mathrm s$ và $4{,}0\,\mathrm s$.
- Hợp lực không đổi trong khoảng giữa $2{,}0\,\mathrm s$ và $4{,}0\,\mathrm s$.
- Hợp lực bằng không tại $t = 0$ và $t = 6{,}0\,\mathrm s$.

</details>

---

### 4.14: Xác định lực tác dụng lên chú mèo từ đồ thị vận tốc

*Độ khó: Mức 1.*

Một chú mèo khối lượng $2{,}75\,\mathrm{kg}$ chuyển động thẳng dọc theo trục $x$. Hình E4.14 biểu diễn thành phần vận tốc $v_x$ của chú mèo theo thời gian.
(a) Tìm hợp lực cực đại tác dụng lên chú mèo. Lực này xuất hiện trong khoảng thời gian nào?
(b) Hợp lực tác dụng lên chú mèo bằng không trong khoảng thời gian nào?
(c) Hợp lực tác dụng lên chú mèo tại thời điểm $8{,}5\,\mathrm s$ bằng bao nhiêu?

![Hình E4.14: Đồ thị vận tốc theo thời gian của chú mèo.](/vat-ly-1/bai-giang/img/young-04/r-exercises-e4-14.png)

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Khối lượng chú mèo: $m = 2{,}75\,\mathrm{kg}$.
- Đồ thị $v_x(t)$:
  - Đoạn 1: Từ $t = 0$ đến $t = 2{,}0\,\mathrm s$, vận tốc tăng tuyến tính từ $0$ lên $8{,}0\,\mathrm{m/s}$.
  - Đoạn 2: Từ $t = 2{,}0\,\mathrm s$ đến $t = 6{,}0\,\mathrm s$, vận tốc không đổi ở mức $8{,}0\,\mathrm{m/s}$.
  - Đoạn 3: Từ $t = 6{,}0\,\mathrm s$ đến $t = 10{,}0\,\mathrm s$, vận tốc tăng tuyến tính từ $8{,}0\,\mathrm{m/s}$ lên $12{,}0\,\mathrm{m/s}$.
- Cần tìm: Lực cực đại và thời gian xuất hiện, khoảng thời gian lực bằng không, và lực tại $t = 8{,}5\,\mathrm s$.

**Hướng đi:**
- Gia tốc là độ dốc (đạo hàm) của đồ thị vận tốc theo thời gian: $a_x = \Delta v_x / \Delta t$.
- Áp dụng định luật II Newton: $\sum F_x = m a_x$.
- Tính gia tốc và lực cho từng đoạn tuyến tính của đồ thị.

**Lời giải chi tiết:**

1. **Gia tốc trong đoạn 1 ($0 \le t \le 2{,}0\,\mathrm s$):**
$$
a_1 = \frac{8{,}0 - 0}{2{,}0 - 0} = 4{,}0\,\mathrm{m/s^2}
$$
Hợp lực tác dụng:
$$
F_1 = 2{,}75(4{,}0) = 11{,}0\,\mathrm N
$$

2. **Gia tốc trong đoạn 2 ($2{,}0\,\mathrm s \le t \le 6{,}0\,\mathrm s$):**
Đồ thị là đường nằm ngang, vận tốc không đổi nên:
$$
a_2 = 0 \implies F_2 = 0
$$

3. **Gia tốc trong đoạn 3 ($6{,}0\,\mathrm s \le t \le 10{,}0\,\mathrm s$):**
$$
\begin{aligned}
a_3 &= \frac{12{,}0 - 8{,}0}{10{,}0 - 6{,}0} \\
&= \frac{4{,}0}{4{,}0} = 1{,}0\,\mathrm{m/s^2}
\end{aligned}
$$
Hợp lực tác dụng:
$$
F_3 = 2{,}75(1{,}0) = 2{,}75\,\mathrm N
$$

**(a) Hợp lực cực đại:**
Lực cực đại là $F_{\max} = 11{,}0\,\mathrm N$, xuất hiện trong khoảng thời gian từ $t = 0$ đến $t = 2{,}0\,\mathrm s$.

**(b) Khoảng thời gian hợp lực bằng không:**
Hợp lực bằng không trong khoảng thời gian từ $t = 2{,}0\,\mathrm s$ đến $t = 6{,}0\,\mathrm s$.

**(c) Hợp lực tại thời điểm $t = 8{,}5\,\mathrm s$:**
Thời điểm $t = 8{,}5\,\mathrm s$ nằm trong đoạn 3 ($6{,}0\,\mathrm s \le t \le 10{,}0\,\mathrm s$). Trong suốt khoảng thời gian này, gia tốc không đổi và bằng $1{,}0\,\mathrm{m/s^2}$.
Do đó, hợp lực tại $t = 8{,}5\,\mathrm s$ là:
$$
F_{\mathrm{net}} = 2{,}75\,\mathrm N
$$

</details>

---

### 4.15: Động cơ tên lửa nhỏ phụ thuộc thời gian

*Độ khó: Mức 1.*

Một tên lửa nhỏ khối lượng $8{,}00\,\mathrm{kg}$ đốt cháy nhiên liệu tạo ra lực đẩy hướng thẳng đứng lên trên phụ thuộc vào thời gian (giả thiết khối lượng tên lửa giảm không đáng kể và được coi như hằng số) khi tên lửa bay lên khỏi bệ phóng. Lực đẩy này tuân theo phương trình $F = A + B t^2$. Các phép đo thực nghiệm cho thấy tại $t = 0$, lực đẩy là $100{,}0\,\mathrm N$, và sau $2{,}00\,\mathrm s$ đầu tiên, lực đẩy đạt $150{,}0\,\mathrm N$.
(a) Tìm các hằng số $A$ và $B$, bao gồm cả đơn vị SI chuẩn của chúng.
(b) Tìm hợp lực tác dụng lên tên lửa và gia tốc của nó tại các thời điểm:
  (i) Ngay sau khi nhiên liệu bắt lửa.
  (ii) Thời điểm $3{,}00\,\mathrm s$ sau khi nhiên liệu bắt lửa.
(c) Giả sử bạn sử dụng chiếc tên lửa này ngoài không gian vũ trụ sâu, cách xa mọi lực hấp dẫn. Gia tốc của nó tại thời điểm $3{,}00\,\mathrm s$ sau khi bắt lửa sẽ bằng bao nhiêu?

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Khối lượng tên lửa: $m = 8{,}00\,\mathrm{kg}$.
- Lực đẩy động cơ: $F(t) = A + B t^2$.
- Tại $t = 0$: $F(0) = 100{,}0\,\mathrm N$.
- Tại $t = 2{,}00\,\mathrm s$: $F(2{,}00) = 150{,}0\,\mathrm N$.
- Cần tìm: Hằng số $A, B$; hợp lực và gia tốc tại $t = 0$ và $t = 3{,}00\,\mathrm s$; gia tốc tại $t = 3{,}00\,\mathrm s$ khi ở ngoài không gian ($g = 0$).

**Hướng đi:**
- Xác định $A$ và $B$ bằng cách thay các điều kiện ban đầu vào phương trình lực.
- Khi ở gần mặt đất, tên lửa chịu hai lực: Lực đẩy động cơ $F(t)$ hướng lên và trọng lực $w = mg$ hướng xuống.
- Hợp lực theo phương thẳng đứng: $F_{\mathrm{net}} = F(t) - mg$.
- Gia tốc: $a = F_{\mathrm{net}} / m$.
- Ngoài không gian sâu không có trọng lực ($g = 0$), hợp lực chính là lực đẩy của động cơ: $F_{\mathrm{net}} = F(t)$, từ đó tính gia tốc $a = F(t) / m$.

**Lời giải chi tiết:**

**(a) Xác định các hằng số $A$ và $B$:**

Tại thời điểm $t = 0$:
$$
F(0) = A = 100\,\mathrm N
$$
Tại thời điểm $t = 2{,}00\,\mathrm s$:
$$
100{,}0 + 4{,}00 B = 150{,}0\,\mathrm N
$$
$$
\begin{aligned}
4{,}00 B &= 50{,}0 \\
B &= \frac{50{,}0}{4{,}00} = 12{,}5\,\mathrm{N/s^2}
\end{aligned}
$$
Vậy phương trình lực đẩy của động cơ là:
$$
F(t) = 100 + 12{,}5 t^2
$$

**(b) Hợp lực và gia tốc gần bề mặt Trái Đất:**

Trọng lượng của tên lửa:
$$
w = 8{,}00(9{,}80) = 78{,}4\,\mathrm N
$$
Hợp lực tác dụng lên tên lửa:
$$
F_{\mathrm{net}}(t) = F(t) - mg
$$

1. **Tại thời điểm ngay sau khi bắt lửa ($t = 0$):**
$$
\begin{aligned}F_{\mathrm{net}}(0)&=100-78{,}4\\
&=21{,}6\,\mathrm N.\end{aligned}
$$
Gia tốc tương ứng:
$$
a(0) = \frac{21{,}6}{8{,}00} = 2{,}70\,\mathrm{m/s^2}
$$

2. **Tại thời điểm $t = 3{,}00\,\mathrm s$:**
Lực đẩy của động cơ khi này là:
$$
\begin{aligned}
F(3{,}00) &= 100 + 12{,}5(9) \\
&= 212{,}5\,\mathrm N
\end{aligned}
$$
Hợp lực:
$$
\begin{aligned}F_{\mathrm{net}}(3)&=212{,}5-78{,}4\\
&\approx134\,\mathrm N.\end{aligned}
$$
Gia tốc tương ứng:
$$
\begin{aligned}a(3{,}00)&=\frac{134{,}1}{8}\\
&\approx16{,}8\,\mathrm{m/s^2}.\end{aligned}
$$

**(c) Gia tốc ngoài không gian vũ trụ sâu ($g = 0$):**

Khi không có trọng lực, hợp lực tác dụng lên tên lửa bằng chính lực đẩy của động cơ tại $t = 3{,}00\,\mathrm s$:
$$
F_{\mathrm{net}} = F(3{,}00) = 212{,}5\,\mathrm N
$$
Gia tốc của tên lửa ngoài vũ trụ khi đó là:
$$
a = \frac{212{,}5}{8{,}00} \approx 26{,}6\,\mathrm{m/s^2}
$$

</details>

---

## Mục 4.4: Khối lượng và trọng lượng

### 4.16: Balo dụng cụ của nhà du hành vũ trụ

*Độ khó: Mức 1.*

Chiếc balo dụng cụ của một nhà du hành vũ trụ có trọng lượng $17{,}5\,\mathrm N$ khi ở trên Trái Đất, nhưng chỉ nặng $3{,}24\,\mathrm N$ khi ở trên bề mặt của một mặt trăng.
(a) Gia tốc rơi tự do do trọng lực trên bề mặt mặt trăng này bằng bao nhiêu?
(b) Khối lượng của chiếc balo khi ở trên mặt trăng này bằng bao nhiêu?

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Trọng lượng trên Trái Đất: $w_E = 17{,}5\,\mathrm N$.
- Gia tốc trọng trường trên Trái Đất: $g_E = 9{,}80\,\mathrm{m/s^2}$.
- Trọng lượng trên bề mặt mặt trăng: $w_M = 3{,}24\,\mathrm N$.
- Cần tìm: Gia tốc rơi tự do trên mặt trăng $g_M$ và khối lượng của balo trên mặt trăng $m$.

**Hướng đi:**
- Khối lượng $m$ là đặc trưng quán tính nội tại của vật, không phụ thuộc vào vị trí của vật trong vũ trụ.
- Tính khối lượng $m = w_E / g_E$ từ số liệu trên Trái Đất.
- Dùng công thức trọng lượng trên mặt trăng $w_M = m g_M$ để tính gia tốc rơi tự do $g_M = w_M / m$.

**Lời giải chi tiết:**

**(a) Gia tốc rơi tự do trên mặt trăng:**

Khối lượng của chiếc balo là:
$$
m = \frac{17{,}5}{9{,}80} \approx 1{,}786\,\mathrm{kg}
$$
Gia tốc do trọng lực trên mặt trăng là:
$$
\begin{aligned}
g_M &= \frac{w_M}{m} \\
&= \frac{3{,}24\,\mathrm N}{1{,}786\,\mathrm{kg}} \approx 1{,}81\,\mathrm{m/s^2}
\end{aligned}
$$

**(b) Khối lượng của chiếc balo trên mặt trăng:**

Việc chuyển balo sang mặt trăng không làm thay đổi khối lượng của nó:
$$
m \approx 1{,}79\,\mathrm{kg}
$$

Kết luận: Gia tốc rơi tự do trên mặt trăng là $1{,}81\,\mathrm{m/s^2}$, và khối lượng của chiếc balo là $1{,}79\,\mathrm{kg}$.

</details>

---

### 4.17: Siêu nhân ném tảng đá lớn

*Độ khó: Mức 1.*

Siêu nhân ném một tảng đá có trọng lượng $2400\,\mathrm N$ vào đối thủ. Siêu nhân phải tác dụng một lực nằm ngang bằng bao nhiêu để truyền cho tảng đá một gia tốc nằm ngang bằng $12{,}0\,\mathrm{m/s^2}$?

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Trọng lượng của tảng đá: $w = 2400\,\mathrm N$.
- Gia tốc nằm ngang mong muốn: $a = 12{,}0\,\mathrm{m/s^2}$.
- Cần tìm: Lực nằm ngang $F$ mà Siêu nhân cần tác dụng.

**Hướng đi:**
- Tìm khối lượng của tảng đá từ trọng lượng của nó: $m = w / g$.
- Áp dụng định luật II Newton theo phương nằm ngang để tìm lực tác dụng: $F = ma$.

**Lời giải chi tiết:**

Khối lượng của tảng đá là:
$$
m = \frac{2400}{9{,}80} \approx 244{,}9\,\mathrm{kg}
$$
Áp dụng định luật II Newton cho chuyển động theo phương nằm ngang:
$$
\begin{aligned}
F &= m a \\
&= 244{,}9(12{,}0) \approx 2940\,\mathrm N
\end{aligned}
$$

Kết luận: Siêu nhân phải tác dụng một lực nằm ngang có độ lớn $2940\,\mathrm N$.

</details>

---

### 4.18: So sánh khối lượng và trọng lượng của sinh vật

*Độ khó: Mức 1. Ứng dụng sinh học (BIO).*

(a) Một con bọ chét thông thường có khối lượng $210\,\mu\mathrm g$. Nó có trọng lượng bằng bao nhiêu newton?
(b) Khối lượng của một con rầy bọt (froghopper) điển hình là $12{,}3\,\mathrm{mg}$. Nó có trọng lượng bằng bao nhiêu newton?
(c) Một con mèo nhà thường có trọng lượng $45\,\mathrm N$. Nó nặng bao nhiêu pound, và khối lượng của nó theo kilôgam bằng bao nhiêu?

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Khối lượng bọ chét: $m_1 = 210\,\mu\mathrm g$.
- Khối lượng rầy bọt: $m_2 = 12{,}3\,\mathrm{mg}$.
- Trọng lượng mèo nhà: $w_3 = 45\,\mathrm N$.
- Cần tìm: Trọng lượng bọ chét và rầy bọt (theo $\mathrm N$), trọng lượng mèo (theo pound) và khối lượng mèo (theo $\mathrm{kg}$).

**Hướng đi:**
- Đổi các đơn vị khối lượng sang kilôgam: $1\,\mu\mathrm g = 10^{-6}\,\mathrm g = 10^{-9}\,\mathrm{kg}$, và $1\,\mathrm{mg} = 10^{-3}\,\mathrm g = 10^{-6}\,\mathrm{kg}$.
- Áp dụng công thức trọng lượng: $w = mg$ với $g = 9{,}80\,\mathrm{m/s^2}$.
- Đổi đơn vị trọng lượng: $1\,\mathrm{lb} \approx 4{,}448\,\mathrm N$.

**Lời giải chi tiết:**

**(a) Trọng lượng của con bọ chét:**
$$
m_1 = 2{,}10 \times 10^{-7}\,\mathrm{kg}
$$
Trọng lượng của nó là:
$$
\begin{aligned}
w_1 &= m_1 g \\
&= (2{,}10 \times 10^{-7})(9{,}80) \\
&\approx 2{,}06 \times 10^{-6}\,\mathrm N
\end{aligned}
$$

**(b) Trọng lượng của con rầy bọt:**
$$
m_2 = 1{,}23 \times 10^{-5}\,\mathrm{kg}
$$
Trọng lượng của nó là:
$$
\begin{aligned}
w_2 &= m_2 g \\
&= (1{,}23 \times 10^{-5})(9{,}80) \\
&\approx 1{,}21 \times 10^{-4}\,\mathrm N
\end{aligned}
$$

**(c) Trọng lượng theo pound và khối lượng theo kilôgam của con mèo:**

Đổi trọng lượng sang pound:
$$
w_3 = \frac{45\,\mathrm N}{4{,}448\,\mathrm{N/lb}} \approx 10{,}1\,\mathrm{lb}
$$
Khối lượng của con mèo theo kilôgam:
$$
m_3 = \frac{45}{9{,}80} \approx 4{,}59\,\mathrm{kg}
$$

Kết luận:
- Bọ chét nặng $2{,}06 \times 10^{-6}\,\mathrm N$.
- Rầy bọt nặng $1{,}21 \times 10^{-4}\,\mathrm N$.
- Mèo nhà nặng $10{,}1\,\mathrm{lb}$ và có khối lượng $4{,}59\,\mathrm{kg}$.

</details>

---

### 4.19: Trọng lượng của quả dưa hấu trên mặt trăng Io của Sao Mộc

*Độ khó: Mức 1.*

Trên bề mặt mặt trăng Io của Sao Mộc, gia tốc do trọng lực là $g_{\mathrm{Io}} = 1{,}81\,\mathrm{m/s^2}$. Một quả dưa hấu có trọng lượng $44{,}0\,\mathrm N$ trên bề mặt Trái Đất.
(a) Khối lượng của quả dưa hấu trên bề mặt Trái Đất bằng bao nhiêu?
(b) Khối lượng và trọng lượng của quả dưa hấu trên bề mặt mặt trăng Io sẽ bằng bao nhiêu?

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Gia tốc trọng trường trên Io: $g_{\mathrm{Io}} = 1{,}81\,\mathrm{m/s^2}$.
- Trọng lượng quả dưa hấu trên Trái Đất: $w_E = 44{,}0\,\mathrm N$, $g_E = 9{,}80\,\mathrm{m/s^2}$.
- Cần tìm: Khối lượng $m$ trên Trái Đất, khối lượng $m$ và trọng lượng $w_{\mathrm{Io}}$ trên Io.

**Hướng đi:**
- Xác định khối lượng quả dưa hấu từ trọng lượng của nó trên Trái Đất: $m = w_E / g_E$.
- Khối lượng là thuộc tính bất biến, không đổi khi di chuyển giữa các thiên thể.
- Tính trọng lượng trên Io bằng công thức: $w_{\mathrm{Io}} = m g_{\mathrm{Io}}$.

**Lời giải chi tiết:**

**(a) Khối lượng của quả dưa hấu trên bề mặt Trái Đất:**
$$
m = \frac{44{,}0}{9{,}80} \approx 4{,}49\,\mathrm{kg}
$$

**(b) Khối lượng và trọng lượng trên mặt trăng Io:**

Khối lượng của quả dưa hấu không phụ thuộc vào vị trí trong vũ trụ, do đó trên bề mặt Io khối lượng vẫn là:
$$
m \approx 4{,}49\,\mathrm{kg}
$$
Trọng lượng của quả dưa hấu trên bề mặt Io là:
$$
\begin{aligned}
w_{\mathrm{Io}} &= m g_{\mathrm{Io}} \\
&= 4{,}4898(1{,}81) \approx 8{,}13\,\mathrm N
\end{aligned}
$$

Kết luận: Khối lượng trên Trái Đất là $4{,}49\,\mathrm{kg}$. Trên bề mặt Io, khối lượng vẫn là $4{,}49\,\mathrm{kg}$ và trọng lượng là $8{,}13\,\mathrm N$.

</details>

---

## Mục 4.5: Định luật III Newton

### 4.20: Ước lượng khối lượng võ sĩ Sumo

*Độ khó: Mức 1.*

Hãy ước tính khối lượng theo kilôgam và trọng lượng theo pound của một võ sĩ Sumo điển hình. Các ước tính này so với ước tính về khối lượng và trọng lượng trung bình của sinh viên trong lớp học của bạn như thế nào? Liệt kê các giá trị bạn giả định trong bài giải.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Ước tính khối lượng ($m$) và trọng lượng ($w$) của một võ sĩ Sumo.
- So sánh với các giá trị trung bình của sinh viên trong lớp.

**Hướng đi:**
- Chọn thử một võ sĩ có khối lượng $155\,\mathrm{kg}$ để làm ước lượng. Đây là giả thiết, không phải một giá trị trung bình thống kê.
- Để so sánh, giả sử một sinh viên có khối lượng $65\,\mathrm{kg}$. Muốn tính cho lớp thực tế, cần dùng số đo của chính lớp đó.
- Áp dụng các hệ số chuyển đổi: $1\,\mathrm{kg}$ có trọng lượng khoảng $2{,}203\,\mathrm{lb}$ trên Trái Đất ($1\,\mathrm{lb} \approx 4{,}448\,\mathrm N$).

**Lời giải chi tiết:**

1. **Ước tính đối với võ sĩ Sumo:**
- Khối lượng giả định: $m_{\mathrm{sumo}} \approx 155\,\mathrm{kg}$.
- Trọng lượng theo đơn vị SI:
$$
w_{\mathrm{sumo}} = 155(9{,}80) \approx 1520\,\mathrm N
$$
- Trọng lượng theo pound:
$$
\begin{aligned}w_{\mathrm{sumo}}&\approx155(2{,}203)\\
&\approx341\,\mathrm{lb}.\end{aligned}
$$

2. **Ước tính đối với sinh viên trung bình:**
- Khối lượng giả định: $m_{\mathrm{sv}} \approx 65\,\mathrm{kg}$.
- Trọng lượng theo pound:
$$
w_{\mathrm{sv, lb}} \approx 65(2{,}203) \approx 143\,\mathrm{lb}
$$

3. **So sánh:**
Tỷ số khối lượng giữa võ sĩ Sumo và sinh viên:
$$
\frac{m_{\mathrm{sumo}}}{m_{\mathrm{sv}}} = \frac{155\,\mathrm{kg}}{65\,\mathrm{kg}} \approx 2{,}4
$$
Với hai khối lượng đã giả định, võ sĩ nặng gấp khoảng $2{,}4$ lần sinh viên được dùng làm mốc so sánh.

</details>

---

### 4.21: Xuất phát của vận động viên chạy nước rút

*Độ khó: Mức 1. Ứng dụng sinh học (BIO).*

Các vận động viên chạy nước rút đẳng cấp thế giới có thể bứt tốc rời bàn đạp xuất phát với gia tốc gần như nằm ngang có độ lớn lên tới $15\,\mathrm{m/s^2}$. Một vận động viên có khối lượng $55\,\mathrm{kg}$ phải tác dụng một lực nằm ngang bằng bao nhiêu lên bàn đạp xuất phát để tạo ra gia tốc này? Vật nào tác dụng lực trực tiếp đẩy vận động viên tiến về phía trước: bàn đạp hay chính bản thân vận động viên?

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Khối lượng vận động viên: $m = 55\,\mathrm{kg}$.
- Gia tốc nằm ngang: $a = 15\,\mathrm{m/s^2}$.
- Cần tìm: Lực tác dụng lên bàn đạp xuất phát và xác định vật tác dụng lực đẩy vận động viên.

**Hướng đi:**
- Để tạo ra gia tốc $a$ cho vận động viên, hợp lực nằm ngang tác dụng lên cơ thể vận động viên phải thỏa mãn định luật II Newton: $\sum F = ma$.
- Theo định luật III Newton, lực do vận động viên tác dụng lên bàn đạp và phản lực do bàn đạp tác dụng lên bàn chân vận động viên tạo thành một cặp lực trực đối, có cùng độ lớn.
- Một vật thể không thể tự tác dụng ngoại lực lên chính nó để gia tốc khối tâm; lực đẩy vận động viên tiến về phía trước bắt buộc phải là ngoại lực do bàn đạp tác dụng lên vận động viên.

**Lời giải chi tiết:**

1. **Tính độ lớn của lực:**

Theo định luật II Newton, hợp lực tác dụng lên vận động viên để tạo ra gia tốc $15\,\mathrm{m/s^2}$ là:
$$
F_{\mathrm{net}} = ma = 55(15) = 825\,\mathrm N
$$
Theo định luật III Newton, lực mà vận động viên tác dụng lên bàn đạp xuất phát có độ lớn đúng bằng lực mà bàn đạp đẩy lại vận động viên:
$$
F_{\mathrm{vđv \rightarrow bàn đạp}} = 825\,\mathrm N
$$

2. **Xác định vật tạo ra lực đẩy:**

Bản thân vận động viên không thể tự tạo ra ngoại lực để đẩy chính mình. Khi cơ bắp chân co duỗi, bàn chân vận động viên đạp mạnh lùi về phía sau vào bàn đạp xuất phát. Theo định luật III Newton, chính **bàn đạp xuất phát** tác dụng phản lực pháp tuyến hướng về phía trước lên bàn chân vận động viên, và ngoại lực này là nguyên nhân duy nhất đẩy vận động viên lao về phía trước.

Kết luận: Lực tác dụng lên bàn đạp có độ lớn $825\,\mathrm N$, và bàn đạp chính là vật tác dụng lực đẩy vận động viên.

</details>

---

### 4.22: Ô tô đẩy xe tải chết máy

*Độ khó: Mức 1.*

Một chiếc ô tô con có khối lượng $380\,\mathrm{kg}$ đang đẩy một chiếc xe tải lớn có khối lượng $900\,\mathrm{kg}$ di chuyển về hướng Đông trên một đoạn đường bằng phẳng nằm ngang. Chiếc ô tô tác dụng một lực nằm ngang có độ lớn $1600\,\mathrm N$ lên xe tải. Hỏi độ lớn của lực mà xe tải tác dụng ngược lại lên chiếc ô tô bằng bao nhiêu?

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Khối lượng ô tô: $m_1 = 380\,\mathrm{kg}$.
- Khối lượng xe tải: $m_2 = 900\,\mathrm{kg}$.
- Lực ô tô tác dụng lên xe tải: $F_{12} = 1600\,\mathrm N$ (hướng Đông).
- Cần tìm: Độ lớn lực mà xe tải tác dụng lên ô tô ($F_{21}$).

**Hướng đi:**
- Nhận diện bản chất tương tác giữa hai vật tiếp xúc.
- Áp dụng định luật III Newton: Cặp lực tương tác giữa ô tô và xe tải luôn có độ lớn bằng nhau, không phụ thuộc vào trạng thái chuyển động (đứng yên, chuyển động đều hay chuyển động có gia tốc) và không phụ thuộc vào khối lượng của từng vật.

**Lời giải chi tiết:**

Theo định luật III Newton: Khi vật A (ô tô) tác dụng một lực lên vật B (xe tải), thì vật B cũng đồng thời tác dụng trở lại vật A một lực có cùng độ lớn nhưng ngược hướng:
$$
\vec F_{21} = -\vec F_{12}
$$
Do đó, độ lớn của lực mà xe tải tác dụng lên ô tô đúng bằng độ lớn lực mà ô tô tác dụng lên xe tải:
$$
F_{21} = F_{12} = 1600\,\mathrm N
$$
Lực này hướng về phía Tây (ngược chiều với hướng chuyển động).

Kết luận: Độ lớn của lực mà xe tải tác dụng lên ô tô là $1600\,\mathrm N$.

</details>

---

### 4.23: Hai khối hộp tiếp xúc trên mặt sàn nằm ngang

*Độ khó: Mức 2.*

Hai chiếc hộp A và B tiếp xúc nhau trên một mặt phẳng nằm ngang không có ma sát (Hình E4.23). Hộp A có khối lượng $20{,}0\,\mathrm{kg}$ và hộp B có khối lượng $5{,}0\,\mathrm{kg}$. Một lực nằm ngang có độ lớn $250\,\mathrm N$ được tác dụng vào hộp A. Hỏi độ lớn của lực mà hộp A tác dụng lên hộp B bằng bao nhiêu?

![Hình E4.23: Hai khối hộp tiếp xúc chịu lực đẩy nằm ngang.](/vat-ly-1/bai-giang/img/young-04/r-exercises-e4-23.png)

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Khối lượng hộp A: $m_A = 20{,}0\,\mathrm{kg}$.
- Khối lượng hộp B: $m_B = 5{,}0\,\mathrm{kg}$.
- Lực đẩy tác dụng vào A: $F = 250\,\mathrm N$.
- Mặt sàn không có ma sát.
- Cần tìm: Lực tiếp xúc $F_{AB}$ do hộp A tác dụng lên hộp B.

**Hướng đi:**
- Xem hai hộp A và B như một hệ thống liên kết chuyển động cùng gia tốc $a$. Áp dụng định luật II Newton cho toàn hệ để tìm gia tốc chung: $a = F / (m_A + m_B)$.
- Tách riêng hộp B: Theo phương ngang, hộp B chỉ chịu tác dụng của một lực duy nhất là lực đẩy do hộp A tác dụng qua mặt tiếp xúc ($F_{AB}$).
- Áp dụng định luật II Newton cho hộp B: $F_{AB} = m_B a$.

**Lời giải chi tiết:**

1. **Gia tốc của hệ hai hộp:**

Tổng khối lượng của cả hai hộp là:
$$
M = 20{,}0 + 5{,}0 = 25{,}0\,\mathrm{kg}
$$
Áp dụng định luật II Newton cho toàn bộ hệ chuyển động theo phương ngang:
$$
a = \frac{250}{25{,}0} = 10{,}0\,\mathrm{m/s^2}
$$

2. **Lực do hộp A tác dụng lên hộp B:**

Xét riêng hộp B: Theo phương nằm ngang, lực duy nhất tác dụng lên hộp B là lực nén tiếp xúc từ hộp A, ký hiệu là $F_{AB}$. Áp dụng định luật II Newton cho hộp B:
$$
\begin{aligned}
F_{AB} &= m_B a \\
&= 5{,}0(10{,}0) = 50\,\mathrm N
\end{aligned}
$$

Kết luận: Độ lớn của lực mà hộp A tác dụng lên hộp B là $50\,\mathrm N$.

</details>

---

### 4.24: Phản lực pháp tuyến và gia tốc của hành khách trong thang máy

*Độ khó: Mức 2.*

Lực nâng pháp tuyến do sàn thang máy tác dụng lên một hành khách nặng $650\,\mathrm N$ có độ lớn bằng $620\,\mathrm N$.
(a) Các phản lực đối ứng (reaction forces) theo định luật III Newton của hai lực này là những lực nào?
(b) Hành khách này có đang chuyển động có gia tốc hay không? Nếu có, hãy tìm độ lớn và hướng của gia tốc đó.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Trọng lượng hành khách: $w = 650\,\mathrm N$.
- Phản lực nâng pháp tuyến từ sàn: $n = 620\,\mathrm N$.
- Cần tìm: Cặp lực trực đối theo định luật III Newton, xác định trạng thái gia tốc, tính độ lớn và hướng của gia tốc.

**Hướng đi:**
- Định luật III Newton: Nếu vật 1 tác dụng lên vật 2 một lực, thì phản lực đối ứng là lực do vật 2 tác dụng ngược lại lên vật 1 (cùng độ lớn, ngược chiều, khác vật tác dụng).
- Áp dụng định luật II Newton cho hành khách: $\sum F_y = n - w = m a_y$. Nếu $\sum F_y \ne 0$ thì hành khách có gia tốc.
- Tìm khối lượng $m = w / g$ và giải ra $a_y$.

**Lời giải chi tiết:**

**(a) Các phản lực đối ứng theo định luật III Newton:**

1. **Đối với trọng lực $w = 650\,\mathrm N$:**
Đây là lực hấp dẫn do Trái Đất tác dụng kéo hành khách xuống dưới. Phản lực đối ứng theo định luật III Newton là **lực hấp dẫn do hành khách tác dụng hút Trái Đất lên trên**, có độ lớn đúng bằng $650\,\mathrm N$ và điểm đặt tại tâm Trái Đất.

2. **Đối với lực nâng pháp tuyến $n = 620\,\mathrm N$:**
Đây là lực tiếp xúc do sàn thang máy tác dụng đẩy bàn chân hành khách lên trên. Phản lực đối ứng theo định luật III Newton là **lực nén do bàn chân hành khách tác dụng ép xuống sàn thang máy**, có độ lớn đúng bằng $620\,\mathrm N$ và hướng thẳng đứng xuống dưới đặt vào sàn thang máy.

**(b) Gia tốc của hành khách:**

Khối lượng của hành khách:
$$
m = \frac{650}{9{,}80} \approx 66{,}33\,\mathrm{kg}
$$
Chọn trục $Oy$ thẳng đứng hướng lên trên. Hợp lực tác dụng lên hành khách là:
$$
\sum F_y = 620 - 650 = -30\,\mathrm N
$$
Vì hợp lực khác không, hành khách **chắc chắn đang chuyển động có gia tốc**.
Áp dụng định luật II Newton:
$$
a_y = \frac{-30}{66{,}33} \approx -0{,}452\,\mathrm{m/s^2}
$$
Dấu âm chỉ ra rằng vector gia tốc hướng thẳng đứng xuống dưới.

Kết luận: Hành khách đang gia tốc hướng xuống dưới với độ lớn gia tốc xấp xỉ $0{,}452\,\mathrm{m/s^2}$.

</details>

---

### 4.25: Trái Đất gia tốc về phía người nhảy cầu

*Độ khó: Mức 2.*

Một học sinh có khối lượng $45\,\mathrm{kg}$ nhảy từ một ván nhảy cầu trên cao xuống nước. Gia tốc của Trái Đất tiến về phía cô bé bằng bao nhiêu khi cô bé đang rơi tự do về phía Trái Đất với gia tốc $9{,}8\,\mathrm{m/s^2}$? Sử dụng giá trị khối lượng của Trái Đất là $6{,}0 \times 10^{24}\,\mathrm{kg}$, và giả sử hợp lực duy nhất tác dụng lên Trái Đất là lực hấp dẫn do cô bé tác dụng lên nó.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Khối lượng học sinh: $m = 45\,\mathrm{kg}$.
- Gia tốc rơi của học sinh: $g = 9{,}8\,\mathrm{m/s^2}$.
- Khối lượng Trái Đất: $M = 6{,}0 \times 10^{24}\,\mathrm{kg}$.
- Cần tìm: Gia tốc của Trái Đất $a_{\mathrm{Earth}}$.

**Hướng đi:**
- Tính độ lớn lực hấp dẫn do Trái Đất tác dụng lên học sinh: $F = mg$.
- Theo định luật III Newton, lực hấp dẫn do học sinh tác dụng lên Trái Đất có cùng độ lớn $F$.
- Áp dụng định luật II Newton cho Trái Đất: $a_{\mathrm{Earth}} = F / M$.

**Lời giải chi tiết:**

Độ lớn lực hấp dẫn giữa học sinh và Trái Đất là:
$$
F = mg = 45(9{,}8) = 441\,\mathrm N
$$
Theo định luật III Newton, cô bé cũng tác dụng lên Trái Đất một lực hút ngược lại có độ lớn đúng bằng $441\,\mathrm N$ hướng thẳng đứng lên trên về phía cô bé.

Áp dụng định luật II Newton cho Trái Đất:
$$
\begin{aligned}
a_{\mathrm{Earth}} &= \frac{F}{M} \\
&= \frac{441}{6{,}0 \times 10^{24}} \\
&\approx 7{,}4 \times 10^{-23}\,\mathrm{m/s^2}
\end{aligned}
$$

Kết luận: Gia tốc của Trái Đất tiến về phía học sinh là $7{,}4 \times 10^{-23}\,\mathrm{m/s^2}$.

</details>

---

## Mục 4.6: Sơ đồ lực

### 4.26: Sơ đồ lực cho hai khối hộp xếp chồng

*Độ khó: Mức 2.*

Bạn dùng tay kéo nằm ngang một lực lên khối hộp B trên Hình E4.26, làm cho cả hai khối hộp chuyển động cùng nhau như một khối thống nhất sang bên phải. Đối với hệ chuyển động này, hãy vẽ sơ đồ lực có chú thích cẩn thận cho khối hộp A nếu:
(a) Mặt bàn hoàn toàn không có ma sát.
(b) Có ma sát giữa khối B và mặt bàn, và lực kéo của tay có độ lớn đúng bằng độ lớn lực ma sát do mặt bàn tác dụng lên khối B.

![Hình E4.26: Khối hộp A xếp chồng lên trên khối hộp B được kéo trên bàn.](/vat-ly-1/bai-giang/img/young-04/parent-ex-hinh-e4-26.png)

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Khối hộp A nằm trên khối hộp B, cả hai cùng chuyển động sang phải.
- Câu hỏi: Vẽ sơ đồ lực cho khối A trong hai trường hợp: (a) bàn không ma sát; (b) có ma sát bàn-B và lực kéo cân bằng với lực ma sát này.

**Hướng đi:**
- Xác định trạng thái gia tốc của hệ hai vật trong từng trường hợp.
- Trường hợp (a): Không có ma sát bàn, lực kéo gây ra gia tốc $a > 0$ sang phải cho toàn hệ. Khối A muốn gia tốc sang phải thì phải có hợp lực nằm ngang hướng sang phải tác dụng lên nó, đó chính là lực ma sát nghỉ do mặt trên khối B tác dụng.
- Trường hợp (b): Lực kéo cân bằng với lực ma sát của bàn, nên hợp lực tác dụng lên toàn hệ bằng không. Hệ chuyển động thẳng đều với gia tốc $a = 0$. Theo định luật I Newton, hợp lực tác dụng lên khối A phải bằng không, do đó không xuất hiện lực ma sát giữa A và B theo phương ngang.

**Lời giải chi tiết:**

![Sơ đồ lực trong lời giải 4.26.](/vat-ly-1/bai-giang/img/young-04/parent-solution-4-26.svg)

**(a) Trường hợp mặt bàn không có ma sát:**

Lực kéo $\vec F$ hướng sang phải tác dụng lên khối B. Vì mặt bàn không có ma sát, toàn bộ hệ (A + B) chuyển động nhanh dần đều sang phải với gia tốc:
$$
a = \frac{F}{m_A + m_B} > 0
$$
Để khối A có thể tăng tốc sang phải với cùng gia tốc $a$ mà không bị trượt lại phía sau, bề mặt tiếp xúc của khối B phải tác dụng một lực ma sát nghỉ $\vec f_s$ hướng sang phải lên khối A.

Các lực tác dụng lên khối hộp A gồm:
1. **Trọng lực $\vec w_A$:** Do Trái Đất tác dụng, hướng thẳng đứng xuống dưới, độ lớn $w_A = m_A g$.
2. **Phản lực pháp tuyến $\vec n_{BA}$:** Do mặt trên của khối B tác dụng nâng khối A, hướng thẳng đứng lên trên, cân bằng với trọng lượng ($n_{BA} = w_A$).
3. **Lực ma sát nghỉ $\vec f_{s, BA}$:** Do mặt trên của khối B tác dụng lên đáy khối A, hướng nằm ngang sang bên phải, tạo ra gia tốc cho khối A ($f_s = m_A a$).

**(b) Trường hợp lực kéo cân bằng với lực ma sát của mặt bàn:**

Theo giả thiết, lực kéo có độ lớn bằng lực ma sát do mặt bàn tác dụng lên khối B ($F = f_{\mathrm{bàn}}$). Hợp lực tác dụng lên toàn hệ hai khối bằng không:
$$
\sum F_{\mathrm{hệ}, x} = F - f_{\mathrm{bàn}} = 0
$$
Do đó, hệ hai khối chuyển động thẳng đều sang bên phải với gia tốc bằng không ($a = 0$).
Theo định luật II (hoặc định luật I) Newton áp dụng cho riêng khối A:
$$
\sum \vec F_A = m_A \vec a = 0
$$
Vì gia tốc bằng không, hợp lực theo phương nằm ngang tác dụng lên khối A bắt buộc phải bằng không. Do không có lực nào khác tác dụng lên A theo phương ngang để kéo nó giật lùi, lực ma sát nghỉ giữa A và B lúc này phải bằng không ($f_s = 0$).

Các lực tác dụng lên khối hộp A chỉ gồm hai lực theo phương thẳng đứng:
1. **Trọng lực $\vec w_A$:** Hướng thẳng đứng xuống dưới.
2. **Phản lực pháp tuyến $\vec n_{BA}$:** Hướng thẳng đứng lên trên, có độ lớn bằng đúng trọng lượng ($n_{BA} = w_A$).

</details>

---

### 4.27: Hai kiện hàng đặt cạnh nhau trên sàn không ma sát

*Độ khó: Mức 2.*

Hai kiện hàng A và B nằm yên cạnh nhau trên một bề mặt nằm ngang không có ma sát. Chúng có khối lượng lần lượt là $m_A$ và $m_B$. Khi một lực nằm ngang $\vec F$ được tác dụng vào kiện hàng A đẩy sang phải, cả hai kiện hàng cùng chuyển động sang phải.
(a) Vẽ sơ đồ lực có chú thích rõ ràng cho kiện hàng A và kiện hàng B. Chỉ ra những cặp lực nào (nếu có) là cặp lực trực đối theo định luật III Newton.
(b) Nếu độ lớn của lực $\vec F$ nhỏ hơn tổng trọng lượng của hai kiện hàng, liệu lực này có làm cho hai kiện hàng chuyển động được hay không? Hãy giải thích.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Kiện hàng A ($m_A$) và B ($m_B$) đặt kề nhau trên sàn không ma sát.
- Lực nằm ngang $\vec F$ đẩy A sang phải.
- Câu hỏi: (a) Vẽ sơ đồ lực cho A và B, xác định cặp lực trực đối định luật III; (b) Lực $F < w_A + w_B$ có làm vật chuyển động không?

**Hướng đi:**
- Liệt kê mọi ngoại lực tác dụng lên từng kiện hàng.
- Tìm cặp lực tương tác giữa hai bề mặt tiếp xúc của A và B.
- Xem xét bản chất chuyển động trên mặt sàn không ma sát: Trọng lực tác dụng theo phương thẳng đứng và được phản lực pháp tuyến từ sàn cân bằng hoàn toàn. Lực theo phương nằm ngang quyết định chuyển động ngang.

**Lời giải chi tiết:**

![Sơ đồ lực trong lời giải 4.27.](/vat-ly-1/bai-giang/img/young-04/parent-solution-4-27.svg)

Trong hình, $C$ là độ lớn lực tiếp xúc giữa hai kiện, tương ứng với độ lớn của $F_{AB}$ và $F_{BA}$. Các mũi tên minh họa phương và chiều lực, không theo tỷ lệ độ lớn.

**(a) Sơ đồ lực và cặp lực trực đối định luật III Newton:**

1. **Các lực tác dụng lên kiện hàng A:**
- Trọng lực $\vec w_A$: Do Trái Đất tác dụng, hướng thẳng đứng xuống dưới.
- Phản lực pháp tuyến $\vec n_A$: Do mặt sàn tác dụng, hướng thẳng đứng lên trên ($n_A = w_A$).
- Lực đẩy tác dụng $\vec F$: Hướng nằm ngang sang phải.
- Lực tiếp xúc $\vec F_{BA}$: Do kiện hàng B tác dụng cản lại kiện hàng A, hướng nằm ngang sang trái.

2. **Các lực tác dụng lên kiện hàng B:**
- Trọng lực $\vec w_B$: Do Trái Đất tác dụng, hướng thẳng đứng xuống dưới.
- Phản lực pháp tuyến $\vec n_B$: Do mặt sàn tác dụng, hướng thẳng đứng lên trên ($n_B = w_B$).
- Lực tiếp xúc $\vec F_{AB}$: Do kiện hàng A tác dụng đẩy kiện hàng B, hướng nằm ngang sang phải.

3. **Cặp lực trực đối theo định luật III Newton:**
Cặp lực $\vec F_{AB}$ (lực do A đẩy B) và $\vec F_{BA}$ (lực do B cản A) là cặp lực trực đối theo định luật III Newton:
$$
\vec F_{BA} = -\vec F_{AB}
$$
Chúng có cùng độ lớn, ngược hướng và tác dụng lên hai vật thể khác nhau.

**(b) Lực $F$ nhỏ hơn tổng trọng lượng có làm vật chuyển động không?**

Có. Lực khác không làm hai kiện hàng có gia tốc sang phải.
Lý do: Bề mặt sàn hoàn toàn không có ma sát, đồng nghĩa với việc không có bất kỳ lực cản nào chống lại chuyển động theo phương nằm ngang. Trọng lượng của hai kiện hàng hướng thẳng đứng xuống dưới và đã bị các phản lực pháp tuyến từ mặt sàn cân bằng triệt để theo phương thẳng đứng ($\sum F_y = 0$).

Theo định luật II Newton cho phương nằm ngang:
$$
\sum F_x = (m_A + m_B) a
$$
Bất kỳ một lực nằm ngang $F>0$ nào, dù nhỏ đến đâu và dù nhỏ hơn nhiều so với trọng lượng, đều sẽ truyền cho hệ một gia tốc dương và làm cho hai kiện hàng chuyển động ngay lập tức.

</details>

---

### 4.28: Viên đạn súng trường găm vào thân cây

*Độ khó: Mức 2. Tổng hợp kiến thức trước (CP).*

Một viên đạn súng trường cỡ .22 bay với tốc độ $350\,\mathrm{m/s}$ cắm vào một thân cây lớn và xuyên sâu vào trong gỗ một đoạn $0{,}130\,\mathrm m$ trước khi dừng lại. Khối lượng của viên đạn là $1{,}80\,\mathrm g$. Giả sử lực cản của gỗ là không đổi.
(a) Cần khoảng thời gian bao lâu để viên đạn dừng lại hoàn toàn?
(b) Thân cây tác dụng một lực cản bằng bao nhiêu newton lên viên đạn?

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Khối lượng viên đạn: Đổi $1{,}80\,\mathrm g$ thành $1{,}80\times10^{-3}\,\mathrm{kg}$.
- Vận tốc ban đầu: $v_{0x} = 350\,\mathrm{m/s}$.
- Vận tốc cuối: $v_x = 0$.
- Độ sâu xuyên vào gỗ: $d = 0{,}130\,\mathrm m$.
- Lực cản không đổi.
- Cần tìm: Thời gian hãm $t$ và độ lớn lực cản $F_{\mathrm{cản}}$.

**Hướng đi:**
- Chuyển động hãm trong thân cây là chuyển động thẳng biến đổi đều với gia tốc âm.
- Áp dụng công thức liên hệ giữa quãng đường và vận tốc trung bình: $d = \frac{v_{0x} + v_x}{2} t$ để tính thời gian dừng $t$.
- Áp dụng hệ thức độc lập thời gian $v_x^2 - v_{0x}^2 = 2 a_x d$ để tính gia tốc hãm $a_x$.
- Áp dụng định luật II Newton để tính lực cản: $F_{\mathrm{cản}} = m |a_x|$.

**Lời giải chi tiết:**

**(a) Thời gian để viên đạn dừng lại:**

Theo công thức chuyển động biến đổi đều:
$$
d = \left(\frac{v_{0x} + v_x}{2}\right) t
$$
Thay số với $v_{0x} = 350\,\mathrm{m/s}$ và $v_x = 0$:
$$
0{,}130 = \left(\frac{350}{2}\right) t = 175 t
$$
Suy ra thời gian hãm dừng:
$$
\begin{aligned}
t &= \frac{0{,}130}{175} \\
&\approx 7{,}43 \times 10^{-4}\,\mathrm s = 0{,}743\,\mathrm{ms}
\end{aligned}
$$

**(b) Lực cản do thân cây tác dụng lên viên đạn:**

Gia tốc của viên đạn trong thân cây là:
$$
v_x^2 - v_{0x}^2 = 2 a_x d
$$
$$
0 - 350^2 = 2 a_x (0{,}130)
$$
$$
\begin{aligned}
0{,}260 a_x &= -122500 \\
a_x &\approx -4{,}71 \times 10^5\,\mathrm{m/s^2}
\end{aligned}
$$
Áp dụng định luật II Newton, độ lớn lực cản do thân cây tác dụng là:
$$
\begin{aligned}
F_{\mathrm{cản}} &= m |a_x| \\
&=(1{,}80)(4{,}712)\times10^2 \\
&\approx 848\,\mathrm N
\end{aligned}
$$

Kết luận: Thời gian dừng của viên đạn là $7{,}43 \times 10^{-4}\,\mathrm s$, và thân cây tác dụng một lực cản có độ lớn $848\,\mathrm N$ ngược chiều chuyển động.

</details>

---

### 4.29: Quả cầu treo trên trần toa tàu hỏa

*Độ khó: Mức 1.*

Một quả cầu nhỏ được treo bằng một sợi dây dài gắn vào trần của một toa tàu hỏa đang chạy về hướng Đông trên đường ray nằm ngang. Một người quan sát bên trong toa tàu thấy quả cầu nằm yên bất động so với toa tàu. Hãy vẽ sơ đồ lực có chú thích rõ ràng cho quả cầu nếu:
(a) Con tàu chuyển động thẳng đều với vận tốc không đổi.
(b) Con tàu đang tăng tốc đều về phía trước.
Trong mỗi trường hợp, hợp lực tác dụng lên quả cầu có bằng không hay không? Hãy giải thích.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Quả cầu treo bằng dây trên trần toa tàu đang chạy về hướng Đông.
- Câu hỏi: Vẽ sơ đồ lực và xét hợp lực khi (a) tàu chạy thẳng đều; (b) tàu tăng tốc đều về hướng Đông.

**Hướng đi:**
- Phân tích chuyển động trong hệ quy chiếu quán tính gắn với mặt đất:
  - Nếu tàu chuyển động thẳng đều ($a = 0$), quả cầu cũng chuyển động thẳng đều với cùng vận tốc ($a = 0$).
  - Nếu tàu tăng tốc về hướng Đông với gia tốc $a > 0$, quả cầu cũng phải có gia tốc $a > 0$ hướng về phía Đông để đứng yên so với toa tàu.
- Áp dụng định luật II Newton $\sum \vec F = m \vec a$ để biện luận về phương của sợi dây và độ lớn hợp lực.

**Lời giải chi tiết:**

![Sơ đồ lực trong lời giải 4.29.](/vat-ly-1/bai-giang/img/young-04/parent-solution-4-29.svg)

**(a) Trường hợp tàu chạy thẳng đều với vận tốc không đổi ($a = 0$):**

Vì con tàu chuyển động thẳng đều, gia tốc của nó bằng không. Quả cầu đứng yên so với toa tàu nên gia tốc của quả cầu đối với mặt đất cũng bằng không:
$$
\vec a = 0
$$
Theo định luật I Newton, hợp lực tác dụng lên quả cầu phải bằng không:
$$
\sum \vec F = \vec T + \vec w = 0
$$
Sợi dây treo giữ phương thẳng đứng hoàn toàn.

Các lực tác dụng lên quả cầu gồm:
1. **Trọng lực $\vec w$:** Hướng thẳng đứng xuống dưới.
2. **Lực căng dây $\vec T$:** Hướng thẳng đứng lên trên, có độ lớn bằng đúng trọng lượng ($T = w$).

Hợp lực tác dụng lên quả cầu trong trường hợp này **bằng không** ($\sum \vec F = 0$).

**(b) Trường hợp tàu tăng tốc đều về hướng Đông ($a > 0$):**

Để quả cầu giữ nguyên vị trí tương đối đứng yên so với toa tàu, quả cầu bắt buộc phải có cùng gia tốc $\vec a$ hướng về phía Đông đối với mặt đất. Theo định luật II Newton:
$$
\sum \vec F = m \vec a \ne 0
$$
Vì gia tốc hướng về phía Đông, hợp lực tác dụng lên quả cầu **không thể bằng không** mà phải là một vector có hướng sang phía Đông.

Để tạo ra thành phần lực hướng sang phía Đông, sợi dây treo không còn thẳng đứng nữa mà bị nghiêng về phía sau (hướng Tây) một góc $\theta$ so với phương thẳng đứng:
1. **Trọng lực $\vec w$:** Hướng thẳng đứng xuống dưới.
2. **Lực căng dây $\vec T$:** Hướng dọc theo sợi dây (chếch lên trên và hướng về phía Đông).
- Thành phần thẳng đứng cân bằng với trọng lượng: $T \cos\theta = mg$.
- Thành phần nằm ngang hướng về phía Đông tạo ra gia tốc cho quả cầu: $T \sin\theta = ma$.

Hợp lực tác dụng lên quả cầu trong trường hợp này **khác không** (bằng $ma$, hướng sang phía Đông).

Kết luận: Hợp lực bằng không ở trường hợp (a), và khác không ở trường hợp (b).

</details>

---

### 4.30: Đẩy chiếc ghế trượt trên sàn nhà

*Độ khó: Mức 2.*

Một chiếc ghế có khối lượng $12{,}0\,\mathrm{kg}$ đặt trên mặt sàn nằm ngang; mặt sàn này không nhẵn (có ma sát). Bạn dùng tay đẩy chiếc ghế bằng một lực $F = 40{,}0\,\mathrm N$ hướng chếch xuống dưới một góc $37{,}0^\circ$ so với phương nằm ngang, làm cho chiếc ghế trượt dọc theo mặt sàn.
(a) Hãy vẽ sơ đồ lực có chú thích rõ ràng cho chiếc ghế.
(b) Sử dụng sơ đồ lực vừa vẽ và các định luật Newton để tính lực nâng pháp tuyến mà mặt sàn tác dụng lên chiếc ghế.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Khối lượng chiếc ghế: $m = 12{,}0\,\mathrm{kg}$.
- Lực đẩy của tay: $F = 40{,}0\,\mathrm N$, hướng xuống hợp góc $\theta = 37{,}0^\circ$ dưới phương ngang.
- Chiếc ghế trượt trên sàn có ma sát.
- Cần tìm: Sơ đồ lực và phản lực pháp tuyến $n$ do sàn tác dụng lên ghế.

**Hướng đi:**
- Xác định tất cả các lực tác dụng lên chiếc ghế: Trọng lực, phản lực pháp tuyến từ sàn, lực đẩy của tay, và lực ma sát trượt.
- Chiếu các lực lên trục thẳng đứng $Oy$ (chọn chiều dương hướng lên).
- Vì chiếc ghế chỉ trượt trên mặt sàn nằm ngang mà không bị nhấc bổng hay lún sâu vào sàn, gia tốc theo phương thẳng đứng bằng không ($a_y = 0$).
- Thiết lập phương trình cân bằng theo phương $y$: $\sum F_y = 0$, từ đó tính ra phản lực pháp tuyến $n$.

**Lời giải chi tiết:**

![Sơ đồ lực trong lời giải 4.30.](/vat-ly-1/bai-giang/img/young-04/parent-solution-4-30.svg)

**(a) Sơ đồ lực cho chiếc ghế:**

Các lực tác dụng lên chiếc ghế gồm bốn lực:
1. **Trọng lực $\vec w$:** Do Trái Đất tác dụng, hướng thẳng đứng xuống dưới:
$$
\begin{aligned}w&=mg\\
&=12{,}0(9{,}80)\\
&=117{,}6\,\mathrm N.\end{aligned}
$$
2. **Lực đẩy của tay $\vec F$:** Hướng chếch xuống dưới sang phải một góc $37{,}0^\circ$ so với phương ngang.
3. **Phản lực pháp tuyến $\vec n$:** Do mặt sàn tác dụng lên chân ghế, hướng thẳng đứng lên trên.
4. **Lực ma sát trượt $\vec f_k$:** Do mặt sàn tác dụng lên chân ghế, hướng nằm ngang sang trái (ngược chiều chuyển động trượt).

**(b) Tính lực nâng pháp tuyến của mặt sàn:**

Chọn trục tọa độ $Oy$ thẳng đứng hướng lên trên. Phân tích lực đẩy $\vec F$ thành hai thành phần:
- Thành phần nằm ngang: $F_x = F \cos(37{,}0^\circ)$.
- Thành phần thẳng đứng hướng xuống: $F_y = -F \sin(37{,}0^\circ)$.

Vì chiếc ghế duy trì tiếp xúc phẳng với mặt sàn, gia tốc thẳng đứng $a_y = 0$. Áp dụng định luật II Newton theo phương thẳng đứng:
$$
\begin{aligned}n-w-F\sin37^\circ&=0.\end{aligned}
$$
Suy ra biểu thức của lực nâng pháp tuyến:
$$
n = w + F \sin(37{,}0^\circ)
$$
Thay số vào phương trình:
$$
\begin{aligned}
n &= 117{,}6 + 40{,}0\sin(37{,}0^\circ) \\
&= 117{,}6 + 24{,}07 \approx 142\,\mathrm N
\end{aligned}
$$

Kết luận: Phản lực pháp tuyến do mặt sàn tác dụng lên chiếc ghế là $142\,\mathrm N$.

</details>
