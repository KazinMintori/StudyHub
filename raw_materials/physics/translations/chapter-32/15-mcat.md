## Câu hỏi MCAT: So sánh các giới hạn trường

Các nghiên cứu về tác dụng của trường điện từ lên con người là cơ sở để xây dựng hướng dẫn bảo vệ trước những tác dụng bất lợi đã được xác lập. ICNIRP là Ủy ban Quốc tế về Bảo vệ trước Bức xạ Không ion hóa. Hướng dẫn cho công chúng và hướng dẫn đối với người có phơi nhiễm nghề nghiệp được phân biệt.

Để làm các câu 32.54–32.56, xét dữ kiện giới hạn biên độ điện trường:

- Trong miền $1\,\mathrm{Hz}$ đến $25\,\mathrm{Hz}$, lấy $E_{\max}=14\,\mathrm{kV/m}$.
- Trong miền $25\,\mathrm{Hz}$ đến $3\,\mathrm{kHz}$, lấy:

$$
E_{\max}=\frac{350}{f_k}\,\mathrm{V/m},
$$

trong đó $f_k$ là trị số tần số tính bằng kilohertz. Chẳng hạn, $60\,\mathrm{Hz}$ tương ứng với $f_k=0{,}060$.

Các dữ kiện này được dùng như một mô hình bài tập về sóng phẳng chạy. Đánh giá phơi nhiễm thực tế ở tần số thấp cần xét điện trường và từ trường riêng, vì trường gần nguồn không nhất thiết có $E=cB$. Các quy chuẩn và giá trị hiệu dụng cần được tra cứu trong [hướng dẫn ICNIRP về trường tần số thấp](https://www.icnirp.org/cms/upload/publications/ICNIRPLFgdl.pdf).

::: exercise 32.54
Điện lưới tại Hoa Kỳ dùng tần số $60\,\mathrm{Hz}$. Theo giới hạn điện trường của mô hình trên, cường độ lớn nhất của một sóng điện từ hình sin tại tần số này là bao nhiêu?

- (a) $7{,}7\,\mathrm{W/m^2}$.
- (b) $160\,\mathrm{W/m^2}$.
- (c) $45\,\mathrm{kW/m^2}$.
- (d) $260\,\mathrm{kW/m^2}$.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Tần số phải đổi sang kilohertz trước khi dùng công thức giới hạn. Giới hạn đã cho là biên độ điện trường, không phải điện trường hiệu dụng.

**Hướng đi:**

- Dùng $f_k=0{,}060$ để tìm $E_{\max}$.
- Dùng $I=\varepsilon_0cE_{\max}^2/2$, vì đang xét sóng phẳng hình sin trong chân không theo mô hình bài tập.

Biên độ giới hạn:

$$
\begin{aligned}
E_{\max} &= \frac{350}{0{,}060}\,\mathrm{V/m} \\
&= 5{,}83\times10^3\,\mathrm{V/m}.
\end{aligned}
$$

Cường độ tương ứng:

$$
\begin{aligned}
I &= \frac12\varepsilon_0cE_{\max}^2 \\
&\approx 4{,}51\times10^4\,\mathrm{W/m^2} \\
&\approx 45\,\mathrm{kW/m^2}.
\end{aligned}
$$

Chọn (c). Đáp án lớn hơn nếu bỏ nhầm hệ số $1/2$, vì khi đó đã dùng biên độ như giá trị hiệu dụng.
:::

::: exercise 32.55
Nếu tăng gấp đôi tần số trong miền $25\,\mathrm{Hz}$ đến $3\,\mathrm{kHz}$, cường độ lớn nhất theo mô hình giới hạn thay đổi theo hệ số nào?

- (a) $2$.
- (b) $1/\sqrt2$.
- (c) $1/2$.
- (d) $1/4$.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Cả tần số ban đầu lẫn tần số sau khi tăng phải nằm trong miền công thức $350/f_k$ áp dụng.

**Hướng đi:**

- Giới hạn điện trường tỉ lệ nghịch với tần số.
- Cường độ sóng hình sin tỉ lệ với bình phương biên độ điện trường, nên cần bình phương hệ số thay đổi.

Khi $f_k'=2f_k$:

$$
\begin{aligned}
E_{\max}' &= \frac{350}{2f_k} =\frac{E_{\max}}2, \\
\frac{I'}I &= \left(\frac{E_{\max}'}{E_{\max}}\right)^2 \\
&= \frac14.
\end{aligned}
$$

Chọn (d). Nếu tần số mới vượt khỏi miền đã cho, không được kéo dài quy luật này mà chưa có công thức của miền tiếp theo.
:::

::: exercise 32.56
Trong miền $25\,\mathrm{Hz}$ đến $3\,\mathrm{kHz}$, bổ sung vào mô hình một giới hạn từ trường:

$$
B_{\max}=\frac5{f_k}\,\mathrm T.
$$

Đây là dữ kiện giả định để so sánh cường độ tương đương, không phải một giá trị hướng dẫn phơi nhiễm thực tế. Giới hạn điện trường $350/f_k\,\mathrm{V/m}$ hay giới hạn từ trường trên ràng buộc cường độ của sóng phẳng chặt hơn?

- (a) Giới hạn từ trường, vì tại một tần số thì từ trường cho phép nhỏ hơn điện trường cho phép.
- (b) Giới hạn điện trường, vì cường độ cho phép tính từ giới hạn điện trường nhỏ hơn.
- (c) Tùy tần số được chọn, vì cả hai giới hạn đều phụ thuộc tần số.
- (d) Không giới hạn nào chặt hơn, vì tại mỗi tần số chúng cho cùng cường độ.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Cần so sánh cùng một đại lượng là cường độ tương đương. Không so trực tiếp trị số đo bằng tesla với trị số đo bằng vôn trên mét.

**Hướng đi:**

- Quy mỗi giới hạn về cường độ sóng hình sin trong chân không.
- Lấy tỉ số hai cường độ. Cả hai cùng tỉ lệ $1/f_k^2$, nên tần số triệt tiêu.

Đặt $I_E$ và $I_B$ là cường độ suy từ hai giới hạn:

$$
\begin{aligned}
I_E &= \frac12\varepsilon_0c \left(\frac{350}{f_k}\right)^2, \\
I_B &= \frac{c}{2\mu_0} \left(\frac5{f_k}\right)^2.
\end{aligned}
$$

Vì $1/(\varepsilon_0\mu_0)=c^2$:

$$
\begin{aligned}
\frac{I_B}{I_E} &= c^2\left(\frac5{350}\right)^2 \\
&\approx 1{,}84\times10^{13}>1.
\end{aligned}
$$

Giới hạn điện trường cho cường độ tương đương nhỏ hơn, nên chọn (b). Lý do ở (a) không đúng về đơn vị. Hai giới hạn phụ thuộc tần số theo cùng một quy luật nên đáp án không đổi trong miền đã cho.

Kết quả chỉ trả lời phép so sánh toán học với các dữ kiện của bài. Với trường tần số thấp gần dây điện hoặc thiết bị, cần đánh giá các thành phần trường theo quy chuẩn thích hợp.
:::
