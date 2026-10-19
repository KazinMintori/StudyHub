# Thực hành phân tích Porto

Dự án minh họa chạy trên dữ liệu công khai Inside Airbnb, không dùng danh sách mã hoặc kế hoạch riêng của một nhóm. Mẫu mặc định gồm 120 listing có mặt ở cả bốn snapshot. Số lượng mẫu, seed và cửa sổ 30 ngày là lựa chọn minh họa, không phải định mức bài nộp của môn.

## Chạy phần dữ liệu

Đã kiểm thử với Python 3.14.7 ghi trong `.python-version`. Mã chỉ dùng thư viện chuẩn, không cần cài thêm gói. Tệp phiên bản không tự cài Python. Sau khi giải nén, mở terminal tại thư mục dự án:

```bash
python --version
python run_pipeline.py --config configs/porto.json --skip-llm
```

Lần đầu tải 13 tệp từ Inside Airbnb, khoảng 642 MB cho các snapshot hiện tại. Dữ liệu CSV sau giải nén được đọc theo luồng, không tạo một bản CSV đầy đủ trên đĩa. Chương trình giữ toàn bộ tệp nguồn nén để đối chiếu. Lần sau kiểm checksum rồi dùng lại các tệp này. Nếu tệp bắt buộc không có, tải không hoàn chỉnh hoặc khóa bị trùng, chương trình báo lỗi. Không có chế độ tự thay dữ liệu thật bằng dữ liệu giả.

Đọc `latest-run.json` để tìm lần chạy thành công gần nhất. Mỗi lần chạy có thư mục riêng trong `runs/`. Con trỏ này chỉ đổi khi bước tính và sinh hình hoàn thành. Một lần chạy lỗi không được coi là bản kết quả mới.

## Cấu hình

`configs/porto.json` ghi thành phố, đường dẫn nguồn, bốn snapshot, tiền tệ, cỡ mẫu, seed và cỡ mẫu review. `price_decimal` và `price_thousands` xác định cách đọc số tiền, tránh đoán dấu chấm/phẩy. Cấu hình mẫu đang dùng dấu chấm thập phân và dấu phẩy ngăn nghìn như tệp nguồn đã kiểm tra.

Giá không dương hoặc không đọc được không tham gia KPI giá. Listing vẫn còn trong những chỉ số khác nếu các trường cần dùng hợp lệ. Bản mẫu không đặt ngưỡng giá cao tùy tiện. Việc xem phân bố giá và những giá trị lớn nhất được thực hiện trước khi quyết định có cần thêm quy tắc ngoại lai hay không.

Đổi tiền tệ cần sửa và kiểm chứng logic tương ứng. Ví dụ này chủ động từ chối tiền tệ khác EUR để tránh dán nhãn sai đơn vị. Đổi ngày cần xác nhận URL và cấu trúc nguồn tương ứng trước khi chạy.

## Tệp đầu ra

- `data/raw/<snapshot>/`: Các tệp tải nguyên trạng và manifest chứa URL, byte và SHA256.
- `runs/<run>/processed/cohort.csv`: Các mã listing được chọn, lưu để đối chiếu.
- `selected_listings.csv`: Khóa snapshot và listing, giá gốc, giá đọc được, các trường và cờ QA.
- `selected_calendar.csv`: Khóa snapshot, listing và ngày. Chỉ giữ cửa sổ đã cấu hình.
- `selected_reviews.csv`: Mẫu review duy nhất. Review có xung đột nội dung bị loại khỏi mẫu LLM và được ghi nhận.
- `review_appearances.csv`: Những snapshot có quan sát thấy mỗi review. Không dùng số hàng ở đây như số review duy nhất.
- `exceptions.csv`: Khóa bản ghi, quy tắc và hành động cần xem lại.
- `kpi_city.csv`, `kpi_neighbourhood.csv`: Chỉ số có mẫu số, đơn vị và trạng thái.
- `runs/<run>/reports/`: Báo cáo QA, nguồn, baseline, LLM, đánh giá và `report.md`.
- `report.html`, `report.pdf`: Báo cáo từ cùng lượt chạy. Chương trình dùng Chrome/Edge headless có sẵn để xuất PDF. Nếu máy không có trình duyệt phù hợp, đặt đường dẫn `CHROME_PATH` hoặc mở HTML và in PDF. Python không tự cài trình duyệt.
- `runs/<run>/figures/`: Năm hình từ dữ liệu. Hình LLM chỉ sinh khi có dự đoán LLM hợp lệ.
- `data/samples/manual_labels.csv`: Mẫu nhãn trống cho người đọc, được giữ nguyên khi chạy lại.

Những tệp chứa văn bản review chỉ lưu cục bộ. Bản tải mã nguồn không đóng gói dữ liệu thô, review hoặc tên người đánh giá. Với bài nộp chính thức trong repo riêng tư, chuẩn bị tệp nhãn tay theo yêu cầu môn và xem lại phạm vi dữ liệu được phép bàn giao.

