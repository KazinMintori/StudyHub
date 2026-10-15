<!-- Chương 25, mục 25.2. Trang in 816–819, PDF một-based 836–839. -->

## 25.2. Điện trở suất

Mật độ dòng điện $\vec J$ trong vật dẫn phụ thuộc vào điện trường $\vec E$ và tính chất của vật liệu. Quan hệ này nhìn chung có thể phức tạp. Với một số vật liệu, đặc biệt là kim loại ở nhiệt độ không đổi, độ lớn mật độ dòng điện gần tỉ lệ thuận với độ lớn điện trường. Tỉ số giữa hai đại lượng gần như không đổi. Mô hình này được gọi là định luật Ohm, theo tên nhà vật lý Đức Georg Simon Ohm (1787–1854), người công bố kết quả năm 1826. Đây là mô hình lý tưởng mô tả khá tốt một số vật liệu, chứ không phải quy luật áp dụng cho mọi vật chất. Trong mục này, ta giả sử mô hình Ohm đúng.

Điện trở suất $\rho$ của vật liệu được định nghĩa bằng tỉ số giữa độ lớn điện trường trong vật liệu và độ lớn mật độ dòng điện do điện trường gây ra:

$$
\rho = \frac EJ. \tag{25.5}
$$

Điện trở suất càng lớn thì cần điện trường càng mạnh để tạo cùng một mật độ dòng điện. Với điện trường đã cho, điện trở suất lớn cũng tạo mật độ dòng nhỏ hơn.

Từ đơn vị của $E$ và $J$:

$$
\begin{aligned}
[\rho] &= \frac{\mathrm{V/m}}{\mathrm{A/m^2}} \\
&= \frac{\mathrm{V\cdot m}}{\mathrm A} \\
&= \Omega\cdot\mathrm m.
\end{aligned}
$$

Ở đây $1\,\Omega=1\,\mathrm{V/A}$, tức một vôn trên một ampe là một ôm. Đơn vị SI của điện trở suất là ôm mét. Vật dẫn hoàn hảo là mô hình có điện trở suất bằng không, còn chất cách điện hoàn hảo có điện trở suất vô hạn. Kim loại và hợp kim thường có điện trở suất nhỏ nhất. Điện trở suất của chất cách điện có thể lớn hơn kim loại khoảng $10^{22}$ lần.

### Bảng 25.1. Điện trở suất ở nhiệt độ phòng

Bảng sau cho một số giá trị điện trở suất đại diện ở $20^\circ\mathrm C$. Các giá trị có thể thay đổi theo độ tinh khiết, thành phần hợp kim và điều kiện đo.

| Nhóm vật liệu | Chất | $\rho\,(\Omega\cdot\mathrm m)$ |
| --- | --- | ---: |
| Kim loại | Bạc | $1{,}47\times10^{-8}$ |
| Kim loại | Đồng | $1{,}72\times10^{-8}$ |
| Kim loại | Vàng | $2{,}44\times10^{-8}$ |
| Kim loại | Nhôm | $2{,}75\times10^{-8}$ |
| Kim loại | Vonfram | $5{,}25\times10^{-8}$ |
| Kim loại | Thép | $20\times10^{-8}$ |
| Kim loại | Chì | $22\times10^{-8}$ |
| Kim loại | Thủy ngân | $95\times10^{-8}$ |
| Hợp kim | Manganin (Cu 84%, Mn 12%, Ni 4%) | $44\times10^{-8}$ |
| Hợp kim | Constantan (Cu 60%, Ni 40%) | $49\times10^{-8}$ |
| Hợp kim | Nichrome | $100\times10^{-8}$ |
| Bán dẫn | Than chì tinh khiết | $3{,}5\times10^{-5}$ |
| Bán dẫn | Germani tinh khiết | $0{,}60$ |
| Bán dẫn | Silic tinh khiết | $2300$ |
| Cách điện | Hổ phách | $5\times10^{14}$ |
| Cách điện | Thủy tinh | $10^{10}$–$10^{14}$ |
| Cách điện | Lucite | $>10^{13}$ |
| Cách điện | Mica | $10^{11}$–$10^{15}$ |
| Cách điện | Thạch anh nóng chảy | $75\times10^{16}$ |
| Cách điện | Lưu huỳnh | $10^{15}$ |
| Cách điện | Teflon | $>10^{13}$ |
| Cách điện | Gỗ | $10^8$–$10^{11}$ |

Độ dẫn điện $\sigma$ là nghịch đảo của điện trở suất:

$$
\begin{aligned}
\sigma &= \frac1\rho, \\
[\sigma] &= (\Omega\cdot\mathrm m)^{-1}=\mathrm{S/m}.
\end{aligned}
$$

