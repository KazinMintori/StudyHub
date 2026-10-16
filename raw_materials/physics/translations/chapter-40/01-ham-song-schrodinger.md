## 40.1. Hàm sóng và phương trình Schrödinger một chiều

Ở quy mô nguyên tử và hạt hạ nguyên tử, các thực thể vật chất như electron không thể được mô tả đơn thuần như những chất điểm cổ điển tuân theo cơ học Newton. Thay vào đó, ta bắt buộc phải tính đến đặc tính sóng của chúng. Trong mô hình nguyên tử hydro của Bohr, electron được hình dung như một hạt cổ điển chuyển động trên quỹ đạo tròn quanh hạt nhân. Mô hình này vận dụng hệ thức de Broglie giữa động lượng và bước sóng để giải thích tại sao chỉ các quỹ đạo có bán kính nhất định mới được phép tồn tại. Tuy nhiên, nguyên lý bất định Heisenberg chỉ rõ rằng một mô hình lai ghép nửa cổ điển nửa lượng tử như vậy không thể hoàn toàn chính xác.

Phương pháp tiếp cận toàn diện của cơ học lượng tử mô tả trọn vẹn trạng thái của hạt bằng ngôn ngữ sóng. Cách mô tả mới này thay thế lược đồ cổ điển vốn xác định trạng thái của hạt bằng tọa độ và các thành phần vận tốc.

Ngôn ngữ mới của cơ học lượng tử có nhiều nét tương đồng sâu sắc với lý thuyết sóng cổ điển. Đối với sóng cơ học trên một sợi dây, vị trí của từng điểm trên dây tại mỗi thời điểm được xác định thông qua hàm sóng $y(x, t)$ biểu diễn độ dịch chuyển khỏi vị trí cân bằng của phần tử dây tại tọa độ $x$ ở thời điểm $t$ (Hình 40.1). Khi đã biết hàm sóng của một chuyển động sóng, ta nắm giữ mọi thông tin vật lý của chuyển động đó, chẳng hạn như vận tốc và gia tốc của mọi điểm trên dây tại thời điểm bất kỳ. Đối với sóng âm, hàm sóng biểu diễn sự biến thiên áp suất theo tọa độ và thời gian. Đối với sóng điện từ, hai hàm sóng vector được dùng để mô tả điện trường và từ trường.

![Hình 40.1: Hai đứa trẻ đang nói chuyện qua chiếc "điện thoại" ống bơ nối dây. Độ dịch chuyển của từng điểm trên sợi dây được mô tả trọn vẹn bằng hàm sóng $y(x, t)$. Tương tự như vậy, trạng thái của một hạt vi mô được mô tả hoàn chỉnh bằng hàm sóng cơ học lượng tử $\Psi(x, y, z, t)$.](../img/young-40/hinh-40-01.png)

Ta dùng chữ cái Hy Lạp psi để ký hiệu hàm sóng. Chữ hoa $\Psi$ chỉ hàm phụ thuộc tọa độ không gian và thời gian, còn chữ thường $\psi$ chỉ phần không phụ thuộc thời gian trong những nghiệm tách biến. Trong mô hình một hạt đang xét, hàm sóng cho thông tin về trạng thái, thay cho một quỹ đạo có tọa độ và vận tốc xác định.

::: warning Cảnh báo: Sóng hạt khác biệt căn bản với sóng cơ học
Khác với sóng truyền trên dây hay sóng âm trong không khí, hàm sóng của một hạt không phải là sóng cơ học cần một môi trường vật chất đàn hồi để lan truyền. Hàm sóng mô tả trạng thái của hạt, nhưng ta không thể định nghĩa bản thân hàm sóng theo bất kỳ thực thể vật chất nào. Ta chỉ có thể mô tả mối liên hệ giữa hàm sóng với các hệ quả quan sát được trong thực nghiệm.
:::

### Sóng trong một chiều: Sóng trên dây

Hàm sóng của một hạt nhìn chung phụ thuộc vào cả ba chiều không gian. Để tiếp cận một cách sáng tỏ, ta khởi đầu bằng chuyển động một chiều, trong đó một hạt khối lượng $m$ chuyển động dọc theo trục $x$ và hàm sóng $\Psi$ chỉ phụ thuộc vào tọa độ $x$ cùng thời gian $t$.

Để hiểu dạng hình thức của sóng lượng tử, trước hết ta nhắc lại các tính chất của sóng trên dây đàn hồi. Mọi hàm sóng $y(x, t)$ mô tả sóng trên dây đều phải thỏa mãn phương trình sóng cổ điển:

$$
\frac{\partial^2 y}{\partial x^2} = \frac{1}{v^2} \frac{\partial^2 y}{\partial t^2} \tag{40.1}
$$

Trong đó $v$ là tốc độ lan truyền của sóng, có giá trị không đổi đối với mọi bước sóng. Xét trường hợp sóng hình sin có bước sóng $\lambda$ và tần số $f$ lan truyền theo chiều dương trục $x$ dọc theo sợi dây:

$$
y = A \cos\phi + B \sin\phi \tag{40.2}
$$

Ở đây $\phi = kx - \omega t$ là góc pha, $k = 2\pi/\lambda$ là số sóng, và $\omega = 2\pi f$ là tần số góc. Các hằng số $A$ và $B$ xác định biên độ cùng pha ban đầu của sóng. Biểu thức (40.2) là một hàm sóng hợp lệ khi và chỉ khi nó thỏa mãn phương trình sóng (40.1). Lấy đạo hàm riêng bậc nhất và bậc hai của $y$ theo tọa độ $x$:

$$
\frac{\partial y}{\partial x} = k(B\cos\phi - A\sin\phi) \tag{40.3a}
$$

$$
\frac{\partial^2 y}{\partial x^2} = -k^2 y \tag{40.3b}
$$

Tiếp tục lấy đạo hàm riêng bậc nhất và bậc hai của $y$ theo thời gian $t$:

$$
\frac{\partial y}{\partial t} = \omega(A\sin\phi - B\cos\phi) \tag{40.3c}
$$

$$
\frac{\partial^2 y}{\partial t^2} = -\omega^2 y \tag{40.3d}
$$

Thay hai kết quả đạo hàm bậc hai (40.3b) và (40.3d) vào phương trình sóng (40.1):

$$
-k^2 y = -\frac{\omega^2}{v^2} y \tag{40.4}
$$

Phương trình này nghiệm đúng với mọi tọa độ $x$ và thời gian $t$ khi và chỉ khi:

$$
\omega^2 = v^2 k^2 \iff \omega = vk \tag{40.5}
$$

Hệ thức (40.5) khẳng định tần số góc $\omega$ tỷ lệ thuận bậc nhất với số sóng $k$. Vì vận tốc pha $v = \omega/k$ là hằng số, mọi sóng thành phần trên dây đều truyền đi với cùng một tốc độ, không phụ thuộc bước sóng.

### Hàm sóng của hạt tự do và phương trình Schrödinger

Bây giờ ta áp dụng quy trình tương tự để tìm phương trình sóng mô tả một hạt tự do. Hạt tự do là hạt chuyển động trong không gian mà không chịu tác dụng của bất kỳ lực nào, đồng nghĩa thế năng $U(x) = 0$ trên toàn bộ không gian. Trong cơ học phi tương đối tính, toàn bộ năng lượng của hạt là động năng:

$$
E = \frac{p^2}{2m} \tag{40.6}
$$

Quy ước mốc năng lượng này không bao gồm năng lượng nghỉ $mc^2$ của thuyết tương đối hẹp. Theo các hệ thức de Broglie, động lượng và năng lượng của hạt liên hệ với số sóng $k = 2\pi/\lambda$ và tần số góc $\omega = 2\pi f$:

$$
E = \hbar\omega \tag{40.7a}
$$

$$
p = \hbar k \tag{40.7b}
$$

Trong đó hằng số Planck rút gọn $\hbar = h/(2\pi)$ có giá trị bằng $1{,}055 \times 10^{-34}\,\mathrm{J\cdot s}$. Thay các biểu thức (40.7a) và (40.7b) vào phương trình năng lượng (40.6), ta tìm được mối liên hệ giữa $\omega$ và $k$ cho một hạt tự do:

$$
\hbar\omega = \frac{\hbar^2 k^2}{2m} \tag{40.8}
$$

Phương trình (40.8) cho thấy một khác biệt rất lớn so với sóng trên dây: Đối với sóng vật chất, tần số góc $\omega$ tỷ lệ thuận với bình phương số sóng $k^2$, chứ không tỷ lệ thuận bậc nhất với $k$. Phương trình sóng cơ học (40.1) chứa đạo hàm bậc hai theo thời gian dẫn đến $\omega^2 \propto k^2$, do đó không thể dùng để mô tả hạt lượng tử. Phương trình mà ta tìm kiếm bắt buộc phải dẫn đến hệ thức tán sắc (40.8).

Để tìm phương trình này, ta xét một hàm sóng hình sin cho hạt tự do với $\phi = kx - \omega t$:

$$
\Psi = A \cos\phi + B \sin\phi \tag{40.9}
$$

Số sóng $k$ và tần số góc $\omega$ trong biểu thức (40.9) phải thỏa mãn hệ thức (40.8). Từ kết quả đạo hàm bậc hai theo tọa độ trong biểu thức (40.3b), việc lấy đạo hàm bậc hai của $\Psi$ theo $x$ đưa ra thừa số $-k^2$:

$$
-\frac{\hbar^2}{2m} \frac{\partial^2 \Psi}{\partial x^2} = \frac{\hbar^2 k^2}{2m} \Psi \tag{40.10}
$$

Vế phải của đẳng thức (40.10) chứa đúng thừa số $\hbar^2 k^2/(2m) = \hbar\omega$. Trong khi đó, đạo hàm riêng bậc nhất theo thời gian của $\Psi$ ở biểu thức (40.3c) đưa ra thừa số $\omega$. Điều này gợi ý rằng phương trình sóng cần tìm có dạng đạo hàm bậc hai theo không gian ở vế trái và đạo hàm bậc nhất theo thời gian ở vế phải:

$$
-\frac{\hbar^2}{2m} \frac{\partial^2 \Psi}{\partial x^2} = C\hbar \frac{\partial \Psi}{\partial t} \tag{40.11}
$$

Trong đó $C$ là một hằng số chưa biết. Để thấy rõ phép thế mà vẫn theo dõi được từng thành phần, đặt

$$
F=A\cos\phi+B\sin\phi.
$$

$$
G=A\sin\phi-B\cos\phi.
$$

$F$ là chính hàm sóng đang xét, còn $\omega G$ là đạo hàm theo thời gian của nó. Thay vào (40.11):

$$
\frac{\hbar^2k^2}{2m}F=C\hbar\omega G.
\tag{40.12}
$$

Do $\hbar\omega = \hbar^2 k^2 / (2m)$, ta triệt tiêu thừa số chung ở hai vế:

$$
F=CG.
\tag{40.13}
$$

