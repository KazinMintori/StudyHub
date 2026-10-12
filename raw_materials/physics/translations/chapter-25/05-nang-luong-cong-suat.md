<!-- Phần 25.5, trang in 828–832. -->

## 25.5 Năng lượng và công suất trong mạch điện

Khi dòng điện đi qua một bộ phận mạch, điện năng có thể biến thành nhiệt, thành hóa năng trong pin sạc, hoặc được cung cấp cho phần còn lại của mạch. Muốn biết bộ phận ấy đang nhận hay cấp năng lượng, ta cần đồng thời xét chiều dòng điện và hiệu điện thế giữa hai đầu.

### Công suất của một phần tử mạch

Xét phần tử mạch nối giữa hai điểm a và b. Gọi

$$
V_{ab}=V_a-V_b
$$

là hiệu điện thế giữa hai đầu và quy ước dòng điện $I$ đi vào đầu a, đi ra đầu b như Hình 25.21. Phần tử có thể là điện trở, pin hoặc linh kiện khác. Khi điện tích $q$ đi qua, độ biến thiên thế năng điện của nó là $qV_{ab}$.

Với điện tích dương và $V_{ab}>0$, điện tích đi từ thế cao $V_a$ xuống thế thấp $V_b$, nên thế năng điện giảm. Điện tích đang chạy trong mạch không tích lũy động năng đều đặn. Dòng điện đi ra khỏi phần tử phải bằng dòng đi vào. Vì vậy, năng lượng $qV_{ab}$ được truyền vào phần tử, chẳng hạn biến thành nhiệt trong dây đốt của lò nướng.

Nếu $V_{ab}<0$, thế tại a thấp hơn thế tại b. Khi dòng điện đi theo chiều quy ước từ a đến b, phần tử cấp năng lượng cho mạch. Pin đang phát điện là ví dụ quen thuộc: Hóa năng trong pin chuyển thành điện năng cung cấp cho mạch ngoài.

Trong khoảng thời gian $dt$, điện lượng đi qua phần tử là $dQ=I\,dt$. Năng lượng truyền vào phần tử bằng $V_{ab}\,dQ$. Chia cho khoảng thời gian, ta được công suất có dấu:

$$
\begin{aligned}
P&=\frac{V_{ab}\,dQ}{dt}\\
&=V_{ab}I.
\end{aligned}
$$

Với quy ước dòng điện đi vào đầu a, $P>0$ nghĩa là phần tử nhận điện năng. Khi $P<0$, phần tử cấp điện năng cho mạch. Đơn vị của công suất là oát vì một vôn bằng một jun trên culông và một ampe bằng một culông trên giây:

$$
1\,\mathrm V\cdot1\,\mathrm A
=1\,\mathrm{J/s}
=1\,\mathrm W.
$$

![Hình 25.21: Quy ước điện áp và dòng điện giữa hai đầu của một phần tử mạch](img/young-25/hinh-25-21.png)

### Điện trở nhận công suất và tỏa nhiệt

Ở điện trở, dòng điện đi vào đầu có điện thế cao hơn. Theo định luật Ôm, $V_{ab}=IR$. Thay vào biểu thức công suất:

$$
\begin{aligned}
P&=V_{ab}I\\
&=I^2R\\
&=\frac{V_{ab}^2}{R}.
\end{aligned}
$$

Công suất này luôn dương với điện trở thụ động. Điện tích truyền năng lượng cho các nguyên tử của vật liệu qua va chạm, làm tăng nội năng. Điện trở nóng lên, truyền nhiệt ra môi trường, hoặc cả hai cùng xảy ra. Ta gọi quá trình đó là tỏa nhiệt Joule.

Mỗi điện trở có công suất định mức, tức công suất lớn nhất mà nó có thể tỏa ra mà không quá nóng và hư hỏng. Thiết bị sưởi được thiết kế để nóng lên, nhưng nếu vượt công suất định mức, thiết bị vẫn có thể nóng chảy hoặc bốc cháy.

