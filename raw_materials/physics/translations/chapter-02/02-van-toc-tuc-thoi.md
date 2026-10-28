## 2.2. Vận tốc tức thời

Trong một cuộc đua thẳng, đôi khi vận tốc trung bình đã đủ để xác định người thắng. Với cùng độ dời từ vạch xuất phát đến đích, người hoàn thành trong thời gian ngắn nhất có độ lớn vận tốc trung bình lớn nhất.

![Hình 2.4: Người thắng cuộc đua bơi 50 m hoàn thành cùng độ dời trong thời gian ngắn nhất](img/young-02/hinh-2-4.png)

Tuy nhiên, vận tốc trung bình của một khoảng thời gian không cho biết tại từng thời điểm vật chuyển động nhanh đến mức nào và theo hướng nào. Để mô tả điều đó, ta cần **vận tốc tức thời**.

::: warning Thời điểm không phải một khoảng thời gian ngắn
Trong lời nói, “một thoáng” có thể chỉ một khoảng thời gian rất ngắn. Trong vật lý, một thời điểm chỉ một giá trị xác định của t và không có độ dài thời gian.
:::

### Định nghĩa bằng giới hạn

Muốn tìm vận tốc của xe đua tại vị trí $P_1$ trong Hình 2.1, cho vị trí $P_2$ tiến gần $P_1$. Vận tốc trung bình được tính trên những khoảng thời gian ngày càng ngắn. Cả $\Delta x$ và $\Delta t$ đều nhỏ đi, nhưng tỷ số của chúng không nhất thiết nhỏ đi.

Nếu hàm tọa độ khả vi tại thời điểm xét, giới hạn của tỷ số ấy là đạo hàm theo thời gian:

$$
v_x=\lim_{\Delta t\to0}\frac{\Delta x}{\Delta t}=\frac{dx}{dt}.
\tag{2.3}
$$

Vận tốc tức thời theo trục x chính là tốc độ biến thiên tức thời của tọa độ. Khi xét mốc sau với $\Delta t>0$, dấu của tỷ số được quyết định bởi độ dời. Tọa độ tăng cho $v_x>0$, còn tọa độ giảm cho $v_x<0$.

Tọa độ cho biết vật ở đâu, còn vận tốc cho biết vật đang chuyển động thế nào. Vì thế vật có thể ở vị trí x dương nhưng có vận tốc âm, hoặc ở vị trí x âm nhưng có vận tốc dương. Bảng 2.1 cũng dùng được để đọc dấu của vận tốc tức thời.

![Hình 2.5: Người đi xe đạp sang trái có vận tốc âm hoặc dương tùy chiều trục được chọn](img/young-02/hinh-2-5.png)

Vận tốc tức thời là vector. Trong chuyển động thẳng đang xét, chỉ thành phần x khác không. Khi dùng từ “vận tốc” mà không nói rõ “trung bình”, ta hiểu là vận tốc tức thời.

### Vận tốc và tốc độ

Vận tốc cho biết cả mức độ nhanh chậm lẫn hướng chuyển động. **Tốc độ tức thời** chỉ mức độ nhanh chậm, bằng độ lớn của vận tốc tức thời:

$$
v=|v_x|.
$$

Tốc độ không âm. Chẳng hạn, hai chất điểm có vận tốc $+25\,\mathrm{m/s}$ và $-25\,\mathrm{m/s}$ chuyển động ngược chiều, nhưng đều có tốc độ $25\,\mathrm{m/s}$. Tốc độ trung bình và tốc độ tức thời đều là đại lượng vô hướng vì không chứa thông tin về hướng.

::: warning Tốc độ trung bình và độ lớn vận tốc trung bình
Tốc độ trung bình bằng quãng đường đã đi chia cho thời gian, còn vận tốc trung bình được tính từ độ dời.

Trong cuộc bơi 100,0 m với thành tích 46,91 s của César Cielo năm 2009, tốc độ trung bình là:

$$
\frac{100{,}0\,\mathrm m}{46{,}91\,\mathrm s}\approx2{,}132\,\mathrm{m/s}.
$$

Vì người bơi đi hai lượt trong bể dài 50 m nên điểm cuối trùng điểm đầu. Độ dời và vận tốc trung bình bằng không. Do đó tốc độ trung bình không đồng nhất với độ lớn vận tốc trung bình.
:::

### Ví dụ 2.1: Vận tốc trung bình và tức thời

Một con báo ở cách xe quan sát 20 m về phía đông. Tại $t=0$, báo bắt đầu chạy về phía đông tới con linh dương cách xe 50 m. Trong 2,0 s đầu, tọa độ của báo là:

$$
x(t)=20\,\mathrm m+(5{,}0\,\mathrm{m/s^2})t^2.
$$

(a) Tìm độ dời từ $t_1=1{,}0\,\mathrm s$ đến $t_2=2{,}0\,\mathrm s$. (b) Tìm vận tốc trung bình trong khoảng đó. (c) Tìm vận tốc tức thời tại $t_1=1{,}0\,\mathrm s$ bằng các khoảng $\Delta t$ lần lượt bằng 0,1 s, 0,01 s và 0,001 s. (d) Lấy đạo hàm để tìm vận tốc theo thời gian, rồi tính tại 1,0 s và 2,0 s.

![Hình 2.6: Tình huống con báo săn linh dương, sơ đồ tọa độ và các bước chọn trục, gốc, vị trí, đại lượng đã biết](img/young-02/hinh-2-6.png)

::: solution Lời giải
Chọn gốc tại xe và chiều dương hướng đông. Dùng độ dời cho (a), vận tốc trung bình cho (b), giới hạn các vận tốc trung bình cho (c), rồi đạo hàm cho (d).

(a) Thay hai thời điểm tính bằng giây vào hàm tọa độ, các giá trị tọa độ thu được tính bằng mét:

$$
\begin{aligned}
x_1&=[20+5{,}0(1{,}0)^2]\,\mathrm m\\
&=25\,\mathrm m,\\
x_2&=[20+5{,}0(2{,}0)^2]\,\mathrm m\\
&=40\,\mathrm m.
\end{aligned}
$$

Vậy $\Delta x=40\,\mathrm m-25\,\mathrm m=15\,\mathrm m$.

(b) Khoảng thời gian là 1,0 s:

$$
v_{\mathrm{av}-x}=\frac{15\,\mathrm m}{1{,}0\,\mathrm s}=15\,\mathrm{m/s}.
$$

(c) Với $\Delta t=0{,}1\,\mathrm s$, mốc sau là $t_2=1{,}1\,\mathrm s$ và tọa độ sau là $x_2=26{,}05\,\mathrm m$. Do đó:

$$
\begin{aligned}
v_{\mathrm{av}-x}&=\frac{(26{,}05-25)\,\mathrm m}{0{,}1\,\mathrm s}\\
&=10{,}5\,\mathrm{m/s}.
\end{aligned}
$$

Lặp lại phép tính với hai khoảng ngắn hơn:

| Khoảng thời gian, đơn vị s | Tọa độ sau, đơn vị m | Vận tốc trung bình, đơn vị m/s |
| --- | --- | --- |
| 0,1 | 26,05 | 10,5 |
| 0,01 | 25,1005 | 10,05 |
| 0,001 | 25,010005 | 10,005 |

Khi khoảng thời gian tiến về không, vận tốc trung bình tiến tới 10,0 m/s. Trong những phép tính giới hạn này, ta giữ thêm chữ số để quan sát sự hội tụ, thay vì làm tròn ngay theo quy tắc chữ số có nghĩa.

(d) Đạo hàm của hằng số bằng không, còn đạo hàm của số hạng bậc hai đem hệ số 2 ra trước và giảm số mũ đi một:

$$
\begin{aligned}
v_x(t)&=\frac{dx}{dt}\\
&=0+2(5{,}0\,\mathrm{m/s^2})t\\
&=(10\,\mathrm{m/s^2})t.
\end{aligned}
$$

