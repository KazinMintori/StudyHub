## Bài tập về cơ học chất lưu, phần hai

Trong các bài có số, lấy $g=9{,}80\,\mathrm{m/s^2}$ nếu đề không quy định khác. Khi dùng phương trình Bernoulli, xét dòng ổn định, không nén được và bỏ qua tổn hao do nhớt theo mô hình của từng bài.

### 12.47 (•): Áp suất để tia nước đạt độ cao cho trước

Đường ống cấp nước của thành phố phải có áp suất dư bao nhiêu để tia nước từ một vòi chữa cháy nối với đường ống chính có thể vọt thẳng lên độ cao $15{,}0\,\mathrm m$? Giả sử tiết diện đường ống chính lớn hơn nhiều tiết diện vòi.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Tia nước cần lên cao $h=15{,}0\,\mathrm m$ tính từ miệng vòi. Đường ống chính có tiết diện rất lớn, nên tốc độ tại đó có thể bỏ qua so với tốc độ ở vòi.

**Hướng đi:**

- Chọn điểm đầu trong đường ống chính, gần cao độ miệng vòi, và điểm cuối tại đỉnh tia nước. Ở điểm cuối, tốc độ bằng không và áp suất bằng khí áp.
- Dùng Bernoulli vì chênh lệch áp suất của nước được chuyển thành độ cao của tia trong mô hình không tổn hao. Áp suất cần tìm là áp suất dư, nên phải lấy hiệu với khí áp.

**Lời giải:** Chọn cao độ đầu bằng không. Bỏ qua tốc độ trong đường ống chính, phương trình hai điểm cho

$$
p_{\mathrm{main}}=p_{\mathrm{atm}}+\rho gh.
$$

Vì vậy,

$$
\begin{aligned}
p_{\mathrm g}&=\rho gh\\
&=(1000)(9{,}80)(15{,}0)\,\mathrm{Pa}\\
&=1{,}47\times10^5\,\mathrm{Pa}.
\end{aligned}
$$

Đây là áp suất dư theo mô hình lý tưởng. Nếu kể tổn hao cơ năng trên đường ống và ở vòi, áp suất cấp cần lớn hơn giá trị này.

</details>

### 12.48 (•): Nước thoát qua một lỗ nhỏ ở thành bồn

Một lỗ tròn đường kính $6{,}00\,\mathrm{mm}$ nằm trên thành một bồn nước lớn, thấp hơn mặt nước $14{,}0\,\mathrm m$. Phía trên bồn hở ra không khí. Tìm (a) tốc độ nước thoát qua lỗ và (b) thể tích nước thoát ra mỗi giây.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Đường kính lỗ $d=6{,}00\,\mathrm{mm}$, độ sâu $h=14{,}0\,\mathrm m$. Bồn lớn nên tốc độ hạ mặt nước nhỏ so với tốc độ tia nước.

**Hướng đi:**

- Dùng định lý Torricelli vì mặt thoáng và tia nước đều chịu khí áp, tốc độ mặt thoáng có thể bỏ qua và chất lưu được coi là lý tưởng.
- Tính tiết diện lỗ bằng $A=\pi d^2/4$, rồi dùng $Q=Av$ để tìm thể tích đi qua mỗi giây. Phải đổi milimét sang mét trước khi bình phương.

**Lời giải:** (a) Tốc độ thoát là

$$
\begin{aligned}
v&=\sqrt{2gh}\\
&\approx16{,}6\,\mathrm{m/s}.
\end{aligned}
$$

(b) Đường kính theo SI là $d=6{,}00\times10^{-3}\,\mathrm m$. Tiết diện lỗ bằng

$$
A=\frac{\pi d^2}{4}\approx2{,}83\times10^{-5}\,\mathrm{m^2}.
$$

Giữ tốc độ chưa làm tròn trong phép nhân, ta có

$$
\begin{aligned}
Q&=Av\\
&\approx4{,}68\times10^{-4}\,\mathrm{m^3/s}\\
&\approx0{,}468\,\mathrm{L/s}.
\end{aligned}
$$

Như vậy, trong mỗi giây nước thoát ra khoảng $0{,}468\,\mathrm L$ tại mức nước đang xét.

</details>

### 12.49 (•): Ống nằm ngang có tiết diện tăng gấp đôi

Tại một điểm trong đường ống nằm ngang, nước có tốc độ $2{,}50\,\mathrm{m/s}$ và áp suất dư $1{,}80\times10^4\,\mathrm{Pa}$. Tìm áp suất dư tại điểm thứ hai, nơi tiết diện đường ống gấp đôi tiết diện tại điểm đầu.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Hai điểm cùng cao độ, $v_1=2{,}50\,\mathrm{m/s}$, $p_{1\mathrm g}=1{,}80\times10^4\,\mathrm{Pa}$ và $A_2=2A_1$.

**Hướng đi:**

- Dùng phương trình liên tục để tìm tốc độ ở tiết diện rộng hơn. Với nước không nén được, tích tiết diện với tốc độ không đổi.
- Dùng Bernoulli ở cùng cao độ. Có thể dùng áp suất dư ở cả hai điểm vì cùng một khí áp được trừ khỏi hai vế.

**Lời giải:** Phương trình liên tục cho

$$
v_2=\frac{A_1}{A_2}v_1=1{,}25\,\mathrm{m/s}.
$$

Phần áp suất tăng khi dòng chậm lại là

$$
\begin{aligned}
\Delta p&=\frac\rho2(v_1^2-v_2^2)\\
&=2343{,}75\,\mathrm{Pa}.
\end{aligned}
$$

Do đó,

$$
\begin{aligned}
p_{2\mathrm g}&=p_{1\mathrm g}+\Delta p\\
&=20343{,}75\,\mathrm{Pa}\\
&\approx2{,}03\times10^4\,\mathrm{Pa}.
\end{aligned}
$$

Tiết diện lớn hơn làm tốc độ giảm và áp suất tăng trong đường ống nằm ngang đang xét.

</details>

### 12.50 (••): Dòng nước đi xuống và chậm lại

Tại một điểm trong đường ống, tốc độ nước là $3{,}00\,\mathrm{m/s}$ và áp suất dư $5{,}00\times10^4\,\mathrm{Pa}$. Điểm thứ hai thấp hơn $11{,}0\,\mathrm m$ và có đường kính gấp đôi đường kính tại điểm đầu. Áp suất dư tại điểm thứ hai bằng bao nhiêu?

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** $v_1=3{,}00\,\mathrm{m/s}$, $p_{1\mathrm g}=5{,}00\times10^4\,\mathrm{Pa}$, $y_1-y_2=11{,}0\,\mathrm m$ và $d_2=2d_1$. Vì tiết diện tỉ lệ bình phương đường kính, $A_2=4A_1$.

**Hướng đi:**

- Dùng phương trình liên tục để tìm tốc độ ở tiết diện lớn hơn. Đường kính gấp đôi làm tiết diện gấp bốn lần.
- Tách hai ảnh hưởng trong Bernoulli: Đi xuống làm tăng áp suất, còn giảm tốc cũng làm tăng áp suất. Cần giữ cả hai phần và đúng dấu chênh cao.

**Lời giải:** Tốc độ ở điểm thứ hai là

$$
v_2=\frac{A_1}{A_2}v_1=0{,}750\,\mathrm{m/s}.
$$

Gọi $\Delta p_y$ là phần tăng do hạ cao độ và $\Delta p_v$ là phần tăng do giảm tốc. Khi đó,

$$
\begin{aligned}
\Delta p_y&=\rho g(y_1-y_2)\\
&=107800\,\mathrm{Pa}.
\end{aligned}
$$

$$
\begin{aligned}
\Delta p_v&=\frac\rho2(v_1^2-v_2^2)\\
&=4218{,}75\,\mathrm{Pa}.
\end{aligned}
$$

Áp suất dư cần tìm bằng

$$
\begin{aligned}
p_{2\mathrm g}&=p_{1\mathrm g}+\Delta p_y+\Delta p_v\\
&=162018{,}75\,\mathrm{Pa}\\
&\approx1{,}62\times10^5\,\mathrm{Pa}.
\end{aligned}
$$

Cả việc đi xuống lẫn giảm tốc đều làm áp suất cuối cao hơn áp suất đầu trong mô hình đang xét.

</details>

### 12.51 (••): Áp suất qua chỗ thắt của hệ thống tưới

Hệ thống tưới sân golf đưa nước qua một đường ống nằm ngang với lưu lượng $7200\,\mathrm{cm^3/s}$. Tại một điểm có bán kính trong $4{,}00\,\mathrm{cm}$, áp suất tuyệt đối là $2{,}40\times10^5\,\mathrm{Pa}$. Tại điểm thứ hai, đường ống thắt lại với bán kính $2{,}00\,\mathrm{cm}$. Tìm áp suất tuyệt đối của nước ở chỗ thắt.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** $Q=7200\,\mathrm{cm^3/s}$, $r_1=4{,}00\,\mathrm{cm}$, $r_2=2{,}00\,\mathrm{cm}$ và $p_1=2{,}40\times10^5\,\mathrm{Pa}$. Hai điểm cùng cao độ.

**Hướng đi:**

- Tìm từng tốc độ bằng $v=Q/(\pi r^2)$ vì đã biết lưu lượng và hai bán kính.
- Dùng Bernoulli ở cùng cao độ để suy ra độ giảm áp suất do tốc độ tăng. Đề hỏi áp suất tuyệt đối, nên giữ đúng loại áp suất từ đầu đến cuối.

**Lời giải:** Đổi lưu lượng theo SI:

$$
Q=7{,}200\times10^{-3}\,\mathrm{m^3/s}.
$$

Hai tốc độ tương ứng là

$$
\begin{aligned}
&v_1=\frac{Q}{\pi r_1^2}\approx1{,}432\,\mathrm{m/s},\\
&v_2=\frac{Q}{\pi r_2^2}\approx5{,}730\,\mathrm{m/s}.
\end{aligned}
$$

Độ giảm áp suất bằng

$$
\begin{aligned}
\Delta p&=\frac\rho2(v_2^2-v_1^2)\\
&\approx1{,}54\times10^4\,\mathrm{Pa}.
\end{aligned}
$$

Dùng các tốc độ chưa làm tròn, áp suất tại chỗ thắt là

$$
\begin{aligned}
p_2&=p_1-\Delta p\\
&\approx2{,}25\times10^5\,\mathrm{Pa}.
\end{aligned}
$$

Tốc độ tại chỗ thắt gấp bốn lần vì bán kính giảm một nửa, tức tiết diện giảm còn một phần tư.

</details>

### 12.52 (•): Giảm bán kính ống dẫn chất lỏng nhớt

Để duy trì lưu lượng $0{,}800\,\mathrm{m^3/s}$ của một chất lỏng nhớt qua ống trụ bán kính $0{,}210\,\mathrm m$, cần chênh lệch áp suất $6{,}00\times10^4\,\mathrm{Pa}$. Nếu giảm bán kính còn $0{,}0700\,\mathrm m$, phải tạo chênh lệch áp suất bao nhiêu để giữ nguyên lưu lượng?

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** $\Delta p_1=6{,}00\times10^4\,\mathrm{Pa}$, $R_1=0{,}210\,\mathrm m$ và $R_2=0{,}0700\,\mathrm m$. Giữ nguyên chất lỏng, chiều dài ống và lưu lượng.

**Hướng đi:**

- Dùng quan hệ $\Delta p\propto L/R^4$ của dòng nhớt tầng trong ống trụ. Khi các điều kiện khác giữ nguyên, chênh áp tỉ lệ nghịch lũy thừa bốn của bán kính.
- Lấy tỉ số hai chênh áp để khử hệ số phụ thuộc chất lỏng và lưu lượng. Giá trị lưu lượng đã cho không cần thay riêng vào công thức tỉ số.

**Lời giải:** Bán kính giảm ba lần nên

$$
\frac{\Delta p_2}{\Delta p_1}=\left(\frac{R_1}{R_2}\right)^4=3^4=81.
$$

Vì vậy,

$$
\begin{aligned}
\Delta p_2&=81\Delta p_1\\
&=4{,}86\times10^6\,\mathrm{Pa}.
\end{aligned}
$$

Bán kính giảm ba lần đòi hỏi chênh áp tăng tới $81$ lần ở cùng lưu lượng. Quan hệ đang dùng giả thiết dòng vẫn nằm trong phạm vi mô hình chảy tầng.

</details>

## Độ nhớt và lưu lượng

### 12.53: Mở rộng động mạch để tăng lưu lượng

Độ khó: Mức 2. Sinh học (BIO).

Máu có độ nhớt chảy qua một động mạch bị cholesterol làm hẹp một phần. Một bác sĩ phẫu thuật muốn lấy bớt lượng cholesterol để lưu lượng máu qua đoạn mạch tăng gấp đôi. Nếu đường kính ban đầu của lòng mạch còn thông là $D$, đường kính mới phải bằng bao nhiêu theo $D$ để đạt yêu cầu khi gradient áp suất giữ nguyên?

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Lưu lượng cần đổi từ $Q$ thành $Q'=2Q$. Cùng một đoạn mạch, cùng chất lưu, độ nhớt và gradient áp suất không đổi. Gọi đường kính mới là $D'$.

**Hướng đi:**

- Dùng mô hình dòng chảy tầng nhớt trong ống trụ. Ở cùng độ nhớt và gradient áp suất, lưu lượng tỉ lệ với lũy thừa bốn của bán kính, do đó cũng tỉ lệ với $D^4$.
- Lấy tỉ số lưu lượng để khử những đại lượng không thay đổi. Không đồng nhất tăng gấp đôi lưu lượng với tăng gấp đôi đường kính.

**Lời giải:** Trong mô hình đang xét:

$$
\frac{Q'}{Q}=\left(\frac{D'}D\right)^4.
$$

Thay yêu cầu $Q'/Q=2$:

$$
\begin{aligned}
D'&=2^{1/4}D\\
&\approx1{,}19D.
\end{aligned}
$$

Đường kính cần tăng khoảng $18{,}9\%$. Kết quả xét dòng tầng, tiết diện trụ và các điều kiện giữ nguyên đã nêu, không coi đây là một mô tả đầy đủ mọi biến đổi của động mạch thực.

</details>

## Bài tập tổng hợp

### 12.54: Áp suất và sự nén nước ở rãnh Mariana

Độ khó: Mức 2. Bài tập tổng hợp (CP).

Trong bài toán này, điểm sâu nhất được xét trong các đại dương Trái Đất nằm ở rãnh Mariana, sâu $10{,}92\,\mathrm{km}$.

(a) Coi nước không nén được và dùng khối lượng riêng nước biển để tính áp suất ở độ sâu ấy.

(b) Áp suất thực tế được cho là $1{,}16\times10^8\,\mathrm{Pa}$. Kết quả câu (a) nhỏ hơn vì khối lượng riêng thực sự tăng theo độ sâu. Dùng độ nén của nước và áp suất thực tế để tìm khối lượng riêng ở đáy. Khối lượng riêng thay đổi bao nhiêu phần trăm?

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** $h=10920\,\mathrm m$, khối lượng riêng ban đầu $\rho_0=1030\,\mathrm{kg/m^3}$. Lấy khí áp mặt biển $p_0=101325\,\mathrm{Pa}$. Độ nén của nước là $\kappa=4{,}58\times10^{-10}\,\mathrm{Pa^{-1}}$, còn áp suất đáy được cho là $p_b=1{,}16\times10^8\,\mathrm{Pa}$.

