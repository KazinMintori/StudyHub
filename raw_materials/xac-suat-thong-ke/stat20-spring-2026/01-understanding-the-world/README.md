# Stat 20 — Understanding the World with Data

Nguồn: UC Berkeley, Stat 20, học kỳ xuân 2026. Tải ngày 08-10-2026.

- Trang gốc: https://stat20.berkeley.edu/spring-2026/1-questions-and-data/01-understanding-the-world/notes.html
- Hình gốc: https://stat20.berkeley.edu/spring-2026/1-questions-and-data/01-understanding-the-world/images/claims.png
- Thông báo giấy phép: https://stat20.berkeley.edu/spring-2026/license.html
- Điều khoản CC BY 4.0: https://creativecommons.org/licenses/by/4.0/

`notes.html`, `claims.png` và `license.html` giữ nguyên dữ liệu tải về. Bài giảng tại `docs/xac-suat-thong-ke/bai-giang/00-hieu-the-gioi-bang-du-lieu.md` được biên tập độc lập cho StudyHub. Các định nghĩa và sơ đồ chuyển thể được chia sẻ theo CC BY 4.0; thông tin nguồn và giấy phép nằm trong phần Tài liệu tham khảo.

| Đơn vị nguồn | Cách xử lý trong bài giảng |
| --- | --- |
| Tiêu đề Understanding the World with Data | Tiêu đề bài trong frontmatter và catalog |
| Intro and Syllabus, lời chào, câu hỏi đọc bài | Bỏ phần tổ chức khóa học bên ngoài theo yêu cầu người dùng |
| Tên giảng viên/trợ giảng, đề cương/Ed, bài thực hành đầu tiên | Bỏ phần tổ chức khóa học bên ngoài |
| Mục tiêu xây dựng và phản biện phát biểu từ dữ liệu, câu hỏi về các loại phát biểu | Đoạn mở và sơ đồ trong mục 1 |
| Sơ đồ Types of Claims | SVG nhãn Việt trong mục 1; ghi nguồn tại mục 4 |
| Summary: Định nghĩa và ví dụ | Mục 1.1, giữ khảo sát lớp học và tỷ lệ 70% người trả lời chưa có kinh nghiệm viết mã |
| Generalization: Định nghĩa và ví dụ | Mục 1.2, giữ bước suy rộng từ khảo sát lớp sang sinh viên toàn trường và tỷ lệ 70% |
| Causal Claim: Định nghĩa và ví dụ | Mục 1.3, giữ thí nghiệm ngẫu nhiên có đối chứng và kháng sinh loại bỏ hơn 99% ca nhiễm khuẩn |
| Prediction: Định nghĩa và ví dụ | Mục 1.4, giữ tin tức, giá Uber hôm nay và dự đoán tăng 1,2% ngày mai |
| Other Links / Slides, điều hướng trước và sau | Bỏ các liên kết điều hướng sang khóa học bên ngoài |

Các định nghĩa, thứ tự bốn loại phát biểu và ví dụ chính ở mục 1 bám theo Berkeley. Tên lớp được viết là “một lớp học”, nhóm sinh viên của trường được viết là “sinh viên toàn trường” để bỏ nhận diện khóa học mà giữ phạm vi suy luận. Các phát biểu về thuốc và cổ phiếu là ví dụ để phân loại, không phải kết quả y khoa hay dự báo hiện tại do StudyHub xác minh. Mục 2–3 mở thêm bước giải thích và luyện tập. Slides giữ ví dụ chính của Notes. Nguồn và giấy phép chỉ nằm trong phần Tài liệu tham khảo.

Phạm vi người dùng chốt ngày 09-10-2026: Toàn bộ nội dung Notes của đúng URL đã gửi; không nhập bộ Slides, Lab hoặc toàn khóa. Giữ mọi nội dung học thuật, chỉ bổ sung giải thích. Ngoại lệ người dùng yêu cầu loại bỏ: Tên khóa học, tên trường và thông tin tổ chức gắn với bên nguồn (lời chào, giảng viên, đề cương, diễn đàn, bài nộp và điều hướng). Nguồn và giấy phép chỉ đặt ở Tài liệu tham khảo theo yêu cầu trước đó. Kiểm kê `notes-coverage.json` ghi từng đơn vị học thuật và nơi xuất hiện.

Phạm vi người dùng chốt ngày 09-10-2026: Toàn bộ nội dung Notes của đúng URL đã gửi; không nhập bộ Slides, Lab hoặc toàn khóa. Giữ mọi nội dung học thuật, chỉ bổ sung giải thích. Ngoại lệ người dùng yêu cầu loại bỏ: Tên khóa học, tên trường và thông tin tổ chức gắn với bên nguồn (lời chào, giảng viên, đề cương, diễn đàn, bài nộp và điều hướng). Nguồn và giấy phép chỉ đặt ở Tài liệu tham khảo theo yêu cầu trước đó. Kiểm kê `notes-coverage.json` ghi từng đơn vị học thuật và nơi xuất hiện.

Chạy `python -I raw_materials/xac-suat-thong-ke/stat20-spring-2026/01-understanding-the-world/verify_numbers.py` để kiểm tra các phép tính và vị trí phần tham khảo.
