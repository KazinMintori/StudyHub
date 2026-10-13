# Audit lý thuyết và hình Chương 29

## Phạm vi đã rà

Đối chiếu 10 bản dịch `00-mo-dau.md` đến `09-tom-tat.md` với văn bản nguồn `qa/physics/full-source/pdf-0973.txt` đến `pdf-0997.txt`, tương ứng trang in 953–977 theo quy ước index đã giao. Đọc các quy chuẩn trong `studyhub-lecture/SKILL.md` và `references/repo-format.md`.

Đã đối chiếu lần lượt các mục 29.1–29.8, toàn bộ nhãn (29.1)–(29.24), 11 ví dụ 29.1–29.11, câu hỏi mở đầu và sáu câu tự kiểm ở cuối các mục 29.2–29.7. Các câu hỏi vẫn nằm ngay sau phần lý thuyết liên quan, còn đáp án được gập trong `<details>` hoặc `::: details`. Rà các ứng dụng TMS, nhà máy điện, máy phát và động cơ, xe điện, đánh lửa máy bay, guitar, hãm Fu-cô, Io, tụ điện và MRI.

Đã xem trực quan 27 crop Hình 29.1–29.27, hình cầu nối 29.28, hình mở đầu, hình tổng kết và các annotation trong ba module lý thuyết/tổng kết. Đối chiếu bố cục với PDF trực tiếp trang 953, 966–967 và ảnh tổng quan các trang in 953–977. Đã đọc module 8 chủ đề, 12 slide, cheatsheet và foundation/Wiki của bài cảm ứng điện từ. Tính lại các giá trị số trong Ví dụ 29.1, 29.2, 29.4, 29.9 và 29.11 bằng Python. Chưa kiểm tra bản dựng ở viewport điện thoại 320 px.

## Phát hiện cần xử lý

1. **Nghiêm trọng về lập luận vật lý, mục 29.5, dòng 33 của `05-dien-truong-cam-ung.md`.** Câu “Nếu điện trường hướng xuyên tâm thì định luật Gauss đòi hỏi có điện tích thuần bên trong vòng” dùng định luật Gauss sai: đường tròn không phải mặt kín, và trường xuyên tâm nằm trong mặt phẳng vòng không tạo thông lượng qua đĩa phẳng đó. Đối xứng trụ của cấu hình ống dây dài và từ thông dọc trục cho điện trường cảm ứng tiếp tuyến; nên bỏ lập luận Gauss này hoặc thay bằng một suy luận đúng, nêu rõ đối xứng và giả thiết. Lỗi tương tự có trong nguồn, trang in 968, nhưng cần sửa trong bài giảng để không truyền một lập luận sai.

2. **Crop bị cắt và còn chữ tiếng Anh, Hình 29.17.** Ở mép trên `img/young-29/hinh-29-17.png` còn mảnh câu “contacts labeled b.” bị cắt ngang. Đây là phần cuối chú thích hình trên trang in 967, không thuộc hình vẽ. Annotation hiện dịch hai nhãn của sơ đồ nhưng không bao quát mảnh chữ này. Cắt sạch phần chữ thừa hoặc đưa nguyên văn nhãn có bản dịch đầy đủ vào đúng vị trí.

3. **Thiếu điều kiện áp dụng, mục 29.7, dòng 152 của `07-dong-dien-dich-maxwell.md`.** Câu nói có thể suy ra định luật Coulomb từ Gauss và định luật Biot–Savart từ Ampère chưa nêu miền tĩnh điện/từ tĩnh. Bổ sung điều kiện tĩnh điện cho vế Coulomb và dòng điện ổn định cùng giả thiết phù hợp cho vế Biot–Savart để tránh khẳng định quá rộng.

4. **Còn thuật ngữ tiếng Anh trong lời giảng, mục 29.2, dòng 152–155 của `02-dinh-luat-faraday.md`.** Từ “alternator” xuất hiện ba lần chưa được Việt hóa. Có thể dùng “máy phát điện xoay chiều”. Cụm “điện kế galvanometer” ở mục 29.1 và chú thích Hình 29.18 cũng trùng lặp thuật ngữ, nên thống nhất “điện kế” hoặc ghi thuật ngữ Anh một lần trong ngoặc khi giới thiệu.

## Những gì đã xác nhận

- Các phương trình (29.1)–(29.24) đều có mặt, giữ đúng thứ tự và nhìn chung giữ đúng biểu thức, dấu, điều kiện được nêu quanh công thức. Không thấy lỗi số học trong các ví dụ có kết quả số đã tính lại.
- 11 ví dụ và các câu tự kiểm giữ trong mạch lý thuyết. Mỗi câu hỏi tự kiểm có phần trả lời ẩn đặt liền sau câu hỏi. Không phát hiện câu tự kiểm nào bị chuyển sang khu bài tập cuối chương.
- Các annotation đã bao phủ những nhãn tiếng Anh nhìn thấy ở hầu hết crop; Hình 29.17 là ngoại lệ vì phần chú thích bị cắt nói trên. Hình 29.23 không có nhãn văn xuôi tiếng Anh cần dịch. Hình cầu nối 29.28 có bản dịch cho các nhãn chữ và kích thước.
- Các công thức biến đổi dài chủ yếu đã được bẻ dòng bằng `aligned`. Tuy nhiên, yêu cầu không cuộn ngang ở 320 px vẫn cần kiểm trên bản dựng thật, nhất là trong các hộp và tab của trang bài học.

## Phạm vi chưa xác nhận

Đây là rà nội dung nguồn và crop. Chưa chạy build/check_lecture, chưa kiểm tra công thức ở kích thước 320 px, chưa đo độ rộng inline bằng MathJax và chưa xác nhận hành vi thực tế của overlay annotation trên trang đã dựng.
