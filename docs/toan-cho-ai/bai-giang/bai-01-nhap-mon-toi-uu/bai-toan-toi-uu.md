---
course: toan-cho-ai
lecture: bai-01-nhap-mon-toi-uu
topic: bai-toan-toi-uu
section: topic
title: "Bài toán tối ưu và những gì cần viết ra"
description: "Biến tối ưu, hàm mục tiêu, ràng buộc, miền khả thi, giá trị tối ưu theo nghĩa infimum, nghiệm tối ưu, nghiệm ε-gần tối ưu, cực tiểu cục bộ, ràng buộc chặt và cách đổi bài toán max thành min."
---

Mỗi ngày ta đưa ra hàng chục quyết định "tốt nhất có thể": chọn đường đi nhanh nhất, chia thời gian ôn thi cho mấy môn, chọn tham số cho một mô hình dự đoán. Tối ưu hóa toán học bắt đầu bằng một việc nghe thì tầm thường nhưng thực ra khó: **viết ra chính xác** ta được chọn cái gì, thế nào là tốt hơn, và những gì không được phép. Phần lớn sai lầm khi giải bài toán tối ưu không đến từ thuật toán, mà đến từ việc bài toán được viết ra chưa đúng điều ta muốn hỏi.

Trang này giúp bạn đọc và viết một bài toán tối ưu theo đúng ngôn ngữ của sách. Ta sẽ phân biệt giá trị tối ưu với nghiệm tối ưu, gặp ba tình huống mà câu hỏi "nghiệm ở đâu" không có câu trả lời, và hiểu vì sao "tốt nhất xung quanh" khác với "tốt nhất trên toàn bộ". Bạn chỉ cần biết hàm số, đạo hàm một biến và ký hiệu vector.

## 1. Người cứu hộ chọn chỗ xuống nước

Một người cứu hộ đang đứng trên bãi cát, cách mép nước 40 m, thì phát hiện một người bơi bị chuột rút. Người bị nạn ở ngoài khơi, cách mép nước 30 m, và lệch 60 m dọc theo bờ so với chỗ người cứu hộ đứng. Trên cát, người cứu hộ chạy được 5 m/s, nhưng dưới nước chỉ bơi được 1.5 m/s. Câu hỏi đặt ra là: **nên chạy tới điểm nào trên mép nước rồi mới lao xuống, để tới chỗ người bị nạn sớm nhất?**

Có hai câu trả lời nảy ra gần như ngay lập tức, và cả hai đều chưa đúng. Câu trả lời thứ nhất là đi theo đường thẳng, vì đường thẳng ngắn nhất. Quả thật, đường thẳng chỉ dài khoảng 92.2 m, nhưng gần 39.5 m trong số đó nằm dưới nước, và riêng quãng bơi ấy đã tốn khoảng 26.3 s. Tổng cộng, người cứu hộ mất khoảng 36.88 s. Câu trả lời thứ hai đi theo hướng ngược lại: chạy tới đúng chỗ đối diện người bị nạn rồi mới bơi thẳng ra, để quãng bơi chỉ còn 30 m. Phương án này mất khoảng 34.42 s, nhanh hơn đường thẳng, nhưng vẫn chưa phải tốt nhất. Lời giải nằm đâu đó giữa hai thái cực, và muốn tìm ra nó, ta phải biến câu chuyện thành toán.

Chọn mép nước làm trục hoành và lấy mét làm đơn vị. Người cứu hộ ở điểm $A = (0, 40)$, người bị nạn ở điểm $B = (60, -30)$. Giả sử trong mỗi môi trường, người cứu hộ đi theo đường thẳng với vận tốc không đổi. Khi đó cả lộ trình được xác định bởi đúng một con số: hoành độ $x$ của điểm xuống nước $P = (x, 0)$. Thời gian tới nơi là

$$
T(x) = \frac{\sqrt{40^2 + x^2}}{5} + \frac{\sqrt{30^2 + (60 - x)^2}}{1.5}, \qquad 0 \le x \le 60 .
$$

Số hạng thứ nhất là thời gian chạy từ $A$ tới $P$, số hạng thứ hai là thời gian bơi từ $P$ tới $B$. Khi $x$ tăng, quãng chạy dài thêm còn quãng bơi ngắn lại, nên hai số hạng kéo $x$ về hai phía ngược nhau, và nghiệm là điểm cân bằng của cuộc giằng co ấy. Giải bằng máy, ta được $x^\star \approx 52.6$ m và $T(x^\star) \approx 33.82$ s: chạy khoảng 66.1 m trong 13.22 s, rồi bơi khoảng 30.9 m trong 20.60 s. So với đi theo đường thẳng, người cứu hộ tới sớm hơn khoảng 3.06 s, tức hơn 8% thời gian.

Những giả thiết vừa đặt là của người lập mô hình, không phải của bãi biển. Bãi biển thật có sóng và dòng chảy, có đoạn nước nông lội được nhanh hơn bơi. Mỗi chi tiết như thế làm công thức của $T$ thay đổi, và nghiệm thay đổi theo.

<LifeguardLab />

