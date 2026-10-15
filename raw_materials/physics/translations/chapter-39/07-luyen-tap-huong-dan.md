## Luyện tập hướng dẫn

Trong phần này, các hằng số vật lý cơ bản được sử dụng bao gồm:

- Hằng số Planck: $h = 6{,}626\times 10^{-34}\,\mathrm{J\cdot s}$, $\hbar = h/(2\pi) \approx 1{,}055\times 10^{-34}\,\mathrm{J\cdot s}$.
- Tốc độ ánh sáng trong chân không: $c = 2{,}998\times 10^8\,\mathrm{m/s}$.
- Độ lớn điện tích nguyên tố: $e = 1{,}602\times 10^{-19}\,\mathrm C$.
- Khối lượng nghỉ: $m_e = 9{,}109\times 10^{-31}\,\mathrm{kg}$, $m_p = 1{,}673\times 10^{-27}\,\mathrm{kg}$.
- Hằng số Stefan–Boltzmann: $\sigma = 5{,}6704\times 10^{-8}\,\mathrm{W/(m^2\cdot K^4)}$.
- Hằng số dịch chuyển Wien: $b = 2{,}898\times 10^{-3}\,\mathrm{m\cdot K}$.
- Hằng số Boltzmann: $k_{\mathrm B} = 1{,}381\times 10^{-23}\,\mathrm{J/K}$.
- Tích số: $hc \approx 1239{,}84\,\mathrm{eV\cdot nm}$.

### Sóng hạt và nhiễu xạ electron

::: exercise VP39.2.1. Bước sóng de Broglie và cực đại nhiễu xạ electron

Trong một thí nghiệm nhiễu xạ electron, khoảng cách giữa các nguyên tử trong bia tinh thể là $0{,}172\,\mathrm{nm}$. Chùm electron có động năng ban đầu không đáng kể trước khi được gia tốc bởi hiệu điện thế $69{,}0\,\mathrm V$. Hãy tìm (a) bước sóng de Broglie của mỗi electron, và (b) góc tán xạ nhỏ nhất xuất hiện cực đại trong hình ảnh nhiễu xạ.

:::

::: solution Lời giải chi tiết

**Tóm tắt đề bài:** Khoảng cách giữa các nguyên tử $d=0{,}172\,\mathrm{nm}$, hiệu điện thế gia tốc $V_0=69{,}0\,\mathrm V$, động năng ban đầu $K_0\approx0$.

**Hướng đi:**

- Động năng electron nhận được bằng công của lực điện trường: $K=eV_0$. Vì $eV_0=69{,}0\,\mathrm{eV}\ll m_e c^2\approx511\,\mathrm{keV}$, ta áp dụng cơ học phi tương đối tính.
- Bước sóng de Broglie tính theo công thức $\lambda=h/p=h/\sqrt{2m_e eV_0}$.
- Cực đại nhiễu xạ từ mạng phẳng tuần hoàn tuân theo điều kiện giao thoa tăng cường: $d\sin\theta=m\lambda$. Góc tán xạ nhỏ nhất tương ứng với bậc nhiễu xạ $m=1$.

(a) Động năng của electron sau khi tăng tốc qua hiệu điện thế $V_0=69{,}0\,\mathrm V$ là $K=eV_0\approx1{,}105\times10^{-17}\,\mathrm J$. Bước sóng de Broglie của mỗi electron bằng

$$
\begin{aligned}
\lambda &= \frac{h}{\sqrt{2m_e eV_0}} \\
&\approx 0{,}148\,\mathrm{nm}.
\end{aligned}
$$

(b) Cực đại giao thoa bậc một ($m=1$) xuất hiện tại góc tán xạ $\theta$ thỏa mãn

$$
\begin{aligned}
\sin\theta &= \frac{\lambda}{d} \\
&= \frac{0{,}148\,\mathrm{nm}}{0{,}172\,\mathrm{nm}} \\
&\approx 0{,}8593.
\end{aligned}
$$

Suy ra góc tán xạ nhỏ nhất là

$$
\begin{aligned}
\theta &= \arcsin(0{,}8593) \\
&\approx 59{,}1^\circ.
\end{aligned}
$$

:::

::: exercise VP39.2.2. Tìm khoảng cách nguyên tử từ hình ảnh nhiễu xạ

