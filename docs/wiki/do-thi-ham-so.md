---
title: "Đồ thị của hàm số"
wikiTerm: do-thi-ham-so
prev: false
next: false
---

# Đồ thị của hàm số

Đồ thị của hàm $f$ là tập các điểm $(x, f(x))$ với $x$ thuộc miền xác định. Hàm một biến có đồ thị là một đường cong trên mặt phẳng. Hàm hai biến có đồ thị là một mặt cong trong không gian ba chiều, thường được vẽ gián tiếp bằng các đường mức.

<WikiUsage />

## Giải thích kỹ thuật

**Đồ thị là một tập hợp.** Với $f:\mathbb R^n\to\mathbb R$, đồ thị là $\{(x,f(x)) : x\in\operatorname{dom} f\}$, một tập con của $\mathbb R^{n+1}$. Nhìn hàm như một tập hợp cho phép dùng hình học của tập hợp: Hàm lồi khi đồ thị nằm dưới mọi dây cung nối hai điểm của nó, và khi khả vi thì tiếp tuyến hay siêu phẳng tiếp xúc tại mọi điểm nằm dưới đồ thị.

**Đồ thị, epigraph và đường mức.** Epigraph $\{(x,t): f(x)\le t\}$ gồm đồ thị và mọi điểm nằm phía trên nó. Hàm lồi khi và chỉ khi epigraph là tập lồi, trong khi bản thân đồ thị của một hàm lồi không affine thì không lồi: Đồ thị của $x^2$ chứa $(-1,1)$ và $(1,1)$ nhưng không chứa trung điểm $(0,1)$. Đường mức $\{x: f(x)=\alpha\}$ là hình chiếu xuống mặt phẳng nằm ngang của giao giữa đồ thị và mặt phẳng độ cao $\alpha$, nên các đường mức là cách vẽ đồ thị của hàm hai biến trên giấy.

**Không nhầm với đồ thị trong lý thuyết đồ thị.** Cùng là chữ “đồ thị”, nhưng trong lý thuyết đồ thị và trong học sâu (đồ thị tính toán), từ này chỉ một cấu trúc gồm đỉnh và cạnh, hoàn toàn khác đồ thị của một hàm số.

## Ví dụ

Đồ thị của $f(x) = x^2$ là parabol đi qua $(-1, 1)$, $(0, 0)$ và $(2, 4)$.

## Khi nào cần dùng?

Đọc tính lồi bằng hình học: Đồ thị nằm dưới mọi dây cung, tiếp tuyến nằm dưới đồ thị.

## Câu hỏi ôn lại

Đồ thị của một hàm hai biến nằm trong không gian mấy chiều?

<details><summary>Xem đáp án</summary>

Ba chiều, vì mỗi điểm có dạng $(x_1, x_2, f(x_1, x_2))$.

</details>

## Thuật ngữ liên quan

- [Hàm số](./ham-so.md)
- [Đạo hàm](./dao-ham.md)
- [Hàm lồi](./ham-loi.md)
- [Epigraph](./epigraph.md)
