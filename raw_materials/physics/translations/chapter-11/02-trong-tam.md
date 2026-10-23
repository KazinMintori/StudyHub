## 11.2 Trọng Tâm

Trong phần lớn các bài toán cân bằng vật rắn, một trong những ngoại lực chủ yếu luôn luôn hiện diện chính là trọng lực của vật. Trọng lực không tác dụng tập trung vào một điểm hình học duy nhất, mà là một lực khối phân bố liên tục tác dụng lên từng phần tử vật chất cấu tạo nên vật thể. Tuy nhiên, trong tính toán cơ học, ta hoàn toàn có thể biểu diễn tác dụng tổng hợp của toàn bộ hệ lực trọng trường phân bố này bằng một trọng lực duy nhất đặt tại một điểm đặc biệt gọi là **trọng tâm** (center of gravity).

Mỗi phần tử vật chất thứ $i$ có khối lượng $m_i$ chịu một trọng lực $\vec{w}_i = m_i \vec{g}$. Tổng vectơ của tất cả các lực trọng trường này bằng tổng trọng lượng của vật thể:

$$
\vec{w} = \sum_i \vec{w}_i
$$

### Định Nghĩa Trọng Tâm Từ Mômen Trọng Lực

Xét một vật thể có hình dạng bất kỳ đặt trong hệ tọa độ Descartes với gốc tọa độ $O$. Giả sử mỗi phần tử vật chất thứ $i$ có vectơ vị trí $\vec{r}_i = x_i \hat{i} + y_i \hat{j} + z_i \hat{k}$.

Mômen trọng lực của phần tử thứ $i$ đối với gốc $O$ là:

$$
\vec{\tau}_i = \vec{r}_i \times \vec{w}_i
$$

Tổng mômen trọng lực do Trái Đất tác dụng lên toàn bộ vật rắn đối với điểm $O$ được tính bằng tổng các mômen thành phần:

$$
\vec{\tau} = \sum_i (\vec{r}_i \times \vec{w}_i)
$$

**Định nghĩa trọng tâm**: Trọng tâm của một vật là điểm duy nhất có vectơ vị trí $\vec{r}_{\mathrm{cg}}$ sao cho nếu toàn bộ trọng lượng $\vec{w}$ của vật được xem như đặt tập trung tại điểm đó, thì mômen lực do trọng lượng tổng hợp $\vec{w}$ gây ra đối với bất kỳ điểm quy chiếu $O$ nào cũng đúng bằng tổng mômen trọng lực của tất cả các phần tử vật chất cấu thành vật thể:

$$
\vec{\tau} = \vec{r}_{\mathrm{cg}} \times \vec{w}
$$

Giả sử gia tốc trọng trường $\vec{g}$ có cùng độ lớn và phương hướng song song tại mọi điểm trên vật, hướng thẳng đứng xuống dưới theo phương $-y$. Trọng lượng của phần tử thứ $i$ là $w_i = m_i g$. Mômen của lực $\vec{w}_i$ đối với trục $z$ vuông góc với mặt phẳng là:

$$
\tau_{zi} = -x_i w_i
$$

Dấu âm thể hiện xu hướng quay cùng chiều kim đồng hồ quanh gốc tọa độ. Tổng mômen lực quanh trục $z$ của toàn bộ vật thể là:

$$
\tau_z = -\sum_i x_i w_i
$$

Mặt khác, theo định nghĩa trọng tâm, mômen tổng hợp này phải bằng mômen của tổng trọng lượng $w = \sum_i w_i$ đặt tại tọa độ $x_{\mathrm{cg}}$:

$$
\tau_z = -x_{\mathrm{cg}} w
$$

Cân bằng hai vế, ta tìm được tọa độ trọng tâm $x_{\mathrm{cg}}$:

$$
x_{\mathrm{cg}} = \frac{\sum_i w_i x_i}{\sum_i w_i}
$$

Lặp lại lập luận tương tự khi quay vật thể để xác định các tọa độ còn lại:

$$
y_{\mathrm{cg}} = \frac{\sum_i w_i y_i}{\sum_i w_i}
$$

