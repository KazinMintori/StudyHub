---
course: ai-nen-tang-tac-tu
lecture: 15-ca-the-va-quan-he
section: topic
topic: 15-13-bai-tap
title: "15.13 Bài tập"
description: "Hệ thống 15 bài tập tự luyện toàn diện về logic vị từ, Datalog, hợp nhất, phân giải SLD, cấu trúc dữ liệu đệ quy, DCG và giả định tri thức đầy đủ."
---

Hệ thống bài tập dưới đây bao gồm đầy đủ 15 bài tập từ giáo trình gốc của Poole & Mackworth (2023), bao quát toàn bộ các chủ đề lý thuyết và ứng dụng thực hành của Chương 15: Biểu diễn tri thức bằng cá thể và quan hệ, ngữ nghĩa diễn giải và mô hình, thuật toán hợp nhất, thủ tục chứng minh suy diễn tiến (bottom-up) và suy diễn lùi (top-down / SLD), cấu trúc dữ liệu với ký hiệu hàm, văn phạm mệnh đề xác định (DCG), đẳng thức cùng giả định tri thức đầy đủ.

::: exercise Bài tập 15.1: Đếm diễn giải và mô hình trong miền hai cá thể
Xét một miền xác định gồm hai cá thể $\mathcal{D} = \{✂, ☎\}$, hai ký hiệu vị từ một ngôi ($p$ và $q$), và ba hằng số ($a, b, c$). Cơ sở tri thức $KB$ được định nghĩa bởi:

```prolog
p(X) :- q(X).
q(a).
```

- (a) Hãy chỉ ra một diễn giải là mô hình của $KB$.
- (b) Hãy chỉ ra một diễn giải không phải là mô hình của $KB$.
- (c) Có tổng cộng bao nhiêu diễn giải khả dĩ? Trình bày lập luận giải thích ngắn gọn.
- (d) Có bao nhiêu diễn giải trong số đó là mô hình của $KB$? Trình bày lập luận giải thích ngắn gọn.

::: details Lời giải chi tiết
Một diễn giải $I = \langle\mathcal{D}, \phi, \pi\rangle$ được xác định bởi:
- Ánh xạ hằng số $\phi: \{a, b, c\} \to \mathcal{D}$.
- Ánh xạ phần mở rộng vị từ $\pi$, gán cho mỗi vị từ một ngôi một tập con của $\mathcal{D}$.

**(a) Một diễn giải là mô hình của $KB$:**
- Chọn $\phi(a) = ✂, \phi(b) = ✂, \phi(c) = ☎$.
- Chọn phần mở rộng: $\pi(q) = \{✂\}, \pi(p) = \{✂, ☎\}$.
- Kiểm tra:
  - $\phi(a) = ✂ \in \pi(q) \implies q(a)$ đúng.
  - $\pi(q) \subseteq \pi(p)$ (vì $\{✂\} \subseteq \{✂, ☎\}$) $\implies \forall X (q(X) \rightarrow p(X))$ đúng.
  Do đó diễn giải này là một mô hình của $KB$.

**(b) Một diễn giải không phải là mô hình của $KB$:**
- Chọn $\phi(a) = ✂, \phi(b) = ✂, \phi(c) = ☎$.
- Chọn $\pi(q) = \emptyset, \pi(p) = \emptyset$.
- Khi đó $q(a)$ sai vì $\phi(a) \notin \pi(q)$. Câu sự kiện $q(a)$ bị vi phạm, do đó diễn giải này không phải là mô hình của $KB$.

**(c) Tổng số diễn giải khả dĩ:**
- Ánh xạ $\phi$: Có 3 hằng số, mỗi hằng số có 2 lựa chọn phần tử trong $\mathcal{D}$ $\implies 2^3 = 8$ cách gán $\phi$.
- Vị từ $p$: Có $2^{|\mathcal{D}|} = 2^2 = 4$ tập con khả dĩ cho $\pi(p)$.
- Vị từ $q$: Có $2^{|\mathcal{D}|} = 2^2 = 4$ tập con khả dĩ cho $\pi(q)$.
- Tổng số diễn giải:
  $$N_{\text{total}} = 8 \times 4 \times 4 = 128 \text{ diễn giải.}$$

**(d) Số lượng mô hình của $KB$:**
Để một diễn giải là mô hình của $KB$, nó phải thỏa mãn đồng thời hai điều kiện:
1. $q(a)$ đúng: $\phi(a) \in \pi(q)$. Điều này đòi hỏi $\pi(q) \neq \emptyset$.
2. Luật $p(X) \leftarrow q(X)$ đúng: $\pi(q) \subseteq \pi(p)$.

Ta phân loại theo kích thước của $\pi(q)$:
- **Trường hợp 1**: $|\pi(q)| = 1$. Có 2 cách chọn tập $\pi(q)$ (hoặc $\{✂\}$ hoặc $\{☎\}$).
  - Với mỗi cách chọn $\pi(q)$, điều kiện $\pi(q) \subseteq \pi(p)$ đòi hỏi $\pi(p)$ phải chứa phần tử duy nhất đó của $\pi(q)$. Do đó $\pi(p)$ có 2 lựa chọn (chính tập đó hoặc cả miền $\mathcal{D}$). Vậy có $2 \times 2 = 4$ cặp $(\pi(p), \pi(q))$.
  - Với mỗi cặp này, điều kiện $\phi(a) \in \pi(q)$ buộc $\phi(a)$ phải là phần tử duy nhất của $\pi(q)$ (1 cách chọn). Hai hằng số còn lại $\phi(b)$ và $\phi(c)$ mỗi hằng số có 2 cách chọn tùy ý trong $\mathcal{D}$. Vậy có $1 \times 2 \times 2 = 4$ cách gán $\phi$.
  - Số mô hình trong trường hợp 1: $4 \text{ cặp} \times 4 \text{ cách gán } \phi = 16 \text{ mô hình}$.
- **Trường hợp 2**: $|\pi(q)| = 2$, tức $\pi(q) = \mathcal{D}$. Có duy nhất 1 cách chọn $\pi(q)$.
  - Điều kiện $\pi(q) \subseteq \pi(p)$ buộc $\pi(p) = \mathcal{D}$ (1 cách chọn). Vậy có duy nhất 1 cặp $(\pi(p), \pi(q))$.
  - Điều kiện $\phi(a) \in \pi(q) = \mathcal{D}$ luôn được thỏa mãn với mọi phần tử của $\mathcal{D}$, nên $\phi(a)$ có 2 cách chọn, $\phi(b)$ có 2 cách chọn, $\phi(c)$ có 2 cách chọn $\implies 2 \times 2 \times 2 = 8$ cách gán $\phi$.
  - Số mô hình trong trường hợp 2: $1 \times 8 = 8 \text{ mô hình}$.

Tổng số mô hình của $KB$:
$$N_{\text{models}} = 16 + 8 = 24 \text{ mô hình.}$$
:::
:::

::: exercise Bài tập 15.2: Đếm mô hình với miền bốn cá thể
Giả sử một ngôn ngữ có ba ký hiệu hằng số $a, b, c$; hai ký hiệu vị từ một ngôi $p$ và $q$; không có ký hiệu hàm. Xét ba cơ sở tri thức sau:

- $KB_1$: gồm câu tuyển duy nhất $p(a).$
- $KB_2$: gồm câu tuyển duy nhất $p(X) \leftarrow q(X).$
- $KB_3$: gồm ba câu tuyển $p(X) \leftarrow q(X).$, $p(a).$, $q(b).$

Xét các diễn giải có dạng $I = \langle\mathcal{D}, \pi, \phi\rangle$ với miền xác định gồm bốn cá thể:
$$\mathcal{D} = \{✂, ☎, ✈, ✎\}$$

- (a) Có bao nhiêu diễn giải với miền bốn cá thể cho ngôn ngữ này? Trình bày lập luận giải thích ngắn gọn.
- (b) Trong số các diễn giải trên, có bao nhiêu diễn giải là mô hình của $KB_1$?
- (c) Có bao nhiêu diễn giải là mô hình của $KB_2$?
- (d) Có bao nhiêu diễn giải là mô hình của $KB_3$?

::: details Lời giải chi tiết
Miền xác định có $|\mathcal{D}| = 4$.

**(a) Tổng số diễn giải:**
- Số cách gán $\phi$ cho ba hằng số: Mỗi hằng số nhận 1 trong 4 cá thể $\implies 4^3 = 64$ cách gán.
- Số phần mở rộng khả dĩ của vị từ $p$: Là số tập con của $\mathcal{D} \implies 2^4 = 16$ cách chọn $\pi(p)$.
- Số phần mở rộng khả dĩ của vị từ $q$: $2^4 = 16$ cách chọn $\pi(q)$.
- Tổng số diễn giải:
  <span class="logic-expression logic-block">N_total = 64 × 16 × 16 = 16,384  diễn giải.</span>

**(b) Số mô hình của $KB_1 = \{p(a)\}$:**
- $KB_1$ chỉ đòi hỏi $\phi(a) \in \pi(p)$.
- Với mỗi cách gán $\phi$ (64 cách), $\phi(a)$ nhận một cá thể cụ thể $d \in \mathcal{D}$.
- Để $d \in \pi(p)$, tập con $\pi(p)$ bắt buộc phải chứa $d$, và 3 phần tử còn lại có thể thuộc hoặc không thuộc $\pi(p)$ $\implies 2^{4-1} = 2^3 = 8$ cách chọn $\pi(p)$.
- Vị từ $q$ không bị ràng buộc bởi $KB_1 \implies 16$ cách chọn $\pi(q)$.
- Số mô hình của $KB_1$:
  <span class="logic-expression logic-block">N_KB_1 = 64 × 8 × 16 = 8,192  mô hình.</span>

**(c) Số mô hình của $KB_2 = \{p(X) \leftarrow q(X)\}$:**
- $KB_2$ đòi hỏi $\pi(q) \subseteq \pi(p)$.
- Với mỗi cá thể $d \in \mathcal{D}$, cặp giá trị chân lý $(d \in \pi(p), d \in \pi(q))$ có 3 khả năng hợp lệ: <code class="logic-expression">(true, true), (true, false), (false, false)</code> (chỉ loại trừ khả năng $d \in \pi(q)$ mà $d \notin \pi(p)$).
- Với 4 cá thể, có $3^4 = 81$ cặp phần mở rộng $(\pi(p), \pi(q))$ thỏa mãn $\pi(q) \subseteq \pi(p)$.
- Các hằng số hoàn toàn không xuất hiện trong $KB_2$, nên có $4^3 = 64$ cách gán $\phi$ tùy ý.
- Số mô hình của $KB_2$:
  $$N_{KB_2} = 64 \times 81 = 5{,}184 \text{ mô hình.}$$

**(d) Số mô hình của $KB_3 = \{p(X) \leftarrow q(X), p(a), q(b)\}$:**
Ba điều kiện cần thỏa mãn:
1. $\pi(q) \subseteq \pi(p)$.
2. $\phi(a) \in \pi(p)$.
3. $\phi(b) \in \pi(q)$ (kéo theo $\phi(b) \in \pi(p)$ do điều kiện 1).

Ta xét hai trường hợp gán hằng số:
- **Trường hợp $\phi(a) = \phi(b)$**:
  - Số cách gán $\phi$: Có 4 cách chọn cá thể chung cho $a$ và $b$, và 4 cách chọn cá thể cho $c \implies 4 \times 4 = 16$ cách gán.
  - Đặt $d^* = \phi(a) = \phi(b)$. Vì $d^* \in \pi(q)$ và $\pi(q) \subseteq \pi(p)$, nên $d^* \in \pi(p)$ và $d^* \in \pi(q)$ là cố định (1 cách chọn cho $d^*$).
  - Đối với 3 cá thể còn lại trong $\mathcal{D} \setminus \{d^*\}$, mỗi cá thể có 3 cách chọn cặp chân lý thỏa mãn $\pi(q) \subseteq \pi(p) \implies 3^3 = 27$ cặp $(\pi(p), \pi(q))$.
  - Số mô hình: $16 \times 27 = 432$.
- **Trường hợp $\phi(a) \neq \phi(b)$**:
  - Số cách gán $\phi$: Có $4 \times 3 = 12$ cách chọn hai cá thể phân biệt cho $a$ và $b$, và 4 cách chọn cá thể cho $c \implies 12 \times 4 = 48$ cách gán.
  - Đặt $d_a = \phi(a)$ và $d_b = \phi(b)$.
    - Đối với $d_b$: Phải có $d_b \in \pi(q)$, kéo theo $d_b \in \pi(p)$ $\implies 1$ cách chọn duy nhất cho $d_b$: $(true, true)$.
    - Đối với $d_a$: Phải có $d_a \in \pi(p)$. Khi đó $d_a$ có thể thuộc hoặc không thuộc $\pi(q)$ mà vẫn thỏa mãn $\pi(q) \subseteq \pi(p) \implies 2$ cách chọn cho $d_a$: $(true, true)$ hoặc $(true, false)$.
    - Đối với 2 cá thể còn lại: Mỗi cá thể có 3 cách chọn $\implies 3^2 = 9$ cách.
    - Vậy có $1 \times 2 \times 9 = 18$ cặp $(\pi(p), \pi(q))$ cho mỗi phép gán $\phi$.
  - Số mô hình: $48 \times 18 = 864$.

Tổng số mô hình của $KB_3$:
<span class="logic-expression logic-block">N_KB_3 = 432 + 864 = 1,296  mô hình.</span>
:::
:::

::: exercise Bài tập 15.3: Thứ tự dẫn xuất trong thủ tục suy diễn tiến
Xét cơ sở tri thức sau:

```prolog
r(a).
r(e).
p(c).
q(b).
s(a, b).
s(d, b).
s(e, d).
p(X) :- q(X), r(X).
q(X) :- s(X, Y), q(Y).
```

Hãy chỉ ra tập hợp các hệ quả nguyên tử không biến dẫn xuất được từ cơ sở tri thức này bằng thủ tục suy diễn tiến (bottom-up). Giả định rằng tại mỗi bước lặp, câu tuyển đầu tiên có thể áp dụng được theo thứ tự liệt kê sẽ được chọn. Ngoài ra, nếu có nhiều phép thế hằng số cùng áp dụng được cho câu tuyển đó, phép thế theo thứ tự bảng chữ cái sẽ được ưu tiên chọn trước (ví dụ $X/a$ trước $X/b$). Hãy nêu rõ thứ tự các hệ quả được dẫn xuất.

