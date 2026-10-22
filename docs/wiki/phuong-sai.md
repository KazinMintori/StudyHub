---
title: "Phương sai"
wikiTerm: phuong-sai
prev: false
next: false
---

# Phương sai

Hai nhóm dữ liệu đều có trung bình 5 nhưng một nhóm nằm sát 5, còn nhóm kia trải rộng. **Phương sai** phân biệt hai tình huống bằng trung bình của bình phương độ lệch khỏi kỳ vọng.

<WikiUsage />

![Hình 1: Cùng trung bình 5 nhưng hai nhóm có phương sai rất khác nhau.](./img/atlas/variance.svg)

## Giải thích kỹ thuật

Đặt $\mu=\mathbb E[X]$ và giả sử moment bậc hai hữu hạn. Khi đó:

$$
\operatorname{Var}(X)=\mathbb E[(X-\mu)^2].
$$

Với một phân phối rời rạc hữu hạn, đây là tổng các số $(x_i-\mu)^2p_i$ từ $i=1$ đến $k$. Mỗi đóng góp không âm, nên phương sai không âm.

Khai triển bình phương cho công thức tính nhanh:

$$
\operatorname{Var}(X)=\mathbb E[X^2]-\mu^2.
$$

Độ lệch chuẩn $\sigma=\sqrt{\operatorname{Var}(X)}$ có cùng đơn vị với $X$. Phương sai có đơn vị bình phương. Nếu đổi thang đo bằng $Y=aX+b$, phương sai nhân với $a^2$, còn việc cộng $b$ không làm thay đổi nó.

Phương sai mẫu dùng để ước lượng phương sai tổng thể là một bài toán khác. Với mẫu độc lập cùng phân phối và moment hữu hạn, mẫu số $n-1$ cho ước lượng không chệch. Không được thay mọi mẫu số $n$ bằng $n-1$ mà bỏ qua mục tiêu đang tính.

## Ví dụ có lời giải

Chọn đều một giá trị trong nhóm $(4,5,6)$. Trung bình bằng 5. Các độ lệch lần lượt là $-1$, $0$, $1$, nên bình phương độ lệch là 1, 0, 1. Trung bình ba số này cho:

$$
\operatorname{Var}(X)=\frac{1+0+1}{3}=\frac23.
$$

Với nhóm $(0,5,10)$, trung bình vẫn là 5 nhưng phương sai bằng $50/3$, lớn gấp 25 lần. Đây là phương sai của phân phối đều trên ba giá trị, nên chia cho 3.

Nếu xem ba quan sát là một mẫu để ước lượng phương sai tổng thể không chệch, công thức mẫu cho hai kết quả lần lượt là 1 và 25. Phải nói rõ đang mô tả phân phối hay đang ước lượng.

## Câu hỏi ôn lại

Cộng 100 vào mọi quan sát có làm phương sai tăng lên không?

::: details Xem lời giải
Không. Trung bình cũng tăng 100 nên từng độ lệch so với trung bình được giữ nguyên. Nhân mọi quan sát với 100 mới làm phương sai tăng gấp 10.000 lần.
:::

## Đọc tiếp

- [Kỳ vọng](./ky-vong.md)
- [Hiệp phương sai](./hiep-phuong-sai.md)
- [Mẫu & tổng thể](./mau-tong-the.md)

## Tài liệu tham khảo

- [OpenStax, Introductory Statistics 2e, Mean or Expected Value and Standard Deviation](https://openstax.org/books/introductory-statistics-2e/pages/4-2-mean-or-expected-value-and-standard-deviation).
