## 36.7 Khẩu độ tròn và năng suất phân giải

### Hiện tượng nhiễu xạ qua khẩu độ tròn và đĩa Airy

Trong thực tế kỹ thuật, đại đa số các dụng cụ quang học như kính thiên văn, kính hiển vi, máy ảnh và mắt người đều thu nhận ánh sáng qua các lỗ mở hoặc thấu kính có dạng hình tròn thay vì các khe hẹp dài vô hạn. Do đó, hình ảnh nhiễu xạ tạo bởi một khẩu độ hình tròn đóng vai trò quyết định đối với giới hạn phân giải chi tiết của mọi hệ thống quang học.

Về nguyên tắc, ta có thể tính cường độ sáng tại một điểm bất kỳ trên màn bằng cách chia diện tích hình tròn của khẩu độ thành vô số phần tử diện tích vi phân nhỏ, xác định biên độ và pha của sóng thứ cấp từ từng phần tử gửi tới điểm quan sát, rồi lấy tích phân trên toàn bộ diện tích hình tròn. Mặc dù phép tích phân này không thể biểu diễn dưới dạng các hàm số sơ cấp (mà phải sử dụng hàm Bessel bậc một), kết quả giải tích và thực nghiệm cho thấy hình ảnh nhiễu xạ có tính đối xứng quay quanh trục quang học.

![Hình 36.25: Hình ảnh nhiễu xạ tạo bởi một khẩu độ tròn gồm đĩa sáng Airy ở trung tâm và các vành sáng tối xen kẽ.](../img/young-36/hinh-36-25.png)

Hình ảnh nhiễu xạ tạo bởi khẩu độ tròn đường kính $D$ bao gồm một đốm sáng hình tròn rất rõ ở chính giữa, được bao quanh bởi một hệ thống các vành tròn tối và sáng xen kẽ đồng tâm (Hình 36.25). Đốm sáng trung tâm này được gọi là **đĩa Airy** (Airy disk) để vinh danh nhà thiên văn học người Anh Sir George Airy (1801–1892), người đầu tiên tìm được biểu thức cường độ của hệ vân này.

Bán kính góc $\theta_1$ của đĩa Airy (tức là góc từ tâm cực đại đến vành tối thứ nhất) được xác định bởi hệ thức:

$$
\sin\theta_1 = 1{,}22 \frac{\lambda}{D}
\tag{36.17}
$$

Bán kính góc của hai vành tối tiếp theo lần lượt là:

$$
\begin{aligned}
\sin\theta_2 &= 2{,}23 \frac{\lambda}{D}\\
\sin\theta_3 &= 3{,}24 \frac{\lambda}{D}
\end{aligned}
\tag{36.18}
$$

Trong khi đó, bán kính góc của ba vành sáng cực đại phụ đầu tiên nằm bên ngoài đĩa Airy được xác định xấp xỉ bởi:

$$
\begin{aligned}
\sin\theta &\approx 1{,}63 \frac{\lambda}{D}\\
&\approx 2{,}68 \frac{\lambda}{D}\\
&\approx 3{,}70 \frac{\lambda}{D}
\end{aligned}
\tag{36.19}
$$

![Hình 36.26: Ảnh chụp hình ảnh nhiễu xạ tạo bởi một khẩu độ tròn.](../img/young-36/hinh-36-26.png)

Cường độ sáng của các vành sáng phụ bên ngoài giảm đi nhanh theo góc khi góc lệch tăng lên (Hình 36.26). Khi đường kính khẩu độ $D$ lớn hơn rất nhiều so với bước sóng $\lambda$, cường độ đỉnh của vành sáng thứ nhất chỉ bằng $1{,}7\%$ so với cường độ tại tâm đĩa Airy, và vành sáng thứ hai chỉ còn khoảng $0{,}4\%$. Khoảng $85\%$ toàn bộ năng lượng ánh sáng truyền qua khẩu độ đều tập trung bên trong đĩa Airy.

### Nhiễu xạ và sự tạo ảnh của dụng cụ quang học

Hiện tượng nhiễu xạ qua khẩu độ tròn đặt ra giới hạn vật lý cơ bản cho sự tạo ảnh bằng thấu kính và gương cầu. Trong quang hình học cổ điển, chúng ta giả định rằng một thấu kính lý tưởng có tiêu cự $f$ sẽ hội tụ chùm tia song song từ một nguồn điểm ở xa thành một điểm ảnh hình học duy nhất trên tiêu diện. Tuy nhiên, do ánh sáng bị nhiễu xạ qua vành thấu kính (đóng vai trò như một khẩu độ tròn), ảnh của một điểm sáng thực chất là một đĩa Airy với các vành đồng tâm mờ nhạt.

