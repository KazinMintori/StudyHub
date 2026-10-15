## 30.2. Tự cảm và cuộn cảm

Ở mục trước, ta đã khảo sát hiện tượng hỗ cảm giữa hai mạch điện độc lập đặt gần nhau. Một hiệu ứng có liên hệ mật thiết xuất hiện ngay trong một mạch điện đơn lẻ cô lập.

Khi có dòng điện chạy trong một mạch, dòng điện này tạo ra một từ trường trong không gian bao quanh. Các đường sức từ trường này móc vòng qua chính diện tích giới hạn bởi mạch điện đó, tạo nên một từ thông gửi qua chính mạch. Nếu cường độ dòng điện trong mạch biến thiên theo thời gian, từ thông do chính nó sinh ra cũng biến đổi tương ứng. Theo định luật Faraday, sự biến thiên từ thông này sẽ gây ra một suất điện động cảm ứng ngay trong mạch. Hiện tượng này được gọi là **hiện tượng tự cảm (self-inductance)**, và suất điện động sinh ra được gọi là **suất điện động tự cảm**. Theo định luật Lenz, suất điện động tự cảm luôn có chiều chống lại sự biến thiên của dòng điện đã sinh ra nó.

![Hình 30.4: Dòng điện i trong cuộn dây tạo ra từ trường và từ thông qua chính cuộn dây đó.](../img/young-30/hinh-30-04.png)

### Định nghĩa độ tự cảm

Xét một mạch điện kín gồm một cuộn dây có $N$ vòng dây mang dòng điện $i$ như minh họa ở Hình 30.4. Dòng điện này tạo ra một từ trường, và từ trường này gửi qua mỗi vòng dây một từ thông $\Phi_B$. Tương tự như định nghĩa hệ số hỗ cảm ở phương trình (30.5), ta định nghĩa **độ tự cảm** $L$ của mạch điện là tỉ số giữa từ thông móc vòng và cường độ dòng điện:

$$
L = \frac{N\Phi_B}{i} \tag{30.6}
$$

Khi không nhầm lẫn với hỗ cảm $M$, đại lượng $L$ cũng được gọi là điện cảm của cuộn dây. Đơn vị của tự cảm giống đơn vị hỗ cảm, tức henry ($\text{H}$):

$$
\begin{aligned}
1\text{ H} &= 1\text{ Wb/A} \\
&= 1\text{ V}\cdot\text{s/A} \\
&= 1\ \Omega\cdot\text{s} \\
&= 1\text{ J/A}^2
\end{aligned}
$$

Từ phương trình (30.6), ta viết lại từ thông móc vòng dưới dạng $N\Phi_B = Li$. Khi hình học cố định và môi trường tuyến tính có độ từ thẩm không đổi, $L$ là hằng số. Lấy đạo hàm hai vế theo thời gian $t$, ta được:

$$
N \frac{d\Phi_B}{dt} = L \frac{di}{dt}
$$

Theo định luật cảm ứng Faraday, suất điện động tự cảm $\mathcal{E}$ xuất hiện trong cuộn dây có biểu thức:

$$
\mathcal{E} = -N \frac{d\Phi_B}{dt}
$$

Kết hợp hai hệ thức trên, ta thu được phương trình cơ bản của suất điện động tự cảm:

$$
\mathcal{E} = -L \frac{di}{dt} \tag{30.7}
$$

Dấu âm trong phương trình (30.7) là sự thể hiện trực tiếp của định luật Lenz:

- Khi dòng điện $i$ đang tăng ($di/dt > 0$), suất điện động tự cảm có giá trị âm, tức là có chiều ngược chiều dòng điện để cản trở sự tăng của dòng.
- Khi dòng điện $i$ đang giảm ($di/dt < 0$), suất điện động tự cảm có giá trị dương, tức là có chiều cùng chiều với dòng điện để cố gắng duy trì dòng điện đó.
- Khi dòng điện không đổi theo thời gian ($di/dt = 0$), suất điện động tự cảm hoàn toàn triệt tiêu ($\mathcal{E} = 0$), dù cường độ dòng điện có thể rất lớn.

