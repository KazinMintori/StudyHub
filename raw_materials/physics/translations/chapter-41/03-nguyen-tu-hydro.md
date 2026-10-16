## 41.3. Nguyên tử hydro

Mô hình Bohr ở chương 39 cho các mức năng lượng hydro phù hợp với phổ thực nghiệm ở bậc gần đúng đã xét. Mô hình kết hợp quỹ đạo tròn Newton với điều kiện lượng tử hóa mômen động lượng, nhưng chưa giải thích được vì sao có điều kiện ấy.

Mô hình cũng không giải thích đầy đủ quá trình phát và hấp thụ photon, không mở rộng được trực tiếp sang nguyên tử nhiều electron và cho dự đoán sai về mômen từ quỹ đạo ở trạng thái cơ bản. Hình ảnh electron có vị trí và động lượng xác định trên quỹ đạo còn không phù hợp với nguyên lý bất định. Ta cần mô tả bằng hàm sóng.

Để vượt qua những hạn chế đó, chúng ta giải phương trình Schrödinger ba chiều để xác định các hàm sóng trạng thái dừng của nguyên tử hydro. Tương tự như ở Chương 39, chuyển động của hạt nhân được tính đến một cách chính xác bằng cách thay khối lượng electron $m$ bằng khối lượng rút gọn $m_r$ của hệ hai vật electron và hạt nhân:

$$
m_r = \frac{m m_{\mathrm{p}}}{m + m_{\mathrm{p}}}
$$

Trong đó $m_{\mathrm{p}}$ là khối lượng của proton.

### Phương trình Schrödinger cho nguyên tử hydro

Hàm thế năng tương tác tĩnh điện giữa electron mang điện tích $-e$ và proton mang điện tích $+e$ là thế năng Coulomb có tính đối xứng cầu, chỉ phụ thuộc vào khoảng cách $r = \sqrt{x^2 + y^2 + z^2}$ từ gốc tọa độ đặt tại hạt nhân:

$$
U(r) = -\frac{1}{4\pi\epsilon_0} \frac{e^2}{r} \tag{41.18}
$$

Vì thế năng chỉ phụ thuộc vào $r$, bài toán nguyên tử hydro được giải thuận tiện nhất trong hệ tọa độ cầu $(r, \theta, \phi)$ như mô tả trên Hình 41.05.

![Hình 41.05: Hệ tọa độ cầu $(r, \theta, \phi)$ dùng để thiết lập và giải phương trình Schrödinger cho nguyên tử hydro. Hạt nhân mang điện tích $+e$ đặt tại gốc tọa độ, electron mang điện tích $-e$ tại vị trí $(r, \theta, \phi)$.](../img/young-41/hinh-41-05.png)

Áp dụng phương pháp tách biến, hàm sóng không gian $\psi(r, \theta, \phi)$ được phân tách thành tích của ba hàm số độc lập:

$$
\psi(r, \theta, \phi) = R(r)\Theta(\theta)\Phi(\phi) \tag{41.19}
$$

Trong đó $R(r)$ là hàm sóng bán kính chỉ phụ thuộc biến khoảng cách $r$, $\Theta(\theta)$ chỉ phụ thuộc góc cực $\theta$, và $\Phi(\phi)$ chỉ phụ thuộc góc kinh độ (góc phương vị) $\phi$.

Khi thay biểu thức tích (41.19) vào phương trình Schrödinger trong tọa độ cầu, phương trình đạo hàm riêng phân rã thành ba phương trình vi phân thường độc lập. Đặt toán tử vi phân bán kính $\hat{\mathcal{L}}_r R = -\frac{\hbar^2}{2m_r r^2}\frac{d}{dr}\left(r^2 \frac{dR}{dr}\right)$, thế năng hiệu dụng $U_{\mathrm{eff}}(r) = \frac{\hbar^2 l(l+1)}{2m_r r^2} + U(r)$, toán tử góc $\hat{\mathcal{L}}_\theta\Theta = \frac{1}{\sin\theta}\frac{d}{d\theta}\left(\sin\theta \frac{d\Theta}{d\theta}\right)$, và $V_l(\theta) = l(l+1) - \frac{m_l^2}{\sin^2\theta}$:

$$
\hat{\mathcal{L}}_r R + U_{\mathrm{eff}}(r)R = ER \tag{41.20a}
$$

$$
\hat{\mathcal{L}}_\theta\Theta + V_l(\theta)\Theta = 0 \tag{41.20b}
$$

$$
\frac{d^2\Phi}{d\phi^2} + m_l^2\Phi = 0 \tag{41.20c}
$$

Trong hệ phương trình (41.20), $E$ là năng lượng của trạng thái dừng, $l$ và $m_l$ là các hằng số phân tách lượng tử.

::: warning Cảnh báo: Phân biệt ký hiệu khối lượng rút gọn và số lượng tử từ
Cần phân biệt rõ ký hiệu $m_l$ trong các phương trình (41.20b) và (41.20c) với ký hiệu $m_r$ chỉ khối lượng rút gọn của electron và hạt nhân. Ký hiệu $m_l$ là số lượng tử từ không thứ nguyên nhận các giá trị nguyên, trong khi $m_r$ là đại lượng vật lý có đơn vị khối lượng (kilôgam).
:::

