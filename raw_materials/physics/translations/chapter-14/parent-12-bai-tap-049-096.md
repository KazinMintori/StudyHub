### 14.49 (••): Lực và gia tốc của con lắc

Một quả cầu nhỏ khối lượng $m$ gắn ở đầu thanh không khối lượng, dài $L$, có đầu trên quay quanh một trục cố định. Kéo thanh lệch góc $\theta$ so với phương thẳng đứng rồi thả từ nghỉ. (a) Vẽ con lắc ngay sau khi thả, các vectơ lực tác dụng lên quả cầu và vectơ gia tốc, chú ý chính xác hướng của chúng. Gia tốc dài lúc ấy bằng bao nhiêu? (b) Làm lại phần (a) khi thanh lệch góc $\theta/2$. (c) Làm lại phần (a) khi thanh thẳng đứng. Tốc độ quả cầu lúc ấy bằng bao nhiêu?

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Con lắc thanh cứng thả nghỉ từ góc $\theta$, cần phân biệt gia tốc tiếp tuyến và hướng tâm ở ba vị trí.

**Hướng đi:** Dùng bảo toàn cơ năng để tìm tốc độ, rồi chiếu định luật II Newton lên tiếp tuyến và bán kính. Gia tốc hướng tâm bằng không ngay lúc thả nhưng xuất hiện khi quả cầu có tốc độ, nên gia tốc toàn phần thường không cùng hướng tiếp tuyến.

**Lời giải:**

Gọi $\alpha$ là góc lệch tức thời, $\mathbf e_r$ hướng từ trục tới quả cầu và $\mathbf e_t$ hướng theo chiều tăng góc. Chọn phía thả có góc dương. Cơ năng cho:

$$
v^2=2gL(\cos\alpha-\cos\theta).
$$

Các thành phần gia tốc là:

$$
a_t=-g\sin\alpha,
$$

$$
a_r=-\frac{v^2}{L}.
$$

Trọng lực luôn thẳng đứng xuống. Lực của thanh hướng dọc thanh. Với biên độ nhỏ hơn $90^\circ$, lực này hướng về trục và có độ lớn:

$$
S=mg\cos\alpha+\frac{mv^2}{L}.
$$

![Ba sơ đồ lực và các thành phần gia tốc tại góc thả, nửa góc thả và vị trí thấp nhất](/vat-ly-1/bai-giang/img/young-14/solution-14-49-forces.svg)

Hình 14.49: Mũi tên lực và gia tốc được tách thành hai cột. Độ dài vector dùng thang riêng cho mỗi cột. Hình minh họa phía phải quỹ đạo với một góc thả cụ thể, còn các công thức áp dụng cho góc thả bất kỳ trong miền chuyển động đang xét.

(a) Khi $\alpha=\theta$, quả cầu chưa có tốc độ. Do đó $a_r=0$, gia tốc hướng tiếp tuyến về vị trí thấp nhất và có độ lớn $g\sin\theta$. Lực thanh bằng $mg\cos\theta$.

(b) Đặt $c=\cos(\theta/2)-\cos\theta$. Khi $\alpha=\theta/2$:

$$
v^2=2gLc,
$$

$$
a_t=-g\sin(\theta/2),
$$

$$
a_r=-2gc.
$$

Gia tốc toàn phần hướng chếch giữa hướng tiếp tuyến về đáy và hướng về trục. Độ lớn và lực thanh là:

$$
|\mathbf a|=g\sqrt{\sin^2(\theta/2)+4c^2},
$$

$$
S=mg[\cos(\theta/2)+2c].
$$

(c) Ở đáy, gia tốc tiếp tuyến bằng không nhưng gia tốc hướng tâm khác không:

$$
v=\sqrt{2gL(1-\cos\theta)},
$$

$$
|\mathbf a|=2g(1-\cos\theta),
$$

$$
S=mg(3-2\cos\theta).
$$

Gia tốc thẳng đứng lên. Lực thanh hướng lên và lớn hơn trọng lực. Các kết quả năng lượng này không cần xấp xỉ góc nhỏ. Nếu thả ở góc lớn khiến $S$ mang dấu âm, thanh cứng chịu nén và lực dọc thanh đổi chiều.

</details>

### 14.50 (••): Vành tròn treo trên đinh

Treo một vành tròn mảnh lên chiếc đinh nằm ngang sao cho mỗi dao động góc nhỏ hoàn chỉnh kéo dài $2{,}0\,\mathrm s$. Bán kính vành phải bằng bao nhiêu?

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Vành mảnh quay quanh điểm trên chu vi, chu kỳ $T=2{,}0\,\mathrm s$.

**Hướng đi:** Dùng công thức con lắc vật lý vì khối lượng phân bố quanh cả vành. Định lý trục song song đưa mômen quán tính từ tâm tới điểm treo.

**Lời giải:**

Khoảng cách từ trục treo đến tâm khối là $R$. Mômen quán tính đối với đinh bằng:

$$
I=mR^2+mR^2=2mR^2.
$$

Vì vậy:

$$
T=2\pi\sqrt{\frac{2R}{g}},
$$

$$
R=\frac{gT^2}{8\pi^2}.
$$

Với $g=9{,}80\,\mathrm{m/s^2}$, bán kính cần có là $R=0{,}50\,\mathrm m$ (giá trị chưa làm tròn $0{,}4965\,\mathrm m$).

</details>

### 14.51 (•): Phân bố khối lượng và chu kỳ

Hai con lắc có cùng chiều dài $L$ và tổng khối lượng $m$. Con lắc A có quả cầu rất nhỏ ở đầu thanh đồng chất không khối lượng. Ở con lắc B, quả cầu mang nửa tổng khối lượng, còn thanh đồng chất mang nửa còn lại. Tìm chu kỳ dao động góc nhỏ của mỗi con lắc. Con lắc nào mất nhiều thời gian hơn cho một lần đung đưa?

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Cùng chiều dài và khối lượng, nhưng con lắc B có một phần khối lượng phân bố dọc thanh.

**Hướng đi:** So sánh tỷ số $I/(mgd)$ trong công thức chu kỳ con lắc vật lý. Việc đưa khối lượng lên thanh làm thay đổi đồng thời mômen quán tính và vị trí tâm khối.

**Lời giải:**

Đối với A, $I_A=mL^2$ và $d_A=L$, nên:

$$
T_A=2\pi\sqrt{\frac{L}{g}}.
$$

Đối với B, mômen quán tính gồm quả cầu và thanh:

$$
\begin{aligned}
I_B&=\frac{mL^2}{2}+\frac{mL^2}{6}\\
&=\frac{2mL^2}{3}.
\end{aligned}
$$

Tâm khối của B cách điểm treo:

$$
d_B=\frac{L+L/2}{2} =\frac{3L}{4}.
$$

Suy ra:

$$
T_B=2\pi\sqrt{\frac{8L}{9g}},
$$

$$
\frac{T_B}{T_A}=\sqrt{\frac89}\approx0{,}943.
$$

Con lắc A có chu kỳ dài hơn. Kết luận cũng đúng khi so sánh nửa chu kỳ.

</details>

### 14.52 (••): Mỏ lết làm con lắc vật lý

Một mỏ lết khối lượng $1{,}80\,\mathrm{kg}$ quay quanh trục cách tâm khối $0{,}250\,\mathrm m$. Chu kỳ dao động góc nhỏ bằng $0{,}940\,\mathrm s$. (a) Tìm mômen quán tính của mỏ lết đối với trục treo. (b) Nếu ban đầu kéo mỏ lết lệch $0{,}400\,\mathrm{rad}$ khỏi cân bằng rồi thả, tốc độ góc khi đi qua vị trí cân bằng bằng bao nhiêu?

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** $m=1{,}80\,\mathrm{kg}$, $d=0{,}250\,\mathrm m$, chu kỳ góc nhỏ $T=0{,}940\,\mathrm s$, góc thả $0{,}400\,\mathrm{rad}$.

**Hướng đi:** Suy ra mômen quán tính từ chu kỳ góc nhỏ. Sau đó dùng bảo toàn cơ năng với độ tăng độ cao chính xác để tìm tốc độ góc, vì góc thả ở phần (b) không cần bị thay bằng xấp xỉ góc nhỏ.

**Lời giải:**

(a) Từ chu kỳ con lắc vật lý:

$$
\begin{aligned}
I&=mgd\left(\frac{T}{2\pi}\right)^2\\
&=0{,}0987\,\mathrm{kg\,m^2}.
\end{aligned}
$$

(b) Độ giảm thế năng từ góc thả $\theta_0$ đến cân bằng chuyển hoàn toàn thành động năng quay:

$$
\frac12I\Omega^2=mgd(1-\cos\theta_0).
$$

Do đó:

$$
\begin{aligned}
\Omega&=\sqrt{\frac{2mgd(1-\cos\theta_0)}{I}}\\
&\approx2{,}66\,\mathrm{rad/s}.
\end{aligned}
$$

Nếu dùng mô hình dao động điều hòa cho cả phần (b), ta được $\Omega\approx2{,}67\,\mathrm{rad/s}$. Đây là kết quả xấp xỉ góc nhỏ, lệch khoảng $0{,}67\%$ so với biểu thức năng lượng chính xác.

</details>

### 14.53 (••): Quả cầu nhỏ và quả cầu lớn

Hai con lắc ở Hình 14.53 đều gồm quả cầu đặc đồng chất khối lượng $M$ gắn với thanh cứng không khối lượng. Quả cầu A rất nhỏ, còn quả cầu B lớn hơn nhiều. Tâm mỗi quả cầu cách trục treo $L$. Với B, khoảng cách từ trục treo đến mặt trên quả cầu là $L/2$. Tìm chu kỳ dao động góc nhỏ của mỗi con lắc. Quả cầu nào mất nhiều thời gian hơn để hoàn thành một dao động?

![Hai con lắc có tâm quả cầu cùng cách trục L, quả cầu B có bán kính L chia hai](/vat-ly-1/bai-giang/img/young-14/r-exercises-e14-53.png)

Hình 14.53: Các kích thước xác định vị trí tâm và bán kính của hai quả cầu.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** A gần như chất điểm, B có bán kính $R=L/2$. Cả hai có khoảng cách tâm khối đến trục bằng $L$.

**Hướng đi:** Dùng con lắc vật lý và giữ mômen quán tính riêng của quả cầu B. Bán kính lớn làm tăng mômen quán tính mà không đổi mômen phục hồi ở cùng góc lệch.

**Lời giải:**

Với A, bỏ qua kích thước quả cầu:

$$
T_A=2\pi\sqrt{\frac Lg}.
$$

Với B, định lý trục song song cho:

$$
\begin{aligned}
I_B&=ML^2+\frac25M\left(\frac L2\right)^2\\
&=\frac{11}{10}ML^2.
\end{aligned}
$$

Do đó:

$$
T_B=2\pi\sqrt{\frac{11L}{10g}},
$$

$$
\frac{T_B}{T_A}=\sqrt{\frac{11}{10}} \approx1{,}049.
$$

Quả cầu B có chu kỳ dài hơn khoảng $4{,}9\%$.

</details>

### 14.54 (••, CP): Quả trang trí hình cầu rỗng

Một quả trang trí hình cầu rỗng khối lượng $M=0{,}015\,\mathrm{kg}$, bán kính $R=0{,}050\,\mathrm m$ được treo lên cành cây bằng một vòng dây nhỏ gắn trên mặt cầu. Kéo lệch một đoạn nhỏ rồi thả, quả cầu dao động như con lắc vật lý với ma sát không đáng kể. Tính chu kỳ. Gợi ý: Dùng định lý trục song song để tìm mômen quán tính đối với điểm treo.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Vỏ cầu mỏng quay quanh điểm trên bề mặt, tâm khối cách trục $R$.

**Hướng đi:** Mômen quán tính qua tâm của vỏ cầu khác quả cầu đặc. Cộng thêm $MR^2$ để chuyển sang trục treo rồi dùng chu kỳ con lắc vật lý.

**Lời giải:**

Mômen quán tính và chu kỳ là:

$$
\begin{aligned}
I&=\frac23MR^2+MR^2\\
&=\frac53MR^2.
\end{aligned}
$$

$$
T=2\pi\sqrt{\frac{5R}{3g}} \approx0{,}58\,\mathrm s.
$$

Khối lượng triệt tiêu. Kết quả coi vòng dây rất nhỏ, điểm treo ở ngay bề mặt cầu và vỏ cầu đồng chất, mỏng.

</details>

### 14.55 (•): Thay đổi mức tắt dần

Một vật dao động điều hòa tắt dần với hệ số cản có thể thay đổi. Khi hệ số cản bằng không, tần số góc là $\omega$. Tần số góc bằng bao nhiêu, biểu diễn theo $\omega$, khi hệ số cản bằng một nửa giá trị cản tới hạn?

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Tần số góc riêng $\omega=\sqrt{k/m}$, hệ số cản $b=b_c/2$.

**Hướng đi:** Dùng tần số của dao động dưới tới hạn. Hệ số cản làm giảm tần số vì một phần chuyển động bị lực cản làm chậm, đồng thời biên độ giảm theo thời gian.

**Lời giải:**

Với lực cản $F_x=-bv_x$, hệ số cản tới hạn là:

$$
b_c=2\sqrt{km}=2m\omega.
$$

Vì $b=m\omega$, tần số góc dao động là:

$$
\begin{aligned}
\omega_d&=\sqrt{\omega^2-\left(\frac b{2m}\right)^2}\\
&=\frac{\sqrt3}{2}\omega.
\end{aligned}
$$

Hệ vẫn dao động vì $b<b_c$.

