## Bài toán thử thách

::: exercise 29.67
Một vỏ cầu dẫn bán kính $10{,}0\,\mathrm{cm}$ quay quanh trục thẳng đứng với tần số 2 vòng mỗi giây trong từ trường đều $1{,}00\,\mathrm T$ hướng xuống. Hai thanh dẫn cố định tiếp xúc trượt với vỏ cầu. Một thanh đi từ đỉnh cầu, thanh kia hợp phương thẳng đứng góc $60{,}0^\circ$. Hai đầu ngoài nối nhau qua điện trở $10{,}0\,\Omega$.

![Hình P29.67: Vỏ cầu quay giữa hai tiếp điểm cố định, một ở đỉnh và một ở góc 60 độ.](img/young-29/hinh-p29-67.png)

(a) Chọn gốc ở tâm, $z$ hướng lên, $y$ sang phải để hai thanh nằm trong $yz$. Tìm vận tốc điểm trên vỏ ở mặt phẳng ấy, tại góc $\theta$ đo từ $+z$.

(b) Tìm $\vec v\times\vec B$.

(c) Tìm phần tử đường dọc cung ngắn nhất từ thanh trên đến thanh nghiêng.

(d) Tìm độ lớn dòng trong dây nối.

(e) Dòng trong thanh thẳng đứng hướng lên hay xuống?
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** $r=0{,}100\,\mathrm m$, $\omega=2\pi f=4\pi\,\mathrm{rad/s}$. Chiều quay ở hình ứng với vector tốc độ góc $+z$, còn trường hướng $-z$.

**Hướng đi:**

- Dùng vận tốc quay $\vec v=\vec\omega\times\vec r$ để giữ đúng hướng trên vỏ.
- Tích phân lực từ trên một đơn vị điện tích dọc cung cầu, vì tốc độ và phương tiếp tuyến thay đổi theo $\theta$.
- Dùng dấu suất điện động từ đỉnh đến thanh nghiêng để tìm cực tính và chiều dòng ngoài vỏ.

(a) Vector vị trí điểm là

$$
\vec r=r\sin\theta\hat{\jmath}
+r\cos\theta\hat{k}.
$$

Suy ra

$$
\begin{aligned}
\vec v &= -\omega r\sin\theta\hat{\imath} \\
&= -(1{,}257\,\mathrm{m/s})\sin\theta\hat{\imath}.
\end{aligned}
$$

(b)

$$
\vec v\times\vec B
=-\omega rB\sin\theta\hat{\jmath}.
$$

(c) Lấy đạo hàm vị trí theo $\theta$:

$$
d\vec\ell=r(\cos\theta\hat{\jmath}
-\sin\theta\hat{k})\,d\theta.
$$

(d) Đặt $\theta_0=\pi/3$. Suất điện động theo chiều từ đỉnh đến tiếp điểm nghiêng là

$$
\begin{aligned}
\mathcal E &= \int_0^{\theta_0} (\vec v\times\vec B)\cdot d\vec\ell \\
&= -\omega Br^2\int_0^{\theta_0} \sin\theta\cos\theta\,d\theta \\
&= -\frac12\omega Br^2\sin^260^\circ \\
&= -0{,}0471\,\mathrm V.
\end{aligned}
$$

Bỏ qua điện trở vỏ, thanh và tiếp điểm so với điện trở đã cho,

$$
I=\frac{|\mathcal E|}{10{,}0\,\Omega}
=4{,}71\,\mathrm{mA}.
$$

(e) Tiếp điểm đỉnh có điện thế cao hơn tiếp điểm nghiêng. Dòng mạch ngoài đi từ đỉnh đến điện trở rồi xuống thanh nghiêng. Trong thanh thẳng đứng, dòng hướng lên, từ vỏ cầu ra mạch ngoài.
:::

::: exercise 29.68
Một điện trường đều hướng dọc trục vùng hình trụ, chứa vòng dây chữ nhật điện trở tổng $R$. Vòng có cạnh ngang theo bán kính dài $a$, cạnh dọc trục dài $b$, một cạnh áp sát trục như hình. Trường bằng không tại $t=0$ rồi tăng theo

