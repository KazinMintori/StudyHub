## Bài tập cầu nối: Bó sóng trong hộp (A Packet in a Box)

### Bài tập cầu nối

Một hạt có khối lượng $m$ trong giếng thế vuông vô hạn (xem Hình 40.9) có hàm sóng trong miền từ $x = 0$ đến $x = L$ được cho bởi

$$
\begin{aligned}
\Psi(x, t) &= \frac{\Psi_1 + \Psi_2}{\sqrt{2}}, \\
\Psi_n(x, t) &= \psi_n(x)e^{-iE_n t/\hbar}.
\end{aligned}
$$

Trong đó $\psi_1(x)$ và $\psi_2(x)$ là các hàm sóng trạng thái dừng đã được chuẩn hóa của hai mức năng lượng đầu tiên ($n = 1$ và $n = 2$), cho bởi phương trình $\psi_n(x) = \sqrt{\frac{2}{L}}\sin\left(\frac{n\pi x}{L}\right)$. Các năng lượng $E_1$ và $E_2$ tuân theo phương trình $E_n = n^2 \frac{\pi^2 \hbar^2}{2mL^2}$. Hàm sóng bằng 0 khi $x < 0$ và khi $x > L$.
(a) Tìm hàm phân bố xác suất $|\Psi(x, t)|^2$ ứng với hàm sóng này.
(b) Hàm sóng $\Psi(x, t)$ có đại diện cho một trạng thái dừng có năng lượng xác định hay không? Làm thế nào bạn nhận biết được điều đó?
(c) Chứng minh rằng hàm sóng $\Psi(x, t)$ đã được chuẩn hóa trên toàn không gian.
(d) Tìm tần số góc dao động $\omega_{\mathrm{osc}}$ của hàm phân bố xác suất. Ý nghĩa vật lý của dao động này là gì?
(e) Giả sử $\Psi(x,t)$ là sự chồng chập hai mức thấp nhất của giếng thế hữu hạn có chiều rộng $L$. Chiều cao thành $U_0$ bằng sáu lần năng lượng cơ bản của giếng vô hạn cùng chiều rộng ($U_0 = 6 E_{1\text{-IDW}}$). Tần số góc dao động của hàm phân bố xác suất trong trường hợp này bằng bao nhiêu?

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Khảo sát trạng thái chồng chập $\Psi=(\Psi_1+\Psi_2)/\sqrt2$ của hai mức thấp nhất, với $\Psi_j=\psi_j e^{-iE_jt/\hbar}$. Xét cả giếng vô hạn lẫn giếng hữu hạn.
(a) Tính $|\Psi(x, t)|^2$.
(b) Kiểm tra tính chất trạng thái dừng.
(c) Chứng minh điều kiện chuẩn hóa $\int_0^L |\Psi|^2 dx = 1$.
(d) Tìm $\omega_{\mathrm{osc}}$ và phân tích chuyển động của bó sóng.
(e) Tính $\omega_{\mathrm{osc}}$ cho giếng hữu hạn $U_0 = 6 E_{1\text{-IDW}}$.

**Hướng đi:**

- **Mật độ xác suất phức**: $|\Psi|^2 = \Psi^* \Psi$. Sử dụng công thức Euler $e^{i\theta} + e^{-i\theta} = 2\cos\theta$ để gom phần phụ thuộc thời gian thành hàm cosin thực.
- **Tiêu chuẩn trạng thái dừng**: Trạng thái dừng đòi hỏi mật độ xác suất độc lập với thời gian. Nếu $|\Psi(x, t)|^2$ phụ thuộc vào $t$, hệ không phải trạng thái dừng.
- **Tính trực giao**: Tích phân xen phủ của hai trạng thái dừng khác nhau trong giếng thế triệt tiêu: $\int_0^L \psi_1(x)\psi_2(x)dx = 0$.
- **Giao thoa pha lượng tử**: Tần số góc dao động của mật độ xác suất luôn bằng $\omega_{\mathrm{osc}} = (E_2 - E_1)/\hbar$.
- **Giếng thế hữu hạn**: Sử dụng các nghiệm số của mức năng lượng liên kết $E_1$ và $E_2$ từ phương trình siêu việt.

---

### Hướng dẫn giải chi tiết (Solution Guide)

#### Nhận diện và thiết lập (Identify and Set Up)

