---
course: toan-cho-ai
lecture: bai-01-nhap-mon-toi-uu
topic: cuc-bo-va-toan-cuc
section: topic
title: "Cực tiểu cục bộ và cực tiểu toàn cục"
description: "Định nghĩa bài toán tối ưu lồi ở dạng chuẩn và vì sao ràng buộc đẳng thức phải affine, tập nghiệm và tập ε-tối ưu lồi, định lý cực tiểu cục bộ là cực tiểu toàn cục cùng lời chứng minh hình học, vai trò riêng của tính lồi của hàm và của miền, bài toán tựa lồi và ý nghĩa đối với thuật toán."
---

Đến đây, mọi mảnh ghép đã đủ: Tập lồi ở phần II, hàm lồi ở phần III. Phần cuối của chương ráp chúng lại thành **bài toán tối ưu lồi**, và trả lời câu hỏi đã đặt ra ngay từ chủ đề đầu tiên: Vì sao người ta dành trọn vẹn một môn học cho họ bài toán tối ưu này?

Câu trả lời ngắn gọn nằm ở một định lý chỉ dài vài dòng: Trong một bài toán tối ưu lồi, mọi điểm cực tiểu cục bộ đều là cực tiểu toàn cục. Một thuật toán gradient hay tìm kiếm cục bộ chỉ khai thác thông tin vi phân trong một lân cận hẹp của điểm hiện tại; và đối với bài toán tối ưu lồi, thông tin cục bộ ấy là hoàn toàn đủ để dẫn hướng tới nghiệm tối ưu toàn cục. Ta sẽ phát biểu chính xác bài toán tối ưu lồi, chứng minh định lý, rồi xem từng giả thiết của nó đóng vai trò gì.

## 1. Bài toán tối ưu lồi ở dạng chuẩn

Ta định nghĩa một **bài toán tối ưu lồi ở dạng chuẩn** là bài toán có dạng

$$
\begin{aligned}
\text{cực tiểu} \quad & f_0(x) \\
\text{với điều kiện} \quad & f_i(x) \le 0, \quad i = 1, \dots, m, \\
& a_i^T x = b_i, \quad i = 1, \dots, p,
\end{aligned}
$$

trong đó $f_0, f_1, \dots, f_m$ là các hàm lồi, và các ràng buộc đẳng thức là các hàm affine với $a_i^T x = a_{i1} x_1 + a_{i2} x_2 + \dots + a_{in} x_n = b_i$. So với một bài toán tối ưu tổng quát, có ba yêu cầu cốt lõi: Hàm mục tiêu lồi, các hàm ràng buộc bất đẳng thức lồi, và các ràng buộc đẳng thức bắt buộc phải là **affine**.

Ba yêu cầu này bảo đảm miền khả thi là một tập lồi. Miền khả thi là giao của miền xác định chung, các tập mức dưới $\{x : f_i(x) \le 0\}$ của những hàm lồi, và các siêu phẳng $\{x : a_i^T x = b_i\}$. Mỗi tập đều lồi theo các tính chất hình học cơ bản, và giao của các tập lồi luôn là một tập lồi. Như vậy, bài toán tối ưu lồi chính là bài toán **cực tiểu một hàm lồi trên một tập lồi**, với tập lồi đó được mô tả một cách tường minh qua các ràng buộc.

**Vì sao đẳng thức phải affine.** Một ràng buộc đẳng thức $h(x) = 0$ tương đương với hai bất đẳng thức đồng thời $h(x) \le 0$ và $-h(x) \le 0$. Muốn cả hai đều là ràng buộc lồi, ta cần $h$ vừa lồi vừa lõm, kéo theo $h$ bắt buộc phải là hàm affine. Một đẳng thức phi tuyến nói chung sẽ tạo ra miền khả thi không lồi. Xét ràng buộc $x_1^2 + x_2^2 = 1$, tập nghiệm là đường tròn đơn vị, hoàn toàn không chứa trung điểm $(0, 0)$ của hai điểm đối xứng $(1, 0)$ và $(-1, 0)$. Khi thay thế bằng bất đẳng thức $x_1^2 + x_2^2 \le 1$, ta thu được hình tròn đặc, vốn là một tập lồi.