</details>

### 14.56 (••): Suy ra hệ số cản từ biên độ

Một quả trứng luộc chín khối lượng $50{,}0\,\mathrm g$ chuyển động ở đầu lò xo có độ cứng $25{,}0\,\mathrm{N/m}$. Li độ ban đầu là $0{,}300\,\mathrm m$. Lực cản $F_x=-bv_x$ làm biên độ giảm còn $0{,}100\,\mathrm m$ sau $5{,}00\,\mathrm s$. Tính độ lớn hệ số cản $b$.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** $m=0{,}0500\,\mathrm{kg}$, biên độ giảm theo tỷ số $1/3$ trong $5{,}00\,\mathrm s$.

**Hướng đi:** Dùng đường bao biên độ của dao động tắt dần, vì lực cản tỷ lệ vận tốc tạo ra sự giảm biên độ theo hàm mũ. Hai biên độ đo được loại bỏ pha dao động.

**Lời giải:**

Đường bao biên độ thỏa:

$$
A(t)=A_0e^{-bt/(2m)}.
$$

Suy ra:

$$
\begin{aligned}
b&=\frac{2m}{t}\ln\frac{A_0}{A(t)}\\
&=0{,}02197\,\mathrm{kg/s}.
\end{aligned}
$$

Vậy $b=0{,}0220\,\mathrm{kg/s}$. Ở đây li độ ban đầu được hiểu là biên độ ban đầu như dữ kiện mô tả sự giảm biên độ. Một li độ đơn lẻ ở pha chưa biết sẽ không đủ xác định tỷ số hai biên độ.

</details>

### 14.57 (•): Dao động dưới tới hạn và cản tới hạn

Một con vật nhỏ khối lượng $0{,}300\,\mathrm{kg}$ chuyển động ở đầu lò xo có độ cứng $k=2{,}50\,\mathrm{N/m}$ và chịu lực cản $F_x=-bv_x$. (a) Nếu $b=0{,}900\,\mathrm{kg/s}$, tần số dao động bằng bao nhiêu? (b) Hệ số $b$ phải bằng bao nhiêu để chuyển động tắt dần tới hạn?

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** $m=0{,}300\,\mathrm{kg}$, $k=2{,}50\,\mathrm{N/m}$, lực cản tỷ lệ vận tốc.

**Hướng đi:** Kiểm tra điều kiện dưới tới hạn rồi dùng tần số có cản. Giá trị tới hạn là ranh giới giữa nghiệm dao động và nghiệm trở về cân bằng không dao động.

**Lời giải:**

(a) Tần số góc và tần số là:

$$
\begin{aligned}
\omega_d&=\sqrt{\frac km-\frac{b^2}{4m^2}}\\
&\approx2{,}47\,\mathrm{rad/s},
\end{aligned}
$$

$$
f_d=\frac{\omega_d}{2\pi} \approx0{,}393\,\mathrm{Hz}.
$$

(b) Ở cản tới hạn:

$$
b_c=2\sqrt{km} \approx1{,}73\,\mathrm{kg/s}.
$$

Giá trị ở phần (a) nhỏ hơn $b_c$, phù hợp với việc hệ còn dao động.

</details>

### 14.58 (••): Đọc năng lượng từ đồ thị tắt dần

Một vật dao động ở đầu lò xo có độ cứng $225\,\mathrm{N/m}$. Hình 14.58 biểu diễn li độ $x$ theo thời gian $t$. (a) Những thời điểm nào vật không chuyển động? (b) Ban đầu hệ có bao nhiêu cơ năng? (c) Từ $t=1{,}0\,\mathrm s$ đến $t=4{,}0\,\mathrm s$, hệ mất bao nhiêu năng lượng? Năng lượng ấy đi đâu?

![Đồ thị li độ dao động tắt dần, các cực trị khoảng 7, âm 6, 5, âm 4 và 3 cm](/vat-ly-1/bai-giang/img/young-14/r-exercises-e14-58.png)

Hình 14.58: Độ dốc đồ thị bằng không tại các vị trí quay đầu.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** $k=225\,\mathrm{N/m}$. Cần đọc thời điểm quay đầu và độ lớn li độ tại các cực trị.

**Hướng đi:** Vận tốc là độ dốc của đồ thị li độ. Ở cực trị, vận tốc bằng không nên cơ năng bằng hoàn toàn thế năng đàn hồi, cho phép tính năng lượng mà không cần biết khối lượng.

**Lời giải:**

(a) Trong khoảng thời gian được vẽ, vật đứng yên tức thời tại khoảng $0$, $1{,}0$, $2{,}0$, $3{,}0$ và $4{,}0\,\mathrm s$. Các mốc đọc từ hình chỉ có độ chính xác của đồ thị.

(b) Ban đầu $x\approx7\,\mathrm{cm}$ và đồ thị bắt đầu ở một vị trí quay đầu. Do đó:

$$
E_0=\frac12k(0{,}070)^2 \approx0{,}55\,\mathrm J.
$$

(c) Tại hai mốc cần xét, $x_1\approx-6\,\mathrm{cm}$ và $x_4\approx3\,\mathrm{cm}$, đều có vận tốc bằng không:

$$
E_1\approx0{,}405\,\mathrm J,
$$

$$
E_4\approx0{,}101\,\mathrm J.
$$

Năng lượng hao hụt là:

$$
E_1-E_4\approx0{,}30\,\mathrm J.
$$

Công âm của lực cản chuyển cơ năng thành nội năng của vật và môi trường, có thể kèm một phần năng lượng âm thanh.

</details>

### 14.59 (•): Biên độ cưỡng bức khi đổi lực cản

Một lực điều hòa tác dụng lên hệ dao động tắt dần có độ cứng $k$ và khối lượng $m$. Khi hệ số cản là $b_1$, biên độ bằng $A_1$ nếu tần số góc của lực cưỡng bức bằng $\sqrt{k/m}$. Giữ nguyên tần số và biên độ lực cưỡng bức $F_{\max}$. Biên độ mới bằng bao nhiêu theo $A_1$ khi hệ số cản là (a) $3b_1$ và (b) $b_1/2$?

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Dao động xác lập có tần số cưỡng bức đúng bằng tần số góc riêng không cản, thay đổi riêng hệ số $b$.

**Hướng đi:** Dùng công thức biên độ cưỡng bức. Tại tần số đã cho, hai số hạng đàn hồi và quán tính triệt tiêu, nên biên độ tỷ lệ nghịch với hệ số cản.

**Lời giải:**

Đặt $\omega_0=\sqrt{k/m}$. Biên độ xác lập là:

$$
A=\frac{F_{\max}}{\sqrt{(k-m\omega_d^2)^2+b^2\omega_d^2}}.
$$

Tại $\omega_d=\omega_0$:

$$
A=\frac{F_{\max}}{b\omega_0}.
$$

Vì vậy (a) $A=A_1/3$ và (b) $A=2A_1$. Kết quả giả sử $b_1>0$ và đã qua giai đoạn quá độ.

</details>

### 14.60 (••): Độ rộng của đường cong cộng hưởng

Xét hệ dao động cưỡng bức tắt dần có biên độ lực $F_{\max}$, khối lượng $m$, độ cứng $k$ và tần số góc riêng $\omega=\sqrt{k/m}$. (a) Với $b=0{,}20\sqrt{km}$, xác nhận biên độ tại $\omega_d=\omega$ bằng $5F_{\max}/k$. (b) Làm lại với $b=0{,}40\sqrt{km}$ và xác nhận biên độ bằng $2{,}5F_{\max}/k$. (c) Để đánh giá độ rộng đỉnh cộng hưởng, tính biên độ tại $\omega_d=\omega/2$ với mỗi hệ số cản. Trong mỗi trường hợp, tìm tỷ số giữa biên độ tại $\omega_d=\omega$ và tại $\omega_d=\omega/2$. Hệ số cản nào cho mức tăng biên độ lớn hơn?

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** So sánh hai mức cản ở tần số riêng và nửa tần số riêng.

**Hướng đi:** Chuẩn hóa công thức biên độ theo $F_{\max}/k$ để nhìn rõ ảnh hưởng riêng của lực cản. Giữ cả độ lệch tần số và lực cản trong mẫu số vì ở nửa tần số riêng, chúng đều góp phần hạn chế biên độ.

**Lời giải:**

Đặt $q=\omega_d/\omega$, $c=b/\sqrt{km}$ và $A_*=F_{\max}/k$. Khi đó:

$$
\frac{A}{A_*}=\frac1{\sqrt{(1-q^2)^2+c^2q^2}}.
$$

(a) Với $q=1$, $c=0{,}20$, ta có $A/A_*=1/c=5$.

(b) Với $q=1$, $c=0{,}40$, ta có $A/A_*=2{,}5$.

(c) Với $q=1/2$, kết quả là:

| Hệ số $c$ | Biên độ $A/A_*$ tại $q=1/2$ | Tỷ số $A(1)/A(1/2)$ |
| --- | --- | --- |
| $0{,}20$ | $1{,}322$ | $3{,}783$ |
| $0{,}40$ | $1{,}288$ | $1{,}941$ |

Hệ có hệ số cản nhỏ hơn cho mức tăng lớn hơn. Đỉnh cộng hưởng của nó hẹp và cao hơn. Với $b>0$, cực đại biên độ thật sự hơi lệch về phía dưới $\omega$ nên các giá trị tại $q=1$ là giá trị ở tần số riêng, không phải vị trí chính xác của đỉnh.

</details>

### 14.61 (••): So sánh hai hệ lò xo

Vật A có khối lượng $m_A$, gắn với lò xo độ cứng $k_A$ và dao động điều hòa. Vật B tương tự có khối lượng $m_B$ và độ cứng $k_B$. Biết $A_A=2A_B$, $m_B=4m_A$ và $k_A=9k_B$. Tìm (a) tỷ số tốc độ cực đại của A so với B và (b) tỷ số độ lớn gia tốc cực đại của A so với B.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Các tỷ số biên độ, khối lượng và độ cứng đều đã biết.

**Hướng đi:** Dùng $v_{\max}=A\omega$ và $a_{\max}=A\omega^2$. Tốc độ phụ thuộc căn bậc hai của $k/m$, còn gia tốc phụ thuộc trực tiếp vào tỷ số này.

**Lời giải:**

Tỷ số tần số góc bằng:

$$
\frac{\omega_A}{\omega_B}=\sqrt{\frac{k_Am_B}{k_Bm_A}}=6.
$$

Do đó:

$$
\frac{v_{\max,A}}{v_{\max,B}}=2\cdot6=12,
$$

$$
\frac{a_{\max,A}}{a_{\max,B}}=2\cdot6^2=72.
$$

</details>

### 14.62 (•••): Thời gian đi tới một li độ âm

Một vật dao động điều hòa với chu kỳ $0{,}300\,\mathrm s$ và biên độ $6{,}00\,\mathrm{cm}$. Tại $t=0$, vật đứng yên tức thời ở $x=6{,}00\,\mathrm{cm}$. Tính thời gian để vật đi từ đó tới $x=-1{,}50\,\mathrm{cm}$.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Bắt đầu ở biên dương, tìm lần đầu tới li độ bằng $-A/4$.

**Hướng đi:** Chọn hàm cos vì vận tốc ban đầu bằng không ở biên dương. Dùng nhánh góc từ $0$ đến $\pi$ để lấy thời điểm đến đầu tiên.

**Lời giải:**

Phương trình li độ là $x=A\cos(2\pi t/T)$, nên:

$$
\begin{aligned}
t&=\frac{T}{2\pi}\arccos\left(-\frac14\right)\\
&\approx0{,}0871\,\mathrm s.
\end{aligned}
$$

Giá trị này nằm giữa $T/4$ và $T/2$, phù hợp với vị trí cần đến ở phía âm trước biên âm.

</details>

### 14.63 (••): Xác định khoảng cách đến cân bằng

Một vật dao động điều hòa có chu kỳ $1{,}200\,\mathrm s$ và biên độ $0{,}600\,\mathrm m$. Tại $t=0$, vật ở $x=0$ và đang chuyển động theo chiều âm. Khi $t=0{,}480\,\mathrm s$, vật cách vị trí cân bằng bao xa?

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Qua cân bằng theo chiều âm lúc bắt đầu, cần khoảng cách sau $0{,}480\,\mathrm s$.

**Hướng đi:** Dùng hàm sin với dấu âm để thỏa cả vị trí lẫn chiều vận tốc ban đầu. Khoảng cách là độ lớn li độ, không giữ dấu tọa độ.

**Lời giải:**

$$
x(t)=-A\sin\frac{2\pi t}{T}.
$$

Thay số cho $x=-0{,}3527\,\mathrm m$. Vậy khoảng cách đến cân bằng là $0{,}353\,\mathrm m$.

</details>

### 14.64 (•): Chu kỳ của ô tô khi bỏ hành khách

Bốn hành khách có tổng khối lượng $250\,\mathrm{kg}$ làm các lò xo của một ô tô có bộ giảm xóc đã mòn bị nén thêm $4{,}00\,\mathrm{cm}$. Mô hình hóa xe và hành khách thành một vật gắn với một lò xo lý tưởng. Nếu chu kỳ dao động khi có hành khách là $1{,}92\,\mathrm s$, chu kỳ của xe không có hành khách bằng bao nhiêu?

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Khối lượng thêm $\Delta m=250\,\mathrm{kg}$ làm cân bằng dịch $\Delta x=0{,}0400\,\mathrm m$, chu kỳ có tải $T_L=1{,}92\,\mathrm s$.

