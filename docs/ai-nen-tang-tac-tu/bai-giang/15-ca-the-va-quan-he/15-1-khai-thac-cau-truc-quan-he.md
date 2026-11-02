---
course: ai-nen-tang-tac-tu
lecture: 15-ca-the-va-quan-he
section: topic
topic: 15-1-khai-thac-cau-truc-quan-he
title: "15.1 Khai thác cấu trúc quan hệ"
description: "Phân tích động lực chuyển từ biểu diễn đặc trưng sang cá thể và quan hệ, cùng những ưu thế của biểu diễn quan hệ trong trí tuệ nhân tạo."
---

Một trong những bài học quan trọng nhất của trí tuệ nhân tạo là: Các tác tử thành công luôn biết cách khai thác cấu trúc của thế giới thực.

Trong các chương trước, trạng thái của môi trường được biểu diễn, học tập và suy luận chủ yếu thông qua các biến trạng thái hoặc đặc trưng (features). Biểu diễn miền bài toán bằng đặc trưng cô đọng hơn rất nhiều so với việc biểu diễn tường minh từng trạng thái riêng lẻ, và những thuật toán khai thác được tính cô đọng này đạt hiệu quả tính toán cao hơn. Tuy nhiên, ngoài các đặc trưng, thế giới thực thường chứa đựng nhiều cấu trúc phong phú hơn mà ta có thể khai thác để biểu diễn và suy luận. Cụ thể, chương học này xem xét việc suy luận dựa trên các cá thể và mối quan hệ giữa chúng:

- **Cá thể (Individuals)**: Là những thực thể tồn tại trong thế giới, dù đó là cá thể cụ thể như con người và tòa nhà, cá thể tưởng tượng như kỳ lân và chương trình có thể vượt qua phép thử Turing một cách đáng tin cậy, các tiến trình như đọc một cuốn sách hay đi nghỉ mát, hoặc các khái niệm trừu tượng như tiền tệ, một môn học (chẳng hạn môn MCS-224 tại một trường đại học cụ thể), một học kỳ của môn học (chẳng hạn học kỳ mùa xuân năm 2026 của môn MCS-224), và các mốc thời gian. Cá thể còn được gọi bằng các thuật ngữ tương đương như thực thể (entities), đối tượng (objects) hoặc sự vật (things).
- **Quan hệ (Relations)**: Xác định những điều đúng đắn về các cá thể này. Khái niệm quan hệ được hiểu theo nghĩa tổng quát nhất có thể: Bao gồm quan hệ một ngôi (unary relations) phản ánh tính chất đúng hoặc sai của từng cá thể đơn lẻ; các mệnh đề logic (propositions) có giá trị chân lý đúng hoặc sai độc lập với mọi cá thể; cũng như các mối quan hệ liên kết nhiều cá thể với nhau.