::: details Lời giải chi tiết
Tập các sự kiện ban đầu:
<span class="logic-expression logic-block">C_0 = {r(a), r(e), p(c), q(b), s(a, b), s(d, b), s(e, d)}</span>

Hai luật suy diễn cần xét:
- Luật 1: $p(X) \leftarrow q(X) \wedge r(X)$.
- Luật 2: $q(X) \leftarrow s(X, Y) \wedge q(Y)$.

**Vòng lặp 1:**
- Kiểm tra Luật 1: Tập các cá thể thỏa $q$ hiện có $\{b\}$, tập thỏa $r$ có $\{a, e\}$. Giao bằng rỗng, chưa áp dụng được.
- Kiểm tra Luật 2: Cần $q(Y)$ đúng, hiện có $Y = b$.
  Các sự kiện dạng $s(X, b)$ gồm $s(a, b)$ và $s(d, b)$.
  Cả hai phép thế $X/a$ và $X/d$ đều thỏa mãn. Theo quy tắc thứ tự chữ cái, chọn $X/a$ trước:
  - Dẫn xuất: $q(a)$.
  Tiếp theo cho phép thế $X/d$:
  - Dẫn xuất: $q(d)$.

**Vòng lặp 2:**
- Tập sự kiện mở rộng có thêm $q(a), q(d)$.
- Kiểm tra Luật 1: Hiện tại các cá thể thỏa $q$ gồm $\{b, a, d\}$, các cá thể thỏa $r$ gồm $\{a, e\}$.
  Giao điểm có cá thể $a$ thỏa mãn cả $q(a)$ và $r(a)$.
  - Dẫn xuất: $p(a)$.
- Kiểm tra Luật 2: Với sự kiện mới $q(d)$, ta có $s(e, d)$ với $Y = d$.
  - Dẫn xuất: $q(e)$.

**Vòng lặp 3:**
- Tập sự kiện mở rộng có thêm $p(a), q(e)$.
- Kiểm tra Luật 1: Các cá thể thỏa $q$ gồm $\{b, a, d, e\}$, các cá thể thỏa $r$ gồm $\{a, e\}$.
  Giao điểm có thêm cá thể $e$ thỏa mãn cả $q(e)$ và $r(e)$.
  - Dẫn xuất: $p(e)$.
- Kiểm tra Luật 2: Không còn cặp nào sinh ra nguyên tử mới.

**Vòng lặp 4:**
- Không còn luật nào sinh thêm được nguyên tử mới. Thuật toán dừng.

**Kết luận:**
- Tập toàn bộ các hệ quả nguyên tử không biến mới được dẫn xuất là: $\{q(a), q(d), p(a), q(e), p(e)\}$.
- Thứ tự dẫn xuất chính xác là:
  1. $q(a)$
  2. $q(d)$
  3. $p(a)$
  4. $q(e)$
  5. $p(e)$
:::
:::

::: exercise Bài tập 15.4: Dẫn xuất SLD và truy vấn quyền truy cập
Xét cơ sở tri thức sau:

```prolog
has_access(X, library) :- student(X).
has_access(X, library) :- faculty(X).
has_access(X, library) :- parent(Y, X), has_access(Y, library).
has_access(X, office) :- has_keys(X).

faculty(diane).
faculty(ming).
student(william).
student(mary).

parent(diane, karen).
parent(diane, robyn).
parent(susan, sarah).
parent(sarah, ariel).
parent(karen, chelsey).
parent(karen, todd).
```

- (a) Hãy trình bày một dẫn xuất SLD hoàn chỉnh cho truy vấn $has\_access(todd, library)$.
- (b) Truy vấn $has\_access(mary, library)$ có hai nhánh dẫn xuất SLD. Hãy chỉ ra cả hai nhánh đó.
- (c) Có tồn tại dẫn xuất thành công cho truy vấn $has\_access(ariel, library)$ hay không? Giải thích lý do.
- (d) Giải thích tại sao tập câu trả lời cho truy vấn $has\_access(X, office)$ là rỗng.
- (e) Giả sử bổ sung câu tuyển $has\_keys(X) \leftarrow faculty(X)$ vào cơ sở tri thức. Khi đó câu trả lời cho truy vấn $has\_access(X, office)$ là gì?

::: details Lời giải chi tiết
**(a) Dẫn xuất SLD cho $has\_access(todd, library)$:**
1. Câu tuyển mục tiêu khởi đầu:
   $$yes \leftarrow has\_access(todd, library)$$
2. Phân giải với luật 3: <code class="logic-expression">has_access(X_1, library) ← parent(Y_1, X_1) ∧ has_access(Y_1, library)</code>
   - Phép thế: $\{X_1/todd\}$
   - Mục tiêu mới:
     <span class="logic-expression logic-block">yes ← parent(Y_1, todd) ∧ has_access(Y_1, library)</span>
3. Phân giải với sự kiện $parent(karen, todd)$:
   - Phép thế: $\{Y_1/karen\}$
   - Mục tiêu mới:
     $$yes \leftarrow has\_access(karen, library)$$
4. Phân giải tiếp với luật 3: <code class="logic-expression">has_access(X_2, library) ← parent(Y_2, X_2) ∧ has_access(Y_2, library)</code>
   - Phép thế: $\{X_2/karen\}$
   - Mục tiêu mới:
     <span class="logic-expression logic-block">yes ← parent(Y_2, karen) ∧ has_access(Y_2, library)</span>
5. Phân giải với sự kiện $parent(diane, karen)$:
   - Phép thế: $\{Y_2/diane\}$
   - Mục tiêu mới:
     $$yes \leftarrow has\_access(diane, library)$$
6. Phân giải với luật 2: <code class="logic-expression">has_access(X_3, library) ← faculty(X_3)</code>
   - Phép thế: $\{X_3/diane\}$
   - Mục tiêu mới:
     $$yes \leftarrow faculty(diane)$$
7. Phân giải với sự kiện $faculty(diane)$:
   - Thân mục tiêu trở thành rỗng:
     $$yes \leftarrow$$
   - Dẫn xuất thành công.

**(b) Hai nhánh dẫn xuất SLD cho $has\_access(mary, library)$:**
- **Nhánh 1 (Thành công)**:
  $$yes \leftarrow has\_access(mary, library)$$
  $$yes \leftarrow student(mary)$$
  $$yes \leftarrow$$
- **Nhánh 2 (Thất bại)**:
  $$yes \leftarrow has\_access(mary, library)$$
  $$yes \leftarrow faculty(mary)$$
  Thất bại (do không có sự kiện $faculty(mary)$).
  (Nếu xét nhánh qua luật bắc cầu phụ huynh: <code class="logic-expression">yes ← parent(Y, mary) ∧ has_access(Y, library)</code> cũng thất bại ngay vì không có ai là phụ huynh của Mary).

**(c) Dẫn xuất cho $has\_access(ariel, library)$:**
Không tồn tại bất kỳ dẫn xuất thành công nào.
- *Lý do*: Ariel không phải là sinh viên hay giảng viên.
- Cây phả hệ phụ huynh của Ariel là: $parent(sarah, ariel)$ và $parent(susan, sarah)$. Chuỗi phụ huynh dừng lại ở Susan.
- Cả Sarah và Susan đều không phải là $student$ hay $faculty$. Do đó, mọi nhánh tìm kiếm đệ quy ngược dòng phụ huynh đều dẫn tới các nút lá thất bại.

