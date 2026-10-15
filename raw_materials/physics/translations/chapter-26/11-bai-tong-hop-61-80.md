<!-- Source: Problems 26.61–26.80, printed pages 874–876, PDF pages 894–896. -->

## Bài tập tổng hợp 26.61–26.80

::: exercise 26.61
Bộ sạc điện thoại thông thường cung cấp hiệu điện thế $5{,}0\,\mathrm{V}$ và dòng điện $1{,}0\,\mathrm{A}$. (a) Hãy ước lượng đường kính của mỗi dây trong cáp sạc. (b) Xem dây dẫn là đồng có điện trở suất $1{,}72\times10^{-8}\,\Omega\,\mathrm{m}$, hãy tính điện trở trên mỗi mét dây. (c) Nếu điện thoại nhận dòng $1{,}0\,\mathrm{A}$, hiệu điện thế ở điện thoại thấp hơn phía bộ sạc một lượng $IR$. Hãy tính chiều dài cáp làm hiệu điện thế giảm còn $4{,}0\,\mathrm{V}$.
:::

<!-- detailed-solution:26.61 -->
::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Bộ sạc có $5{,}0\,\mathrm{V}$, dòng tải $1{,}0\,\mathrm{A}$, dây đồng có $\rho=1{,}72\times10^{-8}\,\Omega\,\mathrm{m}$. Phần (a) cần một giả thiết về mật độ dòng điện vì đề không quy định đường kính.

**Hướng đi:**

- Chọn mật độ dòng điện thiết kế minh họa $J=5{,}0\,\mathrm{A/mm^2}$. Từ $I=JA$ suy ra diện tích rồi đường kính. Điện trở một dây dài $L$ là $\rho L/A$. Cáp có dây đi và dây về, nên tổng chiều dài kim loại gây sụt áp là $2L$.

(a) Với giả thiết đã nêu, diện tích tiết diện là $A=I/J=0{,}200\,\mathrm{mm^2}$. Tiết diện tròn cho đường kính $d=\sqrt{4A/\pi}=0{,}505\,\mathrm{mm}$. Đây là một ước lượng phụ thuộc giả thiết thiết kế.

(b) Điện trở trên một mét của mỗi lõi:

$$
\begin{aligned}
R' &= \frac{\rho}{A} \\
&= \frac{1{,}72\times10^{-8}}{2{,}00\times10^{-7}} \\
&= 0{,}0860\,\Omega/\mathrm{m}.
\end{aligned}
$$

(c) Mức sụt áp là $1{,}0\,\mathrm{V}$, do đó tổng điện trở vòng dây cần là $1{,}0\,\Omega$. Mỗi mét chiều dài cáp tạo ra $2R'=0{,}172\,\Omega$:

$$
L=\frac{1{,}0\,\Omega}{2(0{,}0860\,\Omega/\mathrm{m})}=5{,}81\,\mathrm{m}.
$$

Vậy chiều dài cáp một chiều xấp xỉ $5{,}8\,\mathrm{m}$ theo giả thiết tiết diện trên. Nếu ký hiệu $R$ trong đề được hiểu là điện trở của riêng một lõi, phép tính hình thức cho $11{,}6\,\mathrm{m}$, nhưng mạch kín thực tế phải tính cả hai lõi.
:::

::: exercise 26.62
(a) Hãy tìm dòng điện qua nguồn và qua từng điện trở trong Hình P26.62. (b) Tính điện trở tương đương của mạng điện trở. Các giá trị trên hình: Nguồn $14{,}0\,\mathrm{V}$, $R_1=1{,}00\,\Omega$, $R_2=2{,}00\,\Omega$, $R_3=1{,}00\,\Omega$, $R_4=2{,}00\,\Omega$, $R_5=1{,}00\,\Omega$.
:::

![Sơ đồ mạch của bài 26.62](img/young-26/hinh-p26-62.png)

<!-- detailed-solution:26.62 -->
::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Hai nhánh trái và phải lần lượt có $R_1,R_4$ và $R_2,R_5$. Điện trở $R_3$ nối hai điểm giữa. Nguồn đặt $14{,}0\,\mathrm{V}$ giữa thanh trên và thanh dưới.

**Hướng đi:**

- Lấy thanh dưới làm mốc $0\,\mathrm{V}$ và thanh trên là $14{,}0\,\mathrm{V}$. Gọi điện thế hai nút giữa là $V_L,V_R$. Viết KCL tại hai nút, giải đồng thời rồi suy ra các dòng nhánh theo định luật Ohm.

$$
\begin{aligned}
\frac{V_L-14}{1} +\frac{V_L}{2} +(V_L-V_R) &= 0, \\
\frac{V_R-14}{2} +V_R +(V_R-V_L) &= 0.
\end{aligned}
$$

Giải hệ được $V_L=8{,}00\,\mathrm{V}$ và $V_R=6{,}00\,\mathrm{V}$. Vì vậy $I_1=6{,}00\,\mathrm{A}$ hướng xuống, $I_4=4{,}00\,\mathrm{A}$ hướng xuống, $I_2=4{,}00\,\mathrm{A}$ hướng xuống, $I_5=6{,}00\,\mathrm{A}$ hướng xuống, còn $I_3=(V_L-V_R)/R_3=2{,}00\,\mathrm{A}$ đi từ trái sang phải. Nguồn cấp $10{,}0\,\mathrm{A}$.

