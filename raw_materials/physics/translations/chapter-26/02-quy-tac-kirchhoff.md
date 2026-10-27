## 26.2. Các quy tắc Kirchhoff

Nhiều mạng điện thực tế không thể rút gọn thành các nhóm nối tiếp và song song đơn giản. Hình 26.6a mô tả một bộ nguồn một chiều có suất điện động $\mathcal E_1$ nạp cho pin có suất điện động nhỏ hơn $\mathcal E_2$, đồng thời cấp dòng cho bóng đèn có điện trở $R$. Hình 26.6b là một mạch cầu, được dùng trong nhiều hệ thống đo lường và điều khiển. Để phân tích những mạng như vậy, ta dùng hai quy tắc do nhà vật lý người Đức Gustav Robert Kirchhoff (1824–1887) phát triển.

Trước hết, cần phân biệt hai khái niệm. **Nút mạch** là điểm nơi ba hay nhiều dây dẫn gặp nhau. **Vòng kín** là một đường dẫn điện khép kín. Trong Hình 26.6a, $a$ và $b$ là nút mạch, còn $c$ và $d$ không phải. Trong Hình 26.6b, $a$, $b$, $c$ và $d$ là nút mạch, còn $e$ và $f$ không phải. Các đường màu xanh trong hình chỉ một vài vòng kín có thể chọn.

![Hình 26.6: Hai mạng điện không thể rút gọn bằng cách mắc nối tiếp và song song](../img/young-26/hinh-26-06.png)

**Hình 26.6:** Sơ đồ (a) gồm hai nguồn có suất điện động $\mathcal E_1$, $\mathcal E_2$ và các điện trở trong $r_1$, $r_2$, cùng điện trở $R$. Sơ đồ (b) là mạch cầu gồm năm điện trở. Một nút là nơi có ít nhất ba dây dẫn gặp nhau. Một vòng kín là đường đi khép kín như các đường màu xanh được vẽ trong hai mạch.

Hai quy tắc Kirchhoff được phát biểu như sau.

**Quy tắc nút mạch:** Tổng đại số các dòng điện đi vào một nút bằng không:

$$
\sum_{j=1}^{m}\widetilde I_j=0.
\tag{26.5}
$$

Chỉ số j chạy qua m nhánh nối với nút. $\widetilde I_j$ là dòng đã gán dấu, dương khi đi vào nút và âm khi đi ra. Với ba nhánh, nếu $I_1$ và $I_2$ đi vào còn $I_3$ đi ra:

$$
\begin{aligned}
&\widetilde I_1+\widetilde I_2+\widetilde I_3 = 0, \\
&I_1+I_2-I_3 = 0, \\
&I_1+I_2 = I_3.
\end{aligned}
$$

Tổng dòng đi vào bằng tổng dòng đi ra. Quy tắc này áp dụng tại mọi nút.

**Quy tắc vòng kín:** Tổng đại số các độ biến thiên điện thế khi đi quanh một vòng kín bằng không:

$$
\sum_{j=1}^{k}\Delta V_j=0.
\tag{26.6}
$$

Chỉ số j chạy qua k phần tử của vòng. $\Delta V_j$ là tăng hoặc giảm điện thế theo chiều đi vòng đã chọn. Trong tổng này phải tính mọi phần tử, kể cả nguồn điện và điện trở.

Chẳng hạn, với ba đoạn mạch, cách viết khai triển là:

$$
\Delta V_1+\Delta V_2+\Delta V_3=0.
$$

Dấu của từng số hạng được xác định theo chiều ta đi quanh vòng.

### Vì sao hai quy tắc đúng?

Quy tắc nút mạch bắt nguồn từ bảo toàn điện tích. Điện tích không thể tích tụ tại nút. Vì dòng điện là lượng điện tích đi qua trong một đơn vị thời gian, tổng dòng đi vào nút phải bằng tổng dòng đi ra. Hình 26.7a minh họa quan hệ này. Có thể hình dung như chỗ nối ống nước ở Hình 26.7b: Nếu hai ống đưa tổng cộng $1\,\mathrm{L/min}$ nước vào nút, ống còn lại không thể đưa $3\,\mathrm{L/min}$ nước ra.

