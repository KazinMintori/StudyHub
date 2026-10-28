## 34.2. Phản xạ tại mặt cầu

Gương phẳng là trường hợp đặc biệt đơn giản nhất của hệ quang học phản xạ. Trong thực tế đời sống và khoa học kỹ thuật, các bề mặt phản xạ dạng cong, đặc biệt là mặt cầu, được dùng từ đèn pha ô tô, kính thiên văn phản xạ cho tới gương nha khoa và gương cầu lồi tại các khúc cua đường bộ. Bài học này khảo sát định lượng quá trình tạo ảnh qua các bề mặt phản xạ hình cầu.

### Gương cầu lõm

Xét một bề mặt phản xạ hình cầu lõm, trong đó mặt phản xạ quay về phía ánh sáng tới như biểu diễn ở Hình 34.10. Một gương như vậy được gọi là **gương cầu lõm** (concave spherical mirror).

![Hình 34.10: Quá trình tạo ảnh của một vật điểm qua gương cầu lõm. (a) Cách dựng hình hình học để xác định vị trí ảnh P′ dựa trên các định luật phản xạ. (b) Minh họa gần đúng cận trục khi góc nghiêng α của tia sáng rất nhỏ, đảm bảo mọi tia xuất phát từ P đều hội tụ tại cùng một ảnh điểm P′.](../img/young-34/hinh-34-10.png)

Bề mặt phản xạ có bán kính cong $R$, tâm cong của mặt cầu đặt tại điểm $C$, và tâm hình học của bề mặt gương được gọi là **đỉnh gương** $V$ (vertex). Đường thẳng nối tâm cong $C$ và đỉnh gương $V$ được định nghĩa là **trục quang** (optic axis).

Xét một vật điểm $P$ nằm trên trục quang, cách đỉnh gương $V$ một khoảng $s$. Một tia sáng $PV$ truyền dọc theo trục quang sẽ đập thẳng góc vào gương tại $V$ và bật ngược trở lại theo đúng phương cũ. Một tia sáng thứ hai xuất phát từ $P$ đập vào mặt gương tại điểm $B$ dưới góc tới $\theta$.

Đoạn thẳng nối tâm cong $C$ với điểm tới $B$ chính là bán kính của mặt cầu, do đó $CB$ đóng vai trò là pháp tuyến của bề mặt gương tại $B$. Theo định luật phản xạ, tia phản xạ $BP'$ tạo với pháp tuyến $CB$ một góc phản xạ đúng bằng góc tới $\theta$. Tia phản xạ này cắt trục quang tại điểm $P'$, cách đỉnh gương một khoảng $s'$. Vì hai tia sáng phản xạ cắt nhau tại $P'$, điểm $P'$ chính là ảnh của $P$. Vì các tia sáng thực sự hội tụ tại $P'$, đây là một **ảnh thật** (real image).

Để thiết lập mối liên hệ định lượng giữa khoảng cách vật $s$, khoảng cách ảnh $s'$ và bán kính cong $R$, ta xét các góc $\alpha$, $\beta$ và $\phi$ mà các đoạn thẳng $PB$, $P'B$ và $CB$ tạo với trục quang:

Trong tam giác $PBC$, góc $\phi$ là góc ngoài tại đỉnh $C$, do đó ta có:

$$
\phi = \alpha + \theta
$$

Suy ra:

$$
\theta = \phi - \alpha
$$

Hoàn toàn tương tự, xét tam giác $P'BC$, góc $\beta$ là góc ngoài tại đỉnh $P'$, nên ta có:

$$
\beta = \phi + \theta
$$

Thay biểu thức của $\theta$ từ hệ thức trên vào, ta thu được:

$$
\beta = \phi + (\phi - \alpha) = 2\phi - \alpha
$$

Chuyển vế, ta tìm được mối quan hệ góc cơ bản:

$$
\alpha + \beta = 2\phi \tag{34.3}
$$

Gọi $h$ là khoảng cách từ điểm tới $B$ hạ vuông góc xuống trục quang, và $d$ là khoảng cách từ chân đường vuông góc này tới đỉnh gương $V$. Nhận xét rằng $s$, $s'$ và $R$ đều là các độ dài hình học dương, ta có thể viết biểu thức tang của các góc:

$$
\tan \alpha = \frac{h}{s - d}
$$

