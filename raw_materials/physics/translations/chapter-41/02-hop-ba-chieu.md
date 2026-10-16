## 41.2. Hạt trong hộp thế ba chiều

Xét một hạt khối lượng $m$ bị giam giữ hoàn toàn bên trong một hộp thế hình lập phương có cạnh bằng $L$. Mô hình này có thể mô tả một electron chuyển động tự do bên trong thể tích của một khối kim loại rắn nhưng không thể thoát ra ngoài bề mặt khối kim loại. Chúng ta chọn gốc tọa độ $O$ tại một đỉnh của hộp, các trục tọa độ $x$, $y$, $z$ hướng dọc theo các cạnh của hộp. Khi đó, hạt bị giới hạn chuyển động trong miền không gian $0 \le x \le L$, $0 \le y \le L$, $0 \le z \le L$.

![Hình 41.01: Hạt bị giam giữ trong một hộp thế hình lập phương có các mặt biên nằm tại $x = 0$, $x = L$, $y = 0$, $y = L$, $z = 0$ và $z = L$.](../img/young-41/hinh-41-01.png)

Tương tự như mô hình giếng thế sâu vô hạn một chiều, thế năng của hạt triệt tiêu ở bên trong hộp và tiến tới vô hạn ở bên ngoài hộp. Đặt $V = (0, L)^3$ là miền không gian bên trong hộp:

$$
U(\vec{r}) = \begin{cases} 0 & (\vec{r} \in V) \\ \infty & (\vec{r} \notin V) \end{cases}
$$

Để số hạng $U(x, y, z)\psi(x, y, z)$ trong phương trình Schrödinger không phụ thuộc thời gian (41.5) không tiến tới vô hạn, hàm sóng không gian $\psi(x, y, z)$ bắt buộc phải triệt tiêu ở bên ngoài hộp: $\psi(x, y, z) = 0$. Kéo theo hàm phân bố xác suất $|\psi(x, y, z)|^2$ triệt tiêu ở ngoài hộp, đồng nghĩa với việc hạt hoàn toàn không có khả năng xuất hiện bên ngoài hộp.

Bên trong hộp thế, thế năng $U(x, y, z) = 0$, phương trình Schrödinger không phụ thuộc thời gian (41.5) trở thành:

$$
-\frac{\hbar^2}{2m}\nabla^2\psi = E\psi \tag{41.7}
$$

Để hàm sóng liên tục tại các bề mặt biên của hộp, hàm sóng $\psi(x, y, z)$ phải bằng không trên toàn bộ sáu mặt thành hộp. Do đó, các điều kiện biên của bài toán là $\psi = 0$ tại $x = 0$, $x = L$, $y = 0$, $y = L$, $z = 0$, và $z = L$.

### Phương pháp tách biến

Để giải phương trình đạo hàm riêng ba chiều (41.7), chúng ta áp dụng phương pháp tách biến. Tương tự như việc phân tách biến thời gian và biến không gian ở phương trình (41.4), chúng ta giả thiết hàm sóng không gian $\psi(x, y, z)$ có thể biểu diễn dưới dạng tích của ba hàm số độc lập, mỗi hàm chỉ phụ thuộc vào duy nhất một tọa độ không gian:

$$
\psi(x, y, z) = X(x) Y(y) Z(z) \tag{41.8}
$$

Thay biểu thức tích (41.8) vào phương trình vi phân (41.7):

$$
-\frac{\hbar^2}{2m}\nabla^2(XYZ) = E\psi \tag{41.9}
$$

Vì đạo hàm riêng tác động lên tích ba hàm đơn biến cho $\frac{\partial^2\psi}{\partial x^2} = YZ\frac{d^2 X}{dx^2}$ (tương tự cho $y$ và $z$), chia cả hai vế của phương trình (41.9) cho tích $XYZ = \psi$, chúng ta thu được:

$$
\varepsilon_x + \varepsilon_y + \varepsilon_z = E \tag{41.10}
$$

