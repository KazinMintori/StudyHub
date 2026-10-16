## 41.5 Spin của electron

Mô hình phương trình Schrödinger giải thích thành công quang phổ nguyên tử hydro và cấu trúc của các trạng thái dừng thông qua ba số lượng tử: Số lượng tử chính $n$, số lượng tử obitan $l$, và số lượng tử từ obitan $m_l$. Tuy nhiên, khi các nhà thực nghiệm quan sát quang phổ với độ phân giải cao và đặt nguyên tử trong từ trường, nhiều hiện tượng bất thường đã xuất hiện mà ba số lượng tử này hoàn toàn không thể giải thích được.

Năm 1925, hai nghiên cứu sinh người Hà Lan là Samuel Goudsmit và George Uhlenbeck đã đề xuất một giả thuyết mang tính đột phá: Electron sở hữu một mômen động lượng nội tại, được gọi là **spin**, độc lập hoàn toàn với chuyển động obitan của nó quanh hạt nhân. Đi kèm với mômen động lượng spin này là một mômen từ nội tại.

### Mô hình tương tự cổ điển và bản chất lượng tử của spin

Để hình dung trực quan về spin, ta có thể liên hệ với chuyển động của Trái Đất trong hệ Mặt Trời:
- **Chuyển động quỹ đạo**: Trái Đất chuyển động trên quỹ đạo quanh Mặt Trời, tương ứng với mômen động lượng obitan $\vec{L}$.
- **Chuyển động tự quay**: Trái Đất tự quay quanh trục đi qua tâm của nó, tương ứng với mômen động lượng spin $\vec{S}$.

Tổng mômen động lượng của hệ là tổng vector:

$$
\vec{J} = \vec{L} + \vec{S}
$$

> [!CAUTION] Cảnh báo quan trọng về mô hình cổ điển
> Ta không được hiểu electron là một quả cầu điện tích thực sự quay quanh trục trong không gian. Nếu giả định electron có bán kính cổ điển hữu hạn và quay để tạo ra mômen động lượng đo được, tốc độ tại bề mặt của nó sẽ phải lớn hơn nhiều lần tốc độ ánh sáng trong chân không $c$, điều này vi phạm thuyết tương đối hẹp. Trong cơ học lượng tử, spin là một đặc tính nội tại thuần túy của hạt cơ bản, tương tự như khối lượng nghỉ và điện tích.

### Lượng tử hóa spin của electron

Thực nghiệm chứng minh rằng mômen động lượng spin $\vec{S}$ của electron bị lượng tử hóa theo các quy tắc tương tự như mômen động lượng obitan $\vec{L}$, nhưng với số lượng tử spin cố định:

$$
s = \frac{1}{2}
$$

Hình chiếu của $\vec{S}$ lên trục $z$ bị lượng tử hóa và được xác định bởi **số lượng tử từ spin** $m_s$:

$$
S_z = m_s \hbar \tag{41.36}
$$

với $m_s = \pm 1/2$. Hai giá trị khả dĩ của $S_z$ tương ứng với:
- **Trạng thái spin hướng lên** ($m_s = +1/2$): $S_z = +\frac{1}{2}\hbar$.
- **Trạng thái spin hướng xuống** ($m_s = -1/2$): $S_z = -\frac{1}{2}\hbar$.

Độ lớn của mômen động lượng spin $\vec{S}$ được xác định bởi biểu thức:

$$
S = \sqrt{s(s + 1)}\,\hbar \tag{41.37}
$$

Với electron có $s = 1/2$, giá trị độ lớn này là $S = \frac{\sqrt{3}}{2}\,\hbar \approx 0{,}866\,\hbar$.

Vì độ lớn $S$ luôn lớn hơn độ lớn hình chiếu $|S_z| = 0{,}500\hbar$, vector spin $\vec{S}$ không bao giờ nằm hoàn toàn song song hoặc phản song song với trục $z$. Góc $\theta$ giữa $\vec{S}$ và trục $z$ được xác định bởi:

$$
\begin{aligned}
\cos\theta &= \frac{S_z}{S} \\
&= \frac{\pm 1/2}{\sqrt{3}/2} = \pm \frac{1}{\sqrt{3}}
\end{aligned}
$$

Góc này nhận hai giá trị đối xứng: $\theta \approx 54{,}7^\circ$ và $\theta \approx 125{,}3^\circ$.

