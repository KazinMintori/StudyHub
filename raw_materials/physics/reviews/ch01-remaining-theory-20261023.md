# Rà lý thuyết chương 1

Ngày chốt nội dung: 24/10/2026. Phạm vi gồm lời mở, mười mục 1.1–1.10 và tổng kết ở trang PDF 21–45, tương ứng trang in 1–25. Chương giữ trạng thái `draft` vì phần bài tập cuối chương chưa được nghiệm thu.

## Nội dung đã đối chiếu

Đã dùng bản kiểm định độc lập để sửa điều kiện xác định góc từ thành phần vector, phân biệt chữ in nghiêng với chữ thường, và giải thích đúng trường hợp nhân vector với số dương nhỏ hơn một. Khi cả hai thành phần bằng không, không gán hướng cho vector không.

Bảng 1.2 giữ nguyên các thừa số 1,32578×10⁷ và 4,11×10⁻³. Tích chưa làm tròn là 54489,558, cho kết quả ba chữ số có nghĩa 5,45×10⁴. Không làm tròn dữ kiện trước phép nhân.

Phần tích vô hướng và tích có hướng đều khai triển đủ chín tích vector đơn vị, giải thích các tích triệt tiêu và bước gom theo ba phương. Mô tả mặt phẳng và quy tắc bàn tay phải có điều kiện hai vector khác không, không cùng phương. Không gán hướng cho tích bằng vector không. Phân biệt rõ thay hệ tọa độ thuận bằng hệ nghịch chỉ làm đổi quy ước dấu của công thức tích có hướng, không đảo dấu toàn bộ phép tính vector.

Giữ 25 số phương trình gốc, 11 ví dụ và sáu câu tự kiểm, cùng câu hỏi mở đầu. Python tính lại độc lập 21 đơn vị gồm ví dụ, tự kiểm, bảng số và phép thử đại số. Kiểm thử tích vô hướng, tích có hướng dùng 36 cặp vector không tầm thường, có cả vector không và vector cùng phương. Những giả thiết minh họa trong bài ước lượng được gọi rõ là giả thiết, không ghi thành thống kê về trường.

Phần khối lượng giữ nội dung hằng số Planck và mốc 2018 vì cả hai có mặt trên trang PDF 24–25. Các nhãn hình và lời dẫn được đối chiếu trực tiếp với nguồn. Đã sửa dẫn chiếu ý nghĩa h từ chương 28 sang chương 38 sau khi kiểm tra mục lục PDF 13 và phần Planck ở PDF 1275–1276, có ghi chú đính chính riêng. Hình 1.34 ở trang PDF 46 là hình bài cầu nối, không bị tính nhầm thành hình lý thuyết còn thiếu.

## Hình và phần hỗ trợ

42 ảnh gồm 34 ảnh cho các hình đánh số 1.1–1.33 (Hình 1.1 có hai ảnh), ảnh mở đầu, ảnh ứng dụng và sáu sơ đồ tổng kết. Đã sửa các vùng trích mất nhãn hoặc thiếu các phần hình, kiểm tra khớp điểm ảnh với PDF và xem trực quan. Sáu ảnh tổng kết được đặt tên minh họa tổng kết thay vì tạo nhầm các số Hình 1.30–1.35.

Chú thích dịch 125 nhãn tiếng Anh thực sự xuất hiện. Không đặt công thức TeX trong bảng nhãn vì nơi hiển thị này là văn bản thuần. Gộp chú thích trùng dưới ảnh để mỗi hình chỉ có một chú thích hiển thị.

Bảng 1.1 giữ đủ 11 mục quy đổi và ứng dụng trong ba nhóm độ dài, khối lượng, thời gian. Các quy tắc trong Bảng 1.2 và dữ liệu thành phần vector của Ví dụ 1.7 được trình bày lại theo từng nhóm để không tràn màn hình nhỏ, không xóa dữ kiện.

Chương không coi đơn vị và vector là kiến thức tiên quyết vì đây là nơi dạy chính các khái niệm ấy. Các mục tra cứu hỗ trợ vẫn liên kết tới Wiki đơn vị, vector, thành phần và hai phép nhân vector. Cheatsheet có 33 dòng công thức, cùng định nghĩa, tính chất và điều kiện áp dụng.

## Kiểm tra

Đã chạy kiểm tra cấu trúc bài và mười trang chủ đề, đo riêng toàn bộ công thức trong các nguồn include và cheatsheet, kiểm tính số bằng Python, cùng kiểm thử biên dịch SVG cho mọi công thức và chú giải biến của module. Kiểm tra 60 trường hợp trình duyệt cho mười mục, trang chương và cheatsheet ở 320, 360, 375, 768, 1440 px: Đạt. Không có công thức vượt mép, lỗi MathJax, ảnh hỏng hoặc TeX thô trong chú thích hình.

Build và deploy toàn cục do GitHub Actions thực hiện. Báo cáo này chỉ chứng nhận phạm vi lý thuyết đã nêu, không chứng nhận bài tập cuối chương chưa hoàn chỉnh.
