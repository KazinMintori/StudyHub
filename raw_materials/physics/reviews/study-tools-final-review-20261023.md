# Công cụ học tập và đối chiếu yêu cầu giao diện

Giữ bố cục khung công cụ trong ảnh người dùng chấp nhận. Hẹn giờ và Sổ nháp nằm trong một bảng mở bằng nút Công cụ học tập. Trang chủ không có đồng hồ, sổ nháp hoặc hàng trống dành cho các công cụ này. Bảng bắt đầu đóng trên cả máy tính và điện thoại. Zen được giữ như vị trí trong ảnh đã chấp nhận.

Thời lượng có hai lựa chọn nhanh 25 và 50 phút, đồng thời cho nhập số phút nguyên từ 1 đến 240. Áp dụng thời lượng sẽ đặt lại đồng hồ. Khi đồng hồ đang chạy, người dùng tạm dừng trước khi đổi thời lượng. Giá trị tùy chọn được giữ sau khi tải lại trang. Dữ liệu cũ và ghi chú theo trang được giữ tương thích.

Đối chiếu các yêu cầu còn hiệu lực:

| Yêu cầu | Kết quả |
| --- | --- |
| Khôi phục hình vẽ và giao diện cũ | HeroArt, CourseArt và SpotArt đã gắn lại. Các tệp hình không đổi. |
| Bỏ ba nút dưới mỗi thẻ môn | Đã bỏ. Thẻ là một liên kết đến học phần. |
| Giữ bộ lọc học phần | Tìm kiếm và lọc nhóm môn hoạt động, Vật lý 1 đứng trước Vật lý 2. |
| Bỏ Slides toàn bộ môn | Tab, nội dung trình chiếu và lối tắt đã gỡ. Địa chỉ cũ chuyển đến Notes. |
| Bỏ đánh dấu hoàn thành và tích xanh | Không còn nút hoặc phần tự gắn dấu lên thanh bên. |
| Bỏ chấm trang trí không phù hợp | Đồng hồ không có chấm. Gợi ý phím tắt không dùng chấm ngăn. |
| Proof accordion và Q.E.D | Giữ bộ dựng details.proof, ký hiệu kết thúc ở cuối toàn khối, không thêm trùng. |
| Công thức và scrollbar | Giữ quy tắc toàn cục cho MathJax, MathML phụ trợ và điều khiển. Không đưa thanh cuộn vào ô thời gian tùy chọn. |
| Tra cứu song song | Giữ tìm kiếm không dấu và khung tra cứu có khoảng bố trí riêng khi mở. |
| Lightbox đổi nền cục bộ | Giữ ba chế độ tự động, sáng, tối, không thay giao diện chung. |
| Thanh Pomodoro đỉnh trang | Giữ chiều cao 2 px, không bóng, không gradient, không chặn thao tác. |
| Công cụ trên điện thoại | Chỉ có nút mở, không bày đồng hồ và ô nháp ra trang học phần. |
| Build toàn bộ | Chỉ chạy bằng GitHub Actions. |

Kiểm chứng trước khi push: 148 kiểm thử dự án, 113 kiểm thử tính năng và 39 kiểm thử công cụ đạt. Kiểm tra mã màu và kiến trúc đạt. Kiểm tra khôi phục trang chủ ở năm độ rộng 320–1440 px đạt. Khung công cụ đạt 21 trường hợp trình duyệt, gồm nhập thời gian sai/đúng, tải lại, bắt đầu, tạm dừng, đặt lại, lưu ghi chú riêng từng trang, Escape, tiêu điểm và đóng khi bấm bên ngoài.

Phạm vi kiểm chứng không đồng nghĩa đã xem thủ công từng công thức và từng câu hỏi của toàn bộ website. Bài chủ đề Toán cho AI có công thức cũ tràn đã được ghi thành tác vụ biên tập riêng. Không coi kết quả kiểm tra điều khiển là chứng nhận toàn bộ nội dung môn học.

Đã tham khảo cách gom tiện ích trong [Carbon UI Shell](https://github.com/carbon-design-system/carbon/blob/main/packages/react/src/components/UIShell/README.md). Thiết kế cuối tuân theo ảnh người dùng chấp nhận, không thay hệ hình minh họa của dự án.
