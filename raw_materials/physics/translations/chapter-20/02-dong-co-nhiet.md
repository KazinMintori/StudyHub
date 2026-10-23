## 20.2 Động cơ nhiệt

Cốt lõi tạo nên nền văn minh công nghệ hiện đại là khả năng khai thác các nguồn năng lượng khác ngoài sức cơ bắp của con người và động vật. Đôi khi cơ năng có sẵn trực tiếp trong tự nhiên, chẳng hạn như năng lượng dòng nước chảy và năng lượng gió. Tuy nhiên, phần lớn năng lượng phục vụ đời sống và sản xuất đến từ quá trình đốt cháy nhiên liệu hóa thạch (than đá, dầu mỏ, khí đốt) và từ các phản ứng phân hạch hạt nhân. Các nguồn này cung cấp năng lượng dưới dạng nhiệt lượng. Nguồn nhiệt này rất hữu ích cho việc sưởi ấm các tòa nhà, nấu nướng và chế biến hóa chất. Tuy nhiên, để vận hành một cỗ máy hoặc đẩy một phương tiện giao thông chuyển động, chúng ta bắt buộc phải có cơ năng.

Do đó, việc tìm hiểu cách trích xuất nhiệt từ một nguồn và chuyển hóa tối đa phần nhiệt lượng đó thành cơ năng hay công cơ học là vấn đề kỹ thuật có ý nghĩa then chốt. Quá trình biến đổi này diễn ra liên tục trong động cơ xăng của ô tô, động cơ phản lực của máy bay, tua-bin hơi nước trong các nhà máy nhiệt điện và nhiều hệ thống kỹ thuật khác. Những quá trình có bản chất tương tự cũng diễn ra trong thế giới sinh vật: Năng lượng từ thức ăn được cơ thể oxy hóa (carbohydrate kết hợp với oxy để tạo ra nước, carbon dioxide và năng lượng) và được chuyển hóa một phần thành cơ năng khi các sợi cơ bắp thực hiện công cơ học lên môi trường xung quanh.

![Hình 20.2](../img/young-20/a-hinh-20-02.png)

*Hình 20.2: Mọi phương tiện cơ giới đường bộ (ngoại trừ xe thuần điện) đều sử dụng động cơ nhiệt để tạo lực đẩy.*

Bất kỳ thiết bị nào thực hiện quá trình chuyển hóa một phần nhiệt lượng thành công cơ học đều được gọi là **động cơ nhiệt**. Thông thường, một lượng vật chất xác định bên trong động cơ sẽ trải qua các quá trình nhận nhiệt, nhả nhiệt, giãn nở, nén và đôi khi chuyển pha. Chúng ta gọi lượng vật chất này là **chất công tác** của động cơ nhiệt. Trong các động cơ đốt trong dùng cho ô tô, chất công tác là hỗn hợp không khí và hơi nhiên liệu; còn trong tua-bin hơi nước, chất công tác là nước và hơi nước.

Dạng động cơ nhiệt đơn giản nhất để phân tích lý thuyết là động cơ mà chất công tác trải qua một **quá trình chu trình**, tức là một chuỗi liên tiếp các quá trình biến đổi trạng thái mà cuối cùng đưa chất công tác trở lại đúng trạng thái ban đầu. Trong tua-bin hơi nước, nước được ngưng tụ và tái tuần hoàn liên tục qua các chu kỳ khép kín. Các động cơ đốt trong không dùng lại cùng một khối không khí cũ mà liên tục nạp khí mới và xả khí thải, nhưng chúng ta vẫn có thể mô hình hóa hoạt động của chúng bằng các chu trình nhiệt động khép kín xấp xỉ gần đúng.

### Nguồn nóng và nguồn lạnh

