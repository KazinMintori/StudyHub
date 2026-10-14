# Rà cuối chương 31

Phạm vi đối chiếu: Trang in 1018–1047, trang PDF 1038–1067. Đây là hồ sơ nội bộ, không đưa lời kể kiểm chứng vào bài giảng.

## Nội dung và nơi đến

- Notes có lời mở, sáu mục, chín ví dụ, 37 công thức đánh số, sáu câu tự kiểm tại vị trí giảng và bảy đơn vị tổng kết.
- Tab Bài tập có 12 bài luyện tập hướng dẫn, một bài cầu nối, 19 câu thảo luận và 72 bài đánh số. Giữ các phần nhỏ, dữ kiện, lựa chọn MCAT và hình được dẫn trong đề.
- 104 lời giải được gập riêng. Mỗi lời giải có Tóm tắt đề bài, Hướng đi với tính chất, công thức và lý do sử dụng, rồi các bước giải.
- Có 11 Slides, sáu nhóm Cheatsheet với 21 mục chỉ gồm định nghĩa, tính chất, công thức, điều kiện và ý nghĩa ký hiệu. Có 10 Wiki mới.

## Hình và lời giải cần biểu diễn

48 PNG trích trực tiếp từ PDF giữ nguyên màu, nét, chữ, mũi tên và bố cục. Mỗi ảnh đã được so sánh pixel với đúng vùng PDF trong verify_chapter31_source_images.py. Hồ sơ tọa độ và hash nằm tại qa/physics/chapter31/source-image-integrity.json.

Đề Q31.4, Q31.6, 31.21 và 31.49 giữ lại hình lý thuyết được dẫn. Các hình cuối chương P31.40, 31.44, 31.47, 31.48, 31.53, 31.62, 31.63, 31.65 và 31.66 xuất hiện đúng bài. Hình bài cầu nối được trích riêng.

Năm SVG bổ sung trình bày giản đồ bài 31.12, đồ thị bài 31.49–31.50, chín khe của bài 31.53 và giản đồ dòng của bài 31.54. Các SVG nằm trong lời giải và đi cùng hình nguồn. Hai đồ thị điện áp của bài 31.50 thể hiện hai vị trí đỉnh khác nhau.

## Hiệu chỉnh đã kiểm lại

1. Giữ 250 microampe ở Ví dụ 31.2.
2. VP31.3.4 thiếu dữ kiện độc lập cho điện áp tụ và điện dung. Lời giải nêu rõ giới hạn dữ kiện, không thêm điều kiện điện áp tụ bằng điện áp điện trở.
3. VP31.7.4 dùng điện dung in 0,440 microfarad. Góc pha âm và điện trở khoảng 103,10 ohm.
4. Q31.8 xét cả điện áp tức thời điện trở. Q31.14 biện luận đủ sáng hơn, tối hơn và không đổi. Q31.18 giữ ngoại lệ điện kháng có tỉ số 5/8.
5. Bài 31.14 chọn rõ gốc pha dòng điện. Tại 20 ms, điện áp nguồn là −22,6957 V và điện áp tụ là −39,5564 V. Tổng tức thời thỏa Kirchhoff.
6. Bài 31.40 giữ điện áp biên độ 30 V. Năm vôn kế đọc giá trị hiệu dụng, nên không đổi dữ kiện thành nguồn hiệu dụng 30 V.
7. Bài 31.44 dùng thông số thiết bị thực tế dưới dạng tham số. Phân biệt dòng tải với dòng từ hóa, chiều dài cuộn dây với chiều dài đường từ và giả thiết dạng sóng dòng.
8. Bài 31.53 có 10 bản xen kẽ tạo chín khe song song. Các kết quả là góc 72,7 độ, tần số 918 kHz ở góc 120 độ và điện áp ra 5,77 V ở cộng hưởng mới.
9. Bài 31.57 giữ hai tần số góc dương khoảng 2781,43 và 28762,19 rad/s. Điều kiện là hệ số công suất bằng một nửa, không phải công suất bằng nửa cực đại cộng hưởng.
10. Bài 31.59–31.60 xét tỉ số điện kháng tại tần số đang hoạt động. Không đồng nhất điện kháng hiện tại với giá trị tại cộng hưởng.
11. Bài 31.65 phân biệt −3,0 dB chính xác với quy ước nửa công suất. Bài 31.66 giữ độ tự cảm 1,00 microhenry.
12. Bài 31.68 xét đủ miền điện trở dương, điều kiện có đỉnh hữu hạn, các giới hạn đơn điệu và trường hợp không tổn hao.

## Bằng chứng kiểm tra

Các bộ Python kiểm chín ví dụ, các câu tự kiểm, 12 bài luyện tập, bài cầu nối, 72 bài đánh số và 19 lập luận thảo luận. Bộ kiểm nâng cao xác nhận đa thức đạo hàm và các giới hạn ở bài 31.68. Các báo cáo được liên kết trong qa/physics/chapter31/numeric-checks.json.

721 công thức hiển thị và 2541 công thức nội dòng qua kiểm tra độ rộng. Ba công thức nội dòng còn gây tràn ở 320 px đã được tách tại quan hệ suy ra hoặc thành các biểu thức tương đương ngắn.

135 lượt trình duyệt đã qua ở 320, 360, 375 và 1440 px, cùng bảy lần đổi bề rộng trực tiếp. Có đủ 104 đề và 104 hộp lời giải ban đầu gập, ảnh có chú thích, không tràn công thức và không có lỗi JavaScript. Bản xem thử riêng chỉ nạp danh mục hai môn Vật lý, giữ nguyên dữ liệu chương, hình, bộ hiển thị toán và CSS.

39 kiểm thử skill và bảy kiểm thử bộ hiển thị toán đã qua. Build toàn bộ và triển khai được giao cho GitHub Actions theo quy định mới. Trạng thái xuất bản được ghi riêng sau push.

Hai worktree Antigravity đã hết ba lần gọi và được giữ nguyên. Nội dung được nhận qua bản sao ổn định, rồi sửa, tính lại và rà thủ công trước khi tích hợp.