Đến đây có một điểm tinh tế cần dừng lại. Con số 33.82 s là tốt nhất **trong lớp các lộ trình gồm hai đoạn thẳng**. Liệu một đường cong khéo léo nào đó có tới nơi sớm hơn không? Câu trả lời là không, và lập luận khá ngắn. Lấy một lộ trình bất kỳ từ $A$ tới $B$, rồi gọi $P$ là điểm cuối cùng mà lộ trình chạm mép nước. Sau $P$, người cứu hộ ở hẳn dưới nước, nên đoạn đường còn lại dài ít nhất $|PB|$ và tốn ít nhất $|PB|/1.5$ giây. Trước $P$, vận tốc không lúc nào vượt quá 5 m/s, nên đoạn đầu tốn ít nhất $|AP|/5$ giây. Cộng lại, lộ trình tốn ít nhất $T(x_P)$ giây, với $x_P$ là hoành độ của $P$. Nếu $x_P$ nằm ngoài đoạn $[0, 60]$, cả hai quãng đều dài hơn so với khi xuống nước ở đầu mút gần nhất, nên trong mọi trường hợp $T(x_P) \ge T(x^\star)$. Điều cần giữ lại là cách lập luận này: một phương án được gọi là tối ưu chỉ khi ta có một cận đúng cho **mọi** phương án hợp lệ, và phương án đó đạt đúng cận ấy.

Vậy vì sao nghiệm lại rơi vào $x^\star \approx 52.6$? Đạo hàm của $T$ là

$$
T'(x) = \frac{x}{5\sqrt{40^2 + x^2}} - \frac{60 - x}{1.5\sqrt{30^2 + (60 - x)^2}} .
$$

Gọi $\theta_1$ là góc giữa quãng chạy và đường vuông góc với mép nước, $\theta_2$ là góc tương ứng của quãng bơi. Nhìn vào tam giác vuông có ba đỉnh $A$, $P$ và gốc tọa độ, ta thấy phân số $\tfrac{x}{\sqrt{40^2 + x^2}}$ chính là $\sin\theta_1$. Tương tự, phân số thứ hai là $\sin\theta_2$. Phương trình $T'(x) = 0$ vì thế có một dạng rất gọn:

$$
\frac{\sin\theta_1}{5} = \frac{\sin\theta_2}{1.5} .
$$

Đây đúng là định luật khúc xạ Snell trong quang học, với vận tốc ánh sáng trong hai môi trường thay cho 5 và 1.5. Fermat từng giải thích sự khúc xạ bằng nguyên lý ánh sáng đi theo đường tốn ít thời gian nhất, và phép tính vừa rồi cho thấy vì sao nguyên lý ấy dẫn tới định luật Snell. Tại nghiệm, $\theta_1 \approx 52.8^\circ$ còn $\theta_2 \approx 13.8^\circ$: quãng chạy đi xiên nhiều, quãng bơi gần như vuông góc với bờ, đúng như trực giác rằng ở môi trường chậm thì nên đi đường ngắn.

Sau khi bình phương hai vế, phương trình $T'(x) = 0$ trở thành một phương trình bậc bốn, nên ta để máy tìm nghiệm. Còn một câu hỏi nữa: làm sao chắc điểm dừng ấy tốt nhất trên cả đoạn, chứ không phải đáy của một "thung lũng" cục bộ nào đó? Đạo hàm cấp hai của mỗi số hạng trong $T$ đều dương, nên $T'$ tăng ngặt. Kết hợp với $T'(0) < 0 < T'(60)$, ta biết $T'$ đổi dấu đúng một lần, từ âm sang dương, nên điểm dừng duy nhất chính là nghiệm. Các chủ đề sau sẽ gọi tên tính chất này: $T$ là một **hàm lồi**.

Bài học đầu tiên của môn học nằm gọn trong câu chuyện này. Trước khi giải, phải viết rõ ba thứ: được chọn cái gì (điểm xuống nước), muốn gì (thời gian tới nơi ngắn nhất) và bị giới hạn bởi điều gì (vận tốc trong từng môi trường, đoạn bờ được phép xuống nước). Đổi một trong ba thứ thì bài toán khác hẳn. Chẳng hạn, nếu điều ta muốn là quãng đường ngắn nhất chứ không phải thời gian ngắn nhất, đoạn thẳng $AB$ lại trở thành nghiệm.

## 2. Dạng tổng quát của một bài toán tối ưu

Trong lý thuyết tối ưu hóa, một bài toán tối ưu chuẩn tắc được biểu diễn như sau:

$$
\begin{aligned}
\text{minimize}\quad & f_0(x)\\
\text{subject to}\quad & f_i(x) \le 0, \quad i = 1, \ldots, m,\\
& h_i(x) = 0, \quad i = 1, \ldots, p.
\end{aligned}
$$

Dòng thứ nhất đọc là "cực tiểu hóa $f_0(x)$", còn "subject to" nghĩa là "với điều kiện". Mỗi ký hiệu có một vai trò riêng:

- $x \in \mathbb{R}^n$ là **biến tối ưu**, hay biến quyết định: đại lượng ta được phép chọn.
- $f_0 : \mathbb{R}^n \to \mathbb{R}$ là **hàm mục tiêu**, còn gọi là hàm chi phí: nó chấm điểm mỗi lựa chọn, và điểm càng nhỏ càng tốt.
- Các bất đẳng thức $f_i(x) \le 0$ là **ràng buộc bất đẳng thức**, các phương trình $h_i(x) = 0$ là **ràng buộc đẳng thức**.

