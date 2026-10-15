## 34.5. Máy ảnh

Khái niệm ảnh đóng vai trò nền tảng trong quang hình học, giúp phân tích và thiết kế hàng loạt dụng cụ quang học quen thuộc trong khoa học và đời sống thường ngày, từ máy ảnh, mắt người, kính lúp cho đến kính hiển vi và kính thiên văn. Trong số đó, máy ảnh là một hệ quang học tạo ảnh thật trực tiếp lên bề mặt ghi nhận tín hiệu.

### Các bộ phận quang học cơ bản của máy ảnh

Hình 34.40 phác họa các bộ phận cấu tạo chủ yếu của một máy ảnh kỹ thuật số hiện đại.

![Các bộ phận cơ bản của một máy ảnh kỹ thuật số. Thấu kính tạo ảnh thật, ngược chiều và thu nhỏ trên cảm biến, trong khi màn trập và khẩu độ điều tiết lượng sáng phơi sáng.](../img/young-34/hinh-34-40.png)

Máy ảnh gồm một hộp kín ánh sáng, thấu kính hội tụ, màn trập và môi trường ghi nhận nhạy sáng (Hình 34.40). Màn trập mở cho ánh sáng đi qua trong khoảng thời gian định trước. Từ Latin “camera” có nghĩa là một căn phòng hoặc không gian khép kín. Trong máy ảnh kỹ thuật số (bao gồm cả máy ảnh điện thoại di động), đây là một cảm biến điện tử. Trong các máy ảnh trước đây, bộ phận này là phim chụp ảnh.

Hệ thống quang học của máy ảnh gồm các khối chức năng chính:
- **Vật kính (thấu kính máy ảnh)**: Là một tổ hợp gồm nhiều thấu kính đơn ghép nối tiếp nhau nhằm triệt tiêu tối đa các hiện tượng quang sai cầu và quang sai sắc. Hệ thấu kính này đóng vai trò như một thấu kính hội tụ tương đương, nhận ánh sáng từ vật và tạo ra một ảnh thật, ngược chiều và thông thường có kích thước thu nhỏ trên môi trường ghi nhận.
- **Môi trường ghi nhận (cảm biến điện tử hoặc phim)**: Trong máy ảnh kỹ thuật số, môi trường ghi nhận là một cảm biến điện tử. Trong các máy ảnh truyền thống, môi trường này là phim chụp ảnh. Thấu kính tạo ra một ảnh thật, ngược chiều của vật thể đang được chụp trên môi trường ghi nhận.
- **Màn trập (shutter)**: Màn trập kiểm soát khoảng thời gian ánh sáng đi vào thấu kính. Khoảng thời gian này thường điều chỉnh được theo các nấc tương ứng với các thừa số khoảng 2, thường từ $1\text{ s}$ đến $1/1000\text{ s}$.
- **Màn chắn khẩu độ (aperture-control diaphragm)**: Một cụm lá khẩu kim loại có thể xếp mở linh hoạt, tạo thành một lỗ tròn mở ở tâm với đường kính thay đổi được. Màn chắn này giới hạn lượng chùm tia đi qua vật kính tới cảm biến.
- **Cơ chế lấy nét (focusing)**: Để ảnh của vật hiện rõ nét trên bề mặt cảm biến, mặt phẳng ảnh phải trùng khớp chính xác với mặt phẳng cảm biến. Từ công thức thấu kính mỏng:

$$
\frac{1}{s} + \frac{1}{s'} = \frac{1}{f}
$$

Khi vật ở rất xa ($s \to \infty$), khoảng cách ảnh bằng đúng tiêu cự ($s' = f$). Khi vật dịch chuyển lại gần máy ảnh hơn ($s$ giảm), khoảng cách ảnh $s'$ bắt buộc phải tăng lên. Vì khoảng cách từ thấu kính đến cảm biến không cố định sẵn cho mọi tình huống, người chụp hoặc động cơ lấy nét tự động phải dịch chuyển vật kính ra xa cảm biến hơn khi chụp vật ở gần, và đưa vật kính lại gần cảm biến hơn khi chụp vật ở xa.

::: info Ứng dụng: Đảo ngược một ảnh đã đảo ngược
Thấu kính máy ảnh tạo một ảnh ngược trên bộ cảm biến điện tử nhạy sáng của máy ảnh. Phần mềm bên trong máy ảnh sau đó sẽ đảo ngược ảnh một lần nữa để ảnh xuất hiện đúng chiều trên màn hình hiển thị của máy ảnh. Một điều tương tự cũng diễn ra với thị giác của bạn: Ảnh tạo trên võng mạc của mắt là ảnh ngược, nhưng "phần mềm" của não bộ sẽ dựng thẳng ảnh lại để bạn nhìn thấy thế giới theo chiều thuận.
:::

### Ống kính máy ảnh: Tiêu cự và góc trông

Việc lựa chọn tiêu cự $f$ cho ống kính máy ảnh phụ thuộc trực tiếp vào kích thước vật lý của cảm biến ảnh và góc trông (trường nhìn) mong muốn đối với khung cảnh chụp.

![Ba bức ảnh chụp từ cùng một vị trí với các ống kính có tiêu cự khác nhau: 28 mm (góc rộng), 70 mm (tiêu cự trung bình) và 135 mm (tele). Tiêu cự càng dài thì kích thước ảnh càng lớn và góc trông càng hẹp.](../img/young-34/hinh-34-41.png)

![Hình 34.41d: Góc trông ứng với ba tiêu cự trên cùng bề rộng phim 36mm. Tiêu cự dài hơn cho góc trông hẹp hơn.](../img/young-34/hinh-34-41-d.png)

Hình 34.41 minh họa ba bức ảnh chụp trên phim 35 mm (kích thước vùng ảnh $24\text{ mm} \times 36\text{ mm}$) từ cùng một vị trí với cùng một máy ảnh nhưng sử dụng các ống kính có tiêu cự khác nhau:
- **Ống kính tiêu cự ngắn (ống kính góc rộng)**: Chẳng hạn $f = 28\text{ mm}$ (Hình 34.41a). Do tỷ số $s'/s$ nhỏ nên vật ở xa chỉ tạo một ảnh nhỏ, nhưng góc trông mở rộng lên tới $65^\circ$ theo chiều rộng 36 mm của phim.
- **Ống kính tiêu cự trung bình**: Chẳng hạn $f = 70\text{ mm}$ (Hình 34.41b), đem lại góc trông $29^\circ$, cho kích thước ảnh vừa phải cân đối giữa toàn cảnh và chi tiết.
- **Ống kính tiêu cự dài (ống kính tele)**: Chẳng hạn $f = 135\text{ mm}$ (Hình 34.41c). Khi sử dụng ống kính có tiêu cự dài, khoảng cách ảnh $s'$ lớn hơn, kéo theo độ lớn độ phóng đại ngang $|m| = s'/s$ tăng lên. Ảnh của cùng một vật thể có thể choán trọn diện tích của cảm biến hoặc khung phim, đem lại góc trông hẹp chỉ $15^\circ$ (Hình 34.41d).

### Khẩu độ và chỉ số f

Khả năng thu nhận ánh sáng của một ống kính máy ảnh được biểu diễn qua tỷ số giữa tiêu cự $f$ và đường kính hiệu dụng $D$ của lỗ mở màn chắn, gọi là **chỉ số f** (ký hiệu là $N$ hay f-number) của ống kính:

$$
N = \frac{f}{D} \tag{34.20}
$$

Chẳng hạn: Một ống kính có tiêu cự $f = 50\text{ mm}$ và đường kính khẩu độ $D = 25\text{ mm}$ có chỉ số f là $N = 50 / 25 = 2$, và được ký hiệu là khẩu độ $f/2$. Ký hiệu này vừa nêu rõ chỉ số f vừa biểu thị đường kính mở bằng $D = f / 2$.

Cường độ sáng (năng lượng ánh sáng trên một đơn vị diện tích trong một đơn vị thời gian) hội tụ lên bề mặt cảm biến tỷ lệ thuận với diện tích thu sáng của lỗ mở, tức tỷ lệ với $D^2$. Đồng thời, kích thước ngang và kích thước dọc của ảnh đều tỷ lệ thuận với khoảng cách ảnh $s'$, và đối với vật ở xa thì $s' \approx f$. Do đó, diện tích mà năng lượng ánh sáng phân bố lên trên cảm biến tỷ lệ với $f^2$. Kết hợp hai yếu tố này, cường độ sáng $I$ trên cảm biến tỷ lệ với đại lượng $(D/f)^2$, tức tỷ lệ nghịch với bình phương của chỉ số f $N$:

$$
I &\propto \frac{D^2}{f^2} = \frac{1}{N^2}
$$

![Ống kính máy ảnh với màn chắn khẩu độ điều chỉnh được. Chỉ số f càng lớn thì khẩu độ mở càng nhỏ.](../img/young-34/hinh-34-42.png)

Đối với một ống kính có màn chắn thay đổi được, nếu ta tăng đường kính $D$ lên $\sqrt{2}$ lần thì chỉ số f $N$ sẽ giảm đi $\sqrt{2}$ lần, làm diện tích lỗ mở tăng gấp đôi và cường độ sáng tới cảm biến tăng gấp đôi. Do đó, các nấc chỉ số f trên vành ống kính (thường gọi là các nấc f-stop) được quy chuẩn theo một chuỗi cấp số nhân với công bội danh định $\sqrt{2} \approx 1{,}414$:

$$
f/1{,}4 \quad f/2 \quad f/2{,}8 f/4 \quad f/5{,}6 \quad f/8 f/11 \quad f/16 \quad f/22
$$

Chỉ số f càng lớn thì khẩu độ mở càng nhỏ, dẫn đến ánh sáng tới cảm biến càng yếu (Hình 34.42). Mỗi nấc dịch chuyển sang phải làm giảm cường độ sáng đi một nửa, trong khi mỗi nấc dịch chuyển sang trái làm tăng cường độ sáng lên gấp đôi.

Tổng lượng phơi sáng $H$ (quang lượng trên một đơn vị diện tích bề mặt cảm biến) tỷ lệ thuận với cả diện tích khẩu độ và khoảng thời gian mở màn trập $\Delta t$:

$$
H &\propto I \Delta t \propto \frac{\Delta t}{N^2}
$$

Vì các giá trị f-stop chuẩn như $5{,}6$ là số làm tròn danh định của $4\sqrt{2} \approx 5{,}657$, các cặp cài đặt $(f/4, 1/500\text{ s})$, $(f/5{,}6, 1/250\text{ s})$ và $(f/8, 1/125\text{ s})$ tương đương nhau về mặt danh định (xấp xỉ gần đúng) về độ phơi sáng trên cảm biến.

### Ống kính zoom và máy chiếu

Ống kính zoom là hệ quang học gồm một tổ hợp phức tạp nhiều thấu kính thành phần có khả năng thay đổi tiêu cự liên tục, thường có dải biến thiên tiêu cự lớn lên tới $15:1$.

![Nguyên lý hoạt động của ống kính zoom gồm hai thấu kính: Phần (a) tiêu cự dài khi hai kính gần nhau, phần (b) tiêu cự ngắn khi hai kính xa nhau, phần (c) là ống kính zoom thực tế gồm 12 thấu kính thành phần chia thành 4 nhóm.](../img/young-34/hinh-34-43.png)

Hình 34.43 mô tả sơ đồ nguyên lý của một ống kính zoom gồm hai thấu kính: Một thấu kính hội tụ và một thấu kính phân kỳ:
- Khi hai thấu kính được đặt sát gần nhau (Hình 34.43a), chùm tia hội tụ từ thấu kính thứ nhất bị thấu kính thứ hai làm lệch phân kỳ nhẹ, làm giao điểm của chùm tia bị đẩy ra xa hơn. Hệ quang học tương đương có tiêu cự dài, mang đặc tính của ống kính tele.
- Khi hai thấu kính dịch chuyển tách xa nhau (Hình 34.43b), chùm tia hội tụ hẹp hơn đi vào thấu kính phân kỳ tại vị trí gần trục chính hơn, tiêu diện tương đương dịch chuyển lại gần hệ hơn. Tiêu cự tương đương của hệ ngắn lại, đưa ống kính về chế độ góc rộng.

Trong thiết kế quang học, việc giữ cho ảnh luôn hội tụ sắc nét và duy trì chỉ số f không đổi khi tiêu cự thay đổi là một bài toán phức tạp. Khi thay đổi tiêu cự của một ống kính zoom điển hình, hai nhóm thấu kính thành phần dịch chuyển đồng thời bên trong ống kính và màn chắn khẩu độ tự động đóng mở tương ứng (Hình 34.43c).

Máy chiếu kỹ thuật số dùng để trình chiếu bài giảng, hình ảnh hoặc phim ảnh hoạt động theo nguyên lý hoàn toàn tương tự như một máy ảnh chạy theo chiều ngược lại. Trong loại máy chiếu kỹ thuật số phổ biến nhất, các điểm ảnh dữ liệu cần chiếu được hiển thị trên một màn hình tinh thể lỏng (LCD) nhỏ, trong suốt nằm bên trong máy chiếu và ở phía sau thấu kính chiếu. Một ngọn đèn chiếu sáng màn hình LCD này, và màn hình LCD đóng vai trò như vật đối với thấu kính. Thấu kính tạo ra một ảnh thật, phóng đại và ngược chiều của màn hình LCD trên màn chiếu ở xa. Vì ảnh tạo ra bị lộn ngược, các điểm ảnh hiển thị trên màn hình LCD được bố trí lộn ngược từ trước để hình ảnh xuất hiện trên màn chiếu luôn đúng chiều.

---

### Ví dụ 34.12: Thời gian phơi sáng trong nhiếp ảnh

Một ống kính tele thông dụng dùng cho máy ảnh phim 35 mm có tiêu cự $f = 200\text{ mm}$, với dải khẩu độ mở từ $f/2{,}8$ đến $f/22$.
- (a) Xác định dải đường kính lỗ mở khẩu độ tương ứng của ống kính.
- (b) Xác định dải cường độ sáng của ảnh tạo trên mặt phẳng phim.

#### Nhận dạng bài toán
- Phần (a) liên hệ giữa tiêu cự $f$, đường kính khẩu độ $D$ và chỉ số f thông qua định nghĩa ở phương trình (34.20).
- Phần (b) dựa trên mối quan hệ giữa cường độ sáng của ảnh trên phim với đường kính khẩu độ và tiêu cự.

#### Chuẩn bị
- Đề bài cho tiêu cự $f = 200\text{ mm}$ cố định.
- Chỉ số f biến thiên từ giá trị cực tiểu $N_1 = 2{,}8$ đến giá trị cực đại $N_2 = 22$.
- Sử dụng phương trình (34.20) để tính đường kính $D = f / (N)$. Vì tiêu cự không đổi, cường độ sáng $I$ tỷ lệ thuận với $D^2$, hay tỷ lệ nghịch với bình phương chỉ số f.

#### Thực hiện
- (a) Áp dụng trực tiếp phương trình (34.20), đường kính khẩu độ tại nấc mở lớn nhất $f/2{,}8$ là:

$$
\begin{aligned}
D_{\max} &= \frac{f}{N} \\
&= \frac{200\text{ mm}}{2{,}8} \\
&= 71\text{ mm}
\end{aligned}
$$

Tại nấc khép khẩu nhỏ nhất $f/22$, đường kính lỗ mở khẩu độ là:

$$
\begin{aligned}
D_{\min} &= \frac{f}{N} \\
&= \frac{200\text{ mm}}{22} \\
&= 9{,}1\text{ mm}
\end{aligned}
$$

- (b) Do cường độ sáng $I$ tỷ lệ thuận với $D^2$, tỷ số giữa cường độ sáng tại khẩu độ $f/2{,}8$ và cường độ sáng tại khẩu độ $f/22$ bằng:

$$
\begin{aligned}
\frac{I_{f/2{,}8}}{I_{f/22}} &= \left(\frac{D_{\max}}{D_{\min}}\right)^2 \\
&= \left(\frac{71\text{ mm}}{9{,}1\text{ mm}}\right)^2 \\
&\approx \left(\frac{22}{2{,}8}\right)^2 \\
&\approx 62
\end{aligned}
$$

Giá trị này xấp xỉ bằng $2^6 = 64$, tương ứng với bước nhảy qua 6 nấc f-stop tiêu chuẩn trên vành ống kính.

#### Đánh giá
Nếu thời gian phơi sáng tại khẩu độ $f/2{,}8$ là $1/1000\text{ s}$, thì để bù lại sự suy giảm cường độ sáng, thời gian phơi sáng tại $f/22$ được tính bằng cách nhân trực tiếp tỷ số cường độ sáng nguyên vẹn trước khi làm tròn:

$$
\begin{aligned}
\Delta t_{f/22} &\approx \left(\frac{22}{2{,}8}\right)^2 \times \frac{1}{1000}\text{ s} \\
&\approx 0{,}062\text{ s} \\
&\approx \frac{1}{16}\text{ s}
\end{aligned}
$$

Quy tắc chung là: Khẩu độ càng nhỏ (chỉ số f càng lớn) thì thời gian phơi sáng yêu cầu càng dài. Mặc dù cần thời gian phơi sáng dài hơn, nhiều nhiếp ảnh gia vẫn chủ động khép khẩu nhỏ. Thao tác này buộc chùm sáng chỉ đi qua vùng trung tâm gần trục của thấu kính, loại bỏ các tia biên để giảm thiểu tối đa hiện tượng quang sai cầu, mang lại độ sắc nét cao nhất cho bức ảnh.

::: tip Khái niệm cốt lõi
Chỉ số f của ống kính máy ảnh là tỷ số giữa tiêu cự và đường kính lỗ mở khẩu độ. Chỉ số f càng lớn thì cường độ sáng của ảnh trên cảm biến càng yếu và thời gian phơi sáng cần thiết để ghi nhận bức ảnh càng kéo dài.
:::

---

### Câu hỏi tự kiểm tra 34.5
Khi sử dụng với phim 35 mm (kích thước vùng nhận ảnh $24\text{ mm} \times 36\text{ mm}$), một ống kính có tiêu cự $f = 50\text{ mm}$ cho góc trông $45^\circ$ và được gọi là một ống kính tiêu chuẩn. Nếu ống kính này được gắn sang một máy ảnh kỹ thuật số có cảm biến kích thước nhỏ $5\text{ mm} \times 5\text{ mm}$, thì đối với máy ảnh kỹ thuật số này, ống kính đóng vai trò là:
- (i) Ống kính góc rộng.
- (ii) Ống kính tiêu chuẩn.
- (iii) Ống kính tele.

::: details Lời giải & Đáp án
**Đáp án đúng**: Phương án (iii).

**Giải thích**: Tiêu cự $f = 50\text{ mm}$ của ống kính là đặc tính vật lý không đổi, do đó kích thước thực tế của ảnh tạo bởi một vật xác định là như nhau trong cả hai trường hợp. Tuy nhiên, diện tích cảm quang của cảm biến nhỏ hơn rất nhiều so với khung phim 35 mm, nên bề mặt cảm biến chỉ hứng được một phần nhỏ ở trung tâm chùm ảnh. Kết quả là góc trông bị thu hẹp đáng kể, khiến khung cảnh ghi nhận được tương đương với góc nhìn của một ống kính tele trên máy ảnh phim 35 mm.
:::