![Hình 26.7: Quy tắc nút mạch và phép tương tự với dòng nước](../img/young-26/hinh-26-07.png)

**Hình 26.7:** (a) Dòng điện rời khỏi nút bằng dòng điện đi vào nút. (b) Lưu lượng nước đi ra tại nhánh ống bằng tổng lưu lượng đi vào.

Quy tắc vòng kín nói rằng lực tĩnh điện là lực thế. Khi đi quanh một vòng và cộng các hiệu điện thế liên tiếp, ta trở về đúng điểm xuất phát. Tổng độ biến thiên điện thế phải bằng không, nếu không điện thế tại điểm ấy sẽ không có một giá trị xác định.

### Quy ước dấu khi áp dụng quy tắc vòng kín

Trước khi lập phương trình, ta giả định chiều dòng điện ở mỗi nhánh và đánh dấu lên sơ đồ. Sau đó, chọn một chiều đi quanh vòng kín. Chiều đi này có thể cùng hoặc ngược với chiều dòng điện đã giả định. Khi đi qua nguồn điện từ cực âm sang cực dương, độ biến thiên điện thế là $+\mathcal E$. Khi đi từ cực dương sang cực âm, độ biến thiên là $-\mathcal E$.

Khi đi qua điện trở theo chiều dòng điện giả định, điện thế giảm, nên ghi $-IR$. Khi đi ngược chiều dòng điện giả định, điện thế tăng, nên ghi $+IR$.

![Hình 26.8: Quy ước dấu của suất điện động và điện trở](../img/young-26/hinh-26-08.png)

**Hình 26.8:** (a) Đi qua nguồn theo chiều từ cực âm đến cực dương thì ghi $+\mathcal E$, còn đi từ cực dương đến cực âm thì ghi $-\mathcal E$. (b) Đi qua điện trở cùng chiều dòng điện giả định thì ghi $-IR$, còn đi ngược chiều dòng điện thì ghi $+IR$. “Chiều đi” là chiều ta chọn để lần theo vòng, không nhất thiết trùng với chiều dòng điện.

Hai quy tắc Kirchhoff đủ để giải nhiều mạng điện. Thường ta biết một số suất điện động, dòng điện và điện trở, còn các đại lượng khác cần tìm. Ta lập đủ số phương trình độc lập bằng số ẩn rồi giải đồng thời. Khó nhất thường là theo dõi dấu đại số chính xác.

::: warning Dòng điện không nhất thiết chia đều tại nút
Khi dòng điện trong dây phân nhánh, dòng ở các nhánh thường không bằng nhau. Dòng điện lớn hơn đi qua nhánh có điện trở nhỏ hơn.
:::

### Chiến lược giải bài toán 26.2: Các quy tắc Kirchhoff

#### Nhận diện khái niệm

Các quy tắc Kirchhoff dùng để phân tích mọi mạch điện.

#### Bố trí bài giải

1. Vẽ sơ đồ mạch và chừa chỗ để ghi các đại lượng đã biết lẫn chưa biết. Đánh dấu chiều giả định của từng dòng điện chưa biết và cực tính giả định của mỗi suất điện động chưa biết. Quy tắc Kirchhoff sẽ cho độ lớn và chiều thực. Nếu chiều thực ngược chiều đã chọn, kết quả đại số mang dấu âm.
2. Khi ghi dòng điện, có thể dùng quy tắc nút như trong Hình 26.9 để biểu diễn các dòng qua ít ẩn nhất có thể.
3. Xác định các đại lượng cần tìm.

![Hình 26.9: Dùng quy tắc nút để giảm số ẩn dòng điện](../img/young-26/hinh-26-09.png)

