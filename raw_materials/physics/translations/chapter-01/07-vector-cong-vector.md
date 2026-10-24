## 1.7. Vector và phép cộng vector

Một số đại lượng vật lý như thời gian, nhiệt độ, khối lượng và khối lượng riêng được mô tả đầy đủ bằng một con số cùng đơn vị tương ứng. Tuy nhiên, nhiều đại lượng vật lý quan trọng khác còn có hướng trong không gian, do đó một con số đơn lẻ chưa đủ để mô tả trọn vẹn.

Chuyển động của máy bay là một ví dụ điển hình: Ta phải biết máy bay đang bay nhanh bao nhiêu và bay theo hướng nào. Tốc độ kết hợp với hướng chuyển động tạo thành đại lượng gọi là **vận tốc**. Một ví dụ khác là **lực**, tức tác dụng đẩy hoặc kéo lên một vật. Mô tả đầy đủ một lực đòi hỏi phải nêu rõ cả độ lớn (mức độ mạnh yếu) lẫn hướng của lực đẩy hoặc kéo.

Đại lượng được mô tả đầy đủ chỉ bằng một giá trị số kèm đơn vị được gọi là **đại lượng vô hướng**. Ngược lại, **đại lượng vector** có cả độ lớn và hướng trong không gian. Những phép tính kết hợp các đại lượng vô hướng tuân theo quy tắc số học thông thường, chẳng hạn $6\,\mathrm{kg}+3\,\mathrm{kg}=9\,\mathrm{kg}$ hoặc $4\times(2\,\mathrm s)=8\,\mathrm s$. Việc kết hợp các đại lượng vector đòi hỏi các quy tắc toán học hình học và giải tích chuyên biệt.

### Ứng dụng: Nhiệt độ vô hướng và vận tốc gió vector

![Ứng dụng: Nhiệt độ là đại lượng vô hướng, vận tốc gió là đại lượng vector. Hình ứng dụng: Nhiệt độ là đại lượng vô hướng, vận tốc gió là đại lượng vector](/vat-ly-1/bai-giang/img/young-01/ung-dung-nhiet-do-gio.png)

Mức độ thoải mái của con người trong một ngày mùa đông phụ thuộc vào hai yếu tố: Nhiệt độ không khí, vốn là đại lượng vô hướng có thể mang dấu dương hoặc âm (chẳng hạn $+5^\circ\mathrm C$ hoặc $-20^\circ\mathrm C$) nhưng hoàn toàn không có hướng. Yếu tố còn lại là vận tốc gió, vốn là đại lượng vector có cả độ lớn (tốc độ gió $15\,\mathrm{km/h}$) lẫn hướng gió thổi (thổi từ phía tây sang đông).

### Độ dời và cách biểu diễn vector

Để nắm vững bản chất của vector và cách kết hợp chúng, ta bắt đầu bằng khái niệm **độ dời**, tức sự thay đổi vị trí của một chất điểm trong không gian. Độ dời là đại lượng vector vì nó xác định rõ vật dịch chuyển một khoảng bao xa và theo hướng nào. Việc đi bộ $3\,\mathrm{km}$ về phía bắc từ nhà sẽ đưa bạn đến một địa điểm hoàn toàn khác so với việc đi bộ $3\,\mathrm{km}$ về phía đông nam. Hai độ dời này có cùng độ lớn nhưng mang hướng khác nhau.

Trong bài giảng này, ta biểu diễn vector bằng ký hiệu có mũi tên phía trên như $\vec A$ để phân biệt với độ lớn vô hướng $A$. Khi viết tay trên giấy hoặc bảng, người học cũng bắt buộc phải vẽ mũi tên trên đầu ký hiệu vector. Nếu không phân biệt rõ ràng giữa đại lượng vô hướng và vector, quá trình tư duy và tính toán rất dễ dẫn đến sai lầm nghiêm trọng.