Khai triển lại $F$ và $G$ đã định nghĩa, hệ số của $\cos\phi$ bên trái là $A$, còn bên phải là $-CB$. Hệ số của $\sin\phi$ lần lượt là $B$ và $CA$. Vì đẳng thức phải đúng với mọi pha, ta có

$$
A = -CB \tag{40.14a}
$$

$$
B = CA \tag{40.14b}
$$

Thay biểu thức $B$ từ (40.14b) vào (40.14a), ta thu được $A = -C(CA) = -C^2 A$, suy ra $C^2 = -1$. Về mặt đại số thuần túy, phương trình này có hai nghiệm phức $C = \pm i$. Việc lựa chọn $C = i$ là một quy ước chuẩn mực và nhất quán trong toàn bộ cơ học lượng tử hiện đại. Lựa chọn này gắn liền chặt chẽ với quy ước pha phụ thuộc thời gian $e^{-i\omega t} = e^{-iEt/\hbar}$ cho các trạng thái có năng lượng dương $E > 0$. Nếu chọn $C = -i$, vế phải của phương trình sẽ đổi dấu và tương ứng với thừa số pha ngược lại $e^{+iEt/\hbar}$. Đặt $C = i$ vào phương trình (40.11), ta nhận được phương trình cơ bản:

$$
-\frac{\hbar^2}{2m} \frac{\partial^2 \Psi}{\partial x^2} = i\hbar \frac{\partial \Psi}{\partial t} \tag{40.15}
$$

Phương trình (40.15) chính là **phương trình Schrödinger một chiều cho hạt tự do**, do nhà vật lý người Áo Erwin Schrödinger thiết lập vào năm 1926 (Hình 40.2).

![Hình 40.2: Erwin Schrödinger (1887–1961), nhà vật lý người Áo đã xây dựng phương trình mang tên ông vào năm 1926. Thành tựu này mang lại cho ông giải Nobel Vật lý năm 1933 (cùng với P. A. M. Dirac). Tấm bia mộ của ông được khắc một dị bản của phương trình (40.15).](../img/young-40/hinh-40-02.png)

Sự xuất hiện của đơn vị ảo $i$ trong phương trình (40.15) có nghĩa là nghiệm của phương trình Schrödinger nhìn chung phải là những hàm số phức. Từ điều kiện $C = i$ và hệ thức (40.14b), ta có $B = iA$. Khi đó hàm sóng (40.9) trở thành:

$$
\Psi = A(\cos\phi + i \sin\phi) \tag{40.16}
$$

Bằng cách chọn pha tổng quát (overall phase) của trạng thái sao cho hằng số biên độ $A$ là một số thực, hàm sóng này gồm phần thực $\mathrm{Re}\,\Psi = A \cos(kx - \omega t)$ và phần ảo $\mathrm{Im}\,\Psi = A \sin(kx - \omega t)$ (Hình 40.3). Nếu $A$ là một số phức tổng quát với pha $\alpha$, phần thực và phần ảo sẽ chứa độ dịch pha ban đầu $\alpha$ tương ứng.

![Hình 40.3: Đồ thị hàm sóng không gian $\Psi(x, 0) = A e^{ikx}$ của một hạt tự do có động lượng xác định $p = \hbar k$. Hàm sóng là một đại lượng phức với phần thực $\mathrm{Re}\,\Psi(x, 0) = A\cos(kx)$ và phần ảo $\mathrm{Im}\,\Psi(x, 0) = A\sin(kx)$ được vẽ tại thời điểm $t = 0$ theo tọa độ $x$.](../img/young-40/hinh-40-03.png)

Vận dụng công thức Euler cho số phức với góc pha $\theta$:

$$
\begin{aligned}
e^{i\theta} &= \cos\theta + i\sin\theta, \\
e^{-i\theta} &= \cos\theta - i\sin\theta
\end{aligned} \tag{40.17}
$$

Hàm sóng điều hòa của hạt tự do được viết lại ở dạng số mũ phức:

$$
\Psi(x, t) = A e^{i(kx - \omega t)} \tag{40.18}
$$

Biểu thức này cũng có thể viết thành $\Psi(x, t) = A e^{ikx} e^{-i\omega t}$. Nếu số sóng $k$ dương, hàm sóng (40.18) mô tả hạt tự do chuyển động theo chiều dương trục $x$ với động lượng $p = \hbar k$ và năng lượng $E = \hbar\omega = \hbar^2 k^2 / (2m)$. Nếu $k$ âm, động lượng và chiều chuyển động của hạt hướng theo chiều âm trục $x$.

### Ý nghĩa xác suất của hàm sóng: Diễn giải Max Born

Trong lý thuyết sóng điện từ, bình phương biên độ điện trường tại một điểm tỷ lệ thuận với cường độ bức xạ, tức tỷ lệ thuận với số lượng photon đập vào một đơn vị diện tích xung quanh điểm đó trong một đơn vị thời gian. Tương tự như vậy, bình phương độ lớn của hàm sóng hạt tại mỗi điểm cung cấp thông tin về xác suất tìm thấy hạt xung quanh điểm đó.

Vì hàm sóng $\Psi(x, t)$ là một đại lượng phức, độ lớn được xác định bằng bình phương môđun $|\Psi(x, t)|^2$. Quy tắc này được nhà vật lý người Đức Max Born đề xuất vào năm 1926 (Hình 40.4).