Các nghiệm chấp nhận được về mặt vật lý của hệ phương trình (41.20) được xác định thông qua các điều kiện biên:

- Hàm bán kính $R(r)$ trong phương trình (41.20a) bắt buộc phải tiến tới $0$ khi khoảng cách $r \to \infty$, vì electron nằm trong trạng thái liên kết định xứ quanh hạt nhân.
- Các hàm góc $\Theta(\theta)$ và $\Phi(\phi)$ phải hữu hạn tại mọi góc trong miền xác định. Hàm $\Theta(\theta)$ không được tiến tới vô hạn tại $\theta = 0$ và $\theta = \pi$ để đảm bảo hàm sóng $\psi$ có thể chuẩn hóa được.
- Hàm kinh độ $\Phi(\phi)$ trong phương trình (41.20c) bắt buộc phải có tính tuần hoàn: Tọa độ $(r, \theta, \phi)$ và $(r, \theta, \phi + 2\pi)$ xác định cùng một điểm vật lý trong không gian, do đó $\Phi(\phi + 2\pi) = \Phi(\phi)$. Điều kiện tuần hoàn này dẫn đến nghiệm $\Phi(\phi) \propto e^{i m_l \phi}$, trong đó $m_l$ bắt buộc phải là một số nguyên (âm, dương hoặc bằng không).

Nghiệm hàm bán kính $R(r)$ thỏa mãn các điều kiện biên là tích của một đa thức theo $r$ với một hàm suy giảm mũ $e^{-\alpha r}$ (với $\alpha > 0$). Hàm $\Theta(\theta)$ là một đa thức chứa các lũy thừa của $\sin\theta$ và $\cos\theta$ (liên hệ với các đa thức Legendre liên kết).

### Lượng tử hóa mức năng lượng

Quá trình tìm kiếm các nghiệm giải tích thỏa mãn điều kiện biên cũng đồng thời xác định các mức năng lượng gián đoạn cho phép của hệ. Các mức năng lượng dừng $E_n$ của nguyên tử hydro là:

$$
\begin{aligned}
E_n &= -\frac{1}{(4\pi\epsilon_0)^2} \frac{m_r e^4}{2n^2\hbar^2} \\
&= -\frac{13{,}60\,\text{eV}}{n^2}
\end{aligned} \tag{41.21}
$$

với $n = 1, 2, 3, \dots$ là số lượng tử chính.

Phương trình (41.21) cho cùng hệ thức năng lượng với mô hình Bohr ở bậc gần đúng đang xét. Trong mô tả Schrödinger, sự lượng tử hóa xuất hiện từ nghiệm hàm sóng và điều kiện biên. Ta không cần đặt thêm điều kiện quỹ đạo tròn có mômen động lượng bằng bội nguyên của $\hbar$.

### Lượng tử hóa mômen động lượng quỹ đạo

Nghiệm của hệ phương trình vi phân (41.20) tự động dẫn đến sự lượng tử hóa của mômen động lượng quỹ đạo: Chỉ một số giá trị gián đoạn nhất định của độ lớn và thành phần của vector mômen động lượng $\vec{L}$ mới được phép tồn tại.

Độ lớn $L$ của vector mômen động lượng quỹ đạo $\vec{L}$ được xác định bởi điều kiện hàm $\Theta(\theta)$ hữu hạn tại hai cực $\theta = 0$ và $\theta = \pi$, với $l = 0, 1, 2, \dots, n-1$:

$$
L = \sqrt{l(l+1)}\hbar \tag{41.22}
$$

Trong đó $l$ là số lượng tử quỹ đạo. Ứng với mức năng lượng thứ $n$, có đúng $n$ giá trị khả dĩ của số lượng tử quỹ đạo $l$, chạy từ $0$ đến $n-1$.

Một kết quả lượng tử quan trọng từ phương trình (41.22) là khi $l = 0$, độ lớn mômen động lượng quỹ đạo bằng không: $L = 0$. Kết quả này hoàn toàn trái ngược với mô hình Bohr, nơi electron luôn quay tròn với $L \ge \hbar$. Các hàm sóng ứng với trạng thái $l = 0$ chỉ phụ thuộc biến bán kính $r$, các hàm góc $\Theta(\theta)$ và $\Phi(\phi)$ đều là hằng số. Vì vậy, các trạng thái $l = 0$ có hàm phân bố xác suất $|\psi|^2$ hoàn toàn đối xứng cầu. Không có bất kỳ hướng không gian nào được ưu tiên, và electron không có chuyển động quay có hướng quanh hạt nhân.

Hình chiếu của vector $\vec{L}$ lên một trục không gian xác định, theo quy ước là trục $z$, được xác định bởi điều kiện tuần hoàn $\Phi(\phi + 2\pi) = \Phi(\phi)$, với $m_l = 0, \pm 1, \pm 2, \dots, \pm l$:

$$
L_z = m_l \hbar \tag{41.23}
$$

Số lượng tử $m_l$ được gọi là số lượng tử từ quỹ đạo (hoặc số lượng tử từ). Ứng với một giá trị $l$, có $2l + 1$ giá trị nguyên khả dĩ của $m_l$, thỏa mãn $|m_l| \le l$.

