---
course: ai-nen-tang-tac-tu
lecture: 05-menh-de-va-suy-dien
section: topic
topic: 5-6-chung-minh-bang-phan-chung
title: "5.6 Chứng minh bằng phản chứng"
description: "Mệnh đề Horn, ràng buộc toàn vẹn, nguyên tử khả giả định (assumables), tập xung đột và chẩn đoán sự cố dựa trên tính nhất quán."
---

Các mệnh đề xác định có thể được mở rộng tự nhiên để thực hiện chứng minh bằng phản chứng thông qua việc cho phép các quy tắc dẫn đến mâu thuẫn. Ví dụ: Trong môi trường mạng điện ở Hình 5.2, việc có thể phát biểu rằng một dự đoán nào đó (chẳng hạn đèn $l_{2}$ đang sáng) là không đúng trong thực tế sẽ mở đường cho lập luận chẩn đoán, từ đó suy ra các công tắc, bóng đèn hoặc cầu dao nào đang bị hỏng.

## 5.6.1 Mệnh đề Horn và ràng buộc toàn vẹn

Ngôn ngữ mệnh đề xác định thuần túy không cho phép diễn đạt trực tiếp một mâu thuẫn. Tuy nhiên, một mở rộng đơn giản của ngôn ngữ sẽ cho phép thực hiện chứng minh bằng phản chứng.

Một **ràng buộc toàn vẹn** (integrity constraint) là một mệnh đề có dạng:

$$
\mathit{false} \leftarrow a_{1} \wedge \ldots \wedge a_{k}.
$$

trong đó các $a_{i}$ là các nguyên tử và $\mathit{false}$ là một nguyên tử đặc biệt mang giá trị sai trong mọi diễn giải.

Một **mệnh đề Horn** (Horn clause) là một mệnh đề xác định hoặc một ràng buộc toàn vẹn. Nói cách khác, một mệnh đề Horn có phần đầu là $\mathit{false}$ hoặc là một nguyên tử thông thường.

Các ràng buộc toàn vẹn cho phép hệ thống chứng minh rằng một phép hội các nguyên tử nào đó là sai trong mọi mô hình của cơ sở tri thức. Nhắc lại rằng $\neg p$ là phủ định của $p$, nhận giá trị đúng khi $p$ sai trong diễn giải đang xét; và $p \vee q$ là phép tuyển của $p$ và $q$. Ràng buộc toàn vẹn $\mathit{false} \leftarrow a_{1} \wedge \ldots \wedge a_{k}$ hoàn toàn tương đương về mặt logic với câu tuyển:

$$
\neg a_{1} \vee \ldots \vee \neg a_{k}.
$$

Khác với cơ sở tri thức gồm toàn mệnh đề xác định (vốn chỉ suy ra được các nguyên tử khẳng định), cơ sở tri thức gồm các mệnh đề Horn có thể kéo theo các phủ định của nguyên tử.

::: example Ví dụ 5.17: Suy diễn phủ định từ ràng buộc toàn vẹn
Xét cơ sở tri thức $\mathit{KB}_{1}$ gồm:

$$
\begin{aligned}
&\mathit{false} \leftarrow a \wedge b. \\
&a \leftarrow c. \\
&b \leftarrow c.
\end{aligned}
$$

Nguyên tử $c$ nhận giá trị sai trong mọi mô hình của $\mathit{KB}_{1}$. Để thấy rõ điều này, giả sử phản chứng rằng $c$ nhận giá trị đúng trong một mô hình $I$ nào đó của $\mathit{KB}_{1}$. Khi đó, theo hai quy tắc sau, cả $a$ và $b$ đều bắt buộc phải đúng trong $I$ (để $I$ là mô hình). Vì $\mathit{false}$ luôn sai trong khi $a$ và $b$ đều đúng, nên mệnh đề đầu tiên $\mathit{false} \leftarrow a \wedge b$ bị sai trong $I$, mâu thuẫn với giả thiết $I$ là mô hình của $\mathit{KB}_{1}$.

