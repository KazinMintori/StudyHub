---
title: "Con trỏ & tham chiếu"
wikiTerm: con-tro
prev: false
next: false
---

# Con trỏ & tham chiếu

Con trỏ lưu địa chỉ một vùng dữ liệu, còn tham chiếu cho phép nhiều tên cùng truy cập một đối tượng. Vì vậy, thay đổi dữ liệu qua một tên có thể được thấy qua tên khác. Sao chép địa chỉ hoặc tham chiếu không đồng nghĩa với sao chép dữ liệu.

<WikiUsage />

## Giải thích kỹ thuật

**Sở hữu dữ liệu và vòng đời.** Con trỏ hay tham chiếu có thể cho phép nhiều tên truy cập cùng vùng dữ liệu. Cần biết ai quản lý bộ nhớ và dữ liệu còn hợp lệ bao lâu. Trong ngôn ngữ có quản lý bộ nhớ thủ công, dùng địa chỉ sau khi giải phóng là lỗi.

Trong Python hoặc NumPy, tác động dễ thấy hơn là thay đổi dữ liệu dùng chung: view có thể làm mảng gốc thay đổi, trong khi copy độc lập không làm vậy.

## Ví dụ

Trong Python, a = [1]. B = a. B.append(2) làm a trở thành [1, 2].

## Khi nào cần dùng?

Hiểu danh sách liên kết, cây, và sự khác nhau giữa view và copy.

## Tự kiểm tra

b = a có tạo một list độc lập với a không?

<details><summary>Xem đáp án</summary>

Không. Cả hai tên cùng trỏ tới một list.

</details>

## Thuật ngữ liên quan

- [Đệ quy](./de-quy.md)
- [Mảng](./mang.md)
- [Đồ thị](./do-thi.md)