**Hình 26.9:** Phần (a) có ba dòng điện chưa biết $I_1$, $I_2$, $I_3$. Phần (b) áp dụng quy tắc nút tại $a$ để biểu diễn nhánh thứ ba bằng tổng hoặc hiệu của hai dòng còn lại, nhờ đó giảm số ẩn độc lập.

#### Thực hiện

1. Chọn một vòng trong mạng và chọn chiều đi quanh vòng, theo chiều kim đồng hồ hoặc ngược chiều kim đồng hồ. Chiều đi không cần trùng với chiều dòng điện giả định.
2. Đi lần lượt quanh vòng, cộng đại số các hiệu điện thế khi đi qua từng phần tử. Dùng quy ước dấu ở Hình 26.8.
3. Đặt tổng ở bước 2 bằng không theo quy tắc vòng kín.
4. Nếu cần thêm phương trình độc lập, chọn vòng khác và lặp lại các bước trên. Tiếp tục đến khi có số phương trình độc lập bằng số ẩn hoặc mọi phần tử mạch đã xuất hiện trong ít nhất một vòng.
5. Giải đồng thời hệ phương trình để tìm các đại lượng chưa biết.
6. Có thể dùng cùng quy ước dấu để tìm điện thế $V_{ab}$ của điểm $a$ so với điểm $b$. Bắt đầu tại $b$, cộng các độ tăng và giảm điện thế khi đi đến $a$. Tổng đại số thu được là $V_{ab}=V_a-V_b$.

#### Đánh giá

Kiểm tra các phép biến đổi đại số. Sau đó áp dụng quy tắc vòng kín cho một vòng chưa dùng. Nếu tổng đại số các độ biến thiên điện thế không bằng không, có sai sót trong lời giải.

### Ví dụ 26.3. Mạch một vòng

Mạch ở Hình 26.10a có hai pin, mỗi pin có suất điện động và điện trở trong, cùng hai điện trở ngoài. Tìm (a) dòng điện trong mạch, (b) hiệu điện thế $V_{ab}$ và (c) công suất của suất điện động mỗi pin.

![Hình 26.10: Mạch khởi động xe bằng pin](../img/young-26/hinh-26-10.png)

**Hình 26.10:** Mạch (a) gồm hai nguồn $12\,\mathrm V$ và $4\,\mathrm V$, các điện trở $2\,\Omega$, $3\,\Omega$, $4\,\Omega$ và $7\,\Omega$. Chiều dòng điện giả định ngược chiều kim đồng hồ. Hình (b) cho thấy tình huống thực tế tương tự khi dùng pin xe đang hoạt động để khởi động xe có pin yếu.

#### Nhận diện và bố trí

Mạch chỉ có một vòng và không có nút phân nhánh, nên không cần dùng quy tắc nút. Ta giả định dòng điện chạy ngược chiều kim đồng hồ như Hình 26.10a rồi áp dụng quy tắc vòng kín.

#### Thực hiện

**(a) Tìm dòng điện.** Bắt đầu tại $a$ và đi ngược chiều kim đồng hồ, cùng chiều dòng điện giả định. Tổng độ tăng thế do hai pin bằng tổng độ giảm thế trên bốn điện trở:

Gọi hai tổng điện trở trên nhánh dưới và nhánh trên lần lượt là:

$$
\begin{aligned}
&R_A=4\,\Omega+7\,\Omega=11\,\Omega,\\
&R_B=2\,\Omega+3\,\Omega=5\,\Omega.
\end{aligned}
$$

Trên chiều đi đã chọn, bốn điện trở đều làm giảm điện thế. Pin $4\,\mathrm V$ cũng làm giảm điện thế, còn pin $12\,\mathrm V$ làm tăng điện thế. Quy tắc vòng cho:

$$
12\,\mathrm V-4\,\mathrm V=I(R_A+R_B).
$$

