## Vận tốc góc và gia tốc góc

Khi phân tích chuyển động quay, trước tiên chúng ta xét một vật rắn quay quanh một trục cố định. Trục quay này đứng yên trong một hệ quy chiếu quán tính và không đổi phương chiều so với hệ quy chiếu đó. Vật rắn quay quanh trục cố định có thể là trục động cơ, miếng thịt nướng trên xiên quay hoặc vòng quay ngựa gỗ trong công viên.

![Hình 9.1: Kim đồng hồ tốc độ (ví dụ về một vật rắn) quay ngược chiều kim đồng hồ quanh một trục cố định vuông góc với mặt phẳng hình vẽ tại điểm O.](../img/young-09/a-hinh-9-01.png)

Hình 9.1 mô tả một vật rắn đang quay quanh một trục cố định. Trục quay đi qua gốc tọa độ $O$ và vuông góc với mặt phẳng hình vẽ (chúng ta gọi đây là mặt phẳng $xy$). Một cách để mô tả chuyển động quay của vật thể là chọn một điểm $P$ cụ thể trên vật rồi theo dõi tọa độ $x$ và $y$ của điểm đó. Tuy nhiên, cách làm này không thuận tiện vì đòi hỏi hai đại lượng tọa độ để xác định vị trí của vật.

Thay vào đó, chúng ta nhận thấy đoạn thẳng nối từ gốc $O$ đến điểm $P$ gắn cố định vào vật rắn và quay cùng với vật. Góc $\theta$ hợp bởi đoạn thẳng $OP$ với chiều dương trục $x$ chính là một **tọa độ góc** (angular coordinate) duy nhất xác định trọn vẹn vị trí quay của vật rắn tại mỗi thời điểm.

Tọa độ góc $\theta$ của vật rắn quay quanh trục cố định có thể nhận giá trị dương hoặc âm. Nếu chúng ta quy ước chiều quay ngược chiều kim đồng hồ là chiều dương, khi đó góc $\theta$ trên Hình 9.1 mang dấu dương. Nếu quy ước ngược lại, góc $\theta$ sẽ mang dấu âm. Tương tự như khi khảo sát chuyển động thẳng cần xác định chiều dương của trục tọa độ, việc xác định chiều quay dương quanh trục cố định là điều kiện bắt buộc trước khi tính toán.

### Phép đo góc theo đơn vị radian

Phương thức tự nhiên và chuẩn mực nhất để đo góc $\theta$ trong cơ học không phải là độ ($^\circ$), mà là đơn vị radian ($\text{rad}$).

![Hình 9.2: Định nghĩa và phép đo góc theo đơn vị radian.](../img/young-09/a-hinh-9-02.png)

Như minh họa trên Hình 9.2a, một radian ($1\text{ rad}$) là góc ở tâm chắn một cung tròn có độ dài đúng bằng bán kính của đường tròn đó. Trên Hình 9.2b, góc $\theta$ chắn một cung có độ dài $s$ trên đường tròn bán kính $r$. Khi đó, giá trị của góc $\theta$ (tính theo radian) bằng thương số giữa độ dài cung $s$ và bán kính $r$:
$$
\theta = \frac{s}{r} \iff s = r\theta
\tag{9.1}
$$
trong đó góc $\theta$ bắt buộc phải tính bằng radian.

Vì góc tính theo radian là tỉ số giữa hai đại lượng có cùng thứ nguyên chiều dài, nó là một đại lượng không thứ nguyên (số thuần túy). Nếu độ dài cung $s = 3{,}0\text{ m}$ và bán kính $r = 2{,}0\text{ m}$, ta có $\theta = 1{,}5$. Dù vậy, chúng ta vẫn thường viết kèm đơn vị là $1{,}5\text{ rad}$ để phân biệt rõ ràng với góc đo bằng độ hay số vòng quay.

Chu vi của một đường tròn bằng $2\pi$ nhân với bán kính. Do đó, một vòng quay trọn vẹn ($360^\circ$) tương ứng với $2\pi\text{ rad}$ (xấp xỉ $6{,}283\text{ rad}$). Từ đó suy ra hệ thức đổi đơn vị:
$$
1\text{ rad} = \frac{360^\circ}{2\pi} \approx 57{,}3^\circ
$$

