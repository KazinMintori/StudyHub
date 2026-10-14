# Chương 31: Kiểm kê và rà lý thuyết

Ngày: 2026-10-14.
Trạng thái: Lý thuyết đã soạn và kiểm nguồn, đang kiểm giao diện. Bài tập cuối chương đang ở hai tác vụ Antigravity riêng. Chưa công bố chương hoàn chỉnh.

## Nguồn và nơi đến

Nguồn là PDF do người dùng cung cấp tại raw_materials/physics/source/young-freedman-15.pdf. Lý thuyết ở trang in 1018–1039, tương ứng PDF 1038–1059. Tổng kết ở trang in 1040. Đáp án câu mở đầu ở trang in 1047. Đã đọc ảnh trang có công thức, hình và dữ kiện dễ bị OCR nhầm.

| Đơn vị nguồn | Fragment | Thành phần giữ lại |
| --- | --- | --- |
| Mở đầu | 00-mo-dau.md | Edison, Westinghouse, truyền tải điện, câu hỏi radio đủ năm lựa chọn, sáu mục tiêu và kiến thức ôn lại |
| 31.1 | 01-gian-do-pha-hieu-dung.md | Nguồn hình sin, vector pha, điện kế, chỉnh lưu, trung bình chỉnh lưu, rms, Ví dụ 31.1, tự kiểm |
| 31.2 | 02-dien-tro-dien-khang.md | Điện trở, cuộn cảm, tụ, suy diễn điện kháng và pha, cảnh báo biên độ/tức thời, dòng dịch, Bảng 31.1, bộ lọc, phân tần loa, Ví dụ 31.2–31.3, tự kiểm |
| 31.3 | 03-mach-rlc-noi-tiep.md | Tổng vector, trở kháng, pha, quả cầu plasma, trở kháng sinh học, thiếu phần tử, hiệu dụng, chiến lược giải, Ví dụ 31.4–31.5, tự kiểm |
| 31.4 | 04-cong-suat-xoay-chieu.md | Công suất từng phần tử, suy diễn trung bình, hình chiếu pha, hệ số công suất, bù tụ, Ví dụ 31.6–31.7, tự kiểm |
| 31.5 | 05-cong-huong.md | Tần số cộng hưởng, điện áp cuộn và tụ, chỉnh đài, độ rộng đáp ứng, liên hệ tắt dần/cơ học, Ví dụ 31.8, tự kiểm |
| 31.6 | 06-may-bien-ap.md | Cấu tạo, Faraday, tỉ số vòng, phân phối điện, adapter, năng lượng, điện trở quy đổi, phối hợp trở kháng, tổn hao, ghép lá, tiếng ù, truyền tải một chiều, Ví dụ 31.9, tự kiểm |
| Tổng kết | 09-tom-tat.md | Đủ bảy đơn vị tổng kết và bảy hình thu nhỏ |

## Số lượng đã đối chiếu

- 37 nhãn phương trình, mỗi nhãn xuất hiện một lần tại phần giảng.
- 9 ví dụ, giữ đủ yêu cầu và phần đánh giá.
- 6 tự kiểm ở đúng mục, đề nhìn thấy và chỉ gập đáp án.
- 24 hình đánh số, một ảnh mở đầu, hai ký hiệu, một hình tự kiểm, ba ảnh ứng dụng, bảy hình tổng kết. Tổng cộng 38 ảnh.
- 11 Slides, 6 nhóm Cheatsheet với 21 mục, 10 Wiki.
- Bài tập cuối chương thuộc fragment riêng, không đưa vào Notes.

## Điểm đã mở rõ hoặc hiệu chỉnh

1. Ví dụ 31.2 dùng 250 microampe. Văn bản trích xuất nhầm micro thành milli. Dữ kiện đã đọc trực tiếp từ ảnh trang 1024.
2. Điện áp nguồn và dòng ở 31.1 có thể chọn mốc pha riêng. Không suy mọi mạch đều có dòng cùng pha nguồn.
3. Dấu điện áp cuộn theo quy ước thụ động khác dấu suất điện động tự cảm dọc chiều dòng.
4. Hằng số điện tích tụ bằng không thuộc trạng thái xoay chiều thuần đang xét, không được bỏ tùy ý.
5. Nối tắt vị trí tụ cho dung kháng bằng không, không đặt điện dung bằng không.
6. Trường hợp điện trở và điện kháng tổng cùng bằng không không cho dòng ổn định hữu hạn theo tỉ số điện áp trên trở kháng.
7. Công suất điện trở không âm, bằng không tại các điểm dòng qua không. Không khẳng định dương ở mọi thời điểm.
8. Tự kiểm 31.4 giữ đủ hai câu và năm lựa chọn. Hai phần tử có khả năng trả năng lượng không phải luôn cùng trả tại mọi thời điểm.
9. Đỉnh dòng cưỡng bức khác đỉnh điện áp phần tử và tần số dao động tự do tắt dần.
10. Công suất máy biến áp nêu tải thuần trở và bỏ qua dòng từ hóa. Chiều quấn, đầu đo quyết định dấu điện áp tức thời.
11. Ứng dụng tác động điện lên cơ thể được đối chiếu NIOSH. Không coi co cơ do dòng một chiều là cơ chế bảo vệ. Giữ nội dung co cơ, khó buông vật và vai trò hạ điện áp.
12. Tuyến điện mặt trời Bắc Phi tới châu Âu là tình huống kỹ thuật, không khẳng định trạng thái hiện nay của dự án.

## Bằng chứng và phần còn lại

verify_chapter31_01.py kiểm trung bình chỉnh lưu, hiệu dụng và bốn góc pha. verify_chapter31_theory.py kiểm chín ví dụ, tự kiểm, Kirchhoff lấy mẫu, trung bình công suất và đường cộng hưởng. Báo cáo tại qa/physics/chapter31/theory-numeric-checks.json.

Nguồn lý thuyết sau bẻ dòng không có công thức vượt 27ex display, 38ex inline. Gợi ý văn phong còn lại thuộc các lựa chọn trắc nghiệm cố ý viết ngắn.

Còn kiểm trực tiếp giao diện, lời giải cuối chương, ảnh bài tập, đáp số và tất cả yêu cầu tích hợp trước khi đổi chương sang hoàn chỉnh hoặc push.
