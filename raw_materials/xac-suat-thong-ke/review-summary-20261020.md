# Kết quả rà soát xác suất thống kê ngày 20/10/2026

Môn học có 27 bài gốc và 18 chuyên đề trong mục “Bổ trợ xác suất thống kê cổ điển”. Phần bổ trợ có 83 bài tập có lời giải gập. Toàn môn có 153 thẻ ôn tập, tra cứu công thức từ cùng nguồn thẻ và kiến thức nền liên kết Wiki. Đã bổ sung 17 mục Wiki về xác suất và suy luận thống kê.

## Nội dung và giao diện

Đã sửa cấu trúc HTML bị đọc thành mã, dấu phân cách toán, công thức dài, các hộp và khoảng cách giữa thẻ. Đã sửa giả thiết về phương sai và độc lập, xấp xỉ chuẩn trên lưới rời rạc, diễn giải p-value và ngẫu nhiên hóa, cùng tiêu chí chi phí khi so sánh ngưỡng phân loại. Những phép tính thay đổi được kiểm lại bằng Python.

Bộ hình gồm 51 SVG xác suất và thống kê cùng ba SVG Bayes. Chữ Be Vietnam Pro được nhúng theo giấy phép OFL. Chú giải có khoảng trống riêng và đường cong được tính từ mô hình. Bộ sinh hình được giữ trong scripts để tái tạo. Các bản hình thử nghiệm không còn được tham chiếu và được lưu riêng ngoài repository.

## Bằng chứng kiểm tra

- 45 bài có trong catalog và chỉ mục nội dung, kiểm tra cấu trúc đạt 0 lỗi và 0 cảnh báo.
- 1.332 trường hợp trình duyệt hợp nhất, gồm Notes, bài tập mở lời giải, toàn bộ 153 thẻ, kiến thức nền và tra cứu, tại 360/375/768/1280 px. Không phát hiện tràn trang/công thức, lỗi TeX, box thô, HTML bị hiểu thành mã, ảnh hỏng hoặc lỗi runtime trong các trường hợp đã kiểm.
- 54 SVG được kiểm tra hộp bao và đường vẽ tại chiều rộng 640 px, đạt 0 chữ bị cắt, 0 cặp chữ chồng nhau và 0 nhãn bị đường vẽ xuyên qua. Đã xem sáu contact sheet. Tỷ lệ SVG giữ nguyên khi co giãn.
- Trang môn và lộ trình bổ trợ được kiểm ở bốn bề rộng. Đủ BT01–BT18, liên kết đúng, sơ đồ Mermaid hiển thị. Cột số thứ tự có bề rộng cố định để tiêu đề thẳng hàng.
- Các bộ kiểm số cho bài gốc, tám bài xác suất, chín bài thống kê, Bayes và Wiki đều đạt. Kiểm kê MathJax toàn bộ 45 Notes đạt 0 lỗi cú pháp, 0 công thức vượt ngưỡng 34ex hiển thị/38ex nội dòng, 0 dấu phân cách sai và 0 ngắt dòng tại phép cộng/trừ.
- 39 kiểm thử công cụ bài giảng, 120 kiểm thử repository và 108 kiểm thử tính năng đều đạt. Kiểm tra kiến trúc, mô hình nội dung, hộp bài giảng, thư viện nhúng và design token đều đạt.

Các kiểm tra hình học và trình duyệt là bằng chứng cho những trường hợp đã chạy, không phải chứng minh mọi cách tổ hợp nội dung trong tương lai. Build toàn cục và deploy do GitHub Actions thực hiện, không chạy trên máy người dùng.

## Đối chiếu chương trình

Lộ trình trong docs/xac-suat-thong-ke/bo-tro-co-dien.md liên kết từng nhóm kiến thức với các bài gốc phù hợp. Hai bảng phạm vi chuyên môn nằm trong classical-probability-coverage.md và classical-statistics-coverage.md. Phần Bayes bổ sung tiên nghiệm, hậu nghiệm, khoảng xác suất và phân phối dự đoán. Đối chiếu dùng chương trình đại học của MIT 18.05, Penn State STAT 414/415 và NIST, không gọi phạm vi này là toàn bộ mọi chuyên ngành thống kê.
