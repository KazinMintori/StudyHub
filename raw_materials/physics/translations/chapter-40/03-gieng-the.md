## 40.3. Giếng thế

Giếng thế là một hàm thế năng $U(x)$ sở hữu một điểm cực tiểu cục bộ. Khái niệm này đã xuất hiện trong bài toán chuyển động thế năng và dao động điều hòa của cơ học cổ điển: Một hạt bị bẫy trong giếng thế cổ điển sẽ chuyển động tuần hoàn qua lại quanh vị trí cân bằng. Mô hình hạt trong hộp mà chúng ta đã khảo sát ở Mục 40.2 là dạng đơn giản nhất của một giếng thế, trong đó thế năng bằng 0 trên một đoạn hữu hạn và bằng vô hạn ở mọi vị trí khác. Mô hình này mô tả gần đúng một số hệ lượng tử đơn giản, nhưng trong tự nhiên các bức tường thế luôn có độ cao hữu hạn.

Một mô hình thực tế hơn là **giếng thế vuông hữu hạn** (finite square well), có đáy phẳng và thành giếng thẳng đứng với độ sâu hữu hạn $U_0$. Hàm thế năng của giếng thế vuông một chiều được định nghĩa bởi:

$$
U(x) = \begin{cases}
0, & x \in [0, L] \\
U_0, & x \notin [0, L]
\end{cases}
$$

Một ứng dụng gần đúng là electron dẫn trong một lá kim loại mỏng có bề dày $L$. Electron tương đối tự do bên trong nhưng cần đủ năng lượng để thoát qua hàng rào bề mặt. Độ sâu giếng liên hệ với năng lượng thoát và công thoát, khi đã xác định rõ mức năng lượng ban đầu.

Trong ba chiều, giếng hữu hạn đối xứng cầu cũng mô hình hóa gần đúng lực hút giam giữ proton và neutron trong hạt nhân.

![Hình 40.13: Hàm thế năng của một giếng thế vuông hữu hạn: Thế năng U(x) bằng 0 bên trong giếng (0 ≤ x ≤ L) và nhận giá trị không đổi U₀ bên ngoài giếng.](../img/young-40/hinh-40-13.png)

### Trạng thái liên kết của giếng thế vuông

Trong cơ học cổ điển, hạt bị bẫy cục bộ trong giếng khi và chỉ khi cơ năng toàn phần $E$ nhỏ hơn thế năng thành giếng $U_0$. Trong cơ học lượng tử, trạng thái bị giam giữ này được gọi là **trạng thái liên kết** (bound state). Đối với giếng sâu vô hạn, mọi trạng thái đều là trạng thái liên kết. Đối với giếng thế hữu hạn, nếu năng lượng $E > U_0$, hạt ở trong trạng thái tán xạ không liên kết (unbound scattering state) chịu ảnh hưởng của các bước nhảy thế năng tại thành giếng chứ không phải sóng phẳng chuyển động hoàn toàn tự do không lực.

Để tìm các trạng thái liên kết ($E < U_0$), ta xét phương trình Schrödinger riêng biệt cho hai vùng: Vùng bên trong giếng và vùng bên ngoài giếng.

#### 1. Vùng bên trong giếng thế ($0 \le x \le L$)

Tại đây $U(x) = 0$, phương trình Schrödinger không phụ thuộc thời gian có dạng:

$$
-\frac{\hbar^2}{2m}\frac{d^2\psi(x)}{dx^2} = E\psi(x) \tag{40.37}
$$

Biến đổi tương đương về dạng phương trình dao động điều hòa:

$$
\begin{aligned}
\frac{d^2\psi(x)}{dx^2} &= -\frac{2mE}{\hbar^2}\psi(x) \\
&= -k^2\psi(x)
\end{aligned}
$$

Trong đó: Số sóng bên trong giếng là $k = \sqrt{2mE}/\hbar$. Để thuận tiện cho biến đổi giải tích, ta viết ngắn gọn $\psi \equiv \psi(x)$. Nghiệm tổng quát bên trong giếng là tổ hợp tuyến tính của các hàm lượng giác:

$$
\psi = A\cos kx + B\sin kx \tag{40.38}
$$

Trong đó: Ký hiệu $A$ và $B$ là các hằng số tích phân. Điểm khác biệt mấu chốt so với giếng vô hạn là thế năng bên ngoài không còn là vô hạn, vì vậy hàm sóng $\psi(x)$ bên ngoài giếng không thể bị triệt tiêu đột ngột.

#### 2. Vùng bên ngoài giếng thế ($x < 0$ và $x > L$)

Tại đây thế năng nhận giá trị không đổi $U(x) = U_0$. Phương trình Schrödinger có dạng:

$$
-\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} + U_0\psi = E\psi
$$

Chuyển vế ta thu được:

$$
\frac{d^2\psi}{dx^2} = \frac{2m(U_0 - E)}{\hbar^2}\psi \tag{40.39}
$$

Vì đang xét trạng thái liên kết ($E < U_0$), hiệu số $U_0 - E$ là một số dương. Phương trình vi phân này không có nghiệm tuần hoàn hình sin mà có nghiệm là các hàm mũ thực. Đặt tham số suy giảm $\kappa$ (chữ cái Hy Lạp kappa):

$$
\kappa = \frac{\sqrt{2m(U_0 - E)}}{\hbar} > 0
$$

Nghiệm tổng quát bên ngoài giếng có dạng:

$$
\psi(x) = C e^{\kappa x} + D e^{-\kappa x} \tag{40.40}
$$

Trong đó: Hai hệ số $C$ và $D$ là các hằng số. Ta xét điều kiện vật lý ở vô cực để thỏa mãn điều kiện chuẩn hóa (40.33): Hàm sóng không được phép phân kỳ ra vô hạn khi $x \to \pm\infty$.

- Ở vùng bên trái giếng ($x < 0$): Khi $x \to -\infty$, số hạng $e^{-\kappa x} \to \infty$. Muốn hàm sóng hội tụ, ta bắt buộc phải triệt tiêu hằng số này bằng cách đặt $D = 0$. Khi đó hàm sóng suy giảm mũ về 0 khi tiến sang trái: $\psi(x) = C e^{\kappa x}$.
- Ở vùng bên phải giếng ($x > L$): Khi $x \to +\infty$, số hạng $e^{\kappa x} \to \infty$. Để nghiệm không bị phân kỳ, ta bắt buộc phải đặt $C = 0$. Khi đó hàm sóng suy giảm mũ về 0 khi tiến sang phải: $\psi(x) = D e^{-\kappa x}$.

#### 3. Điều kiện nối hàm tại ranh giới

Các kết quả trên chứng minh rằng hàm sóng của trạng thái liên kết có dạng hình sin bên trong giếng và dạng hàm mũ suy giảm bên ngoài giếng. Để tạo thành một trạng thái vật lý hợp lệ, các nghiệm bên trong và bên ngoài phải thỏa mãn hai điều kiện biên tại hai điểm ranh giới $x = 0$ và $x = L$:

1. Hàm sóng $\psi(x)$ phải liên tục tại ranh giới.
2. Đạo hàm bậc nhất $d\psi(x)/dx$ phải liên tục tại ranh giới.

Nếu hàm sóng $\psi(x)$ hoặc độ dốc $d\psi(x)/dx$ bị gián đoạn nhảy vọt tại một điểm, đạo hàm bậc hai $d^2\psi(x)/dx^2$ sẽ tiến tới vô hạn tại điểm đó. Điều này vi phạm phương trình Schrödinger (40.23), vốn khẳng định $d^2\psi(x)/dx^2$ tỷ lệ thuận với hiệu $(U - E)\psi$. Do hiệu số $U - E$ có giá trị hữu hạn ở mọi nơi trong giếng thế hữu hạn, đạo hàm bậc hai $d^2\psi(x)/dx^2$ bắt buộc phải hữu hạn trên toàn bộ không gian.

![Hình 40.14: Dạng hàm sóng khả dĩ của một hạt trong giếng thế vuông hữu hạn: Hàm mang dạng hình sin bên trong giếng (0 ≤ x ≤ L) và dạng đuôi hàm mũ suy giảm bên ngoài giếng. Cả hàm sóng và đạo hàm bậc nhất đều liên tục tại hai biên.](../img/young-40/hinh-40-14.png)

