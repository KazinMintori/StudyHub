<!-- Source: Section20.7, printed659–665, PDF679–685. -->

## 20.7. Entropy

Nguyên lý thứ hai nhiệt động lực học, khi được diễn đạt dưới các phát biểu của Kelvin–Planck và Clausius, là những khẳng định về tính bất khả thi mang tính định tính. Để chuyển hóa nguyên lý thứ hai thành một công cụ toán học định lượng có thể đo đạc và tính toán chính xác, ta cần đến một hàm trạng thái nhiệt động mới: **entropy**.

### Khái niệm entropy và tính một chiều của tự nhiên

Mọi quá trình tự nhiên diễn ra một cách tự phát đều có xu hướng biến đổi từ trạng thái có trật tự cao sang trạng thái có độ hỗn loạn (randomness / disorder) lớn hơn. Khi một khối nước đá tan chảy thành nước lỏng, cấu trúc tinh thể mạng lưới ngăn nắp của các phân tử nước bị phá vỡ để chuyển thành sự chuyển động hỗn loạn, xáo trộn của chất lỏng. Khi một quả pháo nổ (Hình 20.17), các chất hóa học được đóng gói cẩn thận bên trong lớp vỏ bị phân tán ngẫu nhiên ra mọi hướng trong không gian, và năng lượng hóa học dự trữ bị phân tán thành nội năng nhiệt truyền vào không khí xung quanh.

![Hình 20.17: Sự nổ pháo hoa phân tán các chất hóa học làm tăng tính hỗn loạn của hệ](../img/young-20/b-hinh-20-17.png)

*Hình 20.17: Khi pháo phát nổ, tính hỗn loạn của hệ tăng lên rõ rệt. Các hóa chất được nén gọn gàng bên trong quả pháo bị bắn tung tóe ra khắp các hướng, đồng thời năng lượng hóa học được giải phóng và phân tán ngẫu nhiên vào không khí xung quanh.*

Entropy là đại lượng vật lý dùng để đo mức độ hỗn loạn của một hệ nhiệt động. Mức độ hỗn loạn của hệ càng cao thì giá trị entropy của hệ càng lớn.

### Định nghĩa định lượng của entropy

Xét một quá trình nhiệt động vô cùng nhỏ mà trong đó hệ trao đổi một nhiệt lượng vô cùng bé $dQ$ với môi trường ở nhiệt độ tuyệt đối $T$. Nếu quá trình này là hoàn toàn thuận nghịch, độ biến thiên entropy vi phân $dS$ của hệ được định nghĩa là:

$$
dS = \frac{dQ}{T}
$$

Đơn vị đo của entropy trong hệ SI là jun trên kelvin ($\mathrm{J/K}$).

Nếu hệ thực hiện một quá trình đẳng nhiệt thuận nghịch ở nhiệt độ tuyệt đối không đổi $T$, tích phân cho ta độ biến thiên entropy hữu hạn:

$$
\begin{aligned}
\Delta S &= S_2 - S_1 \\
&= \frac{Q}{T}
\end{aligned}
$$

Trong đó:
- Nếu hệ nhận nhiệt từ môi trường ($Q > 0$): Entropy của hệ tăng lên ($\Delta S > 0$), tương ứng với việc các phân tử nhận thêm năng lượng chuyển động nhiệt và trở nên hỗn loạn hơn.
- Nếu hệ nhả nhiệt ra môi trường ($Q < 0$): Entropy của hệ giảm đi ($\Delta S < 0$), hệ trở nên trật tự hơn.

Đối với một quá trình thuận nghịch bất kỳ từ trạng thái 1 đến trạng thái 2 mà nhiệt độ $T$ thay đổi liên tục, độ biến thiên entropy tổng cộng được tính bằng tích phân dọc theo đường quá trình thuận nghịch:

$$
\begin{aligned}
\Delta S &= S_2 - S_1 \\
&= \int_1^2 \frac{dQ}{T}
\end{aligned}
$$

