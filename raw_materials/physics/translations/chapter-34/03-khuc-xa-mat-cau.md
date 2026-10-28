## 34.3. Khúc xạ tại mặt cầu

Bên cạnh hiện tượng phản xạ, hình ảnh quang học còn được tạo ra nhờ hiện tượng khúc xạ qua các mặt phân cách trong suốt. Việc khảo sát sự khúc xạ tại một mặt cầu đơn lẻ là bước đệm cơ bản để phân tích các hệ quang học phức tạp hơn, từ mắt người đến hệ thấu kính nhiều tầng trong kính hiển vi và kính thiên văn.

### Tạo ảnh của một vật điểm qua mặt cầu khúc xạ

Xét một mặt cầu bán kính $R$ tạo thành bề mặt phân cách giữa hai môi trường trong suốt có chiết suất khác nhau $n_a$ và $n_b$ như biểu diễn ở Hình 34.21.

![Hình 34.21: Quá trình tạo ảnh của một vật điểm P qua mặt phân cách hình cầu giữa hai môi trường có chiết suất na và nb (với na < nb). Bán kính cong R, khoảng cách vật s và khoảng cách ảnh s′ đều mang giá trị dương.](../img/young-34/hinh-34-21.png)

Ta áp dụng hệ thống quy tắc dấu đã thiết lập:
- Vật điểm $P$ nằm ở phía ánh sáng tới, do đó khoảng cách vật $s$ mang giá trị dương ($s > 0$).
- Ánh sáng khúc xạ truyền qua bề mặt phân cách sang môi trường thứ hai, do đó phía ánh sáng ra là phía bên trong môi trường $b$.
- Tâm cong $C$ của mặt cầu nằm ở phía ánh sáng ra, nên bán kính cong $R$ mang giá trị dương ($R > 0$).
- Điểm $V$ là đỉnh của mặt cầu, đường thẳng đi qua $P$, $V$, $C$ là trục quang của hệ.

Tia sáng $PV$ truyền dọc theo trục quang đập vuông góc vào mặt cầu tại đỉnh $V$, do đó tia này truyền thẳng sang môi trường $b$ mà không bị đổi hướng.

