## 42.2. Phổ phân tử

Trong các nguyên tử cô lập, quang phổ phát xạ và hấp thụ chỉ bắt nguồn từ sự chuyển mức giữa các trạng thái năng lượng của electron. Đối với các phân tử, bức xạ điện từ không chỉ phản ánh sự thay đổi trạng thái điện tử của các electron, mà còn phản ánh hai dạng chuyển động nội tại của các hạt nhân: Sự quay của toàn bộ phân tử quanh khối tâm và sự dao động của các hạt nhân nguyên tử xung quanh vị trí cân bằng bền.

Năng lượng toàn phần của một phân tử có thể phân tách thành ba phần độc lập:
1. **Năng lượng điện tử (Electronic energy)**: Năng lượng chuyển động của các electron trong trường tĩnh điện của các hạt nhân, có độ lớn cỡ $1$ đến $10\,\mathrm{eV}$, tương ứng với các photon nằm trong vùng khả kiến và vùng tử ngoại.
2. **Năng lượng dao động (Vibrational energy)**: Năng lượng dao động tuần hoàn của các hạt nhân dọc theo trục liên kết, có độ lớn cỡ $0{,}1$ đến $1\,\mathrm{eV}$, tương ứng với các photon vùng hồng ngoại.
3. **Năng lượng quay (Rotational energy)**: Động năng quay của phân tử quanh khối tâm, có độ lớn rất nhỏ, cỡ $10^{-4}$ đến $10^{-2}\,\mathrm{eV}$, tương ứng với photon vùng vi sóng và hồng ngoại xa.

Do thang năng lượng của ba dạng chuyển động có sự chênh lệch nhau hàng chục đến hàng nghìn lần:

$$
\Delta E_{\mathrm{elec}} \gg \Delta E_{\mathrm{vib}} \gg \Delta E_{\mathrm{rot}}
$$

Trong mô hình gần đúng đang xét, ta khảo sát các mức quay và dao động khi trạng thái điện tử được giữ cố định.

### Các mức năng lượng quay của phân tử hai nguyên tử

Xét mô hình đơn giản nhất là phân tử hai nguyên tử gồm hai hạt nhân mang khối lượng $m_1$ và $m_2$ được liên kết chặt chẽ ở khoảng cách cân bằng $r_0$. Ta xem phân tử như một quả tạ cứng quay trong không gian xung quanh trục đi qua khối tâm và vuông góc với đường nối hai hạt nhân.

![Hình 42.4: Mô hình phân tử hai nguyên tử gồm hai chất điểm khối lượng $m_1$ và $m_2$ cách nhau khoảng cách cân bằng $r_0$, quay quanh trục đi qua khối tâm (cm). Khoảng cách từ các chất điểm đến khối tâm lần lượt là $r_1$ và $r_2$.](../img/young-42/hinh-42-04.png)

Vị trí của khối tâm được xác định bởi điều kiện cân bằng mômen:

$$
m_1 r_1 = m_2 r_2
$$

Kết hợp với điều kiện khoảng cách $r_1 + r_2 = r_0$, ta tìm được khoảng cách từ mỗi nguyên tử đến khối tâm:

$$
\begin{aligned}
r_1 &= \frac{m_2}{m_1 + m_2} r_0, \\
r_2 &= \frac{m_1}{m_1 + m_2} r_0
\end{aligned}
$$

Mômen quán tính $I$ của phân tử đối với trục quay đi qua khối tâm là:

$$
I = m_1 r_1^2 + m_2 r_2^2 \tag{42.5}
$$

Thay các biểu thức của $r_1$ và $r_2$ vào biểu thức mômen quán tính:

$$
\begin{aligned}
I &= \frac{m_1 m_2^2 + m_2 m_1^2}{(m_1 + m_2)^2} r_0^2 \\
&= \frac{m_1 m_2}{m_1 + m_2} r_0^2
\end{aligned}
$$

Ta định nghĩa **khối lượng rút gọn** (reduced mass) $m_r$ của hệ hai nguyên tử:

$$
m_r = \frac{m_1 m_2}{m_1 + m_2} \tag{42.4}
$$

