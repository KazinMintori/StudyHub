---
course: xac-suat-thong-ke
lecture: 00-hieu-the-gioi-bang-du-lieu
section: lecture
title: "Hiểu thế giới bằng dữ liệu"
prerequisites: []
lessonStatus: ready
readingStyle: plain
description: "Bản dịch đầy đủ bài Understanding the World with Data của Stat 20, UC Berkeley, kèm giải thích và bài tập phân biệt mô tả, suy rộng, nhân quả và dự đoán."
---

“70% người trả lời khảo sát chưa từng lập trình” và “70% sinh viên của trường chưa từng lập trình” có cùng con số, nhưng nói về hai nhóm khác nhau. Dữ liệu nào cho phép ta đưa ra từng phát biểu? Bài mở đầu này giúp ta phân loại một phát biểu từ dữ liệu và chỉ ra điều cần kiểm tra trước khi tin vào kết luận.

Đây là bản dịch đầy đủ phần nội dung của [Understanding the World with Data — Stat 20, UC Berkeley, học kỳ xuân 2026](https://stat20.berkeley.edu/spring-2026/1-questions-and-data/01-understanding-the-world/notes.html). Mục 1–2 giữ lời giới thiệu, các định nghĩa và ví dụ của nguồn. Sơ đồ được vẽ lại với nhãn tiếng Việt. Mục 3–4 là phần giải thích và bài tập do StudyHub bổ sung. Bản gốc được phát hành theo [CC BY 4.0](https://stat20.berkeley.edu/spring-2026/license.html).

Bài không đòi hỏi kiến thức xác suất trước đó. Sau khi học, ta cần phân biệt được bốn loại phát biểu, xác định đúng nhóm đối tượng mà kết luận nói tới và giải thích vì sao một con số mô tả mẫu chưa tự cho phép kết luận về toàn trường.

## 1. Giới thiệu và đề cương khóa học

Chào mừng bạn đến với Stat 20! Chúng tôi rất vui được đón bạn trong học kỳ này. Nội dung hôm nay không có câu hỏi đọc bài. Tuy nhiên, đến cuối buổi học, hãy bảo đảm rằng bạn đã:

- Biết tên giảng viên và các trợ giảng hỗ trợ trong lớp.
- Đọc [đề cương khóa học](https://stat20.berkeley.edu/spring-2026/syllabus.html) và đăng các câu hỏi về đề cương vào luồng thảo luận [Ed](https://edstem.org/) tương ứng với lớp học của mình.
- Bắt đầu làm bài thực hành đầu tiên, và có thể đã nộp bài.

Mục tiêu của khóa học là xây dựng và phản biện các phát biểu dựa trên dữ liệu. Điều này đặt ra câu hỏi: ta có thể đưa ra những loại phát biểu nào?

::: info Bối cảnh của bản gốc
Lời chào, đề cương, Ed và bài thực hành ở trên thuộc khóa Stat 20 tại Berkeley. Chúng được giữ lại để bản dịch có đủ nội dung nguồn.
:::

## 2. Các loại phát biểu từ dữ liệu

Sơ đồ dưới đây đặt việc xây dựng và phản biện phát biểu từ dữ liệu ở trung tâm, rồi chia thành bốn loại nhiệm vụ. Các hình nhỏ minh họa từng nhiệm vụ, không biểu diễn một bộ số liệu cụ thể.

![Từ mục tiêu xây dựng và phản biện phát biểu dựa trên dữ liệu, sơ đồ chia thành bốn nhánh: mô tả dữ liệu đang có, suy rộng sang tập đối tượng lớn hơn, kết luận về tác động nhân quả và dự đoán giá trị chưa biết.](img/lec-00/cac-loai-phat-bieu.svg)

*Vẽ lại và dịch nhãn từ sơ đồ “Types of Claims” trong bài Stat 20 được dẫn ở đầu trang, theo CC BY 4.0.*

### 2.1. Mô tả dữ liệu

**Mô tả dữ liệu (Summary)** là việc mô tả một khía cạnh của dữ liệu đang có bằng con số, đồ thị hoặc lời văn.

**Ví dụ của nguồn:** Dựa trên dữ liệu khảo sát lớp Stat 20, tỷ lệ người trả lời khảo sát cho biết mình chưa có kinh nghiệm viết mã máy tính là 70%.

### 2.2. Suy rộng thống kê

**Suy rộng thống kê (Generalization)** là việc mô tả một tập đối tượng rộng hơn tập đã được ghi nhận dữ liệu, bằng con số, đồ thị hoặc lời văn.

**Ví dụ của nguồn:** Dựa trên dữ liệu khảo sát lớp Stat 20, tỷ lệ sinh viên Berkeley chưa có kinh nghiệm viết mã máy tính là 70%.

### 2.3. Kết luận nhân quả

**Kết luận nhân quả (Causal Claim)** là một phát biểu khẳng định rằng việc thay đổi giá trị của một biến sẽ ảnh hưởng đến giá trị của một biến khác.

**Ví dụ của nguồn:** Dữ liệu từ một thí nghiệm ngẫu nhiên có đối chứng cho thấy việc dùng một loại kháng sinh mới loại bỏ hơn 99% các ca nhiễm khuẩn.

### 2.4. Dự đoán

**Dự đoán (Prediction)** là việc đoán giá trị của một biến chưa biết dựa trên các biến khác đã biết.

**Ví dụ của nguồn:** Dựa trên tin tức đã đọc và giá cổ phiếu Uber hôm nay, tôi dự đoán rằng giá cổ phiếu Uber ngày mai sẽ tăng 1,2%.

Trong trang nguồn, mục “Other Links” dẫn tới [Slides của bài](https://stat20.berkeley.edu/spring-2026/1-questions-and-data/01-understanding-the-world/slides.html). Hai liên kết điều hướng là [Questions and Data](https://stat20.berkeley.edu/spring-2026/1-questions-and-data/notes.html) và bài tiếp theo [The Taxonomy of Data](https://stat20.berkeley.edu/spring-2026/1-questions-and-data/02-taxonomy-of-data/notes.html).

## 3. Giải thích bổ sung: phạm vi của một kết luận

Phần này do StudyHub bổ sung. Các con số về khảo sát, kháng sinh và cổ phiếu ở mục 2 được giữ đúng như ví dụ của Stat 20. Trang nguồn không cung cấp bộ dữ liệu khảo sát, tên thuốc, báo cáo thí nghiệm hay thời điểm dự đoán cổ phiếu. Vì vậy, ở đây ta dùng chúng để học cách phân loại phát biểu, không xem chúng là kết quả thực nghiệm đã được xác minh độc lập.

### 3.1. Mô tả mẫu và suy rộng về tổng thể

Xét một **ví dụ giả định**: muốn tìm hiểu kinh nghiệm lập trình của sinh viên UET, ta nhận được 10 câu trả lời khảo sát, trong đó 7 người cho biết chưa từng lập trình. Nhóm đã trả lời là mẫu thống kê, còn toàn bộ sinh viên UET là tổng thể mà ta muốn nghiên cứu.

::: example Tính tỷ lệ trong nhóm đã trả lời
Tỷ lệ người chưa từng lập trình trong nhóm trả lời bằng số người thuộc nhóm này chia cho tổng số người trả lời:

$$\frac{7}{10}\times 100\%=70\%.$$

Ta có thể mô tả: “Trong 10 người trả lời khảo sát, 70% cho biết chưa từng lập trình.” Mẫu số là 10 vì phát biểu nói về nhóm đã trả lời.
:::

Nếu viết “70% sinh viên UET chưa từng lập trình”, ta đã mở rộng phạm vi kết luận từ mẫu sang tổng thể. Phép chia vẫn đúng với dữ liệu mẫu, nhưng không chứng minh rằng tỷ lệ của toàn trường cũng bằng 70%.

Để đánh giá bước suy rộng, ta cần biết những người trả lời được chọn như thế nào, có nhóm sinh viên nào ít có cơ hội tham gia hay không và có ai được mời nhưng không trả lời. Chẳng hạn, nếu chỉ hỏi trong một câu lạc bộ lập trình, nhóm trả lời có thể khác toàn trường về chính đặc điểm đang nghiên cứu. Việc gọi một phát biểu là suy rộng chỉ xác định loại phát biểu, chưa chứng minh rằng nó có căn cứ.

::: tip Thử phân loại trước khi đọc đáp án
Chỉ thay cụm “10 người trả lời khảo sát” bằng “sinh viên UET” có làm thay đổi loại phát biểu không? Vì sao?
:::

<details><summary>Đáp án và lý do</summary>

Có. Phát biểu ban đầu mô tả nhóm đã được quan sát. Phát biểu sau nói về toàn bộ sinh viên UET, bao gồm những người chưa được quan sát, nên là suy rộng thống kê. Điều thay đổi là phạm vi đối tượng, không phải con số 70%.

</details>

### 3.2. Quan sát và can thiệp

Trong thống kê, một **biến** mô tả một đặc điểm có thể nhận các giá trị khác nhau giữa các đối tượng, chẳng hạn kinh nghiệm lập trình hoặc điểm bài thực hành. **Can thiệp** nghĩa là chủ động thay đổi một yếu tố để xem kết quả chịu tác động thế nào.

Giả sử ta quan sát thấy sinh viên tham gia câu lạc bộ lập trình có điểm bài thực hành cao hơn. Đây là mô tả một quan hệ trong dữ liệu đã quan sát. Nó chưa đủ để khẳng định rằng tham gia câu lạc bộ làm điểm tăng, vì những người tham gia có thể đã có nhiều kinh nghiệm hơn trước đó.

Phát biểu “việc tham gia câu lạc bộ làm điểm tăng” là kết luận nhân quả: nó nói về tác động của việc thay đổi một yếu tố. Muốn bảo vệ kết luận ấy, ta cần căn cứ để phân biệt tác động của việc tham gia với khác biệt có sẵn giữa các nhóm.

Ví dụ kháng sinh trong bản gốc nhắc đến **thí nghiệm ngẫu nhiên có đối chứng**. Trong một thiết kế như vậy, người tham gia được phân ngẫu nhiên vào các nhóm để so sánh nhóm nhận can thiệp với nhóm đối chứng. Cách phân nhóm giúp hạn chế việc các khác biệt có sẵn quyết định ai nhận can thiệp. Việc đọc kết quả vẫn cần xem thiết kế, cách đo và phạm vi đối tượng nghiên cứu. Bài mở đầu chỉ phân biệt loại câu hỏi, chưa trình bày phương pháp ước lượng tác động.

### 3.3. Giá trị chưa biết trong một bài toán dự đoán

Trong ví dụ Uber, tin tức và giá hôm nay là thông tin đã biết, còn mức thay đổi giá ngày mai là giá trị chưa biết. Cụm “ngày mai” thuộc tình huống minh họa của nguồn, không phải một dự báo tại thời điểm bạn đọc bài.

Một giá trị chưa biết cũng có thể đã tồn tại nhưng chưa được quan sát. Chẳng hạn, dùng thông tin đã biết về một sinh viên để đoán điểm của một bài đã chấm nhưng chưa được công bố vẫn là dự đoán.

Dự đoán không tự giải thích nguyên nhân của kết quả. Một thông tin giúp đoán điểm không nhất thiết là yếu tố mà ta có thể thay đổi để làm điểm tăng. Cũng như với suy rộng, phân loại đúng phát biểu chưa cho biết dự đoán chính xác đến đâu.

| Loại phát biểu | Câu hỏi cần xác định | Giới hạn khi đánh giá |
| --- | --- | --- |
| Mô tả dữ liệu | Dữ liệu đã có nói gì về nhóm đã quan sát? | Phải giữ đúng nhóm đối tượng và cách đo. |
| Suy rộng thống kê | Dữ liệu cho phép nói gì về nhóm rộng hơn? | Cần căn cứ cho bước đi từ mẫu sang tổng thể. |
| Kết luận nhân quả | Thay đổi một biến có ảnh hưởng đến biến khác không? | Quan hệ trong dữ liệu quan sát chưa tự chứng minh tác động. |
| Dự đoán | Giá trị chưa biết nào được đoán từ thông tin đã biết? | Một dự đoán cần được đánh giá về độ chính xác. |

## 4. Bài tập tự luyện

Các bài tập dưới đây do StudyHub biên soạn. Mọi số liệu là giả định.

### Bài 1. Nhận diện loại phát biểu

::: exercise
Với mỗi câu sau, hãy xác định loại phát biểu và nêu đặc điểm quyết định:

1. Trong nhóm đã trả lời khảo sát lớp học, 70% cho biết chưa từng lập trình.
2. Dùng khảo sát lớp học để kết luận rằng 70% sinh viên toàn trường chưa từng lập trình.
3. Tham gia câu lạc bộ lập trình làm điểm bài thực hành tăng.
4. Dựa trên kinh nghiệm lập trình đã biết, ta đoán điểm bài thực hành chưa công bố của một sinh viên.
:::

::: solution
1. Mô tả dữ liệu, vì câu chỉ nói về nhóm đã trả lời khảo sát.
2. Suy rộng thống kê, vì kết luận nói về toàn trường, rộng hơn nhóm đã quan sát.
3. Kết luận nhân quả, vì từ “làm” khẳng định tác động của việc tham gia đối với điểm.
4. Dự đoán, vì điểm chưa biết được đoán từ thông tin đã biết về kinh nghiệm.

Đây là phân loại ý nghĩa của từng câu. Nó chưa chứng minh rằng các câu 2–4 đúng hoặc được dữ liệu hỗ trợ.
:::

### Bài 2. Tính đúng tỷ lệ và giữ đúng phạm vi

::: exercise
Một khảo sát giả định nhận 20 câu trả lời, trong đó 14 người cho biết chưa từng lập trình. Hãy tính tỷ lệ, viết một câu mô tả đúng dữ liệu và giải thích vì sao chưa thể thay nhóm trả lời bằng toàn bộ sinh viên của trường.
:::

::: hint
Mẫu số phải là số người thực sự trả lời. Sau khi tính, kiểm tra xem chủ thể trong câu kết luận có đúng là nhóm ấy không.
:::

::: solution
Tỷ lệ trong nhóm trả lời là:

$$\frac{14}{20}\times 100\%=70\%.$$

Một câu mô tả đúng là: “Trong 20 người trả lời khảo sát, 70% cho biết chưa từng lập trình.” Nếu thay bằng toàn bộ sinh viên của trường, ta chuyển sang suy rộng. Đề bài chưa cho biết cách chọn mẫu và khả năng nhóm trả lời đại diện cho toàn trường, nên chưa đủ căn cứ cho kết luận ấy.
:::

### Bài 3. Tìm bước suy luận thiếu căn cứ

::: exercise
Một người lập luận: “Trong dữ liệu khảo sát, người tham gia câu lạc bộ có điểm cao hơn. Vì vậy, nếu buộc mọi người tham gia câu lạc bộ, điểm của họ sẽ tăng.” Hãy chỉ ra bước đầu tiên chưa được dữ liệu nêu trong đề hỗ trợ và đưa ra một cách giải thích khác cho quan sát ban đầu.
:::

::: solution
Bước thiếu căn cứ nằm ở việc chuyển từ khác biệt giữa hai nhóm đã quan sát sang tác động của một can thiệp. Quan sát ban đầu chưa cho biết điểm của cùng những người ấy sẽ thay đổi thế nào nếu họ tham gia.

Một cách giải thích khác là những sinh viên đã có nhiều kinh nghiệm lập trình vừa dễ tham gia câu lạc bộ hơn, vừa có thể đạt điểm cao hơn. Khả năng này cho thấy quan sát ban đầu chưa đủ chứng minh nhân quả. Nó cũng không chứng minh rằng việc tham gia hoàn toàn không có tác động.
:::

## 5. Nguồn và liên kết học tiếp

- **Nguồn của bản dịch:** Stat 20, UC Berkeley, *Understanding the World with Data*, học kỳ xuân 2026, hai mục “Intro and Syllabus” và “Types of Claims”. [Mở trang gốc](https://stat20.berkeley.edu/spring-2026/1-questions-and-data/01-understanding-the-world/notes.html).
- **Giấy phép:** [Thông báo giấy phép của Stat 20](https://stat20.berkeley.edu/spring-2026/license.html) và [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/). Bản dịch và sơ đồ được StudyHub chuyển sang tiếng Việt, có bổ sung giải thích và bài tập. Phần chuyển thể từ Stat 20 trên trang này được chia sẻ theo CC BY 4.0.
- **Tài liệu đi kèm của nguồn:** [Slides](https://stat20.berkeley.edu/spring-2026/1-questions-and-data/01-understanding-the-world/slides.html) và [đề cương](https://stat20.berkeley.edu/spring-2026/syllabus.html).
- **Đọc tiếp trên StudyHub:** [Xác suất có điều kiện và Bayes](/xac-suat-thong-ke/bai-giang/01-xac-suat-va-bayes.md).
