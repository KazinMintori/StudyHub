## 32.2. Sóng điện từ phẳng và vận tốc ánh sáng

Sau khi nhận thức được mối liên hệ bản chất giữa các trường biến thiên và sóng điện từ, ta khảo sát cơ chế truyền sóng định lượng dựa trên hệ phương trình Maxwell. Để quá trình phân tích toán học được sáng sủa và tiếp cận trực diện bản chất vật lý, ta bắt đầu bằng việc giả thuyết một cấu hình sóng đơn giản nhất: Sóng điện từ phẳng.

Trong hệ tọa độ Descartes $xyz$, giả sử sóng lan truyền theo chiều dương của trục $x$ ($+x$) với vận tốc $c$ chưa biết. Tại mỗi điểm trong không gian, ta giả định điện trường $\vec{E}$ chỉ có thành phần dọc theo trục $y$ ($E_y$) và từ trường $\vec{B}$ chỉ có thành phần dọc theo trục $z$ ($B_z$). Cả hai trường đều phụ thuộc vào vị trí $x$ và thời gian $t$. Nhiệm vụ đặt ra là kiểm tra xem cấu hình trường này có thỏa mãn bốn phương trình Maxwell hay không, và từ đó rút ra điều kiện cần thiết đối với vận tốc truyền sóng $c$.

Trước hết xét một mặt sóng bước. Phía sau mặt này, hai trường có độ lớn không đổi là $E$ và $B$. Phía trước, cả hai trường bằng không. Mặt phân cách chuyển động theo $+x$ với tốc độ $c$ sẽ được xác định bằng các phương trình Maxwell.

### Mặt sóng điện từ và tính chất sóng ngang

Trong mô hình bước, mặt sóng là mặt phân cách giữa vùng đã có trường và vùng chưa có trường. Với sóng tuần hoàn, có thể xét các mặt cùng pha. Mặt sóng phẳng vuông góc với phương truyền, tức song song với mặt phẳng tọa độ $yz$ khi sóng truyền theo $x$.

![Hình 32.5: Một mặt sóng điện từ phẳng phân cách giữa vùng đã có trường đồng nhất ở phía sau và vùng chưa có trường ở phía trước. Mặt sóng dịch chuyển sang phải theo chiều +x với tốc độ c.](../img/young-32/hinh-32-05.png)

Để kiểm tra tính nhất quán với phương trình Maxwell thứ nhất và thứ hai, ta xét một mặt kín Gauss hình hộp chữ nhật có các mặt song song với các mặt phẳng tọa độ $xy$, $xz$ và $yz$.

![Hình 32.6: Mặt Gauss hình hộp chữ nhật áp dụng cho sóng điện từ phẳng.](../img/young-32/hinh-32-06.png)

Hình hộp không chứa bất kỳ điện tích tự do nào bên trong ($Q_{\text{encl}} = 0$). Theo định luật Gauss cho điện trường, tổng điện thông qua mặt kín phải triệt tiêu. Đồng thời, theo định luật Gauss cho từ trường, tổng từ thông qua mặt kín cũng luôn bằng không.

Nếu điện trường $\vec{E}$ hoặc từ trường $\vec{B}$ có một thành phần dọc theo trục $x$ (song song với phương truyền sóng), khi mặt sóng đi vào bên trong hình hộp, sẽ xuất hiện thông lượng đi qua mặt bên trái mà không có thông lượng tương ứng đi ra ở mặt bên phải. Điều này sẽ làm cho tổng thông lượng khác không, dẫn tới vi phạm định luật Gauss. Do đó, để thỏa mãn định luật Gauss cho cả điện trường và từ trường, các vector $\vec{E}$ và $\vec{B}$ bắt buộc phải vuông góc với phương truyền sóng. Nói cách khác, **sóng phẳng đang xét phải là sóng ngang**.

### Áp dụng định luật cảm ứng Faraday

Phương trình Maxwell thứ ba là định luật cảm ứng Faraday:

$$
\oint \vec{E} \cdot d\vec{l} = -\frac{d\Phi_B}{dt}. \tag{32.1}
$$

Để kiểm tra định luật này, ta chọn một đường cong kín hình chữ nhật $efgh$ nằm trong mặt phẳng song song với mặt phẳng $xy$ như quan sát ở Hình 32.7a.

![Hình 32.7: Phần (a) áp dụng định luật Faraday cho đường cong chữ nhật song song mặt phẳng xy. (b) Trong khoảng thời gian dt, mặt sóng dịch chuyển một đoạn c dt sang phải, quét qua diện tích ac dt.](../img/young-32/hinh-32-07.png)

Khung chữ nhật có chiều cao $a$ dọc theo trục $y$ và chiều rộng $\Delta x$ dọc theo trục $x$. Xét thời điểm mặt sóng đã đi qua một phần khung chữ nhật: Điện trường $\vec{E}$ trên cạnh $ef$ bằng không vì cạnh này nằm ở vùng sóng chưa tới. Chọn vector pháp tuyến diện tích $d\vec{A}$ hướng theo chiều dương trục $z$ ($+z$), theo quy tắc bàn tay phải, chiều lấy tích phân lưu thông $\oint \vec{E} \cdot d\vec{l}$ là chiều ngược chiều kim đồng hồ quanh khung chữ nhật $efgh$.

- Trên cạnh $ef$: Điện trường bằng không, đóng góp bằng không.
- Trên hai cạnh $fg$ và $he$: Vector $d\vec{l}$ vuông góc với vector $\vec{E}$ (hoặc $\vec{E} = 0$), do đó tích vô hướng $\vec{E} \cdot d\vec{l} = 0$.
- Trên cạnh $gh$: Vector $\vec{E}$ hướng theo chiều $+y$ trong khi vector vi phân dịch chuyển $d\vec{l}$ hướng ngược lại theo chiều $-y$. Do đó tích phân đường cho kết quả:

$$
\oint \vec{E} \cdot d\vec{l} = -Ea. \tag{32.2}
$$

Vế trái của định luật Faraday khác không, kéo theo vế phải cũng phải khác không. Điều này đòi hỏi từ thông qua khung chữ nhật $efgh$ phải biến thiên theo thời gian. Muốn có từ thông gửi qua một khung nằm trong mặt phẳng $xy$, từ trường $\vec{B}$ bắt buộc phải có thành phần vuông góc với mặt phẳng này, tức là có thành phần theo trục $z$.

Trong khoảng thời gian $dt$, mặt sóng chuyển động với vận tốc $c$ sẽ tiến sang phải một quãng đường $c\,dt$, quét thêm một diện tích $a(c\,dt)$ của khung chữ nhật. Lượng từ thông gửi qua khung tăng thêm một lượng $d\Phi_B = B(ac\,dt)$, kéo theo tốc độ biến thiên của từ thông:

$$
\frac{d\Phi_B}{dt} = Bac. \tag{32.3}
$$

Thay các biểu thức (32.2) và (32.3) vào định luật Faraday (32.1), ta thu được $-Ea = -Bac$, suy ra mối liên hệ nền tảng:

$$
E = cB. \tag{32.4}
$$

Phương trình (32.4) khẳng định rằng: Sóng điện từ chỉ thỏa mãn định luật Faraday khi vận tốc truyền sóng $c$ cùng độ lớn của điện trường $E$ và từ trường $B$ liên hệ chặt chẽ với nhau qua hệ thức $E = cB$. Nếu ta giả sử từ trường $\vec{B}$ hướng theo chiều âm trục $z$ ($-z$), vế phải của phương trình sẽ đổi dấu và dẫn tới $E = -cB$, điều này vô nghiệm vì các độ lớn $E$, $B$ và $c$ đều là các số thực dương. Đồng thời, bất kỳ thành phần nào của từ trường dọc theo trục $y$ (song song với $\vec{E}$) đều không tạo ra từ thông qua khung $efgh$ và không tham gia vào cấu trúc sóng truyền đi.

