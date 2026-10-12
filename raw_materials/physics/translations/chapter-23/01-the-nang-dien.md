<!-- Source: Section23.1, printed747–753, PDF767–773. -->

## 23.1. Thế năng điện

### Công, lực thế và bảo toàn cơ năng

Khi lực $\vec F$ tác dụng lên hạt đi từ a đến b, công được tính bằng tích phân đường. Tại mỗi phần dịch chuyển nhỏ, chỉ thành phần lực dọc đường đi sinh công:

$$
\begin{aligned}
W_{a\to b}&=\int_a^b\vec F\cdot d\vec\ell\\
&=\int_a^bF\cos\varphi\,d\ell
\end{aligned}
\tag{23.1}
$$

Góc φ là góc giữa lực và dịch chuyển nhỏ tại điểm đang xét. Nếu lực là **lực thế**, công được viết qua hiệu thế năng:

$$
\begin{aligned}
W_{a\to b}&=U_a-U_b\\
&=-\Delta U.
\end{aligned}
\tag{23.2}
$$

Công dương làm thế năng giảm. Khi quả bóng rơi, trọng lực sinh công dương và thế năng trọng trường giảm. Khi bóng đi lên, trọng lực sinh công âm và thế năng tăng.

![Hình 23.1: Công trọng lực khi bóng đi từ a xuống b không phụ thuộc đường đi](../img/young-23/hinh-23-1.png)

Định lý công–động năng cho biến thiên động năng bằng tổng công. Nếu chỉ các lực thế sinh công, biến thiên động năng bằng âm biến thiên thế năng, nên:

$$
K_a+U_a=K_b+U_b
\tag{23.3}
$$

Cơ năng được bảo toàn **trong điều kiện ấy**. Nếu có lực ngoài không thế sinh công, cần tính thêm phần công đó.

### Thế năng trong điện trường đều

Hai bản kim loại song song lớn tạo trường đều hướng xuống, độ lớn E. Điện tích thử dương q₀ chịu lực hướng xuống có độ lớn q₀E. Khi đi xuống từ a đến b một khoảng d, trường sinh công:

$$
\begin{aligned}
W_{a\to b}&=Fd\\
&=q_0Ed
\end{aligned}
\tag{23.4}
$$

![Hình 23.2: Điện tích thử dương đi xuống trong trường đều giữa hai bản](../img/young-23/hinh-23-2.png)

Chọn +y hướng lên. Thành phần lực là $F_y=-q_0E$, còn các thành phần x,z bằng không. Cấu trúc này giống $F_y=-mg$ của trọng lực gần mặt đất. Lực điện trong trường đều là lực thế, nên công không phụ thuộc đường đi giữa hai điểm. Tương tự U = mgy của trọng trường, ta dùng:

$$
U=q_0Ey.
\tag{23.5}
$$

Mốc U = 0 được chọn tại y = 0. Vì vậy:

$$
\begin{aligned}
W_{a\to b}&=-\Delta U\\
&=-q_0E(y_b-y_a)\\
&=q_0E(y_a-y_b)
\end{aligned}
\tag{23.6}
$$

Nếu q₀ dương và yₐ > yᵦ, hạt đi cùng trường, lực cùng dịch chuyển, công dương và U giảm. Nếu hạt dương đi ngược trường, công âm và U tăng. Khi q₀ âm, lực đảo chiều: Đi cùng trường làm U tăng, đi ngược trường làm U giảm.

![Hình 23.3: Điện tích dương đi cùng trường làm U giảm, đi ngược trường làm U tăng](../img/young-23/hinh-23-3.png)

Quy tắc chung cần gắn với **hướng lực**, không chỉ hướng trường. Đi cùng lực điện làm thế năng giảm. Đi ngược lực điện làm thế năng tăng. Với điện tích âm, hướng lực ngược hướng trường.

![Hình 23.4: Điện tích âm có lực ngược trường và sự thay đổi thế năng tương ứng](../img/young-23/hinh-23-4.png)

### Hai điện tích điểm

Xét nguồn điểm q đứng yên và điện tích q₀ chuyển động. Trước hết cho q₀ đi theo một đường xuyên tâm, từ khoảng cách rₐ đến rᵦ. Thành phần lực theo chiều tăng r là:

$$
F_r=k\frac{qq_0}{r^2}.
\tag{23.7}
$$

![Hình 23.5: Điện tích thử thay đổi khoảng cách từ rₐ đến rᵦ theo đường xuyên tâm](../img/young-23/hinh-23-5.png)

