# Phần còn lại của Vật lý đại cương 1

Phạm vi mới: Chương 1, 3–8 và 12–16, tức 12 chương. Giữ nguyên các chương 2, 9–11 và 17–20 đã hoàn thiện. Chương 1 có bản thảo cũ và cần rà nguồn, hình cùng lời giải chi tiết. Các chương mới chỉ được đặt trạng thái hoàn tất sau đối chiếu nguồn, kiểm chứng phép tính và xem trên trình duyệt.

Đã chuẩn bị 24 tác vụ riêng cho lý thuyết và bài tập, mỗi tác vụ có danh sách tệp được sửa, worktree riêng và bản giao việc đã commit. Antigravity không được sửa cấu hình chung, build toàn bộ, commit, push hoặc deploy. Thông tin job và ảnh kiểm tra tạm được lưu dưới qa/physics1-remaining, không đưa lên trang học.

Các yêu cầu được giữ: Tiếng Việt đầy đủ, đúng giả thiết và từng phần đề bài, hình trích nguyên dạng với chú thích Việt và mỗi nhãn Anh được giải thích một lần, ví dụ/câu tự kiểm trong Notes, bài cuối chương trong Bài tập, lời giải gập có Tóm tắt đề bài, Hướng đi và lập luận chi tiết. Cheatsheet chỉ có định nghĩa, tính chất, công thức cùng điều kiện áp dụng. Không khôi phục Slides hoặc thay giao diện đã được người dùng chấp nhận.

Parent đã bổ sung 20 mục Wiki về lực, năng lượng, khối tâm, chất lưu, hấp dẫn và sóng. Kiểm tra tích hợp toàn kho hiện đạt 0 lỗi và 0 cảnh báo. Các mục mới qua kiểm tra độ rộng toán, rà văn phong và các phép thử độc lập bằng Python. 39 kiểm thử công cụ đạt. Những kết quả này không chứng nhận bản dịch của 12 chương đã hoàn tất.

Bộ tích hợp mới yêu cầu bằng chứng rà nguồn, phép tính, trình duyệt và hash tệp được nghiệm thu trước khi cho phép đặt ready. Bộ kiểm kê cấu trúc riêng kiểm tra mục, ví dụ, ID bài tập, từng khung lời giải đóng và hình còn tồn tại. Kiểm kê máy không thay thế đối chiếu nội dung nguồn.

Lượt tiếp nối: Cầu nối mất trạng thái các job sau khi nạp lại. Parent đã kiểm tra 24 worktree có HEAD không đổi, không sửa vượt tệp được giao và không còn tiến trình worker. Đã giữ mọi bản thảo, tiếp nối chương 1 và 3 bằng lượt gọi thứ hai, không đánh dấu các job mất trạng thái là thành công. Các chương sau còn trong danh sách cần tiếp nối.

Chương 3 đã có một phần lý thuyết cùng Guided Practice, Discussion và bài cầu nối. Parent đối chiếu 17 hình bài tập bằng pixel với vùng PDF, xem ảnh tổng hợp và ghi nhận một vùng cắt cần bỏ dòng văn thừa. Đã tính độc lập 13 bài Guided Practice cùng ví dụ xe tự hành. Những phép tính này còn cần đối chiếu bản cuối trước nghiệm thu. Chưa tích hợp hoặc xuất bản chương còn dở.

Lượt tiếp theo: Đã đưa lại các tác vụ chương 4–8 và 12–16 vào hàng đợi với cùng phạm vi và số lượt gọi được ghi lại. Chương 1 và 3 vẫn đang chạy, chưa nghiệm thu. Parent tính độc lập thêm các bài 3.3–3.17 bằng dữ kiện đề gốc. Kiểm tra bản nháp Guided Practice, Discussion và bài cầu nối chương 3 phát hiện 76 công thức cần rà độ rộng hoặc cú pháp. Kết quả này thuộc bản dở, được giữ làm danh sách sửa, không phải chứng nhận hiển thị hoàn tất.

Parent tiếp tục tính các bài 3.18–3.45, giữ riêng các bài yêu cầu ước lượng bằng công thức theo tham số giả thiết. Đã ghi rõ điều kiện tầm xa cùng độ cao đầu/cuối, mốc hướng vận tốc tương đối và trường hợp vận tốc bằng không không có hướng xác định. Các kết quả là bằng chứng tính toán độc lập, chưa thay thế bước đọc lời giải bản cuối. Các worker chương 1 và 3 vẫn hoạt động, các chương sau còn chờ lượt. Toàn bộ môn chưa hoàn tất và chưa có bản dịch dở nào được đẩy lên main.
