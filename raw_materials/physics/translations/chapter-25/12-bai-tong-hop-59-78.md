<!-- Bài 25.59–25.78, trang in 841–843. -->

## Bài tập tổng hợp

::: exercise 25.59 • CALC
Một vật liệu có điện trở suất $\rho$ được tạo thành khối nón cụt đặc, chiều cao $h$, bán kính hai mặt phẳng đầu mút lần lượt là $r_1$ và $r_2$. Hình P25.59 minh họa khối vật liệu. (a) Tính điện trở giữa hai mặt phẳng. Gợi ý: Chia hình nón cụt thành nhiều đĩa mỏng rồi tính điện trở của một đĩa. (b) Chứng minh kết quả trở về công thức (25.10) khi $r_1=r_2$.
:::

![Hình P25.59: Khối nón cụt có bán kính đầu nhỏ r₁, đầu lớn r₂ và chiều cao h](img/young-25/hinh-p25-59.png)

<!-- detailed-solution:25.59 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Dòng điện chạy dọc trục khối nón cụt. Bán kính mặt cắt biến thiên tuyến tính từ $r_1$ đến $r_2$.

**Hướng đi:**

- Chia vật thành các lát bề dày $dx$, có điện trở $dR=\rho\,dx/A(x)$.
- Viết bán kính tại vị trí $x$ từ tam giác đồng dạng, rồi tích phân các lát nối tiếp.
- Cho hai bán kính bằng nhau để so với dây trụ có tiết diện không đổi.

(a) Đo $x$ từ mặt bán kính $r_1$. Bán kính tại $x$ là

$$
r(x)=r_1+\frac{r_2-r_1}{h}x.
$$

Diện tích tiết diện là $A(x)=\pi r(x)^2$, nên

$$
\begin{aligned}
R &= \int_0^h dR \\
&= \frac{\rho}{\pi}\int_0^h \frac{dx}{\left(r_1+\frac{r_2-r_1}{h}x\right)^2} \\
&= \frac{\rho h}{\pi r_1r_2}.
\end{aligned}
$$

Ở bước tích phân, đặt $u=r_1+(r_2-r_1)x/h$. Khi đó $dx=h\,du/(r_2-r_1)$, còn $u$ chạy từ $r_1$ đến $r_2$. Tích phân $\int u^{-2}du=-1/u$ cho thừa số $h/(r_1r_2)$.

(b) Khi $r_1=r_2=r$, khối trở thành trụ đồng nhất. Công thức thu được:

$$
R=\frac{\rho h}{\pi r^2}
=\frac{\rho L}{A},
$$

đúng với công thức điện trở của dây trụ.
:::

::: exercise 25.60 • CALC
Vùng giữa hai vỏ cầu dẫn đồng tâm bán kính $a$ và $b$ được lấp bằng vật liệu có điện trở suất $\rho$. (a) Chứng minh điện trở giữa hai vỏ là

$$
R=\frac{\rho}{4\pi}\left(\frac1a-\frac1b\right).
$$

(b) Tìm mật độ dòng điện theo bán kính, biểu diễn qua hiệu điện thế $V_{ab}$ giữa hai vỏ. (c) Chứng minh kết quả câu (a) trở về công thức (25.10) khi khe $L=b-a$ nhỏ.
:::

<!-- detailed-solution:25.60 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Dòng chạy xuyên tâm qua các mặt cầu. Diện tích mặt cầu bán kính $r$ là $4\pi r^2$.

**Hướng đi:**

- Các vỏ cầu mỏng mắc nối tiếp theo bán kính, nên $dR=\rho\,dr/(4\pi r^2)$.
- Tích phân từ $a$ đến $b$, sau đó dùng $I=V_{ab}/R$ và $J=I/(4\pi r^2)$.
- Với khe nhỏ, coi diện tích mặt cầu gần như không đổi trên toàn bề dày.

(a)

$$
\begin{aligned}
R &= \int_a^b\frac{\rho\,dr}{4\pi r^2} \\
&= \frac{\rho}{4\pi}\left(\frac1a-\frac1b\right).
\end{aligned}
$$

(b) Mật độ dòng hướng từ vỏ có điện thế cao sang vỏ có điện thế thấp. Độ lớn của nó tại bán kính $r$ là

$$
\begin{aligned}
J(r) &= \frac{I}{4\pi r^2} \\
&= \frac{V_{ab}}{4\pi Rr^2} \\
&= \frac{V_{ab}ab}{\rho(b-a)r^2}.
\end{aligned}
$$

(c) Nếu $L=b-a\ll a$, bán kính gần như không đổi trong khe, lấy $r\approx a$ và $b\approx a+L$. Khi đó

$$
R\approx\frac{\rho L}{4\pi a^2}
=\frac{\rho L}{A},
$$

với $A\approx4\pi a^2$. Đây là công thức của một lớp vật liệu phẳng mỏng.
:::

::: exercise 25.61 •
Hiệu điện thế giữa hai cực của pin là 8,40 V khi dòng điện 1,50 A đi qua pin từ cực âm đến cực dương. Khi dòng điện 3,50 A chạy theo chiều ngược lại, hiệu điện thế hai cực là 10,20 V. (a) Tìm điện trở trong của pin. (b) Tìm suất điện động.
:::

<!-- detailed-solution:25.61 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Trường hợp đầu pin phát điện, dòng đi từ cực âm đến cực dương bên trong. Trường hợp sau dòng bị đảo và pin nhận điện.

**Hướng đi:**

