---
course: ai-nen-tang-tac-tu
lecture: 15-ca-the-va-quan-he
section: topic
topic: 15-6-ky-hieu-ham-va-cau-truc-du-lieu
title: "15.6 Ký hiệu hàm và cấu trúc dữ liệu"
description: "Mở rộng Datalog với ký hiệu hàm: Biểu diễn cấu trúc dữ liệu đệ quy, tính đầy đủ Turing, logic bậc một và bậc hai, cùng cơ chế occurs check."
---

Datalog đòi hỏi phải có một tên gọi, sử dụng một hằng số, cho mọi cá thể mà hệ thống cần suy luận. Trong nhiều trường hợp, việc xác định một cá thể thông qua các thành phần cấu tạo nên nó sẽ đơn giản hơn nhiều so với việc bắt buộc phải có một hằng số riêng biệt cho từng cá thể.

::: example Ví dụ 15.23: Biểu diễn thời gian và ngày tháng
Trong nhiều miền ứng dụng, ta muốn coi thời gian là một cá thể. Chẳng hạn, ta muốn phát biểu rằng một khóa học diễn ra vào lúc 11:30 sáng. Ta không muốn gán một hằng số riêng biệt cho từng mốc thời gian khả dĩ, dù điều này hoàn toàn có thể làm được.

Việc định nghĩa thời gian thông qua số giờ trôi qua kể từ nửa đêm và số phút trôi qua trong giờ đó sẽ thuận tiện hơn nhiều. Tương tự, ta có thể muốn suy luận với các sự kiện về những ngày tháng cụ thể. Ta không thể gán một hằng số cho từng ngày tùy ý trong tương lai xa, bởi có vô hạn ngày tháng có thể xảy ra. Thay vào đó, việc định nghĩa một ngày theo năm, tháng và ngày sẽ dễ dàng hơn nhiều.
:::

Việc sử dụng một hằng số để đặt tên cho từng cá thể đồng nghĩa với việc cơ sở tri thức chỉ có thể biểu diễn một số lượng hữu hạn các cá thể, và số lượng cá thể này bị cố định ngay khi cơ sở tri thức được xây dựng. Tuy nhiên, ta thường muốn suy luận trên một tập hợp cá thể tiềm năng vô hạn.

::: example Ví dụ 15.24: Biểu diễn câu trong xử lý ngôn ngữ tự nhiên
Giả sử ta muốn xây dựng một hệ thống tiếp nhận các câu hỏi bằng tiếng Anh và trả lời câu hỏi bằng cách tra cứu cơ sở dữ liệu trực tuyến. Trong trường hợp này, mỗi câu là một cá thể. Ta không muốn phải gán tên riêng cho từng câu, bởi số lượng câu tiếng Anh là quá lớn để có thể đặt tên hết.

Cách tiếp cận khả thi hơn là đặt tên cho các từ, sau đó xác định mỗi câu thông qua chuỗi các từ cấu thành nên câu đó. Phương pháp này thực tế hơn vì số lượng từ cần đặt tên ít hơn số lượng câu rất nhiều, và mỗi từ đều đã có một tên gọi tự nhiên. Ta cũng có thể muốn xác định các từ dựa trên các chữ cái cấu tạo nên từ đó hoặc dựa trên các thành phần ngữ pháp của chúng.
:::

Ký hiệu hàm (function symbols) cho phép ta mô tả các cá thể một cách gián tiếp. Thay vì dùng một hằng số để mô tả một cá thể, cá thể đó được mô tả thông qua các cá thể khác. Ký hiệu hàm giúp ngôn ngữ biểu diễn được các cấu trúc dữ liệu phong phú; một ký hiệu hàm biểu thị một tập hợp có cấu trúc gồm các thực thể khác.

Về mặt cú pháp, một ký hiệu hàm là một từ bắt đầu bằng chữ cái viết thường. Định nghĩa về số hạng (term) được mở rộng: Một số hạng là một biến, một hằng số, hoặc có dạng $f(t_{1}, \ldots, t_{n})$, trong đó $f$ là một ký hiệu hàm và mỗi $t_{i}$ là một số hạng. Ngoại trừ việc mở rộng định nghĩa về số hạng, phần còn lại của ngôn ngữ vẫn giữ nguyên.

