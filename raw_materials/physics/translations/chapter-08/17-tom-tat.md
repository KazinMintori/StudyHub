## Tổng kết

Chương 8 phát triển hoàn chỉnh các nguyên lý bảo toàn động lượng và chuyển động của hệ chất điểm. Dưới đây là hệ thống hóa các định luật, công thức cốt lõi và phạm vi ứng dụng trong toàn bộ chương.

### Động lượng của một chất điểm

Động lượng $\vec{p}$ của một chất điểm là một đại lượng vector bằng tích của khối lượng $m$ với vận tốc $\vec{v}$ của chất điểm đó:

$$
\vec{p} = m\vec{v}
$$

Công thức (8.2).

Định luật II Newton cho phép phát biểu khái quát tốc độ biến thiên động lượng của chất điểm dưới tác dụng của hợp ngoại lực $\sum \vec{F}$:

$$
\sum \vec{F} = \frac{d\vec{p}}{dt}
$$

Công thức (8.4).



![Vector động lượng và các thành phần tọa độ](/vat-ly-1/bai-giang/img/young-08/r-theory-tom-tat-1.png)

### Xung lượng và Động lượng

Nếu một hợp lực không đổi $\sum \vec{F}$ tác dụng lên chất điểm trong khoảng thời gian $\Delta t = t_2 - t_1$, xung lượng $\vec{J}$ của lực được định nghĩa là:

$$
\vec{J} = \sum \vec{F}\,\Delta t
$$

Công thức (8.5).

Nếu hợp lực $\sum \vec{F}$ biến thiên liên tục theo thời gian, xung lượng $\vec{J}$ được tính bằng tích phân:

$$
\vec{J} = \int_{t_1}^{t_2} \sum \vec{F}\,dt
$$

Công thức (8.7).

**Định lý xung lượng - động lượng**: Xung lượng của hợp lực tác dụng lên một chất điểm trong một khoảng thời gian bằng đúng độ biến thiên động lượng của chất điểm trong khoảng thời gian đó:

$$
\vec{J} = \vec{p}_2 - \vec{p}_1
$$

Công thức (8.6).

Động lượng tức thời của chất điểm bằng đúng xung lượng của lực cần thiết để gia tốc chất điểm từ trạng thái nghỉ đến vận tốc hiện tại.



![Diện tích dưới đồ thị lực–thời gian biểu diễn xung lượng](/vat-ly-1/bai-giang/img/young-08/r-theory-tom-tat-2.png)

### Bảo toàn động lượng

Nội lực là lực tương tác giữa các phần tử bên trong hệ. Ngoại lực là lực tác dụng từ môi trường bên ngoài lên các phần tử của hệ.

Tổng động lượng $\vec{P}$ của hệ là tổng vector của tất cả động lượng của các chất điểm riêng lẻ trong hệ:

$$
\vec{P} = \vec{p}_A + \vec{p}_B + \dots = \sum_i \vec{p}_i
$$

**Định luật bảo toàn động lượng**: Nếu tổng ngoại lực tác dụng lên hệ bằng không ($\sum \vec{F}_{\text{ext}} = \vec{0}$), tổng động lượng của hệ được bảo toàn:

$$
\vec{P} = \text{không đổi}
$$

Công thức (8.14).

Mỗi thành phần tọa độ của tổng động lượng $(P_x, P_y, P_z)$ được bảo toàn một cách độc lập.



![Tổng động lượng của hệ hai phi hành gia](/vat-ly-1/bai-giang/img/young-08/r-theory-tom-tat-3.png)

### Phân loại va chạm

Trong mọi quá trình va chạm điển hình giữa các vật thể trong một hệ cô lập, tổng động lượng của hệ trước và sau va chạm luôn bằng nhau:

- **Va chạm đàn hồi (Elastic collision)**: Cả động lượng và tổng động năng của hệ đều được bảo toàn trọn vẹn ($K_1 = K_2$). Độ lớn vận tốc tương đối giữa hai vật sau va chạm bằng độ lớn vận tốc tương đối trước va chạm.
- **Va chạm không đàn hồi (Inelastic collision)**: Động lượng được bảo toàn, nhưng tổng động năng sau va chạm nhỏ hơn tổng động năng ban đầu ($K_2 < K_1$). Phần động năng bị hao hụt chuyển hóa thành nội năng, nhiệt hoặc năng lượng biến dạng của các vật thể.
- **Va chạm hoàn toàn không đàn hồi (Completely inelastic collision)**: Các vật sau va chạm dính liền vào nhau và chuyển động cùng một vận tốc cuối duy nhất.



