---
title: "Dự án mẫu: Phân tích Porto"
description: "Kế hoạch độc lập, kiến trúc và chương trình xử lý dữ liệu Porto có kết quả chạy thực tế."
course: xu-ly-du-lieu
section: project
pageClass: data-project-brief
outline: [2, 2]
prev: false
next: false
---

<script setup>
import ProjectSections from '../../../src/features/course-project/components/ProjectSections.vue'
import ProjectWorkflow from '../../../src/features/course-project/components/ProjectWorkflow.vue'
import ProjectPlan from '../../../src/features/course-project/components/ProjectPlan.vue'
</script>

<ProjectSections active="practice" />

# Dự án mẫu: Phân tích Porto

Một nhóm phân tích muốn giúp đơn vị quản lý du lịch hiểu nguồn cung chỗ ở, lịch còn sẵn và trải nghiệm khách. Dự án chọn Porto, xây một quy trình nhỏ có thể chạy lại, rồi dùng kết quả để kiểm tra từng quyết định xử lý.

Đây là dự án độc lập trên dữ liệu công khai. Mẫu được chọn có seed, không dùng danh sách thành viên, phân công hoặc tập ID của một nhóm học phần. Lịch dưới đây là kế hoạch đề xuất, còn kết quả đã chạy được trình bày riêng ở cuối trang.

[Tải mã nguồn dự án](/materials/xu-ly-du-lieu/airbnb/airbnb-porto.zip) · [Tải bảng kế hoạch để tự cập nhật](/materials/xu-ly-du-lieu/airbnb/ke-hoach-doc-lap.csv)

## 1. Phạm vi và lựa chọn ban đầu

| Lựa chọn của dự án | Cách thực hiện |
| --- | --- |
| Địa bàn và dữ liệu | Porto, tiền tệ EUR. Bốn mốc 21/09/2025, 25/12/2025, 26/03/2026 và 23/06/2026. |
| Tập listing | Chọn 120 ID từ giao các listing có ở cả bốn mốc, bằng seed `20261019`. Lưu danh sách để chạy lại. |
| Thời gian trong calendar | Giữ 30 ngày tính từ từng ngày snapshot. Cửa sổ dài bằng nhau nhưng thuộc những thời điểm khác nhau. |
| Giá | Chỉ phân tích giá chào ở mốc cuối. Không gọi giá chào là doanh thu đã thu hoặc ADR thực thu. |
| Review cho LLM | Dự kiến tối đa 300 review duy nhất của tập listing. Giữ nguyên văn bản trong đầu vào cục bộ. |
| Nhãn tham chiếu | Chuẩn bị 160 hàng nhãn trống, dự kiến 40 để điều chỉnh và 120 để đánh giá cuối. Người đọc tự gán trước khi xem dự đoán. |
| Công cụ | Python và thư viện chuẩn cho tải, xử lý bảng, thống kê, HTTP và sinh SVG. Cấu hình JSON giúp đổi tham số. |

Chọn giao ID giúp so cùng một nhóm listing qua các mốc, nhưng loại các listing mới xuất hiện hoặc biến mất. Vì vậy, các kết quả mô tả nhóm tồn tại qua bốn mốc, không đo tăng trưởng nguồn cung toàn thành phố. Đây là giới hạn cần giữ trong báo cáo.

Các con số mẫu và thời gian là lựa chọn của dự án minh họa. Khi làm bài chính thức, phải dùng đầu vào và điều kiện được giao cho nhóm.

## 2. Kiến trúc và quyết định QA

<ProjectWorkflow />

Ba tên Bronze, Silver và Gold chỉ ba trạng thái: Dữ liệu nguyên trạng, dữ liệu đã chuẩn hóa và bảng phục vụ phân tích. Trong dự án này chúng tương ứng với tệp và bước Python, không kéo theo yêu cầu dùng Spark, Databricks hoặc cơ sở dữ liệu.

### Những kiểm tra thực sự cần cho mẫu Porto

Mẫu đã được đọc và tính thử trước khi chọn quy tắc. Bốn quyết định dưới đây phục vụ trực tiếp các kết quả đang làm:

| Quan sát và câu hỏi cần giải quyết | Quyết định trong bản mẫu |
| --- | --- |
| Một listing xuất hiện qua bốn snapshot. Có phải hàng trùng cần xóa? | Không. Khóa là snapshot và listing. Giữ bốn lần quan sát để so sánh đúng đối tượng. Chỉ từ chối khóa lặp trong cùng mốc. |
| KPI đếm và KPI giá cần cùng số hàng không? | Không. Giữ 120 listing để đếm, dùng 111 giá hợp lệ mốc cuối để tính trung vị. Không xóa listing khỏi toàn bộ phân tích chỉ vì không dùng được giá. |
| Mỗi hàng calendar có cùng ý nghĩa với một listing không? | Không. Một hàng là một listing tại một ngày. Chọn đúng cửa sổ, đếm ngày có trạng thái hợp lệ và tính theo từng listing trước khi lấy trung bình. |
| Review lặp trong nhiều snapshot có phải nhiều ý kiến? | Không. Dùng review ID và nội dung để nhận diện, giữ dấu vết xuất hiện nhưng chỉ chọn một lần cho mẫu đánh giá. |

Giá hợp lệ mốc cuối trong mẫu nằm từ 43,50 đến 773 EUR/đêm. Mức cao nhất chưa đủ để kết luận dữ liệu sai. Bản mẫu giữ các giá này và xem phân bố, không tự xóa theo ba độ lệch chuẩn hoặc một ngưỡng chưa có lý do.

Bản đồ hiện tổng hợp theo tên khu, không dựa vào điểm tọa độ listing. Vì vậy, ví dụ không thêm một quy trình kiểm tọa độ hay phân vùng mới không phục vụ phép tính đang làm. Khi chuyển sang bản đồ điểm, đó mới là kiểm tra cần bổ sung.

::: details Mã kiểm tra và thời điểm ghi tác động

Cột khóa được kiểm trước khi xử lý. Giá trị không hợp lệ được giữ dấu vết và chỉ loại khỏi KPI chịu ảnh hưởng. Các nhãn `ERROR`, `WARN` hoặc `INFO` không thay cho việc nêu hành động cụ thể.

Số dòng và cờ QA có ngay khi đọc. Phần so sánh KPI trong `qa_report.csv` được hoàn thiện sau bước tính chỉ số. Vì vậy, báo cáo QA và chặng KPI có thể gối đầu, không phải chờ mọi ô báo cáo QA xong mới được tính chỉ số.

Dữ liệu thô giữ nguyên, mỗi lượt chạy có thư mục riêng. Chỉ cập nhật con trỏ kết quả gần nhất khi lượt chạy đã hoàn thành. Kiểm thử dùng fixture riêng, không có cơ chế tự thay dữ liệu thật bằng fixture.

:::

## 3. Kế hoạch thực hiện và điều kiện hoàn thành

Kế hoạch gồm tám chặng, mỗi chặng có đầu ra và cách xác nhận. Có thể làm đồng thời phần gán nhãn, baseline và QA sau khi đã chốt mẫu review. Không cần chờ toàn bộ KPI xong mới chuẩn bị nhãn hoặc nối chương trình.

<ProjectPlan />

Ngày trong kế hoạch tính từ lúc bắt đầu, không thay các mốc nộp của môn. Với nhóm nhiều người, mỗi việc có người thực hiện và người kiểm tra. Người kiểm tra phải đối chiếu đầu ra với điều kiện đạt, không chỉ xác nhận mã chạy hết.

Một người tự làm có thể thay lượt kiểm tra chéo bằng phép tính độc lập trên mẫu nhỏ, bộ dữ liệu kiểm thử có đáp án biết trước và lần chạy trong thư mục mới. Cách này không thay yêu cầu nhóm 4–5 thành viên của bài nộp chính thức.

## 4. Thiết kế bảy KPI