với các số hạng phân li $\varepsilon_x(x) = -\frac{\hbar^2}{2m}\frac{1}{X}\frac{d^2 X}{dx^2}$, $\varepsilon_y(y) = -\frac{\hbar^2}{2m}\frac{1}{Y}\frac{d^2 Y}{dy^2}$, và $\varepsilon_z(z) = -\frac{\hbar^2}{2m}\frac{1}{Z}\frac{d^2 Z}{dz^2}$. Vế phải của phương trình (41.10) là mức năng lượng $E$ của trạng thái dừng. Năng lượng $E$ là một hằng số xác định, hoàn toàn không phụ thuộc vào các giá trị tọa độ $x$, $y$, $z$. Do đó, vế trái của phương trình cũng phải độc lập với $x$, $y$, $z$. Khi tọa độ $x$ biến đổi mà $y$ và $z$ giữ nguyên, chỉ có $\varepsilon_x(x)$ biến đổi. Để tổng ba số hạng luôn bằng một hằng số $E$, mỗi số hạng bắt buộc phải bằng một hằng số độc lập, lần lượt ký hiệu là $E_X$, $E_Y$, và $E_Z$:

$$
-\frac{\hbar^2}{2m}\frac{d^2 X}{dx^2} = E_X X \tag{41.11a}
$$

$$
-\frac{\hbar^2}{2m}\frac{d^2 Y}{dy^2} = E_Y Y \tag{41.11b}
$$

$$
-\frac{\hbar^2}{2m}\frac{d^2 Z}{dz^2} = E_Z Z \tag{41.11c}
$$

Điều kiện biên $\psi(x, y, z) = X(x)Y(y)Z(z) = 0$ trên các mặt của hộp thế đòi hỏi: $X(0) = X(L) = 0$, $Y(0) = Y(L) = 0$, và $Z(0) = Z(L) = 0$.

Từ phương trình (41.10), mối liên hệ giữa các hằng số phân tách và năng lượng toàn phần là:

$$
E_X + E_Y + E_Z = E \tag{41.12}
$$

Hệ thức (41.12) hoàn toàn tương ứng với biểu thức động năng phi tương đối tính (41.1) theo ba thành phần động lượng. Vì thế năng bên trong hộp bằng không, năng lượng toàn phần của hạt hoàn toàn là động năng, và các hằng số $E_X$, $E_Y$, $E_Z$ chính là năng lượng ứng với chuyển động của hạt dọc theo từng trục tọa độ.

### Hàm sóng dừng và các số lượng tử

Phương pháp tách biến đã biến đổi một phương trình vi phân đạo hàm riêng phức tạp với ba biến độc lập thành ba phương trình vi phân thường độc lập, mỗi phương trình chỉ chứa một biến duy nhất. Mỗi phương trình vi phân thường trong hệ (41.11) có dạng toán học giống hệt phương trình Schrödinger của một hạt trong hộp thế một chiều với cùng điều kiện biên tại $0$ và $L$. Với các số lượng tử $n_X, n_Y, n_Z = 1, 2, 3, \dots$, nghiệm của hệ phương trình (41.11) là các hàm sóng điều hòa:

$$
X_{n_X}(x) = C_X \sin\frac{n_X \pi x}{L} \tag{41.13a}
$$

$$
Y_{n_Y}(y) = C_Y \sin\frac{n_Y \pi y}{L} \tag{41.13b}
$$

$$
Z_{n_Z}(z) = C_Z \sin\frac{n_Z \pi z}{L} \tag{41.13c}
$$

Trong đó $C_X$, $C_Y$, $C_Z$ là các hằng số biên độ, và các thành phần năng lượng tương ứng nhận các giá trị gián đoạn:

$$
E_X = \frac{n_X^2 \pi^2 \hbar^2}{2mL^2} \tag{41.14a}
$$

$$
E_Y = \frac{n_Y^2 \pi^2 \hbar^2}{2mL^2} \tag{41.14b}
$$

$$
E_Z = \frac{n_Z^2 \pi^2 \hbar^2}{2mL^2} \tag{41.14c}
$$

Nếu như bài toán hộp thế một chiều chỉ xuất hiện duy nhất một số lượng tử $n$, thì bài toán hộp thế ba chiều đòi hỏi đồng thời ba số lượng tử độc lập $n_X, n_Y, n_Z$ để xác định trọn vẹn trạng thái dừng của hạt. Tổ hợp ba hàm sóng đơn biến cho hàm sóng không gian toàn phần của trạng thái $(n_X, n_Y, n_Z)$:

$$
\psi_{n_X, n_Y, n_Z} = X_{n_X} Y_{n_Y} Z_{n_Z} \tag{41.15}
$$

với $n_X, n_Y, n_Z \in \{1, 2, 3, \dots\}$, trong đó $C = C_X C_Y C_Z$ là hằng số chuẩn hóa toàn phần, được xác định thông qua điều kiện chuẩn hóa (41.6).

Các nghiệm ở phương trình (41.15) tương tự sóng điện từ đứng trong một hốc cộng hưởng hình hộp, chẳng hạn khoang lò vi sóng. Các nút sóng tạo những vùng nhận ít năng lượng. Đĩa quay đưa thực phẩm qua nhiều vị trí để việc làm nóng đều hơn. Tương tự, hàm sóng trong hộp có các mặt nút, tại đó mật độ xác suất bằng không.

Chẳng hạn, xét trạng thái có bộ số lượng tử $(n_X, n_Y, n_Z) = (2, 1, 1)$. Đặt $S_{nx} = \sin^2(n\pi x/L)$ (tương tự cho $y$ và $z$), hàm phân bố xác suất của trạng thái này là:

$$
|\psi_{2, 1, 1}|^2 = |C|^2 S_{2x} S_{1y} S_{1z}
$$

Vì $\sin^2(2\pi x/L) = 0$ tại vị trí $x = L/2$, mật độ xác suất hoàn toàn triệt tiêu trên mặt phẳng $x = L/2$. Hạt có xác suất xuất hiện lớn nhất tại những vị trí cả ba hàm $\sin^2$ đồng thời đạt cực đại, tức là tại $(x, y, z) = (L/4, L/2, L/2)$ và $(x, y, z) = (3L/4, L/2, L/2)$.

![Hình 41.02: Hàm phân bố xác suất $|\psi_{n_X, n_Y, n_Z}(x, y, z)|^2$ ứng với ba trạng thái suy biến: (a) $(2, 1, 1)$, (b) $(1, 2, 1)$, và (c) $(1, 1, 2)$. Mật độ các chấm xanh tỷ lệ thuận với giá trị của $|\psi|^2$. Hàm sóng triệt tiêu trên các vách của hộp thế và trên mặt phẳng giữa hộp.](../img/young-41/hinh-41-02.png)

Khi các số lượng tử $n_X, n_Y, n_Z$ nhận giá trị lớn hơn, số lượng các mặt nút phân cách có mật độ xác suất bằng không sẽ tăng lên tương ứng.

### Ví dụ 41.1: Tính toán xác suất trong hộp thế ba chiều

Xét một hạt chuyển động trong hộp thế hình lập phương có cạnh bằng $L$.

(a) Xác định giá trị của hằng số $C$ để chuẩn hóa hàm sóng trong phương trình (41.15).

(b) Tính xác suất tìm thấy hạt trong phần tư thể tích hộp $0 \le x \le L/4$ đối với ba trạng thái lượng tử: (i) $(n_X, n_Y, n_Z) = (1, 2, 1)$, (ii) $(n_X, n_Y, n_Z) = (2, 1, 1)$, và (iii) $(n_X, n_Y, n_Z) = (3, 1, 1)$.

![Hình 41.03: Phần tư thể tích của hộp thế được giới hạn bởi $0 \le x \le L/4$, $0 \le y \le L$, và $0 \le z \le L$.](../img/young-41/hinh-41-03.png)

#### Phương pháp giải

Để chuẩn hóa hàm sóng ở câu (a), chúng ta vận dụng điều kiện chuẩn hóa (41.6): Tích phân của mật độ xác suất $|\psi_{n_X, n_Y, n_Z}(x, y, z)|^2$ lấy trên toàn bộ thể tích hộp thế phải bằng 1. Ở câu (b), xác suất tìm thấy hạt trong miền không gian xác định bằng tích phân của $|\psi|^2$ lấy trên miền giới hạn $0 \le x \le L/4$, $0 \le y \le L$, $0 \le z \le L$.

