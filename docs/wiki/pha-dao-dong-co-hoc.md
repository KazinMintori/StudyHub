---
title: "Pha của dao động cơ"
wikiTerm: pha-dao-dong-co-hoc
prev: false
next: false
---

# Pha của dao động cơ

Trong $x=A\cos(\omega t+\phi)$, pha là $\omega t+\phi$ và $\phi$ là pha ban đầu. Pha phải phù hợp cả vị trí lẫn vận tốc đầu.

<WikiUsage />

## Giải thích kỹ thuật

Với $A>0$, điều kiện đầu là:

$$
x_0=A\cos\phi
$$

$$
v_0=-\omega A\sin\phi
$$

Một lựa chọn pha phù hợp là:

$$
\phi=\operatorname{atan2}(-v_0/\omega,x_0)
$$

Các pha khác nhau bởi bội nguyên của $2\pi$ mô tả cùng trạng thái. Pha là tọa độ xác định vị trí trong một chu kỳ, không phải góc quay thật của một con trượt.

## Ví dụ

Cùng vị trí đầu nhưng vận tốc trái dấu có thể cho hai pha khác nhau và cùng biên độ.

## Khi nào cần dùng?

Khôi phục trạng thái đầu và so sánh các dao động hình sin.

## Câu hỏi ôn lại

Chỉ dùng arctan của một tỷ số đã luôn xác định đúng pha chưa?

<details><summary>Xem đáp án</summary>

Chưa. Cần xét góc phần tư từ cả dấu cos và sin hoặc dùng hàm $\operatorname{atan2}$. Khi biên độ bằng không, pha không có giá trị vật lý duy nhất.

</details>

## Thuật ngữ liên quan

- [Dao động điều hòa](./dao-dong-dieu-hoa.md)
- [Tần số góc của dao động](./tan-so-goc-dao-dong.md)

## Tài liệu tham khảo

Young & Freedman, *University Physics with Modern Physics*, ấn bản 15, mục 14.2.
