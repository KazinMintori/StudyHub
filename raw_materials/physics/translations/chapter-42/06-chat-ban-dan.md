## 42.6 Chất bán dẫn

Chất bán dẫn giữ vai trò nền tảng trong toàn bộ nền văn minh công nghệ hiện đại. Về mặt dẫn điện, điện trở suất của chất bán dẫn nằm ở khoảng trung gian giữa kim loại dẫn điện tốt và chất cách điện. Tuy nhiên, sự khác biệt căn bản nhất giữa kim loại và chất bán dẫn không chỉ nằm ở độ lớn của điện trở suất, mà thể hiện rõ nét ở sự phụ thuộc của điện trở suất vào nhiệt độ.

Ở kim loại, điện trở suất tăng dần khi nhiệt độ tăng do mạng tinh thể dao động mạnh hơn và tán xạ các electron dẫn. Trái lại, ở chất bán dẫn thuần, điện trở suất giảm rất nhanh khi nhiệt độ tăng, đồng nghĩa với việc độ dẫn điện tăng vọt theo nhiệt độ. Để hiểu thấu đáo hành vi này, ta cần khảo sát cấu trúc dải năng lượng và cơ chế kích thích nhiệt của các hạt mang điện.

### Cấu trúc dải năng lượng của chất bán dẫn thuần

Xét hai nguyên tố bán dẫn kinh điển thuộc nhóm IV trong bảng tuần hoàn là Silicon ($\mathrm{Si}$, $Z = 14$) và Germanium ($\mathrm{Ge}$, $Z = 32$). Mỗi nguyên tử có bốn electron hóa trị và liên kết với bốn nguyên tử lân cận thông qua các liên kết cộng hóa trị để tạo nên cấu trúc tinh thể dạng kim cương.

![Hình 42.24: Cấu trúc dải năng lượng của chất bán dẫn thuần](../img/young-42/hinh-42-24.png)

Ở nhiệt độ không độ tuyệt đối ($T = 0\,\mathrm{K}$): Toàn bộ các electron hóa trị đều tham gia trọn vẹn vào các liên kết cộng hóa trị. Trên bức tranh năng lượng dải:
- Dải hóa trị (valence band) phía dưới được điền đầy hoàn toàn.
- Dải dẫn (conduction band) phía trên hoàn toàn trống rỗng.
- Hai dải này cách nhau bởi một dải cấm hẹp có độ rộng $E_g$ (thường vào khoảng $1\,\mathrm{eV}$).

Độ rộng dải cấm ở nhiệt độ phòng ($300\,\mathrm{K}$) có giá trị thực nghiệm:
- Đối với Silicon: $E_g = 1{,}12\,\mathrm{eV}$.
- Đối với Germanium: $E_g = 0{,}67\,\mathrm{eV}$.

So sánh với chất cách điện như kim cương tinh khiết ($E_g = 5{,}47\,\mathrm{eV}$): Dải cấm của Silicon và Germanium hẹp hơn rất nhiều. Khoảng cách hẹp này cho phép các electron ở đỉnh dải hóa trị nhận năng lượng dao động nhiệt để nhảy qua dải cấm lên dải dẫn khi nhiệt độ tăng lên.

Trong chất bán dẫn thuần tinh khiết, mức năng lượng Fermi $E_F$ nằm gần chính giữa dải cấm. Khi kích thích nhiệt đưa một electron từ đỉnh dải hóa trị vượt qua dải cấm lên đáy dải dẫn, năng lượng cần thiết tối thiểu xấp xỉ bằng $E_g$. Do $E_F$ nằm ở trung tâm dải cấm, khoảng cách năng lượng từ mức Fermi đến đáy dải dẫn là:

$$
E - E_F \approx \frac{E_g}{2}
$$

### Cơ chế dẫn điện: Electron dẫn và lỗ trống

Khi một electron được kích thích nhiệt vượt qua dải cấm lên dải dẫn, hai hệ quả xảy ra đồng thời:
1. Electron tại dải dẫn: Electron này chiếm một trạng thái lượng tử trong một dải hầu như còn trống rỗng. Khi có điện trường ngoài tác dụng, electron dễ dàng nhận thêm động năng và trôi ngược chiều điện trường, tạo nên dòng điện của các hạt mang điện âm.
2. Lỗ trống tại dải hóa trị: Việc electron rời đi để lại một trạng thái lượng tử chưa được lấp đầy trong dải hóa trị, gọi là một lỗ trống (hole). Khi một electron lân cận trong dải hóa trị dịch chuyển sang lấp vào vị trí khuyết này dưới tác dụng của điện trường, khoảng trống lại dời sang vị trí ban đầu của electron đó.

