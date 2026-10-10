<!-- Nguồn: mục 1.8, trang in 14–18, trang PDF 34–38; gồm Hình 1.17–1.23, công thức 1.5–1.11, Ví dụ 1.6–1.7, Chiến lược 1.3 và câu hỏi. -->

## 1.8. Thành phần của vector

Mục 1.7 cộng vector bằng hình vẽ theo tỷ lệ và tính chất tam giác vuông. Tuy nhiên, cách tính với tam giác vuông chỉ dùng trực tiếp khi hai vector vuông góc. Ta cần một phương pháp đơn giản nhưng tổng quát hơn, gọi là **phương pháp thành phần**.

Xét hệ tọa độ vuông góc, hay hệ Descartes, ở Hình 1.17. Nếu $\vec A$ là độ dời, ta có thể xem nó là tổng của một độ dời song song trục $x$ và một độ dời song song trục $y$. Hai số $A_x$, $A_y$ lần lượt cho biết độ dời theo mỗi trục.

Chẳng hạn, nếu chiều $+x$ là đông, $+y$ là bắc, vector trong Hình 1.17 có thể là tổng của $2.00\,\mathrm m$ về đông và $1.00\,\mathrm m$ về bắc. Khi ấy $A_x=+2.00\,\mathrm m$, $A_y=+1.00\,\mathrm m$. Cách mô tả này dùng cho mọi vector, không chỉ độ dời. Hai số ấy là **các thành phần** của $\vec A$.

::: warning Thành phần không phải vector
$A_x$ và $A_y$ là các số, không phải chính chúng là vector. Do đó chúng được viết không có mũi tên, để phân biệt với $\vec A$.
:::

Nếu biết độ lớn $A$ và hướng, ta tính được các thành phần. Trong Hình 1.17, hướng được biểu diễn bằng góc $\theta$ đo từ trục $+x$. Tưởng tượng vector ban đầu nằm trên $+x$, rồi quay tới hướng thật. Góc dương nếu quay từ $+x$ về $+y$, và âm nếu quay từ $+x$ về $-y$. Vì thế, $+y$ ứng với $90^\circ$, $-x$ với $180^\circ$, $-y$ với $270^\circ$ hoặc $-90^\circ$.

Theo định nghĩa lượng giác:

$$\frac{A_x}{A}=\cos\theta,\qquad\frac{A_y}{A}=\sin\theta.$$

Suy ra:

$$A_x=A\cos\theta,\qquad A_y=A\sin\theta.\tag{1.5}$$

Ở đây, $\theta$ được đo từ $+x$, chiều quay dương hướng về $+y$.

![Hình 1.17 nguyên tác: Chiếu vector lên hai trục vuông góc](img/young-01/hinh-1-17.png)

**Hình 1.17:** Hai thành phần là hình chiếu của vector lên trục $x$, $y$. Trong trường hợp được vẽ, $A_x$, $A_y$ đều dương, phù hợp vì $\theta$ ở góc phần tư thứ nhất nên cả sin và cos đều dương.

Trong Hình 1.18a, $B_x<0$, $B_y>0$. Nếu $+x$ là đông và $+y$ là bắc, vector có thể biểu diễn $2.00\,\mathrm m$ về tây và $1.00\,\mathrm m$ về bắc, nên $B_x=-2.00\,\mathrm m$, $B_y=+1.00\,\mathrm m$. Góc thuộc phần tư thứ hai có cos âm, sin dương, phù hợp công thức (1.5). Trong Hình 1.18b, cả $C_x$, $C_y$ âm vì cả sin và cos âm ở phần tư thứ ba.

![Hình 1.18 nguyên tác: Dấu của các thành phần trong góc phần tư thứ hai và thứ ba](img/young-01/hinh-1-18.png)

**Hình 1.18:** (a) Thành phần ngang của $\vec B$ âm, thành phần đứng dương. (b) Cả hai thành phần của $\vec C$ âm.

::: warning Góc tham chiếu trong công thức thành phần
Công thức (1.5) chỉ đúng với quy ước góc đo từ $+x$ và chiều quay dương về $+y$. Nếu đề đo góc từ hướng khác hoặc dùng chiều quay khác, phải đổi góc hoặc lập lại quan hệ lượng giác. Ví dụ 1.6 minh họa điều này.
:::

### Ví dụ 1.6 — Tìm các thành phần

::: exercise Đề bài trong sách
**(a)** Tìm thành phần $x$, $y$ của $\vec D$ ở Hình 1.19a, biết $D=3.00\,\mathrm m$ và $\alpha=45^\circ$.

**(b)** Tìm thành phần $x$, $y$ của $\vec E$ ở Hình 1.19b, biết $E=4.50\,\mathrm m$ và $\beta=37.0^\circ$.
:::

