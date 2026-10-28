## 2.4. Chuyển động với gia tốc không đổi

Một vật rơi gần mặt đất có gia tốc gần như không đổi nếu có thể bỏ qua ảnh hưởng của không khí. Vật trượt trên mặt phẳng nghiêng, vật trượt trên mặt phẳng ngang nhám hoặc máy bay được phóng từ boong tàu sân bay cũng có thể được mô tả bằng mô hình này.

Trong chuyển động thẳng với gia tốc không đổi, vận tốc thay đổi cùng một lượng trong những khoảng thời gian bằng nhau. Hình 2.15 biểu diễn vị trí, vận tốc và gia tốc ở các thời điểm cách đều. Khoảng cách giữa các vị trí không bằng nhau vì vận tốc đang thay đổi.

![Hình 2.15: Chất điểm chuyển động theo chiều dương với gia tốc dương không đổi](img/young-02/hinh-2-15.png)

Hình 2.16 và Hình 2.17 mô tả cùng chuyển động bằng đồ thị. Đồ thị gia tốc theo thời gian là đường nằm ngang. Đồ thị vận tốc theo thời gian có độ dốc không đổi nên là đường thẳng. Có thể dùng Bảng 2.4 ở cuối Mục 2.3 để đối chiếu ý nghĩa của giá trị, độ dốc và độ cong trên các đồ thị.

![Hình 2.16: Đồ thị gia tốc theo thời gian khi gia tốc dương không đổi](img/young-02/hinh-2-16.png)

![Hình 2.17: Đồ thị vận tốc theo thời gian của chuyển động có gia tốc dương không đổi](img/young-02/hinh-2-17.png)

### Vận tốc theo thời gian

Khi gia tốc không đổi, gia tốc trung bình trên mọi khoảng thời gian bằng gia tốc tức thời. Thay vào định nghĩa gia tốc trung bình:

$$
a_x=\frac{v_{2x}-v_{1x}}{t_2-t_1}.
\tag{2.7}
$$

Chọn thời điểm đầu là $t_1$ = 0. Gọi vận tốc đầu là $v_{0x}$ và vận tốc tại thời điểm t là $v_x$. Ta có:

$$
a_x=\frac{v_x-v_{0x}}{t}.
$$

Nhân hai vế với t rồi chuyển $v_{0x}$ sang vế phải:

$$
v_x=v_{0x}+a_xt.
\tag{2.8}
$$

Tích $a_x$t là gia tốc, tức tốc độ biến thiên vận tốc, nhân với thời gian. Nó bằng toàn bộ độ biến thiên vận tốc trong khoảng từ 0 đến t. Vì vậy, vận tốc cuối bằng vận tốc đầu cộng với độ biến thiên ấy.

Trên Hình 2.16, hình chữ nhật dưới đồ thị có chiều cao $a_x$, chiều rộng t và diện tích $a_x$t. Diện tích này bằng độ biến thiên vận tốc:

$$
v_x-v_{0x}=a_xt.
$$

Mối liên hệ giữa diện tích dưới đồ thị gia tốc và độ biến thiên vận tốc vẫn đúng khi gia tốc thay đổi. Khi ấy phải dùng tích phân ở Mục 2.6, thay cho phép nhân với một giá trị gia tốc cố định.

### Tọa độ theo thời gian

Ta tìm tọa độ bằng hai biểu thức của vận tốc trung bình trên cùng khoảng từ 0 đến t. Gọi $x_0$ là tọa độ đầu và x là tọa độ cuối. Định nghĩa vận tốc trung bình cho:

$$
v_{\mathrm{av}-x}=\frac{x-x_0}{t}.
\tag{2.9}
$$

Định nghĩa này đúng cả khi gia tốc thay đổi. Riêng khi gia tốc không đổi, vận tốc biến thiên tuyến tính nên trung bình trên khoảng bằng trung bình cộng của hai giá trị đầu và cuối:

$$
v_{\mathrm{av}-x}=\frac{v_{0x}+v_x}{2}.
\tag{2.10}
$$

