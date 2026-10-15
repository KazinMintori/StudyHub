## 30.3. Năng lượng từ trường

Muốn thiết lập dòng trong cuộn cảm, nguồn ngoài phải sinh công. Với cuộn lý tưởng không có điện trở, công ấy làm tăng năng lượng của từ trường. Khi dòng giảm, năng lượng đó có thể được giải phóng trở lại mạch.

### Năng lượng tích trữ trong cuộn cảm

Ta hãy tính tổng năng lượng $U$ mà nguồn điện bên ngoài cần cung cấp để đưa cường độ dòng điện trong cuộn cảm có độ tự cảm $L$ từ giá trị ban đầu bằng không lên một giá trị ổn định cuối cùng $I$. Giả thiết cuộn cảm là lý tưởng với điện trở thuần bằng không, do đó không có sự tiêu hao năng lượng thành nhiệt bên trong cuộn dây.

Tại một thời điểm bất kỳ trong quá trình nạp dòng, giả sử cường độ dòng điện tức thời là $i$ và dòng điện đang tăng với tốc độ $di/dt > 0$. Hiệu điện thế giữa hai đầu cực $a$ và $b$ của cuộn cảm ở thời điểm này là $V_{ab} = L \frac{di}{dt}$. Công suất tức thời $P$ mà nguồn điện bên ngoài cung cấp cho cuộn cảm được xác định bởi:

$$
P = V_{ab} i = L i \frac{di}{dt}
$$

Trong một khoảng thời gian vô cùng nhỏ $dt$, phần năng lượng $dU$ truyền vào cuộn cảm là $dU = P dt$, tức là:

$$
dU = L i\, di
$$

Tổng năng lượng $U$ cung cấp cho cuộn cảm trong toàn bộ quá trình dòng điện tăng từ giá trị ban đầu $i = 0$ đến giá trị cuối cùng $i = I$ chính là tích phân:

$$
U = \int_0^I L i\, di = \frac{1}{2} L I^2 \tag{30.9}
$$

Sau khi dòng điện đã đạt đến giá trị ổn định $I$, đạo hàm $di/dt = 0$, công suất cung cấp triệt tiêu và không còn năng lượng nào được nạp thêm vào cuộn cảm nữa. Khi trong mạch không có dòng điện ($I = 0$), năng lượng tích trữ bằng không.

![Hình 30.9: Điện trở tiêu tán năng lượng thành nhiệt không thể thu hồi, trong khi cuộn cảm tích trữ năng lượng từ trường có thể hoàn trả cho mạch.](../img/young-30/hinh-30-09.png)

Quan sát Hình 30.9 để thấy rõ sự khác biệt bản chất giữa điện trở và cuộn cảm:

- Trong một **điện trở thuần**, công suất điện $P = i^2 R$ bị tiêu tán không thuận nghịch thành nhiệt năng và tỏa ra môi trường xung quanh. Năng lượng này không thể tự động biến đổi ngược lại thành điện năng cho mạch.
- Trong một **cuộn cảm lý tưởng**, năng lượng $\frac{1}{2} L I^2$ không bị tiêu tán mà được tích trữ lại. Khi cường độ dòng điện giảm từ $I$ về không, cuộn cảm đóng vai trò như một nguồn cấp điện, giải phóng toàn bộ năng lượng tích trữ này trở lại mạch điện bên ngoài.

Nếu mở công tắc để ngắt mạch nhanh, suất điện động tự cảm có thể tăng cao và ion hóa không khí ở khe tiếp điểm. Hồ quang tạo đường dẫn để dòng tiếp tục tồn tại trong một thời gian hữu hạn. Một phần năng lượng từ trường được chuyển thành nhiệt và ánh sáng ở hồ quang.

### Mật độ năng lượng của từ trường

Năng lượng tích trữ trong cuộn cảm được lưu giữ ở đâu? Bản chất vật lý cho thấy nguồn năng lượng này cư trú ngay trong từ trường do dòng điện tạo ra trong không gian.

Để làm rõ điều này, ta xét lại ống dây hình xuyến ở Ví dụ 30.3 có lõi chân không, bán kính trung bình $r$, diện tích tiết diện $A$ và $N$ vòng dây quấn sít nhau. Toàn bộ từ trường được giam giữ trọn vẹn bên trong thể tích lõi xuyến $V = 2\pi r A$, và từ trường ở bên ngoài hoàn toàn bằng không. Độ tự cảm của ống xuyến là $L = \frac{\mu_0 N^2 A}{2\pi r}$. Khi cuộn dây mang dòng điện $I$, tổng năng lượng tích trữ theo phương trình (30.9) là:

$$
\begin{aligned}
U &= \frac{1}{2} L I^2 \\
&= \frac{1}{2} \left(\frac{\mu_0 N^2 A}{2\pi r}\right) I^2
\end{aligned}
$$