**Hướng đi:** Từ độ nén thêm suy ra độ cứng tương đương. Dùng chu kỳ có tải để suy ra tổng khối lượng đang dao động rồi trừ khối lượng hành khách.

**Lời giải:**

Độ cứng tương đương thỏa:

$$
\begin{aligned}
k&=\frac{\Delta mg}{\Delta x}\\
&=6{,}125\times10^4\,\mathrm{N/m}.
\end{aligned}
$$

Khối lượng có tải và không tải là:

$$
M_L=k\left(\frac{T_L}{2\pi}\right)^2 \approx5719\,\mathrm{kg},
$$

$$
M_0=M_L-250\approx5469\,\mathrm{kg}.
$$

Vậy:

$$
T_0=2\pi\sqrt{\frac{M_0}{k}} \approx1{,}88\,\mathrm s.
$$

Đây là khối lượng suy ra trong mô hình một vật, một lò xo của đề. Không cần thay đổi dữ kiện để ép nó giống một mẫu xe cụ thể.

</details>

### 14.65 (••): Tăng năng lượng nhưng giảm biên độ

Một vật khối lượng $m$ dao động điều hòa với biên độ $A_1$, cơ năng $E_1$ khi lò xo có độ cứng $k_1$. Muốn tăng cơ năng lên $E_2=4E_1$ đồng thời giảm biên độ còn $A_2=A_1/2$, ta thay bằng lò xo độ cứng $k_2$. (a) $k_2$ liên hệ với $k_1$ thế nào? (b) Việc thay đổi ấy ảnh hưởng thế nào đến tốc độ cực đại của vật?

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Giữ khối lượng, tăng cơ năng bốn lần và giảm biên độ hai lần.

**Hướng đi:** Dùng cơ năng $E=kA^2/2$ để xác định lò xo. Sau đó dùng động năng cực đại bằng cơ năng, tránh nhầm biên độ nhỏ đồng nghĩa tốc độ nhỏ.

**Lời giải:**

(a) Tỷ số cơ năng là:

$$
4=\frac{E_2}{E_1} =\frac{k_2}{k_1}\left(\frac12\right)^2.
$$

Suy ra $k_2=16k_1$.

(b) Vì $E=mv_{\max}^2/2$, khối lượng không đổi nên:

$$
\frac{v_{\max,2}}{v_{\max,1}}=\sqrt{\frac{E_2}{E_1}}=2.
$$

Tốc độ cực đại tăng gấp đôi.

</details>

### 14.66 (••, CP): Điều kiện hai khối không trượt

Khối dưới khối lượng $M$ nằm trên mặt phẳng không ma sát và gắn với lò xo nằm ngang có độ cứng $k$, đầu còn lại cố định vào tường. Khối trên khối lượng $m$ đặt lên khối dưới. Hệ số ma sát nghỉ giữa hai khối là $\mu_s$. Tìm biên độ dao động lớn nhất để khối trên không trượt trên khối dưới.

![Khối m nằm trên khối M, khối M nối vào lò xo độ cứng k, hai mặt tiếp xúc có hệ số ma sát nghỉ](/vat-ly-1/bai-giang/img/young-14/r-exercises-p14-66.png)

Hình 14.66: Ma sát nghỉ truyền gia tốc từ khối dưới sang khối trên.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Hai khối phải có cùng gia tốc trong suốt dao động, mặt sàn không ma sát.

**Hướng đi:** Xét cả hai khối để tìm tần số, rồi xét riêng khối trên để tìm ma sát cần thiết. Kiểm tra ở biên vì gia tốc điều hòa có độ lớn lớn nhất tại đó.

**Lời giải:**

Nếu không trượt, khối lượng dao động là $M+m$:

$$
\omega^2=\frac{k}{M+m}.
$$

Khối trên chỉ chịu lực ngang là ma sát nghỉ, do đó:

$$
|f_s|=m|a|\le\mu_smg.
$$

Gia tốc cực đại là $\omega^2A$. Điều kiện không trượt trở thành:

$$
\omega^2A\le\mu_sg.
$$

Vậy biên độ lớn nhất là:

$$
A_{\max}=\frac{\mu_s(M+m)g}{k}.
$$

Khối lượng $m$ triệt tiêu trong điều kiện lực riêng của khối trên, nhưng vẫn xuất hiện trong khối lượng toàn hệ quyết định tần số.

</details>

### 14.67 (••): Đọc độ cứng từ hệ số góc

Một khối khối lượng $m$ dao động điều hòa trên mặt phẳng ngang không ma sát, gắn với lò xo nhẹ có độ cứng $k$. Dùng cảm biến đo tốc độ cực đại với nhiều khối lượng khác nhau nhưng giữ biên độ ở $12{,}0\,\mathrm{cm}$. Đồ thị $v_{\max}^2$ theo $1/m$ gần một đường thẳng có hệ số góc $8{,}62\,\mathrm{N\,m}$. Tìm độ cứng lò xo.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** $A=0{,}120\,\mathrm m$, hệ số góc của đồ thị bình phương tốc độ theo nghịch đảo khối lượng bằng $8{,}62\,\mathrm{N\,m}$.

**Hướng đi:** Bình phương công thức tốc độ cực đại để nhận ra phương trình đường thẳng. Hệ số góc là $kA^2$, không phải riêng $k$.

**Lời giải:**

$$
v_{\max}^2=kA^2\left(\frac1m\right).
$$

Do đó:

$$
k=\frac{8{,}62}{(0{,}120)^2} \approx599\,\mathrm{N/m}.
$$

Đơn vị của hệ số góc là năng lượng, phù hợp với $kA^2$.

</details>

### 14.68 (••, CP): Đo ma sát bằng ngưỡng trượt

Xét hệ hai khối và lò xo ở Hình 14.66. Mặt sàn không ma sát, giữa các khối có ma sát nghỉ. Độ cứng lò xo $150\,\mathrm{N/m}$, khối trên $m=0{,}500\,\mathrm{kg}$ và khối dưới $M=4{,}00\,\mathrm{kg}$. Kéo khối dưới để lò xo giãn đoạn $d$ rồi thả, tăng dần $d$ qua các lần thử. Với $d$ nhỏ, cả hai khối cùng dao động điều hòa. Với $d$ lớn, khối trên trượt ngay khi thả khối dưới. (a) Tìm chu kỳ khi hai khối chưa trượt. (b) Nếu độ giãn lớn nhất chưa gây trượt là $8{,}8\,\mathrm{cm}$, tìm $\mu_s$.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Tổng khối lượng $4{,}50\,\mathrm{kg}$, biên độ giới hạn $d=0{,}088\,\mathrm m$.

**Hướng đi:** Khi chưa trượt, hai khối là một hệ duy nhất. Tại ngưỡng trượt, ma sát cực đại vừa đủ tạo ra gia tốc cực đại, cho phép suy ra hệ số ma sát.

**Lời giải:**

(a) Chu kỳ là:

$$
T=2\pi\sqrt{\frac{M+m}{k}} \approx1{,}09\,\mathrm s.
$$

(b) Khi thả từ biên, gia tốc có độ lớn cực đại. Đặt bằng $\mu_sg$:

$$
\mu_s=\frac{kd}{(M+m)g} \approx0{,}30.
$$

Độ lớn này là hệ số ma sát nghỉ, vì ta xét thời điểm bắt đầu trượt.

</details>

### 14.69 (•••): Khi quả cầu rời khỏi khay

Một khay ngang đồng chất khối lượng $1{,}50\,\mathrm{kg}$ gắn với lò xo lý tưởng thẳng đứng có độ cứng $185\,\mathrm{N/m}$. Lò xo nằm dưới khay, cho phép khay dao động lên xuống. Một quả cầu kim loại khối lượng $275\,\mathrm g$ nằm trong khay. Đẩy khay xuống điểm A, thấp hơn vị trí cân bằng $15{,}0\,\mathrm{cm}$, rồi thả từ nghỉ. (a) Khay đã lên cao bao nhiêu so với A khi quả cầu rời khay? Gợi ý: Sự tách rời không xảy ra khi khay và quả cầu đạt tốc độ cực đại. (b) Từ lúc thả đến khi tách rời mất bao lâu? (c) Tốc độ quả cầu ngay khi tách rời bằng bao nhiêu?

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Trước khi tách rời, khay và cầu có tổng khối lượng $1{,}775\,\mathrm{kg}$, biên độ $A=0{,}150\,\mathrm m$ quanh vị trí cân bằng chung.

**Hướng đi:** Điều kiện rời khay là phản lực bằng không. Khi đó gia tốc quả cầu bằng gia tốc rơi tự do, không phải bằng không. Dùng chuyển động điều hòa của toàn hệ chỉ đến đúng thời điểm mất tiếp xúc.

**Lời giải:**

Chọn $y$ hướng lên, gốc tại cân bằng của khay có cầu. Trước khi tách rời:

$$
\begin{aligned}
\omega&=\sqrt{\frac{185}{1{,}775}}\\
&\approx10{,}209\,\mathrm{rad/s},
\end{aligned}
$$

$$
y(t)=-A\cos(\omega t).
$$

Đối với quả cầu, phương trình lực là:

$$
N-mg=ma_y=-m\omega^2y.
$$

(a) Điều kiện $N=0$ cho vị trí tách rời:

$$
y_* =\frac{g}{\omega^2} \approx0{,}0940\,\mathrm m.
$$

Vì $y_*<A$, sự tách rời xảy ra trước biên trên. Quãng lên cao so với điểm A là:

$$
h=A+y_*=0{,}244\,\mathrm m.
$$

(b) Tại lần đi lên đầu tiên:

$$
\begin{aligned}
t_* &=\frac1\omega\arccos\left(-\frac{y_*}{A}\right)\\
&\approx0{,}220\,\mathrm s.
\end{aligned}
$$

(c) Tốc độ lúc ấy là:

$$
\begin{aligned}
v_* &=\omega\sqrt{A^2-y_*^2}\\
&\approx1{,}19\,\mathrm{m/s}.
\end{aligned}
$$

Quả cầu đang đi lên. Sau khi rời khay, nó chuyển động dưới tác dụng của trọng lực, còn khay có vị trí cân bằng và tần số mới. Vì vậy không kéo dài phương trình chung sang giai đoạn sau.

</details>

### 14.70 (•, CP): Va chạm dính với vật gắn lò xo

Một vật khối lượng $10{,}0\,\mathrm{kg}$ chuyển động sang phải với tốc độ $2{,}00\,\mathrm{m/s}$ trên mặt ngang nhẵn, va vào và dính với vật thứ hai cũng có khối lượng $10{,}0\,\mathrm{kg}$. Vật thứ hai ban đầu đứng yên ở đầu lò xo nhẹ nằm ngang có độ cứng $170{,}0\,\mathrm{N/m}$, đầu còn lại cố định vào tường bên phải. (a) Tìm tần số, biên độ và chu kỳ dao động sau va chạm. (b) Sau bao lâu hệ lần đầu trở lại vị trí ngay sau va chạm?

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Va chạm dính tại vị trí cân bằng ban đầu của lò xo, tổng khối lượng sau va chạm $20{,}0\,\mathrm{kg}$.

**Hướng đi:** Bảo toàn động lượng trong va chạm rất ngắn để tìm vận tốc chung. Sau va chạm, cơ năng của hệ lò xo được bảo toàn và vận tốc chung là tốc độ cực đại vì lò xo đang ở cân bằng.

**Lời giải:**

Vận tốc chung sau va chạm là:

$$
V=\frac{10{,}0(2{,}00)}{20{,}0} =1{,}00\,\mathrm{m/s}.
$$

(a) Tần số góc, tần số và chu kỳ là:

$$
\omega=\sqrt{\frac{170{,}0}{20{,}0}} \approx2{,}915\,\mathrm{rad/s},
$$

$$
f=\frac\omega{2\pi}\approx0{,}464\,\mathrm{Hz},
$$

$$
T=\frac{2\pi}\omega\approx2{,}16\,\mathrm s.
$$

Do $V=\omega A$, biên độ là $A=0{,}343\,\mathrm m$.

(b) Hệ bắt đầu tại cân bằng, đến biên nén rồi trở lại cân bằng sau nửa chu kỳ. Vậy thời gian cần tìm bằng $T/2=1{,}08\,\mathrm s$. Ở lần trở lại này, vận tốc ngược chiều ban đầu.

</details>

### 14.71 (•••): Cùng lò xo, hai kiểu dao động

Một quả táo có trọng lượng $1{,}00\,\mathrm N$ treo ở đầu lò xo dài, khối lượng không đáng kể và độ cứng $1{,}50\,\mathrm{N/m}$. Quả táo có thể dao động điều hòa lên xuống. Nếu dừng chuyển động ấy rồi cho táo đung đưa với góc nhỏ, tần số con lắc đơn bằng một nửa tần số lên xuống. Vì góc nhỏ, chiều dài lò xo không thay đổi đáng kể trong khi đung đưa. Tìm chiều dài tự nhiên của lò xo khi bỏ quả táo.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Tần số ngang bằng nửa tần số dọc, chiều dài con lắc là chiều dài lò xo đã giãn ở cân bằng.

**Hướng đi:** So sánh hai công thức tần số để tìm chiều dài đang treo. Trừ độ giãn do trọng lượng để thu được chiều dài tự nhiên.

**Lời giải:**

Gọi $\ell$ là chiều dài lò xo khi treo táo. Điều kiện tần số cho:

$$
\sqrt{\frac g\ell}=\frac12\sqrt{\frac km}.
$$

Suy ra:

$$
\ell=\frac{4mg}{k} =2{,}667\,\mathrm m.
$$