![Hình 40.4: Năm 1926, nhà vật lý người Đức Max Born (1882–1970) đưa ra diễn giải xác suất mang tính nền tảng: $|\Psi|^2$ là hàm mật độ xác suất tìm thấy hạt được mô tả bởi hàm sóng $\Psi$. Ông cũng là người đặt ra thuật ngữ "cơ học lượng tử" (trong tiếng Đức là Quantenmechanik) và được trao giải Nobel Vật lý năm 1954.](../img/young-40/hinh-40-04.png)

Đối với một hạt chuyển động dọc theo trục $x$, đại lượng $|\Psi(x, t)|^2$ được gọi là **hàm mật độ xác suất**. Bình phương môđun được tính bằng tích của hàm sóng với liên hợp phức của nó:

$$
|\Psi(x, t)|^2 = \Psi^* \Psi
$$

Trong đó liên hợp phức $\Psi^*$ nhận được bằng cách thay $i$ bằng $-i$. Đối với sóng phẳng hạt tự do (40.18), liên hợp phức là $\Psi^*(x, t) = A^* e^{-i\phi}$, kéo theo:

$$
\begin{aligned}
|\Psi|^2 &= [A^* e^{-i\phi}] [A e^{i\phi}] \\
&= |A|^2
\end{aligned}
$$

Giá trị $|\Psi|^2 = |A|^2$ hoàn toàn độc lập với tọa độ $x$ và thời gian $t$. Kết quả này biểu thị một mật độ xác suất tương đối đồng đều trên toàn không gian. Trong khuôn khổ lý tưởng hóa của sóng phẳng đơn sắc lý tưởng (vốn không thể chuẩn hóa trên toàn bộ trục số thực), xác suất tương đối tìm thấy hạt trong một đoạn có độ dài $\Delta x$ cho trước là như nhau ở mọi vị trí trên trục $x$.

::: warning Cảnh báo: Phân biệt mật độ xác suất và xác suất trong một khoảng
Đại lượng $|\Psi(x, t)|^2$ là mật độ xác suất, có thứ nguyên là $1/\text{chiều dài}$ (đơn vị $\mathrm{m}^{-1}$ trong hệ SI). Bản thân $|\Psi(x, t)|^2$ không phải là xác suất không thứ nguyên. Xác suất tìm thấy hạt trong một khoảng vi phân giữa tọa độ $x$ và $x + dx$ tại thời điểm $t$ là:

$$
dP = |\Psi(x, t)|^2\,dx
$$

Xác suất tìm thấy hạt chính xác tại một điểm toán học duy nhất luôn bằng 0. Để tìm xác suất hạt nằm trong một khoảng tọa độ hữu hạn từ $x = a$ đến $x = b$, ta phải lấy tích phân của hàm mật độ xác suất:

$$
P(a \le x \le b) = \int_a^b |\Psi|^2\,dx
$$

Vì hạt chắc chắn phải nằm ở một vị trí nào đó trên toàn bộ trục tọa độ, tổng xác suất trên toàn không gian phải bằng 1:

$$
\int_{-\infty}^{\infty} |\Psi|^2\,dx = 1
$$

Đẳng thức này được gọi là **điều kiện chuẩn hóa** của hàm sóng. Sóng phẳng đơn sắc của hạt tự do ở phương trình (40.18) có mật độ xác suất không đổi $|A|^2$ trên toàn trục số, do đó tích phân trên toàn không gian phân kỳ tới vô hạn. Một sóng phẳng lý tưởng không thể chuẩn hóa được, phản ánh đúng nguyên lý bất định: Khi động lượng của hạt được xác định chính xác tuyệt đối ($\Delta p = 0$), vị trí của hạt hoàn toàn không xác định trên toàn vũ trụ ($\Delta x = \infty$).
:::

### Ví dụ 40.1: Giao thoa và vị trí của hạt tự do

Xét hàm sóng $\Psi(x, t) = \Psi_1 + \Psi_2$ là sự chồng chập của hai hàm sóng hạt tự do dạng (40.18), trong đó $\Psi_1 = A e^{i(k_1 x - \omega_1 t)}$ và $\Psi_2 = A e^{i(k_2 x - \omega_2 t)}$. Cả hai số sóng $k_1$ và $k_2$ đều là các số thực dương và phân biệt ($k_1 \ne k_2$, giả sử $k_2 > k_1$).

(a) Chứng minh rằng hàm sóng này thỏa mãn phương trình Schrödinger cho một hạt tự do khối lượng $m$.

(b) Tìm hàm mật độ xác suất $|\Psi(x, t)|^2$ của trạng thái chồng chập này.

::: details Lời giải chi tiết
**Nhận diện và thiết lập**: Cả hai hàm sóng thành phần $\Psi_1$ và $\Psi_2$ đều mô tả hạt chuyển động theo chiều dương trục $x$, nhưng với động lượng và năng lượng khác nhau: $p_1 = \hbar k_1$, $E_1 = \hbar\omega_1 = \hbar^2 k_1^2/(2m)$ cho sóng thứ nhất và $p_2 = \hbar k_2$, $E_2 = \hbar\omega_2 = \hbar^2 k_2^2/(2m)$ cho sóng thứ hai. Để kiểm tra hàm sóng chồng chập có thỏa mãn phương trình Schrödinger cho hạt tự do (40.15) hay không, ta thay trực tiếp $\Psi(x, t)$ vào hai vế của phương trình.

**Thực hiện**:

(a) Lấy đạo hàm riêng bậc hai của các sóng thành phần theo $x$:

$$
\begin{aligned}
\frac{\partial^2 \Psi_1}{\partial x^2} &= -k_1^2 \Psi_1, \\
\frac{\partial^2 \Psi_2}{\partial x^2} &= -k_2^2 \Psi_2
\end{aligned}
$$

