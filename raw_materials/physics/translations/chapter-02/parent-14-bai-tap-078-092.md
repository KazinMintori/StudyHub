## Bài tập tổng hợp và thử thách

### 2.78 ••• Thiết kế tên lửa nghiên cứu

Trong kỳ thực tập hè tại một công ty hàng không vũ trụ, bạn được giao thiết kế tên lửa nghiên cứu nhỏ. Tên lửa xuất phát nghỉ từ mặt đất và phải đạt độ cao cực đại 960 m. Động cơ tạo gia tốc hướng lên 16,0 $\mathrm{m/s^2}$ trong thời gian hoạt động T. Sau khi tắt máy, tên lửa rơi tự do. Bỏ qua sức cản không khí. T phải bằng bao nhiêu?

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Độ cao cực đại H = 960 m. Trong thời gian T, gia tốc tổng hợp hướng lên là $a=16{,}0\,\mathrm{m/s^2}$. Sau đó gia tốc là −g.

**Hướng đi:** Độ cao cực đại gồm đoạn có động cơ và đoạn bay lên sau tắt máy. Vận tốc cuối đoạn đầu là vận tốc đầu của đoạn sau.

**Lời giải:** Khi tắt máy, tốc độ là u = aT và độ cao là $h_c=aT^2/2$. Sau đó tên lửa lên thêm $u^2/(2g)$:

$$
\begin{aligned}
H&=\frac12aT^2+\frac{a^2T^2}{2g}\\
&=\frac{aT^2}{2}\left(1+\frac ag\right).
\end{aligned}
$$

Lấy nghiệm thời gian dương:

$$
T=\sqrt{\frac{2H}{a(1+a/g)}}
\approx6{,}75\,\mathrm s.
$$

Gia tốc đã cho là gia tốc chuyển động khi động cơ hoạt động, nên không trừ g thêm một lần nữa.

</details>

### 2.79 ••• Trực thăng và bộ phản lực

Một trực thăng chở Dr. Evil cất cánh với gia tốc hướng lên không đổi 5,0 $\mathrm{m/s^2}$. Mật vụ Austin Powers nhảy lên đúng lúc trực thăng rời mặt đất. Sau khi hai người giằng co trong 10,0 s, Powers tắt động cơ rồi bước ra ngoài. Trực thăng rơi tự do sau khi tắt máy. Bỏ qua sức cản không khí.

(a) Trực thăng đạt độ cao cực đại bao nhiêu? (b) Powers kích hoạt bộ phản lực đeo lưng sau khi rời trực thăng 7,0 s. Từ đó anh có gia tốc không đổi hướng xuống, độ lớn 2,0 $\mathrm{m/s^2}$. Khi trực thăng chạm đất, Powers còn cách đất bao xa?

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Trực thăng xuất phát nghỉ, tăng tốc lên trong 10,0 s. Khi Powers rời trực thăng, cả hai cùng có độ cao và vận tốc ban đầu. Powers rơi tự do 7,0 s rồi chuyển sang gia tốc tổng hợp hướng xuống có độ lớn 2,0 $\mathrm{m/s^2}$.

**Hướng đi:** Tính trạng thái lúc tắt máy, rồi dùng thời điểm trực thăng chạm đất làm mốc chung. Powers và trực thăng có cùng chuyển động trong 7,0 s đầu sau khi rời nhau, nhưng có gia tốc khác nhau sau đó.

**Lời giải:** Chọn +y hướng lên. Lúc tắt máy,

$$
\begin{aligned}
&u=50{,}0\,\mathrm{m/s},\\
&h=250\,\mathrm m.
\end{aligned}
$$

(a) Độ cao cực đại:

$$
H_{\max}=h+\frac{u^2}{2g}\approx378\,\mathrm m.
$$

(b) Lấy t = 0 khi tắt máy. Trực thăng chạm đất tại nghiệm dương

$$
\begin{aligned}
T&=\frac{u+\sqrt{u^2+2gh}}g\\
&\approx13{,}88\,\mathrm s.
\end{aligned}
$$

Khi Powers bật bộ phản lực ở t = 7,0 s,

$$
\begin{aligned}
&y_7=359{,}9\,\mathrm m,\\
&v_7=-18{,}6\,\mathrm{m/s}.
\end{aligned}
$$

Thời gian còn lại tới lúc trực thăng chạm đất là Δt = T − 7,0 s, khoảng 6,88 s. Với $a_P=-2{,}0\,\mathrm{m/s^2}$,

$$
y_P=y_7+v_7\Delta t+\frac12a_P(\Delta t)^2.
$$

Thay các giá trị chưa làm tròn được

$$
y_P\approx185\,\mathrm m.
$$

