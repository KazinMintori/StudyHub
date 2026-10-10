---
course: toan-cho-ai
lecture: bai-01-nhap-mon-toi-uu
topic: tap-loi-va-bao-loi
section: topic
title: "Tập lồi, tổ hợp lồi và bao lồi"
description: "Định nghĩa tập lồi qua đoạn thẳng, cách chứng minh và bác bỏ tính lồi, tổ hợp lồi như phép trộn, bao lồi, tổ hợp lồi vô hạn và kỳ vọng, cùng các ví dụ trong học máy."
---

Ở chủ đề về tập affine, ta đã thấy công thức $\theta x_1 + (1 - \theta) x_2$ cho ra cả một đường thẳng khi $\theta$ chạy trên $\mathbb{R}$, và chỉ cho ra đoạn thẳng nối $x_1$, $x_2$ khi $\theta$ bị giới hạn trong $[0, 1]$. Tập affine được định nghĩa bằng đường thẳng. Câu hỏi tự nhiên tiếp theo là: Nếu định nghĩa một loại tập bằng **đoạn thẳng** thì sao?

Câu trả lời là khái niệm trung tâm của cả môn học. Một **tập lồi** là tập chứa trọn đoạn thẳng nối hai điểm bất kỳ của nó. Điều kiện nghe rất hiền lành, nhưng hầu hết mọi điều tốt đẹp của tối ưu lồi, từ chuyện cực tiểu cục bộ là toàn cục cho tới lý thuyết đối ngẫu, đều bắt nguồn từ nó. Trang này giúp bạn cảm được định nghĩa bằng mắt, chứng minh và bác bỏ tính lồi bằng lập luận, rồi mở rộng sang tổ hợp lồi và bao lồi.

## 1. Định nghĩa và một cách hình dung

> **Định nghĩa.** Tập $C \subseteq \mathbb{R}^n$ là **lồi** nếu với mọi $x_1, x_2 \in C$ và mọi $\theta$ thỏa $0 \le \theta \le 1$, ta có $\theta x_1 + (1 - \theta) x_2 \in C$.

Sách đưa ra một cách hình dung rất dễ nhớ: Một tập là lồi nếu **mọi điểm trong tập đều nhìn thấy mọi điểm khác** theo một đường thẳng không bị che khuất, trong đó "không bị che khuất" nghĩa là đường nhìn nằm trọn trong tập. Một căn phòng hình chữ nhật là lồi: Đứng ở góc nào cũng nhìn thấy mọi góc khác. Một căn phòng hình chữ L thì không: Đứng ở cuối một nhánh, bạn không nhìn thấy cuối nhánh kia vì bức tường ở góc trong che mất.

So sánh với tập affine, chỉ có miền của $\theta$ thay đổi: Tập affine đòi mọi $\theta \in \mathbb{R}$, còn tập lồi chỉ đòi $\theta \in [0, 1]$. Đòi ít hơn thì dễ thỏa hơn, nên **mọi tập affine đều lồi**, còn chiều ngược lại sai. Một đoạn thẳng, một hình tròn đặc hay một tam giác đặc là lồi nhưng không affine.

Hãy tự kiểm tra định nghĩa với vài hình trong mô phỏng sau. Kéo hai điểm $x, y$ sao cho cả hai nằm trong vùng tô, rồi quan sát xem đoạn nối chúng có lòi ra ngoài hay không.

<ConvexSetLab type="test" />

## 2. Bác bỏ thì dễ, chứng minh thì cần lập luận

Định nghĩa có chữ "mọi" ở hai chỗ, và điều này tạo ra một sự bất đối xứng mà bạn đã cảm thấy khi dùng mô phỏng. Muốn chứng tỏ một tập không lồi, chỉ cần **một** cặp điểm và một giá trị $\theta$ làm đoạn nối đi ra ngoài. Muốn chứng tỏ một tập lồi, phải lập luận cho **mọi** cặp điểm và mọi $\theta$, và thử bao nhiêu cặp cụ thể cũng không đủ.