Một tia sáng thứ hai xuất phát từ $P$ đập vào mặt cầu tại điểm $B$ dưới góc tới $\theta_a$ so với pháp tuyến $CB$. Tia sáng khúc xạ vào môi trường $b$ với góc khúc xạ $\theta_b$ tuân theo định luật Snell. Khi $n_a < n_b$, tia khúc xạ bị bẻ lệch lại gần pháp tuyến hơn và cắt trục quang tại điểm $P'$. Điểm $P'$ chính là ảnh của $P$. Vì các tia sáng thực sự hội tụ tại $P'$, đây là một **ảnh thật** (real image), và khoảng cách ảnh $s'$ mang giá trị dương ($s' > 0$).

Để tìm mối liên hệ giữa $s$, $s'$ và $R$, ta xét các góc $\alpha$, $\beta$ và $\phi$ tạo bởi các đoạn thẳng $PB$, $P'B$ và $CB$ với trục quang:

Trong tam giác $PBC$, góc ngoài tại đỉnh $B$ là góc tới $\theta_a$:

$$
\theta_a = \alpha + \phi \tag{34.8}
$$

Trong tam giác $P'BC$, góc ngoài tại đỉnh $C$ là góc $\phi$:

$$
\phi = \beta + \theta_b
$$

Suy ra:

$$
\theta_b = \phi - \beta \tag{34.9}
$$

Theo định luật khúc xạ ánh sáng (định luật Snell):

$$
n_a \sin \theta_a = n_b \sin \theta_b
$$

Trong giới hạn gần đúng cận trục, góc $\alpha$ rất nhỏ, kéo theo các góc $\beta$, $\phi$, $\theta_a$ và $\theta_b$ đều rất nhỏ. Khi đó ta có thể xấp xỉ $\sin \theta_a \approx \theta_a$ và $\sin \theta_b \approx \theta_b$. Định luật Snell trở thành:

$$
n_a \theta_a \approx n_b \theta_b
$$

Thay các biểu thức của $\theta_a$ và $\theta_b$ từ phương trình (34.8) và (34.9) vào:

$$
n_a (\alpha + \phi) = n_b (\phi - \beta)
$$

Khai triển và sắp xếp lại các số hạng:

$$
n_a \alpha + n_b \beta = (n_b - n_a)\phi \tag{34.10}
$$

Gọi $h$ là khoảng cách từ điểm tới $B$ hạ vuông góc xuống trục quang. Trong gần đúng cận trục, khoảng cách từ chân đường vuông góc này đến đỉnh $V$ là không đáng kể, do đó ta có các xấp xỉ tang góc theo radian:

$$
\alpha \approx \frac{h}{s}
$$

$$
\beta \approx \frac{h}{s'}
$$

$$
\phi \approx \frac{h}{R}
$$

Thay các góc này vào phương trình (34.10):

$$
n_a \frac{h}{s} + n_b \frac{h}{s'} = (n_b - n_a)\frac{h}{R}
$$

Triệt tiêu đại lượng $h$ ở cả hai vế, ta nhận được **phương trình tạo ảnh qua mặt cầu khúc xạ**:

$$
\frac{n_a}{s} + \frac{n_b}{s'} = \frac{n_b - n_a}{R} \tag{34.11}
$$

Biểu thức này không chứa góc $\alpha$. Do đó, trong gần đúng cận trục, mọi tia sáng xuất phát từ vật điểm $P$ sau khi khúc xạ đều hội tụ chính xác tại cùng một ảnh điểm $P'$.

### Quy tắc dấu cho mặt khúc xạ

Để phương trình (34.11) có hiệu lực tổng quát cho mọi trường hợp (mặt lồi, mặt lõm, chùm tia hội tụ, chùm tia phân kỳ, ảnh thật hoặc ảnh ảo), ta tuân thủ quy tắc dấu thống nhất:

- Khoảng cách vật $s$: Mang dấu dương ($s > 0$) khi vật nằm ở phía ánh sáng tới. Mang dấu âm ($s < 0$) đối với vật ảo.
- Khoảng cách ảnh $s'$: Mang dấu dương ($s' > 0$) khi ảnh nằm ở phía ánh sáng ra (phía môi trường thứ hai, ảnh thật). Mang dấu âm ($s' < 0$) khi ảnh nằm ở phía ánh sáng tới (ảnh ảo).
- Bán kính cong $R$: Mang dấu dương ($R > 0$) khi tâm cong $C$ nằm ở phía ánh sáng ra. Mang dấu âm ($R < 0$) khi tâm cong $C$ nằm ở phía ánh sáng tới.

> [!IMPORTANT]
> Điểm khác biệt mấu chốt giữa gương và mặt khúc xạ nằm ở vị trí của "phía ánh sáng ra":
> - Đối với gương: Ánh sáng bị phản xạ quay ngược trở lại, do đó phía ánh sáng ra nằm cùng phía với phía ánh sáng tới.
> - Đối với mặt khúc xạ: Ánh sáng xuyên qua bề mặt phân cách sang môi trường thứ hai, do đó phía ánh sáng ra nằm ở phía bên kia bề mặt phân cách.

### Độ phóng đại ngang của mặt khúc xạ

Xét một vật phẳng nhỏ có chiều cao $y$ đặt vuông góc với trục quang tại điểm $P$ như mô tả ở Hình 34.22. Đỉnh của vật là điểm $Q$. Tia sáng từ $Q$ chiếu thẳng tới đỉnh $V$ tạo góc tới $\theta_a$ với trục quang. Tia khúc xạ tương ứng tạo góc khúc xạ $\theta_b$ với trục quang và đi tới đỉnh ảnh $Q'$ có độ cao $y'$.

![Hình 34.22: Cách xác định độ phóng đại ngang m của mặt khúc xạ hình cầu. Tia sáng truyền tới đỉnh V tuân theo định luật Snell na sin θa = nb sin θb.](../img/young-34/hinh-34-22.png)

Theo định luật Snell:

$$
n_a \sin \theta_a = n_b \sin \theta_b
$$

Trong gần đúng góc nhỏ:

$$
n_a \theta_a \approx n_b \theta_b
$$

Quan sát hai tam giác vuông ở hai phía đỉnh $V$:
- Tam giác vật có $\tan \theta_a \approx \theta_a = y/s$.
- Tam giác ảnh có đỉnh $Q'$ nằm phía dưới trục quang, nên $\tan \theta_b \approx \theta_b = -y'/s'$.

Thay vào định luật Snell:

$$
n_a \left(\frac{y}{s}\right) = -n_b \left(\frac{y'}{s'}\right)
$$

Suy ra tỷ số kích thước ảnh trên kích thước vật:

$$
\begin{aligned}
m &= \frac{y'}{y} \\
&= -\frac{n_a s'}{n_b s}
\end{aligned} \tag{34.12}
$$

Độ phóng đại ngang $m$ cho biết:
- Dấu của $m$: Nếu $m > 0$, ảnh cùng chiều với vật. Nếu $m < 0$, ảnh ngược chiều với vật.
- Độ lớn $|m|$ biểu thị độ phóng đại kích thước của ảnh so với vật.

Hiện tượng khúc xạ qua mặt cong giải thích việc người làm vườn tránh tưới cây giữa trưa. Khi ánh sáng Mặt Trời đi vào một giọt nước trên lá (Hình 34.23), các tia khúc xạ hội tụ về phía nhau như trong Hình 34.21 và 34.22. Do đó, ánh sáng Mặt Trời chiếu tới phiến lá bị tập trung năng lượng nhiều hơn và có thể gây tổn thương lá.

![Hình 34.23: Các tia sáng bị khúc xạ khi truyền qua các bề mặt cong của những giọt nước đọng trên lá cây.](../img/young-34/hinh-34-23.png)

### Khúc xạ qua mặt phẳng

Mặt phân cách phẳng giữa hai môi trường là trường hợp giới hạn đặc biệt của mặt cầu khi bán kính cong tiến tới vô cực ($R \to \infty$). Thay $R = \infty$ vào phương trình (34.11), vế phải bằng không:

$$
\frac{n_a}{s} + \frac{n_b}{s'} = 0
$$

Biến đổi tìm khoảng cách ảnh:

$$
\frac{n_b}{s'} = -\frac{n_a}{s}
$$

Dẫn tới hệ thức tạo ảnh qua **mặt phân cách phẳng**:

$$
s' = -\frac{n_b}{n_a} s \tag{34.13}
$$

Thay hệ thức này vào công thức độ phóng đại ngang (34.12):

$$
\begin{aligned}
m &= -\frac{n_a}{n_b s} \left(-\frac{n_b}{n_a} s\right) \\
&= +1
\end{aligned}
$$

Kết quả $m = +1$ mang ý nghĩa vật lý quan trọng: Với vật thật, mặt phân cách phẳng tạo ra ảnh ảo cùng chiều và có kích thước ngang bằng đúng kích thước của vật, không phụ thuộc vào chiết suất hai môi trường.

### Ví dụ 34.5: Tạo ảnh qua thanh thủy tinh đầu cầu đặt trong không khí

Một thanh thủy tinh hình trụ đặc có chiết suất $n_b = 1{,}52$ được mài một đầu thành mặt cầu lồi bán kính cong $R = +2{,}00\,\mathrm{cm}$. Thanh thủy tinh đặt trong không khí ($n_a = 1{,}00$). Một vật điểm nhỏ $P$ đặt trên trục quang trong không khí, cách đỉnh mặt cầu một khoảng $s = 8{,}00\,\mathrm{cm}$. Hãy tìm vị trí của ảnh và độ phóng đại ngang.

![Hình 34.24: Tạo ảnh của một vật điểm qua thanh thủy tinh đầu cầu đặt trong không khí. Vì na < nb và s đủ lớn, mặt cầu lồi tạo ra ảnh thật P′ nằm bên trong thanh thủy tinh.](../img/young-34/hinh-34-24.png)

**Nhận dạng bài toán**: Xác định vị trí ảnh và độ phóng đại qua một mặt cầu khúc xạ lồi ngăn cách không khí và thủy tinh.

**Chuẩn bị**: Áp dụng phương trình tạo ảnh (34.11) và công thức độ phóng đại ngang (34.12).
- Môi trường tới: Không khí $n_a = 1{,}00$.
- Môi trường ra: Thủy tinh $n_b = 1{,}52$.
- Bán kính cong: Tâm cong nằm trong thủy tinh (phía ánh sáng ra), nên $R = +2{,}00\,\mathrm{cm}$.
- Khoảng cách vật: $s = +8{,}00\,\mathrm{cm}$.

**Thực hiện**: Áp dụng phương trình (34.11):

$$
\frac{n_a}{s} + \frac{n_b}{s'} = \frac{n_b - n_a}{R}
$$

Thay các giá trị số vào:

Đặt P là vế phải của phương trình tạo ảnh và Q là số hạng do vật:

$$
\begin{aligned}
P&=\frac{n_b-n_a}{R}\\
&=\frac{1{,}52-1{,}00}{2{,}00\,\mathrm{cm}}\\
&=0{,}260\,\mathrm{cm^{-1}}.
\end{aligned}
$$

$$
Q=\frac{n_a}{s}=0{,}125\,\mathrm{cm^{-1}}.
$$

Phương trình tạo ảnh trở thành $n_b/s'=P-Q$.

Chuyển vế:

$$
\begin{aligned}
\frac{1{,}52}{s'}&=P-Q\\
&=(0{,}260-0{,}125)\,\mathrm{cm^{-1}}\\
&=0{,}135\,\mathrm{cm^{-1}}.
\end{aligned}
$$

Suy ra khoảng cách ảnh:

$$
\begin{aligned}
s' &= \frac{1{,}52}{0{,}135\,\mathrm{cm}^{-1}} \\
&\approx +11{,}26\,\mathrm{cm} \approx +11{,}3\,\mathrm{cm}
\end{aligned}
$$

Độ phóng đại ngang của ảnh:

$$
\begin{aligned}
m &= -\frac{n_a s'}{n_b s} \\
&= -\frac{(1{,}00)(+11{,}26\,\mathrm{cm})}{(1{,}52)(8{,}00\,\mathrm{cm})} \\
&\approx -0{,}926
\end{aligned}
$$

**Đánh giá**: Vì $s' > 0$, ảnh tạo thành là ảnh thật nằm bên trong thủy tinh, cách đỉnh mặt cầu $11{,}3\,\mathrm{cm}$ về phía sau. Vì $m < 0$, ảnh bị ngược chiều so với vật. Độ lớn $|m| \approx 0{,}93$ cho biết kích thước ảnh thu nhỏ nhẹ khoảng 7% so với vật.

Với vật là mũi tên cao $1{,}000\,\mathrm{mm}$ hướng lên, ảnh hướng xuống và cao khoảng $0{,}926\,\mathrm{mm}$ khi giữ đủ chữ số. Nếu dùng khoảng ảnh đã làm tròn $11{,}3\,\mathrm{cm}$ ngay trong phép tính phóng đại, ta nhận khoảng $0{,}929\,\mathrm{mm}$. Sự khác biệt nhỏ này xuất phát từ bước làm tròn trung gian.

**Khái niệm cần nhớ**: Một mặt cầu lồi ngăn cách giữa môi trường chiết quang kém sang môi trường chiết quang hơn có tác dụng hội tụ chùm tia sáng và có thể tạo ra ảnh thật của một vật thật.

### Ví dụ 34.6: Thanh thủy tinh nhúng trong nước

Xét lại thanh thủy tinh trong Ví dụ 34.5 ($n_b = 1{,}52, R = +2{,}00\,\mathrm{cm}$), nhưng bây giờ toàn bộ hệ thống được nhúng vào trong một bể nước có chiết suất $n_a = 1{,}33$. Vật điểm vẫn đặt cách đỉnh mặt cầu một khoảng $s = 8{,}00\,\mathrm{cm}$. Hãy xác định vị trí và tính chất của ảnh mới.

![Hình 34.25: Khi thanh thủy tinh được nhúng trong nước, độ chênh lệch chiết suất giữa hai môi trường giảm đáng kể, khiến mặt cầu không còn đủ khả năng bẻ hội tụ các tia sáng. Kết quả là tạo ra một ảnh ảo P′ nằm ở phía nước.](../img/young-34/hinh-34-25.png)

**Nhận dạng bài toán**: Bài toán khúc xạ tại mặt cầu khi môi trường tới thay đổi từ không khí sang nước.

**Chuẩn bị**: Áp dụng phương trình (34.11) và (34.12) với các thông số:
- $n_a = 1{,}33$ (nước).
- $n_b = 1{,}52$ (thủy tinh).
- $R = +2{,}00\,\mathrm{cm}$.
- $s = +8{,}00\,\mathrm{cm}$.

**Thực hiện**: Áp dụng phương trình tạo ảnh:

$$
\frac{n_a}{s} + \frac{n_b}{s'} = \frac{n_b - n_a}{R}
$$

Thay số:

Đặt P là vế phải của phương trình tạo ảnh và Q là số hạng do vật:

$$
\begin{aligned}
P&=\frac{n_b-n_a}{R}\\
&=\frac{1{,}52-1{,}33}{2{,}00\,\mathrm{cm}}\\
&=0{,}0950\,\mathrm{cm^{-1}}.
\end{aligned}
$$

$$
Q=\frac{n_a}{s}=0{,}16625\,\mathrm{cm^{-1}}.
$$

Phương trình tạo ảnh trở thành $n_b/s'=P-Q$.

Chuyển vế:

$$
\begin{aligned}
\frac{1{,}52}{s'}&=P-Q\\
&=(0{,}0950-0{,}16625)\,\mathrm{cm^{-1}}\\
&=-0{,}07125\,\mathrm{cm^{-1}}.
\end{aligned}
$$

Suy ra khoảng cách ảnh:

$$
\begin{aligned}
s' &= \frac{1{,}52}{-0{,}07125\,\mathrm{cm}^{-1}} \\
&\approx -21{,}33\,\mathrm{cm} \approx -21{,}3\,\mathrm{cm}
\end{aligned}
$$

Độ phóng đại ngang:

$$
\begin{aligned}
m &= -\frac{n_a s'}{n_b s} \\
&= -\frac{(1{,}33)(-21{,}33\,\mathrm{cm})}{(1{,}52)(8{,}00\,\mathrm{cm})} \\
&\approx +2{,}33
\end{aligned}
$$

**Đánh giá**: Khi nhúng vào nước, hiệu chiết suất $n_b - n_a$ giảm từ $0{,}52$ xuống chỉ còn $0{,}19$. Khả năng bẻ khúc xạ của mặt cầu bị yếu đi đáng kể, không còn đủ sức bẻ chùm tia phân kỳ từ vật thành chùm tia hội tụ. Các tia khúc xạ ló vào thủy tinh vẫn phân kỳ ra, và đường kéo dài của chúng cắt nhau tại điểm ảnh ảo $P'$ nằm trong nước, cách đỉnh mặt cầu $21{,}3\,\mathrm{cm}$ ($s' < 0$). Vì $m = +2{,}33 > 0$, ảnh cùng chiều và phóng đại lớn gấp $2{,}33$ lần vật.

**Khái niệm cần nhớ**: Khả năng hội tụ hay phân kỳ của một mặt khúc xạ phụ thuộc quyết định vào độ chênh lệch chiết suất giữa hai môi trường chứ không chỉ phụ thuộc vào bán kính cong hình học của bề mặt.

### Ví dụ 34.7: Độ sâu biểu kiến của bể bơi

Một người đứng trên bờ nhìn thẳng góc xuống đáy một bể bơi có độ sâu thực tế là $2{,}00\,\mathrm{m}$. Biết chiết suất của nước trong bể là $n_a = 1{,}33$ và chiết suất của không khí là $n_b = 1{,}00$. Hỏi đáy bể bơi dường như cách mặt nước bao nhiêu mét?

![Hình 34.26: Khúc xạ qua mặt nước phẳng làm đáy bể bơi bị nâng lên. Vật PQ ở đáy nước tạo ra ảnh ảo P′Q′ nằm nông hơn so với độ sâu thực tế.](../img/young-34/hinh-34-26.png)

**Nhận dạng bài toán**: Xác định độ sâu biểu kiến của vật chìm dưới nước khi quan sát từ không khí qua một mặt phân cách phẳng.

**Chuẩn bị**: Mặt nước là mặt phẳng khúc xạ có bán kính cong $R \to \infty$.
- Ánh sáng truyền từ đáy bể lên mắt người, do đó môi trường tới là nước ($n_a = 1{,}33$).
- Môi trường ra là không khí chứa mắt người quan sát ($n_b = 1{,}00$).
- Khoảng cách vật thực tế: $s = +2{,}00\,\mathrm{m}$.
- Áp dụng phương trình tạo ảnh qua mặt phẳng (34.13).

**Thực hiện**: Áp dụng phương trình (34.13):

$$
\begin{aligned}
s' &= -\frac{n_b}{n_a} s \\
&= -\frac{1{,}00}{1{,}33} (2{,}00\,\mathrm{m}) \\
&\approx -1{,}50\,\mathrm{m}
\end{aligned}
$$

Dấu âm khẳng định đây là ảnh ảo nằm ở phía ánh sáng tới, tức là nằm bên dưới mặt nước.

Độ sâu biểu kiến mà mắt nhìn thấy là khoảng cách hình học từ ảnh ảo tới mặt nước:

$$
d' = |s'| = 1{,}50\,\mathrm{m}
$$

Độ phóng đại ngang của ảnh:

$$
m = +1{,}00
$$

![Hình 34.27: Hình ảnh chiếc ống hút cắm nghiêng trong cốc nước minh họa hiện tượng độ sâu biểu kiến. Phần ngập nước trông như bị nâng lên gần mặt thoáng hơn, nhưng kích thước bề ngang của ống hút không hề bị biến dạng vì độ phóng đại ngang bằng đúng 1.](../img/young-34/hinh-34-27.png)

**Đánh giá**: Đáy bể bơi trông như chỉ sâu $1{,}50\,\mathrm{m}$, tức là nông hơn $25\%$ so với độ sâu thực tế $2{,}00\,\mathrm{m}$. Vì độ phóng đại ngang $m = +1$, các hoa văn hay viên gạch lát đáy bể giữ nguyên chiều rộng ngang thực tế, chỉ có vị trí theo phương thẳng đứng bị nâng cao lên về phía mặt nước. Đây là một hiện tượng quang học phổ biến cần lưu ý để tránh tai nạn đuối nước khi ước lượng độ sâu nguồn nước bằng mắt thường.

**Khái niệm cần nhớ**: Với vật thật, mặt phân cách phẳng tạo ảnh ảo có khoảng cách tỉ lệ với tỉ số chiết suất hai môi trường ($s' = -s n_b / n_a$), với kích thước ngang không đổi ($m = 1$).

### Câu hỏi tự kiểm tra 34.3

Các giọt nước ở Hình 34.23 có bán kính cong $R$ và chiết suất $n=1{,}33$. Ánh sáng Mặt Trời (coi là chùm tia sáng song song) chiếu thẳng góc vào bề mặt giọt sương. Các tia sáng Mặt Trời có hội tụ tại mặt sau của giọt sương tiếp xúc với phiến lá hay không?

<details><summary>Xem đáp án và giải thích</summary>

Không hội tụ tại mặt sau của giọt sương.

Giải thích:

Mặt Trời ở rất xa Trái Đất, do đó khoảng cách vật thực tế tiến tới vô cực ($s \to \infty$), kéo theo $1/s = 0$. Môi trường tới là không khí ($n_a = 1{,}00$) và môi trường khúc xạ là nước ($n_b = 1{,}33$). Bề mặt trước của giọt sương là mặt cầu lồi có bán kính cong $R > 0$.

Áp dụng phương trình tạo ảnh (34.11):

$$
\begin{aligned}
\frac{n_a}{s} + \frac{n_b}{s'} &= \frac{n_b - n_a}{R} \\
0 + \frac{1{,}33}{s'} &= \frac{1{,}33 - 1{,}00}{R} \\
&= \frac{0{,}33}{R}
\end{aligned}
$$

Suy ra khoảng cách ảnh từ mặt trước của giọt sương:

$$
s' = \frac{1{,}33}{0{,}33} R \approx 4{,}0 R
$$

Điểm hội tụ của chùm tia sáng cách bề mặt trước của giọt nước một khoảng bằng $4{,}0 R$. Tuy nhiên, vì giọt sương chỉ là một phần hình cầu, khoảng cách từ mặt trước đến mặt sau tiếp xúc với phiến lá tối đa chỉ bằng đường kính hình cầu $2 R$.

Vì $4{,}0 R > 2 R$, các tia sáng Mặt Trời sau khi khúc xạ qua mặt trước chưa kịp hội tụ đã chạm tới bề mặt phiến lá. Chùm tia sáng bị thu hẹp diện tích đáng kể và tập trung mật độ năng lượng cao, có thể làm nóng cục bộ phiến lá nhưng không tạo ảnh Mặt Trời trên lá. Khoảng $4R$ là kết quả xét khúc xạ ở mặt trước trong nước, không phải vị trí hội tụ thực sau khi đã đi qua thêm các mặt khác.

</details>