- Khi pin phát điện, điện áp cực là $\mathcal E-I_1r$.
- Khi nạp pin, điện áp cực là $\mathcal E+I_2r$.
- Trừ hai phương trình để tìm $r$, rồi thế lại tìm $\mathcal E$.

Ta có

$$
\begin{aligned}
8{,}40 &= \mathcal E-(1{,}50)r, \\
10{,}20 &= \mathcal E+(3{,}50)r.
\end{aligned}
$$

Lấy phương trình thứ hai trừ phương trình thứ nhất:

$$
r=\frac{10{,}20-8{,}40}{1{,}50+3{,}50}
=0{,}360\,\Omega.
$$

Suy ra

$$
\begin{aligned}
\mathcal E &= 8{,}40+(1{,}50)(0{,}360) \\
&= 8{,}94\,\mathrm V.
\end{aligned}
$$
:::

::: exercise 25.62 •
(a) Tìm hiệu điện thế $V_{ad}$ của mạch Hình P25.62. (b) Tìm điện áp hai cực của pin 4,00 V. (c) Mắc thêm tại d một pin có suất điện động 10,30 V, điện trở trong 0,50 Ω, cực âm nối với cực âm của pin 8,00 V. Tìm hiệu điện thế $V_{bc}$ giữa hai cực pin 4,00 V sau khi thêm pin.
:::

![Hình P25.62: Mạch một vòng có hai pin 4,00 V và 8,00 V cùng các điện trở](img/young-25/hinh-p25-62.png)

<!-- detailed-solution:25.62 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Hai pin 4,00 V và 8,00 V có cực dương ở bên trái. Tổng điện trở vòng ban đầu là $24{,}0\,\Omega$.

**Hướng đi:**

- Viết quy tắc vòng theo chiều kim đồng hồ. Pin 8 V làm tăng thế theo vòng, pin 4 V làm giảm thế.
- Dùng dòng điện để suy sụt áp trên các điện trở và điện áp hai đầu pin.
- Ở câu (c), pin mới có cực âm tại d, nên khi đi theo chiều kim đồng hồ qua pin mới là đi từ cực dương sang cực âm.

(a) Dòng vòng ban đầu là

$$
I=\frac{8{,}00-4{,}00}{24{,}0}
=\frac16\,\mathrm A.
$$

Đi từ a đến d qua điện trở 6 Ω, điện trở trong 0,50 Ω, pin 4 V và điện trở 9 Ω:

$$
\begin{aligned}
V_a-V_d &= 6I+V_{bc}+9I \\
&= 6{,}58\,\mathrm V.
\end{aligned}
$$

Vậy $V_{ad}=+6{,}58$ V.

(b) Dòng đi từ cực dương b qua pin 4 V về cực âm c, nên pin đang nhận điện. Điện áp hai cực:

$$
V_{bc}=4{,}00+(0{,}50)I
=4{,}08\,\mathrm V.
$$

(c) Tổng điện trở mới là $24{,}5\,\Omega$. Dòng theo chiều kim đồng hồ:

$$
\begin{aligned}
I' &= \frac{8{,}00-4{,}00-10{,}30}{24{,}5} \\
&= -0{,}257\,\mathrm A.
\end{aligned}
$$

Dấu âm cho biết dòng thực chạy ngược chiều đã chọn. Điện áp pin 4 V khi đó là

$$
\begin{aligned}
V'_{bc} &= 4{,}00+(0{,}50)I' \\
&= 3{,}87\,\mathrm V.
\end{aligned}
$$
:::

::: exercise 25.63 • BIO
Điện trở suất khối trung bình của cơ thể người, không kể điện trở bề mặt da, xấp xỉ 5,0 Ω·m. Đường dẫn điện giữa hai bàn tay có thể mô hình gần đúng như một trụ dài 1,6 m, đường kính 0,10 m. Có thể làm điện trở da không đáng kể bằng cách ngâm tay trong nước muối. (a) Tìm điện trở giữa hai tay trong điều kiện đó. (b) Cần hiệu điện thế bao nhiêu giữa hai tay để có dòng điện nguy hiểm 100 mA? Kết quả cho thấy ngay cả hiệu điện thế nhỏ cũng gây nguy hiểm khi da ẩm. (c) Với dòng ở câu (b), công suất tỏa nhiệt trong cơ thể là bao nhiêu?
:::

<!-- detailed-solution:25.63 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Mô hình cơ thể là trụ dẫn, bỏ điện trở da. Bán kính đường dẫn là 0,050 m.

**Hướng đi:**

- Dùng $R=\rho L/A$, với $A=\pi(0{,}050)^2$.
- Dùng định luật Ôm ở dòng 0,100 A.
- Công suất tỏa nhiệt là $I^2R$.

Diện tích tiết diện:

$$
\begin{aligned}
A &= \pi(0{,}050)^2 \\
&= 7{,}85\times10^{-3}\,\mathrm{m^2}.
\end{aligned}
$$

(a)

$$
\begin{aligned}
R &= \frac{(5{,}0)(1{,}6)}{7{,}85\times10^{-3}} \\
&\approx 1{,}02\times10^3\,\Omega.
\end{aligned}
$$

(b) $V=IR=(0{,}100)(1019)\approx102$ V. (c) $P=I^2R\approx10{,}2$ W. Dòng điện nguy hiểm vẫn có thể xuất hiện ở điện áp khoảng một trăm vôn khi điện trở da giảm mạnh.
:::

