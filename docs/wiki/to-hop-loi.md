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

**Nhiều điểm và điều kiện trọng số.** Với $k$ điểm $x_1,\ldots,x_k$, một tổ hợp lồi được biểu diễn dưới dạng tường minh:

$$z = \lambda_1 x_1 + \lambda_2 x_2 + \cdots + \lambda_k x_k = \sum_{i=1}^k \lambda_i x_i.$$

Mỗi trọng số không âm và tổng toàn bộ các trọng số bằng 1:

$$\sum_{i=1}^k \lambda_i = \lambda_1 + \lambda_2 + \cdots + \lambda_k = 1 \quad (\lambda_i \ge 0, \; \forall i = 1, \dots, k).$$

Về mặt bản chất, đây là một **phép bình quân gia quyền** hay **pha trộn tỉ lệ phần trăm** (tổng bằng 100% và không có thành phần âm):

$$
\underbrace{\sum_{i=1}^k \lambda_i x_i}_{\text{điểm pha trộn}} \quad \text{với} \quad \underbrace{\sum_{i=1}^k \lambda_i = 1}_{\text{tổng tỉ lệ bằng } 1} \quad \text{và} \quad \underbrace{\lambda_i \ge 0}_{\text{trọng số không âm}}
$$

Chỉ số $i$ chạy từ 1 đến $k$, qua các điểm đã chọn. Khi phạm vi ngữ cảnh đã hoàn toàn rõ ràng, tài liệu có thể viết vắn tắt là $\sum_i \lambda_i = 1$ (hoặc dùng ký hiệu $\theta_i$ thay cho $\lambda_i$). 

Với hai điểm ($k=2$), điều kiện trở thành $\lambda x + (1 - \lambda) y$ với $\lambda \in [0, 1]$, quét nên trọn vẹn đoạn thẳng nối hai điểm. Nếu bỏ điều kiện không âm mà chỉ giữ tổng bằng 1, ta được tổ hợp affine kéo dài ra vô hạn trên toàn bộ đường thẳng. Bao lồi là tập hợp chứa tất cả các tổ hợp lồi có thể tạo ra từ các điểm đã cho.

## Ví dụ

$x = 0$, $y = 10$, $\lambda  = 0.3$: Điểm tạo ra là $0.3\times 0 + 0.7\times 10 = 7$.

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
