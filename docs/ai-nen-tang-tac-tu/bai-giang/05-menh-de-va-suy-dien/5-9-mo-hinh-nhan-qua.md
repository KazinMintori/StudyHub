---
course: ai-nen-tang-tac-tu
lecture: 05-menh-de-va-suy-dien
section: topic
topic: 5-9-mo-hinh-nhan-qua
title: "5.9 Mô hình nhân quả"
description: "Mô hình nhân quả, can thiệp (intervention), phân biệt mô hình nhân quả với mô hình bằng chứng, và cơ chế cấu trúc nhân quả trong logic mệnh đề."
---

Một nguyên tử sơ cấp (primitive atom) là một nguyên tử được định nghĩa thông qua các sự kiện. Một nguyên tử dẫn xuất (derived atom) là một nguyên tử được định nghĩa thông qua các quy tắc suy diễn. Thông thường, người thiết kế xây dựng các tiên đề và quy tắc cho những nguyên tử dẫn xuất, sau đó kỳ vọng người dùng hoặc các cảm biến sẽ cung cấp trạng thái thực tế của các nguyên tử sơ cấp. Từ đó, các nguyên tử dẫn xuất sẽ được tự động suy ra khi cần thiết.

Người thiết kế cơ sở tri thức phải đưa ra nhiều quyết định mang tính cấu trúc:

Xét trường hợp đơn giản chỉ gồm hai mệnh đề $a$ và $b$, trong đó cả hai đều đúng. Có nhiều cách biểu diễn khác nhau:

- Khai báo cả $a$ và $b$ dưới dạng sự kiện nguyên tử độc lập (coi cả hai là sơ cấp).
- Khai báo sự kiện $a$ cùng quy tắc $b \leftarrow a$ (coi $a$ là sơ cấp và $b$ là dẫn xuất).
- Khai báo sự kiện $b$ cùng quy tắc $a \leftarrow b$ (coi $b$ là sơ cấp và $a$ là dẫn xuất).

Ba cách biểu diễn trên hoàn toàn tương đương nhau về mặt logic thuần túy (không thể phân biệt được bằng phép kiểm tra mô hình tĩnh). Tuy nhiên, chúng tạo ra những hệ quả hoàn toàn khác biệt khi cơ sở tri thức có sự biến động: Giả sử vì một lý do nào đó mà $a$ không còn đúng nữa:

- Trong cách biểu diễn thứ nhất và thứ ba, $b$ vẫn tiếp tục đúng.
- Nhưng trong cách biểu diễn thứ hai, $b$ sẽ lập tức trở thành sai.

## 5.9.1 Can thiệp và mô hình nhân quả

Một **mô hình nhân quả** (causal model) là một dạng biểu diễn miền bài toán có khả năng dự đoán chính xác kết quả của các hành động can thiệp.

Một **can thiệp** (intervention) là một hành động tác động trực tiếp nhằm ép buộc một biến phải nhận một giá trị xác định cụ thể, mà không phải thông qua các tác dụng phụ từ việc thao tác trên những biến khác trong mô hình. Khi một biến bị can thiệp, giá trị của nó thay đổi và có thể kéo theo sự thay đổi của các biến phụ thuộc khác.

Để dự đoán đúng đắn tác động của các can thiệp:

- Mô hình nhân quả biểu diễn theo chiều **từ nguyên nhân đến kết quả** (nguyên nhân kéo theo kết quả). Khi nguyên nhân bị thay đổi, kết quả của nó sẽ bị thay đổi tương ứng.
- Ngược lại, một **mô hình bằng chứng** (evidential model) biểu diễn miền bài toán theo chiều ngược lại: **Từ kết quả suy về nguyên nhân**.
- Lưu ý rằng chúng ta không giả định chỉ có duy nhất một "nguyên nhân đơn lẻ" cho một hiện tượng, mà có thể có một tập hợp nhiều mệnh đề cùng phối hợp để làm cho kết quả xuất hiện.

Một **mô hình nhân quả cấu trúc** (structural causal model) định nghĩa một cơ chế nhân quả cho từng nguyên tử được mô hình hóa. Cơ chế này quy định rõ nguyên tử đó trở nên đúng trong những điều kiện nào thông qua các nguyên tử khác. Nếu thế giới bị can thiệp để làm cho một nguyên tử trở thành đúng hoặc sai, thì các mệnh đề định nghĩa nguyên tử đó sẽ bị thay thế bằng một khẳng định trực tiếp rằng nguyên tử đó mang giá trị đúng hoặc sai tương ứng.

