---
course: ai-nen-tang-tac-tu
lecture: 05-menh-de-va-suy-dien
section: topic
topic: 5-1-menh-de
title: "5.1 Mệnh đề"
description: "Cú pháp và ngữ nghĩa của giải tích mệnh đề, liên từ logic, bảng chân trị, mô hình, quan hệ kéo theo logic cùng góc nhìn ngữ nghĩa từ con người và máy tính."
---

Một mệnh đề (proposition) là một câu văn, được viết trong một ngôn ngữ hình thức, mang một giá trị chân lý (tức là đúng hoặc sai) trong một thế giới cụ thể. Một mệnh đề được xây dựng từ các mệnh đề nguyên tử cùng các liên từ logic.

## 5.1.1 Cú pháp của giải tích mệnh đề

Một **mệnh đề nguyên tử** (atomic proposition), hay gọi tắt là một **nguyên tử** (atom), là một ký hiệu biểu diễn một sự kiện cơ sở. Các nguyên tử được viết dưới dạng chuỗi các chữ cái, chữ số và dấu gạch dưới (`_`), bắt đầu bằng một chữ cái viết thường. Chẳng hạn: $a$, ${ai\_is\_fun}$, ${lit\_l}_{1}$, ${live\_outside}$, ${mimsy}$, và ${sunny}$ đều là các nguyên tử hợp lệ.

Các mệnh đề phức hợp có thể được xây dựng từ những mệnh đề đơn giản hơn nhờ các liên từ logic. Một mệnh đề hoặc công thức logic (logical formula) có thể là:

- Một mệnh đề nguyên tử.
- Hoặc một mệnh đề phức hợp có một trong các dạng sau:

| Biểu thức logic | Cách đọc | Tên gọi chuẩn |
| :--- | :--- | :--- |
| $\neg p$ | "Không $p$" | Phủ định của $p$ (negation) |
| $p \wedge q$ | "$p$ và $q$" | Phép hội của $p$ và $q$ (conjunction) |
| $p \vee q$ | "$p$ hoặc $q$" | Phép tuyển của $p$ và $q$ (disjunction) |
| $p \rightarrow q$ | "$p$ kéo theo $q$" | Phép kéo theo thuận của $q$ từ $p$ (implication) |
| $p \leftarrow q$ | "$p$ nếu $q$" | Phép kéo theo nghịch của $p$ từ $q$ (implication) |
| $p \leftrightarrow q$ | "$p$ khi và chỉ khi $q$" | Phép tương đương logic giữa $p$ và $q$ (equivalence) |
| $p \oplus q$ | "$p$ tuyển loại trừ $q$" | Phép XOR giữa $p$ và $q$ (exclusive-or) |

Trong các dạng biểu thức trên, $p$ và $q$ là các mệnh đề.

Các toán tử $\neg$, $\wedge$, $\vee$, $\rightarrow$, $\leftarrow$, $\leftrightarrow$, và $\oplus$ được gọi là các liên từ logic (logical connectives).

Dấu ngoặc đơn có thể được sử dụng để loại bỏ tính nhập nhằng trong các công thức logic. Khi lược bỏ dấu ngoặc đơn, thứ tự ưu tiên của các toán tử được quy định theo đúng thứ tự xuất hiện trong bảng trên:

1. Phủ định ($\neg$) có độ ưu tiên cao nhất.
2. Phép hội ($\wedge$).
3. Phép tuyển ($\vee$).
4. Phép kéo theo thuận ($\rightarrow$).
5. Phép kéo theo nghịch ($\leftarrow$).
6. Phép tương đương ($\leftrightarrow$).
7. Tuyển loại trừ ($\oplus$) có độ ưu tiên thấp nhất.

Do đó, một mệnh đề phức hợp không chứa dấu ngoặc có thể được xác định tường minh bằng cách bổ sung các cặp ngoặc đơn theo thứ tự ưu tiên đã nêu. Ví dụ: Biểu thức $\neg a \vee b \land c \rightarrow d \land \neg e \vee f$ chính là cách viết rút gọn của biểu thức đầy đủ:

