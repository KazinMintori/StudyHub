## Tổng kết chương

### Hàm sóng và phương trình Schrödinger

Hàm sóng $\Psi(x,t)$ chứa thông tin về trạng thái của hạt trong mô hình đang xét. Mật độ xác suất bằng $|\Psi(x,t)|^2$, còn xác suất trên một khoảng được tính bằng tích phân mật độ trên khoảng ấy.

Với hạt phi tương đối tính chuyển động một chiều trong thế năng $U(x)$, toán tử Hamilton có dạng

$$
\hat H=-\frac{\hbar^2}{2m}\frac{\partial^2}{\partial x^2}+U(x).
$$

Phương trình tiến triển theo thời gian là

$$
i\hbar\frac{\partial\Psi}{\partial t}=\hat H\Psi.
$$

Hạng đạo hàm bậc hai biểu diễn động năng, còn hạng nhân với $U(x)$ biểu diễn thế năng. Với hạt tự do, $U=0$ khi chọn mốc thích hợp.

Trong một trạng thái có năng lượng xác định,

$$
\Psi(x,t)=\psi(x)e^{-iEt/\hbar}.
$$

Khi đó, $|\Psi|^2=|\psi|^2$ không phụ thuộc thời gian, còn $\psi$ thỏa phương trình Schrödinger không phụ thuộc thời gian:

$$
-\frac{\hbar^2}{2m}\psi''+U\psi=E\psi.
$$

Chồng chập các trạng thái dừng cho những trạng thái tổng quát hơn. Các gói sóng có thể tập trung trong một miền không gian và biểu hiện đồng thời tính sóng lẫn sự định xứ của hạt.

![Tổng kết hàm sóng: Phần thực và phần ảo của một hàm sóng phức có thể dao động theo tọa độ. Xác suất phải được tính từ bình phương môđun của toàn bộ hàm phức.](./img/young-40/tom-tat-ham-song.png)

### Hạt trong hộp vô hạn

Với hộp rộng $L$, thế năng bằng không bên trong và vô hạn bên ngoài, các mức được đánh số $n=1,2,3,\ldots$:

$$
\begin{aligned}
E_n&=\frac{p_n^2}{2m}\\
&=\frac{n^2h^2}{8mL^2}\\
&=\frac{n^2\pi^2\hbar^2}{2mL^2}.
\end{aligned}
$$

Các hàm riêng đã chuẩn hóa bên trong hộp là

$$
\psi_n(x)=\sqrt{\frac2L}\sin\frac{n\pi x}{L}.
$$

Chúng bằng không ở hai vách và bên ngoài. Trạng thái $n=0$ chỉ cho hàm bằng không nên không phải một trạng thái vật lý.

![Tổng kết hạt trong hộp: Ba hàm sóng dừng đầu tiên cùng hai vách. Số nửa bước sóng vừa trong hộp bằng số lượng tử n.](./img/young-40/tom-tat-hat-trong-hop.png)

### Chuẩn hóa và điều kiện nối nghiệm

Đối với một trạng thái chuẩn hóa được trên toàn trục,

$$
\int_{-\infty}^{\infty}|\psi(x)|^2\,dx=1.
$$

Điều kiện này nói rằng xác suất tìm thấy hạt ở đâu đó bằng một. Hàm sóng và đạo hàm phải liên tục qua các bước thế năng hữu hạn, với khối lượng không đổi và không có tương tác kỳ dị tại biên. Thành giếng vô hạn cần được xử lý bằng điều kiện biên riêng, không áp máy móc quy tắc nối đạo hàm.

![Tổng kết chuẩn hóa: Mật độ xác suất của ba mức đầu trong hộp có số đỉnh khác nhau, nhưng tích phân trên toàn hộp đều bằng một.](./img/young-40/tom-tat-chuan-hoa.png)

### Giếng thế hữu hạn

Giếng hữu hạn chỉ có một số hữu hạn trạng thái liên kết. Với cùng khối lượng, cùng chiều rộng và cùng mốc thế năng tại đáy, các mức liên kết thấp hơn các mức tương ứng của giếng vô hạn. Hàm sóng thâm nhập ra ngoài và giảm theo hàm mũ trong vùng bị cấm cổ điển.

Năng lượng được xác định bằng cách nối $\psi$ và $\psi'$ tại hai biên. Phần nằm ngoài giếng không được bỏ đi khi chuẩn hóa. Những mức trên ngưỡng thoát thuộc phổ liên tục, không phải những trạng thái liên kết bổ sung.

![Tổng kết giếng hữu hạn: Ví dụ giếng sâu bằng sáu lần năng lượng cơ bản của hộp vô hạn cùng rộng có ba mức liên kết. Trên ngưỡng U₀ là phổ năng lượng liên tục.](./img/young-40/tom-tat-gieng-huu-han.png)

### Hàng rào thế và xuyên hầm

Một hạt có cơ năng nhỏ hơn chiều cao hàng rào vẫn có xác suất truyền qua. Với hàng rào chữ nhật và hệ số truyền rất nhỏ,

$$
T\approx Ge^{-2kL}.
$$

Ở đây $k=\sqrt{2m(U_0-E)}/\hbar$ và $G=16(E/U_0)(1-E/U_0)$. Độ rộng và độ chênh năng lượng tác động lên số mũ, làm xác suất xuyên hầm thay đổi nhanh.

![Tổng kết xuyên hầm: Nghiệm giảm theo dạng mũ trong hàng rào vẫn nối với một nghiệm có biên độ khác không ở phía bên kia.](./img/young-40/tom-tat-xuyen-ham.png)

### Dao động tử điều hòa

Với thế năng $U=k'x^2/2$ và $\omega=\sqrt{k'/m}$, các mức năng lượng là

$$
E_n=\left(n+\frac12\right)\hbar\omega.
$$

Số lượng tử nhận các giá trị $n=0,1,2,\ldots$. Các mức liền nhau cách đều $\hbar\omega$, còn mức cơ bản có năng lượng $\hbar\omega/2$. Hàm sóng cơ bản là Gaussian và đạt tích độ bất định bằng $\hbar/2$.

![Tổng kết dao động tử: Các mức cách đều nằm trên thế năng parabol, bắt đầu từ mức năng lượng điểm không ℏω/2.](./img/young-40/tom-tat-dao-dong.png)

### Phép đo và trạng thái sau phép đo

Một trạng thái có năng lượng xác định không nhất thiết có động lượng xác định. Khi đo lý tưởng một đại lượng mà trạng thái là chồng chập của các trạng thái riêng tương ứng, mỗi kết quả có xác suất và trạng thái có điều kiện thay đổi theo kết quả ấy.

Ngược lại, đo năng lượng lý tưởng trên một trạng thái riêng năng lượng không bắt buộc làm đổi trạng thái. Muốn mô tả chính xác một phép đo thực, phải xác định dụng cụ, tương tác và điều kiện biên, thay vì coi mọi bố trí đều thực hiện cùng một phép chiếu.

### Trở lại câu hỏi mở đầu

Lựa chọn đúng là **1**: Các mức năng lượng của electron cách xa nhau hơn trong hạt nhỏ. Khi electron chuyển xuống một mức thấp hơn, photon phát ra mang phần năng lượng chênh lệch giữa hai mức.

Trong mô hình giam giữ đơn giản, giảm kích thước làm khoảng cách mức tăng. Photon có năng lượng cao hơn nên bước sóng ngắn hơn, tương ứng với phía xanh của phổ nhìn thấy. Hạt lớn hơn có thể phát photon năng lượng thấp hơn và bước sóng dài hơn, về phía đỏ.
