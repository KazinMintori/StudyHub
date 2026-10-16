## 40.2. Hạt trong hộp thế

Một bài toán nền tảng của cơ học lượng tử là sử dụng phương trình Schrödinger không phụ thuộc thời gian để xác định các mức năng lượng khả dĩ cùng hàm sóng tương ứng cho các hệ vật lý khác nhau. Với một hàm thế năng $U(x)$ cho trước, nhiệm vụ trọng tâm là tìm các hàm sóng trạng thái dừng $\psi(x)$ cùng các giá trị năng lượng $E$ đi kèm.

Đối với một hạt tự do chuyển động trong không gian không có lực tác dụng, thế năng bằng 0 ở mọi nơi ($U(x) = 0$). Các hàm sóng trạng thái dừng và mức năng lượng tương ứng có dạng:

$$
\begin{aligned}
\psi(x) &= A e^{ikx}, \\
E &= \frac{\hbar^2 k^2}{2m}
\end{aligned} \tag{40.24}
$$

Trong đó: Số sóng $k$ liên hệ với bước sóng $\lambda$ qua hệ thức $k = 2\pi/\lambda$. Do số sóng $k$ có thể nhận giá trị thực bất kỳ, năng lượng $E$ của hạt tự do có thể biến thiên liên tục từ 0 đến vô hạn. Mật độ xác suất tìm thấy hạt $|\psi(x)|^2 = |A|^2$ là đồng đều trên toàn bộ trục $x$, phản ánh một trạng thái hoàn toàn không bị giam giữ và không thể chuẩn hóa trên toàn bộ đường thẳng thực.

Bây giờ, chúng ta khảo sát một mô hình đơn giản trong đó hạt bị liên kết trong một vùng không gian giới hạn và không thể thoát ra xa vô cực. Hệ gồm một hạt chuyển động một chiều dọc theo trục $x$, bị giam giữa hai bức tường cứng cách nhau một khoảng $L$. Các bức tường đặt tại tọa độ $x = 0$ và $x = L$. Thế năng tại vị trí các bức tường cứng là vô hạn ($U = \infty$), ngăn cản hoàn toàn hạt vượt ra ngoài. Trong khoảng giữa hai bức tường, thế năng bằng 0 ($U = 0$). Mô hình này được gọi là **hạt trong hộp** hay **giếng thế sâu vô hạn một chiều**. Mô hình này có thể mô tả gần đúng một electron tự do di chuyển dọc theo mạch polymer liên hợp dài hoặc trong một dây dẫn nano rất mảnh.

![Hình 40.8: Quan niệm cơ học cổ điển Newton về một hạt có khối lượng m chuyển động qua lại giữa hai bức tường cứng cách nhau khoảng L với tốc độ không đổi.](../img/young-40/hinh-40-08.png)

![Hình 40.9: Hàm thế năng của một hạt trong hộp một chiều: Thế năng U(x) bằng 0 trong khoảng 0 < x < L và bằng vô hạn ở mọi vị trí bên ngoài khoảng này.](../img/young-40/hinh-40-09.png)

### Hàm sóng của hạt trong hộp

Để giải phương trình Schrödinger cho hệ này, trước hết ta xét các điều kiện vật lý áp đặt lên hàm sóng trạng thái dừng $\psi(x)$. Do hạt bị giam giữ hoàn toàn trong khoảng $0 \le x \le L$, xác suất tìm thấy hạt bên ngoài vùng này phải bằng 0, kéo theo hàm sóng $\psi(x) = 0$ với mọi $x < 0$ và $x > L$. Kết quả này hoàn toàn phù hợp với phương trình Schrödinger: Muốn tích số $U(x)\psi(x)$ trong phương trình không bị phân kỳ tại những nơi thế năng $U(x)$ tiến tới vô hạn, hàm sóng $\psi(x)$ bắt buộc phải triệt tiêu tại đó.

