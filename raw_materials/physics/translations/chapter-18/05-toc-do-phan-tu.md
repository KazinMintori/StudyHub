## 18.5 Tốc độ phân tử

Trong mô hình động học phân tử cơ sở, chúng ta đã tính toán tốc độ căn quân phương $v_{\mathrm{rms}}$ của các phân tử khí. Tuy nhiên, các phân tử trong một khối khí thực không hề chuyển động với cùng một tốc độ duy nhất. Các va chạm hỗn loạn liên tục giữa các phân tử làm vận tốc của từng hạt biến thiên không ngừng, tạo nên một dải phân bố tốc độ rộng từ rất nhỏ đến rất lớn.

### Phép đo thực nghiệm phân bố tốc độ

Hình 18.22 mô tả một phương pháp thực nghiệm kinh điển dùng để đo trực tiếp phân bố tốc độ của các phân tử khí. Một chất được hóa hơi bên trong lò nung ở nhiệt độ xác định. Các phân tử khí thoát ra ngoài qua một lỗ nhỏ trên thành lò và đi vào buồng chân không cao.

Hệ thống các khe chuẩn trực hẹp chặn đứng hầu hết các phân tử lệch hướng, chỉ cho phép một chùm phân tử song song hẹp đi qua và hướng thẳng vào một cặp đĩa đồng trục đang quay tròn. Hai đĩa đặt cách nhau một khoảng cách $x$ và được gắn trên cùng một trục quay với tốc độ góc $\omega$. Khe hở trên đĩa thứ hai được đặt lệch một góc $\theta$ so với khe hở trên đĩa thứ nhất.

![Hình 18.22: Phân tử bay qua khe trên đĩa quay thứ nhất với tốc độ $v$. Khi phân tử bay tới đĩa thứ hai sau quãng đường $x$, hệ hai đĩa đã quay được góc $\theta = \omega t$. Nếu tốc độ thỏa mãn $v = \omega x / \theta$, phân tử sẽ lọt qua khe thứ hai và đi tới đầu dò.](../img/young-18/b-hinh-18-22.png)

Thời gian cần thiết để một phân tử có tốc độ $v$ bay hết khoảng cách $x$ giữa hai đĩa là:

$$
t = \frac{x}{v}
$$

Trong khoảng thời gian $t$ đó, hai đĩa đã quay được một góc:

$$
\theta = \omega t = \frac{\omega x}{v}
$$

Hệ thống hoạt động như một bộ lọc lựa chọn tốc độ: Chỉ những phân tử có tốc độ thỏa mãn điều kiện lọt qua cả hai khe:

$$
v = \frac{\omega x}{\theta}
$$

mới có thể đến được đầu dò để ghi nhận số lượng. Bằng cách thay đổi tốc độ quay $\omega$ của động cơ, ta có thể đo đạc chính xác số lượng phân tử có tốc độ nằm trong từng khoảng hẹp khác nhau.

### Hàm phân bố tốc độ

Để mô tả kết quả đo đạc phân bố tốc độ một cách toán học, ta định nghĩa hàm phân bố $f(v)$. Nếu tổng số phân tử quan sát được trong khối khí là $N$, thì số phân tử $dN$ có tốc độ nằm trong khoảng hẹp từ $v$ đến $v + dv$ được biểu diễn bởi:

$$
dN = N f(v)\,dv \tag{18.29}
$$

Xác suất để một phân tử bất kỳ được chọn ngẫu nhiên có tốc độ nằm trong khoảng từ $v$ đến $v + dv$ bằng $f(v)\,dv$. Do đó, $f(v)$ chính là mật độ xác suất trên một đơn vị khoảng tốc độ. Đại lượng $f(v)$ không phải là xác suất để phân tử có tốc độ chính xác bằng $v$, bởi vì xác suất tại một điểm vận tốc đơn lẻ trong biến số liên tục luôn bằng không. Vì xác suất là một số thuần túy không có thứ nguyên, đơn vị đo của hàm phân bố $f(v)$ là nghịch đảo của tốc độ: $\mathrm{s/m}$.

