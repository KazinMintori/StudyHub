## 41.1. Phương trình Schrödinger trong không gian ba chiều

Ở Chương 40, chúng ta đã nghiên cứu phương trình Schrödinger và các ứng dụng điển hình trong không gian một chiều, tương đương với bài toán chất điểm cổ điển chuyển động dọc theo một đường thẳng. Mô hình một chiều cho phép tiếp cận sáng tỏ những khái niệm nền tảng của cơ học lượng tử. Tuy nhiên, để tìm hiểu cấu trúc thực tế của nguyên tử và các hệ vi mô trong tự nhiên, chúng ta cần khái quát hóa phương trình Schrödinger lên không gian ba chiều $(x, y, z)$.

### Mở rộng hàm sóng và phương trình sóng lên ba chiều

Dạng hình thức của phương trình Schrödinger ba chiều có thể được suy luận trực tiếp từ các nguyên lý cơ bản. Trước hết, hàm sóng toàn phần $\Psi$ phụ thuộc vào thời gian $t$ và cả ba tọa độ không gian $(x, y, z)$. Hàm thế năng tổng quát cũng phụ thuộc vào vị trí của hạt trong không gian và được viết dưới dạng $U(x, y, z)$.

Từ phương trình Schrödinger một chiều, số hạng đạo hàm bậc hai không gian liên hệ mật thiết với động năng của hạt. Đối với một hạt tự do có độ lớn động lượng $p = \hbar k$ và động năng $K = p^2/(2m)$, hàm sóng phẳng có dạng $\Psi(x, t) = A e^{i(kx - \omega t)}$. Tác động đạo hàm bậc hai theo tọa độ cho kết quả:

$$
\begin{aligned}
-\frac{\hbar^2}{2m} \frac{\partial^2\Psi}{\partial x^2} &= \frac{\hbar^2 k^2}{2m}\Psi \\
&= \frac{p^2}{2m}\Psi = K\Psi
\end{aligned}
$$

Khi hạt chuyển động tự do trong không gian ba chiều, vector động lượng của hạt gồm ba thành phần $(p_x, p_y, p_z)$. Động năng phi tương đối tính của hạt là tổng động năng của từng bậc tự do chuyển động:

$$
K = \frac{p_x^2}{2m} + \frac{p_y^2}{2m} + \frac{p_z^2}{2m} \tag{41.1}
$$

Kết hợp các đóng góp động năng dọc theo ba trục tọa độ và sử dụng toán tử Laplace ba chiều $\nabla^2 = \frac{\partial^2}{\partial x^2} + \frac{\partial^2}{\partial y^2} + \frac{\partial^2}{\partial z^2}$, phương trình Schrödinger tổng quát cho một hạt chuyển động trong không gian ba chiều có dạng:

$$
-\frac{\hbar^2}{2m}\nabla^2\Psi + U\Psi = i\hbar\frac{\partial\Psi}{\partial t} \tag{41.2}
$$

Trong phương trình (41.2), $\Psi = \Psi(x, y, z, t)$ là hàm sóng phụ thuộc thời gian, $U = U(x, y, z)$ là hàm thế năng, $m$ là khối lượng của hạt, và $\hbar = h/(2\pi)$ là hằng số Planck rút gọn.

### Ý nghĩa xác suất và điều kiện chuẩn hóa trong ba chiều

Ý nghĩa vật lý của hàm sóng ba chiều hoàn toàn tương đồng với trường hợp một chiều. Bản thân hàm sóng $\Psi(x, y, z, t)$ là một đại lượng phức gồm cả phần thực và phần ảo. Tuy nhiên, bình phương môđun của hàm sóng, ký hiệu là $|\Psi(x, y, z, t)|^2$ và được xác định bằng tích của $\Psi$ với hàm liên hợp phức $\Psi^*$, luôn là một đại lượng thực không âm tại mọi điểm trong không gian.

Đại lượng $|\Psi(x, y, z, t)|^2 \, dV$ biểu diễn xác suất tìm thấy hạt trong một phần tử thể tích vi phân $dV = dx\,dy\,dz$ bao quanh điểm $(x, y, z)$ tại thời điểm $t$. Do đó, $|\Psi(x, y, z, t)|^2$ chính là hàm phân bố xác suất trong không gian ba chiều (mật độ xác suất thể tích).

Vì hạt chắc chắn phải tồn tại ở một nơi nào đó trong không gian, tổng xác suất tìm thấy hạt trên toàn bộ không gian vô hạn bắt buộc phải bằng 1. Đây là điều kiện chuẩn hóa của hàm sóng trong không gian ba chiều:

$$
\int |\Psi(x, y, z, t)|^2 \, dV = 1 \tag{41.3}
$$

Tích phân trong biểu thức (41.3) là tích phân bội ba lấy trên toàn thể tích không gian vô hạn, với phần tử thể tích $dV = dx\,dy\,dz$ trong hệ tọa độ Descartes.

### Trạng thái dừng và phương trình không phụ thuộc thời gian

Khi một trạng thái lượng tử có năng lượng xác định $E$, trạng thái đó được gọi là trạng thái dừng. Đặt $\vec{r} = (x, y, z)$ là vector vị trí trong không gian ba chiều. Đối với trạng thái dừng, hàm sóng toàn phần $\Psi(\vec{r}, t)$ có thể tách biến thành tích của hàm sóng không gian $\psi(\vec{r})$ và hàm dao động điều hòa theo thời gian $e^{-iEt/\hbar}$:

$$
\Psi(\vec{r}, t) = \psi(\vec{r}) e^{-iEt/\hbar} \tag{41.4}
$$

Đạo hàm riêng theo thời gian của hàm sóng (41.4) cho:

$$
\begin{aligned}
i\hbar \frac{\partial\Psi}{\partial t} &= i\hbar \left(-\frac{iE}{\hbar}\right)\Psi \\
&= E\Psi
\end{aligned}
$$

Thay biểu thức (41.4) vào phương trình Schrödinger ba chiều (41.2), sau đó giản ước thừa số chung $e^{-iEt/\hbar}$ khác không ở cả hai vế, ta thu được phương trình Schrödinger không phụ thuộc thời gian trong không gian ba chiều:

$$
-\frac{\hbar^2}{2m}\nabla^2\psi + U\psi = E\psi \tag{41.5}
$$

Trong phương trình (41.5), $\psi = \psi(x, y, z)$ là hàm sóng không gian và $E$ là mức năng lượng xác định của trạng thái đang xét.

Mật độ xác suất của một trạng thái dừng là bình phương môđun của hàm sóng toàn phần:

$$
|\Psi(\vec{r}, t)|^2 = |\psi(\vec{r})|^2
$$

Biểu thức này không phụ thuộc thời gian $t$. Trong trạng thái có năng lượng xác định, phân bố kết quả đo không phụ thuộc thời gian nếu toán tử đo cũng không phụ thuộc thời gian. Đó là ý nghĩa của tên gọi trạng thái dừng. Điều kiện chuẩn hóa (41.3) trở thành:

$$
\int |\psi(x, y, z)|^2 \, dV = 1 \tag{41.6}
$$

Phương trình Schrödinger là một định luật vật lý, không phải một định lý suy ra chỉ bằng biến đổi toán học. Cách mở rộng từ một chiều giúp nhận ra dạng phương trình. Sự phù hợp với thực nghiệm xác nhận khả năng áp dụng của nó trong miền phi tương đối tính đang xét.

Một mục tiêu trọng tâm là ứng dụng phương trình (41.5) để tìm kiếm các hàm sóng trạng thái dừng của nguyên tử hydro. Hàm thế năng Coulomb giữa electron và hạt nhân có tính đối xứng cầu, chỉ phụ thuộc vào khoảng cách $r = \sqrt{x^2 + y^2 + z^2}$ từ electron đến gốc tọa độ đặt tại hạt nhân. Nhằm khai thác triệt để tính đối xứng cầu này, phương pháp tối ưu là chuyển sang hệ tọa độ cầu $(r, \theta, \phi)$ thay vì dùng hệ tọa độ Descartes $(x, y, z)$. Trước khi khảo sát nguyên tử hydro phức tạp, việc xem xét mô hình hạt bị giam trong một hộp thế ba chiều sẽ cung cấp các trực giác vật lý sâu sắc về cách thức các điều kiện biên hình thành nên những số lượng tử và hiện tượng suy biến năng lượng.

### Câu tự kiểm tra 41.1

Trong một vùng không gian nhất định, hàm thế năng của một hạt lượng tử triệt tiêu: $U(x, y, z) = 0$. Tại vùng này, hàm sóng $\psi(x, y, z)$ của một trạng thái dừng là một hàm thực và thỏa mãn đồng thời ba điều kiện $\frac{\partial^2\psi}{\partial x^2} > 0$, $\frac{\partial^2\psi}{\partial y^2} > 0$, và $\frac{\partial^2\psi}{\partial z^2} > 0$. Hạt có năng lượng xác định $E > 0$. Kết luận nào sau đây về giá trị của $\psi(x, y, z)$ trong vùng này là chính xác?

- (i) $\psi(x, y, z)$ bắt buộc phải mang giá trị dương.
- (ii) $\psi(x, y, z)$ bắt buộc phải mang giá trị âm.
- (iii) $\psi(x, y, z)$ bắt buộc phải bằng không.
- (iv) Chưa đủ thông tin để đưa ra kết luận.

::: details Lời giải chi tiết
**Đáp án:** Chọn (ii). $\psi(x, y, z)$ bắt buộc phải mang giá trị âm.

Trong vùng không gian có $U(x, y, z) = 0$, phương trình Schrödinger không phụ thuộc thời gian (41.5) được viết lại dưới dạng:

$$
\nabla^2\psi = -\frac{2mE}{\hbar^2}\psi
$$

Theo giả thiết đề bài, cả ba đạo hàm riêng bậc hai của hàm sóng đều dương, do đó vế trái của phương trình mang giá trị dương:

$$
\frac{\partial^2\psi}{\partial x^2} + \frac{\partial^2\psi}{\partial y^2} + \frac{\partial^2\psi}{\partial z^2} > 0
$$

Từ đó suy ra vế phải cũng phải mang giá trị dương:

$$
-\frac{2mE}{\hbar^2}\psi > 0
$$

Vì năng lượng của hạt thỏa mãn $E > 0$ và khối lượng $m > 0$, đại lượng $-2mE/\hbar^2$ mang dấu âm. Để tích của một số âm với hàm sóng $\psi(x, y, z)$ cho ra kết quả dương, bản thân hàm sóng $\psi(x, y, z)$ bắt buộc phải nhận giá trị âm trong toàn bộ vùng không gian đang xét. Do đó, phương án (ii) là kết luận chuẩn xác.
:::