Khi không có ràng buộc nào ($m = p = 0$), ta nói bài toán **không ràng buộc**. Trong dạng chuẩn này, vế phải của mọi ràng buộc đều bằng 0. Điều đó luôn sắp xếp được: ràng buộc $g(x) \le b$ được viết thành $g(x) - b \le 0$, còn ràng buộc $g(x) \ge 0$ được viết thành $-g(x) \le 0$. Bài toán cứu hộ ở mục 1, chẳng hạn, có biến $x$, hàm mục tiêu $f_0(x) = T(x)$ và hai ràng buộc bất đẳng thức $-x \le 0$, $x - 60 \le 0$.

Một bài toán còn chứa những đại lượng không phải biến, chẳng hạn tọa độ của $A$, $B$ và hai vận tốc 5 m/s, 1.5 m/s trong bài toán cứu hộ. Chúng là **dữ liệu**, hay tham số của bài toán, được cố định trước khi giải. Phân biệt biến với dữ liệu là việc đầu tiên khi đọc một mô hình. Trong học máy, sự phân biệt này có khi bị đảo ngược theo ngữ cảnh: lúc huấn luyện, trọng số $w$ là biến và dữ liệu huấn luyện là cố định, còn lúc dự đoán, $w$ đã cố định và đầu vào mới là thứ thay đổi.

Các hàm $f_i, h_i$ chỉ có thể tính được trên miền xác định của chúng. Giao của tất cả các miền xác định được gọi là **miền của bài toán**, ký hiệu $\mathcal{D}$. Chẳng hạn bài toán có hàm mục tiêu $-\log x$ ngầm chứa điều kiện $x > 0$, dù không ai viết điều kiện đó ra thành một ràng buộc.

## 3. Điểm khả thi, miền khả thi và giá trị tối ưu

Một điểm $x \in \mathcal{D}$ là **khả thi** nếu nó thỏa mọi ràng buộc. Tập tất cả các điểm khả thi là **miền khả thi**. Bài toán là khả thi nếu có ít nhất một điểm khả thi, và **bất khả thi** nếu không có điểm nào. Khả thi chỉ có nghĩa là hợp lệ, chưa nói gì về chuyện tốt hay xấu.

**Giá trị tối ưu** của bài toán được định nghĩa là

$$
p^\star = \inf\{f_0(x) : x \text{ khả thi}\}.
$$

Ký hiệu $\inf$ (infimum) đọc là "cận dưới lớn nhất". Nó là số lớn nhất mà không vượt quá bất kỳ giá trị $f_0(x)$ nào. Vì sao sách không dùng $\min$? Lý do là giá trị nhỏ nhất có thể không tồn tại, trong khi cận dưới lớn nhất luôn được định nghĩa, nếu ta cho phép hai giá trị $+\infty$ và $-\infty$:

- Nếu bài toán bất khả thi, tập các giá trị là rỗng và theo quy ước $p^\star = +\infty$. Hiểu nôm na, không có lựa chọn nào cả, nên chi phí "tốt nhất" được quy ước lớn hơn mọi số thực.
- Nếu có một dãy điểm khả thi $x_k$ với $f_0(x_k) \to -\infty$, thì $p^\star = -\infty$ và ta nói bài toán **không bị chặn dưới**.

Một điểm khả thi $x^\star$ với $f_0(x^\star) = p^\star$ được gọi là **nghiệm tối ưu**. Khi có ít nhất một nghiệm tối ưu, ta nói giá trị tối ưu **đạt được**. Tập mọi nghiệm tối ưu là **tập tối ưu**, và nó có thể chứa nhiều điểm, một điểm, hoặc không điểm nào.

Ba bài toán một biến sau, đều xét trên miền $x > 0$, cho thấy các khả năng ấy khác nhau thế nào (Ví dụ 4.1 trong sách):

| Hàm mục tiêu trên $x > 0$ | Giá trị tối ưu | Có đạt không? |
| --- | --- | --- |
| $f_0(x) = 1/x$ | $p^\star = 0$ | Không: với mọi $x$, điểm $2x$ cho giá trị nhỏ hơn |
| $f_0(x) = -\log x$ | $p^\star = -\infty$ | Không: bài toán không bị chặn dưới |
| $f_0(x) = x\log x$ | $p^\star = -1/e$ | Có, tại duy nhất $x^\star = 1/e$ |

Hàng thứ ba có thể kiểm tra bằng đạo hàm: $f_0'(x) = \log x + 1$ bằng 0 khi $x = 1/e$, và $f_0'$ âm trước điểm đó, dương sau điểm đó. Hàng thứ nhất là trường hợp đáng suy nghĩ nhất. Số 0 là cận dưới lớn nhất vì mọi giá trị đều dương và ta có thể làm giá trị nhỏ tùy ý bằng cách chọn $x$ đủ lớn. Thế nhưng không điểm nào đạt đúng 0. Một bài toán như vậy có giá trị tối ưu nhưng không có nghiệm tối ưu.

Bạn có thể tự tạo những tình huống đó trong mô phỏng sau. Hãy chọn một hàm, đặt hoặc bỏ các cận $l \le x \le u$, rồi xem kết luận thay đổi ra sao.

<OptimumLab />