Thu gọn các hạng tử:

$$
8\,\mathrm V = I(16\,\Omega) \implies I = 0{,}5\,\mathrm A.
$$

Dòng điện tìm được dương, vì vậy chiều dòng điện thực đúng với chiều đã giả định.

**(b) Tìm $V_{ab}$.** Để tìm điện thế tại $a$ so với $b$, bắt đầu ở $b$ rồi cộng các độ biến thiên điện thế trên đường đi đến $a$. Theo nhánh dưới:

$$
\begin{aligned}
V_{ab}&=IR_A+4\,\mathrm V\\
&=(0{,}5\,\mathrm A)(11\,\Omega)+4\,\mathrm V\\
&=9{,}5\,\mathrm V.
\end{aligned}
$$

Vậy điện thế tại $a$ cao hơn tại $b$ $9{,}5\,\mathrm V$. Mọi số hạng đều dương vì trên đường đi từ $b$ đến $a$, mỗi số hạng biểu thị một độ tăng điện thế. Đi theo nhánh trên cũng cho

$$
\begin{aligned}
V_{ab}&=12\,\mathrm V-IR_B\\
&=12\,\mathrm V-(0{,}5\,\mathrm A)(5\,\Omega)\\
&=9{,}5\,\mathrm V.
\end{aligned}
$$

Trên nhánh trên, hai số hạng $IR$ âm vì ta đi cùng chiều dòng điện, qua các điện trở có điện thế giảm. Hai đường cho cùng $V_{ab}$, đúng như yêu cầu của quy tắc vòng kín.

**(c) Công suất của hai suất điện động.** Quy ước dấu của suất điện động cho công suất:

$$
\begin{aligned}
P_{12\,\mathrm V} &= (12\,\mathrm V)(0{,}5\,\mathrm A) \\
&= 6\,\mathrm W, \\
P_{4\,\mathrm V} &= (-4\,\mathrm V)(0{,}5\,\mathrm A) \\
&= -2\,\mathrm W.
\end{aligned}
$$

Dấu âm của suất điện động $4\,\mathrm V$ cho biết dòng thực đi qua pin từ phía có điện thế cao sang phía có điện thế thấp. Công suất âm biểu thị pin đang tích trữ năng lượng. Pin $12\,\mathrm V$ nạp cho pin $4\,\mathrm V$ nếu pin sau có thể nạp lại. Nếu không, pin đó bị phá hủy.

#### Đánh giá

Tổng công suất tỏa nhiệt ở bốn điện trở, tính theo $P=I^2R$, là

$$
\begin{aligned}
P_R&=I^2(R_A+R_B)\\
&=(0{,}5\,\mathrm A)^2(16\,\Omega)\\
&=4\,\mathrm W.
\end{aligned}
$$

Trong $6\,\mathrm W$ do suất điện động $12\,\mathrm V$ cung cấp, có $2\,\mathrm W$ được tích trữ trong pin $4\,\mathrm V$ và $4\,\mathrm W$ tỏa nhiệt ở các điện trở. Mạch tương tự mạch dùng pin còn đầy của một xe đang chạy để khởi động xe có pin yếu. Điện trở $3\,\Omega$ và $7\,\Omega$ trong mô hình đại diện cho điện trở dây câu và đường dẫn điện qua xe có pin yếu. Trong ô tô thật, điện trở này nhỏ hơn nhiều và suất điện động của pin yếu thường không thấp hơn $12\,\mathrm V$ quá nhiều.

#### Ý chính

Trong mọi vòng kín, tổng các độ biến thiên điện thế bằng không. Nếu mạch chỉ có một vòng, dòng điện có cùng độ lớn tại mọi vị trí trong mạch.

### Ví dụ 26.4. Nạp pin

