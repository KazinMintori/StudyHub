# Rà định dạng Cheatsheet và đường dẫn bài học

Ngày rà: 26/10/2026. Phạm vi: Dữ liệu và phần hiển thị của 44 Cheatsheet thuộc Vật lý đại cương 1 và 2, cùng lỗi tra bài khi metadata chưa sẵn sàng. Đây là một phần của lượt rà cuối, chưa chứng nhận đầy đủ nội dung hai học phần.

## Những lỗi đã sửa

Quét 2936 đoạn toán trong 44 Cheatsheet tìm được 13 công thức ngắt dòng giữa phép cộng, trừ hoặc nhân ở tám module Vật lý 2. Đã đặt lại các biểu thức theo dòng hoàn chỉnh hoặc mở tường minh từng định nghĩa thành phần. Tổng thế năng ba điện tích được viết qua ba năng lượng cặp, rồi cộng chúng lại. Định luật Ampère–Maxwell nêu rõ dòng điện dịch trước khi cộng với dòng dẫn trên cùng mặt.

Mọi số hạng, hằng số, dấu và điều kiện được giữ. Các chú giải bổ sung giải thích ký hiệu đã dùng, không thêm bài tập hoặc suy diễn mới vào Cheatsheet. Kiểm dữ liệu trước/sau xác nhận những trường khác và mọi export không liên quan giữ nguyên. 32 phép đối chiếu độc lập kiểm phép nhóm lại điện trường đĩa, năng lượng cặp và kernel Biot–Savart, cùng tổng dòng điện trong định luật Ampère–Maxwell.

Một cảnh báo là hệ bất đẳng thức bắt đầu bằng số âm, không phải dòng tiếp của phép trừ, nên được giữ nguyên. Năm cảnh báo còn lại chỉ vượt nhẹ ngưỡng đo bảo thủ 28 ex. Biểu thức đầy đủ được giữ trên một dòng và kiểm trực tiếp thay vì bẻ ở toán tử.

Ở màn hình hẹp tới 360px, giảm khoảng đệm của thẻ và khung công thức bằng token khoảng cách hiện có. Không giảm cỡ chữ toán, cắt biểu thức hoặc ẩn phần tràn. Lượt kiểm sau đạt 220 trường hợp trên năm chiều rộng 320, 360, 375, 768 và 1440 px cho toàn bộ 44 Cheatsheet.

## Phạm vi bằng chứng giao diện

Phiên mở route VitePress chứa cả nhiều lời giải đã chạm giới hạn heap 1,5GB và dừng. Không tăng giới hạn để tiếp tục biên dịch trang nặng trên máy người dùng. Lượt thay thế render đúng template LecturePanels.vue, dùng cùng dịch vụ MathText, CSS production và khung VPDoc, chỉ tách khỏi việc nạp Notes và bài tập. Harness này có giới hạn heap 768MB và không chạy build website.

Kết quả 220 trường hợp xác nhận bố cục component trong phạm vi ấy. Nó chưa xác nhận routing, tải dữ liệu lười hoặc bản web đã xuất bản. Sau build GitHub, các route production cần được kiểm riêng.

## Lỗi runtime tra bài

Khi cả mã môn và slug bài còn thiếu, hai giá trị undefined có thể so bằng nhau ở nhánh tra trang ôn tập. Nhánh ấy sau đó đọc course.review dù course chưa tồn tại. Đã thêm điều kiện trả về an toàn trước nhánh dự phòng. Hai kiểm thử tái hiện metadata thiếu và kiểm các route bài giảng/ôn tập hợp lệ đều đạt. Chúng được đưa vào lệnh kiểm thử tính năng để tiếp tục chạy trên GitHub.

## Công việc còn lại

Kiểm cấu trúc đạt 133 bài và 354 trang chủ đề, không lỗi hoặc cảnh báo. Bộ công cụ bài giảng đạt 39/39, kiểm thử tính năng đạt 139/139, kiểm chia gói đạt 8/8 và bộ toán đạt 31/31. Kiểm token màu và ranh giới kiến trúc đều đạt. Không chạy build toàn cục tại máy người dùng.

Sau commit và build GitHub phải kiểm route thực của cả 44 Cheatsheet. Việc đối chiếu học thuật với từng chương, hoàn thiện bốn chương Vật lý 1, báo cáo tổng kết và dọn dẹp chưa được thay thế bằng kết quả định dạng này.
