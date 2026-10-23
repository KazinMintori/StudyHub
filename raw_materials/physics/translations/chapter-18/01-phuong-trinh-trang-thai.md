## 18.1 Phương trình trạng thái

Các đại lượng như áp suất $p$, thể tích $V$, nhiệt độ $T$ và lượng chất (đặc trưng bởi khối lượng tổng cộng $m_{\mathrm{total}}$ hoặc số mol $n$) xác định trạng thái tồn tại của một hệ vật chất xác định. Các đại lượng này được gọi là các **thông số trạng thái**. Các thông số này liên hệ với nhau, nên không thể tùy ý ấn định tất cả mà không xét những ràng buộc của hệ. Mối quan hệ hàm số giữa các thông số trạng thái được gọi là **phương trình trạng thái**.

Đối với chất rắn và chất lỏng, hãy xét những thay đổi nhỏ quanh trạng thái ban đầu có nhiệt độ $T_0$, áp suất $p_0$ và thể tích $V_0$. Đặt các độ biến thiên:

$$
\begin{aligned}
&\Delta T=T-T_0,\\
&\Delta p=p-p_0.
\end{aligned}
$$

Độ biến thiên tương đối của thể tích trong phép gần đúng tuyến tính là:

$$
\varepsilon=\beta\Delta T-k\Delta p.
$$

Phương trình trạng thái tương ứng:

$$
V=V_0(1+\varepsilon). \tag{18.1}
$$

Ở đây, $\beta$ là hệ số nở khối và $k$ là độ nén đẳng nhiệt. Số hạng $\beta\Delta T$ mô tả sự nở do tăng nhiệt độ, còn $-k\Delta p$ mô tả sự co do tăng áp suất. Phép gần đúng này chỉ dùng khi các hệ số có thể coi là không đổi trong khoảng đang xét.

Chất rắn và chất lỏng thường có độ nén nhỏ. Vì vậy, cần một độ tăng áp suất lớn mới làm thể tích giảm đáng kể.

### Phương trình khí lý tưởng

Đối với chất khí, các biến số trạng thái liên hệ với nhau qua những quy luật thực nghiệm rõ nét. Hình 18.1 minh họa một thiết lập thực nghiệm cho phép ta chủ động thay đổi thể tích, áp suất, nhiệt độ và lượng khí chứa bên trong buồng đo.

![Hình 18.1: Mô hình thí nghiệm giả định khảo sát hành vi của chất khí. Bằng cách đun nóng khối khí, thay đổi thể tích qua pít-tông di động và thêm hoặc bớt khí, ta có thể kiểm soát áp suất p, thể tích V, nhiệt độ T và lượng khí m_total hoặc n.](../img/young-18/a-hinh-18-01.png)

Các quan sát thực nghiệm lịch sử đã xác lập những mối liên hệ nền tảng:
- **Định luật Boyle**: Khi nhiệt độ $T$ không đổi, áp suất $p$ tỉ lệ nghịch với thể tích $V$, nghĩa là tích $pV$ giữ nguyên giá trị.
- **Định luật Charles**: Khi áp suất $p$ không đổi, thể tích $V$ tỉ lệ thuận với nhiệt độ tuyệt đối $T$.
- **Định luật Gay-Lussac**: Khi thể tích $V$ không đổi, áp suất $p$ tỉ lệ thuận với nhiệt độ tuyệt đối $T$.
- **Định luật Avogadro**: Ở cùng nhiệt độ và áp suất, thể tích $V$ tỉ lệ thuận với số mol chất khí $n$.

Khối lượng tổng cộng $m_{\mathrm{total}}$ của chất khí liên hệ với số mol $n$ và khối lượng mol $M$ qua hệ thức:

$$
m_{\mathrm{total}} = nM \tag{18.2}
$$

Kết hợp các định luật thực nghiệm trên dẫn đến **phương trình khí lý tưởng**:

$$
pV = nRT \tag{18.3}
$$

Ở đây, $R$ là **hằng số khí lý tưởng**, có cùng giá trị cho mọi chất khí ở giới hạn áp suất thấp. Giá trị của hằng số này, làm tròn đến chín chữ số có nghĩa, là:

$$
R = 8{,}31446262\,\mathrm{\frac{J}{mol\cdot K}}
$$

Trong các bài toán sau, ta dùng giá trị bốn chữ số có nghĩa $R = 8{,}314\,\mathrm{J/(mol\cdot K)}$. Đơn vị của tích áp suất nhân thể tích là pascal nhân mét khối ($1\,\mathrm{Pa\cdot m^3} = 1\,\mathrm{J}$), do đó hai vế của phương trình đồng nhất về thứ nguyên năng lượng. Trong hóa học, hằng số khí thường được biểu diễn theo đơn vị lít và atmosphere:

$$
R = 0{,}08206\,\mathrm{\frac{L\cdot atm}{mol\cdot K}}
$$

Chất khí tuân theo chính xác phương trình (18.3) ở mọi điều kiện nhiệt độ và áp suất được gọi là **khí lý tưởng**. Trong thực tế, không có chất khí nào hoàn toàn lý tưởng. Tuy nhiên, khi áp suất đủ thấp và nhiệt độ đủ cao so với nhiệt độ hóa lỏng, các khí thực (như không khí, oxy, nitơ, heli) tuân theo phương trình khí lý tưởng với độ chính xác rất cao.

![Hình 18.2: Phương trình khí lý tưởng pV = nRT mô tả chính xác hành vi của chất khí ở áp suất thấp và nhiệt độ tương đối cao so với điểm hóa lỏng. Trong lốp xe ô tô ở áp suất khoảng 3 atm, khí oxy và nitơ ở nhiệt độ phòng tuân theo mô hình này rất tốt. Khi lốp nóng lên trong lúc xe chạy, thể tích biến thiên không đáng kể trong khi áp suất tăng lên rõ rệt.](../img/young-18/a-hinh-18-02.png)

::: warning Lưu ý: Áp suất tuyệt đối và nhiệt độ tuyệt đối
Áp suất $p$ trong phương trình khí lý tưởng bắt buộc phải là **áp suất tuyệt đối**, không phải áp suất dư (áp suất đo bằng đồng hồ). Đồng thời, nhiệt độ $T$ bắt buộc phải là **nhiệt độ tuyệt đối** tính theo thang Kelvin, tuyệt đối không dùng độ Celsius ($^\circ\mathrm{C}$) hay độ Fahrenheit ($^\circ\mathrm{F}$). Việc dùng nhầm áp suất dư hoặc độ Celsius sẽ dẫn đến sai số nghiêm trọng.
:::

Thay $n = m_{\mathrm{total}}/M$ vào phương trình (18.3), ta biểu diễn phương trình trạng thái qua khối lượng tổng cộng của khối khí:

$$
pV = \frac{m_{\mathrm{total}}}{M} RT \tag{18.4}
$$

Từ phương trình (18.4), ta suy ra biểu thức tính khối lượng riêng $\rho = m_{\mathrm{total}}/V$ của chất khí:

$$
\rho = \frac{pM}{RT} \tag{18.5}
$$

Biểu thức này chỉ rõ: Ở áp suất và nhiệt độ xác định, khối lượng riêng của chất khí tỉ lệ thuận với khối lượng mol $M$. Do đó, khí heli ($M = 4{,}00\,\mathrm{g/mol}$) nhẹ hơn nhiều so với không khí ($M \approx 28{,}8\,\mathrm{g/mol}$), giải thích vì sao khí cầu chứa heli có thể bay lên khi lực nổi lớn hơn tổng trọng lượng của khí cầu và tải.

Khi xét một khối khí lý tưởng có khối lượng không đổi (số mol $n$ xác định), tích $nR$ là một hằng số. Khi hệ chuyển từ trạng thái 1 $(p_1, V_1, T_1)$ sang trạng thái 2 $(p_2, V_2, T_2)$, ta có:

$$
\frac{p_1 V_1}{T_1} = \frac{p_2 V_2}{T_2} \tag{18.6}
$$

Phương trình (18.6) cho phép giải bài toán biến đổi trạng thái mà không cần tra cứu giá trị số của hằng số khí $R$.

### Ứng dụng sinh học: Hô hấp và phương trình khí lý tưởng

