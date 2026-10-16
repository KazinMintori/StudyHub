## 42.7 Các linh kiện bán dẫn

Những thiết bị phát và thu vô tuyến ban đầu sử dụng đèn điện tử chân không. Transistor, diode và vi mạch bán dẫn cho phép thực hiện nhiều chức năng tương tự trong các linh kiện thể rắn nhỏ gọn hơn. Ta sẽ xét cách các hạt tải và tiếp giáp tạo nên những chức năng ấy.

### Tế bào quang điện và đầu dò hạt

Một linh kiện bán dẫn cơ bản là tế bào quang điện (photocell). Khi một phiến bán dẫn mỏng được chiếu sáng bởi bức xạ có năng lượng photon lớn hơn hoặc bằng độ rộng dải cấm ($hf \ge E_g$):

![Hình 42.28: Sơ đồ nguyên lý của một tế bào quang điện chất bán dẫn](../img/young-42/hinh-42-28.png)

Các photon bị hấp thụ sẽ kích thích các electron từ dải hóa trị nhảy qua dải cấm lên dải dẫn, tạo ra các cặp electron–lỗ trống tự do. Sự gia tăng nồng độ hạt tải làm tăng độ dẫn điện của phiến bán dẫn (hiện tượng quang dẫn), dẫn đến sự sụt giảm điện trở và làm tăng cường độ dòng điện chạy trong mạch ngoài.

Nguyên lý vật lý này cũng được ứng dụng trực tiếp trong các đầu dò hạt mang điện thể rắn: Khi một hạt mang điện giàu năng lượng (như proton hoặc hạt alpha) đi xuyên qua tinh thể bán dẫn, hạt sẽ ion hóa các nguyên tử trên đường đi và giải phóng một thác lũ các cặp electron–lỗ trống. Xung điện tích thu được có biên độ tỷ lệ thuận với năng lượng của hạt tới, cho phép các nhà vật lý nhận diện chính xác loại hạt và đo đạc phổ năng lượng của chúng.

### Lớp chuyển tiếp p–n

Hầu hết các linh kiện bán dẫn đều khai thác tính chất cơ bản xuất hiện tại ranh giới tiếp xúc giữa hai miền bán dẫn loại p và loại n trong cùng một đơn tinh thể, cấu trúc này được gọi là lớp chuyển tiếp p–n (p–n junction).

#### Trạng thái cân bằng nhiệt và vùng nghèo

Xét một tinh thể bán dẫn duy nhất có một nửa được pha tạp chất nhận (loại p) và nửa kia được pha tạp chất cho (loại n):

![Hình 42.30: Lớp chuyển tiếp p–n ở trạng thái cân bằng nhiệt](../img/young-42/hinh-42-30.png)

Do sự chênh lệch nồng độ hạt tải rất lớn ở hai phía của mặt tiếp xúc:
- Các electron tự do từ miền n có xu hướng khuếch tán sang miền p và tái hợp với các lỗ trống.
- Các lỗ trống tự do từ miền p có xu hướng khuếch tán sang miền n và tái hợp với các electron.

Quá trình khuếch tán và tái hợp này làm triệt tiêu các hạt tải tự do ngay tại khu vực tiếp giáp, để lại:
- Các ion tạp chất cho mang điện tích dương cố định ở phía miền n.
- Các ion tạp chất nhận mang điện tích âm cố định ở phía miền p.

Khu vực lân cận mặt tiếp xúc bị quét sạch các hạt mang điện tự do được gọi là vùng nghèo (depletion region). Sự phân bố điện tích không gian của các ion cố định này thiết lập nên một điện trường nội tại $\vec{E}$ hướng từ miền n sang miền p.

Điện trường nội tại sinh ra một hiệu điện thế tiếp xúc, tạo nên một hàng rào thế năng ngăn cản sự khuếch tán tiếp theo của các hạt tải đa số. Trên phương diện vi mô, có bốn dòng hạt đồng thời chuyển động qua lớp chuyển tiếp:
1. Dòng tái hợp lỗ trống $i_{pr}$: Lỗ trống từ miền p có đủ năng lượng nhiệt để vượt qua hàng rào thế năng khuếch tán sang miền n.
2. Dòng tái hợp electron $i_{nr}$: Electron từ miền n có đủ năng lượng nhiệt để vượt qua hàng rào thế năng khuếch tán sang miền p.
3. Dòng sinh nhiệt lỗ trống $i_{pg}$: Các cặp electron–lỗ trống sinh ra do kích thích nhiệt trong vùng nghèo hoặc lân cận, trong đó lỗ trống bị điện trường nội tại quét dạt về miền p.
4. Dòng sinh nhiệt electron $i_{ng}$: Electron sinh ra do nhiệt bị điện trường nội tại quét dạt về miền n.

