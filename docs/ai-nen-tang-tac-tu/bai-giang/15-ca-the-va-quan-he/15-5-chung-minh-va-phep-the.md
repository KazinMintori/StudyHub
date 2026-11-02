---
course: ai-nen-tang-tac-tu
lecture: 15-ca-the-va-quan-he
section: topic
topic: 15-5-chung-minh-va-phep-the
title: "15.5 Chứng minh và phép thế"
description: "Cơ chế suy luận trong Datalog: Phép thế, hợp nhất (unification), thủ tục suy diễn tiến trên mô hình Herbrand và giải thuật giải quyết SLD suy diễn lùi."
---

Cả hai thủ tục chứng minh suy diễn tiến (bottom-up) và suy diễn lùi (top-down) trong logic mệnh đề đều có thể mở rộng sang ngôn ngữ Datalog. Khi có biến logic, một biến tự do trong câu tuyển đồng nghĩa với việc mọi thể hiện của câu tuyển đó đều đúng. Do đó, một quá trình chứng minh hoàn chỉnh có thể phải sử dụng nhiều thể hiện khác nhau của cùng một luật suy diễn.

## 15.5.1 Thể hiện và phép thế (Instances and Substitutions)

Một **thể hiện** (instance) của một câu tuyển thu được bằng cách thay thế các biến bằng các số hạng một cách nhất quán (tất cả các lần xuất hiện của cùng một biến đều được thay thế bởi cùng một số hạng).

Quy tắc gán giá trị cho từng biến được gọi là một **phép thế** (substitution):

- Một phép thế $\sigma$ là một tập hợp các phép gán có dạng:

  $$
  \sigma = \{V_{1}/t_{1}, \ldots, V_{n}/t_{n}\}
  $$

  Trong đó, mỗi $V_{i}$ là một biến logic phân biệt và mỗi $t_{i}$ là một số hạng. Phần tử $V_{i}/t_{i}$ được gọi là một phép ràng buộc (binding) cho biến $V_{i}$.
- Một phép thế ở **dạng chuẩn** (normal form) nếu không có bất kỳ biến $V_{i}$ nào ở vế trái lại xuất hiện bên trong bất kỳ số hạng $t_{j}$ nào ở vế phải.

::: example Ví dụ 15.14: Phép thế dạng chuẩn
Phép thế:

$$
\sigma = \{X/Y, Z/chile\}
$$

là một phép thế ở dạng chuẩn, vì hai biến vế trái ($X$ và $Z$) không hề xuất hiện ở vế phải.

Ngược lại, phép thế $\{X/Y, Z/X\}$ không ở dạng chuẩn, vì biến $X$ vừa xuất hiện ở vế trái (được gán bằng $Y$), vừa xuất hiện ở vế phải (làm giá trị gán cho $Z$).
:::

Khi áp dụng phép thế $\sigma$ lên một biểu thức $e$ (ký hiệu là $e\sigma$), ta thu được một biểu thức mới giống hệt $e$ ngoại trừ mọi lần xuất hiện của biến $V_{i}$ đều được thay bằng $t_{i}$. Biểu thức $e\sigma$ được gọi là một thể hiện của $e$. Nếu $e\sigma$ không còn chứa bất kỳ biến nào, nó được gọi là một **thể hiện không biến** (ground instance).

::: example Ví dụ 15.15: Áp dụng phép thế
Xét các phép áp dụng sau:

- <code class="logic-expression">borders(peru, X){X/chile} = borders(peru, chile)</code>
- <code class="logic-expression">borders(Y, chile){Y/peru} = borders(peru, chile)</code>
- <code class="logic-expression">borders(peru, X){Y/peru, Z/X} = borders(peru, X)</code> (do $Y$ và $Z$ không xuất hiện trong biểu thức)
- <code class="logic-expression">p(X, X, Y, Y, Z){X/Z, Y/brazil} = p(Z, Z, brazil, brazil, Z)</code>

Phép thế áp dụng đồng nhất lên cả câu tuyển: Áp dụng $\{X/Y, Z/peru\}$ lên câu tuyển:

$$
p(X, Y) \leftarrow q(peru, Z, X, Y, Z)
$$

cho kết quả:

<pre class="logic-expression">p(Y, Y) ← q(peru, peru, Y, Y, peru)</pre>
:::

Một phép thế $\sigma$ được gọi là một **bộ hợp nhất** (unifier) của hai biểu thức $e_{1}$ và $e_{2}$ nếu:

$$
e_{1}\sigma = e_{2}\sigma
$$

Khi đó, ta nói hai biểu thức $e_{1}$ và $e_{2}$ **hợp nhất được với nhau** (unify).