Cực đại cường độ bậc $m=1$ trong thí nghiệm nhiễu xạ electron xuất hiện tại góc tán xạ $48{,}0^\circ$. Hiệu điện thế gia tốc chùm electron là $36{,}5\,\mathrm V$. Hãy tìm (a) động năng của mỗi electron theo joule, (b) bước sóng de Broglie của electron, và (c) khoảng cách giữa các nguyên tử trong bia tinh thể.

:::

::: solution Lời giải chi tiết

**Tóm tắt đề bài:** Bậc cực đại $m=1$, góc tán xạ $\theta=48{,}0^\circ$, hiệu điện thế gia tốc $V_0=36{,}5\,\mathrm V$.

**Hướng đi:**

- Công lực điện trường chuyển hóa trọn vẹn thành động năng: $K=eV_0$.
- Động lượng electron liên hệ với động năng qua $p=\sqrt{2m_e K}$, từ đó suy ra bước sóng de Broglie $\lambda=h/p$.
- Vị trí cực đại nhiễu xạ bậc $m$ xác định theo hệ thức giao thoa bề mặt: $d\sin\theta=m\lambda$, cho phép suy ngược ra khoảng cách mạng $d$.

(a) Với $e = 1{,}602\times10^{-19}\,\mathrm C$ và $V_0 = 36{,}5\,\mathrm V$, động năng của mỗi electron sau khi tăng tốc là

$$
\begin{aligned}
K &= eV_0 \\
&\approx 5{,}85\times10^{-18}\,\mathrm J.
\end{aligned}
$$

(b) Bước sóng de Broglie của electron là

$$
\begin{aligned}
\lambda &= \frac{h}{\sqrt{2m_e K}} \\
&\approx 0{,}203\,\mathrm{nm}.
\end{aligned}
$$

(c) Khoảng cách giữa các nguyên tử trong bia tinh thể được tính từ điều kiện cực đại bậc một:

$$
\begin{aligned}
d &= \frac{m\lambda}{\sin\theta} \\
&= \frac{1\times0{,}2031\,\mathrm{nm}}{\sin 48{,}0^\circ} \\
&\approx 0{,}273\,\mathrm{nm}.
\end{aligned}
$$

:::

::: exercise VP39.2.3. Điều khiển điện áp để tạo cực đại nhiễu xạ mong muốn

Sử dụng bia tinh thể có khoảng cách nguyên tử là $0{,}218\,\mathrm{nm}$, người ta muốn tạo ra hình ảnh nhiễu xạ electron sao cho cực đại bậc $m=2$ xuất hiện chính xác tại góc tán xạ $75{,}0^\circ$. Hãy xác định (a) bước sóng de Broglie cần thiết của chùm electron, và (b) hiệu điện thế gia tốc yêu cầu.

:::

::: solution Lời giải chi tiết

**Tóm tắt đề bài:** Khoảng cách mạng $d=0{,}218\,\mathrm{nm}$, bậc cực đại $m=2$, góc cực đại $\theta=75{,}0^\circ$.

**Hướng đi:**

- Từ điều kiện giao thoa $d\sin\theta=m\lambda$, tính trực tiếp bước sóng de Broglie yêu cầu $\lambda$.
- Từ bước sóng de Broglie $\lambda=h/\sqrt{2m_e eV_0}$, đảo công thức để tìm hiệu điện thế gia tốc $V_0$.

(a) Bước sóng de Broglie cần thiết thỏa mãn điều kiện cực đại bậc hai:

$$
\begin{aligned}
\lambda &= \frac{d\sin\theta}{m} \\
&= \frac{(0{,}218\,\mathrm{nm})\sin 75{,}0^\circ}{2} \\
&\approx 0{,}105\,\mathrm{nm}.
\end{aligned}
$$

(b) Hiệu điện thế gia tốc cần đặt vào là

$$
\begin{aligned}
V_0 &= \frac{h^2}{2m_e e\lambda^2} \\
&\approx 136\,\mathrm V.
\end{aligned}
$$

:::

::: exercise VP39.2.4. Bước sóng de Broglie của proton được gia tốc

