## 33.2. Phản xạ và khúc xạ

Ta dùng mô hình tia để khảo sát phản xạ và khúc xạ. Khi sóng gặp mặt phân cách nhẵn giữa hai môi trường trong suốt, như không khí–thủy tinh hoặc nước–thủy tinh, một phần thường phản xạ về môi trường đầu. Phần còn lại khúc xạ, truyền sang môi trường thứ hai.

![Hình 33.5: Phần (a) biểu diễn sóng phẳng một phần bị phản xạ và một phần bị khúc xạ tại mặt phân cách giữa hai môi trường (ở đây là không khí và thủy tinh của cửa kính). Ánh sáng đi vào bên trong quán cà phê trải qua hai lần khúc xạ: Lần thứ nhất khi vào thủy tinh và lần thứ hai khi ra khỏi thủy tinh. Phần (b) và (c) mô tả hành vi của ánh sáng tại mặt phân cách khi biểu diễn bằng các chùm tia sáng và bằng một tia sáng đơn lẻ.](../img/young-33/hinh-33-05.png)


Các mặt sóng phẳng ở Hình 33.5a có thể được biểu diễn thuận tiện bằng các chùm tia sáng ở Hình 33.5b. Để khảo sát hình học định lượng, ta chỉ cần vẽ một tia sáng đại diện trong mỗi chùm như ở Hình 33.5c.

### Phản xạ gương và phản xạ khuếch tán

Tính chất của chùm sáng phản xạ phụ thuộc quyết định vào độ nhẵn của bề mặt phân cách so với bước sóng ánh sáng:

- **Phản xạ gương** (specular reflection): Xảy ra khi bề mặt phân cách phẳng và rất nhẵn (như mặt gương phẳng hoặc mặt nước lặng). Các tia sáng tới song song sẽ cho các tia phản xạ song song với nhau.
- **Phản xạ khuếch tán** (diffuse reflection): Xảy ra khi bề mặt gồ ghề, nhám ở quy mô vi mô (như mặt giấy, mặt tường vôi hay mặt đường nhựa). Tại mỗi điểm tới cục bộ, pháp tuyến có hướng khác nhau, khiến các tia phản xạ tỏa ra theo mọi hướng hỗn loạn. Do đó, chúng ta có thể nhìn thấy một trang sách từ nhiều góc độ khác nhau nhờ phản xạ khuếch tán.

![Hình 33.6: Hai dạng phản xạ ánh sáng. (a) Phản xạ gương trên bề mặt nhẵn. (b) Phản xạ khuếch tán trên bề mặt gồ ghề.](../img/young-33/hinh-33-06.png)


### Chiết suất của môi trường

Trong các môi trường trong suốt thông thường đang xét, tốc độ pha $v$ nhỏ hơn tốc độ ánh sáng $c$ trong chân không. Tỷ số giữa tốc độ ánh sáng trong chân không và tốc độ ánh sáng trong môi trường được định nghĩa là **chiết suất** (index of refraction) $n$ của môi trường đó:

$$
\begin{aligned}
n &= \frac{c}{v}
\end{aligned}
\tag{33.1}
$$

Với các vật liệu trong suốt thông thường ở miền bước sóng đang xét, tốc độ pha nhỏ hơn $c$ nên $n>1$. Đối với chân không, $n = 1$ theo đúng định nghĩa. Đối với không khí ở điều kiện chuẩn nhiệt độ và áp suất, chiết suất xấp xỉ $1{,}0003$, và trong hầu hết các bài toán thực hành ta có thể lấy $n \approx 1{,}00$.

### Các định luật phản xạ và khúc xạ

Các khảo sát thực nghiệm chi tiết về hiện tượng phản xạ và khúc xạ tại mặt phân cách phẳng, nhẵn giữa hai môi trường quang học dẫn tới ba kết luận cốt lõi:

1. **Mặt phẳng tới**: Tia tới, tia phản xạ, tia khúc xạ và pháp tuyến của bề mặt phân cách tại điểm tới đều cùng nằm trong một mặt phẳng, gọi là mặt phẳng tới. Mặt phẳng tới luôn vuông góc với mặt phẳng phân cách giữa hai môi trường.
2. **Định luật phản xạ**: Góc phản xạ $\theta_r$ luôn bằng góc tới $\theta_a$ đối với mọi bước sóng và đối với bất kỳ cặp môi trường nào:

$$
\begin{aligned}
\theta_r &= \theta_a
\end{aligned}
\tag{33.2}
$$

3. **Định luật khúc xạ (Định luật Snell)**: Đối với ánh sáng đơn sắc và đối với một cặp môi trường xác định $a$ và $b$, tỷ số giữa sin của góc tới $\theta_a$ và sin của góc khúc xạ $\theta_b$ bằng tỷ số nghịch đảo của hai chiết suất:

$$
\begin{aligned}
\frac{\sin \theta_a}{\sin \theta_b} &= \frac{n_b}{n_a}
\end{aligned}
\tag{33.3}
$$

Hệ thức này thường được viết gọn gàng dưới dạng đối xứng:

$$
\begin{aligned}
n_a \sin \theta_a &= n_b \sin \theta_b
\end{aligned}
\tag{33.4}
$$

> [!IMPORTANT]
> Toàn bộ các góc tới $\theta_a$, góc phản xạ $\theta_r$ và góc khúc xạ $\theta_b$ bắt buộc phải được đo so với **pháp tuyến** của bề mặt phân cách, tuyệt đối không được đo so với chính bề mặt phân cách.

Định luật khúc xạ mang tên nhà toán học Hà Lan Willebrord Snell (1591–1626), dù dạng hình học của định luật này từng được nhà khoa học Ba Tư Ibn Sahl tìm ra vào thế kỷ thứ 10. Mối liên hệ sâu sắc giữa chiết suất và vận tốc sóng $n = c/v$ chỉ được làm sáng tỏ nhiều thế kỷ sau đó.

![Hình 33.7: Các định luật phản xạ và khúc xạ ánh sáng.](../img/young-33/hinh-33-07.png)


### Chiều lệch của tia khúc xạ

Phương trình (33.4) chỉ ra hai trường hợp chuyển tiếp quan trọng giữa hai môi trường:

- Khi ánh sáng đi từ môi trường chiết quang kém sang môi trường chiết quang hơn ($n_b > n_a$), tốc độ truyền sóng giảm ($v_b < v_a$). Khi đó $\sin \theta_b < \sin \theta_a$, dẫn tới $\theta_b < \theta_a$: Tia khúc xạ **lệch lại gần pháp tuyến** hơn so với tia tới (Hình 33.8a).
- Khi ánh sáng đi từ môi trường chiết quang hơn sang môi trường chiết quang kém ($n_b < n_a$), tốc độ truyền sóng tăng ($v_b > v_a$). Khi đó $\sin \theta_b > \sin \theta_a$, dẫn tới $\theta_b > \theta_a$: Tia khúc xạ **lệch ra xa pháp tuyến** hơn so với tia tới (Hình 33.8b).
- Khi tia sáng truyền tới vuông góc với bề mặt phân cách (chiếu theo pháp tuyến, $\theta_a = 0$), ta có $\sin \theta_a = 0$, kéo theo $\theta_b = 0$ và $\theta_r = 0$: Tia sáng truyền thẳng qua bề mặt mà không bị đổi hướng, bất kể chiết suất hai môi trường là gì (Hình 33.8c).

![Hình 33.8: Khúc xạ và phản xạ trong ba trường hợp điển hình. (a) Môi trường b có chiết suất lớn hơn môi trường a. (b) Môi trường b có chiết suất nhỏ hơn môi trường a. (c) Tia sáng tới theo phương pháp tuyến.](../img/young-33/hinh-33-08.png)


