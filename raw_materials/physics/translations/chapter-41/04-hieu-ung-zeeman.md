## 41.4. Hiệu ứng Zeeman

Khi đặt nguyên tử trong từ trường ngoài, một vạch phổ có thể tách thành nhiều vạch gần nhau. Đó là hiệu ứng Zeeman, gắn với sự dịch chuyển các mức năng lượng. Hiện tượng giúp kiểm tra sự lượng tử hóa mômen động lượng. Trước hết, ta chỉ xét mômen quỹ đạo của một electron để thấy vai trò của số lượng tử từ $m_l$.

Các nguyên tử cấu tạo từ những điện tích chuyển động, do đó lực từ tác dụng lên các dòng điện vi mô này sẽ làm biến đổi trạng thái chuyển động và làm dịch chuyển các mức năng lượng. Năm 1896, nhà vật lý người Hà Lan Pieter Zeeman lần đầu tiên phát hiện khi đặt nguồn phát sáng trong từ trường, một số vạch quang phổ vốn đơn lẻ bị tách thành các nhóm vạch nằm sát nhau. Hiện tượng này mang tên ông: Hiệu ứng Zeeman.

![Hình 41.11: Ảnh hưởng của từ trường lên quang phổ Mặt Trời. Ở phần (a), khe máy quang phổ đi qua vết đen. Ở phần (b), từ trường khoảng 0,4 T làm vạch giữa tách thành ba. Từ trường này mạnh hơn nhiều từ trường Trái Đất.](../img/young-41/hinh-41-11.png)

![Hình 41.12: Hiệu ứng Zeeman thường. Khi một chất khí kích thích được đặt trong từ trường ngoài, tương tác của mômen từ quỹ đạo với từ trường làm tách các vạch quang phổ riêng lẻ của chất khí thành các bộ ba vạch phân biệt.](../img/young-41/hinh-41-12.png)

### Mômen từ của electron quay trên quỹ đạo

Để phân tích hiệu ứng Zeeman, trước hết chúng ta nhắc lại khái niệm momen lưỡng cực từ (gọi tắt là mômen từ) của dòng điện kín. Một vòng dây phẳng có diện tích vector $\vec{A}$ mang dòng điện cường độ $I$ sở hữu mômen từ $\vec{\mu}$ được xác định bởi:

$$
\vec{\mu} = I\vec{A} \tag{41.27}
$$

Khi đặt lưỡng cực từ có mômen từ $\vec{\mu}$ vào trong một từ trường ngoài $\vec{B}$, từ trường sẽ tác dụng lên lưỡng cực một ngẫu lực $\vec{\tau} = \vec{\mu} \times \vec{B}$. Thế năng tương tác $U$ của lưỡng cực từ trong từ trường là:

$$
U = -\vec{\mu}\cdot\vec{B} \tag{41.28}
$$

Áp dụng các hệ thức trên cho chuyển động của electron trong nguyên tử. Một electron mang điện tích có độ lớn $e$ chuyển động với tốc độ $v$ trên quỹ đạo tròn bán kính $r$ tương đương với một dòng điện tròn có diện tích $A = \pi r^2$. Cường độ dòng điện trung bình $I$ là lượng điện tích dịch chuyển qua một tiết diện trong một đơn vị thời gian, bằng điện tích $e$ chia cho chu kỳ quay $T = 2\pi r/v$:

$$
I = \frac{e}{T} = \frac{ev}{2\pi r}
$$

Độ lớn mômen từ quỹ đạo của electron là:

$$
\begin{aligned}
\mu &= IA \\
&= \frac{evr}{2}
\end{aligned} \tag{41.29}
$$

Mặt khác, độ lớn mômen động lượng của electron quay tròn là $L = mvr$, suy ra $vr = L/m$. Thay vào biểu thức (41.29), độ lớn mômen từ liên hệ trực tiếp với độ lớn mômen động lượng quỹ đạo:

$$
\mu = \frac{e}{2m} L \tag{41.30}
$$

Tỷ số giữa độ lớn mômen từ $\mu$ và độ lớn mômen động lượng $L$ là $\mu/L = e/(2m)$, được gọi là tỷ số từ cơ (gyromagnetic ratio).

Trong mô hình Bohr, trạng thái cơ bản có $L = \hbar$, khi đó biểu thức (41.30) trở thành $\mu = (e/2m)\hbar$. Đại lượng này là đơn vị tự nhiên chuẩn mực của mômen từ trong vật lý nguyên tử, được gọi là magneton Bohr, ký hiệu là $\mu_{\mathrm{B}}$:

$$
\mu_{\mathrm{B}} = \frac{e\hbar}{2m} \tag{41.31}
$$

Giá trị của magneton Bohr trong hệ SI và hệ đơn vị electron-volt là:

$$
\begin{aligned}
\mu_{\mathrm{B}} &= 9{,}274 \times 10^{-24}\,\text{J/T} \\
&= 5{,}788 \times 10^{-5}\,\text{eV/T}
\end{aligned}
$$

Lưu ý rằng hai đơn vị $\text{J/T}$ và $\text{A}\cdot\text{m}^2$ hoàn toàn tương đương nhau.

Mô hình bán cổ điển giúp liên hệ mômen từ với mômen động lượng, nhưng dự đoán sai mômen từ quỹ đạo ở trạng thái cơ bản của hydro. Mô hình Bohr cho $L=\hbar$ và mômen từ quỹ đạo bằng $\mu_{\rm B}$. Nghiệm Schrödinger cho trạng thái $1s$ có $l=0$, nên cả $L$ và mômen từ quỹ đạo đều bằng không.

### Năng lượng tương tác từ trong cơ học lượng tử

Trong cơ học lượng tử, electron vẫn bảo toàn tỷ số từ cơ $e/(2m)$. Tuy nhiên, vì electron mang điện tích âm $-e$, vector mômen từ quỹ đạo $\vec{\mu}$ luôn hướng ngược chiều với vector mômen động lượng quỹ đạo $\vec{L}$:

$$
\vec{\mu} = -\frac{e}{2m} \vec{L}
$$

Chọn chiều dương của trục $z$ trùng với hướng của từ trường ngoài $\vec{B} = B\hat{k}$. Từ phương trình (41.28), năng lượng tương tác $U$ giữa mômen từ của electron và từ trường ngoài là:

$$
U = -\vec{\mu}\cdot\vec{B} = -\mu_z B \tag{41.32}
$$

Trong đó $\mu_z$ là hình chiếu của vector mômen từ $\vec{\mu}$ lên trục $z$. Vì vector $\vec{\mu}$ ngược hướng với $\vec{L}$, thành phần $\mu_z$ liên hệ với thành phần $L_z$ thông qua dấu trừ:

$$
\mu_z = -\frac{e}{2m} L_z \tag{41.33}
$$

Theo lý thuyết lượng tử Schrödinger, hình chiếu của mômen động lượng lên trục $z$ bị lượng tử hóa: $L_z = m_l \hbar$, với $m_l \in \{0, \pm 1, \pm 2, \dots, \pm l\}$. Thay vào phương trình (41.33):

$$
\begin{aligned}
\mu_z &= -m_l \frac{e\hbar}{2m} \\
&= -m_l \mu_{\mathrm{B}}
\end{aligned} \tag{41.34}
$$

::: warning Cảnh báo: Phân biệt ký hiệu khối lượng và số lượng tử từ
Một lần nữa cần lưu ý ký hiệu $m$ trong mẫu số của phương trình (41.34) là khối lượng của electron, trong khi $m_l$ là số lượng tử từ quỹ đạo không thứ nguyên.
:::

Thay biểu thức $\mu_z$ vào phương trình năng lượng tương tác (41.32), chúng ta thu được thế năng tương tác từ:

$$
\begin{aligned}
U &= -\mu_z B \\
&= m_l \mu_{\mathrm{B}} B
\end{aligned} \tag{41.35}
$$

Trong gần đúng đang xét, từ trường làm dịch mức năng lượng một lượng $U$. Độ dịch phụ thuộc $m_l$, vì số này xác định hình chiếu mômen từ theo hướng từ trường. Quan hệ ấy giải thích tên gọi số lượng tử từ.

### Sự tách mức năng lượng và phá vỡ tính suy biến

Ứng với một giá trị xác định của số lượng tử quỹ đạo $l$, số lượng tử từ $m_l$ nhận $2l + 1$ giá trị nguyên khác nhau từ $-l$ đến $+l$. Khi chưa có từ trường ($B = 0$), toàn bộ $2l + 1$ trạng thái này có cùng một mức năng lượng, tức là mức năng lượng bị suy biến bậc $2l + 1$.

Khi đặt nguyên tử vào từ trường ngoài $B$, từ trường sẽ khử bỏ tính suy biến này. Mỗi trạng thái có một mức dịch chuyển năng lượng khác nhau phụ thuộc vào $m_l$, làm mức năng lượng ban đầu bị tách thành $2l + 1$ mức phân biệt. Khoảng cách năng lượng giữa hai mức kế tiếp nhau là một lượng không đổi:

$$
\Delta E = \mu_{\mathrm{B}} B = \left(\frac{e\hbar}{2m}\right)B
$$

Từ trường dọc trục $z$ làm mất đối xứng quay cầu của bài toán, vì xuất hiện một hướng ưu tiên. Phép quay quanh chính trục $z$ vẫn giữ nguyên từ trường. Vì thế, không nên hiểu sự tách mức là mất mọi đối xứng quay.

Sơ đồ mức năng lượng của nguyên tử hydro khi đặt trong từ trường ngoài minh họa rõ nét cách thức từ trường làm tách các mức năng lượng ban đầu. Ở trạng thái cơ bản $n = 1$ ($l = 0, m_l = 0$), mức năng lượng không bị tách vì mômen từ quỹ đạo triệt tiêu. Ở mức $n = 2$, trạng thái $2s$ ($l = 0$) không đổi, trong khi phân lớp $2p$ ($l = 1$) tách thành ba mức ứng với $m_l = +1, 0, -1$. Tương tự, ở mức $n = 3$, phân lớp $3s$ không tách, phân lớp $3p$ tách thành 3 mức, và phân lớp $3d$ ($l = 2$) tách thành 5 mức ứng với $m_l = +2, +1, 0, -1, -2$. Khoảng cách giữa các mức kề nhau đối với các trạng thái có cùng số lượng tử quỹ đạo $l$ đều bằng $\Delta E = \mu_{\mathrm{B}} B$. Mặc dù độ tách mức này rất nhỏ so với khoảng cách giữa các mức chính $n$, các chuyển dời quang học giữa các nhóm mức này sẽ phát ra các bộ vạch quang phổ nằm sát nhau thay vì các vạch đơn lẻ.

![Hình 41.13: Các mức của hydro khi chưa xét spin. Từ trường làm tách các trạng thái có số lượng tử từ khác nhau, trong khi mức s không có độ dịch quỹ đạo.](../img/young-41/hinh-41-13.png)

![Hình 41.14: Mức d tách thành năm mức khi từ trường tăng. Các độ dịch năng lượng lần lượt là hai, một, không, trừ một và trừ hai lần μB B.](../img/young-41/hinh-41-14.png)

### Ví dụ 41.5: Nguyên tử trong từ trường ngoài

Một nguyên tử ở trạng thái có $l = 1$ phát ra một photon có bước sóng $600{,}000\,\text{nm}$ khi chuyển dời về trạng thái có $l = 0$. Nếu nguyên tử được đặt trong một từ trường đều có độ lớn $B = 2{,}00\,\text{T}$, hãy xác định độ dịch chuyển của các mức năng lượng và độ dịch chuyển bước sóng sinh ra do tương tác giữa mômen từ quỹ đạo của electron với từ trường ngoài.

