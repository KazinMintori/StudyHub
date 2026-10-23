<!-- Source: Section20.6, printed653–659, PDF673–679. -->

## 20.6. Chu trình Carnot

Theo nguyên lý thứ hai nhiệt động lực học, không một động cơ nhiệt nào có thể đạt hiệu suất $100\%$. Câu hỏi tự nhiên đặt ra là: Trong điều kiện lý tưởng nhất, hiệu suất cực đại mà một động cơ nhiệt có thể đạt được là bao nhiêu? Câu trả lời đã được kỹ sư người Pháp Nicolas Léonard Sadi Carnot (1796–1832) tìm ra vào năm 1824 trước cả khi nguyên lý thứ nhất và thứ hai được phát biểu hoàn chỉnh. Chu trình nhiệt động mang tên ông, **chu trình Carnot**, đóng vai trò là chuẩn mực lý thuyết tối cao để đánh giá mọi động cơ nhiệt và máy lạnh.

### Tính không thuận nghịch và hiệu suất động cơ

Để một động cơ đạt hiệu suất tối đa, toàn bộ các quá trình diễn ra trong chu trình phải hoàn toàn thuận nghịch. Trong thực tế, các động cơ nhiệt thông thường luôn chứa đựng nhiều yếu tố không thuận nghịch làm giảm đáng kể hiệu suất chuyển hóa năng lượng:
- **Ma sát cơ học và độ nhớt**: Chuyển động tương đối giữa piston và thành xylanh, các ổ bi và dòng chảy cuộn xoáy của chất khí đều làm thất thoát một phần công cơ học thành nội năng phân tán.
- **Truyền nhiệt qua chênh lệch nhiệt độ hữu hạn**: Trong các động cơ hơi nước hoặc nhà máy nhiệt điện, nhiệt lượng truyền từ ngọn lửa buồng đốt có nhiệt độ rất cao sang nước trong nồi hơi ở nhiệt độ thấp hơn nhiều (Hình 20.12). Sự truyền nhiệt qua độ chênh lệch nhiệt độ lớn này là một quá trình không thuận nghịch điển hình, gây lãng phí khả năng sinh công hữu ích của nhiên liệu.

![Hình 20.12: Quá trình truyền nhiệt không thuận nghịch do chênh lệch nhiệt độ lớn trong lò hơi](../img/young-20/b-hinh-20-12.png)

*Hình 20.12: Nhiệt độ của buồng đốt trong động cơ hơi nước cao hơn rất nhiều so với nhiệt độ của nước trong nồi hơi, khiến nhiệt lượng truyền đi một cách không thuận nghịch từ buồng đốt sang nước.*

Muốn loại bỏ hoàn toàn tính không thuận nghịch trong quá trình trao đổi nhiệt, mọi sự truyền nhiệt giữa chất tác công và môi trường ngoài chỉ được phép xảy ra khi chênh lệch nhiệt độ giữa chúng tiến tới vô cùng bé. Điều này đồng nghĩa với việc chất tác công chỉ được hấp thụ nhiệt hoặc nhả nhiệt thông qua các **quá trình đẳng nhiệt thuận nghịch**. Khi cần thay đổi nhiệt độ của chất tác công giữa nguồn nóng $T_H$ và nguồn lạnh $T_C$, hệ thống phải thực hiện các **quá trình đoạn nhiệt thuận nghịch**, trong đó không có bất kỳ nhiệt lượng nào trao đổi qua lại giữa hệ và môi trường.

### Các giai đoạn của chu trình Carnot

Xét một động cơ Carnot sử dụng chất tác công là khí lý tưởng chứa trong một xylanh có đáy dẫn nhiệt tốt và các thành xung quanh cách nhiệt lý tưởng, được đậy kín bởi một piston chuyển động không ma sát (Hình 20.13). Chu trình Carnot bao gồm bốn quá trình thuận nghịch xen kẽ:

![Hình 20.13: Chu trình Carnot đối với khí lý tưởng trong xylanh có piston](../img/young-20/b-hinh-20-13.png)

*Hình 20.13: Chu trình Carnot đối với khí lý tưởng. Trên đồ thị $p-V$, các đường màu xanh nhạt là đường đẳng nhiệt (nhiệt độ không đổi), còn các đường màu xanh đậm là đường đoạn nhiệt (không có nhiệt lượng trao đổi).*