$$
z_{\mathrm{cg}} = \frac{\sum_i w_i z_i}{\sum_i w_i}
$$

Kết hợp ba thành phần tọa độ thành biểu thức vectơ trọng tâm:

$$
\vec{r}_{\mathrm{cg}} = \frac{\sum_i w_i \vec{r}_i}{\sum_i w_i}
$$

Phương trình trên định nghĩa tọa độ trọng tâm dưới dạng bình quân gia quyền theo trọng lượng của các phần tử.

![](../img/young-11/a-hinh-11-02.png)

*Hình 11.2: Trọng tâm (cg) và khối tâm (cm) của một vật thể mở rộng: Khi gia tốc trọng trường đều, trọng tâm trùng hoàn toàn với khối tâm.*

### Mối Quan Hệ Giữa Trọng Tâm Và Khối Tâm

Khối tâm của một vật thể được định nghĩa hoàn toàn dựa trên sự phân bố khối lượng của các phần tử chất điểm tạo nên vật. Tọa độ các thành phần của khối tâm là:

$$
x_{\mathrm{cm}} = \frac{\sum_i m_i x_i}{\sum_i m_i}
\tag{11.3}
$$

$$
y_{\mathrm{cm}} = \frac{\sum_i m_i y_i}{\sum_i m_i}
$$

$$
z_{\mathrm{cm}} = \frac{\sum_i m_i z_i}{\sum_i m_i}
$$

Ba phương trình tọa độ thành phần trong hệ phương trình (11.3) hoàn toàn tương đương với phương trình vectơ khối tâm duy nhất:

$$
\vec{r}_{\mathrm{cm}} = \frac{\sum_i m_i \vec{r}_i}{\sum_i m_i}
\tag{11.4}
$$

Bây giờ ta hãy khảo sát mômen trọng lực tác dụng lên toàn bộ vật thể có hình dạng bất kỳ (Hình 11.2). Giả sử gia tốc trọng trường $\vec{g}$ có cùng độ lớn và phương hướng tại mọi điểm trên vật thể. Mỗi phần tử khối lượng $m_i$ chịu trọng lực $\vec{w}_i = m_i \vec{g}$. Tổng mômen trọng lực đối với điểm gốc $O$ là:

$$
\vec{\tau} = \sum_i (\vec{r}_i \times m_i \vec{g})
$$

Đưa $\vec{g}$ ra ngoài dấu tích có hướng:

$$
\vec{\tau} = \left(\sum_i m_i \vec{r}_i\right) \times \vec{g}
$$

Nhân và chia biểu thức này cho tổng khối lượng $M = \sum_i m_i$ của toàn bộ vật thể:

$$
\vec{\tau} = \left(\frac{\sum_i m_i \vec{r}_i}{\sum_i m_i}\right) \times (M\vec{g})
$$

Thừa số trong dấu ngoặc đơn chính là vectơ vị trí khối tâm $\vec{r}_{\mathrm{cm}}$ đã xác định ở phương trình (11.4), còn đại lượng $M\vec{g}$ chính là tổng trọng lượng $\vec{w}$ của toàn bộ vật thể. Do đó:

$$
\vec{\tau} = \vec{r}_{\mathrm{cm}} \times \vec{w}
\tag{11.5}
$$

Phương trình (11.5) chứng tỏ rằng tổng mômen trọng lực tác dụng lên vật hoàn toàn tương đương với trường hợp toàn bộ trọng lượng $\vec{w}$ của vật được đặt tập trung tại duy nhất một điểm: Khối tâm $\vec{r}_{\mathrm{cm}}$ của vật. Điểm đặt hiệu dụng này chính là **trọng tâm** của vật.

Do đó, một hệ quả nền tảng được rút ra: **Nếu gia tốc trọng trường $\vec{g}$ có cùng giá trị tại mọi điểm trên một vật thể thì trọng tâm của vật hoàn toàn trùng khớp với khối tâm của nó.**

![](../img/young-11/a-hinh-11-03.png)

*Hình 11.3: Tòa tháp đôi Petronas tại Malaysia cao 452 m: Do độ cao lớn, gia tốc trọng trường ở chân tháp chỉ lớn hơn ở đỉnh tháp khoảng 0,014%, khiến trọng tâm lệch xuống dưới khối tâm một đoạn cực nhỏ vài milimét.*