<pre class="logic-expression">((¬ a) ∨ (b ∧ c)) → ((d ∧ (¬ e)) ∨ f).</pre>

## 5.1.2 Ngữ nghĩa của giải tích mệnh đề

Ngữ nghĩa (semantics) xác định ý nghĩa thực sự của các câu trong một ngôn ngữ. Ngữ nghĩa của giải tích mệnh đề được định nghĩa thông qua khái niệm diễn giải và chân trị.

Về mặt trực giác, các mệnh đề mang ý nghĩa đối với người thiết kế hệ thống, người tuyên bố các mệnh đề mà họ khẳng định là đúng, sau đó đặt câu hỏi truy vấn xem những điều gì khác cũng bắt buộc phải đúng. Một **diễn giải** (interpretation) là một khả năng mà thế giới có thể tồn tại. Tất cả những gì hệ thống biết về thế giới chỉ là các mệnh đề được chỉ định là đúng, do đó thế giới thực bắt buộc phải tương ứng với một diễn giải mà trong đó những mệnh đề này đồng thời thỏa mãn.

Một diễn giải bao gồm một hàm $\pi$ ánh xạ mỗi nguyên tử vào tập chân trị $\{\mathit{true}, \mathit{false}\}$:

- Nếu $\pi(a) = \mathit{true}$, nguyên tử $a$ là đúng trong diễn giải đó.
- Nếu $\pi(a) = \mathit{false}$, nguyên tử $a$ là sai trong diễn giải đó.

Đôi khi, việc hình dung $\pi$ dưới dạng tập hợp các nguyên tử được gán giá trị $\mathit{true}$ cũng rất hữu ích, khi đó mọi nguyên tử nằm ngoài tập hợp này đều mặc định mang giá trị $\mathit{false}$.

Giá trị chân lý của một mệnh đề phức hợp trong một diễn giải được xác định từ giá trị chân lý của các mệnh đề thành phần thông qua bảng chân trị (Hình 5.1).

Giá trị chân lý chỉ được xác định khi gắn liền với một diễn giải cụ thể. Cùng một mệnh đề có thể nhận các giá trị chân lý khác nhau trong các diễn giải khác nhau.

| $p$ | $q$ | $\neg p$ | $p \wedge q$ | $p \vee q$ | $p \rightarrow q$ | $p \leftarrow q$ | $p \leftrightarrow q$ | $p \oplus q$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $\mathit{true}$ | $\mathit{true}$ | $\mathit{false}$ | $\mathit{true}$ | $\mathit{true}$ | $\mathit{true}$ | $\mathit{true}$ | $\mathit{true}$ | $\mathit{false}$ |
| $\mathit{true}$ | $\mathit{false}$ | $\mathit{false}$ | $\mathit{false}$ | $\mathit{true}$ | $\mathit{false}$ | $\mathit{true}$ | $\mathit{false}$ | $\mathit{true}$ |
| $\mathit{false}$ | $\mathit{true}$ | $\mathit{true}$ | $\mathit{false}$ | $\mathit{true}$ | $\mathit{true}$ | $\mathit{false}$ | $\mathit{false}$ | $\mathit{true}$ |
| $\mathit{false}$ | $\mathit{false}$ | $\mathit{true}$ | $\mathit{false}$ | $\mathit{false}$ | $\mathit{true}$ | $\mathit{true}$ | $\mathit{true}$ | $\mathit{false}$ |

Hình 5.1: Bảng chân trị định nghĩa các phép toán $\neg$, $\wedge$, $\vee$, $\rightarrow$, $\leftarrow$, $\leftrightarrow$ và $\oplus$.

::: example Ví dụ 5.1: Đánh giá chân trị mệnh đề trong các diễn giải khác nhau
Giả sử có ba nguyên tử: $\mathit{ai\_is\_fun}$, $\mathit{happy}$, và $\mathit{light\_on}$.