### Áp dụng định luật Ampere mở rộng

Phương trình Maxwell thứ tư là định luật Ampere mở rộng. Khi xét sóng truyền trong chân không không có dòng điện dẫn ($i_{\text{C}} = 0$), định luật có dạng:

$$
\oint \vec{B} \cdot d\vec{l} = \mu_0 \epsilon_0 \frac{d\Phi_E}{dt}. \tag{32.5}
$$

Để kiểm tra định luật Ampere, ta đặt một khung chữ nhật $efgh$ nằm trong mặt phẳng song song với mặt phẳng $xz$ có chiều cao $a$ dọc theo trục $z$ và chiều rộng $\Delta x$ dọc theo trục $x$.

![Hình 32.8: Phần (a) áp dụng định luật Ampere cho đường cong chữ nhật song song mặt phẳng xz. (b) Trong khoảng thời gian dt, điện thông qua khung tăng một lượng dPhi_E = Eac dt.](../img/young-32/hinh-32-08.png)

Chọn vector pháp tuyến diện tích $d\vec{A}$ hướng theo chiều $+y$. Theo quy tắc bàn tay phải, chiều lấy tích phân lưu thông của từ trường là chiều ngược chiều kim đồng hồ quanh khung chữ nhật.

Hoàn toàn tương tự, chỉ có cạnh $gh$ nơi từ trường $\vec{B}$ và vector dịch chuyển $d\vec{l}$ cùng hướng song song với trục $+z$ đóng góp vào tích phân đường:

$$
\oint \vec{B} \cdot d\vec{l} = Ba. \tag{32.6}
$$

Trong khoảng thời gian $dt$, diện tích vùng có điện trường quét qua khung tăng thêm $a(c\,dt)$, do đó điện thông qua khung tăng một lượng $d\Phi_E = E(ac\,dt)$. Tốc độ biến thiên của điện thông là:

$$
\frac{d\Phi_E}{dt} = Eac. \tag{32.7}
$$

Thay các kết quả (32.6) và (32.7) vào định luật Ampere (32.5), ta được $Ba = \mu_0 \epsilon_0 Eac$, rút gọn cho ta:

$$
B = \epsilon_0 \mu_0 c E. \tag{32.8}
$$

### Vận tốc của sóng điện từ trong chân không

Để sóng điện từ tồn tại và thỏa mãn đồng thời cả định luật Faraday lẫn định luật Ampere, cả hai hệ thức (32.4) và (32.8) phải cùng được thỏa mãn. Thay biểu thức $E = cB$ từ (32.4) vào (32.8), ta có:

$$
\begin{aligned}
B &= \epsilon_0 \mu_0 c(cB) \\
&= \epsilon_0\mu_0c^2B.
\end{aligned}
$$

Vì độ lớn từ trường $B$ khác không, phương trình đòi hỏi $\epsilon_0 \mu_0 c^2 = 1$, kéo theo công thức xác định vận tốc ánh sáng trong chân không:

$$
c = \frac{1}{\sqrt{\epsilon_0 \mu_0}}. \tag{32.9}
$$

Thay các giá trị bằng số của hằng số điện và hằng số từ:

$$
\begin{aligned}
\epsilon_0 &= 8{,}854\times10^{-12}\,\mathrm{F/m}, \\
\mu_0 &= 4\pi\times10^{-7}\,\mathrm{H/m} \\
&\approx 1{,}257\times10^{-6}\,\mathrm{H/m}.
\end{aligned}
$$

Vận tốc ánh sáng tính được là:

$$
\begin{aligned}
\epsilon_0\mu_0 &\approx 1{,}113\times10^{-17}\,\mathrm{s^2/m^2}, \\
c &= 1/\sqrt{\epsilon_0\mu_0} \\
&\approx 2{,}998\times10^8\,\mathrm{m/s}.
\end{aligned}
$$

