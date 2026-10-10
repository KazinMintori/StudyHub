---
course: toan-cho-ai
lecture: bai-01-nhap-mon-toi-uu
topic: noi-tuong-doi
section: topic
title: "Chiều affine và nội tương đối"
description: "Chiều affine của một tập, sự khác nhau giữa điểm trong và điểm trong tương đối, biên tương đối, và vì sao các điều kiện như Slater cần nội tương đối thay vì phần trong thông thường."
---

Hãy cầm một tờ giấy phẳng và hỏi: Tờ giấy có "phần bên trong" không? Câu trả lời trực giác là có, đó là toàn bộ tờ giấy trừ bốn mép. Nhưng nếu dùng định nghĩa điểm trong quen thuộc của giải tích, thì trong không gian ba chiều tờ giấy **không có điểm trong nào**. Quanh bất kỳ điểm nào trên tờ giấy, một quả cầu nhỏ đến mấy cũng có phần nhô lên phía trên và phần chìm xuống phía dưới mặt giấy, tức là có điểm không thuộc tờ giấy.

Mâu thuẫn giữa trực giác và định nghĩa ấy không phải chuyện bắt bẻ chữ nghĩa. Trong tối ưu, miền khả thi rất thường "mỏng" như tờ giấy, chẳng hạn khi có ràng buộc đẳng thức $x_1 + x_2 + x_3 = 1$. Nếu chỉ dùng khái niệm điểm trong thông thường, những miền đó không có điểm trong, và mọi định lý nào đòi hỏi "một điểm nằm hẳn bên trong miền" đều không dùng được. Khái niệm thay thế là **nội tương đối**, tức phần trong được đo bên trong bao affine của tập. Ta cũng làm rõ một khái niệm đi kèm là **chiều affine**.

Kiến thức nền tảng bao gồm bao affine và khái niệm quả cầu $B(x, r) = \{y : \|y - x\| \le r\}$.

## 1. Chiều affine

Ở chủ đề trước, ta định nghĩa số chiều của một tập affine là số chiều của không gian con đi kèm. Với một tập $C$ bất kỳ, ta mượn số chiều của tập affine nhỏ nhất chứa nó.

> **Định nghĩa.** **Chiều affine** của tập $C$ là số chiều của bao affine $\operatorname{aff} C$.

Một đoạn thẳng trong $\mathbb{R}^3$ có chiều affine 1, vì bao affine của nó là một đường thẳng. Một tam giác đặc trong $\mathbb{R}^3$ có chiều affine 2. Tập các phân phối xác suất trên ba kết quả, tức các vector $p \in \mathbb{R}^3$ với $p_i \ge 0$ và $p_1 + p_2 + p_3 = 1$, có chiều affine 2, vì nó nằm trọn trong mặt phẳng $p_1 + p_2 + p_3 = 1$ và không nằm trong đường thẳng nào.

Chiều affine không phải lúc nào cũng trùng khớp với các khái niệm số chiều topo thông thường. Ta xét ví dụ đường tròn đơn vị $\{x \in \mathbb{R}^2 : x_1^2 + x_2^2 = 1\}$. Theo trực giác vi phân và topo, đường tròn là đối tượng một chiều: Muốn chỉ ra một điểm trên nó, chỉ cần một tham số góc $\varphi$. Nhưng bao affine của đường tròn là cả mặt phẳng $\mathbb{R}^2$, nên chiều affine của nó bằng 2. Sự khác biệt này hoàn toàn có lý: Chiều affine đo xem tập hợp cần một không gian phẳng bao nhiêu chiều để chứa trọn nó, chứ không đo số bậc tự do cục bộ. Đường tròn bị cong, nên không có đường thẳng một chiều nào chứa nổi nó.

## 2. Điểm trong và vấn đề của những tập mỏng

Nhắc lại, $x$ là một **điểm trong** của $C \subseteq \mathbb{R}^n$ nếu có một bán kính $r > 0$ sao cho cả quả cầu $B(x, r)$ nằm trong $C$. Tập các điểm trong là **phần trong**, ký hiệu $\operatorname{int} C$.