Tuy nhiên, giữa hai khái niệm này có sự khác biệt bản chất về mặt vật lý:

- **Khối tâm** là một đại lượng hình học và quán tính thuần túy, phản ánh đặc tính phân bố khối lượng của vật. Khối tâm tồn tại độc lập với bất kỳ trường hấp dẫn nào. Một phi thuyền du hành trong khoảng không vũ trụ xa xôi không có trọng lực vẫn sở hữu một khối tâm xác định duy nhất.
- **Trọng tâm** lại phụ thuộc trực tiếp vào trường trọng lực tác dụng lên vật thể. Nếu trường trọng lực không đều, trọng tâm và khối tâm sẽ tách rời nhau. Chẳng hạn với một công trình kiến trúc chọc trời như tòa tháp đôi Petronas ở Malaysia có chiều cao $h = 452\,\text{m}$ (Hình 11.3), gia tốc trọng trường giảm dần theo độ cao. Tỷ số gia tốc trọng trường giữa mặt đất và đỉnh tháp được ước lượng theo quy luật vạn vật hấp dẫn:

$$
\frac{g_{\text{đáy}}}{g_{\text{đỉnh}}} \approx 1 + \frac{2h}{R_E}
$$

Thay bán kính Trái Đất $R_E \approx 6{,}38 \times 10^6\,\text{m}$ và chiều cao $h = 452\,\text{m}$, gia tốc trọng trường ở mặt đất chỉ lớn hơn ở đỉnh tháp khoảng $0{,}014\%$. Mức chênh lệch cực nhỏ này khiến các phần tử vật chất ở tầng dưới nặng hơn đôi chút so với các phần tử giống hệt ở tầng trên, làm cho trọng tâm thực tế nằm thấp hơn khối tâm một khoảng chừng vài milimét. Trong hầu hết các bài toán vật lý và kỹ thuật công trình, độ lệch này là hoàn toàn không đáng kể, do đó ta luôn luôn coi trọng tâm trùng với khối tâm.

### Phương Pháp Xác Định Và Tính Chất Của Trọng Tâm

Đối với các vật thể đồng chất có tính đối xứng hình học cao (như quả cầu, khối hộp chữ nhật, hình trụ tròn hoặc thanh thẳng đồng chất), trọng tâm luôn nằm ngay tại tâm đối xứng hình học của vật.

![](../img/young-11/a-hinh-11-04.png)

*Hình 11.4: Phương pháp xác định trọng tâm của vật có hình dạng bất kỳ bằng cách treo: Trọng tâm là giao điểm của hai đường thẳng đứng kẻ từ hai điểm treo khác nhau.*

Đối với những vật thể có hình dạng phức tạp, không đồng chất hoặc bất đối xứng, ta có thể xác định trọng tâm bằng thực nghiệm thông qua phương pháp treo dây dọi được mô tả trên Hình 11.4:

1. **Bước 1**: Treo vật tự do từ một điểm treo tùy ý $A$. Vật sẽ tự động xoay cho đến khi trọng tâm của nó nằm chính xác trên đường thẳng đứng kéo dài từ điểm treo xuống dưới. Tại vị trí này, cánh tay đòn của trọng lực đối với điểm treo bằng không, do đó mômen của trọng lực triệt tiêu và vật dừng lại ở trạng thái cân bằng tĩnh. Ta dùng dây dọi để đánh dấu đường thẳng đứng thứ nhất này lên vật.
2. **Bước 2**: Tiếp tục treo vật từ một điểm treo thứ hai $B$ khác với điểm ban đầu. Khi vật dừng lại ở trạng thái cân bằng mới, ta lại dùng dây dọi đánh dấu đường thẳng đứng thứ hai. Giao điểm của hai đường thẳng đứng này chính là vị trí của trọng tâm.

Trọng tâm không nhất thiết phải nằm bên trong phần vật chất hữu hình của vật thể. Đối với một chiếc cốc rỗng (Hình 11.4), một chiếc lốp xe hay một chiếc nhẫn tròn, trọng tâm hoàn toàn nằm trong không gian rỗng bên ngoài vật chất.

