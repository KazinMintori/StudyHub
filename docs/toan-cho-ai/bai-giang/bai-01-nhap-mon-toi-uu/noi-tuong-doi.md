---
course: toan-cho-ai
lecture: bai-01-nhap-mon-toi-uu
topic: noi-tuong-doi
section: topic
title: "Chiều affine và nội tương đối"
description: "Chiều affine của một tập, sự khác nhau giữa điểm trong và điểm trong tương đối, biên tương đối, và vì sao các điều kiện như Slater cần nội tương đối thay vì phần trong thông thường."
---

Hãy tưởng tượng một tờ giấy phẳng đặt trong không gian ba chiều: Tờ giấy có "phần bên trong" hay không? Trực giác thường trả lời là có, đó là toàn bộ diện tích tờ giấy trừ đi bốn mép viền ngoài cùng. Thế nhưng, nếu áp dụng máy móc định nghĩa điểm trong quen thuộc của giải tích topo, thì trong không gian ba chiều tờ giấy **không có bất kỳ điểm trong nào**. Quanh một điểm bất kỳ trên mặt giấy, quả cầu mở bán kính $r > 0$ dù nhỏ đến đâu cũng sẽ nhô ra phía trên và chìm xuống phía dưới mặt phẳng chứa giấy, tức là luôn chứa những điểm không thuộc tờ giấy.

Mâu thuẫn giữa trực giác hình học và định nghĩa topo không dừng lại ở khía cạnh câu chữ. Trong tối ưu hóa, miền khả thi rất thường có dạng "phẳng và mỏng" như tờ giấy, điển hình là khi xuất hiện các ràng buộc đẳng thức tuyến tính dạng $x_1 + x_2 + x_3 = 1$. Nếu chỉ bám vào khái niệm điểm trong thông thường, những miền khả thi này sẽ có phần trong rỗng, khiến mọi định lý yêu cầu "tồn tại điểm nằm hẳn bên trong miền khả thi" đều bị vô hiệu hóa. Khái niệm thay thế chuẩn mực là **nội tương đối** (relative interior), tức phần trong được xác định cục bộ bên trong chính bao affine của tập hợp. Đi cùng với khái niệm này là **chiều affine**, thước đo số chiều không gian phẳng tối thiểu cần thiết để bao trọn một tập.

Kiến thức nền tảng bao gồm bao affine và khái niệm quả cầu Euclid $B(x, r) = \{y \mid \|y - x\|_2 \le r\}$.

## 1. Chiều affine

Số chiều của một tập affine được định nghĩa là số chiều của không gian con phương đi kèm. Với một tập $C$ bất kỳ, ta xác định số chiều thông qua tập affine nhỏ nhất bao bọc nó.

> **Định nghĩa.** **Chiều affine** của tập hợp $C$, ký hiệu $\operatorname{affdim}(C)$, là số chiều của bao affine $\operatorname{aff} C$.

Một đoạn thẳng nối hai điểm phân biệt trong $\mathbb{R}^3$ có chiều affine bằng 1, bởi bao affine của nó là một đường thẳng. Một tam giác đặc trong $\mathbb{R}^3$ có chiều affine bằng 2. Xét tập các phân phối xác suất rời rạc trên ba biến cố, tức tập các vector $p \in \mathbb{R}^3$ thỏa mãn $p_i \ge 0$ và có tổng thành phần bằng 1:

$$
\sum_{i=1}^3 p_i = p_1 + p_2 + p_3 = 1 .
$$

Tập hợp này có chiều affine bằng 2, vì nó nằm trọn trong mặt phẳng $p_1 + p_2 + p_3 = 1$ và không suy biến về một đường thẳng.