Hơn nữa, để là một nghiệm vật lý chấp nhận được, $\psi(x)$ phải là một hàm liên tục trên toàn miền xác định. Tính liên tục tại hai mép biên đòi hỏi hàm sóng phải triệt tiêu ngay tại các điểm ranh giới:

$$
\psi(0) = 0 \quad \text{và} \quad \psi(L) = 0
$$

Hai điều kiện này đóng vai trò là các điều kiện biên của bài toán. Chúng tương tự như điều kiện biên hai đầu cố định khi khảo sát sóng dừng và các họa tần chuẩn trên sợi dây đàn hồi.

Một điều kiện bổ sung quan trọng: Để đạo hàm bậc hai $d^2\psi(x)/dx^2$ tồn tại, đạo hàm bậc nhất $d\psi(x)/dx$ cũng phải liên tục ở mọi nơi, ngoại trừ những điểm mà thế năng trở nên vô hạn (chính là tại hai thành hộp). Điều này tương đương với yêu cầu một sợi dây dao động không thể bị gập gãy đột ngột tại bất kỳ điểm nào giữa hai đầu dây.

![Hình 40.10: Các họa tần chuẩn của một sợi dây có chiều dài L cố định tại hai đầu: Chiều dài dây bằng một số nguyên lần nửa bước sóng, hai đầu là hai nút sóng.](../img/young-40/hinh-40-10.png)

Bây giờ ta giải phương trình Schrödinger trong khoảng $0 \le x \le L$. Trong vùng này $U(x) = 0$, phương trình Schrödinger không phụ thuộc thời gian có dạng:

$$
-\frac{\hbar^2}{2m}\frac{d^2\psi(x)}{dx^2} = E\psi(x) \tag{40.25}
$$

Phương trình (40.25) có dạng toán học tương tự như phương trình của hạt tự do, nhưng hàm sóng đơn lẻ dạng sóng chạy $\psi(x) = A e^{ikx}$ không thể thỏa mãn đồng thời hai điều kiện biên. Tại $x = 0$, hàm sóng này bằng $A e^0 = A$. Tại $x = L$, nó bằng $A e^{ikL}$. Nếu ép hai giá trị này bằng 0 thì đòi hỏi biên độ $A = 0$, dẫn đến hàm sóng triệt tiêu $\psi(x) = 0$ trên toàn không gian. Hàm sóng triệt tiêu đồng nhất không thể chuẩn hóa được ($\int |\psi|^2 dx = 0 \ne 1$), do đó không thể đại diện cho trạng thái vật lý của một hạt.

Nghiệm dừng tổng quát của phương trình tuyến tính (40.25) cho phép chồng hai sóng phẳng truyền ngược chiều nhau. Ta sẽ chọn các hệ số để tổng ấy thỏa điều kiện tại hai vách. Viết gọn $\psi=\psi(x)$:

$$
\psi = A_1 e^{ikx} + A_2 e^{-ikx} \tag{40.26}
$$

Hàm sóng này gồm một sóng truyền theo chiều dương trục $x$ với biên độ $A_1$ và một sóng truyền theo chiều âm trục $x$ với biên độ $A_2$. Hiện tượng này hoàn toàn tương tự như sự tạo thành sóng dừng trên sợi dây đàn hồi, vốn là kết quả của sự giao thoa giữa hai sóng hình sin lan truyền ngược chiều nhau. Năng lượng tương ứng với nghiệm chồng chập này vẫn là $E = \hbar^2 k^2/(2m)$, hoàn toàn giống như đối với từng sóng đơn lẻ.

Để áp dụng các điều kiện biên, ta biểu diễn nghiệm qua các hàm lượng giác bằng công thức Euler. Đặt hai thành phần sóng:

$$
\begin{aligned}
\psi_1(x) &= (A_1 + A_2)\cos kx, \\
\psi_2(x) &= i(A_1 - A_2)\sin kx
\end{aligned}
$$

Khi đó hàm sóng tổng cộng nhận dạng:

$$
\psi(x) = \psi_1(x) + \psi_2(x) \tag{40.27}
$$

