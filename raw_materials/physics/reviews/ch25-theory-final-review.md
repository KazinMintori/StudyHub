# Rà soát độc lập cuối phần lý thuyết chương 25

Ngày rà: 12-10-2026.

## Phạm vi và kết luận

Đã đối chiếu các tệp raw `00-mo-dau.md`, mục 25.1–25.6, `07-tom-tat.md`, `08-luyen-tap-huong-dan.md`, `09-cau-hoi-thao-luan.md` với PDF nguồn và các bản trích chữ tương ứng. Phạm vi là trang in 812–838, tương ứng PDF một-based 832–858, chỉ số PyMuPDF zero-based 831–857.

Không thấy sai định luật, chứng minh bị đảo chiều hay số liệu mẫu sai trong phần lý thuyết đã đối chiếu. Các ví dụ, cảnh báo, ứng dụng, bảng và câu tự kiểm chính đều có mặt. Các phát hiện P2 của vòng trước đã được xử lý và xác nhận lại trong lượt cập nhật này. Phạm vi cập nhật trực tiếp là bốn tệp raw được giao cùng các sửa liên quan trong module đang chuẩn bị tích hợp. Chưa nghiệm thu build hoặc responsive layout.

| Phần | Trang in / PDF | Đối chiếu nguồn |
| --- | --- | --- |
| Mở đầu 00 | 812 / 832 | Giữ câu hỏi dòng ra khỏi bóng đèn, truyền năng lượng, các ứng dụng âm thanh, sưởi, máy tính và phân phối điện, mục tiêu chương và kiến thức cần ôn. Không thấy thêm khẳng định lịch sử ngoài nguồn. |
| 25.1 Dòng điện | 813–816 / 833–836 | Đủ chuyển động ngẫu nhiên và trôi, thiết lập nhanh điện trường, dòng quy ước, dấu hạt tải, dòng vô hướng, đơn vị ampere, dẫn xuất dòng/mật độ dòng, nhiều hạt tải, trạng thái ổn định, DC/AC, Ví dụ 25.1 và câu hỏi thay dây có đường kính gấp đôi. |
| 25.2 Điện trở suất | 816–819 / 836–839 | Đủ miền áp dụng Ohm, điện trở suất/độ dẫn và đơn vị, hai bảng vật liệu và hệ số nhiệt, tương quan dẫn điện–dẫn nhiệt, bảng mạch, chất bán dẫn, phép tương tự bộ lọc, nhiệt điện trở, siêu dẫn và ứng dụng myelin. Các mốc lịch sử về siêu dẫn khớp nguồn. Số liệu nhiệt độ tới hạn cao nhất được ghi rõ là mốc nguồn nêu năm 2018. Câu tự kiểm ở cuối mục. |
| 25.3 Điện trở | 819–823 / 839–843 | Đủ suy diễn điện trở từ trường và mật độ dòng, giả thiết dây đồng nhất/tiết diện đều, định nghĩa $R=V/I$, giới hạn định luật Ohm, mã màu/dung sai, nhiệt độ, đồ thị điôt và điện trở Ohm, Ví dụ 25.2–25.3, câu tự kiểm cuối mục. |
| 25.4 Suất điện động và mạch điện | 823–828 / 843–848 | Đủ giải thích dòng thoáng qua trong vật dẫn cô lập, nguồn và máy bơm, suất điện động cùng các cơ chế hóa học/cơ/từ/nhiệt, lực không tĩnh điện, mạch lý tưởng/thực, điện trở trong, nạp/phóng, ký hiệu và dụng cụ đo, ứng dụng cá đuối điện, Ví dụ 25.4–25.7, ngắn mạch, biến thiên điện thế quanh vòng và câu tự kiểm cuối mục. |
| 25.5 Năng lượng và công suất | 828–832 / 848–852 | Đủ quy ước dấu phần tử, công suất điện trở, công suất nguồn khi phát và khi nạp, tổn hao điện trở trong, Ví dụ 25.8–25.10, chiến lược cân bằng công suất và câu tự kiểm. |
| 25.6 Mô hình dẫn điện trong kim loại | 832–835 / 852–855 | Đủ mô hình cổ điển có giới hạn, chuyển động ngẫu nhiên, thời gian tự do trung bình, dẫn xuất $v_d$ và $\rho$, giả thiết $n$ và $\tau$ không đổi theo trường, diễn biến nhiệt ở kim loại/bán dẫn, đánh thủng điện môi, Ví dụ 25.11 và câu tự kiểm cuối mục. |
| 07 Tóm tắt | 835 / 855 | Các định nghĩa và công thức trọng tâm đều có, gồm điều kiện của điện trở hình học và nguồn thực. |
| 08 Luyện tập hướng dẫn | 836 / 856 | Giữ đủ 12 bài VP25.3.1–25.3.4, VP25.5.1–25.5.4, VP25.9.1–25.9.4 và bài nối cầu dây Nichrome. Các kết quả số đã được đối chiếu bằng tính toán độc lập trước đó. |
| 09 Câu hỏi thảo luận | 837–838 / 857–858 | Đủ Q25.1–Q25.24, cả hình Q25.12, Q25.14–Q25.16 và lời giải cho từng câu. Đã xem trực tiếp sơ đồ đồ thị, bóng đèn và dụng cụ đo. |

