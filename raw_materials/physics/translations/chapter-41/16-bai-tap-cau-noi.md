## Bài tập cầu nối: Mô hình nguyên tử nhiều electron trong hộp (A Many-Electron Atom in a Box)

### Bài tập cầu nối

Một nguyên tử titan mang $22$ electron và có bán kính nguyên tử bằng $1{,}47 \times 10^{-10}\,\mathrm{m}$. Xét một hộp lập phương cứng có thể tích bằng đúng thể tích của nguyên tử titan này.

(a) Kích thước các cạnh của chiếc hộp lập phương này bằng bao nhiêu?

(b) Xác định các số lượng tử $n_X, n_Y, n_Z$ và $m_s$ cho trạng thái của từng electron trong số $22$ electron ở trạng thái cơ bản của “nguyên tử” hình hộp lập phương này. (Gợi ý: Tham khảo Hình 41.4 trong bài học để xác định một số mức năng lượng đầu tiên của hộp lập phương so với mức cơ bản $E_{1,1,1}$.)

(c) Tìm năng lượng của từng mức năng lượng mà các electron chiếm giữ. (Bỏ qua tương tác lực điện từ giữa các electron với nhau.)

(d) Giả sử bạn bứt một trong các electron ở mức năng lượng thấp nhất ra khỏi hộp. Kết quả là một trong các electron từ mức năng lượng bị chiếm cao nhất nhảy xuống mức thấp nhất để lấp đầy lỗ trống, đồng thời phát xạ một photon trong quá trình dịch chuyển này. Năng lượng của photon phát ra bằng bao nhiêu? Giá trị này so với năng lượng của photon tia X $K_\alpha$ của titanium dự đoán theo định luật Moseley như thế nào?

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Khảo sát mô hình gián tiếp của nguyên tử titan ($Z = 22$, $R = 1{,}47 \times 10^{-10}\,\mathrm{m}$) dưới dạng $22$ electron độc lập bị giam cầm trong hộp lập phương có cùng thể tích $V = \frac{4}{3}\pi R^3 = L^3$.
(a) Tìm chiều dài cạnh hộp $L$.
(b) Liệt kê bộ bốn số lượng tử $(n_X, n_Y, n_Z, m_s)$ của $22$ electron ở trạng thái cơ bản.
(c) Tính trị số năng lượng của các mức bị chiếm.
(d) Tính năng lượng photon phát ra khi electron từ mức cao nhất nhảy xuống lấp lỗ trống mức thấp nhất và so sánh với photon $K_\alpha$ theo định luật Moseley.

**Hướng đi:**

- **Hình học không gian**: Đồng nhất thể tích hình cầu của nguyên tử với thể tích hình lập phương: $L = (4\pi/3)^{1/3} R$.
- **Mức năng lượng hạt trong hộp ba chiều**: Năng lượng trạng thái dừng là $E = K E_0$ với hằng số tỉ lệ $E_0 = \frac{\pi^2 \hbar^2}{2m_e L^2}$.
- **Nguyên lý loại trừ Pauli**: Mỗi trạng thái không gian $(n_X, n_Y, n_Z)$ chứa tối đa $2$ electron ứng với hai chiều spin $m_s = \pm 1/2$. Sắp xếp lần lượt $22$ electron vào các mức có tổng bình phương $K = n_X^2 + n_Y^2 + n_Z^2$ từ thấp lên cao.
- **Bảo toàn năng lượng phát xạ**: Năng lượng photon phát ra bằng hiệu mức năng lượng: $E_{\mathrm{photon}} = E_{\mathrm{cao}} - E_{\mathrm{thấp}}$.
- **Định luật Moseley:** Dùng tần số $f=C(Z-1)^2$, với $C=2{,}48\times10^{15}\,\mathrm{Hz}$, rồi tính năng lượng photon bằng $E=hf$. Mô hình che chắn đơn giản còn cho ước lượng năng lượng khoảng $10{,}2(Z-1)^2\,\mathrm{eV}$.

---

#### Hướng dẫn giải chi tiết

#### Nhận diện và thiết lập (Identify and Set Up)