Tại điểm biên $x = 0$, hàm sóng có giá trị:

$$
\psi(0) = A_1 + A_2 = 0
$$

Hệ thức trên kéo theo $A_2 = -A_1$. Thay hệ thức này trở lại vào phương trình (40.27), số hạng chứa $\cos kx$ triệt tiêu hoàn toàn và ta thu được:

$$
\begin{aligned}
\psi(x) &= 2iA_1 \sin kx \\
&= C\sin kx
\end{aligned} \tag{40.28}
$$

Trong đó: Ta đặt hằng số mới $C = 2iA_1$. Về mặt toán học, hằng số $C$ nói chung là một số phức. Do hàm sóng triệt tiêu $\psi(x) = 0$ không thể chuẩn hóa được, ta yêu cầu $C \ne 0$. Để thỏa mãn điều kiện biên thứ hai tại $x = L$, ta cần:

$$
\psi(L) = C\sin kL = 0
$$

Vì hằng số $C \ne 0$, phương trình lượng giác đòi hỏi $\sin kL = 0$, dẫn đến $kL = n\pi$. Với mỗi số nguyên dương $n = 1, 2, 3, \dots$, các giá trị khả dĩ của số sóng $k$ và bước sóng de Broglie $\lambda_n$ được lượng tử hóa:

$$
\begin{aligned}
k_n &= \frac{n\pi}{L}, \\
\lambda_n &= \frac{2\pi}{k_n} = \frac{2L}{n}
\end{aligned} \tag{40.29}
$$

Chiều rộng $L$ của hộp đúng bằng một số nguyên lần nửa bước sóng ($L = n\lambda_n/2$), hoàn toàn tương ứng với điều kiện sóng dừng trên sợi dây hai đầu cố định.

### Các mức năng lượng của hạt trong hộp

Năng lượng của hạt bên trong hộp hoàn toàn là động năng do thế năng bằng 0:

$$
p_n = \frac{h}{\lambda_n} = \frac{nh}{2L} \tag{40.30}
$$

Với mỗi số lượng tử $n = 1, 2, 3, \dots$, các mức năng lượng cho phép của một hạt trong hộp được xác định bởi:

$$
\begin{aligned}
E_n &= \frac{p_n^2}{2m} = \frac{n^2 h^2}{8mL^2} \\
&= \frac{n^2 \pi^2 \hbar^2}{2mL^2}
\end{aligned} \tag{40.31}
$$

Mỗi mức năng lượng tương ứng với một giá trị của số lượng tử $n = 1, 2, 3, \dots$ và một hàm sóng trạng thái dừng riêng biệt:

$$
\psi_n(x) = C\sin\frac{n\pi x}{L} \tag{40.32}
$$

![Hình 40.11: Sơ đồ mức năng lượng và hàm sóng dừng của hạt trong hộp. Phần (a) biểu diễn các mức năng lượng tỷ lệ với bình phương số lượng tử. Phần (b) biểu diễn các hàm sóng từ n = 1 đến n = 5 được tịnh tiến theo phương đứng.](../img/young-40/hinh-40-11.png)

Năng lượng của hạt tỷ lệ với $n^2$, do đó khoảng cách giữa hai mức năng lượng kế tiếp nhau càng lên cao càng dãn rộng. Do các bức tường cứng hoàn hảo, hệ có vô số mức năng lượng gián đoạn. Ngay cả hạt có động năng cực lớn cũng không thể thoát khỏi hộp.

::: warning Thận trọng: Hạt trong hộp không thể có năng lượng bằng không
Năng lượng của một hạt bị giam trong hộp thế không bao giờ có thể bằng 0. Để $E = 0$ thì phương trình (40.31) đòi hỏi $n = 0$, nhưng khi thay $n = 0$ vào phương trình (40.32) ta nhận được $\psi(x) = C\sin(0) = 0$ ở mọi nơi. Một hàm sóng triệt tiêu đồng nhất $\psi(x) = 0$ không thể thỏa mãn điều kiện chuẩn hóa tích phân bằng 1, do đó không thể đại diện cho trạng thái của một hạt.

