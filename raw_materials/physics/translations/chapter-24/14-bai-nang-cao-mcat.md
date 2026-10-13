<!-- Bài 24.69–24.72 và MCAT 24.73–24.76. Nguồn: trang in 810–811. -->

## Bài tập thử thách

::: exercise 24.69 •• DỮ LIỆU
Bạn khảo sát một tụ điện phẳng chứa không khí. Tụ được nối với nguồn điện có hiệu điện thế 24,0 V. Ban đầu khoảng cách giữa hai bản là 0,0500 cm. Trong thí nghiệm thứ nhất, bạn giữ tụ nối với nguồn, tăng khoảng cách giữa hai bản và đo năng lượng lưu trong tụ ở mỗi khoảng cách. Trong thí nghiệm thứ hai, bạn làm tương tự nhưng ngắt nguồn trước khi thay đổi khoảng cách. Hình P24.69 cho một tập dữ liệu, với năng lượng $U$ được biểu diễn theo $1/d$. (a) Tập dữ liệu thuộc thí nghiệm nào: giữ tụ nối với nguồn hay ngắt nguồn trước khi thay đổi $d$? Giải thích. (b) Dùng đồ thị để tính diện tích $A$ của mỗi bản tụ. (c) Khi $d=0{,}400$ cm, trường hợp nào có năng lượng lưu trong tụ lớn hơn? Giải thích.
:::

![Hình P24.69: Đồ thị năng lượng U theo nghịch đảo khoảng cách giữa hai bản tụ](img/young-24/hinh-p24-69.png)

<!-- detailed-solution:24.69 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Tụ không khí có hiệu điện thế ban đầu 24,0 V. Đồ thị biểu diễn $U$ theo $1/d$, trong đó $U$ tính theo $10^{-9}$ J và $1/d$ theo cm⁻¹.

**Hướng đi:**

- Viết $U$ theo $C$ và nhận ra $C$ tỉ lệ nghịch với $d$. Giữ $V$ không đổi làm $U$ tỉ lệ với $1/d$, còn giữ $Q$ không đổi làm $U$ tỉ lệ với $d$.
- Đọc độ dốc đồ thị, đổi đúng đơn vị từ $\mathrm{J}/(\mathrm{cm}^{-1})$ sang $\mathrm{J\,m}$, rồi so với hệ số của công thức năng lượng.
- Với tụ không khí, dùng $C=\varepsilon_0A/d$. Khi ngắt nguồn, $Q$ không đổi trong lúc kéo hai bản ra.

(a) Dữ liệu ứng với thí nghiệm giữ tụ nối với nguồn. Thật vậy, khi $V$ không đổi:

$$
\begin{aligned}
&U = \frac12CV^2\\
&\quad =\frac{\varepsilon_0AV^2}{2d}.
\end{aligned}
$$

Vì vậy $U$ tuyến tính theo $1/d$. Nếu tụ bị ngắt khỏi nguồn, Q không đổi và:

$$
\begin{aligned}
&U = \frac{Q^2}{2C}\\
&\quad =\frac{Q^2d}{2\varepsilon_0A}.
\end{aligned}
$$

nên $U$ tuyến tính theo d, không phải theo $1/d$.

(b) Độ dốc đọc từ đồ thị xấp xỉ 3,67 đơn vị tung độ cho mỗi đơn vị hoành độ. Do trục đứng dùng 10⁻⁹ J còn trục ngang dùng cm⁻¹:

$$
\begin{aligned}
&m = 3{,}67\frac{10^{-9}\,\mathrm J}{\mathrm{cm}^{-1}}\\
&\quad =3{,}67\times10^{-11}\,\mathrm{J\,m}.
\end{aligned}
$$

So sánh với $U=(\varepsilon_0AV^2/2)(1/d)$, ta có $m=\varepsilon_0AV^2/2$. Do đó:

$$
\begin{aligned}
&A = \frac{2m}{\varepsilon_0V^2}\\
&\quad =\frac{7{,}34\times10^{-11}}{5{,}100\times10^{-9}}\,\mathrm{m^2}\\
&\quad \approx1{,}44\times10^{-2}\,\mathrm{m^2}\\
&\quad \approx144\,\mathrm{cm^2}.
\end{aligned}
$$

(c) Khi nguồn vẫn nối, V không đổi và $U$ tỉ lệ nghịch với $d$. Khi ngắt nguồn, $Q$ không đổi và $U$ tỉ lệ thuận với d. Hai trường hợp có cùng $U$ tại khoảng cách ban đầu. Vì $0{,}400$ cm lớn gấp tám lần $0{,}0500$ cm, năng lượng tăng tám lần ở trường hợp ngắt nguồn, nhưng giảm còn một phần tám ở trường hợp vẫn nối nguồn. Vậy tụ đã ngắt nguồn có năng lượng lớn hơn.
:::

::: exercise 24.70 ••• THỬ THÁCH
Một trụ dẫn đặc bán kính $a$ đặt đồng trục bên trong một trụ dẫn rỗng thành mỏng bán kính $b$. Cả hai có chiều dài $L$. Giữa chúng có một vỏ trụ điện môi rắn, bán kính trong $a$, bán kính ngoài $R$ và hằng số điện môi $K$. Vỏ có thể trượt dọc trục giữa hai trụ dẫn. Các trụ được nối bằng dây dẫn với hai cực của một nguồn điện duy trì hiệu điện thế $V$. Gọi $x$ là chiều dài vỏ điện môi đã trượt vào vùng giữa hai trụ. (a) Tìm điện dung theo $x$. (b) Với $L=10{,}0$ cm, $a=1{,}00$ cm, $b=4{,}00$ cm, $R=3{,}00$ cm và $K=3{,}21$, tính điện dung khi $x=0$. (c) Tính điện dung khi $x=L$. (d) Khi $V=1{,}00$ kV, chiều dài $x$ nào làm điện tích trên trụ dương bằng 6,00 nC? Bỏ qua hiệu ứng mép.
:::

![Hình P24.70: Hai trụ dẫn đồng trục và vỏ điện môi trượt vào khe giữa chúng](img/young-24/hinh-p24-70.png)

<!-- detailed-solution:24.70 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Bán kính thỏa $a<R<b$. Đoạn dài $x$ có điện môi từ a đến R và không khí từ R đến b. Đoạn dài $L-x$ chỉ chứa không khí từ a đến b. Bỏ qua hiệu ứng mép và xem trường gần như không phụ thuộc vị trí dọc trục.

**Hướng đi:**

- Với một lát đồng trục dài ℓ, điện môi từ a đến R và không khí từ R đến b mắc nối tiếp theo phương xuyên tâm. Hai hiệu điện thế xuyên tâm cộng lại.
- Các đoạn dọc trục cùng nối vào hai trụ dẫn nên có cùng hiệu điện thế. Điện dung của chúng cộng như các nhánh song song.
- Dùng $Q=CV$ để chuyển yêu cầu điện tích thành điện dung cần có, rồi giải phương trình tuyến tính theo $x$.

Một lát đồng trục thuần không khí dài ℓ có điện dung $2\pi\varepsilon_0\ell/\ln(b/a)$. Với lát có điện môi, cùng điện tích tuyến tính theo chiều dài đi qua cả hai miền xuyên tâm. Vì $E_r=\lambda/(2\pi\varepsilon_0K r)$ trong điện môi và $E_r=\lambda/(2\pi\varepsilon_0r)$ trong không khí, hiệu điện thế của lát là:

$$
\begin{aligned}
&V = \int_a^R\frac{\lambda}{2\pi\varepsilon_0K r}\,dr\\
&\quad+\int_R^b\frac{\lambda}{2\pi\varepsilon_0 r}\,dr\\
&\quad =\frac{\lambda}{2\pi\varepsilon_0K}\ln\frac Ra\\
&\quad+\frac{\lambda}{2\pi\varepsilon_0}\ln\frac bR.
\end{aligned}
$$

