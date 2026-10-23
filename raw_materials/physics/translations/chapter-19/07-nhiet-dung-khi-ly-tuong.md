## 19.7 Nhiệt dung của khí lý tưởng

Khi nghiên cứu về nhiệt lượng, chúng ta đã định nghĩa nhiệt dung riêng và nhiệt dung mol của các chất. Đối với chất khí, nhiệt dung mol phụ thuộc rất lớn vào điều kiện mà quá trình truyền nhiệt diễn ra, cụ thể là thể tích của khối khí được giữ cố định hay áp suất được giữ cố định. Trong mục này, chúng ta sẽ khảo sát hai đại lượng cơ bản: Nhiệt dung mol đẳng tích $C_V$ và nhiệt dung mol đẳng áp $C_p$.

Để so sánh hai nhiệt dung, trước hết viết nguyên lý thứ nhất:

$$
Q=\Delta U+W. \tag{19.11}
$$

Cùng một độ tăng nhiệt độ làm nội năng của một lượng khí lý tưởng tăng như nhau. Khi giãn nở ở áp suất không đổi, khí còn sinh công, nên cần nhận thêm nhiệt lượng so với khi giữ thể tích cố định.

### Nhiệt dung mol đẳng tích và biểu thức nội năng

Xét một khối khí lý tưởng gồm $n$ mol được chứa trong một bình cứng có thể tích không đổi $V$ (Hình 19.18a). Khi ta truyền một lượng nhiệt vi phân $dQ$ vào bình để làm nhiệt độ của khối khí tăng thêm một lượng vi phân $dT$, nhiệt dung mol đẳng tích $C_V$ được định nghĩa theo hệ thức:

$$
dQ = n C_V dT \tag{19.12}
$$

![Hình 19.18: Đo nhiệt dung mol của một khối khí lý tưởng: (a) Giữ thể tích không đổi bằng bình chứa cứng. (b) Giữ áp suất không đổi bằng piston di động có tải trọng cố định.](../img/young-19/b-hinh-19-18.png)

Trong quá trình đẳng tích, do thể tích không thay đổi ($dV = 0$), khối khí không thực hiện công cơ học lên môi trường:

$$
dW = 0
$$

Áp dụng nguyên lý thứ nhất của nhiệt động lực học dưới dạng vi phân $dQ = dU + dW$, ta nhận được:

$$
dU = dQ
$$

Thay định nghĩa nhiệt dung đẳng tích vào hệ thức $dU=dQ$, ta được:

$$
dU = n C_V dT \tag{19.13}
$$

Đây là một trong những kết quả quan trọng nhất của nhiệt động lực học khí lý tưởng. Như chúng ta đã chứng minh ở mục 19.6, nội năng $U$ của một khối khí lý tưởng chỉ phụ thuộc duy nhất vào nhiệt độ $T$. Với cùng lượng khí lý tưởng và cùng nhiệt độ ban đầu, một độ tăng nhiệt độ $dT$ cho trước làm nội năng tăng cùng một lượng $dU$. Kết quả không phụ thuộc việc giữ thể tích, giữ áp suất hay đi theo một đường khác.

Do đó, phương trình (19.13) có giá trị tổng quát cho mọi quá trình của khí lý tưởng. Đối với độ biến thiên nhiệt độ hữu hạn từ $T_1$ đến $T_2$, nếu $C_V$ gần như không đổi trong khoảng đang xét thì:

$$
\Delta U = n C_V \Delta T
$$

với $\Delta T=T_2-T_1$. Khi $C_V$ phụ thuộc nhiệt độ, cần dùng dạng tích phân:

$$
\Delta U=n\int_{T_1}^{T_2}C_V(T)\,dT.
$$

### Nhiệt dung mol đẳng áp và hệ thức Mayer

Bây giờ, chúng ta xét cùng khối khí gồm $n$ mol đó, nhưng được đặt trong một xi lanh có piston di chuyển tự do không ma sát, chịu một áp suất ngoài $p$ không đổi (Hình 19.18b và Hình 19.19). Khi ta cung cấp một lượng nhiệt $dQ$ để nâng nhiệt độ của khối khí lên cùng một lượng $dT$, nhiệt dung mol đẳng áp $C_p$ được định nghĩa bởi:

$$
dQ = n C_p dT \tag{19.14}
$$

![Hình 19.19: Nâng nhiệt độ của một khối khí lý tưởng từ $T_1$ lên $T_2$ bằng hai con đường khác nhau: Quá trình đẳng tích (khí không sinh công, $Q = \Delta U$) và quá trình đẳng áp (khí giãn nở sinh công, $Q = \Delta U + W$).](../img/young-19/b-hinh-19-19.png)

