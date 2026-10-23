## Liên hệ giữa các đại lượng động học dài và góc

Làm thế nào để tìm vận tốc dài và gia tốc dài của một điểm cụ thể trên một vật rắn đang quay? Đây là câu hỏi có ý nghĩa then chốt để chúng ta mở rộng khảo sát động học sang động lực học và năng lượng. Chẳng hạn, khi xác định động năng của vật rắn quay, chúng ta phải xuất phát từ biểu thức động năng của từng chất điểm cấu thành $K = \frac{1}{2}mv^2$, đòi hỏi phải nắm rõ tốc độ dài $v$ của từng hạt trong vật. Vì vậy, việc thiết lập mối liên hệ tổng quát giữa các đại lượng góc của vật rắn và các đại lượng dài của một điểm bất kỳ trên vật là bước đi căn bản và thiết thực.

### Tốc độ dài trong chuyển động quay của vật rắn

Khi một vật rắn quay quanh trục cố định, mọi chất điểm cấu thành vật đều chuyển động theo một quỹ đạo tròn nằm trong mặt phẳng vuông góc với trục quay và có tâm nằm ngay trên trục quay. Tốc độ dài của một chất điểm tỷ lệ thuận với tốc độ góc của vật: Khi vật quay càng nhanh, tốc độ chuyển động của từng điểm trên vật càng lớn.

Xét một điểm $P$ nằm cách trục quay một khoảng cách vuông góc cố định là $r$ như trong Hình 9.9. Khi vật quay, điểm $P$ vạch nên một đường tròn bán kính $r$. Tại mỗi thời điểm, mối liên hệ giữa góc quay $\theta$ (đo bằng radian) và độ dài cung tròn $s$ mà điểm $P$ đã quét qua được xác định bởi:
$$
s = r\theta
$$

![Hình 9.9: Vật rắn quay quanh một trục cố định đi qua điểm O.](../img/young-09/a-hinh-9-09.png)

Lấy đạo hàm hai vế của phương trình này theo thời gian $t$, chú ý rằng khoảng cách $r$ là đại lượng không đổi đối với một điểm cố định trên vật rắn:
$$
\left| \frac{ds}{dt} \right| = r\left| \frac{d\theta}{dt} \right|
$$

Đại lượng $|\frac{ds}{dt}|$ là độ lớn tốc độ biến thiên của độ dài cung, chính là tốc độ dài tức thời $v$ của điểm $P$. Còn $|\frac{d\theta}{dt}|$ là độ lớn tốc độ biến thiên của góc quay, tức là tốc độ góc tức thời $\omega$ của vật rắn (đơn vị $\text{rad/s}$). Từ đó, ta thu được mối liên hệ:
$$
v = r\omega
\tag{9.13}
$$

Trong phương trình (9.13):
- $v$ là tốc độ dài của điểm đang xét trên vật rắn ($\text{m/s}$).
- $r$ là khoảng cách vuông góc từ điểm đó đến trục quay ($\text{m}$).
- $\omega$ là tốc độ góc tức thời của vật rắn ($\text{rad/s}$).

Phương trình (9.13) cho thấy: Điểm nào càng ở xa trục quay (giá trị $r$ càng lớn) thì tốc độ dài $v$ của nó càng lớn. Vector vận tốc $\vec{v}$ của điểm $P$ luôn tiếp tuyến với quỹ đạo tròn tại mỗi thời điểm.

::: warning Lưu ý: Phân biệt tốc độ và vận tốc
Cần phân biệt rõ giữa tốc độ dài $v$ và tốc độ góc $\omega$ trong phương trình (9.13) với các đại lượng vận tốc dài $v_x$ và vận tốc góc $\omega_z$.

Các đại lượng không mang chỉ số dưới ($v$ và $\omega$) luôn luôn không âm, vì chúng đại diện cho độ lớn của các vector vận tốc $\vec{v}$ và $\vec{\omega}$, chỉ cho biết chất điểm chuyển động nhanh đến mức nào hoặc vật quay nhanh đến mức nào.

