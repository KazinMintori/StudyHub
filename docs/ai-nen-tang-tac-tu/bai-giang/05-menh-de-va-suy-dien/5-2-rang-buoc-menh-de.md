---
course: ai-nen-tang-tac-tu
lecture: 05-menh-de-va-suy-dien
section: topic
topic: 5-2-rang-buoc-menh-de
title: "5.2 Ràng buộc mệnh đề"
description: "Mô hình hóa bài toán thỏa mãn ràng buộc bằng logic mệnh đề, dạng câu tuyển, thuật toán DPLL, độ nhất quán cung và tìm kiếm cục bộ ngẫu nhiên."
---

Các công thức logic cung cấp một dạng thức biểu diễn súc tích cho các ràng buộc với cấu trúc nội tại phong phú có thể khai thác được. Có nhiều lý do quan trọng để sử dụng mệnh đề trong việc đặc tả các ràng buộc và câu hỏi truy vấn:

- Việc phát biểu một mệnh đề logic về mối quan hệ giữa các biến thường ngắn gọn và dễ đọc hơn nhiều so với việc liệt kê tường minh toàn bộ các phép gán hợp lệ (biểu diễn ngoại diên).
- Cấu trúc hình thức của tri thức có thể được khai thác triệt để nhằm nâng cao hiệu quả suy luận.
- Mệnh đề có tính mô đun cao, do đó những thay đổi nhỏ trong bài toán chỉ dẫn đến những thay đổi nhỏ trong cơ sở tri thức. Điều này giúp việc kiểm thử và gỡ lỗi cơ sở tri thức trở nên thuận tiện hơn các dạng biểu diễn khác.
- Dạng câu hỏi truy vấn có thể phong phú hơn việc chỉ gán giá trị đơn lẻ cho các biến.
- Ngôn ngữ mệnh đề có thể được mở rộng tự nhiên để suy luận về các cá thể (đối tượng, thực thể) cùng các mối quan hệ giữa chúng.

Họ các bài toán thỏa mãn mệnh đề (propositional satisfiability, thường gọi tắt là bài toán SAT) được cấu thành từ:

- **Biến Boolean**: Là biến có miền giá trị gồm hai phần tử $\{\mathit{true}, \mathit{false}\}$. Nếu $X$ là một biến Boolean, việc gán $X = \mathit{true}$ được viết dưới dạng nguyên tử chữ thường tương ứng là $x$, và $X = \mathit{false}$ được viết là $\neg x$. Chẳng hạn: Mệnh đề $\mathit{happy}$ có nghĩa là biến Boolean $\mathit{Happy}$ nhận giá trị đúng ($\mathit{Happy} = \mathit{true}$), còn $\neg \mathit{happy}$ có nghĩa là $\mathit{Happy} = \mathit{false}$.
- **Ràng buộc dạng câu tuyển (clausal constraints)**: Một **câu tuyển** (clause) là một biểu thức logic có dạng $l_{1} \vee l_{2} \vee \dots \vee l_{k}$, trong đó mỗi $l_{i}$ là một **từ vị** (literal). Một từ vị là một nguyên tử hoặc phủ định của một nguyên tử, tương ứng với một phép gán giá trị cho một biến Boolean. Khái niệm biến chỉ báo là một kỹ thuật riêng biệt được dùng khi mã hóa các bài toán CSP rời rạc sang câu tuyển mệnh đề. Một câu tuyển là đúng trong một diễn giải khi và chỉ khi có ít nhất một từ vị trong câu tuyển đó nhận giá trị đúng trong diễn giải ấy.

Nếu $\neg a$ xuất hiện trong một câu tuyển, nguyên tử $a$ được gọi là xuất hiện phủ định trong câu tuyển đó. Nếu $a$ xuất hiện không có dấu phủ định, ta nói $a$ xuất hiện khẳng định trong câu tuyển.

Xét trên giác độ giải tích mệnh đề, một tập hợp các câu tuyển là một dạng công thức logic có cấu trúc chuẩn tắc. Mọi công thức mệnh đề bất kỳ đều có thể biến đổi tương đương về dạng các câu tuyển (dạng chuẩn hội - CNF). Một phép gán toàn phần cho tất cả các biến tương ứng với một diễn giải hình thức.

Xét trên giác độ mạng ràng buộc, một câu tuyển là một ràng buộc trên một tập hợp các biến Boolean nhằm loại bỏ chính xác một phép gán giá trị không hợp lệ của các từ vị trong câu tuyển đó. Câu tuyển $l_{1} \vee l_{2} \vee \dots \vee l_{k}$ tương đương với mệnh đề $\neg(\neg l_{1} \wedge \neg l_{2} \wedge \dots \wedge \neg l_{k})$, phát biểu rằng không được phép để tất cả các $l_{i}$ đồng thời nhận giá trị sai.

