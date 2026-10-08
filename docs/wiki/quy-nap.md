---
title: "Quy nạp toán học"
wikiTerm: quy-nap
prev: false
next: false
---

# Quy nạp toán học

Để chứng minh P(n) với mọi số nguyên $n \ge  n_{0}$: kiểm tra trường hợp cơ sở $n_{0}$, rồi giả sử P(k) đúng và chứng minh $P(k+1)$. Hai bước đi cùng nhau: bước cơ sở khởi đầu chuỗi, bước suy diễn truyền tính đúng sang số tiếp theo.

<WikiUsage />

## Giải thích kỹ thuật

**Giả thiết quy nạp không phải kết luận đã chứng minh.** Nó chỉ được dùng trong bước suy diễn để đi từ k tới $k+1$. Quy nạp mạnh cho phép giả sử mọi trường hợp từ $n_{0}$ đến k đúng.

Cách này hữu ích với đệ quy có nhiều bài toán con. Trước khi áp dụng, kiểm tra mọi bài toán con đều nhỏ hơn bài toán hiện tại và các trường hợp cơ sở đã đủ.

## Ví dụ

$1 + 2 + \ldots  + n = \frac{n(n+1)}{2}$: đúng ở $n = 1$. Cộng thêm $k+1$ vào công thức tại k để thu được công thức tại $k+1$.

## Khi nào cần dùng?

Chứng minh thuật toán đệ quy, công thức tổng và bất biến.

## Tự kiểm tra

Chỉ chứng minh $P(k) \to  P(k+1)$ đã đủ chưa?

<details><summary>Xem đáp án</summary>

Chưa. Cần trường hợp cơ sở đúng để bắt đầu chuỗi.

</details>

## Thuật ngữ liên quan

- [Tổ hợp &amp; giai thừa](./to-hop.md)
- [Vị từ &amp; lượng từ](./luong-tu.md)
- [Tập hợp](./tap-hop.md)