Sự khúc xạ ánh sáng giải thích nhiều hiện tượng thị giác quen thuộc: Chiếc thước kẻ hay ống hút cắm nghiêng trong cốc nước có vẻ như bị gập khúc tại mặt nước (Hình 33.9). Tia sáng phát ra từ phần ngập nước khi truyền ra không khí bị bẻ lệch xa pháp tuyến, khiến ảnh biểu kiến của đáy thước bị nâng cao lên về phía mặt nước so với vị trí thực.

![Hình 33.9: Hiện tượng thước gãy trong nước. (a) Chiếc thước thẳng nhúng một nửa trong nước trông như bị bẻ cong. (b) Các tia sáng từ vật chìm dưới nước lệch ra xa pháp tuyến khi ra không khí, làm mắt nhìn thấy ảnh biểu kiến ở vị trí nông hơn thực tế.](../img/young-33/hinh-33-09.png)


Một hiệu ứng tương tự diễn ra trong khí quyển Trái Đất: Không khí ở các tầng thấp có khối lượng riêng lớn hơn nên chiết suất cao hơn một chút so với các tầng cao. Do đó, các tia sáng từ Mặt Trời khi đi xiên qua khí quyển bị uốn cong nhẹ hướng về phía mặt đất (Hình 33.10a). Khi Mặt Trời vừa lặn xuống dưới đường chân trời hình học, ta vẫn nhìn thấy hình ảnh biểu kiến của nó nhô lên phía trên chân trời. Hơn nữa, vì các tia từ mép dưới của Mặt Trời đi qua tầng khí quyển dày và đặc hơn mép trên, mép dưới bị nâng cao mạnh hơn, làm Mặt Trời lúc hoàng hôn có dạng hình bầu dục dẹt theo phương thẳng đứng (Hình 33.10b).

![Hình 33.10: Khúc xạ ánh sáng Mặt Trời trong khí quyển. (a) Chiết suất không khí tăng dần từ trên cao xuống mặt đất, uốn cong tia sáng từ Mặt Trời lặn. (b) Mép dưới của Mặt Trời bị khúc xạ mạnh hơn mép trên khiến đĩa Mặt Trời có dạng hình dẹt theo phương thẳng đứng.](../img/young-33/hinh-33-10.png)


### Tính thuận nghịch của chiều truyền ánh sáng

Một nguyên lý tổng quát mang tính nền tảng là **tính thuận nghịch của chiều truyền ánh sáng**: Đường đi của một tia sáng là hoàn toàn thuận nghịch theo hai chiều. Nếu ta đảo ngược chiều truyền của tia khúc xạ trong môi trường $b$ để nó trở thành tia tới, nó sẽ khúc xạ vào môi trường $a$ theo đúng quỹ đạo của tia tới ban đầu. Hoàn toàn tương tự, đường đi của tia phản xạ cũng có tính thuận nghịch. Đó là lý do khi bạn nhìn thấy mắt của một người qua gương phẳng, người đó cũng đồng thời nhìn thấy mắt của bạn.

Cường độ năng lượng phân bổ giữa tia phản xạ và tia khúc xạ phụ thuộc vào góc tới, chiết suất của hai môi trường và trạng thái phân cực của sóng tới. Đối với mặt phân cách không khí - thủy tinh khi chiếu thẳng góc ($\theta_a = 0$), tỷ lệ năng lượng phản xạ chỉ chiếm khoảng 4%. Với ánh sáng tới chưa phân cực, tỷ lệ này tăng khi góc tới tăng và tiến tới 100% khi góc tới tiệm cận góc lướt ($\theta_a \to 90^\circ$).

![Ứng dụng 33.1: Ấu trùng lươn biển gần như trong suốt tuyệt đối so với nước biển bao quanh. Tuy nhiên, ấu trùng vẫn quan sát được rõ ràng vì chiết suất của cơ thể nó hơi lớn hơn chiết suất của nước biển, khiến một phần ánh sáng bị phản xạ thay vì truyền qua hoàn toàn. Rìa cơ thể ấu trùng trông đặc biệt sáng bóng do ánh sáng chạm vào mép ở góc tới lướt xấp xỉ 90 độ, dẫn tới phản xạ gần 100%.](../img/young-33/ung-dung-33-do-trong-suot-au-trung.png)