1. Trong Mục 40.1, chúng ta đã khảo sát sự chồng chập của hai hàm sóng hạt tự do có năng lượng khác nhau để tạo thành hiện tượng phách lượng tử. Trong bài toán này, nguyên lý chồng chập được áp dụng cho các sóng đứng bị giam cầm trong giếng thế vô hạn (Mục 40.2) và giếng thế hữu hạn (Mục 40.3). Vì toán tử Schrödinger là một toán tử vi phân tuyến tính, bất kỳ tổ hợp tuyến tính nào của các nghiệm trạng thái dừng cũng là một nghiệm hợp lệ của phương trình Schrödinger phụ thuộc thời gian.

#### Thực hiện giải toán (Execute)

2. **Xác định hàm sóng và mật độ xác suất (Ý a & b)**:
Hàm sóng không gian của hai mức năng lượng đầu tiên là

$$
\begin{aligned}
\psi_1(x) &= \sqrt{\frac{2}{L}}\sin\left(\frac{\pi x}{L}\right), \\
\psi_2(x) &= \sqrt{\frac{2}{L}}\sin\left(\frac{2\pi x}{L}\right).
\end{aligned}
$$

Hàm sóng toàn phần phụ thuộc thời gian và liên hợp phức của nó:

$$
\begin{aligned}
\Psi(x, t) &= \frac{1}{\sqrt{2}}(\Psi_1 + \Psi_2), \\
\Psi^*(x, t) &= \frac{1}{\sqrt{2}}(\Psi_1^* + \Psi_2^*).
\end{aligned}
$$

Nhân hai hàm sóng, ta tách thành thành phần dừng $P_0(x)$ và thành phần dao động $P_{\mathrm{osc}}(x, t)$:

$$
\begin{aligned}
|\Psi|^2 &= P_0(x) + P_{\mathrm{osc}}(x, t), \\
P_0(x) &= \frac{1}{2}\psi_1^2 + \frac{1}{2}\psi_2^2, \\
P_{\mathrm{osc}} &= \psi_1\psi_2\cos(\omega_{\mathrm{osc}} t).
\end{aligned}
$$

Đặt $S_1 = \sin(\pi x/L)$ và $S_2 = \sin(2\pi x/L)$, mật độ xác suất viết dưới dạng hàm sin là:

$$
\begin{aligned}
P_0 &= \frac{S_1^2 + S_2^2}{L}, \\
P_{\mathrm{osc}} &= \frac{2S_1 S_2}{L}\cos(\omega_{\mathrm{osc}} t).
\end{aligned}
$$

Kết luận cho phần (b):
- Hàm sóng $\Psi(x, t)$ **không đại diện cho một trạng thái dừng** có năng lượng xác định.
- Dấu hiệu nhận biết: Mật độ xác suất $|\Psi(x, t)|^2$ phụ thuộc tuần hoàn vào thời gian thông qua số hạng giao thoa cosin. Trạng thái dừng đòi hỏi mật độ xác suất phải hoàn toàn tĩnh và độc lập với thời gian. Hơn nữa, trạng thái này là sự chồng chập mạch lạc của hai trạng thái năng lượng khác nhau ($E_1$ và $E_2$), do đó một phép đo năng lượng sẽ cho kết quả ngẫu nhiên là $E_1$ hoặc $E_2$ chứ không có một giá trị đơn nhất chắc chắn.

3. **Kiểm tra điều kiện chuẩn hóa (Ý c)**:
Đặt $I_1 = \int_0^L \psi_1^2 dx$, $I_2 = \int_0^L \psi_2^2 dx$, và tích phân xen phủ $I_{12} = \int_0^L \psi_1\psi_2 dx$:

$$
\int_0^L |\Psi|^2 dx = I_0 + I_{\mathrm{cross}}.
$$

Với $I_0 = \frac{1}{2}I_1 + \frac{1}{2}I_2$ và $I_{\mathrm{cross}} = I_{12}\cos(\omega_{\mathrm{osc}} t)$.

Vì các hàm sóng trạng thái dừng $\psi_1$ và $\psi_2$ đã được chuẩn hóa riêng biệt:

$$
\begin{aligned}
I_1 &= \int_0^L \psi_1^2(x)dx = 1, \\
I_2 &= \int_0^L \psi_2^2(x)dx = 1.
\end{aligned}
$$

Suy ra $I_0 = \frac{1}{2}(1) + \frac{1}{2}(1) = 1$.

Xét tích phân xen phủ $I_{12} = \int_0^L \psi_1\psi_2 dx$:

$$
I_{12} = \int_0^L \psi_1(x)\psi_2(x)dx.
$$

Đặt $u = \frac{\pi x}{L}$, biến đổi tích hàm sin thành tổng các hàm cosin:

$$
\begin{aligned}
S_1 S_2 &= \frac{1}{2}(\cos u - \cos 3u), \\
u &= \frac{\pi x}{L}.
\end{aligned}
$$

