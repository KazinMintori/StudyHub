## 31.1. Giản đồ pha và dòng xoay chiều

Muốn cấp dòng xoay chiều cho mạch, cần nguồn điện áp hoặc suất điện động xoay chiều. Một vòng dây quay đều trong từ trường tạo suất điện động hình sin, như máy phát đã khảo sát ở Ví dụ 29.3. Đó là mô hình cơ bản của máy phát điện xoay chiều.

### Đại lượng tức thời và biên độ

Nguồn xoay chiều là thiết bị cung cấp điện áp hoặc dòng biến thiên hình sin. Ký hiệu nguồn trên sơ đồ là một vòng tròn có nét hình sin bên trong.

![Ký hiệu: Nguồn điện xoay chiều trên sơ đồ mạch.](../img/young-31/ky-hieu-nguon-xoay-chieu.png)

Chọn gốc thời gian thích hợp, điện áp có thể được viết

$$
v(t)=V\cos\omega t.\tag{31.1}
$$

Chữ thường $v$ chỉ điện áp tức thời. Chữ hoa $V$ là điện áp lớn nhất về độ lớn, gọi là biên độ điện áp. Tần số góc $\omega=2\pi f$ liên hệ với số chu kỳ trong một giây là $f$.

![Hình 31.1: Điện áp nguồn hình sin lần lượt dương, bằng không và âm khi nguồn đi qua các phần của chu kỳ.](../img/young-31/hinh-31-01.png)

Hệ điện thương mại ở Hoa Kỳ và Canada dùng tần số 60 Hz trong mô hình lưới đang xét, tương ứng khoảng $377\,\mathrm{rad/s}$. Một tần số lưới khác được dùng ở nhiều nơi là 50 Hz, tương ứng khoảng $314\,\mathrm{rad/s}$.

Tương tự, một dòng hình sin có biên độ $I$ được viết

$$
i(t)=I\cos\omega t.\tag{31.2}
$$

Biên độ không phải giá trị tức thời. Tại những thời điểm nhất định, dòng có thể bằng không hoặc âm dù $I$ luôn là độ lớn không âm.

Hai cách viết điện áp và dòng ở trên chọn mốc pha riêng cho từng đại lượng. Khi xét điện áp và dòng của cùng một mạch, nói chung phải giữ góc lệch pha giữa chúng, không tự cho rằng cả hai cùng đạt cực đại tại $t=0$.

### Biểu diễn bằng giản đồ pha

Một đại lượng hình sin có thể được biểu diễn bằng hình chiếu của một vector quay lên trục ngang. Độ dài vector bằng biên độ, còn vector quay ngược chiều kim đồng hồ với tốc độ góc $\omega$. Vector biểu diễn này được gọi là **vector pha** (phasor), và hình chứa nó là giản đồ pha.

![Hình 31.2: Hình chiếu ngang của vector pha quay đều cho giá trị dòng tức thời.](../img/young-31/hinh-31-02.png)

Với vector có độ dài $I$ và góc $\omega t$ so với trục ngang, hình chiếu bằng $I\cos\omega t$. Đó là lý do chọn cosin trong (31.2). Nếu chọn sin thì phải dùng hình chiếu hoặc gốc góc tương ứng.

::: warning Ý nghĩa của vector pha
Vector pha không phải vector vật lý chỉ một hướng trong không gian như vận tốc hoặc điện trường. Nó là đối tượng hình học dùng để biểu diễn pha và biên độ của một đại lượng biến thiên. Cộng các đại lượng hình sin có khác pha trở thành phép cộng vector trong giản đồ này.

Một vector pha đã được dùng để biểu diễn li độ dao động điều hòa. Ở đây nhiều vector pha được dùng để cộng điện áp và dòng. Cách biểu diễn cũng sẽ được dùng khi phân tích giao thoa ánh sáng ở các chương 35, 36.
:::

### Dòng xoay chiều sau chỉnh lưu

