## 1.5. Độ bất định và chữ số có nghĩa

Phép đo luôn có độ bất định. Nếu đo độ dày bìa một cuốn sách đóng bìa cứng bằng thước thông thường, kết quả chỉ đáng tin đến milimét gần nhất, chẳng hạn $3\,\mathrm{mm}$. Viết $3.00\,\mathrm{mm}$ là không đúng với khả năng của dụng cụ, vì thước ấy không cho biết độ dày thực là $3.00\,\mathrm{mm}$, $2.85\,\mathrm{mm}$ hay $3.11\,\mathrm{mm}$. Nếu dùng panme đo được đến $0.01\,\mathrm{mm}$, ta có thể thu được $2.91\,\mathrm{mm}$.

Hai phép đo khác nhau ở **độ bất định**: Phép đo bằng panme có độ bất định nhỏ hơn. Trong thực hành đo lường, độ bất định còn thường được gọi là sai số vì cho biết độ chênh lớn nhất có khả năng xảy ra giữa giá trị đo và giá trị thực. Độ bất định hay sai số của giá trị đo phụ thuộc trực tiếp vào phương pháp và dụng cụ đo.

Ta thường thể hiện mức gần với giá trị thực bằng cách viết giá trị đo, dấu $\pm$ và một số chỉ độ bất định. Nếu đường kính thanh thép là $56.47\pm0.02\,\mathrm{mm}$, giá trị thực có khả năng nằm trong khoảng $56.45\,\mathrm{mm}$ đến $56.49\,\mathrm{mm}$.

Một cách viết rút gọn thường dùng trong khoa học là $1.6454(21)$, nghĩa là $1.6454\pm0.0021$. Các chữ số trong ngoặc biểu thị độ bất định ở những hàng cuối của số chính.

Ta cũng có thể diễn tả độ chính xác bằng **sai số tương đối** hoặc **sai số phần trăm**, còn gọi là độ bất định tương đối và độ bất định phần trăm. Điện trở ghi “$47\,\Omega \pm10\%$” có giá trị thực chênh lệch không quá $10\%$ của $47\,\Omega$, tức khoảng $5\,\Omega$. Do đó giá trị điện trở thực nằm trong khoảng từ $42\,\Omega$ đến $52\,\Omega$.

Với đường kính thanh thép ở trên, sai số tương đối là:

$$
\frac{0.02\,\mathrm{mm}}{56.47\,\mathrm{mm}} \approx 0.0004.
$$

Sai số phần trăm tương ứng xấp xỉ $0.0004\times100\% = 0.04\%$. Một sai số phần trăm nhỏ vẫn có thể gây ra hậu quả đáng kể, như minh họa ở Hình 1.7.

### Hình 1.7: Sai số phần trăm nhỏ vẫn có thể gây hậu quả lớn

![Hình 1.7: Một đầu tàu lao qua phần tường phía trước nhà ga. Tai nạn đường sắt do sai số phần trăm rất nhỏ](/vat-ly-1/bai-giang/img/young-01/hinh-1-7.png)

Sự cố trong hình là kết quả của một sai số phần trăm rất nhỏ: Chạy quá vài mét ở cuối một hành trình dài hàng trăm nghìn mét.

### Chữ số có nghĩa

Trong nhiều trường hợp, độ bất định không được ghi rõ tường minh mà được thể hiện qua số chữ số có ý nghĩa trong giá trị đo, gọi là **chữ số có nghĩa**. Độ dày bìa $2.91\,\mathrm{mm}$ có ba chữ số có nghĩa. Điều đó biểu thị hai chữ số đầu đã biết chắc chắn đúng, còn chữ số cuối có độ bất định. Chữ số cuối ở hàng phần trăm milimét, nên độ bất định vào khoảng $0.01\,\mathrm{mm}$.

Hai giá trị cùng số chữ số có nghĩa có thể có độ bất định khác nhau:
- Khoảng cách $137\,\mathrm{km}$ có ba chữ số có nghĩa, độ bất định vào khoảng $1\,\mathrm{km}$.
- Khoảng cách $0.25\,\mathrm{km}$ có hai chữ số có nghĩa, vì số không đứng trước dấu thập phân không được tính.
- Khoảng cách $0.250\,\mathrm{km}$ có ba chữ số có nghĩa, vì số không tận cùng sau dấu thập phân được tính là chữ số có nghĩa.

