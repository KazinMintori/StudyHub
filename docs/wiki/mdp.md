---
title: "Quá trình quyết định Markov"
---

# Quá trình quyết định Markov

## Giải thích kỹ thuật

Mô hình ra quyết định tuần tự gồm trạng thái, hành động, xác suất chuyển và phần thưởng. Phân phối bước tiếp theo chỉ phụ thuộc trạng thái và hành động hiện tại khi đã biết đủ thông tin trong trạng thái.

Robot chọn đi lên nhưng có thể trượt sang hai bên. Mô hình phải ghi xác suất từng kết quả và cách nhận thưởng.

Biết tọa độ đã đủ tính Markov cho robot có pin chưa?

Chưa đủ nếu mức pin ảnh hưởng bước chuyển hoặc hành động khả dụng. Có thể cần thêm mức pin vào trạng thái.

## Khi nào dùng

Mô hình hóa bài toán có kết quả hành động ngẫu nhiên trước khi tính chính sách.
