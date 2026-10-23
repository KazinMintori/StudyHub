<!-- Nguồn: Trang in 224, trang PDF 244; Tóm tắt toàn bộ Chương 7. -->

## Tóm tắt Chương 7: Thế năng và bảo toàn năng lượng

### 1. Thế năng trọng trường và thế năng đàn hồi

Công thực hiện lên một vật bởi trọng lực không đổi có thể biểu diễn qua độ giảm của thế năng trọng trường $U_{g} = mgy$. Dạng năng lượng này là đặc tính chung của cả hệ gồm vật thể và Trái Đất.

Tương tự, thế năng cũng gắn liền với lực đàn hồi $F_x = -kx$ của lò xo lý tưởng tuân theo định luật Hooke (với $x$ là độ dãn hoặc độ nén tính từ vị trí cân bằng). Công sinh ra bởi lực đàn hồi bằng độ giảm thế năng đàn hồi của lò xo: $U_{e} = \frac{1}{2}kx^2$.

![Bảng tóm tắt 1: Thế năng trọng trường và thế năng đàn hồi](/vat-ly-1/bai-giang/img/young-07/r-theory-tom-tat-01.png)

Các phương trình cốt lõi:
$$
\begin{aligned}
W_{g} &= mgy_1 - mgy_2 \\
&= U_{g, 1} - U_{g, 2} \\
&= -\Delta U_{g}
\end{aligned}
$$

Công thức (7.2, 7.3).
$$
\begin{aligned}
W_{e} &= \frac{1}{2}kx_1^2 - \frac{1}{2}kx_2^2 \\
&= U_{e, 1} - U_{e, 2} \\
&= -\Delta U_{e}
\end{aligned}
$$

Công thức (7.10, 7.11).

### 2. Khi cơ năng toàn phần được bảo toàn

Thế năng toàn phần $U$ của hệ là tổng của thế năng trọng trường và thế năng đàn hồi:
$$
U = U_{g} + U_{e}
$$
Nếu không có lực nào khác ngoài trọng lực và lực đàn hồi sinh công lên vật, tổng động năng và thế năng của hệ là một đại lượng bảo toàn. Tổng này được gọi là cơ năng toàn phần: $E = K + U$.

![Bảng tóm tắt 2: Khi cơ năng toàn phần được bảo toàn](/vat-ly-1/bai-giang/img/young-07/r-theory-tom-tat-02.png)

Phương trình bảo toàn cơ năng:
$$
K_1 + U_1 = K_2 + U_2
$$

Công thức (7.4, 7.12).

### 3. Khi cơ năng toàn phần không được bảo toàn

Khi có các lực khác ngoài trọng lực và lực đàn hồi sinh công lên vật (như lực ma sát, lực cản chất lưu hay lực kéo đẩy từ bên ngoài), công $W_{o}$ do các lực này thực hiện bằng đúng độ biến thiên của cơ năng toàn phần:

![Bảng tóm tắt 3: Khi cơ năng toàn phần không được bảo toàn](/vat-ly-1/bai-giang/img/young-07/r-theory-tom-tat-03.png)

Phương trình năng lượng tổng quát:
$$
K_1 + U_1 + W_{o} = K_2 + U_2
$$

Công thức (7.14).

### 4. Lực bảo toàn, lực không bảo toàn và định luật bảo toàn năng lượng

Mọi lực trong tự nhiên đều thuộc một trong hai loại: Lực bảo toàn (lực thế) hoặc lực không bảo toàn (lực phi thế).
- Lực bảo toàn là lực mà mối quan hệ công – động năng có tính thuận nghịch hoàn toàn. Công của lực bảo toàn luôn biểu diễn được qua hàm thế năng.
- Lực không bảo toàn không thể biểu diễn bằng hàm thế năng. Công của lực ma sát làm tiêu tán cơ năng thành nội năng $U_{\mathrm{int}}$ (làm nóng các vật thể).
- Tổng của động năng, thế năng và nội năng của một hệ cô lập luôn luôn được bảo toàn.

![Bảng tóm tắt 4: Lực bảo toàn, lực không bảo toàn và định luật bảo toàn năng lượng](/vat-ly-1/bai-giang/img/young-07/r-theory-tom-tat-04.png)

Định luật bảo toàn năng lượng tổng quát:
$$
\Delta K + \Delta U + \Delta U_{\mathrm{int}} = 0
$$

Công thức (7.15).

### 5. Xác định lực từ hàm thế năng

Đối với chuyển động dọc theo một đường thẳng, thành phần lực bảo toàn $F_x(x)$ bằng đạo hàm có dấu trừ của hàm thế năng tương ứng $U(x)$. Trong không gian ba chiều, các thành phần của lực bảo toàn là đạo hàm riêng có dấu trừ của $U(x, y, z)$.

![Bảng tóm tắt 5: Xác định lực từ hàm thế năng](/vat-ly-1/bai-giang/img/young-07/r-theory-tom-tat-05.png)

Các hệ thức vi phân xác định lực:
$$
F_x(x) = -\frac{dU(x)}{dx}
$$

Công thức (7.16).
$$
\begin{aligned}
F_x &= -\frac{\partial U}{\partial x}, \\
F_y &= -\frac{\partial U}{\partial y}, \\
F_z &= -\frac{\partial U}{\partial z}
\end{aligned}
$$

Công thức (7.17).
$$
\vec{F} = -\vec{\nabla} U
$$

Công thức (7.18).

Tại vị trí cân bằng, lực tác dụng triệt tiêu ($\frac{dU}{dx} = 0$). Vị trí cực tiểu của $U(x)$ ứng với trạng thái cân bằng bền, vị trí cực đại ứng với trạng thái cân bằng không bền.
