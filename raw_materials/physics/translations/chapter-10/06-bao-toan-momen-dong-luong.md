## 10.6 Bảo toàn mômen động lượng

Một người đang quay có thể quay nhanh hơn khi thu tay mà không cần một mômen ngoại lực mới. Để giải thích, phải xét cả sự thay đổi mômen quán tính và định luật bảo toàn mômen động lượng.

### Điều kiện bảo toàn và phạm vi áp dụng

Từ phương trình động lực học tổng quát, nếu tổng mômen ngoại lực bằng không trong suốt quá trình thì:

$$
\frac{d\vec L}{dt}=0.
$$

Vì vậy, $\vec L$ của toàn hệ được bảo toàn. Mômen ngoại lực phải được xét đối với cùng một mốc. Nếu chỉ thành phần mômen ngoại lực theo một trục bằng không, chỉ thành phần mômen động lượng theo trục ấy được bảo toàn.

Đối với hệ có $L_z=I\omega_z$, ta viết:

$$
I_1\omega_{1z}=I_2\omega_{2z}. \tag{10.30}
$$

Khi $I$ giảm, độ lớn vận tốc góc tăng nếu mômen động lượng khác không được giữ nguyên. Đây là cơ chế khi vận động viên trượt băng hoặc người nhào lộn thu tay, chân lại. Trong giai đoạn bay, trọng lực không gây mômen quanh khối tâm nếu trọng trường đều.

### Nội lực trao đổi mômen động lượng giữa các phần

Xét hai vật A, B chỉ tương tác với nhau bằng một cặp lực cùng đường nối. Mômen lực của A lên B bằng đạo hàm mômen động lượng của B, còn mômen của B lên A bằng đạo hàm mômen động lượng của A. Hai mômen đối nhau, nên:

$$
\frac{d}{dt}(\vec L_A+\vec L_B)=0. \tag{10.31}
$$

Từng phần có thể đổi mômen động lượng nhưng tổng của hệ không đổi. Không thể chỉ nhìn một phần rồi kết luận toàn hệ vi phạm bảo toàn.

![Hình 10.28: Mèo đổi tư thế bằng cách xoay các phần cơ thể theo những cách phối hợp, trong khi mômen động lượng toàn thân có thể vẫn bằng không.](../img/young-10/b-hinh-10-28.png)

Trường hợp mèo đang rơi cần phân biệt với hệ chỉ có một trục quay và một mômen quán tính. Cơ thể có nhiều phần và thay đổi cấu hình. Việc tổng mômen động lượng bằng không không buộc mọi phần đứng yên hoặc cấm cơ thể đổi hướng.

::: example Ví dụ 10.10: Thu tạ khi đang quay

Một giảng viên đứng ở tâm bàn quay không ma sát, mỗi tay cầm tạ $5{,}0\,\mathrm{kg}$. Ban đầu dang tay, quay một vòng trong $2{,}0\,\mathrm s$. Sau đó thu hai tạ vào bụng.

Mômen quán tính cơ thể, không kể tạ, giảm từ $3{,}0$ xuống $2{,}2\,\mathrm{kg\cdot m^2}$. Khoảng cách mỗi tạ đến trục giảm từ $1{,}0$ xuống $0{,}20\,\mathrm m$. Tìm vận tốc góc cuối.

![Hình 10.29: Thu hai tạ về gần trục làm mômen quán tính giảm và vận tốc góc tăng.](../img/young-10/b-hinh-10-29.png)

**Tóm tắt đề bài:** Xem mỗi tạ như chất điểm. Mômen ngoại lực quanh trục đứng không đáng kể.

**Hướng đi:** Cộng mômen quán tính cơ thể và hai tạ tại từng cấu hình. Sau đó bảo toàn thành phần mômen động lượng theo trục đứng. Động năng không được tự coi là bảo toàn vì người thực hiện công khi thu tạ.

**Lời giải:**

$$
\begin{aligned}
I_1&=3{,}0+2(5{,}0)(1{,}0)^2\\
&=13\,\mathrm{kg\cdot m^2},\\
I_2&=2{,}2+2(5{,}0)(0{,}20)^2\\
&=2{,}6\,\mathrm{kg\cdot m^2}.
\end{aligned}
$$

Vận tốc góc cuối:

$$
\omega_{2z}=\frac{I_1}{I_2}\omega_{1z}=5\omega_{1z}.
$$

Vì ban đầu $\omega_{1z}=0{,}50\,\mathrm{vòng/s}$, kết quả là $2{,}5\,\mathrm{vòng/s}$, tương đương khoảng $15{,}7\,\mathrm{rad/s}$. Có thể lấy tỷ số mà không đổi vòng sang radian vì hệ số đổi đơn vị triệt tiêu.

Để tính năng lượng theo joule, phải đổi sang radian. Động năng đầu khoảng $64\,\mathrm J$, động năng cuối khoảng $321\,\mathrm J$, tăng năm lần. Năng lượng tăng thêm do công của người khi kéo tay và tạ vào, không phải do mômen ngoại lực.
:::

::: example Ví dụ 10.11: Hai đĩa quay ghép với nhau

Hai đĩa gồm bánh đà A và đĩa ly hợp B, có mômen quán tính $I_A,I_B$, ban đầu quay cùng chiều với vận tốc góc $\omega_A,\omega_B$. Ép hai đĩa sát nhau bằng các lực dọc trục. Ma sát giữa hai mặt khiến chúng cuối cùng quay chung. Tìm vận tốc góc chung.

![Hình 10.30: Lực ép dọc trục không gây mômen quanh trục. Ma sát trao đổi mômen động lượng giữa hai đĩa.](../img/young-10/b-hinh-10-30.png)