Powers vẫn đang chuyển động xuống. Gia tốc hướng xuống 2,0 $\mathrm{m/s^2}$ làm tốc độ đi xuống tăng chậm hơn khi rơi tự do, không phải làm tốc độ ấy giảm.

</details>

### 2.80 •• Độ cao vách đá

Khi leo núi ở High Sierra, bạn gặp một vách đá bị sương che. Bạn thả một hòn đá từ đỉnh và nghe tiếng va chạm ở chân vách sau 8,00 s.

(a) Vách cao bao nhiêu nếu bỏ qua sức cản không khí và tốc độ âm là 330 m/s? (b) Nếu bỏ qua thời gian âm truyền tới tai, độ cao tính được lớn hơn hay nhỏ hơn giá trị đúng? Giải thích.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Tổng thời gian T = 8,00 s gồm thời gian đá rơi t và thời gian âm truyền lên h/c. Tốc độ âm c = 330 m/s.

**Hướng đi:** Thời gian âm truyền không bằng không. Dùng cùng chiều cao h cho chuyển động rơi và đường truyền âm, rồi cộng hai thời gian.

**Lời giải:** (a) Hai quan hệ:

$$
h=\frac12gt^2,
\qquad T=t+\frac hc.
$$

Khử h:

$$
\frac{g}{2c}t^2+t-T=0.
$$

Nghiệm vật lý thỏa 0 < t < T là khoảng 7,225 s. Suy ra

$$
h=\frac12gt^2\approx256\,\mathrm m.
$$

(b) Nếu dùng toàn bộ 8,00 s làm thời gian rơi,

$$
h_{\mathrm{sai}}=\frac12gT^2=313{,}6\,\mathrm m.
$$

Kết quả lớn hơn chiều cao thật, vì đã cộng thời gian âm truyền vào thời gian rơi.

</details>

### 2.81 •• CALC Gia tốc tỉ lệ với thời gian

Một vật chuyển động trên trục x, tại t = 0 có vận tốc 20,0 m/s. Từ lúc đó, gia tốc là $a_x(t)=-Ct$, với C có đơn vị $\mathrm{m/s^3}$. (a) Tìm C để vật dừng sau 8,00 s. (b) Vật đi được bao xa trong khoảng ấy?

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** $v_0=20{,}0\,\mathrm{m/s}$, T = 8,00 s, $a_x=-Ct$ và v(T) = 0.

**Hướng đi:** Tích phân gia tốc để tìm vận tốc và hằng số C. Vận tốc không âm trước lúc dừng, nên tích phân vận tốc cũng là quãng đường.

**Lời giải:** (a)

$$
v_x(t)=v_0-\frac12Ct^2.
$$

Điều kiện dừng cho

$$
C=\frac{2v_0}{T^2}=0{,}625\,\mathrm{m/s^3}.
$$

(b) Quãng đường:

$$
\begin{aligned}
s&=\int_0^T v_x(t)\,\mathrm dt\\
&=v_0T-\frac16CT^3\\
&\approx107\,\mathrm m.
\end{aligned}
$$

Không dùng gia tốc không đổi vì độ lớn gia tốc đang tăng theo thời gian.

</details>

### 2.82 •• Hai quả bóng gặp nhau

Một bóng được ném thẳng đứng lên từ mặt đất với tốc độ $v_0$. Cùng lúc, một bóng khác được thả nghỉ ở độ cao H, ngay trên điểm ném bóng thứ nhất. Bỏ qua sức cản không khí.

(a) Tìm thời điểm hai bóng va chạm. (b) H phải bằng bao nhiêu theo $v_0$ và g để bóng thứ nhất ở đỉnh quỹ đạo khi va chạm?

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Hai bóng bắt đầu đồng thời, có cùng gia tốc −g. Bóng một ở y = 0 với vận tốc đầu $v_0>0$. Bóng hai ở y = H với vận tốc đầu bằng không.

**Hướng đi:** Trừ hai tọa độ để triệt tiêu phần chuyển động do cùng gia tốc. Kiểm tra nghiệm gặp nhau còn nằm trên mặt đất.

**Lời giải:** (a)

$$
\begin{aligned}
&y_1=v_0t-\frac12gt^2,\\
&y_2=H-\frac12gt^2.
\end{aligned}
$$

Cho hai tọa độ bằng nhau:

$$
t_c=\frac H{v_0}.
$$

Để va chạm trên không trước khi một bóng chạm đất, cần

$$
0<H<\frac{2v_0^2}{g}.
$$

Dấu bằng ở cận trên tương ứng gặp nhau ngay trên mặt đất. Với H lớn hơn cận này, nghiệm hình thức nằm dưới đất, ngoài mô hình bay tự do của bài toán.

(b) Bóng một lên đỉnh lúc $t_p=v_0/g$. Kết hợp với $t_c=H/v_0$:

$$
H=\frac{v_0^2}{g}.
$$

Vị trí va chạm khi đó là H/2.

</details>

### 2.83 • CALC Hai ô tô có quy luật vị trí khác nhau

Hai xe A và B chuyển động thẳng từ cùng điểm xuất phát. Tọa độ là

$$
x_A(t)=\alpha t+\beta t^2,
$$

$$
x_B(t)=\gamma t^2-\delta t^3.
$$

Các hằng số: $\alpha=2{,}60\,\mathrm{m/s}$, $\beta=1{,}20\,\mathrm{m/s^2}$, $\gamma=2{,}80\,\mathrm{m/s^2}$ và $\delta=0{,}20\,\mathrm{m/s^3}$.

(a) Xe nào ở trước ngay sau khi xuất phát? (b) Hai xe ở cùng vị trí vào những thời điểm nào? (c) Khi nào khoảng cách giữa A và B không tăng cũng không giảm? (d) Khi nào hai gia tốc bằng nhau?

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Hai tọa độ đã cho theo thời gian, chỉ xét t ≥ 0.

**Hướng đi:** So sánh tọa độ để xác định thứ tự và điểm gặp. Đạo hàm tọa độ cho vận tốc, đạo hàm lần hai cho gia tốc. Khoảng cách có thể có góc nhọn tại điểm hai xe vượt nhau, nên không đồng nhất mọi cực tiểu với đạo hàm bằng không.

**Lời giải:** (a) Ở thời gian dương rất nhỏ, xe A có số hạng tuyến tính dương $\alpha t$, còn xe B bắt đầu bằng số hạng bậc hai. Vì vậy A ở trước.

(b) Tại t = 0, hai xe ở cùng vị trí. Với t > 0, cho hai tọa độ bằng nhau rồi chia cả hai vế cho t:

$$
\delta t^2+(\beta-\gamma)t+\alpha=0.
$$

Hai nghiệm dương của phương trình này là

$$
t=(4\pm\sqrt3)\,\mathrm s.
$$

Hai lần gặp sau khi xuất phát là khoảng 2,27 s và 5,73 s.

(c) Ở nơi hai tọa độ khác nhau, khoảng cách đứng yên tức thời khi $v_A=v_B$. Hai vận tốc:

$$
v_A=\alpha+2\beta t,
$$

$$
v_B=2\gamma t-3\delta t^2.
$$

Cho chúng bằng nhau được

$$
\begin{aligned}
&t_1=1{,}00\,\mathrm s,\\
&t_2=\frac{13}{3}\,\mathrm s\approx4{,}33\,\mathrm s.
\end{aligned}
$$

Tại hai thời điểm vượt nhau ở câu (b), khoảng cách bằng không nhưng có góc nhọn vì vận tốc tương đối khác không. Vì vậy đạo hàm khoảng cách không bằng không tại đó.

(d) Gia tốc là $a_A=2\beta$ và $a_B=2\gamma-6\delta t$. Điều kiện bằng nhau cho

$$
t=\frac{\gamma-\beta}{3\delta}
\approx2{,}67\,\mathrm s.
$$

</details>

### 2.84 •• DATA Tuyến tính hóa số liệu con trượt

Trong phòng thí nghiệm, bạn thả một con trượt từ nghỉ tại nhiều vị trí trên đệm khí dài, không ma sát, nghiêng góc $\theta$ so với phương ngang. Cổng quang đo thời gian t để con trượt đi quãng đường x từ điểm thả tới chân đệm. Hình P2.84 cho các số đo và một đường khớp đa thức bậc hai. Gia tốc được coi là không đổi. Mỗi phép đo có sai số, nên cần khai thác nhiều điểm thay vì chỉ một cặp x, t.

(a) Vẽ lại đại lượng nào theo đại lượng nào để các điểm gần một đường thẳng? Gợi ý: Có thể nâng x, t hoặc cả hai lên một lũy thừa thích hợp. (b) Dựng đồ thị đó và tìm phương trình đường thẳng khớp tốt nhất. (c) Suy ra gia tốc. (d) Thả con trượt cách chân đệm 1,35 m. Dùng gia tốc ở câu (c) để tìm tốc độ khi tới chân đệm.

![Hình P2.84: Thời gian trượt theo quãng đường, gồm sáu điểm đo và đường khớp](/vat-ly-1/bai-giang/img/young-02/hinh-p2-84.png)

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Con trượt xuất phát nghỉ và có gia tốc a không đổi. Dữ liệu được cho bằng đồ thị, nên các giá trị đọc ra có độ chính xác hữu hạn.

**Hướng đi:** Từ $x=at^2/2$, vẽ x theo $t^2$ để hệ số góc bằng a/2. Dùng đường khớp của toàn bộ điểm. Phân biệt giá trị đọc xấp xỉ trên hình với dữ liệu số chính xác.