Tương tự, ta có $180^\circ = \pi\text{ rad}$, $90^\circ = \pi/2\text{ rad}$, $60^\circ = \pi/3\text{ rad}$, $45^\circ = \pi/4\text{ rad}$. Nếu đo góc $\theta$ bằng đơn vị độ, vế phải của phương trình $s = r\theta$ sẽ phải nhân thêm thừa số đổi $(2\pi/360)$. Việc sử dụng đơn vị radian giúp phương trình liên hệ giữa góc và độ dài cung giữ được dạng thức gọn gàng nhất.

### Vận tốc góc

Tọa độ $\theta$ trên Hình 9.1 xác định vị trí góc của vật rắn tại một thời điểm cho trước. Chúng ta mô tả chuyển động quay của vật thông qua tốc độ biến thiên của $\theta$ theo thời gian, hoàn toàn tương tự như cách mô tả chuyển động thẳng.

![Hình 9.3: (a) Độ dời góc $\Delta\theta$ của vật rắn trong khoảng thời gian $\Delta t$. (b) Mọi điểm trên vật rắn đều quay cùng một góc trong cùng thời gian.](../img/young-09/a-hinh-9-03.png)

Trên Hình 9.3a, một đoạn chuẩn $OP$ trên vật rắn quay hợp với trục $+x$ một góc $\theta_1$ tại thời điểm $t_1$. Ở thời điểm $t_2$ muộn hơn, góc này đã thay đổi thành $\theta_2$. Chúng ta định nghĩa **vận tốc góc trung bình** $\omega_{\text{av-}z}$ (ký hiệu bằng chữ cái Hy Lạp omega $\omega$) của vật rắn trong khoảng thời gian $\Delta t = t_2 - t_1$ là tỉ số giữa độ dời góc $\Delta\theta = \theta_2 - \theta_1$ và $\Delta t$:
$$
\omega_{\text{av-}z} = \frac{\theta_2 - \theta_1}{t_2 - t_1} = \frac{\Delta\theta}{\Delta t}
\tag{9.2}
$$

Chỉ số dưới $z$ chỉ rõ rằng vật thể đang quay quanh trục $z$ vuông góc với mặt phẳng hình vẽ. **Vận tốc góc tức thời** $\omega_z$ là giới hạn của vận tốc góc trung bình khi khoảng thời gian $\Delta t$ dần tới không:
$$
\omega_z = \lim_{\Delta t \to 0} \frac{\Delta\theta}{\Delta t} = \frac{d\theta}{dt}
\tag{9.3}
$$

Khi dùng thuật ngữ "vận tốc góc", chúng ta luôn ngầm hiểu đó là vận tốc góc tức thời.

![Hình 9.4: Dấu của vận tốc góc trung bình và tức thời phụ thuộc vào chiều quay của vật rắn.](../img/young-09/a-hinh-9-04.png)

Vận tốc góc $\omega_z$ có thể nhận giá trị dương hoặc âm tùy thuộc vào chiều quay của vật rắn (Hình 9.4). **Tốc độ góc** $\omega$ là độ lớn của vận tốc góc ($\omega = |\omega_z|$). Tương tự như tốc độ dài $v$, tốc độ góc $\omega$ không bao giờ âm.

::: warning Lưu ý: Phân biệt vận tốc góc và vận tốc dài
Cần phân biệt rành mạch giữa vận tốc góc $\omega_z$ và vận tốc dài $v_x$. Nếu một vật có vận tốc dài $v_x$, toàn bộ vật thể đang tịnh tiến dọc theo trục $x$. Ngược lại, nếu vật có vận tốc góc $\omega_z$, vật thể đang quay quanh trục $z$ chứ không phải đang chuyển động tịnh tiến dọc theo trục $z$.
:::

Các điểm khác nhau trên một vật rắn chuyển động được những quãng đường khác nhau trong cùng một khoảng thời gian, tùy thuộc vào khoảng cách từ điểm đó tới trục quay. Tuy nhiên, vì vật thể là vật rắn lý tưởng, mọi điểm trên vật đều quay được cùng một góc trong cùng một khoảng thời gian (Hình 9.3b). Do đó, tại mỗi thời điểm xác định, mọi thành phần cấu tạo nên vật rắn đều có cùng một vận tốc góc.