**Hướng đi:**

- Ở câu (a), dùng $p=p_0+\rho_0gh$ theo giả thiết khối lượng riêng không đổi. Phân biệt áp suất tuyệt đối với phần tăng áp do cột nước.
- Ở câu (b), dùng quan hệ biến dạng khối $\Delta V/V_0\approx-\kappa\Delta p$ với $\Delta p=p_b-p_0$. Khối lượng một phần nước không đổi khi bị nén, nên khối lượng riêng tăng khi thể tích giảm.
- Nêu rõ mức xấp xỉ. Giữ công thức thể tích tuyến tính rồi tính nghịch đảo cho một kết quả hơi khác với việc khai triển luôn khối lượng riêng đến bậc nhất.

**Lời giải:** (a) Phần áp suất do cột nước:

$$
\rho_0gh=1{,}1022648\times10^8\,\mathrm{Pa}.
$$

Áp suất tuyệt đối:

$$
\begin{aligned}
p&=p_0+\rho_0gh\\
&\approx1{,}1033\times10^8\,\mathrm{Pa}\\
&\approx1{,}10\times10^8\,\mathrm{Pa}.
\end{aligned}
$$

Giá trị nhỏ hơn áp suất thực tế đã cho.

(b) Đặt $\varepsilon=\kappa(p_b-p_0)$ là phần thể tích giảm theo mô hình nén tuyến tính. Tính được:

$$
\varepsilon\approx0{,}05308.
$$

Thể tích sau nén và sự bảo toàn khối lượng cho:

$$
V\approx V_0(1-\varepsilon).
$$

$$
\rho V=\rho_0V_0.
$$

Do đó:

$$
\rho\approx\frac{\rho_0}{1-\varepsilon}
\approx1088\,\mathrm{kg/m^3}.
$$

Trong mô hình này, phần tăng khối lượng riêng là:

$$
\frac{\rho-\rho_0}{\rho_0}
\approx0{,}0561.
$$

Khối lượng riêng tăng khoảng $5{,}6\%$.

Nếu giữ mọi đại lượng chỉ tới bậc nhất theo $\varepsilon$, dùng thêm xấp xỉ $1/(1-\varepsilon)\approx1+\varepsilon$. Khi ấy:

$$
\rho\approx\rho_0(1+\varepsilon)
\approx1085\,\mathrm{kg/m^3},
$$

và phần tăng khoảng $5{,}3\%$. Hai giá trị phản ánh hai cách giữ bậc của cùng phép xấp xỉ nén, không phải hai bộ dữ kiện khác nhau. Độ nén được coi không đổi chỉ là mô hình gần đúng trong khoảng áp suất này.

</details>

### 12.55: Lực nước tác dụng lên hồ bơi

Độ khó: Mức 3. Dùng giải tích (CALC).

Một hồ bơi dài $5{,}0\,\mathrm m$, rộng $4{,}0\,\mathrm m$ và sâu $3{,}0\,\mathrm m$. Tính lực của nước lên

(a) đáy hồ và

(b) một trong hai mặt đầu hồ.

Gợi ý: Với mặt đầu hồ, tính lực trên một dải ngang mỏng ở độ sâu $h$ rồi tích phân theo chiều sâu. Không kể lực do áp suất khí quyển.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Chiều dài $L=5{,}0\,\mathrm m$, chiều rộng $b=4{,}0\,\mathrm m$, chiều sâu $H=3{,}0\,\mathrm m$. Mỗi mặt đầu có kích thước $b\times H$. Dùng $\rho=1000\,\mathrm{kg/m^3}$ và chỉ xét áp suất dư.

**Hướng đi:**

- Ở đáy ngang, mọi điểm có cùng độ sâu $H$, nên áp suất đều và lực bằng áp suất nhân diện tích.
- Trên mặt đứng, áp suất tăng tuyến tính theo độ sâu. Chia thành dải ngang có diện tích $dA=b\,dh$ rồi cộng các lực bằng tích phân.
- Tất cả lực pháp tuyến trên một mặt đầu đều cùng hướng, nên độ lớn lực tổng bằng tổng các độ lớn vi phân.

**Lời giải:** (a) Áp suất dư ở đáy là $p_H=\rho gH$. Diện tích đáy $A=Lb$, do đó:

$$
\begin{aligned}
F_{\mathrm{day}}&=\rho gHLb\\
&=588000\,\mathrm N\\
&\approx5{,}9\times10^5\,\mathrm N.
\end{aligned}
$$

Lực hướng xuống, vuông góc đáy hồ.

(b) Chọn tọa độ $h$ đo xuống từ mặt nước. Áp suất ở độ sâu $h$ là $p(h)=\rho gh$. Trên dải ngang:

$$
dF=p(h)b\,dh=\rho gbh\,dh.
$$

Tích phân từ mặt nước tới đáy:

$$
\begin{aligned}
F_{\mathrm{dau}}&=\rho gb\int_0^Hh\,dh\\
&=\frac{\rho gbH^2}{2}\\
&=176400\,\mathrm N\\
&\approx1{,}8\times10^5\,\mathrm N.
\end{aligned}
$$

Lực hướng ngang, từ nước ra phía thành đầu hồ. Áp suất trung bình trên mặt đứng bằng $\rho gH/2$, nên có thể kiểm tra bằng áp suất trung bình nhân diện tích $bH$. Không lấy áp suất đáy nhân cả diện tích mặt đứng.

</details>

### 12.56: Trọng lượng đá từ hai lực căng

Độ khó: Mức 2.

Một hòn đá treo ở đầu dưới dây nhẹ. Khi ngập hoàn toàn trong nước, lực căng dây bằng $1{,}20\,\mathrm N$. Khi ngập hoàn toàn trong ethanol, lực căng là $1{,}60\,\mathrm N$. Dùng các khối lượng riêng trong Bảng 12.1 để tính trọng lượng hòn đá.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** $T_w=1{,}20\,\mathrm N$, $T_e=1{,}60\,\mathrm N$. Khối lượng riêng nước $\rho_w=1000\,\mathrm{kg/m^3}$, ethanol $\rho_e=810\,\mathrm{kg/m^3}$. Hòn đá có cùng thể tích $V$ trong hai lần nhúng.

**Hướng đi:**

- Viết cân bằng lực cho từng chất lỏng với cùng trọng lượng $w$.
- Lấy hiệu hai phương trình để khử $w$ và tìm thể tích từ độ khác nhau của lực đẩy. Sau đó thay lại để tìm trọng lượng.

**Lời giải:** Hai phương trình cân bằng:

$$
\begin{aligned}
&w=T_w+\rho_wgV,\\
&w=T_e+\rho_egV.
\end{aligned}
$$

Lấy hiệu:

$$
T_e-T_w=(\rho_w-\rho_e)gV.
$$

Thể tích:

$$
\begin{aligned}
V&=\frac{T_e-T_w}{(\rho_w-\rho_e)g}\\
&\approx2{,}15\times10^{-4}\,\mathrm{m^3}.
\end{aligned}
$$

Thay vào phương trình trong nước:

$$
\begin{aligned}
w&=T_w+\rho_wgV\\
&\approx3{,}31\,\mathrm N.
\end{aligned}
$$

Lực căng trong ethanol lớn hơn trong nước vì ethanol có khối lượng riêng nhỏ hơn, nên cùng thể tích đá nhận lực đẩy nhỏ hơn.

</details>

### 12.57: Mômen lực nước quanh trục giữa cửa đập

Độ khó: Mức 3. Bài tập tổng hợp (CP). Dùng giải tích (CALC).

Mép trên một cửa đập nằm ngang mặt nước. Cửa cao $2{,}00\,\mathrm m$, rộng $4{,}00\,\mathrm m$ và có bản lề theo một đường ngang qua chính giữa, như Hình P12.57. Tính mômen quanh trục bản lề do lực nước.

Gợi ý: Tính mômen trên một dải ngang mỏng ở độ sâu $h$ rồi tích phân trên toàn cửa, tương tự cách chia dải trong Bài 12.55.

![Hình P12.57: Cửa đập cao 2,00 m, rộng 4,00 m có trục bản lề nằm ngang qua giữa chiều cao.](/vat-ly-1/bai-giang/img/young-12/r-exercises-fig-p12-57.png)

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Cửa đứng có chiều cao $H=2{,}00\,\mathrm m$, chiều rộng $b=4{,}00\,\mathrm m$. Bản lề nằm ở độ sâu $H/2$. Mặt nước chịu khí áp và ta xét phần áp suất thủy tĩnh của nước.

**Hướng đi:**

- Dùng dải ngang $dA=b\,dh$ vì áp suất $\rho gh$ đều trên mỗi dải nhưng thay đổi theo độ sâu.
- Dùng cánh tay đòn có dấu $h-H/2$. Lực ở nửa trên và nửa dưới tạo mômen ngược chiều nhau quanh trục giữa.
- Cộng mômen có dấu bằng tích phân. Không dùng lực tổng nhân nửa chiều cao vì hợp lực không đặt tại mép cửa.

**Lời giải:** Chọn chiều mômen dương là chiều đẩy nửa dưới cửa ra xa phía nước. Lực lên dải ở độ sâu $h$:

$$
dF=\rho gbh\,dh.
$$

Mômen vi phân quanh trục giữa:

$$
d\tau=\rho gbh(h-H/2)\,dh.
$$

Tích phân trên toàn chiều cao:

$$
\tau=\rho gb\int_0^Hh(h-H/2)\,dh.
$$

Tính tích phân:

$$
\begin{aligned}
\tau&=\rho gb\left(\frac{H^3}{3}-\frac{H^3}{4}\right)\\
&=\frac{\rho gbH^3}{12}\\
&\approx2{,}61\times10^4\,\mathrm{N\,m}.
\end{aligned}
$$

Mômen dương theo quy ước đã chọn, vì áp suất lớn hơn ở nửa dưới. Cửa có xu hướng quay để nửa dưới dịch ra phía không có nước.

Có thể kiểm tra bằng hợp lực $F=\rho gbH^2/2$, đặt tại độ sâu $2H/3$. Cánh tay đòn tới trục giữa là $H/6$, nên $F(H/6)$ cho đúng mômen trên.

</details>

### 12.58: Khối gỗ nổi giữa nước và glycerin

Độ khó: Mức 3.

Một bồn lớn chứa lớp nước dày $40{,}0\,\mathrm{cm}$ nổi trên lớp glycerin dày $60{,}0\,\mathrm{cm}$. Một khối gỗ đặc, hình lập phương cạnh $2{,}00\,\mathrm{cm}$, có khối lượng $9{,}20\times10^{-3}\,\mathrm{kg}$. Khi khối nổi trong bồn, phần thể tích nào nằm dưới mặt glycerin?

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Cạnh khối $a=0{,}0200\,\mathrm m$, khối lượng $m=0{,}00920\,\mathrm{kg}$. Dùng $\rho_w=1000\,\mathrm{kg/m^3}$ và $\rho_g=1260\,\mathrm{kg/m^3}$. Hai lớp đều dày hơn nhiều so với kích thước khối.

**Hướng đi:**

- Tính khối lượng riêng của gỗ để xác định nó nổi ở mặt thoáng nước hay ở mặt phân cách hai chất.
- Nếu khối nặng hơn nước nhưng nhẹ hơn glycerin, nó cân bằng ở mặt phân cách và ngập hoàn toàn trong hai chất lỏng.
- Cộng lực đẩy do thể tích trong nước và thể tích trong glycerin, vì hai phần chiếm chỗ hai chất có khối lượng riêng khác nhau.

**Lời giải:** Thể tích khối và khối lượng riêng:

$$
V=a^3=8{,}00\times10^{-6}\,\mathrm{m^3}.
$$

$$
\rho_b=\frac mV=1150\,\mathrm{kg/m^3}.
$$

Ta có $\rho_w<\rho_b<\rho_g$, nên khối nằm tại mặt phân cách.

Gọi $f$ là phần thể tích trong glycerin. Phần còn lại $1-f$ nằm trong nước. Cân bằng nổi sau khi chia cho $gV$:

$$
\rho_w(1-f)+\rho_gf=\rho_b.
$$

Giải theo $f$:

$$
f=\frac{\rho_b-\rho_w}{\rho_g-\rho_w}
\approx0{,}577.
$$

Khoảng $57{,}7\%$ thể tích gỗ nằm dưới mặt glycerin. Phần này ứng với chiều cao khoảng $1{,}15\,\mathrm{cm}$ trong glycerin, phần còn lại khoảng $0{,}846\,\mathrm{cm}$ trong nước, đều nhỏ hơn bề dày hai lớp đã cho.

</details>

### 12.59: Khối lượng khối nhựa từ đường thẳng thực nghiệm

Độ khó: Mức 2.

Một khối nhựa hình hộp chữ nhật cao $8{,}00\,\mathrm{cm}$ có hai mặt ngang diện tích $A$ và nổi trong nước. Bạn đặt các đồng xu ở giữa mặt trên để mặt này luôn nằm ngang. Từ chiều cao nhô lên, bạn suy ra phần chiều cao $h$ chìm dưới nước cho từng tổng khối lượng xu $m$.

Đồ thị $h$ theo $m$ gần một đường thẳng có hệ số góc $0{,}0390\,\mathrm{m/kg}$ và tung độ gốc $0{,}0312\,\mathrm m$. Tính khối lượng khối nhựa.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Khối nhựa có khối lượng chưa biết $M$, chiều cao $H=0{,}0800\,\mathrm m$. Quan hệ đo có dạng $h=sm+b$, với $s=0{,}0390\,\mathrm{m/kg}$ và $b=0{,}0312\,\mathrm m$.

**Hướng đi:**

- Dùng cân bằng nổi cho cả khối nhựa và xu. Thể tích nước bị chiếm chỗ bằng $Ah$ khi các mặt ngang.
- Viết $h$ theo $m$ rồi so sánh hệ số góc và tung độ gốc. Tỉ số tung độ gốc với hệ số góc sẽ khử diện tích chưa biết.
- Xét các trạng thái xu còn ở trên mặt nước, chưa bị ngập và khối vẫn nổi, đúng phạm vi đo đang dùng.

**Lời giải:** Cân bằng lực:

$$
\rho_wgAh=(M+m)g.
$$

Khử $g$ và giải theo $h$:

$$
h=\frac{m}{\rho_wA}+\frac{M}{\rho_wA}.
$$

Đối chiếu với đường thẳng:

$$
\begin{aligned}
&s=\frac{1}{\rho_wA},\\
&b=\frac{M}{\rho_wA}=Ms.
\end{aligned}
$$

Vậy:

$$
M=\frac bs=0{,}800\,\mathrm{kg}.
$$

Tung độ gốc dương là độ chìm của riêng khối nhựa khi chưa có xu. Chiều cao $8{,}00\,\mathrm{cm}$ đặt giới hạn cho khoảng tải có thể khảo sát trước khi mặt trên chạm nước, nhưng không cần dùng riêng để tính $M$ từ hai hệ số đã biết.

</details>

### 12.60: Khí cầu thăm dò sao Hỏa

Độ khó: Mức 2.

Một đề xuất thăm dò sao Hỏa dùng khí cầu lơ lửng ngay trên bề mặt nhờ lực đẩy của khí quyển. Lấy khối lượng riêng khí quyển sao Hỏa là $0{,}0154\,\mathrm{kg/m^3}$, dù đại lượng này có thay đổi theo nhiệt độ.

