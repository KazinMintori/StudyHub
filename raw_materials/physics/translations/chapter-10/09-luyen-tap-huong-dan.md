### VP10.3.1

Trong hệ trụ và dây ở Ví dụ 10.2, trụ đặc có khối lượng $50\,\mathrm{kg}$ và bán kính $0{,}060\,\mathrm m$. Kéo dây để một điểm trên đoạn dây ngang gia tốc sang trái $0{,}60\,\mathrm{m/s^2}$. Tìm độ lớn (a) gia tốc góc của trụ, (b) mômen do dây tác dụng lên trụ và (c) lực kéo dây.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** $M=50\,\mathrm{kg}$, $R=0{,}060\,\mathrm m$, gia tốc dây $a=0{,}60\,\mathrm{m/s^2}$. Dây không trượt, trục quay cố định và không ma sát.

**Hướng đi:** Dùng liên kết không trượt để suy ra gia tốc góc. Sau đó áp dụng phương trình mômen và quan hệ cánh tay đòn của lực tiếp tuyến.

**Lời giải:**

(a) Gia tốc góc:

$$
\alpha=a/R=10\,\mathrm{rad/s^2}.
$$

(b) Mômen quán tính của trụ $I=MR^2/2=0{,}090\,\mathrm{kg\cdot m^2}$. Vì vậy:

$$
\tau=I\alpha=0{,}90\,\mathrm{N\cdot m}.
$$

(c) Lực tiếp tuyến có cánh tay đòn $R$, nên:

$$
F=\tau/R=15\,\mathrm N.
$$

</details>

### VP10.3.2

Trong hệ trụ, dây và vật treo ở Ví dụ 10.3, thay trụ đặc bằng trụ rỗng thành mỏng có khối lượng $M$, bán kính $R$. Tìm (a) gia tốc của vật treo khối lượng $m$ và (b) lực căng dây trong lúc vật rơi.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Trụ rỗng có $I=MR^2$, dây không dãn và không trượt. Chọn chiều vật rơi là dương.

**Hướng đi:** Lập phương trình lực cho vật treo và mômen cho trụ. Khối lượng như cũ nhưng mômen quán tính đã đổi, nên phải thay đúng biểu thức $I$.

**Lời giải:**

$$
\begin{aligned}
&mg-T=ma,\\
&TR=MR^2\alpha,\\
&a=R\alpha.
\end{aligned}
$$

Hai phương trình sau cho $T=Ma$. Thay vào phương trình đầu, được:

$$
\begin{aligned}
a&=\frac{mg}{m+M},\\
T&=\frac{mMg}{m+M}.
\end{aligned}
$$

Đối chiếu trụ đặc có cùng $M,R$, trụ rỗng có quán tính quay lớn hơn nên vật rơi chậm hơn và lực căng lớn hơn.

</details>

### VP10.3.3

Xô khối lượng $m$ treo ở đầu dây quấn quanh tang bán kính $R$, khối lượng $M$. Tang quay quanh trục ngang cố định với ma sát không đáng kể, nhưng không đồng chất và chưa biết mômen quán tính. Khi thả xô từ nghỉ, đo được gia tốc đi xuống $a$. Tìm (a) lực căng dây và (b) mômen quán tính của tang.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Đã biết $m,R,a$. Không được giả sử $I=MR^2/2$ vì tang không phải trụ đồng chất.

**Hướng đi:** Từ gia tốc của xô, dùng định luật II Newton để tìm lực căng. Lực căng tạo mômen lên tang, còn không trượt nối gia tốc xô với gia tốc góc.

**Lời giải:**

(a) $mg-T=ma$, nên:

$$
T=m(g-a).
$$

(b) Từ $TR=I\alpha$ và $\alpha=a/R$:

$$
I=mR^2(g/a-1).
$$

Để có mômen quán tính dương trong mô hình này, số đo phải thỏa $0<a<g$. Khối lượng tang không tự quyết định $I$ khi chưa biết cách phân bố khối lượng.

