---
course: ai-nen-tang-tac-tu
lecture: 15-ca-the-va-quan-he
section: topic
topic: 15-9-gia-dinh-tri-thuc-day-du
title: "15.9 Giả định tri thức đầy đủ"
description: "Giả định tri thức đầy đủ (CKA), dạng chuẩn và bao đóng Clark, phủ định như một sự thất bại (NAF) và xử lý biến tự do gây tắc nghẽn (floundering)."
---

Giả định tri thức đầy đủ (complete knowledge assumption), như đã thảo luận trong Chương 5, là giả định cho rằng bất kỳ phát biểu nào không tất suy từ cơ sở tri thức thì đều là sai. Giả định này cũng cho phép chứng minh bằng phương pháp phủ định như một sự thất bại (negation as failure — NAF).

Giả định tri thức đầy đủ đối với các chương trình logic có chứa biến và ký hiệu hàm đòi hỏi các tiên đề cho đẳng thức, phép đóng miền (domain closure), và một khái niệm tinh vi hơn về bao đóng (completion).

::: example Ví dụ 15.41: Giả định tri thức đầy đủ về tập sinh viên
Giả sử quan hệ $student$ được định nghĩa bởi các câu tuyển:

```prolog
student(huan).
student(manpreet).
student(karan).
```

Giả định tri thức đầy đủ sẽ phát biểu rằng ba người này là những sinh viên duy nhất:

<span class="logic-expression logic-block">student(X) ↔ X = huan ∨ X = manpreet ∨ X = karan</span>

Nghĩa là, nếu $X$ là $huan$, $manpreet$, hoặc $karan$, thì $X$ là một sinh viên, và nếu $X$ là một sinh viên thì $X$ bắt buộc phải là một trong ba người này. Cụ thể, $kim$ không phải là một sinh viên.

Để kết luận $\neg student(kim)$, hệ thống đòi hỏi phải chứng minh được:

<span class="logic-expression logic-block">kim ≠ huan ∧ kim ≠ manpreet ∧ kim ≠ karan</span>

Để dẫn xuất các bất đẳng thức này, ta bắt buộc phải sử dụng giả định tên duy nhất (UNA). Như vậy, giả định tri thức đầy đủ bao hàm cả giả định tên duy nhất.
:::

Dạng chuẩn Clark (Clark normal form) của câu tuyển:

$$
p(t_{1}, \ldots, t_{k}) \leftarrow B
$$

là câu tuyển có dạng:

<span class="logic-expression logic-block">p(V_1, …, V_k) ← ∃ W_1 … ∃ W_m V_1 = t_1 ∧ … ∧ V_k = t_k ∧ B</span>

trong đó $V_{1}, \ldots, V_{k}$ là $k$ biến mới không xuất hiện trong câu tuyển gốc, và $W_{1}, \ldots, W_{m}$ là các biến ban đầu trong câu tuyển. Ký hiệu "$\exists$" có nghĩa là "tồn tại". Khi câu tuyển là một câu tuyển nguyên tử (sự kiện), thân $B$ nhận giá trị $true$.

Giả sử toàn bộ các câu tuyển định nghĩa vị từ $p$ được đưa về dạng chuẩn Clark với cùng một tập hợp biến đối số mới được giới thiệu:

$$
\begin{aligned}
&p(V_{1}, \ldots, V_{k}) \leftarrow B_{1}, \\
&\vdots \\
&p(V_{1}, \ldots, V_{k}) \leftarrow B_{n},
\end{aligned}
$$

điều này tương đương với:

$$
p(V_{1}, \ldots, V_{k}) \leftarrow B_{1} \vee \ldots \vee B_{n}
$$

Phép kéo theo này tương đương logic với tập hợp các câu tuyển ban đầu.