**(d) Tập câu trả lời cho $has\_access(X, office)$ là rỗng:**
- Luật duy nhất suy ra quyền vào văn phòng là <code class="logic-expression">has_access(X, office) ← has_keys(X)</code>.
- Trong toàn bộ cơ sở tri thức, không có bất kỳ sự kiện hay luật nào có phần đầu là $has\_keys(\ldots)$. Do đó mục tiêu $has\_keys(X)$ không thể hợp nhất với bất kỳ câu tuyển nào và thất bại ngay lập tức, dẫn tới tập câu trả lời rỗng.

**(e) Khi thêm luật $has\_keys(X) \leftarrow faculty(X)$:**
- Ta có chuỗi suy luận: <code class="logic-expression">has_access(X, office) ← has_keys(X) ← faculty(X)</code>.
- Các sự kiện thỏa mãn $faculty$ là $faculty(diane)$ và $faculty(ming)$.
- Do đó, tập các câu trả lời cho truy vấn $has\_access(X, office)$ là:
  $$\{X = diane, X = ming\}$$
:::
:::

::: exercise Bài tập 15.5: Thực thi phép thế trên biểu thức
Hãy xác định kết quả của các phép áp dụng thế sau đây:

- (a) $f(A, X, Y, X, Y) \{A/X, Z/b, Y/c\}$
- (b) <code class="logic-expression">(yes(F, L) ← append(F, c(L, nil), c(l, c(i, c(s, c(t, nil)))))) {F/c(l, X_1), Y_1/c(L, nil), A_1/l, Z_1/c(i, c(s, c(t, nil)))}</code>
- (c) <code class="logic-expression">(append(c(A_1, X_1), Y_1, c(A_1, Z_1)) ← append(X_1, Y_1, Z_1)) {F/c(l, X_1), Y_1/c(L, nil), A_1/l, Z_1/c(i, c(s, c(t, nil)))}</code>

::: details Lời giải chi tiết
**(a)**
- Thay thế biến $A$ bằng $X$, thay thế biến $Y$ bằng $c$ (biến $Z$ không xuất hiện trong biểu thức nên bỏ qua):
  <span class="logic-expression logic-block">f(A, X, Y, X, Y){A/X, Z/b, Y/c} = f(X, X, c, X, c)</span>

**(b)**
- Trong câu tuyển này, các biến có mặt là $F$ và $L$.
- Phép thế chứa $F/c(l, X_1)$. Biến $L$ không bị thay thế. Các phép gán cho $Y_1, A_1, Z_1$ không ảnh hưởng vì các biến này không có mặt trong biểu thức ban đầu.
- Kết quả:
  <span class="logic-expression logic-block">yes(c(l, X_1), L) ← append(c(l, X_1), c(L, nil), c(l, c(i, c(s, c(t, nil)))))</span>

**(c)**
- Các biến có mặt trong câu tuyển là $A_1, X_1, Y_1, Z_1$.
- Áp dụng các phép thế tương ứng: $A_1 \to l$, $Y_1 \to c(L, nil)$, $Z_1 \to c(i, c(s, c(t, nil)))$. Biến $X_1$ giữ nguyên.
- Kết quả:
  <span class="logic-expression logic-block">append(c(l, X_1), c(L, nil), c(l, c(i, c(s, c(t, nil))))) ← append(X_1, c(L, nil), c(i, c(s, c(t, nil))))</span>
:::
:::

::: exercise Bài tập 15.6: Tìm bộ hợp nhất tổng quát nhất (MGU)
Hãy tìm bộ hợp nhất tổng quát nhất (MGU) cho từng cặp biểu thức sau:

- (a) $p(f(X), g(g(b)))$ và $p(Z, g(Y))$
- (b) $g(f(X), r(X), t)$ và $g(W, r(Q), Q)$
- (c) $bar(val(X, bb), Z)$ và $bar(P, P)$

::: details Lời giải chi tiết
**(a) Cặp $p(f(X), g(g(b)))$ và $p(Z, g(Y))$:**
- So khớp đối số 1: $f(X)$ và $Z \implies Z / f(X)$.
- So khớp đối số 2: $g(g(b))$ và $g(Y) \implies Y / g(b)$.
- MGU:
  $$\sigma = \{Z / f(X), Y / g(b)\}$$

**(b) Cặp $g(f(X), r(X), t)$ và $g(W, r(Q), Q)$:**
- So khớp đối số 1: $f(X)$ và $W \implies W / f(X)$.
- So khớp đối số 2: $r(X)$ và $r(Q) \implies Q / X$.
- So khớp đối số 3: $t$ và $Q$. Do $Q$ đã liên kết với $X$, ta có phương trình $X = t \implies X / t$.
- Cập nhật lại các phép thế trước đó theo $X = t$:
  - $W / f(t)$
  - $Q / t$
- MGU:
  $$\sigma = \{W / f(t), Q / t, X / t\}$$

**(c) Cặp $bar(val(X, bb), Z)$ và $bar(P, P)$:**
- So khớp đối số 1: $val(X, bb)$ và $P \implies P / val(X, bb)$.
- So khớp đối số 2: $Z$ và $P$. Vì $P$ đã liên kết với $val(X, bb)$, ta có $Z / val(X, bb)$.
- MGU:
  $$\sigma = \{P / val(X, bb), Z / val(X, bb)\}$$
:::
:::

::: exercise Bài tập 15.7: Kiểm tra tính hợp nhất của các nguyên tử
Đối với mỗi cặp nguyên tử sau, hãy chỉ ra bộ hợp nhất tổng quát nhất hoặc giải thích lý do tại sao không tồn tại bộ hợp nhất:

- (a) $p(X, Y, a, b, W)$ và $p(E, c, F, G, F)$
- (b) $p(Y, a, b, Y)$ và $p(c, F, G, F)$
- (c) $foo(Z, [a, z \mid X], X)$ và $foo([a, m \mid W], W, [i, n, g])$
- (d) <code class="logic-expression">ap(F0, c(b, c(B0, L0)), c(a, c(b, c(a, emp))))</code> và $ap(c(H1, T1), L1, c(H1, R1))$

::: details Lời giải chi tiết
**(a)**
- Đối số 1: $X$ và $E \implies E / X$.
- Đối số 2: $Y$ và $c \implies Y / c$.
- Đối số 3: $a$ và $F \implies F / a$.
- Đối số 4: $b$ và $G \implies G / b$.
- Đối số 5: $W$ và $F$. Do $F = a \implies W / a$.
- Hợp nhất thành công. MGU:
  $$\sigma = \{E/X, Y/c, F/a, G/b, W/a\}$$

**(b)**
- Đối số 1: $Y$ và $c \implies Y / c$.
- Đối số 2: $a$ và $F \implies F / a$.
- Đối số 3: $b$ và $G \implies G / b$.
- Đối số 4: $Y$ và $F$. Nhưng từ các bước trước ta có $Y = c$ và $F = a$. Do đó phương trình trở thành $c = a$.
- Hai hằng số khác nhau $c$ và $a$ không thể hợp nhất. Do đó **không tồn tại bộ hợp nhất**.

