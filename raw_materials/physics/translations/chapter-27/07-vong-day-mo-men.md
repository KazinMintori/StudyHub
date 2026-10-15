<!-- Source: Section 27.7, “Force and Torque on a Current Loop,” printed pages 897–902 through the section check, PDF pages 917–922. -->

## 27.7 Lực và mômen lực lên vòng dây mang dòng điện

Trong từ trường đều, một vòng dây kín mang dòng điện chịu tổng lực bằng không. Tuy vậy, các lực trên từng cạnh có thể tạo thành ngẫu lực làm vòng quay. Mômen này giải thích cách cuộn dây quay trong máy đo dòng, cách một vòng dây định hướng như nam châm và cách một từ trường làm sắt chưa nhiễm từ bị hút.

### Lực tổng hợp và mômen của một vòng chữ nhật

![Vòng dây chữ nhật mang dòng điện trong từ trường đều, các lực trên hai cặp cạnh đối diện triệt tiêu tổng lực nhưng tạo mômen](../img/young-27/hinh-27-31.png)

Hình 27.31: Vòng dây có cạnh dài $a$ và $b$. Góc $\phi$ là góc giữa pháp tuyến của mặt vòng và từ trường.

Xét vòng dây chữ nhật mang dòng điện $I$ trong từ trường đều $\vec{B}$. Một cặp cạnh dài $a$ vuông góc với từ trường, nên mỗi cạnh chịu lực có độ lớn $F=IaB$. Hai lực này ngược chiều và đặt trên hai đường tác dụng khác nhau. Cặp cạnh dài $b$ chịu hai lực ngược chiều, cùng nằm trên một đường tác dụng, nên không tạo mômen tổng.

Lực trên mỗi cạnh dài $a$ là:

$$
F=IBa.
\tag{27.21}
$$

Các cạnh dài $b$ hợp với từ trường góc $90^\circ-\phi$, nên lực trên mỗi cạnh có độ lớn:

$$
F' = IbB\sin(90^\circ-\phi) = IbB\cos\phi.
$$

Các lực trên từng cặp cạnh triệt tiêu theo véc-tơ. Vì thế tổng lực lên vòng bằng không. Tuy nhiên, hai lực trên cạnh dài $a$ có cánh tay đòn $\tfrac{b}{2}\sin\phi$ đối với trục qua tâm, nên mômen tổng có độ lớn:

$$
\begin{aligned}
\tau &= 2F\left(\frac{b}{2}\sin\phi\right) \\
&= (IaB)(b\sin\phi).
\end{aligned} \tag{27.22}
$$

Ở đây $A=ab$ là diện tích vòng dây. Vì vậy:

$$
\tau=IAB\sin\phi.
\tag{27.23}
$$

 Mômen lớn nhất khi $\phi=90^\circ$, tức từ trường nằm trong mặt phẳng vòng. Mômen bằng không khi pháp tuyến song song hoặc ngược song song với từ trường, tại $\phi=0^\circ$ hoặc $180^\circ$. Vị trí $\phi=0^\circ$ cân bằng bền: Nếu vòng lệch nhẹ, mômen đưa nó trở lại. Vị trí $180^\circ$ cân bằng không bền: Một lệch nhỏ khiến vòng tiếp tục rời xa vị trí ấy.

### Mômen lưỡng cực từ

Tích của dòng điện với diện tích vòng được gọi là độ lớn mômen lưỡng cực từ:

$$
\mu = IA. \tag{27.24}
$$

Véc-tơ $\vec{\mu}$ vuông góc mặt vòng. Chiều của nó được xác định bằng quy tắc bàn tay phải: Khum các ngón theo chiều dòng điện, ngón cái duỗi ra chỉ chiều $\vec{\mu}$. Đây cũng là chiều véc-tơ diện tích $\vec{A}$, nên $\vec{\mu}=I\vec{A}$.

Với góc $\phi$ giữa $\vec{\mu}$ và $\vec{B}$, độ lớn mômen lực là:

$$
\tau = \mu B\sin\phi. \tag{27.25}
$$