Chiết suất chất khí tăng khi khối lượng riêng tăng. Đa số thủy tinh quang học có chiết suất khoảng 1,5–2,0, còn một số vật liệu như kim cương có giá trị lớn hơn.

Maxwell cũng cho phép xác định biên độ, cường độ, pha và trạng thái phân cực của sóng phản xạ, khúc xạ. Các định luật tia đang dùng chỉ mô tả hướng truyền của những sóng đó.

Bảng 33.1 dưới đây liệt kê giá trị chiết suất của một số vật chất trong suốt đối với vạch vàng natri ($\lambda_0 = 589\,\mathrm{nm}$):

#### Chất rắn

| Vật chất | Chiết suất $n$ |
| :--- | :--- |
| Nước đá ($\mathrm{H_2O}$) | $1{,}309$ |
| Fluorit ($\mathrm{CaF_2}$) | $1{,}434$ |
| Polystyren | $1{,}49$ |
| Muối mỏ ($\mathrm{NaCl}$) | $1{,}544$ |
| Thạch anh ($\mathrm{SiO_2}$) | $1{,}544$ |
| Zircon ($\mathrm{ZrO_2 \cdot SiO_2}$) | $1{,}923$ |
| Kim cương ($\mathrm{C}$) | $2{,}417$ |
| Fabulite ($\mathrm{SrTiO_3}$) | $2{,}409$ |
| Rutil ($\mathrm{TiO_2}$) | $2{,}62$ |

#### Các loại thủy tinh (giá trị điển hình)

| Vật chất | Chiết suất $n$ |
| :--- | :--- |
| Crown | $1{,}52$ |
| Flint nhẹ | $1{,}58$ |
| Flint vừa | $1{,}62$ |
| Flint đặc | $1{,}66$ |
| Flint lanthan | $1{,}80$ |

#### Chất lỏng ở $20^\circ\mathrm{C}$

| Vật chất | Chiết suất $n$ |
| :--- | :--- |
| Methanol ($\mathrm{CH_3OH}$) | $1{,}329$ |
| Nước ($\mathrm{H_2O}$) | $1{,}333$ |
| Ethanol ($\mathrm{C_2H_5OH}$) | $1{,}36$ |
| Carbon tetrachloride ($\mathrm{CCl_4}$) | $1{,}460$ |
| Dầu thông (Turpentine) | $1{,}472$ |
| Glycerin | $1{,}473$ |
| Benzen | $1{,}501$ |
| Carbon disulfide ($\mathrm{CS_2}$) | $1{,}628$ |

### Bước sóng và tần số trong môi trường

Khi tia đi từ môi trường này sang môi trường khác, những đặc trưng sóng nào thay đổi?

Khi một sóng ánh sáng truyền từ môi trường này sang môi trường khác có chiết suất khác nhau:

Thứ nhất, tại mặt phân cách đứng yên trong mô hình tuyến tính, **tần số $f$ của sóng giữ nguyên**: Số dao động sóng tới mặt phân cách trong một đơn vị thời gian bắt buộc phải bằng số dao động rời khỏi mặt phân cách trong cùng khoảng thời gian đó. Mặt phân cách không thể tự tạo ra thêm hoặc làm biến mất các chu kỳ dao động của sóng.

Thứ hai, **bước sóng $\lambda$ của ánh sáng trong môi trường thay đổi**: Vì vận tốc truyền sóng trong môi trường là $v = \lambda f$, và tần số $f$ được giữ cố định bằng tần số trong chân không $f = c/\lambda_0$, ta có hệ thức:

$$
\begin{aligned}
f &= \frac{c}{\lambda_0} = \frac{v}{\lambda}
\end{aligned}
$$

Kết hợp với định nghĩa chiết suất $n = c/v$, ta rút ra bước sóng $\lambda$ của ánh sáng trong môi trường có chiết suất $n$:

$$
\begin{aligned}
\lambda &= \frac{\lambda_0}{n}
\end{aligned}
\tag{33.5}
$$

Trong đó $\lambda_0$ là bước sóng của ánh sáng đó trong chân không. Khi ánh sáng truyền vào môi trường có chiết suất lớn hơn ($n_b > n_a$), tốc độ truyền sóng giảm xuống, khiến các mặt sóng bị "nén lại" và bước sóng $\lambda$ ngắn đi. Ngược lại, khi truyền vào môi trường có chiết suất nhỏ hơn ($n_b < n_a$), tốc độ sóng tăng lên, các mặt sóng bị "dãn ra" và bước sóng $\lambda$ dài hơn.

### Chiến lược giải bài toán 33.1: Phản xạ và khúc xạ

- **Nhận dạng bài toán**: Áp dụng các nguyên lý quang hình học khi chùm sáng gặp bề mặt phân cách giữa hai môi trường.
- **Chuẩn bị**:
  1. Vẽ hình hình học rõ ràng, biểu diễn pháp tuyến, các góc tới, phản xạ, khúc xạ và ghi rõ chiết suất của từng môi trường.
  2. Xác định các đại lượng đã biết và các biến số cần tìm.
- **Thực hiện**:
  1. Vận dụng định luật phản xạ $\theta_r = \theta_a$ và định luật khúc xạ $n_a \sin \theta_a = n_b \sin \theta_b$. Tuyệt đối luôn đo các góc so với pháp tuyến bề mặt.
  2. Sử dụng các hệ thức hình học và lượng giác tam giác vuông (tổng hai góc nhọn phụ nhau bằng $90^\circ$, tổng ba góc trong tam giác bằng $180^\circ$).
  3. Tần số $f$ không đổi tại mặt phân cách đứng yên. Bước sóng thay đổi theo hệ thức $\lambda = \lambda_0 / n$.
- **Đánh giá**: Kiểm tra tính nhất quán với định luật Snell ($n_a \sin \theta_a = n_b \sin \theta_b$). Nếu môi trường thứ hai có chiết suất lớn hơn môi trường đầu ($n_b > n_a$) và tia tới xiên, góc khúc xạ phải nhỏ hơn góc tới ($\theta_b < \theta_a$): Tia khúc xạ lệch lại gần pháp tuyến. Nếu môi trường đầu có chiết suất lớn hơn môi trường thứ hai ($n_a > n_b$), góc khúc xạ phải lớn hơn góc tới ($\theta_b > \theta_a$): Tia khúc xạ lệch ra xa pháp tuyến.

### Ví dụ 33.1: Phản xạ và khúc xạ tại mặt phân cách nước - thủy tinh

Trong Hình 33.11, môi trường $a$ là nước ($n_a = 1{,}33$) và môi trường $b$ là thủy tinh có chiết suất $n_b = 1{,}52$. Tia tới tạo với pháp tuyến một góc $\theta_a = 60{,}0^\circ$. Tìm hướng truyền của tia phản xạ và tia khúc xạ.

![Hình 33.11: Sự phản xạ và khúc xạ của tia sáng truyền từ nước sang thủy tinh.](../img/young-33/hinh-33-11.png)


**Nhận dạng bài toán**: Bài toán yêu cầu xác định góc phản xạ và góc khúc xạ khi biết góc tới và chiết suất của hai môi trường.

**Chuẩn bị**: Áp dụng định luật phản xạ phương trình (33.2) và định luật Snell phương trình (33.4). Các dữ kiện đã cho: $n_a = 1{,}33$, $n_b = 1{,}52$, $\theta_a = 60{,}0^\circ$.

**Lời giải**: Theo định luật phản xạ, góc phản xạ bằng góc tới:

$$
\begin{aligned}
\theta_r &= \theta_a = 60{,}0^\circ
\end{aligned}
$$

Để tìm góc khúc xạ $\theta_b$, ta áp dụng định luật Snell:

$$
\begin{aligned}
n_a \sin \theta_a &= n_b \sin \theta_b
\end{aligned}
$$