### Mômen từ spin của electron

Tương tự như chuyển động obitan tạo ra mômen từ obitan $\vec{\mu}_L = -(e/2m)\vec{L}$, spin của electron tạo ra một **mômen từ spin** $\vec{\mu}_s$. Mômen từ này tỷ lệ với vector spin $\vec{S}$:

$$
\begin{aligned}
\vec{\mu}_s &= -g \left(\frac{e}{2m}\right)\vec{S} \\
&= -g \frac{\mu_B}{\hbar}\vec{S}
\end{aligned}
$$

Trong đó:
- $\mu_B = e\hbar / (2m)$ là **magneton Bohr**, có giá trị $\mu_B \approx 9{,}274 \times 10^{-24}\,\mathrm{J/T}$ (tương đương $5{,}788 \times 10^{-5}\,\mathrm{eV/T}$).
- Dấu trừ phản ánh điện tích âm của electron: Vector mômen từ $\vec{\mu}_s$ luôn chỉ ngược hướng với vector mômen động lượng spin $\vec{S}$.
- $g$ là hệ số không thứ nguyên của mômen từ spin. Độ lớn tỷ số từ cơ là $ge/(2m)$, có đơn vị khác với $g$. Phương trình tương đối tính do Paul Dirac xây dựng năm 1928 cho $g=2$ ở bậc gần đúng ấy. Điện động lực học lượng tử (QED), được phát triển sau đó khoảng hai thập niên, kể các hiệu chỉnh bức xạ và cho:

$$
g \approx 2{,}00232
$$

Giá trị thực nghiệm 2,00231930436182(52) cho thấy phép so sánh giữa tính toán QED và đo đạc có độ chính xác rất cao. Con số trong ngoặc biểu thị độ không đảm bảo ở những chữ số cuối. Độ lớn tỷ số từ cơ spin gần gấp đôi giá trị $e/(2m)$ của mômen quỹ đạo.

Thành phần của mômen từ spin theo trục $z$ nhận giá trị:

$$
\begin{aligned}
\mu_{sz} &= -g \left(\frac{e}{2m}\right)S_z \\
&= -g m_s \mu_B
\end{aligned} \tag{41.38}
$$

Với $m_s = \pm 1/2$ và lấy $g \approx 2{,}00232$:

$$
\begin{aligned}
\mu_{sz} &= \mp \frac{1}{2} g \mu_B \\
&= \mp (1{,}00116)\mu_B
\end{aligned}
$$

Khi đặt electron trong từ trường ngoài $\vec{B}$ hướng dọc theo trục $z$, thế năng tương tác từ $U$ của mômen từ spin là:

$$
U = -\vec{\mu}_s \cdot \vec{B} = -\mu_{sz} B
$$

Thay giá trị $\mu_{sz}$:

$$
U = \pm (1{,}00116)\mu_B B
$$

![Hình 41.16: So sánh giản đồ vạch quang phổ của hiệu ứng Zeeman thường và hiệu ứng Zeeman dị thường ở kẽm và natri.](../img/young-41/hinh-41-16.png)

### Thí nghiệm Stern–Gerlach

Năm 1922, Otto Stern và Walther Gerlach đã thực hiện một thí nghiệm lịch sử cung cấp bằng chứng trực tiếp cho sự lượng tử hóa không gian của mômen từ nguyên tử.

Trong thí nghiệm:
1. Chùm nguyên tử bạc trung hòa được tạo ra từ một lò nhiệt và bay theo phương ngang qua một khe hẹp.
2. Chùm hạt đi qua vùng từ trường có cấu tạo hình học bất đối xứng đặc biệt: Cực từ sắc nhọn kết hợp với cực từ lõm rãnh. Hình học này tạo ra một từ trường $\vec{B}$ không đều mạnh dọc theo phương thẳng đứng (trục $z$), tức là gradient từ trường $\partial B_z / \partial z$ rất lớn.
3. Lực tác dụng lên nguyên tử có mômen từ $\mu_z$ dọc theo phương $z$ được xác định bởi:

$$
F_z = -\frac{\partial U}{\partial z} = \mu_z \frac{\partial B_z}{\partial z}
$$

