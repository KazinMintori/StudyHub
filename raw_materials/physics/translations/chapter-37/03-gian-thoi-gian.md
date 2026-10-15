## Một đồng hồ chuyển động chạy chậm theo nghĩa nào?

Hai người có thể đồng ý về vị trí gặp nhau, cùng khởi động đồng hồ tại chỗ ấy, rồi vẫn gán những khoảng thời gian khác nhau cho hai sự kiện tiếp theo. Ta cần một phép so sánh định lượng, bắt đầu từ một đồng hồ chỉ dùng ánh sáng và một gương.

### 1. Đồng hồ ánh sáng

Hệ $S'$ của Mavis chuyển động theo chiều $+x$ với tốc độ không đổi $u$ đối với hệ $S$ của Stanley. Tại gốc O′ có nguồn sáng, còn một gương nằm cách nguồn đoạn $d$ theo phương vuông góc vận tốc.

Sự kiện 1 là lúc nguồn phát xung. Sự kiện 2 là lúc xung phản xạ từ gương rồi trở về nguồn. Trong hệ Mavis, hai sự kiện xảy ra tại cùng một vị trí O′.

![Hình 37.6: Mavis đo đường đi lên xuống dài 2d, còn Stanley đo hai đoạn xiên vì nguồn và gương chuyển động trong thời gian ánh sáng truyền.](../img/young-37/hinh-37-06.png)

Gọi khoảng thời gian trong hệ Mavis là $\Delta t_0$. Ánh sáng đi tổng quãng đường $2d$, nên

$$
\Delta t_0=\frac{2d}{c}.
\tag{37.3}
$$

Trong hệ Stanley, nguồn đi từ vị trí phát đến vị trí nhận, cách nhau $u\Delta t$. Mỗi nửa hành trình ánh sáng có quãng dời ngang $u\Delta t/2$ và quãng dời đứng $d$. Phần sau về chiều dài sẽ giải thích vì sao hai hệ dùng cùng giá trị $d$ theo phương vuông góc chuyển động này.

Đặt $a=u\Delta t/2$ để biểu diễn cạnh ngang của mỗi tam giác. Độ dài mỗi đoạn xiên thỏa mãn

$$
l^2=d^2+a^2.
$$

Tốc độ ánh sáng vẫn bằng $c$ trong hệ Stanley, nên

$$
\begin{aligned}
\Delta t&=\frac{2l}{c}\\
&=\frac2c\sqrt{d^2+a^2}.
\end{aligned}
\tag{37.4}
$$

Từ (37.3), $d=c\Delta t_0/2$. Gọi $b=c\Delta t_0/2$ chính là biểu thức của cạnh đứng theo khoảng thời gian Mavis. Thay vào (37.4) cho

$$
\Delta t=\frac2c\sqrt{b^2+a^2}.
\tag{37.5}
$$

Ở đây $a=u\Delta t/2$ và $b=c\Delta t_0/2$, nên bình phương hai vế rồi khử mẫu cho

$$
c^2\Delta t^2=c^2\Delta t_0^2+u^2\Delta t^2.
$$

Đưa số hạng chứa $u^2\Delta t^2$ sang trái và chia cho $c^2$:

$$
\Delta t^2(1-u^2/c^2)=\Delta t_0^2.
$$

Chọn căn dương vì đang xét khoảng thời gian dương, ta được quan hệ giữa hai phép đo.

### 2. Thời gian riêng và hệ số Lorentz

**Khoảng thời gian riêng** giữa hai sự kiện là khoảng thời gian đo trong một hệ mà hai sự kiện xảy ra tại cùng một vị trí. Với hai lần tích tắc của một đồng hồ đứng yên trong hệ ấy, đồng hồ trực tiếp có mặt ở cả hai sự kiện.

Nếu hệ nghỉ của đồng hồ chuyển động với tốc độ $u$ đối với hệ thứ hai thì

