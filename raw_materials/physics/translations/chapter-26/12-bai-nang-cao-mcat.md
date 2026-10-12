<!-- Source: Challenge Problems 26.81–26.85 and MCAT-Style Passage Problems 26.86–26.88, printed pages 876–877, PDF pages 896–897. -->

## Bài tập nâng cao 26.81–26.88

### Bài tập thử thách

::: exercise 26.81
Thiết bị ba cực trong Hình P26.81 là transistor NPN. Nó tuân theo ba quy tắc: Tổng dòng đi vào bằng tổng dòng đi ra, $I_C+I_B=I_E$. Điện thế tại $e$ luôn thấp hơn điện thế tại $b$ là $0{,}60\,\mathrm{V}$. Dòng đi vào cực $c$ bằng $\beta$ lần dòng đi vào cực $b$, tức $I_C=\beta I_B$, với $\beta\gg1$. (a) Tìm $V_{out}$ theo $V_{in}$ khi $\beta\to\infty$. (b) Cần $V_{in}$ bằng bao nhiêu để $V_{out}=7{,}5\,\mathrm{V}$? (c) Nếu $V_{in}=15{,}0\,\mathrm{V}+v_{in}(t)$ và $V_{out}=7{,}5\,\mathrm{V}+Gv_{in}(t)$, tìm hệ số khuếch đại $G$.
:::

![Mạch transistor của bài 26.81](img/young-26/hinh-p26-81.png)

<!-- detailed-solution:26.81 -->
::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Điện trở emitter là $100\,\Omega$, điện trở collector là $1{,}00\,\mathrm{k\Omega}$, nguồn collector là $15{,}0\,\mathrm{V}$ và $V_e=V_{in}-0{,}60\,\mathrm{V}$.

**Hướng đi:**

- Từ điện trở emitter tìm $I_E$. Khi $\beta$ rất lớn, $I_B\to0$ và $I_C\approx I_E$. Sau đó dùng điện trở collector tìm $V_{out}$.
- Dùng quy tắc dòng để liên hệ $I_C$ với $I_E$, rồi lấy đạo hàm $dV_{out}/dV_{in}$ cho tín hiệu nhỏ.

$$
\begin{aligned}
I_E&=\frac{V_{in}-0{,}60}{100\,\Omega},\\
V_{out}&=15{,}0\,\mathrm{V}-(1{,}00\,\mathrm{k\Omega})I_E\\
&=21{,}0\,\mathrm{V}-10V_{in}.
\end{aligned}
$$

(b) Đặt $V_{out}=7{,}5\,\mathrm{V}$ được $V_{in}=1{,}35\,\mathrm{V}$. (c) Độ dốc của quan hệ truyền là $G=-10$. Dấu âm cho biết tín hiệu ra đảo pha. Tuy nhiên, số hạng một chiều $V_{in}=15{,}0\,\mathrm{V}$ trong đề không tương thích với mô hình ở (a): Công thức cho $V_{out}=-129\,\mathrm{V}$, ngoài miền nguồn $0$–$15\,\mathrm{V}$. Mức ra một chiều $7{,}5\,\mathrm{V}$ đòi hỏi $V_{in}=1{,}35\,\mathrm{V}$. Hệ số khuếch đại vi sai theo quy tắc lý tưởng vẫn là $-10$.
:::

::: exercise 26.82
Trong mạch Hình P26.82, công tắc $S$ đã đóng từ lâu. (a) Tìm điện áp ra $V_{out}$. Sau đó mở công tắc để điện áp ra tăng. Khi điện áp đạt $10{,}0\,\mathrm{V}$, đóng công tắc khiến tụ phóng điện. Khi điện áp còn $5{,}0\,\mathrm{V}$, mở công tắc lại. Chu trình lặp tuần hoàn. (b) Tìm hằng số thời gian khi nạp. (c) Tìm hằng số thời gian khi phóng. (d) Tìm thời gian giữa hai lần điện áp đạt $10{,}0\,\mathrm{V}$. (e) Nếu $R=10{,}0\,\mathrm{k\Omega}$ và $C=10{,}0\,\mathrm{\mu F}$, tìm tần số hoạt động.
:::

