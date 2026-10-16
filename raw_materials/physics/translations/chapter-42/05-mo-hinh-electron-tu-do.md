## 42.5 Mô hình electron tự do của kim loại

Trong các chất dẫn điện là kim loại, liên kết kim loại giải phóng các electron hóa trị khỏi từng nguyên tử riêng lẻ. Các ion dương dao động quanh các nút mạng tinh thể cố định, trong khi các electron hóa trị chuyển động hỗn loạn trong toàn bộ thể tích của khối kim loại tương tự như các phân tử của một chất khí. Mô hình đơn giản nhưng mang lại nhiều kết quả thực nghiệm chuẩn xác này được gọi là mô hình electron tự do của kim loại.

### Hộp thế ba chiều và các mức năng lượng gián đoạn

Để xây dựng mô hình định lượng, ta đưa ra hai giả thiết căn bản:
- Thế năng tương tác tuần hoàn giữa electron với các ion dương bên trong lòng khối kim loại được xấp xỉ bằng một giá trị không đổi. Ta chọn mốc thế năng này bằng 0.
- Ở bề mặt kim loại, lực hút tĩnh điện của khối ion kéo electron trở lại, tạo thành một rào thế năng rất cao ngăn không cho electron thoát ra ngoài.

Khối kim loại thể tích $V$ được mô hình hóa bằng một giếng thế sâu vô hạn hình hộp lập phương có cạnh $L$, thể tích $V = L^3$:

![Hình 42.20: Hộp thế thế năng ba chiều lập phương cạnh L giam giữ các electron tự do bên trong khối kim loại.](../img/young-42/hinh-42-20.png)

Hàm sóng dừng của một electron chuyển động trong hộp thế ba chiều phải triệt tiêu tại các mặt biên. Nghiệm của phương trình Schrödinger cho bài toán này dẫn đến các mức năng lượng gián đoạn được xác định bởi bộ ba số lượng tử nguyên dương $(n_X, n_Y, n_Z)$:

$$
E = \frac{(n_X^2 + n_Y^2 + n_Z^2)h^2}{8mL^2}
\tag{42.10}
$$

Trong đó $m$ là khối lượng nghỉ của electron, $h$ là hằng số Planck, và các số lượng tử chỉ nhận các giá trị nguyên dương: $n_X, n_Y, n_Z = 1, 2, 3, \dots$. Nếu đưa vào hằng số Dirac $\hbar = h / (2\pi)$, biểu thức tương đương là $E = (n_X^2 + n_Y^2 + n_Z^2)\frac{\pi^2 \hbar^2}{2mL^2}$.

### Mật độ trạng thái lượng tử

Để tính số trạng thái lượng tử $dn$ có năng lượng nằm trong một khoảng hẹp $dE$, trước hết ta khảo sát một không gian ba chiều với các trục tọa độ $(n_X, n_Y, n_Z)$:

![Hình 42.21: Các giá trị cho phép của ba số lượng tử nX, nY và nZ là các số nguyên dương trong góc phần tám thứ nhất của không gian n. Tính cả hai trạng thái spin của electron, mỗi đơn vị thể tích trong không gian n chứa hai trạng thái lượng tử.](../img/young-42/hinh-42-21.png)

Bán kính $n_{\mathrm{rs}}$ của một mặt cầu có tâm tại gốc tọa độ trong không gian này là $n_{\mathrm{rs}} = (n_X^2 + n_Y^2 + n_Z^2)^{1/2}$. Mỗi điểm có tọa độ nguyên trong không gian biểu diễn một trạng thái lượng tử không gian và chiếm một đơn vị thể tích. Tổng số điểm có tọa độ nguyên bên trong một hình cầu bán kính $n_{\mathrm{rs}}$ bằng thể tích của hình cầu đó, tức là $\frac{4}{3}\pi n_{\mathrm{rs}}^3$.

Vì các số lượng tử $n_X, n_Y, n_Z$ đều nguyên dương, ta chỉ lấy một góc phần tám của hình cầu với thể tích bằng $\frac{1}{8}\left(\frac{4}{3}\pi n_{\mathrm{rs}}^3\right) = \frac{1}{6}\pi n_{\mathrm{rs}}^3$. Do electron có spin ($m_s = \pm 1/2$), mỗi điểm không gian tương ứng với hai trạng thái lượng tử có spin ngược nhau. Vì vậy, tổng số trạng thái electron $n$ nằm bên trong góc phần tám bán kính $n_{\mathrm{rs}}$ gấp đôi $\frac{1}{6}\pi n_{\mathrm{rs}}^3$:

$$
n = \frac{\pi n_{\mathrm{rs}}^3}{3}
\tag{42.11}
$$

