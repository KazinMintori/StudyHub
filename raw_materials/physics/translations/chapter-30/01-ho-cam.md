## 30.1. Hỗ cảm

Trong các bài học trước, ta đã khảo sát tương tác từ giữa hai dây dẫn thẳng song song mang dòng điện không đổi. Dòng điện trong dây dẫn thứ nhất tạo ra từ trường, và từ trường này tác dụng lực từ lên dòng điện trong dây dẫn thứ hai. Điều gì sẽ xảy ra nếu cường độ dòng điện trong các dây dẫn biến thiên theo thời gian? Khi đó, từ trường do dòng điện tạo ra sẽ biến đổi, làm xuất hiện hiện tượng cảm ứng điện từ giữa các mạch đặt gần nhau.

### Khái niệm hệ số hỗ cảm

Các đại lượng biến thiên theo thời gian được ký hiệu bằng chữ thường, chẳng hạn $i$ là dòng điện tức thời. Chỉ số dưới phân biệt mạch, như $i_1$ và $i_2$.

Xét hai cuộn dây dẫn đặt gần nhau như minh họa ở Hình 30.1. Một dòng điện $i_1$ chạy trong cuộn dây 1 có $N_1$ vòng dây sẽ tạo ra một từ trường $\vec{B}$. Các đường sức của từ trường này đi qua không gian lân cận và xuyên qua cuộn dây 2 có $N_2$ vòng dây, tạo nên một từ thông $\Phi_{B2}$ qua mỗi vòng của cuộn dây 2. Nếu từ thông qua các vòng dây không hoàn toàn như nhau, ta hiểu $\Phi_{B2}$ là giá trị từ thông trung bình trên một vòng dây của cuộn 2.

![Hình 30.1: Dòng i1 trong cuộn 1 tạo từ thông qua cuộn 2. Chỉ vẽ một nửa mỗi cuộn để thấy rõ các đường sức.](../img/young-30/hinh-30-01.png)

Khi dòng điện $i_1$ biến thiên theo thời gian, từ thông $\Phi_{B2}$ cũng thay đổi tương ứng. Theo định luật cảm ứng Faraday, sự biến thiên từ thông này làm xuất hiện trong cuộn dây 2 một suất điện động cảm ứng $\mathcal{E}_2$:

$$
\mathcal{E}_2 = -N_2 \frac{d\Phi_{B2}}{dt} \tag{30.1}
$$

Trong chân không hoặc trong môi trường không có vật liệu từ tính phi tuyến, cảm ứng từ $\vec{B}$ tại mỗi điểm tỉ lệ thuận với dòng điện $i_1$ sinh ra nó. Kéo theo đó, từ thông $\Phi_{B2}$ qua mỗi vòng của cuộn 2 cũng tỉ lệ thuận với $i_1$. Đại lượng $N_2 \Phi_{B2}$ được gọi là **từ thông móc vòng** qua toàn bộ cuộn dây 2. Ta biểu diễn mối quan hệ tỉ lệ này bằng phương trình:

$$
N_2 \Phi_{B2} = M_{21} i_1 \tag{30.2}
$$

Hệ số $M_{21}$ được gọi là **hỗ cảm** của cuộn 2 đối với cuộn 1. Giữ vị trí, hướng các cuộn và độ từ thẩm không đổi để $M_{21}$ không phụ thuộc thời gian. Lấy đạo hàm (30.2), ta được:

$$
N_2 \frac{d\Phi_{B2}}{dt} = M_{21} \frac{di_1}{dt}
$$

Kết hợp với định luật Faraday ở phương trình (30.1), ta thu được biểu thức của suất điện động cảm ứng trong cuộn 2:

$$
\mathcal{E}_2 = -M_{21} \frac{di_1}{dt} \tag{30.3}
$$

Phương trình này chỉ rõ: Suất điện động cảm ứng xuất hiện trong cuộn 2 tỉ lệ thuận với tốc độ biến thiên của dòng điện trong cuộn 1, chứ không phụ thuộc vào độ lớn tức thời của dòng điện đó.