1. Bài toán kết hợp mô hình hạt trong hộp thế lập phương ba chiều với nguyên lý loại trừ Pauli để xây dựng cấu hình electron cho một hệ nhiều hạt giam cầm. Sau đó, hiện tượng phát xạ photon khi lấp lỗ trống lớp trong được đối chiếu trực tiếp với cơ chế phát xạ phổ tia X đặc trưng $K_\alpha$ và định luật Moseley.

2. Các đại lượng mục tiêu cần xác định gồm:
   - Chiều dài cạnh hộp lập phương $L$.
   - Cấu hình trạng thái lượng tử của $22$ electron biểu diễn qua bộ bốn số lượng tử $(n_X, n_Y, n_Z, m_s)$.
   - Năng lượng của các mức lượng tử tương ứng theo đơn vị electronvolt ($\mathrm{eV}$).
   - Năng lượng photon phát xạ và mức độ chênh lệch so với giá trị thực tế của vạch phổ $K_\alpha$.

#### Thực hiện giải toán (Execute)

3. **Xác định kích thước cạnh hộp lập phương (Ý a)**:
Thể tích của nguyên tử titan hình cầu bán kính $R = 1{,}47 \times 10^{-10}\,\mathrm{m}$ là:

$$
V = \frac{4}{3}\pi R^3.
$$

Vì hộp lập phương có thể tích đúng bằng thể tích nguyên tử:

$$
L^3 = \frac{4}{3}\pi R^3.
$$

Với bán kính $R = 1{,}47 \times 10^{-10}\,\mathrm{m}$ và $(4\pi/3)^{1/3} \approx 1{,}612$, suy ra chiều dài mỗi cạnh của hộp lập phương:

$$
\begin{aligned}
L
&= \left(\frac{4\pi}{3}\right)^{1/3} R \\
&\approx 2{,}37 \times 10^{-10}\,\mathrm{m}.
\end{aligned}
$$

4. **Xác định các mức năng lượng và cấu hình $22$ electron (Ý b)**:
Năng lượng của một hạt electron khối lượng $m_e$ bị giam giữ trong hộp lập phương ba chiều có cạnh $L$ với mức năng lượng cơ sở $E_0$:

$$
E_0 = \frac{\pi^2 \hbar^2}{2m_e L^2}.
$$

Năng lượng của trạng thái $(n_X, n_Y, n_Z)$ là:

$$
E = (n_X^2 + n_Y^2 + n_Z^2) E_0.
$$

Tính giá trị số của $E_0$ với $L \approx 2{,}37 \times 10^{-10}\,\mathrm{m}$:

$$
\begin{aligned}
E_0
&= \frac{\pi^2 \hbar^2}{2m_e L^2} \\
&\approx 1{,}072 \times 10^{-18}\,\mathrm{J} \\
&\approx 6{,}70\,\mathrm{eV}.
\end{aligned}
$$

Mỗi tổ hợp các số nguyên dương $(n_X, n_Y, n_Z)$ xác định một hàm sóng không gian. Do electron mang spin $s = 1/2$, mỗi trạng thái không gian có thể tiếp nhận đúng $2$ electron mang hai hướng spin trái dấu: $m_s = +1/2$ và $m_s = -1/2$.

Để hệ đạt trạng thái cơ bản có tổng năng lượng cực tiểu, các electron sẽ lần lượt chiếm giữ các mức có giá trị tổng bình phương $K = n_X^2 + n_Y^2 + n_Z^2$ từ nhỏ đến lớn:

- Mức cơ bản $K = 1^2 + 1^2 + 1^2 = 3$: Gồm duy nhất $1$ trạng thái không gian $(1, 1, 1)$. Mức này chứa tối đa $2$ electron:

$$
(1, 1, 1, \pm 1/2).
$$

Số electron tích lũy: $2$ electron.

- Mức kích thích thứ nhất $K = 2^2 + 1^2 + 1^2 = 6$: Gồm $3$ trạng thái không gian suy biến hoán vị $(2, 1, 1)$, $(1, 2, 1)$, $(1, 1, 2)$. Mức này chứa tối đa $3 \times 2 = 6$ electron:

$$
\begin{aligned}
&(2, 1, 1, \pm 1/2), \\
&(1, 2, 1, \pm 1/2), \\
&(1, 1, 2, \pm 1/2).
\end{aligned}
$$

