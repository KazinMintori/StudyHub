## Mô hình động học phân tử của khí lý tưởng

Một bình khí gây áp suất lên thành bình dù ta không nhìn thấy từng phân tử. Có thể giải thích áp suất này chỉ từ chuyển động và các va chạm tuân theo định luật Newton hay không? Mô hình động học phân tử trả lời câu hỏi đó và nối nhiệt độ với động năng chuyển động nhiệt.

Mục tiêu của lý thuyết phân tử là hiểu tính chất vĩ mô thông qua cấu trúc và chuyển động vi mô. Cách tiếp cận này còn giúp thiết kế vật liệu có tính chất mong muốn, từ thép bền đến các vật liệu bán dẫn dùng trong linh kiện điện tử.

### Những giả thiết của mô hình

Ta xét khí trong một bình kín có thể tích $V$ với các giả thiết:

1. Bình chứa một số rất lớn $N$ phân tử giống nhau, mỗi phân tử có khối lượng $m$.
2. Kích thước phân tử nhỏ so với kích thước bình và khoảng cách trung bình giữa các phân tử. Ở bước đầu, coi chúng là chất điểm.
3. Phân tử chuyển động liên tục và đôi khi va chạm với thành bình. Các va chạm này hoàn toàn đàn hồi.
4. Thành bình cứng, đứng yên và có khối lượng rất lớn so với phân tử, nên không dịch chuyển khi phân tử va chạm.

Đồng thời, mô hình khí lý tưởng bỏ qua lực hút giữa các phân tử. Phân tử chuyển động thẳng đều giữa những lần va chạm được xét.

Không nhầm số phân tử $N$ với số mol $n$. Hai đại lượng liên hệ bởi:

$$
N=nN_A.
$$

Số $N$ đếm từng phân tử, còn $n$ đo lượng chất theo mol.

### Va chạm với thành bình tạo áp suất

Chọn một mặt thành bình vuông góc trục $x$. Trong va chạm đàn hồi với thành đứng yên, thành phần vận tốc song song thành không đổi. Thành phần vuông góc thành đổi dấu nhưng giữ nguyên độ lớn.

![Hình 18.11: Thành phần vận tốc vuông góc thành bình đảo chiều sau va chạm đàn hồi, còn thành phần song song giữ nguyên.](../img/young-18/a-hinh-18-11.png)

Để trình bày từng bước, trước hết giả sử mọi phân tử có cùng độ lớn thành phần vận tốc $|v_x|$. Sau đó ta sẽ bỏ giả thiết tạm thời này bằng cách lấy trung bình.

Một phân tử đến thành theo chiều âm có động lượng trước va chạm là $-m|v_x|$ và sau va chạm là $+m|v_x|$. Độ biến thiên động lượng:

$$
\Delta p_x=2m|v_x|.
$$

Trong khoảng thời gian rất nhỏ $dt$, một phân tử muốn đập vào vùng thành diện tích $A$ phải nằm cách thành không quá $|v_x|dt$ và đang chuyển động về phía thành.

![Hình 18.12: Những phân tử có thể đập vào vùng thành A trong thời gian dt nằm trong một hình trụ và đang hướng về phía thành.](../img/young-18/a-hinh-18-12.png)

Đặt $\nu=N/V$ là mật độ số phân tử. Hình trụ có đáy $A$, chiều dài $|v_x|dt$, nên chứa $\nu A|v_x|dt$ phân tử. Trung bình một nửa hướng về thành, nửa còn lại hướng ra xa. Số phân tử va chạm trong thời gian đó:

$$
dN_{\mathrm{vc}}=\frac12\nu A|v_x|dt.
$$

Nhân số va chạm với độ biến thiên động lượng mỗi va chạm:

$$
\begin{aligned}
dP_x&=dN_{\mathrm{vc}}(2m|v_x|)\\
&=\nu Amv_x^2dt.
\end{aligned}
\tag{18.9}
$$

Ở đây $P_x$ là tổng thành phần động lượng của các phân tử, khác với ký hiệu $p$ dùng cho áp suất. Bình phương $|v_x|$ bằng $v_x^2$, nên không cần giữ dấu giá trị tuyệt đối trong biểu thức cuối.

Định luật II Newton cho độ lớn lực thành tác dụng lên khí:

