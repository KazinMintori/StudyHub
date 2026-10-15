## Bài tập tổng hợp chương 27: Bài 27.61–27.80

### Bài tập

::: exercise 27.61 •• CALC
Điểm $a$ nằm trên trục $+y$ tại $y=+0{,}200\,\mathrm{m}$, còn điểm $b$ nằm trên trục $+x$ tại $x=+0{,}200\,\mathrm{m}$. Một dây có dạng cung tròn bán kính $0{,}200\,\mathrm{m}$, tâm ở gốc tọa độ, nối từ $a$ đến $b$ và mang dòng điện $I=5{,}00\,\mathrm{A}$ theo chiều từ $a$ đến $b$.

(a) Nếu dây nằm trong từ trường đều $\vec B=0{,}800\,\mathrm{T}$ theo chiều $+z$, hãy tìm độ lớn và hướng lực tổng hợp của từ trường lên cung dây. (b) Tìm độ lớn và hướng lực tổng hợp nếu từ trường $\vec B=0{,}800\,\mathrm{T}$ theo chiều $+x$.
:::

::: solution
**Tóm tắt đề bài:** $R=0{,}200\,\mathrm{m}$, $I=5{,}00\,\mathrm{A}$. Cung đi từ $\vec r_a=(0,R,0)$ đến $\vec r_b=(R,0,0)$.

**Hướng đi:**
- Trong từ trường đều, $d\vec F=I\,d\vec\ell\times\vec B$. Tích phân theo cung chỉ còn phụ thuộc độ dời hai đầu dây: $\vec F=I(\vec r_b-\vec r_a)\times\vec B$.
- Tính tích có hướng với từng hướng từ trường, sau đó đổi vectơ thành độ lớn và chiều.

**Lời giải.** Độ dời từ $a$ đến $b$ là $\Delta\vec r=(R,-R,0)$.

(a) Với $\vec B=(0,0,B)$:

$$
\begin{aligned}
\vec F &= I(R,-R,0)\times(0,0,B) \\
&= (-IRB,-IRB,0) \\
&= (-0{,}800\,\hat i-0{,}800\,\hat j)\,\mathrm{N}.
\end{aligned}
$$

Độ lớn lực là

$$
F = \sqrt{2}(0{,}800\,\mathrm{N}) = 1{,}13\,\mathrm{N}.
$$

Lực hướng theo đường phân giác xuống dưới và sang trái, tức chiều $-x,-y$.

(b) Với $\vec B=(B,0,0)$:

$$
\begin{aligned}
\vec F &= I(R,-R,0)\times(B,0,0) \\
&= IRB\,\hat k \\
&= 0{,}800\,\hat k\,\mathrm{N}.
\end{aligned}
$$

Lực có độ lớn $0{,}800\,\mathrm{N}$ và hướng $+z$.
:::

::: exercise 27.62 ••
Quạt trần dùng động cơ điện có nam châm vĩnh cửu đứng yên (stator) gắn vào moay-ơ trung tâm. Từ trường điển hình có độ lớn $1{,}0\,\mathrm{T}$ và tạo mômen lực lên các cuộn dây mang dòng điện (rotor) gắn với cánh quạt. Hãy xét một chiếc quạt trần ở nhà hoặc nơi làm việc.

(a) Ước lượng đường kính moay-ơ tại mép trong của các cánh. (b) Nếu 12 rotor bố trí quanh moay-ơ và tổng đường kính của chúng bằng một phần ba chu vi moay-ơ, hãy tìm đường kính một rotor. (c) Quạt thông dụng tạo mômen lực $1{,}4\,\mathrm{N\,m}$. Nếu 12 rotor chia đều mômen này trong từ trường stator song song với trục mỗi rotor, hãy ước lượng mômen từ của từng rotor. (d) Các rotor mắc song song, nên mỗi rotor nhận một phần mười hai dòng điện của quạt, thường là $0{,}75\,\mathrm{A}$. Hãy ước lượng số vòng dây của mỗi rotor.
:::

::: solution
**Tóm tắt đề bài:** Đây là bài ước lượng. Chọn đường kính moay-ơ đại diện $D=0{,}15\,\mathrm{m}$, từ trường $B=1{,}0\,\mathrm{T}$, mômen tổng $1{,}4\,\mathrm{N\,m}$ và dòng tổng $0{,}75\,\mathrm{A}$.

**Hướng đi:**
- Nêu một kích thước hợp lý cho moay-ơ. Các đáp số phụ thuộc lựa chọn này.
- Dùng chu vi $\pi D$ để suy ra kích thước rotor, rồi chia đều mômen và dòng điện.
- Với mỗi rotor, dùng $\tau=\mu B$ và $\mu=NIA$.

**Lời giải.**

(a) Một moay-ơ có đường kính khoảng $15\,\mathrm{cm}$ là ước lượng hợp lý cho quạt trần cỡ gia dụng.

(b) Mười hai đường kính rotor cộng lại bằng $\pi D/3$, do đó đường kính mỗi rotor là

$$
\begin{aligned}
d &= \frac{\pi D}{36} \\
&= 1{,}31\times10^{-2}\,\mathrm{m} \\
&= 1{,}31\,\mathrm{cm}.
\end{aligned}
$$

(c) Mỗi rotor tạo mômen $1{,}4/12=0{,}117\,\mathrm{N\,m}$. Để ước lượng, lấy mỗi cuộn ở vị trí có mômen cực đại, tức pháp tuyến của cuộn vuông góc với từ trường. Khi đó $\tau=\mu B$ và $\mu=0{,}117\,\mathrm{A\,m^2}$.

Trục cơ học của rôto không tự xác định pháp tuyến từng cuộn dây. Nếu “trục rôto” được hiểu là trục từ của một vòng phẳng, tức hướng $\vec\mu$, thì $\vec\mu$ song song $\vec B$ sẽ cho mômen bằng không. Vì vậy, kết quả ước lượng này cần giả thiết góc nêu trên. Nếu $\sin\phi<1$, mômen từ cần lớn hơn theo hệ số $1/\sin\phi$.

(d) Dòng qua mỗi rotor là $I=0{,}75/12=0{,}0625\,\mathrm{A}$. Xấp xỉ rotor là một cuộn tròn đường kính $d$. Diện tích mỗi vòng là

$$
A=\pi(d/2)^2=1{,}35\times10^{-4}\,\mathrm{m^2}.
$$

Khi đó

$$
\begin{aligned}
N &= \frac{\mu}{IA} \\
&\approx 1{,}38\times10^4\text{ vòng}.
\end{aligned}
$$

Con số này là ước lượng bậc độ lớn. Kích thước moay-ơ và hình học thực của rotor quyết định kết quả chính xác.
:::

::: exercise 27.63 ••
Gần mặt đất, từ trường Trái Đất thường có độ lớn $0{,}50\,\mathrm{G}$, với $1\,\mathrm{G}=10^{-4}\,\mathrm{T}$. Ở các vĩ độ ôn đới Bắc bán cầu, trường nghiêng xuống dưới khoảng $45^\circ$. Hãy xét tính khả thi của thiết bị nâng thanh dẫn như hình P27.63.

(a) Ước lượng dòng điện cần để nâng một thanh đồng đường kính $d=5{,}0\,\mathrm{mm}$ bằng thành phần ngang của từ trường Trái Đất. Khối lượng riêng của đồng là $8900\,\mathrm{kg/m^3}$. (b) Thanh đồng đường kính này nóng chảy nếu dòng vượt dòng nung chảy $900\,\mathrm{A}$. Thiết bị có khả thi không? (c) Ước lượng độ lớn nhỏ nhất của từ trường cần để nâng thanh đồng. (d) Giả sử dùng nam châm vĩnh cửu phổ biến tạo trường ngang $1{,}0\,\mathrm{T}$ và thanh dài $10\,\mathrm{cm}$. Với dòng $10\,\mathrm{A}$, thiết bị có thể nâng thêm trọng lượng bao nhiêu ngoài chính thanh đồng?

