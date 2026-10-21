# Bài 1 — Đáp án rút gọn

Đối chiếu với [đề bài](Bai1_60_cau_hoi.md). Đủ 60 câu: 40 trắc nghiệm, 20 tự luận.

Trắc nghiệm chỉ ghi lựa chọn; tự luận ghi kết quả và phần giải thích tối đa 2 dòng. Đoạn mã được giữ khi đề yêu cầu viết hoặc sửa mã.

## Trắc nghiệm

| Mã câu | Đáp án |
|---|:---:|
| B1-001 | B |
| B1-002 | C |
| B1-003 | C |
| B1-004 | A |
| B1-005 | D |
| B1-006 | C |
| B1-007 | D |
| B1-011 | D |
| B1-012 | D |
| B1-013 | C |
| B1-014 | A |
| B1-015 | D |
| B1-016 | A |
| B1-017 | C |
| B1-021 | B |
| B1-022 | D |
| B1-023 | C |
| B1-024 | C |
| B1-025 | A |
| B1-026 | A |
| B1-027 | B |
| B1-031 | A |
| B1-032 | B |
| B1-033 | D |
| B1-034 | B |
| B1-035 | B |
| B1-036 | A |
| B1-037 | C |
| B1-041 | B |
| B1-042 | D |
| B1-043 | C |
| B1-044 | B |
| B1-045 | A |
| B1-046 | B |
| B1-051 | B |
| B1-052 | C |
| B1-053 | D |
| B1-054 | A |
| B1-055 | D |
| B1-056 | A |

## Tự luận

### B1-008

Phiên cũ in 80; sau restart, cell A gặp NameError vì chưa có `gia`.
Thêm `gia = 40` trước A, chạy lại từ đầu và đối chiếu tính tay 40 × 2 = 80.

### B1-009

Nhóm đã khai báo AI nhưng còn thiếu hiểu hàm và kiểm chứng số liệu.
Người nộp chịu trách nhiệm về kết quả sai; viết lại code không miễn khai báo hay trách nhiệm hiểu.

### B1-010

Thiếu repo GitHub private và lịch sử commit của nhóm.
Git quản lý lịch sử phiên bản; GitHub lưu repo và hỗ trợ cộng tác.

### B1-018

80 là trung bình 3 giá đã biết, chưa xác định trung bình cả 5 chỗ ở.
Kiểm tay 240/3 = 80; hai giá chưa biết không tự được tính là 0.

### B1-019

Tệp mô tả môi trường A vì Python đang trỏ A; chuyển thư mục không đổi venv.
Tại B, chạy `source .venv/bin/activate` rồi `python -m pip freeze > requirements.txt`.

### B1-020

Phần code An không giải thích được nhận 0 điểm cá nhân; không suy thành cả nhóm nhận 0.
Khai báo AI không thay trách nhiệm hiểu; không dùng AI trong vấn đáp là đúng chế độ.

### B1-028

B in 3 trước restart, rồi gặp NameError sau restart; xóa cell chỉ xóa mã, chưa xóa biến đang lưu.
Khôi phục `muc = 3` trước B rồi Restart & Run all.

### B1-029

Dùng AI dịch nhưng khai không dùng là khai man; cần khai đúng công cụ, công việc và kiểm bản dịch.
Nhờ AI viết lại code nhóm khác vẫn là chép bài; phải tự làm, hiểu và kiểm chứng phần của nhóm.

### B1-030

Thu thập → làm sạch → biến đổi → trực quan → kể chuyện.
Phải chuẩn bị và kiểm tra dữ liệu vì đầu vào sai có thể làm thống kê, kết luận sai.

### B1-038

Chọn đúng Python đã ghi, tạo venv mới, cài từ requirements.txt rồi chạy theo README.
README cần ghi hệ điều hành và lệnh dựng/chạy; chép .venv không thay thế quy trình này.

### B1-039

I: vi phạm chế độ đóng dù đã khai; II: giấu dùng AI dù bài mở; III: bài làm sai, người nộp chịu trách nhiệm.
Khai báo, quyền dùng và tính đúng là các yêu cầu riêng, không thay thế nhau.

### B1-040

Tôi dùng ChatGPT, chưa biết model, với prompt “Tính phần trăm số hàng theo room_type của ds, kết quả ở thang 0–100”.
AI trả 0–1; tôi nhân 100, đối chiếu từng nhóm bằng đếm tay mẫu nhỏ và kiểm tổng gần 100%.

### B1-047

`print(ten)` gặp NameError vì restart xóa biến trong phiên.
Mã, output đã lưu và tệp Drive vẫn còn; output cũ không chứng minh biến đã được tạo lại.

### B1-048

Khuyến nghị tự gõ không đổi nhãn mở của phần tự làm; quiz đóng cấm AI dù chỉ hỏi chút.
Xác định quyền theo nhãn/hướng dẫn từng hoạt động; chưa rõ thì hỏi giảng viên trước khi dùng.

### B1-049

Hai assert chỉ kiểm A và tổng, bỏ sót B/C sai; đúng là A/B/C = 0,8/0,15/0,05 = 80%/15%/5%.
Đối chiếu từng nhãn với 16/20, 3/20, 1/20; vài assert qua chưa chứng minh toàn bộ dữ liệu đúng.

### B1-050

Mỗi chấm là một con chim, màu phân biệt loài; groupby("species") chia dữ liệu theo loài.
Lưu API key trong Secrets, không dán khóa thật vào code hoặc commit.

### B1-057

Run all phiên cũ in 5; sau restart, A gặp NameError và chưa chạy B.
Thêm `dem = 4` trước A để lượt chạy sạch in 5.

### B1-058

Đã cài đúng thư viện nhưng Python nền 3.11.9 chưa khớp 3.12.3; .python-version không tự đổi venv.
Chạy `python3.12 -m venv .venv312`, kích hoạt venv này, cài requirements rồi chạy theo README.

### B1-059

Không đúng: trung bình giá đã biết là 30; điền 0 làm đổi mẫu số và tạo kết quả 15.
Kiểm tay (20 + 40)/2 = 30 trên mẫu có thiếu; ca không thiếu chưa kiểm được cách xử lý thiếu.

### B1-060

Mỗi tuần 3 tiết lý thuyết và 3 tiết lab; nộp qua GitHub Classroom, xem thông báo/phân công trên Canvas.
Trước Bài 2: chạy notebook, đọc policy, tìm nhóm 4–5; cài local chỉ khuyến nghị trước Bài 2 (G)/Bài 3 (lecture).
