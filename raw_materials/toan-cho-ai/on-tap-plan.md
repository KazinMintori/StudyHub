# Kế hoạch xử lý Tài liệu ôn tập

Nguồn được người dùng giao ngày 12/10/2026: `toan-cho-ai/Tài liệu ôn tập/`. Gồm 103 ảnh bảng, chia thành Buổi 1 (28 ảnh), Buổi 2 (22 ảnh), Buổi 3 (27 ảnh), Buổi 4 (26 ảnh). Đây là nguồn được phép dùng trực tiếp theo yêu cầu mới của người dùng.

- [x] Kiểm kê toàn bộ tệp và kiểm tra SHA-256: Không có ảnh trùng byte.
- [x] Đọc trực tiếp từng ảnh, ghi đơn vị nội dung và phần bị che/cắt.
- [x] Sao chép ảnh nguyên vẹn vào tài nguyên website, lưu tên gốc và SHA-256 trong manifest.
- [x] Phân chia thành 12 chủ đề và bốn phần trong tab Ôn luyện cạnh tab Bài giảng.
- [x] Chuyển đầy đủ công thức, ví dụ, bài tập và hình học thành lời giảng, bổ sung điều kiện cần thiết.
- [x] Tính lại ví dụ và lời giải bằng Python.
- [x] Tích hợp Notes, Cheatsheet và Kiến thức nền theo giao diện hiện tại của repo.
- [x] Đối chiếu 103/103 ảnh với nơi đến, kiểm nội dung và 49 lượt kiểm trình duyệt. Build cuối sau lượt bẻ dòng đã hoàn tất với exit 0.

## Điều chỉnh thứ tự học

Theo yêu cầu bổ sung của người dùng, đổi nhãn thành Ôn luyện 1–4 và sắp theo quan hệ tiên quyết, không giữ thứ tự thư mục làm thứ tự giảng dạy. Thứ tự gốc đặt KKT ở Buổi 2 trước phần hệ thống tính lồi ở Buổi 3. Chuẩn và ma trận cũng cần đứng trước tiêu chuẩn Hessian.

| Phần mới | Nội dung theo thứ tự | Nguồn gốc |
| --- | --- | --- |
| Ôn luyện 1 | Không gian, chuẩn, ma trận, dạng toàn phương → đạo hàm, gradient, Hessian, cực trị | Buổi 3 ảnh 01–10 và Buổi 1 ảnh 19–28 |
| Ôn luyện 2 | Tập lồi, hàm lồi → mô hình và hồi quy → LP → bài toán có cos | Buổi 3 ảnh 11–27 và Buổi 1 ảnh 01–18 |
| Ôn luyện 3 | KKT → bài tham số → đối ngẫu → bài tập có ràng buộc | Buổi 2 ảnh 01–22 |
| Ôn luyện 4 | Quy tắc chuỗi → Taylor nhiều biến → hướng giảm → gradient, backtracking, Newton | Buổi 4 ảnh 01–26 |

Các phần xuất hiện lại giữa ảnh nguồn được gom vào chủ đề giải thích chính, không bỏ ảnh. Manifest tiếp tục giữ nhãn thư mục Buổi 1–4 và tên tệp gốc. `requires` trong catalog và `scripts/verify-math-ai-review.mjs` kiểm mọi chủ đề cần học trước đều nằm phía trước chủ đề sử dụng nó.

## Kết quả kiểm tra

- `npm run ci:build`: Build cuối thành công với exit 0. Có cảnh báo kích thước bundle lớn của toàn site.
- Kiểm tra máy chủ local: 103/103 URL ảnh trả HTTP 200 với đúng số byte của tệp gốc.
- `scripts/verify-math-ai-review.py`: Các phép tính hồi quy, LP, KKT, đối ngẫu, Hessian, Taylor và Armijo đều qua.
- `scripts/verify-math-ai-review.mjs`: 103/103 ảnh khớp byte và SHA-256, đủ 12 chủ đề, không đảo phụ thuộc.
- `check_lecture.mjs --all`: 88 bài và 67 trang chủ đề, không lỗi và không cảnh báo.
- `test_tools.py`: 39 kiểm thử qua khi chạy với quyền truy cập tệp tạm phù hợp trên Windows.
- `scripts/verify-math-ai-review-browser.mjs`: 49 lượt kiểm tại 360px, 375px, 1440px, không lỗi JavaScript, không lỗi MathJax, không tràn công thức.
- Kiểm tra bản đã build: 8 lượt kiểm tab, lịch sử trình duyệt, ba chủ đề đại diện và các phần của trang tổng hợp đều qua, không lỗi hoặc tràn công thức.
- `scripts/tests/math-ai.test.mjs`: 7 kiểm thử mô phỏng toán qua.
- Kiểm tra bổ sung `scripts/tests/math-text.test.mjs`: Bị chặn bởi dấu đô la trong đoạn giá tiền ở `docs/xu-ly-du-lieu/bai-tap.md`. Không sửa nội dung môn khác trong nhiệm vụ này.

