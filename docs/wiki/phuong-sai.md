---
title: "Phương sai"
wikiTerm: phuong-sai
prev: false
next: false
---

# Phương sai

Phương sai Var(X)=E[(X−E[X])²] đo mức phân tán quanh kỳ vọng. Độ lệch chuẩn là căn bậc hai của phương sai nên có cùng đơn vị với X. Với mẫu và mục tiêu ước lượng phương sai tổng thể không chệch, công thức phổ biến chia tổng bình phương độ lệch cho n−1.

## Giải thích kỹ thuật

**Công thức kỹ thuật.** Với moment bậc hai hữu hạn:

$$\operatorname{Var}(X)=E[(X-E[X])^2]=E[X^2]-E[X]^2.$$

Với hai biến, Var(X+Y)=Var(X)+Var(Y)+2Cov(X,Y). Độc lập và các moment hữu hạn cho Cov=0. Phương sai có đơn vị bình phương của dữ liệu; độ lệch chuẩn có cùng đơn vị với dữ liệu. Đừng nhầm phương sai tổng thể với ước lượng phương sai mẫu chia n−1.

## Ví dụ

X nhận 0 và 2, mỗi giá trị xác suất 1/2: E[X]=1, Var(X)=1, độ lệch chuẩn = 1.

## Khi nào cần dùng?

Đọc độ bất định, sai số và tiêu chí so sánh dữ liệu.

## Tự kiểm tra

Phương sai có thể âm không?

<details><summary>Xem đáp án</summary>

Không, vì là kỳ vọng của một bình phương.

</details>

## Thuật ngữ liên quan

- [Kỳ vọng](./ky-vong.md)
- [Biến ngẫu nhiên](./bien-ngau-nhien.md)
- [Mẫu &amp; tổng thể](./mau-tong-the.md)