![Hình 36.27: Các hình ảnh này cho thấy hình ảnh nhiễu xạ tạo ra khi quan sát bốn nguồn sáng rất nhỏ ("nguồn điểm") qua một thấu kính có khẩu độ tròn đặt phía trước thấu kính. (a) Khẩu độ rất nhỏ khiến hình ảnh của các nguồn 3 và 4 chồng lấn và vừa vặn được phân giải theo tiêu chuẩn Rayleigh. Khi tăng kích thước khẩu độ, kích thước của hình ảnh nhiễu xạ giảm đi, như thể hiện trong (b) và (c).](../img/young-36/hinh-36-27.png)

Nếu có hai nguồn sáng điểm đặt gần nhau, ảnh của chúng sẽ là hai đĩa Airy nằm cạnh nhau (Hình 36.27). Khi hai nguồn đặt rất sát nhau, hai đĩa Airy sẽ chồng lấn lên nhau:
- Ở khẩu độ nhỏ (Hình 36.27a), đĩa Airy mở rộng ra khiến ảnh của hai nguồn 3 và 4 dính liền thành một đốm sáng dài duy nhất, không thể tách biệt.
- Khi tăng kích thước khẩu độ lên mức trung bình (Hình 36.27b), kích thước đĩa Airy co hẹp lại và hai điểm ảnh bắt đầu tách rời.
- Với khẩu độ lớn (Hình 36.27c), đĩa Airy rất nhỏ và hai nguồn sáng được phân giải hoàn toàn rõ rệt.

