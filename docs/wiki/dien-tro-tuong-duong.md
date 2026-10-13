---
title: "Điện trở tương đương"
wikiTerm: dien-tro-tuong-duong
prev: false
next: false
---

# Điện trở tương đương

Điện trở tương đương của một tổ hợp điện trở giữ nguyên quan hệ giữa dòng vào tổ hợp và hiệu điện thế hai đầu. Hai điện trở nối tiếp có $R_s=R_1+R_2$. Hai điện trở song song có $1/R_p=1/R_1+1/R_2$.

<WikiUsage />

## Giải thích kỹ thuật

Hai điện trở nối tiếp có cùng dòng I vì không có nhánh rẽ giữa chúng. Cộng các hiệu điện thế cho V = IR₁ + IR₂, nên R_s = R₁ + R₂. Hai điện trở song song có cùng V vì nối cùng hai nút. Cộng các dòng cho I = V/R₁ + V/R₂.

Với n điện trở dương, khai triển trước khi dùng ký hiệu tổng:

$$
\begin{aligned}
&R_s = R_1+R_2+\cdots+R_n,\\
&R_s = \sum_{j=1}^{n}R_j,\\
&\frac1{R_p} = \frac1{R_1}+\frac1{R_2}+\cdots+\frac1{R_n},\\
&\frac1{R_p} = \sum_{j=1}^{n}\frac1{R_j}.
\end{aligned}
$$

Chỉ số j chạy từ 1 đến n qua các điện trở của tổ hợp. R_s lớn hơn từng điện trở thành phần khi có ít nhất hai điện trở dương. R_p nhỏ hơn từng điện trở thành phần. Thay tổ hợp bằng điện trở tương đương giữ quan hệ ở hai đầu, nhưng vẫn cần quay lại mạch ban đầu để tìm dòng mỗi nhánh.

## Ví dụ

Hai điện trở 2 Ω và 3 Ω cho 5 Ω khi nối tiếp, nhưng chỉ 1,2 Ω khi song song. Đây là hai cách nối khác nhau của cùng các phần tử.

## Khi nào cần dùng?

Thay một tổ hợp bằng một điện trở khi xét quan hệ dòng và điện áp ở hai đầu, rồi suy dòng và điện áp từng phần tử.

## Câu hỏi ôn lại

Hai điện trở cùng nối vào một nút có nhất thiết mắc song song không?

<details><summary>Xem đáp án</summary>

Không. Mắc song song cần cả hai đầu của mỗi điện trở nối vào cùng hai nút. Chung một nút chưa đủ.

</details>

## Thuật ngữ liên quan

- [Điện trở](./dien-tro.md)
- [Dòng điện](./dong-dien.md)
- [Điện thế](./dien-the.md)
- [Quy tắc Kirchhoff](./quy-tac-kirchhoff.md)

## Tài liệu tham khảo

Young & Freedman, *University Physics with Modern Physics*, ấn bản 15, chương 26, trang 844–867.