![Hình P27.63: Thiết bị nâng thanh dẫn bằng từ trường.](img/young-27/hinh-p27-63.png)
:::

::: solution
**Tóm tắt đề bài:** $B_{\oplus}=0{,}50\,\mathrm{G}$ nghiêng $45^\circ$, $d=5{,}0\,\mathrm{mm}$, $\rho=8900\,\mathrm{kg/m^3}$. Diện tích tiết diện thanh là

$$
A = \pi(d/2)^2 = 1{,}96\times10^{-5}\,\mathrm{m^2}.
$$

**Hướng đi:**
- Dùng thành phần ngang $B_h=B_{\oplus}\cos45^\circ$ để tạo lực thẳng đứng.
- Khối lượng thanh trên mỗi mét là $\rho A$. So sánh $ILB_h$ với $\rho ALg$ để tìm dòng điện, trong đó chiều dài $L$ triệt tiêu.
- Với nam châm $1{,}0\,\mathrm{T}$, trừ trọng lượng thanh khỏi lực từ để tìm tải nâng thêm.

**Lời giải.** Thành phần ngang của trường Trái Đất là $B_h=3{,}54\times10^{-5}\,\mathrm{T}$. Định hướng dòng điện sao cho tích có hướng $I\vec L\times\vec B_h$ hướng lên.

(a) Điều kiện cân bằng là $ILB_h=\rho ALg$, vì vậy

$$
I = \frac{\rho Ag}{B_h} = 4{,}82\times10^4\,\mathrm{A}.
$$

(b) Dòng cần thiết lớn hơn nhiều so với $900\,\mathrm{A}$, do đó thiết bị không khả thi với từ trường Trái Đất.

(c) Ở ngưỡng $I=900\,\mathrm{A}$, từ trường ngang nhỏ nhất là

$$
\begin{aligned}
B_{\min} &= \frac{\rho Ag}{900\,\mathrm{A}} \\
&= 1{,}90\times10^{-3}\,\mathrm{T}.
\end{aligned}
$$

(d) Với thanh dài $0{,}100\,\mathrm{m}$, lực từ là $ILB=1{,}00\,\mathrm{N}$. Khối lượng thanh là $\rho AL=0{,}0175\,\mathrm{kg}$, nên trọng lượng thanh khoảng $0{,}171\,\mathrm{N}$. Phần lực còn lại đỡ tải ngoài bằng $0{,}829\,\mathrm{N}$, tương ứng khối lượng

$$
\begin{aligned}
m_{\mathrm{tải}} &= \frac{1{,}00-0{,}171}{9{,}80} \\
&= 0{,}0846\,\mathrm{kg}.
\end{aligned}
$$
:::

::: exercise 27.64 •• CALC
Khung dây chữ nhật trong hình P27.64 quay quanh trục $y$ và mang dòng điện $15{,}0\,\mathrm{A}$ theo chiều chỉ trên hình. (a) Nếu khung nằm trong từ trường đều $0{,}48\,\mathrm{T}$ theo chiều $+x$, hãy tìm độ lớn và hướng mômen lực cần tác dụng để giữ khung ở vị trí đó. (b) Làm lại câu (a) khi từ trường hướng $-z$. (c) Với mỗi từ trường trên, mômen lực cần thiết thay đổi thế nào nếu trục quay đi qua tâm khung và song song trục $y$?

![Hình P27.64: Khung dây chữ nhật quay quanh trục y.](img/young-27/hinh-p27-64.png)
:::

::: solution
**Tóm tắt đề bài:** $I=15{,}0\,\mathrm{A}$, kích thước khung $8{,}00\,\mathrm{cm}\times6{,}00\,\mathrm{cm}$, góc nghiêng trong hình là $30{,}0^\circ$, $B=0{,}48\,\mathrm{T}$.

**Hướng đi:**
- Mômen từ là $\vec\mu=IA\hat n$, với $\hat n$ vuông góc mặt khung theo quy tắc bàn tay phải.
- Tính $\vec\tau_{B}=\vec\mu\times\vec B$. Mômen ngoài để giữ cân bằng quay có hướng ngược với $\vec\tau_B$.
- Lực tổng trên khung kín trong từ trường đều bằng không, nên chuyển trục song song từ cạnh sang tâm không làm đổi mômen.

**Lời giải.** Diện tích là

$$
A = (0{,}0800)(0{,}0600) = 4{,}80\times10^{-3}\,\mathrm{m^2}.
$$

Do đó $\mu=0{,}0720\,\mathrm{A\,m^2}$. Theo chiều dòng điện trong hình, thành phần pháp tuyến là

$$
\vec\mu = \mu\sin30^\circ\,\hat i -\mu\cos30^\circ\,\hat k.
$$

Vì vậy từ trường tạo mômen $0{,}0299\,\mathrm{N\,m}$ theo $-y$ khi $\vec B$ hướng $+x$, và $0{,}0173\,\mathrm{N\,m}$ theo $+y$ khi $\vec B$ hướng $-z$.

(a) Mômen lực ngoài cần thiết là $0{,}0299\,\mathrm{N\,m}$ theo $+y$.

(b) Mômen lực ngoài cần thiết là $0{,}0173\,\mathrm{N\,m}$ theo $-y$.

(c) Cả hai đáp số không đổi. Trong từ trường đều, tổng lực bằng không, vì vậy độ dời trục quay song song không tạo thêm mômen do lực tổng.
:::

::: exercise 27.65 •• CP
Khung dây trong hình P27.65 có khối lượng dây $0{,}15\,\mathrm{g/cm}$, được bản lề không ma sát dọc cạnh $ab$. Dòng điện $8{,}2\,\mathrm{A}$ chạy theo chiều chỉ trên hình. Tìm độ lớn và hướng của từ trường song song trục $y$ làm khung dao động lên đến khi mặt phẳng khung tạo góc $30{,}0^\circ$ với mặt phẳng $yz$.

![Hình P27.65: Khung dây có bản lề dọc cạnh ab.](img/young-27/hinh-p27-65.png)
:::

::: solution
**Tóm tắt đề bài:** Khung có hai cạnh $8{,}00\,\mathrm{cm}$ và $6{,}00\,\mathrm{cm}$, $I=8{,}2\,\mathrm{A}$, mật độ dài $0{,}15\,\mathrm{g/cm}$.

**Hướng đi:**
- Tính khối lượng toàn bộ dây từ chu vi khung.
- Lấy mômen quanh bản lề. Trọng lực đặt tại trọng tâm, cách bản lề một nửa cạnh ngang.
- Cân bằng mômen từ với mômen trọng lực ở góc $30^\circ$.

**Lời giải.** Chu vi là $0{,}28\,\mathrm{m}$, nên khối lượng dây là

$$
\begin{aligned}
m &= (0{,}015\,\mathrm{kg/m})(0{,}28\,\mathrm{m}) \\
&= 4{,}20\times10^{-3}\,\mathrm{kg}.
\end{aligned}
$$

Diện tích khung là

$$
A = (0{,}08)(0{,}06) = 4{,}8\times10^{-3}\,\mathrm{m^2}.
$$

Do đó $\mu=IA=0{,}0394\,\mathrm{A\,m^2}$.

Tại góc $\theta=30^\circ$, cánh tay đòn của trọng lực bằng $(0{,}08/2)\sin\theta$. Thành phần mômen từ quanh bản lề có độ lớn $IAB\cos\theta$. Hai mômen có chiều ngược nhau. Điều kiện cân bằng là:

$$
\begin{aligned}
\tau_g &= mg\frac{0{,}08}{2}\sin\theta, \\
\tau_B &= IAB\cos\theta, \\
IAB\cos\theta &= mg\frac{0{,}08}{2}\sin\theta.
\end{aligned}
$$

Chia hai vế cho $IA\cos\theta$ cho:

$$
\begin{aligned}
B &= \frac{mg(0{,}08/2)\tan30^\circ}{IA} \\
&= 2{,}41\times10^{-2}\,\mathrm{T}.
\end{aligned}
$$

Từ trường phải hướng theo $+y$ để mômen từ ngược chiều mômen trọng lực quanh bản lề.
:::

::: exercise 27.66 •• CALC
Thanh dẫn thẳng đồng chất dài $L$ mang dòng điện $I$ từ điểm $a$ đến điểm $b$ như hình P27.66. Thanh nằm trong từ trường đều hướng vào trang giấy. Xét mômen lực quanh trục vuông góc với thanh tại $a$ do lực từ tác dụng lên thanh. (a) Một đoạn vi phân dài $dx$ cách $a$ một khoảng $x$. Hãy tính mômen vi phân $d\tau$ quanh $a$ do lực từ lên đoạn này. (b) Dùng $\tau=\int_a^b d\tau$ để tính mômen lực tổng. (c) Chứng minh kết quả giống như khi coi toàn bộ lực từ đặt tại trung điểm thanh.

![Hình P27.66: Lực từ vi phân trên thanh dẫn.](img/young-27/hinh-p27-66.png)
:::

::: solution
**Tóm tắt đề bài:** $L$, $I$, $B$ không đổi. Lấy chiều dương của mômen theo quy tắc bàn tay phải từ hướng của dòng điện và từ trường.

**Hướng đi:**
- Trên đoạn $dx$, lực từ có độ lớn $dF=IB\,dx$ vì thanh vuông góc với trường.
- Mômen vi phân bằng cánh tay đòn $x$ nhân lực vi phân.
- Tích phân từ đầu bản lề tới cuối thanh.

**Lời giải.** Với $d\vec\ell=dx\,\hat i$ và $\vec B=-B\hat k$, lực vi phân là

$$
d\vec F=I\,d\vec\ell\times\vec B=IB\,dx\,\hat j.
$$

Mômen vi phân quanh $a$ là

$$
d\vec\tau = x\hat i\times d\vec F = IBx\,dx\,\hat k.
$$

(b) Tích phân:

$$
\vec\tau = IB\hat k\int_0^L x\,dx = \frac{1}{2}IBL^2\hat k.
$$

(c) Tổng lực từ có độ lớn $F=IBL$. Đặt lực tại trung điểm thì cánh tay đòn là $L/2$, do đó $\tau=F(L/2)=IBL^2/2$, trùng với kết quả tích phân.
:::

::: exercise 27.67 ••
Vòng dây trong hình P27.67 là tam giác vuông, mang dòng điện $I=5{,}00\,\mathrm{A}$ theo chiều chỉ trên hình. Từ trường đều $B=3{,}00\,\mathrm{T}$ cùng hướng với dòng điện trên cạnh $PQ$. (a) Tìm lực từ trên từng cạnh của tam giác và hướng của mỗi lực khác không. (b) Tìm lực tổng lên vòng dây. (c) Vòng quay quanh trục dọc cạnh $PR$. Dùng kết quả bài 27.66 để tính mômen lực trên từng cạnh. (d) Tính độ lớn mômen tổng bằng cả tổng mômen từng cạnh và phương trình (27.28). Hai kết quả có khớp nhau không? (e) Mômen tổng làm điểm $Q$ quay vào hay ra khỏi mặt phẳng hình?

![Hình P27.67: Vòng dây hình tam giác vuông trong từ trường.](img/young-27/hinh-p27-67.png)
:::

::: solution
**Tóm tắt đề bài:** Theo hình, $PQ=0{,}600\,\mathrm{m}$ song song từ trường, $PR=0{,}800\,\mathrm{m}$, $I=5{,}00\,\mathrm{A}$, $B=3{,}00\,\mathrm{T}$.

**Hướng đi:**
- Tính lực từng cạnh bằng $I\vec L\times\vec B$. Cạnh song song với $\vec B$ không chịu lực.
- Lực hai cạnh còn lại bằng nhau và ngược nhau, nên lực tổng bằng không.
- Lấy mômen từng lực quanh $PR$ rồi kiểm tra bằng $\tau=IAB$.

**Lời giải.** (a) Dòng trên $PQ$ hướng $+y$, cùng chiều từ trường, nên $\vec F_{PQ}=0$. Trên $QR$, thành phần dòng theo $+x$ tạo lực $12{,}0\,\mathrm{N}$ hướng ra khỏi trang giấy. Trên $RP$, dòng hướng $-x$, nên lực $12{,}0\,\mathrm{N}$ hướng vào trang giấy.

(b) Hai lực triệt tiêu nhau: $\vec F_{\mathrm{net}}=0$.

(c) Lực trên $PQ$ bằng không. Lực phân bố trên $PR$ có tổng lực $12{,}0\,\mathrm{N}$ nhưng mômen chiếu lên trục $PR$ bằng không. Cạnh $QR$ đóng góp $+3{,}60\,\mathrm{N\,m}$ dọc trục bản lề. Tổng mômen quanh trục là $+3{,}60\,\mathrm{N\,m}$.

(d) Diện tích tam giác $A=(0{,}800)(0{,}600)/2=0{,}240\,\mathrm{m^2}$. Dòng chạy theo chiều kim đồng hồ khi nhìn từ $+z$, nên $\vec\mu=-IA\hat k$. Với $\vec B=3\hat j\,\mathrm{T}$, mômen từ có độ lớn $IAB=3{,}60\,\mathrm{N\,m}$ dọc trục $+x$. Kết quả khớp với tổng mômen quanh bản lề.

(e) Mômen theo $+x$ làm điểm $Q$ quay ra khỏi mặt phẳng hình.
:::

::: exercise 27.68 ••
Làm lại bài 27.67 nhưng cho từ trường $\vec B=3{,}00\,\mathrm{T}$ hướng vào trang giấy trong hình P27.67.
:::

::: solution
**Tóm tắt đề bài:** Giữ hình học và dòng điện của bài 27.67, đổi từ trường thành $-3{,}00\hat k\,\mathrm{T}$.

**Hướng đi:**
- Dùng lại các vector cạnh, thay trường hướng $+y$ bằng trường hướng $-z$, rồi tính lại từng tích có hướng.
- Trong trường đều, lực tổng trên vòng kín vẫn bằng không.
- Chiếu mômen từng cạnh lên trục $PR$. Vì mômen từ của vòng song song trường mới, mômen tổng bằng không.

**Lời giải.** Dùng $\vec F=I\vec L\times\vec B$ với $\vec B=-3{,}00\hat k\,\mathrm{T}$: Cạnh $PQ$ chịu lực $9{,}00\,\mathrm{N}$ theo $-x$, $QR$ chịu lực $15{,}0\,\mathrm{N}$ theo hướng $(0{,}600\hat i+0{,}800\hat j)$, còn $RP$ chịu lực $12{,}0\,\mathrm{N}$ theo $-y$. Tổng ba lực bằng không. Mômen vectơ quanh $P$ lần lượt là $+2{,}70\hat k$, $+2{,}10\hat k$ và $-4{,}80\hat k\,\mathrm{N\,m}$, nên mômen tổng quanh trục $PR$ bằng không.

Với trục quay dọc $PR$ (trục $x$), các lực trong mặt phẳng $xy$ không tạo thành phần mômen quanh trục này. Điều đó cũng theo $\vec\mu$ song song $\vec B$, nên mômen tổng bằng không. (e) Vòng không có xu hướng quay đưa đỉnh $Q$ vào hoặc ra khỏi trang giấy.
:::

