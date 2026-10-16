## Tổng kết chương

### Phương trình Schrödinger trong ba chiều

Với khối lượng không đổi và thế năng không phụ thuộc thời gian, đặt toán tử Laplace bằng tổng ba đạo hàm bậc hai:

$$
\begin{aligned}
\nabla^2\psi&=\psi_{xx}+\psi_{yy}+\psi_{zz},\\
\psi_{xx}&=\frac{\partial^2\psi}{\partial x^2}.
\end{aligned}
$$

Hai ký hiệu $\psi_{yy}$ và $\psi_{zz}$ được định nghĩa tương tự theo $y$ và $z$. Phương trình trạng thái dừng là:

$$
-\frac{\hbar^2}{2m}\nabla^2\psi+U\psi=E\psi.
$$

Mật độ xác suất là $|\psi|^2$, còn xác suất trong một miền được tính bằng tích phân theo thể tích. Hàm sóng phải thỏa mãn điều kiện biên và điều kiện chuẩn hóa trên toàn miền.

### Hạt trong hộp ba chiều

Trong hộp lập phương cạnh $L$ có thành vô hạn và đáy thế bằng 0, ba số lượng tử $n_x,n_y,n_z$ là các số nguyên dương. Đặt:

$$
\begin{aligned}
N&=n_x^2+n_y^2+n_z^2,\\
E_*&=\frac{\pi^2\hbar^2}{2mL^2}.
\end{aligned}
$$

Năng lượng bằng $E=NE_*$. Phần không gian của hàm sóng là tích ba hàm sin một chiều. Những bộ số lượng tử khác nhau có thể cho cùng tổng $N$, tạo nên suy biến năng lượng. Hoán đổi các trục làm đổi trạng thái khi bộ số lượng tử đổi, dù năng lượng có thể giữ nguyên.

![Tổng kết hộp ba chiều: Hạt bị giới hạn bởi sáu thành của hộp lập phương. Các nút sóng tại thành lượng tử hóa ba thành phần số sóng.](./img/young-41/tom-tat-hop-ba-chieu.png)

### Nguyên tử hydro

Trong mô hình Coulomb phi tương đối tính, năng lượng phụ thuộc số lượng tử chính $n$. Nếu tính chuyển động của hạt nhân, dùng khối lượng rút gọn:

$$
m_r=\frac{m_eM}{m_e+M}.
$$

Ở đây $M$ là khối lượng hạt nhân. Đặt thang năng lượng dương $E_{\rm H}$ và bán kính $a$:

$$
\begin{aligned}
E_{\rm H}&=\frac{m_re^4}{2(4\pi\varepsilon_0)^2\hbar^2},\\
a&=\frac{4\pi\varepsilon_0\hbar^2}{m_re^2}.
\end{aligned}
$$

Với hydro, $E_n=-E_{\rm H}/n^2$, trong đó $E_{\rm H}\approx13{,}60\,\mathrm{eV}$ và $a\approx5{,}29\times10^{-11}\,\mathrm m$. Với ion chỉ có một electron và điện tích hạt nhân $Ze$, năng lượng nhận thêm hệ số $Z^2$.

Các số lượng tử quỹ đạo có miền:

$$
\begin{aligned}
n&=1,2,3,\dots,\\
\ell&=0,1,\dots,n-1,\\
m_\ell&=-\ell,-\ell+1,\dots,\ell.
\end{aligned}
$$

Độ lớn mômen động lượng quỹ đạo và hình chiếu lên trục chọn trước là:

$$
\begin{aligned}
L&=\sqrt{\ell(\ell+1)}\,\hbar,\\
L_z&=m_\ell\hbar.
\end{aligned}
$$

Không đồng nhất $L$ với $L_z$ và không gán một quỹ đạo cổ điển xác định cho orbital.

![Tổng kết mômen quỹ đạo: Với cùng số lượng tử ℓ, hình chiếu lên trục z chỉ nhận các giá trị rời rạc, trong khi độ lớn mômen giữ nguyên.](./img/young-41/tom-tat-momen-quy-dao.png)

Mật độ theo bán kính khác mật độ theo thể tích. Nếu $\psi$ không phụ thuộc góc, chẳng hạn trạng thái $1s$:

$$
P(r)=4\pi r^2|\psi(r)|^2.
$$

Khi đã tách phần góc chuẩn hóa khỏi hàm sóng, dạng tổng quát tương ứng là $P(r)=r^2|R(r)|^2$. Xác suất tìm thấy electron trong vỏ cầu từ $r$ đến $r+dr$ bằng $P(r)\,dr$.

### Hiệu ứng Zeeman

Mômen từ quỹ đạo của electron ngược hướng với mômen động lượng vì điện tích electron âm. Đặt magneton Bohr:

$$
\mu_{\rm B}=\frac{e\hbar}{2m_e}.
$$

Với từ trường hướng dương trục $z$, năng lượng tương tác quỹ đạo là:

$$
U=-\mu_zB=m_\ell\mu_{\rm B}B.
$$

Trước khi kể spin, một mức có số lượng tử $\ell$ có thể tách thành $2\ell+1$ thành phần. Cấu trúc vạch quan sát được còn phụ thuộc các điều kiện chọn của chuyển mức.

