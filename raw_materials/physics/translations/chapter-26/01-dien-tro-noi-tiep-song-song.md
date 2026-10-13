## 26.1. Điện trở mắc nối tiếp và mắc song song

Điện trở có mặt trong nhiều mạch điện, từ máy sấy tóc, lò sưởi điện đến các mạch dùng để giới hạn hoặc phân chia dòng điện và giảm hoặc chia điện áp. Vì một mạch thường có nhiều điện trở, ta cần biết cách phân tích các tổ hợp của chúng. Chuỗi bóng đèn trang trí ngày lễ là một ví dụ đơn giản: Mỗi bóng hoạt động như một điện trở, nên nhìn từ góc độ phân tích mạch, cả chuỗi là một tổ hợp điện trở.

Hình 26.1 minh họa bốn cách mắc ba điện trở $R_1$, $R_2$ và $R_3$ giữa hai điểm $a$ và $b$. Khi các phần tử mạch được nối liên tiếp và chỉ có một đường dòng điện giữa hai điểm, chúng mắc **nối tiếp**. Khi mỗi điện trở tạo thành một đường riêng nối cùng hai điểm, chúng mắc **song song**. Hình 26.1c là tổ hợp trong đó $R_2$ và $R_3$ song song rồi nối tiếp với $R_1$. Ở Hình 26.1d, $R_2$ và $R_3$ nối tiếp rồi mắc song song với $R_1$.

![Hình 26.1: Bốn cách mắc ba điện trở giữa hai điểm](../img/young-26/hinh-26-01.png)

**Hình 26.1:** Bốn cách mắc ba điện trở. (a) $R_1$, $R_2$ và $R_3$ nối tiếp. (b) Cả ba điện trở song song. (c) $R_1$ nối tiếp với tổ hợp song song của $R_2$ và $R_3$. (d) $R_1$ song song với tổ hợp nối tiếp của $R_2$ và $R_3$.

Với bất kỳ tổ hợp điện trở nào, ta có thể thay cả tổ hợp bằng một điện trở duy nhất sao cho dòng điện tổng và hiệu điện thế hai đầu vẫn như cũ. Điện trở duy nhất ấy gọi là **điện trở tương đương** $R_{\mathrm{eq}}$. Nếu mạng điện nằm giữa hai đầu $a$ và $b$, có hiệu điện thế $V_{ab}$ và dòng điện tổng $I$, thì

$$
\begin{aligned}
&V_{ab} = IR_{\mathrm{eq}},\\
&R_{\mathrm{eq}} = \frac{V_{ab}}{I}.
\end{aligned}
$$

Để tìm $R_{\mathrm{eq}}$, ta đặt hiệu điện thế $V_{ab}$ lên mạng điện thật, tính dòng điện tương ứng $I$, rồi lấy tỉ số $V_{ab}/I$.

### Điện trở mắc nối tiếp

Trong Hình 26.1a, dòng điện $I$ như nhau qua cả ba điện trở. Định luật Ôm cho từng điện trở:

$$
\begin{aligned}
&V_{ax} = IR_1,\\
&V_{xy} = IR_2,\\
&V_{yb} = IR_3.
\end{aligned}
$$

Hiệu điện thế trên từng điện trở không nhất thiết bằng nhau, trừ trường hợp đặc biệt các điện trở bằng nhau. Hiệu điện thế giữa hai đầu toàn bộ tổ hợp bằng tổng các độ giảm thế thành phần:

$$
\begin{aligned}
&V_{ab} = V_{ax}+V_{xy}+V_{yb}\\
&\quad =IR_1+IR_2+IR_3\\
&\quad =I(R_1+R_2+R_3).
\end{aligned}
$$

Chia hai vế cho dòng điện chung $I$ và dùng định nghĩa điện trở tương đương, ta được

$$
\begin{aligned}
&R_{\mathrm{eq}} = R_1+R_2\\
&\quad+R_3.
\end{aligned}
\tag{26.1}
$$

Với nhiều điện trở nối tiếp, tổng quát hóa bằng cách cộng lần lượt các điện trở:

$$
R_{\mathrm{eq}}=R_1+R_2+R_3+\cdots.
$$

Vì các điện trở đều dương, điện trở tương đương của một tổ hợp nối tiếp lớn hơn từng điện trở thành phần. Trong dây bóng đèn nối tiếp, chẳng hạn, thêm bóng làm tăng điện trở tương đương của chuỗi.