$$
F=\frac{dP_x}{dt}=\nu Amv_x^2.
\tag{18.10}
$$

Theo định luật III Newton, khí tác dụng lên thành một lực ngược hướng và cùng độ lớn. Áp suất là:

$$
p=\frac FA=\nu mv_x^2.
\tag{18.11}
$$

Áp suất tăng khi có nhiều phân tử hơn trong một đơn vị thể tích, khi khối lượng mỗi phân tử lớn hơn hoặc khi thành phần vận tốc đập vào thành lớn hơn.

### Bỏ giả thiết các phân tử có cùng tốc độ

Trong khí thực, các phân tử có nhiều vận tốc khác nhau. Có thể chia chúng thành những nhóm có cùng $|v_x|$, tính đóng góp áp suất từng nhóm rồi cộng lại. Kết quả tương đương thay $v_x^2$ bằng giá trị trung bình $\langle v_x^2\rangle$:

$$
p=\nu m\langle v_x^2\rangle.
$$

Chẳng hạn, gọi tổng bình phương các tốc độ là:

$$
S_v=v_1^2+v_2^2+\cdots+v_N^2.
$$

Ký hiệu tổng viết gọn cùng miền chỉ số:

$$
\begin{aligned}
S_v&=\sum_{i=1}^{N}v_i^2,\\
\langle v^2\rangle&=\frac{S_v}{N}.
\end{aligned}
$$

Như vậy, dấu ngoặc nhọn góc ở đây biểu thị phép lấy trung bình trên các phân tử, không phải tốc độ của một phân tử riêng.

Với mỗi phân tử:

$$
v^2=v_x^2+v_y^2+v_z^2.
$$

Lấy trung bình cũng cho tổng ba thành phần. Khí ở trạng thái cân bằng không có phương ưu tiên, nên:

$$
\langle v_x^2\rangle
=\langle v_y^2\rangle
=\langle v_z^2\rangle.
$$

Do đó:

$$
\langle v_x^2\rangle
=\frac13\langle v^2\rangle.
$$

Giả thiết đẳng hướng này phù hợp khi ảnh hưởng của trọng lực lên phân bố vận tốc trong thể tích đang xét có thể bỏ qua và khí không có dòng chuyển động vĩ mô ưu tiên.

Thay vào biểu thức áp suất:

$$
pV=\frac13Nm\langle v^2\rangle.
\tag{18.12}
$$

### Nhiệt độ và động năng tịnh tiến phân tử

Động năng tịnh tiến trung bình của một phân tử là:

$$
\overline K=\frac12m\langle v^2\rangle.
$$

Tổng động năng tịnh tiến hỗn loạn của $N$ phân tử là $K_{\mathrm{tr}}=N\overline K$. Do đó:

$$
pV=\frac23K_{\mathrm{tr}}.
\tag{18.13}
$$

Động năng này chỉ gồm chuyển động tịnh tiến. Khi cấu trúc phân tử cho phép, còn có thể có năng lượng quay hoặc dao động bên trong.

So sánh với phương trình khí lý tưởng $pV=nRT$:

$$
K_{\mathrm{tr}}=\frac32nRT.
\tag{18.14}
$$

Động năng tịnh tiến hỗn loạn tỉ lệ thuận với nhiệt độ tuyệt đối.

![Hình 18.13: Không khí có nhiệt độ cao hơn tương ứng với động năng tịnh tiến trung bình của các phân tử lớn hơn.](../img/young-18/a-hinh-18-13.png)

Chia tổng năng lượng cho số phân tử:

$$
\overline K=\frac{3nRT}{2N}.
$$

Vì $N=nN_A$:

$$
\overline K=\frac32\frac{R}{N_A}T.
\tag{18.15}
$$

Tỉ số $R/N_A$ là hằng số Boltzmann $k$. Giá trị số chính xác của $k$ trong đơn vị $\mathrm{J/K}$ là:

$$
1{,}380649\times10^{-23}.
$$

Vì vậy:

$$
\frac12m\langle v^2\rangle=\frac32kT.
\tag{18.16}
$$

Ở cùng nhiệt độ, các loại phân tử khí lý tưởng có cùng động năng tịnh tiến trung bình, không phụ thuộc khối lượng, áp suất hay thể tích.

Năng lượng tịnh tiến trên mỗi mol:

$$
\frac12M\langle v^2\rangle=\frac32RT.
\tag{18.17}
$$

Dùng $R=N_Ak$, phương trình trạng thái cũng có dạng theo số phân tử:

$$
pV=NkT.
\tag{18.18}
$$

Hằng số $k$ đóng vai trò tương ứng với $R$ khi chuyển từ cách tính theo mol sang cách tính theo từng phân tử.

::: info Hằng số cơ bản và thang Kelvin

Trong cách suy luận trên, ta đi từ $R$ và $N_A$ đến $k$ để làm rõ ý nghĩa vật lý. Trong định nghĩa SI hiện hành, $N_A$ và $k$ đều có giá trị được cố định chính xác, còn $R=N_Ak$. Định nghĩa kelvin gắn với giá trị của $k$. Khi nhiệt độ tăng $1\,\mathrm K$, năng lượng $kT$ tăng đúng $1{,}380649\times10^{-23}\,\mathrm J$.
:::

### Tốc độ căn quân phương

Căn bậc hai của trung bình bình phương tốc độ được gọi là **tốc độ căn quân phương**, ký hiệu $v_{\mathrm{rms}}$:

$$
v_{\mathrm{rms}}=\sqrt{\langle v^2\rangle}.
$$

Từ hệ thức năng lượng:

$$
\begin{aligned}
v_{\mathrm{rms}}&=\sqrt{\frac{3kT}{m}}\\
&=\sqrt{\frac{3RT}{M}}.
\end{aligned}
\tag{18.19}
$$

Để tính đại lượng này, lần lượt bình phương tốc độ từng phân tử, cộng các bình phương, chia cho số phân tử rồi lấy căn. Đây là phép tính khác với lấy trung bình trực tiếp các tốc độ.

Ở cùng nhiệt độ, phân tử nhẹ có tốc độ căn quân phương lớn hơn phân tử nặng. Chẳng hạn, phân tử nitrogen có khối lượng mol khoảng $28\,\mathrm{g/mol}$, nên chuyển động nhanh hơn phân tử oxy có khối lượng mol khoảng $32\,\mathrm{g/mol}$. Phân tử hydro còn nhẹ hơn, với khối lượng mol khoảng $2\,\mathrm{g/mol}$.

Sự chênh lệch tốc độ nhiệt giúp giải thích vì sao các khí nhẹ dễ thất thoát khỏi khí quyển hơn. Muốn xét một phân tử có thoát ra được hay không, phải so sánh tốc độ cụ thể của nó với tốc độ thoát tại nơi đang xét, không chỉ so sánh riêng tốc độ căn quân phương.

Tốc độ thoát gần bề mặt Trái Đất xấp xỉ $1{,}12\times10^4\,\mathrm{m/s}$. Khả năng thất thoát khí còn phụ thuộc phần phân bố vận tốc cao và điều kiện ở tầng khí quyển cao. Khí nặng chuyển động nhiệt chậm hơn nên khó thất thoát bằng cơ chế nhiệt tương ứng.

![Hình 18.14: Hydro là nhiên liệu có thể sử dụng trong giao thông, nhưng chỉ có hàm lượng vết trong khí quyển. Điện phân nước là một cách sản xuất hydro và đòi hỏi cung cấp năng lượng.](../img/young-18/a-hinh-18-14.png)

Giả thiết va chạm hoàn toàn đàn hồi với thành cũng là một lý tưởng hóa. Trong nhiều trường hợp, phân tử bám trên thành một thời gian ngắn rồi rời đi với tốc độ đặc trưng cho nhiệt độ thành. Nếu khí và thành cân bằng nhiệt, không có dòng năng lượng ròng giữa chúng, nên các kết luận trung bình vẫn được giữ.

### Cách giải bài toán động học phân tử

1. Xác định đề đang hỏi đại lượng vĩ mô như nhiệt độ, áp suất hay đại lượng vi mô như năng lượng và tốc độ phân tử.
2. Phân biệt dữ kiện theo từng phân tử với dữ kiện theo mol. Dùng bộ $m,N,k$ cho từng phân tử, hoặc bộ $M,n,R$ khi tính theo mol.
3. Khi dùng SI, đổi khối lượng mol từ gam trên mol sang kilôgam trên mol. Ví dụ, oxy có $M=0{,}0320\,\mathrm{kg/mol}$.
4. Luôn dùng nhiệt độ tuyệt đối theo kelvin trong các hệ thức năng lượng và tốc độ.
5. Kiểm tra đơn vị và độ lớn. Với nhiều khí thông thường ở gần nhiệt độ phòng, tốc độ phân tử có bậc vài trăm mét trên giây.

