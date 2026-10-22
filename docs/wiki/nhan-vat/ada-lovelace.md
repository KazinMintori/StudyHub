---
title: "Ada Lovelace: Từ con số đến ký hiệu"
prev: false
next: false
---

# Ada Lovelace: Từ con số đến ký hiệu

Một máy tính xử lý bản nhạc như thế nào nếu nó chỉ thao tác với số? Câu hỏi dẫn tới sự phân biệt giữa vật mang thông tin và ý nghĩa của thông tin. Một con số có thể biểu diễn độ cao của nốt nhạc, một màu sắc hoặc một lệnh.

## Dấu mốc năm 1843

Ada Lovelace công bố những ghi chú về Analytical Engine của Charles Babbage năm 1843. Trong đó, bà trình bày một chuỗi thao tác tính toán và bàn về khả năng xử lý những đối tượng được biểu diễn bằng ký hiệu. Computer History Museum lưu ý rằng phạm vi đóng góp trong sự cộng tác này vẫn là chủ đề nghiên cứu lịch sử.

Điểm đáng theo đuổi khi học lập trình là ý tưởng về biểu diễn. Máy thực hiện quy tắc trên dữ liệu đã mã hóa. Để kết quả có nghĩa, người thiết kế phải xác định dữ liệu biểu diễn điều gì và phép biến đổi được phép làm gì.

## Thử một phép biến đổi âm nhạc

Xét một ví dụ lập trình nhỏ. Mỗi số nguyên biểu diễn độ cao theo nửa cung. Tăng tất cả các số lên cùng một lượng giữ nguyên khoảng cách giữa các nốt:

```python
melody = [60, 64, 67]
shifted = [note + 2 for note in melody]
assert shifted == [62, 66, 69]
assert shifted[1] - shifted[0] == melody[1] - melody[0]
```

Quy tắc cộng 2 không hiểu cảm xúc của bản nhạc. Nó bảo toàn một quan hệ đã được mô hình hóa, cụ thể là hiệu độ cao giữa hai nốt. Muốn xử lý nhịp, ta phải biểu diễn thêm trường độ. Muốn xử lý âm lượng, ta cần thêm một thuộc tính khác.

## Điều cần phân biệt

Biểu diễn bằng số không có nghĩa mọi phép toán số đều có ý nghĩa. Cộng hai mã định danh sinh viên không tạo ra một sinh viên mới. Một thuật toán đúng cần cả thao tác hợp lệ lẫn cách diễn giải đúng dữ liệu.

## Câu hỏi tự kiểm

Vì sao cùng một danh sách ba số có thể là một màu RGB hoặc một vector vị trí, nhưng không thể áp dụng mọi phép biến đổi giống nhau?

::: details Xem gợi ý
Kiểu lưu trữ chỉ cho biết cách mã hóa. Ý nghĩa, đơn vị và các ràng buộc của bài toán quyết định phép biến đổi nào hợp lệ. Màu RGB còn có giới hạn của từng kênh, trong khi tọa độ phụ thuộc hệ quy chiếu.
:::

## Đọc tiếp

- [Hàm trong lập trình](../ham-lap-trinh.md)
- [Vòng lặp](../vong-lap.md)
- [Trạng thái](../trang-thai.md)
- [Khám phá Wiki](../index.md)

## Tài liệu tham khảo

- Computer History Museum. [Ada Lovelace](https://www.computerhistory.org/babbage/adalovelace/).