Kiểm tra công suất cho thấy $R_1,R_4,R_2,R_5,R_3$ lần lượt tiêu tán $36,32,32,36,4\,\mathrm{W}$. Tổng là $140\,\mathrm{W}$, bằng công suất nguồn $14{,}0\times10{,}0=140\,\mathrm{W}$.

Do đó dòng $10{,}0\,\mathrm{A}$ đi ra khỏi cực dương nguồn vào mạng ngoài. $R_{eq}=14{,}0/10{,}0=1{,}40\,\Omega$.
:::

::: exercise 26.63
Xét mạch ở Hình P26.63. (a) Suất điện động $\mathcal E$ của nguồn chưa biết phải bằng bao nhiêu để dòng $2{,}00\,\mathrm{A}$ đi qua nguồn $5{,}00\,\mathrm{V}$ theo chiều mũi tên? Cực tính của nguồn $\mathcal E$ có đúng như hình không? (b) Cần bao lâu để điện trở $10{,}0\,\Omega$ tỏa ra $60{,}0\,\mathrm{J}$ nhiệt?
:::

![Sơ đồ mạch của bài 26.63](img/young-26/hinh-p26-63.png)

<!-- detailed-solution:26.63 -->
::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Dòng $2{,}00\,\mathrm{A}$ đi qua pin $5{,}00\,\mathrm{V}$ theo mũi tên. Mạng trên gồm bốn nhánh song song. Cần tìm suất điện động $\mathcal E$, cực tính cần thiết và thời gian tỏa nhiệt ở điện trở $10{,}0\,\Omega$.

**Hướng đi:**

- Đặt điện thế nút trên trái $A$ bằng không. Rút gọn mạng phía trên rồi lần theo sụt áp từ $A$ đến nút dưới phải $D$.
- Dùng cực tính nguồn $5{,}00\,\mathrm{V}$ và chiều dòng đi lên qua điện trở trái $5{,}00\,\Omega$ để tìm nút dưới trái $L$. Sau đó áp dụng KCL tại $D$.
- Dùng KVL trong nhánh $15{,}0\,\Omega$ để tìm $\mathcal E$. Dòng qua nhánh $10+20\,\Omega$ cho phép tính nhiệt ở phần (b).

Điện trở tương đương của mạng trên:

$$
\begin{aligned}
\frac{1}{R_{AB}} &= \frac{1}{30}+\frac{1}{60} +\frac{1}{60}+\frac{1}{30}, \\
R_{AB} &= 10{,}0\,\mathrm{\Omega}.
\end{aligned}
$$

Đặt $V_A=0$. Vì dòng $2{,}00\,\mathrm{A}$ chạy từ $A$ sang $B$, $V_B=-20{,}0\,\mathrm{V}$. Sụt áp trên điện trở ngang $5{,}00\,\Omega$ là $10{,}0\,\mathrm{V}$, nên $V_C=-30{,}0\,\mathrm{V}$. Cực dương nguồn $10{,}0\,\mathrm{V}$ ở trên, do đó $V_D=-40{,}0\,\mathrm{V}$.

Gọi $X$ là nút giữa nguồn $5{,}00\,\mathrm{V}$ và điện trở trái $5{,}00\,\Omega$. Ta có $V_A-V_X=5{,}00\,\mathrm{V}$, nên $V_X=-5{,}00\,\mathrm{V}$. Dòng qua điện trở trái đi lên từ $L$ đến $X$. Vì thế $V_L-V_X=(2{,}00)(5{,}00)=10{,}0\,\mathrm{V}$ và $V_L=+5{,}00\,\mathrm{V}$. Hiệu điện thế nhánh dưới là:

$$
V_D-V_L=-45{,}0\,\mathrm{V}.
$$

Chọn chiều dòng từ phải sang trái ở các nhánh dưới. Khi đó dòng điện trở $20{,}0\,\Omega$ là $I_{20}=(V_D-V_L)/20=-2{,}25\,\mathrm{A}$, tức dòng thực tế hướng sang phải. KCL tại $D$ cho dòng nhánh $15{,}0\,\Omega$ là $I_{15}=2{,}00-I_{20}=4{,}25\,\mathrm{A}$ từ phải sang trái. KVL trong nhánh đó:

$$
\mathcal E = V_D-V_L -15I_{15} = -108{,}75\,\mathrm{V}.
$$

Vậy nguồn cần có độ lớn $108{,}75\,\mathrm{V}$ với cực tính ngược chiều hình vẽ. Dòng qua nhánh $10+20\,\Omega$ là $20/30=0{,}667\,\mathrm{A}$. Phần (b):

$$
t=\frac{60{,}0}{(0{,}667)^2(10{,}0)}=13{,}5\,\mathrm{s}.
$$
:::

::: exercise 26.64
Trong mạch Hình P26.64, $\mathcal E=24{,}0\,\mathrm{V}$, $R_1=6{,}00\,\Omega$, $R_3=12{,}0\,\Omega$, còn $R_2$ thay đổi từ $3{,}00$ đến $24{,}0\,\Omega$. Chọn $R_2$ thế nào để công suất tỏa nhiệt trên bộ phận nung $R_1$ lớn nhất? Tính công suất cực đại.
:::