Năng lượng $E$ của các trạng thái nằm trên mặt cầu bán kính $n_{\mathrm{rs}}$ được biểu diễn qua phương trình (42.10) thành:

$$
E = \frac{n_{\mathrm{rs}}^2 \pi^2 \hbar^2}{2mL^2}
\tag{42.12}
$$

Kết hợp phương trình (42.11) và (42.12) để triệt tiêu bán kính $n_{\mathrm{rs}}$, ta thu được mối liên hệ giữa năng lượng $E$ và tổng số trạng thái $n$. Với thể tích khối kim loại là $V = L^3$, tổng số trạng thái lượng tử có năng lượng nhỏ hơn hoặc bằng $E$ là:

$$
n = \frac{(2m)^{3/2} V E^{3/2}}{3\pi^2 \hbar^3}
\tag{42.13}
$$

Để tìm số trạng thái $dn$ trong dải năng lượng từ $E$ đến $E + dE$, ta xem $n$ và $E$ là các biến số liên tục rồi lấy vi phân hai vế của phương trình (42.13):

$$
dn = \frac{(2m)^{3/2} V E^{1/2}}{2\pi^2 \hbar^3}\,dE
\tag{42.14}
$$

Mật độ trạng thái $g(E)$, định nghĩa là số trạng thái lượng tử trên một đơn vị dải năng lượng ($g(E) = dn / dE$), nhận biểu thức:

$$
g(E) = \frac{(2m)^{3/2} V}{2\pi^2 \hbar^3} E^{1/2}
\tag{42.15}
$$

Nếu biểu diễn theo hằng số Planck $h$, mật độ trạng thái nhận dạng tương đương $g(E) = \frac{8\sqrt{2}\pi m^{3/2} V}{h^3} E^{1/2}$. Do số trạng thái trong một thể tích vĩ mô lớn, các mức năng lượng nằm sát nhau đến mức ta hoàn toàn có thể xem $n$ và $E$ là các biến số liên tục.

### Phân bố Fermi–Dirac

Để xác định các electron phân bố vào các trạng thái lượng tử như thế nào ở nhiệt độ $T$, ta không thể áp dụng phân bố cổ điển Maxwell–Boltzmann vì hai nguyên nhân căn bản:
- Nguyên lý loại trừ Pauli: Electron là fermion (hạt có spin bán nguyên), mỗi trạng thái lượng tử chỉ được phép chứa tối đa một electron. Ở độ không tuyệt đối ($T = 0\,\mathrm{K}$), các electron không thể đồng loạt rơi về mức cơ bản đáy mà phải lấp đầy tuần tự từ mức thấp nhất cho đến một mức năng lượng trần nào đó gọi là mức Fermi.
- Tính không thể phân biệt: Các electron đồng nhất hoàn toàn và không thể đánh dấu riêng lẻ để phân biệt trạng thái hoán vị.

Sự kết hợp giữa nguyên lý loại trừ Pauli và tính chất không thể phân biệt dẫn tới phân bố thống kê lượng tử Fermi–Dirac. Hàm phân bố Fermi–Dirac cho biết xác suất $f(E)$ để một trạng thái lượng tử có năng lượng $E$ bị chiếm giữ bởi một electron ở nhiệt độ tuyệt đối $T$:

$$
f(E) = \frac{1}{e^{(E - E_F)/kT} + 1}
\tag{42.16}
$$

Trong đó $k$ là hằng số Boltzmann, $T$ là nhiệt độ Kelvin, và $E_F$ là mức năng lượng Fermi. Ở độ không tuyệt đối ($T = 0\,\mathrm{K}$), giá trị mức Fermi được ký hiệu là $E_{F0}$. Khi $T = 0\,\mathrm{K}$:
- Với mọi trạng thái có $E < E_{F0}$, số mũ $(E - E_{F0})/kT \to -\infty$, do đó $e^{-\infty} = 0$ và xác suất chiếm giữ là $f(E) = 1$.
- Với mọi trạng thái có $E > E_{F0}$, số mũ $(E - E_{F0})/kT \to +\infty$, do đó $e^{+\infty} = \infty$ và xác suất chiếm giữ là $f(E) = 0$.

![Hình 42.22: Hàm phân bố xác suất chiếm giữ các trạng thái năng lượng của electron tự do ở độ không tuyệt đối, biểu diễn dưới dạng hàm bước nhảy với giá trị bằng 1 khi năng lượng nhỏ hơn mức Fermi và bằng 0 khi năng lượng lớn hơn mức Fermi.](../img/young-42/hinh-42-22.png)