**Tóm tắt đề bài:** Không có mômen ngoại lực đáng kể quanh trục. Sau cùng, hệ có mômen quán tính $J=I_A+I_B$.

**Hướng đi:** Chọn hệ gồm cả hai đĩa để ma sát trở thành nội lực. Bảo toàn tổng mômen động lượng, nhưng không bảo toàn động năng vì va chạm quay có tiêu tán.

**Lời giải:** Đặt $L_A=I_A\omega_A$, $L_B=I_B\omega_B$. Tổng ban đầu là $L_A+L_B$ và tổng cuối là $J\omega$, nên:

$$
\omega=\frac{L_A+L_B}{J}.
$$

Tức là tử số cộng $I_A\omega_A$ với $I_B\omega_B$, còn mẫu số cộng hai mômen quán tính. Khi hai đĩa quay ngược chiều, vẫn dùng biểu thức này nếu vận tốc góc được gán dấu nhất quán.

Để xem sự đổi động năng, đặt $\mu_I=I_AI_B/J$. Lấy động năng đầu trừ động năng cuối và khai triển bình phương, được:

$$
K_1-K_2=\tfrac12\mu_I(\omega_A-\omega_B)^2.
$$

Vế phải không âm và chỉ bằng không khi hai vận tốc góc ban đầu bằng nhau. Cơ năng mất đi chuyển thành nội năng do ma sát.

Với A là đĩa đặc $2{,}0\,\mathrm{kg}$, bán kính $0{,}20\,\mathrm m$, quay $50\,\mathrm{rad/s}$, còn B là đĩa đặc $4{,}0\,\mathrm{kg}$, bán kính $0{,}10\,\mathrm m$, quay $200\,\mathrm{rad/s}$:

$$
\begin{aligned}
I_A&=0{,}040\,\mathrm{kg\cdot m^2},\\
I_B&=0{,}020\,\mathrm{kg\cdot m^2},\\
\omega&=100\,\mathrm{rad/s}.
\end{aligned}
$$

Động năng đầu $450\,\mathrm J$, động năng cuối $300\,\mathrm J$. Hệ giữ lại hai phần ba động năng ban đầu và mất $150\,\mathrm J$ cơ năng.
:::

::: example Ví dụ 10.12: Đạn găm vào cửa

Cửa rộng $d=1{,}00\,\mathrm m$, khối lượng $M=15\,\mathrm{kg}$, quay tự do quanh trục đứng qua bản lề. Viên đạn khối lượng $m=10\,\mathrm g$ có tốc độ $v=400\,\mathrm{m/s}$ đập vuông góc vào tâm cửa và găm vào. Tìm vận tốc góc của cửa sau va chạm. Động năng có bảo toàn không?

![Hình 10.31: Chọn trục bản lề để lực từ bản lề không gây mômen quanh trục bảo toàn mômen động lượng.](../img/young-10/b-hinh-10-31.png)

**Tóm tắt đề bài:** Khoảng cách từ trục bản lề đến đường bay $l=d/2=0{,}50\,\mathrm m$. Cửa ban đầu đứng yên. Bỏ qua mômen ma sát bản lề và các mômen ngoại lực quanh trục trong thời gian va chạm.

**Hướng đi:** Chọn hệ gồm cửa và viên đạn. Động lượng tịnh tiến của hệ không được bảo toàn vì bản lề tác dụng xung lực. Tuy nhiên, xung lực này không có mômen quanh chính trục bản lề, nên thành phần mômen động lượng theo trục được bảo toàn.

**Lời giải:** Mômen động lượng ban đầu do viên đạn:

$$
L=mvl=2{,}0\,\mathrm{kg\cdot m^2/s}.
$$

Mômen quán tính cuối phải gồm cả đạn:

$$
\begin{aligned}
I_{\mathrm{cửa}}&=Md^2/3\\
&=5{,}0\,\mathrm{kg\cdot m^2},\\
I_{\mathrm{đạn}}&=ml^2\\
&=0{,}0025\,\mathrm{kg\cdot m^2}.
\end{aligned}
$$

Đặt $I=I_{\mathrm{cửa}}+I_{\mathrm{đạn}}$. Bảo toàn $L=I\omega$ cho:

$$
\omega=L/I\approx0{,}40\,\mathrm{rad/s}.
$$

Động năng đầu $K_1=mv^2/2=800\,\mathrm J$. Động năng cuối $K_2=I\omega^2/2\approx0{,}40\,\mathrm J$, chỉ còn khoảng một phần hai nghìn. Đây là va chạm không đàn hồi, nên động năng không bảo toàn.

Nếu bỏ qua cản sau va chạm, cửa cần khoảng $3{,}9\,\mathrm s$ để quay $90^\circ$. Ví dụ cho thấy bảo toàn mômen động lượng không kéo theo bảo toàn động năng.
:::

### Câu tự kiểm 10.6

Nếu băng ở các cực tan hoàn toàn và lượng nước ấy phân bố lại trên Trái Đất, độ dài ngày sẽ tăng, giảm hay không đổi? Bỏ qua mômen do Mặt Trời, Mặt Trăng và các hành tinh trong mô hình này.

<details><summary>Xem giải thích</summary>

Nước phân bố ra xa trục quay hơn làm mômen quán tính tăng. Khi mômen động lượng được bảo toàn, vận tốc góc giảm và thời gian quay một vòng tăng. Vì vậy, ngày dài hơn trong mô hình đang xét. Đây là dự đoán định tính từ phân bố khối lượng, không phải phép tính toàn bộ các quá trình làm biến đổi độ dài ngày thực tế.

</details>