Trong quá trình đẳng áp này, khi nhiệt độ tăng thì thể tích khối khí tăng thêm một lượng $dV$, khối khí thực hiện công cơ học lên piston:

$$
dW = p dV
$$

Từ phương trình trạng thái khí lý tưởng $pV = nRT$, lấy vi phân hai vế trong điều kiện áp suất $p$ không đổi, ta thu được mối liên hệ:

$$
p dV = n R dT
$$

Do đó, công cơ học vi phân do chất khí sinh ra có thể viết dưới dạng:

$$
dW = n R dT \tag{19.15}
$$

Áp dụng nguyên lý thứ nhất của nhiệt động lực học cho quá trình đẳng áp này:

$$
dQ = dU + dW
$$

Thay $dQ = n C_p dT$ và $dW = n R dT$ vào, ta có:

$$
n C_p dT = dU + n R dT \tag{19.16}
$$

Vì nội năng của khí lý tưởng chỉ phụ thuộc vào nhiệt độ nên biến thiên nội năng $dU$ ở đây cũng chính bằng $n C_V dT$ theo phương trình (19.13). Thay $dU = n C_V dT$ vào phương trình (19.16), ta được:

$$
n C_p dT = n(C_V + R) dT
$$

Triệt tiêu thừa số chung $n dT$ ở cả hai vế, ta thu được hệ thức Mayer:

$$
C_p = C_V + R \tag{19.17}
$$

Hệ thức (19.17) giải thích rõ ràng tại sao nhiệt dung mol đẳng áp $C_p$ luôn lớn hơn nhiệt dung mol đẳng tích $C_V$ một lượng đúng bằng hằng số khí lý tưởng $R = 8{,}314\text{ J/(mol}\cdot\text{K)}$. Trong quá trình đẳng tích, toàn bộ nhiệt lượng truyền vào làm tăng nội năng. Tùy cấu trúc phân tử và nhiệt độ, năng lượng này có thể phân bố vào chuyển động tịnh tiến, quay và dao động. Trái lại, trong quá trình đẳng áp, ngoài việc tăng nội năng đúng bằng lượng như ở quá trình đẳng tích, hệ còn phải tiêu tốn thêm một phần năng lượng để sinh công cơ học đẩy piston chống lại áp suất môi trường ngoài.

Một chất có thể co lại khi được đun nóng ở áp suất không đổi, như nước trong khoảng $0$–$4^\circ\mathrm C$. Khi đó, công biến đổi thể tích là âm và $Q<\Delta U$ trên quá trình đang xét.

Không được từ nhận xét này suy ra quan hệ nhiệt dung của khí lý tưởng cho chất lỏng. Nội năng của nước có thể phụ thuộc cả thể tích, nên hai đường đẳng tích và đẳng áp có cùng độ tăng nhiệt độ không nhất thiết có cùng $\Delta U$.

### Tỷ số nhiệt dung

Tỷ số giữa hai nhiệt dung mol được ký hiệu bằng chữ cái Hy Lạp $\gamma$ (gamma):

$$
\gamma = \frac{C_p}{C_V} \tag{19.18}
$$

Sử dụng hệ thức $C_p = C_V + R$, ta có thể biểu diễn $\gamma$ dưới dạng:

$$
\gamma = 1 + \frac{R}{C_V}
$$

Vì hằng số khí $R$ luôn dương nên với khí lý tưởng có nhiệt dung dương, $C_p>C_V$ và $\gamma>1$.

### Thuyết động học phân tử và cấu trúc phân tử

Theo thuyết động học phân tử, nhiệt dung mol của chất khí phản ánh trực tiếp số bậc tự do chuyển động của các phân tử cấu thành:

1. Khí đơn nguyên tử (như He, Ne, Ar): Phân tử chỉ là một chất điểm, có 3 bậc tự do chuyển động tịnh tiến trong không gian ba chiều. Nội năng của $n$ mol khí đơn nguyên tử là:

$$
U = \frac{3}{2} n R T
$$

Lấy đạo hàm theo nhiệt độ, ta thu được các giá trị lý thuyết:

$$
C_V = \frac{3}{2} R
$$

Giá trị này xấp xỉ bằng $12{,}47\text{ J/(mol}\cdot\text{K)}$. Từ đó:

$$
C_p = C_V + R = \frac{5}{2} R
$$

Giá trị đẳng áp tương ứng xấp xỉ $20{,}79\text{ J/(mol}\cdot\text{K)}$, và tỷ số nhiệt dung là:

$$
\gamma = \frac{5}{3} \approx 1{,}67
$$

