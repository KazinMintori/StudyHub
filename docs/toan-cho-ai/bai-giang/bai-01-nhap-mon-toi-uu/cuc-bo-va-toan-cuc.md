---
course: toan-cho-ai
lecture: bai-01-nhap-mon-toi-uu
topic: cuc-bo-va-toan-cuc
section: topic
title: "Cực tiểu cục bộ và cực tiểu toàn cục"
description: "Định nghĩa bài toán tối ưu lồi ở dạng chuẩn và vì sao ràng buộc đẳng thức phải affine, tập nghiệm và tập ε-tối ưu lồi, định lý cực tiểu cục bộ là cực tiểu toàn cục cùng lời chứng minh hình học, vai trò riêng của tính lồi của hàm và của miền, bài toán tựa lồi và ý nghĩa đối với thuật toán."
---

Đến đây, mọi mảnh ghép đã đủ: tập lồi ở phần II, hàm lồi ở phần III. Phần cuối của chương ráp chúng lại thành **bài toán tối ưu lồi**, và trả lời câu hỏi đã đặt ra ngay từ chủ đề đầu tiên: vì sao người ta dành cả một môn học cho lớp bài toán này?

Câu trả lời ngắn gọn nằm ở một định lý chỉ dài vài dòng: trong một bài toán tối ưu lồi, mọi điểm cực tiểu cục bộ đều là cực tiểu toàn cục. Một thuật toán chỉ nhìn được xung quanh điểm đang đứng, và với bài toán lồi, chừng ấy là đủ. Ta sẽ phát biểu chính xác bài toán tối ưu lồi, chứng minh định lý, rồi xem từng giả thiết của nó đóng vai trò gì.

## 1. Bài toán tối ưu lồi ở dạng chuẩn

Sách định nghĩa một **bài toán tối ưu lồi** là bài toán có dạng

$$
\begin{aligned}
\text{cực tiểu} \quad & f_0(x) \\
\text{với điều kiện} \quad & f_i(x) \le 0, \quad i = 1, \dots, m, \\
& a_i^T x = b_i, \quad i = 1, \dots, p,
\end{aligned}
$$

trong đó $f_0, f_1, \dots, f_m$ là các hàm lồi. So với một bài toán tối ưu tổng quát, có ba yêu cầu thêm: hàm mục tiêu lồi, các hàm ràng buộc bất đẳng thức lồi, và các ràng buộc đẳng thức **affine**.

Ba yêu cầu này bảo đảm miền khả thi là một tập lồi. Miền khả thi là giao của miền xác định chung, các tập mức dưới $\{x : f_i(x) \le 0\}$ của những hàm lồi, và các siêu phẳng $\{x : a_i^T x = b_i\}$. Mỗi tập đều lồi theo những gì đã học, và giao của các tập lồi là tập lồi. Vậy bài toán tối ưu lồi là bài toán **cực tiểu một hàm lồi trên một tập lồi**, với tập lồi đó được mô tả theo một cách cụ thể.

**Vì sao đẳng thức phải affine.** Một ràng buộc đẳng thức $h(x) = 0$ tương đương với hai bất đẳng thức $h(x) \le 0$ và $-h(x) \le 0$. Muốn cả hai đều là ràng buộc lồi, ta cần $h$ vừa lồi vừa lõm, tức $h$ affine. Một đẳng thức phi tuyến thường cho tập không lồi. Ràng buộc $x_1^2 + x_2^2 = 1$ cho đường tròn, không chứa trung điểm $(0, 0)$ của hai điểm $(1, 0)$ và $(-1, 0)$. Thay nó bằng $x_1^2 + x_2^2 \le 1$ thì được cả hình tròn, lồi.

**Một chi tiết về cách mô tả.** Sách cẩn thận phân biệt giữa "cực tiểu hàm lồi trên tập lồi" và "bài toán lồi ở dạng chuẩn". Ví dụ của sách: cực tiểu $x_1^2 + x_2^2$ với $x_1/(1 + x_2^2) \le 0$ và $(x_1 + x_2)^2 = 0$. Miền khả thi $\{x : x_1 \le 0,\ x_1 + x_2 = 0\}$ là tập lồi, nhưng bài toán không ở dạng chuẩn, vì hàm ràng buộc thứ nhất không lồi và hàm đẳng thức không affine. Viết lại thành $x_1 \le 0$ và $x_1 + x_2 = 0$, ta được một bài toán lồi ở dạng chuẩn, tương đương với bài toán ban đầu. Trong thực hành, việc tìm một mô tả đúng dạng như vậy thường không khó, nhưng nó là việc phải làm: các bộ giải chỉ nhận bài toán ở dạng chuẩn.