::: example Ví dụ 15.1: Cấu trúc hóa miền bài toán mạch điện
Trong cách biểu diễn miền mạch điện ở [Ví dụ 5.8](https://artint.info/3e/html/ArtInt3e.Ch5.S3.html#Ch5.Thmciexamplered8), các mệnh đề như $up\_s_{2}$, $up\_s_{3}$ và $ok\_s_{2}$ hoàn toàn không có cấu trúc nội tại:

- Không có khái niệm nào thể hiện rằng các mệnh đề $up\_s_{2}$ và $up\_s_{3}$ cùng nói về một mối quan hệ (công tắc đang ở vị trí bật lên) nhưng áp dụng cho hai cá thể khác nhau.
- Tương tự, cũng không có khái niệm nào cho thấy $up\_s_{2}$ và $ok\_s_{2}$ cùng nói về một công tắc duy nhất. Khi đó hoàn toàn vắng bóng khái niệm về cá thể và quan hệ.

Một cách tiếp cận thay thế là biểu diễn tường minh các cá thể công tắc $s_{1}$, $s_{2}$, $s_{3}$, cùng các thuộc tính $up$ và $ok$. Sử dụng cách biểu diễn này, mệnh đề "công tắc $s_{2}$ đang bật lên" được biểu diễn dưới dạng:

$$
up(s_{2})
$$

Bằng cách hiểu ý nghĩa của $up$ và $s_{1}$, tác tử không cần một định nghĩa riêng biệt nào cho $up(s_{1})$. Một quan hệ hai ngôi như $connected\_to$ có thể được dùng để liên kết hai cá thể, chẳng hạn:

$$
connected\_to(w_{1}, s_{1})
$$
:::

## Những ưu thế của biểu diễn quan hệ

Việc mô hình hóa theo cá thể và quan hệ mang lại nhiều ưu thế so với việc chỉ dùng thuần túy các đặc trưng:

### 1. Tính tự nhiên của biểu diễn

Đây thường là cách biểu diễn tự nhiên. Thông thường các đặc trưng vốn là thuộc tính của các cá thể, và cấu trúc nội tại này sẽ bị mất đi khi ta chuyển đổi bài toán sang các đặc trưng phẳng.

### 2. Khả năng mô hình hóa khi chưa biết trước số lượng cá thể

Một tác tử có thể phải mô hình hóa một miền bài toán mà không biết trước các cá thể là gì, hoặc có bao nhiêu cá thể, do đó không biết trước các đặc trưng cụ thể là gì. Khi tương tác với môi trường, tác tử có thể tự kiến tạo các đặc trưng ngay khi phát hiện những cá thể nào đang hiện diện trong môi trường cụ thể đó.

### 3. Khả năng suy luận trừu tượng không phụ thuộc cá thể cụ thể

Tác tử có thể thực hiện một số bước suy luận mà không cần quan tâm đến các cá thể cụ thể:

- Tác tử có thể suy ra rằng một điều gì đó đúng cho mọi cá thể mà không cần định danh từng cá thể riêng lẻ.
- Tác tử có thể suy ra rằng tồn tại một cá thể nào đó thỏa mãn một số tính chất mà không cần bận tâm đến những cá thể khác.
- Có những câu hỏi truy vấn mà tác tử có thể trả lời mà không cần phân biệt danh tính các cá thể. Ví dụ: Một robot hút bụi có thể suy ra rằng có ai đó hoặc vật gì đó đã làm bẩn sàn nhà, mà không cần biết chính xác thực thể nào đã gây ra.

### 4. Xử lý sự tồn tại bất định của cá thể

Sự tồn tại của các cá thể có thể phụ thuộc vào hành động của tác tử hoặc mang tính bất định. Ví dụ trong bài toán lập kế hoạch sản xuất: Liệu có một linh kiện hoạt động tốt hay không có thể phụ thuộc vào việc nhiều linh kiện con khác hoạt động tốt và được lắp ráp chính xác; một số công đoạn có thể phụ thuộc vào hành động của tác tử, và một số công đoạn khác có thể nằm ngoài tầm kiểm soát của tác tử. Do đó, một tác tử có thể phải hành động mà không biết những đặc trưng nào đang tồn tại hoặc sẽ tồn tại.

### 5. Khả năng xử lý miền đối tượng vô hạn

Thông thường, số lượng cá thể mà một tác tử suy luận là vô hạn, kéo theo số lượng đặc trưng tiềm năng là vô hạn:

- Ví dụ: Nếu các cá thể là các câu văn, tác tử có thể chỉ cần suy luận trên một tập hợp rất hạn chế các câu (chẳng hạn các câu mà một người đang nói có thể muốn truyền đạt, hoặc các câu hợp lý để tác tử sinh ra), mặc dù số lượng câu văn khả dĩ trong ngôn ngữ là vô hạn, và do đó số lượng đặc trưng là vô hạn.

## Tài liệu tham khảo

1. Poole, D. L., & Mackworth, A. K. (2023). *Artificial Intelligence: Foundations of Computational Agents* (3rd ed.). Cambridge University Press. Nguồn trực tuyến: [https://artint.info/3e/html/ArtInt3e.Ch15.S1.html](https://artint.info/3e/html/ArtInt3e.Ch15.S1.html).
