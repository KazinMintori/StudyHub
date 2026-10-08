---
title: "Tham số trong mô hình toán học"
wikiTerm: tham-so-toan-hoc
prev: false
next: false
---

# Tham số trong mô hình toán học

Tham số là đại lượng xác định một hàm, mô hình hoặc họ bài toán. Tùy ngữ cảnh, tham số có thể là đại lượng cần ước lượng hoặc dữ liệu được giữ cố định. Vì vậy, cần đọc rõ bài toán đang tối ưu theo biến nào.

<WikiUsage />

## Giải thích kỹ thuật

**Vai trò phụ thuộc bài toán.** Trong biểu thức $f(x;\rho)$, dấu chấm phẩy thường nhắc rằng $x$ là biến đang được xét còn $\rho$ được ấn định khi giải một bài cụ thể. Nếu chuyển sang bài chọn cả $x$ và $\rho$, vai trò của $\rho$ đã thay đổi và miền tối ưu phải được viết lại.

Trong thống kê và học máy, tham số thường là đại lượng chưa biết của mô hình và được ước lượng từ dữ liệu. Trong một định lý, “tham số” cũng có thể chỉ một số đánh chỉ mục cho cả một họ đối tượng. Vì vậy không thể quyết định vai trò chỉ từ tên ký hiệu. Phải đọc câu khai báo biến và dữ liệu. Nguồn: Convex Optimization, §1.1 và quy ước ký hiệu §1.6.

## Ví dụ

Trong mô hình dự đoán $\hat b=Aw$, $w$ là tham số cần ước lượng khi $A$ và $b$ được xem là dữ liệu.

## Khi nào cần dùng?

Phân biệt biến quyết định với dữ liệu cố định, đồng thời xác định đại lượng nào điều khiển hình dạng của mô hình.

## Câu hỏi ôn lại

Trong bài minₓ f(x. $\rho$), nếu $\rho$ được ấn định trước thì biến tối ưu là x hay $\rho$?

<details><summary>Xem đáp án</summary>

Biến tối ưu là x, còn $\rho$ là tham số được giữ cố định.

</details>

## Thuật ngữ liên quan

- [Hàm số](./ham-so.md)
- [Gradient](./gradient.md)
- [Điểm và miền khả thi](./mien-kha-thi.md)