$$
\Delta t=\frac{\Delta t_0}{\sqrt{1-u^2/c^2}}.
\tag{37.6}
$$

Quan hệ này áp dụng cho $0\le u<c$. Khi $u>0$, mẫu số nhỏ hơn một nên $\Delta t>\Delta t_0$. Khoảng thời gian riêng ngắn hơn khoảng thời gian giữa cùng hai sự kiện trong hệ mà đồng hồ chuyển động. Hiệu ứng này gọi là **giãn thời gian**.

Nếu Mavis dùng một đồng hồ quả lắc có hai tiếng tích tắc cách nhau một giây trong hệ nghỉ, Stanley gán khoảng thời gian lớn hơn một giây cho cùng hai tiếng tích tắc. Vì mỗi nhịp đồng hồ cần nhiều thời gian hơn trong hệ Stanley, ông nói đồng hồ chuyển động chạy chậm.

Đặt **hệ số Lorentz** là

$$
\gamma=\frac1{\sqrt{1-u^2/c^2}}.
\tag{37.7}
$$

Khi ấy, công thức giãn thời gian trở thành

$$
\Delta t=\gamma\Delta t_0.
\tag{37.8}
$$

Có thể dùng tỉ số không thứ nguyên $\beta=u/c$, khi đó $\gamma=1/\sqrt{1-\beta^2}$. Ký hiệu $\gamma$ được đọc là gamma, còn $\beta$ là beta.

![Hình 37.8: Hệ số Lorentz gần một ở tốc độ nhỏ và tăng không bị chặn khi tốc độ tương đối tiến đến c từ phía nhỏ hơn.](../img/young-37/hinh-37-08.png)

Ở $u=0{,}200c=6{,}00\times10^7\,\mathrm{m/s}$, hệ số Lorentz xấp xỉ $1{,}02$. Ở $u=0{,}000200c=6{,}00\times10^4\,\mathrm{m/s}$, hệ số ấy chỉ khoảng $1{,}00000002$. Việc có cần tính hiệu chỉnh tương đối tính hay không phụ thuộc độ chính xác cần đạt, không có một ranh giới vận tốc duy nhất cho mọi phép đo.

Khi $u/c$ rất nhỏ, $\gamma$ tiến về một. Ta tìm lại gần đúng Newton rằng hai hệ gán gần như cùng khoảng thời gian.

Một quá trình vật lý cũng có thể đóng vai trò đồng hồ. Độ sáng siêu tân tinh biến thiên theo thời gian, nên khi so sánh các đường biến thiên phải xét thời gian trong hệ nguồn và hệ quan sát. Sự kéo dài thang thời gian của một nguồn chuyển động là cách biểu hiện của cùng nguyên lý.

![Hình 37.7: Siêu tân tinh trong một thiên hà minh họa việc dùng sự biến thiên độ sáng như một đồng hồ vật lý.](../img/young-37/hinh-37-07.png)

### 3. Đo thời gian không đồng nghĩa với nhìn thấy tín hiệu lúc nào

Trong hệ $S$, hai sự kiện của đồng hồ chuyển động xảy ra ở hai vị trí khác nhau. Khoảng $\Delta t$ trong (37.6) là hiệu thời gian đã gán cho các sự kiện, chứ không phải đơn giản hiệu hai thời điểm ánh sáng từ chúng đến mắt Stanley.

Ta có thể hiệu chỉnh thời gian truyền ánh sáng. Chẳng hạn, một sự kiện trên Mặt Trời được nhìn thấy ở Trái Đất muộn hơn thời điểm nó xảy ra khoảng 500 giây. Việc biết độ trễ truyền không làm mất hiệu ứng giãn thời gian.

Cách khác là đặt một đồng hồ tại vị trí sự kiện thứ nhất và một đồng hồ tại vị trí sự kiện thứ hai. Hai đồng hồ đứng yên trong cùng hệ được đồng bộ trước. Có thể phát đồng thời hai xung từ điểm giữa để chúng đến hai đồng hồ rồi đặt cùng một số chỉ quy ước.

