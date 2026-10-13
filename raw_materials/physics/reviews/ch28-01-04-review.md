# Rà soát nguồn Chương 28.1–28.4

## Phạm vi đã soạn

Năm mảnh nguồn trong `translations/chapter-28/` bao quát phần mở đầu và các Mục 28.1–28.4 trên trang in 918–927 (PDF 938–947). Nội dung giữ đủ 8 mục tiêu học tập, kiến thức tiên quyết, 4 mục chính, các tiểu mục, 11 phương trình đánh số (28.1)–(28.11), 5 ví dụ đánh số, 4 câu tự kiểm tra có đáp án, Chiến lược giải 28.1, ứng dụng từ trường hành tinh, điều kiện mô hình, giới hạn đo trực tiếp phần tử dòng điện, và phần SI về μ₀ trước/sau năm 2018. Phạm vi dừng trước Mục 28.5.

Các mảnh đã tạo:

- `00-mo-dau.md`
- `01-dien-tich-chuyen-dong.md`
- `02-phan-tu-dong-dien.md`
- `03-day-thang.md`
- `04-luc-hai-day.md`

## Hình và nhãn

Đã tạo 14 ảnh lý thuyết cho phạm vi này: ảnh mở chương, Hình 28.1–28.10, ảnh ứng dụng hành tinh, và hai sơ đồ tự kiểm tra 28.3–28.4. Mỗi ảnh được liên kết trong mảnh nguồn bằng đường dẫn tương đối và chú thích tiếng Việt. Mô-đun chú giải có 14 mục tương ứng, không lặp nhãn tiếng Anh. Các crop được so trực tiếp với trang nguồn; ranh giới tránh phần văn xuôi hoặc chú thích ngoài hình, đồng thời giữ nhãn bên trong hình.

## Kiểm tra tính toán

`verify_chapter28_01_04.py` chạy thành công. Script kiểm tra giá trị gần đúng của μ₀ và liên hệ với c; hướng và tỉ số lực ở Ví dụ 28.1; độ lớn, hướng ở Ví dụ 28.2; thứ tự tự kiểm tra 28.2; tích phân dây hữu hạn bằng tích phân Simpson số; giới hạn dây dài và Ví dụ 28.3; chồng chất tại ba điểm và giới hạn xa trong Ví dụ 28.4; cùng lực trên đơn vị chiều dài và chiều lực ở Ví dụ 28.5. Script còn kiểm tra chiều trôi của hạt tải âm và cấu hình dùng để định nghĩa ampere trước năm 2018.

## Giới hạn kiểm tra

Đây là kiểm tra nguồn riêng cho các Mục 28.1–28.4, không phải xác nhận build trang công khai. Không sửa wrapper, catalog, registry, Wiki hoặc tài nguyên ngoài phạm vi này. Các kiểm tra phép tính xác nhận những giá trị và chiều được liệt kê ở trên, không thay cho rà soát sư phạm toàn chương.

## Rà soát độ rộng công thức lần hai

Sau rà chéo MathJax, các bước tích phân ở Mục 28.3 và các tổng véc-tơ được dàn lại để mỗi dòng công thức không vượt quá 27ex. Kiểm tra riêng năm mảnh 00–04 bằng cùng thư viện Markdown-It/MathJax của dự án ghi nhận 0 công thức hiển thị rộng hơn 27ex và 0 công thức nội dòng rộng hơn 38ex khi đo biểu thức, loại cú pháp `\tag{...}` như bộ kiểm tra dự án. Bộ hiển thị tách số phương trình ra khỏi SVG công thức, nên cả 11 thẻ số vẫn được giữ nguyên trong các mảnh nguồn.
