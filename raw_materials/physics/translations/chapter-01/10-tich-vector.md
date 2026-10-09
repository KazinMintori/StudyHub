<!-- Nguồn: mục 1.10, trang in 19–24, trang PDF 39–44; gồm công thức 1.16–1.25, đầy đủ khai triển, Hình 1.26–1.33, Ví dụ 1.9–1.11 và câu hỏi. -->

## 1.10. Các phép nhân vector

Phép cộng vector xuất hiện tự nhiên khi kết hợp các độ dời và còn có ích cho nhiều đại lượng vector khác. Nhiều quan hệ vật lý cũng được diễn tả bằng tích của các vector. Tuy nhiên vector không phải số thông thường, nên không thể áp dụng nguyên dạng phép nhân số.

Ta định nghĩa hai phép nhân khác nhau. **Tích vô hướng** cho kết quả là đại lượng vô hướng. **Tích có hướng** cho kết quả là một vector khác.

### Tích vô hướng

Tích vô hướng của $\vec A$, $\vec B$ được ký hiệu $\vec A\cdot\vec B$. Do dấu chấm trong ký hiệu, tiếng Anh còn gọi là *dot product*. Dù hai đầu vào là vector, kết quả là một số vô hướng.

Đặt hai vector chung đuôi như Hình 1.26a. Góc $\varphi$ giữa hai hướng nằm từ $0^\circ$ đến $180^\circ$. Hình 1.26b chiếu $\vec B$ lên hướng $\vec A$, cho thành phần $B\cos\varphi$. Ta có thể lấy thành phần theo bất kỳ hướng thuận tiện nào, không chỉ các trục tọa độ. Tích vô hướng được định nghĩa bằng độ lớn $A$ nhân thành phần của $\vec B$ theo hướng $\vec A$:

$$
\vec A\cdot\vec B=AB\cos\varphi
=|\vec A|\,|\vec B|\cos\varphi.
\tag{1.16}
$$

Tương tự, có thể lấy $B$ nhân thành phần $A\cos\varphi$ của $\vec A$ theo hướng $\vec B$, như Hình 1.26c. Kết quả $B(A\cos\varphi)=AB\cos\varphi$ vẫn như (1.16).

![Hình 1.26 nguyên tác: tích vô hướng được tính từ độ lớn một vector và thành phần vector còn lại theo hướng ấy](img/young-01/hinh-1-26.png)

**Hình 1.26:** (a) Đặt chung đuôi. (b) $\vec A\cdot\vec B=A(B\cos\varphi)$. (c) Cũng có thể tính $\vec A\cdot\vec B=B(A\cos\varphi)$.

Tích vô hướng có thể dương, âm hoặc bằng không. Nếu $0^\circ\le\varphi<90^\circ$, cos dương nên tích dương. Nếu $90^\circ<\varphi\le180^\circ$, thành phần $B\cos\varphi$ âm nên tích âm. Nếu hai vector vuông góc, $\varphi=90^\circ$ và tích bằng không.

![Hình 1.27 nguyên tác: tích vô hướng dương, âm hoặc bằng không theo góc giữa hai vector](img/young-01/hinh-1-27.png)

**Hình 1.27:** (a) Góc nhọn cho $B\cos\varphi>0$, tích dương. (b) Góc tù cho $B\cos\varphi<0$, tích âm. (c) Góc vuông cho thành phần theo hướng vector kia bằng không, nên tích bằng không.

Vì $AB\cos\varphi=BA\cos\varphi$, ta có $\vec A\cdot\vec B=\vec B\cdot\vec A$. Tích vô hướng có tính giao hoán. Sách dùng tích này ở chương 6 để mô tả công của lực, rồi ở các chương sau để tính điện thế và ảnh hưởng của từ trường biến thiên lên mạch điện.

### Tính tích vô hướng bằng các thành phần

Trước hết xét các vector đơn vị trực chuẩn $\hat{\mathbf i}$, $\hat{\mathbf j}$, $\hat{\mathbf k}$. Chúng đều có độ lớn $1$ và vuông góc từng đôi. Theo (1.16):

