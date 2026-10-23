<!-- Source: Chapter 20 Summary, printed669–670, PDF689–690. -->

## Tóm tắt Chương 20: Nguyên lý thứ hai nhiệt động lực học

### Quá trình thuận nghịch và không thuận nghịch

Một quá trình được gọi là **thuận nghịch** (reversible) nếu chiều diễn biến của nó có thể bị đảo ngược chỉ bằng một biến đổi vô cùng nhỏ ở các điều kiện môi trường bên ngoài. Trong một quá trình thuận nghịch, hệ luôn ở trạng thái cân bằng nhiệt động hoặc vô cùng gần trạng thái cân bằng tại mọi thời điểm. Các quá trình tự nhiên như truyền nhiệt qua chênh nhiệt độ hữu hạn, ma sát và khuếch tán tự do là **không thuận nghịch** (irreversible).

![Hình tóm tắt: Quá trình thuận nghịch và không thuận nghịch](./img/young-20/b-tt-thuan-nghich.png)

*Hình tóm tắt: Sự truyền nhiệt giữa khối kim loại $70^\circ\mathrm C$ và nước $40^\circ\mathrm C$ là không thuận nghịch do chênh lệch nhiệt độ hữu hạn lớn. Ngược lại, sự truyền nhiệt giữa khối kim loại ở $0^\circ\mathrm C$ và hỗn hợp nước đá ở gần $0^\circ\mathrm C$ tiến tới giới hạn thuận nghịch khi chênh lệch nhiệt độ được giữ vô cùng nhỏ. Ở đúng cùng nhiệt độ, không có dòng nhiệt ròng.*

### Động cơ nhiệt

**Động cơ nhiệt** (heat engine) là một thiết bị nhận nhiệt lượng $Q_H > 0$ từ một nguồn nóng ở nhiệt độ $T_H$, chuyển đổi một phần năng lượng đó thành công cơ học $W > 0$, và thải phần nhiệt lượng còn lại $Q_C < 0$ (với độ lớn $|Q_C|$) ra một nguồn lạnh ở nhiệt độ thấp hơn $T_C$.

![Hình tóm tắt: Sơ đồ dòng năng lượng của động cơ nhiệt](./img/young-20/b-tt-dong-co-nhiet.png)

*Hình tóm tắt: Sơ đồ dòng năng lượng của động cơ nhiệt. Trong mỗi chu trình kín, công sinh ra bằng tổng nhiệt lượng trao đổi: $W = Q_H + Q_C$, tương đương $W = |Q_H| - |Q_C|$.*

**Hiệu suất nhiệt** $e$ của động cơ nhiệt đo lường tỷ lệ phần trăm nhiệt lượng nhận vào được chuyển hóa thành công cơ học:

$$
\begin{aligned}
e &= \frac{W}{Q_H} \\
&= 1 - \frac{|Q_C|}{|Q_H|}
\end{aligned}
$$

### Chu trình Otto

Động cơ xăng bốn kỳ hoạt động theo **chu trình Otto** lý tưởng gồm hai quá trình đoạn nhiệt xen kẽ hai quá trình đẳng tích. Hiệu suất nhiệt lý thuyết cực đại của chu trình Otto là:

$$
e = 1 - \frac{1}{r^{\gamma - 1}}
$$

trong đó $r = V_{\max} / V_{\min}$ là tỷ số nén của động cơ và $\gamma = C_p / C_V$ là tỷ số nhiệt dung riêng của chất khí.

![Hình tóm tắt: Đồ thị p-V của chu trình Otto](./img/young-20/b-tt-chu-trinh-otto.png)

*Hình tóm tắt: Đồ thị $p-V$ của chu trình Otto đối với khí lý tưởng. Quá trình $a \to b$ và $c \to d$ là các quá trình đoạn nhiệt; $b \to c$ và $d \to a$ là các quá trình đẳng tích.*

### Máy lạnh

**Máy lạnh** (refrigerator) là một thiết bị nhận nhiệt lượng $Q_C > 0$ từ một vật có nhiệt độ thấp $T_C$, cần một công ngoại lực đầu vào $W < 0$ (độ lớn $|W|$), và thải nhiệt lượng $|Q_H| = Q_C + |W|$ ra môi trường có nhiệt độ cao hơn $T_H$.

![Hình tóm tắt: Sơ đồ dòng năng lượng của máy lạnh](./img/young-20/b-tt-may-lanh.png)

*Hình tóm tắt: Sơ đồ dòng năng lượng của máy lạnh. Hệ nhận công $|W|$ từ bên ngoài để bơm nhiệt lượng $Q_C$ từ nguồn lạnh lên nguồn nóng.*

Hiệu quả hoạt động của máy lạnh được đặc trưng bởi **hệ số làm lạnh** $K$:

$$
\begin{aligned}
K &= \frac{|Q_C|}{|W|} \\
&= \frac{|Q_C|}{|Q_H| - |Q_C|}
\end{aligned}
$$

### Nguyên lý thứ hai nhiệt động lực học

Nguyên lý thứ hai nhiệt động lực học mô tả chiều hướng tự nhiên không thể đảo ngược của các hiện tượng nhiệt. Nguyên lý này có hai phát biểu tương đương nhau:
- **Phát biểu Kelvin–Planck (dạng động cơ)**: Không thể chế tạo một động cơ hoạt động theo chu trình mà kết quả duy nhất là biến đổi hoàn toàn nhiệt lượng hấp thụ từ một nguồn nhiệt thành công cơ học. Động cơ nhiệt đạt hiệu suất $100\%$ là bất khả thi.
- **Phát biểu Clausius (dạng máy lạnh)**: Không thể chế tạo một máy lạnh hoạt động theo chu trình mà kết quả duy nhất là truyền nhiệt lượng từ một vật lạnh sang một vật nóng hơn mà không tiêu thụ công cơ học.