![Sơ đồ mạch của bài 26.64](img/young-26/hinh-p26-64.png)

<!-- detailed-solution:26.64 -->
::: solution Lời giải chi tiết
**Tóm tắt đề bài:** $R_1$ và $R_2$ mắc song song, tổ hợp này nối tiếp với $R_3$ và nguồn.

**Hướng đi:**

- Dùng phân áp để viết $V_1$ theo $R_2$, sau đó cực đại hóa $P_1=V_1^2/R_1$. Đặt $x=R_2/R_1$ để phương trình gọn.

$$
\begin{aligned}
V_1 &= \mathcal E\frac{R_1R_2/(R_1+R_2)}{R_3+R_1R_2/(R_1+R_2)} \\
&= \mathcal E\frac{R_1R_2}{R_1R_2+R_3R_1+R_3R_2}.
\end{aligned}
$$

Đạo hàm của điện áp nhánh theo $R_2$ dương:

$$
\begin{aligned}
D &= R_1(R_2+R_3)+R_2R_3, \\
K &= \mathcal E R_1^2R_3, \\
\frac{dV_1}{dR_2} &= \frac{K}{D^2}>0.
\end{aligned}
$$

Do đó cực đại tại biên $R_2=24{,}0\,\Omega$. Khi đó $R_1\parallel R_2=4{,}80\,\Omega$, $V_1=24(4{,}80)/(16{,}80)=6{,}857\,\mathrm{V}$ và $P_{1,max}=V_1^2/6=7{,}84\,\mathrm{W}$.
:::

::: exercise 26.65
(a) Hãy lập bảng ước tính năng lượng và chi phí điện trong nhà. Ghi các thiết bị điện, điện áp sử dụng (dùng $240\,\mathrm{V}$ cho bình nước nóng, sưởi chân tường và lò nướng, dùng $120\,\mathrm{V}$ cho thiết bị còn lại), dòng điện, số giờ dùng mỗi ngày, công suất $P=IV$ và điện năng ngày $U=PT$ tính bằng kilowatt-giờ. Cộng điện năng ngày. (b) Tính chi phí tháng bằng cách nhân tổng điện năng ngày với giá $0{,}12\,\mathrm{USD/kWh}$ rồi nhân $30$ ngày.
:::

<!-- detailed-solution:26.65 -->
::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Bảng cần dùng số liệu thực tế của từng hộ gia đình. Đề không cung cấp danh sách thiết bị, dòng tải hay thời gian sử dụng.

**Hướng đi:**

- Điền dữ liệu của gia đình vào bảng mẫu. Đổi watt sang kilowatt trước khi nhân thời gian tính kWh.

Để ghi đủ dữ liệu trên màn hình nhỏ, trước hết lập danh mục thiết bị và điện áp. Sau đó điền một phiếu dữ liệu cho mỗi thiết bị theo mẫu bên dưới.

| Mã và thiết bị | Điện áp (V) |
| --- | ---: |
| 1. Bình nước nóng | 240 |
| 2. Sưởi chân tường | 240 |
| 3. Lò nướng | 240 |
| 4. Thiết bị khác | 120 |

| Đại lượng của một thiết bị | Giá trị cần điền |
| --- | --- |
| Mã và tên thiết bị |  |
| Điện áp, đơn vị V |  |
| Dòng điện, đơn vị A |  |
| Thời gian dùng, đơn vị h/ngày |  |
| Công suất, đơn vị kW |  |
| Điện năng ngày, đơn vị kWh/ngày |  |

Với mỗi thiết bị, tính công suất bằng $P=VI$ rồi đổi sang kilowatt. Điện năng ngày bằng $U=PT$. Cộng điện năng từng hàng để được điện năng ngày của gia đình, ký hiệu $U_{\mathrm{day}}$.

Giá điện là $0{,}12\,\mathrm{USD/kWh}$. Chi phí tháng:

$$
\begin{aligned}
K_{\mathrm{month}} &= 30(0{,}12)U_{\mathrm{day}} \\
&= 3{,}60U_{\mathrm{day}}\,\mathrm{USD}.
\end{aligned}
$$

Không thể cho một tổng số duy nhất nếu chưa có dữ liệu sử dụng trong nhà.
:::

::: exercise 26.66
Trong mạch Hình P26.66, mỗi điện trở có công suất tối đa $2{,}00\,\mathrm{W}$. Suất điện động lớn nhất của nguồn là bao nhiêu để không điện trở nào quá công suất?
:::

![Sơ đồ mạch của bài 26.66](img/young-26/hinh-p26-66.png)

<!-- detailed-solution:26.66 -->
::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Mạch có điện trở nối tiếp $25,30,40\,\Omega$, nhánh song song $25,15,10+(20\parallel20)\,\Omega$, cùng hai điện trở $50\,\Omega$ song song ở nhánh dưới.

**Hướng đi:**

- Gán điện thế cho mọi nút, giải hệ nút, rồi tính công suất từng điện trở theo $P=(V_i-V_j)^2/R$. Tăng $\mathcal E$ đến khi điện trở nguy hiểm nhất đạt $2{,}00\,\mathrm{W}$.

Điện trở tương đương nhóm giữa là $6{,}383\,\Omega$. Toàn mạch:

$$
R_{eq} = 25+30+6{,}383 +40+25 = 126{,}383\,\Omega.
$$

