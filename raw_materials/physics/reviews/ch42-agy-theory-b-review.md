# Chương 42, nhóm theory-b: Hồ sơ rà của tác vụ chính

Đầu ra Antigravity được giữ trong các bản chụp call1–call3 tại qa/physics/chapter42. Lỗi cầu nối hoặc trạng thái unknown không được công nhận là thành công. Không có lượt gọi thứ tư, không mở rộng phạm vi sở hữu và không dùng subagent GPT.

Tác vụ chính đã nhập bản chụp cuối để đọc, sửa và kiểm tra riêng. Báo cáo tự thẩm định ban đầu được giữ trong bản chụp, không dùng làm bằng chứng nghiệm thu.

Phạm vi và các sửa dữ kiện, hệ số, mô hình, tiểu câu hỏi, nhãn công thức, đường dẫn, vùng cắt ảnh và cách ngắt dòng được ghi tại [Hồ sơ cuối chương](./ch42-final-source-review.md).

Các bộ Python, kiểm ảnh RGB, đo toàn bộ MathJax, kiểm cấu trúc và trình duyệt có hồ sơ trong qa/physics/chapter42. Những kết quả chỉ xác nhận các trường hợp đã kiểm, không chứng nhận toàn bộ hai môn hoặc mọi phép đo ngoài mô hình.

Đặc biệt, các khối toán bị đổi thành dấu dollar đơn đã được khôi phục. Ngưỡng hình học của tác vụ chính là 27 ex cho thân công thức hiển thị, kết hợp kiểm thực tế ở 320–1440 px. Mục tiêu biên tập 25 ex của lượt giao việc không thay thế phép kiểm khung thực tế. Bản lỗi và log giới hạn 25 ex vẫn được giữ.

Build và triển khai chỉ thực hiện trên GitHub Actions. Trạng thái công khai được xác minh riêng sau khi push.
