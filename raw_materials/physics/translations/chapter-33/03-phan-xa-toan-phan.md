## 33.3. Phản xạ toàn phần

Ở mục trước, chúng ta đã thấy rằng khi ánh sáng truyền tới mặt phân cách giữa hai môi trường trong suốt có chiết suất khác nhau, chùm sáng nói chung bị phân tách: Một phần bị phản xạ và một phần bị khúc xạ truyền sang môi trường thứ hai. Tuy nhiên, trong những điều kiện hình học và vật lý nhất định, toàn bộ năng lượng ánh sáng có thể bị phản xạ hoàn toàn trở lại môi trường ban đầu mà không có bất kỳ tia khúc xạ nào truyền qua, ngay cả khi môi trường thứ hai hoàn toàn trong suốt. Hiện tượng này được gọi là **hiện tượng phản xạ toàn phần** (total internal reflection).

### Cơ chế hình thành và góc tới giới hạn

Để làm sáng tỏ cơ chế phản xạ toàn phần, xét một nguồn sáng điểm đặt trong môi trường $a$ có chiết suất $n_a$, phát ra các tia sáng truyền tới mặt phân cách với môi trường $b$ có chiết suất $n_b$ như biểu diễn ở Hình 33.13a. Điều kiện tiên quyết đầu tiên là ánh sáng phải truyền từ môi trường chiết quang hơn sang môi trường chiết quang kém hơn, tức là:

$$
n_a > n_b
$$

Theo định luật khúc xạ Snell:

$$
\sin \theta_b = \frac{n_a}{n_b} \sin \theta_a
$$

Vì tỷ số $n_a / n_b > 1$, giá trị $\sin \theta_b$ luôn lớn hơn $\sin \theta_a$, đồng nghĩa với việc góc khúc xạ $\theta_b$ luôn lớn hơn góc tới $\theta_a$ ($\theta_b > \theta_a$). Tia khúc xạ luôn lệch ra xa pháp tuyến hơn so với tia tới:

- Đối với tia 1 truyền tới với góc tới nhỏ $\theta_a$, tia sáng phân tách thành tia phản xạ một phần và tia khúc xạ truyền vào môi trường $b$.
- Khi tăng dần góc tới $\theta_a$ (tia 2), góc khúc xạ $\theta_b$ tăng nhanh hơn và tiến dần về $90^\circ$. Cường độ của tia khúc xạ giảm dần trong khi cường độ của tia phản xạ tăng lên.
- Khi góc tới đạt tới một giá trị xác định $\theta_{\text{crit}}$, góc khúc xạ đạt giá trị cực đại $\theta_b = 90^\circ$ ($\sin \theta_b = 1$). Tia khúc xạ lúc này đi là là sát mặt phân cách giữa hai môi trường (tia 3). Góc tới đặc biệt này được gọi là **góc tới giới hạn** hay góc khúc xạ giới hạn (critical angle), ký hiệu là $\theta_{\text{crit}}$.
- Nếu góc tới tiếp tục tăng vượt quá góc giới hạn ($\theta_a > \theta_{\text{crit}}$, tia 4), hệ thức Snell đòi hỏi $\sin \theta_b > 1$, điều này hoàn toàn vô nghiệm về mặt toán học. Khi đó, không thể có tia khúc xạ truyền sang môi trường $b$: Toàn bộ ánh sáng bị giữ lại và phản xạ $100\%$ tại mặt phân cách.

![Hình 33.13: Phản xạ toàn phần. Ở phần (a), các tia đi từ môi trường a tới môi trường b, với na lớn hơn nb. Tia 3 ở góc giới hạn, có góc khúc xạ bằng 90 độ. Tia 4 phản xạ toàn phần. Ở phần (b), các chùm laser phản xạ từ gương nghiêng ở đáy bể, trong đó một chùm phản xạ toàn phần tại mặt nước–không khí.](../img/young-33/hinh-33-13.png)


Ta xác định góc tới giới hạn $\theta_{\text{crit}}$ bằng cách thay $\theta_b = 90^\circ$ ($\sin \theta_b = 1$) vào định luật Snell:

$$
\sin \theta_{\text{crit}} = \frac{n_b}{n_a} \tag{33.6}
$$

Như vậy, hai điều kiện cần và đủ để xảy ra hiện tượng phản xạ toàn phần là:

1. Ánh sáng truyền từ môi trường có chiết suất lớn hơn sang môi trường có chiết suất nhỏ hơn ($n_a > n_b$).
2. Góc tới phải lớn hơn hoặc bằng góc tới giới hạn ($\theta_a \ge \theta_{\text{crit}}$).

### Ứng dụng của hiện tượng phản xạ toàn phần

Hiện tượng phản xạ toàn phần được ứng dụng sâu rộng trong kỹ thuật quang học hiện đại:

#### 1. Lăng kính phản xạ toàn phần và ống nhòm

Xét khối thủy tinh có chiết suất $n = 1{,}52$ đặt trong không khí ($n = 1{,}00$). Góc tới giới hạn tại mặt phân cách thủy tinh - không khí là:

$$
\begin{aligned}
\sin \theta_{\text{crit}} &= \frac{1{,}00}{1{,}52} \approx 0{,}658 \\
&\implies \theta_{\text{crit}} \approx 41{,}1^\circ
\end{aligned}
$$

Ánh sáng truyền trong khối thủy tinh sẽ bị phản xạ toàn phần nếu đập vào mặt phân cách thủy tinh - không khí ở góc tới bằng hoặc lớn hơn $41{,}1^\circ$. Vì góc tới giới hạn này nhỏ hơn $45^\circ$, ta có thể sử dụng một lăng kính có các góc $45^\circ-45^\circ-90^\circ$ làm bề mặt phản xạ toàn phần. Một lăng kính $45^\circ-45^\circ-90^\circ$, được sử dụng như ở Hình 33.14a, được gọi là **lăng kính Porro**. Ánh sáng đi vào và đi ra vuông góc với cạnh huyền, và phản xạ toàn phần tại từng mặt góc vuông ngắn hơn. Sự đổi hướng tổng cộng của các tia sáng là $180^\circ$. Ống nhòm thường sử dụng các tổ hợp gồm hai lăng kính Porro, như ở Hình 33.14b.

![Hình 33.14: Ứng dụng lăng kính Porro. (a) Phản xạ toàn phần trong lăng kính Porro làm đổi hướng tia sáng 180 độ. (b) Hệ hai lăng kính Porro trong ống nhòm giúp đảo ngược chiều ảnh và rút ngắn chiều dài thân ống nhòm.](../img/young-33/hinh-33-14.png)


Với vai trò là gương phản xạ, các lăng kính phản xạ toàn phần có một số ưu điểm so với bề mặt kim loại như gương kính tráng bạc thông thường. Trong khi không có bề mặt kim loại nào phản xạ được $100\%$ lượng ánh sáng chiếu tới nó, ánh sáng có thể bị phản xạ toàn phần lý tưởng tại các mặt phân cách bên trong lăng kính. Đặc tính phản xạ này của lăng kính không bị suy giảm do sự xỉn màu bề mặt theo thời gian. Tuy nhiên, tại các mặt cạnh huyền nơi ánh sáng đi vào và đi ra khỏi lăng kính, vẫn có thể có một phần nhỏ năng lượng bị thất thoát do phản xạ bề mặt.

#### 2. Ống dẫn sáng và sợi quang học

Thanh thủy tinh hoặc nhựa trong có thể giữ ánh sáng nhờ những lần phản xạ toàn phần tại thành bên (Hình 33.15). Chiết suất thanh phải lớn hơn môi trường ngoài, và mỗi góc tới phải đạt điều kiện phản xạ. Thanh có thể uốn cong, nhưng uốn quá gắt sẽ làm một số tia rò ra.

![Hình 33.15: Thanh dẫn sáng trong suốt có chiết suất lớn hơn môi trường bao quanh. Ánh sáng bị giữ lại bên trong thanh nếu mọi góc tới tại thành bên (như alpha, beta, gamma) đều lớn hơn góc giới hạn.](../img/young-33/hinh-33-15.png)


Một bó gồm hàng nghìn sợi thủy tinh hoặc sợi nhựa có đường kính rất nhỏ (khoảng $0{,}002\,\mathrm{mm}$ đến $0{,}01\,\mathrm{mm}$) ghép song song tạo thành **cáp sợi quang** (fiber-optic cable). Nếu các đầu sợi được sắp xếp trật tự tương ứng chính xác ở cả hai đầu, bó sợi có thể truyền tải nguyên vẹn hình ảnh quang học từ đầu này sang đầu kia.