![Hình 1.19 nguyên tác: Góc đo theo chiều âm và góc đo từ trục dương y](img/young-01/hinh-1-19.png)

**Hình 1.19:** (a) $\alpha$ đo từ $+x$ theo chiều ngược quy ước của công thức (1.5), nên cần dùng $-\alpha$. $D_x>0$, $D_y<0$. (b) $\beta$ đo từ $+y$, nên cần đổi thành góc $\theta$ đo từ $+x$ về $+y$. Cả $E_x$, $E_y$ dương.

::: solution Lời giải của sách
**Xác định và thiết lập.** Có thể dùng công thức (1.5), nhưng cả $\alpha$ lẫn $\beta$ đều chưa được đo theo quy ước ấy. Từ hình, ước lượng hai độ dài thành phần ở (a) khoảng $2\,\mathrm m$; ở (b), chúng khoảng $3$ và $4\,\mathrm m$. Hình cũng cho biết dấu của từng thành phần.

**Thực hiện (a).** Góc $\alpha$ đo từ $+x$ về $-y$, nên:

$$\theta=-\alpha=-45^\circ.$$

Do đó:

$$
\begin{aligned}
D_x&=D\cos\theta=(3.00\,\mathrm m)\cos(-45^\circ)
\approx+2.1\,\mathrm m,\\
D_y&=D\sin\theta=(3.00\,\mathrm m)\sin(-45^\circ)
\approx-2.1\,\mathrm m.
\end{aligned}
$$

Nếu thay nhầm $+45^\circ$, kết quả $D_y$ sẽ sai dấu.

**Thực hiện (b).** Hai trục vẫn vuông góc, nên không có vấn đề gì dù chúng không nằm ngang và thẳng đứng. Tuy nhiên $\beta$ đo từ $+y$, không thể thay trực tiếp vào (1.5). Góc cần dùng là:

$$\theta=90.0^\circ-\beta=90.0^\circ-37.0^\circ=53.0^\circ.$$

Vì vậy:

$$
\begin{aligned}
E_x&=(4.50\,\mathrm m)\cos53.0^\circ\approx+2.71\,\mathrm m,\\
E_y&=(4.50\,\mathrm m)\sin53.0^\circ\approx+3.59\,\mathrm m.
\end{aligned}
$$

**Đánh giá.** Cả hai phần đều gần kết quả ước lượng. Vì sao kết quả ở phần (a) chỉ giữ hai chữ số có nghĩa là phù hợp?

**Ý chính của ví dụ:** Khi tìm thành phần, luôn dùng hình vector cùng hệ trục để định hướng việc tính toán.
:::

### Tính độ lớn và hướng từ thành phần

Ta có thể mô tả đầy đủ một vector bằng độ lớn và hướng, hoặc bằng các thành phần $x$, $y$. Công thức (1.5) chuyển từ độ lớn, hướng sang thành phần. Ta cũng làm được chiều ngược lại.

Theo định lý Pythagoras ở Hình 1.17:

$$A=\sqrt{A_x^2+A_y^2}.\tag{1.6}$$

Lấy căn không âm. Công thức đúng với bất kỳ cách chọn hai trục vuông góc. Theo định nghĩa tang, với cùng quy ước góc từ $+x$ về $+y$:

$$\tan\theta=\frac{A_y}{A_x},\qquad
\theta=\arctan\frac{A_y}{A_x}.\tag{1.7}$$

Sách dùng $\arctan$ để ký hiệu hàm tang ngược. Ký hiệu $\tan^{-1}$ cũng thường gặp; trên máy tính có thể cần nút INV hoặc 2ND kết hợp TAN.

::: warning Chọn đúng góc phần tư
Hai góc lệch nhau $180^\circ$ có cùng tang. Trong Hình 1.20, $A_x=-2\,\mathrm m$, $A_y=-2\,\mathrm m$, nên tỷ số $A_y/A_x=+1$. Máy tính cho $\arctan1=45^\circ$, nhưng $225^\circ$ cũng có tang bằng $1$. Hình cho thấy vector ở góc phần tư thứ ba, nên góc đúng là $225^\circ$. Luôn vẽ phác để chọn đúng trong hai khả năng.
:::

![Hình 1.20 nguyên tác: Vector có cả hai thành phần âm và góc 225 độ](img/young-01/hinh-1-20.png)

**Hình 1.20:** Tang bằng $+1$ chưa đủ phân biệt $45^\circ$ với $225^\circ$. Dấu hai thành phần và hình vẽ xác định $225^\circ$ là đáp án đúng.

### Nhân vector với số vô hướng theo thành phần

Nếu $\vec D=c\vec A$, mỗi thành phần của tích bằng $c$ nhân thành phần tương ứng:

$$D_x=cA_x,\qquad D_y=cA_y.\tag{1.8}$$

