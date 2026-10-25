## Bài tập cầu nối

### Bài tập cầu nối: Tháo cạn một bồn nước mất bao lâu?

Một bồn hình trụ lớn có đường kính $D$, miệng trên hở ra không khí và chứa nước đến độ cao ban đầu $H$. Mở một lỗ tròn nhỏ có đường kính $d$ ở đáy, với $d\ll D$, như Hình 12.32. Bỏ qua mọi tác dụng của độ nhớt.

- (a) Tìm độ cao nước $y$ trong bồn theo thời gian $t$ sau khi mở lỗ.
- (b) Bao lâu thì bồn cạn hoàn toàn?
- (c) Nếu tăng gấp đôi độ cao ban đầu $H$, thời gian tháo cạn tăng bao nhiêu lần?

![Hình 12.32: Bồn trụ có đường kính D, lỗ đáy có đường kính d. Nước ban đầu cao H và còn cao y ở thời điểm t, cả mặt thoáng và đầu ra cùng tiếp xúc khí quyển.](/vat-ly-1/bai-giang/img/young-12/r-exercises-fig-12-32.png)

Gợi ý triển khai bài toán:

1. Vẽ phác tình huống và ghi đủ những kích thước liên quan.
2. Liệt kê các đại lượng chưa biết, rồi xác định những đại lượng cần tìm.
3. Nước ra khỏi đáy với tốc độ bao nhiêu? Tốc độ ấy liên hệ thế nào với lưu lượng ra và tốc độ thay đổi của $y$?
4. Từ các quan hệ trên, lập một phương trình cho $dy/dt$.
5. Tích phân phương trình vi phân để tìm $y(t)$. Sau khi tích phân, còn cần biến đổi đại số để đưa về dạng độ cao theo thời gian.
6. Dùng kết quả để tìm thời điểm bồn cạn và xem nó phụ thuộc độ cao ban đầu $H$ ra sao.
7. Kiểm tra tính hợp lý bằng đồ thị $y$ theo $t$. Dấu của $dy/dt$ ở những thời điểm khác nhau có phù hợp việc nước chảy ra không?

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài**

Hai tiết diện cố định là diện tích mặt cắt bồn $A$ và diện tích lỗ $a$:

$$
\begin{aligned}
&A=\frac{\pi D^2}{4},\\
&a=\frac{\pi d^2}{4}.
\end{aligned}
$$

Đặt $\alpha=a/A=(d/D)^2$. Ban đầu $y(0)=H$. Cần tìm $y(t)$, thời gian cạn $T$ và tỷ số thời gian khi $H$ tăng gấp đôi.

**Hướng đi:**

- Dùng Bernoulli giữa mặt thoáng và lỗ ra. Hai nơi cùng chịu khí áp, còn tiết diện bồn lớn hơn lỗ nhiều nên tốc độ mặt thoáng nhỏ. Trong mô hình gần ổn định, định luật Torricelli cho tốc độ ra phụ thuộc độ cao nước tức thời.
- Dùng bảo toàn thể tích để liên hệ lưu lượng ra với độ giảm thể tích trong bồn. Dấu âm cần giữ vì $y$ giảm trong khi lưu lượng chảy ra được lấy dương.
- Giải phương trình vi phân tách biến với điều kiện ban đầu $y(0)=H$. Chỉ lấy nhánh có $\sqrt y\ge0$, không kéo dài đa thức sau khi bồn đã cạn.
- Dùng $y(T)=0$ để tìm thời gian, rồi so sánh khi thay $H$ bằng $2H$.

**Lời giải**

(a) Hình 12.32 cho sơ đồ và các kích thước cần dùng. Chọn mốc cao độ tại lỗ đáy, nên mặt thoáng ở cao độ $y$ và miệng ra ở cao độ không. Gọi tốc độ chảy ra là $v$.

Bỏ qua tốc độ mặt thoáng so với tốc độ lỗ ra, Bernoulli cho

$$
p_a+\rho gy=p_a+\frac12\rho v^2.
$$

Khử khí áp và khối lượng riêng, chọn tốc độ ra không âm:

$$
v=\sqrt{2gy}.
$$

Lưu lượng ra tại thời điểm ấy là

$$
Q=av=a\sqrt{2gy}.
$$