::: warning Điều kiện dùng trung bình cộng hai vận tốc
Công thức (2.10) được bảo đảm khi gia tốc không đổi trên toàn khoảng xét. Nếu gia tốc thay đổi, nó không còn là công thức tổng quát. Một chuyển động cụ thể vẫn có thể tình cờ thỏa đẳng thức trên một khoảng, nên không được dùng đẳng thức ấy để kết luận ngược rằng gia tốc chắc chắn không đổi.
:::

Thay công thức (2.8) vào (2.10):

$$
\begin{aligned}
v_{\mathrm{av}-x}
&=\frac{2v_{0x}+a_xt}{2}\\
&=v_{0x}+\frac12a_xt.
\end{aligned}
\tag{2.11}
$$

Đồng nhất với (2.9):

$$
\frac{x-x_0}{t}=v_{0x}+\frac12a_xt.
$$

Nhân với t và cộng $x_0$ vào hai vế:

$$
x=x_0+v_{0x}t+\frac12a_xt^2.
\tag{2.12}
$$

Tọa độ gồm ba phần. Phần thứ nhất là tọa độ đầu $x_0$. Phần thứ hai là độ dời $v_{0x}$t nếu vận tốc giữ nguyên giá trị đầu. Phần thứ ba là độ dời bổ sung do vận tốc thay đổi.

![Hình 2.18: Chuyển động thẳng và đồ thị tọa độ khi tọa độ đầu, vận tốc đầu, gia tốc đều dương](img/young-02/hinh-2-18.png)

Với gia tốc khác không và không đổi, đồ thị của (2.12) là parabol. Giao điểm với trục tọa độ tại t = 0 cho $x_0$. Độ dốc tiếp tuyến lúc đầu cho $v_{0x}$, còn độ dốc tại thời điểm bất kỳ cho $v_x$. Gia tốc dương làm đồ thị lõm lên. Gia tốc âm làm đồ thị lõm xuống.

Nếu gia tốc bằng không, số hạng bậc hai mất đi và đồ thị tọa độ là đường thẳng. Đồng thời, đồ thị vận tốc là đường nằm ngang. Hình 2.19 cho thấy hai thay đổi xuất hiện khi thêm một gia tốc dương không đổi.

![Hình 2.19: So sánh đồ thị tọa độ và vận tốc khi gia tốc bằng không và khi gia tốc dương không đổi](img/young-02/hinh-2-19.png)

Cũng có thể suy ra (2.12) bằng diện tích dưới đồ thị vận tốc ở Hình 2.17. Hình chữ nhật có diện tích $v_{0x}$t. Tam giác có đáy t và chiều cao $a_x$t:

$$
S_{\triangle}=\frac12(a_xt)t=\frac12a_xt^2.
$$

Tổng diện tích cho độ dời:

$$
x-x_0=v_{0x}t+\frac12a_xt^2.
$$

Trong hình minh họa, các diện tích đều dương. Với vận tốc âm, phải dùng diện tích có dấu khi xác định độ dời.

### Hệ thức không chứa thời gian

Khi đã biết vận tốc đầu, vận tốc cuối và gia tốc, ta có thể loại thời gian khỏi hai phương trình. Đặt độ biến thiên vận tốc là u:

$$
u=v_x-v_{0x}.
$$

Với gia tốc khác không, công thức (2.8) cho:

$$
t=\frac{u}{a_x}.
$$

Thay vào công thức độ dời:

$$
x-x_0=\frac{v_{0x}u}{a_x}+\frac{u^2}{2a_x}.
$$

Nhân hai vế với 2$a_x$:

$$
2a_x(x-x_0)=2v_{0x}u+u^2.
$$

Khai triển từng phần để thấy các số hạng triệt tiêu:

$$
2v_{0x}u=2v_{0x}v_x-2v_{0x}^2,
$$

$$
u^2=v_x^2-2v_{0x}v_x+v_{0x}^2.
$$

Khi cộng hai biểu thức, hai số hạng chứa tích $v_{0x}v_x$ triệt tiêu. Hai số hạng chứa bình phương vận tốc đầu còn lại âm một lần bình phương ấy. Do đó:

$$
2a_x(x-x_0)=v_x^2-v_{0x}^2.
$$

Chuyển vế:

$$
v_x^2=v_{0x}^2+2a_x(x-x_0).
\tag{2.13}
$$

