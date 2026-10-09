<!-- Nguồn: mục 2.2, trang in 37–40, trang PDF 57–60; gồm công thức 2.3, Hình 2.4–2.9, Ví dụ 2.1 và câu hỏi. -->

## 2.2. Vận tốc tức thời

Đôi khi vận tốc trung bình đã đủ để mô tả câu hỏi về chuyển động. Chẳng hạn, cuộc đua trên đường thẳng là cuộc so sánh ai có độ lớn vận tốc trung bình lớn nhất. Người chiến thắng đi hết độ dời từ vạch đầu tới vạch cuối trong thời gian ngắn nhất, như Hình 2.4.

![Hình 2.4 nguyên tác: cuộc thi bơi trên đường thẳng dài 50 mét](img/young-02/hinh-2-4.png)

**Hình 2.4:** Người thắng cuộc bơi $50\,\mathrm m$ có độ lớn vận tốc trung bình lớn nhất, tức thực hiện độ dời $50\,\mathrm m$ trong khoảng thời gian ngắn nhất.

Nhưng vận tốc trung bình không cho biết chất điểm đi nhanh thế nào và theo hướng nào tại từng thời điểm bên trong khoảng ấy. Để biết, cần **vận tốc tức thời**, tức vận tốc tại một thời điểm xác định hoặc tại một điểm xác định trên đường đi.

::: warning Một thời điểm kéo dài bao lâu?
Trong đời thường, “chỉ trong một thoáng” có thể chỉ một khoảng thời gian rất ngắn. Trong vật lý, một thời điểm không có độ kéo dài: đó là một giá trị thời gian duy nhất.
:::

Để tìm vận tốc xe đua ở $P_1$ trong Hình 2.1, đưa $P_2$ càng gần $P_1$ và tính $\Delta x/\Delta t$ trên những độ dời, thời gian càng ngắn. Cả tử và mẫu đều nhỏ đi, nhưng tỷ số không nhất thiết nhỏ. Trong giải tích, giới hạn khi $\Delta t$ tiến tới không là đạo hàm của $x$ theo $t$, ký hiệu $dx/dt$. Ta dùng $v_x$, không có chỉ số av, cho vận tốc tức thời theo $x$:

$$v_x=\lim_{\Delta t\to0}\frac{\Delta x}{\Delta t}
=\frac{dx}{dt}.\tag{2.3}$$

Đây là tốc độ biến thiên tức thời của tọa độ. Khoảng $\Delta t$ trong cách xét luôn dương, nên $v_x$ cùng dấu $\Delta x$. $v_x>0$ cho biết $x$ tăng và vật đi theo $+x$; $v_x<0$ cho biết $x$ giảm và vật đi theo $-x$.

Vật có thể có $x>0$ mà $v_x<0$, hoặc ngược lại: tọa độ cho biết vật ở đâu, vận tốc cho biết nó chuyển động thế nào. Quy tắc Bảng 2.1 áp dụng cho cả vận tốc trung bình và tức thời.

![Hình 2.5 nguyên tác: người đi xe đạp sang trái với hai lựa chọn chiều dương](img/young-02/hinh-2-5.png)

**Hình 2.5:** Người đi xe đạp sang trái có $v_x<0$ nếu chọn chiều dương sang phải, nhưng $v_x>0$ nếu chọn chiều dương sang trái. Trong bài chuyển động thẳng, lựa chọn chiều dương thuộc về bạn.

Vận tốc tức thời cũng là vector. (2.3) định nghĩa thành phần $x$; trong chuyển động thẳng theo $x$, các thành phần khác bằng không. Ta thường gọi ngắn $v_x$ là vận tốc tức thời. Chương 3 sẽ xét các thành phần khác không. Khi dùng từ “vận tốc” mà không ghi “trung bình”, sách luôn hiểu là vận tốc tức thời.

### Phân biệt tốc độ với vận tốc

Trong giao tiếp hằng ngày, hai từ có thể dùng lẫn, nhưng vật lý định nghĩa khác nhau. **Tốc độ** liên hệ quãng đường đi được với thời gian, ở mức trung bình hoặc tức thời. **Tốc độ tức thời**, ký hiệu $v$ không chỉ số, chỉ mức nhanh chậm. Vận tốc tức thời cho cả nhanh chậm lẫn hướng. Tốc độ tức thời là độ lớn vận tốc tức thời và không âm.

Ví dụ, hai chất điểm có $v_x=25\,\mathrm{m/s}$ và $v_x=-25\,\mathrm{m/s}$ đi ngược hướng nhưng cùng tốc độ $25\,\mathrm{m/s}$.

::: warning Tốc độ trung bình không bằng độ lớn vận tốc trung bình
Theo dữ kiện của sách, năm 2009 César Cielo lập kỷ lục bơi $100.0\,\mathrm m$ trong $46.91\,\mathrm s$. Tốc độ trung bình là $100.0/46.91\approx2.132\,\mathrm{m/s}$. Nhưng vì bơi hai chiều dài của bể $50\,\mathrm m$, điểm đầu và cuối trùng nhau. Độ dời tổng và vận tốc trung bình đều bằng không. Cả tốc độ trung bình và tức thời là số vô hướng vì không chứa thông tin hướng.
:::