### Trọng Tâm Và Mức Độ Bền Vững Của Trạng Thái Cân Bằng

Khi một vật thể được nâng đỡ trên một mặt phẳng bằng nhiều điểm tựa phân tán, **diện tích mặt chân đế** (area of support) được định nghĩa là đa giác lồi nhỏ nhất bao quanh tất cả các điểm tiếp xúc đó.

![](../img/young-11/a-hinh-11-05.png)

*Hình 11.5: Vị trí trọng tâm và điều kiện lật của vật thể: Trong (a) trọng tâm nằm trong diện tích mặt chân đế nên xe cân bằng; trong (b) và (c) trọng tâm vượt ra ngoài mép chân đế khiến xe và khối hộp bị lật.*

Mối liên hệ giữa vị trí trọng tâm và tính bền vững của cân bằng được thể hiện rõ trên Hình 11.5:

- **Hình 11.5(a)**: Khi chiếc xe nghiêng ở góc nhỏ, đường thẳng đứng đi qua trọng tâm vẫn rơi vào bên trong diện tích mặt chân đế giữa hai bánh xe. Trọng lực tạo ra một mômen lực hướng ngược chiều nghiêng, có xu hướng kéo chiếc xe quay trở lại vị trí thăng bằng ban đầu. Trạng thái này là **cân bằng bền**.
- **Hình 11.5(b)**: Khi góc nghiêng tăng lên đến mức đường thẳng đứng đi qua trọng tâm vượt ra ngoài mép chân đế, mômen của trọng lực sẽ đổi chiều, có xu hướng làm chiếc xe quay xa hơn khỏi vị trí cân bằng và khiến xe bị lật nhào.
- **Hình 11.5(c)**: Khối hộp hoặc phương tiện có trọng tâm càng ở trên cao thì góc nghiêng giới hạn dẫn tới lật đổ càng nhỏ. Do đó, các dòng xe thể thao đua luôn được thiết kế gầm cực thấp và khoảng cách bánh xe rất rộng để đảm bảo an toàn cơ học khi vào cua gấp.

Đặc tính cơ học này giải thích sự khác biệt sinh học rõ rệt giữa động vật bốn chân và con người: Các loài thú bốn chân có diện tích mặt chân đế rất rộng giới hạn bởi bốn bàn chân, vì vậy chúng sở hữu tính ổn định tự nhiên rất cao và chỉ cần các bàn chân có kích thước tương đối nhỏ. Trái lại, con người đứng thẳng trên hai chân nên diện tích mặt chân đế nhỏ hơn rất nhiều, đòi hỏi bàn chân phải có chiều dài đáng kể và não bộ cùng hệ cơ bắp phải liên tục điều chỉnh tư thế để duy trì trọng tâm luôn nằm phía trên diện tích bàn chân.

![](../img/young-11/a-hinh-11-06.png)

*Hình 11.6: Phác thảo sơ đồ cơ học cho Ví dụ 11.1: Tấm ván đồng chất đặt trên hai giá đỡ và người bước ra mép ván.*

::: example Ví dụ 11.1: Đi trên tấm ván bắc cầu
Một tấm ván gỗ đồng chất có chiều dài $L = 6{,}0\,\text{m}$ và khối lượng $M = 90\,\text{kg}$ được đặt nằm ngang trên hai chiếc giá đỡ bằng gỗ. Hai giá đỡ cách nhau một khoảng $D = 1{,}5\,\text{m}$ và được bố trí đối xứng qua tâm của tấm ván, tức là phần ván nhô ra ở hai đầu có độ dài bằng nhau. Một cậu bé tên Throckmorton có khối lượng $m$ bước từ từ ra phía đầu mút bên phải của tấm ván (Hình 11.6). Hãy xác định giá trị khối lượng $m$ lớn nhất của cậu bé để tấm ván vẫn chưa bị bập bênh lật đổ.