![Mạch định thời RC của bài 26.82](img/young-26/hinh-p26-82.png)

<!-- detailed-solution:26.82 -->
::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Nguồn là $15\,\mathrm{V}$. Nhánh nạp có điện trở $4R$. Khi đóng công tắc, điện trở $R$ mắc từ đầu ra xuống đất và tụ phóng qua tải $R$ song song với nhánh nguồn đã triệt tiêu.

**Hướng đi:**

- Dùng điện trở Thévenin nhìn từ tụ ở mỗi trạng thái công tắc. Tính thời gian nạp từ $5$ lên $10\,\mathrm{V}$ và thời gian phóng từ $10$ xuống $5\,\mathrm{V}$ rồi cộng lại.
- Đoạn nạp tiến tới $15\,\mathrm{V}$, còn đoạn phóng tiến tới điện áp chia áp khi công tắc đóng.

(a) Khi đóng lâu, đầu ra là điện áp chia trên $R$ và $4R$, nên $V_{out}=15R/(5R)=3{,}00\,\mathrm{V}$.

$$
\begin{aligned}
\tau_{nạp}&=4RC,\\
\tau_{phóng}&=(R\parallel4R)C=\frac45RC.
\end{aligned}
$$

Trong pha nạp, $V_C=15-(15-5)e^{-t/(4RC)}$. Do đó $t_n=4RC\ln2$. Trong pha phóng, $V_C=3+(10-3)e^{-t/[(4/5)RC]}$, nên $t_p=(4/5)RC\ln(7/2)$.

$$
T=RC\left(4\ln2+\frac45\ln\frac72\right).
$$

Với $RC=0{,}100\,\mathrm{s}$, ta có $t_n=0{,}277\,\mathrm{s}$, $t_p=0{,}100\,\mathrm{s}$, $T=0{,}377\,\mathrm{s}$ và $f=1/T=2{,}65\,\mathrm{Hz}$.
:::

::: exercise 26.83
**Mạng vô hạn.** Mạng điện trở trong Hình P26.83 gồm các điện trở $R_1$ nối dọc hai thanh và các điện trở ngang $R_2$, kéo dài vô hạn về bên phải. Chứng minh điện trở toàn phần $R_T$ là

$$
R_T=R_1+\sqrt{R_1^2+2R_1R_2}.
$$

Gợi ý: Vì mạng kéo dài vô hạn, phần mạng bên phải hai điểm $c,d$ cũng có điện trở $R_T$.
:::

![Mạng điện trở vô hạn của bài 26.83](img/young-26/hinh-p26-83.png)

<!-- detailed-solution:26.83 -->
::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Sau hai điện trở dọc đầu vào, phần còn lại nhìn từ $c,d$ có cùng điện trở $R_T$ do tính tự đồng dạng.

**Hướng đi:**

- Rút gọn đoạn đầu thành một nhánh trực tiếp $R_2$ song song với nhánh đi tiếp gồm hai điện trở $R_1$ nối tiếp với $R_T$.
- Đặt $x$ là điện trở giữa $c,d$. Rút gọn $R_2$ song song với toàn bộ phần mạng còn lại để lập phương trình.

Gọi $x$ là điện trở nhìn vào mạng từ hai điểm $c,d$. Tự đồng dạng cho $x=R_2\parallel(2R_1+x)$, còn điện trở toàn phần là $R_T=2R_1+x$:

$$
\begin{gathered}
xR_2+2R_1x+x^2\\
=2R_1R_2+R_2x,\\
x^2+2R_1x=2R_1R_2,\\
D^2=R_1^2+2R_1R_2,\\
x+R_1=D,\\
R_T=2R_1+x=R_1+D.
\end{gathered}
$$
:::

