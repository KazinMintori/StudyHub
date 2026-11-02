---
course: ai-nen-tang-tac-tu
lecture: 05-menh-de-va-suy-dien
section: topic
topic: 5-5-go-loi-o-muc-tri-thuc
title: "5.5 Gỡ lỗi ở mức tri thức"
description: "Phương pháp luận gỡ lỗi cơ sở tri thức ở mức tri thức, thuật toán xử lý lỗi dương tính giả (câu trả lời sai) và lỗi âm tính giả (câu trả lời thiếu)."
---

Việc sử dụng ngữ nghĩa tường minh cho phép chúng ta thực hiện giải thích và gỡ lỗi trực tiếp ở mức tri thức (knowledge level). Để một hệ thống có thể được con người tin cậy sử dụng trong thực tế, nó không thể chỉ đưa ra câu trả lời đơn thuần và bắt người dùng phải chấp nhận một cách mù quáng. Hãy xem xét trường hợp một hệ thống trí tuệ nhân tạo hỗ trợ các bác sĩ, những người chịu trách nhiệm pháp lý trực tiếp đối với phác đồ điều trị mà họ chỉ định dựa trên kết quả chẩn đoán. Các bác sĩ bắt buộc phải được thuyết phục rằng kết luận chẩn đoán là hoàn toàn hợp lý. Hệ thống phải có khả năng biện minh cho tính đúng đắn của câu trả lời. Cơ chế giải thích chuỗi suy diễn cũng chính là công cụ đắc lực để phát hiện và khắc phục các sai sót trong cơ sở tri thức.

**Gỡ lỗi ở mức tri thức** là quá trình tìm kiếm sai sót trong cơ sở tri thức chỉ bằng cách đối chiếu ý nghĩa của các ký hiệu với sự thật trong thế giới thực, mà không cần phải can thiệp hay phân tích chi tiết các bước tính toán thuật toán phức tạp bên dưới.

Có ba dạng lỗi phi cú pháp điển hình thường gặp trong các hệ thống dựa trên quy tắc:

1. **Câu trả lời không chính xác (Lỗi dương tính giả)**: Hệ thống suy ra một nguyên tử mang giá trị sai trong diễn giải dự định.
2. **Câu trả lời bị bỏ sót (Lỗi âm tính giả)**: Quá trình chứng minh thất bại trên một nguyên tử thực sự đúng trong diễn giải dự định.
3. **Chương trình rơi vào vòng lặp vô hạn**: Lỗi này có thể được kiểm soát trong quy trình chứng minh từ trên xuống bằng kỹ thuật cắt tỉa chu trình (cycle pruning) trên các nguyên tử được chọn. Riêng quy trình chứng minh từ dưới lên hoàn toàn không bao giờ rơi vào vòng lặp vô hạn.

## 5.5.1 Câu trả lời không chính xác (Lỗi dương tính giả)

Một câu trả lời không chính xác (false-positive error) là một câu trả lời đã được chứng minh thành công bởi hệ thống nhưng lại mang giá trị sai trong diễn giải dự định thực tế.

Một quy trình chứng minh đúng đắn chỉ có thể sinh ra câu trả lời sai nếu trong quá trình suy diễn đã sử dụng ít nhất một mệnh đề bị sai sự thật. Mục tiêu của thuật toán gỡ lỗi là lần ngược chuỗi chứng minh để chỉ ra chính xác mệnh đề sai đó.

Giả sử nguyên tử $g$ đã được chứng minh nhưng lại bị sai trong diễn giải dự định. Khi đó, chắc chắn phải tồn tại một mệnh đề xác định $g \leftarrow a_{1} \wedge \dots \wedge a_{k}$ trong cơ sở tri thức được kích hoạt để suy ra $g$. Có hai khả năng xảy ra:

- Nếu toàn bộ các nguyên tử trong phần thân $a_{1}, \dots, a_{k}$ đều đúng trong diễn giải dự định, thì bản thân quy tắc này chính là nguyên nhân gây lỗi (vì phần thân đúng nhưng phần đầu lại sai). Mệnh đề lỗi đã được tìm thấy.
- Nếu tồn tại ít nhất một nguyên tử $a_{i}$ trong phần thân bị sai trong diễn giải dự định, thì sai sót bắt nguồn từ việc chứng minh $a_{i}$. Ta tiến hành đệ quy gỡ lỗi trên chính nguyên tử $a_{i}$ này.