**Phân biệt bài toán lồi tổng quát và bài toán lồi dạng chuẩn.** Ta cần lưu ý sự khác biệt giữa khái niệm bài toán "cực tiểu hàm lồi trên tập lồi" và "bài toán tối ưu lồi ở dạng chuẩn". Xét ví dụ: Cực tiểu $x_1^2 + x_2^2$ với các ràng buộc $x_1/(1 + x_2^2) \le 0$ và $(x_1 + x_2)^2 = 0$. Miền khả thi $\{x : x_1 \le 0,\ x_1 + x_2 = 0\}$ thực chất là một tập lồi, nhưng cách biểu diễn ban đầu chưa ở dạng chuẩn vì hàm ràng buộc thứ nhất không lồi và hàm đẳng thức không affine. Khi viết lại thành $x_1 \le 0$ và $x_1 + x_2 = 0$, ta thu được một bài toán tối ưu lồi ở dạng chuẩn hoàn toàn tương đương với bài toán ban đầu. Trong thực tế tính toán, việc đưa bài toán về đúng dạng chuẩn là bước tiên quyết, bởi các thuật toán tối ưu và bộ giải số học (solver) chỉ chấp nhận dữ liệu đầu vào ở dạng chuẩn.

**Cực đại hàm lõm.** Bài toán cực đại một hàm lõm $f_0$ với cùng loại ràng buộc cũng được gọi là bài toán lồi, vì nó tương đương với cực tiểu hàm lồi $-f_0$.

## 2. Tập nghiệm của bài toán lồi

Gọi $p^\star$ là giá trị tối ưu. Tập nghiệm tối ưu là $\{x \text{ khả thi} : f_0(x) \le p^\star\}$, giao của miền khả thi với một tập mức dưới của $f_0$. Cả hai đều lồi, nên **tập nghiệm tối ưu của một bài toán lồi là tập lồi**. Lập luận y hệt cho tập các điểm $\varepsilon$-tối ưu $\{x \text{ khả thi} : f_0(x) \le p^\star + \varepsilon\}$.

Hệ quả cụ thể: Một bài toán lồi có thể không có nghiệm, có đúng một nghiệm, hoặc có vô số nghiệm, nhưng **không bao giờ có đúng hai nghiệm**, hay bất kỳ số hữu hạn nào lớn hơn 1. Nếu có hai nghiệm thì cả đoạn thẳng nối chúng đều là nghiệm. Hiện tượng này đã xuất hiện hai lần trong các bài trước: Ở chủ đề về hai dạng bài toán kinh điển, quy hoạch tuyến tính có thể đạt tối ưu trên cả một cạnh của đa giác khả thi. Ở chủ đề điều kiện bậc hai, bình phương tối thiểu với hai đặc trưng cộng tuyến có cả một đường thẳng nghiệm. Nếu hàm mục tiêu lồi nghiêm ngặt, tập nghiệm có nhiều nhất một điểm.

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

Mô phỏng trực quan minh họa cơ chế vi phạm khi từng giả thiết bị phá vỡ. Với hàm hai giếng $0.25x^4 - x^2 + 0.3x$ và $x$ ở đáy giếng phải gần $1.332$, điểm $z$ của lời chứng minh vẫn khả thi, nhưng đồ thị tại $z$ nằm **trên** dây cung, nên bước 2 sụp đổ. Với hàm lồi $\tfrac12 (x - 1)^2$ nhưng miền khả thi gồm hai đoạn rời nhau, điểm $x = -1.2$ ở mép đoạn trái là cực tiểu cục bộ không toàn cục. Lần này điểm $z$ rơi vào khoảng trống giữa hai đoạn, nên bước 1 sụp đổ. Định lý cần **cả hai** loại tính lồi, của hàm và của miền.

## 4. Ý nghĩa đối với thuật toán

Mọi phương pháp tối ưu lặp, từ phương pháp gradient tới phương pháp Newton, đều chỉ dùng thông tin trong một lân cận nhỏ của điểm đang đứng: Giá trị, gradient, có khi thêm Hessian. Với bài toán không lồi, một phương pháp như vậy có thể dừng ở một cực tiểu cục bộ tồi, ở một điểm yên ngựa, và kết quả phụ thuộc vào điểm xuất phát. Với bài toán lồi, ba nỗi lo đó biến mất cùng lúc:

- Mọi cực tiểu cục bộ là toàn cục, nên không có cực tiểu cục bộ "tồi".
- Với hàm khả vi, mọi điểm dừng đều là cực tiểu toàn cục (chủ đề điều kiện bậc nhất), do đó hoàn toàn không xuất hiện điểm yên ngựa làm chệch hướng thuật toán.
- Tập nghiệm lồi, nên các điểm xuất phát khác nhau có thể dẫn tới các nghiệm khác nhau, nhưng tất cả đều tối ưu như nhau.

Đây là lý do một bài toán đã được nhận ra là lồi được xem gần như "đã giải xong": Việc còn lại là chọn một bộ giải đủ tốt. Còn với mạng nơ-ron, hàm mất mát không lồi, và câu hỏi "vì sao phương pháp gradient vẫn tìm được nghiệm tốt" là một hướng nghiên cứu còn mở, không có lời đáp gọn như định lý trên.

**Tính tựa lồi chưa đủ để bảo toàn tính chất.** Với bài toán tựa lồi (quasiconvex optimization), tức hàm mục tiêu chỉ thỏa mãn điều kiện các tập mức dưới lồi, định lý này không còn đúng nữa. Hàm $f(x) = \min\{\max\{x, 0\},\ 1\}$ bằng 0 khi $x \le 0$, tăng tuyến tính trên $[0, 1]$, và bằng 1 khi $x \ge 1$. Hàm này đơn điệu nên tựa lồi. Điểm $x = 2$ nằm trên đoạn phẳng ở độ cao 1, do đó là một cực tiểu cục bộ với mọi $R < 1$, trong khi giá trị nhỏ nhất toàn cục của hàm lại là 0. Lời chứng minh ở Mục 3 không còn áp dụng được vì tính tựa lồi không cho bất đẳng thức dây cung, mà chỉ cho $f(z) \le \max\{f(x), f(y)\}$, điều kiện này không đủ mạnh để suy ra $f(z) < f(x)$.

## 5. Những câu hỏi để đào sâu

**Câu 1.** Lời chứng minh chọn $z$ cách $x$ đúng $R/2$. Nếu chọn $z$ cách $x$ đúng $R$ thì có còn đúng không? Còn chọn $z = y$ thì sao?

<details><summary>Xem lời giải thích</summary>

Chọn khoảng cách đúng $R$ vẫn hoàn toàn hợp lệ, vì định nghĩa cực tiểu cục bộ ở đây sử dụng điều kiện $\|z - x\|_2 \le R$ (bao gồm cả biên). Việc chọn $R/2$ là một kỹ thuật chặt chẽ nhằm bảo đảm $z$ nằm hẳn bên trong hình cầu mở của lân cận, tránh phụ thuộc vào việc định nghĩa dùng bất đẳng thức ngặt hay không. Trái lại, việc chọn ngay $z = y$ sẽ không mang lại kết quả: Điểm $y$ nằm ngoài lân cận bán kính $R$, do đó $f_0(y) < f_0(x)$ không hề mâu thuẫn với tính tối ưu cục bộ tại $x$. Toàn bộ vẻ đẹp và sức mạnh của phép chứng minh nằm ở chỗ: Tính lồi **kéo thông tin từ điểm $y$ ở rất xa về một điểm $z$ nằm ngay sát trong lân cận**.

</details>

**Câu 2.** Một bài toán lồi có thể có đúng hai nghiệm tối ưu không? Một bài toán không lồi thì sao?

<details><summary>Xem lời giải thích</summary>

Bài toán lồi thì không: Tập nghiệm lồi, nên nếu chứa hai điểm thì chứa cả đoạn nối chúng, tức vô số điểm. Bài toán không lồi thì có thể. Hàm $x^4 + y^4 - 4xy$ ở bài tập của chủ đề điều kiện bậc hai có đúng hai cực tiểu toàn cục $(1, 1)$ và $(-1, -1)$, còn trung điểm của chúng có giá trị cao hơn hẳn. Hiện tượng "các nghiệm đối xứng tách rời" như vậy là dấu hiệu điển hình của bài toán không lồi, và nó xuất hiện tự nhiên trong mạng nơ-ron, như chủ đề cuối của chương sẽ chỉ ra.

</details>

**Câu 3.** Bài toán cực tiểu $x_1 + x_2$ với $x_1^2 + x_2^2 = 1$ không lồi. Thay ràng buộc bằng $x_1^2 + x_2^2 \le 1$, ta được một bài toán lồi. Hai bài toán có cùng nghiệm không? Điều đó có luôn đúng khi nới đẳng thức thành bất đẳng thức?

