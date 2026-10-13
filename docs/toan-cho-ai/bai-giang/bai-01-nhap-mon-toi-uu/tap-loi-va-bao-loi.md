---
course: toan-cho-ai
lecture: bai-01-nhap-mon-toi-uu
topic: tap-loi-va-bao-loi
section: topic
title: "Tập lồi, tổ hợp lồi và bao lồi"
description: "Định nghĩa tập lồi qua đoạn thẳng, cách chứng minh và bác bỏ tính lồi, tổ hợp lồi như phép trộn, bao lồi, tổ hợp lồi vô hạn và kỳ vọng, cùng các ví dụ trong học máy."
---

Ở chủ đề về tập affine, chúng ta đã chứng kiến cách biểu thức tham số $\theta x_1 + (1 - \theta) x_2$ quét qua toàn bộ một đường thẳng vô hạn khi tham số $\theta$ nhận giá trị tùy ý trên toàn trục số thực $\mathbb{R}$. Đồng thời, biểu thức đó chỉ giới hạn trong một đoạn thẳng hữu hạn nối hai đầu mút $x_1$ và $x_2$ khi tham số $\theta$ bị chặn trong đoạn đơn vị $[0, 1]$. Tập affine đòi hỏi việc bảo toàn các đường thẳng kéo dài vô tận. Câu hỏi tự nhiên và cốt lõi đặt ra là: Điều gì sẽ xảy ra nếu ta xây dựng một cấu trúc hình học mới chỉ dựa trên các **đoạn thẳng**?

Câu trả lời cho câu hỏi đó chính là khái niệm trung tâm của toàn bộ lý thuyết tối ưu hóa hiện đại: **Tập lồi**. Một tập hợp được gọi là lồi nếu nó chứa trọn vẹn đoạn thẳng nối hai điểm bất kỳ thuộc tập hợp đó. Định nghĩa này thoạt nhìn rất mộc mạc và trực quan, nhưng lại là khởi nguồn của hầu hết các tính chất tuyệt vời của tối ưu hóa lồi: Mọi điểm cực tiểu cục bộ đều là điểm cực tiểu toàn cục, lý thuyết đối ngẫu Lagrange đạt trạng thái không có khoảng cách đối ngẫu (zero duality gap), và các thuật toán hạ gradient luôn đảm bảo hội tụ. Bài học này giúp bạn đọc làm chủ trực giác hình học, rèn luyện kỹ năng chứng minh và bác bỏ tính lồi, đồng thời mở rộng khái niệm từ tổ hợp lồi hữu hạn sang bao lồi, định lý Carathéodory và các phép trộn xác suất liên tục.

## 1. Định nghĩa và trực giác hình học: Tầm nhìn không bị che khuất

Ta bắt đầu bằng định nghĩa toán học chính xác của tập lồi trong không gian Euclid:

> **Định nghĩa.** Một tập hợp $C \subseteq \mathbb{R}^n$ được gọi là **tập lồi** nếu với mọi cặp điểm $x_1, x_2 \in C$ và với mọi hệ số $\theta \in [0, 1]$, ta luôn có:
> $$
> \theta x_1 + (1 - \theta) x_2 \in C
> $$

Về mặt hình học trực quan, ta có một cách hình dung rất tự nhiên: Một tập hợp là lồi nếu **mọi điểm nằm bên trong tập hợp đều nhìn thấy mọi điểm khác** theo một đường ngắm thẳng hoàn toàn không bị che khuất. Ở đây, "không bị che khuất" đồng nghĩa với việc toàn bộ tia sáng thẳng nối giữa hai điểm quan sát phải nằm trọn vẹn bên trong tập hợp, không bị đứt đoạn hay cắt ngang qua bất kỳ khoảng trống bên ngoài nào.

Hãy xem xét hai căn phòng kiến trúc quen thuộc để thấy rõ sự khác biệt:
- **Căn phòng hình chữ nhật lồi**: Một người đứng ở bất kỳ vị trí hay góc nào của căn phòng cũng có thể quan sát trọn vẹn bất kỳ góc nào khác, vì đoạn thẳng nối hai điểm luôn nằm bên trong phòng.
- **Căn phòng hình chữ L không lồi**: Đứng ở điểm cuối của nhánh nằm ngang, tầm nhìn của người quan sát tới điểm cuối của nhánh thẳng đứng sẽ bị góc tường vuông nhô ra ở giữa che khuất. Đoạn thẳng nối hai vị trí đó phải cắt xuyên qua bức tường và đi ra ngoài không gian căn phòng.

So sánh với định nghĩa của tập affine, sự khác biệt duy nhất nằm ở miền giá trị hợp lệ của tham số $\theta$:
- Tập affine đòi hỏi tính chất bảo toàn với **mọi $\theta \in \mathbb{R}$**.
- Tập lồi chỉ đòi hỏi tính chất bảo toàn với **$\theta \in [0, 1]$**.

Bởi vì điều kiện của tập lồi lỏng hơn rất nhiều so với tập affine ($[0, 1] \subset \mathbb{R}$), ta rút ra một định lý bao hàm căn bản: **Mọi tập affine đều là tập lồi**. Chiều ngược lại hoàn toàn không đúng: Một đoạn thẳng, một hình tròn đặc, một tam giác đặc hay một khối cầu đa chiều đều là các tập lồi nhưng tuyệt đối không phải là tập affine.

<ConvexSetLab type="test" />

## 2. Phương pháp chứng minh và bác bỏ tính lồi