Nếu mômen từ định hướng ngẫu nhiên và liên tục theo quan điểm cổ điển, vết chùm hạt trên bản kính hứng phải trải rộng thành một dải liên tục. Tuy nhiên, kết quả thực nghiệm cho thấy chùm hạt bị tách thành **hai vạch riêng biệt**, một vạch lệch lên trên và một vạch lệch xuống dưới đối xứng qua trục ban đầu.

Mỗi nguyên tử bạc ở trạng thái cơ bản có 46 electron lấp đầy các vỏ trong với tổng mômen động lượng bằng không, và duy nhất 1 electron hóa trị ở phân lớp $5s$ ($l=0$). Do $l=0$, mômen từ obitan bằng không: Sự phân tách chùm tia hoàn toàn do mômen từ spin của electron $5s$ duy nhất này gây ra!

![Hình 41.17: Bố trí thực nghiệm của thí nghiệm Stern–Gerlach tách chùm nguyên tử thành hai thành phần.](../img/young-41/hinh-41-17.png)

### Ví dụ 41.6: Năng lượng spin của electron trong từ trường

Một electron tự do được đặt trong từ trường đều có độ lớn $B = 2{,}00\,\mathrm{T}$. Hãy xác định thành phần mômen từ $\mu_z$, thế năng tương tác từ $U$ của electron ở hai trạng thái spin, và tần số sóng điện từ cần thiết để kích thích bước nhảy spin giữa hai mức này.

**Nhận dạng bài toán**: Electron có hai định hướng spin khả dĩ đối với trục từ trường ($m_s = \pm 1/2$), dẫn đến hai mức năng lượng tách rời nhau do tương tác spin–từ trường.

**Chuẩn bị**: Sử dụng các biểu thức $\mu_z = \mp (1{,}00116)\mu_B$ và $U = -\mu_z B$. Hiệu năng lượng giữa hai trạng thái là $\Delta U = U_{\mathrm{up}} - U_{\mathrm{down}}$. Tần số photon kích thích thỏa mãn điều kiện cộng hưởng $h f = \Delta U$.

**Thực hiện**:
Thành phần mômen từ theo phương $z$ ứng với hai trạng thái:

$$
\begin{aligned}
\mu_z &= \mp (1{,}00116)\mu_B \\
&= \mp 9{,}285 \times 10^{-24}\,\mathrm{J/T} \\
&= \mp 5{,}795 \times 10^{-5}\,\mathrm{eV/T}
\end{aligned}
$$

Thế năng tương tác từ trong từ trường $B = 2{,}00\,\mathrm{T}$:

$$
\begin{aligned}
U &= -\mu_z B \\
&= \pm 1{,}159 \times 10^{-4}\,\mathrm{eV} \\
&= \pm 1{,}857 \times 10^{-23}\,\mathrm{J}
\end{aligned}
$$

Hiệu năng lượng giữa trạng thái spin hướng lên và spin hướng xuống:

$$
\begin{aligned}
\Delta U &= 2|U| \\
&= 2{,}318 \times 10^{-4}\,\mathrm{eV} \\
&= 3{,}714 \times 10^{-23}\,\mathrm{J}
\end{aligned}
$$

Tần số photon tương ứng với sự cộng hưởng spin electron:

$$
\begin{aligned}
f &= \frac{\Delta U}{h} \\
&= 5{,}60 \times 10^{10}\,\mathrm{Hz} \\
&= 56{,}0\,\mathrm{GHz}
\end{aligned}
$$

**Đánh giá**: Tần số $56{,}0\,\mathrm{GHz}$ nằm trong dải sóng vi ba (microwaves). Hiện tượng hấp thụ năng lượng vi ba kích thích đảo spin của electron trong từ trường là nguyên lý của phương pháp **Cộng hưởng thuận từ electron** (EPR hay ESR).

**Khái niệm cần nhớ**: Mômen từ spin của electron tương tác với từ trường ngoài làm tách mức năng lượng thành hai trạng thái riêng biệt, mở ra khả năng điều khiển trạng thái lượng tử bằng sóng điện từ dải vi ba.

![Ứng dụng: Xác định niên đại nguồn gốc loài người bằng phương pháp cộng hưởng spin electron.](../img/young-41/ung-dung-b-1.png)

