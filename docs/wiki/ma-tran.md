---
title: "Ma trận"
wikiTerm: ma-tran
prev: false
next: false
---

# Ma trận

Ma trận là bảng số có hàng và cột. Kích thước $m \times  n$ nghĩa là m hàng, n cột. Nếu A có n cột và x có n phần tử thì Ax là vector có m phần tử. Mỗi phần tử của Ax là tổng tích giữa một hàng của A với x.

<WikiUsage />

## Giải thích kỹ thuật

Với ma trận $A$ có $m$ hàng, $n$ cột và vector $x$ có $n$ thành phần, phép nhân $y=Ax$ tạo vector $y$ có $m$ thành phần. Hàng thứ $i$ được tính bằng

$$
\begin{aligned}
y_i&=A_{i1}x_1+A_{i2}x_2+\cdots+A_{in}x_n\\
&=\sum_{j=1}^n A_{ij}x_j.
\end{aligned}
$$

$i$ chọn hàng của $A$. $j$ chạy qua các cột, từ 1 đến $n$. Các tích trong một hàng được cộng lại để cho một thành phần của $y$.

**Điều kiện nhân và thứ tự.** Nếu A có kích thước $m\times n$ và B có kích thước $n\times p$ thì AB có kích thước $m\times p$, với mỗi phần tử là tích vô hướng của một hàng của A và một cột của B. Nhìn chung AB khác BA. Đôi khi BA còn không xác định.

Ma trận chuyển vị $A^{T}$ đổi hàng thành cột. Ma trận vuông khả nghịch có A⁻¹ sao cho $A^{-1}A=AA^{-1}=I$. Không phải mọi ma trận vuông đều khả nghịch.

## Ví dụ

Với

$$A=\begin{bmatrix}1&2\\0&3\end{bmatrix},\qquad x=\begin{bmatrix}2\\1\end{bmatrix},$$

ta có $Ax=(4,3)^T$.

## Khi nào cần dùng?

Hiểu biến đổi tuyến tính, mô hình dữ liệu và tính toán phân tán.

## Tự kiểm tra

Ma trận $3 \times  2$ nhân vector 2 chiều cho kết quả mấy chiều?

<details><summary>Xem đáp án</summary>

3 chiều.

</details>

## Thuật ngữ liên quan

- [Tích vô hướng](./tich-vo-huong.md)
- [Vector](./vector.md)