Độ giãn cân bằng bằng $\Delta\ell=mg/k=0{,}667\,\mathrm m$. Vì vậy:

$$
\begin{aligned}
\ell_0&=\ell-\Delta\ell\\
&=\frac{3mg}{k}=2{,}00\,\mathrm m.
\end{aligned}
$$

</details>

### 14.72 (•••, CP): Dao động của vật nổi

Một vật cao $h$, khối lượng $M$, tiết diện ngang đều $A$ nổi thẳng đứng trong chất lỏng khối lượng riêng $\rho$. (a) Tìm khoảng cách thẳng đứng từ mặt thoáng đến đáy vật ở cân bằng. (b) Tác dụng lực thẳng đứng xuống có độ lớn $F$ lên mặt trên. Ở cân bằng mới, đáy vật hạ thêm bao nhiêu so với phần (a)? Giả sử một phần vật vẫn ở trên mặt thoáng. (c) Bỏ lực đột ngột, vật dao động điều hòa lên xuống. Tính chu kỳ theo $\rho$, $M$ và $A$. Bỏ qua tắt dần do ma sát chất lỏng.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Tiết diện không đổi làm lực đẩy Archimedes biến thiên tuyến tính theo độ sâu, trong miền vật chưa chìm hoàn toàn hoặc rời khỏi chất lỏng.

**Hướng đi:** Dùng lực đẩy bằng trọng lượng chất lỏng bị chiếm chỗ. Phần thay đổi lực đẩy đóng vai trò lực lò xo kéo về, từ đó xác định độ cứng hiệu dụng và chu kỳ.

**Lời giải:**

(a) Gọi $z_0$ là độ sâu đáy vật. Cân bằng đòi hỏi:

$$
\rho gAz_0=Mg,
$$

$$
z_0=\frac{M}{\rho A}.
$$

Cần có $0<z_0<h$ để vật nổi một phần như giả thiết.

(b) Ở cân bằng mới, lực đẩy tăng thêm $F$, do đó:

$$
\Delta z=\frac{F}{\rho gA}.
$$

Điều kiện của phần này là $z_0+\Delta z<h$.

(c) Chọn $y$ là li độ hướng xuống so với cân bằng ban đầu. Sau khi bỏ lực, hợp lực hướng xuống là:

$$
\begin{aligned}
F_y&=Mg-\rho gA(z_0+y)\\
&=-\rho gAy.
\end{aligned}
$$

Vì vậy:

$$
\ddot y=-\frac{\rho gA}{M}y,
$$

$$
T=2\pi\sqrt{\frac{M}{\rho gA}}.
$$

Phương trình chỉ đúng khi đáy còn ngập và đỉnh còn ở trên mặt thoáng suốt dao động. Với thả nghỉ từ độ lệch $\Delta z$, cần thêm $\Delta z<z_0$ để vật không nhô hoàn toàn khỏi chất lỏng ở biên đối diện. Nếu điều kiện ấy hỏng, không thể coi toàn bộ chuyển động là điều hòa theo công thức trên.

</details>

### 14.73 (••, CP): Khung vuông treo tại một đỉnh

Một khung vuông tổng khối lượng $m$ được ghép từ bốn thanh mảnh đồng chất giống nhau, mỗi thanh dài $L$. Khung được treo trên móc ở đỉnh trên như Hình 14.73. Nếu quay khung lệch nhẹ sang trái rồi thả, khung dao động với tần số bao nhiêu?

![Khung vuông gồm bốn thanh mảnh dài L, treo tại một đỉnh với đường chéo thẳng đứng](/vat-ly-1/bai-giang/img/young-14/r-exercises-p14-73.png)

Hình 14.73: Móc treo ở đỉnh trên của khung.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Khối lượng toàn khung là $m$, không phải khối lượng mỗi thanh. Tâm khối ở tâm hình vuông.

**Hướng đi:** Cộng mômen quán tính của bốn thanh đối với tâm khung rồi chuyển sang điểm treo. Công thức con lắc vật lý áp dụng vì góc lệch nhỏ và trọng lực tạo mômen phục hồi.

**Lời giải:**

Khoảng cách từ điểm treo đến tâm khối bằng nửa đường chéo:

$$
d=\frac L{\sqrt2}.
$$

Mỗi thanh có khối lượng $m/4$, tâm cách tâm khung $L/2$. Mômen quán tính của mỗi thanh đối với trục qua tâm khung, vuông góc mặt khung là:

$$
I_1=\frac{mL^2}{48}+\frac{mL^2}{16}.
$$

Bốn thanh có cùng đóng góp nên:

$$
I_{\mathrm{cm}}=4I_1=\frac13mL^2,
$$

$$
I_p=I_{\mathrm{cm}}+md^2 =\frac56mL^2.
$$

Tần số là:

$$
\begin{aligned}
f&=\frac1{2\pi}\sqrt{\frac{mgd}{I_p}}\\
&=\frac1{2\pi}\sqrt{\frac{3\sqrt2g}{5L}}.
\end{aligned}
$$

</details>

### 14.74 (•••): Đồ thị thế năng và pha ban đầu

Một vật khối lượng $0{,}200\,\mathrm{kg}$ chịu lực đàn hồi kéo về có độ cứng $10{,}0\,\mathrm{N/m}$. (a) Vẽ thế năng đàn hồi $U$ theo li độ $x$ trên khoảng từ $-0{,}300\,\mathrm m$ đến $+0{,}300\,\mathrm m$. Dùng tỷ lệ $1\,\mathrm{cm}$ ứng với $0{,}05\,\mathrm J$ theo trục đứng và $1\,\mathrm{cm}$ ứng với $0{,}05\,\mathrm m$ theo trục ngang. Vật được đặt vào dao động với thế năng ban đầu $0{,}140\,\mathrm J$ và động năng ban đầu $0{,}060\,\mathrm J$. Dựa vào đồ thị để trả lời các câu hỏi sau. (b) Biên độ bằng bao nhiêu? (c) Thế năng khi li độ bằng nửa biên độ là bao nhiêu? (d) Ở những li độ nào động năng bằng thế năng? (e) Pha ban đầu $\phi$ bằng bao nhiêu nếu vận tốc ban đầu dương và li độ ban đầu âm?

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** $m=0{,}200\,\mathrm{kg}$, $k=10{,}0\,\mathrm{N/m}$, $U_0=0{,}140\,\mathrm J$, $K_0=0{,}060\,\mathrm J$.

**Hướng đi:** Vẽ parabol thế năng và đường cơ năng không đổi. Giao điểm với đường cơ năng xác định biên độ, còn điều kiện động năng bằng thế năng tương ứng nửa cơ năng. Xét đồng thời dấu li độ và vận tốc để chọn đúng góc pha.

**Lời giải:**

(a) Với $x$ đo bằng mét, phương trình đồ thị là:

$$
U=\frac12kx^2=5{,}00x^2.
$$

![Parabol thế năng từ âm 0,3 đến dương 0,3 mét và đường cơ năng 0,200 jun, các ô hai trục có cùng kích thước hình học. Mỗi ô vuông biểu diễn 0,05 m theo phương ngang và 0,05 J theo phương dọc](/vat-ly-1/bai-giang/img/young-14/solution-14-74-potential.svg)

Hình 14.74: Mỗi ô có cùng cạnh theo hai phương, ứng với $0{,}05\,\mathrm m$ và $0{,}05\,\mathrm J$. Khi ảnh được phóng đúng tỷ lệ, chọn mỗi cạnh ô bằng $1\,\mathrm{cm}$ sẽ cho thang đo đã yêu cầu.

(b) Cơ năng bằng $E=U_0+K_0=0{,}200\,\mathrm J$. Ở biên, $U=E$, do đó:

$$
A=\sqrt{\frac{2E}{k}}=0{,}200\,\mathrm m.
$$

(c) Tại $x=A/2$, thế năng bằng một phần tư cơ năng:

$$
U=\frac E4=0{,}0500\,\mathrm J.
$$

(d) Khi $K=U$, mỗi phần bằng $E/2$, nên:

$$
x=\pm\frac A{\sqrt2} \approx\pm0{,}141\,\mathrm m.
$$

(e) Chọn $x=A\cos(\omega t+\phi)$ với $\omega=\sqrt{k/m}$. Dữ kiện năng lượng và dấu cho:

$$
\begin{aligned}
\cos\phi&=-\sqrt{\frac{U_0}{E}}\\
&=-\sqrt{0{,}700}.
\end{aligned}
$$

Vì $v_0=-A\omega\sin\phi>0$, ta cần $\sin\phi<0$. Pha nằm ở góc phần tư thứ ba nếu chọn khoảng từ $0$ đến $2\pi$:

$$
\phi=3{,}721\,\mathrm{rad}.
$$

Giá trị tương đương là $\phi=-2{,}562\,\mathrm{rad}$, và có thể cộng thêm một bội nguyên của $2\pi$. Chỉ dùng hàm arccos mà bỏ dấu vận tốc sẽ chọn nhầm góc phần tư.

</details>

### 14.75 (•, CALC): Xô nước rò rỉ

Một xô khối lượng $2{,}00\,\mathrm{kg}$ chứa $10{,}0\,\mathrm{kg}$ nước được treo ở lò xo lý tưởng thẳng đứng có độ cứng $450\,\mathrm{N/m}$ và dao động lên xuống với biên độ $3{,}00\,\mathrm{cm}$. Đáy xô đột ngột bị thủng và nước nhỏ ra đều với tốc độ $2{,}00\,\mathrm{g/s}$. Khi nước chỉ còn một nửa, tìm (a) chu kỳ dao động và (b) tốc độ biến thiên chu kỳ theo thời gian. Chu kỳ dài ra hay ngắn đi? (c) Chu kỳ ngắn nhất hệ có thể có là bao nhiêu?

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Xô nặng $2{,}00\,\mathrm{kg}$, nước còn $5{,}00\,\mathrm{kg}$ ở thời điểm cần xét, khối lượng giảm với tốc độ $0{,}00200\,\mathrm{kg/s}$.

**Hướng đi:** Dùng chu kỳ tức thời với khối lượng đang treo, vì lượng nước thay đổi rất chậm trong một dao động. Lấy đạo hàm theo khối lượng rồi nhân với tốc độ giảm khối lượng để xác định dấu của biến thiên chu kỳ.

**Lời giải:**

(a) Khi xô còn nửa nước, tổng khối lượng là $m=7{,}00\,\mathrm{kg}$. Chu kỳ tức thời là:

$$
T=2\pi\sqrt{\frac mk} \approx0{,}784\,\mathrm s.
$$

(b) Từ $T\propto\sqrt m$:

$$
\begin{aligned}
\frac{dT}{dt}&=\frac{T}{2m}\frac{dm}{dt}\\
&\approx-1{,}12\times10^{-4}\,\mathrm{s/s}.
\end{aligned}
$$

Chu kỳ ngắn dần vì khối lượng giảm. Không đưa khối lượng nước đã rơi ra vào khối lượng dao động.

(c) Chu kỳ nhỏ nhất đạt khi chỉ còn xô:

$$
T_{\min}=2\pi\sqrt{\frac{2{,}00}{450}} \approx0{,}419\,\mathrm s.
$$

Nước rò làm vị trí cân bằng dịch dần. Đây là mô tả gần đúng theo chu kỳ tức thời của hệ thay đổi chậm, không phải một chuyển động tuần hoàn chính xác với khối lượng cố định. Thang thời gian mất khối lượng ở thời điểm đang xét khoảng $3500\,\mathrm s$, lớn hơn nhiều chu kỳ, nên xấp xỉ này phù hợp. Biên độ ban đầu không quyết định chu kỳ trong mô hình lò xo tuyến tính.

</details>

### 14.76 (••): Mô hình cổ điển của phân tử HI

Cơ học lượng tử mô tả dao động phân tử, nhưng mô hình cổ điển vẫn cho một số ước lượng hữu ích. Có thể coi các nguyên tử nối với nhau bằng lò xo và dao động quanh tâm khối. Trong phân tử hai nguyên tử HI, iốt nặng hơn hiđrô nhiều nên coi iốt đứng yên, còn hiđrô dao động điều hòa. (a) Với tần số ước lượng $f=7\times10^{13}\,\mathrm{Hz}$ và khối lượng nguyên tử hiđrô gần bằng khối lượng proton, độ cứng tương đương bằng bao nhiêu? (b) Nếu năng lượng dao động khoảng $5\times10^{-20}\,\mathrm J$, tốc độ cực đại của nguyên tử H bằng bao nhiêu? (c) Biên độ dao động bằng bao nhiêu? So sánh với khoảng cách cân bằng giữa hai nguyên tử, khoảng $1{,}6\times10^{-10}\,\mathrm m$.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Coi nguyên tử H là khối lượng dao động, iốt cố định, dao động ở tần số rất cao.

**Hướng đi:** Dùng quan hệ tần số lò xo để suy ra độ cứng. Sau đó đặt cơ năng bằng động năng cực đại và thế năng cực đại để tìm tốc độ và biên độ. Các kết quả chỉ là ước lượng trong mô hình cổ điển đã nêu.

**Lời giải:**

Lấy $m_H\approx1{,}67\times10^{-27}\,\mathrm{kg}$.

(a) Độ cứng tương đương là:

$$
\begin{aligned}
k&=m_H(2\pi f)^2\\
&\approx3{,}2\times10^2\,\mathrm{N/m}.
\end{aligned}
$$

(b) Tốc độ cực đại là:

$$
\begin{aligned}
v_{\max}&=\sqrt{\frac{2E}{m_H}}\\
&\approx7{,}7\times10^3\,\mathrm{m/s}.
\end{aligned}
$$