Cấu trúc logic của định nghĩa tập lồi chứa hai lượng từ "với mọi" liên tiếp ($\forall x_1, x_2 \in C$ và $\forall \theta \in [0, 1]$). Điều này tạo nên một tính chất bất đối xứng sâu sắc trong phương pháp luận suy diễn toán học:
- **Để bác bỏ tính lồi của một tập hợp**: Ta chỉ cần tìm ra **duy nhất một phản ví dụ**, nghĩa là chỉ ra một cặp điểm cụ thể $x_1, x_2 \in C$ cùng một giá trị $\theta \in [0, 1]$ sao cho điểm $\theta x_1 + (1 - \theta) x_2$ văng ra khỏi tập hợp.
- **Để chứng minh tính lồi của một tập hợp**: Bắt buộc phải xây dựng một lập luận giải tích tổng quát, chứng minh rằng điều kiện lồi được thỏa mãn cho **mọi** cặp điểm tùy ý và **mọi** hệ số $\theta \in [0, 1]$.

### Bác bỏ tính lồi bằng phản ví dụ

Xem xét hai bài toán điển hình minh họa cho việc bác bỏ:

**Ví dụ 1: Đường tròn rỗng ruột.** Xét đường tròn trong mặt phẳng $\mathbb{R}^2$:

$$
S = \{x \in \mathbb{R}^2 \mid x_1^2 + x_2^2 = 1\}
$$

Tập hợp này không lồi. Chọn hai điểm đối xứng qua gốc tọa độ: Điểm $x_1 = (1, 0) \in S$ (vì $1^2 + 0^2 = 1$) và điểm $x_2 = (-1, 0) \in S$ (vì $(-1)^2 + 0^2 = 1$). Chọn hệ số $\theta = \tfrac{1}{2}$. Điểm tổ hợp tương ứng là trung điểm của đoạn thẳng:

$$
x_m = \frac{1}{2}(1, 0) + \frac{1}{2}(-1, 0) = (0, 0)
$$

Thử vào phương trình xác định tập hợp: $0^2 + 0^2 = 0 \ne 1$. Do đó trung điểm $x_m \notin S$, chứng minh rằng đường tròn không phải tập lồi.

**Ví dụ 2: Miền quyết định rời rạc trong học máy.** Xét tập hợp các biến nhị phân trong $\mathbb{R}^2$:

$$
D = \{0, 1\}^2 = \{(0, 0), (0, 1), (1, 0), (1, 1)\}
$$

Tập này thường xuất hiện khi mô hình học máy cần lựa chọn bật hoặc tắt các đặc trưng (feature selection). Tập $D$ không lồi: Điểm $(0, 0) \in D$ và điểm $(1, 1) \in D$, nhưng trung điểm $(\tfrac{1}{2}, \tfrac{1}{2})$ rõ ràng không thuộc $D$. Các bài toán tối ưu với biến nguyên hoặc biến nhị phân rất khó giải quyết trong lý thuyết độ phức tạp tính toán chính vì miền khả thi của chúng thiếu tính lồi, buộc các nhà nghiên cứu phải tìm đến kỹ thuật nới lỏng lồi.

### Chứng minh tính lồi bằng lập luận giải tích

Xét hình tròn đặc (hình cầu đóng theo chuẩn Euclid) trong $\mathbb{R}^n$:

$$
B = \{x \in \mathbb{R}^n \mid \|x\|_2 \le 1\}
$$

Ta chứng minh $B$ là tập lồi: Lấy hai điểm tùy ý $x_1, x_2 \in B$ và một hệ số bất kỳ $\theta \in [0, 1]$. Theo giả thiết, ta có $\|x_1\|_2 \le 1$ và $\|x_2\|_2 \le 1$.

Áp dụng bất đẳng thức tam giác và tính thuần nhất tuyệt đối của chuẩn vector:

$$
\begin{aligned}
&\|\theta x_1 + (1 - \theta) x_2\|_2 \le \|\theta x_1\|_2 + \|(1 - \theta) x_2\|_2\\
&\quad = |\theta|\, \|x_1\|_2 + |1 - \theta|\, \|x_2\|_2\\
&\quad = \theta \|x_1\|_2 + (1 - \theta) \|x_2\|_2\\
&\quad \le \theta(1) + (1 - \theta)(1) = 1
\end{aligned}
$$

Trong chuỗi biến đổi trên, bước triệt tiêu dấu giá trị tuyệt đối $|\theta| = \theta$ và $|1 - \theta| = 1 - \theta$ hoàn toàn dựa vào điều kiện $\theta \ge 0$ và $1 - \theta \ge 0$. Nếu $\theta$ nằm ngoài đoạn $[0, 1]$, bất đẳng thức sẽ lập tức bị phá vỡ. Vì chuẩn của điểm tổ hợp không vượt quá 1, điểm $\theta x_1 + (1 - \theta) x_2$ thuộc $B$. Vậy hình cầu đóng là tập lồi.

::: warning Cạm bẫy biên không trọn vẹn trong topo
Tính lồi của một tập hợp không chỉ phụ thuộc vào "hình dạng bao quát" mà còn phụ thuộc rất nhạy cảm vào việc biên của tập hợp được giữ lại như thế nào.

Xét hình vuông mở $U = (0, 1)^2$ trong mặt phẳng. Bây giờ ta thêm vào tập hợp này đúng hai điểm nằm trên cạnh đáy: Điểm $A = (0.2, 0)$ và điểm $B = (0.8, 0)$. Tập hợp mới $U \cup \{A, B\}$ trông có vẻ lồi, nhưng thực tế **không lồi**: Cả hai điểm $A$ và $B$ đều thuộc tập hợp, nhưng trung điểm $M = \tfrac{A + B}{2} = (0.5, 0)$ nằm trên cạnh đáy và không thuộc tập hợp (vì cạnh đáy ban đầu bị bỏ khỏi $U$). Do đó, việc giữ lại một phần biên chắp vá sẽ phá hủy hoàn toàn tính lồi.
:::

## 3. Tổ hợp lồi: Phép trộn tỷ lệ và phân phối xác suất

Tương tự như cách ta mở rộng tổ hợp affine từ hai điểm sang nhiều điểm, khái niệm đoạn thẳng cũng được tổng quát hóa một cách tự nhiên sang nhiều điểm:

> **Định nghĩa.** Cho $k$ điểm $x_1, \ldots, x_k \in \mathbb{R}^n$. Một điểm $y$ được gọi là một **tổ hợp lồi** (convex combination) của $k$ điểm đó nếu nó được biểu diễn dưới dạng:
> $$
> y = \sum_{i=1}^k \theta_i x_i = \theta_1 x_1 + \theta_2 x_2 + \dots + \theta_k x_k
> $$
> trong đó các trọng số $\theta_1, \dots, \theta_k$ thỏa mãn đồng thời hai điều kiện:
> $$
> \sum_{i=1}^k \theta_i = \theta_1 + \theta_2 + \dots + \theta_k = 1 \quad \text{và} \quad \theta_i \ge 0, \quad \forall i = 1, \dots, k
> $$

### Trực giác vật lý: Phép pha trộn thành phần

So với tổ hợp affine, tổ hợp lồi bổ sung thêm đúng một điều kiện tiên quyết: Các trọng số $\theta_i$ không được phép nhận giá trị âm.

Hai ràng buộc $\sum_{i=1}^k \theta_i = 1$ và $\theta_i \ge 0$ chính là các tiên đề định nghĩa một **phân phối xác suất rời rạc** trên $k$ điểm. Về mặt vật lý và đời sống thường ngày, tổ hợp lồi mô tả chính xác một **phép pha trộn tỷ lệ** (mixture), trong đó mỗi $\theta_i$ là tỷ lệ phần trăm đóng góp của thành phần $x_i$:

$$
\underbrace{\sum_{i=1}^k \theta_i x_i}_{\text{kết quả pha trộn}} \quad \text{với} \quad \underbrace{\sum_{i=1}^k \theta_i = 1}_{\text{tổng tỷ lệ bằng } 100\%} \quad \text{và} \quad \underbrace{\theta_i \ge 0}_{\text{không có trọng số âm}}
$$

Chẳng hạn khi một barista pha một tách cà phê sữa gồm 30% cà phê nguyên chất ($x_{\text{cà phê}}$) và 70% sữa tươi ($x_{\text{sữa}}$), đặc tính hương vị của ly nước thu được chính là tổ hợp lồi:

$$
x_{\text{thức uống}} = 0.3\, x_{\text{cà phê}} + 0.7\, x_{\text{sữa}}
$$

Vì các trọng số đều không âm và có tổng bằng 1, hương vị thu được không bao giờ vượt ra ngoài phổ hương vị vốn có của hai nguyên liệu ban đầu.

### Định lý tương đương và chứng minh quy nạp

Định lý căn bản kết nối giữa định nghĩa hai điểm và tổ hợp nhiều điểm được phát biểu như sau:

> **Định lý.** Một tập hợp $C \subseteq \mathbb{R}^n$ là tập lồi khi và chỉ khi nó chứa mọi tổ hợp lồi của một số hữu hạn các điểm bất kỳ thuộc $C$.

::: proof Chứng minh bằng phương pháp quy nạp toán học
Chiều đảo là hiển nhiên vì đoạn thẳng nối hai điểm chính là trường hợp cơ sở với $k = 2$. Ta chứng minh chiều thuận bằng phương pháp quy nạp theo số điểm $k$:

- **Cơ sở quy nạp**: Với $k = 1$, $y = 1 \cdot x_1 = x_1 \in C$. Với $k = 2$, khẳng định đúng theo chính định nghĩa tập lồi.
- **Giả thiết quy nạp**: Giả sử khẳng định đúng với mọi tổ hợp lồi của $k - 1$ điểm thuộc $C$.
- **Bước quy nạp**: Xét một tổ hợp lồi của $k$ điểm:
  $$
  y = \sum_{i=1}^k \theta_i x_i, \quad \text{với } \sum_{i=1}^k \theta_i = 1 \text{ và } \theta_i \ge 0
  $$
  Nếu $\theta_k = 1$, thì các hệ số còn lại $\theta_1 = \dots = \theta_{k-1} = 0$, suy ra $y = x_k \in C$.
  Nếu $\theta_k < 1$, ta có $1 - \theta_k > 0$. Ta tách số hạng thứ $k$ ra ngoài và viết lại $y$ dưới dạng:
  $$
  y = (1 - \theta_k) \underbrace{\left( \sum_{i=1}^{k-1} \frac{\theta_i}{1 - \theta_k} x_i \right)}_{z} + \theta_k x_k
  $$
  Hãy kiểm tra các hệ số mới $\mu_i = \tfrac{\theta_i}{1 - \theta_k}$ trong biểu thức của $z$:
  1. Vì $\theta_i \ge 0$ và $1 - \theta_k > 0$, ta có $\mu_i \ge 0$ với mọi $i = 1, \dots, k - 1$.
  2. Tổng các hệ số:
     $$
     \sum_{i=1}^{k-1} \mu_i = \sum_{i=1}^{k-1} \frac{\theta_i}{1 - \theta_k} = \frac{1}{1 - \theta_k} \sum_{i=1}^{k-1} \theta_i = \frac{1 - \theta_k}{1 - \theta_k} = 1
     $$
  Như vậy điểm $z$ là một tổ hợp lồi của $k - 1$ điểm $x_1, \dots, x_{k-1} \in C$. Theo giả thiết quy nạp, ta có $z \in C$.
  
  Cuối cùng, quan sát biểu thức tổng thể:
  $$
  y = (1 - \theta_k) z + \theta_k x_k
  $$
  Đây chính là tổ hợp lồi của hai điểm $z \in C$ và $x_k \in C$ với hai trọng số $1 - \theta_k \ge 0$ và $\theta_k \ge 0$ có tổng bằng 1. Theo định nghĩa tập lồi với $k = 2$, ta suy ra $y \in C$. Phép quy nạp hoàn tất.
:::

## 4. Bao lồi và Định lý Carathéodory

Khi một tập hợp $S$ ban đầu không có tính lồi, ta hoàn toàn có thể "lồi hóa" nó bằng cách bổ sung toàn bộ các tổ hợp lồi của các điểm thuộc $S$:

> **Định nghĩa.** **Bao lồi** (convex hull) của một tập hợp $S \subseteq \mathbb{R}^n$, ký hiệu là $\operatorname{conv} S$, là tập hợp tất cả các tổ hợp lồi của các điểm thuộc $S$:
> $$
> \operatorname{conv} S = \left\{ \sum_{i=1}^k \theta_i x_i \;\middle|\; x_i \in S, \; \sum_{i=1}^k \theta_i = 1, \; \theta_i \ge 0, \; k \ge 1 \right\}
> $$

Bao lồi luôn luôn là một tập lồi, và nó chính là **tập lồi nhỏ nhất chứa $S$**: Nếu $B$ là một tập lồi bất kỳ chứa $S$ ($S \subseteq B$), thì bắt buộc $\operatorname{conv} S \subseteq B$. Nói cách khác, bao lồi của $S$ chính bằng giao của tất cả các tập lồi chứa $S$.

### Trực giác sợi dây chun trong mặt phẳng

Đối với một tập hữu hạn các điểm trong mặt phẳng hai chiều $\mathbb{R}^2$, bao lồi có một hình ảnh cơ học rất trực quan: Hãy tưởng tượng mỗi điểm dữ liệu là một chiếc đinh đóng thẳng đứng trên mặt bàn gỗ. Ta lấy một sợi dây chun co giãn kéo căng thật rộng bao quanh toàn bộ các chiếc đinh rồi thả tay ra. Dưới lực đàn hồi, sợi dây chun co lại và ôm sát lấy chùm đinh.

Hình đa giác khép kín được tạo bởi sợi dây chun cùng toàn bộ vùng mặt phẳng bên trong chính là bao lồi $\operatorname{conv} S$. Những chiếc đinh chạm vào sợi dây chun chính là các **điểm cực biên** (đỉnh) của bao lồi, còn những chiếc đinh nằm sâu bên trong hoàn toàn không làm thay đổi hình dáng của bao lồi.

<ConvexSetLab type="hull" />

::: example Tính tọa độ trọng tâm và kiểm tra bao lồi tam giác
Trong mặt phẳng $\mathbb{R}^2$, xét tam giác tạo bởi ba đỉnh: $A = (0, 0)$, $B = (4, 0)$ và $C = (0, 4)$. Bao lồi $\operatorname{conv}\{A, B, C\}$ chính là tam giác đặc $ABC$. Ta kiểm tra hai điểm $P = (1, 2)$ và $Q = (3, 3)$:

1. **Khảo sát điểm $P = (1, 2)$**:
   Thiết lập phương trình tổ hợp:
   $$
   \theta_A (0, 0) + \theta_B (4, 0) + \theta_C (0, 4) = (1, 2)
   $$
   Cân bằng tọa độ từng thành phần:
   - Tọa độ thứ nhất: $4 \theta_B = 1 \implies \theta_B = \tfrac{1}{4}$.
   - Tọa độ thứ hai: $4 \theta_C = 2 \implies \theta_C = \tfrac{1}{2}$.
   - Tổng trọng số bằng 1: $\theta_A = 1 - \theta_B - \theta_C = 1 - \tfrac{1}{4} - \tfrac{1}{2} = \tfrac{1}{4}$.
   
   Cả ba trọng số đều thỏa mãn điều kiện không âm: $\theta_A = 0.25 \ge 0$, $\theta_B = 0.25 \ge 0$, $\theta_C = 0.5 \ge 0$. Do đó điểm $P$ nằm trọn vẹn bên trong tam giác $ABC$.
2. **Khảo sát điểm $Q = (3, 3)$**:
   Cân bằng tọa độ:
   - $4 \theta_B = 3 \implies \theta_B = \tfrac{3}{4} = 0.75$.
   - $4 \theta_C = 3 \implies \theta_C = \tfrac{3}{4} = 0.75$.
   - Trọng số thứ ba: $\theta_A = 1 - 0.75 - 0.75 = -0.5$.
   
   Vì trọng số $\theta_A = -0.5 < 0$, điểm $Q$ không thể biểu diễn dưới dạng tổ hợp lồi của ba đỉnh. Điểm $Q$ nằm ngoài tam giác (dù nó vẫn là tổ hợp affine thuộc mặt phẳng chứa tam giác).
:::

### Định lý Carathéodory: Cận trên số điểm biểu diễn

Trong định nghĩa của bao lồi, số lượng điểm $k$ có thể lớn tùy ý. Tuy nhiên, một định lý nổi tiếng và sâu sắc của Constantin Carathéodory khẳng định rằng số lượng điểm này thực chất bị chặn bởi số chiều của không gian:

> **Định lý Carathéodory.** Nếu một tập hợp $S \subseteq \mathbb{R}^n$, thì mọi điểm $x \in \operatorname{conv} S$ đều có thể biểu diễn như một tổ hợp lồi của **không quá $n + 1$** điểm thuộc $S$.

Ý nghĩa thực tiễn của định lý này là:
- Trong mặt phẳng $\mathbb{R}^2$ ($n = 2$): Dù tập $S$ chứa một triệu điểm, bất kỳ điểm nào nằm trong bao lồi của $S$ cũng chỉ cần nhiều nhất $2 + 1 = 3$ điểm của $S$ để tạo thành một tam giác bao quanh nó.
- Trong không gian ba chiều $\mathbb{R}^3$ ($n = 3$): Mọi điểm trong bao lồi đều nằm trong một tứ diện (tổ hợp của không quá 4 điểm).

Cận số $n + 1$ là tối ưu và không thể giảm bớt: Trọng tâm của một đơn hình $n$ chiều (chẳng hạn trọng tâm tam giác trong 2D) bắt buộc phải cần đúng $n + 1$ đỉnh với trọng số dương $\theta_i = \tfrac{1}{n+1}$, không thể biểu diễn bằng bất kỳ tập hợp $n$ điểm nào.

## 5. Tổ hợp lồi vô hạn, tích phân và kỳ vọng

