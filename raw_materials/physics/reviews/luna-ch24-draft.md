# Luna độc lập: Rà bản nháp Chương 24

Ngày rà: 12-10-2026. Nguồn đối chiếu: Young & Freedman, ấn bản 15, trang in 781–811; số trang PDF một-based bằng trang in + 20. Phạm vi công khai: mở đầu và sáu topic 24.1–24.6 trong Notes. Frontmatter của `docs/vat-ly-2/bai-giang/04-tu-dien-dien-moi.md` ghi `lessonStatus: draft`, phù hợp với phạm vi hiện có.

Các mục lý thuyết công khai đúng mạch và giả thiết chính: Điện dung đo Q/V của từng bản; chuỗi giữ cùng độ lớn Q trong trường hợp tụ bắt đầu chưa nạp; song song giữ cùng V; năng lượng được tính khác nhau khi Q hoặc V được giữ cố định; điện tích cảm ứng làm giảm trường trong điện môi; Gauss trong điện môi tuyến tính đếm điện tích tự do và dùng K tại từng điểm khi vật liệu thay đổi. Các ví dụ và các phép tính hiện có khớp với sổ QA trong `qa/physics/chapter24/`.

## Findings đã rà lại và disposition

| Mức | Vị trí | Bằng chứng và ảnh hưởng | Sửa đề nghị |
| --- | --- | --- | --- |
| P1, resolved | `docs/.vitepress/physics23-24-image-annotations.mjs` | Các câu và nhãn tiếng Anh trong Hình 24.2, 24.8–24.9, 24.14–24.15, 24.18 hiện có cặp chú giải tiếng Việt. Map 24.1 chỉ giữ một cặp cho nhãn Conductor lặp. Mục kiểm tra ở mép ngoài ảnh Hình 24.10 đã bỏ vì nằm ngoài crop hình. | Đã tích hợp bảng chú giải sau caption hình bằng plugin trong `docs/.vitepress/config.mjs`. Đối chiếu lại map với OCR và các ảnh figure; không thấy thiếu câu/nhãn tiếng Anh trong nhóm ảnh công khai đã kiểm. |
| P3, resolved | `raw_materials/physics/translations/chapter-24/05-mo-hinh-phan-tu.md:50` | Danh sách lựa chọn hiện viết hoa chữ đầu ngay sau dấu hai chấm. | Không còn chỉnh sửa cần thiết. |

`qa/physics/chapter24/language-review.txt` còn có cảnh báo heuristic về mật độ chữ đậm và một đoạn lời giải thiếu từ nối. Đây là gợi ý biên tập, chưa thấy chúng làm sai nội dung hay bước suy luận trong đoạn được rà.

## Những phần đã đối chiếu

| Vùng nguồn | Nội dung đã kiểm | Kết quả |
| --- | --- | --- |
| Trang in 781–786, PDF 801–806 | Mở đầu, mục 24.1, Caution về ký hiệu C/Q, tụ phẳng/cầu/trụ và Ví dụ 24.1–24.4 | PASS. Định nghĩa Q là độ lớn trên từng bản, tổng cả tụ bằng không, công thức điện dung, đơn vị và các kết quả số khớp. |
| Trang in 786–790, PDF 806–810 | Mục 24.2, chuỗi/song song, hai Caution, chiến lược rút gọn mạng, màn hình cảm ứng, Ví dụ 24.5–24.6 và câu hỏi cuối mục | PASS về mạch vật lý, điều kiện nút giữa ban đầu trung hòa và các giá trị Q,V. Mô tả màn hình cảm ứng dùng mô hình thêm tụ nối tiếp như nguồn. Glossary hình 24.8–24.9 còn thiếu các câu giải thích. |
| Trang in 790–793, PDF 810–813 | Mục 24.3, tích phân công nạp, các dạng U, mật độ năng lượng, máy Z, Ví dụ 24.7–24.9, Caution năng lượng trường và câu hỏi cuối mục | PASS. Phân biệt bảo toàn điện tích với phần năng lượng chuyển sang nhiệt/bức xạ khi nối tụ, và không đếm năng lượng điện trường thành một phần bổ sung. |
| Trang in 793–799, PDF 813–819 | Mục 24.4, K, ε, điện tích liên kết, Ví dụ 24.10–24.11, đánh thủng và ứng dụng màng tế bào | PASS. Giữ điều kiện điện tích không đổi, V=V₀/K, C=KC₀, hướng cảm ứng và ví dụ số. Bảng vật liệu hiện diện. Các câu chú giải trong Hình 24.14–24.15 hiện có cặp tiếng Việt trong map ảnh. |
| Trang in 799–800, PDF 819–820 | Mục 24.5, phân tử phân cực/không phân cực, điện tích liên kết, lực hút vật trung hòa, điện thoại và câu hỏi cuối mục | PASS về phân cực và lực tổng trong trường không đều. Chú giải Hình 24.17–24.18 hiện bao gồm các câu giải thích trong hình. |
| Trang in 801–802, PDF 821–822 | Mục 24.6, Gauss với điện tích tổng/free charge, điều kiện K biến thiên, Ví dụ 24.12 và câu hỏi cuối mục | PASS. Công thức và giới hạn điện môi tuyến tính/đẳng hướng được nêu; khi K thay đổi, bản dịch dặn dùng giá trị địa phương trong tích phân. |

## Hình và phạm vi draft

Đã xem contact sheet trang nguồn in 781–811, contact sheet assets, contact sheet figures, và mở riêng các trang 781, 787, 794, 799–802 cùng hình có nhiều chú giải 24.2, 24.5, 24.8–24.10, 24.13–24.18, 24.20 và 24.22. Không thấy crop nào cắt mất dữ kiện hình học thiết yếu. Đã đối chiếu lại map chú giải tích hợp với OCR và ảnh nguồn. Riêng Hình 24.10, lời kiểm tra nằm ngoài crop mạng tụ nên không đưa vào map.

Draft công khai hiện gồm `00-mo-dau.md` và sáu topic `01`–`06`. Các bài luyện tập `08`–`11` trong raw materials chưa được đưa vào trang công khai, và bài 40–76 chưa soạn. Đây là trạng thái dự kiến của draft. Báo cáo này không đánh dấu chương hoàn tất; khi công bố, giữ `lessonStatus: draft` cho tới khi phần luyện tập và phạm vi còn lại được hoàn thiện.

Các tệp QA hiện có báo 20 nhóm kiểm tra lý thuyết, 21 câu hỏi thảo luận, 13 nhóm guided practice, cùng rà soát ngôn ngữ heuristic. Đã đọc các kết quả hiện có, không chạy lại script vì chúng ghi ra tệp QA khác phạm vi được phép của lượt rà này.


## Disposition sau lượt kiểm tra tích hợp

Các mục P1/P3 trong bảng trên đã được xử lý. Đã xác nhận chú giải tiếng Việt hiển thị theo dạng danh sách dưới caption, không bị lặp trong cùng ảnh. Phần draft công khai vẫn có trạng thái `draft`: phạm vi luyện tập và các bài 40–76 chưa hoàn tất theo kế hoạch, nên kết luận này không đánh dấu chương 24 hoàn tất. Không phát hiện lỗi nội dung mới trong sáu topic, ví dụ hay các hình đã kiểm trong lượt này.