Nếu góc $\theta$ đo bằng radian, đơn vị của vận tốc góc là radian trên giây ($\text{rad/s}$). Các đơn vị khác cũng thường gặp trong thực tế kỹ thuật là vòng trên giây ($\text{rev/s}$) và vòng trên phút ($\text{rev/min}$ hay $\text{rpm}$). Vì một vòng tương ứng với $2\pi\text{ rad}$, hai hệ thức quy đổi thông dụng là:
$$
1\text{ rev/s} = 2\pi\text{ rad/s}
$$
$$
\begin{aligned}
1\text{ rpm} &= \frac{2\pi}{60}\text{ rad/s} \\
&= \frac{\pi}{30}\text{ rad/s}
\end{aligned}
$$
Như vậy, tốc độ góc $1\text{ rad/s}$ tương đương với khoảng $9{,}55\text{ rpm}$ (khoảng $10\text{ rpm}$).

::: example Ví dụ 9.1: Tính toán vận tốc góc của bánh đà
**Bài toán**: Vị trí góc $\theta$ của một bánh đà đường kính $0{,}36\text{ m}$ biến thiên theo thời gian theo quy luật:
$$
\theta = (2{,}0\text{ rad/s}^3)t^3
$$

(a) Xác định giá trị $\theta$ theo đơn vị radian và theo độ tại hai thời điểm $t_1 = 2{,}0\text{ s}$ và $t_2 = 5{,}0\text{ s}$.

(b) Tính quãng đường một hạt nằm trên vành ngoài của bánh đà đi được trong khoảng thời gian từ $t_1 = 2{,}0\text{ s}$ đến $t_2 = 5{,}0\text{ s}$.

(c) Tính vận tốc góc trung bình trong khoảng thời gian đó theo đơn vị $\text{rad/s}$ và $\text{rev/min}$.

(d) Xác định vận tốc góc tức thời tại hai thời điểm $t_1 = 2{,}0\text{ s}$ và $t_2 = 5{,}0\text{ s}$.

**Tóm tắt**:
- Đường kính bánh đà: $d = 0{,}36\text{ m}$, suy ra bán kính $r = 0{,}18\text{ m}$.
- Phương trình góc: $\theta(t) = (2{,}0\text{ rad/s}^3)t^3$.
- Thời điểm: $t_1 = 2{,}0\text{ s}$, $t_2 = 5{,}0\text{ s}$.

**Hướng đi**:
- Ở câu (a), thay trực tiếp giá trị thời gian vào hàm $\theta(t)$, sau đó dùng tỉ số $360^\circ/(2\pi\text{ rad})$ để đổi ra độ.
- Ở câu (b), tính độ dời góc $\Delta\theta = \theta_2 - \theta_1$ rồi áp dụng hệ thức cung tròn $s = r\Delta\theta$ với góc bắt buộc tính theo radian.
- Ở câu (c), dùng định nghĩa vận tốc góc trung bình $\omega_{\text{av-}z} = \Delta\theta/\Delta t$, sau đó đổi đơn vị sang vòng trên phút.
- Ở câu (d), lấy đạo hàm bậc nhất của hàm vị trí góc theo thời gian để nhận được hàm vận tốc góc tức thời $\omega_z(t) = d\theta/dt$, rồi thay thời điểm $t_1, t_2$.

**Lời giải**:

(a) Thay các mốc thời gian vào biểu thức của $\theta$:
$$
\begin{aligned}
\theta_1 &= (2{,}0\text{ rad/s}^3)(2{,}0\text{ s})^3 \\
&= 16\text{ rad}
\end{aligned}
$$
$$
\begin{aligned}
\theta_1 &= 16\text{ rad} \cdot \frac{360^\circ}{2\pi\text{ rad}} \\
&\approx 920^\circ
\end{aligned}
$$
$$
\begin{aligned}
\theta_2 &= (2{,}0\text{ rad/s}^3)(5{,}0\text{ s})^3 \\
&= 250\text{ rad}
\end{aligned}
$$
$$
\begin{aligned}
\theta_2 &= 250\text{ rad} \cdot \frac{360^\circ}{2\pi\text{ rad}} \\
&\approx 14\,000^\circ
\end{aligned}
$$

(b) Trong khoảng thời gian từ $t_1$ đến $t_2$, độ dời góc của bánh đà là:
$$
\begin{aligned}
\Delta\theta &= \theta_2 - \theta_1 \\
&= 250\text{ rad} - 16\text{ rad} \\
&= 234\text{ rad}
\end{aligned}
$$