Tốc độ suy từ các hằng số điện và từ phù hợp với tốc độ ánh sáng đo được. Sự phù hợp này củng cố dự đoán rằng ánh sáng là sóng điện từ, được kiểm tra tiếp qua các thí nghiệm truyền và phản xạ sóng.

### Các đặc tính cốt lõi của sóng điện từ

Từ việc phân tích cấu hình sóng phẳng ở trên, ta đúc kết các tính chất của một sóng phẳng chạy trong chân không:

1. **Tính chất sóng ngang**: Cả điện trường $\vec{E}$ và từ trường $\vec{B}$ đều vuông góc với phương truyền sóng, đồng thời vuông góc với nhau. Hướng truyền sóng được xác định bởi hướng của tích có hướng giữa điện trường và từ trường: Chiều của $\vec{E} \times \vec{B}$ trùng với chiều truyền sóng.

![Hình 32.9: Quy tắc bàn tay phải cho sóng điện từ: Ngón cái chỉ theo hướng truyền sóng, quay ngón tay từ vector E sang vector B thì ngón cái chỉ chiều lan truyền.](../img/young-32/hinh-32-09.png)

2. **Tỉ số xác định giữa biên độ**: Tại mọi điểm và mọi thời điểm của một sóng phẳng chạy duy nhất trong chân không, độ lớn của điện trường và từ trường luôn tuân theo hệ thức nghiêm ngặt: $E = cB$.
3. **Vận tốc lan truyền xác định**: Sóng điện từ truyền trong chân không với tốc độ cố định $c \approx 3{,}00 \times 10^8\,\mathrm{m/s}$, không phụ thuộc vào hệ quy chiếu quán tính của người quan sát.
4. **Không cần môi trường vật chất**: Sóng điện từ có thể tự duy trì và lan truyền qua không gian chân không tuyệt đối.
5. **Nguyên lý chồng chất**: Các trường $\vec{E}$ và $\vec{B}$ của sóng điện từ tuân theo nguyên lý chồng chất tuyến tính. Các mặt sóng bước cùng truyền theo $+x$ với tốc độ $c$ có thể được chồng lên nhau để tạo một trường biến thiên theo từng đoạn. Trên mỗi mặt phẳng ngang, các trường vẫn đồng đều. Khi các bước trở nên nhỏ vô hạn, ta thu được trường biến thiên liên tục theo $x$. Với một sóng chạy tuần hoàn như vậy, hai trường đạt cực đại độ lớn và triệt tiêu đồng thời.
6. **Tính phân cực**: Sóng điện từ có tính phân cực. Khi vector điện trường $\vec{E}$ luôn dao động dọc theo một phương xác định trong không gian, sóng được gọi là phân cực thẳng dọc theo phương đó. Một sóng chạy theo $x$ có thể được phân tích thành hai sóng phân cực thẳng theo các phương $y$ và $z$.

### Thiết lập phương trình vi phân sóng điện từ

Phương trình sóng (32.9) có thể được thiết lập một cách tổng quát và chặt chẽ hơn bằng phép tính vi phân. Trong cơ học sóng (mục 15.3), li độ dao động $y(x,t)$ của một sóng cơ lan truyền dọc theo trục $x$ với vận tốc $v$ phải thỏa mãn phương trình vi phân đạo hàm riêng:

$$
\frac{\partial^2 y(x,t)}{\partial x^2} = \frac{1}{v^2} \times \frac{\partial^2 y(x,t)}{\partial t^2}. \tag{32.10}
$$

Để thiết lập phương trình tương ứng cho sóng điện từ, ta xét điện trường $E_y(x,t)$ và từ trường $B_z(x,t)$ biến thiên liên tục theo cả tọa độ $x$ và thời gian $t$.

Áp dụng định luật Faraday cho một khung chữ nhật hẹp có chiều cao $a$ và bề rộng vô cùng bé $\Delta x$ nằm song song với mặt phẳng $xy$ giữa hai tọa độ $x$ và $x + \Delta x$:

![Hình 32.10: Định luật Faraday áp dụng cho khung chữ nhật có chiều rộng vi phân delta x song song mặt phẳng xy.](../img/young-32/hinh-32-10.png)