::: example Ví dụ 18.6: Động năng phân tử và tốc độ căn quân phương

(a) Động năng tịnh tiến trung bình của một phân tử khí lý tưởng ở $27^\circ\mathrm C$ bằng bao nhiêu? (b) Tổng động năng tịnh tiến hỗn loạn của các phân tử trong một mol khí đó bằng bao nhiêu? (c) Tìm tốc độ căn quân phương của phân tử oxy ở cùng nhiệt độ.

**Tóm tắt đề bài:**

- Nhiệt độ: $27^\circ\mathrm C$, lấy xấp xỉ $T=300\,\mathrm K$ trong phép tính.
- Lượng khí ở câu (b): $n=1\,\mathrm{mol}$.
- Oxy có khối lượng mol $M=0{,}0320\,\mathrm{kg/mol}$.
- Khi thay số, dùng các giá trị làm tròn $k=1{,}38\times10^{-23}\,\mathrm{J/K}$ và $R=8{,}314\,\mathrm{J/(mol\,K)}$.

**Hướng đi:**

- Dùng năng lượng trung bình theo một phân tử cho câu (a), theo một mol cho câu (b).
- Câu (c) phụ thuộc khối lượng phân tử. Có thể dùng dạng chứa $M,R$ hoặc dạng chứa $m,k$, với mức làm tròn nhất quán.

**Lời giải:**

(a) Động năng tịnh tiến trung bình:

$$
\begin{aligned}
\overline K &= \frac32kT \\
&= 6{,}21\times10^{-21}\,\mathrm J.
\end{aligned}
$$

Kết quả này áp dụng cho mỗi phân tử khí lý tưởng ở nhiệt độ đã cho, không riêng oxy.

(b) Tổng động năng tịnh tiến của một mol:

$$
K_{\mathrm{tr}}=\frac32nRT
\approx3740\,\mathrm J.
$$

(c) Dùng khối lượng mol:

$$
v_{\mathrm{rms}}=\sqrt{\frac{3RT}{M}}.
$$

Thay $T=300\,\mathrm K$ và $M=0{,}0320\,\mathrm{kg/mol}$ cho:

$$
v_{\mathrm{rms}}\approx484\,\mathrm{m/s}.
$$

Với khối lượng một phân tử oxy $m\approx5{,}31\times10^{-26}\,\mathrm{kg}$, công thức $\sqrt{3kT/m}$ cũng cho khoảng $484\,\mathrm{m/s}$. Tốc độ này tương đương khoảng $1740\,\mathrm{km/h}$ hoặc $1080$ dặm/giờ.

**Đánh giá:** Nhân năng lượng trung bình của một phân tử với số phân tử trong một mol cũng cho xấp xỉ $3740\,\mathrm J$. Đây là động năng tịnh tiến hỗn loạn, không phải động năng của một khối khí đang chuyển động đồng loạt với tốc độ đó.
:::

::: example Ví dụ 18.7: Tốc độ trung bình và tốc độ căn quân phương

Năm phân tử khí có các tốc độ $500$, $600$, $700$, $800$ và $900\,\mathrm{m/s}$. Tìm tốc độ căn quân phương và tốc độ trung bình.

**Tóm tắt đề bài:** Có $N=5$ phân tử. Mỗi giá trị đã cho là độ lớn vận tốc của một phân tử, không phải một thành phần vận tốc có dấu.

**Hướng đi:**

- Tốc độ trung bình dùng tổng các tốc độ chia cho số phân tử.
- Tốc độ căn quân phương dùng tổng bình phương tốc độ chia số phân tử, sau đó lấy căn. Không được lấy căn của tốc độ trung bình.

**Lời giải:**

Tổng tốc độ của năm phân tử là $3500\,\mathrm{m/s}$. Do đó:

$$
\overline v=\frac{3500}{5}
=700\,\mathrm{m/s}.
$$

