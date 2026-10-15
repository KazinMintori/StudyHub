## Đo chiều dài một vật đang chuyển động

Để đo chiều dài xe chạy ngang, có thể nhờ hai người đánh dấu vị trí cản trước và cản sau trên đường, rồi đo khoảng cách giữa hai dấu. Hai người phải đánh dấu đồng thời trong hệ mặt đường. Nếu đánh dấu đầu trước rồi đợi nửa giây mới đánh dấu đầu sau, ta đã ghép hai thời điểm khác nhau và không đo đúng chiều dài xe trong hệ ấy.

Tính đồng thời phụ thuộc hệ quy chiếu, nên chiều dài cũng có thể phụ thuộc hệ. Ta sẽ suy ra quan hệ bằng cùng tốc độ ánh sáng bất biến đã dùng cho đồng hồ.

### 1. Chiều dài dọc phương chuyển động

Một thước đứng yên trong hệ Mavis $S'$, có chiều dài $l_0$. Nguồn sáng gắn ở một đầu, gương gắn ở đầu kia. Trong hệ thước, thời gian xung đi rồi về là

$$
\Delta t_0=\frac{2l_0}{c}.
\tag{37.9}
$$

Đây là thời gian riêng vì xung rời nguồn rồi trở về cùng nguồn.

![Hình 37.10: Khi thước chuyển động dọc chiều dài, gương đi ra xa xung ở lượt đi, còn nguồn đi đón xung ở lượt về trong hệ Stanley.](../img/young-37/hinh-37-10.png)

Trong hệ Stanley $S$, thước chuyển động sang phải với tốc độ $u$ và có chiều dài chưa biết $l$. Ở lượt đi, xung cần thời gian $\Delta t_1$ để gặp gương. Gương đã đi thêm $u\Delta t_1$, nên quãng đường ánh sáng đi là

$$
d=l+u\Delta t_1.
\tag{37.10}
$$

Mặt khác,

$$
d=c\Delta t_1.
\tag{37.11}
$$

Khử $d$ và giải theo thời gian:

$$
\Delta t_1=\frac{l}{c-u}.
\tag{37.12}
$$

Mẫu số $c-u$ không có nghĩa ánh sáng truyền với tốc độ $c-u$. Ánh sáng vẫn truyền ở $c$ trong hệ Stanley. Hiệu tốc độ chỉ dùng để tính thời gian nó đuổi kịp gương chuyển động.

Ở lượt về, nguồn đi đón xung, nên

$$
\Delta t_2=\frac{l}{c+u}.
\tag{37.13}
$$

Tổng hai lượt là

$$
\begin{aligned}
\Delta t&=\frac{l}{c-u}+\frac{l}{c+u}\\
&=\frac{2l}{c(1-u^2/c^2)}.
\end{aligned}
\tag{37.14}
$$

Quan hệ giãn thời gian giữa cùng hai sự kiện phát và nhận lại cho

$$
\Delta t\sqrt{1-u^2/c^2}=\frac{2l_0}{c}.
\tag{37.15}
$$

Thế (37.14) vào để khử $\Delta t$, rồi rút gọn, ta thu được

$$
\begin{aligned}
l&=l_0\sqrt{1-u^2/c^2}\\
&=\frac{l_0}{\gamma}.
\end{aligned}
\tag{37.16}
$$

**Độ dài riêng** là chiều dài đo trong hệ nghỉ của vật. Ở đây $l_0$ là độ dài riêng, còn $l$ là chiều dài đo dọc chuyển động trong hệ khác. Với $u>0$, ta có $l<l_0$. Hiệu ứng ấy gọi là **co chiều dài Lorentz**.

Ở tốc độ nhỏ so với $c$, $\gamma$ gần một nên $l$ gần $l_0$. Đó là miền biến đổi Galileo mô tả tốt các phép đo thông thường. Co chiều dài là khác biệt thật giữa các phép đo đồng thời trong hai hệ, không phải một ảo giác quang học.

![Hình 37.11: Đường ống chùm hạt dài 3 km tại SLAC minh họa sự khác nhau rất lớn giữa chiều dài trong hệ phòng thí nghiệm và hệ nghỉ của electron rất nhanh.](../img/young-37/hinh-37-11.png)

