# Rà soát nguồn cuối Chương 28

## Phạm vi và cách kiểm tra

Đã rà các fragment 00–13, sổ nguồn và các verifier hiện có. Đối chiếu trực tiếp với PDF chương 28, đặc biệt các hình có hướng dòng và trang in 947–949. Chạy các bộ kiểm chứng 01–04, 05–08, bài 01–30, bài 31–60, bài 61–83, câu hỏi thảo luận và Guided Practice. Tất cả đều chạy qua. Một số lệnh in thêm cảnh báo môi trường `Failed to find real location of C:\Users\Ai\miniconda3\python.exe`, nhưng từng script vẫn hoàn tất và báo kết quả PASS.

Kiểm kê cấu trúc tìm thấy 12 Guided Practice, 20 câu hỏi thảo luận, 30 bài trong fragment 12, 30 bài trong fragment 13, cùng 30 cặp exercise/solution cho mỗi fragment bài tập. Fragment 10 có 12 bài hướng dẫn và một lời giải cho bài cầu nối. Phần thảo luận ghi đủ 20 cặp đề/lời giải. Hình và nhãn được rà theo các báo cáo phạm vi; không xem con số tổng như bằng chứng thay cho việc đọc hình.

## Các sai lệch nguồn đã phát hiện và trạng thái

| Mức | Vị trí | Phát hiện và sửa đề nghị |
|---|---|---|
| Đã sửa bởi root | `translations/chapter-28/12-bai-tap-01-30.md`, lời giải 28.25, Tóm tắt đề bài | Đề và Hình E28.25 cho dây đứng mang dòng $12{,}0\,\mathrm A$, trong khi Tóm tắt trước đó ghi $15{,}0\,\mathrm A$. Các trường $25{,}0\,\mu\mathrm T$, $16{,}0\,\mu\mathrm T$, $41{,}0\,\mu\mathrm T$ và $9{,}0\,\mu\mathrm T$ khớp với $12{,}0\,\mathrm A$. Tóm tắt đã được sửa về 12,0 A. |
| Đã sửa bởi root | `translations/chapter-28/12-bai-tap-01-30.md`, alt ảnh 28.29 | Alt text cũ ghi hai dòng “cùng chiều”, trong khi Hình E28.29 cho dòng trên sang phải và dòng dưới sang trái. Alt đã được sửa để nêu hai dòng ngược chiều. Đề và lời giải hiểu đúng cấu hình ngược chiều, lực đẩy. |
| Đã sửa bởi root | `translations/chapter-28/12-bai-tap-01-30.md`, bài 28.21(b) và lời giải 28.24 | Bài 28.21(b) đã được chỉnh để nói rõ hai trường cùng chiều nên cộng độ lớn. Tóm tắt 28.24 đã được sửa để mô tả bốn dây nằm trong mặt phẳng hình, chạy dọc các cạnh hình vuông, với dòng cần tìm hướng xuống. |
| Đã sửa trong lượt này | `translations/chapter-28/12-bai-tap-01-30.md`, bài 28.7 | Ảnh phóng to của PDF trang in 945 cho thấy khoảng cách ghi $6{,}60\,\mu\mathrm m$, không phải $6{,}60\,\mathrm{mm}$. Đề và Tóm tắt đã đổi sang micromet. Với tốc độ $3{,}30\,\mathrm{km/s}$, trường phần (c) đúng là $1{,}21\times10^{-12}\,\mathrm T=1{,}21\,\mathrm{pT}$. Kết quả trước đó dùng đơn vị mm và nhỏ hơn một triệu lần. Đáp số phụ lục không được dùng để thay dữ kiện nhìn thấy trong hình nguồn. |

Các mâu thuẫn đã liệt kê trong rà chéo trước được đối chiếu lại: E28.3 dùng góc $60^\circ$ đo từ phương ngang nên góc với vận tốc hướng lên là $30^\circ$/$150^\circ$ và trường A, B đều hướng ra khỏi trang; E28.8 cho hai đóng góp cùng hướng vào trang, tổng $1{,}21\,\mathrm{mT}$; E28.16 hướng bắc; E28.23(c) hướng trái; E28.28 cho dây giữa lực tổng bằng không và hai dây ngoài bị đẩy ra xa dây giữa. Các con số và hướng này phù hợp với verifier hiện có.

## Hình và bố cục

- P28.58 trước đây bị cắt mất dây dưới tại $y=-a$. Đã mở rộng tọa độ crop trong `scripts/prepare-physics28-exercise-assets.py` từ `y2=485` lên `y2=515`, dựng lại ảnh và xác nhận đủ hai dây, trong đó dây trên có dòng ra trang và dây dưới có dòng vào trang.
- P28.61 trước đây bị cắt dây dẫn dưới và mũi tên dòng sang trái. Đã mở rộng crop từ `y2=370` lên `y2=400`, dựng lại và xác nhận cả hai dây dẫn, dây treo và hướng dòng đều hiện đủ.
- Đã nhìn lại P28.59, P28.60 và P28.62. Các crop này giữ đủ nội dung cần cho đề.

## Chuẩn hóa Hướng đi trong fragment 13

Theo yêu cầu tích hợp của root, đã đổi 30 đoạn Hướng đi trong `translations/chapter-28/13-bai-tap-31-60.md` từ đoạn văn thành gạch đầu dòng. Các câu hướng dẫn được tách theo từng ý, giữ nguyên chữ và công thức. Không đổi dữ kiện, phép tính hay phần lời giải. Kiểm kê xác nhận fragment vẫn có 30 exercise và 30 solution.

Đã xử lý các gợi ý biên tập của công cụ rà câu trong fragment 10–12. Các đề có nhiều tiểu mục nay tách thành từng phần dễ đọc, câu nhiều ý được nối hoặc chia câu phù hợp, và phần Hướng đi nêu lý do chọn công thức. Fragment 13 đã được rà lại sau lượt gạch đầu dòng. Lệnh `review_teaching_text.py --format text` trên 10–13 kết thúc bằng “Không có gợi ý nào”. Nhật ký của lượt rà là `qa/physics/chapter28/teaching-review-10-13.log`.

## Giới hạn

Đây là lượt audit bổ sung tập trung vào tính toàn vẹn nguồn, các trường hợp dễ sai hướng, crop và hành văn trong phạm vi 10–13. Bảy verifier hiện có chạy qua sau khi chỉnh câu. Không chạy build website hoặc kiểm tra hiển thị trên trình duyệt.

## Verifier véc-tơ độc lập bổ sung

Đã thêm `raw_materials/physics/verify_chapter28_basic_cross.py`. Suite dựng lại trường và lực từ tọa độ cùng dòng điện có dấu, không nhập hoặc gọi verifier khác. Nó kiểm tra E28.3, E28.7, E28.8, E28.16, E28.19, E28.21, E28.23–E28.25, E28.28–E28.29, các dòng bao trong E28.38, lực E28.49–E28.50, trường E28.58–E28.59, lực vòng P28.60 và lực tương hỗ VP28.2.2. Kết quả được lưu ở `qa/physics/chapter28/basic-cross.json`.

Suite chạy qua 18 cấu hình. Không phát hiện sai lệch mới trong các fragment đã đối chiếu. E28.7 dùng $6{,}60\,\mu\mathrm m$ theo ảnh nguồn và cho $1{,}2121\,\mathrm{pT}$. VP28.2.2 cho hai lực bằng nhau, hướng vào nhau. P28.60 có lực tổng hướng lên, còn lực ngang trên hai cạnh ngắn triệt tiêu.