::: tip Thử trả lời trước khi đọc tiếp
Nếu bài toán $\min\ x$ với ràng buộc $x > 0$ được sửa thành $x \ge 0$, kết luận về $p^\star$ và về nghiệm thay đổi thế nào? Vì sao chỉ một ký hiệu nhỏ lại đổi cả câu trả lời?
:::

<details><summary>Xem lời giải thích</summary>

Với $x > 0$, giá trị tối ưu là $p^\star = 0$ nhưng không đạt, vì điểm $0$ không thuộc miền khả thi. Với $x \ge 0$, điểm $0$ trở thành khả thi và cho đúng giá trị $0$, nên $x^\star = 0$ là nghiệm duy nhất. Hai miền khả thi chỉ khác nhau đúng một điểm, nhưng đó lại là điểm mà mọi dãy tốt dần đều tiến tới. Đây là lý do các bài toán tối ưu "đẹp" thường được phát biểu với ràng buộc dạng $\le$ chứ không phải $<$: miền khả thi khi đó là tập đóng, và các điểm giới hạn không bị loại ra.

</details>

## 4. Nghiệm gần tối ưu và chuyện dừng thuật toán

Trên máy tính, ta hiếm khi tính được $p^\star$ một cách chính xác tuyệt đối. Vì vậy sách định nghĩa thêm: một điểm khả thi $x$ là **$\varepsilon$-gần tối ưu** ($\varepsilon$-suboptimal) nếu

$$
f_0(x) \le p^\star + \varepsilon, \qquad \varepsilon > 0 .
$$

Định nghĩa này trông có vẻ phụ, nhưng nó gắn với một câu hỏi rất thực tế: khi nào một thuật toán được phép dừng? Nếu biết một cận dưới $\ell \le p^\star$ và một điểm khả thi $x$ có $f_0(x) - \ell \le \varepsilon$, thì $x$ chắc chắn là $\varepsilon$-gần tối ưu, dù ta không biết chính xác $p^\star$.

Bài toán cứu hộ cho một ví dụ cụ thể. Vì $\sqrt{40^2 + x^2} \ge 40$ và $\sqrt{30^2 + (60 - x)^2} \ge 30$, mọi phương án đều tốn ít nhất $\tfrac{40}{5} + \tfrac{30}{1.5} = 28$ giây, nên $\ell = 28$ là một cận dưới của $p^\star$. Phương án chạy tới $x = 60$ rồi bơi thẳng ra tốn khoảng 34.42 giây. Không cần giải gì thêm, ta đã biết phương án ấy chậm hơn tối ưu không quá 6.43 giây, tức nó là $6.43$-gần tối ưu. Cận 28 giây khá lỏng, vì thực ra phương án ấy chỉ chậm hơn tối ưu khoảng 0.61 giây, và Câu 6 ở cuối trang sẽ chỉ cách nâng cận lên đúng bằng $p^\star$. Ý tưởng "kẹp" $p^\star$ giữa một giá trị đạt được và một cận dưới chứng minh được sẽ trở thành trung tâm của chương đối ngẫu Lagrange.

## 5. Tốt nhất xung quanh và tốt nhất trên toàn miền

Định nghĩa nghiệm tối ưu ở mục 3 so sánh $x^\star$ với **mọi** điểm khả thi. Có một khái niệm yếu hơn chỉ so với các điểm khả thi ở gần. Điểm khả thi $x$ là **tối ưu cục bộ** nếu có một bán kính $R > 0$ sao cho $x$ là nghiệm của bài toán

$$
\begin{aligned}
\text{minimize}\quad & f_0(z)\\
\text{subject to}\quad & f_i(z) \le 0,\ i = 1, \ldots, m, \quad h_i(z) = 0,\ i = 1, \ldots, p,\\
& \|z - x\|_2 \le R,
\end{aligned}
$$

với biến $z$. Nói cách khác, trong một quả cầu bán kính $R$ quanh $x$, không có điểm khả thi nào tốt hơn $x$. Để phân biệt, nghiệm tối ưu theo nghĩa ở mục 3 đôi khi được gọi là tối ưu toàn cục. Trong sách và trong môn học này, chữ "tối ưu" không kèm thêm gì luôn có nghĩa là tối ưu toàn cục.

Hàm $f(x) = x^4 - 4x^2 + x$ là một ví dụ dễ hình dung. Đồ thị của nó có hai "thung lũng": một ở gần $x \approx -1.47$ với giá trị khoảng $-5.44$, một ở gần $x \approx 1.35$ với giá trị khoảng $-2.62$. Cả hai đều là cực tiểu cục bộ, nhưng chỉ thung lũng bên trái là cực tiểu toàn cục. Một thuật toán chỉ nhìn được độ dốc quanh điểm đang đứng, nếu xuất phát ở bên phải, rất có thể dừng ở thung lũng bên phải mà không biết bên trái còn một điểm tốt hơn. Bạn có thể chọn hàm này trong mô phỏng ở mục 3 và đặt $l = 0$ để thấy điều xảy ra khi thung lũng bên trái bị ràng buộc loại ra.

Sự khác nhau giữa cục bộ và toàn cục là lý do chính khiến tối ưu tổng quát khó. Một trong những điều đẹp nhất của chương này là: với bài toán lồi, hai khái niệm trùng nhau. Ta sẽ chứng minh điều đó ở chủ đề "Cực tiểu cục bộ và cực tiểu toàn cục", sau khi đã có đủ khái niệm tập lồi và hàm lồi.