### Tính đối xứng của hệ số hỗ cảm

Bây giờ, ta đảo ngược vai trò của hai cuộn dây. Giả sử ta cho một dòng điện biến thiên $i_2$ chạy qua cuộn dây 2. Dòng điện này tạo ra một từ trường biến thiên, làm xuất hiện từ thông $\Phi_{B1}$ qua mỗi vòng của cuộn dây 1. Lập luận hoàn toàn tương tự, từ thông móc vòng qua cuộn 1 tỉ lệ với $i_2$ theo hệ số hỗ cảm $M_{12}$:

$$
N_1 \Phi_{B1} = M_{12} i_2
$$

Khi đó, suất điện động cảm ứng xuất hiện trong cuộn 1 là:

$$
\mathcal{E}_1 = -M_{12} \frac{di_2}{dt}
$$

Từ các định luật điện từ tổng quát, người ta chứng minh được rằng đối với hai cuộn dây bất kỳ đặt trong chân không hoặc trong môi trường vật chất có độ từ thẩm không đổi, hai hệ số hỗ cảm $M_{12}$ và $M_{21}$ luôn luôn bằng nhau:

$$
M_{12} = M_{21} = M
$$

Tính chất đối xứng này luôn nghiệm đúng, bất kể hai cuộn dây có hình dạng, kích thước hoặc số vòng dây khác nhau đến mức nào. Vì vậy, ta chỉ cần dùng một ký hiệu chung $M$ cho hệ số hỗ cảm giữa hai cuộn dây. Khi đó, các suất điện động hỗ cảm trong hai cuộn được viết là:

$$
\begin{aligned}
\mathcal{E}_2 &= -M \frac{di_1}{dt} \\
\mathcal{E}_1 &= -M \frac{di_2}{dt}
\end{aligned} \tag{30.4}
$$

Dấu âm trong các phương trình (30.4) thể hiện nội dung của định luật Lenz: Chiều của suất điện động cảm ứng luôn chống lại sự biến thiên của dòng điện đã sinh ra nó. Từ định nghĩa trên, ta có biểu thức đối xứng của hệ số hỗ cảm $M$:

$$
M = \frac{N_2 \Phi_{B2}}{i_1} = \frac{N_1 \Phi_{B1}}{i_2} \tag{30.5}
$$

Lưu ý: Đẳng thức (30.5) không đồng nghĩa với việc hai từ thông $\Phi_{B1}$ và $\Phi_{B2}$ bằng nhau. Hai cuộn dây có thể có cấu hình hình học và số vòng dây rất khác nhau, nhưng tích số giữa số vòng dây và từ thông trên mỗi đơn vị dòng điện của hai cuộn thì luôn bằng nhau.

### Đơn vị và các yếu tố quyết định hệ số hỗ cảm

Từ phương trình (30.5), đơn vị đo của hệ số hỗ cảm trong hệ SI là weber trên ampe ($\text{Wb/A}$). Đơn vị này được đặt tên là **henry** (ký hiệu là $\text{H}$) để vinh danh nhà vật lý người Mỹ Joseph Henry (1797–1878), một trong những người phát hiện hiện tượng cảm ứng điện từ:

$$
\begin{aligned}
1\text{ H} &= 1\text{ Wb/A} \\
&= 1\text{ V}\cdot\text{s/A} \\
&= 1\ \Omega\cdot\text{s} \\
&= 1\text{ J/A}^2
\end{aligned}
$$

Trong các mạch điện và thiết bị thông dụng, độ hỗ cảm thường có giá trị cỡ millihenry ($\text{mH}$, $1\text{ mH} = 10^{-3}\text{ H}$) hoặc microhenry ($\mu\text{H}$, $1\ \mu\text{H} = 10^{-6}\text{ H}$).