Khái niệm tổ hợp lồi không dừng lại ở số hữu hạn các điểm mà mở rộng tự nhiên sang giải tích liên tục và lý thuyết xác suất:

1. **Chuỗi vô hạn có trọng số**: Cho dãy vô hạn các điểm $x_1, x_2, \ldots \in C$ và dãy trọng số không âm $\theta_i \ge 0$ thỏa mãn $\sum_{i=1}^\infty \theta_i = 1$. Khi đó, nếu chuỗi hội tụ thì:
   $$
   \sum_{i=1}^\infty \theta_i x_i \in C
   $$
2. **Tích phân mật độ xác suất**: Cho hàm mật độ xác suất $p(x) \ge 0$ xác định trên tập lồi $C \subseteq \mathbb{R}^n$ thỏa mãn điều kiện chuẩn hóa $\int_C p(x)\, dx = 1$. Khi đó, nếu tích phân hội tụ tuyệt đối thì:
   $$
   \int_C p(x)\, x\, dx \in C
   $$
3. **Kỳ vọng của vector ngẫu nhiên**: Dạng tổng quát nhất phát biểu rằng: Nếu $X$ là một vector ngẫu nhiên nhận giá trị trong tập lồi $C$ với xác suất 1 ($\mathbb{P}(X \in C) = 1$), thì **kỳ vọng toán học của nó cũng thuộc $C$**:
   $$
   \mathbb{E}[X] \in C
   $$

Dạng phát biểu thứ ba bao hàm trọn vẹn cả trường hợp rời rạc và liên tục. Chẳng hạn, nếu biến ngẫu nhiên $X$ chỉ nhận hai giá trị $x_1$ và $x_2$ với xác suất tương ứng $\theta$ và $1 - \theta$, thì kỳ vọng $\mathbb{E}[X] = \theta x_1 + (1 - \theta) x_2$, khớp chính xác với định nghĩa đoạn thẳng ban đầu.

Như vậy, về bản chất triết học toán học, tập lồi chính là **tập hợp khép kín đối với mọi phép tính trung bình**: Dù bạn lấy trung bình các điểm trong tập theo bất kỳ quy luật phân phối xác suất nào, kết quả thu được vẫn luôn nằm trọn vẹn bên trong tập hợp đó.

### Ứng dụng trong học máy hiện đại

- **Mô hình hỗn hợp (Mixture Models)**: Phân phối hỗn hợp Gaussian (GMM) biểu diễn mật độ xác suất dưới dạng tổ hợp lồi của nhiều phân phối thành phần, theo công thức $p(x) = \sum_{k=1}^K \pi_k \mathcal{N}(x \mid \mu_k, \Sigma_k)$ với $\sum_k \pi_k = 1, \pi_k \ge 0$.
- **Lấy trung bình trọng số mô hình (Stochastic Weight Averaging - SWA & Model Soups)**: Trong huấn luyện mạng nơ-ron sâu, thay vì chỉ sử dụng trọng số tại bước lặp cuối cùng, người ta lấy trung bình cộng các điểm checkpoint dọc theo quỹ đạo tối ưu: $w_{\text{SWA}} = \tfrac{1}{T} \sum_{t=1}^T w_t$. Khi các trọng số bị ràng buộc trong một tập lồi (chẳng hạn $\|w\| \le R$), vector trọng số trung bình luôn đảm bảo thỏa mãn ràng buộc mà không cần phép chiếu phụ trợ.
- **Nới lỏng lồi (Convex Relaxation)**: Đối với các bài toán tối ưu tổ hợp có miền nghiệm rời rạc $S$ không lồi, người ta thay thế $S$ bằng bao lồi $\operatorname{conv} S$. Kỹ thuật này chuyển bài toán NP-khó thành một bài toán quy hoạch lồi giải được trong thời gian đa thức.

## 6. Tính lồi theo trung điểm và điều kiện đóng

Một câu hỏi giải tích tinh tế thường được đặt ra là: Liệu ta có thể đơn giản hóa việc kiểm tra tính lồi bằng cách chỉ kiểm tra trung điểm của hai điểm bất kỳ thay vì phải kiểm tra mọi $\theta \in [0, 1]$?

> **Định nghĩa.** Tập hợp $C$ được gọi là **lồi theo trung điểm** (midpoint convex) nếu với mọi $a, b \in C$, ta luôn có:
> $$
> \frac{a + b}{2} \in C
> $$

Rõ ràng mọi tập lồi đều lồi theo trung điểm (chỉ cần chọn $\theta = \tfrac{1}{2}$). Chiều ngược lại có luôn đúng không?

Câu trả lời là **không đúng** trong trường hợp tổng quát. Phản ví dụ kinh điển là tập hợp tất cả các điểm có tọa độ hữu tỉ $\mathbb{Q}^2$ trong mặt phẳng. Trung điểm của hai điểm hữu tỉ là một điểm hữu tỉ, do đó $\mathbb{Q}^2$ lồi theo trung điểm. Tuy nhiên $\mathbb{Q}^2$ hoàn toàn không lồi: Đoạn thẳng nối $(0, 0)$ và $(1, 0)$ đi qua điểm $(\tfrac{1}{\sqrt{2}}, 0)$ có tọa độ vô tỉ, văng ra ngoài tập hợp.

Tuy nhiên, trong thực hành tối ưu hóa, hầu hết các tập hợp khả thi đều là tập đóng (closed set). Khi đó ta có một định lý then chốt:

> **Định lý.** Nếu một tập hợp $C \subseteq \mathbb{R}^n$ là **tập đóng** và **lồi theo trung điểm**, thì $C$ là một **tập lồi**.