Khi dùng các giá trị có độ bất định để tính đại lượng khác, kết quả tính cũng mang độ bất định:

1. **Trong phép nhân hoặc chia**: Số chữ số có nghĩa của kết quả không được nhiều hơn số chữ số có nghĩa của thừa số kém chính xác nhất:

$$
3.1416\times2.34\times0.58 \approx 4.3.
$$

2. **Trong phép cộng hoặc trừ**: Vị trí hàng thập phân quyết định độ chính xác, không phải số chữ số có nghĩa:

$$
123.62 + 8.9 \approx 132.5.
$$

Số $123.62$ có độ bất định khoảng $0.01$, còn $8.9$ có độ bất định khoảng $0.1$. Vì vậy tổng có độ bất định khoảng $0.1$ và phải làm tròn thành $132.5$, thay vì viết $132.52$.

### Bảng 1.2: Sử dụng chữ số có nghĩa

#### Nhân hoặc chia

Kết quả không có nhiều chữ số có nghĩa hơn dữ kiện đo có ít chữ số có nghĩa nhất. Ví dụ:

$$
\frac{0.745\times2.2}{3.885}\approx0.42.
$$

Số $2.2$ có hai chữ số có nghĩa, nên kết quả giữ hai chữ số có nghĩa.

Quy tắc không thay đổi khi sử dụng lũy thừa của $10$. Với hai thừa số $a$ và $b$ được xác định ngay dưới đây:

$$
ab\approx5.45\times10^4.
$$

Kết quả giữ ba chữ số có nghĩa.

#### Cộng hoặc trừ

Hàng cuối của kết quả do số hạng có độ bất định lớn nhất quyết định. Trong phép tính $27.153+138.2-11.74$, số $138.2$ chỉ xác định đến hàng phần mười. Vì thế kết quả phải làm tròn thành $153.6$.

Trong ví dụ nhân có lũy thừa của $10$, hai thừa số được giữ đầy đủ chữ số:

$$
\begin{aligned}
a &= 1.32578\times10^7, \\
b &= 4.11\times10^{-3}.
\end{aligned}
$$

Tích chưa làm tròn là $ab=54489.558$. Vì $b$ có ba chữ số có nghĩa, ta ghi kết quả là $5.45\times10^4$.

Để áp dụng, giả sử bạn muốn kiểm tra giá trị $\pi$, tức tỷ số giữa chu vi và đường kính hình tròn. Giá trị đúng viết đến mười chữ số là $3.141592654$. Bạn vẽ một hình tròn lớn rồi đo chu vi và đường kính đến milimét gần nhất, được $424\,\mathrm{mm}$ và $135\,\mathrm{mm}$, như Hình 1.8. Phép chia cho:

$$
\frac{424\,\mathrm{mm}}{135\,\mathrm{mm}} \approx 3.140740741.
$$

Thoạt nhìn, kết quả dường như không trùng khớp hoàn toàn với số $\pi$. Tuy nhiên, mỗi số đo chỉ có ba chữ số có nghĩa, nên giá trị $\pi$ thực nghiệm cũng chỉ được ghi với ba chữ số: $3.14$. Trong giới hạn độ chính xác ấy, phép đo hoàn toàn phù hợp với giá trị lý thuyết.

### Hình 1.8: Xác định giá trị pi bằng chu vi và đường kính

![Hình 1.8: Đo chu vi 424 milimét và đường kính 135 milimét của hình tròn. Xác định giá trị số pi từ chu vi và đường kính](/vat-ly-1/bai-giang/img/young-01/hinh-1-8.png)

Các số đo chỉ có ba chữ số có nghĩa. Vì vậy tỷ số tính từ chúng, tức giá trị $\pi$ thu được bằng phép đo này, cũng chỉ có ba chữ số có nghĩa: $3.14$.