::: exercise 27.69 •• CALC
### Cuộn dây loa
Mục 27.7 chỉ ra rằng lực tổng lên vòng dây có dòng điện bằng không nếu từ trường đều. Lực lên cuộn dây loa khác không vì từ trường tại cuộn không đều. Cuộn loa có 50 vòng dây, đường kính $1{,}56\,\mathrm{cm}$ và dòng điện $0{,}950\,\mathrm{A}$. Giả sử tại mỗi điểm trên cuộn, từ trường có độ lớn không đổi $0{,}220\,\mathrm{T}$ và hướng lệch ra ngoài một góc $60{,}0^\circ$ so với pháp tuyến của mặt phẳng cuộn như hình P27.69. Trục cuộn theo phương $y$. Dòng điện chạy theo chiều chỉ trên hình, ngược chiều kim đồng hồ khi nhìn từ điểm phía trên cuộn trên trục $y$. Tính độ lớn và hướng lực từ tổng lên cuộn dây.

![Hình P27.69: Cuộn dây loa trong từ trường không đều.](img/young-27/hinh-p27-69.png)
:::

::: solution
**Tóm tắt đề bài:** $N=50$, $I=0{,}950\,\mathrm{A}$, $D=0{,}0156\,\mathrm{m}$, $B=0{,}220\,\mathrm{T}$.

**Hướng đi:**
- Thành phần pháp tuyến của trường tạo các lực hướng tâm, khử nhau quanh vòng.
- Thành phần hướng ra ngoài trong mặt phẳng cuộn có độ lớn $B\sin60^\circ$ và lực vi phân của nó cùng trục $y$ quanh toàn cuộn.
- Nhân lực trên một vòng với số vòng.

**Lời giải.** Với dòng ngược chiều kim đồng hồ khi nhìn từ $+y$, chiều dòng điện tiếp tuyến và thành phần trường hướng ra ngoài tạo lực dọc trục. Theo quy tắc bàn tay phải, lực hướng $-y$ trong hình. Độ lớn là

$$
\begin{aligned}
F &= NI(B\sin60^\circ)(\pi D) \\
&= (50)(0{,}950) \times(0{,}220\sin60^\circ) \times\pi(0{,}0156) \\
&= 0{,}444\,\mathrm{N}.
\end{aligned}
$$
:::

::: exercise 27.70 •• CP
Thanh đồng chất có khối lượng $0{,}0120\,\mathrm{kg}$, dài $30{,}0\,\mathrm{cm}$, quay không ma sát quanh trục vuông góc với thanh tại điểm $a$ như hình P27.70. Trọng lực hướng $-y$. Thanh nằm trong từ trường đều hướng vào trang giấy, $B=0{,}150\,\mathrm{T}$. (a) Tìm dòng điện cần chạy trong thanh để thanh cân bằng quay khi nó tạo góc $\theta=30{,}0^\circ$ phía trên phương ngang. Dùng kết quả bài 27.66. (b) Dòng điện phải chạy từ $a$ đến $b$ hay từ $b$ đến $a$?

![Hình P27.70: Thanh dẫn quay quanh trục tại điểm a.](img/young-27/hinh-p27-70.png)
:::

::: solution
**Tóm tắt đề bài:** $m=0{,}0120\,\mathrm{kg}$, $L=0{,}300\,\mathrm{m}$, $B=0{,}150\,\mathrm{T}$, $\theta=30{,}0^\circ$.

**Hướng đi:**
- Trọng lực tác dụng tại trung điểm, mômen trọng lực có độ lớn $mg(L/2)\cos\theta$.
- Bài 27.66 cho mômen từ $IBL^2/2$ quanh đầu thanh.
- Cân bằng mômen để tìm dòng, rồi xác định chiều dòng sao cho mômen từ ngược chiều mômen trọng lực.

**Lời giải.** Cân bằng độ lớn mômen cho

$$
\begin{aligned}
mg\frac{L}{2}\cos\theta &= IB\frac{L^2}{2} \\
I &= \frac{mg\cos\theta}{BL} \\
&= 2{,}26\,\mathrm{A}.
\end{aligned}
$$

Trọng lực làm thanh quay theo chiều kim đồng hồ. Với $\vec B$ hướng vào trang, dòng từ $a$ đến $b$ tạo mômen ngược chiều kim đồng hồ, nên dòng điện phải chạy từ $a$ đến $b$.
:::

### Bài tập tiếp theo

::: exercise 27.71 •• CALC
Trong mục 27.7 đã chỉ ra rằng lực tổng trên vòng dây có dòng điện bằng không trong từ trường đều. Nếu $\vec B$ không đều thì sao? Hình P27.71 là một vòng dây vuông nằm trong mặt phẳng $xy$, có các đỉnh $(0,0)$, $(0,L)$, $(L,0)$ và $(L,L)$, mang dòng điện không đổi $I$ theo chiều kim đồng hồ. Từ trường không có thành phần $x$, nhưng có các thành phần $y$ và $z$:

$$
\vec B = \frac{B_0z}{L}\hat j +\frac{B_0y}{L}\hat k.
$$

trong đó $B_0$ là hằng số dương. (a) Phác họa đường sức từ trong mặt phẳng $yz$. (b) Dùng cách tích phân phương trình (27.20), tìm độ lớn và hướng lực từ trên từng cạnh. (c) Tìm độ lớn và hướng lực từ tổng lên vòng dây.

![Hình P27.71: Vòng dây vuông nằm trong mặt phẳng xy.](img/young-27/hinh-p27-71.png)
:::

::: solution
**Tóm tắt đề bài:** Vòng vuông cạnh $L$ mang dòng chiều kim đồng hồ. Trường có $B_y=B_0z/L$ và $B_z=B_0y/L$.

**Hướng đi:**
- Dùng $d\vec F=I\,d\vec\ell\times\vec B$ trên từng cạnh, giữ thành phần trường thay đổi dọc cạnh.
- Cộng các lực cạnh đối diện để thấy thành phần triệt tiêu hoặc cộng lại.
- Trong mặt phẳng $yz$, đường sức của trường thỏa $dy/B_y=dz/B_z$.

**Lời giải.** (a) Ta có $dy/dz=B_y/B_z=z/y$, nên $y\,dy=z\,dz$. Tích phân cho $y^2-z^2=C$. Các đường sức là họ hyperbol, cùng với các trường hợp đường tiệm cận.

![Đồ thị lời giải 27.71: Đường sức trong mặt phẳng yz](img/young-27/hinh-giai27-71-duong-suc.svg)

Mũi tên cho hướng từ trường. Các đường giữ y² − z² không đổi, còn tại gốc trường bằng không.


(b) Theo chiều kim đồng hồ nhìn từ $+z$, dòng trên cạnh $y=0$ hướng $-x$, cạnh $x=L$ hướng $-y$, cạnh $y=L$ hướng $+x$, cạnh $x=0$ hướng $+y$.

Vòng nằm trên mặt phẳng $z=0$, nên $B_y=0$ tại mọi điểm trên dây. Trường tại dây chỉ còn thành phần $B_z=B_0y/L$.

Trên cạnh dưới $y=0$, trường bằng không, nên lực bằng không. Trên cạnh trên $y=L$, dòng theo $+x$ và trường bằng $B_0\hat k$:

$$
\begin{aligned}
\vec F_{\mathrm{top}} &= IB_0\int_0^L dx \times(\hat i\times\hat k) \\
&= -IB_0L\hat j.
\end{aligned}
$$

Trên cạnh trái $x=0$, dòng theo $+y$:

$$
\begin{aligned}
\vec F_{\mathrm{left}} &= \frac{IB_0}{L}\int_0^L y\,dy \times(\hat j\times\hat k) \\
&= \frac12IB_0L\hat i.
\end{aligned}
$$

Trên cạnh phải $x=L$, tích phân theo chiều dòng đi từ $y=L$ xuống $y=0$:

$$
\begin{aligned}
\vec F_{\mathrm{right}} &= \frac{IB_0}{L}\int_L^0 y\,dy \times(\hat j\times\hat k) \\
&= -\frac12IB_0L\hat i.
\end{aligned}
$$

