## 39.4. Laser

Laser là một nguồn sáng phát ra chùm ánh sáng có độ kết hợp rất cao và rất gần với đơn sắc (với độ rộng phổ hữu hạn) nhờ sự phát xạ phối hợp của nhiều nguyên tử. Tên gọi "laser" là từ viết tắt của cụm từ tiếng Anh: *Light Amplification by Stimulated Emission of Radiation* (Khuếch đại ánh sáng bằng phát xạ kích thích). Ta có thể hiểu nguyên lý hoạt động của laser dựa trên các mức năng lượng nguyên tử và photon thông qua hai khái niệm nền tảng: Sự phát xạ kích thích và sự đảo lộn mật độ cư trú.

### Phát xạ tự phát và phát xạ kích thích

Xét một khối khí nguyên tử đặt trong một bình chứa trong suốt. Giả sử mỗi nguyên tử ban đầu ở mức cơ bản có năng lượng $E_g$ và có một mức kích thích với năng lượng $E_{\text{ex}}$.

Nếu ta chiếu một chùm sáng có tần số $f$ vào bình chứa, một nguyên tử có thể hấp thụ một photon tới nếu năng lượng photon $hf$ thỏa mãn đúng điều kiện cộng hưởng bằng hiệu năng lượng giữa hai mức:

$$
hf = E_{\text{ex}} - E_g
$$

Quá trình này được gọi là sự hấp thụ (absorption). Khi hấp thụ photon, nguyên tử chuyển từ mức cơ bản $E_g$ lên mức kích thích $E_{\text{ex}}$ (Hình 39.28a).

![Hình 39.28: Ba quá trình tương tác cơ bản giữa nguyên tử và ánh sáng. (a) Quá trình hấp thụ photon. (b) Quá trình phát xạ tự phát với hướng và pha ngẫu nhiên. (c) Quá trình phát xạ kích thích tạo ra hai photon kết hợp về tần số, pha, hướng truyền và trạng thái phân cực.](../img/young-39/hinh-39-28.png)

Sau một khoảng thời gian ngắn ở mức kích thích, nguyên tử có thể tự phát rơi trở về mức cơ bản $E_g$ bằng cách giải phóng một photon có cùng tần số $f$ (Hình 39.28b). Quá trình này được gọi là sự phát xạ tự phát (spontaneous emission). Trong phát xạ tự phát, hướng truyền, pha dao động và trạng thái phân cực của mỗi photon phát ra là hoàn toàn ngẫu nhiên và độc lập giữa các nguyên tử khác nhau. Ánh sáng phát ra từ các nguồn sáng thông thường (như bóng đèn dây tóc hay đèn huỳnh quang) chủ yếu là kết quả của sự phát xạ tự phát không kết hợp.

Ngược lại, trong quá trình phát xạ kích thích (stimulated emission), photon tới gặp một nguyên tử vốn đã ở sẵn trạng thái kích thích (Hình 39.28c). Điện từ trường dao động của photon tới gây ra một hiệu ứng cộng hưởng, kích hoạt nguyên tử phát ra một photon thứ hai. Photon mới sinh ra này có cùng tần số, cùng hướng truyền, cùng pha và cùng trạng thái phân cực với photon kích thích ban đầu. Photon tới không bị suy giảm hay biến đổi sau quá trình này.

Như vậy, trước khi phát xạ chỉ có một photon tới, nhưng sau phát xạ ta thu được hai photon giống hệt nhau cùng bay theo một hướng. Vì hai photon có cùng pha dao động, chúng giao thoa tăng cường và tạo thành bức xạ kết hợp. Đây chính là bản chất của cơ chế khuếch đại ánh sáng.

---

### Phân bố Maxwell–Boltzmann và giới hạn của cân bằng nhiệt

Để hiểu rõ điều kiện xảy ra phát xạ kích thích, ta cần phân biệt giữa hai khái niệm: Mức năng lượng (energy level) và trạng thái lượng tử (quantum state). Một hệ vật lý có thể có nhiều trạng thái khác nhau cùng sở hữu chung một giá trị năng lượng (các trạng thái suy biến). Chẳng hạn, một con lắc lò xo không ma sát có thể đạt cùng một thế năng đàn hồi $U = \frac{1}{2} k b^2$ khi nén một đoạn $x = -b$ hoặc khi kéo giãn một đoạn $x = +b$. Đối với nguyên tử hydro, mức cơ bản $-13{,}60\text{ eV}$ gồm hai trạng thái khác nhau do spin của electron, trong khi mức kích thích thứ nhất $-3{,}40\text{ eV}$ gồm tám trạng thái lượng tử khác nhau.

