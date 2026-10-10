<!-- Nguồn: mục 1.7, trang in 10–14, trang PDF 30–34; gồm ứng dụng, Hình 1.9–1.16, Ví dụ 1.5, câu hỏi và đáp án. -->

## 1.7. Vector và phép cộng vector

Một số đại lượng vật lý như thời gian, nhiệt độ, khối lượng và khối lượng riêng được mô tả đầy đủ bằng một con số cùng đơn vị. Tuy nhiên, nhiều đại lượng khác còn có hướng nên một con số chưa đủ để mô tả.

Chuyển động của máy bay là một ví dụ. Ta phải biết máy bay đi nhanh bao nhiêu và theo hướng nào. Tốc độ kết hợp với hướng chuyển động tạo thành đại lượng gọi là **vận tốc**. Một ví dụ khác là **lực**, tức sự đẩy hoặc kéo tác dụng lên vật. Mô tả đầy đủ lực cần nêu cả mức độ mạnh yếu lẫn hướng đẩy hoặc kéo.

Đại lượng được mô tả bằng một con số được gọi là **đại lượng vô hướng**. Ngược lại, **đại lượng vector** có cả độ lớn và hướng trong không gian. Những phép tính kết hợp đại lượng vô hướng dùng số học thông thường, chẳng hạn $6\,\mathrm{kg}+3\,\mathrm{kg}=9\,\mathrm{kg}$ hoặc $4\times2\,\mathrm s=8\,\mathrm s$. Kết hợp các vector cần những phép toán riêng.

### Ứng dụng — Nhiệt độ vô hướng, vận tốc gió có hướng

![Ảnh trong ô ứng dụng của sách: Người di chuyển ngoài trời trong thời tiết mùa đông](img/young-01/ung-dung-nhiet-do-gio.png)

Mức dễ chịu của một ngày mùa đông phụ thuộc nhiệt độ, một đại lượng vô hướng có thể dương hoặc âm, chẳng hạn $+5^\circ\mathrm C$ hoặc $-20^\circ\mathrm C$, nhưng không có hướng. Nó cũng phụ thuộc vận tốc gió, một đại lượng vector có cả độ lớn lẫn hướng, chẳng hạn gió $15\,\mathrm{km/h}$ thổi từ phía tây.

### Độ dời và cách biểu diễn vector

Để hiểu vector và cách kết hợp chúng, ta bắt đầu với **độ dời**, tức sự thay đổi vị trí của vật. Độ dời là vector vì phải cho biết vật dịch chuyển bao xa và theo hướng nào. Đi bộ $3\,\mathrm{km}$ về phía bắc từ cửa nhà không đưa bạn tới cùng vị trí như đi $3\,\mathrm{km}$ về phía đông nam. Hai độ dời có cùng độ lớn nhưng khác hướng.

Sách biểu diễn vector bằng chữ đậm nghiêng có mũi tên phía trên. Trong bản dịch, ký hiệu vector như $\vec A$ giữ mũi tên để phân biệt với độ lớn $A$. Khi viết tay, cũng cần ghi mũi tên. Nếu ký hiệu không phân biệt vô hướng với vector, việc suy nghĩ và tính toán dễ lẫn hai loại đại lượng.

Một vector được vẽ bằng đoạn thẳng có đầu mũi tên. Chiều dài đoạn biểu thị độ lớn, còn mũi tên biểu thị hướng. Độ dời luôn là đoạn thẳng có hướng từ điểm đầu đến điểm cuối, dù đường đi thực tế có thể cong. Vì vậy độ dời không liên hệ trực tiếp với tổng quãng đường đi được. Nếu vật đi từ $P_1$ qua $P_2$ rồi trở về $P_1$, độ dời tổng bằng không.

![Hình 1.9 nguyên tác: Độ dời thẳng, quỹ đạo cong và hành trình khép kín](img/young-01/hinh-1-9.png)

**Hình 1.9:** (a) Độ dời được biểu diễn bằng mũi tên theo hướng dịch chuyển. Các nhãn chỉ vị trí đầu $P_1$, vị trí cuối $P_2$ và độ dời $\vec A$; hình cũng cho cách viết tay vector. (b) Mũi tên độ dời nối thẳng vị trí đầu với cuối, không phụ thuộc đường đi, kể cả khi đường ấy cong. (c) Độ dời tổng của hành trình đi rồi trở về bằng không, bất kể đường đi và quãng đường.

