---
course: ai-nen-tang-tac-tu
lecture: 05-menh-de-va-suy-dien
section: topic
topic: 5-7-gia-thiet-tri-thuc-day-du
title: "5.7 Giả thiết tri thức đầy đủ"
description: "Giả thiết thế giới đóng (CWA), phép bao đóng Clark, phủ định như một thất bại (NAF), lập luận phi đơn điệu cùng các quy trình chứng minh tiến và lùi."
---

Một cơ sở dữ liệu thường mang tính trọn vẹn theo nghĩa: Bất kỳ sự kiện nào không được khẳng định hoặc không suy ra được từ cơ sở dữ liệu thì mặc định được coi là sai.

::: example Ví dụ 5.25: Trực giác về giá trị mặc định trong mạch điện
Người thiết kế có thể mong muốn người dùng chỉ cần khai báo công tắc nào đang bật lên ($\mathit{up}$) và cầu dao nào đang bị hỏng ($\mathit{broken}$), để từ đó hệ thống tự động suy ra rằng mọi công tắc không được nhắc đến thì đang gạt xuống ($\mathit{down}$), và mọi cầu dao không bị khai báo hỏng thì đang hoạt động tốt ($\mathit{ok}$).

Như vậy, trạng thái gạt xuống là giá trị mặc định của công tắc, và trạng thái tốt là giá trị mặc định của cầu dao. Việc giao tiếp dựa trên các giá trị mặc định giúp tiết kiệm công sức mô tả những thông tin hiển nhiên. Để suy luận được với các giá trị mặc định này, tác tử phải giả định rằng mình có **tri thức đầy đủ**: Việc một công tắc không được nhắc tới đồng nghĩa với việc nó đang gạt xuống, chứ không phải vì tác tử không biết tình trạng của nó.
:::

Logic mệnh đề xác định thuần túy không cho phép rút ra kết luận từ sự thiếu hụt tri thức hoặc từ sự thất bại trong chứng minh. Nó không giả định rằng tri thức là trọn vẹn. Đặc biệt, phủ định của một nguyên tử không bao giờ có thể là hệ quả logic của một cơ sở tri thức gồm toàn mệnh đề xác định.

**Giả thiết tri thức đầy đủ** (complete knowledge assumption) giả định rằng đối với mỗi nguyên tử, các mệnh đề có nguyên tử đó ở phần đầu đã bao quát toàn bộ các trường hợp mà nguyên tử đó nhận giá trị đúng. Cụ thể: Một nguyên tử không có quy tắc nào định nghĩa ở phần đầu sẽ mặc định nhận giá trị sai. Dưới giả thiết này, tác tử có thể kết luận một nguyên tử là sai nếu không thể chứng minh được nó là đúng.

Giả thiết này còn được gọi là **giả thiết thế giới đóng** (closed-world assumption - CWA). Nó đối lập với **giả thiết thế giới mở** (open-world assumption - OWA), vốn thừa nhận rằng tác tử không biết hết mọi sự thật và do đó không thể kết luận điều gì chỉ từ sự thiếu hụt thông tin. Giả thiết thế giới đóng đòi hỏi mọi sự thật liên quan về thế giới đều phải được tác tử nắm rõ.

## 5.7.1 Phép bao đóng Clark (Clark's Completion)

Giả thiết cho rằng mỗi nguyên tử đều có một định nghĩa trọn vẹn thông qua các mệnh đề chính là nền tảng của lập trình logic.

Giả sử các mệnh đề có đầu là nguyên tử $a$ trong cơ sở tri thức là:

$$
\begin{aligned}
&a \leftarrow b_{1}. \\
&\vdots \\
&a \leftarrow b_{n}.
\end{aligned}
$$

trong đó một sự kiện nguyên tử $a.$ được xem tương đương với quy tắc $a \leftarrow \mathit{true}$.

Các mệnh đề trên đã khẳng định chiều suy luận thuận: $b_{1} \vee \ldots \vee b_{n} \rightarrow a$. Giả thiết tri thức đầy đủ bổ sung thêm chiều suy luận ngược lại: Nếu $a$ đúng trong một diễn giải nào đó, thì bắt buộc một trong các thân quy tắc $b_{i}$ phải đúng, tức là:

$$
a \rightarrow b_{1} \vee \ldots \vee b_{n}.
$$