![Hình 37.9: Một hệ quy chiếu có thể được hình dung như lưới các đồng hồ đứng yên và đồng bộ trong hệ ấy.](../img/young-37/hinh-37-09.png)

Lưới này mở rộng ra ba chiều. Đồng hồ đồng bộ trong một hệ nói chung không đồng bộ trong hệ chuyển động đối với nó.

Khi nói “Stanley xác định Mavis đi qua điểm $x=5{,}00\,\mathrm m$ lúc $t=2{,}00\,\mathrm s$”, ta hiểu đồng hồ của mạng Stanley đặt tại điểm ấy chỉ $2{,}00\,\mathrm s$ khi Mavis đi ngang. Không cần ánh sáng từ sự kiện ấy đến mắt Stanley ngay lập tức.

### 4. Cách giải bài toán giãn thời gian

1. Nêu rõ hai sự kiện đầu và cuối. Xác định hai hệ quy chiếu đang được so sánh và đại lượng cần tìm.
2. Tìm hệ mà hai sự kiện xảy ra cùng một vị trí. Khoảng thời gian trong hệ ấy là $\Delta t_0$.
3. Dùng $\Delta t=\gamma\Delta t_0$ cho hệ còn lại. Không chọn thời gian riêng chỉ từ việc số đo “ở trên tàu” hay “ở dưới đất”.
4. Đánh giá kết quả bằng điều kiện khoảng thời gian đo trong hệ chuyển động không nhỏ hơn thời gian riêng. Tốc độ hệ phải nhỏ hơn $c$.

### Ví dụ 37.1: Thời gian sống của muon ở tốc độ 0,990c

Các hạt năng lượng cao từ vũ trụ tương tác với nguyên tử trong khí quyển và có thể tạo muon không bền. Muon có thời gian sống trung bình riêng $2{,}20\,\mu\mathrm s$. Nếu muon chuyển động với tốc độ $0{,}990c$ đối với Trái Đất, người trên Trái Đất đo thời gian sống trung bình bao nhiêu?

**Nhận dạng và chuẩn bị:** Hai sự kiện là lúc muon được tạo ra và lúc nó phân rã. Chúng xảy ra tại cùng vị trí trong hệ nghỉ muon, nên $\Delta t_0=2{,}20\,\mu\mathrm s$. Trong hệ Trái Đất, muon đã di chuyển giữa hai sự kiện.

**Thực hiện:** Với $\gamma\approx7{,}08881$,

$$
\Delta t=\gamma\Delta t_0\approx15{,}6\,\mu\mathrm s.
$$

**Đánh giá:** Thời gian sống trung bình trong hệ Trái Đất dài hơn khoảng bảy lần. Các phép đo hạt không bền chuyển động là một kiểm tra thực nghiệm của giãn thời gian. Kết luận không nói muon có một thời gian sống tuyệt đối chung cho mọi hệ.

### Ví dụ 37.2: Đồng hồ trên máy bay

Máy bay đi từ San Francisco đến New York, quãng đường khoảng $4800\,\mathrm{km}$, với tốc độ đều $300\,\mathrm{m/s}$, xấp xỉ $670\,\mathrm{mile/h}$. Người dưới đất và người trên máy bay đo thời gian chuyến đi bằng bao nhiêu?

**Nhận dạng và chuẩn bị:** Hai sự kiện là rời San Francisco và đến New York. Trong hệ mặt đất, hai sự kiện ở hai nơi khác nhau. Trong hệ máy bay, chúng cùng xảy ra tại vị trí máy bay, nên thời gian trên máy bay là thời gian riêng.

**Thực hiện:** Trong hệ mặt đất,

$$
\begin{aligned}
\Delta t&=\frac{4{,}80\times10^6}{300}\\
&=1{,}60\times10^4\,\mathrm s.
\end{aligned}
$$