Trong phần lớn các ví dụ và bài tập, số liệu thường được cho với ba chữ số có nghĩa, nên kết quả không nên ghi quá ba chữ số. Nhiều con số ngoài thực tế còn kém chính xác hơn. Chẳng hạn, đồng hồ tốc độ xe thường chỉ cho hai chữ số có nghĩa. Dù máy tính cầm tay hiển thị mười chữ số, ghi cả mười chữ số sẽ thể hiện sai lệch độ chính xác của phép đo.

Hãy làm tròn đáp số cuối đến số chữ số có nghĩa thích hợp. Khi giảm số chữ số, cần **làm tròn** đúng quy tắc, không chỉ cắt bỏ đơn thuần. Ví dụ: Máy tính cho $525/311 \approx 1.688102894$. Với ba chữ số có nghĩa, kết quả là $1.69$, không phải $1.68$.

Với phép tính nhiều bước, nên giữ thêm chữ số ở các bước trung gian, rồi chỉ làm tròn khi đã có đáp số cuối. Cách này hạn chế sai số làm tròn tích lũy.

### Ký pháp khoa học

Với số rất lớn hoặc rất nhỏ, **ký pháp khoa học** (cách viết theo lũy thừa của $10$) thể hiện chữ số có nghĩa rõ ràng nhất. Khoảng cách từ Trái Đất tới Mặt Trăng khoảng $384\,000\,000\,\mathrm m$, nhưng cách viết ấy không chỉ rõ có bao nhiêu chữ số có nghĩa.

Dịch dấu thập phân sang trái tám hàng, tương ứng chia cho $10^8$, rồi nhân lại với $10^8$:

$$
\begin{aligned}
d &= 384\,000\,000\,\mathrm m \\
&= 3.84\times10^8\,\mathrm m.
\end{aligned}
$$

Ở dạng này, ta thấy rõ ba chữ số có nghĩa. Số $4.00\times10^{-7}$ cũng có ba chữ số có nghĩa dù hai chữ số cuối là số không. Thông thường, ký pháp khoa học biểu diễn giá trị dương bằng một số từ $1$ đến dưới $10$, nhân với lũy thừa thích hợp của $10$.

Khi một số nguyên hoặc phân số xuất hiện như hệ số chính xác trong phương trình đại số, ta xem nó không có độ bất định. Chẳng hạn, trong phương trình chuyển động:

$$
v_x^2 = v_{0x}^2 + 2a_x(x - x_0),
$$

hệ số $2$ đúng bằng $2$, có thể coi là có vô hạn chữ số có nghĩa: $2.000000\ldots$ Điều tương tự áp dụng cho số mũ $2$ trong $v_x^2$ và $v_{0x}^2$.

### Độ chụm và độ đúng

**Độ chụm** (*precision*) và **độ đúng** (*accuracy*) là hai khái niệm khác biệt:
- **Độ chụm**: Thể hiện mức độ chi tiết và tính lặp lại của phép đo. Một đồng hồ điện tử rẻ tiền hiển thị $10{:}35{:}17$ có độ chụm đến từng giây. Nhưng nếu nó chạy chậm vài phút, giá trị hiển thị không có độ đúng.
- **Độ đúng**: Thể hiện mức độ gần của kết quả đo so với giá trị thực. Một chiếc đồng hồ quả lắc chỉ đúng giờ có độ đúng cao, nhưng không có kim giây nên độ chụm thấp hơn.

Một phép đo khoa học chất lượng cao đòi hỏi phải có cả độ chụm lẫn độ đúng.

### Ví dụ 1.3: Chữ số có nghĩa trong phép nhân

::: exercise Ví dụ 1.3: Chữ số có nghĩa trong phép nhân
Năng lượng nghỉ $E$ của một vật có khối lượng nghỉ $m$ được cho bởi phương trình nổi tiếng của Albert Einstein: $E = mc^2$, trong đó $c$ là tốc độ ánh sáng trong chân không. Hãy tìm $E$ cho một electron có khối lượng nghỉ được cho với ba chữ số có nghĩa: $m = 9.11\times10^{-31}\,\mathrm{kg}$. Biết đơn vị năng lượng SI là joule ($\mathrm J$), với $1\,\mathrm J = 1\,\mathrm{kg\cdot m^2/s^2}$.
:::