Dòng qua điện trở $40\,\Omega$ lớn nhất về công suất trên mỗi linh kiện. Đặt $I=\sqrt{2/40}=0{,}2236\,\mathrm{A}$ để điện trở này vừa đạt giới hạn. Khi đó $\mathcal E_{max}=IR_{eq}=28{,}3\,\mathrm{V}$. Mỗi điện trở $50\,\Omega$ tiêu tán $0{,}625\,\mathrm{W}$. Hai điện trở nối tiếp $25,30\,\Omega$ tiêu tán $1{,}25$ và $1{,}50\,\mathrm{W}$. Các nhánh song song giữa tiêu tán lần lượt khoảng $0{,}082$, $0{,}136$ và $0{,}102\,\mathrm{W}$.
:::

::: exercise 26.67
Hình P26.67 dùng quy ước không vẽ nguồn. Nút trên ở $36{,}0\,\mathrm{V}$, thanh dưới nối đất. (a) Tìm $V_{ab}=V_a-V_b$ khi công tắc $S$ mở. (b) Tìm dòng qua công tắc khi đóng. (c) Tìm điện trở tương đương khi đóng. Hai nhánh dọc lần lượt là $6{,}00\,\Omega$ trên và $3{,}00\,\Omega$ dưới ở bên trái, $3{,}00\,\Omega$ trên và $6{,}00\,\Omega$ dưới ở bên phải. Điện trở ngang nối $a,b$ là $3{,}00\,\Omega$.
:::

![Sơ đồ mạch của bài 26.67](img/young-26/hinh-p26-67.png)

<!-- detailed-solution:26.67 -->
::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Nguồn lý tưởng giữ thanh trên ở $36\,\mathrm{V}$ và đất ở $0\,\mathrm{V}$.

**Hướng đi:**

- Khi hở, mỗi bên là bộ chia áp riêng. Khi đóng, giải KCL ở hai nút $a,b$. Dòng qua điện trở ngang chính là dòng công tắc.

Khi hở, $V_a=36(3)/(6+3)=12\,\mathrm{V}$ và $V_b=36(6)/(3+6)=24\,\mathrm{V}$, nên $V_{ab}=-12\,\mathrm{V}$. Khi đóng:

$$
\begin{aligned}
\frac{V_a-36}{6} +\frac{V_a}{3} +\frac{V_a-V_b}{3} &= 0, \\
\frac{V_b-36}{3} +\frac{V_b}{6} +\frac{V_b-V_a}{3} &= 0.
\end{aligned}
$$

Suy ra $V_a=15{,}43\,\mathrm{V}$ và $V_b=20{,}57\,\mathrm{V}$. Dòng trong nhánh nối chạy từ $b$ sang $a$, độ lớn $1{,}71\,\mathrm{A}$. Dòng nguồn bằng $8{,}57\,\mathrm{A}$, nên $R_{eq}=36/8{,}57=4{,}20\,\Omega$.
:::

::: exercise 26.68
Ba điện trở giống nhau mắc nối tiếp tiêu tán tổng công suất $45{,}0\,\mathrm{W}$ khi đặt một hiệu điện thế nào đó vào tổ hợp. Nếu mắc ba điện trở song song vào cùng hiệu điện thế ấy, công suất tổng là bao nhiêu?
:::

<!-- detailed-solution:26.68 -->
::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Tổng điện trở nối tiếp là $3R$, còn tổng điện trở song song là $R/3$.

**Hướng đi:**

- Với hiệu điện thế không đổi, $P=V^2/R_{eq}$. Tỉ số hai công suất bằng tỉ số nghịch đảo điện trở tương đương.

$$
\begin{aligned}
\frac{P_{song\ song}}{P_{noi\ tiep}} &= \frac{3R}{R/3}=9, \\
P_{song\ song} &= 9(45{,}0\,\mathrm{W}) \\
&= 405\,\mathrm{W}.
\end{aligned}
$$
:::

::: exercise 26.69
Hai bản tụ có diện tích $A$, cách nhau $d$, được lấp đầy bởi điện môi có hằng số điện môi $K$ và điện trở suất $\rho$. Tụ đã nạp đầy đến suất điện động $\mathcal E$. Khi mở công tắc, tụ rò điện qua điện trở của điện môi mắc song song với tụ. (a) Tìm hằng số thời gian theo các tham số đã cho. Với $A=1{,}00\,\mathrm{cm^2}$, $d=30{,}0\,\mathrm{\mu m}$, $K=8{,}70$, $\rho=3{,}10\times10^{12}\,\Omega\,\mathrm{m}$, $\mathcal E=5{,}00\,\mathrm{V}$, hãy tính (b) điện tích ban đầu, (c) thời điểm điện tích còn một nửa, (d) độ lớn dòng rò khi đó.
:::

![Tụ điện rò của bài 26.69](img/young-26/hinh-p26-69.png)

<!-- detailed-solution:26.69 -->
::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Điện trở xuyên điện môi là $R=\rho d/A$, còn điện dung là $C=K\epsilon_0A/d$.

**Hướng đi:**

- Nhân $R$ với $C$ để thấy diện tích và khoảng cách triệt tiêu. Dùng nghiệm phóng điện mũ cho $q(t)$ và $i(t)$.

