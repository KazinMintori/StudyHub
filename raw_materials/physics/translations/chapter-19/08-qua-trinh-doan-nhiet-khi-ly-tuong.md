## 19.8 Quá trình đoạn nhiệt của khí lý tưởng

Trong mục 19.5, chúng ta đã định nghĩa quá trình đoạn nhiệt là quá trình không có sự trao đổi nhiệt giữa hệ nhiệt động và môi trường xung quanh ($Q = 0$). Áp dụng nguyên lý thứ nhất của nhiệt động lực học, độ biến thiên nội năng của hệ có độ lớn bằng nhưng trái dấu với công cơ học do hệ sinh ra:

$$
\Delta U = -W
$$

Hệ thức này mang một ý nghĩa vật lý trực quan: Khi một khối khí giãn nở đoạn nhiệt và thực hiện công dương lên môi trường ($W > 0$), do đó nội năng của nó phải giảm xuống ($\Delta U < 0$), kéo theo sự suy giảm nhiệt độ của khối khí. Ngược lại, khi khối khí bị nén đoạn nhiệt, môi trường sinh công lên khối khí ($W < 0$), nội năng tăng lên ($\Delta U > 0$) và nhiệt độ của khối khí tăng cao.

Không khí ở đầu ra máy nén dùng để bơm lốp hoặc nạp bình lặn thường nóng hơn không khí đi vào. Quá trình nén nhanh hạn chế thời gian trao đổi nhiệt, nên có thể gần đúng là đoạn nhiệt.

Khi mở một chai đồ uống có gas, phần khí ngay trên mặt chất lỏng giãn nở nhanh. Nhiệt độ của phần khí giảm trong mô hình giãn nở sinh công gần đoạn nhiệt. Hơi nước có thể ngưng tụ thành một đám mây nhỏ, như minh họa ở Hình 19.14.

::: Warning Cảnh báo: Làm nóng và làm lạnh không cần nhiệt
Trong ngôn ngữ đời thường, người ta thường đồng nhất khái niệm "nóng lên" với việc "nhận thêm nhiệt lượng", và "lạnh đi" với việc "mất nhiệt lượng". Tuy nhiên trong nhiệt động lực học, nhiệt độ của một hệ hoàn toàn có thể tăng lên hoặc hạ xuống mà không cần có bất kỳ sự truyền nhiệt nào ($Q = 0$). Trong quá trình nén đoạn nhiệt, nhiệt độ của chất khí tăng lên hoàn toàn do công cơ học tác dụng lên nó được biến đổi trực tiếp thành nội năng.
:::

### Mối liên hệ giữa thể tích, nhiệt độ và áp suất

Bây giờ chúng ta sẽ thiết lập phương trình định lượng mô tả mối liên hệ giữa các thông số trạng thái $p, V, T$ trong quá trình đoạn nhiệt thuận nghịch của một khối khí lý tưởng. Coi số mol không đổi và $C_V$ gần như không đổi trong khoảng nhiệt độ đang xét. Xét một biến đổi đoạn nhiệt vô cùng nhỏ: Vì $dQ = 0$ nên nguyên lý thứ nhất cho ta $dU = -dW = -p dV$.

Theo phương trình (19.13), độ biến thiên nội năng của một khối khí lý tưởng luôn được tính bởi $dU = n C_V dT$. Do đó:

$$
n C_V dT = -p dV \tag{19.19}
$$

Để thu được mối liên hệ chỉ chứa thể tích $V$ và nhiệt độ $T$, chúng ta sử dụng phương trình trạng thái khí lý tưởng dưới dạng $p = \frac{nRT}{V}$ để khử áp suất $p$:

$$
n C_V dT = -\frac{n R T}{V} dV
$$

Chia cả hai vế của phương trình cho $n T$ và chuyển các số hạng về cùng một vế:

$$
\frac{dT}{T} + \frac{R}{C_V} \frac{dV}{V} = 0
$$

Nhớ lại rằng $C_p - C_V = R$, do đó:

$$
\begin{aligned}
\frac{R}{C_V} &= \frac{C_p - C_V}{C_V} \\
&= \gamma - 1
\end{aligned}
$$

Thay kết quả này vào biểu thức trên, ta thu được phương trình vi phân cơ bản của quá trình đoạn nhiệt:

$$
\frac{dT}{T} + (\gamma - 1) \frac{dV}{V} = 0 \tag{19.20}
$$

Vì $\gamma > 1$ nên thừa số $(\gamma - 1)$ luôn dương. Phương trình (19.20) cho thấy vi phân $dT$ và $dV$ luôn trái dấu: Khi thể tích tăng ($dV > 0$) thì nhiệt độ phải giảm ($dT < 0$), và ngược lại.

Lấy tích phân hai vế của phương trình (19.20) cho một biến đổi hữu hạn từ trạng thái ban đầu đến trạng thái cuối:

$$
\ln T + (\gamma - 1) \ln V = C
$$

với $C$ là hằng số tích phân. Sử dụng tính chất của hàm logarit:

$$
\ln(T V^{\gamma - 1}) = \text{const}
$$

Lấy hàm mũ hai vế, ta thu được mối liên hệ giữa nhiệt độ và thể tích trong quá trình đoạn nhiệt của khí lý tưởng:

$$
T V^{\gamma - 1} = \text{const} \tag{19.21}
$$

Đối với hai trạng thái nhiệt động bất kỳ $(T_1, V_1)$ và $(T_2, V_2)$ trên cùng một đường đoạn nhiệt:

$$
T_1 V_1^{\gamma - 1} = T_2 V_2^{\gamma - 1} \tag{19.22}
$$

Chúng ta cũng có thể chuyển đổi phương trình (19.22) thành mối liên hệ giữa áp suất và thể tích. Nhiệt độ trong các hệ thức này luôn phải tính bằng kelvin. Từ phương trình khí lý tưởng, thay $T = \frac{pV}{nR}$ vào biểu thức $T V^{\gamma - 1} = \text{const}$:

$$
\left(\frac{p V}{n R}\right) V^{\gamma - 1} = \text{const}
$$

Vì số mol $n$ và hằng số khí $R$ không đổi, ta thu được định luật Poisson mô tả đường đoạn nhiệt của khí lý tưởng:

$$
p V^\gamma = \text{const} \tag{19.23}
$$

Đối với hai trạng thái $(p_1, V_1)$ và $(p_2, V_2)$ bất kỳ:

$$
p_1 V_1^\gamma = p_2 V_2^\gamma \tag{19.24}
$$

### So sánh đường đoạn nhiệt và đường đẳng nhiệt trên giản đồ pV

Hình 19.20 biểu diễn đường đoạn nhiệt của một khối khí lý tưởng trên giản đồ $pV$.

![Hình 19.20: Giản đồ $pV$ của quá trình đoạn nhiệt ($Q = 0$) đối với một khối khí lý tưởng. Khi khí giãn nở từ $V_a$ đến $V_b$, khí sinh công dương lên môi trường, nội năng giảm ($\Delta U = -W < 0$) và nhiệt độ giảm từ $T + dT$ xuống $T$.](../img/young-19/b-hinh-19-20.png)

Để so sánh hình dạng hình học của hai đường trên giản đồ $pV$:

1. Đường đẳng nhiệt tuân theo định luật Boyle–Mariotte: $p = \frac{\text{const}}{V}$. Độ dốc của đường tiếp tuyến là:

$$
\left(\frac{dp}{dV}\right)_{\text{đẳng nhiệt}} = -\frac{p}{V}
$$

2. Đường đoạn nhiệt tuân theo định luật Poisson: $p = \frac{\text{const}}{V^\gamma}$. Lấy đạo hàm theo thể tích $V$:

$$
\left(\frac{dp}{dV}\right)_{\text{đoạn nhiệt}} = -\gamma \frac{p}{V}
$$

