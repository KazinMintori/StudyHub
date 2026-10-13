# Rà chéo độc lập Bài tập 28.61–28.75

## Nguồn đã đối chiếu

Đối chiếu đề và hình trên trang in 949–951 của *University Physics with Modern Physics*, ấn bản 15. Các trang tương ứng số trang PDF vật lý 969–971. Đã đọc toàn bộ ba trang render ở 120 dpi và so từng đề 28.61–28.75 với `translations/chapter-28/14-bai-tong-hop-61-75.md`. File bài tập không được sửa trong lần rà này.

## Kết quả đối chiếu đề

Đủ 15 đề, giữ các dữ kiện, hình học, các phần a–g và yêu cầu về độ lớn/chiều. Các điểm cần chú ý đã được kiểm tra trực tiếp:

- 28.61: Dây treo dài 4,00 cm, khối lượng dài 0,0125 kg/m, hai dòng ngược chiều và góc 6,00° với phương thẳng đứng. Khoảng cách giữa dây lấy bằng hai lần độ lệch ngang.
- 28.62–28.64: Chiều dòng trên hai bán nguyệt và hai cung 120° khớp hình nguồn. Các đoạn nối theo bán kính không đóng góp tại tâm. Chiều trường ở 28.64 là vào trang giấy.
- 28.63 và 28.67: Mật độ dòng có phụ thuộc bán kính đúng như đề. Ở 28.63, mật độ điểmwise phân kỳ như 1/r tại trục, nhưng tích phân dòng vẫn hội tụ.
- 28.65–28.70: Điều kiện dây vô hạn, hình học đoạn bán vô hạn, dòng vòng, hai mặt dòng, các điểm P/R/S và chiều trường được giữ đúng.
- 28.71–28.72: Mô hình vỏ trụ tích điện quay, đĩa nhỏ, phép đọc đồ thị và quy ước chiều dòng cuộn dây được giữ.
- 28.73–28.75: Dữ liệu Hall, khoảng cách đo từ mặt cáp, hai lò xo tác dụng lên mỗi thanh, mô hình dây dài, mật độ plasma và lớp điện tích mặt khớp đề.

## Rà soát định lượng và chiều

Chạy `verify_chapter28_61_83.py`: thành công. Các kết quả liên quan trong phạm vi gồm dòng 28.61 xấp xỉ 23,2 A; trường 28.64 có độ lớn 4,19 μT và hướng vào trang; đồ thị 28.72 cho ước lượng khoảng 1,33×10³ và 2,67×10³ vòng; dữ liệu 28.73 cho I xấp xỉ 64,9 A và R xấp xỉ 1,19 cm; 28.74 cho l₀ xấp xỉ 8,34 mm, k xấp xỉ 0,0656 N/m, độ giãn khoảng 7,10 mm tại 12,0 A và dòng khoảng 15,5 A để giãn 1,00 cm; 28.75 cho áp suất ép khoảng 1,91×10⁻⁵ Pa.

Phần kiểm tra 28.63 xác nhận tổng dòng hữu hạn, trường liên tục tại r=a và giới hạn độ lớn trường khi r→0 hữu hạn dù chiều tiếp tuyến không xác định duy nhất trên trục. Phần 28.75 cộng độ lớn các lực hướng vào trên từng dải thành để tính áp suất. Tổng véc-tơ lực trên toàn ống bằng không do đối xứng, nhưng không làm áp suất triệt tiêu.

## Giới hạn

Đây là rà chéo nguồn và các phép kiểm tra số/chiều của verifier, không phải biên tập lại lời giải 61–75 hay xác nhận toàn bộ chương. Không sửa `14-bai-tong-hop-61-75.md`, `15-nang-cao-mcat.md` hoặc file công khai.