Số lượng nguyên tử cư trú ở một trạng thái xác định trong chất khí ở trạng thái cân bằng nhiệt tuân theo định luật phân bố Maxwell–Boltzmann. Tại nhiệt độ tuyệt đối $T$, số nguyên tử $n_i$ ở một trạng thái có năng lượng $E_i$ tỉ lệ với thừa số Boltzmann $e^{-E_i / kT}$, trong đó $k = 1{,}38 \times 10^{-23}\text{ J/K}$ là hằng số Boltzmann.

Nếu viết $n_i = A e^{-E_i/(kT)}$, hệ số $A$ là hệ số chuẩn hóa chung cho các trạng thái trong cùng hệ ở nhiệt độ đang xét.

Tỉ số giữa số nguyên tử ở một trạng thái kích thích $E_{\text{ex}}$ và số nguyên tử ở một trạng thái cơ bản $E_g$ trong điều kiện cân bằng nhiệt được xác định bởi:

$$
\begin{aligned}
\frac{n_{\mathrm{ex}}}{n_g} &= \frac{A e^{-E_{\mathrm{ex}}/kT}}{A e^{-E_g/kT}} \\
&= e^{-(E_{\mathrm{ex}} - E_g)/kT}
\end{aligned}
\tag{39.18}
$$

Xét một ví dụ định lượng cụ thể: Giả sử độ chênh lệch năng lượng là $E_{\text{ex}} - E_g = 2{,}0\text{ eV} = 3{,}2 \times 10^{-19}\text{ J}$, tương ứng với photon ánh sáng đỏ có bước sóng $620\text{ nm}$. Ở nhiệt độ rất cao $T = 3000\text{ K}$ (xấp xỉ nhiệt độ dây tóc bóng đèn sợi đốt), với hằng số $k = 1{,}38 \times 10^{-23}\text{ J/K}$, tích số năng lượng nhiệt là:

$$
kT = 4{,}14 \times 10^{-20}\text{ J}
$$

Với $E_{\text{ex}} - E_g = 3{,}2 \times 10^{-19}\text{ J}$ và $kT = 4{,}14 \times 10^{-20}\text{ J}$, số mũ Boltzmann tương ứng có giá trị:

$$
\frac{E_{\text{ex}} - E_g}{kT} = 7{,}73
$$

Khi đó, tỉ số số lượng nguyên tử cư trú là:

$$
\begin{aligned}
\frac{n_{\mathrm{ex}}}{n_g} &= e^{-7{,}73} \\
&\approx 0{,}00044 = 0{,}044\%
\end{aligned}
$$

Ngay cả ở nhiệt độ $3000\text{ K}$, tỉ số số nguyên tử trong hai trạng thái vẫn chưa tới $1$ phần nghìn. Trong mô hình hai trạng thái ở cân bằng nhiệt này, phát xạ kích thích không thể lấn át sự hấp thụ. Khi photon tương tác với môi trường, nó có khả năng gặp một nguyên tử ở trạng thái cơ bản lớn hơn khả năng gặp một nguyên tử kích thích. Không thể tạo khuếch đại thuần chỉ bằng cách giữ hệ ở cân bằng nhiệt.

---

### Sự đảo lộn mật độ cư trú và laser bốn mức

Liệu có thể tăng số nguyên tử kích thích chỉ bằng cách chiếu bức xạ có tần số cộng hưởng vào bình? Một số nguyên tử sẽ hấp thụ photon và chuyển lên mức trên, làm tỉ số số nguyên tử ở hai trạng thái tăng trong chốc lát. Tuy nhiên, ban đầu số nguyên tử ở trạng thái cơ bản lớn hơn nhiều. Vì vậy, tốc độ hấp thụ năng lượng từ chùm tới lớn hơn tốc độ bổ sung năng lượng cho chùm bằng phát xạ kích thích. Muốn nâng số nguyên tử ở mức trên đến gần số nguyên tử ở mức dưới trong một thời gian ngắn cũng cần chùm sáng rất mạnh.

Muốn khuếch đại ánh sáng bằng phát xạ kích thích, ta phải đưa hệ ra khỏi cân bằng nhiệt. Trong hệ khi đó, số nguyên tử ở trạng thái trên phải lớn hơn số nguyên tử ở trạng thái dưới của chuyển dời laser. Tình trạng bất thường này được gọi là sự đảo lộn mật độ cư trú (population inversion). Khi đã có sự đảo lộn mật độ cư trú, tốc độ phát xạ kích thích sẽ vượt qua tốc độ hấp thụ, biến môi trường hoạt chất thành một nguồn khuếch đại ánh sáng.