Việc nối trơn tru cả hàm sóng lẫn đạo hàm tại hai mép biên chỉ có thể thực hiện được đối với một số giá trị năng lượng $E$ rời rạc nhất định. Điều kiện này dẫn đến một phương trình siêu việt xác định các mức năng lượng cho phép của giếng thế hữu hạn.

Đặc điểm nổi bật nhất của hàm sóng giếng thế hữu hạn là sự xuất hiện của các **đuôi hàm mũ** (exponential tails) xâm nhập vào vùng bên ngoài giếng. Đây là các vùng bị cấm tuyệt đối theo cơ học cổ điển vì nếu hạt xuất hiện tại đó, động năng $K = E - U_0$ sẽ mang giá trị âm. Trong cơ học lượng tử, xác suất tìm thấy hạt bên ngoài giếng thế là khác không, một hiện tượng thuần túy lượng tử mở đường cho hiệu ứng xuyên hầm.

---

### Ví dụ 40.5: Bên ngoài giếng thế hữu hạn

1. Hãy chứng minh rằng hàm số $\psi(x) = C e^{\kappa x} + D e^{-\kappa x}$ là nghiệm của phương trình Schrödinger không phụ thuộc thời gian trong các vùng bên ngoài giếng thế ($x < 0$ và $x > L$), nơi $U = U_0$.
2. Hãy chứng minh rằng trong giới hạn $U_0 \to \infty$, hàm sóng bên ngoài giếng tiến dần về 0 ở mọi điểm, thu về đúng kết quả của hạt trong hộp thế sâu vô hạn ở Mục 40.2.

#### Nhận dạng và thiết lập bài toán

Ở câu thứ nhất, ta tính đạo hàm bậc hai của hàm số đã cho rồi thế vào phương trình Schrödinger ngoài giếng (40.39). Ở câu thứ hai, ta xét giới hạn của hệ số tắt dần $\kappa$ khi thế năng thành giếng $U_0$ tiến ra vô cực.

#### Lời giải chi tiết

1. Lấy đạo hàm bậc nhất của hàm sóng ngoài giếng:

$$
\frac{d\psi(x)}{dx} = \kappa C e^{\kappa x} - \kappa D e^{-\kappa x}
$$

Lấy tiếp đạo hàm bậc hai:

$$
\begin{aligned}
\frac{d^2\psi}{dx^2} &= \kappa^2(C e^{\kappa x} + D e^{-\kappa x}) \\
&= \kappa^2\psi
\end{aligned}
$$

Theo định nghĩa của tham số $\kappa$, ta có $\kappa^2 = \frac{2m(U_0 - E)}{\hbar^2}$. Thay hệ thức này vào biểu thức đạo hàm bậc hai:

$$
\frac{d^2\psi}{dx^2} = \frac{2m(U_0 - E)}{\hbar^2}\psi
$$

Biểu thức này đồng nhất hoàn toàn với phương trình Schrödinger (40.39). Do đó hàm số $\psi(x) = C e^{\kappa x} + D e^{-\kappa x}$ chính là nghiệm của phương trình Schrödinger bên ngoài giếng.

2. Khi độ sâu thành giếng $U_0 \to \infty$, tham số suy giảm $\kappa = \sqrt{2m(U_0 - E)}/\hbar$ cũng tiến dần ra vô cực ($\kappa \to \infty$).

- Trong vùng $x < 0$: Hàm sóng vật lý là $\psi(x) = C e^{\kappa x}$. Do tọa độ $x$ mang giá trị âm, tích số $\kappa x \to -\infty$ khi $\kappa \to \infty$, kéo theo $e^{\kappa x} \to 0$. Do đó $\psi(x) \to 0$ với mọi $x < 0$.
- Trong vùng $x>L$, viết lại hệ số theo giá trị tại biên để được $\psi(x)=\psi(L)e^{-\kappa(x-L)}$. Khi giữ một mức liên kết cố định và cho độ sâu tăng, $\kappa$ tăng không giới hạn. Tại một vị trí cố định bên ngoài, thừa số mũ giảm về không và hàm sóng triệt tiêu trong giới hạn.