Điện kế d’Arsonval đo dòng không đổi qua mômen lực tác dụng lên cuộn quay. Nếu cho dòng hình sin qua điện kế, mômen đổi chiều sau mỗi nửa chu kỳ. Kim có thể rung khi tần số đủ thấp, nhưng độ lệch trung bình bằng không. Vì vậy điện kế ấy đứng riêng chưa thích hợp để đo dòng xoay chiều.

Diode dẫn tốt hơn theo một chiều so với chiều ngược lại. Diode lý tưởng có điện trở bằng không theo chiều dẫn và vô hạn theo chiều chặn. Mạch chỉnh lưu toàn sóng ở Hình 31.3 dùng diode để giữ dòng qua điện kế luôn cùng chiều, dù dòng nguồn đổi chiều.

![Hình 31.3: Mạch chỉnh lưu toàn sóng làm dòng qua điện kế luôn cùng chiều, với đồ thị dòng và điện lượng sau chỉnh lưu.](../img/young-31/hinh-31-03.png)

Dòng chỉnh lưu vẫn biến thiên về độ lớn. **Dòng trung bình sau chỉnh lưu** $I_{\mathrm{rav}}$ được định nghĩa sao cho trong một số nguyên chu kỳ, điện lượng qua điện kế bằng điện lượng của dòng không đổi $I_{\mathrm{rav}}$ trong cùng thời gian.

Điện lượng là diện tích dưới đồ thị dòng theo thời gian, vì $i=dq/dt$. Ta cần diện tích hình chữ nhật có cùng diện tích với đường $|I\cos\omega t|$. Lấy trung bình trên một chu kỳ $T$:

$$
\begin{aligned}
I_{\mathrm{rav}} &= \frac1T\int_0^T|i(t)|\,dt \\
&= \frac{I}{2\pi}\int_0^{2\pi}|\cos\theta|\,d\theta \\
&= \frac{I}{2\pi}\,4 \\
&= \frac2\pi I \\
&\approx 0{,}637I.\tag{31.3}
\end{aligned} \tag{31.3}
$$

Ở bước tích phân, bốn phần tư chu kỳ có cùng diện tích. Hệ số $2/\pi$ cũng là trung bình của $|\sin\theta|$ trên một chu kỳ. Độ lệch điện kế tỉ lệ với dòng trung bình sau chỉnh lưu. Thang đo có thể được hiệu chuẩn để chỉ biên độ, trung bình chỉnh lưu hoặc giá trị hiệu dụng.

### Giá trị hiệu dụng

Một cách hữu ích hơn để mô tả đại lượng có cả dấu dương lẫn âm là **giá trị hiệu dụng**, tức căn trung bình bình phương (rms). Thao tác gồm bình phương giá trị tức thời, lấy trung bình rồi lấy căn. Với dòng điện:

$$
I_{\mathrm{rms}}=\sqrt{\overline{i^2}}.
$$

Ngay khi $i$ âm, bình phương $i^2$ vẫn không âm. Giá trị hiệu dụng chỉ bằng không nếu dòng bằng không ở mọi thời điểm trong mô hình đang xét.

![Hình 31.4: Bốn bước lấy giá trị hiệu dụng gồm vẽ dòng, bình phương dòng, lấy trung bình bình phương và lấy căn.](../img/young-31/hinh-31-04.png)

Với dòng hình sin ở (31.2), dùng công thức góc đôi để khai triển:

$$
i^2 =I^2\cos^2\omega t.
$$

$$
\cos^2\omega t&=\frac12 +\frac12\cos2\omega t.
$$

$$
i^2&=\frac12I^2 +\frac12I^2\cos2\omega t.
$$

Trung bình của cosin trên một số nguyên chu kỳ bằng không. Do đó trung bình bình phương là $I^2/2$, suy ra

$$
I_{\mathrm{rms}}=\frac I{\sqrt2}.\tag{31.4}
$$

Điện áp hình sin có quan hệ tương tự:

$$
V_{\mathrm{rms}}=\frac V{\sqrt2}.\tag{31.5}
$$

Hai hệ số $1/\sqrt2$ này cần dạng hình sin. Với dạng sóng khác, phải dùng định nghĩa căn trung bình bình phương, không tự áp hệ số của cosin.