Khi đó, mômen quán tính của phân tử hai nguyên tử được viết dưới dạng gọn gàng tương đương với một chất điểm khối lượng $m_r$ chuyển động ở khoảng cách $r_0$ so với trục quay:

$$
I = m_r r_0^2 \tag{42.6}
$$

Theo cơ học lượng tử, độ lớn của mômen động lượng quay $L$ bị lượng tử hóa với số lượng tử quay $l = 0, 1, 2, \dots$:

$$
L = \sqrt{l(l+1)}\,\hbar \tag{42.2}
$$

Trong đó $l$ là số lượng tử quay. Động năng quay bằng năng lượng toàn phần khi chọn thế năng không phụ thuộc góc bằng không:

$$
E=\frac{L^2}{2I}\tag{42.1}
$$

Do đó, các mức năng lượng quay cho phép của phân tử hai nguyên tử nhận các giá trị gián đoạn:

$$
E_l = l(l+1)\frac{\hbar^2}{2I} \tag{42.3}
$$

Mức quay cơ bản ứng với $l = 0$ có năng lượng bằng không ($E_0 = 0$), nghĩa là ở mức này phân tử hoàn toàn không tự quay. Các mức năng lượng kích thích tiếp theo lần lượt là:

$$
\begin{aligned}
E_1 &= 2\left(\frac{\hbar^2}{2I}\right) = \frac{\hbar^2}{I}, \\
E_2 &= 6\left(\frac{\hbar^2}{2I}\right) = 3\,\frac{\hbar^2}{I}, \\
E_3 &= 12\left(\frac{\hbar^2}{2I}\right) = 6\,\frac{\hbar^2}{I}
\end{aligned}
$$

![Hình 42.5: Các mức năng lượng quay từ $l=0$ đến $l=4$. Khoảng cách giữa các mức liên tiếp tăng theo số lượng tử quay.](../img/young-42/hinh-42-05.png)

Để một phân tử có thể tương tác với sóng điện từ để hấp thụ hoặc phát xạ photon trong các chuyển mức quay thuần túy, phân tử bắt buộc phải có một mômen lưỡng cực điện vĩnh cửu (chẳng hạn phân tử phân cực như $\mathrm{CO}, \mathrm{HCl}$). Các phân tử đối xứng hai nguyên tử đồng hạch như $\mathrm{H}_2, \mathrm{N}_2, \mathrm{O}_2$ không có mômen lưỡng cực điện vĩnh cửu, nên chúng không có các chuyển mức quay thuần túy qua cơ chế lưỡng cực điện này.

Quy tắc chọn lọc cho các chuyển mức quay lưỡng cực điện là:

$$
\Delta l = \pm 1
$$

Khi phân tử hấp thụ một photon để chuyển từ mức $l$ lên mức $l+1$, năng lượng của photon bị hấp thụ bằng độ chênh lệch năng lượng giữa hai mức:

$$
\begin{aligned}
\Delta E &= E_{l+1} - E_l \\
&= (l+1)\frac{\hbar^2}{I}
\end{aligned}
$$

với bước rút gọn đại số $[(l+1)(l+2) - l(l+1)] / 2 = l+1$.

Tần số photon tương ứng là $f = \Delta E / h$:

$$
\begin{aligned}
f &= \frac{(l+1)\hbar^2}{h I} \\
&= (l+1)\frac{h}{4\pi^2 I}
\end{aligned}
$$

Khoảng cách tần số giữa hai vạch hấp thụ kế tiếp nhau trong phổ quay là một hằng số không đổi:

$$
\Delta f = \frac{h}{4\pi^2 I}
$$

Đặc tính cách đều tuyệt đối này là dấu hiệu thực nghiệm đặc trưng của phổ quay thuần túy. Bằng cách đo khoảng cách tần số $\Delta f$ trong vùng vi sóng, người ta xác định được mômen quán tính $I$, và từ đó tính được khoảng cách liên kết $r_0$ giữa các hạt nhân với độ chính xác cao.

### Ví dụ 42.2: Phổ quay của phân tử carbon monoxide