Ý tưởng chứng minh định lý này dựa trên phép chia đôi lặp lại: Bắt đầu từ hai đầu mút $a, b$, lấy trung điểm ta được điểm ứng với $\theta = \tfrac{1}{2}$. Lặp lại phép lấy trung điểm giữa điểm mới với các đầu mút, ta thu được mọi điểm ứng với $\theta$ có dạng phân số nhị phân hữu hạn $\tfrac{m}{2^k}$ với $0 \le m \le 2^k$. Tập các phân số nhị phân này tạo thành một tập trù mật trong đoạn $[0, 1]$. Bất kỳ số thực $\theta \in [0, 1]$ nào cũng là giới hạn của một dãy phân số nhị phân. Vì $C$ là tập đóng, nó chứa tất cả các điểm giới hạn của dãy, do đó chứa toàn bộ đoạn thẳng $\theta a + (1 - \theta) b$.

Định lý này mang lại lợi thế tính toán lớn: Trong nhiều chứng minh, kiểm tra trung điểm đại số $\tfrac{a+b}{2}$ đơn giản hơn rất nhiều so với kiểm tra tham số $\theta$ tổng quát.

## 7. Những câu hỏi để đào sâu

**Câu 1.** Giao của hai tập lồi có luôn luôn là một tập lồi không? Hợp của hai tập lồi thì sao?

<details><summary>Xem lời giải thích</summary>

Giao của hai tập lồi (và tổng quát hơn là giao của một họ tùy ý các tập lồi, kể cả vô hạn) luôn luôn là một tập lồi. Lập luận chứng minh rất sáng rõ: Nếu $x_1, x_2$ cùng thuộc giao $C_1 \cap C_2$, thì chúng thuộc cả $C_1$ và $C_2$. Do $C_1$ lồi, toàn bộ đoạn thẳng nối hai điểm nằm trong $C_1$. Do $C_2$ lồi, đoạn thẳng đó cũng nằm trong $C_2$. Do đó đoạn thẳng nằm trong phần giao.

Ngược lại, hợp của hai tập lồi nói chung **không lồi**. Một phản ví dụ trực quan là hợp của hai hình tròn rời nhau: Chọn một điểm thuộc hình tròn này và một điểm thuộc hình tròn kia, đoạn thẳng nối chúng bắt buộc phải băng qua khoảng trống ngăn cách ở giữa, do đó không nằm trong hợp. Hệ quả đối với bài toán tối ưu là: Thêm các ràng buộc đồng thời (phép giao) luôn bảo toàn tính lồi của miền khả thi, nhưng các ràng buộc dạng "hoặc điều kiện này hoặc điều kiện kia" (phép hợp) sẽ phá vỡ tính lồi.

</details>

**Câu 2.** Xét nhận định sau: "Tập hợp $S = \{x \in \mathbb{R}^2 \mid x_1 x_2 \ge 1\}$ là một tập lồi vì đồ thị của hàm số $x_2 \ge \tfrac{1}{x_1}$ là một đường cong lồi hướng lên trên." Nhận định này đúng hay sai?

<details><summary>Xem lời giải thích</summary>

Nhận định trên là sai lầm vì đã bỏ qua nhánh tọa độ âm.

Điều kiện $x_1 x_2 \ge 1$ được thỏa mãn trong hai trường hợp:
1. Nhánh dương: Miền $x_1 > 0$ và $x_2 > 0$ với $x_2 \ge \tfrac{1}{x_1}$ (góc phần tư thứ nhất).
2. Nhánh âm: Miền $x_1 < 0$ và $x_2 < 0$ với $x_2 \le \tfrac{1}{x_1}$ (góc phần tư thứ ba).

Cả hai điểm $A = (2, 2)$ và $B = (-2, -2)$ đều thuộc tập $S$ (vì $2 \cdot 2 = 4 \ge 1$ và $(-2)(-2) = 4 \ge 1$). Tuy nhiên, trung điểm của chúng là gốc tọa độ $M = (0, 0)$ cho tích $0 \cdot 0 = 0 < 1$, vi phạm điều kiện tập hợp. Chỉ khi ta giới hạn bài toán trên góc phần tư dương $\mathbb{R}^2_{++}$, tập hợp mới thực sự lồi. Đây là bài học sư phạm quan trọng: Cảm nhận trực quan qua hình vẽ nhánh đồ thị luôn phải đi kèm với việc rà soát miền xác định của toàn bộ các biến số.

</details>

**Câu 3.** Bao lồi của bao lồi của một tập hợp $S$ là gì? Phép lấy bao lồi có bảo toàn quan hệ bao hàm giữa hai tập hợp không?

<details><summary>Xem lời giải thích</summary>

Ta có:
$$
\operatorname{conv}(\operatorname{conv} S) = \operatorname{conv} S
$$
Lý do là bản thân $\operatorname{conv} S$ đã là một tập lồi, và bao lồi của một tập lồi chính là chính nó. Tính chất này thể hiện tính lũy đẳng (idempotence) của toán tử bao lồi.

Ngoài ra, phép lấy bao lồi bảo toàn quan hệ bao hàm: Nếu $A \subseteq B$, thì mọi tổ hợp lồi của các điểm thuộc $A$ cũng là tổ hợp lồi của các điểm thuộc $B$, do đó $\operatorname{conv} A \subseteq \operatorname{conv} B$. Cùng với tính chất $S \subseteq \operatorname{conv} S$, toán tử bao lồi hành xử hoàn toàn tương thích như toán tử đóng topo trong giải tích.

</details>

**Câu 4.** Giả sử một biến ngẫu nhiên $X$ nhận giá trị trong đoạn $[0, 1]$. Ta có thể kết luận gì về kỳ vọng toán học $\mathbb{E}[X]$? Nếu $X$ chỉ nhận giá trị rời rạc trong tập $\{0, 1\}$, kỳ vọng $\mathbb{E}[X]$ có bắt buộc thuộc $\{0, 1\}$ không?

<details><summary>Xem lời giải thích</summary>

Vì đoạn $[0, 1]$ là một tập lồi, theo định lý về kỳ vọng, ta luôn có $\mathbb{E}[X] \in [0, 1]$ với bất kỳ phân phối xác suất nào.

