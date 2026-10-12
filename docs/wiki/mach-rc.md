---
title: "Mạch R-C"
wikiTerm: mach-rc
prev: false
next: false
---

# Mạch R-C

Mạch R-C gồm điện trở và tụ điện. Trong mạch nạp hoặc phóng đơn giản, dòng và điện tích thay đổi theo thời gian do điện áp tụ phụ thuộc điện tích. Thời gian đặc trưng là $\tau=RC$.

<WikiUsage />

## Giải thích kỹ thuật

Khi nạp tụ chưa tích điện từ nguồn lý tưởng có suất điện động ℰ không đổi qua R, quy tắc vòng cho ℰ − iR − q/C = 0. Vì i = dq/dt, đây là phương trình vi phân của điện tích:

$$
\begin{aligned}
\frac{dq}{dt}&=\frac{\mathcal E}{R}-\frac q{RC},\\
q(t)&=C\mathcal E(1-e^{-t/(RC)}),\\
i(t)&=\frac{\mathcal E}{R}e^{-t/(RC)}.
\end{aligned}
$$

Điện tích không nhảy đột ngột trong mạch có dòng hữu hạn. Lúc đầu q = 0, sau thời gian đủ dài q tiến đến Cℰ và dòng tiến đến không.

Ngắt nguồn rồi cho tụ có điện tích Q₀ phóng qua R:

$$
\begin{aligned}
q(t)&=Q_0e^{-t/(RC)},\\
i(t)&=-\frac{Q_0}{RC}e^{-t/(RC)}.
\end{aligned}
$$

Dấu âm dùng chiều nạp làm chiều dương. Năng lượng ban đầu Q₀²/(2C) cuối cùng chuyển thành nhiệt trên điện trở. Các công thức cần R và C không đổi, tụ lý tưởng và đúng cấu hình nạp hoặc phóng đã nêu.

## Ví dụ

Tụ 5,0 µF nạp qua điện trở 2,0 MΩ từ nguồn 10 V có hằng số thời gian 10 s, điện tích cuối 50 µC và dòng đầu 5,0 µA.

## Khi nào cần dùng?

Phân tích nạp, phóng, tính điện tích, dòng, điện áp và năng lượng theo thời gian.

## Câu hỏi ôn lại

Dòng qua mạch nạp có bằng ℰ/R ở mọi thời điểm không?

<details><summary>Xem đáp án</summary>

Không. Giá trị ấy chỉ là dòng đầu khi tụ chưa tích điện. Điện áp trên tụ tăng làm điện áp trên điện trở và dòng giảm dần.

</details>

## Thuật ngữ liên quan

- [Điện dung](./dien-dung.md)
- [Điện trở](./dien-tro.md)
- [Quy tắc Kirchhoff](./quy-tac-kirchhoff.md)
- [Hằng số thời gian](./hang-so-thoi-gian.md)
- [Đạo hàm](./dao-ham.md)

## Tài liệu tham khảo

Young & Freedman, *University Physics with Modern Physics*, ấn bản 15, chương 26, trang 844–867.