Khoảng cách giữa hai hạt nhân trong phân tử carbon monoxide ($\mathrm{CO}$) là $r_0 = 0{,}1128\,\mathrm{nm}$. Khối lượng của đồng vị carbon phổ biến nhất là $1{,}993 \times 10^{-26}\,\mathrm{kg}$, và của đồng vị oxy phổ biến nhất là $2{,}656 \times 10^{-26}\,\mathrm{kg}$.

(a) Tìm năng lượng của ba mức năng lượng quay thấp nhất của phân tử $\mathrm{CO}$. Biểu diễn kết quả theo đơn vị $\mathrm{meV}$ ($1\,\mathrm{meV} = 10^{-3}\,\mathrm{eV}$).
(b) Tìm bước sóng của photon phát xạ khi phân tử chuyển từ mức $l = 2$ xuống mức $l = 1$.

**Nhận diện và thiết lập**: Bài toán khảo sát các mức năng lượng quay của phân tử hai nguyên tử. Đầu tiên, ta tính khối lượng rút gọn $m_r$ từ phương trình (42.4), sau đó tính mômen quán tính $I$ từ phương trình (42.5). Năng lượng của các mức quay $E_l$ được xác định theo phương trình (42.3).

Trong câu (b), photon phát xạ có năng lượng bằng hiệu năng lượng giữa mức ban đầu $l = 2$ và mức cuối $l = 1$, tuân theo quy tắc chọn lọc $\Delta l = 1 - 2 = -1$. Bước sóng photon được tính từ hệ thức $E = hc / \lambda$.

**Thực hiện**:
(a) Thay khối lượng hai đồng vị $m_1 = 1{,}993 \times 10^{-26}\,\mathrm{kg}$ và $m_2 = 2{,}656 \times 10^{-26}\,\mathrm{kg}$ vào biểu thức khối lượng rút gọn:

$$
\begin{aligned}
m_r &= \frac{m_1 m_2}{m_1 + m_2} \\
&= 1{,}139 \times 10^{-26}\,\mathrm{kg}
\end{aligned}
$$

Mômen quán tính của phân tử với khoảng cách hạt nhân $r_0 = 0{,}1128 \times 10^{-9}\,\mathrm m$ là:

$$
\begin{aligned}
I &= m_r r_0^2 \\
&= 1{,}449 \times 10^{-46}\,\mathrm{kg\cdot m^2}
\end{aligned}
$$

Đại lượng năng lượng cơ sở $\hbar^2 / (2I)$ có giá trị:

$$
\frac{\hbar^2}{2I} = 3{,}838 \times 10^{-23}\,\mathrm J
$$

Đổi sang đơn vị electron-volt và millielectron-volt:

$$
\begin{aligned}
\frac{\hbar^2}{2I} &= 2{,}395 \times 10^{-4}\,\mathrm{eV} \\
&= 0{,}2395\,\mathrm{meV}
\end{aligned}
$$

Theo biểu thức năng lượng quay, các mức năng lượng là $E_l = l(l+1)(0{,}2395\,\mathrm{meV})$. Lần lượt thay $l = 0, 1, 2$:
- Với $l = 0$: $E_0 = 0$
- Với $l=1$, thay vào công thức được $E_1=2(0{,}2395\,\mathrm{meV})$, tức $0{,}479\,\mathrm{meV}$.
- Với $l=2$, thay vào công thức được $E_2=6(0{,}2395\,\mathrm{meV})$, tức $1{,}437\,\mathrm{meV}$.

(b) Năng lượng của photon phát xạ khi chuyển từ mức $l = 2$ về $l = 1$ là:

$$
\begin{aligned}
E &= E_2 - E_1 \\
&= 0{,}958\,\mathrm{meV}
\end{aligned}
$$

tương đương $0{,}958 \times 10^{-3}\,\mathrm{eV}$.

Bước sóng của photon phát xạ được tính từ hệ thức:

$$
\begin{aligned}
\lambda &= \frac{hc}{E} \\
&= 1{,}29 \times 10^{-3}\,\mathrm m \\
&= 1{,}29\,\mathrm{mm}
\end{aligned}
$$