Thể tích nước còn trong bồn bằng $Ay$. Tốc độ giảm thể tích bằng lưu lượng chảy ra:

$$
-A\frac{dy}{dt}=a\sqrt{2gy}.
$$

Vì thế,

$$
\frac{dy}{dt}=-\alpha\sqrt{2g}\sqrt y.
$$

Phương trình này cho ngay $dy/dt<0$ khi $y>0$. Trong giai đoạn còn nước, tách biến:

$$
\frac{dy}{\sqrt y}=-\alpha\sqrt{2g}\,dt.
$$

Tích phân từ $y=H$ lúc $t=0$ đến $y$ lúc $t$:

$$
\int_H^y\frac{du}{\sqrt u}=-\alpha\sqrt{2g}\int_0^t d\tau.
$$

Ta được

$$
2\sqrt y-2\sqrt H=-\alpha\sqrt{2g}\,t.
$$

Chuyển vế và chia hai:

$$
\sqrt y=\sqrt H-\alpha\sqrt{\frac g2}\,t.
$$

Vế trái không âm, nên biểu thức bên phải cũng phải không âm. Trong miền thời gian thỏa điều kiện ấy,

$$
y(t)=\left(\sqrt H-\alpha\sqrt{\frac g2}\,t\right)^2.
$$

Trong biểu thức này, $\alpha=(d/D)^2$, nên kết quả xác định đầy đủ $y$ theo $D$, $d$, $H$, $g$ và $t$.

(b) Bồn cạn khi $y=0$, tức

$$
\sqrt H-\alpha\sqrt{\frac g2}\,T=0.
$$

Suy ra

$$
\begin{aligned}
T&=\frac1\alpha\sqrt{\frac{2H}{g}}\\
&=\left(\frac Dd\right)^2\sqrt{\frac{2H}{g}}.
\end{aligned}
$$

Từ đó, cách viết gọn cho độ cao nước là

$$
y(t)=H\left(1-\frac tT\right)^2.
$$

Khai triển dạng không thứ nguyên của cùng kết quả:

$$
\frac{y(t)}{H}=1-2\frac tT+\left(\frac tT\right)^2.
$$

Hai dạng này đều áp dụng trong miền $0\le t\le T$. Sau thời điểm $T$, bồn đã hết nước, nên mô hình vật lý cho $y=0$. Không dùng tiếp đa thức bình phương để suy rằng mực nước tự tăng trở lại khi $t>T$.

(c) Với đường kính bồn và lỗ giữ nguyên, thời gian cạn tỷ lệ với căn bậc hai độ cao ban đầu:

$$
T\propto\sqrt H.
$$

Vì thế,

$$
\frac{T(2H)}{T(H)}=\sqrt2.
$$

Thời gian tăng $\sqrt2$ lần. Lượng nước tăng gấp đôi nhưng độ cao lớn hơn cũng làm tốc độ chảy ban đầu lớn hơn, nên thời gian không tăng gấp đôi.

![Đồ thị lời giải: Độ cao nước giảm từ H đến không trong khoảng từ 0 đến T. Đường cong có độ dốc âm khi còn nước và tiến tới tiếp tuyến ngang tại lúc cạn trong mô hình lý tưởng.](/vat-ly-1/bai-giang/img/young-12/bridge-12-water-height-solution.svg)

Đồ thị chỉ biểu diễn giai đoạn $0\le t\le T$. Đạo hàm trong giai đoạn đó là

$$
\frac{dy}{dt}=-\frac{2H}{T}\left(1-\frac tT\right).
$$

Mực nước giảm nhanh nhất lúc đầu, rồi chậm dần vì cột nước tạo dòng ra thấp đi. Độ dốc tiến tới không khi $t$ tiến đến $T$ từ bên trái. Sau khi bồn cạn, độ cao giữ ở không và đạo hàm cũng bằng không.

Các kết quả có đơn vị phù hợp. Đại lượng $\sqrt{H/g}$ có đơn vị thời gian, còn tỷ số $D/d$ không có đơn vị. Lỗ nhỏ hơn làm thời gian tăng theo $1/d^2$, đúng với việc diện tích thoát nước giảm. Đây là kết quả của mô hình bỏ nhớt, lỗ nhỏ và dòng gần ổn định, không phải thời gian tháo thực tế có mọi tổn thất.

</details>
