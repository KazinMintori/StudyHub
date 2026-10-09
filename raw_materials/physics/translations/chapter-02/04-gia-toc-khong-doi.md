<!-- Nguồn: mục 2.4, trang in 44–49, trang PDF 64–69; đầy đủ công thức 2.7–2.14, các cách suy ra, Chiến lược 2.1, Ví dụ 2.4–2.5, ứng dụng BIO và hình. -->

## 2.4. Chuyển động với gia tốc không đổi

Trường hợp đơn giản nhất của chuyển động có gia tốc là đi trên đường thẳng với gia tốc không đổi. Vận tốc biến thiên cùng tốc độ trong suốt chuyển động. Ví dụ là vật rơi khi tác dụng không khí không đáng kể. Các ví dụ khác là vật trượt trên mặt nghiêng, trên mặt ngang nhám, hoặc máy bay được phóng từ boong tàu sân bay.

![Hình 2.15 nguyên tác: vị trí, vận tốc và gia tốc của chất điểm ở các thời điểm cách đều](img/young-02/hinh-2-15.png)

**Hình 2.15:** Chất điểm đi theo $+x$ với gia tốc dương không đổi. Các thời điểm $0$, $\Delta t$, $2\Delta t$, $3\Delta t$, $4\Delta t$ có vận tốc tăng những lượng bằng nhau, nhưng vị trí thay đổi những lượng khác nhau vì vận tốc đang đổi.

Hình 2.16 và 2.17 mô tả cùng chuyển động bằng đồ thị. Gia tốc không đổi cho đồ thị $a_x$–$t$ là đường ngang. Vận tốc có độ dốc không đổi nên đồ thị $v_x$–$t$ là đường thẳng.

### Vận tốc theo thời gian

Khi $a_x$ không đổi, gia tốc trung bình trên mọi khoảng bằng chính $a_x$. Thay vào (2.4):

$$a_x=\frac{v_{2x}-v_{1x}}{t_2-t_1}.\tag{2.7}$$

Chọn $t_1=0$, $t_2=t$, gọi vận tốc đầu là $v_{0x}$ và vận tốc sau là $v_x$. Khi ấy $a_x=(v_x-v_{0x})/t$, hay:

$$v_x=v_{0x}+a_xt.\tag{2.8}$$

Tích $a_xt$ là tốc độ biến thiên vận tốc không đổi nhân thời gian, tức toàn bộ độ biến thiên vận tốc từ $0$ đến $t$. Vận tốc sau bằng đầu cộng phần biến thiên.

(2.8) cũng cho biết độ biến thiên vận tốc bằng diện tích dưới đồ thị gia tốc giữa hai thời điểm. Trong Hình 2.16, đó là hình chữ nhật cao $a_x$, rộng $t$, diện tích $a_xt=v_x-v_{0x}$. Mục 2.6 sẽ cho thấy quan hệ diện tích vẫn đúng khi gia tốc biến thiên, dù (2.8) không còn áp dụng.

![Hình 2.16 nguyên tác: gia tốc dương không đổi và diện tích hình chữ nhật dưới đồ thị](img/young-02/hinh-2-16.png)

**Hình 2.16:** Đường gia tốc nằm ngang, độ dốc bằng không. Diện tích từ $0$ tới $t$ bằng $v_x-v_{0x}$.

![Hình 2.17 nguyên tác: đồ thị vận tốc tăng tuyến tính với phần diện tích chữ nhật và tam giác](img/young-02/hinh-2-17.png)

**Hình 2.17:** Vận tốc đầu và gia tốc đều dương. Độ dốc bằng gia tốc; sau thời gian $t$, vận tốc tăng $a_xt$. Tổng diện tích dưới đồ thị bằng độ dời $x-x_0$.

### Vị trí theo thời gian

Ta suy phương trình vị trí bằng hai cách viết vận tốc trung bình trên khoảng $0$ đến $t$. Vị trí đầu là $x_0$, sau là $x$. Theo định nghĩa, dù gia tốc có cố định hay không:

$$v_{\mathrm{av}-x}=\frac{x-x_0}{t}.\tag{2.9}$$

Riêng khi gia tốc không đổi, vận tốc biến thiên tuyến tính. Khi ấy vận tốc trung bình bằng trung bình vận tốc đầu và cuối:

$$v_{\mathrm{av}-x}=\frac12(v_{0x}+v_x).\tag{2.10}$$

Công thức (2.10) không đúng tổng quát nếu gia tốc thay đổi. Thay (2.8) vào:

$$
\begin{aligned}
v_{\mathrm{av}-x}&=\frac12(v_{0x}+v_{0x}+a_xt)\\
&=v_{0x}+\frac12a_xt.
\end{aligned}\tag{2.11}
$$

Đặt (2.9) bằng (2.11), rồi nhân với $t$:

$$v_{0x}+\frac12a_xt=\frac{x-x_0}{t},$$

suy ra:

$$x=x_0+v_{0x}t+\frac12a_xt^2.\tag{2.12}$$

Vị trí bằng tổng ba phần: vị trí đầu; độ dời $v_{0x}t$ nếu vận tốc giữ nguyên giá trị đầu; và độ dời bổ sung $\tfrac12a_xt^2$ do vận tốc biến thiên.

![Hình 2.18 nguyên tác: xe có gia tốc không đổi và đồ thị vị trí dạng parabol](img/young-02/hinh-2-18.png)

**Hình 2.18:** (a) Xe đi theo $x$ với gia tốc không đổi, vận tốc từ $v_{0x}$ lên $v_x=v_{0x}+a_xt$. (b) Đồ thị $x$–$t$ có giao trục đứng tại $x_0$; độ dốc tiếp tuyến lúc đầu là $v_{0x}$, về sau là $v_x$. Trong hình, $x_0$, $v_{0x}$, $a_x$ đều dương, nên đồ thị cong lên. Gia tốc âm cho parabol cong xuống.

Nếu gia tốc bằng không, đồ thị vị trí là đường thẳng. Thêm gia tốc không đổi làm xuất hiện số hạng bậc hai và đường cong parabol. Tương tự, không có gia tốc thì đồ thị vận tốc nằm ngang; gia tốc không đổi làm nó có độ dốc.

![Hình 2.19 nguyên tác: so sánh đồ thị khi không gia tốc với khi gia tốc không đổi](img/young-02/hinh-2-19.png)

**Hình 2.19:** (a) Đường không gia tốc là $x=x_0+v_{0x}t$; phần thêm $\tfrac12a_xt^2$ làm đường thành parabol. (b) Đường không gia tốc là $v_x=v_{0x}$; phần thêm $a_xt$ làm vận tốc tăng tuyến tính.

Một cách khác để suy (2.12) là dùng diện tích dưới đồ thị vận tốc. Độ dời từ $0$ đến $t$ bằng diện tích ấy. Trong Hình 2.17, tách thành hình chữ nhật cao $v_{0x}$, rộng $t$, diện tích $v_{0x}t$; và tam giác vuông cao $a_xt$, rộng $t$, diện tích $\tfrac12(a_xt)t=\tfrac12a_xt^2$. Tổng là $x-x_0=v_{0x}t+\tfrac12a_xt^2$, phù hợp (2.12).

### Ứng dụng BIO — Thử nghiệm con người ở gia tốc lớn

![Chuỗi ảnh nguyên tác: John Stapp trên xe trượt tên lửa trong các giai đoạn tăng tốc và hãm](img/young-02/ung-dung-gia-toc-lon.png)

Trong các thí nghiệm Không quân Hoa Kỳ ở những năm 1940–1950 được sách mô tả, người trên xe trượt tên lửa có thể chịu gia tốc tới $440\,\mathrm{m/s^2}$. Ba ảnh đầu cho thấy bác sĩ Không quân John Stapp tăng từ nghỉ lên $188\,\mathrm{m/s}$, tương đương $678\,\mathrm{km/h}$ hoặc $421\,\mathrm{mi/h}$, chỉ trong $5\,\mathrm s$. Ảnh 4–6 cho thấy giai đoạn hãm tới dừng có độ lớn gia tốc còn cao hơn.

### Quan hệ không chứa thời gian

Để liên hệ vị trí, vận tốc và gia tốc không đổi mà không chứa $t$, giải (2.8) theo thời gian rồi thay vào (2.12). Ở bước chia, xét $a_x\ne0$:

$$t=\frac{v_x-v_{0x}}{a_x},$$

$$x=x_0+v_{0x}\frac{v_x-v_{0x}}{a_x}
+\frac12a_x\left(\frac{v_x-v_{0x}}{a_x}\right)^2.$$

Chuyển $x_0$ sang trái, nhân hai vế với $2a_x$, khai triển:

$$
\begin{aligned}
2a_x(x-x_0)
&=2v_{0x}v_x-2v_{0x}^2\\
&\quad+v_x^2-2v_{0x}v_x+v_{0x}^2\\
&=v_x^2-v_{0x}^2.
\end{aligned}
$$

Cuối cùng:

$$v_x^2=v_{0x}^2+2a_x(x-x_0).\tag{2.13}$$

Một quan hệ khác có được bằng cách đặt (2.9) bằng (2.10) rồi nhân với $t$:

$$x-x_0=\frac12(v_{0x}+v_x)t.\tag{2.14}$$

(2.14) không chứa gia tốc, thuận tiện khi biết gia tốc cố định nhưng chưa biết giá trị. Bốn phương trình (2.8), (2.12), (2.13), (2.14) là các phương trình chuyển động thẳng với gia tốc không đổi, tập hợp ở Bảng 2.5. Với trường hợp các Hình 2.15–2.18, vị trí đầu, vận tốc đầu và gia tốc đều dương. Sách đề nghị vẽ lại khi một, hai hoặc cả ba đại lượng âm.

### Bảng 2.5 — Phương trình chuyển động với gia tốc không đổi

| Phương trình | Số hiệu | Những đại lượng cuối hoặc biến thiên có mặt, ngoài điều kiện đầu |
| --- | --- | --- |
| $v_x=v_{0x}+a_xt$ | (2.8) | $t,v_x,a_x$ |
| $x=x_0+v_{0x}t+\tfrac12a_xt^2$ | (2.12) | $t,x,a_x$ |
| $v_x^2=v_{0x}^2+2a_x(x-x_0)$ | (2.13) | $x,v_x,a_x$ |
| $x-x_0=\tfrac12(v_{0x}+v_x)t$ | (2.14) | $t,x,v_x$ |

### Chiến lược giải bài toán 2.1 — Gia tốc không đổi

**Xác định khái niệm.** Trong nhiều bài chuyển động thẳng, có thể dùng bốn phương trình trên. Nếu gia tốc thay đổi, cần cách khác như mục 2.6.

**Thiết lập.**

1. Đọc kỹ đề và vẽ sơ đồ vị trí ở các thời điểm cần xét. Chọn gốc và chiều dương. Đặt vật ở gốc lúc $t=0$ thường thuận tiện, khi đó $x_0=0$. Chiều dương tọa độ đồng thời xác định chiều dương vận tốc, gia tốc. Nếu $x$ dương về phải thì $v_x$, $a_x$ cũng dương về phải.
2. Nhận diện thời gian, vị trí, vận tốc, gia tốc và đặt ký hiệu $t,x,x_0,v_x,v_{0x},a_x$ hoặc ký hiệu liên quan. Chuyển câu chữ thành đại lượng: “Khi nào vật tới điểm cao nhất?” là tìm $t$ khi $x$ cực đại; “Ở đâu khi tốc độ bằng $25\,\mathrm{m/s}$?” trong Ví dụ 2.4 là tìm $x$ khi $v_x=25\,\mathrm{m/s}$. Chú ý dữ kiện ngầm: xe đang đợi đèn thường có $v_{0x}=0$.
3. Liệt kê các đại lượng, giá trị đã biết, chưa biết và đại lượng cần tìm. Ghi nhận đại lượng nào không có thông tin trong đề.
4. Dùng Bảng 2.5 chọn công thức, thường là công thức không chứa đại lượng bị thiếu. Thường có một phương trình chỉ chứa một ẩn cần tìm; đôi khi cần hai phương trình chứa cùng hai ẩn.
5. Vẽ đồ thị ứng với phương trình: (2.8) là đường thẳng có độ dốc $a_x$; (2.12) là parabol cong lên nếu $a_x>0$, cong xuống nếu $a_x<0$.
6. Từ kinh nghiệm và đồ thị, đưa ra các dự đoán định tính, định lượng có thể về kết quả.

**Thực hiện.** Nếu chỉ cần một phương trình, giải bằng ký hiệu trước rồi thay số. Nếu có hai phương trình hai ẩn, giải đồng thời.

**Đánh giá.** Xem kết quả có hợp lý, nằm trong khoảng giá trị dự đoán không.

### Ví dụ 2.4 — Tính toán với gia tốc không đổi

::: exercise Đề bài trong sách
Người đi mô tô hướng đông qua thị trấn nhỏ, sau khi rời ranh giới thị trấn có gia tốc cố định $4.0\,\mathrm{m/s^2}$, như Hình 2.20. Lúc $t=0$, người ấy cách biển ranh giới $5.0\,\mathrm m$ về đông, đi về đông với $15\,\mathrm{m/s}$.

**(a)** Tìm vị trí và vận tốc ở $t=2.0\,\mathrm s$.

**(b)** Khi tốc độ là $25\,\mathrm{m/s}$, người ấy ở đâu?
:::

