# Nhận xét từ lượt đọc mô phỏng sinh viên mới học

Người dùng yêu cầu một lượt Antigravity bắt đầu bằng vai đọc sau: “Bạn là một sinh viên có kiến thức cơ bản về python và mới học môn lập trình xử lý dữ liệu này”. Bản đề trước chỉnh sửa được đưa cho người rà độc lập, chưa kèm nguồn chính thức, ghi chú Google Docs hoặc gợi ý trả lời của tác giả.

Đây là mô phỏng vai đọc bằng tác tử AI, không phải khảo sát sinh viên thật và không chứng minh mọi người học sẽ hiểu như nhau. Không dùng điểm phần trăm để nhận xét độ dễ hiểu.

## Kết quả lượt đầu

Người rà kể lại được các sản phẩm phải nộp, các bước dự định làm trong buổi đầu, nơi lưu tệp và trách nhiệm vấn đáp. Tuy vậy, người rà còn đặt ra 10 câu hỏi, trong đó quan trọng nhất là thời điểm ghi KPI trước/sau QA, phạm vi đối chứng của baseline, việc đọc bảng calendar lớn và gán nhãn review ngoại ngữ.

Nhận xét này cho thấy bản cũ giúp nắm yêu cầu nhưng còn thiếu một số bước giải thích để bắt đầu. Những câu hỏi được dùng để cải thiện lời giảng, còn các kết luận kỹ thuật do người rà tự suy ra vẫn phải được kiểm tra riêng.

## Các điểm đã chỉnh trong trang

| Câu hỏi từ lượt đọc | Cách xử lý sau đối chiếu |
| --- | --- |
| QA đứng trước KPI thì ghi KPI trước/sau bằng cách nào? | Giữ trạng thái cần so sánh, ghi số dòng khi QA chạy và hoàn thiện các cột KPI sau khi đã có đầu vào. Tệp báo cáo có thể được hoàn thiện cuối quy trình. Không bỏ yêu cầu KPI để chỉ ghi số dòng. |
| Calendar lớn có cần đưa mọi snapshot vào RAM? | Giải thích đọc một phần, chọn cột hoặc theo khối và giữ đơn vị listing–ngày. Không chép khẳng định chưa đo về số triệu dòng hay chắc chắn treo máy. |
| GeoJSON có phải chỉ tải một bản cho mọi snapshot? | Giải thích URL theo mốc và việc lưu dấu vết từng mốc. Chỉ tái sử dụng sau khi xác minh, không mặc định các ranh giới giống hệt nhau. |
| Đọc `.csv.gz` thế nào? | Nêu Python gzip, khả năng đọc nén của thư viện bảng và việc dùng CSV parser cho nội dung sau giải nén. |
| Tên biến môi trường của khóa API là gì? | Phải nhất quán giữa mã, `.env.example` và README. Không tự tạo một tên bắt buộc của môn khi đề chưa nêu. |
| Baseline cần so những đầu ra nào? | So cùng nhiệm vụ, cùng nhãn tay và cách chấm. Giữ yêu cầu LLM trích đủ ba loại thông tin, còn quy cách đánh giá chi tiết đối chiếu hướng dẫn chấm khi có. |
| Chấm danh sách nhiều khía cạnh ra sao? | Phân biệt khớp cả tập nhãn với đếm nhãn đúng/thừa/bỏ sót, giải thích micro và macro. Ví dụ nhỏ đã được tính lại bằng Python. |
| Không hiểu ngoại ngữ của review thì gán nhãn tay thế nào? | Không đoán nhãn hay dùng chính LLM đang chấm làm chuẩn. Nêu lựa chọn phạm vi có thể đọc, hỗ trợ của người hiểu ngôn ngữ và điều kiện xác nhận nếu mẫu được giao cố định. |
| Cache và `--skip-llm` hoạt động khác nhau ra sao? | Phân biệt dùng lại kết quả phù hợp, bỏ bước gọi mới và trường hợp thiếu đầu vào phải báo rõ. Không làm mất khả năng gọi thật khi chấm. |
| Để từ điển dữ liệu ở đâu? | Có thể đặt tệp riêng trong reports và chỉ đường dẫn, nhưng không suy ra ngoại lệ về giới hạn PDF khi format chưa công bố. |

Đã thêm bảng bước bắt đầu với dấu hiệu hoàn thành, giải thích mã định danh khác index, và phần phân biệt bảy loại tệp trên Inside Airbnb. Bản ghi Google Docs được đọc như nguồn tham khảo, với 15 điểm đối chiếu thay vì áp các con số riêng của ghi chú vào đề chung.

## Những suy luận của người rà không được nhận nguyên trạng

- Không có bằng chứng mọi calendar có một số triệu dòng cố định hoặc chắc chắn gây lỗi bộ nhớ trên mọi máy.
- Không có bằng chứng GeoJSON không đổi giữa mọi snapshot.
- Cache định dạng JSONL, tên mô-đun và đuôi hình PNG là cách tổ chức minh họa, không phải các lựa chọn duy nhất đã được đề ấn định.
- Tối đa 10 trang bao gồm trường hợp đúng 10 trang, không phải chỉ dưới 10 trang.
- Việc câu hỏi đánh giá còn cần thông tin riêng của lớp không cho phép tự đặt thêm quy định rồi gọi đó là đề chính thức.

## Bằng chứng và giới hạn

Các bản ghi nguyên trạng của Antigravity được giữ trong thư mục QA của worktree B và bản sao tại `qa/airbnb-student-review-20261019/agy/`. Tác tử chỉ được tạo tệp đánh giá, không sửa nội dung website. Hash của các tệp có sẵn được so sánh sau lượt làm.

Cả hai lượt bridge kết thúc bằng lỗi `NoneType` sau khi đã lưu báo cáo. Các nhận xét chỉ được nhận sau khi đọc và đối chiếu lại, không xem lỗi transport là trạng thái thành công. Lượt đọc lại được theo dõi và lưu riêng, không viết đè kết luận lần đầu.

## Nhận xét sau khi đọc lại bản sửa

Trong bản đánh giá lại, Antigravity nói đã xác định được việc cần làm từ buổi đầu đến bàn giao, gồm đọc đúng dữ liệu, thiết kế QA, ghi báo cáo, chuẩn bị nhãn và nối các bước. Chín câu hỏi ban đầu được phân loại đã giải thích. Một câu hỏi còn phụ thuộc hướng dẫn chấm chi tiết là phạm vi đối chứng baseline cho từng trường trích xuất.

Các mức phân loại trên là nhận xét của lượt mô phỏng, không chuyển thành tỷ lệ dễ hiểu hoặc cam kết mọi sinh viên đã tự cài được chương trình. Bản sửa giữ những điều chưa thể xác nhận từ nguồn, thay vì bịa quy định để đánh dấu mọi mục đã xong.

Sau khi đọc báo cáo lại, tác giả cũng giới hạn ba suy luận còn quá rộng của người rà:

- Giải thích micro và macro không có nghĩa bắt buộc báo cáo cả hai cách trong mọi bài. Nhóm phải ghi rõ cách chọn và so sánh nhất quán.
- Gợi ý chọn review thuộc ngôn ngữ có thể đọc không cho phép tự đổi một tập mẫu cố định do giảng viên giao.
- Nêu cách dùng cache hoặc để từ điển dữ liệu ở tệp riêng là hướng dẫn thiết kế, không bổ sung một rubric mới hay ngoại lệ số trang PDF.