::: example Ví dụ 5.4: Ràng buộc câu tuyển và phép gán vi phạm
Câu tuyển $\mathit{happy} \vee \mathit{sad} \vee \neg \mathit{living}$ là một ràng buộc giữa ba biến Boolean $\mathit{Happy}$, $\mathit{Sad}$, và $\mathit{Living}$. Ràng buộc này nhận giá trị đúng nếu $\mathit{Happy}$ nhận giá trị $\mathit{true}$, hoặc $\mathit{Sad}$ nhận giá trị $\mathit{true}$, hoặc $\mathit{Living}$ nhận giá trị $\mathit{false}$. Các nguyên tử $\mathit{happy}$ và $\mathit{sad}$ xuất hiện khẳng định, trong khi $\mathit{living}$ xuất hiện phủ định trong câu tuyển.

Phép gán $\neg \mathit{happy}$, $\neg \mathit{sad}$, và $\mathit{living}$ vi phạm ràng buộc của câu tuyển $\mathit{happy} \vee \mathit{sad} \vee \neg \mathit{living}$. Đây là phép gán duy nhất trong số 8 tổ hợp giá trị của ba biến này làm cho câu tuyển bị sai.
:::

## 5.2.1 Biến đổi bài toán CSP sang dạng câu tuyển

Mọi bài toán thỏa mãn ràng buộc (CSP) hữu hạn đều có thể chuyển đổi thành một bài toán thỏa mãn mệnh đề tương đương theo quy trình chuẩn sau:

- Một biến $Y$ có miền giá trị rời rạc gồm $k$ phần tử $\{v_{1}, \dots, v_{k}\}$ được chuyển đổi thành $k$ biến Boolean $\{Y_{1}, \dots, Y_{k}\}$, trong đó biến $Y_{i}$ nhận giá trị đúng khi $Y = v_{i}$ và nhận giá trị sai trong trường hợp ngược lại. Mỗi biến $Y_{i}$ được gọi là một **biến chỉ báo** (indicator variable). Do đó, ta sử dụng $k$ nguyên tử $y_{1}, \dots, y_{k}$ để đại diện cho biến CSP ban đầu.
- Có các ràng buộc quy định rằng $y_{i}$ và $y_{j}$ không thể đồng thời nhận giá trị đúng khi $i \neq j$, tức là các câu tuyển loại trừ: $\neg y_{i} \vee \neg y_{j}$ với mọi cặp chỉ số thỏa mãn $i < j$. Đồng thời, có một ràng buộc quy định rằng ít nhất một trong các $y_{i}$ bắt buộc phải đúng, tức là câu tuyển bao phủ: $y_{1} \vee \dots \vee y_{k}$.
- Để dịch các ràng buộc gốc của bài toán, lưu ý rằng $\neg x_{1} \vee \dots \vee \neg x_{k}$ tương đương với $\neg(x_{1} \wedge \dots \wedge x_{k})$ với các nguyên tử $x_{1}, \dots, x_{k}$ bất kỳ. Một phương pháp tổng quát để biểu diễn một ràng buộc là sử dụng một câu tuyển cho mỗi phép gán giá trị vi phạm ràng buộc đó. Ví dụ: Câu tuyển $\neg x_{5} \vee \neg y_{7}$ biểu diễn rằng tổ hợp $X = v_{5}$ và $Y = v_{7}$ là một cấu hình vi phạm ràng buộc.

Trong thực tế, người ta thường rút gọn được số lượng câu tuyển ít hơn rất nhiều so với cách tiếp cận chuyển đổi ngây thơ.

::: example Ví dụ 5.5: Biến đổi ràng buộc bất đẳng thức giữa hai biến
Xét hai biến $A$ và $B$, mỗi biến đều có miền giá trị $\{1, 2, 3, 4\}$.

Đối với biến $A$, ta khởi tạo bốn biến Boolean $a_{1}, a_{2}, a_{3}$, và $a_{4}$, trong đó $a_{1}$ đúng khi $A = 1$, $a_{2}$ đúng khi $A = 2$, $a_{3}$ đúng khi $A = 3$, và $a_{4}$ đúng khi $A = 4$. Bốn biến này thỏa mãn tính chất đôi một rời nhau và bao phủ toàn bộ miền giá trị, dẫn đến hệ gồm 7 câu tuyển:

<pre class="logic-expression">¬ a_1 ∨ ¬ a_2,   ¬ a_1 ∨ ¬ a_3,   ¬ a_1 ∨ ¬ a_4, 

¬ a_2 ∨ ¬ a_3,   ¬ a_2 ∨ ¬ a_4,   ¬ a_3 ∨ ¬ a_4, 

a_1 ∨ a_2 ∨ a_3 ∨ a_4.</pre>

