<!-- Nguồn: mục 1.4, trang in 6–7, trang PDF 26–27; gồm cảnh báo, Chiến lược 1.2, Ví dụ 1.1 và 1.2. -->

## 1.4. Sử dụng và đổi đơn vị

Ta dùng phương trình để biểu diễn quan hệ giữa các đại lượng vật lý, với mỗi đại lượng được ký hiệu bằng một biến đại số. Mỗi ký hiệu ấy biểu thị cả một giá trị số và một đơn vị. Chẳng hạn, $d$ có thể là khoảng cách $10\,\mathrm m$, $t$ là thời gian $5\,\mathrm s$ và $v$ là tốc độ $2\,\mathrm{m/s}$.

Phương trình luôn phải **nhất quán về thứ nguyên**. Giống như không thể cộng số táo với số ô tô rồi xem là cùng một loại đại lượng, hai số hạng chỉ có thể cộng hoặc đặt bằng nhau khi có đơn vị phù hợp. Nếu vật đi quãng đường $d$ trong thời gian $t$ với tốc độ không đổi $v$, ta có:

$$d=vt.$$

Nếu $d$ đo bằng mét thì tích $vt$ cũng phải có đơn vị mét. Với các số vừa nêu:

$$
10\,\mathrm m=\left(2\,\frac{\mathrm m}{\mathrm s}\right)(5\,\mathrm s).
$$

Đơn vị giây ở mẫu của $\mathrm{m/s}$ triệt tiêu với đơn vị giây của thời gian, nên tích có đơn vị mét như yêu cầu. Trong phép nhân và chia, ta xử lý đơn vị giống các ký hiệu đại số.

::: warning Luôn ghi đơn vị trong phép tính
Hãy ghi mỗi số cùng đơn vị đúng và giữ đơn vị qua các bước tính như ví dụ trên. Đây là một cách kiểm tra có ích. Nếu ở một bước, phương trình hoặc biểu thức có những đơn vị không nhất quán, ta biết đã có lỗi. Sách giữ đơn vị trong mọi phép tính và khuyến khích người học làm tương tự khi giải bài.
:::

### Chiến lược giải bài toán 1.2 — Đổi đơn vị

**Xác định khái niệm.** Trong phần lớn bài toán, nên dùng các đơn vị SI cơ bản: độ dài bằng mét, khối lượng bằng kilôgam và thời gian bằng giây. Nếu đề yêu cầu kết quả theo đơn vị khác như kilômét, gam hoặc giờ, có thể đợi đến cuối lời giải mới quy đổi.

**Thiết lập và thực hiện.** Đơn vị được nhân và chia như ký hiệu đại số. Ta có thể đổi đơn vị bằng cách biểu diễn cùng một đại lượng theo hai đơn vị khác nhau rồi lập một đẳng thức.

Ví dụ, $1\,\mathrm{min}=60\,\mathrm s$ không khẳng định số $1$ bằng số $60$. Nó nói rằng một phút và sáu mươi giây biểu thị cùng một khoảng thời gian vật lý. Vì thế:

$$
\frac{1\,\mathrm{min}}{60\,\mathrm s}=1,
\qquad
\frac{60\,\mathrm s}{1\,\mathrm{min}}=1.
$$

Ta có thể nhân đại lượng với một trong hai **hệ số đổi đơn vị** này mà không thay đổi ý nghĩa vật lý của nó. Muốn đổi $3$ phút sang giây, chọn hệ số sao cho đơn vị phút triệt tiêu:

$$
3\,\mathrm{min}
=(3\,\mathrm{min})\frac{60\,\mathrm s}{1\,\mathrm{min}}
=180\,\mathrm s.
$$

**Đánh giá.** Nếu đổi đúng, đơn vị không cần giữ sẽ triệt tiêu. Nếu lại nhân $3\,\mathrm{min}$ với $1\,\mathrm{min}/(60\,\mathrm s)$, ta nhận $\tfrac1{20}\,\mathrm{min^2/s}$, không phải một đại lượng thời gian hợp lý cho yêu cầu này. Ghi đơn vị ở mọi bước sẽ giúp phát hiện lỗi.

Cuối cùng, xét độ hợp lý của kết quả. $3\,\mathrm{min}=180\,\mathrm s$ là hợp lý vì giây nhỏ hơn phút, nên cùng một khoảng thời gian phải có số giây lớn hơn số phút.

### Ví dụ 1.1 — Đổi đơn vị tốc độ

::: exercise Đề bài trong sách
Theo dữ kiện được sách ghi lại, kỷ lục tốc độ trên mặt đất $763.0\,\mathrm{mi/h}$ do Andy Green lập ngày 15 tháng 10 năm 1997 trên chiếc xe dùng động cơ phản lực Thrust SSC. Hãy biểu diễn tốc độ ấy bằng mét trên giây.
:::