Mọi động cơ nhiệt đều hoạt động theo nguyên tắc chung: Hấp thụ nhiệt lượng từ một nguồn ở nhiệt độ tương đối cao, sinh ra một lượng công cơ học hữu ích, và nhả một phần nhiệt lượng dư thừa ra môi trường ở nhiệt độ thấp hơn. Xét theo quan điểm hiệu quả năng lượng của động cơ, phần nhiệt lượng nhả ra này chính là nhiệt hao phí. Trong động cơ đốt trong, nhiệt hao phí bị thất thoát qua khí thải nóng thoát ra ống xả và qua hệ thống tản nhiệt làm mát; trong tua-bin hơi nước, đó là nhiệt lượng phải truyền ra khỏi hơi nước đã giãn nở để làm nó ngưng tụ thành nước lỏng rồi bơm ngược lại lò hơi.

Khi chất công tác trải qua một chu trình khép kín, trạng thái nhiệt động ban đầu và trạng thái kết thúc hoàn toàn trùng nhau. Do đó, nội năng ban đầu $U_1$ và nội năng cuối $U_2$ bằng nhau, tức là $\Delta U = U_2 - U_1 = 0$. Áp dụng nguyên lý thứ nhất của nhiệt động lực học cho một chu trình:

$$
\begin{aligned}
U_2 - U_1 &= 0 = Q - W \\
&\implies W = Q
\end{aligned}
$$

Hệ thức này khẳng định: Tổng công cơ học ròng sinh ra bởi động cơ trong một chu trình bằng đúng nhiệt lượng thuần túy mà động cơ nhận vào trong chu trình đó.

Khi phân tích động cơ nhiệt, ta mô hình hóa hai vật thể mà chất công tác của động cơ tương tác nhiệt. Vật thể thứ nhất, gọi là **nguồn nóng**, đại diện cho nguồn cung cấp nhiệt ở nhiệt độ cao $T_H$. Nguồn này có nhiệt dung vô cùng lớn nên có thể cấp những lượng nhiệt dồi dào cho chất công tác mà nhiệt độ $T_H$ hầu như không bị suy giảm. Vật thể thứ hai, gọi là **nguồn lạnh**, có thể hấp thụ lượng nhiệt thải ra từ động cơ ở nhiệt độ thấp hơn $T_C$ mà không làm thay đổi nhiệt độ của nguồn. Trong nhà máy nhiệt điện dùng tua-bin hơi nước, ngọn lửa và khí cháy trong lò hơi đóng vai trò là nguồn nóng, còn dòng nước sông làm mát cuộn ngưng tụ đóng vai trò là nguồn lạnh.

Ta ký hiệu nhiệt lượng trao đổi với nguồn nóng và nguồn lạnh lần lượt là $Q_H$ và $Q_C$. Theo quy ước dấu chuẩn mực của nhiệt động lực học, nhiệt lượng $Q$ có giá trị dương khi nhiệt truyền vào chất công tác, và mang giá trị âm khi nhiệt rời khỏi chất công tác. Vì vậy, đối với động cơ nhiệt: $Q_H > 0$ do động cơ nhận nhiệt từ nguồn nóng, còn $Q_C < 0$ do động cơ thải nhiệt ra nguồn lạnh. Để diễn đạt mạch lạc và tránh nhầm lẫn về dấu, ta thường dùng độ lớn $|Q_H| = Q_H$ và $|Q_C| = -Q_C$.

Nhiệt lượng ròng $Q$ mà động cơ hấp thụ trong một chu trình là:

$$
\begin{aligned}
Q &= Q_H + Q_C \\
&= |Q_H| - |Q_C|
\end{aligned}
\tag{20.1}
$$

Công có ích do động cơ sinh ra trong một chu trình được xác định bởi nguyên lý thứ nhất:

$$
\begin{aligned}
W &= Q = Q_H + Q_C \\
&= |Q_H| - |Q_C|
\end{aligned}
\tag{20.2}
$$

### Biểu đồ dòng năng lượng và hiệu suất nhiệt