::: example Ví dụ 20.5: Biến thiên entropy khi làm nóng chảy nước đá
Tính độ biến thiên entropy của $1{,}00\,\mathrm{kg}$ nước đá tan chảy thuận nghịch ở nhiệt độ $0^\circ\mathrm C$ để chuyển thành nước lỏng ở cùng nhiệt độ $0^\circ\mathrm C$. Nhiệt nóng chảy riêng của nước đá là $L_f = 3{,}34 \times 10^5\,\mathrm{J/kg}$.

**Tóm tắt**:
- $m = 1{,}00\,\mathrm{kg}$
- $T = 0^\circ\mathrm C = 273\,\mathrm K$
- $L_f = 3{,}34 \times 10^5\,\mathrm{J/kg}$

**Hướng đi**:
- Quá trình chuyển pha diễn ra ở nhiệt độ không đổi $T = 273\,\mathrm K$, do đó đây là quá trình đẳng nhiệt thuận nghịch.
- Tính nhiệt lượng cần cung cấp để làm nóng chảy hoàn toàn khối đá: $Q = m L_f$.
- Áp dụng công thức biến thiên entropy cho quá trình đẳng nhiệt.

**Các bước tính toán**:
Nhiệt lượng cung cấp cho khối đá là:

$$
\begin{aligned}
Q &= m L_f \\
&= (1{,}00)(3{,}34 \times 10^5) \\
&= 3{,}34 \times 10^5\,\mathrm J
\end{aligned}
$$

Độ biến thiên entropy của nước đá khi nóng chảy là:

$$
\begin{aligned}
\Delta S &= \frac{Q}{T} \\
&= \frac{3{,}34 \times 10^5\,\mathrm J}{273\,\mathrm K} \\
&= 1{,}22 \times 10^3\,\mathrm{J/K}
\end{aligned}
$$

**Đánh giá kết quả**:
Entropy tăng thêm $1{,}22 \times 10^3\,\mathrm{J/K}$ phản ánh sự chuyển đổi trạng thái từ mạng tinh thể chất rắn có cấu trúc ngăn nắp sang trạng thái chất lỏng có độ hỗn loạn cao hơn rất nhiều.
Nếu ta làm đông đặc lượng nước lỏng này trở lại thành nước đá ở $0^\circ\mathrm C$, nhiệt lượng nhả ra là $Q = -3{,}34 \times 10^5\,\mathrm J$, dẫn đến độ biến thiên entropy là $\Delta S = -1{,}22 \times 10^3\,\mathrm{J/K}$. Các phân tử sắp xếp lại thành mạng tinh thể, độ hỗn loạn và entropy của nước đều giảm.
:::

::: example Ví dụ 20.6: Biến thiên entropy khi nhiệt độ thay đổi
Một kilôgam nước ở $0^\circ\mathrm C$ được đun nóng đến $100^\circ\mathrm C$. Hãy tính độ biến thiên entropy của khối nước. Giả thiết nhiệt dung riêng của nước không đổi trong khoảng nhiệt độ này và bằng $c = 4190\,\mathrm{J/(kg\cdot K)}$.

**Tóm tắt**:
- $m = 1{,}00\,\mathrm{kg}$
- $T_1 = 0^\circ\mathrm C = 273\,\mathrm K$
- $T_2 = 100^\circ\mathrm C = 373\,\mathrm K$
- $c = 4190\,\mathrm{J/(kg\cdot K)}$

**Hướng đi**:
- Trong quá trình đun nóng, nhiệt độ tăng liên tục từ $T_1$ đến $T_2$.
- Nhiệt lượng vi phân cung cấp cho khối nước khi nhiệt độ tăng thêm $dT$ là $dQ = m c dT$.
- Tích phân từ $T_1$ đến $T_2$.

**Các bước tính toán**:
Thay biểu thức vi phân nhiệt lượng vào công thức định nghĩa entropy:

$$
\begin{aligned}
\Delta S &= \int_{T_1}^{T_2} \frac{m c dT}{T} \\
&= m c \ln \frac{T_2}{T_1}
\end{aligned}
$$

Thay các giá trị số $m = 1{,}00\,\mathrm{kg}$, $c = 4190\,\mathrm{J/(kg\cdot K)}$, $T_1 = 273\,\mathrm K$, $T_2 = 373\,\mathrm K$:

$$
\begin{aligned}
\Delta S &= (4190\,\mathrm{J/K})\ln \frac{373}{273} \\
&= 1{,}31 \times 10^3\,\mathrm{J/K}
\end{aligned}
$$

**Đánh giá kết quả**:
Độ biến thiên entropy mang dấu dương vì khối nước nhận nhiệt lượng từ nguồn bên ngoài. Khi nhiệt độ tăng, tốc độ chuyển động nhiệt của các phân tử nước tăng lên, làm mức độ hỗn loạn trong chuyển động của các phân tử gia tăng.
:::

::: example Ví dụ 20.7: Biến thiên entropy trong quá trình đoạn nhiệt thuận nghịch
Một khối khí giãn nở đoạn nhiệt thuận nghịch. Hãy xác định độ biến thiên entropy của khối khí trong quá trình này.

**Giải thích bản chất vật lý**:
Trong một quá trình đoạn nhiệt, hệ hoàn toàn không trao đổi nhiệt lượng với môi trường xung quanh, do đó $dQ = 0$ tại mọi thời điểm biến đổi.
Vì quá trình là thuận nghịch, ta có thể áp dụng trực tiếp định nghĩa entropy:

$$
dS = \frac{dQ}{T} = 0
$$

Từ đó suy ra $\Delta S = 0$. Mọi quá trình đoạn nhiệt thuận nghịch đều là **quá trình đẳng entropy** (isentropic process). Trong quá trình này, sự gia tăng mức độ hỗn loạn do thể tích khối khí mở rộng được bù trừ chính xác bởi sự suy giảm mức độ hỗn loạn do nhiệt độ hạ thấp và tốc độ chuyển động của các phân tử giảm đi.
:::

::: example Ví dụ 20.8: Biến thiên entropy trong quá trình giãn nở tự do
Một vách ngăn phân chia một hộp cách nhiệt lý tưởng thành hai ngăn có thể tích bằng nhau và bằng $V$ (Hình 20.18). Ban đầu, một ngăn chứa $n\,\mathrm{mol}$ khí lý tưởng ở nhiệt độ $T$, còn ngăn kia là chân không. Ta phá vỡ vách ngăn để chất khí giãn nở tự do, chiếm trọn toàn bộ thể tích $2V$ của hộp. Hãy tính độ biến thiên entropy của khối khí.

**Tóm tắt**:
- Khí lý tưởng: $n\,\mathrm{mol}$
- Trạng thái đầu: $V_1 = V$, nhiệt độ $T$
- Trạng thái cuối: $V_2 = 2V$, nhiệt độ $T$

**Hướng đi**:
- Vì hộp cách nhiệt lý tưởng nên $Q = 0$. Khí giãn vào chân không không gặp lực cản nên không sinh công ngoại lực ($W = 0$).
- Theo nguyên lý thứ nhất, biến thiên nội năng $\Delta U = Q - W = 0$. Vì là khí lý tưởng, nội năng chỉ phụ thuộc nhiệt độ nên nhiệt độ không đổi: $\Delta T = 0$, nhiệt độ cuối vẫn là $T$.
- Quá trình giãn nở tự do là không thuận nghịch nên ta không thể áp dụng trực tiếp $\int dQ/T$ cho đường đi thực tế.
- Entropy là hàm trạng thái: Biến thiên entropy giữa hai trạng thái chỉ phụ thuộc vào trạng thái đầu và cuối. Do đó, ta thay thế quá trình thực tế bằng một **quá trình giãn nở đẳng nhiệt thuận nghịch** ở nhiệt độ $T$ từ thể tích $V$ đến $2V$.

