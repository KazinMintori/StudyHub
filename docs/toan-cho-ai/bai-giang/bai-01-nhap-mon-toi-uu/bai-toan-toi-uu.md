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

## 1. Một sợi dây và một bờ biển

Truyền thuyết kể rằng nàng Dido đến bờ biển Bắc Phi và chỉ được phép lấy phần đất mà một tấm da bò bao quanh được. Virgil nhắc tới chi tiết này trong sử thi *Aeneid* (quyển I, dòng 365–368). Theo lời kể phổ biến về sau, nàng cho cắt tấm da thành những dải thật mảnh rồi nối lại thành một sợi dây dài. Câu hỏi toán học rút ra từ câu chuyện rất rõ ràng: **với một sợi dây có độ dài cố định, nên căng nó theo hình nào để bao được nhiều đất nhất?**

Để biến câu chuyện thành toán, ta phải chọn một mô hình. Giả sử bờ biển là một đường thẳng, sợi dây có độ dài $L$ chỉ dùng cho phần biên phía đất liền, còn hai đầu dây được đặt tự do trên bờ. Những giả thiết này là của người lập mô hình chứ không có trong đoạn thơ cổ, và đổi giả thiết thì đáp án cũng đổi, như ta sẽ thấy ngay.

**Thử với hình chữ nhật.** Gọi $x$ là chiều sâu vuông góc với bờ và $y$ là cạnh song song với bờ. Dây phải rào hai cạnh sâu và một cạnh song song, nên $2x + y = L$, tức là $y = L - 2x$. Diện tích là

$$
S(x) = x(L - 2x) = -2\left(x - \frac{L}{4}\right)^2 + \frac{L^2}{8}, \qquad 0 \le x \le \frac{L}{2}.
$$

Số hạng bình phương không âm, nên $S(x) \le \tfrac{L^2}{8}$, với dấu bằng khi $x = \tfrac{L}{4}$ và $y = \tfrac{L}{2}$. Với $L = 100$ m, hình chữ nhật tốt nhất có diện tích $1250\ \text{m}^2$.

**Thử với nửa hình tròn.** Nếu dây uốn thành nửa đường tròn bán kính $r$ có đường kính nằm trên bờ, thì $\pi r = L$ và diện tích là $\tfrac12 \pi r^2 = \tfrac{L^2}{2\pi}$. Với $L = 100$ m, ta được khoảng $1591.55\ \text{m}^2$, nhiều hơn hình chữ nhật tốt nhất chừng $27.3\%$ mà không tốn thêm mét dây nào.

Đến đây có một điểm tinh tế cần dừng lại. Hình chữ nhật với $x = \tfrac{L}{4}$ là tối ưu, nhưng chỉ **trong lớp các hình chữ nhật**. Khi lớp các phương án được phép rộng hơn, nghiệm cũ không còn tốt nhất. Còn nửa hình tròn có thật sự tốt nhất trong mọi hình dạng hay không lại là một câu hỏi khác. Câu trả lời là có, và nó dựa vào bất đẳng thức đẳng chu: mọi đường cong kín có độ dài $P$ bao một diện tích $A$ thỏa $4\pi A \le P^2$. Phản chiếu khu đất qua bờ biển, ta được một miền kín có chu vi $2L$ và diện tích $2S$, nên $4\pi(2S) \le (2L)^2$, tức là $S \le \tfrac{L^2}{2\pi}$. Nửa hình tròn đạt đúng dấu bằng. Ta không chứng minh bất đẳng thức đẳng chu ở đây. Điều cần giữ lại là cách lập luận: một phương án được gọi là tối ưu chỉ khi ta có một cận đúng cho **mọi** phương án hợp lệ và phương án đó đạt cận ấy.

Bài học đầu tiên của môn học nằm gọn trong câu chuyện này. Trước khi giải, phải viết rõ ba thứ: được chọn cái gì (hình dạng của đường biên), muốn gì (diện tích lớn nhất) và bị giới hạn bởi điều gì (độ dài dây). Đổi một trong ba thứ, chẳng hạn bắt dây phải rào kín cả bốn phía, bài toán đã khác hẳn.

## 2. Dạng tổng quát của một bài toán tối ưu

Sách dùng một cách viết chung cho mọi bài toán tối ưu:

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

Khi không có ràng buộc nào ($m = p = 0$), ta nói bài toán **không ràng buộc**. Trong dạng chuẩn này, vế phải của mọi ràng buộc đều bằng 0. Điều đó luôn sắp xếp được: ràng buộc $g(x) \le b$ được viết thành $g(x) - b \le 0$, còn ràng buộc $g(x) \ge 0$ được viết thành $-g(x) \le 0$. Bài toán Dido trong lớp hình chữ nhật, chẳng hạn, có biến $x$, hàm mục tiêu $f_0(x) = -x(L - 2x)$ (dấu trừ vì ta muốn diện tích lớn nhất) và hai ràng buộc $-x \le 0$, $x - \tfrac{L}{2} \le 0$.