> [!NOTE] Ứng dụng y sinh: Spin của electron và việc xác định niên đại nguồn gốc loài người
> Trong nhiều nguyên tử, tổng spin của tất cả các electron bằng không (số electron spin hướng lên bằng số electron spin hướng xuống). Tuy nhiên, nếu các nguyên tử này bị ion hóa và mất đi một electron, tổng spin của ion còn lại sẽ khác không. Quá trình này diễn ra tự nhiên trong men răng, nơi sự ion hóa gây ra bởi phóng xạ từ môi trường. Răng tiếp xúc càng lâu thì số lượng ion tích tụ càng nhiều. Để xác định niên đại của các răng hóa thạch, chẳng hạn như những chiếc răng trong hộp sọ người Neanderthal (*Homo neanderthalensis*), một mẫu men răng được đặt trong từ trường mạnh. Spin của các ion định hướng ngược chiều với từ trường (trạng thái spin hướng xuống). Sau đó, mẫu vật được chiếu các photon sóng vi ba có mức năng lượng thích hợp để kích thích đảo spin sang cấu hình năng lượng cao hơn cùng chiều với từ trường (trạng thái spin hướng lên). Lượng năng lượng sóng vi ba bị hấp thụ trong quá trình này (gọi là phương pháp cộng hưởng spin electron - ESR) cho biết số lượng ion hiện diện và từ đó xác định được niên đại của men răng.

### Tương tác spin–quỹ đạo và cấu trúc tinh tế

Trong hệ quy chiếu gắn với electron, hạt nhân mang điện tích dương chuyển động tròn xung quanh electron. Dòng điện này tạo ra một từ trường nội tại $\vec{B}_{\mathrm{int}}$ ngay tại vị trí của electron. Mômen từ spin $\vec{\mu}_s$ của electron tương tác với chính từ trường nội tại này, tạo nên thế năng tương tác:

$$
U = -\vec{\mu}_s \cdot \vec{B}_{\mathrm{int}}
$$

Hiệu ứng này được gọi là **tương tác spin–quỹ đạo** (spin-orbit coupling). Vì $\vec{B}_{\mathrm{int}}$ cùng phương với mômen động lượng obitan $\vec{L}$, thế năng tương tác tỷ lệ với tích vô hướng:

$$
U \propto \vec{L} \cdot \vec{S}
$$

Mômen động lượng obitan $\vec{L}$ và mômen động lượng spin $\vec{S}$ có thể kết hợp theo nhiều cách khác nhau. Tổng vector của $\vec{L}$ và $\vec{S}$ là **tổng mômen động lượng** $\vec{J}$:

$$
\vec{J} = \vec{L} + \vec{S} \tag{41.39}
$$

Độ lớn của $\vec{J}$ được lượng tử hóa theo số lượng tử tổng $j$, gọi là **số lượng tử mômen động lượng tổng**:

$$
J = \sqrt{j(j + 1)}\,\hbar \tag{41.40}
$$

Đối với một electron đơn lẻ với $s = 1/2$, số lượng tử $j$ có hai giá trị khả dĩ ứng với $l > 0$:

$$
\begin{aligned}
j &= l + \frac{1}{2}, \\
j &= l - \frac{1}{2}.
\end{aligned}
$$

- Khi $j = l + 1/2$: Vector $\vec{L}$ và $\vec{S}$ có xu hướng song song, năng lượng tương tác đẩy mức lên cao hơn.
- Khi $j = l - 1/2$: Vector $\vec{L}$ và $\vec{S}$ có xu hướng phản song song, năng lượng tương tác kéo mức xuống thấp hơn.

![Hình 41.18: Mức l = 0 của một electron đơn lẻ bị tách đôi do tương tác của mômen từ spin với từ trường ngoài.](../img/young-41/hinh-41-18.png)

Ký hiệu quang phổ cho các trạng thái này có dạng:

$$
n^{2s+1}L_j
$$

Ví dụ: Mức $2p$ ($n=2, l=1$) của hydro bị tách thành hai mức con: $2P_{3/2}$ và $2P_{1/2}$.

Khi tính đến cả tương tác spin–quỹ đạo lẫn hiệu chỉnh động năng tương đối tính, mức năng lượng của nguyên tử hydro phụ thuộc vào cả $n$ và $j$:

$$
E_{n,j} = -\frac{13{,}60\,\mathrm{eV}}{n^2}(1 + \delta_{n,j}) \tag{41.41}
$$