(c) Biên độ là:

$$
A=\sqrt{\frac{2E}{k}} \approx1{,}8\times10^{-11}\,\mathrm m.
$$

Biên độ bằng khoảng $0{,}11$ lần khoảng cách cân bằng, tức khoảng $11\%$. Khối lượng iốt chỉ được bỏ qua trong chuyển động nhờ sự chênh lệch khối lượng đã giả thiết, không phải vì mọi phân tử hai nguyên tử đều có một nguyên tử đứng yên.

</details>

### 14.77 (••): Chim treo trên lò xo

Một con chim khối lượng $5{,}00\,\mathrm{kg}$ treo vào cành lê bằng lò xo lý tưởng không đáng kể khối lượng. Kéo chim xuống $0{,}100\,\mathrm m$ dưới cân bằng rồi thả, chu kỳ dao động là $4{,}20\,\mathrm s$. (a) Tốc độ qua cân bằng bằng bao nhiêu? (b) Gia tốc khi chim ở trên cân bằng $0{,}050\,\mathrm m$ bằng bao nhiêu? (c) Trong chiều đi lên, mất bao lâu để đi từ điểm dưới cân bằng $0{,}050\,\mathrm m$ đến điểm trên cân bằng $0{,}050\,\mathrm m$? (d) Dừng dao động rồi tháo chim khỏi lò xo. Lò xo ngắn đi bao nhiêu?

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Biên độ $A=0{,}100\,\mathrm m$, chu kỳ $T=4{,}20\,\mathrm s$, khối lượng $5{,}00\,\mathrm{kg}$.

**Hướng đi:** Dùng li độ đo từ vị trí cân bằng đã treo chim. Các quan hệ điều hòa cho tốc độ, gia tốc và pha, còn độ ngắn đi khi tháo vật chính là độ giãn tĩnh $mg/k$.

**Lời giải:**

Tần số góc là $\omega=2\pi/T\approx1{,}496\,\mathrm{rad/s}$.

(a) Tại cân bằng:

$$
v_{\max}=\omega A \approx0{,}150\,\mathrm{m/s}.
$$

(b) Chọn trục hướng lên. Tại $y=0{,}050\,\mathrm m$:

$$
a_y=-\omega^2y \approx-0{,}112\,\mathrm{m/s^2}.
$$

Gia tốc có hướng xuống.

(c) Khi đi lên, có thể đặt $y=-A\cos\psi$ với pha tăng từ $0$ đến $\pi$. Hai điểm cần xét tương ứng $\psi=\pi/3$ và $\psi=2\pi/3$. Hiệu pha bằng $\pi/3$ nên:

$$
\Delta t=\frac{\pi}{3\omega} =\frac T6=0{,}700\,\mathrm s.
$$

(d) Vì $k=m\omega^2$:

$$
\Delta\ell=\frac{mg}{k} =\frac g{\omega^2}\approx4{,}38\,\mathrm m.
$$

Độ co lại lớn là hệ quả của độ cứng rất nhỏ tương ứng chu kỳ đã cho. Độ giãn tĩnh này khác biên độ $0{,}100\,\mathrm m$ quanh cân bằng.

</details>

### 14.78 (••): Đo mômen quán tính của thanh không đồng chất

Một thanh mảnh dài $80{,}0\,\mathrm{cm}$, khối lượng $0{,}400\,\mathrm{kg}$ có trọng tâm tại tâm hình học. Khối lượng riêng không đều và tăng đối xứng từ tâm về hai đầu. Cần tìm mômen quán tính $I_{\mathrm{cm}}$ đối với trục qua tâm, vuông góc thanh, nhưng chưa biết hàm phân bố khối lượng nên không thể tính bằng tích phân. Treo thanh quanh trục cách tâm đoạn $d$ (đo bằng mét), đo chu kỳ góc nhỏ $T$ (đo bằng giây), rồi lặp lại với nhiều giá trị $d$. Đồ thị của hiệu bình phương chu kỳ và số hạng $4\pi^2d/g$ theo $1/d$ gần một đường thẳng có hệ số góc $0{,}320\,\mathrm{m\,s^2}$. Tìm $I_{\mathrm{cm}}$.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Đồ thị có tung độ $T^2-4\pi^2d/g$, hoành độ $1/d$ và hệ số góc $0{,}320\,\mathrm{m\,s^2}$.

**Hướng đi:** Kết hợp định lý trục song song với chu kỳ con lắc vật lý. Phép trừ trong tung độ loại phần mômen quán tính do dịch trục, để hệ số góc chỉ còn phụ thuộc mômen quán tính qua tâm.

**Lời giải:**

Với $m$ là khối lượng thanh:

$$
T^2=\frac{4\pi^2(I_{\mathrm{cm}}+md^2)}{mgd}.
$$

Chuyển vế:

$$
T^2-\frac{4\pi^2d}{g}=\frac{4\pi^2I_{\mathrm{cm}}}{mg}\frac1d.
$$

Vì vậy hệ số góc $s$ thỏa:

$$
s=\frac{4\pi^2I_{\mathrm{cm}}}{mg},
$$

$$
I_{\mathrm{cm}}=\frac{smg}{4\pi^2} \approx0{,}0318\,\mathrm{kg\,m^2}.
$$

Không dùng công thức $mL^2/12$, vì thanh không đồng chất. Kết quả đo lớn hơn giá trị của thanh đồng chất cùng khối lượng và chiều dài, phù hợp với việc khối lượng tập trung hơn về hai đầu.

</details>

### 14.79 (••, CP): Thả thịt lên đĩa cân

Một lò xo không đáng kể khối lượng, độ cứng $400\,\mathrm{N/m}$ treo thẳng đứng, đầu dưới mang đĩa cân khối lượng $0{,}200\,\mathrm{kg}$. Người bán thịt thả miếng thịt $2{,}2\,\mathrm{kg}$ từ độ cao $0{,}40\,\mathrm m$ xuống đĩa. Thịt va chạm hoàn toàn mềm với đĩa và làm hệ dao động điều hòa theo phương thẳng đứng. Tìm (a) tốc độ chung ngay sau va chạm, (b) biên độ dao động sau đó và (c) chu kỳ.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Trước va chạm, đĩa đứng yên ở cân bằng khi chưa có thịt. Sau va chạm, khối lượng tăng thành $2{,}4\,\mathrm{kg}$ và cân bằng dịch xuống.

**Hướng đi:** Tách ba giai đoạn: Rơi tự do, va chạm dính và dao động của hệ mới. Dùng động lượng trong va chạm, rồi dùng cơ năng quanh vị trí cân bằng mới để tính biên độ từ cả li độ lẫn vận tốc ban đầu.

**Lời giải:**

(a) Tốc độ thịt trước va chạm là:

$$
u=\sqrt{2gh}=2{,}80\,\mathrm{m/s}.
$$

Bỏ qua xung lực ngoại lực trong va chạm rất ngắn, vận tốc chung hướng xuống có độ lớn:

$$
V=\frac{2{,}2}{2{,}4}u \approx2{,}57\,\mathrm{m/s}.
$$

(b) Cân bằng mới thấp hơn cân bằng cũ một đoạn:

$$
\delta=\frac{(2{,}2)g}{400} =0{,}0539\,\mathrm m.
$$

Chọn trục dương xuống và gốc ở cân bằng mới, ngay sau va chạm có $y_0=-\delta$ và $v_0=V$. Với $\omega=\sqrt{400/2{,}4}$, biên độ bằng:

$$
A=\sqrt{\delta^2+\frac{V^2}{\omega^2}} \approx0{,}206\,\mathrm m.
$$

(c) Chu kỳ của hệ mới là:

$$
T=2\pi\sqrt{\frac{2{,}4}{400}} \approx0{,}487\,\mathrm s.
$$

Không bảo toàn cơ năng qua va chạm mềm. Cũng không đặt ngay sau va chạm ở cân bằng mới, vì đĩa chưa kịp dịch chuyển trong khoảng va chạm.

</details>

### 14.80 (••): Vị trí, chiều chuyển động và lực lò xo

Lực $40{,}0\,\mathrm N$ làm lò xo thẳng đứng giãn $0{,}250\,\mathrm m$. (a) Phải treo khối lượng bao nhiêu để hệ có chu kỳ $1{,}00\,\mathrm s$? (b) Nếu biên độ là $0{,}050\,\mathrm m$ và chu kỳ như phần (a), vật ở đâu và chuyển động theo chiều nào sau $0{,}35\,\mathrm s$ kể từ lúc qua cân bằng theo chiều xuống? (c) Khi vật ở dưới cân bằng $0{,}030\,\mathrm m$ và đang đi lên, lực lò xo tác dụng lên vật có độ lớn và hướng thế nào?

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Độ cứng được đo bằng lực và độ giãn. Li độ dao động đo từ cân bằng khi đã treo vật.

**Hướng đi:** Suy ra độ cứng và khối lượng từ định luật Hooke và chu kỳ. Với phần (b), chọn pha theo lần qua cân bằng đi xuống. Với phần (c), lực lò xo phụ thuộc độ giãn tổng cộng, còn hợp lực mới tỷ lệ với li độ quanh cân bằng.

**Lời giải:**

(a) Độ cứng và khối lượng cần treo là:

$$
k=\frac{40{,}0}{0{,}250} =160\,\mathrm{N/m},
$$

$$
m=k\left(\frac{T}{2\pi}\right)^2 \approx4{,}05\,\mathrm{kg}.
$$

(b) Chọn $x$ hướng xuống, gốc tại cân bằng và $t=0$ lúc qua cân bằng theo chiều xuống:

$$
x=A\sin(\omega t),
$$

$$
v=A\omega\cos(\omega t).
$$

Với $\omega=2\pi\,\mathrm{rad/s}$ và thời điểm đã cho, ta được $x=0{,}0405\,\mathrm m$ và $v=-0{,}185\,\mathrm{m/s}$. Vật ở dưới cân bằng khoảng $4{,}05\,\mathrm{cm}$ và đang đi lên.

(c) Ở dưới cân bằng $x=0{,}030\,\mathrm m$, lò xo giãn thêm so với độ giãn tĩnh:

$$
F_{\mathrm{lx}}=mg+kx \approx44{,}5\,\mathrm N.
$$

Lực lò xo hướng lên. Tốc độ và chiều chuyển động không làm đổi lực đàn hồi tại cùng một vị trí.

</details>

### 14.81 (••): Khoảng thời gian lên thuyền

Trong chuyến thăm Minnesota, vùng đất được gọi là “xứ sở 10.000 hồ”, bạn định đi tham quan một hồ lớn. Đến bến, bạn thấy chiếc thuyền khối lượng $1500\,\mathrm{kg}$ nhấp nhô điều hòa với biên độ $20\,\mathrm{cm}$ và chu kỳ $3{,}5\,\mathrm s$. Khi thuyền ở vị trí cao nhất, boong ngang bằng cầu tàu đứng yên. Bạn nặng $60\,\mathrm{kg}$, đang hơi choáng, một phần do bữa tối hôm trước có món lutefisk. Bạn chỉ đồng ý lên thuyền khi boong cách mức cầu tàu không quá $10\,\mathrm{cm}$. Trong mỗi chu kỳ, bạn có bao nhiêu thời gian để lên thuyền thuận tiện?

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Biên độ $A=20\,\mathrm{cm}$, cầu tàu ở mức $+A$, khoảng cách được chấp nhận không quá $10\,\mathrm{cm}$.

**Hướng đi:** Chuyển điều kiện chênh lệch độ cao thành điều kiện pha của dao động. Tính tổng độ dài khoảng pha quanh vị trí cao nhất thay vì dùng tốc độ trung bình.

**Lời giải:**

Chọn gốc độ cao tại cân bằng của thuyền và đặt $y=A\cos\psi$. Vì cầu tàu ở $y=A$, điều kiện lên thuyền là:

$$
A-y\le0{,}10\,\mathrm m,
$$

$$
\cos\psi\ge\frac12.
$$

Trong một chu kỳ, tổng khoảng pha thỏa điều kiện bằng $2\pi/3$. Do đó:

$$
\Delta t=\frac{2\pi/3}{2\pi}T =\frac T3\approx1{,}17\,\mathrm s.
$$

Khối lượng của thuyền và người không cần cho cửa sổ thời gian trước khi người bước lên, vì chuyển động của thuyền đã được cho trực tiếp.

</details>

### 14.82 (•, CP): Rơi qua đường hầm xuyên Trái Đất

Xét một ví dụ dao động thú vị nhưng rất khó thực hiện: Thả vật xuống đường hầm xuyên qua tâm Trái Đất đến phía đối diện. Với giả thiết không thực tế rằng Trái Đất là quả cầu có khối lượng riêng đều, chứng minh chuyển động là điều hòa và tìm chu kỳ. Có thể dùng kết quả lực hấp dẫn bên trong quả cầu đồng chất. Chuyển động là điều hòa nếu gia tốc tỷ lệ với li độ và ngược dấu, rồi chu kỳ bằng $2\pi/\omega$.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Mật độ Trái Đất đồng nhất, đường hầm thẳng qua tâm, bỏ lực cản và ảnh hưởng quay của Trái Đất trong mô hình đang xét.

**Hướng đi:** Dùng định lý lớp cầu: Chỉ phần khối lượng nằm trong bán kính hiện tại góp vào hợp lực. Khối lượng ấy tỷ lệ với lập phương bán kính, nên khi chia cho bình phương bán kính trong lực hấp dẫn, lực còn tỷ lệ bậc nhất với li độ.

**Lời giải:**