Vì nguyên hàm của $\cos(k\pi x/L)$ là $\frac{L}{k\pi}\sin(k\pi x/L)$ triệt tiêu tại cả hai cận $x = 0$ và $x = L$, với mọi số nguyên $k \ge 1$ ta có:

$$
\int_0^L \cos\left(\frac{k\pi x}{L}\right)dx = 0.
$$

Áp dụng cho $k = 1$ và $k = 3$, tích phân xen phủ triệt tiêu hoàn toàn: $I_{12} = 0$, kéo theo $I_{\mathrm{cross}} = 0$.

Thay các kết quả tích phân vào:

$$
\begin{aligned}
\int_0^L |\Psi|^2 dx &= 1 + 0 \\
&= 1.
\end{aligned}
$$

Điều kiện chuẩn hóa được thỏa mãn nghiêm ngặt tại mọi thời điểm $t$.

4. **Tần số góc và chuyển động của bó sóng (Ý d)**:
Tần số góc dao động của hàm phân bố xác suất là

$$
\omega_{\mathrm{osc}} = \frac{E_2 - E_1}{\hbar}.
$$

Trong giếng thế vô hạn, $E_1 = \frac{\pi^2 \hbar^2}{2mL^2}$ và $E_2 = 2^2 E_1 = 4E_1$. Độ chênh lệch năng lượng là

$$
\begin{aligned}
E_2 - E_1 &= 3E_1 \\
&= 3\frac{\pi^2 \hbar^2}{2mL^2}.
\end{aligned}
$$

Do đó:

$$
\omega_{\mathrm{osc}} = \frac{3\pi^2 \hbar}{2mL^2}.
$$

Chu kỳ dao động tuần hoàn của phân bố xác suất là $T = \frac{2\pi}{\omega_{\mathrm{osc}}} = \frac{4mL^2}{3\pi \hbar}$.

![Hình lời giải cầu nối: Mật độ xác suất ở bốn thời điểm của một chu kỳ. Diện tích dưới mỗi đường đều bằng 1.](./img/young-40/loi-giai-cau-noi.svg)

Ý nghĩa vật lý: Sự chồng chập lượng tử giữa hai trạng thái dừng $n = 1$ và $n = 2$ tạo ra một phân bố xác suất thay đổi tuần hoàn, luân phiên tập trung nhiều hơn ở nửa trái rồi nửa phải của giếng:
- Tại thời điểm $t = 0$: $\cos(\omega_{\mathrm{osc}} t) = 1$. Số hạng giao thoa mang dấu dương ở nửa trái ($x < L/2$) và mang dấu âm ở nửa phải ($x > L/2$). Mật độ xác suất tập trung phồng lớn lệch hẳn sang nửa bên trái của giếng thế, giá trị kỳ vọng vị trí đạt cực tiểu $\langle x \rangle \approx 0{,}32L$.
- Tại thời điểm $t = T/4$: $\omega_{\mathrm{osc}} t = \pi/2 \implies \cos(\omega_{\mathrm{osc}} t) = 0$. Số hạng giao thoa triệt tiêu, phân bố xác suất trở thành đối xứng hoàn hảo với hai đỉnh cực đại tương đương ở hai bên tâm giếng, $\langle x \rangle = 0{,}50L$. Bó sóng đang chuyển động nhanh sang phải.
- Tại thời điểm $t = T/2$: $\omega_{\mathrm{osc}} t = \pi \implies \cos(\omega_{\mathrm{osc}} t) = -1$. Dấu của số hạng giao thoa bị đảo ngược, làm mật độ xác suất dồn lệch hẳn sang nửa bên phải của giếng thế, $\langle x \rangle \approx 0{,}68L$.
- Tại thời điểm $t = 3T/4$: $\omega_{\mathrm{osc}} t = 3\pi/2 \implies \cos(\omega_{\mathrm{osc}} t) = 0$. Phân bố trở lại đối xứng hai đỉnh và bó sóng đang trên đường chuyển động ngược về bên trái.

5. **Áp dụng cho giếng thế hữu hạn (Ý e)**:
Trong giếng thế hữu hạn, phương trình Schrödinger vẫn là tuyến tính và sự chồng chập hai trạng thái dừng thấp nhất vẫn cho mật độ xác suất dao động với tần số góc:

$$
\omega_{\mathrm{osc}} = \frac{E_2 - E_1}{\hbar}.
$$

Với độ sâu giếng $U_0 = 6 E_{1\text{-IDW}}$, các mức năng lượng liên kết được tính toán từ phương trình siêu việt khớp điều kiện biên (như đã trình bày trong Mục 40.3 và Hình 40.15b):
- Dùng các mức năng lượng làm tròn:

$$
\begin{aligned}
E_1 &\approx 0{,}625 E_{1\text{-IDW}}, \\
E_2 &\approx 2{,}43 E_{1\text{-IDW}}.
\end{aligned}
$$

Độ chênh lệch năng lượng là $E_2 - E_1 \approx (2{,}43 - 0{,}625)E_{1\text{-IDW}}$:

$$
E_2 - E_1 \approx 1{,}805 E_{1\text{-IDW}}.
$$

Đặt $\omega_0 = \frac{\pi^2\hbar}{mL^2}$, thay $E_{1\text{-IDW}} = \hbar\omega_0/2$ vào ta được:

$$
\begin{aligned}
\omega_{\mathrm{osc}} &= \frac{1{,}805}{2}\omega_0 \\
&= 0{,}9025\omega_0 \approx 0{,}903\omega_0.
\end{aligned}
$$

- Nếu tính toán số trị chính xác cao trực tiếp từ các nghiệm siêu việt: Nghiệm trạng thái chẵn cho $E_1 \approx 0{,}62527 E_{1\text{-IDW}}$ và nghiệm trạng thái lẻ cho $E_2 \approx 2{,}43467 E_{1\text{-IDW}}$, dẫn đến hiệu năng lượng $\Delta E \approx 1{,}8094 E_{1\text{-IDW}}$, tương ứng với tần số góc chính xác là $\omega_{\mathrm{osc}} \approx 0{,}9047\frac{\pi^2 \hbar}{mL^2}$. Cả hai cách biểu diễn đều xác nhận tần số dao động vào khoảng $0{,}90\frac{\pi^2 \hbar}{mL^2}$.

---

#### Đánh giá và nhận xét (Evaluate)

6. **Tầm quan trọng của các hệ số $1/\sqrt{2}$**:
Các thừa số $1/\sqrt{2}$ có hai vai trò:
- **Chuẩn hóa xác suất**: Đảm bảo tổng xác suất toàn phần của trạng thái chồng chập bằng đúng 1. Vì $\left(\frac{1}{\sqrt{2}}\right)^2 + \left(\frac{1}{\sqrt{2}}\right)^2 = \frac{1}{2} + \frac{1}{2} = 1$, xác suất tìm thấy hạt trong giếng vô hạn bằng 1.
- **Cân bằng trọng số hai mức**: Hai trạng thái dừng đóng góp với trọng số bằng nhau ($50\%$ xác suất cho $E_1$ và $50\%$ xác suất cho $E_2$). Với hai hàm riêng cố định, hệ số giao thoa có độ lớn tỉ lệ với $|c_1c_2|$. Khi $|c_1|^2+|c_2|^2=1$, tích này lớn nhất ở hai trọng số bằng nhau. Độ tương phản tại một tọa độ còn phụ thuộc giá trị hai hàm riêng tại đó.

7. **Tại sao tần số dao động của giếng hữu hạn lại thấp hơn giếng vô hạn?**
Tần số góc dao động tỉ lệ thuận với hiệu năng lượng: $\omega_{\mathrm{osc}} = (E_2 - E_1)/\hbar$.
- Trong giếng thế vô hạn, hai thành thế là các bức tường cứng tuyệt đối, hàm sóng bị ép triệt tiêu ngay tại mép $x = 0$ và $x = L$.
- Trong giếng thế hữu hạn, các vách thế có thể đâm xuyên được. Hàm sóng của cả hai trạng thái $n = 1$ và $n = 2$ đều thâm nhập một đoạn vào vùng cấm cổ điển bên ngoài giếng. Điều này làm cho bước sóng hiệu dụng dài hơn, tương đương với một giếng thế rộng hơn ($L_{\mathrm{eff}} > L$).
- Do năng lượng tỉ lệ nghịch với bình phương bề rộng hiệu dụng ($E \propto 1/L_{\mathrm{eff}}^2$), hai mức thấp nhất trong trường hợp đang xét hạ xuống và hiệu năng lượng giảm. Điều này được xác nhận bằng các nghiệm điều kiện biên:

$$
\Delta E_{\mathrm{finite}} < \Delta E_{\mathrm{infinite}}.
$$

Cụ thể, $\Delta E$ giảm từ $3E_{1\text{-IDW}}$ xuống còn khoảng $1{,}805 E_{1\text{-IDW}}$ (giảm khoảng $40\%$). Vì khoảng cách năng lượng nhỏ hơn, tần số góc dao động $\omega_{\mathrm{osc}}$ của bó sóng trong giếng hữu hạn thấp hơn rõ rệt so với giếng vô hạn cùng kích thước.

</details>
