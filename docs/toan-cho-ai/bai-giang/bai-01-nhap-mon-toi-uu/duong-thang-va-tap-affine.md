---
course: toan-cho-ai
lecture: bai-01-nhap-mon-toi-uu
topic: duong-thang-va-tap-affine
section: topic
title: "Đường thẳng, đoạn thẳng và tập affine"
description: "Tham số hóa đường thẳng bằng θ, tập affine, tổ hợp affine, ý nghĩa của điều kiện tổng hệ số bằng 1, cấu trúc không gian con tịnh tiến, tập nghiệm của Ax = b và bao affine."
---

Ở phổ thông, đường thẳng thường được viết dưới dạng $y = ax + b$. Cách viết ấy rất tiện để vẽ đồ thị, nhưng nó có hai nhược điểm khi ta bước sang tối ưu. Nhược điểm thứ nhất là nó không mô tả được đường thẳng đứng, vì khi đó hệ số góc không tồn tại. Nhược điểm thứ hai nghiêm trọng hơn: cách viết này gắn chặt với mặt phẳng hai chiều. Không ai viết "$y = ax + b$" cho một đường thẳng trong không gian các bộ trọng số của một mô hình có hàng triệu tham số, vậy mà trong học máy ta vẫn liên tục phải nói về những đường thẳng như thế.

Chương này cần một cách nói về đường thẳng, đoạn thẳng và "mặt phẳng" dùng được ở bất kỳ số chiều nào. Cách nói đó dựa trên một hình ảnh rất đời thường: đứng ở một điểm, nhìn về phía một điểm khác, rồi đi một quãng theo hướng ấy. Toàn bộ trang này được xây lên từ hình ảnh đó. Ta sẽ thấy nó dẫn tới khái niệm **tập affine**. Khái niệm này giải thích vì sao tập nghiệm của một hệ phương trình tuyến tính trông như một không gian con bị đẩy lệch khỏi gốc tọa độ, và vì sao điều kiện "các hệ số cộng lại bằng 1" xuất hiện ở khắp nơi trong môn học.

Để đọc trang này, bạn cần biết phép cộng vector, phép nhân vector với một số và khái niệm không gian con. Nếu "không gian con" còn mơ hồ, hãy tạm hình dung một đường thẳng hoặc một mặt phẳng đi qua gốc tọa độ. Định nghĩa chính xác sẽ được nhắc lại đúng lúc cần dùng.

## 1. Một điểm chạy trên đường thẳng

Lấy hai điểm khác nhau $x_1, x_2 \in \mathbb{R}^n$. Với mỗi số thực $\theta$, ta đặt

$$
y = \theta x_1 + (1-\theta)\,x_2 .
$$

Khi $\theta$ chạy trên toàn bộ trục số, điểm $y$ vạch ra đúng đường thẳng đi qua $x_1$ và $x_2$. Hai giá trị đặc biệt có thể kiểm tra ngay: $\theta = 0$ cho $y = x_2$, còn $\theta = 1$ cho $y = x_1$.

Công thức trên đúng nhưng chưa nói được nhiều với người đọc. Hãy gom các số hạng chứa $\theta$ lại:

$$
y = x_2 + \theta\,(x_1 - x_2).
$$

Bây giờ công thức có thể đọc thành lời. Ta xuất phát từ điểm $x_2$, đi theo vector $x_1 - x_2$ (vector chỉ từ $x_2$ sang $x_1$), và đi một quãng bằng $\theta$ lần vector đó. Như vậy $\theta$ chính là tỉ lệ quãng đường đã đi từ $x_2$ về phía $x_1$. Với $\theta = \tfrac12$ ta dừng ở trung điểm, với $\theta = \tfrac13$ ta dừng ở điểm cách $x_2$ một phần ba đoạn. Khi $\theta > 1$, ta đã đi quá $x_1$. Còn khi $\theta < 0$, ta đi lùi ra phía sau $x_2$.

Các giá trị $0 \le \theta \le 1$ cho ra **đoạn thẳng** đóng nối $x_1$ với $x_2$. Chỉ cần thu hẹp miền của $\theta$, cùng một công thức đã sinh ra một đối tượng hình học khác. Ý tưởng "giữ nguyên công thức, đổi miền của hệ số" sẽ quay lại nhiều lần trong chương: đoạn thẳng dẫn tới tập lồi, còn tia và hình quạt dẫn tới nón. Vì thế bạn nên để ý đến nó ngay từ lúc này.

::: example Đi trên đường thẳng qua hai điểm cụ thể
Chọn $x_1 = (4, 3)$ và $x_2 = (1, 1)$. Vector chỉ hướng là $x_1 - x_2 = (3, 2)$, nên mọi điểm trên đường thẳng có dạng

$$
y = (1, 1) + \theta\,(3, 2) = (1 + 3\theta,\; 1 + 2\theta).
$$

Với $\theta = \tfrac13$ ta được $y = (2, \tfrac53)$, một điểm trên đoạn và cách $x_2$ một phần ba quãng đường. Với $\theta = 2$ ta được $(7, 5)$, nằm trên phần kéo dài về phía $x_1$. Với $\theta = -1$ ta được $(-2, -1)$, nằm phía sau $x_2$.

Điểm $(10, 7)$ có thuộc đường thẳng này không? Từ tọa độ thứ nhất, $1 + 3\theta = 10$ cho $\theta = 3$. Thay $\theta = 3$ vào tọa độ thứ hai được $1 + 2\cdot 3 = 7$, khớp với điểm đã cho. Vậy $(10, 7)$ thuộc đường thẳng và ứng với $\theta = 3$. Làm tương tự với $(5, 4)$: tọa độ thứ nhất đòi $\theta = \tfrac43$, còn tọa độ thứ hai đòi $\theta = \tfrac32$. Hai đòi hỏi mâu thuẫn nhau, nên $(5, 4)$ không nằm trên đường thẳng.
:::

Mô phỏng dưới đây tái hiện ý của Hình 2.1 trong sách (tr. 22) với hai điểm vừa dùng. Bạn có thể kéo $x_1$, $x_2$ hoặc trượt $\theta$. Hãy chú ý các vạch nhỏ ghi giá trị $\theta$ dọc theo đường thẳng: chúng cách đều nhau, đúng như cách đọc "$\theta$ là tỉ lệ quãng đường".

<AffineLab type="line" />