::: exercise 26.84
Mỗi cạnh của một khối lập phương có một điện trở $R$, tổng cộng $12$ điện trở nối tại các đỉnh. Tìm điện trở tương đương giữa hai đỉnh đối diện qua đường chéo khối, $a$ và $b$ trong Hình P26.84.
:::

![Khối lập phương điện trở của bài 26.84](img/young-26/hinh-p26-84.png)

<!-- detailed-solution:26.84 -->
::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Ba đỉnh kề với $a$ có cùng điện thế do đối xứng. Ba đỉnh kề với $b$ cũng cùng điện thế.

**Hướng đi:**

- Gộp các điện trở giữa hai nhóm đỉnh thành ba tầng nối tiếp. Tầng đầu và cuối có ba điện trở song song, tầng giữa có sáu điện trở song song.
- Mỗi tầng lần lượt tương đương $R/3$, $R/6$ và $R/3$ khi xét các đỉnh cùng điện thế.

$$
R_{eq}=\frac{R}{3}+\frac{R}{6}+\frac{R}{3}=\frac{5R}{6}.
$$
:::

::: exercise 26.85
**Chuỗi suy hao và sợi trục thần kinh.** Mạng vô hạn trong Hình P26.83 làm giảm hiệu điện thế giữa hai thanh dọc theo chiều dài. (a) Chứng minh nếu $V_{ab}$ là hiệu điện thế đầu vào thì $V_{cd}=V_{ab}/(1+\beta)$, trong đó $\beta=2R_1(R_T+R_2)/(R_TR_2)$ và $R_T$ từ bài 26.83. (b) Nếu đầu vào là $V_0$, chứng minh sau $n$ đoạn $V_n=V_0/(1+\beta)^n$. Với $R_1=R_2$, cần ít nhất bao nhiêu đoạn để $V_n<0{,}010V_0$? (c) Với $\Delta x=1{,}0\,\mathrm{\mu m}$, $R_1=6{,}4\times10^3\,\Omega$, $R_2=8{,}0\times10^8\,\Omega$, tính $R_T$ và $\beta$. (d) Tính phần điện áp còn lại và phần giảm sau quãng đường $2{,}0\,\mathrm{mm}$. Kết quả cho thấy sợi trục không thể chỉ là một dây dẫn thụ động: Hiệu điện thế phải được phục hồi định kỳ dọc theo sợi. Cơ chế phục hồi này chậm, nên tín hiệu truyền với tốc độ khoảng $30\,\mathrm{m/s}$. Khi cần đáp ứng nhanh hơn, một số sợi trục được bọc bởi bao myelin gồm nhiều đoạn mỡ ngăn cách bởi các nút Ranvier. Mỗi nút cách nút kế tiếp khoảng $2{,}0\,\mathrm{mm}$. Bao myelin làm tăng điện trở $R_2$ của đoạn màng dài $1{,}0\,\mathrm{\mu m}$ lên $3{,}3\times10^{12}\,\Omega$. (e) Tính phần điện áp còn lại và phần giảm giữa hai nút Ranvier liên tiếp.
:::

![Chuỗi suy hao dùng trong bài 26.85](img/young-26/hinh-p26-83.png)

<!-- detailed-solution:26.85 -->
::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Mỗi đoạn dài $\Delta x=1{,}0\,\mathrm{\mu m}$ có hai điện trở dọc $R_1$ nối tiếp trên hai thanh và điện trở ngang $R_2$. Điện trở nhìn vào phần mạng vô hạn là $R_T$.

**Hướng đi:**

- Tại cặp nút $c,d$, áp dụng chia áp giữa $R_2$ và đường vòng gồm $2R_1+R_T$. Tỉ số điện áp hai nút là hệ số truyền của một đoạn.
- Đổi quãng đường thành số đoạn bằng $n=L/\Delta x$. Tính tỉ số điện áp còn lại $V_n/V_0$, rồi lấy $1-V_n/V_0$ để được phần điện áp giảm.