## 6. Ràng buộc chặt, ràng buộc thừa và bài toán khả thi

Tại một điểm khả thi $x$, ràng buộc $f_i(x) \le 0$ được gọi là **chặt** (active) nếu $f_i(x) = 0$, và **không chặt** nếu $f_i(x) < 0$. Ràng buộc đẳng thức thì chặt tại mọi điểm khả thi. Hình ảnh trực quan là: ràng buộc chặt là ràng buộc đang "chạm" vào điểm $x$, còn ràng buộc không chặt vẫn còn khoảng trống.

Hãy xét bài toán khớp một hằng số $c$ với ba số liệu tự đặt $1, 5, 6$:

$$
\min_c\ (c - 1)^2 + (c - 5)^2 + (c - 6)^2 .
$$

Đạo hàm bằng $2(c-1) + 2(c-5) + 2(c-6)$, tức $6c - 24$, triệt tiêu tại $c = 4$, trung bình của ba số, và giá trị tối ưu là $9 + 1 + 4 = 14$. Bây giờ thêm ràng buộc $c \le 3$. Nghiệm không ràng buộc $c = 4$ không còn khả thi, và trên miền $c \le 3$ đạo hàm $6c - 24$ luôn âm, nên hàm giảm khi $c$ tăng. Nghiệm mới là $c^\star = 3$ với giá trị $4 + 4 + 9 = 17$. Ràng buộc $c \le 3$ chặt tại nghiệm, và nó thật sự làm thay đổi nghiệm. Ngược lại, nếu ràng buộc là $c \le 5$ thì nghiệm vẫn là $c = 4$, ràng buộc không chặt, và bỏ nó đi cũng chẳng sao.

Một ràng buộc là **thừa** nếu bỏ nó đi không làm thay đổi miền khả thi. Chẳng hạn trong hệ $x \le 1$ và $x \le 2$, ràng buộc thứ hai thừa. Cần phân biệt hai ý: ràng buộc không chặt tại nghiệm vẫn có thể không thừa, vì nó vẫn cắt bỏ một phần miền khả thi ở chỗ khác. Hai ràng buộc $0 \le x \le 60$ của bài toán cứu hộ là ví dụ. Tại nghiệm $x^\star \approx 52.6$, cả hai đều không chặt, nhưng chúng không thừa, vì chúng vẫn loại những điểm như $x = 70$ ra khỏi miền khả thi.

Cuối cùng, nếu hàm mục tiêu bằng 0 với mọi $x$, thì giá trị tối ưu chỉ có thể là $0$ (khi miền khả thi khác rỗng) hoặc $+\infty$ (khi miền khả thi rỗng). Ta gọi đó là **bài toán khả thi** và viết

$$
\begin{aligned}
\text{find}\quad & x\\
\text{subject to}\quad & f_i(x) \le 0,\ i = 1, \ldots, m, \quad h_i(x) = 0,\ i = 1, \ldots, p.
\end{aligned}
$$

Bài toán khả thi hỏi hai việc: các ràng buộc có mâu thuẫn nhau không, và nếu không thì chỉ ra một điểm thỏa chúng. Nghe đơn giản, nhưng trong thực tế nhiều thuật toán phải giải một bài toán khả thi trước rồi mới bắt đầu cực tiểu hóa.

## 7. Bài toán cực đại

Sách thống nhất dùng bài toán cực tiểu. Muốn cực đại $f_0(x)$, ta cực tiểu $-f_0(x)$ trên cùng miền khả thi. Hai bài toán có cùng tập nghiệm, còn giá trị tối ưu đổi dấu: nếu $p^\star_{\min}$ là giá trị tối ưu của bài toán cực tiểu $-f_0$, thì bài toán cực đại $f_0$ có giá trị tối ưu $-p^\star_{\min}$. Trong bài toán cực đại, sách định nghĩa $p^\star = \sup\{f_0(x) : x \text{ khả thi}\}$, và hàm mục tiêu thường được gọi là hàm lợi ích thay vì hàm chi phí. Học máy dùng phép đổi này liên tục. Thay vì cực đại hóa hàm hợp lý của dữ liệu, người ta cực tiểu hóa âm logarit của nó. Phép đổi dấu biến cực đại thành cực tiểu, còn phép lấy logarit không làm thay đổi tập nghiệm vì logarit là hàm tăng ngặt, cùng lý do như ở Câu 5 cuối trang.

## 8. Ba loại bài toán thường gặp

Sách nêu ba lĩnh vực ứng dụng để minh họa rằng cùng một khuôn dạng có thể chứa những câu hỏi rất khác nhau. Bảng dưới đây diễn đạt lại ba ví dụ ấy theo các thành phần vừa học.

| Bài toán | Biến | Hàm mục tiêu | Ràng buộc |
| --- | --- | --- | --- |
| Phân bổ danh mục đầu tư | Số tiền đầu tư vào từng tài sản | Độ rủi ro, chẳng hạn phương sai lợi nhuận | Ngân sách, không bán khống, lợi nhuận kỳ vọng tối thiểu |
| Thiết kế kích thước linh kiện mạch | Chiều rộng, chiều dài từng linh kiện | Tổng công suất tiêu thụ | Giới hạn chế tạo, yêu cầu thời gian đáp ứng, tổng diện tích |
| Khớp mô hình với dữ liệu | Tham số của mô hình | Độ lệch giữa dự đoán và quan sát | Thông tin biết trước, chẳng hạn tham số không âm |