## Phát hiện đã xử lý và xác nhận

### P2. Mười một khối công thức vượt ngưỡng 30ex (đã xử lý)

Danh sách dưới đây ghi bề rộng ở lần audit trước khi chỉnh sửa. Các công thức đã được ngắt dòng hoặc viết lại theo các bước tương đương, không thu nhỏ chữ và không cắt biểu thức. Audit cuối bằng MarkdownItMathJax trên bốn tệp được giao (`01`, `03`, `05`, `08`) đã render 65 khối display và 212 công thức inline. Không còn khối display vượt 30ex, inline vượt 38ex hoặc lỗi TeX. Bề rộng lớn nhất lần lượt là 29,424ex và 27,791ex.

| Vị trí lúc audit đầu | Bề rộng ban đầu | Nội dung |
| --- | ---: | --- |
| [01-dong-dien.md:182](../translations/chapter-25/01-dong-dien.md:182) | 31,984ex | Tốc độ trôi trong Ví dụ 25.1 |
| [03-dien-tro.md:139](../translations/chapter-25/03-dien-tro.md:139) | 30,719ex | $J$ và $E$ trong Ví dụ 25.2 |
| [03-dien-tro.md:163](../translations/chapter-25/03-dien-tro.md:163) | 30,056ex | Điện trở dây trong Ví dụ 25.2 |
| [03-dien-tro.md:199](../translations/chapter-25/03-dien-tro.md:199) | 32,014ex | $R(0)$ trong Ví dụ 25.3 |
| [03-dien-tro.md:211](../translations/chapter-25/03-dien-tro.md:211) | 32,516ex | $R(100)$ trong Ví dụ 25.3 |
| [05-nang-luong-cong-suat.md:122](../translations/chapter-25/05-nang-luong-cong-suat.md:122) | 30,002ex | Tỏa nhiệt trong điện trở trong ở Ví dụ 25.8 |
| [05-nang-luong-cong-suat.md:152](../translations/chapter-25/05-nang-luong-cong-suat.md:152) | 32,332ex | Dòng điện trong Ví dụ 25.9 |
| [05-nang-luong-cong-suat.md:160](../translations/chapter-25/05-nang-luong-cong-suat.md:160) | 32,172ex | Điện áp tải trong Ví dụ 25.9 |
| [08-luyen-tap-huong-dan.md:241](../translations/chapter-25/08-luyen-tap-huong-dan.md:241) | 30,755ex | Công suất pin VP25.9.2 |
| [08-luyen-tap-huong-dan.md:264](../translations/chapter-25/08-luyen-tap-huong-dan.md:264) | 30,878ex | Điện áp và công suất VP25.9.3 |
| [08-luyen-tap-huong-dan.md:299](../translations/chapter-25/08-luyen-tap-huong-dan.md:299) | 33,786ex | So sánh công suất VP25.9.4 |

Các vị trí hiện tại đã đổi do ngắt dòng. Mười hai bài VP25.3.1–VP25.9.4 vẫn có đủ 12 nhãn bài tập, mỗi nhãn xuất hiện ở đề và lời giải. Cả 24 nhãn phương trình `25.1`–`25.24` còn nguyên, tăng tuần tự và không trùng lặp.

### P2. Phép tương tự ống nước thiếu hai điều kiện (đã xử lý)

