# Luna độc lập: Rà bản nháp Chương 24

Ngày rà: 12-10-2026. Nguồn đối chiếu: Young & Freedman, ấn bản 15, trang in 781–811; số trang PDF một-based bằng trang in + 20. Phạm vi công khai: mở đầu và sáu topic 24.1–24.6 trong Notes. Frontmatter của `docs/vat-ly-2/bai-giang/04-tu-dien-dien-moi.md` ghi `lessonStatus: draft`, phù hợp với phạm vi hiện có.

Các mục lý thuyết công khai đúng mạch và giả thiết chính: Điện dung đo Q/V của từng bản; chuỗi giữ cùng độ lớn Q trong trường hợp tụ bắt đầu chưa nạp; song song giữ cùng V; năng lượng được tính khác nhau khi Q hoặc V được giữ cố định; điện tích cảm ứng làm giảm trường trong điện môi; Gauss trong điện môi tuyến tính đếm điện tích tự do và dùng K tại từng điểm khi vật liệu thay đổi. Các ví dụ và các phép tính hiện có khớp với sổ QA trong `qa/physics/chapter24/`.

## Findings cần xử lý trước khi công bố

| Mức | Vị trí | Bằng chứng và ảnh hưởng | Sửa đề nghị |
| --- | --- | --- | --- |
| P1 | `docs/.vitepress/physics-image-labels.mjs:79,81–82,85–86,89` | Nhiều hình công khai vẫn chứa câu chú giải tiếng Anh bên trong ảnh nhưng glossary chỉ giải nghĩa tiêu đề hoặc một vài thuật ngữ. Hình 24.2 (trang in 783/PDF 803) còn câu về trường loe khi khe nhỏ so với kích thước bản, nhưng map chỉ ghi “fringing”. Hình 24.8–24.9 (trang in 786–787/PDF 806–807) còn các câu về cùng điện tích/cùng điện áp, cách cộng điện áp/điện tích và quan hệ điện dung tương đương. Hình 24.14–24.15 (trang in 794–795/PDF 814–815) còn câu về điện áp giảm khi đưa điện môi vào và điện tích cảm ứng làm giảm trường. Hình 24.18 (trang in 799/PDF 819) còn diễn giải phân tử không phân cực trở nên phân cực khi điện tích dương, âm tách nhẹ. Văn xuôi gần hình có giải thích một phần, nhưng người đọc ảnh vẫn thấy các câu tiếng Anh chưa được giải nghĩa theo yêu cầu từng hình. | Thêm cặp tiếng Việt cho toàn bộ câu chú giải trong đúng image ID, hoặc vẽ lại các dòng chú giải bằng tiếng Việt. Giữ mỗi bản giải nghĩa một lần trong glossary của hình tương ứng. |
| P3 | `raw_materials/physics/translations/chapter-24/05-mo-hinh-phan-tu.md:50` | Câu hỏi xếp thứ tự đặt danh sách sau dấu hai chấm, nhưng phần chữ sau lựa chọn (ii) và (iii) bắt đầu bằng chữ thường. | Viết hoa đầu phần chữ của từng lựa chọn để tuân quy tắc dấu hai chấm của repo. |

`qa/physics/chapter24/language-review.txt` còn có cảnh báo heuristic về mật độ chữ đậm và một đoạn lời giải thiếu từ nối. Đây là gợi ý biên tập, chưa thấy chúng làm sai nội dung hay bước suy luận trong đoạn được rà.

## Những phần đã đối chiếu

| Vùng nguồn | Nội dung đã kiểm | Kết quả |
| --- | --- | --- |
| Trang in 781–786, PDF 801–806 | Mở đầu, mục 24.1, Caution về ký hiệu C/Q, tụ phẳng/cầu/trụ và Ví dụ 24.1–24.4 | PASS. Định nghĩa Q là độ lớn trên từng bản, tổng cả tụ bằng không, công thức điện dung, đơn vị và các kết quả số khớp. |
| Trang in 786–790, PDF 806–810 | Mục 24.2, chuỗi/song song, hai Caution, chiến lược rút gọn mạng, màn hình cảm ứng, Ví dụ 24.5–24.6 và câu hỏi cuối mục | PASS về mạch vật lý, điều kiện nút giữa ban đầu trung hòa và các giá trị Q,V. Mô tả màn hình cảm ứng dùng mô hình thêm tụ nối tiếp như nguồn. Glossary hình 24.8–24.9 còn thiếu các câu giải thích. |
| Trang in 790–793, PDF 810–813 | Mục 24.3, tích phân công nạp, các dạng U, mật độ năng lượng, máy Z, Ví dụ 24.7–24.9, Caution năng lượng trường và câu hỏi cuối mục | PASS. Phân biệt bảo toàn điện tích với phần năng lượng chuyển sang nhiệt/bức xạ khi nối tụ, và không đếm năng lượng điện trường thành một phần bổ sung. |
| Trang in 793–799, PDF 813–819 | Mục 24.4, K, ε, điện tích liên kết, Ví dụ 24.10–24.11, đánh thủng và ứng dụng màng tế bào | PASS. Giữ điều kiện điện tích không đổi, V=V₀/K, C=KC₀, hướng cảm ứng và ví dụ số. Bảng vật liệu hiện diện. Một số câu chú giải trong Hình 24.14–24.15 chưa nằm trong glossary. |
| Trang in 799–800, PDF 819–820 | Mục 24.5, phân tử phân cực/không phân cực, điện tích liên kết, lực hút vật trung hòa, điện thoại và câu hỏi cuối mục | PASS về phân cực và lực tổng trong trường không đều. Hình 24.17 có giải nghĩa các nhãn chính; Hình 24.18 còn thiếu nghĩa đầy đủ của đoạn giải thích ở trong hình. |
| Trang in 801–802, PDF 821–822 | Mục 24.6, Gauss với điện tích tổng/free charge, điều kiện K biến thiên, Ví dụ 24.12 và câu hỏi cuối mục | PASS. Công thức và giới hạn điện môi tuyến tính/đẳng hướng được nêu; khi K thay đổi, bản dịch dặn dùng giá trị địa phương trong tích phân. |

## Hình và phạm vi draft

Đã xem contact sheet trang nguồn in 781–811, contact sheet assets, contact sheet figures, và mở riêng các trang 781, 787, 794, 799–802 cùng hình có nhiều chú giải 24.2, 24.5, 24.8–24.10, 24.13–24.18, 24.20 và 24.22. Không thấy crop nào cắt mất dữ kiện hình học thiết yếu. Các ảnh mang nhãn tiếng Anh còn đủ hình, nhưng các câu chú giải nêu ở trên chưa được giải nghĩa trong bảng glossary.

Draft công khai hiện gồm `00-mo-dau.md` và sáu topic `01`–`06`. Các bài luyện tập `08`–`11` trong raw materials chưa được đưa vào trang công khai, và bài 40–76 chưa soạn. Đây là trạng thái dự kiến của draft. Báo cáo này không đánh dấu chương hoàn tất; khi công bố, giữ `lessonStatus: draft` cho tới khi phần luyện tập và phạm vi còn lại được hoàn thiện.

Các tệp QA hiện có báo 20 nhóm kiểm tra lý thuyết, 21 câu hỏi thảo luận, 13 nhóm guided practice, cùng rà soát ngôn ngữ heuristic. Đã đọc các kết quả hiện có, không chạy lại script vì chúng ghi ra tệp QA khác phạm vi được phép của lượt rà này.
