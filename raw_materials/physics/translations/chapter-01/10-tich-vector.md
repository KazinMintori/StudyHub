## 1.10. Các phép nhân vector

Phép cộng vector xuất hiện tự nhiên khi ta kết hợp các độ dời, và nó còn có vai trò nền tảng cho nhiều đại lượng vector khác trong cơ học. Bên cạnh phép cộng, nhiều quy luật vật lý quan trọng được diễn đạt thông qua tích của các vector. Tuy nhiên, vì vector vừa có độ lớn vừa có hướng trong không gian, ta không thể áp dụng nguyên dạng phép nhân số thông thường cho hai vector.

Trong toán học và vật lý, ta định nghĩa hai phép nhân vector khác nhau:
1. **Tích vô hướng** (scalar product hay dot product): Cho kết quả là một đại lượng vô hướng.
2. **Tích có hướng** (vector product hay cross product): Cho kết quả là một vector mới.

### Tích vô hướng

Tích vô hướng của hai vector $\vec A$ và $\vec B$ được ký hiệu là $\vec A\cdot\vec B$ (do có dấu chấm nên tiếng Anh thường gọi là *dot product*). Mặc dù hai thừa số đầu vào là các vector, kết quả của phép nhân này luôn là một đại lượng vô hướng.

Với hai vector khác không, ta định nghĩa tích vô hướng bằng cách đặt $\vec A$ và $\vec B$ có chung điểm gốc như minh họa ở Hình 1.26a. Góc $\varphi$ hợp bởi hướng của hai vector nằm trong giới hạn từ $0^\circ$ đến $180^\circ$. Hình 1.26b biểu diễn phép chiếu vuông góc của vector $\vec B$ lên phương của vector $\vec A$, cho thành phần hình chiếu có độ dài đại số là $B\cos\varphi$. Tích vô hướng bằng độ lớn vector thứ nhất nhân với thành phần vector thứ hai theo phương ấy. Định nghĩa (1.16) là:

$$
\begin{aligned}
\vec A\cdot\vec B &= AB\cos\varphi \\
&= \|\vec A\|\,\|\vec B\|\cos\varphi.
\end{aligned}
$$

Hoàn toàn tương đương, ta cũng có thể lấy độ lớn $B$ nhân với hình chiếu $A\cos\varphi$ của vector $\vec A$ lên phương của vector $\vec B$ như ở Hình 1.26c: $B(A\cos\varphi) = AB\cos\varphi$.

![Hình 1.26: Ý nghĩa hình học của tích vô hướng. Tích vô hướng qua độ lớn và hình chiếu](/vat-ly-1/bai-giang/img/young-01/hinh-1-26.png)

- **(a) Đặt chung gốc**: Hai vector $\vec A$ và $\vec B$ tạo với nhau góc $\varphi$ ($0^\circ \le \varphi \le 180^\circ$).
- **(b) Chiếu $\vec B$ lên $\vec A$**: $\vec A\cdot\vec B = A(B\cos\varphi)$.
- **(c) Chiếu $\vec A$ lên $\vec B$**: $\vec A\cdot\vec B = B(A\cos\varphi)$.

Nếu một trong hai vector bằng không, tích vô hướng bằng không. Với hai vector khác không, tích vô hướng có thể nhận giá trị dương, âm hoặc bằng không tùy thuộc vào góc $\varphi$:
- Nếu $0^\circ \le \varphi < 90^\circ$ (góc nhọn): $\cos\varphi > 0 \implies \vec A\cdot\vec B > 0$.
- Nếu $90^\circ < \varphi \le 180^\circ$ (góc tù): $\cos\varphi < 0 \implies \vec A\cdot\vec B < 0$.
- Nếu $\varphi = 90^\circ$ (hai vector vuông góc nhau): $\cos 90^\circ = 0 \implies \vec A\cdot\vec B = 0$.

![Hình 1.27: Dấu của tích vô hướng theo góc giữa hai vector. Dấu của tích vô hướng trong các trường hợp góc khác nhau](/vat-ly-1/bai-giang/img/young-01/hinh-1-27.png)

- **(a) Góc nhọn**: Tích vô hướng mang dấu dương ($\vec A\cdot\vec B > 0$).
- **(b) Góc tù**: Tích vô hướng mang dấu âm ($\vec A\cdot\vec B < 0$).
- **(c) Vuông góc**: Tích vô hướng đúng bằng không ($\vec A\cdot\vec B = 0$).