### Ví dụ 2.1 — Vận tốc trung bình và tức thời

::: exercise Đề bài trong sách
Một con báo săn đang phục kích cách một xe $20\,\mathrm m$ về đông, như Hình 2.6a. Tại $t=0$, nó bắt đầu chạy thẳng về đông tới con linh dương cách xe $50\,\mathrm m$ về đông. Trong $2.0\,\mathrm s$ đầu, tọa độ báo thay đổi theo:

$$x=20\,\mathrm m+(5.0\,\mathrm{m/s^2})t^2.$$

**(a)** Tìm độ dời từ $t_1=1.0\,\mathrm s$ đến $t_2=2.0\,\mathrm s$.

**(b)** Tìm vận tốc trung bình trong khoảng ấy.

**(c)** Tìm vận tốc tức thời tại $t_1=1.0\,\mathrm s$ bằng cách lần lượt lấy $\Delta t=0.1$, $0.01$, $0.001\,\mathrm s$.

**(d)** Lập biểu thức vận tốc tức thời theo thời gian, dùng nó tìm $v_x$ tại $t=1.0$ và $2.0\,\mathrm s$.
:::

![Hình 2.6 nguyên tác: báo săn phục kích linh dương, sơ đồ vị trí và các lựa chọn thiết lập bài](img/young-02/hinh-2-6.png)

**Hình 2.6:** (a) Tình huống báo tấn công linh dương từ chỗ phục kích; các con vật không vẽ cùng tỷ lệ với trục. (b) Hình phác đặt xe ở gốc, báo lúc đầu tại $20\,\mathrm m$, linh dương tại $50\,\mathrm m$, ghi vị trí báo ở $1$ và $2$ giây cùng dữ kiện và đại lượng chưa biết. (c) Các quyết định: hướng trục theo chiều báo chạy để các giá trị dương; đặt gốc tại xe; đánh dấu vị trí đầu báo và linh dương; đánh dấu vị trí báo sau $1$, $2$ giây; thêm đại lượng đã biết và cần tìm.

::: solution Lời giải của sách
**Xác định và thiết lập.** Theo hình phác 2.6b, dùng (2.1) cho độ dời, (2.2) cho vận tốc trung bình, (2.3) cho tức thời.

**Thực hiện (a).**

$$
\begin{aligned}
x_1&=20\,\mathrm m+(5.0\,\mathrm{m/s^2})(1.0\,\mathrm s)^2=25\,\mathrm m,\\
x_2&=20\,\mathrm m+(5.0\,\mathrm{m/s^2})(2.0\,\mathrm s)^2=40\,\mathrm m.
\end{aligned}
$$

Độ dời trong khoảng $1.0\,\mathrm s$ là $\Delta x=40-25=15\,\mathrm m$.

**(b)**

$$v_{\mathrm{av}-x}=\frac{40\,\mathrm m-25\,\mathrm m}{2.0\,\mathrm s-1.0\,\mathrm s}
=15\,\mathrm{m/s}.$$

**(c)** Với $\Delta t=0.1\,\mathrm s$, thời điểm cuối mới là $t_2=1.1\,\mathrm s$:

$$x_2=20\,\mathrm m+(5.0\,\mathrm{m/s^2})(1.1\,\mathrm s)^2=26.05\,\mathrm m,$$

$$v_{\mathrm{av}-x}=\frac{26.05\,\mathrm m-25\,\mathrm m}{1.1\,\mathrm s-1.0\,\mathrm s}
=10.5\,\mathrm{m/s}.$$

Làm tương tự với khoảng $0.01$ và $0.001\,\mathrm s$, được $10.05$ và $10.005\,\mathrm{m/s}$. Khi khoảng nhỏ dần, vận tốc trung bình tiến tới $10.0\,\mathrm{m/s}$. Vì vậy đó là vận tốc tức thời tại $t=1.0\,\mathrm s$. Trong các phép tính giới hạn này, sách tạm không áp dụng quy tắc làm tròn chữ số có nghĩa.

**(d)** Đạo hàm hằng số bằng không, đạo hàm $t^2$ bằng $2t$:

$$
\begin{aligned}
v_x&=\frac{dx}{dt}
=\frac{d}{dt}[20\,\mathrm m+(5.0\,\mathrm{m/s^2})t^2]\\
&=0+(5.0\,\mathrm{m/s^2})(2t)
=(10\,\mathrm{m/s^2})t.
\end{aligned}
$$

Tại $1.0\,\mathrm s$, $v_x=10\,\mathrm{m/s}$, phù hợp (c). Tại $2.0\,\mathrm s$, $v_x=20\,\mathrm{m/s}$.

**Đánh giá.** Báo tăng tốc độ từ lúc đầu đứng yên đến $10\,\mathrm{m/s}$ sau một giây và $20\,\mathrm{m/s}$ sau hai giây. Điều đó hợp lý vì giây đầu nó đi $5\,\mathrm m$, còn giây thứ hai đi $15\,\mathrm m$.