Tích phân lưu thông của điện trường dọc theo chu vi khung là:

$$
\begin{aligned}
E_{\mathrm L} &= E_y(x,t), \\
E_{\mathrm R} &= E_y(x+\Delta x,t).
\end{aligned}
$$

$$
\oint\vec E\cdot d\vec l &=a(E_{\mathrm R}-E_{\mathrm L}). \tag{32.11}
$$

Các chỉ số L và R biểu thị cạnh trái và cạnh phải của khung. Từ thông qua khung là $\Phi_B \approx B_z(x,t) a \Delta x$. Khi lấy đạo hàm theo thời gian, Faraday cho $a(E_{\mathrm R}-E_{\mathrm L})=-a\Delta x\,\partial B_z/\partial t$. Chia cho $a\Delta x$, ta có:

$$
\frac{E_{\mathrm R}-E_{\mathrm L}}{\Delta x}
=-\frac{\partial B_z}{\partial t}.
$$

Cho $\Delta x\to0$, thương ở vế trái tiến tới đạo hàm theo $x$, nên ta thu được phương trình đạo hàm riêng liên hệ giữa tốc độ biến thiên không gian của điện trường và tốc độ biến thiên thời gian của từ trường:

$$
\frac{\partial E_y}{\partial x} = -\frac{\partial B_z}{\partial t}. \tag{32.12}
$$

Hoàn toàn tương tự, áp dụng định luật Ampere mở rộng trong chân không cho một khung chữ nhật hẹp song song với mặt phẳng $xz$:

![Hình 32.11: Định luật Ampere áp dụng cho khung chữ nhật có chiều rộng vi phân delta x song song mặt phẳng xz.](../img/young-32/hinh-32-11.png)

Tích phân lưu thông của từ trường dọc theo chu vi khung là:

$$
\begin{aligned}
B_{\mathrm L} &= B_z(x,t), \\
B_{\mathrm R} &= B_z(x+\Delta x,t).
\end{aligned}
$$

$$
\oint\vec B\cdot d\vec l &=-a(B_{\mathrm R}-B_{\mathrm L}). \tag{32.13}
$$

Tốc độ biến thiên điện thông qua khung là $d\Phi_E/dt \approx (\partial E_y/\partial t) a \Delta x$. Ampère–Maxwell cho $-a(B_{\mathrm R}-B_{\mathrm L})=\epsilon_0\mu_0a\Delta x\,\partial E_y/\partial t$. Chia cho $a\Delta x$ và cho $\Delta x\to0$, ta thu được phương trình đạo hàm riêng thứ hai:

$$
-\frac{\partial B_z}{\partial x} &= \epsilon_0 \mu_0 \times \frac{\partial E_y}{\partial t}. \tag{32.14}
$$

Bây giờ ta thực hiện bước kết hợp quyết định: Lấy đạo hàm riêng theo $x$ đối với cả hai vế của phương trình (32.12), và lấy đạo hàm riêng theo $t$ đối với cả hai vế của phương trình (32.14):

$$
\frac{\partial^2 E_y}{\partial x^2} = -\frac{\partial^2 B_z}{\partial x \partial t},
$$

$$
\begin{aligned}
-\frac{\partial^2 B_z}{\partial t \partial x} &= \frac{\partial}{\partial t} \big( -\frac{\partial B_z}{\partial x} \big) \\
&= \frac{\partial}{\partial t} \big( \epsilon_0 \mu_0 \frac{\partial E_y}{\partial t} \big) \\
&= \epsilon_0 \mu_0 \frac{\partial^2 E_y}{\partial t^2}.
\end{aligned}
$$

Trong miền các trường có đạo hàm bậc hai liên tục, thứ tự lấy đạo hàm riêng không làm thay đổi giá trị đạo hàm hỗn hợp ($\partial^2 B_z / \partial x \partial t$ bằng $\partial^2 B_z / \partial t \partial x$), ta khử được từ trường $B_z$ và thu được phương trình vi phân truyền sóng thuần túy của điện trường:

$$
\frac{\partial^2 E_y}{\partial x^2} = \epsilon_0 \mu_0 \times \frac{\partial^2 E_y}{\partial t^2}. \tag{32.15}
$$

Phương trình (32.15) có dạng toán học trùng khớp hoàn toàn với phương trình sóng tổng quát (32.10). Bằng cách so sánh hệ số trước đạo hàm bậc hai theo thời gian, ta tìm được vận tốc truyền sóng:

$$
\begin{aligned}
\frac{1}{v^2} &= \epsilon_0 \mu_0 \\
\implies v &= \frac{1}{\sqrt{\epsilon_0 \mu_0}} = c.
\end{aligned}
$$

Bằng cách hoàn toàn tương tự, nếu lấy đạo hàm riêng (32.12) theo $t$ và lấy đạo hàm riêng (32.14) theo $x$, ta khử được điện trường $E_y$ và chứng minh được rằng từ trường $B_z$ cũng thỏa mãn phương trình vi phân sóng tương đương:

$$
\frac{\partial^2 B_z}{\partial x^2} = \epsilon_0 \mu_0 \times \frac{\partial^2 B_z}{\partial t^2}.
$$

Như vậy, cả hai thành phần trường của sóng điện từ đều tuân theo cùng một phương trình truyền sóng với vận tốc truyền sóng trong chân không đúng bằng tốc độ ánh sáng.

### Câu hỏi tự kiểm tra 32.2

Đối với mỗi sóng điện từ sau đây, hãy xác định chiều của vector từ trường $\vec{B}$:

(a) Sóng lan truyền theo chiều dương trục $z$ ($+z$), và vector điện trường $\vec{E}$ hướng theo chiều dương trục $x$ ($+x$).

(b) Sóng lan truyền theo chiều dương trục $y$ ($+y$), và vector điện trường $\vec{E}$ hướng theo chiều âm trục $z$ ($-z$).

(c) Sóng lan truyền theo chiều âm trục $x$ ($-x$), và vector điện trường $\vec{E}$ hướng theo chiều dương trục $z$ ($+z$).

<details><summary>Xem đáp án và giải thích</summary>

(a) Chiều dương trục $y$ ($+y$).

(b) Chiều âm trục $x$ ($-x$).

(c) Chiều dương trục $y$ ($+y$).

**Giải thích chi tiết**: Hướng truyền sóng của sóng điện từ luôn trùng với hướng của tích có hướng $\vec{E} \times \vec{B}$, hay sử dụng quy tắc bàn tay phải ở Hình 32.9:

- Ở trường hợp (a): Sóng truyền theo hướng $+z$ (vector đơn vị $\hat{k}$), và $\vec{E}$ theo $+x$ ($\hat{i}$). Ta cần tìm hướng của $\vec{B}$ sao cho $\hat{i} \times \vec{e}_B = \hat{k}$. Vì $\hat{i} \times \hat{j} = \hat{k}$, nên từ trường $\vec{B}$ phải hướng theo chiều dương trục $y$ ($+y$).
- Ở trường hợp (b): Sóng truyền theo hướng $+y$ ($\hat{j}$), và $\vec{E}$ theo $-z$ ($-\hat{k}$). Ta cần $(-\hat{k}) \times \vec{e}_B = \hat{j}$. Vì $(-\hat{k}) \times (-\hat{i}) = \hat{j}$, nên từ trường $\vec{B}$ phải hướng theo chiều âm trục $x$ ($-x$).
- Ở trường hợp (c): Sóng truyền theo hướng $-x$ ($-\hat{i}$), và $\vec{E}$ theo $+z$ ($\hat{k}$). Ta cần $\hat{k} \times \vec{e}_B = -\hat{i}$. Vì $\hat{k} \times \hat{j} = -\hat{i}$, nên từ trường $\vec{B}$ phải hướng theo chiều dương trục $y$ ($+y$).

</details>