Hai điện tích cùng dấu cho Fᵣ dương, lực đẩy. Hai điện tích trái dấu cho Fᵣ âm, lực hút. Lực thay đổi theo r nên phải tích phân:

$$
\begin{aligned}
W_{a\to b}&=kqq_0\int_{r_a}^{r_b}\frac{dr}{r^2}\\
&=kqq_0\left(\frac1{r_a}-\frac1{r_b}\right)
\end{aligned}
\tag{23.8}
$$

![Hình 23.6: Dịch chuyển theo đường bất kỳ chỉ sinh công qua thành phần xuyên tâm](../img/young-23/hinh-23-6.png)

Với đường đi bất kỳ, lực vẫn xuyên tâm. Thành phần dịch chuyển theo phương xuyên tâm là dr, nên tích vô hướng lực với dịch chuyển bằng Fᵣdr. Những phần dịch chuyển tiếp tuyến không sinh công. Tích phân công do đó vẫn bằng (23.8), chỉ phụ thuộc hai khoảng cách đầu, cuối.

Nếu hạt đi một vòng về vị trí đầu theo đường khác, hai cận xuyên tâm cuối cùng bằng nhau và tổng công bằng không. Đây là những đặc trưng của lực thế. Chọn thế năng bằng không khi hai nguồn cách nhau vô hạn, ta có:

$$
U=k\frac{qq_0}{r}.
\tag{23.9}
$$

**Giữ dấu trong tích qq₀.** Cùng dấu cho U dương, trái dấu cho U âm. U biến thiên theo 1/r, còn lực theo 1/r². Hai công thức không được dùng thay nhau.

![Hình 23.7: Thế năng theo khoảng cách với hai nguồn cùng dấu hoặc trái dấu](../img/young-23/hinh-23-7.png)

U còn bằng công của lực điện nếu q₀ đi từ khoảng cách r ra vô hạn. Với cùng dấu, lực đẩy sinh công dương và U dương. Với trái dấu, lực hút sinh công âm khi hạt bị đưa ra xa và U âm. Ở r rất nhỏ, mô hình nguồn điểm cho U tiến đến +∞ với cùng dấu và −∞ với trái dấu. Ở r rất lớn, U tiến về không.

Thế năng này thuộc **hệ tương tác của hai điện tích**, không thuộc riêng một hạt cô lập. Đổi khoảng cách từ rₐ sang rᵦ cho cùng biến thiên U dù giữ q cố định và di chuyển q₀ hay làm ngược lại. Tương tự, thế năng trọng trường thuộc hệ vật và Trái Đất.

Công thức cũng dùng được khi q₀ ở ngoài một phân bố cầu đối xứng có tổng q. Khoảng cách r lúc ấy đo đến tâm phân bố, vì Gauss cho trường ngoài giống nguồn điểm q ở tâm.

### Ví dụ 23.1: Bảo toàn năng lượng với lực điện

Positron, phản hạt của electron, có khối lượng $m=9.11\times10^{-31}$ kg và điện tích $q_0=+1.60\times10^{-19}$ C. Hạt α có $q=+3.20\times10^{-19}$ C, khối lượng $6.64\times10^{-27}$ kg. Hạt α nặng hơn positron trên 7000 lần, nên coi nó đứng yên. Ở $r_a=1.00\times10^{-10}$ m, positron bay thẳng ra xa với $v_a=3.00\times10^6$ m/s. (a) Tìm tốc độ tại $r_b=2.00\times10^{-10}$ m. (b) Tìm tốc độ ở rất xa. (c) Giữ cùng điều kiện đầu nhưng thay positron bằng electron cùng khối lượng, điện tích âm, mô tả chuyển động sau đó.

::: solution Chi tiết
**Xác định và thiết lập.** Lực điện là lực thế và nguồn α được coi cố định, nên bảo toàn cơ năng của hạt chuyển động với thế năng tương tác $\frac{kqq_0}{r}$. Với positron, lực đẩy làm hạt nhanh lên khi ra xa.

(a) Các năng lượng đầu và thế năng cuối là:

$$
\begin{aligned}
K_a&=\frac12mv_a^2\\
&=4.10\times10^{-18}\,\mathrm J,\\
U_a&=\frac{kqq_0}{r_a}\\
&=4.61\times10^{-18}\,\mathrm J,\\
U_b&=\frac{kqq_0}{r_b}\\
&=2.30\times10^{-18}\,\mathrm J,\\
K_b&=K_a+U_a-U_b\\
&=6.41\times10^{-18}\,\mathrm J,\\
v_b&=\sqrt{\frac{2K_b}{m}}\\
&\approx3.8\times10^6\,\mathrm{m/s}.
\end{aligned}
$$

