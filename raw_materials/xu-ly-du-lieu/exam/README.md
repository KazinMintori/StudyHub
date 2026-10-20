# Ngân hàng Ôn thi xử lý dữ liệu

Nguồn: [Thư mục câu hỏi và đáp án](https://drive.google.com/drive/folders/1OXMdS5xJ57Shd4UrBnpuQz0sLjmyqrA8).
Đã kiểm kê và tải ngày 18/10/2026.

| Bài | Trắc nghiệm | Tự luận | Tổng |
|---|---:|---:|---:|
| 1 | 40 | 20 | 60 |
| 2 | 40 | 20 | 60 |
| 3 | 48 | 24 | 72 |
| 4 | 40 | 20 | 60 |
| 5 | 48 | 24 | 72 |
| 6 | 48 | 24 | 72 |
| 7 | 52 | 28 | 80 |
| 8 | 48 | 24 | 72 |
| Tổng | 364 | 184 | 548 |

Giữ đủ 48 câu MR và 20 câu regex B7-R01 đến B7-R20. Các tình huống về
quy định học tập được giữ nguyên giả thiết của câu hỏi.

`source/` giữ nguyên 18 tệp tải xuống, gồm 16 Markdown và hai PDF Bài 4.
Hai PDF là bản xuất của cùng 60 câu và đáp án Bài 4, không phải 60 câu mới.
`source-manifest.json` ghi kích thước, SHA-256 và liên kết Drive của từng tệp.
`drive-inventory.json` ghi cây thư mục đã truy cập. Không lưu URL tải có thông
tin xác thực trong repository.

`banks/` lưu đề, bốn lựa chọn, lời giải và vị trí trong tệp nguồn. Hai câu
B4-011 và B4-021 có lựa chọn dưới dạng bảng được chuyển thành bốn lựa chọn
dọc, giữ đủ cả hai dòng output. `coverage.json` đối chiếu toàn bộ mã câu.

`reviews/` lưu phần giải thích từng lựa chọn và phương pháp đối chiếu đáp án.
Kiểm tra bằng thực thi, mô phỏng tệp/API và suy luận được ghi riêng theo
bằng chứng thực tế. Chạy được một đoạn mã không tự chứng minh toàn bộ
lời giải tự luận hoặc tất cả lựa chọn đúng. Các câu về notebook cần xét đúng
thứ tự chạy cell. Các đoạn mã có chỗ trống và lỗi cố ý phải được đọc theo đề.

`detailed-solutions/` lưu lời giải đầy đủ của 364 câu trắc nghiệm. Mỗi lời
giải giải thích riêng cả bốn phương án và bổ sung diễn biến code, ý nghĩa hàm
hoặc ví dụ chạy lại khi phù hợp. Phần phản hồi ngắn sau khi chọn đáp án được
lưu riêng với phần mở rộng “Xem lời giải”. Kiểm tra chuẩn viết hoa sau dấu
hai chấm được áp dụng lên token văn xuôi, không sửa code hoặc dữ liệu chuỗi.

Trang học sử dụng HTML đã render bằng cùng bộ Markdown, tô màu code và
MathJax của website. Các dòng ghi chú biên soạn như mã mục tiêu, địa chỉ
đọc lại và tuyên bố kiểm chứng cũ không được đưa vào lời giải hiển thị.
Nội dung đó vẫn còn nguyên trong tệp nguồn và ngân hàng. Các bước giải,
code, output và hướng dẫn chấm được giữ lại.

Không có mục quy ước chung trên trang làm bài. `question-context.json` chỉ
thêm điều kiện vào từng đề khi phiên bản hoặc cách xử lý cảnh báo ảnh hưởng
đáp án. Mã câu, đề gốc, code và lựa chọn trong `banks/` vẫn giữ nguyên.
Các dấu `$` của tiền tệ, regex và các chuỗi thẻ HTML trong đề được render
như dữ liệu, không bị hiểu nhầm thành TeX hoặc thẻ giao diện.

Quy trình cập nhật từ thư mục gốc repository:

```sh
python scripts/import-data-exam.py
# Rà lại reviews nếu nguồn thay đổi.
node scripts/build/render-data-exam.mjs
node scripts/verify-data-exam.mjs
node --test scripts/tests/data-exam-session.test.mjs
python scripts/verify-data-exam-01-04.py
python scripts/verify-data-exam-05-08.py
python scripts/verify-data-exam-code.py
python scripts/verify-source-essay-code.py
python scripts/verify-data-exam-cross-methods.py
python scripts/verify-detailed-exam-code.py
node scripts/verify-data-exam-browser.mjs
node scripts/verify-data-exam-interactions.mjs
```

Các script Python kiểm code cần NumPy, pandas 3, requests, DuckDB và pyarrow.
Script trình duyệt dùng máy chủ dev đang chạy và Chrome. Có thể đặt
`CHROME_PATH`, `QA_URL`, `QA_WIDTHS` và `QA_OUTPUT` để đổi môi trường.
Kết quả chạy chi tiết và ảnh kiểm tra nằm trong thư mục `qa/` được Git bỏ qua.
Không chạy build toàn site trên máy cục bộ. GitHub Actions thực hiện build
và deploy sau khi push.

Tài liệu kỹ thuật dùng để đối chiếu các điểm phụ thuộc thư viện:

- Quy tắc kiểu khi mảng NumPy kết hợp với số vô hướng Python được đối chiếu
  với [NumPy promotion](https://numpy.org/doc/stable/reference/arrays.promotion.html).
- Hành vi gán chuỗi chỉ mục và bản sao của pandas 3 được đối chiếu với
  [Copy-on-Write](https://pandas.pydata.org/docs/user_guide/copy_on_write.html).
- Kiểu chuỗi `str` và giá trị thiếu được đối chiếu với
  [Hướng dẫn chuyển đổi pandas 3](https://pandas.pydata.org/docs/user_guide/migration-3-strings.html).
- Thứ tự hàng sau JOIN cần được xét theo truy vấn và `ORDER BY`, đối chiếu
  với [DuckDB order preservation](https://duckdb.org/docs/stable/sql/dialect/order_preservation).
- Nhóm bắt, chuỗi raw và `fullmatch` được đối chiếu với
  [Python re](https://docs.python.org/3/library/re.html).

Tài liệu trực tuyến được đọc ngày 18/10/2026. Phiên bản chạy thực tế được
ghi trong báo cáo QA, không đồng nhất phiên bản cài cục bộ với phiên bản
tài liệu trực tuyến. Các phép kiểm chỉ có ý nghĩa trong phạm vi đã thực hiện.

## Giữ nguyên mã khi biên tập văn phong

`code-integrity.json` lưu riêng các đoạn mã và output của đề cùng lời giải đã kiểm tra ở commit `e81119de`. Bản tham chiếu này không được tự sinh lại từ HTML vừa sửa chỉ để làm kiểm tra vượt qua. Các phương án còn được đối chiếu trực tiếp với Markdown nguồn, độc lập với hash render.

`verify-data-exam.mjs` so sánh 12.278 đoạn mã, bao gồm mã nội dòng và mã nhiều dòng. Phép kiểm phát hiện đổi toán tử, dấu phẩy trong chuỗi, thay output hoặc bỏ đoạn mã. Các tên biến bổ sung trong lời giảng vẫn được phép xuất hiện. Kiểm tra trình duyệt đối chiếu tiếp nội dung các thẻ `code` với dữ liệu đã được kiểm chứng.

Mốc rà ngày 20/10/2026 phục hồi các phương án bị chèn dấu phẩy, các literal bị đổi khi sửa câu chữ và các đề còn thiếu hoặc thay đoạn mã. Mã câu hỏi và đáp án chấm điểm được giữ nguyên. Hai trường hợp người dùng chỉ ra còn được chạy bằng Python và đối chiếu giá trị tuple. Đối chiếu ký tự không thay cho kiểm chứng tính đúng của đáp án.
