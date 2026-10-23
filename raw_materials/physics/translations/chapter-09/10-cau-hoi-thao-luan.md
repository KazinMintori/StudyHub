## Câu hỏi thảo luận

Nhóm 22 câu hỏi thảo luận sau giúp đào sâu bản chất vật lý của chuyển động quay của vật rắn quanh trục cố định, mối quan hệ giữa các đại lượng động học góc và dài, ý nghĩa vật lý của mômen quán tính và sự bảo toàn cơ năng trong các hệ thống quay thực tế.

---

### Q9.1

Công thức nào sau đây vẫn nghiệm đúng nếu gia tốc góc của vật không phải là hằng số? Giải thích lập luận của bạn trong từng trường hợp:
(a) $v = r\omega$.
(b) $a_{\mathrm{tan}} = r\alpha$.
(c) $\omega = \omega_0 + \alpha t$.
(d) $a_{\mathrm{tan}} = r\omega^2$.
(e) $K = \frac{1}{2}I\omega^2$.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Xét vật rắn quay quanh trục cố định với gia tốc góc biến thiên theo thời gian: $\alpha(t) \neq \mathrm{const}$.
- Đánh giá tính đúng đắn của 5 công thức (a), (b), (c), (d), (e).

**Hướng đi:**
- Phân biệt giữa các hệ thức định nghĩa vi phân tức thời (luôn đúng tại mọi thời điểm) với các công thức tích phân giả định gia tốc không đổi.
- Phân biệt giữa các thành phần gia tốc tiếp tuyến và gia tốc hướng tâm.

**Lời giải chi tiết:**

(a) $v = r\omega$: ĐÚNG. Hệ thức này suy ra trực tiếp từ định nghĩa độ dài cung tròn $s = r\theta$. Lấy đạo hàm theo thời gian:
$$
v = \frac{ds}{dt} = r\frac{d\theta}{dt} = r\omega
$$
Hệ thức là mối liên hệ tức thời giữa tốc độ dài và tốc độ góc của một điểm cách trục khoảng $r$, nghiệm đúng tại bất kỳ thời điểm nào dù $\alpha$ có biến thiên hay không.

(b) $a_{\mathrm{tan}} = r\alpha$: ĐÚNG. Gia tốc tiếp tuyến là tốc độ biến thiên của tốc độ dài. Lấy đạo hàm hệ thức $v = r\omega$ theo thời gian với bán kính $r$ không đổi:
$$
a_{\mathrm{tan}} = \frac{dv}{dt} = r\frac{d\omega}{dt} = r\alpha
$$
Phương trình này là hệ thức vi phân tức thời, luôn có giá trị tại mọi thời điểm.