(b) Ở vô hạn, U tiến về không, nên:

$$
\begin{aligned}
K_\infty&=K_a+U_a\\
&=8.71\times10^{-18}\,\mathrm J,\\
v_\infty&\approx4.4\times10^6\,\mathrm{m/s}.
\end{aligned}
$$

(c) Electron bị hút về α và chậm lại khi đi ra. Thế năng đầu đổi thành $-4.61\times10^{-18}$ J, nên cơ năng đầu khoảng $-0.51\times10^{-18}$ J. Ở vô hạn, thế năng bằng không và động năng không thể âm, vì vậy cơ năng âm không cho electron thoát ra vô hạn.

Hạt đến khoảng cách lớn nhất r_d thì vận tốc và động năng bằng không. Đặt U_d bằng cơ năng đầu:

$$
\begin{aligned}
-\frac{k(2e)e}{r_d}&=K_a+U_a,\\
r_d&\approx9.0\times10^{-10}\,\mathrm m.
\end{aligned}
$$

Sau đó hạt quay lại. Tại rᵦ, thế năng là $-2.30\times10^{-18}$ J, động năng khoảng $1.79\times10^{-18}$ J và tốc độ khoảng $2.0\times10^6$ m/s.

**Đánh giá.** Positron nhanh lên do lực đẩy, electron chậm lại rồi quay đầu do lực hút. Dấu thế năng và bảo toàn cơ năng cùng giải thích hai hành vi mà không cần tìm gia tốc theo thời gian. Các bài biến thể nằm trong phần luyện tập cuối chương.
:::

::: exercise Câu hỏi sau Ví dụ 23.1
Electron phải có tốc độ đầu tối thiểu bao nhiêu tại $r_a=1.00\times10^{-10}$ m để có thể đi ra vô hạn? Liên hệ với vận tốc thoát trong Ví dụ 13.5.
:::

### Nhiều điện tích điểm

Nếu trường do q₁,q₂,q₃,... tạo ra, công tổng lên q₀ bằng tổng công của các lực thành phần. Với hai nguồn để hình dung, phần thế năng liên quan việc đưa q₀ vào là $kq_0q_1/r_1+kq_0q_2/r_2$. Với n nguồn:

$$
\begin{aligned}
U&=kq_0\frac{q_1}{r_1}
+kq_0\frac{q_2}{r_2}\\
&\quad+\cdots+kq_0\frac{q_n}{r_n}.
\end{aligned}
$$

Với chỉ số i chạy từ 1 đến n, viết gọn thành:

$$
U=kq_0\sum_{i=1}^{n}\frac{q_i}{r_i}.
\tag{23.10}
$$

![Hình 23.8: Ba nguồn tạo thế năng tương tác với q₀ tại điểm a](../img/young-23/hinh-23-8.png)

Chỉ số i chạy qua n nguồn, rᵢ là khoảng cách từ nguồn i đến vị trí q₀. Đây là **tổng đại số**, không phải tổng vector. Khi q₀ chuyển từ a sang b, các khoảng cách đổi và công vẫn bằng Uₐ − Uᵦ.

Mọi phân bố tĩnh đều có thể chia thành nguồn điểm hoặc phần tử nguồn, nên có thể xây dựng hàm thế năng tương ứng. Vì thế lực do điện trường của phân bố điện tích **tĩnh** là lực thế.

Trong (23.9), (23.10), mốc U = 0 được đặt khi q₀ ở rất xa mọi nguồn. Có thể cộng một hằng số để chọn mốc khác mà không đổi công hoặc lực. Mốc vô hạn thường thuận tiện trong tĩnh điện, còn trong mạch điện có những mốc phù hợp hơn.

### Ứng dụng: Động cơ ion

Động cơ ion của tàu vũ trụ dùng lực điện phóng các ion xenon dương $\mathrm{Xe^+}$ với tốc độ trên 30 km/s. Lực đẩy có thể rất nhỏ, khoảng 0,09 N trong cấu hình được xét, nhưng duy trì liên tục nhiều ngày. Điều đó khác tên lửa hóa học tạo lực lớn trong thời gian ngắn. Các động cơ ion đã được sử dụng để điều khiển tàu liên hành tinh.

