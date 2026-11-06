# Cập nhật bộ đề xử lý dữ liệu từ Drive

Các bộ bài 1–8 dùng nguồn, mã câu và quy trình kiểm tra hiện có. Các bộ mới bài 10 và 11 được nhập riêng qua `scripts/import-data-exam-additions.py`, không chạy lại bộ nhập cũ để ghi đè dữ liệu đã rà.

Nguồn riêng của học phần nằm trong repo `StudyHub-course-xu-ly-du-lieu`, gồm:

- `raw_materials/xu-ly-du-lieu/exam/source/`: Bốn tệp Markdown đầy đủ tải từ Drive, giữ nguyên ký tự và xuống dòng của bản gốc.
- `additions-20261106.json`: ID tệp, kích thước, SHA-256 và toàn bộ mã câu đã đọc.
- `banks/bai-10.json`, `banks/bai-11.json`: Câu hỏi và đáp án chính sau khi bỏ phần hướng dẫn chấm, thời gian, độ khó và ghi chú biên soạn.
- `reviews/bai-10.json`, `reviews/bai-11.json`: Kết quả rà, giải thích từng phương án và phần diễn giải thêm cho tự luận.
- `additions-render-coverage.json`: Mã câu đầu vào/đầu ra cùng mã băm nội dung đã dựng.

Mỗi bộ có 60 câu trắc nghiệm và 30 câu tự luận. Thứ tự A–D và mọi ký tự mã phải được giữ nguyên. Các giả định quyết định đáp án được đặt trong đề tương ứng. Không tạo một bảng quy ước chung cho toàn ngân hàng.

JSON và tập nhãn có dấu ngoặc nhọn là dữ liệu của đề. Bộ dựng cho các ngân hàng mới tắt quy tắc Markdown attributes để tránh biến dữ liệu đó thành thuộc tính HTML rồi làm mất chữ. Các payload JSON được đưa vào khối mã, giữ giá trị và thứ tự trường. Bộ kiểm tra so cả dữ liệu trong ngoặc nhọn với nguồn gốc, không chỉ so giao diện với HTML đã biên dịch.

Các lệnh kiểm tra nguồn:

```powershell
python scripts/verify-data-exam-additions.py
node scripts/build/render-data-exam-additions.mjs
node scripts/verify-data-exam-additions.mjs
node --test scripts/tests/data-exam-additions.test.mjs
```

Script Python dùng dữ liệu giả lập để kiểm tra phép tính, mặt nạ pandas, JSON/schema và trạng thái cache/retry. Không gọi API, không sử dụng API key và không chờ bằng `sleep`. Những câu lập luận về cách diễn giải dữ liệu còn phải được đọc riêng. Một phép thử số học không tự chứng minh mọi lời giải đều đúng.

Kiểm tra trình duyệt trên GitHub đọc đủ 180 câu ở bề rộng 360 và 1280 px, xác nhận mỗi màn hình có một câu, các lựa chọn xếp theo A–D, bốn giải thích xuất hiện sau khi chọn và tự luận ẩn lời giải ban đầu. Mã được so từng ký tự với nội dung đã dựng. Báo cáo và một số ảnh cần thiết được lưu tối đa ba ngày theo workflow hiện có.

Sau khi xuất nội dung vào repo học phần, commit và push ở đó trước. Cập nhật pin học phần tại repo chính, commit rồi dùng `npm run verify:cloud -- full` để kiểm tra bản ghép trên GitHub. Không build toàn bộ trên máy cục bộ.