Trong ví dụ ở Hình 37.11, tốc độ electron nhỏ hơn $c$ chỉ khoảng $10\,\mathrm{cm/s}$. Một đường ống dài $3\,\mathrm{km}$ trong hệ phòng chỉ dài khoảng $8\,\mathrm{cm}$ trong hệ nghỉ electron. Các số này mô tả tình huống của ví dụ, không phải mọi chế độ vận hành của máy gia tốc.

### 2. Vì sao kích thước vuông góc không co?

Xét hai thước mét giống nhau. Một thước đứng yên theo trục $y$ của Stanley, thước kia theo trục $y'$ của Mavis. Hai gốc thước O và O′ đi ngang nhau, còn vận tốc tương đối dọc trục $x$. Mỗi người đứng tại vạch 50 cm của thước mình và đánh dấu vị trí trên thước kia lúc chúng trùng phương.

![Hình 37.12: Hai thước vuông góc vận tốc tương đối vẫn có cùng chiều dài một mét trong cả hai hệ.](../img/young-37/hinh-37-12.png)

Giả sử Stanley cho rằng thước chuyển động của Mavis dài hơn thước mình. Dấu của Stanley tại vạch giữa thước mình sẽ ở dưới điểm giữa thước Mavis. Theo cùng sự trùng nhau tại chỗ ấy, Mavis phải cho rằng nửa thước Stanley ngắn hơn nửa thước mình.

Khi đó Stanley kết luận thước chuyển động dài ra, còn Mavis kết luận thước chuyển động ngắn đi. Hai hệ hoàn toàn tương đương lại nhận hai quy luật đối lập cho cùng bố trí, trái nguyên lý tương đối. Kết luận phù hợp là các kích thước vuông góc vận tốc tương đối bằng nhau.

Điều này cũng biện minh việc dùng cùng khoảng gương–nguồn $d$ theo phương vuông góc trong suy diễn đồng hồ ánh sáng.

Nếu một thanh có độ dài riêng $l_0$ và tạo góc $\theta_0$ với phương chuyển động trong hệ nghỉ, thành phần dọc chuyển động co, còn thành phần ngang giữ nguyên:

$$
\begin{aligned}
l_x&=\frac{l_0\cos\theta_0}{\gamma},\\
l_y&=l_0\sin\theta_0.
\end{aligned}
$$

Không áp dụng cùng một hệ số co cho mọi phương.

### 3. Cách giải bài toán co chiều dài

1. Xác định hai đầu vật hoặc hai mốc không gian đang tạo nên chiều dài. Có thể hình dung một thước nối hai mốc nếu đề không cho một vật hữu hình.
2. Tìm hệ mà vật hoặc hai mốc đứng yên. Chiều dài trong hệ ấy là độ dài riêng $l_0$.
3. Phân biệt thành phần song song và vuông góc vận tốc tương đối. Chỉ thành phần song song dùng $l=l_0/\gamma$.
4. Giải đại lượng cần tìm và đánh giá: Chiều dài co không lớn hơn độ dài riêng, tốc độ hệ phải nhỏ hơn $c$.

### Ví dụ 37.4: Chiều dài tàu đo từ Trái Đất

Một tàu bay ngang Trái Đất với tốc độ $0{,}990c$. Phi hành đoàn đo chiều dài dọc tàu bằng $400\,\mathrm m$. Người trên Trái Đất đo được bao nhiêu?

**Nhận dạng và chuẩn bị:** Tàu đứng yên trong hệ phi hành đoàn, nên $l_0=400\,\mathrm m$. Chiều dài đang xét song song vận tốc tương đối.

**Thực hiện:** Với $\gamma\approx7{,}08881$,

$$
l=\frac{400}{\gamma}\approx56{,}4\,\mathrm m.
$$

![Hình 37.13: Hai người trên Trái Đất dùng đồng hồ đồng bộ để ghi vị trí đầu và đuôi tàu tại cùng thời điểm trong hệ Trái Đất.](../img/young-37/hinh-37-13.png)

**Đánh giá:** Có thể đặt hai người quan sát với đồng hồ đồng bộ để ghi $x_1,x_2$ cùng lúc và tính $l=x_2-x_1$. Hai lần ghi ấy không đồng thời trong hệ tàu. Kết quả $56{,}4\,\mathrm m$ không làm độ dài riêng $400\,\mathrm m$ của tàu thay đổi.

### Ví dụ 37.5: Khoảng cách hai người trên mặt đất đo từ tàu

