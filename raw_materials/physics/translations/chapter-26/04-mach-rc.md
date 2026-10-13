## 26.4. Mạch R-C

Trong một mạch chỉ gồm nguồn không đổi và điện trở, dòng điện có thể ổn định theo thời gian. Nhưng khi đóng công tắc để nạp tụ điện, dòng ban đầu lớn rồi giảm dần. Muốn mô tả quá trình ấy, ta phải theo dõi đồng thời điện tích trên tụ, hiệu điện thế và dòng điện.

Mạch gồm điện trở $R$ và tụ điện $C$ mắc nối tiếp với nguồn có suất điện động không đổi $\mathcal E$ được gọi là **mạch R-C**. Ta coi nguồn lý tưởng, có điện trở trong bằng không, và bỏ qua điện trở của dây nối. Mạch loại này có trong đèn giao thông nhấp nháy, đèn báo rẽ trên ô tô và đèn chớp điện tử.

### Nạp tụ điện

![Hình 26.20: Mạch R-C trước và sau khi đóng công tắc để nạp tụ](../img/young-26/hinh-26-20.png)

**Hình 26.20:** Trước khi đóng công tắc, tụ chưa tích điện. Sau khi đóng tại $t=0$, điện tích dương tích tụ trên một bản, dòng điện ban đầu lớn rồi giảm dần.

Giả sử tụ ban đầu chưa tích điện. Tại $t=0$, ta đóng công tắc. Vì điện tích ban đầu bằng không, hiệu điện thế trên tụ khi ấy bằng không. Toàn bộ suất điện động đặt lên điện trở, nên dòng điện ban đầu là:

$$
I_0=\frac{\mathcal E}{R}.
$$

Trong mạch nối tiếp, dòng điện có cùng độ lớn tại mọi vị trí. Khi tụ nạp, điện tích trên tụ tăng và hiệu điện thế trên tụ cũng tăng. Do quy tắc vòng kín, độ giảm thế trên điện trở giảm tương ứng, khiến dòng điện giảm. Sau thời gian dài, dòng tiến về không, điện trở không còn độ giảm thế, còn hiệu điện thế trên tụ tiến tới $\mathcal E$.

Để phân biệt đại lượng biến thiên với đại lượng không đổi, ta viết điện áp, dòng và điện tích tức thời bằng chữ thường $v$, $i$, $q$. Ký hiệu viết hoa $V$, $I$, $Q$ dành cho giá trị không đổi hoặc giá trị đặc trưng như dòng ban đầu.

Chọn chiều dòng dương sao cho điện tích dương đi vào bản trái của tụ. Khi ấy $v_{ab}=iR$ là hiệu điện thế trên điện trở và $v_{bc}=q/C$ là hiệu điện thế trên tụ. Áp dụng quy tắc vòng kín:

$$
\begin{aligned}
&\mathcal E-iR-\frac{q}{C} = 0.\end{aligned}
\tag{26.9}
$$

Giải phương trình theo dòng điện, ta được:

$$
\begin{aligned}
&i = \frac{\mathcal E}{R}-\frac{q}{RC}\\
&\quad =\frac{\mathcal E}{R}\left(1-\frac{q}{C\mathcal E}\right).
\end{aligned}
\tag{26.10}
$$

Khi tụ đã nạp ổn định, dòng điện bằng không. Thay $i=0$ vào phương trình vòng kín, điện tích cuối cùng trên tụ là:

$$
Q_f=C\mathcal E.
\tag{26.11}
$$

Điện tích cuối cùng không phụ thuộc điện trở $R$. Điện trở chỉ ảnh hưởng tốc độ nạp.

Để tìm $q$ theo thời gian, dùng $i=dq/dt$ trong phương trình (26.10):

$$
\begin{aligned}
&\frac{dq}{dt} = \frac{\mathcal E}{R}-\frac{q}{RC}\\
&\quad =-\frac{q-C\mathcal E}{RC}.
\end{aligned}
$$

Tách biến rồi lấy tích phân từ trạng thái ban đầu $q=0$, $t=0$ đến điện tích $q$ tại thời điểm $t$:

$$
\begin{aligned}
&\int_0^q\frac{dq'}{q'-C\mathcal E} = -\int_0^t\frac{dt'}{RC}\\
&\ln\left(\frac{q-C\mathcal E}{-C\mathcal E}\right) = -\frac{t}{RC}.
\end{aligned}
$$

Lấy hàm mũ hai vế rồi giải theo $q$, ta được điện tích trên tụ trong quá trình nạp:

$$
\begin{aligned}
&q = C\mathcal E\left(1-e^{-t/(RC)}\right)\\
&\quad =Q_f\left(1-e^{-t/(RC)}\right).
\end{aligned}
\tag{26.12}
$$

Dòng điện là đạo hàm theo thời gian của điện tích:

$$
\begin{aligned}
&i = \frac{dq}{dt}\\
&\quad =\frac{\mathcal E}{R}e^{-t/(RC)}\\
&\quad =I_0e^{-t/(RC)}.
\end{aligned}
\tag{26.13}
$$

Dòng điện bắt đầu ở $I_0=\mathcal E/R$ rồi giảm tiệm cận về không. Điện tích bắt đầu ở không rồi tăng tiệm cận đến $Q_f=C\mathcal E$.

![Hình 26.21: Dòng điện giảm và điện tích tăng trong quá trình nạp tụ](../img/young-26/hinh-26-21.png)

**Hình 26.21:** Đồ thị cho thấy dòng điện $i$ giảm theo thời gian, còn điện tích $q$ tăng về giá trị cuối $Q_f$. Sau một hằng số thời gian, dòng còn $I_0/e$ và tụ đạt $Q_f(1-1/e)$.

### Hằng số thời gian

Tích $RC$ xác định thang thời gian của quá trình nạp. Ta gọi đại lượng này là hằng số thời gian $\tau$ của mạch:

$$
\tau=RC.
\tag{26.14}
$$

Khi $t=\tau$, dòng điện còn $1/e\approx0{,}368$ lần dòng ban đầu. Điện tích trên tụ bằng $(1-1/e)Q_f\approx0{,}632Q_f$. Vì vậy, $\tau$ càng lớn thì tụ nạp càng chậm. Đơn vị của $RC$ là giây.

Về mặt toán học, dòng điện không chạm đúng giá trị không và điện tích không đạt đúng $Q_f$ tại một thời điểm hữu hạn. Cả hai chỉ tiến gần các giới hạn ấy. Sau $10\tau$, phần dòng còn lại và phần điện tích còn thiếu đều xấp xỉ $0{,}000045$ lần giá trị đặc trưng ban đầu hoặc cuối cùng.

![Ứng dụng bộ kích nhịp tim có tụ điện được nạp rồi phóng theo chu kỳ](../img/young-26/ung-dung-may-tao-nhip-tim.png)

**Ứng dụng:** Bộ kích nhịp tim dùng pin, tụ điện và công tắc điều khiển bằng máy tính. Khoảng mỗi giây, công tắc cho tụ phóng để gửi một xung điện qua dây dẫn đến tim, rồi nối tụ vào mạch nạp cho nhịp tiếp theo.

### Ví dụ 26.12: Nạp một tụ điện

Một điện trở $10\,\mathrm{M\Omega}$ mắc nối tiếp với tụ điện $1{,}0\,\mathrm{\mu F}$ và nguồn $12{,}0\,\mathrm V$. Tụ ban đầu chưa tích điện. (a) Tính hằng số thời gian. (b) Tại $t=46\,\mathrm s$, tụ đã đạt bao nhiêu phần điện tích cuối cùng? (c) Dòng điện còn bao nhiêu phần dòng ban đầu?

**Tóm tắt đề bài:** $R=10\,\mathrm{M\Omega}$, $C=1{,}0\,\mathrm{\mu F}$, $\mathcal E=12{,}0\,\mathrm V$, $q(0)=0$ và $t=46\,\mathrm s$.

**Hướng đi:**

- Tính hằng số thời gian bằng $RC$, vì đây là tích điện trở và điện dung của nhánh nối tiếp.
- Dùng phương trình (26.12) cho tỉ số $q/Q_f$ và phương trình (26.13) cho tỉ số $i/I_0$.

**Thực hiện:**

**(a) Hằng số thời gian.**

$$
\begin{aligned}
&\tau = RC\\
&\quad =(10\,\mathrm{M\Omega})(1{,}0\,\mathrm{\mu F})\\
&\quad =10\,\mathrm s.
\end{aligned}
$$

**(b) Phần điện tích cuối cùng đã đạt được.**

$$
\begin{aligned}
&\frac{q}{Q_f} = 1-e^{-t/\tau}\\
&\quad =1-e^{-46/10}\\
&\quad \approx0{,}99.
\end{aligned}
$$

**(c) Phần dòng điện ban đầu còn lại.**

$$
\begin{aligned}
&\frac{i}{I_0} = e^{-t/\tau}\\
&\quad =e^{-46/10}\\
&\quad \approx0{,}010.
\end{aligned}
$$

**Đánh giá:** Sau $4{,}6$ hằng số thời gian, tụ đạt khoảng $99\%$ điện tích cuối cùng, trong khi dòng nạp chỉ còn khoảng $1{,}0\%$ giá trị ban đầu. Giảm điện trở sẽ làm giảm $\tau$ và nạp tụ nhanh hơn.

**Ý chính:** Khi nạp tụ qua điện trở, điện tích tiến đến giá trị cuối còn dòng điện tiến đến không. Cả hai quá trình có cùng hằng số thời gian $RC$.

### Phóng điện qua điện trở

![Hình 26.22: Mạch tụ điện phóng qua điện trở sau khi đóng công tắc](../img/young-26/hinh-26-22.png)

**Hình 26.22:** Trước khi đóng công tắc, tụ có điện tích $Q_0$. Sau khi đóng, điện tích và dòng điện giảm dần. Chiều dòng thực ngược chiều dương đã chọn.

![Hình 26.23: Đồ thị dòng điện và điện tích trong quá trình phóng tụ](../img/young-26/hinh-26-23.png)

**Hình 26.23:** Đồ thị cho thấy điện tích và độ lớn dòng điện phóng đều giảm theo hàm mũ. Với quy ước chiều dương giữ như lúc nạp, dòng phóng mang dấu âm.

Giả sử tụ đã tích điện ban đầu $Q_0$. Ta tháo nguồn rồi nối tụ với điện trở. Giữ quy ước chiều dòng dương giống quá trình nạp. Điện tích dương rời bản dương của tụ, nên dòng thực chạy ngược chiều dương đã chọn.

Khi không còn nguồn trong mạch, quy tắc vòng kín và $i=dq/dt$ cho:

$$
\begin{aligned}
&i = \frac{dq}{dt}\\
&\quad =-\frac{q}{RC}.
\end{aligned}
\tag{26.15}
$$

Tách biến và lấy tích phân với điều kiện đầu $q(0)=Q_0$:

$$
\begin{aligned}
&\int_{Q_0}^{q}\frac{dq'}{q'} = -\int_0^t\frac{dt'}{RC}\\
&\ln\left(\frac{q}{Q_0}\right) = -\frac{t}{RC}.
\end{aligned}
$$

Suy ra điện tích và dòng điện trong quá trình phóng:

$$
\begin{aligned}
&q = Q_0e^{-t/(RC)},\end{aligned}
\tag{26.16}
$$

Tại $t=0$, dòng ban đầu theo quy ước này là $I_0=-Q_0/(RC)$. Dòng tức thời là:

$$
\begin{aligned}
&i = \frac{dq}{dt}\\
&\quad =-\frac{Q_0}{RC}e^{-t/(RC)}\\
&\quad =I_0e^{-t/(RC)}.
\end{aligned}
\tag{26.17}
$$

Dấu âm cho biết dòng phóng ngược chiều dòng dương đã chọn. Độ lớn dòng và điện tích đều tiến về không với cùng hằng số thời gian $\tau=RC$.

#### Ví dụ 26.13: Phóng điện một tụ điện

Điện trở và tụ điện trong Ví dụ 26.12 được mắc lại để phóng điện. Tụ có điện tích ban đầu $Q_0=5{,}0\,\mathrm{\mu C}$. (a) Sau bao lâu điện tích còn $0{,}50\,\mathrm{\mu C}$? (b) Dòng điện khi ấy bằng bao nhiêu?

**Tóm tắt đề bài:** $R=10\,\mathrm{M\Omega}$, $C=1{,}0\,\mathrm{\mu F}$, $Q_0=5{,}0\,\mathrm{\mu C}$ và cần xét lúc $q=0{,}50\,\mathrm{\mu C}$.

**Hướng đi:**

- Dùng $q=Q_0e^{-t/(RC)}$ để tìm thời điểm đạt điện tích đã cho.
- Tại thời điểm đó, dùng trực tiếp tỉ số $q/Q_0$ trong công thức dòng, vì dòng có cùng thừa số mũ.

**Thực hiện:** Hằng số thời gian vẫn là $\tau=10\,\mathrm s$. Từ $q=Q_0e^{-t/\tau}$, thời điểm cần tìm là:

$$
\begin{aligned}
&t = -\tau\ln\left(\frac{q}{Q_0}\right)\\
&\quad =-(10\,\mathrm s)\ln\left(\frac{0{,}50}{5{,}0}\right)\\
&\quad \approx23\,\mathrm s.
\end{aligned}
$$

Tại thời điểm ấy, $q/Q_0=0{,}10$, do đó:

$$
\begin{aligned}
&i = -\frac{Q_0}{\tau}\frac{q}{Q_0}\\
&\quad =-\frac{5{,}0\times10^{-6}\,\mathrm C}{10\,\mathrm s}(0{,}10)\\
&\quad =-5{,}0\times10^{-8}\,\mathrm A.
\end{aligned}
$$

**Đánh giá:** Dòng âm vì chiều thực của dòng phóng ngược chiều dương đã chọn. Tại thời điểm này, điện tích cũng chỉ còn một phần mười giá trị đầu.

**Ý chính:** Điện tích và dòng trong quá trình phóng đều giảm theo hàm mũ với hằng số thời gian $RC$. Dấu của dòng phụ thuộc quy ước chiều đã chọn.

### Cân bằng năng lượng trong mạch R-C

Trong quá trình nạp, nguồn cung cấp công suất tức thời $P_{\mathrm{nguồn}}=\mathcal E i$. Điện trở tỏa nhiệt với công suất $P_R=i^2R$. Tốc độ tăng năng lượng điện trường của tụ là $P_C=i(q/C)$. Nhân phương trình vòng kín (26.9) với $i$, ta thu được:

$$
\begin{aligned}
&\mathcal E i = i^2R+i\frac{q}{C}.\end{aligned}
\tag{26.18}
$$

Phương trình nói rằng công suất nguồn chia thành công suất nhiệt ở điện trở và tốc độ tích trữ năng lượng trong tụ.

Tổng điện tích chuyển từ nguồn sang tụ trong suốt quá trình nạp là:

$$
\begin{aligned}
&\int_0^\infty i\,dt = Q_f\\
&\quad =C\mathcal E.
\end{aligned}
$$

Do đó, tổng năng lượng nguồn cung cấp bằng $\mathcal E Q_f=C\mathcal E^2$. Năng lượng cuối cùng lưu trong tụ là:

$$
U_C=\frac{Q_f^2}{2C}=\frac12 C\mathcal E^2.
$$

Phần còn lại tỏa nhiệt ở điện trở. Vì hai phần bằng nhau, một nửa năng lượng nguồn cấp được lưu trong tụ, một nửa chuyển thành nhiệt, không phụ thuộc $R$, $C$ hay $\mathcal E$.

Ta cũng có thể tính trực tiếp nhiệt lượng tỏa trong điện trở. Đặt $u=t/\tau$, khi đó $dt=\tau\,du$ và $i=(\mathcal E/R)e^{-u}$:

$$
\begin{aligned}
&U_R = \int_0^\infty i^2R\,dt\\
&\quad =\frac{\mathcal E^2\tau}{R}\int_0^\infty e^{-2u}\,du\\
&\quad =\frac{\mathcal E^2\tau}{2R}\\
&\quad =\frac12 C\mathcal E^2.
\end{aligned}
$$

Khi phóng tụ, toàn bộ năng lượng điện trường ban đầu chuyển thành nhiệt trong điện trở. Thật vậy, với $q=Q_0e^{-t/(RC)}$, công suất nhiệt tích lũy là:

Đặt biến không thứ nguyên $u=t/(RC)$, nên $dt=RC\,du$. Khi thay biểu thức dòng điện và đổi biến tích phân, ta được:

$$
\begin{aligned}
&\int_0^\infty i^2R\,dt = \frac{Q_0^2}{C}\int_0^\infty e^{-2u}\,du\\
&\quad =\frac{Q_0^2}{C}\left(\frac12\right)\\
&\quad =\frac{Q_0^2}{2C}.
\end{aligned}
$$

Kết quả đúng bằng năng lượng ban đầu $Q_0^2/(2C)$ của tụ.

#### Kiểm tra hiểu mục 26.4

Năng lượng ban đầu của tụ bằng $Q_0^2/(2C)$. Sau một hằng số thời gian khi đang phóng điện, phần năng lượng còn lại bằng bao nhiêu?

- (i) $1/e$.
- (ii) $1/e^2$.
- (iii) $1-1/e$.
- (iv) $(1-1/e)^2$.
- (v) Kết quả còn phụ thuộc năng lượng ban đầu của tụ.

<details><summary>Lời giải kiểm tra hiểu</summary>

**Tóm tắt:** Sau một hằng số thời gian $t=RC$, điện tích của tụ đã giảm theo phương trình phóng điện.

**Hướng đi:**

- Sau một hằng số thời gian, lấy tỉ số điện tích từ phương trình phóng điện.
- Bình phương tỉ số ấy để có tỉ số năng lượng, vì năng lượng tụ tỉ lệ với $q^2$.

Sau một hằng số thời gian:

$$
\begin{aligned}
&\frac{q}{Q_0} = e^{-t/(RC)}\\
&\quad =e^{-1}.
\end{aligned}
$$

Vì $U=q^2/(2C)$, phần năng lượng còn lại là:

$$
\begin{aligned}
&\frac{U}{U_0} = \left(\frac{q}{Q_0}\right)^2\\
&\quad =\frac1{e^2}\\
&\quad \approx0{,}135.
\end{aligned}
$$

Đáp án là (ii), $1/e^2$, tương ứng khoảng $13{,}5\%$ năng lượng ban đầu.

</details>

### Tóm tắt

- Khi nạp tụ chưa tích điện, dòng ban đầu là $I_0=\mathcal E/R$. Sau thời gian dài, điện tích tiến đến $Q_f=C\mathcal E$ và dòng tiến đến không.
- Trong quá trình nạp, $q=Q_f(1-e^{-t/(RC)})$ và $i=I_0e^{-t/(RC)}$.
- Trong quá trình phóng, $q=Q_0e^{-t/(RC)}$ và dòng có dấu ngược với quy ước chiều nạp.
- Hằng số thời gian là $\tau=RC$. Sau một $\tau$, tụ nạp được khoảng $63{,}2\%$ điện tích cuối hoặc còn khoảng $36{,}8\%$ điện tích ban đầu khi phóng.
- Trong quá trình nạp từ nguồn lý tưởng, một nửa năng lượng nguồn cấp lưu ở tụ và một nửa tỏa nhiệt. Khi phóng, toàn bộ năng lượng ban đầu của tụ tỏa ở điện trở.

### Tài liệu tham khảo

Young, H. D., & Freedman, R. A. *University Physics with Modern Physics* (ấn bản 15, mục 26.4, tr. 858–863). Pearson.
