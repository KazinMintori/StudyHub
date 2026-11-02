---
course: ai-nen-tang-tac-tu
lecture: 15-ca-the-va-quan-he
section: topic
topic: 15-3-logic-vi-tu
title: "15.3 Logic vị từ"
description: "Cú pháp và ngữ nghĩa hình thức của logic vị từ: Miền cá thể, phép gán biến, lượng từ, công thức mở và quy trình xây dựng cơ sở tri thức."
---

Logic vị từ (predicate calculus hay predicate logic) mở rộng [logic mệnh đề](https://artint.info/3e/html/ArtInt3e.Ch5.S1.html) theo hai phương diện:

- Các nguyên tử mang cấu trúc nội tại và có thể bao gồm hằng số cùng biến logic.
- Lượng từ hóa các biến logic.

Tài liệu này tuân theo quy ước cú pháp của Prolog: Các biến bắt đầu bằng một chữ cái viết hoa. Trong toán học, các biến thường là $x$, $y$ và $z$. Trong Prolog, cũng như trong các ngôn ngữ lập trình khác, các tên dài hơn thường được dùng để mã nguồn dễ đọc hơn. Chữ hoa được sử dụng để làm nổi bật các biến.

Cú pháp của logic vị từ mở rộng cú pháp của [logic mệnh đề](https://artint.info/3e/html/ArtInt3e.Ch5.S1.html#SS1) như sau, trong đó một ký hiệu là một chuỗi các chữ cái, chữ số hoặc dấu gạch dưới (`_`):

- **Biến logic (Logical variable)**: Là một ký hiệu bắt đầu bằng một chữ cái viết hoa hoặc dấu gạch dưới `_`. Ví dụ: $X$, $Room$, $\_B4$, $Raths$, và $The\_big\_guy$ đều là các biến.
- **Hằng số (Constant)**: Là một ký hiệu bắt đầu bằng một chữ cái viết thường, một hằng số số học, hoặc một chuỗi ký tự.
- **Ký hiệu vị từ (Predicate symbol)**: Là một ký hiệu bắt đầu bằng một chữ cái viết thường. Hằng số và ký hiệu vị từ có thể phân biệt được thông qua ngữ cảnh xuất hiện trong cơ sở tri thức. Ví dụ: `kim`, `r123`, `f`, `grandfather`, và `borogroves` có thể là hằng số hoặc ký hiệu vị từ tùy theo ngữ cảnh; `725` là một hằng số.
- **Số hạng (Term)**: Là một biến hoặc một hằng số. Ví dụ: $X$, $kim$, $cs422$, $mome$, hoặc $Raths$ đều có thể là số hạng.
- **Ký hiệu nguyên tử (Atomic symbol)**, hay gọi đơn giản là **nguyên tử (Atom)**: Có dạng $p$ hoặc $p(t_{1}, \ldots, t_{n})$, trong đó $p$ là một ký hiệu vị từ và mỗi $t_{i}$ là một số hạng. Mỗi $t_{i}$ được gọi là một đối số của vị từ. Ví dụ: `teaches(sue, cs422)`, `in(kim, r123)`, `father(bill, Y)`, `happy(C)`, `outgrabe(mome, Raths)`, và `sunny` đều có thể là các nguyên tử. Từ ngữ cảnh trong nguyên tử `outgrabe(mome, Raths)`, ký hiệu `outgrabe` là một ký hiệu vị từ, còn `mome` là một hằng số.

Một công thức logic được xây dựng từ các nguyên tử bằng cách sử dụng các phép nối logic của [logic mệnh đề](https://artint.info/3e/html/ArtInt3e.Ch5.S1.html#SS1) và các lượng từ. Các biểu thức sau cũng là công thức logic:

- $\forall X~p$: Trong đó $X$ là một biến, và $p$ là một công thức logic (thường chứa biến $X$), được đọc là "với mọi $X$, có $p$". Biến $X$ được gọi là được lượng từ hóa với mọi.
- $\exists X~p$: Trong đó $X$ là một biến, và $p$ là một công thức logic, được đọc là "tồn tại một $X$ sao cho $p$". Biến $X$ được gọi là được lượng từ hóa tồn tại.

::: example Ví dụ 15.3: Các công thức logic vị từ
Các biểu thức sau đây là những công thức logic:

<span class="logic-expression logic-block">∀ G (grandfather(sam, G) ← ∃ P (father(sam, P) ∧ parent(P, G)))</span>

<span class="logic-expression logic-block">in(X, Y) ← part_of(Z, Y) ∧ in(X, Z)</span>

<span class="logic-expression logic-block">slithy(toves) ← ∀ Raths (mimsy ∧ borogroves ∧ outgrabe(mome, Raths))</span>

Dựa vào ngữ cảnh: `sam`, `toves` và `mome` là các hằng số; `grandfather`, `father`, `parent`, `in`, `part_of`, `slithy`, `mimsy`, `borogroves` và `outgrabe` là các ký hiệu vị từ; còn $G, P, X, Y, Z$ và $Raths$ là các biến logic.

Hai công thức đầu tiên có thể gợi lên một ý nghĩa trực giác nào đó đối với con người, ngay cả khi chưa có đặc tả hình thức tường minh về ý nghĩa công thức. Tuy nhiên, bất kể các tên gợi nhớ có tính khơi gợi ra sao, đối với máy tính, hai công thức đầu tiên không mang nhiều ý nghĩa hơn công thức thứ ba. Ý nghĩa chỉ được xác lập thông qua ngữ nghĩa hình thức.
:::

Một biểu thức được gọi là **không biến** (ground) nếu nó không chứa bất kỳ biến logic nào. Ví dụ: `teaches(chris, cs322)` là biểu thức không biến, trong khi `teaches(Prof, Course)` không phải là biểu thức không biến.

## 15.3.1 Ngữ nghĩa của các công thức logic không biến

Bước đầu tiên trong việc xây dựng ngữ nghĩa của logic vị từ là xác định ngữ nghĩa cho trường hợp không biến (không chứa biến).

Một diễn giải là một bộ ba:

$$
I = \langle D, \phi, \pi \rangle
$$

- $D$ là một tập hợp khác rỗng được gọi là **miền cá thể** (domain). Các phần tử của $D$ là các cá thể.
- $\phi$ là một ánh xạ gán cho mỗi hằng số một phần tử của $D$.
- $\pi$ là một ánh xạ gán cho mỗi ký hiệu vị từ $n$ ngôi một hàm từ $D^{n}$ vào tập giá trị chân lý:

  $$
  \{true, false\}
  $$

Ánh xạ $\phi$ là một hàm từ các tên gọi sang các cá thể trong thế giới. Hằng số $c$ được gọi là biểu thị cho cá thể $\phi(c)$. Ở đây $c$ là một ký hiệu, nhưng $\phi(c)$ có thể là bất cứ thứ gì: Một cá thể vật lý thực như một con người hay một loại virus, một khái niệm trừu tượng như một khóa học, tình yêu, con số 2, hoặc chính một ký hiệu.

Ánh xạ $\pi(p)$ xác định xem mối quan hệ biểu thị bởi ký hiệu vị từ $n$ ngôi $p$ nhận giá trị đúng hay sai đối với mỗi bộ $n$ cá thể. Nếu ký hiệu vị từ $p$ không có đối số, thì $\pi(p)$ nhận giá trị $true$ hoặc $false$. Do đó, đối với các ký hiệu vị từ không có đối số, ngữ nghĩa này thu gọn về [ngữ nghĩa của logic mệnh đề](https://artint.info/3e/html/ArtInt3e.Ch5.S1.html#SS2).

::: example Ví dụ 15.4: Diễn giải trên một bàn học cụ thể
Xét thế giới gồm ba vật thể đặt trên bàn:

✂ (kéo) &emsp; ✈ (máy bay mô hình) &emsp; ✎ (bút chì)

Các vật thể này được vẽ theo cách như vậy vì chúng là những thực thể trong thế giới thực, không phải là các ký hiệu. Ký hiệu ✂ là một chiếc kéo, ✈ là một chiếc máy bay mô hình, và ✎ là một chiếc bút chì.

Giả sử các hằng số trong ngôn ngữ của chúng ta là $plane$, $pencil$ và $model$; các ký hiệu vị từ là $noisy$ và $left\_of$. Giả sử $noisy$ là vị từ một ngôi (nhận một đối số) và $left\_of$ là vị từ hai ngôi (nhận hai đối số).

Một ví dụ về diễn giải biểu diễn các cá thể trên bàn như sau:

- Miền cá thể:

  $$
  D = \{✂, ✈, ✎\}
  $$

- Ánh xạ hằng số:

  <span class="logic-expression logic-block">φ(plane) = ✈,   φ(pencil) = ✎,   φ(model) = ✈</span>

- Ánh xạ vị từ:

  Đối với $\pi(noisy)$:
  - $\langle ✂ \rangle \mapsto false$
  - $\langle ✈ \rangle \mapsto true$
  - $\langle ✎ \rangle \mapsto false$

  Đối với $\pi(left\_of)$:
  - <code class="logic-expression">⟨ ✂, ✂ ⟩ ↦ false,   ⟨ ✂, ✈ ⟩ ↦ true,   ⟨ ✂, ✎ ⟩ ↦ true</code>
  - <code class="logic-expression">⟨ ✈, ✂ ⟩ ↦ false,   ⟨ ✈, ✈ ⟩ ↦ false,   ⟨ ✈, ✎ ⟩ ↦ true</code>
  - <code class="logic-expression">⟨ ✎, ✂ ⟩ ↦ false,   ⟨ ✎, ✈ ⟩ ↦ false,   ⟨ ✎, ✎ ⟩ ↦ false</code>

Vì $noisy$ là vị từ một ngôi, nó nhận một cá thể đơn lẻ và có một giá trị chân lý cho từng cá thể.

Vì $left\_of$ là vị từ hai ngôi, nó nhận một cặp cá thể và nhận giá trị đúng khi phần tử thứ nhất của cặp nằm bên trái phần tử thứ hai. Chẳng hạn:

$$
\pi(left\_of)(\langle ✂, ✈ \rangle) = true
$$

bởi vì chiếc kéo nằm ở bên trái chiếc máy bay mô hình; trong khi:

$$
\pi(left\_of)(\langle ✎, ✎ \rangle) = false
$$

bởi vì chiếc bút chì không thể nằm bên trái chính nó.

Lưu ý rằng miền $D$ là một tập hợp các thực thể trong thế giới. Các quan hệ là các mối quan hệ giữa các cá thể trong thế giới, chứ không phải giữa các tên gọi. Do $\phi$ quy định rằng cả $plane$ và $model$ cùng biểu thị một cá thể duy nhất, nên mọi phát biểu về hai hằng số này đều nhận giá trị chân lý hoàn toàn giống nhau trong diễn giải này.
:::

::: example Ví dụ 15.5: Diễn giải ngữ nghĩa tòa nhà công nghệ thông tin
Xét diễn giải của [Hình 15.1](https://artint.info/3e/html/ArtInt3e.Ch15.S2.html#Ch15.F1).

Miền cá thể $D$ là tập hợp gồm bốn phần tử: Con người Kim, phòng 123, phòng 023 và tòa nhà CS. Đây không phải là tập hợp gồm bốn ký hiệu, mà là tập hợp chứa con người thật, các căn phòng thật và tòa nhà thật. Rất khó để viết ra tập hợp này một cách hình thức và người thiết kế thực tế không bắt buộc phải làm vậy. Để ghi nhớ ý nghĩa và truyền đạt cho người khác, người thiết kế cơ sở tri thức thường mô tả $D$, $\phi$ và $\pi$ bằng cách chỉ vào các cá thể vật lý hoặc hình vẽ biểu diễn chúng (như trong Hình 15.1), hoặc mô tả ý nghĩa bằng ngôn ngữ tự nhiên.

Các hằng số là $kim$, $r123$, $r023$ và $cs\_building$. Ánh xạ $\phi$ được xác định bởi các cung màu xám đi từ mỗi hằng số này tới một cá thể trong thế giới như minh họa ở Hình 15.1.

Các ký hiệu vị từ là $person$, $in$ và $part\_of$. Ý nghĩa của chúng được truyền tải trong hình bằng các cung nối từ các ký hiệu vị từ đến các quan hệ tương ứng.

Như vậy, con người tên là Kim ở trong phòng $r123$ và cũng ở trong tòa nhà CS, và đây là những trường hợp duy nhất của quan hệ $in$ nhận giá trị đúng. Tương tự, phòng $r123$ và phòng $r023$ là một phần của tòa nhà CS, và không có mối quan hệ $part\_of$ nào khác nhận giá trị đúng trong diễn giải này.
:::

Mỗi số hạng không biến biểu thị một cá thể trong một diễn giải. Hằng số $c$ biểu thị cá thể $\phi(c)$ trong $I$.

Một nguyên tử không biến nhận giá trị $true$ hoặc $false$ trong một diễn giải. Nguyên tử $p(t_{1}, \ldots, t_{n})$ nhận giá trị $true$ trong diễn giải $I$ nếu:

$$
\pi(p)(\langle t_{1}^{\prime}, \ldots, t_{n}^{\prime} \rangle) = true
$$

trong đó $t_{i}^{\prime}$ là cá thể được biểu thị bởi số hạng $t_{i}$; và nhận giá trị $false$ trong trường hợp ngược lại.

::: example Ví dụ 15.6: Giá trị chân lý của các nguyên tử không biến
Nguyên tử `in(kim, r123)` nhận giá trị $true$ trong diễn giải của [Ví dụ 15.5](https://artint.info/3e/html/ArtInt3e.Ch15.S3.html#Ch15.Thmciexamplered5), bởi vì con người được biểu thị bởi $kim$ quả thực đang ở trong căn phòng được biểu thị bởi $r123$.

Tương tự, `person(kim)` nhận giá trị $true$, và `part_of(r123, cs_building)` cũng nhận giá trị $true$.

Ngược lại, các nguyên tử `in(cs_building, r123)` và `person(r123)` nhận giá trị $false$ trong diễn giải này.
:::

Các phép nối logic mang ý nghĩa giống hệt như trong [logic mệnh đề](https://artint.info/3e/html/ArtInt3e.Ch5.S1.html#SS2); xem bảng chân lý của các phép nối logic trong [Hình 5.1](https://artint.info/3e/html/ArtInt3e.Ch5.S1.html#Ch5.F1).

## 15.3.2 Diễn giải các biến logic

Để định nghĩa ngữ nghĩa của các công thức logic chứa biến, một **phép gán biến** (variable assignment), ký hiệu là $\rho$, là một hàm từ tập hợp các biến vào miền cá thể $D$. Do đó, một phép gán biến sẽ gán một phần tử của miền cho mỗi biến logic.

Cho trước một diễn giải $\langle D, \phi, \pi \rangle$ và một phép gán biến $\rho$, mỗi số hạng biểu thị một cá thể trong miền:
- Nếu số hạng là một hằng số, cá thể được xác định bởi $\phi$.
- Nếu số hạng là một biến logic, cá thể được xác định bởi $\rho$.

Cho trước một diễn giải và một phép gán biến cho toàn bộ các biến, mỗi nguyên tử nhận giá trị $true$ hoặc $false$ theo định nghĩa tương tự như đối với trường hợp không biến ở trên.

Ngữ nghĩa của các lượng từ được định nghĩa như sau:

- **Lượng từ với mọi**: Công thức lượng từ hóa với mọi $\forall X~p$ nhận giá trị $true$ trong một diễn giải nếu $p$ nhận giá trị $true$ với mọi phép gán biến của $X$ vào một cá thể trong miền $D$. Do đó, công thức $\forall X~p$ nhận giá trị $false$ trong một diễn giải bất cứ khi nào tồn tại một phép gán biến cho $X$ làm cho công thức $p$ nhận giá trị $false$. Công thức $p$ được gọi là **phạm vi** (scope) của biến $X$.
- **Lượng từ tồn tại**: Công thức lượng từ hóa tồn tại $\exists X~p$ nhận giá trị $true$ trong một diễn giải nếu $p$ nhận giá trị $true$ với ít nhất một phép gán biến của $X$ vào một cá thể trong miền $D$. Cá thể tồn tại này có thể phụ thuộc vào các biến được lượng từ hóa với mọi mà $\exists X~p$ nằm trong phạm vi của chúng:
  - Ví dụ: Trong $\forall Y~(\exists X~p)$, cá thể $X$ có thể phụ thuộc vào cá thể $Y$; đối với mọi số $Y$, luôn tồn tại một số $X$ sao cho $X = Y + 1$.
  - Trong $\exists X~(\forall Y~p)$, cá thể $X$ không thể phụ thuộc vào $Y$ vì $X$ không nằm trong phạm vi của $Y$; không tồn tại một số cố định $X$ sao cho với mọi số $Y$, $X = Y + 1$.

Một công thức chứa một biến không nằm trong phạm vi của lượng từ bao bọc nó được gọi là **công thức mở** (open formula). Công thức mở không có giá trị chân lý xác định vì không phải mọi biến đều được gán giá trị thông qua phép gán biến hoặc lượng từ.

::: example Ví dụ 15.7: Đánh giá chân lý của các công thức có lượng từ
Công thức:

<span class="logic-expression logic-block">∀ X ∀ Y (part_of(X, Y) ← in(X, Y))</span>

nhận giá trị $false$ trong diễn giải của [Ví dụ 15.5](https://artint.info/3e/html/ArtInt3e.Ch15.S3.html#Ch15.Thmciexamplered5), bởi vì dưới phép gán biến trong đó $X$ biểu thị Kim và $Y$ biểu thị phòng 123, mệnh đề $in(X, Y)$ nhận giá trị $true$ nhưng $part\_of(X, Y)$ nhận giá trị $false$.

Ngược lại, công thức:

<span class="logic-expression logic-block">∀ X ∀ Y ∀ Z (in(X, Y) ← part_of(Z, Y) ∧ in(X, Z))</span>

nhận giá trị $true$ trong diễn giải đó, bởi vì $in(X, Y)$ nhận giá trị $true$ trong mọi phép gán biến mà $part\_of(Z, Y) \wedge in(X, Z)$ nhận giá trị $true$.
:::

Khái niệm hệ quả logic được định nghĩa tương tự như trong [logic mệnh đề](https://artint.info/3e/html/ArtInt3e.Ch5.S1.html#SS2): Một câu $g$ là một **hệ quả logic** của cơ sở tri thức $KB$, ký hiệu là $KB \models g$, nếu $g$ nhận giá trị $true$ trong mọi mô hình của $KB$.

::: example Ví dụ 15.8: Kiểm tra hệ quả logic
Giả sử cơ sở tri thức $KB$ là hội của ba công thức:

1. `in(kim, r123).`
2. `part_of(r123, cs_building).`
3. <code class="logic-expression">∀ X ∀ Y ∀ Z (in(X, Y) ← part_of(Z, Y) ∧ in(X, Z))</code>

Diễn giải được xác định trong [Ví dụ 15.5](https://artint.info/3e/html/ArtInt3e.Ch15.S3.html#Ch15.Thmciexamplered5) là một mô hình của $KB$, bởi vì mỗi công thức trên đều nhận giá trị $true$ trong diễn giải đó.

Ta xem xét các khẳng định hệ quả logic:

- $KB \models in(kim, r123)$: Khẳng định này đúng, vì sự kiện này được phát biểu trực tiếp trong cơ sở tri thức. Nếu mọi công thức trong $KB$ đều đúng trong một diễn giải, thì $in(kim, r123)$ chắc chắn phải đúng trong diễn giải đó.
- $KB \not\models in(kim, r023)$: Khẳng định này đúng (tức $in(kim, r023)$ không phải là hệ quả logic), bởi vì diễn giải trong Ví dụ 15.5 là một mô hình của $KB$ mà trong đó $in(kim, r023)$ nhận giá trị $false$.
- <code class="logic-expression">KB ⊭ part_of(r023, cs_building)</code>: Khẳng định này đúng (không phải là hệ quả logic). Mặc dù $part\_of(r023, cs\_building)$ nhận giá trị $true$ trong diễn giải của Ví dụ 15.5, nhưng vẫn tồn tại một mô hình khác của $KB$ trong đó $part\_of(r023, cs\_building)$ nhận giá trị $false$. Cụ thể, một diễn giải tương tự như Ví dụ 15.5 nhưng gán:

  <span class="logic-expression logic-block">π(part_of)(⟨ φ(r023), φ(cs_building) ⟩) = false</span>

  vẫn là một mô hình hợp lệ của $KB$ mà trong đó $part\_of(r023, cs\_building)$ nhận giá trị $false$.
- $KB \models in(kim, cs\_building)$: Khẳng định này đúng. Nếu các công thức trong $KB$ đều nhận giá trị $true$ trong diễn giải $I$, thì $in(kim, cs\_building)$ bắt buộc phải nhận giá trị $true$ trong $I$, nếu không sẽ tồn tại một trường hợp cụ thể hóa của công thức thứ ba trong $KB$ nhận giá trị $false$ trong $I$ — mâu thuẫn với giả thiết $I$ là một mô hình của $KB$.
:::

### Góc nhìn của con người về ngữ nghĩa

Mô tả hình thức về ngữ nghĩa chưa giải thích đầy đủ vì sao ngữ nghĩa lại thú vị hoặc cách thức sử dụng ngữ nghĩa làm nền tảng để xây dựng các hệ thống thông minh. Phương pháp luận sử dụng ngữ nghĩa cho các chương trình logic mệnh đề có thể được mở rộng sang logic vị từ qua quy trình 5 bước:

- **Bước 1**: Chọn miền bài toán hoặc thế giới cần biểu diễn. Đây có thể là một khía cạnh của thế giới thực (ví dụ cấu trúc các khóa học và sinh viên tại một trường đại học, hoặc môi trường phòng thí nghiệm tại một thời điểm), một thế giới tưởng tượng (như thế giới xứ sở thần tiên của Alice, hoặc trạng thái mạch điện khi một công tắc bị hỏng), hoặc một thế giới trừu tượng (như thế giới tiền tệ, con số và tập hợp). Trong thế giới này, xác định miền $D$ là tập hợp tất cả các cá thể hoặc sự vật mà bạn muốn nhắc đến và suy luận. Đồng thời chọn các mối quan hệ cần biểu diễn.
- **Bước 2**: Gán các hằng số trong ngôn ngữ cho các cá thể trong thế giới mà bạn muốn đặt tên. Đối với mỗi phần tử của $D$ cần nhắc đến theo tên, hãy gán một hằng số trong ngôn ngữ. Ví dụ: Bạn có thể chọn tên `kim` để biểu thị một giáo sư cụ thể và tên `cs322` cho một khóa học nhập môn trí tuệ nhân tạo cụ thể. Mỗi tên gọi này biểu thị cho cá thể tương ứng trong thế giới.
- **Bước 3**: Đối với mỗi mối quan hệ muốn biểu diễn, hãy gán một ký hiệu vị từ trong ngôn ngữ. Mỗi ký hiệu vị từ $n$ ngôi biểu thị một hàm từ $D^{n}$ vào $\{true, false\}$, quy định tập con của $D^{n}$ mà mối quan hệ đó nhận giá trị đúng. Ví dụ: Ký hiệu vị từ `teaches` có hai đối số (một giảng viên và một khóa học) có thể tương ứng với quan hệ hai ngôi nhận giá trị đúng khi cá thể được biểu thị bởi đối số thứ nhất giảng dạy khóa học được biểu thị bởi đối số thứ hai. Sự liên kết giữa các ký hiệu và ý nghĩa của chúng tạo nên một **diễn giải dự định** (intended interpretation), xác định điều mà các ký hiệu được dự định biểu thị.
- **Bước 4**: Viết các công thức nhận giá trị đúng trong diễn giải dự định. Công việc này thường được gọi là tiên đề hóa miền bài toán (axiomatizing the domain), trong đó các công thức được đưa ra là các tiên đề của miền, hay chính là cơ sở tri thức. Ví dụ: Nếu người biểu thị bởi ký hiệu `kim` giảng dạy khóa học biểu thị bởi ký hiệu `cs322`, bạn có thể khẳng định công thức `teaches(kim, cs322)` là đúng trong diễn giải dự định. Không cần viết ra mọi điều đúng đắn; không cần phát biểu những gì đã được suy ra từ các tiên đề khác.
- **Bước 5**: Đặt các câu hỏi truy vấn về diễn giải dự định. Hệ thống sẽ đưa ra các câu trả lời mà bạn có thể diễn giải dựa trên ý nghĩa đã gán cho các ký hiệu.

Theo phương pháp luận này, người thiết kế cơ sở tri thức thực chất không cung cấp thông tin gì cho máy tính cho đến bước 4. Ba bước đầu tiên hoàn toàn diễn ra trong tâm trí của người thiết kế. Tất nhiên, người thiết kế nên ghi lại tài liệu về các phép biểu thị để người khác có thể hiểu cơ sở tri thức, để chính họ ghi nhớ phép biểu thị của từng ký hiệu, và để họ có thể kiểm tra tính chân lý của các công thức.

Bản thân thế giới không tự quy định các cá thể phải là gì:

::: example Ví dụ 15.9: Đa dạng trong sự khái niệm hóa
Trong một sự khái niệm hóa của miền bài toán, $pink$ (màu hồng) có thể là một ký hiệu vị từ một ngôi nhận giá trị đúng khi cá thể được biểu thị bởi đối số đó có màu hồng.

Trong một sự khái niệm hóa khác, $pink$ có thể là một cá thể đại diện cho màu hồng, và nó được dùng làm đối số thứ hai cho một vị từ hai ngôi $color$, diễn đạt rằng cá thể được biểu thị bởi đối số thứ nhất có màu sắc được biểu thị bởi đối số thứ hai.

Ngoài ra, người ta có thể muốn mô tả thế giới ở mức độ chi tiết mà các sắc độ khác nhau của màu đỏ không bị phân biệt, và do đó màu hồng không xuất hiện. Một người khác lại có thể mô tả thế giới chi tiết hơn, thấy rằng $pink$ là thuật ngữ quá chung chung, và sử dụng các thuật ngữ như $coral$ (màu san hô) và $salmon$ (màu hồng cá hồi).
:::

Khi các cá thể trong miền là những vật thể vật lý thực, thường rất khó để đưa ra phép biểu thị mà không chỉ trực tiếp vào cá thể đó. Khi cá thể là một thực thể trừu tượng — chẳng hạn một khóa học đại học hay khái niệm tình yêu — việc viết ra phép biểu thị gần như là bất khả thi. Tuy nhiên, điều này không hề cản trở hệ thống biểu diễn và suy luận về các khái niệm trừu tượng đó.

## Tài liệu tham khảo

1. Poole, D. L., & Mackworth, A. K. (2023). *Artificial Intelligence: Foundations of Computational Agents* (3rd ed.). Cambridge University Press. Nguồn trực tuyến: [https://artint.info/3e/html/ArtInt3e.Ch15.S3.html](https://artint.info/3e/html/ArtInt3e.Ch15.S3.html).