::: exercise 25.64 • BIO
Điện trở giữa hai bàn tay của một người là 10 kΩ. Người đó vô tình chạm vào hai cực của nguồn 14 kV có điện trở trong 2000 Ω. (a) Dòng điện qua cơ thể là bao nhiêu? (b) Công suất tỏa trong cơ thể là bao nhiêu? (c) Muốn nguồn an toàn hơn bằng cách tăng điện trở trong, cần điện trở trong tối thiểu bao nhiêu để dòng cực đại trong tình huống trên không vượt 1,00 mA?
:::

<!-- detailed-solution:25.64 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Điện trở cơ thể 10 kΩ mắc nối tiếp với điện trở trong nguồn. Dùng định luật Ôm cho toàn mạch.

**Hướng đi:**

- Tổng điện trở ban đầu là $10\,\mathrm{k}\Omega+2\,\mathrm{k}\Omega$.
- Công suất trong cơ thể chỉ dùng điện trở cơ thể: $I^2R_{\mathrm{cơ thể}}$.
- Với giới hạn 1,00 mA, tổng điện trở ít nhất phải là $\mathcal E/I_{\max}$.

(a)

$$
I=\frac{14\,000}{10\,000+2\,000}
=1{,}17\,\mathrm A.
$$

(b) $P_{\mathrm{cơ thể}}=I^2(10\,000)\approx1{,}36\times10^4$ W.

(c)

$$
\begin{aligned}
r_{\min} &= \frac{14\,000}{0{,}00100}-10\,000 \\
&= 1{,}399\times10^7\,\Omega.
\end{aligned}
$$

Đây là mô hình dòng một chiều đơn giản. Không được dùng kết quả này thay cho quy chuẩn an toàn điện thực tế.
:::

::: exercise 25.65 •
Chi phí điện điển hình là 0,120 đô la mỗi kilowatt-giờ. (a) Một bóng đèn hiên 75 W bật liên tục ngày đêm. Chi phí điện trong một năm là bao nhiêu? (b) Tủ lạnh dùng 400 W khi chạy và chạy 8 giờ mỗi ngày. Chi phí điện hằng năm là bao nhiêu?
:::

<!-- detailed-solution:25.65 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Giá điện $0{,}120$ đô la/kWh. Lấy một năm bằng 365 ngày.

**Hướng đi:**

- Năng lượng là công suất nhân thời gian, đổi W thành kW.
- Tiền điện bằng số kWh nhân đơn giá.

(a) Bóng đèn dùng $0{,}075\times24\times365=657$ kWh mỗi năm, nên chi phí khoảng 78,8 đô la. (b) Tủ lạnh dùng $0{,}400\times8\times365=1168$ kWh mỗi năm, nên chi phí khoảng 140 đô la.
:::

::: exercise 25.66 ••
Một dây cáp đồng hình trụ dài 1,50 km mắc vào hiệu điện thế 220,0 V. (a) Đường kính dây phải bằng bao nhiêu để dây tỏa nhiệt với công suất 90,0 W? (b) Điện trường bên trong dây khi đó có độ lớn bao nhiêu?
:::

<!-- detailed-solution:25.66 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Dây đồng có $\rho=1{,}72\times10^{-8}\,\Omega\mathrm m$, $L=1500$ m, $V=220$ V và $P=90{,}0$ W.

**Hướng đi:**

- Từ $P=V^2/R$ tìm điện trở cần có.
- Dùng $R=\rho L/A$ tìm tiết diện, rồi đổi diện tích tròn thành đường kính.
- Điện trường dọc dây là $V/L$.

$$
\begin{aligned}
R &= \frac{V^2}{P}=537{,}8\,\Omega, \\
A &= \frac{\rho L}{R}=4{,}80\times10^{-8}\,\mathrm{m^2}, \\
d &= 2\sqrt{\frac A\pi}=2{,}47\times10^{-4}\,\mathrm m \\
&= 0{,}247\,\mathrm{mm}, \\
E &= \frac VL=0{,}147\,\mathrm{V/m}.
\end{aligned}
$$
:::

::: exercise 25.67 •• CALC
Một trụ dài 1,50 m, bán kính 1,10 cm, được làm từ hỗn hợp vật liệu có điện trở suất thay đổi theo khoảng cách x tính từ đầu trái, theo $\rho(x)=a+bx^2$, trong đó a và b là hằng số. Ở đầu trái, $\rho=2{,}25\times10^{-8}\,\Omega\mathrm m$, còn ở đầu phải $\rho=8{,}50\times10^{-8}\,\Omega\mathrm m$. (a) Tìm điện trở của trụ. (b) Tìm độ lớn điện trường tại trung điểm khi dòng điện là 1,75 A. (c) Cắt trụ thành hai đoạn dài 75,0 cm. Tìm điện trở mỗi đoạn.
:::

<!-- detailed-solution:25.67 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Tiết diện trụ không đổi $A=\pi(0{,}0110)^2$. Điện trở suất tăng bậc hai từ trái sang phải.

**Hướng đi:**

- Từ hai đầu suy $a=\rho_0$ và $b=(\rho_L-\rho_0)/L^2$.
- Các lát theo chiều dài mắc nối tiếp, nên tích phân $dR=\rho(x)dx/A$.
- Tại trung điểm dùng $E=\rho I/A$. Hai nửa cần tích phân trên các khoảng riêng.

Ta có $a=2{,}25\times10^{-8}$ Ω·m và
$b=(8{,}50-2{,}25)\times10^{-8}/(1{,}50)^2$.

(a)

