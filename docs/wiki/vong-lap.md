---
title: "Vòng lặp & điều kiện"
wikiTerm: vong-lap
prev: false
next: false
---

# Vòng lặp & điều kiện

if chọn nhánh theo điều kiện Boolean. for duyệt các phần tử của đối tượng lặp, còn while tiếp tục chạy chừng nào điều kiện còn đúng. Cần xác định trạng thái thay đổi và điều kiện dừng. Trong Python, thụt lề xác định khối lệnh.

<WikiUsage />

## Giải thích kỹ thuật

**Bất biến và kết thúc.** Bất biến vòng lặp là điều đúng trước và sau mỗi lần lặp, giúp chứng minh kết quả. Cần thêm đại lượng giảm hoặc miền hữu hạn để giải thích tại sao vòng lặp dừng.

Dừng đúng không đồng nghĩa kết quả đúng. Với while, kiểm tra cả việc khởi tạo, điều kiện và cập nhật biến. Nếu bỏ bước cập nhật, vòng lặp có thể không kết thúc.

## Ví dụ

for x in [1,2,3]: Cộng x vào tổng ban đầu bằng 0, cuối cùng nhận 6.

## Khi nào cần dùng?

Hiểu code mẫu và vì sao vector hóa có thể tránh nhiều vòng lặp Python.

## Tự kiểm tra

range(3) tạo các số nào?

<details><summary>Xem đáp án</summary>

0, 1, 2 và không gồm 3.

</details>

## Thuật ngữ liên quan

- [Chỉ mục &amp; lát cắt](./chi-muc.md)
- [Hàm trong lập trình](./ham-lap-trinh.md)
- [Biến &amp; kiểu dữ liệu](./bien-kieu.md)