## Buổi 1: Đã đọc 28/28 ảnh

| Ảnh | Nội dung | Ghi chú |
| --- | --- | --- |
| 01–02 | Vector quyết định, mục tiêu, ràng buộc, phương án, nghiệm và giá trị tối ưu, quy hoạch nguyên | Phân biệt tập khả thi D với bộ dữ liệu học |
| 03–05 | Học có giám sát, dữ liệu trong R^d × R^k, hàm dự đoán, loss, tham số, trung bình loss | Chỉ số thành phần của đầu ra trên bảng chưa thống nhất, chuẩn hóa về k |
| 06–10 | Hồi quy affine, sai số bình phương, ma trận X có cột 1, phép chiếu lên Col(X), phương trình chuẩn | 07 chụp lại 06, 10 tổng quan 08–09 |
| 11–14 | LP tổng quát, nửa mặt phẳng, min(x−y) trên tam giác x,y≥0 và x+y≤1 | Nghiệm (0,1), giá trị −1 |
| 15 | min(−3x−2y), x+y≤6, 0≤x≤4, 0≤y≤3 | Năm đỉnh, nghiệm (4,2), giá trị −16 |
| 16–18 | Quy hoạch lồi, bất đẳng thức dây cung, đoạn thẳng, quy hoạch phi tuyến không lồi | 17 chụp lại 16. Bổ sung: Phi tuyến không đồng nghĩa phi lồi |
| 19–22 | Đạo hàm, định lý giá trị trung bình, Taylor bậc hai, cực tiểu địa phương, Fermat, điều kiện đủ bậc hai | Bổ sung điều kiện trơn và điểm trong |
| 23–27 | Đạo hàm riêng của x²+xy+xz, gradient, đạo hàm hỗn hợp, Hessian, Fermat nhiều biến | 24 chụp lại 23, 25 tổng quan có đạo hàm bậc hai |
| 28 | Bài tập min 2x²+2xy+y²+xz+2z²+cos(x) trên R³ | Cần giải đầy đủ bằng khử y,z và kiểm chứng |

## Buổi 2: Đã đọc 22/22 ảnh

| Ảnh | Nội dung | Ghi chú |
| --- | --- | --- |
| 01–04 | Lagrangian, tập ràng buộc chặt J, độc lập tuyến tính LICQ, định lý KKT cần, KKT đủ trong quy hoạch lồi | Phần tiêu đề Karush/Kuhn/Tucker bị cắt, không mất nội dung toán |
| 05–10 | min x3 + (x1²+x2²+x3²)/2, tổng xi=r>0, xi≥0, Lagrangian, KKT, xét các trường hợp, nghiệm khi r≤2 và r≥2 | Ảnh 09 đặt trước 07–08 trong mạch giải. Ảnh 08,10 ghi λ=−(r+1)/2 nhưng hệ cho λ=−(r+1)/3. Ghi rõ hiệu chỉnh |
| 11,14–16 | Primal, hàm đối ngẫu inf L, dual max g, chứng minh −g lồi, đối ngẫu yếu/mạnh, Slater, cách tính g | μ≥0 nghĩa từng μi≥0. Điểm dừng chỉ tính inf nếu là cực tiểu toàn cục |
| 12–13 | min tổng xi³, tổng xi²≤4, tổng xi≤1, Lagrangian và trọn hệ KKT | Hàm mục tiêu không lồi trên R³. Không nhầm λ của bất đẳng thức với nhân tử tự do của đẳng thức |
| 17–18,22 | min x² với x≥1, g(λ)=λ−λ²/4, λ*=2, x*=1, p*=d*=1 | 18 chụp lại 17 |
| 19–22 | min x1²+x2², x1+x2≥1, g(y)=y−y²/2, y*=1, x*=(1/2,1/2), p*=d*=1/2 | 19 và 21 có phần bài tập tiếp theo |
| 19,21 | min tổng xi² với x1²+x2²+3x3≤5/2 và x1+x2+x3=−2 | 19 mới viết mục tiêu, 21 có đủ đề. Cần giải bổ sung |

## Buổi 3: Đã đọc 27/27 ảnh