Bán kính bánh đà bằng một nửa đường kính: $r = 0{,}18\text{ m}$. Áp dụng phương trình (9.1) với góc đo bằng radian:
$$
\begin{aligned}
s &= r\Delta\theta \\
&= (0{,}18\text{ m})(234\text{ rad}) \\
&\approx 42\text{ m}
\end{aligned}
$$
Chúng ta có thể lược bỏ đơn vị radian trong kết quả của $s$ vì radian là đại lượng không thứ nguyên.

(c) Từ phương trình (9.2), vận tốc góc trung bình là:
$$
\begin{aligned}
\omega_{\text{av-}z} &= \frac{250\text{ rad} - 16\text{ rad}}{5{,}0\text{ s} - 2{,}0\text{ s}} \\
&= 78\text{ rad/s}
\end{aligned}
$$

Đổi sang đơn vị vòng trên phút ($\text{rev/min}$):
$$
\begin{aligned}
\omega_{\text{av-}z} &= 78 \cdot \frac{60}{2\pi}\text{ rev/min} \\
&\approx 740\text{ rev/min}
\end{aligned}
$$

(d) Lấy đạo hàm của tọa độ góc theo thời gian:
$$
\begin{aligned}
\omega_z &= \frac{d\theta}{dt} \\
&= \frac{d}{dt}\left[(2{,}0\text{ rad/s}^3)t^3\right] \\
&= (6{,}0\text{ rad/s}^3)t^2
\end{aligned}
$$

Tại hai thời điểm $t_1 = 2{,}0\text{ s}$ và $t_2 = 5{,}0\text{ s}$, ta nhận được:
$$
\begin{aligned}
\omega_{1z} &= (6{,}0\text{ rad/s}^3)(2{,}0\text{ s})^2 \\
&= 24\text{ rad/s}
\end{aligned}
$$
$$
\begin{aligned}
\omega_{2z} &= (6{,}0\text{ rad/s}^3)(5{,}0\text{ s})^2 \\
&= 150\text{ rad/s}
\end{aligned}
$$

**Đánh giá**:
Vận tốc góc tức thời $\omega_z = (6{,}0\text{ rad/s}^3)t^2$ tăng liên tục theo thời gian. Giá trị cuối khoảng là $150\text{ rad/s}$, lớn hơn giá trị đầu khoảng $24\text{ rad/s}$. Vận tốc góc trung bình $78\text{ rad/s}$ nằm giữa hai giá trị này.

**Trọng tâm tư duy**:
Để tìm vận tốc góc trung bình của vật rắn quay, trước hết hãy xác định độ dời góc trong khoảng thời gian rồi chia cho khoảng thời gian đó. Để tìm vận tốc góc tức thời, hãy lấy đạo hàm bậc nhất của hàm vị trí góc theo thời gian.
:::

### Vận tốc góc dưới dạng vectơ

Ký hiệu vận tốc góc $\omega_z$ quanh trục $z$ tương đồng với ký hiệu vận tốc $v_x$ trong chuyển động thẳng dọc theo trục $x$. Giống như $v_x$ là thành phần đại số của vectơ vận tốc $\vec{v}$, $\omega_z$ là thành phần theo trục $z$ của **vectơ vận tốc góc** $\vec{\omega}$ hướng dọc theo trục quay.

![Hình 9.5: (a) Quy tắc bàn tay phải xác định chiều của vectơ vận tốc góc $\vec{\omega}$. Đảo chiều quay sẽ đảo chiều của $\vec{\omega}$. (b) Dấu của thành phần $\omega_z$ khi quay quanh trục $z$.](../img/young-09/a-hinh-9-05.png)

Như mô tả trên Hình 9.5a, hướng của $\vec{\omega}$ được xác định bằng quy tắc bàn tay phải: Nếu khum các ngón tay phải theo chiều quay của vật rắn, ngón tay cái choãi ra sẽ chỉ theo hướng của vectơ $\vec{\omega}$. Nếu vật quay quanh trục $z$, vectơ $\vec{\omega}$ chỉ có thành phần theo phương $z$. Thành phần này mang dấu dương nếu $\vec{\omega}$ hướng theo chiều dương trục $z$ và mang dấu âm nếu hướng theo chiều âm trục $z$ (Hình 9.5b).