Đối với các mạch đặt trong chân không hoặc trong môi trường không có tính chất từ, hệ số hỗ cảm $M$ là một hằng số hình học thuần túy. Giá trị của $M$ phụ thuộc vào kích thước, hình dạng, số vòng dây của từng cuộn, cũng như khoảng cách và hướng định vị tương đối giữa hai cuộn dây. Nếu ta tăng khoảng cách giữa hai cuộn hoặc xoay chúng sao cho các trục vuông góc với nhau, từ thông móc vòng giữa chúng sẽ giảm, dẫn đến hệ số hỗ cảm $M$ giảm.

Nếu có vật liệu từ giữa hai cuộn, hỗ cảm còn phụ thuộc tính chất của vật liệu. Khi độ từ thẩm không còn không đổi và sự từ hóa không tỉ lệ với trường, từ thông không còn tỉ lệ với dòng. Khi ấy hỗ cảm phụ thuộc cả giá trị dòng điện. Trong các phân tích tiếp theo, ta giả định vật liệu tuyến tính với độ từ thẩm không đổi.

Lưu ý: Chỉ có dòng điện biến thiên theo thời gian mới gây ra suất điện động cảm ứng. Một dòng điện không đổi dù có cường độ rất lớn cũng chỉ tạo ra một từ trường tĩnh, do đó không làm phát sinh suất điện động trong cuộn dây lân cận. Suất điện động cảm ứng phụ thuộc trực tiếp vào đạo hàm $di/dt$, không phụ thuộc vào giá trị tức thời của dòng điện.

### Ứng dụng thực tế của hiện tượng hỗ cảm

Hỗ cảm có thể gây suất điện động không mong muốn trong các mạch đặt gần nhau. Để giảm tác dụng này, hệ thống nhiều mạch cần được bố trí để hỗ cảm nhỏ, chẳng hạn đặt các cuộn cách xa nhau.

Máy biến áp dùng cùng nguyên lý ghép từ giữa hai cuộn. Dòng xoay chiều ở một cuộn gây suất điện động xoay chiều ở cuộn kia. Hỗ cảm, được quyết định bởi cấu hình hai cuộn và môi trường từ, liên hệ tốc độ biến thiên dòng đầu vào với biên độ suất điện động đầu ra. Cách phân tích máy biến áp sẽ được phát triển ở chương dòng xoay chiều.

Bàn chải điện ở Hình 30.2 có một cuộn nối với pin, còn đế sạc có cuộn được cấp dòng xoay chiều từ ổ điện. Dù hai phần không tiếp xúc điện trực tiếp, từ thông biến thiên vẫn gây suất điện động trong cuộn của bàn chải và nạp lại pin.

![Hình 30.2: Bàn chải đánh răng điện ứng dụng hiện tượng hỗ cảm để sạc pin không cần tiếp xúc kim loại.](../img/young-30/hinh-30-02.png)

![Hình 30.3: Một ống dây dài có diện tích tiết diện A và N1 vòng dây được bọc ngoài bởi một cuộn dây ngắn có N2 vòng dây.](../img/young-30/hinh-30-03.png)

::: example Ví dụ 30.1: Tính hệ số hỗ cảm của ống dây dài và cuộn dây ngoài
Xét một mô hình máy phát cao áp dạng cuộn Tesla: Ống dây dài 1 có chiều dài $l$, diện tích tiết diện thẳng $A$, gồm $N_1$ vòng dây quấn đều. Quanh phần giữa của ống dây này, người ta quấn thêm một cuộn dây 2 gồm $N_2$ vòng dây ôm sát bên ngoài như minh họa ở Hình 30.3. Giả sử môi trường bên trong ống dây là chân không. Hãy tìm hệ số hỗ cảm giữa hai cuộn dây. Áp dụng bằng số với $l = 0{,}50\text{ m}$, $A = 10\text{ cm}^2 = 1{,}0 \times 10^{-3}\text{ m}^2$, $N_1 = 1000$ vòng và $N_2 = 10$ vòng.

