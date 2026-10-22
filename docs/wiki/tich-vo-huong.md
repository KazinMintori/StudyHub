---
title: "Tích vô hướng"
wikiTerm: tich-vo-huong
prev: false
next: false
---

# Tích vô hướng

Cùng một lực kéo nhưng tác dụng theo hướng chuyển động khác nhau sẽ sinh công khác nhau. **Tích vô hướng** đo mức độ hai vector cùng hướng, đồng thời cho một kết quả là số.

<WikiUsage />

![Hình 1: Thành phần theo từng trục giúp tính tích vô hướng.](./img/atlas/vector.svg)

## Giải thích kỹ thuật

Với $u=(u_1,u_2)$ và $v=(v_1,v_2)$:

$$
u\cdot v=u_1v_1+u_2v_2.
$$

Trong $n$ chiều, khai triển tương tự thành $u_1v_1+\cdots+u_nv_n$, rồi viết gọn bằng $\sum_{i=1}^n u_iv_i$. Kết quả không còn là vector.

Với hai vector khác không, góc $\theta$ giữa chúng thỏa mãn:

$$
u\cdot v=\|u\|_2\|v\|_2\cos\theta.
$$

Tích dương ứng với góc nhọn, tích bằng 0 ứng với vuông góc, tích âm ứng với góc tù. Nếu có vector không thì tích vẫn bằng 0 nhưng góc với vector không không được xác định.

Khi $v$ là vector đơn vị, $u\cdot v$ chính là độ dài có dấu của hình chiếu $u$ theo hướng $v$. Đó là lý do đạo hàm theo hướng và công cơ học cùng chứa tích vô hướng.

## Ví dụ có lời giải

Lấy $u=(3,4)$ và $v=(1,-1)$. Khi đó:

$$
u\cdot v=3\cdot1+4(-1)=-1.
$$

Hai vector tạo góc tù. Đổi thành $w=(4,-3)$ thì $u\cdot w=12-12=0$, nên $u$ và $w$ vuông góc.

Trong cơ học, nếu lực không đổi $F=(3,4)$ newton và độ dời $d=(2,0)$ mét, công bằng $F\cdot d=6$ joule. Thành phần vuông góc với độ dời không đóng góp vào công.

## Câu hỏi ôn lại

Nếu $u\cdot v=0$, có suy ra một trong hai vector bằng 0 không?

::: details Xem lời giải
Không. Chẳng hạn $(1,0)$ và $(0,1)$ đều khác không nhưng có tích vô hướng bằng 0. Đây là trường hợp vuông góc.
:::

## Đọc tiếp

- [Vector](./vector.md)
- [Chuẩn vector](./chuan.md)
- [Ma trận](./ma-tran.md)
- [Công & năng lượng](./cong-nang-luong.md)

## Tài liệu tham khảo

- [OpenStax, Calculus Volume 3, The Dot Product](https://openstax.org/books/calculus-volume-3/pages/2-3-the-dot-product).
