## 10.3 Vật rắn quay quanh trục chuyển động

Một gậy tung lên không chỉ quay quanh một trục cố định trong phòng. Khối tâm của nó chuyển động trong khi gậy quay. Để phân tích, ta tách chuyển động thành tịnh tiến của khối tâm và quay quanh một trục đi qua khối tâm.

![Hình 10.11: Chuyển động của gậy được tách thành quỹ đạo khối tâm và sự quay quanh khối tâm.](../img/young-10/a-hinh-10-11.png)

Sự tách này vẫn dùng được khi khối tâm có gia tốc. Điều đó không có nghĩa hệ quy chiếu gắn với khối tâm luôn là quán tính. Ta đang biểu diễn vận tốc và năng lượng của các phần tử trong một hệ quán tính ban đầu.

### Động năng của chuyển động kết hợp

Gọi $\vec u=\vec v_{\mathrm{cm}}$ là vận tốc khối tâm và $\vec w_i$ là vận tốc phần tử $i$ tương đối với khối tâm. Vì vậy, độ lớn $u=v_{\mathrm{cm}}$. Vận tốc trong hệ quán tính là:

$$
\vec v_i=\vec u+\vec w_i. \tag{10.9}
$$

![Hình 10.12: Vận tốc của một phần tử bằng tổng vận tốc khối tâm và vận tốc quay tương đối với khối tâm.](../img/young-10/a-hinh-10-12.png)

Để khai triển động năng mà không bỏ sót số hạng chéo, đặt:

$$
\begin{aligned}
T_i&=\tfrac12m_iu^2,\\
C_i&=m_i\vec u\cdot\vec w_i,\\
R_i&=\tfrac12m_iw_i^2.
\end{aligned}
$$

Bình phương tổng vận tốc theo tích vô hướng cho:

$$
K_i=T_i+C_i+R_i.
$$

Với hai phần tử, tổng khối lượng $M=m_1+m_2$, động lượng tương đối $\vec P'=m_1\vec w_1+m_2\vec w_2$ và động năng tương đối $K'=R_1+R_2$. Với $N$ phần tử, ba tổng được viết gọn:

$$
\begin{aligned}
M&=\sum_{i=1}^{N}m_i,\\
\vec P'&=\sum_{i=1}^{N}m_i\vec w_i,\\
K'&=\sum_{i=1}^{N}R_i.
\end{aligned}
$$

Khai triển đầy đủ theo chỉ số từ 1 đến N:

$$
M=m_1+m_2+\dots+m_N.
$$

Đặt $\vec p_i'=m_i\vec w_i$, tức động lượng phần tử i trong hệ chuyển động cùng khối tâm. Khi ấy:

$$
\vec P'=\vec p_1'+\vec p_2'+\dots+\vec p_N'.
$$

$$
K'=R_1+R_2+\dots+R_N.
$$

Cộng ba đóng góp năng lượng của mọi phần tử:

$$
K=\tfrac12Mu^2+\vec u\cdot\vec P'+K'. \tag{10.10}
$$

Theo định nghĩa khối tâm, tổng động lượng tương đối so với chính khối tâm bằng không, tức $\vec P'=0$. Nếu phần chuyển động tương đối là quay của vật rắn quanh trục qua khối tâm, $K'=I_{\mathrm{cm}}\omega^2/2$. Do đó:

$$
K=\tfrac12Mv_{\mathrm{cm}}^2+\tfrac12I_{\mathrm{cm}}\omega^2. \tag{10.8}
$$

Số hạng thứ nhất là động năng tịnh tiến của toàn khối lượng, còn số hạng thứ hai là động năng quay quanh khối tâm. Không thay $I_{\mathrm{cm}}$ bằng mômen quán tính của một trục khác trong công thức này.

### Lăn không trượt

Xét bánh tròn bán kính $R$ lăn trên mặt phẳng đứng yên. Nếu không trượt, điểm tiếp xúc có vận tốc tức thời bằng không đối với mặt phẳng. Vận tốc quay tương đối của điểm ấy phải triệt tiêu vận tốc khối tâm, nên về độ lớn:

$$
v_{\mathrm{cm}}=R\omega. \tag{10.11}
$$