Không có bước nào ở trên dùng đến việc $n = 2$. Với hai vector trong $\mathbb{R}^{1000}$, công thức $\theta x_1 + (1-\theta)x_2$ vẫn mô tả đường thẳng và đoạn thẳng nối chúng, dù ta không còn vẽ được. Trong học máy, người ta dùng đúng công thức này để "nhìn" một hàm mất mát nhiều triệu chiều: lấy hai bộ trọng số $w_1, w_2$ của cùng một mạng và vẽ giá trị hàm mất mát tại $\theta w_1 + (1-\theta) w_2$ khi $\theta$ chạy từ 0 đến 1. Goodfellow, Vinyals và Saxe đã dùng cách nhìn qua một lát cắt thẳng như vậy để khảo sát đường đi từ điểm khởi tạo tới điểm đã huấn luyện. Một nghiên cứu sau đó của Frankle cho thấy trên các mạng và tập dữ liệu lớn hơn, bức tranh dọc lát cắt phức tạp hơn nhiều. Điều đáng giữ lại ở đây không phải là kết luận của các nghiên cứu ấy, mà là việc một đường thẳng trong không gian tham số được mô tả hoàn toàn bằng một số thực $\theta$.

## 2. Tập affine: tập giữ trọn mọi đường thẳng của nó

Bây giờ ta đặt câu hỏi ngược lại. Thay vì bắt đầu từ hai điểm rồi vẽ đường thẳng, ta bắt đầu từ một tập hợp và hỏi nó có "khép kín" đối với việc kẻ đường thẳng hay không.

> **Định nghĩa.** Tập $C \subseteq \mathbb{R}^n$ là **tập affine** nếu với mọi $x_1, x_2 \in C$ và mọi $\theta \in \mathbb{R}$, ta có $\theta x_1 + (1-\theta)x_2 \in C$.

Nói bằng hình học, cứ chọn hai điểm khác nhau bất kỳ trong $C$ thì toàn bộ đường thẳng đi qua chúng phải nằm trong $C$, kể cả hai phần kéo dài vô hạn. Định nghĩa có hai chữ "mọi", và cả hai đều quan trọng. Chữ "mọi" thứ nhất áp lên cặp điểm: chỉ một cặp điểm vi phạm là đủ để kết luận $C$ không affine. Chữ "mọi" thứ hai áp lên $\theta$: không chỉ các điểm nằm giữa, mà cả những điểm rất xa ở hai đầu cũng phải thuộc $C$.

Vài tập quen thuộc giúp ta cảm được định nghĩa. Một đường thẳng là tập affine, và một mặt phẳng trong $\mathbb{R}^3$ cũng vậy. Toàn bộ không gian $\mathbb{R}^n$ hiển nhiên là affine. Hai trường hợp suy biến cũng thỏa định nghĩa: tập chỉ có một điểm (khi $x_1 = x_2$ thì "đường thẳng" thu lại thành chính điểm đó) và tập rỗng (không có cặp điểm nào để kiểm tra, nên điều kiện đúng một cách hiển nhiên).

Những tập sau thì không affine, và mỗi trường hợp đều có một giá trị $\theta$ cụ thể làm hỏng định nghĩa:

| Tập | Vì sao không phải tập affine |
| --- | --- |
| Đoạn thẳng $[x_1, x_2]$ với $x_1 \ne x_2$ | $\theta = 2$ cho điểm $2x_1 - x_2$, nằm ngoài đoạn |
| Tia $\{x_0 + \theta v : \theta \ge 0\}$ với $v \ne 0$ | Hai điểm $x_0$ và $x_0 + v$ thuộc tia, nhưng $\theta = 2$ trong công thức $\theta x_0 + (1-\theta)(x_0+v)$ cho $x_0 - v$, nằm ngoài tia |
| Đường tròn $x_1^2 + x_2^2 = 1$ | Đường thẳng qua $(1,0)$ và $(-1,0)$ đi qua gốc tọa độ, mà gốc không nằm trên đường tròn |
| Hợp của hai đường thẳng song song | Đường thẳng nối một điểm trên đường này với một điểm trên đường kia đi ra ngoài cả hai |

::: tip Thử trả lời trước khi đọc tiếp
Hợp của hai đường thẳng cắt nhau, chẳng hạn hai trục tọa độ trong mặt phẳng, có phải là tập affine không?
:::

<details><summary>Xem lời giải thích</summary>

Không. Lấy $(1, 0)$ trên trục hoành và $(0, 1)$ trên trục tung. Trung điểm $(\tfrac12, \tfrac12)$, ứng với $\theta = \tfrac12$, không nằm trên trục nào. Hai đường thẳng giao nhau tại một điểm chung, nhưng việc có điểm chung không giúp chúng khép kín đối với phép kẻ đường thẳng giữa hai điểm thuộc hai nhánh khác nhau.

</details>

## 3. Tổ hợp affine của nhiều điểm

Định nghĩa tập affine chỉ nói về hai điểm. Tuy nhiên, trong tính toán ta thường gặp những biểu thức có nhiều điểm hơn, chẳng hạn trọng tâm $\tfrac13(x_1 + x_2 + x_3)$ của một tam giác. Vì vậy ta mở rộng khái niệm.

> **Định nghĩa.** Một điểm có dạng $\theta_1 x_1 + \theta_2 x_2 + \cdots + \theta_k x_k$ với $\theta_1 + \theta_2 + \cdots + \theta_k = 1$ được gọi là một **tổ hợp affine** của các điểm $x_1, \ldots, x_k$.

Các hệ số $\theta_i$ ở đây được phép âm, miễn là tổng của chúng bằng 1. Viết gọn bằng ký hiệu tổng, điểm đó là $\sum_{i=1}^{k} \theta_i x_i$ với $\sum_{i=1}^{k} \theta_i = 1$. Trường hợp $k = 2$ chính là công thức $\theta x_1 + (1-\theta)x_2$ ở mục 1, vì hai hệ số $\theta$ và $1 - \theta$ cộng lại bằng 1.

Câu hỏi tự nhiên là: một tập affine, vốn chỉ được định nghĩa qua các cặp điểm, có chứa mọi tổ hợp affine của nhiều điểm hay không? Câu trả lời là có, và cách chứng minh cho thấy rõ vai trò của điều kiện tổng bằng 1.

::: proof Tập affine chứa mọi tổ hợp affine của các điểm của nó
Ta quy nạp theo số điểm $k$. Với $k = 1$, tổ hợp chỉ là $1\cdot x_1 = x_1 \in C$. Với $k = 2$, đó là định nghĩa.

Giả sử khẳng định đúng cho $k - 1$ điểm, với $k \ge 3$. Xét $y = \theta_1 x_1 + \cdots + \theta_k x_k$ với tổng các hệ số bằng 1. Không phải mọi $\theta_i$ đều bằng 1, vì nếu thế thì tổng của chúng bằng $k \ne 1$. Đánh số lại nếu cần để $\theta_k \ne 1$, rồi tách $y$ thành hai phần:

$$
y = (1 - \theta_k)\left(\frac{\theta_1}{1-\theta_k}x_1 + \cdots + \frac{\theta_{k-1}}{1-\theta_k}x_{k-1}\right) + \theta_k x_k .
$$

Các hệ số trong ngoặc cộng lại bằng $\dfrac{\theta_1 + \cdots + \theta_{k-1}}{1 - \theta_k} = \dfrac{1-\theta_k}{1-\theta_k} = 1$. Vì vậy biểu thức trong ngoặc là một tổ hợp affine của $k - 1$ điểm, và theo giả thiết quy nạp nó là một điểm $z \in C$. Khi đó $y = (1-\theta_k)z + \theta_k x_k$ là tổ hợp affine của hai điểm $z, x_k \in C$, nên $y \in C$.
:::

Điều kiện tổng bằng 1 được dùng đúng một lần, ở bước kiểm tra các hệ số trong ngoặc. Không có nó, phép chia tách trên không đưa ta về một tổ hợp affine ngắn hơn.

### 3.1 Tọa độ trọng tâm

Ba điểm không thẳng hàng trong mặt phẳng là đủ để "đi tới" mọi điểm của mặt phẳng bằng tổ hợp affine. Chính xác hơn, nếu $p_1, p_2, p_3$ không thẳng hàng thì mỗi điểm $y \in \mathbb{R}^2$ viết được duy nhất dưới dạng $y = \theta_1 p_1 + \theta_2 p_2 + \theta_3 p_3$ với $\theta_1 + \theta_2 + \theta_3 = 1$. Bộ ba $(\theta_1, \theta_2, \theta_3)$ được gọi là **tọa độ trọng tâm** (barycentric coordinates) của $y$ đối với tam giác.

::: example Tọa độ trọng tâm trong một tam giác vuông
Xét $A = (0, 0)$, $B = (4, 0)$, $C = (0, 4)$. Điểm $(1, 1)$ có tọa độ trọng tâm $(\tfrac12, \tfrac14, \tfrac14)$, vì

$$
\tfrac12(0,0) + \tfrac14(4,0) + \tfrac14(0,4) = (1, 1), \qquad \tfrac12 + \tfrac14 + \tfrac14 = 1 .
$$

Cả ba hệ số đều dương, và điểm $(1,1)$ nằm trong tam giác. Còn điểm $(3, 3)$ nằm ngoài tam giác, phía bên kia cạnh $BC$. Tọa độ trọng tâm của nó là $(-\tfrac12, \tfrac34, \tfrac34)$. Tổng vẫn bằng 1, nhưng hệ số gắn với $A$ đã âm. Hệ số âm ở $A$ cho biết điểm nằm khác phía với $A$ so với cạnh đối diện $BC$.
:::

Hãy kéo điểm màu vàng trong mô phỏng sau. Khi điểm đi qua một cạnh, đúng một hệ số đổi dấu, và đó là hệ số của đỉnh đối diện cạnh ấy. Các đường nét đứt kéo dài ba cạnh chia mặt phẳng thành bảy miền theo dấu của ba hệ số.

<AffineLab type="combination" />

Tọa độ trọng tâm có mặt cả ngoài sách toán. Trong đồ họa máy tính, khi tô màu bên trong một tam giác mà ba đỉnh có ba màu khác nhau, máy tính tính màu của mỗi điểm ảnh bằng tổ hợp ba màu ở đỉnh với chính các hệ số $\theta_1, \theta_2, \theta_3$. Điểm ảnh nằm trong tam giác thì mọi hệ số đều không âm, nên màu thu được là một "pha trộn" thực sự của ba màu.

## 4. Vì sao điều kiện lại là tổng bằng 1?

Đến đây ta đã dùng điều kiện $\sum_i \theta_i = 1$ nhiều lần mà chưa hỏi vì sao nó lại tự nhiên đến thế. Câu trả lời nằm ở sự khác nhau giữa một **điểm** và một **vector**.

Một điểm là một vị trí, chẳng hạn vị trí của Hà Nội trên bản đồ. Một vector là một độ dời, chẳng hạn "đi 100 km về phía nam". Cộng hai độ dời với nhau thì có nghĩa. Nhân một độ dời với 2 cũng có nghĩa. Thế nhưng "Hà Nội cộng Huế" thì không có nghĩa gì cả. Con số ta tính ra phụ thuộc vào việc ta đặt gốc tọa độ ở đâu, mà gốc tọa độ chỉ là một quy ước của người vẽ bản đồ, không phải một phần của địa lý.

Phép tính nào trên các điểm thì không phụ thuộc vào quy ước ấy? Giả sử ta dời gốc tọa độ, khiến mọi điểm $x_i$ được ghi thành $x_i + c$ với cùng một vector $c$. Một tổ hợp bất kỳ $\sum_i \theta_i x_i$ khi đó trở thành

$$
\sum_{i=1}^{k} \theta_i (x_i + c) = \sum_{i=1}^{k} \theta_i x_i + \Big(\sum_{i=1}^{k} \theta_i\Big) c .
$$

Nếu tổng các hệ số bằng 1 thì kết quả dời đúng một lượng $c$, giống hệt mọi điểm khác. Nghĩa là trong hệ tọa độ mới, nó vẫn chỉ cùng một vị trí như trước. Ngược lại, nếu tổng các hệ số là $s \ne 1$, kết quả dời một lượng $sc$ khác với $c$, và vị trí mà biểu thức chỉ ra thay đổi theo cách ta đặt gốc.

Nói cách khác, **tổ hợp affine là những tổ hợp có nghĩa hình học**, vì chúng không phụ thuộc vào gốc tọa độ. Trung bình có trọng số của các vị trí, như trọng tâm của một tam giác hay vị trí trung bình của một nhóm người, đều là tổ hợp affine. Còn phép cộng hai vị trí thì không phải.

Mô phỏng dưới đây cho bạn tự dời gốc $O$. Các mũi tên xuất phát từ $O$ là các vector vị trí của ba điểm, và chúng thay đổi khi $O$ di chuyển. Thế nhưng điểm màu tím, một tổ hợp affine, đứng yên. Còn điểm màu đỏ, ứng với tổ hợp có tổng hệ số khác 1, chạy theo $O$.

<AffineLab type="origin" />

Có một cách nhìn khác cho cùng hiện tượng. Mọi tổ hợp affine đều viết lại được thành "một điểm cộng với một vector":

$$
\theta_1 x_1 + \theta_2 x_2 + \cdots + \theta_k x_k = x_1 + \theta_2 (x_2 - x_1) + \cdots + \theta_k (x_k - x_1),
$$

vì $\theta_1 = 1 - \theta_2 - \cdots - \theta_k$. Hiệu hai điểm $x_i - x_1$ là một độ dời, không phụ thuộc gốc tọa độ. Do đó vế phải là "đứng ở $x_1$, rồi đi theo một tổ hợp tuyến tính của các độ dời". Phép tính này hoàn toàn có nghĩa trên bản đồ.