**Bác bỏ.** Đường tròn $S = \{x \in \mathbb{R}^2 : x_1^2 + x_2^2 = 1\}$ không lồi. Lấy $x_1 = (1, 0)$ và $x_2 = (-1, 0)$, cả hai thuộc $S$. Với $\theta = \tfrac12$, ta được trung điểm $(0, 0)$, nhưng $0^2 + 0^2 = 0 \ne 1$, nên trung điểm không thuộc $S$. Một ví dụ khác gần với tối ưu hơn: Tập quyết định nhị phân $D = \{0, 1\}^2$, chẳng hạn "mỗi tính năng của mô hình được bật hoặc tắt", không lồi vì trung điểm $(\tfrac12, \tfrac12)$ của $(0, 0)$ và $(1, 1)$ không thuộc $D$. Các bài toán có biến nguyên hay biến nhị phân khó chính vì miền khả thi của chúng không lồi.

**Chứng minh.** Hình tròn đặc $B = \{x \in \mathbb{R}^2 : \|x\|_2 \le 1\}$ là lồi. Lấy $x_1, x_2 \in B$ bất kỳ và $\theta \in [0, 1]$ bất kỳ. Dùng bất đẳng thức tam giác và tính thuần nhất của chuẩn,

$$
\begin{aligned}
\|\theta x_1 + (1-\theta) x_2\|_2 &\le \|\theta x_1\|_2 + \|(1-\theta)x_2\|_2 \\
&= \theta \|x_1\|_2 + (1 - \theta)\|x_2\|_2 \\
&\le \theta + (1 - \theta) = 1.
\end{aligned}
$$

Bước đẳng thức ở giữa dùng $\theta \ge 0$ và $1 - \theta \ge 0$, vì $\|\alpha x\| = |\alpha|\,\|x\|$ và ta cần $|\theta| = \theta$. Nếu cho phép $\theta$ âm, chứng minh gãy ngay ở bước này, và điều đó khớp với thực tế: Hình tròn không chứa cả đường thẳng qua hai điểm của nó.

Đường tròn và hình tròn đặc chỉ khác nhau ở dấu "$=$" và "$\le$", nhưng một tập không lồi còn tập kia lồi. Khi đọc một ràng buộc trong bài toán tối ưu, hãy chú ý đến từng dấu như vậy.

::: warning Một cái bẫy tinh tế: Biên chỉ có một phần
Xét một ví dụ điển hình cần lưu tâm: Một hình vuông chứa **một số** điểm biên nhưng không chứa các điểm biên khác thì không lồi. Chẳng hạn lấy hình vuông mở $(0, 1)^2$ rồi thêm vào đúng hai điểm $(0.2, 0)$ và $(0.8, 0)$ trên cạnh dưới. Hai điểm này thuộc tập, nhưng trung điểm $(0.5, 0)$ của chúng nằm trên cạnh dưới mà không được thêm vào, nên không thuộc tập. Ngoài "hình dạng nhìn thấy", tính lồi còn phụ thuộc vào việc biên được giữ lại như thế nào.
:::

## 3. Tổ hợp lồi: Phép trộn

Cũng như với tập affine, ta mở rộng từ hai điểm sang nhiều điểm.

> **Định nghĩa.** Một điểm $y$ được gọi là một **tổ hợp lồi** của $k$ điểm $x_1, \ldots, x_k$ nếu nó có dạng:
> $$
> y = \sum_{i=1}^k \theta_i x_i = \theta_1 x_1 + \theta_2 x_2 + \dots + \theta_k x_k
> $$
> trong đó các trọng số thỏa mãn đồng thời hai điều kiện:
> $$
> \sum_{i=1}^k \theta_i = \theta_1 + \theta_2 + \dots + \theta_k = 1 \quad \text{và} \quad \theta_i \ge 0, \; \forall i = 1, \dots, k.
> $$

So với tổ hợp affine, ta thêm đúng một điều kiện: Các trọng số không được mang giá trị âm. Hai điều kiện "tổng bằng 1" và "không âm" chính là hai điều kiện cấu thành một **phân phối xác suất** trên $k$ điểm. Ở góc độ trực quan vật lý và đời sống, tổ hợp lồi bản chất là một **phép pha trộn tỉ lệ (hỗn hợp)**, trong đó $\theta_i$ là tỉ lệ phần trăm của từng thành phần $x_i$:

$$
\underbrace{\sum_{i=1}^k \theta_i x_i}_{\text{điểm pha trộn}} \quad \text{với} \quad \underbrace{\sum_{i=1}^k \theta_i = 1}_{\text{tổng tỉ lệ bằng } 100\%} \quad \text{và} \quad \underbrace{\theta_i \ge 0}_{\text{không có trọng số âm}}
$$