$$
\vec E=\eta t^2\hat{k},
$$

với $\eta$ có đơn vị $\mathrm{V/(m\,s^2)}$.

![Hình P29.68: Vòng chữ nhật nằm trong mặt phẳng chứa trục hình trụ có điện trường hướng lên.](img/young-29/hinh-p29-68.png)

(a) Tìm độ lớn dòng dịch qua đường tròn đồng tâm bán kính $r\le a$.

(b) Dùng Ampere tìm từ trường ở khoảng cách $r\le a$.

(c) Tìm từ thông qua vòng chữ nhật.

(d) Tìm độ lớn dòng trong vòng.

(e) Nhìn như hình, dòng theo chiều kim đồng hồ hay ngược chiều?
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Điện trường tăng theo $t^2$, gây dòng dịch tăng theo $t$, từ đó tạo từ trường biến thiên. Vòng chữ nhật được giữ cố định.

**Hướng đi:**

- Dùng dòng dịch $\varepsilon_0d\Phi_E/dt$ cho diện tích tròn.
- Dùng đối xứng trụ trong Ampere–Maxwell để tìm trường tiếp tuyến.
- Tích phân từ trường không đều theo bán kính trên mặt chữ nhật, rồi dùng Faraday và Ohm.

(a) Trong chân không,

$$
\begin{aligned}
i_D &= \varepsilon_0\pi r^2\frac{dE}{dt} \\
&= 2\pi\varepsilon_0\eta tr^2.
\end{aligned}
$$

(b) Vì không có dòng dẫn xuyên mặt tròn,

$$
\begin{aligned}
2\pi rB &= \mu_0i_D, \\
B(r,t) &= \mu_0\varepsilon_0\eta tr.
\end{aligned}
$$

(c) Trường vuông góc mặt vòng chữ nhật và tăng tuyến tính với bán kính. Độ lớn từ thông là

$$
\begin{aligned}
|\Phi_B| &= b\int_0^aB(r,t)\,dr \\
&= \frac12\mu_0\varepsilon_0\eta tba^2.
\end{aligned}
$$

(d)

$$
\begin{aligned}
|\mathcal E| &= \frac12\mu_0\varepsilon_0\eta ba^2, \\
I &= \frac{\mu_0\varepsilon_0\eta ba^2}{2R}.
\end{aligned}
$$

Dòng có độ lớn không đổi với $t>0$ trong mô hình này, dù điện trường ban đầu tăng theo bình phương thời gian.

(e) Dòng dịch hướng lên, tạo từ trường vào mặt vòng khi nhìn như hình. Trường ấy tăng, nên dòng cảm ứng tạo trường ra mặt hình. Dòng ngược kim đồng hồ, qua điện trở trên từ phải sang trái.
:::

::: exercise 29.69
Thanh kim loại dài $L$, khối lượng $m$, điện trở $R$ trượt không ma sát trên hai ray nghiêng góc $\phi$ so với phương ngang. Bỏ qua điện trở ray. Trường đều $B$ hướng thẳng đứng xuống như hình. Thanh được thả từ nghỉ.

![Hình P29.69: Thanh ab nằm ngang qua hai ray nghiêng, chuyển động xuống dốc trong trường thẳng đứng xuống.](img/young-29/hinh-p29-69.png)

(a) Dòng trong thanh đi từ $a$ đến $b$ hay ngược lại?

(b) Tìm tốc độ giới hạn.

(c) Tìm dòng tại tốc độ giới hạn.

(d) Tìm công suất điện chuyển thành nhiệt khi đã đạt tốc độ giới hạn.

(e) Tìm công suất trọng lực lúc ấy và so sánh với (d).
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Thành phần trường vuông góc mặt ray bằng $B\cos\phi$. Thanh chạy xuống dốc với tốc độ $v$.

**Hướng đi:**

- Dùng thành phần trường vuông góc mặt mạch để tính suất điện động.
- Lực từ $IBL$ nằm ngang. Chiếu lực lên phương dốc để so sánh với $mg\sin\phi$.
- Tại tốc độ giới hạn, dùng cân bằng lực và định luật Ohm. Kiểm tra công suất bằng hai cách.