Tại [03-dien-tro.md:58](../translations/chapter-25/03-dien-tro.md:58), phần giải thích hiện có ống dài và hẹp cản dòng mạnh hơn, việc nhồi bông hoặc cát làm tăng sức cản, và giới hạn rằng lưu lượng nước thường không tỉ lệ với tiết diện như dòng trong dây đều. Nội dung này giữ rõ phạm vi của phép tương tự.

### P2. Nối hệ số nhiệt điện trở với Bảng 25.2 chưa tường minh (đã xử lý)

Tại [03-dien-tro.md:112](../translations/chapter-25/03-dien-tro.md:112), văn bản nay nối trực tiếp $R=\rho L/A$ với giả thiết $L$ và $A$ gần như không đổi, rồi xác định hệ số nhiệt của điện trở bằng hệ số nhiệt điện trở suất trong Bảng 25.2.

### P2. Ký hiệu năng lượng có thể bị hiểu là thế năng điện (đã xử lý)

Trong [physics-current-course.mjs](../../../docs/.vitepress/physics-current-course.mjs), công thức đã dùng $W_{\mathrm{in}}=P\Delta t$ và mô tả đây là năng lượng điện phần tử nhận được. Ký hiệu này không còn lẫn với thế năng điện $U$.

### P2. Công thức nhiệt độ tuyến tính hiển thị như đẳng thức chính xác (đã xử lý)

Trong [physics-current-course.mjs](../../../docs/.vitepress/physics-current-course.mjs), cả quan hệ $\rho(T)$ lẫn $R(T)$ đều dùng dấu $\approx$, phù hợp với giả thiết gần đúng tuyến tính trong khoảng nhiệt độ thích hợp.

### P2. Quy ước dấu công suất nguồn (đã xử lý)

Tại [05-nang-luong-cong-suat.md:60](../translations/chapter-25/05-nang-luong-cong-suat.md:60), văn bản nói rõ $I$ trong Eq. 25.19 là độ lớn dòng đi ra cực dương và phân biệt quy ước công suất nguồn với quy ước dòng đi vào đầu a.

## Modules và phạm vi kiểm tra

`physics-current-course.mjs` có sáu chủ đề và tám slide. `physics-current-foundations.mjs` có định nghĩa, Wiki details và kết nối liên ngành. Hai module import được; các đích trong `currentWikiConnections` tồn tại khi ghép với bộ khái niệm chung Vật lý. Công thức mới trong module không vượt ngưỡng 30ex/38ex. Cheatsheet hiện được import từ `docs/.vitepress/cheatsheets.mjs`. Tại thời điểm rà, `currentTopics` và `currentSlides` chưa được tiêu thụ bởi `course-catalog.mjs`. Root đã nêu việc tích hợp sẽ thực hiện sau khi khóa nội dung và crop ảnh, nên đây là bước chờ chứ chưa được xem là lỗi module.

Một lỗi OCR ở bài 25.57 đã được phát hiện ngoài phần lý thuyết. Ảnh PDF phóng to xác nhận thời lượng sét là $40\,\mathrm{\mu s}$, không phải 40 ms. Bản raw bài tập, verifier và báo cáo bài tập đã được cập nhật. Python tính $U=2{,}5\times10^7$ J, $\Delta T=79{,}6^\circ\mathrm C$ và nhiệt độ mô hình từ 37 °C khoảng 117 °C. Nước bắt đầu sôi gần 100 °C trước đó; hậu quả thực tế không thể suy ra bằng mô hình nhiệt toàn khối.

Lượt review-only trên chưa kiểm tra trang tích hợp. Root đã hoàn tất lượt tích hợp riêng ngày 12-10-2026: Catalog có sáu chủ đề và tám Slides, 53 ảnh nguồn cùng hai đồ thị lời giải được kiểm tra đường dẫn và chú giải. Build cuối `qa/physics/release-verified` exit 0, có 76 lượt kiểm tra chương ở 320, 360, 375, 1440 px, không tràn công thức hoặc lỗi JavaScript. Các lượt bổ trợ có 46 lần chuyển kích thước và 78 lượt Wiki. Phép tính vận tốc trôi 25.2 đã sửa đơn vị $neA$ thành C/m và thêm kiểm tra thứ nguyên riêng. Kết quả bổ trợ và giới hạn phạm vi được ghi trong `chapter-25-review.json`, không thay thế việc đối chiếu từng bài của các báo cáo nguồn.
