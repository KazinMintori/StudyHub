---
title: "Chuẩn vector"
wikiTerm: chuan
prev: false
next: false
---

# Chuẩn vector

Một thuật toán dự đoán sai vector $(3,4)$. Nói sai “bao nhiêu” đòi hỏi chọn cách đo. **Chuẩn** gán một số không âm cho vector và tuân theo các tính chất giúp việc đo độ lớn nhất quán.

<WikiUsage />

![Hình 1: Cùng một tâm nhưng các độ lệch có thể được đánh giá khác nhau.](./img/atlas/variance.svg)

## Giải thích kỹ thuật

Với $x=(x_1,x_2)$, ba cách đo thường gặp là:

$$
\begin{aligned}
\|x\|_1&=|x_1|+|x_2|,\\
\|x\|_2&=\sqrt{x_1^2+x_2^2},\\
\|x\|_\infty&=\max(|x_1|,|x_2|).
\end{aligned}
$$

Một chuẩn phải bằng 0 đúng tại vector không, thỏa mãn $\|ax\|=|a|\|x\|$ và bất đẳng thức tam giác $\|x+y\|\le\|x\|+\|y\|$.

Khoảng cách sinh bởi chuẩn được định nghĩa là $d(x,y)=\|x-y\|$. Chuẩn đo độ lớn của một vector, còn khoảng cách so sánh hai điểm. Cần phân biệt hai vai trò này dù công thức có liên hệ trực tiếp.

Chuẩn một cộng mọi sai lệch tuyệt đối. Chuẩn vô cùng chỉ nhìn sai lệch lớn nhất. Chuẩn Euclid gắn với hình học tròn quen thuộc. Chọn chuẩn đồng nghĩa chọn loại sai số mà bài toán ưu tiên kiểm soát.

## Ví dụ có lời giải

Với $x=(3,4)$:

$$
\|x\|_1=7,\quad\|x\|_2=5,\quad\|x\|_\infty=4.
$$

Không có mâu thuẫn vì ba con số trả lời ba câu hỏi khác nhau. Nếu hai thiết bị có sai số lần lượt là $(0,6)$ và $(4,4)$, chuẩn vô cùng chọn thiết bị thứ hai vì sai số tồi nhất nhỏ hơn. Chuẩn một chọn thiết bị thứ nhất vì tổng sai số nhỏ hơn.

## Câu hỏi ôn lại

Bình phương chuẩn Euclid có phải một chuẩn không?

::: details Xem lời giải
Không. Với $x\ne0$, ta có $\|2x\|_2^2=4\|x\|_2^2$, trong khi tính thuần nhất của chuẩn đòi hệ số 2. Bình phương chuẩn rất hữu ích trong tối ưu nhưng không tự trở thành một chuẩn.
:::

## Đọc tiếp

- [Vector](./vector.md)
- [Tích vô hướng](./tich-vo-huong.md)
- [Bình phương tối thiểu](./binh-phuong-toi-thieu.md)

## Tài liệu tham khảo

- [S. Boyd và L. Vandenberghe, Convex Optimization](https://web.stanford.edu/~boyd/cvxbook/).