$$
\begin{aligned}
\tau &= RC=K\epsilon_0\rho=239\,\mathrm{s}. \\
C &= K\epsilon_0A/d \\
&= 2{,}57\times10^{-10}\,\mathrm{F}, \\
q_0 &= C\mathcal E \\
&= 1{,}29\,\mathrm{nC}, \\
t_{1/2} &= \tau\ln2 \\
&= 166\,\mathrm{s}, \\
i(t_{1/2}) &= q_0/(2\tau) \\
&= 2{,}70\,\mathrm{pA}.
\end{aligned}
$$
:::

::: exercise 26.70
Tụ điện trong Hình P26.70 ban đầu chưa tích điện. Đóng công tắc tại $t=0$. (a) Ngay sau khi đóng, hãy tìm dòng qua mỗi điện trở. (b) Tìm điện tích cuối cùng của tụ. Hình cho $\mathcal E=42{,}0\,\mathrm{V}$, $R_1=8{,}00\,\Omega$, $R_2=6{,}00\,\Omega$, $R_3=3{,}00\,\Omega$, $C=4{,}00\,\mathrm{\mu F}$.
:::

![Sơ đồ mạch của bài 26.70](img/young-26/hinh-p26-70.png)

<!-- detailed-solution:26.70 -->
::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Tụ nối tiếp $R_3$ tạo thành một nhánh song song với $R_2$, còn $R_1$ nối tiếp tổ hợp đó.

**Hướng đi:**

- Phân tích hai mạch giới hạn bằng sơ đồ gốc. Không thể thay tụ bằng cùng một phần tử cho cả hai thời điểm.

Ngay sau khi đóng, tụ tương đương dây dẫn. Khi đó $R_2\parallel R_3=2{,}00\,\Omega$, tổng trở là $10{,}0\,\Omega$ và dòng qua $R_1$ là $4{,}20\,\mathrm{A}$. Điện áp trên các nhánh song song là $8{,}40\,\mathrm{V}$, nên $I_2=1{,}40\,\mathrm{A}$ và $I_3=2{,}80\,\mathrm{A}$. Sau thời gian dài, tụ hở mạch, dòng trong nhánh $R_3$ bằng không. Dòng qua $R_1,R_2$ là $42/(8+6)=3{,}00\,\mathrm{A}$, điện áp trên tụ là điện áp trên $R_2$, bằng $18{,}0\,\mathrm{V}$. Do đó $Q_f=CV_C=72{,}0\,\mathrm{\mu C}$.
:::

::: exercise 26.71
Mạch RC được mắc như Hình P26.71. Tụ có hai bản vuông $2{,}00\,\mathrm{cm}\times2{,}00\,\mathrm{cm}$ song song, cách nhau $3{,}00\,\mathrm{mm}$ và đã nạp đầy. Tại $t=0$, một phiến điện môi kích thước $2{,}00\,\mathrm{cm}\times2{,}00\,\mathrm{cm}\times3{,}00\,\mathrm{mm}$, có hằng số điện môi $K=12{,}0$, được trượt vào giữa hai bản. (a) Điện tích trên bản trên trước khi đưa phiến vào là bao nhiêu? (b) Dòng điện $I$ ngay sau khi phiến được đưa vào là bao nhiêu? (c) Năng lượng trong tụ ngay sau đó là bao nhiêu? (d) Sau một thời gian dài, năng lượng trong tụ tăng thêm bao nhiêu so với giá trị ở phần (c)? (e) Tổng năng lượng pin cung cấp sau khi đưa phiến vào là bao nhiêu? Gợi ý: Tìm $I(t)$ rồi tích phân công suất pin $\int_0^\infty VI(t)\,dt$. (f) Điện trở tiêu tán bao nhiêu năng lượng?
:::

![Mạch và phiến điện môi của bài 26.71](img/young-26/hinh-p26-71.png)

<!-- detailed-solution:26.71 -->
::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Nguồn $10{,}0\,\mathrm{V}$ luôn nối với tụ qua điện trở $10{,}0\,\Omega$. Phiến có $K=12{,}0$ vừa khít khe giữa hai bản vuông.

**Hướng đi:**

- Ban đầu tụ đã đạt $10{,}0\,\mathrm{V}$. Ngay lúc điện môi vào, điện tích tự do chưa kịp đổi, nên điện áp giảm theo tỉ số điện dung. Sau đó dùng nghiệm nạp RC để tính năng lượng và điện năng.

Diện tích là $A=4{,}00\times10^{-4}\,\mathrm{m^2}$ và khoảng cách $d=3{,}00\times10^{-3}\,\mathrm{m}$. Điện dung ban đầu $C_0=1{,}18\times10^{-12}\,\mathrm{F}$. (a) $Q_0=C_0(10{,}0\,\mathrm{V})=1{,}18\times10^{-11}\,\mathrm{C}$. (b) Ngay sau khi trượt, $V_C=10/12=0{,}833\,\mathrm{V}$, vì vậy dòng theo chiều mũi tên là $I=(10-0{,}833)/10=0{,}917\,\mathrm{A}$. (c) Năng lượng tụ ngay sau đó:

$$
U = \frac12(12C_0)(10/12)^2 = 4{,}92\times10^{-12}\,\mathrm{J}.
$$