1. **Giai đoạn 1 ($a \to b$): Giãn nở đẳng nhiệt thuận nghịch ở nhiệt độ $T_H$**:
   Xylanh được đặt tiếp xúc nhiệt với nguồn nóng ở nhiệt độ không đổi $T_H$. Khối khí giãn nở từ thể tích $V_a$ đến thể tích $V_b$, sinh công cơ học $W_{ab} > 0$ đẩy piston đi lên. Do nhiệt độ không đổi, nội năng của khí lý tưởng giữ nguyên ($\Delta U_{ab} = 0$), vì vậy nhiệt lượng $Q_H$ mà khối khí nhận từ nguồn nóng đúng bằng công sinh ra:

$$
\begin{aligned}
W_{ab} &= Q_H \\
&= n R T_H \ln \frac{V_b}{V_a}
\end{aligned}
$$

2. **Giai đoạn 2 ($b \to c$): Giãn nở đoạn nhiệt thuận nghịch từ $T_H$ xuống $T_C$**:
   Đáy xylanh được chuyển sang tiếp xúc với một đế cách nhiệt hoàn hảo. Khối khí tiếp tục giãn nở từ thể tích $V_b$ đến $V_c$, đẩy piston lên tiếp và sinh công $W_{bc} > 0$. Vì quá trình là đoạn nhiệt ($Q_{bc} = 0$), công sinh ra được bù đắp hoàn toàn bởi sự suy giảm nội năng của chất khí ($\Delta U_{bc} = -W_{bc}$), khiến nhiệt độ của khối khí hạ từ $T_H$ xuống nhiệt độ của nguồn lạnh $T_C$:

$$
\begin{aligned}
W_{bc} &= -\Delta U_{bc} \\
&= n C_V (T_H - T_C)
\end{aligned}
$$

   Mối liên hệ giữa nhiệt độ và thể tích trên đường đoạn nhiệt tuân theo hệ thức:

$$
T_H V_b^{\gamma - 1} = T_C V_c^{\gamma - 1}
$$

3. **Giai đoạn 3 ($c \to d$): Nén đẳng nhiệt thuận nghịch ở nhiệt độ $T_C$**:
   Xylanh được đặt tiếp xúc nhiệt với nguồn lạnh ở nhiệt độ không đổi $T_C$. Ngoại lực nén piston đi xuống từ thể tích $V_c$ về $V_d$, thực hiện công lên khối khí làm $W_{cd} < 0$. Nhiệt lượng $Q_C < 0$ tỏa ra từ khối khí được truyền vào nguồn lạnh để giữ nhiệt độ không đổi ($\Delta U_{cd} = 0$):

$$
\begin{aligned}
W_{cd} &= Q_C \\
&= n R T_C \ln \frac{V_d}{V_c}
\end{aligned}
$$

4. **Giai đoạn 4 ($d \to a$): Nén đoạn nhiệt thuận nghịch từ $T_C$ lên $T_H$**:
   Xylanh lại được đặt lên đế cách nhiệt. Piston tiếp tục nén khối khí từ thể tích $V_d$ về lại thể tích ban đầu $V_a$ không ma sát và không trao đổi nhiệt ($Q_{da} = 0$). Công nhận vào làm tăng nội năng của khối khí ($\Delta U_{da} = -W_{da} > 0$), nâng nhiệt độ từ $T_C$ trở lại đúng nhiệt độ ban đầu $T_H$:

$$
\begin{aligned}
W_{da} &= -\Delta U_{da} \\
&= n C_V (T_C - T_H) \\
&= -W_{bc}
\end{aligned}
$$

   Mối quan hệ đoạn nhiệt giữa hai trạng thái $d$ và $a$ là:

$$
T_C V_d^{\gamma - 1} = T_H V_a^{\gamma - 1}
$$

### Hiệu suất nhiệt của động cơ Carnot

Lập tỷ số giữa nhiệt lượng nhả ra $Q_C$ và nhiệt lượng nhận vào $Q_H$:

$$
\begin{aligned}
\frac{Q_C}{Q_H} &= \frac{n R T_C \ln(V_d/V_c)}{n R T_H \ln(V_b/V_a)} \\
&= \frac{T_C \ln(V_d/V_c)}{T_H \ln(V_b/V_a)}
\end{aligned}
$$

Từ hai hệ thức đoạn nhiệt cho giai đoạn $b \to c$ và $d \to a$, ta chia vế theo vế:

$$
\begin{aligned}
\frac{T_H V_b^{\gamma - 1}}{T_H V_a^{\gamma - 1}} &= \frac{T_C V_c^{\gamma - 1}}{T_C V_d^{\gamma - 1}} \\
\implies \frac{V_b}{V_a} &= \frac{V_c}{V_d}
\end{aligned}
$$

Do đó:

$$
\begin{aligned}
\ln \frac{V_d}{V_c} &= -\ln \frac{V_c}{V_d} \\
&= -\ln \frac{V_b}{V_a}
\end{aligned}
$$

Hai thừa số logarit trong biểu thức có độ lớn bằng nhau nhưng trái dấu. Khi thay vào tỷ số nhiệt lượng, ta thu được hệ thức then chốt:

$$
\frac{Q_C}{Q_H} = -\frac{T_C}{T_H}
$$

và tương đương với:

$$
\frac{|Q_C|}{|Q_H|} = \frac{T_C}{T_H}
$$

Tỷ số giữa nhiệt lượng nhả cho nguồn lạnh và nhiệt lượng nhận từ nguồn nóng trong một chu trình Carnot đúng bằng tỷ số giữa hai nhiệt độ tuyệt đối của hai nguồn nhiệt. Khi thay hệ thức này vào định nghĩa tổng quát của hiệu suất nhiệt $e = 1 + Q_C/Q_H$, ta nhận được công thức tính **hiệu suất của động cơ Carnot**:

$$
\begin{aligned}
e_{\text{Carnot}} &= 1 - \frac{T_C}{T_H} \\
&= \frac{T_H - T_C}{T_H}
\end{aligned}
$$

Công thức trên cho thấy một kết luận vô cùng sâu sắc: Hiệu suất nhiệt của động cơ Carnot chỉ phụ thuộc vào nhiệt độ tuyệt đối của hai nguồn nhiệt, hoàn toàn không phụ thuộc vào bản chất của chất tác công cũng như cấu tạo cơ học của động cơ. Muốn hiệu suất đạt cực đại, ta cần:
- Tăng nhiệt độ nguồn nóng $T_H$ lên mức cao nhất có thể.
- Hạ nhiệt độ nguồn lạnh $T_C$ xuống mức thấp nhất có thể.

Động cơ chỉ có thể đạt hiệu suất $100\%$ ($e = 1$) nếu nguồn lạnh ở độ không tuyệt đối ($T_C = 0\,\mathrm K$), một điều kiện không thể đạt được trong thực tế.

::: example Ví dụ 20.2: Phân tích động cơ Carnot I
Một động cơ Carnot nhận $2000\,\mathrm J$ nhiệt lượng từ một nguồn nóng ở nhiệt độ $500\,\mathrm K$, sinh công cơ học và thải nhiệt ra một nguồn lạnh ở nhiệt độ $350\,\mathrm K$. Hãy xác định:
(a) Nhiệt lượng nhả cho nguồn lạnh.
(b) Công cơ học mà động cơ sinh ra.
(c) Hiệu suất nhiệt của động cơ.

**Tóm tắt**:
- $Q_H = 2000\,\mathrm J$
- $T_H = 500\,\mathrm K$
- $T_C = 350\,\mathrm K$

**Hướng đi**:
- Áp dụng hệ thức nhiệt lượng của chu trình Carnot để tìm $Q_C$.
- Áp dụng nguyên lý thứ nhất nhiệt động lực học cho chu trình kín $W = Q_H + Q_C$ để tìm công sinh ra.
- Tính hiệu suất theo công thức Carnot và đối chiếu với định nghĩa $e = W/Q_H$.

![Hình 20.14: Sơ đồ dòng năng lượng cho động cơ Carnot trong Ví dụ 20.2](../img/young-20/b-hinh-20-14.png)

