## 29.2. Định luật Faraday

Từ thông đo mức độ từ trường xuyên qua một diện tích có định hướng. Với phần tử diện tích $dA$, chọn véc-tơ diện tích $d\vec A$ vuông góc với mặt và gọi $\phi$ là góc giữa $\vec B$ và $d\vec A$. Thành phần từ trường xuyên qua mặt là $B\cos\phi$, nên từ thông vi phân bằng thành phần này nhân với diện tích phần tử.

![Hình 29.3: Từ thông qua phần tử diện tích được xác định bởi thành phần từ trường theo pháp tuyến mặt.](../img/young-29/hinh-29-03.png)
Với mặt hữu hạn $S$, cộng các phần tử từ thông trên toàn mặt:

$$
\begin{aligned}
\Phi_B&=\int_S \vec B\cdot d\vec A\\
&=\int_S B\cos\phi\,dA.
\end{aligned}
\tag{29.1}
$$

Nếu $\vec B$ đều trên một mặt phẳng diện tích $A$, tích phân rút gọn thành tích vô hướng giữa $\vec B$ và véc-tơ diện tích $\vec A$:

$$
\begin{aligned}
\Phi_B&=\vec B\cdot\vec A\\
&=BA\cos\phi.
\end{aligned}
\tag{29.2}
$$

Góc $\phi$ nằm giữa véc-tơ từ trường và véc-tơ diện tích, không phải giữa từ trường với mặt phẳng. Mặt hướng thẳng vào từ trường có $\phi=0$ và từ thông $BA$. Khi mặt nghiêng, từ thông bằng $BA\cos\phi$. Khi mặt song song với đường sức, véc-tơ diện tích vuông góc với $\vec B$, nên $\phi=90^\circ$ và từ thông bằng không.

![Hình 29.4: Từ thông phụ thuộc góc giữa từ trường và véc-tơ diện tích.](../img/young-29/hinh-29-04.png)
Véc-tơ diện tích luôn có hai hướng khả dĩ. Chọn hướng lên hay hướng xuống đều hợp lệ, nhưng lựa chọn ấy quyết định dấu của từ thông. Nếu đảo hướng $\vec A$, dấu $\Phi_B$ cũng đảo. Trong một bài toán, hãy ghi lựa chọn ban đầu rồi dùng nhất quán khi xét đạo hàm và chiều dương của suất điện động.

### Định luật Faraday

Định luật Faraday liên hệ suất điện động cảm ứng trong mạch kín với tốc độ thay đổi từ thông qua mạch:

$$
\mathcal E=-\frac{d\Phi_B}{dt}.
\tag{29.3}
$$

Dấu trừ cho biết chiều suất điện động theo quy ước hướng diện tích. Nếu từ thông dương đang tăng thì suất điện động âm. Nếu từ thông dương đang giảm thì suất điện động dương. Chưa thể đổi dấu thành chiều quay cho đến khi đã chọn hướng véc-tơ diện tích, rồi dùng quy tắc bàn tay phải.

![Hình 29.6: Dấu từ thông và chiều suất điện động khi từ thông tăng hoặc giảm.](../img/young-29/hinh-29-06.png)
Nếu cuộn có $N$ vòng giống nhau và từ thông qua mỗi vòng biến thiên cùng tốc độ, tổng suất điện động bằng $N$ lần suất điện động của một vòng. Chẳng hạn, hai vòng nối tiếp có tổng suất điện động bằng suất điện động vòng thứ nhất cộng suất điện động vòng thứ hai. Với $N$ vòng, sự cộng ấy viết thành

$$
\begin{aligned}
\mathcal E_{\mathrm{tổng}}
&=\mathcal E_1+\mathcal E_2+\dots+\mathcal E_N\\
&=-N\frac{d\Phi_B}{dt}.
\end{aligned}
$$

Ở đây $N$ là số nguyên dương và $\Phi_B$ là từ thông qua một vòng. Do đó:

$$
\mathcal E=-N\frac{d\Phi_B}{dt}.
\tag{29.4}
$$

