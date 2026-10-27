# Sửa hồi quy kiểm thử đang chặn triển khai

Lượt GitHub Actions 40365950867 trên commit `227ae2cc581eef998409ad2481b509b7239acf96` thất bại ở bước kiểm tra tính năng và hiển thị. Trong 200 kiểm thử chính, 199 đạt và một kiểm thử không đạt. Bước dựng VitePress và triển khai chưa được chạy ở lượt này.

Nhật ký chỉ rõ `scripts/tests/data-project.test.mjs` yêu cầu mục “Bài tập lớn” đứng ngay sau “Ôn thi”. Commit mới đã thêm mục “Đề thi” cùng năm trang đề vào giữa hai mục đó. Bộ điều hướng hiện đúng với tính năng mới, còn yêu cầu về vị trí liền kề trong kiểm thử đã lỗi thời.

Bản sửa giữ thứ tự “Ôn thi”, “Đề thi”, “Bài tập lớn”. Kiểm thử xác nhận đúng thứ tự, đủ năm tên và đường dẫn đề, đồng thời tiếp tục kiểm tra hai mục con của bài tập lớn và việc học phần khác không bị thêm nhầm nhóm này. Các thay đổi nhập đề của nhánh dữ liệu được ghép vào nguyên vẹn.

Sau sửa, tám kiểm thử trực tiếp liên quan đều đạt. Toàn bộ 200 kiểm thử chính và 159 kiểm thử tính năng đều đạt. Kiểm tra cấu trúc 133 bài cùng 354 chủ đề không ghi nhận lỗi hoặc cảnh báo. Bộ công cụ bài giảng có 39 kiểm thử đạt. Kiểm tra công thức toàn dự án được bao gồm trong bộ kiểm thử chính. Không chạy dựng tĩnh toàn cục trên máy người dùng.

Lỗi lịch sử vẫn giữ trạng thái thất bại của GitHub. Xác nhận đã xử lý xong nguyên nhân phải dựa thêm vào lượt dựng và triển khai mới thành công, không sửa hoặc xóa dấu vết của lượt cũ.

Đã xác nhận lượt [40375605657](https://github.com/KazinMintori/StudyHub/actions/runs/40375605657) trên commit `68ee041995d05688f602f644a262e625f7d3e60e` hoàn tất thành công lúc 18:51:12 UTC ngày 26/10/2026. Cả công việc build và triển khai đều đạt. Lượt này chứa bản sửa kiểm thử và các thay đổi dữ liệu học phần đã ghép, vì vậy lỗi chặn triển khai được nêu ở trên đã có bằng chứng khắc phục trên GitHub.

Ảnh chụp trạng thái toàn bộ lịch sử được làm mới ngày 27/10/2026, gồm 226 lượt thuộc hai workflow. Có 176 lượt thành công, 24 lượt thất bại lịch sử và 26 lượt bị hủy. Không còn lượt đang chạy trong ảnh chụp này. Cả 24 lượt lỗi đều có một lượt thành công cùng workflow và nhánh chạy sau đó. Kết luận này giới hạn ở lịch sử còn được GitHub lưu và cho phép đọc qua API.