Trong Hình 26.11, bộ nguồn $12\,\mathrm V$ có điện trở trong chưa biết $r$, được nối với một pin sạc đang yếu có suất điện động chưa biết $\mathcal E$ và điện trở trong $1\,\Omega$, cùng một bóng đèn báo có điện trở $3\,\Omega$. Dòng qua bóng đèn là $2\,\mathrm A$. Dòng qua pin yếu là $1\,\mathrm A$ theo chiều đã vẽ. Tìm $r$, $\mathcal E$ và dòng điện $I$ qua bộ nguồn.

![Hình 26.11: Bộ nguồn nạp pin yếu và làm sáng bóng đèn](../img/young-26/hinh-26-11.png)

**Hình 26.11:** Bộ nguồn $12\,\mathrm V$ có điện trở trong $r$ nối với pin yếu có suất điện động $\mathcal E$, điện trở trong $1\,\Omega$ và bóng đèn $3\,\Omega$. Các chiều dòng điện, cực tính và ba vòng (1), (2), (3) được giả định trên sơ đồ.

#### Nhận diện và bố trí

Mạch có nhiều vòng và nút phân nhánh, nên cần dùng cả quy tắc nút lẫn quy tắc vòng. Ta giả định chiều dòng điện qua bộ nguồn $12\,\mathrm V$ và cực tính của pin yếu như trên Hình 26.11. Có ba ẩn, nên cần ba phương trình độc lập.

#### Thực hiện

Áp dụng quy tắc nút tại $a$:

$$
\begin{aligned}
I&=1\,\mathrm A+2\,\mathrm A\\
&=3\,\mathrm A.
\end{aligned}
$$

Áp dụng quy tắc vòng kín cho vòng ngoài (1):

Gọi $V_L$ là điện áp hai đầu bóng đèn:

$$
V_L=(2\,\mathrm A)(3\,\Omega)=6\,\mathrm V.
$$

Trên nhánh nguồn:

$$
12\,\mathrm V-(3\,\mathrm A)r=V_L.
$$

Suy ra:

$$
r=\frac{12\,\mathrm V-6\,\mathrm V}{3\,\mathrm A}=2\,\Omega.
$$

Áp dụng quy tắc vòng kín cho vòng bên trái (2):

Độ giảm thế trên điện trở trong pin yếu là:

$$
V_r=(1\,\mathrm A)(1\,\Omega)=1\,\mathrm V.
$$

Quy tắc vòng cho:

$$
-\mathcal E+V_r-V_L=0.
$$

Do đó:

$$
\mathcal E=1\,\mathrm V-6\,\mathrm V=-5\,\mathrm V.
$$

Suất điện động thực có cực tính ngược với giả định ở Hình 26.11. Pin đang được nạp như ở Ví dụ 26.3.

#### Đánh giá

Nếu dùng quy tắc nút tại $b$ hoặc đi theo chiều kim đồng hồ quanh vòng (1), ta vẫn tìm được cùng $I$ và $r$. Có thể kiểm tra $\mathcal E$ bằng vòng (3):

Điện trở trong nguồn làm giảm điện thế một lượng:

$$
V_s=(3\,\mathrm A)(2\,\Omega)=6\,\mathrm V.
$$

Vòng thứ ba cho:

$$
\begin{aligned}
12\,\mathrm V-V_s-V_r+\mathcal E&=0,\\
12\,\mathrm V-6\,\mathrm V-1\,\mathrm V+\mathcal E&=0.
\end{aligned}
$$

phương trình này cũng cho $\mathcal E=-5\,\mathrm V$.

Kiểm tra thêm hiệu điện thế $V_{ba}=V_b-V_a$. Trên điện trở $3\,\Omega$:

$$
V_{ba}=(2\,\mathrm A)(3\,\Omega)=6\,\mathrm V.
$$

Đi theo nhánh bên phải từ $a$ đến $b$:

$$
\begin{aligned}
V_{ba}&=12\,\mathrm V-V_s\\
&=12\,\mathrm V-6\,\mathrm V\\
&=6\,\mathrm V.
\end{aligned}
$$

