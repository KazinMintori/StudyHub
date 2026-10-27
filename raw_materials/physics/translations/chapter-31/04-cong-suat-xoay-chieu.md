## 31.4. Công suất trong mạch xoay chiều

Dòng trung bình trong một chu kỳ có thể bằng không, nhưng máy sấy tóc vẫn làm nóng không khí. Năng lượng phụ thuộc tích điện áp với dòng tại cùng thời điểm, chứ không phụ thuộc riêng dòng trung bình.

Với điện áp tức thời $v$ và dòng tức thời $i$, công suất truyền vào phần tử là

$$
p=vi.
$$

Quy ước $p>0$ khi phần tử nhận năng lượng và $p<0$ khi phần tử trả năng lượng. Trong phần này, chọn $i=I\cos\omega t$.

### Công suất trên điện trở

Với điện trở thuần, dòng và điện áp cùng pha. Nhân hai giá trị tức thời:

$$
p_R = VI\cos^2\omega t = i^2R.
$$

Dòng và điện áp cùng dương hoặc cùng âm, nên tích không âm. Điện trở nhận năng lượng theo cả hai chiều dòng, nhưng công suất thay đổi theo thời gian và bằng không khi dòng bằng không.

![Hình 31.16: Điện áp, dòng và công suất theo thời gian cho điện trở, cuộn cảm, tụ và mạch xoay chiều tổng quát.](../img/young-31/hinh-31-16.png)

Đường công suất điện trở biến thiên quanh một nửa giá trị cực đại $VI$. Do đó

$$
P_{\mathrm{av}}=\frac12VI.\tag{31.27}
$$

Đổi sang giá trị hiệu dụng:

$$
\begin{aligned}
P_{\mathrm{av}} &= \frac V{\sqrt2}\frac I{\sqrt2} \\
&= V_{\mathrm{rms}}I_{\mathrm{rms}}.
\end{aligned} \tag{31.28}
$$

Vì điện trở thuần có $V_{\mathrm{rms}}=I_{\mathrm{rms}}R$:

$$
\begin{aligned}
P_{\mathrm{av}} &= I_{\mathrm{rms}}^2R \\
&= \frac{V_{\mathrm{rms}}^2}{R} \\
&= V_{\mathrm{rms}}I_{\mathrm{rms}}.
\end{aligned} \tag{31.29}
$$

Các dạng này giống công thức một chiều nhưng dùng giá trị hiệu dụng. Chúng áp dụng trực tiếp cho điện trở thuần. Với mạch có độ lệch pha giữa dòng và điện áp nguồn, phải xét thêm hệ số công suất.

### Công suất trên cuộn cảm

Điện áp cuộn cảm thuần sớm dòng 90 độ. Trong một nửa chu kỳ, điện áp và dòng trái dấu nên $p_L<0$. Trong nửa chu kỳ còn lại, chúng cùng dấu nên $p_L>0$.

Đường công suất đối xứng quanh trục thời gian, nên công suất trung bình bằng không. Khi công suất dương, nguồn cung cấp năng lượng để tạo từ trường cuộn. Khi công suất âm, năng lượng từ trường giảm và cuộn trả năng lượng cho nguồn.

Năng lượng trao đổi trong từng phần của chu kỳ không bằng không, nhưng năng lượng nhận ròng qua một chu kỳ bằng không.

### Công suất trên tụ điện

Điện áp tụ thuần trễ dòng 90 độ. Tụ nhận năng lượng khi nạp và trả lại năng lượng khi phóng. Hai phần trao đổi cân bằng qua một chu kỳ, nên công suất trung bình của tụ lý tưởng bằng không.

Đó là sự khác nhau giữa tích trữ năng lượng và tiêu tán năng lượng. Điện trở chuyển năng lượng thành nhiệt, còn cuộn cảm và tụ lý tưởng có thể trả lại năng lượng đã tích trữ.

### Công suất trong mạch tổng quát

Đặt điện áp nguồn có góc pha $\phi$ so với dòng:

$$
\begin{aligned}
v &= V\cos(\omega t+\phi), \\
i &= I\cos\omega t.
\end{aligned}
$$

Công suất tức thời:

$$
p=VI\cos(\omega t+\phi)\cos\omega t.\tag{31.30}
$$

Để lấy trung bình, đặt $c=\cos\omega t$ và $s=\sin\omega t$. Hai ký hiệu này vẫn là các hàm thời gian. Công thức cosin tổng cho:

$$
\cos(\omega t+\phi)=c\cos\phi-s\sin\phi.
$$

Khi nhân thêm $VIc$, tách công suất thành hai số hạng:

$$
\begin{aligned}
&p_1=VI\cos\phi\,c^2,\\
&p_2=VI\sin\phi\,sc.
\end{aligned}
$$

Vì vậy:

$$
p=p_1-p_2.
$$

Số hạng thứ nhất chứa $\cos^2\omega t$, còn số hạng thứ hai chứa $\sin\omega t\cos\omega t$. Trên một chu kỳ, trung bình $\cos^2\omega t$ bằng $1/2$. Vì tích sin với cos bằng một nửa $\sin2\omega t$, trung bình số hạng thứ hai bằng không. Do đó

$$
\begin{aligned}
P_{\mathrm{av}} &= \frac12VI\cos\phi \\
&= V_{\mathrm{rms}}I_{\mathrm{rms}}\cos\phi.
\end{aligned} \tag{31.31}
$$

Trong mạch thụ động có điện trở và có dòng khác không, phần công suất dương nhận vào lớn hơn phần âm trả lại, nên công suất trung bình dương. Khi mạch chỉ chứa phần tử tích trữ lý tưởng, hai phần cân bằng.

![Hình 31.17: Thành phần điện áp cùng pha dòng là hình chiếu V cos phi, quyết định công suất trung bình.](../img/young-31/hinh-31-17.png)

Giản đồ pha cho cách nhìn hình học của công suất. Chỉ thành phần điện áp $V\cos\phi$ cùng pha với dòng đóng góp vào công suất trung bình. Khi $\phi=0$, công suất bằng $VI/2$. Khi điện áp lệch dòng 90 độ, công suất trung bình bằng không.

Ở mạch RLC nối tiếp, hình chiếu $V\cos\phi$ chính là biên độ điện áp điện trở $V_R$. Vì vậy toàn bộ công suất trung bình mà nguồn cấp được tiêu tán trên điện trở. Cuộn cảm và tụ lý tưởng không nhận năng lượng ròng qua một chu kỳ.

### Hệ số công suất

**Hệ số công suất** của mạch hình sin đang xét là $\cos\phi$. Điện trở thuần có hệ số bằng 1. Cuộn cảm hoặc tụ thuần có hệ số bằng 0.

Với RLC nối tiếp:

$$
\begin{aligned}
\cos\phi &= \frac{V_R}{V} \\
&= \frac{IR}{IZ} \\
&= \frac RZ.
\end{aligned}
$$

Hệ số nhỏ có nghĩa cần dòng lớn hơn để cấp cùng công suất trung bình ở cùng điện áp hiệu dụng:

$$
I_{\mathrm{rms}}
=\frac{P_{\mathrm{av}}}{V_{\mathrm{rms}}\cos\phi}.
$$

Dòng lớn làm tăng tổn hao trên dây truyền tải, vì tổn hao bằng bình phương dòng nhân điện trở dây. Nhiều tải máy móc có dòng trễ điện áp, tức $\phi>0$.

Nối tụ song song với tải có thể đưa hệ số công suất gần 1 hơn. Dòng nhánh tụ sớm điện áp, bù một phần dòng trễ của nhánh tải. Tụ lý tưởng trao đổi năng lượng với nguồn nhưng không tiêu thụ công suất trung bình.

::: example Ví dụ 31.6: Công suất máy sấy tóc
Máy sấy được ghi 1500 W tại điện áp 120 V. Xem máy như điện trở thuần, tìm (a) điện trở, (b) dòng hiệu dụng, (c) công suất tức thời lớn nhất.

**Nhận dạng và chuẩn bị:** 1500 W là công suất trung bình, còn 120 V là điện áp hiệu dụng. Dùng công thức điện trở thuần, không dùng trực tiếp 120 V làm biên độ.

**Lời giải:**

(a) Điện trở:

$$
\begin{aligned}
R &= \frac{V_{\mathrm{rms}}^2}{P_{\mathrm{av}}} \\
&= \frac{(120\,\mathrm V)^2}{1500\,\mathrm W} \\
&= 9{,}6\,\Omega.
\end{aligned}
$$

(b) Dòng hiệu dụng:

$$
\begin{aligned}
I_{\mathrm{rms}} &= \frac{P_{\mathrm{av}}}{V_{\mathrm{rms}}} \\
&= \frac{1500\,\mathrm W}{120\,\mathrm V} \\
&= 12{,}5\,\mathrm A.
\end{aligned}
$$

(c) Vì $\phi=0$, công suất là $p=VI\cos^2\omega t$. Giá trị lớn nhất:

$$
p_{\max} = VI = 2P_{\mathrm{av}} = 3000\,\mathrm W.
$$

**Đánh giá:** Quan hệ $I_{\mathrm{rms}}=V_{\mathrm{rms}}/R$ cũng cho 12,5 A. Công suất cực đại gấp đôi công suất trung bình của tải thuần trở hình sin này.

Khi đọc thông số thiết bị, cần phân biệt công suất đỉnh với công suất trung bình. Chẳng hạn, một thông số công suất đỉnh của bộ khuếch đại âm thanh không thể tự thay thế thông số công suất trung bình.
:::

::: example Ví dụ 31.7: Công suất mạch RLC
Với mạch ở Ví dụ 31.4, tìm (a) hệ số công suất, (b) công suất trung bình cấp cho toàn mạch và từng phần tử.

**Nhận dạng và chuẩn bị:** Dùng biên độ nguồn 50 V, biên độ dòng 0,10 A và góc pha đã tìm. Công suất trung bình toàn mạch phụ thuộc thành phần điện áp cùng pha dòng.

**Lời giải:**

(a) Vì $R=300\,\Omega$ và $Z=500\,\Omega$:

$$
\cos\phi=\frac RZ=0{,}60.
$$

(b) Công suất toàn mạch:

$$
\begin{aligned}
P_{\mathrm{av}} &= \frac12VI\cos\phi \\
&= \frac12(50)(0{,}10)(0{,}60)\,\mathrm W \\
&= 1{,}5\,\mathrm W.
\end{aligned}
$$

Công suất trung bình trên điện trở cũng là 1,5 W. Công suất trung bình trên cuộn cảm thuần và tụ lý tưởng đều bằng không.

**Đánh giá:** Đối với điện trở:

$$
\begin{aligned}
P_R &= \frac12I^2R \\
&= \frac12(0{,}10)^2(300)\,\mathrm W \\
&= 1{,}5\,\mathrm W.
\end{aligned}
$$

Kết quả phù hợp với việc toàn bộ năng lượng nhận ròng được tiêu tán trên điện trở. Công suất tức thời cuộn cảm và tụ vẫn có thể khác không, vì chúng đang nhận hoặc trả năng lượng.
:::

### Câu hỏi tự kiểm 31.4

Hình 31.16d có một phần chu kỳ mà công suất truyền vào mạch âm, nghĩa là năng lượng được lấy ra khỏi mạch.

(a) Năng lượng ấy lấy từ đâu? (i) Điện trở. (ii) Cuộn cảm. (iii) Tụ điện. (iv) Nguồn xoay chiều. (v) Nhiều hơn một trong các phần tử trên.

(b) Năng lượng đi đâu? Dùng cùng năm lựa chọn.

<details><summary>Xem đáp án và giải thích</summary>

(a) Chọn (v). Năng lượng trả lại thuộc các phần tử tích trữ, tức cuộn cảm và tụ. Điện trở tiêu tán năng lượng và không hoàn trả năng lượng đã chuyển thành nhiệt trong mô hình này.

Lựa chọn (v) chỉ ra nhiều phần tử có khả năng cung cấp phần năng lượng trả lại. Không cần cả cuộn cảm và tụ đều đang trả năng lượng tại mọi thời điểm công suất tổng âm.

(b) Chọn (iv). Công suất dương mô tả nguồn cấp năng lượng cho mạch, nên công suất tổng âm mô tả năng lượng truyền ngược về nguồn.

</details>