(a) Lực từ lên điện tích dương do $\vec v\times\vec B$ hướng từ $a$ đến $b$, nên dòng trong thanh theo chiều ấy.

(b) Suất điện động và dòng có độ lớn

$$
\begin{aligned}
|\mathcal E| &= BLv\cos\phi, \\
I &= \frac{BLv\cos\phi}{R}.
\end{aligned}
$$

Thành phần lực từ chống chuyển động xuống dốc là $IBL\cos\phi$. Cân bằng tại tốc độ giới hạn cho

$$
\begin{aligned}
mg\sin\phi &= IBL\cos\phi, \\
v_{\mathrm{gh}} &= \frac{Rmg\sin\phi}{B^2L^2\cos^2\phi}.
\end{aligned}
$$

(c)

$$
I_{\mathrm{gh}}=\frac{mg\tan\phi}{BL}.
$$

(d)

$$
\begin{aligned}
P_{\mathrm{th}} &= I_{\mathrm{gh}}^2R \\
&= \frac{Rm^2g^2\tan^2\phi}{B^2L^2}.
\end{aligned}
$$

(e) Trọng lực làm công với công suất

$$
\begin{aligned}
P_g &= mgv_{\mathrm{gh}}\sin\phi \\
&= \frac{Rm^2g^2\tan^2\phi}{B^2L^2}.
\end{aligned}
$$

Hai công suất bằng nhau vì động năng không đổi ở tốc độ giới hạn. Các biểu thức cần $\cos\phi\ne0$ và thanh còn nằm trong mạch có cấu hình đã giả thiết.
:::

::: exercise 29.70
Một vòng dây vuông cạnh $L$, tổng khối lượng $m$, điện trở tổng $R$ ban đầu nằm ngang trong mặt phẳng $xy$. Các đỉnh là $(0,0,0)$, $(0,L,0)$, $(L,0,0)$, $(L,L,0)$. Từ trường đều hướng lên $\vec B=B\hat{k}$. Giữ cạnh từ $(0,0,0)$ đến $(L,0,0)$ cố định trên trục $x$, để phần còn lại tự quay xuống do trọng lực.

(a) Tìm độ lớn và hướng mômen tổng khi vòng đã quay xuống góc $\phi$ và đang quay với tốc độ góc $\omega$.

(b) Tìm gia tốc góc lúc ấy.

(c) So với trường hợp không có từ trường, thời gian quay xuống $90^\circ$ dài hơn hay ngắn hơn? Giải thích.

(d) Cơ năng có bảo toàn trong quá trình quay không? Giải thích.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Dây phân bố khối lượng đều. Chiều quay xuống có vector tốc độ góc theo $-x$. Chọn $\phi$ tăng theo chiều quay xuống và $\omega=\dot\phi>0$.

**Hướng đi:**

- Trọng tâm cách trục $L/2$, nên dùng cánh tay đòn ngang $(L/2)\cos\phi$ cho trọng lực.
- Từ thông $BL^2\cos\phi$ biến đổi khi quay, gây dòng và mômen từ cản quay.
- Tính mômen quán tính từ bốn cạnh thay vì xem toàn khối lượng ở trọng tâm.
- Dùng công suất nhiệt để đánh giá bảo toàn cơ năng.

(a) Mômen trọng lực hướng theo $-x$, có độ lớn $mgL\cos\phi/2$. Suất điện động và dòng cảm ứng có độ lớn

$$
\begin{aligned}
|\mathcal E| &= BL^2\omega\sin\phi, \\
I &= \frac{BL^2\omega\sin\phi}{R}.
\end{aligned}
$$

Mômen từ hướng theo $+x$, chống quay xuống, có độ lớn

$$
\tau_B = IL^2B\sin\phi = \frac{B^2L^4\omega\sin^2\phi}{R}.
$$

Đặt mômen đại số theo chiều quay xuống là

