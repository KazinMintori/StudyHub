---
course: ai-nen-tang-tac-tu
lecture: 05-menh-de-va-suy-dien
section: topic
topic: 5-8-suy-luan-quy-nap-dao
title: "5.8 Suy luận giả thuyết"
description: "Bản chất của suy luận giả thuyết (abduction), giải thích quan sát, chẩn đoán sự cố, hiện tượng giải thích triệt tiêu (explaining away) và ứng dụng trong thiết kế."
---

Suy luận giả thuyết (abduction) là một hình thức suy luận trong đó tác tử đưa ra các giả định hợp lý nhằm giải thích cho những dữ liệu quan sát được. Ví dụ: Nếu tác tử quan sát thấy một bóng đèn không sáng, nó sẽ đưa ra các giả thuyết về những gì đang diễn ra trong thế giới để giải thích nguyên nhân khiến bóng đèn bị tắt. Trong một hệ thống gia sư thông minh, tác tử có thể suy luận lý do học sinh đưa ra một câu trả lời cụ thể dựa trên những khái niệm mà học sinh đã hiểu hoặc chưa hiểu.

Thuật ngữ *abduction* được nhà triết học và logic học Charles Sanders Peirce (1839–1914) đề xuất nhằm phân biệt hình thức suy luận này với hai hình thức tư duy kinh điển:

- **Suy diễn (Deduction)**: Xác định những hệ quả logic bắt buộc phải đúng từ một tập hợp các tiền đề.
- **Quy nạp (Induction)**: Rút ra các mối quan hệ và quy luật tổng quát từ tập hợp các trường hợp quan sát cụ thể.
- **Suy luận giả thuyết (Abduction)**: Đưa ra giả thuyết hợp lý về nguyên nhân tiềm ẩn của một trường hợp quan sát cụ thể.

Trong suy luận giả thuyết, tác tử tìm kiếm những giả định kéo theo được các quan sát, tức là điều gì có thể đúng để làm cho các quan sát trở thành sự thật. Vì mâu thuẫn ($\mathit{false}$) có thể kéo theo mọi mệnh đề một cách tầm thường, ta bắt buộc phải loại bỏ các mâu thuẫn ra khỏi tập các lời giải thích hợp lệ.

## 5.8.1 Khung hình thức của suy luận giả thuyết

Để hình thức hóa suy luận giả thuyết, ta sử dụng ngôn ngữ các mệnh đề Horn kết hợp với các nguyên tử khả giả định. Hệ thống được cung cấp:

- Một cơ sở tri thức $\mathit{KB}$ gồm tập hợp các mệnh đề Horn.
- Một tập hợp $A$ chứa các nguyên tử khả giả định (assumables), đóng vai trò là các thành phần cơ sở để xây dựng nên các giả thuyết.

Thay vì nạp các dữ liệu quan sát trực tiếp vào cơ sở tri thức, các quan sát được xem là mục tiêu cần được giải thích.

Một **kịch bản** (scenario) của cặp $\langle \mathit{KB}, A \rangle$ là một tập con $H \subseteq A$ sao cho $\mathit{KB} \cup H$ là thỏa mãn được. Hệ thống $\mathit{KB} \cup H$ thỏa mãn được khi tồn tại một mô hình mà trong đó mọi mệnh đề của $\mathit{KB}$ và mọi nguyên tử của $H$ đều đồng thời đúng. Điều này tương đương với điều kiện không có tập con nào của $H$ là một xung đột của $\mathit{KB}$.

Một **lời giải thích** (explanation) cho mệnh đề quan sát $g$ từ $\langle \mathit{KB}, A \rangle$ là một kịch bản $H \subseteq A$ sao cho:

$$
\begin{aligned}
&\mathit{KB} \cup H \models g, \\
&\mathit{KB} \cup H \not\models \mathit{false}.
\end{aligned}
$$

Một **lời giải thích tối tiểu** (minimal explanation) cho $g$ từ $\langle \mathit{KB}, A \rangle$ là một lời giải thích $H$ sao cho không có bất kỳ tập con thực sự nào của $H$ cũng là một lời giải thích cho $g$.

Cần lưu ý rằng một lời giải thích giả thuyết không được bảo đảm là sự thật hiển nhiên hay chân lý chắc chắn trong thế giới thực. Đó chỉ là một giả định hoặc kịch bản giả thuyết hợp lý có khả năng giải thích cho các dữ liệu quan sát được và nhất quán với tri thức hiện có.