*Hình 20.14: Sơ đồ dòng năng lượng phác thảo cho bài toán động cơ Carnot trong Ví dụ 20.2.*

**Các bước tính toán**:
(a) Nhiệt lượng nhả cho nguồn lạnh là:

$$
\begin{aligned}
Q_C &= -Q_H \frac{T_C}{T_H} \\
&= -(2000\,\mathrm J)\frac{350\,\mathrm K}{500\,\mathrm K} \\
&= -1400\,\mathrm J
\end{aligned}
$$

(b) Từ nguyên lý thứ nhất đối với chu trình kín, công sinh ra là:

$$
\begin{aligned}
W &= Q_H + Q_C \\
&= 2000\,\mathrm J - 1400\,\mathrm J \\
&= 600\,\mathrm J
\end{aligned}
$$

(c) Hiệu suất nhiệt của động cơ tính theo nhiệt độ của hai nguồn nhiệt:

$$
\begin{aligned}
e &= 1 - \frac{T_C}{T_H} \\
&= 1 - \frac{350\,\mathrm K}{500\,\mathrm K} \\
&= 0{,}30 = 30\%
\end{aligned}
$$

**Đánh giá kết quả**:
Dấu âm của $Q_C$ hoàn toàn chính xác, thể hiện nhiệt lượng $1400\,\mathrm J$ rời khỏi chất tác công và truyền vào nguồn lạnh. Ta kiểm tra lại hiệu suất theo định nghĩa:

$$
\begin{aligned}
e &= \frac{W}{Q_H} \\
&= \frac{600\,\mathrm J}{2000\,\mathrm J} \\
&= 0{,}30 = 30\%
\end{aligned}
$$

Kết quả hoàn toàn trùng khớp.
:::

::: warning Bắt buộc dùng thang nhiệt độ Kelvin trong mọi tính toán chu trình Carnot
Trong các công thức của chu trình Carnot, các giá trị nhiệt độ $T_H$ và $T_C$ bắt buộc phải là nhiệt độ tuyệt đối tính bằng Kelvin ($\mathrm K$). Việc thay thế trực tiếp nhiệt độ theo thang Celsius ($^\circ\mathrm C$) hoặc Fahrenheit ($^\circ\mathrm F$) sẽ dẫn đến sai số nghiêm trọng vì tỷ số nhiệt độ giữa hai thang đo này không tương đồng với tỷ số năng lượng nhiệt.
:::

::: example Ví dụ 20.3: Phân tích động cơ Carnot II
Giả sử $0{,}200\,\mathrm{mol}$ khí lý tưởng lưỡng nguyên tử ($\gamma = 1{,}40$; $C_V = 20{,}8\,\mathrm{J/(mol\cdot K)}$) thực hiện chu trình Carnot giữa hai nhiệt độ $227^\circ\mathrm C$ và $27^\circ\mathrm C$. Trạng thái ban đầu $a$ có áp suất $p_a = 10{,}0 \times 10^5\,\mathrm{Pa}$. Trong quá trình giãn nở đẳng nhiệt $a \to b$, thể tích khối khí tăng gấp đôi.
(a) Tính áp suất và thể tích tại các điểm $a, b, c, d$.
(b) Tính $Q, W, \Delta U$ cho từng giai đoạn và cho toàn bộ chu trình.
(c) Tính hiệu suất trực tiếp từ công và nhiệt lượng, sau đó so sánh với công thức Carnot.

**Tóm tắt**:
- $n = 0{,}200\,\mathrm{mol}$
- $\gamma = 1{,}40$; $C_V = 20{,}8\,\mathrm{J/(mol\cdot K)}$
- $R = 8{,}314\,\mathrm{J/(mol\cdot K)}$
- $T_H = 500\,\mathrm K$ ($227^\circ\mathrm C$)
- $T_C = 300\,\mathrm K$ ($27^\circ\mathrm C$)
- $p_a = 10{,}0 \times 10^5\,\mathrm{Pa}$; $V_b = 2V_a$