::: example Ví dụ 15.16: Hợp nhất hai nguyên tử
Phép thế $\{X/chile, Y/peru\}$ là một bộ hợp nhất của hai nguyên tử $borders(peru, X)$ và $borders(Y, chile)$, vì khi áp dụng vào biểu thức nào cũng đều cho ra:

$$
borders(peru, chile)
$$

Tương tự, phép thế $\{X/a, Y/b\}$ là một bộ hợp nhất của $t(a, Y, c)$ và $t(X, b, c)$:

<pre class="logic-expression">t(a, Y, c){X/a, Y/b} = t(X, b, c){X/a, Y/b} = t(a, b, c)</pre>
:::

::: example Ví dụ 15.17: Các bộ hợp nhất khả dĩ của hai nguyên tử
Hai nguyên tử $p(X, Y)$ và $p(Z, Z)$ có nhiều bộ hợp nhất khác nhau, bao gồm:

- $\{X/b, Y/b, Z/b\}$
- $\{X/c, Y/c, Z/c\}$
- $\{X/Z, Y/Z\}$
- $\{Y/X, Z/X\}$

Hai bộ hợp nhất cuối cùng ($\{X/Z, Y/Z\}$ và $\{Y/X, Z/X\}$) mang tính tổng quát hơn hai bộ hợp nhất đầu tiên. Lý do là hai bộ hợp nhất đầu tiên đều ràng buộc $X$ giống $Z$ và $Y$ giống $Z$, nhưng lại cam kết gán cụ thể các giá trị đó thành $b$ hoặc $c$.
:::

Phép thế $\sigma$ là **bộ hợp nhất tổng quát nhất** (Most General Unifier — MGU) của hai biểu thức $e_{1}$ và $e_{2}$ nếu:

- $\sigma$ là một bộ hợp nhất của hai biểu thức đó, và
- Nếu phép thế $\sigma'$ cũng là một bộ hợp nhất của $e_{1}$ và $e_{2}$, thì $e\sigma'$ phải là một thể hiện của $e\sigma$ đối với mọi biểu thức $e$.

::: example Ví dụ 15.18: Bộ hợp nhất tổng quát nhất
Xét lại hai nguyên tử $p(X, Y)$ và $p(Z, Z)$:

- Cả hai phép thế $\{X/Z, Y/Z\}$ và $\{Z/X, Y/X\}$ đều là các bộ hợp nhất tổng quát nhất (MGU) của $p(X, Y)$ và $p(Z, Z)$.
- Phép thế $\{X/a, Y/a, Z/a\}$ là một bộ hợp nhất, nhưng không phải là bộ hợp nhất tổng quát nhất.

Kết quả khi áp dụng các phép thế này lần lượt là:

<pre class="logic-expression">p(X, Y){X/Z, Y/Z} = p(Z, Z){X/Z, Y/Z} = p(Z, Z)</pre>

<pre class="logic-expression">p(X, Y){Z/X, Y/X} = p(Z, Z){Z/X, Y/X} = p(X, X)</pre>

<pre class="logic-expression">p(X, Y){X/a, Y/a, Z/a} = p(Z, Z){X/a, Y/a, Z/a} = p(a, a)</pre>

Biểu thức $p(a, a)$ là một thể hiện của $p(Z, Z)$, nhưng $p(Z, Z)$ không thể là một thể hiện của $p(a, a)$.
:::

Biểu thức $e_{1}$ là một **bản đổi tên** (renaming) của $e_{2}$ nếu chúng chỉ khác nhau về tên gọi của các biến. Mọi MGU của hai biểu thức đều tương đương với nhau qua phép đổi tên biến.

## 15.5.2 Thủ tục suy diễn tiến cho Datalog (Bottom-Up Procedure for Datalog)