Phương trình (30.7) cũng cho thấy một cách hiểu thực nghiệm về độ tự cảm: Độ tự cảm $L$ của một mạch điện chính là tỉ số giữa độ lớn của suất điện động tự cảm sinh ra trong mạch và tốc độ biến thiên dòng điện trong mạch đó, tức là $L = |\mathcal{E}| / |di/dt|$. Ta có thể đo độ tự cảm $L$ trong phòng thí nghiệm bằng cách làm biến đổi dòng điện qua cuộn dây với tốc độ đã biết và đo suất điện động xuất hiện giữa hai đầu cuộn dây.

### Cuộn cảm trong mạch điện

Một linh kiện mạch điện được thiết kế chuyên dụng để có một độ tự cảm xác định được gọi là **cuộn cảm (inductor)**. Trong kỹ thuật vô tuyến và điện tử truyền thống, cuộn cảm còn được gọi là cuộn chặn (choke). Trên sơ đồ mạch điện, cuộn cảm thường được biểu diễn bằng ký hiệu các vòng dây xoắn nối tiếp.

Tác dụng vật lý cốt lõi của cuộn cảm là chống lại sự biến thiên đột ngột của dòng điện, chứ không phải chống lại bản thân dòng điện. Trong cơ học, khối lượng của vật chống lại sự thay đổi vận tốc theo định luật quán tính. Tương tự như vậy trong mạch điện, độ tự cảm của cuộn dây đóng vai trò như một dạng quán tính điện từ chống lại sự thay đổi của dòng điện.

Trong mạch một chiều, cuộn cảm giúp dòng giữ ổn định khi suất điện động đặt vào dao động. Trong mạch xoay chiều, cuộn cảm hạn chế những biến thiên dòng nhanh hơn mức mong muốn.

Độ tự cảm của một cuộn dây phụ thuộc vào kích thước hình học, hình dạng không gian, số vòng dây và vật liệu lấp đầy bên trong lõi cuộn dây. Đối với một cuộn dây có các vòng quấn sít nhau, cảm ứng từ $B$ tại mỗi điểm tỉ lệ thuận với số vòng dây $N$, và từ thông qua mỗi vòng dây lại được móc vòng qua toàn bộ $N$ vòng dây. Vì vậy, từ thông móc vòng $N\Phi_B$ tỉ lệ thuận với $N^2$, kéo theo độ tự cảm $L$ tỉ lệ thuận với bình phương số vòng dây $N^2$.

Độ tự cảm còn phụ thuộc tính từ của vật liệu trong mạch. Trong biểu thức trường, thay $\mu_0$ bằng $\mu=K_m\mu_0$ khi dùng vật liệu tuyến tính. Với vật liệu nghịch từ hoặc thuận từ, $K_m$ gần 1 nên thay đổi nhỏ. Với lõi sắt từ, thay đổi có thể rất lớn. Chẳng hạn, lõi sắt non có $K_m=5000$ có thể làm tự cảm gần 5000 lần giá trị của cùng cuộn lõi không khí.

Vật liệu sắt từ nói chung không có quan hệ từ hóa tuyến tính, nhất là gần bão hòa, nên tự cảm có thể phụ thuộc dòng. Ta dùng mô hình $L$ không đổi trong phần phân tích mạch. Với vật liệu sắt từ, xấp xỉ này cần giới hạn miền làm việc phù hợp, đủ xa bão hòa.

![Ứng dụng: Cuộn cảm lớn được lắp đặt trên các đường dây truyền tải điện để giảm thiểu xung dòng điện khi bị sét đánh.](../img/young-30/ung-dung-30a-chong-set.png)

### Hiệu điện thế giữa hai cực của cuộn cảm

Để đưa cuộn cảm vào phân tích mạch theo các định luật Kirchhoff, ta cần xác định hiệu điện thế giữa hai đầu cực của nó. Xét mạch điện ở Hình 30.5 gồm một nguồn điện biến thiên nối với một cuộn cảm lý tưởng có hai đầu cực $a$ và $b$. Giả thiết cuộn cảm là lý tưởng, nghĩa là dây dẫn có điện trở thuần không đáng kể ($R = 0$).