Về mặt hình học, một vector được biểu diễn bằng một đoạn thẳng có hướng (mũi tên). Chiều dài của đoạn thẳng theo một tỷ lệ xích xác định biểu thị độ lớn của vector, còn mũi tên chỉ rõ hướng của vector. Độ dời luôn là một đoạn thẳng nối thẳng từ vị trí ban đầu đến vị trí kết thúc, bất kể quỹ đạo chuyển động thực tế của vật có thể là đường cong phức tạp. Do đó, độ dời không đồng nhất với quãng đường đi được. Nếu một chất điểm đi từ điểm $P_1$ qua $P_2$ rồi quay trở lại đúng điểm $P_1$, tổng độ dời của cả hành trình khép kín bằng không.

![Hình 1.9: Độ dời thẳng, quỹ đạo cong và hành trình khép kín. Độ dời là đại lượng vector nối từ vị trí đầu đến vị trí cuối](/vat-ly-1/bai-giang/img/young-01/hinh-1-9.png)

- **(a) Biểu diễn độ dời**: Đoạn thẳng có hướng nối từ vị trí ban đầu $P_1$ đến vị trí cuối $P_2$. Độ dời được ký hiệu là $\vec A$.
- **(b) Độc lập với quỹ đạo**: Độ dời chỉ phụ thuộc vào vị trí đầu và cuối, hoàn toàn không phụ thuộc vào hình dạng đường đi thực tế.
- **(c) Hành trình khép kín**: Tổng độ dời của một hành trình khép kín đi rồi trở về đúng điểm xuất phát luôn bằng không, dù tổng quãng đường đi được rất lớn.

Hai vector có cùng hướng được gọi là **cùng hướng**. Nếu hai vector vừa có cùng độ lớn vừa có cùng hướng, chúng được định nghĩa là **hai vector bằng nhau**, bất kể vị trí điểm đặt của chúng ở đâu trong không gian. Trong Hình 1.10, vector $\vec A'$ từ $P_3$ đến $P_4$ có cùng chiều dài và song song cùng chiều với vector $\vec A$ từ $P_1$ đến $P_2$, do đó $\vec A' = \vec A$. Hai vector chỉ bằng nhau khi thỏa mãn đồng thời cả hai tiêu chuẩn về độ lớn và hướng.

Vector $\vec B$ trong hình không bằng $\vec A$ vì có hướng ngược lại. **Vector đối** của một vector là vector có cùng độ lớn nhưng ngược hướng, ký hiệu là $-\vec A$. Chẳng hạn, nếu $\vec A$ biểu diễn độ dời $87\,\mathrm m$ về phía nam thì $-\vec A$ là độ dời $87\,\mathrm m$ về phía bắc. Do đó $\vec B = -\vec A$, hay tương đương $\vec A = -\vec B$.

![Hình 1.10: Hai độ dời bằng nhau và một độ dời đối. Hai vector bằng nhau và vector đối](/vat-ly-1/bai-giang/img/young-01/hinh-1-10.png)

Theo ký hiệu (1.1), độ lớn của một vector được viết bằng cùng chữ cái nhưng không có mũi tên ở trên, hoặc dùng dấu giá trị tuyệt đối:

$$
A = \|\vec A\|.
$$

Độ lớn của vector luôn là một đại lượng vô hướng không âm ($A \ge 0$). Một vector không bao giờ có thể bằng một số vô hướng đơn thuần. Viết $\vec A = 6\,\mathrm m$ mà không kèm thông tin về hướng là sai bản chất toán học, tương tự như việc đồng nhất hai đối tượng không cùng thứ nguyên.

### Phép cộng và trừ vector theo phương pháp hình học

Xét một chất điểm thực hiện độ dời $\vec A$, tiếp theo sau đó thực hiện độ dời $\vec B$. Kết quả tổng hợp cuối cùng tương đương với việc chất điểm thực hiện một độ dời duy nhất $\vec C$ đi thẳng từ điểm bắt đầu của $\vec A$ đến điểm kết thúc của $\vec B$. Ta gọi $\vec C$ là **vector tổng**, hay vector hợp, và viết hệ thức (1.2):

$$
\vec C = \vec A + \vec B.
$$

Đây là phép cộng hình học vector, hoàn toàn khác với phép cộng đại số thông thường giữa hai con số. Quy tắc dựng hình: Đặt gốc (đuôi) của vector thứ hai $\vec B$ trùng với ngọn (đầu) của vector thứ nhất $\vec A$. Vector tổng $\vec C$ được nối từ gốc của vector thứ nhất $\vec A$ đến ngọn của vector thứ hai $\vec B$.