Hai vector có cùng hướng được gọi là **cùng hướng**. Nếu chúng vừa có cùng độ lớn vừa có cùng hướng, chúng bằng nhau dù được đặt ở những vị trí khác nhau trong không gian. Trong Hình 1.10, $\vec A'$ từ $P_3$ đến $P_4$ có cùng chiều dài và hướng với $\vec A$ từ $P_1$ đến $P_2$, nên $\vec A'=\vec A$. Hai vector chỉ bằng nhau khi thỏa cả hai điều kiện này.

Vector $\vec B$ trong hình không bằng $\vec A$ vì ngược hướng. **Vector đối** của một vector có cùng độ lớn nhưng ngược hướng, ký hiệu $-\vec A$. Nếu $\vec A$ là độ dời $87\,\mathrm m$ về phía nam thì $-\vec A$ là $87\,\mathrm m$ về phía bắc. Vì vậy $\vec B=-\vec A$, hay $\vec A=-\vec B$. Hai vector ngược hướng được gọi là ngược hướng dù độ lớn có bằng nhau hay không.

![Hình 1.10 nguyên tác: Hai độ dời bằng nhau và một độ dời đối](img/young-01/hinh-1-10.png)

**Hình 1.10:** $\vec A$ và $\vec A'$ bằng nhau vì cùng chiều dài và hướng. $\vec B$ có cùng độ lớn nhưng ngược hướng với $\vec A$, nên là vector đối của $\vec A$.

Độ lớn thường được viết bằng cùng chữ cái nhưng không có mũi tên. Nếu $\vec A$ là $87\,\mathrm m$ về phía nam thì $A=87\,\mathrm m$. Cũng có thể viết:

$$A=|\vec A|.\tag{1.1}$$

Độ lớn là một đại lượng vô hướng, không âm. Một vector không thể bằng một số vô hướng vì chúng là hai loại đối tượng khác nhau. Viết $\vec A=6\,\mathrm m$ mà không có thông tin hướng là sai kiểu đại lượng, giống như đặt “hai quả cam” bằng “ba quả táo”.

Khi vẽ, nên dùng một tỷ lệ thống nhất như trên bản đồ. Chẳng hạn, độ dời $5\,\mathrm{km}$ có thể được biểu diễn bằng mũi tên dài $1\,\mathrm{cm}$, còn $10\,\mathrm{km}$ bằng mũi tên dài $2\,\mathrm{cm}$.

### Cộng và trừ vector

Giả sử chất điểm có độ dời $\vec A$, sau đó có độ dời $\vec B$. Kết quả cuối giống như nó thực hiện một độ dời duy nhất $\vec C$ từ cùng điểm đầu tới điểm cuối. Ta gọi $\vec C$ là **tổng vector**, hay vector kết quả:

$$\vec C=\vec A+\vec B.\tag{1.2}$$

Đây là phép cộng theo hình học, không phải chỉ cộng hai số như $2+3=5$. Khi dựng tổng, đặt đuôi của vector thứ hai tại đầu mũi tên của vector thứ nhất. Vector tổng đi từ đuôi vector đầu tới đầu vector cuối.

Nếu thực hiện $\vec B$ trước rồi mới $\vec A$, kết quả vẫn như cũ:

$$
\vec C=\vec B+\vec A,
\qquad\vec A+\vec B=\vec B+\vec A.
\tag{1.3}
$$

Như vậy phép cộng vector có **tính giao hoán**. Một cách dựng tương đương là đặt hai vector chung đuôi, dựng hình bình hành có chúng làm hai cạnh kề. Đường chéo đi từ đuôi chung là vector tổng.

![Hình 1.11 nguyên tác: Hai cách ghép nối tiếp và cách dựng hình bình hành để cộng vector](img/young-01/hinh-1-11.png)

**Hình 1.11:** (a) Ghép đuôi $\vec B$ vào đầu $\vec A$, tổng nối từ đuôi $\vec A$ tới đầu $\vec B$. (b) Đổi thứ tự cho cùng kết quả. (c) Đặt chung đuôi và dùng đường chéo hình bình hành.