Một bài toán còn chứa những đại lượng không phải biến, chẳng hạn độ dài $L$ trong bài toán Dido. Chúng là **dữ liệu**, hay tham số của bài toán, được cố định trước khi giải. Phân biệt biến với dữ liệu là việc đầu tiên khi đọc một mô hình. Trong học máy, sự phân biệt này có khi bị đảo ngược theo ngữ cảnh: lúc huấn luyện, trọng số $w$ là biến và dữ liệu huấn luyện là cố định, còn lúc dự đoán, $w$ đã cố định và đầu vào mới là thứ thay đổi.

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

Định nghĩa này trông có vẻ phụ, nhưng nó gắn với một câu hỏi rất thực tế: khi nào một thuật toán được phép dừng? Nếu biết một cận dưới $\ell \le p^\star$, chẳng hạn từ một lập luận như bất đẳng thức đẳng chu ở trên, và biết một điểm khả thi $x$ có $f_0(x) - \ell \le \varepsilon$, thì $x$ chắc chắn là $\varepsilon$-gần tối ưu, dù ta không biết chính xác $p^\star$. Ý tưởng "kẹp" $p^\star$ giữa một giá trị đạt được và một cận dưới chứng minh được sẽ trở thành trung tâm của chương đối ngẫu Lagrange.

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

Hãy xét bài toán khớp một hằng số $c$ với ba số liệu $2, 4, 6$ (ví dụ trong slide Bài 01 của học phần):

$$
\min_c\ (c - 2)^2 + (c - 4)^2 + (c - 6)^2 .
$$

Đạo hàm bằng $2(c-2) + 2(c-4) + 2(c-6)$, tức $6c - 24$, triệt tiêu tại $c = 4$, trung bình của ba số, và giá trị tối ưu là $4 + 0 + 4 = 8$. Bây giờ thêm ràng buộc $c \le 3$. Nghiệm không ràng buộc $c = 4$ không còn khả thi, và trên miền $c \le 3$ đạo hàm $6c - 24$ luôn âm, nên hàm giảm khi $c$ tăng. Nghiệm mới là $c^\star = 3$ với giá trị $1 + 1 + 9 = 11$. Ràng buộc $c \le 3$ chặt tại nghiệm, và nó thật sự làm thay đổi nghiệm. Ngược lại, nếu ràng buộc là $c \le 5$ thì nghiệm vẫn là $c = 4$, ràng buộc không chặt, và bỏ nó đi cũng chẳng sao.

Một ràng buộc là **thừa** nếu bỏ nó đi không làm thay đổi miền khả thi. Chẳng hạn trong hệ $x \le 1$ và $x \le 2$, ràng buộc thứ hai thừa. Cần phân biệt hai ý: ràng buộc không chặt tại nghiệm vẫn có thể không thừa, vì nó vẫn cắt bỏ một phần miền khả thi ở chỗ khác.

Cuối cùng, nếu hàm mục tiêu bằng 0 với mọi $x$, thì giá trị tối ưu chỉ có thể là $0$ (khi miền khả thi khác rỗng) hoặc $+\infty$ (khi miền khả thi rỗng). Ta gọi đó là **bài toán khả thi** và viết

$$
\begin{aligned}
\text{find}\quad & x\\
\text{subject to}\quad & f_i(x) \le 0,\ i = 1, \ldots, m, \quad h_i(x) = 0,\ i = 1, \ldots, p.
\end{aligned}
$$

Bài toán khả thi hỏi hai việc: các ràng buộc có mâu thuẫn nhau không, và nếu không thì chỉ ra một điểm thỏa chúng. Nghe đơn giản, nhưng trong thực tế nhiều thuật toán phải giải một bài toán khả thi trước rồi mới bắt đầu cực tiểu hóa.

## 7. Bài toán cực đại

Sách thống nhất dùng bài toán cực tiểu. Muốn cực đại $f_0(x)$, ta cực tiểu $-f_0(x)$ trên cùng miền khả thi. Hai bài toán có cùng tập nghiệm, còn giá trị tối ưu đổi dấu: nếu $p^\star_{\min}$ là giá trị tối ưu của bài toán cực tiểu $-f_0$, thì bài toán cực đại $f_0$ có giá trị tối ưu $-p^\star_{\min}$. Trong bài toán cực đại, sách định nghĩa $p^\star = \sup\{f_0(x) : x \text{ khả thi}\}$, và hàm mục tiêu thường được gọi là hàm lợi ích thay vì hàm chi phí. Bài toán Dido ở mục 1 chính là một bài toán cực đại được viết lại thành cực tiểu bằng cách đổi dấu diện tích.

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