Một proton có điện tích $e$ và khối lượng $m_p=1{,}67\times10^{-27}\,\mathrm{kg}$ được gia tốc từ trạng thái nghỉ đến tốc độ $2{,}38\times10^5\,\mathrm{m/s}$. Hãy tìm (a) bước sóng de Broglie của proton, và (b) hiệu điện thế gia tốc đã sử dụng.

:::

::: solution Lời giải chi tiết

**Tóm tắt đề bài:** Khối lượng proton $m_p=1{,}67\times10^{-27}\,\mathrm{kg}$, tốc độ đạt được $v=2{,}38\times10^5\,\mathrm{m/s}$.

**Hướng đi:**

- Tốc độ $v\approx2{,}38\times10^5\,\mathrm{m/s}\ll c$ nên động lượng tính theo cơ học cổ điển: $p=m_p v$.
- Bước sóng de Broglie suy ra từ hệ thức de Broglie: $\lambda=h/p$.
- Định lý động năng cho hạt mang điện tích $e$ tăng tốc từ trạng thái nghỉ: $eV_0=\frac{1}{2}m_p v^2$, suy ra $V_0$.

(a) Động lượng của proton được tính theo

$$
\begin{aligned}
p &= m_p v \\
&\approx 3{,}975\times10^{-22}\,\mathrm{kg\,m/s}.
\end{aligned}
$$

Bước sóng de Broglie tương ứng bằng

$$
\begin{aligned}
\lambda &= \frac{h}{p} \\
&\approx 1{,}67\times10^{-12}\,\mathrm m.
\end{aligned}
$$

(b) Động năng của proton theo joule là

$$
\begin{aligned}
K &= \frac{1}{2}m_p v^2 \\
&\approx 4{,}729\times10^{-17}\,\mathrm J.
\end{aligned}
$$

Hiệu điện thế gia tốc cần dùng để truyền vận tốc trên cho proton là

$$
\begin{aligned}
V_0 &= \frac{K}{e} \\
&\approx 295\,\mathrm V.
\end{aligned}
$$

:::

### Các mức năng lượng và mẫu nguyên tử Bohr

::: exercise VP39.6.1. Phổ phát xạ của nguyên tử giả định ba mức

Một nguyên tử giả định có ba mức năng lượng lần lượt tại $0{,}00\,\mathrm{eV}$, $2{,}00\,\mathrm{eV}$ và $5{,}00\,\mathrm{eV}$. Nếu nguyên tử ban đầu ở mức kích thích $5{,}00\,\mathrm{eV}$, hãy tìm tất cả các bước sóng mà nguyên tử có thể phát ra trong quá trình trở về trạng thái cơ bản.

:::

::: solution Lời giải chi tiết

**Tóm tắt đề bài:** Các mức năng lượng $E_0=0{,}00\,\mathrm{eV}$, $E_1=2{,}00\,\mathrm{eV}$, $E_2=5{,}00\,\mathrm{eV}$. Trạng thái ban đầu là $E_2$.

**Hướng đi:**

- Định đề Bohr về phát xạ: Khi chuyển từ mức năng lượng cao $E_i$ xuống mức thấp $E_f$, nguyên tử phát ra một photon có năng lượng $E_{\mathrm{ph}}=E_i-E_f$.
- Bước sóng photon phát ra liên hệ với độ chênh năng lượng qua $\lambda=hc/E_{\mathrm{ph}}$.
- Liệt kê toàn bộ các bước chuyển khả dĩ từ mức kích thích cao nhất về trạng thái cơ bản (gồm cả chuyển dời trực tiếp và chuyển dời từng nấc).

Từ trạng thái kích thích $E_2=5{,}00\,\mathrm{eV}$, nguyên tử có thể chuyển trực tiếp về trạng thái cơ bản, hoặc chuyển nấc qua trạng thái trung gian $E_1=2{,}00\,\mathrm{eV}$:

- Chuyển dời từ $E_2$ về $E_1$: Độ chênh năng lượng là $\Delta E_{21}=3{,}00\,\mathrm{eV}$. Bước sóng photon phát ra bằng

$$
\begin{aligned}
\lambda_{21} &= \frac{hc}{\Delta E_{21}} \\
&\approx \frac{1239{,}84\,\mathrm{eV\,nm}}{3{,}00\,\mathrm{eV}} \\
&\approx 414\,\mathrm{nm}.
\end{aligned}
$$

