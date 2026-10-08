---
title: "Tìm kiếm đường và backtracking"
wikiTerm: tim-kiem-duong
prev: false
next: false
---

# Tìm kiếm đường và backtracking

Tìm kiếm đường chọn độ dài t sau khi đã có hướng d. Backtracking bắt đầu từ một bước thử rồi giảm dần cho đến khi điểm mới thuộc miền và cho mức giảm đủ theo điều kiện đã chọn.

<WikiUsage />

## Giải thích kỹ thuật

**Điều kiện Armijo trong backtracking.** Với hướng giảm $d$, chọn $0<\alpha<1/2$, $0<\beta<1$ và giảm $t\leftarrow\beta t$ cho tới khi

$$f(x+td)\le f(x)+\alpha t\nabla f(x)^Td.$$

Nếu hàm có miền hạn chế, phải kiểm $x+td\in\operatorname{dom}f$ trước khi tính giá trị. Backtracking tìm một bước giảm đủ, không tìm minimum chính xác trên đường. Hướng và độ dài bước là hai quyết định riêng. Nguồn: Convex Optimization, §9.2–9.3.

## Ví dụ

Với t ban đầu 1 và β=1/2, các bước thử lần lượt là 1, 1/2, 1/4, 1/8,… cho tới khi đạt điều kiện.

## Khi nào cần dùng?

Chọn bước cho gradient descent, Newton và các hướng giảm khác.

## Tự kiểm tra

Một hướng giảm có bảo đảm mọi bước dương đều làm hàm giảm không?

<details><summary>Xem đáp án</summary>

Không. Chỉ các bước dương đủ nhỏ mới được bảo đảm cục bộ.

</details>

## Thuật ngữ liên quan

- [Gradient](./gradient.md)
- [Hessian](./hessian.md)
- [Hàm tự tương hợp (self-concordant)](./tu-tuong-hop.md)