### Công suất pin đang cấp cho mạch

Hình 25.22a mô tả nguồn điện có suất điện động $\mathcal E$ và điện trở trong $r$, nối với mạch ngoài bằng dây dẫn lý tưởng. Gọi a là cực có điện thế cao, b là cực có điện thế thấp. Khi pin cấp dòng ra ngoài từ cực dương, điện áp hai cực là:

$$
V_{ab}=\mathcal E-Ir.
$$

Do đó, công suất điện pin đưa ra hai cực là:

$$
\begin{aligned}
P_{\mathrm{ra}}&=V_{ab}I\\
&=\mathcal EI-I^2r.
\end{aligned}
$$

Hạng $\mathcal EI$ là tốc độ chuyển hóa hóa năng thành điện năng trong nguồn. Hạng $I^2r$ là công suất tỏa nhiệt trong điện trở trong. Phần còn lại, $\mathcal EI-I^2r$, là công suất điện thực sự đi ra mạch ngoài. Hình 25.22b liên hệ sơ đồ với pin ô tô cấp điện cho đèn.

![Hình 25.22: Pin có suất điện động và điện trở trong cấp điện cho tải ngoài](img/young-25/hinh-25-22.png)

### Công suất điện đưa vào pin khi sạc

Khi một nguồn có suất điện động lớn hơn đẩy dòng điện vào cực dương của pin nhỏ hơn, chiều dòng qua pin bị đảo so với chế độ phát điện. Đây là mô hình đơn giản của máy phát điện trên xe nạp cho ắc quy như Hình 25.23. Khi dòng đi vào cực dương, điện áp hai cực pin là:

$$
V_{ab}=\mathcal E+Ir.
$$

Công suất điện đi vào pin trở thành:

$$
\begin{aligned}
P_{\mathrm{vào}}&=V_{ab}I\\
&=\mathcal EI+I^2r.
\end{aligned}
$$

Phần $\mathcal EI$ chuyển thành hóa năng có thể lấy ra về sau. Phần $I^2r$ tỏa nhiệt trong pin. Vì vậy pin sạc có thể ấm lên. Mạch nạp phải giới hạn dòng và công suất để tránh quá nhiệt.

![Hình 25.23: Nguồn có suất điện động lớn hơn nạp năng lượng cho pin nhỏ hơn](img/young-25/hinh-25-23.png)

### Ví dụ 25.8: Cân bằng công suất trong mạch kín

Một pin có suất điện động 12 V và điện trở trong 2 Ω cấp dòng 2 A cho điện trở ngoài 4 Ω. Điện áp hai cực pin là 8 V. Tìm tốc độ chuyển hóa hóa năng trong pin, công suất tỏa nhiệt bên trong pin, công suất ra của pin và công suất tỏa nhiệt ở điện trở ngoài.

**Xác định và lập kế hoạch:** Dùng $\mathcal EI$ để tính công suất chuyển hóa hóa năng. Dùng $I^2r$ cho nhiệt trong pin. Phần điện áp hai cực nhân với dòng cho công suất ra. Với điện trở ngoài, dùng $I^2R$.

**Thực hiện:** Tốc độ chuyển hóa hóa năng:

$$
P_{\mathrm{hóa}\to\mathrm{điện}}
=\mathcal EI
=(12\,\mathrm V)(2\,\mathrm A)
=24\,\mathrm W.
$$

Công suất tỏa nhiệt trong pin:

$$
P_r=I^2r
=(2\,\mathrm A)^2(2\,\Omega)
=8\,\mathrm W.
$$

Vậy công suất điện ra của pin là $24-8=16$ W. Điện trở ngoài nhận:

$$
\begin{aligned}
P_R&=V_{a'b'}I\\
&=(8\,\mathrm V)(2\,\mathrm A)\\
&=I^2R\\
&=(2\,\mathrm A)^2(4\,\Omega)\\
&=16\,\mathrm W.
\end{aligned}
$$