**(c)**
- Đối số 3: $X$ và $[i, n, g] \implies X / [i, n, g]$.
- Đối số 2: $[a, z \mid X]$ và $W$. Thế $X$ vào ta được $W / [a, z, i, n, g]$.
- Đối số 1: $Z$ và $[a, m \mid W]$. Thế $W$ vào ta được $Z / [a, m, a, z, i, n, g]$.
- Hợp nhất thành công. MGU:
  <span class="logic-expression logic-block">σ = {X / [i, n, g], W / [a, z, i, n, g], Z / [a, m, a, z, i, n, g]}</span>

**(d)**
- Đối số 3: $c(a, c(b, c(a, emp)))$ và $c(H1, R1)$:
  - So khớp đầu: $H1 / a$.
  - So khớp đuôi: $R1 / c(b, c(a, emp))$.
- Đối số 1: $F0$ và $c(H1, T1)$. Với $H1 = a$, ta có $F0 / c(a, T1)$.
- Đối số 2: $c(b, c(B0, L0))$ và $L1 \implies L1 / c(b, c(B0, L0))$.
- Hợp nhất thành công. MGU:
  <span class="logic-expression logic-block">σ = {H1/a, R1/c(b, c(a, emp)), L1/c(b, c(B0, L0)), F0/c(a, T1)}</span>
:::
:::

::: exercise Bài tập 15.8: Liệt kê hệ quả logic nguyên tử không biến
Hãy liệt kê tất cả các hệ quả logic nguyên tử không biến của cơ sở tri thức sau:

```prolog
q(Y) :- s(Y, Z), r(Z).
p(X) :- q(f(X)).
s(f(a), b).
s(f(b), b).
s(c, b).
r(b).
```

::: details Lời giải chi tiết
1. **Các sự kiện có sẵn trong $KB$**:
   <span class="logic-expression logic-block">s(f(a), b),   s(f(b), b),   s(c, b),   r(b)</span>
2. **Áp dụng luật $q(Y) \leftarrow s(Y, Z) \wedge r(Z)$**:
   - Ta có sự kiện $r(b)$, nên chọn $Z = b$.
   - Các sự kiện khớp $s(Y, b)$ gồm:
     - $s(f(a), b) \implies q(f(a))$
     - $s(f(b), b) \implies q(f(b))$
     - $s(c, b) \implies q(c)$
3. **Áp dụng luật $p(X) \leftarrow q(f(X))$**:
   - Với $q(f(a))$, thế $X = a \implies p(a)$.
   - Với $q(f(b))$, thế $X = b \implies p(b)$.
   - Đối với $q(c)$, số hạng $c$ không có dạng $f(X)$ nên không kích hoạt thêm câu nào.

**Toàn bộ các hệ quả nguyên tử không biến tất suy từ $KB$ là:**
<span class="logic-expression logic-block">{s(f(a), b), s(f(b), b), s(c, b), r(b), q(f(a)), q(f(b)), q(c), p(a), p(b)}</span>
:::
:::

::: exercise Bài tập 15.9: Dẫn xuất phân giải loại bỏ phần tử trùng liền kề
Xét chương trình logic sau:

```prolog
rd(cons(H, cons(H, T)), T).
rd(cons(H, T), cons(H, R)) :- rd(T, R).
```

Hãy trình bày dẫn xuất từ trên xuống (top-down), chỉ rõ toàn bộ các phép thế cho truy vấn:

<span class="logic-expression logic-block">ask  rd(cons(a, cons(cons(a, X), cons(B, cons(c, Z)))), W).</span>

- Câu trả lời tương ứng với dẫn xuất này là gì?
- Có tồn tại câu trả lời thứ hai hay không? Nếu có, hãy trình bày dẫn xuất; nếu không, hãy giải thích lý do.

::: details Lời giải chi tiết
Ký hiệu hai câu tuyển trong chương trình:
- $(C_1)$: $rd(cons(H_1, cons(H_1, T_1)), T_1).$
- $(C_2)$: <code class="logic-expression">rd(cons(H_2, T_2), cons(H_2, R_2)) ← rd(T_2, R_2).</code>

Truy vấn khởi đầu:
<span class="logic-expression logic-block">yes(W) ← rd(cons(a, cons(cons(a, X), cons(B, cons(c, Z)))), W)</span>

Danh sách đầu vào có phần tử đầu là $a$, phần tử thứ hai là $cons(a, X)$. Vì $a$ (hằng số) và $cons(a, X)$ (cấu trúc hàm) không thể hợp nhất với nhau, nên câu tuyển cơ sở $(C_1)$ không thể áp dụng ở bước đầu tiên. Bắt buộc phải chọn $(C_2)$:

**Bước 1:**
- Hợp nhất với $(C_2)$:
  - $H_2 = a$
  - <code class="logic-expression">T_2 = cons(cons(a, X), cons(B, cons(c, Z)))</code>
  - $W = cons(a, R_2)$
- Mục tiêu mới:
  <span class="logic-expression logic-block">yes(cons(a, R_2)) ← rd(cons(cons(a, X), cons(B, cons(c, Z))), R_2)</span>

Tại bước này, danh sách mục tiêu có hai phần tử đầu là $cons(a, X)$ và $B$.
Ta có hai khả năng chọn câu tuyển:

**Nhánh dẫn xuất 1: Chọn câu tuyển $(C_1)$**
- Hợp nhất đối số đầu của $(C_1)$ với danh sách:
  - $H_1 = cons(a, X)$
  - $B = H_1 = cons(a, X)$
  - $T_1 = cons(c, Z)$
  - $R_2 = T_1 = cons(c, Z)$
- Thân mục tiêu trở thành rỗng:
  $$yes(cons(a, cons(c, Z))) \leftarrow$$
- Câu trả lời thứ nhất:
  <span class="logic-expression logic-block">W = cons(a, cons(c, Z)),   B = cons(a, X)</span>

**Nhánh dẫn xuất 2: Chọn câu tuyển $(C_2)$**
- Hợp nhất với $(C_2)$:
  - $H_3 = cons(a, X)$
  - $T_3 = cons(B, cons(c, Z))$
  - $R_2 = cons(cons(a, X), R_3)$
- Mục tiêu mới:
  <span class="logic-expression logic-block">yes(cons(a, cons(cons(a, X), R_3))) ← rd(cons(B, cons(c, Z)), R_3)</span>
- Tiếp tục phân giải mục tiêu này:
  - Nếu chọn $(C_1)$: Hợp nhất $B$ với $c \implies B = c$, và $T_4 = Z, R_3 = Z$.
    Thân mục tiêu trở thành rỗng.
    Ta thu được câu trả lời thứ hai:
    <span class="logic-expression logic-block">W = cons(a, cons(cons(a, X), Z)),   B = c</span>

Như vậy, **có tồn tại câu trả lời thứ hai**. Cả hai câu trả lời phản ánh hai vị trí khác nhau trong danh sách mà tại đó hai phần tử liên tiếp có thể được hợp nhất để loại bỏ trùng lặp.
:::
:::

::: exercise Bài tập 15.10: Suy diễn quan hệ kề cận với danh sách
Xét chương trình logic sau:

```prolog
ap(emp, L, L).
ap(c(H, T), L, c(H, R)) :- ap(T, L, R).
adj(A, B, L) :- ap(F, c(A, c(B, E)), L).
```

