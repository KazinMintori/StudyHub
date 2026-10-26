# Sửa hồi quy kiểm thử đang chặn triển khai

Lượt GitHub Actions 40365950867 trên commit `227ae2cc581eef998409ad2481b509b7239acf96` thất bại ở bước kiểm tra tính năng và hiển thị. Trong 200 kiểm thử chính, 199 đạt và một kiểm thử không đạt. Bước dựng VitePress và triển khai chưa được chạy ở lượt này.

Nhật ký chỉ rõ `scripts/tests/data-project.test.mjs` yêu cầu mục “Bài tập lớn” đứng ngay sau “Ôn thi”. Commit mới đã thêm mục “Đề thi” cùng năm trang đề vào giữa hai mục đó. Bộ điều hướng hiện đúng với tính năng mới, còn yêu cầu về vị trí liền kề trong kiểm thử đã lỗi thời.

Bản sửa giữ thứ tự “Ôn thi”, “Đề thi”, “Bài tập lớn”. Kiểm thử xác nhận đúng thứ tự, đủ năm tên và đường dẫn đề, đồng thời tiếp tục kiểm tra hai mục con của bài tập lớn và việc học phần khác không bị thêm nhầm nhóm này. Các thay đổi nhập đề của nhánh dữ liệu được ghép vào nguyên vẹn.

Sau sửa, tám kiểm thử trực tiếp liên quan đều đạt. Toàn bộ 200 kiểm thử chính và 159 kiểm thử tính năng đều đạt. Kiểm tra cấu trúc 133 bài cùng 354 chủ đề không ghi nhận lỗi hoặc cảnh báo. Bộ công cụ bài giảng có 39 kiểm thử đạt. Kiểm tra công thức toàn dự án được bao gồm trong bộ kiểm thử chính. Không chạy dựng tĩnh toàn cục trên máy người dùng.

Lỗi lịch sử vẫn giữ trạng thái thất bại của GitHub. Xác nhận đã xử lý xong nguyên nhân phải dựa thêm vào lượt dựng và triển khai mới thành công, không sửa hoặc xóa dấu vết của lượt cũ.