::: example Ví dụ 5.34: Bất đối xứng nhân quả trong hệ thống mạch điện
Trong môi trường mạch điện ở Hình 5.2, xét mối quan hệ giữa hai công tắc $s_{1}, s_{2}$ và bóng đèn $l_{1}$. Giả định rằng mọi linh kiện đều hoạt động hoàn hảo. Đèn $l_{1}$ sáng khi và chỉ khi cả hai công tắc cùng gạt lên hoặc cả hai cùng gạt xuống. Ta có công thức logic:

$$
\mathit{lit\_l}_{1} \leftrightarrow (\mathit{up\_s}_{1} \leftrightarrow \mathit{up\_s}_{2})
$$

Công thức này hoàn toàn tương đương logic với biểu thức:

$$
\mathit{up\_s}_{1} \leftrightarrow (\mathit{lit\_l}_{1} \leftrightarrow \mathit{up\_s}_{2}).
$$

Về mặt đại số logic, công thức này mang tính đối xứng hoàn toàn giữa ba mệnh đề: Nó nhận giá trị đúng khi và chỉ khi có một số lẻ các mệnh đề mang giá trị đúng.

Tuy nhiên, trong thế giới vật lý thực tế, mối quan hệ giữa các mệnh đề này mang tính **bất đối xứng nhân quả**:

- Giả sử ban đầu cả hai công tắc đều gạt lên và đèn đang sáng. Nếu ta gạt công tắc $s_{1}$ xuống, hành động này không thể làm công tắc $s_{2}$ tự động gạt xuống theo để giữ cho đèn sáng. Thay vào đó, việc gạt $s_{1}$ xuống sẽ làm cho đèn $l_{1}$ bị tắt ($\mathit{lit\_l}_{1}$ trở thành sai), trong khi công tắc $s_{2}$ vẫn giữ nguyên vị trí gạt lên ($\mathit{up\_s}_{2}$ vẫn đúng).
- Do đó, một công thức tương đương logic thuần túy là chưa đủ để dự đoán kết quả của các can thiệp. Ta bắt buộc phải thiết lập cơ chế định hướng nhân quả cho từng nguyên tử.

Trong mô hình nhân quả cấu trúc, ta biểu diễn chiều tác động tự nhiên bằng logic vị từ với phủ định như một thất bại:

<span class="logic-expression logic-block">lit_l_1 ← up_s_1 ∧ up_s_2. &#10;&#10;lit_l_1 ← ∼ up_s_1 ∧ ∼ up_s_2. &#10;&#10;up_s_1.</span>

Khi ta thực hiện một can thiệp lên công tắc, ta chỉ cần thay đổi các sự kiện khẳng định vị trí công tắc, và trạng thái bóng đèn sẽ tự động thích ứng chính xác. Nếu ta can thiệp để làm cho đèn tắt (chẳng hạn tháo bóng đèn ra hoặc đập vỡ bóng), ta thay thế các mệnh đề định nghĩa $\mathit{lit\_l}_{1}$ bằng khẳng định $\mathit{false}$; can thiệp này hoàn toàn không làm thay đổi vị trí của các công tắc.

Ngược lại, nếu sử dụng một mô hình bằng chứng:

<span class="logic-expression logic-block">up_s_1 ← lit_l_1 ∧ up_s_2. &#10;&#10;up_s_1 ← ∼ lit_l_1 ∧ ∼ up_s_2.</span>

Mô hình này có thể trả lời tốt câu hỏi suy đoán vị trí của $s_{1}$ khi biết trạng thái của đèn và công tắc $s_{2}$, nhưng nó sẽ đưa ra những dự đoán sai lầm hoàn toàn nếu ta can thiệp làm thay đổi trạng thái của đèn.
:::

Trong hầu hết các ứng dụng trí tuệ nhân tạo, việc xây dựng mô hình theo chiều nhân quả luôn được ưu tiên vượt trội, bởi vì mô hình nhân quả có tính minh bạch, ổn định và mô đun hóa cao hơn rất nhiều so với mô hình bằng chứng.

## Tài liệu tham khảo

1. Poole, D. L., & Mackworth, A. K. (2023). *Artificial Intelligence: Foundations of Computational Agents* (3rd ed.). Chapter 5: Propositions and Inference. Cambridge University Press.
2. Pearl, J. (2000). *Causality: Models, Reasoning, and Inference*. Cambridge University Press.
3. Spirtes, P., Glymour, C. N., & Scheines, R. (2000). *Causation, Prediction, and Search* (2nd ed.). MIT Press.


[Đọc mục tương ứng trong giáo trình](https://artint.info/3e/html/ArtInt3e.Ch5.S9.html).