Khi nhiệt độ tăng lên ($T > 0\,\mathrm{K}$), kích thích nhiệt làm một số electron ở gần sát dưới mức Fermi nhảy lên các trạng thái trống ngay phía trên mức Fermi. Tại đúng giá trị $E = E_F$, số mũ bằng 0 ở mọi nhiệt độ, kéo theo:

$$
f(E_F) = \frac{1}{e^0 + 1} = \frac{1}{2}
$$

Như vậy, mức Fermi $E_F$ chính là mức năng lượng mà tại đó xác suất chiếm giữ của electron luôn đúng bằng $1/2$ ở bất kỳ nhiệt độ nào. Với các chất dẫn điện kim loại, mức Fermi thay đổi rất ít theo nhiệt độ, nên ta có thể lấy xấp xỉ $E_F \approx E_{F0}$.

![Hình 42.23: Đồ thị hàm phân bố Fermi–Dirac tại các giá trị nhiệt độ kT khác nhau khi mức Fermi EF gần như không đổi theo nhiệt độ.](../img/young-42/hinh-42-23.png)

### Nồng độ electron và năng lượng Fermi ở độ không tuyệt đối

Phương trình (42.16) cho biết xác suất để một trạng thái cụ thể có năng lượng $E$ bị chiếm giữ ở nhiệt độ $T$. Để biết số lượng electron thực tế $dN$ nằm trong dải năng lượng $dE$, ta nhân xác suất này với số trạng thái $dn = g(E)\,dE$ trong dải đó. Do đó, số electron $dN$ có năng lượng trong khoảng $dE$ là:

$$
\begin{aligned}
dN &= g(E) f(E)\,dE \\
&= \frac{g(E)\,dE}{e^{(E - E_F)/kT} + 1}
\end{aligned}
\tag{42.17}
$$

Khi thay tường minh $g(E)$ từ phương trình (42.15), ta thu được dạng khai triển: $dN = \frac{(2m)^{3/2} V E^{1/2}}{2\pi^2 \hbar^3} \frac{dE}{e^{(E - E_F)/kT} + 1}$.

Năng lượng Fermi $E_F$ được quyết định bởi tổng số electron $N$. Ở nhiệt độ bất kỳ, tích phân của mật độ trạng thái nhân xác suất chiếm phải cho đúng tổng số electron $N$. Sự điền đầy theo một ngưỡng sắc nét chỉ đúng ở giới hạn không độ tuyệt đối. Ở độ không tuyệt đối, mối liên hệ giữa $E_{F0}$ và $N$ rất đơn giản: Mọi trạng thái nằm dưới $E_{F0}$ đều bị chiếm đầy ($f(E) = 1$) và mọi trạng thái trên $E_{F0}$ đều hoàn toàn trống ($f(E) = 0$). Trong phương trình (42.13), ta gán $n$ bằng tổng số electron $N$ và $E$ bằng năng lượng Fermi ở độ không tuyệt đối $E_{F0}$:

$$
N = \frac{(2m)^{3/2} V E_{F0}^{3/2}}{3\pi^2 \hbar^3}
\tag{42.18}
$$

Biểu thức này cũng chính là kết quả của tích phân $N = \int_0^{E_{F0}} g(E)\,dE$. Nếu tính theo hằng số Planck $h$, tích phân cho hệ số đầy đủ $N = \frac{16\sqrt{2}\pi m^{3/2} V}{3h^3} E_{F0}^{3/2}$, trong đó thừa số $16\sqrt{2}$ xuất hiện từ việc nhân hệ số $2/3$ của tích phân $\int_0^{E_{F0}} E^{1/2}\,dE$ với hệ số $8\sqrt{2}$ của mật độ trạng thái $g(E)$.

Giải phương trình (42.18) theo $E_{F0}$, ta tìm được:

$$
E_{F0} = \frac{3^{2/3}\pi^{4/3}\hbar^2}{2m} \left(\frac{N}{V}\right)^{2/3}
\tag{42.19}
$$

Đại lượng $N/V$ biểu diễn số lượng electron tự do trên một đơn vị thể tích, gọi là nồng độ electron và thường được ký hiệu là $n$. Thay $N/V$ bằng $n$, phương trình (42.19) trở thành:

$$
E_{F0} = \frac{3^{2/3}\pi^{4/3}\hbar^2 n^{2/3}}{2m}
\tag{42.20}
$$

Nếu viết theo hằng số $h$, biểu thức này tương đương với $E_{F0} = \frac{h^2}{8m}\left(\frac{3n}{\pi}\right)^{2/3}$.