2. Khí lưỡng nguyên tử (như $\text{H}_2, \text{N}_2, \text{O}_2, \text{CO}$ ở nhiệt độ phòng): Mỗi phân tử có dạng hình học đối xứng trục giống như quả tạ, gồm 3 bậc tự do tịnh tiến và 2 bậc tự do quay quanh hai trục vuông góc với trục liên kết (tổng cộng 5 bậc tự do). Do đó:

$$
U = \frac{5}{2} n R T
$$

Nhiệt dung mol đẳng tích và đẳng áp tương ứng là:

$$
C_V = \frac{5}{2} R
$$

Giá trị này xấp xỉ $20{,}79\text{ J/(mol}\cdot\text{K)}$. Nhiệt dung đẳng áp là:

$$
C_p = C_V + R = \frac{7}{2} R
$$

Giá trị này xấp xỉ $29{,}10\text{ J/(mol}\cdot\text{K)}$, dẫn đến tỷ số nhiệt dung:

$$
\gamma = \frac{7}{5} = 1{,}40
$$

3. Với phân tử nhiều nguyên tử, số bậc tự do quay phụ thuộc cấu trúc thẳng hay không thẳng, còn đóng góp dao động phụ thuộc nhiệt độ. Bảng 19.1 cho thấy các khí đa nguyên tử được liệt kê có $C_V$ lớn hơn và $\gamma$ gần $1$ hơn so với những khí đơn nguyên tử.

**Bảng 19.1: Nhiệt dung mol của một số chất khí ở áp suất thấp**

Các cột nhiệt dung và hiệu nhiệt dung đều có đơn vị $\mathrm{J/(mol\,K)}$. Tỉ số $\gamma$ không có đơn vị.

<div class="lecture-data-table">

| Loại khí | Chất khí | $C_V$ | $C_p$ | $C_p-C_V$ | $\gamma$ |
| --- | --- | --- | --- | --- | --- |
| <span class="table-cell-label">Loại khí</span> Đơn nguyên tử | <span class="table-cell-label">Chất khí</span> He | <span class="table-cell-label">$C_V$</span> 12,47 | <span class="table-cell-label">$C_p$</span> 20,78 | <span class="table-cell-label">$C_p-C_V$</span> 8,31 | <span class="table-cell-label">$\gamma$</span> 1,67 |
| <span class="table-cell-label">Loại khí</span> Đơn nguyên tử | <span class="table-cell-label">Chất khí</span> Ar | <span class="table-cell-label">$C_V$</span> 12,47 | <span class="table-cell-label">$C_p$</span> 20,78 | <span class="table-cell-label">$C_p-C_V$</span> 8,31 | <span class="table-cell-label">$\gamma$</span> 1,67 |
| <span class="table-cell-label">Loại khí</span> Lưỡng nguyên tử | <span class="table-cell-label">Chất khí</span> H₂ | <span class="table-cell-label">$C_V$</span> 20,42 | <span class="table-cell-label">$C_p$</span> 28,74 | <span class="table-cell-label">$C_p-C_V$</span> 8,32 | <span class="table-cell-label">$\gamma$</span> 1,41 |
| <span class="table-cell-label">Loại khí</span> Lưỡng nguyên tử | <span class="table-cell-label">Chất khí</span> N₂ | <span class="table-cell-label">$C_V$</span> 20,76 | <span class="table-cell-label">$C_p$</span> 29,07 | <span class="table-cell-label">$C_p-C_V$</span> 8,31 | <span class="table-cell-label">$\gamma$</span> 1,40 |
| <span class="table-cell-label">Loại khí</span> Lưỡng nguyên tử | <span class="table-cell-label">Chất khí</span> O₂ | <span class="table-cell-label">$C_V$</span> 20,85 | <span class="table-cell-label">$C_p$</span> 29,17 | <span class="table-cell-label">$C_p-C_V$</span> 8,32 | <span class="table-cell-label">$\gamma$</span> 1,40 |
| <span class="table-cell-label">Loại khí</span> Lưỡng nguyên tử | <span class="table-cell-label">Chất khí</span> CO | <span class="table-cell-label">$C_V$</span> 20,85 | <span class="table-cell-label">$C_p$</span> 29,16 | <span class="table-cell-label">$C_p-C_V$</span> 8,31 | <span class="table-cell-label">$\gamma$</span> 1,40 |
| <span class="table-cell-label">Loại khí</span> Đa nguyên tử | <span class="table-cell-label">Chất khí</span> CO₂ | <span class="table-cell-label">$C_V$</span> 28,46 | <span class="table-cell-label">$C_p$</span> 36,94 | <span class="table-cell-label">$C_p-C_V$</span> 8,48 | <span class="table-cell-label">$\gamma$</span> 1,30 |
| <span class="table-cell-label">Loại khí</span> Đa nguyên tử | <span class="table-cell-label">Chất khí</span> SO₂ | <span class="table-cell-label">$C_V$</span> 31,39 | <span class="table-cell-label">$C_p$</span> 40,37 | <span class="table-cell-label">$C_p-C_V$</span> 8,98 | <span class="table-cell-label">$\gamma$</span> 1,29 |
| <span class="table-cell-label">Loại khí</span> Đa nguyên tử | <span class="table-cell-label">Chất khí</span> H₂S | <span class="table-cell-label">$C_V$</span> 25,95 | <span class="table-cell-label">$C_p$</span> 34,60 | <span class="table-cell-label">$C_p-C_V$</span> 8,65 | <span class="table-cell-label">$\gamma$</span> 1,33 |