</details>

### VP10.3.4

Gắn động cơ vào trục trụ đặc khối lượng $M$, bán kính $R$ của Ví dụ 10.3. Động cơ kéo vật treo khối lượng $m$ đi lên với gia tốc $a$. Tìm (a) lực căng dây, (b) độ lớn mômen do dây tác dụng lên trụ và (c) độ lớn mômen động cơ.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Trụ có $I=MR^2/2$. Dây không trượt và chuyển động lên. Chọn chiều cuốn dây lên là chiều góc dương.

**Hướng đi:** Lực căng phải thắng trọng lực và gây gia tốc lên. Trên trụ, mômen lực căng ngược chiều cuốn dây, nên động cơ phải vừa thắng mômen ấy vừa làm trụ tăng tốc góc.

**Lời giải:**

(a) $T-mg=ma$, nên $T=m(g+a)$.

(b) Độ lớn mômen do dây:

$$
\tau_T=mR(g+a).
$$

(c) Mômen động cơ thỏa $\tau_m-TR=I\alpha$, với $\alpha=a/R$. Vì vậy:

$$
\tau_m=TR+\tfrac12MRa.
$$

Trong đó $T=m(g+a)$ đã được tính ở phần (a). Mômen động cơ lớn hơn mômen do dây vì trụ đang tăng tốc góc.

</details>

### VP10.7.1

Trong yo-yo của Ví dụ 10.6, thay trụ đặc bằng trụ rỗng khối lượng $M$, bán kính ngoài $R$, bán kính trong $R/2$. Tìm (a) gia tốc khối tâm hướng xuống và (b) lực căng dây.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Dây quấn ở bán kính ngoài, đầu dây cố định và không trượt.

**Hướng đi:** Tính mômen quán tính của trụ rỗng thành dày. Kết hợp phương trình lực, mômen quanh khối tâm và điều kiện không trượt.

**Lời giải:**

$$
I=\tfrac12M[R^2+(R/2)^2].
$$

Suy ra $I=5MR^2/8$. Từ $TR=I(a/R)$, lực căng là $T=5Ma/8$. Thay vào $Mg-T=Ma$:

$$
\begin{aligned}
a&=\frac8{13}g,\\
T&=\frac5{13}Mg.
\end{aligned}
$$

</details>

### VP10.7.2

Một vỏ cầu mỏng khối lượng $M$ lăn không trượt trên dốc góc $\beta$. Tìm (a) gia tốc khối tâm, (b) độ lớn ma sát do dốc tác dụng và (c) độ lớn mômen của ma sát quanh tâm. Gọi bán kính cầu là $R$.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** $I=2MR^2/3$, chọn chiều xuống dốc là dương. Ma sát nghỉ hướng lên dốc.

**Hướng đi:** Ma sát tạo mômen quanh tâm. Dùng quan hệ không trượt để khử gia tốc góc khỏi phương trình quay, rồi kết hợp phương trình tịnh tiến.

**Lời giải:**

$$
\begin{aligned}
&Mg\sin\beta-f=Ma,\\
&fR=\tfrac23MR^2(a/R).
\end{aligned}
$$

Từ đó $f=2Ma/3$. Các kết quả:

$$
\begin{aligned}
a&=\tfrac35g\sin\beta,\\
f&=\tfrac25Mg\sin\beta,\\
\tau&=fR.
\end{aligned}
$$

</details>

### VP10.7.3

Làm lại thí nghiệm yo-yo của Ví dụ 10.6, nhưng di chuyển đầu dây thẳng đứng sao cho lực căng bằng $2Mg/3$. (a) Khối tâm gia tốc với độ lớn bao nhiêu và theo chiều nào? (b) Gia tốc góc của trụ quanh trục riêng bằng bao nhiêu?

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Trụ đặc có $I=MR^2/2$, lực căng $T=2Mg/3$. Đầu dây không còn cố định.