![Hình 42.25: Chuyển động của electron dẫn và lỗ trống dưới tác dụng của điện trường](../img/young-42/hinh-42-25.png)

Dưới tác dụng của điện trường ngoài $\vec{E}$:
- Các electron tự do trong dải dẫn chuyển động ngược chiều điện trường.
- Các electron liên kết trong dải hóa trị dịch chuyển nối tiếp nhau, làm cho lỗ trống di chuyển cùng chiều điện trường.

Một lỗ trống hành xử hoàn toàn tương đương với một hạt mang điện tích dương $+e$. Dòng điện tổng cộng trong chất bán dẫn thuần là tổng hợp của hai dòng hạt: Dòng electron mang điện âm trôi ngược chiều điện trường và dòng lỗ trống mang điện tích dương trôi cùng chiều điện trường. Cả hai dòng điện tích này đều đóng góp cùng chiều vào mật độ dòng điện tổng cộng.

Một mô hình so sánh trực quan giúp nắm bắt bản chất hiện tượng này là bãi đỗ xe hai tầng: Tầng một chứa xe chật kín không còn một chỗ trống, còn tầng hai hoàn toàn trống rỗng. Chừng nào toàn bộ các xe còn ở tầng một thì không một xe nào có thể lăn bánh. Nếu một chiếc xe được đưa lên tầng hai, chiếc xe đó có thể chạy tự do trên sàn trống (tương tự electron trong dải dẫn). Đồng thời, khoảng trống để lại ở tầng một cho phép các xe khác dịch chuyển vào vị trí khuyết, khiến khoảng trống di chuyển ngược chiều xe chạy (tương tự lỗ trống trong dải hóa trị).

### Ví dụ 42.9: Nhảy qua dải cấm

**Đề bài**:

Dùng hàm phân bố Fermi–Dirac để tính xác suất một trạng thái lượng tử ở đáy dải dẫn được chiếm bởi một electron tại nhiệt độ $T = 300\,\mathrm{K}$, và so sánh xác suất đó với giá trị tại $T = 310\,\mathrm{K}$, đối với các dải cấm có độ rộng lần lượt là:
- (a) $E_g = 0{,}200\,\mathrm{eV}$.
- (b) $E_g = 1{,}00\,\mathrm{eV}$.
- (c) $E_g = 5{,}00\,\mathrm{eV}$.

**Phân tích và thiết lập**:

Hàm phân bố Fermi–Dirac cho biết xác suất một trạng thái năng lượng $E$ được chiếm ở nhiệt độ $T$:

$$
f(E) = \frac{1}{e^{(E - E_F)/kT} + 1}
$$

Đối với trạng thái ở đáy dải dẫn của chất bán dẫn thuần, mức năng lượng cách mức Fermi một khoảng bằng một nửa độ rộng dải cấm:

$$
E - E_F = \frac{E_g}{2}
$$

Hằng số Boltzmann biểu diễn theo đơn vị electron-volt trên kelvin là $k \approx 8{,}617 \times 10^{-5}\,\mathrm{eV/K}$.
- Tại nhiệt độ $T = 300\,\mathrm{K}$: Ta có $kT \approx 0{,}02585\,\mathrm{eV}$.
- Tại nhiệt độ $T = 310\,\mathrm{K}$: Ta có $kT \approx 0{,}02671\,\mathrm{eV}$.

**Các bước tính toán chi tiết**:

**(a) Trường hợp $E_g = 0{,}200\,\mathrm{eV}$**:

Khoảng cách năng lượng là:

$$
\begin{aligned}
E - E_F &= \frac{0{,}200\,\mathrm{eV}}{2} \\
&= 0{,}100\,\mathrm{eV}
\end{aligned}
$$

Tại $T = 300\,\mathrm{K}$:

$$
\begin{aligned}
\frac{E - E_F}{kT} &= \frac{0{,}100\,\mathrm{eV}}{0{,}02585\,\mathrm{eV}} \\
&\approx 3{,}87
\end{aligned}
$$

Xác suất trạng thái được lấp đầy là:

$$
f(E) = \frac{1}{e^{3{,}87} + 1} \approx 0{,}0205
$$

Tại $T = 310\,\mathrm{K}$:

$$
\begin{aligned}
\frac{E - E_F}{kT} &= \frac{0{,}100\,\mathrm{eV}}{0{,}02671\,\mathrm{eV}} \\
&\approx 3{,}74
\end{aligned}
$$

