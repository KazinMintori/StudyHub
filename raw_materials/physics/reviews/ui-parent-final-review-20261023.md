# Rà soát giao diện ngày23/10/2026

Yêu cầu đã áp dụng cho giao diện chung của toàn bộ môn học:

- Gỡ tabSlides, khung trình chiếu, lối tắtSlides trên thẻ môn và xử lý phím mũi tên của khung đó. Đường dẫn cũ#slides chuyển vềNotes. Dữ liệu công thức cũ còn dùng để tạoCheatsheet không bị xóa.
- Thẻ môn làarticle với liên kết tiêu đề và các liên kết truy cập nhanh độc lập. Không còn nút lồng trong một liên kết lớn. Các lối tắt còn lại làBài học, Cheatsheet vàBài tập nếu môn có nội dung tương ứng. Số bài giữ trên một dòng.
- Bỏ hình trang trí ở thẻ môn, đầu môn và đầu bài, emoji trong các nút, chấm cạnh đồng hồ, chấm ngăn cách trong gợi ý phím tắt. Các danh sách học thuật và hình minh họa thật trong bài được giữ.
- Gỡ nút đánh dấu hoàn thành và cơ chế thêm tích xanh lênsidebar. Giữ dữ liệu cũ và ghi chú trong trình duyệt.
- Tab bài giảng chia hàng phù hợp, trên màn hình nhỏ dùng hai cột. Cụm đồng hồ và ghi chú có hàng riêng trên điện thoại, không chèn vào tiêu đề hoặc nútmenu. Khung tiếp tục học xếp nội dung và nút thành hàng riêng để tránh ép chữ thành cột hẹp.
- Ẩn thanh cuộn và mũi tên cuộn hệ điều hành trên toàn bộ giao diện, giữ khả năng cuộn bằng bàn phím, con lăn và cảm ứng. Các nút và công thức không được tạo vùng cuộn hoặc cắt nội dung.
- Chứng minh được nhận diện thànhdetails.proof thực sự trong bộ dựngMarkdown, giữ trạng thái gập ban đầu. Ký hiệuQ.E.D là phần cuối của toàn khối mở, không gắn vào phần tử con cuối hoặc tiêu đề. Không thêm trùng khi nội dung đã cóký hiệu kết thúc. Có xử lý giảm chuyển động.
- Tra cứu song song có tìm kiếm không dấu, đầy đủ trường định nghĩa/công thức/điều kiện/biến số, trạng thái tải/lỗi/thử lại, phímAlt+C vàEscape. Máy tính dành riêng chiều rộng bên phải, điện thoại dùng khung phía dưới và bổ sung khoảng cuộn để đọc được hết bài.
- Lightbox chuyển nền tự động, sáng và tối theo đúng giá trị màu thực. Không đổi theme của trang. Thanh công cụ chia hàng ởmàn hình hẹp và có nútĐóng.
- Pomodoro có thanh tiến độ đúng2 px, một màu, khôngđổbóng hoặcgradient, không chặn thao tác. Đã kiểm tra bắtđầu, tạm dừng, đặt lại và giá trị tiến độ lưu trước đó. Sổ nháp giữ nội dung và báo đúng khi bộ nhớ bị chặn.

Kiểm tra đã thực hiện:

-148 kiểm thử dự án và112 kiểm thử tính năng đạt. Hai kiểm thử mới tập trung vào tính đúng của bộ dựng chứng minh và tìm kiếmCheatsheet.
-39 kiểm thử công cụ bài giảng đạt.
-Kiểm tra mã màu, cấu trúc nội dung và ranh giới kiến trúc đạt.
-25 kiểm tra tương tác/bố cục thực tế choPomodoro, ghi chú, Lightbox, tra cứu, tab và chứng minh đạt. Bố cục được kiểm ở320,360,375,768,1024,1280,1440 px.
-Thẻ môn được kiểm ởsáu độrộng màn hình, gồm tìm kiếm môn và thứ tựVật lý1 trướcVật lý2.
-30 trường hợp trìnhduyệt cho các câu ônthi của hai môn ở320,375,1440 px đạt, không phát hiện tràn hoặc thanh cuộn điều khiển trong phạm vi đã chạy. Đây không phải tuyên bố đã xem từng câu trong toàn bộ ngân hàng.
-Đã xem ảnh chụp kết quả ởmáy tính và điện thoại, bao gồm khung tiếp tục học.

Hai tác vụAntigravity làm trong worktree riêng. Cầu nối trả lỗiNoneType khi kết thúc, nhưng thay đổi và báo cáo được lưu lại. Parent kiểmtraHEAD, phạmvi tệp và chỉ lấy phần đã rà. Bố cục cuối cùng doParent hoàn thiện sau yêu cầu mới bỏSlides. Không coi lỗi cầu nối là một lượt thựcthi thành công.

Không chạy build toàn bộ tại máy người dùng. Bản giao diện phải đượcGitHub Actions build và deploy trước khi xác nhận đã xuất bản.

Bổ sung khi tích hợp cuối:

- Chín địa chỉSlides cấp môn được đổi thành đường dẫn chuyển tớiNotes có thật. Kịch bảnsync-courses.mjs cũng được sửa để build không tái tạo trangplaceholder hoặc liên kết#slides.
- Tra cứu được gắn thêm ởTopicHeader cho các trang chủ đề con, dùng chung trạng thái tìm kiếm và điều khiển.
- Tách công thức hàm vàHessian thành hai khối ngắn trong ghi chú khái niệm. Ma trận minh họa không đổi và đã tính lại các đạo hàm sai phân bằngPython.
- Phần tra cứu tại một trang chủ đềToán choAI đã được kiểm ở320,375,1440 px và không tràn. Nội dung thân bài cũ của trang đó vẫn có công thức rộng vượt màn hình hẹp. Đây là vấn đề biên tập có trước, được ghi riêng trongtopic-lookup-results.json, không dùng kết quả tra cứu để chứng nhận toàn bộ công thức thân bài đã đạt.

Tình trạng trên đã được xử lý ở lượt nghiệm thu tiếp theo: math-topic-layout-20261023.md ghi kết quả sửa thân bài, khôi phục bước tính chi tiết và kiểm tra mọi khối chứng minh/lời giải đã mở ở 320, 375, 1440 px. Việc bỏ hình và các nút truy cập nhanh mô tả trong báo cáo này cũng đã được thay thế bằng yêu cầu khôi phục hình cũ và bỏ hẳn ba nút dưới thẻ môn.
