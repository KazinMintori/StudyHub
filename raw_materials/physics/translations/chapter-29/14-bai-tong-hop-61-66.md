## Bài toán tổng hợp 29.61–29.66

::: exercise 29.61
Trong một vùng tròn bán kính $R$, từ trường đều hướng vào mặt hình và tăng với tốc độ $dB/dt$. Vùng ấy có thể là tiết diện bên trong ống dây dài. Tìm độ lớn và hướng lực lên điện tích điểm dương $q$ đứng yên tại ba điểm. Điểm $a$ cách tâm $r$ về phía trên, $b$ cách tâm $r$ về phía phải, $c$ ở tâm, với $r<R$.

![Hình P29.61: Ba điện tích đứng yên trong vùng từ trường hướng vào trang đang tăng.](img/young-29/hinh-p29-61.png)
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Điện tích đứng yên không chịu lực từ, nhưng có thể chịu lực điện do điện trường cảm ứng.

**Hướng đi:**

- Dùng đối xứng tròn và Faraday để tìm điện trường tiếp tuyến.
- Từ thông vào trang tăng nên điện trường có chiều tuần hoàn ngược kim đồng hồ.
- Dùng $\vec F=q\vec E$, không dùng lực từ vì vận tốc điện tích bằng không.

Với đường tròn bán kính $r<R$,

$$
\begin{aligned}
2\pi rE&=\pi r^2\frac{dB}{dt},\\
F&=qE=\frac{qr}{2}\frac{dB}{dt}.
\end{aligned}
$$

Tại $a$, tiếp tuyến dương hướng sang trái, nên lực hướng trái. Tại $b$, tiếp tuyến hướng lên, nên lực hướng lên. Hai lực có cùng độ lớn đã tính. Tại $c$, đối xứng cho $E=0$, nên lực bằng không.
:::

::: exercise 29.62
Thanh khối lượng $M=1{,}20\,\mathrm{kg}$, điện trở $R=0{,}500\,\Omega$ trượt không ma sát trên ray chữ U nằm ngang, bề rộng $W=40{,}0\,\mathrm{cm}$. Bỏ qua điện trở ray. Thanh nối lò xo độ cứng $k=90{,}0\,\mathrm{N/m}$. Trường đều $1{,}00\,\mathrm T$ hướng vào mặt hình. Tại $t=0$, kéo thanh lệch khỏi cân bằng $10{,}0\,\mathrm{cm}$ rồi thả từ nghỉ.

![Hình P29.62: Thanh trượt nối lò xo, chuyển động trong từ trường và tạo dòng làm dao động tắt dần.](img/young-29/hinh-p29-62.png)

(a) Tìm hệ số cản $b$ trong phương trình dao động tắt dần.

(b) Tìm tần số dao động.

(c) Tìm biên độ tại $t=5{,}00\,\mathrm s$.

(d) Tìm độ lớn dòng trong thanh khi đi qua vị trí cân bằng lần đầu.

(e) Tìm chiều dòng ở thời điểm ấy.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** $x(0)=x_0=0{,}100\,\mathrm m$, $\dot x(0)=0$. Lực từ có dạng $-b\dot x$, do dòng cảm ứng trong mạch.

**Hướng đi:**

- Tìm dòng $I=BW|\dot x|/R$ rồi lực cản từ $F_B=BWI$ để xác định $b$.
- Giải phương trình tắt dần với đúng hai điều kiện ban đầu. Không lấy nghiệm cosin đơn thuần nếu muốn giữ điều kiện thả từ nghỉ chính xác.
- Tìm lần đầu $x=0$, lấy đạo hàm để có tốc độ, rồi suy dòng.

(a)

$$
\begin{aligned}
&M\ddot x+b\dot x+kx=0,\\
&b=\frac{B^2W^2}{R}\\
&=0{,}320\,\mathrm{kg/s}.
\end{aligned}
$$

(b) Đặt $\alpha=b/(2M)$ và $\omega_0^2=k/M$. Tần số góc tắt dần và tần số là