Thiết bị này được ứng dụng rộng rãi trong y học thông qua các **ống nội soi** (endoscope). Bác sĩ có thể luồn ống nội soi mềm vào phế quản, bàng quang, đại tràng và các cơ quan khác để quan sát trực tiếp bề mặt niêm mạc bên trong cơ thể người (Hình 33.16). Một bó sợi quang thậm chí có thể được lồng vào bên trong một kim tiêm dưới da để khảo sát các mô và mạch máu nằm sâu dưới da.

![Hình 33.16: Ảnh chụp X-quang bụng có màu của một bệnh nhân, thể hiện đường ống nội soi mềm uốn lượn qua đại tràng phục vụ chẩn đoán hình ảnh.](../img/young-33/hinh-33-16.png)

Sợi quang cũng có các ứng dụng quan trọng trong hệ thống truyền thông:

- Tốc độ truyền tải thông tin của một sóng (ánh sáng, vô tuyến hay bất kỳ dạng sóng nào) tỷ lệ thuận với tần số dao động. Để thấy rõ điều này một cách định tính, hãy xét việc điều biến sóng bằng cách cắt bỏ một số đỉnh sóng. Giả sử mỗi đỉnh sóng đại diện cho một chữ số nhị phân, trong đó một đỉnh bị cắt đại diện cho số 0 và một đỉnh nguyên vẹn đại diện cho số 1. Số lượng chữ số nhị phân có thể truyền đi trong một đơn vị thời gian do đó tỷ lệ thuận với tần số của sóng. Sóng hồng ngoại và sóng ánh sáng nhìn thấy có tần số cao hơn rất nhiều so với sóng vô tuyến, vì vậy một chùm tia laser được điều biến có thể truyền tải một lượng thông tin khổng lồ qua một sợi cáp quang duy nhất.
- Một ưu điểm khác của sợi quang là chúng có thể được chế tạo mỏng hơn dây đồng thông thường, cho phép ghép nhiều sợi quang hơn trong một sợi cáp có đường kính cho trước. Nhờ đó, nhiều tín hiệu độc lập hơn (chẳng hạn các đường dây điện thoại khác nhau) có thể được truyền trên cùng một sợi cáp.
- Do cáp sợi quang là các chất cách điện, chúng miễn nhiễm với hiện tượng nhiễu điện từ sét đánh và các nguồn điện khác, đồng thời không cho phép các dòng điện không mong muốn chạy giữa nguồn phát và bộ thu tín hiệu. Vì những lý do này và nhiều ưu điểm khác, cáp sợi quang đóng vai trò cốt lõi trong thông tin liên lạc đường dài của điện thoại, truyền hình và mạng Internet.

#### 3. Độ lấp lánh của kim cương

Kim cương tự nhiên có chiết suất rất cao ($n = 2{,}417$). Do đó, góc tới giới hạn tại mặt phân cách giữa kim cương và không khí nhỏ:

$$
\begin{aligned}
\sin \theta_{\text{crit}} &= \frac{1{,}00}{2{,}417} \\
&\approx 0{,}4137 \\
&\implies \theta_{\text{crit}} \approx 24{,}4^\circ
\end{aligned}
$$

Khi ánh sáng đi vào mặt trước của một viên kim cương đã được cắt giác theo các góc độ hình học tối ưu, phần lớn các tia sáng đập vào các mặt giác ở đáy với góc tới lớn hơn $24{,}4^\circ$. Do đó, ánh sáng bị phản xạ toàn phần nhiều lần ở mặt đáy rồi mới khúc xạ thoát ra ngoài qua các mặt giác ở phía trên, tạo nên độ sáng bóng và lấp lánh rực rỡ đặc trưng của kim cương. Các loại đá giả kim cương như zirconia khối ($\mathrm{ZrO_2}$) cũng được chế tạo từ các tinh thể nhân tạo có chiết suất xấp xỉ cao tương đương.

### Ví dụ 33.4: Kính tiềm vọng bị rò rỉ nước

Kính tiềm vọng của tàu ngầm sử dụng hai lăng kính phản xạ toàn phần $45^\circ-45^\circ-90^\circ$ bằng thủy tinh ($n_a = 1{,}52$) đặt trong không khí ($n_b = 1{,}00$) để đổi hướng tia sáng hai lần. Hãy giải thích tại sao kính tiềm vọng sẽ không còn hoạt động được nếu vỏ ngoài bị nứt rò rỉ và nước biển ($n = 1{,}33$) tràn vào làm ngập lăng kính bên dưới.