Đi theo nhánh giữa:

$$
\begin{aligned}
V_{ba} &= -(-5\,\mathrm V)+(1\,\mathrm A)(1\,\Omega) \\
&= 6\,\mathrm V.
\end{aligned}
$$

Cả ba cách đều cho cùng một hiệu điện thế.

#### Ý chính

Trong mạch có nhiều vòng, quy tắc nút yêu cầu tổng đại số dòng điện đi vào một nút bằng không.

### Ví dụ 26.5. Công suất trong mạch nạp pin

Trong mạch ở Ví dụ 26.4 và Hình 26.11, tìm công suất do bộ nguồn $12\,\mathrm V$ cấp, công suất do pin đang nạp trao đổi và công suất tỏa nhiệt ở từng điện trở.

#### Nhận diện và bố trí

Công suất của suất điện động cấp cho mạch là $P=\mathcal EI$. Công suất truyền từ mạch sang điện trở là $P=V_{ab}I=I^2R$. Các đại lượng cần thiết đã biết từ Ví dụ 26.4.

#### Thực hiện

Công suất do suất điện động của bộ nguồn tạo ra là

$$
P_{\mathrm{source}}=(12\,\mathrm V)(3\,\mathrm A)=36\,\mathrm W.
$$

Điện trở trong $r$ của bộ nguồn tỏa nhiệt công suất

$$
P_{r,\mathrm{source}}=(3\,\mathrm A)^2(2\,\Omega)=18\,\mathrm W.
$$

Vì thế công suất thuần bộ nguồn cấp ra là $36\,\mathrm W-18\,\mathrm W=18\,\mathrm W$. Ta cũng có thể dùng điện áp hai đầu bộ nguồn $V_{ba}=6\,\mathrm V$:

$$
P_{\mathrm{net}}=(6\,\mathrm V)(3\,\mathrm A)=18\,\mathrm W.
$$

Công suất của suất điện động $\mathcal E$ trong pin đang được nạp là

$$
P_{\mathcal E}=(-5\,\mathrm V)(1\,\mathrm A)=-5\,\mathrm W.
$$

Dấu âm xuất hiện vì dòng điện $1\,\mathrm A$ đi qua pin từ phía điện thế cao sang phía điện thế thấp. Pin tích trữ năng lượng. Điện trở trong $1\,\Omega$ của pin tỏa nhiệt:

$$
P_{r,\mathrm{pin}}=(1\,\mathrm A)^2(1\,\Omega)=1\,\mathrm W.
$$

Do đó, tổng công suất nhận vào của pin là $1\,\mathrm W+|-5\,\mathrm W|=6\,\mathrm W$. Trong đó, $5\,\mathrm W$ làm tăng năng lượng lưu trữ của pin và $1\,\mathrm W$ tỏa nhiệt ở điện trở trong. Bóng đèn tỏa nhiệt công suất

$$
P_{\mathrm{lamp}}=(2\,\mathrm A)^2(3\,\Omega)=12\,\mathrm W.
$$

#### Đánh giá

Toàn bộ công suất thuần $18\,\mathrm W$ của bộ nguồn được phân bổ thành ba phần. Trong đó, $5\,\mathrm W$ được lưu trữ trong pin, $1\,\mathrm W$ tỏa ở điện trở trong pin và $12\,\mathrm W$ tỏa ở bóng đèn.

#### Ý chính

Trong mạch chỉ gồm nguồn và điện trở, tổng công suất các nguồn cấp ra bằng tổng công suất tỏa nhiệt ở các điện trở. Nếu mạch có pin đang được nạp, phần công suất điện còn lại làm tăng năng lượng lưu trữ của pin, như phép cân bằng ngay phía trên.

### Ví dụ 26.6. Mạng điện phức tạp

Hình 26.12 là mạch cầu, một dạng mạch đã nêu ở đầu mục. Tìm dòng điện qua mỗi điện trở và điện trở tương đương của mạng gồm năm điện trở.