Phép loại thời gian ở trên chia cho $a_x$ nên đã xét $a_x$ khác không. Khi $a_x$ = 0, vận tốc cuối bằng vận tốc đầu, và (2.13) vẫn đúng.

Một hệ thức khác nhận được khi đồng nhất (2.9) với (2.10), rồi nhân với t:

$$
x-x_0=\frac12(v_{0x}+v_x)t.
\tag{2.14}
$$

Công thức này không chứa gia tốc. Nó hữu ích khi gia tốc không đổi nhưng chưa biết giá trị.

### Bảng 2.5: Các phương trình chuyển động với gia tốc không đổi

Bốn phương trình trên dùng tọa độ đầu và vận tốc đầu làm điều kiện đã xác định tại t = 0. Bảng dưới ghi các đại lượng cần liên hệ bên cạnh điều kiện ban đầu.

| Số hiệu | Các đại lượng có mặt |
| --- | --- |
| (2.8) | Thời gian, vận tốc, gia tốc |
| (2.12) | Thời gian, tọa độ, gia tốc |
| (2.13) | Tọa độ, vận tốc, gia tốc |
| (2.14) | Thời gian, tọa độ, vận tốc |

Trong Hình 2.15–2.18, tọa độ đầu, vận tốc đầu và gia tốc đều dương. Hãy phác lại các hình khi một, hai hoặc cả ba đại lượng mang dấu âm để kiểm tra cách hiểu về trục và độ dốc.

### Ứng dụng: Thử nghiệm ở gia tốc lớn

![Ứng dụng 2.A: Chuỗi ảnh John Stapp trên xe trượt tên lửa trong thí nghiệm gia tốc lớn](img/young-02/ung-dung-gia-toc-lon.png)

Trong các thí nghiệm của Không quân Hoa Kỳ vào những năm 1940 và 1950, người ngồi trên xe trượt tên lửa chịu các gia tốc có độ lớn tới 440 m/s². Ba ảnh đầu ghi lại bác sĩ John Stapp tăng tốc từ trạng thái nghỉ lên 188 m/s trong 5 s. Tốc độ ấy tương đương khoảng 678 km/h hoặc 421 dặm/h. Ba ảnh sau cho thấy giai đoạn xe hãm lại, với độ lớn gia tốc lớn hơn.

### Phương pháp giải 2.1: Chuyển động với gia tốc không đổi

Trước hết, xác định gia tốc có thể coi là không đổi hay không. Khi điều kiện này không thỏa, cần dùng cách khác, chẳng hạn tích phân ở Mục 2.6.

1. Đọc đề và vẽ sơ đồ chuyển động ở các thời điểm cần xét. Chọn gốc tọa độ và chiều dương. Đặt vật ở gốc lúc t = 0 có thể giúp $x_0$ = 0. Chiều dương của trục đồng thời quy định dấu của thành phần vận tốc và gia tốc.
2. Gán ký hiệu cho thời gian, tọa độ, vận tốc và gia tốc. Chuyển lời văn thành điều kiện toán học. Câu hỏi về thời điểm ở vị trí cao nhất yêu cầu tìm thời gian ứng với tọa độ cực đại. Câu hỏi về vị trí khi vận tốc bằng 25 m/s yêu cầu tìm tọa độ tại vận tốc đó. Cụm “xe đang dừng ở đèn đỏ” cung cấp vận tốc đầu bằng không.
3. Liệt kê các đại lượng đã biết và chưa biết, rồi xác định chính xác đại lượng cần tìm. Chú ý đại lượng nào không xuất hiện trong dữ kiện hoặc yêu cầu.
4. Dùng Bảng 2.5 chọn phương trình thích hợp. Thường nên chọn phương trình không chứa đại lượng vắng mặt. Có bài chỉ cần một phương trình với một ẩn, có bài cần giải đồng thời hai phương trình với hai ẩn.
5. Phác đồ thị theo các phương trình đã chọn. Đồ thị vận tốc là đường thẳng có độ dốc bằng gia tốc. Đồ thị tọa độ là parabol lõm lên nếu gia tốc dương và lõm xuống nếu gia tốc âm.
6. Dựa vào sơ đồ và đồ thị, dự đoán định tính hoặc ước lượng độ lớn của kết quả.