Định luật Faraday phụ thuộc sự thay đổi từ thông, không phụ thuộc riêng giá trị từ thông. Từ thông có thể rất lớn nhưng không đổi, khi ấy suất điện động bằng không. Từ thông cũng có thể bằng không tại một thời điểm nhưng đang biến đổi, khi ấy suất điện động khác không.

Không chỉ biến thiên độ lớn từ trường mới gây cảm ứng. Mạch có thể dịch chuyển trong từ trường không đều hoặc thay đổi hình dạng trong từ trường không đổi. Cả ba cơ chế đều phải được xét thông qua tốc độ biến thiên từ thông.

Đơn vị của từ thông là weber, với $1\,\mathrm{Wb}=1\,\mathrm{T\,m^2}$. Do đó tốc độ biến thiên từ thông có đơn vị volt, $1\,\mathrm V=1\,\mathrm{Wb/s}$.

### Ví dụ 29.1. Suất điện động và dòng điện cảm ứng trong một vòng

Một vòng dây dẫn đứng yên nằm trong vùng có từ trường đều vuông góc mặt vòng. Diện tích vòng là $120\,\mathrm{cm^2}$, độ lớn từ trường tăng với tốc độ $0{,}020\,\mathrm{T/s}$, và điện trở toàn mạch kể cả điện kế là $5{,}0\,\Omega$. Hãy tìm độ lớn suất điện động và dòng điện. Sau đó thay vòng dẫn bằng một vòng cách điện, rồi xét lại hai đại lượng ấy.

![Hình 29.5: Vòng dây đứng yên trong từ trường đang tăng.](../img/young-29/hinh-29-05.png)
**Hướng đi hợp lý:** Từ thông đổi vì độ lớn $B$ tăng, còn diện tích và hướng vòng giữ nguyên. Chọn véc-tơ diện tích hướng lên, cùng hướng $\vec B$. Tính từ thông rồi lấy đạo hàm theo thời gian. Dùng định luật Ohm để tìm dòng điện.

Đổi diện tích sang đơn vị SI:

$$
\begin{aligned}
A&=120\,\mathrm{cm^2}\\
&=0{,}012\,\mathrm{m^2}.
\end{aligned}
$$

Vì $\phi=0$, ta có $\Phi_B=BA$. Do $A$ không đổi:

$$
\begin{aligned}
\frac{d\Phi_B}{dt}&=A\frac{dB}{dt}\\
&=(0{,}012)(0{,}020)\\
&=2{,}4\times10^{-4}\,\mathrm{Wb/s}.
\end{aligned}
$$

Độ lớn suất điện động cảm ứng là $2{,}4\times10^{-4}\,\mathrm V=0{,}24\,\mathrm{mV}$. Dấu của $\mathcal E$ theo lựa chọn véc-tơ diện tích sẽ là âm vì từ thông dương đang tăng. Dòng điện có độ lớn:

$$
\begin{aligned}
I&=\frac{|\mathcal E|}{R}\\
&=\frac{2{,}4\times10^{-4}}{5{,}0}\\
&=4{,}8\times10^{-5}\,\mathrm A\\
&=0{,}048\,\mathrm{mA}.
\end{aligned}
$$

Đổi sang vòng cách điện không làm đổi suất điện động, vì định luật Faraday không chứa điện trở. Điện trở rất lớn làm dòng nhỏ hơn. Với chất cách điện lý tưởng có điện trở vô hạn, dòng bằng không dù suất điện động vẫn tồn tại.

### Cách giải bài toán theo định luật Faraday

**Nhận diện:** Xác định đại lượng cần tìm và liệu từ thông có thay đổi hay không. Xác định diện tích nào được tính từ thông, thường là mặt bị bao quanh bởi mạch kín.

**Thiết lập:** Tìm nguyên nhân làm từ thông đổi. Đó có thể là từ trường biến thiên, dây dẫn chuyển động, diện tích mạch thay đổi hoặc mạch xoay đổi hướng. Chọn hướng véc-tơ diện tích vuông góc với mặt và cố định lựa chọn ấy trong toàn bài.