- Chuyển dời tiếp theo từ $E_1$ về $E_0$: Độ chênh năng lượng là $\Delta E_{10}=2{,}00\,\mathrm{eV}$. Bước sóng tương ứng là

$$
\begin{aligned}
\lambda_{10} &= \frac{hc}{\Delta E_{10}} \\
&\approx \frac{1239{,}84\,\mathrm{eV\,nm}}{2{,}00\,\mathrm{eV}} \\
&\approx 620\,\mathrm{nm}.
\end{aligned}
$$

- Chuyển dời trực tiếp từ $E_2$ về $E_0$: Độ chênh năng lượng là $\Delta E_{20}=5{,}00\,\mathrm{eV}$. Bước sóng phát xạ là

$$
\begin{aligned}
\lambda_{20} &= \frac{hc}{\Delta E_{20}} \\
&\approx \frac{1239{,}84\,\mathrm{eV\,nm}}{5{,}00\,\mathrm{eV}} \\
&\approx 248\,\mathrm{nm}.
\end{aligned}
$$

Như vậy, các bước sóng khả dĩ mà nguyên tử có thể phát ra gồm $248\,\mathrm{nm}$, $414\,\mathrm{nm}$ và $620\,\mathrm{nm}$.

:::

::: exercise VP39.6.2. Xác định các mức kích thích từ bước sóng phổ

Một nguyên tử giả định phát ra một photon bước sóng $674\,\mathrm{nm}$ khi chuyển từ mức kích thích thứ hai xuống mức kích thích thứ nhất, và phát ra một photon bước sóng $385\,\mathrm{nm}$ khi chuyển từ mức kích thích thứ nhất về trạng thái cơ bản. Hãy tìm (a) năng lượng của mức kích thích thứ nhất và thứ hai so với trạng thái cơ bản, và (b) bước sóng của photon phát ra khi nguyên tử chuyển thẳng từ mức kích thích thứ hai về trạng thái cơ bản.

:::

::: solution Lời giải chi tiết

**Tóm tắt đề bài:** Bước sóng chuyển dời $\lambda_{21}=674\,\mathrm{nm}$ và $\lambda_{10}=385\,\mathrm{nm}$. Chọn mốc năng lượng trạng thái cơ bản $E_0=0$.

**Hướng đi:**

- Năng lượng của mỗi photon phát ra bằng hiệu mức năng lượng giữa hai trạng thái: $\Delta E=hc/\lambda$.
- Mức kích thích thứ nhất có năng lượng $E_1=\Delta E_{10}$. Mức kích thích thứ hai có năng lượng $E_2=E_1+\Delta E_{21}$.
- Khi chuyển trực tiếp từ mức hai về mức cơ bản, năng lượng photon phát ra là $E_2-E_0=E_2$, từ đó tính bước sóng tương ứng $\lambda_{20}=hc/E_2$.

(a) Năng lượng photon phát ra khi chuyển từ mức kích thích thứ nhất về trạng thái cơ bản là

$$
\begin{aligned}
\Delta E_{10} &= \frac{hc}{\lambda_{10}} \\
&\approx \frac{1239{,}84\,\mathrm{eV\,nm}}{385\,\mathrm{nm}} \\
&\approx 3{,}22\,\mathrm{eV}.
\end{aligned}
$$

Do đó năng lượng của mức kích thích thứ nhất so với trạng thái cơ bản là $E_1=3{,}22\,\mathrm{eV}$. Năng lượng photon phát ra ở bước chuyển từ mức hai xuống mức một là

$$
\begin{aligned}
\Delta E_{21} &= \frac{hc}{\lambda_{21}} \\
&\approx \frac{1239{,}84\,\mathrm{eV\,nm}}{674\,\mathrm{nm}} \\
&\approx 1{,}84\,\mathrm{eV}.
\end{aligned}
$$

Năng lượng của mức kích thích thứ hai so với trạng thái cơ bản bằng

$$
\begin{aligned}
E_2 &= E_1 + \Delta E_{21} \\
&= 3{,}22\,\mathrm{eV} + 1{,}84\,\mathrm{eV} \\
&= 5{,}06\,\mathrm{eV}.
\end{aligned}
$$