![Hình 20.18: Giãn nở tự do của khối khí cách nhiệt và quá trình đẳng nhiệt thuận nghịch thay thế](../img/young-20/b-hinh-20-18.png)

*Hình 20.18: (a, b) Giãn nở tự do của khối khí lý tưởng trong hộp cách nhiệt. (c) Quá trình giãn nở tự do không đi qua các trạng thái cân bằng từ $a$ đến $b$ (đường nét đứt). Tuy nhiên, độ biến thiên entropy $S_b - S_a$ có thể được tính chính xác bằng cách sử dụng đường đẳng nhiệt thuận nghịch đi từ $a$ đến $b$ (đường nét liền).*

**Các bước tính toán**:
Xét quá trình đẳng nhiệt thuận nghịch từ $V$ đến $2V$ ở nhiệt độ $T$, công do khối khí sinh ra là:

$$
\begin{aligned}
W &= n R T \ln \frac{V_2}{V_1} \\
&= n R T \ln 2
\end{aligned}
$$

Để giữ nhiệt độ không đổi trong quá trình giãn đẳng nhiệt, nhiệt lượng cung cấp cho khối khí phải bằng đúng công sinh ra:

$$
Q = W = n R T \ln 2
$$

Áp dụng công thức biến thiên entropy cho quá trình đẳng nhiệt thuận nghịch thay thế:

$$
\begin{aligned}
\Delta S &= \frac{Q}{T} \\
&= n R \ln 2
\end{aligned}
$$

**Đánh giá kết quả**:
Mặc dù trong quá trình giãn nở tự do thực tế không hề có nhiệt lượng trao đổi ($Q = 0$), entropy của khối khí vẫn tăng lên một lượng $\Delta S = n R \ln 2 > 0$. Điều này hoàn toàn phù hợp với trực giác vật lý: Sau khi giãn nở, thể tích tăng gấp đôi khiến các phân tử khí có vùng không gian chuyển động rộng hơn, làm mức độ hỗn loạn về vị trí của các phân tử tăng lên rõ rệt.
:::

::: example Ví dụ 20.9: Entropy và chu trình Carnot
Đối với động cơ Carnot trong Ví dụ 20.2, hãy tính tổng độ biến thiên entropy của chất tác công trong một chu trình hoạt động hoàn chỉnh.

**Tóm tắt**:
- $Q_H = 2000\,\mathrm J$; $T_H = 500\,\mathrm K$
- $Q_C = -1400\,\mathrm J$; $T_C = 350\,\mathrm K$

**Hướng đi**:
- Mọi giai đoạn trong chu trình Carnot đều là thuận nghịch.
- Tính biến thiên entropy cho từng giai đoạn và cộng lại để tìm độ biến thiên entropy tổng cộng.

**Các bước tính toán**:
- Trong hai giai đoạn đoạn nhiệt ($b \to c$ và $d \to a$), $dQ = 0$ nên $\Delta S_{bc} = 0$ và $\Delta S_{da} = 0$.
- Trong giai đoạn giãn đẳng nhiệt $a \to b$ ở nhiệt độ $T_H = 500\,\mathrm K$, động cơ nhận nhiệt lượng $Q_H = 2000\,\mathrm J$:

$$
\begin{aligned}
\Delta S_H &= \frac{Q_H}{T_H} \\
&= \frac{2000\,\mathrm J}{500\,\mathrm K} \\
&= +4{,}0\,\mathrm{J/K}
\end{aligned}
$$

- Trong giai đoạn nén đẳng nhiệt $c \to d$ ở nhiệt độ $T_C = 350\,\mathrm K$, động cơ nhả nhiệt lượng $Q_C = -1400\,\mathrm J$:

$$
\begin{aligned}
\Delta S_C &= \frac{Q_C}{T_C} \\
&= \frac{-1400\,\mathrm J}{350\,\mathrm K} \\
&= -4{,}0\,\mathrm{J/K}
\end{aligned}
$$