Kết luận cũng phù hợp nguyên lý bất định. Nếu động năng bằng không một cách xác định, phân bố động lượng chỉ còn giá trị không. Khi ấy, độ phân tán động lượng bằng không không thể đi cùng một trạng thái chuẩn hóa bị giới hạn trong hộp hữu hạn.

Mức thấp nhất $E_1>0$ vì vậy được gọi là **năng lượng điểm không**, với mốc thế năng trong hộp bằng không. Các hàm sin có thể khai triển thành hai thành phần sóng chạy ngược chiều và cùng độ lớn biên độ trên khoảng của hộp. Đây là chồng chập biên độ, không phải một hỗn hợp thống kê của hai quỹ đạo.

Trạng thái dừng có động lượng trung bình bằng không nhưng độ phân tán khác không. Muốn suy ra toàn bộ phân bố của một phép đo động lượng, còn phải nêu cách đo và điều kiện giam giữ. Phép khai triển sóng đứng riêng lẻ không thay thế được bước ấy.
:::

### Ứng dụng: Hạt trong "hộp" polymer

Polyacetylene là một đại diện tiêu biểu của nhóm polymer hữu cơ dẫn điện dạng mạch dài. Phân tử này cấu tạo từ chuỗi liên kết luân phiên giữa các liên kết đơn và liên kết đôi carbon–carbon gồm các đơn vị monome $\mathrm{C_2H_2}$. Các electron $\pi$ có thể chuyển động tự do dọc theo chiều dài phân tử nhưng không thể rời khỏi mạch theo phương ngang. Do đó, toàn bộ phân tử đóng vai trò như một "hộp thế một chiều" giam giữ các electron. Chiều dài $L$ của phân tử tỷ lệ thuận với số lượng đơn vị monome ghép lại. Thực nghiệm quang phổ xác nhận rằng các mức năng lượng của electron trong polyacetylene tuân theo rất sát phương trình (40.31): Chiều dài phân tử $L$ càng lớn thì năng lượng các mức càng thấp và khoảng cách giữa các mức năng lượng càng thu hẹp lại.

![Ứng dụng: Cấu trúc polyacetylene gồm những đơn vị monome C₂H₂. Các liên kết đơn và đôi xen kẽ, còn electron bị giới hạn dọc theo chiều dài L của phân tử như hạt trong hộp một chiều.](../img/young-40/ung-dung-polyacetylene.png)

---

### Ví dụ 40.3: Electron trong hộp có kích thước nguyên tử

Xét một electron bị giam giữ trong một hộp thế một chiều có chiều rộng $L = 5{,}0 \times 10^{-10}\text{ m}$ (xấp xỉ đường kính của một nguyên tử). Hãy xác định giá trị của hai mức năng lượng đầu tiên $E_1$ và $E_2$.

#### Nhận dạng và thiết lập bài toán

Bài toán yêu cầu tính các mức năng lượng khả dĩ của một electron bị giam giữ trong hộp thế một chiều. Hai mức năng lượng đầu tiên tương ứng với số lượng tử $n = 1$ và $n = 2$ trong phương trình (40.31). Khối lượng của electron là $m = 9{,}109 \times 10^{-31}\text{ kg}$ và hằng số Planck là $h = 6{,}626 \times 10^{-34}\text{ J}\cdot\text{s}$.

#### Lời giải chi tiết

Áp dụng phương trình (40.31) cho trạng thái cơ bản ($n = 1$). Thay các giá trị số $m = 9{,}109 \times 10^{-31}\text{ kg}$, $h = 6{,}626 \times 10^{-34}\text{ J}\cdot\text{s}$ và $L = 5{,}0 \times 10^{-10}\text{ m}$:

$$
\begin{aligned}
E_1 &= \frac{h^2}{8mL^2} \\
&= 2{,}41 \times 10^{-19}\text{ J} \\
&= 1{,}5\text{ eV}
\end{aligned}
$$