$$
\begin{aligned}
\alpha&=0{,}1333\,\mathrm{s^{-1}},\\
\omega_d&=\sqrt{\omega_0^2-\alpha^2}\\
&=8{,}659\,\mathrm{rad/s},\\
f&=\frac{\omega_d}{2\pi}=1{,}38\,\mathrm{Hz}.
\end{aligned}
$$

(c) Nghiệm đúng điều kiện ban đầu là

$$
\begin{aligned}
&x(t)=x_0e^{-\alpha t}\cos\omega_dt\\
&\quad+x_0e^{-\alpha t}\frac{\alpha}{\omega_d}\sin\omega_dt.
\end{aligned}
$$

Viết tổng trong ngoặc thành một cosin có pha, hệ số biên độ tại thời gian $t$ là

$$
\begin{aligned}
&A(t)=x_0e^{-\alpha t}\\
&\quad\times\sqrt{1+\left(\frac\alpha{\omega_d}\right)^2}.
\end{aligned}
$$

Tại $5{,}00\,\mathrm s$, $A=0{,}05135\,\mathrm m\approx5{,}13\,\mathrm{cm}$. Vì cản yếu, xấp xỉ $A\approx x_0e^{-\alpha t}$ cho cùng kết quả ở ba chữ số có nghĩa.

(d) Lần qua cân bằng đầu tiên thỏa mãn

$$
\begin{aligned}
\omega_dt_1&=\frac\pi2+\arctan\frac\alpha{\omega_d},\\
t_1&=0{,}18318\,\mathrm s.
\end{aligned}
$$

Đạo hàm nghiệm cho

$$
\dot x(t)=-x_0e^{-\alpha t}
\frac{\omega_0^2}{\omega_d}\sin\omega_dt.
$$

Do đó $|\dot x(t_1)|=0{,}845\,\mathrm{m/s}$ và

$$
\begin{aligned}
&I(t_1)\\
&=\frac{BW|\dot x(t_1)|}{R}\\
&=0{,}676\,\mathrm A.
\end{aligned}
$$

(e) Thanh đang đi về phía trái. Với trường vào trang, lực từ lên điện tích dương hướng xuống dọc thanh. Dòng trong thanh chạy từ trên xuống.
:::

::: exercise 29.63
Một điện môi lý tưởng, không có tính từ, điện thẩm $3{,}5\times10^{-11}\,\mathrm{F/m}$ lấp đầy khe tụ. Dòng dẫn qua điện môi bằng không. Với $t>0$, thông lượng điện là

$$
\Phi_E=(8{,}0\times10^3\,\mathrm{V\,m/s^3})t^3.
$$

Khi nào dòng dịch bằng $21\,\mu\mathrm A$?
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** $\varepsilon=3{,}5\times10^{-11}\,\mathrm{F/m}$. Dòng dịch mục tiêu là $21\times10^{-6}\,\mathrm A$.

**Hướng đi:**

- Lấy đạo hàm thông lượng trong định nghĩa dòng dịch.
- Giải nghiệm thời gian dương vì đề xét $t>0$.

$$
\begin{aligned}
i_D&=\varepsilon\frac{d\Phi_E}{dt}\\
&=\varepsilon(2{,}4\times10^4\,\mathrm{V\,m/s^3})t^2.
\end{aligned}
$$

Thay dòng mục tiêu rồi giải theo $t$ cho $t=5{,}0\,\mathrm s$.
:::

::: exercise 29.64
Để đo từ trường của một nam châm điện lớn, đặt giữa hai cực một cuộn nhỏ 4 vòng, bán kính $0{,}800\,\mathrm{cm}$, điện trở $0{,}250\,\Omega$. Mặt cuộn song song mặt các cực như Hình 29.5. Trường ban đầu bằng không và tăng khi dòng nam châm điện tăng. Dòng cảm ứng qua cuộn đo được như đồ thị, luôn cùng một chiều.

