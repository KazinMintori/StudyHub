## 10.2 Mômen lực và gia tốc góc của vật rắn

Tua vít chỉ bắt đầu quay nhanh hơn khi tổng mômen lực tác dụng lên nó khác không. Để định lượng sự thay đổi ấy, ta cần nối mômen ngoại lực với gia tốc góc và sự phân bố khối lượng quanh trục.

![Hình 10.7: Cán tua vít rộng hơn cho phép cùng lực tay tạo mômen lớn hơn đối với trục vít.](../img/young-10/a-hinh-10-07.png)

### Suy ra phương trình động lực học quay

Xét vật rắn quay quanh trục $z$ cố định trong hệ quy chiếu quán tính. Phần tử thứ nhất có khối lượng $m_1$, cách trục $r_1$. Hợp lực tác dụng lên phần tử có các thành phần xuyên tâm, tiếp tuyến và dọc trục.

![Hình 10.6: Chỉ thành phần lực tiếp tuyến tạo mômen theo trục quay z của phần tử đang xét.](../img/young-10/a-hinh-10-06.png)

Định luật II Newton theo phương tiếp tuyến:

$$
F_{1t}=m_1a_{1t}. \tag{10.4}
$$

Vật rắn có cùng gia tốc góc $\alpha_z$ cho mọi phần tử. Dùng $a_{1t}=r_1\alpha_z$ rồi nhân hai vế với $r_1$:

$$
F_{1t}r_1=m_1r_1^2\alpha_z. \tag{10.5}
$$

Vế trái là thành phần mômen theo trục $z$. Thành phần lực xuyên tâm đi qua trục, còn thành phần dọc trục không gây mômen theo $z$.

Với hai phần tử, cộng hai phương trình tương ứng:

$$
\tau_{1z}+\tau_{2z}=(I_1+I_2)\alpha_z,
$$

trong đó $I_1=m_1r_1^2$ và $I_2=m_2r_2^2$. Với $N$ phần tử, đặt tổng mômen và tổng mômen quán tính:

$$
\begin{aligned}
\tau_z&=\sum_{i=1}^{N}\tau_{iz},\\
I&=\sum_{i=1}^{N}m_ir_i^2.
\end{aligned} \tag{10.6}
$$

Để thấy đầy đủ phép cộng, đặt $I_i=m_ir_i^2$. Khi đó:

$$
\tau_z=\tau_{1z}+\tau_{2z}+\dots+\tau_{Nz}.
$$

$$
I=I_1+I_2+\dots+I_N.
$$

Chỉ số i chạy từ 1 đến N, nên mỗi phần tử góp đúng một số hạng trong mỗi tổng. Khi cộng toàn vật, các mômen nội lực triệt tiêu từng cặp trong mô hình các lực tương tác cùng đường nối hai phần tử.

![Hình 10.8: Hai nội lực bằng nhau, ngược chiều và cùng đường tác dụng có các mômen đối nhau quanh cùng mốc.](../img/young-10/a-hinh-10-08.png)

Do đó, $\tau_z$ còn lại là tổng mômen ngoại lực theo trục. Phương trình động lực học quay:

$$
\sum\tau_{z,\mathrm{ext}}=I\alpha_z. \tag{10.7}
$$

Ở đây, tổng được lấy trên mọi ngoại lực tác dụng lên vật. $I$ được tính đối với chính trục đang dùng. Radian không có thứ nguyên, nhưng khi ghi gia tốc góc ta vẫn có thể dùng đơn vị $\mathrm{rad/s^2}$ để phân biệt đại lượng.

Điều kiện vật rắn rất cần thiết trong phép suy ra này, vì mọi phần tử phải có cùng $\alpha_z$. Nếu vật đổi hình, không thể tự dùng cùng một $I$ không đổi trong công thức. Quan hệ tổng quát với mômen động lượng sẽ được phát triển ở mục 10.5.

Trong trọng trường đều, tổng mômen do trọng lực có thể tính bằng cách đặt trọng lượng tại khối tâm. Các lực liên kết đi qua trục không gây mômen quanh trục ấy, nhưng vẫn phải xuất hiện trong phương trình lực nếu cần tìm phản lực.

### Cách lập phương trình

Trước hết, xác định vật và vẽ mọi ngoại lực đúng điểm đặt. Chọn trục quay, chiều góc dương và các trục tịnh tiến. Với mỗi vật, viết phương trình lực và mômen trước khi thay dữ kiện. Sau đó thêm quan hệ dây không dãn, không trượt hoặc các liên kết hình học khác.

Không đặt trước lực căng bằng trọng lượng. Cũng không đặt hai phía dây qua một ròng rọc có mômen quán tính bằng nhau. Những đẳng thức ấy chỉ đúng trong những điều kiện cụ thể cần được suy ra từ phương trình.

::: example Ví dụ 10.2: Dây tháo khỏi trụ dưới lực kéo không đổi