- (a) Hãy trình bày dẫn xuất từ trên xuống (bao gồm mọi phép thế) cho một câu trả lời của truy vấn:
  <span class="logic-expression logic-block">ask  adj(b, Y, c(a, c(b, c(b, c(a, emp))))).</span>
- (b) Có câu trả lời nào khác không? Nếu có, hãy giải thích điểm rẽ nhánh trong dẫn xuất và tiếp tục dẫn xuất để chỉ ra câu trả lời đó. Nếu không, hãy giải thích tại sao.

::: details Lời giải chi tiết
*(Gợi ý: Đọc $ap$ là append, $c$ là cons, $emp$ là danh sách rỗng, $adj(A, B, L)$ là $A$ đứng liền trước $B$ trong danh sách $L$). Danh sách đầu vào tương ứng với chuỗi $[a, b, b, a]$.*

**(a) Dẫn xuất câu trả lời thứ nhất:**
1. Khởi đầu:
   <span class="logic-expression logic-block">yes(Y) ← adj(b, Y, c(a, c(b, c(b, c(a, emp)))))</span>
2. Áp dụng luật $adj$:
   <span class="logic-expression logic-block">yes(Y) ← ap(F, c(b, c(Y, E)), c(a, c(b, c(b, c(a, emp)))))</span>
3. Với mục tiêu $ap$, phần tử đầu của danh sách kết quả là $a$, trong khi phần tử đầu của đối số thứ hai là $b$. Vì $a \neq b$, câu tuyển $ap(emp, L, L)$ không thể áp dụng được ngay. Buộc phải chọn câu tuyển đệ quy của $ap$:
   - Hợp nhất: <code class="logic-expression">F = c(a, T_1), H_1 = a, R_1 = c(b, c(b, c(a, emp)))</code>.
   - Mục tiêu mới:
     <span class="logic-expression logic-block">yes(Y) ← ap(T_1, c(b, c(Y, E)), c(b, c(b, c(a, emp))))</span>
4. Tại bước này, ta có thể chọn câu tuyển cơ sở $ap(emp, L, L)$:
   - Hợp nhất: $T_1 = emp$, <code class="logic-expression">L = c(b, c(Y, E)) = c(b, c(b, c(a, emp)))</code>.
   - So khớp: $b = b$, $Y = b$, $E = c(a, emp)$.
   - Thân mục tiêu trở thành rỗng:
     $$yes(b) \leftarrow$$
   - Câu trả lời thứ nhất: $Y = b$.

**(b) Câu trả lời thứ hai:**
Tại bước 4 ở trên, thay vì chọn $ap(emp, L, L)$, ta có thể tiếp tục chọn câu tuyển đệ quy của $ap$:
- Hợp nhất: <code class="logic-expression">T_1 = c(b, T_2), H_2 = b, R_2 = c(b, c(a, emp))</code>.
- Mục tiêu mới:
  <span class="logic-expression logic-block">yes(Y) ← ap(T_2, c(b, c(Y, E)), c(b, c(a, emp)))</span>
- Bây giờ chọn câu tuyển cơ sở $ap(emp, L, L)$:
  - Hợp nhất: $T_2 = emp$, $c(b, c(Y, E)) = c(b, c(a, emp))$.
  - So khớp: $b = b$, $Y = a$, $E = emp$.
  - Thân mục tiêu trở thành rỗng:
    $$yes(a) \leftarrow$$
  - Câu trả lời thứ hai: $Y = a$.

Như vậy có hai câu trả lời: $Y = b$ (ứng với cặp phần tử thứ 2 và thứ 3 trong $[a, b, b, a]$) và $Y = a$ (ứng với cặp phần tử thứ 3 và thứ 4).
:::
:::

::: exercise Bài tập 15.11: Lập trình logic thao tác trên danh sách
- (a) Hãy viết quan hệ $remove(E, L, R)$ đúng nếu $R$ là danh sách thu được từ việc loại bỏ chính xác một lần xuất hiện của phần tử $E$ khỏi danh sách $L$. Quan hệ nhận giá trị sai nếu $E$ không thuộc $L$.
- (b) Hãy chỉ ra tất cả các câu trả lời cho các truy vấn sau:
  - $\text{ask } remove(a, [b, a, d, a], R).$
  - $\text{ask } remove(E, [b, a, d, a], R).$
  - $\text{ask } remove(E, L, [b, a, d]).$
  - <code class="logic-expression">ask  remove(p(X), [a, p(a), p(p(a)), p(p(p(a)))], R).</code>
- (c) Hãy viết quan hệ $subsequence(L1, L2)$ đúng nếu danh sách $L1$ là một dãy con của $L2$ (các phần tử xuất hiện cùng thứ tự).
- (d) Có bao nhiêu phép chứng minh khác nhau cho mỗi truy vấn sau:
  - $\text{ask } subsequence([a, d], [b, a, d, a]).$
  - $\text{ask } subsequence([b, a], [b, a, d, a]).$
  - $\text{ask } subsequence([X, Y], [b, a, d, a]).$
  - $\text{ask } subsequence(S, [b, a, d, a]).$

::: details Lời giải chi tiết
**(a) Định nghĩa quan hệ $remove(E, L, R)$:**
```prolog
% Trường hợp cơ sở: Loại bỏ E ở ngay đầu danh sách
remove(E, [E | T], T).

% Trường hợp đệ quy: Giữ lại phần tử đầu H và tiếp tục loại E ở phần đuôi T
remove(E, [H | T], [H | R]) :-
    remove(E, T, R).
```

**(b) Các câu trả lời cho truy vấn:**
1. `ask remove(a, [b, a, d, a], R).`
   - Lần 1 (bỏ chữ $a$ đầu tiên): $R = [b, d, a]$.
   - Lần 2 (bỏ chữ $a$ thứ hai): $R = [b, a, d]$.
2. `ask remove(E, [b, a, d, a], R).`
   - $E = b, R = [a, d, a]$
   - $E = a, R = [b, d, a]$
   - $E = d, R = [b, a, a]$
   - $E = a, R = [b, a, d]$
3. `ask remove(E, L, [b, a, d]).`
   Đây là bài toán chèn phần tử $E$ vào mọi vị trí khả dĩ của danh sách $[b, a, d]$:
   - $L = [E, b, a, d]$
   - $L = [b, E, a, d]$
   - $L = [b, a, E, d]$
   - $L = [b, a, d, E]$
4. `ask remove(p(X), [a, p(a), p(p(a)), p(p(p(a)))], R).`
   Hợp nhất $p(X)$ lần lượt với các phần tử trong danh sách:
   - Khớp $p(a)$ với <code class="logic-expression">X = a ⇒ R = [a, p(p(a)), p(p(p(a)))]</code>.
   - Khớp $p(p(a))$ với <code class="logic-expression">X = p(a) ⇒ R = [a, p(a), p(p(p(a)))]</code>.
   - Khớp $p(p(p(a)))$ với <code class="logic-expression">X = p(p(a)) ⇒ R = [a, p(a), p(p(a))]</code>.

**(c) Định nghĩa quan hệ $subsequence(L1, L2)$:**
```prolog
subsequence([], _).
subsequence([X | T1], [X | T2]) :-
    subsequence(T1, T2).
subsequence(L1, [_ | T2]) :-
    subsequence(L1, T2).
```