Do đó, $\neg c$ là đúng trong mọi mô hình của $\mathit{KB}_{1}$, tức là:

$$
\mathit{KB}_{1} \models \neg c.
$$
:::

Mặc dù ngôn ngữ mệnh đề Horn không cho phép nhập vào các phép tuyển và phủ định ở dạng tùy ý, hệ thống vẫn có thể suy dẫn ra phép tuyển của các phủ định nguyên tử.

::: example Ví dụ 5.18: Suy dẫn phép tuyển các nguyên tử phủ định
Xét cơ sở tri thức $\mathit{KB}_{2}$:

$$
\begin{aligned}
&\mathit{false} \leftarrow a \wedge b. \\
&a \leftarrow c. \\
&b \leftarrow d. \\
&b \leftarrow e.
\end{aligned}
$$

Trong mọi mô hình của $\mathit{KB}_{2}$, hoặc $c$ sai hoặc $d$ sai. Nếu cả $c$ và $d$ cùng đúng trong mô hình $I$, thì $a$ và $b$ cũng cùng đúng, khiến ràng buộc toàn vẹn đầu tiên bị vi phạm. Tương tự, hoặc $c$ sai hoặc $e$ sai trong mọi mô hình. Vì vậy:

$$
\begin{aligned}
&\mathit{KB}_{2} \models \neg c \vee \neg d, \\
&\mathit{KB}_{2} \models \neg c \vee \neg e.
\end{aligned}
$$
:::

Một tập hợp các câu tuyển được gọi là **không thể thỏa mãn** (unsatisfiable) nếu nó không tồn tại bất kỳ mô hình nào. Một tập hợp các câu tuyển là **mâu thuẫn có thể chứng minh được** (provably inconsistent) đối với một quy trình chứng minh nếu nguyên tử $\mathit{false}$ có thể được suy dẫn ra từ các câu tuyển đó. Nếu quy trình chứng minh là đúng đắn và đầy đủ, một tập câu tuyển là mâu thuẫn có thể chứng minh được khi và chỉ khi nó không thể thỏa mãn.

Đối với một tập hợp chỉ gồm các mệnh đề xác định, ta luôn luôn tìm được ít nhất một mô hình (chẳng hạn diễn giải gán tất cả các nguyên tử nhận giá trị đúng). Do đó cơ sở tri thức mệnh đề xác định luôn luôn thỏa mãn được. Tuy nhiên, một tập hợp các mệnh đề Horn hoàn toàn có thể rơi vào trạng thái không thể thỏa mãn.

::: example Ví dụ 5.19: Tập mệnh đề Horn không thể thỏa mãn
Tập các câu tuyển $\{a, \mathit{false} \leftarrow a\}$ là không thể thỏa mãn. Không tồn tại bất kỳ diễn giải nào thỏa mãn đồng thời cả hai câu tuyển, bởi cả $a$ và $\mathit{false} \leftarrow a$ không thể cùng nhận giá trị đúng trong bất kỳ diễn giải nào.

Cả quy trình chứng minh từ trên xuống lẫn từ dưới lên đều có thể dùng để chứng minh tính không nhất quán, bằng cách sử dụng $\mathit{false}$ làm câu truy vấn.
:::

Cả quy trình chứng minh từ dưới lên lẫn từ trên xuống đều có thể được dùng để kiểm tra tính mâu thuẫn, bằng cách đặt mục tiêu truy vấn là nguyên tử $\mathit{false}$.

## 5.6.2 Nguyên tử khả giả định và tập xung đột

Lập luận dựa trên mâu thuẫn là một công cụ mạnh mẽ trong giải quyết bài toán:

- Trong lập kế hoạch hành động, việc nhận biết một tập hợp các giả định hành động là bất khả thi giúp tác tử loại bỏ sớm các kế hoạch hỏng.
- Trong thiết kế hệ thống, ta có thể chứng minh rằng một số tổ hợp linh kiện không thể phối hợp hoạt động cùng nhau.
- Trong chẩn đoán sự cố, ta cần chứng minh rằng giả thiết "các linh kiện đều hoạt động bình thường" mâu thuẫn với các dữ liệu đo đạc thực tế của hệ thống, từ đó khoanh vùng linh kiện bị hỏng.