Xác suất trạng thái được lấp đầy là:

$$
f(E) = \frac{1}{e^{3{,}74} + 1} \approx 0{,}0231
$$

Tỷ số xác suất giữa hai nhiệt độ là:

$$
\frac{0{,}0231}{0{,}0205} \approx 1{,}13
$$

Khi nhiệt độ tăng thêm $10\,\mathrm{K}$, xác suất tăng $13\%$.

**(b) Trường hợp $E_g = 1{,}00\,\mathrm{eV}$**:

Khoảng cách năng lượng là:

$$
\begin{aligned}
E - E_F &= \frac{1{,}00\,\mathrm{eV}}{2} \\
&= 0{,}500\,\mathrm{eV}
\end{aligned}
$$

Số mũ lớn gấp 5 lần so với phần (a):
- Tại $T = 300\,\mathrm{K}$: Số mũ là $5 \times 3{,}87 = 19{,}35$, cho xác suất $f(E) \approx 4{,}0 \times 10^{-9}$.
- Tại $T = 310\,\mathrm{K}$: Số mũ là $5 \times 3{,}74 = 18{,}70$, cho xác suất $f(E) \approx 7{,}4 \times 10^{-9}$.

Tỷ số xác suất giữa hai nhiệt độ là:

$$
\frac{7{,}4 \times 10^{-9}}{4{,}0 \times 10^{-9}} \approx 1{,}86
$$

Khi nhiệt độ tăng thêm $10\,\mathrm{K}$, xác suất gần như tăng gấp đôi (tăng $86\%$).

**(c) Trường hợp $E_g = 5{,}00\,\mathrm{eV}$**:

Khoảng cách năng lượng là:

$$
\begin{aligned}
E - E_F &= \frac{5{,}00\,\mathrm{eV}}{2} \\
&= 2{,}50\,\mathrm{eV}
\end{aligned}
$$

Số mũ lớn gấp 25 lần so với phần (a):
- Tại $T = 300\,\mathrm{K}$: Số mũ là $2{,}50 / 0{,}02585 \approx 96{,}7$, cho xác suất $f(E) \approx 1{,}0 \times 10^{-42}$.
- Tại $T = 310\,\mathrm{K}$: Số mũ là $2{,}50 / 0{,}02671 \approx 93{,}6$, cho xác suất $f(E) \approx 2{,}3 \times 10^{-41}$.

Tỷ số xác suất giữa hai nhiệt độ là:

$$
\frac{2{,}3 \times 10^{-41}}{1{,}0 \times 10^{-42}} \approx 23
$$

Khi nhiệt độ tăng thêm $10\,\mathrm{K}$, xác suất tăng vọt lên tới 23 lần.

**Đánh giá kết quả**:

Ví dụ này làm nổi bật hai quy luật vật lý then chốt:
1. Độ nhạy theo bề rộng dải cấm: Ở nhiệt độ phòng, xác suất tìm thấy electron ở đáy dải dẫn giảm nhanh khi dải cấm mở rộng. Với $E_g = 0{,}200\,\mathrm{eV}$, xác suất là khoảng $2\%$, trong khi với $E_g = 1{,}00\,\mathrm{eV}$, giá trị này chỉ còn vài phần tỷ, và với $E_g = 5{,}00\,\mathrm{eV}$, xác suất hầu như triệt tiêu hoàn toàn. Điều này giải thích vì sao kim cương tinh khiết ($E_g = 5{,}47\,\mathrm{eV}$) hoàn toàn không có electron trong dải dẫn và trở thành chất cách điện lý tưởng.
2. Độ nhạy theo nhiệt độ: Với một dải cấm cho trước, xác suất phụ thuộc rất mạnh vào nhiệt độ. Dải cấm càng rộng thì mức độ nhạy nhiệt tương đối càng lớn (tăng $13\%$ ở $0{,}2\,\mathrm{eV}$, tăng $86\%$ ở $1{,}0\,\mathrm{eV}$, và tăng $2300\%$ ở $5{,}0\,\mathrm{eV}$).

Cần phân biệt rõ giữa xác suất chiếm chỗ của một trạng thái $f(E)$ và mật độ hạt mang điện thực tế $n$: Để tìm mật độ electron dẫn trên một đơn vị thể tích, ta phải nhân xác suất $f(E)$ với mật độ trạng thái $g(E)$ rồi lấy tích phân trên toàn dải dẫn. Tuy nhiên, yếu tố quyết định sự phụ thuộc nhiệt độ mãnh liệt của độ dẫn điện chính là hàm mũ trong phân bố Fermi–Dirac.