$$
\begin{aligned}
\hat{\mathbf i}\cdot\hat{\mathbf i}
=\hat{\mathbf j}\cdot\hat{\mathbf j}
=\hat{\mathbf k}\cdot\hat{\mathbf k}
&=(1)(1)\cos0^\circ=1,\\
\hat{\mathbf i}\cdot\hat{\mathbf j}
=\hat{\mathbf i}\cdot\hat{\mathbf k}
=\hat{\mathbf j}\cdot\hat{\mathbf k}
&=(1)(1)\cos90^\circ=0.
\end{aligned}\tag{1.17}
$$

Biểu diễn hai vector bằng thành phần rồi khai triển đầy đủ:

$$
\begin{aligned}
\vec A\cdot\vec B
&=(A_x\hat{\mathbf i}+A_y\hat{\mathbf j}+A_z\hat{\mathbf k})\\
&\quad\cdot(B_x\hat{\mathbf i}+B_y\hat{\mathbf j}+B_z\hat{\mathbf k})\\
&=A_x\hat{\mathbf i}\cdot B_x\hat{\mathbf i}
 +A_x\hat{\mathbf i}\cdot B_y\hat{\mathbf j}
 +A_x\hat{\mathbf i}\cdot B_z\hat{\mathbf k}\\
&\quad+A_y\hat{\mathbf j}\cdot B_x\hat{\mathbf i}
 +A_y\hat{\mathbf j}\cdot B_y\hat{\mathbf j}
 +A_y\hat{\mathbf j}\cdot B_z\hat{\mathbf k}\\
&\quad+A_z\hat{\mathbf k}\cdot B_x\hat{\mathbf i}
 +A_z\hat{\mathbf k}\cdot B_y\hat{\mathbf j}
 +A_z\hat{\mathbf k}\cdot B_z\hat{\mathbf k}\\
&=A_xB_x(\hat{\mathbf i}\cdot\hat{\mathbf i})
 +A_xB_y(\hat{\mathbf i}\cdot\hat{\mathbf j})
 +A_xB_z(\hat{\mathbf i}\cdot\hat{\mathbf k})\\
&\quad+A_yB_x(\hat{\mathbf j}\cdot\hat{\mathbf i})
 +A_yB_y(\hat{\mathbf j}\cdot\hat{\mathbf j})
 +A_yB_z(\hat{\mathbf j}\cdot\hat{\mathbf k})\\
&\quad+A_zB_x(\hat{\mathbf k}\cdot\hat{\mathbf i})
 +A_zB_y(\hat{\mathbf k}\cdot\hat{\mathbf j})
 +A_zB_z(\hat{\mathbf k}\cdot\hat{\mathbf k}).
\end{aligned}\tag{1.18}
$$

Theo (1.17), sáu trong chín số hạng bằng không. Ba số hạng còn lại cho:

$$\vec A\cdot\vec B=A_xB_x+A_yB_y+A_zB_z.\tag{1.19}$$

Như vậy tích vô hướng bằng tổng tích các thành phần tương ứng. Khi biết thành phần hai vector, ta có thể dùng (1.19) rồi kết hợp (1.16) để tìm góc giữa chúng, như Ví dụ 1.10.

### Ví dụ 1.9 — Tính tích vô hướng

Nguyên tác đánh dấu ví dụ này có các bài biến thể trong phần luyện tập.

::: exercise Đề bài trong sách
Tìm $\vec A\cdot\vec B$ của hai vector ở Hình 1.28, biết $A=4.00$, $B=5.00$. Góc của chúng so với chiều $+x$ lần lượt là $53.0^\circ$ và $130.0^\circ$.
:::

![Hình 1.28 nguyên tác: hai vector trong mặt phẳng tạo góc 53 độ và 130 độ với trục x](img/young-01/hinh-1-28.png)

**Hình 1.28:** Hai vector nằm trong mặt phẳng $xy$; góc giữa chúng là phần chênh giữa hai góc với $+x$.