Ta biểu diễn các biến đổi năng lượng trong một động cơ nhiệt bằng sơ đồ dòng năng lượng ở Hình 20.3. Bản thân động cơ được biểu thị bằng một hình tròn ở giữa. Nhiệt lượng $Q_H$ do nguồn nóng cung cấp tỉ lệ với độ rộng của "đường ống dẫn" đi vào ở phía trên. Độ rộng của đường ống thoát ra ở phía dưới tỉ lệ với độ lớn nhiệt thải $|Q_C|$ nhả ra nguồn lạnh. Nhánh rẽ sang bên phải đại diện cho phần nhiệt lượng được chuyển hóa thành công cơ học $W$.

![Hình 20.3](../img/young-20/a-hinh-20-03.png)

*Hình 20.3: Sơ đồ dòng năng lượng mô tả nguyên lý làm việc của động cơ nhiệt.*

Về mặt lý tưởng, ta luôn mong muốn chuyển hóa trọn vẹn toàn bộ nhiệt lượng $Q_H$ thành công cơ học $W$. Nếu làm được điều đó, ta sẽ có $W = Q_H$ và $Q_C = 0$. Tuy nhiên, mọi trải nghiệm thực nghiệm đều chứng minh rằng điều này là bất khả thi: Động cơ luôn làm thất thoát một phần nhiệt ra môi trường, và $Q_C$ không bao giờ bằng không.

Ta định nghĩa **hiệu suất nhiệt** của động cơ nhiệt, ký hiệu là $e$, là thương số giữa công hữu ích sinh ra và nhiệt lượng nhận vào:

$$
e = \frac{W}{Q_H}
\tag{20.3}
$$

Hiệu suất nhiệt $e$ biểu thị tỷ phần của nhiệt lượng $Q_H$ được chuyển hóa thành công cơ học hữu ích. Nói một cách trực quan, $e$ chính là tỷ số giữa "những gì nhận được" chia cho "những gì phải chi trả". Tỷ số này luôn luôn nhỏ hơn 1. Trên sơ đồ dòng năng lượng ở Hình 20.3, một động cơ càng hiệu quả khi nhánh ống dẫn công cơ học $W$ càng rộng, còn ống dẫn nhiệt thải $|Q_C|$ càng hẹp.

Thay các biểu thức của công $W$ từ phương trình (20.2) vào định nghĩa (20.3), ta nhận được các dạng tương đương của hiệu suất nhiệt $e$:

$$
\begin{aligned}
e &= \frac{W}{Q_H} = 1 + \frac{Q_C}{Q_H} \\
&= 1 - \frac{|Q_C|}{Q_H}
\end{aligned}
\tag{20.4}
$$

Lưu ý rằng hiệu suất nhiệt $e$ là tỉ số giữa hai đại lượng có cùng thứ nguyên năng lượng, do đó $e$ là một số thuần túy không có đơn vị. Khi tính toán, ta luôn phải quy đổi $W$, $Q_H$ và $Q_C$ về cùng một đơn vị đo lường.

![Hình 20.3b](../img/young-20/a-ung-dung-01.png)

*Hình 20.3b: Ứng dụng sinh học: Cơ thể người khi tập thể dục trên xe đạp tập có hiệu suất chuyển hóa cơ học khoảng 25%.*

::: tip Ứng dụng sinh học: Hiệu suất cơ học của cơ thể sống
Mặc dù cơ thể sinh vật không phải là một động cơ nhiệt theo nghĩa nhiệt động học cổ điển, khái niệm hiệu suất vẫn được áp dụng chặt chẽ: Hiệu suất $e$ là tỉ số giữa công cơ học thực hiện được chia cho tổng năng lượng hóa học đã tiêu tốn.

Khi đạp xe đạp tập thể dục, cơ thể phải trải qua một chuỗi biến đổi nhiều tầng: Đầu tiên, chuyển hóa năng lượng liên kết hóa học trong glucose thành năng lượng trong các phân tử ATP (adenosine triphosphate). Sau đó, chuyển hóa năng lượng từ ATP thành lực co giãn của các sợi cơ bắp chân. Cuối cùng, biến chuyển động của các cơ thành lực đẩy quay bàn đạp. Hiệu suất tổng thể của toàn bộ chuỗi quá trình phức tạp này chỉ đạt khoảng 25%. Khoảng 75% năng lượng giải phóng từ glucose bị tiêu hao dưới dạng nhiệt tỏa ra làm ấm cơ thể và thoát ra môi trường xung quanh.
:::