**Cực đại hàm lõm.** Bài toán cực đại một hàm lõm $f_0$ với cùng loại ràng buộc cũng được gọi là bài toán lồi, vì nó tương đương với cực tiểu hàm lồi $-f_0$.

## 2. Tập nghiệm của bài toán lồi

Gọi $p^\star$ là giá trị tối ưu. Tập nghiệm tối ưu là $\{x \text{ khả thi} : f_0(x) \le p^\star\}$, giao của miền khả thi với một tập mức dưới của $f_0$. Cả hai đều lồi, nên **tập nghiệm tối ưu của một bài toán lồi là tập lồi**. Lập luận y hệt cho tập các điểm $\varepsilon$-tối ưu $\{x \text{ khả thi} : f_0(x) \le p^\star + \varepsilon\}$.

Hệ quả cụ thể: một bài toán lồi có thể không có nghiệm, có đúng một nghiệm, hoặc có vô số nghiệm, nhưng **không bao giờ có đúng hai nghiệm**, hay bất kỳ số hữu hạn nào lớn hơn 1. Nếu có hai nghiệm thì cả đoạn thẳng nối chúng đều là nghiệm. Bạn đã gặp điều này hai lần. Ở chủ đề về hai lớp bài toán kinh điển, quy hoạch tuyến tính có thể đạt tối ưu trên cả một cạnh của đa giác khả thi. Ở chủ đề điều kiện bậc hai, bình phương tối thiểu với hai đặc trưng cộng tuyến có cả một đường thẳng nghiệm. Nếu hàm mục tiêu lồi nghiêm ngặt, tập nghiệm có nhiều nhất một điểm.

Ngược lại, hàm $0.25x^4 - x^2 + 0.3x$ có hai điểm cực tiểu cục bộ tách rời, tại $x \approx -1.484$ và $x \approx 1.332$. Một hàm lồi không thể có hình dạng như vậy.

## 3. Cực tiểu cục bộ là cực tiểu toàn cục

> **Định nghĩa.** Điểm khả thi $x$ là **cực tiểu cục bộ** nếu có $R > 0$ sao cho $f_0(x) \le f_0(z)$ với mọi điểm khả thi $z$ thỏa $\|z - x\|_2 \le R$.

> **Định lý.** Trong một bài toán tối ưu lồi, mọi điểm cực tiểu cục bộ đều là cực tiểu toàn cục.

**Chứng minh.** Giả sử $x$ là cực tiểu cục bộ với bán kính $R$, nhưng có một điểm khả thi $y$ với $f_0(y) < f_0(x)$. Điểm $y$ phải nằm xa $x$ hơn $R$, vì trong bán kính $R$ không có điểm nào tốt hơn $x$. Đi từ $x$ về phía $y$ một đoạn bằng $R/2$, tức lấy

$$
z = (1 - \theta)\, x + \theta\, y, \qquad \theta = \frac{R}{2\|y - x\|_2} \in (0, \tfrac12).
$$

Hai tính lồi lần lượt được dùng ở hai bước:

1. **Miền khả thi lồi**, nên $z$, nằm trên đoạn nối hai điểm khả thi $x$ và $y$, cũng khả thi. Vì $\|z - x\|_2 = R/2 < R$, điểm $z$ nằm trong lân cận của $x$.
2. **Hàm mục tiêu lồi**, nên $f_0(z) \le (1 - \theta) f_0(x) + \theta f_0(y)$. Vì $f_0(y) < f_0(x)$ và $\theta > 0$, vế phải nhỏ hơn hẳn $f_0(x)$.

Vậy $z$ là một điểm khả thi trong lân cận của $x$ với $f_0(z) < f_0(x)$, trái với giả thiết $x$ là cực tiểu cục bộ. Không thể có $y$ như vậy, và $x$ là cực tiểu toàn cục. $\square$

Về hình ảnh, nếu ở rất xa có một điểm tốt hơn, thì dây cung từ $x$ tới điểm đó đi xuống ngay từ đầu, và đồ thị hàm lồi nằm dưới dây cung, nên ngay sát $x$ đã có điểm tốt hơn. Một hàm lồi không thể "giấu" một thung lũng sâu sau một ngọn đồi.