Chẳng hạn khi pha 30% cà phê với 70% sữa, mỗi thành phần được mô tả bằng một vector đặc trưng (độ đắng, độ ngọt, độ béo), vector đặc trưng của thức uống sau khi pha chính là $0.3\,x_{\text{cà phê}} + 0.7\,x_{\text{sữa}}$ (với giả thiết đơn giản hóa rằng các đặc tính pha trộn tuyến tính).

Một tập là lồi **khi và chỉ khi** nó chứa mọi tổ hợp lồi của các điểm thuộc tập đó. Chiều "nếu" là hiển nhiên vì đoạn thẳng nối hai điểm chính là trường hợp cơ sở $k = 2$. Chiều "chỉ nếu" được chứng minh chặt chẽ bằng phương pháp quy nạp:

::: proof Tập lồi chứa mọi tổ hợp lồi của các điểm thuộc tập
Quy nạp theo $k$. Với $k = 1, 2$, khẳng định đúng theo định nghĩa. Giả sử khẳng định đúng với $k - 1$ điểm, ta xét $y = \theta_1 x_1 + \cdots + \theta_k x_k$ với $\theta_i \ge 0$ và $\sum_{i=1}^k \theta_i = 1$. Nếu $\theta_k = 1$ thì kéo theo mọi $\theta_i$ còn lại đều bằng 0, dẫn đến $y = x_k \in C$. Nếu $\theta_k < 1$, ta viết lại $y$ dưới dạng:

$$
y = (1 - \theta_k) \underbrace{\left( \frac{\theta_1}{1 - \theta_k} x_1 + \cdots + \frac{\theta_{k-1}}{1 - \theta_k} x_{k-1} \right)}_{z} + \theta_k x_k .
$$

Các hệ số trong ngoặc không âm và cộng lại bằng 1, nên $z$ là tổ hợp lồi của $k - 1$ điểm và thuộc $C$ theo giả thiết quy nạp. Khi đó $y$ là tổ hợp lồi của hai điểm $z, x_k \in C$ với trọng số $1 - \theta_k$ và $\theta_k$, cả hai thuộc $[0, 1]$. Vậy $y \in C$.
:::

So với chứng minh cho tập affine, có thêm một việc phải kiểm tra: Các hệ số mới vẫn không âm. Điều này đúng vì ta chia các số không âm cho số dương $1 - \theta_k$.

## 4. Bao lồi

> **Định nghĩa.** **Bao lồi** của tập $C$, ký hiệu $\operatorname{conv} C$, là tập mọi tổ hợp lồi của các điểm thuộc $C$:
> $$
> \operatorname{conv} C = \left\{\sum_{i=1}^k \theta_i x_i : X_i \in C, \ \sum_{i=1}^k \theta_i = 1, \ \theta_i \ge 0, \ k \ge 1\right\}.
> $$

Đúng như tên gọi, bao lồi luôn là một tập lồi, và nó là **tập lồi nhỏ nhất chứa $C$**: Nếu $B$ là tập lồi bất kỳ chứa $C$, thì $\operatorname{conv} C \subseteq B$. Lý do là $B$ lồi nên chứa mọi tổ hợp lồi của các điểm của nó, trong đó có các điểm của $C$. Nói cách khác, bao lồi của $C$ chính bằng giao của **mọi** tập lồi chứa $C$.

Với một tập hữu hạn điểm trong mặt phẳng, bao lồi có một hình ảnh rất cụ thể. Hãy tưởng tượng cắm một chiếc đinh tại mỗi điểm rồi thả một sợi dây chun căng rộng bao quanh tất cả. Khi dây chun co lại, nó ôm lấy một đa giác lồi, và đa giác đó cùng phần bên trong của nó là bao lồi. Những chiếc đinh chạm dây chun là đỉnh của đa giác, còn những chiếc nằm bên trong không ảnh hưởng gì tới hình dạng cuối cùng.

<ConvexSetLab type="hull" />

Bao lồi của một hình không lồi thì "lấp đầy" các chỗ lõm. Bao lồi của hình trăng khuyết trong mô phỏng đầu trang là cả hình tròn lớn, bao lồi của ngôi sao năm cánh là ngũ giác nối năm đầu cánh, còn bao lồi của hai hình tròn rời nhau là hình "viên thuốc" gồm hai hình tròn và dải nối giữa chúng.

