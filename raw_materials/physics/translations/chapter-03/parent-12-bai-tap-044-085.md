Trừ khi có chỉ dẫn khác, lấy $g=9{,}80\,\mathrm{m/s^2}$ và bỏ qua lực cản không khí. Với bài ném, chọn trục ngang hướng theo chuyển động và trục đứng hướng lên. Các phương trình theo thời gian dùng đơn vị SI.

### 3.44 (••, CP, CALC): Khoảng cách của chó tới gốc cây

Một con chó đứng yên dưới gốc cây tại $t=0$, rồi chạy trong cánh đồng với các thành phần gia tốc:

$$
a_x=0{,}400\,\mathrm{m/s^2},
$$

$$
a_y=-(0{,}180\,\mathrm{m/s^3})t.
$$

Sau $8{,}00\,\mathrm s$, chó cách gốc cây bao xa?

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Vị trí và vận tốc ban đầu đều bằng không khi chọn gốc tại cây.

**Hướng đi:** Gia tốc chưa cho trực tiếp độ dời. Tích phân từng thành phần hai lần, dùng điều kiện đầu rồi lấy độ lớn vector vị trí. Khoảng cách tới cây khác tổng chiều dài đường chạy.

**Lời giải:** Từ điều kiện đầu:

$$
v_x=0{,}400t,
$$

$$
v_y=-0{,}0900t^2.
$$

Tích phân tiếp được:

$$
x=0{,}200t^2,
$$

$$
y=-0{,}0300t^3.
$$

Tại $t=8{,}00\,\mathrm s$, $x=12{,}8\,\mathrm m$ và $y=-15{,}36\,\mathrm m$. Vì hai trục vuông góc:

$$
r=\sqrt{x^2+y^2}\approx20{,}0\,\mathrm m.
$$

</details>

### 3.45 (••, CALC): Khi vận tốc nghiêng đều với hai trục

Vị trí của một vật có các thành phần $x=bt^2$, $y=ct^3$, với $b,c$ là các hằng số dương. Khi nào vector vận tốc tạo góc $45{,}0^\circ$ với cả trục $x$ lẫn trục $y$?

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Các hệ số dương nên tại $t>0$, cả hai thành phần vận tốc đều dương.

**Hướng đi:** Lấy đạo hàm vị trí trước khi xét hướng. Góc bằng nhau với hai trục dương đòi hỏi hai thành phần vận tốc bằng nhau, không phải hai tọa độ bằng nhau.

**Lời giải:** Ta có $v_x=2bt$ và $v_y=3ct^2$. Với $t>0$:

$$
2bt=3ct^2.
$$

Chia cho $t$ rồi giải:

$$
t=\frac{2b}{3c}.
$$

Nghiệm $t=0$ của phương trình chưa rút gọn bị loại vì khi ấy vận tốc bằng không và không có hướng xác định.

</details>

### 3.46 (•••, CALC): Tên lửa có gia tốc biến thiên

Một tên lửa mô hình bị lỗi chuyển động trong mặt phẳng $xy$, với chiều $y$ dương hướng lên. Gia tốc là $a_x=at^2$ và $a_y=\beta-\gamma t$, trong đó:

$$
a=2{,}50\,\mathrm{m/s^4},
$$

$$
\beta=9{,}00\,\mathrm{m/s^2},
$$

$$
\gamma=1{,}40\,\mathrm{m/s^3}.
$$

Tại $t=0$, tên lửa ở gốc, có $v_{0x}=1{,}00\,\mathrm{m/s}$ và $v_{0y}=7{,}00\,\mathrm{m/s}$. (a) Tìm vector vận tốc và vị trí theo thời gian. (b) Tìm độ cao lớn nhất. (c) Khi tên lửa trở lại $y=0$, độ dời ngang bằng bao nhiêu?

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Đây là gia tốc được cho theo thời gian, không phải chuyển động ném với gia tốc đứng không đổi.

**Hướng đi:** Tích phân độc lập hai thành phần. Điểm cao nhất thỏa vận tốc đứng bằng không. Lúc trở về mặt phẳng ban đầu phải là nghiệm dương khác thời điểm phóng.

**Lời giải:** (a) Với $\vec v=v_x\hat\imath+v_y\hat\jmath$, các thành phần là:

$$
v_x=v_{0x}+\frac a3t^3,
$$

$$
v_y=v_{0y}+\beta t-\frac\gamma2t^2.
$$

Vector vị trí $\vec r=x\hat\imath+y\hat\jmath$ có:

$$
x=v_{0x}t+\frac a{12}t^4,
$$

$$
y=v_{0y}t+\frac\beta2t^2-\frac\gamma6t^3.
$$

(b) Giải $v_y=0$ cho nghiệm dương $t_h\approx13{,}5928\,\mathrm s$. Trước nghiệm này $v_y>0$, sau đó $v_y<0$, nên:

$$
y_{\max}\approx340{,}58\,\mathrm m.
$$

(c) Ngoài nghiệm $t=0$, điều kiện $y=0$ là:

$$
7{,}00+4{,}50t-\frac{1{,}40}{6}t^2=0.
$$

Nghiệm dương $t_f\approx20{,}7327\,\mathrm s$ cho:

$$
x(t_f)\approx3{,}85\times10^4\,\mathrm m.
$$

Độ dời ngang lớn do gia tốc ngang tăng theo bình phương thời gian trong mô hình đã cho.

</details>

### 3.47 (•••, CP): Tên lửa rời mặt dốc

Một tên lửa thử nghiệm bắt đầu đứng yên tại A, được gia tốc $1{,}90\,\mathrm{m/s^2}$ dọc mặt dốc dài $200{,}0\,\mathrm m$, nghiêng $35{,}0^\circ$ so với phương ngang. Ngay khi rời dốc, động cơ tắt và tên lửa chỉ còn chịu trọng lực. Tìm (a) độ cao lớn nhất so với mặt đất và (b) độ dời ngang lớn nhất tính từ A.

![Hình P3.47: Tên lửa tăng tốc trên mặt dốc trước khi bay tự do.](/vat-ly-1/bai-giang/img/young-03/r-numbered-late-p3-47.png)

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Chuyển động gồm giai đoạn gia tốc dọc dốc và giai đoạn bay tự do.

**Hướng đi:** Tìm tốc độ ở cuối dốc bằng hệ thức không chứa thời gian. Sau đó giữ vận tốc tiếp tuyến làm vận tốc đầu của chuyển động ném. Cộng cả tọa độ cuối dốc khi tính từ A.

**Lời giải:** Tốc độ rời dốc là:

$$
u=\sqrt{2as}\approx27{,}568\,\mathrm{m/s}.
$$

Điểm rời dốc có $x_B=200\cos35^\circ$ và $y_B=200\sin35^\circ$, theo đơn vị mét. Đặt $u_x=u\cos35^\circ$, $u_y=u\sin35^\circ$.

(a) Độ cao cực đại là:

$$
H=y_B+\frac{u_y^2}{2g}\approx127\,\mathrm m.
$$

(b) Tính thời gian $t$ kể từ khi rời dốc. Nghiệm dương của phương trình $y_B+u_yt-gt^2/2=0$ là $t\approx6{,}714\,\mathrm s$. Vì thế:

$$
X=x_B+u_xt\approx315\,\mathrm m.
$$

Khoảng bay ngang sau khi rời dốc chỉ là một phần của độ dời ngang tính từ A.

</details>

### 3.48 (••, CALC): Hướng gia tốc của chuồn chuồn

Một con chuồn chuồn bay trong mặt phẳng song song mặt đất với:

$$
x=2{,}90+0{,}0900t^2,
$$

$$
y=-0{,}0150t^3.
$$

Tọa độ tính bằng mét, thời gian bằng giây. (a) Khi nào vận tốc nghiêng $30{,}0^\circ$ theo chiều kim đồng hồ từ trục $x$ dương? (b) Khi ấy gia tốc có độ lớn và hướng nào?

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Mặt phẳng chuyển động là mặt phẳng ngang. Trục $y$ ở đây không chỉ độ cao.

**Hướng đi:** Góc vận tốc được quyết định bởi tỷ số hai đạo hàm bậc nhất. Sau khi tìm thời điểm mới dùng đạo hàm bậc hai để xác định gia tốc.

**Lời giải:** (a) Các thành phần vận tốc là $v_x=0{,}180t$, $v_y=-0{,}0450t^2$. Với $t>0$:

$$
\frac{v_y}{v_x}=-\frac t4=-\tan30^\circ.
$$

Suy ra $t\approx2{,}31\,\mathrm s$. Thời điểm $t=0$ không có hướng vận tốc.

(b) Ta có $a_x=0{,}180\,\mathrm{m/s^2}$ và $a_y=-0{,}0900t$. Tại thời điểm vừa tìm, $a_y\approx-0{,}20785\,\mathrm{m/s^2}$. Do đó:

$$
|\vec a|\approx0{,}275\,\mathrm{m/s^2}.
$$

Gia tốc nghiêng khoảng $49{,}1^\circ$ theo chiều kim đồng hồ từ trục $x$ dương, khác hướng của vận tốc.

</details>

### 3.49 (••): Thả vật đánh dấu từ máy bay

Để luyện thả nước hỗ trợ chữa cháy rừng, phi công thả một hộp thuốc nhuộm đỏ nhằm trúng mục tiêu dưới đất. Máy bay bay ngang ở độ cao $90{,}0\,\mathrm m$ với tốc độ $64{,}0\,\mathrm{m/s}$, xấp xỉ $143\,\mathrm{mi/h}$. Phải thả hộp khi còn cách mục tiêu bao xa theo phương ngang?

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Hộp được thả từ máy bay bay ngang nên có vận tốc ngang ban đầu nhưng vận tốc đứng ban đầu bằng không.

**Hướng đi:** Thời gian rơi do chuyển động đứng quyết định. Trong thời gian ấy hộp vẫn chuyển động ngang cùng vận tốc ban đầu.

**Lời giải:** Từ $90{,}0-gt^2/2=0$:

$$
t=\sqrt{\frac{2(90{,}0)}g}\approx4{,}286\,\mathrm s.
$$

Khoảng cách cần thả trước là:

$$
d=64{,}0t\approx274\,\mathrm m.
$$

Kết quả là khoảng cách ngang, không phải khoảng cách xiên từ máy bay tới mục tiêu.

</details>

### 3.50 (••, CALC): Chim trở lại đường thẳng đứng qua điểm đầu

Một con chim bay trong mặt phẳng $xy$, với $y$ dương hướng lên. Vận tốc có $v_x=a-bt^2$, $v_y=\gamma t$, trong đó $a=2{,}4\,\mathrm{m/s}$, $b=1{,}6\,\mathrm{m/s^3}$ và $\gamma=4{,}0\,\mathrm{m/s^2}$. Chim ở gốc tại $t=0$. (a) Tìm vector vị trí và gia tốc theo thời gian. (b) Lần đầu sau $t=0$ chim bay qua $x=0$, độ cao bằng bao nhiêu?

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Phương trình đã cho là vận tốc. Trục $y$ biểu diễn độ cao.

**Hướng đi:** Tích phân để tìm vị trí và lấy đạo hàm để tìm gia tốc. Điều kiện trở lại $x=0$ có nghiệm ban đầu cần loại.

**Lời giải:** (a) Các thành phần của $\vec r=x\hat\imath+y\hat\jmath$ là:

$$
x=at-\frac b3t^3,\qquad y=\frac\gamma2t^2.
$$

Các thành phần của $\vec a$ là $a_x=-2bt$ và $a_y=\gamma$. Hai vector đầy đủ là:

$$
\vec r=\left(at-\frac b3t^3\right)\hat\imath+\frac\gamma2t^2\hat\jmath.
$$

$$
\vec a=-2bt\hat\imath+\gamma\hat\jmath.
$$

(b) Từ $x=t(a-bt^2/3)=0$, nghiệm dương khác không là:

$$
t=\sqrt{\frac{3a}b}\approx2{,}121\,\mathrm s.
$$