::: warning Lưu ý quan trọng về ký hiệu
Tuyệt đối không nhầm lẫn nồng độ electron tự do $n = N/V$ (có đơn vị là $\mathrm{m}^{-3}$) với số lượng tử $n$ trong phương trình sóng, và cũng không nhầm lẫn tổng số hạt electron $N$ với tổng số trạng thái lượng tử.
:::

---

### Ví dụ 42.6: Xác suất chiếm giữ trong mô hình electron tự do

**Bài toán**: Đối với các electron tự do trong chất rắn ở nhiệt độ tuyệt đối $T$, hãy tìm mức năng lượng mà tại đó xác suất chiếm giữ trạng thái tương ứng nhận giá trị:
- (a) $f(E) = 0{,}01$ (tức là $1\%$).
- (b) $f(E) = 0{,}99$ (tức là $99\%$).

**Phân tích và thiết lập**: Bài toán yêu cầu khảo sát hàm phân bố Fermi–Dirac. Công thức (42.16) cho biết xác suất $f(E)$ theo năng lượng $E$. Ta biến đổi đại số để biểu diễn độ chênh lệch năng lượng $E - E_F$ theo hàm số của xác suất $f(E)$:

$$
\frac{1}{f(E)} - 1 = e^{(E - E_F)/kT}
$$

Lấy logarit tự nhiên hai vế, ta tìm được hiệu năng lượng giữa trạng thái và mức Fermi:

$$
\frac{E - E_F}{kT} = \ln\left(\frac{1}{f(E)} - 1\right)
$$

hay biểu diễn tường minh theo $E$: $E = E_F + kT \ln [1/f(E) - 1]$. Ta cũng có thể quy đồng mẫu số bên trong logarit:

$$
\frac{E - E_F}{kT} = \ln\left(\frac{1 - f(E)}{f(E)}\right)
$$

**Các bước tính toán chi tiết**:
- Câu (a): Khi $f(E) = 0{,}01$, ta có $1/f(E) - 1 = 99$, do đó:

$$
\begin{aligned}
E - E_F &= kT \ln(99) \\
&\approx 4{,}595 kT \\
&\approx 4{,}6 kT
\end{aligned}
$$

hay $E \approx E_F + 4{,}6 kT$. Xác suất để một trạng thái lượng tử nằm phía trên mức Fermi một khoảng $4{,}6 kT$ bị chiếm giữ chỉ là $0{,}01$, tức $1\%$.

- Câu (b): Khi $f(E) = 0{,}99$, ta có $1/f(E) - 1 = 1/99$, do đó:

$$
\begin{aligned}
E - E_F &= -kT \ln(99) \\
&\approx -4{,}595 kT \\
&\approx -4{,}6 kT
\end{aligned}
$$

hay $E \approx E_F - 4{,}6 kT$. Xác suất để một trạng thái lượng tử nằm dưới mức Fermi một khoảng $4{,}6 kT$ bị chiếm giữ lên tới $0{,}99$, tức $99\%$.

**Đánh giá và nhận xét**: Kết quả thể hiện tính đối xứng chuẩn mực của phân bố Fermi–Dirac quanh mức Fermi. Với độ lệch năng lượng $\delta > 0$:

$$
\begin{aligned}
f(E_F - \delta) &= \frac{1}{e^{-\delta/kT} + 1} \\
&= \frac{e^{\delta/kT}}{e^{\delta/kT} + 1} \\
&= 1 - f(E_F + \delta)
\end{aligned}
$$

hay $f(E_F + \delta) + f(E_F - \delta) = 1$.

Nếu xác suất chiếm giữ một mức năng lượng cao hơn mức Fermi một khoảng $\delta$ là $P$, thì xác suất chiếm giữ mức năng lượng thấp hơn mức Fermi đúng một khoảng $\delta$ sẽ là $1 - P$. Ở nhiệt độ phòng ($kT \approx 0{,}025\,\mathrm{eV}$), khoảng chuyển tiếp $4{,}6 kT \approx 0{,}12\,\mathrm{eV}$ là rất hẹp so với mức Fermi vài electron-volt của kim loại, chứng minh bề mặt phân cách Fermi diễn ra rất đột ngột.

**Trực giác cốt lõi**: Phân bố Fermi–Dirac có tâm đối xứng tại điểm $(E_F, 1/2)$. Mọi trạng thái nằm cách mức Fermi quá vài lần $kT$ về phía dưới gần như chắc chắn bị chiếm giữ đầy, trong khi các trạng thái nằm cao hơn mức Fermi vài lần $kT$ gần như hoàn toàn bỏ trống.

---

### Ví dụ 42.7: Năng lượng Fermi và tốc độ electron trong đồng