![Hình 26.2: Đèn pha và đèn hậu ô tô mắc song song](../img/young-26/hinh-26-02.png)

**Hình 26.2:** Đèn pha và đèn hậu ô tô mắc song song. Mỗi đèn nhận toàn bộ hiệu điện thế của hệ thống điện trên xe nên đạt độ sáng thiết kế. Nếu một đèn hỏng, các đèn còn lại vẫn sáng (xem Ví dụ 26.2).

::: warning Điện trở và tụ điện mắc nối tiếp
Không nên nhầm quy tắc mắc nối tiếp của điện trở với quy tắc mắc nối tiếp của tụ điện. Điện trở mắc nối tiếp cộng trực tiếp theo (26.1), vì hiệu điện thế trên mỗi điện trở tỉ lệ thuận với điện trở của nó khi cùng một dòng điện chạy qua. Tụ điện mắc nối tiếp cộng nghịch đảo theo (24.5), vì hiệu điện thế trên mỗi tụ tỉ lệ nghịch với điện dung khi điện tích trên chúng bằng nhau.
:::

### Điện trở mắc song song

Trong Hình 26.1b, dòng điện qua mỗi điện trở có thể khác nhau. Tuy nhiên, hai đầu của từng điện trở được nối vào cùng hai điểm $a$ và $b$, nên hiệu điện thế trên mỗi điện trở đều bằng $V_{ab}$. Kết luận này không phụ thuộc đường đi giữa hai điểm.

Gọi các dòng điện qua ba điện trở lần lượt là $I_1$, $I_2$ và $I_3$. Từ định luật Ôm:

$$
\begin{aligned}
&I_1 = \frac{V_{ab}}{R_1},\\
&I_2 = \frac{V_{ab}}{R_2},\\
&I_3 = \frac{V_{ab}}{R_3}.
\end{aligned}
$$

Điện tích không tích tụ tại điểm $a$ cũng không biến mất khỏi đó. Bởi vậy, dòng tổng bằng tổng các dòng phân nhánh:

$$
\begin{aligned}
&I = I_1+I_2+I_3\\
&\quad =\frac{V_{ab}}{R_1}+\frac{V_{ab}}{R_2}\\
&\quad+\frac{V_{ab}}{R_3}.
\end{aligned}
$$

Theo định nghĩa điện trở tương đương, $I/V_{ab}=1/R_{\mathrm{eq}}$. Do đó,

$$
\begin{aligned}
&\frac{1}{R_{\mathrm{eq}}} = \frac{1}{R_1}\\
&\quad+\frac{1}{R_2}\\
&\quad+\frac{1}{R_3}.
\end{aligned}
\tag{26.2}
$$

Với $n$ điện trở mắc song song, ta khai triển ba số hạng đầu trước khi viết gọn bằng ký hiệu tổng:

$$
\begin{aligned}
&\frac{1}{R_{\mathrm{eq}}} = \frac{1}{R_1}+\frac{1}{R_2}\\
&\quad+\frac{1}{R_3}+\cdots+\frac{1}{R_n}\\
&\quad =\sum_{i=1}^{n}\frac{1}{R_i}.
\end{aligned}
$$

Điện trở tương đương song song luôn nhỏ hơn từng điện trở nhánh. Mỗi nhánh thêm vào tạo thêm một đường cho điện tích chuyển động, làm tổng dòng tăng khi hiệu điện thế không đổi.

::: warning Điện trở và tụ điện mắc song song
Điện trở mắc song song cộng nghịch đảo theo (26.2), vì dòng qua mỗi nhánh tỉ lệ thuận với hiệu điện thế chung và tỉ lệ nghịch với điện trở nhánh. Tụ điện mắc song song cộng trực tiếp theo (24.7), vì điện tích trên mỗi tụ tỉ lệ thuận với điện dung khi hiệu điện thế trên các tụ bằng nhau.
:::

Với hai điện trở song song, quy tắc trên cho

$$
\begin{aligned}
&\frac{1}{R_{\mathrm{eq}}} = \frac{1}{R_1}\\
&\quad +\frac{1}{R_2}\\
&\quad =\frac{R_1+R_2}{R_1R_2}.
\end{aligned}
$$

Suy ra công thức tích trên tổng:

$$
\begin{aligned}
&R_{\mathrm{eq}} = \\
&\frac{R_1R_2}{R_1+R_2}.
\end{aligned}
\tag{26.3}
$$