Khi ấy $y=\gamma t^2/2=9{,}0\,\mathrm m$.

</details>

### 3.51 (•••): Rời trực thăng đang bay lên

Một nữ diễn viên đóng thế buông mình từ trực thăng ở độ cao $30{,}0\,\mathrm m$. Trực thăng có vận tốc không đổi, gồm $10{,}0\,\mathrm{m/s}$ hướng lên và $15{,}0\,\mathrm{m/s}$ theo phương ngang về nam. (a) So với vị trí trực thăng lúc cô rời đi, phải đặt đệm ở đâu trên mặt đất? (b) Vẽ các đồ thị tọa độ ngang, tọa độ đứng và hai thành phần vận tốc theo thời gian.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Buông người không làm mất vận tốc đứng đang có cùng trực thăng.

**Hướng đi:** Giữ cả hai thành phần vận tốc lúc rời máy bay. Giải nghiệm thời gian chạm đất dương rồi tính độ dời ngang. Các đồ thị phải cho thấy cơ thể còn đi lên một đoạn trước khi rơi.

**Lời giải:** Chọn $x$ dương về nam và $y=0$ ở mặt đất. Các phương trình là:

$$
x=15{,}0t,\qquad v_x=15{,}0,
$$

$$
y=30{,}0+10{,}0t-4{,}90t^2,
$$

$$
v_y=10{,}0-9{,}80t.
$$

(a) Nghiệm $y=0$ dương là $t_f\approx3{,}697\,\mathrm s$. Cần đặt đệm trên mặt đất, cách điểm ngay dưới trực thăng lúc buông khoảng $55{,}5\,\mathrm m$ về nam.

(b) Đồ thị $x(t)$ là đường thẳng tăng, $y(t)$ là parabol úp, $v_x(t)$ nằm ngang và $v_y(t)$ giảm tuyến tính. Miền vẽ kết thúc tại $t_f$.

![Bốn đồ thị của diễn viên với vị trí ngang tăng đều, độ cao ban đầu tăng rồi giảm và vận tốc đứng giảm](/vat-ly-1/bai-giang/img/young-03/solution-s3-51.svg)


</details>

### 3.52 (••): Vượt mép vách đá với góc phóng cố định

Một khẩu pháo cách chân vách đá thẳng đứng $60{,}0\,\mathrm m$, vách cao $25{,}0\,\mathrm m$. Pháo bắn đạn khối lượng $15\,\mathrm{kg}$ về vách ở góc $43{,}0^\circ$ trên phương ngang. (a) Tốc độ đầu nhỏ nhất để vừa vượt mép vách là bao nhiêu? (b) Với điều kiện ấy, đạn rơi cách mép bao xa trên vùng đất nằm ngang cao $25{,}0\,\mathrm m$?

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Góc phóng đã cố định. Mặt đất phía sau vách có cùng cao độ với đỉnh vách.

**Hướng đi:** Loại thời gian để xét độ cao tại mép. Sau khi tìm tốc độ giới hạn, kiểm tra chiều vận tốc đứng tại mép trước khi chọn nghiệm giao với mặt đất phía trên.

**Lời giải:** (a) Với $d=60{,}0\,\mathrm m$, $h=25{,}0\,\mathrm m$ và $\theta=43{,}0^\circ$, phương trình quỹ đạo cho:

$$
h=d\tan\theta-\frac{gd^2}{2v_0^2\cos^2\theta}.
$$

Suy ra:

$$
v_0^2=\frac{gd^2}{2\cos^2\theta(d\tan\theta-h)}.
$$

Kết quả $v_{0,\min}\approx32{,}64\,\mathrm{m/s}$. Đây là tốc độ giới hạn để vừa chạm mép, còn muốn có khoảng hở phải tăng tốc độ.

(b) Đạn tới mép sau khoảng $2{,}5133\,\mathrm s$, với $v_y\approx-2{,}368\,\mathrm{m/s}$. Như vậy nó đang đi xuống. Hai vị trí toán học có $y=25{,}0\,\mathrm m$ là $x\approx48{,}46\,\mathrm m$ và $x=60{,}0\,\mathrm m$.

Vị trí đầu nằm trước vách và không phải mặt đất phía trên. Vị trí thứ hai chính là mép. Vì vậy ở tốc độ giới hạn, khoảng rơi vượt mép bằng $0\,\mathrm m$. Không chọn lại nghiệm đi lên ở trước vách làm điểm rơi.

</details>

### 3.53 (•, CP, CALC): Tên lửa đồ chơi có động cơ đẩy ngang

Một tên lửa đồ chơi được phóng ngang từ mái nhà cao $30{,}0\,\mathrm m$ với vận tốc đầu $12{,}0\,\mathrm{m/s}$. Động cơ tạo gia tốc ngang $(1{,}60\,\mathrm{m/s^3})t$, cùng chiều vận tốc ngang ban đầu. Gia tốc đứng vẫn là $g$ hướng xuống. Tên lửa đi ngang bao xa trước khi chạm đất?

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Hai phương có mô hình gia tốc khác nhau. Động cơ không tạo gia tốc đứng trong bài này.

**Hướng đi:** Tìm thời gian từ chuyển động rơi tự do theo phương đứng. Với phương ngang, cần tích phân gia tốc biến thiên thay vì dùng công thức gia tốc không đổi.

**Lời giải:** Thời gian bay là:

$$
t_f=\sqrt{\frac{2(30{,}0)}g}\approx2{,}4744\,\mathrm s.
$$

Theo phương ngang:

$$
v_x=12{,}0+0{,}800t^2,
$$

$$
x=12{,}0t+\frac{1{,}60}{6}t^3.
$$

Do đó $x(t_f)\approx33{,}7\,\mathrm m$.

</details>

### 3.54 (•••): Ném thiết bị tới tàu đang cập bến

Một thiết bị cần được ném tới mũi tàu trước khi tàu cập bến. Tàu chuyển động về bến với tốc độ $45{,}0\,\mathrm{cm/s}$. Thiết bị được ném từ đỉnh tháp ở mép nước, cao hơn boong $8{,}75\,\mathrm m$, với tốc độ $15{,}0\,\mathrm{m/s}$ và góc $60{,}0^\circ$ trên phương ngang. Khi ném, mũi tàu phải cách bến một khoảng $D$ bao nhiêu?

![Hình P3.54: Ném thiết bị từ tháp tới mũi tàu đang tiến về bến.](/vat-ly-1/bai-giang/img/young-03/r-numbered-late-p3-54.png)

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Vật ném và mũi tàu gặp nhau sau cùng một khoảng thời gian, tính từ lúc ném.

**Hướng đi:** Chuyển động đứng cho thời gian tới cao độ boong. Khi ấy tàu đã tiến một đoạn về bến, nên khoảng cách ban đầu lớn hơn tầm bay ngang của vật.

**Lời giải:** Đặt gốc tại điểm ném, $x$ dương về phía tàu. Nghiệm dương của:

$$
-8{,}75=15\sin60^\circ\,t-\frac g2t^2
$$

là $t\approx3{,}2078\,\mathrm s$. Tọa độ ngang của vật khi đó là $x\approx24{,}058\,\mathrm m$.

Đổi tốc độ tàu thành $u=0{,}450\,\mathrm{m/s}$. Điều kiện gặp nhau là $x=D-ut$, nên:

$$
D=x+ut\approx25{,}5\,\mathrm m.
$$

</details>

### 3.55 (••): Vận tốc bóng lúc chạm tòa nhà

Một quả bóng chày được ném ở góc $60{,}0^\circ$ trên phương ngang. Bóng chạm tòa nhà cách ngang $18{,}0\,\mathrm m$, tại điểm cao hơn vị trí ném $8{,}00\,\mathrm m$. (a) Tìm độ lớn vận tốc đầu. (b) Tìm độ lớn và hướng vận tốc ngay trước khi bóng chạm tòa nhà.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Vị trí chạm có độ cao dương so với điểm ném, nhưng bóng vẫn có thể đang đi xuống khi chạm.

**Hướng đi:** Dùng phương trình quỹ đạo để giải tốc độ đầu. Sau đó lấy thời gian từ chuyển động ngang và tính vận tốc đứng, giữ nguyên dấu để suy ra hướng.

**Lời giải:** (a) Đặt $d=18{,}0\,\mathrm m$, $h=8{,}00\,\mathrm m$ và $\theta=60{,}0^\circ$. Ta có:

$$
v_0^2=\frac{gd^2}{2\cos^2\theta(d\tan\theta-h)}.
$$

Kết quả $v_0\approx16{,}6\,\mathrm{m/s}$.

(b) Từ $t=d/(v_0\cos\theta)$ được $t\approx2{,}1749\,\mathrm s$. Các thành phần ngay trước va chạm là:

$$
v_x\approx8{,}276\,\mathrm{m/s},
$$

$$
\begin{aligned}
v_y &= v_0\sin\theta-gt \\
&\approx -6{,}978\,\mathrm{m/s}.
\end{aligned}
$$

Do đó tốc độ khoảng $10{,}8\,\mathrm{m/s}$, hướng chếch xuống $40{,}1^\circ$ so với phương ngang.

</details>

### 3.56 (••): Thả cỏ khô khi máy bay đang lên cao

Một máy bay thả những kiện cỏ khô cho đàn gia súc mắc kẹt trong bão tuyết trên đồng bằng. Lúc thả, máy bay cao $150\,\mathrm m$ so với mặt đất phẳng, bay với tốc độ $75\,\mathrm{m/s}$ theo hướng $55^\circ$ trên phương ngang. Phải thả kiện cỏ khi còn cách đàn gia súc bao xa theo phương ngang?

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Kiện cỏ lúc rời máy bay có cả vận tốc ngang lẫn vận tốc đứng hướng lên.

**Hướng đi:** Tách vận tốc máy bay thành hai thành phần. Thời gian chạm đất gồm cả thời gian kiện cỏ còn bay lên, nên không dùng thời gian rơi từ nghỉ ở độ cao 150 m.

**Lời giải:** Đặt $u_x=75\cos55^\circ$ và $u_y=75\sin55^\circ$, theo đơn vị mét trên giây. Phương trình đứng là:

$$
0=150+u_yt-\frac g2t^2.
$$

Nghiệm dương $t_f\approx14{,}63\,\mathrm s$ cho khoảng cách thả trước:

$$
d=u_xt_f\approx629\,\mathrm m.
$$

Với độ chính xác của các dữ kiện, có thể ghi khoảng $6{,}3\times10^2\,\mathrm m$.

</details>

### 3.57 (••): Châu chấu nhảy từ mép vách

Một con châu chấu nhảy khỏi mép vách đá thẳng đứng theo góc $50{,}0^\circ$ trên phương ngang. Đỉnh quỹ đạo cao hơn mép vách $6{,}74\,\mathrm{cm}$, còn điểm chạm đất cách chân vách theo phương ngang $1{,}06\,\mathrm m$. Tìm (a) tốc độ đầu và (b) chiều cao vách.

![Hình P3.57: Châu chấu nhảy khỏi vách đá, hình không theo đúng tỉ lệ.](/vat-ly-1/bai-giang/img/young-03/r-numbered-late-p3-57.png)

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Phải đổi $6{,}74\,\mathrm{cm}$ thành $0{,}0674\,\mathrm m$. Hình không vẽ đúng tỷ lệ.

**Hướng đi:** Độ tăng chiều cao tới đỉnh xác định vận tốc đứng ban đầu. Từ góc phóng suy ra tốc độ đầu và vận tốc ngang, rồi dùng khoảng ngang để tìm thời gian và chiều cao vách.

**Lời giải:** (a) Ở đỉnh, vận tốc đứng bằng không. Vì vậy:

$$
\begin{aligned}
u_y &= \sqrt{2g(0{,}0674)} \\
&\approx 1{,}1494\,\mathrm{m/s}.
\end{aligned}
$$

Từ đó:

$$
v_0=\frac{u_y}{\sin50^\circ}\approx1{,}50\,\mathrm{m/s}.
$$

(b) Thời gian tới đất là:

$$
t_f=\frac{1{,}06}{v_0\cos50^\circ}\approx1{,}0991\,\mathrm s.
$$

Nếu $H$ là chiều cao vách thì $-H=u_yt_f-gt_f^2/2$. Suy ra $H\approx4{,}66\,\mathrm m$.

</details>

### 3.58 (•••): Khoảng tốc độ để tia nước vào bồn

Một vòi nước ở cùng cao độ với đáy bồn trụ, cách thành gần của bồn $6D$. Bồn có đường kính $D$, cao $2D$. Vòi phun nghiêng $45^\circ$ trên phương ngang. Tìm khoảng tốc độ đầu để nước đi vào bồn, biểu diễn theo $D$ và $g$.

![Hình P3.58: Tia nước phải đi qua miệng bồn ở độ cao 2D.](/vat-ly-1/bai-giang/img/young-03/r-numbered-late-p3-58.png)

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Hai mép miệng bồn có tọa độ ngang $6D$ và $7D$, cùng cao độ $2D$.

**Hướng đi:** Đổi yêu cầu vào bồn thành hai điều kiện hình học. Tia phải ở trên mép gần nhưng đã xuống tới miệng bồn trước mép xa. Kiểm tra thêm tia đang đi xuống tại vùng miệng.

**Lời giải:** Với góc $45^\circ$, quỹ đạo là:

$$
y=x-\frac{gx^2}{v_0^2}.
$$

Để vừa vượt mép gần, $y(6D)\ge2D$, nên $v_0^2\ge9gD$. Để không bay qua mép xa, $y(7D)\le2D$, nên $v_0^2\le49gD/5$.

Vậy khoảng tốc độ giới hạn là:

$$
3\sqrt{gD}\le v_0\le7\sqrt{\frac{gD}{5}}.
$$

Trong khoảng này, độ dốc $dy/dx=1-2gx/v_0^2$ âm trên miệng bồn, nên lần cắt cao độ $2D$ đúng là nhánh đi xuống. Hai dấu bằng ứng với tia chạm đúng mép bồn. Muốn tia vào trong mà không chạm mép, dùng hai bất đẳng thức nghiêm.

</details>

### 3.59 (••): Tốc độ chạm đất có phụ thuộc góc ném?

Một vật được ném với tốc độ đầu $v_0$ từ mép mái nhà cao $H$. Vận tốc đầu tạo góc $\alpha_0$ với phương ngang. (a) Nếu $\alpha_0=90^\circ$, vật được ném thẳng lên và không chạm mái khi rơi xuống, tốc độ ngay trước khi chạm đất là bao nhiêu? (b) Trả lời cho $\alpha_0=-90^\circ$, tức ném thẳng xuống. (c) Tìm công thức cho góc tổng quát. (d) Nếu thay góc $\alpha_1$ bằng góc lớn hơn nhưng giữ $v_0$, tốc độ chạm đất tăng, giảm hay không đổi?

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Mọi trường hợp có cùng tốc độ đầu và cùng độ giảm độ cao. Dấu vận tốc đứng ban đầu có thể khác nhau.

**Hướng đi:** Hệ thức vận tốc đứng bình phương không cần biết thời gian. Cộng bình phương thành phần ngang để thấy phụ thuộc góc triệt tiêu.

**Lời giải:** (a), (b) Theo phương đứng:

$$
v_y^2=v_{0y}^2+2gH.
$$

Với ném thẳng lên hoặc xuống, $v_{0y}^2=v_0^2$. Cả hai trường hợp đều cho:

$$
v=\sqrt{v_0^2+2gH}.
$$

(c) Với góc bất kỳ, $v_x=v_0\cos\alpha_0$ không đổi. Do đó:

$$
\begin{aligned}
v^2&=v_x^2+v_y^2\\
&=v_0^2+2gH.
\end{aligned}
$$

Đã dùng $\cos^2\alpha_0+\sin^2\alpha_0=1$, nên vẫn được cùng công thức.

(d) Tốc độ chạm đất không đổi. Góc ném làm thay đổi thời gian bay và vị trí rơi, nhưng không thay đổi tốc độ cuối trong các giả thiết này.

</details>

### 3.60 (••): Sút bóng vừa qua xà ngang

Sau một lần ghi điểm trong bóng bầu dục Canada, đội có thể đá bóng qua xà giữa hai cột để ghi thêm một điểm. Xà cao $10{,}0\,\mathrm{ft}$, cách điểm đá trên mặt đất $36{,}0\,\mathrm{ft}$ theo phương ngang. Đổi sang SI để giải. (a) Tìm góc giới hạn mà nếu đá thấp hơn góc ấy thì bóng không thể qua xà dù tốc độ lớn đến đâu. (b) Nếu đá ở góc $45{,}0^\circ$, tốc độ đầu để vừa qua xà là bao nhiêu, tính bằng mét trên giây và kilômét trên giờ?

![Hình P3.60: Bóng được đá từ mặt đất để vượt xà ngang.](/vat-ly-1/bai-giang/img/young-03/r-numbered-late-p3-60.png)

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Dùng $1\,\mathrm{ft}=0{,}3048\,\mathrm m$. Bóng bay dưới đường tiếp tuyến ban đầu do trọng lực.

**Hướng đi:** Xét đường tiếp tuyến để tìm giới hạn hình học trước. Với góc đã cho ở phần (b), dùng độ cao quỹ đạo tại xà để giải tốc độ.

**Lời giải:** Đổi được $d=10{,}9728\,\mathrm m$ và $h=3{,}048\,\mathrm m$.

(a) Đường quỹ đạo nằm dưới đường $y=x\tan\theta$ với mọi tốc độ hữu hạn. Góc giới hạn thỏa:

$$
\theta_{\inf}=\arctan\frac hd\approx15{,}5^\circ.
$$

Muốn vượt xà bằng tốc độ hữu hạn phải có $\theta>\theta_{\inf}$. Ngay tại góc giới hạn, bóng chỉ tiệm cận độ cao xà khi tốc độ tăng không giới hạn.

(b) Với $\theta=45^\circ$:

$$
h=d-\frac{gd^2}{v_0^2}.
$$

Suy ra $v_0\approx12{,}2\,\mathrm{m/s}$, tương đương $43{,}9\,\mathrm{km/h}$.

</details>

### 3.61 (•••): Quả cầu tuyết rời mái dốc xuống

Một quả cầu tuyết lăn khỏi mái nhà kho nghiêng xuống $40^\circ$. Mép mái cao $14{,}0\,\mathrm m$, tốc độ quả cầu khi rời mái $7{,}00\,\mathrm{m/s}$. (a) Nếu không va vật khác, quả cầu chạm đất cách mép nhà bao xa? (b) Vẽ đồ thị hai tọa độ và hai thành phần vận tốc theo thời gian. (c) Một người cao $1{,}9\,\mathrm m$ đứng cách mép nhà $4{,}0\,\mathrm m$. Quả cầu có trúng người ấy không?

![Hình P3.61: Quả cầu tuyết rời mái dốc với vận tốc chếch xuống.](/vat-ly-1/bai-giang/img/young-03/r-numbered-late-p3-61.png)

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Chọn gốc ngang ở mép nhà, gốc đứng trên mặt đất. Góc vận tốc đầu so với chiều ngang dương là $-40^\circ$.

**Hướng đi:** Giữ dấu âm của thành phần đứng. Tìm nghiệm thời gian dương cho mặt đất. Để kiểm va người, cần tính độ cao tại đúng vị trí người đứng.

**Lời giải:** Các thành phần đầu là $u_x\approx5{,}3623\,\mathrm{m/s}$ và $u_y\approx-4{,}4995\,\mathrm{m/s}$.

(a) Các phương trình là:

$$
x=u_xt,
$$

$$
y=14{,}0+u_yt-\frac{1}{2}gt^2.
$$

Nghiệm $y=0$ dương cho $t_f\approx1{,}2924\,\mathrm s$, nên $x_f\approx6{,}93\,\mathrm m$.

(b) Vận tốc ngang không đổi, còn $v_y=u_y-gt$ âm và giảm tiếp. Đồ thị đứng bắt đầu bằng độ dốc âm, không có giai đoạn bay lên.

![Bốn đồ thị của quả cầu tuyết với độ cao giảm ngay từ đầu và vận tốc đứng ban đầu âm](/vat-ly-1/bai-giang/img/young-03/solution-s3-61.svg)


(c) Tại $x=4{,}0\,\mathrm m$, thời gian là $t=x/u_x\approx0{,}74595\,\mathrm s$. Độ cao khi ấy khoảng $7{,}92\,\mathrm m$, lớn hơn $1{,}9\,\mathrm m$, nên quả cầu bay qua phía trên người ấy.

</details>

### 3.62 (•): Người chạy đón bóng từ vách cao

Một quả bóng khối lượng $2{,}7\,\mathrm{kg}$ được ném chếch lên với tốc độ $20{,}0\,\mathrm{m/s}$ từ mép vách cao $45{,}0\,\mathrm m$. Đúng lúc ném, một người phụ nữ bắt đầu chạy thẳng ra xa chân vách trên đất phẳng với tốc độ không đổi $6{,}00\,\mathrm{m/s}$. (a) Phải ném góc bao nhiêu để cô bắt được bóng ngay trước khi bóng chạm đất? Cô chạy bao xa? (b) Phác quỹ đạo bóng đối với người đứng yên trên mặt đất và đối với chính người chạy.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Bóng và người bắt đầu cùng lúc trên cùng đường thẳng đứng. Khối lượng bóng không ảnh hưởng quỹ đạo trong mô hình này.

**Hướng đi:** Muốn hai vật có cùng vị trí ngang ở một thời điểm dương, vận tốc ngang của bóng phải bằng tốc độ người chạy. Sau đó chọn thành phần đứng dương theo yêu cầu ném lên.

**Lời giải:** (a) Điều kiện gặp nhau cho $20\cos\theta=6{,}00$, nên:

$$
\theta\approx72{,}5^\circ.
$$

Vận tốc đứng ban đầu $u_y\approx19{,}0788\,\mathrm{m/s}$. Giải:

$$
0=45{,}0+u_yt-\frac g2t^2
$$

được $t_f\approx5{,}5487\,\mathrm s$. Người chạy được $6{,}00t_f\approx33{,}3\,\mathrm m$.

(b) Trong hệ mặt đất, bóng đi theo parabol, còn người chạy giữ vị trí ngay dưới bóng. Trong hệ người chạy:

$$
x'=x-6{,}00t=0.
$$

Bóng đi thẳng đứng lên rồi xuống. Hình quỹ đạo thẳng đứng không có nghĩa tốc độ đứng không đổi.

 Cùng chuyển động có hình dạng quỹ đạo khác nhau trong hai hệ quy chiếu.

![Quỹ đạo của bóng trong hệ mặt đất và hệ người chạy](/vat-ly-1/bai-giang/img/young-03/solution-s3-62.svg)



</details>

### 3.63 (••): Xe máy cố vượt sông

Một giảng viên vật lý làm các màn biểu diễn mạo hiểm trong thời gian rảnh. Lần cuối, ông định nhảy qua sông bằng xe máy. Dốc phóng nghiêng $53{,}0^\circ$, sông rộng $40{,}0\,\mathrm m$, bờ bên kia thấp hơn đỉnh dốc $15{,}0\,\mathrm m$. Mặt sông thấp hơn đỉnh dốc $100\,\mathrm m$. (a) Tốc độ ở đầu dốc phải bằng bao nhiêu để vừa tới mép bờ bên kia? (b) Nếu tốc độ chỉ bằng nửa giá trị ấy thì ông rơi ở đâu?

![Hình P3.63: Đường phóng qua sông, cao độ bờ xa và mặt nước.](/vat-ly-1/bai-giang/img/young-03/r-numbered-late-p3-63.png)

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Đặt gốc tại đầu dốc. Đích phần (a) có tọa độ $(40{,}0;-15{,}0)$ theo đơn vị mét.

