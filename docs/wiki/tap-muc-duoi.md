---
title: "Tập mức dưới"
wikiTerm: tap-muc-duoi
prev: false
next: false
---

# Tập mức dưới

Tập mức dưới mức $\alpha$ của hàm f là $\{x \in \operatorname{dom} f : f(x) \le \alpha\}$. Nếu f lồi thì mọi tập mức dưới đều lồi. Hàm có mọi tập mức dưới lồi được gọi là hàm tựa lồi, một lớp rộng hơn hàm lồi.

<WikiUsage />

## Giải thích kỹ thuật

**Chiều thuận và chiều ngược.** Nếu $f(x) \le \alpha$ và $f(y) \le \alpha$ thì tính lồi cho $f(\theta x + (1-\theta)y) \le \alpha$, nên tập mức dưới lồi. Chiều ngược sai, và các hàm có mọi tập mức dưới lồi tạo thành lớp hàm tựa lồi.

**Hàm tựa lồi khác hàm lồi ở đâu.** Với hàm tựa lồi khả vi, bất đẳng thức $f(y) \le f(x)$ suy ra $\nabla f(x)^T (y - x) \le 0$, nên gradient vẫn loại được nửa không gian. Nhưng gradient bằng 0 không còn bảo đảm cực tiểu toàn cục, và cực tiểu cục bộ có thể không toàn cục, chẳng hạn hàm số $x^3$ có đạo hàm bằng 0 tại gốc tọa độ. Nguồn: Convex Optimization, §3.1.6 và §3.4.

## Ví dụ

Hàm $-e^x$ lõm, nhưng mọi tập mức dưới của nó là một nửa trục, nên lồi: Hàm này tựa lồi mà không lồi.

## Khi nào cần dùng?

Chứng minh một tập là lồi bằng cách viết nó thành tập mức dưới của một hàm lồi, chẳng hạn ràng buộc $\|w\|_2 \le r$.

## Câu hỏi ôn lại

Tập mức dưới của một hàm không lồi có thể là tập lồi không?

<details><summary>Xem đáp án</summary>

Có. Chẳng hạn $-e^x$ và $x^3$ có mọi tập mức dưới là một khoảng.

</details>

## Thuật ngữ liên quan

- [Hàm lồi](./ham-loi.md)
- [Epigraph](./epigraph.md)
- [Tập lồi](./tap-loi.md)
