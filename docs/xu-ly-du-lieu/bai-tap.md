---
course: xu-ly-du-lieu
title: "Bài tập xử lý dữ liệu theo chương"
---

# Bài tập xử lý dữ liệu theo chương

Bài tập nằm trong từng bài giảng, cạnh phần kiến thức cần dùng. Hãy tự giải trước khi mở lời giải. Với bài thực hành trên dữ liệu bên ngoài, kết quả còn phụ thuộc bản dữ liệu, thời điểm chụp và quy tắc chọn hàng.

Trong tab **Bài tập**, các bộ thực hành được chia theo chủ đề. Mỗi đề nêu dữ liệu, việc cần làm và kết quả cần trả về. Phần lời giải mở đầu bằng cách làm từng bước, sau đó trình bày cách xử lý thích hợp khi làm việc với dữ liệu lớn hơn. Bảng output giúp đối chiếu kết quả của cả hai cách.

Các bộ dữ liệu nhỏ được ghi đầy đủ trong bài để có thể chạy lại ngay. Khi chuyển sang dữ liệu thật, hãy giữ cùng quy tắc về giá trị thiếu, ngày tháng, mẫu số và khóa ghép. Kết quả của dữ liệu minh họa không phải số liệu tổng kết của Santiago.

- [Chương 1. Công việc xử lý dữ liệu và môi trường Python](/xu-ly-du-lieu/bai-giang/bai-01-tong-quan-cong-cu-chinh-sach-ai.md#bai-tap)
- [Chương 2. Python, IPython và Jupyter Notebook](/xu-ly-du-lieu/bai-giang/bai-02-python-co-ban.md#bai-tap)
- [Chương 3. Cấu trúc dữ liệu, hàm và tệp](/xu-ly-du-lieu/bai-giang/bai-03-cau-truc-du-lieu-ham-tep.md#bai-tap)
- [Chương 4. Mảng NumPy và tính toán trên mảng](/xu-ly-du-lieu/bai-giang/bai-03-numpy.md#bai-tap)
- [Chương 5. Series, DataFrame và chỉ mục trong pandas](/xu-ly-du-lieu/bai-giang/bai-04-lam-quen-pandas.md#bai-tap)
- [Chương 6. Nạp, lưu trữ và truy xuất dữ liệu](/xu-ly-du-lieu/bai-giang/bai-06-ket-noi-truy-xuat-du-lieu.md#bai-tap)
- [Chương 7. Làm sạch, chuẩn bị và xử lý chuỗi](/xu-ly-du-lieu/bai-giang/bai-10-lam-sach-du-lieu.md#bai-tap)
- [Chương 8. Chỉ mục phân cấp, ghép bảng và chuyển dạng](/xu-ly-du-lieu/bai-giang/bai-08-ghep-bang-chuyen-dang.md#bai-tap)
- [Chương 9. Trực quan hóa dữ liệu và đọc biểu đồ](/xu-ly-du-lieu/bai-giang/bai-12-truc-quan-hoa-co-ban.md#bai-tap)
- [Chương 10. Tổng hợp dữ liệu và phép toán theo nhóm](/xu-ly-du-lieu/bai-giang/bai-10-tong-hop-theo-nhom.md#bai-tap)
- [Chương 11. Chuỗi thời gian](/xu-ly-du-lieu/bai-giang/bai-08-du-lieu-thoi-gian.md#bai-tap)
- [Chương 12. Từ bảng dữ liệu đến mô hình thống kê và dự đoán](/xu-ly-du-lieu/bai-giang/bai-12-mo-hinh-hoa.md#bai-tap)
- [Chương 13. Các bài toán phân tích dữ liệu và kiểm tra kết luận](/xu-ly-du-lieu/bai-giang/bai-14-ke-chuyen-bang-du-lieu.md#bai-tap)
- [Phụ lục A: NumPy nâng cao](/xu-ly-du-lieu/bai-giang/phu-luc-a-numpy-nang-cao.md#bai-tap)
- [Phụ lục B: Làm việc hiệu quả với IPython](/xu-ly-du-lieu/bai-giang/phu-luc-b-ipython.md#bai-tap)

## Dữ liệu thực hành

Các bài về chỗ ở và đánh giá dùng snapshot Santiago ngày 29/06/2026. Giá trong bản dữ liệu này tính bằng CLP mỗi đêm. Chọn đúng tệp theo trường dữ liệu mà bài yêu cầu.

| Tệp | Nội dung |
| --- | --- |
| [Bảng chỗ ở rút gọn](https://data.insideairbnb.com/chile/rm/santiago/2026-06-29/visualisations/listings.csv) | Một dòng cho mỗi chỗ ở, gồm giá, quận, loại phòng và số đánh giá. |
| [Bảng ngày đánh giá](https://data.insideairbnb.com/chile/rm/santiago/2026-06-29/visualisations/reviews.csv) | Mã chỗ ở và ngày của từng đánh giá. |
| [Bảng chỗ ở chi tiết, dạng gzip](https://data.insideairbnb.com/chile/rm/santiago/2026-06-29/data/listings.csv.gz) | Thêm tiện nghi, thông tin chủ nhà và các trường mô tả. |
| [Bảng đánh giá có văn bản, dạng gzip](https://data.insideairbnb.com/chile/rm/santiago/2026-06-29/data/reviews.csv.gz) | Thêm nội dung nhận xét để thực hành xử lý chuỗi. |

Bảng rút gọn có 18.534 chỗ ở và 690.112 dòng đánh giá. Trong bảng đánh giá có 204 dòng mang ngày sau 29/06/2026. Vì vậy, tên thư mục snapshot chưa đủ để bảo đảm mọi dòng nằm trước mốc phân tích. Bài yêu cầu giới hạn thời gian nào thì phải lọc rõ giới hạn đó.

Với phần biểu thức chính quy, có thể tải [321 cặp đầu vào và kết quả cần nhận của 20 bài regex](/materials/data-labs/regex-cases.json) để đối chiếu thêm các trường hợp rỗng, thiếu, Unicode và chuỗi gần giống mẫu.

## Tài liệu tham khảo

- [Inside Airbnb: Dữ liệu Santiago, snapshot 29/06/2026](https://data.insideairbnb.com/chile/rm/santiago/2026-06-29/visualisations/listings.csv).
- [IAI: Học liệu và notebook thực hành](https://courses.iaidev.com/programming-for-data-processing/2627-1/).