<details><summary>Xem lời giải thích</summary>

Lần này cùng nghiệm. Bài toán nới lỏng cực tiểu một hàm tuyến tính trên hình tròn, và nghiệm nằm trên biên tại $(-1/\sqrt2,\ -1/\sqrt2)$ với giá trị $-\sqrt2$, điểm này cũng thỏa đẳng thức. Nhưng điều đó không luôn đúng. Nếu hàm mục tiêu là $(x_1 - 0.1)^2 + x_2^2$, bài toán nới lỏng có nghiệm $(0.1, 0)$ nằm hẳn bên trong hình tròn, không thỏa đẳng thức, trong khi bài toán gốc có nghiệm $(1, 0)$. Nới lỏng chỉ "chặt" khi hàm mục tiêu tự đẩy nghiệm ra biên.

</details>

**Câu 4.** Trong bài toán lồi, phương pháp gradient xuất phát từ hai điểm khác nhau có thể hội tụ về hai điểm khác nhau không? Điều đó có mâu thuẫn với định lý không?

<details><summary>Xem lời giải thích</summary>

Có thể, khi tập nghiệm có nhiều hơn một điểm. Với bình phương tối thiểu có hai đặc trưng cộng tuyến ở chủ đề điều kiện bậc hai, phương pháp gradient xuất phát từ $w^{(0)}$ chỉ di chuyển trong tập $w^{(0)} + \mathcal{R}(A^T)$, như chủ đề về tập affine đã chỉ ra, nên điểm hội tụ phụ thuộc vào điểm xuất phát. Không có mâu thuẫn nào: Mọi điểm hội tụ đều tối ưu, chúng chỉ khác nhau về vị trí chứ không khác nhau về giá trị hàm mục tiêu.

</details>

## 6. Bài tập tự luyện

::: exercise 1. Bài toán nào là bài toán lồi ở dạng chuẩn?
Với mỗi bài toán, cho biết nó có phải bài toán lồi ở dạng chuẩn không. Nếu không, có viết lại được thành một bài toán lồi tương đương không? (a) Cực tiểu $x_1^2 + x_2^2$ với $x_1 + x_2 \ge 1$. (b) Cực tiểu $x_1 + x_2$ với $x_1^2 + x_2^2 = 1$. (c) Cực đại $\log x_1 + \log x_2$ với $x_1 + 2x_2 \le 4$. (d) Cực tiểu $x_1 x_2$ với $-1 \le x_1 \le 1$, $-1 \le x_2 \le 1$.
:::

::: solution
(a) Có, sau khi viết ràng buộc thành $1 - x_1 - x_2 \le 0$, một hàm affine. Hàm mục tiêu lồi. (b) Không, vì ràng buộc đẳng thức không affine và miền khả thi là đường tròn (tập không lồi). Bài toán gốc không thể biến đổi đại số tương đương về dạng chuẩn, tuy nhiên như Câu 3 đã phân tích, nó có cùng nghiệm với bài toán nới lỏng lồi khi thay dấu đẳng thức "=" bằng bất đẳng thức "≤". (c) Có, đây là bài toán cực đại một hàm lõm với ràng buộc affine, nên là bài toán lồi. Nghiệm là $x = (2, 1)$ với giá trị $\log 2$: Tại đó $\nabla(\log x_1 + \log x_2) = (1/2,\ 1)$ tỉ lệ với $(1, 2)$, pháp tuyến của ràng buộc. (d) Không, vì $x_1 x_2$ không lồi: Hessian $\begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}$ có một trị riêng âm. Miền khả thi lồi, nhưng chừng đó không đủ.
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

Định lý trung tâm: Mọi cực tiểu cục bộ của bài toán lồi là cực tiểu toàn cục. Lời chứng minh dùng tính lồi của miền để giữ một điểm trung gian khả thi, và tính lồi của hàm để điểm đó tốt hơn. Thiếu một trong hai, định lý có thể sai, và với bài toán tựa lồi nó cũng sai. Vì vậy với bài toán lồi, một thuật toán chỉ nhìn cục bộ vẫn tìm được nghiệm toàn cục.

## Tài liệu tham khảo

- Stephen Boyd, Lieven Vandenberghe, *Convex Optimization*, Cambridge University Press.
