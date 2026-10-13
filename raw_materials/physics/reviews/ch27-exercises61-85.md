# Rà soát bài tập chương 27.61–27.85

## Đối chiếu phạm vi

Đã đối chiếu trực tiếp bản PDF Young–Freedman ấn bản 15: trang in 913–917, tương ứng trang PDF 933–937. Tệp 15 chứa bài 27.61–27.80. Tệp 16 chứa bài 27.81–27.82 cùng toàn bộ đoạn BIO “Magnetic Fields and MRI” và ba câu MCAT 27.83–27.85.

Đã xác nhận bài 27.81 nằm trong phần Challenge Problems và có đủ dữ kiện hình học $d=25{,}0\,\mathrm{cm}$, $D=75{,}0\,\mathrm{cm}$; điện tích trên hình nguồn là $2{,}15\,\mu\mathrm{C}$. Bài 27.82 có tiêu đề “A Cycloidal Path” và dùng điện trường $+y$, từ trường ra khỏi trang. Đoạn MRI có hai đoạn văn mô tả và hình hai trạng thái spin, sau đó là đủ lựa chọn của câu 27.83–27.85.

## Kiểm tra tính toán

Tệp `verify_chapter27_61_85.py` chạy bằng Python chỉ thị với NumPy. Script đã kiểm tra các tích có hướng, lực tổng trên vòng kín, tích phân mômen vi phân, các phép hồi quy dữ liệu 27.76, đồ thị 27.77–27.78, tích phân vĩ tuyến 27.79, động học quỹ đạo 27.74/27.81, cùng đáp số số học ở câu MRI.

Lệnh chạy:

```powershell
& 'C:\Users\Ai\miniconda3\python.exe' -X utf8 raw_materials/physics/verify_chapter27_61_85.py
```

Kết quả hiện tại: `Chapter 27 exercises 27.61–27.85: numerical checks passed.`

## Cần xem lại trước khi tích hợp

- Bài 27.73 đã được tác giả, root và người rà chéo suy ra lại theo hai chặng. Mômen từ có μ = 2NIWR, h_top = R(1+π/2), hai nhánh mômen và thế năng liên tục. Công của mômen, điều kiện cân bằng bền và ngưỡng quay quá nửa vòng đã qua kiểm tra Python độc lập. Bản nháp trước đó không được dùng.
- Bộ 34 hình cuối chương đã được tạo tại `docs/vat-ly-2/bai-giang/img/young-27/` và liên kết cạnh đề bài. Lượt rà độc lập cuối đã sửa mép ảnh E27.25, P27.63, P27.65 và nhãn tọa độ dưới P27.71. Các hướng của P27.81 và phần mô tả trôi ngang P27.82 đã được đối chiếu lại với hình và phương trình chuyển động.
- Bài 27.62 và phần (a) của 27.63 là ước lượng. Đáp số của 27.62 ghi giả định đường kính moay-ơ $15\,\mathrm{cm}$. Phần 27.63 dùng thành phần ngang của từ trường Trái Đất tại $45^\circ$.
- Bài 27.68 đòi hỏi nêu mômen trên từng cạnh quanh trục $PR$, không chỉ mômen tổng. Hãy giữ phần chiếu mômen quanh trục bản lề tách biệt với mômen vectơ toàn khung.

## Kiểm tra định dạng

Mỗi bài dùng cặp `::: exercise` và `::: solution`; lời giải có tóm tắt, các bước hướng giải và phép tính. Cần rà lại thêm độ dài công thức inline theo ngưỡng 38ex và kiểm tra ký tự đầu câu sau dấu hai chấm khi tích hợp.

## Kết quả lượt rà cuối

Các câu kết luận 27.71, 27.81 và 27.82 đã giữ nhất quán chiều lực, trục tọa độ và hướng trôi. Bài 27.68 trả lời rõ ý (e). Bài 27.77 dùng giá trị chưa làm tròn cho tốc độ 831890,33 m/s, làm tròn thành 8,32×10⁵ m/s ở cả lời giải và bảng đáp số. Công thức Wiki Tích vô hướng được bẻ thành ba dòng, đồng thời sửa trường ví dụ trong ghi chú nhanh.