![Hình 10.13: Cộng chuyển động tịnh tiến và quay cho vận tốc bằng không tại tiếp điểm, bằng hai lần vận tốc tâm tại điểm cao nhất.](../img/young-10/a-hinh-10-13.png)

Điểm cao nhất có vận tốc cùng chiều và gấp đôi vận tốc khối tâm. Hai điểm ở hai bên có vận tốc tạo góc $45^\circ$ với phương ngang. Những kết quả này là tổng vectơ vận tốc, không phải mọi điểm trên vành đều có cùng vận tốc dài trong hệ mặt đất.

Có thể xem bánh quay tức thời quanh trục đi qua tiếp điểm. Định lý trục song song cho:

$$
I_P=I_{\mathrm{cm}}+MR^2.
$$

Khi dùng $v_{\mathrm{cm}}=R\omega$, động năng $I_P\omega^2/2$ cho cùng kết quả với tổng tịnh tiến và quay. Tuy nhiên, tiếp điểm tức thời thay đổi liên tục. Một phần tử có vận tốc bằng không ở một thời điểm không nhất thiết có gia tốc bằng không.

Quan hệ không trượt không áp dụng khi bánh quay trơn hoặc bị khóa phanh. Bánh xe tăng tốc trơn có thể có $R\omega>v_{\mathrm{cm}}$, còn bánh bị khóa và trượt có thể có $R\omega<v_{\mathrm{cm}}$.

![Hình 10.14: Khói lốp cho thấy bánh đang trượt tương đối với đường, nên không thể dùng điều kiện lăn không trượt.](../img/young-10/a-hinh-10-14.png)

Trong trọng trường đều, thế năng của toàn vật vẫn tính theo độ cao khối tâm:

$$
U=Mgy_{\mathrm{cm}}.
$$

### Ứng dụng ở hạt có cánh

Hạt phong có phần hạt nặng gắn với cánh nhẹ. Dòng khí quanh cánh vừa làm hạt quay vừa làm chậm chuyển động rơi, xuống cỡ $1\,\mathrm{m/s}$ trong tình huống minh họa. Khi không có gió, khối tâm rơi gần thẳng đứng nhưng hạt vẫn quay. Gió có thể đưa hạt đi xa cây mẹ.

![Ứng dụng: Hạt phong vừa rơi vừa quay quanh khối tâm nhờ tương tác với không khí.](../img/young-10/a-hat-phong.png)

::: example Ví dụ 10.4: Tốc độ của yo-yo đơn giản

Dây nhẹ quấn quanh một trụ đặc đồng chất khối lượng $M$, bán kính $R$. Giữ cố định đầu dây và thả trụ từ nghỉ. Dây tháo ra nhưng không dãn và không trượt. Tìm tốc độ khối tâm sau khi trụ hạ xuống một đoạn $h$.

![Hình 10.15: Thế năng giảm chuyển thành cả động năng tịnh tiến và động năng quay của yo-yo.](../img/young-10/a-hinh-10-15.png)

**Tóm tắt đề bài:** $I_{\mathrm{cm}}=MR^2/2$, đầu dây đứng yên và trụ bắt đầu từ nghỉ.

**Hướng đi:** Dùng bảo toàn cơ năng vì đầu dây cố định không cung cấp công và liên kết không trượt không làm mất cơ năng. Liên hệ $\omega=v/R$ để viết động năng bằng một ẩn tốc độ $v$.

**Lời giải:**

$$
\begin{aligned}
K&=\tfrac12Mv^2+\tfrac14Mv^2\\
&=\tfrac34Mv^2.
\end{aligned}
$$

Bảo toàn cơ năng cho $Mgh=3Mv^2/4$. Vì vậy:

$$
v=\sqrt{\frac43gh}.
$$

Hai phần ba động năng là tịnh tiến, một phần ba là quay. Tốc độ nhỏ hơn $\sqrt{2gh}$ của rơi tự do vì một phần thế năng được chuyển sang quay. Dây định hướng sự phân chia này mà không cung cấp thêm năng lượng cho hệ.
:::

::: example Ví dụ 10.5: Cuộc đua của các vật lăn

Thả các vật tròn từ nghỉ trên cùng một mặt phẳng nghiêng có độ chênh cao $h$. Chúng lăn không trượt. So sánh vật nào đến chân dốc trước, bỏ qua cản lăn và sức cản không khí.

