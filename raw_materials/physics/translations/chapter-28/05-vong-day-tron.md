## 28.5 Từ trường trên trục của vòng dây tròn mang dòng điện

Một vòng dây có thể tạo từ trường mạnh khi dòng điện đủ lớn, và cuộn nhiều vòng còn cộng hưởng tác dụng của từng vòng. Để tính trường tại một điểm không nằm ngay trên dây, ta cộng đóng góp của mọi phần tử dòng điện. Với vòng tròn, đối xứng giúp phép cộng ấy rút về một thành phần duy nhất trên trục.

![Nam châm điện dùng cuộn dây mang dòng để nâng các thanh thép và vật chứa sắt](../img/young-28/hinh-28-11.png)

Hình 28.11: Cuộn dây nhiều vòng tạo từ trường đủ mạnh để nâng các vật bằng sắt.

### Thiết lập hình học và trường vi phân

Xét vòng dây bán kính $a$ nằm trong mặt phẳng $yz$, có tâm tại $O$. Trục của vòng là trục $x$. Điểm khảo sát $P$ nằm trên trục, cách tâm một khoảng $x$. Phần tử dây $d\vec l$ tiếp tuyến với vòng và vuông góc với vectơ nối phần tử đến $P$.

Dòng điện được đưa vào và ra vòng qua hai dây thẳng dài đặt sát nhau, mang dòng ngược chiều. Ở vùng khảo sát, trường do hai dây dẫn này gần triệt tiêu nhau. Vì thế ta tập trung vào trường do đoạn vòng tròn tạo ra.

![Phân tích trường vi phân do một phần tử của vòng dây tạo ra tại điểm trên trục](../img/young-28/hinh-28-12.png)

Hình 28.12: Thành phần dọc trục của các vectơ $d\vec B$ cộng lại, còn thành phần ngang triệt tiêu theo cặp.

Theo định luật Biot–Savart, độ lớn trường do phần tử dòng điện gây ra là:

$$
dB=\frac{\mu_0}{4\pi}\frac{I\,dl}{r^2}.
\tag{28.12}
$$

Trong hình học này, $r^2=x^2+a^2$. Hướng $d\vec B$ vuông góc với cả $d\vec l$ và vectơ từ phần tử đến điểm $P$. Phân tích $d\vec B$ thành thành phần theo trục $x$ và thành phần trong mặt phẳng vòng:

Vì $r^2=x^2+a^2$, góc trong hình cho $\cos\theta=a/r$. Thành phần theo trục là:

$$
dB_x=dB\cos\theta.
$$

Thay $dB$ từ (28.12) và $\cos\theta=a/r$:

$$
dB_x=\frac{\mu_0I a\,dl}{4\pi r^3}.
\tag{28.13}
$$

Thành phần vuông góc trục dùng $\sin\theta=x/r$:

$$
dB_{\perp}=dB\sin\theta
=\frac{\mu_0I x\,dl}{4\pi r^3}.
\tag{28.14}
$$

Ký hiệu $dB_{\perp}$ chỉ thành phần vuông góc trục $x$, không phải thành phần theo một phương cố định duy nhất. Với mỗi phần tử có một phần tử đối diện. Hai thành phần $dB_{\perp}$ ngược hướng nên triệt tiêu, còn hai thành phần $dB_x$ cùng hướng nên cộng lại. Sau khi cộng quanh cả vòng, tổng trường chỉ còn theo trục $x$.

### Tích phân quanh vòng và trường trên trục

Trong biểu thức $dB_x$, các đại lượng $I$, $a$, $x$ và $r$ không đổi khi chạy quanh vòng. Chỉ còn $dl$ thay đổi. Ta lấy tích phân trên toàn chu vi:

$$
\begin{aligned}
&B_x = \oint dB_x\\
&\quad =\frac{\mu_0 I a}{4\pi(x^2+a^2)^{3/2}}\oint dl\\
&\quad =\frac{\mu_0 I a}{4\pi(x^2+a^2)^{3/2}}(2\pi a)\\
&\quad =\frac{\mu_0 I a^2}{2(x^2+a^2)^{3/2}}.
\end{aligned}
\tag{28.15}
$$

Chiều của $\vec B$ được xác định bằng quy tắc bàn tay phải. Khum các ngón theo chiều dòng điện trên vòng. Ngón cái duỗi ra chỉ chiều trường trên trục.

![Quy tắc bàn tay phải xác định chiều trường trên trục vòng dây](../img/young-28/hinh-28-13.png)

Hình 28.13: Ngón cái chỉ chiều từ trường khi các ngón tay khum theo chiều dòng điện.

![Đồ thị độ lớn từ trường dọc trục của cuộn dây tròn nhiều vòng](../img/young-28/hinh-28-14.png)

Hình 28.14: Trường đạt cực đại tại tâm và giảm xấp xỉ theo $1/|x|^3$ khi điểm khảo sát ở rất xa vòng dây.

Nếu cuộn dây có $N$ vòng giống nhau, đặt sát nhau để có thể coi các vòng cùng bán kính và cùng mặt phẳng, các trường cùng chiều nên độ lớn nhân $N$:

$$
B_x=\frac{\mu_0NIa^2}{2(x^2+a^2)^{3/2}}.
\tag{28.16}
$$

Tại tâm vòng dây, $x=0$. Vì vậy trường tại tâm cuộn $N$ vòng là:

$$
B_x(0)=\frac{\mu_0NI}{2a}.
\tag{28.17}
$$

Mẫu số của biểu thức (28.16) nhỏ nhất khi $x=0$, nên độ lớn trường trên trục lớn nhất ở tâm. Nếu $|x|\gg a$, ta có $(x^2+a^2)^{3/2}\approx |x|^3$. Do đó trường giảm xấp xỉ theo nghịch đảo lập phương khoảng cách. Đây là lý do một cuộn dây có mômen từ lớn vẫn tạo trường yếu ở điểm rất xa.

### Liên hệ với mômen lưỡng cực từ

Diện tích vòng dây là $A=\pi a^2$. Mômen lưỡng cực từ của một vòng có độ lớn $\mu=IA$, còn cuộn $N$ vòng có $\mu=NIA$. Thay $NIA$ bằng $\mu$ trong (28.16), ta được:

$$
B_x=\frac{\mu_0\mu}{2\pi(x^2+a^2)^{3/2}}.
\tag{28.18}
$$

Trên trục, chiều trường của vòng giống chiều vectơ mômen từ. Biểu thức này chỉ mô tả các điểm trên trục của vòng hoặc cuộn dây. Không được dùng nó cho một điểm bất kỳ nằm ngoài trục.

![Các đường sức của từ trường do vòng dây tròn tạo ra](../img/young-28/hinh-28-15.png)

Hình 28.15: Đường sức khép kín quanh vòng dây. Trên trục, trường cùng chiều mômen lưỡng cực từ.

### Ứng dụng: Nam châm trong máy chụp cộng hưởng từ

![Cuộn dây nam châm trong hệ thống chụp cộng hưởng từ](../img/young-28/ung-dung-mri-28.png)

Ứng dụng MRI: Bệnh nhân nằm bên trong cuộn dây tạo từ trường mạnh.

Máy chụp cộng hưởng từ thường cần trường cỡ $1{,}5\,\mathrm T$. Dòng điện lớn tạo ra nhiệt đáng kể trong dây cuộn. Vì vậy cuộn nam châm được làm lạnh bằng helium lỏng ở nhiệt độ $4{,}2\,\mathrm K$ để hạn chế quá nhiệt.

### Ví dụ 28.6: Trường của một cuộn dây nhiều vòng

Cuộn dây có $N=100$ vòng tròn, bán kính $a=0{,}60\,\mathrm m$, mang dòng $I=5{,}0\,\mathrm A$.

