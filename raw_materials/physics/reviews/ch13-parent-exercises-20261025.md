# Rà bài tập chương 13: Hấp dẫn

Ngày rà: 25/10/2026. Phạm vi: Phần luyện tập ở cuối PDF 440 đến hết PDF 448. Đã đối chiếu với đề và hình trên các trang thực, không chỉ kiểm số tiêu đề.

## Độ phủ nội dung

Đủ 84 bài đánh số, 21 câu thảo luận, 12 bài luyện tập hướng dẫn và một bài cầu nối, tổng cộng 118 đơn vị. Ba bài Challenge là 13.79–13.81. Ba câu MCAT là 13.82–13.84, có đoạn đọc và bảng phân loại thành phần ngoại hành tinh. Bài cầu nối giữ cả chín câu hướng dẫn trước khung và chín bước giải bên trong.

Mỗi đơn vị có đề trước một khung lời giải đóng sẵn. Trong khung có Tóm tắt đề bài, Hướng đi nêu công thức và lý do dùng, rồi Lời giải mọi phần. Toàn bộ phần cuối chương nằm trong tab Bài tập. Các ví dụ và tự kiểm trong mạch dạy vẫn ở Notes.

Tám hình bài tập được cắt nguyên bản, giữ đủ nhãn và phần hình. Năm hình lý thuyết được dùng lại. Mười hình lời giải mới phục vụ đúng yêu cầu sơ đồ lực, đồ thị và hình học phân tích của đề. Mã sinh hình được lưu để tái lập và đối chiếu mã băm. Hình E13.39 dùng một khung hợp nhất đủ rộng, không lưu hai bản cắt cạnh tranh.

## Những điểm cần đọc cẩn thận

Bài 13.1 so lực Mặt Trời lên Mặt Trăng với lực Trái Đất lên Mặt Trăng. Bài 13.3 yêu cầu thời gian hai phi hành gia từ nghỉ cách 20 m gặp nhau, không phải thời gian tiến gần thêm 1 cm. Bài 13.8 có hai khối lượng cách 50 cm và điểm thả cách vật 8 kg một đoạn 20 cm. Các bản nháp sai dữ kiện đã được sửa trước khi nhập công khai.

Ở bài 13.58, với đúng vị trí và hai khối lượng được cho, vật thả từ nghỉ gia tốc sang trái. Vị trí được hỏi ở bên phải còn bị ngăn bởi rào thế. Lời giải chứng minh không thể có chuyển động ấy, đồng thời phân biệt tốc độ hình thức từ năng lượng với một trạng thái thật sự tiếp cận được.

Bài 13.70 cho tốc độ 9640 m/s trên quỹ đạo tròn quanh Trái Đất. Điều kiện quỹ đạo tròn của trường khối lượng tập trung lại cho bán kính nhỏ hơn bán kính Trái Đất. Đề được giữ nguyên, và kết quả đại số được nêu cùng giới hạn vật lý thay vì âm thầm đổi số.

Bài 13.47 phân biệt vị trí hai bề mặt tiếp xúc với quãng đường tâm quả cầu đi được. Bài 13.76 giữ tám dòng dữ liệu và giá trị G riêng của đề. Hồi quy tự do và hồi quy cố định hệ số góc Kepler được trình bày riêng, không sửa dữ liệu để ép khối lượng Mặt Trời về một đáp số chọn trước.

Các câu thảo luận nêu rõ miền áp dụng của tốc độ thoát, chuyển động xuyên tâm suy biến, xấp xỉ parabol gần mặt đất, lực trung tâm tỉ lệ nghịch lập phương, lực hấp dẫn ở khoảng cách hữu hạn và không trọng lượng biểu kiến cục bộ. Không đưa định luật Newton của hệ quán tính sang hệ máy bay gia tốc mà quên lực quán tính.

## Kiểm chứng và bố cục

Toàn bộ kết quả số được tính lại bằng Python. Lượt rà độc lập phần đầu có 139 đối chiếu. Phần sau có 189 kiểm tra số/hình học và 106 kiểm tra cấu trúc. Các câu thảo luận có 122 đối chiếu độc lập. Gói luyện tập hướng dẫn và bài cầu nối có 67 đối chiếu, gồm tích phân công và kiểm nghiệm quỹ đạo. Các số đếm này có phần chồng lấp, không phải số bài khác nhau.

Kiểm trình duyệt đủ 21 nhóm ở năm chiều rộng 320, 360, 375, 768 và 1440 px: 105 trường hợp đạt, đủ 118 đề và lời giải đóng sẵn. Một bảng ba cột bị tràn tại 320 px đã được tách thành hai bảng hai cột, giữ nguyên dữ liệu và đơn vị. Các tiêu đề con của bài cầu nối được phân cấp để bộ nhóm chỉ nhận một bài cầu nối.

Không thấy công thức tràn, ảnh hỏng, ký hiệu toán lỗi hoặc thanh cuộn toán trong phạm vi kiểm cuối. Sau khi phiên kiểm tra bị dừng bởi môi trường, các nhóm đã đạt được giữ lại và phần còn lại được kiểm tiếp. Hai phần bằng chứng có cùng mã băm nội dung và được ghép thành bộ 105 trường hợp đầy đủ.

## Phạm vi xác nhận

Kết hợp với lượt rà lý thuyết đã có, chương 13 đủ nội dung trong phạm vi nguồn và các kiểm tra được ghi. Việc này không chứng nhận những chương khác hoặc toàn bộ hai học phần. Build và xuất bản toàn cục chỉ chạy trên GitHub Actions sau push. Ảnh và dữ liệu trên bản web còn được kiểm riêng sau khi triển khai thành công.