Hoạt động hô hấp của con người dựa trên sự điều khiển áp suất và thể tích khoang ngực theo phương trình khí lý tưởng $pV = nRT$.

![Ứng dụng sinh học 18.1: Cơ chế hít vào và thở ra của phổi người. Khi hít vào, cơ hoành co lại và phẳng xuống, lồng ngực mở rộng làm tăng thể tích khoang ngực, hạ áp suất trong phổi xuống thấp hơn áp suất khí quyển để không khí tràn vào. Khi thở ra, cơ hoành giãn ra cong lên, thể tích khoang ngực thu hẹp làm áp suất phế nang tăng lên, đẩy không khí ra ngoài.](../img/young-18/a-ung-dung-18-01.png)

Khi hít vào, cơ hoành co lại, làm tăng thể tích khoang ngực và giảm áp suất. Phổi giãn ra và nhận thêm không khí trong khi nhiệt độ gần như không đổi. Khi thở ra, cơ hoành giãn, phổi co lại và đẩy không khí ra ngoài.

### Chiến lược giải bài toán: Khí lý tưởng

- **Nhận diện**: Xác định bài toán liên quan đến trạng thái cân bằng của một khối khí lý tưởng khi biết hoặc cần tìm các thông số $p, V, T, m_{\mathrm{total}}$ hoặc $n$.
- **Thiết lập**:
  1. Kiểm tra xem khối lượng chất khí có đổi hay không. Nếu khối lượng không đổi và bài toán cho trước hai trạng thái, dùng phương trình (18.6).
  2. Nếu bài toán liên quan đến mật độ hoặc khối lượng riêng, dùng phương trình (18.5). Trường hợp cần tìm trực tiếp số mol hoặc thể tích tuyệt đối, dùng phương trình (18.3).
  3. Chuyển đổi mọi thông số về đơn vị SI chuẩn. Áp suất $p$ tính bằng $\mathrm{Pa}$, $V$ tính bằng $\mathrm{m^3}$, $T$ tính bằng $\mathrm{K}$, $M$ tính bằng $\mathrm{kg/mol}$.
- **Thực hiện**: Rút ẩn số cần tìm và thay các giá trị số cẩn thận, theo dõi tính nhất quán của đơn vị đo.
- **Đánh giá**: So sánh kết quả thu được với các mốc chuẩn thực tế, chẳng hạn thể tích mol của khí ở điều kiện chuẩn khoảng $22{,}4\,\mathrm{L/mol}$.

::: example Ví dụ 18.1: Thể tích của khí lý tưởng ở điều kiện tiêu chuẩn
**Đề bài**: Điều kiện tiêu chuẩn về nhiệt độ và áp suất (kí hiệu là STP) được định nghĩa tại nhiệt độ $T = 0^\circ\mathrm{C} = 273{,}15\,\mathrm{K}$ và áp suất $p = 1{,}013 \times 10^5\,\mathrm{Pa}$ (tức $1{,}00\,\mathrm{atm}$). Tính thể tích của $1{,}00\,\mathrm{mol}$ khí lý tưởng ở điều kiện STP.

**Tóm tắt**:
- $n = 1{,}00\,\mathrm{mol}$
- $T = 273{,}15\,\mathrm{K}$
- $p = 1{,}013 \times 10^5\,\mathrm{Pa}$
- $R = 8{,}314\,\mathrm{J/(mol\cdot K)}$

**Hướng đi**:
- Áp dụng phương trình trạng thái khí lý tưởng $pV = nRT$ vì bài toán yêu cầu tìm thể tích tuyệt đối của một lượng chất xác định.
- Rút $V = nRT/p$ và thế số với các đơn vị chuẩn SI.

**Bài giải**:
Từ phương trình khí lý tưởng $pV = nRT$, ta suy ra thể tích khối khí:

$$
V = \frac{nRT}{p}
$$

Thay các giá trị số vào biểu thức:

$$
\begin{aligned}
V &= \frac{(8{,}314)(273{,}15)}{1{,}013\times10^5} \\
&= 0{,}02241\,\mathrm{m^3}
\end{aligned}
$$

