## Bài tập đoạn văn theo định dạng MCAT: Chấm lượng tử (Quantum Dots)

### Đoạn văn mở đầu

**Chấm lượng tử (Quantum Dots)**. Chấm lượng tử là một loại tinh thể bán dẫn có kích thước nhỏ đến mức các hiệu ứng cơ học lượng tử đóng vai trò chi phối rõ rệt. Một ứng dụng quan trọng của chấm lượng tử là trong kỹ thuật chụp ảnh huỳnh quang y sinh học, trong đó chấm lượng tử được liên kết hóa học với một phân tử hoặc cấu trúc tế bào cần quan sát. Khi chấm lượng tử được chiếu sáng, nó hấp thụ các photon kích thích và sau đó tái phát xạ các photon ở một bước sóng khác dài hơn. Hiện tượng này được gọi là sự phát huỳnh quang. Bước sóng mà chấm lượng tử phát ra khi được kích thích phụ thuộc trực tiếp vào kích thước hình học của tinh thể, do đó có thể điều chỉnh phổ hấp thụ và phát xạ bằng cách chọn kích thước tinh thể trong phạm vi vật liệu cho phép.

Chúng ta có thể thấu hiểu nhiều tính chất cơ bản của chấm lượng tử thông qua mô hình đơn giản: Một hạt có khối lượng $M$ (xấp xỉ khối lượng của electron) bị giam cầm bên trong một hộp vuông cứng hai chiều có cạnh bằng $L$. Trong mô hình này, các mức năng lượng của chấm lượng tử được cho bởi

$$
E_{m, n} = (m^2 + n^2)\frac{\pi^2 \hbar^2}{2ML^2}
$$

trong đó $m$ và $n$ là các số nguyên dương độc lập ($m, n = 1, 2, 3, \dots$).

---

### 40.67

Theo mô hình này, phát biểu nào sau đây là đúng về khoảng cách giữa các mức năng lượng của các chấm lượng tử có kích thước khác nhau?
(a) Các chấm nhỏ hơn có các mức năng lượng cách đều nhau, nhưng các chấm lớn hơn có các mức năng lượng ngày càng xa nhau khi năng lượng tăng.
(b) Các chấm lớn hơn có khoảng cách giữa các mức năng lượng lớn hơn so với các chấm nhỏ hơn.
(c) Các chấm nhỏ hơn có khoảng cách giữa các mức năng lượng lớn hơn so với các chấm lớn hơn.
(d) Khoảng cách giữa các mức năng lượng hoàn toàn độc lập với kích thước của chấm lượng tử.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** So sánh khoảng cách mức năng lượng $\Delta E$ giữa các chấm lượng tử kích thước khác nhau dựa vào biểu thức $E_{m, n} = (m^2 + n^2)\frac{\pi^2 \hbar^2}{2ML^2}$.

**Hướng đi:**

- **Phụ thuộc vào kích thước hộp**: Mức năng lượng và độ chênh lệch năng lượng $\Delta E$ tỉ lệ nghịch với bình phương cạnh hộp: $\Delta E \propto \frac{1}{L^2}$.
- **Quy luật kích thước**: Khi cạnh $L$ giảm (chấm nhỏ hơn), giá trị $\frac{1}{L^2}$ tăng lên, kéo theo khoảng cách giữa các mức năng lượng tăng lên.

Từ công thức mức năng lượng của hạt trong giếng vuông hai chiều:

$$
\begin{aligned}
E_{m, n} &= (m^2 + n^2)E_0, \\
E_0 &= \frac{\pi^2 \hbar^2}{2ML^2}.
\end{aligned}
$$

Độ chênh lệch năng lượng giữa hai trạng thái bất kỳ $(m_1, n_1)$ và $(m_2, n_2)$ với $\Delta K = (m_2^2 + n_2^2) - (m_1^2 + n_1^2)$ là:

$$
\begin{aligned}
\Delta E &= \Delta K \cdot E_0 \\
&= \Delta K \frac{\pi^2 \hbar^2}{2ML^2}.
\end{aligned}
$$

Biểu thức này cho thấy với cùng một bước chuyển mức lượng tử, $\Delta E$ tỉ lệ nghịch với bình phương kích thước hình học $L$ của chấm lượng tử:

$$
\Delta E \propto \frac{1}{L^2}.
$$

- Chấm lượng tử có kích thước càng nhỏ ($L$ nhỏ) thì mẫu số càng bé, dẫn đến khoảng cách giữa các mức năng lượng $\Delta E$ càng lớn.
- Ngược lại, chấm lượng tử có kích thước càng lớn ($L$ lớn) thì khoảng cách giữa các mức năng lượng càng bị thu hẹp lại.

Do đó, phát biểu chính xác là: **Các chấm nhỏ hơn có khoảng cách giữa các mức năng lượng lớn hơn so với các chấm lớn hơn**.

