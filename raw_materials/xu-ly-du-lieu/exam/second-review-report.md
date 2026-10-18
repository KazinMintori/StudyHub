# Rà soát độc lập bổ sung ngày 18/10/2026

Lượt rà này giữ nguyên 548 câu, 364 khóa trắc nghiệm và 184 câu tự luận. Chưa tìm thấy bằng chứng buộc đổi khóa A–D trong phạm vi đã giải lại. Không suy ra tỷ lệ đáp án đúng của toàn bộ ngân hàng từ kết quả đó.

Luna ghi kết luận trước khi mở khóa cho 132 câu, gồm 35 câu trắc nghiệm và 97 câu tự luận. Sol 6.1 ở mức xhigh giải trước 33 câu khó. Antigravity lưu kết luận trước khi mở khóa cho 46 câu, gồm 25 câu trắc nghiệm và 21 câu tự luận. Hợp của ba tập có 177 câu riêng biệt, gồm 68 câu trắc nghiệm và 109 câu tự luận. Đây là phạm vi giải lại, không phải 177 câu được chứng minh đúng tuyệt đối.

Hai mươi câu Bài 1 viện dẫn quy định hoặc nội dung tổ chức riêng của môn. Khóa các câu này khớp đáp án nguồn, nhưng sự trùng khớp không xác nhận độc lập hiệu lực hay tính đúng đắn của quy định được viện dẫn. Những câu này được đánh dấu `source_dependent_course_recall` trong hồ sơ rà, không thêm bảng giả định chung vào giao diện.

## Các hiệu chỉnh đã áp dụng

Lời giải chi tiết của 13 câu được sửa để loại bỏ khẳng định sai hoặc quá rộng:

- B1-001, B1-003, B1-005, B1-015, B1-024: Phạm vi quy trình dữ liệu, điều kiện nhân hàng khi nối bảng, môi trường ảo, phụ thuộc gói và trách nhiệm khi khai báo AI.
- B3-016: An toàn của `int16` phụ thuộc miền giá trị, không suy ra độ rộng thanh ghi hoặc khả năng tránh mọi tràn số.
- B4-003, B4-022: Tham số `squeeze` không còn trong `read_csv` ở pandas 3. `head()` theo thứ tự hàng hiện tại, không theo địa chỉ bộ nhớ vật lý.
- B6-015, B6-044: Phân biệt điều kiện đủ với điều kiện cần của số hàng LEFT JOIN và phân biệt NaN với NULL khi DuckDB đọc pandas.
- B7-056: `StringDtype` có thể dùng storage Python hoặc PyArrow. Không hứa mọi `.str` chạy song song hoặc nhanh hơn `apply`.
- B8-051, B8-055: Phân biệt cảnh báo với ngoại lệ khi đọc ngày và phân biệt phép chia scalar Python với kết quả `pct_change` trên Series.

Phản hồi ngắn của 26 câu Bài 1 được đối chiếu lại với đúng đề và bốn lựa chọn. Hai phản hồi B3-003 và B3-MR09 được phục hồi dấu âm của chỉ mục `-1`. Tám câu khác được sửa dấu backtick hoặc chuỗi kỹ thuật bị chèn khoảng trắng, gồm B6-001, B7-003, B7-005, B7-022, B7-054, B7-055, B7-R11 và B8-035. Tổng cộng 47 câu có thay đổi nội dung hiển thị.

Metadata kiểm chứng cũ của 252 câu Bài 1–4 được thay bằng quan sát thực thi có thật hoặc giới hạn được nêu rõ. Không tiếp tục giữ các mô tả chạy thử dùng nhầm dữ liệu, biến hoặc chương trình. B2-030 đã được chạy lại bằng đúng module `cleaning` cung cấp trong đề với namespace của chương trình chính tách biệt, xác nhận `NameError`. Lỗi thiếu fixture của trình chạy cũ không được xem là đáp án của bài.

## Kiểm tra và giới hạn

Script `scripts/verify-data-exam-second-review.py` chạy 20 phép kiểm bằng đầu vào cụ thể, phép tính hữu tỷ, liệt kê cặp, phản ví dụ, metadata gói và đối chiếu Python/pandas/DuckDB. Môi trường chạy gồm Python 3.14.7, NumPy 2.5.2, pandas 3.0.5 và DuckDB 1.5.6. Phiên bản cài cục bộ không được đồng nhất với mọi phiên bản ghi trong đề.

Các bộ kiểm tra đã qua gồm cấu trúc và bảo toàn nguồn của 548 câu, 16 kiểm thử chức năng/liên quan đến phản hồi, 329 ví dụ code với output minh họa và 92 lượt câu hỏi/màn hình cho toàn bộ 46 câu sửa ở 360 px và 1280 px. B1-001 và B4-003 được kiểm thêm tổng cộng bốn lượt sau những lần sửa cuối. Các lượt trình duyệt kiểm cả bốn phản hồi, lời giải mở rộng, mã, công thức, viết hoa sau dấu hai chấm và tràn khung. Bộ công cụ bài giảng gồm 39 kiểm thử đã qua, kiểm cấu trúc bài giảng không có lỗi.

Kết luận giải trước khi xem khóa vẫn có thể sai. Ba kết luận ban đầu của Luna về đường dẫn B1-019, nhãn phí B5-050 và phép gán B5-MR12 đã được đính chính bằng đầu vào cụ thể, không sửa khóa để chạy theo kết luận sai của người rà. Bản thảo Antigravity cũng có diễn giải sai về LEFT JOIN, thứ tự căn chỉnh, giá trị thiếu và alias thời gian. Sol phân xử riêng các điểm này. Chỉ các nhận định được đối chiếu và tái hiện mới được dùng để sửa nội dung.

Bridge Antigravity mất trạng thái ở lần gọi đầu và báo lỗi `NoneType` ở lần tiếp tục, dù các tệp kết luận và báo cáo đã được lưu. Không coi trạng thái chạy đó là thành công tự động. Các tệp được đọc, đối chiếu độc lập và giữ nguyên để kiểm toán. Bốn mươi bảy tệp có sẵn trong worktree C giữ nguyên hash. Ba lỗi khi chạy riêng đoạn lời giải tự luận thiếu setup là giới hạn trình chạy, không phải bằng chứng lời giải gốc sai.

## Tài liệu tham khảo

- [Python venv](https://docs.python.org/3/library/venv.html).
- [pip freeze và các gói bị bỏ qua mặc định](https://pip.pypa.io/en/stable/cli/pip_freeze/).
- [Kiểu số NumPy và tràn số](https://numpy.org/doc/stable/user/basics.types.html).
- [pandas DataFrame.head](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.head.html).
- [pandas StringDtype](https://pandas.pydata.org/docs/reference/api/pandas.StringDtype.html).
- [pandas to_datetime](https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html).
- [DuckDB NULL](https://duckdb.org/docs/current/sql/data_types/nulls).
- [Python ZeroDivisionError](https://docs.python.org/3/library/exceptions.html#ZeroDivisionError).