Gọi $M_E$, $R_E$ là khối lượng và bán kính Trái Đất, $x$ là tọa độ có dấu dọc đường hầm, gốc ở tâm. Khối lượng bên trong bán kính $|x|$ là:

$$
M_r=M_E\frac{|x|^3}{R_E^3}.
$$

Hướng hấp dẫn luôn về tâm, nên:

$$
a_x=-\frac{GM_E}{R_E^3}x =-\frac{g}{R_E}x.
$$

Đây là phương trình điều hòa, với:

$$
\omega=\sqrt{\frac{g}{R_E}},
$$

$$
T=2\pi\sqrt{\frac{R_E}{g}}.
$$

Nếu lấy $R_E\approx6{,}37\times10^6\,\mathrm m$, chu kỳ xấp xỉ $5{,}07\times10^3\,\mathrm s$, tức khoảng $84\,\mathrm{phút}$. Chu kỳ không phụ thuộc khối lượng vật trong mô hình này.

</details>

### 14.83 (•••, CP): Viên đạn găm vào khối gắn lò xo

Một viên đạn khối lượng $8{,}00\,\mathrm g$ bay ngang với vận tốc $280\,\mathrm{m/s}$, đâm vào và nằm lại trong khối khối lượng $0{,}992\,\mathrm{kg}$. Khối nằm trên mặt phẳng không ma sát và gắn ở đầu lò xo lý tưởng, đầu kia cố định vào tường. Va chạm làm lò xo bị nén nhiều nhất $15{,}0\,\mathrm{cm}$. Sau va chạm, khối dao động điều hòa. Tính chu kỳ.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Tổng khối lượng sau va chạm $1{,}000\,\mathrm{kg}$, biên độ sau va chạm $0{,}150\,\mathrm m$.

**Hướng đi:** Bảo toàn động lượng để tìm vận tốc chung ngay sau va chạm. Vì va chạm xảy ra khi lò xo chưa biến dạng, vận tốc ấy là tốc độ cực đại của dao động, cho phép tìm tần số mà chưa cần tính độ cứng.

**Lời giải:**

Vận tốc chung là:

$$
\begin{aligned}
V&=\frac{(0{,}00800)(280)}{1{,}000}\\
&=2{,}24\,\mathrm{m/s}.
\end{aligned}
$$

Từ $V=\omega A$, ta có:

$$
T=\frac{2\pi A}{V} \approx0{,}421\,\mathrm s.
$$

Động năng không được bảo toàn trong lúc viên đạn găm vào khối. Bảo toàn cơ năng chỉ áp dụng cho giai đoạn dao động sau va chạm.

</details>

### 14.84 (•••, CP): Hai quả cầu lăn ở đầu lò xo

Hai quả cầu đặc đồng chất, mỗi quả có khối lượng $M=0{,}800\,\mathrm{kg}$ và bán kính $R=0{,}0800\,\mathrm m$, được nối bằng thanh ngắn nhẹ dọc theo một đường kính của mỗi quả và nằm yên trên mặt bàn ngang. Một đầu lò xo có độ cứng $160\,\mathrm{N/m}$ cố định vào tường. Đầu kia gắn vào vòng không ma sát luồn qua thanh ở tâm khối chung, giữa hai tâm cầu. Kéo hai quả cầu cùng một đoạn ra xa tường để giãn lò xo rồi thả. Ma sát đủ lớn để hai quả cầu lăn không trượt khi chuyển động qua lại. Chứng minh tâm khối chung dao động điều hòa và tính chu kỳ.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Hai quả cầu cùng vận tốc tịnh tiến, đồng thời quay do lăn không trượt. Lò xo tác dụng qua tâm khối chung.

**Hướng đi:** Tính cả động năng tịnh tiến và động năng quay. Ràng buộc lăn liên hệ tốc độ quay với tốc độ tâm, làm tăng quán tính hiệu dụng dù lực kéo về vẫn là lực lò xo tuyến tính.

**Lời giải:**

Mỗi quả có $I=2MR^2/5$, tốc độ quay $\Omega=\dot x/R$. Động năng của một quả gồm phần tịnh tiến và phần quay:

$$
K_1=\frac12M\dot x^2+\frac12I\Omega^2.
$$

Thay mômen quán tính và điều kiện lăn vào, được:

$$
K_1=\frac{7M}{10}\dot x^2.
$$

Hai quả có tổng động năng:

$$
K=2K_1=\frac{7M}{5}\dot x^2.
$$

Đặt $\mu=14M/5$ là quán tính hiệu dụng. Cơ năng bảo toàn vì ma sát nghỉ tại tiếp điểm đứng yên không sinh công:

$$
E=\frac12\mu\dot x^2+\frac12kx^2.
$$

Lấy đạo hàm theo thời gian, hoặc viết phương trình tịnh tiến kết hợp phương trình quay, cho:

$$
\frac{14M}{5}\ddot x=-kx.
$$

Vậy chuyển động là điều hòa với chu kỳ:

$$
T=2\pi\sqrt{\frac{14M}{5k}} \approx0{,}743\,\mathrm s.
$$

Bán kính triệt tiêu vì mômen quán tính tỷ lệ với $R^2$, còn tốc độ góc tỷ lệ nghịch với $R$. Không được chỉ thay tổng khối lượng $2M$ vào công thức lò xo của vật trượt.

</details>

### 14.85 (•, CP): Hai quả cầu dính nhau khi đung đưa

Trong Hình 14.85, thả quả cầu trên từ nghỉ. Nó va vào quả cầu dưới đang đứng yên rồi dính lại. Hai dây đều dài $50{,}0\,\mathrm{cm}$. Quả cầu trên nặng $2{,}00\,\mathrm{kg}$, ban đầu cao hơn quả cầu dưới $10{,}0\,\mathrm{cm}$, còn quả cầu dưới nặng $3{,}00\,\mathrm{kg}$. Tìm tần số và góc lệch cực đại của chuyển động sau va chạm.

![Quả cầu trên treo lệch, cao hơn quả cầu đang ở vị trí thấp nhất 10 cm, hai dây có chung điểm treo](/vat-ly-1/bai-giang/img/young-14/r-exercises-p14-85.png)

Hình 14.85: Quả cầu trên đi xuống đến vị trí thấp nhất trước khi dính vào quả cầu dưới.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Chiều dài con lắc sau va chạm vẫn là $L=0{,}500\,\mathrm m$, tổng khối lượng $5{,}00\,\mathrm{kg}$.

**Hướng đi:** Dùng năng lượng trước va chạm, động lượng theo tiếp tuyến trong va chạm và năng lượng sau va chạm. Công thức tần số con lắc đơn là xấp xỉ góc nhỏ, còn độ cao cực đại có thể tìm chính xác bằng cos của góc.

**Lời giải:**

Tốc độ quả cầu trên ngay trước va chạm là:

$$
u=\sqrt{2g(0{,}100)} =1{,}40\,\mathrm{m/s}.
$$

Vận tốc chung ngay sau va chạm bằng:

$$
V=\frac{2{,}00}{5{,}00}u =0{,}560\,\mathrm{m/s}.
$$

Tần số trong mô hình góc nhỏ là:

$$
f\approx\frac1{2\pi}\sqrt{\frac gL}=0{,}705\,\mathrm{Hz}.
$$

Năng lượng từ đáy lên biên cho:

$$
gL(1-\cos\theta_{\max})=\frac12V^2.
$$

Do đó:

$$
\begin{aligned}
\theta_{\max}&=\arccos\left(1-\frac{V^2}{2gL}\right)\\
&\approx14{,}5^\circ.
\end{aligned}
$$

Tần số thực ở biên độ hữu hạn hơi nhỏ hơn giá trị góc nhỏ. Góc cực đại ở trên đã được tính bằng độ cao chính xác.

</details>

### 14.86 (••): Quả chuông rung mà không phát tiếng

Một quả chuông lớn khối lượng $34{,}0\,\mathrm{kg}$ treo trên xà gỗ, có thể đung đưa với ma sát không đáng kể. Tâm khối chuông nằm dưới trục treo $0{,}60\,\mathrm m$. Mômen quán tính đối với trục ấy là $18{,}0\,\mathrm{kg\,m^2}$. Quả lắc gõ chuông là khối nhỏ $1{,}8\,\mathrm{kg}$ ở đầu thanh mảnh không đáng kể khối lượng, dài $L$. Đầu kia gắn bên trong chuông và quay tự do quanh cùng trục với chuông. Chọn $L$ bằng bao nhiêu để chuông rung yên lặng, nghĩa là chu kỳ của chuông bằng chu kỳ quả lắc gõ?

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Chuông là con lắc vật lý, quả lắc gõ gần như con lắc đơn. Hai chu kỳ góc nhỏ phải bằng nhau.

**Hướng đi:** Viết chu kỳ cho từng bộ phận rồi đồng nhất. Khối lượng của quả lắc gõ triệt tiêu trong chu kỳ con lắc đơn.

**Lời giải:**

Điều kiện bằng chu kỳ là:

$$
2\pi\sqrt{\frac{I}{Mgd}}=2\pi\sqrt{\frac Lg}.
$$

Suy ra:

$$
\begin{aligned}
L&=\frac I{Md}\\
&=\frac{18{,}0}{34{,}0(0{,}60)}\\
&\approx0{,}88\,\mathrm m.
\end{aligned}
$$

Kết quả áp dụng cho dao động góc nhỏ với điều kiện khởi đầu phù hợp để chuông và quả lắc gõ chuyển động cùng pha. Chỉ bằng chu kỳ chưa tự bảo đảm mọi trạng thái khởi đầu đều tránh va chạm.

</details>

### 14.87 (••, CALC): Thanh có trục quay tại trung điểm

Một thanh kim loại mảnh đồng chất khối lượng $M$ quay không ma sát quanh trục qua trung điểm, vuông góc thanh. Lò xo nằm ngang có độ cứng $k$ gắn vào đầu dưới, đầu còn lại gắn vào giá cố định. Kéo thanh lệch góc nhỏ $\Theta$ khỏi phương thẳng đứng như Hình 14.87 rồi thả. Chứng minh thanh dao động điều hòa theo góc và tính chu kỳ. Gợi ý: Dùng xấp xỉ sin của góc bằng góc và cos của góc bằng một. Dao động góc điều hòa có gia tốc góc ngược dấu và tỷ lệ với góc lệch.

![Thanh quay quanh trung điểm, đầu dưới nối với lò xo ngang và góc lệch được đo từ phương thẳng đứng](/vat-ly-1/bai-giang/img/young-14/r-exercises-p14-87.png)

Hình 14.87: Trọng lực đi qua trục quay, còn lò xo tạo mômen phục hồi.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Thanh đồng chất quay quanh tâm khối. Gọi chiều dài thanh là $L$ và coi lò xo không biến dạng ở vị trí cân bằng thẳng đứng.

**Hướng đi:** Tính độ dời ngang của đầu dưới rồi nhân lực lò xo với cánh tay đòn. Vì trục qua tâm khối, trọng lực không tạo mômen, nên chu kỳ chỉ do độ cứng và mômen quán tính quyết định.

**Lời giải:**

Ở góc nhỏ $\theta$, đầu dưới dịch ngang $x\approx L\theta/2$. Lực lò xo có độ lớn $kx$, cánh tay đòn gần bằng $L/2$. Mômen có dấu kéo về:

$$
\tau\approx-k\frac{L^2}{4}\theta.
$$

Với $I=ML^2/12$, phương trình quay là:

$$
\frac{ML^2}{12}\ddot\theta=-\frac{kL^2}{4}\theta,
$$

$$
\ddot\theta=-\frac{3k}{M}\theta.
$$

Vậy:

$$
T=2\pi\sqrt{\frac M{3k}}.
$$

Chiều dài triệt tiêu vì cả mômen quán tính và hệ số mômen phục hồi đều tỷ lệ với bình phương chiều dài. Kết quả là xấp xỉ góc nhỏ, không phải phương trình chính xác ở góc lớn.

</details>

### 14.88 (•••): Hai thanh ghép thành góc vuông

Hai thanh mảnh giống nhau, mỗi thanh khối lượng $m$, dài $L$, ghép vuông góc thành vật hình chữ L. Vật cân bằng trên một cạnh sắc như Hình 14.88. Khi kéo lệch nhẹ rồi thả, vật dao động. Tìm tần số dao động.

![Hai thanh dài L tạo góc vuông mở xuống, đỉnh chung tựa trên cạnh sắc](/vat-ly-1/bai-giang/img/young-14/r-exercises-p14-88.png)

Hình 14.88: Tâm khối nằm dưới đỉnh tựa trên đường phân giác của góc vuông.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Khối lượng toàn vật $2m$, hai thanh cùng quay quanh đầu chung tại cạnh sắc.

**Hướng đi:** Xác định tâm khối bằng trung bình hai tâm thanh. Cộng mômen quán tính quanh đầu chung rồi dùng công thức con lắc vật lý cho góc lệch nhỏ.

**Lời giải:**

Mỗi tâm thanh cách đỉnh $L/2$ và nằm lệch $45^\circ$ so với phương thẳng đứng. Hai thành phần ngang triệt tiêu, nên tâm khối chung cách đỉnh:

$$
d=\frac L2\cos45^\circ =\frac L{2\sqrt2}.
$$

Mômen quán tính quanh đỉnh tựa là:

$$
I=2\left(\frac13mL^2\right) =\frac23mL^2.
$$

Do đó:

$$
\begin{aligned}
f&=\frac1{2\pi}\sqrt{\frac{(2m)gd}{I}}\\
&=\frac1{2\pi}\sqrt{\frac{3g}{2\sqrt2L}}.
\end{aligned}
$$