Để thực hiện các tác vụ này, hệ thống cần đưa ra các giả định có thể bị bác bỏ qua mâu thuẫn:

- Một **nguyên tử khả giả định** (assumable) là một nguyên tử được phép đưa vào dưới dạng giả định trong một chứng minh phản chứng. Chứng minh phản chứng sẽ dẫn xuất ra một phép tuyển phủ định của các nguyên tử khả giả định.
- Với một cơ sở tri thức mệnh đề Horn cùng tập hợp các nguyên tử khả giả định tường minh, nếu hệ thống chứng minh được mâu thuẫn ($\mathit{false}$) từ một nhóm giả định nào đó, nó có thể trích xuất ra tổ hợp các giả định không thể đồng thời đúng. Thay vì chứng minh một truy vấn, hệ thống tìm cách chứng minh $\mathit{false}$ và thu thập toàn bộ các nguyên tử khả giả định đã tham gia vào chứng minh đó.

Nếu $\mathit{KB}$ là một tập các mệnh đề Horn, một **xung đột** (conflict) của $\mathit{KB}$ là một tập hợp các nguyên tử khả giả định mà khi kết hợp với $\mathit{KB}$ sẽ kéo theo $\mathit{false}$. Tức là tập $C = \{c_{1}, \ldots, c_{r}\}$ là một xung đột nếu:

$$
\mathit{KB} \cup \{c_{1}, \ldots, c_{r}\} \models \mathit{false}.
$$

Khi đó, hệ quả logic tương ứng thu được là:

$$
\mathit{KB} \models \neg c_{1} \vee \ldots \vee \neg c_{r}.
$$

Một **xung đột tối tiểu** (minimal conflict) là một xung đột sao cho không có bất kỳ tập con thực sự nào của nó cũng là một xung đột.

::: example Ví dụ 5.20: Xác định xung đột tối tiểu
Trong Ví dụ 5.18, nếu tập các nguyên tử khả giả định là $\{c, d, e, f, g, h\}$, thì $\{c, d\}$ và $\{c, e\}$ là các xung đột tối tiểu của $\mathit{KB}_{2}$. Tập $\{c, d, e, h\}$ cũng là một xung đột nhưng không phải là xung đột tối tiểu vì nó chứa tập con $\{c, d\}$.
:::

## 5.6.3 Chẩn đoán sự cố dựa trên tính nhất quán

Việc đưa ra các giả định về việc linh kiện hoạt động bình thường và suy diễn ra những linh kiện nào có thể bất thường chính là nền tảng của **chẩn đoán dựa trên tính nhất quán** (consistency-based diagnosis).

Giả sử một lỗi (fault) là một hỏng hóc trong hệ thống. Mục tiêu là xác định các lỗi tiềm ẩn dựa trên mô hình hoạt động danh định của hệ thống cùng các dữ liệu quan sát được. Bằng cách thiết lập mệnh đề "không có lỗi" là khả giả định, các xung đột logic được dùng để chứng minh sự cố của hệ thống.

```
% Kiến thức nền cho Ví dụ 5.21
light_l1.
light_l2.
live_outside.
live_l1 <- live_w0.
live_l2 <- live_w4.
live_p1 <- live_w3.
live_p2 <- live_w6.
lit_l1 <- light_l1 ^ live_l1 ^ ok_l1.
lit_l2 <- light_l2 ^ live_l2 ^ ok_l2.

live_w0 <- live_w1 ^ up_s2 ^ ok_s2.
live_w0 <- live_w2 ^ down_s2 ^ ok_s2.
live_w1 <- live_w3 ^ up_s1 ^ ok_s1.
live_w2 <- live_w3 ^ down_s1 ^ ok_s1.
live_w3 <- live_w5 ^ ok_cb1.
live_w4 <- live_w3 ^ up_s3 ^ ok_s3.
live_w5 <- live_outside.
live_w6 <- live_w5 ^ ok_cb2.

false <- dark_l1 ^ lit_l1.
false <- dark_l2 ^ lit_l2.

assumable ok_cb1, ok_cb2, ok_s1, ok_s2, ok_s3, ok_l1, ok_l2.
```