::: solution Lời giải
**Tóm tắt đề bài**:
- Khối lượng electron: $m = 9.11\times10^{-31}\,\mathrm{kg}$ (3 chữ số có nghĩa).
- Tốc độ ánh sáng trong chân không: $c = 2.99792458\times10^8\,\mathrm{m/s}$ (chính xác tuyệt đối).
- Cần tìm: Năng lượng nghỉ $E$ với số chữ số có nghĩa phù hợp.

**Hướng đi**:
- Vận dụng hệ thức Einstein: $E = mc^2$.
- Phép nhân giữa $m$ (3 chữ số có nghĩa) và $c^2$ đòi hỏi kết quả cuối cùng phải được làm tròn về đúng ba chữ số có nghĩa.

**Lời giải chi tiết**:
Khi bình phương tốc độ ánh sáng, số mũ của $10$ tăng từ $8$ lên $16$. Nhân với khối lượng có số mũ $-31$ cho số mũ tổng:

$$
-31+2(8)=-15.
$$

Tách riêng hệ số số học để theo dõi phép nhân:

$$
\begin{aligned}
\beta &= 9.11(2.99792458)^2 \\
&= 81.87659678\ldots
\end{aligned}
$$

Hệ số $\beta$ không mang đơn vị. Vì $\mathrm{kg\cdot m^2/s^2}$ là joule, ta được:

$$
\begin{aligned}
E &= mc^2 \\
&= \beta\times10^{-15}\,\mathrm J \\
&\approx 8.187659678\times10^{-14}\,\mathrm J \\
&\approx 8.19\times10^{-14}\,\mathrm J.
\end{aligned}
$$

Dù tốc độ ánh sáng được xác định chính xác, khối lượng $m$ chỉ có ba chữ số có nghĩa. Vì thế đáp số cuối cũng giữ ba chữ số có nghĩa.

**Đánh giá**:
Năng lượng này có vẻ rất nhỏ trong đời sống hằng ngày, nhưng lại rất lớn ở quy mô hạt vi mô. Để so sánh: Năng lượng mà một nguyên tử nhận hoặc mất trong một phản ứng hóa học điển hình chỉ vào khoảng $10^{-19}\,\mathrm J$. Do đó năng lượng nghỉ của electron lớn hơn năng lượng hóa học nguyên tử tới gần một triệu lần. Ta sẽ tìm hiểu sâu hơn về ý nghĩa của năng lượng nghỉ trong thuyết tương đối hẹp.
:::

### Câu hỏi tự kiểm tra hiểu bài 1.5

::: exercise Câu hỏi tự kiểm tra 1.5: Khối lượng riêng của hòn đá
Khối lượng riêng bằng khối lượng chia cho thể tích. Một hòn đá có khối lượng $1.80\,\mathrm{kg}$ và thể tích $6.0\times10^{-4}\,\mathrm{m^3}$. Khối lượng riêng, tính bằng $\mathrm{kg/m^3}$, nên được ghi bằng phương án nào dưới đây?

- (i) $3\times10^3$
- (ii) $3.0\times10^3$
- (iii) $3.00\times10^3$
- (iv) $3.000\times10^3$
- (v) Phương án nào cũng được vì các giá trị đều bằng nhau về mặt toán học.
:::

::: solution Lời giải chi tiết
Chọn **(ii) $3.0\times10^3\,\mathrm{kg/m^3}$**.

**Giải thích**:
Tính khối lượng riêng theo định nghĩa:

$$
\begin{aligned}
\rho &= \frac{m}{V} \\
&= \frac{1.80\,\mathrm{kg}}{6.0\times10^{-4}\,\mathrm{m^3}} \\
&= 3000\,\mathrm{kg/m^3}.
\end{aligned}
$$

Trong phép chia, số chữ số có nghĩa của kết quả do số hạng kém chính xác nhất quyết định:
- Khối lượng $m = 1.80\,\mathrm{kg}$ có ba chữ số có nghĩa.
- Thể tích $V = 6.0\times10^{-4}\,\mathrm{m^3}$ có hai chữ số có nghĩa.

Do đó, kết quả bắt buộc phải được trình bày với đúng hai chữ số có nghĩa: $3.0\times10^3\,\mathrm{kg/m^3}$.
:::