Định nghĩa này phụ thuộc vào không gian ta đang đứng. Đoạn thẳng $[0, 1]$ xét trong $\mathbb{R}$ có phần trong là khoảng mở $(0, 1)$. Cũng đoạn thẳng đó, đặt nằm trên trục hoành của $\mathbb{R}^2$, lại có phần trong rỗng: Quanh điểm $(\tfrac12, 0)$, mọi hình tròn nhỏ đều chứa những điểm có tung độ khác 0, nên không nằm trên đoạn.

Mô phỏng dưới đây cho thấy đúng hiện tượng ấy. Hình tròn quanh $x$ luôn lòi ra khỏi đường thẳng chứa đoạn. Tuy vậy, nếu chỉ nhìn phần hình tròn nằm trên đường thẳng đó, câu chuyện lại khác.

<RelintLab type="segment" />

## 3. Nội tương đối

Ý tưởng sửa chữa rất tự nhiên: Khi kiểm tra một điểm có nằm "bên trong" hay không, ta chỉ xét những điểm lân cận thuộc bao affine của tập, bỏ qua các hướng mà tập vốn dĩ không bao giờ đi tới.

> **Định nghĩa.** **Nội tương đối** của tập $C$ là
> $$\operatorname{relint} C = \{x \in C : B(x, r) \cap \operatorname{aff} C \subseteq C \text{ với một } r > 0 \text{ nào đó}\}.$$

So sánh với định nghĩa điểm trong, chỉ có một chỗ khác: Quả cầu $B(x, r)$ được thay bằng phần giao $B(x, r) \cap \operatorname{aff} C$. Với tờ giấy trong $\mathbb{R}^3$, phần giao này là một hình tròn nằm phẳng trên mặt giấy, và câu hỏi trở thành "có hình tròn phẳng nhỏ nào quanh $x$ nằm trọn trên tờ giấy không?". Câu hỏi này có câu trả lời khớp với trực giác.

Ta cần lưu ý một tính chất giải tích quan trọng: Chuẩn dùng để định nghĩa quả cầu hoàn toàn không ảnh hưởng đến kết quả: Dùng bất kỳ chuẩn nào trên $\mathbb{R}^n$ cũng đều dẫn tới cùng một nội tương đối. Điều này xuất phát từ định lý tương đương chuẩn trong không gian hữu hạn chiều $\mathbb{R}^n$: Quả cầu theo chuẩn này luôn chứa một quả cầu nhỏ hơn theo chuẩn kia có cùng tâm.

Từ nội tương đối ta định nghĩa **biên tương đối** là $\operatorname{cl} C \setminus \operatorname{relint} C$, trong đó $\operatorname{cl} C$ là bao đóng của $C$. Biên tương đối là "mép" của tập khi nhìn từ bên trong bao affine của nó.

::: example Hình vuông trong mặt phẳng tọa độ của R³
Xét hình vuông nằm phẳng trên mặt $x_3 = 0$ của không gian ba chiều,

$$
C = \{x \in \mathbb{R}^3 : -1 \le x_1 \le 1,\ -1 \le x_2 \le 1,\ x_3 = 0\}.
$$

Bao affine của nó là mặt phẳng $\{x : x_3 = 0\}$. Phần trong của $C$ trong $\mathbb{R}^3$ là rỗng, và biên của $C$ trong $\mathbb{R}^3$ là chính $C$. Trong khi đó,

$$
\operatorname{relint} C = \{x \in \mathbb{R}^3 : -1 < x_1 < 1,\ -1 < x_2 < 1,\ x_3 = 0\},
$$

và biên tương đối là khung viền $\{x \in \mathbb{R}^3 : \max\{|x_1|, |x_2|\} = 1,\ x_3 = 0\}$. Nói cách khác, nội tương đối là hình vuông bỏ đi bốn cạnh, đúng như cảm nhận ban đầu về "phần bên trong của tờ giấy".
:::

Người học có thể trực tiếp kiểm chứng từng điểm trong mô phỏng dưới đây. Hình vẽ sử dụng phép chiếu xiên để mô tả trực quan: Đường tròn nét đứt tượng trưng cho quả cầu quanh điểm đang xét, còn hình tròn tô màu là phần giao của quả cầu với mặt phẳng $x_3 = 0$.

<RelintLab type="square" />