::: tip Chiến lược giải bài tập 20.1: Động cơ nhiệt
- **Nhận diện khái niệm**: Động cơ nhiệt là thiết bị chuyển hóa một phần nhiệt lượng hấp thụ từ nguồn nóng thành công cơ học và nhả nhiệt lượng còn lại cho nguồn lạnh.
- **Thiết lập bài toán**:
  - Vẽ sơ đồ dòng năng lượng như Hình 20.3 để hình dung rõ ràng các dòng năng lượng vào và ra.
  - Sử dụng phương trình (20.4) khi đề bài đề cập tới hiệu suất nhiệt của động cơ.
- **Thực hiện các bước giải**:
  1. Cẩn thận tuyệt đối với quy ước dấu: $W > 0$ khi hệ giãn nở sinh công, $W < 0$ khi hệ bị nén. Các đại lượng $Q$ mang dấu dương khi nhiệt đi vào hệ và mang dấu âm khi nhiệt đi ra khỏi hệ. Khi biết $Q_C < 0$, ta có thể viết $Q_C = -|Q_C|$.
  2. Công suất là công sinh ra trong một đơn vị thời gian ($P = W/t$). Tốc độ truyền nhiệt (dòng nhiệt) là nhiệt lượng truyền qua trong một đơn vị thời gian ($H = Q/t$). Với các bài toán có yếu tố thời gian, hãy xác định lượng công $W$ hoặc nhiệt $Q$ trao đổi trong 1 giây hoặc 1 giờ.
  3. Giải hệ phương trình để tìm các biến số mục tiêu.
- **Đánh giá kết quả**: Dùng nguyên lý thứ nhất của nhiệt động lực học để kiểm tra lại tính bảo toàn năng lượng và độ hợp lý của các dấu đại số.
:::

::: example Ví dụ 20.1: Phân tích một động cơ nhiệt
Một động cơ xe tải chạy bằng xăng hấp thụ $10{,}000\,\mathrm{J}$ nhiệt lượng và sinh ra $2000\,\mathrm{J}$ công cơ học trong mỗi chu trình hoạt động. Nhiệt lượng nhận được từ việc đốt cháy xăng có nhiệt dung cháy $L_c = 5{,}0 \times 10^4\,\mathrm{J/g}$.

(a) Hiệu suất nhiệt của động cơ này bằng bao nhiêu?
(b) Mỗi chu trình động cơ thải ra môi trường bao nhiêu nhiệt lượng?
(c) Nếu động cơ thực hiện 25 chu trình trong mỗi giây, công suất phát ra của động cơ bằng bao nhiêu watt? Bằng bao nhiêu mã lực (hp)?
(d) Khối lượng xăng bị đốt cháy trong mỗi chu trình là bao nhiêu?
(e) Khối lượng xăng bị đốt cháy trong mỗi giây là bao nhiêu? Trong mỗi giờ là bao nhiêu?

![Hình 20.4](../img/young-20/a-hinh-20-04.png)

*Hình 20.4: Sơ đồ dòng năng lượng cho bài toán Ví dụ 20.1.*

**Tóm tắt**:
- $Q_H = 10{,}000\,\mathrm{J}$ trên mỗi chu trình
- $W = 2000\,\mathrm{J}$ trên mỗi chu trình
- $L_c = 5{,}0 \times 10^4\,\mathrm{J/g}$
- Tần số chu trình: $f = 25\,\text{chu trình/s}$
- Hệ số đổi đơn vị: $1\,\mathrm{hp} = 746\,\mathrm{W}$
- Khối lượng riêng của xăng: $\rho \approx 0{,}70\,\mathrm{g/cm^3}$

