## 41.7 Phổ tia X

Tia X (tia Röntgen) là bức xạ điện từ có bước sóng rất ngắn, thường nằm trong khoảng từ $0{,}001\,\mathrm{nm}$ đến $10\,\mathrm{nm}$, tương ứng với năng lượng photon từ khoảng $100\,\mathrm{eV}$ đến hàng trăm kilô-electronvolt ($\mathrm{keV}$). Chúng được tạo ra khi một chùm electron mang động năng lớn (được gia tốc dưới hiệu điện thế hàng chục đến hàng trăm kilovolt) bắn phá vào một bia kim loại nặng (anot) trong ống chân không.

Phổ phát xạ tia X thu được gồm hai thành phần độc lập nhưng xếp chồng lên nhau:
1. **Phổ liên tục** (bức xạ hãm – Bremsstrahlung): Tạo nên nền phổ trải dài trên một dải bước sóng rộng.
2. **Phổ đặc trưng**: Gồm các vạch phát xạ sắc nhọn với cường độ rất lớn tại các bước sóng xác định, mang tính chất đặc trưng riêng của từng nguyên tố làm bia.

![Hình 41.23: Phổ tia X khi electron được gia tốc qua hiệu điện thế 35 kV đập vào bia molipđen. Nền liên tục của bức xạ hãm chồng với các đỉnh phổ đặc trưng.](../img/young-41/hinh-41-23.png)

### Phổ liên tục và bước sóng cắt ngắn

Khi các electron năng lượng cao xâm nhập vào bia kim loại, chúng bị tán xạ và giảm tốc đột ngột trong điện trường Coulomb mạnh mẽ của các hạt nhân nguyên tử bia. Theo điện động lực học, một hạt mang điện tích khi có gia tốc sẽ phát ra sóng điện từ. Trong tiếng Đức, bức xạ phát ra do sự hãm tốc này được gọi là **Bremsstrahlung** (bức xạ hãm).

Một electron có thể mất một phần hoặc toàn bộ động năng của nó sau một hoặc nhiều lần va chạm liên tiếp. Mỗi lần va chạm giải phóng một photon có năng lượng $h f$. Vì năng lượng mất mát trong các va chạm hãm tốc là ngẫu nhiên và liên tục, bức xạ hãm tạo nên một **phổ liên tục**.

Trường hợp giới hạn xảy ra khi electron bị hãm dừng lại hoàn toàn chỉ sau một lần va chạm trực diện duy nhất. Toàn bộ động năng ban đầu của nó biến thành năng lượng của một photon duy nhất:

$$
h f_{\max} = \frac{h c}{\lambda_{\min}} = e V_{AC}
$$

Trong đó $V_{AC}$ là hiệu điện thế gia tốc giữa catot và anot. Bước sóng ngắn nhất khả dĩ trong phổ liên tục được gọi là **bước sóng cắt ngắn** $\lambda_{\min}$:

$$
\lambda_{\min} = \frac{h c}{e V_{AC}} \tag{41.46}
$$

Thay các hằng số vật lý:

$$
\lambda_{\min} \approx \frac{1{,}24 \times 10^{-6}\,\mathrm{V\cdot m}}{V_{AC}}
$$

> [!IMPORTANT] Tính chất của bước sóng cắt ngắn
> Bước sóng cắt ngắn $\lambda_{\min}$ chỉ phụ thuộc duy nhất vào hiệu điện thế gia tốc $V_{AC}$ mà hoàn toàn không phụ thuộc vào bản chất vật liệu làm bia kim loại. Không một photon nào có thể phát ra với bước sóng nhỏ hơn $\lambda_{\min}$ vì điều đó sẽ vi phạm định luật bảo toàn năng lượng.

### Phổ đặc trưng và mức năng lượng nguyên tử

Khi hiệu điện thế gia tốc đủ lớn, electron bắn phá có thể thâm nhập sâu vào các lớp vỏ bên trong của nguyên tử bia và đánh bật một electron ở lớp vỏ trong cùng ra khỏi nguyên tử.

Quá trình hình thành vạch đặc trưng diễn ra qua hai giai đoạn:
1. **Tạo lỗ trống**: Một electron ở vỏ trong (thường là vỏ $K$, ứng với $n=1$) bị bắn bật ra ngoài, để lại một trạng thái trống gọi là **lỗ trống** (hole). Nguyên tử trở thành một ion kích thích với mức năng lượng rất cao.
2. **Lấp đầy lỗ trống**: Một electron từ một trong các vỏ ngoài có mức năng lượng cao hơn (như vỏ $L$ với $n=2$, vỏ $M$ với $n=3$, hoặc vỏ $N$ với $n=4$) sẽ nhảy xuống lấp đầy lỗ trống ở vỏ $K$. Trong quá trình chuyển dời này, nguyên tử phát ra một photon tia X có năng lượng đúng bằng độ chênh lệch năng lượng giữa hai mức dừng:

$$
h f = E_i - E_f
$$

Vì năng lượng liên kết của các electron lớp trong bị chi phối trực tiếp bởi điện tích hạt nhân $+Ze$ của nguyên tố làm bia, độ chênh lệch năng lượng này có giá trị xác định và đặc trưng cho từng nguyên tố hóa học. Các vạch phát xạ này được gọi là **phổ tia X đặc trưng**.

Quy ước gọi tên các vạch quang phổ đặc trưng:
- **Dãy K**: Tạo thành khi electron từ các vỏ ngoài nhảy về lấp lỗ trống ở vỏ $K$ ($n=1$):
  - Chuyển dời từ vỏ $L$ ($n=2$) về vỏ $K$ ($n=1$): Vạch $K_\alpha$.
  - Chuyển dời từ vỏ $M$ ($n=3$) về vỏ $K$ ($n=1$): Vạch $K_\beta$.
  - Chuyển dời từ vỏ $N$ ($n=4$) về vỏ $K$ ($n=1$): Vạch $K_\gamma$.
- **Dãy L**: Tạo thành khi electron từ các vỏ cao hơn nhảy về lấp lỗ trống ở vỏ $L$ ($n=2$), phát ra các vạch $L_\alpha, L_\beta, \dots$ Các vạch này có năng lượng nhỏ hơn và bước sóng dài hơn so với dãy $K$.

![Hình 41.25: So sánh bước sóng của các vạch Ka, Kb và Kg của ba nguyên tố kim loại làm bia: Vonfram (W), Molipđen (Mo) và Đồng (Cu).](../img/young-41/hinh-41-25.png)

![Ứng dụng: Ứng dụng phổ tia X đặc trưng trong khoa học hình sự để phân tích dư lượng thuốc súng.](../img/young-41/ung-dung-b-3.png)

> [!NOTE] Ứng dụng thực tiễn: Tia X trong khoa học hình sự
> Phổ tia X là một công cụ quan trọng trong phân tích tội phạm. Khi một khẩu súng ngắn được bắn, một đám khói dư lượng thuốc súng (gunshot residue - GSR) được phụt ra từ nòng súng. Phổ phát xạ tia X của GSR bao gồm các đỉnh đặc trưng từ chì ($\mathrm{Pb}$), antimon ($\mathrm{Sb}$) và bari ($\mathrm{Ba}$). Nếu một mẫu thu thập từ da hoặc quần áo của nghi phạm có phổ phát xạ tia X mang những đặc trưng này, điều đó chỉ ra rằng nghi phạm gần đây đã nổ súng.

### Định luật Moseley

Năm 1913, Henry G. J. Moseley khảo sát thực nghiệm phổ tia X đặc trưng của các nguyên tố. Ông nhận thấy tần số của vạch $K_\alpha$ liên hệ chặt chẽ với số hiệu nguyên tử $Z$. Trong khi tính chất phổ quang học của những nguyên tố có $Z$ gần nhau có thể rất khác, các phổ tia X này biến đổi đều đặn hơn.

Moseley phát hiện ra rằng căn bậc hai của tần số vạch phát xạ tỷ lệ bậc nhất với số thứ tự của nguyên tố trong bảng tuần hoàn:

$$
\sqrt{f} \propto (Z - 1)
$$

Hệ thức thực nghiệm của Moseley đối với vạch $K_\alpha$ có dạng:

$$
f = C_0 (Z - 1)^2 \tag{41.47}
$$

với hằng số thực nghiệm $C_0 \approx 2{,}48 \times 10^{15}\,\mathrm{Hz}$.

![Hình 41.24: Căn bậc hai tần số vạch Kα của 14 nguyên tố gần nằm trên một đường thẳng theo số hiệu nguyên tử Z, với giao điểm tại Z = 1.](../img/young-41/hinh-41-24.png)

Ta có thể giải thích trực quan định luật Moseley dựa trên mô hình Bohr kết hợp với hiện tượng che chắn điện tích:
1. Để phát ra vạch $K_\alpha$, nguyên tử trước tiên phải có một lỗ trống ở vỏ $K$ ($n=1$). Do đó, tại vỏ $K$ chỉ còn lại duy nhất một electron.
2. Khi một electron ở vỏ $L$ ($n=2$) chuẩn bị nhảy xuống lấp chỗ trống, nó chuyển động trong điện trường của hạt nhân mang điện tích $+Ze$ bị che chắn bởi chính 1 electron $1s$ còn lại kia.
3. Vì vậy, điện tích hạt nhân hiệu dụng mà electron $2p$ cảm nhận được là:

$$
Z_{\mathrm{eff}} \approx Z - 1
$$

Năng lượng của electron ở vỏ $K$ ($n=1$) và vỏ $L$ ($n=2$) xấp xỉ bằng:

$$
E_1 \approx -(Z - 1)^2 (13{,}60\,\mathrm{eV})
$$

$$
\begin{aligned}
E_2 &\approx -\frac{(Z - 1)^2}{4}(13{,}60\,\mathrm{eV}) \\
&= -3{,}40\,\mathrm{eV}(Z - 1)^2
\end{aligned}
$$

Năng lượng của photon tia X phát ra khi electron chuyển từ $n=2$ về $n=1$:

$$
\begin{aligned}
hf &= E_2 - E_1 \\
&\approx (Z - 1)^2 (10{,}20\,\mathrm{eV})
\end{aligned} \tag{41.48}
$$

Tần số photon tương ứng:

$$
\begin{aligned}
f &= \frac{10{,}20\,\mathrm{eV}}{h}(Z - 1)^2 \\
&\approx C_0 (Z - 1)^2
\end{aligned}
$$

với $C_0 = \frac{10{,}20\,\mathrm{eV}}{h} \approx 2{,}466 \times 10^{15}\,\mathrm{Hz}$. Hằng số lý thuyết $2{,}47 \times 10^{15}\,\mathrm{Hz}$ phù hợp một cách phi thường với hằng số thực nghiệm $2{,}48 \times 10^{15}\,\mathrm{Hz}$ của Moseley!


### Ví dụ 41.11: Phân tích nguyên tố bằng phổ phát xạ tia X

Một nhà khoa học bắn chùm electron vào một mẫu kim loại chưa biết và đo được bước sóng của vạch phát xạ tia X đặc trưng $K_\alpha$ là $\lambda = 0{,}0709\,\mathrm{nm} = 70{,}9\,\mathrm{pm}$. Hãy xác định số hiệu nguyên tử $Z$ và gọi tên nguyên tố hóa học này.

**Nhận dạng bài toán**: Bước sóng vạch $K_\alpha$ liên hệ trực tiếp với số hiệu nguyên tử $Z$ thông qua định luật Moseley.

**Chuẩn bị**: Tần số của photon phát xạ được tính từ bước sóng: $f = c/\lambda$. Từ định luật Moseley $f = (2{,}48 \times 10^{15}\,\mathrm{Hz})(Z - 1)^2$, ta giải phương trình để tìm $Z$:

$$
Z = 1 + \sqrt{\frac{f}{2{,}48 \times 10^{15}\,\mathrm{Hz}}}
$$

**Thực hiện**:
Tính tần số của bức xạ:

$$
\begin{aligned}
f &= \frac{c}{\lambda} \\
&\approx 4{,}228 \times 10^{18}\,\mathrm{Hz}
\end{aligned}
$$

với bước sóng $\lambda = 0{,}0709 \times 10^{-9}\,\mathrm{m}$.

Thay vào hệ thức Moseley:

$$
\begin{aligned}
Z &= 1 + \sqrt{\frac{f}{C_0}} \\
&= 1 + \sqrt{1705} \approx 42{,}3
\end{aligned}
$$

Vì số hiệu nguyên tử $Z$ bắt buộc phải là một số nguyên, ta kết luận:

$$
Z = 42
$$

Tra bảng tuần hoàn, nguyên tố có $Z = 42$ chính là **Molipđen** (Molybdenum, ký hiệu $\mathrm{Mo}$).

**Đánh giá:** Kết quả $Z\approx42{,}3$ không nguyên vì quan hệ Moseley là một mô hình thực nghiệm gần đúng. Cấu trúc vỏ electron khác nhau giữa các nguyên tố gây những độ lệch nhỏ. Trong bài toán này, giá trị gần số nguyên 42 cho phép nhận diện molipđen.

Niels Bohr từng nhấn mạnh vai trò của những quan sát Moseley trong việc củng cố mô hình hạt nhân dương được các electron bao quanh. Moseley không nhận giải Nobel cho công trình này. Ông hy sinh khi mới 27 tuổi trong Chiến tranh thế giới thứ nhất, còn giải Nobel không được trao theo hình thức truy tặng.

**Khái niệm cần nhớ**: Phổ tia X đặc trưng là một dấu vân tay nguyên tử độc nhất, cho phép định danh chính xác thành phần nguyên tố hóa học của vật chất.

### Phổ hấp thụ tia X và bờ hấp thụ

Phổ hấp thụ tia X không đơn giản là đảo ngược phổ phát xạ. Vạch $K_\alpha$ xuất hiện khi một electron từ lớp $L$ chuyển xuống lỗ trống ở lớp $K$. Với nguyên tử ở trạng thái cơ bản có $Z\ge10$, lớp $L$ đã đầy, nên photon không thể chỉ đẩy electron $K$ vào đúng trạng thái $L$ đã bị chiếm.