![Hình 2.20 nguyên tác: mô tô đi qua biển Osage với vị trí và vận tốc đầu](img/young-02/hinh-2-20.png)

**Hình 2.20:** Gốc ở biển Osage, chiều x là đông. Vị trí đầu $x_0=5.0\,\mathrm m$, vận tốc đầu $15\,\mathrm{m/s}$, gia tốc $4.0\,\mathrm{m/s^2}$. Vị trí, vận tốc tại $2.0\,\mathrm s$ là đại lượng cần tìm.

::: solution Lời giải của sách
**Xác định và thiết lập.** Gia tốc cố định nên dùng các phương trình trên. Chọn biển làm gốc, $+x$ là đông. Dữ kiện là $x_0=5.0\,\mathrm m$, $v_{0x}=15\,\mathrm{m/s}$, $a_x=4.0\,\mathrm{m/s^2}$. Ở (a), tìm $x,v_x$ khi $t=2.0\,\mathrm s$; ở (b), tìm $x$ khi $v_x=25\,\mathrm{m/s}$.

**Thực hiện (a).** Bảng 2.5 cho (2.12) để tính vị trí, (2.8) để tính vận tốc:

$$x=5.0\,\mathrm m+(15\,\mathrm{m/s})(2.0\,\mathrm s)
+\frac12(4.0\,\mathrm{m/s^2})(2.0\,\mathrm s)^2=43\,\mathrm m,$$

$$v_x=15\,\mathrm{m/s}+(4.0\,\mathrm{m/s^2})(2.0\,\mathrm s)
=23\,\mathrm{m/s}.$$

**(b)** Chưa biết thời gian nên chọn (2.13), chứa vị trí, vận tốc, gia tốc nhưng không có $t$. Giải theo $x$:

$$
\begin{aligned}
x&=x_0+\frac{v_x^2-v_{0x}^2}{2a_x}\\
&=5.0\,\mathrm m+
\frac{(25\,\mathrm{m/s})^2-(15\,\mathrm{m/s})^2}{2(4.0\,\mathrm{m/s^2})}
=55\,\mathrm m.
\end{aligned}
$$

**Đánh giá.** Có thể kiểm tra (b) bằng (2.8), tìm thời điểm $v_x=25\,\mathrm{m/s}$ là $t=2.5\,\mathrm s$, rồi thay vào (2.12) để được cùng $x=55\,\mathrm m$. Cách ấy dài hơn; dùng trực tiếp công thức không chứa thời gian hiệu quả hơn.

::: info Đối chiếu một lỗi số trong bản nguồn
Ở đoạn đánh giá Ví dụ 2.4, trang in 48 của bản được cung cấp in thời gian là “$25\,\mathrm s$”. Phép tính từ chính dữ kiện của ví dụ cho $t=(25-15)/4=2.5\,\mathrm s$. Dòng trên dùng kết quả đã đối chiếu và giữ ghi nhận giá trị in ở đây để không sửa nguồn một cách âm thầm.
:::

**Ý chính của ví dụ:** Một hoặc nhiều phương trình Bảng 2.5 giải được chuyển động thẳng với gia tốc không đổi.
:::

### Ví dụ 2.5 — Hai vật có gia tốc khác nhau

Nguyên tác đánh dấu ví dụ này có các bài biến thể trong phần luyện tập.

::: exercise Đề bài trong sách
Người lái xe đi đều $15\,\mathrm{m/s}$, tương đương $54\,\mathrm{km/h}$ hay khoảng $34\,\mathrm{mi/h}$, qua lối sang đường trường học có giới hạn $10\,\mathrm{m/s}$, tương đương $36\,\mathrm{km/h}$ hay khoảng $22\,\mathrm{mi/h}$. Đúng lúc xe qua biển, cảnh sát trên mô tô đang dừng ở đó bắt đầu đuổi theo với gia tốc cố định $3.0\,\mathrm{m/s^2}$, như Hình 2.21a.

**(a)** Bao lâu sau cảnh sát vượt người lái xe? Lúc ấy: **(b)** tốc độ cảnh sát bằng bao nhiêu; **(c)** mỗi xe đã đi bao xa?
:::

![Hình 2.21 nguyên tác: xe đi đều, cảnh sát xuất phát từ nghỉ và hai đồ thị vị trí cắt nhau](img/young-02/hinh-2-21.png)