(a) Hai điện trở dọc $R_1$ tạo thành điện trở nối tiếp $2R_1$ từ $a,b$ đến $c,d$. Nhìn từ $c,d$, nhánh tải là $R_2$ song song với phần mạng vô hạn còn lại có điện trở $R_T$. Vì thế:

$$
\begin{aligned}
R_L&=R_2\parallel R_T,\\
\frac{V_{cd}}{V_{ab}}&=\frac{R_L}{2R_1+R_L}\\
&=\frac{1}{1+2R_1/R_L},\\
\frac{2R_1}{R_L}&=2R_1\left(\frac1{R_2}+\frac1{R_T}\right)\\
&=\beta,\\
\frac{V_{cd}}{V_{ab}}&=\frac{1}{1+\beta}.
\end{aligned}
$$

(b) Mỗi đoạn nhân điện áp với cùng hệ số, do đó lặp lại phép chia $n$ lần:

$$
V_n=\frac{V_0}{(1+\beta)^n}.
$$

Khi $R_1=R_2=R$, bài 26.83 cho $R_T=(1+\sqrt3)R$, nên $\beta=2(R_T+R)/R_T=2{,}732$. Điều kiện là $n>\ln(0{,}010)/\ln[1/(1+\beta)]$, tức $n>3{,}50$. Cần ít nhất $4$ đoạn.

(c) Từ công thức bài 26.83, $R_T=3{,}2064\times10^6\,\Omega$. Thay vào biểu thức của $\beta$ được $\beta=4{,}01\times10^{-3}$.

(d) Quãng đường $2{,}0\,\mathrm{mm}$ gồm $2000$ đoạn. Tỉ số điện áp còn lại và phần giảm là:

$$
\begin{aligned}
\frac{V_{2000}}{V_0}&=(1+\beta)^{-2000}\\
&\approx3{,}4\times10^{-4},\\
1-\frac{V_{2000}}{V_0}&\approx0{,}99966\\
&=99{,}966\%.
\end{aligned}
$$

(e) Với điện trở màng đã tăng lên, $R_T\approx2{,}055\times10^8\,\Omega$ và $\beta\approx6{,}23\times10^{-5}$. Khoảng cách $2{,}0\,\mathrm{mm}$ vẫn tương ứng với $2000$ đoạn dài $1{,}0\,\mathrm{\mu m}$, nên:

$$
\begin{aligned}
\frac{V_{2000}}{V_0}&=(1+\beta)^{-2000}\\
&\approx0{,}883,\\
1-\frac{V_{2000}}{V_0}&\approx0{,}117\\
&=11{,}7\%.
\end{aligned}
$$

:::

### Bài tập theo đoạn đọc MCAT

**Tế bào thần kinh và mạch RC.** Sợi trục là phần tế bào thần kinh dẫn truyền tín hiệu. Nhiều tính chất điện của sợi trục do các kênh ion chi phối. Mỗi kênh ion là một phân tử protein xuyên qua màng tế bào. Khi mở, lỗ kênh chứa chất lỏng có điện trở suất thấp và nối điện bên trong tế bào với môi trường bên ngoài. Ngược lại, màng giàu lipid có điện trở suất rất cao.

::: exercise 26.86
Một kênh ion mở điển hình xuyên màng có điện trở $1\times10^{11}\,\Omega$. Mô hình lỗ kênh là hình trụ dài $12\,\mathrm{nm}$, bán kính $0{,}3\,\mathrm{nm}$. Điện trở suất của chất lỏng trong lỗ là bao nhiêu? (a) $10\,\Omega\,\mathrm{m}$, (b) $6\,\Omega\,\mathrm{m}$, (c) $2\,\Omega\,\mathrm{m}$, (d) $1\,\Omega\,\mathrm{m}$.
:::