Muốn được hấp thụ, photon phải đưa electron đến một trạng thái còn trống. Trạng thái cuối có thể là trạng thái liên kết còn trống hoặc trạng thái tự do. Trong nhiều nguyên tử nhiều electron, các mức trống đầu tiên chỉ thấp hơn mốc electron tự do vài electronvolt. Vì thế, ngưỡng hấp thụ của electron lớp sâu gần bằng năng lượng ion hóa của lớp ấy.

Khi photon đưa electron ra trạng thái tự do, điều kiện năng lượng là:

Quá trình này đòi hỏi năng lượng photon $E = h f$ phải lớn hơn hoặc tối thiểu bằng năng lượng liên kết (năng lượng ion hóa) của electron ở lớp vỏ tương ứng:

$$
E \ge E_{\mathrm{binding}}
$$

Khi tăng dần năng lượng photon $E$ (tức là giảm dần bước sóng $\lambda$):
1. Khi $E$ nhỏ hơn năng lượng ion hóa của vỏ $K$, photon không đủ năng lượng để đánh bật electron vỏ $K$. Độ hấp thụ tia X của vật liệu giảm dần khi năng lượng tăng.
2. Ngay khi năng lượng photon đạt tới ngưỡng liên kết của electron vỏ $K$, một kênh hấp thụ mới mở ra: Photon có thể đánh bật electron vỏ $K$. Tại điểm này, độ hấp thụ tăng vọt đột ngột lên gấp nhiều lần. Bước nhảy hấp thụ đột ngột này được gọi là **bờ hấp thụ K** (K absorption edge).
3. Tương tự, ở các dải năng lượng thấp hơn, ta quan sát thấy các bờ hấp thụ ứng với các phân lớp của vỏ $L$ ($L_{\mathrm{I}}, L_{\mathrm{II}}, L_{\mathrm{III}}$).

![Hình 41.26: Đồ thị độ hấp thụ tia X theo năng lượng photon khi đi qua lá kim loại molipđen, xuất hiện bờ hấp thụ K sắc nhọn tại khoảng 20 keV.](../img/young-41/hinh-41-26.png)

### Câu tự kiểm tra 41.7

Một chùm photon được truyền qua một mẫu khí hydro nguyên tử ở nhiệt độ cao. Tại giá trị năng lượng photon nào sau đây ta kỳ vọng sẽ xuất hiện bờ hấp thụ tương tự như bờ hấp thụ hiển thị trong Hình 41.26?

(i) $13{,}60\,\mathrm{eV}$

(ii) $3{,}40\,\mathrm{eV}$

(iii) $1{,}51\,\mathrm{eV}$

(iv) Tất cả các mức này

(v) Không có mức nào trong số này

::: details Lời giải chi tiết
**Đáp án đúng**: (iv) Tất cả các mức này.

**Lập luận**:
Một bờ hấp thụ xuất hiện nếu năng lượng của photon vừa đủ lớn để bứt một electron ở một mức năng lượng cho trước ra khỏi nguyên tử (tức là chuyển lên trạng thái tự do $E \ge 0$).

Trong một mẫu khí hydro ở nhiệt độ cao, các va chạm nhiệt làm cho một phần các nguyên tử bị kích thích lên các trạng thái cao hơn, do đó ta kỳ vọng sẽ tìm thấy các nguyên tử có electron ở trạng thái cơ bản ($n = 1$), mức kích thích thứ nhất ($n = 2$), và mức kích thích thứ hai ($n = 3$).

Theo PT (41.21), mức năng lượng của nguyên tử hydro có dạng:

$$
E_n = -\frac{13{,}60\,\mathrm{eV}}{n^2}
$$

Với $n = 1, 2, 3$, các mức năng lượng này lần lượt bằng $-13{,}60\,\mathrm{eV}$, $-3{,}40\,\mathrm{eV}$ và $-1{,}51\,\mathrm{eV}$ (xem Hình 39.23 ở Mục 39.3). Năng lượng photon tối thiểu cần thiết để ion hóa một electron từ các mức này lần lượt bằng:
- Từ mức $n = 1$: $E_{\mathrm{photon}} = 13{,}60\,\mathrm{eV}$
- Từ mức $n = 2$: $E_{\mathrm{photon}} = 3{,}40\,\mathrm{eV}$
- Từ mức $n = 3$: $E_{\mathrm{photon}} = 1{,}51\,\mathrm{eV}$

Vì vậy, ta kỳ vọng sẽ quan sát thấy một bờ hấp thụ tại mỗi giá trị năng lượng photon này, do đó đáp án đúng là (iv).
:::