![Hình 26.12: Mạng điện cầu gồm năm điện trở](../img/young-26/hinh-26-12.png)

**Hình 26.12:** Mạng điện có nguồn $13\,\mathrm V$, bốn điện trở $1\,\Omega$ và một điện trở $2\,\Omega$. Các dòng $I_1$, $I_2$, $I_3$ cùng chiều giả định và ba vòng (1), (2), (3) được đánh dấu trên sơ đồ.

#### Nhận diện và bố trí

Mạng này không phải tổ hợp nối tiếp hoặc song song đơn giản, nên cần dùng các quy tắc Kirchhoff. Có năm dòng chưa biết. Áp dụng quy tắc nút tại $a$ và $b$ cho phép biểu diễn chúng theo ba ẩn $I_1$, $I_2$, $I_3$ như hình.

#### Thực hiện

Áp dụng quy tắc vòng kín cho ba vòng được đánh dấu:

Vì mọi điện trở đều bằng $1\,\Omega$ hoặc $2\,\Omega$, chia từng phương trình vòng cho $1\,\Omega$. Các số hạng điện trở trở thành hệ số 1 hoặc 2, còn $13\,\mathrm V/(1\,\Omega)=13\,\mathrm A$:

$$
\begin{aligned}
&13\,\mathrm A=I_1+(I_1-I_3),\\
&13\,\mathrm A=I_2+2(I_2+I_3),\\
&-I_1-I_3+I_2=0.
\end{aligned}
$$

Từ phương trình thứ ba, $I_2=I_1+I_3$. Thay vào phương trình thứ hai, rồi thu gọn phương trình thứ nhất, ta được

$$
\begin{aligned}
13\,\mathrm V &= I_1(2\,\Omega) - I_3(1\,\Omega), \\
13\,\mathrm V &= I_1(3\,\Omega) + I_3(5\,\Omega).
\end{aligned}
$$

Nhân phương trình đầu với $5$ rồi cộng phương trình sau, ta khử được $I_3$:

$$
78\,\mathrm V = I_1(13\,\Omega) \implies I_1 = 6\,\mathrm A.
$$

Thay $I_1$ vào phương trình đầu thu gọn, ta được $I_3=-1\,\mathrm A$. Từ $I_2=I_1+I_3$, suy ra $I_2=5\,\mathrm A$. Dấu âm của $I_3$ cho biết dòng thực chạy ngược chiều giả định.

Các dòng qua năm điện trở lần lượt là $I_1=6\,\mathrm A$, $I_2=5\,\mathrm A$, $I_3=-1\,\mathrm A$, $I_1-I_3=7\,\mathrm A$ và $I_2+I_3=4\,\mathrm A$. Dòng tổng qua mạng là $I_1+I_2=11\,\mathrm A$. Hiệu điện thế hai đầu mạng bằng suất điện động $13\,\mathrm V$, nên

$$
R_{\mathrm{eq}}=\frac{13\,\mathrm V}{11\,\mathrm A}
=1{,}2\,\Omega.
$$

#### Đánh giá

Thay $I_1=6\,\mathrm A$, $I_2=5\,\mathrm A$ và $I_3=-1\,\mathrm A$ vào cả ba phương trình vòng sẽ thu lại đẳng thức. Cụ thể, vế tổng lần lượt bằng $13-6-7=0\,\mathrm V$, $-5-8+13=0\,\mathrm V$ và $-6-(-1)+5=0\,\mathrm V$. Điều này kiểm tra đồng thời dấu và chiều dòng điện.

#### Ý chính

Một số mạng điện có cấu trúc không rút gọn được thành nối tiếp hoặc song song. Ta phân tích các mạch đó bằng cả quy tắc nút lẫn quy tắc vòng kín.

### Kiểm tra hiểu mục 26.2

