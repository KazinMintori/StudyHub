---
title: "Đề bài tập lớn: Phân tích thị trường Airbnb"
description: "Giải thích đầy đủ yêu cầu, dữ liệu, sản phẩm bàn giao và cách đánh giá bài tập lớn Inside Airbnb."
course: xu-ly-du-lieu
section: project
outline: [2, 3]
prev: false
next: false
---

<script setup>
import ProjectSections from '../../../src/features/course-project/components/ProjectSections.vue'
import ProjectCities from '../../../src/features/course-project/components/ProjectCities.vue'
</script>

<ProjectSections active="brief" />

# Đề bài tập lớn: Phân tích thị trường Airbnb

Một bên đặt hàng, chẳng hạn chính quyền thành phố hoặc hiệp hội du lịch, cần hiểu thị trường cho thuê chỗ ở tại một thành phố. Họ muốn biết giá cả khác nhau giữa các khu vực ra sao, thị trường thay đổi thế nào qua các lần thu thập dữ liệu, và khách đang khen hoặc phàn nàn về điều gì. Nhóm của bạn sẽ xây dựng một chương trình để đi từ các tệp dữ liệu đến những câu trả lời có bằng chứng.

Sản phẩm gồm mã nguồn chạy lại được và một báo cáo giải thích quá trình xử lý, kết quả, cùng giới hạn của các kết luận. Người khác phải có thể làm theo hướng dẫn, chạy chương trình và tạo lại các tệp kết quả. Việc chỉ lưu sẵn hình hoặc output trong notebook chưa đáp ứng yêu cầu đó.