![Hình 30.5: Mạch điện gồm nguồn điện biến thiên nối với một cuộn cảm lý tưởng có độ tự cảm L.](../img/young-30/hinh-30-05.png)

Hộp nguồn có thể gồm pin và các điện trở biến thiên, cho phép điều chỉnh dòng cũng như tốc độ biến thiên dòng trong mạch.

Bên trong vật dẫn làm cuộn dây, tổng điện trường tác dụng lên các hạt mang điện tự do bằng không vì dây không có điện trở thuần. Điện trường tổng này gồm hai thành phần: Điện trường tĩnh điện bảo toàn $\vec{E}_c$ do các điện tích tích tụ trên bề mặt dây dẫn và hai đầu cực sinh ra, và điện trường cảm ứng không bảo toàn $\vec{E}_n$ do từ thông biến thiên tạo ra theo định luật Faraday. Do đó, tại mọi điểm bên trong dây dẫn:

$$
\begin{aligned}
\vec{E}_c + \vec{E}_n &= \vec{0} \\
\implies \vec{E}_c &= -\vec{E}_n
\end{aligned}
$$

Hiệu điện thế giữa hai đầu cực $a$ và $b$ của cuộn cảm, ký hiệu là $V_{ab} = V_a - V_b$, được định nghĩa là tích phân đường của điện trường bảo toàn $\vec{E}_c$ dọc theo cuộn dây từ $a$ sang $b$:

$$
\begin{aligned}
V_{ab} &= V_a - V_b \\
&= \int_a^b \vec{E}_c \cdot d\vec{l} \\
&= -\int_a^b \vec{E}_n \cdot d\vec{l}
\end{aligned}
$$

Trong mô hình mạch tập trung, áp dụng Faraday quanh vòng theo chiều dòng cho

$$
\oint\vec E_n\cdot d\vec l=-L\frac{di}{dt}.
$$

Đóng góp của điện trường cảm ứng ngoài cuộn được bỏ qua trong mô hình này. Vì vậy tích phân quanh cả vòng được thay bằng tích phân từ $a$ đến $b$ dọc cuộn:

$$
\int_a^b\vec E_n\cdot d\vec l=-L\frac{di}{dt}.
$$

Kết hợp với $\vec E_c=-\vec E_n$ bên trong cuộn, ta nhận được hiệu điện thế hai đầu:

$$
V_{ab} = V_a - V_b = L \frac{di}{dt} \tag{30.8}
$$

Phương trình (30.8) cho thấy hiệu điện thế hai đầu cuộn cảm lý tưởng phụ thuộc tốc độ biến thiên dòng. Chiều dương của dòng được chọn từ $a$ sang $b$.

Hiệu điện thế này liên hệ với điện trường bảo toàn do phân bố điện tích tạo ra. Vì thế tổng các độ biến thiên điện thế quanh một vòng vẫn bằng không, và có thể áp dụng quy tắc vòng Kirchhoff khi tính cả điện áp cuộn cảm. Điều đó không làm điện trường cảm ứng trở thành điện trường bảo toàn.

![Hình 30.6: So sánh hiệu điện thế hai đầu cực của điện trở thuần và cuộn cảm lý tưởng trong các chế độ dòng điện khác nhau.](../img/young-30/hinh-30-06.png)

Quan sát Hình 30.6 để nắm vững quy ước dấu của hiệu điện thế:

- **Hình 30.6a: Điện trở thuần**: Với dòng điện $i$ chạy từ $a$ sang $b$, hiệu điện thế tuân theo định luật Ohm: $V_{ab} = iR$. Bất kể dòng điện tăng, giảm hay không đổi, điện thế luôn giảm từ $a$ sang $b$, tức là $V_a > V_b$ và $V_{ab} > 0$.
- **Hình 30.6b: Cuộn cảm khi dòng điện không đổi ($di/dt = 0$)**: Hiệu điện thế giữa hai đầu cực hoàn toàn bằng không: $V_{ab} = 0$. Cuộn cảm lý tưởng đóng vai trò tương đương một dây nối không điện trở.
- **Hình 30.6c: Cuộn cảm khi dòng điện đang tăng ($di/dt > 0$)**: Hiệu điện thế $V_{ab} = L \frac{di}{dt} > 0$, nghĩa là điện thế ở cực $a$ cao hơn cực $b$ ($V_a > V_b$). Cực $a$ là cực dương, cực $b$ là cực âm, đồng thời suất điện động tự cảm hướng từ $b$ về $a$ để cản trở sự tăng của dòng điện. Cuộn cảm hoạt động như một tải tiêu thụ năng lượng từ nguồn ngoài.
- **Hình 30.6d: Cuộn cảm khi dòng điện đang giảm ($di/dt < 0$)**: Hiệu điện thế $V_{ab} = L \frac{di}{dt} < 0$, nghĩa là điện thế ở cực $a$ thấp hơn cực $b$ ($V_a < V_b$). Cực $b$ là cực dương, đồng thời suất điện động tự cảm hướng từ $a$ sang $b$ cùng chiều với dòng điện để cản trở sự suy giảm của dòng. Khi đó, cuộn cảm đóng vai trò như một nguồn cấp điện trả năng lượng về cho mạch.

### Ứng dụng của cuộn cảm trong đời sống

Tính chất cản trở biến thiên dòng được dùng trong các ứng dụng sau:

- **Hạn chế xung do sét trên đường dây điện**: Sét tạo xung điện áp có thể làm hỏng các phần tử của hệ thống truyền tải và thiết bị nối vào, chẳng hạn đồ điện gia dụng. Các cuộn cảm lớn được đưa vào hệ thống để hạn chế biến thiên dòng nhanh, góp phần giảm tác hại của xung.
- **Chấn lưu đèn huỳnh quang (Ballast)**: Trong đèn huỳnh quang (Hình 30.7), dòng điện chạy qua chất khí ion hóa (plasma) bên trong ống để kích thích phát sáng. Khí ion hóa là một chất dẫn điện phi ohmic có điện trở vi phân âm: Cường độ dòng điện càng lớn thì chất khí càng bị ion hóa mạnh và điện trở càng giảm. Nếu nối trực tiếp ống đèn với nguồn điện, dòng điện sẽ tăng mất kiểm soát và phá hỏng mạch. Người ta mắc nối tiếp ống đèn với một cuộn cảm (chấn lưu từ) để giới hạn tốc độ tăng của dòng điện. Ngoài ra, điện áp lưới xoay chiều $60\text{ Hz}$ đổi chiều và triệt tiêu tức thời 120 lần trong một giây. Khi điện áp lưới đi qua giá trị không, suất điện động tự cảm của chấn lưu phóng ra để duy trì dòng điện liên tục, giữ cho chất khí không bị khử ion và đèn không bị tắt.
- **Cảm biến vòng từ phát hiện xe cộ**: Khung xe chứa thép, một vật liệu sắt từ. Khi xe qua cuộn chôn dưới mặt đường, tự cảm của cuộn tăng và mạch điện tử phát hiện thay đổi đó. Một cách điều khiển là chuyển đèn xanh sau khi số xe đã đi qua vòng đạt giá trị lập trình trước.

Chấn lưu từ còn được dùng cho đèn đường phát sáng nhờ hơi thủy ngân hoặc natri và cho đèn neon. Trong đèn huỳnh quang compact, chấn lưu từ được thay bằng mạch phức tạp hơn dùng transistor, sẽ được xét ở phần điện tử bán dẫn.

![Hình 30.7: Đèn huỳnh quang sử dụng cuộn cảm chấn lưu mắc nối tiếp để ổn định dòng điện plasma và duy trì độ sáng.](../img/young-30/hinh-30-07.png)

![Hình 30.8: Ống dây hình xuyến chỉ vẽ một số vòng minh họa. Một phần được cắt để thấy tiết diện A và bán kính r.](../img/young-30/hinh-30-08.png)