$$
\begin{aligned}
R &= \frac1A\int_0^L(a+bx^2)\,dx \\
&= \frac{L}{A}\left(\rho_0+\frac{\rho_L-\rho_0}{3}\right) \\
&\approx 1{,}71\times10^{-4}\,\Omega.
\end{aligned}
$$

(b) Ở $x=L/2$, $\rho=\rho_0+(\rho_L-\rho_0)/4=3{,}8125\times10^{-8}$ Ω·m, do đó

$$
\begin{aligned}
E_{\mathrm{mid}} &= \frac{\rho(L/2)I}{A} \\
&\approx 1{,}76\times10^{-4}\,\mathrm{V/m}.
\end{aligned}
$$

(c)

$$
\begin{aligned}
R_{\mathrm{trái}} &= \frac1A\int_0^{L/2}(a+bx^2)\,dx \\
&\approx 5{,}47\times10^{-5}\,\Omega, \\
R_{\mathrm{phải}} &= R-R_{\mathrm{trái}} \\
&\approx 1{,}16\times10^{-4}\,\Omega.
\end{aligned}
$$

:::

::: exercise 25.68 •• DỮ LIỆU
Đèn huỳnh quang compact hiệu quả phát sáng hơn bóng sợi đốt. Một bóng compact cho lượng sáng tương đương bóng sợi đốt 100 W chỉ tiêu thụ 23 W. Bóng compact có giá 11,00 đô la và tuổi thọ trung bình 10 000 giờ. Bóng sợi đốt giá 0,75 đô la, tuổi thọ 750 giờ. Lấy giá điện 0,080 đô la/kWh và thời gian sử dụng 4,0 giờ mỗi ngày. (a) Tính tổng chi phí, gồm tiền mua bóng và tiền điện, để vận hành mỗi loại trong 3,0 năm. (b) Dùng bóng compact tiết kiệm được bao nhiêu? (c) Điện trở của bóng “100 W” compact là bao nhiêu? Nhớ rằng bóng thực sự dùng 23 W khi hoạt động ở 120 V.
:::

<!-- detailed-solution:25.68 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Thời gian hoạt động trong ba năm là $3\times365\times4=4380$ giờ. Cần mua đủ số bóng sợi đốt để phủ hết khoảng thời gian này.

**Hướng đi:**

- Tính điện năng mỗi bóng dùng theo kWh rồi nhân giá điện.
- Số bóng sợi đốt là làm tròn lên $4380/750$, còn bóng compact chỉ cần một bóng.
- Dùng công suất thực 23 W và điện áp 120 V để tìm điện trở compact.

(a) Bóng compact dùng $0{,}023\times4380=100{,}74$ kWh. Tiền điện tương ứng là $100{,}74\times0{,}080\approx8{,}06$ USD. Tổng chi phí:

$$
\begin{aligned}
C_1 &= 11{,}00+8{,}06 \\
&\approx 19{,}06.
\end{aligned}
$$

Chi phí này là 19,06 USD.

Bóng sợi đốt cần $\lceil4380/750\rceil=6$ bóng. Chúng dùng $0{,}100\times4380=438$ kWh, tương ứng tiền điện $438\times0{,}080=35{,}04$ USD. Tổng chi phí:

$$
\begin{aligned}
C_2 &= 6(0{,}75)+35{,}04 \\
&= 39{,}54.
\end{aligned}
$$

Chi phí này là 39,54 USD.

(b) Tiết kiệm khoảng $39{,}54-19{,}06=20{,}48$ đô la trong ba năm. (c)

$$
R=\frac{V^2}{P}
=\frac{120^2}{23}
\approx626\,\Omega.
$$
:::

::: exercise 25.69 ••• CP
Hai bình hình trụ có thành cách điện và hai nắp dẫn điện được nối vào mạch Hình P25.69 để đo độ mặn của nước. Hai bình giống nhau, bán kính $r=5{,}00$ cm, chiều dài $L=3{,}00$ cm. Pin lý tưởng có điện áp 10,0 V, nối tiếp với điện trở $R=15{,}0\,\Omega$. Bình trái chứa nước cất tinh khiết, có điện trở suất vô hạn. Bình phải chứa nước muối. Điện trở suất dung dịch có quan hệ $\rho=(s_0/s)\,\Omega\mathrm m$, trong đó s là độ mặn tính theo phần nghìn (ppt), $s_0=6{,}30$ ppt. Ampe kế chỉ 484 mA. (a) Tìm độ mặn của dung dịch. (b) Bình trái hoạt động như một tụ điện. Dùng công thức (24.19) để tìm điện dung, rồi tính điện tích trên bản trên. Điện môi nước có K = 80,4. (c) Tốc độ tiêu tán năng lượng trong nước muối là bao nhiêu? (d) Độ mặn nào làm điện trở 15,0 Ω tiêu tán một nửa công suất do pin cung cấp?
:::

![Hình P25.69: Hai bình dẫn điện hình trụ nối song song, cùng mạch pin, điện trở và ampe kế](img/young-25/hinh-p25-69.png)

<!-- detailed-solution:25.69 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Bình nước cất là tụ, nhánh nước muối là điện trở. Ở trạng thái dòng điện một chiều ổn định, tụ đã nạp nên không có dòng liên tục qua nhánh đó.

**Hướng đi:**

- Dòng 484 mA đi qua điện trở 15 Ω và dung dịch nước muối. Từ điện áp pin suy điện trở dung dịch.
- Dòng chạy dọc trục giữa hai nắp, nên điện trở là $\rho L/(\pi r^2)$.
- Điện áp trên hai bình song song bằng điện áp trên dung dịch. Tính tụ phẳng của bình nước cất rồi dùng $Q=CV$.
- Với câu (d), đặt công suất trên điện trở ngoài bằng một nửa công suất pin cấp.