Ngành hình học chỉ quan tâm tới những gì không đổi khi dời gốc và khi biến đổi bởi các ánh xạ affine (mục 8) được gọi là **hình học affine**. Trong đó có khái niệm đường thẳng, tính song song và tỉ lệ độ dài trên cùng một đường thẳng (chính là $\theta$). Ngược lại, khoảng cách và góc không thuộc về hình học affine, vì một ánh xạ affine có thể kéo dãn hay làm méo chúng. Sau này, khi gặp các tính chất "đúng với mọi ánh xạ affine" như tính lồi, bạn sẽ hiểu vì sao chúng chỉ nói về đoạn thẳng và tỉ lệ, mà không nói gì về khoảng cách.

## 5. Mỗi tập affine là một không gian con được tịnh tiến

Ta đã thấy vài ví dụ tập affine: điểm, đường thẳng, mặt phẳng, toàn không gian. Danh sách đó gợi ý rằng tập affine luôn "phẳng". Kết quả sau đây biến cảm giác ấy thành một mô tả chính xác.

Nhắc lại, một **không gian con** $V \subseteq \mathbb{R}^n$ là tập khép kín với phép cộng và phép nhân với số: nếu $v_1, v_2 \in V$ và $\alpha, \beta \in \mathbb{R}$ thì $\alpha v_1 + \beta v_2 \in V$. Đặc biệt, mọi không gian con khác rỗng đều chứa vector $0$.

> **Mệnh đề.** Cho $C$ là một tập affine và $x_0$ là một điểm bất kỳ thuộc $C$. Khi đó tập
> $$V = C - x_0 = \{x - x_0 : x \in C\}$$
> là một không gian con, và $C = V + x_0 = \{v + x_0 : v \in V\}$.

Bằng lời, ta "kéo" tập $C$ về sao cho điểm $x_0$ trùng với gốc tọa độ, và thu được một không gian con. Ngược lại, $C$ chính là không gian con $V$ được tịnh tiến đi một đoạn $x_0$.

::: proof Vì sao C − x₀ là một không gian con
Lấy $v_1, v_2 \in V$ và $\alpha, \beta \in \mathbb{R}$. Theo định nghĩa của $V$, các điểm $v_1 + x_0$ và $v_2 + x_0$ thuộc $C$. Ta viết

$$
\alpha v_1 + \beta v_2 + x_0 = \alpha (v_1 + x_0) + \beta (v_2 + x_0) + (1 - \alpha - \beta)\, x_0 .
$$

Ba hệ số $\alpha$, $\beta$ và $1 - \alpha - \beta$ cộng lại bằng 1, nên vế phải là một tổ hợp affine của ba điểm thuộc $C$. Theo mục 3, nó thuộc $C$. Vì vậy $\alpha v_1 + \beta v_2 + x_0 \in C$, tức là $\alpha v_1 + \beta v_2 \in V$.
:::

Mẹo trong chứng minh đáng để ý: số hạng $(1 - \alpha - \beta)x_0$ được thêm vào chỉ để "bù" cho tổng hệ số trở về 1. Đây là một cách dùng điều kiện tổng bằng 1 mà bạn sẽ gặp lại khi làm việc với tập lồi.

Còn một chi tiết sách nói nhưng không chứng minh: không gian con $V$ không phụ thuộc vào việc chọn $x_0$. Lý do khá ngắn. Nếu chọn một điểm khác $x_0' \in C$, thì $x_0' - x_0 = u$ là một vector thuộc $V$, và

$$
C - x_0' = (C - x_0) - u = V - u = V,
$$

trong đó đẳng thức cuối đúng vì một không gian con không thay đổi khi ta dịch nó đi một vector của chính nó. Vì $V$ chỉ phụ thuộc vào $C$, ta có thể định nghĩa **số chiều của tập affine** $C$ là số chiều của $V$. Một điểm có số chiều 0, một đường thẳng có số chiều 1, một mặt phẳng có số chiều 2.

Mệnh đề cũng cho một cách nhận ra ngay khi nào tập affine là không gian con. Nếu $0 \in C$ thì chọn $x_0 = 0$, ta được $C = V$. Ngược lại, mọi không gian con đều chứa 0 và hiển nhiên là tập affine. Tóm lại, **một tập affine là không gian con khi và chỉ khi nó chứa gốc tọa độ**. Tập affine chính là không gian con "được phép đứng lệch khỏi gốc".

## 6. Tập nghiệm của hệ phương trình tuyến tính

Đến đây ta đã sẵn sàng cho ví dụ quan trọng nhất về tập affine, cũng là ví dụ xuất hiện trong gần như mọi bài toán tối ưu có ràng buộc đẳng thức.

Cho $A \in \mathbb{R}^{m \times n}$ và $b \in \mathbb{R}^m$. Tập nghiệm $C = \{x : Ax = b\}$ là một tập affine. Thật vậy, lấy $x_1, x_2 \in C$, tức là $Ax_1 = b$ và $Ax_2 = b$. Với mọi $\theta \in \mathbb{R}$,

$$
A\big(\theta x_1 + (1-\theta)x_2\big) = \theta A x_1 + (1-\theta) A x_2 = \theta b + (1-\theta) b = b .
$$

Bước cuối dùng đúng điều kiện hai hệ số cộng lại bằng 1. Nếu thay $(\theta, 1-\theta)$ bằng hai hệ số tùy ý $(\alpha, \beta)$, vế phải sẽ là $(\alpha + \beta) b$, và nó chỉ bằng $b$ khi $\alpha + \beta = 1$ hoặc $b = 0$. Đó cũng là lý do tập nghiệm của hệ **thuần nhất** $Ax = 0$ là không gian con, còn tập nghiệm của hệ $Ax = b$ với $b \ne 0$ thì không.

Không gian con gắn với $C$ là **không gian nghiệm** (null space) của $A$, ký hiệu $\mathcal{N}(A) = \{v : Av = 0\}$. Kết hợp với mục 5, ta được một điều quen thuộc từ đại số tuyến tính: nếu $x_0$ là một nghiệm riêng của $Ax = b$, thì mọi nghiệm có dạng $x_0 + v$ với $v \in \mathcal{N}(A)$. "Nghiệm tổng quát bằng nghiệm riêng cộng nghiệm tổng quát của hệ thuần nhất" thực ra là một mệnh đề hình học: tập nghiệm là không gian con $\mathcal{N}(A)$ được tịnh tiến tới $x_0$.