Nếu ta cho chất điểm thực hiện độ dời $\vec B$ trước rồi mới đến độ dời $\vec A$, kết quả vị trí cuối cùng vẫn không thay đổi, cho hệ thức (1.3):

$$
\begin{aligned}
\vec C &= \vec B + \vec A, \\
\vec A + \vec B &= \vec B + \vec A.
\end{aligned}
$$

Như vậy, phép cộng vector có **tính chất giao hoán**. Một phương pháp dựng hình tương đương là **quy tắc hình bình hành**: Đặt hai vector $\vec A$ và $\vec B$ có chung điểm gốc, sau đó dựng hình bình hành nhận hai vector này làm hai cạnh kề. Đường chéo xuất phát từ gốc chung chính là vector tổng $\vec C$.

![Hình 1.11: Các phương pháp hình học để cộng hai vector. Phép cộng hai vector theo quy tắc nối tiếp và quy tắc hình bình hành](/vat-ly-1/bai-giang/img/young-01/hinh-1-11.png)

- **(a) Quy tắc nối đuôi vào đầu**: Đặt đuôi $\vec B$ tại đầu $\vec A$, vector tổng nối từ đuôi $\vec A$ đến đầu $\vec B$.
- **(b) Tính giao hoán**: Đổi thứ tự thực hiện $\vec B + \vec A$ vẫn cho cùng một vector tổng $\vec C$.
- **(c) Quy tắc hình bình hành**: Đặt chung đuôi và lấy đường chéo hình bình hành.

::: warning Độ lớn của vector tổng
Từ hệ thức vector $\vec C = \vec A + \vec B$, ta tuyệt đối **không được suy ra** đẳng thức độ lớn $C = A + B$. Độ lớn của vector tổng phụ thuộc căn bản vào góc hợp bởi hai vector:
- Chỉ khi hai vector cùng phương, cùng chiều thì độ lớn tổng mới bằng $C = A + B$.
- Khi hai vector cùng phương, ngược chiều thì độ lớn tổng bằng $C = |A - B|$.
- Trong trường hợp tổng quát, độ lớn thỏa mãn bất đẳng thức tam giác: $|A - B| \le C \le A + B$.
:::

![Hình 1.12: Cộng hai vector cùng hướng hoặc ngược hướng. Cộng hai vector cùng phương](/vat-ly-1/bai-giang/img/young-01/hinh-1-12.png)

- **(a) Hai vector cùng hướng**: $C = A + B$.
- **(b) Hai vector ngược hướng**: $C = |A - B|$.

Khi cần cộng ba vector trở lên, ta có thể cộng hai vector đầu tiên $\vec A + \vec B$ để được vector trung gian $\vec D$, sau đó cộng tiếp với $\vec C$:

$$
\vec R = (\vec A + \vec B) + \vec C = \vec D + \vec C.
$$

Ta cũng có thể nhóm $\vec B + \vec C$ trước thành $\vec E$, rồi cộng với $\vec A$:

$$
\vec R = \vec A + (\vec B + \vec C) = \vec A + \vec E.
$$

Trên thực tế, ta chỉ cần đặt đuôi của vector sau nối tiếp vào đầu của vector trước thành một đa giác vector liên tục. Vector tổng cuối cùng $\vec R$ sẽ nối từ gốc đầu tiên đến ngọn cuối cùng. Phép cộng vector có **tính chất kết hợp**:

$$
\begin{aligned}
\vec R &= (\vec A + \vec B) + \vec C \\
&= \vec A + (\vec B + \vec C).
\end{aligned}
$$

![Hình 1.13: Tính chất kết hợp của phép cộng nhiều vector. Tính kết hợp khi cộng ba vector](/vat-ly-1/bai-giang/img/young-01/hinh-1-13.png)

**Phép trừ vector** được định nghĩa qua phép cộng với vector đối, theo hệ thức (1.4):

$$
\vec A - \vec B = \vec A + (-\vec B).
$$

![Hình 1.14: Dựng hiệu hai vector bằng vector đối](/vat-ly-1/bai-giang/img/young-01/hinh-1-14.png)