Vì $AB\cos\varphi = BA\cos\varphi$, tích vô hướng có **tính chất giao hoán**:

$$
\vec A\cdot\vec B = \vec B\cdot\vec A.
$$

Ta sẽ sử dụng tích vô hướng ở chương 6 để định nghĩa công cơ học của một lực ($W = \vec F\cdot\vec s$), và trong các chương điện từ để tính thông lượng điện trường, thế điện và năng lượng từ trường.

### Tính tích vô hướng bằng các thành phần tọa độ

Xét hệ vector đơn vị trực chuẩn $\hat{\mathbf i}, \hat{\mathbf j}, \hat{\mathbf k}$. Vì chúng có độ lớn bằng $1$ và đôi một vuông góc, bảng tích (1.17) là:

$$
\begin{aligned}
\hat{\mathbf i}\cdot\hat{\mathbf i} &= \hat{\mathbf j}\cdot\hat{\mathbf j} = \hat{\mathbf k}\cdot\hat{\mathbf k} = 1, \\
\hat{\mathbf i}\cdot\hat{\mathbf j} &= \hat{\mathbf i}\cdot\hat{\mathbf k} = \hat{\mathbf j}\cdot\hat{\mathbf k} = 0.
\end{aligned}
$$

Khi phân tích hai vector $\vec A$ và $\vec B$ theo các thành phần tọa độ:

$$
\begin{aligned}
\vec A &= A_x\hat{\mathbf i} + A_y\hat{\mathbf j} + A_z\hat{\mathbf k}, \\
\vec B &= B_x\hat{\mathbf i} + B_y\hat{\mathbf j} + B_z\hat{\mathbf k}.
\end{aligned}
$$

Khai triển phân phối tạo ra chín tích đơn vị. Để theo dõi từng số hạng mà không viết một dòng quá dài, đặt $p_{ab}=A_aB_b(\hat{\mathbf e}_a\cdot\hat{\mathbf e}_b)$, trong đó $a,b$ lần lượt nhận các giá trị $x,y,z$. Ở đây $\hat{\mathbf e}_x=\hat{\mathbf i}$, $\hat{\mathbf e}_y=\hat{\mathbf j}$ và $\hat{\mathbf e}_z=\hat{\mathbf k}$.

Khai triển (1.18) gồm đầy đủ chín số hạng sau:

$$
\begin{aligned}
p_{xx} &= A_xB_x(\hat{\mathbf i}\cdot\hat{\mathbf i}) = A_xB_x, \\
p_{xy} &= A_xB_y(\hat{\mathbf i}\cdot\hat{\mathbf j}) = 0, \\
p_{xz} &= A_xB_z(\hat{\mathbf i}\cdot\hat{\mathbf k}) = 0, \\
p_{yx} &= A_yB_x(\hat{\mathbf j}\cdot\hat{\mathbf i}) = 0, \\
p_{yy} &= A_yB_y(\hat{\mathbf j}\cdot\hat{\mathbf j}) = A_yB_y, \\
p_{yz} &= A_yB_z(\hat{\mathbf j}\cdot\hat{\mathbf k}) = 0, \\
p_{zx} &= A_zB_x(\hat{\mathbf k}\cdot\hat{\mathbf i}) = 0, \\
p_{zy} &= A_zB_y(\hat{\mathbf k}\cdot\hat{\mathbf j}) = 0, \\
p_{zz} &= A_zB_z(\hat{\mathbf k}\cdot\hat{\mathbf k}) = A_zB_z.
\end{aligned}
$$

Gom mỗi hàng của phép phân phối thành một tổng:

$$
\begin{aligned}
p_x &= p_{xx}+p_{xy}+p_{xz} \\
&= A_xB_x, \\
p_y &= p_{yx}+p_{yy}+p_{yz} \\
&= A_yB_y, \\
p_z &= p_{zx}+p_{zy}+p_{zz} \\
&= A_zB_z.
\end{aligned}
$$

Theo tính phân phối, tích vô hướng bằng $p_x+p_y+p_z$. Sáu tích của hai vector đơn vị khác nhau bằng không. Chỉ ba tích cùng hướng còn lại. Đặt $S=\vec A\cdot\vec B$, công thức (1.19) là:

$$
S = A_xB_x+A_yB_y+A_zB_z.
$$

