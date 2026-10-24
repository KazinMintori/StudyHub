## 1.9. Vector đơn vị

**Vector đơn vị** là một vector có độ lớn đúng bằng $1$ và không mang đơn vị đo lường. Mục đích duy nhất của vector đơn vị là xác định một hướng xác định trong không gian. Sử dụng vector đơn vị cho phép biểu diễn các đại lượng vector một cách gọn gàng, thuận tiện cho việc biến đổi giải tích.

Ký hiệu dấu mũ trên đầu vector như $\hat{\mathbf i}, \hat{\mathbf j}, \hat{\mathbf k}$ được dùng để phân biệt vector đơn vị với vector thông thường (vốn có thể có độ lớn bất kỳ).

Trong hệ tọa độ vuông góc hai chiều $xy$, ta định nghĩa $\hat{\mathbf i}$ là vector đơn vị hướng theo chiều dương của trục $x$, và $\hat{\mathbf j}$ là vector đơn vị hướng theo chiều dương của trục $y$ như minh họa ở Hình 1.24a. Khi đó, mọi vector $\vec A$ nằm trong mặt phẳng $xy$ đều có thể biểu diễn bằng công thức (1.12):

$$
\vec A = A_x\hat{\mathbf i} + A_y\hat{\mathbf j}.
$$

Đây là một phương trình vector hoàn chỉnh. Trong phương trình này, mỗi số hạng $A_x\hat{\mathbf i}$ và $A_y\hat{\mathbf j}$ là một vector thành phần dọc theo từng trục tương ứng, như thể hiện ở Hình 1.24b.

![Hình 1.24: Các vector đơn vị trong mặt phẳng. Biểu diễn vector trong mặt phẳng bằng các vector đơn vị $\hat{\mathbf i}$ và $\hat{\mathbf j}$](/vat-ly-1/bai-giang/img/young-01/hinh-1-24.png)

- **(a) Hệ vector đơn vị trực chuẩn**: $\hat{\mathbf i}$ và $\hat{\mathbf j}$ có độ lớn bằng $1$, lần lượt hướng theo các chiều dương $+x$ và $+y$.
- **(b) Biểu diễn vector**: Vector $\vec A$ được phân tích thành tổng của hai vector thành phần: $\vec A = A_x\hat{\mathbf i} + A_y\hat{\mathbf j}$.

Nhờ hệ vector đơn vị, phép cộng được thực hiện bằng cách cộng các hệ số cùng hướng. Với hai vector trong mặt phẳng, đặt:

$$
\begin{aligned}
\vec R_x &= (A_x+B_x)\hat{\mathbf i}, \\
\vec R_y &= (A_y+B_y)\hat{\mathbf j}.
\end{aligned}
$$

Hai vector thành phần này có tổng bằng $\vec R$. Vì $R_x=A_x+B_x$ và $R_y=A_y+B_y$, hệ thức (1.13) được viết:

$$
\begin{aligned}
\vec R &= \vec A+\vec B \\
&= \vec R_x+\vec R_y \\
&= R_x\hat{\mathbf i}+R_y\hat{\mathbf j}.
\end{aligned}
$$

Như vậy, cộng các vector là cộng đại số những thành phần tương ứng, rồi ghép các vector thành phần lại.

Khi mở rộng ra không gian ba chiều, ta bổ sung trục $z$ vuông góc với mặt phẳng $xy$ và vector đơn vị $\hat{\mathbf k}$ hướng dọc theo chiều dương của trục $z$, như minh họa ở Hình 1.25. Mỗi vector trong không gian ba chiều được viết theo công thức (1.14):

$$
\vec A = A_x\hat{\mathbf i} + A_y\hat{\mathbf j} + A_z\hat{\mathbf k}.
$$

Vector tổng $\vec R = \vec A + \vec B$ trong không gian ba chiều có dạng:

$$
\vec R = R_x\hat{\mathbf i} + R_y\hat{\mathbf j} + R_z\hat{\mathbf k},
$$

Đây là hệ thức (1.15), với các thành phần tọa độ:

$$
\begin{aligned}
R_x &= A_x+B_x, \\
R_y &= A_y+B_y, \\
R_z &= A_z+B_z.
\end{aligned}
$$

Vì vậy ba vector thành phần lần lượt là $(A_x+B_x)\hat{\mathbf i}$, $(A_y+B_y)\hat{\mathbf j}$ và $(A_z+B_z)\hat{\mathbf k}$. Cộng chúng cho cùng vector $\vec R$ ở trên.

![Hình 1.25: Ba vector đơn vị trực chuẩn trong không gian. Các vector đơn vị $\hat{\mathbf i}, \hat{\mathbf j}, \hat{\mathbf k}$ trong không gian ba chiều](/vat-ly-1/bai-giang/img/young-01/hinh-1-25.png)

### Ví dụ 1.8: Sử dụng vector đơn vị trong không gian ba chiều