Cách biểu diễn dưới dạng vectơ đặc biệt hữu ích khi phương của trục quay thay đổi trong không gian. Cần lưu ý rằng trong không gian ba chiều tổng quát, các góc quay hữu hạn không phải là đại lượng vectơ vì phép quay hữu hạn không có tính giao hoán. Tuy nhiên, đạo hàm của độ dời góc theo thời gian là một vectơ thực sự, và khi trục quay luôn được giữ cố định như trong chương này, vectơ $\vec{\omega}$ luôn nằm dọc theo trục quay và chúng ta hoàn toàn mô tả chuyển động thông qua thành phần đại số $\omega_z$.

::: warning Lưu ý: Vectơ vận tốc góc vuông góc với mặt phẳng quay
Người học rất dễ nhầm lẫn rằng vectơ vận tốc góc $\vec{\omega}$ chỉ theo hướng chuyển động của một phần tử nào đó trên vật, hoặc tưởng tượng $\vec{\omega}$ là một "vectơ cong" uốn theo chiều quay. Cả hai cách hiểu này đều sai bản chất. Vận tốc góc là thuộc tính chung của toàn bộ vật rắn quay chứ không thuộc về riêng một điểm nào, và trong toán học giải tích vectơ không tồn tại khái niệm vectơ cong. Hướng của $\vec{\omega}$ được quy ước nằm dọc theo trục quay, vuông góc với mặt phẳng quay, vì trục quay là yếu tố hình học chung duy nhất cho mọi phần tử trên vật rắn.
:::

### Gia tốc góc

Một vật rắn có vận tốc góc biến đổi theo thời gian sẽ có gia tốc góc. Khi người đạp xe dùng lực nhấn bàn đạp mạnh hơn để bánh xe quay nhanh hơn hoặc bóp phanh để dừng xe, bánh xe đang nhận một gia tốc góc.

Nếu $\omega_{1z}$ và $\omega_{2z}$ là các giá trị vận tốc góc tức thời tại hai thời điểm $t_1$ và $t_2$, chúng ta định nghĩa **gia tốc góc trung bình** $\alpha_{\text{av-}z}$ trong khoảng thời gian $\Delta t = t_2 - t_1$ là tỉ số giữa độ biến thiên vận tốc góc và $\Delta t$ (Hình 9.6):
$$
\begin{aligned}
\alpha_{\text{av-}z} &= \frac{\omega_{2z} - \omega_{1z}}{t_2 - t_1} \\
&= \frac{\Delta\omega_z}{\Delta t}
\end{aligned}
\tag{9.4}
$$

![Hình 9.6: Tính gia tốc góc trung bình của một vật rắn quay quanh trục cố định.](../img/young-09/a-hinh-9-06.png)

**Gia tốc góc tức thời** $\alpha_z$ là giới hạn của gia tốc góc trung bình khi khoảng thời gian $\Delta t$ dần tới không:
$$
\alpha_z = \lim_{\Delta t \to 0} \frac{\Delta\omega_z}{\Delta t} = \frac{d\omega_z}{dt}
\tag{9.5}
$$

Đơn vị đo tiêu chuẩn của gia tốc góc là radian trên giây bình phương ($\text{rad/s}^2$). Từ đây về sau, thuật ngữ "gia tốc góc" luôn ngầm định là gia tốc góc tức thời.

Vì $\omega_z = d\theta/dt$, chúng ta cũng có thể biểu diễn gia tốc góc thông qua đạo hàm bậc hai của tọa độ góc:
$$
\alpha_z = \frac{d}{dt}\left(\frac{d\theta}{dt}\right) = \frac{d^2\theta}{dt^2}
\tag{9.6}
$$

Các đại lượng động học góc được ký hiệu bằng các chữ cái Hy Lạp: $\theta$ cho vị trí góc, $\omega_z$ cho vận tốc góc và $\alpha_z$ cho gia tốc góc. Các đại lượng này hoàn toàn tương đồng với $x$, $v_x$ và $a_x$ trong chuyển động thẳng. Trong cả hai trường hợp, vận tốc là tốc độ biến thiên của vị trí theo thời gian và gia tốc là tốc độ biến thiên của vận tốc theo thời gian.

