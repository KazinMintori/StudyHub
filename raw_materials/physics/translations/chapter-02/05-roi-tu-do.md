## 2.5. Vật rơi tự do

Khi thả một vật, điều gì quyết định cách nó rơi? Từ thời cổ đại, câu hỏi này đã thu hút các nhà tư tưởng và nhà khoa học. Vào thế kỷ IV trước Công nguyên, Aristotle cho rằng vật nặng rơi nhanh hơn vật nhẹ theo tỉ lệ trọng lượng. Mười chín thế kỷ sau, Galileo lập luận rằng gia tốc rơi hướng xuống là không đổi và không phụ thuộc trọng lượng.

Thí nghiệm cho thấy khi bỏ qua ảnh hưởng của không khí, các vật ở cùng một nơi rơi với cùng gia tốc hướng xuống, bất kể kích thước và trọng lượng. Nếu quãng rơi nhỏ so với bán kính Trái Đất và bỏ qua ảnh hưởng nhỏ của sự quay Trái Đất, ta có thể coi gia tốc không đổi.

Chuyển động lý tưởng dưới các giả thiết ấy gọi là **rơi tự do**. Tên gọi này bao gồm cả giai đoạn vật đi lên lẫn đi xuống, miễn là chỉ trọng lực tác dụng. Chương 3 mở rộng mô hình sang chuyển động ném có cả thành phần ngang và thành phần thẳng đứng.

![Hình 2.22: Ảnh hoạt nghiệm của quả bóng rơi tự do, ghi sau các khoảng thời gian bằng nhau](img/young-02/hinh-2-22.png)

Nguồn sáng hoạt nghiệm phát các chớp ngắn sau những khoảng thời gian bằng nhau. Mỗi chớp ghi lại vị trí bóng trên cùng bức ảnh. Khoảng cách giữa các ảnh tăng dần cho thấy bóng có gia tốc hướng xuống. Đo cẩn thận cho thấy vận tốc thay đổi những lượng bằng nhau trong các khoảng thời gian bằng nhau, tức gia tốc không đổi.

### Gia tốc trọng trường và quy ước dấu

Gia tốc rơi tự do gọi là gia tốc trọng trường. Ký hiệu g biểu thị độ lớn của vector gia tốc này. Gần mặt đất, thường dùng:

$$
g\approx9{,}80\,\mathrm{m/s^2}.
$$

Các cách biểu diễn tương đương gần đúng là:

$$
g\approx980\,\mathrm{cm/s^2},
$$

$$
g\approx32{,}2\,\mathrm{ft/s^2}.
$$

Giá trị chính xác thay đổi theo địa điểm, nên đôi khi chỉ giữ hai chữ số có nghĩa là 9,8 m/s². Trên bề mặt Mặt Trăng, gia tốc do lực hấp dẫn của Mặt Trăng có độ lớn khoảng 1,6 m/s². Gần bề mặt Mặt Trời, giá trị ấy khoảng 270 m/s².

::: warning g là độ lớn dương
Không gán dấu âm cho g. Nếu chọn chiều dương của trục y hướng lên, thành phần gia tốc mới mang dấu âm:

$$
a_y=-g.
$$

Nếu chọn chiều dương hướng xuống, thành phần gia tốc bằng +g. Dùng nhất quán chiều trục trong cả bài toán.
:::

Tốc độ không âm, còn thành phần vận tốc có thể dương, âm hoặc bằng không. Trong rơi tự do, vận tốc và tốc độ thay đổi nhưng gia tốc vẫn giữ nguyên hướng xuống. Các ví dụ sau dùng bốn phương trình ở Mục 2.4 với tọa độ x thay bằng y. Có thể đối chiếu phương pháp giải 2.1 trước khi tính.

### Ví dụ 2.6: Đồng xu rơi tự do

::: exercise Thả đồng xu từ tháp Pisa
Một đồng xu một euro được thả từ trạng thái nghỉ trên tháp nghiêng Pisa. Bỏ qua sức cản không khí. Tìm vị trí và vận tốc của đồng xu sau 1,0 s, 2,0 s và 3,0 s.
:::