Vì tỷ số nhiệt dung $\gamma > 1$, tại bất kỳ điểm giao nhau $(p, V)$ nào trên giản đồ $pV$, độ dốc âm của đường đoạn nhiệt luôn có độ lớn lớn hơn độ dốc của đường đẳng nhiệt một thừa số đúng bằng $\gamma$. Nói cách khác, trên giản đồ $pV$, đường đoạn nhiệt luôn dốc hơn đường đẳng nhiệt đi qua cùng một điểm trạng thái. Khi khối khí giãn nở, áp suất trong quá trình đoạn nhiệt tụt nhanh hơn so với quá trình đẳng nhiệt vì nhiệt độ của khối khí bị giảm sút.

Các hệ thức lũy thừa trên có điều kiện áp dụng cụ thể. Hệ phải cách nhiệt đủ tốt, hoặc biến đổi đủ nhanh để trao đổi nhiệt không đáng kể, đồng thời không rời xa cân bằng nhiệt và cơ học.

“Nhanh” ở đây được so với thời gian trao đổi nhiệt với môi trường. Còn điều kiện gần cân bằng được xét so với thời gian hệ tự thiết lập cân bằng bên trong. Một quá trình đoạn nhiệt bất thuận nghịch bất kỳ không nhất thiết tuân theo $pV^\gamma=\text{hằng số}$.

### Công sinh ra trong quá trình đoạn nhiệt

Chúng ta có thể tính công cơ học $W$ do một khối khí lý tưởng sinh ra trong quá trình đoạn nhiệt bằng hai phương pháp tương đương:

1. Cách tiếp cận từ biến thiên nội năng: Vì $Q = 0$, công do hệ thực hiện đơn giản bằng độ giảm nội năng:

$$
\begin{aligned}
W &= -\Delta U \\
&= n C_V(T_1 - T_2) \tag{19.25}
\end{aligned}
$$

2. Cách tiếp cận từ áp suất và thể tích: Sử dụng hệ thức $C_V = \frac{R}{\gamma - 1}$ và các mối liên hệ $n R T_1 = p_1 V_1$, $n R T_2 = p_2 V_2$, ta biến đổi phương trình (19.25) thành:

$$
W = \frac{1}{\gamma - 1}(p_1 V_1 - p_2 V_2) \tag{19.26}
$$

Nếu quá trình là một sự giãn nở ($V_2 > V_1$), nhiệt độ và áp suất đều giảm, kéo theo $p_1 V_1 > p_2 V_2$ và công $W$ mang giá trị dương. Ngược lại, nếu quá trình là một sự nén khí ($V_2 < V_1$), công $W$ mang giá trị âm, phù hợp với quy ước công được thực hiện lên khối khí.

::: Tip Ứng dụng sinh học: Thở ra khí ấm hay khí mát
Hãy đưa bàn tay lại gần miệng một khoảng vài centimet, mở rộng miệng và phà hơi: Bạn sẽ cảm nhận luồng khí thở ra rất ấm áp. Bây giờ, hãy lặp lại thí nghiệm nhưng chúm môi lại thật nhỏ và thổi mạnh qua khe môi: Bạn sẽ thấy luồng khí mát hơn rõ rệt (Hình ứng dụng 19.1).

![Hình ứng dụng 19.1: Thở ra khí ấm khi mở rộng miệng và thổi ra khí mát khi chúm môi: Minh họa sinh động cho hiện tượng giãn nở đoạn nhiệt trong đời sống hàng ngày.](../img/young-19/b-ung-dung-01.png)

Một mô hình định tính liên hệ hiện tượng này với sự giãn nở nhanh của khí khi thoát qua khe môi. Nếu theo dõi một phần khí đang giãn nở, bỏ qua trao đổi nhiệt và coi nó sinh công lên môi trường, nội năng của phần khí ấy giảm.

Khi mở rộng miệng và thở chậm, chênh lệch áp suất nhỏ hơn nên hiệu ứng giãn nở này yếu hơn. Tuy nhiên, cảm giác trên tay còn liên quan đến luồng khí cuốn theo không khí xung quanh và sự truyền nhiệt tại da. Không thể dùng riêng phương trình của một hệ khí kín gần cân bằng để định lượng toàn bộ luồng thổi.

:::