<LocalGlobalLab />

Mô phỏng cho bạn xem từng giả thiết hỏng ra sao. Với hàm hai giếng $0.25x^4 - x^2 + 0.3x$ và $x$ ở đáy giếng phải gần $1.332$, điểm $z$ của lời chứng minh vẫn khả thi, nhưng đồ thị tại $z$ nằm **trên** dây cung, nên bước 2 sụp đổ. Với hàm lồi $\tfrac12 (x - 1)^2$ nhưng miền khả thi gồm hai đoạn rời nhau, điểm $x = -1.2$ ở mép đoạn trái là cực tiểu cục bộ không toàn cục. Lần này điểm $z$ rơi vào khoảng trống giữa hai đoạn, nên bước 1 sụp đổ. Định lý cần **cả hai** loại tính lồi, của hàm và của miền.

## 4. Ý nghĩa đối với thuật toán

Mọi phương pháp tối ưu lặp, từ phương pháp gradient tới phương pháp Newton, đều chỉ dùng thông tin trong một lân cận nhỏ của điểm đang đứng: giá trị, gradient, có khi thêm Hessian. Với bài toán không lồi, một phương pháp như vậy có thể dừng ở một cực tiểu cục bộ tồi, ở một điểm yên ngựa, và kết quả phụ thuộc vào điểm xuất phát. Với bài toán lồi, ba nỗi lo đó biến mất cùng lúc:

- Mọi cực tiểu cục bộ là toàn cục, nên không có cực tiểu cục bộ "tồi".
- Với hàm khả vi, điểm dừng là cực tiểu toàn cục (chủ đề điều kiện bậc nhất), nên không có điểm yên ngựa nào để mắc kẹt.
- Tập nghiệm lồi, nên các điểm xuất phát khác nhau có thể dẫn tới các nghiệm khác nhau, nhưng tất cả đều tối ưu như nhau.

Đây là lý do một bài toán đã được nhận ra là lồi được xem gần như "đã giải xong": việc còn lại là chọn một bộ giải đủ tốt. Còn với mạng nơ-ron, hàm mất mát không lồi, và câu hỏi "vì sao phương pháp gradient vẫn tìm được nghiệm tốt" là một hướng nghiên cứu còn mở, không có lời đáp gọn như định lý trên.

**Tựa lồi chưa đủ.** Với bài toán tựa lồi, tức hàm mục tiêu chỉ có các tập mức dưới lồi, định lý không còn đúng (§4.2.5). Hàm $f(x) = \min\{\max\{x, 0\},\ 1\}$ bằng 0 khi $x \le 0$, tăng tuyến tính trên $[0, 1]$, và bằng 1 khi $x \ge 1$. Nó đơn điệu nên tựa lồi. Điểm $x = 2$ nằm trên đoạn phẳng ở độ cao 1, nên là cực tiểu cục bộ với mọi $R < 1$, trong khi giá trị nhỏ nhất là 0. Lời chứng minh ở mục 3 hỏng vì tựa lồi không cho bất đẳng thức dây cung, chỉ cho $f(z) \le \max\{f(x), f(y)\}$, mà như vậy thì không đủ để $f(z) < f(x)$.

## 5. Những câu hỏi để đào sâu

**Câu 1.** Lời chứng minh chọn $z$ cách $x$ đúng $R/2$. Nếu chọn $z$ cách $x$ đúng $R$ thì có còn đúng không? Còn chọn $z = y$ thì sao?

<details><summary>Xem lời giải thích</summary>

Chọn khoảng cách đúng $R$ vẫn được, vì định nghĩa cực tiểu cục bộ ở đây dùng điều kiện $\|z - x\|_2 \le R$, có cả biên. Sách chọn $R/2$ cho an toàn, để $z$ nằm hẳn trong lân cận dù định nghĩa dùng bất đẳng thức chặt hay không. Còn chọn $z = y$ thì vô dụng: $y$ ở ngoài lân cận, nên $f_0(y) < f_0(x)$ không mâu thuẫn gì với tính tối ưu cục bộ. Toàn bộ sức mạnh của lời chứng minh nằm ở chỗ tính lồi **kéo thông tin từ $y$ ở xa về một điểm $z$ ở gần**.

</details>