(b) Bước sóng của photon phát ra khi nguyên tử chuyển thẳng từ mức hai về trạng thái cơ bản là

$$
\begin{aligned}
\lambda_{20} &= \frac{hc}{E_2-E_0} \\
&\approx \frac{1239{,}84\,\mathrm{eV\,nm}}{5{,}06\,\mathrm{eV}} \\
&\approx 245\,\mathrm{nm}.
\end{aligned}
$$

:::

::: exercise VP39.6.3. Năng lượng và bước sóng các vạch phổ hiđrô

Hãy tính năng lượng và bước sóng của photon phát ra bởi nguyên tử hiđrô khi thực hiện các bước chuyển: (a) từ mức $n=5$ xuống mức $n=3$, (b) từ mức $n=4$ xuống mức $n=2$, và (c) từ mức $n=3$ xuống mức $n=1$.

:::

::: solution Lời giải chi tiết

**Tóm tắt đề bài:** Nguyên tử hiđrô chuyển mức lượng tử giữa các cặp $(n_i, n_f)$: $(5, 3)$, $(4, 2)$, $(3, 1)$.

**Hướng đi:**

- Trong mẫu Bohr cho nguyên tử hiđrô, mức năng lượng lượng tử hóa xác định theo công thức $E_n=-13{,}60\,\mathrm{eV}/n^2$.
- Năng lượng photon phát ra bằng độ chênh năng lượng:

$$
\Delta E = E_i - E_f.
$$

- Bước sóng photon tính theo công thức $\lambda=hc/\Delta E$.

(a) Đối với bước chuyển từ $n=5$ xuống $n=3$ (thuộc dãy Paschen):

$$
\begin{aligned}
\Delta E &= 13{,}60\,\mathrm{eV}\left(\frac{1}{9}-\frac{1}{25}\right) \\
&= 13{,}60\,\mathrm{eV}\times\frac{16}{225} \\
&\approx 0{,}967\,\mathrm{eV}.
\end{aligned}
$$

Bước sóng photon phát ra là

$$
\begin{aligned}
\lambda &= \frac{hc}{\Delta E} \\
&\approx \frac{1239{,}84\,\mathrm{eV\,nm}}{0{,}9671\,\mathrm{eV}} \\
&\approx 1282\,\mathrm{nm} \\
&\approx 1{,}28\,\mu\mathrm m.
\end{aligned}
$$

Bức xạ này nằm trong vùng hồng ngoại.

(b) Đối với bước chuyển từ $n=4$ xuống $n=2$ (vạch $\mathrm H_\beta$ thuộc dãy Balmer):

$$
\begin{aligned}
\Delta E &= 13{,}60\,\mathrm{eV}\left(\frac{1}{4}-\frac{1}{16}\right) \\
&= 13{,}60\,\mathrm{eV}\times\frac{3}{16} \\
&\approx 2{,}55\,\mathrm{eV}.
\end{aligned}
$$

Bước sóng photon phát ra là

$$
\begin{aligned}
\lambda &= \frac{hc}{\Delta E} \\
&\approx \frac{1239{,}84\,\mathrm{eV\,nm}}{2{,}550\,\mathrm{eV}} \\
&\approx 486\,\mathrm{nm}.
\end{aligned}
$$

Vạch phổ này nằm trong vùng ánh sáng nhìn thấy (màu lam-chàm).

(c) Đối với bước chuyển từ $n=3$ xuống $n=1$ (thuộc dãy Lyman):

$$
\begin{aligned}
\Delta E &= 13{,}60\,\mathrm{eV}\left(1-\frac{1}{9}\right) \\
&= 13{,}60\,\mathrm{eV}\times\frac{8}{9} \\
&\approx 12{,}1\,\mathrm{eV}.
\end{aligned}
$$

Bước sóng photon phát ra là

$$
\begin{aligned}
\lambda &= \frac{hc}{\Delta E} \\
&\approx \frac{1239{,}84\,\mathrm{eV\,nm}}{12{,}089\,\mathrm{eV}} \\
&\approx 103\,\mathrm{nm}.
\end{aligned}
$$

Vạch phổ này nằm trong vùng tử ngoại.

:::

::: exercise VP39.6.4. Động năng, thế năng và bước sóng hấp thụ theo mẫu Bohr