| Chỉ số | Định nghĩa và phạm vi |
| --- | --- |
| Số listing | Đếm ID phân biệt trong mẫu tại một snapshot và khu vực. Với tập giao ID cố định, chỉ số mô tả quy mô mẫu. |
| Tỷ lệ cho thuê cả chỗ ở | Số listing `Entire home/apt` chia số listing có loại phòng hợp lệ trong cùng nhóm. Báo mẫu số. |
| Trung vị số đêm tối thiểu | Trung vị `minimum_nights` của listing có giá trị hợp lệ, theo snapshot và khu vực. Đơn vị là đêm. |
| Mức sẵn có 30 ngày tới | Tính tỷ lệ ngày `available = t` trên các ngày có trạng thái hợp lệ của từng listing, rồi lấy trung bình theo listing. Kèm độ phủ lịch so với cửa sổ 30 ngày. |
| Trung vị giá chào mốc cuối | Trung vị `price` đọc được và dương ở mốc cuối, theo EUR cho một đêm như trường nguồn mô tả. Báo số listing đủ điều kiện. |
| Tỷ lệ listing chưa có review | Số listing có `number_of_reviews = 0` chia số listing có số đếm review hợp lệ trong cùng nhóm. Không suy thành tỷ lệ khách hài lòng. |
| Tỷ lệ review tiêu cực từ LLM | Số review duy nhất có nhãn `negative` chia số review có dự đoán hợp lệ trong phạm vi xét. Báo độ phủ và chất lượng đánh giá đi kèm. |

Chỉ số theo khu vực dùng `neighbourhood_cleansed`. Dự án công khai này không tự tạo `analysis_area` từ bảng của nhóm khác. Khi làm theo một bộ phân công có vùng riêng, giữ cả hai hệ vùng và đặt tên kết quả rõ ràng.

Không lấy trung bình các tỷ lệ khu vực để gọi là tỷ lệ toàn mẫu nếu mẫu số khác nhau. Hãy tính từ tổng tử số và tổng mẫu số khi đó là định nghĩa của chỉ số chung. Với trung vị, cần trở về các giá trị gốc đủ điều kiện, không lấy trung vị của các trung vị khu vực.

::: details Đọc thêm về kiến trúc, occupancy và các gợi ý nghiên cứu

| Gợi ý | Cách dùng trong dự án |
| --- | --- |
| Bronze → Silver → Gold | Giữ cách tách nguyên trạng, chuẩn hóa và tổng hợp. Đây là mẫu thiết kế, không phải điều kiện bắt buộc của đề. |
| Càng nhiều QA càng tốt | Chọn quy tắc theo hành động khi phát hiện vấn đề. Đo thời gian chạy nếu kiểm tra lớn, gộp cảnh báo có cùng nguyên nhân. |
| Mọi lỗi Bronze đều dừng | Không áp dụng máy móc. Thiếu tệp bắt buộc có thể chặn bước, còn thay đổi ở cột tùy chọn có thể chỉ cần cảnh báo. |
| Xóa giá ngoài ba độ lệch chuẩn | Chỉ coi là cách tìm ứng viên cần xem. Phân bố giá có thể lệch, giá cao không tự là lỗi. Giữ giá gốc và so sánh độ nhạy. |
| Ép occupancy vào đoạn 0–1 | Không dùng `clip()` để che công thức hoặc dữ liệu sai. Tìm nguyên nhân trước khi quyết định loại khỏi chỉ số nào. |
| Giá chia số đêm tối thiểu | Không dùng để tạo giá theo đêm. `minimum_nights` là điều kiện lưu trú, không phải số đêm mà giá nguồn đang bao gồm. |
| Review chia tuổi listing để ước occupancy | Chưa đủ cơ sở. Review không phải toàn bộ lượt đặt, ngày review đầu không chắc là ngày bắt đầu kinh doanh và độ dài lưu trú phải có giả thiết. |
| RevPAR từ giá chào và lịch không sẵn có | Không gọi là RevPAR thực thu. Thiếu doanh thu và đêm bán thực tế. Chỉ mô hình hóa khi có cơ sở và phân tích độ nhạy riêng. |
| Bốn snapshot thành mùa vụ theo tháng | Bốn quan sát không tự tạo lịch sử tháng đầy đủ. Cửa sổ lịch ở mỗi mốc nhìn về tương lai, không phải doanh thu tháng đã xảy ra. |