Vỏ khí cầu làm bằng nhựa mỏng nhưng bền, mỗi mét vuông có khối lượng $5{,}00\,\mathrm g$. Khí cầu được bơm bằng khí rất nhẹ và có thể bỏ qua khối lượng khí bên trong.

(a) Bán kính và khối lượng khí cầu hình cầu phải bằng bao nhiêu để vừa đủ lơ lửng trên sao Hỏa?

(b) Đem một khí cầu ở câu (a) thả trên Trái Đất, nơi không khí có khối lượng riêng $1{,}20\,\mathrm{kg/m^3}$. Giữ nguyên kích thước như trên sao Hỏa, gia tốc ban đầu bằng bao nhiêu, hướng lên hay xuống?

(c) Nếu bán kính khí cầu trên sao Hỏa lớn gấp năm kết quả câu (a), nó có thể mang một bộ thiết bị nặng bao nhiêu?

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Khối lượng trên một đơn vị diện tích vỏ $\sigma=0{,}00500\,\mathrm{kg/m^2}$. Dùng $\rho_M=0{,}0154\,\mathrm{kg/m^3}$ cho khí quyển sao Hỏa và $\rho_E=1{,}20\,\mathrm{kg/m^3}$ cho không khí Trái Đất.

**Hướng đi:**

- Vỏ khí cầu có khối lượng tỉ lệ diện tích $4\pi r^2$, còn lực đẩy tỉ lệ thể tích $4\pi r^3/3$. Cân bằng hai lực để tìm bán kính giới hạn.
- Trên Trái Đất, dùng lực đẩy trừ trọng lượng để tính hợp lực rồi chia khối lượng khí cầu. Xét gia tốc ngay lúc thả, bỏ qua lực cản ở vận tốc đầu bằng không trong mô hình.
- Khi bán kính tăng năm lần, khối lượng vỏ tăng $25$ lần còn sức đỡ tính theo khối lượng khí quyển bị chiếm chỗ tăng $125$ lần. Hiệu hai phần là tải có thể mang.

**Lời giải:** (a) Khối lượng vỏ:

$$
M=4\pi r^2\sigma.
$$

Điều kiện lơ lửng trên sao Hỏa:

$$
\rho_Mg_M\frac{4\pi r^3}{3}=Mg_M.
$$

Thay biểu thức $M$ và rút gọn:

$$
r=\frac{3\sigma}{\rho_M}\approx0{,}974\,\mathrm m.
$$

Khối lượng khí cầu:

$$
M=4\pi r^2\sigma\approx0{,}0596\,\mathrm{kg}.
$$

Gia tốc trọng trường sao Hỏa triệt tiêu trong điều kiện cân bằng này.

(b) Do khí cầu ở câu (a) có $M=\rho_MV$, gia tốc trên Trái Đất là:

$$
\begin{aligned}
a&=\frac{\rho_EVg-Mg}{M}\\
&=g\left(\frac{\rho_E}{\rho_M}-1\right)\\
&\approx754\,\mathrm{m/s^2}.
\end{aligned}
$$

Gia tốc hướng lên, khoảng $76{,}9g$. Đây là gia tốc ban đầu của mô hình vỏ rất nhẹ, giữ nguyên thể tích và chỉ xét lực đẩy cùng trọng lực. Khi khí cầu đã chuyển động, lực cản và các tác dụng động lực học khác không còn được phép bỏ qua chỉ dựa vào kết quả ban đầu này.

(c) Gọi $M$ là khối lượng vỏ ở câu (a). Khí cầu bán kính $5r$ có vỏ khối lượng $25M$, trong khi khối lượng khí quyển bị chiếm chỗ bằng $125M$. Tải trọng cho phép tính theo khối lượng:

$$
\begin{aligned}
m_{\mathrm{tai}}&=125M-25M\\
&=100M.
\end{aligned}
$$

Do đó:

$$
m_{\mathrm{tai}}\approx5{,}96\,\mathrm{kg}.
$$

Nếu biểu diễn bằng trọng lượng trên sao Hỏa với $g_M=3{,}71\,\mathrm{m/s^2}$, tải này nặng khoảng $22{,}1\,\mathrm N$. Đây là tổng khối lượng thiết bị mà khí cầu có thể vừa đủ giữ lơ lửng theo các giả thiết đã cho.

</details>

### 12.61: Mực chất lỏng khi băng tan trong glycerin

Độ khó: Mức 2.

Một khối băng nước khối lượng $0{,}180\,\mathrm{kg}$ nổi trong glycerin chứa ở một bình trụ cao có bán kính trong $3{,}50\,\mathrm{cm}$. Mặt glycerin còn thấp hơn nhiều so với miệng bình. Nếu băng tan hoàn toàn, chiều cao mặt chất lỏng thay đổi bao nhiêu? Mặt nước sau cùng cao hơn hay thấp hơn mặt glycerin ban đầu?

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** $m=0{,}180\,\mathrm{kg}$, bán kính bình $R=0{,}0350\,\mathrm m$. Dùng $\rho_g=1260\,\mathrm{kg/m^3}$ và $\rho_w=1000\,\mathrm{kg/m^3}$. Xét các thể tích theo khối lượng riêng đã cho và bỏ qua thay đổi thể tích do hòa trộn.

**Hướng đi:**

- Khi băng nổi, thể tích glycerin bị chiếm chỗ bằng $m/\rho_g$, suy từ cân bằng nổi. Không dùng toàn thể tích băng để tính mực glycerin ban đầu.
- Sau khi tan, cùng khối lượng ấy tạo lượng nước thể tích $m/\rho_w$.
- Lấy hiệu hai thể tích góp vào phần dưới mặt chất lỏng, rồi chia tiết diện bình để tìm độ đổi chiều cao.

**Lời giải:** Lúc đầu, băng làm dâng glycerin bằng thể tích chiếm chỗ:

$$
\begin{aligned}
V_{\mathrm{chiem}}&=\frac m{\rho_g}\\
&\approx1{,}43\times10^{-4}\,\mathrm{m^3}.
\end{aligned}
$$

Thể tích nước sau khi băng tan:

$$
V_w=\frac m{\rho_w}=1{,}80\times10^{-4}\,\mathrm{m^3}.
$$

Độ tăng thể tích dưới mặt chất lỏng:

$$
\Delta V=m\left(\frac1{\rho_w}-\frac1{\rho_g}\right).
$$

Vì $\rho_w<\rho_g$, ta có $\Delta V>0$. Độ cao tăng:

$$
\begin{aligned}
\Delta h&=\frac{\Delta V}{\pi R^2}\\
&\approx0{,}00965\,\mathrm m\\
&=9{,}65\,\mathrm{mm}.
\end{aligned}
$$

Mặt chất lỏng tăng lên. Kết quả khác trường hợp băng nổi và tan trong chính nước, vì ở đây chất lỏng bị chiếm chỗ ban đầu là glycerin đặc hơn nước tan ra.

</details>

### 12.62: Hai cột dầu và nước sau khi bỏ vách ngăn

Độ khó: Mức 2.

Một ống thủy tinh chữ U hẹp, hai đầu hở, ban đầu có cột dầu cao $25{,}0\,\mathrm{cm}$ ở một phía và cột nước cao $25{,}0\,\mathrm{cm}$ ở phía kia. Dầu có tỉ khối $0{,}80$, còn hai chất được giữ riêng bằng vách ngăn như Hình P12.62.

(a) Bỏ vách ngăn, giả sử hai chất không trộn. Tìm chiều cao cuối cùng của các cột chất lỏng ở hai nhánh.

(b) Không tính toán, dùng lập luận vật lý để cho biết chiều cao mỗi nhánh nếu (i) dầu và nước có cùng khối lượng riêng, (ii) khối lượng riêng dầu rất nhỏ so với nước.

![Hình P12.62: Hai cột nước và dầu ban đầu cao bằng nhau được giữ riêng trong ống chữ U bằng vách ngăn.](/vat-ly-1/bai-giang/img/young-12/r-exercises-fig-p12-62.png)

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Cột ban đầu $H=0{,}250\,\mathrm m$, $\rho_o=0{,}80\rho_w$. Ống có cùng tiết diện nhỏ ở hai nhánh và coi phần cong ở đáy không làm thay đổi phép đếm chiều dài cột. Nhánh A chứa nước, nhánh B chứa dầu.

**Hướng đi:**

- Dầu nhẹ hơn nên nằm phía trên nước sau khi bỏ vách. Chiều dài cột dầu vẫn là $H$, còn nước được phân bố sang hai nhánh.
- Bảo toàn thể tích nước cho tổng hai chiều cao phần nước bằng $H$. Cân bằng áp suất ở đáy cho quan hệ thứ hai.
- Trong các trường hợp giới hạn ở câu (b), dùng cân bằng áp suất và bảo toàn thể tích để hình dung vị trí các mặt thoáng, thay vì chỉ thay số vào công thức.

**Lời giải:** (a) Gọi $x$ là chiều cao nước ở nhánh A và $z$ là chiều cao nước phía dưới dầu ở nhánh B. Thể tích nước không đổi:

$$
x+z=H.
$$

Áp suất đáy ở hai phía bằng nhau:

$$
\rho_wgx=\rho_wgz+\rho_ogH.
$$

Khử $g$ và chia cho $\rho_w$:

$$
x-z=0{,}80H.
$$

Giải hai phương trình:

$$
\begin{aligned}
&x=0{,}225\,\mathrm m,\\
&z=0{,}0250\,\mathrm m.
\end{aligned}
$$

Vậy mặt thoáng ở A cao $22{,}5\,\mathrm{cm}$ trên đáy, còn ở B cao:

$$
z+H=27{,}5\,\mathrm{cm}.
$$

Trong nhánh B, phần dưới $2{,}50\,\mathrm{cm}$ là nước, phần trên $25{,}0\,\mathrm{cm}$ là dầu.

(b)(i) Nếu hai chất có cùng khối lượng riêng, cân bằng đòi hỏi hai mặt thoáng cùng cao độ. Tổng lượng chất lỏng và hai tiết diện không đổi, nên hai mức đều giữ ở $25{,}0\,\mathrm{cm}$.

(ii) Nếu dầu nhẹ đến mức áp suất do nó gần như không đáng kể, mặt phân cách nước–dầu và mặt nước nhánh kia sẽ gần cùng cao độ. Lượng nước chia đều cho hai nhánh, nên mỗi phần nước cao gần $12{,}5\,\mathrm{cm}$.

Cột dầu vẫn cao $25{,}0\,\mathrm{cm}$ ở nhánh B. Do đó mặt nước A cao gần $12{,}5\,\mathrm{cm}$, còn mặt dầu B cao gần $37{,}5\,\mathrm{cm}$ trên đáy.

</details>

### 12.63: Mức nước và thủy ngân trong ống chữ U

Độ khó: Mức 1.

Một ống chữ U chứa thủy ngân và hở ra không khí ở cả hai đầu. Đổ nước cẩn thận vào nhánh trái tới khi cột nước có chiều cao thẳng đứng $15{,}0\,\mathrm{cm}$ như Hình P12.63.

(a) Tính áp suất dư ở mặt phân cách nước–thủy ngân.

(b) Tính khoảng cách thẳng đứng $h$ từ mặt thủy ngân ở nhánh phải tới mặt nước ở nhánh trái.

![Hình P12.63: Cột nước cao 15,0 cm phía trên thủy ngân làm hai mặt thủy ngân lệch nhau.](/vat-ly-1/bai-giang/img/young-12/r-exercises-fig-p12-63.png)

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Cột nước có $H=0{,}150\,\mathrm m$, $\rho_w=1000\,\mathrm{kg/m^3}$ và thủy ngân có $\rho_m=13600\,\mathrm{kg/m^3}$. Hai mặt thoáng đều chịu khí áp.

**Hướng đi:**

- Tính áp suất dư ở đáy cột nước bằng $\rho_wgH$.
- Tại cùng cao độ trong thủy ngân liên thông, áp suất bằng nhau. Từ đó tìm độ cao mặt thủy ngân bên phải so với mặt phân cách bên trái.
- Khoảng cách cần hỏi là chiều cao cột nước trừ độ chênh mức thủy ngân, không phải chính độ chênh mức thủy ngân.

**Lời giải:** (a) Áp suất dư ở mặt phân cách:

$$
p_g=\rho_wgH=1470\,\mathrm{Pa}.
$$

(b) Gọi $\delta$ là độ cao mặt thủy ngân bên phải trên mặt phân cách. Khi đi từ mặt thủy ngân phải xuống mức mặt phân cách:

$$
\rho_mg\delta=p_g.
$$

Suy ra:

$$
\delta=\frac{\rho_wH}{\rho_m}
\approx0{,}0110\,\mathrm m.
$$

Mặt nước bên trái cao hơn mặt phân cách $H$, nên:

$$
h=H-\delta\approx0{,}139\,\mathrm m.
$$

Khoảng cách được hỏi là $13{,}9\,\mathrm{cm}$, trong khi hai mặt thủy ngân chỉ chênh khoảng $1{,}10\,\mathrm{cm}$.

</details>

### 12.64: Lực lên thành bồn trong trận lũ mật mía Boston

Độ khó: Mức 2. Dùng giải tích (CALC).

Chiều ngày 15 tháng 1 năm 1919, một ngày ấm bất thường ở Boston, một bồn kim loại hình trụ chứa mật mía cao $17{,}7\,\mathrm m$, đường kính $27{,}4\,\mathrm m$ bị vỡ. Mật mía tràn ra đường thành dòng sâu khoảng $5\,\mathrm m$, làm chết người đi bộ và ngựa, đồng thời làm đổ các tòa nhà.

Mật mía có khối lượng riêng $1600\,\mathrm{kg/m^3}$. Nếu trước tai nạn bồn đầy, tổng độ lớn lực hướng ra ngoài mà mật mía tác dụng lên các thành bên là bao nhiêu?

Gợi ý: Xét một vành tròn mỏng của thành bồn, bề rộng $dy$, ở độ sâu $y$ dưới mặt mật mía rồi tích phân. Trước khi bồn vỡ, áp suất trên mặt mật mía bằng áp suất không khí ngoài bồn.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Bồn cao $H=17{,}7\,\mathrm m$, đường kính $D=27{,}4\,\mathrm m$, mật mía có $\rho=1600\,\mathrm{kg/m^3}$. Phần áp suất khí quyển hai phía thành triệt tiêu, nên chỉ tính tải do áp suất dư.

**Hướng đi:**

- Chia thành bên thành những vành ngang vì áp suất có cùng giá trị tại mọi điểm trên một vành cùng độ sâu.
- Diện tích vành là chu vi $\pi D$ nhân bề rộng $dy$. Cộng độ lớn các lực pháp tuyến hướng ra bằng tích phân theo độ sâu.
- Phân biệt tổng độ lớn tải hướng ra với hợp lực vector trên toàn mặt trụ. Các lực ở hai phía đối diện có thể triệt tiêu về vector nhưng vẫn kéo căng thành bồn.

**Lời giải:** Ở độ sâu $y$, áp suất dư là $p_g=\rho gy$. Vành mỏng có diện tích:

$$
dA=\pi D\,dy.
$$

Tổng độ lớn lực trên vành:

$$
dF=\rho gy\,\pi D\,dy.
$$

Tích phân theo chiều sâu:

$$
\begin{aligned}
F&=\rho g\pi D\int_0^Hy\,dy\\
&=\frac{\rho g\pi DH^2}{2}\\
&\approx2{,}11\times10^8\,\mathrm N.
\end{aligned}
$$