Số hạng chỉ xuất hiện bên trong các ký hiệu vị từ. Ta không viết các câu tuyển có vế kết luận suy ra một số hạng. Tuy nhiên, ta có thể viết các câu tuyển chứa các nguyên tử có sử dụng ký hiệu hàm.

Ngữ nghĩa của Datalog được mở rộng để phản ánh cú pháp mới này. Định nghĩa về ánh xạ $\phi$ được mở rộng sao cho $\phi$ cũng gán cho mỗi ký hiệu hàm $n$ ngôi một hàm toán học từ $\mathcal{D}^{n}$ vào $\mathcal{D}$. Một hằng số có thể xem là một ký hiệu hàm 0 ngôi (tức không có đối số). Như vậy, $\phi$ xác định cá thể nào được biểu thị bởi mỗi số hạng không biến.

::: example Ví dụ 15.25: Biểu diễn ngày tháng với ký hiệu hàm
Giả sử ta muốn định nghĩa ngày tháng, chẳng hạn ngày 20 tháng 7 năm 1969, ngày đầu tiên con người đặt chân lên Mặt Trăng. Ta có thể sử dụng ký hiệu hàm $ce$ (Công nguyên — common era), sao cho $ce(Y, M, D)$ biểu thị một ngày với năm $Y$, tháng $M$ và ngày $D$. Chẳng hạn, $ce(1969, jul, 20)$ biểu thị ngày 20 tháng 7 năm 1969. Tương tự, ta có thể định nghĩa ký hiệu $bce$ để biểu thị một ngày trước Công nguyên.

Cách duy nhất để sử dụng ký hiệu hàm là viết các câu tuyển định nghĩa các quan hệ có chứa ký hiệu hàm đó. Không có khái niệm "định nghĩa" hàm $ce$; ngày tháng không nằm trong máy tính, cũng như con người không nằm trong máy tính vậy.

Để sử dụng ký hiệu hàm, ta có thể viết các câu tuyển được lượng từ hóa trên các đối số của ký hiệu hàm. Ví dụ dưới đây định nghĩa quan hệ $before(D_{1}, D_{2})$, vốn đúng nếu ngày $D_{1}$ diễn ra trước ngày $D_{2}$ trong lịch.
:::

Quan hệ $before(D_{1}, D_{2})$ được tiên đề hóa bằng các luật sau:

```prolog
% D1 diễn ra trước D2 nếu năm của D1 nhỏ hơn năm của D2
before(ce(Y1, M1, D1), ce(Y2, M2, D2)) :-
    Y1 < Y2.

% Nếu cùng năm, D1 diễn ra trước D2 nếu tháng của D1 đứng trước tháng của D2
before(ce(Y, M1, D1), ce(Y, M2, D2)) :-
    month(M1, N1),
    month(M2, N2),
    N1 < N2.

% Nếu cùng năm và cùng tháng, D1 diễn ra trước D2 nếu ngày của D1 nhỏ hơn ngày của D2
before(ce(Y, M, D1), ce(Y, M, D2)) :-
    D1 < D2.

% month(M, N) đúng nếu tháng M là tháng thứ N trong năm
month(jan, 1).   month(feb, 2).   month(mar, 3).
month(apr, 4).   month(may, 5).   month(jun, 6).
month(jul, 7).   month(aug, 8).   month(sep, 9).
month(oct, 10).  month(nov, 11).  month(dec, 12).
```

*Hình 15.7: Tiên đề hóa quan hệ "trước" cho các ngày trong Công nguyên.*

Hệ luật này giả định vị từ "$<$" biểu thị quan hệ "nhỏ hơn" giữa các số nguyên. Quan hệ này có thể được biểu diễn bằng các câu tuyển, nhưng thường được định nghĩa sẵn, như trong ngôn ngữ Prolog. Các tháng được biểu diễn bằng các hằng số gồm ba chữ cái đầu của tên tháng.

Một cơ sở tri thức bao gồm các câu tuyển có chứa ký hiệu hàm có thể tính toán bất kỳ hàm tính toán được nào. Do đó, một cơ sở tri thức có thể được diễn giải như một chương trình, gọi là một chương trình logic (logic program). Các chương trình logic đạt tính đầy đủ Turing (Turing complete); chúng có thể tính toán bất kỳ hàm nào có thể tính toán được trên một máy tính kỹ thuật số.

Sự mở rộng ngôn ngữ này đem lại một tác động to lớn: Chỉ với một ký hiệu hàm và một hằng số, ngôn ngữ đã chứa vô hạn số hạng không biến và vô hạn nguyên tử không biến. Tập hợp vô hạn các số hạng này có thể được dùng để mô tả một số lượng vô hạn các cá thể.