Ngược lại, tập rời rạc $\{0, 1\}$ không lồi. Do đó kỳ vọng không nhất thiết phải thuộc tập này: Chẳng hạn khi tung một đồng xu cân đối với giá trị 0 (sấp) và 1 (ngửa), kỳ vọng là $\mathbb{E}[X] = 0.5 \notin \{0, 1\}$. Kỳ vọng chỉ chắc chắn nằm trong bao lồi của tập giá trị, tức là $\operatorname{conv}\{0, 1\} = [0, 1]$. Đây là lý do vì sao trong thống kê học, giá trị trung bình của một mẫu rời rạc thường là một số thập phân mà không một cá thể nào trong mẫu thực tế sở hữu (chẳng hạn con số "trung bình mỗi hộ gia đình có 2.3 người con").

</details>

## 8. Bài tập tự luyện

::: exercise 1. Chứng minh hoặc bác bỏ tính lồi của các tập hợp
Trong không gian mặt phẳng $\mathbb{R}^2$, hãy chứng minh tập hợp là lồi hoặc chỉ ra một phản ví dụ cụ thể cho các tập hợp sau:
1. $S_1 = \{x \in \mathbb{R}^2 \mid |x_1| + |x_2| \le 1\}$
2. $S_2 = \{x \in \mathbb{R}^2 \mid x_2 \ge x_1^2\}$
3. $S_3 = \{x \in \mathbb{R}^2 \mid x_2 \le x_1^2\}$
4. $S_4 = \{x \in \mathbb{R}^2 \mid \max\{x_1, x_2\} \le 1\}$
:::

::: solution
1. **Tập $S_1$ là tập lồi**: Đây là quả cầu đóng đơn vị theo chuẩn $\ell_1$. Lấy hai điểm $x, y \in S_1$ và $\theta \in [0, 1]$. Áp dụng bất đẳng thức tam giác cho từng tọa độ:
   $$
   \begin{aligned}
   &|\theta x_1 + (1 - \theta) y_1| + |\theta x_2 + (1 - \theta) y_2| \le \theta(|x_1| + |x_2|) + (1 - \theta)(|y_1| + |y_2|)\\
   &\quad \le \theta(1) + (1 - \theta)(1) = 1
   \end{aligned}
   $$
   Do đó tổ hợp lồi thuộc $S_1$.
2. **Tập $S_2$ là tập lồi**: Lấy $x, y \in S_2$ thỏa $x_2 \ge x_1^2$ và $y_2 \ge y_1^2$. Với $\theta \in [0, 1]$:
   $$
   \theta x_2 + (1 - \theta) y_2 \ge \theta x_1^2 + (1 - \theta) y_1^2
   $$
   Mặt khác, xét hiệu:
   $$
   [\theta x_1^2 + (1 - \theta) y_1^2] - (\theta x_1 + (1 - \theta) y_1)^2 = \theta(1 - \theta)(x_1 - y_1)^2 \ge 0
   $$
   Vì $\theta \ge 0, 1 - \theta \ge 0$ và bình phương không âm, ta suy ra:
   $$
   \theta x_2 + (1 - \theta) y_2 \ge (\theta x_1 + (1 - \theta) y_1)^2
   $$
   Chứng tỏ tổ hợp lồi thuộc $S_2$.
3. **Tập $S_3$ không lồi**: Chọn $x = (-1, 1)$ và $y = (1, 1)$. Cả hai điểm đều thỏa $x_2 \le x_1^2$ (vì $1 \le (-1)^2 = 1$ và $1 \le 1^2 = 1$). Trung điểm của chúng với $\theta = 0.5$ là $m = (0, 1)$. Thử vào điều kiện: $1 \le 0^2 = 0$, mâu thuẫn. Vậy $S_3$ không lồi.
4. **Tập $S_4$ là tập lồi**: Điều kiện $\max\{x_1, x_2\} \le 1$ tương đương đồng thời với $x_1 \le 1$ và $x_2 \le 1$. Đây là giao của hai nửa mặt phẳng lồi gồm nửa mặt phẳng $H_1 = \{x \mid x_1 \le 1\}$ và nửa mặt phẳng $H_2 = \{x \mid x_2 \le 1\}$. Vì giao của hai tập lồi là tập lồi, $S_4$ là tập lồi.
:::

::: exercise 2. Tổ hợp lồi của các phân phối xác suất
Cho ba phân phối xác suất rời rạc trên ba biến cố:
$$
p = (0.5, 0.3, 0.2), \quad q = (0.1, 0.1, 0.8), \quad r = (0.2, 0.6, 0.2)
$$
1. Tính phân phối tổ hợp lồi $u = \tfrac{1}{2} p + \tfrac{1}{4} q + \tfrac{1}{4} r$ và kiểm tra xem $u$ có phải là một phân phối xác suất hợp lệ không.
2. Có tồn tại bộ ba trọng số không âm $\alpha, \beta, \gamma \ge 0$ với $\alpha + \beta + \gamma = 1$ sao cho tổ hợp $\alpha p + \beta q + \gamma r$ tạo thành phân phối đều $d = (\tfrac{1}{3}, \tfrac{1}{3}, \tfrac{1}{3})$ không?
:::

::: solution
1. Tính từng thành phần tọa độ của $u$:
   $$
   \begin{aligned}
   &u_1 = 0.5(0.5) + 0.25(0.1) + 0.25(0.2) = 0.325\\
   &u_2 = 0.5(0.3) + 0.25(0.1) + 0.25(0.6) = 0.325\\
   &u_3 = 0.5(0.2) + 0.25(0.8) + 0.25(0.2) = 0.350
   \end{aligned}
   $$
   
   Kiểm tra: Các thành phần đều không âm ($u_i \ge 0$) và tổng bằng $0.325 + 0.325 + 0.350 = 1$. Do đó $u$ là một phân phối xác suất hợp lệ.