Khoảng này xấp xỉ 4,4 giờ. Bình phương tỉ số tốc độ là $u^2/c^2=10^{-12}$. Vì vậy,

$$
\Delta t_0=\Delta t\sqrt{1-10^{-12}}.
$$

Để không mất độ chính xác khi trừ hai số gần nhau, dùng khai triển

$$
\sqrt{1-z}\approx1-\frac z2
$$

khi $z$ rất nhỏ. Các số hạng tiếp theo ở đây có bậc $10^{-24}$ hoặc nhỏ hơn. Thời gian riêng nhỏ hơn thời gian mặt đất một lượng

$$
\Delta t-\Delta t_0\approx8{,}00\times10^{-9}\,\mathrm s.
$$

**Đánh giá:** Hai số đo đều làm tròn thành $1{,}60\times10^4\,\mathrm s$ ở các chữ số thông thường, nhưng khác nhau khoảng 8 nano giây. Đồng hồ nguyên tử đủ chính xác cho phép nhận ra những chênh lệch nhỏ như vậy. Thí nghiệm đồng hồ bay đầy đủ còn phải xét các hiệu ứng hấp dẫn và chuyển động Trái Đất.

### Ví dụ 37.3: Khi nào một khoảng thời gian là thời gian riêng?

Mavis bay ngang Stanley với tốc độ $0{,}600c$. Khi gặp nhau, cả hai khởi động bộ đếm. (a) Khi Stanley xác định Mavis đã đi xa $9{,}00\times10^7\,\mathrm m$ và đi ngang trạm không gian, đồng hồ mỗi người chỉ bao nhiêu? (b) Stanley bắt đầu chớp mắt đúng lúc gặp Mavis. Mavis gán thời gian cho cái chớp mắt bằng $0{,}400\,\mathrm s$. Stanley đo thời gian ấy bằng bao nhiêu?

**Nhận dạng và chuẩn bị:** Phần (a) xét hai lần Mavis đi ngang Stanley rồi trạm. Phần (b) xét bắt đầu và kết thúc chớp mắt trên Stanley. Hệ có hai sự kiện cùng vị trí đã đổi giữa hai phần.

**Thực hiện:** Ở (a), trong hệ Stanley,

$$
\Delta t=\frac{9{,}00\times10^7}{0{,}600c}=0{,}500\,\mathrm s.
$$

Hệ số Lorentz là $1{,}25$, nên đồng hồ Mavis chỉ $0{,}400\,\mathrm s$. Stanley vì thế kết luận đồng hồ Mavis chạy chậm so với mạng đồng hồ trong hệ mình.

Ở (b), hai sự kiện chớp mắt cùng vị trí trong hệ Stanley. Giá trị $0{,}400\,\mathrm s$ Mavis cho thuộc loại $\Delta t$, còn số chỉ đồng hồ Stanley là

$$
\Delta t_0=\frac{0{,}400}{1{,}25}=0{,}320\,\mathrm s.
$$

**Đánh giá:** Mavis cũng kết luận đồng hồ Stanley chạy chậm trong hệ mình. Trong hệ Mavis, việc cô đi ngang trạm và Stanley kết thúc chớp mắt đồng thời ở $0{,}400\,\mathrm s$. Trong hệ Stanley, hai sự kiện ấy lần lượt xảy ra ở $0{,}500\,\mathrm s$ và $0{,}320\,\mathrm s$.

Hai kết luận về đồng hồ chuyển động không mâu thuẫn, vì cách xác định đồng thời ở những nơi khác nhau không giống nhau giữa hai hệ.

### 5. Nghịch lý sinh đôi

Hai chị em sinh đôi Eartha và Astrid là nhà du hành. Eartha ở lại Trái Đất, còn Astrid đi xa với tốc độ lớn rồi quay về. Trong mô tả của Eartha, nhịp tim và các quá trình sinh học của Astrid tiến chậm hơn trong các chặng chuyển động. Astrid trở về trẻ hơn Eartha.