**Đánh giá**: Photon phát xạ có bước sóng $1{,}29\,\mathrm{mm}$, nằm trong dải vi sóng của quang phổ điện từ. Bức xạ phát xạ từ các chuyển mức quay của phân tử $\mathrm{CO}$ trong các đám mây khí liên sao là một trong những công cụ quan trọng hàng đầu giúp các nhà thiên văn học vẽ bản đồ phân bố vật chất và cấu trúc của Ngân Hà.

::: tip Khái niệm cốt lõi: Năng lượng quay phân tử
Các mức năng lượng quay của phân tử hai nguyên tử phụ thuộc vào mômen quán tính $I$ và số lượng tử quay $l$. Khoảng cách giữa các mức năng lượng lân cận tăng tuyến tính theo $l$, và các chuyển mức phát xạ/hấp thụ tuân theo quy tắc chọn lọc $\Delta l = \pm 1$.
:::

### Các mức năng lượng dao động của phân tử hai nguyên tử

Khi hai hạt nhân của phân tử hai nguyên tử bị kích thích dao động dọc theo đường nối tâm, thế năng tương tác của chúng gần vị trí cân bằng bền $r_0$ có thể được xấp xỉ bằng một hàm bậc hai parabol.

![Hình 42.6: Mô hình phân tử hai nguyên tử dao động dọc theo trục liên kết, được mô hình hóa bằng hai khối lượng $m_1$ và $m_2$ nối với nhau bằng một lò xo lý tưởng có độ cứng hiệu dụng $k'$.](../img/young-42/hinh-42-06.png)

Khi hạt nhân dịch chuyển một đoạn nhỏ $x = r - r_0$ ra khỏi vị trí cân bằng, lực phục hồi kéo hạt nhân trở lại vị trí cân bằng tuân theo định luật Hooke:

$$
F = -k'(r - r_0)
$$

Trong đó $k'$ là **hằng số lực hiệu dụng** của liên kết hóa học. Thế năng tương ứng là thế năng của một dao động tử điều hòa:

$$
U(r) = \frac{1}{2}k'(r - r_0)^2
$$

Tần số góc cổ điển của dao động hai vật nối với lò xo được xác định thông qua khối lượng rút gọn $m_r$:

$$
\omega = \sqrt{\frac{k'}{m_r}}
$$

Áp dụng cơ học lượng tử cho dao động tử điều hòa một chiều, các mức năng lượng dao động cho phép bị lượng tử hóa với $n = 0, 1, 2, \dots$:

$$
E_n = \left(n + \frac{1}{2}\right)\hbar \omega \tag{42.7}
$$

Trong đó $n$ là **số lượng tử dao động**. Điểm đặc biệt của cơ học lượng tử là ngay ở trạng thái thấp nhất ($n = 0$), phân tử vẫn sở hữu một năng lượng dao động khác không, gọi là **năng lượng điểm không** (zero-point energy):

$$
E_0 = \frac{1}{2}\hbar \omega
$$

Khoảng cách năng lượng giữa hai mức dao động liên tiếp liền kề là một hằng số đồng đều:

$$
\Delta E = E_{n+1} - E_n = \hbar \omega \tag{42.8}
$$

![Hình 42.7: Giản đồ các mức năng lượng dao động của phân tử hai nguyên tử từ $n = 0$ đến $n = 3$. Các mức năng lượng cách đều nhau một khoảng $\hbar \omega$. Mức cơ bản $n = 0$ có năng lượng điểm không bằng $\frac{1}{2}\hbar \omega$.](../img/young-42/hinh-42-07.png)

Quy tắc chọn lọc cho các chuyển mức dao động lưỡng cực điện là:

$$
\Delta n = \pm 1
$$

Do đó, trong gần đúng dao động tử điều hòa, mọi chuyển mức hấp thụ hoặc phát xạ photon dao động đều có năng lượng photon bằng đúng $\hbar \omega$, tương ứng với một vạch phổ dao động duy nhất trong dải hồng ngoại.

### Phổ dao động - quay kết hợp

Trong thực tế, sự dao động và sự quay diễn ra đồng thời. Tổng năng lượng nội tại của phân tử hai nguyên tử ở trạng thái lượng tử $(n, l)$ là tổng của năng lượng dao động và năng lượng quay:

$$
\begin{aligned}
&E(n, l) = E_{\mathrm{vib}} + E_{\mathrm{rot}}, \\
&E_{\mathrm{vib}} = \left(n + \frac{1}{2}\right)\hbar \omega, \\
&E_{\mathrm{rot}} = l(l+1)\frac{\hbar^2}{2I}
\end{aligned}\tag{42.9}
$$

Vì khoảng cách giữa các mức dao động $\hbar \omega$ lớn hơn rất nhiều so với khoảng cách giữa các mức quay $\hbar^2 / I$, mỗi mức dao động $n$ chứa một tập hợp gồm rất nhiều mức quay $l$ nằm san sát nhau.

![Hình 42.8: Giản đồ mức năng lượng dao động - quay kết hợp của phân tử hai nguyên tử. Mỗi mức dao động $n$ chứa một thang các mức quay $l$. Các mũi tên phát xạ đi từ mức dao động cao xuống mức thấp hơn, với $\Delta n=-1$ và $\Delta l=\pm1$, tạo nên nhánh P ($\Delta l = -1$, bước sóng dài hơn) và nhánh R ($\Delta l = +1$, bước sóng ngắn hơn). Chuyển mức $\Delta l = 0$ thuần túy dao động bị cấm.](../img/young-42/hinh-42-08.png)

Khi phân tử hấp thụ hoặc phát xạ photon, cả trạng thái dao động và trạng thái quay đều thay đổi đồng thời. Các quy tắc chọn lọc là:

$$
\Delta n = \pm 1, \quad \Delta l = \pm 1
$$

Chuyển dịch với $\Delta l = 0$ (chỉ đổi mức dao động mà không đổi mức quay) bị cấm đối với các phân tử hai nguyên tử đơn giản. Do đó, khi phân tử chuyển mức dao động từ $n$ lên $n+1$, phổ hấp thụ tách thành hai nhánh vạch đặc trưng:
- **Nhánh R** ($\Delta l = +1$): Phân tử chuyển từ trạng thái quay $l$ lên $l+1$. Năng lượng photon hấp thụ lớn hơn năng lượng dao động thuần túy $\hbar \omega$:

$$
\Delta E = \hbar \omega + (l+1)\frac{\hbar^2}{I}
$$

- **Nhánh P** ($\Delta l = -1$): Phân tử chuyển từ trạng thái quay $l$ xuống $l-1$. Năng lượng photon hấp thụ nhỏ hơn năng lượng dao động thuần túy $\hbar \omega$:

$$
\Delta E = \hbar \omega - l\frac{\hbar^2}{I}
$$

Giữa nhánh P và nhánh R có một khoảng trống không có vạch phổ tại đúng tần số dao động thuần túy $\hbar \omega$ (vị trí tương ứng với $\Delta l = 0$ bị cấm).

![Hình 42.9: Bản ghi quang phổ dải phân tử thực nghiệm đặc trưng. Các dải vạch tối hấp thụ nằm san sát nhau phản ánh các chuyển dịch dao động - quay chi tiết của phân tử.](../img/young-42/hinh-42-09.png)

### Ví dụ 42.3: Phổ dao động - quay của phân tử carbon monoxide

Xét lại phân tử $\mathrm{CO}$ trong Ví dụ 42.2. Tìm bước sóng của photon phát xạ bởi phân tử $\mathrm{CO}$ khi năng lượng dao động của nó thay đổi và năng lượng quay của nó (a) ban đầu bằng không và (b) cuối cùng bằng không.

**Nhận diện và thiết lập**: Bài toán khảo sát sự chuyển mức dao động - quay kết hợp của phân tử hai nguyên tử. Vì photon được phát xạ khi năng lượng dao động thay đổi, quy tắc chọn lọc $\Delta n = -1$ cho biết số lượng tử dao động $n$ giảm đi 1 đơn vị trong cả hai trường hợp.

Trong phần (a), giá trị ban đầu của số lượng tử quay là $l = 0$. Quy tắc chọn lọc $\Delta l = \pm 1$ đòi hỏi giá trị cuối cùng của $l$ phải là 1 (vì $l$ không thể âm). Do đó, năng lượng quay của phân tử tăng lên, và năng lượng photon phát xạ bằng độ giảm năng lượng dao động trừ đi phần năng lượng quay tăng thêm.

Trong phần (b), giá trị cuối cùng của số lượng tử quay là $l = 0$. Quy tắc chọn lọc $\Delta l = \pm 1$ đòi hỏi giá trị ban đầu của $l$ phải là 1. Do đó, năng lượng quay của phân tử giảm đi, và năng lượng photon phát xạ bằng độ giảm năng lượng dao động cộng thêm phần năng lượng quay được giải phóng.

Từ Ví dụ 42.2, độ chênh lệch giữa hai mức quay $l = 0$ và $l = 1$ là:

$$
\Delta E_{\mathrm{rot}} = 0{,}479\,\mathrm{meV}
$$

tương đương $0{,}000479\,\mathrm{eV}$.

Độ chênh lệch giữa hai mức năng lượng dao động lân cận của phân tử $\mathrm{CO}$ đo được từ thực nghiệm là:

$$
\hbar \omega = 0{,}2690\,\mathrm{eV}
$$

Ta sử dụng hệ thức $\lambda = hc / E$ để xác định bước sóng tương ứng của photon phát xạ.

**Thực hiện**:
(a) Phân tử $\mathrm{CO}$ mất đi một lượng năng lượng dao động bằng $0{,}2690\,\mathrm{eV}$ và nhận thêm một lượng năng lượng quay bằng $0{,}000479\,\mathrm{eV}$. Năng lượng chuyển hóa thành photon phát xạ là:

$$
E = 0{,}2685\,\mathrm{eV}
$$

Bước sóng của photon phát xạ tương ứng là:

$$
\begin{aligned}
\lambda &= \frac{hc}{E} \\
&= 4{,}618 \times 10^{-6}\,\mathrm m \\
&= 4{,}618\,\mu\mathrm m
\end{aligned}
$$

(b) Phân tử $\mathrm{CO}$ mất đi năng lượng dao động $0{,}2690\,\mathrm{eV}$ và đồng thời giải phóng thêm năng lượng quay $0{,}000479\,\mathrm{eV}$. Năng lượng chuyển hóa thành photon phát xạ là:

$$
E = 0{,}2695\,\mathrm{eV}
$$

Bước sóng của photon phát xạ tương ứng là:

$$
\begin{aligned}
\lambda &= \frac{hc}{E} \\
&= 4{,}601 \times 10^{-6}\,\mathrm m \\
&= 4{,}601\,\mu\mathrm m
\end{aligned}
$$

**Đánh giá**: Ở phần (b), phân tử mất nhiều năng lượng hơn so với phần (a), nên photon phát ra mang năng lượng lớn hơn và có bước sóng ngắn hơn ($4{,}601\,\mu\mathrm m < 4{,}618\,\mu\mathrm m$). Kết quả này hoàn toàn phù hợp với nguyên lý bảo toàn năng lượng.

::: tip Khái niệm cốt lõi: Chuyển dịch dao động - quay
Bên cạnh chuyển động quay quanh khối tâm (số lượng tử $l$), phân tử hai nguyên tử còn có chuyển động dao động của các hạt nhân (số lượng tử $n$). Khi chuyển mức dao động xảy ra đồng thời với chuyển dịch mức quay, năng lượng photon phát xạ hoặc hấp thụ phụ thuộc vào việc năng lượng quay tăng lên hay giảm đi theo quy tắc chọn lọc $\Delta l = \pm 1$.
:::

### Các kiểu dao động của phân tử CO2 và hiệu ứng nhà kính

Phân tử carbon dioxide có ba kiểu dao động được biểu diễn ở Hình 42.10. Các hạt nhân có thể uốn lệch khỏi trục hoặc dao động dọc theo trục theo kiểu đối xứng và bất đối xứng.

![Hình 42.10: Ba kiểu dao động chuẩn của phân tử carbon dioxide ($\mathrm{CO}_2$). (a) Dao động uốn (suy biến bậc 2): Nguyên tử carbon dịch chuyển lên trên trong khi hai nguyên tử oxy dịch chuyển xuống dưới, hoặc dao động tương tự vuông góc với mặt phẳng hình vẽ. (b) Dao động dãn đối xứng: Nguyên tử carbon đứng yên, hai nguyên tử oxy chuyển động ra xa và lại gần nhau đối xứng. (c) Dao động dãn bất đối xứng: Nguyên tử carbon dịch chuyển sang phải trong khi hai nguyên tử oxy dịch chuyển sang trái.](../img/young-42/hinh-42-10.png)

1. Dao động uốn: Nguyên tử carbon dịch chuyển vuông góc với trục phân tử theo một chiều, còn hai nguyên tử oxy dịch chuyển theo chiều ngược lại.
2. Dao động dãn đối xứng: Carbon đứng yên, còn hai nguyên tử oxy dịch chuyển theo hai chiều ngược nhau dọc theo trục.
3. Dao động dãn bất đối xứng: Carbon dịch chuyển dọc trục theo một chiều, còn hai nguyên tử oxy dịch chuyển theo chiều ngược lại.

Có thể có các chuyển mức giữa những mức kích thích của cùng một kiểu dao động hoặc giữa các kiểu dao động. Các hiệu năng lượng đang xét nhỏ hơn $1\,\mathrm{eV}$, nên liên quan đến photon hồng ngoại có bước sóng lớn hơn $1\,\mu\mathrm m$.

Khí carbon dioxide vì thế hấp thụ bức xạ ở nhiều bước sóng hồng ngoại. Nó góp phần vào hiệu ứng nhà kính trên Trái Đất dù chỉ chiếm khoảng $0{,}04\%$ thể tích khí quyển trong các số liệu đang xét.

Khí quyển Sao Kim có khối lượng hơn 90 lần khí quyển Trái Đất và gần như toàn khí carbon dioxide. Hiệu ứng nhà kính làm nhiệt độ bề mặt cao hơn hơn $400\,\mathrm K$ so với trường hợp hành tinh không có khí quyển. Ảnh mở đầu chương minh họa hành tinh này, không phải bản đồ hấp thụ hồng ngoại.

### Câu tự kiểm tra 42.2

Một phân tử hai nguyên tử đang quay phát xạ một photon khi thực hiện chuyển mức từ trạng thái $(n, l)$ xuống trạng thái $(n - 1, l - 1)$. Nếu giá trị của $l$ tăng lên trong khi $n$ không đổi, thì bước sóng của photon phát xạ sẽ:

(i) Tăng lên;
(ii) Giảm đi;
(iii) Không đổi?

::: details Giải thích và đáp án
**Đáp án lựa chọn**: (ii) Giảm đi.

**Lời giải chi tiết**: Giản đồ năng lượng ở Hình 42.5 và phương trình (42.6) chỉ ra rằng độ chênh lệch năng lượng giữa hai mức quay liên tiếp $\Delta E_{\mathrm{rot}}=E_l - E_{l-1}$, tức $l\hbar^2 / I$ tăng tuyến tính theo số lượng tử quay $l$.

Trong chuyển dịch từ trạng thái $(n, l)$ xuống $(n - 1, l - 1)$, phân tử vừa giảm một mức dao động (giải phóng năng lượng dao động $\hbar \omega$) vừa giảm một mức quay (giải phóng thêm năng lượng quay $\Delta E_{\mathrm{rot}} = l\hbar^2 / I$). Tổng năng lượng mà phân tử giải phóng chuyển hóa trọn vẹn thành năng lượng photon phát xạ:

$$
E_{\mathrm{photon}} = \hbar \omega + l\frac{\hbar^2}{I}
$$

Khi giá trị của $l$ tăng lên trong khi $n$ không đổi, lượng năng lượng quay được giải phóng $l\hbar^2 / I$ sẽ lớn hơn. Do đó, năng lượng $E_{\mathrm{photon}}$ của photon phát xạ tăng lên. Vì bước sóng của photon tỷ lệ nghịch với năng lượng ($\lambda = hc / E_{\mathrm{photon}}$), nên năng lượng photon lớn hơn đồng nghĩa với việc bước sóng của photon phát xạ sẽ ngắn hơn (tức bước sóng giảm đi).
:::