![Tổng kết Zeeman: Các trạng thái có hình chiếu mômen khác nhau tách năng lượng khi độ lớn từ trường tăng.](./img/young-41/tom-tat-zeeman.png)

### Spin electron và tương tác spin–quỹ đạo

Electron có spin nội tại $s=1/2$. Độ lớn spin và hai giá trị hình chiếu là:

$$
\begin{aligned}
S&=\sqrt{s(s+1)}\,\hbar=\frac{\sqrt3}{2}\hbar,\\
S_z&=m_s\hbar,\qquad m_s=\pm\frac12.
\end{aligned}
$$

Spin là mômen động lượng nội tại, không phải chuyển động tự quay cổ điển của một quả cầu electron.

Mômen từ spin gần bằng $-e\mathbf S/m_e$. Với từ trường hướng dương trục $z$, trạng thái có $S_z>0$ có năng lượng tương tác cao hơn trạng thái có $S_z<0$. Sự tách mức này là cơ sở của cộng hưởng spin.

![Tổng kết spin: Hai trạng thái spin theo trục từ trường tách năng lượng với độ dịch chuyển trái dấu khi từ trường tăng.](./img/young-41/tom-tat-spin.png)

Khi cộng mômen quỹ đạo và spin, số lượng tử tổng nhận $j=\ell+1/2$ hoặc $j=\ell-1/2$, với giá trị thứ hai chỉ tồn tại khi $\ell\ge1$. Các hiệu chỉnh tương đối tính và tương tác spin–quỹ đạo làm năng lượng phụ thuộc $j$.

Với hydro, đặt hằng số cấu trúc tinh tế $\alpha=e^2/(4\pi\varepsilon_0\hbar c)$ và:

$$
\begin{aligned}
b&=\frac{n}{j+1/2}-\frac34,\\
F_{n,j}&=\frac{\alpha^2b}{n^2}.
\end{aligned}
$$

Ở bậc gần đúng đang xét:

$$
E_{n,j}\approx-\frac{E_{\rm H}}{n^2}(1+F_{n,j}).
$$

### Nguyên tử nhiều electron và nguyên lý loại trừ

Bốn số lượng tử $n,\ell,m_\ell,m_s$ xác định một trạng thái một electron trong mô hình trường xuyên tâm. Không có hai electron trong nguyên tử cùng chiếm một trạng thái với cả bốn số lượng tử giống nhau. Vì vậy, một orbital không gian chứa tối đa hai electron có spin đối nhau.

Các electron bên trong che chắn một phần điện tích hạt nhân đối với electron bên ngoài. Với điện tích hiệu dụng $Z_{\rm eff}e$, ước lượng năng lượng là:

$$
E_n\approx-\frac{Z_{\rm eff}^2}{n^2}(13{,}6\,\mathrm{eV}).
$$

Điện tích hiệu dụng phụ thuộc trạng thái, nên không thể thay toàn nguyên tử bằng một giá trị che chắn duy nhất cho mọi orbital. Cấu hình electron và cấu trúc bảng tuần hoàn xuất hiện từ việc lấp đầy các trạng thái dưới ràng buộc Pauli.

![Tổng kết che chắn: Trong nguyên tử liti, hai electron bên trong che chắn một phần điện tích hạt nhân đối với electron ở xa hơn.](./img/young-41/tom-tat-che-chan.png)

### Phổ tia X đặc trưng

Khi tạo lỗ trống ở một mức sâu, electron từ mức cao hơn có thể chuyển xuống và phát photon tia X. Tần số vạch đặc trưng phản ánh hiệu năng lượng giữa các mức. Với vạch $K_\alpha$, gần đúng Moseley cho:

$$
\begin{aligned}
C&=2{,}48\times10^{15}\,\mathrm{Hz},\\
f&\approx C(Z-1)^2.
\end{aligned}
$$

Thừa số $Z-1$ biểu diễn gần đúng che chắn bởi electron còn lại ở lớp trong. Phổ đặc trưng cần được phân biệt với nền liên tục do bức xạ hãm.

![Tổng kết Moseley: Căn bậc hai tần số vạch Kα biến thiên gần tuyến tính theo số hiệu nguyên tử trong mô hình che chắn đơn giản.](./img/young-41/tom-tat-moseley.png)

### Rối lượng tử

Trạng thái thuần của hai hạt có thể không viết được thành tích hai trạng thái riêng biệt. Chẳng hạn, nếu $A$ và $B$ là hai trạng thái một hạt trực chuẩn, ta đặt:

$$
\begin{aligned}
\Phi_1&=A(1)B(2),\\
\Phi_2&=B(1)A(2).
\end{aligned}
$$

Tổ hợp chuẩn hóa:

$$
\Psi=\frac{\Phi_1-\Phi_2}{\sqrt2}
$$

là một trạng thái rối đối xứng lẻ dưới hoán đổi hai hạt. Khi đo một hạt trong cơ sở thích hợp, kết quả xác định phân bố có điều kiện của hạt còn lại. Những tương quan này không đồng nghĩa với khả năng gửi thông tin điều khiển được nhanh hơn ánh sáng.

![Tổng kết rối lượng tử: Trạng thái hai hạt được tạo bởi sự chồng chập mạch lạc của hai cấu hình. Dấu tương đối giữa hai thành phần ảnh hưởng các tương quan đo.](./img/young-41/tom-tat-roi-luong-tu.png)