Vấn đề có vẻ đối xứng: Astrid có thể nói Trái Đất chuyển động đối với mình, rồi kết luận Eartha mới trẻ hơn hay không? Nếu cả hai cùng kết luận người kia trẻ hơn khi gặp lại, sẽ có mâu thuẫn.

Hai hành trình không đối xứng. Eartha ở trong một hệ gần quán tính suốt quá trình. Astrid phải đổi vận tốc để rời đi, quay đầu và trở về, nên không thể dùng duy nhất một hệ quán tính gắn với mình cho toàn hành trình.

Khi phân tích các chặng và ghép các thời gian riêng đúng cách, Astrid trải qua ít thời gian hơn giữa hai lần gặp. Không được áp dụng đối xứng của hai hệ quán tính chuyển động đều cho cả một chuyến đi có quay đầu.

### Câu hỏi tự kiểm tra 37.3

Samir đứng trên mặt đất. Maria bay ngang Samir với tốc độ $0{,}600c$. Khi gặp nhau, cả hai cùng khởi động đồng hồ bấm giây.

(a) Trong hệ Samir, khi đồng hồ Samir chỉ $10{,}0\,\mathrm s$, đồng hồ Maria chỉ gì? (i) $10{,}0\,\mathrm s$, (ii) ít hơn $10{,}0\,\mathrm s$, hay (iii) nhiều hơn $10{,}0\,\mathrm s$?

(b) Trong hệ Maria, khi đồng hồ Maria chỉ $10{,}0\,\mathrm s$, đồng hồ Samir chỉ gì? (i) $10{,}0\,\mathrm s$, (ii) ít hơn $10{,}0\,\mathrm s$, hay (iii) nhiều hơn $10{,}0\,\mathrm s$?

<details><summary>Xem đáp án và giải thích</summary>

Cả hai phần đều chọn (ii). Trong hệ Samir, đồng hồ Maria chuyển động và chỉ $8{,}00\,\mathrm s$ tại sự kiện được xem là đồng thời với số chỉ $10{,}0\,\mathrm s$ của Samir. Trong hệ Maria, đồng hồ Samir cũng chỉ $8{,}00\,\mathrm s$ khi so sánh đồng thời với số chỉ $10{,}0\,\mathrm s$ của Maria.

Hai phép so sánh dùng hai cặp sự kiện khác nhau trên hai đồng hồ ở xa. Không có mâu thuẫn với nguyên lý tương đối.

</details>

### 6. Ai là bà trong một chuyến đi rất xa?

Một phụ nữ 20 tuổi sinh con rồi lập tức thực hiện hành trình 100 năm ánh sáng, gồm 50 năm ánh sáng đi và 50 năm ánh sáng về, với tốc độ $0{,}995c$ trên các chặng. Bỏ qua thời gian quay đầu, người ở Trái Đất trải qua khoảng 100 năm, còn người đi chỉ trải qua khoảng 10 năm.

![Ứng dụng: Một chuyến đi tương đối tính có thể làm tuổi sinh học của người bà nhỏ hơn tuổi của cháu khi họ gặp lại.](../img/young-37/ung-dung-37-sinh-doi.png)

Người phụ nữ trở về ở tuổi khoảng 30. Nếu người con ở nhà sinh con sau khi mẹ đi 20 năm, người cháu khi ấy đã khoảng 80 tuổi. Thứ bậc gia đình không thay đổi, nhưng tuổi sinh học đo bằng thời gian riêng trên những hành trình khác nhau có thể rất khác nhau.

Với các con số đã cho, thời gian Trái Đất chính xác hơn trong mô hình là khoảng 100,5 năm, còn thời gian trên tàu khoảng 10,04 năm. Những số 100, 10, 30 và 80 ở ví dụ được hiểu là các giá trị xấp xỉ.