Nếu gia tốc góc $\alpha_z$ mang dấu dương, vận tốc góc $\omega_z$ đang tăng đại số. Ngược lại, nếu $\alpha_z$ mang dấu âm, vận tốc góc $\omega_z$ đang giảm đại số. Chuyển động quay là nhanh dần khi $\alpha_z$ và $\omega_z$ cùng dấu, và là chậm dần khi hai đại lượng trái dấu. Quy tắc này cũng áp dụng cho chuyển động thẳng một chiều.

::: example Ví dụ 9.2: Tính toán gia tốc góc của bánh đà
**Bài toán**: Đối với bánh đà đã khảo sát trong Ví dụ 9.1:

(a) Tìm gia tốc góc trung bình trong khoảng thời gian từ $t_1 = 2{,}0\text{ s}$ đến $t_2 = 5{,}0\text{ s}$.

(b) Xác định gia tốc góc tức thời tại hai thời điểm $t_1 = 2{,}0\text{ s}$ và $t_2 = 5{,}0\text{ s}$.

**Tóm tắt**:
- Vận tốc góc tại các mốc thời gian: $\omega_{1z} = 24\text{ rad/s}$ tại $t_1 = 2{,}0\text{ s}$; $\omega_{2z} = 150\text{ rad/s}$ tại $t_2 = 5{,}0\text{ s}$.
- Hàm vận tốc góc tức thời: $\omega_z(t) = (6{,}0\text{ rad/s}^3)t^2$.

**Hướng đi**:
- Ở câu (a), áp dụng phương trình (9.4) tính tỉ số $\Delta\omega_z/\Delta t$.
- Ở câu (b), lấy đạo hàm của $\omega_z(t)$ theo thời gian để nhận được hàm $\alpha_z(t) = d\omega_z/dt$ rồi thay các giá trị $t_1, t_2$.

**Lời giải**:

(a) Từ các kết quả của Ví dụ 9.1, vận tốc góc ở hai thời điểm là $\omega_{1z} = 24\text{ rad/s}$ và $\omega_{2z} = 150\text{ rad/s}$. Độ biến thiên vận tốc góc là $\Delta\omega_z = 126\text{ rad/s}$ trong khoảng thời gian $\Delta t = 3{,}0\text{ s}$. Áp dụng phương trình (9.4), gia tốc góc trung bình là:
$$
\begin{aligned}
\alpha_{\text{av-}z} &= \frac{\Delta\omega_z}{\Delta t} \\
&= \frac{126\text{ rad/s}}{3{,}0\text{ s}} \\
&= 42\text{ rad/s}^2
\end{aligned}
$$

(b) Từ hàm $\omega_z = (6{,}0\text{ rad/s}^3)t^2$, áp dụng phương trình (9.5) ta có gia tốc góc tại thời điểm $t$ bất kỳ:
$$
\begin{aligned}
\alpha_z &= \frac{d\omega_z}{dt} \\
&= \frac{d}{dt}\left[(6{,}0\text{ rad/s}^3)t^2\right] \\
&= (12\text{ rad/s}^3)t
\end{aligned}
$$

Thay các giá trị thời điểm cụ thể:
$$
\begin{aligned}
\alpha_{1z} &= (12\text{ rad/s}^3)(2{,}0\text{ s}) \\
&= 24\text{ rad/s}^2
\end{aligned}
$$
$$
\begin{aligned}
\alpha_{2z} &= (12\text{ rad/s}^3)(5{,}0\text{ s}) \\
&= 60\text{ rad/s}^2
\end{aligned}
$$

**Đánh giá**:
Gia tốc góc trong chuyển động này không phải là hằng số mà tăng tuyến tính theo thời gian. Vận tốc góc $\omega_z$ luôn tăng vì $\alpha_z$ luôn dương, và tốc độ tăng của vận tốc góc cũng tăng dần vì bản thân $\alpha_z$ tăng theo thời gian.

**Trọng tâm tư duy**:
Để tìm gia tốc góc trung bình của vật rắn quay, hãy lấy độ biến thiên vận tốc góc chia cho khoảng thời gian. Để tìm gia tốc góc tức thời, hãy lấy đạo hàm bậc nhất của hàm vận tốc góc theo thời gian.
:::

### Gia tốc góc dưới dạng vectơ

Tương tự như vận tốc góc, chúng ta định nghĩa **vectơ gia tốc góc** $\vec{\alpha}$. Về mặt toán học, $\vec{\alpha}$ là đạo hàm theo thời gian của vectơ vận tốc góc:
$$
\vec{\alpha} = \frac{d\vec{\omega}}{dt}
$$