Ở trạng thái cân bằng nhiệt (không có điện áp ngoài đặt vào mạch, $V = 0$): Dòng sinh và dòng tái hợp của từng loại hạt mang điện tự triệt tiêu lẫn nhau từng đôi một:

$$
\begin{aligned}
&|i_{pg}| = |i_{pr}|, \\
&|i_{ng}| = |i_{nr}|
\end{aligned}
\tag{42.23}
$$

Dòng điện tổng cộng qua mặt tiếp xúc bằng không, và mức Fermi $E_F$ có giá trị không đổi đồng nhất tại mọi vị trí trong toàn bộ tinh thể.

#### Phân cực thuận và phân cực nghịch

Khi đặt một hiệu điện thế ngoài $V$ vào hai đầu lớp chuyển tiếp:

![Hình 42.29: Đường đặc tuyến vôn-ampe của một điốt tiếp giáp p–n](../img/young-42/hinh-42-29.png)

- Phân cực thuận ($V > 0$): Cực dương nối với miền p và cực âm nối với miền n.

![Hình 42.31: Lớp chuyển tiếp p–n trong điều kiện phân cực thuận](../img/young-42/hinh-42-31.png)

Điện áp ngoài tạo ra điện trường ngược chiều với điện trường nội tại, làm suy giảm điện trường tổng cộng trong vùng nghèo và hạ thấp hàng rào thế năng một lượng $\Delta E = -eV$. Nhờ đó, các electron từ miền n và các lỗ trống từ miền p dễ dàng vượt qua hàng rào để khuếch tán sang phía đối diện.

Cả hai dòng tái hợp đều tăng vọt theo thừa số Maxwell–Boltzmann $e^{-\Delta E/kT} = e^{eV/kT}$. Trong khi đó, các dòng sinh nhiệt $i_{pg}$ và $i_{ng}$ hầu như không thay đổi vì chúng phụ thuộc vào tốc độ tạo cặp bằng nhiệt chứ không phụ thuộc vào độ cao hàng rào. Dòng lỗ trống tổng cộng là:

$$
\begin{aligned}
i_{p,\text{tot}} &= i_{pr} - |i_{pg}| \\
&= |i_{pg}| e^{eV/kT} - |i_{pg}| \\
&= |i_{pg}| (e^{eV/kT} - 1)
\end{aligned} \tag{42.24}
$$

Dòng electron tổng cộng $i_{n,\text{tot}}$ cũng tuân theo quy luật tương tự. Do đó, cường độ dòng điện tổng cộng chạy qua lớp chuyển tiếp $I = i_{p,\text{tot}} + i_{n,\text{tot}}$ được mô tả bởi phương trình Shockley:

$$
I = I_S (e^{eV/kT} - 1) \tag{42.22}
$$

hoặc viết tương đương theo các thành phần dòng sinh nhiệt vi mô:

$$
I = I_S (e^{eV/kT} - 1) \tag{42.25}
$$

trong đó $I_S = |i_{pg}| + |i_{ng}|$ được gọi là dòng điện bão hòa ngược.

- Phân cực nghịch ($V < 0$): Cực dương nối với miền n và cực âm nối với miền p.

Hàng rào thế năng được nâng cao thêm, ngăn chặn gần như hoàn toàn các dòng khuếch tán tái hợp ($i_{pr} \approx 0$ và $i_{nr} \approx 0$). Chỉ còn lại các dòng sinh nhiệt do các hạt thiểu số tạo ra bị quét qua mặt tiếp xúc. Khi điện áp ngược đủ lớn ($|eV| \gg kT$), thừa số mũ triệt tiêu và dòng điện tiệm cận giá trị dòng bão hòa ngược nhỏ: $I \approx -I_S$.

Đặc tuyến không đối xứng cho phép dùng tiếp giáp p–n để chỉnh lưu. Dòng ngược nhỏ trong miền đang xét, nhưng không bằng không tuyệt đối và có thể tăng mạnh khi xảy ra đánh thủng.

### Các cơ chế đánh thủng diode

Khi điện áp phân cực nghịch tăng lên quá lớn, dòng điện ngược không còn giữ ở mức $I_S$ mà tăng vọt đột ngột, hiện tượng này gọi là sự đánh thủng (breakdown):
1. Đánh thủng thác lũ (Avalanche breakdown): Khi điện áp ngược rất cao, điện trường trong vùng nghèo trở nên khổng lồ. Các hạt tải thiểu số nhận được động năng rất lớn giữa hai lần va chạm, đủ để ion hóa các nguyên tử mạng tinh thể trong các va chạm không đàn hồi và giải phóng thêm các cặp electron–lỗ trống mới. Các hạt mới sinh lại tiếp tục được gia tốc và gây ra phản ứng dây chuyền dạng thác lũ.
2. Đánh thủng Zener (Zener breakdown): Ở các lớp tiếp giáp p–n được pha tạp nồng độ rất cao, vùng nghèo có bề dày mỏng (cỡ vài nanômét).