**Lời giải:** (a) Chọn trục ngang là $t^2$, trục đứng là x. Quan hệ lý tưởng là đường thẳng qua gốc. Cũng có thể vẽ $t^2$ theo x và lấy nghịch đảo hệ số góc thích hợp.

(b) Một lần đọc xấp xỉ các tâm điểm cho bảng:

| x (m) | t (s) |
| :---: | :---: |
| 0,50 | 0,36 |
| 1,00 | 0,51 |
| 1,50 | 0,63 |
| 2,00 | 0,73 |
| 2,50 | 0,81 |
| 3,00 | 0,89 |

Đặt z = $t^2$ và khớp x = A + Bz theo bình phương tối thiểu. Với $\bar z,\bar x$ là trung bình của sáu giá trị, đặt

$$
c_i=(z_i-\bar z)(x_i-\bar x),
$$

$$
d_i=(z_i-\bar z)^2.
$$

Chỉ số i chạy từ 1 tới 6, tương ứng sáu điểm đọc trên hình.

Hệ số góc và hệ số chặn:

$$
B=\frac{c_1+c_2+\dots+c_6}{d_1+d_2+\dots+d_6},
$$

$$
A=\bar x-B\bar z.
$$

Với bảng đọc ở trên, A ≈ 0,0092 m và B ≈ 3,77 $\mathrm{m/s^2}$. Đồ thị minh họa đường khớp:

![Lời giải 2.84: Sáu điểm x theo t bình phương và đường thẳng bình phương tối thiểu](/vat-ly-1/bai-giang/img/young-02/solution-p2-84.svg)

(c) Vì B = a/2, ta được

$$
a=2B\approx7{,}5\,\mathrm{m/s^2}.
$$

Hệ số chặn nhỏ phản ánh độ lệch của các giá trị đọc trên hình. Không diễn giải nó thành quãng đường ban đầu khác không của con trượt.

(d) Với $\ell=1{,}35\,\mathrm m$ và xuất phát nghỉ,

$$
v=\sqrt{2a\ell}\approx4{,}5\,\mathrm{m/s}.
$$

Đọc điểm với độ chính xác khác có thể làm thay đổi vài chữ số cuối của đường khớp. Vì vậy không coi 7,547469… $\mathrm{m/s^2}$ là một phép đo gia tốc chính xác tới nhiều chữ số.

</details>

### 2.85 •• DATA Độ cao theo bình phương tốc độ

Bạn thả một viên bi thép nhỏ từ nhiều độ cao, đo tốc độ ngay trước khi chạm đất và vẽ độ cao thả h theo bình phương tốc độ cuối $v^2$. Các điểm gần một đường thẳng.

(a) Với $g=9{,}80\,\mathrm{m/s^2}$ và bỏ qua cản khí, hệ số góc bằng bao nhiêu, có đơn vị gì? Lực cản làm giảm độ lớn gia tốc hướng xuống và tác dụng mạnh hơn khi tốc độ tăng. Lặp lại với bóng tennis thì lực cản ảnh hưởng rõ rệt. (b) Ở cùng độ cao, tốc độ cuối lớn hơn, nhỏ hơn hay bằng khi bỏ qua lực cản? (c) Đồ thị còn thẳng không? Vẽ dạng định tính khi có lực cản.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Vật được thả nghỉ. Trục đứng là h, trục ngang là $v^2$. Không có quy luật lực cản cụ thể.

**Hướng đi:** Dùng $v^2=2gh$ cho trường hợp không cản. Khi có lực cản, xét gia tốc hướng xuống hiệu dụng để xác định vị trí và độ cong của đồ thị, không tự gán một hàm lực cản.

**Lời giải:** (a)

$$
h=\frac1{2g}v^2.
$$

Hệ số góc:

$$
m=\frac1{2g}\approx0{,}0510\,\mathrm{s^2/m}.
$$

(b) Với cùng độ cao, lực cản làm tốc độ cuối nhỏ hơn.

(c) Gọi $a_{\mathrm{eff}}(v)$ là độ lớn gia tốc hướng xuống khi bóng đang rơi và còn tăng tốc. Khi đó

$$
\frac{\mathrm d(v^2)}{\mathrm dh}=2a_{\mathrm{eff}}(v).
$$

Vì vậy

$$
\frac{\mathrm dh}{\mathrm d(v^2)}
=\frac1{2a_{\mathrm{eff}}(v)}.
$$

Khi lực cản tăng theo tốc độ, gia tốc hiệu dụng giảm và hệ số góc này tăng. Đồ thị h theo $v^2$ cong lên, nằm phía trên đường không cản. Ở cùng tốc độ cuối, bóng cần rơi từ độ cao lớn hơn.

