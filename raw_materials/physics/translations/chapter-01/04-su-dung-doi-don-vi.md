## 1.4. Sử dụng và đổi đơn vị

Ta dùng phương trình để biểu diễn quan hệ giữa các đại lượng vật lý, với mỗi đại lượng được ký hiệu bằng một biến đại số. Mỗi ký hiệu ấy biểu thị cả một giá trị số và một đơn vị. Chẳng hạn, $d$ có thể là khoảng cách $10\,\mathrm m$, $t$ là thời gian $5\,\mathrm s$ và $v$ là tốc độ $2\,\mathrm{m/s}$.

Phương trình luôn phải **nhất quán về thứ nguyên**. Giống như không thể cộng số táo với số ô tô rồi xem là cùng một loại đại lượng, hai số hạng chỉ có thể cộng hoặc đặt bằng nhau khi có đơn vị phù hợp. Nếu vật đi quãng đường $d$ trong thời gian $t$ với tốc độ không đổi $v$, ta có:

$$
d = vt.
$$

Nếu $d$ đo bằng mét thì tích $vt$ cũng phải có đơn vị mét. Với các số vừa nêu:

$$
10\,\mathrm m = \left(2\,\frac{\mathrm m}{\mathrm s}\right)(5\,\mathrm s).
$$

Đơn vị giây ở mẫu của $\mathrm{m/s}$ triệt tiêu với đơn vị giây của thời gian, nên tích có đơn vị mét như yêu cầu. Trong phép nhân và chia, ta xử lý đơn vị giống các ký hiệu đại số.

::: warning Luôn ghi rõ đơn vị trong mọi bước tính
Hãy ghi mỗi số cùng đơn vị tương ứng và giữ đơn vị qua từng bước tính toán. Đây là cách tự kiểm tra hiệu quả: Nếu ở một bước biến đổi, phương trình hoặc biểu thức xuất hiện những đơn vị không nhất quán, ta biết ngay phép tính đã có sai sót. Ta luôn giữ đơn vị trong mọi phép tính và người học cần rèn luyện thói quen tương tự khi giải bài.
:::

### Chiến lược giải bài toán 1.2: Đổi đơn vị

**Bước 1. Xác định khái niệm**:
Trong phần lớn bài toán, nên dùng các đơn vị SI cơ bản: Độ dài bằng mét, khối lượng bằng kilôgam và thời gian bằng giây. Nếu đề bài yêu cầu kết quả theo đơn vị khác như kilômét, gam hoặc giờ, có thể đợi đến bước cuối cùng mới thực hiện quy đổi.

**Bước 2. Thiết lập và thực hiện**:
Đơn vị được nhân và chia như các ký hiệu đại số thông thường. Ta có thể đổi đơn vị bằng cách biểu diễn cùng một đại lượng vật lý theo hai đơn vị khác nhau rồi thiết lập một đẳng thức.

Ví dụ: Đẳng thức $1\,\mathrm{min} = 60\,\mathrm s$ không khẳng định số $1$ bằng số $60$. Nó cho biết một phút và sáu mươi giây biểu thị cùng một khoảng thời gian vật lý. Do đó:

$$
\frac{1\,\mathrm{min}}{60\,\mathrm s} = 1,
\qquad
\frac{60\,\mathrm s}{1\,\mathrm{min}} = 1.
$$

Ta có thể nhân đại lượng với một trong hai **hệ số đổi đơn vị** này mà không làm thay đổi bản chất vật lý của nó. Muốn đổi $3$ phút sang giây, chọn hệ số sao cho đơn vị phút triệt tiêu:

$$
\begin{aligned}
3\,\mathrm{min} &= (3\,\mathrm{min})\left(\frac{60\,\mathrm s}{1\,\mathrm{min}}\right) \\
&= 180\,\mathrm s.
\end{aligned}
$$

**Bước 3. Đánh giá**:
Nếu đổi đúng, đơn vị không mong muốn sẽ triệt tiêu hoàn toàn. Nếu nhân nhầm $3\,\mathrm{min}$ với $1\,\mathrm{min}/(60\,\mathrm s)$, ta sẽ nhận được $\frac{1}{20}\,\mathrm{min^2/s}$, hoàn toàn không phải một đơn vị thời gian hợp lý. Ghi đơn vị ở mọi bước sẽ giúp phát hiện sai sót ngay lập tức.

Cuối cùng, hãy đánh giá độ hợp lý của kết quả: $3\,\mathrm{min} = 180\,\mathrm s$ là hoàn toàn hợp lý vì giây nhỏ hơn phút, nên cùng một khoảng thời gian phải có số giây lớn hơn số phút.

### Ví dụ 1.1: Đổi đơn vị tốc độ

::: exercise Ví dụ 1.1: Đổi đơn vị tốc độ
Kỷ lục tốc độ trên mặt đất $763.0\,\mathrm{mi/h}$ do Andy Green thiết lập ngày 15 tháng 10 năm 1997 trên chiếc xe phản lực Thrust SSC. Hãy biểu diễn tốc độ ấy bằng mét trên giây ($\mathrm{m/s}$).
:::

