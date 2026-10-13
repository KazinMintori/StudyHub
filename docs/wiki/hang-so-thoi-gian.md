---
title: "Hằng số thời gian"
wikiTerm: hang-so-thoi-gian
prev: false
next: false
---

# Hằng số thời gian

Hằng số thời gian τ đặc trưng tốc độ giảm theo hàm mũ. Nếu một đại lượng giảm theo $e^{-t/\tau}$, sau thời gian τ nó còn $e^{-1}$ lần giá trị đầu. Với điện tích và dòng trong mạch R-C đơn giản, $\tau=RC$.

<WikiUsage />

## Giải thích kỹ thuật

Một đại lượng x giảm theo x(t) = x₀e^(−t/τ) còn x₀/e sau một τ. Đây là thời gian để giảm theo một hệ số xác định, không phải thời gian đại lượng đột ngột trở thành không.

Trong mạch R-C đơn giản, điện tích phóng, điện áp tụ và độ lớn dòng có τ = RC. Với tụ đang nạp từ không, đại lượng giảm theo cùng τ là phần điện tích còn thiếu so với Q_f = Cℰ.

Nếu muốn đại lượng giảm còn một phần f, với 0 < f < 1:

$$
\begin{aligned}
&f = e^{-t/\tau},\\
&t = -\tau\ln f.
\end{aligned}
$$

Năng lượng của tụ tỉ lệ q², nên khi phóng nó giảm theo e^(−2t/τ). Thời gian đặc trưng của năng lượng là τ/2. Do đó, cùng một giá trị f đòi hỏi thời gian khác nhau khi xét điện tích và năng lượng.

## Ví dụ

Sau một τ, dòng nạp hoặc độ lớn dòng phóng còn khoảng 36,8% ban đầu. Điện tích tụ đang nạp từ không đạt khoảng 63,2% giá trị cuối.

## Khi nào cần dùng?

So sánh thời gian nạp, phóng và nhận ra đại lượng nào có cùng hoặc khác thời gian đặc trưng.

## Câu hỏi ôn lại

Năng lượng tụ phóng có cùng hằng số thời gian với điện tích không?

<details><summary>Xem đáp án</summary>

Không. Năng lượng tỉ lệ bình phương điện tích nên giảm theo e^(−2t/τ). Hằng số thời gian của năng lượng là τ/2.

</details>

## Thuật ngữ liên quan

- [Mạch R-C](./mach-rc.md)
- [Điện dung](./dien-dung.md)
- [Điện trở](./dien-tro.md)
- [Tích phân](./tich-phan.md)

## Tài liệu tham khảo

Young & Freedman, *University Physics with Modern Physics*, ấn bản 15, chương 26, trang 844–867.
