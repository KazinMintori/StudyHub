---
title: "Epigraph"
wikiTerm: epigraph
prev: false
next: false
---

# Epigraph

Epigraph của f là tập các cặp (x,t) thỏa $t\ge f(x)$. Hàm f lồi khi và chỉ khi epigraph của nó là một tập lồi. Nói cách khác, ta xét cả miền phía trên đồ thị thay vì chỉ xét đường đồ thị.

<WikiUsage />

## Giải thích kỹ thuật

**Đưa giá trị hàm thành một tọa độ.** Epigraph của $f$ là $\operatorname{epi}f=\{(x,t):x\in\operatorname{dom}f,\ f(x)\le t\}$. Điều kiện $t\ge f(x)$ đặt điểm ở trên đồ thị trong trường hợp một biến.

Phép cải dạng epigraph thay $\min_x f(x)$ bằng $\min_{x,t}t$ với $f(x)\le t$. Hai bài có cùng giá trị tối ưu và thu hồi cùng $x$ tối ưu khi giá trị nhỏ nhất đạt được. Với $f=\max_i f_i$, ràng buộc epigraph tách thành $f_i(x)\le t$ cho mọi $i$. Nguồn: Convex Optimization, §3.1.7 và §4.1.3.

## Ví dụ

Epigraph của $f(x)=x^2$ là miền $t\ge x^{2}$. Điểm (0,1) thuộc epigraph còn $(0,-1)$ thì không.

## Khi nào cần dùng?

Đổi một mục tiêu hoặc maximum thành ràng buộc với biến phụ.

## Tự kiểm tra

Đồ thị của một hàm lồi có nhất thiết là tập lồi không?

<details><summary>Xem đáp án</summary>

Không. Epigraph mới là tập lồi.

</details>

## Thuật ngữ liên quan

- [Hàm lồi](./ham-loi.md)
- [Tập lồi](./tap-loi.md)
- [Nới lỏng bài toán](./noi-long-toi-uu.md)
