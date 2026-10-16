## Bài tập trắc nghiệm theo ngữ cảnh (MCAT)

**Tìm hiểu cơ chế hoạt động của kỹ thuật PET (Looking Under the Hood of PET).** Trong phương pháp chẩn đoán hình ảnh chụp cắt lớp phát xạ positron (PET), bệnh nhân được tiêm các phân tử chứa những nguyên tử có hạt nhân dư thừa proton. Khi phân rã thành neutron, các proton này phát ra các hạt positron. Positron được phát ra chuyển động một quãng ngắn và chậm dần về vận tốc gần bằng không. Khi gặp một electron, chúng có thể hủy cặp lẫn nhau và phát ra hai photon chuyển động theo hai hướng ngược nhau. Bệnh nhân được đặt bao quanh bởi một mảng máy dò dạng vòng tròn, với mô cần ghi hình nằm ở tâm mảng máy dò. Nếu hai photon có mức năng lượng thích hợp đập vào hai máy dò đồng thời (trong khoảng thời gian $10\,\mathrm{ns}$), ta có thể kết luận rằng các photon này được tạo ra bởi sự hủy positron–electron ở một vị trí nào đó dọc theo đường thẳng nối hai máy dò. Bằng cách quan sát rất nhiều sự kiện đồng thời như vậy, ta có thể lập bản đồ phân bố các nguyên tử phát xạ positron trong mô. Tuy nhiên, các photon có thể bị hấp thụ hoặc tán xạ khi đi qua mô. Số lượng photon còn lại sau khi truyền qua một quãng đường $x$ trong mô được cho bởi công thức $N = N_0 \mathrm{e}^{-\mu x}$, trong đó $N_0$ là số photon ban đầu và $\mu$ là hệ số suy giảm, có giá trị xấp xỉ $0{,}1\,\mathrm{cm^{-1}}$ đối với các photon có năng lượng này. Chiết suất của mô sinh học đối với tia X là $1$.

### 44.57

Năng lượng của mỗi photon được tạo ra từ sự hủy cặp positron–electron bằng bao nhiêu?
(a) $\frac{1}{2} m_e v^2$, trong đó $v$ là tốc độ của positron phát ra;
(b) $m_e v^2$;
(c) $\frac{1}{2} m_e c^2$;
(d) $m_e c^2$.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Tính năng lượng của mỗi photon sinh ra khi một positron chậm hủy cặp với một electron đứng yên.

**Hướng đi:**

- **Trạng thái ban đầu:** Positron đã chậm dần về vận tốc gần bằng 0 trước khi hủy cặp. Do đó, động năng của electron và positron đều xấp xỉ bằng 0.
- **Bảo toàn năng lượng toàn phần:** Toàn bộ năng lượng nghỉ ban đầu chuyển hóa thành năng lượng của hai photon.
- **Bảo toàn động lượng:** Hai photon phát ra ngược chiều với độ lớn động lượng bằng nhau và mang năng lượng bằng nhau.

Trước khi hủy cặp, positron và electron đều có động năng không đáng kể so với năng lượng nghỉ:

$$
K \approx 0
$$

Tổng năng lượng ban đầu của hệ gồm hai hạt:

$$
\begin{aligned}
E_{\text{tot}} &= m_{e^+} c^2 + m_{e^-} c^2 \\
&= 2 m_e c^2
\end{aligned}
$$

Do hệ ban đầu gần như đứng yên, tổng động lượng của hệ xấp xỉ bằng 0. Để bảo toàn động lượng:

$$
\vec{p}_1 + \vec{p}_2 = \vec{0}
$$

Hai photon phát ra phải có độ lớn động lượng bằng nhau:

$$
p_1 = p_2
$$

Do năng lượng photon liên hệ với động lượng qua $E_\gamma = p c$, hai photon mang năng lượng bằng nhau:

$$
E_1 = E_2 = E_\gamma
$$

Áp dụng định luật bảo toàn năng lượng:

$$
2 E_\gamma = 2 m_e c^2
$$

Rút ra năng lượng của mỗi photon:

$$
E_\gamma = m_e c^2
$$

Với $m_e c^2 \approx 0{,}511\,\mathrm{MeV}$, mỗi photon gamma phát ra mang năng lượng đúng bằng năng lượng nghỉ của một electron.

**Đáp án đúng:** (d).

</details>

### 44.58

