## 40.4. Hàng rào thế và sự xuyên hầm

Một toa tàu lượn không đủ cơ năng để lên đỉnh dốc sẽ quay lại. Với hạt vi mô, liệu kết luận ấy còn tuyệt đối đúng khi vùng thế năng cao chỉ là một hàng rào rất mỏng?

### Giới hạn của mô tả cổ điển

**Hàng rào thế** là một miền mà thế năng tăng lên tới cực đại, trái với giếng thế có cực tiểu. Trong hình 40.18, hạt có cơ năng $E_1$ đi từ bên trái chỉ có thể tới vị trí $x=a$, nơi thế năng bằng cơ năng.

![Hình 40.18: Hàng rào thế có dạng một đỉnh. Hạt cổ điển với cơ năng E₁ quay lại tại x = a, còn hạt có cơ năng E₂ lớn hơn đỉnh có thể đi qua.](../img/young-40/hinh-40-18.png)

Nếu hạt có cơ năng $E_1$ đi tiếp vào vùng $U>E_1$, động năng

$$
K=E_1-U
$$

sẽ âm. Điều ấy không thể xảy ra trong cơ học Newton vì $K=mv^2/2$ không âm. Ngược lại, hạt có cơ năng $E_2$ lớn hơn cực đại thế năng có thể vượt đỉnh.

Một hạt lượng tử có cơ năng thấp hơn đỉnh vẫn có thể được phát hiện ở phía bên kia hàng rào. Hiện tượng ấy gọi là **xuyên hầm**. Hạt không đục thủng hàng rào như một vật thể lớn xuyên qua vách, cũng không mất cơ năng vì phải “leo” qua đỉnh thế năng.

### Hàng rào chữ nhật

Xét thế năng bằng $U_0$ trong đoạn từ $0$ đến $L$:

$$
U(x)=U_0,\qquad0\le x\le L.
$$

Bên ngoài đoạn này, $U(x)=0$. Đây có thể là mô hình đơn giản của một electron trước hai miếng kim loại cách nhau bởi khe không khí rộng $L$. Thế năng thấp trong kim loại và cao trong khe.

![Hình 40.19: Hàng rào chữ nhật cao U₀, rộng L. Hạt có cơ năng E nhỏ hơn U₀ bị cấm đi vào hàng rào trong mô tả cổ điển.](../img/young-40/hinh-40-19.png)

Giả sử $0<E<U_0$. Ngoài hàng rào, phương trình Schrödinger có các nghiệm dạng sóng hình sin, hoặc tương đương là tổng các sóng mũ phức truyền theo hai chiều. Bên trong hàng rào, nghiệm có dạng hàm mũ theo tọa độ.

Tại hai biên hữu hạn $x=0$ và $x=L$, cả $\psi$ lẫn đạo hàm $d\psi/dx$ đều phải liên tục. Vì vậy, các phần nghiệm phải nối trơn. Hàm sóng không bằng không trong hàng rào và có thể còn một phần ở phía bên kia.

![Hình 40.20: Hàm sóng biến thiên theo dạng mũ trong hàng rào và dạng hình sin ở bên ngoài. Tính liên tục của hàm và đạo hàm nối các miền, tạo nên biên độ truyền qua khác không.](../img/young-40/hinh-40-20.png)

**Hệ số truyền qua** $T$ là tỉ số dòng xác suất truyền qua so với dòng xác suất tới. Vì thế năng ở hai phía bằng nhau, nó cũng bằng bình phương tỉ số biên độ sóng truyền qua và sóng tới.

Khi $T$ rất nhỏ so với $1$, kết quả gần đúng là

$$
\begin{aligned}
&T\approx Ge^{-2kL},\\
&G=16\frac{E}{U_0}\left(1-\frac{E}{U_0}\right),\\
&k=\frac{\sqrt{2m(U_0-E)}}{\hbar}.
\end{aligned}
\tag{40.42}
$$

Trong mục này, $k$ là hằng số suy giảm trong hàng rào, có đơn vị $\mathrm{m^{-1}}$. Tăng độ rộng $L$ làm xác suất giảm theo hàm mũ. Hiệu $U_0-E$ cũng có ảnh hưởng mạnh: Nó là phần năng lượng mà hạt cổ điển còn thiếu để vượt hàng rào.

Hệ số $G$ riêng lẻ có thể lớn hơn $1$, nhưng $T$ mới là xác suất. Công thức gần đúng chỉ được dùng khi tích đầy đủ cho $T\ll1$, không được ngoại suy đến mọi độ rộng hoặc mọi năng lượng.

<details><summary>Từ việc nối nghiệm đến công thức truyền qua</summary>

Đặt số sóng bên ngoài hàng rào là

$$
k_0=\frac{\sqrt{2mE}}{\hbar}.
$$