$$
\tau_\phi=\frac{mgL}{2}\cos\phi -\frac{B^2L^4\omega}{R}\sin^2\phi.
$$

Vector tổng bằng $-\tau_\phi\hat{\imath}$, độ lớn $|\tau_\phi|$. Nếu $\tau_\phi<0$, mômen tổng quay ngược chiều chuyển động hiện thời.

(b) Cạnh trên trục không góp mômen quán tính. Cạnh đối diện cách trục $L$ có khối lượng $m/4$. Hai cạnh còn lại mỗi cạnh là thanh dài $L$ quay quanh đầu:

$$
\begin{aligned}
J_x &= 0+\frac m4L^2 +2 \left(\frac13\frac m4L^2\right) \\
&= \frac5{12}mL^2.
\end{aligned}
$$

Do đó

$$
\begin{aligned}
\ddot\phi &= \frac{\tau_\phi}{J_x} \\
&= \frac{6g}{5L}\cos\phi -\frac{12B^2L^2}{5mR}\omega\sin^2\phi.
\end{aligned}
$$

(c) Thời gian dài hơn. Mômen từ cản chuyển động, làm năng lượng cơ bị tiêu tán và tốc độ tại cùng góc nhỏ hơn trường hợp không có trường.

(d) Cơ năng không bảo toàn. Năng lượng mất đi chuyển thành nhiệt:

$$
\frac{dE_{\mathrm{mech}}}{dt}=-I^2R.
$$

Nếu kể cả nhiệt trong mạch, tổng năng lượng vẫn bảo toàn.
:::

## Các bài đọc hiểu theo dạng MCAT

### Kích thích não bằng cảm ứng điện từ

Sự truyền tin trong hệ thần kinh dựa trên các tín hiệu điện gọi là điện thế hoạt động, lan dọc sợi trục, tức phần kéo dài của tế bào thần kinh. Tín hiệu phát sinh khi hiệu điện thế qua màng thay đổi, cụ thể là phía trong tế bào trở nên dương hơn.

Trước khi có cách kích thích từ xuyên sọ, các nhà nghiên cứu y học lâm sàng và thần kinh sinh học chưa thể kích thích thần kinh tại vị trí xác định trên người đang tỉnh mà vẫn tránh xâm lấn. Dùng điện cực trên da gây đau và đòi hỏi dòng lớn, có thể nguy hiểm.

Anthony Barker cùng cộng sự tại Đại học Sheffield ở Anh đã phát triển kỹ thuật kích thích từ xuyên sọ, gọi tắt là TMS. Một cuộn gần hộp sọ tạo từ trường biến thiên, cảm ứng dòng trong mô não dẫn điện. Dòng ấy đủ để gây điện thế hoạt động ở tế bào thần kinh.

Chẳng hạn, đặt cuộn gần vỏ não vận động, vùng điều khiển vận động chủ ý, cho phép quan sát co cơ để đánh giá mối liên hệ giữa não và cơ. Hình (a) biểu diễn cuộn và dòng trong mô. Hình (b) biểu diễn dạng xung từ trường theo thời gian.

![Bài đọc TMS: Cuộn kích thích phía trên não và xung từ trường tăng nhanh rồi giảm dần.](img/young-29/mcat29-tms.png)

::: exercise 29.71
Trong phần (a), dòng trong cuộn tăng đến cực đại rồi giảm về không theo chiều đã vẽ. Dòng cảm ứng trên đường nét đứt trong mô não có chiều nào?

(a) Chiều 1.

(b) Chiều 2.

(c) Chiều 1 khi dòng cuộn tăng, chiều 2 khi dòng cuộn giảm.

(d) Chiều 2 khi dòng cuộn tăng, chiều 1 khi dòng cuộn giảm.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Dòng nguồn giữ cùng chiều nhưng độ lớn trải qua hai giai đoạn tăng và giảm. Hai mũi tên 1,2 chỉ hai chiều tuần hoàn trái nhau trong mô.

**Hướng đi:**

- Dòng cảm ứng chống biến thiên từ thông, nên phải đảo chiều khi dòng nguồn đi qua cực đại.
- Đối chiếu chiều dòng cuộn với hai mũi tên trong hình bằng quy tắc bàn tay phải.

