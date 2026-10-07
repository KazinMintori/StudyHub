# Báo cáo kiểm tra nội dung

Đã tạo bản đặc tả 8 slide cho bài giảng tiếng Việt 12 phút và note đi kèm. Chưa tạo PDF, PPTX hoặc trang slide đã render. Mọi file tạo trong lần này nằm tại `Research/evaluation/slides-forward`.

## Phạm vi và người học

Người dùng xác nhận sinh viên biết đạo hàm, mới học tối ưu. Giả định thêm: sinh viên biết tính đạo hàm đa thức, tính bình phương và xử lý số thực. Bài chỉ truy vết một biến. Ý gradient nhiều biến được giải nghĩa ngắn, không dùng để tính hoặc làm tiên quyết cho bài tập.

Nguồn tự viết có ba đơn vị có ý nghĩa. SRC-01 là gradient descent và αₖ > 0; SRC-02 là ví dụ f, x₀, α; SRC-03 là ràng buộc đẳng thức, hàm Lagrange và ν không bị giới hạn dấu. Cả ba có nơi đến ở tuyến chính; không có hình nguồn bị bỏ. Địa chỉ nguồn ghi đúng là các câu trong yêu cầu, không bịa số trang.

## Nội dung và tiến trình đã tự rà

- Slide 2 nối gradient với đạo hàm người học đã biết. Dấu trừ và độ dời được phân biệt với điểm cập nhật.
- Slide 3 làm mẫu x₀ → x₁, gồm đạo hàm, độ dời, điểm mới và kiểm tra f.
- Slide 4 cho người học tự tính x₂; lời giải hiển thị ở Slide 5, không lộ ngay trên câu hỏi.
- Ví dụ thay riêng α thành 2 ở Slide 5 giới hạn suy luận “mọi α > 0 đều giảm f”. Không khẳng định hội tụ tổng quát.
- Slide 6 lập L với h(x) = x − 1, giữ dấu cộng trong L = f + νh và quy ước ν không bị giới hạn dấu. Không mở thêm KKT hoặc điều kiện tìm nhân tử.
- Slide 7 kiểm tra việc nhầm αₖ với ν; lời giải ở Slide 8 phân biệt “được phép về dấu” với “đã tìm được nhân tử tại nghiệm”.
- Thuật ngữ, dữ kiện, chữ slide, lời giảng và note tự học đã đối chiếu. Script xác nhận nội dung tương ứng có mặt nguyên văn trong note và các địa chỉ mục thật tồn tại.

Đây là tự rà của người soạn và kiểm tra script; không có thử nghiệm độc lập hoặc dữ liệu bài làm của sinh viên.

## Kiểm tra đã chạy

Đã dùng đúng Python yêu cầu:

```text
C:/Users/Ai/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe
```

`verify_artifacts.py` gọi `scripts/audit_spec.py` của skill với `course-spec.json` và `--asset-root` là thư mục artifact này. Lệnh đầy đủ, exit code và stderr được lưu trong `audit-command.txt`; stdout JSON lưu trong `audit-result.json`.

Kết quả: exit code 0; 8 slide; 3 đơn vị nguồn; 0 lỗi; 0 cảnh báo; tổng thời gian tuyến chính 12 phút. Hash đặc tả đã khóa trong audit: `dc248b1b713d948fe990614eae3e3e4f96b4ebae417b6b0e5da617e57f4c48d1`.

Phép tính kiểm tra bằng `fractions.Fraction`: x₁ = 3/2, x₂ = 9/4, f(x₀) = 9, f(x₁) = 9/4, f(x₂) = 9/16. Khi thay α = 2 ở x₀, x₁ = 12 và f(x₁) = 81. Assertions đã thực thi thành công; kết quả lưu trong `calculation-and-consistency.json`.

## Phần chưa kiểm chứng

Không render theo yêu cầu đánh giá. Chưa nhìn contact sheet hoặc từng trang, chưa kiểm chứng font, glyph, overflow, kích thước chữ, bố cục, màu và khả năng đọc trên output cuối. Không gọi audit cấu trúc là chứng nhận chất lượng slide hay hiệu quả học tập. Cần render và kiểm tra hình thức trước khi phát hành bộ slide dùng trong lớp.

Đã đọc SKILL.md và các reference phục vụ soạn, ngôn ngữ, note, cấu trúc, sư phạm và kế hoạch hình thức. Không đọc `behavior-tests` hoặc `prompt-research`. Không sửa skill hay site; không tìm nguồn bên ngoài.