**Bài toán**: Ở nhiệt độ thấp, đồng có nồng độ electron tự do $n = 8{,}45 \times 10^{28}\,\mathrm{m^{-3}}$. Sử dụng mô hình electron tự do, hãy tìm:
- (a) Năng lượng Fermi của đồng ở trạng thái rắn.
- (b) Tốc độ của một electron có động năng bằng năng lượng Fermi.

**Phân tích và thiết lập**: Bài toán sử dụng mối liên hệ giữa năng lượng Fermi và nồng độ electron tự do. Vì đồng là chất dẫn điện thể rắn, năng lượng Fermi của nó biến thiên rất ít theo nhiệt độ, nên ta có thể sử dụng biểu thức năng lượng Fermi ở độ không tuyệt đối theo phương trình (42.20). Ta áp dụng công thức phi tương đối tính $E_F = \frac{1}{2} m v_F^2$ để tìm tốc độ Fermi $v_F$ tương ứng với động năng $E_F$.

**Công thức và cơ sở áp dụng**:
- Năng lượng Fermi:

$$
E_{F0} = \frac{3^{2/3}\pi^{4/3}\hbar^2 n^{2/3}}{2m}
$$

- Tốc độ Fermi:

$$
v_F = \sqrt{\frac{2E_{F0}}{m}}
$$

**Các bước tính toán chi tiết**:
- Câu (a): Tính năng lượng Fermi $E_{F0}$ từ nồng độ hạt $n = 8{,}45 \times 10^{28}\,\mathrm{m^{-3}}$:

$$
\begin{aligned}
\frac{3n}{\pi} &= \frac{3(8{,}45 \times 10^{28})}{\pi}\,\mathrm{m^{-3}} \\
&\approx 8{,}069 \times 10^{28}\,\mathrm{m^{-3}}
\end{aligned}
$$

Lấy lũy thừa $2/3$, ta thu được $\left(\frac{3n}{\pi}\right)^{2/3} \approx 1{,}867 \times 10^{19}\,\mathrm{m^{-2}}$. Thay các hằng số vật lý $h = 6{,}626 \times 10^{-34}\,\mathrm{J\cdot s}$ và $m = 9{,}109 \times 10^{-31}\,\mathrm{kg}$:

$$
\begin{aligned}
E_{F0} &= \frac{h^2}{8m} \left(\frac{3n}{\pi}\right)^{2/3} \\
&\approx 1{,}126 \times 10^{-18}\,\mathrm{J}
\end{aligned}
$$

Đổi sang đơn vị electron-volt với $1\,\mathrm{eV} = 1{,}602 \times 10^{-19}\,\mathrm{J}$:

$$
\begin{aligned}
E_{F0} &= \frac{1{,}126 \times 10^{-18}\,\mathrm{J}}{1{,}602 \times 10^{-19}\,\mathrm{J/eV}} \\
&\approx 7{,}03\,\mathrm{eV}
\end{aligned}
$$

- Câu (b): Tính tốc độ Fermi $v_F$:

$$
\begin{aligned}
v_F &= \sqrt{\frac{2E_{F0}}{m}} \\
&\approx 1{,}57 \times 10^6\,\mathrm{m/s}
\end{aligned}
$$

**Đánh giá và nhận xét**:
- Các giá trị tính được của $E_{F0}$ và $v_F$ nằm hoàn toàn trong khoảng giá trị điển hình của các kim loại (lần lượt là $1{,}6$ đến $14\,\mathrm{eV}$ và $0{,}8$ đến $2{,}2 \times 10^6\,\mathrm{m/s}$).
- Tốc độ Fermi $v_F \approx 1{,}57 \times 10^6\,\mathrm{m/s}$ nhỏ hơn rất nhiều so với tốc độ ánh sáng trong chân không $c = 3{,}00 \times 10^8\,\mathrm{m/s}$ (chỉ chiếm khoảng $0{,}52\% c$), hoàn toàn biện minh cho việc sử dụng công thức động năng cổ điển phi tương đối tính $E_F = \frac{1}{2} m v_F^2$.
- Năng lượng Fermi $E_{F0}\approx7{,}03\,\mathrm{eV}$ lớn hơn nhiều so với $kT$ ở nhiệt độ phòng. Với $k=1{,}381\times10^{-23}\,\mathrm{J/K}$ và $T=293\,\mathrm K$, tích $kT$ nhận giá trị:

$$
\begin{aligned}
kT &= 4{,}05 \times 10^{-21}\,\mathrm{J} \\
&\approx 0{,}02525\,\mathrm{eV}
\end{aligned}
$$

