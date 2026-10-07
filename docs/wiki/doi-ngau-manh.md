---
title: "Đối ngẫu mạnh và khoảng cách đối ngẫu"
wikiTerm: doi-ngau-manh
prev: false
next: false
---

# Đối ngẫu mạnh và khoảng cách đối ngẫu

Đối ngẫu yếu luôn cho d*≤p* trong bài cực tiểu. Đối ngẫu mạnh là trường hợp d*=p*. Với một điểm gốc và một bộ nhân tử đều khả thi, hiệu f(x)−g(λ,ν) là khoảng cách đối ngẫu và chặn trên độ thiếu tối ưu của x.

<WikiUsage />

## Giải thích kỹ thuật

**Ba mức cần phân biệt.** Đối ngẫu yếu nói $g(\lambda,\nu)\le p^\star$ với mọi nhân tử khả thi. Lấy supremum cho $d^\star\le p^\star$. Đối ngẫu mạnh thêm đẳng thức $d^\star=p^\star$.

Với $x$ khả thi gốc, khoảng cách $f_0(x)-g(\lambda,\nu)$ thỏa $0\le f_0(x)-p^\star\le f_0(x)-g(\lambda,\nu)$. Khoảng cách nhỏ là chứng nhận định lượng nếu cả hai phía thực sự khả thi; chỉ nhìn hai giá trị gần nhau mà chưa kiểm khả thi thì chưa đủ. Nguồn: Convex Optimization, §5.2 và §5.5.2.

## Ví dụ

Nếu f(x)=4 và g(λ)=1 thì nghiệm đang xét kém tối ưu không quá 3.

## Khi nào cần dùng?

Dừng thuật toán với một chứng nhận số thay vì chỉ nhìn thay đổi của loss.

## Tự kiểm tra

Khoảng cách đối ngẫu bằng 0 cho biết gì khi hai phía đều khả thi?

<details><summary>Xem đáp án</summary>

Điểm gốc và bộ nhân tử đều tối ưu.

</details>

## Thuật ngữ liên quan

- [Hàm đối ngẫu Lagrange](./ham-doi-ngau.md)
- [Điều kiện Slater](./dieu-kien-slater.md)
- [Điều kiện KKT](./kkt.md)
