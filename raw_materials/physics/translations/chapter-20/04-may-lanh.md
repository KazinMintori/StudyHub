## 20.4 Máy làm lạnh

Chúng ta có thể hình dung máy làm lạnh như một động cơ nhiệt hoạt động theo chiều ngược lại. Một động cơ nhiệt nhận nhiệt lượng từ nơi có nhiệt độ cao và nhả nhiệt lượng cho nơi có nhiệt độ thấp hơn. Trái lại, máy làm lạnh lấy nhiệt lượng từ một nơi lạnh (khoang bên trong tủ lạnh) và nhả nhiệt lượng ra một nơi ấm hơn (thường là không khí trong căn phòng đặt tủ lạnh). Động cơ nhiệt tạo ra công cơ học hữu ích ra bên ngoài ($W > 0$), trong khi máy làm lạnh bắt buộc phải tiêu tốn một lượng công cơ học ròng cấp vào từ bên ngoài ($W < 0$).

Với các quy ước dấu đã thiết lập ở Mục 20.2: Đối với máy làm lạnh, nhiệt lượng lấy từ nguồn lạnh $Q_C$ mang giá trị dương ($Q_C > 0$), trong khi cả công $W$ và nhiệt lượng nhả cho nguồn nóng $Q_H$ đều mang giá trị âm ($W < 0$ và $Q_H < 0$). Do đó, độ lớn của công và nhiệt lượng nhả ra được viết là $|W| = -W$ và $|Q_H| = -Q_H$.

![Hình 20.8](../img/young-20/a-hinh-20-08.png)

*Hình 20.8: Sơ đồ dòng năng lượng mô tả nguyên lý làm việc của máy làm lạnh.*

Hình 20.8 biểu diễn sơ đồ dòng năng lượng cho một máy làm lạnh. Áp dụng nguyên lý thứ nhất của nhiệt động lực học cho một chu trình khép kín ($\Delta U = 0$):

$$
Q_H + Q_C - W = 0
$$

Kéo theo:

$$
-Q_H = Q_C - W
$$

Vì cả $Q_H$ và $W$ đều mang giá trị âm, ta có thể viết lại theo độ lớn:

$$
|Q_H| = Q_C + |W|
\tag{20.7}
$$

Như sơ đồ dòng năng lượng chỉ rõ, nhiệt lượng $|Q_H|$ nhả ra môi trường xung quanh luôn lớn hơn nhiệt lượng $Q_C$ hút từ buồng lạnh đúng bằng lượng công cơ học $|W|$ cấp vào. Lưu ý rằng hệ thức độ lớn tuyệt đối sau:

$$
|Q_H| = |Q_C| + |W|
\tag{20.8}
$$

nghiệm đúng cho cả động cơ nhiệt lẫn máy làm lạnh.

### Hệ số hiệu năng

Xét theo quan điểm kinh tế và hiệu quả sử dụng năng lượng, một chu trình làm lạnh tốt nhất là chu trình lấy đi được lượng nhiệt $|Q_C|$ lớn nhất từ bên trong buồng lạnh với lượng công cơ học $|W|$ phải tiêu tốn là nhỏ nhất. Vì vậy, tỉ số đánh giá hiệu quả kinh tế là $|Q_C|/|W|$; tỉ số này càng lớn thì máy làm lạnh vận hành càng hiệu quả. Đại lượng này được gọi là **hệ số hiệu năng** (coefficient of performance), ký hiệu là $K$.

Từ phương trình (20.8), ta có $|W| = |Q_H| - |Q_C|$, do đó:

$$
\begin{aligned}
K &= \frac{|Q_C|}{|W|} \\
&= \frac{|Q_C|}{|Q_H| - |Q_C|}
\end{aligned}
\tag{20.9}
$$

Như thường lệ, ta luôn đo lường $Q_H$, $Q_C$ và $W$ theo cùng một đơn vị năng lượng, do đó $K$ là một số thuần túy không có thứ nguyên. Khác với hiệu suất nhiệt $e$ của động cơ luôn nhỏ hơn 1, hệ số hiệu năng $K$ của máy làm lạnh thực tế thường có giá trị lớn hơn 1 (điển hình khoảng từ 2 đến 5 hoặc cao hơn).