Như vậy: Tích vô hướng của hai vector bằng tổng tích các thành phần tọa độ tương ứng của chúng.

### Ví dụ 1.9: Tính tích vô hướng của hai vector

::: exercise Ví dụ 1.9: Tính tích vô hướng của hai vector
Tìm tích vô hướng $\vec A\cdot\vec B$ của hai vector trong mặt phẳng $xy$ ở Hình 1.28, biết độ lớn $A = 4.00$, $B = 5.00$. Góc định hướng của $\vec A$ và $\vec B$ so với trục dương $+x$ lần lượt là $53.0^\circ$ và $130.0^\circ$.
:::

![Hình 1.28: Hai vector trong mặt phẳng xy. Hai vector $\vec A$ và $\vec B$ trong mặt phẳng $xy$](/vat-ly-1/bai-giang/img/young-01/hinh-1-28.png)

::: solution Lời giải
**Tóm tắt đề bài**:
- Vector $\vec A$: $A = 4.00$, góc $\theta_A = 53.0^\circ$.
- Vector $\vec B$: $B = 5.00$, góc $\theta_B = 130.0^\circ$.
- Cần tìm: Tích vô hướng $\vec A\cdot\vec B$ bằng cả hai phương pháp (hình học và thành phần giải tích).

**Hướng đi**:
- Phương pháp 1 (Hình học): Tìm góc $\varphi = \theta_B - \theta_A$, rồi áp dụng $\vec A\cdot\vec B = AB\cos\varphi$.
- Phương pháp 2 (Giải tích): Tính các thành phần $(A_x, A_y)$ và $(B_x, B_y)$, rồi áp dụng $\vec A\cdot\vec B = A_x B_x + A_y B_y$.

**Lời giải chi tiết**:
Bước 1. Phương pháp hình học:
   Góc hợp bởi hai vector là:

$$
\varphi = 130.0^\circ - 53.0^\circ = 77.0^\circ.
$$

Áp dụng định nghĩa tích vô hướng:

$$
\begin{aligned}
\vec A\cdot\vec B &= AB\cos\varphi \\
&= (20.0)\cos 77.0^\circ \\
&\approx 4.50.
\end{aligned}
$$

Bước 2. Phương pháp thành phần tọa độ:
   Tính các thành phần của từng vector:

$$
\begin{aligned}
A_x &= 4.00\cos 53.0^\circ \\
&\approx 2.407, \\
A_y &= 4.00\sin 53.0^\circ \\
&\approx 3.195, \\
B_x &= 5.00\cos 130.0^\circ \\
&\approx -3.214, \\
B_y &= 5.00\sin 130.0^\circ \\
&\approx 3.830.
\end{aligned}
$$

Tính tích vô hướng từ các tích thành phần $A_x B_x \approx -7.736$ và $A_y B_y \approx 12.237$:

$$
\begin{aligned}
\vec A\cdot\vec B &= A_x B_x + A_y B_y \\
&\approx -7.736 + 12.237 \\
&\approx 4.50.
\end{aligned}
$$

**Đánh giá**:
Cả hai phương pháp hình học và giải tích đều cho kết quả trùng khớp chính xác: $\vec A\cdot\vec B = 4.50$. Tùy thuộc vào dữ kiện đề bài, ta có thể lựa chọn phương pháp thuận tiện nhất.
:::

### Ví dụ 1.10: Tìm góc giữa hai vector bằng tích vô hướng

::: exercise Ví dụ 1.10: Tìm góc giữa hai vector bằng tích vô hướng
Tìm góc hợp bởi hai vector sau trong không gian ba chiều:

$$
\begin{aligned}
\vec A &= 2.00\hat{\mathbf i} + 3.00\hat{\mathbf j} + 1.00\hat{\mathbf k}, \\
\vec B &= -4.00\hat{\mathbf i} + 2.00\hat{\mathbf j} - 1.00\hat{\mathbf k}.
\end{aligned}
$$
:::

![Hình 1.29: Hai vector trong không gian ba chiều](/vat-ly-1/bai-giang/img/young-01/hinh-1-29.png)

::: solution Lời giải
**Tóm tắt đề bài**:
- $\vec A = 2.00\hat{\mathbf i} + 3.00\hat{\mathbf j} + 1.00\hat{\mathbf k}$.
- $\vec B = -4.00\hat{\mathbf i} + 2.00\hat{\mathbf j} - 1.00\hat{\mathbf k}$.
- Cần tìm: Góc $\varphi$ giữa hai vector.