::: solution Lời giải của sách
**Xác định và thiết lập.** Tính theo hai cách: dùng độ lớn và góc ở (1.16), rồi dùng thành phần ở (1.19). Hai kết quả dùng để kiểm tra lẫn nhau.

**Thực hiện.** Góc giữa hai vector:

$$\varphi=130.0^\circ-53.0^\circ=77.0^\circ.$$

Theo (1.16):

$$\vec A\cdot\vec B=(4.00)(5.00)\cos77.0^\circ\approx4.50.$$

Để dùng (1.19), tính các thành phần theo đúng góc tham chiếu:

$$
\begin{aligned}
A_x&=(4.00)\cos53.0^\circ\approx2.407,\\
A_y&=(4.00)\sin53.0^\circ\approx3.195,\\
B_x&=(5.00)\cos130.0^\circ\approx-3.214,\\
B_y&=(5.00)\sin130.0^\circ\approx3.830.
\end{aligned}
$$

Giữ thêm một chữ số ở thành phần và làm tròn ở cuối, như Ví dụ 1.7:

$$
\begin{aligned}
\vec A\cdot\vec B
&=A_xB_x+A_yB_y+A_zB_z\\
&\approx(2.407)(-3.214)+(3.195)(3.830)+(0)(0)\\
&\approx4.50.
\end{aligned}
$$

**Đánh giá.** Hai phương pháp cho cùng kết quả.

**Ý chính của ví dụ:** Tích vô hướng là một số bằng tổng các tích thành phần $x$, $y$, $z$ tương ứng.
:::

### Ví dụ 1.10 — Tìm góc bằng tích vô hướng

Nguyên tác đánh dấu ví dụ này có các bài biến thể trong phần luyện tập.

::: exercise Đề bài trong sách
Tìm góc giữa:

$$\vec A=2.00\hat{\mathbf i}+3.00\hat{\mathbf j}+1.00\hat{\mathbf k}$$

và:

$$\vec B=-4.00\hat{\mathbf i}+2.00\hat{\mathbf j}-1.00\hat{\mathbf k}.$$
:::

![Hình 1.29 nguyên tác: hai vector không gian biểu diễn bằng các cạnh của hai khối hộp](img/young-01/hinh-1-29.png)

**Hình 1.29:** $\vec A$ nối gốc tới đỉnh gần của khối hộp đỏ; $\vec B$ nối gốc tới đỉnh xa của khối hộp xanh.

::: solution Lời giải của sách
**Xác định và thiết lập.** Đã biết ba thành phần của mỗi vector, cần tìm góc $\varphi$. Giải (1.16) theo cos của góc, dùng (1.19) tính tích vô hướng và công thức độ lớn để tính $A$, $B$.

**Thực hiện.**

$$\cos\varphi=\frac{\vec A\cdot\vec B}{AB}
=\frac{A_xB_x+A_yB_y+A_zB_z}{AB}.$$

Trong trường hợp này:

$$
\begin{aligned}
\vec A\cdot\vec B
&=(2.00)(-4.00)+(3.00)(2.00)+(1.00)(-1.00)\\
&=-3.00,\\
A&=\sqrt{(2.00)^2+(3.00)^2+(1.00)^2}=\sqrt{14.00},\\
B&=\sqrt{(-4.00)^2+(2.00)^2+(-1.00)^2}=\sqrt{21.00}.
\end{aligned}
$$

Do đó:

$$\cos\varphi=\frac{-3.00}{\sqrt{14.00}\sqrt{21.00}}\approx-0.175,$$

và $\varphi\approx100^\circ$.

**Đánh giá.** Tích vô hướng âm đòi hỏi góc nằm giữa $90^\circ$ và $180^\circ$, phù hợp kết quả.

**Ý chính của ví dụ:** Khi biết thành phần, tìm góc bằng cách tính tích vô hướng rồi dùng quan hệ $\vec A\cdot\vec B=AB\cos\varphi$.
:::

### Tích có hướng

Tích có hướng, tiếng Anh *cross product*, được ký hiệu $\vec A\times\vec B$ và có kết quả là vector. Sách dùng nó trong chương 10 cho mômen lực và mômen động lượng, rồi ở chương 27–28 cho từ trường và lực từ.