Biến đổi tìm $\sin \theta_b$:

$$
\begin{aligned}
\sin \theta_b &= \frac{n_a}{n_b} \sin \theta_a \\
&= \frac{1{,}33}{1{,}52} \sin 60{,}0^\circ \\
&\approx 0{,}758
\end{aligned}
$$

Lấy hàm ngược arcsin:

$$
\begin{aligned}
\theta_b &= \arcsin(0{,}758) = 49{,}3^\circ
\end{aligned}
$$

**Đánh giá**: Môi trường thứ hai có chiết suất lớn hơn môi trường đầu ($n_b > n_a$), do đó tia khúc xạ lệch lại gần pháp tuyến hơn so với tia tới và $\theta_b < \theta_a$ ($49{,}3^\circ < 60{,}0^\circ$). Kết quả phù hợp hoàn toàn với dự đoán định tính.

**Nội dung cần nhớ**: Khi ánh sáng chạm vào một mặt phân cách nhẵn giữa hai môi trường trong suốt, ánh sáng có thể vừa bị phản xạ trở lại môi trường thứ nhất vừa bị khúc xạ vào môi trường thứ hai. Góc tới và góc phản xạ luôn luôn bằng nhau. Góc khúc xạ được xác định bởi góc tới và chiết suất của hai môi trường (định luật Snell). Hãy luôn luôn đo các góc này từ đường pháp tuyến của mặt phân cách.

### Ví dụ 33.2: Chiết suất của thủy dịch trong mắt người

Bước sóng của ánh sáng đỏ phát ra từ laser helium-neon trong không khí là $633\,\mathrm{nm}$, nhưng khi truyền vào thủy dịch bên trong nhãn cầu mắt người, bước sóng giảm xuống còn $474\,\mathrm{nm}$. Tính chiết suất của thủy dịch, tốc độ truyền và tần số của ánh sáng đó bên trong thủy dịch.

**Nhận dạng bài toán**: Áp dụng định nghĩa chiết suất $n = c/v$ và mối liên hệ giữa bước sóng trong môi trường với bước sóng chân không $\lambda = \lambda_0 / n$.

**Chuẩn bị**: Vì chiết suất của không khí rất xấp xỉ 1, ta coi bước sóng trong chân không $\lambda_0 \approx 633\,\mathrm{nm} = 633 \times 10^{-9}\,\mathrm{m}$. Bước sóng trong thủy dịch $\lambda = 474\,\mathrm{nm} = 474 \times 10^{-9}\,\mathrm{m}$. Ta dùng phương trình (33.5) $\lambda = \lambda_0 / n$ để tìm $n$, sau đó tính $v = c/n$ và $f = v/\lambda$.

**Lời giải**: Từ phương trình (33.5), ta xác định chiết suất của thủy dịch:

$$
\begin{aligned}
n &= \frac{\lambda_0}{\lambda} \\
&= \frac{633\,\mathrm{nm}}{474\,\mathrm{nm}} \\
&\approx 1{,}34
\end{aligned}
$$

Giá trị này rất gần với chiết suất của nước tinh khiết ($n = 1{,}333$). Tốc độ truyền ánh sáng trong thủy dịch tính từ tỷ số chưa làm tròn $n = 633 / 474$:

$$
\begin{aligned}
v &= \frac{c}{n} \\
&= \frac{3{,}00 \times 10^8\,\mathrm{m/s}}{633 / 474} \\
&\approx 2{,}25 \times 10^8\,\mathrm{m/s}
\end{aligned}
$$

Tần số của ánh sáng bên trong thủy dịch là:

$$
\begin{aligned}
f &= \frac{v}{\lambda} \\
&= \frac{2{,}25 \times 10^8\,\mathrm{m/s}}{474 \times 10^{-9}\,\mathrm{m}} \\
&\approx 4{,}74 \times 10^{14}\,\mathrm{Hz}
\end{aligned}
$$