#### Lời giải chi tiết

(a) Từ biểu thức (41.15), mật độ xác suất là:

$$
|\psi|^2 = |C|^2 S_x S_y S_z
$$

với $S_x = \sin^2(n_X\pi x/L)$, $S_y = \sin^2(n_Y\pi y/L)$, và $S_z = \sin^2(n_Z\pi z/L)$. Đặt $I_X = \int_0^L S_x\,dx$ (tương tự cho $I_Y, I_Z$). Điều kiện chuẩn hóa đòi hỏi tích phân trên toàn thể tích hộp bằng 1:

$$
\begin{aligned}
\int |\psi|^2 \, dV &= |C|^2 I_X I_Y I_Z \\
&= 1
\end{aligned}
$$

Áp dụng công thức hạ bậc $\sin^2\theta = \frac{1}{2}(1 - \cos 2\theta)$ và nguyên hàm $F(u) = \frac{u}{2} - \frac{L}{4n\pi}\sin\frac{2n\pi u}{L}$ để tính tích phân phụ thuộc $x$:

$$
I_X = [F(x)]_0^L = \frac{L}{2}
$$

Tích phân theo biến $y$ và $z$ cũng cho kết quả tương tự: $I_Y = I_Z = L/2$. Ta chọn pha chung để $C$ thực và dương. Điều kiện chuẩn hóa trở thành:

$$
\begin{aligned}
|C|^2 (L/2)^3 &= 1 \\
\implies C &= (2/L)^{3/2}
\end{aligned}
$$

(b) Tính xác suất $P$ tìm thấy hạt trong miền $0 \le x \le L/4$. Giới hạn tích phân theo biến $y$ và biến $z$ vẫn mở rộng từ $0$ đến $L$, cho giá trị mỗi tích phân là $L/2$. Tích phân theo biến $x$ lấy từ $0$ đến $L/4$:

$$
\begin{aligned}
I_X &= [F(x)]_0^{L/4} \\
&= \frac{L}{8} - \frac{L}{4n_X\pi} \sin\frac{n_X\pi}{2}
\end{aligned}
$$

Kết hợp các kết quả trên, xác suất toàn phần tìm thấy hạt trong miền $0 \le x \le L/4$ là:

$$
\begin{aligned}
P &= |C|^2 I_X (L/2)^2 \\
&= \frac{1}{4} - \frac{1}{2n_X\pi} \sin\frac{n_X\pi}{2}
\end{aligned}
$$

Xác suất này chỉ phụ thuộc vào số lượng tử $n_X$, hoàn toàn độc lập với $n_Y$ và $n_Z$. Thay các giá trị cụ thể của $n_X$:

- Trường hợp (i) với $n_X = 1$:

$$
P_1 = \frac{1}{4} - \frac{1}{2\pi} \approx 0{,}091
$$

- Trường hợp (ii) với $n_X = 2$:

$$
P_2 = \frac{1}{4} - 0 = 0{,}250
$$

- Trường hợp (iii) với $n_X = 3$:

$$
P_3 = \frac{1}{4} + \frac{1}{6\pi} \approx 0{,}303
$$

#### Đánh giá kết quả

Sự khác biệt về xác suất trong ba trường hợp có nguồn gốc trực tiếp từ đồ thị hàm $\sin^2(n_X\pi x/L)$. Đối với $n_X = 2$, đồ thị hàm $\sin^2(2\pi x/L)$ có tính đối xứng hoàn hảo trong bốn phần tư của hộp, diện tích dưới đường cong trong khoảng $x \in [0, L/4]$ chiếm đúng $1/4$ tổng diện tích. Đối với $n_X = 1$, hạt có xu hướng tập trung ở giữa hộp quanh vị trí $x = L/2$, do đó xác suất xuất hiện ở phần tư cạnh thành hộp giảm xuống chỉ còn $9{,}1\%$. Ngược lại, với $n_X = 3$, một cực đại xác suất nằm trọn bên trong khoảng $x \in [0, L/4]$, khiến xác suất nâng lên thành $30{,}3\%$.