Vật liệu dẫn điện tốt có độ dẫn điện lớn. Độ dẫn điện tương tự độ dẫn nhiệt trong phép so sánh truyền nhiệt. Kim loại thường dẫn điện và dẫn nhiệt tốt, còn gốm và nhựa thường dẫn kém cả điện lẫn nhiệt. Trong kim loại, electron tự do vừa tải điện, vừa là cơ chế chính truyền nhiệt. Sự tương đồng này giải thích phần nào vì sao hai tính chất thường đi cùng nhau.

![Hình 25.5: Các đường dẫn bằng đồng in trên bảng mạch cách điện](../img/young-25/hinh-25-05.png)

**Hình 25.5:** Những đường dẫn đồng trên bảng mạch chỉ cách nhau khoảng một milimét. Điện trở suất cao và độ dẫn điện thấp của nền cách điện giúp dòng điện gần như không truyền từ đường mạch này sang đường mạch bên cạnh.

Do độ dẫn điện giữa vật dẫn và chất cách điện chênh lệch rất lớn, ta có thể giới hạn dòng điện đi theo các đường mạch xác định. Độ dẫn nhiệt thay đổi trong phạm vi hẹp hơn nhiều, chỉ cỡ hệ số $10^3$, nên thường không thể giới hạn dòng nhiệt vào đường dẫn hẹp tương tự.

Chất bán dẫn có điện trở suất nằm giữa kim loại và chất cách điện. Chúng quan trọng vì điện trở suất nhạy với nhiệt độ và với một lượng nhỏ tạp chất.

Vật liệu tuân theo định luật Ohm trong phạm vi phù hợp gọi là vật dẫn Ohm hay vật dẫn tuyến tính. Ở nhiệt độ cố định, điện trở suất của vật liệu loại này không phụ thuộc độ lớn điện trường. Nhiều vật liệu lệch đáng kể khỏi mô hình Ohm, được gọi là vật dẫn phi Ohm hay phi tuyến. Khi ấy, mật độ dòng điện phụ thuộc điện trường theo quan hệ phức tạp hơn.

Có thể hình dung mối quan hệ này qua dòng chất lỏng qua một bộ lọc. Trong quá trình làm rượu vang hoặc si-rô cây phong, người ta có thể bơm chất lỏng qua bộ lọc để loại cặn. Nếu lưu lượng tỉ lệ với độ chênh áp suất giữa hai phía bộ lọc, lưu lượng đóng vai trò tương tự mật độ dòng điện $J$, còn chênh áp đóng vai trò tương tự điện trường $E$. Quan hệ tỉ lệ đó tương tự mô hình Ohm.

### Điện trở suất và nhiệt độ

Điện trở suất của kim loại gần như luôn tăng khi nhiệt độ tăng. Các ion trong vật dẫn dao động với biên độ lớn hơn, làm electron chuyển động dễ va chạm hơn. Va chạm cản trở chuyển động trôi của electron và làm giảm dòng điện nếu các điều kiện khác giữ nguyên.

Trong một khoảng nhiệt độ nhỏ, thường đến độ chênh khoảng $100^\circ\mathrm C$, điện trở suất của kim loại có thể được xấp xỉ tuyến tính:

$$
\rho(T) = \rho_0\left[1+\alpha(T-T_0)\right]. \tag{25.6}
$$

Trong đó $\rho_0$ là điện trở suất tại nhiệt độ tham chiếu $T_0$, còn $\alpha$ là hệ số nhiệt điện trở suất. $T_0$ thường được chọn là $0^\circ\mathrm C$ hoặc $20^\circ\mathrm C$, còn $T$ có thể cao hơn hoặc thấp hơn $T_0$. Hiệu nhiệt độ có cùng độ lớn khi tính bằng kelvin hoặc độ Celsius. Hợp kim manganin gần như không đổi điện trở suất theo nhiệt độ.

![Hình 25.6: Sự phụ thuộc của điện trở suất vào nhiệt độ ở kim loại, bán dẫn và siêu dẫn](../img/young-25/hinh-25-06.png)

**Hình 25.6:** Đường biểu diễn (a) kim loại thường, (b) chất bán dẫn và (c) chất siêu dẫn. Đường thẳng gần đúng của kim loại đi qua đúng điểm $(T_0,\rho_0)$.