#### Đánh giá và bài học phương pháp

Giới hạn này nối hai mô hình. Với mức có số thứ tự cố định, tăng độ sâu giếng làm đuôi ngoài ngắn lại. Khi thành giếng tiến tới vô hạn, hàm sóng ngoài triệt tiêu và ta thu lại điều kiện giam giữ của hộp vô hạn.

::: tip Khái niệm cần nhớ
Trong giới hạn thế năng thành giếng tiến ra vô cực ($U_0 \to \infty$), nghiệm của giếng thế hữu hạn chuyển liên tục về nghiệm của giếng thế sâu vô hạn. Đuôi hàm mũ suy giảm co lại thành không và hạt hoàn toàn không thể thoát ra ngoài.
:::

---

### So sánh giếng thế hữu hạn và giếng thế sâu vô hạn

Việc so sánh sâu sắc giữa hai loại giếng thế mang lại nhiều trực giác vật lý quan trọng:

Thứ nhất, hàm sóng của giếng hữu hạn không bị ép bằng không ngay tại hai biên. Những đuôi hàm mũ làm vùng phân bố rộng hơn và bước sóng của phần hình sin trong giếng dài hơn ở mức tương ứng của hộp vô hạn cùng rộng.

Bước sóng dài hơn cho số sóng trong giếng nhỏ hơn. Với mốc thế năng tại đáy bằng không, năng lượng phụ thuộc bình phương số sóng ấy. Vì vậy, mỗi mức liên kết của giếng hữu hạn thấp hơn mức cùng thứ tự của hộp vô hạn:

$$
E_n < E_{n\text{-IDW}}
$$

Thứ hai, giếng có độ sâu hữu hạn $U_0$ chỉ chứa một số lượng hữu hạn các trạng thái liên kết. Ta lấy năng lượng trạng thái cơ bản của giếng sâu vô hạn cùng bề rộng làm đơn vị chuẩn:

$$
\begin{aligned}
E_{1\text{-IDW}} &= \frac{\pi^2\hbar^2}{2mL^2} \\
&= \frac{h^2}{8mL^2}
\end{aligned} \tag{40.41}
$$

Khi độ sâu giếng rất lớn ($U_0 \gg E_{1\text{-IDW}}$), giếng chứa nhiều trạng thái liên kết. Xét trường hợp điển hình khi độ sâu giếng bằng $U_0 = 6E_{1\text{-IDW}}$, hệ tồn tại chính xác ba trạng thái liên kết với năng lượng:

$$
\begin{aligned}
E_1 &= 0{,}625 E_{1\text{-IDW}}, \\
E_2 &= 2{,}43 E_{1\text{-IDW}}, \\
E_3 &= 5{,}09 E_{1\text{-IDW}}
\end{aligned}
$$

Tương đương với các phân số của độ sâu giếng: $E_1 = 0{,}104 U_0$, $E_2 = 0{,}405 U_0$ và $E_3 = 0{,}848 U_0$. Cả ba mức này đều nhỏ hơn $U_0$ và đều thấp hơn các mức tương ứng của giếng vô hạn ($1{,}0 E_{1\text{-IDW}}$, $4{,}0 E_{1\text{-IDW}}$, $9{,}0 E_{1\text{-IDW}}$).

Khi độ sâu giếng giảm xuống nhỏ hơn $E_{1\text{-IDW}}$ ($U_0 < E_{1\text{-IDW}}$), hệ chỉ còn lại duy nhất một trạng thái liên kết. Trong cơ học lượng tử một chiều, một giếng thế vuông đối xứng hút (attractive finite square well) với độ sâu dương $U_0 > 0$ và bề rộng dương $L > 0$ luôn sở hữu ít nhất một trạng thái liên kết dù giếng có nông hay hẹp đến mức nào.