Độ lớn hình chiếu $|L_z|$ luôn nhỏ hơn độ lớn toàn phần $L$ (trừ trường hợp cả hai cùng bằng không). Chẳng hạn, khi $l = 2$, giá trị cực đại của $m_l$ là $2$:

$$
\begin{aligned}
L &= \sqrt{2(2+1)}\hbar \\
&= \sqrt{6}\hbar \approx 2{,}45\hbar
\end{aligned}
$$

$$
(L_z)_{\max} = 2\hbar
$$

Góc cực tiểu $\theta_L$ giữa vector $\vec{L}$ và trục $z$ là:

$$
\begin{aligned}
\theta_L &= \arccos\frac{(L_z)_{\max}}{L} \\
&= \arccos\frac{2}{2{,}45} \approx 35{,}3^\circ
\end{aligned}
$$

![Hình 41.06: (a) Khi $l = 2$, độ lớn của vector mômen động lượng là $L = \sqrt{6}\hbar \approx 2{,}45\hbar$, nhưng vector $\vec{L}$ không có hướng xác định trong không gian. Khi thành phần $L_z$ đạt cực đại $2\hbar$, $\vec{L}$ tạo với trục $z$ một góc cực tiểu $35{,}3^\circ$. (b) Các hình nón biểu diễn tập hợp các hướng khả dĩ của $\vec{L}$ ứng với các giá trị khác nhau của $L_z$.](../img/young-41/hinh-41-06.png)

Với $l>0$, các giá trị cho phép thỏa $|L_z|<L$. Khi $l=0$, cả hai cùng bằng không. Ta có thể xác định đồng thời $L^2$ và một thành phần, chẳng hạn $L_z$. Ba thành phần không thể đồng thời có giá trị xác định nói chung vì các toán tử của chúng không giao hoán.

Hình nón ở Hình 41.06b giúp biểu diễn cùng độ lớn $L$ và cùng hình chiếu $L_z$. Nó không mô tả một vector cổ điển đang tiến động với ba thành phần đã xác định. Tương tự, orbital mô tả trạng thái bằng hàm sóng, không phải một quỹ đạo electron cố định.

### Quy ước ký hiệu trạng thái và lớp vỏ điện tử

Khi chưa xét spin và từ trường, các trạng thái riêng đang dùng được gắn nhãn bằng $(n,l,m_l)$. Nghiệm thế Coulomb cho năng lượng chỉ phụ thuộc $n$. Vì vậy, các trạng thái cùng $n$ có thể suy biến. Riêng mức $n=1$ chỉ có một trạng thái không gian.

Đối xứng cầu bảo đảm các trạng thái khác $m_l$ trong cùng một bộ $(n,l)$ có cùng năng lượng. Việc các giá trị $l$ khác nhau cũng cho cùng năng lượng là tính chất thêm của thế Coulomb. Nó không đúng với mọi thế có đối xứng cầu.

![Hình 41.07: Trong mô hình hấp dẫn Newton, năng lượng của vệ tinh quanh Trái Đất chỉ phụ thuộc bán trục lớn của quỹ đạo. Các quỹ đạo có cùng bán trục lớn có thể có độ lệch tâm và mômen động lượng khác nhau. Năng lượng Coulomb lượng tử cũng có thể bằng nhau cho những trạng thái khác mômen động lượng.](../img/young-41/hinh-41-07.png)

Trong quang phổ học, các trạng thái ứng với các giá trị khác nhau của số lượng tử quỹ đạo $l$ được ký hiệu bằng các chữ cái:

- $l = 0$: Trạng thái $s$
- $l = 1$: Trạng thái $p$
- $l = 2$: Trạng thái $d$
- $l = 3$: Trạng thái $f$
- $l = 4$: Trạng thái $g$
- $l = 5$: Trạng thái $h$

Các chữ cái này bắt nguồn từ những từ mô tả đặc điểm vạch quang phổ (sharp, principal, diffuse, fundamental). Trạng thái có $n=2,l=1$ được gọi là $2p$, còn trạng thái có $n=4,l=0$ được gọi là $4s$. Các trạng thái $s$ ($l=0$) có hàm sóng không phụ thuộc góc.

Các giá trị của số lượng tử chính $n$ xác định các lớp vỏ electron (shells), được ký hiệu bằng các chữ cái viết hoa:

- $n = 1$: Lớp vỏ $K$
- $n = 2$: Lớp vỏ $L$
- $n = 3$: Lớp vỏ $M$
- $n = 4$: Lớp vỏ $N$

Trong mỗi lớp vỏ $n$, các giá trị khác nhau của $l$ hình thành nên các phân lớp (subshells). Ví dụ: Lớp vỏ $L$ ($n = 2$) gồm hai phân lớp $2s$ và $2p$.

Bảng 41.1 liệt kê các trạng thái lượng tử của nguyên tử hydro ứng với các mức năng lượng đầu tiên:

- Trạng thái $1s$ thuộc vỏ K, với $n=1$, $\ell=0$ và $m_\ell=0$.
- Trạng thái $2s$ thuộc vỏ L, với $n=2$, $\ell=0$ và $m_\ell=0$.
- Trạng thái $2p$ thuộc vỏ L, với $n=2$, $\ell=1$ và $m_\ell=0,\pm1$.
- Trạng thái $3s$ thuộc vỏ M, với $n=3$, $\ell=0$ và $m_\ell=0$.
- Trạng thái $3p$ thuộc vỏ M, với $n=3$, $\ell=1$ và $m_\ell=0,\pm1$.
- Trạng thái $3d$ thuộc vỏ M, với $n=3$, $\ell=2$ và $m_\ell=0,\pm1,\pm2$.
- Trạng thái $4s$ thuộc vỏ N, với $n=4$, $\ell=0$ và $m_\ell=0$.

### Cách tổ chức bài toán cấu trúc nguyên tử

Trước hết, xác định bài toán hỏi năng lượng, độ lớn mômen động lượng, hình chiếu hay số trạng thái. Các đại lượng này gắn với những số lượng tử khác nhau. Chọn các phương trình (41.21), (41.22) và (41.23) theo đúng đại lượng cần tìm.

Tiếp đó, ghi miền các số lượng tử. $n$ là số nguyên dương, $\ell$ nhận các số nguyên từ 0 đến $n-1$, còn $m_\ell$ chạy từ $-\ell$ đến $\ell$. Từ các miền này, hãy dựng lại các trạng thái trong một vỏ hay phân lớp, thay vì chỉ nhớ bảng.

Sau khi giải, kiểm tra dấu, đơn vị và bậc độ lớn. Ở khoảng cách $0{,}10\,\mathrm{nm}$, thế năng điện của một proton và một electron xấp xỉ $-14{,}4\,\mathrm{eV}$, tức cỡ $-15\,\mathrm{eV}$. Ánh sáng có bước sóng $500\,\mathrm{nm}$ có tần số khoảng $6\times10^{14}\,\mathrm{Hz}$. Những thang này giúp nhận ra kết quả sai nhiều bậc mười.

### Ví dụ 41.2: Đếm số trạng thái lượng tử của nguyên tử hydro

Có bao nhiêu trạng thái lượng tử phân biệt $(n, l, m_l)$ của nguyên tử hydro ứng với số lượng tử chính $n = 3$? Mức năng lượng của các trạng thái này bằng bao nhiêu?

#### Phương pháp giải

Vận dụng quy tắc giới hạn của các số lượng tử: Với một giá trị $n$ xác định, số lượng tử quỹ đạo $l$ nhận $n$ giá trị nguyên từ $0$ đến $n-1$. Với mỗi giá trị $l$, số lượng tử từ $m_l$ nhận $2l + 1$ giá trị nguyên từ $-l$ đến $+l$. Năng lượng của trạng thái được xác định bằng phương trình (41.21).

#### Lời giải chi tiết

Với $n = 3$, số lượng tử quỹ đạo $l$ có thể nhận các giá trị $0$, $1$, hoặc $2$:

- Khi $l = 0$: Số lượng tử $m_l$ chỉ có duy nhất một giá trị $m_l = 0$ (1 trạng thái, phân lớp $3s$).
- Khi $l = 1$: Số lượng tử $m_l$ nhận ba giá trị $-1, 0, 1$ (3 trạng thái, phân lớp $3p$).
- Khi $l = 2$: Số lượng tử $m_l$ nhận năm giá trị $-2, -1, 0, 1, 2$ (5 trạng thái, phân lớp $3d$).

Tổng số trạng thái lượng tử không gian ứng với $n = 3$ là:

$$
1 + 3 + 5 = 9 \text{ trạng thái}
$$

Năng lượng của nguyên tử hydro chỉ phụ thuộc vào $n$, do đó toàn bộ 9 trạng thái này đều có cùng mức năng lượng:

$$
\begin{aligned}
E_3 &= -\frac{13{,}60\,\text{eV}}{3^2} \\
&= -\frac{13{,}60\,\text{eV}}{9} \\
&\approx -1{,}51\,\text{eV}
\end{aligned}
$$

#### Đánh giá kết quả

Tổng số trạng thái không gian $(n, l, m_l)$ ứng với một số lượng tử chính $n$ bất kỳ luôn bằng $n^2$. Với $n = 3$, số trạng thái là $3^2 = 9$. Khi tính thêm bậc tự do spin của electron ở các mục tiếp theo, mỗi trạng thái không gian chứa được 2 trạng thái spin, nâng tổng số trạng thái của lớp $n = 3$ lên thành $2n^2 = 18$ trạng thái.

### Ví dụ 41.3: Mômen động lượng ở mức kích thích của nguyên tử hydro

Xét các trạng thái lượng tử của nguyên tử hydro ở mức $n = 4$.

(a) Xác định độ lớn cực đại $L_{\max}$ của vector mômen động lượng quỹ đạo.

(b) Xác định giá trị cực đại của thành phần $(L_z)_{\max}$.

(c) Tính góc cực tiểu giữa vector mômen động lượng $\vec{L}$ và trục $z$.

Biểu diễn kết quả câu (a) và (b) theo hằng số $\hbar$.

#### Phương pháp giải

Với $n = 4$, giá trị cực đại của số lượng tử quỹ đạo là $l_{\max} = n - 1$. Độ lớn $L$ được tính theo phương trình (41.22), và thành phần $L_z$ tính theo phương trình (41.23). Góc giữa $\vec{L}$ và trục $z$ đạt cực tiểu khi $L_z$ đạt giá trị lớn nhất.

