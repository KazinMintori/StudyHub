## 1.8. Thành phần của vector

Mục 1.7 đã trình bày cách cộng vector bằng hình vẽ theo tỷ lệ xích và vận dụng tính chất của tam giác vuông. Tuy nhiên, cách tính bằng tam giác vuông chỉ áp dụng trực tiếp khi hai vector vuông góc với nhau. Để xử lý bài toán tổng quát với các góc bất kỳ và số lượng vector tùy ý, ta cần một phương pháp giải tích tổng quát và thuận tiện hơn: **Phương pháp thành phần**.

Xét hệ tọa độ vuông góc hai chiều (hệ tọa độ Descartes) trong mặt phẳng $xy$ như ở Hình 1.17. Nếu $\vec A$ là một vector độ dời, ta có thể xem nó như tổng của hai độ dời liên tiếp: Một độ dời song song với trục $x$ và một độ dời song song với trục $y$. Hai con số đại số $A_x$ và $A_y$ lần lượt cho biết độ dài đại số của các độ dời dọc theo từng trục tọa độ.

Chẳng hạn: Nếu chiều $+x$ là hướng đông và chiều $+y$ là hướng bắc, vector $\vec A$ trong Hình 1.17 có thể xem là tổng của $2.00\,\mathrm m$ về phía đông và $1.00\,\mathrm m$ về phía bắc. Khi ấy: $A_x = +2.00\,\mathrm m$ và $A_y = +1.00\,\mathrm m$. Cách mô tả này áp dụng cho mọi đại lượng vector, không chỉ riêng độ dời. Hai số $A_x, A_y$ được gọi là **các thành phần** của vector $\vec A$.

::: warning Thành phần của vector không phải là vector
Các thành phần $A_x$ và $A_y$ là các đại lượng đại số vô hướng (mang dấu âm, dương hoặc bằng không), bản thân chúng không phải là vector. Do đó chúng được viết bằng chữ in nghiêng, không in đậm và không đặt mũi tên vector phía trên.
:::

Nếu biết độ lớn $A$ và góc định hướng của vector, ta có thể tính được các thành phần của nó. Trong Hình 1.17, hướng của vector $\vec A$ được xác định bằng góc $\theta$ đo từ trục dương $+x$. Ta tưởng tượng vector ban đầu nằm dọc theo trục $+x$, sau đó quay ngược chiều kim đồng hồ tới hướng thực tế của nó. Góc $\theta$ mang giá trị dương nếu quay từ trục $+x$ về phía trục $+y$ (ngược chiều kim đồng hồ), và mang giá trị âm nếu quay theo chiều ngược lại (cùng chiều kim đồng hồ). Theo quy ước này: Trục $+y$ ứng với góc $90^\circ$, trục $-x$ ứng với góc $180^\circ$, và trục $-y$ ứng với góc $270^\circ$ (hoặc $-90^\circ$).

Theo định nghĩa các hàm số lượng giác trong tam giác vuông:

$$
\begin{aligned}
\frac{A_x}{A} &= \cos\theta, \\
\frac{A_y}{A} &= \sin\theta.
\end{aligned}
$$

Suy ra các thành phần tọa độ của vector, theo công thức (1.5):

$$
\begin{aligned}
A_x &= A\cos\theta, \\
A_y &= A\sin\theta.
\end{aligned}
$$

Ở đây, góc $\theta$ bắt buộc phải được đo từ trục dương $+x$, với chiều quay dương là chiều hướng về trục $+y$.

![Hình 1.17: Phân tích vector thành hai thành phần vuông góc. Biểu diễn vector bằng các thành phần $A_x$ và $A_y$](/vat-ly-1/bai-giang/img/young-01/hinh-1-17.png)

Hai thành phần $A_x, A_y$ chính là hình chiếu vuông góc của vector $\vec A$ lên hai trục tọa độ $x$ và $y$. Trong trường hợp vẽ ở Hình 1.17, cả $A_x$ và $A_y$ đều mang dấu dương, hoàn toàn phù hợp vì góc $\theta$ nằm trong góc phần tư thứ nhất nên cả hàm $\sin\theta$ và $\cos\theta$ đều dương.