![Hình tóm tắt: Động cơ đạt hiệu suất 100% là bất khả thi](./img/young-20/b-tt-nguyen-ly-2.png)

*Hình tóm tắt: Một động cơ nhiệt hấp thụ nhiệt $Q_H$ từ nguồn nóng và chuyển hóa toàn bộ thành công $W$ mà không thải nhiệt ra nguồn lạnh ($Q_C = 0$) là điều không thể thực hiện được theo nguyên lý thứ hai.*

### Chu trình Carnot

**Chu trình Carnot** là một chu trình lý tưởng chỉ bao gồm bốn quá trình hoàn toàn thuận nghịch: Hai quá trình giãn nở và nén đẳng nhiệt xen kẽ hai quá trình giãn nở và nén đoạn nhiệt. Một động cơ hoạt động theo chu trình Carnot giữa hai nguồn nhiệt ở nhiệt độ tuyệt đối $T_H$ và $T_C$ đạt hiệu suất nhiệt cực đại:

$$
\begin{aligned}
e_{\text{Carnot}} &= 1 - \frac{T_C}{T_H} \\
&= \frac{T_H - T_C}{T_H}
\end{aligned}
$$

Một phát biểu tương đương của nguyên lý thứ hai khẳng định rằng: Không một động cơ nhiệt nào hoạt động giữa hai nguồn nhiệt xác định có thể đạt hiệu suất cao hơn động cơ Carnot hoạt động giữa chính hai nguồn nhiệt đó.

![Hình tóm tắt: Đồ thị p-V của chu trình Carnot](./img/young-20/b-tt-chu-trinh-carnot.png)

*Hình tóm tắt: Đồ thị $p-V$ của chu trình Carnot. Chu trình gồm hai đường đẳng nhiệt ở $T_H$ và $T_C$ kết hợp với hai đường đoạn nhiệt.*

Khi vận hành ngược lại, chu trình Carnot trở thành **máy lạnh Carnot** với hệ số làm lạnh cực đại:

$$
K_{\text{Carnot}} = \frac{T_C}{T_H - T_C}
$$

Không một máy lạnh nào hoạt động giữa hai nguồn nhiệt $T_H$ và $T_C$ có thể đạt hệ số làm lạnh cao hơn máy lạnh Carnot.

### Entropy

**Entropy** $S$ là một hàm trạng thái nhiệt động lực học đóng vai trò là thước đo định lượng cho mức độ hỗn loạn của hệ. Độ biến thiên entropy của một hệ nhiệt động trong một quá trình thuận nghịch bất kỳ từ trạng thái 1 đến trạng thái 2 được định nghĩa là:

$$
\Delta S = \int_1^2 \frac{dQ}{T}
$$

Đơn vị của entropy là jun trên kelvin ($\mathrm{J/K}$).

- Đối với một chu trình thuận nghịch kín: Tổng độ biến thiên entropy của hệ luôn triệt tiêu: $\oint dQ/T = 0$.
- Đối với mọi quá trình diễn ra trong một hệ cô lập: Độ biến thiên entropy luôn thỏa mãn bất đẳng thức:

$$
\Delta S \ge 0
$$

Entropy không đổi trong các quá trình thuận nghịch ($\Delta S = 0$) và luôn gia tăng trong các quá trình không thuận nghịch ($\Delta S > 0$). Nó không bao giờ tự phát suy giảm trong một hệ cô lập.

### Entropy và trạng thái vi mô

Ở cấp độ phân tử, trạng thái nhiệt động vĩ mô của một hệ tương ứng với $w$ trạng thái vi mô khác nhau. Mức độ hỗn loạn của hệ càng cao thì số lượng trạng thái vi mô $w$ khả dĩ càng lớn.

Công thức Boltzmann thiết lập mối liên hệ trực tiếp giữa entropy vĩ mô $S$ và số trạng thái vi mô $w$:

$$
S = k \ln w
$$

trong đó $k = 1{,}381 \times 10^{-23}\,\mathrm{J/K}$ là hằng số Boltzmann.

![Hình tóm tắt: Sự gia tăng số trạng thái vi mô khi thể tích tăng gấp đôi](./img/young-20/b-tt-vi-mo-entropy.png)

*Hình tóm tắt: Khối khí gồm $N$ phân tử trong thể tích $V$ có $w$ trạng thái vi mô. Khi giãn nở tự do sang thể tích $2V$, mỗi phân tử có số vị trí khả dĩ tăng gấp đôi, làm tổng số trạng thái vi mô tăng vọt thành $2^N w$.*

Khi thể tích của khối khí gồm $N$ phân tử tăng từ $V$ lên $2V$, số trạng thái vi mô tăng thêm một thừa số $2^N$, dẫn đến độ biến thiên entropy vi mô:

$$
\begin{aligned}
\Delta S &= k \ln \frac{2^N w}{w} \\
&= n R \ln 2
\end{aligned}
$$

kết quả này hoàn toàn đồng nhất với công thức biến thiên entropy suy ra từ nhiệt động lực học vĩ mô.