::: solution Lời giải
**Tóm tắt đề bài**:
- Tốc độ ban đầu: $v = 763.0\,\mathrm{mi/h}$.
- Hệ số đổi dặm: $1\,\mathrm{mi} = 1.609\,\mathrm{km} = 1609\,\mathrm m$.
- Hệ số đổi thời gian: $1\,\mathrm h = 3600\,\mathrm s$.
- Cần tìm: Tốc độ $v$ tính bằng $\mathrm{m/s}$.

**Hướng đi**:
- Cần đổi dặm ($\mathrm{mi}$) sang mét ($\mathrm m$) và giờ ($\mathrm h$) sang giây ($\mathrm s$).
- Sử dụng các hệ số đổi đơn vị bằng $1$: $(1609\,\mathrm m / 1\,\mathrm{mi})$ và $(1\,\mathrm h / 3600\,\mathrm s)$ để triệt tiêu dặm và giờ.

**Lời giải chi tiết**:
Nhân tốc độ với các hệ số đổi đơn vị tương ứng:

$$
\begin{aligned}
v &= 763.0\,\mathrm{mi/h} \\
&= (763.0)\left(\frac{1609\,\mathrm m}{3600\,\mathrm s}\right) \\
&= \frac{(763.0)(1609)}{3600}\,\mathrm{m/s} \\
&\approx 341.0\,\mathrm{m/s}.
\end{aligned}
$$

**Đánh giá**:
Kết quả $341.0\,\mathrm{m/s}$ cho ta một quy tắc ước lượng nhanh trong thực tế: Giá trị tốc độ tính bằng $\mathrm{m/s}$ hơi nhỏ hơn một nửa giá trị tính bằng $\mathrm{mi/h}$, và hơi nhỏ hơn một phần ba giá trị tính bằng $\mathrm{km/h}$. Chẳng hạn:
- Tốc độ thông thường trên đường cao tốc xấp xỉ $30\,\mathrm{m/s} \approx 67\,\mathrm{mi/h}$ (tương đương $108\,\mathrm{km/h}$).
- Tốc độ đi bộ điển hình xấp xỉ $1.4\,\mathrm{m/s} \approx 3.1\,\mathrm{mi/h}$ (tương đương $5.0\,\mathrm{km/h}$).

:::

### Ví dụ 1.2: Đổi đơn vị thể tích

::: exercise Ví dụ 1.2: Đổi đơn vị thể tích
Viên kim cương First Star of Africa là một trong những viên kim cương đã được cắt gọt lớn nhất thế giới. Viên kim cương này được gắn trên vương trượng Hoàng gia Anh và lưu giữ tại Tháp London. Thể tích của viên kim cương là $1.84\,\mathrm{in^3}$. Thể tích ấy bằng bao nhiêu centimét khối ($\mathrm{cm^3}$) và bao nhiêu mét khối ($\mathrm{m^3}$)?
:::

::: solution Lời giải
**Tóm tắt đề bài**:
- Thể tích ban đầu: $V = 1.84\,\mathrm{in^3}$.
- Hệ số đổi độ dài: $1\,\mathrm{in} = 2.54\,\mathrm{cm}$ và $1\,\mathrm m = 100\,\mathrm{cm}$.
- Cần tìm: Thể tích $V$ tính bằng $\mathrm{cm^3}$ và $\mathrm{m^3}$.

**Hướng đi**:
- Thể tích có thứ nguyên chiều dài bậc ba. Do đó, hệ số đổi đơn vị thể tích bằng lập phương của hệ số đổi đơn vị độ dài:
  $(2.54\,\mathrm{cm} / 1\,\mathrm{in})^3$ và $(1\,\mathrm m / 100\,\mathrm{cm})^3$.

**Lời giải chi tiết**:
Bước 1. Đổi thể tích từ $\mathrm{in^3}$ sang $\mathrm{cm^3}$:

$$
\begin{aligned}
V &= 1.84\,\mathrm{in^3} \\
&= (1.84\,\mathrm{in^3}) \left(\frac{2.54\,\mathrm{cm}}{1\,\mathrm{in}}\right)^3 \\
&= (1.84)(2.54)^3\,\mathrm{cm^3} \\
&\approx 30.2\,\mathrm{cm^3}.
\end{aligned}
$$

Bước 2. Đổi thể tích từ $\mathrm{cm^3}$ sang $\mathrm{m^3}$:

$$
\begin{aligned}
V &= 30.2\,\mathrm{cm^3} \\
&= (30.2\,\mathrm{cm^3}) \left(\frac{1\,\mathrm m}{100\,\mathrm{cm}}\right)^3 \\
&= (30.2)\left(10^{-2}\right)^3\,\mathrm{m^3} \\
&= 30.2\times10^{-6}\,\mathrm{m^3} \\
&= 3.02\times10^{-5}\,\mathrm{m^3}.
\end{aligned}
$$

**Đánh giá**:
Từ các hệ số đổi đơn vị, hãy tự kiểm tra hai ước lượng: $1\,\mathrm{in^3}\approx16\,\mathrm{cm^3}$ và $1\,\mathrm{m^3}\approx60000\,\mathrm{in^3}$. Kết quả $3.02\times10^{-5}\,\mathrm{m^3}$ là một số rất nhỏ khi tính bằng mét khối, hoàn toàn phù hợp vì mét khối là một đơn vị thể tích rất lớn dành cho các vật thể tầm vóc con người và kiến trúc.
:::