Vì thế, mỗi thành phần của $2\vec A$ gấp đôi thành phần ban đầu: Vector giữ hướng và có độ lớn gấp đôi. Mỗi thành phần của $-3\vec A$ gấp ba về độ lớn nhưng đổi dấu: Vector ngược hướng và có độ lớn gấp ba. Kết quả phù hợp với phép nhân vector ở mục 1.7 và Hình 1.15.

### Cộng vector theo thành phần

Hình 1.21 vẽ $\vec A$, $\vec B$ và tổng $\vec R$. Thành phần $x$ của tổng bằng tổng các thành phần $x$, và tương tự với $y$:

$$R_x=A_x+B_x,\qquad R_y=A_y+B_y.\tag{1.9}$$

![Hình 1.21 nguyên tác: Các thành phần của vector tổng bằng tổng các thành phần tương ứng](img/young-01/hinh-1-21.png)

**Hình 1.21:** $\vec R$ là tổng của $\vec A$ và $\vec B$. $R_x=A_x+B_x$ và $R_y=A_y+B_y$. Hình minh họa trường hợp mọi thành phần đều dương. Bạn có thể vẽ thêm các trường hợp khác để kiểm tra quan hệ vẫn đúng khi thành phần có dấu âm.

Khi biết thành phần hai vector, ta dùng (1.9) để tìm thành phần tổng. Nếu cần độ lớn và hướng của tổng, dùng (1.6), (1.7) với ký hiệu $R$ thay cho $A$.

Phương pháp cũng dùng được cho nhiều vector. Nếu $\vec R$ là tổng của $\vec A$, $\vec B$, $\vec C$, $\vec D$, $\vec E$, … thì:

$$
\begin{aligned}
R_x&=A_x+B_x+C_x+D_x+E_x+\cdots,\\
R_y&=A_y+B_y+C_y+D_y+E_y+\cdots.
\end{aligned}\tag{1.10}
$$

Các vector không nhất thiết nằm trong mặt phẳng $xy$. Thêm trục $z$ vuông góc mặt phẳng ấy, vector tổng quát có ba thành phần $A_x,A_y,A_z$ và độ lớn:

$$A=\sqrt{A_x^2+A_y^2+A_z^2}.\tag{1.11}$$

Ta vẫn lấy căn không âm. Đồng thời, phép cộng có thêm phương trình:

$$R_z=A_z+B_z+C_z+D_z+E_z+\cdots.$$

![Hình 1.22 nguyên tác: Vector và ba thành phần trong hệ tọa độ không gian](img/young-01/hinh-1-22.png)

**Hình 1.22:** Vector trong ba chiều có thành phần theo $x$, $y$, $z$. Độ lớn được tính từ tổng bình phương ba thành phần như (1.11).

### Chiến lược giải bài toán 1.3 — Cộng vector

**Xác định khái niệm.** Xác định đại lượng cần tìm là độ lớn vector tổng, hướng hay cả hai.

**Thiết lập.** Vẽ các vector cùng hệ trục thích hợp. Đặt đuôi vector đầu ở gốc, rồi ghép đuôi từng vector vào đầu vector trước. Dựng $\vec R$ từ gốc tới đầu vector cuối. Dựa vào hình để ước lượng độ lớn và hướng. Chọn các công thức cần dùng: (1.5) tìm thành phần nếu cần, (1.10) cộng thành phần, (1.11) tìm độ lớn, (1.7) tìm hướng.

**Thực hiện.**

1. Tìm thành phần $x$, $y$ của từng vector và ghi vào bảng, như Ví dụ 1.7. Nếu góc $\theta$ đo từ $+x$ về $+y$, dùng $A_x=A\cos\theta$, $A_y=A\sin\theta$. Nếu đề cho góc theo cách khác, đổi sang quy ước này như Ví dụ 1.6.
2. Cộng đại số các thành phần $x$, gồm cả dấu, để được $R_x$. Làm tương tự để được $R_y$.
3. Tính $R=\sqrt{R_x^2+R_y^2}$ và $\theta=\arctan(R_y/R_x)$, đồng thời xét góc phần tư.

**Đánh giá.** Kiểm tra kết quả có phù hợp ước lượng từ hình hay không. Góc máy tính trả về có thể lệch $180^\circ$; hình sẽ cho biết góc đúng, như Ví dụ 1.7.

Phần vừa trình bày tập trung vào độ dời, nhưng phương pháp áp dụng cho mọi đại lượng vector. Ở chương 4, ta sẽ thấy lực cũng tuân theo các quy tắc cộng này.

### Ví dụ 1.7 — Cộng vector bằng thành phần

Nguyên tác đánh dấu ví dụ này có các bài biến thể trong phần luyện tập.

