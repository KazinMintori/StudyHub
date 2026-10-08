---
title: "Tổ hợp lồi"
wikiTerm: to-hop-loi
prev: false
next: false
---

# Tổ hợp lồi

Tổ hợp lồi là tổng có trọng số không âm và tổng trọng số bằng 1. Với hai điểm, $\lambda x+(1-\lambda )y$, $0 \le  \lambda  \le  1$, chạy trên đoạn thẳng nối chúng. Cho $\lambda$ ngoài khoảng đó thường đưa điểm ra khỏi đoạn thẳng.

<WikiUsage />

## Giải thích kỹ thuật

**Nhiều điểm và điều kiện trọng số.** Với $k$ điểm $x_1,\ldots,x_k$, một tổ hợp lồi có dạng đầy đủ

$$z=\lambda_1x_1+\lambda_2x_2+\cdots+\lambda_kx_k.$$

Mỗi trọng số không âm và tổng trọng số bằng 1:

$$\lambda_1+\lambda_2+\cdots+\lambda_k=1,\qquad\lambda_i\ge0.$$

Viết gọn bằng ký hiệu tổng:

$$z=\sum_{i=1}^k\lambda_i x_i,\qquad\sum_{i=1}^k\lambda_i=1.$$

Chỉ số $i$ chạy từ 1 đến $k$, qua các điểm đã chọn. Sau khi phạm vi đã rõ, $\sum_i\lambda_i=1$ là cách viết tắt cùng điều kiện. Tài liệu có thể dùng $\theta_i$ thay cho $\lambda_i$. Cả hai đều là tên của trọng số. Bao lồi là tập tất cả tổ hợp lồi của các điểm đã cho.

Với hai điểm, điều kiện tạo đúng đoạn nối. Nếu bỏ điều kiện không âm nhưng vẫn giữ tổng bằng 1, ta có tổ hợp affine có thể nằm ngoài đoạn. Đây là sự khác nhau cần nhớ khi đọc tập lồi.

## Ví dụ

$x = 0$, $y = 10$, $\lambda  = 0.3$: điểm tạo ra là $0.3\times 0 + 0.7\times 10 = 7$.

## Khi nào cần dùng?

Đọc định nghĩa tập lồi, hàm lồi và nội suy.

## Tự kiểm tra

$2x-y$ có phải tổ hợp lồi của x và y không?

<details><summary>Xem đáp án</summary>

Không. Trọng số của y là −1, vi phạm điều kiện không âm.

</details>

## Thuật ngữ liên quan

- [Vector](./vector.md)
- [Tập hợp](./tap-hop.md)
- [Hàm số](./ham-so.md)