Với sóng tới chỉ đi từ bên trái, các phần nghiệm có dạng

$$
\begin{aligned}
&\psi_{\rm I}=Ae^{ik_0x}+Be^{-ik_0x},\\
&\psi_{\rm II}=Ce^{kx}+De^{-kx},\\
&\psi_{\rm III}=Fe^{ik_0x}.
\end{aligned}
$$

$A$ là biên độ tới, $B$ là biên độ phản xạ và $F$ là biên độ truyền qua. Bốn điều kiện liên tục tại hai biên xác định các tỉ số biên độ. Để viết kết quả gọn mà không làm dài một dòng công thức, đặt

$$
a=\frac{U_0^2}{4E(U_0-E)}.
$$

Kết quả chính xác cho hàng rào chữ nhật tĩnh là

$$
T=\frac{1}{1+a\sinh^2(kL)}.
$$

Nếu $kL$ đủ lớn thì $\sinh(kL)\approx e^{kL}/2$. Khi số hạng chứa hàm mũ lớn hơn nhiều so với $1$,

$$
\begin{aligned}
T&\approx\frac{4}{a}e^{-2kL}\\
&=16\frac{E(U_0-E)}{U_0^2}e^{-2kL}.
\end{aligned}
$$

Đó là công thức (40.42). Việc nối nghiệm giữ cả phần mũ tăng lẫn phần mũ giảm trong vùng hữu hạn, không tự ý loại một phần chỉ vì nó tăng theo $x$.

</details>

### Ví dụ 40.7: Electron xuyên qua hàng rào

Một electron có cơ năng $2{,}0\,\mathrm{eV}$ gặp hàng rào cao $5{,}0\,\mathrm{eV}$. Tìm xác suất xuyên hầm nếu độ rộng hàng rào là (a) $1{,}00\,\mathrm{nm}$ và (b) $0{,}50\,\mathrm{nm}$.

**Nhận dạng:** Cơ năng nhỏ hơn độ cao hàng rào. Ta dùng công thức xuyên hầm chữ nhật, sau đó kiểm tra điều kiện xác suất nhỏ.

**Chuẩn bị:** Khối lượng electron là $9{,}11\times10^{-31}\,\mathrm{kg}$. Hiệu thế năng và cơ năng bằng

$$
\begin{aligned}
U_0-E&=3{,}0\,\mathrm{eV}\\
&\approx4{,}8\times10^{-19}\,\mathrm J.
\end{aligned}
$$

**Thực hiện:** Các hệ số làm tròn tới hai chữ số có nghĩa là

$$
\begin{aligned}
G&=16\frac{2{,}0}{5{,}0}
\left(1-\frac{2{,}0}{5{,}0}\right)\\
&\approx3{,}8.
\end{aligned}
$$

$$
k\approx8{,}9\times10^9\,\mathrm{m^{-1}}.
$$

(a) Với $L=1{,}00\,\mathrm{nm}$, số mũ $2kL\approx17{,}8$. Thay những hệ số đã làm tròn:

$$
\begin{aligned}
T&\approx3{,}8e^{-17{,}8}\\
&\approx7{,}1\times10^{-8}.
\end{aligned}
$$

(b) Khi $L=0{,}50\,\mathrm{nm}$, số mũ giảm còn $8{,}9$. Do đó,

$$
\begin{aligned}
T&\approx3{,}8e^{-8{,}9}\\
&\approx5{,}2\times10^{-4}.
\end{aligned}
$$

**Đánh giá:** Với các giá trị trên, giảm một nửa độ rộng làm xác suất tăng khoảng $7{,}3\times10^3$ lần, tức gần bốn bậc độ lớn. Cả hai xác suất đều nhỏ hơn nhiều so với $1$, phù hợp với điều kiện của công thức.

Vì $k$ nằm trong số mũ, làm tròn sớm có ảnh hưởng thấy được. Giữ thêm chữ số ở các bước trung gian cho $G=3{,}84$ và $k\approx8{,}874\times10^9\,\mathrm{m^{-1}}$, với các xác suất tương ứng khoảng $7{,}5\times10^{-8}$ và $5{,}4\times10^{-4}$. Cả hai cách tính đều cho thấy giảm một nửa độ rộng làm xác suất tăng hàng nghìn lần.

### Từ tiếp điểm điện đến kính hiển vi quét

Khi xoắn hai dây đồng hoặc đóng tiếp điểm công tắc, một màng oxide đồng cách điện mỏng có thể ngăn giữa hai bề mặt kim loại. Electron vẫn truyền qua màng bằng xuyên hầm. Vì vậy, sự có mặt của một lớp cách điện cực mỏng không tự động làm dòng điện bằng không.

Trong diode xuyên hầm, electron đi qua hàng rào thế của cấu trúc bán dẫn. Thay đổi hàng rào cho phép điều khiển dòng điện rất nhanh, với thời gian chuyển mạch cỡ vài picosecond.