**Hướng đi:** Tính gia tốc khối tâm trực tiếp từ hợp lực và gia tốc góc từ mômen. Không đặt $a=R\alpha$ cho khối tâm vì điểm giữ dây đang chuyển động.

**Lời giải:**

(a) Chọn chiều xuống là dương. $Mg-T=Ma$ cho:

$$
a=g/3.
$$

Khối tâm gia tốc xuống vì trọng lực lớn hơn lực căng.

(b) Lực căng có cánh tay đòn $R$:

$$
\alpha=TR/I=\frac{4g}{3R}.
$$

Gia tốc góc theo chiều tháo dây. Hai kết quả không thỏa $a=R\alpha$, phù hợp với việc đầu dây chuyển động.

</details>

### VP10.7.4

Trụ đặc khối lượng $M$ đặt trên dốc góc $\beta$, hệ số ma sát nghỉ $\mu_s$. (a) Nếu lăn không trượt xuống dốc, ma sát có độ lớn bao nhiêu? (b) Tăng góc dốc thì trụ bắt đầu trượt khi góc vượt một giá trị tới hạn. Tìm góc ấy.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** $I=MR^2/2$. Phản lực pháp tuyến $N=Mg\cos\beta$.

**Hướng đi:** Trước hết tìm ma sát cần thiết cho lăn không trượt bằng động lực học. Sau đó so với giá trị lớn nhất $\mu_sN$, không tự đặt ma sát bằng giá trị cực đại trong mọi trường hợp.

**Lời giải:** Phương trình quay và không trượt cho $f=Ma/2$. Kết hợp $Mg\sin\beta-f=Ma$:

$$
\begin{aligned}
a&=\tfrac23g\sin\beta,\\
f&=\tfrac13Mg\sin\beta.
\end{aligned}
$$

Ở ngưỡng trượt, $f=\mu_sMg\cos\beta$. Rút gọn các thừa số dương, được:

$$
\tan\beta_c=3\mu_s.
$$

Do đó, $\beta_c=\arctan(3\mu_s)$. Dưới góc này, ma sát nghỉ có thể cung cấp mômen cần thiết.

</details>

### VP10.12.1

Hai đĩa của Ví dụ 10.11 có $I_B=I_A/4$ và ban đầu $\omega_B=\omega_A/2$, cùng chiều. (a) Tìm vận tốc góc chung sau khi ghép. (b) Tìm tỷ phần động năng quay còn lại sau khi hai đĩa quay chung.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Tổng mômen quán tính $J=5I_A/4$. Không có mômen ngoại lực quanh trục.

**Hướng đi:** Bảo toàn mômen động lượng để tìm vận tốc góc cuối. Tính động năng hai thời điểm riêng, vì ma sát làm động năng giảm.

**Lời giải:**

$$
\begin{aligned}
L_1&=I_A\omega_A(1+1/8),\\
\omega&=L_1/J\\
&=\tfrac9{10}\omega_A.
\end{aligned}
$$

Đặt $E=I_A\omega_A^2$. Động năng đầu và cuối:

$$
\begin{aligned}
K_1&=\tfrac{17}{32}E,\\
K_2&=\tfrac{81}{160}E.
\end{aligned}
$$

Tỷ phần còn lại $K_2/K_1=81/85\approx0{,}953$.

</details>

### VP10.12.2

Giữ các mômen quán tính và độ lớn vận tốc góc của VP10.12.1, nhưng hai đĩa ban đầu quay ngược chiều. (a) Tìm vận tốc góc chung. (b) Tìm tỷ phần động năng quay còn lại.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Chọn chiều quay ban đầu của A là dương. Khi đó vận tốc góc của B bằng $-\omega_A/2$ và $J=5I_A/4$.

