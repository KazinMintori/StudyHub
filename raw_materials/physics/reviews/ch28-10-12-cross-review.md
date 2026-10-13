# Rà chéo độc lập: Fragment 10–12 chương 28

Ngày rà: 2026-10-13. Phạm vi gồm nội dung, giả thiết, dữ kiện, hướng vectơ, phép tính mẫu và cú pháp toán trong `10-luyen-tap-huong-dan.md`, `11-cau-hoi-thao-luan.md`, và `12-bai-tap-01-30.md`. Các trường hợp có hình được đối chiếu trực tiếp với asset hình đã trích và nội dung PDF gốc. Các phép tính nêu dưới đây được kiểm tra lại bằng Python và vectơ tọa độ. Đây là rà soát độc lập, không chỉnh sửa ba fragment.

## Lỗi cần sửa

| Mức | Vị trí | Phát hiện và hiệu chỉnh |
|---|---|---|
| P1 | `10-luyen-tap-huong-dan.md`, VP28.2.2 | Lời giải cuối nói hai lực đẩy nhau nhưng lời giải từng phần nói lực electron hướng về proton; chính kết luận từng phần đó mới đúng. Với proton ở x=0 chuyển động +y và electron ở x=d chuyển động −y: lực từ proton lên electron hướng −x, lực từ electron lên proton hướng +x. Hai lực hút nhau, cùng độ lớn xấp xỉ `1.13×10⁻²⁸ N`. Sửa câu “đẩy nhau” thành “hút nhau” và làm câu hướng dẫn nhất quán. |
| P1 | `12-bai-tap-01-30.md`, Bài 28.3 | Hình E28.3 ghi góc 60° từ phương ngang, trong khi vận tốc hướng thẳng lên. Vì vậy góc giữa vận tốc và vectơ vị trí là 30°/150°, và độ lớn `6.00×10⁻⁸ T` trong bản hiện tại là đúng. Tuy nhiên, quy tắc tích có hướng cùng dấu điện tích âm cho thấy trường tại cả A và B hướng ra khỏi trang; lời giải hiện ghi B vào trang. |
| P1 | `12-bai-tap-01-30.md`, Bài 28.8(a) | Tại gốc, trường do electron (y=5 nm, v sang trái) hướng vào trang, khoảng `471 μT`. Trường do proton (x=4 nm, v hướng xuống) cũng hướng vào trang, khoảng `736 μT`. Tổng đúng khoảng `1.21 mT` vào trang, không phải `265 μT` ra trang. Các phần (b), (c) trong lời giải có hướng và độ lớn phù hợp với hình. |
| P1 | `12-bai-tap-01-30.md`, Bài 28.23(c) | Hình E28.23(c) có hai dòng trên đi vào trang và hai dòng dưới đi ra trang. Tại tâm, thành phần y triệt tiêu, bốn thành phần x cùng hướng sang trái. Độ lớn `4.00×10⁻⁴ T` đúng, nhưng bản hiện tại ghi sang phải. |
| P2 | `12-bai-tap-01-30.md`, Bài 28.9 | Bước thế số cho điểm B dùng tử số `5.50×10⁻¹²` nhưng chia cho `0.149³` và ghi kết quả `1.67×10⁻⁸ T`; các số trên dòng không cho kết quả đó. Tử số phải có bậc `10⁻¹¹` để khớp phép tính và kết quả. Rà lại cách ghi đơn vị và phép thế số từ định luật Biot–Savart. |
| P2 | `12-bai-tap-01-30.md`, Bài 28.25 | Hình E28.25 và prompt đều cho dây đứng mang `12 A`, còn phần Tóm tắt ghi `15 A`. Các độ lớn `16 μT`, `41 μT`, và `9 μT` thực ra khớp với dòng `12 A`; sửa dữ kiện Tóm tắt, giữ các kết quả. |

## Kết quả các mục đã kiểm tra khác

- Bài 28.16: độ lớn `6.57 μT` hợp lý, nhưng hướng trường tại điểm phía trên dây cần là hướng bắc trong mặt phẳng ngang (dòng điện quy ước hướng tây do electron trôi hướng đông). Bản hiện tại ghi “thẳng xuống”.
- Bài 28.17: dòng `250 μA` khớp phép tính vật lý; phần đáp án in ở phụ lục nguồn ghi khác một hệ số 10, nên giữ sai khác này trong ghi chú riêng khi tích hợp.
- Bài 28.19: các giá trị thành phần và vectơ tổng hợp kiểm tra được: trường lần lượt khoảng `0.10 μT`, `2.19 μT` ở góc `46.8°` so với +x về phía +z, và `7.90 μT` theo +x.
- Bài 28.24–30: các kết quả định lượng và hướng chính đã rà qua đều nhất quán với hình, ngoại trừ dữ kiện Tóm tắt Bài 28.25 nêu trên. Bài 28.26 cho trường hữu hạn `2.86×10⁻⁵ T`, trường vô hạn `3.20×10⁻⁵ T`, chênh lệch 11.8% lấy trường hữu hạn làm mốc. Bài 28.27–30 có biểu thức lực/cân bằng đúng theo cấu hình hình.
- `10-luyen-tap-huong-dan.md`: VP28.2.2 là lỗi nội dung nêu trên. Những ví dụ được lấy mẫu về dây dài và định luật Ampere cho số liệu nhất quán. Chưa xác nhận toàn bộ từng dòng của mọi bài luyện tập bằng phép thế độc lập.
- `11-cau-hoi-thao-luan.md`: không phát hiện thêm lỗi vật lý rõ ràng trong các câu khái niệm đã đối chiếu; cần sửa các lỗi ở 10/12 trước khi gộp để tránh kết luận mâu thuẫn giữa phần giảng và bài tập.

## Kiểm tra định dạng các fragment do người rà soạn

Đã sửa display quá dài trong fragment 05, chuyển điều kiện bằng lời khỏi `cases` ở fragment 06, và tách tham chiếu phương trình ở phần tóm tắt fragment 09. Sau đó chạy `node scripts/audit-physics-math.mjs 28`: toàn bộ tài liệu chương 28 có 566 display, 2.135 inline, 0 lỗi cú pháp TeX. Các cảnh báo độ rộng trong lần chạy này thuộc fragment 10, 14, và 15; không có cảnh báo trong các fragment thuộc phạm vi của người rà soạn là 05–09 hoặc 13. Các cảnh báo ngoài phạm vi gồm display dài nhất được ghi nhận 40.664ex ở fragment 10; các fragment 14/15 cũng có display trên 27ex. Parser chấp nhận display ở Bài 28.21.

Phạm vi rà chéo 10–12 tập trung vào các ví dụ, hình có hướng vectơ, dữ kiện dễ lệch giữa đề và hình, và kết quả số được kiểm tra độc lập. Các vấn đề ở bảng trên đã được chuyển cho root; tài liệu này ghi lại cơ sở và giới hạn rà soát.
