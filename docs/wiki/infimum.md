---
title: "Infimum"
wikiTerm: infimum
prev: false
next: false
---

# Infimum

Infimum của một tập giá trị là cận dưới lớn nhất của tập đó. Nó có thể không thuộc tập, nên giá trị tối ưu có infimum hữu hạn nhưng bài toán vẫn không có điểm đạt giá trị ấy.

<WikiUsage />

## Giải thích kỹ thuật

**Cận dưới và phần tử nhỏ nhất.** Số $a$ là cận dưới của tập $S$ nếu $a\le s$ với mọi $s\in S$. Infimum $\inf S$ là cận dưới lớn nhất. Nếu tồn tại $s^\star\in S$ bằng $\inf S$, khi đó $s^\star$ là phần tử nhỏ nhất.

Trong tối ưu, $p^\star=\inf_{x\in C}f(x)$ luôn mô tả giá trị tối ưu mở rộng, kể cả khi không có nghiệm đạt hoặc khi giá trị là $-\infty$. Muốn khẳng định có nghiệm, cần thêm lập luận về tính đạt, chẳng hạn hàm liên tục trên một miền đóng và bị chặn khác rỗng. Nguồn: Convex Optimization, §4.1.

## Ví dụ

Với $x>0$, $\inf x=0$ nhưng không có $x>0$ nào bằng 0.

## Khi nào cần dùng?

Phân biệt giá trị tối ưu với sự tồn tại của nghiệm đạt tối ưu.

## Tự kiểm tra

Bài min x với $x>0$ có nghiệm tối ưu $x=0$ không?

<details><summary>Xem đáp án</summary>

Không. 0 là infimum nhưng không thuộc miền $x>0$.

</details>

## Thuật ngữ liên quan

- [Điểm và miền khả thi](./mien-kha-thi.md)
- [Nới lỏng bài toán](./noi-long-toi-uu.md)
- [Hàm đối ngẫu Lagrange](./ham-doi-ngau.md)
