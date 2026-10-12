<!-- Source: Section23.5, printed767–769, PDF787–789. -->

## 23.5. Gradient điện thế

Đã biết trường theo vị trí, ta tích phân để tìm hiệu điện thế. Theo chiều ngược lại, biết điện thế như hàm V(x,y,z) cho phép tìm trường bằng đạo hàm.

Từ hệ thức tích phân giữa a,b, so sánh tích phân trường với biến thiên điện thế cho mọi khoảng rất nhỏ:

$$
-dV=\vec E\cdot d\vec\ell.
$$

Khai triển hai vector trong hệ trục vuông góc:

$$
\begin{aligned}
\vec E&=E_x\hat{\mathbf i}+E_y\hat{\mathbf j}+E_z\hat{\mathbf k},\\
d\vec\ell&=dx\hat{\mathbf i}+dy\hat{\mathbf j}+dz\hat{\mathbf k},\\
-dV&=E_xdx+E_ydy+E_zdz.
\end{aligned}
$$

Nếu chỉ dịch chuyển theo x, giữ y,z không đổi, thì −dV = Eₓdx. Đạo hàm theo một tọa độ trong khi giữ những tọa độ khác không đổi là **đạo hàm riêng**. Tương tự cho ba trục:

$$
\begin{aligned}
E_x&=-\frac{\partial V}{\partial x},\\
E_y&=-\frac{\partial V}{\partial y},\\
E_z&=-\frac{\partial V}{\partial z}.
\end{aligned}
\tag{23.19}
$$

Các đạo hàm có đơn vị V/m, khớp đơn vị trường. Dạng vector là:

$$
\begin{aligned}
\vec E&=-\hat{\mathbf i}\frac{\partial V}{\partial x}\\
&\quad-\hat{\mathbf j}\frac{\partial V}{\partial y}\\
&\quad-\hat{\mathbf k}\frac{\partial V}{\partial z}.
\end{aligned}
\tag{23.20}
$$

Với hàm f bất kỳ, định nghĩa gradient bằng ba thành phần đạo hàm riêng:

$$
\begin{aligned}
\nabla f&=\hat{\mathbf i}\frac{\partial f}{\partial x}\\
&\quad+\hat{\mathbf j}\frac{\partial f}{\partial y}\\
&\quad+\hat{\mathbf k}\frac{\partial f}{\partial z}.
\end{aligned}
\tag{23.21}
$$

Ký hiệu ∇ được đọc là grad hoặc del. Hệ thức trường–điện thế viết ngắn thành:

$$
\vec E=-\nabla V.
\tag{23.22}
$$

Gradient điện thế hướng theo phía V tăng nhanh nhất tại điểm. Điện trường, có dấu trừ, hướng theo phía V giảm nhanh nhất và vuông góc mặt đẳng thế ở nơi trường khác không.

Đổi mốc điện thế chỉ cộng một hằng số vào V ở mọi điểm. Đạo hàm của hằng số bằng không, nên điện trường không đổi. Nếu dùng khoảng cách xuyên tâm r từ một điểm hoặc một trục, thành phần xuyên tâm là:

$$
E_r=-\frac{\partial V}{\partial r}.
\tag{23.23}
$$

Tính trường trực tiếp cần cộng vector hoặc tích phân từng thành phần. Tính điện thế trước chỉ cần tổng hoặc tích phân vô hướng, rồi lấy gradient. Vì vậy cách thứ hai thường làm tính toán gọn hơn. Tuy nhiên phải biết **miền mà biểu thức điện thế đúng** trước khi lấy đạo hàm.

### Ứng dụng: Điện thế qua màng tế bào

Trong mô hình tế bào nghỉ, điện thế bên trong thấp hơn bên ngoài. Hiệu bên trong so với bên ngoài điển hình cỡ −70 mV ở neuron và −95 mV ở tế bào cơ xương. Vì vậy gradient điện thế hướng từ trong ra ngoài màng, còn điện trường hướng từ ngoài vào trong. Trường ảnh hưởng sự đi vào, đi ra của các ion natri, kali, canxi qua những kênh chuyên biệt trong màng.