Thủ tục suy diễn tiến trong Datalog áp dụng trực tiếp thủ tục mệnh đề ([Mục 5.3.2](https://artint.info/3e/html/ArtInt3e.Ch5.S3.html#SS2.SSSx1)) lên tập hợp tất cả các thể hiện không biến (ground instances) của cơ sở tri thức:

::: example Ví dụ 15.19: Dẫn xuất tiến trên tập thể hiện không biến
Giả sử cơ sở tri thức gồm các câu tuyển:

```prolog
q(a).
q(b).
r(a).
s(W) :- r(W).
p(X, Y) :- q(X), s(Y).
```

Tập hợp tất cả các thể hiện không biến được tạo ra từ hai hằng số $a$ và $b$ là:

```prolog
q(a).
q(b).
r(a).
s(a) :- r(a).
s(b) :- r(b).
p(a, a) :- q(a), s(a).
p(a, b) :- q(a), s(b).
p(b, a) :- q(b), s(a).
p(b, b) :- q(b), s(b).
```

Áp dụng thủ tục suy diễn tiến mệnh đề lên tập thể hiện không biến này, ta lần lượt rút ra các hệ quả logic không biến:

<pre class="logic-expression">q(a),   q(b),   r(a),   s(a),   p(a, a),   p(b, a)</pre>
:::

::: example Ví dụ 15.20: Trường hợp truy vấn không chứa hằng số
Giả sử cơ sở tri thức là:

```prolog
p(X, Y).
g :- p(W, W).
```

Để trả lời câu hỏi truy vấn `ask g`, thủ tục suy diễn tiến cần tạo ra một ký hiệu hằng số mới, chẳng hạn ký hiệu $c$. Khi đó, tập hợp các thể hiện không biến là:

```prolog
p(c, c).
g :- p(c, c).
```

Thủ tục suy diễn tiến mệnh đề sẽ rút ra được $p(c, c)$ và $g$.

Nếu câu hỏi truy vấn là `ask p(b, d)`, tập hợp các thể hiện không biến sẽ thay đổi để phản ánh các hằng số $b$ và $d$.
:::

Thủ tục suy diễn tiến áp dụng cho tập thể hiện không biến bảo đảm tính đúng đắn (soundness), vì mỗi thể hiện của mỗi luật đều đúng trong mọi mô hình. Đối với Datalog (không chứa ký hiệu hàm), thủ tục này chắc chắn dừng vì số lượng các nguyên tử không biến là hữu hạn.

## 15.5.3 Hợp nhất (Unification)

Thuật toán tìm MGU giữa hai số hạng hoặc nguyên tử $t_1, t_2$ đưa bài toán về việc giải một hệ phương trình cú pháp:

```
procedure Unify(t1, t2)
    Đầu vào: Hai nguyên tử hoặc số hạng t1, t2
    Đầu ra: MGU của t1 và t2 nếu tồn tại; ngược lại trả về fail (⊥)
    Biến cục bộ: Tập các phương trình E; phép thế S ở dạng chuẩn

    E := {t1 = t2}
    S := {}

    while E ≠ {} do
        chọn và loại bỏ phương trình α = β khỏi E
        if β không trùng hệt α then
            if α là một biến then
                thay thế α bằng β trong toàn bộ E và S
                S := {α / β} ∪ S
            else if β là một biến then
                thay thế β bằng α trong toàn bộ E và S
                S := {β / α} ∪ S
            else if α có dạng p(α1, ..., αn) và β có dạng p(β1, ..., βn) then
                E := E ∪ {α1 = β1, ..., αn = βn}
            else
                return ⊥    // Không cùng vị từ, khác số ngôi hoặc hằng số khác nhau

    return S
```

::: example Ví dụ 15.21: Lần vết thuật toán Unify
Xét lời gọi `Unify(p(X, Y, Y), p(a, Z, b))`:

1. Ban đầu: $E = \{p(X, Y, Y) = p(a, Z, b)\}$, $S = \{\}$.
2. Phân rã theo vị từ: $E = \{X = a, Y = Z, Y = b\}$.
3. Chọn $X = a$: Vì $X$ là biến, ta thêm $X/a$ vào $S$. Lúc này $S = \{X/a\}$, $E = \{Y = Z, Y = b\}$.
4. Chọn $Y = Z$: Thay thế $Y$ bằng $Z$, cập nhật $S = \{X/a, Y/Z\}$, $E = \{Z = b\}$.
5. Chọn $Z = b$: Thay thế $Z$ bằng $b$, thu được $S = \{X/a, Y/b, Z/b\}$, $E = \{\}$.
6. Thuật toán dừng và trả về MGU là $\{X/a, Y/b, Z/b\}$.

Nếu gọi `Unify(p(a, Y, Y), p(Z, Z, b))`:
- Bước 1: $E = \{a = Z, Y = Z, Y = b\}$.
- Thế $Z$ bằng $a$: $E = \{Y = a, Y = b\}$.
- Thế $Y$ bằng $a$: $E = \{a = b\}$.
- Vì hai hằng số $a$ và $b$ khác nhau, thuật toán rơi vào trường hợp thất bại và trả về $\bot$.
:::

## 15.5.4 Phân giải xác định chứa biến (Definite Resolution with Variables)

Thủ tục suy diễn lùi tìm kiếm câu trả lời bằng phương pháp phân giải SLD (*Linear Resolution with Selection Function for Definite Clauses*):

- **Mệnh đề câu trả lời tổng quát (Generalized Answer Clause)**: Có dạng:

  <pre class="logic-expression">yes(V_1, …, V_k) ← a_1 ∧ a_2 ∧ … ∧ a_m</pre>

  Các đối số của vị từ đặc biệt $yes$ lưu giữ các giá trị cụ thể hóa của các biến trong truy vấn ban đầu.
- **Quy tắc đổi tên biến (Standardizing Apart)**: Khi chọn một luật $a \leftarrow b_1 \wedge \ldots \wedge b_p$ từ $KB$ để phân giải, ta bắt buộc phải **đổi tên toàn bộ các biến** trong luật đó sang các tên biến mới chưa từng xuất hiện. Điều này loại bỏ hiện tượng xung đột tên biến và cho phép tái sử dụng cùng một luật nhiều lần trong cùng một cây chứng minh.

```
procedure Prove_datalog_TD(KB, q)
    Đầu vào: Cơ sở tri thức KB; truy vấn q chứa các biến V1, ..., Vk
    Đầu ra: Phép thế θ sao cho KB ⊨ qθ; hoặc fail

    Khởi tạo mệnh đề mục tiêu: G := (yes(V1, ..., Vk) :- q)
    while thân của G chưa rỗng do
        chọn một nguyên tử a1 trong thân của G
        chọn một luật (a :- b1, ..., bp) trong KB
        đổi tên tất cả các biến trong luật sang tên mới
        σ := Unify(a1, a)
        if σ = ⊥ then backtrack sang lựa chọn khác
        G := (yes(V1, ..., Vk) :- b1, ..., bp, a2, ..., am)σ

    return {V1 = t1, ..., Vk = tk} từ mệnh đề yes(t1, ..., tk) :- .
```

::: example Ví dụ 15.22: Cây dẫn xuất SLD tìm nơi sinh của Shakira
Nữ ca sĩ Shakira sinh ra tại Barranquilla, thủ phủ của tỉnh Atlántico thuộc Colombia. Do đó cô sinh ra ở Colombia.

Xét cơ sở tri thức địa lý:

1. $born\_in(shakira, barranquilla)$
2. <code class="logic-expression">born_in(P, L) ← part_of(S, L) ∧ born_in(P, S)</code>
3. $part\_of(barranquilla, atlantico)$
4. $part\_of(atlantico, colombia)$
5. $part\_of(colombia, south\_america)$

Truy vấn đặt ra: "Ai sinh ra ở Colombia?" $\rightarrow \text{ask } born\_in(P, colombia)$.

Quá trình dẫn xuất SLD diễn ra tuần tự như sau:

1. **Trạng thái ban đầu**:

   $$
   yes(P) \leftarrow born\_in(P, colombia)
   $$

2. **Phân giải bước 1**: Chọn luật 2, đổi tên biến thành $P_1, L_1, S_1$. Hợp nhất $born\_in(P, colombia)$ với $born\_in(P_1, L_1)$ bằng MGU $\sigma_1 = \{P_1/P, L_1/colombia\}$:

   <pre class="logic-expression">yes(P) ← part_of(S_1, colombia) ∧ born_in(P, S_1)</pre>

3. **Phân giải bước 2**: Chọn nguyên tử đầu tiên $part\_of(S_1, colombia)$. Hợp nhất với sự kiện 4 ($part\_of(atlantico, colombia)$) bằng MGU $\sigma_2 = \{S_1/atlantico\}$:

   $$
   yes(P) \leftarrow born\_in(P, atlantico)
   $$

4. **Phân giải bước 3**: Tiếp tục phân giải với bản sao mới của luật 2 ($P_2, L_2, S_2$) bằng MGU $\sigma_3 = \{P_2/P, L_2/atlantico\}$:

   <pre class="logic-expression">yes(P) ← part_of(S_2, atlantico) ∧ born_in(P, S_2)</pre>

5. **Phân giải bước 4**: Hợp nhất $part\_of(S_2, atlantico)$ với sự kiện 3 ($part\_of(barranquilla, atlantico)$) bằng MGU $\sigma_4 = \{S_2/barranquilla\}$:

   <pre class="logic-expression">yes(P) ← born_in(P, barranquilla)</pre>

6. **Phân giải bước 5**: Hợp nhất với sự kiện 1 ($born\_in(shakira, barranquilla)$) bằng MGU $\sigma_5 = \{P/shakira\}$:

   $$
   yes(shakira) \leftarrow
   $$

Thân mục tiêu trở nên rỗng hoàn toàn. Thuật toán kết thúc thành công và trích xuất câu trả lời: $P = shakira$. Luật bắc cầu số 2 đã được sử dụng hai lần độc lập với hai bản sao biến khác nhau trong cùng một chuỗi chứng minh.
:::

## Tài liệu tham khảo

1. Poole, D. L., & Mackworth, A. K. (2023). *Artificial Intelligence: Foundations of Computational Agents* (3rd ed.). Cambridge University Press. Nguồn trực tuyến: [https://artint.info/3e/html/ArtInt3e.Ch15.S5.html](https://artint.info/3e/html/ArtInt3e.Ch15.S5.html).