Độ lớn lực trên các cạnh dưới, trên, trái, phải lần lượt là $0$, $IB_0L$, $IB_0L/2$, $IB_0L/2$. Hai lực theo $x$ triệt tiêu.

(c) Cộng ba lực khác không:

$$
\vec F_{\mathrm{net}}=-IB_0L\hat j.
$$

Độ lớn là $IB_0L$, hướng $-y$.
:::

::: exercise 27.72 •• CP
Đầu dưới của thanh mảnh đồng chất trong hình P27.72 gắn với sàn bằng bản lề không ma sát tại $P$. Thanh có khối lượng $0{,}0840\,\mathrm{kg}$, dài $18{,}0\,\mathrm{cm}$, đặt trong từ trường đều $B=0{,}120\,\mathrm{T}$ hướng vào trang giấy. Một sợi dây ngang nối đầu trên của thanh với tường để giữ thanh ở góc $\theta=53{,}0^\circ$ trên phương ngang. Dòng điện $I=12{,}0\,\mathrm{A}$ chạy về phía $P$. Tính lực căng dây. Dùng kết quả bài 27.66 để tính mômen do lực từ.

![Hình P27.72: Thanh dẫn có bản lề và dây treo ngang.](img/young-27/hinh-p27-72.png)
:::

::: solution
**Tóm tắt đề bài:** $m=0{,}0840\,\mathrm{kg}$, $L=0{,}180\,\mathrm{m}$, $\theta=53{,}0^\circ$, $I=12{,}0\,\mathrm{A}$, $B=0{,}120\,\mathrm{T}$.

**Hướng đi:**
- Lực từ dọc thanh có mômen $IBL^2/2$ quanh bản lề.
- Với dòng hướng về bản lề và $\vec B$ vào trang, mômen từ cùng chiều mômen trọng lực.
- Lực căng dây ngang tạo mômen ngược chiều hai mômen kia.

**Lời giải.** Mômen từ là

$$
\tau_B = \frac12 IBL^2 = 2{,}33\times10^{-2}\,\mathrm{N\,m}.
$$

Mômen trọng lực có độ lớn

$$
\begin{aligned}
\tau_g &= mg\frac L2\cos\theta \\
&= 4{,}45\times10^{-2}\,\mathrm{N\,m}.
\end{aligned}
$$

Lực căng tác dụng ngang ở đầu thanh, nên cánh tay đòn là $L\sin\theta$. Cân bằng mômen:

$$
\begin{aligned}
\tau_g &= mg\frac L2\cos\theta \\
&= 0{,}0446\,\mathrm{N\cdot m}, \\
\tau_B &= \frac12IBL^2 \\
&= 0{,}0233\,\mathrm{N\cdot m}, \\
T &= \frac{\tau_g+\tau_B}{L\sin\theta} \\
&= 0{,}472\,\mathrm N.
\end{aligned}
$$
:::

::: exercise 27.73 ••• CP
Thiết bị nâng từ dùng một trụ hình trụ bán kính $R$, bề rộng $W$, quấn dây dẫn $N$ vòng theo một đường kính như hình P27.73. Từ trường ngoài đều $\vec B$ hướng xuống, còn dòng $I$ chạy theo chiều được chỉ ra. Một vật khối lượng $M$ treo vào trụ bằng cáp gắn ở vành trụ, trên trục cuộn dây. Độ cao của vật so với vị trí thấp nhất có thể là $h$.

(a) Tìm dòng điện nhỏ nhất để vật có thể được giữ lơ lửng với $h>0$. (b) Tìm độ cao $h=h_{\mathrm{top}}$ khi điểm gắn cáp quay nửa vòng tới đỉnh trụ. Đặt tham số không thứ nguyên $s=2NIWB/(Mg)$ và biểu diễn các kết quả tiếp theo theo $s$ cùng các đại lượng đã cho. (c) Tìm mômen lực tổng lên trụ khi $0\le h\le R$. (d) Tìm mômen lực tổng khi $R\le h\le h_{\mathrm{top}}$. (e) Xác định thế năng $U(h)$ bằng không tại $h=0$ khi $0\le h\le R$. (f) Tìm $U(h)$ khi $R\le h\le h_{\mathrm{top}}$. (g) Nếu $s>1$, vật đứng yên ở độ cao nào? (h) Với những giá trị $s$ nào, trụ quay quá nửa vòng khi thả vật từ nghỉ tại $h=h_{\mathrm{top}}$? Gợi ý: Điều này tương đương $U(h_{\mathrm{top}})>0$.

![Hình P27.73: Trụ cuốn dây dùng để nâng vật.](img/young-27/hinh-p27-73.png)
:::

::: solution
**Tóm tắt đề bài:** Mỗi vòng dây có diện tích $2RW$, nên mômen từ của cuộn là $\mu=2NIWR$. Đặt $s=\mu B/(MgR)=2NIWB/(Mg)$. Chọn chiều quay nâng vật làm chiều mômen dương.

**Hướng đi:**
- Trong chặng đầu, điểm treo đi từ đáy tới mép ngang của vành trụ. Hình học đường tròn cho $h=R(1-\cos\theta)$.
- Ở mép ngang, cáp bắt đầu trượt quanh vành trụ. Sau đó vật tăng độ cao $R$ cho mỗi radian trụ quay.
- Tính riêng mômen từ và mômen trọng lực ở từng chặng. Thế năng tìm từ công của từng lực, không suy rộng một biểu thức qua điểm chuyển tiếp.

**Lời giải.** Vì $\mu=2NIWR$ và $s=\mu B/(MgR)$, độ lớn mômen từ cực đại là $\mu B=sMgR$.

(a) Ở chặng đầu, cả mômen trọng lực lẫn mômen từ đều tỉ lệ với $R\sin\theta$. Mômen từ thắng mômen trọng lực khi $s>1$. Dòng điện ngưỡng là

$$
I_{\min}=\frac{Mg}{2NWB}.
$$

(b) Khi điểm treo đi từ đáy tới mép ngang, vật tăng độ cao $R$. Sau đó cáp trượt thêm một phần tư chu vi quanh vành trụ, kéo vật lên thêm $R\pi/2$. Vì vậy

$$
h_{\mathrm{top}}=R\left(1+\frac{\pi}{2}\right).
$$

(c) Với $0\le h\le R$, từ $h=R(1-\cos\theta)$ ta được cánh tay đòn

$$
R\sin\theta=\sqrt{h(2R-h)}.
$$

Trong chặng này, mômen từ có độ lớn $\mu B\sin\theta$ theo chiều nâng. Mômen trọng lực có độ lớn $MgR\sin\theta$ theo chiều ngược lại. Vì vậy

$$
\tau_{\mathrm{net}}=Mg(s-1)\sqrt{h(2R-h)}.
$$

(d) Với $R\le h\le h_{\mathrm{top}}$, đặt $\theta=h/R-1$ là góc quay thêm sau khi cáp tới mép ngang. Cáp kéo vật thẳng đứng nên trọng lực có cánh tay đòn cố định $R$, tạo mômen $-MgR$. Khi cuộn quay thêm góc $\theta$, thành phần mômen từ dọc trục giảm theo $\cos\theta$ và bằng $sMgR\cos\theta$. Do đó

$$
\begin{aligned}
\theta &= \frac hR-1, \\
\tau_{\mathrm{net}} &= MgR(s\cos\theta-1).
\end{aligned}
$$

(e) Thế năng trọng trường tăng $Mgh$. Công của mômen từ trong chặng đầu làm thế năng giảm $\mu B(1-\cos\theta)=sMgh$. Chọn $U(0)=0$:

$$
U(h)=(1-s)Mgh.
$$

(f) Tại $h=R$, $U(R)=(1-s)MgR$. Trên chặng sau, trọng lực làm thế năng tăng $MgR\theta$, còn mômen từ làm thế năng giảm $\mu B\sin\theta$. Do đó