**Khái niệm cốt lõi**: Đặc tính của phân bố Fermi–Dirac giải thích nguyên nhân số lượng electron trong dải dẫn của chất bán dẫn nhạy cảm với cả nhiệt độ và độ rộng của dải cấm.

### Tạp chất và sự pha tạp

Trong chất bán dẫn thuần tinh khiết ở nhiệt độ phòng với $E_g \approx 1{,}0\,\mathrm{eV}$, mật độ electron kích thích nhiệt chỉ vào khoảng $10^{-9}$ so với mật độ electron dẫn trong kim loại. Vì vậy, độ dẫn điện của bán dẫn thuần rất nhỏ. Để kiểm soát và tăng cường độ dẫn điện theo ý muốn công nghệ, người ta chủ động đưa một lượng nhỏ các nguyên tử tạp chất vào mạng tinh thể, quá trình này gọi là sự pha tạp (doping).

#### Bán dẫn loại n và tạp chất cho (Donor)

Giả sử ta pha một lượng nhỏ Arsenic ($\mathrm{As}$, $Z = 33$) vào Germanium lỏng ($\mathrm{Ge}$, $Z = 32$) rồi để nguội cho kết tinh. Arsenic thuộc nhóm V trong bảng tuần hoàn, có năm electron hóa trị, trong khi Germanium chỉ có bốn.

![Hình 42.26: Chất bán dẫn loại n: Germanium pha tạp Arsenic](../img/young-42/hinh-42-26.png)

Khi một nguyên tử Arsenic thế chỗ một nguyên tử Germanium trong mạng tinh thể:
- Bốn trong số năm electron hóa trị của Arsenic tham gia tạo liên kết cộng hóa trị với bốn nguyên tử Germanium lân cận.
- Electron hóa trị thứ năm không tham gia liên kết nên liên kết rất lỏng lẻo với ion Arsenic.

Hạt nhân Arsenic mang điện tích $+33e$, bị chắn bởi 32 electron bên trong nên điện tích hiệu dụng tác dụng lên electron thứ năm xấp xỉ $+e$. Nếu ước tính thô theo mô hình Bohr cho quỹ đạo $n = 4$ của nguyên tử hydro, năng lượng liên kết sẽ là:

$$
\frac{1}{4^2}(13{,}6\,\mathrm{eV}) \approx 0{,}85\,\mathrm{eV}
$$

Trong thực tế, năng lượng liên kết này nhỏ hơn rất nhiều, chỉ vào khoảng $0{,}01\,\mathrm{eV}$. Nguyên nhân là hàm sóng của electron thứ năm trải rộng trên nhiều hằng số mạng và hiệu ứng phân cực điện môi của các nguyên tử xung quanh làm giảm đáng kể lực hút tĩnh điện.

Trên bức tranh dải năng lượng: Mức năng lượng của electron thứ năm này nằm cô lập ngay trong dải cấm, chỉ cách đáy dải dẫn khoảng $E_d \approx 0{,}01\,\mathrm{eV}$. Mức này được gọi là mức cho (donor level), và nguyên tử tạp chất nhóm V được gọi là chất cho (donor). Mọi nguyên tố nhóm V như $\mathrm{N}$, $\mathrm{P}$, $\mathrm{As}$, $\mathrm{Sb}$, $\mathrm{Bi}$ đều đóng vai trò chất cho.

Ở nhiệt độ phòng ($300\,\mathrm{K}$): Năng lượng nhiệt $kT \approx 0{,}025\,\mathrm{eV}$ lớn hơn đáng kể so với $E_d \approx 0{,}01\,\mathrm{eV}$. Do đó, hầu hết các electron từ mức cho đều nhận đủ năng lượng nhiệt để nhảy lên dải dẫn và chuyển động tự do khắp tinh thể. Ion tạp chất cho sau khi mất electron mang điện tích $+e$ nhưng bị giam lỏng cố định tại nút mạng và không tham gia dẫn điện.

Chỉ cần nồng độ tạp chất cho rất nhỏ vào khoảng $10^{-8}$ (một nguyên tử tạp chất trên 100 triệu nguyên tử bán dẫn), mật độ electron dẫn do tạp chất cung cấp đã áp đảo hoàn toàn mật độ electron dẫn nhiệt tự nhiên. Dòng điện lúc này chủ yếu do các hạt mang điện âm (electron) vận chuyển. Vật liệu như vậy được gọi là chất bán dẫn loại n (n-type semiconductor).