Một nguyên tử hiđrô chuyển từ mức năng lượng $n=2$ lên mức $n=6$. Theo mẫu nguyên tử Bohr, hãy tìm (a) độ biến thiên động năng của electron, (b) độ biến thiên thế năng tĩnh điện, và (c) bước sóng của photon mà nguyên tử đã hấp thụ để thực hiện bước chuyển này.

:::

::: solution Lời giải chi tiết

**Tóm tắt đề bài:** Nguyên tử hiđrô chuyển dời từ trạng thái ban đầu $n=2$ lên trạng thái kích thích $n=6$.

**Hướng đi:**

- Trong quỹ đạo dừng Bohr bán kính $r_n$, lực Coulomb đóng vai trò lực hướng tâm kéo theo định lý virian: $K_n=-E_n=+13{,}60\,\mathrm{eV}/n^2$ và $U_n=2E_n=-27{,}20\,\mathrm{eV}/n^2$.
- Độ biến thiên động năng $\Delta K=K_6-K_2$ và thế năng $\Delta U=U_6-U_2$.
- Năng lượng photon bị hấp thụ bằng tổng năng lượng thu vào: $E_{\mathrm{ph}}=\Delta E=\Delta K+\Delta U$. Bước sóng hấp thụ tính qua $\lambda=hc/E_{\mathrm{ph}}$.

(a) Động năng của electron tại quỹ đạo $n$ là $K_n=13{,}60\,\mathrm{eV}/n^2$. Khi chuyển từ $n=2$ lên $n=6$, bán kính quỹ đạo tăng lên làm electron chuyển động chậm lại, độ biến thiên động năng bằng

$$
\begin{aligned}
\Delta K &= K_6 - K_2 \\
&= 0{,}378\,\mathrm{eV} - 3{,}40\,\mathrm{eV} \\
&\approx -3{,}02\,\mathrm{eV}.
\end{aligned}
$$

(b) Thế năng tĩnh điện giữa electron và hạt nhân tại quỹ đạo $n$ là $U_n=-27{,}20\,\mathrm{eV}/n^2$. Độ biến thiên thế năng bằng

$$
\begin{aligned}
\Delta U &= U_6 - U_2 \\
&\approx +6{,}04\,\mathrm{eV}.
\end{aligned}
$$

Thế năng tăng gấp đôi độ giảm của động năng, phù hợp với định lý virian của lực thế tỉ lệ nghịch với bình phương khoảng cách.

(c) Tổng năng lượng mà nguyên tử hấp thụ từ photon là

$$
\begin{aligned}
E_{\mathrm{ph}} &= \Delta K+\Delta U \\
&= (-3{,}02 + 6{,}04)\,\mathrm{eV} \\
&\approx 3{,}02\,\mathrm{eV}.
\end{aligned}
$$

Bước sóng của photon bị hấp thụ bằng

$$
\begin{aligned}
\lambda &= \frac{hc}{E_{\mathrm{ph}}} \\
&\approx \frac{1239{,}84\,\mathrm{eV\,nm}}{3{,}022\,\mathrm{eV}} \\
&\approx 411\,\mathrm{nm}.
\end{aligned}
$$

:::

### Bức xạ vật đen và định luật dịch chuyển Wien

::: exercise VP39.8.1. Nhiệt độ và bức xạ của sao Betelgeuse

Ngôi sao Betelgeuse có nhiệt độ bề mặt là $3590\,\mathrm K$ và có thể coi gần đúng như một vật đen tuyệt đối. (a) Hãy tìm bước sóng mà tại đó Betelgeuse phát xạ mạnh nhất. Bước sóng này nằm trong vùng ánh sáng nhìn thấy, tử ngoại hay hồng ngoại? (b) Tính công suất phát xạ trên một đơn vị diện tích bề mặt của ngôi sao này.

:::

::: solution Lời giải chi tiết

**Tóm tắt đề bài:** Nhiệt độ bề mặt Betelgeuse $T=3590\,\mathrm K$, hệ số phát xạ $e=1$.

**Hướng đi:**

