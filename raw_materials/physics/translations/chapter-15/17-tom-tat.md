## Tổng kết chương 15

### Sóng và các đại lượng đặc trưng

Sóng là nhiễu loạn truyền từ vùng này sang vùng khác. Sóng cơ cần môi trường vật chất. Tốc độ truyền phụ thuộc loại sóng và tính chất của môi trường, còn chuyển động của từng phần tử cần được phân biệt với sự truyền nhiễu loạn.

Với sóng tuần hoàn, $T$ là chu kỳ, $f=1/T$ là tần số, $A$ là biên độ li độ và $\lambda$ là bước sóng. Trong một chu kỳ, dạng sóng truyền một bước sóng:

$$
v=\lambda f.
$$

Sóng hình sin là trường hợp tuần hoàn mà từng phần tử dao động điều hòa. Sóng ngang có phương dao động vuông góc chiều truyền, còn sóng dọc có hai phương trùng nhau.

![Tổng kết: Biên độ, bước sóng và tốc độ truyền của sóng ngang, trong khi từng phần tử dây dao động điều hòa](/vat-ly-1/bai-giang/img/young-15/r-theory-summary-01.png)

### Hàm sóng và động lực học sóng

Hàm $y(x,t)$ cho li độ của phần tử ở vị trí cân bằng $x$ tại thời điểm $t$. Với sóng hình sin truyền theo chiều dương:

$$
y(x,t)=A\cos\!\left[\omega\left(\frac xv-t\right)\right].
$$

Đây là công thức (15.3). Dùng $T=1/f$, $\lambda=vT$ và viết $y$ cho cùng hàm $y(x,t)$:

$$
y=A\cos\!\left[2\pi\left(\frac x\lambda-\frac tT\right)\right].
$$

Đây là công thức (15.4). Dạng tương đương (15.7) là:

$$
y(x,t)=A\cos(kx-\omega t).
$$

Các tham số liên hệ qua:

$$
k=\frac{2\pi}{\lambda},\qquad \omega=2\pi f=vk.
$$

Đổi dấu trừ giữa phần không gian và thời gian thành dấu cộng cho sóng truyền theo chiều âm. Cùng một hàm có thể được đọc theo $x$ ở thời điểm cố định để thấy hình dạng, hoặc theo $t$ tại một vị trí để thấy dao động của phần tử.

![Tổng kết: Đồ thị li độ theo vị trí cho bước sóng, còn đồ thị li độ theo thời gian cho chu kỳ](/vat-ly-1/bai-giang/img/young-15/r-theory-summary-02.png)

Trong mô hình tuyến tính, hàm sóng thỏa phương trình (15.12):

$$
\frac{\partial^2y}{\partial x^2}
=\frac1{v^2}\frac{\partial^2y}{\partial t^2}.
$$

Với dây mềm đồng nhất, lực căng gần đều và dao động ngang nhỏ:

$$
v=\sqrt{\frac F\mu}.
$$

Đó là công thức (15.14), trong đó $\mu$ là khối lượng trên một đơn vị chiều dài.

### Công suất và cường độ sóng

Sóng truyền năng lượng. Với một sóng chạy hình sin trên dây, công suất trung bình theo công thức (15.25) là:

$$
P_{\mathrm{tb}}=\frac12\sqrt{\mu F}\,\omega^2A^2.
$$

Giữ nguyên môi trường và lực căng, công suất tỉ lệ $A^2f^2$, với $A$ là biên độ li độ. Công suất tức thời dao động giữa không và cực đại, còn trung bình bằng nửa cực đại.

![Tổng kết: Công suất tức thời biến đổi hai lần trong mỗi chu kỳ, với đường trung bình bằng một nửa cực đại](/vat-ly-1/bai-giang/img/young-15/r-theory-summary-03.png)

Cường độ là công suất trung bình trên một đơn vị diện tích vuông góc chiều truyền. Với nguồn phát đều mọi hướng và không có hấp thụ, công suất phân bố trên diện tích cầu nên:

$$
\frac{I_1}{I_2}=\frac{r_2^2}{r_1^2}.
$$

Đó là định luật nghịch đảo bình phương (15.26). Điều kiện không tổn thất và phân bố đều theo hướng là một phần của kết luận.

### Chồng chất và phản xạ

Sóng gặp biên có thể phản xạ. Với đầu cố định, xung phản xạ đảo dấu li độ. Với đầu tự do lý tưởng, xung phản xạ giữ nguyên dấu.

Trong miền tuyến tính, li độ của hai sóng chồng nhau được cộng đại số tại cùng vị trí và thời điểm:

$$
y(x,t)=y_1(x,t)+y_2(x,t).
$$

Công thức (15.27) là nguyên lý chồng chất. Tăng cường hay triệt tiêu mô tả li độ tổng, không có nghĩa từng sóng bị tiêu hủy sau khi vượt qua nhau.

![Tổng kết: Li độ tổng khi hai xung chồng lên nhau được xác định bằng phép cộng đại số từng li độ](/vat-ly-1/bai-giang/img/young-15/r-theory-summary-04.png)

### Sóng dừng và các dạng dao động riêng

Hai sóng sin cùng biên độ, tần số và bước sóng truyền ngược chiều có thể tạo sóng dừng. Với nút tại $x=0$:

$$
y(x,t)=A_{\mathrm{SW}}\sin kx\sin\omega t.
$$

Đó là công thức (15.28), với $A_{\mathrm{SW}}=2A$. Hai nút hoặc hai bụng liên tiếp cách nhau $\lambda/2$, còn nút và bụng kề cách nhau $\lambda/4$. Công suất trung bình qua mọi tiết diện bằng không dù có trao đổi năng lượng cục bộ theo thời gian.

Với dây dài $L$ cố định hai đầu, lần lượt có một, hai, ba, v.v. nửa bước sóng trong chiều dài dây. Những tần số tương ứng là $f_1$, $2f_1$, $3f_1$, v.v. Viết gọn:

$$
f_n=\frac{nv}{2L}=nf_1.
$$

Đây là công thức (15.33), với $n=1,2,3,\ldots$. Dùng tính chất dây, tần số cơ bản còn có dạng (15.35):

$$
f_1=\frac1{2L}\sqrt{\frac F\mu}.
$$

![Tổng kết: Bốn dạng dao động riêng đầu tiên của dây cố định hai đầu, từ một đến bốn bó sóng](/vat-ly-1/bai-giang/img/young-15/r-theory-summary-05.png)

Mỗi dạng riêng có cùng tần số tại mọi điểm dao động nhưng biên độ phụ thuộc vị trí. Chồng nhiều dạng riêng cho chuyển động phức tạp và các thành phần họa âm của âm phát ra. Tần số của sóng âm bằng tần số kích thích từ dây, còn bước sóng có thể khác vì tốc độ truyền trong không khí khác trên dây.