Sau thời gian dài, năng lượng là $\tfrac12(12C_0)(10)^2=7{,}08\times10^{-10}\,\mathrm{J}$, nên (d) phần tăng là $7{,}03\times10^{-10}\,\mathrm{J}$. (e) Điện tích cuối tăng từ $10C_0$ lên $120C_0$, nên pin cấp $1{,}30\times10^{-9}\,\mathrm{J}$. (f) Dòng giảm mũ từ $I_0=0{,}917\,\mathrm{A}$, do đó năng lượng nhiệt:

$$
\begin{aligned}
U_R &= \int_0^\infty RI^2\,dt \\
&= \frac12(12C_0)(10-10/12)^2 \\
&= 5{,}95\times10^{-10}\,\mathrm{J}.
\end{aligned}
$$
:::

::: exercise 26.72
Tụ $6{,}00\,\mathrm{\mu F}$ ban đầu chưa nạp, mắc nối tiếp với điện trở $5{,}00\,\Omega$ và nguồn $50{,}0\,\mathrm{V}$ lý tưởng. Tại thời điểm điện trở đang tiêu tán công suất $300\,\mathrm{W}$, năng lượng trong tụ là bao nhiêu?
:::

<!-- detailed-solution:26.72 -->
::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Công suất điện trở cho dòng tức thời $I=\sqrt{P/R}=\sqrt{60}=7{,}746\,\mathrm{A}$.

**Hướng đi:**

- Dòng nạp giảm từ $\mathcal E/R=10{,}0\,\mathrm{A}$ về không. Điện áp tụ khi đó là $V_C=\mathcal E-IR$.

$$
\begin{aligned}
V_C &= 50{,}0-(7{,}746)(5{,}00) \\
&= 11{,}27\,\mathrm{V}, \\
U_C &= \frac12CV_C^2 \\
&= 3{,}81\times10^{-4}\,\mathrm{J}.
\end{aligned}
$$
:::

::: exercise 26.73
Nút $a$ trong Hình P26.73 được giữ ở điện thế $400\,\mathrm{V}$ so với đất. Tìm số chỉ của vôn kế mắc giữa $b$ và đất nếu điện trở trong của vôn kế lần lượt là (a) $5{,}00\times10^4\,\Omega$, (b) $5{,}00\times10^6\,\Omega$, (c) vô hạn. Hình có $100\,\mathrm{k\Omega}$ giữa $a,b$ và $200\,\mathrm{k\Omega}$ giữa $b$ và đất.
:::

![Mạch đo điện áp của bài 26.73](img/young-26/hinh-p26-73.png)

<!-- detailed-solution:26.73 -->
::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Vôn kế mắc song song với điện trở $200\,\mathrm{k\Omega}$.

**Hướng đi:**

- Tính điện trở tải song song rồi dùng bộ chia áp giữa $100\,\mathrm{k\Omega}$ và tải tương đương.

$$
\begin{aligned}
R_L &= (200\,\mathrm{k\Omega})\parallel R_V, \\
V_b &= 400\frac{R_L}{100\,\mathrm{k\Omega}+R_L}.
\end{aligned}
$$

Các kết quả lần lượt là $114\,\mathrm{V}$, $263\,\mathrm{V}$ và $267\,\mathrm{V}$. Giới hạn điện trở vôn kế vô hạn khôi phục bộ chia áp không tải $400(200)/(100+200)=266{,}7\,\mathrm{V}$.
:::

::: exercise 26.74
Mạch cầu Wheatstone ở Hình P26.74 dùng các điện trở $M,N,P$ đã biết để xác định điện trở chưa biết $X$. Khi hai công tắc đóng và cầu cân bằng, dòng qua điện kế bằng không. (a) Chứng minh $X=MP/N$. (b) Tính $X$ nếu $M=850{,}0\,\Omega$, $N=15{,}00\,\Omega$, $P=33{,}48\,\Omega$.
:::

![Cầu Wheatstone của bài 26.74](img/young-26/hinh-p26-74.png)

<!-- detailed-solution:26.74 -->
::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Khi cầu cân bằng, hai nút giữa có cùng điện thế và không có dòng qua nhánh điện kế.

**Hướng đi:**

- So sánh sụt áp trên mỗi nhánh nối tiếp. Tỉ số điện trở trên và dưới của hai nhánh bằng nhau.

$$
\begin{aligned}
\frac{N}{M} &= \frac{P}{X}, \\
X &= \frac{MP}{N} \\
&= 1{,}897\times10^3\,\Omega.
\end{aligned}
$$
:::

::: exercise 26.75
(Xem bài 26.67.) (a) Tìm điện thế của điểm $a$ so với điểm $b$ trong Hình P26.75 khi công tắc $S$ mở. (b) Điểm nào có điện thế cao hơn? (c) Tìm điện thế cuối cùng của điểm $b$ so với đất khi đóng $S$. (d) Điện tích trên mỗi tụ thay đổi bao nhiêu? Nút trên cùng được giữ ở $18{,}0\,\mathrm{V}$ so với đất. Nhánh trái có điện trở $6{,}00\,\Omega$ và tụ $3{,}00\,\mathrm{\mu F}$. Nhánh phải có tụ $6{,}00\,\mathrm{\mu F}$ và điện trở $3{,}00\,\Omega$. Công tắc nối các điểm giữa hai nhánh.
:::

![Mạch tụ của bài 26.75](img/young-26/hinh-p26-75.png)