Đây là tổng độ lớn lực hướng ra trên toàn thành bên. Trong mô hình bồn trụ đối xứng, hợp lực vector theo phương ngang trên cả thành bằng không. Điều đó không làm tải phá hủy trên thành mất đi, vì các phần thành vẫn chịu lực đẩy ra theo những hướng khác nhau.

</details>

### 12.65: Chở gạch trên khối gỗ nổi

Độ khó: Mức 2.

Một khối gỗ lập phương lớn, đồng nhất, khối lượng $40{,}0\,\mathrm{kg}$ nổi trên hồ nước ngọt với $20{,}0\%$ thể tích nằm trên mặt nước. Bạn muốn xếp gạch lên khối gỗ rồi đẩy ngang qua hồ tới đảo để xây một bếp nướng ngoài trời.

(a) Tính thể tích khối gỗ.

(b) Khối lượng gạch lớn nhất có thể đặt lên mà khối gỗ chưa chìm dưới mặt nước bằng bao nhiêu?

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Khối lượng gỗ $M=40{,}0\,\mathrm{kg}$, phần chìm ban đầu $f=0{,}800$, nước có $\rho_w=1000\,\mathrm{kg/m^3}$. Xét trạng thái nổi cân bằng trước khi vận chuyển.

**Hướng đi:**

- Dùng cân bằng nổi ban đầu để suy ra thể tích từ phần chìm đã biết.
- Tải gạch lớn nhất đạt tại giới hạn khối gỗ vừa ngập toàn bộ. Lực đẩy khi ấy phải đỡ cả gỗ và gạch.
- Bỏ qua thể tích chiếm chỗ của gạch vì bài xét giới hạn mặt trên khối gỗ vừa tới mặt nước, còn gạch vẫn đặt ở trên.

**Lời giải:** (a) Từ cân bằng ban đầu:

$$
\rho_wgfV=Mg.
$$

Do đó:

$$
V=\frac{M}{\rho_wf}=0{,}0500\,\mathrm{m^3}.
$$

(b) Gọi $m$ là khối lượng gạch. Ở giới hạn:

$$
\rho_wgV=(M+m)g.
$$

Suy ra:

$$
m_{\max}=\rho_wV-M=10{,}0\,\mathrm{kg}.
$$

Đây là giới hạn của mô hình cân bằng. Muốn mặt trên gỗ còn cao hơn mặt nước một khoảng dương, lượng gạch phải nhỏ hơn $10{,}0\,\mathrm{kg}$.

</details>

### 12.66: Khối lượng riêng khí nóng trong khí cầu

Độ khó: Mức 3.

Một khí cầu khí nóng có thể tích $2200\,\mathrm{m^3}$. Vải vỏ khí cầu nặng $900\,\mathrm N$. Giỏ cùng thiết bị và các bình propane đầy nặng $1700\,\mathrm N$. Khí cầu vừa đủ nâng thêm $3200\,\mathrm N$ gồm hành khách, bữa sáng và champagne khi không khí ngoài có khối lượng riêng $1{,}23\,\mathrm{kg/m^3}$.

Tính khối lượng riêng trung bình của các khí đã được đốt nóng bên trong vỏ.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** $V=2200\,\mathrm{m^3}$, $\rho_a=1{,}23\,\mathrm{kg/m^3}$. Ba phần trọng lượng ngoài khí nóng là $900$, $1700$ và $3200\,\mathrm N$.

**Hướng đi:**

- Lực đẩy bằng trọng lượng không khí bên ngoài bị chiếm chỗ, tức $\rho_a gV$.
- Khí cầu vừa đủ nâng tải nên coi tổng lực thẳng đứng bằng không. Tổng trọng lượng phải gồm cả khí nóng bên trong, không chỉ vỏ và hành khách.
- Tách trọng lượng khí nóng rồi dùng $m=\rho V$ để tìm khối lượng riêng trung bình.

**Lời giải:** Tổng trọng lượng không kể khí nóng:

$$
W_0=5800\,\mathrm N.
$$

Lực đẩy:

$$
B=\rho_agV=26518{,}8\,\mathrm N.
$$

Gọi $\rho_h$ là khối lượng riêng khí nóng. Điều kiện cân bằng:

$$
\rho_agV=W_0+\rho_hgV.
$$

Do đó:

$$
\begin{aligned}
\rho_h&=\rho_a-\frac{W_0}{gV}\\
&\approx0{,}961\,\mathrm{kg/m^3}.
\end{aligned}
$$

Khối lượng riêng khí nóng nhỏ hơn không khí bên ngoài. Phần chênh lệch ấy tạo sức nâng đủ đỡ vỏ, giỏ và toàn bộ tải bổ sung.

</details>

### 12.67: Tải than cực đại của sà lan

Độ khó: Mức 1.

Một sà lan hở có các kích thước như Hình P12.67: Dài $40\,\mathrm m$, rộng $22\,\mathrm m$, cao $12\,\mathrm m$. Bốn thành bên và đáy đều làm bằng tấm thép dày $4{,}0\,\mathrm{cm}$.

Sà lan có thể chở bao nhiêu than trong nước ngọt mà chưa chìm? Trong lòng sà lan có đủ chỗ để chứa khối lượng than đó không? Lấy khối lượng riêng than khoảng $1500\,\mathrm{kg/m^3}$.

![Hình P12.67: Sà lan hở dài 40 m, rộng 22 m, cao 12 m, có bốn thành và đáy bằng thép.](/vat-ly-1/bai-giang/img/young-12/r-exercises-fig-p12-67.png)

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Lấy kích thước hình là kích thước ngoài $L=40\,\mathrm m$, $b=22\,\mathrm m$, $H=12\,\mathrm m$ và bề dày $t=0{,}040\,\mathrm m$. Thép có $\rho_s=7800\,\mathrm{kg/m^3}$, nước ngọt có $\rho_w=1000\,\mathrm{kg/m^3}$.

**Hướng đi:**

- Ở giới hạn tải, mép trên sà lan vừa ngang mặt nước. Thể tích chiếm chỗ đạt $LbH$.
- Từ khối lượng nước chiếm chỗ, trừ khối lượng thép để tìm tải than. Sà lan hở nên không có tấm thép ở mặt trên.
- Kiểm tra thể tích than bằng khối lượng chia khối lượng riêng. So sánh với thể tích rỗng bên trong để bảo đảm điều kiện sức nâng và điều kiện chứa cùng thỏa mãn.

**Lời giải:** Thể tích ngoài ở giới hạn:

$$
V_o=LbH=10560\,\mathrm{m^3}.
$$

Các kích thước trong lần lượt là $L_i=L-2t$, $b_i=b-2t$ và $H_i=H-t$. Đặt $V_i$ là thể tích lòng sà lan:

$$
V_i=L_ib_iH_i.
$$

Tính được $V_i\approx10465{,}6\,\mathrm{m^3}$. Thể tích thép:

$$
V_s=V_o-V_i\approx94{,}45\,\mathrm{m^3}.
$$

Khối lượng sà lan:

$$
M_s=\rho_sV_s\approx7{,}37\times10^5\,\mathrm{kg}.
$$

Ở giới hạn nổi, tổng khối lượng bằng $\rho_wV_o$. Tải than cực đại:

$$
\begin{aligned}
M_c&=\rho_wV_o-M_s\\
&\approx9{,}82\times10^6\,\mathrm{kg}.
\end{aligned}
$$

Xấp xỉ các thành là những tấm mỏng cũng cho khoảng $9{,}8\times10^6\,\mathrm{kg}$ ở độ chính xác của kích thước đã cho.

Với $\rho_c=1500\,\mathrm{kg/m^3}$, thể tích than:

$$
V_c=\frac{M_c}{\rho_c}\approx6{,}55\times10^3\,\mathrm{m^3}.
$$

Giá trị này nhỏ hơn thể tích lòng sà lan khoảng $1{,}05\times10^4\,\mathrm{m^3}$. Vì vậy có đủ chỗ chứa lượng than theo mô hình, với tải phân bố để sà lan giữ cân bằng. Tải cực đại vừa tìm là ngưỡng mép trên chạm nước, không còn phần mạn khô dự trữ.

</details>

### 12.68: Gắn chì để dìm khối gỗ tới mặt trên

Độ khó: Mức 3.

Một miếng gỗ dài $0{,}600\,\mathrm m$, rộng $0{,}250\,\mathrm m$, dày $0{,}080\,\mathrm m$, có khối lượng riêng $700\,\mathrm{kg/m^3}$. Cần gắn bên dưới thể tích chì bao nhiêu để gỗ nổi trong nước yên lặng với mặt trên vừa ngang mặt nước? Phần chì ấy có khối lượng bao nhiêu?

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Gỗ có thể tích $V_w$, khối lượng riêng $\rho_b=700\,\mathrm{kg/m^3}$. Dùng $\rho_l=11300\,\mathrm{kg/m^3}$ cho chì và $\rho_w=1000\,\mathrm{kg/m^3}$ cho nước. Gỗ và chì đều ngập hoàn toàn ở trạng thái cần tìm.

**Hướng đi:**

- Cân bằng cho cả gỗ và chì, vì phần chì vừa thêm trọng lượng vừa chiếm chỗ nước.
- Lực đẩy phải tính trên tổng thể tích ngập $V_w+V_l$. Không chỉ gán toàn trọng lượng chì cho phần sức nâng còn dư của riêng gỗ.
- Sau khi tìm $V_l$, dùng $m_l=\rho_lV_l$.

**Lời giải:** Gọi $L,b,h$ là chiều dài, chiều rộng và bề dày gỗ đã cho. Thể tích:

$$
V_w=Lbh.
$$

$$
V_w=0{,}0120\,\mathrm{m^3}.
$$

Cân bằng lực sau khi chia cho $g$:

$$
\rho_w(V_w+V_l)=\rho_bV_w+\rho_lV_l.
$$

Chuyển các phần chứa $V_l$ về cùng một phía:

$$
(\rho_l-\rho_w)V_l=(\rho_w-\rho_b)V_w.
$$

Do đó:

$$
\begin{aligned}
V_l&=\frac{(\rho_w-\rho_b)V_w}{\rho_l-\rho_w}\\
&\approx3{,}50\times10^{-4}\,\mathrm{m^3}.
\end{aligned}
$$

Khối lượng chì:

$$
m_l=\rho_lV_l\approx3{,}95\,\mathrm{kg}.
$$

Phải tính lực đẩy lên chì vì chì cũng nằm trong nước. Nếu bỏ phần này, lượng chì dự đoán sẽ nhỏ hơn lượng thật cần trong mô hình.

</details>

### 12.69: Tầm ngang của tia sữa từ bình trên bàn

Độ khó: Mức 2.

Một bình nhựa đầy một gallon sữa đặt sát mép bàn bếp. Hãy ước lượng khoảng cách thẳng đứng từ mặt sữa tới đáy bình, đồng thời ước lượng độ cao mặt bàn so với sàn. Bạn đục một lỗ nhỏ ở thành bình ngay trên đáy để sữa chảy ngang ra ngoài.

Khi sữa vừa bắt đầu chảy, nó đi được bao xa theo phương ngang trước khi chạm sàn? Coi sữa rơi tự do sau khi qua lỗ và bỏ qua độ nhớt.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Gọi $h$ là độ cao mặt sữa trên lỗ và $H$ là độ cao lỗ trên sàn. Hai độ dài phải được tự ước lượng. Bình cần thông khí để mặt sữa gần áp suất khí quyển trong mô hình dòng thoát được dùng.

**Hướng đi:**

- Dùng Torricelli $v=\sqrt{2gh}$ vì bình lớn so với lỗ và xét thời điểm đầu, mặt sữa chưa hạ đáng kể.
- Sau khi qua lỗ, tia sữa có vận tốc ban đầu nằm ngang. Thời gian tới sàn phụ thuộc $H$, còn tầm ngang bằng tốc độ ra nhân thời gian rơi.
- Giữ công thức theo $h,H$ trước khi chọn số ước lượng. Một gallon là bối cảnh kích thước bình, chưa đủ để suy ra duy nhất chiều cao chất lỏng.

**Lời giải:** Tốc độ ra ban đầu:

$$
v=\sqrt{2gh}.
$$

Chuyển động đứng bắt đầu với vận tốc đứng bằng không:

$$
H=\frac12gt^2.
$$

Do đó $t=\sqrt{2H/g}$. Tầm ngang:

$$
\begin{aligned}
R&=vt\\
&=\sqrt{2gh}\sqrt{\frac{2H}{g}}\\
&=2\sqrt{hH}.
\end{aligned}
$$

Chẳng hạn, chọn minh họa $h=0{,}25\,\mathrm m$ và $H=0{,}80\,\mathrm m$. Khi ấy:

$$
R\approx0{,}894\,\mathrm m.
$$

Theo bộ ước lượng này, sữa đi ngang khoảng $0{,}9\,\mathrm m$ trước khi chạm sàn. Với các số đo khác của bình và bàn, thay lại vào công thức. Nếu bình kín không thông khí, áp suất mặt sữa có thể giảm và mô hình trên phải được điều chỉnh.

</details>

### 12.70: Áp suất cấp cho dòng ethanol đi lên

Độ khó: Mức 2.

Ethanol chảy và luôn chiếm đầy ống. Tại A, áp suất dư là $p$ và tiết diện $0{,}0500\,\mathrm{m^2}$. Đầu B hở ra không khí có tiết diện $0{,}0200\,\mathrm{m^2}$ và cao hơn A $3{,}00\,\mathrm m$. Để lưu lượng tại B bằng $0{,}0800\,\mathrm{m^3/s}$, áp suất dư ở A phải bằng bao nhiêu?

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** $A_A=0{,}0500\,\mathrm{m^2}$, $A_B=0{,}0200\,\mathrm{m^2}$, $Q=0{,}0800\,\mathrm{m^3/s}$ và $h=3{,}00\,\mathrm m$. Ethanol có $\rho=810\,\mathrm{kg/m^3}$. Lấy áp suất dư tại B bằng không.

**Hướng đi:**

- Dùng $v=Q/A$ để tìm hai tốc độ trước khi xét chênh áp.
- Dùng Bernoulli trong mô hình dòng ổn định, chất lưu không nén được và bỏ qua ma sát nội. Áp suất ở A phải cung cấp cả phần tăng động năng lẫn phần tăng thế năng khi đi tới B.
- Cùng dùng áp suất dư theo một mốc khí quyển, nên không cộng thêm khí áp vào riêng một phía.

**Lời giải:** Hai tốc độ:

$$
\begin{aligned}
&v_A=\frac{Q}{A_A}=1{,}60\,\mathrm{m/s},\\
&v_B=\frac{Q}{A_B}=4{,}00\,\mathrm{m/s}.
\end{aligned}
$$

Đặt $\Delta(v^2)=v_B^2-v_A^2$ là hiệu hai bình phương tốc độ. Từ Bernoulli:

$$
p=\frac{\rho}{2}\Delta(v^2)+\rho gh.
$$

Các phần đóng góp:

$$
\begin{aligned}
&p_v=\frac{\rho}{2}\Delta(v^2)=5443{,}2\,\mathrm{Pa},\\
&p_h=\rho gh=23814\,\mathrm{Pa}.
\end{aligned}
$$

Vậy:

$$
\begin{aligned}
p&=p_v+p_h\\
&\approx2{,}93\times10^4\,\mathrm{Pa}.
\end{aligned}
$$