(giá trị làm tròn trong một số tài liệu là $0{,}0254\,\mathrm{eV}$). Tỉ số $kT / E_{F0}\approx0{,}02525 / 7{,}03$, xấp xỉ $0{,}0036$, tức là năng lượng nhiệt chỉ chiếm chưa đầy $0{,}4\%$ mức Fermi. Vì vậy, ta hoàn toàn có thể lấy xấp xỉ xem gần như toàn bộ các trạng thái nằm dưới $E_{F0}$ bị điền đầy hoàn toàn và hầu hết các trạng thái nằm trên $E_{F0}$ hoàn toàn trống rỗng (xem Hình 42.22).
- Ta cũng có thể sử dụng phương trình (42.15) để tính mật độ trạng thái $g(E)$ khi biết trước $E$ và $V$. Với mức năng lượng $E = 7{,}03\,\mathrm{eV}$ và thể tích $V=1{,}00\,\mathrm{cm^3}$, tức $1{,}00 \times 10^{-6}\,\mathrm{m^3}$, mật độ trạng thái nhận giá trị xấp xỉ $2 \times 10^{22}\,\mathrm{states/eV}$ (tương đương $1{,}81 \times 10^{22}\,\mathrm{eV^{-1}}$ hay $1{,}13 \times 10^{41}\,\mathrm{J^{-1}}$):

$$
\begin{aligned}
g(E_{F0}) &= \frac{(2m)^{3/2} V}{2\pi^2 \hbar^3} E_{F0}^{1/2} \\
&\approx 1{,}81 \times 10^{22}\,\mathrm{eV^{-1}}
\end{aligned}
$$

Con số khổng lồ này khẳng định lý do tại sao ta hoàn toàn có cơ sở khi xem $n$ và $E$ là các biến số liên tục trong quá trình thiết lập biểu thức mật độ trạng thái.

**Khái niệm cốt lõi**: Năng lượng Fermi trong mô hình electron tự do của kim loại phụ thuộc vào nồng độ electron (số electron tự do trên một đơn vị thể tích). Trong một kim loại điển hình ở nhiệt độ phòng $T$, năng lượng Fermi lớn hơn rất nhiều so với $kT$.

---

### Năng lượng trung bình của electron tự do

Ta có thể tính năng lượng trung bình của electron tự do trong kim loại ở độ không tuyệt đối bằng cách tương tự như cách tìm $E_{F0}$. Từ phương trình (42.17), số electron $dN$ có năng lượng trong dải $dE$ là $g(E) f(E)\,dE$. Năng lượng của các electron này là $E\,dN = E g(E) f(E)\,dE$.

Ở độ không tuyệt đối, ta thay $f(E) = 1$ cho các mức năng lượng từ $E = 0$ đến $E = E_{F0}$ và $f(E) = 0$ cho mọi mức năng lượng khác. Do đó, năng lượng toàn phần $E_{\mathrm{tot}}$ của tất cả $N$ electron là:

$$
E_{\mathrm{tot}} = \int_0^{E_{F0}} E g(E)\,dE
$$

Cách đơn giản nhất để tính tích phân này là so sánh phương trình (42.15) với (42.19), dẫn đến hệ thức liên hệ trực tiếp:

$$
g(E) = \frac{3N E^{1/2}}{2E_{F0}^{3/2}}
$$

Thay biểu thức này vào tích phân và sử dụng công thức tính giá trị trung bình $E_{\mathrm{av}} = E_{\mathrm{tot}} / N$:

$$
E_{\mathrm{tot}} = \frac{3}{5} N E_{F0}
$$

Từ đó, động năng trung bình trên mỗi electron tự do ở độ không tuyệt đối bằng đúng ba phần năm năng lượng Fermi:

$$
E_{\mathrm{av}} = \frac{E_{\mathrm{tot}}}{N} = \frac{3}{5} E_{F0}
\tag{42.21}
$$

---

### Ví dụ 42.8: Khí electron tự do so với khí lý tưởng cổ điển

**Bài toán**:
- (a) Hãy tìm động năng trung bình của các electron tự do trong đồng ở độ không tuyệt đối bằng cách sử dụng kết quả của Ví dụ 42.7.
- (b) Nếu các electron này hành xử như một khối khí lý tưởng cổ điển ở nhiệt độ phòng $20^\circ\mathrm{C}$ ($293\,\mathrm{K}$), động năng tịnh tiến trung bình của mỗi electron và tốc độ tương ứng sẽ là bao nhiêu? So sánh các giá trị cổ điển này với giá trị lượng tử thực tế.