#### Bán dẫn loại p và tạp chất nhận (Acceptor)

Nếu thay vì nhóm V, ta pha tạp các nguyên tố thuộc nhóm III trong bảng tuần hoàn như Gallium ($\mathrm{Ga}$, $Z = 31$), Boron ($\mathrm{B}$), Nhôm ($\mathrm{Al}$), Indium ($\mathrm{In}$), các nguyên tử này chỉ có ba electron hóa trị.

![Hình 42.27: Chất bán dẫn loại p: Germanium pha tạp Gallium](../img/young-42/hinh-42-27.png)

Khi nguyên tử Gallium thế chỗ nguyên tử Germanium:
- Để tạo đủ bốn liên kết cộng hóa trị với các nguyên tử lân cận, Gallium lấy thêm một electron từ một liên kết của nguyên tử Germanium bên cạnh.
- Việc này tạo ra một lỗ trống tại nguyên tử Germanium bị mất electron. Lỗ trống này tự do chuyển động trong mạng tinh thể tương tự hạt mang điện dương.

Electron bị hút về phía nguyên tử Gallium nằm tại một mức năng lượng cục bộ trong dải cấm, gọi là mức nhận (acceptor level), nằm ngay phía trên đỉnh dải hóa trị khoảng $E_a \approx 0{,}01\,\mathrm{eV}$. Nguyên tử tạp chất nhóm III được gọi là chất nhận (acceptor). Sau khi nhận thêm một electron, nguyên tử Gallium trở thành một ion âm mang điện tích $-e$ cố định tại nút mạng.

Dưới kích thích nhiệt ở nhiệt độ phòng, các electron từ đỉnh dải hóa trị dễ dàng nhảy lên chiếm chỗ tại các mức nhận, để lại vô số lỗ trống trong dải hóa trị. Độ dẫn điện lúc này chủ yếu do các lỗ trống mang điện tích dương đảm nhận. Vật liệu như vậy được gọi là chất bán dẫn loại p (p-type semiconductor).

Nếu một khối bán dẫn được pha đồng thời cả tạp chất loại n và loại p thì được gọi là chất bán dẫn bù (compensated semiconductor).

::: warning Cảnh báo: Bản chất trung hòa điện của bán dẫn loại n và loại p
Một hiểu lầm rất phổ biến là cho rằng bán dẫn loại p tích điện dương và bán dẫn loại n tích điện âm. Thực tế, cả hai loại bán dẫn đều trung hòa điện tuyệt đối về mặt vĩ mô vì toàn bộ hệ được cấu thành từ các nguyên tử trung hòa ban đầu.

Ký hiệu "loại p" chỉ mang ý nghĩa hạt mang điện tự do đa số trong vật liệu là hạt mang điện dương (lỗ trống), còn "loại n" chỉ ra hạt mang điện tự do đa số là hạt mang điện âm (electron). Điện tích của các hạt tải tự do này luôn được cân bằng hoàn hảo bởi điện tích trái dấu của các ion tạp chất cố định tại các nút mạng tinh thể.
:::

Bằng cách sử dụng hiệu ứng Hall, ta có thể đo đạc thực nghiệm và kiểm chứng trực tiếp dấu của các hạt mang điện. Dấu của suất điện động Hall đảo ngược hoàn toàn giữa bán dẫn loại n và bán dẫn loại p, khẳng định chắc chắn rằng dòng điện trong hai loại vật liệu lần lượt do electron và lỗ trống vận chuyển.

### Kiểm tra mức độ hiểu mục 42.6

Có mang lại lợi ích nào về mặt dẫn điện khi pha tạp chất loại n hoặc loại p vào đồng kim loại không?

::: details Giải thích
Không. Bản thân đồng nguyên chất đã là một kim loại dẫn điện lý tưởng vì có dải dẫn được lấp đầy một phần. Hơn nữa, đồng kết tinh theo liên kết kim loại chứ không phải liên kết cộng hóa trị như Silicon hay Germanium, do đó cơ chế dùng tạp chất để cho hoặc nhận electron không thể vận hành trong đồng.

Trong thực tế, việc đưa tạp chất vào đồng tinh khiết chỉ làm giảm độ dẫn điện, bởi các nguyên tử tạp chất ngoại lai sẽ đóng vai trò các trung tâm tán xạ khuyết tật, cản trở chuyển động có hướng của các electron tự do.
:::