Ký hiệu hàm được sử dụng để xây dựng các cấu trúc dữ liệu, như trong các ví dụ dưới đây.

::: example Ví dụ 15.26: Cấu trúc dữ liệu cây
Cây là một cấu trúc dữ liệu hữu ích. Ta có thể dùng cây để xây dựng biểu diễn cú pháp của một câu cho hệ thống xử lý ngôn ngữ tự nhiên. Ta có thể quy ước rằng một cây có nhãn hoặc có dạng $node(N, LT, RT)$, hoặc có dạng $leaf(L)$. Như vậy, $node$ là một hàm nhận một tên, một cây con trái và một cây con phải để tạo thành một cây. Ký hiệu hàm $leaf$ biểu thị một hàm chuyển từ nhãn của một nút lá thành một cây.

Quan hệ $at\_leaf(L, T)$ đúng nếu nhãn $L$ là nhãn của một lá trong cây $T$. Quan hệ này có thể được định nghĩa như sau:

```prolog
at_leaf(L, leaf(L)).
at_leaf(L, node(N, LT, RT)) :-
    at_leaf(L, LT).
at_leaf(L, node(N, LT, RT)) :-
    at_leaf(L, RT).
```

Đây là một ví dụ về chương trình đệ quy cấu trúc. Các quy tắc bao quát toàn bộ các trường hợp cấu trúc biểu diễn cây.

Quan hệ $in\_tree(L, T)$, đúng nếu nhãn $L$ là nhãn của một nút bên trong của cây $T$, có thể được định nghĩa như sau:

```prolog
in_tree(L, node(L, LT, RT)).
in_tree(L, node(N, LT, RT)) :-
    in_tree(L, LT).
in_tree(L, node(N, LT, RT)) :-
    in_tree(L, RT).
```
:::

::: example Ví dụ 15.27: Biểu diễn danh sách
Danh sách là một dãy có thứ tự gồm các phần tử. Ta có thể suy luận về danh sách chỉ bằng các ký hiệu hàm và hằng số, mà không cần khái niệm danh sách phải được định nghĩa sẵn trong ngôn ngữ. Một danh sách hoặc là danh sách rỗng, hoặc là một phần tử đứng trước một danh sách. Ta có thể đặt ra một hằng số để biểu thị danh sách rỗng, chẳng hạn dùng hằng số $nil$. Ta chọn một ký hiệu hàm, chẳng hạn $cons(Hd, Tl)$, với diễn giải dự định rằng nó biểu thị một danh sách có phần tử đầu tiên là $Hd$ và phần còn lại của danh sách là $Tl$. Danh sách chứa các phần tử $a, b, c$ khi đó được biểu diễn là:

$$
cons(a, cons(b, cons(c, nil)))
$$

Để sử dụng danh sách, ta cần viết các vị từ thao tác trên chúng. Chẳng hạn, quan hệ $append(X, Y, Z)$ đúng khi $X, Y, Z$ là các danh sách sao cho $Z$ chứa các phần tử của $X$ được tiếp nối bởi các phần tử của $Y$. Quan hệ này được định nghĩa đệ quy như sau:

```prolog
append(nil, L, L).
append(cons(Hd, X), Y, cons(Hd, Z)) :-
    append(X, Y, Z).
```

Không có gì đặc biệt đối với tên gọi $cons$ hay $nil$; ta hoàn toàn có thể thay bằng các tên gọi khác như $foo$ và $bar$.
:::

### Logic bậc một và logic bậc hai

Phép tính vị từ bậc một (First-order predicate calculus) là một hệ logic mở rộng phép tính mệnh đề nhằm bao gồm các nguyên tử có ký hiệu hàm và các biến logic. Mọi biến logic đều phải được lượng từ hóa tường minh thông qua "với mọi" ($\forall$) và "tồn tại" ($\exists$). Ngữ nghĩa của phép tính vị từ bậc một tương tự ngữ nghĩa của các chương trình logic được trình bày trong chương này, nhưng có tập toán tử phong phú hơn.

Ngôn ngữ của các chương trình logic tạo thành một tập con thực dụng của phép tính vị từ bậc một, được phát triển vì tính hữu ích trong nhiều bài toán. Phép tính vị từ bậc một có thể xem là ngôn ngữ bổ sung phép tuyển và phép lượng từ hóa tường minh vào các chương trình logic.