Muốn trừ $\vec B$ khỏi $\vec A$, ta lấy vector đối $-\vec B$ rồi cộng vào $\vec A$ theo quy tắc nối tiếp. Với hai vector đặt chung ngọn như Hình 1.14, hiệu hướng từ đuôi $\vec A$ đến đuôi $\vec B$. Hoặc nếu đặt $\vec A$ và $\vec B$ chung gốc, vector hiệu $\vec A - \vec B$ sẽ là vector hướng từ ngọn của $\vec B$ sang ngọn của $\vec A$.

### Phép nhân vector với một số vô hướng

Độ dời $2\vec A$ là một vector có cùng hướng với $\vec A$ nhưng có chiều dài gấp đôi, tương đương với tổng $\vec A + \vec A$. Một cách tổng quát: Khi nhân một vector $\vec A$ với một số vô hướng $c$, ta thu được một vector mới $c\vec A$ có độ lớn bằng $|c|A$:
- Nếu $c > 0$: Vector tích $c\vec A$ có cùng hướng với $\vec A$.
- Nếu $c < 0$: Vector tích $c\vec A$ có hướng ngược lại với $\vec A$.

![Hình 1.15: Nhân vector với số vô hướng dương và âm](/vat-ly-1/bai-giang/img/young-01/hinh-1-15.png)

Số vô hướng đem nhân cũng có thể là một đại lượng vật lý mang đơn vị. Ví dụ: Trong định luật II Newton $\vec F=m\vec a$, hợp lực $\vec F$ là tích của khối lượng vô hướng $m$ với gia tốc vector $\vec a$. Vì khối lượng luôn dương ($m > 0$), vector lực luôn cùng hướng với vector gia tốc khi gia tốc khác không. Độ lớn của lực bằng khối lượng nhân với độ lớn gia tốc ($F = ma$).

### Ví dụ 1.5: Cộng hai vector vuông góc

::: exercise Ví dụ 1.5: Cộng hai vector vuông góc
Một vận động viên trượt tuyết băng đồng di chuyển $1.00\,\mathrm{km}$ về phía bắc, sau đó tiếp tục di chuyển $2.00\,\mathrm{km}$ về phía đông trên một cánh đồng tuyết phẳng. Người ấy cách điểm xuất phát ban đầu một khoảng bao xa và theo hướng nào?
:::

::: solution Lời giải
**Tóm tắt đề bài**:
- Độ dời thứ nhất: $\vec A$ có độ lớn $A = 1.00\,\mathrm{km}$, hướng về phía bắc.
- Độ dời thứ hai: $\vec B$ có độ lớn $B = 2.00\,\mathrm{km}$, hướng về phía đông.
- Cần tìm: Độ lớn $R$ và góc định hướng $\varphi$ của vector độ dời tổng hợp $\vec R = \vec A + \vec B$.

**Hướng đi**:
- Vì hướng bắc và hướng đông vuông góc nhau, hai vector độ dời $\vec A$ và $\vec B$ tạo thành hai cạnh góc vuông của một tam giác vuông.
- Sử dụng định lý Pythagoras để tìm độ lớn cạnh huyền $R = \sqrt{A^2 + B^2}$.
- Sử dụng hàm lượng giác tang để xác định góc lệch $\varphi$ so với hướng bắc.

**Lời giải chi tiết**:
Bước 1. Tính độ lớn của vector độ dời tổng hợp:

$$
\begin{aligned}
R &= \sqrt{A^2 + B^2} \\
&= \sqrt{(1.00)^2 + (2.00)^2}\,\mathrm{km} \\
&= \sqrt{5.00}\,\mathrm{km} \\
&\approx 2.24\,\mathrm{km}.
\end{aligned}
$$

Bước 2. Xác định hướng của vector độ dời:
   Xét góc $\varphi$ là góc hợp bởi vector tổng $\vec R$ với hướng bắc:

$$
\begin{aligned}
\tan\varphi &= \frac{B}{A} \\
&= \frac{2.00\,\mathrm{km}}{1.00\,\mathrm{km}} \\
&= 2.00.
\end{aligned}
$$

Suy ra:

$$
\varphi = \arctan(2.00) \approx 63.4^\circ.
$$