Một điểm $(a, b, 0)$ với $|a| < 1$ và $|b| < 1$ thuộc nội tương đối, vì chọn $r \le \min\{1 - |a|, 1 - |b|\}$ thì hình tròn giao nằm trọn trong hình vuông. Điểm trên cạnh, chẳng hạn $(1, 0, 0)$, thì không: Hình tròn giao có bán kính bao nhiêu cũng chứa những điểm có $x_1 > 1$.

## 4. Một vài ví dụ để luyện mắt

Bảng sau đặt phần trong và nội tương đối cạnh nhau. Hai khái niệm trùng nhau đúng khi tập có chiều affine bằng số chiều của không gian, tức là khi tập "đủ dày".

| Tập | Phần trong | Nội tương đối |
| --- | --- | --- |
| Đoạn $[a, b]$ trong $\mathbb{R}$ | $(a, b)$ | $(a, b)$ |
| Đoạn nối $x_1 \ne x_2$ trong $\mathbb{R}^2$ | Rỗng | Đoạn bỏ hai đầu mút |
| Một điểm $\{x_0\}$ | Rỗng (nếu $n \ge 1$) | Chính $\{x_0\}$ |
| Hình tròn đặc trong $\mathbb{R}^2$ | Hình tròn mở | Hình tròn mở |
| Đơn hình xác suất trong $\mathbb{R}^3$ | Rỗng | Các $p$ có mọi $p_i > 0$ và tổng bằng 1 |
| Một đường thẳng trong $\mathbb{R}^2$ | Rỗng | Chính đường thẳng đó |

Dòng thứ ba thường làm người học bất ngờ. Bao affine của một điểm là chính điểm đó, nên $B(x_0, r) \cap \operatorname{aff}\{x_0\} = \{x_0\} \subseteq \{x_0\}$ với mọi $r$. Vì thế một điểm đơn lẻ là "toàn bộ phần trong của chính nó". Kết quả nghe kỳ lạ nhưng nhất quán: Trong không gian không chiều chứa nó, điểm ấy không có mép nào cả.

Dòng thứ năm có ý nghĩa trực tiếp trong học máy. Đầu ra của hàm softmax là một vector xác suất có mọi thành phần **dương**, nên nó luôn nằm trong nội tương đối của đơn hình xác suất, không bao giờ chạm biên tương đối. Một mô hình softmax không thể gán xác suất đúng bằng 0 cho một lớp nào. Đó cũng là lý do hàm mất mát cross-entropy không bao giờ đạt đúng giá trị 0 với một tham số hữu hạn, chỉ tiến dần về 0.

## 5. Vì sao ta cần nội tương đối

Thoạt nhìn, nội tương đối giống một khái niệm kỹ thuật dành cho người thích chi tiết. Thực ra nó cần thiết mỗi khi bài toán có ràng buộc đẳng thức, vì khi đó miền khả thi nằm trong một tập affine thấp chiều và phần trong thông thường của nó rỗng.

Chỗ quan trọng nhất là **điều kiện Slater** ở Lecture 03, điều kiện bảo đảm đối ngẫu mạnh cho bài toán lồi. Điều kiện này yêu cầu có một điểm thỏa mọi đẳng thức và thỏa **chặt** mọi bất đẳng thức, đồng thời nằm trong **nội tương đối** của miền xác định chung. Nếu ta đòi điểm đó nằm trong phần trong thông thường, thì mọi bài toán có miền xác định nằm trong một tập affine thấp chiều sẽ bị loại oan, dù chúng hoàn toàn bình thường.

Ý nghĩa quan trọng thứ hai là tính liên tục của hàm lồi. Một kết quả kinh điển của giải tích lồi khẳng định: Mọi hàm lồi luôn liên tục trên nội tương đối của miền xác định, và chỉ có thể xảy ra hiện tượng gián đoạn tại biên tương đối. Chẳng hạn, xét hàm số nhận giá trị 0 trên khoảng mở $(0, 1)$ và nhận giá trị 1 tại hai đầu mút của đoạn $[0, 1]$. Đây là một hàm lồi trên $[0, 1]$, nhưng bị gián đoạn đúng tại hai đầu mút, tức ngay trên biên tương đối.

Chỗ thứ ba là chứng minh định lý siêu phẳng tựa ở một chủ đề sau. Lập luận chia làm hai trường hợp: Tập có phần trong khác rỗng, hoặc tập nằm trọn trong một tập affine thấp chiều. Trường hợp thứ hai chính là tình huống mà phần trong thông thường không còn hữu ích.

