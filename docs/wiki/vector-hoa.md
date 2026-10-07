---
title: "Vector hóa"
wikiTerm: vector-hoa
prev: false
next: false
---

# Vector hóa

Vector hóa biểu diễn thao tác trên cả mảng bằng các phép toán tối ưu thay vì một vòng lặp Python cho từng phần tử. Cần hiểu shape, dtype và quy tắc broadcasting để phép toán tương ứng đúng với điều định làm. Không phải mọi phép vector hóa đều giảm bộ nhớ.

## Giải thích kỹ thuật

**Tốc độ không phải tiêu chí duy nhất.** Phép toán trên mảng có thể chuyển vòng lặp sang mã tối ưu bên dưới, nhưng vẫn phải thực hiện công việc. Các mảng tạm có thể làm tăng bộ nhớ và đọc/ghi.

Vector hóa đúng cần giữ ý nghĩa trục, shape và dtype. Kiểm tra đầu ra trên ví dụ nhỏ trước khi thay toàn bộ vòng lặp bằng một biểu thức mảng.

## Ví dụ

Với mảng a=[1,2,3], phép a*2 tạo [2,4,6] theo từng phần tử.

## Khi nào cần dùng?

Đọc NumPy, pandas và lựa chọn cách tính hiệu quả.

## Tự kiểm tra

List Python [1,2]*2 có phải nhân từng số không?

<details><summary>Xem đáp án</summary>

Không. Nó lặp list thành [1,2,1,2].

</details>

## Thuật ngữ liên quan

- [Mảng](./mang.md)
- [Broadcasting](./broadcasting.md)
- [Vòng lặp &amp; điều kiện](./vong-lap.md)
- [Biến &amp; kiểu dữ liệu](./bien-kieu.md)