- Tổng độ biến thiên entropy của chất tác công sau một chu trình kín:

$$
\begin{aligned}
\Delta S &= \Delta S_H + \Delta S_C \\
&= 4{,}0 - 4{,}0 = 0
\end{aligned}
$$

**Đánh giá kết quả**:
Kết quả $\Delta S_{\text{chu trình}} = 0$ khẳng định rằng sau một chu trình tuần hoàn kín, chất tác công quay trở lại trạng thái ban đầu và entropy của nó hoàn toàn không thay đổi.
:::

### Entropy trong chu trình thuận nghịch và hàm trạng thái

Từ tỷ số nhiệt lượng chu trình Carnot, ta có mối liên hệ:

$$
\frac{Q_H}{T_H} + \frac{Q_C}{T_C} = 0
$$

Tổng độ biến thiên entropy của chất tác công trong chu trình Carnot luôn bằng không.

Kết quả này có thể tổng quát hóa cho một chu trình thuận nghịch bất kỳ biểu diễn bởi đường cong kín trên đồ thị $p-V$ (Hình 20.19a). Ta có thể chia nhỏ diện tích bên trong chu trình thành một lưới gồm rất nhiều chu trình Carnot con ghép sát nhau (Hình 20.19b). Khi số lượng chu trình Carnot tiến tới vô hạn, các đường dích dắc của các chu trình con sẽ tiệm cận chính xác đường bao của chu trình thực tế.

![Hình 20.19: Chia chu trình thuận nghịch thành các chu trình Carnot và tính độc lập đường đi của entropy](../img/young-20/b-hinh-20-19.png)

*Hình 20.19: (a) Một chu trình thuận nghịch của khí lý tưởng biểu diễn bởi đường cong khép kín trên đồ thị $p-V$. (b) Xấp xỉ chu trình thuận nghịch bằng một chuỗi các chu trình Carnot con. (c) Hai đường đi thuận nghịch khác nhau (đường 1 và đường 2) nối từ trạng thái $a$ đến trạng thái $b$: Độ biến thiên entropy $S_b - S_a$ hoàn toàn như nhau trên cả hai đường.*

Lấy tổng tích phân cho toàn bộ các chu trình con, ta thu được định lý Clausius cho chu trình thuận nghịch kín:

$$
\oint \frac{dQ}{T} = 0
$$

Hệ thức trên áp dụng cho một chu trình thuận nghịch kín bất kỳ. Tích phân của nhiệt thuận nghịch chia nhiệt độ chỉ phụ thuộc hai trạng thái đầu và cuối. Vì vậy, **entropy $S$ là một hàm trạng thái của hệ**, không phụ thuộc đường biến đổi đã đưa hệ đến trạng thái đó (Hình 20.19c):

$$
\begin{aligned}
\Delta S &= \int_{a (1)}^b \frac{dQ}{T} \\
&= S_b - S_a
\end{aligned}
$$

### Biến thiên entropy trong các quá trình không thuận nghịch

Trong thực tế, đa số các quá trình nhiệt động diễn ra tự nhiên đều là quá trình không thuận nghịch. Do entropy là hàm trạng thái, để tính độ biến thiên entropy của một hệ trải qua một quá trình không thuận nghịch từ trạng thái 1 đến trạng thái 2, ta luôn thực hiện theo quy tắc:
1. Xác định chính xác trạng thái đầu (1) và trạng thái cuối (2) của hệ.
2. Thiết kế một quá trình thuận nghịch tưởng tượng bất kỳ nối trạng thái 1 với trạng thái 2.
3. Tính tích phân $\int_1^2 dQ/T$ dọc theo con đường thuận nghịch tưởng tượng đó.