Vì toàn bộ năng lượng này phân bố đều trong thể tích lõi $V = 2\pi r A$, năng lượng trên một đơn vị thể tích, gọi là **mật độ năng lượng từ trường** $u = U / V$, có biểu thức:

$$
u = \frac{U}{2\pi r A} = \frac{1}{2} \mu_0 \frac{N^2 I^2}{(2\pi r)^2}
$$

Mặt khác, cảm ứng từ $B$ bên trong lòng ống xuyến được xác định bởi $B = \frac{\mu_0 N I}{2\pi r}$, kéo theo tỉ số:

$$
\frac{N I}{2\pi r} = \frac{B}{\mu_0}
$$

Thay hệ thức này vào biểu thức của mật độ năng lượng $u$, ta thu được công thức tổng quát cho mật độ năng lượng từ trường trong chân không:

$$
u = \frac{B^2}{2\mu_0} \tag{30.10}
$$

Phương trình (30.10) là biểu thức tương ứng của từ trường đối với công thức mật độ năng lượng của điện trường trong chân không $u = \frac{1}{2} \epsilon_0 E^2$ đã học ở Chương 24. Chẳng hạn, trong máy chụp cộng hưởng từ (MRI) có từ trường mạnh $B = 1{,}5\text{ T}$, mật độ năng lượng từ trường trong chân không đạt giá trị:

$$
\begin{aligned}
u &= \frac{B^2}{2\mu_0} \\
&= \frac{(1{,}5\text{ T})^2}{2(4\pi \times 10^{-7}\text{ T}\cdot\text{m/A})} \\
&\approx 9{,}0 \times 10^5\text{ J/m}^3
\end{aligned}
$$

Với vật liệu từ tuyến tính có độ từ thẩm không đổi $\mu=K_m\mu_0$, thay $\mu_0$ bằng $\mu$ trong biểu thức mật độ năng lượng:

$$
u = \frac{B^2}{2\mu} \tag{30.11}
$$

Phương trình (30.11) vừa được dẫn ra từ mô hình cụ thể của ống dây hình xuyến. Tuy nhiên, các phân tích điện động lực học tổng quát khẳng định rằng biểu thức này luôn nghiệm đúng cho mọi cấu hình từ trường bất kỳ trong chân không cũng như trong môi trường vật chất tuyến tính.

![Ứng dụng: Ảnh ghép từ hai ảnh Mặt Trời cho thấy một đợt phun trào nhật hoa, được cấp năng lượng bởi từ trường.](../img/young-30/ung-dung-30a-nhat-hoa.png)

![Hình 30.10: Bugi ô tô được đánh lửa nhờ năng lượng từ trường tích lũy trong cuộn cảm của hệ thống đánh lửa.](../img/young-30/hinh-30-10.png)

### Ứng dụng của năng lượng từ trường

Năng lượng từ trường đóng vai trò quyết định trong nhiều hiện tượng từ quy mô vi mô đến quy mô vũ trụ:

- **Hệ thống đánh lửa của ô tô chạy xăng (Ignition System)**: Trong động cơ đốt trong (Hình 30.10), cuộn sơ cấp gồm khoảng 250 vòng dây được nối với ắc quy $12\text{ V}$ để tích lũy năng lượng dưới dạng từ trường mạnh. Bao quanh cuộn này là cuộn thứ cấp gồm khoảng 25 000 vòng dây mảnh. Đúng thời điểm cần đánh lửa trong xi lanh, công tắc ngắt dòng điện sơ cấp. Từ trường suy giảm về không với tốc độ rất nhanh, làm xuất hiện một xung suất điện động cảm ứng lên tới hàng chục nghìn volt ở cuộn thứ cấp. Xung năng lượng từ trường này phóng qua khe hở của bugi tạo thành tia lửa điện nóng bỏng, đốt cháy hỗn hợp nhiên liệu và không khí.
- **Phun trào nhật hoa trên Mặt Trời (Coronal Mass Ejection - CME)**: Trong thiên văn học, các vụ phun trào nhật hoa giải phóng một khối lượng plasma khổng lồ khoảng $10^{12}\text{ kg}$ (tương đương một tỷ tấn vật chất) vào không gian liên hành tinh với vận tốc từ $500\text{ km/s}$ trở lên. Các đợt phun trào này cách nhau từ vài giờ đến vài ngày. Những vụ nổ khổng lồ này được cung cấp năng lượng bởi năng lượng tích trữ trong từ trường của Mặt Trời. Khác với từ trường tương đối ổn định của Trái Đất, từ trường của Mặt Trời liên tục biến đổi, và các vùng có từ trường mạnh bất thường (kéo theo mật độ năng lượng từ trường đặc biệt cao) thường xuyên hình thành. Một vụ phun trào nhật hoa xuất hiện khi năng lượng tích trữ trong một vùng như vậy đột ngột được giải phóng.