![Hình 42.32: Hiện tượng đánh thủng Zener do hiệu ứng đường ngầm trong lớp chuyển tiếp p–n](../img/young-42/hinh-42-32.png)

Dưới điện áp phân cực nghịch lớn, đáy dải dẫn ở miền n bị kéo tụt xuống thấp hơn đỉnh dải hóa trị ở miền p. Hàng rào thế năng giữa hai dải trở nên đủ mỏng để các electron trong dải hóa trị ở miền p có thể chui hầm lượng tử trực tiếp xuyên qua dải cấm sang các trạng thái còn trống ở dải dẫn miền n. Quá trình đường ngầm này tạo ra dòng điện ngược tăng mạnh ở một điện áp xác định gọi là điện áp Zener. Diode Zener được ứng dụng rộng rãi trong các mạch ổn định điện áp.

### Ứng dụng quang điện tử

Mối liên hệ giữa dòng điện và photon trong lớp chuyển tiếp p–n là cơ sở của ngành quang điện tử:
- Diode phát quang (LED): Khi phân cực thuận, các electron từ miền n và lỗ trống từ miền p được tiêm vào vùng tiếp giáp và tái hợp với nhau. Khi electron rơi từ dải dẫn xuống dải hóa trị để lấp lỗ trống, năng lượng giải phóng được phát xạ dưới dạng một photon có năng lượng xấp xỉ bằng độ rộng dải cấm: $hf \approx E_g$. Bước sóng và màu sắc của ánh sáng phát ra có thể được điều chỉnh chính xác bằng cách chế tạo các vật liệu bán dẫn có độ rộng dải cấm khác nhau. LED có hiệu suất chuyển đổi năng lượng rất cao và tuổi thọ bền bỉ, ứng dụng phổ biến trong chiếu sáng dân dụng, đèn tín hiệu và màn hình hiển thị.
- Pin mặt trời và cảm biến quang: Là quá trình ngược lại của LED, gọi là hiệu ứng quang điện trong. Ánh sáng chiếu vào vùng tiếp giáp p–n tạo ra các cặp electron–lỗ trống. Điện trường nội tại lập tức phân tách cặp hạt này trước khi chúng kịp tái hợp: Đẩy electron về miền n và lỗ trống về miền p, tạo nên một suất điện động quang điện và cung cấp công suất cho mạch ngoài. Nguyên lý này vận hành trong các tấm pin quang điện mặt trời và các cảm biến mảng tích điện (CCD) của máy ảnh kỹ thuật số.

![Hình Ứng dụng Sinh học B.1: Viên nang nội soi bán dẫn](../img/young-42/ung-dung-b-1.png)

Viên nang trong hình chứa một camera dùng đầu dò CCD và sáu đèn LED chiếu sáng. Khi đi qua dạ dày và ruột, nó truyền hình ảnh có độ phân giải cao bằng sóng vô tuyến tới bộ ghi bên ngoài. Cấu trúc này cho phép quan sát ruột non, nơi phương pháp nội soi thông thường khó tiếp cận.

### Transistor

Transistor là linh kiện bán dẫn có khả năng khuếch đại tín hiệu điện và vận hành như những khóa chuyển mạch siêu nhanh.

#### Transistor lưỡng cực (BJT)

Transistor tiếp giáp lưỡng cực gồm hai lớp tiếp giáp p–n ghép đối lưng nhau trong cấu trúc ba lớp kẹp: P-n-p hoặc n-p-n.

![Hình 42.33: Sơ đồ cấu tạo và mạch điện của transistor tiếp giáp p-n-p](../img/young-42/hinh-42-33.png)

Ba miền bán dẫn lần lượt được gọi là:
- Cực phát (Emitter, E): Pha tạp nồng độ cao nhằm cung cấp dồi dào hạt tải.
- Cực gốc (Base, B): Là lớp ở giữa, có bề dày rất mỏng và nồng độ pha tạp rất thấp.
- Cực thu (Collector, C): Có kích thước lớn hơn để thu nhận các hạt tải và tản nhiệt.

Trong mạch cực gốc chung của transistor p-n-p:
- Lớp tiếp xúc phát–gốc được phân cực thuận bởi nguồn điện áp $V_e$, làm các lỗ trống từ cực phát tràn sang cực gốc.
- Do cực gốc rất hẹp và ít hạt tải, hầu hết các lỗ trống này (thường trên $98\%$) không bị tái hợp mà khuếch tán thẳng sang lớp tiếp xúc gốc–thu.
- Tại đây, điện trường phân cực nghịch mạnh của nguồn điện áp $V_c$ lập tức hút các lỗ trống vào cực thu, tạo nên dòng điện cực thu $I_c$ chạy qua điện trở tải $R$.

