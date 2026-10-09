<!-- Nguồn: Summary, trang in 56, trang PDF 76. -->

## Tóm tắt chương 2 trong sách

### Chuyển động thẳng và vận tốc trung bình, vận tốc tức thời

Khi chất điểm chuyển động trên đường thẳng, ta mô tả vị trí của nó so với gốc $O$ bằng một tọa độ, chẳng hạn $x$. Vận tốc trung bình theo trục $x$ trong khoảng thời gian $\Delta t=t_2-t_1$ bằng độ dời $\Delta x=x_2-x_1$ chia cho khoảng thời gian ấy. Vận tốc tức thời tại thời điểm $t$ là giới hạn của vận tốc trung bình trên khoảng từ $t$ đến $t+\Delta t$ khi $\Delta t$ tiến tới không. Tương đương, nó là đạo hàm của hàm vị trí theo thời gian. Xem Ví dụ 2.1.

$$v_{\mathrm{av}-x}=\frac{\Delta x}{\Delta t}=\frac{x_2-x_1}{t_2-t_1}.\qquad\text{(2.2)}$$

$$v_x=\lim_{\Delta t\to0}\frac{\Delta x}{\Delta t}=\frac{dx}{dt}.\qquad\text{(2.3)}$$

![Minh họa tóm tắt: trên đồ thị vị trí theo thời gian, độ dốc dây cung là vận tốc trung bình và độ dốc tiếp tuyến là vận tốc tức thời](img/young-02/tom-tat-van-toc.png)

Trong hình, hai điểm có tọa độ $(t_1,x_1)$ và $(t_2,x_2)$. Nhãn “Slope” chỉ độ dốc: dây cung có độ dốc $v_{\mathrm{av}-x}$, còn tiếp tuyến có độ dốc $v_x$.

### Gia tốc trung bình và gia tốc tức thời

Gia tốc trung bình theo trục $x$ trong khoảng $\Delta t$ bằng độ biến thiên vận tốc $\Delta v_x=v_{2x}-v_{1x}$ chia cho khoảng thời gian ấy. Gia tốc tức thời là giới hạn của gia tốc trung bình khi $\Delta t$ tiến tới không, hay đạo hàm của $v_x$ theo $t$. Xem Ví dụ 2.2 và 2.3.

$$a_{\mathrm{av}-x}=\frac{\Delta v_x}{\Delta t}=\frac{v_{2x}-v_{1x}}{t_2-t_1}.\qquad\text{(2.4)}$$

$$a_x=\lim_{\Delta t\to0}\frac{\Delta v_x}{\Delta t}=\frac{dv_x}{dt}.\qquad\text{(2.5)}$$

![Minh họa tóm tắt: độ dốc dây cung của đồ thị vận tốc là gia tốc trung bình, còn độ dốc tiếp tuyến là gia tốc tức thời](img/young-02/tom-tat-gia-toc.png)

Hai đầu khoảng là $(t_1,v_{1x})$ và $(t_2,v_{2x})$, với $\Delta v_x=v_{2x}-v_{1x}$. Các nhãn độ dốc lần lượt chỉ $a_{\mathrm{av}-x}$ và $a_x$.

### Chuyển động thẳng với gia tốc không đổi

Khi $a_x$ không đổi, bốn phương trình liên hệ vị trí $x$ và vận tốc $v_x$ tại thời điểm $t$ với vị trí đầu $x_0$, vận tốc đầu $v_{0x}$ ở $t=0$, cùng gia tốc $a_x$. Xem Ví dụ 2.4 và 2.5. Các phương trình sau **chỉ dùng khi gia tốc theo trục $x$ không đổi**:

$$v_x=v_{0x}+a_xt.\qquad\text{(2.8)}$$

$$x=x_0+v_{0x}t+\frac12a_xt^2.\qquad\text{(2.12)}$$

$$v_x^2=v_{0x}^2+2a_x(x-x_0).\qquad\text{(2.13)}$$

$$x-x_0=\frac12(v_{0x}+v_x)t.\qquad\text{(2.14)}$$

![Minh họa tóm tắt: tại các thời điểm cách đều, gia tốc không đổi còn vận tốc và khoảng cách giữa các vị trí tăng dần](img/young-02/tom-tat-gia-toc-khong-doi.png)

Các hàng ứng với $t=0,\Delta t,2\Delta t,3\Delta t,4\Delta t$. Mũi tên $\vec v$ chỉ vận tốc, $\vec a$ chỉ gia tốc và $x$ chỉ trục chuyển động.

### Vật rơi tự do

Rơi tự do là chuyển động thẳng đứng không có lực cản không khí, nên chỉ trọng lực tác dụng lên chuyển động. Đây là một trường hợp chuyển động với gia tốc không đổi. Độ lớn gia tốc trọng trường là đại lượng dương $g$, còn vector gia tốc luôn hướng xuống. Nếu chọn chiều $+y$ hướng lên thì:

$$a_y=-g=-9.80\,\mathrm{m/s^2}.$$

Xem Ví dụ 2.6–2.8.

![Minh họa tóm tắt: vật đi lên rồi đi xuống với gia tốc trọng trường luôn hướng xuống](img/young-02/tom-tat-roi-tu-do.png)

Mũi tên gia tốc hướng xuống ở cả hai nhánh chuyển động, với $a_y=-g$ khi trục $+y$ hướng lên.

### Chuyển động thẳng với gia tốc biến thiên

Nếu gia tốc không cố định nhưng đã biết dưới dạng hàm thời gian, ta tìm vận tốc và vị trí bằng cách tích phân hàm gia tốc. Xem Ví dụ 2.9.

$$v_x=v_{0x}+\int_0^t a_x\,dt.\qquad\text{(2.17)}$$

$$x=x_0+\int_0^t v_x\,dt.\qquad\text{(2.18)}$$

![Minh họa tóm tắt: dải diện tích dưới đồ thị gia tốc theo thời gian](img/young-02/tom-tat-tich-phan.png)

Trục đứng là $a_x$, trục ngang là $t$. Dải rộng $\Delta t$ nằm giữa $t_1$ và $t_2$, với gia tốc trung bình $a_{\mathrm{av}-x}$, biểu diễn phần biến thiên vận tốc trên khoảng nhỏ.