![Hình 10.16: Các vật có cùng độ hạ thấp khối tâm nhưng mômen quán tính theo khối lượng và bán kính khác nhau.](../img/young-10/a-hinh-10-16.png)

**Tóm tắt đề bài:** Viết mômen quán tính dưới dạng $I_{\mathrm{cm}}=cMR^2$, trong đó $c$ phụ thuộc hình dạng và phân bố khối lượng.

**Hướng đi:** Dùng cơ năng và điều kiện không trượt. So sánh $c$ sau khi khử $M,R$ để thấy yếu tố nào quyết định tốc độ.

**Lời giải:**

$$
Mgh=\tfrac12(1+c)Mv^2.
$$

Suy ra:

$$
v=\sqrt{\frac{2gh}{1+c}}.
$$

Với cùng $c$, tốc độ không phụ thuộc khối lượng hay bán kính. Các vật đồng chất có thứ tự đến trước đến sau là cầu đặc ($c=2/5$), trụ đặc ($c=1/2$), vỏ cầu mỏng ($c=2/3$), rồi trụ rỗng thành mỏng ($c=1$).

$c$ nhỏ hơn nghĩa là ít năng lượng gắn với chuyển động quay hơn tại cùng tốc độ khối tâm. Vì vậy, vật có thể tăng tốc tịnh tiến nhanh hơn trên cùng dốc.
:::

### Phương trình lực và mômen quanh khối tâm

Chuyển động khối tâm tuân theo định luật II Newton:

$$
\sum\vec F_{\mathrm{ext}}=M\vec a_{\mathrm{cm}}. \tag{10.12}
$$

Đối với vật rắn quay quanh một trục qua khối tâm là trục đối xứng và giữ nguyên phương, có thể viết:

$$
\sum\tau_{z,\mathrm{ext}}=I_{\mathrm{cm}}\alpha_z. \tag{10.13}
$$

Hai điều kiện về trục làm cho mômen động lượng cùng phương với vận tốc góc và không phát sinh sự thay đổi phương trục. Trục có thể chuyển động tịnh tiến. Trường hợp trục thay đổi phương cần dùng quan hệ vectơ tổng quát của mục 10.5.

![Hình 10.17: Trục bánh xe qua khối tâm và là trục đối xứng. Trong tình huống xét, phương trục không đổi.](../img/young-10/a-hinh-10-17.png)

Khi giải, dùng tổng ngoại lực để tìm gia tốc khối tâm và tổng mômen quanh khối tâm để tìm gia tốc góc. Chọn chiều dương sao cho quan hệ liên kết có dấu đúng, rồi giải đồng thời.

::: example Ví dụ 10.6: Gia tốc của yo-yo

Với yo-yo ở Ví dụ 10.4, tìm gia tốc đi xuống của trụ và lực căng dây.

![Hình 10.18: Trọng lực làm khối tâm gia tốc xuống, còn lực căng tạo mômen làm trụ quay.](../img/young-10/a-hinh-10-18.png)

**Tóm tắt đề bài:** Trụ đặc có $I_{\mathrm{cm}}=MR^2/2$. Trọng lượng $Mg$ hướng xuống, lực căng $T$ hướng lên.

**Hướng đi:** Viết phương trình lực cho toàn trụ và mômen đối với khối tâm. Dùng dây không trượt để có $a=R\alpha_z$.

**Lời giải:**

$$
Mg-T=Ma. \tag{10.14}
$$

Phương trình mômen quanh khối tâm:

$$
TR=\tfrac12MR^2\alpha_z. \tag{10.15}
$$

Điều kiện dây không trượt:

$$
a=R\alpha_z. \tag{10.16}
$$

Từ phương trình mômen, $T=Ma/2$. Thay vào phương trình lực:

$$
\begin{aligned}
a&=\frac23g,\\
T&=\frac13Mg.
\end{aligned}
$$

Lực căng làm gia tốc nhỏ hơn rơi tự do nhưng không giữ trụ đứng yên. Đừng đặt $T=Mg$, vì như vậy phương trình lực sẽ cho gia tốc bằng không.
:::

::: example Ví dụ 10.7: Quả cầu lăn trên dốc

