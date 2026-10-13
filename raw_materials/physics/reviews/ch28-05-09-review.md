# Rà soát nội dung Chương 28, mục 28.5–28.8 và tóm tắt

## Phạm vi

Đã soạn các fragment `05-vong-day-tron.md`, `06-dinh-luat-ampere.md`, `07-ung-dung-ampere.md`, `08-vat-lieu-tu.md` và `09-tom-tat.md` trong `raw_materials/physics/translations/chapter-28/`. Đối chiếu PDF in 927–943 (PDF 947–963), kể cả toàn bộ trang tóm tắt 942–943. Nội dung Guided Practice ở phần dưới trang 943 không được đưa vào fragment tóm tắt.

Các mục giữ các công thức (28.12)–(28.32), Ví dụ 28.6 và 28.7–28.12, Chiến lược 28.2, bốn câu tự kiểm tra, Bảng 28.1, ứng dụng MRI, cáp đồng trục và hạt nano. Phần tóm tắt chứa đủ hàng 28.1–28.8, toàn bộ bảng phân bố trường và đồ thị vật liệu từ.

## Phép tính và kiểm tra độc lập

Suite `raw_materials/physics/verify_chapter28_05_08.py` dùng NumPy và số học chuẩn, không dùng SymPy. Tất cả kiểm tra đều qua:

- Ví dụ 28.6: $B(0{,}80\,\mathrm m)=1{,}130973\times10^{-4}\,\mathrm T$, $B(0)=5{,}23599\times10^{-4}\,\mathrm T$, $\mu=565{,}487\,\mathrm{A\,m^2}$. Tích phân vectơ tại hai phần tử đối diện cho thành phần trục cùng dấu và thành phần ngang trái dấu. Vị trí $x=\pm\sqrt3a$ cho đúng tỉ số trường $1/8$.
- Định luật Ampere: Tích phân số trường của dây dài trên một ellipse bao dây cho $\mu_0I$; ellipse lệch tâm không bao dây cho tích phân xấp xỉ 0 dù trường trên đường không bằng không.
- Ứng dụng Ampere: Trường bên trong/ngoài dây trụ liên tục tại mặt dây; tích phân ống dây khớp $\mu_0 nLI$; cáp đồng trục có dòng tổng bao bằng không.
- Vật liệu từ: Tính lại $\mu_B=9{,}2740101\times10^{-24}\,\mathrm{J/T}$; Ví dụ 28.11 cho $|U|_{\max}=1{,}39110\times10^{-23}\,\mathrm J$, $K=6{,}21292\times10^{-21}\,\mathrm J$ và tỉ số $0{,}2239\%$.
- Ví dụ 28.12: Với dữ kiện đầy đủ trước khi làm tròn, $\mu=6{,}4\,\mathrm{A\,m^2}$ và trường xa là $1{,}28\times10^{-3}\,\mathrm T$. Kết quả có một chữ số có nghĩa là $6\,\mathrm{A\,m^2}$ và xấp xỉ $1\times10^{-3}\,\mathrm T=10\,\mathrm G$, như đáp số trong ví dụ.

Kiểm tra MathJax theo cấu hình của repo đo 287 công thức inline, bề rộng lớn nhất 32,8 ex (không công thức nào vượt 38 ex). Cả 50 công thức hiển thị đều không vượt 26,9 ex.

## Ranh giới vật lý được giữ rõ

- Công thức trường vòng (28.15), (28.16), (28.18) chỉ áp dụng trên trục.
- Định luật Ampere ở dạng dùng trong các ví dụ là dạng từ tĩnh: Dòng không đổi và không có điện trường biến thiên theo thời gian. Tích phân không phải công cơ học và không chứng minh lực từ là lực bảo toàn.
- Tích phân bằng không không kéo theo trường bằng không tại từng điểm. Phải dùng thêm đối xứng trong các trường hợp xuyến hoặc cáp đồng trục để kết luận độ lớn trường triệt tiêu.
- Trường ống dây thẳng và hình xuyến dùng các giả thiết quấn sít, đối xứng và gần lý tưởng. Trường tại đầu ống dây, trường rò của xuyến thực và trường trong lõi từ cần được phân biệt với kết quả lý tưởng.
- Mô hình quỹ đạo electron được đánh dấu là hình dung cổ điển sơ lược. Mômen spin là tính chất nội tại. Trong vật liệu sắt từ, $K_m$ không hằng và quan hệ từ hóa có thể phi tuyến, bão hòa và có trễ.
- Đáp số Example 28.12 được đối chiếu với phép tính trước làm tròn, tránh coi $6$ là giá trị chính xác hơn dữ kiện cho phép.

## Hình ảnh và cấu trúc

Các fragment 05–08 dùng đường dẫn `../img/young-28/...`; fragment 09 dùng `img/young-28/...`, theo vị trí include cuối cùng. Hình 28.11–28.29, MRI, cáp đồng trục, hạt nano và tám tài sản tóm tắt đã được cắt trong thư mục ảnh Chương 28. Không đăng ký module chú giải trong registry toàn cục.

Không sửa catalog, Wiki, wrapper, fragment ngoài phạm vi, bản PDF nguồn hay nội dung Git.
