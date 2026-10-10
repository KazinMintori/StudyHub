---
title: "Hàm trong lập trình"
wikiTerm: ham-lap-trinh
prev: false
next: false
---

# Hàm trong lập trình

Hàm gom một công việc có tên, nhận tham số và có thể trả kết quả bằng return. Tham số là tên trong định nghĩa. Đối số là giá trị truyền khi gọi. In ra màn hình bằng print khác trả kết quả: Print chủ yếu tạo tác động phụ, còn return cho phép dùng kết quả trong biểu thức tiếp theo.

<WikiUsage />

## Giải thích kỹ thuật

**Tham số có thể dùng chung đối tượng.** Truyền list vào một hàm rồi sửa list tại chỗ có thể làm dữ liệu của bên gọi thay đổi. Gán lại tên tham số bên trong hàm thường không gán lại tên ở bên gọi.

Hàm có tác động phụ khác hàm chỉ trả kết quả. Đọc kiểu đầu vào, kết quả trả về và điều gì bị thay đổi để dùng hàm chính xác.

## Ví dụ

def double(x): Return 2*x. Gọi double(3) nhận 6 và có thể gán cho biến.

## Khi nào cần dùng?

Đọc code, chia nhỏ thao tác xử lý dữ liệu và viết hàm map/reduce.

## Tự kiểm tra

Hàm chỉ print(3) nhưng không return trả gì trong Python?

<details><summary>Xem đáp án</summary>

None.

</details>

## Thuật ngữ liên quan

- [Vòng lặp &amp; điều kiện](./vong-lap.md)
- [Dictionary](./dictionary.md)
- [Biến &amp; kiểu dữ liệu](./bien-kieu.md)