Số electron tích lũy: $2 + 6 = 8$ electron.

- Mức kích thích thứ hai $K = 2^2 + 2^2 + 1^2 = 9$: Gồm $3$ trạng thái không gian $(2, 2, 1)$, $(2, 1, 2)$, $(1, 2, 2)$. Mức này chứa tối đa $3 \times 2 = 6$ electron:

$$
\begin{aligned}
&(2, 2, 1, \pm 1/2), \\
&(2, 1, 2, \pm 1/2), \\
&(1, 2, 2, \pm 1/2).
\end{aligned}
$$

Số electron tích lũy: $8 + 6 = 14$ electron.

- Mức kích thích thứ ba $K = 3^2 + 1^2 + 1^2 = 11$: Gồm $3$ trạng thái không gian $(3, 1, 1)$, $(1, 3, 1)$, $(1, 1, 3)$. Mức này chứa tối đa $3 \times 2 = 6$ electron:

$$
\begin{aligned}
&(3, 1, 1, \pm 1/2), \\
&(1, 3, 1, \pm 1/2), \\
&(1, 1, 3, \pm 1/2).
\end{aligned}
$$

Số electron tích lũy: $14 + 6 = 20$ electron.

- Mức kích thích thứ tư $K = 2^2 + 2^2 + 2^2 = 12$: Gồm duy nhất $1$ trạng thái không gian $(2, 2, 2)$. Để đủ tổng số $22$ electron của nguyên tử titan, $2$ electron cuối cùng sẽ chiếm trọn vẹn mức này:

$$
(2, 2, 2, \pm 1/2).
$$

Số electron tích lũy: $20 + 2 = 22$ electron. Mức năng lượng này vừa vặn được lấp đầy hoàn toàn.

5. **Năng lượng của từng mức bị chiếm (Ý c)**:
Sử dụng giá trị cơ sở $E_0 \approx 6{,}692\,\mathrm{eV}$ (hoặc làm tròn tiêu chuẩn $6{,}70\,\mathrm{eV}$), năng lượng của $5$ mức lượng tử bị chiếm lần lượt là:

$$
\begin{aligned}
&E_1 = 3E_0 \approx 20{,}1\,\mathrm{eV}, \\
&E_2 = 6E_0 \approx 40{,}2\,\mathrm{eV}, \\
&E_3 = 9E_0 \approx 60{,}3\,\mathrm{eV}, \\
&E_4 = 11E_0 \approx 73{,}7\,\mathrm{eV}, \\
&E_5 = 12E_0 \approx 80{,}4\,\mathrm{eV}.
\end{aligned}
$$

![Hình 41.B: Sơ đồ 5 mức năng lượng bị chiếm bởi 22 electron của nguyên tử Titan trong mô hình hộp thế lập phương và bước chuyển phát xạ photon 60,3 eV khi lấp lỗ trống mức cơ bản.](./img/young-41/loi-giai-d-10.svg)

6. **Năng lượng photon phát xạ và so sánh với định luật Moseley (Ý d)**:
Khi một electron ở mức thấp nhất $(1, 1, 1)$ bị bứt ra ngoài, một electron từ mức cao nhất bị chiếm $(2, 2, 2)$ nhảy xuống lấp lỗ trống. Năng lượng của photon phát xạ bằng độ chênh lệch năng lượng giữa hai mức này:

$$
\begin{aligned}
E_{\mathrm{photon}} &= E_{2,2,2} - E_{1,1,1} \\
&= 12E_0 - 3E_0 \\
&= 9E_0 \\
&= 9 \times 6{,}692\,\mathrm{eV} \\
&\approx 60{,}3\,\mathrm{eV}.
\end{aligned}
$$

Với nguyên tử titan có $Z=22$, định luật Moseley cho tần số vạch $K_\alpha$. Đặt $C=2{,}48\times10^{15}\,\mathrm{Hz}$:

$$
\begin{aligned}
f_{\rm M}&=C(Z-1)^2\\
&\approx1{,}094\times10^{18}\,\mathrm{Hz}.
\end{aligned}
$$

Năng lượng photon tương ứng là:

$$
\begin{aligned}
E_{\rm M}&=hf_{\rm M}\\
&\approx4{,}52\,\mathrm{keV}.
\end{aligned}
$$