- Bước sóng có mật độ thông lượng phát xạ cực đại $\lambda_{\mathrm m}$ xác định theo định luật dịch chuyển Wien: $\lambda_{\mathrm m}T=b$, với hằng số $b\approx2{,}898\times10^{-3}\,\mathrm{m\,K}$.
- So sánh bước sóng thu được với thang sóng điện từ để xác định vùng phổ.
- Cường độ phát xạ toàn phần (công suất trên một đơn vị diện tích) tuân theo định luật Stefan–Boltzmann: $I=\sigma T^4$.

(a) Theo định luật dịch chuyển Wien, bước sóng phát xạ mạnh nhất là

$$
\begin{aligned}
\lambda_{\mathrm m} &= \frac{b}{T} \\
&= \frac{2{,}898\times10^{-3}\,\mathrm{m\,K}}{3590\,\mathrm K} \\
&\approx 808\,\mathrm{nm}.
\end{aligned}
$$

Vì bước sóng này lớn hơn ranh giới đỏ của vùng ánh sáng nhìn thấy ($750\,\mathrm{nm}$), bức xạ cực đại của Betelgeuse thuộc vùng hồng ngoại gần.

(b) Cường độ bức xạ toàn phần trên mỗi mét vuông bề mặt ngôi sao là

$$
\begin{aligned}
I &= \sigma T^4 \\
&\approx 9{,}42\times10^6\,\mathrm{W/m^2} \\
&= 9{,}42\,\mathrm{MW/m^2}.
\end{aligned}
$$

:::

::: exercise VP39.8.2. Suy ra nhiệt độ vật đen từ cường độ bức xạ

Cường độ bức xạ toàn phần phát ra từ một vật đen tuyệt đối là $78{,}0\,\mathrm{MW/m^2}$. Hãy tìm (a) nhiệt độ của vật đen, (b) bước sóng mà tại đó vật đen phát xạ mạnh nhất, và (c) cho biết bước sóng ở phần (b) thuộc vùng nhìn thấy, tử ngoại hay hồng ngoại.

:::

::: solution Lời giải chi tiết

**Tóm tắt đề bài:** Cường độ phát xạ $I=78{,}0\,\mathrm{MW/m^2}=7{,}80\times10^7\,\mathrm{W/m^2}$.

**Hướng đi:**

- Từ định luật Stefan–Boltzmann $I=\sigma T^4$, ta tính trực tiếp nhiệt độ tuyệt đối $T=(I/\sigma)^{1/4}$.
- Dùng định luật Wien $\lambda_{\mathrm m}=b/T$ để xác định bước sóng có cường độ phát xạ đỉnh.
- Đối chiếu giá trị bước sóng với các vùng của phổ sóng điện từ.

(a) Nhiệt độ của vật đen là

$$
\begin{aligned}
T &= \left(\frac{I}{\sigma}\right)^{1/4} \\
&\approx 6{,}09\times10^3\,\mathrm K.
\end{aligned}
$$

(b) Bước sóng phát xạ mạnh nhất là

$$
\begin{aligned}
\lambda_{\mathrm m} &= \frac{b}{T} \\
&\approx \frac{2{,}898\times10^{-3}\,\mathrm{m\,K}}{6088\,\mathrm K} \\
&\approx 476\,\mathrm{nm}.
\end{aligned}
$$

(c) Bước sóng $476\,\mathrm{nm}$ nằm hoàn toàn trong dải phổ ánh sáng nhìn thấy (tương ứng với màu lam).

:::

::: exercise VP39.8.3. Nhiệt độ và công suất phát xạ của sao Rigel A

Đường cong phân bố phát xạ phổ của sao Rigel A xấp xỉ rất tốt dạng đường cong của một vật đen tuyệt đối. Đỉnh phát xạ của đường cong này nằm tại bước sóng $239\,\mathrm{nm}$. Hãy tìm (a) nhiệt độ bề mặt của Rigel A, và (b) công suất mà Rigel A bức xạ trên mỗi đơn vị diện tích bề mặt.

:::

::: solution Lời giải chi tiết

**Tóm tắt đề bài:** Bước sóng cực đại $\lambda_{\mathrm m}=239\,\mathrm{nm}=2{,}39\times10^{-7}\,\mathrm m$.

**Hướng đi:**