Chiều ngược lại cũng đúng, dù ta không chứng minh chi tiết ở đây: **mọi tập affine khác rỗng trong $\mathbb{R}^n$ đều là tập nghiệm của một hệ phương trình tuyến tính**. Ý chính như sau. Viết $C = x_0 + V$, chọn một cơ sở $a_1, \ldots, a_m$ của phần bù trực giao $V^{\perp}$ và lấy chúng làm các hàng của $A$, rồi đặt $b = Ax_0$. Khi đó $Ax = b$ đúng khi và chỉ khi $x - x_0$ vuông góc với mọi $a_i$, tức là $x - x_0 \in V$. Như vậy "tập affine" và "tập nghiệm của hệ tuyến tính" là hai cách gọi của cùng một loại đối tượng: cách thứ nhất nhìn từ hình học, cách thứ hai nhìn từ đại số.

::: example Một mặt phẳng trong không gian ba chiều
Xét phương trình $x_1 + 2x_2 + 3x_3 = 6$ trong $\mathbb{R}^3$. Điểm $x_0 = (1, 1, 1)$ là một nghiệm vì $1 + 2 + 3 = 6$. Hệ thuần nhất $x_1 + 2x_2 + 3x_3 = 0$ có không gian nghiệm hai chiều, sinh bởi $(-2, 1, 0)$ và $(-3, 0, 1)$. Bạn có thể kiểm tra từng vector: $-2 + 2 + 0 = 0$ và $-3 + 0 + 3 = 0$. Vì vậy

$$
C = \{(1,1,1) + s(-2,1,0) + t(-3,0,1) : s, t \in \mathbb{R}\}.
$$

Đây là một mặt phẳng không đi qua gốc tọa độ, song song với mặt phẳng $x_1 + 2x_2 + 3x_3 = 0$. Lấy thử $s = t = 1$ được điểm $(-4, 2, 2)$, và quả thật $-4 + 4 + 6 = 6$.
:::

Trong mặt phẳng, một phương trình $a_1 x_1 + a_2 x_2 = b$ (với $a_1, a_2$ không đồng thời bằng 0) cho một đường thẳng. Mô phỏng sau tách đường thẳng đó thành hai phần: một nghiệm riêng $x_0$ và một hướng $d$ của không gian nghiệm thuần nhất. Khi bạn đổi $b$, đường nét đứt đi qua gốc không hề nhúc nhích. Chỉ có lượng tịnh tiến $x_0$ thay đổi.

<AffineLab type="solutions" />

### 6.1 Khi dữ liệu không đủ để chọn ra một bộ tham số

Kết quả "tập nghiệm là tập affine" có một hệ quả rất cụ thể trong học máy. Giả sử ta có $m$ mẫu dữ liệu và một mô hình tuyến tính với $n$ tham số, trong đó $n > m$. Đây là tình huống "nhiều tham số hơn dữ liệu" rất thường gặp với các mô hình lớn. Gọi $X \in \mathbb{R}^{m \times n}$ là ma trận dữ liệu, mỗi hàng là một mẫu, và $y \in \mathbb{R}^m$ là nhãn. Tập các bộ tham số khớp dữ liệu hoàn toàn, $\{w : Xw = y\}$, là một tập affine. Nếu các hàng của $X$ độc lập tuyến tính thì tập này khác rỗng, có số chiều $n - m \ge 1$, nên có vô số bộ tham số cùng cho sai số huấn luyện bằng 0.

Vậy thuật toán huấn luyện sẽ chọn bộ nào? Hãy xem trường hợp nhỏ nhất: một mẫu duy nhất với đặc trưng $(1, 1)$ và nhãn $2$. Mô hình $w_1 \cdot 1 + w_2 \cdot 1$ khớp dữ liệu khi $w_1 + w_2 = 2$, tức là trên cả một đường thẳng. Chạy phương pháp gradient cho hàm mất mát $f(w) = \tfrac12 (w_1 + w_2 - 2)^2$ với bước $\eta = \tfrac14$:

$$
w^{(k+1)} = w^{(k)} - \eta\,\big(w_1^{(k)} + w_2^{(k)} - 2\big)\,(1, 1).
$$

Mỗi bước chỉ cộng thêm một bội của vector $(1, 1)$. Vì vậy, nếu xuất phát từ $w^{(0)} = (0, 0)$, mọi bước lặp đều nằm trên đường $w_1 = w_2$. Các bước đầu là $(0.5, 0.5)$ rồi $(0.75, 0.75)$, và dãy hội tụ về $(1, 1)$. Đây là giao điểm của đường $w_1 = w_2$ với tập nghiệm, cũng là nghiệm có chuẩn nhỏ nhất trong cả đường thẳng nghiệm. Nhưng nếu xuất phát từ $(2, -2)$, phần vuông góc với $(1,1)$ của điểm đầu không bao giờ bị xóa đi, và dãy hội tụ về $(3, -1)$. Đó vẫn là một nghiệm, chỉ là một nghiệm khác.

Bài học từ ví dụ nhỏ này khá sâu. Khi tập nghiệm là một tập affine nhiều chiều, hàm mất mát không đủ để quyết định mô hình cuối cùng. Thuật toán tối ưu và điểm khởi tạo cùng tham gia vào lựa chọn đó. Lập luận "mọi bước lặp nằm trong $w^{(0)} + \operatorname{span}\{\text{các hàng của } X\}$" đúng cho mọi ma trận $X$, không riêng ví dụ này, và bạn sẽ tự kiểm tra nó trong phần bài tập.

## 7. Bao affine

Với một tập $C$ bất kỳ, chưa chắc affine, ta có thể hỏi: tập affine nhỏ nhất chứa $C$ là gì? Câu trả lời được gọi là bao affine.

> **Định nghĩa.** **Bao affine** của tập $C \subseteq \mathbb{R}^n$, ký hiệu $\operatorname{aff} C$, là tập mọi tổ hợp affine của các điểm thuộc $C$:
> $$\operatorname{aff} C = \{\theta_1 x_1 + \cdots + \theta_k x_k : x_1, \ldots, x_k \in C,\ \theta_1 + \cdots + \theta_k = 1\}.$$

Bao affine là tập affine nhỏ nhất chứa $C$, theo nghĩa nếu $S$ là một tập affine bất kỳ chứa $C$ thì $\operatorname{aff} C \subseteq S$. Lý do nằm ngay ở mục 3: tập affine $S$ chứa mọi tổ hợp affine của các điểm của nó, trong đó có các điểm của $C$.

Bảng dưới đây cho vài ví dụ. Bạn nên tự giải thích từng dòng trước khi đọc cột cuối.