![Hình 2.23: Sơ đồ vị trí và vận tốc của đồng xu thả từ trạng thái nghỉ](img/young-02/hinh-2-23.png)

::: solution Tọa độ và vận tốc tại ba thời điểm
Chọn gốc tại điểm thả và chiều dương hướng lên. Vị trí đầu và vận tốc đầu đều bằng không. Gia tốc hướng xuống nên $a_y$ = −g. Vì gia tốc không đổi, dùng phương trình tọa độ (2.12) và vận tốc (2.8).

$$
\begin{aligned}
y&=y_0+v_{0y}t+\frac12a_yt^2\\
&=-\frac12gt^2,
\end{aligned}
$$

$$
v_y=v_{0y}+a_yt=-gt.
$$

Với g = 9,8 m/s², tại t = 1,0 s:

$$
y=-4{,}9(1{,}0)^2\,\mathrm m=-4{,}9\,\mathrm m,
$$

$$
\begin{aligned}
v_y&=-9{,}8(1{,}0)\,\mathrm{m/s}\\
&=-9{,}8\,\mathrm{m/s}.
\end{aligned}
$$

Đồng xu nằm thấp hơn điểm thả 4,9 m và đi xuống với tốc độ 9,8 m/s. Làm tương tự ở hai thời điểm còn lại:

| Thời gian | Tọa độ trước khi làm tròn | Vận tốc trước khi làm tròn |
| --- | --- | --- |
| 2,0 s | −19,6 m | −19,6 m/s |
| 3,0 s | −44,1 m | −29,4 m/s |

Giữ hai chữ số có nghĩa cho kết quả ở 2,0 s là −20 m và −20 m/s. Ở 3,0 s, kết quả là −44 m và −29 m/s.

Các dấu âm phù hợp với chiều trục đã chọn. Nếu chọn chiều dương hướng xuống thì gia tốc, tọa độ và vận tốc trong ví dụ này đều dương. Vị trí và chuyển động thực của đồng xu không thay đổi theo cách chọn trục.
:::

### Ví dụ 2.7: Chuyển động đi lên và đi xuống

::: exercise Ném bóng từ mái nhà
Bạn ném một quả bóng thẳng đứng lên từ mái tòa nhà cao. Bóng rời tay ngang lan can với tốc độ hướng lên 15,0 m/s, sau đó rơi tự do. Khi đi xuống, bóng vừa tránh được lan can. Bỏ qua sức cản không khí.

(a) Tìm vị trí và vận tốc sau 1,00 s và 4,00 s. (b) Tìm vận tốc khi bóng ở cao hơn lan can 5,00 m. (c) Tìm độ cao cực đại. (d) Gia tốc của bóng tại độ cao cực đại bằng bao nhiêu?
:::

![Hình 2.24: Các vị trí cần xét của bóng ném thẳng đứng từ mái nhà](img/young-02/hinh-2-24.png)

::: solution Xét dấu vận tốc và vị trí
Chọn gốc tại điểm bóng rời tay, chiều dương hướng lên. Khi ấy $y_0$ = 0, $v_{0y}$ = +15,0 m/s và $a_y$ = −9,80 m/s². Câu (a) biết thời gian nên dùng (2.12) và (2.8). Câu (b) biết vị trí mà không biết thời gian nên dùng (2.13).

(a) Phương trình tọa độ và vận tốc là:

$$
y=v_{0y}t-\frac12gt^2,
$$

$$
v_y=v_{0y}-gt.
$$

Khi t đo bằng giây, biểu thức số theo đơn vị SI là:

$$
y=(15{,}0t-4{,}90t^2)\,\mathrm m,
$$

$$
v_y=(15{,}0-9{,}80t)\,\mathrm{m/s}.
$$

Tại t = 1,00 s:

$$
\begin{aligned}
y&=(15{,}0-4{,}90)\,\mathrm m\\
&=10{,}1\,\mathrm m,
\end{aligned}
$$