![Hai chất điểm trước, trong và sau một va chạm đàn hồi](/vat-ly-1/bai-giang/img/young-08/r-theory-tom-tat-4.png)

Trong va chạm đàn hồi một chiều khi vật $B$ ban đầu đứng yên ($v_{B1x} = 0$), các vận tốc sau va chạm được xác định bởi:

$$
v_{A2x} = \frac{m_A - m_B}{m_A + m_B}v_{A1x}
$$

Công thức (8.24).

$$
v_{B2x} = \frac{2m_A}{m_A + m_B}v_{A1x}
$$

Công thức (8.25).

### Khối tâm

Bán kính vector khối tâm $\vec{r}_{\text{cm}}$ của một hệ chất điểm là vị trí trung bình có trọng số theo khối lượng của các chất điểm:

$$
\vec{r}_{\text{cm}} = \frac{\sum_i m_i\vec{r}_i}{\sum_i m_i}
$$

Công thức (8.29).

Các tọa độ thành phần của khối tâm:

$$
x_{\text{cm}} = \frac{\sum_i m_i x_i}{\sum_i m_i}
$$

Công thức (8.28a).

$$
y_{\text{cm}} = \frac{\sum_i m_i y_i}{\sum_i m_i}
$$

Công thức (8.28b).

$$
z_{\text{cm}} = \frac{\sum_i m_i z_i}{\sum_i m_i}
$$

Công thức (8.28c).

Tổng động lượng $\vec{P}$ của hệ liên hệ trực tiếp với vận tốc khối tâm $\vec{v}_{\text{cm}}$ qua tổng khối lượng $M = \sum_i m_i$:

$$
\vec{P} = M\vec{v}_{\text{cm}}
$$

Công thức (8.32).

**Định lý chuyển động khối tâm**: Khối tâm của hệ chuyển động như thể toàn bộ khối lượng $M$ của hệ tập trung tại điểm đó và chịu tác dụng của tổng ngoại lực:

$$
\sum \vec{F}_{\text{ext}} = M\vec{a}_{\text{cm}}
$$

Công thức (8.34).

Nếu tổng ngoại lực triệt tiêu, khối tâm chuyển động thẳng đều hoặc đứng yên với vận tốc $\vec{v}_{\text{cm}} = \text{không đổi}$.



![Khối tâm của các mảnh đạn tiếp tục quỹ đạo ban đầu](/vat-ly-1/bai-giang/img/young-08/r-theory-tom-tat-5.png)

### Chuyển động phản lực của tên lửa

Trong chuyển động phản lực, khối lượng $m$ của tên lửa giảm dần theo thời gian khi nhiên liệu bị đốt cháy và phụt ra phía sau với tốc độ tương đối $v_{\text{ex}}$.

Lực đẩy của động cơ tên lửa là phản lực từ dòng khí phụt ra:

$$
F = -v_{\text{ex}}\frac{dm}{dt}
$$

Công thức (8.38).

Gia tốc tức thời của tên lửa trong không gian phi trọng lực:

$$
a = \frac{dv}{dt} = -\frac{v_{\text{ex}}}{m}\frac{dm}{dt}
$$

Công thức (8.39).

Độ tăng vận tốc của tên lửa theo phương trình Tsiolkovsky phụ thuộc vào tỉ số khối lượng ban đầu $m_0$ và khối lượng còn lại $m$:

$$
\begin{aligned}
v - v_0 &= -v_{\text{ex}}\ln\left(\frac{m}{m_0}\right) \\
&= v_{\text{ex}}\ln\left(\frac{m_0}{m}\right)
\end{aligned}
$$

Công thức (8.40).

![Dòng khí phụt và tên lửa trong cùng hệ quy chiếu](/vat-ly-1/bai-giang/img/young-08/r-theory-tom-tat-6.png)