| Tập $C$ | $\operatorname{aff} C$ | Số chiều |
| --- | --- | --- |
| Hai điểm khác nhau | Đường thẳng qua hai điểm | 1 |
| Ba điểm không thẳng hàng trong $\mathbb{R}^3$ | Mặt phẳng qua ba điểm | 2 |
| $\{(1,1), (2,2), (3,3)\}$ | Đường thẳng $x_1 = x_2$ | 1 |
| Đường tròn đơn vị trong $\mathbb{R}^2$ | Cả mặt phẳng $\mathbb{R}^2$ | 2 |
| Ba vector đơn vị $e_1, e_2, e_3$ trong $\mathbb{R}^3$ | Mặt phẳng $x_1 + x_2 + x_3 = 1$ | 2 |

Dòng thứ tư có thể gây bất ngờ. Đường tròn là một đường cong, ta quen coi nó là đối tượng "một chiều". Nhưng không có đường thẳng nào chứa nó, nên tập affine nhỏ nhất chứa đường tròn là cả mặt phẳng. Dòng cuối cũng đáng chú ý: tập các phân phối xác suất trên ba kết quả, những vector $p$ có $p_i \ge 0$ và $p_1 + p_2 + p_3 = 1$, nằm trọn trong mặt phẳng $x_1 + x_2 + x_3 = 1$. Mặt phẳng ấy là "không gian nền" tự nhiên của nó, dù cả hai đều nằm trong $\mathbb{R}^3$.

Ý tưởng "không gian nền tự nhiên" là cầu nối sang chủ đề tiếp theo. Một hình vuông nằm phẳng trong $\mathbb{R}^3$ không có điểm trong nào nếu ta nhìn bằng con mắt của $\mathbb{R}^3$, nhưng nhìn trong mặt phẳng chứa nó thì nó có cả một miền trong rõ ràng. Bao affine cho ta đúng mặt phẳng đó.

## 8. Hàm affine: ánh xạ giữ nguyên tổ hợp affine

Có tập affine thì cũng có hàm affine. Một hàm $f : \mathbb{R}^n \to \mathbb{R}^m$ được gọi là **affine** nếu nó có dạng $f(x) = Ax + b$ với $A \in \mathbb{R}^{m \times n}$ và $b \in \mathbb{R}^m$, tức là một hàm tuyến tính cộng thêm một hằng số. Tính chất quan trọng nhất của hàm affine là nó giữ nguyên tổ hợp affine. Nếu $\sum_i \theta_i = 1$ thì

$$
f\Big(\sum_{i=1}^{k} \theta_i x_i\Big) = A\sum_{i=1}^{k} \theta_i x_i + b = \sum_{i=1}^{k} \theta_i A x_i + \Big(\sum_{i=1}^{k} \theta_i\Big) b = \sum_{i=1}^{k} \theta_i f(x_i).
$$

Một lần nữa, điều kiện tổng bằng 1 làm cho số hạng $b$ "đi qua" được dấu tổng. Với tổ hợp tuyến tính tùy ý thì đẳng thức này sai, trừ khi $b = 0$. Hệ quả trực tiếp là ảnh của một tập affine qua hàm affine lại là một tập affine, và ảnh của một đoạn thẳng là một đoạn thẳng (có thể suy biến thành một điểm), với cùng tỉ lệ $\theta$ trên đó.

Bạn sẽ gặp hàm affine ở khắp nơi trong học sâu, đôi khi dưới một cái tên gây nhầm lẫn. Tầng mà các thư viện gọi là "tầng tuyến tính" (linear layer) tính $Wx + b$. Theo định nghĩa của toán học, đó là một hàm affine, và nó chỉ là hàm tuyến tính khi độ lệch $b = 0$. Sự phân biệt này có hệ quả cụ thể: hàm tuyến tính luôn biến $0$ thành $0$, còn hàm affine thì không.

Cuối cùng, tập mức của một hàm affine nhận giá trị thực, $\{x : a^T x + c = 0\}$ với $a \ne 0$, là một tập affine có số chiều $n - 1$. Đó là **siêu phẳng**, đối tượng mà ta sẽ nghiên cứu kỹ ở một chủ đề sau. Ranh giới quyết định của một bộ phân loại tuyến tính, nơi điểm số $w^T x + b$ đổi dấu, chính là một siêu phẳng như vậy.

## 9. Những câu hỏi để đào sâu

Các câu hỏi dưới đây không cần tính toán dài. Mỗi câu nhắm vào một chỗ mà định nghĩa dễ bị hiểu lệch. Hãy tự trả lời trước khi mở phần giải thích.

**Câu 1.** Nếu chỉ cho phép $\theta \ge 0$ trong công thức $\theta x_1 + (1-\theta)x_2$, tập điểm thu được có hình dạng gì? Nó bắt đầu từ đâu và chạy về phía nào?

<details><summary>Xem lời giải thích</summary>

Viết lại thành $x_2 + \theta(x_1 - x_2)$ với $\theta \ge 0$. Ta xuất phát từ $x_2$ và chỉ được đi tới theo hướng $x_1 - x_2$. Kết quả là một tia có gốc tại $x_2$, đi qua $x_1$ (ứng với $\theta = 1$) rồi chạy mãi về phía sau $x_1$. Tia này không chứa những điểm nằm phía sau $x_2$, nên nó không phải tập affine.

</details>

**Câu 2.** Nếu tập $C$ chứa đoạn thẳng nối hai điểm bất kỳ của nó, đã đủ để $C$ là tập affine chưa? Hãy chỉ ra chỗ thiếu trong suy luận đó và đưa ra một ví dụ cho thấy kết luận sai.

<details><summary>Xem lời giải thích</summary>

Chứa đoạn thẳng chỉ bảo đảm các tổ hợp với $0 \le \theta \le 1$. Định nghĩa tập affine đòi hỏi mọi $\theta \in \mathbb{R}$. Hình tròn đặc $\{x : \|x\|_2 \le 1\}$ chứa mọi đoạn nối hai điểm của nó, nhưng đường thẳng qua $(0,0)$ và $(\tfrac12, 0)$ đi ra ngoài hình tròn, chẳng hạn tại điểm $(2, 0)$ ứng với $\theta = 4$ trong công thức $\theta(\tfrac12,0) + (1-\theta)(0,0)$. Tính chất mà bạn kia mô tả chính là tính lồi, chủ đề của một trang sau. Mọi tập affine đều lồi, nhưng điều ngược lại sai.

</details>

**Câu 3.** Tập nghiệm của hệ $x_1 + x_2 + x_3 = 1$ và $x_1 - x_3 = 0$ trong $\mathbb{R}^3$ có số chiều bằng bao nhiêu? Mô tả nó bằng một nghiệm riêng và một hướng.

<details><summary>Xem lời giải thích</summary>