Cần phân biệt rõ: Chiều affine không nhất thiết trùng khớp với khái niệm số chiều topo hay số chiều vi phân của đa tạp. Xét đường tròn đơn vị phẳng $\{x \in \mathbb{R}^2 \mid x_1^2 + x_2^2 = 1\}$. Theo quan điểm giải tích vi phân, đường tròn là một đối tượng một chiều, vì vị trí mỗi điểm trên đường tròn được xác định duy nhất qua một tham số góc $\varphi \in [0, 2\pi)$. Tuy nhiên, bao affine của đường tròn là toàn bộ mặt phẳng $\mathbb{R}^2$, kéo theo chiều affine của nó bằng 2. Sự khác biệt này hoàn toàn tự nhiên: Chiều affine đo kích thước của không gian phẳng nhỏ nhất có thể chứa trọn vẹn tập hợp, chứ không đo số bậc tự do cục bộ. Đường tròn bị uốn cong trong mặt phẳng, do đó không có đường thẳng một chiều nào có thể chứa nổi nó.

## 2. Điểm trong và hiện tượng các tập bị dẹp

Nhắc lại định nghĩa topo cơ bản: Một điểm $x$ được gọi là **điểm trong** của tập $C \subseteq \mathbb{R}^n$ nếu tồn tại bán kính $r > 0$ sao cho quả cầu mở $B(x, r) = \{y \mid \|y - x\|_2 < r\}$ nằm hoàn toàn trong $C$. Tập hợp tất cả các điểm trong được gọi là **phần trong** của $C$, ký hiệu là $\operatorname{int} C$.

Định nghĩa này phụ thuộc trực tiếp vào không gian bao quanh mà ta đang đứng để quan sát. Xét đoạn thẳng $C = [0, 1]$:
- Khi xét trong không gian một chiều $\mathbb{R}$, phần trong của $C$ là khoảng mở $\operatorname{int} C = (0, 1)$.
- Nhưng khi đặt chính đoạn thẳng đó nằm trên trục hoành của mặt phẳng $\mathbb{R}^2$, tức $C = \{(x_1, 0) \mid 0 \le x_1 \le 1\}$, phần trong của nó trong $\mathbb{R}^2$ lại rỗng hoàn toàn. Quanh điểm $(\tfrac12, 0)$, bất kỳ hình tròn mở nào dù bán kính nhỏ đến đâu cũng chứa các điểm có tung độ khác 0, và những điểm đó không thuộc đoạn thẳng.

Mô phỏng dưới đây trực quan hóa hiện tượng này. Quả cầu mở quanh điểm $x$ luôn tràn ra ngoài đường thẳng chứa đoạn thẳng. Thế nhưng, nếu ta chỉ thu hẹp tầm nhìn vào phần giao giữa quả cầu và đường thẳng đó, câu chuyện lại hoàn toàn khác.

<RelintLab type="segment" />

## 3. Nội tương đối và biên tương đối

Ý tưởng khắc phục hiện tượng trên rất mạch lạc: Khi kiểm tra xem một điểm có nằm "bên trong" tập hợp hay không, ta chỉ xét các điểm lân cận thuộc bao affine của tập, bỏ qua những hướng không gian mà tập hợp vốn dĩ không bao giờ vươn tới.

> **Định nghĩa.** **Nội tương đối** của tập $C$, ký hiệu $\operatorname{relint} C$, là tập hợp
> $$
> \operatorname{relint} C = \{x \in C \mid \exists r > 0 : B(x, r) \cap \operatorname{aff} C \subseteq C\} .
> $$

So với định nghĩa điểm trong thông thường, điểm khác biệt duy nhất nằm ở chỗ quả cầu $B(x, r)$ được thay bằng phần giao $B(x, r) \cap \operatorname{aff} C$. Quay lại hình ảnh tờ giấy trong $\mathbb{R}^3$, phần giao này chính là một hình tròn phẳng nằm trọn trên mặt phẳng của tờ giấy. Bài toán kiểm tra điểm trong trở thành: "Liệu có tồn tại một hình tròn phẳng nhỏ quanh $x$ nằm trọn trên tờ giấy hay không?". Cách đặt vấn đề này đem lại câu trả lời hoàn toàn ăn khớp với trực giác ban đầu.