Vị trí cân bằng ổn định vì tâm khối nằm dưới trục tựa. Công thức giả sử điểm tựa không trượt hay dịch trong dao động nhỏ.

</details>

### 14.89 (••, DATA): Đọc chuyển động từ đồ thị vận tốc

Vật khối lượng $m$ gắn với lò xo độ cứng $75\,\mathrm{N/m}$ và dao động. Hình 14.89 là đồ thị thành phần vận tốc $v_x$ theo thời gian $t$. Tìm (a) chu kỳ, (b) tần số và (c) tần số góc. (d) Biên độ, tính bằng xentimét, bằng bao nhiêu và vật đạt vị trí ấy ở những thời điểm nào? (e) Tìm độ lớn gia tốc cực đại và những thời điểm đạt nó. (f) Khối lượng $m$ bằng bao nhiêu?

![Đồ thị vận tốc có các đỉnh 20 cm mỗi giây, trục thời gian ghi các nhãn 0.2, 0.6, 1.0, 1.4 và 1.6](/vat-ly-1/bai-giang/img/young-14/r-exercises-p14-89.png)

Hình 14.89: Vận tốc biến thiên hình sin. Nhãn thời gian cuối không nhất quán với khoảng chia trước đó, nên cần kiểm tra thang thời gian khi đọc.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Đọc được $v_{\max}=20\,\mathrm{cm/s}$. Lưới thời gian có một nhãn cuối bất nhất, cần nêu rõ cách đọc trước khi tính.

**Hướng đi:** Dùng khoảng cách giữa hai cực đại vận tốc để tìm chu kỳ. Sau đó dùng quan hệ $v_{\max}=\omega A$, $a_{\max}=\omega v_{\max}$ và $k=m\omega^2$. Vật ở biên khi vận tốc bằng không, không phải khi vận tốc đạt cực đại.

**Lời giải:**

Các nhãn $0{,}2$, $0{,}6$, $1{,}0$ và $1{,}4\,\mathrm s$ cách đều nhau trên trục. Mỗi ô nhỏ ứng với $0{,}2\,\mathrm s$. Nhãn cuối in $1{,}6$ nằm tại vị trí tương ứng $1{,}8\,\mathrm s$ theo thang đó. Giữ thang nhất quán của bốn nhãn đầu, hai đỉnh vận tốc cách nhau tám ô nhỏ.

(a) Chu kỳ là $T=1{,}6\,\mathrm s$.

(b) Tần số là:

$$
f=\frac1T=0{,}625\,\mathrm{Hz}.
$$

(c) Tần số góc là:

$$
\omega=\frac{2\pi}{T} \approx3{,}93\,\mathrm{rad/s}.
$$

(d) Biên độ là:

$$
A=\frac{v_{\max}}\omega \approx5{,}09\,\mathrm{cm}.
$$

Đồ thị bắt đầu với vận tốc cực đại dương tại $t=0$, nên chọn $x=A\sin(\omega t)$. Vật đạt biên dương tại $t=T/4+nT$ và biên âm tại $t=3T/4+nT$, với $n$ nguyên không âm. Trong miền thời gian không âm của hình, các mốc là $0{,}4$ và $2{,}0\,\mathrm s$ ở biên dương, $1{,}2\,\mathrm s$ ở biên âm.

(e) Gia tốc cực đại về độ lớn là:

$$
a_{\max}=\omega v_{\max} \approx78{,}5\,\mathrm{cm/s^2}.
$$

Gia tốc đạt độ lớn ấy ở cả hai biên, tại $t=0{,}4+0{,}8n$ giây, với $n$ nguyên không âm. Trong miền đã vẽ có các mốc $0{,}4$, $1{,}2$ và $2{,}0\,\mathrm s$.

(f) Khối lượng là:

$$
m=\frac k{\omega^2} \approx4{,}86\,\mathrm{kg}.
$$

Các giá trị số ở đây dựa trên thang lưới nhất quán vừa nêu. Không thể dùng đồng thời nhãn cuối sai vị trí và những nhãn trước để có một thang thời gian tuyến tính duy nhất.

</details>

### 14.90 (••, DATA): Khối lượng hiệu dụng của lò xo có tiết diện thay đổi

Treo lần lượt các vật khối lượng $m$ ở đầu một lò xo thẳng đứng có khối lượng $0{,}250\,\mathrm{kg}$, tuân theo định luật Hooke và có đường kính thay đổi dọc chiều dài. Vì khối lượng lò xo không thể bỏ qua, trong công thức chu kỳ phải thay $m$ bằng $m+m_{\mathrm{eff}}$, trong đó $m_{\mathrm{eff}}$ là khối lượng hiệu dụng của phần lò xo đang dao động. Có thể đối chiếu cách xây dựng khối lượng hiệu dụng ở Bài 14.93. Thời gian đo cho 10 dao động hoàn chỉnh như sau:

| $m$ ($\mathrm{kg}$) | Thời gian ($\mathrm s$) |
| --- | --- |
| $0{,}100$ | $8{,}7$ |
| $0{,}200$ | $10{,}5$ |
| $0{,}300$ | $12{,}2$ |
| $0{,}400$ | $13{,}9$ |
| $0{,}500$ | $15{,}1$ |

(a) Vẽ bình phương chu kỳ theo khối lượng treo và tìm đường thẳng khớp tốt nhất. (b) Suy ra độ cứng từ hệ số góc. (c) Suy ra khối lượng hiệu dụng từ tung độ gốc. (d) Khối lượng hiệu dụng bằng bao nhiêu phần khối lượng lò xo? (e) Nếu treo vật $0{,}450\,\mathrm{kg}$, tìm chu kỳ, tần số và tần số góc.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Số liệu là thời gian của 10 chu kỳ, không phải một chu kỳ. Lò xo không đồng đều nên khối lượng hiệu dụng phải rút ra từ phép đo.

**Hướng đi:** Bình phương chu kỳ làm phương trình trở thành đường thẳng theo khối lượng. Hệ số góc xác định độ cứng, còn tung độ gốc biểu diễn đóng góp quán tính của chính lò xo.

**Lời giải:**

(a) Chia thời gian đo cho 10 rồi bình phương, được:

| $m$ ($\mathrm{kg}$) | $T^2$ ($\mathrm{s^2}$) |
| --- | --- |
| $0{,}100$ | $0{,}7569$ |
| $0{,}200$ | $1{,}1025$ |
| $0{,}300$ | $1{,}4884$ |
| $0{,}400$ | $1{,}9321$ |
| $0{,}500$ | $2{,}2801$ |

Mô hình là:

$$
T^2=\frac{4\pi^2}{k}(m+m_{\mathrm{eff}}).
$$

Viết đường khớp dạng $T^2=sm+c$. Hồi quy bình phương tối thiểu không trọng số cho:

$$
s=3{,}876\,\mathrm{s^2/kg},
$$

$$
c=0{,}3492\,\mathrm{s^2}.
$$

![Các điểm dữ liệu bình phương chu kỳ theo khối lượng treo cùng đường hồi quy tuyến tính](/vat-ly-1/bai-giang/img/young-14/solution-14-90-regression.svg)

Hình 14.90: Đường thẳng có tung độ gốc dương do quán tính của lò xo.

(b) Độ cứng là:

$$
k=\frac{4\pi^2}{s} \approx10{,}2\,\mathrm{N/m}.
$$

(c) Khối lượng hiệu dụng là:

$$
m_{\mathrm{eff}}=\frac cs \approx0{,}0901\,\mathrm{kg}.
$$

(d) Tỷ phần của khối lượng lò xo bằng:

$$
\frac{m_{\mathrm{eff}}}{0{,}250}\approx0{,}360.
$$

Tức khoảng $36\%$. Không áp đặt giá trị $1/3$ của lò xo đồng đều lên lò xo có tiết diện thay đổi.

(e) Với khối lượng treo $0{,}450\,\mathrm{kg}$, dùng chính đường khớp cho:

$$
T=\sqrt{s(0{,}450)+c} \approx1{,}45\,\mathrm s,
$$

$$
f=\frac1T\approx0{,}691\,\mathrm{Hz},
$$

$$
\omega=\frac{2\pi}{T} \approx4{,}34\,\mathrm{rad/s}.
$$

</details>

### 14.91 (•••, DATA): Nhận ra giới hạn của xấp xỉ góc nhỏ

Treo một quả cầu kim loại nhỏ bằng dây nhẹ từ trần nhà. Kéo quả cầu sang trái $2{,}00\,\mathrm m$, gần chạm một bức tường thẳng đứng, giữ dây căng rồi thả từ nghỉ. Quả cầu đung đưa như con lắc đơn. Đo chu kỳ $T$, lặp lại với nhiều chiều dài dây $L$, lần nào cũng kéo ngang $2{,}00\,\mathrm m$ so với vị trí dây thẳng đứng. Bán kính quả cầu rất nhỏ so với $L$. Thu được số liệu:

| $L$ ($\mathrm m$) | $T$ ($\mathrm s$) |
| --- | --- |
| $12{,}00$ | $6{,}96$ |
| $10{,}00$ | $6{,}36$ |
| $8{,}00$ | $5{,}70$ |
| $6{,}00$ | $4{,}95$ |
| $5{,}00$ | $4{,}54$ |
| $4{,}00$ | $4{,}08$ |
| $3{,}00$ | $3{,}60$ |
| $2{,}50$ | $3{,}35$ |
| $2{,}30$ | $3{,}27$ |

(a) Với năm chiều dài lớn nhất, vẽ $T^2$ theo $L$. Giải thích vì sao các điểm gần thẳng hàng. Hệ số góc có như dự đoán không? (b) Thêm các số liệu còn lại vào đồ thị. Giải thích vì sao chúng lệch khỏi đường khớp khi $L$ giảm. Để thấy rõ hơn, vẽ tỷ số $T/T_0$ theo $L$, với $T_0$ là chu kỳ góc nhỏ và $g=9{,}80\,\mathrm{m/s^2}$. (c) Dùng đồ thị tỷ số để ước lượng biên độ góc, tính bằng độ, tại đó công thức chu kỳ góc nhỏ sai khoảng $5\%$.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Độ dời ngang ban đầu giữ cố định $2{,}00\,\mathrm m$, nên giảm chiều dài làm tăng biên độ góc.

**Hướng đi:** So sánh dữ liệu với quan hệ tuyến tính của con lắc góc nhỏ. Sau đó dùng hình học để nối sự tăng tỷ số chu kỳ với biên độ góc hữu hạn, thay vì quy mọi độ lệch cho sai số đo.

**Lời giải:**

(a) Trong xấp xỉ góc nhỏ:

$$
T_0^2=\frac{4\pi^2}{g}L.
$$

Vì vậy hệ số góc dự đoán là $4{,}0284\,\mathrm{s^2/m}$. Hồi quy năm điểm có chiều dài lớn nhất cho đường $T^2=sL+c$, với:

$$
s=3{,}9795\,\mathrm{s^2/m},
$$

$$
c=0{,}6674\,\mathrm{s^2}.
$$

![Năm điểm ứng với chiều dài lớn nhất nằm gần đường thẳng theo chiều dài](/vat-ly-1/bai-giang/img/young-14/solution-14-91-five.svg)

Hình 14.91a: Năm chiều dài lớn cho gần quan hệ tuyến tính của chu kỳ góc nhỏ. Hệ số góc gần giá trị dự đoán, nhưng tung độ gốc không cần bằng không trong phép khớp thực nghiệm này.

(b) Hình học ban đầu cho:

$$
\sin\theta_0=\frac{2{,}00\,\mathrm m}{L}.
$$

Khi $L$ giảm, góc thả tăng. Lực tiếp tuyến tỷ lệ với sin của góc, không còn tỷ lệ với góc, nên chu kỳ tăng so với dự đoán tuyến tính.

![Toàn bộ chín điểm cùng đường khớp của năm điểm đầu, các chiều dài nhỏ lệch lên trên](/vat-ly-1/bai-giang/img/young-14/solution-14-91-all.svg)

Hình 14.91b: Các điểm ở chiều dài nhỏ nằm cao hơn đường khớp từ năm điểm đầu.

Tỷ số tính từ dữ liệu là:

| $L$ ($\mathrm m$) | $T/T_0$ |
| --- | --- |
| $12$ | $1{,}0010$ |
| $10$ | $1{,}0021$ |
| $8$ | $1{,}0041$ |
| $6$ | $1{,}0068$ |
| $5$ | $1{,}0116$ |
| $4$ | $1{,}0164$ |
| $3$ | $1{,}0356$ |
| $2{,}5$ | $1{,}0556$ |
| $2{,}3$ | $1{,}0743$ |

![Tỷ số chu kỳ đo được trên chu kỳ góc nhỏ tăng khi chiều dài giảm, đường ngang đánh dấu 1,05](/vat-ly-1/bai-giang/img/young-14/solution-14-91-ratio.svg)

Hình 14.91c: Đường ngang $1{,}05$ cắt đường đi qua các điểm ở giữa $L=2{,}5\,\mathrm m$ và $L=3{,}0\,\mathrm m$.

(c) Đọc gần đúng tỷ số $T/T_0=1{,}05$ cho $L\approx2{,}6\,\mathrm m$. Nội suy tuyến tính giữa hai điểm kề cho $L\approx2{,}64\,\mathrm m$, dẫn đến:

$$
\theta_0\approx\arcsin\frac{2{,}00}{2{,}64}\approx49^\circ.
$$

Vì đề yêu cầu ước lượng trên đồ thị, có thể kết luận biên độ khoảng $50^\circ$. Nếu định nghĩa sai số $5\%$ theo chu kỳ thật thay vì theo $T_0$, tỷ số mục tiêu là $1/0{,}95$ và kết quả vẫn xấp xỉ $50^\circ$ ở độ chính xác của đồ thị.