Tương tự, đối với biến $B$, ta cũng thu được hệ 7 câu tuyển tương ứng cho các biến chỉ báo $b_{1}, b_{2}, b_{3}, b_{4}$.

Ràng buộc $A < B$ kéo theo rằng $a_{4}$ bắt buộc phải sai (vì không có giá trị nào trong miền của $B$ lớn hơn 4), $b_{1}$ bắt buộc phải sai (vì không có giá trị nào trong miền của $A$ nhỏ hơn 1). Các cặp giá trị khác vi phạm điều kiện $A < B$ cũng bị loại trừ, tạo nên hệ 5 câu tuyển bổ sung:

<pre class="logic-expression">¬ a_4,   ¬ b_1,   ¬ a_2 ∨ ¬ b_2,   ¬ a_3 ∨ ¬ b_3,   ¬ a_3 ∨ ¬ b_2.</pre>

Lưu ý rằng ta không cần đưa vào câu tuyển $\neg a_{1} \vee \neg b_{1}$, bởi vì câu tuyển này đã được suy ra trực tiếp từ sự kiện đơn vị $\neg b_{1}$.
:::

Các thuật toán kiểm tra tính nhất quán có thể được tối ưu hóa vượt bậc khi áp dụng cho bài toán thỏa mãn mệnh đề so với bài toán CSP tổng quát. Khi miền giá trị chỉ có đúng hai phần tử, việc tỉa một giá trị khỏi miền tương đương trực tiếp với việc gán biến nhận giá trị đối lập còn lại. Vì vậy, nếu $X$ có miền $\{\mathit{true}, \mathit{false}\}$, việc loại bỏ $\mathit{true}$ khỏi miền của $X$ đồng nghĩa với việc gán $X = \mathit{false}$.

Độ nhất quán cung (arc consistency) được áp dụng để đồng thời tỉa bớt miền giá trị và rút gọn tập các ràng buộc:

- Nếu $X$ được gán giá trị $\mathit{true}$, toàn bộ các câu tuyển chứa từ vị khẳng định $X = \mathit{true}$ đều trở nên dư thừa vì chúng đã được thỏa mãn. Ta có thể loại bỏ hoàn toàn các câu tuyển này khỏi tập đang xét. Tương tự, nếu $X$ được gán giá trị $\mathit{false}$, các câu tuyển chứa từ vị phủ định $X = \mathit{false}$ cũng được loại bỏ.
- Nếu $X$ được gán giá trị $\mathit{true}$, bất kỳ câu tuyển nào chứa từ vị phủ định $X = \mathit{false}$ đều có thể rút gọn bằng cách xóa bỏ từ vị sai đó ra khỏi câu tuyển. Tương tự, nếu $X$ được gán giá trị $\mathit{false}$, thì từ vị khẳng định $X = \mathit{true}$ có thể bị xóa khỏi mọi câu tuyển mà nó góp mặt. Bước biến đổi này được gọi là **phân giải đơn vị** (unit resolution).

Nếu sau quá trình tỉa rút, xuất hiện một câu tuyển chỉ chứa đúng một từ vị duy nhất dạng $Y = v$ (câu tuyển đơn vị), giá trị đối lập còn lại sẽ bị loại bỏ khỏi miền của $Y$. Đây chính là một biểu hiện của độ nhất quán cung. Nếu tất cả các từ vị trong một câu tuyển đều bị xóa bỏ (trở thành câu tuyển rỗng $\Box$), hệ ràng buộc rơi vào trạng thái không thể thỏa mãn (unsatisfiable).

::: example Ví dụ 5.6: Quá trình rút gọn câu tuyển và tỉa miền giá trị
Xét câu tuyển $\neg x \vee y \vee \neg z$:

- Nếu biến $X$ được gán giá trị $\mathit{true}$, từ vị $\neg x$ nhận giá trị sai và bị loại bỏ, câu tuyển rút gọn thành $y \vee \neg z$.
- Nếu tiếp tục gán $Y = \mathit{false}$, từ vị $y$ bị loại bỏ, câu tuyển rút gọn thành câu tuyển đơn vị $\neg z$. Khi đó, giá trị $\mathit{true}$ bị tỉa khỏi miền của $Z$, buộc $Z$ phải nhận giá trị $\mathit{false}$.
- Ngược lại, nếu ngay từ đầu $X$ được gán giá trị $\mathit{false}$, từ vị $\neg x$ nhận giá trị đúng và toàn bộ câu tuyển được thỏa mãn, cho phép ta loại bỏ hoàn toàn câu tuyển này khỏi quá trình tính toán tiếp theo.
:::