```
Quy trình Debug_false(g, KB)
  Đầu vào:
    KB: Cơ sở tri thức
    g: Một nguyên tử sao cho KB |- g nhưng g bị SAI trong diễn giải dự định
  Đầu ra:
    Mệnh đề xác định trong KB bị sai sự thật

  1. Tìm mệnh đề xác định "g <- a_1 ^ ... ^ a_k" trong KB đã được dùng để chứng minh g
  2. Hiển thị quy tắc cho người dùng và hỏi xem từng a_i có đúng trong thực tế hay không
  3. Nếu người dùng xác định có một a_i bị sai:
  4.    Trả về Debug_false(a_i, KB)
  5. Ngược lại (nếu người dùng xác định tất cả a_i đều đúng):
  6.    Trả về mệnh đề "g <- a_1 ^ ... ^ a_k"
```

Hình 5.6: Thuật toán định vị mệnh đề sai khi gặp lỗi dương tính giả.

Thuật toán trong Hình 5.6 chỉ yêu cầu người dùng trả lời các câu hỏi đúng - sai đơn giản về các sự kiện thực tế trong miền chuyên môn, mà không đòi hỏi họ phải hiểu cấu trúc mã nguồn suy luận của hệ thống.

::: example Ví dụ 5.15: Định vị quy tắc lỗi trong hệ thống mạch điện
Xem xét lại môi trường mạch điện trong Ví dụ 5.8, nhưng giả định rằng cơ sở tri thức đã bị cài đặt sai sót do chuyên gia nhầm lẫn: Thay vì quy định dây $w_{1}$ nối với $w_{3}$ qua công tắc $s_{1}$, họ lại viết nhầm thành công tắc $s_{3}$. Cụ thể, cơ sở tri thức chứa quy tắc sai:

<span class="logic-expression logic-block">live_w_1 ← live_w_3 ∧ up_s_3.</span>

Các tiên đề khác đều giữ nguyên như trong Ví dụ 5.8. Khi người dùng truy vấn, hệ thống chứng minh được rằng $\mathit{lit\_l}_{1}$ là đúng, nhưng trong thực tế đèn $l_{1}$ đang tắt. Quá trình gỡ lỗi diễn ra từng bước:

1. Nguyên tử $\mathit{lit\_l}_{1}$ được suy ra từ quy tắc:
  
  <span class="logic-expression logic-block">lit_l_1 ← light_l_1 ∧ live_l_1 ∧ ok_l_1.</span>
   Người dùng xác nhận $\mathit{light\_l}_{1}$ và $\mathit{ok\_l}_{1}$ đều đúng, nhưng $\mathit{live\_l}_{1}$ bị sai.
2. Tiếp tục kiểm tra $\mathit{live\_l}_{1}$, nguyên tử này được suy ra từ quy tắc:
  
  $$
   \mathit{live\_l}_{1} \leftarrow \mathit{live\_w}_{0}.
  
  $$
   Người dùng xác nhận $\mathit{live\_w}_{0}$ bị sai.
3. Tiếp tục kiểm tra $\mathit{live\_w}_{0}$, nguyên tử này được suy ra từ quy tắc:
  
  <span class="logic-expression logic-block">live_w_0 ← up_s_2 ∧ live_w_1.</span>
   Người dùng xác nhận $\mathit{up\_s}_{2}$ đúng nhưng $\mathit{live\_w}_{1}$ bị sai.
4. Tiếp tục kiểm tra $\mathit{live\_w}_{1}$, nguyên tử này được suy ra từ quy tắc:
  
  <span class="logic-expression logic-block">live_w_1 ← up_s_3 ∧ live_w_3.</span>
   Người dùng xác nhận cả $\mathit{up\_s}_{3}$ và $\mathit{live\_w}_{3}$ đều thực sự đúng trong thực tế.

Tại thời điểm này, phần thân gồm $\mathit{up\_s}_{3} \wedge \mathit{live\_w}_{3}$ là đúng nhưng phần đầu $\mathit{live\_w}_{1}$ lại sai. Thuật toán kết luận chính xác rằng đây là quy tắc bị lỗi và trả về quy tắc này để người lập trình sửa lại.
:::

## 5.5.2 Câu trả lời bị bỏ sót (Lỗi âm tính giả)

Dạng lỗi thứ hai xuất hiện khi một câu trả lời đáng lẽ phải được khẳng định nhưng hệ thống lại trả về thất bại (false-negative error). Một nguyên tử $g$ đúng trong thế giới thực nhưng lại không thể chứng minh được từ cơ sở tri thức.