Mô hình che chắn đơn giản với $Z_{\rm eff}=21$ còn cho ước lượng:

$$
\begin{aligned}
E_{K_\alpha}&\approx21^2(10{,}2\,\mathrm{eV})\\
&\approx4{,}50\,\mathrm{keV}.
\end{aligned}
$$

Hai con số khác nhau do hệ số thực nghiệm Moseley và mô hình che chắn chỉ gần trùng nhau. Sự khác biệt nhỏ ấy không làm thay đổi so sánh với photon của hộp thế.

So sánh hai kết quả:

$$
\frac{E_{K_\alpha}}{E_{\mathrm{photon}}} \approx \frac{4\,520\,\mathrm{eV}}{60{,}3\,\mathrm{eV}} \approx 75.
$$

Năng lượng photon phát ra trong mô hình hộp lập phương nhỏ hơn giá trị thực tế của vạch tia X $K_\alpha$ tới $75$ lần.

#### Đánh giá và thảo luận (Evaluate)

7. **Mô hình nguyên tử hình hộp có phải là một mô hình hữu ích cho titan hay không?**
   - Về mặt định tính: Mô hình này rất trực quan và bổ ích trong việc minh họa nguyên lý loại trừ Pauli, quy tắc lấp đầy các orbital lượng tử độc lập, sự hình thành các vỏ năng lượng đóng kín và độ suy biến trạng thái do tính đối xứng không gian.
   - Về mặt định lượng: Mô hình không tái hiện được thang năng lượng tia X của titan. Hạt nhân thực mang điện tích $+Ze=+22e$ và tạo thế Coulomb $-Ze^2/(4\pi\varepsilon_0r)$. Các electron vỏ trong tập trung gần hạt nhân và có năng lượng liên kết tới hàng nghìn electronvolt. Trong hộp vô hạn, thế năng bên trong bằng không ở mọi vị trí, nên thiếu cơ chế liên kết này.

8. **Ước lượng độ lớn tương tác đẩy tĩnh điện giữa hai electron**:
Để đánh giá việc bỏ qua tương tác tĩnh điện giữa các electron trong đề bài có phải là một phép xấp xỉ tốt hay không, ta ước tính thế năng đẩy Coulomb giữa hai electron đặt cách nhau một khoảng bằng một nửa kích thước hộp:

$$
r_{12} = \frac{L}{2} \approx 1{,}185 \times 10^{-10}\,\mathrm{m}
$$

Thế năng đẩy tĩnh điện giữa hai điện tích nguyên tố này với $e^2 / (4\pi\varepsilon_0) \approx 2{,}307 \times 10^{-28}\,\mathrm{J\cdot m}$ là:

$$
\begin{aligned}
U_{\mathrm{Coulomb}}
&= \frac{1}{4\pi\varepsilon_0}\frac{e^2}{r_{12}} \\
&\approx 1{,}947 \times 10^{-18}\,\mathrm{J} \\
&\approx 12{,}2\,\mathrm{eV}.
\end{aligned}
$$

So sánh năng lượng tương tác đẩy $U_{\mathrm{Coulomb}} \approx 12{,}2\,\mathrm{eV}$ này với khoảng cách giữa các mức năng lượng đã tính ở bước 5:
- Độ chênh lệch giữa các mức là $\Delta E_{1\to 2} \approx 20{,}1\,\mathrm{eV}$.
- $\Delta E_{2\to 3} \approx 20{,}1\,\mathrm{eV}$.
- $\Delta E_{3\to 4} \approx 13{,}4\,\mathrm{eV}$.
- $\Delta E_{4\to 5} \approx 6{,}7\,\mathrm{eV}$.

Năng lượng đẩy ước tính $12{,}2\,\mathrm{eV}$ cùng bậc với các khoảng cách mức, trong đó có những khoảng chỉ $6{,}7\,\mathrm{eV}$ hoặc $13{,}4\,\mathrm{eV}$. Vì vậy, không có tham số nhỏ để biện minh việc bỏ tương tác này trong phép tính định lượng đang xét. Ước lượng trên chưa xác định chi tiết các mức sẽ dịch chuyển và sắp xếp lại như thế nào.

</details>