**Hướng đi**:
- Áp dụng phương trình (20.4) ở dạng $e = W/Q_H$ để tính hiệu suất nhiệt ở câu (a).
- Dùng phương trình (20.2) để tìm nhiệt thải $Q_C$ ở câu (b).
- Công suất phát ra là tích giữa công sinh ra trong một chu trình và số chu trình thực hiện được trong một giây ở câu (c).
- Nhiệt dung cháy $L_c$ cho phép tính khối lượng nhiên liệu cần đốt để cung cấp nhiệt lượng $Q_H$ ở câu (d) và (e).

**Lời giải chi tiết**:

(a) Từ phương trình (20.4), hiệu suất nhiệt của động cơ là:

$$
\begin{aligned}
e &= \frac{W}{Q_H} = \frac{2000\,\mathrm{J}}{10{,}000\,\mathrm{J}} \\
&= 0{,}20 = 20\%
\end{aligned}
$$

(b) Từ phương trình (20.2), ta có $W = Q_H + Q_C$, suy ra:

$$
\begin{aligned}
Q_C &= W - Q_H \\
&= 2000\,\mathrm{J} - 10{,}000\,\mathrm{J} \\
&= -8000\,\mathrm{J}
\end{aligned}
$$

Dấu âm chỉ rõ nhiệt lượng thoát ra khỏi chất công tác. Như vậy, động cơ thải ra $8000\,\mathrm{J}$ nhiệt lượng trong mỗi chu trình.

(c) Công suất phát ra $P$ bằng công sinh ra trong một chu trình nhân với số chu trình trong một giây:

$$
\begin{aligned}
P &= (2000\,\mathrm{J})(25\,\mathrm{s^{-1}}) \\
&= 50{,}000\,\mathrm{W} = 50\,\mathrm{kW}
\end{aligned}
$$

Đổi công suất sang đơn vị mã lực:

$$
\begin{aligned}
P &= \frac{50{,}000\,\mathrm{W}}{746\,\mathrm{W/hp}} \\
&\approx 67\,\mathrm{hp}
\end{aligned}
$$

(d) Gọi $m$ là khối lượng xăng bị đốt cháy trong mỗi chu trình. Vì $Q_H = m L_c$, ta suy ra:

$$
\begin{aligned}
m &= \frac{Q_H}{L_c} \\
&= \frac{10{,}000\,\mathrm{J}}{5{,}0 \times 10^4\,\mathrm{J/g}} \\
&= 0{,}20\,\mathrm{g}
\end{aligned}
$$

(e) Khối lượng xăng tiêu thụ trong mỗi giây bằng khối lượng tiêu thụ mỗi chu trình nhân với số chu trình mỗi giây:

$$
(0{,}20\,\mathrm{g})(25\,\mathrm{s^{-1}}) = 5{,}0\,\mathrm{g/s}
$$

Khối lượng xăng tiêu thụ trong một giờ ($3600\,\mathrm{s}$) là:

$$
\begin{aligned}
\frac{m}{t} &= (5{,}0\,\mathrm{g/s})(3600\,\mathrm{s/h}) \\
&= 18{,}000\,\mathrm{g/h} \\
&= 18\,\mathrm{kg/h}
\end{aligned}
$$

**Đánh giá**: Mức hiệu suất nhiệt 20% là giá trị hoàn toàn điển hình đối với động cơ ô tô và xe tải khi $W$ chỉ tính phần công hữu ích truyền tới các trục bánh xe. Ta có thể kiểm tra lượng xăng đốt cháy trong một giờ dưới dạng độ tiêu thụ nhiên liệu. Khối lượng riêng của xăng vào khoảng $0{,}70\,\mathrm{g/cm^3}$, tương ứng với thể tích tiêu thụ khoảng $25{,}7\,\text{lít/h}$ (khoảng $6{,}8\,\text{gallon/h}$). Nếu xe tải chạy với tốc độ ổn định $88\,\mathrm{km/h}$ ($55\,\mathrm{mi/h}$), mức tiêu thụ này tương đương với khoảng $3{,}4\,\mathrm{km/L}$ ($8{,}1\,\mathrm{mi/gallon}$). Đây là mức tiêu hao nhiên liệu thực tế thường thấy ở các dòng xe tải chở hàng cỡ lớn.
:::