$$
\tan \beta = \frac{h}{s' - d}
$$

$$
\tan \phi = \frac{h}{R - d}
$$

Các phương trình lượng giác này phụ thuộc vào điểm tới $B$ cụ thể. Tuy nhiên, nếu góc $\alpha$ rất nhỏ, góc tới $\theta$ cũng nhỏ, kéo theo các góc $\beta$ và $\phi$ đều rất nhỏ. Khi đó điểm tới $B$ nằm rất gần đỉnh gương $V$, khoảng cách $d$ trở nên không đáng kể so với $s$, $s'$ và $R$ ($d \approx 0$). Đồng thời ta có thể áp dụng gần đúng góc nhỏ theo radian:

$$
\tan \alpha \approx \alpha \approx \frac{h}{s}
$$

$$
\tan \beta \approx \beta \approx \frac{h}{s'}
$$

$$
\tan \phi \approx \phi \approx \frac{h}{R}
$$

Các tia sáng tạo các góc nhỏ với trục quang và truyền đi gần trục quang được gọi là **tia cận trục** (paraxial rays), và phép đơn giản hóa này được gọi là **gần đúng cận trục** (paraxial approximation).

Thay các gần đúng góc này vào phương trình (34.3):

$$
\frac{h}{s} + \frac{h}{s'} = \frac{2h}{R}
$$

Triệt tiêu đại lượng $h$ ở cả hai vế, ta thu được **phương trình tạo ảnh của gương cầu**:

$$
\frac{1}{s} + \frac{1}{s'} = \frac{2}{R} \tag{34.4}
$$

Phương trình (34.4) hoàn toàn không chứa góc $\alpha$. Điều này mang ý nghĩa vật lý cốt lõi: Trong giới hạn gần đúng cận trục, mọi tia sáng xuất phát từ vật điểm $P$ sau khi phản xạ trên mặt gương cầu đều hội tụ tại cùng một ảnh điểm duy nhất $P'$.

### Quy tắc dấu cho bán kính cong

Để phương trình tạo ảnh có thể áp dụng nhất quán cho cả gương phẳng, gương cầu lõm và gương cầu lồi, ta thiết lập quy tắc dấu chuẩn mực cho bán kính cong $R$:

- **Quy tắc dấu cho bán kính cong**: Bán kính cong $R$ mang giá trị dương ($R > 0$) khi tâm cong $C$ nằm ở phía ánh sáng phản xạ (ánh sáng ra). Ngược lại, $R$ mang giá trị âm ($R < 0$) khi tâm cong $C$ nằm ở phía đối diện với ánh sáng phản xạ.

![Hình 34.11: Quy ước dấu cho bán kính cong R của mặt phản xạ hình cầu. Khi tâm cong C nằm cùng phía với chùm tia phản xạ (ánh sáng ra), R mang giá trị dương. Khi tâm cong C nằm ở phía đối diện, R mang giá trị âm.](../img/young-34/hinh-34-11.png)

Đối với gương cầu lõm, tâm cong $C$ nằm cùng phía với chùm tia phản xạ truyền ra, do đó $R > 0$. Đối với mặt gương phẳng, bề mặt không có độ cong, tương ứng với bán kính cong vô cùng lớn ($R = \infty$). Khi đó phương trình (34.4) trở thành:

$$
\frac{1}{s} + \frac{1}{s'} = 0
$$

Kéo theo:

$$
s' = -s
$$

Kết quả này hoàn toàn trùng khớp với định luật tạo ảnh của gương phẳng.

### Quang sai cầu

Nếu chùm tia sáng tới mở rộng và góc $\alpha$ không còn nhỏ, gần đúng cận trục sẽ không còn chính xác. Các tia sáng đập vào gần rìa mép ngoài của gương cầu sẽ hội tụ tại một điểm trên trục quang nằm gần đỉnh gương hơn so với các tia cận trục. Hiện tượng này làm cho ảnh của một vật điểm không còn là một điểm sắc nét mà bị nhòe mờ, gọi là hiện tượng **quang sai cầu** (spherical aberration).

![Hình 34.12: Gương vật kính Hubble đường kính 2,4m ở phần (a). Sau khi lên quỹ đạo năm 1990, gương được phát hiện quá nông một lượng chỉ khoảng 1/50 bề rộng sợi tóc, gây quang sai cầu và ảnh sao nhòe ở (b). Hệ quang học hiệu chỉnh được lắp năm 1993 giúp gần như loại bỏ ảnh hưởng ấy ở (c).](../img/young-34/hinh-34-12.png)

Để triệt tiêu hoàn toàn quang sai cầu đối với chùm tia song song với trục quang, người ta có thể thay thế mặt gương cầu bằng một mặt **paraboloid** phản xạ. Gương paraboloid có đặc tính hình học tuyệt đối: Mọi tia tới song song với trục đối xứng sau khi phản xạ đều hội tụ chính xác tại tiêu điểm của paraboloid, bất kể khoảng cách từ tia tới tới trục lớn bao nhiêu.

### Tiêu điểm và tiêu cự

Khi một vật điểm nằm ở rất xa gương, khoảng cách vật tiến tới vô cực ($s \to \infty$). Các tia sáng tới xuất phát từ vật đi tới gương sẽ là một chùm tia song song với trục quang. Theo phương trình (34.4):

$$
\frac{1}{\infty} + \frac{1}{s'} = \frac{2}{R}
$$

Suy ra khoảng cách ảnh tương ứng:

$$
s' = \frac{R}{2}
$$

Điểm hội tụ của chùm tia tới song song này được gọi là **tiêu điểm** (focal point), ký hiệu là $F$. Khoảng cách từ đỉnh gương tới tiêu điểm được gọi là **tiêu cự** (focal length), ký hiệu là $f$. Ta có hệ thức liên hệ trực tiếp giữa tiêu cự và bán kính cong:

$$
f = \frac{R}{2} \tag{34.5}
$$

![Hình 34.13: Khái niệm tiêu điểm F và tiêu cự f của gương cầu lõm. (a) Chùm tia tới song song với trục quang sau phản xạ hội tụ tại tiêu điểm F, nằm cách đỉnh gương một khoảng f = R/2. (b) Ngược lại, một nguồn sáng đặt tại tiêu điểm F sẽ tạo ra chùm tia phản xạ song song với trục quang.](../img/young-34/hinh-34-13.png)

Nhờ tính thuận nghịch của chiều truyền ánh sáng, nếu ta đặt một vật điểm tại đúng tiêu điểm $F$ ($s = f = R/2$), các tia phản xạ sẽ trở thành một chùm tia song song với trục quang ($s' \to \infty$). Thay hệ thức $f = R/2$ vào phương trình (34.4), ta có thể viết phương trình tạo ảnh của gương cầu dưới dạng quen thuộc:

$$
\frac{1}{s} + \frac{1}{s'} = \frac{1}{f} \tag{34.6}
$$

### Kích thước ảnh và độ phóng đại ngang

Xét một vật phẳng nhỏ có chiều cao $y$ đặt vuông góc với trục quang tại điểm $P$, như mô tả ở Hình 34.14. Đỉnh của vật là điểm $Q$. Để tìm ảnh $Q'$ của điểm $Q$, ta vẽ một tia sáng xuất phát từ $Q$ đập vào đỉnh gương $V$. Góc tới của tia này là $\theta$. Tia phản xạ $VQ'$ tạo với trục quang một góc phản xạ đúng bằng $\theta$. Tia này cắt đường thẳng hạ vuông góc từ ảnh điểm $P'$ tại $Q'$. Đoạn thẳng $P'Q'$ có chiều cao là $y'$, chính là ảnh của vật $PQ$.

![Hình 34.14: Cách xác định độ phóng đại ngang m của gương cầu lõm. Do hai tam giác vuông PVQ và P′VQ′ đồng dạng, tỷ số kích thước ảnh trên kích thước vật liên hệ trực tiếp với tỷ số khoảng cách ảnh và khoảng cách vật.](../img/young-34/hinh-34-14.png)

Độ phóng đại ngang (lateral magnification) $m$ được định nghĩa là tỷ số giữa kích thước ảnh $y'$ và kích thước vật $y$:

$$
m = \frac{y'}{y}
$$

Quan sát hai tam giác vuông $PVQ$ và $P'VQ'$ ở Hình 34.14, ta thấy chúng đồng dạng vì có chung góc nhọn $\theta$. Do đó ta có tỷ số cạnh:

$$
\frac{y}{s} = -\frac{y'}{s'}
$$

Dấu âm xuất hiện vì vật và ảnh nằm ở hai phía đối diện của trục quang: Khi vật hướng lên trên trục quang ($y > 0$), ảnh hướng xuống dưới trục quang ($y' < 0$). Từ đó ta thu được công thức tính **độ phóng đại ngang**:

$$
\begin{aligned}
m &= \frac{y'}{y} \\
&= -\frac{s'}{s}
\end{aligned} \tag{34.7}
$$

Ý nghĩa của độ phóng đại ngang $m$:
- Nếu $m > 0$: Ảnh cùng chiều với vật (erect image).
- Nếu $m < 0$: Ảnh ngược chiều với vật (inverted image).
- Độ lớn $|m|$ cho biết ảnh lớn gấp bao nhiêu lần vật: Nếu $|m| > 1$, ảnh phóng đại lớn hơn vật. Nếu $|m| < 1$, ảnh thu nhỏ hơn vật.

::: warning Độ phóng đại có thể nhỏ hơn1
Tên gọi độ phóng đại không hàm ý ảnh luôn lớn hơn vật. Ảnh có thể nhỏ hơn, lớn hơn hoặc bằng vật. Ảnh của một ngôi sao qua gương thiên văn chỉ rộng vài milimét, dù đường kính ngôi sao hàng trăm nghìn kilômét.
:::

Vật thật ở ngoài tiêu điểm gương lõm cho ảnh thật ngược chiều. Vật ở trong tiêu cự cho ảnh ảo cùng chiều và phóng đại. Vì vậy, gương trang điểm là gương lõm, dùng với khoảng mặt–gương nhỏ hơn tiêu cự.

### Ứng dụng: Chảo thu tín hiệu truyền hình vệ tinh

Chảo thu truyền hình vệ tinh là một gương parabol lõm. Sóng thu có tần số khoảng $1{,}2\times10^{10}$ đến $1{,}8\times10^{10}\,\mathrm{Hz}$, thấp hơn nhiều so với ánh sáng nhìn thấy, khoảng $4{,}0\times10^{14}$ đến $7{,}9\times10^{14}\,\mathrm{Hz}$. Tuy nhiên, chúng tuân theo cùng định luật phản xạ.

Máy phát trên quỹ đạo ở rất xa nên các tia sóng tới gần như song song. Chảo phản xạ và hội tụ chúng tại ống thu sóng. Từ đó, tín hiệu được dẫn đến bộ giải mã để tách nội dung truyền hình.

![Ứng dụng: Chảo parabol và sơ đồ phản xạ hội tụ sóng từ vệ tinh tại ống thu. Phần chảo lệch trục giúp bộ thu không chắn sóng tới.](../img/young-34/ung-dung-34-chao-thu.png)

### Ví dụ 34.1: Tạo ảnh bằng gương cầu lõm

Một gương lõm tạo ảnh dây tóc đèn pha trên bức tường cách gương $3{,}00\,\mathrm m$ phía trước. Dây tóc cách gương $10{,}0\,\mathrm{cm}$ và cao $5{,}00\,\mathrm{mm}$.

(a) Hãy xác định bán kính cong cần thiết của gương và tiêu cự của gương.

(b) Tính độ phóng đại ngang và chiều cao ảnh trên tường.

![Hình 34.15: Bản phác thảo các tia sáng cho bài toán này (Ví dụ 34.1).](../img/young-34/hinh-34-15.png)

**Nhận dạng bài toán**: Bài toán yêu cầu tìm các thông số hình học của gương cầu lõm (bán kính $R$ và tiêu cự $f$) và chiều cao ảnh khi biết khoảng cách vật $s$, khoảng cách ảnh thật $s'$, và chiều cao vật ban đầu $y$.

**Chuẩn bị**: Áp dụng phương trình tạo ảnh gương cầu (34.4), hệ thức liên hệ tiêu cự (34.5), và công thức độ phóng đại ngang (34.7).

Các dữ kiện đã cho:
- Chiều cao vật: $y = +0{,}500\,\mathrm{cm}$.
- Khoảng cách vật: $s = +10{,}0\,\mathrm{cm} = +0{,}100\,\mathrm{m}$.
- Vì ảnh được hứng rõ nét trên màn, ảnh là ảnh thật nằm ở phía ánh sáng phản xạ, do đó khoảng cách ảnh mang dấu dương: $s' = +3{,}00\,\mathrm{m} = +300\,\mathrm{cm}$.

**Thực hiện**:

(a) Áp dụng phương trình tạo ảnh của gương cầu:

$$
\frac{1}{s} + \frac{1}{s'} = \frac{2}{R}
$$

Thay số:

Hai nghịch đảo khoảng cách có giá trị:

$$
\begin{aligned}
&\frac1s=0{,}100\,\mathrm{cm^{-1}},\\
&\frac1{s'}\approx0{,}00333\,\mathrm{cm^{-1}}.
\end{aligned}
$$

Từ phương trình gương cầu:

$$
\begin{aligned}
\frac2R&=\frac1s+\frac1{s'}\\
&\approx(0{,}100+0{,}00333)\,\mathrm{cm^{-1}}\\
&=0{,}10333\,\mathrm{cm^{-1}}.
\end{aligned}
$$

Suy ra bán kính cong:

$$
\begin{aligned}
R &= \frac{2}{0{,}10333\,\mathrm{cm}^{-1}} \\
&\approx 19{,}35\,\mathrm{cm} \approx 19{,}4\,\mathrm{cm}
\end{aligned}
$$

Tiêu cự của gương:

$$
\begin{aligned}
f &= \frac{R}{2} \\
&= \frac{19{,}35\,\mathrm{cm}}{2} \\
&\approx 9{,}68\,\mathrm{cm}
\end{aligned}
$$

(b) Độ phóng đại ngang của gương là:

$$
\begin{aligned}
m &= -\frac{s'}{s} \\
&= -\frac{300\,\mathrm{cm}}{10{,}0\,\mathrm{cm}} \\
&= -30{,}0
\end{aligned}
$$

Chiều cao của ảnh là:

$$
\begin{aligned}
y'&=my\\
&=(-30{,}0)(0{,}500\,\mathrm{cm})\\
&=-15{,}0\,\mathrm{cm}.
\end{aligned}
$$

**Đánh giá**: Giá trị âm của $m$ và $y'$ khẳng định ảnh tạo thành là ảnh ngược chiều so với vật. Chiều cao độ lớn của ảnh là $15{,}0\,\mathrm{cm}$, lớn gấp 30 lần kích thước vật ban đầu. Bán kính cong $R$ và tiêu cự $f$ đều mang dấu dương, hoàn toàn phù hợp với tính chất của gương cầu lõm.

**Khái niệm cần nhớ**: Một gương cầu lõm có thể tạo ra ảnh thật, phóng đại rất lớn của một vật đặt ngoài tiêu cự nhưng gần tiêu điểm của gương.

### Ví dụ 34.2: Một nửa gương bị phủ bồ hóng

Xét lại chiếc gương cầu lõm trong Ví dụ 34.1. Giả sử người ta phủ một lớp bồ hóng đen hoàn toàn lên nửa dưới của bề mặt gương, khiến nửa dưới không còn khả năng phản xạ ánh sáng. Điều gì sẽ xảy ra với hình ảnh của vật trên màn hứng?

**Nhận dạng bài toán**: Câu hỏi định tính về bản chất tạo ảnh của từng phần tử diện tích trên bề mặt gương.

**Chuẩn bị**: Áp dụng nguyên lý tạo ảnh độc lập: Mỗi điểm trên vật phát ra ánh sáng tỏa theo mọi hướng đến khắp các vùng trên bề mặt gương.

**Thực hiện**: Mọi điểm trên vật phát ra vô số tia sáng truyền tới nửa trên của gương. Vì nửa trên của gương vẫn giữ nguyên hình dạng cầu với cùng bán kính cong $R$, mọi tia sáng cận trục đập vào nửa trên này vẫn phản xạ và hội tụ chính xác về cùng các ảnh điểm $P'$ trên màn như trước.

Do đó, toàn bộ hình ảnh đầy đủ của vật vẫn được tạo ra trọn vẹn trên màn, không có bất kỳ phần nào của ảnh bị biến mất hay bị cắt cụt. Tuy nhiên, vì diện tích phản xạ của gương bị giảm đi một nửa, tổng năng lượng ánh sáng hội tụ về màn bị giảm 50%, khiến hình ảnh hiển thị bị mờ đi và có độ sáng chỉ bằng một nửa so với ban đầu.

**Đánh giá**: Kết luận này hoàn toàn thống nhất với thực tế: Khi che bớt một phần gương hay thấu kính, ảnh không bị mất góc mà chỉ bị giảm độ sáng.

**Khái niệm cần nhớ**: Mỗi phần của bề mặt phản xạ đều tham gia tạo dựng toàn bộ hình ảnh. Việc che bớt một phần bề mặt chỉ làm giảm độ rọi của ảnh chứ không làm mất thông tin hình học của ảnh.

### Gương cầu lồi

Khi bề mặt lồi của mặt cầu quay về phía ánh sáng tới, ta có một **gương cầu lồi** (convex spherical mirror).

![Hình 34.16: Quá trình tạo ảnh qua gương cầu lồi. (a) Cách dựng hình tìm vị trí ảnh ảo P′ của một vật điểm P. Vì tâm cong C nằm ở phía sau gương (khác phía với ánh sáng phản xạ), bán kính R mang giá trị âm. (b) Cách xác định độ phóng đại ngang của vật PQ: Ảnh P′Q′ luôn là ảnh ảo, cùng chiều và nhỏ hơn vật.](../img/young-34/hinh-34-16.png)

Ở gương cầu lồi, tâm cong $C$ nằm ở phía sau gương, tức là phía đối diện với chùm tia phản xạ truyền ra. Theo quy tắc dấu ở Hình 34.11, bán kính cong của gương cầu lồi mang giá trị âm ($R < 0$).

Xét một tia sáng $PB$ xuất phát từ vật điểm $P$ nằm trên trục quang (Hình 34.16a). Pháp tuyến tại điểm tới $B$ là đường thẳng nối tâm cong $C$ với $B$. Tia phản xạ bị bẻ lệch xa trục quang. Khi kéo dài tia phản xạ này về phía sau mặt gương, nó cắt trục quang tại điểm $P'$. Mọi tia cận trục khác phát ra từ $P$ sau khi phản xạ đều có đường kéo dài đi qua điểm $P'$.

Vì các tia phản xạ thực tế phân kỳ ra xa nhau và chỉ có đường kéo dài hình học của chúng cắt nhau ở phía sau gương, điểm $P'$ là một **ảnh ảo** (virtual image). Khoảng cách ảnh $s'$ mang giá trị âm ($s' < 0$).

Bằng các bước chứng minh hình học hoàn toàn tương tự như gương cầu lõm, với việc tuân thủ chặt chẽ quy tắc dấu ($s > 0, s' < 0, R < 0$), ta chứng minh được rằng phương trình tạo ảnh (34.4) và công thức độ phóng đại ngang (34.7) hoàn toàn nghiệm đúng đối với gương cầu lồi:

$$
\frac{1}{s} + \frac{1}{s'} = \frac{2}{R} = \frac{1}{f}
$$

$$
m = -\frac{s'}{s}
$$

### Tiêu điểm ảo của gương cầu lồi

Khi chùm tia sáng tới song song với trục quang chiếu vào gương cầu lồi ($s \to \infty$), các tia phản xạ phân kỳ ra như thể chúng xuất phát từ một điểm $F$ nằm ở phía sau gương, cách đỉnh một khoảng $f = R/2$ (Hình 34.17a).

![Hình 34.17: Tiêu điểm ảo F của gương cầu lồi. (a) Chùm tia tới song song với trục quang sau khi phản xạ trên mặt cầu lồi phân kỳ như thể phát ra từ tiêu điểm ảo F ở phía sau gương. (b) Các tia tới hội tụ hướng về tiêu điểm ảo F sau phản xạ sẽ trở thành chùm tia song song với trục quang.](../img/young-34/hinh-34-17.png)

Vì tâm cong $C$ nằm ở phía sau gương nên $R$ mang dấu âm, kéo theo tiêu cự $f$ của gương cầu lồi cũng mang dấu âm ($f < 0$). Điểm $F$ này được gọi là **tiêu điểm ảo** (virtual focal point).

![Hình 34.18: Quả cầu trang trí mạ bạc đóng vai trò như một gương cầu lồi. (a) Quả cầu tạo ra một ảnh ảo, thu nhỏ và cùng chiều của ông già Noel. (b) Bản phác thảo hai tia sáng tạo nên hình ảnh.](../img/young-34/hinh-34-18.png)

### Ví dụ 34.3: Bài toán tạo ảnh của ông già Noel

Ông già Noel tự kiểm tra xem mình có bị dính bồ hóng hay không bằng cách nhìn hình ảnh phản xạ của bản thân trong một quả cầu trang trí cây thông Noel mạ bạc cách ông $0{,}750\,\mathrm{m}$ (Hình 34.18a). Đường kính của quả cầu trang trí là $7{,}20\,\mathrm{cm}$. Các tài liệu tiêu chuẩn mô tả ông là một "chàng yêu tinh già vui vẻ", vì vậy ta ước lượng chiều cao của ông là $1{,}6\,\mathrm{m}$. Hình ảnh của ông già Noel do quả cầu tạo ra nằm ở đâu và cao bao nhiêu? Ảnh này là ảnh cùng chiều hay ngược chiều?

**Nhận dạng và chuẩn bị**: Hình 34.18b mô tả tình huống bài toán. Ông già Noel đóng vai trò là vật sáng, và bề mặt quả cầu gần ông nhất đóng vai trò như một gương cầu lồi. Các hệ thức liên hệ giữa khoảng cách vật, khoảng cách ảnh, tiêu cự và độ phóng đại hoàn toàn giống như đối với gương cầu lõm, miễn là ta áp dụng nhất quán quy tắc dấu. Bán kính cong và tiêu cự của gương cầu lồi mang dấu âm.
- Đường kính $D = 7{,}20\,\mathrm{cm} \implies$ Bán kính cong hình học là $r = D/2 = 3{,}60\,\mathrm{cm}$.
- Vì tâm cong nằm ở phía sau mặt phản xạ, bán kính cong mang dấu âm: $R = -3{,}60\,\mathrm{cm}$.
- Tiêu cự của gương: $f = R/2 = -1{,}80\,\mathrm{cm}$.
- Khoảng cách vật: $s = +0{,}750\,\mathrm{m} = +75{,}0\,\mathrm{cm}$.
- Chiều cao ước tính của ông già Noel: $y = 1{,}6\,\mathrm{m}$.

Ta giải phương trình tạo ảnh của gương cầu để tìm khoảng cách ảnh $s'$, sau đó dùng công thức độ phóng đại ngang để tính $m$ và chiều cao ảnh $y'$. Dấu của $m$ sẽ cho biết ảnh cùng chiều hay ngược chiều.

**Thực hiện**:

Áp dụng phương trình tạo ảnh:

$$
\frac{1}{s} + \frac{1}{s'} = \frac{1}{f}
$$

Biến đổi tìm khoảng cách ảnh $s'$:

Với $f=-1{,}80\,\mathrm{cm}$ và $s=75{,}0\,\mathrm{cm}$, hai nghịch đảo xấp xỉ là $1/f\approx-0{,}5556\,\mathrm{cm^{-1}}$ và $1/s\approx0{,}0133\,\mathrm{cm^{-1}}$:

$$
\begin{aligned}
\frac1{s'}&=\frac1f-\frac1s\\
&\approx(-0{,}5556-0{,}0133)\,\mathrm{cm^{-1}}\\
&=-0{,}5689\,\mathrm{cm^{-1}}.
\end{aligned}
$$

Suy ra:

$$
\begin{aligned}
s' &= \frac{1}{-0{,}5689\,\mathrm{cm}^{-1}} \\
&\approx -1{,}76\,\mathrm{cm}
\end{aligned}
$$

Vì $s'$ mang giá trị âm, ảnh nằm ở phía sau gương, tức là ở phía đối diện với ánh sáng phản xạ (Hình 34.18b), và đây là một ảnh ảo. Vị trí của ảnh nằm ở khoảng giữa đỉnh mặt trước và tâm của quả cầu.

Từ công thức độ phóng đại ngang:

$$
\begin{aligned}
m &= -\frac{s'}{s} \\
&= -\frac{-1{,}76\,\mathrm{cm}}{75{,}0\,\mathrm{cm}} \\
&= +0{,}0234
\end{aligned}
$$

Chiều cao của hình ảnh là:

$$
\begin{aligned}
y' &= m y \\
&= (0{,}0234)(1{,}6\,\mathrm{m}) \\
&= 3{,}8 \times 10^{-2}\,\mathrm{m} \\
&= 3{,}8\,\mathrm{cm}
\end{aligned}
$$

**Đánh giá**: Bản phác thảo cho thấy ảnh là ảnh cùng chiều, do đó cả $m$ và $y'$ đều mang dấu dương, hoàn toàn phù hợp với kết quả tính toán. Khi khoảng cách vật $s$ dương, gương cầu lồi luôn luôn tạo ra một ảnh cùng chiều, là ảnh ảo, thu nhỏ và bị đảo trái - phải. Vì vậy, gương cầu lồi được dùng ở giao lộ khuất, để giám sát cửa hàng và làm gương chiếu hậu góc rộng cho ô tô, xe tải. Lời nhắc trên nhiều gương có nghĩa: Vật ở gần hơn so với khoảng cách mà chúng có vẻ ở.

**Khái niệm cần nhớ**: Một gương cầu lồi có tiêu cự mang giá trị âm: Các tia sáng tới song song phản xạ từ gương phân kỳ như thể chúng xuất phát từ một tiêu điểm nằm ở phía sau gương. Các mối liên hệ giữa khoảng cách vật, khoảng cách ảnh và tiêu cự, cũng như giữa độ phóng đại, khoảng cách vật và khoảng cách ảnh đều giống hệt như đối với gương cầu lõm.

### Phương pháp đồ thị cho gương cầu

Bên cạnh việc giải đại số bằng các phương trình (34.6) và (34.7), ta có thể xác định trực quan vị trí, kích thước và tính chất của ảnh bằng phương pháp vẽ tia hình học. Phương pháp này dựa trên việc tìm giao điểm của một vài tia sáng đặc biệt xuất phát từ đỉnh của vật (điểm $Q$ không nằm trên trục quang). Bốn tia sáng này được gọi là **các tia chính** (principal rays), như biểu diễn ở Hình 34.19:

![Hình 34.19: Bốn tia chính dùng để dựng ảnh bằng phương pháp đồ thị. (a) Đối với gương cầu lõm. (b) Đối với gương cầu lồi. Chỉ cần vẽ chính xác hai trong số bốn tia chính là đủ để xác định vị trí của ảnh điểm Q′.](../img/young-34/hinh-34-19.png)

Bốn tia chính bao gồm:
1. **Tia 1 (Tia song song)**: Tia tới truyền song song với trục quang, sau khi phản xạ sẽ đi qua tiêu điểm $F$ của gương cầu lõm, hoặc có đường kéo dài đi qua tiêu điểm ảo $F$ của gương cầu lồi.
2. **Tia 2 (Tia tiêu điểm)**: Tia tới đi qua tiêu điểm $F$ của gương cầu lõm (hoặc có đường hướng tới tiêu điểm ảo $F$ của gương cầu lồi), sau khi phản xạ sẽ truyền song song với trục quang.
3. **Tia 3 (Tia tâm cong)**: Tia tới truyền dọc theo đường nối tâm cong $C$ sẽ đập vuông góc vào mặt gương và phản xạ bật ngược trở lại theo đúng đường truyền ban đầu.
4. **Tia 4 (Tia đỉnh gương)**: Tia tới đập vào đỉnh gương $V$ sẽ phản xạ đối xứng qua trục quang (góc phản xạ bằng góc tới so với trục quang).

> [!CAUTION]
> Các tia chính không phải là những tia sáng duy nhất tạo ảnh. Thực tế, mọi tia sáng từ điểm vật đập vào gương đều phản xạ đi qua điểm ảnh (đối với ảnh thật) hoặc có đường kéo dài đi qua điểm ảnh (đối với ảnh ảo). Chúng ta lựa chọn bốn tia chính đơn thuần vì quỹ đạo hình học của chúng có thể vẽ được ngay lập tức mà không cần dùng thước đo góc.

### Chiến lược giải bài toán: Tạo ảnh bằng gương cầu

- **Nhận dạng bài toán**: Áp dụng cho các bài toán xác định vị trí, kích thước hoặc tính chất của ảnh tạo bởi gương phẳng, gương cầu lõm hoặc gương cầu lồi.
- **Chuẩn bị**:
  1. Vẽ sơ đồ quang học rõ ràng thể hiện trục quang, vị trí đỉnh gương $V$, tiêu điểm $F$ và tâm cong $C$.
  2. Xác định các đại lượng đã cho và biến số cần tìm, luôn ghi nhớ tiêu cự liên hệ với bán kính cong qua hệ thức $f = R/2$.
- **Thực hiện**:
  1. Dựng đồ thị hình học bằng cách vẽ ít nhất hai tia chính xuất phát từ ngọn của vật để định vị điểm ảnh.
  2. Áp dụng phương trình tạo ảnh $1/s + 1/s' = 1/f$ và độ phóng đại ngang $m = -s'/s$.
  3. Tuân thủ nghiêm ngặt quy tắc dấu: Vật thật có $s > 0$. Ảnh thật có $s' > 0$, ảnh ảo có $s' < 0$. Gương lõm có $R > 0, f > 0$. Gương lồi có $R < 0, f < 0$.
- **Đánh giá**: Đối chiếu kết quả đại số tính toán được với hình vẽ đồ thị: Vị trí của ảnh trên hình vẽ phải hoàn toàn trùng khớp với giá trị $s'$, chiều của ảnh (cùng chiều hay ngược chiều) phải khớp với dấu của $m$.

### Ví dụ 34.4: Tạo ảnh bằng gương cầu lõm ở các khoảng cách vật khác nhau

Một chiếc gương cầu lõm có bán kính cong $R = +20\,\mathrm{cm}$, tương ứng với tiêu cự $f = R/2 = +10\,\mathrm{cm}$. Hãy dựng ảnh bằng phương pháp đồ thị và tính toán vị trí, độ phóng đại của ảnh đối với các khoảng cách vật sau:

(a) $s = 30\,\mathrm{cm}$.

(b) $s = 20\,\mathrm{cm}$.

(c) $s = 10\,\mathrm{cm}$.

(d) $s = 5\,\mathrm{cm}$.

![Hình 34.20: Dựng ảnh bằng phương pháp đồ thị cho gương cầu lõm có f = 10 cm ở bốn vị trí vật khác nhau. (a) Khi s = 30 cm, ảnh thật, ngược chiều và thu nhỏ. (b) Khi s = 20 cm = 2f, ảnh thật, ngược chiều và có kích thước bằng vật. (c) Khi s = 10 cm = f, chùm tia phản xạ song song, ảnh ở vô cực. (d) Khi s = 5 cm < f, ảnh ảo, cùng chiều và phóng đại.](../img/young-34/hinh-34-20.png)

**Nhận dạng bài toán**: Khảo sát toàn diện sự biến đổi tính chất ảnh tạo bởi gương cầu lõm khi vật di chuyển từ xa vào sát mặt gương.

**Chuẩn bị**: Áp dụng phương trình tạo ảnh (34.6) và công thức độ phóng đại ngang (34.7) với $f = +10\,\mathrm{cm}$.

**Thực hiện**:

(a) Khi $s = 30\,\mathrm{cm}$ (vật đặt ngoài tâm cong $C$, Hình 34.20a):

$$
\begin{aligned}
\frac{1}{s'} &= \frac{1}{f} - \frac{1}{s} \\
&= \frac{1}{10\,\mathrm{cm}} - \frac{1}{30\,\mathrm{cm}} \\
&= \frac{2}{30\,\mathrm{cm}}
\end{aligned}
$$

Suy ra:

$$
s' = +15\,\mathrm{cm}
$$

Độ phóng đại ngang:

$$
\begin{aligned}
m &= -\frac{s'}{s} \\
&= -\frac{15\,\mathrm{cm}}{30\,\mathrm{cm}} \\
&= -0{,}50
\end{aligned}
$$

Ảnh là ảnh thật ($s' > 0$), ngược chiều ($m < 0$), thu nhỏ bằng một nửa vật, nằm giữa $F$ và $C$. Cả 4 tia chính đều vẽ được dễ dàng.

(b) Khi $s = 20\,\mathrm{cm}$ (vật đặt đúng tại tâm cong $C = 2f$, Hình 34.20b):

$$
\begin{aligned}
\frac{1}{s'} &= \frac{1}{10\,\mathrm{cm}} - \frac{1}{20\,\mathrm{cm}} \\
&= \frac{1}{20\,\mathrm{cm}}
\end{aligned}
$$

Suy ra:

$$
s' = +20\,\mathrm{cm}
$$

Độ phóng đại ngang:

$$
m = -\frac{20\,\mathrm{cm}}{20\,\mathrm{cm}} = -1{,}0
$$

Ảnh là ảnh thật, ngược chiều, có kích thước bằng đúng vật và nằm đối xứng ngay tại tâm cong $C$.

(c) Khi $s = 10\,\mathrm{cm}$ (vật đặt đúng tại tiêu điểm $F$, Hình 34.20c):

$$
\begin{aligned}
\frac{1}{s'} &= \frac{1}{10\,\mathrm{cm}} - \frac{1}{10\,\mathrm{cm}} \\
&= 0
\end{aligned}
$$

Suy ra:

$$
s' \to \pm\infty
$$

Các tia phản xạ song song với nhau. Ảnh ở xa vô cực.

(d) Khi $s = 5\,\mathrm{cm}$ (vật đặt trong khoảng tiêu cự, giữa $F$ và $V$, Hình 34.20d):

$$
\begin{aligned}
\frac{1}{s'} &= \frac{1}{10\,\mathrm{cm}} - \frac{1}{5\,\mathrm{cm}} \\
&= -\frac{1}{10\,\mathrm{cm}}
\end{aligned}
$$

Suy ra:

$$
s' = -10\,\mathrm{cm}
$$

Độ phóng đại ngang:

$$
m = -\frac{-10\,\mathrm{cm}}{5\,\mathrm{cm}} = +2{,}0
$$

Ảnh là ảnh ảo ($s' < 0$), cùng chiều ($m > 0$), lớn gấp 2 lần vật và nằm ở phía sau mặt gương $10\,\mathrm{cm}$.

**Đánh giá**: Quan sát quy luật biến đổi qua 4 trường hợp: Khi vật ở rất xa, ảnh là ảnh thật nhỏ hơn vật và nằm sát tiêu điểm. Khi vật tiến lại gần gương, ảnh thật di chuyển ra xa gương hơn và tăng dần kích thước. Khi vật đến đúng tiêu điểm $F$, ảnh dịch ra vô cực. Khi vật vượt qua tiêu điểm vào trong khoảng tiêu cự, ảnh lập tức đổi bản chất thành ảnh ảo, cùng chiều và lớn hơn vật. Chúng ta có thể kiểm nghiệm trực tiếp các kết luận này bằng cách đưa ngón tay lại gần mặt lõm của một chiếc thìa kim loại sáng bóng.

**Khái niệm cần nhớ**: Đối với gương cầu lõm, vị trí của vật so với tiêu điểm quyết định bản chất thật hay ảo và chiều của ảnh.

### Câu hỏi tự kiểm tra 34.2

Một chiếc gương trang điểm được thiết kế sao cho hình ảnh phản chiếu khuôn mặt của bạn luôn cùng chiều và được phóng đại lớn hơn thực tế.

(a) Chiếc gương này là gương cầu lõm hay gương cầu lồi?

(b) Để nhìn thấy ảnh phóng đại, khoảng cách từ gương (có tiêu cự $f$) tới khuôn mặt bạn phải thỏa mãn điều kiện nào sau đây?
- (i) Bằng $|f|$.
- (ii) Nhỏ hơn $|f|$.
- (iii) Lớn hơn $|f|$.

<details><summary>Xem đáp án và giải thích</summary>

(a) Gương cầu lõm. (b) Chọn (ii).

Giải thích:

Gương cầu lồi luôn luôn tạo ra ảnh cùng chiều nhưng ảnh đó luôn luôn nhỏ hơn vật đối với mọi khoảng cách vật thật (như đã chứng minh ở Hình 34.16b). Do đó, để thu được ảnh phóng đại lớn hơn vật, bắt buộc phải sử dụng gương cầu lõm.

Đối với gương cầu lõm, ảnh chỉ cùng chiều và phóng đại khi khoảng cách từ vật (khuôn mặt bạn) đến gương nhỏ hơn tiêu cự của gương ($s < f$), tương tự như trường hợp ở Hình 34.20d. Nếu đặt mặt xa hơn tiêu cự, ảnh sẽ trở thành ảnh thật và bị lộn ngược chiều.

</details>