Dòng cuối là dòng gần với học máy nhất. Huấn luyện một mô hình, về bản chất, là giải một bài toán tối ưu mà biến là tham số. Tuy vậy, cần nói rõ một điều mà sách cũng nhấn mạnh: lời giải tối ưu chỉ tốt bằng mô hình mà nó tối ưu. Một mô hình khớp dữ liệu huấn luyện hoàn hảo vẫn có thể dự đoán kém trên dữ liệu mới, vì tiêu chí "khớp dữ liệu huấn luyện" chưa chắc là điều ta thật sự muốn.

## 9. Những câu hỏi để đào sâu

**Câu 1.** Khẳng định "bài toán có giá trị tối ưu hữu hạn thì chắc chắn có nghiệm tối ưu" nghe rất hợp lý. Hãy tìm một phản ví dụ khác với các ví dụ trong trang này, rồi nêu thêm một điều kiện về miền khả thi để khẳng định trở nên đúng với hàm liên tục.

<details><summary>Xem lời giải thích</summary>

Chẳng hạn $\min\ e^{x}$ trên $\mathbb{R}$: mọi giá trị đều dương, có thể nhỏ tùy ý khi $x \to -\infty$, nên $p^\star = 0$ nhưng không đạt. Nếu hàm mục tiêu liên tục và miền khả thi là tập khác rỗng, đóng và bị chặn, thì theo định lý Weierstrass hàm đạt giá trị nhỏ nhất, nên nghiệm tồn tại. Trong phản ví dụ, miền $\mathbb{R}$ đóng nhưng không bị chặn. Trong ví dụ $\min x$ với $x > 0$, miền bị chặn dưới nhưng không đóng.

</details>

**Câu 2.** Bài toán $\min\ (x-1)^2$ với ràng buộc $x^2 \le 4$ có bao nhiêu ràng buộc chặt tại nghiệm? Nếu thay ràng buộc bằng $x^2 \le \tfrac14$ thì sao?

<details><summary>Xem lời giải thích</summary>

Ràng buộc $x^2 \le 4$ nghĩa là $-2 \le x \le 2$, chứa điểm $x = 1$ nơi hàm mục tiêu bằng 0. Nghiệm là $x^\star = 1$ và ràng buộc không chặt vì $1^2 - 4 < 0$. Với $x^2 \le \tfrac14$, miền khả thi là $[-\tfrac12, \tfrac12]$. Hàm $(x-1)^2$ giảm trên miền này khi $x$ tăng, nên nghiệm là $x^\star = \tfrac12$ với giá trị $\tfrac14$, và ràng buộc chặt vì $(\tfrac12)^2 = \tfrac14$.

</details>

**Câu 3.** Trong bài toán cứu hộ, nếu người cứu hộ bơi nhanh đúng bằng tốc độ chạy thì nên xuống nước ở đâu? Còn nếu đảo vai trò, chẳng hạn cát lún đến mức chỉ đi được 1.5 m/s nhưng dưới nước có sẵn xuồng máy chạy 5 m/s, lộ trình tối ưu bẻ góc theo chiều nào?

<details><summary>Xem lời giải thích</summary>

Khi hai vận tốc cùng bằng $v$, ta có $T(x) = \tfrac{1}{v}\big(|AP| + |PB|\big)$, nên cực tiểu thời gian cũng là cực tiểu quãng đường. Theo bất đẳng thức tam giác, $|AP| + |PB| \ge |AB|$, với dấu bằng khi $P$ nằm trên đoạn $AB$. Vậy nghiệm là giao điểm của đoạn thẳng $AB$ với mép nước, $x = \tfrac{240}{7} \approx 34.29$. Định luật Snell nói đúng điều này theo cách khác: $\sin\theta_1 = \sin\theta_2$ nghĩa là hai đoạn nối tiếp nhau mà không gãy.

Khi vận tốc dưới nước lớn hơn, điều kiện $\tfrac{\sin\theta_1}{v_1} = \tfrac{\sin\theta_2}{v_2}$ với $v_2 > v_1$ buộc $\theta_2 > \theta_1$. Lộ trình xuống nước sớm, đi gần như vuông góc qua bãi cát rồi chạy xiên trên mặt nước. Với $v_1 = 1.5$ và $v_2 = 5$, nghiệm là $x^\star \approx 10.6$ m. Quy tắc chung rất dễ nhớ: đi xiên ở môi trường nhanh, đi gần vuông góc với mặt phân cách ở môi trường chậm. Bạn có thể kiểm tra cả hai trường hợp bằng hai thanh trượt vận tốc trong mô phỏng ở mục 1.

</details>

**Câu 4.** Tìm một bài toán khả thi, bị chặn dưới, có nghiệm, nhưng tập tối ưu có vô số điểm.

<details><summary>Xem lời giải thích</summary>

Bài toán $\min\ 0$ với $-1 \le x \le 1$ có mọi điểm khả thi đều tối ưu. Một ví dụ ít "giả tạo" hơn là $\min\ \max\{0,\ |x| - 1\}$ trên $\mathbb{R}$: hàm bằng 0 trên cả đoạn $[-1, 1]$ và dương bên ngoài, nên tập tối ưu là đoạn $[-1, 1]$. Ví dụ này cũng cho thấy tập tối ưu có thể là một đoạn thẳng. Ở các chủ đề sau, ta sẽ thấy với bài toán lồi, tập tối ưu luôn là một tập lồi.