Áp suất dư cần khoảng $29{,}3\,\mathrm{kPa}$. Cả hai phần đều dương vì chất lỏng đi lên cao và tăng tốc ở đoạn hẹp hơn.

</details>

### 12.71: Chọn đường kính vòi chữa cháy

Độ khó: Mức 2. Bài tập tổng hợp (CP).

Một vòi chữa cháy phải phun được nước tới đỉnh tòa nhà cao $28{,}0\,\mathrm m$ khi chĩa thẳng đứng lên. Nước vào vòi đều với lưu lượng $0{,}500\,\mathrm{m^3/s}$ và ra qua đầu phun tròn. Bỏ qua lực cản không khí.

(a) Đầu phun có đường kính lớn nhất bao nhiêu?

(b) Nếu chỉ có đầu phun đường kính lớn gấp đôi giá trị ấy, độ cao lớn nhất tia nước đạt được bằng bao nhiêu?

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Độ cao cần đạt so với đầu phun là $H=28{,}0\,\mathrm m$, lưu lượng $Q=0{,}500\,\mathrm{m^3/s}$. Coi đầu phun đặt gần mức chân tòa nhà để độ cao cần đạt là $H$ như mô hình đề bài.

**Hướng đi:**

- Dùng chuyển động thẳng đứng hoặc bảo toàn cơ năng cho nước sau khi ra vòi để tìm tốc độ ra nhỏ nhất, $v_{\min}=\sqrt{2gH}$.
- Dùng $Q=Av$. Với lưu lượng giữ nguyên, tốc độ tối thiểu tương ứng diện tích và đường kính đầu phun lớn nhất.
- Khi đường kính tăng hai lần, diện tích tăng bốn lần nên tốc độ giảm bốn lần. Độ cao cực đại tỉ lệ bình phương tốc độ.

**Lời giải:** (a) Tốc độ nhỏ nhất đủ đạt độ cao:

$$
v_{\min}=\sqrt{2gH}\approx23{,}4\,\mathrm{m/s}.
$$

Diện tích cực đại là $A_{\max}=Q/v_{\min}$. Do đó:

$$
D_{\max}=\sqrt{\frac{4Q}{\pi v_{\min}}}
\approx0{,}165\,\mathrm m.
$$

Đường kính lớn nhất khoảng $16{,}5\,\mathrm{cm}$.

(b) Với $D'=2D_{\max}$, diện tích mới $A'=4A_{\max}$, nên tốc độ ra chỉ còn:

$$
v'=\frac{v_{\min}}4.
$$

Độ cao lớn nhất:

$$
\begin{aligned}
H'&=\frac{v'^2}{2g}\\
&=\frac{H}{16}\\
&=1{,}75\,\mathrm m.
\end{aligned}
$$

Tăng đường kính làm tia nước lên thấp hơn nếu lưu lượng không đổi. Kết luận ở đây giữ đúng điều kiện lưu lượng đã cho, không giả thiết tốc độ ra tự giữ nguyên khi đổi đầu phun.

</details>

### 12.72: Hai cân và khối vật nhúng trong chất lỏng

Độ khó: Mức 2.

Khối A trong Hình P12.72 được treo bằng dây từ cân lò xo D và ngập trong chất lỏng C chứa ở cốc B. Cốc có khối lượng $1{,}00\,\mathrm{kg}$, chất lỏng có khối lượng $1{,}80\,\mathrm{kg}$. Cân D chỉ $3{,}50\,\mathrm{kg}$, còn cân E đỡ cốc chỉ $7{,}50\,\mathrm{kg}$. Thể tích khối A là $3{,}80\times10^{-3}\,\mathrm{m^3}$.

(a) Tính khối lượng riêng chất lỏng.

(b) Mỗi cân sẽ chỉ bao nhiêu nếu khối A được kéo lên hẳn khỏi chất lỏng?

![Hình P12.72: Cân D treo khối A trong chất lỏng C. Cốc B cùng chất lỏng được đỡ riêng bởi cân E.](/vat-ly-1/bai-giang/img/young-12/r-exercises-fig-p12-72.png)

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Khối lượng cốc $m_B=1{,}00\,\mathrm{kg}$, chất lỏng $m_C=1{,}80\,\mathrm{kg}$. Các số chỉ khối lượng tương đương ban đầu là $r_D=3{,}50\,\mathrm{kg}$ và $r_E=7{,}50\,\mathrm{kg}$. Khối A ngập hoàn toàn, không chạm đáy cốc.

**Hướng đi:**

- Số chỉ theo kilôgam của mỗi cân là lực nó đỡ chia cho $g$. Không coi $7{,}50\,\mathrm{kg}$ là một lực tính bằng newton.
- Khối A nhận lực đẩy $B$ hướng lên, nên theo định luật III Newton nó đẩy chất lỏng xuống một lực cùng độ lớn. Cân E phải đỡ thêm phản lực ấy.
- Sau khi tìm $B$ từ cân E, dùng $B=\rho gV$ để tính khối lượng riêng. Dùng cân bằng khối A để tìm khối lượng thật và số chỉ cân D khi không còn lực đẩy chất lỏng.

**Lời giải:** (a) Cân E đỡ trọng lượng cốc, chất lỏng và phản lực do A tác dụng lên chất lỏng:

$$
r_Eg=(m_B+m_C)g+B.
$$

Chia cho $g$:

$$
\begin{aligned}
\frac Bg&=r_E-m_B-m_C\\
&=4{,}70\,\mathrm{kg}.
\end{aligned}
$$

Vậy lực đẩy $B=46{,}06\,\mathrm N$. Với $V=3{,}80\times10^{-3}\,\mathrm{m^3}$:

$$
\begin{aligned}
\rho&=\frac{B/g}{V}\\
&\approx1{,}24\times10^3\,\mathrm{kg/m^3}.
\end{aligned}
$$

(b) Gọi $m_A$ là khối lượng thật của A. Cân bằng trên A cho:

$$
r_Dg+B=m_Ag.
$$

Suy ra:

$$
m_A=r_D+\frac Bg=8{,}20\,\mathrm{kg}.
$$

Khi A được kéo lên hẳn, bỏ qua lực đẩy không khí, cân D đỡ toàn trọng lượng A nên chỉ $8{,}20\,\mathrm{kg}$.

Cân E không còn nhận phản lực của A qua chất lỏng, nên chỉ còn đỡ cốc và lượng chất lỏng giữ nguyên:

$$
r'_E=m_B+m_C=2{,}80\,\mathrm{kg}.
$$

Tổng hai số chỉ vẫn là $11{,}0\,\mathrm{kg}$ trước và sau khi nhấc vật. Đó là cách kiểm tra rằng việc nhấc A chỉ chuyển phần tải giữa hai cân, không làm thay đổi tổng khối lượng của hệ đang xét.

</details>

### 12.73 (•••, CALC): Tháo nước khỏi bồn có khí nén

Một bồn trụ kín đặt trên cao, đường kính $2{,}00\,\mathrm m$, chứa nước sâu $0{,}800\,\mathrm m$. Một công nhân vô ý đục một lỗ tròn đường kính $0{,}0200\,\mathrm m$ ở đáy bồn. Trong khi nước thoát, khí nén phía trên luôn duy trì áp suất dư $5{,}00\times10^3\,\mathrm{Pa}$ tại mặt nước. Bỏ qua độ nhớt.

(a) Ngay sau khi có lỗ, tốc độ nước thoát bằng bao nhiêu? Tỉ số của tốc độ này với tốc độ khi bồn hở ra khí quyển bằng bao nhiêu?

(b) Nước thoát hết sau bao lâu? Tỉ số của thời gian ấy với thời gian tháo hết nước khi bồn hở bằng bao nhiêu?

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Gọi $A$ là tiết diện bồn, $a$ là tiết diện lỗ, $H=0{,}800\,\mathrm m$ là độ sâu đầu và $y$ là độ sâu tức thời. Áp suất dư $p_{\mathrm g}=5{,}00\times10^3\,\mathrm{Pa}$ được giữ không đổi.

**Hướng đi:**

- Dùng Bernoulli giữa mặt thoáng và cửa thoát. Khí nén cung cấp thêm công áp suất, nên tốc độ thoát phụ thuộc cả áp suất dư lẫn độ sâu.
- Dùng bảo toàn thể tích $A\,dy/dt=-av$ để nối tốc độ thoát với tốc độ hạ mặt nước. Phải tích phân vì độ sâu thay đổi trong quá trình tháo.
- So sánh với cùng bồn có áp suất dư bằng không. Hai trường hợp có cùng hình học và cùng độ sâu đầu.

**Lời giải:** Đặt hai đại lượng phụ đã biết

$$
\begin{aligned}
\gamma&=\frac Aa=\left(\frac{2{,}00}{0{,}0200}\right)^2\\
&=10^4,
\end{aligned}
$$

$$
b=\frac{p_{\mathrm g}}{\rho g}\approx0{,}510\,\mathrm m.
$$

Vì tiết diện bồn lớn hơn tiết diện lỗ $10^4$ lần, tốc độ mặt nước rất nhỏ so với tốc độ thoát. Với xấp xỉ này, Bernoulli cho

$$
v=\sqrt{2g(y+b)}.
$$

(a) Ở thời điểm đầu,

$$
\begin{aligned}
v_i&=\sqrt{2g(H+b)}\\
&\approx5{,}07\,\mathrm{m/s}.
\end{aligned}
$$

Khi bồn hở, tốc độ đầu là $v_{i0}=\sqrt{2gH}\approx3{,}96\,\mathrm{m/s}$. Do đó,

$$
\frac{v_i}{v_{i0}}=\sqrt{1+\frac bH}\approx1{,}28.
$$

(b) Lưu lượng thoát ra làm thể tích trong bồn giảm:

$$
A\frac{dy}{dt}=-a\sqrt{2g(y+b)}.
$$

Tách biến rồi tích phân từ $y=H$ đến $y=0$:

$$
T=\frac{\gamma}{\sqrt{2g}}\int_0^H\frac{dy}{\sqrt{y+b}}.
$$

Nguyên hàm của $1/\sqrt{y+b}$ là $2\sqrt{y+b}$, nên

$$
T=\gamma\sqrt{\frac2g}\left(\sqrt{H+b}-\sqrt b\right).
$$

Thay số được $T\approx1{,}94\times10^3\,\mathrm s$, khoảng $32{,}4$ phút. Với bồn hở,

$$
T_0=\gamma\sqrt{\frac{2H}{g}}\approx4{,}04\times10^3\,\mathrm s.
$$

Tỉ số thời gian là

$$
\begin{aligned}
\frac{T}{T_0}&=\frac{\sqrt{H+b}-\sqrt b}{\sqrt H}\\
&\approx0{,}481.
\end{aligned}
$$

Khí nén làm thời gian tháo còn khoảng $48{,}1\%$ trường hợp bồn hở. Khi mức nước gần đáy, khí nén vẫn duy trì tốc độ thoát hữu hạn, còn dòng thoát của bồn hở chậm dần về không.

</details>

### 12.74 (••): Giữ một quả bóng nhựa ngập hoàn toàn

Một quả bóng nhựa bán kính $12{,}0\,\mathrm{cm}$ nổi trên nước với $24{,}0\%$ thể tích ngập nước. (a) Phải tác dụng lực nào để giữ bóng đứng yên và ngập hoàn toàn dưới mặt nước? (b) Khi buông bóng, gia tốc của bóng ngay lúc buông bằng bao nhiêu?

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Bóng có bán kính $r=0{,}120\,\mathrm m$. Khi nổi cân bằng, phần thể tích ngập chiếm tỉ lệ $f=0{,}240$. Xét ngay lúc bóng còn ngập hoàn toàn, bỏ qua lực cản trong mô hình lực đang dùng.

**Hướng đi:**

- Dùng cân bằng nổi để tìm khối lượng riêng trung bình của bóng từ phần thể tích ngập. Không lấy khối lượng riêng của vật liệu nhựa thay cho khối lượng riêng trung bình của cả bóng.
- Khi ngập hoàn toàn, lực đẩy ứng với toàn bộ thể tích bóng. Hiệu giữa lực đẩy và trọng lượng cho lực cần giữ.
- Ngay khi buông, lực tay biến mất nhưng lực đẩy và trọng lực vẫn còn. Dùng định luật II Newton để tìm gia tốc tức thời.

**Lời giải:** Gọi $V$ là thể tích bóng. Ở trạng thái nổi đầu,

$$
mg=f\rho_wVg.
$$

Vì vậy, khối lượng riêng trung bình của bóng là $\rho_b=f\rho_w=240\,\mathrm{kg/m^3}$. Thể tích và khối lượng bóng lần lượt là

$$
\begin{aligned}
V&=\frac43\pi r^3\\
&\approx7{,}24\times10^{-3}\,\mathrm{m^3},
\end{aligned}
$$

$$
m=\rho_bV\approx1{,}74\,\mathrm{kg}.
$$

(a) Khi bóng ngập hoàn toàn, lực đẩy lớn hơn trọng lượng. Tay phải ép xuống với độ lớn

$$
\begin{aligned}
F&=\rho_wVg-mg\\
&=(1-f)\rho_wVg\\
&\approx53{,}9\,\mathrm N.
\end{aligned}
$$

(b) Ngay khi buông, hợp lực hướng lên có độ lớn bằng $F$ vừa tìm. Gia tốc hướng lên là

$$
\begin{aligned}
a&=\frac{F}{m}=\left(\frac1f-1\right)g\\
&\approx31{,}0\,\mathrm{m/s^2}.
\end{aligned}
$$

Gia tốc có thể lớn hơn $g$ vì bóng không chỉ chịu trọng lực. Khi bóng bắt đầu nhô khỏi nước, thể tích ngập giảm và lực đẩy không còn bằng giá trị lúc ngập hoàn toàn.

</details>

### 12.75 (•••): Khối lập phương nổi giữa hai chất lỏng

Một khối lập phương cạnh $L$, khối lượng riêng $\rho_B$, nổi trong chất lỏng có khối lượng riêng lớn hơn là $\rho_L$.

(a) Phần thể tích khối nằm trên mặt chất lỏng bằng bao nhiêu phần thể tích toàn khối?

(b) Chất lỏng này đặc hơn nước, có khối lượng riêng $\rho_W$, và không hòa trộn với nước. Đổ nước lên trên, cần lớp nước sâu bao nhiêu để mặt nước vừa ngang mặt trên của khối? Biểu diễn theo $L$, $\rho_B$, $\rho_L$, $\rho_W$.

(c) Tìm độ sâu ấy nếu chất lỏng là thủy ngân, khối bằng sắt và $L=10{,}0\,\mathrm{cm}$.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Khối đứng thẳng, có thể tích $L^3$. Hai chất lỏng phân tầng, nước ở trên. Gọi $h$ là chiều dày lớp nước khi mặt nước vừa tới mặt trên của khối.

**Hướng đi:**

- Dùng cân bằng giữa trọng lượng và lực đẩy để tìm phần thể tích ngập trong một chất lỏng.
- Ở phần (b), khối chiếm chỗ cả nước lẫn chất lỏng dưới. Phải cộng hai lực đẩy với hai khối lượng riêng tương ứng.
- Kiểm tra nghiệm $0\le h\le L$ vì chiều cao phần khối nằm trong mỗi chất lỏng phải không âm.

**Lời giải:** (a) Gọi thể tích ngập ban đầu là $V_s$. Cân bằng cho

$$
\rho_LV_sg=\rho_BL^3g.
$$

Phần thể tích ở trên mặt là