Giả sử sự hủy cặp positron–electron xảy ra trên đường nối hai máy dò, cách tâm đường nối một khoảng $3\,\mathrm{cm}$. Các photon tạo thành có được tính là đến các máy dò này đồng thời hay không?
(a) Không, vì độ chênh lệch thời gian đến nơi là $100\,\mathrm{ms}$;
(b) Không, vì độ chênh lệch thời gian là $200\,\mathrm{ms}$;
(c) Có, vì độ chênh lệch thời gian là $0{,}1\,\mathrm{ns}$;
(d) Có, vì độ chênh lệch thời gian là $0{,}2\,\mathrm{ns}$.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Vị trí hủy cặp lệch khỏi tâm $d_0 = 3\,\mathrm{cm}$. Kiểm tra xem hiệu thời gian truyền photon tới hai máy dò đối diện có nằm trong cửa sổ trùng phùng $10\,\mathrm{ns}$ hay không.

**Hướng đi:**

- **Hiệu quang trình:** Tính độ lệch đường truyền giữa hai photon đến hai đầu máy dò.
- **Vận tốc truyền sóng:** Với chiết suất mô sinh học $n = 1$, tốc độ truyền là tốc độ ánh sáng trong chân không $c$.
- **Độ trễ thời gian:** $\Delta t = \Delta d / c$.
- **Điều kiện trùng phùng:** So sánh $\Delta t$ với khoảng thời gian đồng thời quy ước ($10\,\mathrm{ns}$).

Gọi $L$ là khoảng cách từ tâm mảng máy dò đến mỗi máy dò đối diện. Điểm hủy cặp nằm lệch tâm một đoạn:

$$
\Delta x = 3\,\mathrm{cm} = 0{,}03\,\mathrm{m}
$$

Khoảng cách từ điểm hủy cặp đến hai máy dò lần lượt là:

$$
\begin{aligned}
d_1 &= L - \Delta x \\
d_2 &= L + \Delta x
\end{aligned}
$$

Hiệu quãng đường truyền của hai photon là:

$$
\begin{aligned}
\Delta d &= d_2 - d_1 \\
&= 2 \Delta x \\
&= 0{,}06\,\mathrm{m}
\end{aligned}
$$

Vì chiết suất của mô sinh học đối với bức xạ này bằng $1$, tốc độ truyền sóng là $c = 3{,}00 \times 10^8\,\mathrm{m/s}$. Độ chênh lệch thời gian đến hai máy dò:

$$
\begin{aligned}
\Delta t &= \frac{\Delta d}{c} \\
&= \frac{0{,}06}{3{,}00 \times 10^8} \\
&= 2{,}0 \times 10^{-10}\,\mathrm{s} \\
&= 0{,}2\,\mathrm{ns}
\end{aligned}
$$

Vì $\Delta t = 0{,}2\,\mathrm{ns} \le 10\,\mathrm{ns}$, hai tín hiệu rơi vào bên trong cửa sổ thời gian $10\,\mathrm{ns}$ và được hệ thống máy tính ghi nhận là hai biến cố đồng thời.

**Đáp án đúng:** (d).

</details>

### 44.59

Nếu các photon hủy cặp phát ra từ một phần của cơ thể cách máy dò $20\,\mathrm{cm}$ mô sinh học, thì tỉ lệ phần trăm photon ban đầu truyền về phía máy dò còn lại sau khi đi qua mô là bao nhiêu?
(a) $1{,}4\%$;
(b) $8{,}6\%$;
(c) $14\%$;
(d) $86\%$.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Bề dày mô sinh học là $x = 20\,\mathrm{cm}$, hệ số suy giảm là $\mu = 0{,}1\,\mathrm{cm^{-1}}$. Tính phần trăm số photon truyền qua lớp mô này.

**Hướng đi:**

- **Định luật hấp thụ bức xạ:** $N = N_0 \mathrm{e}^{-\mu x}$.
- **Tỉ số truyền qua:** Lập tỉ số $N / N_0 = \mathrm{e}^{-\mu x}$ rồi quy đổi sang phần trăm.

![Minh họa bài 44.59: Sự suy giảm photon PET theo hàm mũ qua bề dày mô sinh học](./img/young-44/loi-giai-d-07.svg)

Độ suy giảm số lượng photon tuân theo hàm mũ:

$$
N = N_0 \mathrm{e}^{-\mu x}
$$

Số mũ suy giảm với $\mu = 0{,}1\,\mathrm{cm^{-1}}$ và $x = 20\,\mathrm{cm}$:

$$
\begin{aligned}
\mu x &= 0{,}1 \times 20 \\
&= 2{,}0
\end{aligned}
$$

Tỉ số photon còn lại sau khi xuyên qua bề dày mô:

$$
\begin{aligned}
\frac{N}{N_0} &= \mathrm{e}^{-2{,}0} \\
&\approx 0{,}1353
\end{aligned}
$$

Quy đổi sang phần trăm:

$$
\frac{N}{N_0} \times 100\% \approx 13{,}5\%
$$

Làm tròn đến chữ số có nghĩa thích hợp theo các phương án đề bài, ta được giá trị $14\%$.

**Đáp án đúng:** (c).

</details>
