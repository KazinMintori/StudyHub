## Bài tập nâng cao 36.65–36.68

::: exercise 36.65
Một vách chắn sáng gồm màng trong và màng ngoài trượt qua nhau như Hình P36.65. Mỗi màng có các khe song song rộng a, cách nhau d. Màn quan sát là cung tròn chắn góc $60^\circ$ tại trung điểm cố định giữa hai khe. Laser xanh lục $532\,\mathrm{nm}$ chiếu từ trái. Màng ngoài đi lên, màng trong đi xuống với cùng tốc độ v nhờ các động cơ nano.

Ở $t=0$, điểm P trên màng ngoài sát điểm Q trên màng trong, nên độ mở hiệu dụng bằng không. Khẩu độ đóng hoàn toàn lần tiếp theo ở $t=3{,}00\,\mathrm s$.

(a) Ở $t=1{,}00\,\mathrm s$, có 19 đốm sáng cách đều và cường độ xấp xỉ nhau trên màn. Tại hai mép màn, cực tiểu nhiễu xạ đầu trùng một cực đại giao thoa hai khe. Tìm d. Màn không bao trùm toàn bộ hệ vân. (b) Tìm tốc độ v. (c) Tìm độ mở lớn nhất a. (d) Ở một thời điểm, các đốm ngoài cùng $m=\pm9$ biến mất. Thời điểm đó là bao nhiêu? (e) Ở $t=1{,}50\,\mathrm s$, cường độ các đốm $m=\pm1$ bằng bao nhiêu theo đốm trung tâm? (f) Các đốm này nằm ở những góc nào?

![Hình P36.65: Hai màng trượt ngược chiều làm thay đổi độ mở và tạo hệ vân trên màn cung tròn.](img/young-36/hinh-p36-65.png)
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Đặt T bằng thời gian từ đóng đến đóng lại, $T=3{,}00\,\mathrm s$. Độ mở chồng lấp là w(t), khác với a là bề rộng lớn nhất. Hai màng có tốc độ tương đối 2v.

**Hướng đi:**

- Dùng các bậc giao thoa từ $-9$ đến 9 để xác định bậc khuyết tại mép $30^\circ$.
- Dùng $w\sin\theta=\lambda$ cho cực tiểu đầu của khe hiệu dụng.
- Độ mở tăng theo $w=2vt$ trước lúc mở hết, rồi giảm đối xứng về không.
- Tại hướng cực đại giao thoa, tỉ số cường độ chỉ còn bao bình phương sinc.

(a) Có 19 bậc chưa khuyết trong phần màn đang xét, gồm $m=-9,\ldots,9$. Cực đại kế tiếp ở hai mép có bậc $\pm10$. Vì nửa góc màn là $30^\circ$:

$$
\begin{aligned}
d\sin30^\circ&=10\lambda,\\
d&=20\lambda\\
&=10{,}64\,\mu\mathrm m.
\end{aligned}
$$

(b) Ở một giây, cực tiểu nhiễu xạ đầu nằm tại mép nên:

$$
\begin{aligned}
w(1\,\mathrm s)\sin30^\circ&=\lambda,\\
w(1\,\mathrm s)&=2\lambda.
\end{aligned}
$$

Trong nửa đầu chu kỳ mở, $w=2vt$. Do đó:

$$
v=0{,}532\,\mu\mathrm{m/s}.
$$

(c) Mở lớn nhất tại $T/2=1{,}50\,\mathrm s$. Khi đó:

$$
a = vT = 3\lambda = 1{,}596\,\mu\mathrm m.
$$

(d) Các đốm bậc chín nằm ở hướng có $\sin\theta_9=9\lambda/d$. Muốn chúng trùng cực tiểu đầu, độ mở phải thỏa:

$$
\begin{aligned}
w\frac{9\lambda}{d}&=\lambda,\\
w&=\frac d9=\frac{20\lambda}{9}.
\end{aligned}
$$

Trên nhánh đang mở, $2vt=w$ cho lần đầu:

$$
t_1=\frac{10}{9}\,\mathrm s\approx1{,}11\,\mathrm s.
$$

Độ mở ấy còn xuất hiện trên nhánh đang đóng, tại $t_2=T-t_1\approx1{,}89\,\mathrm s$. Nếu hỏi thời điểm đầu sau trạng thái ở một giây, đáp số là $1{,}11\,\mathrm s$.

(e) Ở lúc mở lớn nhất, $a/d=3/20$. Tại bậc một:

$$
\begin{aligned}
\frac{I_1}{I_0}&=\left[\frac{\sin(3\pi/20)}{3\pi/20}\right]^2\\
&=0{,}928135\\
&\approx0{,}928.
\end{aligned}
$$

(f):

$$
\theta_{\pm1} = \pm\arcsin(\lambda/d) = \pm2{,}87^\circ.
$$

Các kết quả dùng số bậc và điều kiện vân khuyết ở mép. Trong cùng mô hình bao nhiễu xạ, các đốm ở một giây không thật sự có cường độ xấp xỉ bằng nhau. Chẳng hạn, bậc chín chỉ có khoảng $0{,}0119$ lần cường độ tâm. Độ cách góc cũng chỉ gần đều, vì điều kiện đều theo sin góc chứ không theo chính góc.
:::

::: exercise 36.66
Xét N khe cách tâm đều nhau một khoảng d, phát kết hợp đồng pha với bước sóng $\lambda$. Điểm P ở xa, góc quan sát $\theta$ được đo với đường trung trực của hệ khe. Ký hiệu R là khoảng từ P tới khe xa nhất và giả thiết R lớn hơn d rất nhiều.

(a) Chứng minh tổng trường có dạng sau, theo quy ước pha của đề. Đặt $\delta=kR-\omega t$, $\phi=2\pi d\sin\theta/\lambda$ và $\psi_N=\delta+(N-1)\phi$:

$$
\begin{aligned}
E_1&=E_0\cos\delta,\\
E_2&=E_0\cos(\delta+\phi),\\
E_3&=E_0\cos(\delta+2\phi),\\
E_N&=E_0\cos\psi_N.
\end{aligned}
$$

Các số hạng ở giữa tiếp tục theo cùng quy luật. Trường tổng được khai triển là:

$$
E_P=E_1+E_2+\cdots+E_N.
$$

(b) Với $e^{iz}=\cos z+i\sin z$ và $i^2=-1$, chứng minh trường trên là phần thực của tổng phức gồm các số hạng $E_0e^{i(\delta+n\phi)}$, với n từ 0 đến $N-1$.

(c) Dùng $e^Ae^B=e^{A+B}$ và $(e^A)^n=e^{nA}$ để cộng tổng thành cấp số nhân, rồi biến đổi thành dạng lượng giác. Chứng minh biên độ có hệ số $\sin(N\phi/2)/\sin(\phi/2)$ và pha là $\delta+(N-1)\phi/2$.

(d) Suy cường độ theo góc, với $I_0$ là cường độ cực đại của một khe riêng. (e) Kiểm tra $N=2$ bằng $\sin2A=2\sin A\cos A$. Vì sao biểu thức khác (35.10) một thừa số 4?
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Các khe có cùng biên độ tại P và pha tăng đều giữa hai khe kề nhau trong gần đúng miền xa. Phân biệt hệ số có dấu của trường với độ lớn biên độ.

**Hướng đi:**

- Dùng nguyên lý chồng chất để cộng các điện trường, không cộng cường độ trước.
- Viết tường minh tổng hữu hạn rồi dùng cấp số nhân với $q=e^{i\phi}$.
- Tách nhân tử pha để đổi hiệu các hàm mũ thành sin.
- Cường độ tỉ lệ bình phương độ lớn biên độ, còn chuẩn $I_0$ phải được giữ nhất quán.

(a) Tại P, các khe có cùng biên độ $E_0$, còn độ lệch pha giữa các khe kề nhau là $\phi$. Vì vậy các số hạng lần lượt có pha $\delta$, $\delta+\phi$, $\delta+2\phi$ và tiếp tục tới $\delta+(N-1)\phi$. Cộng các số hạng ấy cho biểu thức trong đề.

Dấu của $\phi$ gắn với chiều đánh số khe và góc có dấu. Đảo chiều đánh số làm đổi pha chung và dấu pha tương đối nhưng không đổi cường độ cuối cùng. Điều kiện miền xa cần áp dụng cho toàn dãy khe để các tia tới P gần song song.

(b) Lấy phần thực của từng số hạng mũ phức cho cos của đúng pha tương ứng. Bởi phép lấy phần thực có tính tuyến tính, phần thực của tổng phức là tổng các điện trường.

Đặt $q=e^{i\phi}$. Tổng hữu hạn được khai triển trước khi viết gọn:

$$
S_N = 1+q+\cdots+q^{N-1} = \sum_{n = 0}^{N-1}q^n.
$$

Biểu thức trường phức là $E_0e^{i\delta}S_N$.

(c) Với ba khe, ta có $S_3=1+q+q^2$. Lấy $S_3-qS_3$ làm các số hạng ở giữa triệt tiêu, chỉ còn $1-q^3$. Cùng phép trừ đó với N số hạng cho:

$$
\begin{aligned}
(1-q)S_N&=1-q^N,\\
S_N&=\frac{q^N-1}{q-1}.
\end{aligned}
$$

Phép chia dùng khi $q\ne1$. Với $q=1$, tổng trực tiếp bằng N.

Dùng đồng nhất thức $e^{ix}-e^{-ix}=2i\sin x$, ta viết:

$$
\begin{aligned}
A_N&=\frac{\sin(N\phi/2)}{\sin(\phi/2)},\\
\eta&=(N-1)\phi/2,\\
S_N&=A_Ne^{i\eta}.
\end{aligned}
$$

Đặt $A_N=\sin(N\phi/2)/\sin(\phi/2)$ và $\psi=\delta+(N-1)\phi/2$. Khi đó:

$$
E_P(t)=E_0A_N\cos\psi.
$$

Độ lớn biên độ là $E_0|A_N|$. Nếu $A_N$ âm, dấu âm tương ứng thêm pha $\pi$, không phải một độ lớn biên độ âm.

(d) Vì $I_0$ là cường độ một khe:

$$
\begin{aligned}
I&=I_0A_N^2,\\
A_N&=\frac{\sin(N\phi/2)}{\sin(\phi/2)}.
\end{aligned}
$$

Tại bội của $2\pi$, lấy giới hạn hoặc cộng trực tiếp các trường đồng pha để được $I=N^2I_0$.

(e) Với $N=2$:

$$
\begin{aligned}
A_2&=\frac{\sin\phi}{\sin(\phi/2)}\\
&=2\cos(\phi/2),\\
I&=4I_0\cos^2(\phi/2).
\end{aligned}
$$

Ở đây $I_0$ thuộc một khe riêng. Trong (35.10), $I_0$ là cường độ cực đại của cả hai nguồn, lớn gấp bốn lần cường độ một nguồn. Khác biệt chỉ nằm ở chuẩn ký hiệu, không phải một dự đoán vật lý khác.
:::

::: exercise 36.67
Dùng biểu thức cường độ của N khe ở Bài 36.66 để kiểm tra các phát biểu sau. (a) Cường độ cực đại bằng $N^2I_0$. (b) Cực đại chính ở tâm mở từ $\phi=-2\pi/N$ tới $\phi=2\pi/N$, nên bề rộng “tỉ lệ nghịch với $1/N$”. (c) Có cực tiểu khi $\phi$ là bội nguyên của $2\pi/N$, trừ bội của $2\pi$ tạo cực đại chính. (d) Có $N-1$ cực tiểu giữa hai cực đại chính. (e) Ở chính giữa hai cực đại chính, cường độ không vượt $I_0$, tức không quá $1/N^2$ cường độ đỉnh chính.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** $I_0$ là cường độ một khe. Dùng $I=I_0A_N^2$ với $A_N=\sin(N\phi/2)/\sin(\phi/2)$.

**Hướng đi:**

- Lấy giới hạn tại pha của cực đại chính để xử lý dạng $0/0$.
- Các cực tiểu có tử số bằng không nhưng mẫu khác không.
- Đếm các giá trị pha trong một khoảng $2\pi$ và kiểm riêng trung điểm ở pha $\pi$.

(a) Tại $\phi=2k\pi$, mọi khe đồng pha. Tổng biên độ gấp N lần một khe nên $I_{\max}=N^2I_0$.

(b) Hai cực tiểu sát tâm là $\phi=\pm2\pi/N$, nên:

$$
\Delta\phi=\frac{4\pi}{N}.
$$

Bề rộng tỉ lệ thuận với $1/N$, tức tỉ lệ nghịch với N. Cụm “tỉ lệ nghịch với $1/N$” trong phát biểu cần được sửa theo hệ thức vừa tính.

(c) Tử số bằng không khi:

$$
\phi=\frac{2\pi q}{N}, q\in\mathbb Z.
$$

Nếu q không là bội của N, mẫu khác không và I bằng không. Nếu q là bội của N thì cả tử và mẫu cùng bằng không, nhưng giới hạn thuộc cực đại chính ở câu (a).

(d) Giữa pha 0 và $2\pi$, các giá trị q tạo cực tiểu là $1,2,\ldots,N-1$, đúng $N-1$ giá trị. Các khoảng giữa những cực đại chính khác có cùng cách đếm.

(e) Trung điểm của hai cực đại chính liên tiếp có pha là một số lẻ lần $\pi$. Khi đó mẫu số bình phương bằng một, còn tử số bình phương không vượt một:

$$
\begin{aligned}
I_{\rm giữa}&\le I_0,\\
\frac{I_{\rm giữa}}{I_{\max}}&\le\frac1{N^2}.
\end{aligned}
$$

Cụ thể, với N chẵn, cường độ trung điểm bằng không. Với N lẻ, nó bằng $I_0$. Cả hai đều thỏa cận đã yêu cầu.
:::

::: exercise 36.68
Có thể tính cường độ nhiễu xạ Fraunhofer một khe mà không dùng giản đồ pha. Gọi $y'$ là tọa độ trong khe rộng a, từ $-a/2$ tới $a/2$, với gốc ở tâm. Chia khe thành các dải vi phân rộng $dy'$.

(a) Biên độ tổng tại O ở xa là $E_0$. Giải thích vì sao biên độ từ một dải là $E_0dy'/a$, nên ở khoảng x trường của dải là $dE=E_0(dy'/a)\sin(kx-\omega t)$.

(b) Giải thích biểu thức trường của mỗi dải khi tới P, với D là khoảng từ tâm khe tới P và $k=2\pi/\lambda$:

$$
\begin{aligned}
dE&=E_0\frac{dy'}a\sin\psi,\\
\psi&=k(D-y'\sin\theta)-\omega t.
\end{aligned}
$$

(c) Tích phân mọi dải để chứng minh trường có dạng $E=E_0\sin(kD-\omega t)\sin\alpha/\alpha$, trong đó $\alpha=ka\sin\theta/2=\pi a\sin\theta/\lambda$. Kiểm tra tại $\theta=0$. (d) Từ đó suy biểu thức cường độ (36.7), với $I_0$ là cường độ tại O.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Giả thiết mặt sóng tới phẳng, chiếu đều trên khe và P thuộc miền Fraunhofer. Các dải có cùng đóng góp biên độ trên một đơn vị bề rộng.

**Hướng đi:**

- Chia thành N dải bằng nhau trước để thấy mỗi dải có biên độ $E_0/N$, rồi chuyển sang giới hạn vi phân.
- Giữ hiệu đường đi tuyến tính $-y'\sin\theta$ của miền xa để xác định pha.
- Dùng đối xứng để tích phân phần lẻ bằng không và phần chẵn cho hàm sinc.

(a) Tại O, các dải phát sóng tới cùng pha. Nếu chia khe thành N phần bằng nhau, mỗi phần phải đóng góp $E_0/N$ để tổng bằng $E_0$. Một dải rộng $dy'$ chiếm phần $dy'/a$ của khe, nên biên độ là $E_0dy'/a$.

(b) Khoảng truyền từ dải ở tọa độ $y'$ tới P, trong gần đúng miền xa, là $D-y'\sin\theta$. Thay khoảng này vào pha sóng hình sin cho đúng biểu thức trong đề. Sự thay đổi nhỏ của biên độ theo khoảng truyền được bỏ qua, nhưng phần chênh pha được giữ.

(c) Đặt $u=y'/a$, $\delta=kD-\omega t$ và $\alpha=ka\sin\theta/2$. Khi đó:

$$
J=\int_{-1/2}^{1/2}\sin(\delta-2\alpha u)\,du.
$$

Trường tổng là $E=E_0J$. Khai triển sin của hiệu trong J. Phần chứa $\sin(2\alpha u)$ là hàm lẻ nên tích phân trên miền đối xứng bằng không. Phần còn lại cho:

$$
\begin{aligned}
E&=E_0\sin\delta\,C,\\
C&=\int_{-1/2}^{1/2}\cos(2\alpha u)\,du\\
&=\frac{\sin\alpha}{\alpha}.
\end{aligned}
$$

Vì vậy:

$$
E=E_0\sin(kD-\omega t)\frac{\sin\alpha}{\alpha}.
$$

Tại $\theta=0$, đối số $\alpha$ tiến về không và tỉ số sinc tiến tới một. Ta thu lại sóng có biên độ $E_0$ như yêu cầu.

(d) Cường độ là trung bình theo thời gian của bình phương trường. Hệ số hình sin theo thời gian như nhau tại O và P, nên:

$$
\begin{aligned}
I&=I_0\left(\frac{\sin\alpha}{\alpha}\right)^2,\\
\alpha&=\frac{\pi a}{\lambda}\sin\theta.
\end{aligned}
$$

Đây là biểu thức (36.7). Cách tích phân và cách giản đồ pha cùng cộng những đóng góp trường của toàn bộ khe, nên cho cùng kết quả.
:::