**(d) Số lượng phép chứng minh:**
1. `ask subsequence([a, d], [b, a, d, a]).`
   - Chữ $a$ chỉ có thể lấy từ vị trí thứ 2 (chữ $a$ ở vị trí thứ 4 đứng sau $d$ nên không tạo được dãy con $[a, d]$). Chữ $d$ lấy ở vị trí thứ 3.
   - Có **1 phép chứng minh**.
2. `ask subsequence([b, a], [b, a, d, a]).`
   - Phần tử $b$ lấy ở vị trí 1. Phần tử $a$ có thể lấy ở vị trí 2 hoặc vị trí 4.
   - Có **2 phép chứng minh**.
3. `ask subsequence([X, Y], [b, a, d, a]).`
   - Số cặp chỉ số $(i, j)$ với $1 \le i < j \le 4$ là $\binom{4}{2} = 6$.
   - Mỗi cặp chỉ số tương ứng với một phép chứng minh duy nhất.
   - Có **6 phép chứng minh**.
4. `ask subsequence(S, [b, a, d, a]).`
   - Mỗi phần tử trong danh sách 4 phần tử có 2 lựa chọn (chọn đưa vào dãy con hoặc bỏ qua).
   - Tổng số phép chứng minh bằng số tập con của tập 4 phần tử: $2^4 = 16$.
   - Có **16 phép chứng minh**.
:::
:::

::: exercise Bài tập 15.12: Thiết kế bài trình chiếu video tự động
Giả sử các phân đoạn video được chú thích thông qua quan hệ:

<span class="logic-expression logic-block">segment(SegId, Duration, Covers)</span>

trong đó $SegId$ là định danh phân đoạn, $Duration$ là thời lượng (giây), và $Covers$ là danh sách các chủ đề được phân đoạn đó đề cập. Xét cơ sở dữ liệu sau:

```prolog
segment(seg0, 10, [welcome]).
segment(seg1, 30, [skiing, views]).
segment(seg2, 50, [welcome, artificial_intelligence, robots]).
segment(seg3, 40, [graphics, dragons]).
segment(seg4, 50, [skiing, robots]).
```

- (a) Hãy tiên đề hóa vị từ <code class="logic-expression">presentation(MustCover, Maxtime, Segments)</code> vốn đúng nếu $Segments$ là một danh sách phân đoạn có tổng thời lượng không vượt quá $Maxtime$ giây và bao quát toàn bộ các chủ đề trong danh sách $MustCover$. Minh họa và kiểm tra truy vấn với <code class="logic-expression">MustCover = [welcome, skiing, robots]</code> và $Maxtime = 90$.
- (b) Nêu ba tính năng quan trọng mà hệ thống trên chưa đáp ứng được trong một ứng dụng biên tập video thực tế.

::: details Lời giải chi tiết
**(a) Tiên đề hóa trong Prolog:**
```prolog
% presentation(MustCover, MaxTime, Segments)
presentation(MustCover, MaxTime, Segs) :-
    find_segments(MustCover, Segs),
    total_time(Segs, Time),
    Time =< MaxTime.

% Chọn các phân đoạn bao quát toàn bộ chủ đề
find_segments([], []).
find_segments([Topic | Rest], [Seg | Segs]) :-
    segment(Seg, _, Topics),
    member(Topic, Topics),
    remove_covered(Rest, Topics, Remaining),
    find_segments(Remaining, Segs).

% Loại bỏ các chủ đề đã được phân đoạn bao quát
remove_covered([], _, []).
remove_covered([T | Rest], Covered, Rem) :-
    member(T, Covered),
    remove_covered(Rest, Covered, Rem).
remove_covered([T | Rest], Covered, [T | Rem]) :-
    \+ member(T, Covered),
    remove_covered(Rest, Covered, Rem).

% Tính tổng thời lượng của danh sách phân đoạn
total_time([], 0).
total_time([Seg | Rest], Time) :-
    segment(Seg, Dur, _),
    total_time(Rest, RestTime),
    Time is Dur + RestTime.
```

Đối với truy vấn `ask presentation([welcome, skiing, robots], 90, Segs)`, hệ thống tìm được ít nhất hai nghiệm:
1. `Segs = [seg0, seg4]`: Tổng thời lượng $= 10 + 50 = 60 \le 90$. Chủ đề: $welcome$ (seg0), $skiing, robots$ (seg4).
2. `Segs = [seg2, seg1]`: Tổng thời lượng $= 50 + 30 = 80 \le 90$. Chủ đề: $welcome, robots$ (seg2), $skiing$ (seg1).

**(b) Ba hạn chế lớn trong thực tế:**
1. **Thiếu tính mạch lạc và thứ tự chuyển cảnh**: Chương trình chỉ quan tâm đến việc vét cạn chủ đề mà không xét đến thứ tự logic kể chuyện (ví dụ phân đoạn chào mừng $welcome$ phải luôn đứng ở đầu video thay vì bị xáo trộn ở cuối).
2. **Không xử lý trùng lặp nội dung**: Hai phân đoạn có thể cùng nói về một chủ đề dẫn tới việc người xem phải nghe lại cùng một thông tin thừa.
3. **Chưa có hàm tối ưu hóa**: Hệ thống chỉ kiểm tra điều kiện $Time \le MaxTime$ mà không tối ưu hóa các tiêu chí thẩm mỹ, chất lượng hình ảnh hoặc độ liền mạch của âm thanh giữa các phân đoạn.
:::
:::

::: exercise Bài tập 15.13: Biểu diễn ngôn ngữ $a^n b^n c^n$ bằng văn phạm DCG
Ngôn ngữ $L = \{a^n b^n c^n \mid n \ge 0\}$ gồm các chuỗi chứa một số lượng ký tự $a$, theo sau bởi cùng một số lượng ký tự $b$, và theo sau bởi cùng một số lượng ký tự $c$. Đây là ngôn ngữ phi ngữ cảnh kinh điển không thể biểu diễn được bằng văn phạm phi ngữ cảnh thông thường. Hãy định nghĩa ngôn ngữ này bằng văn phạm mệnh đề xác định (DCG).

::: details Lời giải chi tiết
Bằng cách sử dụng các đối số bổ sung để đếm số lượng ký tự thông qua ký hiệu số Peano ($0$ và $s(N)$), văn phạm DCG có thể biểu diễn hoàn hảo ngôn ngữ này:

```prolog
% Câu hợp lệ gồm n ký tự 'a', theo sau bởi n ký tự 'b', theo sau bởi n ký tự 'c'
s(L0, L3) :-
    as(N, L0, L1),
    bs(N, L1, L2),
    cs(N, L2, L3).

% Khớp N ký tự 'a'
as(0, L, L).
as(s(N), ["a" | L0], L1) :-
    as(N, L0, L1).

% Khớp N ký tự 'b'
bs(0, L, L).
bs(s(N), ["b" | L0], L1) :-
    bs(N, L0, L1).

% Khớp N ký tự 'c'
cs(0, L, L).
cs(s(N), ["c" | L0], L1) :-
    cs(N, L0, L1).
```

Ví dụ, câu `["a", "a", "b", "b", "c", "c"]` sẽ thành công với biến đếm $N = s(s(0))$, trong khi chuỗi bất đối xứng như `["a", "b", "c", "c"]` sẽ thất bại.
:::
:::