2. Để tìm $\alpha, \beta, \gamma$, ta thiết lập hệ phương trình tuyến tính:
   $$
   \begin{aligned}
   &0.5 \alpha + 0.1 \beta + 0.2 \gamma = \frac{1}{3}\\
   &0.3 \alpha + 0.1 \beta + 0.6 \gamma = \frac{1}{3}\\
   &\alpha + \beta + \gamma = 1
   \end{aligned}
   $$
   Lấy phương trình thứ nhất trừ phương trình thứ hai:
   $$
   (0.5 - 0.3)\alpha + (0.1 - 0.1)\beta + (0.2 - 0.6)\gamma = 0 \iff 0.2 \alpha - 0.4 \gamma = 0 \iff \alpha = 2\gamma
   $$
   Thay $\beta = 1 - \alpha - \gamma = 1 - 3\gamma$ vào phương trình thứ nhất:
   $$
   0.5(2\gamma) + 0.1(1 - 3\gamma) + 0.2\gamma = \frac{1}{3}
   $$
   Rút gọn:
   $$
   \gamma + 0.1 - 0.3\gamma + 0.2\gamma = \frac{1}{3} \iff 0.9 \gamma = \frac{1}{3} - \frac{1}{10} = \frac{7}{30}
   $$
   Do đó:
   $$
   \gamma = \frac{7}{30 \times 0.9} = \frac{7}{27}
   $$
   Suy ra:
   $$
   \alpha = 2\gamma = \frac{14}{27}, \quad \beta = 1 - 3\left(\frac{7}{27}\right) = 1 - \frac{21}{27} = \frac{6}{27}
   $$
   Cả ba trọng số đều thỏa mãn điều kiện không âm: $\alpha = \tfrac{14}{27} > 0$, $\beta = \tfrac{6}{27} > 0$, $\gamma = \tfrac{7}{27} > 0$.
   
   Kết luận: Phân phối đều $d$ hoàn toàn có thể biểu diễn dưới dạng tổ hợp lồi của ba phân phối đã cho, nghĩa là $d$ nằm trọn trong tam giác xác suất sinh bởi $p, q, r$.
:::

::: exercise 3. Chứng minh bao lồi là giao của mọi tập lồi chứa tập hợp ban đầu
Cho tập hợp $S \subseteq \mathbb{R}^n$. Gọi $\mathcal{F} = \{B \subseteq \mathbb{R}^n \mid B \text{ lồi và } S \subseteq B\}$ là họ tất cả các tập lồi chứa $S$. Chứng minh rằng:
$$
\operatorname{conv} S = \bigcap_{B \in \mathcal{F}} B
$$
:::

::: solution
Đặt $G = \bigcap_{B \in \mathcal{F}} B$. Ta cần chứng minh hai chiều bao hàm:

1. **Chứng minh $G \subseteq \operatorname{conv} S$**:
   Theo định nghĩa, bao lồi $\operatorname{conv} S$ là một tập lồi và rõ ràng chứa $S$ (vì mọi $x \in S$ đều là tổ hợp lồi với $k=1, \theta_1=1$). Do đó $\operatorname{conv} S \in \mathcal{F}$. Vì $G$ là giao của toàn bộ các tập hợp thuộc họ $\mathcal{F}$, và $\operatorname{conv} S$ là một phần tử trong họ đó, ta suy ra ngay $G \subseteq \operatorname{conv} S$.
2. **Chứng minh $\operatorname{conv} S \subseteq G$**:
   Lấy một tập lồi bất kỳ $B \in \mathcal{F}$. Theo giả thiết, $S \subseteq B$. Vì $B$ là tập lồi, theo định lý về tổ hợp lồi, $B$ phải chứa mọi tổ hợp lồi của các điểm thuộc $B$, và do đó chứa mọi tổ hợp lồi của các điểm thuộc $S$. Điều này có nghĩa là $\operatorname{conv} S \subseteq B$.
   Vì khẳng định này đúng với **mọi** tập $B \in \mathcal{F}$, ta suy ra $\operatorname{conv} S \subseteq \bigcap_{B \in \mathcal{F}} B = G$.

Từ hai chiều bao hàm, ta kết luận $\operatorname{conv} S = G$. Đẳng thức này cũng chứng minh trực tiếp rằng bao lồi chính là tập lồi nhỏ nhất chứa $S$.
:::

## Tóm tắt

Một tập hợp $C \subseteq \mathbb{R}^n$ là tập lồi nếu nó chứa trọn vẹn đoạn thẳng nối hai điểm bất kỳ thuộc tập hợp đó. Mọi tập affine đều là tập lồi, nhưng chiều ngược lại không đúng. Để bác bỏ tính lồi chỉ cần một phản ví dụ gồm hai điểm và một hệ số $\theta \in [0, 1]$, trong khi để chứng minh đòi hỏi một lập luận tổng quát cho mọi điểm và mọi hệ số, thường sử dụng bất đẳng thức tam giác hoặc tính chất giao của các tập lồi.

Tổ hợp lồi là một phép bình quân gia quyền với các trọng số tạo thành một phân phối xác suất rời rạc ($\sum_i \theta_i = 1$ và $\theta_i \ge 0$). Khái niệm này mở rộng sang các phân phối liên tục và kỳ vọng toán học: Nếu một vector ngẫu nhiên nhận giá trị trong một tập lồi thì kỳ vọng của nó cũng nằm trong tập lồi đó.

Bao lồi $\operatorname{conv} S$ là tập lồi nhỏ nhất chứa $S$, bằng giao của tất cả các tập lồi chứa $S$. Theo Định lý Carathéodory, mọi điểm trong bao lồi trong không gian $n$ chiều đều có thể biểu diễn như tổ hợp lồi của không quá $n + 1$ điểm. Cuối cùng, một tập đóng có tính lồi theo trung điểm thì luôn luôn là một tập lồi trọn vẹn.

## Tài liệu tham khảo

- Stephen Boyd, Lieven Vandenberghe, *Convex Optimization*, Cambridge University Press.
- R. Tyrrell Rockafellar, *Convex Analysis*, Princeton University Press.