Logic bậc một được gọi là *bậc một* (first order) vì nó cho phép lượng từ hóa trên các cá thể trong miền xác định. Logic bậc một không cho phép biến đại diện cho vị từ, cũng như không cho phép lượng từ hóa trên các vị từ.

Logic bậc hai (Second-order logic) cho phép lượng từ hóa trên các quan hệ bậc một, và cho phép các vị từ nhận đối số là các quan hệ bậc một. Đây là các quan hệ bậc hai. Ví dụ, công thức logic bậc hai sau:

<pre class="logic-expression">∀ R symmetric(R) ↔ (∀ X ∀ Y R(X, Y) → R(Y, X))</pre>

định nghĩa quan hệ bậc hai $symmetric$, vốn đúng nếu đối số của nó là một quan hệ đối xứng.

Logic bậc hai dường như là cần thiết trong nhiều ứng dụng vì bao đóng bắc cầu (transitive closure) không thể định nghĩa được trong logic bậc một. Chẳng hạn, giả sử ta muốn $before$ là bao đóng bắc cầu của $next$, trong đó $next(X, s(X))$ là đúng. Hãy hình dung $next$ mang ý nghĩa "mili-giây tiếp theo" và $before$ biểu thị "trước". Định nghĩa tự nhiên trong logic bậc một sẽ là:

<pre class="logic-expression">∀ X ∀ Y before(X, Y) ↔ (Y = s(X) ∨ before(s(X), Y))</pre>

Biểu thức này không nắm bắt chính xác định nghĩa trên, bởi vì chẳng hạn:

<pre class="logic-expression">∀ X ∀ Y before(X, Y) → ∃ W Y = s(W)</pre>

không suy diễn được một cách logic từ công thức trên. Lý do là tồn tại các mô hình phi chuẩn (nonstandard models) của công thức, trong đó $Y$ biểu thị giá trị *vô hạn* ($\infty$). Để nắm bắt bao đóng bắc cầu, ta cần một công thức khẳng định rằng $before$ là vị từ cực tiểu thỏa mãn định nghĩa. Điều này chỉ có thể phát biểu được bằng cách sử dụng logic bậc hai.

Logic bậc một đạt tính nửa quyết định được (semi-decidable), nghĩa là tồn tại một thủ tục chứng minh đúng đắn và đầy đủ, trong đó mọi phát biểu đúng đều có thể được chứng minh, nhưng thủ tục có thể không dừng nếu phát biểu không đúng. Logic bậc hai là không quyết định được (undecidable); không thể cài đặt bất kỳ thủ tục chứng minh đúng đắn và đầy đủ nào cho logic bậc hai trên một máy Turing.

## 15.6.1 Thủ tục chứng minh với ký hiệu hàm

Các thủ tục chứng minh có chứa biến vẫn áp dụng được cho trường hợp có ký hiệu hàm. Điểm khác biệt chính là tập hợp các số hạng được mở rộng để chứa các ký hiệu hàm.

Việc sử dụng ký hiệu hàm kéo theo số lượng số hạng là vô hạn. Để đảm bảo tính đầy đủ, quá trình suy diễn tiến (bottom-up / forward chaining) trên các câu tuyển phải đảm bảo tiêu chí lựa chọn câu tuyển là công bằng (fair).

::: example Ví dụ 15.28: Tầm quan trọng của tính công bằng trong suy diễn tiến
Để thấy rõ lý do tại sao tính công bằng lại quan trọng, xét các câu tuyển sau:

```prolog
num(0).
num(s(N)) :- num(N).
a :- b.
b.
```

Một chiến lược không công bằng có thể ban đầu chọn câu tuyển thứ nhất để suy diễn tiến, và trong mọi bước lựa chọn tiếp theo, chiến lược này luôn chọn câu tuyển thứ hai. Câu tuyển thứ hai luôn có thể được dùng để dẫn xuất một hệ quả mới ($num(s(0)), num(s(s(0))), \ldots$). Chiến lược này không bao giờ chọn một trong hai câu tuyển cuối cùng, và do đó không bao giờ dẫn xuất được $a$ hoặc $b$.