Trong đó số hiệu chỉnh cấu trúc tinh tế $\delta_{n,j}$ được xác định bởi:

$$
\delta_{n,j} = \frac{\alpha^2}{n^2}\left(\frac{n}{j + 1/2} - \frac{3}{4}\right)
$$

Và $\alpha$ là **hằng số cấu trúc tinh tế**, một đại lượng không thứ nguyên:

$$
\begin{aligned}
\alpha &= \frac{1}{4\pi\epsilon_0}\frac{e^2}{\hbar c} \\
&\approx \frac{1}{137{,}04}
\end{aligned} \tag{41.42}
$$

Giá trị thực nghiệm chính xác của hằng số này là $\alpha \approx 7{,}29735 \times 10^{-3}$.

### Ví dụ 41.7: Từ trường hiệu dụng

Với độ chính xác 6 chữ số có nghĩa, bước sóng của hai vạch quang phổ tạo nên vạch đôi natri là $\lambda_1 = 588{,}995\,\mathrm{nm}$ và $\lambda_2 = 589{,}592\,\mathrm{nm}$. Hãy tính từ trường hiệu dụng mà electron trong các mức $3p$ của nguyên tử natri cảm nhận được.

**Nhận dạng bài toán**: Hai vạch trong vạch đôi natri sinh ra từ các bước chuyển từ hai mức $3p$ (bị tách do tương tác spin–quỹ đạo) xuống mức $3s$ (không bị tách vì có $L = 0$). Ta hình dung tương tác spin–quỹ đạo như tương tác giữa mômen từ spin của electron và từ trường hiệu dụng do hạt nhân tạo ra trong hệ quy chiếu của electron. Bài toán này là bài toán ngược của Ví dụ 41.6: Ở đó ta biết $B$ và tìm độ tách mức năng lượng, còn ở đây ta dùng độ tách năng lượng để tìm độ lớn từ trường $B$. Độ chênh lệch năng lượng giữa hai mức $3p$ bằng hiệu năng lượng giữa hai photon của vạch đôi natri.

**Chuẩn bị**: Năng lượng của hai photon lần lượt là $E_1 = hc/\lambda_1$ và $E_2 = hc/\lambda_2$. Ở đây $E_1 > E_2$ vì $\lambda_1 < \lambda_2$, do đó độ chênh lệch năng lượng giữa hai photon là:

$$
\Delta E = hc\left(\frac{1}{\lambda_1} - \frac{1}{\lambda_2}\right)
$$

**Thực hiện**:
Thay các giá trị số với $\lambda_1 = 588{,}995\,\mathrm{nm}$, $\lambda_2 = 589{,}592\,\mathrm{nm}$, $h = 4{,}136 \times 10^{-15}\,\mathrm{eV\cdot s}$ và $c = 2{,}998 \times 10^8\,\mathrm{m/s}$:

$$
\begin{aligned}
\Delta E &= 0{,}00213\,\mathrm{eV} \\
&= 3{,}41 \times 10^{-22}\,\mathrm{J}
\end{aligned}
$$

Giá trị này đúng bằng độ chênh lệch năng lượng giữa hai mức $3p$. Tương tác spin–quỹ đạo nâng một mức lên một lượng $1{,}70 \times 10^{-22}\,\mathrm{J}$ (một nửa của $3{,}41 \times 10^{-22}\,\mathrm{J}$) và hạ mức kia xuống một lượng $1{,}70 \times 10^{-22}\,\mathrm{J}$. Từ Ví dụ 41.6, độ dịch năng lượng của mỗi trạng thái là $|U| = (1{,}00116)\mu_B B$, do đó:

$$
\begin{aligned}
B &= \frac{|U|}{(1{,}00116)\mu_B} \\
&\approx 18{,}4\,\mathrm{T}
\end{aligned}
$$

**Đánh giá:** Từ trường hiệu dụng khoảng $18{,}4\,\mathrm T$ biểu diễn độ tách năng lượng do tương tác spin–quỹ đạo trong mô hình đang xét. Đây là thang tương tác bên trong nguyên tử, không phải một từ trường ngoài đã được đặt vào mẫu.

**Khái niệm cần nhớ**: Với mômen động lượng obitan khác không, chuyển động tương đối của hạt nhân tạo nên từ trường hiệu dụng trong mô hình gắn với electron. Tương tác giữa trường này và mômen từ spin góp phần tách các mức năng lượng.