**(a) Tính trường tại điểm trên trục cách tâm cuộn $x=0{,}80\,\mathrm m$.** Dùng (28.16), vì điểm khảo sát nằm trên trục:

$$
\begin{aligned}
&B_x = \frac{\mu_0NIa^2}{2(x^2+a^2)^{3/2}}\\
&\quad =2\pi\times10^{-7}\frac{180}{(1{,}00)^{3/2}}\\
&\quad =1{,}13\times10^{-4}\,\mathrm T\\
&\quad \approx1{,}1\times10^{-4}\,\mathrm T.
\end{aligned}
$$

**(b) Tìm các vị trí trên trục nơi trường có độ lớn bằng một phần tám trường tại tâm.** Tỉ số trường tại $x$ so với trường ở tâm là:

$$
\frac{B_x(x)}{B_x(0)}
=\frac{a^3}{(x^2+a^2)^{3/2}}.
$$

Đặt tỉ số bằng $1/8$. Vì hai vế dương, nâng lũy thừa $2/3$ không đổi dấu bất đẳng thức hay loại nghiệm:

$$
\begin{aligned}
&\frac{a^3}{(x^2+a^2)^{3/2}} = \frac18\\
&(x^2+a^2)^{3/2} = 8a^3\\
&x^2+a^2 = 4a^2\\
&x = \pm\sqrt3\,a\\
&\quad =\pm1{,}04\,\mathrm m.
\end{aligned}
$$

Hai vị trí đối xứng qua tâm. Kiểm tra độc lập tại tâm cho $B_x(0)=5{,}24\times10^{-4}\,\mathrm T$. Một phần tám giá trị này là $6{,}55\times10^{-5}\,\mathrm T$, khớp với trường của (28.16) tại $x=\pm\sqrt3a$.

Mômen từ của cuộn là:

$$
\begin{aligned}
&\mu = NIA=N I\pi a^2\\
&\quad =100(5{,}0)\pi(0{,}60)^2\\
&\quad =5{,}65\times10^2\,\mathrm{A\,m^2}\\
&\quad \approx5{,}7\times10^2\,\mathrm{A\,m^2}.
\end{aligned}
$$

Thay mômen này vào (28.18) cũng cho $1{,}13\times10^{-4}\,\mathrm T$ tại $x=0{,}80\,\mathrm m$. Mômen từ khá lớn nhưng trường thu được tại điểm xa vẫn chỉ cùng cỡ trường Trái Đất.

### Tự kiểm tra 28.5

![Hình học các thành phần trường do những phần tử khác nhau trên vòng dây tạo ra](../img/young-28/hinh-28-12.png)

**(a)** Ở điểm $P$ trên trục, phần tử ở đỉnh vòng tạo các thành phần $dB_x>0$, $dB_y>0$, $dB_z=0$. Hãy tìm dấu của các thành phần do phần tử ở đáy vòng, trên trục $y$ âm.

**(b)** Hãy tìm dấu của các thành phần do phần tử ở mép phải vòng, trên trục $z$ âm.

**Đáp án và lập luận:** (a) Chọn $d\vec l=-\hat k\,dl$ và $\vec r=x\hat i+a\hat j$. Khi đó:

Vì $(-\hat k)\times\hat i=-\hat j$ và $(-\hat k)\times\hat j=\hat i$, nên:

$$
d\vec l\times\vec r=dl(a\hat i-x\hat j).
$$

Vì vậy $dB_x>0$, $dB_y<0$, $dB_z=0$, tức lựa chọn (ii). (b) Với phần tử ở trục $z$ âm, $d\vec l=\hat j\,dl$ và $\vec r=x\hat i+a\hat k$. Tích có hướng cho thành phần $x$ dương, thành phần $z$ âm và thành phần $y$ bằng không. Do đó đáp án là (v), vì không lựa chọn nào trong danh sách nêu đúng bộ dấu ấy.
