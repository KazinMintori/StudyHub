---
title: "Vector"
wikiTerm: "vector"
prev: false
next: false
---

# Vector

Khi đã chọn cơ sở, một vector được biểu diễn bằng một bộ thành phần có thứ tự. Cộng hai vector cùng cơ sở bằng cách cộng các thành phần tương ứng. Nhân vector với một số bằng cách nhân từng thành phần với số ấy. Trong hình học và cơ học, vector có ý nghĩa về độ lớn và hướng.

<WikiUsage />

## Giải thích kỹ thuật

Vector hình học và bộ tọa độ của nó cần được phân biệt. Cùng một vector có thể có các thành phần khác nhau khi đổi cơ sở. Khi cộng hoặc so sánh các thành phần, phải dùng cùng cơ sở và cùng số chiều.

Trong hệ trục vuông góc hai chiều, phép cộng được khai triển:

$$
\vec u+\vec v=(u_x+v_x,\,u_y+v_y).
$$

Độ lớn được tính bằng chuẩn Euclid:

$$
\|\vec v\|=\sqrt{v_x^2+v_y^2}.
$$

Với vector khác không, vector cùng hướng có độ lớn bằng một là:

$$
\hat v=\frac{\vec v}{\|\vec v\|}.
$$

Không thể dùng phép chia này cho vector không. Trong dữ liệu nhiều chiều, các thành phần có thể biểu diễn đặc trưng, nên không nhất thiết phải hình dung một mũi tên trong không gian vật lý.

## Ví dụ

Với $\vec u=(1,2)$ và $\vec v=(3,-1)$, tổng là $\vec u+\vec v=(4,1)$, còn $2\vec u=(2,4)$.

## Khi nào cần dùng?

Biểu diễn vị trí, lực, động lượng, gradient và các bộ đặc trưng dữ liệu.

## Câu hỏi ôn lại

Với $v = (2, -3)$, −v là gì?

<details><summary>Xem đáp án</summary>

$(-2, 3)$.

</details>

## Thuật ngữ liên quan

- [Ma trận](./ma-tran.md)
- [Tổ hợp lồi](./to-hop-loi.md)

## Tài liệu tham khảo

Young & Freedman, *University Physics with Modern Physics*, ấn bản 15, mục 1.7–1.10.