Hai phương trình độc lập (ma trận hệ số có hạng 2), nên không gian nghiệm thuần nhất có số chiều $3 - 2 = 1$, và tập nghiệm là một đường thẳng. Đặt $x_1 = x_3 = s$, phương trình đầu cho $x_2 = 1 - 2s$. Vậy tập nghiệm là $\{(0, 1, 0) + s(1, -2, 1) : s \in \mathbb{R}\}$. Với $s = 2$ ta được $(2, -3, 2)$, và quả thật $2 - 3 + 2 = 1$, $2 - 2 = 0$.

</details>

**Câu 4.** Giao của hai tập affine có phải là tập affine không? Còn hợp của chúng thì sao?

<details><summary>Xem lời giải thích</summary>

Giao luôn là tập affine. Nếu $x_1, x_2$ thuộc cả hai tập, thì mỗi tập chứa toàn bộ đường thẳng qua $x_1, x_2$, nên giao cũng chứa đường thẳng đó. Lập luận này dùng được cho giao của bất kỳ họ tập affine nào, kể cả vô hạn tập. Hợp thì nói chung không phải: hai trục tọa độ trong câu hỏi ở mục 2 là một phản ví dụ. Theo ngôn ngữ đại số, giao tương ứng với việc gộp hai hệ phương trình thành một hệ lớn hơn, và tập nghiệm của hệ lớn vẫn là tập nghiệm của một hệ tuyến tính.

</details>

**Câu 5.** Xét $\mathbb{Q}^2$, tập các điểm có hai tọa độ hữu tỉ. Nó chứa trung điểm của hai điểm bất kỳ của nó, và chứa cả điểm đối xứng $2x_1 - x_2$. Có thể kết luận $\mathbb{Q}^2$ là tập affine không?

<details><summary>Xem lời giải thích</summary>

Không. Trung điểm ứng với $\theta = \tfrac12$, điểm đối xứng ứng với $\theta = 2$, và lặp lại hai phép này chỉ sinh ra những giá trị $\theta$ hữu tỉ. Định nghĩa đòi mọi $\theta$ thực. Với $x_1 = (1, 0)$, $x_2 = (0, 0)$ và $\theta = \sqrt{2}$, ta được $(\sqrt{2}, 0) \notin \mathbb{Q}^2$. Câu hỏi này cho thấy chữ "mọi $\theta \in \mathbb{R}$" trong định nghĩa không phải chi tiết hình thức: kiểm tra một số hữu hạn giá trị $\theta$ không đủ để kết luận.

</details>

**Câu 6.** Nếu một tập $C$ chứa gốc tọa độ và khép kín với phép lấy tổ hợp affine, thì $C$ có khép kín với phép cộng hai vector không?

<details><summary>Xem lời giải thích</summary>

Có. Với $x, y \in C$, tổng $x + y$ là tổ hợp affine $1\cdot x + 1\cdot y + (-1)\cdot 0$ của ba điểm $x, y, 0 \in C$, vì $1 + 1 - 1 = 1$. Tương tự, $\alpha x = \alpha x + (1-\alpha)\cdot 0$ thuộc $C$ với mọi $\alpha$. Do đó $C$ là một không gian con. Lập luận này chứng minh lại chiều "tập affine chứa gốc là không gian con" ở mục 5, theo một đường khác.

</details>

## 10. Bài tập tự luyện

::: exercise 1. Đọc vị trí trên đường thẳng
Cho $x_1 = (2, -1, 3)$ và $x_2 = (0, 1, 1)$ trong $\mathbb{R}^3$. Viết tham số hóa của đường thẳng qua hai điểm dưới dạng $x_2 + \theta(x_1 - x_2)$. Điểm $(5, -4, 6)$ có thuộc đường thẳng không? Nếu có, nó nằm trên đoạn $[x_2, x_1]$, phía sau $x_2$ hay phía trước $x_1$?
:::

::: hint
Tìm $\theta$ từ một tọa độ rồi kiểm tra hai tọa độ còn lại.
:::

::: solution
Vector chỉ hướng là $x_1 - x_2 = (2, -2, 2)$, nên mọi điểm có dạng $(2\theta,\ 1 - 2\theta,\ 1 + 2\theta)$. Tọa độ đầu cho $2\theta = 5$, tức $\theta = \tfrac52$. Kiểm tra: $1 - 2\cdot\tfrac52 = -4$ và $1 + 2\cdot\tfrac52 = 6$, khớp cả hai. Vậy điểm thuộc đường thẳng với $\theta = \tfrac52 > 1$, tức là nằm trên phần kéo dài, phía trước $x_1$ khi đi từ $x_2$ sang $x_1$.
:::

::: exercise 2. Tập nghiệm và số chiều
Cho $A = \begin{bmatrix} 1 & 1 & 0 & 0 \\ 0 & 1 & 1 & 0 \end{bmatrix}$ và $b = (2, 3)$. Tìm một nghiệm riêng của $Ax = b$, một cơ sở của $\mathcal{N}(A)$, và cho biết tập nghiệm có số chiều bao nhiêu.
:::

::: solution
Đặt $x_2 = 0$ và $x_4 = 0$, ta được $x_1 = 2$ và $x_3 = 3$, nên $x_0 = (2, 0, 3, 0)$ là một nghiệm riêng. Hệ thuần nhất cho $x_1 = -x_2$ và $x_3 = -x_2$, còn $x_4$ tùy ý. Chọn $x_2 = 1, x_4 = 0$ được $(-1, 1, -1, 0)$, chọn $x_2 = 0, x_4 = 1$ được $(0, 0, 0, 1)$. Hai vector này độc lập và sinh ra $\mathcal{N}(A)$. Tập nghiệm là $x_0 + \operatorname{span}\{(-1,1,-1,0), (0,0,0,1)\}$, một tập affine hai chiều trong $\mathbb{R}^4$. Số chiều cũng có thể suy ra từ hạng: $4 - \operatorname{rank} A = 4 - 2 = 2$.
:::

::: exercise 3. Kiểm tra tập affine qua các đường thẳng
Chứng minh rằng một tập $C$ là affine khi và chỉ khi giao của $C$ với mọi đường thẳng là một tập affine. (Bài 2.2 trong sách, phần thứ hai.)
:::

::: hint
Một chiều là hệ quả của câu 4 ở mục 9. Với chiều còn lại, hãy chọn đúng đường thẳng đi qua hai điểm của $C$ mà bạn cần kiểm tra.
:::

::: solution
Nếu $C$ affine, giao của nó với một đường thẳng $L$ là giao của hai tập affine, nên affine theo câu 4. Ngược lại, giả sử mọi giao $C \cap L$ đều affine. Lấy $x_1 \ne x_2$ thuộc $C$ và gọi $L$ là đường thẳng qua chúng. Tập $C \cap L$ là affine và chứa $x_1, x_2$, nên chứa mọi $\theta x_1 + (1-\theta)x_2$. Các điểm này thuộc $C \cap L \subseteq C$. Nếu $x_1 = x_2$ thì mọi tổ hợp đều bằng $x_1 \in C$. Vậy $C$ affine.
:::