## Nhãn tay và so sánh hai phương pháp

Mẫu 160 review gồm 40 review phát triển và 120 review kiểm tra. Chọn `split` được ghi sẵn. Người đọc điền các cột sau trước khi xem dự đoán:

- `sentiment`: Một trong `positive`, `mixed`, `negative`.
- `aspects_json`: Mảng JSON. Mỗi phần tử có `aspect` và `polarity`. Các khía cạnh là `location`, `cleanliness`, `host`, `amenities`, `noise`, `value`. Hai sắc thái `praised` và `criticized` có thể cùng có ở một khía cạnh. Khi không có khía cạnh nào, điền `[]`.
- `language`: Mã hai chữ thường như `pt`, `en`, `fr`, `es`, hoặc `und` nếu chưa xác định.
- `annotator`: Mã người gán do nhóm tự quy ước, không bắt buộc ghi tên thật.

Không dùng nhãn baseline hoặc mô hình làm nhãn người. Nếu đổi mẫu, giữ tệp nhãn cũ ở nơi riêng rồi tạo tệp cho mẫu mới. Chương trình từ chối dùng nhãn khi ID, văn bản hoặc phân chia không khớp. Nó không ghi đè các nhãn đã điền.

Baseline dùng từ vựng tiếng Anh/Bồ Đào Nha và quy tắc đơn giản. Nhãn cảm xúc mặc định `mixed` khi không có dấu hiệu, phát hiện ngôn ngữ ngoài phạm vi có thể trả `und`. Đây là một đối chứng yếu có chủ đích, chưa được khẳng định chính xác trên mọi ngôn ngữ.

Khi có ít nhất 100 nhãn kiểm tra hoàn chỉnh, chương trình đo accuracy và macro F1 cho cảm xúc/ngôn ngữ, micro F1 theo cặp khía cạnh–sắc thái. Các nhãn cảm xúc vắng mặt vẫn có F1 bằng 0 trong macro trên ba nhãn đã khai báo. Nhãn ngôn ngữ dùng hợp các mã ở nhãn người và dự đoán. Dự đoán lỗi hoặc thiếu được tính là bỏ sót, độ phủ được báo riêng.

## Gọi Gemini thật

Đối chiếu tên model và hạn mức tại [tài liệu Gemini](https://ai.google.dev/gemini-api/docs/models). Cấu hình không điền sẵn một model giả định đã được kiểm thử. Chỉ dùng tên model thực sự khả dụng với tài khoản của bạn.

PowerShell:

```powershell
$env:GEMINI_API_KEY = Read-Host 'Khóa API cục bộ'
python run_pipeline.py --config configs/porto.json --run-llm --model <ten-model-hop-le> --llm-limit 300
```

Không đưa khóa vào dòng lệnh hoặc repo. `.env.example` chỉ là ví dụ tên biến, Python không tự nạp tệp này. Chương trình gửi khóa trong header, không ghi giá trị khóa vào log. Các bài review sẽ được gửi tới dịch vụ khi bạn bật chế độ này.

Adapter giới hạn retry cho lỗi tạm thời, kiểm schema và nhãn, rồi lưu cache theo ID, nội dung, model, prompt và tham số. Lỗi không được lưu như thành công. Lần chạy sau có thể thử lại review lỗi. `--skip-llm` không dùng baseline làm dự đoán LLM và không tạo accuracy/F1 giả khi thiếu nhãn người.

Lệnh mặc định không gọi API, không phát sinh phí dịch vụ. Chi phí xử lý toàn bộ review cần tính từ usage token của lần gọi thật và bảng giá tại thời điểm chạy. Chưa gọi API thì chưa có số đo chi phí thực tế để báo cáo.

## Phạm vi kết luận

Giá là giá chào mốc cuối. Số ngày không sẵn có không xác nhận đặt phòng. Giao listing qua bốn mốc loại các listing mới hoặc biến mất, nên mẫu không đo tăng trưởng thị trường. Cửa sổ calendar ở từng snapshot nhìn về tương lai. Các kết quả theo mẫu cần ghi rõ N, không suy thành toàn thành phố.

## Kiểm thử

```bash
python -m unittest discover -s tests -v
```

Các fixture kiểm thử là giả định và nằm riêng, không được dùng để thay nguồn của lần chạy dữ liệu thật.

## Tài liệu tham khảo

- [Inside Airbnb](https://insideairbnb.com/get-the-data/), giấy phép CC BY 4.0.
- [Giả thiết và giới hạn](https://insideairbnb.com/data-assumptions/).
- [Gemini REST và đầu ra có cấu trúc](https://ai.google.dev/gemini-api/docs/structured-output).
