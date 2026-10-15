---
title: "Quá tắt dần"
wikiTerm: qua-tat-dan
prev: false
next: false
---

# Quá tắt dần

Quá tắt dần xảy ra khi điện trở RLC thỏa $R^2>4L/C$. Phương trình đặc trưng có hai nghiệm thực âm, nên nghiệm là tổng hai hàm mũ suy giảm và không dao động lặp lại.

<WikiUsage />

## Giải thích kỹ thuật

Với $R^2>4L/C$, đặt các hệ số

$$
\begin{aligned}
\alpha &= \frac{R}{2L}, \\
\delta &= \sqrt{\alpha^2-\frac1{LC}}, \\
\alpha_1 &= \alpha-\delta, \\
\alpha_2 &= \alpha+\delta.
\end{aligned}
$$

Hai tốc độ suy giảm đều dương. Khi ấy

$$
q(t)=ae^{-\alpha_1t}+be^{-\alpha_2t}.
$$

Các nghiệm đặc trưng là $-\alpha_1,-\alpha_2$. Hệ không có thành phần lượng giác với tần số thực. Một trong hai tốc độ có thể nhỏ khi điện trở rất lớn, nên đuôi đáp ứng tiến về không chậm.

Hai hệ số a,b phụ thuộc điện tích và dòng đầu. Chúng có thể khác dấu, nên nghiệm có thể đổi dấu một lần. Điều đó không tạo chu kỳ dao động và không cho phép dùng công thức thời gian theo một chu kỳ LC.

## Ví dụ

Tăng R rất lớn có thể làm một thành phần nghiệm suy giảm chậm, dù năng lượng vẫn mất trên điện trở.

## Khi nào cần dùng?

Chọn nghiệm RLC và phân biệt dao động với suy giảm thuần túy.

## Câu hỏi ôn lại

Có tần số dao động thực để dùng 2π/ωd trong miền quá tắt dần không?

<details><summary>Xem đáp án</summary>

Không. Dạng tần số dưới tắt dần có biểu thức dưới căn âm trong miền này.

</details>

## Thuật ngữ liên quan

- [Mạch RLC nối tiếp](./mach-rlc.md)
- [Tắt dần tới hạn](./tat-dan-toi-han.md)
- [Dao động tắt dần](./dao-dong-tat-dan.md)

## Tài liệu tham khảo

Young & Freedman, ấn bản 15, chương 30, trang 988–1009.
