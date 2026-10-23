## 11.1 Các Điều Kiện Cân Bằng

Một vật thể được định nghĩa là ở trạng thái cân bằng khi nó chuyển động với vận tốc không đổi trong một hệ quy chiếu quán tính. Khái niệm này bao hàm cả trường hợp đặc biệt nhưng phổ biến nhất trong thực tế: Vật thể hoàn toàn đứng yên, không có vận tốc tịnh tiến và không có vận tốc quay. Trạng thái đứng yên bền vững này được gọi là **cân bằng tĩnh** (static equilibrium). Trọng tâm nghiên cứu của phần lớn nội dung trong chương này là khảo sát các cấu trúc kỹ thuật và vật thể ở trạng thái cân bằng tĩnh.

Mô hình hạt chất điểm trước đây chỉ cho phép xem xét chuyển động tịnh tiến. Đối với một vật thể thực có kích thước hữu hạn, các ngoại lực có thể tác dụng tại những vị trí hình học khác nhau. Do đó, một vật thể thực có thể vừa tịnh tiến vừa quay. Để đảm bảo vật thể ở trạng thái cân bằng tĩnh hoàn toàn, ta cần thiết lập các điều kiện vật lý chặt chẽ để triệt tiêu đồng thời cả xu hướng tịnh tiến lẫn xu hướng quay.

### Điều Kiện Thứ Nhất Cho Trạng Thái Cân Bằng

Từ định luật II Newton mở rộng cho hệ hạt và vật rắn, gia tốc khối tâm $\vec{a}_{\mathrm{cm}}$ của một vật có tổng khối lượng $M$ được xác định bởi tổng vectơ của các ngoại lực:

$$
\sum \vec{F} = M \vec{a}_{\mathrm{cm}}
$$

Nếu một vật ban đầu đang đứng yên mà muốn tiếp tục giữ nguyên trạng thái đứng yên, khối tâm của nó tuyệt đối không được phép xuất hiện gia tốc tịnh tiến. Nghĩa là $\vec{a}_{\mathrm{cm}} = \vec{0}$. Hệ quả tất yếu là tổng vectơ của tất cả các ngoại lực tác dụng lên vật phải triệt tiêu:

$$
\sum \vec{F} = \vec{0}
\tag{11.1}
$$

Phương trình vectơ (11.1) chính là **điều kiện thứ nhất cho trạng thái cân bằng**. Khi biểu diễn trong hệ tọa độ Descartes ba chiều, điều kiện này tương đương với ba phương trình đại số độc lập cho từng thành phần lực:

$$
\sum F_x = 0
$$

$$
\sum F_y = 0
$$

$$
\sum F_z = 0
$$

Trong đó, tổng đại số của các thành phần lực dọc theo mỗi trục tọa độ phải đồng thời triệt tiêu.

![](../img/young-11/a-hinh-11-01.png)

*Hình 11.1: Để ở trạng thái cân bằng tĩnh, vật đứng yên phải thỏa mãn đồng thời cả hai điều kiện cân bằng: Vật không có xu hướng gia tốc tịnh tiến và không có xu hướng bắt đầu quay.*

### Vì Sao Điều Kiện Thứ Nhất Chưa Đủ?

Quan sát ba tình huống cơ bản được minh họa trên Hình 11.1 để làm sáng tỏ vai trò độc lập của từng điều kiện cơ học:

- **Tình huống (a)**: Hai lực có cùng độ lớn $F$ tác dụng vào hai đầu một thanh phẳng nhưng ngược chiều và cùng nằm trên một đường thẳng tác dụng. Tổng hợp lực bằng không ($\sum \vec{F} = \vec{0}$) và tổng mômen lực quanh tâm cũng bằng không ($\sum \vec{\tau} = \vec{0}$). Thanh đứng yên cân bằng tĩnh hoàn hảo.
- **Tình huống (b)**: Hai lực có cùng độ lớn $F$ và ngược chiều nhau, thỏa mãn $\sum \vec{F} = \vec{0}$. Tuy nhiên, hai lực này không cùng nằm trên một đường thẳng mà cách nhau một cánh tay đòn nhất định (tạo thành một ngẫu lực). Khối tâm của vật không bị gia tốc tịnh tiến, nhưng cặp lực này sinh ra một mômen lực thuần túy khiến thanh bắt đầu quay nhanh dần theo chiều kim đồng hồ quanh trục vuông góc với mặt phẳng. Rõ ràng, dù thỏa mãn hoàn toàn điều kiện thứ nhất, vật vẫn không thể đạt trạng thái cân bằng tĩnh.
- **Tình huống (c)**: Hai lực cùng hướng lên trên với độ lớn $F$, đặt đối xứng qua tâm. Tổng mômen lực đối với trục quay đi qua tâm triệt tiêu ($\sum \tau_z = 0$), do đó thanh không có xu hướng bắt đầu quay. Thế nhưng tổng hợp lực lại mang giá trị $\sum F_y = 2F \ne 0$, khiến vật lập tức bị gia tốc tịnh tiến lên phía trên.

### Điều Kiện Thứ Hai Cho Trạng Thái Cân Bằng

Sự xuất hiện chuyển động quay có gia tốc trong tình huống (b) chứng minh rằng ta bắt buộc phải có một điều kiện thứ hai để ngăn chặn xu hướng quay của vật rắn.

Theo nguyên lý động lực học chuyển động quay quanh một trục cố định, gia tốc góc $\vec{\alpha}$ của vật rắn liên hệ trực tiếp với tổng mômen ngoại lực $\sum \vec{\tau}$ qua phương trình:

$$
\sum \vec{\tau} = I \vec{\alpha}
$$

Trong đó, $I$ là mômen quán tính của vật rắn đối với trục quay đang xét. Để một vật đang không quay tiếp tục duy trì trạng thái không quay ($\vec{\alpha} = \vec{0}$), tổng vectơ mômen lực tác dụng lên vật đối với một điểm bất kỳ phải bằng không:

$$
\sum \vec{\tau} = \vec{0}
\tag{11.2}
$$

Phương trình (11.2) là **điều kiện thứ hai cho trạng thái cân bằng**.

Khi xét các bài toán cơ học phẳng mà mọi lực đều nằm trong mặt phẳng $xy$, vectơ mômen lực $\vec{\tau} = \vec{r} \times \vec{F}$ của mỗi lực chỉ có thành phần dọc theo trục $z$ vuông góc với mặt phẳng hình vẽ. Khi ấy, điều kiện thứ hai rút gọn về một phương trình vô hướng đơn giản:

$$
\sum \tau_z = 0
$$

Quy ước chuẩn mực: Các mômen lực có xu hướng làm vật quay ngược chiều kim đồng hồ quanh trục mang giá trị dương, trong khi các mômen lực có xu hướng làm vật quay cùng chiều kim đồng hồ mang giá trị âm.

### Tính Độc Lập Của Điểm Quy Chiếu Tính Mômen Lực

Một câu hỏi tự nhiên xuất hiện: Điểm quy chiếu dùng để tính mômen lực trong phương trình (11.2) có cần phải là một trục quay vật lý cố định hay không? Câu trả lời là không. Điểm tính mômen lực có thể là bất kỳ điểm nào trong không gian, nằm trên vật thể hoặc hoàn toàn ở bên ngoài vật thể.

Ta chứng minh định lý toán học sau: Khi điều kiện thứ nhất đã được thỏa mãn ($\sum \vec{F} = \vec{0}$), thì tổng mômen lực $\sum \vec{\tau}$ có cùng một giá trị duy nhất đối với mọi điểm quy chiếu được chọn.