Một dây nhẹ quấn quanh trụ đặc đồng chất khối lượng $M=50\,\mathrm{kg}$, bán kính $R=0{,}060\,\mathrm m$. Trụ quay quanh trục cố định không ma sát. Kéo dây tiếp tuyến bằng lực $F=9{,}0\,\mathrm N$. Tìm gia tốc của dây.

![Hình 10.9: Lực kéo dây tạo mômen quanh trục trụ, còn trọng lực và lực của ổ trục có đường tác dụng qua trục.](../img/young-10/a-hinh-10-09.png)

**Tóm tắt đề bài:** Trụ đặc có $I=MR^2/2$. Dây không trượt trên vành, nên gia tốc dây bằng gia tốc tiếp tuyến của vành tại điểm dây tiếp xúc.

**Hướng đi:** Dùng mômen lực để tìm gia tốc góc. Liên hệ $a=R\alpha_z$ để chuyển về gia tốc dài. Công và năng lượng không trực tiếp chứa gia tốc nên cần dùng phương trình động lực học.

**Lời giải:** Chọn chiều quay do lực kéo gây ra là dương. Mômen ngoại lực đối với trục là $FR$, nên:

$$
\begin{aligned}
\alpha_z&=FR/I\\
&=\frac{2F}{MR}\\
&=6{,}0\,\mathrm{rad/s^2}.
\end{aligned}
$$

Gia tốc dây:

$$
a=R\alpha_z=0{,}36\,\mathrm{m/s^2}.
$$

Nếu bắt đầu từ nghỉ và dây được kéo ra $2{,}0\,\mathrm m$, quan hệ $v^2=2as$ cho $v=1{,}2\,\mathrm{m/s}$. Kết quả cũng thu được từ công $Fs$ bằng động năng quay tăng thêm.
:::

::: example Ví dụ 10.3: Vật rơi làm trụ quay

Dây nhẹ quấn quanh trụ đặc khối lượng $M$, bán kính $R$, quay tự do quanh trục ngang cố định. Đầu dây gắn vật khối lượng $m$. Dây không dãn, không trượt. Tìm gia tốc đi xuống của vật và lực căng dây.

![Hình 10.10: Lập riêng phương trình tịnh tiến cho vật treo và phương trình quay cho trụ.](../img/young-10/a-hinh-10-10.png)

**Tóm tắt đề bài:** Trụ có $I=MR^2/2$. Vật treo có trọng lượng $mg$ hướng xuống và lực căng $T$ hướng lên.

**Hướng đi:** Chọn chiều xuống là dương đối với vật treo và chiều tháo dây là dương đối với trụ. Dùng quan hệ không trượt để nối gia tốc của vật với gia tốc góc.

**Lời giải:** Ba quan hệ độc lập:

$$
\begin{aligned}
&mg-T=ma,\\
&TR=I\alpha_z,\\
&a=R\alpha_z.
\end{aligned}
$$

Từ hai phương trình sau, $T=Ma/2$. Đặt $c=M/(2m)$, phương trình của vật treo cho:

$$
a=\frac{g}{1+c}.
$$

Lực căng:

$$
T=\frac{mg}{1+2m/M}.
$$

Với $M,m>0$, gia tốc nhỏ hơn $g$ và lực căng nhỏ hơn $mg$. Nếu $M$ rất lớn so với $m$, gia tốc nhỏ và lực căng gần $mg$. Khi quán tính trụ tiến về không, lực căng tiến về không và vật tiến tới rơi tự do.

Nếu vật rơi từ nghỉ qua độ cao $h$, ta được:

$$
v=\sqrt{\frac{2gh}{1+c}}.
$$

Đây cũng là kết quả của bảo toàn cơ năng, với thế năng giảm chia thành động năng vật treo và động năng quay của trụ.
:::

### Câu tự kiểm 10.2

Vật $m_1$ trượt không ma sát trên đệm khí ngang, nối bằng dây nhẹ qua ròng rọc có bán kính $R$, mômen quán tính $I$, với vật treo $m_2$. Khi thả, vật treo đi xuống và dây không trượt. Xếp độ lớn lực căng ngang $T_1$, lực căng đứng $T_2$ và trọng lượng $m_2g$ từ lớn đến nhỏ.

![Câu tự kiểm 10.2: Ròng rọc có quán tính quay nên hai lực căng không bằng nhau khi hệ tăng tốc.](../img/young-10/a-tu-kiem-10-02.png)

<details><summary>Xem giải thích</summary>

Vật treo gia tốc xuống nên $m_2g>T_2$. Ròng rọc gia tốc theo chiều kéo xuống của nhánh đứng. Hai lực căng có cùng cánh tay đòn $R$, nên cần $T_2>T_1$ để tạo mômen theo chiều ấy. Vì vậy:

$$
m_2g>T_2>T_1.
$$

</details>