Với hai điện trở mắc song song, tỉ số dòng điện là

$$
\frac{I_1}{I_2}=\frac{R_2}{R_1}.
\tag{26.4}
$$

Dòng điện trong hai nhánh tỉ lệ nghịch với điện trở. Nhánh có điện trở nhỏ mang dòng lớn hơn.

### Chiến lược giải bài toán 26.1: Điện trở nối tiếp và song song

#### Nhận diện khái niệm

Nhiều mạng điện gồm những nhóm điện trở mắc nối tiếp, mắc song song hoặc kết hợp cả hai kiểu. Có thể thay các mạng như vậy bằng một điện trở tương đương. Cách suy luận tương tự chiến lược giải mạng tụ điện ở Mục 24.2.

#### Bố trí bài giải

1. Vẽ sơ đồ mạng điện.
2. Xác định những nhóm điện trở mắc nối tiếp hoặc song song.
3. Ghi các đại lượng cần tìm. Chúng có thể là điện trở tương đương của mạng, hiệu điện thế trên từng điện trở hoặc dòng điện qua từng điện trở.

#### Thực hiện

1. Dùng (26.1) hoặc (26.2) để tìm điện trở tương đương của nhóm nối tiếp hoặc song song.
2. Với mạng phức tạp hơn, thử rút gọn từng nhóm. Trong Hình 26.1c, trước hết thay cặp $R_2$, $R_3$ song song bằng điện trở tương đương, rồi ghép kết quả nối tiếp với $R_1$. Trong Hình 26.1d, trước hết gộp $R_2$, $R_3$ nối tiếp, rồi xét tổ hợp đó song song với $R_1$.
3. Ghi nhớ hiệu điện thế toàn tổ hợp nối tiếp bằng tổng hiệu điện thế trên từng điện trở. Trong tổ hợp song song, hiệu điện thế trên mỗi điện trở bằng hiệu điện thế trên cả tổ hợp.
4. Dòng qua các điện trở nối tiếp như nhau và bằng dòng qua tổ hợp. Dòng tổng qua các điện trở song song bằng tổng dòng qua từng nhánh.

#### Đánh giá

Kiểm tra xem kết quả có phù hợp với cấu trúc mạch không. Điện trở tương đương nối tiếp phải lớn hơn từng điện trở thành phần. Điện trở tương đương song song phải nhỏ hơn từng điện trở thành phần.

### Ví dụ 26.1. Điện trở tương đương

Tìm điện trở tương đương của mạng trong Hình 26.3a và dòng điện qua mỗi điện trở. Nguồn điện có suất điện động $18\,\mathrm V$ và điện trở trong không đáng kể.

![Hình 26.3: Các bước rút gọn tổ hợp điện trở](../img/young-26/hinh-26-03.png)

**Hình 26.3:** Các phần (a)–(c) lần lượt cho thấy mạng ban đầu, thay cặp song song bằng điện trở $2\,\Omega$, rồi thay toàn mạng bằng điện trở tương đương $6\,\Omega$. Các sơ đồ (d)–(f) lặp lại các bước theo chiều ngược để khôi phục dòng và hiệu điện thế ban đầu.

#### Nhận diện và bố trí

Mạng gồm ba điện trở, trong đó $6\,\Omega$ song song với $3\,\Omega$, rồi nhóm này nối tiếp với điện trở $4\,\Omega$. Ta tìm điện trở tương đương của cặp song song trước, rồi cộng với $4\,\Omega$. Sau đó, từ dòng qua mạng tổng thể, ta lần lượt tìm dòng trong nhánh nối tiếp và các nhánh song song.

#### Thực hiện

Từ (26.2), điện trở tương đương của cặp $6\,\Omega$ và $3\,\Omega$ là

$$
\begin{aligned}
&\frac{1}{R_{6\parallel3}} = \frac{1}{6\,\Omega}\\
&\quad +\frac{1}{3\,\Omega}\\
&\quad =\frac{1}{2\,\Omega},\\
&R_{6\parallel3} = 2\,\Omega.
\end{aligned}
$$

Cặp tương đương này nối tiếp với điện trở $4\,\Omega$, nên

$$
R_{\mathrm{eq}}=2\,\Omega+4\,\Omega=6\,\Omega.
$$