::: example Ví dụ 20.10: Biến thiên entropy trong truyền nhiệt không thuận nghịch
Cho $1{,}00\,\mathrm{kg}$ nước ở $100^\circ\mathrm C$ tiếp xúc nhiệt trực tiếp với $1{,}00\,\mathrm{kg}$ nước ở $0^\circ\mathrm C$ bên trong một bình cách nhiệt lý tưởng. Hãy tính tổng độ biến thiên entropy của hệ sau khi đạt trạng thái cân bằng nhiệt. Lấy nhiệt dung riêng của nước không đổi $c = 4190\,\mathrm{J/(kg\cdot K)}$.

**Tóm tắt**:
- $m_1 = 1{,}00\,\mathrm{kg}$; $T_{\text{nóng}} = 100^\circ\mathrm C = 373\,\mathrm K$
- $m_2 = 1{,}00\,\mathrm{kg}$; $T_{\text{lạnh}} = 0^\circ\mathrm C = 273\,\mathrm K$
- $c = 4190\,\mathrm{J/(kg\cdot K)}$

**Hướng đi**:
- Vì hai khối nước có khối lượng bằng nhau và bình cách nhiệt, nhiệt độ cân bằng cuối cùng là trung bình cộng:

$$
\begin{aligned}
T_{\text{cb}} &= \frac{373\,\mathrm K + 273\,\mathrm K}{2} \\
&= 323\,\mathrm K = 50^\circ\mathrm C
\end{aligned}
$$

- Sự truyền nhiệt trực tiếp giữa hai khối nước chênh lệch nhiệt độ lớn là quá trình không thuận nghịch.
- Để tính biến thiên entropy, ta giả tưởng làm nguội khối nước nóng thuận nghịch từ $373\,\mathrm K$ xuống $323\,\mathrm K$, và đun nóng khối nước lạnh thuận nghịch từ $273\,\mathrm K$ lên $323\,\mathrm K$.

**Các bước tính toán**:
Độ biến thiên entropy của khối nước nóng (với $m = 1{,}00\,\mathrm{kg}$, $c = 4190\,\mathrm{J/(kg\cdot K)}$):

$$
\begin{aligned}
\Delta S_{\text{nóng}} &= \int_{373}^{323} \frac{m c dT}{T} \\
&= -603\,\mathrm{J/K}
\end{aligned}
$$

Độ biến thiên entropy của khối nước lạnh:

$$
\begin{aligned}
\Delta S_{\text{lạnh}} &= \int_{273}^{323} \frac{m c dT}{T} \\
&= +705\,\mathrm{J/K}
\end{aligned}
$$

Tổng độ biến thiên entropy của toàn hệ thống:

$$
\begin{aligned}
\Delta S_{\text{tổng}} &= -603 + 705 \\
&= +102\,\mathrm{J/K}
\end{aligned}
$$

**Đánh giá kết quả**:
Mặc dù hệ hoàn toàn cô lập về mặt nhiệt ($Q_{\text{ngoài}} = 0$), tổng entropy của hệ vẫn tăng lên một lượng $+102\,\mathrm{J/K}$. Lượng entropy giảm của khối nước nóng nhỏ hơn lượng entropy tăng của khối nước lạnh vì nhiệt lượng truyền đi tại nhiệt độ thấp tạo ra mức độ gia tăng hỗn loạn lớn hơn so với lượng trật tự tăng lên ở nhiệt độ cao.
:::

### Nguyên lý tăng entropy

Kết quả của Ví dụ 20.8 và Ví dụ 20.10 minh họa một quy luật phổ quát của vũ trụ:
- Trong một quá trình thuận nghịch diễn ra trong hệ cô lập, tổng entropy của hệ không đổi: $\Delta S = 0$.
- Trong một quá trình không thuận nghịch diễn ra trong hệ cô lập, tổng entropy của hệ luôn luôn tăng: $\Delta S > 0$.

Đó chính là **nguyên lý tăng entropy**:

$$
\Delta S \ge 0
$$

đối với mọi quá trình trong hệ cô lập.

Entropy của một hệ cô lập không bao giờ có thể tự phát suy giảm. Vũ trụ có thể được xem là một hệ cô lập tối thượng; vì mọi quá trình tự nhiên diễn ra trong vũ trụ đều ít nhiều mang tính không thuận nghịch, tổng entropy của vũ trụ không ngừng gia tăng theo thời gian.