Có một kết quả nền tảng của giải tích lồi mà ta chỉ phát biểu: **Mọi tập lồi khác rỗng trong $\mathbb{R}^n$ đều có nội tương đối khác rỗng**. Phần trong thì có thể rỗng, nhưng nội tương đối thì không bao giờ. Đây là lý do nội tương đối là khái niệm "đúng" để làm việc với tập lồi.

## 6. Những câu hỏi để đào sâu

**Câu 1.** Nội tương đối của một tập có thể rỗng không? Hãy tìm một tập không lồi có nội tương đối rỗng.

<details><summary>Xem lời giải thích</summary>

Có thể, nếu tập không lồi. Đường tròn đơn vị trong $\mathbb{R}^2$ có bao affine là cả mặt phẳng, nên nội tương đối trùng với phần trong thông thường, và phần này rỗng vì quanh mỗi điểm của đường tròn luôn có điểm không thuộc đường tròn. Một ví dụ khác là tập hai điểm $\{(0,0), (1,0)\}$: Bao affine là trục hoành, và quanh mỗi điểm, phần giao của quả cầu với trục hoành là một đoạn chứa những điểm không thuộc tập. Kết quả "nội tương đối luôn khác rỗng" ở mục 5 cần giả thiết lồi.

</details>

**Câu 2.** Nếu $C_1 \subseteq C_2$, có thể kết luận $\operatorname{relint} C_1 \subseteq \operatorname{relint} C_2$ không? Hãy thử với $C_1$ là một cạnh của hình vuông và $C_2$ là cả hình vuông trong $\mathbb{R}^2$.

<details><summary>Xem lời giải thích</summary>

Không. Với $C_1$ là cạnh dưới của hình vuông $[0,1]^2$, nội tương đối của $C_1$ là cạnh đó bỏ hai đầu mút, chẳng hạn chứa điểm $(\tfrac12, 0)$. Nhưng $(\tfrac12, 0)$ nằm trên biên của hình vuông, nên không thuộc $\operatorname{relint} C_2 = (0,1)^2$. Phép lấy nội tương đối không có tính đơn điệu như phép lấy phần trong, vì bao affine của tập con có thể nhỏ hơn hẳn. Đây là một chỗ dễ sai khi chứng minh, cần kiểm tra cẩn thận mỗi khi muốn suy từ tập con sang tập lớn.

</details>

**Câu 3.** Trong ràng buộc của một bài toán có $x_1 + x_2 = 1$ và $x_1, x_2 \ge 0$, điểm nào thuộc nội tương đối của miền khả thi? Điểm $(\tfrac12, \tfrac12)$ có phải "điểm trong" của miền khả thi xét trong $\mathbb{R}^2$ không?

<details><summary>Xem lời giải thích</summary>

Miền khả thi là đoạn nối $(1, 0)$ và $(0, 1)$. Nội tương đối là đoạn bỏ hai đầu mút, tức các điểm có $x_1, x_2 > 0$ và $x_1 + x_2 = 1$. Điểm $(\tfrac12, \tfrac12)$ thuộc nội tương đối nhưng không phải điểm trong trong $\mathbb{R}^2$, vì miền khả thi là một đoạn thẳng. Với những miền khả thi như vậy, điều kiện Slater phải được phát biểu bằng nội tương đối thì mới có ý nghĩa.

</details>

**Câu 4.** Thử một định nghĩa khác cho "điểm trong theo chiều affine": Thay $\mathbb{R}^n$ bởi không gian con $V$ đi kèm $\operatorname{aff} C$ thay vì chính $\operatorname{aff} C$. Định nghĩa đó có cho cùng kết quả không?

<details><summary>Xem lời giải thích</summary>

Không, nếu $\operatorname{aff} C$ không đi qua gốc. Chẳng hạn với $C$ là đoạn nối $(1, 0)$ và $(0, 1)$, không gian con đi kèm là đường $x_1 + x_2 = 0$, không chứa điểm nào của $C$. Giao của một quả cầu quanh điểm thuộc $C$ với không gian con đó có thể rỗng hoặc chẳng liên quan gì đến $C$. Định nghĩa đúng phải dùng tập affine chứa $C$, chứ không phải bản sao đi qua gốc của nó. Đây lại là một lần chữ "affine" khác chữ "tuyến tính" một cách có hệ quả.