**Đánh giá**: Dù vận tốc và bước sóng của ánh sáng thay đổi khi đi vào thủy dịch, tần số của sóng trong không khí $f_0$ bằng đúng tần số $f$ trong thủy dịch:

$$
\begin{aligned}
f_0 &= \frac{c}{\lambda_0} \\
&= \frac{3{,}00 \times 10^8\,\mathrm{m/s}}{633 \times 10^{-9}\,\mathrm{m}} \\
&\approx 4{,}74 \times 10^{14}\,\mathrm{Hz}
\end{aligned}
$$

Điều này khẳng định một nguyên lý cốt lõi: Khi ánh sáng truyền qua mặt phân cách giữa hai môi trường, vận tốc và bước sóng cùng biến thiên theo chiết suất nhưng tần số dao động luôn được bảo toàn tuyệt đối.

**Nội dung cần nhớ**: Tại mặt phân cách đứng yên, tần số giữ nguyên. Chiết suất lớn hơn ứng với tốc độ nhỏ hơn và bước sóng ngắn hơn. Ngược lại, chiết suất nhỏ hơn ứng với tốc độ lớn hơn và bước sóng dài hơn.

### Ví dụ 33.3: Tia sáng phản xạ liên tiếp qua hai gương vuông góc

Hai gương phẳng đặt vuông góc với nhau tại $O$. Một tia sáng truyền trong mặt phẳng vuông góc với cả hai gương phản xạ lần lượt tại $P$ trên gương 1, sau đó phản xạ tại $Q$ trên gương 2 như quan sát ở Hình 33.12. Hướng truyền cuối cùng của tia sáng sau hai lần phản xạ có quan hệ như thế nào so với hướng truyền ban đầu?

![Hình 33.12: Một tia sáng chuyển động trong mặt phẳng xy. Lần phản xạ thứ nhất đổi dấu thành phần vận tốc theo trục y, và lần phản xạ thứ hai đổi dấu thành phần vận tốc theo trục x.](../img/young-33/hinh-33-12.png)


**Nhận dạng bài toán**: Bài toán yêu cầu áp dụng định luật phản xạ hai lần liên tiếp cho hệ hai gương phẳng tạo góc vuông.

**Chuẩn bị**: Áp dụng định luật phản xạ tại từng điểm tới $P$ và $Q$. Gọi $\theta_1$ là góc tới tại gương 1. Xét tam giác vuông tạo bởi hai gương và đường truyền của tia sáng.

**Lời giải**: Tại gương 1, góc tới là $\theta_1$, do đó góc phản xạ cũng bằng $\theta_1$. Góc hợp bởi tia phản xạ từ $P$ với mặt gương 1 là $90^\circ - \theta_1$.

Vì hai gương vuông góc với nhau ($90^\circ$), trong tam giác vuông $PQR$, góc tới tại gương 2 là:

$$
\begin{aligned}
\theta_2 &= 90^\circ - \theta_1
\end{aligned}
$$

Theo định luật phản xạ, góc phản xạ tại gương 2 cũng bằng $90^\circ - \theta_1$.

Độ đổi hướng của tia sáng tại mỗi lần phản xạ bằng $180^\circ - 2\theta_{\text{tới}}$. Tổng góc đổi hướng sau cả hai lần phản xạ là:

$$
\begin{aligned}
\Delta \theta &= 2(90^\circ - \theta_1) + 2\theta_1 \\
&= 180^\circ - 2\theta_1 + 2\theta_1 \\
&= 180^\circ
\end{aligned}
$$

Như vậy, tia sáng sau hai lần phản xạ bị đổi hướng đúng $180^\circ$, tức là truyền song song và ngược chiều hoàn toàn so với tia tới ban đầu.

