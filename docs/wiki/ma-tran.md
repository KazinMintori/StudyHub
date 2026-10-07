---
title: "Ma trận"
wikiTerm: ma-tran
prev: false
next: false
---

# Ma trận

Ma trận là bảng số có hàng và cột; kích thước m × n nghĩa là m hàng, n cột. Nếu A có n cột và x có n phần tử thì Ax là vector có m phần tử. Mỗi phần tử của Ax là tổng tích giữa một hàng của A với x.

<WikiUsage />

## Giải thích kỹ thuật

**Điều kiện nhân và thứ tự.** Nếu A có shape m×n và B có shape n×p thì AB có shape m×p, với mỗi phần tử là tích vô hướng của một hàng A và một cột B. Nhìn chung AB khác BA; đôi khi BA còn không xác định.

Ma trận chuyển vị Aᵀ đổi hàng thành cột. Ma trận vuông khả nghịch có A⁻¹ sao cho A⁻¹A=AA⁻¹=I. Không phải mọi ma trận vuông đều khả nghịch.

## Ví dụ

A = [[1, 2], [0, 3]], x = (2, 1): Ax = (4, 3).

## Khi nào cần dùng?

Hiểu biến đổi tuyến tính, mô hình dữ liệu và tính toán phân tán.

## Tự kiểm tra

Ma trận 3 × 2 nhân vector 2 chiều cho kết quả mấy chiều?

<details><summary>Xem đáp án</summary>

3 chiều.

</details>

## Thuật ngữ liên quan

- [Tích vô hướng](./tich-vo-huong.md)
- [Vector](./vector.md)
