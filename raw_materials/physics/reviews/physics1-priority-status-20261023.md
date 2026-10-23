# Trạng thái biên tập Vật lý đại cương 1, ngày 23/10/2026

## Phần đã hoàn tất trong worktree riêng

Chương 9 và chương 18 đã hoàn tất lượt đối chiếu, tính lại và kiểm tra trình bày. Đây là trạng thái nội dung cục bộ, chưa xác nhận triển khai công khai.

Chương 18 có sáu mục, tám ví dụ, 12 bài luyện tập hướng dẫn, 30 câu thảo luận, 87 bài đánh số và một bài cầu nối. Tổng cộng 130 đề với lời giải gập, chia thành 24 nhóm. 52 ảnh PNG đối chiếu lại byte RGB với PDF, kèm hai hình lời giải bổ sung. Trình duyệt kiểm tra 156 trường hợp ở 320, 360, 375 và 1440 px.

Chương 9 đã kiểm tra lại 14 chỗ ngắt dòng làm tách vế trái của một phương trình mới khỏi dấu quan hệ. Đồng thời, 12 công thức chỉ có một dòng được bỏ môi trường căn lề thừa. Sau sửa, 130 đề trong 23 nhóm được kiểm tra lại trên bốn kích thước màn hình, cùng Notes, sáu chủ đề, Slides và Cheatsheet. Tổng cộng 168 trường hợp trình duyệt đạt.

Bổ sung bộ kiểm tra trước khi tạo nhóm bài tập để chặn kiểu ngắt dòng này và trường hợp xuống dòng ngay sau dấu bằng. Không dùng việc công thức vừa màn hình làm bằng chứng duy nhất rằng bố cục đúng.

## Chương 19 đang rà

Đã nhận đủ 15 tệp thô, gồm tám mục lý thuyết, lời mở, tổng kết và các tệp bài tập. Việc có đủ tệp hoặc đủ mã bài không đồng nghĩa với hoàn tất nghiệm thu.

Đã sửa các dấu xuống dòng viết thành ký tự khiến 31 tiêu đề không được nhận diện. Đã phục hồi đoạn đọc và đầy đủ lựa chọn cho 19.63–19.66. Bài 19.66 phải cộng áp suất khí quyển vào áp suất đo, nên kết quả khoảng 0,211 m³, chọn (a). Bản soạn trước chọn (b) không đúng.

Đã sửa việc đọc mốc áp suất tại điểm c trong Hình P19.38. Áp suất ở a và b là 8,0 × 10⁵ Pa, không phải 2,0 × 10⁵ Pa. Đã tính lại nhiệt độ, nhiệt lượng và độ biến thiên nội năng tương ứng. Các sửa chữa này là lỗi biên soạn, không quy cho tài liệu nguồn.

Đã sửa tọa độ đọc từ Hình E19.4. Việc dời cả bốn đỉnh không làm đổi diện tích nhưng đã làm sai số mol cực đại. Dùng tọa độ thật cho số mol cực đại khoảng 0,0590 mol. Lời giải diện tích được trình bày lại bằng các tích chéo, không ngắt giữa các số hạng.

Đã thêm tám đồ thị lời giải cho 19.1, 19.17–19.19, 19.29, 19.52, 19.60 và 19.62. Mỗi đồ thị được tạo bằng Python, có dữ kiện hoặc giả thiết biểu diễn rõ ràng. Giữ riêng các ảnh trích từ PDF. 18 ảnh cuối chương so khớp lại RGB, đồng thời giảm chú giải xuống đúng chữ tiếng Anh thực sự xuất hiện.

Lý thuyết, phần C và phần D đã qua kiểm tra độ rộng nghiêm ngặt trong lượt gần nhất. Phần E vẫn còn 103 khối hiển thị và 50 biểu thức nội dòng vượt ngưỡng rà chặt hoặc cần xem lại cách hiển thị. Chương 19 vẫn là bản nháp, cần rà từng dữ kiện, đủ ý hỏi, các bước giải, hình và bố cục trước khi nghiệm thu.

## Các phần còn lại

Chương 10, 11, 17 và 20 vẫn có nội dung hoặc bài tập cần hoàn thiện. Không thay đổi trạng thái thành hoàn tất chỉ dựa trên báo cáo của tác vụ Antigravity.

Các kết quả công cụ Antigravity không tìm thấy sau khi cầu nối khởi động lại đã được bảo toàn và kiểm tra ranh giới tệp. Tác vụ cuối của phần E chương 11 báo hết tín dụng, RESOURCE_EXHAUSTED 429, mã thoát 3. Mọi tác vụ đã dùng hết ba lượt được dừng đúng giới hạn và giữ worktree, không mở lượt thứ tư dưới tên mới.

## Kiểm tra dự án

146 kiểm thử dự án, 108 kiểm thử tính năng và 39 kiểm thử công cụ bài giảng đạt. Kiểm tra mô hình nội dung, ranh giới kiến trúc và các hộp lời giải đạt. Ba thẻ ôn tập được đăng ký cho chương 2 đã có trạng thái sẵn sàng, để bổ sung liên kết Slides còn thiếu khi môn Vật lý 1 bắt đầu có bộ thẻ ôn tập.

Không chạy build toàn cục tại máy người dùng. Máy chủ xem thử phục vụ kiểm tra đã được dừng sau khi dùng. Chưa commit hoặc push các thay đổi của đợt biên tập này. Nhánh từ xa có cập nhật ở học phần khác, cần tích hợp cẩn thận trước khi xuất bản.