Để định lượng ranh giới phân biệt giữa hai nguồn điểm, nhà vật lý người Anh Lord Rayleigh (1842–1919) đã đưa ra một tiêu chuẩn thực nghiệm gọi là **tiêu chuẩn Rayleigh** (Rayleigh's criterion): Hai nguồn sáng điểm được coi là vừa vặn phân biệt được nếu tâm của đĩa Airy của nguồn này trùng đúng vào cực tiểu thứ nhất (vành tối đầu tiên) của đĩa Airy của nguồn kia.

Khi góc $\theta$ đủ nhỏ ($\sin\theta \approx \theta$), khoảng cách góc tối thiểu giữa hai nguồn điểm để mắt hoặc thiết bị vừa phân biệt được là:

$$
\theta_{\text{min}} \approx 1{,}22 \frac{\lambda}{D}
$$

Khoảng cách góc nhỏ nhất này được gọi là **giới hạn phân giải** (limit of resolution) của dụng cụ quang học. Giới hạn phân giải càng nhỏ thì **năng suất phân giải** (resolving power) của dụng cụ càng cao.

Nhiễu xạ đặt ra giới hạn cơ bản cho năng suất phân giải của thấu kính. Quang hình học có thể khiến chúng ta nghĩ rằng ta có thể phóng to hình ảnh tùy thích. Tuy nhiên, cuối cùng ta luôn đạt tới một điểm mà ở đó hình ảnh trở nên lớn hơn nhưng không hề tăng thêm độ chi tiết. Các hình ảnh trong Hình 36.27 sẽ không hề sắc nét hơn nếu được phóng to.

::: warning Cảnh báo: Năng suất phân giải và năng suất phân giải phổ
Đừng nhầm lẫn năng suất phân giải của một dụng cụ quang học với năng suất phân giải phổ của một cách tử (Mục 36.5). Năng suất phân giải đề cập đến khả năng phân biệt hình ảnh của các vật thể nằm gần nhau, khi quan sát qua một dụng cụ quang học hoặc trên một bức ảnh chụp bởi dụng cụ đó. Năng suất phân giải phổ mô tả khả năng phân biệt các bước sóng khác nhau trong một quang phổ tạo bởi cách tử nhiễu xạ.
:::

Phương trình (36.17) và tiêu chuẩn Rayleigh chỉ rõ hai con đường kỹ thuật để nâng cao năng suất phân giải:
1. **Tăng đường kính khẩu độ $D$**: Chế tạo các vật kính thiên văn hoặc hệ gương có đường kính khổng lồ (chẳng hạn các kính thiên văn không gian hoặc kính mặt đất đường kính hàng chục mét).
2. **Giảm bước sóng $\lambda$**: Sử dụng ánh sáng tử ngoại hoặc chùm electron. Trong kính hiển vi tử ngoại, năng suất phân giải cao hơn so với kính hiển vi ánh sáng nhìn thấy. Trong kính hiển vi điện tử, năng suất phân giải bị giới hạn bởi bước sóng gắn liền với electron (sẽ được thảo luận kỹ hơn ở Chương 39). Các bước sóng này có thể nhỏ hơn bước sóng ánh sáng nhìn thấy tới $100.000\text{ lần}$, mang lại sự gia tăng tương ứng về năng suất phân giải.

Năng suất phân giải cũng giải thích sự khác biệt về dung lượng lưu trữ giữa đĩa DVD (ra đời năm 1995) và đĩa Blu-ray (ra đời năm 2003). Thông tin được lưu trữ trên cả hai loại đĩa này dưới dạng một chuỗi các hốc siêu nhỏ. Để không làm mất thông tin trong quá trình quét, hệ quang học quét phải phân giải được hai hốc liền kề để chúng không bị hòa lẫn thành một hốc duy nhất (xem các nguồn 3 và 4 trong Hình 36.27). Tia laser quét màu xanh lam sử dụng trong đầu đọc Blu-ray có bước sóng ngắn hơn ($405\text{ nm}$), do đó có năng suất phân giải tốt hơn so với laser màu đỏ $650\text{ nm}$ trong đầu đĩa DVD. Vì vậy, các hốc trên đĩa Blu-ray có thể được bố trí sát nhau hơn so với đĩa DVD, và nhiều thông tin hơn có thể được lưu trữ trên một đĩa cùng kích thước vật lý ($50\text{ GB}$ trên đĩa Blu-ray so với $4{,}7\text{ GB}$ trên đĩa DVD).

::: tip Ứng dụng: Kính thiên văn càng lớn, độ phân giải càng cao
![Ứng dụng: Các ăng-ten của VLA phối hợp thu tín hiệu để tăng kích thước hiệu dụng của hệ quan sát.](../img/young-36/ung-dung-36-vla.png)

Khẩu độ đường kính lớn của kính thiên văn giúp hạn chế tối đa ảnh hưởng bất lợi của hiện tượng nhiễu xạ. Đường kính hiệu dụng của một hệ thống có thể tăng lên đáng kể bằng cách kết hợp nhiều kính thiên văn nhỏ thành một mảng giao thoa kế. Điển hình là Hệ thống kính thiên văn cực lớn (Very Large Array - VLA) tại New Mexico, bao gồm 27 kính thiên văn vô tuyến đường kính $25\text{ m}$ bố trí theo hình chữ Y có sải rộng lên tới $36\text{ km}$. Nhờ đường kính hiệu dụng $D = 36\text{ km}$, mảng VLA đạt giới hạn phân giải nhỏ $5 \times 10^{-8}\text{ rad}$ ở bước sóng vô tuyến $1{,}5\text{ cm}$. Nếu mắt người có được năng suất phân giải này, chúng ta có thể đọc được dòng chữ kiểm tra thị lực chuẩn trên bảng đo mắt từ khoảng cách xa hơn $30\text{ km}$.
:::

::: info Ví dụ 36.6: Năng suất phân giải của ống kính máy ảnh
Một ống kính máy ảnh có tiêu cự $f = 50\text{ mm}$ và khẩu độ mở tối đa là $f/2$ được dùng để chụp ảnh một vật thể cách thấu kính $s = 9{,}0\text{ m}$.

a) Nếu năng suất phân giải bị giới hạn bởi hiện tượng nhiễu xạ, khoảng cách nhỏ nhất giữa hai điểm trên vật thể để ảnh của chúng vừa vặn phân biệt được là bao nhiêu? Khoảng cách tương ứng giữa hai điểm ảnh trên cảm biến là bao nhiêu?

b) Tình hình sẽ thay đổi như thế nào nếu ống kính được khép khẩu xuống $f/16$? Trong cả hai trường hợp, sử dụng bước sóng ánh sáng $\lambda = 500\text{ nm}$.

**Nhận dạng bài toán**: Bài toán kết hợp các khái niệm về năng suất phân giải theo tiêu chuẩn Rayleigh, sự tạo ảnh qua thấu kính mỏng và chỉ số độ mở khẩu độ ($f\text{-number}$).

**Chuẩn bị**: Theo định nghĩa chỉ số khẩu độ, đường kính khẩu độ $D$ bằng tiêu cự $f$ chia cho chỉ số khẩu độ:

$$
D = \frac{f}{f\text{-number}}
$$

Góc phân giải tối thiểu $\theta$ được tính theo tiêu chuẩn Rayleigh từ Phương trình (36.17). Từ công thức thấu kính mỏng, khoảng cách góc của hai điểm vật và hai điểm ảnh đối với quang tâm thấu kính là bằng nhau: $y / s = y' / s'$. Vì khoảng cách vật $s = 9{,}0\text{ m}$ lớn hơn rất nhiều so với tiêu cự $f = 50\text{ mm}$, khoảng cách ảnh $s'$ xấp xỉ bằng tiêu cự $f$.

**Thực hiện**:

a) Với khẩu độ tối đa $f/2$, đường kính lỗ mở khẩu độ là:

$$
\begin{aligned}
D &= \frac{50\text{ mm}}{2}\\
&= 25\text{ mm}\\
&= 25 \times 10^{-3}\text{ m}
\end{aligned}
$$

Áp dụng tiêu chuẩn Rayleigh:

$$
\begin{aligned}
\theta &\approx 1{,}22 \frac{\lambda}{D}\\
&= \frac{1{,}22(500 \times 10^{-9}\text{ m})}{25 \times 10^{-3}\text{ m}}\\
&= 2{,}44 \times 10^{-5}\text{ rad}\\
&\approx 2{,}4 \times 10^{-5}\text{ rad}
\end{aligned}
$$

Khoảng cách nhỏ nhất giữa hai điểm trên vật thể đặt cách $s = 9{,}0\text{ m}$ là:

$$
\begin{aligned}
y &= s\theta\\
&= (9{,}0\text{ m})(2{,}4 \times 10^{-5})\\
&= 2{,}16 \times 10^{-4}\text{ m}\\
&\approx 0{,}22\text{ mm}
\end{aligned}
$$

Khoảng cách tương ứng giữa hai điểm ảnh trên mặt phẳng cảm biến ảnh là:

$$
\begin{aligned}
y' &= f\theta\\
&= 50\text{ mm} \times 2{,}4 \times 10^{-5}\\
&= 1{,}2 \times 10^{-3}\text{ mm}\\
&= 0{,}0012\text{ mm}\\
&\approx \frac{1}{800}\text{ mm}
\end{aligned}
$$

b) Khi khép khẩu xuống $f/16$, đường kính khẩu độ mới là $D' = 50\text{ mm} / 16$, nhỏ hơn 8 lần so với trường hợp a. Do đó, góc phân giải tối thiểu tăng lên gấp 8 lần, kéo theo khoảng cách giữa hai điểm vừa phân biệt được trên vật thể và trên cảm biến cũng tăng lên gấp 8 lần:

$$
\begin{aligned}
y &= 8(0{,}22\text{ mm})\\
&\approx 1{,}8\text{ mm}
\end{aligned}
$$

$$
\begin{aligned}
y' &= 8(0{,}0012\text{ mm})\\
&= 0{,}0096\text{ mm}\\
&\approx \frac{1}{100}\text{ mm}
\end{aligned}
$$

Chỉ những ống kính máy ảnh tốt nhất mới có thể tiệm cận năng suất phân giải này.

**Đánh giá**: Trong thực tế nhiếp ảnh, người ta thường muốn khép khẩu nhỏ để giảm bớt hiện tượng quang sai cầu và mở rộng độ sâu trường ảnh (depth of field). Tuy nhiên, khi khẩu độ quá nhỏ (như $f/16$ hay $f/22$), hiệu ứng nhiễu xạ qua lỗ mở lại trở nên vượt trội, khiến các điểm ảnh bị nhòe thành các đĩa Airy lớn. Do đó, người chụp ảnh luôn phải cân bằng hài hòa giữa độ sâu trường ảnh và giới hạn nhiễu xạ để đạt được độ nét quang học tối ưu.

**Khái niệm cốt lõi**: Sự nhiễu xạ của sóng ánh sáng khi đi qua khẩu độ tròn của thấu kính làm biến các điểm ảnh thành các đĩa Airy có kích thước hữu hạn. Hiện tượng này thiết lập một giới hạn tự nhiên không thể vượt qua đối với khả năng phân giải của mọi hệ thấu kính quang học.
:::

::: tip Ứng dụng sinh học: Đĩa Airy trong mắt chim đại bàng
![Ứng dụng: Đồng tử lớn và các tế bào cảm quang của mắt đại bàng phối hợp tạo thị giác phân giải cao.](../img/young-36/ung-dung-36-dai-bang.png)