**Thực hiện:** Nếu từ trường đều, dùng công thức (29.2). Nếu không đều, dùng tích phân công thức (29.1). Tính tốc độ thay đổi từ thông rồi dùng công thức (29.3), hoặc công thức (29.4) nếu có $N$ vòng. Nếu biết điện trở, tìm độ lớn dòng bằng $I=|\mathcal E|/R$.

**Đánh giá:** Kiểm tra đơn vị, dấu từ thông, dấu suất điện động và chiều dòng theo lựa chọn véc-tơ diện tích.

### Ví dụ 29.2. Độ lớn và chiều của suất điện động cảm ứng

Một cuộn dây tròn có $500$ vòng và bán kính $4{,}00\,\mathrm{cm}$. Cuộn nằm trong từ trường đều. Từ trường tạo góc $60^\circ$ với mặt phẳng cuộn và giảm với tốc độ $0{,}200\,\mathrm{T/s}$. Hãy tìm độ lớn và chiều suất điện động cảm ứng.

![Hình 29.7: Cuộn dây nghiêng trong từ trường, với góc đề bài đo từ mặt phẳng cuộn.](../img/young-29/hinh-29-07.png)
**Hướng đi hợp lý:** Đổi bán kính sang mét. Từ trường tạo góc $60^\circ$ với mặt phẳng, nên tạo góc $30^\circ$ với véc-tơ diện tích. Dùng công thức (29.4), chú ý $dB/dt<0$.

Diện tích mỗi vòng là $A=\pi(0{,}0400\,\mathrm m)^2$. Vì $B$ đều và hướng cuộn không đổi:

$$
\begin{aligned}
\mathcal E&=-N\frac{dB}{dt}A\cos30^\circ\\
&=-500(-0{,}200)\\
&\quad\times\pi(0{,}0400)^2\cos30^\circ\\
&=+0{,}435\,\mathrm V.
\end{aligned}
$$

Độ lớn là $0{,}435\,\mathrm V$. Dấu dương cho biết suất điện động cùng chiều các ngón tay phải khi ngón cái chỉ theo véc-tơ diện tích đã chọn trong hình. Nhìn cuộn từ phía trái theo chiều véc-tơ diện tích, suất điện động quay theo chiều kim đồng hồ. Nếu mạch kín thì dòng có cùng chiều và tạo từ trường chống lại sự giảm từ thông.

### Ví dụ 29.3. Máy phát xoay chiều đơn giản

Một khung dây diện tích $A$ quay đều với tốc độ góc $\omega$ trong từ trường đều, không đổi, có độ lớn $B$. Tại $t=0$, góc giữa $\vec B$ và véc-tơ diện tích bằng không. Hãy tìm suất điện động cảm ứng theo thời gian.

**Hướng đi hợp lý:** Khi quay đều, góc giữa $\vec B$ và véc-tơ diện tích là $\phi=\omega t$. Tính từ thông bằng công thức (29.2), sau đó lấy đạo hàm.

$$
\begin{aligned}
\Phi_B(t)&=BA\cos(\omega t),\\
\mathcal E(t)&=-\frac{d\Phi_B}{dt}\\
&=\omega BA\sin(\omega t).
\end{aligned}
$$

Suất điện động biến thiên hình sin. Khi mặt cuộn vuông góc với $\vec B$, từ thông đạt cực đại hoặc cực tiểu và tốc độ biến thiên của nó bằng không, nên $\mathcal E=0$. Khi mặt cuộn song song với $\vec B$, từ thông bằng không nhưng đổi nhanh nhất, nên độ lớn suất điện động đạt cực đại. Kết quả chỉ phụ thuộc diện tích, không phụ thuộc hình dạng cụ thể của cuộn.

![Hình 29.8: Cuộn dây quay tạo suất điện động xoay chiều và đồ thị theo thời gian.](../img/young-29/hinh-29-08.png)
Trong máy phát điện xoay chiều (alternator), vòng trượt quay cùng cuộn dây và trượt trên các chổi tiếp xúc đứng yên. Điện áp đổi dấu tuần hoàn nên dòng điện trong mạch ngoài là dòng xoay chiều. Có thể tăng biên độ suất điện động bằng cách tăng tốc độ quay, tăng độ lớn từ trường, tăng diện tích cuộn hoặc tăng số vòng.