::: tip Thử trả lời trước khi đọc tiếp
Cho ba điểm $A = (0, 0)$, $B = (4, 0)$, $C = (0, 4)$ và điểm $P = (1, 2)$. Điểm $P$ có thuộc $\operatorname{conv}\{A, B, C\}$ không? Nếu có, hãy chỉ ra các trọng số.
:::

<details><summary>Xem lời giải thích</summary>

Cần $\theta_A, \theta_B, \theta_C \ge 0$ với tổng bằng 1 và $\theta_A A + \theta_B B + \theta_C C = P$. Tọa độ thứ nhất cho $4\theta_B = 1$, tọa độ thứ hai cho $4\theta_C = 2$. Vậy $\theta_B = \tfrac14$, $\theta_C = \tfrac12$ và $\theta_A = 1 - \tfrac14 - \tfrac12 = \tfrac14$. Cả ba đều không âm, nên $P$ thuộc tam giác. Nếu một trọng số tính ra âm, điểm đó vẫn là tổ hợp affine của ba đỉnh nhưng nằm ngoài tam giác, như ta đã thấy ở chủ đề về tập affine.

</details>

Một kết quả đẹp và sâu sắc trong hình học lồi là **Định lý Carathéodory**: Trong không gian $\mathbb{R}^n$, mỗi điểm thuộc $\operatorname{conv} C$ đều có thể biểu diễn như một tổ hợp lồi của **không quá $n + 1$** điểm của $C$. Chẳng hạn trong mặt phẳng $\mathbb{R}^2$, mỗi điểm thuộc bao lồi của một nghìn điểm đều nằm trọn trong một tam giác có ba đỉnh lấy từ chính nghìn điểm đó. Con số $n + 1$ là tối ưu và không thể giảm bớt, vì trọng tâm của một tam giác không thể là tổ hợp lồi của chỉ hai đỉnh.

## 5. Tổ hợp lồi vô hạn và kỳ vọng

Ý tưởng tổ hợp lồi không dừng lại ở hữu hạn điểm mà mở rộng tự nhiên sang trường hợp liên tục và vô hạn:

- Với chuỗi vô hạn các trọng số $\theta_1, \theta_2, \ldots \ge 0$ có tổng $\sum_{i=1}^{\infty} \theta_i = 1$ và các điểm $x_1, x_2, \ldots \in C$, ta có $\sum_{i=1}^{\infty} \theta_i x_i \in C$, miễn là chuỗi hội tụ.
- Với một hàm mật độ xác suất $p(x) \ge 0$ trên $C$ thỏa mãn $\int_C p(x)\,dx = 1$, ta có $\int_C p(x)\, x\, dx \in C$, nếu tích phân tồn tại.
- Dạng tổng quát nhất trong lý thuyết xác suất: Nếu $x$ là một vector ngẫu nhiên nhận giá trị trong $C$ với xác suất 1, thì **kỳ vọng $\mathbb{E}[x]$ cũng thuộc $C$**.

Dạng thứ ba bao gồm tất cả các dạng còn lại. Chẳng hạn nếu $x$ chỉ nhận hai giá trị $x_1$ và $x_2$ với xác suất $\theta$ và $1 - \theta$, thì $\mathbb{E}\,x = \theta x_1 + (1 - \theta) x_2$, đúng là định nghĩa ban đầu. Như vậy tập lồi là những tập **khép kín đối với phép lấy trung bình**: Lấy trung bình theo bất kỳ cách nào của những điểm trong tập, kết quả vẫn ở trong tập.

Cách nhìn này có những hệ quả rất thực tế:

- Tập các phân phối xác suất trên một tập hữu hạn là lồi. Trộn hai phân phối, chẳng hạn $0.3\,p + 0.7\,q$, cho ra một phân phối. Đó là cơ sở của các mô hình hỗn hợp trong thống kê.
- Trong huấn luyện mô hình, người ta đôi khi lấy trung bình các bộ trọng số ở nhiều bước lặp cuối thay vì dùng bước lặp cuối cùng. Nếu tham số bị ràng buộc trong một tập lồi, chẳng hạn mọi trọng số nằm trong $[-1, 1]$, thì trung bình đó vẫn thỏa ràng buộc mà không cần chiếu lại. Nếu tập ràng buộc không lồi, như tập các vector nhị phân, thì trung bình nói chung không còn hợp lệ.
- Ngược lại, khi một bài toán tự nhiên có miền không lồi, việc thay miền đó bằng bao lồi của nó là một kỹ thuật quan trọng gọi là **nới lỏng lồi**. Lecture 02 sẽ trở lại với kỹ thuật này.