Hình 5.8: Cơ sở tri thức Horn và các nguyên tử khả giả định phục vụ chẩn đoán mạch điện.

::: example Ví dụ 5.21: Chẩn đoán sự cố mạch điện từ quan sát xung đột
Xem xét cơ sở tri thức trong Hình 5.8. Các nguyên tử $\mathit{ok}$ thể hiện trạng thái hoạt động bình thường của công tắc, bóng đèn, cầu dao không có quy tắc định nghĩa, nhưng được khai báo là khả giả định.

Một bóng đèn không thể vừa sáng vừa tối, điều này được quy định bởi hai ràng buộc toàn vẹn:

$$
\begin{aligned}
&\mathit{false} \leftarrow \mathit{dark\_l}_{1} \wedge \mathit{lit\_l}_{1}. \\
&\mathit{false} \leftarrow \mathit{dark\_l}_{2} \wedge \mathit{lit\_l}_{2}.
\end{aligned}
$$

Giả sử người dùng quan sát thấy cả ba công tắc đều đang gạt lên, nhưng cả hai bóng đèn $l_{1}$ và $l_{2}$ đều tối:

<pre class="logic-expression">up_s_1.   up_s_2.   up_s_3.   dark_l_1.   dark_l_2.</pre>

Từ cơ sở tri thức và các quan sát này, hệ thống phát hiện hai xung đột tối tiểu:

1. $\{\mathit{ok\_cb}_{1}, \mathit{ok\_s}_{1}, \mathit{ok\_s}_{2}, \mathit{ok\_l}_{1}\}$ (nếu tất cả đều tốt thì đèn $l_{1}$ phải sáng, mâu thuẫn với $\mathit{dark\_l}_{1}$).
2. $\{\mathit{ok\_cb}_{1}, \mathit{ok\_s}_{3}, \mathit{ok\_l}_{2}\}$ (nếu tất cả đều tốt thì đèn $l_{2}$ phải sáng, mâu thuẫn với $\mathit{dark\_l}_{2}$).

Từ đó kéo theo:

<pre class="logic-expression">KB ⊨ ¬ ok_cb_1 ∨ ¬ ok_s_1 ∨ ¬ ok_s_2 ∨ ¬ ok_l_1, 

KB ⊨ ¬ ok_cb_1 ∨ ¬ ok_s_3 ∨ ¬ ok_l_2.</pre>
:::

Một **chẩn đoán dựa trên tính nhất quán** (consistency-based diagnosis) là một tập hợp các nguyên tử khả giả định chứa ít nhất một phần tử của mỗi xung đột tối tiểu; đây chính là bài toán tìm **tập đánh trúng** (hitting set) của tập các xung đột tối tiểu. Một **chẩn đoán tối tiểu** (minimal diagnosis) là một chẩn đoán tối tiểu theo quan hệ bao hàm tập hợp (inclusion-minimal), tức là không có bất kỳ tập con thực sự nào của nó cũng là một chẩn đoán (phân biệt với khái niệm tập có số lượng phần tử ít nhất - minimum cardinality).

::: example Ví dụ 5.22: Phân tích chẩn đoán tối tiểu dưới dạng chuẩn tuyển
Từ hai xung đột trong Ví dụ 5.21, ta có biểu thức dạng chuẩn hội (CNF):

<pre class="logic-expression">(¬ ok_cb_1 ∨ ¬ ok_s_1 ∨ ¬ ok_s_2 ∨ ¬ ok_l_1) ∧ (¬ ok_cb_1 ∨ ¬ ok_s_3 ∨ ¬ ok_l_2).</pre>