Giá trị thể tích này tương đương $22{,}41\,\mathrm{L} \approx 22{,}4\,\mathrm{L}$.

**Đánh giá**: Kết quả $22{,}4\,\mathrm{L}$ là mốc số liệu kinh điển trong vật lý và hóa học. Một khối lập phương chứa lượng khí này có cạnh bằng khoảng $0{,}282\,\mathrm{m} \approx 28{,}2\,\mathrm{cm}$.

**Ý tưởng cốt lõi**: Ở điều kiện tiêu chuẩn STP, một mol của bất kỳ khí lý tưởng nào cũng chiếm thể tích xấp xỉ $22{,}4\,\mathrm{L}$.
:::

::: example Ví dụ 18.2: Nén khí trong xi lanh động cơ ô tô
**Đề bài**: Trong động cơ ô tô, hỗn hợp không khí và hơi xăng được hút vào xi lanh ở áp suất ban đầu $p_1 = 1{,}00\,\mathrm{atm}$ và nhiệt độ $T_1 = 27^\circ\mathrm{C} = 300\,\mathrm{K}$. Sau đó, pít-tông nén thể tích khí từ $V_1$ xuống $V_2 = V_1/9{,}00$ (tỉ số nén bằng $9{,}00$). Áp suất sau khi nén đo được là $p_2 = 21{,}7\,\mathrm{atm}$. Giả thiết hỗn hợp khí hoạt động như một khí lý tưởng, hãy tính nhiệt độ $T_2$ của khối khí sau khi nén.

![Hình 18.3: Cắt bổ buồng đốt động cơ ô tô bốn kỳ. Trong quá trình pít-tông nén hỗn hợp nhiên liệu trước khi đánh lửa, cả van nạp và van xả đều đóng kín hoàn toàn, bảo toàn khối lượng khí bên trong.](../img/young-18/a-hinh-18-03.png)

**Tóm tắt**:
- $p_1 = 1{,}00\,\mathrm{atm}$
- $V_1 = 9{,}00 V_2$
- $T_1 = 300\,\mathrm{K}$
- $p_2 = 21{,}7\,\mathrm{atm}$

**Hướng đi**:
- Vì các van nạp và xả đều đóng kín trong hành trình nén, khối lượng khí bên trong xi lanh được bảo toàn.
- Sử dụng phương trình biến đổi trạng thái cho khối lượng khí cố định: $p_1 V_1 / T_1 = p_2 V_2 / T_2$.
- Rút ẩn số nhiệt độ $T_2$.

**Bài giải**:
Từ phương trình (18.6), ta biến đổi để tìm $T_2$:

$$
T_2 = T_1 \frac{p_2 V_2}{p_1 V_1}
$$

Thay các giá trị áp suất và tỉ số thể tích:

$$
\begin{aligned}
T_2 &= T_1 \left(\frac{p_2}{p_1}\right) \left(\frac{V_2}{V_1}\right) \\
&= (300\,\mathrm{K}) \frac{21{,}7}{9{,}00} \\
&= 723{,}3\,\mathrm{K} \approx 723\,\mathrm{K}
\end{aligned}
$$

Đổi sang thang nhiệt độ Celsius:

$$
T_2 = 723 - 273 = 450^\circ\mathrm{C}
$$

**Đánh giá**: Nhiệt độ khối khí tăng vọt từ $27^\circ\mathrm{C}$ lên $450^\circ\mathrm{C}$ do môi trường thực hiện công nén lên khí. Quá trình đánh lửa và cháy xảy ra sau hành trình nén là một giai đoạn khác của chu trình động cơ.

**Ý tưởng cốt lõi**: Với cùng lượng khí lý tưởng, $pV/T$ có cùng giá trị ở mọi trạng thái cân bằng.
:::

::: example Ví dụ 18.3: Khối lượng không khí nạp thêm vào bình lặn

Một bình lặn bằng nhôm được gọi là “rỗng” nhưng vẫn chứa $11{,}0\,\mathrm L$ không khí ở $21^\circ\mathrm C$ và áp suất $1\,\mathrm{atm}$. Sau khi được nạp nhanh từ máy nén, nhiệt độ khí là $42^\circ\mathrm C$ và đồng hồ chỉ áp suất dư $2{,}10\times10^7\,\mathrm{Pa}$.