### Máy làm lạnh trong thực tế

Hình 20.9a mô tả nguyên lý nhiệt động của chu trình làm lạnh cơ học dùng trong các tủ lạnh gia đình. Mạch ống kín chứa một môi chất lạnh (chất công tác). Nhánh bên trái của mạch ống (bao gồm dàn bay hơi đặt bên trong tủ lạnh) ở áp suất thấp và nhiệt độ thấp; nhánh bên phải của mạch ống (bao gồm dàn ngưng tụ đặt bên ngoài tủ lạnh) ở áp suất cao và nhiệt độ cao. Thông thường, cả hai nhánh đều chứa hỗn hợp chất lỏng và hơi ở trạng thái cân bằng pha.

![Hình 20.9](../img/young-20/a-hinh-20-09.png)

*Hình 20.9: (a) Nguyên lý chu trình làm lạnh cơ học; (b) Bố trí các bộ phận chính trong một tủ lạnh thực tế.*

Chu trình làm lạnh cơ học diễn ra qua năm giai đoạn liên tiếp:

1. **Giai đoạn nén**: Máy nén (thường dẫn động bằng động cơ điện) hút hơi môi chất lạnh, thực hiện công $|W|$ lên môi chất để nén đoạn nhiệt và đẩy môi chất có áp suất cao, nhiệt độ cao vào cuộn dây ngưng tụ. Vì máy nén đòi hỏi năng lượng đầu vào, tủ lạnh bắt buộc phải cắm điện để hoạt động.
2. **Giai đoạn ngưng tụ**: Môi chất bị nén trong dàn ngưng tụ có nhiệt độ cao hơn không khí bên ngoài phòng, do đó môi chất tỏa nhiệt $|Q_H|$ ra không khí xung quanh và ngưng tụ một phần thành thể lỏng ở áp suất cao.
3. **Giai đoạn tiết lưu**: Môi chất lỏng chảy qua van tiết lưu và giãn nở đoạn nhiệt qua một lỗ hẹp, khiến áp suất và nhiệt độ của môi chất giảm xuống rất thấp.
4. **Giai đoạn bay hơi**: Sau khi giãn nở, môi chất trong dàn bay hơi có nhiệt độ thấp hơn nhiệt độ bên trong buồng lạnh. Do đó, môi chất hấp thụ nhiệt $|Q_C|$ từ các đồ vật để trong tủ, làm lạnh khoang chứa và môi chất bay hơi một phần.
5. **Khép kín chu trình**: Hơi môi chất quay trở lại máy nén và một chu trình mới lại bắt đầu.

### Máy điều hòa không khí và bơm nhiệt

Máy điều hòa không khí (Hình 20.10) hoạt động hoàn toàn dựa trên cùng nguyên lý nhiệt động với tủ lạnh gia đình. Trong trường hợp này, khoang làm lạnh trở thành một căn phòng hoặc toàn bộ tòa nhà. Dàn bay hơi được đặt bên trong nhà, dàn ngưng tụ được đặt ngoài trời, và các quạt gió thổi không khí lưu thông qua các dàn ống này. Trong các hệ thống làm mát công nghiệp lớn, dàn ngưng tụ thường được làm mát bằng dòng nước tuần hoàn.

![Hình 20.10](../img/young-20/a-hinh-20-10.png)

*Hình 20.10: Máy điều hòa không khí hoạt động trên cùng nguyên lý với máy làm lạnh.*

Đối với máy điều hòa, các đại lượng có ý nghĩa thực tiễn lớn nhất là tốc độ lấy nhiệt khỏi phòng (gọi là dòng nhiệt $H$ từ không gian cần làm mát) và công suất tiêu thụ điện $P = |W|/t$ cấp cho máy nén. Nếu nhiệt lượng $|Q_C|$ được lấy đi trong thời gian $t$, thì dòng nhiệt làm mát là $H = |Q_C|/t$. Khi đó, ta có thể biểu diễn hệ số hiệu năng $K$ theo $H$ và $P$:

$$
\begin{aligned}
K &= \frac{|Q_C|}{|W|} = \frac{H t}{P t} \\
&= \frac{H}{P}
\end{aligned}
$$