Nếu vật thể quay quanh trục $z$ cố định, vectơ $\vec{\alpha}$ chỉ có một thành phần duy nhất là $\alpha_z$ dọc theo trục quay. Trong trường hợp này, $\vec{\alpha}$ cùng hướng với $\vec{\omega}$ nếu chuyển động quay nhanh dần, và ngược hướng với $\vec{\omega}$ nếu chuyển động quay chậm dần (Hình 9.7).

![Hình 9.7: Khi trục quay cố định, cả vectơ gia tốc góc $\vec{\alpha}$ và vectơ vận tốc góc $\vec{\omega}$ đều nằm dọc theo trục quay đó.](../img/young-09/a-hinh-9-07.png)

::: info Ứng dụng sinh học: Chuyển động quay ở vi khuẩn
Vi khuẩn *Escherichia coli* (kích thước khoảng $2\,\mu\text{m} \times 0{,}5\,\mu\text{m}$) sinh sống phổ biến trong hệ tiêu hóa của người và động vật máu nóng. Vi khuẩn này bơi trong môi trường dịch lỏng bằng cách quay các sợi roi bơi (flagella) dài có dạng xoắn ốc, hoạt động tương tự như những cánh chân vịt.

Mỗi sợi roi bơi được dẫn động bởi một cỗ máy phân tử protein quay nằm tại màng tế bào của vi khuẩn. Động cơ sinh học này có thể quay roi bơi với tốc độ góc từ $200$ đến $1000\text{ rpm}$ (khoảng $20$ đến $100\text{ rad/s}$) và có khả năng thay đổi tốc độ linh hoạt để tạo ra gia tốc góc cho roi bơi, giúp vi khuẩn chuyển hướng hoặc tăng tốc tìm kiếm nguồn dinh dưỡng.

![Hình 9.7A: Động cơ quay phân tử sinh học điều khiển roi bơi ở vi khuẩn Escherichia coli.](../img/young-09/a-ung-dung-vi-khuan.png)
:::

::: info Câu hỏi tự kiểm tra mục 9.1
Hình 9.7B biểu diễn đồ thị vận tốc góc $\omega_z$ và gia tốc góc $\alpha_z$ theo thời gian của một vật rắn quay quanh trục cố định.

![Hình 9.7B: Đồ thị vận tốc góc $\omega_z$ và gia tốc góc $\alpha_z$ theo thời gian cho câu hỏi tự kiểm tra.](../img/young-09/a-tyu-9-01.png)

(a) Trong những khoảng thời gian nào chuyển động quay là nhanh dần?
- (i) $0 < t < 2\text{ s}$
- (ii) $2\text{ s} < t < 4\text{ s}$
- (iii) $4\text{ s} < t < 6\text{ s}$

(b) Trong những khoảng thời gian nào chuyển động quay là chậm dần?
- (i) $0 < t < 2\text{ s}$
- (ii) $2\text{ s} < t < 4\text{ s}$
- (iii) $4\text{ s} < t < 6\text{ s}$

<details><summary>Xem lời giải thích</summary>

**Đáp án đúng**:
- **(a): (i) và (iii)**.
- **(b): (ii)**.

Chuyển động quay là nhanh dần khi vận tốc góc và gia tốc góc có cùng dấu, và là chậm dần khi chúng trái dấu:

- Trong khoảng $0 < t < 2\text{ s}$: Cả $\omega_z$ và $\alpha_z$ đều mang dấu dương, do đó chuyển động quay nhanh dần.
- Trong khoảng $2\text{ s} < t < 4\text{ s}$: Vận tốc góc $\omega_z$ mang dấu dương nhưng gia tốc góc $\alpha_z$ mang dấu âm, hai đại lượng trái dấu nên chuyển động quay chậm dần.
- Trong khoảng $4\text{ s} < t < 6\text{ s}$: Cả $\omega_z$ và $\alpha_z$ đều mang dấu âm, hai đại lượng cùng dấu âm nên chuyển động quay nhanh dần theo chiều ngược lại.

Lưu ý rằng vật rắn quay theo một chiều ứng với $\omega_z > 0$ khi $t < 4\text{ s}$, và quay theo chiều ngược lại ứng với $\omega_z < 0$ khi $t > 4\text{ s}$.

</details>
:::