Tìm khối lượng không khí đã nạp thêm. Không khí gồm khoảng $78\%$ nitrogen, $21\%$ oxy và $1\%$ các khí khác, có khối lượng mol trung bình $M=28{,}8\,\mathrm{g/mol}$. Dùng mô hình khí lý tưởng.

**Tóm tắt đề bài:**

- Thể tích hai trạng thái: $V_1=V_2=0{,}0110\,\mathrm{m^3}$.
- Ban đầu: $p_1=1{,}013\times10^5\,\mathrm{Pa}$, $T_1\approx294\,\mathrm K$.
- Sau nạp: $p_{2,\mathrm{dư}}=2{,}10\times10^7\,\mathrm{Pa}$, $T_2\approx315\,\mathrm K$.
- Khối lượng mol: $M=0{,}0288\,\mathrm{kg/mol}$.
- Cần tìm: Khối lượng tăng thêm $\Delta m$.

**Hướng đi:**

- Bình “rỗng” vẫn có khí ban đầu, nên cần lấy hiệu hai khối lượng, không lấy toàn bộ khối lượng cuối.
- Tính số mol riêng ở hai trạng thái vì nhiệt độ thay đổi trong khi nạp.
- Đổi áp suất dư sang áp suất tuyệt đối trước khi dùng phương trình khí lý tưởng.

**Lời giải:**

Áp suất tuyệt đối cuối:

$$
p_2=p_{2,\mathrm{dư}}+p_{\mathrm{atm}}.
$$

Ta có $p_2\approx2{,}11\times10^7\,\mathrm{Pa}$. Bỏ qua thay đổi nhỏ của thể tích bình, số mol ở mỗi trạng thái:

$$
\begin{aligned}
n_1&=\frac{p_1V}{RT_1}\\
&\approx0{,}456\,\mathrm{mol},\\
n_2&=\frac{p_2V}{RT_2}\\
&\approx88{,}6\,\mathrm{mol}.
\end{aligned}
$$

Lượng khí nạp thêm xấp xỉ $n_2-n_1=88{,}1\,\mathrm{mol}$. Vì vậy:

$$
\begin{aligned}
\Delta m&=M(n_2-n_1)\\
&\approx2{,}54\,\mathrm{kg}.
\end{aligned}
$$

**Đánh giá:** Khối lượng tăng thêm đủ lớn để có thể nhận biết bằng cân. Kết quả phụ thuộc cả nhiệt độ ban đầu và sau nạp, nên không thể thay hai trạng thái bằng một nhiệt độ tùy chọn.
:::

::: example Ví dụ 18.4: Áp suất khí quyển thay đổi theo độ cao

Tìm sự phụ thuộc của áp suất khí quyển vào độ cao. Giả sử ở mọi độ cao, nhiệt độ là $0^\circ\mathrm C$ và gia tốc trọng trường là $9{,}80\,\mathrm{m/s^2}$.

**Tóm tắt đề bài:** Tìm hàm $p(y)$ với $y$ là độ cao. Lấy nhiệt độ xấp xỉ $T=273\,\mathrm K$, $g$ không đổi và thành phần khí quyển, do đó khối lượng mol $M$, không đổi theo độ cao. Ở mực nước biển, $p(0)=p_0=1{,}013\times10^5\,\mathrm{Pa}$.

**Hướng đi:**

- Áp suất và khối lượng riêng đều thay đổi theo độ cao. Cần ghép phương trình cân bằng thủy tĩnh với phương trình khí lý tưởng.
- Loại khối lượng riêng để được phương trình vi phân cho áp suất, sau đó tách biến và tích phân.

**Lời giải:**

Cân bằng của một lớp khí mỏng cho:

$$
\frac{dp}{dy}=-\rho g.
$$

Phương trình khí lý tưởng viết theo khối lượng riêng:

$$
\rho=\frac{pM}{RT}.
$$

Thay vào phương trình cân bằng:

$$
\frac{dp}{p}=-\frac{Mg}{RT}\,dy.
$$

Tích phân giữa hai độ cao $y_1,y_2$:

$$
\int_{p_1}^{p_2}\frac{dp}{p}
=-\frac{Mg}{RT}\int_{y_1}^{y_2}dy.
$$

Đặt $H=RT/(Mg)$, là độ cao đặc trưng của mô hình đẳng nhiệt. Khi đó:

$$
\ln\frac{p_2}{p_1}=-\frac{y_2-y_1}{H}.
$$

Lấy hàm mũ:

$$
\frac{p_2}{p_1}=e^{-(y_2-y_1)/H}.
$$

Chọn $y_1=0$, kết quả:

$$
p(y)=p_0e^{-y/H}.
$$

Với định nghĩa của $H$, đây cũng là $p(y)=p_0e^{-Mgy/(RT)}$.

![Hình 18.4: Áp suất khí quyển giảm theo độ cao trong mô hình nhiệt độ không đổi.](../img/young-18/a-hinh-18-04.png)

**Đánh giá:** Áp suất giảm theo hàm mũ. Khối lượng riêng cũng giảm vì $\rho=pM/(RT)$, nên độ dốc $dp/dy=-\rho g$ có độ lớn giảm theo độ cao.

Tại độ cao $8848\,\mathrm m$ của đỉnh Everest, dùng $M=0{,}0288\,\mathrm{kg/mol}$, ta được:

$$
\frac{y}{H}\approx1{,}10.
$$

Do đó:

$$
\begin{aligned}
p&=p_0e^{-y/H}\\
&\approx3{,}37\times10^4\,\mathrm{Pa}\\
&\approx0{,}33\,\mathrm{atm}.
\end{aligned}
$$

Nhiệt độ khí quyển thực thay đổi theo độ cao và gia tốc trọng trường cũng giảm nhẹ. Vì vậy, đây là kết quả của mô hình đẳng nhiệt. Mô hình giúp giải thích sự cần thiết của oxy bổ sung khi leo núi cao và khoang điều áp trên máy bay thường bay ở độ cao $8000$–$12000\,\mathrm m$.
:::

### Phương trình van der Waals

Mô hình khí lý tưởng dựa trên hai giả thiết đơn giản hóa: Bỏ qua kích thước riêng của các phân tử và bỏ qua lực tương tác hút giữa các phân tử khi chúng chưa va chạm vào nhau. Trong thực tế, các phân tử khí thực có kích thước hữu hạn và tác dụng lực hút lẫn nhau ở cự ly gần. Để phản ánh chính xác hơn hành vi của khí thực ở mật độ cao, nhà vật lý người Hà Lan Johannes Diderik van der Waals đã đưa ra hai hiệu chỉnh quan trọng vào phương trình trạng thái.

![Hình 18.5: Hai mô hình mô tả chất khí: (a) Mô hình khí lý tưởng coi các phân tử là những chất điểm không có thể tích riêng và không hút nhau. (b) Mô hình khí van der Waals tính đến thể tích riêng của phân tử làm giảm không gian tự do, cùng lực hút giữa các phân tử làm giảm áp lực tác dụng lên thành bình.](../img/young-18/a-hinh-18-05.png)

1. **Hiệu chỉnh thể tích**: Các phân tử có kích thước xác định nên không thể chiếm chỗ của nhau. Nếu một mol phân tử có thể tích hiệu dụng là $b$, thì với $n$ mol khí, thể tích tự do mà các phân tử có thể chuyển động bị thu hẹp từ $V$ xuống thành $(V - nb)$.
2. **Hiệu chỉnh áp suất do lực hút phân tử**: Một phân tử ở sát thành bình chịu lực hút hướng vào trong từ các phân tử lân cận trong lòng khối khí, làm giảm lực va đập lên thành bình. Độ giảm áp suất tỉ lệ với số phân tử ở lớp sát thành và số phân tử trong lớp bên trong đang hút chúng, nghĩa là tỉ lệ với bình phương mật độ phân tử $(n/V)^2$. Do đó, áp suất đo được $p$ bị hụt đi một lượng áp suất nội $p_{\mathrm{int}} = an^2/V^2$ so với áp suất lý tưởng.

Để viết gọn hai hiệu chỉnh, đặt:

$$
p^\ast=p+\frac{an^2}{V^2},
$$

$$
V^\ast=V-nb.
$$

**Phương trình van der Waals** có dạng:

$$
p^\ast V^\ast=nRT. \tag{18.7}
$$

Đại lượng $p^\ast$ đã cộng lại phần áp suất bị giảm do lực hút, còn $V^\ast$ là thể tích tự do hiệu dụng. Hai hằng số $a$ và $b$ phụ thuộc chất khí. Khi khí đủ loãng để cả hai hiệu chỉnh không đáng kể, phương trình trở về $pV=nRT$.

Xét carbon dioxide với các hằng số:

$$
a=0{,}364\,\mathrm{J\,m^3/mol^2},
$$

$$
b=4{,}27\times10^{-5}\,\mathrm{m^3/mol}.
$$

Một mol khí ở $273{,}15\,\mathrm K$ chiếm thể tích khoảng $0{,}0224\,\mathrm{m^3}$. Giải phương trình van der Waals theo áp suất:

$$
p=\frac{nRT}{V-nb}-\frac{an^2}{V^2}.
$$

Với các số liệu đã làm tròn này, hai mô hình cho:

$$
\begin{aligned}
p_{\mathrm{ideal}}&\approx1{,}01383\times10^5\,\mathrm{Pa},\\
p_{\mathrm{vdW}}&\approx1{,}00851\times10^5\,\mathrm{Pa}.
\end{aligned}
$$

Chênh lệch giữa hai giá trị xấp xỉ $532\,\mathrm{Pa}$, tức khoảng $0{,}5\%$. Cần dùng cùng một thể tích trong cả hai phép tính để so sánh. Khi nén khí đến mật độ cao, ảnh hưởng của kích thước và lực hút phân tử tăng lên.

### Giản đồ p-V và các đường đẳng nhiệt

Trạng thái cân bằng của một khối khí có thể được biểu diễn trên hệ trục tọa độ áp suất - thể tích, gọi là **giản đồ $p-V$**. Mỗi đường cong biểu diễn sự phụ thuộc của áp suất vào thể tích ở một nhiệt độ cố định được gọi là một **đường đẳng nhiệt**.

![Hình 18.6: Các đường đẳng nhiệt p-V của một lượng khí lý tưởng xác định ở các nhiệt độ khác nhau (T4 > T3 > T2 > T1). Mỗi đường cong là một nhánh hypebol tuân theo định luật Boyle pV = hằng số. Đường ứng với nhiệt độ càng cao thì càng nằm xa gốc tọa độ.](../img/young-18/a-hinh-18-06.png)

Đối với khí lý tưởng, $p = nRT/V$. Ở nhiệt độ không đổi, áp suất tỉ lệ nghịch với thể tích, các đường đẳng nhiệt là những đường hypebol đều. Khi nhiệt độ càng cao, tích $pV$ càng lớn, đường đẳng nhiệt càng dịch chuyển ra xa gốc tọa độ $O$.

Đối với chất khí thực, hành vi của các đường đẳng nhiệt thay đổi căn bản khi nhiệt độ hạ xuống dưới một giá trị đặc biệt gọi là **nhiệt độ tới hạn** $T_c$.

![Hình 18.7: Giản đồ p-V của chất khí thực thể hiện các đường đẳng nhiệt ở nhiệt độ trên và dưới nhiệt độ tới hạn Tc. Vùng màu xanh lá biểu diễn trạng thái cân bằng lỏng - hơi. Ở dưới Tc, quá trình nén đẳng nhiệt xuất hiện đoạn nằm ngang tương ứng với sự ngưng tụ hơi thành chất lỏng ở áp suất hơi bão hòa không đổi.](../img/young-18/a-hinh-18-07.png)