(a) Điện trở dung dịch:

$$
R_s=\frac{10{,}0}{0{,}484}-15{,}0
=5{,}66\,\Omega.
$$

Suy ra $\rho_s=R_s\pi r^2/L=1{,}48\,\Omega\mathrm m$, nên $s=s_0/\rho_s\approx4{,}25$ ppt.

(b) Bình nước cất có

$$
\begin{aligned}
C &= \frac{K\varepsilon_0\pi r^2}{L} \\
&\approx 1{,}86\times10^{-10}\,\mathrm F.
\end{aligned}
$$

Điện áp nhánh song song là $V_s=I R_s\approx2{,}74$ V. Do đó $Q=CV_s\approx5{,}11\times10^{-10}$ C, tức khoảng 510 pC trên bản trên.

(c)

$$
P_s=I^2R_s
\approx1{,}33\,\mathrm W.
$$

(d) Công suất pin cấp là $\mathcal EI$, còn điện trở 15 Ω tiêu tán $I^2R$. Điều kiện $I^2R=\mathcal EI/2$ cho $I=\mathcal E/(2R)=1/3$ A. Khi đó điện trở dung dịch phải là $10/(1/3)-15=15\,\Omega$. Từ $\rho_s=R_s\pi r^2/L$, suy ra độ mặn khoảng 1,60 ppt.
:::

::: exercise 25.70 •• CP
Xét mạch Hình P25.70. Pin có suất điện động 72,0 V và điện trở trong không đáng kể. $R_2=2{,}00\,\Omega$, $C_1=3{,}00$ mF và $C_2=6{,}00$ mF. Sau khi các tụ đạt điện tích cuối, $C_1$ mang $Q_1=18{,}0$ mC. Tìm (a) điện tích cuối trên $C_2$, (b) điện trở $R_1$.
:::

![Hình P25.70: Điện trở R₁ nối tiếp với các nhánh song song R₂, C₁ và C₂](img/young-25/hinh-p25-70.png)

<!-- detailed-solution:25.70 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Ở trạng thái cuối của mạch một chiều, nhánh tụ hở mạch. C₁ và C₂ mắc song song với nhau và với R₂.

**Hướng đi:**

- Tìm điện áp nhánh từ $V_1=Q_1/C_1$, rồi tính $Q_2=C_2V_1$.
- Dòng qua R₂ là $V_1/R_2$. Ở trạng thái ổn định, dòng đó cũng chạy qua R₁.
- Dùng độ sụt áp trên R₁ cộng điện áp nhánh để tìm R₁.

Điện áp trên các nhánh song song là $V=18{,}0\,\mathrm{mC}/3{,}00\,\mathrm{mF}=6{,}00$ V. Vậy

$$
\begin{aligned}
Q_2 &= C_2V \\
&= (6{,}00\,\mathrm{mF})(6{,}00\,\mathrm V) \\
&= 36{,}0\,\mathrm{mC}.
\end{aligned}
$$

Dòng qua R₂ là $I=6{,}00/2{,}00=3{,}00$ A. Trên R₁ có $72{,}0-6{,}00=66{,}0$ V, vì thế $R_1=66{,}0/3{,}00=22{,}0\,\Omega$.
:::

::: exercise 25.71 •• CP
Xét mạch Hình P25.71. Nguồn điện động lý tưởng. Các điện trở có $R_1=6{,}00\,\Omega$ và $R_2=4{,}00\,\Omega$. Tụ điện có $C=9{,}00$ mF. Khi tụ đã nạp đầy, điện tích có độ lớn $Q=36{,}0$ mC. Tính suất điện động $\mathcal E$.
:::

![Hình P25.71: Nguồn và hai điện trở cấp dòng đến nhánh tụ điện](img/young-25/hinh-p25-71.png)

<!-- detailed-solution:25.71 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Khi tụ nạp đầy trong mạch một chiều, nhánh tụ không còn dòng. Dòng chạy qua R₂ và R₁ nối tiếp.

**Hướng đi:**

- Điện áp trên tụ là $V_C=Q/C$, bằng điện áp trên R₁ vì chúng mắc giữa cùng hai nút.
- Dùng $I=V_C/R_1$, rồi tính sụt áp trên R₂.
- Suất điện động bằng tổng hai sụt áp.

Ta có $V_C=36{,}0\,\mathrm{mC}/9{,}00\,\mathrm{mF}=4{,}00$ V. Dòng ổn định là $I=4{,}00/6{,}00=0{,}667$ A. Do đó

$$
\begin{aligned}
\mathcal E &= V_C+IR_2 \\
&= 4{,}00+(0{,}667)(4{,}00) \\
&= 6{,}67\,\mathrm V.
\end{aligned}
$$
:::

::: exercise 25.72 •• DATA
Một điện trở ngoài R được mắc vào hai cực của pin. Thay đổi R, rồi đo dòng I và điện áp đầu cực $V_{ab}$. Kết quả được vẽ thành đồ thị $V_{ab}$ theo I ở Hình P25.72 cùng đường thẳng khớp dữ liệu. (a) Dùng đồ thị tìm suất điện động và điện trở trong. (b) Giá trị R nào làm $V_{ab}$ bằng 80,0% suất điện động?
:::

![Hình P25.72: Đồ thị điện áp đầu cực của pin theo dòng điện](img/young-25/hinh-p25-72.png)