<!-- detailed-solution:26.75 -->
::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Trước khi đóng công tắc, điện trở không có dòng một chiều. Vì vậy $V_a=18\,\mathrm{V}$, $V_b=0$.

**Hướng đi:**

- Khi hở, mỗi nhánh là bộ chia điện dung nối tiếp. Khi đóng, hai điểm giữa trở thành một nút chung. Tổng điện tích trên nút cô lập được bảo toàn.

Do đó (a) $V_{ab}=18{,}0\,\mathrm{V}$ và (b) điểm $a$ cao thế hơn. Trước khi đóng, bản trên của tụ $3\,\mathrm{\mu F}$ mang $+54\,\mathrm{\mu C}$, bản dưới của tụ $6\,\mathrm{\mu F}$ mang $-108\,\mathrm{\mu C}$, nên điện tích tổng trên hai phần dẫn được nối với nhau là $-54\,\mathrm{\mu C}$. Sau khi đóng, bảo toàn điện tích trên nút chung:

$$
6(V_b-18)+3V_b=-54,
$$

trong đó điện dung tính bằng $\mathrm{\mu F}$ và điện tích bằng $\mathrm{\mu C}$. Suy ra (c) $V_b=6{,}00\,\mathrm{V}$. Tụ $6\,\mathrm{\mu F}$ giảm điện tích từ $108$ xuống $72\,\mathrm{\mu C}$, còn tụ $3\,\mathrm{\mu F}$ giảm từ $54$ xuống $18\,\mathrm{\mu C}$. Độ biến thiên độ lớn điện tích mỗi tụ là $36{,}0\,\mathrm{\mu C}$.
:::

::: exercise 26.76
Điện trở $R=850\,\Omega$ được mắc vào hai bản của tụ đã tích điện $C=4{,}62\,\mathrm{\mu F}$. Ngay trước khi nối, điện tích tụ là $6{,}90\,\mathrm{\mu C}$. (a) Tính năng lượng ban đầu của tụ. (b) Tính công suất tỏa nhiệt trong điện trở ngay sau khi nối. (c) Tính công suất khi năng lượng tụ còn một nửa giá trị ban đầu.
:::

<!-- detailed-solution:26.76 -->
::: solution Lời giải chi tiết
**Tóm tắt đề bài:** $V_0=Q_0/C$ và $U_0=Q_0^2/(2C)$. Trong quá trình phóng, công suất điện trở là $V_C^2/R$.

**Hướng đi:**

- Tính điện áp ban đầu, rồi dùng $U\propto V_C^2$ để tìm điện áp ở thời điểm năng lượng còn một nửa.

$$
\begin{aligned}
V_0 &= Q_0/C \\
&= 1{,}494\,\mathrm{V}, \\
U_0 &= Q_0^2/(2C) \\
&= 5{,}15\,\mathrm{\mu J}, \\
P(0^+) &= V_0^2/R \\
&= 2{,}62\,\mathrm{mW}, \\
P(U_0/2) &= P(0^+)/2 \\
&= 1{,}31\,\mathrm{mW}.
\end{aligned}
$$
:::

::: exercise 26.77
Tụ chưa nạp mắc nối tiếp với điện trở và nguồn lý tưởng $110\,\mathrm{V}$. Ngay sau khi đóng mạch, dòng điện là $6{,}5\times10^{-5}\,\mathrm{A}$. Hằng số thời gian của mạch là $5{,}2\,\mathrm{s}$. Tìm điện trở và điện dung.
:::

<!-- detailed-solution:26.77 -->
::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Ban đầu tụ tương đương dây dẫn, nên $I_0=\mathcal E/R$. Đồng thời $\tau=RC$.

**Hướng đi:**

- Tính $R$ từ dòng ban đầu rồi chia hằng số thời gian cho $R$.

$$
\begin{aligned}
R &= \frac{110}{6{,}5\times10^{-5}} \\
&= 1{,}69\,\mathrm{M\Omega}, \\
C &= \frac{5{,}2}{R} \\
&= 3{,}07\,\mathrm{\mu F}.
\end{aligned}
$$
:::

::: exercise 26.78
Mạch trong Hình 26.22a có $R=196\,\Omega$. Đóng công tắc tại $t=0$ và đo độ lớn dòng $i$ theo thời gian. Đồ thị $\ln i$ theo $t$ trong Hình P26.78. (a) Giải thích vì sao các điểm gần nằm trên đường thẳng. (b) Dùng đồ thị để tìm $C$ và điện tích ban đầu $Q_0$. (c) Khi $i=0{,}0500\,\mathrm{A}$, điện tích trên tụ là bao nhiêu? (d) Khi $q=0{,}500\times10^{-4}\,\mathrm{C}$, dòng điện là bao nhiêu?
:::

![Đồ thị bài 26.78](img/young-26/hinh-p26-78.png)

<!-- detailed-solution:26.78 -->
::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Dòng phóng điện tuân theo $i=i_0e^{-t/RC}$, do đó $\ln i=\ln i_0-t/(RC)$.

**Hướng đi:**

- Hệ số góc của đường thẳng là $-1/(RC)$, còn tung độ gốc là $\ln i_0$. Dùng $Q_0=RCi_0$ và $q=RCi$.

