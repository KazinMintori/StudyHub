# Nguồn và đối chiếu đề bài tập lớn Inside Airbnb

Trang trình bày: `docs/xu-ly-du-lieu/bai-tap-lon/index.md`.
Trang kế hoạch và thực hành Porto: `docs/xu-ly-du-lieu/bai-tap-lon/thuc-hanh.md`.

Hai bản HTML được tải nguyên vẹn ngày 19/10/2026. `source-manifest.json` ghi URL, số byte và SHA256. Tệp `.gitattributes` giữ nguyên byte HTML khi checkout. Các tệp `.txt` là bản trích văn bản để đọc, không thay bản HTML lưu trữ.

`coverage.json` đối chiếu 54 nhóm yêu cầu, lựa chọn, thông tin và ví dụ với vị trí trong bản diễn giải. Các nhóm bao gồm toàn bộ nội dung giao nhiệm vụ của trang nguồn, kể cả lịch nộp, quyền sử dụng AI, cấu hình mẫu, cấu trúc repo và điều kiện chấm. Marker chỉ giúp phát hiện nội dung bị xóa ngoài ý muốn, không thay việc đọc so sánh từng yêu cầu.

Danh sách thành phố được trích từ từng thẻ `article.city` của HTML vào `src/content/courses/xu-ly-du-lieu/project/cities.json`. Có 26 thành phố, mỗi thành phố bốn ngày. Giữ nguyên tên, đường dẫn, các ngày và dấu hiệu thu thập hằng tháng của bốn thành phố. Bộ kiểm thử đối chiếu trực tiếp với HTML, không chỉ kiểm số lượng.

## Cách diễn giải

- Giải thích thuật ngữ trước hoặc ngay tại nơi cần dùng, rồi nối yêu cầu với thao tác và tệp kết quả.
- Giữ các điều bắt buộc, nhưng không nâng lựa chọn của nhóm hoặc giá trị mẫu thành quy định mới.
- Không ấn định mô hình Gemini, schema JSON, thư viện Python, số người gán nhãn, số hình hoặc ngưỡng QA khi đề chưa ấn định.
- Giữ rõ format PDF và trọng số rubric sẽ được công bố sau.
- Phần LLM phải có khả năng gọi thật bằng khóa người chấm. Cache không thay khả năng này.
- Phân biệt snapshot với kỳ sự kiện, listing với host/review, và trạng thái lịch với bằng chứng có giao dịch đặt phòng.
- Phân biệt yêu cầu của đề với lựa chọn triển khai của ví dụ độc lập.

Antigravity được giao đọc nguồn và rà văn phong trong worktree A, chỉ được ghi các tệp QA. Bản hướng dẫn đầu có một số khái quát không được nhận vào trang, như coi YAML là lựa chọn duy nhất, dùng tần suất lỗi không có số liệu hoặc coi cache chỉ theo review ID là đủ. Mọi đề xuất được đối chiếu lại với nguồn và bản thảo trước khi áp dụng. Biên bản và ảnh QA chi tiết nằm trong `qa/airbnb-project-20261019/`, được Git bỏ qua.

## Kiểm tra

```sh
node scripts/verify-data-project.mjs
node --test scripts/tests/data-project.test.mjs
python .agents/skills/studyhub-lecture/scripts/review_teaching_text.py --format text docs/xu-ly-du-lieu/bai-tap-lon/index.md docs/xu-ly-du-lieu/bai-tap-lon/thuc-hanh.md
```

Các kiểm tra liên quan còn gồm bộ câu hỏi ôn thi để xác nhận điều hướng cũ vẫn hoạt động, các kiểm thử chức năng, công cụ bài giảng và mô hình nội dung. Trình duyệt kiểm hai trang, sidebar, font, bảng, mã, thẻ thành phố và chữ hoa sau dấu hai chấm ở 360 px, 375 px và 1280 px, cả sáng lẫn tối. Toàn bộ build và deploy do GitHub Actions thực hiện, không build toàn site cục bộ.

## Kế hoạch và lượt thực hành Porto

Trang đầu giữ 54 nhóm yêu cầu trong các mục mở rộng, đồng thời bổ sung sơ đồ xử lý và bản tóm tắt sản phẩm cần nộp. Bảy khối mã của bản trước vẫn giữ nguyên. Rubric trong ảnh được phân biệt với các thông tin còn chờ công bố trên trang đề, không tự thay bốn snapshot thành ba.

Kế hoạch gồm 8 giai đoạn và 24 công việc có đầu ra, điều kiện nghiệm thu và quan hệ phụ thuộc. Bảng kế hoạch riêng của người dùng chỉ được đọc để hiểu cách phối hợp. Không lưu workbook, URL, tên thành viên, phân công hoặc bản sao các hàng của nhóm.

`examples/airbnb-porto/` là dự án Python chạy trên 13 tệp công khai thật, không sinh dữ liệu thay thế khi tải thất bại. Lượt công bố chọn 120 listing thuộc giao 12.453 ID qua bốn snapshot và xử lý 480 hàng listing, 13.842 hàng calendar trong cửa sổ đã chọn. Mẫu phân tích văn bản có 300 review duy nhất. Dữ liệu thô và nội dung review không nằm trong gói tải mã nguồn hoặc bản xuất công khai.

