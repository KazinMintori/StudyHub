---
section: wiki
concept: dong-nhat-hoa
title: "Đồng nhất hóa và MGU"
---

## Giải thích kỹ thuật

Thuật toán hợp nhất vận hành trên cây cú pháp của hai biểu thức. Trong quá trình duyệt, khi gặp một biến chưa được gán, thuật toán phải xác minh xem biến đó có nằm trong hạng thức đối ứng hay không.

Nếu biến xuất hiện trong hạng thức, việc gán giá trị sẽ dẫn đến một cấu trúc đệ quy vô hạn trong đại số hạng thức hữu hạn. Quá trình kiểm tra xuất hiện cần được thực hiện đệ quy trên toàn bộ cấu trúc sau khi đã giải tham chiếu các biến đã biết trong phép thế hiện thời.

Độ phức tạp tính toán của thuật toán phụ thuộc vào cách biểu diễn cấu trúc dữ liệu và việc tối ưu hóa các bước kiểm tra chu trình.