**Đánh giá**: Góc lệch tổng cộng $180^\circ$ hoàn toàn độc lập với góc tới $\theta_1$ ban đầu. Dưới góc độ vector vận tốc, sự phản xạ làm đổi dấu thành phần vận tốc vuông góc với mặt gương nhưng giữ nguyên các thành phần vận tốc khác. Lần phản xạ tại gương 1 nằm ngang đổi dấu thành phần vận tốc $v_y$ ($v_y \to -v_y$), còn lần phản xạ tại gương 2 thẳng đứng đổi dấu thành phần vận tốc $v_x$ ($v_x \to -v_x$). Sau hai lần phản xạ, vector vận tốc chuyển thành $-\vec{v}$, khẳng định tia sáng truyền ngược chiều ban đầu.

Với ba gương tạo thành góc lập phương, mỗi lần phản xạ đảo một thành phần vận tốc. Nếu tia gặp đủ ba mặt, cả ba thành phần đều đổi dấu nên tia ra ngược hướng tia vào. Hai tia không nhất thiết nằm trên cùng đường thẳng hoặc trở lại đúng điểm phát.

Bộ phản xạ góc được dùng trong đèn hậu ô tô và tấm phản xạ xe đạp để tăng khả năng nhận diện ban đêm. Các phi hành gia Apollo cũng đặt những mảng phản xạ trên Mặt Trăng. Dùng chùm laser phản xạ từ đó, khoảng cách Trái Đất–Mặt Trăng đã được đo với độ chính xác $0{,}15\,\mathrm m$.

**Nội dung cần nhớ**: Khi ánh sáng trải qua nhiều lần phản xạ, nhiều lần khúc xạ, hoặc kết hợp cả phản xạ và khúc xạ, hãy áp dụng định luật phản xạ hoặc định luật khúc xạ một cách độc lập tại từng bề mặt phân cách.

### Câu hỏi tự kiểm tra 33.2

Bạn đang đứng trên bờ một hồ nước trong vắt và nhìn thấy một con cá đang bơi ở một độ sâu nào đó dưới mặt nước.

(a) Muốn dùng lao đâm cá, bạn nên nhắm ở đâu so với vị trí biểu kiến?

- (i) Phía trên.
- (ii) Phía dưới.
- (iii) Đúng vị trí biểu kiến.

(b) Nếu thay lao bằng laser công suất cao để vừa làm chết vừa làm chín cá, bạn nên nhắm ở đâu?

- (i) Phía trên vị trí biểu kiến.
- (ii) Phía dưới vị trí biểu kiến.
- (iii) Đúng vị trí biểu kiến.

![Câu tự kiểm tra 33.2: Vị trí biểu kiến của cá cao hơn vị trí thật do khúc xạ tại mặt nước.](../img/young-33/tu-kiem-33-02.png)

<details><summary>Xem đáp án và giải thích</summary>

(a) Chọn (ii). (b) Chọn (iii).

Giải thích:

Đối với ngọn lao (phần a): Tia sáng từ con cá truyền từ nước ($n = 1{,}33$) ra không khí ($n = 1{,}00$) bị khúc xạ lệch ra xa pháp tuyến. Mắt người quan sát tiếp nhận chùm tia khúc xạ và cảm nhận ảnh biểu kiến của con cá nằm nông hơn (cao hơn) so với vị trí thực của nó dưới nước. Ngọn lao chuyển động theo quỹ đạo thẳng trong không khí và không bị bẻ cong như tia sáng khi chạm mặt nước. Do đó, bạn bắt buộc phải phóng ngọn lao nhắm vào vị trí **phía dưới** vị trí biểu kiến mà mắt nhìn thấy để trúng con cá thực.

Đối với chùm laser (phần b): Chùm tia laser là ánh sáng. Theo nguyên lý thuận nghịch của chiều truyền ánh sáng, chùm laser phát ra từ mắt bạn khi đi vào mặt nước sẽ bị khúc xạ lệch lại gần pháp tuyến theo đúng đường đi mà ánh sáng từ con cá truyền lên mắt bạn nhưng theo chiều ngược lại. Do đó, bạn chỉ cần nhắm chùm laser **thẳng trực diện** vào vị trí biểu kiến của con cá thì chùm laser sẽ tự động bị khúc xạ tới trúng vị trí thực của con cá.

</details>