::: exercise 4. Bao affine của một tập điểm
Viết $\operatorname{aff}\{(1, 0, 0), (0, 1, 0), (0, 0, 1)\}$ dưới dạng tập nghiệm của một phương trình tuyến tính. Làm tương tự với $\operatorname{aff}\{(1, 2), (3, 6)\}$ trong $\mathbb{R}^2$. Tập nào trong hai tập là không gian con?
:::

::: solution
Tổ hợp affine của ba vector đơn vị là $(\theta_1, \theta_2, \theta_3)$ với $\theta_1 + \theta_2 + \theta_3 = 1$. Mọi điểm thỏa $x_1 + x_2 + x_3 = 1$ đều viết được như vậy bằng cách chọn $\theta_i = x_i$. Do đó bao affine là mặt phẳng $x_1 + x_2 + x_3 = 1$, không chứa gốc nên không phải không gian con. Với hai điểm $(1,2)$ và $(3,6)$, bao affine là đường thẳng qua chúng, và cả hai đều nằm trên đường $2x_1 - x_2 = 0$, vốn đi qua gốc. Vì vậy bao affine thứ hai là không gian con $\{x : 2x_1 = x_2\}$.
:::

::: exercise 5. Phương pháp gradient không rời khỏi một tập affine
Cho $X \in \mathbb{R}^{m \times n}$ và $f(w) = \tfrac12 \|Xw - y\|_2^2$. Phương pháp gradient lặp $w^{(k+1)} = w^{(k)} - \eta X^T (X w^{(k)} - y)$. Chứng minh rằng mọi $w^{(k)}$ đều thuộc tập affine $w^{(0)} + \mathcal{R}(X^T)$, trong đó $\mathcal{R}(X^T)$ là không gian sinh bởi các hàng của $X$. Từ đó giải thích vì sao, trong ví dụ ở mục 6.1, xuất phát từ $(0, 0)$ cho nghiệm $(1, 1)$.
:::

::: hint
Quan sát rằng mỗi bước cộng thêm một vector có dạng $X^T u$. Với ví dụ ở mục 6.1, hãy tìm giao của đường $w_1 = w_2$ với đường $w_1 + w_2 = 2$.
:::

::: solution
Mỗi bước cộng vào $w^{(k)}$ vector $-\eta X^T(Xw^{(k)} - y)$, có dạng $X^T u$ với $u = -\eta(Xw^{(k)} - y)$, nên thuộc $\mathcal{R}(X^T)$. Quy nạp theo $k$ cho $w^{(k)} - w^{(0)} \in \mathcal{R}(X^T)$, tức $w^{(k)} \in w^{(0)} + \mathcal{R}(X^T)$. Với $X = [1 \;\; 1]$ ta có $\mathcal{R}(X^T) = \operatorname{span}\{(1,1)\}$, nên khi $w^{(0)} = 0$ mọi bước lặp nằm trên đường $w_1 = w_2$. Nếu dãy hội tụ về một nghiệm thì nghiệm đó phải nằm trên cả đường $w_1 = w_2$ lẫn đường $w_1 + w_2 = 2$, nên đó là $(1, 1)$. Để thấy dãy thật sự hội tụ với $\eta = \tfrac14$, đặt $s_k = w_1^{(k)} + w_2^{(k)}$. Công thức lặp cho $s_{k+1} - 2 = (1 - 2\eta)(s_k - 2)$. Với $\eta = \tfrac14$, hệ số $1 - 2\eta$ bằng $\tfrac12$, nên khoảng cách từ $s_k$ tới 2 giảm một nửa sau mỗi bước và $s_k \to 2$.
:::

## Tóm tắt

Một đường thẳng qua hai điểm $x_1, x_2$ trong không gian bất kỳ được mô tả bởi $\theta x_1 + (1-\theta)x_2$, trong đó $\theta$ là tỉ lệ quãng đường đi từ $x_2$ về phía $x_1$. Giới hạn $0 \le \theta \le 1$ cho đoạn thẳng. Tập affine là tập chứa trọn đường thẳng qua hai điểm bất kỳ của nó, và nó cũng chứa mọi tổ hợp affine của các điểm của nó.

Điều kiện "tổng hệ số bằng 1" là điều kiện để một phép trộn các điểm không phụ thuộc vào gốc tọa độ, vì vậy tổ hợp affine mang nghĩa hình học thật sự. Mỗi tập affine khác rỗng là một không gian con được tịnh tiến, và đó cũng chính là tập nghiệm của một hệ phương trình tuyến tính $Ax = b$, với không gian con đi kèm là $\mathcal{N}(A)$. Bao affine là tập affine nhỏ nhất chứa một tập cho trước. Hàm affine giữ nguyên tổ hợp affine, và "tầng tuyến tính" trong học sâu thực ra là một hàm affine.

Sau trang này, bạn có thể tham số hóa đường thẳng và đoạn thẳng trong $\mathbb{R}^n$, và kiểm tra một tập có affine hay không bằng một phản ví dụ cụ thể. Bạn cũng mô tả được tập nghiệm của một hệ tuyến tính bằng nghiệm riêng cộng không gian nghiệm thuần nhất, và giải thích được vì sao một mô hình có nhiều tham số hơn dữ liệu có vô số nghiệm khớp dữ liệu.

## Nguồn và đọc thêm

- S. Boyd, L. Vandenberghe, *Convex Optimization*, Cambridge University Press, 2004, §2.1.1–2.1.2 (tr. 21–23), Ví dụ 2.1 và Bài tập 2.2. Hình mô phỏng đầu trang tái hiện ý của Hình 2.1 (tr. 22) bằng dữ liệu tự chọn.
- Chứng minh không gian con đi kèm không phụ thuộc vào điểm chọn, ví dụ tọa độ trọng tâm, ví dụ dời gốc tọa độ, ví dụ hồi quy thiếu dữ liệu và các bài tập 1, 2, 4, 5 do người soạn bổ sung. Mọi con số đã được tính lại bằng chương trình.
- I. J. Goodfellow, O. Vinyals, A. M. Saxe, [*Qualitatively characterizing neural network optimization problems*](https://arxiv.org/abs/1412.6544), ICLR 2015. J. Frankle, [*Revisiting "Qualitatively Characterizing Neural Network Optimization Problems"*](https://arxiv.org/abs/2012.06898), 2020. Hai bài này chỉ được nhắc tới như ví dụ về việc khảo sát hàm mất mát dọc một đoạn thẳng trong không gian tham số.