$$
\begin{aligned}
v_y&=(15{,}0-9{,}80)\,\mathrm{m/s}\\
&=5{,}20\,\mathrm{m/s}.
\end{aligned}
$$

Bóng cao hơn lan can 10,1 m và còn đi lên. Tốc độ nhỏ hơn lúc ném vì bóng chậm dần khi bay lên.

Tại t = 4,00 s, phần $v_{0y}$t bằng 60,0 m, còn phần gt²/2 bằng 78,4 m. Do đó:

$$
\begin{aligned}
y&=(60{,}0-78{,}4)\,\mathrm m\\
&=-18{,}4\,\mathrm m,
\end{aligned}
$$

$$
\begin{aligned}
v_y&=[15{,}0-9{,}80(4{,}00)]\,\mathrm{m/s}\\
&=-24{,}2\,\mathrm{m/s}.
\end{aligned}
$$

Bóng đã qua đỉnh, thấp hơn lan can 18,4 m và đang đi xuống với tốc độ 24,2 m/s.

(b) Hệ thức không chứa thời gian cho:

$$
v_y^2=v_{0y}^2-2g(y-y_0).
$$

Tại y = +5,00 m, bình phương vận tốc đầu bằng 225 m²/s², còn 2gy bằng 98,0 m²/s²:

$$
\begin{aligned}
v_y^2&=(225-98{,}0)\,\mathrm{m^2/s^2}\\
&=127\,\mathrm{m^2/s^2}.
\end{aligned}
$$

Hai nghiệm là:

$$
v_y=\pm11{,}3\,\mathrm{m/s}.
$$

Nghiệm dương ứng với lúc bóng đi lên, nghiệm âm ứng với lúc bóng đi xuống. Bóng qua cùng độ cao hai lần với cùng tốc độ 11,3 m/s.

(c) Tại độ cao cực đại $y_1$, vận tốc bằng không:

$$
0=v_{0y}^2-2gy_1.
$$

Suy ra:

$$
\begin{aligned}
y_1&=\frac{v_{0y}^2}{2g}\\
&=\frac{15{,}0^2}{2(9{,}80)}\,\mathrm m\\
&\approx11{,}5\,\mathrm m.
\end{aligned}
$$

(d) Gia tốc tại đỉnh vẫn là:

$$
a_y=-g=-9{,}80\,\mathrm{m/s^2}.
$$

Vận tốc bằng không tại một thời điểm không đồng nghĩa gia tốc bằng không. Vận tốc vẫn đang biến thiên từ dương sang âm. Nếu gia tốc tiếp tục bằng không sau khi bóng tới đỉnh, bóng sẽ đứng yên tại đó, trái với mô hình rơi tự do.

Để đối chiếu kết quả, dựng đồ thị tọa độ và vận tốc theo thời gian. Đồ thị tọa độ là parabol lõm xuống, còn đồ thị vận tốc là đường thẳng dốc xuống. Có thể dựng chúng từ các phương trình bằng công cụ vẽ đồ thị.
:::

![Hình 2.25: Đồ thị tọa độ và vận tốc của bóng ném lên với vận tốc đầu 15,0 m/s](img/young-02/hinh-2-25.png)

### Ví dụ 2.8: Hai nghiệm hay một nghiệm

::: exercise Thời điểm bóng ở dưới lan can
Sau khi rời tay, vào thời điểm nào quả bóng trong Ví dụ 2.7 ở thấp hơn lan can 5,00 m?
:::

::: solution Giải và xét ý nghĩa nghiệm
Dùng cùng trục tọa độ và điều kiện đầu như Ví dụ 2.7. Đại lượng cần tìm là thời gian ứng với y = −5,00 m. Phương trình tọa độ là bậc hai theo t:

$$
y=y_0+v_{0y}t-\frac12gt^2.
$$

Chuyển về dạng:

$$
\frac12gt^2-v_{0y}t+(y-y_0)=0.
$$

Đặt A = g/2, B = −$v_{0y}$ và C = y − $y_0$. Công thức nghiệm của phương trình bậc hai cho:

$$
t=\frac{-B\pm\sqrt{B^2-4AC}}{2A}.
$$

Thay các hệ số:

$$
t=\frac{v_{0y}\pm\sqrt{v_{0y}^2-2g(y-y_0)}}{g}.
$$

Để tính gọn mà giữ đầy đủ đơn vị, gọi biệt thức dưới căn là D:

$$
D=v_{0y}^2-2g(y-y_0).
$$

Với y = −5,00 m, giá trị của −2g(y − $y_0$) bằng +98,0 m²/s²:

$$
\begin{aligned}
D&=(225+98{,}0)\,\mathrm{m^2/s^2}\\
&=323\,\mathrm{m^2/s^2}.
\end{aligned}
$$

Hai nghiệm thời gian là:

$$
t_{\pm}=\frac{15{,}0\pm\sqrt{323}}{9{,}80}\,\mathrm s.
$$

Nghiệm dương xấp xỉ 3,36 s, còn nghiệm âm xấp xỉ −0,30 s. Chỉ nghiệm dương thuộc chuyển động sau khi bóng rời tay.

Nghiệm âm mô tả phần ngoại suy của parabol về trước t = 0. Nếu kéo dài mô hình gia tốc không đổi về quá khứ, bóng sẽ từng ở dưới lan can 5,00 m và đang bay lên để tới tay. Bóng thực tế chưa được thả vào khoảng ấy nên nghiệm này không thuộc bài toán.

Hãy xét lại cùng phương trình cho y = +5,00 m. Khi ấy biệt thức bằng 127 m²/s² và hai nghiệm là:

$$
t_{\pm}=\frac{15{,}0\pm\sqrt{127}}{9{,}80}\,\mathrm s.
$$

Hai thời điểm xấp xỉ 0,38 s và 2,68 s đều dương, lần lượt ứng với nhánh đi lên và nhánh đi xuống. Điều này phù hợp với hai dấu vận tốc trong câu (b) của Ví dụ 2.7.

Nếu thay y = +15,0 m, tích 2g(y − $y_0$) bằng 294 m²/s²:

$$
D=(225-294)\,\mathrm{m^2/s^2},
$$

$$
D=-69\,\mathrm{m^2/s^2}<0.
$$

Không có nghiệm thời gian thực vì bóng chỉ lên được khoảng 11,5 m, thấp hơn độ cao 15,0 m.

Với gia tốc khác không, phương trình tọa độ là bậc hai. Nghiệm có thể không thực, có thể trùng nhau hoặc có thể nằm ngoài miền thời gian của tình huống. Cần xét từng nghiệm theo điều kiện vật lý, cả trong rơi tự do lẫn các bài chuyển động thẳng có gia tốc không đổi khác.
:::

### Tự kiểm tra 2.5

::: exercise Tăng gấp đôi tốc độ ném
Ném bóng lên với một tốc độ ban đầu cho trước. Bóng rơi tự do và đạt độ cao cực đại h sau thời gian t kể từ lúc rời tay.

(a) Nếu ném lên với tốc độ ban đầu gấp đôi, độ cao cực đại mới là bao nhiêu: (i) h√2, (ii) 2h, (iii) 4h, (iv) 8h hay (v) 16h?

(b) Thời gian lên tới đỉnh mới là bao nhiêu: (i) t/2, (ii) t/√2, (iii) t, (iv) t√2 hay (v) 2t?
:::

::: solution Giải thích
(a) Chọn (iii). Tại đỉnh, vận tốc bằng không. Hệ thức (2.13) với trục y cho:

$$
h=\frac{v_{0y}^2}{2g}.
$$

Khi vận tốc ném tăng gấp đôi:

$$
h'=\frac{(2v_{0y})^2}{2g}=4h.
$$

(b) Chọn (v). Dùng (2.8) tại đỉnh:

$$
0=v_{0y}-gt.
$$

Suy ra thời gian lên tới đỉnh t = $v_{0y}$/g. Khi vận tốc ném tăng gấp đôi, thời gian này tăng gấp đôi thành 2t.
:::