Áp dụng toán tử cho từng hàm sóng thành phần:

$$
-\frac{\hbar^2}{2m} \frac{\partial^2 \Psi_1}{\partial x^2} = \hbar\omega_1 \Psi_1
$$

$$
-\frac{\hbar^2}{2m} \frac{\partial^2 \Psi_2}{\partial x^2} = \hbar\omega_2 \Psi_2
$$

Do tính tuyến tính, vế trái đối với hàm sóng chồng chập $\Psi = \Psi_1 + \Psi_2$ bằng tổng hai kết quả: $\hbar\omega_1 \Psi_1 + \hbar\omega_2 \Psi_2$. Bây giờ tính vế phải của phương trình Schrödinger (40.15):

$$
i\hbar \frac{\partial \Psi}{\partial t} = \hbar\omega_1 \Psi_1 + \hbar\omega_2 \Psi_2
$$

Vì cả hai sóng thành phần đều thỏa mãn hệ thức tán sắc (40.8), tức $\hbar\omega_1 = \hbar^2 k_1^2 / (2m)$ và $\hbar\omega_2 = \hbar^2 k_2^2 / (2m)$, vế trái và vế phải hoàn toàn bằng nhau. Do đó, hàm sóng chồng chập thỏa mãn phương trình Schrödinger cho hạt tự do.

(b) Hàm mật độ xác suất $|\Psi(x, t)|^2$ là tích của $\Psi$ với liên hợp phức của nó:

$$
|\Psi|^2 = 2|A|^2 + 2\operatorname{Re}(\Psi_1^* \Psi_2)
$$

Đặt $\Delta k=k_2-k_1$ và $\Delta\omega=\omega_2-\omega_1$. Hiệu pha là

$$
\Delta\phi=\Delta k\,x-\Delta\omega\,t.
$$

Phần thực của số hạng giao thoa là

$$
\operatorname{Re}(\Psi_1^* \Psi_2) = |A|^2 \cos(\Delta\phi)
$$

Cộng các số hạng lại:

$$
\begin{aligned}
|\Psi|^2 &= 2|A|^2 [1 + \cos(\Delta\phi)] \\
&= 4|A|^2 \cos^2(\Delta\phi / 2)
\end{aligned}
$$

**Đánh giá**: Tại thời điểm $t=0$, hiệu pha bằng $\Delta k\,x$. Mật độ xác suất có dạng

$$
\rho(x,0)=4|A|^2\cos^2\frac{\Delta k\,x}{2}.
$$

Ở đây $\rho=|\Psi|^2$ là mật độ xác suất. Như hình 40.5, mật độ biến thiên tuần hoàn giữa $0$ và $4|A|^2$, không bao giờ âm. Khoảng cách giữa hai cực đại liên tiếp là $2\pi/|\Delta k|$. Các khoảng nhỏ quanh cực đại có xác suất tương đối lớn hơn các khoảng cùng rộng quanh nút giao thoa.

Cần lưu ý thêm rằng đây không phải trạng thái dừng. Các dải giao thoa chuyển động dọc theo chiều dương trục $x$. Tương tự một sóng hình sin có tốc độ pha $\omega/k$, số hạng giao thoa $\cos(\Delta k\,x-\Delta\omega\,t)$ cho tốc độ dịch chuyển của các dải là

$$
v_{\mathrm{av}} = \frac{\omega_2 - \omega_1}{k_2 - k_1}
$$

Chỉ số dưới "av" biểu thị đây là tốc độ trung bình của hạt. Cái giá phải trả cho việc bước đầu định xứ hạt trong không gian là hạt không còn sở hữu một động lượng xác định hay năng lượng xác định duy nhất. Điều này hoàn toàn phù hợp với nguyên lý bất định Heisenberg: Khi ta thu hẹp độ bất định về vị trí của hạt, độ bất định về động lượng và năng lượng của hạt bắt buộc phải tăng lên.

Động lượng trung bình của hạt là $p_{\mathrm{av}} = (\hbar k_2 + \hbar k_1)/2$, là trung bình cộng động lượng của hai sóng thành phần. Giá trị này tương ứng với tốc độ trung bình của hạt:

$$
v_{\mathrm{av}} = \frac{p_{\mathrm{av}}}{m} = \frac{\hbar(k_2 + k_1)}{2m}
$$

Ta kiểm tra tính nhất quán trực tiếp với biểu thức tốc độ sóng ở trên:

$$
\begin{aligned}
v_{\mathrm{av}} &= \frac{\omega_2 - \omega_1}{k_2 - k_1} \\
&= \frac{\hbar(k_2^2 - k_1^2)}{2m(k_2 - k_1)} \\
&= \frac{\hbar(k_2 + k_1)}{2m}
\end{aligned}
$$

Hai cách tính dẫn đến cùng một kết quả chính xác. Mô hình hai sóng này là một sự lý tưởng hóa không chuẩn hóa được trên toàn trục số thực. Tuy nhiên, nó minh họa sáng tỏ cơ chế giao thoa chuyển động trước khi ta mở rộng sang gói sóng định xứ hoàn chỉnh có thể chuẩn hóa.
:::

::: tip Khái niệm cốt lõi: Chồng chập định xứ hạt tự do
Một hạt tự do chuyển động dọc theo trục $x$ được mô tả bằng hàm sóng $\Psi(x, t)$ thỏa mãn phương trình Schrödinger cho hạt tự do (40.15). Một hàm sóng có động lượng và năng lượng xác định thì hoàn toàn không định xứ trong không gian. Để xây dựng một hàm sóng định xứ trong không gian, ta bắt buộc phải chồng chập các hàm sóng có các giá trị động lượng và năng lượng khác nhau.
:::