**Phân tích và thiết lập**:
- Đối với phần (a), ta áp dụng hệ thức lượng tử (42.21) với mức Fermi $E_{F0} = 7{,}03\,\mathrm{eV}$ của đồng.
- Đối với phần (b), mô hình động học phân tử cổ điển cho khí đơn nguyên tử xác định động năng tịnh tiến trung bình là $E_{\mathrm{av, cl}} = \frac{3}{2} kT$. Tốc độ tương ứng tính từ công thức động năng cổ điển $E_{\mathrm{av, cl}} = \frac{1}{2} m v^2$.

**Công thức và cơ sở áp dụng**:
- Năng lượng trung bình lượng tử ở $T = 0\,\mathrm{K}$:

$$
E_{\mathrm{av}} = \frac{3}{5} E_{F0}
$$

- Năng lượng trung bình cổ điển theo định luật phân bố đều:

$$
E_{\mathrm{av, cl}} = \frac{3}{2} kT
$$

- Tốc độ tương ứng:

$$
v = \sqrt{\frac{2E_{\mathrm{av, cl}}}{m}}
$$

**Các bước tính toán chi tiết**:
- Câu (a): Năng lượng trung bình của electron tự do trong đồng ở $T = 0\,\mathrm{K}$:

$$
\begin{aligned}
E_{\mathrm{av}} &= \frac{3}{5}(7{,}03\,\mathrm{eV}) \\
&\approx 4{,}22\,\mathrm{eV}
\end{aligned}
$$

hoặc đổi sang đơn vị joule: $E_{\mathrm{av}} \approx 6{,}76 \times 10^{-19}\,\mathrm{J}$.

- Câu (b): Nếu tuân theo khí lý tưởng cổ điển ở $T = 293\,\mathrm{K}$ ($kT \approx 0{,}02525\,\mathrm{eV}$):

$$
\begin{aligned}
E_{\mathrm{av, cl}} &= \frac{3}{2}(0{,}02525\,\mathrm{eV}) \\
&\approx 0{,}0379\,\mathrm{eV}
\end{aligned}
$$

hay đổi sang joule: $E_{\mathrm{av, cl}} \approx 6{,}07 \times 10^{-21}\,\mathrm{J}$. Tốc độ chuyển động nhiệt cổ điển của electron sẽ là:

$$
\begin{aligned}
v &= \sqrt{\frac{2E_{\mathrm{av, cl}}}{m}} \\
&\approx 1{,}15 \times 10^5\,\mathrm{m/s}
\end{aligned}
$$

So sánh tỉ số năng lượng và tỉ số tốc độ:

$$
\begin{aligned}
\frac{E_{\mathrm{av, cl}}}{E_{\mathrm{av}}} &= \frac{0{,}0379\,\mathrm{eV}}{4{,}22\,\mathrm{eV}} \\
&\approx 0{,}90\%
\end{aligned}
$$

$$
\begin{aligned}
\frac{v}{v_F} &= \frac{1{,}15 \times 10^5\,\mathrm{m/s}}{1{,}57 \times 10^6\,\mathrm{m/s}} \\
&\approx 7{,}3\%
\end{aligned}
$$

**Đánh giá và nhận xét**: Động năng dự đoán bởi mô hình cổ điển chỉ bằng khoảng $1\%$ giá trị lượng tử thực tế, và tốc độ cổ điển chỉ bằng khoảng $7\%$ tốc độ Fermi. Điều này cho thấy nhiệt độ môi trường đóng vai trò rất thứ yếu trong việc định hình động năng của electron trong kim loại. Năng lượng khổng lồ của các electron dẫn gần như hoàn toàn là hệ quả trực tiếp từ nguyên lý loại trừ Pauli.

**Trực giác cốt lõi**: Khí electron trong kim loại là một hệ lượng tử suy biến cao độ. Do nguyên lý loại trừ Pauli ngăn cản các electron chiếm cùng một trạng thái, các hạt bị cưỡng bức phải điền đầy các mức năng lượng cao ngay từ độ không tuyệt đối.

---

### Đóng góp của electron vào nhiệt dung của kim loại

Sự thất bại của vật lý cổ điển thể hiện rõ nét nhất ở bài toán nhiệt dung của kim loại. Theo nguyên lý phân bố đều năng lượng của nhiệt động lực học cổ điển, nếu mỗi nguyên tử kim loại đóng góp một electron tự do chuyển động tịnh tiến ba chiều, khối khí electron này sẽ đóng góp một lượng vào nhiệt dung mol đẳng tích:

$$
C_{V, \mathrm{cl}} = \frac{3}{2} R \approx 1{,}5 R
$$