**Câu 2.** Một bài toán lồi có thể có đúng hai nghiệm tối ưu không? Một bài toán không lồi thì sao?

<details><summary>Xem lời giải thích</summary>

Bài toán lồi thì không: tập nghiệm lồi, nên nếu chứa hai điểm thì chứa cả đoạn nối chúng, tức vô số điểm. Bài toán không lồi thì có thể. Hàm $x^4 + y^4 - 4xy$ ở bài tập của chủ đề điều kiện bậc hai có đúng hai cực tiểu toàn cục $(1, 1)$ và $(-1, -1)$, còn trung điểm của chúng có giá trị cao hơn hẳn. Hiện tượng "các nghiệm đối xứng tách rời" như vậy là dấu hiệu điển hình của bài toán không lồi, và nó xuất hiện tự nhiên trong mạng nơ-ron, như chủ đề cuối của chương sẽ chỉ ra.

</details>

**Câu 3.** Bài toán cực tiểu $x_1 + x_2$ với $x_1^2 + x_2^2 = 1$ không lồi. Thay ràng buộc bằng $x_1^2 + x_2^2 \le 1$, ta được một bài toán lồi. Hai bài toán có cùng nghiệm không? Điều đó có luôn đúng khi nới đẳng thức thành bất đẳng thức?

<details><summary>Xem lời giải thích</summary>

Lần này cùng nghiệm. Bài toán nới lỏng cực tiểu một hàm tuyến tính trên hình tròn, và nghiệm nằm trên biên tại $(-1/\sqrt2,\ -1/\sqrt2)$ với giá trị $-\sqrt2$, điểm này cũng thỏa đẳng thức. Nhưng điều đó không luôn đúng. Nếu hàm mục tiêu là $(x_1 - 0.1)^2 + x_2^2$, bài toán nới lỏng có nghiệm $(0.1, 0)$ nằm hẳn bên trong hình tròn, không thỏa đẳng thức, trong khi bài toán gốc có nghiệm $(1, 0)$. Nới lỏng chỉ "chặt" khi hàm mục tiêu tự đẩy nghiệm ra biên.

</details>

**Câu 4.** Trong bài toán lồi, phương pháp gradient xuất phát từ hai điểm khác nhau có thể hội tụ về hai điểm khác nhau không? Điều đó có mâu thuẫn với định lý không?

<details><summary>Xem lời giải thích</summary>

Có thể, khi tập nghiệm có nhiều hơn một điểm. Với bình phương tối thiểu có hai đặc trưng cộng tuyến ở chủ đề điều kiện bậc hai, phương pháp gradient xuất phát từ $w^{(0)}$ chỉ di chuyển trong tập $w^{(0)} + \mathcal{R}(A^T)$, như chủ đề về tập affine đã chỉ ra, nên điểm hội tụ phụ thuộc vào điểm xuất phát. Không có mâu thuẫn nào: mọi điểm hội tụ đều tối ưu, chúng chỉ khác nhau về vị trí chứ không khác nhau về giá trị hàm mục tiêu.

</details>

## 6. Bài tập tự luyện

::: exercise 1. Bài toán nào là bài toán lồi ở dạng chuẩn?
Với mỗi bài toán, cho biết nó có phải bài toán lồi ở dạng chuẩn không. Nếu không, có viết lại được thành một bài toán lồi tương đương không? (a) Cực tiểu $x_1^2 + x_2^2$ với $x_1 + x_2 \ge 1$. (b) Cực tiểu $x_1 + x_2$ với $x_1^2 + x_2^2 = 1$. (c) Cực đại $\log x_1 + \log x_2$ với $x_1 + 2x_2 \le 4$. (d) Cực tiểu $x_1 x_2$ với $-1 \le x_1 \le 1$, $-1 \le x_2 \le 1$.
:::

::: solution
(a) Có, sau khi viết ràng buộc thành $1 - x_1 - x_2 \le 0$, một hàm affine. Hàm mục tiêu lồi. (b) Không, vì ràng buộc đẳng thức không affine và miền khả thi là đường tròn, không lồi. Bài toán gốc không có dạng lồi tương đương theo nghĩa của sách, nhưng như Câu 3 cho thấy, nó có cùng nghiệm với bài toán nới lỏng lồi khi thay "=" bằng "≤". (c) Có, đây là bài toán cực đại một hàm lõm với ràng buộc affine, nên là bài toán lồi. Nghiệm là $x = (2, 1)$ với giá trị $\log 2$: tại đó $\nabla(\log x_1 + \log x_2) = (1/2,\ 1)$ tỉ lệ với $(1, 2)$, pháp tuyến của ràng buộc. (d) Không, vì $x_1 x_2$ không lồi: Hessian $\begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}$ có một trị riêng âm. Miền khả thi lồi, nhưng chừng đó không đủ.
:::

