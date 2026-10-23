## Tổng kết chương 10

### Mômen lực

Mômen đối với một điểm được xác định bởi vectơ từ điểm đó đến điểm đặt lực và chính lực tác dụng:

$$
\vec\tau=\vec r\times\vec F.
$$

Độ lớn có thể tính từ cánh tay đòn $l$, từ góc $\phi$ giữa hai vectơ hoặc từ thành phần tiếp tuyến:

$$
\tau=Fl=rF\sin\phi=rF_t.
$$

![Tổng kết 10.1: Các cách tính mômen lực đối với cùng một mốc.](./img/young-10/b-tom-tat-10-01.png)

### Động lực học quay

Vật rắn có mômen quán tính $I$ không đổi quanh trục cố định tuân theo:

$$
\sum\tau_{z,\mathrm{ext}}=I\alpha_z.
$$

Mọi mômen trong tổng phải được tính đối với cùng trục và cùng chiều dương. Nội lực không xuất hiện trong tổng mômen ngoại lực.

![Tổng kết 10.2: Ngoại lực tạo mômen làm đổi chuyển động quay của vật rắn.](./img/young-10/b-tom-tat-10-02.png)

### Tịnh tiến kết hợp quay

Động năng của vật rắn được tách thành phần tịnh tiến của khối tâm và phần quay quanh khối tâm:

$$
K=\tfrac12Mv_{\mathrm{cm}}^2+\tfrac12I_{\mathrm{cm}}\omega^2.
$$

Dùng tổng ngoại lực cho chuyển động khối tâm. Khi trục qua khối tâm là trục đối xứng và không đổi phương, dùng tổng mômen quanh trục ấy để tìm gia tốc góc. Với lăn không trượt trên mặt phẳng đứng yên, $v_{\mathrm{cm}}=R\omega$.

![Tổng kết 10.3: Phương trình tịnh tiến, phương trình quay và liên kết không trượt cùng mô tả một chuyển động.](./img/young-10/b-tom-tat-10-03.png)

### Công và công suất

Góc quay phải tính bằng radian. Công của mômen và công suất tức thời:

$$
\begin{aligned}
W&=\int_{\theta_1}^{\theta_2}\tau_z\,d\theta,\\
P&=\tau_z\omega_z.
\end{aligned}
$$

Nếu mômen không đổi, $W=\tau_z\Delta\theta$. Công của tổng mômen bằng độ biến thiên động năng quay khi dùng cùng trục và mômen quán tính không đổi.

![Tổng kết 10.4: Mômen lực truyền năng lượng qua góc quay và tạo công suất khi vật đang quay.](./img/young-10/b-tom-tat-10-04.png)

### Mômen động lượng và bảo toàn

Với chất điểm, $\vec L=\vec r\times\vec p$. Với vật rắn quay quanh trục đối xứng, $\vec L=I\vec\omega$. Nếu trục không đối xứng, chỉ dùng $L_z=I\omega_z$ cho thành phần theo trục, không tự coi hai vectơ cùng phương.

Phương trình tổng quát đối với cùng một mốc thích hợp:

$$
\sum\vec\tau_{\mathrm{ext}}=\frac{d\vec L}{dt}.
$$

Tổng mômen ngoại lực bằng không cho bảo toàn mômen động lượng. Từng phần của hệ vẫn có thể trao đổi mômen động lượng với nhau. Động năng không nhất thiết bảo toàn khi hệ đổi hình hoặc khi hai vật ma sát ghép với nhau.

![Tổng kết 10.5: Mômen động lượng nối chuyển động của chất điểm với chuyển động quay của vật rắn.](./img/young-10/b-tom-tat-10-05.png)

![Tổng kết 10.6: Thu tay làm mômen quán tính giảm và vận tốc góc tăng khi mômen động lượng được bảo toàn.](./img/young-10/b-tom-tat-10-06.png)

### Tiến động chậm

Với bánh đà quay nhanh, mômen trọng lực có thể làm trục đổi hướng thay vì đổ xuống như bánh không tự quay. Ở tiến động đều, trục nằm ngang và $\Omega\ll\omega$:

$$
\Omega=\frac{mgr}{I\omega}.
$$

Phải phân biệt tốc độ tiến động $\Omega$ với tốc độ tự quay $\omega$. Khi không còn điều kiện tiến động chậm, cần xét thêm mômen động lượng của chuyển động tiến động và có thể xuất hiện chương động.