</details>

### 14.92 (•••, Thử thách): Độ cứng tương đương của hai lò xo

Hai lò xo có cùng chiều dài tự nhiên nhưng độ cứng khác nhau $k_1$ và $k_2$ nối với khối khối lượng $m$ trên mặt phẳng ngang không ma sát. Tính độ cứng tương đương $k_{\mathrm{eff}}$ cho ba cấu hình (a), (b), (c) trong Hình 14.92. Độ cứng tương đương được định nghĩa qua hợp lực kéo về:

$$
F_x=-k_{\mathrm{eff}}x.
$$

(d) Một vật khối lượng $m$ treo ở lò xo đồng đều độ cứng $k$ dao động với tần số $f_1$. Cắt lò xo làm hai phần bằng nhau rồi treo cùng vật vào một nửa, tần số trở thành $f_2$. Tìm tỷ số $f_1/f_2$.

![Ba cấu hình gồm hai lò xo song song cùng phía, hai lò xo ở hai phía vật và hai lò xo mắc nối tiếp](/vat-ly-1/bai-giang/img/young-14/r-exercises-p14-92.png)

Hình 14.92: Ba cách ghép hai lò xo, giữ đầy đủ các phần (a), (b), (c).

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** So sánh độ biến dạng và lực của từng lò xo khi khối dịch khỏi cân bằng. Ở phần (d), lò xo đồng đều bị giảm một nửa chiều dài.

**Hướng đi:** Dùng định luật Hooke cho từng lò xo, rồi cộng lực hoặc cộng độ giãn theo cấu hình. Lò xo ngắn hơn gồm ít đoạn đàn hồi nối tiếp hơn nên có độ cứng lớn hơn.

**Lời giải:**

(a) Hai lò xo cùng phía đều biến dạng bằng $x$ và kéo về cùng chiều:

$$
F_x=-(k_1+k_2)x.
$$

Do đó $k_{\mathrm{eff}}=k_1+k_2$.

(b) Khi khối dịch sang phải, lò xo trái giãn còn lò xo phải nén. Cả hai lực biến thiên đều hướng trái, nên vẫn có:

$$
k_{\mathrm{eff}}=k_1+k_2.
$$

Kết quả là độ cứng quanh cân bằng, kể cả khi hai lò xo có lực căng trước.

(c) Với hai lò xo nối tiếp, gọi $F$ là độ lớn lực đàn hồi và $x_1$, $x_2$ là các độ giãn. Điểm nối không khối lượng đòi hỏi lực hai bên bằng nhau:

$$
x=x_1+x_2 =\frac F{k_1}+\frac F{k_2}.
$$

Suy ra:

$$
k_{\mathrm{eff}}=\frac{k_1k_2}{k_1+k_2}.
$$

(d) Hai nửa lò xo giống nhau ghép nối tiếp khôi phục lò xo ban đầu. Nếu độ cứng mỗi nửa là $k_h$, thì $k=k_h/2$, tức $k_h=2k$. Vì tần số tỷ lệ với căn độ cứng:

$$
\frac{f_1}{f_2}=\sqrt{\frac{k}{2k}} =\frac1{\sqrt2}\approx0{,}707.
$$

</details>

### 14.93 (•••, CALC, Thử thách): Lò xo có khối lượng

Xét lò xo khối lượng $M$, chiều dài cân bằng $L_0$, độ cứng $k$. Khi chiều dài là $L$, thế năng đàn hồi bằng $kx^2/2$ với $x=L-L_0$. (a) Một đầu cố định, đầu kia chuyển động với tốc độ $v$. Giả sử tốc độ các điểm trên lò xo tăng tuyến tính theo khoảng cách $l$ từ đầu cố định và khối lượng phân bố đều dọc chiều dài. Tính động năng theo $M$ và $v$. Gợi ý: Chia thành các đoạn $dl$, tìm tốc độ và khối lượng từng đoạn rồi tích phân từ $0$ đến $L$. Kết quả không bằng $Mv^2/2$ vì các đoạn không có cùng tốc độ. (b) Lấy đạo hàm theo thời gian của phương trình bảo toàn cơ năng đối với vật khối lượng $m$ gắn vào lò xo không khối lượng. So sánh với phương trình điều hòa để chứng minh tần số góc bằng $\sqrt{k/m}$. (c) Áp dụng cách ở (b) cho lò xo ở (a), tìm tần số góc. Nếu định nghĩa khối lượng hiệu dụng $M'$ qua $\omega=\sqrt{k/M'}$, biểu diễn $M'$ theo $M$.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Lò xo có phân bố vận tốc tuyến tính dọc chiều dài và phân bố khối lượng đều. Phần (c) xét chính lò xo chuyển động, không tự thêm một vật ở đầu tự do.

**Hướng đi:** Tích phân động năng từng phần để thay lò xo bằng một quán tính hiệu dụng. Sau đó lấy đạo hàm cơ năng để đọc hệ số giữa gia tốc và li độ. Phải giữ các giả thiết phân bố vì chúng quyết định hệ số hiệu dụng.

**Lời giải:**

(a) Ở tọa độ $l$, tốc độ và khối lượng của đoạn nhỏ là:

$$
u(l)=\frac lL v,
$$

$$
dm=\frac ML\,dl.
$$

Động năng cả lò xo là:

$$
\begin{aligned}
K&=\int_0^L\frac12u(l)^2\,dm\\
&=\frac{Mv^2}{2L^3}\int_0^L l^2\,dl\\
&=\frac16Mv^2.
\end{aligned}
$$

(b) Với vật khối lượng $m$ và lò xo không khối lượng:

$$
E=\frac12m\dot x^2+\frac12kx^2.
$$

Lấy đạo hàm và dùng $dE/dt=0$:

$$
\dot x(m\ddot x+kx)=0.
$$

Ở các thời điểm $\dot x\ne0$, ta có $m\ddot x=-kx$. Tại các điểm quay đầu, phương trình vẫn đúng theo tính liên tục của lực và gia tốc. Do đó:

$$
\ddot x=-\frac kmx,
$$

$$
\omega=\sqrt{\frac km}.
$$

(c) Thay động năng bởi kết quả phần (a), với $v=\dot x$:

$$
E=\frac M6\dot x^2+\frac12kx^2.
$$

Lấy đạo hàm như trên cho:

$$
\frac M3\ddot x=-kx.
$$

Vì vậy:

$$
\omega=\sqrt{\frac{3k}{M}},
$$

$$
M'=\frac M3.
$$

Đây là kết quả trong mô hình vận tốc tuyến tính đã giả thiết, không phải phổ dao động chính xác của mọi lò xo liên tục. Nếu gắn thêm vật khối lượng $m$ ở đầu, quán tính hiệu dụng sẽ là $m+M/3$ trong cùng xấp xỉ, nhưng đó là một hệ bổ sung khác.

</details>

## Đọc hiểu khoa học: Quan sát bề mặt ở thang nanomét (MCAT, BIO)

Một phương pháp tạo ảnh bề mặt ở thang nanomét, kể cả màng và phân tử sinh học, là kính hiển vi lực nguyên tử động. Một đầu dò nhỏ gắn vào công xôn, tức một phiến chữ nhật mềm được đỡ ở một đầu như ván nhảy. Công xôn rung làm đầu dò đi lên xuống gần như điều hòa. Trong một chế độ làm việc, công xôn có độ cứng $k=1000\,\mathrm{N/m}$ và tần số cộng hưởng $100\,\mathrm{kHz}$.

Khi đầu dò đến cách bề mặt mẫu vài nanomét, nó chịu lực hút từ bề mặt. Với biên độ rất nhỏ, thường là $0{,}050\,\mathrm{nm}$, lực $F$ do bề mặt tác dụng biến thiên tuyến tính theo độ dời $x$ của đầu dò theo cách viết:

$$
|F|=k_{\mathrm{surf}}x.
$$

Ở đây $k_{\mathrm{surf}}$ là độ cứng hiệu dụng của tương tác bề mặt. Tình huống mô tả hợp lực qua biểu thức $(k+k_{\mathrm{surf}})x$, làm tần số thay đổi nhẹ khi đầu dò tương tác với mẫu. Đo sự thay đổi tần số khi quét đầu dò qua các vùng khác nhau cung cấp thông tin về bề mặt.

![Công xôn và đầu dò nhỏ nằm rất gần bề mặt mẫu](/vat-ly-1/bai-giang/img/young-14/r-exercises-mcat14-94-96.png)

Hình 14.94: Đầu dò gần bề mặt mẫu.

### 14.94 (MCAT): Khối lượng của mô hình dao động

Nếu mô hình hóa hệ đang rung bằng vật gắn lò xo, cần khối lượng bao nhiêu để đạt tần số cộng hưởng đã cho khi đầu dò chưa tương tác với bề mặt? Chọn (a) $25\,\mathrm{ng}$, (b) $100\,\mathrm{ng}$, (c) $2{,}5\,\mathrm{\mu g}$ hoặc (d) $100\,\mathrm{\mu g}$.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** $k=1000\,\mathrm{N/m}$, $f=100\,\mathrm{kHz}$, chưa có tương tác bề mặt.

**Hướng đi:** Đồng nhất tần số cộng hưởng với tần số riêng của mô hình lò xo lý tưởng. Đổi kilôhéc sang héc trước khi bình phương, rồi đổi kilôgam sang microgam để đối chiếu lựa chọn.

**Lời giải:**

Ta có $f=1{,}00\times10^5\,\mathrm{Hz}$ và:

$$
\begin{aligned}
m&=\frac{k}{(2\pi f)^2}\\
&\approx2{,}53\times10^{-9}\,\mathrm{kg}.
\end{aligned}
$$

Vì $1\,\mathrm{\mu g}=10^{-9}\,\mathrm{kg}$, khối lượng gần $2{,}5\,\mathrm{\mu g}$. Chọn (c). Đây là khối lượng hiệu dụng của mô hình rung, không bắt buộc bằng khối lượng hình học toàn công xôn.

</details>

### 14.95 (MCAT): Năng lượng dao động của đầu dò

Trong mô hình của Bài 14.94, tổng cơ năng dao động khi đầu dò chưa tương tác với bề mặt bằng bao nhiêu? Chọn (a) $1{,}2\times10^{-18}\,\mathrm J$, (b) $1{,}2\times10^{-16}\,\mathrm J$, (c) $1{,}2\times10^{-9}\,\mathrm J$ hoặc (d) $5{,}0\times10^{-8}\,\mathrm J$.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Độ cứng $1000\,\mathrm{N/m}$, biên độ $0{,}050\,\mathrm{nm}$ từ tình huống chung.

**Hướng đi:** Cơ năng dao động điều hòa bằng thế năng đàn hồi ở biên. Cần đổi nanomét sang mét rồi mới bình phương vì năng lượng tỷ lệ với bình phương biên độ.

**Lời giải:**

Biên độ là $A=5{,}0\times10^{-11}\,\mathrm m$. Do đó:

$$
\begin{aligned}
E&=\frac12kA^2\\
&=1{,}25\times10^{-18}\,\mathrm J.
\end{aligned}
$$

Giá trị tương ứng với lựa chọn (a), $1{,}2\times10^{-18}\,\mathrm J$, ở độ chính xác của các phương án.

</details>

### 14.96 (MCAT): Độ thay đổi tần số do bề mặt

Tần số dao động thay đổi bao nhiêu phần trăm nếu $k_{\mathrm{surf}}=5\,\mathrm{N/m}$? Chọn (a) $0{,}1\%$, (b) $0{,}2\%$, (c) $0{,}5\%$ hoặc (d) $1{,}0\%$.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Tình huống dùng độ cứng hiệu dụng $k+k_{\mathrm{surf}}$, với $k=1000\,\mathrm{N/m}$ và phần thêm $5\,\mathrm{N/m}$.

**Hướng đi:** Tần số tỷ lệ với căn bậc hai độ cứng khi khối lượng không đổi. Vì vậy phần trăm thay đổi tần số gần bằng một nửa phần trăm thay đổi độ cứng khi nhiễu nhỏ.

**Lời giải:**

Theo độ cứng tổng đã nêu:

$$
\begin{aligned}
\frac{f'}f&=\sqrt{\frac{k+k_{\mathrm{surf}}}{k}}\\
&=\sqrt{1{,}005}.
\end{aligned}
$$

Độ tăng phần trăm là:

$$
100\left(\frac{f'}f-1\right)\approx0{,}2497\%.
$$

Phương án gần nhất là (b), $0{,}2\%$. Giá trị chính xác của mô hình không trùng hẳn một lựa chọn, nên không ép nó thành đúng $0{,}2\%$.

Biểu thức hợp lực trong tình huống chưa thể hiện dấu kéo về. Nếu $x$ là li độ có dấu từ cân bằng và độ cứng tổng là $k+k_{\mathrm{surf}}$, phương trình có hướng phải là:

$$
F_{\mathrm{net}}=-(k+k_{\mathrm{surf}})x.
$$

Lực hút tự nó chưa xác định dấu thay đổi độ cứng, vì dấu ấy phụ thuộc độ dốc lực quanh cân bằng. Nếu chọn một mô hình tương tác làm mềm lò xo với độ cứng tổng $k-k_{\mathrm{surf}}$, tần số sẽ giảm khoảng $0{,}2503\%$. Đó là quy ước tương tác khác với độ cứng tổng đã ghi trong tình huống, nên không dùng để thay đổi dữ kiện của bài này.

</details>