Khi dòng cuộn tăng, trường cảm ứng phải ngược trường cuộn. Mũi tên 1 tạo chiều trường yêu cầu. Khi dòng cuộn giảm, trường cảm ứng phải cùng chiều trường cuộn để duy trì từ thông, tương ứng mũi tên 2. Chọn (c).
:::

::: exercise 29.72
Xem mô não ở độ cao đường nét đứt như các vòng tròn đồng tâm độc lập. Suất điện động cảm ứng lớn nhất ở đâu?

(a) Tại tâm đường nét đứt.

(b) Tại phần ngoài cùng của đường nét đứt.

(c) Bằng nhau trên mọi vòng đồng tâm.

(d) Ở tâm khi dòng kích thích tăng, ở ngoài cùng khi dòng kích thích giảm.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Mô hình dùng các vòng đồng tâm trong vùng trường gần đều. So sánh suất điện động quanh các vòng bán kính khác nhau.

**Hướng đi:**

- Dùng Faraday với diện tích vòng tròn. Suất điện động quanh vòng phụ thuộc diện tích, không chỉ độ lớn trường tại một điểm.
- Xét độ lớn để thấy tăng hay giảm dòng nguồn chỉ đổi dấu, không đổi vòng nào có suất điện động lớn nhất.

$$
|\mathcal E(r)|=\pi r^2\left|\frac{dB}{dt}\right|.
$$

Vòng ngoài có diện tích lớn nhất nên suất điện động lớn nhất. Chọn (b). Khi dòng nguồn đổi từ tăng sang giảm, chiều cảm ứng đảo nhưng thứ tự theo bán kính không đổi trong mô hình này.
:::

::: exercise 29.73
Muốn tăng dòng cảm ứng cực đại trong mô, nên dùng dạng từ trường theo thời gian A hay B trong hình, nếu các điều kiện khác giữ nguyên?

![Hình P29.73: Hai dạng xung A và B có độ cao cực đại và độ dốc sườn tăng khác nhau.](img/young-29/hinh-p29-73.png)

(a) A.

(b) B.

(c) A hoặc B đều như nhau.

(d) Cả A và B đều không tăng được.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Trường cực đại của B lớn hơn, nhưng cần so độ dốc cực đại để xác định suất điện động.

**Hướng đi:**

- Dùng $I=|\mathcal E|/R$ với các điều kiện khác không đổi.
- Faraday cho suất điện động tỉ lệ $|dB/dt|$, tức độ dốc đồ thị, không phải độ cao đỉnh.

Sườn tăng của đường A dốc hơn đường B. Vì thế A cho độ lớn $dB/dt$ cực đại lớn hơn và dòng cảm ứng cực đại lớn hơn. Chọn (a). Đỉnh trường cao hơn của B không tự bảo đảm dòng cảm ứng lớn hơn.
:::

::: exercise 29.74
Nếu mô được xem như mạch điện trở, đồ thị nào biểu diễn đúng dòng cảm ứng $i$ theo thời gian? Đơn vị dòng trên hình là tùy ý.

![Hình P29.74: Bốn đồ thị dòng đề xuất A, B, C và D.](img/young-29/hinh-p29-74.png)

(a) A.

(b) B.

(c) C.

(d) D.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Xung trường tăng nhanh, đạt đỉnh rồi giảm chậm. Điện trở được xem không đổi và bỏ qua tự cảm.

**Hướng đi:**

- Dòng tỉ lệ đạo hàm có dấu của trường qua $i=\mathcal E/R$.
- Dòng phải đổi dấu khi trường qua cực đại, với đỉnh lớn ở giai đoạn tăng nhanh và đuôi trái dấu nhỏ hơn khi trường giảm chậm.

Đồ thị C có xung lớn ban đầu, qua không lúc trường đạt cực đại, rồi có phần trái dấu kéo dài và giảm về không. Nó phù hợp dạng đạo hàm của xung đã cho, với quy ước chiều dương như hình. Chọn (c).
:::