Ngược lại, các đại lượng có chỉ số thành phần như $v_x$ hay $\omega_z$ có thể nhận giá trị dương hoặc âm để chỉ rõ chiều chuyển động dọc theo trục tọa độ đã chọn.
:::

### Gia tốc dài trong chuyển động quay của vật rắn

Gia tốc toàn phần $\vec{a}$ của một chất điểm chuyển động tròn có thể phân tích thành hai thành phần vuông góc: Thành phần tiếp tuyến $a_{\text{tan}}$ và thành phần hướng tâm $a_{\text{rad}}$ (Hình 9.10).

![Hình 9.10: Vật rắn có chuyển động quay nhanh dần. Gia tốc của điểm P gồm thành phần hướng tâm $a_{\text{rad}}$ hướng về trục quay và thành phần tiếp tuyến $a_{\text{tan}}$ dọc theo quỹ đạo tròn.](../img/young-09/a-hinh-9-10.png)

Thành phần gia tốc tiếp tuyến $a_{\text{tan}}$ song song với vector vận tốc tức thời, có vai trò làm biến đổi độ lớn vận tốc (tức làm thay đổi tốc độ dài). Lấy đạo hàm hai vế của phương trình (9.13) theo thời gian:
$$
a_{\text{tan}} = \frac{dv}{dt}
$$
$$
a_{\text{tan}} = r\frac{d\omega}{dt} = r\alpha
\tag{9.14}
$$

Trong phương trình (9.14), $\alpha = \frac{d\omega}{dt}$ là tốc độ biến thiên của tốc độ góc. Thành phần gia tốc tiếp tuyến này luôn tiếp xúc với quỹ đạo tròn của điểm $P$. Cần lưu ý rằng $\alpha$ ở đây là tốc độ biến đổi của tốc độ góc, không hoàn toàn đồng nhất với gia tốc góc đại số $\alpha_z = \frac{d\omega_z}{dt}$. Đối với chuyển động quay quanh trục cố định, $\alpha = \alpha_z$ khi $\omega_z > 0$, và $\alpha = -\alpha_z$ khi $\omega_z < 0$.

Thành phần gia tốc hướng tâm $a_{\text{rad}}$ hướng thẳng vào trục quay, gắn liền với sự đổi hướng của vector vận tốc của điểm $P$. Từ kết quả động học chất điểm $a_{\text{rad}} = \frac{v^2}{r}$, kết hợp với biểu thức $v = r\omega$ từ phương trình (9.13), ta có:
$$
a_{\text{rad}} = \frac{v^2}{r} = \omega^2 r
\tag{9.15}
$$

Phương trình (9.15) nghiệm đúng tại mọi thời điểm tức thời, ngay cả khi tốc độ góc $\omega$ và gia tốc góc $\alpha$ biến thiên theo thời gian. Vector gia tốc hướng tâm luôn luôn hướng về trục quay.

::: warning Lưu ý: Bắt buộc dùng đơn vị radian
Phương trình $s = r\theta$ chỉ nghiệm đúng khi góc $\theta$ được đo bằng đơn vị radian. Do đó, mọi hệ thức suy biến từ nó, bao gồm phương trình (9.13), (9.14) và (9.15), đều bắt buộc phải biểu diễn các đại lượng góc theo đơn vị radian ($\text{rad}$, $\text{rad/s}$, $\text{rad/s}^2$).

Tuyệt đối không được thay trực tiếp số đo góc bằng độ hoặc số vòng quay vào các phương trình này mà chưa đổi sang radian (Hình 9.11).
:::

![Hình 9.11: Luôn luôn sử dụng đơn vị radian khi thiết lập liên hệ giữa các đại lượng dài và đại lượng góc.](../img/young-09/a-hinh-9-11.png)

### Sự truyền động không trượt

Các phương trình (9.1), (9.13) và (9.14) cũng nghiệm đúng cho bất kỳ chất điểm hoặc vật thể nào có cùng vận tốc tiếp tuyến với một điểm trên vật rắn quay.