![Điện trường qua màng ảnh hưởng sự di chuyển của ion canxi, kali và natri](../img/young-23/ung-dung-mang-te-bao.png)

### Ví dụ 23.13: Trường từ điện thế nguồn điểm

Điện thế nguồn điểm q là $V = \frac{kq}{r}$. Tìm vector trường.

::: solution Chi tiết
**Xác định và thiết lập.** Đối xứng cho trường chỉ có thành phần xuyên tâm. Dùng (23.23):

$$
\begin{aligned}
E_r&=-\frac{d}{dr}\left(\frac{kq}{r}\right)\\
&=\frac{kq}{r^2},\\
\vec E&=\frac{kq}{r^2}\hat{\mathbf r}.
\end{aligned}
$$

Kết quả trùng trường Coulomb (21.7), kể cả dấu của q.

**Cách tính bằng tọa độ.** Không dùng đối xứng ngay, viết $r=\sqrt{x^2+y^2+z^2}$. Quy tắc đạo hàm hàm hợp cho:

$$
\begin{aligned}
\frac{\partial V}{\partial x}&=-\frac{kqx}{r^3},\\
\frac{\partial V}{\partial y}&=-\frac{kqy}{r^3},\\
\frac{\partial V}{\partial z}&=-\frac{kqz}{r^3}.
\end{aligned}
$$

Thay vào gradient và nhận $\hat{\mathbf r}=\frac{x\hat{\mathbf i}+y\hat{\mathbf j}+z\hat{\mathbf k}}{r}$:

$$
\begin{aligned}
\vec E&=\frac{kq}{r^3}
(x\hat{\mathbf i}+y\hat{\mathbf j}+z\hat{\mathbf k})\\
&=\frac{kq}{r^2}\hat{\mathbf r}.
\end{aligned}
$$

Hai cách cho cùng kết quả. Khai thác đối xứng ngay từ đầu giúp tránh ba đạo hàm riêng không cần thiết.
:::

### Ví dụ 23.14: Trường trên trục vòng tích điện

Vòng bán kính a mang Q có điện thế trên trục x là $V(x)=\frac{kQ}{\sqrt{x^2+a^2}}$. Tìm trường tại điểm trên trục.

::: solution Chi tiết
**Xác định và thiết lập.** Đối xứng của vòng buộc các thành phần y,z bằng không **trên trục**. Lấy đạo hàm điện thế theo x để tìm thành phần còn lại:

$$
\begin{aligned}
E_x&=-\frac{d}{dx}\left[kQ(x^2+a^2)^{-1/2}\right]\\
&=\frac{kQx}{(x^2+a^2)^{3/2}}.
\end{aligned}
$$

Trùng Ví dụ 21.9. Biểu thức điện thế được cho chỉ đúng trên trục, nên không dùng nó để suy trường ở điểm ngoài trục. Biết V dọc một đường chỉ cho thành phần trường tiếp tuyến đường ấy qua đạo hàm. Kết luận các thành phần vuông góc bằng không ở đây phải dựa thêm vào đối xứng, không được suy chỉ từ việc biểu thức trên trục không viết y,z.
:::

::: exercise Câu hỏi ôn lại mục 23.5
Trong vùng có $V=A+Bx+Cy^3+Dxy$, với A,B,C,D dương, những phát biểu nào đúng? (i) Tăng A làm trường tăng ở mọi điểm. (ii) Tăng A làm trường giảm ở mọi điểm. (iii) Trường không có thành phần z. (iv) Trường bằng không ở gốc.
:::

::: solution Giải thích
Đạo hàm từng tọa độ cho:

$$
\begin{aligned}
E_x&=-(B+Dy),\\
E_y&=-(3Cy^2+Dx),\\
E_z&=0.
\end{aligned}
$$

A không ảnh hưởng các đạo hàm. Ở gốc, Eₓ = −B khác không. Vì vậy chỉ (iii) đúng. Cộng một hằng số vào điện thế không đổi trường hoặc hiệu điện thế.
:::