Vì điện tích trên trụ trong của lát có độ lớn $Q=\lambda\ell$, điện dung lát có điện môi là:

$$
\begin{aligned}
&C_D(\ell) = \frac{Q}{V}\\
&\quad =\frac{2\pi\varepsilon_0\ell}{\ln(R/a)/K+\ln(b/R)}.
\end{aligned}
$$

Đặt điện dung trên một đơn vị chiều dài của phần không khí và phần có điện môi lần lượt là:

$$
\begin{aligned}
&c_a = \frac{2\pi\varepsilon_0}{\ln(b/a)},\\
&c_D = \frac{2\pi\varepsilon_0}{\ln(R/a)/K+\ln(b/R)}.
\end{aligned}
$$

(a) Hai đoạn dọc trục mắc song song vì cùng chịu hiệu điện thế $V$. Do đó:

$$
C(x)=c_a(L-x)+c_Dx.
$$

(b) Khi x = 0, toàn khe chứa không khí:

$$
\begin{aligned}
&C(0) = \frac{2\pi\varepsilon_0L}{\ln(b/a)}\\
&\quad \approx4{,}01\,\mathrm{pF}.
\end{aligned}
$$

(c) Khi x = L, toàn chiều dài được lấp theo cấu hình điện môi và không khí xuyên tâm:

$$
\begin{aligned}
&C(L) = \frac{2\pi\varepsilon_0L}{\ln(R/a)/K+\ln(b/R)}\\
&\quad \approx8{,}83\,\mathrm{pF}.
\end{aligned}
$$

(d) Điện dung cần có là $C_{\mathrm{yc}}=Q/V=6{,}00\,\mathrm{pF}$. Từ $C(x)$,

$$
\begin{aligned}
&x = \frac{C_{\mathrm{yc}}-c_aL}{c_D-c_a}\\
&\quad \approx0{,}0412\,\mathrm m\\
&\quad =4{,}12\,\mathrm{cm}.
\end{aligned}
$$

Giá trị này nằm trong đoạn $0\le x\le L$, như yêu cầu hình học.
:::

::: exercise 24.71 ••• TÍNH TOÁN
Hai bản dẫn có diện tích $A$, cách nhau khoảng $d$. Hằng số điện môi thay đổi tuyến tính theo chiều vuông góc hai bản, từ 1 ở sát bản này đến $K$ ở sát bản kia. (a) Tìm điện dung của tụ. Gợi ý: Có thể xem hệ như một dãy liên tục các tụ vi phân mắc nối tiếp. Nghịch đảo điện dung của lát có bề dày $dx$ là $dx/[K(x)\varepsilon_0A]$, trong đó $K(x)$ là hằng số điện môi tại vị trí đó. (b) Chứng minh kết quả trở về công thức đúng khi $K$ tiến đến 1.
:::

<!-- detailed-solution:24.71 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Chọn tọa độ $x$ từ bản có hằng số điện môi 1 đến bản có hằng số K. Giả sử $K\ge1$ và điện môi thay đổi đều theo $x$.

**Hướng đi:**

- Ghi $K(x)$ theo nội suy tuyến tính giữa hai giá trị ở hai mặt.
- Vì các lát mỏng mắc nối tiếp, cộng nghịch đảo điện dung của từng lát, không cộng điện dung trực tiếp.
- Tính tích phân logarit và kiểm tra giới hạn $K\to1$ bằng giới hạn $\ln K/(K-1)\to1$.

Hằng số điện môi ở vị trí $x$ là:

$$
K(x)=1+\frac{K-1}{d}x.
$$

Với lát mỏng bề dày $dx$, nghịch đảo điện dung là $dx/[\varepsilon_0A K(x)]$. Các lát mắc nối tiếp nên:

$$
\begin{aligned}
&\frac1C = \frac1{\varepsilon_0A}\int_0^d\frac{dx}{K(x)}\\
&\quad =\frac1{\varepsilon_0A}\int_0^d\frac{dx}{1+(K-1)x/d}\\
&\quad =\frac{d}{\varepsilon_0A(K-1)}\int_1^K\frac{du}{u}\\
&\quad =\frac{d\ln K}{\varepsilon_0A(K-1)}.
\end{aligned}
$$

(a) Vì thế:

$$
C=\frac{\varepsilon_0A(K-1)}{d\ln K}.
$$

(b) Khi $K$ tiến đến 1, dùng $\lim_{K\to1}(K-1)/\ln K=1$:

$$
\lim_{K\to1}C=\frac{\varepsilon_0A}{d},
$$

đúng bằng điện dung của tụ không khí có cùng hình học.
:::

::: exercise 24.72 ••• THỬ THÁCH
Hai bản dẫn hình vuông cạnh $L$ cách nhau $D$. Một tấm điện môi hằng số $K$, kích thước $L\times L\times D$, được đưa một phần vào khoảng giữa hai bản như Hình P24.72. Gọi $x$ là chiều dài tấm đã đi vào, với $0\le x\le L$. (a) Tìm điện dung $C$ của hệ. (b) Nếu tụ nối với nguồn giữ hiệu điện thế $V$ không đổi, khi đưa tấm vào thêm một đoạn $dx$, hãy chứng minh công thức sau:

$$
dU=+\frac{(K-1)\varepsilon_0V^2L}{2D}\,dx.
$$

(c) Nếu trước khi dịch tấm một đoạn $dx$, tụ được ngắt khỏi nguồn để điện tích trên bản không đổi, tìm độ lớn điện tích trên mỗi bản và chứng minh năng lượng thay đổi một lượng trái dấu với kết quả câu (b). (d) Gọi $F$ là lực điện do các điện tích tác dụng lên tấm. Công chống lại lực này khi dịch tấm một đoạn $dx$ là $-Fdx$. Hãy dùng kết quả câu (b), rồi câu (c), để xác định chiều lực mà mỗi kết quả gợi ra. (e) Hình 24.16 cho thấy lực thực tế kéo tấm vào trong tụ. Giải thích vì sao suy luận ở câu (b) cho sai chiều lực, rồi tính độ lớn lực. Cách tính không cần biết cấu trúc của trường loe ở mép.
:::

![Hình P24.72: Tấm điện môi trượt một phần vào giữa hai bản tụ hình vuông](img/young-24/hinh-p24-72.png)

<!-- detailed-solution:24.72 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Phần tấm chồng lên bản có diện tích $Lx$, còn phần diện tích $L(L-x)$ chứa không khí. Giả sử hiệu ứng mép không làm thay đổi đáng kể điện dung.

**Hướng đi:**

- Hai vùng điện môi và không khí nằm cạnh nhau theo diện tích, cùng chịu hiệu điện thế giữa hai bản, nên điện dung cộng song song.
- Với nguồn nối, $V$ cố định và $U=\frac{1}{2}CV^2$. Với tụ ngắt nguồn, $Q$ cố định và $U=Q^2/(2C)$.
- Khi $V$ cố định, năng lượng pin trao đổi với tụ cũng thay đổi. Không thể xem riêng độ tăng năng lượng điện trường là công cơ học cần thiết.

(a) Hai vùng có điện dung:

$$
\begin{aligned}
&C_D = \frac{K\varepsilon_0Lx}{D},\\
&C_a = \frac{\varepsilon_0L(L-x)}D.
\end{aligned}
$$

Cộng hai nhánh song song:

$$
C(x)=\frac{\varepsilon_0L}{D}\left[L+(K-1)x\right].
$$

(b) Khi V không đổi, $U=\frac{1}{2}CV^2$, vì vậy:

$$
\begin{aligned}
&dU = \frac12V^2dC\\
&\quad =+\frac{(K-1)\varepsilon_0V^2L}{2D}\,dx.
\end{aligned}
$$

(c) Trước khi ngắt nguồn, điện tích có độ lớn $Q=C(x)V$, tức:

$$
Q=\frac{\varepsilon_0L}{D}\left[L+(K-1)x\right]V.
$$

Sau khi ngắt, $Q$ giữ nguyên. Vi phân $U=Q^2/(2C)$ theo $C$ cho $dU=-Q^2dC/(2C^2)$. Vì $Q/C=V$ ở trạng thái ngay trước khi dịch tấm:

$$
\begin{aligned}
&dU = -\frac12V^2dC\\
&\quad =-\frac{(K-1)\varepsilon_0V^2L}{2D}\,dx.
\end{aligned}
$$

(d) Nếu xem độ tăng năng lượng ở câu (b) là công cơ học chống lại lực điện, thì $dU=-Fdx$ cho $F$ âm, tức lực đẩy tấm ra ngoài. Câu (c) cho $dU<0$, nên $F=-dU/dx>0$, tức lực kéo tấm vào trong. Hai suy luận trái nhau vì ở câu (b), pin vẫn trao đổi năng lượng với tụ.

(e) Khi tấm đi vào, điện dung tăng một lượng $dC$ và điện tích từ pin tăng $dQ=VdC$. Công pin truyền cho hệ tụ là:

$$
\begin{aligned}
&dW_{\mathrm{pin}} = VdQ\\
&\quad =V^2dC.
\end{aligned}
$$

Phần năng lượng điện trường chỉ tăng $dU=V^2dC/2$. Bảo toàn năng lượng cho công cơ học ngoài:

$$
\begin{aligned}
&dW_{\mathrm{ext}} = dU-dW_{\mathrm{pin}}\\
&\quad =-\frac12V^2dC.
\end{aligned}
$$

Do $dW_{\mathrm{ext}}=-Fdx$, lực điện hướng vào trong. Độ lớn của lực là:

$$
\begin{aligned}
&F = \frac12V^2\frac{dC}{dx}\\
&\quad =\frac{(K-1)\varepsilon_0V^2L}{2D}.
\end{aligned}
$$

Lực không đổi theo x trong mô hình bỏ qua hiệu ứng mép.
:::

## Bài đọc và câu hỏi kiểu MCAT

### Trứng điện

Sau khi được thụ tinh, trứng của nhiều loài thay đổi nhanh hiệu điện thế qua màng ngoài. Sự thay đổi này ảnh hưởng đến quá trình phát triển sinh lý của trứng. Hiệu điện thế giữa mặt trong và mặt ngoài màng được gọi là điện thế màng $V_m$, lấy điện thế bên trong trừ điện thế bên ngoài.

Điện thế màng hình thành khi enzyme sử dụng năng lượng ATP để chủ động đưa ba ion natri Na⁺ ra ngoài và tích lũy hai ion kali K⁺ ở bên trong. Vì vậy, phần trong màng mang điện dương ít hơn phần ngoài. Với trứng nhím biển, $V_m$ xấp xỉ −70 mV, nghĩa là điện thế bên trong thấp hơn bên ngoài 70 mV.

Màng trứng hoạt động như một tụ điện có điện dung trên một đơn vị diện tích khoảng 1 µF/cm². Màng của trứng chưa thụ tinh thấm chọn lọc với K⁺. Ion K⁺ có thể đi qua một số kênh trong màng, còn những ion khác thì không. Khi trứng nhím biển được thụ tinh, các kênh Na⁺ mở ra và Na⁺ đi vào trứng. Điện thế màng tăng nhanh đến +30 mV rồi duy trì trong vài phút.

