---
title: "Chỉ mục & lát cắt"
wikiTerm: chi-muc
prev: false
next: false
---

# Chỉ mục & lát cắt

Chỉ mục chọn vị trí. Lát cắt start:stop:step chọn một dãy vị trí. Với list và mảng Python/NumPy theo vị trí, stop không được lấy. Cần phân biệt chỉ mục vị trí với nhãn trong pandas: Loc thường gồm nhãn cuối, còn iloc theo quy tắc vị trí.

<WikiUsage />

## Giải thích kỹ thuật

**Nhãn và vị trí không giống nhau.** pandas loc theo nhãn, iloc theo vị trí. Hai giá trị cùng là số nguyên vẫn có thể được hiểu theo hai cách khác nhau. Một lát cắt loc thường gồm nhãn cuối, còn iloc không gồm vị trí cuối.

NumPy basic slicing thường tạo view dùng chung dữ liệu, còn advanced indexing thường tạo copy. Đọc quy tắc của đối tượng cụ thể thay vì suy từ cú pháp dấu ngoặc.

## Ví dụ

Với a = [10, 20, 30, 40], lát cắt a[1:3] chọn [20, 30].

## Khi nào cần dùng?

Đọc chọn hàng/cột và tránh sai lệch một vị trí.

## Tự kiểm tra

a[0:2] lấy mấy phần tử nếu a có ít nhất 2 phần tử?

<details><summary>Xem đáp án</summary>

2 phần tử, ở vị trí 0 và 1.

</details>

## Thuật ngữ liên quan

- [Vector hóa](./vector-hoa.md)
- [Vòng lặp &amp; điều kiện](./vong-lap.md)
- [Biến &amp; kiểu dữ liệu](./bien-kieu.md)