(c) $\omega = \omega_0 + \alpha t$: SAI (không còn nghiệm đúng). Phương trình này là kết quả của phép tích phân:
$$
\int_{\omega_0}^\omega d\omega = \int_0^t \alpha\,dt
$$
Chỉ khi $\alpha$ là hằng số thì tích phân vế phải mới cho kết quả $\alpha t$. Nếu $\alpha$ biến thiên theo thời gian, dạng tổng quát phải là $\omega = \omega_0 + \int_0^t \alpha(t')\,dt'$.

(d) $a_{\mathrm{tan}} = r\omega^2$: SAI (sai bản chất công thức). Đại lượng $r\omega^2 = \frac{v^2}{r}$ là gia tốc hướng tâm $a_{\mathrm{rad}}$, đặc trưng cho sự thay đổi về phương của vector vận tốc hướng về tâm quỹ đạo. Gia tốc tiếp tuyến đặc trưng cho sự thay đổi về độ lớn của vận tốc và phải bằng $r\alpha$.

(e) $K = \frac{1}{2}I\omega^2$: ĐÚNG. Động năng của vật rắn là tổng động năng của từng phần tử khối lượng:
$$
\begin{aligned}
K &= \sum_i \frac{1}{2}m_i v_i^2 \\
&= \sum_i \frac{1}{2}m_i (r_i\omega)^2 \\
&= \frac{1}{2}\left(\sum_i m_i r_i^2\right)\omega^2 \\
&= \frac{1}{2}I\omega^2
\end{aligned}
$$
Động năng là hàm trạng thái phụ thuộc duy nhất vào phân bố khối lượng $I$ và tốc độ góc tức thời $\omega$ tại thời điểm khảo sát, hoàn toàn không phụ thuộc vào đạo hàm của tốc độ góc $\alpha$.

</details>

---

### Q9.2

Một phân tử hai nguyên tử có thể được mô hình hóa dưới dạng hai chất điểm mang khối lượng $m_1$ và $m_2$ đặt cách nhau một khoảng nhỏ (Hình Q9.2). Nếu phân tử định hướng dọc theo trục $y$, nó có động năng $K$ khi quay quanh trục $x$. Động năng của phân tử (tính theo $K$) sẽ bằng bao nhiêu nếu nó quay với cùng tốc độ góc quanh:
(a) Trục $z$?
(b) Trục $y$?

![Hình Q9.2: Mô hình phân tử hai nguyên tử nằm dọc theo trục y.](./img/young-09/c-hinh-q9-2.png)

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Hai chất điểm $m_1, m_2$ nằm trên trục $y$.
- Động năng quay quanh trục $x$ với tốc độ góc $\omega$ là $K_x = K$.
- Cần tìm: Động năng quay $K_z$ và $K_y$ với cùng tốc độ góc $\omega$.

**Hướng đi:**
- Động năng quay quanh một trục bất kỳ là $K = \frac{1}{2}I\omega^2$.
- Với cùng tốc độ góc $\omega$, động năng tỉ lệ thuận với mômen quán tính quanh trục quay tương ứng.
- Khoảng cách từ một điểm có tọa độ $(0, y_i, 0)$ trên trục $y$ đến trục $x$, trục $z$ và trục $y$ lần lượt là:
$$
\begin{aligned}
r_{ix} &= \sqrt{y_i^2 + 0^2} \\
&= |y_i|, \\
r_{iz} &= \sqrt{0^2 + y_i^2} \\
&= |y_i|, \\
r_{iy} &= \sqrt{0^2 + 0^2} \\
&= 0.
\end{aligned}
$$

**Lời giải chi tiết:**

1. Xác định mômen quán tính đối với trục $x$:
Vì hai chất điểm nằm trên trục $y$ tại các tọa độ $y_1$ và $y_2$, khoảng cách vuông góc từ mỗi hạt đến trục $x$ đúng bằng $|y_1|$ và $|y_2|$. Do đó:
$$
I_x = m_1 y_1^2 + m_2 y_2^2
$$
Động năng quay quanh trục $x$ là:
$$
\begin{aligned}
K &= \frac{1}{2}I_x\omega^2 \\
&= \frac{1}{2}(m_1 y_1^2 + m_2 y_2^2)\omega^2
\end{aligned}
$$

2. (a) Động năng quay quanh trục $z$:
Khoảng cách vuông góc từ mỗi hạt nằm trên trục $y$ đến trục $z$ cũng bằng $|y_1|$ và $|y_2|$. Mômen quán tính đối với trục $z$ là:
$$
I_z = m_1 y_1^2 + m_2 y_2^2 = I_x
$$
Với cùng tốc độ góc $\omega$, động năng quay quanh trục $z$ là:
$$
\begin{aligned}
K_z &= \frac{1}{2}I_z\omega^2 \\
&= \frac{1}{2}I_x\omega^2 \\
&= K
\end{aligned}
$$

3. (b) Động năng quay quanh trục $y$:
Vì cả hai chất điểm đều nằm chính xác trên trục $y$, khoảng cách từ mỗi hạt đến trục quay $y$ bằng $0$ ($r_{1y} = r_{2y} = 0$). Bỏ qua kích thước hữu hạn của bản thân từng hạt chất điểm, mômen quán tính đối với trục liên kết $y$ triệt tiêu:
$$
\begin{aligned}
I_y &= m_1(0)^2 + m_2(0)^2 \\
&= 0
\end{aligned}
$$
Do đó, động năng quay quanh trục $y$ bằng:
$$
K_y = \frac{1}{2}I_y\omega^2 = 0
$$

Kiểm tra: Đây chính là cơ sở vật lý giải thích vì sao trong nhiệt động lực học và cơ học lượng tử, phân tử khí lưỡng nguyên tử chỉ có $2$ bậc tự do quay quanh hai trục vuông góc với trục liên kết, trong khi chuyển động quay quanh trục liên kết không đóng góp vào nhiệt dung ở nhiệt độ thông thường.

</details>

---

### Q9.3

Sự khác biệt giữa gia tốc tiếp tuyến và gia tốc hướng tâm (pháp tuyến) đối với một điểm trên vật rắn đang quay là gì?

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- So sánh bản chất vật lý, phương chiều và biểu thức của gia tốc tiếp tuyến $a_{\mathrm{tan}}$ và gia tốc hướng tâm $a_{\mathrm{rad}}$.

**Hướng đi:**
- Phân tích đạo hàm của vector vận tốc trong tọa độ tự nhiên:
$$
\vec{a} = \frac{d\vec{v}}{dt} = \frac{dv}{dt}\hat{u}_t + \frac{v^2}{r}\hat{u}_n
$$

**Lời giải chi tiết:**

Gia tốc của một điểm chuyển động tròn trên vật rắn quay được phân tách thành hai thành phần trực giao mang ý nghĩa vật lý hoàn toàn khác biệt:

1. **Gia tốc tiếp tuyến ($a_{\mathrm{tan}}$)**:
- **Phương chiều**: Luôn tiếp tuyến với quỹ đạo tròn tại điểm khảo sát, cùng chiều với vector vận tốc khi chuyển động quay nhanh dần và ngược chiều khi quay chậm dần.
- **Biểu thức**: $a_{\mathrm{tan}} = r\alpha = \frac{dv}{dt}$.
- **Bản chất vật lý**: Đặc trưng cho tốc độ biến thiên về **độ lớn** (tốc độ dài) của vector vận tốc. Nếu vật rắn quay đều ($\alpha = 0$), gia tốc tiếp tuyến triệt tiêu hoàn toàn.

2. **Gia tốc hướng tâm hay pháp tuyến ($a_{\mathrm{rad}}$)**:
- **Phương chiều**: Nằm dọc theo phương bán kính nối điểm đang xét với trục quay, luôn hướng thẳng vào trục quay (tâm quỹ đạo).
- **Biểu thức**: $a_{\mathrm{rad}} = r\omega^2 = \frac{v^2}{r}$.
- **Bản chất vật lý**: Đặc trưng cho tốc độ biến thiên về **phương hướng** của vector vận tốc để giữ cho điểm chuyển động bẻ cong theo quỹ đạo tròn. Thành phần này luôn tồn tại chừng nào vật rắn còn đang quay ($\omega \neq 0$), ngay cả khi chuyển động quay là hoàn toàn đều đặn.

</details>

---

### Q9.4

Ở Hình Q9.4, tất cả các điểm trên sợi xích đều có cùng tốc độ dài. Độ lớn gia tốc dài có giống nhau đối với mọi điểm trên xích hay không? Gia tốc góc của hai đĩa xích liên hệ với nhau như thế nào? Giải thích.

![Hình Q9.4: Hệ thống truyền động xích xe đạp gồm đĩa xích trước và đĩa xích sau.](./img/young-09/c-hinh-q9-4.png)

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Sợi xích truyền động nối đĩa xích trước (bán kính $r_{\mathrm{front}}$) và đĩa xích sau (bán kính $r_{\mathrm{rear}}$).
- Các mắt xích có cùng tốc độ dài $v$.
- Cần giải thích: (a) Độ lớn gia tốc toàn phần của các điểm trên xích có như nhau không; (b) Mối liên hệ giữa gia tốc góc $\alpha_{\mathrm{front}}$ và $\alpha_{\mathrm{rear}}$.

**Hướng đi:**
- Phân tích chuyển động của mắt xích trên các đoạn thẳng và các đoạn ôm quanh đĩa xích tròn.
- Sử dụng điều kiện tiếp xúc không trượt giữa xích và các răng đĩa để liên hệ gia tốc tiếp tuyến.

**Lời giải chi tiết:**

1. **Về độ lớn gia tốc dài của các điểm trên sợi xích**:
Độ lớn gia tốc dài KHÔNG giống nhau đối với mọi điểm trên xích.
- Trên các nhánh xích căng thẳng nằm giữa hai đĩa: Các mắt xích chuyển động tịnh tiến thẳng, quỹ đạo không uốn cong nên bán kính cong bằng vô cùng ($a_{\mathrm{rad}} = 0$). Gia tốc của các mắt xích này thuần túy là gia tốc tiếp tuyến $a = a_{\mathrm{tan}} = \frac{dv}{dt}$.
- Trên các đoạn xích đang ôm quanh đĩa xích: Mắt xích chuyển động tròn có bán kính $r$, do đó ngoài gia tốc tiếp tuyến $a_{\mathrm{tan}} = \frac{dv}{dt}$, nó còn chịu thêm gia tốc hướng tâm:
$$
a_{\mathrm{rad}} = \frac{v^2}{r}
$$
Vì bán kính của đĩa trước và đĩa sau khác nhau ($r_{\mathrm{rear}} < r_{\mathrm{front}}$), gia tốc hướng tâm của mắt xích khi đi qua đĩa sau lớn hơn khi đi qua đĩa trước ($v^2/r_{\mathrm{rear}} > v^2/r_{\mathrm{front}}$).
Độ lớn gia tốc toàn phần là $a = \sqrt{a_{\mathrm{tan}}^2 + a_{\mathrm{rad}}^2}$, do đó gia tốc của các điểm trên xích khác nhau tùy thuộc vào vị trí của mắt xích.

2. **Mối liên hệ giữa gia tốc góc của hai đĩa xích**:
Vì xích không dãn và ăn khớp hoàn hảo không trượt với các răng đĩa, vành ngoài của hai đĩa xích chuyển động với cùng tốc độ tiếp tuyến $v = r_{\mathrm{front}}\omega_{\mathrm{front}} = r_{\mathrm{rear}}\omega_{\mathrm{rear}}$.
Lấy đạo hàm theo thời gian, gia tốc tiếp tuyến của hai vành đĩa phải bằng nhau:
$$
\begin{aligned}
a_{\mathrm{tan}} &= r_{\mathrm{front}}\alpha_{\mathrm{front}} \\
&= r_{\mathrm{rear}}\alpha_{\mathrm{rear}}
\end{aligned}
$$

Từ đó suy ra tỉ số gia tốc góc:
$$
\frac{\alpha_{\mathrm{rear}}}{\alpha_{\mathrm{front}}} = \frac{r_{\mathrm{front}}}{r_{\mathrm{rear}}}
$$

Đĩa xích sau có bán kính nhỏ hơn nên luôn có gia tốc góc lớn hơn đĩa xích trước theo tỉ lệ nghịch với bán kính.

</details>

---

### Q9.5

Ở Hình Q9.4, gia tốc hướng tâm của các điểm tại răng của hai đĩa xích liên hệ với nhau như thế nào? Giải thích.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Xét các điểm nằm tại vành răng của đĩa xích trước (bán kính $r_{\mathrm{front}}$) và đĩa xích sau (bán kính $r_{\mathrm{rear}}$) trong Hình Q9.4.
- Cần tìm: Mối liên hệ giữa gia tốc hướng tâm $a_{\mathrm{rad, front}}$ và $a_{\mathrm{rad, rear}}$.

**Hướng đi:**
- Do xích không trượt trên răng đĩa, tốc độ tiếp tuyến tại răng của cả hai đĩa xích bằng đúng tốc độ dài $v$ của sợi xích.
- Biểu diễn gia tốc hướng tâm qua tốc độ tiếp tuyến $a_{\mathrm{rad}} = \frac{v^2}{r}$.

**Lời giải chi tiết:**

Tại vị trí tiếp xúc với xích, các điểm tại vành răng của hai đĩa xích chuyển động tròn với cùng tốc độ dài $v$.

Gia tốc hướng tâm của điểm ở răng đĩa xích sau là:
$$
a_{\mathrm{rad, rear}} = \frac{v^2}{r_{\mathrm{rear}}}
$$

Gia tốc hướng tâm của điểm ở răng đĩa xích trước là:
$$
a_{\mathrm{rad, front}} = \frac{v^2}{r_{\mathrm{front}}}
$$

Lập tỉ số giữa hai gia tốc hướng tâm:
$$
\begin{aligned}
\frac{a_{\mathrm{rad, rear}}}{a_{\mathrm{rad, front}}} &= \frac{v^2 / r_{\mathrm{rear}}}{v^2 / r_{\mathrm{front}}} \\
&= \frac{r_{\mathrm{front}}}{r_{\mathrm{rear}}}
\end{aligned}
$$

Vì đĩa xích sau có bán kính nhỏ hơn đĩa xích trước ($r_{\mathrm{rear}} < r_{\mathrm{front}}$), các điểm tại vành răng của đĩa xích sau luôn chịu gia tốc hướng tâm lớn hơn các điểm tại vành răng của đĩa xích trước theo đúng tỉ lệ nghịch của hai bán kính:
$$
\frac{a_{\mathrm{rad,rear}}}{a_{\mathrm{rad,front}}}=\frac{r_{\mathrm{front}}}{r_{\mathrm{rear}}}.
$$

</details>

---

### Q9.6

Một bánh đà quay với vận tốc góc không đổi. Một điểm trên mép của bánh đà có gia tốc tiếp tuyến hay không? Có gia tốc hướng tâm hay không? Các gia tốc này có không đổi về độ lớn hay không? Có không đổi về hướng hay không? Giải thích trong từng trường hợp.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Bánh đà quay đều: $\vec{\omega} = \mathrm{const}$.
- Khảo sát điểm trên mép bánh đà bán kính $R$: Gia tốc tiếp tuyến, gia tốc hướng tâm, độ lớn và hướng của chúng.

**Hướng đi:**
- Vận dụng định nghĩa $a_{\mathrm{tan}} = R\alpha$ và $a_{\mathrm{rad}} = R\omega^2$.
- Phân tích tính chất vector (độ lớn và hướng) khi điểm quay tròn trong không gian.

**Lời giải chi tiết:**

1. **Gia tốc tiếp tuyến**:
Vì vận tốc góc không đổi ($\omega = \mathrm{const}$), gia tốc góc của bánh đà triệt tiêu:
$$
\alpha = \frac{d\omega}{dt} = 0
$$
Do đó điểm trên mép bánh đà **không có gia tốc tiếp tuyến**:
$$
a_{\mathrm{tan}} = R\alpha = 0
$$

2. **Gia tốc hướng tâm**:
Điểm trên mép bánh đà chuyển động trên quỹ đạo tròn nên phương của vector vận tốc liên tục thay đổi, do đó điểm **luôn có gia tốc hướng tâm**:
$$
a_{\mathrm{rad}} = R\omega^2 = \frac{v^2}{R} > 0
$$

3. **Về độ lớn của gia tốc**:
Độ lớn gia tốc hướng tâm $a_{\mathrm{rad}} = R\omega^2$ là **hằng số không đổi**, vì cả bán kính $R$ và tốc độ góc $\omega$ đều không đổi theo thời gian.

4. **Về hướng của gia tốc**:
Hướng của vector gia tốc hướng tâm **không đổi về bản chất quy chiếu hướng vào tâm**, nhưng **liên tục thay đổi trong không gian**. Khi điểm trên vành quay tròn, vector gia tốc hướng tâm quay theo góc $\theta(t)$ trong mặt phẳng bánh đà, liên tục đổi hướng (lúc hướng sang trái, lúc hướng sang phải, lúc hướng lên, lúc hướng xuống). Vì hướng thay đổi, vector gia tốc $\vec{a}$ không phải là vector không đổi.

</details>

---

### Q9.7

Mục đích của chu trình vắt trong máy giặt là gì? Hãy giải thích nguyên lý hoạt động dựa trên các thành phần gia tốc.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Giải thích cơ chế tách nước khỏi quần áo trong chu trình vắt của máy giặt dựa trên các thành phần gia tốc.

**Hướng đi:**
- Khảo sát chuyển động tròn của lồng giặt ở tốc độ góc cao $\omega$.
- Phân tích lực liên kết giữ nước với sợi vải đối chiếu với lực hướng tâm cần thiết.

**Lời giải chi tiết:**

Mục đích của chu trình vắt là loại bỏ phần lớn lượng nước thấm trong quần áo trước khi đem phơi hoặc sấy.

Cơ chế hoạt động giải thích thông qua các thành phần gia tốc như sau:
1. Trong chu trình vắt, lồng giặt quay xung quanh trục với tốc độ góc $\omega$ rất lớn. Quần áo bị ép chặt vào thành lồng giặt có đục nhiều lỗ nhỏ.
2. Để một giọt nước hoặc một phần tử quần áo chuyển động tròn bán kính $r$ theo lồng giặt, nó bắt buộc phải có một gia tốc hướng tâm rất lớn:
$$
a_{\mathrm{rad}} = r\omega^2
$$
Theo định luật II Newton, gia tốc này đòi hỏi một hợp lực hướng tâm có độ lớn:
$$
F_{\mathrm{ht}} = m a_{\mathrm{rad}} = m r\omega^2
$$
3. Đối với quần áo, thành lồng giặt rắn chắc tác dụng phản lực pháp tuyến hướng vào tâm để cung cấp lực hướng tâm này, giữ quần áo ở lại trong quỹ đạo tròn.
4. Đối với các giọt nước đọng trên vải, lực giữ chúng lại chỉ là lực dính ướt (lực liên kết phân tử giữa nước và sợi vải). Khi tốc độ góc $\omega$ tăng cao, lực hướng tâm cần thiết $m r\omega^2$ vượt quá giới hạn cực đại của lực dính ướt.
5. Khi đó, lực dính ướt không thể cung cấp đủ gia tốc hướng tâm $a_{\mathrm{rad}}$. Do quán tính, các giọt nước có xu hướng tiếp tục chuyển động theo phương tiếp tuyến với vận tốc dài $v = r\omega$ và văng qua các lỗ thoát nước trên thành lồng giặt ra ngoài, tách rời hoàn toàn khỏi quần áo.

</details>

---

### Q9.8

Bạn đang thiết kế một bánh đà để lưu trữ động năng. Giả sử tất cả các vật thể đồng chất sau đây đều có cùng khối lượng và cùng vận tốc góc, vật thể nào sẽ lưu trữ lượng động năng lớn nhất? Vật thể nào sẽ lưu trữ lượng động năng nhỏ nhất? Giải thích.
(a) Một quả cầu đặc đường kính $D$ quay quanh một trục đi qua đường kính.
(b) Một hình trụ đặc đường kính $D$ quay quanh trục đối xứng đi qua tâm các mặt đáy.
(c) Một hình trụ rỗng thành mỏng đường kính $D$ quay quanh trục đối xứng đi qua tâm mặt tròn.
(d) Một thanh mảnh đồng chất chiều dài $D$ quay quanh trục vuông góc với thanh tại tâm.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- 4 vật đồng chất cùng khối lượng $M$, cùng kích thước đặc trưng $D$ (bán kính $R = D/2$ hoặc chiều dài $L = D$), cùng tốc độ góc $\omega$.
- Cần tìm: Vật có động năng lớn nhất và nhỏ nhất.

**Hướng đi:**
- Động năng quay là $K = \frac{1}{2}I\omega^2$. Với cùng $M$ và $\omega$, động năng tỉ lệ thuận trực tiếp với mômen quán tính $I$.
- Tra cứu và quy đổi mômen quán tính của từng vật thể về dạng $c M D^2$, từ đó so sánh các hệ số $c$.

**Lời giải chi tiết:**

Biểu diễn mômen quán tính của từng vật theo khối lượng $M$ và đường kính $D$ (bán kính $R = D/2$):

1. **(a) Quả cầu đặc đồng chất bán kính $R = D/2$**:
$$
\begin{aligned}
I_a &= \frac{2}{5}MR^2 \\
&= \frac{2}{5}M\left(\frac{D}{2}\right)^2 \\
&= \frac{1}{10}MD^2 \\
&= 0{,}100\,MD^2
\end{aligned}
$$

2. **(b) Hình trụ đặc đồng chất bán kính $R = D/2$**:
$$
\begin{aligned}
I_b &= \frac{1}{2}MR^2 \\
&= \frac{1}{2}M\left(\frac{D}{2}\right)^2 \\
&= \frac{1}{8}MD^2 \\
&= 0{,}125\,MD^2
\end{aligned}
$$

3. **(c) Hình trụ rỗng thành mỏng bán kính $R = D/2$**:
$$
\begin{aligned}
I_c &= MR^2 \\
&= M\left(\frac{D}{2}\right)^2 \\
&= \frac{1}{4}MD^2 \\
&= 0{,}250\,MD^2
\end{aligned}
$$

4. **(d) Thanh mảnh đồng chất chiều dài $L = D$, trục qua tâm**:
$$
\begin{aligned}
I_d &= \frac{1}{12}ML^2 \\
&= \frac{1}{12}MD^2 \\
&\approx 0{,}0833\,MD^2
\end{aligned}
$$

So sánh độ lớn mômen quán tính:
$$
I_c>I_b>I_a>I_d.
$$

Kết luận:
- **Lưu trữ động năng lớn nhất**: (c) Hình trụ rỗng thành mỏng. Toàn bộ khối lượng của hình trụ rỗng đều phân bố ở khoảng cách xa trục quay nhất ($r = D/2$).
- **Lưu trữ động năng nhỏ nhất**: (d) Thanh mảnh đồng chất. Khối lượng phân bố rải rác từ tâm ra hai đầu, bình phương khoảng cách trung bình chỉ bằng $(D/2)^2 / 3 = D^2/12$.

</details>

---

### Q9.9

Bạn có thể nghĩ ra một vật thể nào có cùng mômen quán tính đối với mọi trục quay có thể có trong không gian hay không? Nếu có, hãy nêu ví dụ; nếu không, hãy giải thích vì sao điều này không thể xảy ra. Bạn có thể nghĩ ra một vật thể nào có cùng mômen quán tính đối với mọi trục quay đi qua một điểm xác định hay không? Nếu có, hãy nêu ví dụ và chỉ rõ điểm đó nằm ở đâu.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Đánh giá sự tồn tại của: (1) Vật có $I$ giống nhau đối với mọi trục bất kỳ trong không gian; (2) Vật có $I$ giống nhau đối với mọi trục đi qua một điểm xác định.

**Hướng đi:**
- Sử dụng định lý trục song song $I = I_{\mathrm{cm}} + Md^2$ để khảo sát tính biến thiên của $I$ theo khoảng cách $d$.
- Sử dụng tính đối xứng hình học cầu để khảo sát các trục đi qua tâm.

**Lời giải chi tiết:**

1. **Đối với mọi trục quay bất kỳ trong không gian: KHÔNG THỂ CÓ**.
Theo định lý trục song song, mômen quán tính của một vật đối với một trục bất kỳ nằm cách trục song song đi qua khối tâm một khoảng $d$ được tính bởi:
$$
I = I_{\mathrm{cm}} + Md^2
$$
- Đối với một trục đi qua khối tâm, khoảng cách $d = 0$, mômen quán tính nhận giá trị cực tiểu $I = I_{\mathrm{cm}}$.
- Nếu chọn một trục khác tịnh tiến ra xa khối tâm ở khoảng cách $d > 0$, mômen quán tính tăng thêm một lượng $Md^2 > 0$.
Vì khoảng cách $d$ từ một trục đến khối tâm có thể nhận giá trị biến thiên tùy ý từ $0$ đến vô cùng, $I$ bắt buộc phải thay đổi theo khoảng cách $d$. Do đó không thể tồn tại bất kỳ vật thể nào có cùng mômen quán tính đối với mọi trục trong không gian.

2. **Đối với mọi trục quay đi qua một điểm xác định: HOÀN TOÀN CÓ THỂ**.
- **Ví dụ**: Một quả cầu đặc đồng chất (hoặc một vỏ cầu rỗng đồng chất) có khối lượng $M$ và bán kính $R$.
- **Vị trí của điểm**: Điểm đó chính là **khối tâm (tâm đối xứng)** của quả cầu.
- **Giải thích**: Do quả cầu có tính đối xứng cầu hoàn hảo, mọi đường thẳng đi qua tâm của quả cầu đều là trục đối xứng hoàn toàn tương đương nhau. Do đó, mômen quán tính của quả cầu đặc đối với bất kỳ trục nào đi qua tâm đều bằng đúng $I = \frac{2}{5}MR^2$ (đối với vỏ cầu mỏng là $I = \frac{2}{3}MR^2$).

</details>

---

### Q9.10

Để tối đa hóa mômen quán tính của một bánh đà trong khi tối thiểu hóa khối lượng của nó, bánh đà nên có hình dạng và sự phân bố khối lượng như thế nào? Giải thích.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Thiết kế hình học bánh đà để đạt tỉ số $I/M$ lớn nhất có thể.

**Hướng đi:**
- Xuất phát từ định nghĩa vi phân $I = \int r^2\,dm$ để lập luận về khoảng cách phân bố khối lượng $r$.

**Lời giải chi tiết:**

1. Mômen quán tính của một vật thể được định nghĩa bởi tích phân:
$$
I = \int r^2\,dm
$$
trong đó $r$ là khoảng cách vuông góc từ phần tử khối lượng $dm$ đến trục quay.

2. Để cực đại hóa giá trị tích phân $I$ với một khối lượng tổng cộng $M = \int dm$ cho trước ở mức nhỏ nhất, giá trị $r^2$ của mọi phần tử khối lượng phải đạt mức lớn nhất có thể.

3. Do đó, cấu trúc tối ưu của bánh đà phải thỏa mãn:
- Hầu hết toàn bộ khối lượng của bánh đà tập trung ở một **vành tròn ngoài cùng (vành đai mỏng)** có bán kính $R$ lớn nhất cho phép.
- Phần nối giữa vành ngoài và trục quay ở tâm được làm bằng các **nan hoa thanh mảnh, nhẹ** hoặc một đĩa mỏng có gân trợ lực với khối lượng chiếm tỉ lệ không đáng kể.

Khi đó, mômen quán tính đạt xấp xỉ mức trần lý thuyết $I \approx MR^2$, mang lại khả năng tích trữ động năng và ổn định chuyển động quay tối đa trên mỗi đơn vị khối lượng.

</details>

---

### Q9.11

Bạn có thể xác định mômen quán tính của một vật có hình dạng bất kỳ đối với một trục đã cho bằng thực nghiệm như thế nào?

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Đề xuất phương án thực nghiệm đo mômen quán tính $I$ của vật thể có hình dạng bất đối xứng/không quy chuẩn quanh một trục cố định.

**Hướng đi:**
- Vận dụng các định luật bảo toàn cơ năng hoặc định luật chuyển động quay (phương pháp động học hoặc con lắc xoắn).

**Lời giải chi tiết:**

Có thể xác định $I$ bằng thực nghiệm thông qua hai phương pháp đo cơ bản:

**Phương pháp 1: Sử dụng vật rơi và bảo toàn cơ năng (hoặc gia tốc dài)**:
1. Gắn vật rắn cần đo lên một trục quay cố định có ổ bi ma sát không đáng kể.
2. Gắn đồng trục với vật một tang trống hình trụ có bán kính $r$ đã biết. Quấn một sợi dây nhẹ không dãn quanh tang trống và treo một quả nặng khối lượng $m$ vào đầu dây tự do.
3. Thả quả nặng rơi từ trạng thái nghỉ từ độ cao $h$. Dùng cảm biến thời gian để đo thời gian rơi $t$ (hoặc đo tốc độ chạm đất $v$).
4. Gia tốc rơi của quả nặng là $a = \frac{2h}{t^2}$, vận tốc góc của hệ khi đó là $\omega = \frac{v}{r} = \frac{at}{r}$.
5. Áp dụng định luật bảo toàn cơ năng:
$$
2mgh = mv^2 + I_{\mathrm{tong}}\omega^2
$$
với $I_{\mathrm{tong}} = I + I_{\mathrm{tang}}$. Từ đó suy ra mômen quán tính của vật:
Đặt $J=I+I_{\mathrm{tang}}$, là momen quán tính tổng của vật và tang quấn dây. Khi đó:

$$
\frac{J}{mr^2}=\frac{2gh}{v^2}-1.
$$

Với chuyển động từ nghỉ có gia tốc không đổi, $v=2h/t$, nên:

$$
\frac{J}{mr^2}=\frac{gt^2}{2h}-1.
$$

Từ $J$ suy ra $I=J-I_{\mathrm{tang}}$.

**Phương pháp 2: Sử dụng con lắc xoắn**:
1. Treo vật thể vào một dây kim loại đàn hồi sao cho trục cần đo trùng với phương của dây treo. Dây có mômen xoắn hồi phục $\tau = -\kappa\theta$ với hằng số xoắn $\kappa$ đã biết từ trước.
2. Xoay vật đi một góc nhỏ rồi thả tự do để hệ dao động điều hòa quanh trục.
3. Đo chu kỳ dao động $T$ của con lắc xoắn. Chu kỳ liên hệ với mômen quán tính qua hệ thức $T = 2\pi\sqrt{I/\kappa}$.
4. Rút ra mômen quán tính cần tìm:
$$
I = \frac{\kappa T^2}{4\pi^2}
$$

</details>

---

### Q9.12

Một vật thể hình trụ có khối lượng $M$ và bán kính $R$. Khối lượng bên trong vật thể có thể được phân bố theo cách nào đó để mômen quán tính của nó đối với trục đối xứng lớn hơn $MR^2$ hay không? Giải thích.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Vật hình trụ khối lượng $M$, bán kính ngoài $R$.
- Đánh giá khả năng $I > MR^2$ quanh trục đối xứng.

**Hướng đi:**
- Đánh giá cận trên của tích phân định nghĩa mômen quán tính dựa trên miền hình học của vật thể hình trụ.

**Lời giải chi tiết:**

**KHÔNG THỂ**. Khối lượng không thể phân bố theo bất kỳ cách nào để $I > MR^2$.

Chứng minh bằng đánh giá giải tích:
1. Xét một vật thể hình trụ bán kính ngoài $R$. Mọi phần tử khối lượng $dm$ nằm bên trong hoặc trên bề mặt hình trụ đều có khoảng cách $r$ đến trục đối xứng thỏa mãn bất đẳng thức hình học:
$$
0 \le r \le R
$$
2. Bình phương khoảng cách của từng phần tử khối lượng do đó bị chặn trên bởi:
$$
r^2 \le R^2
$$
3. Mômen quán tính của vật được tính bằng tích phân:
$$
\begin{aligned}
I &= \int r^2\,dm \le \int R^2\,dm \\
&= R^2\int dm \\
&= MR^2
\end{aligned}
$$
4. Đẳng thức $I = MR^2$ chỉ đạt được trong trường hợp giới hạn lý tưởng khi toàn bộ khối lượng $100\%$ tập trung chính xác tại mặt ngoài ở khoảng cách $r = R$ (hình trụ rỗng thành vô cùng mỏng).
5. Đối với bất kỳ vật thể thực nào có khối lượng phân bố ở bên trong ($r < R$), tích phân bắt buộc phải nhỏ hơn giá trị giới hạn: $I < MR^2$.

Do đó, $MR^2$ là chặn trên tuyệt đối của mômen quán tính đối với bất kỳ phân bố khối lượng nào bên trong hình trụ bán kính $R$.

</details>

---

### Q9.13

Hãy mô tả cách bạn có thể sử dụng kết quả ở phần (b) của Bảng 9.2 để suy ra kết quả ở phần (d).

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Dùng công thức thanh mảnh quay quanh một đầu trong Bảng 9.2(b) ($I = \frac{1}{3}ML^2$) để suy ra công thức tấm chữ nhật mỏng quay quanh một cạnh trong Bảng 9.2(d) ($I = \frac{1}{3}Ma^2$).

**Hướng đi:**
- Chia tấm phẳng chữ nhật thành tập hợp các dải hẹp song song, mỗi dải đóng vai trò như một thanh mảnh quay quanh đầu mút.
- Tích hợp mômen quán tính của tất cả các dải.

**Lời giải chi tiết:**

1. **Dữ liệu xuất phát từ Bảng 9.2(b)**:
Mômen quán tính của một thanh mảnh đồng chất chiều dài $L$ và khối lượng $m_{\mathrm{thanh}}$ đối với trục quay vuông góc với thanh tại một đầu là:
$$
I = \frac{1}{3}m_{\mathrm{thanh}}L^2
$$

2. **Thiết lập mô hình phân rã tấm chữ nhật ở Bảng 9.2(d)**:
Xét một tấm phẳng chữ nhật đồng chất mỏng có kích thước chiều dài cạnh $a$ (vuông góc với trục quay) và chiều rộng $b$ (dọc theo trục quay), khối lượng tổng cộng là $M$. Trục quay nằm dọc theo mép có chiều dài $b$.

3. Ta chia tấm chữ nhật thành vô số dải hẹp có chiều rộng vi phân $dy$ song song với cạnh $a$.
- Mỗi dải hẹp có chiều dài đúng bằng $a$.
- Trục quay nằm vuông góc với chiều dài $a$ tại một đầu mút của dải.
- Do đó, mỗi dải hẹp hoạt động giống hệt như một thanh mảnh đồng chất chiều dài $a$ quay quanh một đầu.

4. Khối lượng của một dải hẹp vi phân là:
$$
dm = \frac{M}{b}\,dy
$$
Áp dụng công thức Bảng 9.2(b) cho dải này:
$$
\begin{aligned}
dI &= \frac{1}{3}(dm)a^2 \\
&= \frac{1}{3}\left(\frac{M}{b}\,dy\right)a^2
\end{aligned}
$$

5. Tích phân trên toàn bộ bề rộng của tấm từ $y = 0$ đến $y = b$:
$$
\begin{aligned}
I &= \int dI \\
&= \frac{1}{3}\frac{Ma^2}{b}\int_0^b dy \\
&= \frac{1}{3}\frac{Ma^2}{b}(b) \\
&= \frac{1}{3}Ma^2
\end{aligned}
$$

Kết quả thu được trùng khớp hoàn toàn với phần (d) của Bảng 9.2.

</details>

---

### Q9.14

Một vỏ cầu rỗng bán kính $R$ đang quay quanh trục đi qua tâm của nó có động năng quay là $K$. Nếu bạn muốn sửa đổi quả cầu này sao cho nó có động năng quay gấp ba lần ở cùng tốc độ góc trong khi vẫn giữ nguyên khối lượng, bán kính mới của nó theo $R$ phải bằng bao nhiêu?

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Vỏ cầu rỗng bán kính $R$, khối lượng $M$, tốc độ góc $\omega$, động năng $K$.
- Cần tìm bán kính $R'$ để $K' = 3K$ với cùng khối lượng $M$ và cùng tốc độ góc $\omega$.

**Hướng đi:**
- Biểu diễn động năng quay của vỏ cầu rỗng qua mômen quán tính $I = \frac{2}{3}MR^2$.
- Lập tỉ số động năng để suy ra tỉ số bán kính.

**Lời giải chi tiết:**

1. Mômen quán tính của vỏ cầu rỗng bán kính $R$ quay quanh trục qua tâm là:
$$
I = \frac{2}{3}MR^2
$$

2. Động năng quay ban đầu của vỏ cầu là:
$$
\begin{aligned}
K &= \frac{1}{2}I\omega^2 \\
&= \frac{1}{2}\left(\frac{2}{3}MR^2\right)\omega^2 \\
&= \frac{1}{3}MR^2\omega^2
\end{aligned}
$$

3. Động năng quay của vỏ cầu mới có bán kính $R'$ với cùng khối lượng $M$ và cùng tốc độ góc $\omega$ là:
$$
K' = \frac{1}{3}M(R')^2\omega^2
$$