### Mức năng lượng, độ suy biến và tính đối xứng

Từ hệ thức (41.12) và các thành phần năng lượng (41.14), mức năng lượng cho phép của một hạt khối lượng $m$ giam trong hộp lập phương cạnh $L$ là:

$$
E_{n_X, n_Y, n_Z} = \frac{n^2 \pi^2\hbar^2}{2mL^2} \tag{41.16}
$$

với $n^2 = n_X^2 + n_Y^2 + n_Z^2$ và $n_X, n_Y, n_Z \in \{1, 2, 3, \dots\}$.

![Hình 41.04: Giản đồ các mức năng lượng của một hạt trong hộp thế lập phương ba chiều. Mỗi mức năng lượng được gán các bộ ba số lượng tử $(n_X, n_Y, n_Z)$. Năng lượng của các mức kích thích được biểu diễn dưới dạng bội số của năng lượng trạng thái cơ bản $E_{1,1,1}$.](../img/young-41/hinh-41-04.png)

Trạng thái có năng lượng thấp nhất (trạng thái cơ bản) ứng với bộ ba số lượng tử $(n_X, n_Y, n_Z) = (1, 1, 1)$, có mức năng lượng:

$$
E_{1, 1, 1} = \frac{3\pi^2\hbar^2}{2mL^2}
$$

Quan sát giản đồ Hình 41.04, phần lớn các mức năng lượng tương ứng với nhiều bộ ba số lượng tử $(n_X, n_Y, n_Z)$ khác nhau, nghĩa là ứng với nhiều trạng thái lượng tử phân biệt. Hiện tượng hai hay nhiều trạng thái lượng tử riêng biệt có cùng một mức năng lượng được gọi là hiện tượng suy biến (degeneracy), và các trạng thái đó được gọi là các trạng thái suy biến. Số lượng trạng thái ứng với cùng một mức năng lượng được gọi là bậc suy biến (hoặc độ suy biến).

Trong hộp thế một chiều, mỗi mức năng lượng chỉ ứng với duy nhất một trạng thái sóng dừng, hoàn toàn không có hiện tượng suy biến. Ngược lại, trong hộp thế ba chiều hình lập phương:

- Trạng thái cơ bản $E_{1, 1, 1}$: Chỉ có một trạng thái duy nhất $(1, 1, 1)$, độ suy biến bằng 1 (không suy biến).
- Mức kích thích thứ nhất $E = 2 E_{1, 1, 1} = \frac{6}{3}E_{1, 1, 1}$: Gồm ba trạng thái phân biệt $(2, 1, 1)$, $(1, 2, 1)$, và $(1, 1, 2)$, độ suy biến bằng 3.
- Mức kích thích thứ hai $E = 3 E_{1, 1, 1} = \frac{9}{3}E_{1, 1, 1}$: Gồm ba trạng thái phân biệt $(2, 2, 1)$, $(2, 1, 2)$, và $(1, 2, 2)$, độ suy biến bằng 3.
- Mức kích thích thứ ba $E = \frac{11}{3} E_{1, 1, 1}$: Gồm ba trạng thái phân biệt $(3, 1, 1)$, $(1, 3, 1)$, và $(1, 1, 3)$, độ suy biến bằng 3.
- Mức kích thích thứ tư $E = 4 E_{1, 1, 1} = \frac{12}{3}E_{1, 1, 1}$: Ứng với bộ số $(2, 2, 2)$, độ suy biến bằng 1.
- Mức kích thích thứ năm $E = \frac{14}{3} E_{1, 1, 1}$: Ứng với tổng các bình phương bằng $14$, gồm 6 hoán vị khác nhau của bộ ba $(3, 2, 1)$: $(3, 2, 1)$, $(3, 1, 2)$, $(1, 3, 2)$, $(2, 3, 1)$, $(1, 2, 3)$, và $(2, 1, 3)$, độ suy biến bằng 6.

Ba trạng thái này có cùng năng lượng vì tính đối xứng của hộp lập phương. Phép quay hộp thích hợp một góc $90^\circ$ hoán đổi các trục và chuyển trạng thái này thành trạng thái kia, có thể kèm một pha chung. Phép quay giữ nguyên bài toán, nên năng lượng không đổi.