::: Example Ví dụ 19.7: Nén đoạn nhiệt trong động cơ diesel
Tỷ số nén của một động cơ diesel là $15{,}0 : 1$, nghĩa là không khí trong xi lanh bị nén từ thể tích ban đầu $V_1$ xuống thể tích nhỏ nhất lúc nén là $V_2 = V_1 / 15{,}0$ (Hình 19.21). Không khí đi vào buồng đốt ở áp suất ban đầu $p_1 = 1{,}01 \times 10^5\text{ Pa}$ và nhiệt độ ban đầu $T_1 = 27^\circ\text{C} = 300\text{ K}$. Coi không khí là khí lý tưởng có tỷ số nhiệt dung $\gamma = 1{,}40$ và nhiệt dung mol đẳng tích $C_V = 20{,}8\text{ J/(mol}\cdot\text{K)}$. Thể tích ban đầu của xi lanh là $V_1 = 1{,}00\text{ L}$ (tương ứng $1{,}00 \times 10^{-3}\text{ m}^3$).

(a) Tính nhiệt độ cuối cùng $T_2$ và áp suất cuối cùng $p_2$ của khối không khí sau khi nén.

(b) Tính công cơ học $W$ do khối khí thực hiện trong quá trình nén này.

![Hình 19.21: Quá trình nén đoạn nhiệt không khí trong xi lanh của một động cơ diesel từ thể tích ban đầu $V_1$ xuống thể tích nén cực đại $V_2 = V_1 / 15{,}0$.](../img/young-19/b-hinh-19-21.png)

**Tóm tắt:**

- Tỷ số nén: $V_1 / V_2 = 15{,}0$.
- Trạng thái ban đầu: $p_1 = 1{,}01 \times 10^5\text{ Pa}$, $T_1 = 300\text{ K}$, $V_1 = 1{,}00 \times 10^{-3}\text{ m}^3$.
- Thông số khí: $\gamma = 1{,}40$, $C_V = 20{,}8\text{ J/(mol}\cdot\text{K)}$.
- Yêu cầu: Tính $T_2$, $p_2$ và công $W$.

**Hướng đi:**

1. Áp dụng phương trình đoạn nhiệt liên hệ giữa nhiệt độ và thể tích $T_1 V_1^{\gamma - 1} = T_2 V_2^{\gamma - 1}$ để tìm $T_2$.
2. Áp dụng phương trình đoạn nhiệt liên hệ giữa áp suất và thể tích $p_1 V_1^\gamma = p_2 V_2^\gamma$ để tìm $p_2$.
3. Tính công thực hiện bằng công thức liên hệ áp suất và thể tích $W = \frac{1}{\gamma - 1}(p_1 V_1 - p_2 V_2)$, sau đó kiểm tra lại bằng công thức biến thiên nội năng $W = n C_V(T_1 - T_2)$.

**Bài giải:**

(a) Từ phương trình liên hệ giữa nhiệt độ và thể tích trong quá trình đoạn nhiệt, ta có:

$$
\begin{aligned}
T_2 &= T_1 \left(\frac{V_1}{V_2}\right)^{\gamma - 1} \\
&= (300\text{ K})(15{,}0)^{0{,}40} \\
&= 886\text{ K}
\end{aligned}
$$

Giá trị này tương đương với $613^\circ\text{C}$.

Áp suất cuối cùng của khối khí sau khi nén được xác định bởi:

$$
\begin{aligned}
p_2 &= p_1 \left(\frac{V_1}{V_2}\right)^\gamma \\
&=p_1(15{,}0)^{1{,}40} \\
&= 44{,}8 \times 10^5\text{ Pa}
\end{aligned}
$$

Áp suất này tương đương khoảng $44\text{ atm}$.

(b) Áp dụng phương trình (19.26) để tính công thực hiện bởi khối khí:

$$
W = \frac{1}{\gamma - 1}(p_1 V_1 - p_2 V_2)
$$

Vì $V_2 = V_1 / 15{,}0$, thay các giá trị chưa làm tròn trung gian cho:

$$
\begin{aligned}
W &= \frac{p_1 V_1 - p_2 V_2}{\gamma - 1} \\
&\approx -493{,}4\,\mathrm J
\end{aligned}
$$

Chúng ta có thể kiểm tra lại kết quả này bằng phương trình (19.25). Trước hết, số mol không khí trong xi lanh là:

$$
n = \frac{p_1 V_1}{R T_1} = 0{,}0405\text{ mol}
$$

Khi đó, công cơ học tính theo biến thiên nội năng là:

$$
\begin{aligned}
W &= n C_V(T_1 - T_2) \\
&= -494\text{ J}
\end{aligned}
$$

Dùng $C_V=20{,}8\,\mathrm{J/(mol\,K)}$ đã làm tròn cho công xấp xỉ $-493{,}8\,\mathrm J$, tức $-494\,\mathrm J$. Độ lệch nhỏ so với phép tính trên do $C_V$ và $\gamma$ được làm tròn riêng. Nếu dùng nhất quán $C_V=R/(\gamma-1)$ thì hai cách tính cho cùng kết quả.

**Đánh giá:** Công mang dấu âm vì môi trường thực hiện công nén lên khí. Nếu nén đẳng nhiệt cùng tỉ số thể tích, áp suất cuối chỉ xấp xỉ 15 lần ban đầu. Nén đoạn nhiệt làm nhiệt độ tăng, nên áp suất cuối lớn hơn đáng kể. Nhiệt độ cao đạt được ở cuối hành trình nén cho phép nhiên liệu diesel được phun vào tự bốc cháy mà không cần bugi đánh lửa.
:::

::: Info Tự kiểm tra 19.8
**Câu hỏi:** Bạn có bốn mẫu khí lý tưởng khác nhau, mỗi mẫu đều có cùng số mol khí, cùng nhiệt độ, thể tích và áp suất ban đầu. Nén mỗi mẫu khí về một nửa thể tích ban đầu ($V_2 = V_1 / 2$). Hãy sắp xếp bốn mẫu khí theo thứ tự áp suất cuối cùng từ cao nhất đến thấp nhất: (i) Khí đơn nguyên tử nén đẳng nhiệt. (ii) Khí đơn nguyên tử nén đoạn nhiệt. (iii) Khí lưỡng nguyên tử nén đẳng nhiệt. (iv) Khí lưỡng nguyên tử nén đoạn nhiệt.

<details><summary>Xem lời giải thích</summary>

**Trả lời:** Thứ tự sắp xếp từ cao nhất đến thấp nhất là: (ii), (iv), (i) và (iii) đồng hạng.

- Đối với các mẫu khí nén đẳng nhiệt (i) và (iii): Phương trình trạng thái là $pV = \text{const}$. Khi thể tích giảm một nửa ($V_2 = V_1 / 2$), áp suất cuối cùng tăng lên gấp 2 lần áp suất ban đầu ($p_2 = 2 p_1$), bất kể chất khí là đơn nguyên tử hay lưỡng nguyên tử. Do đó mẫu (i) và (iii) có cùng áp suất cuối cùng.
- Đối với các mẫu khí nén đoạn nhiệt (ii) và (iv): Phương trình trạng thái là $p V^\gamma = \text{const}$, suy ra áp suất cuối cùng tăng lên theo thừa số $2^\gamma$:

$$
p_2 = p_1 \cdot 2^\gamma
$$

- Mẫu (ii) là khí đơn nguyên tử có $\gamma = 5/3 \approx 1{,}67$: Áp suất cuối cùng tăng lên theo thừa số $2^{5/3} \approx 3{,}17$ lần áp suất ban đầu.
- Mẫu (iv) là khí lưỡng nguyên tử có $\gamma = 7/5 = 1{,}40$: Áp suất cuối cùng tăng lên theo thừa số $2^{7/5} \approx 2{,}64$ lần áp suất ban đầu.

Vì $3{,}17 > 2{,}64 > 2{,}00$, thứ tự áp suất cuối cùng từ cao nhất đến thấp nhất là: (ii) > (iv) > (i) = (iii).
</details>
:::
