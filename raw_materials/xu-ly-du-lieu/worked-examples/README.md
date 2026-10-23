# Ví dụ Python trong bài giảng xử lý dữ liệu

Mỗi tệp JSON lưu vị trí chèn, đề dẫn, mã hoàn chỉnh và lời giải của một bài. `verified-results.json` lưu kết quả thực thi và SHA-256 của đúng đoạn mã được đưa lên trang. Chỉ chấp nhận kết quả có trạng thái `passed` và mã băm khớp.

Chạy lại các ví dụ bằng môi trường Python có NumPy, pandas và các thư viện được dùng trong bài:

```powershell
python scripts/run-data-teaching-examples.py raw_materials/xu-ly-du-lieu/worked-examples --output qa/data-teaching-20261022/reproduced.json --jobs 3
```

Mỗi ví dụ chạy trong thư mục tạm và tiến trình riêng. Công cụ chặn truy cập mạng, thu bảng ngay lúc `print` được gọi và giữ kết quả trước các phép sửa dữ liệu tiếp theo. Đầu ra bảng được hiển thị bằng bảng HTML, có xử lý ký tự đặc biệt và giá trị thiếu. Mã Python được giữ nguyên từng ký tự.

Sau khi đối chiếu kết quả và lời giải, chấp nhận đầu ra mới và xuất các hình đã chạy thành SVG:

```powershell
python scripts/integrate-data-teaching-examples.py --results qa/data-teaching-20261022/reproduced.json
python scripts/integrate-data-teaching-examples.py --check
node scripts/qa/verify-data-teaching-browser.mjs
```

Lệnh tích hợp chỉ thay các khối có dấu `worked-example`. Bài tập, lời giải đã có, frontmatter và liên kết của bài được giữ lại. Lệnh kiểm tra trình duyệt dùng máy chủ dev cục bộ tại cổng 5193, kiểm từng bài ở bốn bề rộng và hai giao diện sáng/tối. Không cần build toàn bộ website trên máy cục bộ.

Lượt xác minh này dùng Python 3.14.7, pandas 3.0.5 và NumPy 2.5.2. Các ví dụ còn sử dụng Matplotlib, Seaborn, scikit-learn, statsmodels, Patsy, IPython, openpyxl và pyarrow. Bộ kiểm tra hình chạy với backend Agg, nên lời gọi `plt.show()` phát cảnh báo không có cửa sổ tương tác. Hình thực tế vẫn được thu từ Figure và lưu thành SVG.

Các con số phụ thuộc môi trường, như phiên bản gói hoặc dung lượng đối tượng Python, cần được diễn giải theo môi trường đã chạy. Kết quả trên dữ liệu minh họa không tự chứng minh tốc độ chạy, quan hệ nhân quả hoặc khả năng dự báo trên dữ liệu mới.