Nồng độ Na⁺ bên trong trứng xấp xỉ 30 mmol/L, còn trong nước biển xung quanh là 450 mmol/L. Nồng độ K⁺ bên trong xấp xỉ 200 mmol/L, còn bên ngoài là 10 mmol/L. Hằng số Faraday liên hệ các đại lượng điện và hóa học, có giá trị gần $10^5$ C/mol. Nghĩa là một mol ion đơn hóa trị như Na⁺ hoặc K⁺ mang điện tích $10^5$ C.

::: exercise 24.73
Nếu xem màng chỉ như một tụ điện, mỗi đơn vị diện tích màng cần nhận bao nhiêu mol Na⁺ để $V_m$ đổi từ −70 mV lên +30 mV? Chọn phương án đúng: (A) $10^{-4}$ mol/cm², (b) $10^{-9}$ mol/cm², (c) $10^{-12}$ mol/cm² hoặc (d) $10^{-14}$ mol/cm².
:::

<!-- detailed-solution:24.73 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Điện dung màng trên mỗi đơn vị diện tích là 1 µF/cm². Na⁺ đi vào làm điện thế tăng 100 mV.

**Hướng đi:**

- Tính lượng điện tích tăng trên mỗi đơn vị diện tích bằng mật độ điện dung nhân độ biến thiên điện thế.
- Chia điện tích đó cho điện tích của một mol Na⁺, dùng số Faraday đã cho.

Độ biến thiên điện thế là:

$$
\begin{aligned}
&\Delta V_m = +30\,\mathrm{mV}-(-70\,\mathrm{mV})\\
&\quad =0{,}100\,\mathrm V.
\end{aligned}
$$

Số mol Na⁺ đi vào trên mỗi cm² là:

$$
\begin{aligned}
&\frac{\Delta n_{\mathrm{Na}}}{A} = \frac{(C/A)\Delta V_m}{F}\\
&\quad =\frac{1{,}0\times10^{-7}}{1{,}0\times10^5}\,\mathrm{mol/cm^2}\\
&\quad =1{,}0\times10^{-12}\,\mathrm{mol/cm^2}.
\end{aligned}
$$

Chọn (c). Dấu dương của $\Delta V_m$ phù hợp với việc cation Na⁺ đi vào.
:::

::: exercise 24.74
Giả sử trứng có đường kính 200 µm. Nồng độ Na⁺ bên trong thay đổi theo tỷ lệ nào khi trứng được thụ tinh? Giả sử Na⁺ được phân bố khắp thể tích tế bào. Nồng độ tăng khoảng: (a) 1 phần trong $10^4$, (b) 1 phần trong $10^5$, (c) 1 phần trong $10^6$ hoặc (d) 1 phần trong $10^7$.
:::

<!-- detailed-solution:24.74 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Bán kính trứng là 100 µm. Dùng mật độ Na⁺ đi vào tìm ở câu 24.73 và nồng độ Na⁺ ban đầu 30 mmol/L.

**Hướng đi:**

- Tính diện tích màng để suy ra tổng số mol Na⁺ đi vào.
- Tính thể tích hình cầu, đổi sang lít, rồi chia số mol tăng thêm cho thể tích.
- So sánh độ tăng nồng độ với nồng độ ban đầu 0,030 mol/L.

Đổi bán kính sang đơn vị cm được $r=0{,}0100$ cm. Diện tích màng và thể tích trứng lần lượt là:

$$
\begin{aligned}
&A = 4\pi r^2\\
&\quad =1{,}2566\times10^{-3}\,\mathrm{cm^2},\\
&\mathcal V = \frac43\pi r^3\\
&\quad =4{,}1888\times10^{-6}\,\mathrm{cm^3}\\
&\quad =4{,}1888\times10^{-9}\,\mathrm L.
\end{aligned}
$$

Tổng số mol Na⁺ đi vào là:

$$
\begin{aligned}
&\Delta n = (\Delta n/A)A\\
&\quad =1{,}2566\times10^{-15}\,\mathrm{mol}.
\end{aligned}
$$

Do đó:

$$
\begin{aligned}
&\Delta c = \frac{\Delta n}{\mathcal V}\\
&\quad =3{,}00\times10^{-7}\,\mathrm{mol/L},\\
&\frac{\Delta c}{c_0} = \frac{3{,}00\times10^{-7}}{3{,}00\times10^{-2}}\\
&\quad =1{,}00\times10^{-5}.
\end{aligned}
$$

Nồng độ tăng 1 phần trong $10^5$. Chọn (b).
:::

::: exercise 24.75
Giả sử sự thay đổi $V_m$ do Ca²⁺ đi vào thay cho Na⁺. Trên mỗi đơn vị diện tích màng, cần bao nhiêu ion Ca²⁺ để tạo cùng độ biến thiên điện thế? (a) Bằng một nửa số ion Na⁺, (b) bằng số ion Na⁺, (c) gấp đôi số ion Na⁺ hoặc (d) Không thể biết nếu chưa biết nồng độ Ca²⁺ ở trong và ngoài tế bào.
:::

<!-- detailed-solution:24.75 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Cùng màng, cùng độ biến thiên điện thế nên lượng điện tích cần thêm trên mỗi đơn vị diện tích không đổi.

**Hướng đi:**

- Điện tích mỗi ion Ca²⁺ là +2e, gấp đôi điện tích của mỗi ion Na⁺.
- Giữ tổng điện tích thêm không đổi nên số ion Ca²⁺ chỉ bằng một nửa số ion Na⁺.

Gọi $N$ là số ion Na⁺ cần đi vào và $N_{\mathrm{Ca}}$ là số ion Ca²⁺. Cân bằng điện tích cho:

$$
\begin{aligned}
&N_{\mathrm{Ca}}(2e) = N e,\\
&N_{\mathrm{Ca}} = \frac N2.
\end{aligned}
$$

Chọn (a). Nồng độ trong và ngoài không cần dùng vì câu hỏi chỉ yêu cầu lượng điện tích để nạp tụ, không hỏi năng lượng hóa học của quá trình vận chuyển ion.
:::

::: exercise 24.76
Lượng công nhỏ nhất tế bào phải thực hiện để đưa $V_m$ trở về −70 mV là bao nhiêu? Chọn phương án đúng: (A) 3 mJ, (b) 3 µJ, (c) 3 nJ hoặc (d) 3 pJ.
:::

<!-- detailed-solution:24.76 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Màng có điện dung 1 µF/cm², điện thế ban đầu sau thụ tinh là +30 mV và điện thế cuối cần đạt là −70 mV. Đường kính trứng 200 µm.

**Hướng đi:**

- Năng lượng của tụ phụ thuộc bình phương điện thế, vì vậy phải lấy năng lượng cuối trừ năng lượng ban đầu, không trừ trực tiếp hai điện thế có dấu.
- Tính độ tăng năng lượng trên mỗi đơn vị diện tích, rồi nhân với diện tích màng hình cầu.
- Trong mô hình tụ lý tưởng, độ tăng năng lượng điện trường là công tối thiểu. Bỏ qua tổn hao và công hóa học bổ sung khi vận chuyển ion.

Độ tăng năng lượng trên mỗi cm² là:

$$
\begin{aligned}
&\frac{\Delta U}{A} = \frac12\frac CA(V_f^2-V_i^2)\\
&\quad =\frac12(10^{-6})(0{,}00400)\\
&\quad =2{,}0\times10^{-9}\,\mathrm{J/cm^2}.
\end{aligned}
$$

Với diện tích màng $A=1{,}2566\times10^{-3}\,\mathrm{cm^2}$,

$$
\begin{aligned}
&\Delta U = (\Delta U/A)A\\
&\quad =2{,}51\times10^{-12}\,\mathrm J\\
&\quad \approx2{,}5\,\mathrm{pJ}.
\end{aligned}
$$

Chọn (d). Dù điện thế cuối âm, độ lớn của nó lớn hơn ban đầu nên năng lượng $\frac{1}{2}CV_m^2$ tăng.
:::