Giải phương trình bằng ký hiệu trước, sau đó thay số kèm đơn vị. Nếu có hai ẩn, giải hệ để tìm đại lượng cần thiết. Cuối cùng, đối chiếu dấu và độ lớn với dự đoán ban đầu, đồng thời xem chúng có phù hợp tình huống vật lý hay không.

### Ví dụ 2.4: Tính toán với gia tốc không đổi

::: exercise Người lái mô tô qua ranh giới thị trấn
Một người đi mô tô về phía đông tăng tốc với gia tốc không đổi 4,0 m/s² sau khi ra khỏi thị trấn. Tại t = 0, xe ở cách biển ranh giới 5,0 m về phía đông và đang đi về phía đông với tốc độ 15 m/s.

(a) Tìm vị trí và vận tốc lúc t = 2,0 s. (b) Xe ở đâu khi tốc độ đạt 25 m/s?
:::

![Hình 2.20: Vị trí, vận tốc và gia tốc của mô tô đi về phía đông](img/young-02/hinh-2-20.png)

::: solution Các bước tính toán
Chọn gốc tại biển báo và chiều dương về phía đông. Khi ấy $x_0$ = 5,0 m, $v_{0x}$ = 15 m/s và $a_x$ = 4,0 m/s². Gia tốc không đổi nên dùng được bốn phương trình vừa thiết lập.

(a) Vì thời gian đã biết, dùng (2.12) tìm tọa độ và (2.8) tìm vận tốc. Tại t = 2,0 s:

$$
x=x_0+v_{0x}t+\frac12a_xt^2.
$$

Hai phần độ dời lần lượt là:

$$
v_{0x}t=(15)(2{,}0)\,\mathrm m=30\,\mathrm m,
$$

$$
\begin{aligned}
\frac12a_xt^2&=\frac12(4{,}0)(2{,}0)^2\,\mathrm m\\
&=8{,}0\,\mathrm m.
\end{aligned}
$$

Do đó:

$$
\begin{aligned}
x&=(5{,}0+30+8{,}0)\,\mathrm m\\
&=43\,\mathrm m.
\end{aligned}
$$

Xe ở cách biển 43 m về phía đông. Vận tốc là:

$$
\begin{aligned}
v_x&=[15+(4{,}0)(2{,}0)]\,\mathrm{m/s}\\
&=23\,\mathrm{m/s}.
\end{aligned}
$$

(b) Chưa biết thời gian nên dùng (2.13). Giải theo x:

$$
x=x_0+\frac{v_x^2-v_{0x}^2}{2a_x}.
$$

Độ dời để tăng vận tốc từ 15 m/s lên 25 m/s là:

$$
\begin{aligned}
x-x_0&=\frac{25^2-15^2}{2(4{,}0)}\,\mathrm m\\
&=50\,\mathrm m.
\end{aligned}
$$

Vì vậy, xe ở cách biển 55 m về phía đông. Có thể đối chiếu bằng thời gian:

$$
t=\frac{25-15}{4{,}0}\,\mathrm s=2{,}5\,\mathrm s.
$$

Thay thời gian này vào (2.12) cũng cho tọa độ 55 m. Cách dùng (2.13) tìm trực tiếp tọa độ cần ít bước hơn vì không phải tính thời gian trước.
:::

### Ví dụ 2.5: Hai vật có gia tốc khác nhau

::: exercise Mô tô cảnh sát đuổi ô tô
Một ô tô đi với tốc độ không đổi 15 m/s, tương đương 54 km/h hoặc khoảng 34 dặm/h, qua chỗ học sinh sang đường. Giới hạn tốc độ tại đây là 10 m/s, tương đương 36 km/h hoặc khoảng 22 dặm/h. Đúng lúc ô tô qua biển báo, một cảnh sát trên mô tô đang dừng tại đó bắt đầu đuổi theo với gia tốc không đổi 3,0 m/s².

(a) Sau bao lâu cảnh sát vượt ô tô? (b) Tốc độ của cảnh sát lúc ấy bằng bao nhiêu? (c) Mỗi xe đã đi được bao xa?
:::

![Hình 2.21: Sơ đồ và đồ thị tọa độ của mô tô có gia tốc không đổi đuổi ô tô đi đều](img/young-02/hinh-2-21.png)