![Hình 18.23: Phân bố tốc độ và các khoảng xác suất. (a) Các đường cong phân bố Maxwell–Boltzmann $f(v)$ ở ba nhiệt độ khác nhau ($T_3 > T_2 > T_1$). Khi nhiệt độ tăng, đỉnh cực đại dịch sang phía tốc độ cao hơn và đường cong dẹt dần. (b) Diện tích dưới đường cong giữa hai giá trị $v_1$ và $v_2$ tương ứng với tỷ lệ phân tử có tốc độ trong khoảng này. Tốc độ có xác suất lớn nhất $v_{\mathrm{mp}}$ nằm tại đỉnh của đường cong.](../img/young-18/b-hinh-18-23.png)

Hình 18.23a thể hiện hàm phân bố tốc độ ở ba giá trị nhiệt độ khác nhau. Tại mỗi nhiệt độ, độ cao của đường cong ở một giá trị $v$ bất kỳ tỷ lệ thuận với số lượng phân tử có tốc độ lân cận $v$. Đỉnh của đường cong ứng với tốc độ có xác suất lớn nhất, ký hiệu là $v_{\mathrm{mp}}$ (most probable speed). Khi nhiệt độ tăng lên, động năng phân tử trung bình tăng làm đỉnh của $f(v)$ dịch chuyển về phía các giá trị tốc độ cao hơn, đồng thời đường cong trải rộng và hạ thấp xuống.

Hình 18.23b cho thấy diện tích dưới đường cong giữa hai giá trị $v_1$ và $v_2$ đại diện cho tỷ lệ của toàn bộ số phân tử sở hữu tốc độ trong khoảng đó. Vì mọi phân tử đều phải có một tốc độ xác định nào đó trong khoảng từ $0$ đến $\infty$, tích phân của $f(v)$ trên toàn miền xác định bắt buộc phải bằng $1$ (điều kiện chuẩn hóa):

$$
\int_0^\infty f(v)\,dv = 1
$$

Từ hàm phân bố $f(v)$, ta có thể tính toán ba giá trị tốc độ đặc trưng quan trọng:
1. **Tốc độ có xác suất lớn nhất $v_{\mathrm{mp}}$**: Là vị trí đỉnh của đường cong phân bố, được xác định bằng phương trình đạo hàm:

$$
\frac{df(v)}{dv} = 0
$$

2. **Tốc độ trung bình $v_{\mathrm{av}}$**: Lấy số phân tử $N f(v)\,dv$ có tốc độ trong khoảng $dv$, nhân với tốc độ $v$, tích phân trên toàn miền từ $0$ đến $\infty$, rồi chia cho tổng số hạt $N$:

$$
v_{\mathrm{av}} = \int_0^\infty v f(v)\,dv \tag{18.30}
$$

3. **Tốc độ căn quân phương $v_{\mathrm{rms}}$**: Trước hết tính trung bình của bình phương tốc độ:

$$
(v^2)_{\mathrm{av}} = \int_0^\infty v^2 f(v)\,dv \tag{18.31}
$$

và lấy căn bậc hai:

$$
v_{\mathrm{rms}} = \sqrt{(v^2)_{\mathrm{av}}}
$$

### Phân bố Maxwell–Boltzmann

Hàm giải tích mô tả chính xác phân bố tốc độ của các phân tử trong chất khí lý tưởng ở trạng thái cân bằng nhiệt động được gọi là **phân bố Maxwell–Boltzmann**. Đặt hệ số chuẩn hóa:

$$
C = 4\pi \left(\frac{m}{2\pi kT}\right)^{3/2}
$$

Khi đó, hàm phân bố tốc độ có dạng:

$$
f(v) = C v^2 e^{-mv^2/(2kT)} \tag{18.32}
$$

Ở đây, $m$ là khối lượng của một phân tử khí, $k$ là hằng số Boltzmann, và $T$ là nhiệt độ tuyệt đối của khối khí.

Động năng tịnh tiến của một phân tử là $\epsilon=mv^2/2$. Ta có thể dùng $\epsilon$ để ghi lại cùng đường cong mật độ theo tốc độ. Đặt:

$$
C_\epsilon=\frac{8\pi}{m}
\left(\frac{m}{2\pi kT}\right)^{3/2}.
$$

