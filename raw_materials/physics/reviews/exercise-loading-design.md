# Hướng giảm tải lời giải dài

Trạng thái: Khảo sát, chưa triển khai thay đổi kiến trúc tải lời giải.

## Bằng chứng hiện có

Trang Mạch điện một chiều được đo trong qa/physics/chapter38/public-loading-baseline.json có HTML giải nén khoảng 12,58 MB, thân truyền gzip khoảng 1,26 MB, JavaScript lean truyền khi mở trực tiếp khoảng 21 KB, 2179 khối toán và 94 thẻ ảnh. Không được cộng HTML và bundle đầy đủ để kết luận mọi lần mở trực tiếp đều tải hơn 24 MB.

Ảnh đã có chính sách tải ngay ảnh đầu, tải chậm ảnh sau và giải mã bất đồng bộ. Bốn font preload khớp các font thật mà CSS yêu cầu. Hai thay đổi này đã được kiểm tra trên bản xuất GitHub ở commit e666219.

## Điểm cần xử lý tiếp

Nội dung Bài tập của các chương lớn vẫn nằm trong cùng Markdown với Notes. CSS đổi tab không tách phần giải chi tiết khỏi DOM ban đầu. Bộ dựng toán đã dùng một HTML binding cho từng công thức, giảm số node Vue, nhưng vẫn giữ cây SVG trong HTML.

Hướng phù hợp để thử là giữ toàn bộ đề bài và nút mở lời giải trong trang, đồng thời tải phần thân lời giải sau khi người học mở hộp. Chia các lời giải thành nhóm nhỏ giúp tránh tạo quá nhiều chunk và tránh tải toàn bộ đáp án chỉ vì mở một bài.

## Yêu cầu đối với một bản thử cụ thể

- Giữ nguyên mọi đề, hình, lời giải, công thức, ghi chú và thứ tự. Người đọc vẫn mở lời giải ngay bên dưới đề.
- Dùng component bất đồng bộ thay vì đưa HTML chưa render vào một chuỗi rồi làm mất xử lý Vue, MathJax, hình ảnh và liên kết Wiki.
- Giữ các thành phần Vue nằm trong lời giải hoạt động được, hỗ trợ phím và thông báo lỗi tải có thể thử lại.
- Chỉ bật trong bản thử có giới hạn trước khi áp dụng toàn bộ bài giảng.
- So trước/sau bằng HTML và lượng dữ liệu thực truyền trên bản xuất GitHub. Đo DOM trước/sau khi mở lời giải, thời gian tương tác và các công thức ở 320–375 px.
- Không chuyển đổi PNG nguồn sang dạng mất dữ liệu. Không bỏ nội dung để giảm kích thước.

## Phạm vi kiểm tra

Cần kiểm đường mở trực tiếp, chuyển trang trong ứng dụng, mở qua liên kết neo, bật/tắt tab, mở nhiều lời giải, quay lại trang và in. Kiểm DOM không thay thế việc đọc đối chiếu nội dung. Build toàn cục vẫn chỉ chạy trên GitHub Actions.
