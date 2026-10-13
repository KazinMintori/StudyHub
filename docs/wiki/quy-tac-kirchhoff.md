---
title: "Quy tắc Kirchhoff"
wikiTerm: quy-tac-kirchhoff
prev: false
next: false
---

# Quy tắc Kirchhoff

Quy tắc nút nói tổng dòng đi vào bằng tổng dòng đi ra khi điện tích không tích tụ tại nút. Quy tắc vòng nói tổng đại số các biến thiên điện thế khi đi hết một vòng kín bằng không trong mô hình mạch đang xét.

<WikiUsage />

## Giải thích kỹ thuật

Chọn chiều dương của từng dòng trước khi lập phương trình. Với hai dòng I₁, I₂ đi vào nút và I₃ đi ra, bảo toàn điện tích cho I₁ + I₂ − I₃ = 0. Tổng quát, với m dòng có dấu:

$$
\begin{aligned}
&\widetilde I_1+\widetilde I_2+\cdots+\widetilde I_m = 0,\\
&\sum_{j=1}^{m}\widetilde I_j = 0.
\end{aligned}
$$

Chỉ số j chạy qua m nhánh tại nút. Dấu của mỗi dòng biểu thị chiều vào hoặc ra theo quy ước chung.

Khi đi quanh vòng, mỗi đoạn có một biến thiên điện thế. Với ba đoạn, ΔV₁ + ΔV₂ + ΔV₃ = 0. Tổng quát cho k đoạn:

$$
\sum_{j=1}^{k}\Delta V_j=0.
$$

Qua điện trở theo chiều dòng cho −IR, đi ngược chiều dòng cho +IR. Qua nguồn từ cực âm đến cực dương cho +ℰ, chiều ngược lại cho −ℰ. Trong mạch nhiều nhánh, không được tự coi mọi điện trở trên một vòng có cùng dòng.

Quy tắc vòng dùng tính chất thế của điện trường trong mô hình tĩnh điện. Nếu có từ thông biến thiên, cần tính suất điện động cảm ứng trong phương trình mạch tương ứng.

## Ví dụ

Hai dòng 2 A và 3 A đi vào nút, một dòng đi ra phải bằng 5 A. Một nguồn 12 V nối tiếp các điện trở 2 Ω và 4 Ω cho dòng 2 A và sụt áp 4 V, 8 V.

## Khi nào cần dùng?

Lập phương trình cho mạch có nhiều nguồn và nhánh, giữ nhất quán chiều dòng, chiều đi vòng và cực tính.

## Câu hỏi ôn lại

Dòng tính ra âm có chứng tỏ phương trình sai không?

<details><summary>Xem đáp án</summary>

Không. Nếu phương trình được lập nhất quán, dấu âm cho biết dòng thực chạy ngược chiều giả định.

</details>

## Thuật ngữ liên quan

- [Điện tích](./dien-tich.md)
- [Dòng điện](./dong-dien.md)
- [Điện thế](./dien-the.md)
- [Suất điện động](./suat-dien-dong.md)

## Tài liệu tham khảo

Young & Freedman, *University Physics with Modern Physics*, ấn bản 15, chương 26, trang 844–867.