Khai triển phân phối biểu thức này sang dạng chuẩn tuyển (DNF), tức là phép tuyển của các phép hội các nguyên tử phủ định, ta thu được:

<pre class="logic-expression">¬ ok_cb_1 ∨ 

(¬ ok_s_1 ∧ ¬ ok_s_3) ∨ (¬ ok_s_1 ∧ ¬ ok_l_2) ∨ 

(¬ ok_s_2 ∧ ¬ ok_s_3) ∨ (¬ ok_s_2 ∧ ¬ ok_l_2) ∨ 

(¬ ok_l_1 ∧ ¬ ok_s_3) ∨ (¬ ok_l_1 ∧ ¬ ok_l_2).</pre>

Như vậy, hệ thống chứng minh được rằng sự cố bắt nguồn từ một lỗi đơn lẻ duy nhất là cầu dao $cb_{1}$ bị hỏng, hoặc rơi vào ít nhất một trong sáu tổ hợp lỗi kép của hai linh kiện.

Các số hạng hội này tương ứng chính xác với 7 chẩn đoán tối tiểu của hệ thống:

<pre class="logic-expression">{ok_cb_1},   {ok_s_1, ok_s_3},   {ok_s_1, ok_l_2}, 

{ok_s_2, ok_s_3},   {ok_s_2, ok_l_2},   {ok_l_1, ok_s_3},   {ok_l_1, ok_l_2}.</pre>
:::

## 5.6.4 Thuật toán tìm tập xung đột

### Cài đặt theo phương pháp từ dưới lên (ATMS)

Quy trình từ dưới lên cho mệnh đề Horn và nguyên tử khả giả định là một phiên bản mở rộng của thuật toán suy diễn tiến. Thay vì chỉ lưu trữ nguyên tử được chứng minh, mỗi kết luận trong tập $C$ là một cặp $\langle a, A \rangle$, trong đó $a$ là một nguyên tử và $A$ là tập các nguyên tử khả giả định kéo theo $a$.

```
Quy trình Prove_conflict_BU(KB, Assumables)
  Đầu vào:
    KB: Tập hợp các mệnh đề Horn
    Assumables: Tập hợp các nguyên tử khả giả định
  Đầu ra:
    Tập hợp các xung đột
  Biến cục bộ:
    C là tập hợp các cặp <a, A>

  1. Khởi tạo C := { <a, {a}> : a thuộc Assumables }
  2. Lặp:
  3.    Chọn mệnh đề "h <- b_1 ^ ... ^ b_m" trong KB sao cho:
        Với mỗi b_i đều có <b_i, A_i> thuộc C, và
        <h, A> chưa thuộc C (với A = A_1 U ... U A_m)
  4.    C := C U { <h, A> }
  5. Cho đến khi: Không còn mệnh đề nào có thể chọn được nữa
  6. Trả về { A : <false, A> thuộc C }
```

Hình 5.9: Thuật toán suy diễn tiến từ dưới lên tìm tập xung đột (ATMS).

Mỗi khi một cặp $\langle \mathit{false}, A \rangle$ được sinh ra, tập các giả định $A$ chính là một xung đột. Thuật toán này chính là hạt nhân của **hệ thống duy trì chân lý dựa trên giả định (ATMS - Assumption-based Truth Maintenance System)**.

Để tối ưu hóa, ta có thể tỉa bỏ các tập giả định bao hàm: Nếu $\langle a, A_{1} \rangle$ và $\langle a, A_{2} \rangle$ cùng thuộc $C$ với $A_{1} \subset A_{2}$, thì cặp $\langle a, A_{2} \rangle$ có thể bị loại bỏ. Tương tự, nếu $\langle \mathit{false}, A_{1} \rangle$ thuộc $C$ và $A_{1} \subseteq A_{2}$, thì mọi cặp $\langle a, A_{2} \rangle$ đều có thể loại bỏ vì $A_{2}$ đã mâu thuẫn.