</details>

**Câu 5.** Bài toán $\min\ f_0(x)$ và bài toán $\min\ e^{f_0(x)}$, cùng miền khả thi, có cùng tập nghiệm không? Có cùng giá trị tối ưu không?

<details><summary>Xem lời giải thích</summary>

Cùng tập nghiệm, vì hàm $u \mapsto e^u$ tăng ngặt nên thứ tự giữa các giá trị được giữ nguyên: $f_0(x) \le f_0(y)$ khi và chỉ khi $e^{f_0(x)} \le e^{f_0(y)}$. Giá trị tối ưu thì khác nhau, liên hệ bởi $p^\star_2 = e^{p^\star_1}$ khi $p^\star_1$ hữu hạn. Đây là ví dụ về hai bài toán **tương đương** nhưng không **giống nhau**. Trong thực tế ta dùng phép biến đổi tương đương này rất thường xuyên, chẳng hạn thay việc cực tiểu $\|Ax - b\|_2$ bằng cực tiểu $\|Ax - b\|_2^2$ để có hàm khả vi.

</details>

**Câu 6.** Cận dưới 28 giây ở mục 4 khá lỏng. Hãy dùng bất đẳng thức $\sqrt{p^2 + q^2} \ge p\cos\varphi + q\sin\varphi$, đúng với mọi góc $\varphi$, để tìm một họ cận dưới của $T(x)$ không phụ thuộc vào $x$. Cận tốt nhất trong họ ấy bằng bao nhiêu?

<details><summary>Xem lời giải thích</summary>

Bất đẳng thức đã cho là bất đẳng thức Cauchy–Schwarz cho hai vector $(p, q)$ và $(\cos\varphi, \sin\varphi)$, với dấu bằng khi hai vector cùng hướng. Áp dụng cho từng số hạng của $T$ với hai góc $\varphi_1, \varphi_2$, ta được

$$
T(x) \ge \frac{40\cos\varphi_1 + x\sin\varphi_1}{5} + \frac{30\cos\varphi_2 + (60 - x)\sin\varphi_2}{1.5} .
$$

Vế phải còn phụ thuộc vào $x$ qua số hạng $x\left(\tfrac{\sin\varphi_1}{5} - \tfrac{\sin\varphi_2}{1.5}\right)$. Nếu chọn hai góc sao cho $\tfrac{\sin\varphi_1}{5} = \tfrac{\sin\varphi_2}{1.5}$, số hạng ấy biến mất, và ta có một cận đúng với **mọi** $x$:

$$
T(x) \ge 8\cos\varphi_1 + 20\cos\varphi_2 + 40\sin\varphi_2 .
$$

Với $\varphi_1 = \varphi_2 = 0$, ta thu lại cận 28 giây. Tăng dần hai góc mà vẫn giữ tỉ lệ ấy, cận tăng theo: khoảng 30.69, 32.70 rồi 33.78 giây khi $\tfrac{\sin\varphi_1}{5}$ lần lượt bằng 0.05, 0.10 và 0.15. Cận lớn nhất, khoảng 33.82 giây, đúng bằng $T(x^\star)$, và đạt được khi $\varphi_1, \varphi_2$ trùng với hai góc $\theta_1, \theta_2$ của lộ trình tối ưu. Điều kiện để triệt tiêu $x$ hóa ra lại chính là định luật Snell. Chương đối ngẫu sẽ gặp lại kịch bản này ở dạng tổng quát. Ở đó ta cũng có một họ cận dưới phụ thuộc tham số, và tham số tốt nhất mang thông tin về nghiệm. Với bài toán lồi thỏa một điều kiện nhẹ như điều kiện Slater, cận tốt nhất bằng đúng giá trị tối ưu.

</details>

## 10. Bài tập tự luyện

::: exercise 1. Đoạn bờ có đá
Trở lại bài toán cứu hộ ở mục 1, nhưng giả sử đoạn bờ ứng với $x > 45$ là bãi đá, không thể xuống nước ở đó. Viết bài toán mới dưới dạng chuẩn, tìm nghiệm và cho biết ràng buộc nào chặt. Tính $T'$ tại nghiệm và giải thích vì sao không thể chỉ giải phương trình $T'(x) = 0$.
:::

::: hint
Nghiệm cũ $x \approx 52.6$ có còn khả thi không? Hãy xét dấu của $T'$ trên đoạn $[0, 45]$, và nhớ rằng $T'$ tăng ngặt.
:::

::: solution
Dạng chuẩn là cực tiểu $T(x)$ với ba ràng buộc $-x \le 0$, $x - 60 \le 0$ và $x - 45 \le 0$. Ràng buộc $x \le 60$ giờ thừa, vì đã có $x \le 45$. Nghiệm cũ $x \approx 52.6$ vi phạm ràng buộc mới. Tính trực tiếp, $T'(45) \approx -0.149 < 0$. Vì $T'$ tăng ngặt, đạo hàm âm trên cả đoạn $[0, 45]$, nên $T$ giảm trên đoạn này và nghiệm là $x^\star = 45$, với $T(45) \approx 34.40$ s, chậm hơn trước khoảng 0.59 s. Ràng buộc $x \le 45$ chặt. Tại nghiệm $T'(45) \ne 0$: đạo hàm không triệt tiêu vì nghiệm nằm trên biên, nơi người cứu hộ còn muốn dời sang phải để bơi ít hơn nhưng bãi đá không cho phép. Phương trình $T'(x) = 0$ chỉ có nghiệm $x \approx 52.6$, nằm ngoài miền khả thi.
:::