Trong Hình 1.18a, $B_x < 0$ và $B_y > 0$. Nếu trục $+x$ là hướng đông và trục $+y$ là hướng bắc, vector $\vec B$ biểu diễn độ dời $2.00\,\mathrm m$ về phía tây và $1.00\,\mathrm m$ về phía bắc, tức $B_x = -2.00\,\mathrm m$ và $B_y = +1.00\,\mathrm m$. Góc định hướng $\theta$ thuộc góc phần tư thứ hai nên có $\cos\theta < 0$ và $\sin\theta > 0$, hoàn toàn nhất quán. Trong Hình 1.18b, cả hai thành phần $C_x$ và $C_y$ đều âm vì góc thuộc góc phần tư thứ ba.

![Hình 1.18: Dấu của các thành phần trong các góc phần tư khác nhau. Dấu của các thành phần vector phụ thuộc vào góc phần tư](/vat-ly-1/bai-giang/img/young-01/hinh-1-18.png)

- **(a) Góc phần tư thứ hai**: Thành phần ngang mang dấu âm ($B_x < 0$), thành phần đứng mang dấu dương ($B_y > 0$).
- **(b) Góc phần tư thứ ba**: Cả hai thành phần ngang và đứng đều mang dấu âm ($C_x < 0, C_y < 0$).

::: warning Chú ý góc tham chiếu khi tính thành phần
Các công thức $A_x = A\cos\theta$ và $A_y = A\sin\theta$ chỉ đúng khi góc $\theta$ được đo từ trục dương $+x$ theo chiều dương về trục $+y$. Nếu đề bài đo góc từ một trục khác (chẳng hạn đo từ trục $+y$ hoặc đo theo chiều kim đồng hồ), người giải bắt buộc phải quy đổi góc về chuẩn hoặc thiết lập lại hệ thức lượng giác tương ứng.
:::

### Ví dụ 1.6: Xác định các thành phần của vector

::: exercise Ví dụ 1.6: Xác định các thành phần của vector
**(a)** Tìm các thành phần $x$ và $y$ của vector độ dời $\vec D$ ở Hình 1.19a, biết độ lớn $D = 3.00\,\mathrm m$ và góc $\alpha = 45^\circ$.

**(b)** Tìm các thành phần $x$ và $y$ của vector độ dời $\vec E$ ở Hình 1.19b, biết độ lớn $E = 4.50\,\mathrm m$ và góc $\beta = 37.0^\circ$.
:::

![Hình 1.19: Xác định góc chuẩn cho các vector. Tính toán thành phần khi góc không đo theo chuẩn](/vat-ly-1/bai-giang/img/young-01/hinh-1-19.png)

- **(a) Góc quay âm**: Góc $\alpha$ đo từ trục $+x$ hướng xuống dưới, ngược chiều chuẩn. Do đó góc chuẩn là $\theta = -\alpha$.
- **(b) Góc đo từ trục tung**: Góc $\beta$ đo từ trục $+y$. Do đó góc chuẩn đo từ trục $+x$ là $\theta = 90.0^\circ - \beta$.

::: solution Lời giải
**Tóm tắt đề bài**:
- Phần (a): $D = 3.00\,\mathrm m$, góc $\alpha = 45^\circ$ nằm dưới trục $+x$.
- Phần (b): $E = 4.50\,\mathrm m$, góc $\beta = 37.0^\circ$ đo theo chiều kim đồng hồ từ trục $+y$.
- Cần tìm: Các thành phần $(D_x, D_y)$ và $(E_x, E_y)$.

**Hướng đi**:
- Quy đổi các góc đã cho về góc chuẩn $\theta$ đo từ trục $+x$ ngược chiều kim đồng hồ.
- Áp dụng công thức thành phần: Thành phần $x$ bằng độ lớn nhân cosin góc chuẩn. Thành phần $y$ bằng độ lớn nhân sin góc chuẩn.

**Lời giải chi tiết**:
Bước 1. Xét vector $\vec D$ ở phần (a):
   Góc $\alpha$ quay từ trục $+x$ xuống trục $-y$ (cùng chiều kim đồng hồ), do đó góc chuẩn mang giá trị âm:

$$
\theta = -\alpha = -45^\circ.
$$

Tính các thành phần:

$$
\begin{aligned}
D_x &= D\cos(-45^\circ) \\
&= (3.00\,\mathrm m)(0.707) \\
&\approx +2.1\,\mathrm m, \\
D_y &= D\sin(-45^\circ) \\
&= (3.00\,\mathrm m)(-0.707) \\
&\approx -2.1\,\mathrm m.
\end{aligned}
$$