$$
\begin{aligned}
\theta &= \frac hR-1, \\
U(h) &= Mgh -MgRs -MgRs\sin\theta, \\
R &\le h\le h_{\mathrm{top}}.
\end{aligned}
$$

Hai nhánh thế năng trùng nhau tại $h=R$, nên thế năng liên tục ở điểm chuyển tiếp.

(g) Cân bằng ở chặng sau thỏa $\tau_{\mathrm{net}}=0$, vì thế $\cos\theta=1/s$. Với $s>1$, nghiệm là $\theta=\arccos(1/s)$. Đạo hàm mômen theo góc tại nghiệm âm, nên cân bằng bền. Độ cao cân bằng:

$$
h = R\left[1+\arccos\left(\frac{1}{s}\right)\right].
$$

(h) Thay $h_{\mathrm{top}}=R(1+\pi/2)$ vào thế năng:

$$
U(h_{\mathrm{top}}) = MgR\left(1+\frac{\pi}{2}\right) -2sMgR.
$$

Vật quay quá nửa vòng khi $U(h_{\mathrm{top}})>0$, tức là $s<\frac12(1+\pi/2)$.
:::

::: exercise 27.74 ••• CP CALC
Một hạt điện tích $q$, khối lượng $m$, được thả từ nghỉ tại gốc $t=0$ trong vùng có từ trường không đổi $\vec B$ nằm ngang. Điều gì xảy ra? Dùng hệ tọa độ Descartes với trục $y$ hướng xuống và trục $z$ cùng hướng từ trường. Tại thời điểm $t\ge0$, hạt có vận tốc $\vec v=v_x\hat i+v_y\hat j$. Tổng lực $\vec F=F_x\hat i+F_y\hat j$ là hợp lực trọng trường và lực từ.

(a) Dùng định luật II Newton, viết phương trình cho $a_x,a_y$. (b) Lấy đạo hàm theo thời gian phương trình thứ hai, rồi thay biểu thức $a_x=dv_x/dt$ để tìm phương trình cho $d^2v_y/dt^2$ theo $v_y$. (c) Kết quả cho thấy $v_y$ là dao động điều hòa đơn. Dùng điều kiện đầu tìm $v_y(t)$ theo $\omega=qB/m$. Biết $(dv_y/dt)_0=g$. (d) Thay $v_y(t)$ vào phương trình cho $dv_x/dt$ rồi tích phân với điều kiện đầu để tìm $v_x(t)$. (e) Tích phân hai vận tốc để tìm $x(t),y(t)$. (f) Nếu $m=1{,}00\,\mathrm{mg}$, $q=19{,}6\,\mu\mathrm{C}$, $B=10{,}0\,\mathrm{T}$, hạt rơi xuống tối đa bao xa trước khi chuyển động lên?
:::

::: solution
**Tóm tắt đề bài:** Trục $y$ hướng xuống, $\vec B=B\hat k$, hạt bắt đầu từ nghỉ. Đặt $\omega=qB/m$ theo dấu của điện tích.

**Hướng đi:**
- Viết $q\vec v\times\vec B$ theo thành phần để giữ đúng dấu của lực từ.
- Khử $v_x$ để thu được phương trình dao động điều hòa cho $v_y$.
- Tích phân vận tốc, rồi tìm cực đại của $y(t)$.

**Lời giải.** (a) Với $\vec v=(v_x,v_y,0)$ và $\vec B=(0,0,B)$, ta có $\vec v\times\vec B=(v_yB,-v_xB,0)$. Do đó

$$
a_x=\omega v_y,\qquad a_y=g-\omega v_x.
$$

(b) Lấy đạo hàm phương trình thứ hai rồi dùng phương trình của $dv_x/dt$:

$$
\frac{d^2v_y}{dt^2} = -\omega\frac{dv_x}{dt} = -\omega^2v_y.
$$

(c) Điều kiện $v_y(0)=0$ và $v_y'(0)=g$ cho

$$
v_y(t)=\frac{g}{\omega}\sin(\omega t).
$$

(d) Từ $dv_x/dt=\omega v_y=g\sin(\omega t)$ và $v_x(0)=0$:

$$
v_x(t)=\frac{g}{\omega}[1-\cos(\omega t)].
$$

(e) Tích phân với $x(0)=y(0)=0$:

$$
\begin{aligned}
x(t) &= \frac{g}{\omega}t-\frac{g}{\omega^2}\sin(\omega t), \\
y(t) &= \frac{g}{\omega^2}[1-\cos(\omega t)].
\end{aligned}
$$

(f) Điểm thấp nhất xảy ra tại $\omega t=\pi$, do đó $y_{\max}=2g/\omega^2$. Thay các thông số đã cho, ta có

$$
\omega=\frac{qB}{m}=196\,\mathrm{rad/s}.
$$

Vì vậy:

$$
\begin{aligned}
y_{\max} &= 5{,}10\times10^{-4}\,\mathrm{m} \\
&= 0{,}510\,\mathrm{mm}.
\end{aligned}
$$
:::

::: exercise 27.75 ••
Từ trường ngoài tạo mômen lực $\vec\tau=D(4\hat i-3\hat j)$ lên vòng dây tròn diện tích $A$ nằm trong mặt phẳng $xy$. Nhìn dọc trục $z$ theo chiều về gốc tọa độ, dòng điện $I$ chạy theo chiều kim đồng hồ. Với hướng đặt vòng này, thế năng từ $U=-\vec\mu\cdot\vec B$ âm. Độ lớn từ trường là $B_0=13D/(IA)$. (a) Xác định vectơ mômen từ của vòng. (b) Tìm các thành phần $B_x,B_y,B_z$.
:::

::: solution
**Tóm tắt đề bài:** Dòng nhìn từ $+z$ chạy theo chiều kim đồng hồ, $\vec\mu=-IA\hat k$. Mômen lực đã biết, còn độ lớn $B_0$ và dấu của thế năng ràng buộc các thành phần trường.

**Hướng đi:**
- Dùng chiều dòng điện để xác định dấu của $\vec\mu$.
- Từ $\vec\tau=\vec\mu\times\vec B$, suy ra hai thành phần nằm trong mặt phẳng $xy$.
- Điều kiện $U<0$ chọn dấu của $B_z$, còn $|\vec B|=B_0$ kiểm tra độ lớn.

**Lời giải.**

$$
\vec\mu=-IA\hat k.
$$

Tích có hướng cho các thành phần:

$$
\begin{aligned}
\tau_x &= IAB_y=4D, \\
\tau_y &= -IAB_x=-3D.
\end{aligned}
$$

Đặt $C=D/(IA)$, suy ra $B_x=3C$, $B_y=4C$. Dùng độ lớn trường đã cho:

$$
B_z^2 = (13C)^2-(3C)^2 -(4C)^2 = 144C^2.
$$

Vì $U=IAB_z<0$, phải chọn $B_z=-12C$.

$$
\vec B = \frac{D}{IA}(3\hat i+4\hat j-12\hat k).
$$

:::

::: exercise 27.76 •• DATA
Bạn dùng một loại khối phổ để đo tỉ số điện tích trên khối lượng của ion nguyên tử. Nguyên tử được ion hóa bằng chùm electron để tạo ion dương, rồi gia tốc qua hiệu điện thế $V$. Tốc độ ban đầu có thể bỏ qua. Các ion đi vào vùng từ trường đều vuông góc vận tốc, $B=0{,}250\,\mathrm{T}$, và chuyển động theo nửa đường tròn bán kính $R$. Bảng số liệu:

| $V$ (kV) | 10,0 | 12,0 | 14,0 | 16,0 | 18,0 |
|---|---:|---:|---:|---:|---:|
| $R$ (cm) | 19,9 | 21,8 | 23,6 | 25,2 | 26,8 |