Nếu một biến chỉ xuất hiện với cùng một cực tính trong tất cả các câu tuyển còn lại, và thuật toán chỉ cần tìm kiếm một mô hình thỏa mãn duy nhất, nó có thể gán ngay giá trị tương ứng cho biến đó. Ví dụ: Nếu biến $Y$ chỉ xuất hiện dưới dạng khẳng định $Y = \mathit{true}$ (tức là $\neg y$ hoàn toàn không có mặt trong bất kỳ câu tuyển nào), thì $Y$ có thể được gán giá trị $\mathit{true}$. Phép gán này không làm mất đi các mô hình thỏa mãn, nó chỉ đơn giản hóa bài toán vì tập hợp các câu tuyển còn lại sau khi gán $Y = \mathit{true}$ là một tập con của tập câu tuyển còn lại nếu $Y$ bị gán giá trị $\mathit{false}$. Một biến chỉ xuất hiện dưới một dạng duy nhất trong toàn bộ các câu tuyển được gọi là một **từ vị thuần khiết** (pure literal).

Sự kết hợp giữa tỉa miền giá trị và ràng buộc, phân chia miền (tìm kiếm nhánh) cùng quy tắc gán từ vị thuần khiết tạo nên **thuật toán Davis–Putnam–Logemann–Loveland (DPLL)**. Đây là một thuật toán có hiệu năng giải quyết bài toán SAT vượt trội khi được tích hợp các cấu trúc dữ liệu đánh chỉ mục tối ưu.

## 5.2.2 Khai thác cấu trúc mệnh đề trong tìm kiếm cục bộ

Phương pháp tìm kiếm cục bộ ngẫu nhiên (stochastic local search) có thể đạt tốc độ thực thi nhanh hơn đáng kể trên các bài toán CSP dạng SAT so với bài toán CSP tổng quát nhờ những đặc tính cấu trúc sau:

- Vì mỗi biến Boolean chỉ có duy nhất một giá trị thay thế đối lập, thuật toán không cần phải duyệt qua một danh sách dài các giá trị ứng viên khi quyết định đổi giá trị.
- Việc thay đổi giá trị của bất kỳ biến nào nằm trong một câu tuyển chưa được thỏa mãn đều sẽ làm cho câu tuyển đó trở nên thỏa mãn ngay lập tức. Do đó, việc thỏa mãn một câu tuyển đơn lẻ là rất dễ dàng, dù hành động này có thể vô tình làm một số câu tuyển khác mất đi tính thỏa mãn.
- Nếu một biến được chuyển trạng thái sang $\mathit{true}$, tất cả các câu tuyển mà nó xuất hiện khẳng định đều lập tức được thỏa mãn, và chỉ những câu tuyển mà nó xuất hiện phủ định mới có nguy cơ chuyển sang trạng thái vi phạm. Ngược lại, nếu một biến đổi sang $\mathit{false}$, tất cả các câu tuyển chứa nó ở dạng phủ định đều được thỏa mãn, và chỉ các câu tuyển chứa nó ở dạng khẳng định mới có nguy cơ bị vi phạm. Đặc tính này cho phép xây dựng cơ chế chỉ mục và cập nhật trạng thái cực nhanh.
- Không gian tìm kiếm được mở rộng linh hoạt: Trước khi tìm ra lời giải cuối cùng, có thể xảy ra trường hợp nhiều hơn một biến chỉ báo của cùng một biến gốc $Y$ đồng thời nhận giá trị đúng (tương ứng với việc $Y$ nhận nhiều giá trị), hoặc tất cả các biến chỉ báo đều nhận giá trị sai (tương ứng với việc $Y$ không nhận giá trị nào). Điều này giúp thuật toán dễ dàng thoát khỏi những điểm cực tiểu cục bộ vốn từng là rào cản trong không gian biểu diễn CSP gốc.
- Bài toán SAT đã được cộng đồng khoa học nghiên cứu sâu rộng hơn hầu hết các dạng CSP khác, dẫn đến sự ra đời của các bộ giải (SAT solvers) được tối ưu hóa cao độ.

Việc chuyển đổi một bài toán CSP cụ thể sang dạng bài toán thỏa mãn mệnh đề có làm tăng hiệu năng tìm kiếm hay không là một câu hỏi mang tính thực nghiệm, phụ thuộc vào đặc thù của từng bài toán và công cụ hỗ trợ hiện có.

## Tài liệu tham khảo

1. Poole, D. L., & Mackworth, A. K. (2023). *Artificial Intelligence: Foundations of Computational Agents* (3rd ed.). Chapter 5: Propositions and Inference. Cambridge University Press. Bản gốc trực tuyến: [ArtInt3e.Ch5.S2.html](https://artint.info/3e/html/ArtInt3e.Ch5.S2.html).
2. Davis, M., Logemann, G., & Loveland, D. (1962). A machine program for theorem-proving. *Communications of the ACM*, 5(7), 394–397.
3. Biere, A., Heule, M., van Maaren, H., & Walsh, T. (Eds.). (2009). *Handbook of Satisfiability*. IOS Press.