**Hướng đi**:
- Vận dụng hệ thức liên hệ: $\vec A\cdot\vec B = AB\cos\varphi$ suy ra $\cos\varphi = \frac{\vec A\cdot\vec B}{AB}$.
- Tính tích vô hướng từ các thành phần tọa độ theo công thức tích vô hướng.
- Tính độ lớn $A$ và $B$, từ đó suy ra giá trị $\cos\varphi$ và góc $\varphi$.

**Lời giải chi tiết**:
Bước 1. Tính tích vô hướng của hai vector với các tích thành phần $A_x B_x = -8.00$, $A_y B_y = 6.00$, và $A_z B_z = -1.00$:

$$
\begin{aligned}
\vec A\cdot\vec B &= -8.00 + 6.00 - 1.00 \\
&= -3.00.
\end{aligned}
$$

Bước 2. Tính độ lớn của từng vector từ các thành phần:

$$
\begin{aligned}
A &= \sqrt{4.00 + 9.00 + 1.00} \\
&= \sqrt{14.00}, \\
B &= \sqrt{16.00 + 4.00 + 1.00} \\
&= \sqrt{21.00}.
\end{aligned}
$$

Bước 3. Xác định góc giữa hai vector:

$$
\begin{aligned}
\cos\varphi &= \frac{\vec A\cdot\vec B}{AB} \\
&= \frac{-3.00}{\sqrt{14.00}\sqrt{21.00}} \\
&= \frac{-3.00}{\sqrt{294.00}} \\
&\approx -0.175.
\end{aligned}
$$

Suy ra:

$$
\varphi = \arccos(-0.175) \approx 100^\circ.
$$

**Đánh giá**:
Vì tích vô hướng mang dấu âm ($\vec A\cdot\vec B = -3.00 < 0$), góc $\varphi$ bắt buộc phải là một góc tù ($90^\circ < \varphi < 180^\circ$). Kết quả $\varphi \approx 100^\circ$ hoàn toàn phù hợp với lý thuyết và hình vẽ trực quan trong không gian.
:::

### Tích có hướng

Tích có hướng của hai vector $\vec A$ và $\vec B$ (tiếng Anh là *vector product* hay *cross product*) được ký hiệu là $\vec A\times\vec B$. Kết quả của phép toán này là một **vector mới** (ký hiệu $\vec C = \vec A\times\vec B$).

Trước hết, xét hai vector $\vec A$ và $\vec B$ khác không, không cùng phương. Đặt chúng có chung điểm gốc như ở Hình 1.30a. Khi đó, hai vector xác định một mặt phẳng duy nhất. Vector tích có hướng $\vec C = \vec A\times\vec B$ là một vector vuông góc với mặt phẳng chứa hai vector ban đầu (tức vuông góc với cả $\vec A$ lẫn $\vec B$), có độ lớn cho bởi công thức (1.20):

$$
C = AB\sin\varphi.
$$

Trong đó $\varphi$ là góc giữa $\vec A$ và $\vec B$ ($0^\circ \le \varphi \le 180^\circ$). Vì $\sin\varphi \ge 0$ trong khoảng này, độ lớn $C$ luôn không âm ($C \ge 0$). Nếu hai vector cùng phương ($\varphi = 0^\circ$ hoặc $\varphi = 180^\circ$), thì tích có hướng bằng vector không: $\vec A\times\vec B = \vec 0$. Nếu một trong hai vector là vector không, tích cũng bằng vector không. Vector không không có hướng xác định. Đặc biệt: Tích có hướng của một vector với chính nó luôn bằng không: $\vec A\times\vec A = \vec 0$.

::: warning Phân biệt rõ hai phép nhân vector
- Độ lớn của tích có hướng là $AB\sin\varphi$, đạt cực đại khi hai vector vuông góc ($\varphi = 90^\circ$) và bằng $0$ khi cùng phương.
- Tích vô hướng là $AB\cos\varphi$, đạt cực đại khi hai vector cùng hướng ($\varphi = 0^\circ$) và bằng $0$ khi vuông góc.
:::