**Ý chính của ví dụ:** Tính vận tốc trung bình bằng độ dời cuối trừ đầu, chia thời gian. Tính vận tốc tức thời bằng đạo hàm vị trí theo thời gian, tương ứng giới hạn vận tốc trung bình trên khoảng thời gian vô cùng ngắn.
:::

### Tìm vận tốc trên đồ thị vị trí–thời gian

Có thể tìm vận tốc từ đồ thị vị trí theo thời gian. Khi $P_2$ trên đường xe đua tiến về $P_1$, điểm $p_2$ trên đồ thị ở Hình 2.7a,b tiến về $p_1$, và vận tốc trung bình được tính trên khoảng càng ngắn. Trong giới hạn $\Delta t\to0$, độ dốc dây cung $p_1p_2$ trở thành độ dốc tiếp tuyến tại $p_1$, như Hình 2.7c. Vì vậy vận tốc tức thời bằng độ dốc tiếp tuyến của đồ thị $x$–$t$.

![Hình 2.7 nguyên tác: từ độ dốc dây cung trên hai khoảng thời gian tới độ dốc tiếp tuyến](img/young-02/hinh-2-7.png)

**Hình 2.7:** (a) $\Delta t=2.0\,\mathrm s$, $\Delta x=150\,\mathrm m$, vận tốc trung bình $75\,\mathrm{m/s}$. (b) $\Delta t=1.0\,\mathrm s$, $\Delta x=55\,\mathrm m$, vận tốc trung bình $55\,\mathrm{m/s}$. (c) Độ dốc tiếp tuyến cho vận tốc tức thời $160\,\mathrm m/(4.0\,\mathrm s)=40\,\mathrm{m/s}$. Để tính độ dốc tiếp tuyến, có thể chọn bất kỳ đoạn tăng đứng nào trên đường tiếp tuyến và đoạn tăng ngang tương ứng. Hai trục đều ghi đơn vị mét và giây.

Tiếp tuyến dốc lên về phải có độ dốc và vận tốc dương, chuyển động theo $+x$. Dốc xuống về phải cho vận tốc âm, chuyển động theo $-x$. Tiếp tuyến ngang cho vận tốc bằng không. Hình 2.8 minh họa các khả năng này.

![Hình 2.8 nguyên tác: đồ thị vị trí theo thời gian và sơ đồ chuyển động tại năm thời điểm](img/young-02/hinh-2-8.png)

**Hình 2.8a:** Trên đồ thị, độ dốc tiếp tuyến ở mỗi điểm bằng vận tốc. Độ dốc càng lớn về giá trị tuyệt đối, tốc độ càng lớn, bất kể dấu.

**Hình 2.8b:** Tại $t_A=0$, chất điểm có $x<0$ nhưng đi theo $+x$. Từ A đến B nó nhanh dần; từ B đến C chậm dần và dừng tức thời ở C. Từ C đến D nó nhanh dần theo $-x$; từ D đến E chậm dần theo $-x$. Các mũi tên vận tốc, vị trí và dấu trên hình thể hiện những thay đổi ấy.

Hình 2.8 diễn tả cùng chuyển động bằng hai cách: đồ thị $x$–$t$ và sơ đồ gồm vị trí tại từng thời điểm, như các khung hình video, cùng mũi tên vận tốc. Chương sử dụng cả hai. Khi giải bài chuyển động, vẽ cả đồ thị và sơ đồ sẽ có ích.

### Câu hỏi kiểm tra hiểu mục 2.2

::: exercise Câu hỏi trong sách
Hình 2.9 là đồ thị $x$–$t$ của chất điểm.

**(a)** Xếp $v_x$ tại P, Q, R, S từ dương nhất tới âm nhất.

**(b)** Điểm nào có $v_x>0$?

**(c)** Điểm nào có $v_x<0$?

**(d)** Điểm nào có $v_x=0$?

**(e)** Xếp tốc độ tại các điểm từ nhanh nhất tới chậm nhất.
:::

![Hình 2.9 nguyên tác: đồ thị vị trí có điểm P trên đoạn tăng, Q và S ở hai cực trị, R trên đoạn giảm](img/young-02/hinh-2-9.png)

**Hình 2.9:** Trục đứng là $x$, trục ngang là $t$, gốc O. Các điểm P, Q, R, S nằm trên đường cong vị trí.

::: solution Đáp án của sách
**(a)** P, rồi Q và S bằng nhau, rồi R.

**(b)** P có vận tốc dương vì độ dốc dương.

**(c)** R có vận tốc âm vì độ dốc âm.

**(d)** Q và S có vận tốc bằng không vì tiếp tuyến ngang.

**(e)** R, rồi P, rồi Q và S bằng nhau. Tốc độ lớn nhất nơi độ dốc lớn nhất về giá trị tuyệt đối, dù dương hay âm; nó bằng không nơi độ dốc bằng không.
:::