::: example Ví dụ 5.23: Các bước tích lũy cặp giả định trong ATMS
Trong môi trường mạch điện ở Hình 5.8, ban đầu $C$ chứa các cặp $\langle \mathit{ok}, \{\mathit{ok}\} \rangle$. Khi các sự kiện quan sát được đưa vào, chuỗi suy diễn tiến sinh ra các cặp:

$$
\begin{aligned}
&\langle \mathit{live\_w}_{3}, \{\mathit{ok\_cb}_{1}\} \rangle \\
&\langle \mathit{live\_w}_{4}, \{\mathit{ok\_cb}_{1}, \mathit{ok\_s}_{3}\} \rangle \\
&\langle \mathit{lit\_l}_{2}, \{\mathit{ok\_cb}_{1}, \mathit{ok\_s}_{3}, \mathit{ok\_l}_{2}\} \rangle \\
&\langle \mathit{false}, \{\mathit{ok\_cb}_{1}, \mathit{ok\_s}_{3}, \mathit{ok\_l}_{2}\} \rangle
\end{aligned}
$$

Do đó, tập $\{\mathit{ok\_cb}_{1}, \mathit{ok\_s}_{3}, \mathit{ok\_l}_{2}\}$ được kết luận là một xung đột.
:::

### Cài đặt theo phương pháp từ trên xuống

Quy trình từ trên xuống bắt đầu với truy vấn cần chứng minh là $\mathit{false}$. Khi gặp một nguyên tử khả giả định trong quá trình phân giải, thuật toán không tìm quy tắc để phân giải tiếp mà giữ lại nguyên tử đó trong tập mục tiêu.

```
Quy trình không tất định Prove_conflict_TD(KB, Assumables)
  Đầu vào:
    KB: Tập hợp các mệnh đề Horn
    Assumables: Tập hợp các nguyên tử khả giả định
  Đầu ra:
    Một tập xung đột
  Biến cục bộ:
    G là tập hợp các nguyên tử

  1. G := {false}
  2. Lặp:
  3.    Chọn một nguyên tử a trong G sao cho a không thuộc Assumables
  4.    Lựa chọn mệnh đề "a <- B" trong KB có đầu là a
  5.    G := (G \ {a}) U B
  6. Cho đến khi: G là tập con của Assumables
  7. Trả về G
```

Hình 5.10: Thuật toán suy diễn lùi từ trên xuống tìm tập xung đột.

::: example Ví dụ 5.24: Dẫn xuất suy diễn lùi tìm xung đột
Bắt đầu với $G_{0} = \{\mathit{false}\}$, thuật toán chọn phân giải với ràng buộc $\mathit{false} \leftarrow \mathit{dark\_l}_{1} \wedge \mathit{lit\_l}_{1}$. Vì $\mathit{dark\_l}_{1}$ là sự kiện quan sát đã biết, tập mục tiêu thu hẹp về $\{\mathit{lit\_l}_{1}\}$. Tiếp tục phân giải qua các quy tắc của mạch điện, $G$ lần lượt nhận các giá trị cho đến khi chỉ còn lại toàn các nguyên tử khả giả định:

<pre class="logic-expression">G = {ok_cb_1, ok_s_1, ok_s_2, ok_l_1}.</pre>

Thuật toán dừng và trả về tập này dưới dạng một xung đột hoàn chỉnh.
:::

## Tài liệu tham khảo

1. Poole, D. L., & Mackworth, A. K. (2023). *Artificial Intelligence: Foundations of Computational Agents* (3rd ed.). Chapter 5: Propositions and Inference. Cambridge University Press. Bản gốc trực tuyến: [ArtInt3e.Ch5.S6.html](https://artint.info/3e/html/ArtInt3e.Ch5.S6.html).
2. de Kleer, J. (1986). An assumption-based TMS. *Artificial Intelligence*, 28(2), 127–162.
3. Reiter, R. (1987). A theory of diagnosis from first principles. *Artificial Intelligence*, 32(1), 57–95.