::: example Ví dụ 30.3: Tính độ tự cảm của ống dây hình xuyến (Toroid)
Xét một ống dây hình xuyến có bán kính trung bình $r$, diện tích tiết diện thẳng $A$, gồm $N$ vòng dây quấn sít nhau như ở Hình 30.8. Bên trong lõi ống dây là chân không. Giả thiết bán kính tiết diện nhỏ hơn nhiều so với bán kính trung bình $r$, hãy xác định độ tự cảm $L$ của ống dây hình xuyến. Áp dụng bằng số với $N = 200$ vòng, $A = 5{,}0\text{ cm}^2 = 5{,}0 \times 10^{-4}\text{ m}^2$ và $r = 0{,}10\text{ m}$.

**Phân tích bài toán**:
Từ trường của ống dây hình xuyến chỉ tập trung bên trong lõi, từ trường ở không gian bên ngoài bằng không. Tại khoảng cách $r$ tính từ trục đối xứng của xuyến, cảm ứng từ $B$ được xác định theo định luật Ampere:

$$
B = \frac{\mu_0 N i}{2\pi r}
$$

Vì tiết diện $A$ có kích thước nhỏ so với $r$, ta có thể xem cảm ứng từ $B$ phân bố đều trên toàn bộ diện tích tiết diện $A$.

**Các bước tính toán**:
Từ thông qua mỗi vòng dây của ống xuyến là:

$$
\Phi_B = BA = \frac{\mu_0 N i A}{2\pi r}
$$

Từ thông này đi qua toàn bộ $N$ vòng dây của ống xuyến. Áp dụng định nghĩa độ tự cảm từ phương trình (30.6):

$$
L = \frac{N \Phi_B}{i} = \frac{\mu_0 N^2 A}{2\pi r}
$$

Biểu thức này cho thấy độ tự cảm của ống xuyến tỉ lệ thuận với bình phương số vòng dây $N^2$, tỉ lệ thuận với diện tích tiết diện $A$ và tỉ lệ nghịch với chu vi trung bình $2\pi r$. Thay các số liệu cụ thể vào:

$$
\begin{aligned}
L &= \frac{\mu_0 N^2 A}{2\pi r} \\
&= \frac{4\pi \times 10^{-7}\text{ T}\cdot\text{m/A}}{2\pi(0{,}10\text{ m})} \times (200)^2 \times (5{,}0 \times 10^{-4}\text{ m}^2) \\
&= 4{,}0 \times 10^{-5}\text{ H} \\
&= 40\ \mu\text{H}
\end{aligned}
$$

Độ tự cảm của cuộn dây hình xuyến này là $40\ \mu\text{H}$.
:::

::: example Ví dụ 30.4: Tính suất điện động tự cảm
Giả sử dòng điện trong cuộn dây hình xuyến của Ví dụ 30.3 tăng đều từ $0$ lên $6{,}0\text{ A}$ trong khoảng thời gian $\Delta t = 3{,}0\ \mu\text{s}$. Hãy xác định độ lớn và chiều của suất điện động tự cảm xuất hiện trong cuộn dây.

**Phân tích bài toán**:
Ta đã biết độ tự cảm của cuộn xuyến là $L = 40\ \mu\text{H} = 40 \times 10^{-6}\text{ H}$. Dòng điện tăng đều nên tốc độ biến thiên dòng điện $di/dt$ là một hằng số. Ta áp dụng phương trình (30.7) để tính độ lớn của suất điện động tự cảm và áp dụng định luật Lenz để xác định chiều của nó.

**Các bước tính toán**:
Tốc độ biến thiên của dòng điện trong khoảng thời gian đã cho là:

$$
\begin{aligned}
\frac{di}{dt} &= \frac{6{,}0\text{ A} - 0}{3{,}0 \times 10^{-6}\text{ s}} \\
&= 2{,}0 \times 10^6\text{ A/s}
\end{aligned}
$$

Áp dụng phương trình (30.7), độ lớn của suất điện động tự cảm xuất hiện trong cuộn dây là:

$$
\begin{aligned}
|\mathcal{E}| &= L \left|\frac{di}{dt}\right| \\
&= (40 \times 10^{-6}\text{ H}) \times (2{,}0 \times 10^6\text{ A/s}) \\
&= 80\text{ V}
\end{aligned}
$$