![Lời giải 2.85: Đường có lực cản cong lên phía trên đường không cản, chỉ biểu diễn định tính](/vat-ly-1/bai-giang/img/young-02/solution-p2-85.svg)

Hình chỉ minh họa chiều cong và thứ tự hai đường, không phải số liệu đo hay kết quả khớp một mô hình lực cản đã biết.

</details>

### 2.86 ••• DATA Gia tốc của xe mô hình

Một xe mô hình xuất phát nghỉ, chạy thẳng. Ứng dụng trên điện thoại gắn trên xe truyền độ lớn gia tốc đo bằng gia tốc kế mỗi giây:

| t (s) | a ($\mathrm{m/s^2}$) |
| :---: | :---: |
| 0 | 5,95 |
| 1,00 | 5,52 |
| 2,00 | 5,08 |
| 3,00 | 4,55 |
| 4,00 | 3,96 |
| 5,00 | 3,40 |

Mỗi số đo có sai số. (a) Vẽ a theo t và tìm phương trình đường thẳng khớp tốt nhất. (b) Tính v(t) từ a(t), vẽ đồ thị và cho biết có phải đường thẳng không. (c) Tính tốc độ tại 5,00 s. (d) Tính quãng đường từ 0 tới 5,00 s.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Sáu cặp số đo, vận tốc đầu bằng không. Chọn chiều dương theo chiều xe chạy và dùng mô hình gia tốc tuyến tính trong khoảng 0–5,00 s.

**Hướng đi:** Khớp cả sáu điểm thay vì chỉ nối hai đầu. Tích phân đường gia tốc khớp để tìm vận tốc và tiếp tục tích phân để tìm quãng đường. Gia tốc giảm nhưng vẫn dương trong khoảng đo.

**Lời giải:** (a) Viết $a(t)=A+Bt$. Trung bình sáu thời gian và sáu gia tốc là

$$
\begin{aligned}
&\bar t=2{,}50\,\mathrm s,\\
&\bar a\approx4{,}74333\,\mathrm{m/s^2}.
\end{aligned}
$$

Với chỉ số i chạy từ 0 tới 5, đặt

$$
c_i=(t_i-\bar t)(a_i-\bar a).
$$

$$
d_i=(t_i-\bar t)^2.
$$

Cộng các giá trị của sáu phép đo:

$$
\begin{aligned}
N&=c_0+c_1+\dots+c_5\\
&=-8{,}98\,\mathrm{m/s},
\end{aligned}
$$

$$
\begin{aligned}
D&=d_0+d_1+\dots+d_5\\
&=17{,}5\,\mathrm{s^2}.
\end{aligned}
$$

Hệ số bình phương tối thiểu:

$$
B=\frac ND\approx-0{,}513143\,\mathrm{m/s^3},
$$

$$
A=\bar a-B\bar t\approx6{,}02619\,\mathrm{m/s^2}.
$$

Đường thẳng gia tốc đi xuống nhưng vẫn nằm phía trên trục thời gian trên toàn khoảng đo.

(b) Vì v(0) = 0,

$$
\begin{aligned}
v(t)&=\int_0^t(A+B\tau)\,\mathrm d\tau\\
&=At+\frac12Bt^2.
\end{aligned}
$$

Đây là một parabol cong xuống, không phải đường thẳng. Tốc độ tiếp tục tăng nhưng tốc độ tăng nhỏ dần.

![Lời giải 2.86: Sáu số đo và đường gia tốc khớp, bên cạnh đồ thị vận tốc tăng với độ dốc giảm](/vat-ly-1/bai-giang/img/young-02/solution-p2-86.svg)

(c) Dùng các hệ số chưa làm tròn:

$$
v(5{,}00\,\mathrm s)\approx23{,}7\,\mathrm{m/s}.
$$

(d) Vận tốc không âm nên quãng đường bằng độ dời:

$$
\begin{aligned}
s&=\int_0^T v(t)\,\mathrm dt\\
&=\frac12AT^2+\frac16BT^3\\
&\approx64{,}6\,\mathrm m,
\end{aligned}
$$

với T = 5,00 s. Không kéo dài đường gia tốc khớp ra ngoài khoảng đo để dự đoán chuyển động mà chưa có thêm dữ liệu.

</details>

### 2.87 ••• Thời gian ở phần trên của cú nhảy

Một vận động viên bắt đầu từ tư thế chùng người rồi bật thẳng đứng lên cao nhất có thể. Ngay cả người bật nhảy tốt nhất cũng chỉ ở trên không hơn 1,00 s một chút. Coi vận động viên là chất điểm, gọi $y_{\max}$ là độ cao cực đại so với sàn. Để giải thích cảm giác vận động viên dường như đứng lại trên không, tìm tỉ số giữa thời gian ở trên $y_{\max}/2$ và thời gian đi từ sàn lên độ cao ấy. Bỏ qua sức cản không khí.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Mô hình chất điểm rời sàn với tốc độ u, bay lên rồi xuống cùng độ cao. Mẫu số của tỉ số chỉ tính một lượt đi lên từ sàn tới nửa độ cao.