<!-- detailed-solution:25.72 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Với pin phát điện, $V_{ab}=\mathcal E-rI$. Vì vậy tung độ gốc là suất điện động, độ lớn hệ số góc là điện trở trong.

**Hướng đi:**

- Đọc hai điểm xa nhau trên đường khớp để tính hệ số góc và giao điểm trục đứng.
- Ở phần (b), dùng $V_{ab}=0{,}8\mathcal E$, giải I rồi dùng $R=V_{ab}/I$.

Đường khớp đi qua gần $(I,V)=(2{,}0\,\mathrm A,32\,\mathrm V)$ và $(8{,}0\,\mathrm A,20\,\mathrm V)$. Hệ số góc là $-2{,}0$ V/A, nên $r=2{,}0\,\Omega$. Ngoại suy về $I=0$, ta được $\mathcal E=36{,}0$ V.

Khi $V_{ab}=28{,}8$ V:

$$
\begin{aligned}
I &= \frac{36{,}0-28{,}8}{2{,}0}=3{,}6\,\mathrm A, \\
R &= \frac{28{,}8}{3{,}6}=8{,}0\,\Omega.
\end{aligned}
$$
:::

::: exercise 25.73 •• DATA
Đo điện áp $V_{ab}$ trên hai điện trở A và B khi thay đổi dòng điện I. Dữ liệu là:

| Điện trở A: I (A) | 0,50 | 1,00 | 2,00 | 4,00 |
| --- | ---: | ---: | ---: | ---: |
| Điện trở A: $V_{ab}$ (V) | 2,55 | 3,11 | 3,77 | 4,58 |
| Điện trở B: I (A) | 0,50 | 1,00 | 2,00 | 4,00 |
| Điện trở B: $V_{ab}$ (V) | 1,94 | 3,88 | 7,76 | 15,52 |

(a) Vẽ $V_{ab}$ theo I và điện trở $R=V_{ab}/I$ theo I cho mỗi điện trở. (b) A có tuân theo định luật Ôm không? Giải thích. (c) B có tuân theo định luật Ôm không? Giải thích. (d) Tìm công suất tỏa trên A khi nối vào pin 4,00 V có điện trở trong không đáng kể. (e) Tìm công suất tỏa trên B khi nối vào pin đó.
:::

<!-- detailed-solution:25.73 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Điện trở Ohm có $V/I$ không đổi. Dữ liệu A tạo đường cong, còn dữ liệu B có cùng tỷ số ở mọi điểm.

**Hướng đi:**

- Tính tỷ số V/I ở mỗi điểm, đồng thời vẽ các cặp (I,V).
- Với A, đọc giao điểm của đường cong gần đúng với $V=4{,}00$ V. Dữ liệu rời rạc nên công suất từ đồ thị là xấp xỉ.
- Với B, dùng điện trở không đổi.

(a) Các điểm A cho $R=5{,}10,\ 3{,}11,\ 1{,}89,\ 1{,}15\,\Omega$, nên R phụ thuộc dòng. Các điểm B đều cho $R=3{,}88\,\Omega$.

![Đồ thị điện áp theo dòng của hai điện trở A và B](img/young-25/hinh-giai25-73-dien-ap.svg)

![Đồ thị điện trở theo dòng, với R được tính bằng V trên I tại từng điểm đo](img/young-25/hinh-giai25-73-dien-tro.svg)

Các điểm đánh dấu là dữ liệu đã cho. Đường cong nét đứt là đường gần đúng bậc hai trên khoảng dòng đo được để đọc giá trị trung gian, không phải một định luật vật liệu ngoài khoảng đó. Điện trở B cho đường điện áp tuyến tính và đường điện trở nằm ngang.

(b) A không tuân theo định luật Ohm. (c) B tuân theo định luật Ohm trong miền dữ liệu.

(d) Từ đường gần đúng V–I của A, tại 4,00 V dòng xấp xỉ 2,34 A, nên công suất khoảng 9,36 W, làm tròn thành 9,4 W. (e)

$$
\begin{aligned}
P_B &= \frac{V^2}{R} \\
&= \frac{(4{,}00)^2}{3{,}88} \\
&= 4{,}12\,\mathrm W.
\end{aligned}
$$
:::

::: exercise 25.74 •• DATA
Bài toán cho bảng giới hạn dòng điện của dây đồng bọc cách điện bằng vải sơn, dùng trong nhà ở, khách sạn, văn phòng và nhà máy. Các giá trị được nêu theo Bộ luật Điện Quốc gia Hoa Kỳ trong bảng dữ kiện này. Cỡ dây là chuẩn mô tả đường kính, với số gauge càng nhỏ thì dây càng lớn.

| Gauge | Đường kính (cm) | $I_{\max}$ (A) |
| ---: | ---: | ---: |
| 14 | 0,163 | 18 |
| 12 | 0,205 | 25 |
| 10 | 0,259 | 30 |
| 8 | 0,326 | 40 |
| 6 | 0,412 | 60 |
| 5 | 0,462 | 65 |
| 4 | 0,519 | 85 |

(a) Những yếu tố nào quyết định dòng tối đa của dây điện gia dụng? (b) Nhà cần cấp tổng công suất 4200 W qua dây, khi điện áp trên các thiết bị là 120 V. Chọn gauge nhỏ nhất vẫn cho phép dòng đó. (c) Nếu dây đã chọn có tổng chiều dài 42,0 m, công suất tỏa nhiệt trên dây là bao nhiêu? (d) Nếu thay bằng dây có đường kính lớn kế tiếp, tiết kiệm được bao nhiêu tiền điện trong một năm? Lấy giá điện 0,11 đô la/kWh và thiết bị hoạt động trung bình 12 giờ/ngày.
:::