Đặt $\vec A$, $\vec B$ chung đuôi như Hình 1.30a. Hai vector nằm trong một mặt phẳng. Tích có hướng là vector vuông góc mặt phẳng ấy, tức vuông góc cả hai vector, với độ lớn $AB\sin\varphi$. Nếu $\vec C=\vec A\times\vec B$ thì:

$$C=AB\sin\varphi.\tag{1.20}$$

Góc $\varphi$ được đo từ $\vec A$ tới $\vec B$, lấy góc nhỏ hơn trong hai góc có thể, nên nằm từ $0^\circ$ đến $180^\circ$. Vì sin không âm trên khoảng này, $C$ không âm, đúng tính chất của độ lớn.

Nếu hai vector cùng hướng hoặc ngược hướng thì $\varphi=0^\circ$ hoặc $180^\circ$ và tích có hướng bằng vector không. Đặc biệt, tích có hướng của một vector với chính nó bằng không.

::: warning Phân biệt hai phép tích
$AB\sin\varphi$ là **độ lớn của tích có hướng**, còn $AB\cos\varphi$ là **tích vô hướng**. Giữ cố định hai độ lớn rồi thay đổi góc: khi cùng hướng, tích có hướng bằng không còn tích vô hướng đạt giá trị lớn nhất; khi vuông góc, độ lớn tích có hướng đạt lớn nhất còn tích vô hướng bằng không.
:::

Một mặt phẳng có hai hướng pháp tuyến đối nhau. Để chọn hướng của $\vec A\times\vec B$, tưởng tượng quay $\vec A$ tới $\vec B$ theo góc nhỏ hơn. Khum các ngón bàn tay phải theo chiều quay ấy; ngón cái duỗi ra chỉ hướng tích có hướng.

![Hình 1.30 nguyên tác: quy tắc bàn tay phải khi đổi thứ tự hai vector](img/young-01/hinh-1-30.png)

**Hình 1.30a:** (1) Đặt chung đuôi. (2) Hướng các ngón bàn tay phải theo $\vec A$, lòng bàn tay hướng về phía $\vec B$. (3) Khum ngón tay từ $\vec A$ tới $\vec B$. (4) Ngón cái chỉ $\vec A\times\vec B$.

**Hình 1.30b:** Đổi thứ tự, hướng ngón tay theo $\vec B$ rồi khum về $\vec A$. Ngón cái chỉ $\vec B\times\vec A$, cùng độ lớn nhưng ngược hướng kết quả trước. Do đó tích có hướng không giao hoán mà **phản giao hoán**:

$$\vec A\times\vec B=-\vec B\times\vec A.\tag{1.21}$$

Tương tự tích vô hướng, có thể diễn giải độ lớn bằng hình học. $B\sin\varphi$ là thành phần của $\vec B$ vuông góc hướng $\vec A$, nên độ lớn tích có hướng bằng $A$ nhân thành phần đó. Cũng có thể lấy $B$ nhân thành phần $A\sin\varphi$ của $\vec A$ vuông góc $\vec B$.

![Hình 1.31 nguyên tác: độ lớn tích có hướng qua thành phần vuông góc](img/young-01/hinh-1-31.png)

**Hình 1.31:** (a) $|\vec A\times\vec B|=A(B\sin\varphi)$. (b) Cũng bằng $B(A\sin\varphi)$. Hình vẽ góc từ $0^\circ$ đến $90^\circ$; hãy dựng hình tương tự cho góc từ $90^\circ$ đến $180^\circ$ để thấy cách diễn giải vẫn đúng.

### Tính tích có hướng bằng thành phần

Trước hết lập bảng tích các vector đơn vị vuông góc trong Hình 1.32a. Tích một vector với chính nó bằng không:

$$\hat{\mathbf i}\times\hat{\mathbf i}
=\hat{\mathbf j}\times\hat{\mathbf j}
=\hat{\mathbf k}\times\hat{\mathbf k}=\vec0.$$

