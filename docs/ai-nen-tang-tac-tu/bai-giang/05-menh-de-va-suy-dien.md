---
course: ai-nen-tang-tac-tu
lecture: 05-menh-de-va-suy-dien
section: lecture
title: "Mệnh đề và suy diễn"
prerequisites: []
lessonStatus: ready
description: "Mệnh đề logic, ngữ nghĩa, ràng buộc mệnh đề, suy diễn với mệnh đề xác định, chứng minh bằng phản chứng, giả thiết tri thức đầy đủ, suy luận giả thuyết và mô hình nhân quả."
---

> *Vì khi gặp một định lý sai, tôi không cần phải xem xét hay thậm chí tìm hiểu chứng minh của nó, bởi tôi sẽ phát hiện ra tính sai lầm của nó theo cách hậu nghiệm thông qua một thực nghiệm đơn giản, tức là bằng một phép tính chỉ tốn giấy mực, phép tính ấy sẽ chỉ ra sai sót dù là nhỏ nhất...*
>
> *Và nếu ai đó nghi ngờ các kết quả của tôi, tôi sẽ nói với người ấy: "Thưa ngài, chúng ta hãy cùng tính toán", và như vậy, bằng cách cầm bút và mực lên, chúng ta sẽ sớm giải quyết xong câu hỏi.*
>
> — Gottfried Wilhelm Leibniz (1677)

Chương học này xem xét các dạng thức suy luận đơn giản dựa trên mệnh đề, vốn là những phát biểu có thể đúng hoặc sai trong một thế giới cụ thể. Các dạng thức suy luận này bao gồm việc tìm mô hình, xác định hệ quả logic, cùng nhiều hình thức suy luận giả định khác nhau. Ngữ nghĩa logic đóng vai trò là nền tảng vững chắc cho việc đặc tả sự kiện, thực hiện suy diễn và gỡ lỗi tri thức trong các hệ thống tác tử thông minh.

## Mục tiêu học tập

Sau khi hoàn thành chương học này, người học có thể:

1. **Làm chủ cú pháp và ngữ nghĩa giải tích mệnh đề**: Định nghĩa chính xác nguyên tử, các liên từ logic, diễn giải, mô hình và quan hệ kéo theo logic.
2. **Biểu diễn bài toán dưới dạng ràng buộc mệnh đề**: Chuyển đổi và mô hình hóa mạng ràng buộc, bài toán lập lịch, cấu hình hệ thống bằng các biểu thức mệnh đề chuẩn.
3. **Thành thạo suy diễn với mệnh đề xác định**: Cài đặt và phân tích thuật toán suy diễn tiến từ dưới lên (bottom-up proof procedure) cùng thuật toán suy diễn lùi từ trên xuống (top-down proof procedure), nắm vững tính đúng đắn và tính đầy đủ.
4. **Vận dụng cơ chế hỏi người dùng và gỡ lỗi mức tri thức**: Tích hợp các nguyên tử khả vấn (askable), định vị lỗi sai sót hoặc thiếu sót trong cơ sở tri thức một cách có hệ thống.
5. **Nắm vững chứng minh bằng phản chứng và phân giải câu tuyển**: Áp dụng dạng chuẩn hội (CNF) và quy tắc phân giải tuyển (resolution refutation) để suy diễn trên logic mệnh đề tổng quát.
6. **Ứng dụng giả thiết tri thức đầy đủ, suy luận giả thuyết và mô hình nhân quả**: Phân tích phủ định như một thất bại (NAF), suy luận giả thuyết (abduction), giải thích chẩn đoán và cấu trúc đồ thị nhân quả của niềm tin.

<TopicMap />

## Bản đồ chương học

Chương học được tổ chức thành 13 chủ đề chi tiết, bám sát toàn diện cấu trúc nội dung học thuật:

- **5.1 Mệnh đề**: Cú pháp giải tích mệnh đề, ngữ nghĩa hình thức, diễn giải, chân trị, mô hình, quan hệ kéo theo logic cùng góc nhìn của con người và máy tính về ngữ nghĩa.
- **5.2 Ràng buộc mệnh đề**: Mô hình hóa mạng ràng buộc bằng logic mệnh đề, dạng chuẩn hội (CNF), bài toán SAT và quy trình chuyển đổi bài toán biến ngẫu nhiên/rời rạc sang mệnh đề.
- **5.3 Mệnh đề xác định**: Cú pháp mệnh đề xác định (Horn clauses), tri thức quy tắc, thuật toán chứng minh từ dưới lên (suy diễn tiến), tính đúng đắn, tính đầy đủ và thuật toán chứng minh từ trên xuống (suy diễn lùi).
- **5.4 Hỏi người dùng**: Tương tác hỏi đáp giữa hệ thống và người dùng, phân loại nguyên tử khả vấn, chiến lược hỏi tối ưu hóa thông tin và tính lười biếng trong truy vấn.
- **5.5 Gỡ lỗi ở mức tri thức**: Phương pháp luận gỡ lỗi tri thức logic, định vị nguyên tử sai dẫn đến kết luận sai, phát hiện quy tắc thiếu dẫn đến câu trả lời phủ định thất bại.
- **5.6 Chứng minh bằng phản chứng**: Dạng mệnh đề tổng quát, chuẩn tắc hội, quy tắc phân giải câu tuyển, thuật toán chứng minh bằng phản chứng và quan hệ tương đương với kiểm tra tính thỏa mãn.
- **5.7 Giả thiết tri thức đầy đủ**: Logic phi đơn điệu, giả thiết thế giới đóng (CWA), phủ định như một thất bại (negation as failure), ngữ nghĩa mô hình ổn định và phân tầng quy tắc.
- **5.8 Suy luận giả thuyết**: Bản chất của suy luận tìm giả thuyết tốt nhất (abduction), chẩn đoán lỗi hệ thống, giải thích quan sát và tính toán tập chẩn đoán tối tiểu.
- **5.9 Mô hình nhân quả**: Biểu diễn quan hệ nhân quả bằng mạng định hướng, suy luận thuận nhân quả và suy luận nghịch chẩn đoán, phân biệt tương quan với nhân quả.
- **5.10 Tác động xã hội**: Trách nhiệm giải trình của hệ thống lập luận biểu tượng, tính minh bạch của chuỗi suy diễn, đạo đức và rủi ro thiên vị trong cơ sở tri thức.
- **5.11 Ôn tập**: Tổng kết 11 điểm cốt lõi của chương, các quy trình chứng minh và các ứng dụng quan trọng.
- **5.12 Tài liệu tham khảo và đọc thêm**: Nguồn tài liệu học thuật kinh điển và các hướng nghiên cứu hiện đại về biểu diễn tri thức và suy diễn tự động.
- **5.13 Bài tập**: Hệ thống bài tập lý thuyết, chứng minh hình thức, giải thuật và bài toán suy luận thực tế.

## Tài liệu tham khảo

1. Poole, D. L., & Mackworth, A. K. (2023). *Artificial Intelligence: Foundations of Computational Agents* (3rd ed.). Cambridge University Press. Bản gốc trực tuyến: [ArtInt3e.Ch5.html](https://artint.info/3e/html/ArtInt3e.Ch5.html).
2. Leibniz, G. W. (1677). *Towards a Universal Characteristic*. In P. Wiener (Ed.), *Leibniz: Selections*. Charles Scribner's Sons, 1951.
3. Robinson, J. A. (1965). A machine-oriented logic based on the resolution principle. *Journal of the ACM*, 12(1), 23–41.
4. Lloyd, J. W. (1987). *Foundations of Logic Programming* (2nd ed.). Springer-Verlag.
5. Pearl, J. (2000). *Causality: Models, Reasoning, and Inference*. Cambridge University Press.