::: exercise 2. Tập nghiệm lồi
Chứng minh trực tiếp rằng nếu $x$ và $y$ đều là nghiệm tối ưu của một bài toán lồi, thì mọi điểm $\theta x + (1 - \theta) y$ với $0 \le \theta \le 1$ cũng là nghiệm tối ưu.
:::

::: solution
Gọi $p^\star$ là giá trị tối ưu, nên $f_0(x) = f_0(y) = p^\star$. Điểm $z = \theta x + (1 - \theta) y$ khả thi vì miền khả thi lồi. Hàm mục tiêu lồi cho $f_0(z) \le \theta p^\star + (1 - \theta) p^\star = p^\star$. Mặt khác $f_0(z) \ge p^\star$ vì $z$ khả thi và $p^\star$ là giá trị nhỏ nhất. Vậy $f_0(z) = p^\star$, và $z$ là nghiệm tối ưu.
:::

::: exercise 3. Hai giếng
Cho $f(x) = 0.25x^4 - x^2 + 0.3x$ trên $\mathbb{R}$. (a) Tìm các điểm dừng bằng số và phân loại chúng. (b) Điểm nào là cực tiểu toàn cục? (c) Chỉ ra một dây cung mà đồ thị vượt lên trên, để thấy vì sao định lý không áp dụng được.
:::

::: solution
(a) $f'(x) = x^3 - 2x + 0.3 = 0$ có ba nghiệm xấp xỉ $-1.484$, $0.152$ và $1.332$. Với $f''(x) = 3x^2 - 2$, ta có $f'' \approx 4.61$, $-1.93$ và $3.32$ tại ba điểm đó, nên đó lần lượt là cực tiểu cục bộ, cực đại cục bộ, và cực tiểu cục bộ. (b) $f(-1.484) \approx -1.435$ và $f(1.332) \approx -0.588$. Vì $f \to \infty$ khi $|x| \to \infty$, cực tiểu toàn cục tồn tại và là một trong hai điểm, nên là $x \approx -1.484$. Điểm $x \approx 1.332$ là cực tiểu cục bộ không toàn cục. (c) Dây cung nối hai cực tiểu có độ cao từ $-1.435$ tới $-0.588$, trong khi tại $x = 0$ nằm giữa chúng, $f(0) = 0$ cao hơn cả hai đầu mút. Đồ thị vượt lên trên dây cung, nên $f$ không lồi.
:::

## Tóm tắt

Bài toán tối ưu lồi ở dạng chuẩn có hàm mục tiêu lồi, các ràng buộc bất đẳng thức là hàm lồi, và các ràng buộc đẳng thức affine. Khi đó miền khả thi lồi, tập nghiệm tối ưu và tập $\varepsilon$-tối ưu cũng lồi, nên bài toán có không, một, hoặc vô số nghiệm, và nghiệm duy nhất nếu hàm mục tiêu lồi nghiêm ngặt.

Định lý trung tâm: mọi cực tiểu cục bộ của bài toán lồi là cực tiểu toàn cục. Lời chứng minh dùng tính lồi của miền để giữ một điểm trung gian khả thi, và tính lồi của hàm để điểm đó tốt hơn. Thiếu một trong hai, định lý có thể sai, và với bài toán tựa lồi nó cũng sai. Vì vậy với bài toán lồi, một thuật toán chỉ nhìn cục bộ vẫn tìm được nghiệm toàn cục.

## Nguồn và đọc thêm

- S. Boyd, L. Vandenberghe, *Convex Optimization*, §4.2.1–4.2.2 (tr. 136–138), các bài toán (4.15)–(4.18). Bài toán tựa lồi ở §4.2.5.
- Mô phỏng lời chứng minh, ví dụ hàm hai giếng, ví dụ miền khả thi gồm hai đoạn, ví dụ hàm tựa lồi có đoạn phẳng, các câu hỏi và bài tập do người soạn bổ sung. Mọi con số đã được tính lại bằng chương trình.