**Đáp án đúng:** **(c)**.

</details>

### 40.68

Khi một chấm lượng tử cho trước có chiều dài cạnh $L$ thực hiện bước chuyển từ trạng thái kích thích thứ nhất xuống trạng thái cơ bản, nó phát ra ánh sáng màu xanh lục có bước sóng $550\,\mathrm{nm}$. Nếu thay vào đó, một chấm lượng tử có chiều dài cạnh $1{,}1L$ được sử dụng, bước sóng ánh sáng phát ra trong cùng bước chuyển này theo mô hình bằng bao nhiêu?
(a) $600\,\mathrm{nm}$.
(b) $670\,\mathrm{nm}$.
(c) $500\,\mathrm{nm}$.
(d) $460\,\mathrm{nm}$.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Chấm cạnh $L$ phát photon $\lambda = 550\,\mathrm{nm}$ khi chuyển từ mức kích thích 1 về mức cơ bản. Tìm $\lambda'$ của chấm có cạnh $L' = 1{,}1L$ trong cùng bước chuyển.

**Hướng đi:**

- **Xác định mức năng lượng cơ bản và kích thích 1**: Mức cơ bản là $(1, 1)$, mức kích thích thứ nhất là $(1, 2)$ hoặc $(2, 1)$.
- **Hiệu năng lượng**: $\Delta E = (5 - 2)E_0 = 3E_0$ với $E_0 = \frac{\pi^2\hbar^2}{2ML^2}$.
- **Mối liên hệ giữa bước sóng và kích thước**: $\lambda = \frac{hc}{\Delta E} \propto L^2$.

Xét bước chuyển từ trạng thái kích thích thứ nhất về trạng thái cơ bản:
- Trạng thái cơ bản $(1, 1)$ có $m^2 + n^2 = 1^2 + 1^2 = 2$.
- Trạng thái kích thích thứ nhất $(1, 2)$ hoặc $(2, 1)$ có $m^2 + n^2 = 1^2 + 2^2 = 5$.
Độ chênh lệch năng lượng là

$$
\begin{aligned}
\Delta E &= (5 - 2)E_0 \\
&= 3E_0 = \frac{3\pi^2 \hbar^2}{2ML^2}.
\end{aligned}
$$

Năng lượng photon phát xạ liên hệ với bước sóng qua hệ thức Planck–Einstein:

$$
\begin{aligned}
\lambda &= \frac{hc}{\Delta E} \\
&= \frac{2 M c h}{3\pi^2 \hbar^2} L^2.
\end{aligned}
$$

Như vậy, bước sóng phát xạ tỉ lệ thuận với bình phương kích thước cạnh của chấm lượng tử:

$$
\lambda \propto L^2.
$$

Khi chiều dài cạnh tăng lên thành $L' = 1{,}1L$, bước sóng mới $\lambda'$ thỏa mãn:

$$
\begin{aligned}
\frac{\lambda'}{\lambda} &= \left(\frac{L'}{L}\right)^2 \\
&= (1{,}1)^2 = 1{,}21.
\end{aligned}
$$

Thay giá trị bước sóng ban đầu $\lambda = 550\,\mathrm{nm}$:

$$
\begin{aligned}
\lambda' &= 1{,}21 \times 550\,\mathrm{nm} \\
&= 665{,}5\,\mathrm{nm} \approx 670\,\mathrm{nm}.
\end{aligned}
$$

Bức xạ dịch chuyển về phía vùng ánh sáng đỏ.

**Đáp án đúng:** **(b)**.

</details>

### 40.69

So sánh các chấm lượng tử có cùng kích thước nhưng được chế tạo từ các vật liệu bán dẫn khác nhau. Trong cùng một bước chuyển mức, một chấm làm bằng vật liệu 1 phát ra photon có bước sóng dài hơn so với photon phát ra từ chấm làm bằng vật liệu 2. Dựa trên mô hình này, nguyên nhân nào sau đây là một giải thích hợp lý?
(a) Khối lượng của hạt bị giam giữ trong vật liệu 1 lớn hơn.
(b) Khối lượng của hạt bị giam giữ trong vật liệu 2 lớn hơn.
(c) Các hạt bị giam giữ thực hiện nhiều bước chuyển hơn mỗi giây trong vật liệu 1.
(d) Các hạt bị giam giữ thực hiện nhiều bước chuyển hơn mỗi giây trong vật liệu 2.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Hai chấm cùng kích thước $L$. Khi chuyển mức, $\lambda_1 > \lambda_2$. Tìm nguyên nhân vật lý liên quan đến khối lượng hạt tải $M$.

**Hướng đi:**

- **Mối liên hệ giữa bước sóng và khối lượng**: $\Delta E \propto \frac{1}{M} \implies \lambda = \frac{hc}{\Delta E} \propto M$.
- **So sánh $\lambda$**: Bước sóng dài hơn tương ứng với độ chênh lệch năng lượng nhỏ hơn và khối lượng hiệu dụng lớn hơn.