Sau khi thay $v^2=2\epsilon/m$ vào biểu thức của $f(v)$, ta được:

$$
g(\epsilon)=C_\epsilon\epsilon e^{-\epsilon/(kT)}. \tag{18.33}
$$

Ở đây, $g(\epsilon)$ là giá trị của $f(v)$ tại tốc độ tương ứng với năng lượng $\epsilon$. Nó vẫn có đơn vị $\mathrm{s/m}$, nên không phải mật độ xác suất trên một đơn vị năng lượng. Biểu thức này cho thấy vai trò của tỷ số $\epsilon/(kT)$ trong thừa số mũ.

Đạo hàm của $\epsilon e^{-\epsilon/(kT)}$ bằng không tại $\epsilon=kT$. Do đó, đỉnh của mật độ theo tốc độ ứng với:

$$
v_{\mathrm{mp}}=\sqrt{\frac{2kT}{m}}. \tag{18.34}
$$

Nếu cần xác suất trong một khoảng năng lượng, phải tính cả hệ số đổi biến $dv/d\epsilon$. Gọi mật độ theo năng lượng là $h(\epsilon)$. Khi đó:

$$
h(\epsilon)\,d\epsilon=f(v)\,dv,
$$

$$
\frac{dv}{d\epsilon}=\frac{1}{mv}.
$$

Đặt $B=2/[\sqrt{\pi}(kT)^{3/2}]$, ta được:

$$
h(\epsilon)=B\sqrt{\epsilon}\,e^{-\epsilon/(kT)}.
$$

Đỉnh của mật độ này ở $\epsilon=kT/2$. Hai vị trí cực đại khác nhau vì mật độ được tính trên hai loại khoảng khác nhau, một theo tốc độ và một theo năng lượng.

Hoặc viết theo hằng số khí lý tưởng $R$ và khối lượng mol $M = N_A m$:

$$
v_{\mathrm{mp}} = \sqrt{\frac{2RT}{M}}
$$

Để xác định tốc độ trung bình, ta thay phương trình (18.32) vào phương trình (18.30), thực hiện đổi biến tích phân và tích phân từng phần:

$$
v_{\mathrm{av}} = \sqrt{\frac{8kT}{\pi m}} = \sqrt{\frac{8RT}{\pi M}} \tag{18.35}
$$

Cuối cùng, thay phương trình (18.32) vào phương trình (18.31) để tính tốc độ căn quân phương:

$$
v_{\mathrm{rms}} = \sqrt{\frac{3kT}{m}} = \sqrt{\frac{3RT}{M}} \tag{18.36}
$$

Kết quả giải tích (18.36) hoàn toàn trùng khớp với biểu thức mà chúng ta đã thu được từ thuyết động học phân tử cơ sở.

So sánh hệ số của ba giá trị tốc độ đặc trưng:
- Tốc độ có xác suất lớn nhất: $\sqrt{2} \approx 1{,}414$
- Tốc độ trung bình: $\sqrt{8/\pi} \approx 1{,}596$
- Tốc độ căn quân phương: $\sqrt{3} \approx 1{,}732$

Mối quan hệ thứ tự giữa ba giá trị tốc độ này luôn thỏa mãn:

$$
v_{\mathrm{mp}} < v_{\mathrm{av}} < v_{\mathrm{rms}}
$$

Có thể thấy rõ ba hệ số khi chọn tốc độ chuẩn $u=\sqrt{kT/m}$:

$$
\begin{aligned}
v_{\mathrm{mp}}&=\sqrt{2}\,u,\\
v_{\mathrm{av}}&=\sqrt{8/\pi}\,u,\\
v_{\mathrm{rms}}&=\sqrt{3}\,u.
\end{aligned}
$$

Bảng 18.2 trình bày tỷ lệ số lượng phân tử có tốc độ nhỏ hơn các bội số khác nhau của $v_{\mathrm{rms}}$, được tính toán bằng phương pháp tích phân số trị cho mọi chất khí lý tưởng:

**Bảng 18.2: Tỷ lệ phân tử trong khí lý tưởng có tốc độ nhỏ hơn các bội số của $v_{\mathrm{rms}}$**

<div class="lecture-data-table">