Chẳng hạn, khi một sợi dây quấn quanh một hình trụ tròn nhả ra mà không bị dãn và không bị trượt, tốc độ và gia tốc tiếp tuyến của sợi dây tại mọi thời điểm đúng bằng tốc độ và gia tốc tiếp tuyến của điểm trên vành hình trụ nơi dây tiếp xúc.

Nguyên lý tương tự cũng áp dụng cho xích và đĩa líp xe đạp, hay dây curoa truyền động giữa các bánh đai quay không trượt. Cần lưu ý rằng phương trình (9.15) cho gia tốc hướng tâm $a_{\text{rad}}$ chỉ áp dụng cho các điểm trên dây hoặc xích khi chúng đang tiếp xúc và uốn cong theo vành bánh đĩa. Các đoạn dây thẳng tự do không có gia tốc hướng tâm hướng về trục quay của bánh xe.

::: example Ví dụ 9.4: Ném đĩa
Một vận động viên quay đĩa ném theo quỹ đạo tròn bán kính $80{,}0\text{ cm}$. Tại một thời điểm xác định, vận động viên đang quay với tốc độ góc $10{,}0\text{ rad/s}$ và tốc độ góc đang tăng với tốc độ $50{,}0\text{ rad/s}^2$. Tại thời điểm này, hãy tìm các thành phần tiếp tuyến và hướng tâm của gia tốc đĩa ném, cùng với độ lớn của gia tốc toàn phần.

![Hình 9.12: (a) Vận động viên quay đĩa ném theo quỹ đạo tròn. (b) Sơ đồ phân tích các thành phần gia tốc của đĩa ném.](../img/young-09/a-hinh-9-12.png)

**Tóm tắt:**
- Bán kính quỹ đạo: $r = 80{,}0\text{ cm} = 0{,}800\text{ m}$.
- Tốc độ góc tức thời: $\omega = 10{,}0\text{ rad/s}$.
- Tốc độ tăng tốc độ góc: $\alpha = 50{,}0\text{ rad/s}^2$.
- Cần tìm: Gia tốc tiếp tuyến $a_{\text{tan}}$, gia tốc hướng tâm $a_{\text{rad}}$, và độ lớn gia tốc toàn phần $a$.

**Hướng đi:**
- Coi đĩa ném như một chất điểm chuyển động tròn quanh trục quay đi qua thân vận động viên (Hình 9.12a).
- Áp dụng phương trình (9.14) $a_{\text{tan}} = r\alpha$ để tính thành phần gia tốc tiếp tuyến gây bởi sự tăng tốc độ quay.
- Áp dụng phương trình (9.15) $a_{\text{rad}} = \omega^2 r$ để tính thành phần gia tốc hướng tâm gây bởi sự đổi hướng chuyển động.
- Vì hai thành phần gia tốc tiếp tuyến và hướng tâm vuông góc với nhau (Hình 9.12b), độ lớn gia tốc toàn phần được xác định bằng định lý Pythagore: $a = \sqrt{a_{\text{tan}}^2 + a_{\text{rad}}^2}$.

**Lời giải:**
- Thành phần gia tốc tiếp tuyến của đĩa ném:
$$
\begin{aligned}
a_{\text{tan}} &= r\alpha \\
&= (0{,}800)(50{,}0) \\
&= 40{,}0\text{ m/s}^2
\end{aligned}
$$

- Thành phần gia tốc hướng tâm của đĩa ném:
$$
\begin{aligned}
a_{\text{rad}} &= \omega^2 r \\
&= (10{,}0)^2(0{,}800) \\
&= 80{,}0\text{ m/s}^2
\end{aligned}
$$

- Độ lớn của gia tốc toàn phần:
$$
\begin{aligned}
a &= \sqrt{a_{\text{tan}}^2 + a_{\text{rad}}^2} \\
&= \sqrt{40{,}0^2 + 80{,}0^2} \\
&= 89{,}4\text{ m/s}^2
\end{aligned}
$$

**Đánh giá:**
Đơn vị radian là một số thuần túy không có thứ nguyên, do đó tự triệt tiêu khi kết hợp với mét để cho đơn vị gia tốc tiêu chuẩn $\text{m/s}^2$.

