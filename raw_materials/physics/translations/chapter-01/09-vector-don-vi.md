<!-- Nguồn: mục 1.9, trang in 18–19, trang PDF 38–39; gồm công thức 1.12–1.15, Hình 1.24–1.25, Ví dụ 1.8 và câu hỏi. -->

## 1.9. Vector đơn vị

**Vector đơn vị** có độ lớn bằng $1$ và không có đơn vị đo. Nó chỉ dùng để xác định một hướng trong không gian. Vector đơn vị cho cách viết thuận tiện nhiều biểu thức chứa các thành phần vector. Sách dùng dấu mũ trên ký hiệu để phân biệt nó với vector thông thường, vốn có thể có độ lớn bằng hoặc khác $1$.

Trong hệ $xy$, đặt $\hat{\mathbf i}$ theo chiều $+x$ và $\hat{\mathbf j}$ theo chiều $+y$, như Hình 1.24a. Khi ấy:

$$\vec A=A_x\hat{\mathbf i}+A_y\hat{\mathbf j}.\tag{1.12}$$

Đây là phương trình vector. Mỗi số hạng, chẳng hạn $A_x\hat{\mathbf i}$, là một vector, như Hình 1.24b.

![Hình 1.24 nguyên tác: vector đơn vị theo hai trục và cách biểu diễn vector bằng thành phần](img/young-01/hinh-1-24.png)

**Hình 1.24:** (a) $\hat{\mathbf i}$, $\hat{\mathbf j}$ hướng theo các trục dương $x$, $y$, mỗi vector có độ lớn $1$. (b) $\vec A$ là tổng $A_x\hat{\mathbf i}+A_y\hat{\mathbf j}$.

Dùng vector đơn vị, phép cộng hai vector được viết thành:

$$
\begin{aligned}
\vec A&=A_x\hat{\mathbf i}+A_y\hat{\mathbf j},\\
\vec B&=B_x\hat{\mathbf i}+B_y\hat{\mathbf j},\\
\vec R&=\vec A+\vec B\\
&=(A_x\hat{\mathbf i}+A_y\hat{\mathbf j})
 +(B_x\hat{\mathbf i}+B_y\hat{\mathbf j})\\
&=(A_x+B_x)\hat{\mathbf i}+(A_y+B_y)\hat{\mathbf j}\\
&=R_x\hat{\mathbf i}+R_y\hat{\mathbf j}.
\end{aligned}\tag{1.13}
$$

Công thức (1.13) diễn đạt nội dung hai phương trình thành phần (1.9) bằng một phương trình vector duy nhất.

Nếu các vector không cùng nằm trong mặt phẳng $xy$, cần thêm thành phần thứ ba. Đặt $\hat{\mathbf k}$ theo chiều $+z$, như Hình 1.25. Khi đó:

$$
\begin{aligned}
\vec A&=A_x\hat{\mathbf i}+A_y\hat{\mathbf j}+A_z\hat{\mathbf k},\\
\vec B&=B_x\hat{\mathbf i}+B_y\hat{\mathbf j}+B_z\hat{\mathbf k}.
\end{aligned}\tag{1.14}
$$

$$
\begin{aligned}
\vec R&=(A_x+B_x)\hat{\mathbf i}
 +(A_y+B_y)\hat{\mathbf j}
 +(A_z+B_z)\hat{\mathbf k}\\
&=R_x\hat{\mathbf i}+R_y\hat{\mathbf j}+R_z\hat{\mathbf k}.
\end{aligned}\tag{1.15}
$$

![Hình 1.25 nguyên tác: ba vector đơn vị theo các trục dương trong không gian](img/young-01/hinh-1-25.png)

**Hình 1.25:** Các vector đơn vị $\hat{\mathbf i}$, $\hat{\mathbf j}$, $\hat{\mathbf k}$ lần lượt hướng theo $+x$, $+y$, $+z$, và đều có độ lớn $1$.