Vì sự suy biến bắt nguồn từ tính đối xứng, chúng ta có thể phá vỡ tính đối xứng để khử suy biến. Xét trường hợp hộp thế hình hộp chữ nhật bất đối xứng có ba kích thước cạnh khác nhau là $L_X$, $L_Y$, và $L_Z$. Giải lại phương trình Schrödinger với các cạnh khác nhau, phổ năng lượng của hạt là:

$$
E = E_X + E_Y + E_Z \tag{41.17}
$$

với $E_X = \frac{n_X^2\pi^2\hbar^2}{2mL_X^2}$ (tương tự cho $Y$ và $Z$) và $n_X, n_Y, n_Z \in \{1, 2, 3, \dots\}$. Nếu ba cạnh đôi một khác nhau, ba trạng thái $(2,1,1)$, $(1,2,1)$ và $(1,1,2)$ có ba năng lượng khác nhau. Đây là sự khử suy biến của bộ ba đang xét. Những mức cao khác vẫn có thể trùng năng lượng với một số tỷ lệ cạnh đặc biệt. Khi ba cạnh cùng bằng $L$, phương trình (41.17) trở về phương trình (41.16).

Tổng kết lại các điểm khác biệt cốt lõi giữa bài toán lượng tử một chiều và ba chiều:

- Các nghiệm tách biến đang xét là tích của ba hàm, mỗi hàm phụ thuộc một tọa độ. Bài toán một chiều chỉ cần một hàm theo $x$. Tổ hợp tuyến tính các nghiệm cùng năng lượng vẫn có thể là trạng thái dừng, dù không nhất thiết có dạng một tích.
- Cần ba số lượng tử $n_X, n_Y, n_Z$ để mô tả trọn vẹn mỗi trạng thái dừng ba chiều, trong khi bài toán một chiều chỉ cần một số lượng tử $n$.
- Phần lớn các mức năng lượng ba chiều đều bị suy biến do tính đối xứng hình học, trong khi bài toán hộp thế một chiều không có sự suy biến.
- Trong các nghiệm ba chiều đang xét, hàm sóng triệt tiêu trên những mặt nút. Trong hộp một chiều, các nút là những điểm riêng lẻ trên trục tọa độ. Hàm sóng vẫn liên tục tại các nút.

### Câu tự kiểm tra 41.2

Sắp xếp các trạng thái lượng tử sau đây của một hạt trong hộp thế lập phương cạnh $L$ theo thứ tự năng lượng từ cao nhất đến thấp nhất:

- (i) $(n_X, n_Y, n_Z) = (2, 3, 2)$
- (ii) $(n_X, n_Y, n_Z) = (4, 1, 1)$
- (iii) $(n_X, n_Y, n_Z) = (2, 2, 3)$
- (iv) $(n_X, n_Y, n_Z) = (1, 3, 3)$

::: details Lời giải chi tiết
**Đáp án:** Thứ tự sắp xếp từ năng lượng cao nhất đến thấp nhất là (iv), (ii), (i) và (iii) đồng hạng.

Theo phương trình (41.16), mức năng lượng của hạt trong hộp lập phương tỷ lệ thuận với tổng bình phương của ba số lượng tử: $n_X^2 + n_Y^2 + n_Z^2$. Việc so sánh thứ tự năng lượng tương đương với việc so sánh giá trị tổng bình phương này cho từng trạng thái:

- Trạng thái (i): $2^2 + 3^2 + 2^2 = 17$.
- Trạng thái (ii): $4^2 + 1^2 + 1^2 = 18$.
- Trạng thái (iii): $2^2 + 2^2 + 3^2 = 17$.
- Trạng thái (iv): $1^2 + 3^2 + 3^2 = 19$.

So sánh các giá trị tính được: $19 > 18 > 17 = 17$. Hai trạng thái (i) $(2, 3, 2)$ và (iii) $(2, 2, 3)$ có cùng mức năng lượng (suy biến với nhau). Do đó, thứ tự sắp xếp từ năng lượng cao nhất đến thấp nhất là: (iv), (ii), (i) và (iii) đồng hạng.
:::
