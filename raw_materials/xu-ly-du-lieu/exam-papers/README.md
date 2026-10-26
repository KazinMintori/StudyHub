# Năm đề giữa kỳ

Nguồn nhập là các ảnh và PDF người dùng cung cấp trong cuộc trò chuyện. Giữ nguyên câu hỏi, phương án và code; lời giải được đối chiếu bằng Python với pandas 3.0.1 và NumPy 2.3.5.

| Trang | Mã đề | Trắc nghiệm | Tự luận |
| --- | --- | --- | --- |
| Đề 1 | 047 | 20 | 6 |
| Đề 2 | 045 | 20 | 6 |
| Đề 3 | 046 | 20 | 6 |
| Đề 4 | 030 | 20 | 6 |
| Đề 5 | 001 (luyện tập) | 20 | 6 |

`source.json` lưu 130 câu, 400 phương án, nguyên văn nguồn và lời giải Markdown đầy đủ. Mã 046 dùng PDF mới nhất; câu 16, 18 và 24 khác ảnh cũ. Câu phụ thuộc phiên bản thư viện có ghi chú ngay trên trang.

Mã 030 có chín câu không đủ điều kiện chấm A–D: 4, 5, 7, 8, 9, 10, 11, 12, 18. Các câu vẫn xuất hiện trong phần trắc nghiệm, cho mở lời giải và ghi nhận đã đối chiếu, nhưng không tính đúng/sai. Câu 13 nhận A hoặc C; câu 17 nhận C hoặc D.

Tái tạo các ngân hàng HTML bằng `node scripts/build/render-imported-exams.mjs`. Bước này kiểm tra code trong cả đề và lời giải không đổi sau render; `render-coverage.json` ghi mã băm nguồn và đầu ra từng đề. Chạy `node --test scripts/tests/imported-exams.test.mjs` để kiểm tra số lượng, phương án, code và chấm điểm.

`metadata.json` phân biệt bốn đề chính thức với mã 001 luyện tập và lưu học kỳ, năm học đúng phần đầu tài liệu. Ngày thi cụ thể chỉ điền theo thông tin đã xác nhận, dùng dạng ISO `YYYY-MM-DD`. Giá trị `null` nghĩa là chưa có thông tin ngày thi, không lấy ngày trong dữ liệu bài tập hoặc ngày biên soạn lời giải làm ngày thi. Giao diện trình bày ngày đã xác nhận theo dạng ngày/tháng/năm.
