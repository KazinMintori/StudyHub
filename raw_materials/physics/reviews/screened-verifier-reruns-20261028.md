# Chạy lại các bộ kiểm chứng hiện có

Đã sàng lọc tĩnh 315 tệp kiểm chứng. Trong 129 tệp đủ điều kiện, năm tệp chỉ in kết quả mà không có phép khẳng định được loại khỏi lượt chạy kiểm tra. Chạy tuần tự 124 tệp còn lại, giới hạn thời gian và số luồng BLAS. Không chạy build trang trên máy người dùng.

Lượt đầu có 121 tệp đạt và ba tệp thất bại. Hai vùng cắt kỳ vọng ở bộ kiểm chương 17 đã cũ so với ảnh đầy đủ đang được dùng. Sau khi đọc ngữ cảnh PDF, đã đồng bộ vùng kỳ vọng và đối chiếu RGB 21 ảnh với bản kết xuất gốc. Không sửa các con số vật lý để làm bộ kiểm đạt.

Ảnh chu trình Otto thực sự thiếu một phần mép trái vòng tròn số 1. Đã mở rộng ba điểm PDF ở cạnh trái, giữ cách kết xuất và mọi phần nội dung, đồng thời cập nhật công cụ xuất ảnh và kích thước kỳ vọng. Các phép kiểm biên trắng ban đầu vẫn giữ nguyên và cả bốn ảnh đều đạt.

Biểu thức 27.16 đã có đủ nội dung toán học nhưng thiếu số phương trình. Đã đối chiếu trang PDF 914 rồi khôi phục nhãn. Bộ kiểm toàn mục đạt, bao gồm các công thức, ví dụ, hình tham chiếu và phép tính vector đã được mã hóa.

Ba tệp đã được chạy lại và đạt. Giới hạn quan trọng của bằng chứng này là phạm vi các khẳng định sẵn có, không phải lời bảo đảm mọi bài trong sách đều đúng. Các tệp có thể ghi dữ liệu hoặc dùng thư viện chưa kiểm tra chưa được thực thi trong lượt này.