**Câu 3.** Trong bài toán Dido, nếu bờ biển không thẳng mà là một góc vuông (khu đất nằm ở góc giữa hai bờ vuông góc nhau, và dây không cần rào dọc hai bờ), bạn dự đoán hình dạng tối ưu là gì? Hãy dùng ý tưởng phản chiếu ở mục 1 để kiểm tra dự đoán.

<details><summary>Xem lời giải thích</summary>

Phản chiếu khu đất qua cả hai bờ, ta được một miền kín gồm bốn bản sao, có chu vi $4L$ và diện tích $4S$. Bất đẳng thức đẳng chu cho $4\pi(4S) \le (4L)^2$, tức là $S \le \tfrac{L^2}{\pi}$. Dấu bằng xảy ra khi miền phản chiếu là một hình tròn, nghĩa là khu đất là một phần tư hình tròn có tâm ở góc. Thật vậy, với dây dài $L = \tfrac{\pi r}{2}$, phần tư hình tròn có diện tích $\tfrac{\pi r^2}{4} = \tfrac{L^2}{\pi}$. Lập luận này cũng cho thấy một kỹ thuật đáng nhớ: biến bài toán mới về bài toán đã biết lời giải bằng một phép đối xứng.

</details>

**Câu 4.** Tìm một bài toán khả thi, bị chặn dưới, có nghiệm, nhưng tập tối ưu có vô số điểm.

<details><summary>Xem lời giải thích</summary>

Bài toán $\min\ 0$ với $-1 \le x \le 1$ có mọi điểm khả thi đều tối ưu. Một ví dụ ít "giả tạo" hơn là $\min\ \max\{0,\ |x| - 1\}$ trên $\mathbb{R}$: hàm bằng 0 trên cả đoạn $[-1, 1]$ và dương bên ngoài, nên tập tối ưu là đoạn $[-1, 1]$. Ví dụ này cũng cho thấy tập tối ưu có thể là một đoạn thẳng. Ở các chủ đề sau, ta sẽ thấy với bài toán lồi, tập tối ưu luôn là một tập lồi.

</details>

**Câu 5.** Bài toán $\min\ f_0(x)$ và bài toán $\min\ e^{f_0(x)}$, cùng miền khả thi, có cùng tập nghiệm không? Có cùng giá trị tối ưu không?

<details><summary>Xem lời giải thích</summary>

Cùng tập nghiệm, vì hàm $u \mapsto e^u$ tăng ngặt nên thứ tự giữa các giá trị được giữ nguyên: $f_0(x) \le f_0(y)$ khi và chỉ khi $e^{f_0(x)} \le e^{f_0(y)}$. Giá trị tối ưu thì khác nhau, liên hệ bởi $p^\star_2 = e^{p^\star_1}$ khi $p^\star_1$ hữu hạn. Đây là ví dụ về hai bài toán **tương đương** nhưng không **giống nhau**. Sách dùng phép biến đổi kiểu này rất thường xuyên, chẳng hạn thay việc cực tiểu $\|Ax - b\|_2$ bằng cực tiểu $\|Ax - b\|_2^2$ để có hàm khả vi.

</details>

## 10. Bài tập tự luyện

::: exercise 1. Khu đất ven bờ có giới hạn chiều sâu
Dùng mô hình hình chữ nhật ở mục 1 với $L = 60$ m, nhưng thêm điều kiện chiều sâu $x \le 10$ m. Viết bài toán dưới dạng chuẩn, tìm nghiệm và cho biết ràng buộc nào chặt. Tính đạo hàm của diện tích tại nghiệm và giải thích vì sao không thể chỉ giải phương trình đạo hàm bằng 0.
:::

::: hint
Trước tiên tìm nghiệm khi chưa có điều kiện $x \le 10$, rồi xem nghiệm đó có thỏa điều kiện mới không.
:::

::: solution
Diện tích là $S(x) = x(60 - 2x)$, và dạng chuẩn là cực tiểu $-x(60 - 2x)$ với các ràng buộc $-x \le 0$, $x - 30 \le 0$, $x - 10 \le 0$ (ràng buộc $x \le 30$ thừa khi đã có $x \le 10$). Không có điều kiện mới, nghiệm là $x = 15$, nhưng $15 > 10$ nên nó không còn khả thi. Đạo hàm $S'(x) = 60 - 4x$ dương trên $[0, 10]$, nên diện tích tăng khi $x$ tăng, và nghiệm là $x^\star = 10$, $y^\star = 40$, diện tích $400\ 	ext{m}^2$. Ràng buộc $x \le 10$ chặt. Tại nghiệm $S'(10) = 20 
e 0$: đạo hàm không triệt tiêu vì nghiệm nằm trên biên, nơi ta muốn đi tiếp theo hướng tăng diện tích nhưng ràng buộc không cho phép.
:::

