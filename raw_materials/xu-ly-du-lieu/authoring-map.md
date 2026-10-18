# Sổ biên soạn môn Lập trình xử lý dữ liệu

## Ranh giới nguồn

Trục học tập gồm chương 1–13 và phụ lục A, B của *Python for Data Analysis*, ấn bản 3. Mỗi chương có bài giảng độc lập bằng tiếng Việt, giữ phạm vi kỹ thuật nhưng dùng mạch giảng và ví dụ riêng. Không dịch toàn văn, không tái bản lời văn hay hình được bảo hộ. Mã MIT chỉ được sử dụng khi có ghi công phù hợp.

IAI là nguồn bổ sung kỹ thuật. Chỉ đưa một mục vào bài khi có câu hỏi chuyên môn cụ thể của chương cần mục đó. Nguồn bổ sung không quyết định thứ tự chương hoặc làm phát sinh một học phần LLM độc lập.

Loại toàn bộ nội dung tổ chức học phần, đánh giá, điểm số, UET, bài tập lớn, vấn đáp và quy định dùng AI đóng/mở. Không dùng notebook `2627-1/notebooks/lecture-01.ipynb`, kể cả ví dụ trong notebook. Phần thiết lập môi trường của trang lecture-01 chỉ được dùng để đối chiếu kỹ thuật đã thuộc chương 1. Lecture-15 nằm ngoài phạm vi. Lịch công khai không liên kết lecture-09, do đó không suy đoán hoặc dựng một bài 9 IAI.

## Đối chiếu chương và phần bổ sung

| Chương | Nội dung chính | Phần IAI được xét | Bài tập IAI minh thị |
| --- | --- | --- | --- |
| 1 | Quy trình dữ liệu, hệ công cụ, thiết lập môi trường | Lecture 1: Môi trường và khả năng chạy lại | Không dùng notebook lecture-01 |
| 2 | Python, IPython, Jupyter, đối tượng, kiểu và điều khiển | Lecture 2: Các thao tác phù hợp với chương | Không có đề được đánh số |
| 3 | Cấu trúc dữ liệu, hàm, generator, ngoại lệ và tệp | Lecture 2: Hàm làm sạch, CSV, JSON, pathlib | Bổ sung bài tập của StudyHub |
| 4 | ndarray, chọn phần tử, ufunc, tổng hợp, đại số tuyến tính, mô phỏng | Lecture 3: Cơ chế thực thi, bộ nhớ, dtype và view/copy | Lecture 3: Bài 1–6 |
| 5 | Series, DataFrame, Index, khớp nhãn và thống kê | Lecture 4 và phần chọn/gán/map của lecture 5 | Lecture 4: Bài 1–5. Lecture 5: Bài 1–2 |
| 6 | CSV, JSON, HTML/XML, Excel, định dạng nhị phân, API và SQL | Lecture 6: DuckDB, Parquet và kiểm tra cách đọc | Lecture 6: Bài 1–3 |
| 7 | Giá trị thiếu, biến đổi, chuỗi, regex và danh mục | Lecture 7, 10. Lecture 11: Chỉ phần văn bản thành bảng và kiểm chứng dữ liệu | Lecture 7: Bài 1–3. Lecture 10: Bài 1–3 |
| 8 | MultiIndex, ghép bảng và chuyển dạng | Lecture 5: Kiểm tra khóa, số lần khớp và chuỗi biến đổi | Lecture 5: Bài 4 |
| 9 | Matplotlib, pandas, seaborn và cách đọc biểu đồ | Lecture 12–13: Font, xuất hình, bản đồ, tương tác và phản biện biểu đồ | Không có đề được đánh số. Các tình huống phản biện phải được giảng |
| 10 | Tổng hợp, transform, apply, bảng pivot và bảng chéo | Lecture 5: Đơn vị quan sát, cỡ nhóm và trung bình gộp | Lecture 5: Bài 3 |
| 11 | Datetime, chỉ mục thời gian, múi giờ, kỳ, resample và cửa sổ | Lecture 8: Tháng thiếu, kỳ chưa trọn và chọn kỳ gốc | Lecture 8: Bài 1–3 |
| 12 | Patsy, statsmodels và scikit-learn | Không ép thêm IAI nếu không có mục phù hợp | Bổ sung bài tập của StudyHub |
| 13 | Phân tích log, đánh giá, tên, thực phẩm và khoản đóng góp | Lecture 14: Mẫu số, cơ cấu nhóm và thẩm định kết luận | Các tình huống kiểm tra kết luận trong lecture 14 |
| A | NumPy nâng cao, kiểu, bố trí bộ nhớ, ufunc, sắp xếp, Numba và tệp lớn | Lecture 3: Các chi tiết liên quan đến bộ nhớ và hiệu năng | Dẫn về các bài tập chương 4 khi phù hợp |
| B | Magic, lịch sử, hệ điều hành, debug, đo thời gian và profile | Không thêm nội dung vận hành học phần | Bổ sung bài tập của StudyHub |