**Hướng đi:** Giải hai thời điểm đi qua nửa độ cao, lấy hiệu để có thời gian ở phần trên. So với thời điểm đi lên đầu tiên, không so với tổng thời gian của cả hai đoạn dưới.

**Lời giải:** Thời gian tới đỉnh là $t_p=u/g$ và $y_{\max}=u^2/(2g)$. Điều kiện nửa độ cao:

$$
ut-\frac12gt^2=\frac{u^2}{4g}.
$$

Hai nghiệm:

$$
t_1=t_p\left(1-\frac1{\sqrt2}\right),
$$

$$
t_2=t_p\left(1+\frac1{\sqrt2}\right).
$$

Thời gian ở phía trên nửa độ cao là

$$
\Delta t_{\mathrm{trên}}=t_2-t_1=\sqrt2\,t_p.
$$

Tỉ số cần tìm:

$$
\begin{aligned}
R&=\frac{\sqrt2}{1-1/\sqrt2}\\
&=2(1+\sqrt2)\approx4{,}83.
\end{aligned}
$$

Khoảng 70,7% tổng thời gian bay được dành cho nửa trên của độ cao. Vận tốc gần đỉnh nhỏ, nên vận động viên ở gần đỉnh lâu hơn cảm giác suy ra từ chuyển động đều. Gia tốc vẫn là −g suốt giai đoạn bay, không có một khoảng thời gian đứng yên ở đỉnh.

</details>

### 2.88 ••• Đuổi xe buýt vừa rời trạm

Một sinh viên chạy với tốc độ tối đa không đổi 5,0 m/s tới một xe buýt đang dừng. Khi sinh viên còn cách xe 40,0 m, xe bắt đầu đi với gia tốc không đổi 0,170 $\mathrm{m/s^2}$.

(a) Sinh viên phải chạy bao lâu và bao xa để vượt tới xe? (b) Khi ấy xe chạy nhanh bao nhiêu? (c) Vẽ hai tọa độ theo thời gian trên cùng hệ trục, gốc tại vị trí đầu của sinh viên. (d) Tìm nghiệm gặp thứ hai nếu cả hai tiếp tục giữ quy luật chuyển động, giải thích và tính tốc độ xe khi ấy. (e) Với tốc độ chạy 3,5 m/s, sinh viên có đuổi kịp không? (f) Tốc độ chạy tối thiểu để vừa đuổi kịp là bao nhiêu? Khi đó phải chạy bao lâu và bao xa?

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Lúc xe rời trạm là t = 0. Sinh viên ở x = 0 chạy đều với tốc độ u. Đuôi xe ở d = 40,0 m, xuất phát nghỉ với $a=0{,}170\,\mathrm{m/s^2}$.

**Hướng đi:** Giải $ut=d+at^2/2$. Hai nghiệm có ý nghĩa khác nhau khi hai bên tiếp tục chạy. Trường hợp tốc độ nhỏ nhất ứng với phương trình có nghiệm kép, tức hai đồ thị tiếp xúc.

**Lời giải:** (a) Đặt $D=u^2-2ad$. Với u = 5,0 m/s, D > 0 và

$$
t_{1,2}=\frac{u\mp\sqrt D}{a}.
$$

Lần gặp đầu:

$$
\begin{aligned}
&t_1\approx9{,}55\,\mathrm s,\\
&x_1=ut_1\approx47{,}8\,\mathrm m.
\end{aligned}
$$

(b) Tốc độ xe lúc ấy:

$$
v_{B1}=at_1\approx1{,}62\,\mathrm{m/s}.
$$

(c) Đường của sinh viên là đường thẳng, đường của xe là parabol cong lên từ x = 40,0 m.

![Lời giải 2.88: Hai lần giao nhau nếu người chạy và xe buýt đều tiếp tục chuyển động theo mô hình](/vat-ly-1/bai-giang/img/young-02/solution-p2-88.svg)

(d) Nghiệm sau là

$$
t_2\approx49{,}3\,\mathrm s.
$$

Nếu sinh viên chưa lên xe và tiếp tục chạy, xe tăng tốc rồi đuổi kịp và vượt sinh viên tại lần gặp thứ hai. Khi đó

$$
v_{B2}=at_2\approx8{,}38\,\mathrm{m/s}.
$$

(e) Với u = 3,5 m/s, biệt thức D âm nên không có lúc gặp. Khoảng cách nhỏ nhất vẫn khoảng 3,97 m.

(f) Nghiệm kép xuất hiện khi $u_{\min}^2=2ad$:

$$
u_{\min}=\sqrt{2ad}\approx3{,}69\,\mathrm{m/s}.
$$

Thời gian và quãng đường chạy trong trường hợp ấy:

$$
t_*=\frac{u_{\min}}a\approx21{,}7\,\mathrm s,
$$

$$
x_*=u_{\min}t_*=2d=80{,}0\,\mathrm m.
$$

Tại thời điểm tiếp xúc, vận tốc xe bằng tốc độ sinh viên. Trước và sau đó xe đều ở phía trước, nên đây là trường hợp vừa đủ để chạm tới xe.

</details>

### 2.89 ••• Hai bóng bắt đầu lệch nhau một giây

Một bóng được ném thẳng đứng lên từ mép mái nhà. Bóng thứ hai được thả từ mái sau đó 1,00 s. Bỏ qua sức cản không khí.

(a) Với mái cao 20,0 m, tốc độ đầu bóng thứ nhất phải bằng bao nhiêu để hai bóng chạm đất đồng thời? Vẽ hai tọa độ theo thời gian, tính từ lần ném đầu. Tiếp theo coi tốc độ đầu $v_0$ đã biết, chiều cao h chưa biết. (b) Tìm h nếu tốc độ đầu lần lượt là (i) 6,0 m/s và (ii) 9,5 m/s. (c) Tìm ngưỡng $v_{\max}$ mà phía trên đó không có h thỏa mãn, giải thích ý nghĩa vật lý. (d) Tương tự, tìm và giải thích ngưỡng $v_{\min}$ mà phía dưới đó không có h thỏa mãn.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Độ trễ τ = 1,00 s. Bóng một được ném lên với tốc độ $v_0>0$, bóng hai được thả nghỉ. Gọi T là lúc cùng chạm đất, tính từ lần ném đầu.

**Hướng đi:** Dùng hai thời gian bay khác nhau là T và T − τ. Trừ hai phương trình để xác định điều kiện vận tốc. Giữ điều kiện h > 0 và T > τ để loại nghiệm hình thức.

**Lời giải:** Chọn gốc độ cao tại mặt đất:

$$
h+v_0T-\frac12gT^2=0,
$$

$$
h-\frac12g(T-\tau)^2=0.
$$

Trừ hai đẳng thức:

$$
v_0=g\tau-\frac{g\tau^2}{2T}.
$$

(a) Bóng hai rơi từ nghỉ trong $\sqrt{2h/g}$, nên

$$
T=\tau+\sqrt{\frac{2h}{g}}\approx3{,}0203\,\mathrm s.
$$

Thay vào biểu thức vận tốc đầu:

$$
v_0\approx8{,}18\,\mathrm{m/s}.
$$

![Lời giải 2.89: Hai bóng từ mái cao 20 m cùng tới mặt đất, bóng hai bắt đầu rơi muộn một giây](/vat-ly-1/bai-giang/img/young-02/solution-p2-89.svg)

Đường bóng hai chỉ được vẽ từ lúc bắt đầu rơi ở t = 1,00 s.

(b) Khi biết $v_0$, trước hết tìm

$$
T=\frac{g\tau^2}{2(g\tau-v_0)}.
$$

Sau đó

$$
h=\frac12g(T-\tau)^2.
$$

Với $g=9{,}80\,\mathrm{m/s^2}$, kết quả lần lượt:

$$
\begin{aligned}
h(6{,}0\,\mathrm{m/s})&\approx0{,}41\,\mathrm m,\\
h(9{,}5\,\mathrm{m/s})&\approx1{,}2\times10^3\,\mathrm m.
\end{aligned}
$$

Giá trị chưa làm tròn của trường hợp thứ hai khoảng 1152 m. Không làm tròn g thành 10 $\mathrm{m/s^2}$ ở đây vì $g\tau-v_0$ nhỏ và chiều cao rất nhạy với hiệu này.

(c) Để T dương hữu hạn, cần $v_0<g\tau$. Vì vậy

$$
v_{\max}=g\tau=9{,}80\,\mathrm{m/s}.
$$

Tại ngưỡng này, bóng một ở đỉnh đúng lúc bóng hai được thả. Hai bóng lúc đó có cùng vận tốc bằng không và sau đó cùng gia tốc, nhưng bóng một vẫn ở cao hơn. Khoảng cách không khép lại. Với tốc độ lớn hơn, bóng một còn đang đi lên khi thả bóng hai và cũng không thể cùng chạm đất.

(d) Để T > τ, biểu thức thời gian cho

$$
v_0>\frac{g\tau}{2}.
$$

Do đó

$$
v_{\min}=\frac{g\tau}{2}=4{,}90\,\mathrm{m/s}.
$$