- Áp dụng định luật Wien $T=b/\lambda_{\mathrm m}$ để tính nhiệt độ bề mặt.
- Áp dụng định luật Stefan–Boltzmann $I=\sigma T^4$ để tính năng lượng phát xạ trên một đơn vị diện tích trong một giây.

(a) Nhiệt độ bề mặt của ngôi sao là

$$
\begin{aligned}
T &= \frac{b}{\lambda_{\mathrm m}} \\
&\approx \frac{2{,}898\times10^{-3}\,\mathrm{m\,K}}{2{,}39\times10^{-7}\,\mathrm m} \\
&\approx 1{,}21\times10^4\,\mathrm K.
\end{aligned}
$$

(b) Công suất bức xạ trên một đơn vị diện tích bề mặt Rigel A là

$$
\begin{aligned}
I &= \sigma T^4 \\
&\approx 1{,}23\times10^9\,\mathrm{W/m^2}.
\end{aligned}
$$

:::

::: exercise VP39.8.4. Phát xạ của sao Proxima Centauri trong dải hẹp

Proxima Centauri, ngôi sao gần Mặt Trời nhất, có nhiệt độ bề mặt là $3040\,\mathrm K$. Hãy xác định (a) bước sóng mà tại đó ngôi sao này phát xạ mạnh nhất, và (b) công suất mà ngôi sao này bức xạ trên một mét vuông bề mặt trong một dải bước sóng hẹp có độ rộng $12{,}0\,\mathrm{nm}$ đối xứng quanh bước sóng ở phần (a).

:::

::: solution Lời giải chi tiết

**Tóm tắt đề bài:** Nhiệt độ bề mặt $T=3040\,\mathrm K$, độ rộng dải phổ $\Delta\lambda=12{,}0\,\mathrm{nm}$ quanh đỉnh $\lambda_{\mathrm m}$.

**Hướng đi:**

- Tính bước sóng cực đại $\lambda_{\mathrm m}$ theo định luật dịch chuyển Wien $\lambda_{\mathrm m}=b/T$.
- Trong dải bước sóng rất hẹp $\Delta\lambda\ll\lambda_{\mathrm m}$, công suất bức xạ trên một đơn vị diện tích được tính bằng tích của mật độ phát xạ phổ Planck $I(\lambda_{\mathrm m})$ với độ rộng dải: $\Delta I\approx I(\lambda_{\mathrm m})\Delta\lambda$.
- Công thức hàm phân bố phổ Planck theo bước sóng: $I(\lambda)=\frac{2\pi hc^2}{\lambda^5 [e^{hc/(\lambda k_{\mathrm B} T)}-1]}$.

(a) Bước sóng phát xạ mạnh nhất của Proxima Centauri là

$$
\begin{aligned}
\lambda_{\mathrm m} &= \frac{b}{T} \\
&\approx \frac{2{,}898\times10^{-3}\,\mathrm{m\,K}}{3040\,\mathrm K} \\
&\approx 954\,\mathrm{nm}.
\end{aligned}
$$

Bước sóng này nằm trong vùng hồng ngoại gần.

(b) Đặt số mũ không thứ nguyên trong phân bố Planck tại bước sóng đỉnh:

$$
\begin{aligned}
x &= \frac{hc}{\lambda_{\mathrm m} k_{\mathrm B} T} \\
&= \frac{hc}{b k_{\mathrm B}} \\
&\approx 4{,}9651.
\end{aligned}
$$

Giá trị của thừa số mẫu số là $e^{4{,}9651}-1\approx142{,}32$. Mật độ phát xạ phổ tại đỉnh đạt giá trị

$$
I(\lambda_{\mathrm m}) = \frac{2\pi hc^2}{\lambda_{\mathrm m}^5 (e^x - 1)}
$$

$$
I(\lambda_{\mathrm m}) \approx 3{,}34\times10^{12}\,\mathrm{W/m^3}.
$$

Công suất bức xạ trên mỗi mét vuông trong dải $\Delta\lambda=12{,}0\,\mathrm{nm}$ là

$$
\begin{aligned}
\Delta I &\approx I(\lambda_{\mathrm m})\Delta\lambda \\
&\approx 4{,}01\times10^4\,\mathrm{W/m^2} \\
&= 40{,}1\,\mathrm{kW/m^2}.
\end{aligned}
$$

:::