![Hình 40.5: Mật độ xác suất tại thời điểm ban đầu của hai sóng phẳng cùng biên độ truyền theo chiều dương. Các dải giao thoa lặp lại, với cực tiểu bằng không và cực đại bằng bốn lần bình phương độ lớn biên độ thành phần.](../img/young-40/hinh-40-05.png)

### Gói sóng và nguyên lý bất định

Hàm sóng trong Ví dụ 40.1 vẫn chưa định xứ thực sự trong không gian vì phân bố xác suất tiếp tục trải dài tuần hoàn từ $-\infty$ đến $+\infty$. Để tạo ra một hàm sóng định vị chặt chẽ hơn, ta tưởng tượng việc chồng chập thêm nhiều sóng hình sin với các số sóng và biên độ thích hợp sao cho chúng giao thoa tăng cường tại một miền không gian hẹp và triệt tiêu lẫn nhau ở mọi nơi khác (Hình 40.6). Khi đó, hàm sóng thu được có dạng một xung sóng cục bộ duy nhất, được gọi là **gói sóng** (wave packet).

![Hình 40.6: Gói sóng tập trung trong vùng rộng Δx, với bước sóng trung bình bằng 2π chia số sóng trung bình. Phần (a) biểu diễn phần thực, phần (b) biểu diễn phần ảo và phần (c) biểu diễn mật độ xác suất tại cùng thời điểm.](../img/young-40/hinh-40-06.png)

Một gói sóng chuyển động một chiều được biểu diễn toán học bằng tích phân chồng chập liên tục vô số sóng thành phần (với $\phi = kx - \omega t$):

$$
\Psi(x, t) = \int_{-\infty}^{\infty} A(k) e^{i\phi}\,dk \tag{40.19}
$$

Trong đó mỗi sóng thành phần có số sóng $k$, tần số góc $\omega = \hbar k^2 / (2m)$, và biên độ $A(k)$ phụ thuộc vào $k$.

Giữa hàm sóng không gian $\Psi(x, t)$ và phổ biên độ $A(k)$ có mối quan hệ tương hỗ sâu sắc thông qua phép biến đổi Fourier (Hình 40.7):

- Nếu phổ $A(k)$ có đỉnh rất hẹp quanh giá trị trung tâm $k_0$ (Hình 40.7a), dải số sóng tham gia chồng chập $\Delta k$ rất nhỏ. Hệ quả là xung sóng $\Psi(x, 0)$ trải rộng trên một miền không gian lớn $\Delta x$ (Hình 40.7b).
- Ngược lại, nếu ta dùng một dải số sóng rộng hơn để $A(k)$ trải rộng (Hình 40.7c), gói sóng $\Psi(x, 0)$ giao thoa triệt tiêu nhanh hơn và định vị trong một miền không gian hẹp hơn rất nhiều (Hình 40.7d).

![Hình 40.7: Phổ biên độ A(k) hẹp trong phần (a) tạo gói sóng trải rộng ở phần (b). Phổ rộng hơn trong phần (c) tạo gói hẹp hơn ở phần (d). Hai cách ghép phổ với hàm sóng minh họa quan hệ giữa độ phân tán số sóng và độ định xứ.](../img/young-40/hinh-40-07.png)

Mối liên hệ này phản ánh bản chất toán học của nguyên lý bất định Heisenberg: Một dải số sóng hẹp $\Delta k$ kéo theo độ bất định động lượng nhỏ $\Delta p_x = \hbar \Delta k$, dẫn đến độ bất định vị trí lớn $\Delta x$. Ngược lại, để định vị hạt trong vùng $\Delta x$ nhỏ, ta buộc phải chồng chập một dải rộng các số sóng, kéo theo $\Delta p_x$ lớn. Hệ thức bất định $\Delta x \Delta p_x \ge \hbar / 2$ thực chất là một hệ quả toán học trực tiếp của tích phân Fourier dạng (40.19).

::: warning Cảnh báo: Sóng vật chất bị tán sắc theo thời gian
Vì vận tốc pha $v_p = \omega/k = \hbar k / (2m)$ của sóng de Broglie phụ thuộc vào số sóng $k$, các sóng thành phần khác nhau lan truyền với tốc độ khác nhau. Hiện tượng này khiến gói sóng vật chất dần dần bị trải rộng (tán sắc) theo thời gian. Ngược lại, một xung ánh sáng trong chân không lan truyền mà không bị biến dạng vì mọi bước sóng ánh sáng đều truyền đi với cùng tốc độ $c$.
:::

### Thế năng và phương trình Schrödinger một chiều tổng quát

Phương trình cho hạt tự do (40.15) dùng mốc thế năng bằng không. Với lực bảo toàn trong một chiều, $F_x=-dU/dx$. Ta viết gọn $U=U(x)$ và dùng hai ký hiệu đạo hàm riêng:

$$
\begin{aligned}
&\Psi_{xx}=\frac{\partial^2\Psi}{\partial x^2},\\
&\Psi_t=\frac{\partial\Psi}{\partial t}.
\end{aligned}
$$

Phương trình Schrödinger một chiều tổng quát là

$$
-\frac{\hbar^2}{2m} \Psi_{xx} + U\Psi = i\hbar \Psi_t \tag{40.20}
$$

Để hiểu nguồn gốc vật lý của phương trình (40.20), xét trường hợp hạt tự do có hàm sóng hình sin $\Psi(x, t) = A e^{i(kx - \omega t)}$. Các số hạng đạo hàm trong phương trình (40.20) trở thành:

$$
-\frac{\hbar^2}{2m} \frac{\partial^2 \Psi}{\partial x^2} = K \Psi
$$

$$
i\hbar \frac{\partial \Psi}{\partial t} = E \Psi
$$

Với sóng phẳng trong miền thế năng không đổi, các phép đạo hàm cho những hệ số động năng và năng lượng tương ứng. Điều này gợi ra cấu trúc $K+U=E$: Toán tử động năng cộng với toán tử thế năng tạo thành toán tử năng lượng.

Đây là một lập luận xây dựng mô hình, không phải phép suy diễn cơ học lượng tử từ các định luật Newton. Phương trình Schrödinger là định luật cơ sở được kiểm tra bằng những dự đoán thực nghiệm, trong miền áp dụng của mô hình phi tương đối tính.

Với khối lượng không đổi và thế năng hữu hạn, không có tương tác kỳ dị tại biên, hàm sóng cùng đạo hàm bậc nhất phải nối liên tục. Điều kiện này có vai trò quyết định khi tìm nghiệm và mức năng lượng. Vách thế vô hạn cần điều kiện biên riêng, không được xử lý như một bước thế hữu hạn.

### Trạng thái dừng

Trong nhiều bài toán vật lý quan trọng, thế năng $U(x)$ chỉ phụ thuộc vào tọa độ không gian mà không phụ thuộc vào thời gian. Khi đó, hạt có thể tồn tại trong một trạng thái có năng lượng xác định $E$. Một trạng thái có năng lượng xác định được gọi là **trạng thái dừng**.

Hàm sóng của một trạng thái dừng luôn phân tách được thành tích của một hàm chỉ phụ thuộc tọa độ không gian $\psi(x)$ với một thừa số dao động điều hòa theo thời gian:

$$
\Psi(x, t) = \psi(x) e^{-iEt/\hbar} \tag{40.21}
$$

Để thấy rõ nguồn gốc của tên gọi "trạng thái dừng", ta nhân hàm sóng (40.21) với liên hợp phức $\Psi^*(x, t) = \psi^*(x) e^{+iEt/\hbar}$ để tìm hàm mật độ xác suất:

$$
\begin{aligned}
|\Psi(x, t)|^2 &= \Psi^*(x, t)\Psi(x, t) \\
&= \psi^*(x)\psi(x) e^0 \\
&= |\psi(x)|^2
\end{aligned}
$$

Vì $|\psi(x)|^2$ hoàn toàn không phụ thuộc vào thời gian, đẳng thức sau đây chứng minh rằng hàm mật độ xác suất $|\Psi(x, t)|^2$ của một trạng thái có năng lượng xác định là không đổi theo thời gian:

$$
|\Psi(x, t)|^2 = |\psi(x)|^2 \tag{40.22}
$$

Với một đại lượng có toán tử không phụ thuộc tường minh vào thời gian, phân bố kết quả đo trong trạng thái riêng năng lượng cũng không đổi theo thời gian. Điều này nói về phân bố trên những hệ được chuẩn bị giống nhau, không gán một giá trị bất biến cho mọi lần đo riêng lẻ.

::: warning Cảnh báo: Trạng thái dừng không có nghĩa là hạt đứng yên
Một hạt ở trạng thái dừng không có nghĩa là một chất điểm đứng yên. Đại lượng giữ nguyên ở đây là phân bố xác suất vị trí, còn trạng thái có năng lượng toàn phần xác định $E$. Trong thế năng tổng quát, điều này không đòi hỏi động năng hay động lượng xác định, cũng không gán cho hạt một quỹ đạo cổ điển.
:::

Phương trình Schrödinger tổng quát (40.20) trở nên đơn giản hơn rất nhiều đối với các trạng thái dừng. Với $\Psi(x, t) = \psi(x) e^{-iEt/\hbar}$, các đạo hàm riêng tương ứng là:

$$
\frac{\partial^2 \Psi}{\partial x^2} = \frac{d^2 \psi}{dx^2} e^{-iEt/\hbar}
$$

$$
i\hbar \frac{\partial \Psi}{\partial t} = E\psi e^{-iEt/\hbar}
$$

Thay các đạo hàm vào phương trình Schrödinger phụ thuộc thời gian và triệt tiêu thừa số chung $e^{-iEt/\hbar} \neq 0$ ở cả hai vế:

$$
-\frac{\hbar^2}{2m} \frac{d^2 \psi}{dx^2} + U\psi = E\psi \tag{40.23}
$$

Phương trình (40.23) được gọi là **phương trình Schrödinger độc lập thời gian**. Phương trình này không còn chứa biến thời gian $t$, mà chỉ chứa hàm sóng không gian $\psi(x)$ cùng năng lượng $E$ của hệ.

### Ví dụ 40.2: Trạng thái dừng của hạt tự do

Chứng minh rằng hàm sóng không gian $\psi(x) = A_1 e^{ikx} + A_2 e^{-ikx}$ với $U(x) = 0$ là một hàm sóng trạng thái dừng hợp lệ của hạt tự do, và tìm năng lượng tương ứng của hạt.

::: details Lời giải chi tiết
**Nhận diện và thiết lập**: Một hàm sóng không gian $\psi(x)$ mô tả trạng thái dừng hợp lệ của một hạt tự do khi và chỉ khi nó thỏa mãn phương trình Schrödinger độc lập thời gian (40.23) với $U(x) = 0$:

$$
-\frac{\hbar^2}{2m} \frac{d^2 \psi}{dx^2} = E\psi
$$