::: solution Điều kiện gặp nhau
Chọn gốc tại biển báo, chiều dương sang phải và t = 0 khi ô tô qua biển. Hai xe cùng xuất phát tại tọa độ 0. Ô tô có gia tốc bằng không, còn mô tô có gia tốc dương không đổi. Cả hai đều thỏa điều kiện dùng các công thức gia tốc không đổi.

Gọi tọa độ của ô tô là $x_M$ và của cảnh sát là $x_P$. Với t đo bằng giây và tọa độ đo bằng mét:

$$
x_M=15t,\qquad x_P=1{,}5t^2.
$$

Đồ thị ô tô là đường thẳng. Đồ thị mô tô là nửa parabol lõm lên. Phác họa cho thấy chúng cắt nhau khoảng 10 s, ở vị trí cách biển khoảng 150 m.

(a) Hai xe gặp nhau khi tọa độ bằng nhau tại cùng thời điểm:

$$
15t=1{,}5t^2.
$$

Phương trình có nghiệm t = 0 và:

$$
t=\frac{2v_{M0x}}{a_{Px}}.
$$

Thay số:

$$
t=\frac{2(15)}{3{,}0}\,\mathrm s=10\,\mathrm s.
$$

Nghiệm 0 ứng với lúc ô tô vượt cảnh sát. Nghiệm 10 s ứng với lúc cảnh sát vượt ô tô.

(b) Vận tốc của cảnh sát khi gặp là:

$$
\begin{aligned}
v_{Px}&=v_{P0x}+a_{Px}t\\
&=(3{,}0)(10)\,\mathrm{m/s}\\
&=30\,\mathrm{m/s}.
\end{aligned}
$$

Giá trị dương nên tốc độ cũng bằng 30 m/s.

(c) Quãng đường ô tô và mô tô đi được lần lượt là:

$$
x_M=(15)(10)\,\mathrm m=150\,\mathrm m,
$$

$$
\begin{aligned}
x_P&=\frac12(3{,}0)(10)^2\,\mathrm m\\
&=150\,\mathrm m.
\end{aligned}
$$

Các giá trị khớp với ước lượng từ đồ thị. Khi gặp nhau, hai xe có cùng tọa độ nhưng vận tốc khác nhau. Trên đồ thị, hai đường cắt nhau với hai độ dốc khác nhau.

Tốc độ cảnh sát bằng hai lần tốc độ ô tô không phải sự trùng hợp. Ô tô đi đều với độ dời $v_{M0x}$t. Mô tô xuất phát nghỉ, có độ dời bằng một nửa tích của vận tốc cuối với thời gian. Độ dời bằng nhau nên:

$$
v_{M0x}t=\frac12v_{Px}t.
$$

Vì thời gian gặp lại dương:

$$
v_{Px}=2v_{M0x}.
$$

Kết quả này không phụ thuộc độ lớn gia tốc của cảnh sát, với điều kiện mô tô xuất phát nghỉ tại cùng vị trí, tăng tốc không đổi và ô tô giữ vận tốc không đổi.
:::

### Tự kiểm tra 2.4

::: exercise Chọn đồ thị vận tốc của hai xe
Bốn đồ thị dưới đây là các khả năng mô tả hai xe trong Ví dụ 2.5. Đồ thị nào đúng?
:::

![Tự kiểm tra 2.4: Bốn đồ thị vận tốc theo thời gian của ô tô và mô tô cảnh sát](img/young-02/cau-hoi-2-4.png)

::: solution Giải thích
Chọn (b). Gia tốc của cảnh sát không đổi nên vận tốc tăng tuyến tính, còn vận tốc ô tô giữ nguyên. Khi gặp nhau ở 10 s, mô tô chạy nhanh hơn ô tô.

Hai vận tốc bằng nhau ở 5 s, khi đường thẳng của mô tô cắt đường nằm ngang của ô tô. Hai xe chưa gặp nhau tại thời điểm đó. Đến 10 s, diện tích tam giác dưới đồ thị mô tô và diện tích hình chữ nhật dưới đồ thị ô tô cùng bằng 150 m, nên độ dời của chúng bằng nhau.
:::