**Đánh giá:** Công suất pin cấp ra đúng bằng công suất tỏa ở điện trở ngoài. Cân bằng năng lượng cho toàn mạch là $24\,\mathrm W=8\,\mathrm W+16\,\mathrm W$.

![Hình 25.24: Sơ đồ mạch gồm pin 12 V có điện trở trong 2 Ω và tải 4 Ω](img/young-25/hinh-25-24.png)

### Ví dụ 25.9: Tăng điện trở tải

Giữ pin có $\mathcal E=12$ V, $r=2$ Ω, nhưng thay điện trở ngoài 4 Ω bằng điện trở 8 Ω. Tìm công suất tỏa ở tải và so với mạch trước.

**Xác định và lập kế hoạch:** Điện trở tải lớn hơn làm dòng mạch thay đổi. Vì vậy không thể giữ nguyên I để dùng $I^2R$, cũng không thể giữ nguyên điện áp đầu cực để dùng $V^2/R$. Trước hết tính dòng bằng tổng điện trở.

**Thực hiện:** Dòng mạch là:

$$
I=\frac{\mathcal E}{R+r}
=\frac{12\,\mathrm V}{8\,\Omega+2\,\Omega}
=1{,}2\,\mathrm A.
$$

Điện áp trên tải:

$$
V_{ab}=IR
=(1{,}2\,\mathrm A)(8\,\Omega)
=9{,}6\,\mathrm V.
$$

Do đó:

$$
\begin{aligned}
P_R&=I^2R\\
&=(1{,}2\,\mathrm A)^2(8\,\Omega)\\
&=12\,\mathrm W,\\
P_R&=\frac{V_{ab}^2}{R}\\
&=\frac{(9{,}6\,\mathrm V)^2}{8\,\Omega}\\
&=12\,\mathrm W.
\end{aligned}
$$

Mạch 4 Ω trước đó tỏa 16 W. Tăng tải lên 8 Ω làm công suất tải giảm xuống 12 W. Nếu giữ nhầm dòng cũ 2 A, ta sẽ ước lượng $P=32$ W. Nếu giữ nhầm điện áp cũ 8 V, ta sẽ được 8 W. Cả hai đều sai vì cả dòng và điện áp đầu cực thay đổi khi tải đổi. Dòng giảm quan trọng hơn việc điện trở tăng. Hệ quả tương tự xảy ra ở bóng đèn: bóng định mức 50 W thường có điện trở lớn hơn bóng định mức 100 W khi so ở cùng điện áp danh định.

**Đánh giá:** Công suất hóa năng thành điện năng của pin giảm từ 24 W xuống $14{,}4$ W, còn tổn hao nội tại giảm từ 8 W xuống $2{,}88$ W. Công suất ra còn $14{,}4-2{,}88=11{,}52$ W, phần chênh do làm tròn trong số liệu 12 W đã làm tròn.

### Ví dụ 25.10: Đoản mạch

Hai cực pin có $\mathcal E=12$ V, $r=2$ Ω được nối bằng dây lý tưởng, nên điện trở ngoài bằng không. Dòng ngắn mạch đã xác định là 6 A. Tìm tốc độ chuyển hóa hóa năng, tốc độ tỏa nhiệt bên trong và công suất ra của pin.

**Xác định và lập kế hoạch:** Khi $R=0$, dùng $\mathcal E=Ir$ để kiểm tra dòng điện. Sau đó áp dụng công thức công suất cho nguồn phát.

**Thực hiện:**

$$
\begin{aligned}
P_{\mathrm{hóa}\to\mathrm{điện}}
&=\mathcal EI\\
&=(12\,\mathrm V)(6\,\mathrm A)\\
&=72\,\mathrm W,\\
P_r&=I^2r\\
&=(6\,\mathrm A)^2(2\,\Omega)\\
&=72\,\mathrm W.
\end{aligned}
$$