Nguồn đặt hiệu điện thế $18\,\mathrm V$ lên điện trở tương đương, vì vậy dòng qua nguồn và điện trở $4\,\Omega$ là

$$
I=\frac{18\,\mathrm V}{6\,\Omega}=3\,\mathrm A.
$$

Dòng $3\,\mathrm A$ cũng đi qua điện trở tương đương $2\,\Omega$. Hiệu điện thế trên nhóm song song là

$$
V_{cb}=I(2\,\Omega)=6\,\mathrm V.
$$

Hai điện trở song song cùng chịu hiệu điện thế này. Do đó,

$$
\begin{aligned}
&I_{6\,\Omega} = \frac{6\,\mathrm V}{6\,\Omega}=1\,\mathrm A,\\
&I_{3\,\Omega} = \frac{6\,\mathrm V}{3\,\Omega}=2\,\mathrm A.
\end{aligned}
$$

#### Đánh giá

Trong hai nhánh song song, điện trở $3\,\Omega$ mang dòng gấp đôi nhánh $6\,\Omega$, đúng với (26.4). Tổng dòng qua hai nhánh là $1\,\mathrm A+2\,\mathrm A=3\,\mathrm A$, bằng dòng qua điện trở nối tiếp $4\,\Omega$.

#### Ý chính

Trong mạch nối tiếp, dòng điện qua các điện trở bằng nhau, còn hiệu điện thế thành phần có thể khác nhau. Trong mạch song song, hiệu điện thế trên các điện trở bằng nhau, còn dòng điện nhánh có thể khác nhau. Điện trở tương đương nối tiếp cộng trực tiếp, còn điện trở tương đương song song được tìm bằng tổng các nghịch đảo.

### Ví dụ 26.2. Mắc nối tiếp và mắc song song

Hai bóng đèn dây tóc giống nhau, mỗi bóng có điện trở $R=2\,\Omega$, được mắc vào nguồn $\mathcal E=8\,\mathrm V$ có điện trở trong không đáng kể. Tìm dòng qua từng bóng, hiệu điện thế trên từng bóng, công suất của mỗi bóng và công suất toàn mạch khi hai bóng mắc (a) nối tiếp và (b) song song. (c) Nếu một bóng bị đứt dây tóc, điều gì xảy ra với bóng kia trong mỗi cách mắc?

![Hình 26.4: Hai bóng đèn mắc nối tiếp và mắc song song](../img/young-26/hinh-26-04.png)

**Hình 26.4:** Hai sơ đồ lần lượt cho thấy (a) hai bóng nối tiếp giữa $a$ và $c$ và (b) hai bóng song song giữa $d$ và $e$.

#### Nhận diện và bố trí

Bóng đèn được xem như điện trở trong các mạch đơn giản ở đây. Khi biết dòng điện qua bóng, có thể tính công suất bằng $P=I^2R$ hoặc $P=V^2/R$.

#### Thực hiện

**(a) Hai bóng mắc nối tiếp.** Điện trở tương đương giữa $a$ và $c$ là

$$
R_{\mathrm{eq}}=R+R=2(2\,\Omega)=4\,\Omega.
$$

Dòng điện qua mỗi bóng giống nhau:

$$
I=\frac{8\,\mathrm V}{4\,\Omega}=2\,\mathrm A.
$$

Vì hai điện trở bằng nhau, hiệu điện thế trên từng bóng cũng bằng nhau:

$$
\begin{aligned}
&V_{ab}=V_{bc} = IR\\
&\quad =(2\,\mathrm A)(2\,\Omega)\\
&\quad =4\,\mathrm V.
\end{aligned}
$$

Công suất mỗi bóng là

$$
\begin{aligned}
&P = I^2R\\
&\quad =(2\,\mathrm A)^2(2\,\Omega)\\
&\quad =8\,\mathrm W.
\end{aligned}
$$

Có thể kiểm tra công suất bằng hiệu điện thế trên bóng:

$$
\begin{aligned}
&P = \frac{V^2}{R}\\
&\quad =\frac{(4\,\mathrm V)^2}{2\,\Omega}\\
&\quad =8\,\mathrm W.
\end{aligned}
$$

Tổng công suất cấp cho hai bóng là

$$
P_{\mathrm{tot}}=2P=16\,\mathrm W.
$$

**(b) Hai bóng mắc song song.** Hiệu điện thế trên mỗi bóng bằng hiệu điện thế hai đầu nguồn, tức $8\,\mathrm V$. Dòng qua mỗi bóng là