![Hình 29.9: Phần ứng nhiều vòng trong máy phát điện xoay chiều thương mại.](../img/young-29/hinh-29-09.png)
Alternator trên ô tô cấp điện cho hệ thống đánh lửa, đèn và thiết bị giải trí. Trong nhiều thiết kế, cuộn dây đứng yên còn nam châm điện quay. Máy phát ở nhà máy điện cũng dựa trên sự biến thiên từ thông qua cuộn dây.

### Ví dụ 29.4. Máy phát một chiều và suất phản điện động của động cơ

Máy phát một chiều dùng cổ góp vòng chia để đảo các kết nối với mạch ngoài đúng lúc suất điện động trong cuộn đổi dấu. Nhờ vậy, suất điện động đầu ra luôn cùng dấu. Máy thương mại dùng nhiều cuộn và nhiều đoạn cổ góp để giảm độ nhấp nhô. Cơ cấu chổi và cổ góp cũng có trong động cơ một chiều. Suất phản điện động của động cơ là suất điện động cảm ứng do từ thông qua cuộn quay biến thiên.

Xét động cơ có cuộn vuông $500$ vòng, cạnh $10{,}0\,\mathrm{cm}$, đặt trong từ trường $0{,}200\,\mathrm T$. Cần tìm tốc độ quay để suất phản điện động trung bình bằng $112\,\mathrm V$.

![Hình 29.10: Máy phát điện một chiều dùng cổ góp vòng chia để đảo kết nối.](../img/young-29/hinh-29-10.png)
**Hướng đi hợp lý:** Không có cổ góp, suất điện động là hình sin và trung bình trên cả chu kỳ bằng không. Có cổ góp, đầu ra giữ nửa chu kỳ dương rồi đảo mối nối để tiếp tục nửa chu kỳ dương. Tính trung bình giá trị tuyệt đối của hàm sin trên nửa chu kỳ.

Suất điện động tức thời có biên độ $\mathcal E_0=N\omega BA$. Trung bình của $|\sin\omega t|$ trên nửa chu kỳ là:

$$
\begin{aligned}
\langle|\sin\omega t|\rangle&=\frac{\int_0^{\pi/\omega}\sin(\omega t)\,dt}{\pi/\omega}\\
&=\frac{2}{\pi}.
\end{aligned}
$$

Do đó $\mathcal E_{\mathrm{av}}=2N\omega BA/\pi$, suy ra:

$$
\begin{aligned}
\omega&=\frac{\pi\mathcal E_{\mathrm{av}}}{2NBA}\\
&=\frac{\pi(112)}{2(500)(0{,}200)(0{,}100)^2}\\
&=176\,\mathrm{rad/s}.
\end{aligned}
$$

Suất phản điện động trung bình tỉ lệ thuận với tốc độ quay. Nếu động cơ quay chậm hơn, suất phản điện động giảm và dòng điện lấy từ nguồn có thể tăng, làm động cơ nóng lên.

### Ví dụ 29.5. Máy phát thanh trượt

Một thanh kim loại dài $L$ trượt sang phải với tốc độ không đổi $v$ trên hai thanh dẫn hình chữ U. Từ trường đều $\vec B$ hướng vào trang giấy. Chọn véc-tơ diện tích cũng hướng vào trang, cùng chiều từ trường. Khi thanh trượt đi sang phải, diện tích mạch tăng.

![Hình 29.11: Thanh trượt làm tăng diện tích mạch trong từ trường hướng vào trang.](../img/young-29/hinh-29-11.png)
**Hướng đi hợp lý:** Từ trường không đổi và vuông góc mặt mạch, nên $\Phi_B=BA$. Trong khoảng $dt$, thanh dịch chuyển $v\,dt$ và diện tích tăng $dA=L v\,dt$. Lấy đạo hàm từ thông rồi dùng quy ước dấu đã chọn.