| Tỷ số $v / v_{\mathrm{rms}}$ | Tỷ lệ phân tử tích lũy |
| --- | --- |
| <span class="table-cell-label">Tỷ số $v / v_{\mathrm{rms}}$</span> $0{,}20$ | <span class="table-cell-label">Tỷ lệ phân tử tích lũy</span> $0{,}011$ ($1{,}1\%$) |
| <span class="table-cell-label">Tỷ số $v / v_{\mathrm{rms}}$</span> $0{,}40$ | <span class="table-cell-label">Tỷ lệ phân tử tích lũy</span> $0{,}077$ ($7{,}7\%$) |
| <span class="table-cell-label">Tỷ số $v / v_{\mathrm{rms}}$</span> $0{,}60$ | <span class="table-cell-label">Tỷ lệ phân tử tích lũy</span> $0{,}218$ ($21{,}8\%$) |
| <span class="table-cell-label">Tỷ số $v / v_{\mathrm{rms}}$</span> $0{,}80$ | <span class="table-cell-label">Tỷ lệ phân tử tích lũy</span> $0{,}411$ ($41{,}1\%$) |
| <span class="table-cell-label">Tỷ số $v / v_{\mathrm{rms}}$</span> $1{,}00$ | <span class="table-cell-label">Tỷ lệ phân tử tích lũy</span> $0{,}608$ ($60{,}8\%$) |
| <span class="table-cell-label">Tỷ số $v / v_{\mathrm{rms}}$</span> $1{,}20$ | <span class="table-cell-label">Tỷ lệ phân tử tích lũy</span> $0{,}771$ ($77{,}1\%$) |
| <span class="table-cell-label">Tỷ số $v / v_{\mathrm{rms}}$</span> $1{,}40$ | <span class="table-cell-label">Tỷ lệ phân tử tích lũy</span> $0{,}882$ ($88{,}2\%$) |
| <span class="table-cell-label">Tỷ số $v / v_{\mathrm{rms}}$</span> $1{,}60$ | <span class="table-cell-label">Tỷ lệ phân tử tích lũy</span> $0{,}947$ ($94{,}7\%$) |
| <span class="table-cell-label">Tỷ số $v / v_{\mathrm{rms}}$</span> $1{,}80$ | <span class="table-cell-label">Tỷ lệ phân tử tích lũy</span> $0{,}979$ ($97{,}9\%$) |
| <span class="table-cell-label">Tỷ số $v / v_{\mathrm{rms}}$</span> $2{,}00$ | <span class="table-cell-label">Tỷ lệ phân tử tích lũy</span> $0{,}993$ ($99{,}3\%$) |

</div>

Từ kết quả tích phân số: Tại mốc $v = v_{\mathrm{rms}}$, có khoảng $60{,}8\%$ số lượng phân tử có tốc độ nhỏ hơn $v_{\mathrm{rms}}$, và chỉ có $39{,}2\%$ số phân tử có tốc độ lớn hơn $v_{\mathrm{rms}}$. Điều này bắt nguồn từ sự bất đối xứng của hàm phân bố Maxwell–Boltzmann với phần đuôi dài kéo dài về phía các giá trị tốc độ cao.

### Ứng dụng: Sự bay hơi và tốc độ phản ứng hóa học

Phân bố tốc độ phân tử trong chất lỏng có dạng tương tự, nhưng không hoàn toàn giống trong chất khí. Phân bố này giúp giải thích cơ chế bay hơi và sự hình thành áp suất hơi bão hòa.

Để một phân tử chất lỏng có thể thắng được lực hút liên kết của các phân tử xung quanh và thoát ra ngoài bề mặt tạo thành pha hơi, nó phải sở hữu một tốc độ tối thiểu $v_A$ nào đó (xem Hình 18.23b). Số lượng các phân tử có tốc độ vượt qua ngưỡng $v_A$ này được biểu diễn bởi diện tích phần đuôi của đường cong phân bố về phía bên phải của $v_A$. Khi nhiệt độ tăng, diện tích phần đuôi này tăng nhanh, nên tốc độ bay hơi tăng theo nhiệt độ trong mô hình này.

