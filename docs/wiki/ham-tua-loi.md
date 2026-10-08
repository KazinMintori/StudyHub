---
title: "Hàm tựa lồi"
wikiTerm: ham-tua-loi
prev: false
next: false
---

# Hàm tựa lồi

Hàm f là tựa lồi nếu miền của nó và mọi tập mức dưới $\{x : f(x) \le \alpha\}$ đều lồi, tương đương với $f(\theta x + (1 - \theta)y) \le \max\{f(x), f(y)\}$. Mọi hàm lồi đều tựa lồi nhưng điều ngược lại sai. Bài toán cực tiểu một hàm tựa lồi có thể có cực tiểu cục bộ không toàn cục, và được giải bằng phương pháp chia đôi trên một dãy bài toán khả thi lồi.

<WikiUsage />

## Giải thích kỹ thuật

**Những gì mất đi.** Với hàm tựa lồi, gradient bằng 0 không đủ để kết luận tối ưu, cực tiểu cục bộ có thể không toàn cục, và tổng của hai hàm tựa lồi có thể không tựa lồi. Giá trị lớn nhất có trọng số không âm và hợp với hàm không giảm vẫn giữ tính tựa lồi.

**Phương pháp chia đôi.** Biểu diễn tập mức dưới bằng một họ hàm lồi $\phi_t$ với $f(x) \le t \iff \phi_t(x) \le 0$. Câu hỏi khả thi tại mức $t$ là một bài toán lồi, cho biết $p^\star \le t$ hay $p^\star \ge t$. Chia đôi khoảng $[l, u]$ cho tới khi độ dài không quá $\varepsilon$ cần đúng $\lceil \log_2((u - l)/\varepsilon) \rceil$ lần. Với tỉ số $p/q$ của hàm lồi không âm và hàm lõm dương, có thể chọn $\phi_t = p - tq$. Nguồn: Convex Optimization, §3.4 và §4.2.5.

## Ví dụ

$\log x$ trên $x > 0$, hàm $x^3$ và mọi hàm phân tuyến tính có mẫu số dương đều tựa lồi.

## Khi nào cần dùng?

Tối ưu các tỉ số như chi phí trung bình, tỉ số khoảng cách hay lợi ích trên chi phí.

## Câu hỏi ôn lại

Tổng của hai hàm tựa lồi có luôn tựa lồi không?

<details><summary>Xem đáp án</summary>

Không. Hai hàm $x^3$ và $-3x$ đều tựa lồi, nhưng tập mức dưới mức 0 của $x^3 - 3x$ gồm hai khoảng rời nhau.

</details>

## Thuật ngữ liên quan

- [Tập mức dưới](./tap-muc-duoi.md)
- [Hàm lồi](./ham-loi.md)
- [Quy hoạch tuyến tính (LP)](./quy-hoach-tuyen-tinh.md)
