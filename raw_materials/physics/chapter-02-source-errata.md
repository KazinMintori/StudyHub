# Các điểm cần hiệu chỉnh trong chương 2

Đối chiếu trực tiếp PDF Young & Freedman, ấn bản 15. Các ghi chú này phục vụ kiểm tra nội dung, không thay thế lời giải.

| Vị trí | Nội dung cần xét | Cách xử lý |
| --- | --- | --- |
| Trang in 48, PDF 68, phần đánh giá Ví dụ 2.4 | Thời gian được in là 25 s khi vận tốc tăng từ 15 m/s lên 25 m/s dưới gia tốc 4,0 m/s². | Kết quả đúng là 2,5 s. Thay vào phương trình tọa độ cho 55 m. |
| Trang in 45, PDF 65, câu sau (2.10) | Câu phủ định tuyệt đối công thức trung bình cộng khi gia tốc thay đổi quá mạnh so với điều có thể chứng minh. | Gia tốc không đổi là điều kiện đủ bảo đảm công thức trên mọi khoảng. Gia tốc thay đổi có thể tình cờ cho cùng giá trị trên một khoảng. Không dùng công thức này như công thức tổng quát cho gia tốc biến thiên. |
| Trang in 54, PDF 74, nhãn cuối Hình 2.28 | Trong ảnh ghi đồ thị x–t, trong khi trục đứng là gia tốc và nội dung nói về độ biến thiên vận tốc. | Giữ nguyên ảnh. Lời giảng và chú thích tiếng Việt xác định đúng đây là đồ thị gia tốc theo thời gian. |

Bài 2.52 ở trang in 62, PDF 82 cho chuyển động dọc trục x nhưng câu yêu cầu đồ thị ghi aᵧ và vᵧ. Các đồ thị gia tốc, vận tốc và tọa độ được giữ nhất quán theo cùng trục x, không đổi nội dung vật lý hoặc điều kiện đã cho.

Các phép đối chiếu tính toán có thể chạy lại bằng raw_materials/physics/verify_chapter02_foundations_parent.py. Các lỗi ở bài tập cuối chương được kiểm kê riêng khi hoàn thiện lời giải.


## Rà soát 2.75–2.76, PDF 83, 2026-10-28

- 2.75: Không thay đổi dữ kiện nguồn. Lời giải lấy mốc rời tay để trả lời 1,41918 s và ghi thêm mốc bắt đầu đẩy 1,61042 s, tránh nhập nhằng mốc đếm.
- 2.76: Nguồn khẳng định gia tốc tầng một không đổi, nhưng chỉ cho thời gian và vận tốc cuối của tầng hai. Chưa đủ suy ra độ dời tầng hai nếu không biết quy luật vận tốc. Đáp số số học theo cách giải thông dụng được gắn điều kiện gia tốc tầng hai không đổi. Không khẳng định đây là lỗi đáp án của sách. Ba đáp số tổng quát phụ thuộc s2 là tích phân vận tốc tầng hai.