## 6. Lồi theo trung điểm có đủ không?

Một tập $C$ được gọi là **lồi theo trung điểm** nếu nó chứa trung điểm $\tfrac12(a + b)$ của hai điểm bất kỳ $a, b \in C$. Tập lồi hiển nhiên lồi theo trung điểm. Chiều ngược lại thì sao?

Không đúng trong trường hợp tổng quát. Tập $\mathbb{Q}^2$ các điểm có tọa độ hữu tỉ chứa trung điểm của hai điểm bất kỳ của nó, nhưng không lồi: Đoạn nối $(0, 0)$ và $(1, 0)$ đi qua $(\tfrac{1}{\sqrt 2}, 0)$, một điểm không có tọa độ hữu tỉ. Tuy nhiên sách chỉ ra (Bài tập 2.3) rằng **nếu $C$ đóng và lồi theo trung điểm thì $C$ lồi**. Ý tưởng chứng minh như sau. Lặp lại phép lấy trung điểm nhiều lần cho ta mọi tổ hợp $\theta a + (1-\theta) b$ với $\theta$ có dạng $\tfrac{m}{2^k}$. Các số như vậy nằm dày đặc trong $[0, 1]$, nên mọi $\theta \in [0, 1]$ là giới hạn của một dãy $\tfrac{m_j}{2^{k_j}}$. Tập đóng chứa giới hạn của mọi dãy hội tụ gồm các điểm của nó, nên chứa cả $\theta a + (1-\theta) b$.

Kết quả này có ích trong thực hành: Nhiều khi kiểm tra trung điểm dễ hơn nhiều so với kiểm tra mọi $\theta$, chẳng hạn khi định nghĩa tập bằng một bất đẳng thức đóng.

## 7. Những câu hỏi để đào sâu

**Câu 1.** Giao của hai tập lồi có lồi không? Hợp của chúng thì sao? Hãy trả lời bằng một lập luận cho câu thứ nhất và một hình vẽ cụ thể cho câu thứ hai.

<details><summary>Xem lời giải thích</summary>

Giao luôn lồi. Nếu $x_1, x_2$ thuộc cả hai tập, thì đoạn nối chúng nằm trong tập thứ nhất (vì tập đó lồi) và cũng nằm trong tập thứ hai, nên nằm trong giao. Lập luận đúng cho giao của bất kỳ họ tập lồi nào, kể cả vô hạn. Hợp thì không: Hai hình tròn rời nhau trong mô phỏng đầu trang là phản ví dụ. Hệ quả cho tối ưu rất rõ: Thêm ràng buộc (lấy giao) không phá tính lồi, còn "thỏa ràng buộc này hoặc ràng buộc kia" (lấy hợp) thường phá tính lồi.

</details>

**Câu 2.** Một bạn khẳng định: "Tập $\{x \in \mathbb{R}^2 : x_1 x_2 \ge 1\}$ là lồi, vì nhìn hình thấy nó giống một miền cong lên." Bạn ấy đúng hay sai?

<details><summary>Xem lời giải thích</summary>

Sai, vì tập này gồm hai nhánh: Nhánh với $x_1, x_2 > 0$ và nhánh với $x_1, x_2 < 0$. Điểm $(1, 1)$ và $(-1, -1)$ đều thuộc tập, nhưng trung điểm $(0, 0)$ cho $0 \cdot 0 = 0 < 1$. Nếu chỉ lấy nhánh dương, $\{x \in \mathbb{R}^2_+ : x_1 x_2 \ge 1\}$, thì tập lồi (Bài tập 2.11 trong sách). Đây là lời nhắc rằng cảm giác "nhìn hình" phải đi kèm với việc xác định chính xác tập đang xét, kể cả những phần nằm ngoài khung hình bạn vẽ.

</details>