::: exercise Ví dụ 1.8: Sử dụng vector đơn vị trong không gian ba chiều
Cho hai vector độ dời $\vec D$ và $\vec E$ trong không gian ba chiều (đơn vị đo là mét):

$$
\begin{aligned}
\vec D &= 6.00\hat{\mathbf i} + 3.00\hat{\mathbf j} - 1.00\hat{\mathbf k}, \\
\vec E &= 4.00\hat{\mathbf i} - 5.00\hat{\mathbf j} + 8.00\hat{\mathbf k}.
\end{aligned}
$$

Hãy tìm độ lớn của vector $\vec F = 2\vec D - \vec E$.
:::

::: solution Lời giải
**Tóm tắt đề bài**:
- Vector $\vec D = 6.00\hat{\mathbf i} + 3.00\hat{\mathbf j} - 1.00\hat{\mathbf k}$ (đơn vị $\mathrm m$).
- Vector $\vec E = 4.00\hat{\mathbf i} - 5.00\hat{\mathbf j} + 8.00\hat{\mathbf k}$ (đơn vị $\mathrm m$).
- Cần tìm: Độ lớn $\|\vec F\|$ của vector $\vec F = 2\vec D - \vec E$.

**Hướng đi**:
- Thực hiện phép nhân số vô hướng với vector: Nhân hệ số $2$ vào từng thành phần của $\vec D$.
- Trừ từng thành phần tương ứng của $\vec E$ khỏi $2\vec D$ để xác định các thành phần $(F_x, F_y, F_z)$.
- Áp dụng công thức tính độ lớn trong không gian ba chiều: $F = \sqrt{F_x^2 + F_y^2 + F_z^2}$.

**Lời giải chi tiết**:
Bước 1. Tính các thành phần của vector $\vec F = 2\vec D - \vec E$ (với $F_x = 2(6.00) - 4.00$, $F_y = 2(3.00) - (-5.00)$, $F_z = 2(-1.00) - 8.00$):

$$
\begin{aligned}
F_x &= 8.00\,\mathrm m, \\
F_y &= 11.00\,\mathrm m, \\
F_z &= -10.00\,\mathrm m.
\end{aligned}
$$

Do đó vector $\vec F$ được biểu diễn là:

$$
\vec F = (8\hat{\mathbf i} + 11\hat{\mathbf j} - 10\hat{\mathbf k})\,\mathrm m.
$$

Bước 2. Tính độ lớn của vector $\vec F$:

$$
\begin{aligned}
F &= \sqrt{F_x^2 + F_y^2 + F_z^2} \\
&= \sqrt{8^2 + 11^2 + (-10)^2}\,\mathrm m \\
&= \sqrt{64 + 121 + 100}\,\mathrm m \\
&= \sqrt{285}\,\mathrm m \\
&\approx 16.9\,\mathrm m.
\end{aligned}
$$

**Đánh giá**:
Độ lớn $16.9\,\mathrm m$ có cùng bậc độ lớn với các thành phần lớn nhất ($11.00\,\mathrm m$ và $10.00\,\mathrm m$), hoàn toàn hợp lý. Vì bình phương của số âm là một số dương, thành phần âm $F_z = -10.00\,\mathrm m$ đóng góp dương vào độ lớn tổng quát.
:::

### Câu hỏi tự kiểm tra hiểu bài 1.9

::: exercise Câu hỏi tự kiểm tra 1.9: So sánh độ lớn của các vector trong không gian
Sắp xếp các vector sau theo thứ tự độ lớn giảm dần (đơn vị đo là mét):
- (i) $\vec A = (3\hat{\mathbf i} + 5\hat{\mathbf j} - 2\hat{\mathbf k})\,\mathrm m$.
- (ii) $\vec B = (-3\hat{\mathbf i} + 5\hat{\mathbf j} - 2\hat{\mathbf k})\,\mathrm m$.
- (iii) $\vec C = (3\hat{\mathbf i} - 5\hat{\mathbf j} - 2\hat{\mathbf k})\,\mathrm m$.
- (iv) $\vec D = (3\hat{\mathbf i} + 5\hat{\mathbf j} + 2\hat{\mathbf k})\,\mathrm m$.
:::

::: solution Lời giải chi tiết
Tất cả bốn vector trên đều có độ lớn bằng nhau:

$$
\begin{aligned}
A &= \sqrt{3^2 + 5^2 + 2^2}\,\mathrm m \\
&= \sqrt{9 + 25 + 4}\,\mathrm m \\
&= \sqrt{38}\,\mathrm m \\
&\approx 6.2\,\mathrm m.
\end{aligned}
$$

Do đó: $A = B = C = D \approx 6.2\,\mathrm m$.

**Giải thích**:
Dù bốn vector có các dấu thành phần khác nhau (tương ứng hướng về các góc phần tám khác nhau trong không gian ba chiều), độ lớn của mỗi vector được tính bằng căn bậc hai của tổng bình phương các thành phần. Vì $(\pm x)^2 = x^2$, dấu của các thành phần không ảnh hưởng đến độ lớn của vector.
:::