Công suất ra của nguồn bằng không vì điện áp hai cực pin bằng không khi hai cực bị nối tắt. Toàn bộ năng lượng chuyển hóa bên trong bị tiêu tán trong điện trở trong.

**Đánh giá:** Dây nối tắt lý tưởng cùng ampe kế lý tưởng có thể làm pin hỏng nhanh và quá nóng. Không nối trực tiếp hai cực pin để thử dòng điện.

![Hình 25.25: Pin bị nối tắt ngoài, điện trở ngoài bằng không](img/young-25/hinh-25-25.png)

### Chiến lược giải toán 25.1: Công suất và năng lượng trong mạch

**Nhận diện:** Bài toán có thể hỏi công suất vào/ra từng phần tử hoặc tổng năng lượng trao đổi trong một khoảng thời gian.

**Thiết lập:**

1. Vẽ sơ đồ mạch.
2. Đánh dấu từng phần tử, gồm nguồn điện động và điện trở. Các bài sau có thể thêm tụ điện hoặc cuộn cảm.
3. Liệt kê đại lượng cần tìm: công suất từng phần tử, hoặc năng lượng truyền vào/ra trong một khoảng thời gian.

**Thực hiện:**

1. Nguồn có suất điện động $\mathcal E$ cấp công suất $\mathcal EI$ cho mạch khi dòng đi qua nguồn từ cực − đến cực +. Khi đó nguồn có công suất vào âm và công suất ra dương.
2. Nguồn nhận công suất $\mathcal EI$ từ mạch khi dòng đi qua nguồn từ cực + đến cực −. Khi đó công suất vào nguồn dương, còn công suất ra khỏi nguồn âm. Đây là chế độ sạc.
3. Điện trở luôn nhận công suất và chuyển điện năng thành nhiệt, bất kể chiều dòng:

$$
P_R=VI=I^2R=\frac{V^2}{R}.
$$

Ở đây V là độ lớn hiệu điện thế trên điện trở.

4. Điện trở trong r của nguồn cũng luôn nhận công suất $I^2r$ và tỏa nhiệt, bất kể chiều dòng qua nguồn.
5. Nếu công suất không đổi trong thời gian Δt, năng lượng truyền là $W=P\Delta t$. Nếu P thay đổi theo thời gian, phải tính tích phân theo thời gian.

**Đánh giá:** Kiểm tra bảo toàn năng lượng. Tổng công suất vào có đại số bằng tổng công suất ra. Tương đương, tổng đại số công suất vào mọi phần tử bằng không.

### Câu hỏi kiểm tra ngay sau mục 25.5

Xếp ba mạch sau theo công suất ra thuần của pin từ lớn đến nhỏ.

- (i) Điện trở 1,4 Ω nối pin 1,5 V, điện trở trong 0,10 Ω.
- (ii) Điện trở 1,8 Ω nối pin 4,0 V, điện áp hai cực 3,6 V, điện trở trong chưa biết.
- (iii) Điện trở chưa biết nối pin 12,0 V, điện trở trong 0,20 Ω, điện áp hai cực 11,0 V.

::: details Đáp án và lời giải
**Tóm tắt đề bài:** Cần so công suất đầu cực $P=V_{ab}I$. Với mỗi pin, lấy dòng từ mạch hoặc suy ra từ suất điện động và điện trở trong.

**Hướng đi:**

- (i) Dùng $I=\mathcal E/(R+r)$, rồi nhân điện áp đầu cực với dòng.
- (ii) Dòng đã biết từ mạch trước là 2,0 A.
- (iii) Dùng $V_{ab}=\mathcal E-Ir$ để tìm I.

(i) $I=1{,}5/(1{,}4+0{,}10)=1{,}0$ A, nên $P=1{,}4$ W. (ii) $P=(3{,}6)(2{,}0)=7{,}2$ W. (iii) $I=(12{,}0-11{,}0)/0{,}20=5{,}0$ A, nên $P=55$ W. Thứ tự là (iii), (ii), (i).
:::