**Câu 3.** Bao lồi của bao lồi của $C$ là gì? Bao lồi có bảo toàn quan hệ chứa không, tức là $A \subseteq B$ có kéo theo $\operatorname{conv} A \subseteq \operatorname{conv} B$ không?

<details><summary>Xem lời giải thích</summary>

$\operatorname{conv}(\operatorname{conv} C) = \operatorname{conv} C$, vì $\operatorname{conv} C$ đã lồi, và bao lồi của một tập lồi là chính nó. Phép lấy bao lồi cũng bảo toàn quan hệ chứa: Nếu $A \subseteq B$ thì mọi tổ hợp lồi của các điểm thuộc $A$ cũng là tổ hợp lồi của các điểm thuộc $B$. Hai tính chất này, cùng với $C \subseteq \operatorname{conv} C$, cho thấy phép lấy bao lồi hành xử giống phép lấy bao đóng trong tô-pô. Sách cũng nhận xét một sự tương tự với bao affine, bao tuyến tính và bao nón.

</details>

**Câu 4.** Giả sử $x$ là biến ngẫu nhiên nhận giá trị trong đoạn $[0, 1]$. Không cần biết phân phối, bạn nói được gì về $\mathbb{E}\,x$? Còn nếu $x$ nhận giá trị trong tập $\{0, 1\}$ thì $\mathbb{E}\,x$ có nhất thiết thuộc $\{0, 1\}$ không?

<details><summary>Xem lời giải thích</summary>

Vì $[0, 1]$ lồi, $\mathbb{E}\,x \in [0, 1]$. Với tập $\{0, 1\}$ không lồi, kỳ vọng không nhất thiết thuộc tập: Tung đồng xu cân đối cho $\mathbb{E}\,x = \tfrac12$. Kỳ vọng chỉ chắc chắn nằm trong bao lồi của tập giá trị, ở đây là $[0, 1]$. Đây là lý do "giá trị trung bình" có thể là một giá trị mà biến không bao giờ nhận, như con số "trung bình 2.3 người mỗi hộ".

</details>

## 8. Bài tập tự luyện

::: exercise 1. Chứng minh hoặc bác bỏ
Với mỗi tập sau trong $\mathbb{R}^2$, chứng minh tập lồi hoặc chỉ ra một cặp điểm cùng một $\theta$ làm hỏng định nghĩa: (A) $\{x : |x_1| + |x_2| \le 1\}$, (b) $\{x : x_2 \ge x_1^2\}$, (c) $\{x : x_2 \le x_1^2\}$, (d) $\{x : \max\{x_1, x_2\} \le 1\}$.
:::

::: hint
Với (a) và (d), dùng bất đẳng thức tam giác hoặc tính chất của hàm max. Với (b), viết điều kiện của điểm trên đoạn rồi dùng $(a-b)^2 \ge 0$. Với (c), thử hai điểm đối xứng qua trục tung.
:::

::: solution
(a) Lồi. Với $x, y$ trong tập và $\theta \in [0,1]$, bất đẳng thức tam giác cho

$$
\begin{aligned}
|\theta x_1 + (1-\theta)y_1| + |\theta x_2 + (1-\theta) y_2| &\le \theta(|x_1| + |x_2|) + (1-\theta)(|y_1| + |y_2|) \\
&\le \theta + (1 - \theta) = 1.
\end{aligned}
$$

(b) Lồi. Nếu $x_2 \ge x_1^2$ và $y_2 \ge y_1^2$, thì $\theta x_2 + (1-\theta)y_2 \ge \theta x_1^2 + (1-\theta) y_1^2$, và vế phải lớn hơn hoặc bằng $(\theta x_1 + (1-\theta) y_1)^2$ vì hiệu của chúng bằng $\theta(1-\theta)(x_1 - y_1)^2 \ge 0$. (c) Không lồi. Lấy $(-1, 1)$ và $(1, 1)$, cả hai thỏa $x_2 \le x_1^2$. Trung điểm $(0, 1)$ cho $1 \le 0$, sai. (d) Lồi. Điều kiện tương đương $x_1 \le 1$ và $x_2 \le 1$, giao của hai nửa mặt phẳng.
:::