Bao đóng Clark (Clark's completion) của vị từ $p$ là mệnh đề tương đương:

<span class="logic-expression logic-block">∀ V_1 … ∀ V_k p(V_1, …, V_k) ↔ B_1 ∨ … ∨ B_n</span>

trong đó phủ định như một sự thất bại ($\sim$) trong thân câu tuyển được thay thế bằng phủ định logic chuẩn ($\neg$). Bao đóng này khẳng định rằng $p(V_{1}, \ldots, V_{k})$ là đúng khi và chỉ khi có ít nhất một thân câu tuyển $B_{i}$ là đúng.

Bao đóng Clark của một cơ sở tri thức bao gồm bao đóng của mọi ký hiệu vị từ có mặt trong cơ sở tri thức đó.

::: example Ví dụ 15.42: Bao đóng Clark cho vị từ sinh viên
Đối với các câu tuyển:

```prolog
student(huan).
student(manpreet).
student(karan).
```

Dạng chuẩn Clark tương ứng là:

```prolog
student(V) :- V = huan.
student(V) :- V = manpreet.
student(V) :- V = karan.
```

tương đương với:

<span class="logic-expression logic-block">student(V) ← V = huan ∨ V = manpreet ∨ V = karan</span>

Bao đóng Clark của vị từ $student$ là:

<span class="logic-expression logic-block">∀ V student(V) ↔ V = huan ∨ V = manpreet ∨ V = karan</span>
:::

::: example Ví dụ 15.43: Dạng chuẩn và bao đóng Clark cho vị từ đệ quy
Xem xét định nghĩa đệ quy sau:

```prolog
passed_each([], St, MinPass).
passed_each([C | R], St, MinPass) :-
    passed(St, C, MinPass),
    passed_each(R, St, MinPass).
```

Ở dạng chuẩn Clark, sau khi đổi tên biến, định nghĩa này có thể được viết thành:

```prolog
passed_each(L, S, M) :- L = [].
passed_each(L, S, M) :-
    exists C, R: L = [C | R] /\ passed(S, C, M) /\ passed_each(R, S, M).
```

Bao đóng Clark của $passed\_each$ là:

<span class="logic-expression logic-block">∀ L ∀ S ∀ M passed_each(L, S, M) ↔ &#10;&#10;  L = [ ] ∨ ∃ C ∃ R (L = [C | R] ∧ passed(S, C, M) ∧ passed_each(R, S, M))</span>
:::

Dưới giả định tri thức đầy đủ, các quan hệ không thể định nghĩa được chỉ bằng các câu tuyển xác định nay đã có thể định nghĩa được.

::: example Ví dụ 15.44: Định nghĩa quan hệ khóa học rỗng bằng phủ định
Giả sử ta được cung cấp một cơ sở dữ liệu gồm $course(C)$ vốn đúng nếu $C$ là một khóa học, và $enrolled(S, C)$ có nghĩa là sinh viên $S$ đăng ký tham gia khóa học $C$. Nếu không có giả định tri thức đầy đủ, ta không thể định nghĩa được vị từ $empty\_course(C)$, vốn đúng nếu không có sinh viên nào đăng ký khóa học $C$. Lý do là vì luôn tồn tại một mô hình của cơ sở tri thức trong đó mọi khóa học đều có người đăng ký.

Sử dụng phủ định như một sự thất bại, $empty\_course(C)$ có thể được định nghĩa bằng:

```prolog
empty_course(C) :-
    course(C),
    ~has_enrollment(C).

has_enrollment(C) :-
    enrolled(S, C).
```

Bao đóng Clark của hệ luật này là:

<span class="logic-expression logic-block">∀ C empty_course(C) ↔ course(C) ∧ ¬ has_enrollment(C)</span>

<span class="logic-expression logic-block">∀ C has_enrollment(C) ↔ ∃ S enrolled(S, C)</span>

Như một lời lưu ý cẩn trọng, ta cần hết sức thận trọng khi đưa các biến tự do vào bên trong phép phủ định thất bại. Chúng thường không mang ý nghĩa như người ta thoạt nghĩ. Vị từ $has\_enrollment$ được đưa vào trong ví dụ trên chính là nhằm tránh việc xuất hiện biến tự do bên trong toán tử phủ định thất bại.
:::

## 15.9.1 Thủ tục chứng minh với giả định tri thức đầy đủ

Thủ tục chứng minh từ trên xuống đối với phép phủ định thất bại có chứa biến và ký hiệu hàm rất giống với thủ tục chứng minh từ trên xuống cho phủ định thất bại trong logic mệnh đề. Tương tự như đối với giả định tên duy nhất, một vấn đề nảy sinh khi có các biến tự do nằm bên trong các mục tiêu bị phủ định.

::: example Ví dụ 15.45: Rủi ro khi có biến tự do trong mục tiêu phủ định
Xét các câu tuyển sau:

```prolog
p(X) :- ~q(X), r(X).
q(a).
q(b).
r(d).
```

Theo ngữ nghĩa, chỉ có duy nhất một câu trả lời cho truy vấn $\text{ask } p(X)$, đó là $X = d$. Vì $r(d)$ tất suy, nên $\sim q(d)$ cũng tất suy, và do đó $p(d)$ tất suy logic từ cơ sở tri thức.

Khi thủ tục chứng minh từ trên xuống bắt gặp $\sim q(X)$, nó không được cố gắng chứng minh mục tiêu con $q(X)$, vốn sẽ thành công (với phép thế $\{X/a\}$). Nếu làm như vậy, mục tiêu $p(X)$ sẽ bị coi là thất bại, trong khi đáng lẽ nó phải thành công với $X = d$. Do đó, thủ tục chứng minh sẽ không đầy đủ. Lưu ý rằng, nếu cơ sở tri thức có chứa câu tuyển $s(X) \leftarrow \sim q(X)$, thì sự thất bại của $q(X)$ đồng nghĩa với việc $s(X)$ thành công. Như vậy, trong bối cảnh phủ định thất bại, tính không đầy đủ sẽ dẫn thẳng tới tính không đúng đắn (unsoundness).

Tương tự như với giả định tên duy nhất, một thủ tục chứng minh đúng đắn phải trì hoãn mục tiêu con bị phủ định cho đến khi biến tự do được liên kết giá trị.
:::

Một thủ tục từ trên xuống phức tạp hơn là cần thiết khi có các lời gọi tới phép phủ định thất bại chứa biến tự do:

- Các mục tiêu phủ định thất bại chứa biến tự do không được phép chọn trong thủ tục chứng minh phủ định thất bại cho đến khi các biến đó được gán giá trị cụ thể.
- Nếu các biến không bao giờ được gán giá trị, mục tiêu đó rơi vào trạng thái tắc nghẽn (flounders). Trong trường hợp này, ta không thể kết luận được điều gì chắc chắn về mục tiêu. Ví dụ sau đây chỉ ra rằng ta cần làm một điều gì đó tinh vi hơn đối với trường hợp các mục tiêu bị tắc nghẽn.

::: example Ví dụ 15.46: Hiện tượng tắc nghẽn và phân tích trường hợp
Xét các câu tuyển sau:

```prolog
p(X) :- ~q(X).
q(X) :- ~r(X).
r(a).
```

và câu truy vấn:

$$
\text{ask } p(X).
$$

Bao đóng của cơ sở tri thức này là:

$$
p(X) \leftrightarrow \neg q(X)
$$

$$
q(X) \leftrightarrow \neg r(X)
$$

$$
r(X) \leftrightarrow X = a
$$

Thay thế $X = a$ cho $r$, ta được $q(X) \leftrightarrow \neg(X = a)$, và từ đó suy ra $p(X) \leftrightarrow X = a$.

Như vậy, tồn tại một câu trả lời duy nhất, cụ thể là $X = a$. Tuy nhiên, việc đơn thuần trì hoãn mục tiêu sẽ không giúp tìm ra câu trả lời này. Một thủ tục chứng minh hoàn chỉnh cần phải phân tích các trường hợp mà mục tiêu thất bại để dẫn xuất câu trả lời này. Tuy nhiên, một thủ tục như vậy vượt ra ngoài phạm vi cuốn sách này.
:::

## Tài liệu tham khảo

- Poole, D. L., & Mackworth, A. K. (2023). *Artificial Intelligence: Foundations of Computational Agents* (3rd ed.). Cambridge University Press. Bản điện tử: [https://artint.info/3e/html/ArtInt3e.Ch15.S9.html](https://artint.info/3e/html/ArtInt3e.Ch15.S9.html).
- Clark, K. L. (1978). Negation as failure. In H. Gallaire & J. Minker (Eds.), *Logic and Data Bases* (pp. 293–322). Plenum Press.