$$
\frac{V_{\mathrm{trên}}}{L^3}=1-\frac{\rho_B}{\rho_L}.
$$

(b) Khi mặt nước vừa ngang mặt trên, phần khối nằm trong nước cao $h$, phần nằm trong chất lỏng dưới cao $L-h$. Hai lực đẩy lần lượt là

$$
\begin{aligned}
&B_W=\rho_WL^2hg,\\
&B_L=\rho_LL^2(L-h)g.
\end{aligned}
$$

Phương trình lực là

$$
B_W+B_L=\rho_BL^3g.
$$

Chia cho $L^2g$ rồi thu gọn:

$$
(\rho_L-\rho_W)h=(\rho_L-\rho_B)L.
$$

Suy ra

$$
h=L\frac{\rho_L-\rho_B}{\rho_L-\rho_W}.
$$

Trạng thái yêu cầu tồn tại với $\rho_W\le\rho_B<\rho_L$. Nếu khối nhẹ hơn cả nước, nó vẫn nổi một phần trên mặt nước nên không đạt trạng thái mô tả chỉ bằng cách đổ thêm nước.

(c) Dùng $\rho_L=13600$, $\rho_B=7800$ và $\rho_W=1000\,\mathrm{kg/m^3}$:

$$
\begin{aligned}
h&=(0{,}100)\frac{13600-7800}{13600-1000}\,\mathrm m\\
&\approx0{,}0460\,\mathrm m\\
&=4{,}60\,\mathrm{cm}.
\end{aligned}
$$

</details>

### 12.76 (••): Chuyển sắt vụn từ bờ xuống sà lan rồi xuống nước

Một sà lan nổi trong âu tàu hình chữ nhật dài $60{,}0\,\mathrm m$, rộng $20{,}0\,\mathrm m$ trên sông nước ngọt. Cửa thép ở hai đầu âu đều đóng. Một lô sắt vụn trọng lượng $2{,}50\times10^6\,\mathrm N$, khối lượng riêng $7200\,\mathrm{kg/m^3}$, ban đầu nằm trên bờ.

(a) Khi đưa toàn bộ lô sắt lên sà lan, mặt nước trong âu dâng bao nhiêu?

(b) Sau đó đẩy sắt từ sà lan xuống nước. Mặt nước dâng, hạ hay giữ nguyên? Nếu thay đổi, độ thay đổi theo phương đứng bằng bao nhiêu?

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Diện tích mặt bằng âu là $A=1200\,\mathrm{m^2}$. Trọng lượng lô sắt là $W=2{,}50\times10^6\,\mathrm N$. Mọi so sánh giữ nguyên lượng nước trong âu.

**Hướng đi:**

- Khi sắt ở trên sà lan nổi, sà lan phải chiếm chỗ thêm lượng nước có trọng lượng bằng $W$.
- Khi sắt chìm xuống đáy, nó chỉ chiếm chỗ thể tích bằng thể tích thật của sắt. Không còn dùng thể tích nước có trọng lượng bằng $W$ cho chính lô sắt ấy.
- Lấy chênh lệch thể tích chiếm chỗ chia cho diện tích mặt bằng âu. Phải chỉ rõ trạng thái dùng làm mốc ở từng phần.

**Lời giải:** (a) Thể tích nước bị chiếm chỗ thêm khi chất sắt lên sà lan là

$$
V_1=\frac{W}{\rho_wg}.
$$

Độ dâng của mặt nước bằng

$$
\begin{aligned}
\Delta h_a&=\frac{V_1}{A}=\frac{W}{\rho_wgA}\\
&\approx0{,}213\,\mathrm m.
\end{aligned}
$$

(b) Sắt chìm vì đặc hơn nước. Thể tích nó chiếm chỗ sau khi chìm là

$$
V_2=\frac{W}{\rho_mg}.
$$

Vì $\rho_m>\rho_w$, ta có $V_2<V_1$. Mặt nước hạ so với trạng thái sắt còn trên sà lan. Độ hạ là

$$
\begin{aligned}
\delta h&=\frac{V_1-V_2}{A}\\
&=\frac{W}{gA}\left(\frac1{\rho_w}-\frac1{\rho_m}\right)\\
&\approx0{,}183\,\mathrm m.
\end{aligned}
$$

Sau cả hai bước, mặt nước vẫn cao hơn lúc sắt còn trên bờ khoảng $0{,}0295\,\mathrm m$, đúng bằng $V_2/A$. Trọng lượng và thể tích chiếm chỗ của riêng sà lan khi không chở lô sắt không đổi giữa hai mốc đó.

</details>

### 12.77 (•, CP): Hai lỗ có cùng tầm phun

Nước sâu $H$ trong một bồn lớn, hở, có thành thẳng đứng. Đục một lỗ ở thành, sâu $h$ dưới mặt nước như Hình P12.77. (a) Tia nước chạm sàn cách chân thành bồn một đoạn $R$ bằng bao nhiêu? (b) Có thể đục lỗ thứ hai ở độ cao nào so với đáy để tia nước có cùng tầm phun?

![Hình P12.77: Tia nước thoát ngang ở độ sâu h dưới mặt thoáng rồi rơi xuống sàn dưới tác dụng trọng lực.](/vat-ly-1/bai-giang/img/young-12/r-exercises-fig-p12-77.png)

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Miệng lỗ cao $H-h$ so với sàn. Xét $0<h<H$ và bỏ qua sự hạ mặt thoáng trong khoảng quan sát.

**Hướng đi:**

- Dùng Torricelli để tìm tốc độ thoát ngang theo độ sâu lỗ.
- Sau khi nước ra khỏi lỗ, dùng chuyển động ném ngang. Thời gian rơi phụ thuộc độ cao lỗ so với sàn, không phải độ sâu dưới mặt thoáng.
- Tìm tính đối xứng của biểu thức tầm xa theo hai độ dài $h$ và $H-h$.

**Lời giải:** (a) Tốc độ thoát và thời gian rơi lần lượt là

$$
\begin{aligned}
&v=\sqrt{2gh},\\
&t=\sqrt{\frac{2(H-h)}g}.
\end{aligned}
$$

Do đó,

$$
R=vt=2\sqrt{h(H-h)}.
$$

(b) Đổi vai trò của $h$ và $H-h$ không làm tích dưới căn thay đổi. Lỗ thứ hai có độ sâu $H-h$ dưới mặt thoáng, tức cao $h$ so với đáy.

Hai lỗ đối xứng qua độ cao giữa bồn cho cùng tầm phun. Nếu lỗ đầu nằm đúng giữa chiều cao thì lỗ đối xứng trùng nó, không có lỗ thứ hai ở độ cao khác cho cùng tầm xa cực đại ấy.

</details>

### 12.78 (••): Nước rò vào khoang bếp của thuyền

Bác của bạn đang ở khoang bếp dưới boong thuyền, còn bạn đang săn cá bằng giáo ở gần đó. Một mũi giáo đi chệch tạo lỗ nhỏ trên vỏ thuyền và nước bắt đầu tràn vào. (a) Nếu lỗ nằm $0{,}900\,\mathrm m$ dưới mặt nước và có diện tích $1{,}20\,\mathrm{cm^2}$, cần bao lâu để $10{,}0\,\mathrm L$ nước vào thuyền? (b) Có cần xét việc thuyền chìm thấp hơn khi nước rò vào không?

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** $h=0{,}900\,\mathrm m$, $a=1{,}20\times10^{-4}\,\mathrm{m^2}$ và $V=0{,}0100\,\mathrm{m^3}$. Trong phép tính đầu, lấy không khí trong khoang ở khí áp và nước trong khoang chưa dâng tới lỗ.

**Hướng đi:**

- Chênh áp ngoài và trong lỗ là $\rho gh$, nên dùng Bernoulli để tìm tốc độ vào qua lỗ.
- Dùng $Q=av$ rồi $t=V/Q$ khi độ sâu lỗ gần như không đổi.
- Với phần (b), kiểm điều kiện của xấp xỉ độ sâu không đổi thay vì tự gán kích thước thuyền chưa được cung cấp.

**Lời giải:** (a) Tốc độ nước qua lỗ là

$$
v=\sqrt{2gh}=4{,}20\,\mathrm{m/s}.
$$

Lưu lượng tương ứng bằng

$$
Q=av=5{,}04\times10^{-4}\,\mathrm{m^3/s}.
$$

Thời gian là

$$
t=\frac{V}{Q}\approx19{,}8\,\mathrm s.
$$

(b) Về nguyên tắc, nước vào làm thuyền nặng hơn và chìm thêm, khiến lỗ sâu hơn nên nước vào nhanh hơn. Nếu $10{,}0\,\mathrm L$ làm thuyền hạ một đoạn rất nhỏ so với $0{,}900\,\mathrm m$, có thể bỏ qua thay đổi ấy trong kết quả gần đúng ở phần (a).

Để hiệu chỉnh bằng số, cần biết diện tích mặt cắt của thân thuyền tại đường nước và mức nước trong khoang. Đề không cho các dữ kiện này, nên kết quả tính được là xấp xỉ với độ sâu lỗ giữ nguyên, không phải một thời gian chính xác cho mọi thân thuyền.

</details>

### 12.79 (••, CP): Thu nhỏ miệng vòi nước

Bạn giữ một ống nước ở ngang thắt lưng và phun nước theo phương ngang. Miệng vòi đường kính $1{,}80\,\mathrm{cm}$ làm tia nước chạm đất cách vòi $0{,}950\,\mathrm m$ theo phương ngang. Nếu thu nhỏ miệng vòi còn đường kính $0{,}750\,\mathrm{cm}$, tia nước đi được bao xa theo phương ngang trước khi chạm đất? Bỏ qua sức cản không khí.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Vòi giữ nguyên độ cao, $d_1=1{,}80\,\mathrm{cm}$, $d_2=0{,}750\,\mathrm{cm}$ và $R_1=0{,}950\,\mathrm m$. Tính theo mô hình lưu lượng nước cấp được giữ như cũ khi thay đổi miệng vòi.

**Hướng đi:**

- Hai tia phun ngang từ cùng độ cao có cùng thời gian rơi, nên tỉ số tầm xa bằng tỉ số tốc độ phun.
- Nếu lưu lượng không đổi, phương trình liên tục cho tốc độ tỉ lệ nghịch tiết diện miệng vòi. Tiết diện tròn tỉ lệ bình phương đường kính.

**Lời giải:** Với cùng thời gian bay,

$$
\frac{R_2}{R_1}=\frac{v_2}{v_1}=\left(\frac{d_1}{d_2}\right)^2.
$$

Do đó,

$$
\begin{aligned}
R_2&=R_1\left(\frac{1{,}80}{0{,}750}\right)^2\\
&\approx5{,}47\,\mathrm m.
\end{aligned}
$$

Kết quả này dùng giả thiết lưu lượng giữ nguyên. Nếu nguồn cấp được đặc trưng bằng áp suất cố định và lưu lượng thay đổi khi thắt vòi, cần thêm mô hình đường ống để xác định tốc độ mới.

</details>

### 12.80 (•••): Mực nước ổn định trong xô có lỗ đáy

Một xô trụ hở cao $25{,}0\,\mathrm{cm}$, đường kính $10{,}0\,\mathrm{cm}$, có lỗ tròn diện tích $1{,}50\,\mathrm{cm^2}$ ở giữa đáy. Nước được đưa từ ống phía trên vào xô với lưu lượng $2{,}40\times10^{-4}\,\mathrm{m^3/s}$. Nước trong xô sẽ dâng tới độ cao nào?

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** $Q_i=2{,}40\times10^{-4}\,\mathrm{m^3/s}$, diện tích lỗ $a=1{,}50\times10^{-4}\,\mathrm{m^2}$ và chiều cao miệng xô $0{,}250\,\mathrm m$.

**Hướng đi:**

- Ở mực nước ổn định, lưu lượng vào bằng lưu lượng ra. Nếu chưa bằng nhau, thể tích nước trong xô còn thay đổi.
- Dùng tốc độ thoát $v=\sqrt{2gh}$ để viết lưu lượng ra theo độ sâu $h$.
- Kiểm tra độ sâu tìm được thấp hơn miệng xô. Nếu không, xô sẽ tràn và không đạt mực cân bằng trong lòng xô theo mô hình này.

**Lời giải:** Cân bằng lưu lượng cho

$$
Q_i=a\sqrt{2gh}.
$$

Suy ra

$$
h=\frac1{2g}\left(\frac{Q_i}{a}\right)^2\approx0{,}131\,\mathrm m.
$$

Mực nước ổn định cao khoảng $13{,}1\,\mathrm{cm}$, thấp hơn miệng xô $25{,}0\,\mathrm{cm}$. Đường kính xô ảnh hưởng tốc độ mực nước thay đổi theo thời gian, nhưng không xuất hiện trong điều kiện lưu lượng vào bằng lưu lượng ra.

Trạng thái này ổn định: Nếu mực nước tăng một chút, lưu lượng ra tăng và làm mức nước hạ trở lại. Nếu mực nước giảm, lưu lượng ra nhỏ hơn lưu lượng vào nên mức nước tăng trở lại.

</details>

### 12.81 (•): Lưu lượng và áp suất trong ống thoát nước

Nước chảy đều từ bồn hở như Hình P12.81. Điểm 1 cao $10{,}0\,\mathrm m$, còn các điểm 2 và 3 cao $2{,}00\,\mathrm m$. Tiết diện ống tại điểm 2 là $0{,}0480\,\mathrm{m^2}$, tại điểm 3 là $0{,}0160\,\mathrm{m^2}$. Tiết diện bồn rất lớn so với tiết diện ống. Giả sử phương trình Bernoulli áp dụng được, tính (a) lưu lượng thoát theo mét khối mỗi giây và (b) áp suất dư tại điểm 2.

![Hình P12.81: Nước từ bồn lớn đi qua hai đoạn ống ở cùng cao độ rồi thoát ra không khí tại điểm 3.](/vat-ly-1/bai-giang/img/young-12/r-exercises-fig-p12-81.png)

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Mặt thoáng và cửa thoát cùng chịu khí áp. Lấy $v_1\approx0$, $y_1-y_3=8{,}00\,\mathrm m$ và $y_2=y_3$.

**Hướng đi:**

- Dùng Bernoulli từ mặt thoáng tới cửa thoát để tìm $v_3$, vì biết áp suất ở cả hai điểm.
- Dùng $Q=A_3v_3=A_2v_2$ để tìm lưu lượng và tốc độ ở điểm 2.
- Dùng Bernoulli giữa 2 và 3 ở cùng cao độ. Vì cửa thoát hở, áp suất dư ở điểm 3 bằng không.

**Lời giải:** (a) Tốc độ ở cửa thoát là

$$
\begin{aligned}
v_3&=\sqrt{2g(y_1-y_3)}\\
&\approx12{,}5\,\mathrm{m/s}.
\end{aligned}
$$

Do đó,

$$
Q=A_3v_3\approx0{,}200\,\mathrm{m^3/s}.
$$

(b) Vì $A_2=3A_3$, tốc độ ở điểm 2 bằng

$$
v_2=\frac{v_3}{3}\approx4{,}17\,\mathrm{m/s}.
$$

Áp suất dư ở điểm 2 là

$$
\begin{aligned}
p_{2\mathrm g}&=\frac\rho2(v_3^2-v_2^2)\\
&\approx6{,}97\times10^4\,\mathrm{Pa}.
\end{aligned}
$$