Về mặt giải tích, việc lựa chọn chuẩn để định nghĩa quả cầu không làm thay đổi kết quả. Trong không gian hữu hạn chiều $\mathbb{R}^n$, bất kỳ chuẩn nào cũng đều dẫn tới cùng một tập nội tương đối. Tính chất này bắt nguồn từ tính tương đương của mọi chuẩn trên không gian hữu hạn chiều: Quả cầu theo chuẩn này luôn chứa một quả cầu đồng tâm nhỏ hơn theo chuẩn khác.

Đi cùng với nội tương đối là khái niệm **biên tương đối** (relative boundary), ký hiệu $\operatorname{relbd} C$, được định nghĩa là:

$$
\operatorname{relbd} C = \operatorname{cl} C \setminus \operatorname{relint} C ,
$$

trong đó $\operatorname{cl} C$ là bao đóng topo thông thường của $C$. Biên tương đối chính là "mép ngoài" của tập hợp khi quan sát từ bên trong bao affine của nó.

::: example Hình vuông phẳng trong không gian ba chiều
Xét hình vuông nằm phẳng trên mặt phẳng tọa độ $x_3 = 0$ của không gian $\mathbb{R}^3$:

$$
C = \{x \in \mathbb{R}^3 \mid -1 \le x_1 \le 1,\ -1 \le x_2 \le 1,\ x_3 = 0\} .
$$

Bao affine của tập $C$ là mặt phẳng $\operatorname{aff} C = \{x \in \mathbb{R}^3 \mid x_3 = 0\}$. Phần trong của $C$ trong $\mathbb{R}^3$ rỗng hoàn toàn, và biên topo thông thường của $C$ trong $\mathbb{R}^3$ chính là toàn bộ tập $C$. Trong khi đó, nội tương đối của tập là:

$$
\operatorname{relint} C = \{x \in \mathbb{R}^3 \mid -1 < x_1 < 1,\ -1 < x_2 < 1,\ x_3 = 0\} ,
$$

và biên tương đối là khung viền bốn cạnh:

$$
\operatorname{relbd} C = \{x \in \mathbb{R}^3 \mid \max\{|x_1|, |x_2|\} = 1,\ x_3 = 0\} .
$$

Nội tương đối là hình vuông đã loại bỏ bốn cạnh bao quanh, đúng như cảm nhận tự nhiên về "phần bên trong của một mặt phẳng hữu hạn".
:::

Người học có thể trực tiếp tương tác với từng điểm trong mô phỏng dưới đây. Hình vẽ sử dụng phép chiếu không gian: Đường tròn nét đứt biểu diễn quả cầu trong $\mathbb{R}^3$, còn hình tròn đặc tô màu là phần giao giữa quả cầu và mặt phẳng $x_3 = 0$.

<RelintLab type="square" />

Một điểm $(a, b, 0)$ với $|a| < 1$ và $|b| < 1$ luôn thuộc nội tương đối, bởi ta chỉ cần chọn bán kính $r \le \min\{1 - |a|, 1 - |b|\}$ thì phần giao hình tròn sẽ nằm gọn trong hình vuông. Ngược lại, điểm nằm trên cạnh, chẳng hạn $(1, 0, 0)$, không thuộc nội tương đối: Bất kể bán kính $r > 0$ nhỏ thế nào, phần giao hình tròn cũng chứa những điểm có $x_1 > 1$, tức nằm ngoài hình vuông.

## 4. Bảng đối chiếu các tập hình học cơ bản

Bảng sau so sánh phần trong thông thường và nội tương đối trên các tập hình học quen thuộc. Hai khái niệm này trùng nhau khi và chỉ khi chiều affine của tập bằng đúng số chiều của không gian bao quanh, nghĩa là khi tập không bị dẹp trong không gian đó.