#### Lời giải chi tiết

(a) Khi $n = 4$, giá trị cực đại của số lượng tử quỹ đạo là:

$$
l_{\max} = n - 1 = 4 - 1 = 3
$$

Độ lớn cực đại của mômen động lượng quỹ đạo là:

$$
\begin{aligned}
L_{\max} &= \sqrt{3(3+1)}\hbar \\
&= \sqrt{12}\hbar \approx 3{,}464\hbar
\end{aligned}
$$

(b) Ứng với $l = 3$, giá trị cực đại của số lượng tử từ là $m_l = 3$. Giá trị cực đại của thành phần $L_z$ là:

$$
(L_z)_{\max} = 3\hbar
$$

(c) Góc cực tiểu giữa $\vec{L}$ và trục $z$ ứng với trạng thái có $l = 3$ và $m_l = 3$:

$$
\begin{aligned}
\theta_{\min} &= \arccos\frac{(L_z)_{\max}}{L_{\max}} \\
&= \arccos\frac{\sqrt{3}}{2} = 30{,}0^\circ
\end{aligned}
$$

#### Đánh giá kết quả

Với $l=1$ hoặc $l=2$, góc nhỏ nhất trong mô hình vector lớn hơn $30{,}0^\circ$. Với $l=3$, góc nhỏ nhất bằng $30{,}0^\circ$, đạt khi $m_l=3$. Trường hợp $l=0$ có $L=0$, nên không xác định một góc giữa vector không và trục $z$.

### Phân bố xác suất của electron và hàm phân bố bán kính

Thay cho hình ảnh electron chuyển động trên một quỹ đạo tròn xác định, cơ học lượng tử mô tả electron thông qua đám mây mật độ xác suất trong không gian ba chiều bao quanh hạt nhân. Để khảo sát xác suất xuất hiện của electron theo khoảng cách từ hạt nhân, chúng ta định nghĩa hàm phân bố xác suất bán kính $P(r)$.

Cần phân biệt rõ ba khái niệm có ý nghĩa vật lý và thứ nguyên hoàn toàn khác nhau:
1. Mật độ xác suất thể tích $|\psi(\vec{r})|^2$ (thứ nguyên $1/\text{m}^3$): Xác suất tìm thấy electron trên một đơn vị thể tích tại một điểm cụ thể có tọa độ $\vec{r} = (x, y, z)$ hay $(r, \theta, \phi)$ trong không gian.
2. Hàm phân bố xác suất bán kính $P(r)$ (thứ nguyên $1/\text{m}$): Mật độ xác suất tìm thấy electron theo khoảng cách hướng tâm $r$, tích hợp trên toàn bộ các hướng không gian. Đại lượng $P(r)\,dr$ biểu diễn xác suất tìm thấy electron ở khoảng cách nằm giữa $r$ và $r + dr$, tức là bên trong toàn bộ một lớp vỏ cầu đồng tâm có bán kính $r$ và bề dày vi phân $dr$.
3. Xác suất trong một khoảng khoảng cách hữu hạn từ $r_1$ đến $r_2$ (không thứ nguyên): Được tính bằng tích phân $P_{r_1 \to r_2} = \int_{r_1}^{r_2} P(r)\,dr$.

Xét một lớp vỏ cầu đồng tâm có bề dày vi phân, với bán kính trong là $r$ và bán kính ngoài là $r + dr$. Thể tích $dV$ của lớp vỏ cầu này là diện tích mặt cầu $4\pi r^2$ nhân với bề dày $dr$:

$$
dV = 4\pi r^2 \, dr \tag{41.24}
$$

Đối với các hàm sóng có tính đối xứng cầu (nghĩa là hàm sóng không phụ thuộc vào các tọa độ góc $\theta$ và $\phi$, điển hình là các trạng thái $s$ với $l = 0$), mật độ xác suất $|\psi(r)|^2$ đồng đều trên toàn bộ mặt cầu bán kính $r$. Do đó, hàm phân bố bán kính có dạng đơn giản:

$$
P(r) = 4\pi r^2 |\psi(r)|^2 \tag{41.25}
$$

Đối với các hàm sóng có phụ thuộc vào góc $\theta$ và $\phi$ ($l \ge 1$), đại lượng $|\psi|^2$ trong phương trình (41.25) được thay bằng giá trị trung bình của $|\psi|^2$ lấy trên toàn bộ các hướng không gian. Trong hệ tọa độ cầu tổng quát với phần tử thể tích $dV = r^2 dr\,d\Omega$ (trong đó $d\Omega = \sin\theta\,d\theta\,d\phi$ là phân tố góc khối), xác suất tìm thấy hạt trong lớp vỏ cầu giữa $r$ và $r + dr$ thu được bằng cách lấy tích phân trên toàn bộ mặt cầu đơn vị:

$$
P(r) = r^2 \int |\psi|^2 d\Omega
$$

Vì hàm sóng được phân tách dưới dạng tích $\psi(r, \theta, \phi) = R(r) Y_{l, m_l}(\theta, \phi)$ và phần hàm sóng góc được chuẩn hóa trên mặt cầu đơn vị:

$$
\int |Y_{l, m_l}|^2 d\Omega = 1
$$

phép tích phân góc dẫn đến hệ thức tổng quát cho hàm phân bố bán kính:

$$
P(r) = r^2 |R(r)|^2
$$

Hệ thức $P(r) = r^2 |R(r)|^2$ khẳng định một tính chất cơ bản: Hàm phân bố xác suất bán kính $P(r)$ chỉ phụ thuộc vào số lượng tử chính $n$ và số lượng tử quỹ đạo $l$ (thông qua hàm sóng bán kính $R(r) = R_{n, l}(r)$), hoàn toàn độc lập với số lượng tử từ $m_l$. Vì vậy, các trạng thái có cùng $n$ và $l$ nhưng khác $m_l$ sẽ có cùng hàm phân bố bán kính $P(r)$, cho dù mật độ xác suất ba chiều cục bộ $|\psi(r, \theta, \phi)|^2$ của chúng thay đổi theo hướng góc và phụ thuộc vào $m_l$.

Hình 41.08 biểu diễn đồ thị của hàm phân bố bán kính $P(r)$ cho một số trạng thái lượng tử. Trục khoảng cách $r$ được chuẩn hóa theo bán kính Bohr $a$:

$$
\begin{aligned}
a &= \frac{4\pi\epsilon_0\hbar^2}{m_r e^2} \\
&\approx 5{,}29 \times 10^{-11}\,\text{m}
\end{aligned} \tag{41.26}
$$

![Hình 41.08: Hàm phân bố xác suất bán kính $P(r)$ của các trạng thái nguyên tử hydro, vẽ theo tỷ số $r/a$. Mỗi hàm có số cực đại đúng bằng $n - l$. Các đường cong có $l = n - 1$ ($1s, 2p, 3d, 4f$) chỉ có một cực đại duy nhất tại vị trí $r = n^2 a$.](../img/young-41/hinh-41-08.png)

Một đặc tính quan trọng của hàm phân bố bán kính $P(r)$ là số cực đại của hàm luôn đúng bằng $n - l$. Đặc biệt, đối với các trạng thái có giá trị $l$ lớn nhất trong mỗi lớp vỏ ($l = n - 1$ như các trạng thái tròn $1s, 2p, 3d, 4f$), hàm $P(r)$ chỉ có duy nhất một cực đại, và cực đại này nằm tại đúng khoảng cách:

$$
r = n^2 a
$$

Giá trị này trùng bán kính quỹ đạo tương ứng trong mô hình Bohr.

Lưu ý rằng quy tắc vị trí cực đại $r = n^2 a$ chỉ đúng cho các trạng thái có $l = n - 1$. Đối với các trạng thái có $l < n - 1$, hàm $P(r)$ có nhiều hơn một đỉnh cực đại và cực đại ngoài cùng nằm tại khoảng cách khác $n^2 a$. Chẳng hạn, đối với trạng thái $2s$ ($n = 2, l = 0$), hàm $P(r)$ có cực đại ngoài cùng tại $r = (3 + \sqrt{5})a \approx 5{,}236a$, hoàn toàn khác với vị trí $4a$.

Cần phân biệt rõ hai khái niệm: Mật độ xác suất ba chiều $|\psi|^2$ và hàm phân bố xác suất bán kính $P(r)$. Đại lượng $|\psi|^2$ cho biết xác suất tìm thấy electron trên một đơn vị thể tích tại một điểm cụ thể trong không gian. Đối với trạng thái $1s$, $|\psi|^2$ đạt cực đại tại ngay tâm hạt nhân ($r = 0$). Ngược lại, hàm phân bố bán kính $P(r)$ nhân thêm thừa số diện tích mặt cầu $4\pi r^2$, do đó $P(r) = 0$ tại $r = 0$, và đạt cực đại tại $r = a$.

![Hình 41.09: Hàm phân bố xác suất ba chiều $|\psi|^2$ của các trạng thái đối xứng cầu $1s, 2s$, và $3s$ của nguyên tử hydro. Độ đậm của đám mây tỷ lệ thuận với mật độ xác suất $|\psi|^2$.](../img/young-41/hinh-41-09.png)

![Hình 41.10: Thiết diện cắt ngang của các đám mây mật độ xác suất ba chiều $|\psi|^2$ cho một số trạng thái lượng tử của nguyên tử hydro. Các hình vẽ không cùng tỷ lệ. Quay mỗi hình quanh trục đối xứng $z$ sẽ tạo thành đám mây xác suất ba chiều (chẳng hạn trạng thái $2p, m_l = \pm 1$ có dạng như một chiếc bánh donut mờ ảo).](../img/young-41/hinh-41-10.png)

### Ví dụ 41.4: Hàm sóng trạng thái cơ bản của nguyên tử hydro

Hàm sóng trạng thái cơ bản của nguyên tử hydro (trạng thái $1s$) có dạng:

$$
\psi_{1s}(r) = \frac{1}{\sqrt{\pi a^3}} e^{-r/a}
$$

(a) Chứng minh rằng hàm sóng này đã được chuẩn hóa.