Than chì là vật liệu phi kim có điện trở suất giảm khi nhiệt độ tăng. Nhiệt độ cao làm thêm electron thoát khỏi liên kết nguyên tử và trở nên linh động, nên hệ số nhiệt điện trở suất của than chì âm. Chất bán dẫn có xu hướng tương tự. Vì điện trở suất của tinh thể bán dẫn nhỏ thay đổi đáng kể theo nhiệt độ, nó có thể dùng làm cảm biến nhiệt điện trở.

Một số hợp kim kim loại và oxit có hiện tượng siêu dẫn. Khi hạ nhiệt độ, điện trở suất ban đầu giảm liên tục như ở kim loại thường. Tại nhiệt độ tới hạn $T_c$, vật liệu chuyển pha và điện trở suất đột ngột bằng không. Khi dòng điện đã được thiết lập trong một vòng siêu dẫn, dòng tiếp tục tồn tại mà không cần điện trường duy trì.

Siêu dẫn được Heike Kamerlingh Onnes phát hiện năm 1911 ở thủy ngân dưới $4{,}2\,\mathrm K$. Trong khoảng 75 năm tiếp theo, nhiệt độ tới hạn cao nhất chỉ vào khoảng $20\,\mathrm K$. Việc làm lạnh khi đó cần heli lỏng đắt tiền hoặc hiđrô lỏng dễ nổ. Năm 1986, Karl Müller và Johannes Bednorz phát hiện một oxit chứa bari, lantan và đồng có nhiệt độ tới hạn gần $40\,\mathrm K$, mở ra cuộc tìm kiếm vật liệu siêu dẫn ở nhiệt độ cao.

Đến năm 1987, người ta tìm được oxit phức hợp yttri, đồng và bari có nhiệt độ tới hạn cao hơn điểm sôi $77\,\mathrm K$ của nitơ lỏng, chất làm lạnh rẻ và an toàn. Tài liệu ghi nhận kỷ lục nhiệt độ tới hạn năm 2018 là $203{,}5\,\mathrm K$ và nêu khả năng chế tạo vật liệu siêu dẫn ở nhiệt độ phòng. Các ứng dụng tiềm năng gồm truyền tải điện, thiết kế máy tính và giao thông. Nam châm điện siêu dẫn làm lạnh bằng heli lỏng được dùng trong máy gia tốc hạt và một số hệ thống tàu đệm từ thử nghiệm. Những tính chất khác của siêu dẫn cần kiến thức từ chương về từ học.

### Ứng dụng sinh học: Điện trở suất và sự dẫn truyền thần kinh

![Ảnh hiển vi mặt cắt sợi thần kinh có bao myelin cách điện quanh sợi trục](../img/young-25/anh-mang-myelin.png)

Ảnh hiển vi điện tử tô màu cho thấy mặt cắt của một sợi thần kinh có đường kính khoảng $1\,\mathrm{\mu m}=10^{-6}\,\mathrm m$. Lớp myelin cách điện bao quanh sợi trục dẫn điện, giúp giới hạn dòng điện thần kinh trong đường dẫn đó.

### Bảng 25.2. Hệ số nhiệt điện trở suất

Các hệ số dưới đây là giá trị gần đúng trong vùng lân cận nhiệt độ phòng. Đơn vị là $^\circ\mathrm C^{-1}$.

| Vật liệu | Hệ số nhiệt α (Nghịch độ C) |
| --- | ---: |
| Nhôm | $0{,}0039$ |
| Chì | $0{,}0043$ |
| Đồng thau | $0{,}0020$ |
| Manganin | $0{,}00000$ |
| Than chì | $-0{,}0005$ |
| Thủy ngân | $0{,}00088$ |
| Constantan | $0{,}000008$ |
| Nichrome | $0{,}0004$ |
| Đồng | $0{,}00393$ |
| Bạc | $0{,}0038$ |
| Sắt | $0{,}0050$ |
| Vonfram | $0{,}0045$ |

::: exercise Kiểm tra hiểu mục 25.2
Giữ điện trường bên trong một mẫu bán dẫn không đổi rồi hạ nhiệt độ của mẫu. Mật độ dòng điện thay đổi thế nào? Chọn một phương án trong danh sách sau:

- (i) Tăng.
- (ii) Giảm.
- (iii) Không đổi.
:::

::: solution Lời giải
**Tóm tắt đề bài:** Điện trường giữ nguyên, còn nhiệt độ bán dẫn giảm.

**Hướng đi:**

- Với chất bán dẫn, điện trở suất tăng khi nhiệt độ giảm.
- Ở cùng điện trường, độ lớn mật độ dòng điện thỏa $J=E/\rho$.
- Vì $E$ không đổi và $\rho$ tăng, $J$ giảm.

Đáp án (ii). Mật độ dòng điện giảm khi nhiệt độ hạ.
:::
