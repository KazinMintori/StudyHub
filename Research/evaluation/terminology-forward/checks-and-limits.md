# Tự rà và giới hạn

Các ghi nhận dưới đây là kiểm tra của người soạn đối với sáu output, không phải kết quả đánh giá việc học của sinh viên.

## Kiểm tra đã thực hiện

- Đọc SKILL.md và các reference: professor-voice.md, content-prompts.md, translation-vi.md, terminology-memory.json, pedagogy.md, writing-examples.md và teaching-review.md. Đối chiếu các mục thuật ngữ phù hợp với từng nguồn; không coi lựa chọn trong dữ liệu thuật ngữ là chuẩn duy nhất của mọi giáo trình.
- Tách lượt rà câu tiếng Việt khỏi lượt đối chiếu nghĩa. Rà đối tượng của từng câu, bước nối trong lập luận, ký hiệu mới, lượng từ, miền, dấu và phần bổ sung. Rà lại toàn bộ các file đã ghi bằng cách đọc văn bản.
- **A:** giữ \(\mathbb R\), khoảng cách \(|x-y|\), một \(c\) dùng chung cho mọi cặp và \(0\le c<1\). Kiểm tra đại số \(T(x)-T(y)=0.4(x-y)\); tính độc lập bằng PowerShell được điểm bất động 5, ảnh 5 và sai số thế lại 0. Không suy “một hằng số” thành “chỉ có duy nhất một hệ số co”. Không dùng định lý điểm bất động tổng quát để bỏ qua việc giải phương trình cụ thể.
- **B:** chọn “phép co tensor” theo ngữ cảnh chỉ số; ví dụ thêm ghi rõ cặp hàng–cột và phạm vi \(i=1,2\). Kiểm tra chỉ lấy \(A_{11},A_{22}\); PowerShell xác nhận \(1+4=5\). Không gán tính chất co khoảng cách cho phép co tensor.
- **C:** kiểm tra cả hai bất đẳng thức tại 0 bằng PowerShell, đều đúng. Giữ nguyên sự khác biệt ký hiệu \(x,z\), chỉ kết luận về \(z\) khi nêu giả định nó là tên của điểm đang kiểm tra. Giữ số 0 trong miền dấu của \(\nu\); phân biệt được phép về dấu với thỏa tất cả điều kiện của bài toán, và khả thi với tối ưu.
- **D:** kiểm tra chiều bất đẳng thức khi chuyển \(-x\le0\) thành \(x\ge0\); kiểm tra active là đẳng thức tại điểm đã nêu. Rà đạo hàm của \(x^2-\lambda x\), dấu trừ của \(\lambda\) và điều kiện \(\lambda\ge0\). PowerShell xác nhận giá trị ràng buộc tại 0 bằng 0, nhân tử suy ra bằng 0 và sai số phương trình dừng bằng 0. Kết luận tối ưu dùng \(x^2\ge0\), không coi điều kiện dừng riêng lẻ luôn đủ cho tối ưu.
- **E:** giữ trạng thái chưa xác định nghĩa của contraction; chỉ nêu hai cách hiểu có điều kiện và không gán chúng cho một chương chưa có nội dung. Không hỏi thêm người dùng.
- **F:** xác định ngữ cảnh ký kết giữa các bên; dịch contract là “hợp đồng”, giữ nghĩa quá khứ qua “đã”.

## Giới hạn

- Chỉ dùng các nguồn tự viết đã được giao và reference cục bộ của skill; không tra cứu ngoài. Các tài liệu nguồn của dữ liệu thuật ngữ không được kiểm chứng lại trên web trong lượt này.
- C chưa có ràng buộc đẳng thức cụ thể hay quan hệ giữa \(x\) và \(z\). E chưa có nội dung chương. Các giới hạn này được nêu ngay trong output tương ứng.
- Phép tính số được chạy bằng PowerShell; các bước đại số và suy luận còn lại được rà thủ công. Không chạy script rà ngôn ngữ, không tạo deck, không render và không thử nghiệm với sinh viên thật. Những kiểm tra đã làm không tự chứng nhận hiệu quả giảng dạy hay mức thành thạo của người đọc.
