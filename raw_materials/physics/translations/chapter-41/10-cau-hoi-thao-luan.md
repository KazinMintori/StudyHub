## Câu hỏi thảo luận

### Q41.1
Hạt A được mô tả bởi hàm sóng $\psi(x, y, z)$. Hạt B được mô tả bởi hàm sóng:
$$
\psi_B(x, y, z) = \psi(x, y, z) e^{i\phi}
$$
trong đó $\phi$ là một hằng số thực. Xác suất tìm thấy hạt A trong một thể tích $dV$ xung quanh một điểm xác định trong không gian so với xác suất tìm thấy hạt B trong chính thể tích đó như thế nào?

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Hạt A: Hàm sóng $\psi_A(\vec{r}) = \psi(\vec{r})$.
- Hạt B: Hàm sóng $\psi_B = \psi_A e^{i\phi}$ với $\phi \in \mathbb{R}$.
- So sánh xác suất tìm thấy hạt $P_A(dV)$ và $P_B(dV)$ trong cùng thể tích vi phân $dV$.

**Hướng đi:**
- Xác suất tìm thấy hạt trong phần tử thể tích $dV$ tỉ lệ với bình phương độ lớn của hàm sóng tại điểm đó: $dP = |\psi(\vec{r})|^2 dV$.
- Khi nhân hàm sóng với một thừa số pha toàn cục $e^{i\phi}$ ($\phi \in \mathbb{R}$), ta tính môđun số phức thông qua công thức Euler:
$$
|e^{i\phi}|^2 = \cos^2\phi + \sin^2\phi = 1
$$
- Từ đó so sánh mật độ xác suất $|\psi_A|^2$ và $|\psi_B|^2$.

**Lời giải chi tiết:**
1. Mật độ xác suất tìm thấy hạt A tại điểm $\vec{r} = (x, y, z)$ là:
$$
|\psi_A(x, y, z)|^2 = |\psi(x, y, z)|^2
$$
Xác suất tìm thấy hạt A trong thể tích vi phân $dV$ quanh điểm đó là:
$$
dP_A = |\psi(x, y, z)|^2 dV
$$

2. Mật độ xác suất tìm thấy hạt B tại cùng điểm $\vec{r}$ là:
$$
\begin{aligned}
|\psi_B(\vec{r})|^2 &= |\psi(\vec{r}) e^{i\phi}|^2 \\
&= |\psi(\vec{r})|^2 |e^{i\phi}|^2
\end{aligned}
$$
Vì $\phi$ là một hằng số thực, số phức liên hợp của $e^{i\phi}$ là $e^{-i\phi}$, do đó:
$$
|e^{i\phi}|^2 = e^{i\phi} e^{-i\phi} = e^0 = 1
$$
Suy ra:
$$
\begin{aligned}
|\psi_B(\vec{r})|^2 &= |\psi(\vec{r})|^2 \\
&= |\psi_A(\vec{r})|^2
\end{aligned}
$$

3. Xác suất tìm thấy hạt B trong thể tích $dV$ là:
$$
\begin{aligned}
\mathrm{d}P_B &= |\psi_B(x, y, z)|^2\,\mathrm{d}V \\
&= \mathrm{d}P_A
\end{aligned}
$$

**Kết luận:** Xác suất tìm thấy hạt A và hạt B trong cùng một thể tích $dV$ tại bất kỳ vị trí nào trong không gian là hoàn toàn bằng nhau. Thừa số pha toàn cục $e^{i\phi}$ không làm thay đổi bất kỳ đại lượng đo đạc vật lý nào của hệ lượng tử.
</details>

### Q41.2
Những điểm khác biệt lớn nhất giữa mô hình Bohr của nguyên tử hydro và phân tích bằng phương trình Schrödinger là gì? Những điểm tương đồng giữa hai mô hình là gì?

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- So sánh hai mô hình nguyên tử hydro: Mô hình bán cổ điển Bohr và cơ học lượng tử dạng sóng Schrödinger.
- Nêu rõ các điểm khác biệt cốt lõi và các điểm tương đồng then chốt.

**Hướng đi:**
- Phân tích bản chất chuyển động của electron: Quỹ đạo hạt xác định (Bohr) so với đám mây mật độ xác suất ba chiều (Schrödinger).
- So sánh các số lượng tử và độ lớn mômen động lượng quỹ đạo.
- Phân tích trạng thái cơ bản ($n=1$): Mômen động lượng bằng bao nhiêu ở mỗi mô hình?
- Nêu các điểm tương đồng về năng lượng ion hóa, kích thước thang đo và quang phổ phát xạ.

**Lời giải chi tiết:**
1. **Các điểm khác biệt lớn nhất:**
   - **Bản chất quỹ đạo và vị trí của electron:**
   - *Mô hình Bohr*: Giả định electron là chất điểm chuyển động trên các quỹ đạo tròn phẳng cố định có bán kính gián đoạn xác định $r_n = n^2 a_0$, với vận tốc và vị trí được xác định chính xác tại mọi thời điểm (mâu thuẫn với nguyên lý bất định Heisenberg).
   - *Mô hình Schrödinger*: Không tồn tại khái niệm quỹ đạo xác định. Electron được mô tả bằng hàm sóng không gian ba chiều $\psi(r, \theta, \phi)$, và vị trí chỉ được mô tả thông qua mật độ xác suất $|\psi|^2$ trong không gian.
   - **Mômen động lượng quỹ đạo ($L$):**
   - *Mô hình Bohr*: Giả thiết lượng tử hóa tiên đề gán $L = n\hbar$ với $n = 1, 2, 3, \dots$. Do đó, trạng thái cơ bản $n=1$ có $L = 1\hbar \ne 0$.
   - *Mô hình Schrödinger*: Mômen động lượng quỹ đạo phụ thuộc vào số lượng tử quỹ đạo $l$ ($l = 0, 1, \dots, n-1$) theo công thức:
$$
L = \sqrt{l(l+1)}\,\hbar
$$
Ở trạng thái cơ bản ($n=1, l=0$), mômen động lượng quỹ đạo bằng $0$ ($L = 0$), electron không quay quanh hạt nhân mà có hàm sóng đối xứng cầu hoàn toàn.
   - **Số lượng tử mô tả:**
   - *Mô hình Bohr*: Chỉ sử dụng một số lượng tử duy nhất là $n$.
   - *Mô hình Schrödinger*: Cần ba số lượng tử không gian $(n, l, m_l)$ xuất phát tự nhiên từ việc giải phương trình vi phân đạo hàm riêng trong tọa độ cầu, cùng với số lượng tử spin $m_s$ mô tả bậc tự do nội tại.

2. **Các điểm tương đồng:**
   - **Mức năng lượng gián đoạn:** Cả hai mô hình đều đưa ra các mức năng lượng gián đoạn giống hệt nhau đối với nguyên tử hydro:
$$
E_n = -\frac{13{,}6\,\mathrm{eV}}{n^2}
$$
   - **Kích thước thang đo của nguyên tử:** Cả hai mô hình đều dẫn đến thang độ dài đặc trưng là bán kính Bohr:
$$
a_0 \approx 0{,}529 \times 10^{-10}\,\mathrm{m}
$$
Trong mô hình Schrödinger, $a_0$ chính là khoảng cách mà tại đó mật độ xác suất hướng tâm $P(r)$ của trạng thái cơ bản đạt cực đại.
   - **Giải thích quang phổ:** Cả hai mô hình đều giải thích định lượng chính xác bước sóng các vạch quang phổ của dãy Lyman, Balmer, Paschen thông qua công thức Rydberg:
$$
\Delta E = h\nu
$$
</details>

### Q41.3
Đối với một vật thể quay quanh Mặt Trời, chẳng hạn một hành tinh, sao chổi hoặc tiểu hành tinh, có bất kỳ hạn chế nào về thành phần $z$ của mômen động lượng quỹ đạo giống như thành phần $z$ của mômen động lượng electron trong nguyên tử hydro không? Giải thích.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Xét thiên thể vĩ mô quay quanh Mặt Trời chịu lực hấp dẫn.
- Câu hỏi: Thành phần $L_z$ của thiên thể có bị lượng tử hóa gián đoạn như $L_z = m_l\hbar$ trong nguyên tử hydro không?