#### Phương pháp giải

Bài toán khảo sát hiện tượng tách mức năng lượng trong từ trường (hiệu ứng Zeeman). Độ dịch chuyển năng lượng của từng mức được xác định bằng phương trình (41.35). Hệ thức $E = hc/\lambda$ cho phép xác định năng lượng photon ban đầu và liên hệ độ dịch chuyển năng lượng $\Delta E$ với độ dịch chuyển bước sóng $\Delta\lambda$.

#### Lời giải chi tiết

Năng lượng của photon có bước sóng $600{,}000\,\text{nm}$ khi chưa có từ trường là:

$$
E = \frac{hc}{\lambda} = 2{,}07\,\text{eV}
$$

với $h = 4{,}136 \times 10^{-15}\,\text{eV}\cdot\text{s}$, $c = 3{,}00 \times 10^8\,\text{m/s}$, và $\lambda = 600 \times 10^{-9}\,\text{m}$. Khi chưa có từ trường ngoài, $2{,}07\,\text{eV}$ chính là hiệu năng lượng giữa mức $l = 1$ và mức $l = 0$.

Khi đặt vào từ trường $B = 2{,}00\,\text{T}$, trạng thái $l = 0$ có $m_l = 0$ nên mức năng lượng không bị dịch chuyển ($U = 0$).

Đối với mức $l = 1$, các giá trị khả dĩ của $m_l$ là $-1, 0, +1$. Độ dịch chuyển năng lượng của các trạng thái này theo đơn vị eV:

$$
U = m_l (1{,}16 \times 10^{-4}\,\text{eV})
$$

với $\Delta E = \mu_{\mathrm{B}} B = 1{,}16 \times 10^{-4}\,\text{eV}$. Biểu diễn theo đơn vị Joule:

$$
U = m_l (1{,}85 \times 10^{-23}\,\text{J})
$$

với $\Delta E = 1{,}85 \times 10^{-23}\,\text{J}$.

Ba mức năng lượng bị tách ra cách đều nhau một khoảng năng lượng $\Delta E = 1{,}16 \times 10^{-4}\,\text{eV}$. So với năng lượng toàn phần của photon $E = 2{,}07\,\text{eV}$, độ dịch năng lượng này chiếm một tỷ lệ rất nhỏ:

$$
\begin{aligned}
\frac{\Delta E}{E} &= \frac{1{,}16 \times 10^{-4}\,\text{eV}}{2{,}07\,\text{eV}} \\
&\approx 5{,}60 \times 10^{-5}
\end{aligned}
$$

Lấy vi phân hệ thức $E = hc/\lambda$, ta có $|\Delta E/E| = |\Delta\lambda/\lambda|$. Độ dịch chuyển bước sóng tương ứng là:

$$
\begin{aligned}
\Delta\lambda &\approx \lambda \frac{\Delta E}{E} \\
&\approx 0{,}034\,\text{nm}
\end{aligned}
$$

Vạch quang phổ ban đầu $\lambda = 600{,}000\,\text{nm}$ bị tách thành bộ ba vạch đối xứng:

Với các bước sóng tính bằng nanômét, vạch dịch về phía sóng ngắn là:

$$
\begin{aligned}
\lambda_1&=600{,}000-0{,}034\\
&=599{,}966\,\mathrm{nm}.
\end{aligned}
$$

Vạch không dịch chuyển có $\lambda_2=600{,}000\,\mathrm{nm}$. Vạch dịch về phía sóng dài là:

$$
\begin{aligned}
\lambda_3&=600{,}000+0{,}034\\
&=600{,}034\,\mathrm{nm}.
\end{aligned}
$$

#### Đánh giá kết quả

