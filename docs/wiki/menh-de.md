---
title: "Mệnh đề"
wikiTerm: menh-de
prev: false
next: false
---

# Mệnh đề

Mệnh đề là phát biểu có giá trị đúng hoặc sai. $\neg p$ phủ định p. Phép hội $p \land  q$ đúng khi cả hai mệnh đề đều đúng, còn phép tuyển $p \lor  q$ đúng khi ít nhất một mệnh đề đúng. $p \to  q$ chỉ sai khi p đúng nhưng q sai. Cần phân biệt “nếu p thì q” với chiều ngược lại.

<WikiUsage />

## Giải thích kỹ thuật

**Bảng chân trị.** Có thể liệt kê mọi tổ hợp đúng/sai của các mệnh đề thành phần để kiểm tra một biểu thức. Với n biến Boolean, bảng có $2^n$ dòng. Hai biểu thức tương đương khi có cùng giá trị ở mọi dòng.

Luật De Morgan: $\neg (p\land q)$ tương đương $\neg p\lor \neg q$. $\neg (p\lor q)$ tương đương $\neg p\land \neg q$. Phép kéo theo $p\to q$ tương đương $\neg p\lor q$, không tương đương $q\to p$.

## Ví dụ

Gọi p là “$x > 3$” và q là “$x > 0$”. Với $x = 5$, cả p và q đều đúng, còn với $x = 1$, p sai nhưng q đúng.

## Khi nào cần dùng?

Đọc điều kiện thuật toán, biểu thức Boolean và luật suy luận.

## Tự kiểm tra

Khi p đúng và q sai, $p \to  q$ đúng hay sai?

<details><summary>Xem đáp án</summary>

Sai. Đây là trường hợp duy nhất làm phép kéo theo sai.

</details>

## Thuật ngữ liên quan

- [Vị từ &amp; lượng từ](./luong-tu.md)
- [Hàm số](./ham-so.md)
- [Tập hợp](./tap-hop.md)
