# Rà soát cuối Chương 33

Phạm vi nguồn là trang in 1077–1109, tương ứng PDF 1097–1129. Đã kiểm tra trang đầu chương 34 để xác nhận ranh giới. Tài liệu là Young & Freedman, *University Physics with Modern Physics*, ấn bản 15, SHA256 `f4ea22dc8d5113f47ec8fd8a2b9f71f7be78ee3db069971aace4b7cda04175ff`.

## Nội dung và nơi hiển thị

| Đơn vị nguồn | Nơi đến | Kết quả rà |
| --- | --- | --- |
| Lời dẫn, mục tiêu, câu hỏi kim cương và kiến thức ôn | Notes trang chương | Đủ năm lựa chọn, chỉ gập câu trả lời |
| 33.1 | Chủ đề bản chất ánh sáng | Hai mô hình, các nguồn phát, tốc độ chính xác, mặt sóng, tia, tự kiểm |
| 33.2 | Chủ đề phản xạ và khúc xạ | Ba định luật, 22 giá trị chiết suất, tính thuận nghịch, ứng dụng, chiến lược 33.1 và ví dụ 33.1–33.3 |
| 33.3 | Chủ đề phản xạ toàn phần | Góc giới hạn, Porro, nội soi, thông tin quang, kim cương, ví dụ 33.4 và tự kiểm |
| 33.4 | Chủ đề tán sắc | Đồ thị, lăng kính và toàn bộ năm phần hình cầu vồng |
| 33.5 | Chủ đề phân cực | Định nghĩa, cơ chế kính vi ba và Polaroid, Malus, chiến lược 33.2, ví dụ 33.5–33.6, Brewster, tròn, elip, lưỡng chiết, quang đàn hồi, phim 3D, LCD và tự kiểm |
| 33.6 | Chủ đề tán xạ | Mô hình điện tích dao động, màu trời, mây, sữa, hoàng hôn và thị giác ong |
| 33.7 | Chủ đề Huygens | Dựng mặt sóng, hai chứng minh, ảo ảnh và tự kiểm sóng âm |
| Tổng kết và sáu hình tổng kết | Notes trang chương | Đủ các quan hệ nguồn, bổ trợ Cheatsheet riêng |
| 12 Guided Practice và bài cầu nối | Bài tập | 13 đề và 13 lời giải |
| Q33.1–Q33.25 | Bài tập | 25 câu và 25 lời giải |
| 33.1–33.35 | Bài tập | 35 bài, đủ dữ kiện và các hình E |
| 33.36–33.58 | Bài tập | 23 bài tổng hợp, đủ các hình P và bảng dữ liệu |
| 33.59–33.61 | Bài tập | Ba bài nâng cao có suy diễn và điều kiện mô hình |
| 33.62–33.64 | Bài tập | Đoạn dẫn MCAT, đủ lựa chọn và lời giải |
| Đáp số bài lẻ | Bài tập | 32 hàng, thống nhất với dữ kiện và lời giải |

Không có câu tự kiểm riêng ở mục 33.4 hoặc 33.6. Đã loại câu tự kiểm 33.6 bị thêm nhầm, đồng thời giữ các câu hỏi trong mạch giảng về biến đổi đặc trưng sóng, kính phân tích, hai góc Brewster và bản phần tư sóng. Các câu hỏi hiện trước phần trả lời, tại vị trí đang giảng.

## Hình và trình bày

Có 76 PNG trích trực tiếp từ các vùng PDF, đối chiếu kích thước và toàn bộ byte RGB giải mã. Bao gồm 36 hình lý thuyết đánh số, hình cầu nối 33.37, 26 hình E/P, hình mở đầu, bốn ảnh ứng dụng, sáu hình tổng kết, hình cá trong câu tự kiểm và ảnh thứ hai của Hình 33.25.

Hai ảnh kính phân cực 33.25 được giữ thành hai vùng gốc riêng, không ghép ảnh lên nền mới. Hình Porro 33.14 và thanh dẫn sáng 33.15 đã mở rộng vùng trích để giữ đủ mũi tên ló. Hình 33.12 giữ trọn phần chú thích thay vì các mẩu chữ bị cắt. Hình cầu vồng giữ đủ năm phần.