| Tập hợp $C$ | Không gian | Phần trong $\operatorname{int} C$ | Nội tương đối $\operatorname{relint} C$ |
| :--- | :--- | :--- | :--- |
| Đoạn thẳng $[a, b]$ ($a < b$) | $\mathbb{R}$ | Khoảng mở $(a, b)$ | Khoảng mở $(a, b)$ |
| Đoạn nối hai điểm $x_1 \ne x_2$ | $\mathbb{R}^2$ | Rỗng $\emptyset$ | Đoạn thẳng bỏ hai đầu mút |
| Một điểm đơn lẻ $\{x_0\}$ | $\mathbb{R}^n$ ($n \ge 1$) | Rỗng $\emptyset$ | Chính điểm $\{x_0\}$ |
| Hình tròn đặc $\{x \mid \|x\|_2 \le 1\}$ | $\mathbb{R}^2$ | Hình tròn mở $\{x \mid \|x\|_2 < 1\}$ | Hình tròn mở $\{x \mid \|x\|_2 < 1\}$ |
| Đơn hình xác suất chuẩn tắc | $\mathbb{R}^3$ | Rỗng $\emptyset$ | $\{p \in \mathbb{R}^3 \mid p_i > 0,\ \sum_{i=1}^3 p_i = 1\}$ |
| Đường thẳng $\{x \mid a^T x = b\}$ | $\mathbb{R}^2$ | Rỗng $\emptyset$ | Chính đường thẳng đó |

Trường hợp điểm đơn lẻ $\{x_0\}$ trong bảng mang một ý nghĩa đặc biệt: Bao affine của một điểm là chính điểm đó, do đó $B(x_0, r) \cap \operatorname{aff}\{x_0\} = \{x_0\} \subseteq \{x_0\}$ với mọi bán kính $r > 0$. Vì thế, một điểm đơn lẻ chính là toàn bộ phần trong của chính nó khi nhìn từ bao affine không chiều của nó. Kết quả này phản ánh bản chất topo nhất quán: Trong không gian không chiều, một điểm không có mép biên.

Trường hợp đơn hình xác suất liên hệ trực tiếp với các mô hình phân loại trong học máy: Đầu ra của hàm softmax là một vector xác suất thỏa mãn mọi thành phần đều dương chặt ($p_i > 0$). Do đó, phân phối dự đoán của mô hình luôn nằm bên trong nội tương đối của đơn hình xác suất, không bao giờ chạm tới biên tương đối. Mô hình softmax không bao giờ gán xác suất bằng 0 cho bất kỳ lớp nào. Đó cũng là lý do vì sao hàm mất mát cross-entropy không thể đạt giá trị đúng bằng 0 với các trọng số hữu hạn, mà chỉ tiệm cận về 0 khi các trọng số tiến tới vô hạn.

## 5. Vai trò quyết định của nội tương đối trong tối ưu hóa

Nội tương đối không phải là một sự phức tạp hóa toán học, mà là công cụ thiết yếu để giải quyết ba vấn đề nền tảng trong giải tích lồi và tối ưu hóa:

### Điều kiện tư cách ràng buộc Slater
Khi xét bài toán tối ưu lồi có ràng buộc đẳng thức affine $Ax = b$ và các ràng buộc bất đẳng thức lồi $f_i(x) \le 0$, miền khả thi luôn nằm trong tập affine $\{x \mid Ax = b\}$. Nếu hệ ràng buộc đẳng thức không tầm thường, miền khả thi này có phần trong topo thông thường bằng rỗng. Điều kiện tư cách ràng buộc Slater (Slater's constraint qualification) bảo đảm đối ngẫu mạnh đòi hỏi tồn tại một điểm khả thi chặt nằm trong **nội tương đối** của miền xác định. Nếu phát biểu điều kiện này bằng phần trong thông thường, mọi bài toán có ràng buộc đẳng thức đều vi phạm điều kiện, dù bài toán hoàn toàn giải được và thỏa mãn đối ngẫu mạnh.

### Tính liên tục của hàm lồi
Một định lý kinh điển của giải tích lồi khẳng định: Mọi hàm lồi hữu hạn trên một tập lồi luôn liên tục trên **nội tương đối** của miền xác định, và hiện tượng gián đoạn chỉ có thể xảy ra trên biên tương đối. Xét hàm số nhận giá trị 0 trên khoảng mở $(0, 1)$ và nhận giá trị 1 tại hai đầu mút $x = 0$ và $x = 1$. Đây là một hàm lồi trên đoạn $[0, 1]$, nhưng bị gián đoạn đúng tại hai đầu mút, tức ngay trên biên tương đối của miền xác định.

### Tính tách được của các tập lồi
Định lý siêu phẳng tách phát biểu rằng: Hai tập lồi $C_1, C_2$ khác rỗng có thể tách được bằng một siêu phẳng khi và chỉ khi nội tương đối của chúng rời nhau, tức:

$$
\operatorname{relint} C_1 \cap \operatorname{relint} C_2 = \emptyset .
$$

Nếu thay bằng điều kiện phần trong thông thường rời nhau, định lý sẽ mất hiệu lực khi hai tập lồi đều mỏng (chẳng hạn hai đoạn thẳng chéo nhau trong không gian ba chiều).

Một kết quả nền tảng của giải tích lồi cần ghi nhớ: **Mọi tập lồi khác rỗng trong $\mathbb{R}^n$ đều có nội tương đối khác rỗng**. Trong khi phần trong thông thường rất dễ bị rỗng khi tập hợp bị dẹp, nội tương đối luôn được bảo toàn, khẳng định vị thế trung tâm của khái niệm này đối với hình học lồi.

## 6. Những câu hỏi để đào sâu

**Câu 1.** Nội tương đối của một tập hợp có thể rỗng hay không? Hãy tìm một tập hợp không lồi có nội tương đối rỗng.

<details><summary>Xem lời giải thích</summary>

Nội tương đối có thể rỗng nếu tập hợp không lồi. Xét đường tròn đơn vị trong $\mathbb{R}^2$: Bao affine của nó là toàn bộ mặt phẳng $\mathbb{R}^2$, do đó nội tương đối trùng với phần trong thông thường, và tập này rỗng vì quanh mỗi điểm trên đường tròn luôn có những điểm ngoài đường tròn. Một ví dụ khác là tập gồm hai điểm phân biệt $\{(0,0), (1,0)\}$: Bao affine là trục hoành, và quanh mỗi điểm, phần giao của quả cầu với trục hoành là một đoạn thẳng chứa vô số điểm không thuộc tập. Định lý "nội tương đối luôn khác rỗng" bắt buộc phải có giả thiết tập hợp lồi.

</details>

**Câu 2.** Nếu $C_1 \subseteq C_2$, liệu có thể suy ra $\operatorname{relint} C_1 \subseteq \operatorname{relint} C_2$ hay không? Hãy kiểm tra với $C_1$ là một cạnh của hình vuông và $C_2$ là toàn bộ hình vuông trong $\mathbb{R}^2$.

<details><summary>Xem lời giải thích</summary>

Khẳng định này không đúng. Lấy $C_1 = [0, 1] \times \{0\}$ là cạnh dưới của hình vuông đơn vị $C_2 = [0, 1]^2$. Nội tương đối của $C_1$ là cạnh đó bỏ đi hai đầu mút, chứa điểm $(\tfrac12, 0)$. Tuy nhiên, điểm $(\tfrac12, 0)$ nằm trên biên của hình vuông, do đó không thuộc $\operatorname{relint} C_2 = (0, 1)^2$. Phép lấy nội tương đối không có tính bảo toàn quan hệ bao hàm như phép lấy phần trong thông thường, bởi bao affine của tập con có thể có số chiều nhỏ hơn hẳn bao affine của tập mẹ.

</details>

**Câu 3.** Trong bài toán tối ưu có ràng buộc $x_1 + x_2 = 1$ và $x_1, x_2 \ge 0$, những điểm nào thuộc nội tương đối của miền khả thi? Điểm $(\tfrac12, \tfrac12)$ có phải là điểm trong của miền khả thi xét trong $\mathbb{R}^2$ hay không?

<details><summary>Xem lời giải thích</summary>

Miền khả thi là đoạn thẳng nối hai điểm $(1, 0)$ và $(0, 1)$. Nội tương đối của miền này là đoạn thẳng bỏ đi hai đầu mút, gồm các điểm thỏa mãn $x_1 + x_2 = 1$ và $x_1 > 0, x_2 > 0$. Điểm $(\tfrac12, \tfrac12)$ thuộc nội tương đối của miền khả thi, nhưng không phải là điểm trong trong $\mathbb{R}^2$ vì miền khả thi là một đoạn thẳng không có độ dày trong mặt phẳng. Với những miền khả thi như vậy, điều kiện Slater bắt buộc phải phát biểu thông qua nội tương đối mới phản ánh đúng bản chất bài toán.

</details>

**Câu 4.** Nếu ta thử thay đổi định nghĩa điểm trong tương đối bằng cách lấy không gian con phương $V$ đi kèm $\operatorname{aff} C$ thay vì chính $\operatorname{aff} C$, định nghĩa đó có cho cùng kết quả hay không?

<details><summary>Xem lời giải thích</summary>

Không, trừ trường hợp $\operatorname{aff} C$ đi qua gốc tọa độ. Chẳng hạn với đoạn thẳng nối $(1, 0)$ và $(0, 1)$, bao affine là đường thẳng $x_1 + x_2 = 1$, trong khi không gian con phương đi kèm là đường thẳng $x_1 + x_2 = 0$ đi qua gốc tọa độ. Hai đường thẳng này song song và không có điểm chung. Do đó, việc giao quả cầu quanh một điểm của tập với không gian con phương sẽ cho kết quả rỗng hoặc không liên quan gì tới tập ban đầu. Định nghĩa nội tương đối bắt buộc phải sử dụng bao affine, một không gian phẳng bao bọc trực tiếp tập hợp.

</details>

## 7. Bài tập tự luyện

::: exercise 1. Xác định nội tương đối của các tập hình học
Tìm chiều affine, phần trong và nội tương đối của các tập hợp sau:
1. Tập hợp:
   $$
   S_1 = \{(x_1, x_2, x_3) \in \mathbb{R}^3 \mid x_1^2 + x_2^2 \le 1,\ x_3 = 2\} .
   $$
2. Tập hợp:
   $$
   S_2 = \{x \in \mathbb{R}^3 \mid x_i \ge 0,\ x_1 + x_2 + x_3 = 1\} .
   $$
3. Đoạn thẳng $S_3$ nối hai điểm $(1, 1)$ và $(3, 2)$ trong $\mathbb{R}^2$.
:::

::: solution
1. Tập $S_1$ là một hình tròn đặc nằm trong mặt phẳng $x_3 = 2$: Bao affine là mặt phẳng $\{x \mid x_3 = 2\}$ có chiều bằng 2, do đó chiều affine bằng 2. Phần trong trong $\mathbb{R}^3$ bằng rỗng. Nội tương đối là:
   $$
   \operatorname{relint} S_1 = \{x \in \mathbb{R}^3 \mid x_1^2 + x_2^2 < 1,\ x_3 = 2\} .
   $$
2. Tập $S_2$ là đơn hình xác suất trong $\mathbb{R}^3$: Bao affine là mặt phẳng $x_1 + x_2 + x_3 = 1$ có chiều bằng 2, chiều affine bằng 2. Phần trong trong $\mathbb{R}^3$ bằng rỗng. Nội tương đối là:
   $$
   \operatorname{relint} S_2 = \{x \in \mathbb{R}^3 \mid x_i > 0,\ x_1 + x_2 + x_3 = 1\} .
   $$
3. Đoạn thẳng $S_3$: Bao affine là đường thẳng đi qua hai điểm, có chiều affine bằng 1. Phần trong trong $\mathbb{R}^2$ bằng rỗng. Nội tương đối là:
   $$
   \operatorname{relint} S_3 = \{(1 - t)(1, 1) + t(3, 2) \mid 0 < t < 1\} .
   $$
:::

::: exercise 2. Tính bất biến của nội tương đối đối với việc chọn chuẩn
Chứng minh rằng nếu thay chuẩn Euclid $\|\cdot\|_2$ bằng chuẩn cực đại $\|x\|_\infty = \max_{1 \le i \le n} |x_i|$ trong định nghĩa nội tương đối, tập hợp thu được không thay đổi.
:::

::: hint
Sử dụng mối quan hệ kẹp giữa hai chuẩn: Bất đẳng thức $\|x\|_\infty \le \|x\|_2 \le \sqrt{n}\, \|x\|_\infty$ giúp so sánh các quả cầu đồng tâm.
:::

::: solution
Ký hiệu $B_2(x, r)$ và $B_\infty(x, r)$ lần lượt là các quả cầu mở theo chuẩn Euclid và chuẩn cực đại. Từ bất đẳng thức $\|y - x\|_\infty \le \|y - x\|_2$, ta có quan hệ bao hàm $B_2(x, r) \subseteq B_\infty(x, r)$. Mặt khác, từ $\|y - x\|_2 \le \sqrt{n}\,\|y - x\|_\infty$, ta suy ra $B_\infty(x, r/\sqrt{n}) \subseteq B_2(x, r)$.

Giả sử điểm $x$ thỏa mãn điều kiện nội tương đối với chuẩn cực đại và bán kính $r > 0$, tức:

$$
B_\infty(x, r) \cap \operatorname{aff} C \subseteq C .
$$

Khi đó, vì $B_2(x, r) \subseteq B_\infty(x, r)$, ta có ngay:

$$
B_2(x, r) \cap \operatorname{aff} C \subseteq B_\infty(x, r) \cap \operatorname{aff} C \subseteq C ,
$$

chứng tỏ $x$ cũng thỏa mãn điều kiện nội tương đối với chuẩn Euclid. Ngược lại, nếu $x$ thỏa mãn điều kiện với chuẩn Euclid ở bán kính $r$, thì quả cầu chuẩn cực đại với bán kính $r' = r/\sqrt{n}$ sẽ thỏa mãn $B_\infty(x, r') \subseteq B_2(x, r)$, kéo theo $x$ thuộc nội tương đối theo chuẩn cực đại. Do đó, hai chuẩn xác định cùng một tập nội tương đối.
:::

## Tóm tắt

Chiều affine của một tập hợp là số chiều của bao affine của nó, thể hiện số chiều tối thiểu của không gian phẳng cần thiết để chứa trọn vẹn tập. Phần trong topo thông thường phụ thuộc vào không gian bao quanh, khiến các tập hợp bị dẹp có phần trong rỗng dù chúng có diện tích hay thể tích bên trong không gian riêng. Nội tương đối khắc phục triệt để nhược điểm này bằng cách giới hạn lân cận khảo sát bên trong bao affine. Hai khái niệm trùng nhau khi và chỉ khi chiều affine của tập bằng số chiều của không gian bao quanh.

Mọi tập lồi khác rỗng trong không gian hữu hạn chiều đều có nội tương đối khác rỗng. Nội tương đối giữ vai trò quyết định trong việc thiết lập điều kiện tư cách ràng buộc Slater cho bài toán quy hoạch lồi, khẳng định tính liên tục của hàm lồi và phát biểu định lý siêu phẳng tách giữa các tập lồi.

## Tài liệu tham khảo

- Stephen Boyd, Lieven Vandenberghe, *Convex Optimization*, Cambridge University Press.
- R. Tyrrell Rockafellar, *Convex Analysis*, Princeton University Press.