::: exercise 2. Xác định p⋆ và tập tối ưu
Với mỗi bài toán sau, cho biết miền khả thi, giá trị tối ưu và tập tối ưu (nếu có): (a) $\min\ (x-5)^2$ với $1 \le x \le 3$, (b) $\min\ (x+1)^2$ với $-1 < x \le 2$, (c) $\min\ x$ với $x \ge 3$ và $x \le 2$, (d) $\min\ (3 - x)$ với $x \ge 1$.
:::

::: solution
(a) Miền $[1, 3]$. Hàm giảm trên miền này vì $x < 5$, nên $x^\star = 3$ và $p^\star = 4$. (b) Miền $(-1, 2]$. Mọi giá trị đều dương và $(x+1)^2 \to 0$ khi $x \to -1^+$, chẳng hạn dãy $x_k = -1 + \tfrac1k$ cho giá trị $\tfrac{1}{k^2}$. Vậy $p^\star = 0$ nhưng không đạt, tập tối ưu rỗng. (c) Không có $x$ nào vừa $\ge 3$ vừa $\le 2$, nên bài toán bất khả thi và $p^\star = +\infty$. (d) Dãy $x_k = k$ cho giá trị $3 - k \to -\infty$, nên $p^\star = -\infty$, bài toán không bị chặn dưới.
:::

::: exercise 3. Viết lại về dạng chuẩn
Đưa bài toán sau về dạng chuẩn của sách và đếm số ràng buộc bất đẳng thức, đẳng thức: cực đại $5x_1 + 4x_2$ với $x_1 + x_2 \le 6$, $2x_1 + x_2 \le 9$, $x_1 \ge 0$, $x_2 \ge 0$.
:::

::: solution
Cực tiểu $f_0(x) = -5x_1 - 4x_2$ với bốn ràng buộc bất đẳng thức $x_1 + x_2 - 6 \le 0$, $2x_1 + x_2 - 9 \le 0$, $-x_1 \le 0$, $-x_2 \le 0$, và không có ràng buộc đẳng thức. Giá trị tối ưu của bài toán cực đại ban đầu bằng $-p^\star$ của bài toán vừa viết. (Đây cũng là bài toán quy hoạch tuyến tính ở chủ đề tiếp theo. Nghiệm là $(3, 3)$ với giá trị 27, và chủ đề đó giải thích vì sao.)
:::

## Tóm tắt

Một bài toán tối ưu gồm biến tối ưu, hàm mục tiêu và các ràng buộc. Những đại lượng còn lại là dữ liệu, được cố định khi giải. Miền khả thi là tập các lựa chọn hợp lệ, và việc nới rộng hay thu hẹp nó có thể thay đổi hoàn toàn nghiệm. Chỉ một đoạn bờ có đá cũng đủ đẩy điểm xuống nước của người cứu hộ ra sát biên. Điều kiện đạo hàm bằng 0 tại một nghiệm bên trong thường mang một ý nghĩa cụ thể, như định luật khúc xạ Snell trong bài toán cứu hộ.

Giá trị tối ưu $p^\star$ được định nghĩa bằng infimum, nên luôn tồn tại nếu cho phép $\pm\infty$. Nghiệm tối ưu là điểm khả thi đạt đúng $p^\star$, và có thể không tồn tại dù $p^\star$ hữu hạn. Tối ưu cục bộ chỉ so với các điểm khả thi ở gần, nên có thể khác tối ưu toàn cục. Ràng buộc chặt tại nghiệm là ràng buộc thật sự định hình nghiệm.

Sau trang này, bạn có thể đọc một bài toán theo đúng các thành phần của nó và nhận ra ba tình huống bất khả thi, không bị chặn dưới, không đạt nghiệm. Bạn cũng chỉ ra được ràng buộc nào chặt tại một nghiệm, và chuyển được một bài toán cực đại thành bài toán cực tiểu tương đương.

## Nguồn và đọc thêm

- S. Boyd, L. Vandenberghe, *Convex Optimization*, §1.1 (tr. 1–3) về bài toán tối ưu và ba lĩnh vực ứng dụng, §4.1.1–4.1.2 (tr. 127–130) về thuật ngữ, Ví dụ 4.1, bài toán khả thi và bài toán cực đại.
- Liên hệ giữa nguyên lý thời gian ngắn nhất của Fermat và định luật khúc xạ Snell là một kết quả kinh điển của quang học hình học.
- Bài toán người cứu hộ với số liệu tự đặt, lập luận về lộ trình hai đoạn thẳng, họ cận dưới ở Câu 6, ví dụ khớp hằng số với ba số liệu $1, 5, 6$, bài toán quy hoạch tuyến tính ở bài tập 3, ví dụ $\max\{0, |x| - 1\}$ và hai mô phỏng do người soạn bổ sung. Mọi con số đã được tính lại bằng chương trình.