(a) Nên biểu diễn dữ liệu thế nào để các điểm gần nằm trên đường thẳng? Giải thích. (b) Vẽ đồ thị ấy và dùng hệ số góc đường hồi quy tốt nhất để tính $q/m$. (c) Với $V=20{,}0\,\mathrm{kV}$, tìm tốc độ ion khi vào vùng từ trường. (d) Nếu ion có $R=21{,}2\,\mathrm{cm}$ ở $12{,}0\,\mathrm{kV}$ mang điện tích đơn, hãy tìm $R$ ở cùng điện áp cho ion mang điện tích gấp đôi.
:::

::: solution
**Tóm tắt đề bài:** $B=0{,}250\,\mathrm{T}$. Dữ liệu $V,R$ như bảng.

**Hướng đi:**
- Ghép $qV=mv^2/2$ với $qvB=mv^2/R$ để thu được quan hệ tuyến tính giữa $R^2$ và $V$.
- Hệ số góc của đồ thị $R^2(V)$ bằng $2/(B^2(q/m))$.
- Tỉ số $q/m$ tăng gấp đôi thì bán kính ở cùng điện áp giảm theo $1/\sqrt{2}$.

**Lời giải.** Từ bảo toàn năng lượng, $v=\sqrt{2qV/m}$. Bán kính quỹ đạo là

$$
R^2=\frac{2m}{qB^2}V.
$$

(a) Vẽ $R^2$ theo $V$ để được đường thẳng.

![Đồ thị lời giải 27.76: Bình phương bán kính theo điện thế gia tốc](img/young-27/hinh-giai27-76-hoi-quy.svg)

Đường khớp dùng toàn bộ năm cặp số liệu. Hệ số góc được tính với điện thế theo volt và bán kính theo mét.


(b) Hồi quy bình phương nhỏ nhất cho các số liệu bảng cho hệ số góc $4{,}02\times10^{-6}\,\mathrm{m^2/V}$. Do đó

$$
\begin{aligned}
\frac qm &= \frac{2}{B^2\,\mathrm{slope}} \\
&= 7{,}96\times10^6\,\mathrm{C/kg}.
\end{aligned}
$$

(c) Tốc độ ion là

$$
v = \sqrt{2(q/m)V} = 5{,}64\times10^5\,\mathrm{m/s}.
$$

(d) Vì $R\propto1/\sqrt q$ ở cùng $V,B,m$, nên $R_2=0{,}212/\sqrt2=0{,}150\,\mathrm{m}$.
:::

::: exercise 27.77 •• DATA
Bạn là nhà nghiên cứu đo khối lượng muon bằng một phiên bản hiện đại của thiết bị $e/m$ Thomson. Từ trường giữa hai bản tích điện là $0{,}340\,\mathrm{T}$. Bạn đo điện trường để hạt không bị lệch theo điện thế gia tốc $V$. Điện thế đủ lớn để có thể bỏ qua vận tốc ban đầu.

Hình P27.77 là đồ thị $E^2$ theo $V$. (a) Giải thích vì sao các điểm gần nằm trên đường thẳng. (b) Dùng đồ thị để tính khối lượng muon. (c) Nếu hai bản cách nhau $6{,}00\,\mathrm{mm}$, cần hiệu điện thế bao nhiêu để điện trường bằng $2{,}00\times10^5\,\mathrm{V/m}$? Kích thước bản lớn hơn nhiều khoảng cách. (d) Khi $V=400\,\mathrm{V}$, tìm tốc độ muon đi vào vùng giữa hai bản.

![Hình P27.77: Đồ thị bình phương điện trường theo điện thế gia tốc.](img/young-27/hinh-p27-77.png)
:::

::: solution
**Tóm tắt đề bài:** $B=0{,}340\,\mathrm{T}$. Điểm cuối đọc trên đồ thị có hoành độ $400\,\mathrm{V}$ và tung độ $8{,}0\times10^{10}\,\mathrm{V^2/m^2}$.

**Hướng đi:**
- Bộ chọn vận tốc thỏa $qE=qvB$, còn năng lượng gia tốc cho $qV=mv^2/2$.
- Khử $v$ để liên hệ $E^2$ với $V$. Hệ số góc cho $m$.
- Dùng $V_{\mathrm{bản}}=Ed$ ở câu (c), rồi năng lượng gia tốc ở câu (d).

**Lời giải.** Từ hai điều kiện:

$$
E^2=\frac{2qB^2}{m}V.
$$

(a) Vì $E^2$ tỉ lệ thuận với $V$, đồ thị là đường thẳng qua gốc.

(b) Hệ số góc xấp xỉ $2{,}0\times10^8\,\mathrm{V^2/(m^2\,V)}$. Với $q=e$, khối lượng muon là

$$
\begin{aligned}
m &= \frac{2eB^2}{\mathrm{slope}} \\
&= 1{,}85\times10^{-28}\,\mathrm{kg}.
\end{aligned}
$$

(c) Hiệu điện thế giữa hai bản là

$$
\begin{aligned}
V_{\mathrm{bản}} &= Ed \\
&= (2{,}00\times10^5) \times(6{,}00\times10^{-3}) \\
&= 1{,}20\times10^3\,\mathrm{V}.
\end{aligned}
$$

(d) Tốc độ là

$$
\begin{aligned}
v &= \sqrt{\frac{2eV}{m}} \\
&= \frac{\sqrt{8{,}0\times10^{10}}}{0{,}340} \\
&= 8{,}32\times10^5\,\mathrm{m/s}.
\end{aligned}
$$
:::

::: exercise 27.78 •• DATA
Bạn là kỹ thuật viên kiểm tra máy gia tốc hạt kiểu cyclotron. Một hạt alpha chuyển động theo quỹ đạo tròn trong từ trường $\vec B$ vuông góc với quỹ đạo. Bạn đo số vòng mỗi giây $f$ theo độ lớn $B$. Hình P27.78 cho kết quả đo và đường thẳng khớp tốt nhất.

(a) Dùng đồ thị để tính tỉ số điện tích trên khối lượng của hạt alpha có điện tích $+2e$. Từ dữ liệu, khối lượng hạt alpha là bao nhiêu? (b) Khi $B=0{,}300\,\mathrm{T}$, tần số cyclotron của proton và electron bằng bao nhiêu? So sánh với tần số của hạt alpha. (c) Với $B=0{,}300\,\mathrm{T}$ và bán kính quỹ đạo $12{,}0\,\mathrm{cm}$, tìm tốc độ và động năng của hạt alpha.

![Hình P27.78: Tần số cyclotron theo độ lớn từ trường.](img/young-27/hinh-p27-78.png)
:::

::: solution
**Tóm tắt đề bài:** Đọc đường thẳng khớp tốt nhất trên đồ thị, hệ số góc xấp xỉ $7{,}67\times10^6\,\mathrm{Hz/T}$. Hạt alpha có điện tích $2e$.

**Hướng đi:**
- Tần số cyclotron là $f=qB/(2\pi m)$, nên hệ số góc $f(B)$ bằng $(q/m)/(2\pi)$.
- Dùng $q=2e$ để suy ra khối lượng hạt alpha.
- Bán kính quỹ đạo cho $v=qBR/m$, sau đó tính $K=mv^2/2$.

**Lời giải.** (a) Hệ số góc đọc từ đồ thị là $7{,}67\times10^6\,\mathrm{Hz/T}$. Do đó

$$
\begin{aligned}
\frac qm &= 2\pi(7{,}67\times10^6) \\
&= 4{,}82\times10^7\,\mathrm{C/kg}.
\end{aligned}
$$

Khối lượng hạt alpha là

$$
m_\alpha = \frac{2e}{q/m} = 6{,}65\times10^{-27}\,\mathrm{kg}.
$$

(b) Tần số cyclotron của proton và electron lần lượt là

$$
\begin{aligned}
f_p &= \frac{eB}{2\pi m_p} \\
&= 4{,}57\times10^6\,\mathrm{Hz}, \\
f_e &= \frac{eB}{2\pi m_e} \\
&= 8{,}41\times10^9\,\mathrm{Hz}.
\end{aligned}
$$