<!-- detailed-solution:26.86 -->
::: solution Lời giải chi tiết
**Tóm tắt đề bài:** $R=1\times10^{11}\,\Omega$, $L=12\times10^{-9}\,\mathrm{m}$, $r=0{,}3\times10^{-9}\,\mathrm{m}$.

**Hướng đi:**

- Từ $R=\rho L/A$ suy ra $\rho=RA/L$, với $A=\pi r^2$.
- Đổi nanomet sang mét trước khi thay số để thu được đơn vị $\Omega\,\mathrm{m}$.

$$
\begin{aligned}
\rho&=\frac{RA}{L}\\
&=\frac{(1\times10^{11})\pi(0{,}3\times10^{-9})^2}{12\times10^{-9}}\\
&=2{,}36\,\Omega\,\mathrm{m}.
\end{aligned}
$$

Đáp án gần nhất là (c), $2\,\Omega\,\mathrm{m}$.
:::

::: exercise 26.87
Trong mô hình đơn giản của xung thần kinh, ion đi qua màng qua các kênh mở thuần trở. Mật độ dòng điện điển hình là $5\,\mathrm{mA/cm^2}$ khi điện áp qua màng là $50\,\mathrm{mV}$. Mật độ số kênh ion mở là bao nhiêu? (a) $1/\mathrm{cm^2}$, (b) $10/\mathrm{cm^2}$, (c) $10/\mathrm{mm^2}$, (d) $100/\mathrm{\mu m^2}$.
:::

<!-- detailed-solution:26.87 -->
::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Mỗi kênh có điện trở $1\times10^{11}\,\Omega$ như bài 26.86. Mỗi kênh chịu hiệu điện thế $0{,}050\,\mathrm{V}$.

**Hướng đi:**

- Tính dòng mỗi kênh, rồi chia mật độ dòng tổng cho dòng một kênh.
- Đổi đơn vị từ $\mathrm{cm^{-2}}$ sang $\mathrm{\mu m^{-2}}$ để khớp các lựa chọn.

$$
\begin{aligned}
i_{\mathrm{ch}}&=0{,}050/(1\times10^{11})\\
&=5{,}0\times10^{-13}\,\mathrm{A},\\
n&=\frac{5\times10^{-3}\,\mathrm{A/cm^2}}{5\times10^{-13}\,\mathrm{A}}\\
&=1\times10^{10}\,\mathrm{cm^{-2}}\\
&=100\,\mathrm{\mu m^{-2}}.
\end{aligned}
$$

Chọn (d).
:::

::: exercise 26.88
Màng tế bào ở nhiều sinh vật có điện dung trên đơn vị diện tích $1\,\mathrm{\mu F/cm^2}$. Để tín hiệu điện truyền dọc sợi trục, điện tích trên tụ màng phải thay đổi. Hằng số thời gian cần thiết khi các kênh ion mở là bao nhiêu? (a) $1\,\mathrm{\mu s}$, (b) $10\,\mathrm{\mu s}$, (c) $100\,\mathrm{\mu s}$, (d) $1\,\mathrm{ms}$.
:::

<!-- detailed-solution:26.88 -->
::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Điện dung đơn vị diện tích là $C_A=1\times10^{-6}\,\mathrm{F/cm^2}$. Từ bài 26.87, độ dẫn trên đơn vị diện tích là $G_A=J/V$.

**Hướng đi:**

- Hằng số thời gian là tỉ số điện dung trên độ dẫn. Diện tích triệt tiêu khi lấy tỉ số.
- Từ bài 26.87 lấy độ dẫn màng, rồi dùng $\tau=C/G$.

$$
\begin{aligned}
\tau&=\frac{C_A}{G_A}\\
&=\frac{1\times10^{-6}}{0{,}1}\\
&=1\times10^{-5}\,\mathrm{s}.
\end{aligned}
$$

Chọn (b), $10\,\mathrm{\mu s}$.
:::