Theo mô hình chấm lượng tử, độ chênh lệch năng lượng của một bước chuyển nhất định được cho bởi

$$
\Delta E = \Delta(m^2 + n^2)\frac{\pi^2 \hbar^2}{2ML^2}.
$$

Với hai chấm có cùng kích thước $L$ và cùng bước chuyển trạng thái lượng tử, $\Delta E$ tỉ lệ nghịch với khối lượng hiệu dụng $M$ của hạt tải:

$$
\Delta E \propto \frac{1}{M}.
$$

Bước sóng của photon phát ra tỉ lệ nghịch với hiệu năng lượng:

$$
\lambda = \frac{hc}{\Delta E} \propto M.
$$

Do đó, bước sóng photon phát xạ tỉ lệ thuận với khối lượng $M$ của hạt bị giam giữ trong tinh thể.
- Đề bài cho biết chấm làm bằng vật liệu 1 phát ra photon có bước sóng dài hơn chấm làm bằng vật liệu 2 ($\lambda_1 > \lambda_2$).
- Điều này tương đương với việc độ chênh lệch năng lượng của bước chuyển trong vật liệu 1 nhỏ hơn trong vật liệu 2 ($\Delta E_1 < \Delta E_2$).
- Do đó, khối lượng hiệu dụng của hạt tải bị giam cầm trong vật liệu 1 bắt buộc phải lớn hơn khối lượng tương ứng trong vật liệu 2 ($M_1 > M_2$).

**Đáp án đúng:** **(a)**.

</details>

### 40.70

Một ưu điểm của chấm lượng tử là so với nhiều vật liệu huỳnh quang hữu cơ khác, các trạng thái kích thích của nó có thời gian sống tương đối dài (khoảng $10\,\mathrm{ns}$). Điều này mang lại ý nghĩa gì đối với độ tán xòe năng lượng của các photon phát ra bởi chấm lượng tử?
(a) Chấm lượng tử phát ra các photon có mức năng lượng được xác định rõ ràng hơn so với các vật liệu huỳnh quang khác.
(b) Chấm lượng tử phát ra các photon có mức năng lượng kém xác định hơn so với các vật liệu huỳnh quang khác.
(c) Độ tán xòe năng lượng chỉ bị ảnh hưởng bởi kích thước của chấm, chứ không phụ thuộc vào thời gian sống.
(d) Năng lượng của các photon phát ra không hề có độ bất định nào, bất kể thời gian sống là bao nhiêu.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Đánh giá ảnh hưởng của thời gian sống trạng thái kích thích dài ($\tau \approx 10\,\mathrm{ns}$) lên độ rộng vạch phổ năng lượng $\Delta E$ của photon phát xạ.

**Hướng đi:**

- **Hệ thức bất định Heisenberg năng lượng – thời gian**: $\Delta E \cdot \Delta t \ge \hbar/2$.
- **Độ rộng vạch phổ tự nhiên**: $\Delta E \approx \frac{\hbar}{\tau}$.
- **Ý nghĩa độ tán xòe**: Thời gian sống $\tau = \Delta t$ càng lớn thì độ bất định năng lượng $\Delta E$ càng nhỏ, nghĩa là mức năng lượng càng sắc nét và xác định rõ ràng.

Theo hệ thức bất định Heisenberg đối với năng lượng và thời gian:

$$
\Delta E \cdot \Delta t \ge \frac{\hbar}{2}.
$$

Trong quá trình phát xạ lượng tử, thời gian sống $\tau$ đặt thang thời gian suy giảm của biên độ trạng thái. Độ rộng vạch tự nhiên có bậc độ lớn $\hbar/\tau$. Nếu định nghĩa độ rộng bằng bề rộng toàn phần ở nửa cực đại của vạch Lorentz thì $\Gamma=\hbar/\tau$.
Độ rộng phổ tự nhiên (độ tán xòe hay độ bất định về năng lượng của photon phát ra) được ước tính bởi

$$
\Delta E \approx \frac{\hbar}{\tau}.
$$

- Khi thời gian sống $\tau$ của trạng thái kích thích càng dài ($\tau \approx 10\,\mathrm{ns}$, tương đối dài so với các vật liệu đang được so sánh), mẫu số càng lớn làm cho độ bất định năng lượng $\Delta E$ càng nhỏ.
- Độ bất định năng lượng nhỏ đồng nghĩa với việc năng lượng của các photon phát xạ tập trung rất hẹp quanh tần số trung tâm, độ rộng vạch tự nhiên nhỏ hơn. Trong một mẫu thực, tương tác với môi trường và phân bố kích thước chấm còn có thể làm vạch rộng thêm.

**Đáp án đúng:** **(a)**.

</details>
