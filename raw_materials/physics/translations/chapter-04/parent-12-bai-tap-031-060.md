## Bài tập tổng hợp và thử thách

### 4.31: Ước lượng lực khi ném bóng chày

*Độ khó: Mức 2. Tổng hợp kiến thức trước (CP).*

Ước lượng lực trung bình mà một vận động viên bóng chày chuyên nghiệp tác dụng lên bóng khi ném bóng nhanh. Biểu diễn kết quả bằng pound lực. Liệt kê các đại lượng phải ước lượng và các giả thiết. Tra cứu trên mạng để hỗ trợ lựa chọn các giá trị ước lượng.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Đây là bài ước lượng, chưa cho khối lượng bóng, tốc độ khi rời tay hoặc thời gian tăng tốc.

**Hướng đi:**

- Dùng định luật thứ hai dưới dạng lực trung bình bằng khối lượng nhân gia tốc trung bình.
- Nếu ước lượng quãng đường tay đẩy bóng thay vì thời gian, mô hình gia tốc không đổi cho liên hệ giữa tốc độ cuối và quãng đường.
- Phân biệt pound lực với đơn vị khối lượng, rồi đổi newton sang pound lực.

**Lời giải:**

Gọi khối lượng bóng là $m$, tốc độ khi rời tay là $v$, và quãng đường tăng tốc là $d$. Giả sử bóng bắt đầu gần trạng thái nghỉ và gia tốc theo hướng ném có thể coi không đổi. Khi đó:

$$
a=\frac{v^2}{2d}.
$$

Lực trung bình theo hướng ném trong mô hình:

$$
F=\frac{mv^2}{2d}.
$$