Khi tích có hướng khác không, hướng của $\vec C = \vec A\times\vec B$ được xác định bằng **quy tắc bàn tay phải**:
1. Đặt hai vector chung gốc.
2. Duỗi các ngón bàn tay phải theo hướng của vector thứ nhất $\vec A$, lòng bàn tay hướng về phía vector thứ hai $\vec B$.
3. Khum các ngón tay từ $\vec A$ sang $\vec B$ theo cung góc nhỏ $\varphi$.
4. Ngón tay cái duỗi ra chỉ đúng hướng của vector tích có hướng $\vec A\times\vec B$.

![Hình 1.30: Quy tắc bàn tay phải và tính phản giao hoán. Quy tắc bàn tay phải xác định hướng của tích có hướng](/vat-ly-1/bai-giang/img/young-01/hinh-1-30.png)

- **(a) Tích $\vec A\times\vec B$**: Ngón cái hướng lên trên.
- **(b) Tích $\vec B\times\vec A$**: Khum ngón tay từ $\vec B$ sang $\vec A$, ngón cái hướng xuống dưới.

Do đó, tích có hướng không có tính giao hoán mà mang **tính chất phản giao hoán**, theo hệ thức (1.21):

$$
\vec A\times\vec B = -\vec B\times\vec A.
$$

Về mặt hình học, $B\sin\varphi$ chính là thành phần của vector $\vec B$ vuông góc với phương của vector $\vec A$. Do đó: Độ lớn của tích có hướng bằng độ lớn của $\vec A$ nhân với thành phần vuông góc của $\vec B$ (hoặc ngược lại, bằng độ lớn của $\vec B$ nhân với thành phần vuông góc của $\vec A$).

![Hình 1.31: Ý nghĩa hình học của độ lớn tích có hướng. Độ lớn tích có hướng qua thành phần vuông góc](/vat-ly-1/bai-giang/img/young-01/hinh-1-31.png)

### Tính tích có hướng bằng các thành phần tọa độ

Xét bảng tích có hướng (1.22) giữa các vector đơn vị trực chuẩn trong hệ tọa độ thuận:

$$
\begin{aligned}
\hat{\mathbf i}\times\hat{\mathbf i} &= \hat{\mathbf j}\times\hat{\mathbf j} = \hat{\mathbf k}\times\hat{\mathbf k} = \vec 0, \\
\hat{\mathbf i}\times\hat{\mathbf j} &= -\hat{\mathbf j}\times\hat{\mathbf i} = \hat{\mathbf k}, \\
\hat{\mathbf j}\times\hat{\mathbf k} &= -\hat{\mathbf k}\times\hat{\mathbf j} = \hat{\mathbf i}, \\
\hat{\mathbf k}\times\hat{\mathbf i} &= -\hat{\mathbf i}\times\hat{\mathbf k} = \hat{\mathbf j}.
\end{aligned}
$$

Tương tự tích vô hướng, phép phân phối tạo chín tích có hướng. Đặt $\vec q_{ab}=A_aB_b(\hat{\mathbf e}_a\times\hat{\mathbf e}_b)$, với $a,b\in\{x,y,z\}$ và các vector đơn vị như đã định nghĩa. Khai triển (1.23) gồm:

$$
\begin{aligned}
\vec q_{xx} &= A_xB_x(\hat{\mathbf i}\times\hat{\mathbf i}) = \vec 0, \\
\vec q_{xy} &= A_xB_y(\hat{\mathbf i}\times\hat{\mathbf j}) \\
&= A_xB_y\hat{\mathbf k}, \\
\vec q_{xz} &= A_xB_z(\hat{\mathbf i}\times\hat{\mathbf k}) \\
&= -A_xB_z\hat{\mathbf j}, \\
\vec q_{yx} &= A_yB_x(\hat{\mathbf j}\times\hat{\mathbf i}) \\
&= -A_yB_x\hat{\mathbf k}, \\
\vec q_{yy} &= A_yB_y(\hat{\mathbf j}\times\hat{\mathbf j}) = \vec 0, \\
\vec q_{yz} &= A_yB_z(\hat{\mathbf j}\times\hat{\mathbf k}) \\
&= A_yB_z\hat{\mathbf i}, \\
\vec q_{zx} &= A_zB_x(\hat{\mathbf k}\times\hat{\mathbf i}) \\
&= A_zB_x\hat{\mathbf j}, \\
\vec q_{zy} &= A_zB_y(\hat{\mathbf k}\times\hat{\mathbf j}) \\
&= -A_zB_y\hat{\mathbf i}, \\
\vec q_{zz} &= A_zB_z(\hat{\mathbf k}\times\hat{\mathbf k}) = \vec 0.
\end{aligned}
$$