### Ví dụ 41.8: Cấu trúc tinh tế và sự tách vạch quang phổ

Đối với một electron có số lượng tử obitan $l = 0$, mômen động lượng hoàn toàn do spin tạo nên và giá trị khả dĩ duy nhất của số lượng tử mômen động lượng tổng là $j = 1/2$. Nếu $l = 1$, có hai giá trị khả dĩ: $j = 3/2$ (các vector mômen động lượng spin và obitan có chiều xấp xỉ cùng nhau nên cộng lại) và $j = 1/2$ (các vector mômen động lượng spin và obitan có chiều gần như ngược nhau nên triệt tiêu một phần).

(a) Hãy tìm năng lượng của trạng thái electron trong nguyên tử hydro có $n = 2, l = 1, j = 3/2$ (trạng thái $2P_{3/2}$) và trạng thái có $n = 2, l = 1, j = 1/2$ (trạng thái $2P_{1/2}$), rồi tính độ chênh lệch giữa hai năng lượng này. Trạng thái nào có năng lượng cao hơn?

(b) Tìm độ chênh lệch bước sóng giữa (i) một photon phát ra trong bước chuyển từ trạng thái $n = 2, l = 1, j = 3/2$ về trạng thái $n = 1, l = 0, j = 1/2$ và (ii) một photon phát ra trong bước chuyển từ trạng thái $n = 2, l = 1, j = 1/2$ về trạng thái $n = 1, l = 0, j = 1/2$. Photon nào có bước sóng dài hơn?

**Nhận dạng và chuẩn bị**: Ở phần (a), ta áp dụng PT (41.41) để tìm năng lượng của hai trạng thái có cùng số lượng tử $n$ nhưng khác số lượng tử $j$. Độ chênh lệch năng lượng này do cấu trúc tinh tế tạo ra nên có giá trị rất nhỏ. Ở phần (b), cả hai bước chuyển đều kết thúc ở cùng một trạng thái cơ bản $n = 1, l = 0, j = 1/2$, thuộc dãy Lyman. Nếu không có cấu trúc tinh tế, hai trạng thái ban đầu sẽ có cùng năng lượng và phát ra cùng một bước sóng. Vì hai trạng thái ban đầu có năng lượng hơi khác nhau, hai photon phát ra sẽ có bước sóng khác nhau đôi chút.

**Thực hiện**:
(a) Với $n = 2$ và độ lớn năng lượng Bohr $B_2 = 3{,}40\,\mathrm{eV}$, PT (41.41) cho năng lượng của hai trạng thái có dạng:

$$
\begin{aligned}
E_{2, 3/2} &= -B_2\left(1 + \frac{\alpha^2}{16}\right) \\
E_{2, 1/2} &= -B_2\left(1 + \frac{5\alpha^2}{16}\right)
\end{aligned}
$$

Các số hạng hiệu chỉnh cấu trúc tinh tế chứa $\alpha^2$ làm cho năng lượng của cả hai trạng thái đều âm hơn (thấp hơn) so với mô hình Bohr ($E_2 = -3{,}40\,\mathrm{eV}$). Số hạng hiệu chỉnh này lớn gấp 5 lần đối với trạng thái $j = 1/2$, do đó trạng thái $j = 3/2$ có mức năng lượng cao hơn (ít âm hơn). Sử dụng giá trị $\alpha \approx 1/137{,}04$ từ PT (41.42), hiệu năng lượng giữa hai trạng thái là:

$$
\begin{aligned}
\Delta E &= 3{,}40\,\mathrm{eV}\left(\frac{\alpha^2}{4}\right) \\
&= 4{,}53 \times 10^{-5}\,\mathrm{eV}
\end{aligned}
$$

(b) Năng lượng photon bằng hiệu năng lượng giữa trạng thái đầu và trạng thái cuối. Trạng thái cơ bản cuối cho cả hai bước chuyển có $n = 1$ và $j = 1/2$, theo PT (41.41) có năng lượng:

$$
E_{\mathrm{g}} = -13{,}60\,\mathrm{eV}\left(1 + \frac{\alpha^2}{4}\right)
$$

Đặt $E_0=3B_2$ và $\delta=B_2\alpha^2/16$. Từ hiệu năng lượng đầu và cuối, ta có:

$$
\begin{aligned}
E_{\gamma1}&=E_{2,3/2}-E_{\rm g}\\
&=E_0+15\delta,\\
E_{\gamma2}&=E_{2,1/2}-E_{\rm g}\\
&=E_0+11\delta.
\end{aligned}
$$

Năng lượng nền là $E_0=10{,}20\,\mathrm{eV}$. Các phần hiệu chỉnh có giá trị:

$$
\begin{aligned}
15\delta&\approx1{,}70\times10^{-4}\,\mathrm{eV},\\
11\delta&\approx1{,}24\times10^{-4}\,\mathrm{eV}.
\end{aligned}
$$

Vì hai chuyển mức có cùng trạng thái cuối, hiệu năng lượng hai photon bằng hiệu năng lượng hai trạng thái đầu:

$$
\Delta E_\gamma=4{,}53\times10^{-5}\,\mathrm{eV}.
$$

Photon phát ra từ trạng thái ban đầu $n = 2, l = 1, j = 1/2$ có năng lượng thấp hơn, do đó sẽ có bước sóng dài hơn theo hệ thức $\lambda = hc/E_{\mathrm{photon}}$. Vì hiệu năng lượng quá nhỏ, việc bấm trực tiếp máy tính sẽ cho ra $\lambda \approx 121{,}6\,\mathrm{nm}$ ở cả hai trường hợp. Để tìm độ lệch bước sóng $\Delta\lambda$, ta lấy vi phân hai vế của $\lambda = hc/E_{\mathrm{photon}}$:

$$
\begin{aligned}
d\lambda&=d\left(\frac{hc}{E_\gamma}\right)\\
&=-\frac{hc}{E_\gamma^2}\,dE_\gamma\\
&=-\frac{\lambda}{E_\gamma}\,dE_\gamma.
\end{aligned}
$$

Dấu trừ biểu thị rằng năng lượng photon giảm thì bước sóng tăng lên. Thay vi phân bằng các biến thiên hữu hạn và lấy độ lớn:

$$
\begin{aligned}
\Delta\lambda &= \frac{\lambda}{E_{\mathrm{photon}}} \Delta E_{\mathrm{photon}} \\
&\approx 5{,}40 \times 10^{-4}\,\mathrm{nm}
\end{aligned}
$$

**Đánh giá**: Sự tách vạch này rất nhỏ, đúng như tên gọi cấu trúc tinh tế. Tuy nhiên, nó hoàn toàn có thể quan sát được bằng cách tử nhiễu xạ có số lượng vạch đủ lớn (xem Mục 36.5). Các bước sóng đo được trong thực nghiệm là $121{,}567364\,\mathrm{nm}$ đối với bước chuyển bắt đầu từ trạng thái $j = 1/2$ và $121{,}566824\,\mathrm{nm}$ đối với bước chuyển bắt đầu từ trạng thái $j = 3/2$. Đây là các bước sóng thuộc vùng tử ngoại.

Nguyên tử hydro cũng có trạng thái với $n = 2, l = 0, j = 1/2$. Từ PT (41.41), trạng thái này có cùng năng lượng với trạng thái $n = 2, l = 1, j = 1/2$ do năng lượng $E_{n,j}$ chỉ phụ thuộc vào $n$ và $j$ mà không phụ thuộc vào $l$. Tuy nhiên, electron ở trạng thái $n = 2, l = 0, j = 1/2$ không thể phát xạ photon để chuyển trực tiếp về trạng thái $n = 1, l = 0, j = 1/2$. Trong gần đúng lưỡng cực điện đang dùng, bước chuyển một photon này bị cấm vì phải có $\Delta l=\pm1$. Kết luận này không loại trừ những cơ chế ở bậc khác.

**Khái niệm cần nhớ**: Khi tính đến cả hiệu ứng từ tính và hiệu ứng tương đối tính, các mức năng lượng của nguyên tử hydro phụ thuộc vào cả số lượng tử chính $n$ và số lượng tử mômen động lượng tổng $j$. Trong gần đúng lưỡng cực điện, chuyển mức một photon thỏa $\Delta l=\pm1$.

### Cấu trúc siêu tinh tế và vạch 21 cm của hydro