**Hướng đi:** Giải tốc độ từ vị trí đích. Với tốc độ bị giảm ở phần (b), tìm giao điểm với mặt nước và kiểm tra nó nằm trước hay sau bờ bên kia.

**Lời giải:** (a) Đặt $d=40{,}0\,\mathrm m$, $h=-15{,}0\,\mathrm m$, $\theta=53{,}0^\circ$. Từ phương trình quỹ đạo:

$$
v_0^2=\frac{gd^2}{2\cos^2\theta(d\tan\theta-h)}.
$$

Suy ra $v_0\approx17{,}8\,\mathrm{m/s}$.

(b) Với $u=v_0/2\approx8{,}916\,\mathrm{m/s}$, giải phương trình đứng:

$$
-100=u\sin53^\circ\,t-\frac g2t^2.
$$

Nghiệm dương khoảng $5{,}3022\,\mathrm s$ cho $x\approx28{,}45\,\mathrm m$. Giá trị này nhỏ hơn bề rộng sông, nên ông rơi xuống nước, cách chân vách bên xuất phát khoảng $28{,}4\,\mathrm m$. Không dùng giao điểm với cao độ bờ xa để kết luận đã tới bờ.

</details>

### 3.64 (••): Ném túi đồ ăn cho người đang chạy

Henrietta chạy trên vỉa hè với tốc độ $3{,}05\,\mathrm{m/s}$ trên đường tới lớp vật lý. Bruce phát hiện cô quên túi bánh, chạy ra cửa sổ cao $38{,}0\,\mathrm m$ ngay trên vỉa hè và ném túi theo phương ngang. Anh ném sau khi cô đi qua dưới cửa sổ $9{,}00\,\mathrm s$, và cô bắt được khi vẫn đang chạy. (a) Tốc độ ném phải bằng bao nhiêu để cô bắt ngay trước khi túi chạm đất? (b) Lúc bắt túi cô ở đâu?

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Thời gian trễ 9 giây thuộc chuyển động của người chạy trước lúc túi bắt đầu bay.

**Hướng đi:** Lấy mốc thời gian tại lúc ném. Thời gian rơi xác định từ độ cao, còn vị trí người chạy có thêm quãng đường đi trước.

**Lời giải:** Thời gian rơi là:

$$
t_f=\sqrt{\frac{2(38{,}0)}g}\approx2{,}7848\,\mathrm s.
$$

(a) Điều kiện vị trí ngang bằng nhau là:

$$
v_0t_f=3{,}05(9{,}00+t_f).
$$

Suy ra $v_0\approx12{,}9\,\mathrm{m/s}$, cùng chiều chạy.

(b) Vị trí bắt cách điểm ngay dưới cửa sổ khoảng $35{,}9\,\mathrm m$ về phía trước.

</details>

### 3.65 (•): Hòn đá vượt đập tới vùng đất thấp

Một hòn đá khối lượng $76{,}0\,\mathrm{kg}$ lăn ngang khỏi đỉnh vách cao $20\,\mathrm m$ trên mặt hồ. Mặt đứng của một con đập cách chân vách $100\,\mathrm m$, đỉnh đập ngang mặt hồ. Vùng đất phẳng sau đập thấp hơn đỉnh đập $25\,\mathrm m$. (a) Tốc độ nhỏ nhất khi rời vách để đá tới vùng đất mà không đập vào mặt đập là bao nhiêu? (b) Đá chạm đất cách chân đập bao xa?

![Hình P3.65: Vách đá, mặt hồ, đập và vùng đất thấp phía sau.](/vat-ly-1/bai-giang/img/young-03/r-numbered-late-p3-65.png)

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Vận tốc đứng ban đầu bằng không. Ngưỡng vừa vượt đập ứng với giảm độ cao 20 mét sau khi đi ngang 100 mét.

**Hướng đi:** Tìm thời gian rơi tới cao độ đỉnh đập để suy ra tốc độ ngang giới hạn. Khi tìm điểm rơi cuối, phải dùng độ giảm độ cao tổng cộng chứ không chỉ 25 mét.

**Lời giải:** (a) Thời gian rơi $20\,\mathrm m$ là $t_d=\sqrt{40/g}$. Do đó:

$$
u_{\inf}=\frac{100}{t_d}\approx49{,}5\,\mathrm{m/s}.
$$

Đây là giới hạn tia đi qua đúng góc trên của đập. Muốn có khoảng hở thực sự cần tốc độ lớn hơn ngưỡng này.

(b) Tới vùng đất, đá đã rơi tổng cộng $45\,\mathrm m$, nên $t_f=\sqrt{90/g}$. Tại tốc độ giới hạn, $x_f=150\,\mathrm m$ tính từ vách ban đầu. Vì vậy điểm rơi cách chân đập $50\,\mathrm m$.

</details>

### 3.66 (••): Hai vị trí đặt vòi rồng

Một đội chữa cháy dùng vòi rồng phun nước với tốc độ $25{,}0\,\mathrm{m/s}$ ở góc cố định $53{,}0^\circ$ trên phương ngang. Đám cháy nằm trên tòa nhà ở độ cao $10{,}0\,\mathrm m$ so với mặt đất. Có hai khoảng cách từ vòi tới nhà để tia nước trúng đích. Tìm cả hai và phác quỹ đạo.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Góc và tốc độ phun cố định. Cùng một cao độ có thể cắt cả nhánh lên lẫn nhánh xuống.

**Hướng đi:** Giải phương trình đứng để lấy cả hai nghiệm thời gian dương. Kiểm tra cao độ đích thấp hơn đỉnh quỹ đạo, rồi chuyển mỗi nghiệm thành khoảng ngang.

**Lời giải:** Đặt $u_x=25\cos53^\circ$, $u_y=25\sin53^\circ$, theo đơn vị mét trên giây. Điều kiện tới đám cháy:

$$
10{,}0=u_yt-\frac g2t^2.
$$

Hai nghiệm là $t_1\approx0{,}58478\,\mathrm s$ và $t_2\approx3{,}48989\,\mathrm s$. Cả hai đều dương. Từ $x=u_xt$ được hai khoảng cách:

$$
x_1\approx8{,}80\,\mathrm m,
$$

$$
x_2\approx52{,}5\,\mathrm m.
$$

Đỉnh quỹ đạo cao khoảng $20{,}34\,\mathrm m$, vượt cao độ đích. Vị trí gần tương ứng nước đang lên, vị trí xa tương ứng nước đang xuống.

 Hai nghiệm đều có ý nghĩa hình học.

![Hai điểm của quỹ đạo tia nước cùng ở độ cao 10 mét](/vat-ly-1/bai-giang/img/young-03/solution-s3-66.svg)



</details>

### 3.67 (••): Dùng tốc độ ở đỉnh để tìm thời gian bay

Một quả bóng được phóng từ mặt sân bóng đá phẳng. Ở điểm cao nhất, tốc độ bóng là $8{,}0\,\mathrm{m/s}$. Tầm xa ngang bằng $50{,}0\,\mathrm m$. Bóng ở trên không bao lâu?

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Tại đỉnh, vận tốc đứng bằng không. Vận tốc ngang không đổi trong suốt chuyến bay.

**Hướng đi:** Tốc độ ở đỉnh chính là độ lớn vận tốc ngang. Chia toàn bộ tầm xa cho thành phần ấy để tìm toàn bộ thời gian bay.

**Lời giải:** Ta có $v_x=8{,}0\,\mathrm{m/s}$, nên:

$$
T=\frac{50{,}0}{8{,}0}=6{,}25\,\mathrm s.
$$

Theo độ chính xác dữ kiện, thời gian khoảng $6{,}3\,\mathrm s$.

</details>

### 3.68 (•••): Vật trượt ngang rồi rơi xuống mặt dốc

Bạn đứng trên bến bốc hàng ở đầu một mặt dốc phẳng nghiêng góc $\alpha_0$ dưới phương ngang. Một hộp nhỏ trượt ngang khỏi bến với tốc độ $v_0$, theo hướng để rơi lên mặt dốc. Hộp giảm độ cao bao nhiêu trước khi chạm dốc?

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Mặt dốc và quỹ đạo cùng đi qua điểm phóng. Xét $0<\alpha_0<90^\circ$.

**Hướng đi:** Viết phương trình mặt dốc và quỹ đạo trong cùng hệ tọa độ. Bỏ nghiệm tại lúc rời bến, vì cần lần gặp tiếp theo.

**Lời giải:** Chọn gốc tại điểm rời bến. Hộp có $x=v_0t$, $y=-gt^2/2$, còn dốc có $y=-x\tan\alpha_0$. Điều kiện gặp là:

$$
\frac g2t^2=v_0t\tan\alpha_0.
$$

Nghiệm dương khác không:

$$
t=\frac{2v_0\tan\alpha_0}{g}.
$$

Độ giảm độ cao là:

$$
\Delta h=\frac{gt^2}{2}=\frac{2v_0^2\tan^2\alpha_0}{g}.
$$

Ở góc bằng không, nghiệm dương biến mất. Khi mặt dốc tiến tới thẳng đứng, mô hình giao điểm ở khoảng cách hữu hạn này không còn áp dụng.

</details>

### 3.69 (•••): Ném đá qua hàng rào

Bạn đứng cách hàng rào cao $5{,}00\,\mathrm m$ một khoảng ngang $14{,}0\,\mathrm m$, trên nền đất phẳng. Một lời nhắn quan trọng được buộc vào hòn đá. Bạn ném đá từ độ cao $1{,}60\,\mathrm m$, ở góc $56{,}0^\circ$ trên phương ngang. Bỏ qua bề dày rào. (a) Tốc độ đầu nhỏ nhất để vừa qua rào là bao nhiêu? (b) Với tốc độ ấy, đá rơi xuống đất cách rào về phía bên kia bao xa?

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Độ cao rào so với điểm ném là $3{,}40\,\mathrm m$, còn mặt đất thấp hơn điểm ném $1{,}60\,\mathrm m$.

**Hướng đi:** Hai điều kiện độ cao dùng hai mốc khác nhau. Tìm tốc độ giới hạn từ vị trí mép rào, rồi tìm thời gian tới mặt đất để tính khoảng rơi vượt rào.

**Lời giải:** (a) Đặt $d=14{,}0\,\mathrm m$, $h=3{,}40\,\mathrm m$, $\theta=56{,}0^\circ$. Phương trình quỹ đạo cho:

$$
h=d\tan\theta-\frac{gd^2}{2v_0^2\cos^2\theta}.
$$

Giải được $v_{0,\min}\approx13{,}30\,\mathrm{m/s}$. Dấu bằng là trường hợp giới hạn đi qua mép rào, còn muốn không chạm mép cần tốc độ nhỉnh hơn.

(b) Với tốc độ này, phương trình tới mặt đất là:

$$
-1{,}60=v_0\sin\theta\,t-\frac g2t^2.
$$

Nghiệm dương $t_f\approx2{,}3875\,\mathrm s$ cho tầm ngang từ chỗ ném $x_f\approx17{,}760\,\mathrm m$. Vì vậy đá rơi cách rào khoảng $3{,}76\,\mathrm m$ về phía bên kia.

</details>

### 3.70 (•••): Tỷ lệ độ cao dọc quỹ đạo ném

Một vật được phóng từ mặt đất phẳng với tốc độ $16{,}0\,\mathrm{m/s}$, ở góc $60{,}0^\circ$. (a) Khi lên cao nhất, vật đã đi ngang bao xa? So sánh với tầm xa $R$. (b) Khi đã đi ngang $80{,}0\%$ tầm xa, độ cao bằng bao nhiêu và bằng phần nào độ cao cực đại $h_{\max}$? (c) Với độ dời ngang $x-x_0=\alpha R$, $\alpha>0$, tìm tỷ số độ cao trên $h_{\max}$ chỉ theo $\alpha$. Kiểm tra với $\alpha=0{,}80$, $0$, $0{,}50$ và $1{,}0$.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Điểm phóng và điểm rơi cùng độ cao. Tầm xa và độ cao cực đại có thể dùng để chuẩn hóa toàn bộ parabol.