**Lời giải**: Khi lăng kính đặt trong không khí, góc tới giới hạn là:

$$
\begin{aligned}
\theta_{\text{crit, kk}} &= \arcsin\left(\frac{1{,}00}{1{,}52}\right) \\
&\approx 41{,}1^\circ
\end{aligned}
$$

Vì góc tới tại mặt góc vuông là $\theta_a = 45^\circ > 41{,}1^\circ$, hiện tượng phản xạ toàn phần xảy ra hoàn hảo.

Tuy nhiên, khi nước tràn vào ngập bề mặt lăng kính, môi trường ngoài lúc này là nước ($n_b = 1{,}33$). Góc tới giới hạn mới tại mặt phân cách thủy tinh - nước là:

$$
\begin{aligned}
\\theta_{\mathrm{crit,water}} &= \arcsin\left(\frac{1{,}33}{1{,}52}\right) \\
&= \arcsin(0{,}875) \\
&\approx 61{,}0^\circ
\end{aligned}
$$

Góc tới $\theta_a = 45^\circ$ nhỏ hơn góc tới giới hạn mới này ($45^\circ < 61{,}0^\circ$). Do đó, điều kiện phản xạ toàn phần không còn được thỏa mãn tại mặt phân cách thủy tinh - nước: Phần lớn ánh sáng bị khúc xạ truyền vào trong nước, và chỉ có một lượng rất nhỏ ánh sáng bị phản xạ trở lại lăng kính. Kết quả là hình ảnh quan sát được qua kính tiềm vọng bị mờ đi rất nhiều  và thiết bị gần như mất tác dụng.

**Nội dung cần nhớ**: Phản xạ toàn phần cần $n_a>n_b$ và góc tới vượt góc giới hạn. Ngưỡng góc phụ thuộc tỉ số $n_b/n_a$.

### Câu hỏi tự kiểm tra 33.3

Trong các trường hợp nào sau đây sẽ xảy ra hiện tượng phản xạ toàn phần?

- (i) Ánh sáng truyền trong nước ($n = 1{,}33$) truyền tới mặt phân cách nước - không khí với góc tới bằng $70^\circ$.

- (ii) Ánh sáng truyền trong thủy tinh ($n = 1{,}52$) truyền tới mặt phân cách thủy tinh - nước với góc tới bằng $70^\circ$.

- (iii) Ánh sáng truyền trong nước truyền tới mặt phân cách nước - thủy tinh với góc tới bằng $70^\circ$.

<details><summary>Xem đáp án và giải thích</summary>

Chọn (i) và (ii).

Giải thích: Hiện tượng phản xạ toàn phần chỉ xảy ra khi thỏa mãn đồng thời hai điều kiện: Chiết suất môi trường chứa tia tới phải lớn hơn chiết suất môi trường thứ hai ($n_a > n_b$), và góc tới phải lớn hơn góc tới giới hạn ($\theta_a > \theta_{\text{crit}}$).

- Ở trường hợp (i): Ánh sáng truyền từ nước ($n_a = 1{,}33$) sang không khí ($n_b = 1{,}00$). Ta có $n_a > n_b$ và góc giới hạn $\theta_{\text{crit}} \approx 48{,}8^\circ$ (tính từ $\sin\theta_{\text{crit}} = 1{,}00 / 1{,}33$). Vì góc tới $\theta_a = 70^\circ > 48{,}8^\circ$, hiện tượng phản xạ toàn phần xảy ra.
- Ở trường hợp (ii): Ánh sáng truyền từ thủy tinh ($n_a = 1{,}52$) sang nước ($n_b = 1{,}33$). Ta có $n_a > n_b$ và góc giới hạn $\theta_{\text{crit}} \approx 61{,}0^\circ$ (tính từ $\sin\theta_{\text{crit}} = 1{,}33 / 1{,}52$). Vì góc tới $\theta_a = 70^\circ > 61{,}0^\circ$, hiện tượng phản xạ toàn phần xảy ra.
- Ở trường hợp (iii): Ánh sáng truyền từ nước ($n_a = 1{,}33$) sang thủy tinh ($n_b = 1{,}52$). Vì $n_a < n_b$, ánh sáng truyền sang môi trường chiết quang hơn nên không bao giờ xảy ra hiện tượng phản xạ toàn phần ở bất kỳ góc tới nào.

</details>