::: exercise 2. Tổ hợp lồi trong một đơn hình
Cho ba phân phối xác suất trên ba kết quả $p = (0.5, 0.3, 0.2)$, $q = (0.1, 0.1, 0.8)$ và $r = (0.2, 0.6, 0.2)$. Tính $\tfrac12 p + \tfrac14 q + \tfrac14 r$ và kiểm tra kết quả là một phân phối. Có tồn tại trọng số không âm $\alpha, \beta, \gamma$ với tổng bằng 1 sao cho $\alpha p + \beta q + \gamma r = (\tfrac13, \tfrac13, \tfrac13)$ không?
:::

::: solution
Cộng từng thành phần,

$$
\begin{aligned}
\tfrac12 p + \tfrac14 q + \tfrac14 r &= (0.25 + 0.025 + 0.05,\ 0.15 + 0.025 + 0.15,\ 0.1 + 0.2 + 0.05) \\
&= (0.325,\ 0.325,\ 0.35),
\end{aligned}
$$

các thành phần không âm và cộng lại bằng 1. Với câu hỏi thứ hai, giải hệ $0.5\alpha + 0.1\beta + 0.2\gamma = \tfrac13$, $0.3\alpha + 0.1\beta + 0.6\gamma = \tfrac13$ cùng $\alpha + \beta + \gamma = 1$. Trừ phương trình thứ nhất cho phương trình thứ hai được $0.2\alpha - 0.4\gamma = 0$, tức $\alpha = 2\gamma$. Thay vào phương trình thứ nhất với $\beta = 1 - 3\gamma$: $\gamma + 0.1 - 0.3\gamma + 0.2\gamma = \tfrac13$, nên $0.9\gamma = \tfrac{7}{30}$ và $\gamma = \tfrac{7}{27}$. Khi đó $\alpha = \tfrac{14}{27}$ và $\beta = \tfrac{6}{27}$, cả ba đều dương. Vậy phân phối đều nằm trong tam giác có ba đỉnh $p, q, r$.
:::

::: exercise 3. Bao lồi bằng giao (Bài tập 2.4 trong sách)
Chứng minh rằng bao lồi của tập $S$ bằng giao của mọi tập lồi chứa $S$.
:::

::: solution
Gọi $G$ là giao của mọi tập lồi chứa $S$. Vì $\operatorname{conv} S$ là một tập lồi chứa $S$, nó là một trong các tập đem giao, nên $G \subseteq \operatorname{conv} S$. Ngược lại, mỗi tập lồi $B \supseteq S$ chứa mọi tổ hợp lồi của các điểm thuộc $S$, nên $\operatorname{conv} S \subseteq B$. Điều này đúng với mọi $B$ đem giao, nên $\operatorname{conv} S \subseteq G$. Vậy $G = \operatorname{conv} S$. Lập luận này cũng cho thấy $G$ lồi, vì giao của các tập lồi là lồi.
:::

## Tóm tắt

Một tập lồi chứa trọn đoạn thẳng nối hai điểm bất kỳ của nó. Mọi tập affine đều lồi, nhưng tập lồi thì không nhất thiết affine. Để bác bỏ tính lồi chỉ cần một cặp điểm và một $\theta$, còn để chứng minh phải lập luận cho mọi cặp, thường bằng bất đẳng thức tam giác hoặc bằng cách viết tập thành giao của các tập lồi đã biết. Một chi tiết như dấu $=$ thay cho $\le$, hay việc giữ lại một phần biên, đủ làm một tập mất tính lồi.

Tổ hợp lồi là trung bình có trọng số với trọng số là một phân phối xác suất, và tập lồi chứa mọi tổ hợp như vậy, kể cả dạng vô hạn và kỳ vọng. Bao lồi là tập lồi nhỏ nhất chứa một tập cho trước, và với một tập hữu hạn điểm trong mặt phẳng, nó là đa giác mà sợi dây chun ôm lấy.

## Nguồn và đọc thêm

- S. Boyd, L. Vandenberghe, *Convex Optimization*, §2.1.4 (tr. 23–25), Hình 2.2 và 2.3, Bài tập 2.1, 2.3, 2.4 và 2.11.
- Định lý Carathéodory: R. T. Rockafellar, *Convex Analysis*, Princeton University Press, 1970, §17.
- Ví dụ căn phòng chữ L, pha cà phê, lấy trung bình trọng số khi huấn luyện, các câu hỏi và bài tập 1, 2 do người soạn bổ sung. Mọi con số đã được tính lại bằng chương trình.