Ngoài mômen từ của electron, hạt nhân nguyên tử (proton đối với hydro) cũng mang điện tích và có spin hạt nhân $I = 1/2$, do đó có một **mômen từ hạt nhân** $\vec{\mu}_p$. Vì proton có khối lượng lớn hơn electron khoảng 1836 lần, mômen từ hạt nhân nhỏ hơn mômen từ electron khoảng ba bậc độ lớn:

$$
\mu_N = \frac{e\hbar}{2 m_p} \approx \frac{\mu_B}{1836}
$$

Sự tương tác từ giữa mômen từ spin của electron và mômen từ của hạt nhân tạo ra một độ dịch năng lượng cực nhỏ gọi là **cấu trúc siêu tinh tế** (hyperfine structure).

Ở trạng thái cơ bản $1s$ của hydro:
- Khi spin của electron và proton **song song nhau**, hệ có năng lượng cao hơn một chút.
- Khi spin của electron và proton **ngược chiều nhau**, hệ có năng lượng thấp hơn.

Độ chênh lệch năng lượng giữa hai trạng thái này là:

$$
\begin{aligned}
\Delta E &= 5{,}9 \times 10^{-6}\,\mathrm{eV} \\
&\approx 9{,}5 \times 10^{-25}\,\mathrm{J}
\end{aligned}
$$

Khi electron ở trạng thái song song tự phát đảo spin để chuyển về trạng thái ngược chiều, nó phát ra một photon có bước sóng:

$$
\begin{aligned}
\lambda &= \frac{hc}{\Delta E} \\
&\approx 0{,}21\,\mathrm{m}=21\,\mathrm{cm}
\end{aligned}
$$

Với độ chính xác của năng lượng đã cho, tần số tương ứng khoảng $1{,}4\,\mathrm{GHz}$.

Vạch vô tuyến $21\,\mathrm{cm}$ cho phép khảo sát những đám mây hydro quá lạnh để phát ánh sáng khả kiến. Ở Hình 41.19, ba thiên hà có vẻ tách rời trong ảnh quang học. Ảnh vô tuyến cho thấy các dải khí hydro nối chúng với nhau.

![Hình 41.19: So sánh hình ảnh quang học vùng ánh sáng khả kiến (a) và ảnh thiên văn vô tuyến ở bước sóng 21 cm (b) của các thiên hà.](../img/young-41/hinh-41-19.png)

### Câu tự kiểm tra 41.5

Trong tình huống nào sau đây thì mômen từ của một electron định hướng thẳng hàng hoàn hảo với từ trường hướng theo chiều dương của trục $z$?

(i) $m_s = +1/2$

(ii) $m_s = -1/2$

(iii) Cả (i) và (ii)

(iv) Cả (i) và (ii) đều không phải

::: details Lời giải chi tiết
**Đáp án đúng**: (iv).

**Lập luận**:
Để mômen từ định hướng thẳng hàng hoàn hảo với chiều dương của trục $z$, thành phần theo trục $z$ của vector spin $\vec{S}$ phải có độ lớn tuyệt đối bằng đúng độ lớn của vector $\vec{S}$.

Tuy nhiên, các giá trị khả dĩ của $S_z$ theo PT (41.36) là:

$$
S_z = \pm \frac{1}{2}\,\hbar
$$

trong khi độ lớn của vector spin theo PT (41.37) là:

$$
\begin{aligned}
S &= \sqrt{s(s + 1)}\,\hbar \\
&= \frac{\sqrt{3}}{2}\,\hbar \approx 0{,}866\,\hbar
\end{aligned}
$$

Vì $|S_z| < S$, góc $\theta$ hợp bởi vector $\vec{S}$ và trục $z$ thỏa mãn:

$$
\cos\theta = \pm \frac{1}{\sqrt{3}}
$$

Góc $\theta$ tương ứng có giá trị xấp xỉ $54{,}7^\circ$ hoặc $125{,}3^\circ$.

Do đó, vector spin $\vec{S}$ không bao giờ có thể nằm hoàn toàn song song hoặc thẳng hàng với bất kỳ một phương xác định nào trong không gian. Vì vector mômen từ $\vec{\mu}_s = -g(e/2m)\vec{S}$ tỷ lệ và ngược hướng với vector spin $\vec{S}$, nó cũng không bao giờ có thể định hướng thẳng hàng hoàn hảo với phương của từ trường ngoài.
:::