Với mức năng lượng thứ hai ($n = 2$):

$$
\begin{aligned}
E_2 &= 2^2 E_1 \\
&= 4(2{,}41 \times 10^{-19}\text{ J}) \\
&= 9{,}64 \times 10^{-19}\text{ J} \\
&= 6{,}0\text{ eV}
\end{aligned}
$$

#### Đánh giá và thảo luận mở rộng

Hiệu năng lượng giữa hai mức đầu tiên là:

$$
\begin{aligned}
\Delta E &= E_2 - E_1 \\
&= 6{,}0\text{ eV} - 1{,}5\text{ eV} \\
&= 4{,}5\text{ eV}
\end{aligned}
$$

Dù electron bị giam trong hộp có thế năng thành giếng sâu vô hạn khác với thế năng Coulomb hút electron trong nguyên tử thực tế, giá trị hiệu năng lượng này cùng bậc độ lớn với khoảng cách giữa các mức năng lượng quang phổ trong nguyên tử thực tế (vài electron-volt).

Để thấy rõ sự phụ thuộc của năng lượng vào khối lượng và kích thước hệ, ta so sánh với hai trường hợp sau:

- **Hạt nucleon trong hạt nhân nguyên tử**: Một proton hoặc neutron ($m = 1{,}67 \times 10^{-27}\text{ kg}$) bị giam trong một hộp thế có kích thước hạt nhân $L = 1{,}1 \times 10^{-14}\text{ m}$. Tính toán cho thấy năng lượng trạng thái cơ bản lớn hơn khoảng một triệu lần: $E_1 = 1{,}7\text{ MeV}$, $E_2 = 4E_1 = 6{,}8\text{ MeV}$, và $\Delta E = 5{,}1\text{ MeV}$. Điều này giải thích tại sao các phản ứng hạt nhân giải phóng năng lượng lớn hơn hàng triệu lần so với phản ứng hóa học thông thường.
- **Vật thể vĩ mô**: Một quả bóng bi-a ($m = 0{,}2\text{ kg}$) chuyển động trong một hộp có chiều rộng $L = 1{,}3\text{ m}$ (chiều rộng bàn bi-a). Khoảng cách giữa các mức năng lượng kế tiếp nhau chỉ vào khoảng $5 \times 10^{-67}\text{ J}$. Khoảng cách này quá nhỏ đến mức không một thiết bị đo lường nào có thể phát hiện được tính gián đoạn, cho thấy tính chất lượng tử hoàn toàn hòa vào cơ học cổ điển ở thế giới vĩ mô.

::: tip Khái niệm cần nhớ
Các hàm sóng trạng thái dừng của hạt trong hộp một chiều là các sóng dừng hình sin bên trong hộp với nút sóng tại hai thành biên. Hàm sóng triệt tiêu bên ngoài hộp. Trạng thái dừng thứ $n$ chứa $n$ nửa bước sóng và có năng lượng tỷ lệ với $n^2$. Hệ sở hữu vô số trạng thái dừng rời rạc.
:::

---

### Xác suất và sự chuẩn hóa hàm sóng

Ý nghĩa thống kê của cơ học lượng tử chỉ ra rằng đại lượng $|\psi(x)|^2 dx$ tỷ lệ thuận với xác suất tìm thấy hạt trong một khoảng vi phân $dx$ quanh tọa độ $x$. Đối với hạt trong hộp thế, mật độ xác suất tìm thấy hạt trong trạng thái thứ $n$ có dạng:

$$
|\psi_n(x)|^2 = C^2 \sin^2\frac{n\pi x}{L}
$$

![Hình 40.12: Đồ thị so sánh giữa hàm sóng và hàm mật độ xác suất cho ba trạng thái đầu tiên n = 1, 2, 3 của hạt trong hộp thế: Phần (a) biểu diễn hàm sóng trạng thái dừng. Phần (b) biểu diễn hàm mật độ xác suất.](../img/young-40/hinh-40-12.png)