Đây là bài tập lớn Inside Airbnb của học phần Lập trình xử lý dữ liệu, mã UET.DSE2049, học kì 1 năm học 2026–2027, thuộc Viện Trí tuệ nhân tạo, Trường Đại học Công nghệ, ĐHQGHN. Bài tập lớn và vấn đáp chiếm **60% điểm học phần**. Các mốc, danh sách dữ liệu và điều kiện bàn giao trong trang này được đối chiếu với [đề bài chính thức](https://courses.iaidev.com/programming-for-data-processing/2627-1/projects/project_airbnb.html).

[Ghi chú diễn giải được cung cấp thêm](https://docs.google.com/document/d/17hqvglaYTn27vNw7siVPxpMGhL6goMkDngQfSOMF8NY/edit?tab=t.0) có một số thông tin khác với trang đề. Những điểm cần đối chiếu được giải thích tại [mục 15](#doi-chieu-ghi-chu), đặc biệt là thành phố, số lượng mẫu và cách chia khu vực. Nhóm cần phân biệt yêu cầu chung với thông báo bổ sung dành riêng cho dữ liệu được giao.

Nếu đang chuẩn bị tải dữ liệu, có thể đến ngay phần [phân biệt bảy loại tệp và cách nối các bảng](#cac-tep-du-lieu), rồi quay lại các bước QA và KPI sau khi hiểu đầu vào.

## 1. Cần hoàn thành những việc gì?

Nhóm cần hoàn thành các việc sau như những phần liên kết của cùng một sản phẩm:

1. Xác định người sẽ sử dụng báo cáo và câu hỏi họ cần trả lời.
2. Tải dữ liệu của thành phố được phân công tại đủ bốn mốc bắt buộc, bằng chương trình.
3. Khảo sát dữ liệu, đề xuất quy tắc phát hiện và xử lý vấn đề chất lượng, rồi ghi lại tác động của các quy tắc.
4. Tính 5–8 chỉ số phù hợp với người sử dụng báo cáo. Các chỉ số phải bao quát góc độ khu vực, thời gian và kết quả phân tích bằng LLM.
5. Dùng LLM để chuyển một mẫu đánh giá của khách thành dữ liệu có cấu trúc. So sánh với một phương pháp không dùng LLM và tự đo chất lượng bằng ít nhất 100 đánh giá được gán nhãn tay.
6. Tạo hình thể hiện các góc độ không gian, thời gian và LLM. Hình phải được chương trình sinh ra.
7. Viết báo cáo PDF tối đa 10 trang và chuẩn bị kho mã có thể chạy toàn bộ quy trình bằng một lệnh.
8. Ghi nhận trung thực việc dùng AI, nộp đúng mốc và chuẩn bị để mỗi thành viên giải thích được toàn bộ sản phẩm.

Phần dưới giải thích từng việc, các tệp cần có và những quyết định nhóm phải tự đưa ra. Các ví dụ giúp làm rõ yêu cầu, không thay cho một phương án bắt buộc áp dụng với mọi thành phố.

### Nếu hôm nay mới bắt đầu, nên làm việc gì trước?

Trước tiên, ghi lại thành phố và bốn snapshot được giao, xác nhận các thông báo bổ sung của giảng viên, rồi tạo repo và môi trường làm việc. Tiếp đó, thử tải và mở một bộ dữ liệu nhỏ để biết các tệp có cột gì và một hàng có ý nghĩa gì. Mục tiêu của buổi đầu là đọc được dữ liệu và hiểu đầu vào, chưa cần viết ngay toàn bộ chương trình.

Khi một bước chạy được, lưu kết quả và nối nó với bước tiếp theo. Bảng dưới là cách chia việc để bắt đầu, không phải một lịch nộp hoặc phương án cài đặt mới của đề:

| Bước chuẩn bị | Dấu hiệu cho thấy đã có thể chuyển sang bước tiếp |
| --- | --- |
| Chốt đầu vào và mục tiêu | Có thành phố, ngày snapshot, người đọc báo cáo và danh sách điều còn phải xác nhận. |
| Dựng môi trường và đọc thử dữ liệu | Gọi đúng Python của dự án, đọc được tệp, nêu được các cột khóa và ý nghĩa một hàng. |
| Viết chức năng tải dữ liệu | Truyền cấu hình vào chương trình, tải được đúng tệp và lưu vào thư mục của đúng snapshot. |
| Khảo sát rồi thử quy tắc QA | Mỗi quy tắc tìm được những hàng cụ thể, có lý do và hành động rõ, ghi được tác động. |
| Tính thử các KPI từ dữ liệu sau QA | Đối chiếu được ít nhất một phép tính trên mẫu nhỏ và giải thích được đơn vị, mẫu số. |
| Chuẩn bị review, nhãn tay và hai phương pháp | Giữ liên kết từ văn bản đến nhãn tay, dự đoán baseline và dự đoán LLM để chấm cùng các trường hợp. |
| Nối các bước, sinh hình và hoàn thiện báo cáo | Một lệnh đọc cấu hình, chạy các phần cần thiết và tạo ra các tệp đã mô tả trong README. |

“Xong bước” không chỉ nghĩa là chương trình không báo lỗi. Chẳng hạn, tải được một tệp nhưng nhầm ngày snapshot thì đầu vào vẫn sai. Phần thực hành sau sẽ minh họa một cách xây toàn bộ quy trình, còn tại đây nhóm cần hiểu công việc và cách tự xác nhận kết quả của từng bước.

## 2. Những từ cần hiểu trước khi bắt đầu

| Thuật ngữ | Hiểu trong bài tập này |
| --- | --- |
| Listing | Một mục đăng chỗ ở cho thuê trên Airbnb. Mã listing giúp nhận diện chỗ ở qua các bảng hoặc lần thu thập. |
| Host | Chủ tài khoản đăng chỗ ở. Một host có thể quản lý nhiều listing. Đếm host và đếm listing là hai việc khác nhau. |
| Snapshot, hay mốc chụp | Bộ dữ liệu được thu thập tại một ngày cụ thể. Bốn snapshot là bốn lần quan sát thị trường, không phải bốn quý có số liệu đầy đủ theo từng ngày. |
| QA | Kiểm soát chất lượng dữ liệu. Nhóm xác định dữ liệu có vấn đề gì, phát hiện bằng điều kiện nào và xử lý ra sao. |
| KPI | Chỉ số được chọn để trả lời một câu hỏi phân tích. Mỗi chỉ số cần có công thức, đơn vị và đối tượng được tính. |
| Pipeline, hay quy trình xử lý | Chuỗi công việc được chương trình thực hiện, từ tải dữ liệu đến xuất kết quả. Đầu ra của bước trước được dùng cho bước sau. |
| Tệp cấu hình | Tệp chứa lựa chọn như thành phố, các mốc dữ liệu và tham số phân tích. Đổi lựa chọn trong tệp này giúp chạy lại mà không sửa mã chương trình. |
| LLM | Mô hình ngôn ngữ lớn, được gọi qua API để đọc văn bản đánh giá và trích xuất thông tin. |
| API và khóa API | API là cách một chương trình gửi yêu cầu đến dịch vụ khác và nhận phản hồi. Khóa API là thông tin xác thực để dịch vụ nhận biết tài khoản gọi, cần được giữ bí mật. |
| Baseline, hay phương pháp đối chứng | Cách làm không dùng LLM để giải cùng nhiệm vụ. Kết quả của nó giúp đánh giá LLM có mang lại lợi ích trên dữ liệu đang xét hay không. |
| Nhãn tay | Kết quả do người đọc đánh giá và gán nhãn theo hướng dẫn thống nhất. Đây là dữ liệu tham chiếu để đo chất lượng của hai phương pháp. |
| Cache, hay kết quả lưu lại | Kết quả xử lý đã ghi ra tệp để tái sử dụng. Khi dùng lại kết quả LLM, cần xét cả nội dung đánh giá, mô hình và prompt, không chỉ mã review. |
| Tái lập kết quả | Chạy lại trên cùng đầu vào và môi trường đã ghi nhận để tạo lại các kết quả cần đối chiếu. Với LLM, còn phải lưu thông tin mô hình, prompt và tham số liên quan. |

## 3. Nhóm, người sử dụng báo cáo và kho mã

### 3.1. Nhận thành phố và xác định mục tiêu phân tích

Mỗi nhóm có 4–5 sinh viên và được giao một thành phố riêng, không trùng nhóm khác. Phân công chính thức được đăng trên Canvas Portal từ đầu kỳ. Nhóm cần kiểm tra đúng thành phố của mình trước khi tải dữ liệu.

Nhóm tự chọn bên đặt hàng phân tích và ghi rõ trong báo cáo. Đó có thể là chính quyền thành phố, một quỹ đầu tư hoặc hiệp hội du lịch. Việc chọn ai đọc báo cáo sẽ ảnh hưởng đến chỉ số cần tính và cách diễn giải.

Chẳng hạn, người muốn hiểu sự phân bố chỗ ở giữa các khu vực sẽ cần kết quả khác với người muốn biết các phàn nàn của khách tập trung ở đâu. Đây là ví dụ để hiểu vai trò của người sử dụng báo cáo. Nhóm phải tự chọn mục tiêu phù hợp và giải thích vì sao các kết quả của mình phục vụ mục tiêu đó.

Mỗi thành viên phải hiểu mã nguồn, số liệu và các quyết định của cả nhóm. Chia việc giúp tổ chức quá trình làm, nhưng không giới hạn trách nhiệm giải thích vào phần một người đã trực tiếp viết.

### 3.2. Tạo và sử dụng GitHub repo

Tạo một kho mã GitHub riêng tư và mời đủ thành viên cùng tài khoản giảng viên. Tên gợi ý là `2627-LTXLDL-Airbnb-<TenNhom>`. Điền liên kết repo vào bảng tính được yêu cầu trong môn học.

Git lưu lịch sử thay đổi của các tệp. Một commit là một mốc ghi nhận thay đổi trong lịch sử đó. Push đưa các commit từ máy cá nhân lên GitHub. Nhóm cần commit và push đều đặn từ đầu kỳ để có lịch sử làm việc, thay vì chỉ đưa một bản cuối lên repo.

Trước mỗi commit, xem lại danh sách tệp được đưa vào. `data/raw/`, `.venv/`, `.env` và mọi tệp chứa khóa API phải nằm trong `.gitignore`. Tệp `.gitignore` chỉ hướng dẫn Git bỏ qua những tệp chưa được theo dõi. Nếu một bí mật đã bị commit, thêm tên vào `.gitignore` không xóa được bí mật khỏi lịch sử.

## 4. Các mốc nộp và cách ghi nhận bản cuối

Đề quy định hạn lúc **23:59 Chủ nhật**, xét theo thời gian commit trên GitHub. Giữ nguyên cách xác định hạn của môn và đối chiếu thông báo chính thức nếu có thay đổi lịch.

| Mốc | Thời điểm được công bố | Nhóm cần hoàn thành |
| --- | --- | --- |
| Mốc 1 | 23:59 Chủ nhật 20/09/2026, tuần 2 | Lập nhóm, tạo repo, nhận thành phố và điền liên kết repo vào bảng tính. Mốc này không cần tag. |
| Mốc 2 | 23:59 Chủ nhật 22/11/2026, tuần 11 | Nộp bản cuối bằng tag `final`. Báo cáo phải ghi mã commit của bản nộp. |
| Mốc 3 | Theo lịch thi của Trường | Vấn đáp khoảng 20 phút cho mỗi nhóm, hỏi riêng từng thành viên. |

Tag là tên gắn với một commit cụ thể để xác định bản bàn giao. Sau khi đã commit và push bản cuối, tại đúng commit muốn nộp, tạo rồi đẩy tag:

```bash
git tag final
git push origin final
```

Tên tag không thay cho việc kiểm tra nội dung bản nộp. Nhóm cần bảo đảm tag chỉ đến đúng commit, các tệp cần bàn giao đã có trên GitHub và mã commit ghi trong PDF trùng với bản đó. Không tự di chuyển một tag đã nộp nếu chưa có hướng dẫn của giảng viên.

## 5. Dữ liệu phải dùng và cách hiểu bốn mốc chụp

### 5.1. Bốn loại tệp

Dữ liệu đến từ [Inside Airbnb](https://insideairbnb.com/get-the-data/), được đề ghi giấy phép CC BY 4.0. Báo cáo cần ghi nguồn và ngày của từng snapshot. Nhóm phải tự khảo sát cấu trúc, kiểu dữ liệu và các điểm bất thường của từng bản chụp, rồi ghi nhận trong QA.

| Tệp trong bộ dữ liệu | Vai trò cần hiểu |
| --- | --- |
| `data/listings.csv.gz` | Thông tin các chỗ ở. Đây là bảng phục vụ nhiều phân tích về giá, loại chỗ ở, host hoặc khu vực, tùy cột thực có trong snapshot. |
| `data/calendar.csv.gz` | Thông tin lịch theo ngày của chỗ ở, phục vụ các phân tích thời gian khi nhóm hiểu đúng cột và phạm vi quan sát. |
| `data/reviews.csv.gz` | Đánh giá văn bản của khách. Đây là đầu vào của phần LLM. |
| `visualisations/neighbourhoods.geojson` | Ranh giới các khu vực, dùng để nối thông tin thống kê với dữ liệu không gian và tạo hình phù hợp. |

Đuôi `.gz` cho biết tệp đã được nén. Nó không làm thay đổi ý nghĩa các cột CSV. GeoJSON là định dạng chứa hình học, chẳng hạn đường bao của một khu vực, cùng thuộc tính của đối tượng địa lý.

CSV là tệp văn bản biểu diễn bảng, thường dùng dấu phẩy để ngăn cột. Trước khi đọc, cần xem hàng tiêu đề và quy tắc của tệp. Không suy ý nghĩa một cột chỉ từ việc chương trình đọc được nó thành số hay chuỗi.

### Trên trang Inside Airbnb có bảy tệp, cần phân biệt thế nào? {#cac-tep-du-lieu}

Tại [Get the Data](https://insideairbnb.com/get-the-data/), mỗi khối thành phố và ngày chụp có các liên kết tải. Bốn loại tệp trong bảng trên là đầu vào được đề nêu. Ngoài chúng, trang còn có ba tệp tổng hợp để hỗ trợ khám phá và trực quan hóa. Không chọn tệp chỉ theo phần tên giống nhau.

| Tên liên kết tải | Vai trò và cách chọn cho bài tập lớn |
| --- | --- |
| `listings.csv.gz` | Bảng listing chi tiết trong thư mục `data/`, dùng khảo sát thông tin chỗ ở và tính chỉ số. |
| `calendar.csv.gz` | Bảng lịch chi tiết trong `data/`, một listing có thể xuất hiện ở nhiều ngày. |
| `reviews.csv.gz` | Bảng review chi tiết trong `data/`, có văn bản bình luận để dùng cho LLM. |
| `listings.csv` | Bảng listing tổng hợp trong `visualisations/`, ít cột hơn bản chi tiết. Không phải chỉ là bản chi tiết đã bỏ nén. |
| `reviews.csv` | Bảng review tổng hợp trong `visualisations/`, phục vụ phân tích thời gian. Bản đã kiểm tra chỉ có mã listing và ngày, không có nội dung bình luận. |
| `neighbourhoods.csv` | Danh sách tên hoặc nhóm khu vực trong `visualisations/`. Có tên khu vực không có nghĩa đã có đường bao để vẽ bản đồ. |
| `neighbourhoods.geojson` | Hình học ranh giới và thuộc tính khu vực trong `visualisations/`, dùng cho bản đồ và liên kết thông tin không gian. |

Các mô tả dưới đây được đối chiếu [Data Dictionary của Inside Airbnb](https://docs.google.com/spreadsheets/d/1iWCNJcSutYqpULSQHlNyGInUvHg2BoUGoNRIGa6Szc4/edit) và đọc thử cấu trúc các tệp Santiago ngày 23/09/2026. Đây là một lần kiểm tra cấu trúc, không thay đổi bốn snapshot bắt buộc của đề. Các cột có thể thay đổi theo phiên bản, nên script phải kiểm tra lại tệp nhóm được giao.

#### `listings.csv.gz`: Thông tin một chỗ ở trong một snapshot

Mỗi hàng mô tả một listing được ghi nhận trong lần thu thập đó. Các nhóm cột có thể gặp gồm:

- Nhận diện và nguồn thu thập: `id`, `listing_url`, `scrape_id`, `last_scraped`.
- Chủ tài khoản: Các cột như `host_id` và thông tin liên quan đến host. Một host có thể có nhiều listing.
- Vị trí: `latitude`, `longitude`, `neighbourhood_cleansed` và cột nhóm khu vực nếu có.
- Đặc điểm: `room_type`, `property_type`, `accommodates`, `bedrooms`, `beds`, `amenities`.
- Giá và điều kiện lưu trú: `price`, `minimum_nights`, `maximum_nights` cùng các trường liên quan tùy phiên bản.
- Thống kê review và lịch: Chẳng hạn `number_of_reviews`, `review_scores_rating`, `availability_365` nếu có trong snapshot.

`number_of_reviews` là một con số tổng hợp, không phải phần bình luận để đưa vào LLM. `amenities` là danh sách tiện nghi, có thể được lưu như văn bản biểu diễn JSON, nên không tách danh sách một cách tùy tiện bằng mọi dấu phẩy.

Một listing là một mục đăng, có thể cho thuê cả chỗ ở hoặc chỉ một phòng. Vì vậy, số listing không tự đồng nghĩa với số căn nhà vật lý riêng biệt. Khi ghi chú nói “1.000 ngôi nhà”, cần xác nhận đơn vị thực sự được yêu cầu là listing hay đối tượng khác.

Từ điển nguồn mô tả giá theo tiền tệ địa phương. Ký hiệu tiền trong chuỗi xuất ra không đủ để kết luận đó là USD. Cần xác nhận loại tiền của thành phố, cách đọc giá và ý nghĩa các trường giá trong đúng snapshot.

#### `calendar.csv.gz`: Một chỗ ở tại một ngày trong lịch

Một hàng thường gắn với cặp `listing_id` và `date`. Tệp Santiago đã kiểm tra có các cột `listing_id`, `date`, `available`, `minimum_nights`, `maximum_nights`. Nó **không có cột `price`**. Vì vậy, không được viết chương trình mặc định mọi bản calendar đều có giá theo ngày chỉ vì ghi chú hoặc một snapshot cũ có nhắc đến.

`date` là ngày trên lịch lưu trú, còn ngày nằm trong URL là ngày snapshot. Inside Airbnb mô tả lịch thu thập cho khoảng một năm phía trước, không phải nhật ký xác nhận mọi giao dịch đã xảy ra trong năm vừa qua. Độ dài và độ đầy đủ thực tế cần được kiểm tra trong từng tệp.

`available` thường biểu diễn trạng thái còn trống bằng `t` hoặc `f`. Theo [mô tả giới hạn dữ liệu của Inside Airbnb](https://insideairbnb.com/data-assumptions/), không còn trống có thể do đã được đặt hoặc do host khóa lịch. Không biến mọi giá trị `f` thành một lượt đặt phòng hoặc doanh thu đã thu được.

Calendar có thể lớn vì lặp lại nhiều ngày cho nhiều listing. Hãy đọc thử một phần, chỉ chọn cột cần dùng hoặc xử lý theo khối nếu bộ nhớ không đủ. Tệp nén nhỏ trên đĩa không chứng minh DataFrame sau đọc sẽ nhỏ. Không cần nạp cả bốn snapshot vào RAM cùng lúc mới có thể phân tích.

#### `reviews.csv.gz`: Một đánh giá văn bản của khách

Các cột đã kiểm tra là `listing_id`, `id`, `date`, `reviewer_id`, `reviewer_name`, `comments`. Trong bảng này, `id` là mã review, không phải mã listing. `listing_id` mới là trường dùng để nối sang `listings.id`.

`comments` chứa nội dung để trích xuất cảm xúc, khía cạnh và ngôn ngữ. `date` là ngày của review. Một listing có nhiều review và cùng một review có thể xuất hiện lại trong snapshot khác. Nếu muốn đếm review duy nhất qua nhiều snapshot, cần xác định khóa và phạm vi trước khi tổng hợp.

Không dùng `reviewer_name` để đoán cảm xúc hoặc ngôn ngữ. Khi tạo mẫu cho LLM và gán nhãn tay, giữ mã review cùng nội dung cần phân tích. Các trường nhận diện cá nhân không phục vụ nhiệm vụ cần được xem xét theo chính sách dữ liệu trước khi gửi ra dịch vụ ngoài.

#### `listings.csv`, `reviews.csv` và `neighbourhoods.csv`: Các bảng tổng hợp

`listings.csv` đã kiểm tra có những cột thuận tiện cho biểu đồ như mã listing, vị trí, loại phòng, giá và một số thống kê review/lịch. Nó không có đầy đủ các trường của `listings.csv.gz`. Cần quay về bản chi tiết khi thiết kế QA hoặc KPI đòi những cột chưa có trong bản tổng hợp.

`reviews.csv` đã kiểm tra chỉ có `listing_id` và `date`. Nó giúp đếm review theo thời gian, nhưng không có `comments` để phân tích văn bản và không có `id` review để dùng thay trực tiếp tập review chi tiết. Hai hàng cùng listing và cùng ngày chưa chắc là một review trùng nhau.

`neighbourhoods.csv` đã kiểm tra có `neighbourhood_group` và `neighbourhood`. Bảng này giúp xem các tên khu vực, nhưng không chứa các chuỗi tọa độ tạo nên đường biên. Muốn vẽ hình khu vực phải đọc tệp GeoJSON.

#### `neighbourhoods.geojson`: Đường bao để vẽ khu vực trên bản đồ

GeoJSON là JSON có cấu trúc mô tả đối tượng địa lý. Tệp được kiểm tra có kiểu ngoài cùng là `FeatureCollection`, nghĩa là một tập các đối tượng. Danh sách `features` chứa các `Feature`. Mỗi Feature có hai phần cần phân biệt:

- `properties` chứa thuộc tính, chẳng hạn `neighbourhood` và `neighbourhood_group`, để nhận diện khu vực.
- `geometry` chứa loại hình và tọa độ đường bao. `Polygon` biểu diễn một vùng đa giác, còn `MultiPolygon` cho phép một khu vực gồm nhiều phần đa giác tách rời. Đa giác cũng có thể có các vòng bên trong biểu diễn phần rỗng.

Trong GeoJSON theo [RFC 7946](https://datatracker.ietf.org/doc/html/rfc7946), cặp tọa độ được viết theo thứ tự kinh độ trước, vĩ độ sau. Khi dùng dữ liệu listing để tạo điểm, cũng phải giữ đúng `longitude` rồi `latitude`. Đảo thứ tự có thể đặt điểm sai vị trí hoặc làm thao tác không gian sai.

Để vẽ bản đồ KPI, trước hết tính một bảng có một hàng cho mỗi khu vực. Sau đó ghép tên hoặc mã khu vực của bảng KPI với trường tương ứng trong `properties`, rồi tô màu các hình theo chỉ số. Phải kiểm tra tên không khớp, giá trị thiếu và quan hệ nối, vì ghép theo thứ tự dòng không bảo đảm đúng khu vực.

Điểm tọa độ của một listing khác với đường bao khu vực. Nếu muốn tự xác định listing nằm trong vùng nào, cần thao tác xét điểm thuộc đa giác và quy tắc cho điểm nằm ở biên. Không tự coi một hàng GeoJSON là một listing hoặc coi `analysis_area` là mã có sẵn trong GeoJSON.

Inside Airbnb cũng nêu rằng vị trí listing được làm mờ để bảo vệ địa chỉ thật. Vì vậy, không diễn giải các điểm đó như tọa độ cửa nhà chính xác, đặc biệt khi kết luận về listing ở sát ranh giới một khu vực.

#### Nối các tệp theo đối tượng, không theo vị trí hàng

| Mục đích | Khóa và phạm vi cần kiểm tra |
| --- | --- |
| Bổ sung thông tin listing cho review | `reviews.listing_id` nối với `listings.id` trong snapshot tương ứng. |
| Bổ sung thông tin listing cho lịch | `calendar.listing_id` nối với `listings.id`. Lịch vẫn có nhiều hàng ngày cho một listing. |
| Theo dõi listing qua snapshot | Giữ `id` cùng ngày snapshot, không xóa mọi lần xuất hiện lặp của `id`. |
| Tính KPI khu vực rồi vẽ bản đồ | Khóa nhóm trong bảng KPI phải khớp trường khu vực đã kiểm tra trong `properties` của GeoJSON. |

Không nối đồng thời toàn bộ lịch ngày với toàn bộ review chỉ bằng `listing_id` rồi đếm hàng kết quả. Mỗi ngày có thể bị lặp với mỗi review của cùng listing. Hãy tổng hợp từng bảng về đúng đơn vị cần phân tích trước khi ghép kết quả.

#### Đọc tệp nén và lưu từng snapshot

Có thể đọc trực tiếp `.csv.gz` bằng `gzip` của Python hoặc `read_csv` có xử lý nén. Không cần giải nén ra một tệp CSV trung gian chỉ để đọc. Khi dùng Python chuẩn, mở nội dung giải nén ở chế độ văn bản và đưa vào `csv.reader` hoặc `csv.DictReader` để xử lý đúng dấu phẩy và dấu ngoặc kép trong văn bản.

Có thể tra cú pháp đọc nén trong [Python gzip](https://docs.python.org/3/library/gzip.html) hoặc [pandas.read_csv](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html). Biết định dạng tệp giúp chọn đúng cách đọc, không buộc nhóm phải dùng một trong hai thư viện này làm công cụ xử lý chính.

Một cách lưu dễ đối chiếu là tạo thư mục riêng theo thành phố và snapshot trong `data/raw/`, rồi giữ phần `data/` và `visualisations/` như trên máy chủ. Chẳng hạn, bên trong thư mục của một snapshot có `data/listings.csv.gz` và `visualisations/listings.csv`. Nhờ vậy, hai loại tệp không bị nhầm tên hoặc ghi đè.

GeoJSON cũng có URL theo snapshot. Không giả định ranh giới giữa các mốc giống hệt nhau chỉ vì chúng cùng tên. Cách đơn giản để giữ dấu vết là lưu hoặc ghi nhận tệp GeoJSON gắn với từng mốc được dùng. Nếu tái sử dụng một bản, cần xác minh sự tương thích và ghi rõ lựa chọn đó.

Khi chọn dữ liệu trên web, kiểm tra đủ ba phần: Thành phố, ngày chụp và thư mục `data/` hay `visualisations/`. Nếu ngày bắt buộc không còn hiện ở phần tải mới nhất, xem mục dữ liệu lưu trữ hoặc xác nhận lại nguồn với giảng viên, không âm thầm dùng ngày mới thay thế.

Trước khi nối hoặc tổng hợp, cần xác định một hàng của từng bảng đại diện cho điều gì. Listing, listing tại một ngày lịch và một review là những đơn vị khác nhau. Nếu ghép một listing với nhiều review rồi tính trung bình giá trên bảng sau ghép, các listing có nhiều review có thể được tính lặp nhiều lần.

Trạng thái không còn trống trong lịch không tự chứng minh một giao dịch đặt phòng đã xảy ra. Chủ nhà cũng có thể khóa lịch vì lý do khác. Nhóm cần đọc mô tả dữ liệu trước khi gọi một tỷ lệ từ lịch là tỷ lệ đặt phòng thực tế.

### 5.2. Dùng đúng thành phố và đủ bốn mốc

Mỗi thành phố có bốn ngày chụp bắt buộc bên dưới, cách nhau khoảng một quý. Nhóm không tự thay bằng bốn ngày khác cho tiện tải. Với thành phố được đánh dấu có dữ liệu hằng tháng, có thể bổ sung các snapshot khác, nhưng vẫn phải có đủ bốn mốc bắt buộc.

<ProjectCities />

Một mã listing xuất hiện ở nhiều snapshot không mặc nhiên là dòng thừa. Đó có thể là cùng một chỗ ở được quan sát tại nhiều thời điểm. Tương tự, một review có thể được lặp lại trong nhiều tệp snapshot vì các tệp chứa lịch sử đánh giá. Cần phân biệt quan sát lặp hợp lệ với việc đếm lại cùng một sự kiện.

`neighbourhood_cleansed` thường dùng để phân biệt khu vực bên trong thành phố, không phải cột tên thành phố. Ý nghĩa chính xác và mức độ đầy đủ vẫn phải khảo sát trên dữ liệu được giao. Nếu có thêm cột `analysis_area`, cần giữ rõ đó là vùng phân tích được tạo ra theo quy tắc riêng, chưa chắc trùng khu vực có sẵn trong dữ liệu.

Mã định danh cũng khác với chỉ số hàng. `id` hoặc `listing_id` dùng để nhận diện chỗ ở theo quy ước của bảng, còn index của DataFrame có thể chỉ là vị trí hàng hiện tại. Đặt lại index không sửa được một phép nối dùng sai khóa và không tạo ra danh tính mới cho chỗ ở.

Không coi ngày chụp là ngày phát sinh mọi review hoặc mọi dòng lịch bên trong tệp. Cũng không nối bốn snapshot rồi tuyên bố đã quan sát đầy đủ mọi ngày giữa các mốc. Phạm vi thời gian phải được xác định từ ý nghĩa của các cột và việc thu thập thực tế.

### 5.3. Dựng địa chỉ tải bằng cấu hình

Địa chỉ có phần chung là máy chủ `https://data.insideairbnb.com`. Phần còn lại gồm quốc gia, vùng, thành phố, ngày snapshot và tên tệp. Hai dạng đường dẫn là:

```text
<country>/<region>/<city>/<YYYY-MM-DD>/data/<bảng>.csv.gz
<country>/<region>/<city>/<YYYY-MM-DD>/visualisations/neighbourhoods.geojson
```

Ở đây, `<bảng>` lần lượt là `listings`, `calendar` hoặc `reviews`. Thêm dấu `/` giữa địa chỉ máy chủ và đường dẫn tương ứng để có URL đầy đủ. Giá trị `data_root` trong cấu hình chính là phần `<country>/<region>/<city>`, cần giữ đúng như danh sách thành phố, kể cả ký tự có dấu nếu có.

Script tải phải tải đủ dữ liệu cho bốn mốc và kiểm tra tệp có tồn tại, đọc được, có các cột khóa cần dùng. Chỉ thấy mã HTTP thành công hoặc một tệp trên ổ đĩa chưa đủ để xác nhận đó là đúng bảng và đúng snapshot.

Giữ dữ liệu tải nguyên trạng trong `data/raw/` để còn đối chiếu khi sửa quy tắc. Không commit thư mục này. Dữ liệu đã xử lý nằm ở `data/processed/` và chỉ commit khi đáp ứng giới hạn dưới 50 MB được đề nêu. Nếu dữ liệu xử lý lớn, chương trình và hướng dẫn phải cho phép tạo lại.

## 6. “Chạy bằng một lệnh” nghĩa là gì?

Sau khi cài môi trường theo `README.md`, người sử dụng chạy một lệnh để chương trình thực hiện các bước và ghi kết quả. Đề minh họa cách gọi sau:

```bash
python run_pipeline.py --config configs/lisbon.yaml
```

`run_pipeline.py` là chương trình điều phối. `--config` cho biết sẽ đọc lựa chọn từ tệp nào. `configs/lisbon.yaml` là một tệp cấu hình ví dụ, không có nghĩa mọi nhóm phải làm Lisbon hoặc phải dùng đúng tên chương trình đó. Có thể tổ chức bằng Makefile hoặc cách tương đương, miễn đáp ứng việc chạy toàn quy trình bằng một lệnh đã ghi rõ.

Ví dụ dùng YAML để lưu cấu hình, nhưng đề không quy định chỉ được dùng định dạng này. Dù chọn cách lưu nào, nhóm vẫn cần tài liệu hướng dẫn rõ để người chấm thay tham số và chạy chương trình.

Một cách đọc luồng công việc là:

```text
Đọc cấu hình
→ Tải và xác minh đầu vào
→ Khảo sát, áp dụng QA và ghi tác động
→ Chuẩn bị mẫu review, phân tích và đánh giá LLM
→ Tính KPI, gồm KPI dùng kết quả LLM
→ Sinh hình và xuất các tệp kết quả
```

Thứ tự chi tiết có thể khác theo thiết kế của nhóm. Điều cần giữ là bước nào cần đầu vào nào, kết quả được lưu ở đâu và một lệnh có thể điều phối đầy đủ những phần bắt buộc. Không yêu cầu người chấm phải tự mở notebook rồi đoán nên chạy các ô theo thứ tự nào.

Thành phố, snapshot và các tham số phải đọc từ cấu hình, không được ghi cố định trong nhiều chỗ của mã. Khi người chấm đổi một snapshot trong cấu hình, chương trình phải dùng giá trị mới thay vì tiếp tục đọc tệp hoặc nhãn ngày cũ.

### Việc người chấm sẽ thực hiện

Giảng viên dùng một bộ test chung cho mọi nhóm. Họ dựng môi trường theo README, chạy một lệnh với snapshot do họ chọn rồi kiểm tra các tệp đầu ra. Snapshot đó có thể là một mốc nhóm chưa xử lý trước, chỉ thay trong cấu hình.

Phần LLM sẽ được gọi lại thật lúc test bằng khóa API do giảng viên đặt trong biến môi trường. Vì vậy, chương trình phải đọc đúng tên biến đã hướng dẫn và làm việc với khóa được cung cấp hợp lệ cho dịch vụ, không phụ thuộc khóa riêng của thành viên nhóm.

Trang đề chưa ấn định một tên biến khóa chung cho mọi cách cài đặt. Nhóm cần chọn tên phù hợp với thư viện gọi dịch vụ, dùng nhất quán trong mã và `.env.example`, rồi ghi đúng tên ấy trong README. Nếu sau đó bộ test chung quy định tên khác, cập nhật cách nhận khóa theo hướng dẫn chấm. Không tự coi một tên biến ví dụ là quy định mới của môn.

Kết quả lưu lại và tùy chọn `--skip-llm` có thể giúp phát triển hoặc chạy lại một số bước. Chúng không thay thế khả năng thực thi phần LLM thật khi người chấm yêu cầu. Chương trình cũng phải cho biết lần chạy nào dùng cache và lần nào gọi dịch vụ.

Chọn dùng cache mặc định hay chỉ dùng khi có tùy chọn là quyết định thiết kế cần ghi trong README. `--skip-llm` nghĩa là không thực hiện bước gọi LLM trong lần chạy đó, không tự tạo ra kết quả mới. Nếu các bước sau cần kết quả chưa có trong cache, phải báo rõ điều còn thiếu thay vì âm thầm xuất chỉ số giả hoặc coi tập kết quả rỗng là đã phân tích xong.

## 7. QA: Phải phát hiện và xử lý vấn đề dữ liệu ra sao?

QA không chỉ là gọi `dropna()` rồi lưu một bảng mới. Nhóm tự đề xuất các quy tắc phù hợp với dữ liệu và mục tiêu phân tích. Mỗi quy tắc phải có tên, điều kiện phát hiện, lý do và hành động xử lý. Đề ưu tiên gắn cờ để giữ lại dấu vết trước khi quyết định sửa hoặc loại bỏ.

### 7.1. Những dạng vấn đề tối thiểu cần xét

- Giá trị thiếu: Phân biệt thiếu dữ liệu với số 0 có ý nghĩa. Nêu cột nào thiếu, thiếu bao nhiêu và việc thiếu ảnh hưởng chỉ số nào.
- Ngoại lai: Một giá trị rất lớn hoặc rất nhỏ cần được xem xét theo đơn vị và ngữ cảnh. Ngoại lai không tự động là lỗi phải xóa.
- Trùng lặp trong một snapshot: Xác định khóa và đơn vị quan sát trước khi quyết định hai hàng có thực sự trùng hay không.
- Trùng giữa các snapshot: Nhận diện cùng một thực thể hoặc cùng một sự kiện xuất hiện nhiều lần, tránh xóa nhầm lịch sử hoặc đếm lặp review.
- Sai kiểu: Ví dụ giá được lưu dưới dạng văn bản. Cần ghi quy tắc chuyển đổi và nhận diện những chuỗi không đọc được, thay vì âm thầm biến mọi lỗi thành 0.
- Danh mục không thống nhất: Cùng một loại chỗ ở hoặc khu vực có thể khác cách viết. Cần đối chiếu và ghi quy tắc chuẩn hóa, không tự gộp hai nhãn chỉ vì trông gần giống nhau.

Khi nói một cột đã “sạch”, nhóm cần chỉ ra điều kiện đã kiểm tra. Một chương trình chạy không báo lỗi vẫn có thể dùng sai đơn vị tiền tệ, nối sai khóa hoặc lấy sai mẫu số.

### 7.2. Viết một quy tắc để người khác hiểu được

Với mỗi quy tắc, giải thích đủ bốn ý:

1. Tên quy tắc gọi đúng vấn đề cần phát hiện.
2. Điều kiện có thể áp dụng bằng chương trình lên cột hoặc hàng xác định.
3. Lý do cho biết vì sao trường hợp đó cần xem xét trong bài toán này.
4. Hành động mô tả việc gắn cờ, chuẩn hóa, giữ lại, điền thiếu hoặc loại hàng và điều kiện thực hiện.

Nếu đề xuất ngưỡng giá, nhóm phải nêu tiền tệ và cơ sở chọn ngưỡng. Không lấy một con số ở cấu hình minh họa làm chuẩn chung cho mọi thành phố. Nếu loại một nhóm hàng, cần giải thích những hàng đó sẽ không còn tham gia chỉ số nào.

### 7.3. Ghi tác động vào báo cáo QA

Tệp bắt buộc là `reports/qa_report.csv`. Tệp này phải ghi tác động của QA, gồm số dòng và KPI trước, sau xử lý. Để đọc được các con số, nên kèm tên quy tắc, snapshot, đối tượng bị tác động và mô tả hành động.

Các cột bổ sung đó là gợi ý tổ chức, không phải một schema CSV đã được giảng viên ấn định. Kết quả cần trả lời được các câu hỏi cụ thể: Quy tắc nào tác động bao nhiêu hàng, vì sao áp dụng và chỉ số đã thay đổi thế nào?

Việc QA đứng trước bước tính KPI không tạo ra vòng lặp bắt buộc trong chương trình. Có thể giữ dữ liệu hoặc thông tin cần thiết trước và sau xử lý, ghi số dòng khi áp dụng quy tắc, rồi hoàn thiện các cột so sánh KPI sau khi tính được chúng. `qa_report.csv` là tệp báo cáo cần có ở đầu ra, không có nghĩa hàm trong `qa.py` phải điền xong mọi chỉ số ngay lập tức.

Khi so sánh một KPI, dùng cùng định nghĩa, đơn vị và phạm vi trên hai trạng thái dữ liệu. Với KPI cần kết quả LLM, chỉ hoàn thiện so sánh sau khi có các đầu vào liên quan. Nêu rõ phần nào của chênh lệch đến từ QA và phần nào đến từ việc đổi mẫu hoặc cách trích xuất, không gộp chúng thành một tác động duy nhất.

Nếu một KPI chưa xác định được trên dữ liệu trước xử lý, ghi tình trạng đó cùng lý do. Không tự điền 0 hoặc bỏ yêu cầu báo cáo tác động lên KPI. Đề chưa quy định một mẫu chi tiết cho mọi chỉ số trước, sau, nên nhóm cần chọn cách thể hiện có thể giải thích và đối chiếu khi hướng dẫn chấm được công bố.

Giữ mối liên hệ giữa dữ liệu thô, cờ QA và dữ liệu dùng tính KPI để có thể giải thích một giá trị trong báo cáo bắt nguồn từ đâu. Nếu các quy tắc chồng lấn, cần nói rõ số hàng theo từng quy tắc không nhất thiết cộng lại thành tổng số hàng bị loại.

## 8. KPI: Chọn và tính 5–8 chỉ số có ý nghĩa

Nhóm phải có 5–8 KPI gắn với bên sử dụng báo cáo. Đề không cho một danh sách chỉ số cố định để sao chép. Mỗi chỉ số phải ghi tên, mục tiêu, công thức, đơn vị và được tính sau QA. Với giá hoặc đại lượng tiền tệ, phải ghi rõ loại tiền.

Trước khi viết công thức, xác định chỉ số nói về đối tượng nào. Trung bình trên listing, trên host, trên review và trên ngày có thể cho kết quả khác nhau. Một chỉ số có mẫu số chưa được giải thích sẽ khó diễn giải, dù phép tính không lỗi.

### Các góc độ bắt buộc phải có

- Theo khu vực: Có KPI phân tích theo `neighbourhood_cleansed`. Khi gắn với GeoJSON, cần kiểm tra các mã hoặc tên khu vực có khớp giữa hai phía hay không.
- Theo thời gian: Có KPI phản ánh sự thay đổi hoặc khác biệt theo thời gian. Phải phân biệt so sánh các snapshot với phân tích lịch sử sự kiện bên trong một snapshot.
- Dùng kết quả LLM: Có ít nhất một KPI được tính từ kết quả trích xuất review bằng LLM.

Các góc độ có thể cùng xuất hiện trong một chỉ số, nhưng bản thiết kế phải cho thấy chúng đã được bao quát. Đề không bắt nhóm thêm một lượng chỉ số cố định ngoài khoảng 5–8 chỉ để mỗi góc độ nằm ở một bảng riêng.

Tệp KPI được xuất ở `data/processed/kpi_*.csv`. Dấu `*` chỉ phần tên thay đổi theo nhóm chỉ số hoặc phạm vi kết quả. Cần để người đọc xác định được snapshot, khu vực, chỉ số và đơn vị từ tệp hoặc từ điển dữ liệu đi kèm.

Nếu dùng tỷ lệ, ghi rõ tử số và mẫu số. Nếu chỉ phân tích một mẫu review, không tự gọi tỷ lệ trong mẫu là tỷ lệ đã đo trên toàn bộ khách hoặc toàn bộ thành phố. Khi các mốc có phạm vi thu thập khác nhau, cần giải thích khả năng so sánh trước khi kết luận tăng hay giảm.

## 9. Phần LLM bắt buộc: Đọc review và tự đo chất lượng

### 9.1. LLM cần trả về thông tin gì?

LLM nhận một mẫu review và chuyển nội dung văn bản thành thông tin có cấu trúc. Với mỗi đánh giá được xử lý, cần trích xuất:

- Cảm xúc theo ba nhãn `positive`, `mixed`, `negative`, tương ứng tích cực, có cả ý tích cực và tiêu cực, hoặc tiêu cực.
- Các khía cạnh được khen hoặc chê, chẳng hạn nội dung liên quan vị trí, sạch sẽ hay tiếng ồn, tùy hệ nhãn nhóm thiết kế.
- Ngôn ngữ của đánh giá.

“Có cấu trúc” nghĩa là kết quả có các trường nhất quán để chương trình đọc và tổng hợp, không chỉ là một đoạn nhận xét tự do. Nhóm cần giữ mã review hoặc cách liên kết rõ ràng với văn bản đầu vào để kiểm tra lại từng kết quả.

Đề không bắt buộc mọi nhóm dùng cùng một schema JSON. Tuy nhiên, nhóm phải giải thích các trường, giá trị hợp lệ và cách xử lý phản hồi thiếu trường, sai kiểu hoặc không đúng nhãn. Không coi một phản hồi đọc được bằng JSON là bằng chứng nội dung của nó đúng.

JSON là cách biểu diễn dữ liệu bằng các trường tên và giá trị, có thể chứa danh sách hoặc các đối tượng lồng nhau. Schema là quy tắc mô tả những trường cần có và kiểu giá trị được chấp nhận. Nhờ quy tắc này, chương trình biết phải đọc và kiểm tra kết quả LLM thế nào.

### 9.2. Dùng dịch vụ nào và chọn mẫu ra sao?

Công cụ được hướng dẫn là Gemini API gói miễn phí. Có thể dùng nhà cung cấp khác nếu nhóm tự chịu chi phí và ghi rõ trong `AI_USAGE.md`. Gói miễn phí vẫn có điều kiện và hạn mức, nên cần xem tài liệu dịch vụ tại thời điểm thực hiện.

Cỡ mẫu và cách chọn mẫu do nhóm quyết định rồi giải thích. Đề không bắt xử lý tất cả review bằng LLM và không ấn định mẫu phải có 3.000 phần tử. Con số 3.000 chỉ xuất hiện trong cấu hình minh họa.

Khi chọn mẫu, cần nói nhóm chọn từ snapshot nào, lọc trùng ra sao và các review đó đại diện cho phạm vi nào. Nếu chỉ lấy review mới nhất hoặc review của một khu vực, cần nêu giới hạn đó trước khi diễn giải KPI.

### 9.3. Tạo ít nhất 100 nhãn tay

Nhóm phải chuẩn bị **ít nhất 100 đánh giá được gán nhãn tay**. Tệp nhãn tham chiếu nằm trong `data/samples/`, giữ được mã review và nhãn để đối chiếu với dự đoán.

Trước khi gán, nên viết hướng dẫn ngắn để các thành viên hiểu thống nhất một nhãn được dùng khi nào. Khi một review vừa khen phòng sạch vừa phàn nàn tiếng ồn, cần có quy tắc quyết định nhãn cảm xúc và cách ghi nhận các khía cạnh. Đây là công việc thiết kế cách đánh giá, không thể thay bằng việc chép nhãn do chính LLM tạo ra.

Đề không ấn định số người gán nhãn hay một thuật toán lấy mẫu bắt buộc. Có thể đọc chéo một phần nhãn để phát hiện cách hiểu khác nhau. Nếu dùng một phần dữ liệu để sửa prompt hoặc điều chỉnh phương pháp, nên tách phần đó khỏi phần đánh giá cuối và ghi cách chia để tránh báo cáo chất lượng quá lạc quan.

Để bắt đầu gán nhãn, xuất một bảng giữ mã review, văn bản và các cột nhãn còn trống, rồi đọc từng review để điền theo hướng dẫn đã thống nhất. Sau khi hoàn thành, kiểm tra mã trùng, ô nhãn thiếu và các nhãn ngoài danh sách đã chọn. Tệp này là dữ liệu tham chiếu, khác tệp dự đoán do LLM sinh ra.

Nếu không hiểu ngôn ngữ của review, không đoán nhãn hoặc lấy chính câu trả lời LLM đang chấm làm nhãn chuẩn. Có thể trao đổi cách gán với người hiểu ngôn ngữ đó, hoặc lựa chọn phạm vi mẫu mà nhóm có thể đọc và giải thích. Nếu có tập review được giao cố định, cần xác nhận cách xử lý trường hợp ngoại ngữ với giảng viên trước khi đổi tập. Dùng công cụ dịch để hỗ trợ cũng phải khai báo và kiểm tra lại ý nghĩa.

### 9.4. Có một phương pháp đối chứng không dùng LLM

Phương pháp đối chứng thực hiện cùng nhiệm vụ trên dữ liệu cần so sánh. Chẳng hạn, nhóm có thể xây quy tắc từ khóa nếu phù hợp, nhưng đề không bắt buộc baseline phải là từ khóa. Điều bắt buộc là có một cách không dùng LLM và đo chất lượng của nó.

Hai phương pháp cần được đối chiếu với nhãn tay theo cùng cách đánh giá để con số có ý nghĩa. Nếu mỗi phương pháp được chấm trên một tập review khác nhau hoặc một bộ nhãn khác nhau, khó xác định chênh lệch đến từ phương pháp hay dữ liệu.

Cần ghi rõ đầu ra nào được đem so sánh. Nếu đang so cảm xúc, cả baseline và LLM phải được chấm bằng cùng bộ nhãn cảm xúc. Không so accuracy cảm xúc của baseline với F1 khía cạnh của LLM rồi kết luận một phương pháp tốt hơn.

LLM vẫn phải trích xuất đủ cảm xúc, khía cạnh khen/chê và ngôn ngữ như đề nêu. Đề công khai chưa mô tả hết cách chấm đối chứng cho từng trường, nên không tự kết luận baseline chỉ cần cảm xúc, hoặc mọi trường đều có một cách tính điểm giống nhau. Nhóm cần mô tả rõ phạm vi đánh giá và đối chiếu hướng dẫn chấm bổ sung khi có.

### 9.5. Báo cáo accuracy và F1 cho cả hai phương pháp

Accuracy là tỷ lệ dự đoán đúng trên số trường hợp đã chấm. Ví dụ dùng để diễn giải một phép đo phải nêu rõ đang đo nhãn cảm xúc, ngôn ngữ hay một đầu ra khác. Không gọi một tỷ lệ chung là chất lượng của mọi phần trích xuất nếu chỉ chấm một trường.

Để tính accuracy, đếm số dự đoán trùng nhãn tham chiếu rồi chia cho số review được chấm. Khi trình bày dạng phần trăm, nhân tỷ lệ đó với 100. Bảng kết quả cần cho thấy riêng LLM và baseline, tập review đã dùng và đầu ra đang được đánh giá.

F1 kết hợp precision và recall. Khi xét một nhãn cụ thể, precision trả lời trong các trường hợp được dự đoán có nhãn ấy thì bao nhiêu là đúng. Recall trả lời trong các trường hợp thực sự mang nhãn ấy thì mô hình tìm được bao nhiêu. F1 cao đòi hỏi cả hai khía cạnh tương đối tốt.

Đề yêu cầu báo cáo accuracy/F1 của cả LLM và phương pháp đối chứng, kèm phân tích lỗi. Với nhiều nhãn, phải ghi cách tính F1, chẳng hạn trung bình đều theo lớp hoặc cách khác mà nhóm lựa chọn. Không tự đổi yêu cầu này thành việc chỉ công bố một con số accuracy.

Phân tích lỗi cần trở lại review cụ thể: Phương pháp dự đoán gì, nhãn tham chiếu là gì và sự khác nhau có thể đến từ đâu? Nếu hướng dẫn gán nhãn còn mơ hồ, cần thừa nhận giới hạn đó thay vì quy mọi sai lệch cho mô hình.

Ngôn ngữ, cảm xúc và các khía cạnh khen/chê có cấu trúc nhãn khác nhau. Nếu đo cả ba, cần giải thích cách xác định đúng, sai cho từng đầu ra. Đề chưa quy định một cách tính F1 duy nhất cho mọi phần, nên nhóm phải ghi lựa chọn của mình thay vì để người đọc tự đoán.

Với danh sách khía cạnh, một review có thể mang nhiều nhãn. Có hai câu hỏi đo khác nhau. Một cách xét dự đoán có khớp nguyên cả danh sách nhãn hay không. Cách khác đếm nhãn đúng, nhãn dự đoán thừa và nhãn bị bỏ sót. Không gọi hai cách đó là cùng một phép đo.

Ví dụ nhỏ chỉ để hiểu cách chấm: Nhãn tay của một review là “sạch sẽ” và “vị trí”, còn mô hình dự đoán “sạch sẽ” và “tiếng ồn”. Mô hình có một nhãn đúng, một nhãn thừa và bỏ sót một nhãn. Khi chỉ chấm tập nhỏ này theo từng nhãn được dự đoán, precision và recall đều bằng một nửa, F1 bằng 0,5. Nếu yêu cầu khớp cả danh sách, trường hợp này bị tính sai hoàn toàn.

Trên nhiều review, cách tính micro cộng các lần đúng, thừa và bỏ sót trước khi tính điểm. Cách tính macro tính điểm cho từng nhãn rồi lấy trung bình đều. Nhóm không bắt buộc chọn cùng một cách trong mọi tình huống, nhưng phải ghi cách đã dùng, xử lý nhãn không xuất hiện ra sao và áp dụng nhất quán cho cả hai phương pháp. Có thể đối chiếu cách tính với [tài liệu F1](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html) và [accuracy](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html).

### 9.6. Chi phí, cache và đưa kết quả vào phân tích

Nhóm phải ước tính chi phí nếu xử lý hết review của thành phố. Cần dựa trên số review, lượng đầu vào/đầu ra dự kiến, cách gọi và mức giá của dịch vụ đang dùng. Phải ghi các giả thiết của ước tính. Yêu cầu ước tính không đồng nghĩa với yêu cầu thực sự gọi API cho toàn bộ thành phố.

Đây là dự toán cần trình bày trong báo cáo. Có thể dùng thông tin về số token đầu vào và đầu ra của mẫu đã xử lý để giải thích cơ sở tính chi phí, đồng thời ghi ngày tra bảng giá. Token là đơn vị mô hình dùng để đếm lượng văn bản, không nhất thiết tương ứng với một từ. Nhà cung cấp có thể áp dụng mức giá khác nhau cho token gửi vào và token được tạo ra.

Lưu kết quả LLM có thể giảm thời gian và số lần gọi khi phát triển. Để tránh dùng lại nhầm, nên nhận diện cache theo review, nội dung đầu vào, mô hình và phiên bản prompt hoặc cấu hình liên quan. Khi đổi cách trích xuất, kết quả cũ có thể không còn phù hợp.

Phải có **ít nhất một KPI và một hình sử dụng kết quả LLM**. Chỉ chạy LLM rồi để tệp kết quả nằm riêng chưa đáp ứng yêu cầu tích hợp. Hình và chỉ số phải góp phần trả lời mục tiêu phân tích đã chọn, đồng thời nêu rõ chúng dựa trên mẫu và chất lượng đã đo.

## 10. Hình và báo cáo kỹ thuật cần thể hiện điều gì?

### 10.1. Sinh hình bằng chương trình

Trực quan hóa phải bao quát không gian, thời gian và kết quả LLM. Nhóm tự chọn loại hình phù hợp với câu hỏi. Có thể dùng bản đồ khi cần thể hiện vị trí, nhưng lựa chọn biểu đồ phải xuất phát từ điều cần so sánh và dữ liệu thực có.

Hình được chương trình xuất vào `figures/`. Chạy lại quy trình phải tạo lại được hình với dữ liệu và cấu hình đã chỉ định. Chú thích cần cho biết chỉ số, đơn vị, phạm vi thời gian và nhóm đối tượng để người đọc hiểu con số đang nói về điều gì.

Đề không ấn định một số hình cố định ngoài yêu cầu có ít nhất một hình từ LLM. Nhóm cần đủ hình để phục vụ các góc độ bắt buộc và báo cáo, tránh hiểu một số lượng tự đề xuất là mức tối thiểu của giảng viên.

### 10.2. Báo cáo PDF tối đa 10 trang

Báo cáo kỹ thuật là PDF đặt trong `reports/`, chẳng hạn `reports/report.pdf`, tối đa 10 trang. Định dạng chi tiết sẽ được công bố sau. Không tự đặt thêm font, cỡ chữ, mẫu bìa hoặc cách tính phụ lục rồi gọi đó là quy định đã có của môn.

Một bố cục có thể dùng để chuẩn bị bản nháp gồm mục tiêu và người sử dụng, dữ liệu, QA, KPI, phần LLM và đánh giá, các kết quả chính, giới hạn và kết luận. Đây là gợi ý tổ chức nội dung, cần điều chỉnh khi format chính thức được công bố.

Báo cáo cần giúp người đọc nối được kết luận với con số, con số với tệp đầu ra và tệp với cách tính. Ghi rõ nguồn dữ liệu, ngày snapshot, tiền tệ, lựa chọn xử lý và mã commit bản nộp. Tránh biến báo cáo thành danh sách ảnh mà người đọc phải tự đoán ý nghĩa.

## 11. Các tệp phải bàn giao và cách tổ chức repo

### 11.1. Môi trường có thể dựng lại

Đề yêu cầu Python 3, nhưng cho phép tự chọn thư viện. Không bắt buộc dùng pandas. Chọn công cụ nào cũng phải hiểu cách hoạt động, giải thích được và kiểm chứng kết quả.

- `.python-version` chứa một dòng ghi phiên bản Python đã chạy thử, theo dạng `3.x.y`.
- `requirements.txt` ghim các phiên bản gói bằng `==`, đủ để chạy toàn quy trình. Có thể dùng lockfile tương đương.
- `README.md` ghi cách cài môi trường, lệnh chạy, tên biến môi trường chứa khóa API và các tệp đầu ra để đối chiếu.
- `.env.example` chỉ ghi tên biến hoặc giá trị mẫu không phải bí mật. Khóa thật đặt trong biến môi trường hoặc công cụ quản lý bí mật thích hợp, không commit.

Tệp `.python-version` chỉ ghi nhận phiên bản, không tự cài hoặc thay Python. Tương tự, một danh sách thư viện thiếu gói cần thiết sẽ không đủ để người chấm dựng lại môi trường, dù máy người viết đã có sẵn gói đó.

Ghim phiên bản nghĩa là chỉ rõ phiên bản sẽ cài, thay vì luôn lấy bản mới nhất. Lockfile là tệp do công cụ quản lý môi trường tạo để ghi lại bộ phiên bản đã chọn, thường gồm cả các gói phụ thuộc. Nhóm chỉ cần chọn một cách quản lý đáp ứng yêu cầu và hướng dẫn cách sử dụng trong README.

### 11.2. Cây thư mục và vai trò của từng phần

```text
.
├── configs/
│   └── <city>.yaml
├── data/
│   ├── raw/
│   ├── processed/
│   └── samples/
├── src/
│   ├── download.py
│   ├── qa.py
│   ├── kpi.py
│   ├── llm.py
│   ├── baseline.py
│   ├── evaluate.py
│   └── viz.py
├── figures/
├── reports/
├── notebooks/
├── run_pipeline.py
├── .python-version
├── .env.example
├── .gitignore
├── AI_USAGE.md
├── README.md
└── requirements.txt
```

Trong cây này, tên các mô-đun `.py` là gợi ý phân chia công việc, không phải yêu cầu phải đặt đúng mọi tên. Vai trò cần có được hiểu như sau:

| Nơi lưu hoặc chương trình | Nội dung, trách nhiệm |
| --- | --- |
| `configs/<city>.yaml` | Lưu thành phố, đường dẫn dữ liệu, danh sách snapshot và tham số QA, KPI, LLM. |
| `data/raw/` | Dữ liệu tải nguyên trạng do script tạo. Không commit. |
| `data/processed/` | Dữ liệu sau QA, các tệp `kpi_*.csv` và kết quả LLM đã lưu. Chỉ commit khi dưới 50 MB. |
| `data/samples/` | Mẫu nhỏ dùng thử và tệp nhãn tay tối thiểu 100 đánh giá, có `review_id` và nhãn tham chiếu. |
| `src/download.py` | Tải và kiểm tra tính toàn vẹn của các tệp đầu vào. |
| `src/qa.py` | Thực hiện quy tắc chất lượng dữ liệu và xuất báo cáo tác động. |
| `src/kpi.py` | Tính các chỉ số đã xác định. |
| `src/llm.py` | Trích xuất thông tin bằng LLM, quản lý cache và cách bỏ qua bước gọi khi phù hợp. |
| `src/baseline.py` | Thực hiện phương pháp đối chứng không dùng LLM. |
| `src/evaluate.py` | Đối chiếu dự đoán với nhãn tay và tính các thước đo đã chọn. |
| `src/viz.py` | Sinh hình và ghi vào `figures/`. |
| `figures/` | Các hình được chương trình tạo. |
| `reports/` | Báo cáo PDF, `qa_report.csv` và từ điển dữ liệu giải thích các cột, đơn vị, ý nghĩa. |
| `notebooks/` | Notebook khảo sát nếu có. Đây không phải chương trình điều phối chính của bài nộp. |
| `run_pipeline.py` hoặc Makefile | Gọi các bước theo thứ tự và truyền cấu hình để chạy toàn quy trình bằng một lệnh. |

Từ điển dữ liệu giúp một người chưa viết chương trình hiểu một cột nghĩa là gì, đo bằng đơn vị nào và mã nào dùng để nối. Đề nêu cần có nội dung này, không ấn định một tên tệp duy nhất cho nó.

Có thể đặt từ điển dữ liệu ở một tệp riêng trong `reports/` và ghi đường dẫn trong README để tiện tra cứu. Đây là gợi ý sắp xếp. Nó không tự tạo ra ngoại lệ về số trang hoặc phụ lục của PDF khi format chính thức chưa được công bố.

### 11.3. Đọc đúng cấu hình minh họa

Đề đưa ví dụ cấu hình Santiago sau. Mọi ngưỡng, cỡ mẫu và lựa chọn trong ví dụ cần được nhóm xem xét lại theo dữ liệu của mình:

```yaml
city: santiago
data_root: chile/rm/santiago
currency: CLP
snapshots:
  - 2025-09-27
  - 2025-12-29
  - 2026-03-30
  - 2026-06-29

qa:
  price_max_clp: 5000000
  min_nights_cap: 365
  dedupe_keys: [id, last_scraped]

kpi:
  area_col: neighbourhood_cleansed

llm:
  provider: gemini
  sample_size: 3000
  aspects:
    - vị trí
    - sạch sẽ
    - chủ nhà
    - giá trị
    - tiện nghi
    - độ ồn
    - an toàn
  cache: data/processed/llm_cache.jsonl

seed: 42
```

Đây là định dạng YAML. Một dòng gán tên cho một giá trị, phần thụt vào nhóm các lựa chọn cùng chủ đề, còn dấu `-` biểu diễn phần tử của một danh sách. Tệp cấu hình chỉ chứa lựa chọn, chương trình Python phải đọc tệp rồi thực hiện công việc tương ứng.

`currency` ghi loại tiền để diễn giải giá. Trong ví dụ Santiago, `CLP` là mã đồng peso Chile. Các khóa dưới `qa` là ví dụ nơi đặt tham số cho quy tắc, không chứng minh ngưỡng giá 5.000.000 CLP hoặc số đêm 365 là đúng cho mọi bài. `dedupe_keys` chỉ ra các cột dự định dùng nhận diện trùng, nhưng nhóm vẫn phải kiểm tra chúng có phù hợp với đơn vị quan sát hay không.

`area_col` cho biết cột dùng phân nhóm khu vực. `provider` là nhà cung cấp LLM. `aspects` liệt kê những khía cạnh muốn trích xuất. `cache` là nơi ghi kết quả đã lưu, còn `seed` giúp tái lập những thao tác ngẫu nhiên có hỗ trợ tham số này. Cố định seed không bảo đảm mẫu đại diện và không buộc mọi dịch vụ LLM trả cùng một kết quả.

Những con số và tên lựa chọn trong cấu hình không phải một phương án thực hành đã hoàn thành. Nhóm cần tự thiết kế, chạy thử và giải thích. Ví dụ thực hành của trang sẽ được xây dựng riêng ở phần 2.

## 12. Dùng AI, khai báo và bảo vệ thông tin

Khi làm ở nhà, bài tập lớn ở chế độ mở. Nhóm được dùng AI nhưng phải hiểu nội dung mình nộp, kiểm chứng kết quả và khai báo trung thực. Buổi vấn đáp ở chế độ đóng, không được dùng AI để trả lời thay.

Tệp `AI_USAGE.md` bắt buộc nằm ở gốc repo và được cập nhật trong quá trình làm. Cần nêu:

1. Công cụ đã dùng và công việc được hỗ trợ.
2. Các prompt then chốt. Mẫu trong đề gợi ý ghi 5–10 prompt, kèm bước xử lý và tệp liên quan, không phải sao chép mọi tin nhắn vào báo cáo.
3. Những chỗ AI thực sự làm sai và cách nhóm phát hiện.
4. Cách nhóm đối chiếu, chạy thử hoặc tính lại kết quả.

Không bịa ví dụ AI sai để điền cho đủ mục. Nếu một phần chưa phát hiện sai lệch, ghi nhận trung thực phạm vi đã xem xét và cách đã kiểm tra. Khai báo đầy đủ không làm bị trừ điểm vì đã dùng AI. Giấu hoặc khai man việc sử dụng vi phạm chính sách của môn.

Không commit khóa API. Chương trình đọc khóa từ biến môi trường theo tên ghi trong README. Khi chấm, giảng viên dùng khóa của họ. Việc chương trình chỉ chạy được vì có khóa ghi sẵn trong mã của nhóm là không phù hợp với yêu cầu bàn giao.

Khi gửi dữ liệu qua công cụ AI, cần tuân thủ [chính sách AI của học phần](https://courses.iaidev.com/programming-for-data-processing/2627-1/ai-policy.html), gồm các quy định liên quan dữ liệu cá nhân và thông tin nhạy cảm. Giấy phép của dữ liệu và quyền sử dụng công cụ không thay cho việc xem xét dữ liệu nào được đưa ra ngoài.

## 13. Cách đánh giá và buổi vấn đáp

Buổi vấn đáp kéo dài khoảng 20 phút cho mỗi nhóm. Không có phần thuyết trình mở đầu. Giảng viên hỏi riêng từng người, có thể chọn bất kỳ đoạn mã hoặc con số nào trong sản phẩm nhóm đã nộp.

Điểm nhóm là mức trần, sau đó được điều chỉnh theo vấn đáp của từng thành viên. Nếu không giải thích được phần được hỏi, cá nhân có thể bị trừ điểm dù phần đó do người khác viết. Vì vậy, mỗi người cần hiểu toàn bộ quá trình và các quyết định quan trọng, không chỉ nhớ chức năng tệp mình phụ trách.

Bốn nhóm tiêu chí được công bố là:

- Thiết kế và tái lập quy trình.
- Lưu trữ và thao tác dữ liệu.
- Trực quan hóa và phát hiện từ phân tích.
- Làm việc nhóm, đạo đức và minh bạch AI.

Điểm nhóm chấm theo thang 10. Trọng số chi tiết và mô tả các mức điểm sẽ được công bố dần. Không có căn cứ tự phân chia phần trăm cho bốn tiêu chí hoặc suy rằng một bộ ngưỡng kỹ thuật đã được ấn định sẵn.

Phần LLM còn được đánh giá trên bộ nhãn tay của nhóm. Bên cạnh việc chương trình chạy được, nhóm phải giải thích chất lượng trích xuất, cách đo và các trường hợp kết quả chưa đáng tin cậy. Dùng AI trong buổi vấn đáp là vi phạm chế độ đóng.

## 14. Tự đối chiếu trước khi bàn giao

Danh sách này giúp kiểm tra các yêu cầu của đề, không thay bộ test hoặc rubric chính thức:

- [ ] Repo riêng tư có đủ thành viên và giảng viên, liên kết đã được điền, lịch sử commit được cập nhật.
- [ ] Thành phố đúng phân công và đã tải đủ bốn snapshot bắt buộc bằng script.
- [ ] Các bảng và dữ liệu ranh giới khu vực được xử lý theo vai trò đã khảo sát. Nguồn và ngày snapshot có trong báo cáo.
- [ ] Dữ liệu thô nằm ở `data/raw/` và không được commit. Các tệp xử lý được commit đáp ứng giới hạn kích thước.
- [ ] QA bao gồm thiếu, ngoại lai, trùng trong và giữa snapshot, sai kiểu và danh mục lệch. Quy tắc có tên, điều kiện, lý do và hành động.
- [ ] `reports/qa_report.csv` cho thấy tác động lên số dòng và KPI trước, sau QA.
- [ ] Có 5–8 KPI, mỗi KPI có mục tiêu, công thức, đơn vị, tiền tệ khi cần và đầu ra `kpi_*.csv`.
- [ ] Có phân tích theo khu vực và thời gian, ít nhất một KPI và một hình dùng kết quả LLM.
- [ ] LLM trích xuất cảm xúc, khía cạnh khen/chê và ngôn ngữ với đầu ra có cấu trúc.
- [ ] Có phương pháp đối chứng không dùng LLM và ít nhất 100 nhãn tay để đánh giá.
- [ ] Đã báo cáo accuracy/F1 của cả hai phương pháp, phân tích lỗi và ước tính chi phí xử lý toàn bộ review của thành phố.
- [ ] Hình tự động sinh vào `figures/`. PDF trong `reports/` không quá 10 trang và ghi đúng mã commit bản nộp.
- [ ] Có từ điển dữ liệu, `README.md`, `.python-version`, tệp khóa phiên bản thư viện hoặc `requirements.txt`, `.env.example`, `.gitignore` và `AI_USAGE.md`.
- [ ] Clone repo vào thư mục mới, dựng môi trường theo README và chạy một lệnh tạo lại được số liệu, hình để đối chiếu.
- [ ] Chương trình đọc khóa API từ biến môi trường và vẫn thực hiện được phần LLM khi được yêu cầu gọi thật.
- [ ] Thử đổi cấu hình snapshot để phát hiện những đường dẫn hoặc ngày còn bị ghi cố định trong mã.
- [ ] Tag `final` trỏ đúng bản muốn nộp và đã được đẩy lên GitHub đúng hạn.
- [ ] Từng thành viên giải thích được lựa chọn QA, công thức KPI, cách đánh giá LLM và các con số trong báo cáo.

Clone là tạo một bản sao repo từ GitHub về máy, gồm mã nguồn và lịch sử Git. Việc clone vào thư mục mới và tạo lại kết quả là yêu cầu tự kiểm của đề. Thử thêm một snapshot khác là cách chuẩn bị hữu ích cho tình huống bộ test chung đổi mốc, không phải một mốc nộp thứ tư.

## 15. Đối chiếu ghi chú tham khảo với đề chính thức {#doi-chieu-ghi-chu}

[Tài liệu Google Docs được cung cấp](https://docs.google.com/document/d/17hqvglaYTn27vNw7siVPxpMGhL6goMkDngQfSOMF8NY/edit?tab=t.0) là một bản ghi lại cách hiểu bài tập lớn. Tài liệu giúp nhìn công việc theo các bước tải dữ liệu, QA, KPI, biểu đồ và báo cáo. Tuy nhiên, tài liệu còn nhắc đến một bảng phân công và những số lượng cụ thể chưa xuất hiện trong trang đề chính thức được đối chiếu ngày 19/10/2026.

Nếu các chi tiết đó đến từ thông báo hoặc bộ dữ liệu bổ sung của giảng viên, chúng có thể áp dụng cho nhóm được giao. Cần giữ lại thông báo hoặc đường dẫn bảng tương ứng để biết chính xác phạm vi. Việc chưa thấy trên trang đề không đủ để khẳng định thông tin bổ sung sai, nhưng cũng chưa đủ để áp dụng nó cho mọi nhóm.

### 15.1. Thành phố, số lượng chỗ ở và review

- Ghi chú nhắc Sydney. Danh sách 26 thành phố hiện công khai có Melbourne và chưa có Sydney. Nhóm cần đối chiếu phân công trên Canvas hoặc bảng được giảng viên gửi. Không lấy tên trong một ghi chú của nhóm khác để thay thành phố của mình.
- Ghi chú chọn 1.000 chỗ ở và nhắc lấy 5.000 review của mỗi chỗ ở. Đề công khai chưa ấn định hai số lượng này. Cần xác nhận 5.000 là tổng review, số tối đa hay số trên mỗi listing, tính ở snapshot nào và xử lý thế nào nếu nguồn không có đủ review.
- Ghi chú mô tả mỗi chỗ ở có 365 ngày trong calendar. Khi làm, phải đọc khoảng ngày thực có trong từng snapshot và xác minh độ đầy đủ. Không tự thêm số liệu chỉ để mỗi listing đủ 365 hàng.
- Đề yêu cầu tải đủ bốn snapshot bằng script. Có thể lấy đúng từng bộ tại địa chỉ của snapshot, không cần tải mọi phiên bản lịch sử của cả thành phố rồi lọc lại bốn ngày. Lọc ngày của review hoặc calendar là một công việc khác với chọn ngày snapshot.

Các số lượng hoặc cách chọn mẫu của một bộ dữ liệu riêng phải được ghi thành điều kiện đầu vào đã xác nhận. Với yêu cầu tự chọn mẫu trong đề chung, nhóm phải giải thích phương pháp và giới hạn mẫu của mình.

### 15.2. Tám vùng và những số đếm được ghi trong tài liệu

Ghi chú đề cập cột `analysis_area` tạo từ kinh độ, vĩ độ và chia thành tám vùng. Nó còn nêu các số đếm sau:

- Trong 1.000 listing có 875 mục loại `Entire home/apt` và 125 mục loại `Private room`.
- Số listing không có review ở bốn mốc lần lượt là 50, 30, 25 và 25.
- Mốc thứ tư có 20 listing không có giá.
- Mỗi vùng có 120–130 listing.

Những con số này chưa được quy định trên trang đề công khai đang lưu. Nếu có bộ test hoặc bảng phân công bổ sung, cần đọc cách chọn mẫu, cách chia vùng, định nghĩa “không có review” và thời điểm áp dụng từng số đếm. Không sửa giá, xóa review hay tạo hàng giả để ép dữ liệu tự khớp số lượng.

`analysis_area` có thể là cách nhóm chia vùng để phân tích, nhưng nó không tự thay yêu cầu phân tích theo `neighbourhood_cleansed`. Nếu được giao chia tám vùng, cần biết ranh giới và cách gán listing ở biên vùng. “Cắt theo kinh độ, vĩ độ” chưa xác định được duy nhất một phương pháp chia.

### 15.3. Dấu X, nhãn tay và kết quả của baseline

Ghi chú nhắc 1.000 review được đánh dấu X để chạy LLM và 100 trường hợp được đánh dấu để chấm tay. Trên trang đề công khai, cỡ mẫu LLM do nhóm chọn và giải thích, còn tập nhãn tay phải có ít nhất 100 trường hợp. Nếu được phát thêm bảng đánh dấu, cần xác nhận bảng, cột và mã review tương ứng trước khi chọn dữ liệu.

Khi đã biết tập được giao, giữ mã review để nối nhãn tay, dự đoán baseline và dự đoán LLM. Không dựa vào thứ tự dòng sau lọc, vì thứ tự có thể thay đổi. Nhãn `en`, `vi`, `fr` trong ghi chú là ví dụ về mã ngôn ngữ, không phải bằng chứng mọi review đều thuộc đúng ba ngôn ngữ ấy.

Một baseline là mốc so sánh. Đề công khai yêu cầu đo accuracy/F1 của cả baseline và LLM, nhưng không quy định LLM bắt buộc thắng baseline. Nếu LLM kém hơn, cần báo kết quả thật và phân tích nguyên nhân. Chọn lại tập chấm hoặc sửa nhãn để làm LLM có vẻ tốt hơn sẽ làm phép đánh giá mất ý nghĩa.

### 15.4. Chạy lại, dữ liệu trong repo và thông tin cần xác nhận

Đề đã nêu người chấm có thể đổi snapshot bằng cấu hình. Ghi chú còn mở rộng sang đổi thành phố. Nhóm có thể thiết kế cấu hình linh hoạt để chuẩn bị, nhưng cần đối chiếu thông báo chính thức trước khi coi việc đổi thành phố là một điều kiện chấm đã được công bố.

Không commit dữ liệu thô không có nghĩa repo phải thiếu mọi thư mục dữ liệu. Đề có `data/samples/` cho mẫu thử và nhãn tay, cùng `data/processed/` cho dữ liệu xử lý đáp ứng giới hạn kích thước. Script cần tự tạo thư mục lưu đầu vào khi tải. Việc tải tệp qua URL cũng không đồng nghĩa với việc phải có khóa API như dịch vụ LLM.

Tệp `.env` chỉ chứa cấu hình hoặc bí mật cục bộ và phải được bỏ qua khi commit. Python không tự đọc mọi tệp `.env`. Nếu chọn cách này, chương trình hoặc lệnh khởi chạy phải nạp giá trị đúng cách. Dù dùng cách nạp nào, chương trình vẫn phải nhận được khóa do giảng viên cung cấp qua biến môi trường theo README.

Trước khi áp dụng các điều kiện riêng trong ghi chú, ghi lại các việc cần xác nhận sau:

1. Thành phố, bốn snapshot và địa chỉ tải chính xác của bộ dữ liệu nhóm được giao.
2. Có hay không mẫu cố định 1.000 listing và các số đếm theo loại phòng, review, giá thiếu.
3. Nếu chia tám vùng, ranh giới và cách gán vùng cụ thể là gì?
4. Số 5.000 review áp dụng cho toàn mẫu hay từng listing, ở mốc nào?
5. Bảng đánh dấu X ở đâu, mã review và vai trò từng dấu X là gì?
6. Bộ test yêu cầu đổi snapshot, đổi thành phố hay cả hai?

Đây là các điểm cần xác nhận từ dữ liệu và hướng dẫn được giao, không phải sáu yêu cầu mới của đề. Trong lúc chờ thông tin, nhóm vẫn có thể dựng môi trường, đọc cấu trúc tệp, thiết kế cấu hình và chuẩn bị cách ghi QA. Tránh gắn cố định các con số chưa được xác nhận vào mã.

## Tài liệu tham khảo

- [Đề bài tập lớn Inside Airbnb, học kì 1 năm học 2026–2027](https://courses.iaidev.com/programming-for-data-processing/2627-1/projects/project_airbnb.html).
- [Chính sách sử dụng AI của học phần](https://courses.iaidev.com/programming-for-data-processing/2627-1/ai-policy.html).
- [Inside Airbnb: Các bộ dữ liệu công khai](https://insideairbnb.com/get-the-data/).
- [Inside Airbnb: Từ điển trường dữ liệu](https://docs.google.com/spreadsheets/d/1iWCNJcSutYqpULSQHlNyGInUvHg2BoUGoNRIGa6Szc4/edit).
- [Inside Airbnb: Các giả thiết và giới hạn của dữ liệu](https://insideairbnb.com/data-assumptions/).
- [RFC 7946: Định dạng GeoJSON](https://datatracker.ietf.org/doc/html/rfc7946).
- [Ghi chú cách hiểu bài tập lớn do người dùng cung cấp](https://docs.google.com/document/d/17hqvglaYTn27vNw7siVPxpMGhL6goMkDngQfSOMF8NY/edit?tab=t.0).

Đối chiếu đề và chính sách ngày 19/10/2026. Các nội dung được ghi là sẽ công bố sau, như format báo cáo và trọng số rubric, cần tiếp tục theo dõi thông báo của học phần.