Mặt khác, các phân tử hơi bên ngoài cũng liên tục va chạm không đàn hồi với bề mặt chất lỏng và bị giữ lại. Trạng thái cân bằng pha lỏng–hơi được thiết lập khi tốc độ phân tử thoát ra ngoài bằng đúng tốc độ phân tử hơi bị ngưng tụ trở lại. Khi chất lỏng bay hơi, những phân tử có tốc độ lớn nhất mang nhiều năng lượng nhất thoát đi trước, khiến năng lượng trung bình của các phân tử còn lại giảm xuống. Sự giảm năng lượng trung bình này giải thích hiện tượng làm mát do bay hơi.

Tương tự, tốc độ của các phản ứng hóa học cũng phụ thuộc mạnh vào nhiệt độ do phân bố Maxwell–Boltzmann. Để phản ứng hóa học xảy ra khi hai phân tử va chạm, các đám mây electron của chúng phải tương tác đủ mạnh. Quá trình này đòi hỏi một ngưỡng năng lượng tối thiểu gọi là **năng lượng hoạt hóa** ($E_a$).

Chỉ những phân tử ở phần đuôi tốc độ cao mới sở hữu động năng vượt qua năng lượng hoạt hóa này. Vì tỷ lệ phân tử ở phần đuôi tăng rất nhanh theo nhiệt độ thông qua thừa số Boltzmann $e^{-E_a/(kT)}$, tốc độ phản ứng hóa học thường tăng mạnh khi nhiệt độ tăng.

![Ứng dụng sinh học: Loài bướm đêm thuộc chi Manduca không thể cất cánh bay nếu nhiệt độ cơ bắp của nó thấp hơn $29^\circ\mathrm{C}$. Nguyên nhân là các phản ứng sinh hóa hiếu khí xúc tác bởi enzyme cung cấp năng lượng cho cơ bay đòi hỏi một mức năng lượng hoạt hóa tối thiểu. Ở nhiệt độ thấp, rất ít phân tử đạt ngưỡng năng lượng này. Khi nhiệt độ vượt quá $29^\circ\mathrm{C}$, tốc độ phản ứng tăng mạnh giúp tạo ra đủ công suất cần thiết cho hoạt động bay.](../img/young-18/b-ung-dung-18-01.png)

::: info Câu hỏi kiểm tra mức độ hiểu mục 18.5
Một lượng khí chứa $N$ phân tử có hàm phân bố tốc độ $f(v)$. Số phân tử có tốc độ từ $v_1$ đến $v_2$, với $v_2>v_1$, bằng bao nhiêu?

Để trình bày gọn các lựa chọn, gọi $F(v)$ là tỷ lệ phân tử có tốc độ không vượt quá $v$:

$$
F(v)=\int_0^v f(u)\,du.
$$

- (i) $F(v_2)-F(v_1)$.
- (ii) $N[F(v_2)-F(v_1)]$.
- (iii) $F(v_1)-F(v_2)$.
- (iv) $N[F(v_1)-F(v_2)]$.
- (v) Không có lựa chọn nào ở trên.

<details>
<summary>Xem lời giải thích</summary>

**Đáp án:** (ii).

**Hướng đi:**

- Diện tích dưới đường cong mật độ cho tỷ lệ phân tử trong khoảng tốc độ đang xét.
- Nhân tỷ lệ đó với tổng số phân tử $N$ để có số lượng phân tử.

**Lời giải:**

Theo tính cộng đoạn của tích phân:

$$
\begin{aligned}
\Delta P&=\int_{v_1}^{v_2}f(v)\,dv\\
&=F(v_2)-F(v_1).
\end{aligned}
$$

Trong hiệu này, $F(v_2)$ tính cả các phân tử có tốc độ nhỏ hơn $v_1$. Trừ $F(v_1)$ sẽ chỉ giữ lại phần nằm giữa hai tốc độ. Vì vậy:

$$
\begin{aligned}
\Delta N&=N\Delta P\\
&=N[F(v_2)-F(v_1)].
\end{aligned}
$$

Lựa chọn (i) chỉ là tỷ lệ. Các lựa chọn (iii) và (iv) đảo thứ tự hai cận nên cho hiệu không dương.
</details>
:::