Kết hợp cả hai chiều suy luận, ý nghĩa trọn vẹn của các quy tắc định nghĩa $a$ chính là công thức tương đương logic:

$$
a \leftrightarrow b_{1} \vee \ldots \vee b_{n}.
$$

Phép tương đương này được gọi là **phép bao đóng Clark** (Clark's completion) cho nguyên tử $a$. Phép bao đóng của cả cơ sở tri thức là tập hợp các phép bao đóng của từng nguyên tử xuất hiện trong cơ sở tri thức đó.

Nếu một nguyên tử $a$ hoàn toàn không có mệnh đề nào quy định ở phần đầu, thì phép bao đóng của nó là $a \leftrightarrow \mathit{false}$, đồng nghĩa với việc $a$ nhận giá trị sai.

::: example Ví dụ 5.26: Phép bao đóng Clark cho hệ thống mạch điện
Xét các mệnh đề trong hệ thống mạch điện:

<span class="logic-expression logic-block">down_s_1.   up_s_2.   ok_cb_1.   live_outside. &#10;&#10;live_l_1 ← live_w_0. &#10;&#10;live_w_0 ← live_w_1 ∧ up_s_2. &#10;&#10;live_w_0 ← live_w_2 ∧ down_s_2. &#10;&#10;live_w_1 ← live_w_3 ∧ up_s_1. &#10;&#10;live_w_2 ← live_w_3 ∧ down_s_1. &#10;&#10;live_w_3 ← live_outside ∧ ok_cb_1.</span>

Giả sử không có quy tắc nào cho các nguyên tử $\mathit{up\_s}_{1}$ và $\mathit{down\_s}_{2}$. Khi đó phép bao đóng Clark của các nguyên tử là:

<span class="logic-expression logic-block">down_s_1 ↔ true. &#10;&#10;up_s_1 ↔ false. &#10;&#10;up_s_2 ↔ true. &#10;&#10;down_s_2 ↔ false. &#10;&#10;ok_cb_1 ↔ true. &#10;&#10;live_l_1 ↔ live_w_0. &#10;&#10;live_w_0 ↔ (live_w_1 ∧ up_s_2) ∨ (live_w_2 ∧ down_s_2). &#10;&#10;live_w_1 ↔ live_w_3 ∧ up_s_1. &#10;&#10;live_w_2 ↔ live_w_3 ∧ down_s_1. &#10;&#10;live_w_3 ↔ live_outside ∧ ok_cb_1. &#10;&#10;live_outside ↔ true.</span>

Phép bao đóng này kéo theo rằng $\mathit{up\_s}_{1}$ sai, $\mathit{live\_w}_{1}$ sai, và $\mathit{live\_w}_{2}$ đúng.
:::

Nhờ phép bao đóng, hệ thống có thể suy dẫn ra các mệnh đề phủ định. Ta mở rộng ngôn ngữ để cho phép các phủ định xuất hiện ngay trong phần thân của quy tắc. Phủ định của nguyên tử $a$ dưới giả thiết tri thức đầy đủ được ký hiệu là $\sim a$ để phân biệt với phép phủ định cổ điển $\neg a$. Phép phủ định này được gọi là **phủ định như một thất bại** (negation as failure - NAF).

Một câu hỏi truy vấn được xem là hệ quả logic dưới giả thiết tri thức đầy đủ nếu nó được kéo theo bởi phép bao đóng Clark của cơ sở tri thức.

::: example Ví dụ 5.27: Khai báo mặc định bằng phủ định như một thất bại
Ta có thể đơn giản hóa việc mô hình hóa bằng cách chỉ yêu cầu người dùng khai báo các công tắc đang bật lên, và hệ thống tự động kết luận công tắc đang gạt xuống nếu không có thông tin bật:

$$
\begin{aligned}
&\mathit{down\_s}_{1} \leftarrow \sim \mathit{up\_s}_{1}. \\
&\mathit{down\_s}_{2} \leftarrow \sim \mathit{up\_s}_{2}. \\
&\mathit{down\_s}_{3} \leftarrow \sim \mathit{up\_s}_{3}. \\
&\mathit{ok\_cb}_{1} \leftarrow \sim \mathit{broken\_cb}_{1}. \\
&\mathit{ok\_cb}_{2} \leftarrow \sim \mathit{broken\_cb}_{2}.
\end{aligned}
$$

Khi người dùng chỉ cần quan sát và nhập:

$$
\mathit{up\_s}_{2}. \quad \mathit{up\_s}_{3}.
$$

Hệ thống tự động suy ra $\mathit{down\_s}_{1}$ đúng, $\mathit{ok\_cb}_{1}$ đúng, và $\mathit{ok\_cb}_{2}$ đúng.
:::

Một cơ sở tri thức là phi chu trình (acyclic) nếu có thể gán cho mỗi nguyên tử một số tự nhiên sao cho các nguyên tử ở phần thân luôn có số thứ tự nhỏ hơn nguyên tử ở phần đầu. Nếu cơ sở tri thức có chu trình kết hợp với phủ định, ngữ nghĩa sẽ trở nên mâu thuẫn hoặc nhập nhằng (chẳng hạn $a \leftarrow \sim b$ và $b \leftarrow \sim a$ dẫn đến $a \leftrightarrow \neg b$; hoặc $a \leftarrow \sim a$ dẫn đến nghịch lý $a \leftrightarrow \neg a$). Phép bao đóng của một cơ sở tri thức phi chu trình luôn luôn nhất quán và xác định duy nhất chân trị cho mọi nguyên tử.

## 5.7.2 Suy luận phi đơn điệu (Non-Monotonic Reasoning)

Một hệ logic được gọi là **đơn điệu** (monotonic) nếu bất kỳ mệnh đề nào đã suy ra được từ cơ sở tri thức thì vẫn tiếp tục suy ra được khi bổ sung thêm các mệnh đề mới vào cơ sở tri thức. Logic mệnh đề xác định thuần túy là một hệ logic đơn điệu.

Một hệ logic được gọi là **phi đơn điệu** (non-monotonic) nếu việc bổ sung thêm tri thức mới có thể làm mất đi tính hợp lệ của những kết luận đã rút ra trước đó. Logic mệnh đề với cơ chế phủ định như một thất bại chính là một hệ logic phi đơn điệu.

Suy luận phi đơn điệu đặc biệt hữu ích trong việc biểu diễn các luật mặc định (defaults). Một luật mặc định là một quy tắc được áp dụng tự động, trừ phi nó bị ghi đè bởi một trường hợp ngoại lệ.

Cấu trúc chuẩn của một luật mặc định thường có dạng:

$$
b \leftarrow c \wedge \sim \mathit{ab\_a}.
$$

trong đó $\mathit{ab\_a}$ là nguyên tử đại diện cho trạng thái bất thường (abnormal) đối với khía cạnh $a$. Khi có điều kiện $c$, tác tử mặc định suy ra $b$, trừ khi được thông báo rằng trường hợp bất thường $\mathit{ab\_a}$ đã xảy ra.

::: example Ví dụ 5.28: Lập luận phi đơn điệu trong tư vấn du lịch
Xét tác tử hỗ trợ mua sắm các gói kỳ nghỉ:

- Một khu nghỉ dưỡng mặc định được xem là ở xa bãi biển nếu không có thông tin khẳng định nó nằm sát biển:
 
 <span class="logic-expression logic-block">away_from_beach ← ∼ on_beach.</span>
- Nếu ở sát biển, khách mặc định có lối đi ra biển:
 
 <span class="logic-expression logic-block">beach_access ← on_beach ∧ ∼ ab_beach_access.</span>
- Nếu có lối ra biển, khách mặc định có thể bơi lội:
 
 <span class="logic-expression logic-block">swim_at_beach ← beach_access ∧ ∼ ab_swim_at_beach.</span>
- Tuy nhiên, nếu khu nghỉ dưỡng nằm trong vịnh kín cạnh một thành phố lớn, thì mặc định nước bị ô nhiễm và không được bơi:
 
 <span class="logic-expression logic-block">ab_swim_at_beach ← enclosed_bay ∧ big_city ∧ ∼ ab_no_swimming_near_city.</span>
- Nhưng nếu thành phố đó thuộc tỉnh British Columbia (BC, nơi xử lý nước thải rất nghiêm ngặt), ngoại lệ này lại bị hủy bỏ và du khách vẫn bơi được:
 
 <span class="logic-expression logic-block">ab_no_swimming_near_city ← in_BC ∧ ∼ ab_BC_beaches.</span>
Chuỗi suy luận phi đơn điệu thể hiện tính thích ứng linh hoạt:

1. Ban đầu chỉ có các luật, tác tử suy ra $\mathit{away\_from\_beach}$.
2. Khi được cung cấp thông tin $\mathit{on\_beach}$, kết luận $\mathit{away\_from\_beach}$ bị thu hồi, thay vào đó tác tử suy ra $\mathit{beach\_access}$ và $\mathit{swim\_at\_beach}$.
3. Khi được thông báo thêm $\mathit{enclosed\_bay}$ và $\mathit{big\_city}$, kết luận $\mathit{swim\_at\_beach}$ bị thu hồi (không được bơi).
4. Nhưng nếu sau đó biết thêm khu nghỉ dưỡng nằm ở $\mathit{in\_BC}$, tác tử lại phục hồi kết luận $\mathit{swim\_at\_beach}$ (được bơi).
:::

## 5.7.3 Các quy trình chứng minh cho phủ định như một thất bại

### Thuật toán suy diễn tiến từ dưới lên

Thuật toán từ dưới lên mở rộng cho phủ định như một thất bại bổ sung thêm các từ vị dạng $\sim p$ vào tập kết luận $C$ mỗi khi xác định được chắc chắn rằng nguyên tử $p$ bắt buộc phải thất bại:

Một nguyên tử $p$ thất bại khi mọi mệnh đề có $p$ ở phần đầu đều thất bại. Một mệnh đề thất bại khi có ít nhất một điều kiện trong phần thân của nó bị thất bại.

```
Quy trình Prove_NAF_BU(KB)
  Đầu vào:
    KB: Tập hợp các mệnh đề có thể chứa phủ định như một thất bại
  Đầu ra:
    Tập hợp C chứa các từ vị suy ra được từ phép bao đóng của KB
  Biến cục bộ:
    C là tập hợp các từ vị

  1. Khởi tạo C := {}
  2. Lặp:
  3.    Hoặc chọn một mệnh đề "h <- b_1 ^ ... ^ b_m" trong KB sao cho:
        Mọi b_i đều thuộc C, và h chưa thuộc C:
  4.       C := C U {h}
  5.    Hoặc chọn nguyên tử h sao cho ~h chưa thuộc C và:
        Với MỌI mệnh đề "h <- b_1 ^ ... ^ b_m" trong KB, đều có
        hoặc một b_i sao cho ~b_i thuộc C,
        hoặc một b_i = ~g mà g thuộc C:
  6.       C := C U {~h}
  7. Cho đến khi: Không thể chọn thêm phần tử nào nữa
  8. Trả về C
```

Hình 5.11: Thuật toán suy diễn tiến từ dưới lên với phủ định như một thất bại.

::: example Ví dụ 5.29: Từng bước tích lũy trong suy diễn tiến NAF
Xét cơ sở tri thức gồm các mệnh đề:

$$
\begin{aligned}
&p \leftarrow q \wedge \sim r. \\
&p \leftarrow s. \\
&q \leftarrow \sim s. \\
&r \leftarrow \sim t. \\
&t. \\
&s \leftarrow w.
\end{aligned}
$$

Chuỗi tích lũy các từ vị vào tập $C$:

1. $t$ được thêm vào do là một sự kiện nguyên tử ($t \in C$).
2. Vì $t \in C$, điều kiện $\sim t$ trong quy tắc của $r$ bị thất bại. Vì $r$ chỉ có duy nhất quy tắc này nên mọi quy tắc của $r$ đều thất bại, dẫn đến $\sim r \in C$.
3. Nguyên tử $w$ không có bất kỳ quy tắc nào định nghĩa ở phần đầu, điều kiện phủ định tự động thỏa mãn, dẫn đến $\sim w \in C$.
4. Quy tắc duy nhất của $s$ là $s \leftarrow w$ có $w$ thất bại ($\sim w \in C$), do đó $\sim s \in C$.
5. Trong quy tắc $q \leftarrow \sim s$, vì $\sim s \in C$ nên toàn bộ phần thân đúng, suy ra $q \in C$.
6. Trong quy tắc $p \leftarrow q \wedge \sim r$, cả $q \in C$ và $\sim r \in C$ đều đã được chứng minh, do đó $p \in C$.

Tập kết quả cuối cùng là $C = \{t, \sim r, \sim w, \sim s, q, p\}$.
:::

### Thuật toán suy diễn lùi từ trên xuống

Thuật toán từ trên xuống xử lý phủ định như một thất bại bằng cách kích hoạt một quy trình chứng minh con độc lập. Khi chọn một mục tiêu phụ dạng $\sim a$, thuật toán khởi động một chứng minh cho nguyên tử khẳng định $a$:

- Nếu chứng minh cho $a$ thất bại hữu hạn, thì mục tiêu phụ $\sim a$ được công nhận thành công và bị loại bỏ khỏi danh sách mục tiêu.
- Nếu chứng minh cho $a$ thành công, thì nhánh suy diễn chứa $\sim a$ thất bại hoàn toàn và thuật toán phải quay lui để tìm lựa chọn khác.

```
Quy trình không tất định Prove_NAF_TD(KB, Query)
  Đầu vào:
    KB: Cơ sở tri thức có thể chứa phủ định như một thất bại
    Query: Tập hợp các từ vị cần chứng minh
  Đầu ra:
    yes nếu phép bao đóng của KB kéo theo Query; ngược lại thất bại
  Biến cục bộ:
    G là tập hợp các từ vị

  1. G := Query
  2. Lặp:
  3.    Chọn một từ vị l trong G
  4.    Nếu l có dạng ~a:
  5.       Nếu Prove_NAF_TD(KB, a) thất bại:
  6.          G := G \ {l}
  7.       Ngược lại:
  8.          Thất bại (fail)
  9.    Ngược lại:
 10.       Lựa chọn mệnh đề "l <- B" trong KB có đầu là l
 11.       G := (G \ {l}) U B
 12. Cho đến khi: G = {}
 13. Trả về yes
```

Hình 5.12: Thuật toán suy diễn lùi từ trên xuống với phủ định như một thất bại.

::: example Ví dụ 5.30: Dẫn xuất suy diễn lùi với truy vấn phủ định
Với cơ sở tri thức ở Ví dụ 5.29 và truy vấn $\mathbf{ask} \; p$:

1. $G_{0} = \{p\}$. Áp dụng quy tắc $p \leftarrow q \wedge \sim r$, ta có $G_{1} = \{q, \sim r\}$.
2. Chọn $q$, phân giải với $q \leftarrow \sim s$, ta có $G_{2} = \{\sim s, \sim r\}$.
3. Chọn $\sim s$, khởi động chứng minh con cho $s$. Quy tắc duy nhất $s \leftarrow w$ dẫn tới mục tiêu $w$. Vì không có quy tắc nào cho $w$, chứng minh cho $w$ thất bại, kéo theo chứng minh cho $s$ thất bại. Do đó mục tiêu phụ $\sim s$ thành công, tập mục tiêu còn lại $G_{3} = \{\sim r\}$.
4. Chọn $\sim r$, khởi động chứng minh con cho $r$. Quy tắc $r \leftarrow \sim t$ dẫn tới chứng minh con cho $t$. Sự kiện $t.$ làm chứng minh cho $t$ thành công, khiến $\sim t$ thất bại, do đó chứng minh cho $r$ thất bại. Vì $r$ không còn quy tắc nào khác, chứng minh cho $r$ thất bại, giúp mục tiêu phụ $\sim r$ thành công.
5. Tập mục tiêu trở nên rỗng: $G_{4} = \{\}$. Thuật toán trả về kết luận **yes**.
:::

Lưu ý rằng thuật toán này hiện thực hóa khái niệm thất bại hữu hạn (finite failure). Nếu một chứng minh rơi vào vòng lặp vô tận (chẳng hạn với quy tắc $p \leftarrow p$), thuật toán không thể dừng lại và một quy trình đúng đắn không được phép vội vã kết luận $\sim p$.

## Tài liệu tham khảo

1. Poole, D. L., & Mackworth, A. K. (2023). *Artificial Intelligence: Foundations of Computational Agents* (3rd ed.). Chapter 5: Propositions and Inference. Cambridge University Press.
2. Clark, K. L. (1978). Negation as failure. In H. Gallaire & J. Minker (Eds.), *Logic and Data Bases* (pp. 293–322). Plenum Press.
3. Reiter, R. (1980). A logic for default reasoning. *Artificial Intelligence*, 13(1–2), 81–132.
4. Gelfond, M., & Lifschitz, V. (1988). The stable model semantics for logic programming. In *Proceedings of the 5th International Conference and Symposium on Logic Programming* (pp. 1070–1080).


[Đọc mục tương ứng trong giáo trình](https://artint.info/3e/html/ArtInt3e.Ch5.S7.html).