::: example Ví dụ 30.5: Tích trữ năng lượng trong cuộn cảm quy mô lớn
Ngành công nghiệp năng lượng điện luôn tìm kiếm các giải pháp hiệu quả để tích trữ điện năng dư thừa phát ra vào các giờ thấp điểm để cung cấp cho phụ tải trong giờ cao điểm. Giả sử ta muốn tích trữ một lượng năng lượng là $1{,}00\text{ kW}\cdot\text{h}$ vào một cuộn cảm mang dòng điện $I = 200\text{ A}$. Độ tự cảm $L$ của cuộn cảm cần thiết phải bằng bao nhiêu?

**Phân tích bài toán**:
Ta đã biết lượng năng lượng cần tích trữ $U$ và cường độ dòng điện $I = 200\text{ A}$. Trước hết, ta đổi năng lượng từ đơn vị kilowatt-giờ sang đơn vị chuẩn joule của hệ SI. Sau đó, ta áp dụng công thức năng lượng từ trường ở phương trình (30.9) để tìm độ tự cảm $L$.

**Các bước tính toán**:
Đổi đơn vị năng lượng sang joule:

$$
\begin{aligned}
U &= 1{,}00\text{ kW}\cdot\text{h} \\
&= (1{,}00 \times 10^3\text{ W}) \times (3600\text{ s}) \\
&= 3{,}60 \times 10^6\text{ J}
\end{aligned}
$$

Từ phương trình (30.9) xác định năng lượng tích trữ trong cuộn cảm:

$$
U = \frac{1}{2} L I^2 \implies L = \frac{2U}{I^2}
$$

Thay các giá trị số vào biểu thức:

$$
\begin{aligned}
L &= \frac{2U}{I^2} \\
&= \frac{2(3{,}60 \times 10^6\text{ J})}{(200\text{ A})^2} \\
&= 180\text{ H}
\end{aligned}
$$

Độ tự cảm yêu cầu là $180\text{ H}$.

**Nhận xét ý nghĩa vật lý**:
Độ tự cảm yêu cầu lớn hơn độ tự cảm của ống dây hình xuyến ở Ví dụ 30.3 hơn một triệu lần. Dây dẫn thông thường để dẫn dòng điện $200\text{ A}$ phải có đường kính lớn nhằm giữ cho điện trở ở mức nhỏ và tránh tổn hao năng lượng không thể chấp nhận được do tỏa nhiệt Joule $I^2 R$. Do đó, một cuộn cảm $180\text{ H}$ chế tạo bằng dây dẫn thông thường sẽ có kích thước rất lớn (tương đương kích thước của một căn phòng). Một cuộn cảm siêu dẫn có thể nhỏ hơn rất nhiều, bởi vì điện trở của vật liệu siêu dẫn bằng không và ta có thể dùng dây dẫn mảnh hơn nhiều. Tuy nhiên, các dây siêu dẫn phải được duy trì ở nhiệt độ thấp để giữ được tính siêu dẫn, và việc duy trì nhiệt độ này bản thân nó cũng tiêu tốn năng lượng. Bất chấp những giới hạn này, các cuộn cảm siêu dẫn vẫn có hiệu quả rất cao để tích trữ năng lượng và đã được một số công ty điện lực sử dụng ở quy mô nhỏ.
:::

### Câu hỏi ôn tập mục 30.3

Dòng trong một ống dây được đảo chiều nhưng giữ nguyên độ lớn.
(a) Thao tác này có làm thay đổi từ trường bên trong ống dây không?
(b) Thao tác này có làm thay đổi mật độ năng lượng từ trường bên trong ống dây không?

<details><summary>Xem đáp án và giải thích</summary>

(a) **Có**. Cảm ứng từ $\vec{B}$ bên trong ống dây là một đại lượng vector. Khi dòng điện đổi chiều, chiều của các đường sức từ trường bị đảo ngược $180^\circ$ theo quy tắc nắm tay phải ($\vec{B} \to -\vec{B}$), dù độ lớn của cảm ứng từ vẫn không đổi. Vì vector thay đổi chiều, từ trường bên trong ống dây đã bị thay đổi.

(b) **Không**. Theo phương trình (30.10), mật độ năng lượng của từ trường là $u = \frac{B^2}{2\mu_0}$. Đại lượng này là một đại lượng vô hướng không âm, tỉ lệ với bình phương độ lớn của cảm ứng từ. Khi độ lớn của cảm ứng từ $B$ không đổi, bình phương $(-B)^2 = B^2$ vẫn giữ nguyên giá trị. Do đó, mật độ năng lượng từ trường bên trong ống dây hoàn toàn không thay đổi.

</details>