Quan sát giản đồ Hình 18.7:
1. **Ở nhiệt độ $T > T_c$**: Không có ranh giới chuyển pha lỏng–hơi. Khi nén đẳng nhiệt, áp suất tăng liên tục mà không xuất hiện quá trình ngưng tụ hóa lỏng. Ở nhiệt độ rất cao (như $T_4$), đường cong gần như trùng với hypebol của khí lý tưởng.
2. **Ở nhiệt độ tới hạn $T = T_c$**: Đường đẳng nhiệt có một điểm uốn nằm ngang tại áp suất tới hạn $p_c$ và thể tích tới hạn $V_c$. Điểm này được gọi là **điểm tới hạn**.
3. **Ở nhiệt độ $T < T_c$**: Khi nén hơi từ thể tích lớn, ban đầu áp suất tăng dọc theo nhánh hơi. Khi đạt tới điểm $a$, hơi bắt đầu ngưng tụ thành chất lỏng. Từ $a$ đến $b$, áp suất giữ nguyên không đổi (gọi là **áp suất hơi bão hòa**) trong khi thể tích tiếp tục giảm, tạo ra đoạn đẳng nhiệt nằm ngang bên trong vùng cân bằng lỏng - hơi. Tại điểm $b$, toàn bộ khối hơi đã ngưng tụ hoàn toàn thành chất lỏng. Tiếp tục nén quá điểm $b$, đường đẳng nhiệt tăng rất dốc do chất lỏng có độ nén rất nhỏ.

Trong hai chương tiếp theo, giản đồ $p-V$ đóng vai trò cốt lõi vì diện tích dưới đường biến trình $p-V$ biểu diễn trực quan công cơ học trao đổi trong quá trình nhiệt động lực học.

### Kiểm tra mức độ hiểu mục 18.1

Hãy xếp hạng các khối khí lý tưởng sau đây theo thứ tự số mol $n$ từ lớn nhất đến nhỏ nhất:
- (i) Áp suất $p = 1\,\mathrm{atm}$, thể tích $V = 1\,\mathrm{L}$, nhiệt độ $T = 300\,\mathrm{K}$.
- (ii) Áp suất $p = 2\,\mathrm{atm}$, thể tích $V = 1\,\mathrm{L}$, nhiệt độ $T = 300\,\mathrm{K}$.
- (iii) Áp suất $p = 1\,\mathrm{atm}$, thể tích $V = 2\,\mathrm{L}$, nhiệt độ $T = 300\,\mathrm{K}$.
- (iv) Áp suất $p = 1\,\mathrm{atm}$, thể tích $V = 1\,\mathrm{L}$, nhiệt độ $T = 600\,\mathrm{K}$.
- (v) Áp suất $p = 2\,\mathrm{atm}$, thể tích $V = 1\,\mathrm{L}$, nhiệt độ $T = 600\,\mathrm{K}$.

<details><summary>Xem lời giải thích</summary>

**Đáp án**: Hai trường hợp (ii) và (iii) có số mol lớn nhất và bằng nhau. Tiếp đến là (i) và (v), cũng bằng nhau. Trường hợp (iv) có số mol nhỏ nhất.

**Giải thích chi tiết**:
Từ phương trình khí lý tưởng $pV = nRT$, ta rút ra biểu thức xác định số mol:

$$
n = \frac{pV}{RT}
$$

Vì hằng số khí $R$ không đổi đối với mọi khối khí, số mol $n$ tỉ lệ thuận với tích $pV$ và tỉ lệ nghịch với nhiệt độ tuyệt đối $T$:

$$
n \propto \frac{pV}{T}
$$

So sánh tỉ số $pV/T$ của từng trường hợp với trường hợp (i) có giá trị chuẩn $pV/T = 1/300$:
- Trường hợp (ii) có $pV/T = 2/300$, lượng khí gấp $2$ lần so với (i).
- Trường hợp (iii) có $pV/T = 2/300$, lượng khí gấp $2$ lần so với (i).
- Trường hợp (iv) có $pV/T = 0{,}5/300$, lượng khí bằng $0{,}5$ lần so với (i).
- Trường hợp (v) có $pV/T = 1/300$, lượng khí bằng đúng $1$ lần so với (i).

Như vậy, quan hệ định lượng giữa các trường hợp là:

$$
n_{(\mathrm{ii})} = n_{(\mathrm{iii})} > n_{(\mathrm{i})} = n_{(\mathrm{v})}
$$

$$
n_{(\mathrm{i})} = n_{(\mathrm{v})} > n_{(\mathrm{iv})}
$$

</details>
