---
title: "Trị riêng & vector riêng"
wikiTerm: tri-rieng
prev: false
next: false
---

# Trị riêng & vector riêng

Nếu $Av = \lambda v$ với v khác vector không, v là vector riêng của ma trận vuông A và $\lambda$ là trị riêng tương ứng. Biến đổi A chỉ co giãn hoặc đổi chiều v mà không đưa nó ra khỏi đường thẳng ban đầu.

<WikiUsage />

## Giải thích kỹ thuật

**Cách tìm trị riêng.** Từ $Av=\lambda v$ suy ra $(A-\lambda I)v=0$. Để có nghiệm $v\ne 0$ trong hữu hạn chiều, ma trận $A-\lambda I$ phải suy biến. Do đó $\det(A-\lambda I)=0$.

Trị riêng có thể là số phức với ma trận thực. Ma trận đối xứng thực có trị riêng thực và một cơ sở vector riêng trực chuẩn. Không phải mọi ma trận đều có đủ vector riêng độc lập để chéo hóa.

## Ví dụ

Với

$$A=\begin{bmatrix}2&0\\0&3\end{bmatrix},$$

vector $(1,0)^T$ có trị riêng 2, còn vector $(0,1)^T$ có trị riêng 3.

## Khi nào cần dùng?

Đọc phân tích tuyến tính, PCA và hành vi lặp ma trận.

## Tự kiểm tra

Vector không có được chọn làm vector riêng không?

<details><summary>Xem đáp án</summary>

Không. Định nghĩa yêu cầu v khác vector không.

</details>

## Thuật ngữ liên quan

- [Ma trận](./ma-tran.md)
- [Vector](./vector.md)
- [Chuẩn vector](./chuan.md)