Trong cơ học cổ điển, một hạt chuyển động nảy qua lại giữa hai bức tường với vận tốc không đổi có xác suất xuất hiện hoàn toàn đồng đều ở mọi vị trí giữa 0 và $L$. Trái lại, trong cơ học lượng tử, mật độ xác suất biến thiên theo dạng hình sin bình phương và triệt tiêu tại các nút sóng.

Do hạt bắt buộc phải tồn tại ở một nơi nào đó trên trục $x$ (giữa $-\infty$ và $+\infty$), tổng xác suất tìm thấy hạt trên toàn bộ không gian phải bằng đúng $1$:

$$
\int_{-\infty}^\infty |\psi(x)|^2\,dx = 1 \tag{40.33}
$$

Điều kiện này được gọi là **điều kiện chuẩn hóa** của hàm sóng. Vì hàm sóng của hạt trong hộp triệt tiêu bên ngoài khoảng $[0, L]$, phương trình (40.33) thu gọn về:

$$
\int_0^L C^2 \sin^2\frac{n\pi x}{L} dx = 1 \tag{40.34}
$$

Sử dụng công thức lượng giác hạ bậc $\sin^2\theta = \frac{1}{2}(1 - \cos 2\theta)$, tích phân trên cho kết quả $|C|^2 \frac{L}{2} = 1 \implies |C| = \sqrt{\frac{2}{L}}$. Ta chọn thừa số pha quy ước sao cho $C$ là số thực dương $C = \sqrt{2/L} > 0$.

Bộ hàm sóng trạng thái dừng đã chuẩn hóa hoàn chỉnh của hạt trong hộp với $n = 1, 2, 3, \dots$ là:

$$
\psi_n(x) = \sqrt{\frac{2}{L}}\sin\frac{n\pi x}{L} \tag{40.35}
$$

---

### Ví dụ 40.4: Một hàm sóng không mang dạng hình sin?

Xét một hạt trong hộp thế có chiều rộng $L$ ($0 \le x \le L$).

1. Hãy chứng minh rằng hàm số $\psi(x) = Ax + B$ (với $A$ và $B$ là các hằng số) là một nghiệm của phương trình Schrödinger cho mức năng lượng $E = 0$.
2. Hãy xác định các điều kiện biên tại $x = 0$ và $x = L$ áp đặt những ràng buộc gì lên các hằng số $A$ và $B$.

#### Nhận dạng và thiết lập bài toán

Một hàm sóng chỉ có ý nghĩa vật lý khi thỏa mãn đồng thời hai tiêu chuẩn: Thỏa mãn phương trình Schrödinger và thỏa mãn các điều kiện biên tương ứng của hệ. Ở câu thứ nhất, ta thay trực tiếp $\psi(x)$ vào phương trình Schrödinger (40.25) với $E = 0$. Ở câu thứ hai, ta kiểm tra các điều kiện biên triệt tiêu tại hai thành hộp: $\psi(0) = 0$ và $\psi(L) = 0$.

#### Lời giải chi tiết

1. Với mức năng lượng $E = 0$, phương trình Schrödinger (40.25) trong khoảng $0 \le x \le L$ trở thành:

$$
-\frac{\hbar^2}{2m}\frac{d^2\psi(x)}{dx^2} = 0
$$

Đạo hàm bậc nhất của hàm số $\psi(x) = Ax + B$ là $\frac{d\psi(x)}{dx} = A$, do đó đạo hàm bậc hai bằng:

$$
\frac{d^2\psi(x)}{dx^2} = 0
$$

Vế trái của phương trình Schrödinger hoàn toàn bằng 0, trùng với vế phải. Do đó, hàm số tuyến tính $\psi(x) = Ax + B$ là một nghiệm toán học chính xác của phương trình Schrödinger ứng với mức năng lượng $E = 0$. Cả hàm sóng và đạo hàm bậc nhất của nó đều liên tục.

2. Áp dụng điều kiện biên thứ nhất tại $x = 0$:

$$
\psi(0) = B = 0
$$

Hệ thức này dẫn đến $\psi(x) = Ax$ trên toàn miền. Áp dụng tiếp điều kiện biên thứ hai tại $x = L$:

$$
\psi(L) = AL = 0
$$

Vì bề rộng của hộp $L > 0$, điều kiện này bắt buộc hằng số $A = 0$. Hệ quả là hàm sóng $\psi(x) = 0$ tại mọi vị trí bên trong cũng như bên ngoài hộp. Một hàm sóng triệt tiêu đồng nhất $\psi(x) = 0$ có tích phân mật độ xác suất bằng 0, không thể chuẩn hóa về 1, do đó không thể mô tả trạng thái của hạt bị giam giữ.

#### Đánh giá và bài học phương pháp

Có rất nhiều hàm toán học có thể thỏa mãn phương trình vi phân Schrödinger của một hệ cơ học lượng tử, nhưng đa số các nghiệm toán học đó phải bị loại bỏ vì không đáp ứng được các điều kiện biên vật lý của bài toán.

::: tip Khái niệm cần nhớ
Một hàm sóng trạng thái dừng chỉ có ý nghĩa vật lý thực tế khi thỏa mãn đồng thời cả phương trình vi phân Schrödinger lẫn tất cả các điều kiện biên áp đặt lên hệ.
:::

---

### Sự phụ thuộc thời gian của trạng thái dừng

Hàm sóng $\psi_n(x)$ trong phương trình (40.35) chỉ phụ thuộc vào tọa độ không gian $x$. Đặt tần số góc dao động $\omega_n = E_n/\hbar$, hàm sóng phụ thuộc thời gian đầy đủ $\Psi_n(x, t)$ ứng với $n = 1, 2, 3, \dots$ nhận biểu thức:

$$
\Psi_n(x, t) = \psi_n(x) e^{-i\omega_n t} \tag{40.36}
$$

Khi tính mật độ xác suất tìm thấy hạt:

$$
|\Psi_n(x, t)|^2 = \frac{2}{L}\sin^2\frac{n\pi x}{L}
$$

Thừa số pha thời gian có bình phương môđun bằng một. Do đó, mật độ xác suất không phụ thuộc thời gian, dù hàm sóng phức vẫn đổi pha. Tính chất ấy giải thích tên gọi **trạng thái dừng**.

---

### Câu hỏi tự kiểm tra 40.2

Nếu một hạt bị giam trong hộp thế đang ở mức năng lượng thứ $n$, giá trị trung bình của thành phần động lượng theo trục $x$ (ký hiệu $\langle p_x \rangle$) bằng bao nhiêu?

- (i) $\frac{nh}{2L}$
- (ii) $\frac{1}{2}\frac{nh}{L}$
- (iii) $\frac{1}{\sqrt{2}}\frac{nh}{L}$
- (iv) $\frac{1}{2\sqrt{2}}\frac{nh}{L}$
- (v) Bằng 0

::: details Lời giải và giải thích
**Đáp án đúng:** Bằng 0, tức phương án (v).

**Giải thích chi tiết**: Quá trình thiết lập hàm sóng trạng thái dừng cho thấy mỗi trạng thái dừng là một sóng dừng có mật độ dòng xác suất triệt tiêu và giá trị trung bình của động lượng $\langle p_x \rangle = 0$ do tính đối xứng không gian:

$$
\langle p_x \rangle = 0
$$

Hai sóng chạy thành phần trong sự chồng chập mang động lượng đối nhau $+p_n = +nh/(2L)$ và $-p_n = -nh/(2L)$ với trọng số biên độ bằng nhau tuyệt đối. Chú ý rằng vì hạt bị giam giữ trong khoảng hữu hạn $[0, L]$, phổ xung lượng thu được từ phép biến đổi Fourier của $\psi_n(x)$ là một phân bố liên tục chứ không phải chỉ gồm hai vạch delta gián đoạn.
:::