$$
I=\frac{8\,\mathrm V}{2\,\Omega}=4\,\mathrm A.
$$

Công suất mỗi bóng là

$$
\begin{aligned}
&P = I^2R\\
&\quad =(4\,\mathrm A)^2(2\,\Omega)\\
&\quad =32\,\mathrm W.
\end{aligned}
$$

Kiểm tra theo hiệu điện thế:

$$
\begin{aligned}
&P = \frac{V^2}{R}\\
&\quad =\frac{(8\,\mathrm V)^2}{2\,\Omega}\\
&\quad =32\,\mathrm W.
\end{aligned}
$$

Tổng công suất của hai bóng là

$$
P_{\mathrm{tot}}=2P=64\,\mathrm W.
$$

Ở cách mắc song song, mỗi bóng có hiệu điện thế và dòng điện gấp đôi so với cách mắc nối tiếp. Công suất mỗi bóng vì thế gấp bốn. Năng lượng được lấy từ nguồn nhanh hơn bốn lần, nên nếu nguồn là pin thì pin cạn nhanh hơn bốn lần.

**(c) Một bóng bị đứt dây tóc.** Trong mạch nối tiếp, bóng bị đứt làm hở toàn mạch. Dòng điện qua cả hai bóng bằng không, nên bóng còn nguyên cũng tắt. Trong mạch song song, nhánh có bóng hỏng bị hở nhưng hiệu điện thế trên bóng còn hoạt động vẫn như cũ. Dòng điện và công suất của bóng còn lại không đổi.

#### Đánh giá

Mô hình tính toán này chưa hoàn toàn chính xác với bóng đèn thật, vì điện trở $R=V/I$ của bóng thay đổi theo hiệu điện thế. Dây tóc nóng hơn khi hiệu điện thế tăng, làm điện trở tăng. Tuy vậy, bóng nối tiếp với cùng nguồn thực tế vẫn sáng yếu hơn bóng mắc song song.

![Hình 26.5: Độ sáng của hai bóng đèn khi mắc nối tiếp và song song](../img/young-26/hinh-26-05.png)

**Hình 26.5:** Hai bóng đèn dây tóc nối tiếp ở phía trên nhận công suất nhỏ hơn và sáng yếu hơn hai bóng mắc song song ở phía dưới khi cùng nối với một nguồn.

#### Ý chính

Với cùng một nguồn, mỗi điện trở trong nhóm song song nhận dòng lớn hơn và tiêu thụ công suất lớn hơn so với khi các điện trở mắc nối tiếp.

### Kiểm tra hiểu mục 26.1

Giả sử ba điện trở trong Hình 26.1 có cùng điện trở $R$. Hãy xếp bốn cách mắc (a)–(d) theo điện trở tương đương từ lớn nhất đến nhỏ nhất.

- (i) $(a)$, $(b)$, $(c)$, $(d)$.
- (ii) $(a)$, $(c)$, $(d)$, $(b)$.
- (iii) $(b)$, $(d)$, $(c)$, $(a)$.
- (iv) $(d)$, $(c)$, $(b)$, $(a)$.

::: details Lời giải kiểm tra hiểu
#### Tóm tắt

Cả bốn mạng đều có ba điện trở bằng nhau, mỗi điện trở là $R$. Cần so sánh điện trở tương đương của từng cấu trúc.

#### Hướng đi

- Ở (a), ba điện trở nối tiếp nên $R_{\mathrm{eq}}=R+R+R=3R$.
- Ở (b), ba điện trở song song nên $1/R_{\mathrm{eq}}=1/R+1/R+1/R=3/R$, suy ra $R_{\mathrm{eq}}=R/3$.
- Ở (c), hai điện trở song song có điện trở tương đương $R/2$. Nhóm đó nối tiếp với điện trở thứ ba, nên $R_{\mathrm{eq}}=R+R/2=3R/2$.
- Ở (d), hai điện trở nối tiếp có điện trở tương đương $2R$. Nhóm đó song song với điện trở còn lại, nên $1/R_{\mathrm{eq}}=1/R+1/(2R)=3/(2R)$, do đó $R_{\mathrm{eq}}=2R/3$.

Vì $3R>3R/2>2R/3>R/3$, thứ tự là (a), (c), (d), (b). Đáp án (ii).
:::