Một quả cầu bowling đặc, đồng chất, khối lượng $M$, bán kính $R$, lăn không trượt trên dốc góc $\beta$. Tìm gia tốc khối tâm và lực ma sát.

![Hình 10.19: Ma sát nghỉ hướng lên dốc tạo mômen quay, trong khi thành phần trọng lực dọc dốc kéo khối tâm xuống.](../img/young-10/a-hinh-10-19.png)

**Tóm tắt đề bài:** $I_{\mathrm{cm}}=2MR^2/5$. Chọn chiều xuống dốc là chiều tịnh tiến dương và chiều lăn xuống là chiều góc dương.

**Hướng đi:** Trọng lực và phản lực pháp tuyến không có mômen quanh khối tâm. Ma sát nghỉ tạo mômen cần cho chuyển động quay. Vì tiếp điểm không trượt, liên hệ $a=R\alpha_z$ nối hai phương trình.

**Lời giải:** Gọi $f$ là độ lớn ma sát hướng lên dốc:

$$
Mg\sin\beta-f=Ma. \tag{10.17}
$$

Phương trình mômen và liên kết không trượt:

$$
fR=I_{\mathrm{cm}}\alpha_z. \tag{10.18}
$$

$$
a=R\alpha_z.
$$

Phương trình quay cho $f=2Ma/5$. Kết hợp phương trình tịnh tiến:

$$
\begin{aligned}
a&=\frac57g\sin\beta,\\
f&=\frac27Mg\sin\beta.
\end{aligned}
$$

Gia tốc bằng $5/7$ gia tốc trượt không ma sát trên cùng dốc. Từ $v^2=2as$ với $h=s\sin\beta$, ta thu được $v^2=10gh/7$, thống nhất với Ví dụ 10.5.

Nếu quả cầu đang lăn lên dốc mà vẫn không trượt, ma sát trong mô hình này vẫn hướng lên dốc. Khi ấy vận tốc khối tâm hướng lên còn gia tốc hướng xuống. Phải phân biệt chiều chuyển động với chiều gia tốc trước khi đoán chiều ma sát.
:::

### Ma sát nghỉ và cản lăn

Ở lăn không trượt trên mặt phẳng đứng yên, ma sát nghỉ có thể khác không nhưng điểm đặt tức thời không chuyển dời. Vì vậy, công suất của ma sát nghỉ đối với toàn vật bằng không trong mô hình vật và mặt phẳng cứng tuyệt đối. Không có mâu thuẫn với việc ma sát tạo mômen và đổi động năng quay.

Vật và mặt phẳng thực tế có thể biến dạng. Hợp lực pháp tuyến khi ấy không nhất thiết đi qua khối tâm, nên tạo mômen cản quay. Biến dạng và trượt vi mô làm cơ năng chuyển thành nội năng. Hiện tượng này gọi là cản lăn.

![Hình 10.20: Mặt phẳng biến dạng làm đường tác dụng của phản lực lệch khỏi khối tâm và tạo mômen cản lăn.](../img/young-10/a-hinh-10-20.png)

Một cây cỏ lăn sau khi khô và tách khỏi gốc có thể được gió đẩy đi bằng chuyển động lăn. Hình dạng phân nhánh giúp nó phát tán hạt trên mặt đất. Tuy nhiên, cây dễ biến dạng nên chịu cản lăn đáng kể. Khi gió ngừng cung cấp năng lượng, nó giảm tốc và dừng lại.

![Ứng dụng: Cây cỏ lăn được gió đưa đi, kết hợp chuyển động tịnh tiến và quay để phát tán hạt.](../img/young-10/a-co-lan.png)

### Câu tự kiểm 10.3

Thay trụ đặc của yo-yo ở Ví dụ 10.6 bằng trụ rỗng thành mỏng có cùng khối lượng và bán kính. Gia tốc đi xuống và lực căng dây tăng, giảm hay giữ nguyên?

<details><summary>Xem giải thích</summary>

Trụ rỗng có mômen quán tính lớn hơn, $I=MR^2$. Giải lại hai phương trình lực và mômen cho $a=g/2$ và $T=Mg/2$. So với trụ đặc, gia tốc giảm từ $2g/3$ xuống $g/2$, còn lực căng tăng từ $Mg/3$ lên $Mg/2$.

</details>
