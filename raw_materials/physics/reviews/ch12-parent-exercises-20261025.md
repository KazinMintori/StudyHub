# Nghiệm thu bài tập chương 12

Ngày rà: 25/10/2026. Phạm vi: PDF406–414, trang in386–394. Lý thuyếtPDF386–405 đã được rà và xuất bản riêng trước đó.

## Phạm vi đã hoàn tất

Đủ92bài12.1–12.92,30câuQ12.1–Q12.30,12bàiVP12.4.1–4/VP12.5.1–4/VP12.9.1–4 vàmột bài cầu nối. Mỗi đơn vị có một lời giải đóng sẵn với tóm tắt, hướng đi giải thích lựa chọn công thức/tính chất và lời giải đủ phần hỏi. Bảy bước gợi ý gốc của bài tháo cạn bồn được giữ đầy đủ.

135đơn vị được chia thành24nhóm để tải theo nhu cầu. Đoạn đọc về áp suất khi voi dùng vòi thở đi cùng nhóm chứa các câu liên quan. Không đưa các bài cuối chương vàoNoteshoặcCheatsheet.

## Nguồn và tính toán

Các bản ghi từng bài và phần hỏi nằm trongch12-exercises-source-unit-ledger.json.46bài đầu được đối chiếu trực tiếp vớiPDF408–410,20bài tiếp theo vớiPDF410–411,26bài còn lại vớiPDF410/412–414. Nhóm12VP/30Q/cầu nối còn có một lượt rà độc lập riêng so với tác giả, bao gồmPDF406–408/414.

Bốn chương trìnhPython có thể chạy lại kiểm46bài đầu,20bài giữa,26bài cuối và43đơn vị hướng dẫn/thảo luận/cầu nối. Các câu định tính được kiểm bằng lập luận và trường hợp tham số, không gọi bản ghi định tính là chứng minh số học. Lượt độc lập26bài có110kiểm tra,59so sánh vô hướng với mã tính của tác giả, dùng thêmODE, tích phân số, tìm nghiệm và hồi quy bằng phân số chính xác. Lượt độc lập phần hướng dẫn kiểm12bộ tham số hữu tỷ của bồn có tiết diện hữu hạn và3trường hợpODE với41thời điểm mỗi trường hợp.

## Những sai lệch đã sửa

- 12.49: Áp suất đầu đúng là1,80×10⁴Pa. Đã sửa đề, mã tính và kết quả thành2,03×10⁴Pa.
- 12.50: Đường kính thứ hai gấp đôi, nên tiết diện gấp bốn và tốc độ còn0,750m/s. Áp suất cuối khoảng1,62×10⁵Pa. Đã sửa cả nguyên nhân tăng áp trong lời giải.
- 12.47/12.48/12.52: Khôi phục mức• và bối cảnh vòi chữa cháy nối ống chính của12.47.
- 12.72: Bỏ dữ kiện giao việc sai. Cốc1,00kg, chất lỏng1,80kg, cân treoDchỉ3,50kg, cân đỡEchỉ7,50kg. Khi kéo khối hẳn ra, hai cân lần lượt8,20kg và2,80kg.
- 12.38: Giữ lưu lượng0,750m³/s đúng đơn vị nguồn, dù tốc độ suy ra rất lớn. Không tự đổi thành lít mỗi giây để làm đáp số dễ nhìn.
- 12.54: Phân biệt việc giữ mô hình biến dạng thể tích tuyến tính rồi lấy nghịch đảo với khai triển khối lượng riêng hoàn toàn đến bậc nhất. Hai mức xấp xỉ được nói rõ, không gán cho hai bộ số liệu khác nhau.
- 12.64: Phân biệt tổng độ lớn tải hướng ra ngoài trên thành trụ với hợp lực vector lên toàn thành. Giữ đầy đủ dữ kiện và bối cảnh Boston1919.
- Q12.3: Hai số đều biểu diễn lực, có vai trò khác nhau. Bỏ cách gọi hai loại đại lượng khác nhau.
- Bốn phép thay sốVP: Gom cộng/trừ trong ngoặc trước đơn vị.
- VP12.9.4: Giữ mẫu1−β², các điều kiện bồn rộng hơn ống, dấu biểu thức dưới căn và nhánh tốc độ ra không âm.
- Q12.26: Giải thích áp suất cục bộ trên bóng khi tia khí bị uốn quanh bóng, không suy diễn mọi tia khí tự do đều có áp suất thấp hơn khí quyển.

## Hình ảnh và đồ thị

16hình gốc cuối chương được giữ trọn, kiểm trùng điểm ảnh với đúng vùngPDFtại tỉ lệ2,5 và xem toàn bộ hình. Biên cắtP12.57loại văn xuôi lân cận nhưng giữ đủ2,00m/4,00m. Hình12.32giữ đủ kích thước và nhãn. P12.81giữ cả sàn. Có22cụm chú thích Việt–Anh, mỗi cụm một lần trong hình tương ứng. Năm hình lý thuyết12.7/12.8/12.10/12.25/12.26được dùng lại.

Ba đồ thị lời giải mới đáp ứng yêu cầu gốc: Độ cao nước theo thời gian cho bài cầu nối chỉ ở0≤t≤T, đồ thị tám nguyên tố ở12.85 và đường khớp năm số đoR²ở12.87. Chữ trong hai đồ thị của tác giả ít nhất14px, đã xem trực quan. Tám khối lượng mol lấy đúng phụ lụcDPDF1550. Khối lượngquarter5,67gđược kiểm ởU.S.Mint. Các hệ số hồi quy12.87được kiểm độc lập bằng đại số hữu tỷ vànumpy. Các giá trị đọc từ đồ thị12.86được nêu xấp xỉ.

## Kiểm tra giao diện

420công thức hiển thị và1356nội dòng đạt kiểm cú pháp/độ rộng28ex/27ex.120trường hợp trình duyệt kiểm toàn24nhóm/135đơn vị ở320,360,375,768,1440pxđều đạt. Mọi lời giải đều đóng lúc tải, mở đủ nội dung khi kiểm. Không có lỗi JavaScript, ảnh hỏng, yêu cầu mạng thất bại, tràn trang, thanh cuộn công thức hoặc MathMLhỗ trợ bị hiện.

Kiểm toàn dự án:133bài/321trang chủ đề không lỗi hoặc cảnh báo cấu trúc.39kiểm tra skill đạt.21kiểm tra nhóm bài tập, dữ liệu ảnh, máy chủ phát triển và biên dịch công thức đạt. Lượtverify:math31kiểm tra/1424trang đã đạt sau tích hợp lý thuyết. Các bài tập tải động được kiểm bằng bộ render/MathJaxvà trình duyệt riêng ở trên.

## Phạm vi nghiệm thu

Chương12đủ nội dung lý thuyết, hình, ví dụ/câu tự kiểm, bài tập vàCheatsheetđã rà. Buildvà triển khai toàn bộ chỉ chạy trênGitHubActions. Cần kiểm commit xuất bản và ảnh trên bản web sau khi triển khai, không coi việc push hoặc buildxanh là bằng chứng tự đủ cho nội dung công khai.
