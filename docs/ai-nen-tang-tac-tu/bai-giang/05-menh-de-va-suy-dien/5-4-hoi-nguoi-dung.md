---
course: ai-nen-tang-tac-tu
lecture: 05-menh-de-va-suy-dien
section: topic
topic: 5-4-hoi-nguoi-dung
title: "5.4 Hỏi người dùng"
description: "Cơ chế hỏi người dùng trong suy diễn logic, nguyên tử khả vấn (askable), thu thập quan sát thời gian thực và tích hợp với thuật toán suy diễn lùi."
---

Một tác tử nhận thông tin từ hai nguồn chính: Tri thức nền được nạp từ trước và các dữ liệu quan sát trực tuyến trong quá trình vận hành. Một quan sát là thông tin nhận được trực tuyến từ người dùng, từ các cảm biến hoặc từ những nguồn tri thức khác. Về mặt biểu diễn, một quan sát thường là một tập hợp các mệnh đề nguyên tử được ngầm định liên kết bằng phép hội.

Người dùng là người cần đến chuyên môn của hệ thống hoặc nắm giữ thông tin cụ thể về một tình huống thực tế cá biệt. Chúng ta không thể kỳ vọng người dùng chủ động cung cấp mọi sự thật về thế giới ngay từ đầu, bởi hai lý do căn bản:

- Người dùng không thể biết trước thông tin nào là thực sự liên quan đến mục tiêu suy diễn của hệ thống.
- Người dùng không nắm được hệ thống thuật ngữ hoặc từ vựng hình thức mà cơ sở tri thức đang sử dụng.

Một bản thể luận (ontology) đặc tả ý nghĩa chuẩn của các ký hiệu, hoặc một giao diện đồ họa cho phép người dùng nhấp chọn những sự kiện đúng, có thể giúp giải quyết bài toán về rào cản thuật ngữ. Tuy nhiên, số lượng các sự kiện đúng tiềm năng là quá lớn để người dùng có thể khai báo toàn bộ, ngay cả khi có giao diện hỗ trợ hiện đại. Do đó, hệ thống bắt buộc phải chủ động định hướng để người dùng chỉ cần cung cấp những thông tin thực sự hữu ích cho bài toán. Tương tự, các cảm biến thụ động có thể liên tục ghi nhận các chuỗi quan sát, nhưng đối với các cảm biến chủ động, tác tử cần phải chủ động truy vấn khi nhận thấy thông tin đó là cần thiết cho nhiệm vụ.

## 5.4.1 Cơ chế nguyên tử khả vấn

Một giải pháp đơn giản và hiệu quả để thu nhận thông tin từ người dùng hoặc từ cảm biến chủ động là tích hợp cơ chế hỏi người dùng (ask-the-user mechanism). Trong cơ chế này, một nguyên tử được đánh dấu là **khả vấn** (askable) nếu người dùng có thể biết được giá trị chân lý của nó tại thời điểm chạy, hoặc nguyên tử đó có thể đo đạc được bằng một cảm biến chủ động.

Quy trình chứng minh từ trên xuống (suy diễn lùi) được tích hợp tự nhiên với cơ chế này:

1. Khi thuật toán chọn một nguyên tử mục tiêu phụ để chứng minh, trước hết nó kiểm tra xem có quy tắc nào trong cơ sở tri thức có thể dùng để suy ra nguyên tử này hay không.
2. Nếu không có quy tắc, hoặc nếu nguyên tử này được khai báo là khả vấn và chưa từng được hỏi trước đó, hệ thống sẽ tạm dừng để đặt câu hỏi cho người dùng hoặc kích hoạt cảm biến chủ động để xác định xem nguyên tử đó là đúng hay sai.
3. Người dùng nhờ đó chỉ bị hỏi về những nguyên tử thực sự có liên quan trực tiếp đến chuỗi suy diễn dẫn tới câu trả lời của truy vấn hiện tại.

Quy trình chứng minh từ dưới lên cũng có thể được điều chỉnh để tương tác với người dùng, nhưng cần có chiến lược điều phối thông minh nhằm tránh việc hỏi tràn lan toàn bộ các nguyên tử khả vấn trong cơ sở tri thức.

::: example Ví dụ 5.14: Đối thoại hỏi đáp trong miền bài toán mạch điện
Trong môi trường mạch điện ở Ví dụ 5.8, người thiết kế mô hình hệ thống dây dẫn trong nhà không thể biết trước trạng thái đóng ngắt của các công tắc tại một thời điểm cụ thể bất kỳ. Vì vậy, người thiết kế sẽ cung cấp toàn bộ các mệnh đề xác định về cấu trúc mạch điện, ngoại trừ vị trí các công tắc. Thay vào đó, các mệnh đề về trạng thái công tắc (chẳng hạn $\mathit{up\_s}_{1}$, $\mathit{down\_s}_{1}$, $\mathit{up\_s}_{2}$, $\mathit{down\_s}_{2}$, $\mathit{up\_s}_{3}$, $\mathit{down\_s}_{3}$) được thiết lập là các nguyên tử khả vấn.

Dưới đây là một đoạn hội thoại tương tác mẫu giữa người dùng và hệ thống khi người dùng đưa ra câu hỏi truy vấn:

> **Người dùng**: $\mathbf{ask} \; \mathit{lit\_l}_{1}.$ (Đèn 1 có đang sáng hay không?)
>
> **Hệ thống**: $\mathit{down\_s}_{2}$ có đúng không? (Công tắc $s_{2}$ có đang gạt xuống không?)
>
> **Người dùng**: Không (no).
>
> **Hệ thống**: $\mathit{up\_s}_{2}$ có đúng không? (Công tắc $s_{2}$ có đang gạt lên không?)
>
> **Người dùng**: Đúng (yes).
>
> **Hệ thống**: $\mathit{up\_s}_{1}$ có đúng không? (Công tắc $s_{1}$ có đang gạt lên không?)
>
> **Người dùng**: Đúng (yes).
>
> **Hệ thống**: Kết quả: $\mathit{True}$ (Đèn 1 đang sáng).

Hệ thống chỉ hỏi người dùng những câu hỏi mà người dùng hoàn toàn có khả năng quan sát và trả lời trực tiếp, đồng thời các câu hỏi đó đều nằm trên nhánh suy diễn liên quan trực tiếp đến câu hỏi truy vấn ban đầu.
:::

## Tài liệu tham khảo

1. Poole, D. L., & Mackworth, A. K. (2023). *Artificial Intelligence: Foundations of Computational Agents* (3rd ed.). Chapter 5: Propositions and Inference. Cambridge University Press.
2. Shortliffe, E. H. (1976). *Computer-Based Medical Consultations: MYCIN*. Elsevier.
3. Buchanan, B. G., & Shortliffe, E. H. (Eds.). (1984). *Rule-Based Expert Systems: The MYCIN Experiments of the Stanford Heuristic Programming Project*. Addison-Wesley.


[Đọc mục tương ứng trong giáo trình](https://artint.info/3e/html/ArtInt3e.Ch5.S4.html).