Xét diễn giải $I_{1}$ gán giá trị $\mathit{true}$ cho $\mathit{ai\_is\_fun}$, $\mathit{false}$ cho $\mathit{happy}$, và $\mathit{true}$ cho $\mathit{light\_on}$. Tức là diễn giải $I_{1}$ được xác định bởi hàm $\pi_{1}$:

<pre class="logic-expression">π_1(ai_is_fun) = true,   π_1(happy) = false,   π_1(light_on) = true.</pre>

Khi đó, giá trị chân lý của các mệnh đề trong diễn giải $I_{1}$ như sau:

- $\mathit{ai\_is\_fun}$ là đúng trong $I_{1}$.
- $\neg \mathit{ai\_is\_fun}$ là sai trong $I_{1}$.
- $\mathit{happy}$ là sai trong $I_{1}$.
- $\neg \mathit{happy}$ là đúng trong $I_{1}$.
- $\mathit{ai\_is\_fun} \vee \mathit{happy}$ là đúng trong $I_{1}$.
- $\mathit{ai\_is\_fun} \leftarrow \mathit{happy}$ là đúng trong $I_{1}$ (vì $\mathit{happy}$ sai nên tiền đề sai, phép kéo theo hiển nhiên đúng).
- $\mathit{happy} \leftarrow \mathit{ai\_is\_fun}$ là sai trong $I_{1}$ (vì tiền đề $\mathit{ai\_is\_fun}$ đúng nhưng kết luận $\mathit{happy}$ sai).
- $\mathit{ai\_is\_fun} \leftarrow \mathit{happy} \wedge \mathit{light\_on}$ là đúng trong $I_{1}$.

Xét diễn giải $I_{2}$ gán giá trị $\mathit{false}$ cho $\mathit{ai\_is\_fun}$, $\mathit{true}$ cho $\mathit{happy}$, và $\mathit{false}$ cho $\mathit{light\_on}$:

- $\mathit{ai\_is\_fun}$ là sai trong $I_{2}$.
- $\neg \mathit{ai\_is\_fun}$ là đúng trong $I_{2}$.
- $\mathit{happy}$ là đúng trong $I_{2}$.
- $\neg \mathit{happy}$ là sai trong $I_{2}$.
- $\mathit{ai\_is\_fun} \vee \mathit{happy}$ là đúng trong $I_{2}$.
- $\mathit{ai\_is\_fun} \leftarrow \mathit{happy}$ là sai trong $I_{2}$ (vì tiền đề $\mathit{happy}$ đúng nhưng kết luận $\mathit{ai\_is\_fun}$ sai).
- $\mathit{ai\_is\_fun} \leftarrow \mathit{light\_on}$ là đúng trong $I_{2}$ (vì $\mathit{light\_on}$ sai).
- $\mathit{ai\_is\_fun} \leftarrow \mathit{happy} \wedge \mathit{light\_on}$ là đúng trong $I_{2}$ (vì $\mathit{happy} \wedge \mathit{light\_on}$ nhận giá trị sai).
:::

Một **cơ sở tri thức** (knowledge base, ký hiệu là $\mathit{KB}$) là một tập hợp các mệnh đề được khẳng định là đúng. Mỗi phần tử trong cơ sở tri thức được gọi là một **tiên đề** (axiom). Các phần tử của một cơ sở tri thức được ngầm định liên kết với nhau bằng phép hội, do đó cơ sở tri thức là đúng khi và chỉ khi mọi tiên đề trong đó đều đồng thời đúng.

Một **mô hình** (model) của cơ sở tri thức $\mathit{KB}$ là một diễn giải mà trong đó tất cả các mệnh đề của $\mathit{KB}$ đều mang giá trị đúng.

Nếu $\mathit{KB}$ là một cơ sở tri thức và $g$ là một mệnh đề, ta nói $g$ là một **hệ quả logic** (logical consequence) của $\mathit{KB}$, hoặc $g$ được suy ra một cách logic từ $\mathit{KB}$, hoặc $\mathit{KB}$ **kéo theo logic** $g$ (entails), ký hiệu là:

$$
\mathit{KB} \models g
$$

nếu $g$ nhận giá trị đúng trong mọi mô hình của $\mathit{KB}$. Ngược lại, $g$ không phải là hệ quả logic của $\mathit{KB}$, ký hiệu là $\mathit{KB} \not\models g$, khi tồn tại ít nhất một mô hình của $\mathit{KB}$ mà trong đó $g$ nhận giá trị sai.

::: example Ví dụ 5.2: Cơ sở tri thức và quan hệ kéo theo logic
Xét cơ sở tri thức $\mathit{KB}$ gồm các tiên đề sau:

<pre class="logic-expression">sam_is_happy. 

ai_is_fun. 

worms_live_underground. 

night_time. 

bird_eats_apple. 

apple_is_eaten ← bird_eats_apple. 

switch_1_is_up ← someone_is_in_room ∧ night_time.</pre>

Với cơ sở tri thức này:

- $\mathit{KB} \models \mathit{bird\_eats\_apple}$ vì $\mathit{bird\_eats\_apple}$ là một tiên đề trực tiếp trong $\mathit{KB}$.
- $\mathit{KB} \models \mathit{apple\_is\_eaten}$ vì trong mọi mô hình của $\mathit{KB}$, $\mathit{bird\_eats\_apple}$ đúng, kéo theo kết luận $\mathit{apple\_is\_eaten}$ bắt buộc phải đúng để thỏa mãn quy tắc kéo theo.
- $\mathit{KB} \not\models \mathit{switch\_1\_is\_up}$ vì tồn tại một mô hình của cơ sở tri thức mà ở đó $\mathit{switch\_1\_is\_up}$ mang giá trị sai. Trong mô hình đó, nguyên tử $\mathit{someone\_is\_in\_room}$ nhận giá trị sai, làm cho vế điều kiện sai và tiên đề kéo theo vẫn thỏa mãn mà không bắt buộc $\mathit{switch\_1\_is\_up}$ phải đúng.
:::

## 5.1.3 Góc nhìn của con người về ngữ nghĩa

Mô tả thuần túy toán học về ngữ nghĩa chưa giải thích vì sao ngữ nghĩa lại có vai trò quan trọng và có thể làm nền tảng để xây dựng các hệ thống thông minh. Ý tưởng cốt lõi đằng sau việc sử dụng logic là: Khi người thiết kế cơ sở tri thức cần mô tả một thế giới cụ thể, họ có thể chọn thế giới đó làm **diễn giải dự định** (intended interpretation), chọn ý nghĩa cho các ký hiệu tương ứng với thế giới đó, và viết ra các mệnh đề về những gì đúng trong thế giới ấy. Khi hệ thống tính toán ra một hệ quả logic của cơ sở tri thức, người thiết kế có thể diễn giải câu trả lời này theo đúng diễn giải dự định ban đầu.

Phương pháp luận được người thiết kế cơ sở tri thức sử dụng để biểu diễn thế giới gồm 4 bước:

1. **Bước 1**: Người thiết kế chọn một miền tác vụ hoặc thế giới cần biểu diễn, đây chính là diễn giải dự định. Miền tác vụ này có thể là một khía cạnh của thế giới thực (ví dụ: Cấu trúc các khóa học và sinh viên tại trường đại học, hoặc môi trường phòng thí nghiệm tại một thời điểm), một thế giới tưởng tượng (như thế giới Alice ở xứ sở diệu kỳ, hoặc trạng thái của hệ thống điện khi một công tắc bị hỏng), hoặc một thế giới trừu tượng (như thế giới của các con số và tập hợp).
2. **Bước 2**: Người thiết kế lựa chọn các nguyên tử để đại diện cho những mệnh đề mà mình quan tâm. Mỗi nguyên tử mang một ý nghĩa chuẩn xác đối với người thiết kế trong diễn giải dự định. Ý nghĩa được gán cho các ký hiệu này tạo nên một diễn giải dự định hoặc một khái niệm hóa (conceptualization).
3. **Bước 3**: Người thiết kế cung cấp cho hệ thống các mệnh đề đúng trong diễn giải dự định. Quá trình này thường được gọi là **tiên đề hóa miền bài toán** (axiomatizing the domain), trong đó các mệnh đề được nạp vào đóng vai trò là các tiên đề của miền bài toán.
4. **Bước 4**: Người dùng có thể đặt các câu hỏi truy vấn về diễn giải dự định. Hệ thống sẽ suy diễn và trả lời các câu hỏi đó. Người dùng, vốn đã thấu hiểu diễn giải dự định, có thể thông hiểu các câu trả lời dựa trên ý nghĩa đã quy ước cho các ký hiệu.

