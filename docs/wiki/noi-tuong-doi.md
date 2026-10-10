---
title: "Nội tương đối"
wikiTerm: noi-tuong-doi
prev: false
next: false
---

# Nội tương đối

Nội tương đối của tập C gồm các điểm x của C sao cho một quả cầu nhỏ quanh x, khi chỉ xét phần nằm trong bao affine của C, vẫn nằm trọn trong C. Đó là phần trong được đo bên trong bao affine thay vì trong toàn không gian.

<WikiUsage />

## Giải thích kỹ thuật

**Định nghĩa.** $\operatorname{relint} C = \{x \in C : B(x, r) \cap \operatorname{aff} C \subseteq C \text{ với một } r > 0\}$. Biên tương đối là $\operatorname{cl} C \setminus \operatorname{relint} C$.

**Vì sao cần.** Phần trong thông thường phụ thuộc vào không gian chứa tập: Cùng một đoạn thẳng có phần trong khác rỗng trong $\mathbb R$ nhưng rỗng trong $\mathbb R^2$. Nội tương đối không phụ thuộc vào điều đó, nên là khái niệm đúng cho các tập thấp chiều, chẳng hạn miền khả thi có ràng buộc đẳng thức. Mọi tập lồi khác rỗng đều có nội tương đối khác rỗng. Nguồn: Convex Optimization, §2.1.3.

## Ví dụ

Hình vuông $[-1, 1]^2$ đặt trên mặt $x_3 = 0$ của $\mathbb R^3$ có phần trong rỗng, nhưng nội tương đối của nó là hình vuông bỏ đi bốn cạnh.

## Khi nào cần dùng?

Phát biểu các điều kiện như Slater cho những tập thấp chiều mà phần trong thông thường rỗng.

## Câu hỏi ôn lại

Một đoạn thẳng trong mặt phẳng có nội tương đối là gì?

<details><summary>Xem đáp án</summary>

Chính đoạn thẳng đó bỏ đi hai đầu mút.

</details>

## Thuật ngữ liên quan

- [Tập affine](./tap-affine.md)
- [Tập lồi](./tap-loi.md)
- [Điều kiện Slater](./dieu-kien-slater.md)