**Tiếp giáp Josephson** gồm hai chất siêu dẫn ngăn bởi một màng oxide chỉ dày khoảng $1$–$2\,\mathrm{nm}$. Các cặp electron có thể xuyên qua màng, tạo ra những đặc tính mạch điện đặc biệt. Tiếp giáp này được dùng trong chuẩn điện áp, phép đo từ trường rất nhỏ và công nghệ tính toán lượng tử.

**Kính hiển vi quét xuyên hầm**, viết tắt STM, tạo ảnh bề mặt ở quy mô nguyên tử. Một đầu dò dẫn điện rất nhọn được đưa đến cách bề mặt khoảng $1\,\mathrm{nm}$. Khi đầu dò có điện thế dương so với mẫu, electron có thể xuyên qua hàng rào thế ở bề mặt và đi tới đầu dò.

![Hình 40.21: Đầu dò STM ở phần (a) quét theo hai phương ngang, đồng thời dịch chuyển theo phương đứng để giữ dòng xuyên hầm không đổi. Phần (b) là ảnh các dây lượng tử bằng silicide đất hiếm trên silicon, mỗi dây chỉ rộng khoảng mười nguyên tử.](../img/young-40/hinh-40-21.png)

Dòng xuyên hầm phụ thuộc rất nhạy vào khoảng cách giữa mẫu và mũi dò. Trong một chế độ đo, thiết bị quét theo hai phương ngang và điều chỉnh độ cao để giữ dòng không đổi. Ghi lại độ cao qua nhiều đường quét song song sẽ tái tạo địa hình bề mặt.

Muốn phân biệt các nguyên tử, vị trí đầu dò phải được điều khiển rất chính xác và cách ly rung động từ bên ngoài. Những dây lượng tử như trong hình 40.21 gợi ra khả năng thu nhỏ hơn nữa các mạch điện.

### Xuyên hầm trong sự sống và trong hạt nhân

Protein đóng vai trò enzyme trong cơ thể thường là những phân tử lớn. Hoạt động của nhiều enzyme phụ thuộc vào khả năng electron xuyên qua khoảng trống giữa các phần của phân tử. Sự sống như ta biết phụ thuộc vào những quá trình truyền electron này.

![Ứng dụng sinh học: Cấu trúc một phân tử enzyme. Sự xuyên hầm của electron giữa các vùng của những phân tử như vậy góp phần thực hiện các chức năng sinh học.](../img/young-40/ung-dung-enzyme.png)

Trong phản ứng nhiệt hạch, hai hạt nhân tích điện dương phải tiến đủ gần để lực hạt nhân hút chúng mạnh. Lực đẩy điện tạo ra hàng rào chống lại sự tiến gần ấy. Xuyên hầm cho phép phản ứng xảy ra ngay cả khi cơ năng tương đối chưa đủ để vượt hàng rào theo cơ học cổ điển.

Các phản ứng này diễn ra trong lõi các sao, kể cả Mặt Trời. Khả năng xuyên qua hàng rào Coulomb là một phần thiết yếu trong việc giải thích nguồn năng lượng của sao.

Một hạt alpha gồm hai proton và hai neutron. Những cụm như vậy có thể hình thành trong một hạt nhân lớn, chẳng hạn hạt nhân radium. Khi thoát ra ngoài, chúng gặp hàng rào thế do tác dụng kết hợp của lực hạt nhân hút và lực đẩy điện.

![Hình 40.22: Thế năng gần đúng của hạt alpha đối với hạt nhân bán kính R. Bên trong, lực hạt nhân tạo giếng hút. Bên ngoài, lực đẩy điện tạo hàng rào mà hạt alpha phải xuyên qua để thoát ra.](../img/young-40/hinh-40-22.png)

Xác suất thoát phụ thuộc vào chiều cao và độ rộng của hàng rào. Vì vậy, những hạt nhân phát alpha khác nhau có thể có mức hoạt độ rất khác nhau. Các hạt alpha từng được Rutherford dùng để khảo sát cấu trúc nguyên tử cũng thoát khỏi hạt nhân nguồn nhờ cơ chế này.

### Câu hỏi tự kiểm tra 40.4

Có thể tìm thấy một hạt đang xuyên hầm ngay bên trong hàng rào, thay vì chỉ ở một trong hai phía của hàng rào, hay không?

<details><summary>Xem đáp án và giải thích</summary>

Có. Hàm sóng $\psi(x)$ không bằng không trong đoạn $0\le x\le L$, nên mật độ xác suất $|\psi(x)|^2$ cũng không bằng không tại những điểm thích hợp trong đoạn ấy. Miền bị cấm trong cơ học cổ điển không phải là miền có xác suất lượng tử bằng không.

</details>