## Truy vết và giấy phép

`source-inventory.json` ghi URL đã truy cập, dấu kiểm nội dung và các đề mục. Bản đầy đủ chỉ phục vụ đối chiếu trong thư mục tạm của máy, không được đưa vào nội dung xuất bản.

`authoring-contract.json` ấn định slug, tiêu đề, tiên quyết và phân công. `coverage-a.json`, `coverage-b.json`, `coverage-c.json` ghi nơi đến của từng đơn vị nguồn cùng lý do loại. Các bài tập chuyển thể IAI được ghi công trong tài liệu tham khảo của bài, kèm giấy phép [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) và [nguồn giấy phép](https://github.com/uet-iai-course/programming-for-data-processing/blob/main/LICENSE). Quy định này chỉ áp dụng cho phần chuyển thể tương ứng, không thay giấy phép mã nguồn toàn repo.

Giữ các URL cũ khi có thể. Các bài IAI cũ được hợp nhất có trang chuyển hướng tới chương phù hợp. Đường dẫn cũ chứa tên chính sách AI được giữ vì tương thích, còn tiêu đề và nội dung mới không có phần chính sách.

## Bổ sung bộ bài thực hành

Đợt bài thực hành đối chiếu 13 notebook trong repo `notebook-labs-template` với
14 notebook lab trên trang học liệu IAI, gồm bản regex riêng. Notebook lab-01
được dùng cho thao tác notebook, trạng thái biến và tính tỷ lệ, theo yêu cầu
bổ sung của người dùng. Việc này không thay ranh giới loại notebook lecture-01.

Chỉ giữ đề kỹ thuật, dữ liệu, yêu cầu đầu vào/đầu ra và các biến thể có nội dung
khác. Loại các ô điểm số, khai báo và chế độ AI, nộp bài, public checks, grader
và hỗ trợ bài tập lớn. Một yêu cầu hàm có giá trị kỹ thuật vẫn được chuyển
thành mô tả đầu vào/đầu ra, dù nó từng nằm trong khung chấm điểm.

Mỗi bài thực hành có hai cách giải, giải thích các hàm chính, output đã chạy
và trường hợp biên. Cách thứ hai phù hợp với xử lý dữ liệu thực tế, không mặc
nhiên được gọi là nhanh hơn nếu thiếu căn cứ. Giữ ràng buộc thư viện của đề.

`lab-source-inventory.json` ghi dấu kiểm của 27 notebook và vị trí mục nguồn.
`labs/coverage-*.json` ghi nguồn và nơi đến của yêu cầu, kể cả phần gộp hoặc
loại. `lab-placement.json` ghi cách đặt bộ bài trong tab Bài tập của từng
chương. Các fragment thực hành cũ được thay bởi bộ tương ứng đã mở rộng lời
giải, tránh xuất hiện cả bản ngắn lẫn bản đầy đủ của cùng một lab.

Các notebook gốc chỉ lưu trong thư mục tạm ngoài repo. Các file snapshot lớn
được liên kết đúng phiên bản, không đưa toàn bộ dữ liệu vào bundle của site.

## Kiểm chứng bài thực hành

Chạy từng `scripts/verify-data-lab-*.py` và kiểm độc lập số liệu, đối chiếu cả
hai cách giải. `scripts/verify-data-labs-browser.mjs` kiểm các bộ bài đang mở
lời giải ở 360, 375, 768 và 1280px, gồm bảng, mã, hình, font và LaTeX. Không
chạy build toàn cục trên máy người dùng.

## Kiểm chứng bài giảng

Chạy ba script `scripts/verify-data-course-{a,b,c}.py`, bộ kiểm cấu trúc bài giảng và bộ kiểm thử của skill. Đối chiếu bộ đề IAI trong inventory với coverage và nội dung thực tế. Rà render bằng dev server, không build toàn site trên máy người dùng. Kiểm font tiếng Việt, công thức và bề rộng màn hình nhỏ, cả Notes và các thẻ ôn tập.

## Kết quả kiểm bộ bài thực hành ngày 18/10/2026

Đã đặt 16 bộ theo chủ đề vào 11 tab Bài tập, với 159 đề và 318 chương trình
lời giải độc lập. Bộ bonus regex gồm đủ 20 bài, 321 cặp đầu vào/đầu ra và 20
đoạn văn để đối chiếu. Dữ liệu kiểm là dữ liệu thuần, không chứa mã chấm bài.

Lượt kiểm cuối dùng `complete-data-lab-code.py --check --published-only` để
chạy đúng code đang hiển thị, mỗi cách trong một tiến trình và thư mục mới.
Lượt kiểm trình duyệt gồm 44 tổ hợp chương và độ rộng 360/375/768/1280 px.
Các bảng giữ cấu trúc thật trên desktop và có nhãn cột ở từng ô khi chuyển
sang thẻ trên điện thoại. Code dùng font 14 px, giữ thụt dòng, cho cuộn riêng
trong khối mã và có nút sao chép tối thiểu 44 px.