$$
\begin{aligned}
\mathcal E&=-\frac{d\Phi_B}{dt}\\
&=-B\frac{dA}{dt}\\
&=-BLv.
\end{aligned}
$$

Dấu âm cho biết suất điện động ngược chiều dương đã chọn. Vì véc-tơ diện tích hướng vào trang, chiều dương theo quy tắc bàn tay phải là chiều kim đồng hồ. Do đó dòng cảm ứng chạy ngược chiều kim đồng hồ. Khi $v$ không đổi, suất điện động không đổi và thiết bị tạo dòng một chiều. Nếu thanh trượt rời khỏi ray chữ U thì mạch hở và dòng dừng.

### Ví dụ 29.6. Công và công suất trong máy phát thanh trượt

Giữ các ký hiệu của Ví dụ 29.5. Gọi $R$ là điện trở toàn mạch. Tìm tốc độ tỏa nhiệt và tốc độ làm công cần thiết để kéo thanh với tốc độ không đổi.

**Hướng đi hợp lý:** Dùng $I=|\mathcal E|/R$ để tìm dòng. Lực từ lên thanh ngược chiều chuyển động. Vì thanh được kéo đều, lực ngoài cùng độ lớn và ngược chiều lực từ. So sánh công suất ngoài $Fv$ với tốc độ tỏa nhiệt $I^2R$.

$$
I=\frac{BLv}{R}.
$$

Công suất điện chuyển thành nhiệt trong mạch là:

$$
\begin{aligned}
P_{\mathrm{nhiệt}}&=I^2R\\
&=\frac{B^2L^2v^2}{R}.
\end{aligned}
$$

Lực từ có độ lớn $F=ILB=B^2L^2v/R$ và hướng sang trái, ngược với thanh đang đi sang phải. Người kéo phải tác dụng lực cùng chiều chuyển động, nên:

$$
\begin{aligned}
P_{\mathrm{ngoài}}&=Fv\\
&=\frac{B^2L^2v^2}{R}\\
&=P_{\mathrm{nhiệt}}.
\end{aligned}
$$

![Hình 29.12: Lực từ trên thanh trượt hướng ngược chiều chuyển động.](../img/young-29/hinh-29-12.png)
Máy phát không tạo điện năng từ hư không. Năng lượng điện và nhiệt trong mạch đến từ công cơ học cần thiết để kéo thanh. Khi bỏ qua ma sát, tốc độ truyền cơ năng bằng tốc độ chuyển hóa thành nhiệt trong điện trở.

Dường như lực từ lên thanh đang chuyển động sinh công âm, điều này có vẻ trái với kết quả rằng lực từ không làm công lên điện tích. Lực từ làm các điện tích trong thanh dịch chuyển ngang, tạo điện tích dương ở một đầu và điện tích âm ở đầu kia. Điện trường phát sinh theo phương chuyển động mới là tác nhân làm công lên các điện tích linh động và gián tiếp lên vật liệu của thanh.

### Tự kiểm tra Mục 29.2

Một cuộn dây tròn bị bóp thành hình oval trong từ trường đều hướng vào trang. (a) Khi đang bóp, suất điện động theo chiều kim đồng hồ, ngược chiều kim đồng hồ hay bằng không? (b) Sau khi cuộn đã giữ nguyên hình oval, suất điện động theo chiều kim đồng hồ, ngược chiều kim đồng hồ hay bằng không?

![Tự kiểm 29.2: Bóp vòng dây tròn thành hình oval làm giảm diện tích trong từ trường đều hướng vào mặt hình.](../img/young-29/hinh-tu-kiem29-2.png)

<details>
<summary>Đáp án</summary>

(a) Theo chiều kim đồng hồ. Từ thông vào trang giảm khi diện tích cuộn giảm, nên $d\Phi_B/dt<0$ theo quy ước diện tích hướng vào trang và $\mathcal E>0$. Chiều dương ứng với chiều kim đồng hồ. (b) Bằng không, vì diện tích và từ trường không còn thay đổi nên từ thông không đổi.

</details>