Có thể biến ampe kế chỉnh lưu thành vôn kế bằng cách thêm điện trở nối tiếp như trường hợp một chiều. Đồng hồ xoay chiều thường được hiệu chuẩn để chỉ giá trị hiệu dụng. Điện áp và dòng trong mô hình phân phối điện cũng được nêu theo giá trị ấy.

![Hình 31.5: Ổ điện trong ví dụ có điện áp hiệu dụng 120 V, khác biên độ điện áp tức thời.](../img/young-31/hinh-31-05.png)

Với nguồn 120 V hiệu dụng:

$$
\begin{aligned}
V &= \sqrt2V_{\mathrm{rms}} \\
&\approx 170\,\mathrm V.
\end{aligned}
$$

Ở tần số 60 Hz, điện áp đi từ khoảng $+170\,\mathrm V$ đến $-170\,\mathrm V$ rồi trở lại 60 lần mỗi giây. Giá trị 120 V không phải biên độ của đồ thị này.

::: example Ví dụ 31.1: Dòng điện của máy tính để bàn
Nhãn phía sau máy tính ghi máy lấy dòng 2,7 A từ đường điện 120 V, 60 Hz. Theo mô hình dòng hình sin, tìm (a) dòng trung bình, (b) trung bình bình phương dòng và (c) biên độ dòng.

**Nhận dạng và chuẩn bị:** Dòng 2,7 A ghi trên nhãn là giá trị hiệu dụng. Trung bình ở (a) được lấy trên một hoặc một số nguyên chu kỳ của dòng chưa chỉnh lưu.

**Lời giải:**

(a) Nửa chu kỳ dương và âm có diện tích đối nhau nên $\overline i=0$.

(b) Theo định nghĩa giá trị hiệu dụng:

$$
\begin{aligned}
\overline{i^2} &= I_{\mathrm{rms}}^2 \\
&= (2{,}7\,\mathrm A)^2 \\
&\approx 7{,}3\,\mathrm{A^2}.
\end{aligned}
$$

(c) Biên độ là

$$
\begin{aligned}
I &= \sqrt2I_{\mathrm{rms}} \\
&\approx 3{,}8\,\mathrm A.
\end{aligned}
$$

![Hình 31.6: Đồ thị dòng i có trung bình bằng không, trong khi bình phương dòng có trung bình dương và xác định giá trị hiệu dụng.](../img/young-31/hinh-31-06.png)

**Đánh giá:** Công suất nhiệt tức thời trên điện trở là $i^2R$, nên trung bình công suất là $\overline{i^2}R=I_{\mathrm{rms}}^2R$. Dòng trung bình bằng không không có nghĩa công suất trung bình bằng không. Giá trị hiệu dụng cho phép mô tả tác dụng nhiệt này, sẽ được dùng trong phần công suất xoay chiều.
:::

### Câu hỏi tự kiểm 31.1

Bốn vector pha trong hình có cùng tần số góc và quay ngược chiều kim đồng hồ. Ở thời điểm được vẽ, vector nào tương ứng với (a) dòng dương đang tăng, (b) dòng dương đang giảm về không, (c) dòng âm có độ lớn đang tăng, (d) dòng âm có độ lớn đang giảm về không?

![Tự kiểm 31.1: Bốn vector pha A, B, C, D ở bốn vị trí góc khác nhau và cùng quay ngược chiều kim đồng hồ.](../img/young-31/tu-kiem-31-01.png)

<details><summary>Xem đáp án và giải thích</summary>

Đáp án theo thứ tự (a)–(d) là D, A, B, C. Dòng là hình chiếu ngang của vector pha.

- A có hình chiếu dương nhưng đang tiến về không khi vector quay.
- B có hình chiếu âm và đang trở nên âm hơn.
- C có hình chiếu âm nhưng đang tiến về không.
- D có hình chiếu dương và đang lớn hơn.

Có thể dùng $i=I\cos\theta$ và $di/dt=-\omega I\sin\theta$ để kiểm tra đồng thời dấu dòng và dấu tốc độ biến thiên. Với dòng âm, độ lớn tăng khi đạo hàm âm, còn độ lớn giảm khi đạo hàm dương.

</details>