**Hướng đi:**
- Xét phạm vi áp dụng của cơ học lượng tử và nguyên lý tương ứng Bohr (Bohr's correspondence principle).
- Tính toán bậc độ lớn của mômen động lượng vĩ mô và so sánh với hằng số Planck rút gọn $\hbar$.
- Giải thích vì sao tính gián đoạn không thể quan sát được trong thực nghiệm.

**Lời giải chi tiết:**
1. **Về mặt nguyên lý cơ học lượng tử thuần túy:**
   - Mọi hệ vật lý hữu hạn trong tự nhiên đều chịu sự chi phối của các quy luật lượng tử. Về mặt toán học hình thức, mômen động lượng quỹ đạo của một hành tinh cũng được lượng tử hóa theo các bội số nguyên của $\hbar$:
$$
L_z = m_l\hbar \quad (m_l \in \mathbb{Z})
$$

2. **Về mặt vật lý thực nghiệm và cơ học cổ điển:**
   - Hãy ước tính mômen động lượng của Trái Đất quay quanh Mặt Trời với khối lượng $M \approx 6 \cdot 10^{24}\,\mathrm{kg}$, bán kính $R \approx 1{,}5 \cdot 10^{11}\text{ m}$, và tốc độ $v \approx 3 \cdot 10^4\,\mathrm{m/s}$:
$$
L \approx M v R \approx 2{,}7 \times 10^{40}\,\mathrm{J\cdot s}
$$
   - Số lượng tử tương ứng có bậc độ lớn:
$$
l \approx \frac{L}{\hbar} \approx 2{,}6 \times 10^{74}
$$
   - Khoảng cách giữa hai mức giá trị $L_z$ kế tiếp nhau là:
$$
\begin{aligned}
\Delta L_z &= \hbar \\
&\approx 1{,}05 \times 10^{-34}\,\mathrm{J\cdot s}
\end{aligned}
$$
   - Tỷ số bước nhảy lượng tử trên tổng mômen động lượng là:
$$
\frac{\Delta L_z}{L} \approx 10^{-74}
$$

Bước lượng tử rất nhỏ so với mômen quỹ đạo vĩ mô đang xét. Vì thế, mô tả cổ điển xem mômen biến đổi liên tục là một gần đúng phù hợp ở thang này. Điều đó không có nghĩa định luật lượng tử chỉ áp dụng cho nguyên tử.
</details>

### Q41.4
Tại sao việc phân tích nguyên tử heli lại phức tạp hơn rất nhiều so với nguyên tử hydro, dù trong mô hình kiểu Bohr hay khi sử dụng phương trình Schrödinger?

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** So sánh mức độ phức tạp của heli và hydro trong mô hình quỹ đạo và trong phương trình Schrödinger.

**Hướng đi:**

- Hydro chỉ có một electron. Thế năng của nó phụ thuộc khoảng cách đến hạt nhân.
- Heli có thêm lực đẩy giữa hai electron. Khoảng cách giữa chúng phụ thuộc đồng thời hai vị trí, nên không thể xem chúng như hai bài toán hydro độc lập.
- Khi dùng hàm sóng, còn phải thỏa mãn điều kiện hoán đổi các electron giống nhau.

Đặt $K=e^2/(4\pi\varepsilon_0)$, còn $r_1,r_2$ là các khoảng cách electron đến hạt nhân. Khoảng cách giữa hai electron là:

$$
r_{12}=|\mathbf r_1-\mathbf r_2|.
$$

Ba phần thế năng Coulomb của heli là:

$$
\begin{aligned}
U_1&=-\frac{2K}{r_1},\\
U_2&=-\frac{2K}{r_2},\\
W&=\frac{K}{r_{12}},\\
U&=U_1+U_2+W.
\end{aligned}
$$

Số hạng $W$ ghép chuyển động của hai electron. Trong một mô hình kiểu Bohr, lực lên electron thứ nhất phụ thuộc vị trí electron thứ hai. Vì vậy, hai quỹ đạo không thể được xác định như hai quỹ đạo Kepler độc lập.

Trong phương trình Schrödinger, hàm sóng phụ thuộc cả hai vị trí. Số hạng $W$ ngăn việc tách bài toán chính xác thành hai phương trình một electron. Các phương pháp trường trung bình xử lý nó gần đúng, rồi có thể kể thêm tương quan giữa electron.

Tương tác này không làm mất bất biến khi quay đồng thời toàn hệ, vì $r_1,r_2,r_{12}$ đều giữ nguyên dưới phép quay ấy. Điều bị mất là dạng thế xuyên tâm độc lập cho từng electron khi giữ vị trí electron còn lại cố định. Hàm sóng toàn phần cũng phải đối xứng lẻ khi hoán đổi hai electron.

</details>

### Q41.5
Thí nghiệm Stern–Gerlach luôn được thực hiện với các chùm nguyên tử trung hòa. Liệu có dễ dàng hơn nếu tạo chùm bằng các nguyên tử ion hóa không? Tại sao phương án này không hoạt động được?

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Giải thích tại sao thí nghiệm Stern–Gerlach bắt buộc dùng chùm nguyên tử trung hòa thay vì chùm ion mang điện.

**Hướng đi:**
- Xác định các lực tác dụng lên hạt mang điện chuyển động trong từ trường không đồng nhất.
- So sánh độ lớn giữa lực Lorentz $\vec{F}_L = q(\vec{v} \times \vec{B})$ và lực do gradient từ trường:
$$
\vec{F}_m = \nabla(\vec{\mu}\cdot\vec{B})
$$
- Phân tích ảnh hưởng của sự tán xạ vận tốc trong chùm ion thực tế.

**Lời giải chi tiết:**
1. **Lực tác dụng trong thí nghiệm Stern–Gerlach:**
   - Mục đích của thí nghiệm là đo lực tách do mômen từ của hạt gây ra trong từ trường có gradient:
$$
F_z = \mu_z \frac{\partial B_z}{\partial z}
$$
   - Với nguyên tử có $\mu \sim 10^{-23}\,\mathrm{J/T}$ và gradient từ trường mạnh:
$$
\frac{\partial B_z}{\partial z} \sim 10^3\,\mathrm{T/m}
$$
Lực này rất nhỏ:
$$
\begin{aligned}
F_m &\approx 10^{-23} \times 10^3 \\
&= 10^{-20}\,\mathrm{N}
\end{aligned}
$$

2. **Lực Lorentz tác dụng lên ion:**
   - Nếu sử dụng ion mang điện tích $q = \pm e$ chuyển động với vận tốc nhiệt $v \sim 10^3\,\mathrm{m/s}$ trong từ trường $B \sim 1\,\mathrm{T}$, lực Lorentz tác dụng lên ion là:
$$
\begin{aligned}
F_L &= q v B \\
&\approx (1{,}6 \times 10^{-19})(10^3)(1) \\
&= 1{,}6 \times 10^{-16}\,\mathrm{N}
\end{aligned}
$$
   - So sánh hai lực:
$$
\begin{aligned}
\frac{F_L}{F_m} &\approx \frac{1{,}6 \times 10^{-16}}{10^{-20}} \\
&= 16\,000
\end{aligned}
$$
Lực Lorentz lớn hơn lực gradient từ tới hơn 4 bậc độ lớn (hàng chục nghìn lần).

3. **Hậu quả đối với chùm hạt:**
   - Trong thực tế, các hạt trong chùm có sự phân bố vận tốc nhiệt (phân bố Maxwell-Boltzmann). Độ lệch do lực Lorentz phụ thuộc trực tiếp vào vận tốc $v$, khiến chùm ion bị uốn cong mạnh mẽ và phân tán loang lổ trên một diện tích rộng.
   - Độ lệch khổng lồ và không đồng đều này sẽ che lấp, làm nhòe và phá hủy hoàn toàn sự phân tách tinh tế thành hai vạch gián đoạn do spin. Do đó, bắt buộc phải dùng nguyên tử trung hòa ($q = 0$) để triệt tiêu hoàn toàn lực Lorentz.
</details>

### Q41.6
(a) Nếu hai electron trong các nguyên tử hydro có cùng số lượng tử chính $n$, chúng có thể có mômen động lượng quỹ đạo khác nhau không? Bằng cách nào?

(b) Nếu hai electron trong các nguyên tử hydro có cùng số lượng tử quỹ đạo $l$, chúng có thể có số lượng tử chính khác nhau không? Bằng cách nào?

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- (a) Cùng $n$, có thể khác $L$ không?
- (b) Cùng $l$, có thể khác $n$ không?

**Hướng đi:**
- Dựa trên miền giá trị cho phép của các số lượng tử trong nghiệm của phương trình Schrödinger cho hydro:
$$
n = 1, 2, 3, \dots
$$
$$
l = 0, 1, 2, \dots, n-1
$$
- Độ lớn mômen động lượng quỹ đạo được xác định duy nhất bởi $l$:
$$
L = \sqrt{l(l+1)}\,\hbar
$$

**Lời giải chi tiết:**
1. **Phần (a): Cùng số lượng tử chính $n$**
   - Hoàn toàn có thể. Với một giá trị $n$ cho trước, số lượng tử quỹ đạo $l$ có thể nhận bất kỳ giá trị nguyên nào từ $0$ đến $n-1$.
   - Mỗi giá trị $l$ khác nhau tương ứng với một độ lớn mômen động lượng quỹ đạo $L = \sqrt{l(l+1)}\hbar$ khác nhau.
   - *Ví dụ*: Với $n = 2$, electron có thể ở phân lớp 2s ($l=0 \implies L=0$) hoặc phân lớp 2p ($l=1 \implies L=\sqrt{2}\hbar$). Hai electron này có cùng năng lượng (cùng $n$) nhưng có mômen động lượng quỹ đạo hoàn toàn khác nhau.

2. **Phần (b): Cùng số lượng tử quỹ đạo $l$**
   - Hoàn toàn có thể. Điều kiện toán học chỉ yêu cầu $n \ge l + 1$. Do đó, với một giá trị $l$ cố định, số lượng tử chính $n$ có thể nhận vô số giá trị nguyên: $n = l+1, l+2, l+3, \dots$
   - *Ví dụ*: Với $l = 1$ (các trạng thái p), electron có thể ở mức $n = 2$ (trạng thái 2p), $n = 3$ (trạng thái 3p), $n = 4$ (trạng thái 4p)... Tất cả các trạng thái này đều có cùng độ lớn mômen động lượng quỹ đạo $L = \sqrt{2}\hbar$, nhưng có số lượng tử chính $n$ khác nhau, dẫn đến bán kính trung bình và mức năng lượng $E_n$ khác biệt hoàn toàn.
</details>

### Q41.7
Trong thí nghiệm Stern–Gerlach, tại sao từ trường bắt buộc phải không đồng nhất (nghĩa là có gradient biến thiên theo không gian)?

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Giải thích vai trò bản chất của gradient từ trường $\frac{\partial B_z}{\partial z} \ne 0$ trong thí nghiệm Stern–Gerlach.

**Hướng đi:**
- Xét thế năng tương tác của lưỡng cực từ trong từ trường: $U = -\vec{\mu} \cdot \vec{B}$.
- Sử dụng mối liên hệ giữa thế năng và lực: $\vec{F} = -\nabla U$.
- Phân tích chuyển động của lưỡng cực từ trong từ trường đều và từ trường không đều.

**Lời giải chi tiết:**
1. **Xét trường hợp từ trường đều ($\vec{B} = \text{const}$):**
   - Thế năng tương tác là $U = -\mu_z B_z$. Lực tịnh tiến tác dụng lên hạt là:
$$
\vec{F} = -\nabla U = \nabla(\vec{\mu} \cdot \vec{B})
$$
   - Vì $\vec{B}$ không đổi theo không gian, đạo hàm không gian triệt tiêu: $\nabla B_z = 0$, kéo theo $\vec{F} = \vec{0}$.
   - Khi đó, từ trường chỉ tác dụng một moment ngẫu lực quay:
$$
\vec{\tau} = \vec{\mu} \times \vec{B}
$$
Moment ngẫu lực này làm cho vector mômen từ tuế sai quanh phương của $\vec{B}$ (chuyển động tuế sai Larmor), nhưng khối tâm của nguyên tử không bị gia tốc hay lệch hướng chuyển động. Toàn bộ chùm nguyên tử sẽ đi thẳng và chỉ tạo thành một vệt duy nhất ở tâm màn hứng.

2. **Xét trường hợp từ trường không đồng nhất:**
   - Thiết kế các cực nam châm bất đối xứng tạo ra một gradient từ trường mạnh theo phương $z$, tức $\frac{\partial B_z}{\partial z} \ne 0$.
   - Khi đó, thành phần lực tịnh tiến theo phương $z$ tác dụng lên nguyên tử là:
$$
F_z = -\frac{\partial U}{\partial z} = \mu_z \frac{\partial B_z}{\partial z}
$$
   - Lực tịnh tiến $F_z$ này khác $0$ và có dấu phụ thuộc trực tiếp vào dấu của $\mu_z$:
   - Hạt có $\mu_z > 0$ chịu lực hướng theo chiều tăng của từ trường.
   - Hạt có $\mu_z < 0$ chịu lực hướng theo chiều giảm của từ trường.

**Kết luận:** Gradient từ trường là điều kiện tiên quyết để chuyển đổi sự định hướng lượng tử của spin thành lực tịnh tiến không gian, làm tách chùm hạt thành các vệt riêng rẽ trên màn quan sát.
</details>

### Q41.8
Ở trạng thái cơ bản của nguyên tử heli, một electron phải có "spin lên" và electron kia phải có "spin xuống". Tại sao?

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Giải thích cấu hình spin đối song song của hai electron trong trạng thái cơ bản của nguyên tử heli.

**Hướng đi:**
- Xác định trạng thái không gian có năng lượng thấp nhất của nguyên tử heli.
- Áp dụng nguyên lý loại trừ Pauli cho hai fermion đồng nhất.
- Liệt kê bộ bốn số lượng tử $(n, l, m_l, m_s)$ của từng electron.

**Lời giải chi tiết:**
1. **Trạng thái không gian cơ bản:**
   - Để nguyên tử heli đạt trạng thái có năng lượng toàn phần thấp nhất (trạng thái cơ bản), cả hai electron đều có xu hướng chiếm mức orbital liên kết chặt chẽ nhất với hạt nhân, đó là orbital 1s với bộ ba số lượng tử không gian:
$$
n = 1, \quad l = 0, \quad m_l = 0
$$

2. **Áp dụng nguyên lý loại trừ Pauli:**
   - Nguyên lý loại trừ Pauli khẳng định: Hai electron (fermion) trong cùng một nguyên tử không bao giờ được phép có cùng một bộ bốn số lượng tử $(n, l, m_l, m_s)$.
   - Vì hai electron đã có cùng ba số lượng tử không gian $(1, 0, 0)$, số lượng tử spin $m_s$ của chúng bắt buộc phải khác nhau.
   - Electron chỉ có hai trạng thái spin khả dĩ: $m_s = +1/2$ (spin lên) và $m_s = -1/2$ (spin xuống).
   - Do đó, một electron bắt buộc phải nhận $m_s = +1/2$ và electron còn lại bắt buộc phải nhận $m_s = -1/2$.

**Kết luận:** Trạng thái cơ bản của heli bắt buộc phải gồm một cặp electron có spin đối song song (spin-singlet, $S=0$) để thỏa mãn nguyên lý loại trừ Pauli.
</details>

### Q41.9
Một electron trong nguyên tử hydro ở mức s, và nguyên tử nằm trong một từ trường $\vec{B} = B\hat{k}$. Hãy giải thích tại sao trạng thái "spin lên" ($m_s = +1/2$) lại có năng lượng cao hơn trạng thái "spin xuống" ($m_s = -1/2$).

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Electron ở mức s ($l=0$) trong từ trường $\vec{B} = B\hat{k}$.
- Ký hiệu hai năng lượng spin hướng lên và hướng xuống là $E_\uparrow$ và $E_\downarrow$. Dùng dấu mômen từ electron để giải thích vì sao $E_\uparrow>E_\downarrow$.

**Hướng đi:**
- Xác định mối liên hệ giữa spin $\vec{S}$ và mômen từ spin $\vec{\mu}_s$.
- Lưu ý điện tích âm của electron khiến vector mômen từ ngược hướng với vector spin.
- Viết công thức thế năng tương tác từ $U = -\vec{\mu}_s \cdot \vec{B}$ và xác định dấu thế năng ứng với mỗi hướng spin.

**Lời giải chi tiết:**
1. **Mối quan hệ giữa mômen từ spin và vector spin của electron:**
   - Mômen từ spin của electron được cho bởi công thức:
$$
\vec{\mu}_s = -g_s \frac{e}{2m_e} \vec{S} \approx -\frac{e}{m_e} \vec{S}
$$
   - Vì điện tích electron là âm ($-e$), vector mômen từ $\vec{\mu}_s$ luôn có chiều **ngược lại** với chiều của vector spin $\vec{S}$.
   - Chiếu lên trục $z$ song song với từ trường ngoài $\vec{B} = B\hat{k}$:
$$
\mu_{s,z} = -g_s \mu_B m_s
$$
với $\mu_B = \frac{e\hbar}{2m_e} > 0$ và $g_s \approx 2$.

2. **Thế năng tương tác từ:**
   - Thế năng của lưỡng cực từ trong từ trường ngoài là:
$$
\begin{aligned}
U &= -\vec{\mu}_s \cdot \vec{B} \\
&= -\mu_{sz} B \\
&= g_s \mu_B B m_s
\end{aligned}
$$
   - Khi electron có "spin lên" ($m_s = +1/2$): Vector spin hướng theo chiều dương trục $z$, nhưng mômen từ lại hướng theo chiều âm trục $z$ ($\mu_{s,z} < 0$). Do mômen từ ngược chiều với từ trường ngoài, thế năng đạt giá trị dương (trạng thái kém bền):
$$
U = +\frac{1}{2} g_s \mu_B B > 0
$$
   - Khi electron có "spin xuống" ($m_s = -1/2$): Vector spin hướng theo chiều âm trục $z$, nên mômen từ hướng cùng chiều với từ trường ngoài ($\mu_{s,z} > 0$). Thế năng đạt giá trị âm (trạng thái bền vững hơn):
$$
U = -\frac{1}{2} g_s \mu_B B < 0
$$

3. **Độ chênh lệch năng lượng:**
$$
\Delta U = g_s \mu_B B \approx 2\mu_B B
$$

**Kết luận:** Trạng thái spin lên có mômen từ ngược chiều từ trường nên có năng lượng tương tác cao hơn trạng thái spin xuống.
</details>

### Q41.10
Gần đúng trường xuyên tâm (central-field approximation) chính xác hơn nhiều đối với các kim loại kiềm so với các kim loại chuyển tiếp như sắt, niken hoặc đồng. Tại sao?

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Giải thích vì sao gần đúng trường xuyên tâm thích hợp hơn với kim loại kiềm so với những kim loại chuyển tiếp được nêu.

**Hướng đi:**

- Trường xuyên tâm thay tác dụng của hạt nhân và các electron còn lại bằng một thế trung bình chỉ phụ thuộc bán kính.
- Một lõi kín và một electron hóa trị ở xa là cấu trúc thuận lợi cho phép lấy trung bình ấy.
- Khi nhiều phân lớp có năng lượng gần nhau và chồng lấp, tương quan cùng sự sắp xếp electron cần được xét kỹ hơn.

Ở kim loại kiềm, các electron bên trong tạo một lõi khí hiếm kín. Electron hóa trị chủ yếu ở bên ngoài lõi, nên thế trung bình mà nó cảm nhận gần đối xứng cầu. Cách mô tả bằng một electron ngoài lõi vì vậy cho phép dự đoán khá tốt nhiều mức hóa trị.

Ở các kim loại chuyển tiếp như sắt và niken, phân lớp $d$ chưa đầy tham gia vào cấu trúc electron. Các orbital $d$ và $s$ có thể chồng lấp đáng kể và có năng lượng gần nhau. Việc thay mọi tương tác giữa electron bằng một thế chỉ theo bán kính bỏ qua những chi tiết quan trọng hơn.

Riêng đồng có cấu hình cơ bản kết thúc bằng $3d^{10}4s$, nên không được nói phân lớp $d$ của mọi nguyên tố trong danh sách đều đang điền dở. Sự hiện diện của các phân lớp gần nhau, mức độ thâm nhập và tương quan electron vẫn làm so sánh với kim loại kiềm trở nên cần thiết.

Gần đúng trường xuyên tâm là phép lấy trung bình, không phải khẳng định từng electron luôn chuyển động trong một trường cầu chính xác tại mọi thời điểm.

</details>

### Q41.11
Bảng cấu hình electron cho thấy ở trạng thái cơ bản của nguyên tử kali, electron ngoài cùng nằm ở trạng thái 4s. Điều này cho bạn biết gì về năng lượng tương đối của các mức 3d và 4s đối với nguyên tử này? Hãy giải thích.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Kali ($Z=19$): Electron thứ 19 chiếm orbital 4s thay vì 3d.
- Rút ra kết luận về năng lượng tương đối $E_{4s}$ và $E_{3d}$ và giải thích cơ chế vật lý.

**Hướng đi:**
- Dựa trên nguyên lý vững bền (Aufbau principle): Electron điền vào mức có năng lượng thấp nhất trước.
- Rút ra so sánh năng lượng: $E_{4s} < E_{3d}$.
- Giải thích cơ chế dựa trên hiệu ứng xâm nhập gần hạt nhân (penetration) và hiệu ứng chắn (screening).

**Lời giải chi tiết:**
1. **Kết luận về năng lượng tương đối:**
   - Theo nguyên lý năng lượng cực tiểu, các electron ở trạng thái cơ bản luôn điền vào các orbital có mức năng lượng thấp nhất có thể.
   - Việc electron thứ 19 của kali ($Z=19$) chiếm orbital 4s thay vì orbital 3d chứng tỏ rõ ràng rằng đối với nguyên tử kali:
$$
E_{4s} < E_{3d}
$$

2. **Giải thích cơ chế vật lý (Hiệu ứng xâm nhập và chắn):**
   - Trong nguyên tử hydro (hệ một electron), mức năng lượng chỉ phụ thuộc vào số lượng tử chính $n$, do đó mức 3d ($n=3$) có năng lượng thấp hơn mức 4s ($n=4$).
   - Tuy nhiên, trong nguyên tử nhiều electron như kali, thế năng tương tác hiệu dụng bị chi phối bởi hiệu ứng chắn của 18 electron lõi (cấu hình argon $1s^2 2s^2 2p^6 3s^2 3p^6$).
   - **Orbital 4s ($l=0$):** Không có rào thế ly tâm. Hàm sóng của orbital 4s có mật độ xác suất khác không ngay tại tâm hạt nhân và sở hữu 3 mặt cầu nút, tạo ra các cực đại phụ nằm sâu bên trong lớp vỏ argon, rất gần hạt nhân. Nhờ hiệu ứng xâm nhập sâu này, electron 4s ít bị chắn hơn và cảm nhận điện tích hạt nhân hiệu dụng lớn hơn:
$$
Z_{\mathrm{eff}}(4s) > Z_{\mathrm{eff}}(3d)
$$
   - **Orbital 3d ($l=2$):** Có rào thế ly tâm mạnh đẩy electron ra xa hạt nhân. Hàm sóng 3d hầu như nằm hoàn toàn bên ngoài lõi argon, do đó bị toàn bộ 18 electron lõi chắn gần như trọn vẹn ($Z_{\mathrm{eff}} \approx 19 - 18 = 1$).

**Kết luận:** Do hiệu ứng xâm nhập mạnh hơn, electron 4s chịu lực hút tĩnh điện trung bình từ hạt nhân lớn hơn, kéo mức năng lượng $E_{4s}$ xuống thấp hơn mức $E_{3d}$ ở nguyên tử kali.
</details>

### Q41.12
Lực hấp dẫn có đóng vai trò đáng kể trong cấu trúc nguyên tử không? Hãy giải thích.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Đánh giá vai trò của lực hấp dẫn trong cấu trúc nguyên tử.
- Chứng minh bằng phép so sánh định lượng giữa lực hấp dẫn và lực tĩnh điện.

**Hướng đi:**
- Viết định luật hấp dẫn vạn vật Newton giữa proton và electron: $F_g = \frac{G m_e m_p}{r^2}$.
- Viết định luật Coulomb về lực tĩnh điện:
$$
F_e = \frac{e^2}{4\pi\varepsilon_0 r^2}
$$
- Lập tỷ số $F_g / F_e$ để so sánh độ lớn độc lập với khoảng cách $r$.

**Lời giải chi tiết:**
1. **Thiết lập công thức so sánh:**
   - Xét tương tác giữa một electron và một proton cách nhau khoảng cách $r$:
$$
F_g = G \frac{m_e m_p}{r^2}
$$
$$
F_e = \frac{1}{4\pi\varepsilon_0} \frac{e^2}{r^2}
$$
   - Tỷ số độ lớn giữa lực hấp dẫn và lực tĩnh điện là:
$$
\frac{F_g}{F_e} = \frac{4\pi\varepsilon_0 G m_e m_p}{e^2}
$$

2. **Thay số:**
   - Thay các hằng số vật lý trong hệ đơn vị SI:
$$
\begin{aligned}
&G \approx 6{,}674 \times 10^{-11}\,\mathrm{SI}, \\
&m_e \approx 9{,}109 \times 10^{-31}\,\mathrm{kg}, \\
&m_p \approx 1{,}673 \times 10^{-27}\,\mathrm{kg}, \\
&e \approx 1{,}602 \times 10^{-19}\,\mathrm{C}, \\
&k_e \approx 8{,}988 \times 10^9\,\mathrm{SI}.
\end{aligned}
$$
   - Ta thu được:
$$
\frac{F_g}{F_e} \approx 4{,}4 \times 10^{-40}
$$

**Kết luận:** Lực hấp dẫn yếu hơn lực tĩnh điện tới 40 bậc độ lớn. Vì vậy, lực hấp dẫn hoàn toàn không đóng bất kỳ vai trò nào có thể đo đạc được trong cấu trúc nguyên tử, mức năng lượng hay quang phổ phát xạ.
</details>

### Q41.13
Tại sao các nguyên tố chuyển tiếp ($Z = 21$ đến 30) đều có tính chất hóa học tương tự nhau?

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Giải thích lý do chuỗi nguyên tố chuyển tiếp thứ nhất ($Z = 21$ đến 30, từ Sc đến Zn) có tính chất hóa học rất tương đồng.

**Hướng đi:**
- Xác định yếu tố quyết định tính chất hóa học của một nguyên tố (cấu hình lớp vỏ ngoài cùng).
- Phân tích cấu hình electron của dãy chuyển tiếp: Quá trình điền electron xảy ra ở phân lớp bên trong $(n-1)d = 3d$.
- Nhận xét cấu hình lớp ngoài cùng $4s$ hầu như không đổi.

**Lời giải chi tiết:**
1. **Yếu tố chi phối tính chất hóa học:**
   - Electron hóa trị tham gia trực tiếp vào liên kết với các nguyên tử lân cận. Cấu hình của chúng vì thế chi phối tính chất hóa học. Với nguyên tố chuyển tiếp, cả electron $4s$ và electron $3d$ đều có thể tham gia.

2. **Đặc điểm cấu hình electron dãy chuyển tiếp $3d$ ($Z = 21$ đến 30):**
   - Khi tăng dần số điện tích hạt nhân $Z$ từ scandium ($Z=21$) đến kẽm ($Z=30$), các electron bổ sung không điền vào lớp ngoài cùng $n=4$ mà điền dần vào phân lớp bên trong là **$3d$**:
   - Sc ($Z=21$): $[\mathrm{Ar}]\,3d^1 4s^2$
   - Ti ($Z=22$): $[\mathrm{Ar}]\,3d^2 4s^2$
   - $\dots$
   - Zn ($Z=30$): $[\mathrm{Ar}]\,3d^{10} 4s^2$
   - Hầu như toàn bộ chuỗi nguyên tố này đều giữ nguyên cấu hình lớp ngoài cùng là **$4s^2$** (ngoại trừ crom $[\mathrm{Ar}]\,3d^5 4s^1$ và đồng $[\mathrm{Ar}]\,3d^{10} 4s^1$ do độ bền đặc biệt của phân lớp d bán bão hòa và bão hòa).

3. **Hệ quả đối với tính chất hóa học:**
   - Sự biến đổi tương đối ít của cấu hình ngoài cùng góp phần tạo nên tính kim loại và những nét tương đồng trong dãy. Nhiều nguyên tố tạo ion $+2$ khi mất hai electron $4s$, nhưng đây không phải quy tắc cho mọi nguyên tố. Phân lớp $3d$ còn dẫn đến các trạng thái oxy hóa khác nhau.

**Kết luận:** Việc điền dần electron vào phân lớp bên trong $3d$ trong khi giữ nguyên lớp ngoài cùng $4s$ chính là nguyên nhân khiến các nguyên tố chuyển tiếp có tính chất hóa học rất tương tự nhau.
</details>

### Q41.14
Sử dụng kiến thức cấu hình electron để xác định cấu hình electron trạng thái cơ bản của nguyên tử gali trung hòa ($\mathrm{Ga}$) cũng như các ion $\mathrm{Ga}^+$ và $\mathrm{Ga}^-$. Gali có số hiệu nguyên tử là 31.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Số hiệu nguyên tử của gali: $Z = 31$.
- Xác định cấu hình electron trạng thái cơ bản của $\mathrm{Ga}$, $\mathrm{Ga}^+$ và $\mathrm{Ga}^-$.

**Hướng đi:**
- Dựa trên quy tắc Klechkowski để điền 31 electron cho nguyên tử trung hòa $\mathrm{Ga}$.
- Với ion dương $\mathrm{Ga}^+$: Bớt 1 electron từ phân lớp ngoài cùng có năng lượng cao nhất.
- Với ion âm $\mathrm{Ga}^-$: Thêm 1 electron vào phân lớp đang điền dở.

**Lời giải chi tiết:**
1. **Nguyên tử gali trung hòa ($\mathrm{Ga}$, $Z = 31$, có 31 electron):**
   - Lõi khí hiếm argon gồm 18 electron: $1s^2 2s^2 2p^6 3s^2 3p^6$.
   - Các electron tiếp theo điền đầy phân lớp $4s$ (2 electron) và phân lớp $3d$ (10 electron).
   - Electron cuối cùng (thứ 31) đi vào phân lớp $4p$:
$$
1s^2 2s^2 2p^6 3s^2 3p^6 3d^{10} 4s^2 4p^1
$$
Dạng thu gọn là $[\mathrm{Ar}]\,3d^{10} 4s^2 4p^1$.

2. **Ion dương $\mathrm{Ga}^+$ (có $31 - 1 = 30$ electron):**
   - Khi nguyên tử bị ion hóa, electron ở phân lớp ngoài cùng có số lượng tử chính lớn nhất ($4p$) và liên kết lỏng lẻo nhất sẽ bị bứt ra đầu tiên:
$$
1s^2 2s^2 2p^6 3s^2 3p^6 3d^{10} 4s^2
$$
Dạng thu gọn là $[\mathrm{Ar}]\,3d^{10} 4s^2$.

3. **Ion âm $\mathrm{Ga}^-$ (có $31 + 1 = 32$ electron):**
   - Electron nhận thêm sẽ đi vào orbital còn trống tiếp theo của phân lớp $4p$ đang điền dở:
$$
1s^2 2s^2 2p^6 3s^2 3p^6 3d^{10} 4s^2 4p^2
$$
Dạng thu gọn là $[\mathrm{Ar}]\,3d^{10} 4s^2 4p^2$.

**Kết luận:**
- $\mathrm{Ga}$: $[\mathrm{Ar}]\,3d^{10} 4s^2 4p^1$
- $\mathrm{Ga}^+$: $[\mathrm{Ar}]\,3d^{10} 4s^2$
- $\mathrm{Ga}^-$: $[\mathrm{Ar}]\,3d^{10} 4s^2 4p^2$
</details>

### Q41.15
Dựa trên nguyên lý loại trừ Pauli, cấu trúc của bảng tuần hoàn các nguyên tố hóa học cho thấy rằng bắt buộc phải có một số lượng tử thứ tư ngoài ba số lượng tử $n$, $l$ và $m_l$. Hãy giải thích.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Chứng minh sự cần thiết phải tồn tại số lượng tử thứ tư ($m_s$) dựa trên chu kỳ và số lượng nguyên tố trong bảng tuần hoàn kết hợp với nguyên lý loại trừ Pauli.

**Hướng đi:**
- Đếm số lượng trạng thái không gian khả dĩ ứng với bộ ba $(n, l, m_l)$.
- So sánh số trạng thái này với số nguyên tố thực tế trong các chu kỳ của bảng tuần hoàn.
- Chỉ ra rằng mỗi trạng thái không gian chứa đúng 2 electron, khẳng định sự tồn tại của số lượng tử thứ tư có đúng 2 giá trị khả dĩ.

**Lời giải chi tiết:**
1. **Đếm số trạng thái không gian với bộ ba $(n, l, m_l)$:**
   - Trong phân tích Schrödinger không kể spin, mỗi trạng thái không gian được xác định trọn vẹn bởi bộ ba $(n, l, m_l)$.
   - Với mỗi số lượng tử chính $n$, số lượng tử quỹ đạo $l$ chạy từ $0$ đến $n-1$, và với mỗi $l$, $m_l$ nhận $2l+1$ giá trị.
   - Tổng số trạng thái không gian khả dĩ cho một lớp vỏ $n$ là:
$$
\sum_{l=0}^{n-1} (2l+1) = n^2
$$
   - Cụ thể:
   - Với $n = 1$: Có $1^2 = 1$ trạng thái không gian (orbital 1s).
   - Với $n = 2$: Có $2^2 = 4$ trạng thái không gian (1 orbital 2s và 3 orbital 2p).

2. **Mâu thuẫn nếu chỉ có ba số lượng tử:**
   - Nếu mỗi electron chỉ được xác định bởi $(n, l, m_l)$, theo nguyên lý loại trừ Pauli, không thể có hai electron cùng trạng thái, nghĩa là mỗi trạng thái không gian chỉ chứa được tối đa **1 electron**:
   - Lớp $n=1$ sẽ bão hòa với 1 electron $\implies$ Chu kỳ 1 chỉ có 1 nguyên tố.
   - Lớp $n=2$ sẽ bão hòa với 4 electron $\implies$ Chu kỳ 2 chỉ có 4 nguyên tố.

3. **Thực tế bảng tuần hoàn:**
   - Trong thực tế:
   - Chu kỳ 1 có **2** nguyên tố (H và He).
   - Chu kỳ 2 có **8** nguyên tố (Li, Be, B, C, N, O, F, Ne).
   - Số nguyên tố thực tế luôn gấp đôi số trạng thái không gian:
$$
N_{\text{electron tối đa}} = 2n^2
$$
   - Điều này đòi hỏi mỗi trạng thái không gian $(n, l, m_l)$ phải chứa được đúng 2 electron phân biệt.

**Kết luận:** Để thỏa mãn nguyên lý loại trừ Pauli, bắt buộc phải tồn tại một số lượng tử nội tại thứ tư (số lượng tử từ spin $m_s$) nhận đúng 2 giá trị khả dĩ ($+1/2$ và $-1/2$).
</details>

### Q41.16
Một lượng tách nhỏ các vạch quang phổ xảy ra ngay cả khi các nguyên tử không nằm trong từ trường ngoài. Hiện tượng này do nguyên nhân nào gây ra?

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Giải thích nguyên nhân gây ra sự tách vạch quang phổ (cấu trúc tinh tế) khi không có từ trường ngoài.

**Hướng đi:**
- Xác định bản chất tương tác spin-quỹ đạo (spin-orbit coupling).
- Đứng trong hệ quy chiếu gắn với electron chuyển động: Hạt nhân mang điện chuyển động tương đối sinh ra từ trường nội tại $\vec{B}_{\mathrm{int}}$.
- Mômen từ spin của electron tương tác với chính từ trường nội tại này.

**Lời giải chi tiết:**
1. **Nguồn gốc từ trường nội tại của nguyên tử:**
   - Trong hệ quy chiếu của hạt nhân, electron mang điện tích âm chuyển động quanh hạt nhân.
   - Nhưng khi chuyển sang hệ quy chiếu gắn với chính electron, hạt nhân mang điện tích dương $+Ze$ chuyển động tương đối xung quanh electron.
   - Dòng điện sinh ra do chuyển động tương đối này của hạt nhân tạo ra một **từ trường nội tại** mạnh $\vec{B}_{\mathrm{int}}$ ngay tại vị trí của electron. Từ trường này tỉ lệ thuận với mômen động lượng quỹ đạo $\vec{L}$ của electron:
$$
\vec{B}_{\mathrm{int}} \propto \vec{L}
$$

2. **Năng lượng tương tác spin-quỹ đạo:**
   - Bản thân electron sở hữu một mômen từ spin nội tại $\vec{\mu}_s$.
   - Mômen từ spin $\vec{\mu}_s$ sẽ tương tác với từ trường nội tại $\vec{B}_{\mathrm{int}}$ thông qua thế năng tương tác:
$$
U_{\mathrm{SO}} = -\vec{\mu}_s \cdot \vec{B}_{\mathrm{int}} \propto \vec{S} \cdot \vec{L}
$$
   - Năng lượng này phụ thuộc vào hướng tương đối giữa vector spin $\vec{S}$ và vector mômen động lượng quỹ đạo $\vec{L}$ (được đặc trưng bởi số lượng tử mômen động lượng toàn phần $\vec{J} = \vec{L} + \vec{S}$ với $j = l \pm 1/2$).

3. **Hệ quả tách vạch quang phổ:**
   - Một mức năng lượng ứng với $l > 0$ ban đầu bị suy biến sẽ bị tách thành hai phân mức có giá trị $j$ khác nhau (gọi là cấu trúc tinh tế - fine structure).
   - Sự chuyển dời giữa các phân mức này sinh ra các vạch phổ kép (chẳng hạn vạch đôi màu vàng của natri 589{,}0 nm và 589{,}6 nm) ngay cả khi không có bất kỳ từ trường ngoài nào can thiệp.

**Kết luận:** Hiện tượng tách vạch khi không có từ trường ngoài sinh ra do tương tác spin-quỹ đạo giữa mômen từ spin của electron và từ trường nội tại tạo bởi chuyển động quỹ đạo tương đối của hạt nhân.
</details>

### Q41.17
Năng lượng ion hóa của các kim loại kiềm (năng lượng tối thiểu để bứt một electron ngoài cùng khi nguyên tử ở trạng thái cơ bản) vào khoảng 4 đến 5 eV, trong khi năng lượng ion hóa của các khí hiếm lại nằm trong khoảng từ 11 đến 25 eV. Tại sao lại có sự chênh lệch lớn như vậy?

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- So sánh năng lượng ion hóa của kim loại kiềm ($4 - 5\,\mathrm{eV}$) và khí hiếm ($11 - 25\,\mathrm{eV}$).
- Giải thích cơ chế vật lý dẫn đến sự khác biệt lớn này.

**Hướng đi:**
- Phân tích cấu hình electron của kim loại kiềm ($[\text{khí hiếm}]\,ns^1$) và khí hiếm ($ns^2 np^6$).
- So sánh điện tích hạt nhân hiệu dụng $Z_{\mathrm{eff}}$ và bán kính orbital của electron ngoài cùng.
- Phân tích tính bền vững của lớp vỏ bão hòa (closed shell).

**Lời giải chi tiết:**
1. **Đối với kim loại kiềm:**
   - Cấu hình electron ngoài cùng là $ns^1$.
   - Electron hóa trị duy nhất này nằm ở lớp vỏ mới ($n$), có bán kính trung bình lớn nhất so với các electron còn lại.
   - Lõi electron bên trong có cấu hình khí hiếm khép kín gồm $Z-1$ electron, chắn gần như hoàn toàn điện tích hạt nhân đối với electron ngoài cùng:
$$
Z_{\mathrm{eff}} \approx Z - (Z - 1) = 1
$$
   - Electron hóa trị ở xa hạt nhân và chỉ cảm nhận điện tích hiệu dụng xấp xỉ $+1e$, nên lực hút tĩnh điện rất yếu, dẫn đến năng lượng liên kết nhỏ (chỉ cần $4 - 5\,\mathrm{eV}$ để bứt electron ra).

2. **Đối với khí hiếm:**
   - Cấu hình electron ngoài cùng là $ns^2 np^6$ (hoặc $1s^2$ đối với He), tạo thành một lớp vỏ khép kín bão hòa hoàn hảo.
   - Trong cùng một chu kỳ, điện tích hạt nhân $Z$ đạt cực đại ở khí hiếm, trong khi các electron đang được điền vào cùng một lớp vỏ $n$. Các electron trong cùng một lớp chắn lẫn nhau rất kém.
   - Do đó, điện tích hạt nhân hiệu dụng $Z_{\mathrm{eff}}$ mà electron ngoài cùng của khí hiếm cảm nhận là rất lớn ($Z_{\mathrm{eff}} \gg 1$).
   - Điện tích hiệu dụng lớn kéo đám mây electron co lại gần hạt nhân, làm bán kính nguyên tử nhỏ nhất trong chu kỳ và lực hút tĩnh điện cực mạnh, đòi hỏi năng lượng rất lớn ($11 - 25\,\mathrm{eV}$) mới có thể bứt được một electron.

**Kết luận:** Sự khác biệt vượt bậc về điện tích hạt nhân hiệu dụng $Z_{\mathrm{eff}}$, bán kính nguyên tử và độ bền cấu trúc của lớp vỏ electron khép kín là nguyên nhân khiến năng lượng ion hóa của khí hiếm cao gấp nhiều lần kim loại kiềm.
</details>

### Q41.18
Đối với magie, thế ion hóa thứ nhất là 7,6 eV. Thế ion hóa thứ hai (năng lượng bổ sung cần thiết để bứt electron thứ hai) gần như gấp đôi giá trị này, đạt 15 eV, và thế ion hóa thứ ba lớn hơn rất nhiều, vào khoảng 80 eV. Làm thế nào để hiểu được các con số này?

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Magie ($Z=12$): $I_1 = 7{,}6\,\mathrm{eV}$, $I_2 = 15\,\mathrm{eV}$, $I_3 \approx 80\,\mathrm{eV}$.
- Giải thích sự gia tăng của từng thế ion hóa dựa trên cấu hình electron và điện tích ion.

**Hướng đi:**
- Viết cấu hình electron của magie: $\mathrm{Mg}$ ($Z=12$): $1s^2 2s^2 2p^6 3s^2$.
- Phân tích quá trình bứt electron thứ nhất ($3s$ từ nguyên tử trung hòa $\mathrm{Mg}$).
- Phân tích quá trình bứt electron thứ hai ($3s$ từ ion dương $\mathrm{Mg}^+$).
- Phân tích quá trình bứt electron thứ ba ($2p$ từ ion $\mathrm{Mg}^{2+}$ có cấu hình khí hiếm neon bền vững).

**Lời giải chi tiết:**
1. **Thế ion hóa thứ nhất ($I_1 = 7{,}6\,\mathrm{eV}$):**
   - Quá trình ion hóa thứ nhất:
$$
\mathrm{Mg} \to \mathrm{Mg}^+ + e^-
$$
   - Bứt một electron từ phân lớp $3s$ của nguyên tử trung hòa. Electron này bị 10 electron lõi ($1s^2 2s^2 2p^6$) chắn mạnh và chịu thêm lực đẩy từ electron $3s$ còn lại, nên điện tích hiệu dụng cảm nhận nhỏ ($Z_{\mathrm{eff}} \approx 2 - 3$), năng lượng liên kết ở mức vừa phải ($7{,}6\,\mathrm{eV}$).

2. **Thế ion hóa thứ hai ($I_2 = 15\,\mathrm{eV} \approx 2 I_1$):**
   - Quá trình ion hóa thứ hai:
$$
\mathrm{Mg}^+ \to \mathrm{Mg}^{2+} + e^-
$$
   - Bứt electron $3s$ thứ hai từ một **ion mang điện tích dương $+1e$**.
   - Không còn electron $3s$ nào khác đẩy chắn nó. Hạt nhân $+12e$ giờ đây hút 11 electron còn lại chặt hơn, đám mây electron co lại khiến bán kính nhỏ đi.
   - Do phải bứt một electron âm ra khỏi một thực thể đã tích điện dương, thế năng Coulomb tăng xấp xỉ gấp đôi so với khi bứt từ nguyên tử trung hòa, làm $I_2 \approx 15\,\mathrm{eV}$.

3. **Thế ion hóa thứ ba ($I_3 \approx 80\,\mathrm{eV} \gg I_2$):**
   - Quá trình ion hóa thứ ba:
$$
\mathrm{Mg}^{2+} \to \mathrm{Mg}^{3+} + e^-
$$
   - Ion $\mathrm{Mg}^{2+}$ có cấu hình $1s^2 2s^2 2p^6$, là cấu hình vỏ khép kín bền của khí hiếm neon.
   - Electron thứ ba bị bứt ra không còn ở lớp ngoài $n=3$ mà nằm ở lớp trong **$n=2$** (phân lớp $2p$).
   - Lớp $n=2$ có bán kính nhỏ hơn rất nhiều so với lớp $n=3$, và chỉ bị chắn bởi 2 electron lớp $1s$. Do đó, điện tích hạt nhân hiệu dụng tăng vọt ($Z_{\mathrm{eff}} \approx 12 - 2 = 10$).
   - Việc phá vỡ lớp vỏ khí hiếm bên trong dưới lực hút mãnh liệt của hạt nhân đòi hỏi năng lượng nhảy vọt hơn 5 lần, lên tới xấp xỉ $80\,\mathrm{eV}$.

**Kết luận:** $I_1$ và $I_2$ tương ứng với việc bứt hai electron hóa trị ở lớp $3s$, trong khi $I_3$ tăng vọt do phải phá vỡ lớp vỏ khép kín $2p$ ở lớp lượng tử chính bên trong ($n=2$).
</details>

### Q41.19
"Gần đúng trường xuyên tâm" là gì và tại sao nó chỉ là một phép gần đúng?

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Nêu gần đúng trường xuyên tâm và giải thích giới hạn của nó.

**Hướng đi:**

- Thay tác dụng của các electron khác bằng trường trung bình để đưa bài toán nhiều electron về những bài toán một electron.
- Giữ sự phụ thuộc bán kính, nhưng kiểm tra những thông tin về vị trí tương đối đã bị bỏ qua.

Trong gần đúng trường xuyên tâm, mỗi electron được mô tả bằng một hàm sóng một hạt trong thế hiệu dụng $U_{\rm eff}(r)$. Thế này gồm lực hút hạt nhân và tác dụng trung bình của các electron khác, được lấy đối xứng cầu.

Nhờ vậy, phần góc và phần bán kính có thể tách như trong bài toán hydro. Các trạng thái được gắn nhãn bằng $n,\ell,m_\ell,m_s$, nhưng năng lượng còn phụ thuộc mức độ che chắn và thâm nhập.

Đây chỉ là gần đúng vì lực đẩy thực tế phụ thuộc các khoảng cách tức thời giữa từng cặp electron. Chuyển động của chúng có tương quan. Một thế trung bình theo bán kính không giữ hết các tương quan ấy, các chi tiết phụ thuộc góc và hiệu ứng trao đổi của hệ nhiều electron.

Một phân lớp đầy có phân bố trung bình đối xứng cầu, nhưng đó không phải điều kiện cần duy nhất để một trạng thái hay một tập hợp nguyên tử có mật độ cầu. Ngay cả khi mật độ trung bình có đối xứng cầu, việc thay tương tác nhiều hạt bằng các bài toán độc lập vẫn là một xấp xỉ.

</details>

### Q41.20
Hạt nhân của một nguyên tử vàng chứa 79 proton. Năng lượng cần thiết để bứt hoàn toàn một electron 1s ra khỏi nguyên tử vàng so với năng lượng cần thiết để bứt electron khỏi mức cơ bản trong nguyên tử hydro như thế nào? Một photon có năng lượng tương ứng cho mỗi nguyên tử này sẽ nằm trong vùng nào của thang sóng điện từ?

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Vàng ($\mathrm{Au}$, $Z = 79$): Xét electron 1s.
- Hydro ($\mathrm{H}$, $Z = 1$): Xét electron 1s.
- So sánh năng lượng bứt electron và xác định vùng quang phổ của photon tương ứng.

**Hướng đi:**
- Dùng mô hình Bohr/Schrödinger với hiệu ứng chắn của electron 1s còn lại: $Z_{\mathrm{eff}} \approx Z - 1$.
- Tính năng lượng bứt electron 1s của vàng:
$$
\begin{aligned}
&E_{1s}(\mathrm{Au}) \approx (Z-1)^2 E_H, \\
&E_H = 13{,}6\,\mathrm{eV}.
\end{aligned}
$$
- So sánh với năng lượng ion hóa của hydro ($13{,}6\,\mathrm{eV}$).
- Xác định dải sóng điện từ (tử ngoại UV, tia X).

**Lời giải chi tiết:**
1. **Tính toán năng lượng bứt electron:**
   - Đối với nguyên tử hydro ($Z=1$): Năng lượng ion hóa từ trạng thái cơ bản 1s là:
$$
E_H = 13{,}6\,\mathrm{eV}
$$
   - Đối với nguyên tử vàng ($Z=79$): Electron ở lớp 1s chuyển động rất gần hạt nhân, bên trong tất cả các lớp electron khác. Nó chỉ bị chắn một phần nhỏ bởi electron 1s thứ hai cùng lớp, do đó điện tích hạt nhân hiệu dụng xấp xỉ:
$$
Z_{\mathrm{eff}} \approx Z - 1 = 79 - 1 = 78
$$
   - Năng lượng liên kết của electron 1s trong vàng xấp xỉ:
$$
\begin{aligned}
E_{\mathrm{Au}} &\approx 78^2 \times 13{,}6\,\mathrm{eV} \\
&\approx 82{,}7\,\mathrm{keV}
\end{aligned}
$$
   - So sánh tỷ số năng lượng:
$$
\begin{aligned}
\frac{E_{\mathrm{Au}}}{E_H} &\approx 78^2 = 6084 \\
&\approx 6 \times 10^3
\end{aligned}
$$
Năng lượng bứt electron 1s của vàng lớn hơn khoảng 6000 lần so với hydro (thực nghiệm đo được tại bờ hấp thụ K của vàng là $80{,}7\,\mathrm{keV}$, rất sát với ước lượng).

2. **Xác định vùng phổ điện từ:**
   - Với photon năng lượng $E_H = 13{,}6\,\mathrm{eV}$:
$$
\begin{aligned}
\lambda_H &= \frac{hc}{E_H} \\
&\approx \frac{1240\,\mathrm{eV\cdot nm}}{13{,}6\,\mathrm{eV}} \\
&\approx 91{,}2\,\mathrm{nm}
\end{aligned}
$$
Bước sóng này nằm trong **vùng tử ngoại chân không (vacuum ultraviolet - UV)**.
   - Với photon năng lượng tia X $E_{\text{Au}} \approx 83\,\mathrm{keV}$:
$$
\begin{aligned}
\lambda_{\mathrm{Au}} &= \frac{hc}{E_{\mathrm{Au}}} \\
&\approx \frac{1{,}240 \times 10^3\,\mathrm{eV\cdot pm}}{82{,}7\,\mathrm{keV}} \\
&\approx 15\,\mathrm{pm}
\end{aligned}
$$
Bước sóng này cực ngắn, nằm sâu trong **vùng tia X cứng (hard X-rays)** / ranh giới tia gamma năng lượng thấp.

**Kết luận:** Năng lượng bứt electron 1s của vàng lớn hơn nguyên tử hydro khoảng 6000 lần. Photon của hydro thuộc vùng tử ngoại, trong khi photon của vàng thuộc vùng tia X cứng.
</details>

### Q41.21
(a) Bạn có thể chứng minh rằng mômen động lượng quỹ đạo của electron theo bất kỳ phương cho trước nào (chẳng hạn dọc theo trục $z$) luôn nhỏ hơn hoặc bằng độ lớn mômen động lượng quỹ đạo toàn phần của nó không? Trong trường hợp nào thì hai đại lượng này bằng nhau?

(b) Kết quả ở phần (a) có đúng đối với một vật thể cổ điển, chẳng hạn một con quay hay một hành tinh không?

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- (a) Chứng minh $|L_z| \le L$ trong cơ học lượng tử. Xác định điều kiện dấu bằng.
- (b) Đánh giá tính đúng đắn của kết luận này đối với vật thể cổ điển.

**Hướng đi:**
- Trong cơ học lượng tử, sử dụng công thức lượng tử hóa:
$$
\begin{aligned}
&L = \sqrt{l(l+1)}\,\hbar, \\
&L_z = m_l\hbar \quad (-l \le m_l \le l).
\end{aligned}
$$
- So sánh $m_l^2$ và $l(l+1)$.
- Đối với vật thể cổ điển, xét trường hợp trục quay trùng với trục $z$.

**Lời giải chi tiết:**
1. **Phần (a): Chứng minh trong cơ học lượng tử**
   - Độ lớn của mômen động lượng quỹ đạo toàn phần là:
$$
L = \sqrt{l(l+1)}\,\hbar
$$
   - Thành phần của mômen động lượng quỹ đạo dọc theo trục $z$ là:
$$
\begin{aligned}
&L_z = m_l\hbar, \\
&m_l \in \{-l, \dots, +l\}.
\end{aligned}
$$
   - Giá trị tuyệt đối lớn nhất của $L_z$ đạt được khi $|m_l| = l$:
$$
|L_z|_{\max} = l\hbar
$$
   - Đặt hiệu bình phương $\Delta L^2 = L^2 - |L_z|_{\max}^2$, ta có:
$$
\begin{aligned}
\Delta L^2 &= l(l+1)\hbar^2 - l^2\hbar^2 \\
&= l\hbar^2 \ge 0
\end{aligned}
$$
   - Do đó, với mọi trạng thái lượng tử:
$$
|L_z| \le L
$$
   - **Xét điều kiện dấu bằng ($|L_z| = L$):**
   - Dấu bằng xảy ra khi và chỉ khi $l\hbar^2 = 0 \iff l = 0$.
   - Khi $l = 0$, ta có $L = 0$ và $m_l = 0 \implies L_z = 0$. Cả hai đại lượng đều đồng thời bằng 0.
   - Với mọi trạng thái có $l > 0$, vì $l < \sqrt{l(l+1)}$ nên $|L_z|$ **luôn luôn nhỏ hơn ngặt** so với $L$ ($|L_z| < L$).
   - Với $l>0$, không thể đồng thời có hai thành phần ngang xác định bằng không và thành phần $L_z$ khác không. Quan hệ giao hoán $[L_x,L_y]=i\hbar L_z$ thể hiện giới hạn ấy. Trường hợp $l=0$ có mômen động lượng bằng không, nên không có hướng vector để xét.

2. **Phần (b): Đối với vật thể cổ điển**
   - Đối với một vật thể cơ học cổ điển (như con quay hoặc hành tinh), vector mômen động lượng $\vec{L} = (L_x, L_y, L_z)$ có độ lớn $L = \sqrt{L_x^2 + L_y^2 + L_z^2}$.
   - Rõ ràng bất đẳng thức $|L_z| \le L$ vẫn luôn đúng về mặt hình học giải tích.
   - **Tuy nhiên, điểm khác biệt then chốt là khả năng xảy ra dấu bằng khi $L \ne 0$:**
   - Trong cơ học cổ điển, không có nguyên lý bất định hạn chế các thành phần của vector. Một vật thể hoàn toàn có thể quay thuần túy quanh trục $z$ ($L_x = 0, L_y = 0$).
   - Khi đó, $|L_z| = L > 0$. Kết luận "vector không thể trùng với trục tọa độ khi $L \ne 0$" của cơ học lượng tử **không áp dụng** cho vật thể cổ điển.

**Kết luận:** Trong cơ học lượng tử, $|L_z| = L$ chỉ xảy ra khi cả hai cùng bằng $0$. Đối với vật thể cổ điển, $|L_z| = L$ có thể xảy ra ở bất kỳ giá trị năng lượng nào khi trục quay của vật trùng với trục $z$.
</details>

### Q41.22
Một nguyên tử ở trạng thái cơ bản hấp thụ một photon có năng lượng đúng bằng bờ hấp thụ K (K absorption edge). Việc hấp thụ photon này có làm ion hóa nguyên tử không? Hãy giải thích.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Nguyên tử hấp thụ photon có năng lượng $h\nu = E_{\text{bờ } K}$.
- Câu hỏi: Quá trình này có làm ion hóa nguyên tử hay không? Giải thích.

**Hướng đi:**
- Nêu định nghĩa vật lý của "bờ hấp thụ K" (K absorption edge).
- Xác định trạng thái ban đầu của electron bị kích thích (lớp K, $n=1$).
- Xác định trạng thái cuối cùng của electron sau khi hấp thụ photon năng lượng ngưỡng này.

**Lời giải chi tiết:**
1. **Định nghĩa bờ hấp thụ K:**
   - Lớp K là lớp vỏ electron trong cùng gần hạt nhân nhất ($n=1$).
   - Bờ hấp thụ K được định nghĩa là **năng lượng photon tối thiểu** cần thiết để đánh bật hoàn toàn một electron từ lớp K ($n=1$) thoát khỏi lực hút liên kết của nguyên tử ra xa vô cực với động năng bằng không ($E_{\text{cuối}} = 0$ ở vùng phổ liên tục).

2. **Phân tích quá trình ion hóa:**
   - Trước khi hấp thụ photon, electron nằm ở trạng thái liên kết sâu trong lớp K với năng lượng $E_K < 0$.
   - Khi nguyên tử hấp thụ photon có năng lượng đúng bằng $h\nu = |E_K|$:
$$
\begin{aligned}
E_{\text{cuối}} &= E_K + h\nu \\
&= -|E_K| + |E_K| = 0
\end{aligned}
$$
   - Năng lượng này vừa đủ để electron lớp K bứt hoàn toàn ra khỏi nguyên tử và trở thành một electron tự do.
   - Nguyên tử ban đầu trung hòa nay mất đi một electron, trở thành một ion dương với một lỗ trống ở lớp vỏ K:
$$
\mathrm{X} + h\nu_K \to \mathrm{X}^+ + e^-
$$

**Kết luận:** Khi bờ K được hiểu là ngưỡng ion hóa của lớp K, hấp thụ photon tại ngưỡng này làm ion hóa nguyên tử. Cần phân biệt ngưỡng ấy với một vạch kích thích electron K lên trạng thái liên kết còn trống. Quá trình thứ hai chưa nhất thiết làm electron rời nguyên tử.
</details>

### Q41.23
Liệu nguyên tử hydro có thể phát ra tia X không? Nếu có thì bằng cách nào? Nếu không thì tại sao?

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Đánh giá khả năng phát tia X của nguyên tử hydro.
- Nêu rõ cơ chế vật lý khả thi hoặc giới hạn lý thuyết.

**Hướng đi:**
- Xác định dải năng lượng đặc trưng của photon tia X ($100\,\mathrm{eV}$ đến hàng trăm $\mathrm{keV}$).
- Tính năng lượng chuyển mức electron lớn nhất trong nguyên tử hydro liên kết: $\Delta E_{\max} = 13{,}6\,\mathrm{eV}$.
- Phân tích các quá trình khác có thể sinh ra tia X từ hệ hạt hydro (bức xạ hãm Bremsstrahlung và tái hợp electron năng lượng cao).

**Lời giải chi tiết:**
1. **Xét quá trình chuyển mức electron liên kết thông thường:**
   - Năng lượng của các trạng thái dừng trong nguyên tử hydro với $n = 1, 2, 3, \dots$:
$$
E_n = -\frac{13{,}6\,\mathrm{eV}}{n^2}
$$
   - Độ chênh lệch năng lượng lớn nhất giữa hai trạng thái bất kỳ là khi electron chuyển từ trạng thái ion hóa ($n \to \infty, E=0$) về trạng thái cơ bản ($n=1$):
$$
\begin{aligned}
\Delta E_{\max} &= E_\infty - E_1 \\
&= 13{,}6\,\mathrm{eV}
\end{aligned}
$$
   - Bước sóng ngắn nhất tương ứng trong phổ vạch hydro (giới hạn dãy Lyman) là:
$$
\lambda_{\min} = \frac{hc}{\Delta E_{\max}} \approx 91{,}2\,\mathrm{nm}
$$
   - Bức xạ này nằm ở vùng **tử ngoại chân không (vacuum UV)**, hoàn toàn chưa đạt tới ngưỡng năng lượng của tia X (tia X thường có năng lượng photon từ khoảng $100\,\mathrm{eV}$ trở lên, tương ứng bước sóng dưới $10\,\mathrm{nm}$). Do đó, hydro **không thể phát tia X đặc trưng thông qua các chuyển mức quang phổ electron liên kết**.

2. **Cách để nguyên tử hydro phát ra tia X:**
   - Hydro vẫn có thể tạo ra photon tia X thông qua các tương tác tán xạ năng lượng cao:
   - **Bức xạ hãm (Bremsstrahlung):** Nếu bắn một chùm electron tự do có động năng lớn (ví dụ $E_k \ge 1\,\mathrm{keV}$) vào chất khí hydro, khi electron bay qua gần hạt nhân proton, lực tĩnh điện Coulomb mạnh của hạt nhân sẽ làm electron bị lệch hướng và giảm tốc đột ngột. Sự giảm tốc này làm electron phát ra bức xạ hãm có phổ liên tục thuộc dải tia X.
   - **Bức xạ tái hợp electron năng lượng cao:** Nếu một electron tự do có động năng ban đầu lớn $K_e \ge 100\,\mathrm{eV}$ bị một proton bắt giữ trực tiếp vào trạng thái cơ bản $n=1$, photon phát ra sẽ mang năng lượng:
$$
\begin{aligned}
h\nu &= K_e + 13{,}6\,\mathrm{eV} \\
&\ge 113{,}6\,\mathrm{eV}
\end{aligned}
$$
Photon này có năng lượng nằm trong dải tia X mềm.

**Kết luận:** Nguyên tử hydro cô lập không thể phát tia X qua chuyển mức quang phổ thông thường vì năng lượng liên kết tối đa chỉ là $13{,}6\,\mathrm{eV}$. Tuy nhiên, hydro có thể phát tia X nếu có chùm electron tự do năng lượng cao tương tác với hạt nhân proton thông qua bức xạ hãm hoặc quá trình bắt giữ electron.
</details>

### Q41.24
Một hệ gồm hai electron có hàm sóng:
$$
\begin{aligned}
&\psi(\vec{r}_1, \vec{r}_2) = \frac{1}{\sqrt{2}}(\psi_A - \psi_B), \\
&\psi_A = \psi_\alpha(\vec{r}_1)\psi_\beta(\vec{r}_2), \\
&\psi_B = \psi_\beta(\vec{r}_1)\psi_\alpha(\vec{r}_2)
\end{aligned}
$$
trong đó $\psi_\alpha$ là hàm sóng đã chuẩn hóa cho một trạng thái có $S_z = +\frac{1}{2}\hbar$ và $\psi_\beta$ là hàm sóng đã chuẩn hóa cho một trạng thái có $S_z = -\frac{1}{2}\hbar$.

(a) Nếu đo $S_z$ của electron 1, những kết quả nào có thể thu được? Xác suất của mỗi kết quả là bao nhiêu?

(b) Nếu đo $S_z$ của electron 2, những kết quả nào có thể thu được? Xác suất của mỗi kết quả là bao nhiêu?

(c) Nếu phép đo $S_z$ của electron 1 cho giá trị $+\frac{1}{2}\hbar$, những kết quả nào có thể thu được trong phép đo tiếp theo của $S_z$ đối với electron 2? Xác suất thu được mỗi kết quả là bao nhiêu? Hãy giải thích.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Trạng thái hai electron:
$$
\begin{aligned}
&\psi(\vec{r}_1, \vec{r}_2) = \frac{1}{\sqrt{2}}(\psi_A - \psi_B), \\
&\psi_A = \psi_\alpha(\vec{r}_1)\psi_\beta(\vec{r}_2), \\
&\psi_B = \psi_\beta(\vec{r}_1)\psi_\alpha(\vec{r}_2).
\end{aligned}
$$
- Trạng thái $\alpha$: $S_z = +\frac{1}{2}\hbar$; trạng thái $\beta$: $S_z = -\frac{1}{2}\hbar$.
- (a) Đo $S_z$ của electron 1: Các giá trị và xác suất?
- (b) Đo $S_z$ của electron 2: Các giá trị và xác suất?
- (c) Nếu electron 1 đo ra $+\frac{1}{2}\hbar$, đo tiếp electron 2 thu được gì và xác suất bao nhiêu?

**Hướng đi:**
- Nhận dạng hàm sóng: Đây là một trạng thái vướng víu lượng tử phản đối xứng (spin-singlet).
- Khai triển trạng thái theo hệ cơ sở riêng của electron 1 và electron 2 để tìm xác suất tiên nghiệm.
- Áp dụng tiên đề suy sụp hàm sóng (wave function collapse) của phép đo cơ học lượng tử để tìm xác suất hậu đo cho electron 2.

**Lời giải chi tiết:**
1. **Phần (a): Đo $S_z$ của electron 1**
   - Hàm sóng của hệ có thể viết dưới dạng tách theo trạng thái spin của electron 1:
$$
\begin{aligned}
&\psi(\vec{r}_1, \vec{r}_2) = \frac{\psi_A}{\sqrt{2}} - \frac{\psi_B}{\sqrt{2}}, \\
&\psi_A = \psi_\alpha(\vec{r}_1)\psi_\beta(\vec{r}_2), \\
&\psi_B = \psi_\beta(\vec{r}_1)\psi_\alpha(\vec{r}_2).
\end{aligned}
$$
   - Số hạng thứ nhất tương ứng với electron 1 ở trạng thái $\psi_\alpha$ (có $S_{z,1} = +\frac{1}{2}\hbar$). Xác suất đo được giá trị này là:
$$
\begin{aligned}
P(S_{z,1} = +\tfrac{1}{2}\hbar) &= \left|\frac{1}{\sqrt{2}}\right|^2 \\
&= 50\%
\end{aligned}
$$
   - Số hạng thứ hai tương ứng với electron 1 ở trạng thái $\psi_\beta$ (có $S_{z,1} = -\frac{1}{2}\hbar$). Xác suất đo được giá trị này là:
$$
\begin{aligned}
P(S_{z,1} = -\tfrac{1}{2}\hbar) &= \left|-\frac{1}{\sqrt{2}}\right|^2 \\
&= 50\%
\end{aligned}
$$
   - Không thể thu được bất kỳ giá trị nào khác.

2. **Phần (b): Đo $S_z$ của electron 2**
   - Nhìn vào hàm sóng đối với electron 2:
   - Khi electron 2 ở trạng thái $\psi_\beta$ ($S_{z,2} = -\frac{1}{2}\hbar$), biên độ là $\frac{1}{\sqrt{2}} \implies$ Xác suất là $50\%$.
   - Khi electron 2 ở trạng thái $\psi_\alpha$ ($S_{z,2} = +\frac{1}{2}\hbar$), biên độ là $-\frac{1}{\sqrt{2}} \implies$ Xác suất là $50\%$.
   - Do đó, nếu thực hiện phép đo trên electron 2 khi chưa đo electron 1, kết quả có thể là:
$$
P(S_{z,2} = +\tfrac{1}{2}\hbar) = 50\%
$$
$$
P(S_{z,2} = -\tfrac{1}{2}\hbar) = 50\%
$$

3. **Phần (c): Đo electron 2 sau khi electron 1 cho kết quả $+\frac{1}{2}\hbar$**
   - Theo tiên đề phép đo cơ học lượng tử (suy sụp hàm sóng): Khi phép đo $S_z$ trên electron 1 cho kết quả $+\frac{1}{2}\hbar$, toàn bộ hàm sóng của hệ lập tức suy sụp về trạng thái riêng tương ứng với kết quả đo này.
   - Nhánh chứa trạng thái spin xuống của electron 1 bị triệt tiêu hoàn toàn. Hàm sóng của hệ sau phép đo trở thành:
$$
\psi_{\text{sau}}(\vec{r}_1, \vec{r}_2) = \psi_\alpha(\vec{r}_1)\psi_\beta(\vec{r}_2)
$$
   - Trong trạng thái mới này, electron 2 hoàn toàn và chắc chắn nằm ở trạng thái $\psi_\beta$, vốn có $S_{z,2} = -\frac{1}{2}\hbar$.
   - Do đó, phép đo tiếp theo của $S_z$ trên electron 2 sẽ cho:
$$
P(S_{z,2} = -\tfrac{1}{2}\hbar) = 100\%
$$
$$
P(S_{z,2} = +\tfrac{1}{2}\hbar) = 0\%
$$

**Kết luận:** Trạng thái cho trước là trạng thái vướng víu lượng tử có tương quan đối nghịch hoàn hảo: Phép đo trên một electron lập tức xác định kết quả đo đối nghịch của electron còn lại.
</details>

### Q41.25
Lặp lại Câu hỏi thảo luận Q41.24 cho hàm sóng:
$$
\psi(\vec{r}_1, \vec{r}_2) = \psi_\alpha(\vec{r}_1) \psi_\alpha(\vec{r}_2)
$$

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Trạng thái hai electron:
$$
\psi(\vec{r}_1, \vec{r}_2) = \psi_\alpha(\vec{r}_1) \psi_\alpha(\vec{r}_2)
$$
- Cả hai hạt đều được mô tả bởi trạng thái $\psi_\alpha$ có $S_z = +\frac{1}{2}\hbar$.
- Trả lời các câu hỏi (a), (b), (c) tương tự Q41.24.

**Hướng đi:**
- Nhận dạng cấu trúc hàm sóng: Đây là một trạng thái tích độc lập (separable product state), không vướng víu.
- Xác định trạng thái spin của từng electron độc lập.
- Nêu lưu ý quan trọng về nguyên lý loại trừ Pauli đối với hai fermion đồng nhất.

**Lời giải chi tiết:**
1. **Phần (a): Đo $S_z$ của electron 1**
   - Hàm sóng của hệ có dạng tích tách biệt:
$$
\psi(\vec{r}_1, \vec{r}_2) = \psi_\alpha(\vec{r}_1) \psi_\alpha(\vec{r}_2)
$$
   - Electron 1 đang ở trạng thái dừng $\psi_\alpha(\vec{r}_1)$, vốn là một trạng thái riêng xác định của toán tử $\hat{S}_z$ với giá trị riêng $+\frac{1}{2}\hbar$.
   - Do đó, kết quả duy nhất có thể thu được khi đo $S_z$ của electron 1 là $S_{z,1} = +\frac{1}{2}\hbar$ với xác suất tuyệt đối:
$$
P(S_{z,1} = +\tfrac{1}{2}\hbar) = 100\%
$$
   - Xác suất đo được $-\frac{1}{2}\hbar$ là $0\%$.

2. **Phần (b): Đo $S_z$ của electron 2**
   - Tương tự như electron 1, electron 2 cũng đang ở trạng thái riêng $\psi_\alpha(\vec{r}_2)$ với $S_z = +\frac{1}{2}\hbar$.
   - Kết quả duy nhất có thể thu được khi đo $S_z$ của electron 2 là $S_{z,2} = +\frac{1}{2}\hbar$ với xác suất tuyệt đối:
$$
P(S_{z,2} = +\tfrac{1}{2}\hbar) = 100\%
$$
   - Xác suất đo được $-\frac{1}{2}\hbar$ là $0\%$.

3. **Phần (c): Đo electron 2 sau khi electron 1 cho kết quả $+\frac{1}{2}\hbar$**
   - Vì hàm sóng ban đầu là một trạng thái tích tách biệt không vướng víu, phép đo trên electron 1 không làm thay đổi trạng thái lượng tử của electron 2.
   - Electron 2 vẫn giữ nguyên trạng thái $\psi_\alpha(\vec{r}_2)$.
   - Do đó, phép đo tiếp theo trên electron 2 chắc chắn cho kết quả:
$$
P(S_{z,2} = +\tfrac{1}{2}\hbar) = 100\%
$$
$$
P(S_{z,2} = -\tfrac{1}{2}\hbar) = 0\%
$$

4. **Lưu ý sư phạm quan trọng về nguyên lý loại trừ Pauli:**
   - Về mặt bản chất vật lý lượng tử, electron là fermion đồng nhất, hàm sóng toàn phần bắt buộc phải phản đối xứng đối với phép hoán vị hạt:
$$
\psi(\vec{r}_1, \vec{r}_2) = -\psi(\vec{r}_2, \vec{r}_1)
$$
   - Hàm sóng tích:
$$
\psi = \psi_\alpha(\vec{r}_1) \psi_\alpha(\vec{r}_2)
$$
là đối xứng hoàn toàn đối với phép hoán vị hạt.
   - Do đó, nếu $\psi_\alpha$ đại diện cho toàn bộ trạng thái không gian và spin, thì trạng thái này **vi phạm nguyên lý loại trừ Pauli** và không thể tồn tại trong tự nhiên đối với hai electron đồng nhất (hai electron không thể cùng ở chung một trạng thái lượng tử toàn phần).
   - Để trạng thái này có thể tồn tại về mặt vật lý, $\psi_\alpha(\vec{r})$ trong công thức chỉ có thể là hàm sóng spin, và phần hàm sóng không gian đi kèm bắt buộc phải là một hàm phản đối xứng để tích toàn phần thỏa mãn tính phản đối xứng fermion.

**Kết luận:** Cả hai electron đều độc lập ở trạng thái spin lên, mọi phép đo $S_z$ trên mỗi electron đều cho kết quả $+\frac{1}{2}\hbar$ với xác suất tuyệt đối $100\%$.
</details>