![Hình 40.15: Đồ thị hàm sóng dừng và sơ đồ các mức năng lượng cho ba trạng thái liên kết trong giếng thế hữu hạn có độ sâu U₀ = 6E_{1-IDW}: Phần (a) biểu diễn các hàm sóng. Phần (b) biểu diễn các mức năng lượng liên kết rời rạc và vùng liên tục.](../img/young-40/hinh-40-15.png)

![Hình 40.16: Các hàm mật độ xác suất |ψ(x)|² cho ba trạng thái liên kết trong giếng thế vuông hữu hạn có độ sâu U₀ = 6E_{1-IDW}, minh họa rõ mức độ thâm nhập ra ngoài thành giếng.](../img/young-40/hinh-40-16.png)

::: warning Thận trọng: Mốc tính năng lượng và sự thâm nhập qua thành giếng
Cần chú ý rằng trong hệ quy chiếu năng lượng chuẩn mực, năng lượng của hạt trong giếng thế được tính mốc tương đối từ đáy giếng, nơi ta quy ước $E = 0$ (hoàn toàn tương tự như giếng sâu vô hạn). Nếu độ sâu giếng là $U_0$, một trạng thái liên kết bắt buộc phải có mức năng lượng thỏa mãn $0 < E < U_0$.

Ngoài ra, khoảng cách thâm nhập của đuôi hàm mũ ra bên ngoài thành giếng phụ thuộc trực tiếp vào năng lượng của trạng thái liên kết: Năng lượng $E$ càng cao (càng tiệm cận thành giếng $U_0$), hiệu số $U_0 - E$ càng nhỏ, dẫn đến hệ số suy giảm $\kappa = \sqrt{2m(U_0 - E)}/\hbar$ càng bé. Hệ quả là hàm sóng suy giảm càng chậm và đuôi hàm mũ vươn càng xa ra bên ngoài giếng, khiến xác suất tìm thấy hạt trong vùng cổ điển cấm càng lớn (Hình 40.15 và Hình 40.16).
:::

Đối với các trạng thái có năng lượng $E > U_0$, hạt không còn bị giam giữ mà ở trong các trạng thái tán xạ không liên kết (unbound scattering states) truyền qua phía trên giếng thế. Các trạng thái này tạo thành một phổ năng lượng liên tục. Sóng bị tán xạ và phản xạ một phần tại các bước nhảy thế năng ở hai thành giếng. Bước sóng bên trong giếng ngắn hơn bước sóng bên ngoài do động năng bên trong giếng lớn hơn bên ngoài.

![Hình 40.17: Ảnh chụp kính hiển vi quét đầu dò đường hầm (STM) của chuồng lượng tử: Một cấu trúc gồm 48 nguyên tử sắt được xếp thành một vòng tròn trên bề mặt tinh thể đồng. Mật độ electron bên trong tạo thành hệ vân sóng dừng tròn đồng tâm, tương tự như các hàm sóng trong giếng thế hữu hạn hai chiều.](../img/young-40/hinh-40-17.png)

---

### Ví dụ 40.6: Electron trong giếng thế hữu hạn

Một electron bị giam giữ trong một giếng thế vuông một chiều có bề rộng $L = 0{,}50\text{ nm}$ (khoảng năm lần đường kính nguyên tử thông thường).

1. Hãy tính năng lượng trạng thái cơ bản $E_{1\text{-IDW}}$ nếu giả sử giếng thế có độ sâu vô hạn.
2. Hãy tìm các mức năng lượng cho phép nếu độ sâu thực tế của giếng là $U_0 = 6E_{1\text{-IDW}}$.
3. Hãy xác định bước sóng của photon phát ra khi electron chuyển dời từ mức $n = 2$ xuống mức $n = 1$. Bước sóng này thuộc vùng nào của thang sóng điện từ?
4. Nếu electron đang ở trạng thái cơ bản ($n = 1$) và hấp thụ một photon, năng lượng tối thiểu của photon cần thiết để giải phóng hoàn toàn electron khỏi giếng thế là bao nhiêu? Bước sóng của photon này thuộc vùng nào của quang phổ?

#### Nhận dạng và thiết lập bài toán