</details>

## 7. Bài tập tự luyện

::: exercise 1. Xác định nội tương đối
Tìm chiều affine, phần trong và nội tương đối của các tập sau: (a) $\{(x_1, x_2, x_3) : x_1^2 + x_2^2 \le 1,\ x_3 = 2\}$ trong $\mathbb{R}^3$, (b) $\{x \in \mathbb{R}^3 : x \succeq 0,\ x_1 + x_2 + x_3 = 1\}$, (c) đoạn nối $(1, 1)$ và $(3, 2)$ trong $\mathbb{R}^2$.
:::

::: solution
(a) Tập là một hình tròn đặc nằm trong mặt phẳng $x_3 = 2$. Chiều affine bằng 2, phần trong trong $\mathbb{R}^3$ rỗng, nội tương đối là $\{x_1^2 + x_2^2 < 1,\ x_3 = 2\}$. (b) Đơn hình xác suất trong $\mathbb{R}^3$: Chiều affine 2, phần trong rỗng, nội tương đối là $\{x \succ 0,\ x_1 + x_2 + x_3 = 1\}$, trong đó $x \succ 0$ nghĩa là mọi thành phần dương. (c) Chiều affine 1, phần trong rỗng, nội tương đối là $\{(1,1) + t(2, 1) : 0 < t < 1\}$.
:::

::: exercise 2. Chuẩn không ảnh hưởng
Chứng minh rằng nếu thay chuẩn Euclid bằng chuẩn $\|x\|_\infty = \max_i |x_i|$ trong định nghĩa nội tương đối, tập thu được không đổi.
:::

::: hint
Dùng hai bất đẳng thức $\|x\|_\infty \le \|x\|_2 \le \sqrt{n}\, \|x\|_\infty$ để so sánh hai loại quả cầu cùng tâm.
:::

::: solution
Gọi $B_2(x, r)$ và $B_\infty(x, r)$ là hai loại quả cầu. Từ $\|y - x\|_\infty \le \|y - x\|_2$, ta có $B_2(x, r) \subseteq B_\infty(x, r)$. Từ $\|y - x\|_2 \le \sqrt{n}\,\|y - x\|_\infty$, ta có $B_\infty(x, r/\sqrt{n}) \subseteq B_2(x, r)$. Nếu $x$ thỏa điều kiện nội tương đối với chuẩn $\infty$ và bán kính $r$, thì

$$
B_2(x, r) \cap \operatorname{aff} C \subseteq B_\infty(x, r) \cap \operatorname{aff} C \subseteq C,
$$

nên $x$ cũng thỏa với chuẩn Euclid. Ngược lại, nếu $x$ thỏa với chuẩn Euclid và bán kính $r$, thì bán kính $r/\sqrt{n}$ dùng được cho chuẩn $\infty$. Hai định nghĩa cho cùng một tập.
:::

## Tóm tắt

Chiều affine của một tập là số chiều của bao affine của nó, tức số chiều không gian phẳng cần để chứa tập. Phần trong thông thường phụ thuộc vào không gian bao quanh, nên những tập "mỏng" như tờ giấy trong $\mathbb{R}^3$ có phần trong rỗng dù trực giác thấy chúng có phần bên trong. Nội tương đối sửa điều đó bằng cách chỉ xét các điểm lân cận nằm trong bao affine. Hai khái niệm trùng nhau khi tập có chiều affine bằng số chiều của không gian.

Mọi tập lồi khác rỗng đều có nội tương đối khác rỗng. Nội tương đối là khái niệm được dùng trong điều kiện Slater, trong kết quả về tính liên tục của hàm lồi và trong chứng minh định lý siêu phẳng tựa. Người học có thể xác định nội tương đối của các tập hình học quen thuộc và giải thích tường minh vì sao một điểm khả thi có ràng buộc đẳng thức không bao giờ là điểm trong theo nghĩa thông thường.

## Tài liệu tham khảo

- Stephen Boyd, Lieven Vandenberghe, *Convex Optimization*, Cambridge University Press.
- R. Tyrrell Rockafellar, *Convex Analysis*, Princeton University Press.