<!-- detailed-solution:25.74 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Dòng tải là $I=P/V$. Tổn hao trên dây phụ thuộc điện trở của cả đoạn dây được cho.

**Hướng đi:**

- Dòng cực đại phụ thuộc khả năng tỏa nhiệt, vật liệu cách điện, điều kiện làm mát và quy định an toàn.
- Chọn gauge nhỏ nhất về kích thước dây, tức gauge có số lớn nhất trong bảng thỏa dòng.
- Dùng $R=\rho L/A$, $P_{\mathrm{dây}}=I^2R$, rồi tính chênh năng lượng và tiền điện.

(b) $I=4200/120=35{,}0$ A, nên gauge 8 là dây mảnh nhất cho phép. (c) Với đường kính $0{,}326$ cm, $A=\pi(0{,}00326/2)^2$. Dùng $\rho_{\mathrm{Cu}}=1{,}72\times10^{-8}\,\Omega\mathrm m$, ta được $R\approx0{,}0865\,\Omega$ và công suất hao phí xấp xỉ 106 W.

(d) Gauge 6 có $d=0{,}412$ cm và hao phí khoảng 66,4 W. Chênh lệch khoảng 39,6 W. Trong $12\times365=4380$ giờ, tiết kiệm $39{,}6\times4380/1000\approx173$ kWh, tương đương khoảng 19,1 đô la/năm. Phần (a) phụ thuộc cách lắp đặt, nhiệt độ môi trường, bó dây, cách điện và giới hạn tăng nhiệt cho phép, không chỉ đường kính.
:::

::: exercise 25.75 ••• CALC
Một vật liệu có điện trở suất $\rho$ tạo thành trụ dài L. Gọi a là bán kính lõi dẫn điện ở giữa và b là bán kính mặt ngoài. Mặt ngoài cũng được phủ vật dẫn, rồi nối với dây thứ hai. (a) Nếu dây thứ hai có điện thế cao hơn dây nối với lõi một lượng V, điện trường cục bộ trong trụ hướng chiều nào? (b) Độ lớn trường là $c/r$, với c là hằng số và r là khoảng cách tới trục. Dùng $V=-\int\vec E\cdot d\vec l$ để tìm c. (c) Tìm điện trở thiết bị. (d) Một điện trở trụ rỗng dài 1,00 cm có a = 1,50 mm, b = 3,00 mm và điện trở 6,80 kΩ. Tìm điện trở suất vật liệu.
:::

<!-- detailed-solution:25.75 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Dòng chạy xuyên tâm qua thành trụ từ mặt ngoài có thế cao đến lõi có thế thấp. Tiết diện vuông góc dòng tại bán kính r là mặt trụ $2\pi rL$, với a là bán kính trong và b là bán kính ngoài.

**Hướng đi:**

- Điện trường hướng từ ngoài vào trong, ngược chiều tăng bán kính.
- Tích phân trường theo bán kính để liên hệ c với V.
- Tính điện trở vi phân $dR=\rho\,dr/(2\pi rL)$, rồi tích phân.

(a) Điện trường hướng xuyên tâm vào trục. (b) Độ lớn:

$$
V=c\int_a^b\frac{dr}{r}
=c\ln\left(\frac{b}{a}\right),
$$

do đó $c=V/\ln(b/a)$.

(c)

$$
\begin{aligned}
R &= \frac{\rho}{2\pi L}\int_a^b\frac{dr}{r} \\
&= \frac{\rho}{2\pi L}\ln\left(\frac{b}{a}\right).
\end{aligned}
$$

(d)

$$
\begin{aligned}
\rho &= \frac{2\pi LR}{\ln(b/a)} \\
&= \frac{2\pi(0{,}0100)(6800)}{\ln 2} \\
&\approx 616\,\Omega\mathrm m.
\end{aligned}
$$
:::

::: exercise 25.76 •••
Một bóng đèn sợi đốt dùng dây tóc tungsten quấn xoắn, dài 580 µm, đường kính 46,0 µm. Ở 20,0 °C, tungsten có điện trở suất $5{,}25\times10^{-8}\,\Omega\mathrm m$. Hệ số nhiệt điện trở suất là $0{,}0045\,(\!^\circ\mathrm C)^{-1}$, được coi không đổi cả ở nhiệt độ cao. Nhiệt độ dây tóc tăng tuyến tính theo dòng, từ 20 °C khi I = 0 đến 2520 °C khi I = 1,00 A. (a) Tìm điện trở ở 20 °C. (b) Tìm dòng khi đặt 120 V vào bóng. Gợi ý: Tìm T(I), rồi R(I), thế vào V=IR. (c) Tìm điện trở khi dùng 120 V. (d) Năng lượng bóng tỏa trong 1 phút ở 120 V là bao nhiêu? (e) Còn khi điện áp bằng một nửa?
:::

<!-- detailed-solution:25.76 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Theo dữ kiện, $T(I)=20+2500I$ °C. Điện trở suất là $\rho(T)=\rho_0[1+\alpha(T-20)]$.

**Hướng đi:**

- Tính $R_0=\rho_0 L/A$ với tiết diện dây tròn.
- Thay quan hệ nhiệt độ theo dòng vào công thức $\rho(T)$. Khi ấy $R(I)=R_0(1+11{,}25I)$.
- Giải phương trình bậc hai $V=IR(I)$ riêng cho 120 V và 60 V.
- Tính điện năng trong một phút từ $W=VIt$, dùng dòng ứng với từng điện áp.