::: solution Lời giải của sách
**Xác định, thiết lập và thực hiện.** Ta đổi tốc độ từ dặm trên giờ sang mét trên giây. Vì vậy cần những hệ số liên hệ: (i) dặm với mét, (ii) giờ với giây. Phụ lục E cho:

$$
1\,\mathrm{mi}=1.609\,\mathrm{km},\qquad
1\,\mathrm{km}=1000\,\mathrm m,\qquad
1\,\mathrm h=3600\,\mathrm s.
$$

Đặt các hệ số theo chiều để dặm, kilômét và giờ triệt tiêu:

$$
\begin{aligned}
763.0\,\frac{\mathrm{mi}}{\mathrm h}
&=\left(763.0\,\frac{\mathrm{mi}}{\mathrm h}\right)
  \left(\frac{1.609\,\mathrm{km}}{1\,\mathrm{mi}}\right)\\
&\quad\times\left(\frac{1000\,\mathrm m}{1\,\mathrm{km}}\right)
  \left(\frac{1\,\mathrm h}{3600\,\mathrm s}\right)\\
&\approx341.0\,\mathrm{m/s}.
\end{aligned}
$$

**Đánh giá.** Ví dụ cho một quy tắc ước lượng: giá trị tốc độ tính bằng $\mathrm{m/s}$ hơi nhỏ hơn một nửa giá trị tính bằng $\mathrm{mi/h}$, và hơi nhỏ hơn một phần ba giá trị tính bằng $\mathrm{km/h}$. Chẳng hạn, tốc độ thông thường trên đường cao tốc xấp xỉ $30\,\mathrm{m/s}=67\,\mathrm{mi/h}=108\,\mathrm{km/h}$; tốc độ đi bộ điển hình xấp xỉ $1.4\,\mathrm{m/s}=3.1\,\mathrm{mi/h}=5.0\,\mathrm{km/h}$.

**Ý chính của ví dụ:** Đổi đơn vị bằng cách nhân với hệ số đổi đơn vị thích hợp.
:::

### Ví dụ 1.2 — Đổi đơn vị thể tích

::: exercise Đề bài trong sách
First Star of Africa là một trong những viên kim cương đã được cắt lớn nhất thế giới theo mô tả của sách. Nó được gắn trên quyền trượng Hoàng gia Anh và lưu giữ ở Tháp London. Thể tích viên kim cương là $1.84$ inch khối. Thể tích ấy bằng bao nhiêu centimét khối và mét khối?
:::

::: solution Lời giải của sách
**Xác định, thiết lập và thực hiện.** Cần đổi đơn vị thể tích từ $\mathrm{in^3}$ sang $\mathrm{cm^3}$ và $\mathrm{m^3}$. Phụ lục E cho $1\,\mathrm{in}=2.540\,\mathrm{cm}$, nên:

$$1\,\mathrm{in^3}=(2.54\,\mathrm{cm})^3.$$

Vì thể tích là tích của ba độ dài, hệ số đổi độ dài cũng phải lấy lũy thừa ba:

$$
\begin{aligned}
1.84\,\mathrm{in^3}
&=(1.84\,\mathrm{in^3})
\left(\frac{2.54\,\mathrm{cm}}{1\,\mathrm{in}}\right)^3\\
&=(1.84)(2.54)^3
\frac{\mathrm{in^3\,cm^3}}{\mathrm{in^3}}\\
&\approx30.2\,\mathrm{cm^3}.
\end{aligned}
$$

Tiếp đó, $1\,\mathrm m=100\,\mathrm{cm}$ cho:

$$
\begin{aligned}
30.2\,\mathrm{cm^3}
&=(30.2\,\mathrm{cm^3})
\left(\frac{1\,\mathrm m}{100\,\mathrm{cm}}\right)^3\\
&=(30.2)\left(\frac1{100}\right)^3
\frac{\mathrm{cm^3\,m^3}}{\mathrm{cm^3}}\\
&=30.2\times10^{-6}\,\mathrm{m^3}\\
&=3.02\times10^{-5}\,\mathrm{m^3}.
\end{aligned}
$$

**Đánh giá.** Theo cách đổi này, bạn có thể tự chỉ ra rằng $1\,\mathrm{in^3}\approx16\,\mathrm{cm^3}$ và $1\,\mathrm{m^3}\approx60\,000\,\mathrm{in^3}$ không?

**Ý chính của ví dụ:** Khi đơn vị là tích của các đơn vị đơn giản hơn, chẳng hạn $\mathrm{m^3}=\mathrm m\times\mathrm m\times\mathrm m$, hãy dùng tích tương ứng của các hệ số đổi đơn vị.
:::