Sáu KPI không phụ thuộc LLM đã được tính. Một chương trình độc lập đọc lại nguồn bằng pandas và Decimal để đối chiếu cả bốn snapshot. Nhánh API, cache và chấm nhãn có mã nguồn, nhưng lượt này chưa gọi LLM và chưa có nhãn người để công bố accuracy/F1.

Năm hình SVG và báo cáo PDF được tạo từ cùng lượt chạy. Bản đồ dùng GeoJSON nguồn, giữ hình đủ lớn và đưa bảng khu vực ra ngoài SVG để tránh co toàn hình theo một danh sách chú giải dài. `porto-example-verification.json` ghi cấu hình, kết quả và hash của các tệp công bố.

Hai tác vụ Antigravity trong worktree A/B lưu được bản nháp và nhận xét nhưng không có trạng thái công cụ thành công. Một lượt sửa hết thời gian, các lượt khác gặp lỗi truyền NoneType. Codex đọc từng đề xuất, loại các cách tự bù dữ liệu và khẳng định thiếu cơ sở, rồi kiểm chứng bản tích hợp độc lập. Kiểm tra sau tác vụ xác nhận 41 và 48 tệp có sẵn trong hai worktree không đổi.

## Bổ sung từ lượt đọc như sinh viên và nguồn tham khảo

Người dùng yêu cầu Antigravity đóng vai sinh viên biết Python cơ bản và mới học môn xử lý dữ liệu. Bản ghi lượt đọc đầu được lưu trước khi cung cấp bản sửa. Đây là mô phỏng vai đọc, không phải khảo sát người học thật. Những nhận xét được đối chiếu lại với đề trước khi bổ sung hướng dẫn. Ví dụ, không nhận đề xuất bỏ yêu cầu KPI trong báo cáo QA hoặc mặc định GeoJSON mọi mốc giống nhau.

`airbnb-reference-google-doc.txt` lưu bản xuất văn bản nguyên vẹn từ Google Docs do người dùng gửi. `reference-manifest.json` ghi nguồn và hash, `reference-comparison.json` ghi 15 điểm đối chiếu. Ở lượt đầu chưa có bảng giao dữ liệu để hiểu những chi tiết riêng được ghi lại trong tài liệu.

Sau đó, người dùng cung cấp một bảng giao dữ liệu và yêu cầu chỉ tham khảo cấu trúc, không lấy thông tin cụ thể. Bảng được đọc trong bộ nhớ, không lưu workbook hoặc dữ liệu hàng vào repo. `assigned-input-guidance.json` chỉ ghi các vai trò đầu vào và thao tác cần giải thích. Không lưu URL của bảng, thông tin cá nhân, mã nhóm, ID thật hoặc tọa độ thật. Mục 15 trên website được viết lại bằng mã giả định, thay cho việc nhắc lại các số lượng riêng trong ghi chú cũ.

Hướng dẫn bổ sung phân biệt danh sách mã với dữ liệu chi tiết, cách lọc listings/calendar/reviews, mẫu LLM với mẫu nhãn tay, vùng được giao với khu vực hành chính, cùng việc đối chiếu đầu vào trước khi QA. Các điều kiện riêng được giữ trong phạm vi hướng dẫn của bộ giao, không biến thành định mức chung. Toàn bộ 54 nhóm yêu cầu của đề công khai vẫn được đối chiếu riêng.

Đã vào trang Get the Data và Data Assumptions của Inside Airbnb, đồng thời đọc Data Dictionary do trang đó liên kết. Các bản nguồn được lưu và kiểm hash bằng `data-source-manifest.json`. `insideairbnb-santiago-download-links.json` giữ bảy liên kết tại một snapshot. `insideairbnb-file-inspection.json` ghi kết quả đọc hàng tiêu đề sáu bảng và cấu trúc GeoJSON của Santiago ngày 23/09/2026.

Chỉ đọc luồng đến hàng tiêu đề cho các CSV hoặc CSV nén, không tải toàn bộ chúng vào repo. Phần GeoJSON được đọc để xác định cấu trúc và thuộc tính. Không dùng việc đọc cấu trúc để khẳng định số hàng, chất lượng dữ liệu hoặc kết quả kinh doanh. Đặc biệt, calendar được kiểm tra không có cột giá, còn reviews tổng hợp không có comments. Những thay đổi schema đó được nêu rõ để tránh áp dụng một mô tả cũ cho mọi snapshot.

Các giải thích bổ sung gồm bước bắt đầu, tệp nén, khóa nối, hình học khu vực, mẫu nhãn tay, cách chấm đa nhãn, thời điểm hoàn thiện báo cáo QA và phạm vi cache. Chưa viết chương trình thực hành hoặc gọi LLM thật. Ví dụ chấm nhãn nhỏ được tính lại bằng Python, bằng chứng nằm trong `qa/airbnb-student-review-20261019/metric-example.json`.

Hai minh họa được thêm để nhận diện đầu vào. Ảnh tải tệp là ảnh chụp nguyên trạng cột tên tệp công khai trên Inside Airbnb, không chụp bảng giao dữ liệu. Hình vùng là SVG minh họa giả định với hai listing và hai vùng, không dùng tọa độ thật. `illustrations.json` ghi nguồn, phương pháp và hash của các ảnh.