### Ví dụ 1.8 — Sử dụng vector đơn vị

::: exercise Đề bài trong sách
Cho hai độ dời:

$$
\begin{aligned}
\vec D&=(6.00\hat{\mathbf i}+3.00\hat{\mathbf j}-1.00\hat{\mathbf k})\,\mathrm m,\\
\vec E&=(4.00\hat{\mathbf i}-5.00\hat{\mathbf j}+8.00\hat{\mathbf k})\,\mathrm m.
\end{aligned}
$$

Tìm độ lớn của $2\vec D-\vec E$.
:::

::: solution Lời giải của sách
**Xác định và thiết lập.** Nhân $\vec D$ với số vô hướng $2$, rồi trừ $\vec E$, để được $\vec F=2\vec D-\vec E$. Theo (1.8), nhân vector với $2$ nghĩa là nhân mỗi thành phần với $2$. Dùng (1.15) để trừ, với lưu ý trừ vector tương đương cộng vector đối.

**Thực hiện.**

$$
\begin{aligned}
\vec F
&=2(6.00\hat{\mathbf i}+3.00\hat{\mathbf j}-1.00\hat{\mathbf k})\,\mathrm m\\
&\quad-(4.00\hat{\mathbf i}-5.00\hat{\mathbf j}+8.00\hat{\mathbf k})\,\mathrm m\\
&=[(12.00-4.00)\hat{\mathbf i}
 +(6.00+5.00)\hat{\mathbf j}\\
&\qquad+(-2.00-8.00)\hat{\mathbf k}]\,\mathrm m\\
&=(8.00\hat{\mathbf i}+11.00\hat{\mathbf j}-10.00\hat{\mathbf k})\,\mathrm m.
\end{aligned}
$$

Theo (1.11):

$$
\begin{aligned}
F&=\sqrt{F_x^2+F_y^2+F_z^2}\\
&=\sqrt{(8.00\,\mathrm m)^2+(11.00\,\mathrm m)^2+(-10.00\,\mathrm m)^2}\\
&\approx16.9\,\mathrm m.
\end{aligned}
$$

**Đánh giá.** Kết quả cùng bậc độ lớn với các thành phần lớn hơn trong tổng. Ta không chờ đợi độ lớn lớn hơn chúng quá nhiều, nhưng trong các trường hợp khác nó có thể nhỏ hơn nhiều do triệt tiêu.

**Ý chính của ví dụ:** Vector đơn vị cho phép viết một phương trình cộng vector bao gồm cả ba thành phần $x$, $y$, $z$.
:::

### Câu hỏi kiểm tra hiểu mục 1.9

::: exercise Câu hỏi trong sách
Sắp xếp các vector sau theo độ lớn giảm dần:

$$
\begin{aligned}
\text{(i)}\quad\vec A&=(3\hat{\mathbf i}+5\hat{\mathbf j}-2\hat{\mathbf k})\,\mathrm m,\\
\text{(ii)}\quad\vec B&=(-3\hat{\mathbf i}+5\hat{\mathbf j}-2\hat{\mathbf k})\,\mathrm m,\\
\text{(iii)}\quad\vec C&=(3\hat{\mathbf i}-5\hat{\mathbf j}-2\hat{\mathbf k})\,\mathrm m,\\
\text{(iv)}\quad\vec D&=(3\hat{\mathbf i}+5\hat{\mathbf j}+2\hat{\mathbf k})\,\mathrm m.
\end{aligned}
$$
:::

::: solution Đáp án của sách
Tất cả có cùng độ lớn, dù hướng khác nhau:

$$
\begin{aligned}
A=B=C=D
&=\sqrt{(\pm3\,\mathrm m)^2+(\pm5\,\mathrm m)^2+(\pm2\,\mathrm m)^2}\\
&=\sqrt{9+25+4}\,\mathrm m
=\sqrt{38}\,\mathrm m
\approx6.2\,\mathrm m.
\end{aligned}
$$
:::