::: exercise Đề bài trong sách
Ba người chơi một chương trình truyền hình thực tế được đưa tới giữa một cánh đồng lớn, bằng phẳng. Mỗi người được phát thước mét, la bàn, máy tính, xẻng và ba độ dời sau, nhưng thứ tự giao cho mỗi người khác nhau:

- $\vec A$: $72.4\,\mathrm m$, lệch $32.0^\circ$ về đông so với bắc.
- $\vec B$: $57.3\,\mathrm m$, lệch $36.0^\circ$ về nam so với tây.
- $\vec C$: $17.8\,\mathrm m$, thẳng về nam.

Ba độ dời dẫn tới nơi chôn chìa khóa một chiếc Porsche mới. Hai người bắt đầu đo ngay; người thắng lại tính trước mình cần đi đâu. Người ấy tính gì?
:::

![Hình 1.23 nguyên tác: Ba độ dời nối tiếp trên hệ trục đông–bắc và vector tổng](img/young-01/hinh-1-23.png)

**Hình 1.23:** Trục $x$ hướng đông, trục $y$ hướng bắc. Các độ dời $\vec A$, $\vec B$, $\vec C$ được ghép nối tiếp; $\vec R=\vec A+\vec B+\vec C$ nối từ điểm đầu đến điểm cuối.

::: solution Lời giải của sách
**Xác định và thiết lập.** Cần tìm tổng ba độ dời, nên dùng phép cộng vector. Chọn $+x$ là đông, $+y$ là bắc. Từ Hình 1.23, ước lượng $\vec R$ dài khoảng $10\,\mathrm m$ và lệch khoảng $40^\circ$ về tây so với bắc, tức $\theta$ khoảng $130^\circ$.

**Thực hiện.** Góc của ba vector, đo từ $+x$ về $+y$, lần lượt là:

$$
\begin{aligned}
\theta_A&=90.0^\circ-32.0^\circ=58.0^\circ,\\
\theta_B&=180.0^\circ+36.0^\circ=216.0^\circ,\\
\theta_C&=270.0^\circ.
\end{aligned}
$$

Ví dụ, thành phần $\vec A$ là:

$$
\begin{aligned}
A_x&=(72.4\,\mathrm m)\cos58.0^\circ\approx38.37\,\mathrm m,\\
A_y&=(72.4\,\mathrm m)\sin58.0^\circ\approx61.40\,\mathrm m.
\end{aligned}
$$

Giữ thêm một chữ số ở các thành phần, rồi làm tròn đáp số cuối. Bảng phép tính của sách:

| Độ lớn | Góc | Thành phần x | Thành phần y |
| --- | --- | --- | --- |
| $A=72.4\,\mathrm m$ | $58.0^\circ$ | $38.37\,\mathrm m$ | $61.40\,\mathrm m$ |
| $B=57.3\,\mathrm m$ | $216.0^\circ$ | $-46.36\,\mathrm m$ | $-33.68\,\mathrm m$ |
| $C=17.8\,\mathrm m$ | $270.0^\circ$ | $0.00\,\mathrm m$ | $-17.80\,\mathrm m$ |
| Tổng | — | $R_x=-7.99\,\mathrm m$ | $R_y=9.92\,\mathrm m$ |

Từ các thành phần:

$$R\approx\sqrt{(-7.99\,\mathrm m)^2+(9.92\,\mathrm m)^2}
\approx12.7\,\mathrm m.$$

Máy tính cho:

$$\arctan\frac{9.92\,\mathrm m}{-7.99\,\mathrm m}\approx-51^\circ.$$

So với hình, góc này lệch $180^\circ$. Giá trị đúng là $180^\circ+(-51^\circ)=129^\circ$, tức lệch $39^\circ$ về tây so với bắc.

**Đánh giá.** Độ lớn và góc phù hợp với ước lượng. Hình vẽ giúp tránh lỗi chọn hướng lệch $180^\circ$.

**Ý chính của ví dụ:** Thành phần $x$ của tổng bằng tổng các thành phần $x$, và tương tự với $y$. Luôn dùng hình để xác định hướng tổng.
:::

### Câu hỏi kiểm tra hiểu mục 1.8

::: exercise Câu hỏi trong sách
Hai vector $\vec A$, $\vec B$ nằm trong mặt phẳng $xy$.

**(a)** Chúng có thể cùng độ lớn nhưng khác thành phần không?

**(b)** Chúng có thể có cùng các thành phần nhưng khác độ lớn không?
:::

::: solution Đáp án của sách
**(a) Có.** Hai vector cùng độ lớn có thể hướng khác nhau, nên có các thành phần khác nhau.

**(b) Không.** Nếu các thành phần tương ứng bằng nhau thì chúng là cùng vector, $\vec A=\vec B$, nên độ lớn cũng bằng nhau.
:::