![Hình 23.9: Động cơ ion phóng dòng xenon dương để tạo lực đẩy tàu vũ trụ](../img/young-23/hinh-23-9.png)

### Thế năng của cả hệ nguồn

(23.10) chỉ tính phần tương tác liên quan q₀ trong trường các nguồn giữ cố định. Khi lắp ráp **toàn bộ hệ**, còn có thế năng giữa các nguồn với nhau. Bắt đầu với ba điện tích ở vô hạn, công lắp ráp gồm ba cặp khác nhau:

$$
U=k\frac{q_1q_2}{r_{12}}
+k\frac{q_1q_3}{r_{13}}
+k\frac{q_2q_3}{r_{23}}.
$$

Tổng quát, với n nguồn:

$$
U=k\sum_{\substack{1\le i<j\\j\le n}}\frac{q_iq_j}{r_{ij}}.
\tag{23.11}
$$

Điều kiện i < j chỉ lấy mỗi cặp một lần. Không lấy i = j vì không tính nguồn tương tác với chính nó. Cặp q₃,q₄ được tính với i = 3,j = 4, không tính lại với i = 4,j = 3.

### Hai cách hiểu công và thế năng

Có thể đi từ công của lực điện: Hạt đi từ a đến b thì công bằng Uₐ − Uᵦ. Nếu Uₐ cao hơn Uᵦ, trường sinh công dương khi hạt “đi xuống” thế năng.

Cũng có thể hỏi công của người đưa hạt từ b lên a **thật chậm**, sao cho động năng không đổi. Khi ấy lực ngoài bằng và ngược lực điện, công lực ngoài bằng Uₐ − Uᵦ. Nếu đưa hạt xuống vùng thế năng thấp hơn, công lực ngoài âm. Hai cách hiểu tương đương, nhưng phải giữ đúng chiều di chuyển và phân biệt lực nào đang sinh công.

### Ví dụ 23.2: Hệ ba nguồn điểm

Hai nguồn cố định trên trục x, q₁ = −e tại x = 0 và q₂ = +e tại x = a. (a) Tìm công lực ngoài để đưa q₃ = +e chậm từ vô hạn đến x = 2a. (b) Tìm thế năng tổng hệ ba nguồn.

![Hình 23.10: Ba điện tích −e, +e, +e ở x = 0, a, 2a](../img/young-23/hinh-23-10.png)

::: solution Chi tiết
**Xác định và thiết lập.** Ở (a), chỉ tính tương tác mới giữa q₃ với hai nguồn có sẵn. Ở (b), tính cả cặp q₁,q₂.

(a) Hai khoảng cách từ q₃ đến q₁,q₂ là 2a và a. Công ngoài bằng phần thế năng được thêm, vì tại vô hạn phần ấy bằng không:

$$
\begin{aligned}
W_{\mathrm{ngoài}}&=ke\left(\frac{-e}{2a}+\frac e a\right)\\
&=\frac{ke^2}{2a}.
\end{aligned}
$$

Kết quả dương. Khi đưa q₃ vào từ phía +x, lực đẩy của nguồn dương gần hơn mạnh hơn lực hút của nguồn âm xa hơn, nên phải sinh công dương.

(b) Cộng ba cặp:

$$
\begin{aligned}
U&=-\frac{ke^2}{a}-\frac{ke^2}{2a}+\frac{ke^2}{a}\\
&=-\frac{ke^2}{2a}.
\end{aligned}
$$

**Đánh giá.** Thế năng tổng âm cho thấy hệ có năng lượng thấp hơn khi mọi nguồn ở vô hạn. Công ngoài để lắp ráp toàn hệ âm, còn công ngoài để đưa chúng từ cấu hình này ra vô hạn dương. Điều đó không mâu thuẫn với công dương khi chỉ thêm q₃ ở (a), vì trước khi thêm đã có cặp q₁,q₂ mang thế năng âm.
:::

::: exercise Câu hỏi ôn lại mục 23.1
Xét ba điện tích trong Ví dụ 21.4 và Hình 21.14. (a) Thế năng tổng có dấu dương, âm hay bằng không? (b) Công ngoài để đưa chúng thật chậm ra xa nhau vô hạn có dấu dương, âm hay bằng không?
:::

::: solution Giải thích
Ba nguồn đều dương nên thế năng của từng cặp dương, tổng U dương. Đưa hệ ra vô hạn làm U giảm về không. Công ngoài trong quá trình chậm bằng biến thiên U, nên âm. Chọn **(a) dương, (b) âm**.
:::