**Hướng đi:** Cộng mômen động lượng có dấu. Khi tính động năng, dùng bình phương vận tốc góc nên dấu quay không làm động năng âm.

**Lời giải:**

$$
\begin{aligned}
L_1&=I_A\omega_A(1-1/8),\\
\omega&=L_1/J\\
&=\tfrac7{10}\omega_A.
\end{aligned}
$$

Hệ quay theo chiều ban đầu của A. Đặt $E=I_A\omega_A^2$, ta có $K_1=17E/32$ và $K_2=49E/160$. Do đó:

$$
K_2/K_1=49/85\approx0{,}576.
$$

</details>

### VP10.12.3

Thay vì đập vào tâm cửa ở Ví dụ 10.12, viên đạn găm vào mép cửa xa bản lề nhất. (a) Tìm vận tốc góc ngay sau va chạm. (b) Tìm tỷ phần động năng viên đạn ban đầu còn lại dưới dạng động năng hệ sau va chạm. Dùng cửa $15\,\mathrm{kg}$, rộng $1{,}00\,\mathrm m$ và đạn $0{,}010\,\mathrm{kg}$, tốc độ $400\,\mathrm{m/s}$.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Cánh tay đòn của động lượng đạn nay là $d=1{,}00\,\mathrm m$. Mômen quán tính cửa $I_c=5{,}0\,\mathrm{kg\cdot m^2}$.

**Hướng đi:** Bảo toàn mômen động lượng quanh bản lề, tính cả mômen quán tính của viên đạn sau khi găm. Sau đó so động năng cuối với động năng đạn đầu.

**Lời giải:** Tổng mômen quán tính cuối là $I=I_c+md^2$, bằng $5{,}01\,\mathrm{kg\cdot m^2}$. Mômen động lượng đầu $L=mvd=4{,}0\,\mathrm{kg\cdot m^2/s}$, nên:

$$
\omega=L/I\approx0{,}798\,\mathrm{rad/s}.
$$

Báo khoảng $0{,}80\,\mathrm{rad/s}$. Tỷ phần động năng:

$$
\frac{K_2}{K_1}=\frac{md^2}{I}=\frac1{501}.
$$

Giá trị này xấp xỉ $0{,}0020$, tức $0{,}20\%$.

</details>

### VP10.12.4

Vỏ cầu mỏng khối lượng $M$, bán kính $R$ có thể quay tự do quanh trục đứng qua tâm và ban đầu đứng yên. Viên đất sét cùng khối lượng $M$ bay ngang với tốc độ $v$, sượt qua xích đạo cầu và tiếp tục bay với tốc độ $v/2$.

(a) Tìm mômen động lượng của đất sét đối với trục trước và sau tương tác. (b) Tìm tốc độ góc của vỏ cầu sau đó. (c) Tìm tỷ phần động năng ban đầu của đất sét còn lại trong hệ cầu và đất sét.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Cánh tay đòn của đường bay là $R$. Vỏ cầu có $I=2MR^2/3$. Đất sét không dính lại mà tiếp tục bay sau khi sượt qua.

**Hướng đi:** Bảo toàn mômen động lượng theo trục đứng của hệ hai vật. Phần mômen động lượng đất sét mất đi được truyền cho cầu. Cộng động năng đất sét và động năng quay của cầu khi tính tỷ phần cuối.

**Lời giải:**

(a) $L_{c,1}=MRv$, còn $L_{c,2}=MRv/2$, cùng dấu theo chiều đường bay ban đầu.

(b) Cầu nhận mômen động lượng $MRv/2$. Vì vậy:

$$
I\omega=MRv/2,
$$

$$
\omega=\frac{3v}{4R}.
$$

(c) Động năng đất sét sau tương tác bằng $Mv^2/8$, còn động năng quay của cầu bằng $3Mv^2/16$. Tổng là $K_2=5Mv^2/16$, so với $K_1=Mv^2/2$:

$$
K_2/K_1=5/8.
$$

</details>