<details>
<summary>Vì sao không tùy tiện nhân hai số trung bình?</summary>

Xét hai đơn vị giả định có cùng số đêm cung ứng. Giá mỗi đêm lần lượt là 90 và 110, tỷ lệ bán lần lượt là 0,2 và 0,8. Doanh thu trên mỗi đêm cung ứng chung là trung bình của 18 và 88, bằng 53.

Nếu lấy giá trung bình 100 nhân tỷ lệ trung bình 0,5, ta được 50. Hai kết quả khác nhau vì việc lấy trung bình đã làm mất quan hệ giữa giá và lượng bán. Với dữ liệu giao dịch thật, phải gộp doanh thu và số đêm theo cùng định nghĩa rồi tính chỉ số.

Định nghĩa ADR và RevPAR có thể đối chiếu tại [STR/CoStar](https://www.costar.com/products/str-benchmark/resources/faqs). Mô hình occupancy của Inside Airbnb cũng nêu các giả thiết riêng về tỷ lệ viết review và độ dài lưu trú, không đồng nhất với dữ liệu đặt phòng quan sát được.

</details>


:::

## 5. Chạy chương trình và đọc trạng thái

Giải nén mã nguồn vào một thư mục mới, đọc README và dùng đúng Python ghi trong `.python-version`. Lệnh chạy phần dữ liệu và baseline mà chưa gọi dịch vụ LLM là:

```bash
python run_pipeline.py --config configs/porto.json --skip-llm
```

Các tệp nguồn tải về được giữ cục bộ và bỏ qua khi commit. Lần đầu cần mạng và dung lượng đĩa cho các bộ đầy đủ của thành phố, dù chỉ giữ một mẫu nhỏ trong bảng xử lý. Lần chạy lại dùng tệp đã tải nếu chúng vẫn vượt qua kiểm tra.

Chế độ `--skip-llm` không có nghĩa hoàn thành phần LLM. Để chạy thật, làm theo README để đặt khóa API trong biến môi trường, chọn mô hình còn khả dụng, kiểm hạn mức và gọi chế độ LLM. Tệp nhãn tay vẫn cần người đọc hoàn thành trước khi có bảng accuracy/F1 đáng tin.

::: details Những đầu ra cần tìm sau khi chạy

- Manifest: Từng URL, snapshot, số byte và checksum của nguồn.
- Bảng chuẩn hóa: Listing theo snapshot, calendar theo ngày và review duy nhất, kèm các cột khóa.
- Báo cáo QA: Quy tắc, điều kiện, hành động, số dòng và ảnh hưởng KPI.
- Bảng KPI: Giá trị, đơn vị, mẫu số, snapshot và trạng thái sẵn sàng.
- Hình SVG: Sinh từ bảng kết quả, có tên trục, chú giải và phạm vi mẫu.
- Tệp nhãn tay: Các cột nhãn trống, tách khỏi dự đoán baseline/LLM.
- Báo cáo đánh giá: Có kết quả khi đủ nhãn người và dự đoán. Nếu chưa đủ, ghi đang chờ cùng lý do.

:::

<!-- @include: ./ket-qua-porto.md -->

## Tài liệu tham khảo

- [Đề bài tập lớn Inside Airbnb](https://courses.iaidev.com/programming-for-data-processing/2627-1/projects/project_airbnb.html).
- [Inside Airbnb: Tải dữ liệu](https://insideairbnb.com/get-the-data/).
- [Inside Airbnb: Giới hạn và mô hình occupancy](https://insideairbnb.com/data-assumptions/).
- [Microsoft Learn: Kiến trúc Medallion](https://learn.microsoft.com/en-us/azure/databricks/lakehouse/medallion).
- [STR/CoStar: Định nghĩa các chỉ số khách sạn](https://www.costar.com/products/str-benchmark/resources/faqs).