Đọc đường thích ứng với các điểm cho độ dốc xấp xỉ $-0{,}64\,\mathrm{ms^{-1}}$ và tung độ gốc xấp xỉ $-2{,}08$. Suy ra $RC=1{,}56\,\mathrm{ms}$, $i_0=e^{-2{,}08}=0{,}125\,\mathrm{A}$, $C=RC/R=7{,}97\,\mathrm{\mu F}$ và $Q_0=RCi_0=1{,}95\times10^{-4}\,\mathrm{C}$. Các giá trị phù hợp độ chính xác đọc từ đồ thị.

(c) Dùng $q=RCi$ với $i=0{,}0500\,\mathrm{A}$:

$$
\begin{aligned}
q &= (1{,}56\,\mathrm{ms})(0{,}0500\,\mathrm{A}) \\
&= 7{,}81\times10^{-5}\,\mathrm{C}.
\end{aligned}
$$

(d) Khi $q=0{,}500\times10^{-4}\,\mathrm{C}$, $i=q/(RC)=0{,}0320\,\mathrm{A}$.
:::

::: exercise 26.79
Mạch ở Hình 26.20 có tụ $C=5{,}00\times10^{-6}\,\mathrm{F}$. Sau khi đóng công tắc, đo điện tích $q$ theo dòng $i$ và thu được bảng số liệu. Dòng $i$ (mA) bằng $56{,}0$, $48{,}0$, $40{,}0$, $32{,}0$, $24{,}0$, còn $q$ ($\mathrm{\mu C}$) bằng $10{,}1$, $19{,}8$, $30{,}2$, $40{,}0$, $49{,}9$. (a) Vẽ $q$ theo $i$, giải thích dạng gần tuyến tính, tìm hệ số góc và giao điểm. (b) Từ đó tính $R$ và suất điện động $\mathcal E$. (c) Khi nào điện áp tụ bằng $10{,}0\,\mathrm{V}$? (d) Khi điện áp tụ là $4{,}00\,\mathrm{V}$, điện áp điện trở bằng bao nhiêu?
:::

<!-- detailed-solution:26.79 -->
::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Khi nạp tụ, $q=C(\mathcal E-iR)$, nên đồ thị $q(i)$ là đường thẳng có hệ số góc $-CR$ và giao điểm $C\mathcal E$.

**Hướng đi:**

- Hồi quy tuyến tính các cặp dữ liệu. Sau đó lấy $R=-m/C$ và $\mathcal E=b/C$. Điện áp tụ tăng theo $V_C=\mathcal E(1-e^{-t/RC})$.

![Đồ thị lời giải 26.79: Điện tích theo dòng điện trong quá trình nạp](img/young-26/hinh-giai26-79-dien-tich-dong-dien.svg)

Các điểm đo gần nằm trên đường thẳng có hệ số góc âm. Đường thẳng khớp dùng toàn bộ năm cặp số liệu.

Hồi quy dữ liệu cho hệ số góc $m=-1{,}2475\,\mathrm{\mu C/mA}$ và giao điểm $b=79{,}9\,\mathrm{\mu C}$. Đổi hệ số góc sang đơn vị SI:

$$
m=-1{,}2475\times10^{-3}\,\mathrm{C/A}.
$$

Suy ra $R=249{,}5\,\Omega$ và $\mathcal E=15{,}98\,\mathrm{V}$. Với $V_C=10{,}0\,\mathrm{V}$:

$$
\begin{aligned}
t &= -RC\ln\left(1-\frac{10{,}0}{15{,}98}\right) \\
&= 1{,}23\,\mathrm{ms}.
\end{aligned}
$$

(d) Theo KVL, điện áp điện trở là $15{,}98-4{,}00=11{,}98\,\mathrm{V}$, xấp xỉ $12{,}0\,\mathrm{V}$.
:::

::: exercise 26.80
Một công ty có hai điện trở $R_1,R_2$ mắc sẵn thành hai tổ hợp nối tiếp và song song, không thể tách riêng. Mỗi tổ hợp được nối riêng với nguồn lý tưởng $48{,}0\,\mathrm{V}$. Công suất nguồn là $48{,}0\,\mathrm{W}$ cho nối tiếp và $256\,\mathrm{W}$ cho song song. Biết $R_1>R_2$. (a) Tìm hai điện trở. (b) Trong tổ hợp nối tiếp, điện trở nào tiêu tán công suất lớn hơn? (c) Trong tổ hợp song song, điện trở nào tiêu tán công suất lớn hơn?
:::

<!-- detailed-solution:26.80 -->
::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Hai phép đo cho $R_1+R_2=48^2/48=48\,\Omega$ và $R_1\parallel R_2=48^2/256=9\,\Omega$.

**Hướng đi:**

- Tích hai điện trở là $R_1R_2=9(R_1+R_2)=432\,\Omega^2$. Giải phương trình bậc hai rồi dùng $P=I^2R$ cho nối tiếp và $P=V^2/R$ cho song song.

$$
R^2-48R+432=0
$$

Hai nghiệm là $36\,\Omega$ và $12\,\Omega$. Vì $R_1>R_2$, $R_1=36\,\Omega$, $R_2=12\,\Omega$. Trong nối tiếp, dòng như nhau nên $R_1$ tiêu tán công suất lớn hơn. Trong song song, điện áp như nhau nên $R_2$ tiêu tán công suất lớn hơn.
:::