Tổng bình phương tốc độ của ba phân tử đầu là $1{,}10\times10^6\,\mathrm{m^2/s^2}$. Hai phân tử cuối đóng góp $1{,}45\times10^6\,\mathrm{m^2/s^2}$. Tổng cộng:

$$
S_v=2{,}55\times10^6\,\mathrm{m^2/s^2}.
$$

Trung bình bình phương:

$$
\begin{aligned}
\langle v^2\rangle &= \frac{S_v}{5} \\
&= 5{,}10\times10^5\,\mathrm{m^2/s^2}.
\end{aligned}
$$

Lấy căn:

$$
v_{\mathrm{rms}}\approx714\,\mathrm{m/s}.
$$

**Đánh giá:** Trong mẫu này, tốc độ căn quân phương lớn hơn tốc độ trung bình. Bình phương làm các tốc độ lớn đóng góp mạnh hơn vào phép trung bình. Nói chung $v_{\mathrm{rms}}\ge\overline v$, với dấu bằng chỉ khi mọi tốc độ đều bằng nhau.
:::

### Va chạm giữa các phân tử

Nếu phân tử là những chất điểm hình học, khả năng va chạm trực tiếp giữa chúng bị bỏ qua. Để mô tả quãng đường và thời gian giữa các va chạm, ta mở rộng mô hình, coi mỗi phân tử là một quả cầu cứng bán kính $r$.

Trước hết, giả sử chỉ một phân tử chuyển động với tốc độ $v$, các phân tử khác tạm đứng yên. Hai phân tử va chạm khi tâm cách nhau không quá $2r$.

Trong thời gian $dt$, phân tử chuyển động quét một hình trụ dài $vdt$, bán kính $2r$. Tâm phân tử khác nằm trong hình trụ này sẽ dẫn đến va chạm.

![Hình 18.15: Phân tử bán kính r quét một thể tích va chạm hình trụ bán kính 2r trong thời gian dt.](../img/young-18/a-hinh-18-15.png)

Tiết diện va chạm của hai quả cầu giống nhau:

$$
\sigma=\pi(2r)^2=4\pi r^2.
$$

Với mật độ số $\nu=N/V$, số tâm phân tử nằm trong thể tích quét là:

$$
dN_{\mathrm{vc}}=\nu\sigma vdt.
$$

Trong mô hình một phân tử chuyển động:

$$
\frac{dN_{\mathrm{vc}}}{dt}
=\nu\sigma v.
$$

Khi mọi phân tử đều chuyển động, phải dùng chuyển động tương đối. Trong mô hình cân bằng của các quả cầu giống nhau, hệ số hiệu chỉnh của tốc độ va chạm trung bình là $\sqrt2$:

$$
\frac{dN_{\mathrm{vc}}}{dt}
=\sqrt2\,\nu\sigma v.
$$

Đây là biểu thức tốc độ va chạm trung bình của mô hình, không phải mô tả chính xác lịch va chạm của một phân tử riêng.

### Thời gian và quãng đường tự do trung bình

**Thời gian tự do trung bình** là khoảng thời gian trung bình giữa hai va chạm liên tiếp. Nó bằng nghịch đảo tần số va chạm:

$$
\tau=\frac{1}{\sqrt2\,\nu\sigma v}.
\tag{18.20}
$$

**Quãng đường tự do trung bình** là quãng đường trung bình đi được giữa hai va chạm:

$$
\begin{aligned}
\lambda&=v\tau\\
&=\frac{1}{\sqrt2\,\nu\sigma}\\
&=\frac{V}{4\pi\sqrt2\,r^2N}.
\end{aligned}
\tag{18.21}
$$

Trong xấp xỉ đang dùng, quãng đường tự do trung bình tỉ lệ nghịch với mật độ số phân tử và tiết diện va chạm. Nó không chứa riêng tốc độ $v$, vì phân tử nhanh đi xa hơn trong một đơn vị thời gian nhưng cũng gặp va chạm thường xuyên hơn.

![Hình 18.16: Khoảng đi được giữa những lần gặp người khác trong đám đông phụ thuộc mật độ người và kích thước của họ, tương tự vai trò mật độ và kích thước phân tử.](../img/young-18/a-hinh-18-16.png)

Dùng $pV=NkT$:

$$
\lambda=\frac{kT}{4\pi\sqrt2\,r^2p}.
\tag{18.22}
$$

Tại áp suất không đổi, tăng nhiệt độ làm khí giãn ra và mật độ số giảm, nên quãng đường tự do trung bình tăng. Tại nhiệt độ không đổi, tăng áp suất làm mật độ số tăng, nên quãng đường tự do trung bình giảm.

::: example Ví dụ 18.8: Quãng đường tự do trung bình của không khí

(a) Ước lượng quãng đường tự do trung bình của một phân tử không khí ở $27^\circ\mathrm C$ và áp suất $1\,\mathrm{atm}$. Coi phân tử là quả cầu bán kính $r=2{,}0\times10^{-10}\,\mathrm m$. (b) Ước lượng thời gian tự do trung bình của phân tử oxy có tốc độ bằng $v_{\mathrm{rms}}$ tại điều kiện đó.

**Tóm tắt đề bài:**

- Lấy $T\approx300\,\mathrm K$.
- Áp suất: $p\approx1{,}01\times10^5\,\mathrm{Pa}$.
- Bán kính phân tử: $r=2{,}0\times10^{-10}\,\mathrm m$.
- Tốc độ căn quân phương của oxy: $v_{\mathrm{rms}}\approx484\,\mathrm{m/s}$.

**Hướng đi:**

- Dùng dạng quãng đường tự do trung bình theo áp suất và nhiệt độ vì đề cho trực tiếp hai đại lượng vĩ mô này.
- Sau khi tìm $\lambda$, lấy $\tau=\lambda/v$ cho tốc độ oxy được chỉ định.

**Lời giải:**

(a) Tiết diện va chạm:

$$
\begin{aligned}
\sigma &= 4\pi r^2 \\
&\approx 5{,}03\times10^{-19}\,\mathrm{m^2}.
\end{aligned}
$$

Quãng đường tự do trung bình:

$$
\lambda=\frac{kT}{\sqrt2\,\sigma p}.
$$

Thay các giá trị đã cho:

$$
\lambda\approx5{,}8\times10^{-8}\,\mathrm m.
$$

(b) Thời gian tự do trung bình:

$$
\begin{aligned}
\tau&=\frac{\lambda}{v_{\mathrm{rms}}}\\
&\approx1{,}2\times10^{-10}\,\mathrm s.
\end{aligned}
$$

Tần số va chạm có bậc khoảng $10^{10}$ lần trong một giây.

**Đánh giá:** Quãng đường tự do trung bình rất nhỏ so với kích thước thông thường của bình khí, nhưng vẫn lớn hơn bán kính phân tử vài trăm lần. Trong mô hình này, thay tốc độ bằng một giá trị nhỏ hơn làm thời gian giữa các va chạm dài hơn, còn biểu thức quãng đường trung bình vẫn do mật độ và tiết diện quyết định.
:::

### Câu tự kiểm tra 18.3

Xếp các mẫu khí sau theo thứ tự (a) Tốc độ căn quân phương lớn nhất đến nhỏ nhất và (b) Động năng tịnh tiến trung bình mỗi phân tử lớn nhất đến nhỏ nhất:

- (i) Oxy có $M=32{,}0\,\mathrm{g/mol}$ ở $300\,\mathrm K$.
- (ii) Nitrogen có $M=28{,}0\,\mathrm{g/mol}$ ở $300\,\mathrm K$.
- (iii) Oxy ở $330\,\mathrm K$.
- (iv) Nitrogen ở $330\,\mathrm K$.

<details><summary>Xem lời giải thích</summary>

(a) Tốc độ căn quân phương tỉ lệ với $\sqrt{T/M}$. Hai giá trị đầu cuối được nhận ra từ việc tăng nhiệt độ và giảm khối lượng. Để so sánh hai mẫu giữa, xét:

$$
\frac{300}{28}>\frac{330}{32}.
$$

Vì vậy thứ tự là (iv), (ii), (iii), (i).

(b) Động năng tịnh tiến trung bình mỗi phân tử chỉ phụ thuộc $T$. Hai mẫu ở $330\,\mathrm K$ bằng nhau và lớn hơn hai mẫu ở $300\,\mathrm K$. Thứ tự là (iii) và (iv) đồng hạng, sau đó (i) và (ii) đồng hạng.

</details>