![Hình P29.64: Dòng cảm ứng tăng tuyến tính đến 3,00 mA ở 2,00 s, giữ đến 5,00 s rồi giảm về không ở 6,00 s.](img/young-29/hinh-p29-64.png)

Tính trường ở cuộn tại (a) $2{,}00\,\mathrm s$, (b) $5{,}00\,\mathrm s$, (c) $6{,}00\,\mathrm s$.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Trường vuông góc cuộn. Đồ thị cho dòng cảm ứng, tức tốc độ biến thiên trường, không cho trực tiếp trường.

**Hướng đi:**

- Dùng $NA\,dB/dt=Ri(t)$ cho các độ lớn, vì trường tăng và dòng giữ chiều.
- Tích phân từ 0 đến thời điểm xét. Giá trị tích phân là diện tích dưới đồ thị dòng.

$$
B(t)=\frac R{N\pi r^2}\int_0^t i(t')\,dt'.
$$

(a) Diện tích tam giác đến 2,00 s bằng $3{,}00\times10^{-3}\,\mathrm{A\,s}$, nên

$$
B(2{,}00\,\mathrm s)=0{,}933\,\mathrm T.
$$

(b) Từ 2 đến 5 s thêm hình chữ nhật diện tích $9{,}00\times10^{-3}\,\mathrm{A\,s}$. Tổng bằng $12{,}0\times10^{-3}\,\mathrm{A\,s}$, nên

$$
B(5{,}00\,\mathrm s)=3{,}73\,\mathrm T.
$$

(c) Từ 5 đến 6 s thêm tam giác diện tích $1{,}50\times10^{-3}\,\mathrm{A\,s}$. Tổng là $13{,}5\times10^{-3}\,\mathrm{A\,s}$, nên

$$
B(6{,}00\,\mathrm s)=4{,}20\,\mathrm T.
$$

Dòng trở về không ở 6 s nghĩa là trường ngừng tăng, không phải trường trở về không.
:::

::: exercise 29.65
Thanh kim loại dài $6{,}00\,\mathrm{cm}$, khối lượng $0{,}200\,\mathrm{kg}$ trượt không ma sát trên hai ray nối qua điện trở $0{,}800\,\Omega$. Bỏ qua điện trở ray và thanh. Trường đều hướng vào mặt hình. Truyền cho thanh vận tốc ban đầu $20{,}0\,\mathrm{cm/s}$ sang phải rồi thả. Chỉ lực từ tác dụng lên thanh theo phương chuyển động. Đo độ lớn gia tốc theo tốc độ được các cặp dữ liệu sau.

| $v$ (cm/s) | $a$ (cm/s²) |
| ---: | ---: |
| 20,0 | 6,2 |
| 16,0 | 4,9 |
| 14,0 | 4,3 |
| 12,0 | 3,7 |
| 10,0 | 3,1 |
| 8,0 | 2,5 |

![Hình P29.65: Thanh đi sang phải, điện trở bên trái có đầu a ở trên và b ở dưới.](img/young-29/hinh-p29-65.png)

(a) Vẽ $a$ theo $v$, giải thích vì sao các điểm gần đường thẳng và tìm hệ số góc đường khớp tốt nhất.

(b) Dùng đồ thị suy độ lớn từ trường.

(c) Khi thanh chuyển động, đầu nào của điện trở có điện thế cao hơn?

(d) Mất bao lâu để tốc độ giảm từ $20{,}0$ xuống $10{,}0\,\mathrm{cm/s}$?
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Mô hình lực từ cản cho độ lớn gia tốc tỉ lệ tốc độ. Dữ liệu có sáu cặp, cần dùng cả sáu khi khớp.

**Hướng đi:**

- Dùng $ma=B^2L^2v/R$ để suy ý nghĩa hệ số góc.
- Khớp tuyến tính tất cả dữ liệu. Dùng hệ số góc, còn tung độ gốc nhỏ chỉ phản ánh đường khớp dữ liệu.
- Giải $dv/dt=-sv$ để tìm thời gian giảm tốc.

(a) Mô hình cho

$$
a=sv,\qquad s=\frac{B^2L^2}{mR}.
$$

Khớp đường $a=sv+c$ cho toàn bộ sáu điểm trong SI được

$$
\begin{aligned}
s&=0{,}30714\,\mathrm{s^{-1}},\\
c&=2{,}14\times10^{-4}\,\mathrm{m/s^2}.
\end{aligned}
$$

Các điểm gần đường thẳng vì lực cản từ tỉ lệ tốc độ trong mô hình này.

![Lời giải 29.65: Sáu số đo gia tốc theo tốc độ và đường thẳng khớp toàn bộ dữ liệu.](img/young-29/hinh-giai29-65.svg)

(b)

$$
B=\frac{\sqrt{smR}}L=3{,}69\,\mathrm T.
$$

(c) Điện tích dương bị lực từ đẩy lên trong thanh. Dòng qua điện trở bên trái đi từ $a$ xuống $b$, nên $a$ có điện thế cao hơn.

(d) Dùng mô hình vật lý $dv/dt=-sv$, tốc độ giảm theo $v=v_0e^{-st}$. Vì thế

$$
\begin{aligned}
&t\\
&=\frac{\ln(v_0/v)}s\\
&=\frac{\ln2}s\\
&=2{,}26\,\mathrm s.
\end{aligned}
$$
:::

::: exercise 29.66
Đo lực ngoài cần để kéo đều một vòng chữ nhật ra khỏi vùng trường đều hướng ra mặt hình. Vòng dài $14{,}0\,\mathrm{cm}$ theo hướng chuyển động, cao $8{,}00\,\mathrm{cm}$ và có điện trở $4{,}00\times10^{-3}\,\Omega$. Vòng giữ nguyên hình dạng.

| $v$ (cm/s) | $F$ (N) |
| ---: | ---: |
| 2,0 | 0,10 |
| 4,0 | 0,21 |
| 6,0 | 0,31 |
| 8,0 | 0,41 |
| 10,0 | 0,52 |

![Hình P29.66: Vòng chữ nhật được kéo ra ngoài sang phải, cạnh thẳng đứng dài 8,00 cm còn trong trường.](img/young-29/hinh-p29-66.png)

(a) Vẽ $F$ theo $v$, giải thích dạng gần đường thẳng và tìm hệ số góc khớp tốt nhất.

(b) Tìm độ lớn từ trường.

(c) Dòng cảm ứng có chiều nào?

(d) Tìm tốc độ tiêu tán điện năng khi $v=5{,}00\,\mathrm{cm/s}$.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** $L=0{,}0800\,\mathrm m$ là chiều dài cạnh vuông góc chuyển động. Thanh bên dài 14 cm không phải chiều dài dùng trong $BLv$.

**Hướng đi:**

- Kéo đều nên lực ngoài bằng lực từ hãm, $F=B^2L^2v/R$.
- Khớp tất cả năm điểm để tìm hệ số góc, rồi suy trường.
- Dùng Lenz cho chiều dòng và bảo toàn công suất để tìm nhiệt.

(a) Khớp $F=sv+c$ với $v$ đo bằng m/s cho

$$
\begin{aligned}
s&=5{,}20\,\mathrm{N\,s/m},\\
c&=-0{,}0020\,\mathrm N.
\end{aligned}
$$

Mô hình lý tưởng có tung độ gốc bằng không và hệ số góc $s=B^2L^2/R$.

![Lời giải 29.66: Năm số đo lực kéo theo tốc độ và đường thẳng khớp toàn bộ dữ liệu.](img/young-29/hinh-giai29-66.svg)

(b)

$$
B=\frac{\sqrt{sR}}L=1{,}80\,\mathrm T.
$$

(c) Từ thông ra trang giảm nên dòng tạo trường ra trang, chạy ngược kim đồng hồ.

(d) Với $v=0{,}0500\,\mathrm{m/s}$,

$$
\begin{aligned}
P&=I^2R=Fv\\
&=sv^2=1{,}30\times10^{-2}\,\mathrm W.
\end{aligned}
$$
:::