**Tóm tắt**:
- Chiều dài tấm ván: $L = 6{,}0\,\text{m}$.
- Khối lượng tấm ván: $M = 90\,\text{kg}$.
- Khoảng cách hai giá đỡ: $D = 1{,}5\,\text{m}$.
- Tấm ván đồng chất, đối xứng.
- Mục tiêu: Tìm $m$ lớn nhất để hệ ở trạng thái cân bằng giới hạn.

**Hướng đi**:
- Tấm ván được nâng đỡ tại hai điểm tựa. Khi cậu bé bước càng xa về phía đầu mút bên phải, xu hướng lật quanh giá đỡ bên phải càng tăng lên, khiến lực ép lên giá đỡ bên trái giảm dần.
- Tại thời điểm tấm ván bắt đầu chớm lật, phản lực pháp tuyến do giá đỡ bên trái tác dụng lên ván sẽ triệt tiêu hoàn toàn: $n_1 = 0$.
- Khi đó, toàn bộ trọng lượng của hệ (gồm tấm ván và cậu bé) chỉ còn được nâng đỡ duy nhất bởi giá đỡ bên phải. Để hệ không bị lật, trọng tâm của hệ hai vật bắt buộc phải nằm thẳng đứng ngay phía trên điểm tựa giá đỡ bên phải.

**Các bước giải chi tiết**:
Chọn gốc tọa độ $O$ tại tâm hình học của tấm ván, chiều dương trục $x$ hướng sang bên phải. Vì tấm ván đồng chất nên khối tâm của ván nằm ngay tại gốc tọa độ: $x_P = 0$.

Do hai giá đỡ đặt đối xứng qua tâm ván và cách nhau $D = 1{,}5\,\text{m}$, tọa độ của giá đỡ bên phải là:

$$
x_S = \frac{D}{2}
$$

Khi cậu bé đứng tại đầu mút bên phải của tấm ván, tọa độ của cậu bé là:

$$
x_T = \frac{L}{2}
$$

Tọa độ trọng tâm $x_{\mathrm{cg}}$ của hệ gồm tấm ván và cậu bé được tính theo phương trình (11.3a):

$$
x_{\mathrm{cg}} = \frac{M x_P + m x_T}{M + m}
$$

Thay $x_P = 0$ và $x_T = L/2$ vào biểu thức:

$$
x_{\mathrm{cg}} = \frac{m}{M + m} \frac{L}{2}
$$

Để hệ vừa đúng ở trạng thái cân bằng giới hạn, trọng tâm của hệ phải trùng đúng với vị trí của giá đỡ bên phải, tức là $x_{\mathrm{cg}} = x_S = D/2$:

$$
\frac{m}{M + m} \frac{L}{2} = \frac{D}{2}
$$

Nhân cả hai vế với 2 rồi giải phương trình đại số để tìm $m$:

$$
m L = (M + m) D
$$

Chuyển các số hạng chứa ẩn số $m$ sang cùng một vế:

$$
m(L - D) = M D
$$

Từ đó, biểu thức khối lượng giới hạn của cậu bé là:

$$
m = M \frac{D}{L - D}
$$

Thay các giá trị số đề bài đã cho vào công thức:

$$
\begin{aligned}
m &= (90\,\text{kg}) \frac{1{,}5}{6{,}0 - 1{,}5} \\
&= 90\,\text{kg} \times \frac{1{,}5}{4{,}5} = 30\,\text{kg}
\end{aligned}
$$

**Đánh giá và kiểm tra**:
Để kiểm tra tính nhất quán vật lý, ta hãy thử lặp lại phép tính với gốc tọa độ đặt ngay tại giá đỡ bên phải. Khi đó, tọa độ tâm tấm ván là $x_P' = -D/2$, còn tọa độ của cậu bé là $x_T' = (L - D)/2$. Để hệ không bị lật thì trọng tâm phải nằm trên giá đỡ, tức là $x_{\mathrm{cg}} = 0$:

$$
-M \frac{D}{2} + m \frac{L - D}{2} = 0
$$

Nhân cả hai vế với 2 rồi rút gọn:

$$
m(L - D) = M D
$$

$$
m = 30\,\text{kg}
$$