Tiết diện ở điểm 2 lớn hơn nên tốc độ nhỏ hơn và áp suất cao hơn tại cửa thoát cùng cao độ.

</details>

### 12.82 (••, CP): Tốc độ gió và chênh áp trong bão Emily

Năm 1993, bão Emily có bán kính khoảng $350\,\mathrm{km}$. Tốc độ gió gần mắt bão, bán kính khoảng $30\,\mathrm{km}$, đạt khoảng $200\,\mathrm{km/h}$. Khi không khí xoáy từ rìa vào gần mắt bão, mômen động lượng của nó gần như được bảo toàn. Ước lượng:

(a) Tốc độ gió ở rìa bão.

(b) Chênh lệch áp suất tại mặt đất giữa mắt và rìa. Nơi nào có áp suất lớn hơn? Gợi ý: Dùng Bảng 12.1.

(c) Nếu toàn bộ động năng xoáy của không khí gần mắt chuyển thành thế năng trọng trường, không khí lên cao bao nhiêu?

(d) Thực tế không khí ở vùng mắt bão có thể được nâng lên cao vài kilômét. Giải thích sự khác biệt với kết quả phần (c).

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** $r_e=30\,\mathrm{km}$, $r_R=350\,\mathrm{km}$, $v_e=200\,\mathrm{km/h}$. Dùng khối lượng riêng không khí $\rho=1{,}20\,\mathrm{kg/m^3}$ theo mô hình ước lượng.

**Hướng đi:**

- Dùng bảo toàn mômen động lượng $mrv$ cho một phần không khí để liên hệ hai tốc độ.
- Với xấp xỉ dòng lý tưởng ở cùng cao độ, dùng Bernoulli để ước lượng chênh áp từ chênh lệch bình phương tốc độ.
- Phần (c) chỉ cho phép chuyển động năng đầu thành thế năng, nên dùng $v_e^2/2=gh$.
- Phần (d) cần xét nguồn năng lượng mà phép giả định trong (c) chưa kể, đặc biệt công của các lực áp suất lên khối khí.

**Lời giải:** (a) Từ $r_Rv_R=r_ev_e$,

$$
\begin{aligned}
v_R&=\frac{30}{350}(200)\\
&\approx17{,}1\,\mathrm{km/h}.
\end{aligned}
$$

(b) Đổi đơn vị được $v_e\approx55{,}6\,\mathrm{m/s}$ và $v_R\approx4{,}76\,\mathrm{m/s}$. Bernoulli cho

$$
\begin{aligned}
p_R-p_e&=\frac\rho2(v_e^2-v_R^2)\\
&\approx1{,}84\times10^3\,\mathrm{Pa}.
\end{aligned}
$$

Áp suất ở rìa lớn hơn ở mắt bão. Đây là ước lượng trong mô hình đã nêu, không phải một mô tả đầy đủ mọi biến đổi khối lượng riêng và vận tốc trong bão thực.

(c) Độ cao theo giả định chuyển toàn bộ động năng là

$$
h=\frac{v_e^2}{2g}\approx157\,\mathrm m.
$$

(d) Giới hạn $157\,\mathrm m$ chỉ đúng nếu nguồn năng lượng nâng khối khí là phần động năng xoáy ban đầu được xét. Không khí thực còn nhận công từ lực áp suất và trao đổi năng lượng với các vùng khí khác. Vì vậy, phần tăng thế năng không bị giới hạn bởi riêng động năng ấy.

</details>

### 12.83 (••): Hút chất lỏng lên ống nối với chỗ thắt

Hai bồn lớn A và F hở, chứa cùng một chất lỏng như Hình P12.83. Một ống ngang BCD dẫn từ đáy bồn A ra không khí ở D và có chỗ thắt C. Một ống đứng E mở vào chỗ thắt C, đầu dưới nhúng trong chất lỏng ở bồn F.

Giả sử dòng chảy theo đường dòng và bỏ qua độ nhớt. Tiết diện tại C bằng một nửa tại D, còn D thấp hơn mặt chất lỏng trong A một đoạn $h_1$. Chất lỏng dâng trong E tới độ cao $h_2$ bằng bao nhiêu so với mặt chất lỏng trong F? Biểu diễn theo $h_1$.

![Hình P12.83: Chỗ thắt C có áp suất thấp, làm chất lỏng từ bồn F dâng trong ống đứng E.](/vat-ly-1/bai-giang/img/young-12/r-exercises-fig-p12-83.png)

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Hai bồn cùng chịu khí áp, tốc độ mặt thoáng có thể bỏ qua. Cho $A_C=A_D/2$. Xét cột chất lỏng dâng trong ống E dưới tác dụng chênh áp.

**Hướng đi:**

- Dùng Bernoulli từ mặt thoáng A tới D để tìm tốc độ thoát theo $h_1$.
- Dùng phương trình liên tục giữa C và D, rồi Bernoulli ở cùng cao độ để tính áp suất tại C.
- Đổi phần áp suất thiếu so với khí quyển thành chiều cao cột chất lỏng trong E bằng quan hệ thủy tĩnh.

**Lời giải:** Tốc độ tại D thỏa

$$
v_D^2=2gh_1.
$$

Tiết diện tại C nhỏ hơn hai lần nên $v_C=2v_D$. Vì hai điểm cùng cao độ,

$$
\begin{aligned}
p_{\mathrm{atm}}-p_C&=\frac\rho2(v_C^2-v_D^2)\\
&=\frac32\rho v_D^2\\
&=3\rho gh_1.
\end{aligned}
$$

Chênh áp ấy giữ được cột chất lỏng cao $h_2$ so với mặt bồn F:

$$
\rho gh_2=p_{\mathrm{atm}}-p_C.
$$

Vì vậy,

$$
h_2=3h_1.
$$

Kết quả mô tả cột chất lỏng liên tục trong ống E trước khi có dòng bổ sung đáng kể từ F trộn vào dòng chính. Áp suất tuyệt đối tính ở C phải nằm trong phạm vi duy trì được cột chất lỏng của mô hình.

</details>

### 12.84 (•): Hình dạng dòng chất lỏng rơi thẳng đứng

Chất lỏng thoát từ một ống thẳng đứng và tạo thành một dòng có hình dạng xác định. Coi chất lỏng rơi tự do sau khi rời ống. Ngay tại miệng ống, tốc độ là $v_0$ và bán kính dòng là $r_0$.

(a) Tìm tốc độ theo quãng đường rơi $y$. Kết hợp với phương trình liên tục để tìm bán kính dòng theo $y$.

(b) Nếu tốc độ thoát của nước là $1{,}20\,\mathrm{m/s}$, bán kính dòng giảm còn một nửa bán kính ban đầu ở vị trí thấp hơn miệng ống bao nhiêu?

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Chọn $y\ge0$ hướng xuống từ miệng ống. Dòng không nén được, có lưu lượng không đổi và chuyển động rơi tự do trong mô hình đã cho.

**Hướng đi:**

- Dùng động học gia tốc không đổi để liên hệ tốc độ với quãng đường rơi, vì gia tốc có độ lớn $g$ hướng xuống.
- Dùng $\pi r^2v=\pi r_0^2v_0$ để liên hệ bán kính và tốc độ. Bán kính không tỉ lệ nghịch trực tiếp với tốc độ, vì tiết diện phụ thuộc bình phương bán kính.

**Lời giải:** (a) Động học rơi tự do cho

$$
v(y)=\sqrt{v_0^2+2gy}.
$$

Từ bảo toàn lưu lượng,

$$
\frac{r}{r_0}=\sqrt{\frac{v_0}{v}}.
$$

Thay biểu thức tốc độ:

$$
r(y)=r_0\left(1+\frac{2gy}{v_0^2}\right)^{-1/4}.
$$

(b) Nếu $r=r_0/2$, tiết diện giảm bốn lần nên tốc độ tăng bốn lần. Do đó,

$$
v=4v_0.
$$

Thay vào $v^2=v_0^2+2gy$, ta được

$$
y=\frac{15v_0^2}{2g}\approx1{,}10\,\mathrm m.
$$

Dòng hẹp dần khi rơi vì tốc độ tăng, còn thể tích đi qua mỗi giây vẫn giữ nguyên.

</details>

### 12.85 (••, DATA): Khối lượng nguyên tử và khối lượng riêng

Các giá trị khối lượng riêng trong Bảng 12.1 được xếp tăng dần. Một sinh viên hóa học nhận thấy bốn nguyên tố hóa học đầu tiên xuất hiện trong bảng cũng được xếp theo khối lượng nguyên tử tăng dần.

(a) Hãy kiểm tra khả năng có một quan hệ đơn giản bằng cách vẽ khối lượng riêng, tính theo $\mathrm{g/cm^3}$, theo khối lượng mol nguyên tử của cả tám nguyên tố trong bảng. Dùng các khối lượng mol tính theo gam trên mol.

(b) Có thể vẽ một đường thẳng hoặc đường cong đơn giản qua các điểm để tìm một quan hệ đơn giản như vậy không?

(c) Giải thích vì sao phát biểu “Nguyên tử nặng hơn tạo ra vật rắn có khối lượng riêng lớn hơn” chưa nói đầy đủ bản chất.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Xét tám nguyên tố Al, Fe, Cu, Ag, Pb, Hg, Au và Pt. Trục ngang biểu diễn khối lượng mol nguyên tử $M$, trục đứng biểu diễn khối lượng riêng $\rho$ của vật liệu.

**Hướng đi:**

- Đổi khối lượng riêng trong Bảng 12.1 từ $\mathrm{kg/m^3}$ sang $\mathrm{g/cm^3}$ rồi ghép từng giá trị với đúng nguyên tố.
- Vẽ các điểm thay vì tự áp đặt trước một đường thẳng. Kiểm tra đặc biệt những nguyên tố có khối lượng mol gần nhau nhưng khối lượng riêng khác rõ rệt.
- Dùng $\rho=M/V_m$, với $V_m$ là thể tích một mol, để thấy khối lượng nguyên tử chưa quyết định thể tích vật liệu mà các nguyên tử ấy chiếm chỗ.

**Lời giải:** (a) Các dữ liệu cần vẽ là

| Nguyên tố | $M$ (g/mol) | $\rho$ (g/cm³) |
| --- | ---: | ---: |
| Al | $26{,}982$ | $2{,}7$ |
| Fe | $55{,}845$ | $7{,}8$ |
| Cu | $63{,}546$ | $8{,}9$ |
| Ag | $107{,}868$ | $10{,}5$ |
| Pb | $207{,}2$ | $11{,}3$ |
| Hg | $200{,}59$ | $13{,}6$ |
| Au | $196{,}967$ | $19{,}3$ |
| Pt | $195{,}078$ | $21{,}4$ |

![Đồ thị khối lượng riêng theo khối lượng mol nguyên tử của tám nguyên tố. Các điểm được ghi đúng ký hiệu hóa học.](/vat-ly-1/bai-giang/img/young-12/solution-p12-85-density.svg)

(b) Bốn điểm đầu tăng cùng nhau, nhưng xu hướng ấy không tiếp tục cho cả tám nguyên tố. Pt có khối lượng mol nhỏ hơn Au, Hg và Pb, trong khi khối lượng riêng lại lớn hơn cả ba.

Những dữ liệu này không cho một đường thẳng chung, cũng không cho một quy luật đơn điệu đơn giản để dự đoán khối lượng riêng chỉ từ khối lượng nguyên tử. Vẽ một đa thức đi qua hữu hạn điểm không tự biến nó thành một định luật vật lý có khả năng tiên đoán.

(c) Khối lượng riêng là khối lượng trên một đơn vị thể tích. Với một mol vật liệu,

$$
\rho=\frac{M}{V_m}.
$$

Khối lượng nguyên tử lớn hơn làm tử số tăng, nhưng kích thước nguyên tử, khoảng cách giữa các nguyên tử và cách sắp xếp của chúng còn ảnh hưởng mẫu số. Hai vật liệu không nhất thiết có cùng thể tích trên mỗi nguyên tử.

Bảng cũng chứa thủy ngân ở trạng thái lỏng trong điều kiện thông thường, nên một phát biểu chỉ nói về vật rắn chưa bao quát toàn bộ dữ liệu. Muốn giải thích khối lượng riêng phải xét cả khối lượng lẫn cấu trúc và trạng thái của vật liệu.

</details>

### 12.86 (••, DATA): Dùng đồng xu để đo khối lượng riêng chất lỏng

Bạn có một xô chứa chất lỏng chưa biết khối lượng riêng và một khối gỗ lập phương cạnh $8{,}0\,\mathrm{cm}$, chưa biết khối lượng hoặc khối lượng riêng. Đặt khối gỗ nổi trong chất lỏng rồi đo chiều cao $h$ của mặt trên so với mặt chất lỏng. Sau đó xếp thêm những số lượng đồng quarter đôla Mỹ khác nhau lên khối và đo lại $h$.

Đường thẳng khớp tốt nhất với các số đo được biểu diễn trong Hình P12.86. Hãy tra khối lượng một đồng quarter lưu thông, tương ứng các đồng phát hành năm 2012. Dùng khối lượng ấy cùng độ dốc và tung độ gốc của đường thẳng để tính (a) khối lượng riêng chất lỏng theo $\mathrm{kg/m^3}$ và (b) khối lượng khối gỗ theo kilôgam.

![Hình P12.86: Chiều cao mặt trên khối gỗ so với mặt thoáng giảm tuyến tính khi số đồng quarter xếp trên khối tăng.](/vat-ly-1/bai-giang/img/young-12/r-exercises-fig-p12-86.png)

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Cạnh khối $L=0{,}080\,\mathrm m$, khối lượng gỗ $m_b$ và khối lượng riêng chất lỏng $\rho$ chưa biết. Gọi $N$ là số đồng xu, mỗi đồng có khối lượng $m_c$. Đường khớp có dạng $h=h_0+sN$.

**Hướng đi:**

- Viết cân bằng nổi cho cả gỗ và các đồng xu. Phần thể tích gỗ ngập là $L^2(L-h)$, còn khối lượng cần đỡ là $m_b+Nm_c$.
- Đưa phương trình về dạng tuyến tính theo $N$ để xác định ý nghĩa của độ dốc và tung độ gốc.
- Các giá trị đọc từ hình có độ chính xác hữu hạn. Kết quả suy ra cũng cần ghi gần đúng, không coi tọa độ đồ thị là số đo chính xác tùy ý.