![Hình ứng dụng 20.1: Biến thiên entropy trong cơ thể sinh vật sống](../img/young-20/b-ung-dung-20-01.png)

*Hình ứng dụng 20.1: Biến thiên entropy trong cơ thể sinh vật sống. Khi một chú cún con ăn thức ăn, cơ thể nó hấp thụ năng lượng hóa học có trật tự cao để tổng hợp tế bào, phát triển cơ bắp và duy trì tổ chức nội tại phức tạp (entropy cục bộ giảm). Tuy nhiên, sinh vật phải thải nhiệt lượng và các phân tử bài tiết đơn giản ra môi trường xung quanh, khiến tổng entropy của toàn bộ hệ sinh vật kết hợp với môi trường luôn tăng lên.*

Hiện tượng sinh vật sống phát triển và tạo nên các cấu trúc tế bào tinh vi, ngăn nắp không hề mâu thuẫn với nguyên lý thứ hai. Sinh vật không phải là một hệ cô lập mà là một hệ mở, liên tục trao đổi chất và năng lượng với môi trường. Sự giảm entropy cục bộ bên trong cơ thể được bù trừ bằng sự gia tăng entropy lớn hơn rất nhiều của môi trường ngoài, đảm bảo entropy tổng thể của vũ trụ luôn tăng.

![Hình 20.20: Sự khuếch tán không thuận nghịch của mực màu trong nước](../img/young-20/b-hinh-20-20.png)

*Hình 20.20: Quá trình hòa tan của giọt mực màu trong nước bắt đầu từ trạng thái có entropy thấp (hai chất lỏng tách biệt rõ ràng). Trong trạng thái cuối cùng, mực khuếch tán đều khắp cốc nước, tạo thành một dung dịch đồng nhất có mức độ hỗn loạn cực đại và entropy cao nhất.*

### Tự kiểm tra kiến thức mục 20.7

Giả sử $2{,}00\,\mathrm{kg}$ nước ở nhiệt độ $50^\circ\mathrm C$ tự phát phân tách thành $1{,}00\,\mathrm{kg}$ nước ở $100^\circ\mathrm C$ và $1{,}00\,\mathrm{kg}$ nước ở $0^\circ\mathrm C$ bên trong một bình cách nhiệt lý tưởng. Hãy tính độ biến thiên entropy của khối nước trong quá trình giả định này. Quá trình đó có thể tự phát xảy ra trong thực tế hay không?

<details>
<summary>Xem lời giải thích</summary>

**Đáp án**: Độ biến thiên entropy là $\Delta S = -102\,\mathrm{J/K}$. Quá trình này không thể xảy ra trong thực tế.

**Giải thích chi tiết**:
- Quá trình được mô tả chính là quá trình diễn biến ngược lại hoàn toàn so với Ví dụ 20.10.
- Khối nước ban đầu ở $50^\circ\mathrm C = 323\,\mathrm K$ được tách thành hai phần: Một phần nhận nhiệt để nóng lên $100^\circ\mathrm C = 373\,\mathrm K$ và một phần nhả nhiệt để nguội xuống $0^\circ\mathrm C = 273\,\mathrm K$.
- Độ biến thiên entropy tổng cộng của khối nước:

$$
\begin{aligned}
\Delta S &= 603 - 705 \\
&= -102\,\mathrm{J/K}
\end{aligned}
$$

- Vì bình chứa cách nhiệt hoàn toàn, khối nước đóng vai trò là một hệ cô lập. Một quá trình diễn ra trong hệ cô lập có độ biến thiên entropy âm ($\Delta S < 0$) vi phạm trực tiếp nguyên lý tăng entropy của nguyên lý thứ hai nhiệt động lực học. Do đó, quá trình phân tách nhiệt độ tự phát này là bất khả thi.
</details>
