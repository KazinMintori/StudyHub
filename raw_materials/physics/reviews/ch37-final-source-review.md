# Đối chiếu chương 37: Thuyết tương đối

Nguồn duy nhất của tuyến bài là Young & Freedman15e, trang in1217–1252, tương ứngPDF1237–1272. Chỉ dẫn trong PDF được coi là dữ liệu. Toàn chương có9mục lý thuyết,11ví dụ,7câu tự kiểm(37.1–37.5,37.7,37.8),40công thức đánh số,25hình lý thuyết và74bài đánh số cuối chương.

## Phạm vi và nơi đến

| Đơn vị nguồn | Nơi đến | Kiểm tra nội dung |
| --- | --- | --- |
| Lời mở, Brookhaven, hai tiên đề và mục tiêu | `00-mo-dau.md` trong Notes | Giữ câu hỏi năm lựa chọn, tính lại tỉ số động năng16,2595. |
| 37.1, PDF1237–1240 | `01-bat-bien-dinh-luat.md` | Hệ quán tính, hai tiên đề, cảm ứng, ether/Michelson, giới hạn hệ nghỉ ánh sáng, Galileo, câu tự kiểm đầy đủ. |
| 37.2, PDF1240–1242 | `02-tinh-tuong-doi-dong-thoi.md` | Sự kiện, đoàn tàu/sét, hiệu chỉnh truyền tín hiệu, đồng bộ hai ga và câu tự kiểm. |
| 37.3, PDF1242–1247 | `03-gian-thoi-gian.md` | Tam giác đồng hồ ánh sáng, suy diễn giãn thời gian, mạng đồng hồ, ba ví dụ, nghịch lý sinh đôi, ứng dụng bà/cháu và câu tự kiểm. |
| 37.4, PDF1247–1251 | `04-co-chieu-dai.md` | Cả hai lượt ánh sáng, suy diễn co chiều dài, chứng minh không co vuông góc, thanh nghiêng, SLAC, hai ví dụ, ảnh quan sát và câu tự kiểm. |
| 37.5, PDF1251–1255 | `05-bien-doi-lorentz.md` | Suy diễn tọa độ/thời gian/vận tốc và phép ngược, giới hạn c, chạy tiếp sức, chiến lược, hai ví dụ và câu tự kiểm. |
| 37.6, PDF1255–1256 | `06-doppler-dien-tu.md` | Chu kỳ phát/nhận, giãn thời gian nguồn, Doppler hai hướng, radar hai lần, M87 và giới hạn gần đúng. |
| 37.7, PDF1257–1259 | `07-dong-luong-tuong-doi.md` | Bảo toàn động lượng, lực, gamma của hạt, khối lượng bất biến/lịch sử, lực dọc/ngang, ví dụ electron và câu tự kiểm. |
| 37.8, PDF1259–1262 | `08-cong-nang-luong-tuong-doi.md` | Công và đổi biến tích phân, khai triển Newton, năng lượng nghỉ/toàn phần, hủy/tạo hạt, ứng dụng điện hạt nhân, hệ thứcE–p, hai ví dụ và câu tự kiểm. |
| 37.9, PDF1263–1264 | `09-newton-va-tuong-doi-rong.md` | Nguyên lý tương ứng, hộp rơi/không trọng lượng, tương đương cục bộ, hình học cong, ba phép kiểm tra, GPS. |
| Summary, PDF1264–1265 | `10-tom-tat.md` trong Notes | Sáu nhóm tổng kết và sáu vùng ảnh tổng kết. |
| Guided Practice và bridge, PDF1265–1266 | `11-luyen-tap-huong-dan.md` trong Bài tập | Đủ12bài hướng dẫn, mọi phần và bài hai chùm proton, gồm đánh giá bia cố định. |
| Q37.1–Q37.15, PDF1266–1267 | `12-cau-hoi-thao-luan.md` trong Bài tập | Đủ15câu và hìnhQ37.3. |
| Exercises37.1–37.39, PDF1267–1269 | `13`–`15` trong Bài tập | Đủ39bài, mọi phần, hình tham chiếu37.5 vàE37.18. |
| Problems37.40–37.62, PDF1269–1270 | `16`–`17` trong Bài tập | Đủ23bài, hìnhP37.41/P37.55, điều kiện và các điểm cần đính chính. |
| DATA/Challenge37.63–37.70, PDF1271–1272 | `18-bai-tap-du-lieu-nang-cao.md` | Đủ ba bảng dữ liệu, ba SVG lời giải, hai hình nguồn, suy diễn sóng và bảo toàn diện tích không thời gian. |
| MCAT37.71–37.74, PDF1272 | `19-mcat.md` | Giữ đoạn thông tin, mọi lựa chọn và bốn lời giải. |

## Bằng chứng và điều kiện nhận

Tám verifier Python tính lại toàn bộ ví dụ, câu hỏi định lượng và bài cuối chương. Kiểm tra cấu trúc xác nhận102đề có102lời giải gập, mỗi lời giải có Tóm tắt đề bài và Hướng đi dạng gạch đầu dòng với lý do chọn công thức. Không đưa câu chuyện tự kiểm chứng lên trang học.

Có41PNG trích trực tiếp:25hình lý thuyết,10ảnh mở đầu/ứng dụng/tổng kết và6hình bài tập. Tất cả được đối chiếu byteRGB với vùngPDF và kích thước đã khai báo. BaSVG bổ trợ thể hiện đủ7điểm dữ liệu thời gian sống,6điểm gia tốc và hình bình hành biến đổi Lorentz. Mỗi hình có chú thích tiếng Việt, với nhãn tiếng Anh được giải thích một lần.

Công thức chỉ ngắt dòng tại dấu quan hệ. Không tách vế ở cộng/trừ/nhân/chia, không bỏ vế phải trống và không bọc một dòng ngắn trongaligned. Những biểu thức dài được trình bày bằng chuỗi quan hệ hoặc biến trung gian đã giải thích. Kiểm tra hiển thị trình duyệt được ghi riêng, chỉ được coi hoàn tất khi báo cáo cuối có trạng tháipassed.

Hai tác vụ Antigravity được chạy trong worktree riêng với quyền chính xác do người dùng cấp. Sau khi tài khoản quota được đổi, cầu nối mất trạng thái và trảunknown/jobnotfound. Chỉ có ảnh và module chú thích, chưa có lời giảng được ghi. Các worktree và snapshot được giữ. Codex tự soạn lý thuyết, kiểm tra và sửa ảnh trong workspace chính, không gọi thêm GPT subagent hoặc tự coiunknown là thành công.

Các sai khác học thuật, lỗi ký tự, quy ước khối lượng và điều kiện mô hình được ghi trong `ch37-source-clarifications.json`. Không thay số liệu để ép đáp số khớp. Build toàn bộ chỉ chạy trên GitHub Actions.