Chú thích tiếng Việt lấy từ văn bản mô tả của ảnh. Các chữ tiếng Anh thực sự có trên hình được giải nghĩa một lần bằng dữ liệu chú thích tập trung. Đã loại các danh sách nhãn thủ công bị lặp trong Markdown và bổ sung nhãn trên màn hình LCD.

Các công thức được biên dịch MathJax và đo riêng phần thân. Mục tiêu biên tập là 27ex cho khối hiển thị, 38ex cho nội dòng. Các số hiệu đặt sau môi trường aligned. Không dùng việc ẩn phần tràn thay cho ngắt công thức.

## Tính toán và các hiệu chỉnh nguồn

Các chương trình `verify_chapter33_*.py` kiểm tra sáu ví dụ, các bài cuối chương và những lập luận định lượng. Bài 33.57 dùng đủ 19 điểm vectơ của đồ thị. Bài 33.54 được kiểm tra riêng bằng thông lượng Poynting pháp tuyến và biên độ Fresnel. Bài 33.59 nêu rõ mô hình uốn đều và đường tia tiếp tuyến biên trong.

Những sai khác cần xử lý được ghi tại `qa/physics/chapter33/source-clarifications.json`: Góc quay không nhất quán ở 33.48, thứ tự bán trục ở 33.54, bất đẳng thức phản xạ ở 33.59, các nhãn góc, đơn vị và số liệu đọc đồ thị. Không thay dữ kiện để ép khớp đáp số. Phần xử lý bất nhất cần thiết cho lời giải được trình bày khách quan, không kể quá trình kiểm chứng trong trang học.

## Antigravity và ranh giới công việc

Hai tác vụ A/B được cho phép đúng worktree và danh sách tệp. Mỗi tác vụ đã dùng đủ ba lượt, gồm lượt đầu bị chặn quyền. Cả hai lượt cuối đều kết thúc với lỗi cầu nối `expected string or bytes-like object, got 'NoneType'`. Vì vậy không ghi nhận chúng là tác vụ thành công dù có các tệp đầu ra.

Đã kiểm tra Git, chụp bản sao ổn định theo hash, giữ nguyên worktree và dừng gọi lại. Codex tự đối chiếu, sửa và kiểm tra các bản sao trong repo chính. Không gọi lượt thứ tư, không mở rộng quyền sở hữu và không dùng subagent GPT.

## Tích hợp và kiểm tra

Có 11 Slides, tám nhóm Cheatsheet với 17 mục chỉ gồm định nghĩa, tính chất, công thức, điều kiện và ký hiệu. Có 14 Wiki mới cùng mục Snell được sửa, giữ lại các ID chiết suất và phân cực thẳng đang dùng. Đã sửa phát biểu Fermat từ thời gian nhỏ nhất tuyệt đối thành quang lộ dừng.

Kiểm tra cấu trúc trên bản ứng viên dùng giao diện đang xuất bản đã qua 44 bài và 83 trang chủ đề, không lỗi hoặc cảnh báo. Kiểm tra toàn repo đang làm việc cũng qua. Kiểm tra ảnh qua 699 danh sách chú thích và 944 đường dẫn. Bộ skill có 39 kiểm thử đạt. Bộ hiển thị đã kiểm 13.878 công thức khác nhau, còn phần dữ liệu Vật lý có 2.295 tham chiếu công thức với bản SVG tương ứng.

Kết quả trình duyệt và xuất bản cuối cùng được ghi tại `chapter-33-review.json` và hồ sơ riêng trong `qa/physics/chapter33/`. Chỉ chấp nhận khi báo cáo cuối có trạng thái passed. Những lần bị ngắt hoặc timeout điều khiển slide được giữ để đối chiếu, không tính là một lượt kiểm hoàn tất.

Không chạy build toàn bộ ở máy người dùng. Build và triển khai được giao cho GitHub Actions sau push.
