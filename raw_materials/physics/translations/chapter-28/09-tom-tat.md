## Tóm tắt Chương 28: Nguồn của từ trường

### Từ trường do điện tích chuyển động

![Sơ đồ chồng chất các vectơ trường do điện tích chuyển động tạo ra](img/young-28/tom-tat-28-01-dien-tich-chuyen-dong.png)

Với điện tích $q$ chuyển động vận tốc $\vec v$, trường tại điểm cách nguồn khoảng $r$ vuông góc với cả $\vec v$ và vectơ đơn vị $\hat r$ hướng từ nguồn đến điểm khảo sát:

$$
\vec B=\frac{\mu_0}{4\pi}\frac{q\,\vec v\times\hat r}{r^2}.
\tag{28.2}
$$

Với nhiều điện tích chuyển động, trường tổng là tổng vectơ các trường riêng.

### Từ trường do phần tử dòng điện

![Phần tử dòng điện và hướng trường vi phân theo định luật Biot–Savart](img/young-28/tom-tat-28-02-biot-savart.png)

Định luật Biot–Savart cho trường vi phân do phần tử $I,d\vec l$ tạo ra. Trường vuông góc với $d\vec l$ và $\hat r$:

$$
d\vec B=\frac{\mu_0}{4\pi}\frac{I\,d\vec l\times\hat r}{r^2}.
\tag{28.6}
$$

Trường của một dây hữu hạn là tích phân các đóng góp vi phân dọc toàn bộ dây.

### Dây dẫn thẳng dài và lực giữa hai dây

![Đường sức tròn quanh dây dẫn thẳng dài](img/young-28/tom-tat-28-03-day-thang.png)

Với dây thẳng dài mang dòng $I$, trường tại khoảng cách $r$ có độ lớn:

$$
B=\frac{\mu_0I}{2\pi r}.
\tag{28.9}
$$

Đường sức là các đường tròn đồng tâm với dây, chiều theo quy tắc bàn tay phải.

![Hai dây song song mang dòng hút nhau khi cùng chiều và đẩy nhau khi ngược chiều](img/young-28/tom-tat-28-04-luc-giua-day.png)

Hai dây thẳng dài song song cách nhau khoảng $r$, mang các dòng $I$ và $I'$, chịu lực trên một đơn vị chiều dài:

$$
\frac{F}{L}=\frac{\mu_0II'}{2\pi r}.
\tag{28.11}
$$

Dòng cùng chiều làm hai dây hút nhau. Dòng ngược chiều làm chúng đẩy nhau.
Định nghĩa ampe gắn với lực trên một đơn vị chiều dài giữa hai dây song song.

### Vòng dây mang dòng

![Phân tích thành phần trường do phần tử dòng điện của vòng tròn](img/young-28/tom-tat-28-05-vong-dong.png)

Với vòng tròn bán kính $a$, trường tại điểm trên trục cách tâm $x$ chỉ còn thành phần theo trục. Các thành phần ngang của những phần tử đối diện triệt tiêu. Trường trên trục và trường ở tâm cuộn $N$ vòng là:

$$
\begin{aligned}
 &B_x = \frac{\mu_0Ia^2}{2(x^2+a^2)^{3/2}}.\end{aligned}
\tag{28.15}
$$

Tại tâm của cuộn $N$ vòng, kết quả là $B_x(0)=\mu_0NI/(2a)$ (28.17).

Nếu cuộn có $N$ vòng giống nhau, trường của một vòng trên trục được nhân với $N$. Các biểu thức này chỉ dùng trên trục. Chiều trường được xác định bằng quy tắc bàn tay phải.

### Định luật Ampere

![Đường tích phân kín và thành phần tiếp tuyến của trường từ](img/young-28/tom-tat-28-06-ampere.png)

Tích phân đường kín của trường từ bằng độ từ thẩm chân không nhân tổng đại số dòng điện xuyên qua mặt được đường kín bao quanh:

$$
\oint\vec B\cdot d\vec l=\mu_0I_{\mathrm{encl}}.
\tag{28.20}
$$

Quy tắc bàn tay phải xác định dấu dòng điện. Định luật hữu ích để tính trực tiếp $B$ khi phân bố dòng có đối xứng cao, chẳng hạn dây thẳng dài, dây trụ, ống dây dài và hình xuyến. Trong cách dùng từ tĩnh, các dòng phải không đổi và không có điện trường biến thiên theo thời gian.

### Bảng trường của các phân bố dòng điện đối xứng

![Bảng đầy đủ các trường từ do dây thẳng, vòng dây, dây trụ, ống dây và hình xuyến tạo ra](img/young-28/tom-tat-28-bang-phan-bo-dong.png)

Bảng dưới đây tổng hợp vị trí khảo sát, điều kiện hình học và độ lớn trường của các cấu hình đối xứng.

#### Dây thẳng dài

Điểm khảo sát cách dây mang dòng I một khoảng r:

$$
B=\frac{\mu_0I}{2\pi r}.
$$

#### Vòng dây tròn và cuộn đồng tâm

Vòng có bán kính a. Điểm nằm trên trục cách tâm x:

$$
B_x=\frac{\mu_0Ia^2}{2(x^2+a^2)^{3/2}}.
$$

Với N vòng cùng diện tích và cùng chiều dòng, nhân trường của một vòng với N. Tại tâm:

$$
B(0)=\frac{\mu_0NI}{2a}.
$$

#### Dây trụ đặc có dòng phân bố đều

Dây dài bán kính R, tổng dòng I. Bên trong trụ:

$$
B(r)=\frac{\mu_0I}{2\pi}\frac r{R^2}.
$$

Bên ngoài trụ:

$$
B(r)=\frac{\mu_0I}{2\pi r}.
$$

Hai biểu thức cho cùng giá trị tại r = R.

#### Ống dây dài quấn sít

Mật độ vòng n, dòng I. Bên trong gần trung điểm:

$$
B\approx\mu_0nI.
$$

Bên ngoài gần trung điểm:

$$
B\approx0.
$$

#### Ống dây hình xuyến

Cuộn quấn sít có N vòng, dòng I. Trong vùng lõi ở khoảng cách r tới trục xuyến:

$$
B(r)=\frac{\mu_0NI}{2\pi r}.
$$

Trong mô hình lý tưởng, trường bằng không trong lỗ giữa và phía ngoài xuyến:

$$
B=0.
$$

Với ống dây thẳng, các giá trị trong bảng là gần đúng cho miền giữa một ống dài và quấn sít. Với xuyến, trường trong lõi phụ thuộc bán kính $r$. Trường ngoài xuyến quấn thực không hoàn toàn bằng không vì dây quấn có độ nghiêng hữu hạn.

### Từ tính trong vật chất

![Đường trễ biểu diễn độ từ hóa theo trường ngoài](img/young-28/tom-tat-28-tu-tinh.png)

Độ từ hóa $\vec M$ là mômen từ tổng trên một đơn vị thể tích, và đóng góp thêm vào trường là $\mu_0\vec M$. Nếu $\vec B_0$ là trường do các dòng điện ngoài vật liệu tạo ra, trường tổng là $\vec B=\vec B_0+\mu_0\vec M$. Với vật liệu thuận từ hoặc nghịch từ trong miền đáp ứng tuyến tính, có thể thay $\mu_0$ trong công thức trường bằng độ từ thẩm $\mu=K_m\mu_0$. Độ cảm từ được định nghĩa:

$$
\chi_m=K_m-1.
$$

Vật liệu thuận từ có độ cảm từ dương nhỏ. Vật liệu nghịch từ có độ cảm từ âm nhỏ và gần như ít phụ thuộc nhiệt độ. $K_m$ và $\chi_m$ đều không thứ nguyên. Vật liệu sắt từ có độ từ thẩm tương đối lớn nhưng không cố định. Độ từ hóa phụ thuộc quá trình tăng và giảm trường ngoài, tạo vòng trễ. Một số vật liệu sắt từ vẫn giữ độ từ hóa đáng kể khi bỏ trường ngoài, nên có thể dùng làm nam châm vĩnh cửu.