::: exercise 2. Xác định p⋆ và tập tối ưu
Với mỗi bài toán sau, cho biết miền khả thi, giá trị tối ưu và tập tối ưu (nếu có): (a) $\min\ (x-5)^2$ với $1 \le x \le 3$, (b) $\min\ (x+1)^2$ với $-1 < x \le 2$, (c) $\min\ x$ với $x \ge 3$ và $x \le 2$, (d) $\min\ (3 - x)$ với $x \ge 1$.
:::

::: solution
(a) Miền $[1, 3]$. Hàm giảm trên miền này vì $x < 5$, nên $x^\star = 3$ và $p^\star = 4$. (b) Miền $(-1, 2]$. Mọi giá trị đều dương và $(x+1)^2 	o 0$ khi $x 	o -1^+$, chẳng hạn dãy $x_k = -1 + 	frac1k$ cho giá trị $	frac{1}{k^2}$. Vậy $p^\star = 0$ nhưng không đạt, tập tối ưu rỗng. (c) Không có $x$ nào vừa $\ge 3$ vừa $\le 2$, nên bài toán bất khả thi và $p^\star = +\infty$. (d) Dãy $x_k = k$ cho giá trị $3 - k 	o -\infty$, nên $p^\star = -\infty$, bài toán không bị chặn dưới.
:::

::: exercise 3. Viết lại về dạng chuẩn
Đưa bài toán sau về dạng chuẩn của sách và đếm số ràng buộc bất đẳng thức, đẳng thức: cực đại $3x_1 + 2x_2$ với $2x_1 + x_2 \le 10$, $x_1 + 2x_2 \le 8$, $x_1 \ge 0$, $x_2 \ge 0$.
:::

::: solution
Cực tiểu $f_0(x) = -3x_1 - 2x_2$ với bốn ràng buộc bất đẳng thức $2x_1 + x_2 - 10 \le 0$, $x_1 + 2x_2 - 8 \le 0$, $-x_1 \le 0$, $-x_2 \le 0$, và không có ràng buộc đẳng thức. Giá trị tối ưu của bài toán cực đại ban đầu bằng $-p^\star$ của bài toán vừa viết. (Đây là bài toán phân bổ thời gian chạy hai tác vụ trong slide Bài 01. Nghiệm là $(4, 2)$ với lợi ích 16, và chủ đề tiếp theo giải thích vì sao.)
:::

## Tóm tắt

Một bài toán tối ưu gồm biến tối ưu, hàm mục tiêu và các ràng buộc. Những đại lượng còn lại là dữ liệu, được cố định khi giải. Miền khả thi là tập các lựa chọn hợp lệ, và việc nới rộng hay thu hẹp nó có thể thay đổi hoàn toàn nghiệm, như câu chuyện về hình chữ nhật và nửa hình tròn.

Giá trị tối ưu $p^\star$ được định nghĩa bằng infimum, nên luôn tồn tại nếu cho phép $\pm\infty$. Nghiệm tối ưu là điểm khả thi đạt đúng $p^\star$, và có thể không tồn tại dù $p^\star$ hữu hạn. Tối ưu cục bộ chỉ so với các điểm khả thi ở gần, nên có thể khác tối ưu toàn cục. Ràng buộc chặt tại nghiệm là ràng buộc thật sự định hình nghiệm.

Sau trang này, bạn có thể đọc một bài toán theo đúng các thành phần của nó và nhận ra ba tình huống bất khả thi, không bị chặn dưới, không đạt nghiệm. Bạn cũng chỉ ra được ràng buộc nào chặt tại một nghiệm, và chuyển được một bài toán cực đại thành bài toán cực tiểu tương đương.

## Nguồn và đọc thêm

- S. Boyd, L. Vandenberghe, *Convex Optimization*, §1.1 (tr. 1–3) về bài toán tối ưu và ba lĩnh vực ứng dụng, §4.1.1–4.1.2 (tr. 127–130) về thuật ngữ, Ví dụ 4.1, bài toán khả thi và bài toán cực đại.
- Câu chuyện Dido, mô hình bờ biển thẳng, ví dụ khớp hằng số với ba số liệu và bài toán phân bổ thời gian chạy hai tác vụ được dùng theo slide Bài 01 và bài tập về nhà chương 01 của học phần (Nguyễn Bích Vân, IAI-UET-VNU). Slide ghi rõ phần mô hình hóa toán học là cách diễn giải về sau, không phải nội dung của đoạn thơ cổ.
- Câu hỏi về góc vuông, ví dụ $\max\{0, |x| - 1\}$ và mô phỏng một biến do người soạn bổ sung. Mọi con số đã được tính lại bằng chương trình.