Ở ngưỡng này, bóng một trở lại mái đúng lúc thả bóng hai. Nó đang đi xuống, trong khi bóng hai mới bắt đầu nghỉ, nên bóng một tới đất trước với mọi h > 0. Với tốc độ nhỏ hơn, bóng một đã ở dưới mái và đi xuống khi bóng hai được thả. Miền có nghiệm vật lý vì thế là khoảng mở giữa hai ngưỡng.

</details>

## Đọc hiểu khoa học: Dòng máu trong tim

Hệ tuần hoàn người là hệ kín. Máu được bơm từ tâm thất trái vào các động mạch và đi trong một hệ mạch liên tục phân nhánh. Máu qua mao mạch, rồi qua tĩnh mạch để trở về tim. Trong mỗi buồng của bốn buồng tim, máu tạm nghỉ trong thời gian ngắn trước khi được đẩy ra nhờ sự co của cơ tim.

### 2.90 Gia tốc trung bình của hồng cầu

Tâm thất trái co trong 250 ms. Cuối giai đoạn co, tốc độ dòng máu trong động mạch chủ, động mạch lớn đi ra từ tim, là 0,80 m/s. Gia tốc trung bình của hồng cầu khi rời tim là bao nhiêu?

(a) 310 $\mathrm{m/s^2}$. (b) 31 $\mathrm{m/s^2}$. (c) 3,2 $\mathrm{m/s^2}$. (d) 0,32 $\mathrm{m/s^2}$.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Hồng cầu bắt đầu từ trạng thái nghỉ trong buồng tim. Vận tốc cuối v = 0,80 m/s, thời gian Δt = 250 ms = 0,250 s.

**Hướng đi:** Gia tốc trung bình là độ biến thiên vận tốc chia thời gian. Cần đổi mili giây sang giây, không cần giả sử gia tốc tức thời không đổi.

**Lời giải:**

$$
a_{\mathrm{tb}}=\frac{0{,}80\,\mathrm{m/s}}{0{,}250\,\mathrm s}
=3{,}2\,\mathrm{m/s^2}.
$$

Chọn (c).

</details>

### 2.91 Tiết diện hai nhánh động mạch

Động mạch chủ có đường kính $d_a$, chia thành hai nhánh động mạch bằng nhau với tổng tiết diện bằng tiết diện động mạch chủ. Đường kính mỗi nhánh bằng bao nhiêu?

(a) $\sqrt{d_a}$. (b) $d_a/\sqrt2$. (c) $2d_a$. (d) $d_a/2$.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Hai nhánh có cùng đường kính d. Tổng hai diện tích hình tròn bằng diện tích của động mạch chủ.

**Hướng đi:** Diện tích tiết diện tỉ lệ với bình phương đường kính. Không chia đường kính cho hai khi diện tích bị chia đôi.

**Lời giải:** Điều kiện diện tích:

$$
2\frac{\pi d^2}{4}=\frac{\pi d_a^2}{4}.
$$

Suy ra

$$
d=\frac{d_a}{\sqrt2}.
$$

Chọn (b). Lấy nghiệm dương vì d là đường kính.

</details>

### 2.92 Đọc đồ thị dòng máu

Vận tốc máu trong động mạch chủ có thể được đo trực tiếp bằng siêu âm. Hình P2.92 cho đồ thị vận tốc theo thời gian trong một nhịp tim. Phát biểu nào giải thích đúng nhất?

(a) Dòng máu đổi chiều khoảng 0,25 s. (b) Tốc độ bắt đầu giảm khoảng 0,10 s. (c) Độ lớn gia tốc lớn nhất khoảng 0,25 s. (d) Độ lớn gia tốc lớn nhất khoảng 0,10 s.

![Hình P2.92: Vận tốc dòng máu theo thời gian trong một nhịp tim](/vat-ly-1/bai-giang/img/young-02/hinh-p2-92.png)

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Trục đứng là vận tốc, trục ngang là thời gian. Đường cong tăng nhanh, đạt đỉnh khoảng 0,25 s rồi giảm về không.

**Hướng đi:** Dấu vận tốc quyết định chiều dòng máu. Gia tốc là độ dốc tiếp tuyến, nên độ lớn gia tốc phải được so bằng độ dốc tuyệt đối, không bằng độ cao của đường cong.

**Lời giải:** Chọn (d). Gần 0,10 s, đoạn tăng có độ dốc lớn nhất về độ lớn. Ở đỉnh khoảng 0,25 s, vận tốc lớn nhất nhưng tiếp tuyến gần nằm ngang, nên gia tốc gần bằng không.

Đường cong không đi xuống phía vận tốc âm, nên không cho thấy dòng máu đổi chiều. Ở khoảng 0,10 s, tốc độ vẫn tăng. Vì vậy (a), (b) và (c) không phù hợp.

</details>