Hai người O₁ và O₂ ở Hình 37.13 đứng cách nhau $56{,}4\,\mathrm m$ trên Trái Đất. Phi hành đoàn của tàu nói trên đo họ cách nhau bao nhiêu?

**Nhận dạng và chuẩn bị:** Lần này, vật được xét là một thước tưởng tượng nối O₁ và O₂, đứng yên trên Trái Đất. Độ dài riêng của nó là $56{,}4\,\mathrm m$, còn hệ tàu chuyển động với tốc độ $0{,}990c$ đối với thước ấy.

**Thực hiện:** Khoảng cách đo đồng thời trong hệ tàu là

$$
l=\frac{56{,}4}{\gamma}\approx7{,}96\,\mathrm m.
$$

**Đánh giá:** Kết quả không nói tàu vừa dài $400\,\mathrm m$ vừa dài $7{,}96\,\mathrm m$ trong cùng một hệ. Con số $7{,}96\,\mathrm m$ là khoảng cách hai người trên mặt đất trong hệ tàu.

Trong hệ mặt đất, đuôi tàu ở O₁ và đầu tàu ở O₂ cùng lúc, nên khoảng cách O₁–O₂ bằng chiều dài co của tàu. Trong hệ tàu, hai sự trùng nhau ấy không đồng thời: Đầu tàu đi ngang O₂ trước khi đuôi tàu đi ngang O₁. Vì vậy, không thể ghép chúng thành một phép đo chiều dài tàu trong hệ tàu.

### 4. Hình dạng nhìn thấy khác với chiều dài đo đồng thời

Nếu biết vị trí mọi điểm của vật tại cùng một thời điểm trong hệ mình, ta sẽ xác định sự co chỉ theo phương chuyển động. Nhưng một ảnh quang học thu các photon đến máy ảnh cùng lúc. Photon từ điểm xa hơn đã rời vật sớm hơn photon từ điểm gần hơn.

Xét một thanh tiết diện vuông có các mặt song song các mặt phẳng tọa độ. Khi nhìn thẳng vào giữa mặt đầu gần nhất của thanh đứng yên, ta chỉ thấy mặt ấy. Nếu thanh chuyển động nhanh sang phải, ánh sáng phát sớm hơn từ mặt bên trái có thể đến mắt vì thanh đã đi khỏi đường truyền.

Ngược lại, có những đường sáng đi được khi thanh đứng yên lại bị thanh chuyển động che. Tổng hợp thời gian truyền và che khuất làm các thanh có vẻ xoay và biến dạng trong ảnh.

![Hình 37.14: Mô phỏng ảnh nhìn thấy của 25 thanh tiết diện vuông khi đứng yên, chuyển động ở 0,2c và 0,9c. Hiệu ứng đổi màu Doppler chưa được đưa vào hình.](../img/young-37/hinh-37-14.png)

Đó là lý do không thể chỉ chụp một ảnh rồi đọc ngay hệ số co chiều dài từ ảnh mà bỏ qua hình học truyền ánh sáng.

### Câu hỏi tự kiểm tra 37.4

Một tàu thu nhỏ bay ngang bạn theo phương ngang với tốc độ đáng kể so với $c$. Tại cùng một thời điểm trong hệ bạn, đầu và đuôi tàu trùng đúng hai đầu thước mét bạn đang cầm.

Xếp các khoảng sau từ dài nhất đến ngắn nhất.

- (i) Độ dài riêng thước mét.
- (ii) Độ dài riêng tàu.
- (iii) Chiều dài tàu trong hệ bạn.
- (iv) Chiều dài thước mét trong hệ tàu.

<details><summary>Xem đáp án và giải thích</summary>

Thứ tự là (ii), rồi (i) bằng (iii), rồi (iv). Trong hệ bạn, thước nghỉ dài một mét và tàu chuyển động cũng có chiều dài co một mét. Độ dài riêng tàu phải lớn hơn một mét.

Trong hệ tàu, thước chuyển động có chiều dài nhỏ hơn một mét. Hai sự trùng nhau giữa đầu, đuôi tàu với đầu thước không đồng thời trong hệ này. Chúng chỉ đồng thời trong hệ bạn, nên không có mâu thuẫn khi chiều dài thước trong hệ tàu ngắn hơn chiều dài tàu.

</details>
