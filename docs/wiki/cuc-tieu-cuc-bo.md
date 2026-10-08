---
title: "Cực tiểu cục bộ và toàn cục"
wikiTerm: cuc-tieu-cuc-bo
prev: false
next: false
---

# Cực tiểu cục bộ và toàn cục

Điểm khả thi x là cực tiểu cục bộ nếu không có điểm khả thi nào tốt hơn trong một lân cận đủ nhỏ của x, và là cực tiểu toàn cục nếu không có điểm khả thi nào tốt hơn trên toàn miền. Trong bài toán tối ưu lồi, mọi cực tiểu cục bộ đều là cực tiểu toàn cục.

<WikiUsage />

## Giải thích kỹ thuật

**Lời chứng minh.** Nếu $x$ là cực tiểu cục bộ với bán kính $R$ mà có điểm khả thi $y$ tốt hơn, điểm $z = (1-\theta)x + \theta y$ cách $x$ một khoảng $R/2$ vẫn khả thi và có $f_0(z) < f_0(x)$, mâu thuẫn.

**Khi không lồi.** Hàm không lồi có thể có cực tiểu cục bộ tồi và điểm yên ngựa, và kết quả của phương pháp gradient khi đó phụ thuộc vào điểm xuất phát. Với hàm tựa lồi, cực tiểu cục bộ cũng có thể không toàn cục. Nguồn: Convex Optimization, §4.2.2 và §4.2.5.

## Ví dụ

Hàm $0.25x^4 - x^2 + 0.3x$ có cực tiểu cục bộ tại $x \approx 1.332$ với giá trị $-0.588$, nhưng cực tiểu toàn cục nằm ở $x \approx -1.484$ với giá trị $-1.435$.

## Khi nào cần dùng?

Đánh giá kết quả của những thuật toán chỉ dùng thông tin cục bộ như phương pháp gradient.

## Câu hỏi ôn lại

Vì sao định lý cục bộ là toàn cục cần cả miền lồi lẫn hàm lồi?

<details><summary>Xem đáp án</summary>

Miền lồi giữ cho điểm trung gian trên đoạn tới một điểm tốt hơn vẫn khả thi, còn hàm lồi làm điểm trung gian ấy tốt hơn điểm đang xét.

</details>

## Thuật ngữ liên quan

- [Hàm lồi](./ham-loi.md)
- [Điểm và miền khả thi](./mien-kha-thi.md)
- [Gradient](./gradient.md)
