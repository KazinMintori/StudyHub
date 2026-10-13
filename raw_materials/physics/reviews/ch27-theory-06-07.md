# Rà soát đối chiếu: Mục 27.6 và 27.7

## Ranh giới trong PDF nguồn

Manifest của Young–Freedman 15e xác định các mục như sau:

| Mục nguồn | Tiêu đề | Trang in | Trang PDF |
| --- | --- | --- | --- |
| 27.6 | Magnetic Force on a Current-Carrying Conductor | 893–896 | 913–916 |
| 27.7 | Force and Torque on a Current Loop | 897–902, đến hết câu tự kiểm tra | 917–922 |

Mục 27.8, *The Direct-Current Motor*, bắt đầu ở cuối trang in 902, sau đáp án câu tự kiểm tra của 27.7. Nội dung bài giảng 06 và 07 theo hai ranh giới này, không lấy số thứ tự tệp làm số mục trong giáo trình.

## Kiểm tra trực tiếp trên trang

Đã render và đọc trực tiếp PDF 913–922. Các hình và chiều véc-tơ đã đối chiếu gồm Hình 27.25–27.30 cho mục 27.6 và Hình 27.31–27.38 cho mục 27.7. Ảnh MRI là ô ứng dụng sinh học trên trang 898, không có số hình riêng. Câu tự kiểm tra 27.7 dẫn Hình 27.13c từ phần trước.

Hai tệp đã giữ các ý, phương trình, ứng dụng, ví dụ có lời giải và câu tự kiểm tra của đúng hai mục:

- Mục 27.6 có suy ra lực tổng hợp từ lực lên hạt tải điện, độ lớn và véc-tơ lực trên dây thẳng, quy tắc đổi chiều, tích phân lực trên dây cong, lưu ý dòng điện là vô hướng, ứng dụng loa, Ví dụ 27.7 và 27.8, phần nâng thanh bằng từ trường, cùng câu hỏi chọn chiều pin trên thanh trượt.
- Mục 27.7 có lực tổng hợp bằng không nhưng mômen có thể khác không, vị trí cân bằng bền và không bền, mômen lưỡng cực, dạng véc-tơ của mômen lực, năng lượng thế, cuộn nhiều vòng và máy đo d’Arsonval, ứng dụng MRI, lực trong từ trường không đều, Ví dụ 27.9 và 27.10, cách sắt chưa nhiễm từ bị hút, cùng câu tự kiểm tra về cực của vòng dây.

## Tính lại độc lập

Chạy thành công `raw_materials/physics/verify_chapter27_06_07.py` bằng Python. Chương trình kiểm tra véc-tơ lực và chiều đảo khi đảo dòng hoặc từ trường, lực trên cung bán nguyệt, tổng lực và mômen của vòng chữ nhật, số liệu cuộn dây tròn và biến thiên năng lượng.

- Ví dụ 27.7 cho lực $42{,}426\,\mathrm{N}$ hướng lên. Khi thanh vuông góc từ trường, lực cực đại là $60{,}0\,\mathrm{N}$, cũng hướng lên.
- Với cung bán nguyệt, thành phần ngang bằng không và thành phần dọc bằng $2IRB$. Cộng hai đoạn thẳng cho lực tổng hợp $IB(2R+L)$ hướng $+y$.
- Với vòng chữ nhật, tổng lực bằng không ở các góc đã thử, còn véc-tơ mômen trùng $\vec{\mu}\times\vec{B}$ và có độ lớn $NIAB|\sin\phi|$.
- Ví dụ 27.9 cho $\mu=1{,}178\,\mathrm{A\,m^2}$ và $\tau=1{,}414\,\mathrm{N\,m}$. Khi cuộn quay từ vuông góc sang song song với từ trường, $\Delta U=-1{,}414\,\mathrm{J}$, khớp Ví dụ 27.10.

## Tài nguyên hình chờ bước tích hợp

Các đường dẫn hình theo quy ước sẽ được trỏ tới `../img/young-27/`:

- Mục 27.6 dùng `hinh-27-25.png` đến `hinh-27-30.png`.
- Mục 27.7 dùng `hinh-27-31.png` đến `hinh-27-38.png`, cùng `ung-dung-mri.png` cho ô ảnh MRI.
- Câu tự kiểm tra 27.7 tham chiếu lại `hinh-27-13.png`.

Đã render các trang PDF nguồn 913–922 để kiểm tra hình và chiều véc-tơ. Bản render dùng rà soát nằm trong `raw_materials/physics/reviews/ch27-06-07-pages/`. Các tài sản minh họa tương ứng trong thư mục bài giảng `img/young-27/` chưa được tạo trong tác vụ này. Không sửa catalog hoặc nội dung site.

## Kiểm tra định dạng công thức

Đã chạy `scripts/audit-physics-math.mjs 27`. Không có công thức lỗi cú pháp hoặc quá rộng trong hai tệp 06 và 07. Báo cáo toàn chương còn phát hiện công thức rộng ở một số tệp trước đó của chương 27, không thuộc hai tệp trong phạm vi rà soát này.
