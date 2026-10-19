# Nguồn và đối chiếu đề bài tập lớn Inside Airbnb

Trang trình bày: `docs/xu-ly-du-lieu/bai-tap-lon/index.md`.
Trang dành cho phần thực hành sau này: `docs/xu-ly-du-lieu/bai-tap-lon/thuc-hanh.md`.

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
- Không tạo ví dụ dự án, dữ liệu phân tích hay kết quả thực nghiệm cho phần 2 trong lượt này.

Antigravity được giao đọc nguồn và rà văn phong trong worktree A, chỉ được ghi các tệp QA. Bản hướng dẫn đầu có một số khái quát không được nhận vào trang, như coi YAML là lựa chọn duy nhất, dùng tần suất lỗi không có số liệu hoặc coi cache chỉ theo review ID là đủ. Mọi đề xuất được đối chiếu lại với nguồn và bản thảo trước khi áp dụng. Biên bản và ảnh QA chi tiết nằm trong `qa/airbnb-project-20261019/`, được Git bỏ qua.

## Kiểm tra

```sh
node scripts/verify-data-project.mjs
node --test scripts/tests/data-project.test.mjs
python .agents/skills/studyhub-lecture/scripts/review_teaching_text.py --format text docs/xu-ly-du-lieu/bai-tap-lon/index.md docs/xu-ly-du-lieu/bai-tap-lon/thuc-hanh.md
```

Các kiểm tra liên quan còn gồm bộ câu hỏi ôn thi để xác nhận điều hướng cũ vẫn hoạt động, các kiểm thử chức năng, công cụ bài giảng và mô hình nội dung. Trình duyệt kiểm hai trang, sidebar, font, bảng, mã, thẻ thành phố và chữ hoa sau dấu hai chấm ở 360 px, 375 px và 1280 px, cả sáng lẫn tối. Toàn bộ build và deploy do GitHub Actions thực hiện, không build toàn site cục bộ.

## Bổ sung từ lượt đọc như sinh viên và nguồn tham khảo

Người dùng yêu cầu Antigravity đóng vai sinh viên biết Python cơ bản và mới học môn xử lý dữ liệu. Bản ghi lượt đọc đầu được lưu trước khi cung cấp bản sửa. Đây là mô phỏng vai đọc, không phải khảo sát người học thật. Những nhận xét được đối chiếu lại với đề trước khi bổ sung hướng dẫn. Ví dụ, không nhận đề xuất bỏ yêu cầu KPI trong báo cáo QA hoặc mặc định GeoJSON mọi mốc giống nhau.

`airbnb-reference-google-doc.txt` lưu bản xuất văn bản nguyên vẹn từ Google Docs do người dùng gửi. `reference-manifest.json` ghi nguồn và hash, `reference-comparison.json` ghi 15 điểm đối chiếu. Các số lượng trong ghi chú chưa có trên đề chung được phân biệt rõ với yêu cầu đã xác nhận. Chưa có bảng phân công hoặc tệp đánh dấu X được gửi kèm để kiểm tra những điều kiện riêng ấy.

Đã vào trang Get the Data và Data Assumptions của Inside Airbnb, đồng thời đọc Data Dictionary do trang đó liên kết. Các bản nguồn được lưu và kiểm hash bằng `data-source-manifest.json`. `insideairbnb-santiago-download-links.json` giữ bảy liên kết tại một snapshot. `insideairbnb-file-inspection.json` ghi kết quả đọc hàng tiêu đề sáu bảng và cấu trúc GeoJSON của Santiago ngày 23/09/2026.

Chỉ đọc luồng đến hàng tiêu đề cho các CSV hoặc CSV nén, không tải toàn bộ chúng vào repo. Phần GeoJSON được đọc để xác định cấu trúc và thuộc tính. Không dùng việc đọc cấu trúc để khẳng định số hàng, chất lượng dữ liệu hoặc kết quả kinh doanh. Đặc biệt, calendar được kiểm tra không có cột giá, còn reviews tổng hợp không có comments. Những thay đổi schema đó được nêu rõ để tránh áp dụng một mô tả cũ cho mọi snapshot.

Các giải thích bổ sung gồm bước bắt đầu, tệp nén, khóa nối, hình học khu vực, mẫu nhãn tay, cách chấm đa nhãn, thời điểm hoàn thiện báo cáo QA và phạm vi cache. Chưa viết chương trình thực hành hoặc gọi LLM thật. Ví dụ chấm nhãn nhỏ được tính lại bằng Python, bằng chứng nằm trong `qa/airbnb-student-review-20261019/metric-example.json`.