Bước 2. Xét vector $\vec E$ ở phần (b):
   Góc $\beta$ đo từ trục $+y$ về phía trục $+x$. Góc chuẩn $\theta$ đo từ trục $+x$ về phía $+y$ là:

$$
\begin{aligned}
\theta &= 90.0^\circ - \beta \\
&= 90.0^\circ - 37.0^\circ \\
&= 53.0^\circ.
\end{aligned}
$$

Tính các thành phần:

$$
\begin{aligned}
E_x &= (4.50\,\mathrm m)\cos 53.0^\circ \\
&\approx +2.71\,\mathrm m, \\
E_y &= (4.50\,\mathrm m)\sin 53.0^\circ \\
&\approx +3.59\,\mathrm m.
\end{aligned}
$$

**Đánh giá**:
Quan sát trực quan trên hình: Vector $\vec D$ hướng chéo xuống phía dưới bên phải nên $D_x>0,D_y<0$. Vector $\vec E$ hướng chếch lên phía trên bên phải nên cả $E_x > 0, E_y > 0$. Dấu và độ lớn phù hợp với hình vẽ. Ở phần (a), góc $45^\circ$ được cho với hai chữ số có nghĩa, nên hai thành phần được ghi thành $\pm2.1\,\mathrm m$. Nếu thế nhầm góc $+45^\circ$, thành phần $D_y$ sẽ sai dấu. Ở phần (b), hai trục tọa độ vẫn vuông góc dù chúng không nằm ngang và thẳng đứng.
:::

### Xác định độ lớn và hướng từ các thành phần

Ta có thể mô tả một vector bằng cặp giá trị độ lớn và hướng $(A, \theta)$, hoặc bằng cặp thành phần tọa độ $(A_x, A_y)$. Hai cách mô tả này hoàn toàn tương đương.

Theo định lý Pythagoras, công thức (1.6) là:

$$
A = \sqrt{A_x^2 + A_y^2}.
$$

Độ lớn $A$ luôn lấy căn bậc hai số học, tức căn không âm. Khi $A_x\ne0$, góc định hướng thỏa mãn hệ thức tang (1.7):

$$
\tan\theta = \frac{A_y}{A_x}.
$$

Đặt góc phụ $\alpha$ bằng giá trị hàm tang ngược do máy tính trả về:

$$
\alpha = \arctan\left(\frac{A_y}{A_x}\right).
$$

Hàm $\arctan$ trả về góc trong khoảng $-90^\circ<\alpha<90^\circ$. Vì hai góc lệch nhau $180^\circ$ có cùng tang, cần chọn $\theta$ theo dấu của cả hai thành phần. Nếu $A_x>0$, có thể lấy $\theta=\alpha$, rồi cộng $360^\circ$ nếu muốn góc trong khoảng từ $0^\circ$ đến dưới $360^\circ$. Nếu $A_x<0$, lấy $\theta=\alpha+180^\circ$.

Khi $A_x=0$, không được chia cho $A_x$. Nếu $A_y>0$, hướng là $90^\circ$. Nếu $A_y<0$, hướng là $270^\circ$ hoặc $-90^\circ$. Nếu cả hai thành phần đều bằng không, ta có vector không và hướng không xác định.

::: warning Phân biệt góc phần tư khi dùng hàm tang
Trong Hình 1.20, $A_x=-2.00\,\mathrm m$ và $A_y=-2.00\,\mathrm m$, nên tỷ số $A_y/A_x=1.00$. Máy tính trả về $\alpha=\arctan(1.00)=45^\circ$. Nhưng cả hai thành phần đều âm, vì vậy vector nằm ở góc phần tư thứ ba. Góc đúng là $\theta=45^\circ+180^\circ=225^\circ$. Hình phác và dấu các thành phần giúp xác định đúng góc phần tư.
:::

![Hình 1.20: Chọn đúng góc phần tư từ dấu của các thành phần. Phân biệt góc $45^\circ$ và $225^\circ$ dựa vào dấu thành phần](/vat-ly-1/bai-giang/img/young-01/hinh-1-20.png)

### Phép nhân vector với số vô hướng theo thành phần

Nếu $\vec D = c\vec A$, mỗi thành phần của vector tích bằng $c$ nhân với thành phần tương ứng. Các hệ thức (1.8) là:

$$
\begin{aligned}
D_x &= cA_x, \\
D_y &= cA_y.
\end{aligned}
$$

Nhân với $c$ làm độ lớn từng thành phần tăng hoặc giảm theo hệ số $|c|$. Với $c>0$, dấu được giữ nguyên. Với $c<0$, dấu của thành phần khác không bị đảo. Với $c=0$, kết quả là vector không. Chẳng hạn, $c=0.5$ làm độ lớn mỗi thành phần giảm một nửa.

### Phép cộng vector bằng phương pháp thành phần

Xét vector tổng $\vec R = \vec A + \vec B$. Quan sát Hình 1.21, thành phần theo trục $x$ của vector tổng bằng tổng các thành phần theo trục $x$ của từng vector. Điều tương tự đúng đối với trục $y$. Các hệ thức (1.9) là:

$$
\begin{aligned}
R_x &= A_x + B_x, \\
R_y &= A_y + B_y.
\end{aligned}
$$

![Hình 1.21: Thành phần của vector tổng bằng tổng các thành phần. Cộng vector bằng phương pháp thành phần](/vat-ly-1/bai-giang/img/young-01/hinh-1-21.png)

Với ba vector, phép cộng được khai triển theo từng trục:

$$
\begin{aligned}
R_x &= A_x+B_x+C_x, \\
R_y &= A_y+B_y+C_y.
\end{aligned}
$$

Tổng quát, nếu cộng $n$ vector $\vec A_1,\vec A_2,\ldots,\vec A_n$, với $n$ là số nguyên dương, mỗi thành phần tổng là tổng các thành phần cùng trục. Để diễn đạt các hệ thức (1.10) bằng ký hiệu tổng hữu hạn, ta viết:

$$
\begin{aligned}
R_x &= A_{1x}+A_{2x}+\cdots+A_{nx} \\
&= \sum_{k=1}^{n} A_{kx}, \\
R_y &= A_{1y}+A_{2y}+\cdots+A_{ny} \\
&= \sum_{k=1}^{n} A_{ky}.
\end{aligned}
$$

Chỉ số $k$ chạy từ $1$ đến $n$, lần lượt chỉ từng vector được cộng. Với $n=2$, ta thu lại các hệ thức cộng hai vector ở trên.

Trong không gian ba chiều với ba trục $x, y, z$ vuông góc từng đôi một, vector có ba thành phần $(A_x,A_y,A_z)$. Công thức (1.11) cho độ lớn:

$$
A = \sqrt{A_x^2 + A_y^2 + A_z^2}.
$$

Thành phần $z$ của vector tổng được tính tương tự:

$$
\begin{aligned}
R_z &= A_{1z}+A_{2z}+\cdots+A_{nz} \\
&= \sum_{k=1}^{n} A_{kz}.
\end{aligned}
$$

![Hình 1.22: Vector trong không gian ba chiều. Vector trong hệ tọa độ ba chiều $xyz$](/vat-ly-1/bai-giang/img/young-01/hinh-1-22.png)

### Chiến lược giải bài toán 1.3: Cộng vector bằng phương pháp thành phần

**Bước 1. Xác định khái niệm**:
Xác định đại lượng mục tiêu cần tìm: Độ lớn của vector tổng, hướng của vector tổng, hay cả hai.

**Bước 2. Thiết lập**:
Vẽ hệ trục tọa độ thích hợp. Đặt đuôi vector thứ nhất ở gốc tọa độ, rồi nối đuôi mỗi vector tiếp theo vào ngọn vector trước. Vẽ vector tổng $\vec R$ từ gốc đầu tiên tới ngọn cuối cùng, rồi ước lượng độ lớn và hướng của nó. Chọn các phương trình cần sử dụng: Tính thành phần, cộng đại số các thành phần, tính độ lớn và xác định góc định hướng.

**Bước 3. Thực hiện**:
1. Tìm các thành phần $x$ và $y$ của từng vector thành phần.
2. Cộng đại số các thành phần cùng trục để tìm $R_x$ và $R_y$ theo các hệ thức (1.10).
3. Tính độ lớn $R=\sqrt{R_x^2+R_y^2}$. Nếu $R_x\ne0$, dùng $\arctan(R_y/R_x)$ để tìm góc phụ, rồi chọn góc phần tư theo dấu của $R_x,R_y$. Nếu $R_x=0$, xét riêng hướng trục tung. Nếu $R=0$, hướng không xác định.