Hướng của người trượt tuyết lệch $63.4^\circ$ về phía đông so với hướng bắc (hoặc tương đương lệch $90.0^\circ - 63.4^\circ = 26.6^\circ$ về phía bắc so với hướng đông).

**Đánh giá**:
Khoảng cách $2.24\,\mathrm{km}$ lớn hơn từng độ dời riêng rẽ nhưng nhỏ hơn tổng hai độ dời ($1.00\,\mathrm{km} + 2.00\,\mathrm{km}$ $= 3.00\,\mathrm{km}$), hoàn toàn phù hợp với bất đẳng thức tam giác. Góc $63.4^\circ$ lớn hơn $45^\circ$, phản ánh đúng thực tế là cạnh đối diện (hướng đông $2.00\,\mathrm{km}$) dài gấp đôi cạnh kề (hướng bắc $1.00\,\mathrm{km}$).
:::

![Hình 1.16: Sơ đồ vector cho chuyến trượt tuyết. Sơ đồ vector theo tỷ lệ xích cho hành trình trượt tuyết](/vat-ly-1/bai-giang/img/young-01/hinh-1-16.png)

### Câu hỏi tự kiểm tra hiểu bài 1.7

::: exercise Câu hỏi tự kiểm tra 1.7: Độ lớn của hiệu hai vector
Hai vector độ dời $\vec S$ và $\vec T$ có độ lớn lần lượt là $S = 3\,\mathrm m$ và $T = 4\,\mathrm m$. Những giá trị nào dưới đây có thể là độ lớn của vector hiệu $\vec S - \vec T$? (Có thể có nhiều hơn một đáp án đúng.)

- (i) $9\,\mathrm m$
- (ii) $7\,\mathrm m$
- (iii) $5\,\mathrm m$
- (iv) $1\,\mathrm m$
- (v) $0\,\mathrm m$
- (vi) $-1\,\mathrm m$.
:::

::: solution Lời giải chi tiết
Chọn các phương án **(ii) $7\,\mathrm m$**, **(iii) $5\,\mathrm m$**, và **(iv) $1\,\mathrm m$**.

**Giải thích**:
Hiệu hai vector được viết lại dưới dạng tổng với vector đối: $\vec S - \vec T = \vec S + (-\vec T)$.
Vì vector đối $-\vec T$ có cùng độ lớn với $\vec T$ ($\|-\vec T\| = T = 4\,\mathrm m$), độ lớn của vector hiệu bị chặn trong khoảng:

$$
|S - T| \le \|\vec S - \vec T\| \le S + T.
$$

Thay số: $|3 - 4|\,\mathrm m \le \|\vec S - \vec T\|$ $\le (3 + 4)\,\mathrm m$, hay:

$$
1\,\mathrm m \le \|\vec S - \vec T\| \le 7\,\mathrm m.
$$

- Khi $\vec S$ và $-\vec T$ cùng hướng (tức $\vec S$ và $\vec T$ ngược hướng), độ lớn đạt giá trị cực đại: $3\,\mathrm m + 4\,\mathrm m = 7\,\mathrm m$ $\implies$ Chọn (ii).
- Khi $\vec S$ và $-\vec T$ ngược hướng (tức $\vec S$ và $\vec T$ cùng hướng), độ lớn đạt giá trị cực tiểu: $|3\,\mathrm m - 4\,\mathrm m| = 1\,\mathrm m$ $\implies$ Chọn (iv).
- Khi $\vec S$ và $\vec T$ vuông góc nhau, độ lớn là cạnh huyền tam giác vuông: $\sqrt{3^2 + 4^2}\,\mathrm m = 5\,\mathrm m$ $\implies$ Chọn (iii).

Các phương án còn lại bị loại:
- Phương án (i) $9\,\mathrm m$ vượt quá giới hạn cực đại $7\,\mathrm m$.
- Phương án (v) $0\,\mathrm m$ không thể xảy ra vì hai vector có độ lớn khác nhau ($3\,\mathrm m \ne 4\,\mathrm m$).
- Phương án (vi) $-1\,\mathrm m$ loại vì độ lớn của một vector luôn là đại lượng không âm.
:::