$\vec0$ là vector có mọi thành phần bằng không và không có hướng xác định. Theo (1.20), (1.21) và bàn tay phải:

$$
\begin{aligned}
\hat{\mathbf i}\times\hat{\mathbf j}
&=-\hat{\mathbf j}\times\hat{\mathbf i}=\hat{\mathbf k},\\
\hat{\mathbf j}\times\hat{\mathbf k}
&=-\hat{\mathbf k}\times\hat{\mathbf j}=\hat{\mathbf i},\\
\hat{\mathbf k}\times\hat{\mathbf i}
&=-\hat{\mathbf i}\times\hat{\mathbf k}=\hat{\mathbf j}.
\end{aligned}\tag{1.22}
$$

Có thể kiểm tra từng quan hệ bằng Hình 1.32a. Biểu diễn hai vector theo thành phần và khai triển:

$$
\begin{aligned}
\vec A\times\vec B
&=(A_x\hat{\mathbf i}+A_y\hat{\mathbf j}+A_z\hat{\mathbf k})\\
&\quad\times(B_x\hat{\mathbf i}+B_y\hat{\mathbf j}+B_z\hat{\mathbf k})\\
&=A_x\hat{\mathbf i}\times B_x\hat{\mathbf i}
 +A_x\hat{\mathbf i}\times B_y\hat{\mathbf j}
 +A_x\hat{\mathbf i}\times B_z\hat{\mathbf k}\\
&\quad+A_y\hat{\mathbf j}\times B_x\hat{\mathbf i}
 +A_y\hat{\mathbf j}\times B_y\hat{\mathbf j}
 +A_y\hat{\mathbf j}\times B_z\hat{\mathbf k}\\
&\quad+A_z\hat{\mathbf k}\times B_x\hat{\mathbf i}
 +A_z\hat{\mathbf k}\times B_y\hat{\mathbf j}
 +A_z\hat{\mathbf k}\times B_z\hat{\mathbf k}.
\end{aligned}\tag{1.23}
$$

Mỗi số hạng có thể viết lại, chẳng hạn $A_x\hat{\mathbf i}\times B_y\hat{\mathbf j}=(A_xB_y)(\hat{\mathbf i}\times\hat{\mathbf j})$. Dùng bảng (1.22) rồi nhóm các số hạng cùng vector đơn vị:

$$
\begin{aligned}
\vec A\times\vec B
&=(A_yB_z-A_zB_y)\hat{\mathbf i}\\
&\quad+(A_zB_x-A_xB_z)\hat{\mathbf j}\\
&\quad+(A_xB_y-A_yB_x)\hat{\mathbf k}.
\end{aligned}\tag{1.24}
$$

So với cách viết vector ở (1.14), các thành phần của $\vec C=\vec A\times\vec B$ là:

$$
\begin{aligned}
C_x&=A_yB_z-A_zB_y,\\
C_y&=A_zB_x-A_xB_z,\\
C_z&=A_xB_y-A_yB_x.
\end{aligned}\tag{1.25}
$$

### Hệ tọa độ thuận và nghịch

Nếu đảo chiều trục $z$ của Hình 1.32a, ta được hệ ở Hình 1.32b. Khi ấy, định nghĩa tích có hướng cho $\hat{\mathbf i}\times\hat{\mathbf j}=-\hat{\mathbf k}$ thay vì $+\hat{\mathbf k}$. Mọi tích vector đơn vị đều đổi dấu so với (1.22).

Như vậy có hai loại hệ tọa độ, khác nhau ở dấu các tích vector đơn vị. Hệ thỏa $\hat{\mathbf i}\times\hat{\mathbf j}=\hat{\mathbf k}$ gọi là **hệ tọa độ thuận**, hay hệ bàn tay phải. Sách tuân theo cách dùng thông thường là chỉ dùng hệ này.

![Hình 1.32 nguyên tác: hệ tọa độ bàn tay phải và hệ bàn tay trái](img/young-01/hinh-1-32.png)