[Luật MLB 2019, mục 3.01](https://img.mlbstatic.com/mlb-images/image/upload/mlb/ub08blsefk8wkkd2oemz.pdf#page=17) quy định khối lượng bóng từ $5$ đến $5{,}25$ ounce, tương ứng khoảng $142$–$149\,\mathrm g$. Chọn $m=0{,}145\,\mathrm{kg}$ trong khoảng này.

[MLB ghi tốc độ fastball bốn đường chỉ khoảng 94 mph](https://www.mlb.com/glossary/pitch-types/four-seam-fastball). Dùng $v\approx42\,\mathrm{m/s}$ và giả sử quãng đường tăng tốc $d=1{,}0\,\mathrm m$. Quãng đường này là giả thiết ước lượng, không phải một số đo được cung cấp trong đề.

$$
\begin{aligned}
F&=\frac{(0{,}145)(42)^2}{2(1{,}0)}\\
&\approx1{,}3\times10^2\,\mathrm N.
\end{aligned}
$$

Dùng $1\,\mathrm{lb}\approx4{,}448\,\mathrm N$:

$$
F\approx29\,\mathrm{lb}.
$$

Lực này là giá trị trung bình theo hướng ném trong mô hình. Lực tức thời của bàn tay biến thiên trong động tác. Ước lượng thay đổi theo bình phương tốc độ và tỷ lệ nghịch quãng đường tăng tốc, vì vậy cần nêu rõ giả thiết khi so sánh các kết quả.
</details>

### 4.32: Trọng lượng trên hành tinh X

*Độ khó: Mức 2. Tổng hợp kiến thức trước (CP).*

Bạn vừa đặt chân tới hành tinh X. Một quả bóng khối lượng $100\,\mathrm g$ được thả từ trạng thái nghỉ ở độ cao $10{,}0\,\mathrm m$ và chạm đất sau $3{,}40\,\mathrm s$. Bỏ qua tác dụng của khí quyển. Quả bóng nặng bao nhiêu tại bề mặt hành tinh?

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Khối lượng $m=0{,}100\,\mathrm{kg}$, độ cao $h=10{,}0\,\mathrm m$, thời gian $t=3{,}40\,\mathrm s$, vận tốc đầu bằng không.

**Hướng đi:**

- Từ chuyển động rơi tự do, dùng độ cao và thời gian để xác định gia tốc trọng trường tại nơi xét.
- Dùng $w=mg_X$. Không thay bằng gia tốc trọng trường Trái Đất vì quả bóng đang ở hành tinh khác.

**Lời giải:**

$$
\begin{aligned}
h&=\frac12g_Xt^2,\\
g_X&=\frac{2h}{t^2}\\
&=\frac{20{,}0}{(3{,}40)^2}\\
&\approx1{,}73\,\mathrm{m/s^2}.
\end{aligned}
$$

Trọng lượng:

$$
\begin{aligned}
w&=mg_X\\
&=(0{,}100)(1{,}73)\\
&\approx0{,}173\,\mathrm N.
\end{aligned}
$$

Khối lượng quả bóng vẫn là $0{,}100\,\mathrm{kg}$. Gia tốc trọng trường nhỏ hơn làm trọng lượng nhỏ hơn.
</details>

### 4.33: Kéo gầu nước mà không làm đứt dây

*Độ khó: Mức 2. Tổng hợp kiến thức trước (CP).*

Một gầu nước khối lượng $5{,}60\,\mathrm{kg}$ được kéo thẳng đứng lên bằng dây có khối lượng không đáng kể. Dây chịu được lực căng lớn nhất $75{,}0\,\mathrm N$. Gầu bắt đầu từ trạng thái nghỉ. Thời gian ngắn nhất để nâng gầu lên $12{,}0\,\mathrm m$ mà không đứt dây là bao nhiêu?

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** $m=5{,}60\,\mathrm{kg}$, lực căng giới hạn $T_{\max}=75{,}0\,\mathrm N$, độ dời $h=12{,}0\,\mathrm m$. Đề không yêu cầu gầu dừng lại ở điểm cuối.

**Hướng đi:**

- Lực căng kéo lên, trọng lực kéo xuống. Giới hạn lực căng cho giới hạn gia tốc hướng lên.
- Muốn thời gian ngắn nhất khi không phải hãm ở cuối, dùng gia tốc lớn nhất trong toàn bộ quãng đường.
- Kết hợp định luật thứ hai với phương trình chuyển động từ trạng thái nghỉ.

**Lời giải:**

Chọn chiều dương hướng lên:

$$
T-mg=ma.
$$

Gia tốc lớn nhất:

$$
\begin{aligned}
a_{\max}&=\frac{T_{\max}}m-g\\
&=\frac{75{,}0}{5{,}60}-9{,}80\\
&\approx3{,}59\,\mathrm{m/s^2}.
\end{aligned}
$$

Từ $h=a_{\max}t^2/2$:

$$
\begin{aligned}
t_{\min}&=\sqrt{\frac{2h}{a_{\max}}}\\
&\approx2{,}58\,\mathrm s.
\end{aligned}
$$

Tại thời điểm đạt độ cao ấy, gầu vẫn đang đi lên. Nếu yêu cầu dừng lại tại đích, phải bổ sung giai đoạn hãm và xét một bài toán khác.
</details>

### 4.34: Hai khối có gia tốc khác nhau

*Độ khó: Mức 2.*

Khối $A$ nằm trên khối $B$ như Hình E4.26. Bàn không có ma sát, nhưng có ma sát giữa hai khối. Khối $B$ có khối lượng $6{,}00\,\mathrm{kg}$, khối $A$ có khối lượng $2{,}00\,\mathrm{kg}$. Khi kéo $B$ bằng lực ngang $12{,}0\,\mathrm N$, gia tốc của $B$ bằng $1{,}80\,\mathrm{m/s^2}$. Tìm gia tốc của $A$.

![Hình E4.26: Khối A đặt trên B và lực kéo ngang tác dụng lên B.](/vat-ly-1/bai-giang/img/young-04/parent-ex-hinh-e4-26.png)

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Biết gia tốc của khối dưới, cần tính gia tốc khối trên. Không được giả sử trước rằng hai khối có cùng gia tốc.

**Hướng đi:**

- Tách sơ đồ lực của từng khối. Ma sát của $A$ lên $B$ hướng ngược lực kéo.
- Dùng định luật thứ hai cho $B$ để suy ra độ lớn ma sát.
- Định luật thứ ba cho lực ma sát bằng độ lớn, ngược chiều trên $A$. Đây là ngoại lực ngang duy nhất của $A$.

**Lời giải:**

Chọn chiều lực kéo làm chiều dương. Với $B$:

$$
F-f=m_Ba_B.
$$

Do đó:

$$
\begin{aligned}
f&=12{,}0-(6{,}00)(1{,}80)\\
&=1{,}20\,\mathrm N.
\end{aligned}
$$

Lực ma sát trên $A$ hướng cùng chiều lực kéo:

$$
\begin{aligned}
a_A&=\frac f{m_A}\\
&=\frac{1{,}20}{2{,}00}\\
&=0{,}600\,\mathrm{m/s^2}.
\end{aligned}
$$

Hai gia tốc khác nhau, nên $A$ trượt tương đối so với $B$. Tính hợp lực của toàn hệ bằng tổng hai khối lượng nhân một gia tốc chung sẽ không đúng ở đây.
</details>

### 4.35: Lực đẩy nhỏ nhất của em bé

*Độ khó: Mức 2.*

Hai người lớn và một em bé muốn đẩy xe theo chiều $+x$ trong Hình P4.35. Hai người lớn tác dụng các lực ngang $F_1=100\,\mathrm N$ và $F_2=140\,\mathrm N$ theo các hướng trên hình.

(a) Tìm độ lớn và hướng lực nhỏ nhất mà em bé phải tác dụng. Bỏ qua ma sát.

(b) Với lực nhỏ nhất vừa tìm, xe có gia tốc $2{,}0\,\mathrm{m/s^2}$ theo chiều $+x$. Tìm trọng lượng xe.

![Hình P4.35: Hai lực người lớn hợp với chiều x các góc 60° và −30°.](/vat-ly-1/bai-giang/img/young-04/parent-ex-hinh-p4-35.png)

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Muốn xe chỉ gia tốc theo $x$, hợp lực theo $y$ phải bằng không.

**Hướng đi:**

- Tính tổng thành phần $y$ của hai lực người lớn.
- Thành phần $y$ của lực em bé phải triệt tiêu tổng ấy. Độ lớn lực nhỏ nhất khi không có thành phần $x$ dư thừa.
- Dùng hợp lực theo $x$ và gia tốc để tìm khối lượng, rồi tính trọng lượng.

**Lời giải:**

(a) Thành phần ngang của hình được giữ theo hệ trục đã chọn:

$$
\begin{aligned}
F_{1y}&=100\sin60^\circ,\\
F_{2y}&=-140\sin30^\circ.
\end{aligned}
$$

Tổng hai thành phần:

$$
\begin{aligned}
F_{1y}+F_{2y}&\approx16{,}6\,\mathrm N.
\end{aligned}
$$

Vậy em bé phải đẩy theo chiều $-y$ với lực:

$$
F_{\min}=16{,}6\,\mathrm N.
$$

Nếu thêm bất kỳ thành phần $x$ nào, độ lớn lực em bé sẽ tăng trong khi thành phần cần triệt tiêu theo $y$ không đổi.

(b) Tổng lực theo $x$:

$$
\begin{aligned}
F_x&=F_{1x}+F_{2x}\\
&=50{,}0+121{,}2\\
&\approx171\,\mathrm N.
\end{aligned}
$$

Khối lượng và trọng lượng:

$$
\begin{aligned}
m&=\frac{F_x}{a}\\
&\approx85{,}6\,\mathrm{kg},\\
w&=mg\\
&\approx8{,}4\times10^2\,\mathrm N.
\end{aligned}
$$
</details>

### 4.36: Dừng ô tô trên chiều dài bằng đường kính đồng xu

*Độ khó: Mức 3. Tổng hợp kiến thức trước (CP).*

Một quảng cáo nói rằng ô tô có thể dừng trên chiều dài chỉ bằng đường kính đồng xu. Cần hợp lực bằng bao nhiêu để dừng một xe khối lượng $850\,\mathrm{kg}$, đang chạy với tốc độ $45{,}0\,\mathrm{km/h}$, trong quãng đường $1{,}8\,\mathrm{cm}$?

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Đổi tốc độ thành $12{,}5\,\mathrm{m/s}$ và quãng đường thành $0{,}018\,\mathrm m$. Tốc độ cuối bằng không.

**Hướng đi:**

- Mô hình gia tốc hãm không đổi cho phép tính gia tốc từ tốc độ đầu, cuối và quãng đường.
- Dùng $F=ma$. Dấu âm chỉ lực ngược chiều chuyển động ban đầu.

**Lời giải:**

$$
\begin{aligned}
a&=\frac{0-v_0^2}{2d}\\
&=-\frac{(12{,}5)^2}{2(0{,}018)}\\
&\approx-4{,}34\times10^3\,\mathrm{m/s^2}.
\end{aligned}
$$

$$
\begin{aligned}
F&=ma\\
&\approx-3{,}7\times10^6\,\mathrm N.
\end{aligned}
$$

Độ lớn hợp lực cần thiết khoảng $3{,}7$ triệu newton. Kết quả cho thấy nếu hiểu quảng cáo theo nghĩa đen thì điều kiện hãm đòi hỏi rất lớn.
</details>

### 4.37: Hai thùng trên mặt hồ đóng băng

*Độ khó: Mức 1.*

Hai thùng khối lượng $4{,}00\,\mathrm{kg}$ và $6{,}00\,\mathrm{kg}$ nằm trên mặt hồ không ma sát, nối với nhau bằng dây nhẹ. Một người mang giày golf để bám mặt băng kéo thùng $6{,}00\,\mathrm{kg}$ bằng lực ngang $F$, tạo gia tốc $2{,}50\,\mathrm{m/s^2}$.

(a) Tìm gia tốc thùng $4{,}00\,\mathrm{kg}$.

(b) Vẽ sơ đồ lực của thùng $4{,}00\,\mathrm{kg}$ và tìm lực căng dây.

(c) Vẽ sơ đồ lực của thùng $6{,}00\,\mathrm{kg}$. Hợp lực hướng nào? Lực $F$ hay lực căng $T$ lớn hơn?

(d) Dùng phần (c) và định luật thứ hai để tính $F$.

![Hình P4.37: Người kéo hai thùng nối bằng dây trên mặt băng.](/vat-ly-1/bai-giang/img/young-04/parent-ex-hinh-p4-37.png)

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Dây nhẹ, căng và không dãn, mặt ngang không ma sát. Hai thùng cùng gia tốc.

**Hướng đi:**

- Ràng buộc dây không dãn xác định gia tốc hai thùng bằng nhau.
- Thùng sau chỉ chịu lực căng theo phương ngang, nên dùng nó để tìm $T$.
- Với thùng trước, lực kéo phải vừa thắng lực căng hướng ngược lại vừa tạo hợp lực tăng tốc.

**Lời giải:**

(a) Thùng $4{,}00\,\mathrm{kg}$ cũng có gia tốc $2{,}50\,\mathrm{m/s^2}$ theo chiều kéo.

(b) Sơ đồ lực của thùng sau gồm trọng lực xuống, lực pháp tuyến lên và lực căng sang phải:

![Lời giải 4.37: Sơ đồ lực riêng của hai thùng, với lực căng hướng ngược nhau trên hai thùng.](/vat-ly-1/bai-giang/img/young-04/parent-solution-4-37.svg)

$$
\begin{aligned}
n_4-4g&=0,\\
T&=4a\\
&=10{,}0\,\mathrm N.
\end{aligned}
$$

(c) Thùng trước chịu trọng lực xuống, lực pháp tuyến lên, lực kéo $F$ sang phải và lực căng $T$ sang trái. Hợp lực sang phải, nên $F>T$.

(d) Phương trình theo phương ngang:

$$
\begin{aligned}
F-T&=6a,\\
F&=T+6a\\
&=10{,}0+(6{,}00)(2{,}50)\\
&=25{,}0\,\mathrm N.
\end{aligned}
$$

Các lực do dây tác dụng lên hai thùng không phải một cặp lực tương tác trực tiếp giữa hai thùng. Mỗi lực có lực đối ứng là lực của chính thùng đó tác dụng lên dây.
</details>

### 4.38: Tìm khối lượng thùng còn lại

*Độ khó: Mức 2. Tổng hợp kiến thức trước (CP).*

Hai khối nối bằng dây nhẹ nằm yên trên mặt ngang không ma sát. Khối $A$ có khối lượng $15{,}0\,\mathrm{kg}$, khối $B$ có khối lượng $m$. Một lực ngang không đổi $F=60{,}0\,\mathrm N$ kéo khối $A$ như Hình P4.38. Trong $5{,}00\,\mathrm s$ đầu tiên, khối $A$ đi sang phải $18{,}0\,\mathrm m$.

(a) Tìm lực căng dây khi hai khối đang chuyển động.

(b) Tìm khối lượng khối $B$.

![Hình P4.38: Lực F kéo khối A, dây kéo khối B theo.](/vat-ly-1/bai-giang/img/young-04/parent-ex-hinh-p4-38.png)

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Hai khối bắt đầu đứng yên và có cùng gia tốc không đổi.

**Hướng đi:**

- Từ quãng đường và thời gian, tính gia tốc bằng động học.
- Với $A$, hợp lực ngang là $F-T$.
- Với $B$, ngoại lực ngang duy nhất là $T$, nên tìm được khối lượng chưa biết.

**Lời giải:**

$$
\begin{aligned}
a&=\frac{2s}{t^2}\\
&=\frac{2(18{,}0)}{(5{,}00)^2}\\
&=1{,}44\,\mathrm{m/s^2}.
\end{aligned}
$$

(a) Với khối $A$:

$$
\begin{aligned}
T&=F-m_Aa\\
&=60{,}0-(15{,}0)(1{,}44)\\
&=38{,}4\,\mathrm N.
\end{aligned}
$$

(b) Với khối $B$:

$$
\begin{aligned}
m&=\frac Ta\\
&=\frac{38{,}4}{1{,}44}\\
&=26{,}7\,\mathrm{kg}.
\end{aligned}
$$

Kiểm tra bằng toàn hệ cho cùng gia tốc khi lấy $60{,}0\,\mathrm N$ chia tổng khối lượng.
</details>

### 4.39: Súng thử va chạm giữa chim và máy bay

*Độ khó: Mức 1. Dùng giải tích (CALC).*

Để nghiên cứu hư hỏng khi máy bay va chạm chim lớn, bạn thiết kế một súng thử gia tốc các vật có kích thước tương đương con gà. Độ dời trong nòng là:

$$
x=At^2-Bt^3,
$$

với $A=9{,}0\times10^3\,\mathrm{m/s^2}$ và $B=8{,}0\times10^4\,\mathrm{m/s^3}$. Vật rời nòng tại $t=0{,}025\,\mathrm s$.

(a) Nòng súng cần dài bao nhiêu?

(b) Tốc độ rời nòng bằng bao nhiêu?

(c) Hợp lực tác dụng lên vật khối lượng $1{,}50\,\mathrm{kg}$ bằng bao nhiêu tại (i) $t=0$ và (ii) $t=0{,}025\,\mathrm s$?

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Biết hàm tọa độ theo thời gian, khối lượng và thời điểm ra khỏi nòng.

**Hướng đi:**

- Thay thời điểm ra khỏi nòng vào $x(t)$ để tìm chiều dài.
- Lấy đạo hàm một lần cho vận tốc, hai lần cho gia tốc.
- Dùng $F=ma(t)$ ở từng thời điểm, vì lực không cố định.

**Lời giải:**

(a) Chiều dài nòng:

$$
\begin{aligned}
L&=A(0{,}025)^2-B(0{,}025)^3\\
&=4{,}375\,\mathrm m\\
&\approx4{,}4\,\mathrm m.
\end{aligned}
$$

(b) Vận tốc:

$$
v=2At-3Bt^2.
$$

Tại thời điểm ra khỏi nòng:

$$
v=3{,}0\times10^2\,\mathrm{m/s}.
$$

(c) Gia tốc và hợp lực:

$$
\begin{aligned}
a&=2A-6Bt,\\
F&=m(2A-6Bt).
\end{aligned}
$$

Do đó:

$$
\begin{aligned}
F(0)&=2{,}7\times10^4\,\mathrm N,\\
F(0{,}025)&=9{,}0\times10^3\,\mathrm N.
\end{aligned}
$$

Hai giá trị đều hướng theo chiều chuyển động trong nòng. Gia tốc giảm nhưng vẫn dương tại lúc vật ra khỏi nòng.
</details>

### 4.40: Lực đẩy để tên lửa đạt độ cao đã định

*Độ khó: Mức 2. Tổng hợp kiến thức trước (CP).*

Một tên lửa khối lượng $400\,\mathrm{kg}$ được phóng từ mặt đất. Động cơ tạo lực đẩy không đổi hướng lên cho tới khi tên lửa lên cao $100\,\mathrm m$, rồi tắt. Muốn tên lửa đạt độ cao cực đại $400\,\mathrm m$, lực đẩy $F$ phải bằng bao nhiêu? Coi biến thiên khối lượng không đáng kể.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Tên lửa bắt đầu từ nghỉ. Có hai giai đoạn, còn động cơ và bay tự do sau khi động cơ tắt.

**Hướng đi:**

- Sau khi tắt máy, tên lửa còn lên thêm $300\,\mathrm m$ với gia tốc $-g$. Độ cao này xác định tốc độ tại thời điểm tắt máy.
- Trong $100\,\mathrm m$ đầu, tốc độ tăng từ không đến tốc độ ấy, nên tìm được gia tốc khi có động cơ.
- Lực đẩy phải tạo gia tốc hướng lên và đồng thời bù trọng lực.

**Lời giải:**

Gọi $v_1$ là tốc độ tại lúc tắt máy. Giai đoạn bay tự do cho:

$$
\begin{aligned}
0&=v_1^2-2g(300),\\
v_1^2&=5880\,\mathrm{m^2/s^2}.
\end{aligned}
$$

Trong giai đoạn có động cơ:

$$
\begin{aligned}
v_1^2&=2a(100),\\
a&=29{,}4\,\mathrm{m/s^2}.
\end{aligned}
$$

Theo định luật thứ hai:

$$
\begin{aligned}
F&=m(a+g)\\
&=(400)(29{,}4+9{,}80)\\
&\approx1{,}57\times10^4\,\mathrm N.
\end{aligned}
$$

Lực đẩy bằng bốn lần trọng lượng tên lửa. Khi động cơ tắt, lực đẩy bằng không nhưng vận tốc vẫn hướng lên cho tới điểm cao nhất.
</details>

### 4.41: Số chỉ cân trong thang máy

*Độ khó: Mức 2. Tổng hợp kiến thức trước (CP).*

Sau khi khám sức khỏe, bạn rời phòng khám, nơi cân cho trọng lượng của bạn là $683\,\mathrm N$. Bạn bước vào thang máy có một chiếc cân. Tìm độ lớn và hướng gia tốc thang máy nếu cân chỉ (a) $725\,\mathrm N$ và (b) $595\,\mathrm N$.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Trọng lượng thật $w=683\,\mathrm N$, còn số chỉ cân là lực pháp tuyến $n$ do cân tác dụng lên người.

**Hướng đi:**

- Tìm khối lượng từ trọng lượng khi đứng yên.
- Chọn chiều dương hướng lên. Hợp lực là hiệu lực pháp tuyến và trọng lượng.
- Dấu của gia tốc cho hướng, không cho biết trực tiếp thang máy đang đi lên hay đi xuống.

**Lời giải:**

$$
\begin{aligned}
m&=\frac wg,\\
n-w&=ma.
\end{aligned}
$$

Do đó:

$$
a=g\left(\frac nw-1\right).
$$

(a) Khi cân chỉ $725\,\mathrm N$:

$$
\begin{aligned}
a&=9{,}80\left(\frac{725}{683}-1\right)\\
&\approx+0{,}603\,\mathrm{m/s^2}.
\end{aligned}
$$

Gia tốc hướng lên.

(b) Khi cân chỉ $595\,\mathrm N$:

$$
\begin{aligned}
a&=9{,}80\left(\frac{595}{683}-1\right)\\
&\approx-1{,}26\,\mathrm{m/s^2}.
\end{aligned}
$$

Gia tốc hướng xuống. Số chỉ cân nhỏ hơn trọng lượng vì lực đỡ không đủ để cân bằng trọng lực.
</details>

### 4.42: Giới hạn gia tốc thang máy

*Độ khó: Mức 1.*

Thang máy và tải có tổng khối lượng $2200\,\mathrm{kg}$. Cáp đã mòn chỉ chịu được lực căng tối đa $28\,000\,\mathrm N$.

(a) Vẽ sơ đồ lực của thang máy. Viết hợp lực theo các lực trên sơ đồ và dùng định luật thứ hai để tìm gia tốc hướng lên lớn nhất mà cáp không đứt.

(b) Kết quả thay đổi thế nào nếu thang máy ở Mặt Trăng, nơi $g=1{,}62\,\mathrm{m/s^2}$?

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Cáp kéo lên, trọng lực kéo xuống. Giới hạn lực căng không thay đổi khi đổi nơi.

**Hướng đi:**

- Sơ đồ lực gồm hai ngoại lực đối nhau theo phương đứng.
- Khối lượng không đổi nên lực căng giới hạn xác định gia tốc qua $T-mg=ma$.
- Giữ cùng khối lượng, thay gia tốc trọng trường tương ứng cho mỗi thiên thể.

**Lời giải:**

(a) Chọn chiều lên dương. Sơ đồ gồm $T$ hướng lên và $mg$ hướng xuống:

![Lời giải 4.42: Lực căng cáp hướng lên và trọng lực thang máy hướng xuống.](/vat-ly-1/bai-giang/img/young-04/parent-solution-4-42.svg)

$$
F_{\mathrm{net}}=T-mg.
$$

Gia tốc lớn nhất:

$$
\begin{aligned}
a_{\max}&=\frac{T_{\max}}m-g\\
&=\frac{28\,000}{2200}-9{,}80\\
&\approx2{,}93\,\mathrm{m/s^2}.
\end{aligned}
$$

(b) Ở Mặt Trăng:

$$
\begin{aligned}
a_{\max}&=\frac{28\,000}{2200}-1{,}62\\
&\approx11{,}1\,\mathrm{m/s^2}.
\end{aligned}
$$

Trọng lượng nhỏ hơn nên với cùng lực căng giới hạn, phần hợp lực dành cho gia tốc hướng lên lớn hơn.
</details>

### 4.43: Lực trung bình của gậy lên bóng

*Độ khó: Mức 2. Tổng hợp kiến thức trước (CP).*

Quả bóng chày khối lượng $0{,}145\,\mathrm{kg}$ đang bay ngang về phía người đánh với tốc độ $40{,}0\,\mathrm{m/s}$. Sau khi bị đánh, bóng bay ngang theo chiều ngược lại với tốc độ $50{,}0\,\mathrm{m/s}$. Gậy tiếp xúc bóng trong $8{,}00\,\mathrm{ms}$. Tìm lực trung bình mà gậy tác dụng lên bóng.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Hai vận tốc ngược chiều. Thời gian tiếp xúc bằng $0{,}00800\,\mathrm s$.

**Hướng đi:**

- Chọn một chiều dương và giữ dấu của hai vận tốc.
- Tính gia tốc trung bình từ độ biến thiên vận tốc.
- Lực ngang trung bình bằng khối lượng nhân gia tốc ngang trung bình. Trọng lực theo phương đứng không đóng góp vào thành phần ngang này.

**Lời giải:**

Chọn chiều bóng rời gậy là chiều dương:

$$
\begin{aligned}
v_i&=-40{,}0\,\mathrm{m/s},\\
v_f&=+50{,}0\,\mathrm{m/s}.
\end{aligned}
$$

$$
\begin{aligned}
\Delta v&=v_f-v_i\\
&=90{,}0\,\mathrm{m/s},\\
a_{\mathrm{tb}}&=\frac{\Delta v}{\Delta t}\\
&=1{,}125\times10^4\,\mathrm{m/s^2}.
\end{aligned}
$$

$$
\begin{aligned}
F_{\mathrm{tb}}&=ma_{\mathrm{tb}}\\
&\approx1{,}63\times10^3\,\mathrm N.
\end{aligned}
$$

Lực hướng theo chiều bóng rời gậy. Lấy hiệu hai tốc độ $50-40$ sẽ bỏ mất sự đảo chiều vận tốc.
</details>

### 4.44: Hợp lực từ phương trình tọa độ

*Độ khó: Mức 2. Tổng hợp kiến thức trước (CP). Dùng giải tích (CALC).*

Vật khối lượng $m$ chuyển động trên trục $x$ theo:

$$
x(t)=at^2-2bt,
$$

trong đó $a$ và $b$ là các hằng số dương. Tìm độ lớn hợp lực tại $t=0$.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Ký hiệu $a$ trong phương trình là một hệ số dương, chưa phải chính gia tốc.

**Hướng đi:**

- Đạo hàm tọa độ hai lần theo thời gian để tìm gia tốc.
- Dùng định luật thứ hai. Cần phân biệt hệ số của $t^2$ với đạo hàm bậc hai.

**Lời giải:**

$$
\begin{aligned}
v_x&=2at-2b,\\
a_x&=\frac{dv_x}{dt}\\
&=2a.
\end{aligned}
$$

Vì gia tốc không đổi:

$$
F=2ma.
$$

Kết quả cũng đúng tại $t=0$. Hệ số $b$ quyết định vận tốc ban đầu nhưng không ảnh hưởng gia tốc.
</details>

### 4.45: Hai hộp đang đi xuống

*Độ khó: Mức 2. Tổng hợp kiến thức trước (CP).*

Hai hộp $A$ và $B$ nối với nhau bằng dây nhẹ thẳng đứng như Hình P4.45. Lực không đổi $F=80{,}0\,\mathrm N$ kéo hộp $A$ lên. Từ trạng thái nghỉ, hộp $B$ đi xuống $12{,}0\,\mathrm m$ trong $4{,}00\,\mathrm s$. Lực căng dây nối hai hộp là $36{,}0\,\mathrm N$. Tìm khối lượng (a) hộp $B$ và (b) hộp $A$.

![Hình P4.45: Lực F kéo hộp A lên, dây nối A với hộp B bên dưới.](/vat-ly-1/bai-giang/img/young-04/parent-ex-hinh-p4-45.png)

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Hai hộp có cùng gia tốc. Dù lực kéo $F$ hướng lên, chuyển động thực tế từ nghỉ là đi xuống.

**Hướng đi:**

- Dùng quãng đường và thời gian để xác định gia tốc có dấu.
- Với hộp dưới, lực căng kéo lên, trọng lực kéo xuống.
- Với hộp trên, lực căng dây nối hai hộp kéo xuống. Viết riêng định luật thứ hai cho mỗi hộp.

**Lời giải:**

Chọn chiều lên dương:

$$
\begin{aligned}
-12{,}0&=\frac12a(4{,}00)^2,\\
a&=-1{,}50\,\mathrm{m/s^2}.
\end{aligned}
$$

(a) Hộp $B$:

$$
T-m_Bg=m_Ba.
$$

$$
\begin{aligned}
m_B&=\frac T{g+a}\\
&=\frac{36{,}0}{9{,}80-1{,}50}\\
&=4{,}34\,\mathrm{kg}.
\end{aligned}
$$

(b) Hộp $A$:

$$
F-T-m_Ag=m_Aa.
$$

$$
\begin{aligned}
m_A&=\frac{F-T}{g+a}\\
&=\frac{80{,}0-36{,}0}{8{,}30}\\
&=5{,}30\,\mathrm{kg}.
\end{aligned}
$$

Trọng lượng toàn hệ lớn hơn lực kéo ngoài, phù hợp với gia tốc hướng xuống.
</details>

### 4.46: Dây nối có khối lượng

*Độ khó: Mức 2.*

Hai khối trong Hình P4.46 nối bằng dây đồng chất có khối lượng $4{,}00\,\mathrm{kg}$. Lực $200\,\mathrm N$ kéo khối trên lên.

(a) Vẽ sơ đồ lực riêng cho khối $6{,}00\,\mathrm{kg}$, dây $4{,}00\,\mathrm{kg}$ và khối $5{,}00\,\mathrm{kg}$. Với mỗi lực, chỉ rõ vật nào gây ra lực ấy.

(b) Tìm gia tốc toàn hệ.

(c) Tìm lực căng ở đầu trên của dây nặng.

(d) Tìm lực căng tại điểm giữa dây.

![Hình P4.46: Hai khối nối qua đoạn dây nặng đồng chất.](/vat-ly-1/bai-giang/img/young-04/parent-ex-hinh-p4-46.png)

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Tổng khối lượng là $15{,}00\,\mathrm{kg}$. Dây nặng nên lực căng không bằng nhau tại mọi điểm.

**Hướng đi:**

- Xét toàn hệ để tìm gia tốc, vì các lực tương tác giữa dây và hai khối là nội lực.
- Để tìm lực căng tại một vị trí, xét toàn bộ phần hệ nằm phía dưới vị trí đó.
- Dây đồng chất nên nửa dưới có khối lượng $2{,}00\,\mathrm{kg}$.

**Lời giải:**

(a) Các sơ đồ lực được xác định như sau:

- Khối trên: Lực kéo ngoài $200\,\mathrm N$ hướng lên, trọng lực do Trái Đất hướng xuống, lực kéo của đầu trên dây hướng xuống.
- Dây: Lực khối trên tác dụng lên đầu trên hướng lên, lực khối dưới tác dụng lên đầu dưới hướng xuống, trọng lực của dây hướng xuống.
- Khối dưới: Lực dây kéo lên và trọng lực do Trái Đất kéo xuống.

![Lời giải 4.46: Ba sơ đồ lực cho khối trên, dây nặng và khối dưới.](/vat-ly-1/bai-giang/img/young-04/parent-solution-4-46.svg)

(b) Chọn chiều lên dương:

$$
\begin{aligned}
200-15g&=15a,\\
a&=\frac{200}{15}-9{,}80\\
&=3{,}53\,\mathrm{m/s^2}.
\end{aligned}
$$

(c) Đầu trên dây phải kéo cả dây và khối dưới, tổng khối lượng $9{,}00\,\mathrm{kg}$:

$$
\begin{aligned}
T_{\mathrm{tren}}&=9(g+a)\\
&=120\,\mathrm N.
\end{aligned}
$$

(d) Điểm giữa kéo nửa dưới dây và khối dưới, tổng khối lượng $7{,}00\,\mathrm{kg}$:

$$
\begin{aligned}
T_{\mathrm{giua}}&=7(g+a)\\
&=93{,}3\,\mathrm N.
\end{aligned}
$$

Đầu dưới chỉ kéo khối $5{,}00\,\mathrm{kg}$, nên lực căng ở đó là $66{,}7\,\mathrm N$. Lực căng tăng khi đi lên dọc dây vì phải kéo thêm phần dây nằm bên dưới.
</details>

### 4.47: Hạ cánh mềm cho tên lửa

*Độ khó: Mức 3. Tổng hợp kiến thức trước (CP).*

Một tên lửa nhỏ khối lượng $20{,}0\,\mathrm{kg}$ đang rơi tự do về Trái Đất. Bỏ qua lực cản không khí. Khi ở độ cao $80{,}0\,\mathrm m$, tên lửa đang đi xuống với tốc độ $30{,}0\,\mathrm{m/s}$. Đúng lúc ấy động cơ bật, tạo lực hướng lên không đổi $F$. Coi khối lượng không đổi. Tìm $F$ để tốc độ tên lửa bằng không đúng lúc tới mặt đất.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Cần hãm vận tốc đi xuống về không trong độ dời $80{,}0\,\mathrm m$.

**Hướng đi:**

- Chọn chiều lên dương. Vận tốc đầu và độ dời đều âm, nhưng gia tốc hãm phải dương.
- Dùng phương trình động học không chứa thời gian.
- Lực đẩy động cơ lớn hơn hợp lực hãm vì còn phải bù trọng lực.

**Lời giải:**

$$
\begin{aligned}
v_f^2&=v_i^2+2a\Delta y,\\
0&=30{,}0^2+2a(-80{,}0),\\
a&=5{,}625\,\mathrm{m/s^2}.
\end{aligned}
$$

Định luật thứ hai:

$$
\begin{aligned}
F&=m(g+a)\\
&=(20{,}0)(9{,}80+5{,}625)\\
&\approx309\,\mathrm N.
\end{aligned}
$$

Tên lửa vẫn đi xuống trong giai đoạn hãm nhưng gia tốc hướng lên. Lấy lực đẩy bằng $ma$ sẽ bỏ quên trọng lực.
</details>

### 4.48: Trọng lượng dụng cụ trên Newtonia

*Độ khó: Mức 2. Tổng hợp kiến thức trước (CP).*

Bạn hạ cánh xuống hành tinh chưa biết tên Newtonia và muốn xác định trọng lượng của các vật ở đó. Trên mặt ngang không ma sát, lực $12{,}0\,\mathrm N$ đẩy một dụng cụ bắt đầu từ nghỉ đi được $16{,}0\,\mathrm m$ trong $2{,}00\,\mathrm s$. Khi thả dụng cụ từ nghỉ ở độ cao $10{,}0\,\mathrm m$, nó chạm đất sau $2{,}58\,\mathrm s$. Dụng cụ nặng bao nhiêu trên Newtonia và trên Trái Đất?

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Thí nghiệm ngang xác định khối lượng quán tính. Thí nghiệm rơi xác định gia tốc trọng trường.

**Hướng đi:**

- Dùng động học của chuyển động ngang từ nghỉ để tính gia tốc, rồi dùng $F=ma$ để tìm khối lượng.
- Tính gia tốc rơi từ độ cao và thời gian.
- Khối lượng không đổi giữa hai hành tinh, còn trọng lượng phụ thuộc gia tốc trọng trường.

**Lời giải:**

Gia tốc ngang:

$$
\begin{aligned}
a_x&=\frac{2s}{t^2}\\
&=\frac{2(16{,}0)}{(2{,}00)^2}\\
&=8{,}00\,\mathrm{m/s^2}.
\end{aligned}
$$

Khối lượng:

$$
m=\frac{12{,}0}{8{,}00}=1{,}50\,\mathrm{kg}.
$$

Gia tốc trọng trường Newtonia:

$$
\begin{aligned}
g_N&=\frac{2h}{t_r^2}\\
&=\frac{20{,}0}{(2{,}58)^2}\\
&\approx3{,}00\,\mathrm{m/s^2}.
\end{aligned}
$$

Hai trọng lượng:

$$
\begin{aligned}
w_N&=mg_N\\
&\approx4{,}51\,\mathrm N,\\
w_E&=m(9{,}80)\\
&=14{,}7\,\mathrm N.
\end{aligned}
$$
</details>

### 4.49: Lực tăng tuyến tính theo thời gian

*Độ khó: Mức 2. Tổng hợp kiến thức trước (CP). Dùng giải tích (CALC).*

Một vật bí ẩn có động cơ tên lửa, khối lượng $45{,}0\,\mathrm{kg}$, ban đầu nằm yên giữa mặt hồ đóng băng nằm ngang không ma sát. Từ lúc $t=0$, lực hướng đông tác dụng lên vật có độ lớn:

$$
F(t)=kt,\qquad k=16{,}8\,\mathrm{N/s}.
$$

Trong $5{,}00\,\mathrm s$ đầu tiên, vật đi được bao xa?

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Lực và gia tốc tăng theo thời gian. Vận tốc đầu bằng không.

**Hướng đi:**

- Dùng $a(t)=F(t)/m$, không dùng một gia tốc không đổi.
- Tích phân gia tốc để tìm vận tốc, dùng điều kiện đầu.
- Tích phân vận tốc để tìm độ dời. Vì vật luôn đi về phía đông, quãng đường bằng độ lớn độ dời.

**Lời giải:**

$$
a(t)=\frac{k}{m}t.
$$

Từ $v(0)=0$:

$$
\begin{aligned}
v(t)&=\int_0^t\frac{k}{m}\tau\,d\tau\\
&=\frac{k}{2m}t^2.
\end{aligned}
$$

Chọn $x(0)=0$:

$$
\begin{aligned}
x(t)&=\int_0^t\frac{k}{2m}\tau^2\,d\tau\\
&=\frac{k}{6m}t^3.
\end{aligned}
$$

$$
\begin{aligned}
x(5{,}00)&=\frac{16{,}8(5{,}00)^3}{6(45{,}0)}\\
&=7{,}78\,\mathrm m.
\end{aligned}
$$
</details>

### 4.50: Gấp đôi lực, so sánh hai điều kiện

*Độ khó: Mức 2. Tổng hợp kiến thức trước (CP).*

Từ $t=0$, hợp lực tác dụng lên vật đang đứng yên.

(a) Khi hợp lực không đổi $F_1$ tác dụng trong quãng đường $d$, tốc độ cuối là $v_1$. Nếu hợp lực tăng thành $F_2=2F_1$ nhưng vật vẫn đi cùng quãng đường $d$, tốc độ cuối $v_2$ theo $v_1$ bằng bao nhiêu?

(b) Khi hợp lực $F_1$ tác dụng trong thời gian $T$, tốc độ cuối là $v_1$. Nếu lực tăng thành $F_2=2F_1$ và vẫn tác dụng trong cùng thời gian $T$, tốc độ cuối là bao nhiêu?

Tích lực với quãng đường liên hệ tới công, còn tích lực với thời gian liên hệ tới xung lượng, được xét ở những chương sau.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Vật bắt đầu từ nghỉ, khối lượng không đổi. Câu (a) giữ quãng đường, câu (b) giữ thời gian.

**Hướng đi:**

- Lực tăng gấp đôi làm gia tốc tăng gấp đôi.
- Với cùng quãng đường, dùng liên hệ giữa bình phương tốc độ và gia tốc.
- Với cùng thời gian, tốc độ tỷ lệ trực tiếp với gia tốc.

**Lời giải:**

(a) Từ $v^2=2ad$:

$$
\begin{aligned}
\frac{v_2^2}{v_1^2}&=\frac{a_2}{a_1}\\
&=2,\\
v_2&=\sqrt2\,v_1.
\end{aligned}
$$

(b) Từ $v=aT$:

$$
\begin{aligned}
\frac{v_2}{v_1}&=\frac{a_2}{a_1}\\
&=2,\\
v_2&=2v_1.
\end{aligned}
$$

Hai kết quả khác nhau vì giữ cùng quãng đường không đồng nghĩa giữ cùng thời gian tác dụng lực.
</details>

### 4.51: So sánh lực tăng tốc của các ô tô

*Độ khó: Mức 2. Phân tích số liệu (DATA).*

Bảng sau cho khối lượng và thời gian tăng tốc từ nghỉ đến $60\,\mathrm{mph}$ của một số xe.

| Xe và năm sản xuất | Khối lượng (kg) | Thời gian tới 60 mph (s) |
| --- | ---: | ---: |
| Alpha Romeo 4C (2013) | 895 | 4,4 |
| Honda Civic 2.0i (2011) | 1320 | 6,4 |
| Ferrari F430 (2004) | 1435 | 3,9 |
| Ford Focus RS500 (2010) | 1468 | 5,4 |
| Volvo S60 (2013) | 1650 | 7,2 |

(a) Xe nào chịu hợp lực trung bình lớn nhất và nhỏ nhất trong giai đoạn tăng tốc này?

(b) Với hành khách khối lượng $72{,}0\,\mathrm{kg}$, hợp lực trung bình lên người đó lớn nhất và nhỏ nhất khi ngồi trong xe nào?

(c) Ferrari F430 tăng tốc từ nghỉ tới $100\,\mathrm{mph}$ trong $8{,}6\,\mathrm s$. Tìm hợp lực trung bình lên xe và so với giai đoạn tới $60\,\mathrm{mph}$. Giải thích vì sao hai lực trung bình có thể khác nhau.

(d) Vì sao xe có tốc độ tối đa? Hợp lực lên Ferrari F430 bằng bao nhiêu khi xe chạy với tốc độ tối đa $196\,\mathrm{mph}$?

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Dữ liệu mô tả cả xe, còn câu (b) xét riêng hành khách có cùng khối lượng trong mọi trường hợp.

**Hướng đi:**

- Đổi mph sang mét trên giây, dùng gia tốc trung bình là độ biến thiên vận tốc chia thời gian.
- Hợp lực trung bình lên xe phụ thuộc cả khối lượng xe lẫn thời gian tăng tốc.
- Với cùng hành khách, chỉ cần so sánh gia tốc.
- Tốc độ tối đa không đồng nghĩa không có lực kéo. Khi chạy thẳng đều, lực kéo cân bằng các lực cản.

**Lời giải:**

Đổi đơn vị:

$$
60\,\mathrm{mph}=26{,}8224\,\mathrm{m/s}.
$$

Với mỗi xe và hành khách:

$$
\begin{aligned}
a_{\mathrm{tb}}&=\frac{\Delta v}{\Delta t},\\
F_{\mathrm{xe}}&=m_{\mathrm{xe}}a_{\mathrm{tb}},\\
F_{\mathrm{nguoi}}&=72{,}0a_{\mathrm{tb}}.
\end{aligned}
$$

| Xe | Hợp lực lên xe (N) | Hợp lực lên hành khách (N) |
| --- | ---: | ---: |
| Alpha Romeo 4C | 5456 | 439 |
| Honda Civic 2.0i | 5532 | 302 |
| Ferrari F430 | 9869 | 495 |
| Ford Focus RS500 | 7292 | 358 |
| Volvo S60 | 6147 | 268 |

(a) Ferrari có hợp lực trung bình lớn nhất. Alpha Romeo có hợp lực trung bình nhỏ nhất.

(b) Hành khách chịu hợp lực trung bình lớn nhất trong Ferrari và nhỏ nhất trong Volvo. Khối lượng xe không trực tiếp được nhân vào lực trên hành khách.

(c) Từ $100\,\mathrm{mph}=44{,}704\,\mathrm{m/s}$:

$$
\begin{aligned}
F_{\mathrm{tb}}&=\frac{m\Delta v}{\Delta t}\\
&=\frac{(1435)(44{,}704)}{8{,}6}\\
&\approx7{,}5\times10^3\,\mathrm N.
\end{aligned}
$$

Giá trị chưa làm tròn bằng khoảng $0{,}756$ lần hợp lực trung bình trong giai đoạn tới $60\,\mathrm{mph}$. Hai khoảng tăng tốc khác nhau có thể có lực kéo và lực cản khác nhau. Lực cản không khí tăng khi xe chạy nhanh hơn, còn lực kéo cũng thay đổi theo chế độ động cơ và số truyền.

(d) Tốc độ tối đa đạt được khi lực kéo sẵn có cân bằng tổng lực cản. Nếu xe giữ tốc độ ấy trên đường thẳng:

$$
F_{\mathrm{net}}=0.
$$

Động cơ vẫn có thể tạo lực kéo khác không. Hợp lực bằng không vì các lực cân bằng nhau.
</details>

### 4.52: Hợp lực lên trực thăng thử nghiệm

*Độ khó: Mức 3. Dùng giải tích (CALC).*

Một trực thăng huấn luyện có trọng lượng $2{,}75\times10^5\,\mathrm N$. Trong chuyến thử, tọa độ của nó thỏa mãn:

$$
\begin{aligned}
x(t)&=At^3,\\
y(t)&=Bt,\\
z(t)&=-Ct^2,
\end{aligned}
$$

với $A=0{,}020\,\mathrm{m/s^3}$, $B=2{,}2\,\mathrm{m/s}$ và $C=0{,}060\,\mathrm{m/s^2}$. Nghĩa là vector vị trí bằng $x\hat i+y\hat j+z\hat k$. Tìm hợp lực tại $t=5{,}0\,\mathrm s$.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Trọng lượng cho phép suy ra khối lượng. Phương trình tọa độ cho ba thành phần gia tốc.

**Hướng đi:**

- Lấy đạo hàm bậc hai riêng từng tọa độ.
- Dùng hợp lực vector bằng khối lượng nhân vector gia tốc.
- Không cộng thêm trọng lực vào $m\vec a$, vì đại lượng này đã là tổng tất cả ngoại lực.

**Lời giải:**

$$
m=\frac{w}{g}\approx2{,}81\times10^4\,\mathrm{kg}.
$$

Các thành phần gia tốc:

$$
\begin{aligned}
a_x&=6At,\\
a_y&=0,\\
a_z&=-2C.
\end{aligned}
$$

Tại $t=5{,}0\,\mathrm s$:

$$
\begin{aligned}
a_x&=0{,}60\,\mathrm{m/s^2},\\
a_y&=0,\\
a_z&=-0{,}12\,\mathrm{m/s^2}.
\end{aligned}
$$

Vì thế:

$$
\begin{aligned}
F_x&\approx1{,}7\times10^4\,\mathrm N,\\
F_y&=0,\\
F_z&\approx-3{,}4\times10^3\,\mathrm N.
\end{aligned}
$$

Vector hợp lực có thành phần theo $+x$ và $-z$, không có thành phần theo $y$ dù trực thăng vẫn chuyển động theo phương ấy.
</details>

### 4.53: Đo khối lượng và trọng trường trên hành tinh khác

*Độ khó: Mức 2. Phân tích số liệu (DATA).*

Bạn là thuyền trưởng Starfleet và tới một hành tinh xa. Trong phòng thử nghiệm, một dây ngắn nhẹ buộc vào đầu trên khối có khối lượng $m$. Lực hướng lên không đổi $F$ tác dụng ở đầu tự do. Khối bắt đầu từ nghỉ. Thời gian đi lên $8{,}00\,\mathrm m$ được đo khi thay đổi lực:

| F (N) | Thời gian (s) |
| ---: | ---: |
| 250 | 3,3 |
| 300 | 2,2 |
| 350 | 1,7 |
| 400 | 1,5 |
| 450 | 1,3 |
| 500 | 1,2 |

(a) Vẽ đồ thị $F$ theo gia tốc $a$ của khối.

(b) Từ đồ thị, xác định khối lượng $m$ và gia tốc trọng trường $g$ tại bề mặt hành tinh. Các số đo có sai số thực nghiệm.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Mỗi phép đo có lực không đổi và chuyển động từ nghỉ trên cùng độ dời.

**Hướng đi:**

- Tính gia tốc từ độ dời và từng thời gian đo.
- Định luật thứ hai cho $F=ma+mg$. Vì vậy hệ số góc của đường thẳng là khối lượng, tung độ gốc là trọng lượng.
- Dùng nhiều điểm để giảm ảnh hưởng của số đo làm tròn, không ép đường thẳng qua gốc.

**Lời giải:**

(a) Với từng thời gian:

$$
a=\frac{2s}{t^2}=\frac{16{,}00}{t^2}.
$$

| a (m/s²) | F (N) |
| ---: | ---: |
| 1,469 | 250 |
| 3,306 | 300 |
| 5,536 | 350 |
| 7,111 | 400 |
| 9,467 | 450 |
| 11,111 | 500 |

![Lời giải 4.53: Các điểm thực nghiệm và đường thẳng khớp F theo a.](/vat-ly-1/bai-giang/img/young-04/parent-solution-4-53.svg)

(b) Viết đường thẳng khớp dạng:

$$
F=Ma+B.
$$

Bình phương tối thiểu không trọng số với các số đo trong bảng cho:

$$
\begin{aligned}
M&\approx25{,}58\,\mathrm{kg},\\
B&\approx212{,}98\,\mathrm N.
\end{aligned}
$$

Đối chiếu với $F=ma+mg$:

$$
\begin{aligned}
m&=M\approx26\,\mathrm{kg},\\
g&=\frac BM\\
&\approx8{,}3\,\mathrm{m/s^2}.
\end{aligned}
$$

Giá trị đọc từ đường thẳng vẽ tay có thể khác đôi chút. Vì thời gian chỉ được cho tới một chữ số thập phân, không nên xem các chữ số lẻ của kết quả khớp là độ chính xác thực nghiệm.
</details>

### 4.54: Lực cản khi hộp trượt chậm dần

*Độ khó: Mức 2. Phân tích số liệu (DATA).*

Một hộp khối lượng $8{,}00\,\mathrm{kg}$ nằm trên sàn ngang. Sau cú đẩy nhanh, hộp trượt $8{,}22\,\mathrm m$ trong $2{,}8\,\mathrm s$ rồi dừng.

(a) Với cú đẩy khác, hộp trượt $4{,}20\,\mathrm m$ trong $2{,}0\,\mathrm s$ rồi dừng. Bạn có cho rằng gia tốc khi hộp chậm dần là không đổi không? Giải thích.

(b) Thêm sách vào hộp và lặp lại phép đo, thu được bảng sau. Cú đẩy có tạo cùng tốc độ đầu trong mọi lần không? Tìm tỷ số tốc độ đầu lớn nhất và nhỏ nhất.

| Khối lượng thêm (kg) | Quãng đường (m) | Thời gian (s) |
| ---: | ---: | ---: |
| 0 | 8,22 | 2,8 |
| 3,00 | 10,75 | 3,2 |
| 7,00 | 9,45 | 3,0 |
| 12,0 | 7,10 | 2,6 |

(c) Lực ngang trung bình $f$ của sàn lên hộp có bằng nhau trong các lần không? Vẽ độ lớn $f$ theo tổng khối lượng $m$ của hộp và sách, rồi xác định biểu thức $f(m)$.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Sau cú đẩy ban đầu, hộp trượt cho tới khi dừng. Tổng khối lượng bằng khối lượng hộp cộng khối lượng thêm.

**Hướng đi:**

- Trong mô hình gia tốc không đổi và vận tốc cuối bằng không, tốc độ đầu bằng hai lần tốc độ trung bình.
- Dùng dữ kiện hai lần đầu để kiểm tra xem độ lớn gia tốc có nhất quán không.
- Từ gia tốc hãm và tổng khối lượng, tính độ lớn lực cản rồi xét đồ thị.

**Lời giải:**

Với gia tốc không đổi:

$$
\begin{aligned}
s&=\frac{v_0+0}{2}t,\\
v_0&=\frac{2s}{t},\\
a&=-\frac{2s}{t^2}.
\end{aligned}
$$

(a) Hai phép đo cho:

$$
\begin{aligned}
a_1&\approx-2{,}097\,\mathrm{m/s^2},\\
a_2&=-2{,}10\,\mathrm{m/s^2}.
\end{aligned}
$$

Các kết quả gần bằng nhau, nên phù hợp với mô hình gia tốc hãm không đổi. Hai phép đo chưa chứng minh được mọi chi tiết của gia tốc theo thời gian, nhưng ủng hộ mô hình trong độ chính xác đã cho.

(b) Áp dụng cho bốn hàng:

| Tổng khối lượng (kg) | Tốc độ đầu (m/s) | Độ lớn lực cản (N) |
| ---: | ---: | ---: |
| 8,00 | 5,871 | 16,78 |
| 11,00 | 6,719 | 23,10 |
| 15,00 | 6,300 | 31,50 |
| 20,00 | 5,462 | 42,01 |

Các tốc độ đầu khác nhau. Tỷ số lớn nhất trên nhỏ nhất:

$$
\frac{v_{\max}}{v_{\min}}\approx1{,}23.
$$

(c) Độ lớn lực cản:

$$
f=m|a|=\frac{2ms}{t^2}.
$$

Các lực không bằng nhau mà gần tỷ lệ với tổng khối lượng.

![Lời giải 4.54: Độ lớn lực cản tăng gần tuyến tính với tổng khối lượng.](/vat-ly-1/bai-giang/img/young-04/parent-solution-4-54.svg)

Đường khớp qua gốc cho:

$$
f\approx(2{,}10\,\mathrm{m/s^2})m.
$$

Nếu cho phép tung độ gốc tự do, kết quả khoảng $-0{,}041\,\mathrm N$, nhỏ so với các lực đo được. Vì vậy mô hình tỷ lệ thuận là phù hợp với các số liệu đã làm tròn.
</details>

### 4.55: Lực đổi dấu và vị trí xa nhất

*Độ khó: Mức 3. Tổng hợp kiến thức trước (CP). Dùng giải tích (CALC). Bài tập thử thách.*

Khối $2{,}00\,\mathrm{kg}$ ban đầu đứng yên tại $x=0$ trên mặt ngang không ma sát. Từ $t=0$, lực ngang tác dụng là:

$$
F_x(t)=b-at,
$$

với $a=6{,}00\,\mathrm{N/s}$ và $b=4{,}00\,\mathrm N$.

(a) Tìm giá trị dương lớn nhất của $x$, thời gian để tới vị trí ấy, và độ lớn lực tại đó.

(b) Sau bao lâu khối trở lại $x=0$? Tốc độ lúc ấy bằng bao nhiêu?

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Hằng số $a$ là hệ số của lực, không phải gia tốc. Lực ban đầu dương rồi đổi dấu.

**Hướng đi:**

- Tích phân gia tốc $F_x/m$ để tìm vận tốc và tọa độ.
- Vị trí lớn nhất đạt khi vận tốc đổi từ dương sang âm. Lực bằng không chỉ đánh dấu vận tốc cực đại, không phải tọa độ cực đại.
- Để tìm lần trở lại gốc, lấy nghiệm dương khác không của $x(t)=0$.

**Lời giải:**

Từ điều kiện đầu:

$$
\begin{aligned}
v_x(t)&=\frac{bt}{m}-\frac{at^2}{2m},\\
x(t)&=\frac{bt^2}{2m}-\frac{at^3}{6m}.
\end{aligned}
$$

(a) Ngoài nghiệm $t=0$, vận tốc bằng không tại:

$$
\begin{aligned}
t_*&=\frac{2b}{a}\\
&=\frac43\,\mathrm s\\
&\approx1{,}33\,\mathrm s.
\end{aligned}
$$

Trước $t_*$ vận tốc dương, sau đó âm. Vì thế đây là điểm xa nhất theo chiều dương:

$$
\begin{aligned}
x_{\max}&=\frac{2b^3}{3ma^2}\\
&\approx0{,}593\,\mathrm m.
\end{aligned}
$$

Lực tại đó:

$$
F_x(t_*)=b-2b=-4{,}00\,\mathrm N.
$$

Độ lớn lực bằng $4{,}00\,\mathrm N$ và hướng theo $-x$.

(b) Phân tích nhân tử:

$$
x(t)=\frac{t^2}{6m}(3b-at).
$$

Nghiệm dương khác không:

$$
t_r=\frac{3b}{a}=2{,}00\,\mathrm s.
$$

Thay vào vận tốc:

$$
\begin{aligned}
v_x(t_r)&=-\frac{3b^2}{2ma}\\
&=-2{,}00\,\mathrm{m/s}.
\end{aligned}
$$

Tốc độ lúc trở về gốc bằng $2{,}00\,\mathrm{m/s}$, chuyển động theo chiều âm.
</details>

### 4.56: Lực ngang phụ thuộc tọa độ đứng

*Độ khó: Mức 3. Dùng giải tích (CALC). Bài tập thử thách.*

Một vật khối lượng $m$ ban đầu đứng yên, cân bằng tại gốc tọa độ. Từ $t=0$, một lực mới có các thành phần:

$$
\begin{aligned}
F_x(t)&=k_1+k_2y,\\
F_y(t)&=k_3t,
\end{aligned}
$$

trong đó $k_1,k_2,k_3$ là hằng số. Tìm các vector vị trí và vận tốc theo thời gian.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Ban đầu $x=y=v_x=v_y=0$. Các lực đã cân bằng trước khi thêm lực mới được coi vẫn triệt tiêu nhau.

**Hướng đi:**

- Giải phương đứng trước vì lực $F_y$ chỉ phụ thuộc thời gian.
- Thay $y(t)$ vào lực ngang. Không được thay $k_2y$ bằng $k_2t$.
- Tích phân hai lần và áp dụng đủ các điều kiện đầu.

**Lời giải:**

Theo phương đứng:

$$
\begin{aligned}
a_y&=\frac{k_3}{m}t,\\
v_y(t)&=\frac{k_3}{2m}t^2,\\
y(t)&=\frac{k_3}{6m}t^3.
\end{aligned}
$$

Thay vào phương ngang:

$$
\begin{aligned}
a_x(t)&=\frac{k_1+k_2y(t)}m\\
&=\frac{k_1}m+\frac{k_2k_3}{6m^2}t^3.
\end{aligned}
$$

Tích phân:

$$
v_x(t)=\frac{k_1}mt+\frac{k_2k_3}{24m^2}t^4.
$$

$$
x(t)=\frac{k_1}{2m}t^2+\frac{k_2k_3}{120m^2}t^5.
$$

Vì vậy:

$$
\begin{aligned}
\vec v(t)&=v_x(t)\hat i+v_y(t)\hat j,\\
\vec r(t)&=x(t)\hat i+y(t)\hat j.
\end{aligned}
$$

Các thành phần ở trên cho đầy đủ biểu thức của hai vector. Đạo hàm lại cho đúng các thành phần lực đã cho và mọi điều kiện đầu.
</details>

## Đọc hiểu khoa học: Lực lên cơ thể vũ công

*Nhóm câu hỏi kiểu MCAT. Ứng dụng sinh học.*

Vũ công chịu những lực lớn khi nhảy và tiếp đất. Chẳng hạn, khi tiếp đất sau cú nhảy thẳng đứng, lực cổ tác dụng lên đầu phải vượt trọng lượng đầu để làm đầu chậm lại và dừng. Khối lượng đầu chiếm khoảng $9{,}4\%$ khối lượng cơ thể. Phân tích video một vũ công khối lượng $65\,\mathrm{kg}$ cho thấy khi tiếp đất, đầu giảm tốc từ $4{,}0\,\mathrm{m/s}$ xuống không trong $0{,}20\,\mathrm s$.

### 4.57: Lực trung bình của cổ lên đầu khi tiếp đất

Độ lớn lực trung bình của cổ tác dụng lên đầu trong giai đoạn tiếp đất là bao nhiêu?

(a) $0\,\mathrm N$.

(b) $60\,\mathrm N$.

(c) $120\,\mathrm N$.

(d) $180\,\mathrm N$.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Khối lượng đầu $m_h=0{,}094(65)=6{,}11\,\mathrm{kg}$. Đầu đang đi xuống rồi dừng.

**Hướng đi:**

- Gia tốc khi hãm hướng lên. Chọn chiều lên dương và tính độ biến thiên vận tốc có dấu.
- Lực cổ kéo lên phải vừa bù trọng lực vừa tạo gia tốc hãm.

**Lời giải:**

$$
\begin{aligned}
a&=\frac{0-(-4{,}0)}{0{,}20}\\
&=20\,\mathrm{m/s^2}.
\end{aligned}
$$

$$
\begin{aligned}
F_{\mathrm{co}}&=m_h(g+a)\\
&=(6{,}11)(9{,}80+20)\\
&\approx182\,\mathrm N.
\end{aligned}
$$

Với độ chính xác các lựa chọn, chọn **(d) $180\,\mathrm N$**. Giá trị khoảng $120\,\mathrm N$ chỉ là hợp lực, chưa phải lực cổ lên đầu.
</details>

### 4.58: Lực của đầu lên cổ

So với lực cổ tác dụng lên đầu trong lúc tiếp đất, lực đầu tác dụng lên cổ:

(a) Có cùng độ lớn.

(b) Lớn hơn.

(c) Nhỏ hơn.

(d) Lớn hơn trong nửa đầu và nhỏ hơn trong nửa sau giai đoạn tiếp đất.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** So sánh hai lực của cùng tương tác giữa đầu và cổ.

**Hướng đi:**

- Định luật thứ ba áp dụng tại mỗi thời điểm, kể cả khi lực và gia tốc đang biến thiên.
- Phân biệt hai lực tác dụng lên hai bộ phận khác nhau với hợp lực trên riêng đầu.

**Lời giải:**

Chọn **(a)**. Đầu và cổ tác dụng lên nhau hai lực bằng độ lớn, ngược hướng. Điều này không phụ thuộc đầu đang nhanh dần, chậm dần hay chuyển động đều. Vì chúng tác dụng lên hai vật khác nhau, không được cộng hai lực ấy để tính hợp lực lên riêng đầu.
</details>

### 4.59: Lực cổ lên đầu khi vũ công đang ở trên không

Khi vũ công đang ở trên không và giữ một tư thế cố định, độ lớn lực cổ tác dụng lên đầu bằng bao nhiêu?

(a) $0\,\mathrm N$.

(b) $60\,\mathrm N$.

(c) $120\,\mathrm N$.

(d) $180\,\mathrm N$.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Xét mô hình bỏ qua lực cản không khí. Đầu và phần thân cùng rơi tự do, giữ tư thế tương đối.

**Hướng đi:**

- Dù đầu không chuyển động tương đối so với thân, cả hai vẫn có gia tốc trọng trường.
- Viết định luật thứ hai với gia tốc hướng xuống bằng $g$, không đặt gia tốc bằng không.

**Lời giải:**

Chọn chiều lên dương:

$$
F_{\mathrm{co}}-m_hg=m_h(-g).
$$

Suy ra:

$$
F_{\mathrm{co}}=0.
$$

Chọn **(a)**. Trọng lực đã tạo đúng gia tốc rơi của đầu. Giá trị gần $60\,\mathrm N$ tương ứng lực đỡ khi đứng yên, không phải khi toàn cơ thể đang rơi tự do.
</details>

### 4.60: Đọc đồ thị lực của tấm đo

Một vũ công nhảy trên tấm đo lực, ghi lại lực giữa bàn chân và mặt sàn theo thời gian như Hình P4.60. Tại $t=0{,}4\,\mathrm s$, điều gì đang xảy ra?

(a) Vũ công gập chân, làm cơ thể gia tốc xuống dưới.

(b) Vũ công đẩy người lên và sắp rời mặt đất.

(c) Vũ công đang ở trên không, tại đỉnh cú nhảy.

(d) Vũ công đang tiếp đất và bàn chân vừa chạm sàn.

![Hình P4.60: Lực giữa bàn chân vũ công và tấm đo trong toàn bộ cú nhảy.](/vat-ly-1/bai-giang/img/young-04/parent-ex-hinh-p4-60.png)

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Lực ban đầu khi đứng yên xấp xỉ trọng lượng cơ thể. Tại $0{,}4\,\mathrm s$, lực trên đồ thị nhỏ hơn mức ban đầu nhưng chưa bằng không.

**Hướng đi:**

- Lực tấm đo biểu diễn độ lớn lực tiếp xúc thẳng đứng. Theo định luật thứ ba, độ lớn lực sàn đẩy người bằng độ lớn người ép sàn.
- So sánh lực đỡ với trọng lượng để suy ra chiều gia tốc.
- Phân biệt lực đỡ nhỏ hơn trọng lượng với lực đỡ bằng không trong giai đoạn bay.

**Lời giải:**

Chọn chiều lên dương:

$$
ma=N-mg.
$$

Tại $0{,}4\,\mathrm s$, đồ thị cho $N<mg$, nên $a<0$. Vũ công đang hạ người bằng cách gập chân, làm khối tâm gia tốc xuống. Chọn **(a)**.

Giai đoạn lực bằng không xuất hiện về sau, khi chân không tiếp xúc tấm đo. Đỉnh lực lớn sau giai đoạn ấy thuộc quá trình tiếp đất.
</details>