**Hướng đi**:
- Chuyển đổi nhiệt độ sang Kelvin. Dùng phương trình khí lý tưởng $p V = n R T$ để tìm thể tích $V_a$.
- Dùng điều kiện đẳng nhiệt $a \to b$ ($T = T_H$, $V_b = 2V_a$) để tìm $p_b, V_b$.
- Dùng phương trình đoạn nhiệt $T V^{\gamma - 1} = \text{const}$ để tìm thể tích tại $c$ và $d$, từ đó tính áp suất $p_c, p_d$.
- Tính công, nhiệt lượng và nội năng cho từng quá trình theo các công thức tương ứng.

**Các bước tính toán**:
(a) Xác định các thông số trạng thái tại $a, b, c, d$:
- Tại điểm $a$:

$$
\begin{aligned}
V_a &= \frac{n R T_H}{p_a} \\
&= 8{,}31 \times 10^{-4}\,\mathrm m^3
\end{aligned}
$$

- Tại điểm $b$: Thể tích tăng gấp đôi ($V_b = 2V_a$):

$$
\begin{aligned}
V_b &= 2(8{,}31 \times 10^{-4}\,\mathrm m^3) \\
&= 16{,}6 \times 10^{-4}\,\mathrm m^3
\end{aligned}
$$

  Vì quá trình $a \to b$ là đẳng nhiệt nên $p_a V_a = p_b V_b$:

$$
\begin{aligned}
p_b &= p_a \frac{V_a}{V_b} \\
&= \frac{10{,}0 \times 10^5\,\mathrm{Pa}}{2} \\
&= 5{,}00 \times 10^5\,\mathrm{Pa}
\end{aligned}
$$

- Tại điểm $c$: Quá trình $b \to c$ là đoạn nhiệt ($T_H V_b^{\gamma - 1} = T_C V_c^{\gamma - 1}$):

$$
\begin{aligned}
V_c &= V_b \left(\frac{T_H}{T_C}\right)^{\frac{1}{\gamma - 1}} \\
&= 59{,}6 \times 10^{-4}\,\mathrm m^3
\end{aligned}
$$

$$
\begin{aligned}
p_c &= \frac{n R T_C}{V_c} \\
&= 0{,}837 \times 10^5\,\mathrm{Pa}
\end{aligned}
$$

- Tại điểm $d$: Quá trình $d \to a$ là đoạn nhiệt ($T_C V_d^{\gamma - 1} = T_H V_a^{\gamma - 1}$):

$$
\begin{aligned}
V_d &= V_a \left(\frac{T_H}{T_C}\right)^{\frac{1}{\gamma - 1}} \\
&= 29{,}8 \times 10^{-4}\,\mathrm m^3
\end{aligned}
$$

$$
\begin{aligned}
p_d &= \frac{n R T_C}{V_d} \\
&= 1{,}67 \times 10^5\,\mathrm{Pa}
\end{aligned}
$$

(b) Tính $Q, W, \Delta U$ cho từng giai đoạn:
- Giai đoạn $a \to b$ (giãn đẳng nhiệt): $\Delta U_{ab} = 0$.

$$
\begin{aligned}
W_{ab} &= n R T_H \ln \frac{V_b}{V_a} \\
&= 576\,\mathrm J
\end{aligned}
$$

- Giai đoạn $b \to c$ (giãn đoạn nhiệt): $Q_{bc} = 0$.

$$
\begin{aligned}
W_{bc} &= n C_V (T_H - T_C) \\
&= 832\,\mathrm J
\end{aligned}
$$

  Do đó $\Delta U_{bc} = -832\,\mathrm J$.
- Giai đoạn $c \to d$ (nén đẳng nhiệt): $\Delta U_{cd} = 0$.

$$
\begin{aligned}
W_{cd} &= n R T_C \ln \frac{V_d}{V_c} \\
&= -346\,\mathrm J
\end{aligned}
$$

- Giai đoạn $d \to a$ (nén đoạn nhiệt): $Q_{da} = 0$.

$$
\begin{aligned}
W_{da} &= n C_V (T_C - T_H) \\
&= -832\,\mathrm J
\end{aligned}
$$

  Do đó $\Delta U_{da} = +832\,\mathrm J$.

Bảng tổng hợp năng lượng cho các giai đoạn trong chu trình:

| Nhánh | Q (J) | W (J) | ΔU (J) |
| --- | ---: | ---: | ---: |
| ab | $+576$ | $+576$ | $0$ |
| bc | $0$ | $+832$ | $-832$ |
| cd | $-346$ | $-346$ | $0$ |
| da | $0$ | $-832$ | $+832$ |
| Chu kỳ | $+230$ | $+230$ | $0$ |

(c) Hiệu suất của chu trình:
Từ bảng trên, công thuần sinh ra là $W = 230\,\mathrm J$ và nhiệt nhận vào là $Q_H = 576\,\mathrm J$:

$$
\begin{aligned}
e &= \frac{W}{Q_H} \\
&= \frac{230\,\mathrm J}{576\,\mathrm J} \\
&= 0{,}40 = 40\%
\end{aligned}
$$

So sánh với công thức hiệu suất Carnot:

$$
\begin{aligned}
e &= \frac{T_H - T_C}{T_H} \\
&= \frac{500\,\mathrm K - 300\,\mathrm K}{500\,\mathrm K} \\
&= 0{,}40 = 40\%
\end{aligned}
$$

**Đánh giá kết quả**:
Sau một chu trình hoàn chỉnh, tổng nhiệt trao đổi đúng bằng công sinh ra ($Q_{\text{net}} = W_{\text{net}} = 230\,\mathrm J$) và biến thiên nội năng triệt tiêu hoàn toàn ($\Delta U = 0$). Ngoài ra, công trong hai quá trình đoạn nhiệt có độ lớn bằng nhau nhưng đối dấu ($W_{bc} = -W_{da} = 832\,\mathrm J$), do đó chúng tự triệt tiêu lẫn nhau trong biểu thức công tổng cộng.
:::

### Máy lạnh Carnot

Do mọi quá trình trong chu trình Carnot đều là thuận nghịch, ta hoàn toàn có thể cho chu trình vận hành theo chiều ngược lại để biến động cơ thành một máy lạnh lý tưởng:
- Chất tác công nhận nhiệt lượng $Q_C > 0$ từ nguồn lạnh ở nhiệt độ $T_C$ thông qua quá trình giãn nở đẳng nhiệt.
- Ngoại lực thực hiện công $W < 0$ (hay tốn công đầu vào $|W|$) để nén chất khí.
- Hệ nhả nhiệt lượng $|Q_H|$ vào nguồn nóng ở nhiệt độ $T_H$.

Hệ số làm lạnh của máy lạnh Carnot được suy ra bằng cách kết hợp định nghĩa tổng quát $K = |Q_C| / |W|$ với hệ thức tỷ số nhiệt lượng:

$$
\begin{aligned}
K_{\text{Carnot}} &= \frac{|Q_C|}{|Q_H| - |Q_C|} \\
&= \frac{T_C}{T_H - T_C}
\end{aligned}
$$

Công thức trên cho thấy khi hiệu nhiệt độ giữa hai nguồn $T_H - T_C$ càng nhỏ thì hệ số làm lạnh $K$ càng lớn. Khi đó, chỉ cần một lượng công nhỏ ngoại lực bỏ ra cũng có thể vận chuyển một nhiệt lượng rất lớn từ nguồn lạnh sang nguồn nóng.

::: example Ví dụ 20.4: Phân tích máy lạnh Carnot
Nếu chu trình Carnot trong Ví dụ 20.3 được vận hành theo chiều ngược lại để hoạt động như một máy lạnh, hãy xác định hệ số làm lạnh của máy.

**Tóm tắt**:
- $T_H = 500\,\mathrm K$
- $T_C = 300\,\mathrm K$
- Các thông số từ Ví dụ 20.3: $Q_C = +346\,\mathrm J$, $W = -230\,\mathrm J$

**Hướng đi**:
- Áp dụng định nghĩa hệ số làm lạnh $K = |Q_C|/|W|$.
- Áp dụng công thức hệ số làm lạnh Carnot và so sánh hai kết quả.

**Các bước tính toán**:
Khi vận hành ngược lại, khối khí nhận nhiệt lượng $Q_C = +346\,\mathrm J$ từ nguồn lạnh và cần một công đầu vào có độ lớn $|W| = 230\,\mathrm J$.
Áp dụng định nghĩa hệ số làm lạnh:

$$
\begin{aligned}
K &= \frac{|Q_C|}{|W|} \\
&= \frac{346\,\mathrm J}{230\,\mathrm J} = 1{,}50
\end{aligned}
$$

Tính trực tiếp theo nhiệt độ của hai nguồn nhiệt:

$$
\begin{aligned}
K &= \frac{T_C}{T_H - T_C} \\
&= \frac{300\,\mathrm K}{500\,\mathrm K - 300\,\mathrm K} \\
&= 1{,}50
\end{aligned}
$$

**Đánh giá kết quả**:
Hai phương pháp cho kết quả hoàn toàn trùng khớp. Đối với chu trình chứa các quá trình không thuận nghịch, hệ số làm lạnh thực tế sẽ luôn nhỏ hơn giá trị này.
:::

### Định lý Carnot và giới hạn tối đa của hiệu suất

Ta có thể chứng minh một định lý nền tảng của nhiệt động lực học: **Không một động cơ nhiệt nào hoạt động giữa hai nguồn nhiệt ở nhiệt độ xác định $T_H$ và $T_C$ có thể đạt hiệu suất cao hơn động cơ Carnot hoạt động giữa chính hai nguồn nhiệt đó**.

![Hình 20.15: Chứng minh tính tối ưu của hiệu suất động cơ Carnot bằng phản chứng](../img/young-20/b-hinh-20-15.png)

*Hình 20.15: Chứng minh động cơ Carnot có hiệu suất cao nhất bằng phương pháp phản chứng. Giả sử tồn tại một động cơ “siêu hiệu suất” (có hiệu suất lớn hơn động cơ Carnot), khi dùng động cơ này để dẫn động một máy lạnh Carnot, hệ kết hợp sẽ tương đương với một động cơ đạt hiệu suất $100\%$, vi phạm nguyên lý thứ hai nhiệt động lực học.*

Chứng minh được thực hiện bằng phương pháp phản chứng (Hình 20.15):
- Giả sử tồn tại một động cơ “siêu hiệu suất” $E_{\text{siêu}}$ có hiệu suất $e_{\text{siêu}} > e_{\text{Carnot}}$.
- Ta cho động cơ này nhận nhiệt lượng $Q_H$ từ nguồn nóng, sinh công $W_{\text{siêu}} = e_{\text{siêu}} Q_H$.
- Ta dùng một phần công này để vận hành một máy lạnh Carnot $R_{\text{Carnot}}$ chạy giữa cùng hai nguồn nhiệt, sao cho máy lạnh lấy đúng lượng nhiệt $|Q_C|$ từ nguồn lạnh và trả lại lượng nhiệt $Q_H$ cho nguồn nóng.
- Vì động cơ siêu hiệu suất sinh ra công $W_{\text{siêu}} > W_{\text{Carnot}}$, công dư thừa $\Delta W = W_{\text{siêu}} - W_{\text{Carnot}} > 0$ được đưa ra môi trường ngoài.
- Tại nguồn nóng, lượng nhiệt lấy đi bằng lượng nhiệt trả về ($Q_H - Q_H = 0$). Toàn bộ hệ liên hợp hoạt động theo chu trình khép kín chỉ hấp thụ nhiệt thuần từ nguồn lạnh và chuyển hóa hoàn toàn thành công cơ học $\Delta W$, vi phạm trực tiếp nguyên lý thứ hai nhiệt động lực học.

Do đó, giả thiết ban đầu là sai: Động cơ Carnot chính là động cơ có hiệu suất nhiệt động cực đại. Mọi động cơ thực tế hoạt động giữa hai nhiệt độ $T_H$ và $T_C$ đều có hiệu suất $e < e_{\text{Carnot}}$.

![Hình 20.16: Cánh tuabin động cơ phản lực chế tạo từ vật liệu gốm chịu nhiệt cực cao](../img/young-20/b-hinh-20-16.png)

*Hình 20.16: Để tối đa hóa hiệu suất nhiệt động theo định luật Carnot, nhiệt độ khí cháy bên trong động cơ phản lực được đẩy lên mức cao nhất có thể. Các cánh tuabin phải được chế tạo từ các vật liệu gốm đặc biệt có khả năng chịu đựng nhiệt độ và ứng suất cơ học khắc nghiệt.*