::: warning Độ lớn của tổng vector
Từ $\vec C=\vec A+\vec B$ không được suy ra $C=A+B$ trong mọi trường hợp. Độ lớn tổng còn phụ thuộc góc giữa hai vector. Chỉ khi hai vector cùng hướng, độ lớn tổng mới bằng tổng hai độ lớn. Khi ngược hướng, độ lớn tổng bằng $|A-B|$. Phân biệt vector với vô hướng sẽ tránh được cách cộng sai này.
:::

![Hình 1.12 nguyên tác: Cộng hai vector cùng hướng hoặc ngược hướng](img/young-01/hinh-1-12.png)

**Hình 1.12:** (a) Cùng hướng cho $C=A+B$. (b) Ngược hướng cho $C=|A-B|$.

Với ba vector, có thể cộng $\vec A$ với $\vec B$ trước để được $\vec D$, rồi cộng $\vec C$:

$$\vec R=(\vec A+\vec B)+\vec C=\vec D+\vec C.$$

Cũng có thể cộng $\vec B$ với $\vec C$ trước để được $\vec E$, rồi cộng $\vec A$:

$$\vec R=\vec A+(\vec B+\vec C)=\vec A+\vec E.$$

Thậm chí không cần dựng riêng $\vec D$ hay $\vec E$. Chỉ cần ghép lần lượt đuôi mỗi vector vào đầu vector trước. Vector tổng nối đuôi đầu tiên với đầu cuối cùng. Thứ tự có thể thay đổi mà kết quả không đổi. Phép cộng vector có **tính kết hợp**.

![Hình 1.13 nguyên tác: Các cách nhóm và đổi thứ tự khi cộng ba vector](img/young-01/hinh-1-13.png)

**Hình 1.13:** (a) Ba vector ban đầu. (b) Cộng $\vec A+\vec B$ rồi thêm $\vec C$. (c) Cộng $\vec B+\vec C$ rồi thêm $\vec A$. (d) Ghép trực tiếp cả ba vector. (e) Đổi thứ tự ghép vẫn thu được $\vec R$.

Ta định nghĩa hiệu hai vector bằng tổng với vector đối:

$$\vec A-\vec B=\vec A+(-\vec B).\tag{1.4}$$

![Hình 1.14 nguyên tác: Dựng hiệu vector bằng vector đối hoặc đặt hai vector chung đầu](img/young-01/hinh-1-14.png)

**Hình 1.14:** Trừ $\vec B$ khỏi $\vec A$ tương đương cộng $-\vec B$ vào $\vec A$. Khi ghép đuôi $-\vec B$ vào đầu $\vec A$, hiệu nối đuôi $\vec A$ tới đầu $-\vec B$. Khi đặt $\vec A$ và $\vec B$ chung đầu, hiệu đi từ đuôi $\vec A$ tới đuôi $\vec B$.

### Nhân vector với một đại lượng vô hướng

Độ dời $2\vec A$ có cùng hướng nhưng dài gấp đôi $\vec A$, tương đương cộng $\vec A$ với chính nó. Tổng quát, với số vô hướng $c$, vector $c\vec A$ có độ lớn $|c|A$. Nếu $c>0$, hướng giữ nguyên; nếu $c<0$, hướng đảo lại. Vì vậy $3\vec A$ cùng hướng với $\vec A$, còn $-3\vec A$ ngược hướng và có độ lớn gấp ba.

![Hình 1.15 nguyên tác: Nhân vector với số dương hoặc số âm](img/young-01/hinh-1-15.png)

**Hình 1.15:** (a) Nhân với số dương thay đổi chiều dài nhưng giữ hướng: $2\vec A$ dài gấp đôi. (b) Nhân với số âm vừa thay đổi chiều dài vừa đảo hướng: $-3\vec A$ dài gấp ba và ngược hướng.

Số vô hướng đem nhân cũng có thể là một đại lượng vật lý. Chẳng hạn, trong $\vec F=m\vec a$, hợp lực là tích của khối lượng vô hướng với gia tốc vector. Vì khối lượng dương, lực và gia tốc cùng hướng. Độ lớn lực bằng khối lượng nhân độ lớn gia tốc; đơn vị lực bằng đơn vị khối lượng nhân đơn vị gia tốc.

### Ví dụ 1.5 — Cộng hai vector vuông góc