Vấn đề bỏ quên vĩnh viễn một số câu tuyển được gọi là hiện tượng bỏ đói (starvation). Một tiêu chí lựa chọn công bằng là tiêu chí đảm bảo rằng bất kỳ câu tuyển nào có thể chọn được thì sớm muộn cũng sẽ được chọn. Thủ tục chứng minh bottom-up có thể sinh ra một chuỗi vô hạn các hệ quả, và nếu sự lựa chọn là công bằng thì mỗi hệ quả sớm muộn đều sẽ được sinh ra, do đó thủ tục chứng minh đạt tính đầy đủ.
:::

Thủ tục chứng minh từ trên xuống (top-down) hoàn toàn giống như đối với Datalog. Phép hợp nhất (unification) trở nên phức tạp hơn vì nó phải đệ quy đi sâu vào cấu trúc của các số hạng. Có một điểm thay đổi đối với thuật toán hợp nhất: Một biến $X$ không thể hợp nhất với một số hạng $t$ nếu $X$ xuất hiện bên trong $t$ và $t$ không phải chính là $X$. Thuật toán phải trả về $\bot$ nếu phép thế $X/t$ chuẩn bị được thêm vào tập thế $S$ trong khi biến $X$ xuất hiện trong số hạng $t$. Việc kiểm tra điều kiện này được gọi là kiểm tra xuất hiện (occurs check).

Phép kiểm tra xuất hiện đôi khi bị lược bỏ (chẳng hạn trong nhiều hệ thống Prolog) vì việc bỏ qua nó giúp thủ tục chứng minh thực thi nhanh hơn, mặc dù việc bỏ kiểm tra này làm cho thủ tục chứng minh mất đi tính đúng đắn, như được minh họa trong ví dụ sau.

::: example Ví dụ 15.29: Mất tính đúng đắn khi bỏ qua occurs check
Xét cơ sở tri thức chỉ gồm duy nhất một câu tuyển:

$$
lt(X, s(X)).
$$

Giả sử diễn giải dự định là miền các số nguyên, trong đó $lt$ mang nghĩa "nhỏ hơn" và $s(X)$ biểu thị số nguyên liền sau $X$. Truy vấn:

$$
\text{ask } lt(Y, Y)
$$

đáng lẽ phải thất bại vì nó sai trong diễn giải dự định; không có số nguyên nào nhỏ hơn chính nó. Tuy nhiên, nếu $X$ và $s(X)$ có thể hợp nhất được (do không kiểm tra $X$ xuất hiện trong $s(X)$), truy vấn này sẽ thành công. Trong trường hợp đó, thủ tục chứng minh không đúng đắn vì nó có thể dẫn xuất được một khẳng định sai trong một mô hình của các tiên đề.
:::

Ví dụ sau đây minh họa chi tiết về phép phân giải SLD khi có ký hiệu hàm.

::: example Ví dụ 15.30: Chi tiết phân giải SLD với ký hiệu hàm
Xét các câu tuyển sau:

```prolog
append(c(A, X), Y, c(A, Z)) :- append(X, Y, Z).
append(nil, Z, Z).
```

Ở đây, ta tạm thời bỏ qua ý nghĩa trực giác của các ký hiệu này. Tương tự như máy tính, ta xem đây thuần túy là một bài toán thao tác trên các ký hiệu. Xét câu truy vấn sau:

<pre class="logic-expression">ask  append(F, c(L, nil), c(l, c(i, c(s, c(t, nil))))).</pre>

Quá trình dẫn xuất diễn ra như sau:

1. Câu tuyển trả lời khởi đầu:
   <pre class="logic-expression">yes(F, L) ← append(F, c(L, nil), c(l, c(i, c(s, c(t, nil)))))</pre>
2. Phân giải với câu tuyển <code class="logic-expression">append(c(A_1, X_1), Y_1, c(A_1, Z_1)) ← append(X_1, Y_1, Z_1)</code>:
   - Phép thế hợp nhất:
     <pre class="logic-expression">{F/c(l, X_1), Y_1/c(L, nil), A_1/l, Z_1/c(i, c(s, c(t, nil)))}</pre>
   - Câu tuyển mục tiêu thu được:
     <pre class="logic-expression">yes(c(l, X_1), L) ← append(X_1, c(L, nil), c(i, c(s, c(t, nil))))</pre>