Phương trình (40.41) cho năng lượng trạng thái cơ bản $E_{1\text{-IDW}}$ của giếng sâu vô hạn. Sơ đồ Hình 40.15b cung cấp tỷ lệ năng lượng của các mức liên kết khi $U_0 = 6E_{1\text{-IDW}}$. Năng lượng của photon phát xạ hoặc hấp thụ bằng độ chênh lệch năng lượng giữa hai mức liên quan: $\Delta E = |E_f - E_i|$. Bước sóng photon liên hệ với năng lượng qua hệ thức $E = hc/\lambda$.

#### Lời giải chi tiết

1. Áp dụng phương trình (40.41) với khối lượng electron $m = 9{,}109 \times 10^{-31}\text{ kg}$, $\hbar = 1{,}055 \times 10^{-34}\text{ J}\cdot\text{s}$ và bề rộng $L = 0{,}50 \times 10^{-9}\text{ m}$:

$$
\begin{aligned}
E_{1\text{-IDW}} &= \frac{\pi^2\hbar^2}{2mL^2} \\
&= 2{,}41 \times 10^{-19}\text{ J} \\
&= 1{,}5\text{ eV}
\end{aligned}
$$

2. Độ sâu thực tế của giếng thế là:

$$
\begin{aligned}
U_0 &= 6E_{1\text{-IDW}} \\
&= 6(1{,}504\text{ eV}) = 9{,}0\text{ eV}
\end{aligned}
$$

Dựa vào tỷ lệ năng lượng trên Hình 40.15b, ta tính được ba mức năng lượng liên kết:

$$
\begin{aligned}
E_1 &= 0{,}625(1{,}504\text{ eV}) \\
&= 0{,}94\text{ eV}, \\
E_2 &= 2{,}43(1{,}504\text{ eV}) \\
&\approx 3{,}6\text{ eV}, \\
E_3 &= 5{,}09(1{,}504\text{ eV}) \\
&\approx 7{,}6\text{ eV}
\end{aligned}
$$

3. Năng lượng của photon phát ra khi electron chuyển dời từ mức $n = 2$ xuống mức $n = 1$ là:

$$
\begin{aligned}
\Delta E &= E_2 - E_1 \\
&= 3{,}66\text{ eV} - 0{,}94\text{ eV} \\
&= 2{,}72\text{ eV} \approx 2{,}7\text{ eV}
\end{aligned}
$$

Bước sóng photon tương ứng là:

$$
\begin{aligned}
\lambda &= \frac{hc}{\Delta E} \\
&= \frac{1240\text{ eV}\cdot\text{nm}}{2{,}72\text{ eV}} \\
&\approx 460\text{ nm}
\end{aligned}
$$

Bước sóng này nằm trong vùng ánh sáng nhìn thấy (vùng ánh sáng màu lam của quang phổ).

4. Năng lượng tối thiểu cần cung cấp để giải phóng electron từ trạng thái cơ bản $n = 1$ lên vùng liên tục ($E \ge U_0$) chính là năng lượng liên kết của electron:

$$
\begin{aligned}
E_{\text{min}} &= U_0 - E_1 \\
&= 9{,}02\text{ eV} - 0{,}94\text{ eV} \\
&= 8{,}08\text{ eV} \approx 8{,}1\text{ eV}
\end{aligned}
$$

Bước sóng photon tương ứng với năng lượng này là:

$$
\begin{aligned}
\lambda_{\text{max}} &= \frac{hc}{E_{\text{min}}} \\
&= \frac{1240\text{ eV}\cdot\text{nm}}{8{,}08\text{ eV}} \\
&\approx 150\text{ nm}
\end{aligned}
$$

Bước sóng $150\text{ nm}$ nằm trong vùng tử ngoại (UV) của quang phổ điện từ.

#### Đánh giá và thảo luận mở rộng

Ta có thể kiểm tra chéo các giá trị năng lượng bằng cách sử dụng tỷ lệ theo $U_0$: $E_1 = 0{,}104 U_0 = 0{,}94\text{ eV}$, $E_2 = 0{,}405 U_0 = 3{,}65\text{ eV}$, và $E_3 = 0{,}848 U_0 = 7{,}65\text{ eV}$. Ba mức năng lượng này đều thấp hơn đáng kể so với các mức năng lượng của giếng sâu vô hạn cùng bề rộng ($E_{1\text{-IDW}} = 1{,}5\text{ eV}$, $E_{2\text{-IDW}} = 6{,}0\text{ eV}$, và $E_{3\text{-IDW}} = 13{,}5\text{ eV}$).