::: exercise Đề bài trong sách
Một người trượt tuyết băng đồng đi $1.00\,\mathrm{km}$ về phía bắc, rồi $2.00\,\mathrm{km}$ về phía đông trên bãi tuyết ngang. Người ấy cách điểm xuất phát bao xa và theo hướng nào?
:::

::: solution Lời giải của sách
**Xác định và thiết lập.** Cần cộng hai độ dời vuông góc, tương đương giải một tam giác vuông bằng định lý Pythagoras và lượng giác. Đại lượng cần tìm là khoảng cách theo đường thẳng cùng hướng từ điểm đầu đến điểm cuối. Hình 1.16 được vẽ theo tỷ lệ, dùng góc $\varphi$ để biểu diễn hướng. Từ hình, ước lượng độ dời hơi lớn hơn $2\,\mathrm{km}$ và góc khoảng $63^\circ$.

**Thực hiện.** Khoảng cách là cạnh huyền:

$$
\sqrt{(1.00\,\mathrm{km})^2+(2.00\,\mathrm{km})^2}
\approx2.24\,\mathrm{km}.
$$

Theo định nghĩa tang:

$$
\tan\varphi
=\frac{\text{cạnh đối}}{\text{cạnh kề}}
=\frac{2.00\,\mathrm{km}}{1.00\,\mathrm{km}}
=2.00.
$$

Do đó $\varphi=\arctan2.00\approx63.4^\circ$. Hướng có thể được mô tả là lệch $63.4^\circ$ về phía đông so với hướng bắc, hoặc lệch $90^\circ-63.4^\circ=26.6^\circ$ về phía bắc so với hướng đông.

**Đánh giá.** Khoảng cách $2.24\,\mathrm{km}$ và góc $63.4^\circ$ gần các giá trị đã ước lượng. Mục 1.8 sẽ trình bày cách cộng thuận tiện khi hai vector không vuông góc.

**Ý chính của ví dụ:** Khi cộng vector, hãy vẽ các vector thành phần và vector tổng, thuận tiện nhất là ghép đuôi vào đầu như Hình 1.11a,b. Hình giúp nhận ra hướng vector tổng. Vẽ hình cũng cần thiết khi trừ vector, như Hình 1.14.
:::

![Hình 1.16 nguyên tác: Hành trình trượt tuyết gồm hai độ dời vuông góc và vector tổng](img/young-01/hinh-1-16.png)

**Hình 1.16:** Sơ đồ theo tỷ lệ có độ dời $1.00\,\mathrm{km}$ về bắc và $2.00\,\mathrm{km}$ về đông, vector độ dời kết quả cùng góc $\varphi$. Thước tỷ lệ đánh dấu $0$, $1$ và $2\,\mathrm{km}$; hoa gió chỉ bắc, đông, nam, tây.

### Câu hỏi kiểm tra hiểu mục 1.7

::: exercise Câu hỏi trong sách
Hai vector độ dời $\vec S$, $\vec T$ có độ lớn $S=3\,\mathrm m$, $T=4\,\mathrm m$. Những giá trị nào sau đây có thể là độ lớn của $\vec S-\vec T$? Có thể có nhiều đáp án đúng.

(i) $9\,\mathrm m$; (ii) $7\,\mathrm m$; (iii) $5\,\mathrm m$; (iv) $1\,\mathrm m$; (v) $0\,\mathrm m$; (vi) $-1\,\mathrm m$.
:::

::: solution Đáp án của sách
Chọn **(ii), (iii), (iv)**. Vì $-\vec T$ có cùng độ lớn với $\vec T$, hiệu $\vec S-\vec T=\vec S+(-\vec T)$ là tổng của hai vector độ lớn $3$ và $4\,\mathrm m$.

Nếu $\vec S$ và $-\vec T$ cùng hướng, tổng có độ lớn $7\,\mathrm m$. Nếu chúng ngược hướng, tổng có độ lớn $1\,\mathrm m$. Nếu vuông góc, tổng có độ lớn $5\,\mathrm m$, tạo tam giác vuông $3$–$4$–$5$.

Phương án (i) không thể vì độ lớn tổng không vượt tổng các độ lớn. Phương án (v) không thể vì tổng chỉ bằng không khi hai vector ngược hướng và bằng độ lớn. Phương án (vi) không thể vì độ lớn không âm.
:::