::: example Ví dụ 5.31: Chẩn đoán y khoa bằng suy luận giả thuyết
Xem xét cơ sở tri thức đơn giản sau cho một hệ thống trợ lý chẩn đoán:

<span class="logic-expression logic-block">bronchitis ← influenza. &#10;&#10;bronchitis ← smokes. &#10;&#10;coughing ← bronchitis. &#10;&#10;wheezing ← bronchitis. &#10;&#10;fever ← influenza. &#10;&#10;fever ← infection. &#10;&#10;sore_throat ← influenza. &#10;&#10;false ← smokes ∧ nonsmoker. &#10;&#10;assumable   smokes, nonsmoker, influenza, infection.</span>

1. Nếu bệnh nhân có triệu chứng thở khò khè ($\mathit{wheezing}$), có hai lời giải thích tối tiểu độc lập:
  
  $$
   \{\mathit{influenza}\} \quad \text{và} \quad \{\mathit{smokes}\}.
  
  $$
   Cả hai giả thuyết này đều giải thích được chứng viêm phế quản ($\mathit{bronchitis}$) và ho ($\mathit{coughing}$).
2. Nếu quan sát thấy bệnh nhân vừa thở khò khè vừa sốt ($\mathit{wheezing} \wedge \mathit{fever}$), các lời giải thích tối tiểu là:
  
  <span class="logic-expression logic-block">{influenza}   và   {smokes, infection}.</span>
   Giả thuyết cúm ($\mathit{influenza}$) là một lời giải thích duy nhất bao quát được cả hai triệu chứng, trong khi nếu do hút thuốc thì bắt buộc phải kết hợp thêm với giả thuyết nhiễm trùng ($\mathit{infection}$) để giải thích triệu chứng sốt.
3. Nếu quan sát thấy bệnh nhân thở khò khè nhưng lại không hút thuốc ($\mathit{wheezing} \wedge \mathit{nonsmoker}$), ta chỉ còn duy nhất một lời giải thích tối tiểu:
  
  $$
   \{\mathit{influenza}, \mathit{nonsmoker}\}.
  
  $$
   Lời giải thích còn lại $\{\mathit{smokes}\}$ bị loại bỏ hoàn toàn do mâu thuẫn với ràng buộc toàn vẹn của người không hút thuốc.
:::

::: example Ví dụ 5.32: Hiện tượng giải thích triệt tiêu (Explaining Away)
Xét cơ sở tri thức về hệ thống chuông báo cháy:

$$
\begin{aligned}
&\mathit{alarm} \leftarrow \mathit{tampering}. \\
&\mathit{alarm} \leftarrow \mathit{fire}. \\
&\mathit{smoke} \leftarrow \mathit{fire}.
\end{aligned}
$$

Nếu chỉ quan sát thấy chuông báo động reo ($\mathit{alarm}$), có hai lời giải thích cạnh tranh:

$$
\{\mathit{tampering}\} \quad \text{và} \quad \{\mathit{fire}\}.
$$

Tuy nhiên, nếu sau đó quan sát thấy có thêm khói ($\mathit{alarm} \wedge \mathit{smoke}$), lời giải thích tối tiểu duy nhất còn lại là:

$$
\{\mathit{fire}\}.
$$

Sự xuất hiện của quan sát khói đã giải thích hoàn toàn cho hiện tượng chuông báo động, từ đó triệt tiêu nhu cầu phải giả định thêm khả năng có người can thiệp phá hoại ($\mathit{tampering}$). Đây chính là hiệu ứng **giải thích triệt tiêu** (explaining away).
:::

## 5.8.2 So sánh chẩn đoán giả thuyết và chẩn đoán dựa trên tính nhất quán

Chẩn đoán giả thuyết (abductive diagnosis) và chẩn đoán dựa trên tính nhất quán (consistency-based diagnosis - CBD) là hai phương pháp luận chẩn đoán kinh điển nhưng có các điểm khác biệt bản chất:

- **Về mô hình hóa hành vi**: Trong CBD, người lập trình chỉ cần mô hình hóa hành vi hoạt động bình thường của hệ thống, và các giả thuyết là những giả định về trạng thái bình thường ($\mathit{ok}$). Trong chẩn đoán giả thuyết, ta bắt buộc phải mô hình hóa chi tiết cả hành vi bình thường lẫn cơ chế gây lỗi của từng dạng hỏng hóc, và tập các nguyên tử khả giả định phải bao gồm cả trạng thái bình thường lẫn từng dạng lỗi cụ thể.
- **Về vai trò của quan sát**: Trong chẩn đoán giả thuyết, các quan sát đóng vai trò là mục tiêu cần được chứng minh suy ra từ giả định. Trong CBD, các quan sát được nạp thẳng vào cơ sở tri thức như những sự kiện hiển nhiên, và thuật toán tìm cách chứng minh mâu thuẫn ($\mathit{false}$).

Chẩn đoán giả thuyết đòi hỏi công sức mô hình hóa chi tiết hơn nhưng mang lại kết luận chẩn đoán cụ thể và sâu sắc hơn. Ngoài ra, chẩn đoán giả thuyết có thể áp dụng cho các hệ thống không hề có khái niệm "trạng thái bình thường danh định", chẳng hạn như việc suy đoán mô hình nhận thức của học sinh trong các tác tử dạy học thông minh.

Hơn nữa, suy luận giả thuyết còn được ứng dụng rất hiệu quả trong bài toán thiết kế: Khi đó câu truy vấn cần giải thích chính là mục tiêu thiết kế (design goal), các nguyên tử khả giả định là các linh kiện cấu thành, và lời giải thích tìm được chính là bản thiết kế hoàn chỉnh đáp ứng mục tiêu.

::: example Ví dụ 5.33: Mô hình hóa suy luận giả thuyết cho hệ thống mạch điện
Trong môi trường mạch điện ở Hình 5.2, để thực hiện chẩn đoán giả thuyết, ta phải tiên đề hóa tường minh cả hai chiều hoạt động:

$$
\begin{aligned}
&\mathit{lit\_l}_{1} \leftarrow \mathit{live\_w}_{0} \wedge \mathit{ok\_l}_{1}. \\
&\mathit{dark\_l}_{1} \leftarrow \mathit{broken\_l}_{1}. \\
&\mathit{dark\_l}_{1} \leftarrow \mathit{dead\_w}_{0}. \\
&\mathbf{assumable} \; \mathit{ok\_l}_{1}, \mathit{broken\_l}_{1}. \\
&\mathit{false} \leftarrow \mathit{ok\_l}_{1} \wedge \mathit{broken\_l}_{1}.
\end{aligned}
$$

Khi người dùng quan sát thấy đèn $l_{1}$ bị tối ($\mathit{dark\_l}_{1}$), quy trình suy luận giả thuyết sẽ tìm kiếm các kịch bản tối tiểu giải thích trực tiếp cho sự kiện này (chẳng hạn $\{\mathit{broken\_l}_{1}\}$ hoặc các kịch bản dẫn đến mất điện dây $w_{0}$).
:::

Cả hai thuật toán suy diễn tiến (ATMS trong Hình 5.9) lẫn suy diễn lùi (Hình 5.10) đều được áp dụng trực tiếp cho suy luận giả thuyết. Trong thuật toán từ dưới lên, tập $C$ sau khi kết thúc vòng lặp sẽ lưu trữ sẵn toàn bộ các lời giải thích tối tiểu cho từng nguyên tử. Trong thuật toán từ trên xuống, ta tìm các lời giải thích cho truy vấn $g$ bằng cách thay thế mục tiêu ban đầu $\mathit{false}$ bằng chính nguyên tử $g$ và thu thập các nguyên tử khả giả định cần thiết sao cho không chứa bất kỳ xung đột nào.

## Tài liệu tham khảo

1. Poole, D. L., & Mackworth, A. K. (2023). *Artificial Intelligence: Foundations of Computational Agents* (3rd ed.). Chapter 5: Propositions and Inference. Cambridge University Press. Bản gốc trực tuyến: [ArtInt3e.Ch5.S8.html](https://artint.info/3e/html/ArtInt3e.Ch5.S8.html).
2. Peirce, C. S. (1931–1958). *Collected Papers of Charles Sanders Peirce*. Harvard University Press.
3. Poole, D. (1988). A logical framework for default reasoning. *Artificial Intelligence*, 36(1), 27–47.
4. Console, L., & Torasso, P. (1991). A spectrum of logical definitions of model-based diagnosis. *Computational Intelligence*, 7(3), 133–141.