Hiện tượng nhiễu xạ qua lỗ đồng tử đặt ra giới hạn cho độ phân giải của thị giác. Ở mắt người, đường kính đồng tử tối đa $D$ vào khoảng $5\text{ mm}$. Trong khi ở mắt chim đại bàng, đường kính đồng tử $D$ lên tới khoảng $9\text{ mm}$. Theo Phương trình (36.17), đồng tử lớn giúp đại bàng có năng suất phân giải cao hơn hẳn mắt người: Một nguồn sáng điểm ở xa chỉ tạo ra một đĩa Airy trên võng mạc đại bàng với kích thước góc bằng khoảng $5/9$ kích thước đĩa Airy trên võng mạc người. (Nếu mắt chúng ta tạo ra một hình ảnh như Hình 36.27b, mắt đại bàng sẽ tạo ra một hình ảnh như Hình 36.27c.) Đồng thời, để tận dụng triệt để độ phân giải cao này, các tế bào nón cảm quang trên võng mạc đại bàng có kích thước nhỏ hơn và mật độ sắp xếp dày đặc hơn rất nhiều so với mắt người, để ghi nhận các chi tiết nhỏ của ảnh có độ phân giải cao ấy.
:::

### Câu hỏi tự kiểm tra 36.7

Hãy xếp hạng bốn đề xuất thiết kế kính thiên văn đặt trên quỹ đạo không gian (loại bỏ hoàn toàn ảnh hưởng gây mờ của khí quyển Trái Đất) theo khả năng phân giải chi tiết nhỏ, từ tốt nhất đến kém nhất:
- (i) Một kính thiên văn vô tuyến đường kính $100\text{ m}$ quan sát ở bước sóng $\lambda = 21\text{ cm}$.
- (ii) Một kính thiên văn quang học đường kính $2{,}0\text{ m}$ quan sát ở bước sóng $\lambda = 500\text{ nm}$.
- (iii) Một kính thiên văn tử ngoại đường kính $1{,}0\text{ m}$ quan sát ở bước sóng $\lambda = 100\text{ nm}$.
- (iv) Một kính thiên văn hồng ngoại đường kính $2{,}0\text{ m}$ quan sát ở bước sóng $\lambda = 10\ \mu\text{m}$.

::: details Trả lời
Thứ tự xếp hạng từ tốt nhất đến kém nhất là (iii), (ii), (iv), (i).

Theo tiêu chuẩn Rayleigh kết hợp với Phương trình (36.17), tỷ số $\lambda / D$ càng nhỏ thì giới hạn góc phân giải $\theta$ càng bé, đồng nghĩa với khả năng phân giải chi tiết nhỏ của kính thiên văn càng tốt.

Ta tính tỷ số $\lambda / D$ cho từng đề xuất:
Phương án (i):

$$
\begin{aligned}
\frac{\lambda}{D} &= \frac{0{,}21\text{ m}}{100\text{ m}}\\
&= 2{,}1 \times 10^{-3}
\end{aligned}
$$
Phương án (ii):

$$
\begin{aligned}
\frac{\lambda}{D} &= \frac{5{,}0 \times 10^{-7}\text{ m}}{2{,}0\text{ m}}\\
&= 2{,}5 \times 10^{-7}
\end{aligned}
$$
Phương án (iii):

$$
\begin{aligned}
\frac{\lambda}{D} &= \frac{1{,}0 \times 10^{-7}\text{ m}}{1{,}0\text{ m}}\\
&= 1{,}0 \times 10^{-7}
\end{aligned}
$$
Phương án (iv):

$$
\begin{aligned}
\frac{\lambda}{D} &= \frac{1{,}0 \times 10^{-5}\text{ m}}{2{,}0\text{ m}}\\
&= 5{,}0 \times 10^{-6}
\end{aligned}
$$

So sánh độ lớn của tỷ số $\lambda / D$:

$$
\begin{aligned}
1{,}0 \times 10^{-7} &< 2{,}5 \times 10^{-7}\\
&< 5{,}0 \times 10^{-6}\\
&< 2{,}1 \times 10^{-3}
\end{aligned}
$$

Do đó, khả năng phân giải chi tiết nhỏ tốt nhất thuộc về kính tử ngoại (iii), tiếp theo là kính quang học (ii), sau đó là kính hồng ngoại (iv), và kém nhất là kính vô tuyến (i).
:::