Các máy điều hòa phòng điển hình có tốc độ làm mát $H$ vào khoảng $1500 - 3000\,\mathrm{W}$ và đòi hỏi công suất điện tiêu thụ vào khoảng $600 - 1200\,\mathrm{W}$. Hệ số hiệu năng điển hình của chúng đạt khoảng $K \approx 3$; giá trị chính xác phụ thuộc chặt chẽ vào độ chênh lệch nhiệt độ giữa trong phòng và ngoài trời.

Một biến thể kỹ thuật rất quan trọng của hệ thống làm lạnh là **bơm nhiệt** (heat pump), thiết bị dùng để sưởi ấm các tòa nhà vào mùa đông bằng cách làm lạnh không khí ngoài trời. Bơm nhiệt hoạt động giống như một chiếc máy làm lạnh được quay ngược từ trong ra ngoài: Dàn bay hơi được đặt ngoài trời để hấp thụ nhiệt từ không khí lạnh mùa đông, còn dàn ngưng tụ được đặt trong nhà để tỏa nhiệt sưởi ấm không khí phòng. Với thiết kế tối ưu, nhiệt lượng $|Q_H|$ cấp vào sưởi ấm trong nhà trong mỗi chu trình có thể lớn hơn rất nhiều so với lượng điện năng công $|W|$ cần cung cấp để vận hành máy ($|Q_H| = |Q_C| + |W| > |W|$).

### Sự cần thiết của công cơ học và máy lạnh không tốn công

Nhiệt lượng luôn luôn tự phát truyền từ một vật nóng sang một vật lạnh hơn. Để đảo ngược dòng nhiệt tự nhiên này, buộc nhiệt lượng truyền từ vật lạnh sang vật nóng, chúng ta bắt buộc phải cung cấp công cơ học từ bên ngoài vào hệ. Mọi kinh nghiệm thực tiễn và bằng chứng thực nghiệm đều khẳng định rằng không thể chế tạo được một chiếc máy làm lạnh nào có thể vận chuyển nhiệt từ một vật lạnh sang một vật nóng hơn mà không cần cung cấp công cơ học từ bên ngoài.

Nếu một thiết bị như vậy có thể hoạt động mà không cần cung cấp công ($|W| = 0$), thì hệ số hiệu năng $K = |Q_C|/|W|$ của nó sẽ tiến tới vô cùng lớn. Chúng ta gọi thiết bị giả định đó là **máy làm lạnh không tốn công** (workless refrigerator). Đây hoàn toàn là một khái niệm không tưởng, một "sinh vật thần thoại" tương tự như loài ngựa một sừng hay "bữa trưa miễn phí" trong thế giới vật lý thực tế.

::: info Câu hỏi kiểm tra hiểu biết 20.4
Bạn có thể làm mát ngôi nhà của mình bằng cách mở toang cửa tủ lạnh không?

<details>
<summary>Xem lời giải thích</summary>

**Đáp án đúng**: Không thể làm mát được nhà.

**Giải thích chi tiết**:

Máy làm lạnh sử dụng năng lượng công cơ học đầu vào để vận chuyển nhiệt từ một hệ này (bên trong buồng tủ lạnh) sang một hệ khác (bên ngoài tủ lạnh, chính là căn phòng nơi đặt chiếc tủ).

Nếu cửa tủ lạnh bị mở toang, hai không gian này hòa làm một và trở thành cùng một hệ nhiệt động duy nhất. Khi đó, hệ sẽ tiến tới cùng một nhiệt độ cân bằng. Theo nguyên lý thứ nhất của nhiệt động lực học, toàn bộ năng lượng công cơ học cấp cho động cơ điện của máy nén sẽ chuyển hóa hoàn toàn thành nhiệt lượng tỏa vào phòng. Do đó, nhiệt độ trong ngôi nhà thực tế sẽ tăng lên chứ không thể giảm đi.

Để làm mát được căn nhà, bạn bắt buộc phải sử dụng một hệ thống có khả năng vận chuyển nhiệt và nhả nhiệt lượng đó ra môi trường bên ngoài ngôi nhà, chẳng hạn như máy điều hòa không khí hoặc bơm nhiệt.
</details>
:::