**Lời giải:** Đồng quarter lưu thông có khối lượng chuẩn $5{,}67\,\mathrm g$, tức $m_c=0{,}00567\,\mathrm{kg}$. Có thể kiểm thông số tại [U.S. Mint](https://www.usmint.gov/learn/coins-and-medals/circulating-coins/coin-specifications).

Khối gỗ và đồng xu nổi cân bằng nên

$$
\rho L^2(L-h)=m_b+Nm_c.
$$

Ở đây, thừa số chung $g$ đã được khử khỏi cân bằng lực. Chia tiếp cho $\rho L^2$ rồi giải theo $h$:

$$
h=L-\frac{m_b}{\rho L^2}-\frac{m_c}{\rho L^2}N.
$$

So sánh với đường thẳng $h=h_0+sN$:

$$
\begin{aligned}
&h_0=L-\frac{m_b}{\rho L^2},\\
&s=-\frac{m_c}{\rho L^2}.
\end{aligned}
$$

Đọc đường khớp được xấp xỉ $h_0=3{,}0\,\mathrm{cm}$ và $h=1{,}2\,\mathrm{cm}$ tại $N=25$. Vì vậy, độ dốc khoảng $-0{,}072\,\mathrm{cm}$ trên mỗi đồng xu, tức $s\approx-7{,}2\times10^{-4}\,\mathrm m$ trên mỗi đồng.

(a) Khối lượng riêng chất lỏng bằng

$$
\begin{aligned}
\rho&=-\frac{m_c}{sL^2}\\
&\approx1{,}23\times10^3\,\mathrm{kg/m^3}.
\end{aligned}
$$

(b) Khối lượng gỗ được xác định từ tung độ gốc:

$$
\begin{aligned}
m_b&=\rho L^2(L-h_0)\\
&\approx0{,}394\,\mathrm{kg}.
\end{aligned}
$$

Với độ chính xác của việc đọc đồ thị, có thể nêu kết quả là khoảng $1{,}2\times10^3\,\mathrm{kg/m^3}$ và $0{,}39\,\mathrm{kg}$. Trong khoảng số đo đã vẽ, mặt trên khối và các đồng xu vẫn ở trên mặt thoáng nên không cần cộng lực đẩy đáng kể lên đồng xu.

</details>

### 12.87 (•••, DATA): Xác định chất lỏng trong bồn kín

Cơ quan Bảo vệ Môi trường đang khảo sát một nhà máy hóa chất bị bỏ hoang. Một bồn trụ kín lớn chứa chất lỏng chưa biết. Cần xác định khối lượng riêng chất lỏng và độ cao $h$ từ đáy bồn tới mặt chất lỏng.

Dùng khí nén để tạo các áp suất dư khác nhau trên mặt chất lỏng. Đục một lỗ nhỏ ở chân thành bồn. Bồn đặt trên bệ bê tông nên lỗ cao $50{,}0\,\mathrm{cm}$ so với mặt đất. Tia chất lỏng thoát ngang đi được quãng đường $R$ trước khi chạm đất, với số đo sau:

| Áp suất dư (atm) | $R$ (m) |
| ---: | ---: |
| $0{,}50$ | $5{,}4$ |
| $1{,}00$ | $6{,}5$ |
| $2{,}00$ | $8{,}2$ |
| $3{,}00$ | $9{,}7$ |
| $4{,}00$ | $10{,}9$ |

(a) Vẽ $R^2$ theo áp suất dư $p_{\mathrm g}$. Giải thích vì sao các điểm gần nằm trên một đường thẳng. Tìm độ dốc và tung độ gốc của đường thẳng đó.

(b) Từ hai hệ số đường thẳng, tính $h$ theo mét và khối lượng riêng theo $\mathrm{kg/m^3}$. Dùng $g=9{,}80\,\mathrm{m/s^2}$. Bỏ qua độ nhớt và coi lỗ đủ nhỏ để mức chất lỏng thay đổi rất ít trong lúc đo.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Gọi $a=0{,}500\,\mathrm m$ là độ cao lỗ so với đất, $h$ là độ sâu lỗ dưới mặt chất lỏng. Mặt thoáng có áp suất dư $p_{\mathrm g}$, còn cửa thoát chịu khí áp.

**Hướng đi:**

- Dùng Bernoulli để liên hệ tốc độ thoát với áp suất dư và độ sâu chất lỏng.
- Dùng ném ngang để liên hệ tốc độ ấy với tầm xa. Thời gian rơi giống nhau cho các lần đo vì độ cao lỗ không đổi.
- Khớp $R^2$ theo áp suất, rồi đổi độ dốc về đơn vị SI trước khi suy ra khối lượng riêng.

**Lời giải:** (a) Hai phương trình động lực học và động học là

$$
v^2=2\left(\frac{p_{\mathrm g}}\rho+gh\right),
$$

$$
t^2=\frac{2a}{g}.
$$

Vì $R=vt$,

$$
R^2=4ah+\frac{4a}{\rho g}p_{\mathrm g}.
$$

Đây là quan hệ tuyến tính khi giữ $a$, $h$, $\rho$ không đổi. Dùng bình phương tối thiểu cho năm cặp dữ liệu được đường khớp $R^2=Sp_{\mathrm g}+B$ với

$$
S\approx25{,}6787\,\mathrm{m^2/atm},
$$

$$
B\approx16{,}3848\,\mathrm{m^2}.
$$

![Đồ thị năm giá trị R bình phương theo áp suất dư và đường thẳng khớp bình phương tối thiểu. Hệ số khớp được hiển thị kèm đơn vị.](/vat-ly-1/bai-giang/img/young-12/solution-p12-87-fit.svg)

(b) Tung độ gốc cho độ sâu:

$$
h=\frac{B}{4a}\approx8{,}19\,\mathrm m.
$$

Với $1\,\mathrm{atm}=1{,}013\times10^5\,\mathrm{Pa}$ ở độ chính xác đang dùng, độ dốc tính trên mỗi pascal là

$$
s\approx2{,}535\times10^{-4}\,\mathrm{m^2/Pa}.
$$

So sánh với hệ số của $p_{\mathrm g}$ trong phương trình lý thuyết:

$$
\rho=\frac{4a}{gs}\approx805\,\mathrm{kg/m^3}.
$$

Các số đo tầm xa chỉ có độ chính xác hữu hạn, nên $h\approx8{,}2\,\mathrm m$ và $\rho\approx8{,}1\times10^2\,\mathrm{kg/m^3}$ là cách nêu kết quả phù hợp. Không dùng độ dốc tính theo atm trực tiếp trong biểu thức SI mà bỏ phép đổi đơn vị.

</details>

### 12.88 (•••): Giới hạn độ cao của ống xi-phông

Ống xi-phông trong Hình P12.88 dùng để lấy chất lỏng khỏi một bình chứa. Để khởi đầu dòng chảy, ống phải được điền đầy chất lỏng. Chất lỏng có khối lượng riêng $\rho$, khí áp là $p_{\mathrm{atm}}$ và tiết diện ống bằng nhau ở mọi vị trí.

(a) Nếu đầu ra thấp hơn mặt chất lỏng trong bình một đoạn $h$, tốc độ chất lỏng thoát ra bằng bao nhiêu? Coi bình có đường kính rất lớn và bỏ qua độ nhớt.

(b) Chất lỏng ban đầu đi lên dốc trong ống. Đỉnh ống có thể cao nhất bao nhiêu, tính theo độ cao $H$ trên mặt chất lỏng, để dòng vẫn tồn tại?

![Hình P12.88: Xi-phông đã được điền đầy chất lỏng, có đầu ra thấp hơn mặt thoáng một đoạn h và đỉnh ống cao hơn mặt thoáng một đoạn H.](/vat-ly-1/bai-giang/img/young-12/r-exercises-fig-p12-88.png)

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Lấy mặt thoáng làm mốc cao độ. Tại mặt thoáng và đầu ra, áp suất bằng khí áp. Tốc độ mặt thoáng bỏ qua được, còn tốc độ trong ống có cùng độ lớn ở mọi tiết diện.

**Hướng đi:**

- Dùng Bernoulli từ mặt thoáng tới đầu ra để tìm tốc độ. Chênh cao đầu ra quyết định tốc độ thoát trong mô hình này.
- Dùng Bernoulli từ mặt thoáng tới đỉnh ống để tìm áp suất thấp nhất.
- Áp suất tuyệt đối không thể giảm tùy ý. Giới hạn lý tưởng đạt khi áp suất tính tại đỉnh chạm không, còn chất lỏng thật có thể đứt cột trước giới hạn hình thức ấy.

**Lời giải:** (a) Bernoulli giữa mặt thoáng và đầu ra cho

$$
\frac12\rho v^2=\rho gh.
$$

Vì vậy,

$$
v=\sqrt{2gh}.
$$

(b) Gọi áp suất ở đỉnh là $p_C$. Đỉnh cao hơn mặt thoáng $H$ và chất lỏng tại đó có tốc độ $v$, nên

$$
p_C=p_{\mathrm{atm}}-\rho gH-\frac12\rho v^2.
$$

Thay $v^2=2gh$:

$$
p_C=p_{\mathrm{atm}}-\rho g(H+h).
$$

Điều kiện $p_C\ge0$ dẫn đến

$$
H\le\frac{p_{\mathrm{atm}}}{\rho g}-h.
$$

Giới hạn độ cao trong mô hình lý tưởng là

$$
H_{\max}=\frac{p_{\mathrm{atm}}}{\rho g}-h.
$$

Muốn đỉnh nằm trên mặt thoáng còn cần vế phải không âm. Đầu ra càng thấp làm tốc độ trong ống càng lớn, nên phần áp suất dành để duy trì cột chất lỏng lên đỉnh càng nhỏ. Với chất lỏng thực, sự tạo hơi hoặc khí trong ống có thể làm dòng ngừng trước giới hạn áp suất tuyệt đối bằng không.

</details>

## Đọc hiểu khoa học: Áp suất khi voi dùng vòi để thở dưới nước

Một con voi có thể bơi hoặc đi khi vùng ngực nằm dưới mặt nước vài mét, còn đầu vòi vẫn ở trên mặt nước và đóng vai trò như ống thở. Mô cơ thể chịu áp suất tăng do nước xung quanh, trong khi phổi thông với không khí qua vòi nên được mô hình hóa ở khí áp.

Hình minh họa cho áp suất dư trong phổi và vùng bụng ở một độ sâu cụ thể. Cơ hoành ngăn phổi với bụng phải chịu chênh lệch hai áp suất ấy. Trong tình huống đang xét, cơ hoành dày khoảng $3{,}0\,\mathrm{cm}$ và đường kính $120\,\mathrm{cm}$.

![Áp suất dư trong phổi bằng 0 mmHg, còn trong vùng bụng bằng 150 mmHg khi phần ngực voi ngập dưới mặt nước. Cơ hoành ngăn hai vùng chịu chênh lệch áp suất.](/vat-ly-1/bai-giang/img/young-12/r-exercises-mcat-elephant.png)

Tài liệu tham khảo cho tình huống: John B. West, “Why Doesn’t the Elephant Have a Pleural Space?”, *Physiology*, tập 17, tr. 47–50, ngày 01/04/2002.

### 12.89 Độ sâu tương ứng với áp suất dư

Ở tình huống trong hình, mô vùng bụng voi có áp suất dư $150\,\mathrm{mmHg}$. Áp suất này ứng với độ sâu nào dưới mặt một hồ nước ngọt?

(a) $1{,}5\,\mathrm m$.

(b) $2{,}0\,\mathrm m$.

(c) $3{,}0\,\mathrm m$.

(d) $15\,\mathrm m$.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** $p_{\mathrm g}=150\,\mathrm{mmHg}$, $\rho_w=1000\,\mathrm{kg/m^3}$. Dùng gần đúng $1\,\mathrm{mmHg}\approx133{,}3\,\mathrm{Pa}$.

**Hướng đi:**

- Đổi áp suất về pascal trước khi dùng các đại lượng SI.
- Dùng $p_{\mathrm g}=\rho_wgh$ vì mặt nước ở khí áp và nước gần như không nén được trong độ sâu này.

**Lời giải:** Áp suất dư gần bằng $2{,}00\times10^4\,\mathrm{Pa}$. Do đó,

$$
h=\frac{p_{\mathrm g}}{\rho_wg}\approx2{,}04\,\mathrm m.
$$

Chọn (b), $2{,}0\,\mathrm m$.

</details>

### 12.90 Chênh áp cực đại trên cơ hoành

Cơ của cơ hoành có thể tạo lực cực đại $24000\,\mathrm N$. Chênh lệch áp suất lớn nhất mà cơ hoành chịu được trong mô hình của bài đọc bằng bao nhiêu?

(a) $160\,\mathrm{mmHg}$.

(b) $760\,\mathrm{mmHg}$.

(c) $920\,\mathrm{mmHg}$.

(d) $5000\,\mathrm{mmHg}$.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** $F_{\max}=24000\,\mathrm N$, đường kính vùng chịu áp suất $D=1{,}20\,\mathrm m$. Coi vùng này là hình tròn có áp suất chênh lệch phân bố đều.

**Hướng đi:**

- Dùng $F=\Delta pA$ vì lực do chênh áp được tính bằng chênh áp nhân diện tích chịu lực.
- Tính diện tích từ bán kính $D/2$, không lấy đường kính làm bán kính. Độ dày cơ hoành không xuất hiện trong phép đổi giữa lực cực đại đã cho và chênh áp.

**Lời giải:** Diện tích chịu lực là

$$
A=\frac{\pi D^2}{4}\approx1{,}13\,\mathrm{m^2}.
$$

Chênh áp cực đại bằng

$$
\begin{aligned}
\Delta p_{\max}&=\frac{F_{\max}}A\\
&\approx2{,}12\times10^4\,\mathrm{Pa}\\
&\approx159\,\mathrm{mmHg}.
\end{aligned}
$$

Chọn (a), $160\,\mathrm{mmHg}$.

</details>

### 12.91 Lực trên cơ hoành thay đổi theo độ sâu

Lực trên cơ hoành do chênh áp giữa phổi và bụng phụ thuộc thế nào vào độ sâu của vùng bụng dưới mặt nước?

(a) Tăng tuyến tính theo độ sâu.

(b) Tăng theo bình phương độ sâu.

(c) Tăng theo lập phương độ sâu.

(d) Tăng theo hàm mũ của độ sâu.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Áp suất phổi được giữ ở khí áp trong mô hình ống thở. Áp suất dư vùng bụng tăng theo độ sâu, còn diện tích cơ hoành được coi không đổi.

**Hướng đi:**

- Kết hợp chênh áp thủy tĩnh $\Delta p=\rho_wgh$ với lực $F=\Delta pA$.
- Giữ rõ các đại lượng được coi không đổi để xác định đúng quan hệ tỉ lệ với độ sâu.

**Lời giải:**

$$
F=\rho_wgAh.
$$

Vì $\rho_w$, $g$ và $A$ không đổi, lực tăng tuyến tính với $h$. Chọn (a).

</details>

### 12.92 Đổi từ nước ngọt sang nước mặn

Nếu voi dùng vòi thở trong nước mặn, vốn đặc hơn nước ngọt, độ sâu cực đại có khác trường hợp nước ngọt không?

(a) Có, độ sâu tăng vì áp suất ở cùng độ sâu nhỏ hơn trong nước mặn.

(b) Có, độ sâu giảm vì áp suất ở cùng độ sâu lớn hơn trong nước mặn.

(c) Không, chênh áp bên trong phần voi ngập chỉ phụ thuộc khối lượng riêng không khí, không phụ thuộc khối lượng riêng nước.

(d) Không, vì lực đẩy lên voi như nhau trong hai trường hợp.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Coi giới hạn lực cơ hoành và diện tích chịu áp suất không đổi. Khối lượng riêng nước mặn lớn hơn nước ngọt.

**Hướng đi:**

- Dùng cùng giới hạn lực $F_{\max}=\rho gAh_{\max}$ để so sánh hai môi trường.
- Phân biệt giới hạn chênh áp qua cơ hoành với lực nổi của toàn cơ thể. Lực nổi không thay thế phương trình áp suất tại độ sâu đang xét.

**Lời giải:** Độ sâu cực đại thỏa

$$
h_{\max}=\frac{F_{\max}}{\rho gA}.
$$

Khối lượng riêng tăng làm độ sâu cực đại giảm. Tại cùng một độ sâu, nước mặn tạo chênh áp lớn hơn qua cơ hoành trong mô hình của bài. Chọn (b).

</details>
