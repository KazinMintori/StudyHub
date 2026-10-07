# Tự rà B: lượt sửa sau review

Đây là lượt sửa sau review. B.md được giữ nguyên làm output lần đầu; B-revised.md chỉ sửa cách xác định tensor và cặp chỉ số trong ví dụ.

## Kiểm tra đã thực hiện

- Review chỉ ra rằng ký hiệu \(A_{ii}\) trong ví dụ ban đầu có hai chỉ số dưới mà chưa nêu loại tensor hay quy ước cho phép ghép chúng. Vì vậy ví dụ ban đầu cần làm rõ để tránh coi việc lấy tổng đường chéo là phép co hợp lệ cho mọi tensor hai chỉ số.
- Đọc phần văn bản mục 2.6, trang in 14 của [Differential Geometry — ghi chép bài giảng của Leonard Tomczak, giảng viên Jack Smith](https://math.berkeley.edu/~ltomczak/notes/Mich2022/DG_Notes.pdf#page=14). Nguồn phân biệt vị trí trên/dưới của chỉ số và nêu lấy tổng theo chỉ số lặp một lần trên, một lần dưới, cùng ví dụ phép co.
- Thay ví dụ bằng tensor loại \((1,1)\), viết thành phần \(A^i{}_j\); nêu rõ một chỉ số trên, một chỉ số dưới, cơ sở hai chiều và cặp được co. Kiểm tra công thức \(\sum_{i=1}^{2}A^i{}_i\) giữ đúng cặp ghép trên–dưới và phạm vi tổng.
- Giữ nguyên các số trong ví dụ. Kiểm tra hai số hạng là \(A^1{}_1=1\) và \(A^2{}_2=4\), cho tổng 5; phép cộng này đã được tính độc lập bằng PowerShell trong lượt đầu.
- Rà bản sửa bằng cách đọc lại file đã ghi; giữ bản dịch, ý phép cộng theo chỉ số và sự phân biệt với ánh xạ co. Chỉ thêm thông tin đủ để ví dụ đúng loại tensor, không mở rộng thành bài lý thuyết tensor.

## Giới hạn

- Phần tra cứu ngoài chỉ phục vụ góp ý kỹ thuật ở lượt sửa B. Ghi nhận “không tra cứu ngoài” trong checks-and-limits.md mô tả bộ output lần đầu A–F.
- Chưa phân tích các loại tensor hay quy ước co khác; ví dụ được giới hạn ở tensor có một chỉ số trên và một chỉ số dưới.
- Đây là tự rà sau review, không phải thử nghiệm với sinh viên và không chứng nhận hiệu quả giảng dạy.