::: exercise Bài tập 15.14: Xây dựng cơ sở tri thức hỏi đáp địa lý bằng DCG
Xây dựng một cơ sở tri thức và từ điển dựa trên văn phạm ở Hình 15.11 và 15.12 của giáo trình để trả lời các câu hỏi địa lý tự nhiên. Đối với mỗi câu hỏi, hãy chỉ ra cách hệ thống trả lời hoặc giải thích lý do tại sao câu hỏi đó gặp khó khăn với các công cụ đã học.

::: details Lời giải chi tiết
Văn phạm DCG ở Mục 15.7 có thể xử lý tốt các câu hỏi có cấu trúc trực diện:
- *"What country borders Chile?"* $\implies$ Hợp nhất vị từ quan hệ $borders(Sub, chile)$ và tìm các cá thể $Sub$ thỏa mãn.
- *"What large country borders Argentina?"* $\implies$ Thêm điều kiện $large(Sub)$ và $borders(Sub, argentina)$.

Các dạng câu hỏi gặp khó khăn và nguyên nhân:
1. **Câu hỏi chứa phép so sánh bậc nhất (Superlatives)**: *"What is the largest country in South America?"*
   - *Khó khăn*: Cần phép toán cực trị $\arg\max$ trên diện tích của toàn bộ các quốc gia. Logic mệnh đề xác định thuần túy không hỗ trợ toán tử kết hợp/tổng hợp (aggregation) trừ khi mở rộng thêm các vị từ ngoại vi.
2. **Câu hỏi định lượng số lượng (Counting/Quantifiers)**: *"How many countries border Bolivia?"*
   - *Khó khăn*: Cần đếm số lượng nghiệm thỏa mãn, đòi hỏi cơ chế ngoài logic như `findall` hoặc `aggregate`.
3. **Câu hỏi phủ định**: *"Which country does not border the ocean?"*
   - *Khó khăn*: Đòi hỏi phủ định thất bại và giả định tri thức đầy đủ, cần xử lý cẩn trọng để tránh hiện tượng tắc nghẽn (floundering).
:::
:::

::: exercise Bài tập 15.15: Rủi ro khi đưa biến tự do vào phủ định thất bại
Xét trường hợp trong Ví dụ 15.44 nếu vị từ $empty\_course$ được định nghĩa trực tiếp bằng câu tuyển:

```prolog
empty_course(C) :-
    course(C),
    ~enrolled(S, C).
```

Giả sử phần còn lại của cơ sở tri thức là:

```prolog
course(cs422).
course(cs486).
course(cs987).

enrolled(huan, cs422).
enrolled(sally, cs486).
```

- (a) Bao đóng Clark của câu tuyển định nghĩa $empty\_course$ là gì?
- (b) Hãy chỉ ra một phản ví dụ về tính đúng đắn của bao đóng này: Nêu một thể hiện cụ thể mà ở đó thân câu tuyển nhận giá trị đúng nhưng đầu câu tuyển nhận giá trị sai.
- (c) Trình thông dịch Prolog thực tế sẽ trả về kết quả gì? So sánh với trường hợp đảo thứ tự mục tiêu trong thân câu tuyển:
  <span class="logic-expression logic-block">empty_course(C) ← $∼$enrolled(S, C) ∧ course(C).</span>

::: details Lời giải chi tiết
**(a) Bao đóng Clark của câu tuyển:**
Vì biến $S$ chỉ xuất hiện ở thân câu tuyển mà không có mặt ở đầu câu tuyển, nên ở dạng chuẩn Clark nó được lượng từ hóa tồn tại:
<span class="logic-expression logic-block">∀ C (empty_course(C) ↔ course(C) ∧ ∃ S ¬ enrolled(S, C))</span>

**(b) Phản ví dụ chứng minh sự vi phạm tính đúng đắn:**
- Xét khóa học $C = cs422$.
- Rõ ràng khóa học này **không rỗng** vì đã có sinh viên Huan đăng ký ($enrolled(huan, cs422)$). Do đó, về mặt ngữ nghĩa thế giới thực, $empty\_course(cs422)$ phải nhận giá trị **sai** ($false$).
- Tuy nhiên, hãy xét biểu thức thân của bao đóng Clark:
  <span class="logic-expression logic-block">course(cs422) ∧ ∃ S ¬ enrolled(S, cs422)</span>
  - $course(cs422)$ là đúng ($true$).
  - Tồn tại sinh viên $S$ không đăng ký $cs422$ không? Có! Chẳng hạn chọn $S = sally$. Rõ ràng $enrolled(sally, cs422)$ là sai, nên $\neg enrolled(sally, cs422)$ là đúng!
  - Như vậy mệnh đề $\exists S~\neg enrolled(S, cs422)$ nhận giá trị **đúng** ($true$)!
- Thân câu tuyển nhận giá trị $true$, nhưng đầu câu tuyển lại nhận giá trị $false$. Bao đóng kết luận sai lệch rằng $cs422$ là một khóa học rỗng!

**(c) Hành vi trong môi trường cài đặt Prolog thực tế:**
- Trong Prolog, toán tử phủ định `\+` hoạt động theo cơ chế phủ định thất bại: `\+ Goal` thành công khi và chỉ khi `Goal` thất bại.
- Với định nghĩa:
  ```prolog
  empty_course(C) :- course(C), \+ enrolled(S, C).
  ```
  Khi gọi truy vấn `ask empty_course(C)`:
  1. `course(C)` thành công với $C = cs422$.
  2. Tiếp theo Prolog gọi `\+ enrolled(S, cs422)`.
  3. Prolog thực thi mục tiêu con `enrolled(S, cs422)`. Mục tiêu này **thành công** với $S = huan$.
  4. Vì mục tiêu con thành công, toán tử `\+` thất bại!
  5. Prolog quay lui và thử khóa học tiếp theo. Với $C = cs987$, mục tiêu `enrolled(S, cs987)` thất bại, do đó `\+ enrolled(S, cs987)` thành công.
  Prolog trả về nghiệm chính xác $C = cs987$.

- Tuy nhiên, nếu đảo thứ tự:
  ```prolog
  empty_course(C) :- \+ enrolled(S, C), course(C).
  ```
  1. Prolog thực thi `\+ enrolled(S, C)` đầu tiên, khi cả $S$ và $C$ đều là biến tự do!
  2. Mục tiêu con `enrolled(S, C)` thành công ngay lập tức với nghiệm đầu tiên $S = huan, C = cs422$.
  3. Do đó `\+ enrolled(S, C)` thất bại ngay lập tức!
  4. Toàn bộ câu truy vấn `empty_course(C)` thất bại và trả về `no`, bỏ sót hoàn toàn khóa học rỗng thực sự là $cs987$!

Ví dụ kinh điển này minh chứng sâu sắc lý do tại sao không bao giờ được phép để biến tự do xuất hiện trong toán tử phủ định thất bại mà chưa được ràng buộc bởi các mục tiêu khẳng định khác.
:::
:::

## Tài liệu tham khảo

- Poole, D. L., & Mackworth, A. K. (2023). *Artificial Intelligence: Foundations of Computational Agents* (3rd ed.). Cambridge University Press. Bản điện tử: [https://artint.info/3e/html/ArtInt3e.Ch15.S13.html](https://artint.info/3e/html/ArtInt3e.Ch15.S13.html).
