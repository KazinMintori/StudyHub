## Tổng kết chương 2

### Chuyển động thẳng và vận tốc

Vị trí của chất điểm trên đường thẳng được xác định bằng tọa độ x so với gốc O. Trong khoảng thời gian từ $t_1$ đến $t_2$, độ dời bằng tọa độ cuối trừ tọa độ đầu. Vận tốc trung bình theo trục x là độ dời chia cho khoảng thời gian, như công thức (2.2):

$$
v_{\mathrm{av}-x}=\frac{\Delta x}{\Delta t}.
$$

Trong đó:

$$
\Delta x=x_2-x_1.
$$

$$
\Delta t=t_2-t_1>0.
$$

Vận tốc tức thời là giới hạn của vận tốc trung bình khi khoảng thời gian tiến tới không. Khi đạo hàm tồn tại, công thức (2.3) có hai cách viết tương đương:

$$
v_x=\lim_{\Delta t\to0}\frac{\Delta x}{\Delta t},
$$

$$
v_x=\frac{dx}{dt}.
$$

Trên đồ thị tọa độ theo thời gian, độ dốc cát tuyến cho vận tốc trung bình, còn độ dốc tiếp tuyến cho vận tốc tức thời. Tốc độ tức thời là độ lớn của vận tốc và không âm. Ví dụ 2.1 minh họa sự khác nhau giữa vận tốc trung bình và vận tốc tức thời.

![Hình 2.S1: Cát tuyến và tiếp tuyến trên đồ thị tọa độ theo thời gian](img/young-02/tom-tat-van-toc.png)

### Gia tốc trung bình và gia tốc tức thời

Gia tốc trung bình theo trục x bằng độ biến thiên vận tốc chia cho khoảng thời gian. Theo công thức (2.4):

$$
a_{\mathrm{av}-x}=\frac{\Delta v_x}{\Delta t}.
$$

Ở đây:

$$
\Delta v_x=v_{2x}-v_{1x}.
$$

Gia tốc tức thời là giới hạn của gia tốc trung bình khi khoảng thời gian tiến tới không. Theo công thức (2.5):

$$
a_x=\lim_{\Delta t\to0}\frac{\Delta v_x}{\Delta t},
$$

$$
a_x=\frac{dv_x}{dt}.
$$

Trên đồ thị vận tốc theo thời gian, gia tốc trung bình bằng độ dốc cát tuyến, còn gia tốc tức thời bằng độ dốc tiếp tuyến. Khi vận tốc và gia tốc cùng dấu, tốc độ tăng. Khi chúng trái dấu, tốc độ giảm. Ví dụ 2.2 và Ví dụ 2.3 trình bày cách tính hai loại gia tốc này.

![Hình 2.S2: Gia tốc trung bình và gia tốc tức thời trên đồ thị vận tốc theo thời gian](img/young-02/tom-tat-gia-toc.png)

### Chuyển động thẳng với gia tốc không đổi

Khi gia tốc theo trục x không đổi trên toàn khoảng xét, bốn phương trình liên hệ tọa độ và vận tốc tại thời điểm t với điều kiện ban đầu tại t = 0. Công thức (2.8) cho vận tốc:

$$
v_x=v_{0x}+a_xt.
$$

Công thức (2.12) cho tọa độ:

$$
x=x_0+v_{0x}t+\frac12a_xt^2.
$$

Công thức (2.13) liên hệ vận tốc với độ dời mà không chứa thời gian:

$$
v_x^2=v_{0x}^2+2a_x(x-x_0).
$$

Công thức (2.14) liên hệ độ dời với vận tốc đầu, vận tốc cuối và thời gian:

$$
x-x_0=\frac12(v_{0x}+v_x)t.
$$

Các công thức này được áp dụng trong Ví dụ 2.4 và Ví dụ 2.5. Phải xác định điều kiện gia tốc không đổi trước khi dùng chúng để mô tả cả khoảng chuyển động.

![Hình 2.S3: Gia tốc không đổi làm vận tốc biến thiên những lượng bằng nhau trong các khoảng thời gian bằng nhau](img/young-02/tom-tat-gia-toc-khong-doi.png)

### Vật rơi tự do

Rơi tự do theo phương thẳng đứng, khi bỏ qua lực cản không khí và chỉ có trọng lực tác dụng, là một trường hợp chuyển động có gia tốc không đổi gần mặt đất. Độ lớn gia tốc trọng trường g là số dương. Vector gia tốc luôn hướng xuống.

Chọn chiều dương của trục y hướng lên:

$$
a_y=-g,\qquad g\approx9{,}80\,\mathrm{m/s^2}.
$$

Gia tốc vẫn hướng xuống khi vật đang bay lên, tại đỉnh và khi vật đi xuống. Ví dụ 2.6–2.8 trình bày các bài toán rơi tự do với những điều kiện ban đầu khác nhau.

![Hình 2.S4: Gia tốc trọng trường hướng xuống trong cả nhánh đi lên và nhánh đi xuống](img/young-02/tom-tat-roi-tu-do.png)

### Chuyển động với gia tốc biến thiên

Nếu gia tốc là hàm đã biết của thời gian, có thể tìm vận tốc bằng tích phân gia tốc và dùng vận tốc để tìm tọa độ. Với vận tốc đầu và tọa độ đầu tại t = 0, công thức (2.17) là:

$$
v_x(t)=v_{0x}+\int_0^t a_x(u)\,du.
$$

Công thức (2.18) là:

$$
x(t)=x_0+\int_0^t v_x(u)\,du.
$$

Biến u là biến lấy tích phân. Diện tích có dấu dưới đồ thị gia tốc theo thời gian cho độ biến thiên vận tốc. Diện tích có dấu dưới đồ thị vận tốc theo thời gian cho độ dời. Cần biết điều kiện ban đầu để xác định vận tốc và tọa độ, như trong Ví dụ 2.9.

![Hình 2.S5: Diện tích có dấu dưới đồ thị gia tốc theo thời gian biểu diễn độ biến thiên vận tốc](img/young-02/tom-tat-tich-phan.png)