(a) $R_0=\rho_0L/[\pi(d/2)^2]\approx18{,}3\,\Omega$.

(b) Với 120 V:

$$
120=18{,}3 I(1+11{,}25I).
$$

Nghiệm dương là $I\approx0{,}720$ A. (c) Điện trở nóng là $R=120/I\approx167\,\Omega$.

(d) $W=(120)(0{,}720)(60)\approx5{,}18\times10^3$ J. (e) Với 60 V, nghiệm dòng là $I\approx0{,}450$ A, nên $W=(60)(0{,}450)(60)\approx1{,}79\times10^3$ J. Không thể lấy nguyên công suất 120 V rồi chia bốn vì nhiệt độ và điện trở dây tóc cũng giảm khi điện áp giảm.
:::

::: exercise 25.77 ••• CALC
Điện trở suất của bán dẫn thay đổi khi thêm tạp chất. Một thanh bán dẫn dài L, tiết diện A, nằm theo trục x từ 0 đến L, có $\rho(x)=\rho_0e^{-x/L}$. Hai đầu được đặt điện thế sao cho đầu x=0 cao hơn đầu x=L một lượng V₀. (a) Tìm điện trở toàn thanh và dòng điện. (b) Tìm độ lớn điện trường E(x). (c) Tìm điện thế V(x). (d) Vẽ $\rho(x)$, E(x), V(x) trên đoạn từ 0 đến L.
:::

<!-- detailed-solution:25.77 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Tiết diện không đổi, nên các lát dọc thanh mắc nối tiếp. Dòng một chiều ổn định không phụ thuộc x.

**Hướng đi:**

- Tích phân $dR=\rho(x)dx/A$ để tìm R, rồi dùng $I=V_0/R$.
- Dùng $E(x)=\rho(x)I/A$.
- Vì đầu x=0 cao thế hơn, $E_x=-dV/dx>0$. Tích phân từ x đến L với điều kiện V(L)=0.

(a)

$$
\begin{aligned}
R &= \frac{\rho_0}{A}\int_0^L e^{-x/L}\,dx \\
&= \frac{\rho_0L}{A}(1-e^{-1}), \\
I &= \frac{V_0}{R} =\frac{V_0A}{\rho_0L(1-e^{-1})}.
\end{aligned}
$$

(b)

$$
\begin{aligned}
E(x) &= \frac{\rho_0I}{A}e^{-x/L} \\
&= \frac{V_0e^{-x/L}}{L(1-e^{-1})}.
\end{aligned}
$$

Điện trường hướng theo chiều +x. (c) Vì $E_x=-dV/dx$ và $V(L)=0$:

$$
\begin{aligned}
V(x) &= \int_x^L E(s)\,ds \\
&= V_0\frac{e^{-x/L}-e^{-1}}{1-e^{-1}}.
\end{aligned}
$$

(d) Cả $\rho(x)$ và E(x) giảm theo hàm mũ từ trái sang phải. Điện thế giảm đơn điệu từ $V_0$ ở x=0 về 0 ở x=L, theo cùng dạng hàm mũ đã tích phân.
:::

::: exercise 25.78 •••
Một điện trở ngoài R mắc với pin có suất điện động $\mathcal E$ và điện trở trong r. Công suất điện đầu ra của nguồn P bằng công suất tiêu thụ trên R. (a) Tìm giới hạn P khi R rất nhỏ. (b) Tìm giới hạn P khi R rất lớn. (c) Chứng minh P cực đại khi R=r và tìm giá trị cực đại theo $\mathcal E,r$. (d) Pin có $\mathcal E=64{,}0$ V, $r=4{,}00\,\Omega$. Tính P khi R lần lượt bằng 2,00 Ω, 4,00 Ω và 6,00 Ω. Kết quả có phù hợp với câu (b) không?
:::

<!-- detailed-solution:25.78 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Dòng là $I=\mathcal E/(R+r)$, và công suất tải $P=I^2R$.

**Hướng đi:**

- Thay I vào P để có hàm của R, rồi xét hai giới hạn.
- Lấy đạo hàm theo R để tìm điểm dừng, kiểm tra đó là cực đại.
- Thế các dữ kiện số cho ba tải và so với xu hướng khi R lớn.

Ta có:

$$
P(R)=\frac{\mathcal E^2R}{(R+r)^2}.
$$

(a) Khi R tiến về 0, P tiến về 0. (b) Khi R tiến ra vô hạn, P cũng tiến về 0, vì dòng tiến về 0 nhanh hơn R tăng.

(c)

$$
\frac{dP}{dR}
=\frac{\mathcal E^2(r-R)}{(R+r)^3}.
$$

Đạo hàm đổi dấu từ dương sang âm tại $R=r$, nên đó là cực đại:

$$
P_{\max}=\frac{\mathcal E^2}{4r}.
$$

(d) Với dữ kiện đề, $P_{\max}=256$ W. Ba công suất lần lượt là:

$$
\begin{aligned}
P(2\,\Omega) &= 227{,}6\,\mathrm W, \\
P(4\,\Omega) &= 256\,\mathrm W, \\
P(6\,\Omega) &= 245{,}8\,\mathrm W.
\end{aligned}
$$

Khi R lớn hơn r và tăng tiếp, công suất giảm về không, đúng giới hạn câu (b).
:::