Tần số alpha là

$$
\begin{aligned}
f_\alpha &= \frac{(q/m)_\alpha B}{2\pi} \\
&= 2{,}30\times10^6\,\mathrm{Hz}.
\end{aligned}
$$

Vậy proton quay nhanh hơn alpha khoảng $1{,}99$ lần, còn electron nhanh hơn khoảng $3{,}66\times10^3$ lần.

(c) $v=(q/m)BR=1{,}73\times10^6\,\mathrm{m/s}$, nên $K=1{,}00\times10^{-14}\,\mathrm{J}$.
:::

::: exercise 27.79 ••• CALC
Tìm mômen từ $\vec M$ của một vỏ cầu bán kính $R$, mang điện tích tổng $Q$ phân bố đều và quay với vận tốc góc $\vec\Omega=\omega\hat k$. Dùng các bước sau. (a) Đặt gốc tọa độ ở tâm cầu, mô tả mỗi vĩ tuyến bằng góc $\theta$ đo từ trục $+z$. Mỗi vĩ tuyến tạo thành một vòng dòng điện, với $0\le\theta\le\pi$. Bán kính vòng theo $\theta$ là bao nhiêu? (b) Dòng vi phân trên vòng là $dI=\sigma v\,dW$, trong đó $\sigma$ là mật độ điện tích mặt, $v$ là tốc độ tiếp tuyến và $dW=R\,d\theta$ là bề rộng vi phân. Biểu diễn $dI$ theo $\sigma,R,\omega,\theta,d\theta$. (c) Mômen từ vi phân của vòng là $dM=A\,dI$, với $A$ là diện tích vòng. Biểu diễn $dM$ theo $R,\omega,\theta,d\theta$. (d) Tích phân trên cả cầu để tìm mômen từ dạng vectơ, dùng điện tích tổng $Q$ thay cho $\sigma$. (e) Nếu cầu đặt trong từ trường đều $\vec B=B(\sin\alpha\,\hat i+\cos\alpha\,\hat j)$, tìm mômen lực.
:::

::: solution
**Tóm tắt đề bài:** Vỏ cầu quay quanh trục $z$, mật độ điện tích mặt $\sigma=Q/(4\pi R^2)$.

**Hướng đi:**
- Vĩ tuyến ở góc $\theta$ có bán kính $R\sin\theta$ và tốc độ $v=\omega R\sin\theta$.
- Mỗi dải vĩ tuyến mang dòng $dI=\sigma vR\,d\theta$.
- Tính mômen của vòng dòng điện vi phân rồi tích phân theo $\theta$.

**Lời giải.** (a) Bán kính vĩ tuyến là $r=R\sin\theta$.

(b)

$$
dI=\sigma\omega R^2\sin\theta\,d\theta.
$$

(c) Diện tích vòng là $\pi R^2\sin^2\theta$, nên

$$
dM=\pi\sigma\omega R^4\sin^3\theta\,d\theta.
$$

(d) Dùng $\int_0^\pi\sin^3\theta\,d\theta=4/3$:

$$
M = \frac{4\pi}{3}\sigma\omega R^4 = \frac{Q\omega R^2}{3}.
$$

Vì $\vec\Omega=\omega\hat k$, ta có $\vec M=(QR^2/3)\vec\Omega$.

(e) Với $\vec B=B(\sin\alpha\hat i+\cos\alpha\hat j)$:

$$
\begin{aligned}
\vec\tau &= \vec M\times\vec B \\
&= \frac{Q\omega R^2B}{3} \times(\sin\alpha\hat j-\cos\alpha\hat i).
\end{aligned}
$$
:::

::: exercise 27.80 •••
Một electron từ gió Mặt Trời bay tới từ quyển Trái Đất tại vĩ độ $80{,}0^\circ$ Bắc, nơi từ trường có độ lớn $15{,}0\,\mu\mathrm{T}$ và hướng về tâm Trái Đất. Electron có tốc độ $400\,\mathrm{km/s}$ và chuyển động song song với xích đạo về phía trục Trái Đất. Lực từ làm electron đi theo quỹ đạo xoắn ốc.

(a) Bán kính đường xoắn là bao nhiêu? (b) Electron tiến tới bề mặt Trái Đất với tốc độ nào? (c) Nếu nhìn xuống Trái Đất từ không gian, electron chuyển động theo chiều kim đồng hồ hay ngược chiều kim đồng hồ? (d) Tần số chuyển động là bao nhiêu? (e) Electron đi vào tầng điện ly, nơi nó còn được gia tốc bởi điện trường $20\,\mathrm{mV/m}$ hướng về phía bắc song song mặt đất. Tốc độ mới sau khi nó bị lệch $100\,\mathrm{km}$ về phía nam là bao nhiêu? (f) Động năng tăng lên bao nhiêu lần do điện trường?
:::

::: solution
**Tóm tắt đề bài:** Electron có tốc độ đầu $v=4{,}00\times10^5\,\mathrm{m/s}$ tại vĩ độ $\lambda=80^\circ$. Từ trường $15{,}0\,\mathrm{\mu T}$ hướng về tâm Trái Đất. Vận tốc hướng về trục Trái Đất và song song mặt phẳng xích đạo, nên góc với từ trường là $80^\circ$.

**Hướng đi:**

- Chiếu vận tốc lên hướng từ trường và phương vuông góc để tính bán kính xoắn và tốc độ tiến về mặt đất. Không thay góc $80^\circ$ bằng góc vuông.
- Dùng dấu điện tích electron và hướng từ trường để xác định chiều quay. Chu kỳ không phụ thuộc tốc độ trong mô hình không tương đối tính.
- Tính công điện trường với dấu của điện tích và độ dời. Dùng bảo toàn năng lượng để tìm tốc độ cuối và tỉ số động năng.

**Lời giải.** Trong mô hình từ trường đều tại chỗ, các thành phần vận tốc là:

$$
\begin{aligned}
v_\parallel &= v\cos80^\circ \\
&= 6{,}95\times10^4\,\mathrm{m/s}, \\
v_\perp &= v\sin80^\circ \\
&= 3{,}94\times10^5\,\mathrm{m/s}.
\end{aligned}
$$

(a) Bán kính quỹ đạo xoắn dùng thành phần vuông góc:

$$
r = \frac{m_ev_\perp}{eB} \approx 0{,}150\,\mathrm m.
$$

(b) Electron tiến về bề mặt dọc từ trường với tốc độ $v_\parallel\approx69{,}5\,\mathrm{km/s}$. Tốc độ toàn phần vẫn là $400\,\mathrm{km/s}$ vì lực từ không sinh công. Hai đại lượng này khác nhau.

(c) Electron quay theo chiều kim đồng hồ khi nhìn từ không gian hướng về Trái Đất. Từ trường hướng ra xa người quan sát, vào trong mặt quan sát. Với vận tốc tức thời sang phải, lực lên điện tích âm hướng xuống, xác định chiều quay ấy.

(d) Tần số:

$$
f = \frac{eB}{2\pi m_e} \approx 4{,}19\times10^5\,\mathrm{Hz}.
$$

(e) Điện trường hướng bắc, còn độ dời $100\,\mathrm{km}$ hướng nam. Electron chịu lực điện hướng nam, nên công dương:

$$
\begin{aligned}
W_E &= eE\Delta s \\
&= 3{,}20\times10^{-16}\,\mathrm J, \\
v_f &= \sqrt{v_i^2+\frac{2W_E}{m_e}} \\
&\approx 2{,}65\times10^7\,\mathrm{m/s}.
\end{aligned}
$$

(f) Tỉ số động năng:

$$
\begin{aligned}
\frac{K_f}{K_i} &= 1+\frac{W_E}{\tfrac12m_ev_i^2} \\
&\approx 4{,}39\times10^3.
\end{aligned}
$$

:::