Để thiết lập sự đảo lộn mật độ cư trú, người ta sử dụng môi trường vật chất có cấu trúc mức năng lượng phù hợp. Một cấu trúc phổ biến là hệ laser bốn mức (four-level laser).

![Hình 39.29(a–c): Các giai đoạn hoạt động của laser bốn mức. (a) Trước khi bơm. (b) Ngay sau khi bơm. (c) Khoảng 10⁻⁸ s sau khi bơm, số nguyên tử ở trạng thái siêu bền E2 vượt quá số nguyên tử ở E1.](../img/young-39/hinh-39-29.png)

Hệ laser bốn mức gồm mức cơ bản $E = 0$ và ba mức kích thích $E_1, E_2, E_3$:
- Mức $E_1$ và mức $E_3$ là các mức kích thích thông thường, có thời gian sống ngắn (khoảng $10^{-8}\text{ s}$).
- Mức $E_2$ là một trạng thái kích thích đặc biệt có thời gian sống dài khác thường (vào khoảng $10^{-3}\text{ s}$, tức là dài hơn khoảng 100.000 lần so với các mức kích thích thông thường). Trạng thái sống lâu này được gọi là trạng thái siêu bền (metastable state). Sự tồn tại của trạng thái siêu bền thường xuất phát từ các quy tắc chọn lọc lượng tử về bảo toàn mômen động lượng ngăn cản nguyên tử giải phóng photon một cách nhanh chóng.

Quá trình hoạt động của laser bốn mức diễn ra theo các bước:

1. **Quá trình bơm (pumping)**: Ban đầu toàn bộ nguyên tử ở trạng thái cơ bản (Hình 39.29a). Người ta cung cấp năng lượng ngoại vi để bơm các nguyên tử từ trạng thái cơ bản lên các mức kích thích $E_1, E_2$ và $E_3$ (Hình 39.29b). Trong laser chất khí, việc bơm được thực hiện bằng cách đặt một điện áp cao giữa hai điện cực đặt trong ống phóng điện; các electron mang động năng lớn va chạm và kích thích các nguyên tử khí.

2. **Thiết lập đảo lộn mật độ cư trú**: Trong khoảng thời gian cực ngắn cỡ $10^{-8}\text{ s}$, các nguyên tử được kích thích lên mức $E_3$ sẽ phát xạ tự phát photon để nhanh chóng rơi về mức siêu bền $E_2$ hoặc về trạng thái cơ bản. Cùng lúc đó, các nguyên tử ở mức $E_1$ cũng nhanh chóng chuyển dời về mức cơ bản $E = 0$. Kết quả là mức $E_1$ gần như bị làm trống hoàn toàn, trong khi các nguyên tử bị "ùn ứ" và tích tụ với mật độ rất lớn tại mức siêu bền $E_2$. Khi đó, số nguyên tử ở mức $E_2$ vượt xa số nguyên tử ở mức $E_1$, tạo thành sự đảo lộn mật độ cư trú giữa mức $E_2$ và mức $E_1$ (Hình 39.29c). Số nguyên tử ở mức siêu bền vẫn có thể nhỏ hơn số nguyên tử ở mức cơ bản. Sự đảo lộn cần thiết ở đây được xét giữa hai trạng thái tham gia chuyển dời laser, không phải giữa mức siêu bền và mức cơ bản.

3. **Phát xạ kích thích trong buồng cộng hưởng quang học**: Trong khoảng thời gian $10^{-3}\text{ s}$ tiếp theo, một vài nguyên tử đầu tiên ở mức siêu bền $E_2$ rơi xuống mức $E_1$ bằng phát xạ tự phát, giải phóng các photon có năng lượng $hf = E_2 - E_1$. Bình chứa hoạt chất laser được đặt giữa hai gương phản xạ phẳng song song tạo thành một buồng cộng hưởng quang học (optical resonator cavity) (Hình 39.29d).

![Hình 39.29(d): Sơ đồ laser chất khí. Hai gương phản xạ ánh sáng qua lại trong hoạt chất để duy trì phát xạ kích thích. Một gương truyền qua một phần ánh sáng, tạo chùm tia đi ra ngoài.](../img/young-39/hinh-39-29d.png)