4. Theo yêu cầu bài toán, $K' = 3K$:
Rút gọn thừa số chung $M\omega^2/3$ trong điều kiện $K'=3K$:

$$
(R')^2=3R^2.
$$

5. Triệt tiêu các đại lượng chung $\frac{1}{3}M\omega^2$ ở cả hai vế:
$$
(R')^2 = 3R^2
$$

Từ đó:

$$
\begin{aligned}
R' &= \sqrt{3}R \\
&\approx 1{,}732\,R
\end{aligned}
$$

Bán kính mới của vỏ cầu phải tăng lên bằng $\sqrt{3}$ lần bán kính ban đầu.

</details>

---

### Q9.15

Để các phương trình tính $I$ đưa ra ở phần (a) và (b) của Bảng 9.2 nghiệm đúng, thanh có bắt buộc phải có tiết diện hình tròn hay không? Có bất kỳ hạn chế nào về kích thước của tiết diện ngang để các phương trình này áp dụng được hay không? Giải thích.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Khảo sát các điều kiện về hình dạng và kích thước tiết diện ngang của thanh mảnh trong công thức $I = \frac{1}{12}ML^2$ và $I = \frac{1}{3}ML^2$.

**Hướng đi:**
- Xem xét giả thiết xấp xỉ thanh mảnh trong phép lấy tích phân một chiều $dm = \lambda dx$.

**Lời giải chi tiết:**

1. **Về hình dạng tiết diện ngang: KHÔNG BẮT BUỘC TRÒN**.
Tiết diện ngang của thanh có thể là hình tròn, hình vuông, hình chữ nhật, hình tam giác hoặc bất kỳ hình dạng nào khác, miễn là tiết diện đó đồng nhất dọc theo toàn bộ chiều dài thanh để mật độ dài $\lambda = M/L$ là hằng số.

2. **Về kích thước tiết diện ngang: CÓ HẠN CHẾ RÕ RỆT**.
Kích thước ngang (đường kính, bề rộng hoặc bề dày) của tiết diện phải **nhỏ hơn rất nhiều so với chiều dài $L$ của thanh** ($w \ll L$).
- **Giải thích**: Trong phép tích phân tính mômen quán tính một chiều, ta đã giả định toàn bộ khối lượng của phần tử vi phân $dx$ ở vị trí $x$ đều có cùng khoảng cách vuông góc đến trục quay bằng đúng $|x|$.
- Nếu tiết diện thanh có kích thước ngang hữu hạn $R$ (ví dụ: Hình trụ tròn bán kính $R$), định lý trục song song và tích phân ba chiều cho thấy mômen quán tính thực tế đối với trục vuông góc đi qua khối tâm là:
$$
I = \frac{1}{12}ML^2 + \frac{1}{4}MR^2
$$
- Để số hạng thứ hai $\frac{1}{4}MR^2$ có thể bỏ qua một cách an toàn so với $\frac{1}{12}ML^2$, ta bắt buộc phải có $(R/L)^2 \ll 1$, tức là $R \ll L$. Nếu thanh quá dày (ví dụ chiều dài chỉ gấp đôi đường kính), các công thức thanh mảnh ở Bảng 9.2(a, b) sẽ dẫn tới sai số đáng kể.

</details>

---

### Q9.16

Ở phần (d) của Bảng 9.2, bề dày của tấm phẳng phải nhỏ hơn rất nhiều so với kích thước $a$ để biểu thức tính $I$ có thể áp dụng được. Nhưng ở phần (c), biểu thức tính $I$ vẫn áp dụng được bất kể tấm phẳng dày bao nhiêu. Giải thích.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- So sánh vai trò của bề dày tấm phẳng giữa Bảng 9.2(d) ($I = \frac{1}{3}Ma^2$) và Bảng 9.2(c) ($I = \frac{1}{12}M(a^2 + b^2)$).

**Hướng đi:**
- Phân tích tọa độ khoảng cách từ phần tử khối lượng đến trục quay trong không gian ba chiều $(x, y, z)$.

**Lời giải chi tiết:**

1. **Trong trường hợp Bảng 9.2(c) (trục quay vuông góc với mặt tấm $a \times b$ và đi qua tâm)**:
- Chọn trục quay là trục $z$. Khoảng cách vuông góc từ một phần tử khối lượng bất kỳ tại tọa độ $(x, y, z)$ đến trục $z$ được xác định bởi:
$$
r_{\perp} = \sqrt{x^2 + y^2}
$$
- Đại lượng $r_{\perp}$ hoàn toàn **độc lập với tọa độ $z$** dọc theo bề dày của tấm.
- Khi tấm có bề dày $t$ bất kỳ dọc theo phương $z$, ta có thể cắt vật thể thành các lớp mỏng có bề dày $dz$. Mỗi lớp mỏng đều có cùng kích thước mặt đáy $a \times b$ và cùng mômen quán tính tỉ lệ với khối lượng của lớp đó: $dI = \frac{1}{12}(dm)(a^2 + b^2)$.
- Tích phân cộng các lớp dọc theo trục $z$ bảo toàn nguyên vẹn thừa số $(a^2 + b^2)$. Do đó công thức $I = \frac{1}{12}M(a^2 + b^2)$ nghiệm đúng chính xác tuyệt đối với **mọi bề dày $t$**, kể cả một thanh lăng trụ chữ nhật rất dài.

2. **Trong trường hợp Bảng 9.2(d) (trục quay nằm dọc theo một mép của tấm mỏng)**:
- Trục quay nằm dọc theo mép cạnh $b$. Khoảng cách từ một phần tử khối lượng đến trục quay không chỉ phụ thuộc vào tọa độ $x$ (theo chiều dài cạnh $a$) mà còn phụ thuộc vào tọa độ $z$ (theo bề dày $t$ của tấm):
$$
r_{\perp} = \sqrt{x^2 + z^2}
$$
- Mômen quán tính chính xác khi xét đến bề dày $t$ là:
$$
I = \frac{1}{3}Ma^2 + \frac{1}{12}Mt^2
$$
- Biểu thức $I = \frac{1}{3}Ma^2$ trong Bảng 9.2(d) đã bỏ qua số hạng $\frac{1}{12}Mt^2$. Muốn phép xấp xỉ này chính xác, ta bắt buộc phải có điều kiện bề dày $t$ nhỏ hơn rất nhiều so với cạnh $a$ ($t \ll a$).

</details>

---

### Q9.17

Hai quả cầu giống hệt nhau, A và B, mỗi quả được buộc vào một sợi dây rất nhẹ, và mỗi sợi dây được quấn quanh vành của một ròng rọc khối lượng $M$ gắn trên trục quay không ma sát. Điểm khác biệt duy nhất là ròng rọc dành cho quả cầu A là một đĩa đặc, trong khi ròng rọc dành cho quả cầu B là một đĩa rỗng (vành tròn) giống như phần (e) trong Bảng 9.2. Nếu cả hai quả cầu được thả rơi từ trạng thái nghỉ và rơi cùng một quãng đường, quả cầu nào sẽ có nhiều động năng hơn, hay chúng sẽ có động năng như nhau? Giải thích lập luận của bạn.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Hai quả cầu cùng khối lượng $m$, thả từ nghỉ rơi cùng độ cao $h$.
- Ròng rọc A: Đĩa đặc khối lượng $M$, bán kính $R$.
- Ròng rọc B: Đĩa rỗng (vành mỏng) khối lượng $M$, bán kính $R$.
- Cần so sánh động năng của hai quả cầu $K_A$ và $K_B$ khi chạm đáy.

**Hướng đi:**
- So sánh mômen quán tính của hai ròng rọc $I_A$ và $I_B$.
- Vận dụng định luật bảo toàn cơ năng cho toàn hệ gồm quả cầu và ròng rọc.

**Lời giải chi tiết:**

1. **So sánh mômen quán tính của hai ròng rọc**:
- Ròng rọc A là đĩa đặc: $I_A = \frac{1}{2}MR^2$.
- Ròng rọc B là vành rỗng: $I_B = MR^2$ (toàn bộ khối lượng tập trung ở vành ngoài).
Như vậy $I_B > I_A$, nghĩa là ròng rọc B có mức quán tính quay lớn hơn ròng rọc A.

2. **Áp dụng bảo toàn cơ năng cho từng hệ**:
Ban đầu cả hai hệ đứng yên và ở cùng độ cao $h$, thế năng trọng trường ban đầu của mỗi quả cầu là $U = mgh$.
Khi rơi hết quãng đường $h$, thế năng chuyển hóa thành động năng tịnh tiến của quả cầu và động năng quay của ròng rọc:
$$
mgh = \frac{1}{2}mv^2 + \frac{1}{2}I\omega^2
$$
Vì dây không trượt trên vành ròng rọc bán kính $R$, ta có $\omega = \frac{v}{R}$:
$$
\begin{aligned}
2mgh &= mv^2 + I\left(\frac{v}{R}\right)^2 \\
&= \left(m + \frac{I}{R^2}\right)v^2
\end{aligned}
$$

Suy ra tốc độ của quả cầu khi rơi hết độ cao $h$ là:
$$
v = \sqrt{\frac{2mgh}{m + I/R^2}}
$$

3. **So sánh tốc độ và động năng của quả cầu**:
- Với hệ A: Mẫu số là $m + \frac{1}{2}M$.
- Với hệ B: Mẫu số là $m + M$.
Vì mẫu số của hệ A nhỏ hơn hệ B, quả cầu A rơi nhanh hơn và đạt tốc độ lớn hơn quả cầu B khi chạm đáy: $v_A > v_B$.

Động năng của riêng quả cầu là $K_{\mathrm{qua}} = \frac{1}{2}mv^2$. Do $v_A > v_B$, ta kết luận:
$$
K_A > K_B
$$
**Quả cầu A sẽ có nhiều động năng hơn quả cầu B**.
(Tổng cơ năng của toàn hệ là như nhau và bằng $mgh$, nhưng ở hệ B, ròng rọc rỗng đã lấy đi một phần năng lượng quay lớn hơn, khiến năng lượng còn lại cho quả cầu ít hơn).

</details>

---

### Q9.18

Một ròng rọc phức hợp bao gồm bốn quả cầu giống hệt nhau gắn ở đầu các nan hoa kéo dài từ một trống quay (Hình Q9.18). Một chiếc hộp được nối với một sợi dây nhẹ quấn quanh vành của trống quay. Khi được thả từ trạng thái nghỉ, chiếc hộp đạt được tốc độ $V$ sau khi rơi được một khoảng cách $d$. Bây giờ bốn quả cầu được dịch chuyển vào phía trong sát gần trống hơn, và chiếc hộp lại được thả rơi từ trạng thái nghỉ. Sau khi nó rơi được khoảng cách $d$, tốc độ của nó sẽ bằng $V$, lớn hơn $V$, hay nhỏ hơn $V$? Hãy chứng minh hoặc giải thích vì sao.

![Hình Q9.18: Ròng rọc mang bốn quả cầu gắn ở đầu các nan hoa kéo dài từ trống quay.](./img/young-09/c-hinh-q9-18.png)

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Hộp rơi từ nghỉ khoảng cách $d$ làm quay ròng rọc có 4 quả cầu gắn trên nan hoa, đạt tốc độ $V$.
- Khi dịch chuyển 4 quả cầu vào sát trống hơn và lặp lại thí nghiệm, so sánh tốc độ mới $v$ với $V$.

**Hướng đi:**
- Thiết lập phương trình bảo toàn cơ năng cho hệ hộp và ròng rọc.
- Đánh giá sự thay đổi của mômen quán tính $I$ khi thay đổi khoảng cách từ 4 quả cầu đến trục quay.

**Lời giải chi tiết:**

1. Áp dụng định luật bảo toàn cơ năng cho hệ gồm chiếc hộp khối lượng $m$ và ròng rọc có bán kính vành trống $R$:
$$
mgd = \frac{1}{2}mv^2 + \frac{1}{2}I_{\mathrm{rr}}\omega^2
$$
Do dây không trượt trên vành trống: $\omega = \frac{v}{R}$. Thay vào phương trình năng lượng:
$$
\begin{aligned}
2mgd &= mv^2 + I_{\mathrm{rr}}\left(\frac{v}{R}\right)^2 \\
&= \left(m + \frac{I_{\mathrm{rr}}}{R^2}\right)v^2
\end{aligned}
$$

Rút ra tốc độ của chiếc hộp sau khi rơi quãng đường $d$:
$$
v = \sqrt{\frac{2mgd}{m + I_{\mathrm{rr}}/R^2}}
$$

2. Mômen quán tính của toàn bộ cụm ròng rọc là:
$$
I_{\mathrm{rr}} = I_{\mathrm{trong}} + 4 m_{\mathrm{cau}} r^2
$$
trong đó $r$ là khoảng cách từ tâm mỗi quả cầu đến trục quay.

3. Khi dịch chuyển bốn quả cầu vào phía trong gần trống quay hơn, khoảng cách $r$ giảm đi. Do đó, mômen quán tính $I_{\mathrm{rr}}$ giảm xuống.

4. Nhìn vào biểu thức của vận tốc $v$, khi $I_{\mathrm{rr}}$ giảm, mẫu số $\left(m + \frac{I_{\mathrm{rr}}}{R^2}\right)$ giảm đi trong khi tử số $2mgd$ không đổi.

Do đó, tốc độ của chiếc hộp sẽ **lớn hơn $V$** ($v > V$).
Vật có quán tính quay nhỏ hơn sẽ cản trở chuyển động quay ít hơn, giải phóng nhiều động năng tịnh tiến hơn cho chiếc hộp.

</details>

---

### Q9.19

Bạn có thể sử dụng bất kỳ đơn vị đo góc nào (radian, độ, hoặc số vòng quay) trong một số phương trình của Chương 9, nhưng bạn chỉ có thể sử dụng đơn vị radian trong các phương trình khác. Hãy xác định những phương trình nào bắt buộc phải dùng radian và những phương trình nào không bắt buộc, đồng thời giải thích lý do trong từng trường hợp.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Phân loại các phương trình trong Chương 9 theo yêu cầu về đơn vị góc: Bắt buộc dùng radian so với có thể dùng đơn vị góc bất kỳ (độ, vòng).

**Hướng đi:**
- Kiểm tra nguồn gốc định nghĩa hình học của radian: Tỉ số giữa độ dài cung và bán kính $\theta = s/r$ là đại lượng không thứ nguyên thuần túy.

**Lời giải chi tiết:**

1. **Các phương trình BẮT BUỘC PHẢI DÙNG RADIAN**:
Bao gồm tất cả các phương trình liên hệ giữa **đại lượng góc** và **đại lượng dài** (chuyển động tịnh tiến) hoặc các biểu thức **năng lượng/công**:
- $s = r\theta$: Công thức xuất phát từ chính định nghĩa radian $\theta = s/r$. Nếu dùng độ hay vòng, công thức sẽ xuất hiện thêm các hằng số chuyển đổi nhân tạo ($\pi/180^\circ$ hoặc $2\pi$).
- $v = r\omega$: Đạo hàm của $s = r\theta$. Để vận tốc $v$ có đơn vị hợp chuẩn $\mathrm{m/s}$, $\omega$ phải có đơn vị $\mathrm{rad/s}$ (với $\mathrm{rad} = 1$).
- $a_{\mathrm{tan}} = r\alpha$: Gia tốc tiếp tuyến có đơn vị $\mathrm{m/s^2}$ chỉ khi $\alpha$ tính theo $\mathrm{rad/s^2}$.
- $a_{\mathrm{rad}} = r\omega^2 = \frac{v^2}{r}$: Tương tự, gia tốc hướng tâm đòi hỏi $\omega$ theo $\mathrm{rad/s}$.
- $K = \frac{1}{2}I\omega^2$: Động năng có đơn vị Joule ($\mathrm{kg\cdot m^2/s^2}$) chỉ khi tốc độ góc được tính bằng $\mathrm{rad/s}$.
- $W = \int \tau\,d\theta$ và $P = \tau\omega$: Công cơ học tính bằng Joule bắt buộc góc quay phải là radian.

2. **Các phương trình KHÔNG BẮT BUỘC PHẢI DÙNG RADIAN (có thể dùng độ hoặc vòng)**:
Bao gồm các phương trình **động học thuần góc với gia tốc góc không đổi**:
- $\omega = \omega_0 + \alpha t$
- $\theta = \theta_0 + \omega_0 t + \frac{1}{2}\alpha t^2$
- $\omega^2 = \omega_0^2 + 2\alpha(\theta - \theta_0)$
- $\theta - \theta_0 = \frac{\omega_0 + \omega}{2}t$
- **Lý do**: Các phương trình này là mối quan hệ tỉ lệ tuyến tính thuần túy giữa các đại lượng góc với nhau. Miễn là ta sử dụng một hệ đơn vị góc nhất quán trong toàn bộ phương trình (chẳng hạn: Tất cả đều dùng $\mathrm{rev}$, $\mathrm{rev/s}$, $\mathrm{rev/s^2}$; hoặc tất cả đều dùng độ, độ/s, độ/s$^2$), các hệ số chuyển đổi đơn vị ở hai vế sẽ tự động triệt tiêu.

</details>

---

### Q9.20

Khi tính toán mômen quán tính của một vật thể, chúng ta có thể coi toàn bộ khối lượng của nó như thể tập trung tại khối tâm của vật thể hay không? Hãy chứng minh câu trả lời của bạn.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Đánh giá tính đúng đắn của giả thiết coi toàn bộ khối lượng tập trung tại khối tâm khi tính mômen quán tính $I$.

**Hướng đi:**
- Áp dụng định lý trục song song (định lý Steiner) để so sánh mômen quán tính thực tế với mômen quán tính của một chất điểm đặt tại khối tâm.

**Lời giải chi tiết:**

**TUYỆT ĐỐI KHÔNG THỂ**.

Chứng minh:
1. Giả sử ta có thể coi toàn bộ khối lượng $M$ của vật thể tập trung tại khối tâm $CM$. Khi đó, vật thể biến thành một chất điểm duy nhất có khối lượng $M$ nằm cách trục quay một khoảng $d_{\mathrm{cm}}$.
Mômen quán tính giả định này sẽ là:
$$
I_{\mathrm{gia\,dinh}} = M d_{\mathrm{cm}}^2
$$

2. Tuy nhiên, theo định lý trục song song, mômen quán tính thực tế của vật thể đối với trục quay đó là:
$$
I = I_{\mathrm{cm}} + M d_{\mathrm{cm}}^2
$$
trong đó $I_{\mathrm{cm}} = \int r_{\mathrm{cm}}^2\,dm$ là mômen quán tính của vật đối với trục song song đi qua khối tâm.

3. Đối với bất kỳ vật thể có kích thước hình học mở rộng nào, các phần tử khối lượng luôn phân bố ra xung quanh khối tâm, do đó:
$$
I_{\mathrm{cm}} > 0
$$
Kéo theo mômen quán tính thực tế luôn lớn hơn đáng kể so với mô hình chất điểm:
$$
I = I_{\mathrm{cm}} + M d_{\mathrm{cm}}^2 > M d_{\mathrm{cm}}^2
$$

4. Đặc biệt, khi trục quay đi qua chính khối tâm ($d_{\mathrm{cm}} = 0$):
- Mô hình điểm đặt tại khối tâm sẽ cho kết quả sai lệch $I = M(0)^2 = 0$.
- Trong khi thực tế vật thể quay quanh khối tâm vẫn có mômen quán tính $I_{\mathrm{cm}} > 0$ và cản trở sự quay rất rõ rệt.

Do đó, không bao giờ được coi khối lượng tập trung tại khối tâm khi tính mômen quán tính.

</details>

---

### Q9.21

Một bánh xe đang quay quanh một trục vuông góc với mặt phẳng bánh xe và đi qua tâm bánh xe. Tốc độ góc của bánh xe đang tăng với tốc độ không đổi. Điểm A nằm trên vành ngoài của bánh xe và điểm B nằm ở vị trí trung điểm giữa vành ngoài và tâm bánh xe. Đối với mỗi đại lượng sau đây, độ lớn của nó lớn hơn ở điểm A, lớn hơn ở điểm B, hay bằng nhau ở cả hai điểm?
(a) Tốc độ góc.
(b) Tốc độ tiếp tuyến.
(c) Gia tốc góc.
(d) Gia tốc tiếp tuyến.
(e) Gia tốc hướng tâm.
Hãy giải thích trong từng trường hợp.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Bánh xe quay nhanh dần đều quanh tâm.
- Bán kính: $r_A = R$ (mép ngoài) và $r_B = R/2$ (trung điểm).
- So sánh tại A và B: (a) $\omega$; (b) $v$; (c) $\alpha$; (d) $a_{\mathrm{tan}}$; (e) $a_{\mathrm{rad}}$.

**Hướng đi:**
- Điểm mấu chốt của vật rắn là mọi điểm trên vật đều quay cùng một góc trong cùng một khoảng thời gian.
- Dùng các công thức liên hệ giữa đại lượng góc và dài: $v = r\omega$, $a_{\mathrm{tan}} = r\alpha$, $a_{\mathrm{rad}} = r\omega^2$.

**Lời giải chi tiết:**

Vì điểm B nằm ở trung điểm giữa tâm và mép ngoài, ta có:
$$
r_A = R,
$$

Đồng thời:

$$
r_B = \frac{R}{2}
$$

Từ đó:

$$
r_A = 2r_B
$$

(a) **Tốc độ góc ($\omega$)**: **BẰNG NHAU ở cả hai điểm**.
Vật rắn không bị biến dạng khi quay, do đó trong cùng một khoảng thời gian, mọi điểm trên bánh xe đều quay được những góc bằng nhau. Tốc độ góc $\omega$ là đại lượng đặc trưng chung cho toàn bộ vật rắn: $\omega_A = \omega_B = \omega$.

(b) **Tốc độ tiếp tuyến ($v$)**: **LỚN HƠN Ở ĐIỂM A**.
Tốc độ tiếp tuyến tỉ lệ thuận với bán kính: $v = r\omega$.
Vì $r_A = 2r_B$, ta có $v_A = 2v_B$. Điểm A đi được quãng đường dài gấp đôi điểm B trong cùng một chu kỳ quay.

(c) **Gia tốc góc ($\alpha$)**: **BẰNG NHAU ở cả hai điểm**.
Gia tốc góc là đạo hàm của tốc độ góc: $\alpha = \frac{d\omega}{dt}$. Vì tốc độ góc của mọi điểm luôn bằng nhau tại mọi thời điểm, tốc độ tăng của vận tốc góc cũng đồng nhất trên toàn bộ bánh xe: $\alpha_A = \alpha_B = \alpha$.

(d) **Gia tốc tiếp tuyến ($a_{\mathrm{tan}}$)**: **LỚN HƠN Ở ĐIỂM A**.
Gia tốc tiếp tuyến được tính bởi $a_{\mathrm{tan}} = r\alpha$.
Do $r_A = 2r_B$, ta có $a_{\mathrm{tan}, A} = 2 a_{\mathrm{tan}, B}$. Điểm A có tốc độ dài tăng nhanh gấp đôi điểm B.

(e) **Gia tốc hướng tâm ($a_{\mathrm{rad}}$)**: **LỚN HƠN Ở ĐIỂM A**.
Gia tốc hướng tâm được tính bởi $a_{\mathrm{rad}} = r\omega^2$.
Vì $r_A = 2r_B$ và $\omega$ bằng nhau, ta có $a_{\mathrm{rad}, A} = 2 a_{\mathrm{rad}, B}$. Điểm A phải chịu gia tốc hướng tâm gấp đôi để duy trì quỹ đạo tròn có bán kính lớn gấp đôi.

</details>

---

### Q9.22

Hãy ước lượng mômen quán tính của chính cơ thể bạn đối với trục thẳng đứng đi qua tâm của đỉnh đầu khi bạn đang đứng thẳng với hai cánh tay dang rộng sang hai bên. Hãy đưa ra các giả thiết xấp xỉ hợp lý và đo đạc hoặc ước lượng các đại lượng cần thiết.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Ước lượng momen quán tính của bản thân đối với trục dọc qua đỉnh đầu khi đứng thẳng và dang hai tay. Cần tự đo hoặc chọn rõ các kích thước và khối lượng.

**Hướng đi:**
- Mô hình thân, đầu và chân bằng một trụ đặc dọc theo trục quay.
- Mô hình hai tay bằng thanh mảnh nằm ngang. Khoảng cách phần tử tay tới trục thay đổi, nên dùng tích phân hoặc định lý trục song song.
- Các số dưới đây chỉ minh họa một mô hình ước lượng, không phải số đo của mọi người.

**Lời giải chi tiết:**

Chọn tổng khối lượng $69\,\mathrm{kg}$. Phần thân, đầu và chân có khối lượng $M_t=60\,\mathrm{kg}$ và bán kính hiệu dụng $R_t=0{,}15\,\mathrm m$. Mỗi tay có khối lượng $m_a=4{,}5\,\mathrm{kg}$ và chiều dài $\ell=0{,}70\,\mathrm m$.

Momen của phần trụ:

$$
\begin{aligned}
I_t &= \frac12M_tR_t^2 \\
&= 0{,}675\,\mathrm{kg\,m^2}.
\end{aligned}
$$

Mỗi tay trải từ bán kính $r_0=0{,}15\,\mathrm m$ đến $r_1=0{,}85\,\mathrm m$. Mật độ dài là $\lambda=m_a/\ell$. Momen của một tay:

$$
\begin{aligned}
I_a&=\lambda\int_{r_0}^{r_1}r^2\,dr\\
&=\frac{\lambda}{3}(r_1^3-r_0^3)\\
&\approx1{,}30875\,\mathrm{kg\,m^2}.
\end{aligned}
$$

Vậy tổng momen quán tính:

$$
\begin{aligned}
I&=I_t+2I_a\\
&=3{,}2925\,\mathrm{kg\,m^2}\\
&\approx3{,}3\,\mathrm{kg\,m^2}.
\end{aligned}
$$

Hai tay chỉ chiếm khoảng $13\%$ khối lượng mô hình nhưng đóng góp gần $80\%$ momen quán tính, vì chúng nằm xa trục. Khi khép tay, khoảng cách các phần tử tay đến trục giảm, nên momen quán tính giảm.

Trong cùng mô hình, nếu toàn bộ hai tay nằm trong bán kính $0{,}15\,\mathrm m$, đóng góp của chúng không vượt quá $9(0{,}15)^2=0{,}2025\,\mathrm{kg\,m^2}$. Tổng momen khi ấy không vượt quá $0{,}8775\,\mathrm{kg\,m^2}$ nếu phần thân giữ nguyên.

</details>