Trong phương pháp luận này, người thiết kế hoàn toàn không truyền đạt bất kỳ thông tin nào cho máy tính cho đến khi thực hiện Bước 3.

## 5.1.4 Góc nhìn của máy tính về ngữ nghĩa

Máy tính không có quyền truy cập trực tiếp vào diễn giải dự định của con người. Tất cả những gì máy tính biết về diễn giải dự định chỉ gói gọn trong cơ sở tri thức $\mathit{KB}$.

Nếu $\mathit{KB} \models g$, thì $g$ bắt buộc phải đúng trong diễn giải dự định, bởi vì $g$ đúng trong mọi mô hình của cơ sở tri thức (mà diễn giải dự định chắc chắn là một trong các mô hình đó).

Nếu $\mathit{KB} \not\models g$, nghĩa là $g$ không phải là hệ quả logic của $\mathit{KB}$, thì tồn tại ít nhất một mô hình của $\mathit{KB}$ mà trong đó $g$ nhận giá trị sai. Đứng từ giác độ của máy tính, diễn giải dự định hoàn toàn có thể chính là mô hình mà $g$ nhận giá trị sai, do đó máy tính không thể kết luận được liệu $g$ có đúng trong diễn giải dự định hay không.

Đối với một cơ sở tri thức cho trước, các mô hình của cơ sở tri thức tương ứng với tất cả các cách mà thế giới có thể tồn tại, miễn là cơ sở tri thức vẫn đúng.

::: example Ví dụ 5.3: Khác biệt giữa góc nhìn con người và máy tính
Xem xét lại cơ sở tri thức trong Ví dụ 5.2:

Người dùng có thể diễn giải các ký hiệu như mang những ý nghĩa thực tế cụ thể. Máy tính không hề biết ý nghĩa tự nhiên của các ký hiệu chuỗi ký tự đó, nhưng nó vẫn rút ra được các kết luận logic chắc chắn dựa trên những gì đã được cung cấp. Nó có thể kết luận chắc chắn rằng $\mathit{apple\_is\_eaten}$ là đúng trong diễn giải dự định. Tuy nhiên, nó không thể kết luận $\mathit{switch\_1\_is\_up}$ vì nó không biết liệu $\mathit{someone\_is\_in\_room}$ là đúng hay sai trong diễn giải dự định.

Nếu người thiết kế cơ sở tri thức đưa vào những thông tin sai lệch, tức là một số tiên đề bị sai trong diễn giải dự định, thì các câu trả lời do máy tính suy diễn ra không còn được đảm bảo là đúng trong diễn giải dự định nữa.
:::

## Tài liệu tham khảo

1. Poole, D. L., & Mackworth, A. K. (2023). *Artificial Intelligence: Foundations of Computational Agents* (3rd ed.). Chapter 5: Propositions and Inference. Cambridge University Press.
2. Enderton, H. B. (2001). *A Mathematical Introduction to Logic* (2nd ed.). Academic Press.
3. Genesereth, M. R., & Nilsson, N. J. (1987). *Logical Foundations of Artificial Intelligence*. Morgan Kaufmann.


[Đọc mục tương ứng trong giáo trình](https://artint.info/3e/html/ArtInt3e.Ch5.S1.html).