Chiều mômen được cho bởi tích có hướng:

$$
\vec{\tau} = \vec{\mu}\times\vec{B}. \tag{27.26}
$$

Mômen luôn làm $\vec{\mu}$ quay về cùng hướng với $\vec{B}$. Ở trạng thái cân bằng bền, hai véc-tơ song song. Khi ngược song song, vòng ở cân bằng không bền. Công thức này tương tự mômen lực $\vec{p}\times\vec{E}$ lên lưỡng cực điện.

![Quy tắc bàn tay phải xác định mômen lưỡng cực từ của vòng dây từ chiều dòng điện](../img/young-27/hinh-27-32.png)

Hình 27.32: Chiều $\vec{\mu}$ trùng với chiều véc-tơ diện tích của vòng dây.

### Năng lượng thế của lưỡng cực từ

Khi mômen từ đổi hướng trong từ trường, từ trường sinh công. Năng lượng thế nhỏ nhất khi $\vec{\mu}$ song song với $\vec{B}$, lớn nhất khi hai véc-tơ ngược chiều. Chọn mốc năng lượng bằng không khi hai véc-tơ vuông góc, ta có:

$$
\begin{aligned}
U &= -\vec{\mu}\cdot\vec{B} \\
&= -\mu B\cos\phi.
\end{aligned} \tag{27.27}
$$

Theo chiều tăng của $\phi$, thành phần mômen lực là $\tau_\phi=-\mu B\sin\phi$. Trong một dịch chuyển góc vi phân, công của từ trường là $dW=\tau_\phi\,d\phi$, còn biến thiên năng lượng thế là $dU=-dW$. Do đó $dU=\mu B\sin\phi\,d\phi$, suy ra biểu thức trên khi chọn $U=0$ tại $\phi=90^\circ$.

Khi $\phi=90^\circ$, năng lượng bằng không theo mốc đã chọn. Khi $\phi=0^\circ$, năng lượng là $-\mu B$ và đạt giá trị nhỏ nhất. Khi $\phi=180^\circ$, năng lượng là $+\mu B$ và đạt giá trị lớn nhất.

### Cuộn nhiều vòng và máy đo dòng điện

Các kết quả trên đúng cho mọi vòng dây phẳng, không chỉ vòng chữ nhật. Có thể hình dung một đường biên bất kỳ được ghép từ nhiều hình chữ nhật nhỏ. Các cạnh nằm bên trong triệt tiêu lực và mômen từng đôi, chỉ còn tác dụng trên đường biên ngoài.

![Một vòng dây phẳng hình dạng bất kỳ được xấp xỉ bằng nhiều vòng chữ nhật nhỏ](../img/young-27/hinh-27-33.png)

Hình 27.33: Các cạnh ở bên trong triệt tiêu từng đôi, chỉ còn lực và mômen trên đường biên ngoài.

Với cuộn gồm $N$ vòng sát nhau, mỗi vòng đóng góp cùng chiều. Mômen lưỡng cực và mômen lực tăng $N$ lần:

$$
\begin{aligned}
\mu &= NIA, \\
\tau &= NIAB\sin\phi.
\end{aligned} \tag{27.28}
$$

Lực tổng hợp và năng lượng thế của cuộn nhiều vòng cũng bằng $N$ lần giá trị trên mỗi vòng.

Một ống dây chặt có thể xem như nhiều vòng dây đặt dọc trục. Mômen từ của nó nằm dọc trục và có xu hướng làm trục song song với từ trường.

![Ống dây mang dòng chịu mômen làm trục quay để mômen từ song song với từ trường](../img/young-27/hinh-27-34.png)

Hình 27.34: Mômen lực $\vec{\tau}=\vec{\mu}\times\vec{B}$ vuông góc mặt giấy làm trục ống dây quay để $\vec{\mu}$ hướng theo $\vec{B}$.

Với ống dây, góc $\phi$ là góc giữa trục dây và từ trường. Mômen cực đại khi trục vuông góc với từ trường, bằng không khi trục song song với từ trường. Ống dây cũng có thể dùng để tạo từ trường.