Nếu tốc độ góc tăng gấp đôi lên $\omega = 20{,}0\text{ rad/s}$ trong khi gia tốc góc vẫn giữ nguyên $\alpha = 50{,}0\text{ rad/s}^2$, thành phần tiếp tuyến vẫn là $a_{\text{tan}} = 40{,}0\text{ m/s}^2$, nhưng thành phần hướng tâm tăng thành $a_{\text{rad}} = 320\text{ m/s}^2$. Khi đó độ lớn gia tốc toàn phần tăng vọt lên thành:
$$
\begin{aligned}
a &= \sqrt{40{,}0^2 + 320^2} \\
&= 322\text{ m/s}^2
\end{aligned}
$$

**Trọng tâm tư duy:**
Các điểm trên một vật rắn luôn có thành phần gia tốc hướng tâm $a_{\text{rad}} = \omega^2 r$ chừng nào vật còn quay. Điểm chỉ có thêm thành phần gia tốc tiếp tuyến $a_{\text{tan}} = r\alpha$ khi tốc độ góc $\omega$ thay đổi. Vì hai thành phần này vuông góc với nhau, chúng ta luôn dùng định lý Pythagore để tìm độ lớn gia tốc toàn phần.
:::

::: example Ví dụ 9.5: Thiết kế cánh quạt máy bay
Bạn đang thiết kế cánh quạt cho một máy bay có tốc độ quay $2400\text{ rpm}$ (Hình 9.13a). Tốc độ bay tới của máy bay là $75{,}0\text{ m/s}$, và tốc độ của đầu mút cánh quạt đối với không khí không được vượt quá $270\text{ m/s}$ (vào khoảng $80\%$ tốc độ âm thanh trong không khí; nếu đầu mút chuyển động nhanh hơn, chúng sẽ gây ra tiếng ồn cực lớn và sóng xung kích có hại). (a) Bán kính tối đa của cánh quạt có thể bằng bao nhiêu? (b) Với bán kính này, gia tốc của đầu mút cánh quạt bằng bao nhiêu?

![Hình 9.13: (a) Máy bay cánh quạt đang bay. (b) Sơ đồ phân tích các thành phần vận tốc tại đầu mút cánh quạt.](../img/young-09/a-hinh-9-13.png)

**Tóm tắt:**
- Tốc độ quay của cánh quạt: $\omega = 2400\text{ rpm}$.
- Tốc độ bay tới của máy bay: $v_{\text{plane}} = 75{,}0\text{ m/s}$.
- Giới hạn tốc độ đầu mút cánh quạt: $v_{\text{tip}} \le 270\text{ m/s}$.
- Cần tìm: Bán kính cực đại $r$ của cánh quạt và gia tốc $a$ của đầu mút.

**Hướng đi:**
- Xét một chất điểm tại đầu mút cánh quạt. Tốc độ của chất điểm này trong không khí là kết quả kết hợp giữa chuyển động quay của cánh quạt và chuyển động tịnh tiến về phía trước của máy bay.
- Hình 9.13b chỉ ra rằng vector vận tốc $\vec{v}_{\text{tip}}$ là tổng vector của vận tốc tiếp tuyến do chuyển động quay $\vec{v}_{\text{tan}}$ và vận tốc tịnh tiến của máy bay $\vec{v}_{\text{plane}}$.
- Cánh quạt quay trong mặt phẳng vuông góc với hướng bay, do đó hai vector $\vec{v}_{\text{tan}}$ và $\vec{v}_{\text{plane}}$ vuông góc với nhau. Ta áp dụng định lý Pythagore để liên hệ $v_{\text{tip}}$ với $v_{\text{tan}}$ và $v_{\text{plane}}$.
- Đặt $v_{\text{tip}} = 270\text{ m/s}$ để giải ra bán kính tối đa $r$.
- Tốc độ quay của cánh quạt là không đổi, nên gia tốc tiếp tuyến bằng không ($a_{\text{tan}} = 0$). Gia tốc của đầu mút chỉ gồm thành phần hướng tâm $a_{\text{rad}} = \omega^2 r$.