### Thang nhiệt độ Kelvin tuyệt đối

Trong các chương trước, thang nhiệt độ khí lý tưởng được xây dựng dựa trên áp suất của khối khí có thể tích không đổi. Tuy nhiên, thang đo này vẫn phụ thuộc vào tính chất tiệm cận của chất khí thực khi áp suất tiến về không.

Dựa vào chu trình Carnot, nhà vật lý Lord Kelvin (William Thomson) đã đề xuất một thang đo nhiệt độ hoàn toàn độc lập với mọi tính chất của bất kỳ chất tác công cụ thể nào. Tỷ số giữa nhiệt lượng nhận vào và nhả ra của một động cơ Carnot chỉ phụ thuộc vào nhiệt độ của hai nguồn nhiệt:

$$
\frac{T_H}{T_C} = \frac{|Q_H|}{|Q_C|}
$$

Đây chính là định nghĩa nhiệt động lực học của **thang nhiệt độ tuyệt đối Kelvin**. Để cố định độ lớn của một độ Kelvin, người ta chọn điểm ba trạng thái của nước (nơi nước đá, nước lỏng và hơi nước cùng tồn tại cân bằng) làm mốc nhiệt độ chuẩn duy nhất, được quy ước chính xác bằng $273{,}16\,\mathrm K$. Khi đó, nhiệt độ tuyệt đối $T$ của một nguồn nhiệt bất kỳ được xác định bằng cách cho một động cơ Carnot hoạt động giữa nguồn nhiệt đó và nguồn chuẩn ở điểm ba của nước:

$$
T = (273{,}16\,\mathrm K) \frac{|Q|}{|Q_{\text{chuẩn}}|}
$$

Thang nhiệt độ nhiệt động lực học này hoàn toàn trùng khớp với thang nhiệt độ khí lý tưởng trong phạm vi mà các chất khí còn tuân theo định luật chất khí, đồng thời mở rộng khái niệm nhiệt độ đến mọi vùng năng lượng của vật lý hiện đại.

### Tự kiểm tra kiến thức mục 20.6

Một nhà phát minh tìm kiếm nguồn tài trợ tài chính tìm đến bạn với bản thiết kế một động cơ chạy xăng hoạt động theo một chu trình nhiệt động mới lạ. Thiết kế này được chế tạo hoàn toàn bằng đồng và làm mát bằng không khí xung quanh. Ông khẳng định động cơ có thể đạt hiệu suất $85\%$. Bạn có nên đầu tư vào sáng chế này hay không?

<details>
<summary>Xem lời giải thích</summary>

**Đáp án**: Tuyệt đối không nên đầu tư.

**Giải thích chi tiết**:
- Theo định lý Carnot, hiệu suất của bất kỳ động cơ nhiệt nào hoạt động giữa hai nguồn nhiệt không thể vượt quá hiệu suất của động cơ Carnot:

$$
e \le e_{\text{Carnot}} = 1 - \frac{T_C}{T_H}
$$

- Động cơ được làm mát bằng không khí môi trường, vì vậy nhiệt độ nguồn lạnh xấp xỉ nhiệt độ phòng: $T_C \approx 300\,\mathrm K$.
- Động cơ được chế tạo hoàn toàn bằng đồng, do đó nhiệt độ nguồn nóng $T_H$ không thể vượt quá nhiệt độ nóng chảy của đồng là $1083^\circ\mathrm C = 1356\,\mathrm K$ (nếu vượt quá mức này, các chi tiết bằng đồng sẽ bị nóng chảy và biến dạng hoàn toàn).
- Hiệu suất lý tưởng tối đa mà động cơ bằng đồng có thể đạt được là:

$$
\begin{aligned}
e_{\max} &= 1 - \frac{300\,\mathrm K}{1356\,\mathrm K} \\
&\approx 0{,}78 = 78\%
\end{aligned}
$$

- Một động cơ thực tế luôn có ma sát, thất thoát nhiệt và các quá trình không thuận nghịch nên hiệu suất chắc chắn sẽ còn thấp hơn $78\%$. Khẳng định đạt hiệu suất $85\%$ của nhà phát minh là điều bất khả thi về mặt nhiệt động lực học.
</details>