</div>


Các giá trị đo cho thấy $C_p-C_V$ gần $R$ ở nhiều khí, nhưng không hoàn toàn bằng nhau vì đây là khí thực. Ba cột đầu tương ứng với dữ liệu nhiệt dung đẳng tích đã xét ở chương trước.

::: Example Ví dụ 19.6: Làm mát căn phòng

Một phòng ở ký túc xá hoặc phòng ngủ điển hình chứa khoảng $2500$ mol không khí. Tìm độ biến thiên nội năng của lượng không khí này khi được làm nguội từ $35{,}0^\circ\mathrm C$ xuống $26{,}0^\circ\mathrm C$ ở áp suất không đổi $1{,}00\,\mathrm{atm}$. Coi không khí là khí lý tưởng có $\gamma=1{,}400$.

**Tóm tắt đề bài:**

- Lượng khí: $n=2500\,\mathrm{mol}$.
- Nhiệt độ đầu: $T_1=35{,}0^\circ\mathrm C$.
- Nhiệt độ cuối: $T_2=26{,}0^\circ\mathrm C$.
- Tỉ số nhiệt dung: $\gamma=1{,}400$.
- Cần tìm: Độ biến thiên nội năng $\Delta U$.

**Hướng đi:**

- Nội năng khí lý tưởng chỉ phụ thuộc nhiệt độ. Dùng $\Delta U=nC_V\Delta T$ dù quá trình đang xét là đẳng áp.
- Tìm $C_V$ từ hai hệ thức $C_p=C_V+R$ và $\gamma=C_p/C_V$. Không thay $C_V$ bằng $C_p$ khi tính nội năng.

**Lời giải:**

Từ hai hệ thức nhiệt dung:

$$
\gamma=1+\frac{R}{C_V}.
$$

Suy ra:

$$
\begin{aligned}
C_V&=\frac{R}{\gamma-1}\\
&=\frac{8{,}314}{0{,}400}\\
&=20{,}785\,\mathrm{J/(mol\,K)}.
\end{aligned}
$$

Độ biến thiên nhiệt độ là $\Delta T=-9{,}0\,\mathrm K$. Bởi vậy:

$$
\begin{aligned}
\Delta U&=nC_V\Delta T\\
&\approx-4{,}68\times10^5\,\mathrm J.
\end{aligned}
$$

**Đánh giá:** Nội năng lượng không khí đã giảm khoảng $468\,\mathrm{kJ}$. Nhiệt lượng trao đổi trong quá trình đẳng áp còn liên hệ với công nén khi khí co lại, nên không được đồng nhất riêng $\Delta U$ với $Q$. Việc tính nội năng vẫn dùng $C_V$ cho cả quá trình đẳng tích lẫn đẳng áp.
:::

::: Info Câu tự kiểm tra 19.7

Bạn muốn làm nguội một bình chứa $10$ mol khí nén từ $30^\circ\mathrm C$ xuống $20^\circ\mathrm C$. Loại khí nào cần truyền ra ít nhiệt lượng nhất trong mô hình khí lý tưởng?

- (i) Khí đơn nguyên tử.
- (ii) Khí lưỡng nguyên tử.
- (iii) Khí đa nguyên tử.
- (iv) Cả ba loại đều như nhau.

<details><summary>Xem lời giải thích</summary>

Chọn (i). Bình có thể tích cố định nên không có công do thay đổi thể tích. Nhiệt lượng cần lấy ra có độ lớn:

$$
|Q|=nC_V|\Delta T|.
$$

Số mol và độ giảm nhiệt độ như nhau, nên loại có $C_V$ nhỏ nhất cần lấy ra ít nhiệt lượng nhất. Trong mô hình nhiệt dung đang xét, khí đơn nguyên tử có $C_V=3R/2$, nhỏ hơn khí lưỡng nguyên tử và đa nguyên tử khi các bậc tự do quay tương ứng đã tham gia.

</details>
:::