**Lời giải:**
- Chuyển đổi tốc độ quay sang đơn vị radian trên giây:
$$
\begin{aligned}
\omega &= 2400\times \frac{2\pi}{60}\text{ rad/s} \\
&\approx 251\text{ rad/s}
\end{aligned}
$$

- (a) Bán kính cực đại của cánh quạt:
Từ Hình 9.13b và phương trình (9.13), ta có:
$$
v_{\text{tip}}^2 = v_{\text{plane}}^2 + v_{\text{tan}}^2
$$
$$
v_{\text{tip}}^2 = v_{\text{plane}}^2 + r^2\omega^2
$$
suy ra:
$$
r = \frac{\sqrt{v_{\text{tip}}^2 - v_{\text{plane}}^2}}{\omega}
$$
Thay các giá trị giới hạn $v_{\text{tip}} = 270\text{ m/s}$, $v_{\text{plane}} = 75{,}0\text{ m/s}$ và $\omega = 251\text{ rad/s}$:
$$
r = \frac{\sqrt{270^2 - 75{,}0^2}}{251}\text{ m}
$$
$$
r = 1{,}03\text{ m}
$$

- (b) Gia tốc của đầu mút cánh quạt:
Vì tốc độ quay không đổi nên $a_{\text{tan}} = 0$. Áp dụng phương trình (9.15), gia tốc hướng tâm là:
$$
\begin{aligned}
a_{\text{rad}} &= \omega^2 r \\
&= (251)^2(1{,}03) \\
&\approx 6{,}5 \times 10^4\text{ m/s}^2
\end{aligned}
$$
Gia tốc toàn phần có độ lớn đúng bằng gia tốc hướng tâm: $a = 6{,}5 \times 10^4\text{ m/s}^2$.

**Đánh giá:**
Theo định luật II Newton $\sum \vec{F} = m\vec{a}$, kết cấu cánh quạt phải chịu và tác dụng một lực giữ lên tới $6{,}5 \times 10^4\text{ N}$ trên mỗi kilogram vật liệu ở đầu mút. Gia tốc này gấp hơn $6600$ lần gia tốc trọng trường $g$. Đây là lý do cốt lõi giải thích vì sao cánh quạt máy bay phải được chế tạo từ các vật liệu có độ bền cơ học đặc biệt cao như hợp kim nhôm chuyên dụng hoặc composite sợi carbon cường lực.

**Trọng tâm tư duy:**
Nếu một vật rắn vừa quay vừa tịnh tiến trong không gian, vận tốc của một điểm bất kỳ trên vật rắn được xác định thông qua phép cộng vector giữa vận tốc tịnh tiến và vận tốc quay tiếp tuyến tương đối.
:::

### Kiểm tra hiểu biết mục 9.3

Thông tin trên đĩa quang Blu-ray (xem Hình 9.8) được lưu trữ dưới dạng các vết lõm siêu nhỏ được mã hóa. Các vết này được bố trí dọc theo một rãnh xoắn ốc tỏa dần từ tâm ra mép ngoài của đĩa. Khi đĩa quay bên trong đầu đọc, rãnh dữ liệu được đầu đọc quang học quét qua với tốc độ dài không đổi. Tốc độ quay $\omega$ của đĩa phải biến đổi như thế nào khi đầu đọc quét dần ra phía ngoài vành đĩa?

- (i) $\omega$ phải tăng dần.
- (ii) $\omega$ phải giảm dần.
- (iii) $\omega$ giữ nguyên không đổi.

<details>
<summary>Xem lời giải thích</summary>

**Đáp án đúng: (ii)**

Theo phương trình (9.13), mối liên hệ giữa tốc độ dài và tốc độ góc là:
$$
v = r\omega
$$

Để duy trì tốc độ dài $v$ không đổi khi quét qua các rãnh dữ liệu, tốc độ góc $\omega$ phải tỷ lệ nghịch với bán kính: $\omega = \frac{v}{r}$. Khi đầu đọc di chuyển dần ra phía ngoài, khoảng cách $r$ từ trục quay đến điểm đọc tăng dần, do đó tốc độ quay $\omega$ của đĩa buộc phải giảm dần tương ứng.

</details>