Để kiểm tra, ta lấy đạo hàm bậc hai của hàm số $\psi(x)$ đã cho theo biến $x$.

**Thực hiện**: Lấy đạo hàm bậc nhất của $\psi(x) = A_1 e^{ikx} + A_2 e^{-ikx}$:

$$
\frac{d\psi}{dx} = ik(A_1 e^{ikx} - A_2 e^{-ikx})
$$

Lấy tiếp đạo hàm bậc hai theo $x$:

$$
\frac{d^2 \psi}{dx^2} = -k^2 \psi(x)
$$

Thay kết quả này vào vế trái của phương trình Schrödinger độc lập thời gian với $U(x) = 0$:

$$
-\frac{\hbar^2}{2m} \frac{d^2 \psi}{dx^2} = \frac{\hbar^2 k^2}{2m} \psi(x)
$$

Kết quả thu được là một hằng số nhân với chính hàm $\psi(x)$. So sánh trực tiếp với vế phải của phương trình (40.23), ta thấy $\psi(x)$ hoàn toàn thỏa mãn phương trình, và hằng số đó chính là năng lượng của hạt:

$$
E = \frac{\hbar^2 k^2}{2m}
$$

**Đánh giá**: Hàm sóng $\psi(x)$ là sự chồng chập của hai sóng: Sóng thứ nhất $A_1 e^{ikx}$ mô tả hạt có độ lớn động lượng $p = \hbar k$ chuyển động theo chiều dương trục $x$, và sóng thứ hai $A_2 e^{-ikx}$ mô tả hạt có cùng độ lớn động lượng chuyển động theo chiều âm trục $x$.

Nếu một trong hai hệ số bằng 0 (chẳng hạn $A_2 = 0$), trạng thái rút về một sóng phẳng đơn sắc duy nhất và hạt sở hữu động lượng xác định $p = +\hbar k$. Tuy nhiên, khi cả $A_1$ và $A_2$ đều khác 0, trạng thái kết hợp $\psi(x)$ là sự chồng chập của hai trạng thái riêng ứng với hai giá trị động lượng đối nhau ($+\hbar k$ và $-\hbar k$), nên trạng thái này không có một động lượng xác định duy nhất. Phép đo động lượng sẽ cho kết quả $+\hbar k$ với xác suất tỷ lệ với $|A_1|^2$ hoặc $-\hbar k$ với xác suất tỷ lệ với $|A_2|^2$.

Nếu hai hệ số có độ lớn bằng nhau ($|A_1| = |A_2|$), mật độ dòng xác suất triệt tiêu và hai sóng giao thoa tạo thành một sóng dừng lượng tử thuần túy. Nếu hai hệ số có độ lớn khác nhau ($|A_1| \ne |A_2|$), mật độ dòng xác suất khác không và động lượng trung bình $\langle p \rangle$ khác 0:

$$
\langle p \rangle = \hbar k\, \frac{|A_1|^2 - |A_2|^2}{|A_1|^2 + |A_2|^2} \neq 0
$$

Như vậy, mặc dù hàm sóng kết hợp $\psi(x)$ biểu diễn một trạng thái dừng có năng lượng xác định $E = \hbar^2 k^2 / (2m)$, trạng thái này nhìn chung không có động lượng xác định. Trong Mục 40.2, ta sẽ thấy dạng hàm sóng này có thể biểu diễn sóng dừng khi hạt bị giam cầm trong một vùng không gian giới hạn.
:::

::: tip Khái niệm cốt lõi: Trạng thái dừng
Một trạng thái cơ học lượng tử có năng lượng xác định $E$ sở hữu hàm sóng toàn phần có dạng $\Psi(x, t) = \psi(x) e^{-iEt/\hbar}$. Trạng thái này được gọi là **trạng thái dừng** vì hàm mật độ xác suất tương ứng $|\Psi(x, t)|^2 = |\psi(x)|^2$ hoàn toàn không phụ thuộc vào thời gian.
:::

### Câu hỏi tự kiểm tra 40.1

Một gói sóng cho bởi tích phân ở phương trình (40.19) có biểu diễn một trạng thái dừng hay không?

::: details Đáp án và lời giải chi tiết
**Đáp án**: Không.

**Lời giải chi tiết**: Phương trình (40.19) biểu diễn sự chồng chập của vô số hàm sóng có số sóng $k$ khác nhau. Cần lưu ý rằng hai số sóng khác nhau không nhất thiết mang năng lượng khác nhau, bởi vì hai sóng có số sóng đối nhau $k$ và $-k$ sở hữu cùng một mức năng lượng tự do $E = \hbar^2 k^2 / (2m)$. Tuy nhiên, một gói sóng định xứ trong không gian bắt buộc phải chứa một dải liên tục các độ lớn $|k|$ khác nhau (tức dải $|\Delta k| > 0$). Do mỗi độ lớn $|k|$ tương ứng với một giá trị năng lượng khác nhau $E(k) = \hbar^2 k^2 / (2m)$, trạng thái mà hàm sóng tổng hợp này biểu diễn không phải là một trạng thái có năng lượng xác định duy nhất. Vì vậy, gói sóng không phải là một trạng thái dừng.

Một cách khác để nhận thấy điều này là quan sát thừa số $e^{-i\omega(k)t}$ nằm trong dấu tích phân (40.19). Những thành phần có độ lớn số sóng khác nhau có tần số góc khác nhau. Ta không thể đưa ra ngoài tích phân một pha thời gian chung cho toàn gói như ở một trạng thái riêng năng lượng.
:::