Tích $\vec A\times\vec B$ bằng tổng chín vector này. Ba số hạng trên đường chéo bằng vector không. Gom hai số hạng theo mỗi hướng đơn vị, ta được dạng phân tích của hệ thức (1.24):

$$
\begin{aligned}
\vec C_x &= \vec q_{yz}+\vec q_{zy} \\
&= (A_yB_z-A_zB_y)\hat{\mathbf i}, \\
\vec C_y &= \vec q_{zx}+\vec q_{xz} \\
&= (A_zB_x-A_xB_z)\hat{\mathbf j}, \\
\vec C_z &= \vec q_{xy}+\vec q_{yx} \\
&= (A_xB_y-A_yB_x)\hat{\mathbf k}.
\end{aligned}
$$

Ghép ba vector thành phần:

$$
\begin{aligned}
\vec C &= \vec C_x+\vec C_y+\vec C_z \\
&= C_x\hat{\mathbf i}+C_y\hat{\mathbf j}+C_z\hat{\mathbf k}.
\end{aligned}
$$

So sánh với biểu diễn vector bằng các vector đơn vị, ta đọc được ba thành phần trong công thức (1.25):

$$
\begin{aligned}
C_x &= A_yB_z-A_zB_y, \\
C_y &= A_zB_x-A_xB_z, \\
C_z &= A_xB_y-A_yB_x.
\end{aligned}
$$

### Hệ tọa độ thuận và hệ tọa độ nghịch

Trong học phần này, ta dùng **hệ tọa độ thuận**, hay hệ bàn tay phải. Hệ này thỏa mãn $\hat{\mathbf i}\times\hat{\mathbf j}=\hat{\mathbf k}$, như Hình 1.32a. Nếu đảo chiều trục $z$ và giữ hai trục còn lại, ta được hệ tọa độ nghịch ở Hình 1.32b. Khi đó, $\hat{\mathbf i}\times\hat{\mathbf j}=-\hat{\mathbf k}$.

Trong hệ nghịch, dấu của các tích có hướng giữa những vector đơn vị khác nhau ngược với bảng (1.22). Vì vậy, các công thức thành phần (1.25) đang dùng phải được hiểu trong hệ tọa độ thuận. Việc đảo một trục không làm toàn bộ công thức khác, chẳng hạn tích vô hướng hay độ lớn vector, đồng loạt đổi dấu.

![Hình 1.32: Hệ tọa độ thuận và nghịch. Hệ tọa độ bàn tay phải và bàn tay trái](/vat-ly-1/bai-giang/img/young-01/hinh-1-32.png)

### Ví dụ 1.11: Tính tích có hướng của hai vector

::: exercise Ví dụ 1.11: Tính tích có hướng của hai vector
Vector $\vec A$ có độ lớn $6.0$ đơn vị, hướng dọc theo trục $+x$. Vector $\vec B$ có độ lớn $4.0$ đơn vị, nằm trong mặt phẳng $xy$ và hợp với trục $+x$ một góc $30.0^\circ$ như ở Hình 1.33. Hãy tìm vector tích có hướng $\vec C = \vec A\times\vec B$.
:::

![Hình 1.33: Tích có hướng của hai vector trong mặt phẳng xy. Vector tích có hướng hướng dọc theo trục $z$](/vat-ly-1/bai-giang/img/young-01/hinh-1-33.png)

::: solution Lời giải
**Tóm tắt đề bài**:
- Vector $\vec A$: $A = 6.0$, hướng theo trục $+x$.
- Vector $\vec B$: $B = 4.0$, nằm trong mặt phẳng $xy$, góc $\varphi = 30.0^\circ$.
- Cần tìm: Vector $\vec C = \vec A\times\vec B$.

**Hướng đi**:
- Phương pháp 1 (Hình học): Tính độ lớn $C = AB\sin\varphi$, sau đó áp dụng quy tắc bàn tay phải để xác định hướng.
- Phương pháp 2 (Giải tích): Phân tích hai vector thành các thành phần tọa độ rồi áp dụng công thức thành phần của tích có hướng.

**Lời giải chi tiết**:
Bước 1. Phương pháp hình học:
   Tính độ lớn của tích có hướng:

$$
\begin{aligned}
C &= AB\sin\varphi \\
&= (6.0)(4.0)\sin 30.0^\circ \\
&= 12.0.
\end{aligned}
$$

Áp dụng quy tắc bàn tay phải: Khum các ngón tay từ $\vec A$ sang $\vec B$ trong mặt phẳng $xy$, ngón tay cái chỉ vuông góc hướng lên theo chiều dương của trục $z$ (hướng của vector đơn vị $\hat{\mathbf k}$). Do đó:

$$
\vec C = 12.0\hat{\mathbf k}.
$$

Bước 2. Phương pháp thành phần giải tích:
   Xác định các thành phần tọa độ:

$$
\begin{aligned}
A_x &= 6.0, \\
A_y &= 0.0, \\
A_z &= 0.0, \\
B_x &= 4.0\cos 30.0^\circ = 2.0\sqrt{3}, \\
B_y &= 4.0\sin 30.0^\circ = 2.0, \\
B_z &= 0.0.
\end{aligned}
$$

Áp dụng công thức tính các thành phần của tích có hướng:

$$
\begin{aligned}
C_x &= A_y B_z - A_z B_y = 0.0, \\
C_y &= A_z B_x - A_x B_z = 0.0, \\
C_z &= A_x B_y - A_y B_x \\
&= (6.0)(2.0) - 0.0 \\
&= 12.0.
\end{aligned}
$$

Kết hợp các thành phần lại, ta thu được:

$$
\vec C = 12.0\hat{\mathbf k}.
$$

**Đánh giá**:
Cả hai phương pháp đều cho cùng một kết quả chính xác: Vector tích có hướng có độ lớn bằng $12.0$ và hướng dọc theo chiều dương của trục $z$.
:::

### Câu hỏi tự kiểm tra hiểu bài 1.10

::: exercise Câu hỏi tự kiểm tra 1.10: Giá trị của tích vô hướng và tích có hướng
Cho hai vector $\vec A$ có độ lớn $A = 2$ và $\vec B$ có độ lớn $B = 3$. Góc $\varphi$ giữa hai vector nhận một trong ba giá trị sau: (i) $0^\circ$, (ii) $90^\circ$, hoặc (iii) $180^\circ$. Hãy xác định giá trị của góc $\varphi$ trong mỗi trường hợp sau (có thể có nhiều hơn một góc thỏa mãn):

**(a)** $\vec A\cdot\vec B = 0$.

**(b)** $\vec A\times\vec B = \vec 0$.

**(c)** $\vec A\cdot\vec B = 6$.

**(d)** $\vec A\cdot\vec B = -6$.

**(e)** $\|\vec A\times\vec B\| = 6$.
:::

::: solution Lời giải chi tiết
**(a) Chọn (ii) $90^\circ$**:
Tích vô hướng $\vec A\cdot\vec B = AB\cos\varphi = 0$. Vì $A \ne 0, B \ne 0$, ta có $\cos\varphi = 0$ suy ra $\varphi = 90^\circ$ (hai vector vuông góc nhau).

**(b) Chọn (i) $0^\circ$ hoặc (iii) $180^\circ$**:
Độ lớn tích có hướng $\|\vec A\times\vec B\| = AB\sin\varphi = 0$ suy ra $\sin\varphi = 0$, dẫn đến $\varphi = 0^\circ$ (cùng chiều) hoặc $\varphi = 180^\circ$ (ngược chiều).

**(c) Chọn (i) $0^\circ$**:
Tích vô hướng đạt giá trị cực đại bằng tích hai độ lớn: $\vec A\cdot\vec B = AB = 6$ suy ra $\cos\varphi = 1$, kéo theo $\varphi = 0^\circ$ (hai vector cùng hướng).

**(d) Chọn (iii) $180^\circ$**:
Tích vô hướng đạt giá trị cực tiểu: $\vec A\cdot\vec B = -AB = -6$ suy ra $\cos\varphi = -1$, kéo theo $\varphi = 180^\circ$ (hai vector ngược hướng).

**(e) Chọn (ii) $90^\circ$**:
Độ lớn tích có hướng đạt cực đại bằng tích hai độ lớn: $\|\vec A\times\vec B\| = AB = 6$ suy ra $\sin\varphi = 1$, kéo theo $\varphi = 90^\circ$ (hai vector vuông góc nhau).
:::