3. Phân giải tiếp với <code class="logic-expression">append(c(A_2, X_2), Y_2, c(A_2, Z_2)) ← append(X_2, Y_2, Z_2)</code>:
   - Phép thế hợp nhất:
     <pre class="logic-expression">{X_1/c(i, X_2), Y_2/c(L, nil), A_2/i, Z_2/c(s, c(t, nil))}</pre>
   - Câu tuyển mục tiêu thu được:
     <pre class="logic-expression">yes(c(l, c(i, X_2)), L) ← append(X_2, c(L, nil), c(s, c(t, nil))))</pre>
4. Phân giải tiếp với <code class="logic-expression">append(c(A_3, X_3), Y_3, c(A_3, Z_3)) ← append(X_3, Y_3, Z_3)</code>:
   - Phép thế hợp nhất:
     <pre class="logic-expression">{X_2/c(s, X_3), Y_3/c(L, nil), A_3/s, Z_3/c(t, nil)}</pre>
   - Câu tuyển mục tiêu thu được:
     <pre class="logic-expression">yes(c(l, c(i, c(s, X_3))), L) ← append(X_3, c(L, nil), c(t, nil))</pre>

Tại giai đoạn này, cả hai câu tuyển đều có thể áp dụng được. Nếu chọn câu tuyển thứ nhất:
- Phân giải với <code class="logic-expression">append(c(A_4, X_4), Y_4, c(A_4, Z_4)) ← append(X_4, Y_4, Z_4)</code>:
  - Phép thế: <code class="logic-expression">{X_3/c(t, X_4), Y_4/c(L, nil), A_4/t, Z_4/nil}</code>
  - Mục tiêu thu được:
    <pre class="logic-expression">yes(c(l, c(i, c(s, X_3))), L) ← append(X_4, c(L, nil), nil)</pre>
  - Tại đây, không có câu tuyển nào có phần đầu hợp nhất được với nguyên tử trong thân câu tuyển mục tiêu. Nhánh chứng minh này thất bại.

Nếu chọn câu tuyển thứ hai thay vì câu tuyển thứ nhất:
- Phân giải với $append(nil, Z_5, Z_5)$:
  - Phép thế hợp nhất: $\{Z_5/c(t, nil), X_3/nil, L/t\}$
  - Câu tuyển mục tiêu thu được:
    $$yes(c(l, c(i, c(s, nil))), t) \leftarrow$$
  - Tại điểm này, việc chứng minh thành công, với câu trả lời:
    $$F = c(l, c(i, c(s, nil))), \quad L = t$$
:::

Trong phần còn lại của chương này, ta sử dụng ký hiệu "đường cú pháp" (syntactic sugar) của ngôn ngữ Prolog để biểu diễn danh sách. Danh sách rỗng $nil$ được viết là $[\,]$. Danh sách có phần tử đầu tiên $E$ và phần còn lại $R$ (vốn là $cons(E, R)$ trong Ví dụ 15.27) được viết là $[E \mid R]$. Ngoài ra còn có một quy ước đơn giản hóa ký hiệu: $[X \mid [Y]]$ được viết là $[X, Y]$, trong đó $Y$ có thể là một chuỗi các giá trị. Ví dụ, $[a \mid [\,]]$ được viết là $[a]$, và $[b \mid [a \mid [\,]]]$ được viết là $[b, a]$. Số hạng $[a \mid [b \mid C]]$ được viết là $[a, b \mid C]$.

::: example Ví dụ 15.31: Phân giải SLD với ký pháp danh sách trong Prolog
Sử dụng ký pháp danh sách, vị từ $append$ từ ví dụ trước có thể được viết thành:

```prolog
append([A | X], Y, [A | Z]) :-
    append(X, Y, Z).
append([], Z, Z).
```

Câu truy vấn:

$$
\text{ask } append(F, [L], [l, i, s, t])
$$

sẽ có câu trả lời là:

$$
F = [l, i, s], \quad L = t
$$

Quá trình chứng minh hoàn toàn tương tự như trong ví dụ trước. Đối với thủ tục chứng minh, bản chất thuật toán không hề thay đổi; đây chỉ đơn thuần là việc đổi tên ký hiệu hàm và hằng số cho dễ đọc hơn.
:::

## Tài liệu tham khảo

- Poole, D. L., & Mackworth, A. K. (2023). *Artificial Intelligence: Foundations of Computational Agents* (3rd ed.). Cambridge University Press. Bản điện tử: [https://artint.info/3e/html/ArtInt3e.Ch15.S6.html](https://artint.info/3e/html/ArtInt3e.Ch15.S6.html).