Mặc dù từ trường $2{,}00\,\text{T}$ là một từ trường tương đối mạnh trong điều kiện phòng thí nghiệm, độ tách bước sóng $\Delta\lambda = 0{,}034\,\text{nm}$ vẫn rất nhỏ. Tuy nhiên, các máy quang phổ hiện đại hoàn toàn có đủ độ phân giải sắc sai để đo đạc và định lượng chính xác độ tách vạch này.

#### Khái niệm cốt lõi

Một electron trong nguyên tử sở hữu mômen từ quỹ đạo khác không khi và chỉ khi electron ở trạng thái có mômen động lượng quỹ đạo khác không ($l > 0$). Khi nguyên tử được đặt trong một từ trường ngoài $\vec{B}$, năng lượng của electron phụ thuộc vào số lượng tử từ quỹ đạo $m_l$, số lượng tử này mô tả định hướng không gian của vector mômen từ so với vector cảm ứng từ $\vec{B}$.

### Quy tắc chọn lọc và hiệu ứng Zeeman thường

Khi cường độ từ trường ngoài $B$ tăng dần từ giá trị không, các mức năng lượng của một trạng thái có số lượng tử quỹ đạo xác định (chẳng hạn trạng thái $d$ với $l = 2$) sẽ tách dần ra theo quy luật tuyến tính với độ dốc tỷ lệ thuận với $m_l \mu_{\mathrm{B}}$. Khi $B = 0$, cả năm trạng thái $m_l = 0, \pm 1, \pm 2$ hoàn toàn suy biến ở cùng mức năng lượng $E_d$. Khi $B > 0$, từ trường làm xòe rộng các mức: Trạng thái $m_l = +2$ dịch lên cao nhất với $+2\mu_{\mathrm{B}} B$, trạng thái $m_l = +1$ dịch lên $+\mu_{\mathrm{B}} B$, trạng thái $m_l = 0$ không đổi, trạng thái $m_l = -1$ dịch xuống $-\mu_{\mathrm{B}} B$, và trạng thái $m_l = -2$ dịch xuống thấp nhất với $-2\mu_{\mathrm{B}} B$.

Xét chuyển dời từ $3d$ xuống $2p$. Từ trường tách mức $3d$ thành năm phân mức và mức $2p$ thành ba phân mức. Có 15 cặp mức đầu và cuối về mặt tổ hợp. Các điều kiện chọn sẽ giới hạn những cặp có thể tham gia chuyển dời.

Tuy nhiên, thực nghiệm chỉ quan sát thấy đúng ba vạch quang phổ phân biệt. Sự hạn chế này là hệ quả tất yếu của định luật bảo toàn mômen động lượng: Một photon phát xạ ra luôn mang một đơn vị mômen động lượng bằng $\hbar$. Quá trình hấp thụ hoặc phát xạ photon đòi hỏi các số lượng tử phải tuân theo các quy tắc chọn lọc nghiêm ngặt:

$$
\Delta l = \pm 1
$$

$$
\Delta m_l = 0 \text{ hoặc } \pm 1
$$

Các chuyển dời thỏa mãn các quy tắc trên được gọi là chuyển dời cho phép, còn các chuyển dời vi phạm được gọi là chuyển dời cấm.

![Hình 41.15: Chuyển dời từ 3d xuống 2p trong từ trường. Đường liền chỉ các chuyển dời được phép, còn đường đứt chỉ các chuyển dời không thỏa điều kiện chọn. Chín chuyển dời được phép tạo ba năng lượng photon khác nhau.](../img/young-41/hinh-41-15.png)

Quy ước dấu của độ biến thiên số lượng tử từ: Khi xét chuyển dời phát xạ từ trạng thái đầu ($i$) xuống trạng thái cuối ($f$), đặt $E_0 = E_i - E_f$ là năng lượng photon phát xạ khi chưa có từ trường ngoài. Nếu định nghĩa độ biến thiên theo chiều chuyển dời phát xạ là trạng thái đầu trừ trạng thái cuối:

$$
\Delta m_l = m_{l, i} - m_{l, f}
$$

thì năng lượng của photon phát xạ liên hệ trực tiếp với dấu của $\Delta m_l$ qua hệ thức:

$$
E_\gamma = E_0 + \Delta m_l \mu_{\mathrm{B}} B
$$

- Khi $\Delta m_l = 0$ (ba chuyển dời $m_l = 1 \to 1$, $0 \to 0$, $-1 \to -1$): Năng lượng photon phát xạ không bị dịch chuyển:

$$
E_\gamma = E_0
$$

- Khi $\Delta m_l = +1$ (ba chuyển dời $m_l = 2 \to 1$, $1 \to 0$, $0 \to -1$): Mức năng lượng đầu cao hơn, photon phát xạ có năng lượng lớn hơn một lượng $\Delta E$:

$$
E_\gamma = E_0 + \mu_{\mathrm{B}} B
$$

- Khi $\Delta m_l = -1$ (ba chuyển dời $m_l = 0 \to 1$, $-1 \to 0$, $-2 \to -1$): Mức năng lượng đầu thấp hơn, photon phát xạ có năng lượng nhỏ hơn một lượng $\Delta E$:

$$
E_\gamma = E_0 - \mu_{\mathrm{B}} B
$$

Ngược lại, nếu chọn quy ước chuẩn của giải tích là trạng thái cuối trừ trạng thái đầu ($\Delta m_l' = m_{l, f} - m_{l, i} = -\Delta m_l$), thì dấu trước số hạng dịch chuyển trong công thức photon sẽ đảo ngược: $E_\gamma = E_0 - \Delta m_l' \mu_{\mathrm{B}} B$. Dù sử dụng quy ước nào, chín chuyển dời cho phép giữa mức $3d$ và $2p$ luôn gom lại thành đúng ba giá trị năng lượng photon khác nhau, tương ứng với ba vạch quang phổ có khoảng cách đều đặn trên Hình 41.12. Hiện tượng này được gọi là hiệu ứng Zeeman thường. Lý thuyết này thuần túy dựa trên mômen động lượng quỹ đạo của electron. Ở mục tiếp theo, chúng ta sẽ thấy rằng electron còn sở hữu một dạng mômen động lượng nội tại gọi là spin, dẫn đến hiệu ứng Zeeman dị thường với số lượng vạch quang phổ phong phú hơn.

### Câu tự kiểm tra 41.4

Trong phân tích trên, chúng ta đã giả thiết từ trường ngoài $\vec{B}$ hướng dọc theo chiều dương của trục $z$. Các kết quả về sự tách mức năng lượng và sự tách vạch quang phổ có bị thay đổi hay không nếu từ trường ngoài hướng theo chiều dương của trục $x$?

::: details Lời giải chi tiết
Không. Các kết quả không thay đổi khi quay hướng từ trường từ trục $z$ sang trục $x$ trong bài toán nguyên tử cô lập đang xét.

Thế năng tương tác từ được xác định bởi tích vô hướng $U = -\vec{\mu}\cdot\vec{B}$, phụ thuộc duy nhất vào góc tương đối giữa vector mômen từ của electron và vector từ trường ngoài $\vec{B}$. Trong phần lý thuyết, chúng ta gọi thành phần mômen từ là $\mu_z$ đơn thuần vì chúng ta đã chủ động chọn quy ước toán học đặt trục $z$ trùng với hướng của vector $\vec{B}$.

Nếu từ trường hướng dọc theo trục $x$, chúng ta hoàn toàn có thể chọn trục lượng tử hóa hướng dọc theo trục $x$. Việc gán tên gọi cho các trục tọa độ trong không gian chỉ là một sự quy ước hình học tùy ý của người quan sát, không thể làm thay đổi các đại lượng đo đạc vật lý khách quan của nguyên tử.
:::
