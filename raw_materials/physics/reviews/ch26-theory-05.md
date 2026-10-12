# Ranh giới nguồn và rà soát mục 26.5

## Phạm vi nguồn

Mục 26.5, “Power Distribution Systems”, bắt đầu trên trang in 863, tương ứng PDF một-based 883 (`qa/physics/full-source/pdf-0883.txt`). Nội dung liên tục qua trang in 864–866, tương ứng PDF 884–886. Phần cuối thuộc mục là Ví dụ 26.14, câu “Test Your Understanding of Section 26.5” và lời giải trên trang in 866. Phần tóm tắt chương bắt đầu ở trang in 867, PDF 887, nên không thuộc bản thảo này.

Trang in 863 mở đầu bằng câu hỏi và lời giải “Test Your Understanding of Section 26.4”, trước tiêu đề 26.5. Hai phần đó được loại khỏi bản dịch mục 26.5. Không đưa nội dung tóm tắt chương ở trang 867 vào cuối bài.

Đã đối chiếu năm bản trích toàn trang `pdf-0883.txt` đến `pdf-0887.txt` và render trực tiếp PDF nguồn, trang một-based 883–886. Bản thảo giữ các ví dụ hệ thống $120\,\mathrm V$ và $240\,\mathrm V$, bảng cỡ dây gauge, giải thích cầu chì/bộ ngắt, dây pha/trung tính/bảo vệ, GFCI, hệ thống ba dây, ví dụ điện ô tô, đổi kWh, Ví dụ 26.14 và câu hỏi cuối mục. Các mức điện áp, cỡ dây, định mức dòng và giá điện được đặt trong mô hình ví dụ của phần, không trình bày thành quy định hiện hành tại địa phương.

## Bản đồ hình và nhãn cần gắn

| Hình nguồn | Trang in / PDF | Crop dự kiến | Nội dung và nhãn cần chuyển ngữ |
| --- | --- | --- | --- |
| 26.24 | 863 / 883 | `docs/vat-ly-2/bai-giang/img/young-26/hinh-26-24.png` | Công tơ, nguồn điện lực, cầu chì chính, hai mạch nhánh, dây pha, dây trung tính, nối đất, ổ cắm, công tắc, đèn và cầu chì từng nhánh. Chú thích ngoài hình nêu rằng sơ đồ chỉ vẽ hai nhánh, hệ thống thực tế trong mô tả nguồn có thể có 4–30 nhánh, dây bảo vệ bị lược bỏ. |
| 26.25 | 864 / 884 | `docs/vat-ly-2/bai-giang/img/young-26/hinh-26-25.png` | (a) Cầu chì với dây hợp kim chì–thiếc bên trong vỏ trong suốt. (b) Bộ ngắt mạch với công tắc chuyển trạng thái khi quá dòng. |
| 26.26 | 865 / 885 | `docs/vat-ly-2/bai-giang/img/young-26/hinh-26-26.png` | So sánh phích hai chấu và ba chấu, dụng cụ có lỗi cách điện, đường dòng sự cố, dây bảo vệ màu xanh, người chạm vào vỏ, đường nối đất. Caption cần giữ đây là cơ chế giảm nguy cơ điện giật trong mô hình, không bảo đảm tuyệt đối rằng người chạm vào không thể bị điện giật. |

Các crop trên chưa có trong thư mục ảnh khi viết báo cáo này. Vì vậy, đường dẫn trong bản dịch là đích dự kiến, còn trạng thái crop và chú giải nhãn trên ảnh đang chờ root cung cấp. Caption tiếng Việt trong `05-he-thong-phan-phoi-dien.md` đã được viết độc lập với chữ nằm bên trong crop để tránh lặp nội dung.

## Phép tính đã kiểm tra

Chạy `python -I raw_materials/physics/verify_chapter26_05.py`, tất cả kiểm tra số học đều qua. Script tính lại dòng/điện trở của bóng $100\,\mathrm W$ và thiết bị $1500\,\mathrm W$, ví dụ tải $1800\,\mathrm W$, $1300\,\mathrm W$, $100\,\mathrm W$ trong Ví dụ 26.14, tỉ số nhiệt $I^2R$ khi so dòng $40\,\mathrm A$ với $20\,\mathrm A$, đổi $1\,\mathrm{kW\cdot h}$ sang joule, chi phí minh họa $0{,}10$ đô la/kWh và dòng của đèn pha $100\,\mathrm W$ ở $13\,\mathrm V$.

Kết quả chính: Ví dụ 26.14 cho tổng dòng $26{,}6667\,\mathrm A$, vượt $20\,\mathrm A$. Với điện trở dây giữ nguyên, $40\,\mathrm A$ tạo công suất nhiệt gấp bốn lần ở $20\,\mathrm A$. Thiết bị $1500\,\mathrm W$ dùng một giờ tiêu thụ $1{,}5\,\mathrm{kW\cdot h}=5{,}4\times10^6\,\mathrm J$ và có chi phí minh họa $0{,}15$ đô la ở đơn giá đã nêu.

## Giới hạn rà soát

Phạm vi là văn bản mục 26.5 và các phép tính được mã hóa trong verifier. Chưa thể kiểm tra trực quan crop, nhãn trên ảnh, khung công thức theo kích cỡ điện thoại, hoặc trang sau tích hợp vì các crop đang chờ. Không kiểm tra build và không đưa ra kết luận về quy chuẩn lắp đặt điện hiện hành ở bất kỳ khu vực nào.