**Hình 1.32:** (a) Hệ thuận dùng trong sách, có các tích tuần hoàn ở (1.22). (b) Hệ nghịch, hay bàn tay trái, có dấu ngược lại và không được dùng trong các công thức thành phần đang xét.

### Ví dụ 1.11 — Tính tích có hướng

::: exercise Đề bài trong sách
$\vec A$ có độ lớn $6$ đơn vị, theo chiều $+x$. $\vec B$ có độ lớn $4$ đơn vị, nằm trong mặt phẳng $xy$ và tạo góc $30^\circ$ với $+x$, theo Hình 1.33. Tìm $\vec C=\vec A\times\vec B$.
:::

![Hình 1.33 nguyên tác: tích có hướng của hai vector trong mặt phẳng xy chỉ theo trục z](img/young-01/hinh-1-33.png)

**Hình 1.33:** $\vec B$ nằm trong mặt phẳng $xy$, lệch $30^\circ$ từ $+x$ về $+y$; $\vec C$ vuông góc mặt phẳng ấy.

::: solution Lời giải của sách
**Xác định và thiết lập.** Tính bằng hai cách để kiểm tra: dùng (1.20) kết hợp bàn tay phải, rồi dùng các thành phần ở (1.25).

**Thực hiện.** Độ lớn tích:

$$AB\sin\varphi=(6)(4)\sin30^\circ=12.$$

Bàn tay phải cho hướng $+z$, nên $\vec C=12\hat{\mathbf k}$ theo đơn vị tích tương ứng.

Theo cách thành phần, vì $\vec A$ theo $x$, chỉ $A_x$ khác không. Góc $\vec B$ đo đúng quy ước, nên:

$$
\begin{aligned}
A_x&=6,&A_y&=0,&A_z&=0,\\
B_x&=4\cos30^\circ=2\sqrt3,&B_y&=4\sin30^\circ=2,&B_z&=0.
\end{aligned}
$$

Thay vào (1.25):

$$
\begin{aligned}
C_x&=(0)(0)-(0)(2)=0,\\
C_y&=(0)(2\sqrt3)-(6)(0)=0,\\
C_z&=(6)(2)-(0)(2\sqrt3)=12.
\end{aligned}
$$

Vậy một lần nữa $\vec C=12\hat{\mathbf k}$.

**Đánh giá.** Hai phương pháp cho cùng kết quả. Tùy dữ kiện và tình huống, một cách có thể thuận tiện hơn cách kia.

**Ý chính của ví dụ:** Tích có hướng là vector thứ ba vuông góc cả hai vector ban đầu. Có thể tìm nó từ độ lớn, góc và bàn tay phải, hoặc từ các thành phần.
:::

### Câu hỏi kiểm tra hiểu mục 1.10

::: exercise Câu hỏi trong sách
$\vec A$ có độ lớn $2$, $\vec B$ có độ lớn $3$. Góc $\varphi$ thuộc các khả năng: (i) $0^\circ$, (ii) $90^\circ$, (iii) $180^\circ$. Xác định góc có thể cho từng trường hợp; có thể có nhiều đáp án:

**(a)** $\vec A\cdot\vec B=0$.

**(b)** $\vec A\times\vec B=\vec0$.

**(c)** $\vec A\cdot\vec B=6$.

**(d)** $\vec A\cdot\vec B=-6$.

**(e)** $|\vec A\times\vec B|=6$.
:::

::: solution Đáp án của sách
**(a)** Chọn (ii), $90^\circ$. Với hai độ lớn khác không đã cho, tích vô hướng bằng không chỉ khi hai vector vuông góc.

**(b)** Chọn (i) hoặc (iii), $0^\circ$ hoặc $180^\circ$. Tích có hướng bằng không khi cùng hoặc ngược hướng.

**(c)** Chọn (i), $0^\circ$. Tích vô hướng bằng $AB$ chỉ khi cùng hướng.

**(d)** Chọn (iii), $180^\circ$. Tích vô hướng bằng $-AB$ chỉ khi ngược hướng.

**(e)** Chọn (ii), $90^\circ$. Độ lớn tích có hướng bằng $AB$ chỉ khi hai vector vuông góc.
:::