**Hướng đi:** Viết phương trình quỹ đạo bằng tầm xa thay cho hệ số tốc độ. Tỷ số độ cao sẽ loại cả góc lẫn tốc độ đầu, cho quan hệ hình dạng chung.

**Lời giải:** (a) Với $u_x=v_0\cos\theta$, $u_y=v_0\sin\theta$, thời gian tới đỉnh bằng $u_y/g$. Toàn bộ thời gian bay bằng $2u_y/g$, nên đỉnh có $x-x_0=R/2$.

Tính được $R\approx22{,}62\,\mathrm m$, vì vậy độ dời ngang tới đỉnh khoảng $11{,}31\,\mathrm m$.

(b) Độ cao cực đại bằng:

$$
h_{\max}=\frac{u_y^2}{2g}\approx9{,}796\,\mathrm m.
$$

Tại $0{,}800R$, độ cao khoảng $6{,}269\,\mathrm m$, bằng $0{,}640h_{\max}$.

(c) Chọn gốc tại điểm phóng. Vì $R=2u_xu_y/g$, phương trình quỹ đạo viết được:

$$
y=x\tan\theta\left(1-\frac xR\right).
$$

Mặt khác, $h_{\max}=R\tan\theta/4$. Thay $x=\alpha R$ cho:

$$
\frac{y-y_0}{h_{\max}}=4\alpha(1-\alpha).
$$

Với $\alpha=0{,}80$, tỷ số bằng $0{,}64$. Các giá trị $0$, $0{,}50$, $1{,}0$ lần lượt cho tỷ số $0$, $1$, $0$, đúng với hai đầu quỹ đạo và đỉnh. Trong chuyến bay thực phía trên mặt đất, $0\le\alpha\le1$.

</details>

### 3.71 (••): Suy ra gió từ hành trình máy bay

Một phi công giữ mũi máy bay hướng tây và tốc độ đối với không khí $220\,\mathrm{km/h}$. Sau $0{,}500\,\mathrm h$, máy bay ở trên một thị trấn cách điểm đầu $120\,\mathrm{km}$ về tây và $20\,\mathrm{km}$ về nam. (a) Tìm độ lớn và hướng vận tốc gió. (b) Trong trường hợp gió thổi về nam với tốc độ $40\,\mathrm{km/h}$, phi công phải hướng mũi về đâu để đi đúng về tây, nếu tốc độ đối với không khí vẫn là $220\,\mathrm{km/h}$?

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Phần (a) suy gió từ vận tốc mặt đất. Phần (b) cho một trường hợp gió mới.

**Hướng đi:** Dùng cộng vector vận tốc giữa máy bay, không khí và mặt đất. Không đồng nhất hướng mũi máy bay với hướng đường bay trên mặt đất.

**Lời giải:** Chọn $x$ về đông, $y$ về bắc. Ký hiệu P là máy bay, A là không khí và E là mặt đất. Ta có:

$$
\vec v_{P/E}=\vec v_{P/A}+\vec v_{A/E}.
$$

(a) Vận tốc mặt đất có hai thành phần $(-240;-40)$, theo đơn vị kilômét trên giờ. Vận tốc máy bay đối với không khí là $(-220;0)$, nên gió có thành phần $(-20;-40)$.

Độ lớn gió khoảng $44{,}7\,\mathrm{km/h}$, hướng $63{,}4^\circ$ về nam so với hướng tây.

(b) Muốn thành phần bắc trên mặt đất bằng không, máy bay cần thành phần bắc đối với không khí bằng $40\,\mathrm{km/h}$. Nếu mũi nghiêng góc $\phi$ về bắc từ hướng tây:

$$
\sin\phi=\frac{40}{220}.
$$

Suy ra $\phi\approx10{,}5^\circ$ về bắc so với hướng tây.

</details>

### 3.72 (••): Mưa nhìn từ toa tàu

Một tàu chạy về đông với tốc độ $12{,}0\,\mathrm{m/s}$. Các giọt mưa rơi thẳng đứng đối với mặt đất nhưng để lại vệt nghiêng $30{,}0^\circ$ với phương đứng trên cửa kính tàu. (a) Thành phần vận tốc ngang của giọt mưa đối với mặt đất và đối với tàu là bao nhiêu? (b) Tốc độ của giọt mưa trong hai hệ ấy bằng bao nhiêu?

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Vệt trên kính biểu diễn hướng vận tốc tương đối của mưa đối với tàu.

**Hướng đi:** Trừ vận tốc tàu khỏi vận tốc mưa trong hệ mặt đất. Góc được đo từ phương đứng, nên tỷ số lượng giác là thành phần ngang chia độ lớn thành phần đứng.

**Lời giải:** (a) Lấy chiều đông dương. Đối với mặt đất, $v_x=0$. Đối với tàu, $v'_x=0-12{,}0=-12{,}0\,\mathrm{m/s}$, tức về tây.

(b) Gọi độ lớn vận tốc đứng là $w$. Biến đổi Galile không đổi thành phần đứng trong hai hệ này. Từ vệt mưa:

$$
\tan30^\circ=\frac{12{,}0}{w}.
$$

Vậy $w\approx20{,}8\,\mathrm{m/s}$, chính là tốc độ mưa đối với mặt đất. Đối với tàu:

$$
\begin{aligned}
v' &= \sqrt{w^2+12{,}0^2} \\
&= 24{,}0\,\mathrm{m/s}.
\end{aligned}
$$

</details>

### 3.73 (•••): Vận tốc bóng đối với cầu thủ

Trong một trận bóng đá, Juan chạy về bắc hướng tới cầu môn với tốc độ $8{,}00\,\mathrm{m/s}$ đối với mặt đất. Đồng đội chuyền bóng cho anh. Bóng có tốc độ $12{,}0\,\mathrm{m/s}$, hướng $37{,}0^\circ$ về đông so với hướng bắc trong hệ mặt đất. Tìm độ lớn và hướng vận tốc bóng đối với Juan.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Hai vận tốc đã biết đều đo trong cùng hệ mặt đất. Cần đổi sang hệ Juan.

**Hướng đi:** Trừ theo từng thành phần. Vì bóng chuyển động chếch, không được lấy hiệu trực tiếp của hai tốc độ.

**Lời giải:** Chọn đông và bắc làm hai chiều dương. Thành phần bóng đối với Juan là:

$$
\begin{aligned}
v'_x &= 12\sin 37^\circ \\
&\approx 7{,}222\,\mathrm{m/s},
\end{aligned}
$$

$$
\begin{aligned}
v'_y &= 12\cos 37^\circ-8 \\
&\approx 1{,}584\,\mathrm{m/s}.
\end{aligned}
$$

Độ lớn khoảng $7{,}39\,\mathrm{m/s}$. Cả hai thành phần dương, nên hướng nằm ở đông bắc, cụ thể $77{,}6^\circ$ về đông so với hướng bắc, hay $12{,}4^\circ$ về bắc so với hướng đông.

</details>

### 3.74 (••): Tốc độ người ném đang chạy ngang

Một cầu thủ bóng chày chạy về đông trong lúc ném bóng cho người bắt đứng yên tại vị trí đích. Đối với người ném, bóng có vận tốc $6{,}00\,\mathrm{m/s}$ về nam. Người bắt đo tốc độ bóng $9{,}00\,\mathrm{m/s}$. Tốc độ người ném đối với mặt đất là bao nhiêu?

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Người bắt đứng yên trên mặt đất. Thành phần vận tốc do người ném chạy vuông góc với vận tốc bóng đối với người ném.

**Hướng đi:** Cộng vận tốc của bóng đối với người ném với vận tốc người ném đối với đất. Vì hai thành phần vuông góc, bình phương tốc độ tuân theo định lý Pythagore.

**Lời giải:** Nếu tốc độ người ném là $u$, vận tốc bóng trong hệ đất có thành phần đông bằng $u$ và thành phần nam bằng $6{,}00\,\mathrm{m/s}$. Do đó:

$$
u^2+6{,}00^2=9{,}00^2.
$$

Lấy căn dương được $u\approx6{,}71\,\mathrm{m/s}$ về đông.

</details>

### 3.75 (••): Cộng vận tốc bóng và người nhận

Hai cầu thủ Mia và Alice đều đang chạy khi Alice chuyền bóng cho Mia. Mia chạy về bắc với tốc độ $6{,}00\,\mathrm{m/s}$. Vận tốc bóng đối với Mia có độ lớn $5{,}00\,\mathrm{m/s}$, hướng $30{,}0^\circ$ về đông so với hướng nam. Tìm độ lớn và hướng vận tốc bóng đối với mặt đất.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Dữ kiện cho vận tốc bóng đối với Mia, không phải đối với Alice.

**Hướng đi:** Cộng vận tốc Mia đối với đất vào vận tốc tương đối đã cho. Chuyển hướng đông của nam thành thành phần đông dương và bắc âm.

**Lời giải:** Các thành phần của bóng trong hệ đất là:

$$
v_x=5\sin30^\circ=2{,}50\,\mathrm{m/s},
$$

$$
\begin{aligned}
v_y &= 6-5\cos 30^\circ \\
&\approx 1{,}670\,\mathrm{m/s}.
\end{aligned}
$$

Vì thế tốc độ bóng khoảng $3{,}01\,\mathrm{m/s}$, hướng $56{,}3^\circ$ về đông so với hướng bắc. Không cần biết vận tốc Alice vì vận tốc tương đối đã đo với Mia.

</details>

### 3.76 (••, DATA): Ước lượng tốc độ súng lò xo từ đồ thị

Một súng lò xo phóng viên đá nhỏ từ gần mặt đất với tốc độ $v_0$, ở góc $\theta_0$. Cấu tạo súng khiến tốc độ đầu gần như độc lập với góc phóng. Trên bãi đất phẳng, bạn đo tầm xa cho nhiều góc và thu được đồ thị trong Hình 3.76. Các phép đo góc và tầm xa có sai số. Bỏ độ cao nhỏ của miệng nòng và bỏ lực cản trong mô hình, với $g=9{,}80\,\mathrm{m/s^2}$, không có gió và viên đá nhỏ, nặng. (a) Chọn cách biểu diễn dữ liệu gần đường thẳng. (b) Dùng hệ số góc của đường khớp tốt nhất để tính $v_0$. (c) Khi góc phóng $36{,}9^\circ$, viên đá lên cao tối đa bao nhiêu?

![Hình P3.76: Mười một điểm đo tầm xa theo góc phóng.](/vat-ly-1/bai-giang/img/young-03/r-numbered-late-p3-76.png)

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Các dữ liệu được cho bằng đồ thị, nên kết quả đọc tọa độ điểm là gần đúng. Kết quả suy từ vị trí chấm phải được hiểu là ước lượng.

**Hướng đi:** Tầm xa trên nền phẳng tỷ lệ với sin của hai lần góc phóng. Chuyển biến góc theo quan hệ ấy rồi khớp đường thẳng, dùng toàn bộ các điểm thay vì chỉ điểm cao nhất.

**Lời giải:** (a) Đặt $X=\sin(2\theta_0)$ và $Y=R$. Công thức tầm xa cho:

$$
Y=sX,\qquad s=\frac{v_0^2}{g}.
$$

Đọc xấp xỉ vị trí 11 chấm rồi khớp $Y=sX+b$ không ép tung độ gốc. Kết quả khoảng $s=10{,}95\,\mathrm m$, $b=0{,}04\,\mathrm m$. Tung độ gốc gần không phù hợp với mô hình lý tưởng.

![Các điểm tầm xa theo sin hai lần góc phóng nằm gần đường hồi quy tuyến tính](/vat-ly-1/bai-giang/img/young-03/solution-s3-76.svg)


(b) Từ hệ số góc:

$$
v_0=\sqrt{gs}\approx10{,}4\,\mathrm{m/s}.
$$

Không nên diễn giải các chữ số từ việc đọc hình như độ chính xác của phép đo gốc.

(c) Với $\theta_0=36{,}9^\circ$:

$$
h_{\max}=\frac{v_0^2\sin^2\theta_0}{2g}\approx2{,}0\,\mathrm m.
$$

</details>

### 3.77 (••, DATA): Đo tốc độ đầu từ các lần phóng ngang

Bạn chế tạo súng phóng khoai tây dùng khí cháy từ keo xịt tóc. Mỗi lần dùng cùng lượng keo, và các lần phóng lặp ở cùng độ cao xác nhận tốc độ đầu gần như nhau. Sau khi được phép lên một tháp tiếp sóng, bạn phóng ngang từ các độ cao khác nhau. Người bạn đo độ cao nòng và tầm xa:

| Độ cao $h$ (m) | Tầm xa $R$ (m) |
| --- | --- |
| $2{,}00$ | $10{,}4$ |
| $6{,}00$ | $17{,}1$ |
| $9{,}00$ | $21{,}3$ |
| $12{,}00$ | $25{,}8$ |

Các số đo có sai số vì tốc độ không hoàn toàn lặp lại và nòng không hoàn toàn ngang. Dùng toàn bộ dữ liệu để ước lượng, lấy $g=9{,}80\,\mathrm{m/s^2}$ và bỏ lực cản trong điều kiện không có gió của mô hình. (a) Chọn cách biểu diễn gần đường thẳng. (b) Dùng hệ số góc để tìm tốc độ đầu trung bình. (c) Với tốc độ ấy, tầm xa khi phóng từ mặt đất ở góc $30{,}0^\circ$ là bao nhiêu?

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Các dữ liệu đều là phóng ngang từ độ cao dương. Phần (c) chuyển sang phóng chếch từ mặt đất.

**Hướng đi:** Từ thời gian rơi, bình phương tầm xa để tuyến tính hóa theo độ cao. Cùng tốc độ đầu được dùng lại khi đổi góc và độ cao ở phần (c).

**Lời giải:** (a) Vì $t=\sqrt{2h/g}$ và $R=v_0t$, ta có:

$$
R^2=\frac{2v_0^2}{g}h.
$$

Chọn trục hoành $h$, trục tung $R^2$. Khớp $R^2=sh+b$ không ép qua gốc cho $s\approx55{,}20\,\mathrm m$ và $b\approx-20{,}25\,\mathrm{m^2}$. Tung độ gốc phản ánh sai lệch của bộ dữ liệu đối với quan hệ lý tưởng.

![Bốn điểm bình phương tầm xa theo độ cao và đường hồi quy tuyến tính dùng mọi số đo](/vat-ly-1/bai-giang/img/young-03/solution-s3-77.svg)


(b) Từ $s=2v_0^2/g$:

$$
v_0=\sqrt{\frac{gs}{2}}\approx16{,}4\,\mathrm{m/s}.
$$

(c) Phóng từ mặt đất, tầm xa là:

$$
R_{30}=\frac{v_0^2\sin60^\circ}{g}\approx23{,}9\,\mathrm m.
$$

Đây là ước lượng theo phép khớp đã chọn, chưa phải xác định độ không đảm bảo khi chưa có mô hình sai số đo.

</details>

### 3.78 (•••, DATA): Suy chiều rộng và dòng chảy của sông

Một nhóm địa chất ở Trung Phi cần đo bề rộng sông và tốc độ dòng chảy về đông. Bạn có thuyền máy đã hiệu chuẩn tốc độ theo mức ga trên ao nước đứng yên. Lượt đi, tốc độ thuyền đối với nước là $6{,}00\,\mathrm{m/s}$, thuyền đi đúng về bắc trong hệ mặt đất và qua sông trong $20{,}1\,\mathrm s$. Lượt về, tốc độ đối với nước là $9{,}00\,\mathrm{m/s}$, thuyền đi đúng về nam và qua trong $11{,}2\,\mathrm s$. (a) Tìm bề rộng sông và tốc độ dòng chảy. (b) Với tốc độ đối với nước $6{,}00\,\mathrm{m/s}$, thời gian qua sông ngắn nhất là bao nhiêu và thuyền tới đâu trên bờ bên kia?

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Hướng bắc và nam của hai lượt đầu là hướng vận tốc đối với mặt đất, không phải hướng mũi thuyền.

**Hướng đi:** Muốn đi thẳng ngang sông, thuyền phải dành một thành phần vận tốc để triệt dòng. Hai thời gian qua cùng một bề rộng tạo hai phương trình tìm dòng chảy. Khi chỉ cần thời gian ngắn nhất, không còn phải triệt độ trôi.

**Lời giải:** (a) Gọi $w$ là bề rộng và $c$ là tốc độ dòng chảy. Đặt $t_1=20{,}1\,\mathrm s$, $t_2=11{,}2\,\mathrm s$, $u_1=6{,}00\,\mathrm{m/s}$, $u_2=9{,}00\,\mathrm{m/s}$. Thành phần ngang sông cho:

$$
\frac{w^2}{t_1^2}+c^2=u_1^2,
$$

$$
\frac{w^2}{t_2^2}+c^2=u_2^2.
$$

Trừ hai phương trình rồi giải, chọn nghiệm $w>0$ và $0<c<u_1$, được $w\approx90{,}5\,\mathrm m$ và $c\approx3{,}97\,\mathrm{m/s}$ về đông.

(b) Thời gian ngắn nhất đạt khi mũi thuyền hướng vuông góc bờ, tức về bắc đối với nước. Khi ấy thành phần bắc trong hệ đất bằng toàn bộ $u_1$, nên:

$$
t_{\min}=\frac w{u_1}\approx15{,}1\,\mathrm s.
$$

Thuyền trôi về đông một đoạn $ct_{\min}\approx59{,}8\,\mathrm m$ so với điểm đối diện điểm xuất phát.

</details>

## Bài tập nâng cao

### 3.79 (•••, CALC): Góc phóng cực đại để khoảng cách luôn tăng

Một vật ném được phóng từ một điểm $P$ chuyển động sao cho khoảng cách từ vật tới điểm $P$ luôn luôn tăng theo thời gian. Bỏ qua lực cản không khí. Tìm góc phóng cực đại phía trên phương ngang để chuyển động thỏa mãn tính chất này.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Chất điểm ném trong trường trọng lực đều từ điểm $P$. Cần tìm góc phóng $\theta_0$ lớn nhất sao cho khoảng cách $r(t)$ từ chất điểm tới $P$ là hàm đơn điệu tăng với mọi $t>0$.

**Hướng đi:** Chọn gốc tọa độ tại điểm phóng $P$. Thiết lập biểu thức khoảng cách bình phương $r^2(t)=x^2+y^2$. Điều kiện khoảng cách luôn tăng tương đương với đạo hàm của $r^2(t)$ theo thời gian luôn không âm với mọi $t>0$. Khảo sát đa thức bậc hai sau khi triệt tiêu thừa số $t$ để tìm điều kiện của biệt thức $\Delta\le 0$.

**Lời giải:** Chọn gốc tọa độ tại điểm phóng $P$, trục $Ox$ nằm ngang, trục $Oy$ thẳng đứng hướng lên. Tọa độ của vật tại thời điểm $t$:

$$
x=(v_0\cos\theta_0)t,
$$

$$
y=(v_0\sin\theta_0)t-\frac{1}{2}gt^2.
$$

Khoảng cách từ vật tới điểm phóng $P$ là $r(t)=\sqrt{x^2+y^2}$. Vì $r(t)>0$ với mọi $t>0$, điều kiện $r(t)$ luôn tăng tương đương với $r^2(t)$ luôn tăng, tức là:

$$
\frac{d(r^2)}{dt}\ge 0\quad\forall t>0.
$$

Khai triển và lấy đạo hàm theo thời gian:

$$
\frac{d(r^2)}{dt}=t\cdot Q(t),
$$

trong đó $Q(t)$ là tam thức bậc hai:

$$
Q(t)=g^2t^2-Bt+2v_0^2,
$$

với hệ số bậc nhất:

$$
B=3gv_0\sin\theta_0.
$$

Với $t>0$, điều kiện khoảng cách luôn tăng tương đương với $Q(t)\ge 0$ với mọi $t>0$.

Nhận xét: Tại $t=0$, $Q(0)=2v_0^2>0$, và hệ số bậc hai $g^2>0$. Để $Q(t)$ luôn không âm với mọi $t>0$, tam thức không được có hai nghiệm phân biệt, tức biệt thức $\Delta$ phải không dương:

$$
\Delta=B^2-8g^2v_0^2\le 0.
$$

Thay biểu thức của $B$:

$$
9g^2v_0^2\sin^2\theta_0-8g^2v_0^2\le 0.
$$

Vì $g^2v_0^2>0$, bất đẳng thức tương đương với:

$$
\sin^2\theta_0\le\frac{8}{9},
$$

$$
\sin\theta_0\le\frac{2\sqrt{2}}{3}.
$$

Góc phóng cực đại phía trên phương ngang:

$$
\theta_{\max}=\arcsin\left(\frac{2\sqrt{2}}{3}\right),
$$

$$
\theta_{\max}\approx 70{,}5^\circ.
$$

Tại góc giới hạn, $Q(t)$ có một nghiệm kép dương. Đạo hàm khoảng cách bằng không ở đúng một thời điểm, nhưng không âm ở các thời điểm còn lại, nên khoảng cách vẫn tăng nghiêm ngặt giữa hai thời điểm bất kỳ. Nếu yêu cầu đạo hàm dương tại mọi $t>0$, góc phải nhỏ hơn giới hạn và $70{,}5^\circ$ là cận trên. Điều kiện vật lý đang xét là khoảng cách không có giai đoạn giảm.

</details>

### 3.80 (•••): Đón chai trôi trên sông

Hai sinh viên chèo một chiếc thuyền ca-nô trên một dòng sông. Trong khi đang chèo ngược dòng, họ vô tình làm rơi một chiếc chai rỗng xuống nước. Họ tiếp tục chèo ngược dòng trong $60$ phút nữa và đến một điểm cách vị trí làm rơi chai $2{,}0\,\mathrm{km}$ về phía thượng lưu. Tại điểm này, họ nhận ra chiếc chai đã bị thất lạc và quyết định quay thuyền chèo xuôi dòng để tìm lại chiếc chai. Họ đuổi kịp và vớt lại chiếc chai (vốn trôi tự do theo dòng nước) tại vị trí cách điểm quay đầu $5{,}0\,\mathrm{km}$ về phía hạ lưu.

(a) Giả sử sức chèo thuyền của họ không đổi trong suốt hành trình, tốc độ dòng chảy của sông bằng bao nhiêu?

(b) Với cùng sức chèo ấy, tốc độ của chiếc thuyền trên mặt hồ nước tĩnh sẽ bằng bao nhiêu?

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Thuyền chèo ngược dòng rơi chai, chèo tiếp $60\,\text{phút}$ được $2{,}0\,\mathrm{km}$ ngược dòng rồi quay lại. Đuổi kịp chai tại điểm cách điểm quay đầu $5{,}0\,\mathrm{km}$ xuôi dòng. Tìm tốc độ dòng nước và tốc độ thuyền trong nước tĩnh.

**Hướng đi:** Phân tích trong hệ quy chiếu dòng nước: Chiếc chai đứng yên. Thuyền chèo ra xa chai trong $60\,\text{phút}$ rồi chèo ngược lại cùng sức chèo nên thời gian quay về đúng bằng $60\,\text{phút}$. Từ tổng thời gian $2\,\text{giờ}$ và quãng đường chai trôi trong hệ mặt đất, suy ra tốc độ dòng chảy. Sau đó tính tốc độ thuyền trong nước tĩnh.

**Lời giải:** (a) Phân tích trong hệ quy chiếu gắn với dòng nước:

Chiếc chai rỗng nổi trôi tự do theo dòng nước, do đó trong hệ quy chiếu của dòng nước, chiếc chai hoàn toàn đứng yên tại gốc tọa độ của hệ này.

Hai sinh viên chèo thuyền với sức chèo không đổi, nghĩa là tốc độ của thuyền đối với nước, ký hiệu là $v_c$, có độ lớn không đổi ở cả lượt chèo ngược dòng lẫn lượt chèo xuôi dòng.

Trong hệ quy chiếu của nước:
- Lượt đi: Thuyền rời xa chiếc chai với tốc độ $v_c$ trong khoảng thời gian $t_1=60\,\text{phút}=1{,}00\,\mathrm h$. Khoảng cách giữa thuyền và chiếc chai lúc này là $d=v_c t_1$.
- Lượt về: Thuyền quay đầu chèo hướng thẳng về phía chiếc chai với cùng tốc độ $v_c$ đối với nước. Khoảng cách cần vượt qua là $d$. Do đó thời gian để thuyền bắt kịp chiếc chai là:

$$
t_2=\frac{d}{v_c}=t_1=1{,}00\,\mathrm h.
$$

Tổng thời gian từ khi chiếc chai bị rơi cho đến khi được vớt lại:

$$
T=t_1+t_2=2{,}00\,\mathrm h.
$$

Bây giờ xét chuyển động của chiếc chai trong hệ quy chiếu mặt đất:
- Vị trí quay đầu cách điểm rơi $2{,}0\,\mathrm{km}$ về phía thượng lưu.
- Điểm vớt chai cách điểm quay đầu $5{,}0\,\mathrm{km}$ về phía hạ lưu.
- Do đó điểm vớt chai cách điểm rơi ban đầu một khoảng xuôi dòng:

$$
\Delta x_{\text{chai}}=5{,}0-2{,}0=3{,}0\,\mathrm{km}.
$$

Trong toàn bộ khoảng thời gian $T=2{,}00\,\mathrm h$, chiếc chai trôi tự do theo dòng nước quãng đường $3{,}0\,\mathrm{km}$ này. Tốc độ của dòng nước là:

$$
\begin{aligned}
v_w &= \frac{\Delta x_{\text{chai}}}{T} \\
&= \frac{3{,}0}{2{,}00} = 1{,}50\,\mathrm{km/h}.
\end{aligned}
$$

(b) Trong lượt chèo ngược dòng thứ nhất, tốc độ của thuyền đối với mặt đất:

$$
v_c-v_w=\frac{2{,}0}{1{,}00}=2{,}0\,\mathrm{km/h}.
$$

Thay $v_w=1{,}50\,\mathrm{km/h}$:

$$
\begin{aligned}
v_c &= 2{,}0+v_w \\
&= 2{,}0+1{,}50 \\
&= 3{,}50\,\mathrm{km/h}.
\end{aligned}
$$

Tốc độ của chiếc thuyền trên mặt hồ nước tĩnh là $3{,}50\,\mathrm{km/h}$.

</details>

### 3.81 (•••, CP): Thả tên lửa từ máy bay

Một tên lửa mang tải trọng nhỏ lên quỹ đạo được một máy bay cải tiến chở lên độ cao $12{,}0\,\mathrm{km}$ so với mực nước biển. Khi máy bay đang bay theo một đường thẳng nằm ngang với tốc độ không đổi $850\,\mathrm{km/h}$, tên lửa được thả ra. Sau khi thả, máy bay vẫn duy trì độ cao và tốc độ này, tiếp tục bay thẳng. Tên lửa rơi tự do trong một khoảng thời gian ngắn, sau đó động cơ tên lửa khởi động. Khi động cơ hoạt động, tác dụng tổng hợp của lực đẩy và trọng lực truyền cho tên lửa một gia tốc không đổi có độ lớn $3{,}00g$ hướng chếch lên một góc $30{,}0^\circ$ phía trên phương ngang. Để đảm bảo an toàn, tên lửa phải ở phía trước máy bay ít nhất $1{,}00\,\mathrm{km}$ khi nó bay ngược lên cắt qua độ cao của máy bay. Nhiệm vụ của bạn là xác định thời gian tối thiểu mà tên lửa phải rơi tự do trước khi khởi động động cơ. Bỏ qua lực cản không khí.

Lời giải cần bao gồm:
(i) Sơ đồ thể hiện quỹ đạo bay của cả máy bay và tên lửa, có vẽ các vector vận tốc và gia tốc tại các điểm mốc chính.
(ii) Đồ thị tọa độ ngang theo thời gian $x-t$ của cả hai phương tiện.
(iii) Đồ thị tọa độ thẳng đứng theo thời gian $y-t$ của cả hai phương tiện.

Trên sơ đồ và các đồ thị, hãy chỉ rõ các thời điểm: Khi tên lửa được thả, khi động cơ tên lửa khởi động, và khi tên lửa bay cắt qua độ cao của máy bay.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Máy bay bay ngang $v_0=850\,\mathrm{km/h}$ ở độ cao $12{,}0\,\mathrm{km}$. Thả tên lửa rơi tự do trong thời gian $t_1$, sau đó động cơ gia tốc $a=3{,}00g$ góc $30{,}0^\circ$ lên trên. Khi tên lửa trở lại độ cao $12{,}0\,\mathrm{km}$, nó phải cách máy bay phía trước ít nhất $1{,}00\,\mathrm{km}$. Tìm $t_1$ tối thiểu và vẽ 3 hình minh họa.

**Hướng đi:** Chọn gốc tọa độ tại vị trí thả tên lửa, trục $Oy$ thẳng đứng với $y=0$ là độ cao máy bay. Chia chuyển động của tên lửa làm hai giai đoạn: Rơi tự do thời gian $t_1$ và chuyển động có gia tốc góc thời gian $t_2$. Thiết lập điều kiện tên lửa trở lại $y=0$ để tìm tỷ lệ giữa $t_2$ và $t_1$. Sau đó dùng điều kiện khoảng cách ngang $\Delta x\ge 1000\,\mathrm m$ để chặn cận dưới của $t_1$.

**Lời giải:** (i) Phân tích chuyển động và sơ đồ quỹ đạo:

Chọn gốc tọa độ tại vị trí thả tên lửa trên độ cao $12{,}0\,\mathrm{km}$. Trục $Ox$ nằm ngang theo hướng bay, trục $Oy$ thẳng đứng hướng lên. Tốc độ ban đầu:

$$
\begin{aligned}
v_0 &= 850\,\mathrm{km/h} \\
&= \frac{850}{3{,}6}\,\mathrm{m/s}\approx 236{,}11\,\mathrm{m/s}.
\end{aligned}
$$

Chuyển động của máy bay: Bay thẳng đều ở độ cao $y_{\text{mb}}=0$ với vận tốc $v_0$:

$$
x_{\text{mb}}(t)=v_0t,
$$

$$
y_{\text{mb}}(t)=0.
$$

Chuyển động của tên lửa gồm hai giai đoạn:

Giai đoạn 1 (rơi tự do trong khoảng thời gian $t_1$):
Gia tốc là $\vec{a}_1=-g\,\vec{j}$. Vận tốc ban đầu bằng vận tốc máy bay:

$$
v_{x1}=v_0,\qquad v_{y1}=-gt.
$$

Tại thời điểm $t_1$ khi động cơ bắt đầu khởi động:

$$
x(t_1)=v_0t_1,
$$

$$
y(t_1)=-\frac{1}{2}gt_1^2,
$$

$$
v_{x}(t_1)=v_0,
$$

$$
v_{y}(t_1)=-gt_1.
$$

Giai đoạn 2 (động cơ hoạt động trong khoảng thời gian $t_2$):
Gia tốc toàn phần của tên lửa có độ lớn $a=3{,}00g$ hướng góc $\alpha=30{,}0^\circ$ phía trên phương ngang:

$$
\begin{aligned}
a_x &= 3{,}00g\cos 30{,}0^\circ \\
&= \frac{3\sqrt{3}}{2}g \approx 25{,}46\,\mathrm{m/s^2},
\end{aligned}
$$

$$
\begin{aligned}
a_y &= 3{,}00g\sin 30{,}0^\circ \\
&= 1{,}50g = 14{,}70\,\mathrm{m/s^2}.
\end{aligned}
$$

Tọa độ thẳng đứng của tên lửa sau thời gian $t_2$ kể từ khi bật động cơ:

$$
y=-\frac{1}{2}gt_1^2-gt_1t_2+\frac{3}{4}gt_2^2.
$$

Tên lửa leo ngược trở lại độ cao của máy bay khi $y=0$:

$$
-\frac{1}{2}gt_1^2-gt_1t_2+\frac{3}{4}gt_2^2=0.
$$

Chia hai vế cho $\frac{1}{4}g$:

$$
3t_2^2-4t_1t_2-2t_1^2=0.
$$

Giải phương trình bậc hai tìm nghiệm dương $t_2$ theo $t_1$:

$$
\begin{aligned}
t_2 &= \frac{4+\sqrt{40}}{6}t_1 \\
&= \frac{2+\sqrt{10}}{3}t_1 \approx 1{,}721t_1.
\end{aligned}
$$

Độ dời ngang tương đối giữa tên lửa và máy bay tại thời điểm cắt ngang:
Tại thời điểm $t=t_1+t_2$, tọa độ ngang của máy bay:

$$
x_{\text{mb}}=v_0(t_1+t_2).
$$

Tọa độ ngang của tên lửa:

$$
x_{\text{tl}}=v_0(t_1+t_2)+\frac{1}{2}a_xt_2^2.
$$

Khoảng cách mà tên lửa vượt lên phía trước máy bay:

$$
\Delta x=x_{\text{tl}}-x_{\text{mb}}=\frac{1}{2}a_xt_2^2.
$$

Theo yêu cầu an toàn:

$$
\frac{1}{2}a_xt_2^2\ge 1000,
$$

$$
t_2^2\ge\frac{2000}{25{,}46}\approx 78{,}55\,\mathrm{s^2},
$$

$$
t_2\ge\sqrt{78{,}55}\approx 8{,}863\,\mathrm s.
$$

Suy ra thời gian rơi tự do tối thiểu:

$$
t_1=\frac{3}{2+\sqrt{10}}t_2\approx 5{,}15\,\mathrm s.
$$

Khi đó, độ cao giảm lớn nhất trong giai đoạn rơi tự do là $\frac{1}{2}gt_1^2\approx 130\,\mathrm m$. Độ cao thấp nhất của quỹ đạo xảy ra tại $t'=gt_1/a_y=\frac{2}{3}t_1\approx 3{,}43\,\mathrm s$ sau khi bật động cơ, với độ giảm cực đại $\frac{5}{6}gt_1^2\approx 217\,\mathrm m$, ứng với độ cao tuyệt đối $11{,}78\,\mathrm{km}$.

![Sơ đồ quỹ đạo và vector vận tốc, gia tốc của máy bay và tên lửa](/vat-ly-1/bai-giang/img/young-03/solution-s3-81a.svg)


(ii) Đồ thị tọa độ ngang $x-t$:
Máy bay chuyển động thẳng đều với đồ thị là đường thẳng có hệ số góc $v_0$. Tên lửa trong giai đoạn $t\le t_1$ có cùng vận tốc ngang nên đồ thị trùng với máy bay. Khi $t>t_1$, tên lửa có gia tốc ngang $a_x>0$ nên đồ thị $x_{\text{tl}}(t)$ uốn cong parabol lên phía trên, tách dần về phía trước máy bay.

![Đồ thị tọa độ x theo thời gian t](/vat-ly-1/bai-giang/img/young-03/solution-s3-81b.svg)


(iii) Đồ thị tọa độ đứng $y-t$:
Máy bay có $y_{\text{mb}}=0$ là đường thẳng nằm ngang trùng trục hoành. Tên lửa rơi tự do theo nhánh parabol úp xuống đỉnh tại $(0,0)$. Từ $t_1$, gia tốc đứng đổi chiều hướng lên ($a_y>0$) nên đường cong chuyển sang parabol ngửa, đạt cực tiểu rồi vươn lên cắt lại trục $y=0$ tại $t_1+t_2\approx 14{,}01\,\mathrm s$.