::: info Khái niệm mấu chốt
Một động cơ nhiệt hấp thụ năng lượng dưới dạng nhiệt từ nguồn nóng, chuyển hóa một phần năng lượng đó thành công cơ học hữu ích, và thải phần năng lượng còn lại dưới dạng nhiệt ra nguồn lạnh. Tỷ phần nhiệt lượng từ nguồn nóng được chuyển hóa thành công cơ học được định nghĩa là hiệu suất nhiệt của động cơ.
:::

::: info Câu hỏi kiểm tra hiểu biết 20.2
Hãy sắp xếp các động cơ nhiệt sau theo thứ tự hiệu suất nhiệt từ cao nhất đến thấp nhất:

(i) Một động cơ trong mỗi chu trình hấp thụ $5000\,\mathrm{J}$ nhiệt lượng và thải ra $4500\,\mathrm{J}$ nhiệt lượng;
(ii) Một động cơ trong mỗi chu trình hấp thụ $25{,}000\,\mathrm{J}$ nhiệt lượng và thực hiện $2000\,\mathrm{J}$ công cơ học;
(iii) Một động cơ trong mỗi chu trình thực hiện $400\,\mathrm{J}$ công cơ học và thải ra $2800\,\mathrm{J}$ nhiệt lượng.

<details>
<summary>Xem lời giải thích</summary>

**Đáp án đúng**: Thứ tự từ cao nhất đến thấp nhất là (iii), (i), (ii).

**Giải thích chi tiết**:

Từ phương trình (20.4), hiệu suất nhiệt được tính bởi $e = W/Q_H$, với công hữu ích $W = |Q_H| - |Q_C|$.

Với động cơ (i): Ta có $Q_H = 5000\,\mathrm{J}$ và $Q_C = -4500\,\mathrm{J}$. Công cơ học thực hiện được là:

$$
\begin{aligned}
W &= 5000\,\mathrm{J} - 4500\,\mathrm{J} \\
&= 500\,\mathrm{J}
\end{aligned}
$$

Do đó hiệu suất nhiệt của động cơ (i) là:

$$
\begin{aligned}
e_{\text{(i)}} &= \frac{500\,\mathrm{J}}{5000\,\mathrm{J}} \\
&= 0{,}100 = 10{,}0\%
\end{aligned}
$$

Với động cơ (ii): Ta có $Q_H = 25{,}000\,\mathrm{J}$ và $W = 2000\,\mathrm{J}$. Hiệu suất nhiệt của động cơ (ii) là:

$$
\begin{aligned}
e_{\text{(ii)}} &= \frac{2000\,\mathrm{J}}{25{,}000\,\mathrm{J}} \\
&= 0{,}080 = 8{,}0\%
\end{aligned}
$$

Với động cơ (iii): Ta có $W = 400\,\mathrm{J}$ và nhiệt thải $|Q_C| = 2800\,\mathrm{J}$. Nhiệt lượng hấp thụ từ nguồn nóng là:

$$
\begin{aligned}
Q_H &= W + |Q_C| \\
&= 400\,\mathrm{J} + 2800\,\mathrm{J} \\
&= 3200\,\mathrm{J}
\end{aligned}
$$

Do đó hiệu suất nhiệt của động cơ (iii) là:

$$
\begin{aligned}
e_{\text{(iii)}} &= \frac{400\,\mathrm{J}}{3200\,\mathrm{J}} \\
&= 0{,}125 = 12{,}5\%
\end{aligned}
$$

So sánh các giá trị hiệu suất, ta có thứ tự sắp xếp là $e_{\text{(iii)}} > e_{\text{(i)}} > e_{\text{(ii)}}$, tương ứng với các giá trị $12{,}5\% > 10{,}0\% > 8{,}0\%$.
</details>
:::