Vì dòng điện đang tăng theo chiều từ $a$ sang $b$, theo định luật Lenz, suất điện động cảm ứng sinh ra phải có chiều chống lại sự tăng của dòng điện này. Do đó, suất điện động tự cảm có chiều hướng từ $b$ về $a$. Nếu xét hiệu điện thế giữa hai đầu cực, cực $a$ có điện thế cao hơn cực $b$ một lượng $V_{ab} = +80\text{ V}$, hoàn toàn phù hợp với trường hợp minh họa ở Hình 30.6c.
:::

### Câu hỏi ôn tập mục 30.2

Hãy sắp xếp các cuộn cảm sau đây theo thứ tự hiệu điện thế $V_{ab}$ từ giá trị dương lớn nhất đến giá trị âm nhỏ nhất. Trong mỗi trường hợp, giả thiết cuộn cảm có điện trở thuần bằng không và chiều dòng điện quy ước đi từ cực $a$ xuyên qua cuộn cảm đến cực $b$:

(i) Cuộn cảm có độ tự cảm $L = 2{,}0\ \mu\text{H}$, dòng điện tăng từ $1{,}0\text{ A}$ lên $2{,}0\text{ A}$ trong $0{,}50\text{ s}$.

(ii) Cuộn cảm có độ tự cảm $L = 4{,}0\ \mu\text{H}$, dòng điện giảm từ $3{,}0\text{ A}$ về $0$ trong $2{,}0\text{ s}$.

(iii) Cuộn cảm có độ tự cảm $L = 1{,}0\ \mu\text{H}$, dòng điện duy trì không đổi ở giá trị $4{,}0\text{ A}$.

(iv) Cuộn cảm có độ tự cảm $L = 1{,}0\ \mu\text{H}$, dòng điện tăng từ $0$ lên $4{,}0\text{ A}$ trong $0{,}25\text{ s}$.

<details><summary>Xem đáp án và giải thích</summary>

Thứ tự sắp xếp đúng từ dương lớn nhất đến âm nhỏ nhất là **(iv), (i), (iii), (ii)**.

Theo phương trình (30.8), hiệu điện thế giữa hai đầu cực của cuộn cảm lý tưởng khi dòng điện đi từ cực $a$ sang cực $b$ được tính theo công thức:

$$
V_{ab} = L \frac{di}{dt}
$$

Ta lần lượt tính giá trị $V_{ab}$ cho từng trường hợp:

- Trường hợp (i): Dòng điện tăng với tốc độ $\frac{di}{dt} = \frac{2{,}0\text{ A} - 1{,}0\text{ A}}{0{,}50\text{ s}} = 2{,}0\text{ A/s}$. Hiệu điện thế là:

$$
\begin{aligned}
V_{ab} &= (2{,}0 \times 10^{-6}\text{ H}) \times (2{,}0\text{ A/s}) \\
&= 4{,}0\ \mu\text{V}
\end{aligned}
$$

- Trường hợp (ii): Dòng điện giảm với tốc độ $\frac{di}{dt} = \frac{0 - 3{,}0\text{ A}}{2{,}0\text{ s}} = -1{,}5\text{ A/s}$. Hiệu điện thế là:

$$
\begin{aligned}
V_{ab} &= (4{,}0 \times 10^{-6}\text{ H}) \times (-1{,}5\text{ A/s}) \\
&= -6{,}0\ \mu\text{V}
\end{aligned}
$$

- Trường hợp (iii): Dòng điện không đổi theo thời gian, nên đạo hàm $\frac{di}{dt} = 0$. Hiệu điện thế là $V_{ab} = 0$.

- Trường hợp (iv): Dòng điện tăng với tốc độ $\frac{di}{dt} = \frac{4{,}0\text{ A} - 0}{0{,}25\text{ s}} = 16\text{ A/s}$. Hiệu điện thế là:

$$
\begin{aligned}
V_{ab} &= (1{,}0 \times 10^{-6}\text{ H}) \times (16\text{ A/s}) \\
&= 16\ \mu\text{V}
\end{aligned}
$$

So sánh các giá trị tính được: $16\ \mu\text{V} > 4{,}0\ \mu\text{V} > 0 > -6{,}0\ \mu\text{V}$, tương ứng với thứ tự các cuộn cảm là (iv), (i), (iii), (ii).

</details>