| Ảnh | Nội dung | Ghi chú |
| --- | --- | --- |
| 01–03 | Tối ưu toàn cục/địa phương, D, −1/x trên (0,1), miền [0,1], hệ fi≤0 và hj=0, trường hợp không ràng buộc | Hàm −1/x không xác định tại 0, đóng miền không tự bảo đảm nghiệm |
| 04–06 | Chuẩn p, 1,2,vô cùng, hình cầu mở/đóng, khoảng tâm (a+b)/2, điểm trong/biên, ma trận m×n | Khai triển các tổng rõ chỉ số |
| 07–10 | Ma trận đối xứng, đa thức đặc trưng det(A−tI), n trị riêng kể bội, affine, dạng toàn phương khai triển và xᵀAx, PD/PSD và dấu trị riêng, đạo hàm hình học | Điều kiện dấu trị riêng dùng cho A đối xứng thực |
| 11–15 | Fermat, giá trị trung bình, Taylor, đạo hàm riêng qua giới hạn, gradient, đạo hàm hỗn hợp và Hessian, điều kiện cần/đủ bậc hai | Bổ sung điều kiện C² cho đổi thứ tự đạo hàm |
| 16–21 | Mô hình ràng buộc, đường/đoạn, tập lồi với hình ví dụ/phản ví dụ, hàm lồi, affine, Jensen k điểm, Hessian PSD, miền khả thi lồi, quy hoạch lồi | Giữ cả hình học và chứng minh |
| 22–23 | Chứng minh cực tiểu địa phương là toàn cục bằng đoạn x+t(y−x), gradient bằng 0 đủ cho hàm lồi | Đầu chứng minh bảng có dòng f(y)≥f(x) trước khi chứng minh. Viết lại lập luận đúng, không dùng kết luận làm giả thiết |
| 24–27 | Giải lại bài tập có cos x của Buổi 1: Gradient, Hessian, đa thức đặc trưng, tính lồi, sin x=7x/4, y=−x,z=−x/4, nghiệm 0, giá trị 1 | Bảng nhầm sin x trong đa thức Hessian và hệ số. Tính lại bằng symbolic Python. Không suy tất cả trị riêng dương chỉ từ việc không có nghiệm ≤0 nếu chưa nêu tính đối xứng |

## Buổi 4: Đã đọc 26/26 ảnh

| Ảnh | Nội dung | Ghi chú |
| --- | --- | --- |
| 01–02 | Vector, bài toán min trên D, sai số nghiệm ε, khoảng cách Euclid, dãy xấp xỉ và hướng d | Sai số nghiệm khác sai số hàm và chuẩn gradient |
| 03–07 | Giá trị trung bình/Taylor một biến, hàm hợp một và nhiều biến, quy tắc chuỗi, đường cong phi và đạo hàm dọc đường | Ký hiệu đạo hàm hàm hợp trên bảng rút gọn, viết đầy đủ |
| 08–11,13 | g(t)=f(x+th), đạo hàm g′, tổng kép g″=hᵀHh, Hessian, Taylor nhiều biến bậc một/hai | 13 chụp lại 10 và thêm g(1)=g(0)+g′(θ) |
| 12,14–18 | Hướng giảm, tích gradient và d âm, learning rate, thuật toán GD, góc tù, đường mức, backtracking α∈(0,1/2), β∈(0,1) | Bảng ghi Armijo–Wolfe nhưng chỉ viết điều kiện Armijo, cần phân biệt |
| 19–22,24,26 | f=x²+2y², x0=(2,1), α=.1,β=.5, gradient (4,4), backtracking 1→.5, x1=(0,−1), vòng hai 1→.5→.25, x2=0 | 22 có hai số nháp sai tại t=1. Bảng thử đủ giá trị đúng |
| 23 | Quét lưới một biến và n biến, hộp tích các khoảng, bùng nổ m^n, số 2^64 và 2^100 | Nhãn m^n=100 trên bảng không rõ ý, giữ ảnh và giải thích số ô thay vì gán thành định lý |
| 25 | Sơ đồ đường lặp, hướng Newton d=−H⁻¹grad, số 2^100 | Bổ sung điều kiện H PD và cách giải hệ không lập nghịch đảo |

## Phạm vi bảo toàn

Mỗi ảnh phải có một mục manifest và ít nhất một nơi đến. Ảnh chụp lại vẫn được giữ. Công thức bị cắt không được đoán thành bản chép chắc chắn. Phần bổ sung sư phạm và hiệu chỉnh kiến thức được ghi trong sổ đối chiếu, không làm mất biểu thức nhìn thấy trên ảnh.