![Đồ thị tọa độ y theo thời gian t](/vat-ly-1/bai-giang/img/young-03/solution-s3-81c.svg)


</details>

## Đọc hiểu khoa học: Cơ chế phát tán hạt bằng đường đạn (Ballistic Seed Dispersal)

Một số loài thực vật phát tán hạt giống khi quả nứt vỡ và co lại, đẩy hạt bắn vào không khí như những viên đạn nhỏ. Quỹ đạo của các hạt giống này có thể được xác định bằng máy quay tốc độ cao (high-speed camera). Trong một thí nghiệm trên một loài thực vật, các hạt giống được phóng ra từ độ cao $20\,\mathrm{cm}$ so với mặt đất với tốc độ ban đầu trong khoảng từ $2{,}3\,\mathrm{m/s}$ đến $4{,}6\,\mathrm{m/s}$. Góc phóng được đo so với phương ngang, với $+90^\circ$ tương ứng với vận tốc ban đầu hướng thẳng đứng lên trên và $-90^\circ$ hướng thẳng đứng xuống dưới.


### 3.82 (•, BIO): Tần số chụp ảnh hạt phát tán

Thí nghiệm được thiết kế sao cho các hạt giống di chuyển không quá $0{,}20\,\mathrm{mm}$ giữa hai khung hình chụp liên tiếp của máy ảnh. Tần số khung hình tối thiểu cần thiết cho máy quay tốc độ cao để đạt được điều này là bao nhiêu?

(a) $250\,\text{khung hình/giây}$.
(b) $2\,500\,\text{khung hình/giây}$.
(c) $25\,000\,\text{khung hình/giây}$.
(d) $250\,000\,\text{khung hình/giây}$.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Hạt được phóng từ độ cao $h=20\,\mathrm{cm}$ với tốc độ đầu từ $2{,}3\,\mathrm{m/s}$ đến $4{,}6\,\mathrm{m/s}$. Độ dịch chuyển giữa hai khung hình liên tiếp không vượt quá $\Delta s=0{,}20\,\mathrm{mm}$. Tìm tần số khung hình tối thiểu của máy ảnh.

**Hướng đi:** Tần số khung hình $f=v/\Delta s$. Để đảm bảo hạt di chuyển không quá $\Delta s$ trong mọi thời điểm của quỹ đạo, cần lấy giá trị tốc độ lớn nhất mà hạt có thể đạt tới. Tốc độ này xuất hiện khi hạt được phóng với tốc độ đầu lớn nhất $4{,}6\,\mathrm{m/s}$ hướng xuống dưới hoặc rơi tự do tới mặt đất.

**Lời giải:** Với khoảng thời gian rất ngắn giữa hai khung hình, quãng đường xấp xỉ $\Delta s\approx v\Delta t=v/f$, trong đó $v$ là tốc độ của hạt và $f$ là tần số khung hình (số khung hình trong một giây).

Điều kiện để $\Delta s\le 0{,}20\,\mathrm{mm}$ (tức $2{,}0\times 10^{-4}\,\mathrm m$) tại mọi điểm trên quỹ đạo đòi hỏi:

$$
f\ge\frac{v_{\max}}{\Delta s}.
$$

Tốc độ lớn nhất có thể có của hạt đạt được khi hạt được phóng với tốc độ đầu cực đại $v_0=4{,}6\,\mathrm{m/s}$ và tiếp tục được trọng lực gia tốc khi rơi xuống tới mặt đất ($h=0{,}20\,\mathrm m$):

$$
\begin{aligned}
v_{\max} &= \sqrt{v_0^2+2gh} \\
&= \sqrt{25{,}08} \approx 5{,}008\,\mathrm{m/s}.
\end{aligned}
$$

Tần số chụp cần thiết:

$$
\begin{aligned}
f &\ge \frac{5{,}008}{2{,}0\times 10^{-4}} \\
&\approx 25\,040\,\mathrm{s^{-1}}.
\end{aligned}
$$

Ngay cả khi chỉ ước lượng dựa trên tốc độ đầu $v_0=4{,}6\,\mathrm{m/s}$:

$$
\begin{aligned}
f &\approx \frac{4{,}6}{2{,}0\times 10^{-4}} \\
&= 23\,000\,\mathrm{s^{-1}}.
\end{aligned}
$$

Theo độ chính xác hai chữ số có nghĩa của các dữ kiện, tốc độ chụp cần có cỡ $2{,}5\times10^4$ khung hình mỗi giây, tương ứng phương án (c).

Nếu coi các dữ kiện là những số chính xác và đòi hỏi quãng đường không vượt ngưỡng tại mọi vị trí, cận bảo đảm là khoảng $25\,040$ khung hình mỗi giây. Vì vậy con số $25\,000$ trong lựa chọn là giá trị xấp xỉ, không phải một cận bảo đảm chính xác đến từng khung hình.

</details>

### 3.83 (•, BIO): Thời gian hạt lên đến đỉnh quỹ đạo

Khoảng thời gian để một hạt giống được phóng ở góc $90^\circ$ với tốc độ ban đầu lớn nhất có thể đạt tới độ cao cực đại là khoảng bao nhiêu? Bỏ qua lực cản không khí.

(a) $0{,}23\,\mathrm s$.
(b) $0{,}47\,\mathrm s$.
(c) $1{,}0\,\mathrm s$.
(d) $2{,}3\,\mathrm s$.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Hạt phóng thẳng đứng lên trên ($\theta_0=90^\circ$) với $v_0=4{,}6\,\mathrm{m/s}$. Tìm thời gian lên tới độ cao cực đại.

**Hướng đi:** Chuyển động thẳng đứng biến đổi đều có $v_y(t)=v_0-gt$. Tại đỉnh quỹ đạo, vận tốc triệt tiêu $v_y=0$. Giải thời gian $t=v_0/g$.

**Lời giải:** Hạt được phóng thẳng đứng lên trên với tốc độ ban đầu lớn nhất theo đề bài là $v_0=4{,}6\,\mathrm{m/s}$.

Gia tốc trọng trường hướng xuống dưới, do đó thành phần vận tốc theo phương thẳng đứng biến thiên theo thời gian:

$$
v_y=v_0-gt.
$$

Tại điểm cao nhất của quỹ đạo, vận tốc tức thời của hạt bằng không ($v_y=0$):

$$
0=v_0-gt\implies t=\frac{v_0}{g}.
$$

Thay số:

$$
t=\frac{4{,}6}{9{,}80}\approx 0{,}469\,\mathrm s\approx 0{,}47\,\mathrm s.
$$

Do đó đáp án đúng là **(b)**.

</details>

### 3.84 (•, BIO): Tầm xa khi hạt phóng ngang

Nếu một hạt giống được phóng ở góc $0^\circ$ với tốc độ ban đầu lớn nhất, hạt sẽ tiếp đất ở khoảng cách bao xa tính từ gốc cây? Bỏ qua lực cản không khí và giả thiết mặt đất bằng phẳng.

(a) $20\,\mathrm{cm}$.
(b) $93\,\mathrm{cm}$.
(c) $2{,}2\,\mathrm m$.
(d) $4{,}6\,\mathrm m$.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Hạt phóng ngang ($\theta_0=0^\circ$) từ độ cao $h=20\,\mathrm{cm}=0{,}20\,\mathrm m$ với $v_0=4{,}6\,\mathrm{m/s}$. Tìm tầm xa trên mặt đất bằng.

**Hướng đi:** Chuyển động ném ngang có vận tốc đầu theo phương đứng bằng không. Thời gian rơi $t=\sqrt{2h/g}$. Tầm xa ngang $R=v_0t$.

**Lời giải:** Hạt được phóng theo phương ngang ($\theta_0=0^\circ$) từ độ cao ban đầu $h=20\,\mathrm{cm}=0{,}20\,\mathrm m$ với vận tốc ban đầu lớn nhất $v_0=4{,}6\,\mathrm{m/s}$.

Vì vận tốc ban đầu theo phương thẳng đứng bằng không ($v_{y0}=0$), thời gian rơi tự do chạm đất của hạt chỉ phụ thuộc vào độ cao:

$$
\begin{aligned}
t &= \sqrt{\frac{2h}{g}} \\
&= \sqrt{\frac{2\times 0{,}20}{9{,}80}}\approx 0{,}2020\,\mathrm s.
\end{aligned}
$$

Trong suốt thời gian rơi, vận tốc theo phương ngang không đổi và bằng $v_0$. Tầm xa hạt bay được từ gốc cây tới điểm chạm đất:

$$
\begin{aligned}
R &= v_0 t \\
&= 4{,}6\times 0{,}2020 \\
&\approx 0{,}929\,\mathrm m = 93\,\mathrm{cm}.
\end{aligned}
$$

Do đó đáp án đúng là **(b)**.

</details>

### 3.85 (•, BIO): Giả thuyết phù hợp nhất với dữ liệu góc phóng

Quan sát một số lượng lớn hạt giống và ghi nhận các góc phóng ban đầu của chúng. Dải góc phóng đo được từ $-51^\circ$ đến $75^\circ$, với giá trị trung bình là $31^\circ$. Khoảng $65\%$ số hạt được phóng trong khoảng giữa $6^\circ$ và $56^\circ$ (theo nghiên cứu của W. J. Garrison và cộng sự, "Ballistic seed projection in two herbaceous species", *Amer. J. Bot.*, 9/2000, 87:9, 1257–64).

Giả thuyết nào sau đây được dữ liệu thực nghiệm ủng hộ tốt nhất? Các hạt có xu hướng ưu tiên được phóng:

(a) Ở các góc tối đa hóa độ cao mà chúng đạt tới phía trên cây.
(b) Ở các góc phía dưới phương ngang để găm hạt vào đất với lực lớn hơn.
(c) Ở các góc tối đa hóa khoảng cách ngang mà hạt bay ra xa khỏi cây.
(d) Ở các góc tối thiểu hóa thời gian hạt phơi nhiễm trong không khí.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Góc phóng nằm từ $-51^\circ$ đến $75^\circ$, trung bình $31^\circ$. Khoảng $65\%$ số hạt có góc từ $6^\circ$ đến $56^\circ$.

**Hướng đi:** So sánh xu thế của dữ liệu với hướng phóng mà mỗi giả thuyết dự đoán. Cần chọn giả thuyết được hỗ trợ tốt nhất, không khẳng định dữ liệu góc phóng đã chứng minh mục đích sinh học của cây.

**Lời giải:**

Phương án (a) đòi hỏi góc gần $90^\circ$ để độ cao tăng tối đa, trong khi các góc quan sát thấp hơn đáng kể. Các phương án (b) và (d) thiên về phóng xuống, trái với việc phần lớn hạt trong khoảng đã nêu được phóng lên.

Để đạt tầm xa lớn, vật cần cả thành phần vận tốc ngang lẫn thành phần hướng lên. Từ độ cao $h>0$, góc tối ưu hơi nhỏ hơn $45^\circ$. Với tốc độ đầu và độ cao trong đoạn dẫn, công thức góc tối ưu là:

$$
\sin\theta_{\mathrm{opt}}=\frac1{\sqrt{2+2gh/v_0^2}}.
$$

Các tốc độ từ $2{,}3$ đến $4{,}6\,\mathrm{m/s}$ cho góc tối ưu khoảng $37{,}2^\circ$ đến $42{,}6^\circ$. Dải góc tập trung quan sát được bao quanh vùng phóng chếch này. Vì vậy, trong bốn lựa chọn, (c) phù hợp nhất.

Các góc đo còn phân tán và góc trung bình không trùng chính xác góc tối ưu của mô hình. Dữ liệu ủng hộ cách giải thích về phát tán xa theo phương ngang, nhưng chưa đủ để khẳng định mọi hạt được phóng với góc tối ưu.

</details>