Máy đo dòng điện kiểu d’Arsonval dùng mômen từ lên cuộn dây. Từ trường trong khe máy hướng xuyên tâm, nên luôn vuông góc với pháp tuyến của cuộn dây và $\sin\phi=1$. Mômen từ vì thế tỉ lệ với dòng điện. Hai lò xo tạo mômen hồi phục tỉ lệ với độ lệch góc, đồng thời dẫn điện vào cuộn dây. Kim dừng ở vị trí mà mômen hồi phục cân bằng mômen từ, nên độ lệch của kim tỉ lệ với dòng điện.

### Ứng dụng sinh học: Chụp cộng hưởng từ

![Ảnh cộng hưởng từ cho thấy mô mềm quanh khớp gối](../img/young-27/ung-dung-mri.png)

Ảnh cộng hưởng từ cung cấp thông tin về mô giàu hiđrô.

Trong chụp cộng hưởng từ, bệnh nhân được đặt trong từ trường mạnh. Hạt nhân hiđrô có mômen từ, có xu hướng định hướng theo trường ngoài. Sóng vô tuyến có tần số thích hợp làm các mômen đổi hướng. Mức hấp thụ sóng phụ thuộc vào lượng hiđrô, nhờ đó máy dựng được ảnh mô mềm giàu hiđrô. Tia X thường thích hợp hơn khi cần ghi hình xương, vốn nghèo hiđrô.

### Từ trường không đều tạo lực tổng hợp lên lưỡng cực

Trong từ trường đều, các lực trên vòng triệt tiêu nên tổng lực bằng không. Nếu từ trường không đều, lực trên các phần khác nhau của vòng không còn cân bằng. Khi mômen từ ngược chiều với từ trường gần nam châm, vòng bị đẩy về vùng từ trường yếu hơn. Khi mômen từ cùng chiều với từ trường, vòng bị kéo về vùng từ trường mạnh hơn.

![Vòng dây trong từ trường không đều chịu lực đẩy ra xa cực bắc hoặc lực hút về cực nam tùy chiều mômen](../img/young-27/hinh-27-36.png)

Hình 27.36: Lực tổng hợp lên một vòng dây trong từ trường không đều phụ thuộc vào chiều mômen từ.

### Ví dụ 27.9: Mômen lực lên cuộn dây tròn

![Cuộn dây tròn nhìn từ trên xuống, mômen từ hướng lên và từ trường hướng sang phải](../img/young-27/hinh-27-35.png)

Hình 27.35: Hình học của cuộn dây trong ví dụ.

Một cuộn tròn bán kính $0{,}0500\,\mathrm{m}$ có $30$ vòng và mang dòng $5{,}00\,\mathrm{A}$. Mặt cuộn nằm ngang, dòng nhìn từ trên chạy ngược chiều kim đồng hồ, còn từ trường đều $1{,}20\,\mathrm{T}$ hướng sang phải. Tìm mômen từ và mômen lực.

Diện tích một vòng là $A=\pi r^2$. Mômen từ của cả cuộn là:

$$
\begin{aligned}
\mu &= NIA \\
&= 30(5{,}00)\pi(0{,}0500)^2 \\
&= 1{,}18\,\mathrm{A\,m^2}.
\end{aligned}
$$

Theo quy tắc bàn tay phải, $\vec{\mu}$ hướng lên, vuông góc với $\vec{B}$, nên $\phi=90^\circ$. Do đó:

$$
\begin{aligned}
\tau &= \mu B\sin90^\circ \\
&= (1{,}18)(1{,}20) \\
&= 1{,}41\,\mathrm{N\,m}.
\end{aligned}
$$

Mômen có chiều $\vec{\mu}\times\vec{B}$ và làm cuộn quay để pháp tuyến của nó song song với từ trường.

### Ví dụ 27.10: Năng lượng thế khi cuộn quay

Nếu cuộn ở trên quay đến vị trí $\vec{\mu}$ song song $\vec{B}$, góc đổi từ $90^\circ$ thành $0^\circ$. Độ biến thiên năng lượng là:

$$
\begin{aligned}
\Delta U &= U_f-U_i \\
&= -\mu B(\cos0^\circ-\cos90^\circ) \\
&= -1{,}41\,\mathrm{J}.
\end{aligned}
$$

Năng lượng giảm vì cuộn quay theo chiều của mômen lực từ. Thế năng phụ thuộc độ lớn và hướng của cả mômen từ lẫn từ trường. Nó nhỏ nhất khi hai vector cùng chiều.

### Vì sao nam châm hút sắt chưa nhiễm từ?

Mômen từ của nam châm thanh hướng từ cực nam đến cực bắc. Ở vật sắt chưa nhiễm từ, các mômen từ vi mô không có hướng ưu tiên nên tổng mômen bằng không. Khi đặt gần nam châm, từ trường làm chúng có xu hướng định hướng theo trường và vật sắt có mômen tổng song song với từ trường tại chỗ. Vì từ trường của nam châm không đều, lưỡng cực cảm ứng bị hút về vùng trường mạnh hơn. Cơ chế này khiến vật sắt có thể bị hút về cả cực bắc lẫn cực nam.

Trong nam châm sắt, nhiều mômen từ vi mô đã định hướng gần cùng chiều nên tổng mômen khác không. Mômen tổng khiến nam châm có hai cực và chịu mômen quay khi đặt trong từ trường. Hình dung electron như một quả cầu tích điện đang quay chỉ là phép tương tự. Electron không phải quả cầu đang quay theo nghĩa cổ điển. Giải thích đầy đủ mômen từ của electron cần đến cơ học lượng tử.

Ở phần lớn nguyên tố khác, các nguyên tử có mômen tổng rất nhỏ hoặc bằng không. Khi vật sắt được lấy ra khỏi từ trường, một phần mômen vi mô vẫn giữ được hướng nên vật có thể còn nhiễm từ. Làm rơi hoặc nung nóng vật có thể khiến các mômen trở nên hỗn loạn trở lại.

Mô hình lưỡng cực cũng giải thích tương tác giữa hai nam châm thanh. Hai cực cùng tên đẩy nhau, còn hai cực khác tên hút nhau. Nghiên cứu đầy đủ tính chất từ của vật liệu được tiếp tục ở mục 28.8.

![Mômen từ trong sắt chưa nhiễm từ phân tán ngẫu nhiên, trong nam châm thì định hướng gần cùng chiều](../img/young-27/hinh-27-37.png)

Hình 27.37: Sự định hướng của mômen từ vi mô tạo nên mômen tổng của nam châm.

![Từ trường của mỗi cực nam châm làm đinh sắt cảm ứng mômen từ rồi hút đinh về phía nam châm](../img/young-27/hinh-27-38.png)

Hình 27.38: Vật sắt chưa nhiễm từ bị hút vì từ trường vừa cảm ứng mômen từ vừa không đều trong không gian.

### Tự kiểm tra

Trong Hình 27.13c, đường sức của vòng dây có dòng điện cho biết từ trường dọc trục hướng sang phải. Xác định chiều mômen từ của vòng và cho biết phía nào tương đương cực bắc.

![Đường sức từ của vòng dây có dòng điện hướng dọc trục sang phải](../img/young-27/hinh-27-13.png)

::: details Lời giải
Mômen từ hướng sang phải. Quy tắc bàn tay phải xác nhận chiều này khi khum ngón theo chiều dòng điện. Mômen từ của nam châm hướng từ cực nam đến cực bắc, nên phía phải của vòng tương đương cực bắc, còn phía trái tương đương cực nam.
:::

::: info Ý chính
Vòng dây mang dòng trong từ trường đều có tổng lực bằng không nhưng nói chung chịu mômen $\vec{\tau}=\vec{\mu}\times\vec{B}$. Mômen từ có độ lớn $NIA$, còn năng lượng thế là $-\vec{\mu}\cdot\vec{B}$. Từ trường không đều có thể tạo lực tổng hợp lên vòng dây.
:::