Một câu trả lời đúng không được sinh ra chỉ khi cơ sở tri thức bị thiếu mất một hoặc nhiều mệnh đề xác định cần thiết. Bằng cách nắm rõ diễn giải dự định và biết trước câu hỏi nào đáng lẽ phải thành công, chuyên gia có thể lần tìm nguyên nhân thiếu sót thông qua thuật toán trong Hình 5.7:

```
Quy trình Debug_missing(g, KB)
  Đầu vào:
    KB: Cơ sở tri thức
    g: Một nguyên tử sao cho KB |/- g nhưng g ĐÚNG trong diễn giải dự định
  Đầu ra:
    Nguyên tử đang bị thiếu mệnh đề xác định tương ứng

  1. Nếu tồn tại một mệnh đề xác định "g <- a_1 ^ ... ^ a_k" trong KB
     sao cho tất cả a_i đều ĐÚNG trong diễn giải dự định:
  2.    Chọn một a_i không thể chứng minh được từ KB
  3.    Trả về Debug_missing(a_i, KB)
  4. Ngược lại:
  5.    Trả về g (g chính là nguyên tử bị thiếu quy tắc hoặc sự kiện)
```

Hình 5.7: Thuật toán định vị nguyên tử bị thiếu quy tắc khi gặp lỗi âm tính giả.

Thuật toán duyệt qua không gian các nhánh chứng minh hợp lý cho đến khi cô lập được nguyên tử chưa hề có mệnh đề thích hợp nào trong cơ sở tri thức.

::: example Ví dụ 5.16: Định vị sự kiện bị thiếu trong hệ thống mạch điện
Giả sử trong môi trường mạch điện ở Ví dụ 5.8, công tắc $s_{2}$ trên thực tế đang gạt xuống, nhưng người lập trình quên không đưa sự kiện $\mathit{down\_s}_{2}$ vào cơ sở tri thức. Khi người dùng truy vấn $\mathbf{ask} \; \mathit{lit\_l}_{1}$, hệ thống trả lời **no** mặc dù đèn đang sáng.

Quá trình gỡ lỗi diễn ra như sau:

1. Xét quy tắc duy nhất có đầu là $\mathit{lit\_l}_{1}$:
  
  <span class="logic-expression logic-block">lit_l_1 ← light_l_1 ∧ live_l_1 ∧ ok_l_1.</span>
   Cả ba điều kiện đều đúng trong thực tế. Trong đó $\mathit{light\_l}_{1}$ và $\mathit{ok\_l}_{1}$ đều chứng minh được, chỉ riêng $\mathit{live\_l}_{1}$ thất bại. Thuật toán đệ quy gỡ lỗi cho $\mathit{live\_l}_{1}$.
2. Xét quy tắc duy nhất có đầu là $\mathit{live\_l}_{1}$:
  
  $$
   \mathit{live\_l}_{1} \leftarrow \mathit{live\_w}_{0}.
  
  $$
   Nguyên tử $\mathit{live\_w}_{0}$ đúng trong thực tế nhưng không chứng minh được.
3. Xét hai quy tắc có đầu là $\mathit{live\_w}_{0}$:
   <span class="logic-expression logic-block">live_w_0 ← live_w_1 ∧ up_s_2. &#10;&#10;live_w_0 ← live_w_2 ∧ down_s_2.</span>
   Chuyên gia xác định phần thân của quy tắc thứ hai là đúng trong thực tế. Trong quy tắc này, nguyên tử $\mathit{live\_w}_{2}$ đã có chứng minh thành công, nhưng $\mathit{down\_s}_{2}$ thì không thể chứng minh được vì không có quy tắc hay sự kiện nào có đầu là $\mathit{down\_s}_{2}$.

Thuật toán dừng lại và trả về nguyên tử $\mathit{down\_s}_{2}$. Biện pháp khắc phục là bổ sung sự kiện $\mathit{down\_s}_{2}.$ vào cơ sở tri thức.
:::

## Tài liệu tham khảo

1. Poole, D. L., & Mackworth, A. K. (2023). *Artificial Intelligence: Foundations of Computational Agents* (3rd ed.). Chapter 5: Propositions and Inference. Cambridge University Press.
2. Shapiro, E. Y. (1983). *Algorithmic Program Debugging*. MIT Press.
3. Davis, R. (1984). Diagnostic reasoning based on structure and behavior. *Artificial Intelligence*, 24(1–3), 347–410.


[Đọc mục tương ứng trong giáo trình](https://artint.info/3e/html/ArtInt3e.Ch5.S5.html).