**Hình 2.21:** (a) Gốc tại biển SCHOOL CROSSING, tức lối sang đường trường học. Xe có vận tốc cố định $15\,\mathrm{m/s}$; cảnh sát ban đầu nghỉ, gia tốc $3.0\,\mathrm{m/s^2}$. (b) Đường vị trí xe thẳng, đường cảnh sát cong lên; chúng cắt nhau khi cùng vị trí. Trục x ghi mét, trục t ghi giây.

::: solution Lời giải của sách
**Xác định và thiết lập.** Cả hai có gia tốc không đổi, xe có gia tốc bằng không. Chọn gốc tại biển, $x_0=0$ cho cả hai, chiều dương sang phải. Vị trí cảnh sát là $x_P$, xe là $x_M$; $v_{P0x}=0$, $v_{M0x}=15\,\mathrm{m/s}$, $a_{Px}=3.0\,\mathrm{m/s^2}$, $a_{Mx}=0$.

Ở (a), cần thời điểm hai vị trí bằng nhau, nên dùng (2.12). Ở (b), dùng (2.8) tìm vận tốc cảnh sát tại thời điểm ấy. Ở (c), dùng (2.12) tìm vị trí.

Hình 2.21b có đường thẳng $x_M=v_{M0x}t$ và nửa parabol $x_P=\tfrac12a_{Px}t^2$. Hình phác hợp lý cho giao điểm khoảng $10\,\mathrm s$ và khoảng cách khoảng $150\,\mathrm m$.

**Thực hiện (a).** Đặt $x_P=x_M$:

$$v_{M0x}t=\frac12a_{Px}t^2.$$

Hai nghiệm:

$$t=0\quad\text{hoặc}\quad
t=\frac{2v_{M0x}}{a_{Px}}
=\frac{2(15\,\mathrm{m/s})}{3.0\,\mathrm{m/s^2}}=10\,\mathrm s.$$

Ở $t=0$, xe vượt cảnh sát. Ở $t=10\,\mathrm s$, cảnh sát vượt xe.

**(b)**

$$v_{Px}=v_{P0x}+a_{Px}t
=0+(3.0\,\mathrm{m/s^2})(10\,\mathrm s)=30\,\mathrm{m/s}.$$

Tốc độ là giá trị tuyệt đối và cũng bằng $30\,\mathrm{m/s}$.

**(c)**

$$x_M=(15\,\mathrm{m/s})(10\,\mathrm s)=150\,\mathrm m,$$

$$x_P=\frac12(3.0\,\mathrm{m/s^2})(10\,\mathrm s)^2=150\,\mathrm m.$$

Hai xe đi cùng quãng đường sau mười giây.

**Đánh giá.** Kết quả phù hợp ước lượng. Khi gặp nhau, vận tốc không bằng nhau: xe đi $15\,\mathrm{m/s}$, cảnh sát đi $30\,\mathrm{m/s}$. Hai đồ thị vị trí cắt nhau nhưng tiếp tuyến có độ dốc khác nhau.

Việc cảnh sát đi nhanh gấp đôi không phải trùng hợp. Theo (2.14), xe đi đều có độ dời $v_{M0x}t$. Cảnh sát xuất phát từ nghỉ nên độ dời $\tfrac12v_{Px}t$. Cùng độ dời trong cùng thời gian cho $v_{M0x}t=\tfrac12v_{Px}t$, tức $v_{Px}=2v_{M0x}$. Quan hệ đúng bất kể giá trị gia tốc cảnh sát trong mô hình này.

**Ý chính của ví dụ:** Hai vật gặp hoặc vượt nhau khi có cùng tọa độ, tức đồ thị vị trí cắt nhau. Vận tốc khi ấy vẫn có thể khác nhau.
:::

### Câu hỏi kiểm tra hiểu mục 2.4

::: exercise Câu hỏi trong sách
Sách cho bốn đồ thị $v_x$–$t$ khả dĩ của hai xe ở Ví dụ 2.5. Đồ thị nào đúng?
:::

![Bốn đồ thị vận tốc a–d của câu hỏi kiểm tra mục 2.4 trong nguyên tác](img/young-02/cau-hoi-2-4.png)

Các đồ thị đều phân biệt Motorist, người lái xe, với Officer, cảnh sát; trục ngang ghi thời gian và mốc $10\,\mathrm s$, trục đứng ghi $v_x$. Chúng khác nhau ở dạng và độ dốc đường cảnh sát, vị trí giao với đường xe.

::: solution Đáp án của sách
Chọn **(b)**. Gia tốc cảnh sát cố định nên đồ thị vận tốc là đường thẳng. Tại lúc hai xe gặp nhau, $t=10\,\mathrm s$, mô tô chạy nhanh hơn ô tô.
:::