Nhờ điện áp thu $V_c$ có thể lớn hơn nhiều so với điện áp phát $V_e$, công suất tiêu tán trên điện trở $R$ lớn hơn rất nhiều so với công suất cung cấp ở mạch vào, tạo ra sự khuếch đại công suất và khuếch đại điện áp.

![Hình 42.34: Mạch khuếch đại transistor mắc theo kiểu cực phát chung](../img/young-42/hinh-42-34.png)

Một sơ đồ phối ghép thông dụng khác là mạch cực phát chung: Một biến thiên rất nhỏ của dòng điện cực gốc $I_b$ ở đầu vào sẽ điều khiển một biến thiên rất lớn của dòng điện cực thu $I_c$ ở đầu ra, đem lại hiệu quả khuếch đại dòng điện đáng kể.

#### Transistor hiệu ứng trường (MOSFET)

Một họ transistor quan trọng khác là transistor hiệu ứng trường kim loại–oxit–bán dẫn (MOSFET).

![Hình 42.35: Cấu tạo của một transistor hiệu ứng trường loại MOSFET](../img/young-42/hinh-42-35.png)

Trong cấu trúc MOSFET chế độ làm giàu:
- Trên một phiến đế silicon loại p, người ta tạo hai vùng loại n gọi là cực nguồn (source) và cực máng (drain).
- Một điện cực thứ ba gọi là cực cổng (gate) được cách điện hoàn toàn khỏi đế silicon và các cực nguồn, máng bằng một lớp màng mỏng cách điện Silicon Dioxide ($\mathrm{SiO}_2$).

Khi chưa đặt điện áp lên cực cổng: Dù có đặt hiệu điện thế giữa cực nguồn và cực máng theo bất kỳ chiều nào, dòng điện chạy qua kênh vẫn gần như triệt tiêu vì luôn có một trong hai lớp tiếp giáp p–n bị phân cực nghịch.

Khi đặt một điện tích dương lên cực cổng: Điện trường sinh ra xuyên qua lớp cách điện $\mathrm{SiO}_2$ sẽ hút các electron tự do (vốn là hạt thiểu số trong đế p) tập trung dày đặc về vùng bề mặt ngay bên dưới cực cổng. Lớp electron này tạo thành một "kênh dẫn n" nối thông giữa cực nguồn và cực máng, cho phép dòng điện chạy qua dễ dàng. Cường độ dòng điện qua kênh biến thiên rất nhạy theo điện tích và điện thế của cực cổng. Do dòng điện vào cực cổng bằng không nhờ lớp cách điện $\mathrm{SiO}_2$, MOSFET có trở kháng đầu vào vô cùng lớn và tiêu thụ công suất điều khiển cực thấp.

### Vi mạch tích hợp (Integrated Circuits)

Bằng công nghệ quang khắc và lắng đọng màng mỏng liên tiếp, người ta có thể chế tạo hàng triệu đến hàng tỷ transistor MOSFET, điện trở và tụ điện trên một phiến bán dẫn duy nhất chỉ rộng vài milimét vuông, tạo thành các vi mạch tích hợp (IC chip).

![Hình 42.36: Vi mạch tích hợp chứa hàng triệu linh kiện](../img/young-42/hinh-42-36.png)

Transistor được phát minh năm 1947. Các linh kiện bán dẫn và vi mạch sau đó làm thay đổi thiết kế thiết bị điện tử nhờ giảm kích thước, tăng độ tin cậy và kết hợp nhiều chức năng trên cùng một cấu trúc.

### Kiểm tra mức độ hiểu mục 42.7

Giả sử ta đặt một điện tích âm lên cực cổng của transistor MOSFET trong Hình 42.35. Liệu có dòng điện đáng kể nào có thể chạy giữa cực nguồn và cực máng không?

::: details Giải thích
Không. Điện tích âm trên cực cổng sẽ sinh ra lực tĩnh điện đẩy các electron tự do ra xa bề mặt tiếp xúc và hút các lỗ trống lại gần lớp cách điện.

Do đó, nồng độ hạt mang điện âm trong khu vực nằm giữa hai lớp tiếp giáp p–n càng bị suy giảm trầm trọng hơn, không thể hình thành kênh dẫn kết nối. Vì hầu như không có hạt tải tự do dẫn điện trong vùng này, dòng điện chạy giữa cực nguồn và cực máng vẫn hoàn toàn bị ngăn chặn.
:::