**Bước 4. Đánh giá**:
Kiểm tra độ lớn và hướng của kết quả tính toán có phù hợp với ước lượng ban đầu trên hình vẽ hay không.

### Ví dụ 1.7: Cộng vector bằng phương pháp thành phần

::: exercise Ví dụ 1.7: Cộng vector bằng phương pháp thành phần
Ba người chơi trong một chương trình truyền hình thực tế được đưa tới giữa một cánh đồng rộng lớn, bằng phẳng. Mỗi người được phát một thước dây, la bàn, máy tính cầm tay, xẻng và danh sách ba độ dời sau (thứ tự thực hiện của mỗi người khác nhau):
- $\vec A$: Độ lớn $72.4\,\mathrm m$, lệch $32.0^\circ$ về phía đông so với hướng bắc.
- $\vec B$: Độ lớn $57.3\,\mathrm m$, lệch $36.0^\circ$ về phía nam so với hướng tây.
- $\vec C$: Độ lớn $17.8\,\mathrm m$, thẳng về phía nam.

Ba độ dời này dẫn thẳng tới vị trí chôn chiếc chìa khóa của một chiếc ô tô Porsche phần thưởng. Người chiến thắng đã tính vector tổng trước khi đo từng đoạn mà ngồi tính toán trước vector tổng để đi thẳng một mạch tới đích. Hãy tìm độ dời tổng hợp mà người đó đã tính.
:::

![Hình 1.23: Ba độ dời liên tiếp và vector tổng hợp. Ba độ dời $\vec A, \vec B, \vec C$ và vector tổng $\vec R$](/vat-ly-1/bai-giang/img/young-01/hinh-1-23.png)

::: solution Lời giải
**Tóm tắt đề bài**:
- $\vec A$: $A = 72.4\,\mathrm m$, góc $32.0^\circ$ đông so với bắc.
- $\vec B$: $B = 57.3\,\mathrm m$, góc $36.0^\circ$ nam so với tây.
- $\vec C$: $C = 17.8\,\mathrm m$, hướng chính nam.
- Cần tìm: Độ lớn $R$ và hướng $\theta$ của vector tổng $\vec R = \vec A + \vec B + \vec C$.

**Hướng đi**:
- Chọn hệ trục tọa độ: Chiều $+x$ là hướng đông, chiều $+y$ là hướng bắc.
- Chuyển đổi hướng của ba vector về góc chuẩn $\theta$ đo từ trục $+x$ ngược chiều kim đồng hồ.
- Lập bảng tính các thành phần $x$ và $y$ của từng vector.
- Tính tổng các thành phần $R_x, R_y$ rồi suy ra độ lớn $R$ và góc định hướng $\theta$.

**Lời giải chi tiết**:
Bước 1. Xác định góc chuẩn $\theta$ cho từng vector:

$$
\begin{aligned}
\theta_A &= 90.0^\circ - 32.0^\circ \\
&= 58.0^\circ, \\
\theta_B &= 180.0^\circ + 36.0^\circ \\
&= 216.0^\circ, \\
\theta_C &= 270.0^\circ.
\end{aligned}
$$

Bước 2. Tính thành phần của từng độ dời:
- Đối với vector $\vec A$:

$$
\begin{aligned}
A_x &= (72.4\,\mathrm m)\cos 58.0^\circ \\
&\approx 38.37\,\mathrm m, \\
A_y &= (72.4\,\mathrm m)\sin 58.0^\circ \\
&\approx 61.40\,\mathrm m.
\end{aligned}
$$

- Đối với vector $\vec B$:

$$
\begin{aligned}
B_x &= (57.3\,\mathrm m)\cos 216.0^\circ \\
&\approx -46.36\,\mathrm m, \\
B_y &= (57.3\,\mathrm m)\sin 216.0^\circ \\
&\approx -33.68\,\mathrm m.
\end{aligned}
$$

- Đối với vector $\vec C$:

$$
\begin{aligned}
C_x &= (17.8\,\mathrm m)\cos 270.0^\circ \\
&= 0.00\,\mathrm m, \\
C_y &= (17.8\,\mathrm m)\sin 270.0^\circ \\
&= -17.80\,\mathrm m.
\end{aligned}
$$

Bước 3. Tổng hợp độ lớn, góc chuẩn và các thành phần:

- Vector $\vec A$ có độ lớn $72.4\,\mathrm m$, góc chuẩn $58.0^\circ$, thành phần $x$ bằng $+38.37\,\mathrm m$ và thành phần $y$ bằng $+61.40\,\mathrm m$.
- Vector $\vec B$ có độ lớn $57.3\,\mathrm m$, góc chuẩn $216.0^\circ$, thành phần $x$ bằng $-46.36\,\mathrm m$ và thành phần $y$ bằng $-33.68\,\mathrm m$.
- Vector $\vec C$ có độ lớn $17.8\,\mathrm m$, góc chuẩn $270.0^\circ$, thành phần $x$ bằng $0.00\,\mathrm m$ và thành phần $y$ bằng $-17.80\,\mathrm m$.

Cộng từng nhóm thành phần. Theo trục $x$, thành phần của vector $\vec C$ bằng không. Theo trục $y$, tổng hai thành phần âm bằng $-51.48\,\mathrm m$. Do đó:

$$
\begin{aligned}
R_x&=(38.37-46.36)\,\mathrm m\\
&=-7.99\,\mathrm m,\\
R_y&=A_y+B_y+C_y\\
&=(61.40-51.48)\,\mathrm m\\
&=+9.92\,\mathrm m.
\end{aligned}
$$

Bước 4. Tính độ lớn và hướng của vector tổng hợp:

$$
\begin{aligned}
R &= \sqrt{R_x^2 + R_y^2} \\
&= \sqrt{(-7.99)^2 + (9.92)^2}\,\mathrm m \\
&\approx 12.7\,\mathrm m.
\end{aligned}
$$

Xét tỷ số xác định góc:

$$
\begin{aligned}
\tan\theta &= \frac{R_y}{R_x} \\
&= \frac{9.92\,\mathrm m}{-7.99\,\mathrm m} \\
&\approx -1.242.
\end{aligned}
$$

Máy tính cho $\arctan(-1.242) \approx -51^\circ$. Vì $R_x < 0$ và $R_y > 0$, vector $\vec R$ nằm ở góc phần tư thứ hai. Do đó góc đúng là:

$$
\theta = 180^\circ - 51^\circ = 129^\circ.
$$

Góc này tương đương với hướng lệch $129^\circ - 90^\circ = 39^\circ$ về phía tây so với hướng bắc.

**Đánh giá**:
Đi thẳng một mạch theo độ dời $12.7\,\mathrm m$ theo hướng lệch $39^\circ$ tây so với bắc giúp người thắng cuộc tiết kiệm rất nhiều thời gian so với việc phải đi qua ba chặng với tổng quãng đường $72.4\,\mathrm m + 57.3\,\mathrm m + 17.8\,\mathrm m$ $= 147.5\,\mathrm m$.
:::

### Câu hỏi tự kiểm tra hiểu bài 1.8

::: exercise Câu hỏi tự kiểm tra 1.8: Quan hệ giữa độ lớn và các thành phần vector
Hai vector $\vec A$ và $\vec B$ cùng nằm trong mặt phẳng $xy$:

**(a)** Hai vector có thể có cùng độ lớn nhưng các thành phần khác nhau không?

**(b)** Hai vector có thể có cùng các thành phần tương ứng nhưng độ lớn khác nhau không?
:::

::: solution Lời giải chi tiết
**(a) Có**:
Hai vector có thể có cùng độ lớn nhưng hướng khác nhau trong mặt phẳng (chẳng hạn $\vec A$ hướng theo trục $+x$ có thành phần $(A, 0)$ còn $\vec B$ hướng theo trục $+y$ có thành phần $(0, A)$). Cả hai vector đều có độ lớn bằng $A$ nhưng các thành phần hoàn toàn khác nhau.

**(b) Không**:
Độ lớn của một vector được xác định duy nhất từ các thành phần của nó theo hệ thức:

$$
A = \sqrt{A_x^2 + A_y^2}.
$$

Nếu hai vector $\vec A$ và $\vec B$ có cùng các thành phần tương ứng ($A_x = B_x$ và $A_y = B_y$), thì độ lớn của chúng bắt buộc phải bằng nhau: $A = B$. Hai vector bằng nhau: $\vec A=\vec B$. Nếu chúng khác vector không, hướng của chúng cũng trùng nhau.
:::
