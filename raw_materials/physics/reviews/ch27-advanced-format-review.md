# Rà định dạng toán: Bài 27.61–27.85

Phạm vi rà soát gồm hai bản dịch 27.61–27.80 và 27.81–27.85. Đợt này chỉ sửa bố cục công thức và lỗi dấu ngoặc TeX bị thiếu trong câu 27.63. Không thay dữ liệu bảng hoặc kết quả vật lý.

## Kết quả

- Chuẩn hóa các chuỗi phép tính dài thành khối `aligned`, giữ các bước suy luận và đơn vị. Các trường hợp dài ở câu 27.61, 27.65, 27.69, 27.71, 27.73, 27.74, 27.77–27.80 và 27.81–27.85 được bẻ dòng tại phép toán hoặc dấu bằng.
- Ở 27.73, đặt rõ `\theta=h/R-1` cho chặng thứ hai. Các biểu thức mômen và thế năng được viết lại theo biến này, đồng thời giữ khai triển từng hạng tử của thế năng.
- Câu 27.63 có lỗi trích xuất `$10\,\mathrm{cm$`; đã khép ngoặc thành `$10\,\mathrm{cm}$` để TeX phân tích đúng.
- Các nhãn `**Hướng đi:**` đều đứng riêng trước danh sách gạch đầu dòng. Dấu mở/đóng `$$` đứng trên dòng riêng.

## Kiểm tra MathJax

Đã chuyển từng công thức qua MathJax CHTML với toàn bộ gói TeX. Không công thức nào báo lỗi phân tích cú pháp. Đo chiều rộng khối display qua độ rộng MathJax và quy đổi gần đúng `1 em = 2,33 ex`. Inline được đo dưới dạng hàng `aligned` ở `textstyle`, tạo cận trên bảo thủ cho biểu thức nội dòng.

| Tệp | Display | Inline | Display rộng nhất | Inline cận trên rộng nhất | Lỗi TeX |
|---|---:|---:|---:|---:|---:|
| `15-bai-tong-hop-61-80.md` | 69 | 550 | 27,2 ex | 33,9 ex | 0 |
| `16-bai-nang-cao-mcat.md` | 10 | 112 | 26,8 ex | 25,8 ex | 0 |

Cả hai giá trị display đều dưới 30 ex, các giá trị inline đều dưới 38 ex.

## Dấu vân tay nguồn

SHA-256 của PDF nguồn được dùng trong đợt rà:

`raw_materials/physics/source/young-freedman-15.pdf`

`F4EA22DC8D5113F47EC8FD8A2B9F71F7BE78EE3DB069971AACE4B7CDA04175FF`

SHA-256 sau khi định dạng:

- `15-bai-tong-hop-61-80.md`: `7FC3C84ABF1AAC90EE99BA1BCCC83EB693FFBA5723F42D10D4D5CF381A8F7461`
- `16-bai-nang-cao-mcat.md`: `EAC3727A48A21E4CE645EF096E97A34791CFFD7A8A038089F79537A20C028819`
