---
title: "Log-sum-exp và softmax"
wikiTerm: log-sum-exp
prev: false
next: false
---

# Log-sum-exp và softmax

Hàm log-sum-exp $f(x) = \log(e^{x_1} + \cdots + e^{x_n})$ là một hàm lồi, xấp xỉ trơn của $\max_i x_i$ với $\max_i x_i \le f(x) \le \max_i x_i + \log n$. Gradient của nó là vector softmax, có thành phần thứ i bằng $e^{x_i} / \sum_j e^{x_j}$.

<WikiUsage />

## Giải thích kỹ thuật

**Vì sao lồi.** Hessian bằng $\operatorname{diag}(p) - pp^T$ với $p = \operatorname{softmax}(x)$, và $v^T(\operatorname{diag}(p) - pp^T)v$ là phương sai của biến ngẫu nhiên nhận giá trị $v_i$ với xác suất $p_i$, nên không âm. Độ cong bằng 0 đúng theo hướng $\mathbf 1 = (1, \dots, 1)$.

**Nhiệt độ.** Hàm $f_\beta(x) = \frac1\beta \log\sum_i e^{\beta x_i}$ thỏa $\max_i x_i \le f_\beta(x) \le \max_i x_i + \frac{\log n}{\beta}$, và gradient của nó là $\operatorname{softmax}(\beta x)$.

**Entropy chéo.** Với logit $z$ và nhãn $y$, hàm mất mát $\log\sum_j e^{z_j} - z_y$ lồi theo $z$ và có gradient $\operatorname{softmax}(z) - e_y$. Nguồn: Convex Optimization, §3.1.5.

## Ví dụ

Với $x = (3, 1, 0)$: $\max_i x_i = 3$, $f(x) \approx 3.170$, và softmax xấp xỉ $(0.844, 0.114, 0.042)$.

## Khi nào cần dùng?

Hàm mất mát entropy chéo theo logit và phiên bản trơn của hàm max trong tối ưu.

## Câu hỏi ôn lại

Cộng cùng một hằng số c vào mọi thành phần của x thì softmax thay đổi thế nào?

<details><summary>Xem đáp án</summary>

Không đổi, vì $f(x + c\mathbf 1) = f(x) + c$ nên gradient giữ nguyên.

</details>

## Thuật ngữ liên quan

- [Hàm lồi](./ham-loi.md)
- [Hessian](./hessian.md)
- [Phương sai](./phuong-sai.md)
