# Rà soát văn bản người học chương 25 và mô-đun tích hợp

## Phạm vi

Đã rà văn bản câu hỏi thảo luận Q25.1–Q25.24 trong `raw_materials/physics/translations/chapter-25/09-cau-hoi-thao-luan.md`, bài 25.1–25.30 trong `10-bai-tap-01-30.md`, bài 25.31–25.58 trong `11-bai-tap-31-58.md`, bảng đáp số trong `14-dap-so.md`, cùng `docs/.vitepress/physics-current-course.mjs` và `physics-current-foundations.mjs`. Đã đọc các báo cáo rà soát theo dải trước đó để nắm kết quả tính độc lập và phạm vi chưa khép lại. Trực tiếp render PDF nguồn ở trang một-based 859–861, tương ứng trang in 839–841, để kiểm tra các dữ kiện có dấu, hướng mạch và đơn vị nhạy cảm.

Đây là rà soát văn bản và đối chiếu nguồn theo phạm vi nêu trên, không phải phép giải độc lập cả 82 bài. Không chạy build hoặc kiểm tra hiển thị trang sau tích hợp.

## Phát hiện

### Trạng thái tích hợp: Đã khép P1

Rà soát lại sau khi tích hợp xác nhận `docs/vat-ly-2/bai-giang/05-dong-dien-dien-tro.md` hiện đặt `lessonStatus: ready` và `hasChapterExercises: true`. Lệnh Node nhập `courseCatalog` cho thấy bài `05-dong-dien-dien-tro` có trạng thái `ready`, số bài 5, 6 chủ đề, 8 slides và `hasChapterExercises: true`. Catalog lấy cấu hình Vật lý 2 qua `physics2Course` trong `physics-courses.mjs`, nên không cần import `currentTopics`/`currentSlides` trực tiếp trong `course-catalog.mjs`. Nội dung Notes hiện dùng các đoạn include từ 15 tệp chương 25. Phát hiện P1 trước tích hợp đã được giải quyết.

### Trạng thái công thức gần đúng: Đã khép P2

Rà soát lại xác nhận `docs/.vitepress/physics-current-foundations.mjs:82` hiện viết `\rho(T)\approx\rho_0[1+\alpha(T-T_0)]`, nhất quán với lời dẫn và cheatsheet. Phát hiện P2 trong bản báo cáo trước đã được xử lý.

## Đối chiếu nguồn và kết quả đã xác nhận

- Bài 25.31: Lời giải chọn dòng 1,41 A theo chiều kim đồng hồ sau khi đảo pin, và ghi `V_ab = −13,7 V` theo đúng quy ước `V_ab = V_a − V_b`. Đây là dấu đúng vì cực dương của pin đảo nằm tại b. Sơ đồ gốc E25.30 được xem trực tiếp trên trang in 839.
- Bài 25.55: Trang in 841 cho dây dài tổng 3,00 m, hai đoạn 1,20 m/1,60 mm và 1,80 m/0,80 mm, dòng 2,5 mA. Bản thảo giữ đúng đơn vị của điện trường và hiệu điện thế. Kết quả kiểm tra trong báo cáo dải 31–58 tương đương 21,4 µV/m, 85,5 µV/m và 0,1796 mV, được làm tròn thành 0,180 mV trong đáp số.
- Bài 25.57: PDF ghi rõ xung kéo dài khoảng 40 µs. Bản thảo đã sửa dữ kiện OCR thành `40 µs` và dùng `4,0×10⁻⁵ s` trong phép tính. Báo cáo dải 31–58 ghi kết quả Python là năng lượng 2,5×10⁷ J và độ tăng nhiệt độ mô hình 79,6 °C.
- Bài 25.67: Đề PDF ghi bán kính 1,10 cm. Bản thảo giữ đúng bán kính. Báo cáo 59–82 đã đối chiếu đáp số phóng to và xác nhận các tiền tố đơn vị đúng là µ: 171 µΩ, 176 µV/m, 54,7 µΩ và 116 µΩ.
- Bài 25.6: Báo cáo rà chéo cũ ghi câu hỏi giá vàng còn bỏ ngỏ. Bản hiện tại đã bổ sung câu trả lời định tính, quy đổi giá tham khảo có ghi ngày truy cập, nêu nguồn tỷ giá khối lượng và nói rõ giá trị chưa gồm công chế tạo. Phát hiện cũ này đã được xử lý trong nội dung hiện tại.
- Ở các phần đã kiểm tra, không thấy các câu tự độc thoại bị cấm trong lời giải, các cụm ghi công thụ động như “theo sách”/“bản dịch của”, hay lỗi viết thường ngay sau dấu hai chấm. Hình thức lời giải thường nêu tóm tắt, hướng đi, phép biến đổi rồi kết luận, đủ để người học lần theo lý do thay vì chỉ nhận đáp số.

## Giới hạn

Các báo cáo `ch25-exercises-01-30.md`, `ch25-exercises-31-58.md`, `ch25-exercises-59-82.md` lưu chi tiết kiểm tra tiểu mục, số học và ảnh mạch theo từng dải. Báo cáo này dùng chúng làm bằng chứng nền và chỉ trực tiếp đối chiếu lại các điểm số liệu được nêu ở trên. Chưa rà độc lập từng phép tính của toàn bộ 82 bài, chưa kiểm tra crop ảnh/nhãn ở kích thước hiển thị, và chưa xác nhận build hay trang Notes sau khi tích hợp.