Tại 1,0 s, vận tốc là 10 m/s. Tại 2,0 s, vận tốc là 20 m/s. Kết quả đầu khớp giới hạn ở (c).

Trong giây đầu, báo đi được 5 m. Trong giây thứ hai, báo đi thêm 15 m. Vận tốc tăng từ 0 lên 10 m/s rồi 20 m/s phù hợp với các quãng đường ấy. Muốn tìm vận tốc trung bình, dùng độ dời chia thời gian. Muốn tìm vận tốc tức thời từ hàm tọa độ, lấy đạo hàm.
:::

### Tìm vận tốc trên đồ thị tọa độ

Khi $p_2$ tiến gần $p_1$ trên đồ thị tọa độ theo thời gian, cát tuyến tiến tới tiếp tuyến tại $p_1$. Vận tốc tức thời tại một thời điểm bằng độ dốc của tiếp tuyến tại điểm đồ thị tương ứng.

![Hình 2.7: Vận tốc trung bình trên khoảng ngắn dần tiến tới độ dốc tiếp tuyến, tức vận tốc tức thời](img/young-02/hinh-2-7.png)

Trong các hình (a) và (b), độ dốc cát tuyến lần lượt là 75 m/s và 55 m/s. Ở hình (c), chọn hai khoảng tương ứng trên tiếp tuyến cho:

$$
v_x=\frac{160\,\mathrm m}{4{,}0\,\mathrm s}=40\,\mathrm{m/s}.
$$

Tiếp tuyến dốc lên sang phải cho vận tốc dương. Tiếp tuyến dốc xuống sang phải cho vận tốc âm. Tiếp tuyến nằm ngang cho vận tốc bằng không. Độ lớn của độ dốc càng lớn thì tốc độ càng lớn.

![Hình 2.8: Cùng một chuyển động được mô tả bằng đồ thị tọa độ và sơ đồ vị trí, vector vận tốc tại từng mốc](img/young-02/hinh-2-8.png)

Ở mốc A, chất điểm có tọa độ âm nhưng chuyển động theo chiều dương. Từ A đến B, nó nhanh dần. Từ B đến C, nó chậm dần và dừng tức thời tại C.

Từ C đến D, vật chuyển động theo chiều âm và nhanh dần. Từ D đến E, nó vẫn đi theo chiều âm nhưng chậm dần. Đồ thị tọa độ và sơ đồ chuyển động là hai cách bổ sung cho nhau, nên có thể vẽ cả hai khi giải bài.

### Tự kiểm tra 2.2

::: exercise Đọc vận tốc và tốc độ từ đồ thị
Hình 2.9 là đồ thị tọa độ theo thời gian của một chất điểm.

![Hình 2.9: Đồ thị tọa độ với bốn điểm P, Q, R và S](img/young-02/hinh-2-9.png)

(a) Xếp vận tốc theo trục x tại P, Q, R, S từ dương lớn nhất đến âm nhỏ nhất. (b) Ở điểm nào vận tốc dương? (c) Ở điểm nào vận tốc âm? (d) Ở điểm nào vận tốc bằng không? (e) Xếp tốc độ từ lớn nhất đến nhỏ nhất.
:::

::: solution Giải thích
Đọc dấu và độ lớn của độ dốc tiếp tuyến tại từng điểm.

(a) P có vận tốc dương. Q và S có tiếp tuyến ngang nên vận tốc bằng không. R có vận tốc âm. Thứ tự là P, rồi Q và S bằng nhau, cuối cùng R.

(b) Vận tốc dương tại P. (c) Vận tốc âm tại R. (d) Vận tốc bằng không tại Q và S.

(e) Tốc độ là độ lớn vận tốc, nên dấu âm của độ dốc không làm tốc độ nhỏ hơn. Tiếp tuyến ở R dốc nhất về độ lớn, sau đó là P. Tại Q và S, tốc độ đều bằng không. Thứ tự tốc độ là R, P, rồi Q và S bằng nhau.
:::