Lấy phương trình (1) trong Ví dụ 26.6 trừ khỏi phương trình (2). Phương trình thu được ứng với vòng nào trong Hình 26.12? Phương trình này có giúp lời giải Ví dụ 26.6 đơn giản hơn không?

::: details Lời giải kiểm tra hiểu
#### Tóm tắt

Cần trừ phương trình vòng (1) khỏi phương trình vòng (2), rồi xác định đường đi tương ứng trong Hình 26.12 và xem phương trình mới có độc lập hay không.

#### Hướng đi

Phép trừ và thu gọn các số hạng cho

Chia phương trình hiệu cho $1\,\Omega$ như khi lập hệ:

$$
\begin{aligned}
&I_1+I_1=2I_1,\\
&-I_2-2I_2=-3I_2,\\
&-2I_3-I_3=-3I_3.
\end{aligned}
$$

Gom các số hạng theo từng dòng điện cho:

$$
2I_1-3I_2-3I_3=0.
$$

Đây chính là phương trình thu được khi đi theo vòng $c\to b\to d\to a\to c$. Nó không độc lập với các phương trình đã lập, vì có thể tạo ra bằng cách trừ hai phương trình kia. Do đó, phương trình này không giúp giải Ví dụ 26.6.
:::

### Ví dụ 26.7. Hiệu điện thế trong mạng điện phức tạp

Trong mạch ở Ví dụ 26.6 và Hình 26.12, tìm hiệu điện thế $V_{ab}$.

#### Nhận diện và bố trí

Đại lượng cần tìm là $V_{ab}=V_a-V_b$, tức điện thế tại $a$ so với $b$. Bắt đầu tại $b$ rồi lần theo một đường bất kỳ đến $a$, cộng các độ tăng và giảm điện thế. Mọi đường nối hai điểm ấy phải cho cùng kết quả. Đây là cách kiểm tra lời giải.

#### Thực hiện

Đường ngắn nhất đi qua điện trở $1\,\Omega$ ở giữa mạng. Ví dụ 26.6 cho $I_3=-1\,\mathrm A$, nghĩa là dòng thực qua điện trở này chạy từ phải sang trái. Khi đi từ $b$ đến $a$, ta đi cùng chiều dòng thực nên điện thế giảm $1\,\mathrm V$:

$$
V_{ab} = -(1\,\mathrm A)(1\,\Omega) = -1\,\mathrm V.
$$

Điện thế tại $a$ thấp hơn tại $b$ $1\,\mathrm V$.

#### Đánh giá

Có thể kiểm tra bằng đường đi từ $b$ đến $a$ qua hai điện trở phía dưới. Dòng qua hai điện trở ấy lần lượt là

$$
\begin{aligned}
I_2+I_3&=5\,\mathrm A-1\,\mathrm A\\
&=4\,\mathrm A,\\
I_1-I_3&=6\,\mathrm A+1\,\mathrm A\\
&=7\,\mathrm A.
\end{aligned}
$$

Theo đường này,

Hai độ biến thiên điện thế trên đường dưới lần lượt là $-8\,\mathrm V$ và $+7\,\mathrm V$:

$$
\begin{aligned}
&\Delta V_1=-(4\,\mathrm A)(2\,\Omega)=-8\,\mathrm V,\\
&\Delta V_2=(7\,\mathrm A)(1\,\Omega)=7\,\mathrm V.
\end{aligned}
$$

Do đó:

$$
\begin{aligned}
V_{ab}&=\Delta V_1+\Delta V_2\\
&=-8\,\mathrm V+7\,\mathrm V\\
&=-1\,\mathrm V.
\end{aligned}
$$

Các đường khác từ $b$ đến $a$ cũng cho cùng kết quả.

#### Ý chính

Có thể phát biểu quy tắc vòng kín theo cách khác: Với bất kỳ đường đi nào trong mạch từ $a$ đến $b$, hiệu điện thế $V_{ab}$ đều như nhau.