Xét hai điểm quy chiếu tùy ý $O$ và $O'$. Giả sử vị trí của điểm $O'$ đối với gốc $O$ được xác định bởi vectơ $\vec{R}$. Đối với một lực $\vec{F}_i$ đặt tại điểm có vectơ vị trí $\vec{r}_i$ so với $O$, vectơ vị trí của điểm đặt lực đó đối với $O'$ sẽ là:

$$
\vec{r}'_i = \vec{r}_i - \vec{R}
$$

Tổng mômen lực của toàn bộ hệ lực đối với điểm quy chiếu mới $O'$ được xác định bằng cách tính mômen của từng lực rồi lấy tổng:

$$
\vec{\tau}'_i = (\vec{r}_i - \vec{R}) \times \vec{F}_i
$$

Khai triển tích có hướng theo tính chất phân phối:

$$
\vec{\tau}'_i = (\vec{r}_i \times \vec{F}_i) - (\vec{R} \times \vec{F}_i)
$$

Lấy tổng cho toàn bộ các ngoại lực tác dụng lên vật, đặt hợp lực là $\vec{F}_{\mathrm{net}} = \sum \vec{F}$:

$$
\sum \vec{\tau}' = \sum \vec{\tau} - \vec{R} \times \vec{F}_{\mathrm{net}}
$$

Bởi vì hệ lực thỏa mãn điều kiện thứ nhất của trạng thái cân bằng nên $\sum \vec{F} = \vec{0}$. Do đó, số hạng thứ hai hoàn toàn triệt tiêu:

$$
\sum \vec{\tau}' = \sum \vec{\tau}
$$

Như vậy, nếu tổng mômen lực đối với một điểm nào đó bằng không thì nó cũng tự động bằng không đối với bất kỳ điểm nào khác. Tính chất này mang lại cho người giải bài toán một lợi thế chiến lược rất lớn: Ta có thể tự do lựa chọn điểm tính mômen lực tại chính vị trí đặt của một hoặc nhiều lực chưa biết, nhờ đó cánh tay đòn của các lực này bằng không và triệt tiêu được các ẩn số phức tạp khỏi phương trình mômen lực.

::: question Kiểm tra hiểu biết 11.1
Tình huống nào dưới đây thỏa mãn đồng thời cả điều kiện thứ nhất và điều kiện thứ hai cho trạng thái cân bằng?

- (a) Một máy bay đang bay theo đường thẳng ở độ cao không đổi và vận tốc không đổi.
- (b) Một chiếc gậy bóng chày đang vung với tốc độ quay không đổi.
- (c) Một vòng đu quay đang quay đều với tốc độ góc không đổi.
- (d) Không có tình huống nào trong số các tình huống trên.

<details>
<summary>Xem lời giải thích</summary>

**Đáp án chính xác**: (a).

**Giải thích chi tiết**:
Đối với máy bay đang bay theo đường thẳng với vận tốc không đổi và độ cao ổn định, gia tốc của máy bay bằng không ($\vec{a} = \vec{0}$). Do đó, tổng hợp lực tác dụng lên máy bay triệt tiêu hoàn toàn ($\sum \vec{F} = \vec{0}$), thỏa mãn điều kiện thứ nhất. Đồng thời máy bay không quay, gia tốc góc bằng không ($\vec{\alpha} = \vec{0}$), kéo theo tổng mômen lực triệt tiêu ($\sum \vec{\tau} = \vec{0}$), thỏa mãn điều kiện thứ hai.

Ngược lại, trong trường hợp chiếc gậy bóng chày đang vung ở câu (b) hoặc vòng đu quay ở câu (c), các phần tử vật chất trên vật đều đang chuyển động tròn có gia tốc hướng tâm ($\vec{a}_{\mathrm{rad}} \ne \vec{0}$). Khi khối tâm hoặc các phần tử có gia tốc khác không, tổng hợp lực tác dụng lên vật không thể triệt tiêu. Do đó, các trường hợp này không thỏa mãn điều kiện cân bằng tĩnh.

</details>
:::