Tuy nhiên, các phép đo thực nghiệm cho thấy nhiệt dung mol của kim loại ở nhiệt độ phòng hoàn toàn không tăng thêm $1{,}5 R$ so với chất cách điện, mà gần như tuân theo đúng quy tắc Dulong–Petit của dao động mạng ion ($C_V \approx 3R$).

Mô hình lượng tử Fermi–Dirac giải thích triệt để nghịch lý này:
- Để một electron có thể hấp thụ năng lượng nhiệt khi nhiệt độ tăng thêm $\Delta T$, nó bắt buộc phải nhảy lên một trạng thái lượng tử còn trống ở mức năng lượng cao hơn.
- Do $kT \ll E_F$, hầu như toàn bộ các trạng thái nằm sâu bên dưới mức Fermi đều đã bị lấp kín, các electron tại đó không thể tìm thấy trạng thái trống liền kề để chuyển dời.
- Chỉ có một phần rất nhỏ các electron nằm sát mặt Fermi trong phạm vi năng lượng cỡ $kT$ mới có thể hấp thụ nhiệt và thay đổi trạng thái. Phân số electron tham gia quá trình này tỉ lệ thuận với $kT / E_F$.

Do đó, nhiệt dung mol của khí electron tỷ lệ với $(kT / E_F)(3R/2)$. Phân tích lượng tử chính xác cho thấy đóng góp của electron vào nhiệt dung mol đẳng tích của kim loại là:

$$
C_{V, \mathrm{elec}} = \frac{\pi^2 kT}{2E_F} R
$$

Với mẩu đồng ở nhiệt độ phòng $T = 293\,\mathrm{K}$ có $E_F \approx 7{,}03\,\mathrm{eV}$ và $kT \approx 0{,}02525\,\mathrm{eV}$:

$$
\begin{aligned}
C_{V, \mathrm{elec}} &= \frac{\pi^2(0{,}02525\,\mathrm{eV})}{2(7{,}03\,\mathrm{eV})} R \\
&\approx 0{,}018 R
\end{aligned}
$$

Giá trị này chỉ chiếm khoảng $1{,}2\%$ so với dự đoán sai lầm $1{,}5 R$ của nhiệt động lực học cổ điển. Vì đóng góp của electron quá nhỏ bé, nhiệt dung của hầu hết các kim loại ở nhiệt độ thông thường chủ yếu xuất phát từ dao động nhiệt của các ion tại các nút mạng tinh thể.

---

### Kiểm tra mức độ hiểu mục 42.5

Một khối khí lý tưởng tuân theo phương trình trạng thái $pV = n_{\mathrm{mol}} R T$. Với thể tích $V$ và số mol $n_{\mathrm{mol}}$ không đổi, khi nhiệt độ tuyệt đối $T$ giảm, áp suất $p$ giảm tỉ lệ thuận và tiến về 0 khi $T$ tiến dần về độ không tuyệt đối. Khẳng định này có đúng đối với chất khí electron tự do trong kim loại rắn hay không?

::: details Xem đáp án và giải thích
**Đáp án**: Không (Khẳng định trên hoàn toàn không đúng với khí electron tự do).

**Giải thích chi tiết**: Theo thuyết động học phân tử, áp suất của chất khí tỉ lệ thuận với động năng tịnh tiến trung bình $E_{\mathrm{av}}$ của các hạt cấu thành nên khí. Trong một khối khí lý tưởng cổ điển, động năng trung bình $E_{\mathrm{av}} = \frac{3}{2} kT$ tỷ lệ thuận trực tiếp với nhiệt độ tuyệt đối $T$, do đó áp suất giảm dần về 0 khi nhiệt độ hạ về độ không tuyệt đối.

Ngược lại, đối với khí electron tự do trong kim loại, chuyển động của các hạt bị chi phối bởi nguyên lý loại trừ Pauli chứ không phải bởi chuyển động nhiệt thông thường. Như đã chứng minh ở phương trình (42.21) và Ví dụ 42.8, ở độ không tuyệt đối động năng trung bình của electron vẫn duy trì một giá trị rất lớn $E_{\mathrm{av}} = \frac{3}{5} E_{F0}$ (đạt tới $4{,}22\,\mathrm{eV}$ ở đồng). Khi nhiệt độ tăng từ $0\,\mathrm{K}$ lên nhiệt độ phòng ($293\,\mathrm{K}$), kích thích nhiệt chỉ làm thay đổi động năng trung bình chưa tới $1\%$. Vì vậy, áp suất suy biến của chất khí electron tự do trong lòng kim loại hầu như không thay đổi giữa nhiệt độ phòng và độ không tuyệt đối, và hoàn toàn không bao giờ tiến về 0 khi $T \to 0\,\mathrm{K}$.
:::
