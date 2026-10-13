<!-- Bài 25.79–25.82, trang in 843. -->

## Bài tập nâng cao và MCAT

### Đoạn đọc: Khả năng dẫn điện của mạng nhện

Một số loài nhện tạo mạng bằng những sợi tơ khô được phủ dung dịch chứa nhiều hợp chất. Lớp phủ này khiến sợi tơ có tính hút ẩm, nghĩa là có thể hút nước từ không khí. Các nhà nghiên cứu đưa ra giả thuyết rằng lớp nước trên bề mặt giúp sợi tơ dẫn điện tốt.

Để khảo sát tính chất điện của sợi tơ đã phủ, họ đặt một đoạn dài 5 mm giữa hai tiếp điểm điện. Họ kéo giãn sợi tơ từng bước 1 mm cho đến khi chiều dài vượt quá gấp đôi ban đầu, rồi để sợi co trở lại chiều dài ban đầu, cũng theo từng bước 1 mm. Bảng dưới đây ghi lại một số số đo điện trở.

| Chiều dài sợi tơ (mm) | Điện trở sợi tơ (10⁹ Ω) |
| ---: | ---: |
| 5 | 9 |
| 7 | 19 |
| 9 | 41 |
| 11 | 63 |
| 13 | 102 |
| 9 | 76 |
| 7 | 50 |
| 5 | 24 |

*Dữ liệu dựa trên nghiên cứu của F. Vollrath và D. Edmonds, “Consequences of electrical conductivity in an orb spider’s capture web,” Naturwissenschaften, tập 100, số 12, tháng 12 năm 2013, trang 1163–1169.*

::: exercise 25.79 • MCAT
Giải thích nào phù hợp nhất với xu hướng trong số liệu?

(a) Sợi dài hơn có thể mang dòng điện lớn hơn sợi ngắn, nên dẫn điện tốt hơn.

(b) Khi bị kéo dài đến 13 mm, sợi không còn dẫn điện vì lớp phủ mỏng bị đứt.

(c) Khi sợi bị kéo giãn, lớp phủ mỏng đi và điện trở tăng. Khi sợi co lại, lớp phủ gần trở về trạng thái ban đầu.

(d) Điện trở của sợi tăng theo khoảng cách tính từ đầu sợi.
:::

<!-- detailed-solution:25.79 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Điện trở tăng từ 9 GΩ lên 102 GΩ khi sợi dài từ 5 mm đến 13 mm. Khi sợi co lại, điện trở giảm nhưng ở cùng chiều dài 9 mm và 7 mm, giá trị lúc co lớn hơn lúc kéo.

**Hướng đi:**

- So sánh điện trở theo chiều dài trong hai lượt kéo và co.
- Xác định mô hình nào giải thích được cả xu hướng tăng khi kéo lẫn sự khác nhau giữa hai lượt.

Khi kéo dài sợi, điện trở tăng đều theo số liệu. Khi co lại, điện trở giảm, nhưng tại 9 mm điện trở là 76 GΩ thay vì 41 GΩ, còn tại 7 mm là 50 GΩ thay vì 19 GΩ. Vì vậy đáp án (c) phù hợp nhất: lớp phủ hút ẩm thay đổi khi bị kéo và chỉ gần phục hồi sau khi sợi co lại. Dữ liệu không ủng hộ việc sợi mất hoàn toàn tính dẫn điện tại 13 mm, vì khi đó vẫn đo được điện trở hữu hạn 102 GΩ.
:::

::: exercise 25.80 • MCAT
Nếu độ dẫn điện chỉ do lớp nước phủ tạo ra, tiết diện $A$ của lớp phủ khi sợi dài 13 mm so với lúc ban đầu dài 5 mm như thế nào? Giả sử điện trở suất của lớp phủ không đổi và lớp phủ đồng đều dọc sợi. Tỉ số $A_{13\,\mathrm{mm}}/A_{5\,\mathrm{mm}}$ xấp xỉ bằng (a) $1/10$, (b) $1/4$, (c) $2/5$ hay (d) 1.
:::

<!-- detailed-solution:25.80 -->
::: solution Chi tiết
**Tóm tắt đề bài:** So sánh tiết diện lớp phủ khi chiều dài là 13 mm và 5 mm. Điện trở suất không đổi, lớp phủ đồng đều. Từ bảng, điện trở tương ứng là 102 GΩ và 9 GΩ.

**Hướng đi:**

- Dùng $R=\rho L/A$ cho mỗi chiều dài.
- Lấy tỉ số để triệt tiêu điện trở suất, rồi chọn phương án gần nhất.

Với điện trở suất không đổi, $A=\rho L/R$, do đó

$$
\begin{aligned}
&\frac{A_{13}}{A_5} = \frac{13/102}{5/9}\\
&\quad =\frac{13}{5}\frac{9}{102}\\
&\quad \approx 0{,}229.
\end{aligned}
$$

Giá trị này gần $1/4=0{,}250$ nhất. Chọn (b). Tiết diện giảm còn khoảng 23% giá trị ban đầu, phù hợp với giả thuyết lớp dẫn điện mỏng đi khi sợi bị kéo.
:::

::: exercise 25.81 • MCAT
Trong thí nghiệm này, nguồn điện là pin 9 V. Dòng điện lớn nhất chạy qua sợi tơ xấp xỉ bằng bao nhiêu? (a) 1 A, (b) 0,1 A, (c) 1 mA hay (d) 1 nA.
:::

<!-- detailed-solution:25.81 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Hiệu điện thế nguồn là 9 V. Điện trở nhỏ nhất trong bảng là 9 GΩ.

**Hướng đi:**

- Theo định luật Ôm, dòng lớn nhất ứng với điện trở nhỏ nhất khi điện áp không đổi.
- Đổi GΩ sang Ω trước khi tính.

$$
\begin{aligned}
&I_{\max} = \frac{9\,\mathrm V}{9\times10^9\,\Omega}\\
&\quad =1{,}0\times10^{-9}\,\mathrm A.
\end{aligned}
$$

Vậy dòng cực đại khoảng 1 nA, chọn (d).
:::

::: exercise 25.82 • MCAT
Trong một thí nghiệm khác, một phần mạng nhện được treo tự do để có thể chuyển động. Khi đưa một vật tích điện dương hoặc âm đến gần mạng, sợi tơ đều chuyển động về phía vật đó. Cách giải thích nào phù hợp nhất? Mạng nhện là (a) vật dẫn mang điện âm, (b) vật dẫn mang điện dương, (c) vật dẫn mang điện dương hoặc âm hay (d) vật dẫn trung hòa về điện.
:::

<!-- detailed-solution:25.82 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Vật tích điện ở gần có thể mang điện dương hoặc âm. Trong cả hai trường hợp, sợi tơ trung hòa bị hút về phía vật.

**Hướng đi:**

- Xét sự phân bố lại điện tích trong vật dẫn khi có điện tích ngoài.
- So sánh lực hút do phân cực với khả năng một vật mang điện cùng dấu bị đẩy.

Một vật dẫn trung hòa có thể phân cực khi đặt gần vật tích điện. Điện tích trái dấu với vật ngoài dịch chuyển về phía gần hơn, còn điện tích cùng dấu dịch chuyển ra xa. Vì lực Coulomb mạnh hơn ở khoảng cách ngắn, lực hút ở phía gần lớn hơn lực đẩy ở phía xa. Do đó vật dẫn trung hòa bị hút dù vật ngoài mang điện dương hay âm. Chọn (d).
:::