Mở rộng phân tích: Nếu một người trưởng thành có khối lượng $60\,\text{kg}$ bước ra đầu mút bên phải của tấm ván thì tấm ván chắc chắn sẽ bị bập bênh lật đổ. Để không bị lật, người trưởng thành đó chỉ có thể bước ra một đoạn tối đa là $1{,}125\,\text{m}$ tính từ giá đỡ bên phải, tức là chỉ đi được một nửa quãng đường của phần ván nhô ra ngoài.
:::

::: tip Khái niệm cốt lõi: Điều kiện vị trí trọng tâm
Nếu một vật thể mở rộng được nâng đỡ tại hai hay nhiều điểm tựa thì để vật đạt trạng thái cân bằng tĩnh bền vững, trọng tâm của vật bắt buộc phải nằm ở một vị trí nào đó phía trên diện tích mặt chân đế được giới hạn bởi các điểm tựa. Nếu vật chỉ được nâng đỡ duy nhất tại một điểm tựa, trọng tâm của vật phải nằm chính xác trên đường thẳng đứng đi qua điểm tựa đó.
:::

::: warning Thận trọng: Lựa chọn điểm quy chiếu khi tính mômen lực
Trong trạng thái cân bằng, tổng mômen lực bằng không đối với mọi điểm quy chiếu trong không gian. Tuy nhiên, điều này không có nghĩa là mômen của một lực đơn lẻ bất kỳ đối với mọi điểm đều bằng nhau. Mômen của một lực phụ thuộc chặt chẽ vào vị trí điểm quy chiếu được chọn. Chỉ có **tổng** của tất cả các mômen lực mới độc lập với việc lựa chọn điểm quy chiếu, với điều kiện tiên quyết là tổng hợp lực tác dụng lên vật đã bằng không.
:::

![](../img/young-11/a-hinh-11-07.png)

*Hình 11.7: Xác định vị trí đặt con đội tam giác để thước mét gắn hòn đá đạt trạng thái cân bằng nằm ngang.*

::: question Kiểm tra hiểu biết 11.2
Một hòn đá được gắn chặt vào đầu mút bên trái của một chiếc thước mét đồng chất. Biết rằng chiếc thước mét có khối lượng đúng bằng khối lượng $m$ của hòn đá. Để tổ hợp gồm hòn đá và chiếc thước mét có thể cân bằng thăng bằng nằm ngang trên đỉnh một con đội hình tam giác nhọn như trên Hình 11.7, con đội tam giác cần phải được đặt cách đầu mút bên trái của cây thước một khoảng bằng bao nhiêu?

- (i) Nhỏ hơn $0{,}25\,\text{m}$.
- (ii) Bằng $0{,}25\,\text{m}$.
- (iii) Nằm trong khoảng từ $0{,}25\,\text{m}$ đến $0{,}50\,\text{m}$.
- (iv) Bằng $0{,}50\,\text{m}$.
- (v) Lớn hơn $0{,}50\,\text{m}$.

<details>
<summary>Xem lời giải thích</summary>

**Đáp án chính xác**: (ii) Bằng $0{,}25\,\text{m}$.

**Giải thích chi tiết**:
Để hệ gồm hòn đá và thước mét cân bằng trên đỉnh con đội tam giác, điểm tựa của con đội bắt buộc phải đặt trùng đúng vị trí trọng tâm của hệ.

Chọn gốc tọa độ $x = 0$ tại đầu mút bên trái của cây thước mét. Hòn đá có khối lượng $m$ nằm ở tọa độ $x_{\text{đá}} = 0$. Thước mét đồng chất có chiều dài $1{,}00\,\text{m}$ và khối lượng $m$, do đó khối tâm của riêng cây thước nằm chính giữa tại tọa độ $x_{\text{thước}} = 0{,}50\,\text{m}$.

Tọa độ trọng tâm của toàn bộ hệ hai vật là:

$$
\begin{aligned}
x_{\mathrm{cg}} &= \frac{m(0) + m(0{,}50\,\text{m})}{m + m} \\
&= \frac{0{,}50 m}{2m} = 0{,}25\,\text{m}
\end{aligned}
$$

Như vậy, con đội tam giác phải được đặt cách đầu trái của thước một khoảng đúng bằng $0{,}25\,\text{m}$.

</details>
:::