Một gương có hệ số phản xạ gần như $100\%$, trong khi gương đối diện có hệ số phản xạ khoảng $95\%$ (cho phép khoảng $5\%$ ánh sáng truyền qua). Các photon phát ra theo phương trục của buồng cộng hưởng sẽ phản xạ qua lại liên tục giữa hai gương, quét qua khối khí nhiều lần. Trên đường đi, chúng liên tục kích thích các nguyên tử khác ở mức $E_2$ giải phóng thêm các photon giống hệt, tạo thành một phản ứng dây chuyền phát xạ kích thích dạng thác lũ. Các quá trình này tạo ra chùm sáng có tần số $f$, cường độ lớn và các tia gần song song. Chùm laser có độ đơn sắc cao nhưng vẫn có độ rộng phổ hữu hạn. Nó còn có tính kết hợp không gian giữa các điểm trên cùng một tiết diện. Một phần chùm sáng kết hợp này thoát qua gương bán mạ, tạo thành chùm tia laser phát ra ngoài.

---

### Chế độ hoạt động và ứng dụng của laser

Tùy thuộc vào phương thức cung cấp năng lượng bơm, laser có thể hoạt động ở hai chế độ:
- **Laser xung (Pulsed laser)**: Năng lượng bơm được cung cấp ngắt quãng theo từng xung điện áp cao ngắn, tạo ra chùm tia laser dưới dạng các xung năng lượng tập trung. Laser xung được ứng dụng rộng rãi trong y học, chẳng hạn như phẫu thuật khúc xạ mắt LASIK (Laser-Assisted In Situ Keratomileusis) để điều chỉnh giác mạc chữa cận thị, viễn thị và loạn thị.
- **Laser liên tục (Continuous-wave laser)**: Năng lượng bơm được cấp liên tục và đều đặn với cường độ đủ lớn để duy trì sự đảo lộn mật độ cư trú ổn định. Tốc độ bổ sung nguyên tử lên mức $E_2$ thông qua bơm cân bằng đúng với tốc độ nguyên tử phát xạ rơi về $E_1$. Laser liên tục được sử dụng trong các máy quét mã vạch ở quầy thanh toán, máy đo đạc trắc địa và viễn thông quang học.

Vì cần có một sự bố trí mức năng lượng đặc biệt để tạo ra hoạt động laser, chỉ một số vật liệu nhất định mới có thể được dùng làm laser:
- **Laser chất khí**: Sử dụng chất khí làm hoạt chất, tiêu biểu là laser heli–neon (phát ra ánh sáng đỏ bước sóng $632{,}8\text{ nm}$).
- **Laser chất rắn**: Một số loại laser sử dụng vật liệu rắn trong suốt, chẳng hạn như thủy tinh neodymium (neodymium glass), thay vì chất khí.
- **Laser bán dẫn**: Loại laser phổ biến nhất, được sử dụng trong máy in laser, bút chỉ laser và đầu đọc dữ liệu trên đĩa trong đầu phát DVD hoặc Blu-ray. Laser bán dẫn không sử dụng các mức năng lượng nguyên tử riêng rẽ mà sử dụng các mức năng lượng của electron chuyển động tự do trong toàn bộ thể tích chất bán dẫn (sẽ được khảo sát ở Chương 42).

---

### Câu hỏi tự kiểm tra 39.4

Một bóng đèn quảng cáo neon thông thường phát ra ánh sáng màu đỏ có bước sóng $632{,}8\text{ nm}$. Các nguyên tử neon cũng được sử dụng trong laser khí heli–neon. Ánh sáng phát ra từ bóng đèn quảng cáo neon là:

(i) Phát xạ tự phát

(ii) Phát xạ kích thích

(iii) Cả phát xạ tự phát và phát xạ kích thích

::: details Đáp án và giải thích
**Đáp án đúng**: (i).

**Giải thích chi tiết**:
Trong bóng đèn quảng cáo neon thông thường, một hiệu điện thế lớn được đặt giữa hai đầu ống thủy tinh chứa khí neon. Điện trường làm ion hóa một phần chất khí, tạo thành dòng electron mang động năng lớn chạy qua khối khí. Các electron này va chạm và kích thích các nguyên tử neon lên các mức năng lượng cao. Từ các mức kích thích này, các nguyên tử neon rơi về mức thấp hơn theo cơ chế phát xạ tự phát, phát ra các photon có bước sóng $632{,}8\text{ nm}$.

Trong bóng đèn neon thông thường:
- Không có cơ chế bơm tạo sự đảo lộn mật độ cư trú.
- Không có hệ thống gương phản xạ song song để giam hãm photon tạo phát xạ kích thích dây chuyền.

Do đó, ánh sáng phát ra hoàn toàn là phát xạ tự phát, không có tính kết hợp và không phải là ánh sáng laser.
:::