(b) Tính xác suất để tìm thấy electron ở khoảng cách nhỏ hơn bán kính Bohr $a$ tính từ hạt nhân.

#### Phương pháp giải

Hàm sóng $\psi_{1s}(r)$ chỉ phụ thuộc tọa độ bán kính $r$, có tính đối xứng cầu. Chúng ta chọn phần tử thể tích là các lớp vỏ cầu mỏng $dV = 4\pi r^2 dr$. Ở câu (a), tích phân lấy trên toàn bộ không gian từ $r = 0$ đến $r = \infty$. Ở câu (b), tích phân lấy từ $r = 0$ đến $r = a$.

#### Lời giải chi tiết

(a) Đặt tích phân bán kính $I_\infty = \int_0^\infty r^2 e^{-2r/a} \, dr$. Tích phân của mật độ xác suất trên toàn bộ không gian là:

$$
\begin{aligned}
\int |\psi_{1s}|^2 \, dV &= \frac{4}{a^3} I_\infty \\
&= 1
\end{aligned}
$$

Áp dụng công thức tích phân từng phần với nguyên hàm $Q_a(r) = \left(-\frac{a r^2}{2} - \frac{a^2 r}{2} - \frac{a^3}{4}\right) e^{-2r/a}$:

$$
\int r^2 e^{-2r/a} \, dr = Q_a(r)
$$

Khi thay cận $r \to \infty$, thừa số mũ suy giảm về không. Tại cận dưới $r = 0$, hai số hạng đầu triệt tiêu:

$$
\begin{aligned}
[Q_a(r)]_0^\infty &= 0 - (-a^3/4) \\
&= \frac{a^3}{4}
\end{aligned}
$$

Thay kết quả tích phân vào biểu thức chuẩn hóa:

$$
\frac{4}{a^3}\left(\frac{a^3}{4}\right) = 1
$$

Hàm sóng hoàn toàn thỏa mãn điều kiện chuẩn hóa.

(b) Tính xác suất $P$ tìm thấy electron trong miền $r < a$:

$$
P = \frac{4}{a^3} [Q_a(r)]_0^a
$$

Thay cận trên $r = a$ và cận dưới $r = 0$:

$$
[Q_a(r)]_0^a = -\frac{5a^3}{4}e^{-2} + \frac{a^3}{4}
$$

Do đó xác suất tìm thấy electron ở khoảng cách nhỏ hơn $a$ là:

$$
\begin{aligned}
P &= 1 - 5e^{-2} \\
&\approx 1 - 0{,}677 = 0{,}323
\end{aligned}
$$

#### Đánh giá kết quả

Kết quả chỉ ra rằng ở trạng thái cơ bản, xác suất tìm thấy electron ở khoảng cách gần hạt nhân hơn bán kính Bohr $a$ chỉ chiếm khoảng $1/3$ ($32{,}3\%$), trong khi xác suất tìm thấy electron ở khoảng cách xa hơn $a$ chiếm tới gần $2/3$ ($67{,}7\%$).

#### Khái niệm cốt lõi

Nếu một hạt ở trạng thái dừng được mô tả bởi hàm sóng $\psi$, xác suất để tìm thấy hạt ở khoảng cách bán kính trong khoảng từ $r$ đến $r + dr$ là $P(r)\,dr$, với $P(r) = 4\pi r^2 |\psi|^2$ khi hàm sóng có tính đối xứng cầu. Nếu hàm sóng phụ thuộc vào cả tọa độ góc và bán kính, chúng ta phải lấy giá trị trung bình của $|\psi|^2$ trên mọi hướng không gian (tương đương với việc lấy tích phân góc khối trên mặt cầu), dẫn đến hệ thức tổng quát $P(r) = r^2 |R(r)|^2$. Cần phân biệt rõ ba đại lượng: Mật độ xác suất thể tích $|\psi|^2$ tại một điểm trong không gian, mật độ xác suất bán kính $P(r)$ trên toàn bộ lớp vỏ cầu bề dày $dr$, và xác suất toàn phần trong một khoảng bán kính hữu hạn.

### Nguyên tử và ion dạng hydro

Lý thuyết Schrödinger được áp dụng trực tiếp cho các hệ nguyên tử mở rộng:

- Khối lượng rút gọn cần được tính lại khi thay các hạt cấu thành. Positronium gồm electron và positron có cùng khối lượng, nên $m_r=m/2$. Trong nguyên tử muon, electron được thay bằng muon có cùng điện tích nhưng khối lượng lớn hơn khoảng 207 lần. Thay $m_r$ trong các phương trình (41.21) và (41.26) làm thay đổi cả năng lượng lẫn kích thước đặc trưng.
- Với ion chỉ có một electron, chẳng hạn $He^+$ hoặc $Li^{2+}$, hạt nhân mang điện tích $+Ze$. Thay $e^2$ bằng $Ze^2$ trong các phương trình (41.21) và (41.26). Năng lượng nhận hệ số $Z^2$, còn bán kính đặc trưng là $a_Z=a/Z$, với khối lượng rút gọn phù hợp.

### Câu tự kiểm tra 41.3

Sắp xếp các trạng thái lượng tử sau đây của nguyên tử hydro theo thứ tự xác suất tìm thấy electron ở lân cận khoảng cách $r = 5a$ từ cao nhất đến thấp nhất:

- (i) $n = 1, l = 0, m_l = 0$
- (ii) $n = 2, l = 1, m_l = +1$
- (iii) $n = 2, l = 1, m_l = 0$

::: details Lời giải chi tiết
**Đáp án:** Thứ tự sắp xếp từ cao nhất đến thấp nhất là (ii) và (iii) đồng hạng, sau đó đến (i).

**Giải thích:**

1. **Khảo sát từ hàm phân bố bán kính thực tế**:
Xác suất tìm thấy electron trong một khoảng bán kính vi phân quanh vị trí $r$ được xác định bởi hàm phân bố bán kính $P(r) = r^2 |R(r)|^2$:
- Đối với trạng thái $1s$ ($n = 1, l = 0$): Hàm sóng bán kính là $R_{10}(r) = \frac{2}{a^{3/2}} e^{-r/a}$, cho hàm phân bố bán kính:

$$
P_{1s}(r) = \frac{4}{a^3} r^2 e^{-2r/a}
$$

Tại khoảng cách $r = 5a$, giá trị của hàm phân bố bán kính là:

$$
\begin{aligned}
P_{1s}(5a) &= \frac{4}{a^3}(5a)^2 e^{-10} \\
&= \frac{100 e^{-10}}{a} \\
&\approx \frac{0{,}00454}{a}
\end{aligned}
$$

Đuôi hàm mũ suy giảm $e^{-10} \approx 4{,}54 \times 10^{-5}$ khiến xác suất tìm thấy electron $1s$ ở vùng $r = 5a$ giảm xuống mức gần như triệt tiêu.

- Đối với các trạng thái $2p$ ($n = 2, l = 1$): Hàm sóng bán kính là $R_{21}(r) = \frac{1}{2\sqrt{6}a^{3/2}}\frac{r}{a} e^{-r/(2a)}$, cho hàm phân bố bán kính:

$$
P_{2p}(r) = \frac{1}{24 a^5} r^4 e^{-r/a}
$$

Tại khoảng cách $r = 5a$, giá trị của hàm phân bố bán kính là:

$$
\begin{aligned}
P_{2p}(5a) &= \frac{1}{24 a^5}(5a)^4 e^{-5} \\
&= \frac{625 e^{-5}}{24 a} \\
&\approx \frac{0{,}17547}{a}
\end{aligned}
$$

So sánh trực tiếp: $P_{2p}(5a) \approx 38{,}6 \times P_{1s}(5a)$. Xác suất tìm thấy electron ở lân cận $r = 5a$ của trạng thái $2p$ vượt trội hoàn toàn so với trạng thái $1s$.

2. **Quy tắc đỉnh cực đại cho các trạng thái tròn ($l = n - 1$)**:
Cả hai trạng thái trong bài toán này đều là các trạng thái tròn có $l = n - 1$ ($1s$ có $l = 0 = 1 - 1$, và $2p$ có $l = 1 = 2 - 1$). Đối với các trạng thái có $l = n - 1$, hàm $P(r)$ chỉ có duy nhất một đỉnh cực đại nằm tại đúng khoảng cách $r = n^2 a$.
- Trạng thái $1s$ có đỉnh cực đại tại $r = 1^2 a = a$. Vị trí $r = 5a$ cách đỉnh cực đại này một khoảng rất xa ($4a$).
- Trạng thái $2p$ có đỉnh cực đại tại $r = 2^2 a = 4a$. Vị trí $r = 5a$ nằm ngay sát đỉnh cực đại $4a$, do đó mật độ xác suất bán kính vẫn duy trì ở mức rất cao.

Lưu ý rằng quy tắc vị trí cực đại $r = n^2 a$ chỉ đúng tuyệt đối cho các trạng thái có $l = n - 1$. Với các trạng thái có $l < n - 1$, hàm $P(r)$ có $n - l$ cực đại và đỉnh ngoài cùng không nằm tại $n^2 a$. Điển hình như trạng thái $2s$ ($n = 2, l = 0$), hàm $P_{2s}(r)$ có cực đại ngoài cùng nằm tại $r = (3 + \sqrt{5})a \approx 5{,}236a$, chứ không phải tại $4a$.

3. **Tính độc lập của hàm phân bố bán kính với số lượng tử từ $m_l$**:
Hàm phân bố xác suất bán kính $P(r) = r^2 |R(r)|^2$ thu được sau khi đã lấy tích phân trên toàn bộ các góc $\theta$ và $\phi$. Do các hàm cầu điều hòa $Y_{l, m_l}(\theta, \phi)$ đều được chuẩn hóa trên mặt cầu đơn vị, hàm phân bố bán kính $P(r)$ hoàn toàn không phụ thuộc vào số lượng tử từ $m_l$.
Do đó, hai trạng thái (ii) ($2p, m_l = +1$) và (iii) ($2p, m_l = 0$) có cùng một hàm phân bố bán kính $P_{2p}(r)$, và xác suất tìm thấy electron ở lân cận $r = 5a$ của hai trạng thái này hoàn toàn bằng nhau.

Kết luận: Thứ tự sắp xếp từ cao nhất đến thấp nhất là (ii) và (iii) đồng hạng, sau đó đến (i).
:::