Một ứng dụng của giếng thế hữu hạn là **chấm lượng tử**, những hạt bán dẫn có kích thước cỡ nanômét, chẳng hạn cadmium selenide, ký hiệu $\mathrm{CdSe}$. Electron trong chấm có thể được mô hình hóa như một hạt trong giếng hữu hạn, với chiều rộng đặc trưng $L$ bằng kích thước chấm.

Chiếu tia tử ngoại làm electron hấp thụ photon và lên những mức năng lượng cao, chẳng hạn mức $n=3$ trong ví dụ. Khi trở về trạng thái cơ bản, electron có thể chuyển thẳng hoặc qua nhiều bước. Chẳng hạn, trong chuỗi $3\to2\to1$, một bước có thể phát photon nhìn thấy như chuyển mức vừa tính.

Khi tăng $L$ trong mô hình với các thông số khác giữ cố định, các mức và khoảng cách mức giảm. Photon chuyển mức có năng lượng thấp hơn và bước sóng dài hơn. Điều này giải thích việc điều chỉnh màu huỳnh quang bằng kích thước chấm.

Chấm lượng tử có thể được đưa vào mô sống để tín hiệu huỳnh quang làm chất đánh dấu trong nghiên cứu sinh học và y học. Những tính chất quang học này cũng gợi ra khả năng phát triển các loại laser và máy tính tốc độ cao.

::: tip Khái niệm cần nhớ
Một giếng thế vuông hữu hạn chỉ chứa một số lượng hữu hạn các trạng thái liên kết. Năng lượng của các trạng thái này được quyết định bởi điều kiện biên liên tục của cả hàm sóng và đạo hàm bậc nhất tại các mép ranh giới của giếng.
:::

---

### Câu hỏi tự kiểm tra 40.3

Giả sử bề rộng của giếng thế vuông hữu hạn trên Hình 40.15 giảm đi một nửa ($L' = L/2$). Giá trị của độ sâu giếng $U_0$ phải thay đổi như thế nào để hệ vẫn tồn tại đúng ba trạng thái liên kết với năng lượng bằng các tỷ lệ phần trăm của $U_0$ như trên Hình 40.15b? Độ sâu $U_0$ phải:

- (i) Tăng lên 4 lần
- (ii) Tăng lên 2 lần
- (iii) Giữ nguyên không đổi
- (iv) Giảm đi một nửa
- (v) Giảm đi 4 lần

::: details Lời giải và giải thích
**Đáp án đúng:** Tăng lên 4 lần, tức phương án (i).

**Giải thích chi tiết**: Các mức năng lượng được phân bố theo đúng các tỷ lệ trên Hình 40.15b khi và chỉ khi độ sâu thành giếng thỏa mãn hệ thức tỷ lệ cố định $U_0 = 6E_{1\text{-IDW}}$, trong đó:

$$
E_{1\text{-IDW}} = \frac{\pi^2\hbar^2}{2mL^2}
$$

Năng lượng trạng thái cơ bản $E_{1\text{-IDW}}$ của giếng sâu vô hạn tỷ lệ nghịch với bình phương bề rộng giếng ($1/L^2$). Khi bề rộng $L$ giảm đi một nửa ($L' = L/2$), mẫu số giảm đi 4 lần khiến năng lượng $E_{1\text{-IDW}}$ tăng lên 4 lần. Để duy trì cùng tỷ lệ hình học và số lượng trạng thái liên kết ($U_0 = 6E_{1\text{-IDW}}$), giá trị của độ sâu giếng $U_0$ bắt buộc phải tăng lên 4 lần. Khi đó, các mức năng lượng $E_1$, $E_2$ và $E_3$ (vốn là các phân số xác định của $U_0$) cũng sẽ đồng thời tăng lên 4 lần.
:::
