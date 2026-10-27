# Sửa bố cục công thức của chương Mạch điện một chiều

Notes và năm chủ đề của chương 26 đã qua 30 trường hợp kiểm tra hiển thị thực tế ở 320, 360, 375, 768 và 1440 px. Những lỗi tràn đã quan sát trong phần nối tiếp, song song, Kirchhoff và mạch RC không còn xuất hiện trong lượt kiểm sau khi sửa.

Các hệ phương trình cho từng điện trở được trình bày trên các dòng riêng, còn các chuỗi biến đổi chỉ xuống dòng tại dấu quan hệ. Những công thức ngắn vẫn giữ trên một dòng. Tổng nghịch đảo điện trở được khai triển bằng các đại lượng đã định nghĩa trước khi viết dưới ký hiệu tổng.

Trong mạch một vòng, các điện trở được gom theo hai nhánh với giá trị từng phần tử vẫn ghi rõ. Các phương trình tìm điện thế theo hai đường đi và cân bằng công suất được tính lại. Trong mạch cầu, chia các phương trình cho điện trở chuẩn 1 Ω giúp giữ đủ các số hạng dòng điện và hệ số mà không dồn cả hệ lên dòng quá dài.

Các phép tính số của điện trở tương đương, dòng nhánh, hiệu điện thế, công suất và phần điện tích, dòng điện còn lại trong mạch RC được kiểm lại bằng Python. Có 130 phép kiểm mô hình độc lập, gồm cả nghiệm ma trận và cân bằng năng lượng. Các tiêu đề, hình tham chiếu và số hiệu phương trình trong ba tệp được sửa giữ nguyên.

Chỉ mục được sinh lại cho đúng bài này, 137 chỉ mục khác giữ nguyên từng byte. Bộ kiểm tra cấu trúc đạt 133 bài và 354 chủ đề, không có lỗi hoặc cảnh báo. Bộ công cụ đạt 39 kiểm thử.

Báo cáo này xác nhận phạm vi sửa bố cục lý thuyết. Việc đối chiếu đầy đủ toàn bộ nội dung, từng hình, các lời giải cuối chương, Cheatsheet và Wiki còn thuộc đợt rà nguồn tiếp theo. Bản công khai của các sửa đổi này còn chờ lượt build và deploy tiếp theo.