**Phân tích bài toán**:
Ống dây 1 có chiều dài $l$ lớn hơn nhiều so với bán kính tiết diện, cho phép ta áp dụng mô hình ống dây dài lý tưởng. Khi đó, từ trường bên ngoài ống dây coi như bằng không, còn từ trường bên trong phân bố đều trên toàn bộ tiết diện và có độ lớn xác định theo công thức:

$$
B_1 = \mu_0 \frac{N_1}{l} i_1
$$

Vì cuộn dây 2 ôm quanh phần giữa của ống dây 1, toàn bộ từ thông sinh ra bởi dòng điện $i_1$ bên trong tiết diện $A$ của ống dây 1 đều đi qua mỗi vòng của cuộn dây 2.

**Các bước tính toán**:
Từ thông qua mỗi vòng của cuộn dây 2 là:

$$
\Phi_{B2} = B_1 A = \mu_0 \frac{N_1 A}{l} i_1
$$

Áp dụng định nghĩa hệ số hỗ cảm từ phương trình (30.5):

$$
M = \frac{N_2 \Phi_{B2}}{i_1} = \frac{\mu_0 A N_1 N_2}{l}
$$

Biểu thức cho thấy $M$ tỉ lệ với tích số vòng $N_1N_2$, đồng thời phụ thuộc hình học và môi trường đã cố định. Trong mô hình tuyến tính này, $M$ không phụ thuộc độ lớn dòng. Trước hết tính hai thừa số:

$$
\frac{\mu_0}{l}=8\pi\times10^{-7}\,\frac{\mathrm H}{\mathrm{m^2}},
$$

$$
\begin{aligned}
AN_1N_2&=(1{,}0\times10^{-3})(10^4)\,\mathrm{m^2}\\
&=10\,\mathrm{m^2}.
\end{aligned}
$$

Nhân hai kết quả:

$$
\begin{aligned}
M &= \frac{\mu_0 A N_1 N_2}{l} \\
&=(8\pi)(10)\times10^{-7}\,\mathrm H\\
&= 2{,}513 \times 10^{-5}\text{ H} \\
&\approx 25\ \mu\text{H}
\end{aligned}
$$

Kết quả thu được là $M \approx 25\ \mu\text{H}$, tức là $25 \times 10^{-6}\text{ H}$.
:::

::: example Ví dụ 30.2: Suất điện động do hiện tượng hỗ cảm gây ra
Trong cấu hình của Ví dụ 30.1, cho dòng chạy qua cuộn ngoài 2 và tăng theo $i_2 = (2{,}0 \times 10^6\text{ A/s})t$. Dòng trong dây có thể tăng nhanh như vậy trong những khoảng thời gian ngắn.
1. Tại thời điểm $t = 3{,}0\ \mu\text{s}$, hãy xác định từ thông trung bình $\Phi_{B1}$ qua mỗi vòng của ống dây trong 1.
2. Tìm suất điện động cảm ứng xuất hiện trong ống dây 1.

**Phân tích bài toán**:
Ta đã biết hệ số hỗ cảm của hệ cuộn dây là $M = 25\ \mu\text{H}$. Nhờ tính đối xứng của hiện tượng hỗ cảm, khi dòng điện biến thiên ở cuộn ngoài 2, ta có thể dùng trực tiếp giá trị $M$ này để tính từ thông móc vòng và suất điện động cảm ứng xuất hiện ở ống dây trong 1.

**Các bước tính toán**:
1. Tại thời điểm $t = 3{,}0\ \mu\text{s} = 3{,}0 \times 10^{-6}\text{ s}$, cường độ dòng điện tức thời ở cuộn dây 2 là:

$$
\begin{aligned}
i_2 &= (2{,}0)(3{,}0)\times10^{6-6}\,\mathrm A\\
&= 6{,}0\text{ A}
\end{aligned}
$$

Áp dụng hệ thức đối xứng của độ hỗ cảm theo phương trình (30.5), ta có:

$$
\begin{aligned}
N_1 \Phi_{B1} &= M i_2 \\
\implies \Phi_{B1} &= \frac{M i_2}{N_1}
\end{aligned}
$$

Thay các giá trị $M = 25 \times 10^{-6}\text{ H}$, $i_2 = 6{,}0\text{ A}$ và $N_1 = 1000$ vòng vào:

$$
\begin{aligned}
\Phi_{B1} &= \frac{M i_2}{N_1} \\
&=\frac{(25)(6{,}0)}{1000}\times10^{-6}\,\mathrm{Wb}\\
&= 1{,}5 \times 10^{-7}\text{ Wb}
\end{aligned}
$$

Đây là từ thông trung bình trên mỗi vòng. Từ thông thực có thể khác nhau đáng kể giữa các vòng ở giữa và ở hai đầu ống dây.

2. Tốc độ biến thiên của dòng điện trong cuộn 2 là hằng số:

$$
\frac{di_2}{dt} = 2{,}0 \times 10^6\text{ A/s}
$$

Suất điện động cảm ứng xuất hiện trong ống dây 1 được xác định theo phương trình (30.4):

$$
\begin{aligned}
\mathcal{E}_1 &= -M \frac{di_2}{dt} \\
&=-(25)(2{,}0)\times10^{-6+6}\,\mathrm V\\
&= -50\text{ V}
\end{aligned}
$$

Dấu âm cho biết suất điện động cảm ứng chống sự tăng từ thông theo định luật Lenz. Độ lớn là $50\text{ V}$. Trong cuộn Tesla đang vận hành, dòng có dạng xoay chiều tần số cao thay vì tăng liên tục. Khi ấy đạo hàm dòng và suất điện động đều đổi dấu, với biên độ có thể lớn hơn hàng nghìn lần giá trị của ví dụ này.
:::

### Câu hỏi ôn tập mục 30.1

Xét ống dây solenoid mô tả trong Ví dụ 30.1. Giả sử ta quấn lại ống dây trong bằng một đoạn dây có chiều dài gấp đôi. Ống dây mới có số vòng dây tăng gấp đôi ($2N_1$) và chiều dài cũng tăng gấp đôi ($2l$), trong khi diện tích tiết diện $A$ và số vòng dây $N_2$ của cuộn ngoài giữ nguyên. Khi đó, hệ số hỗ cảm $M$ giữa hai cuộn dây sẽ thay đổi như thế nào?

(i) $M$ tăng gấp bốn lần.

(ii) $M$ tăng gấp đôi.

(iii) $M$ không đổi.

(iv) $M$ giảm đi một nửa.

(v) $M$ giảm còn một phần tư.

<details><summary>Xem đáp án và giải thích</summary>

Chọn (iii). Theo kết quả đã dẫn ra ở Ví dụ 30.1, hệ số hỗ cảm của hệ hai cuộn dây có dạng:

$$
\begin{aligned}
M &= \frac{\mu_0 A N_1 N_2}{l} \\
&= \mu_0 A \left(\frac{N_1}{l}\right) N_2
\end{aligned}
$$

Biểu thức này cho thấy hệ số hỗ cảm tỉ lệ trực tiếp với mật độ số vòng dây trên một đơn vị chiều dài của ống dây trong, tức là tỉ số $n_1 = N_1 / l$. Khi cả số vòng dây và chiều dài của ống dây đều tăng lên hai lần, tỉ số này trở thành $(2N_1)/(2l) = N_1/l$, tức là mật độ vòng dây không thay đổi. Vì diện tích tiết diện $A$ và số vòng dây $N_2$ của cuộn ngoài cũng được giữ nguyên, từ trường do ống dây trong tạo ra trên mỗi đơn vị dòng điện vẫn không đổi, kéo theo từ thông gửi qua mỗi vòng cuộn ngoài không đổi. Do đó, hệ số hỗ cảm $M$ giữa hai cuộn dây hoàn toàn không thay đổi.

</details>
