---
title: "Định luật Snell"
wikiTerm: dinh-luat-snell
prev: false
next: false
---

# Định luật Snell

Định luật Snell mô tả sự đổi hướng của tia sóng khi truyền qua mặt phân cách phẳng giữa hai môi trường có vận tốc truyền sóng khác nhau, biểu diễn bởi hệ thức $\frac{\sin\theta_1}{v_1} = \frac{\sin\theta_2}{v_2}$ hoặc $n_1\sin\theta_1 = n_2\sin\theta_2$.

<WikiUsage />

## Giải thích kỹ thuật

Định luật khúc xạ Snell (Snell's Law) là một trong những định luật nền tảng nhất của quang hình học và lý thuyết sóng. Trong đó:
- $\theta_1$ và $\theta_2$ là góc giữa phương truyền tia sóng và pháp tuyến của mặt phân cách lần lượt trong môi trường 1 và môi trường 2.
- $v_1, v_2$ là vận tốc pha của sóng trong hai môi trường.
- $n_1, n_2$ là chiết suất tuyệt đối của môi trường ($n = c / v$).

Theo **Nguyên lý Fermat (Nguyên lý thời gian cực tiểu)**, tia sáng khi đi giữa hai điểm cố định sẽ luôn chọn quỹ đạo chuyển động sao cho thời gian truyền ánh sáng là nhỏ nhất:
$$
T(x) = \frac{d_1(x)}{v_1} + \frac{d_2(x)}{v_2}.
$$
Bài toán tìm vị trí khúc xạ tối ưu trên mặt phân cách chính là một bài toán tối ưu hóa một biến lồi ngặt. Nghiệm của phương trình đạo hàm thời gian triệt tiêu $T'(x) = 0$ dẫn trực tiếp và tất yếu tới hệ thức $\frac{\sin\theta_1}{v_1} = \frac{\sin\theta_2}{v_2}$.

## Ví dụ thực tế

1. **Khúc xạ ánh sáng**: Khi chiếu một chùm sáng từ không khí ($n_1 \approx 1$) vào nước ($n_2 \approx 1.33$), tia sáng bị bẻ gãy lại gần đường pháp tuyến hơn vì vận tốc ánh sáng trong nước nhỏ hơn trong không khí.
2. **Bài toán Người cứu hộ**: Người cứu hộ chạy trên bãi cát với vận tốc $5\text{ m/s}$ và bơi dưới nước với vận tốc $1.5\text{ m/s}$. Để đến vị trí người bị nạn nhanh nhất, góc tiếp bờ và góc bơi thỏa mãn đúng hệ thức Snell: $\frac{\sin\theta_1}{5} = \frac{\sin\theta_2}{1.5}$.

## Khi nào cần dùng?

- Tính toán góc khúc xạ, thiết kế thấu kính quang học, sợi quang viễn thông (phản xạ toàn phần khi $\sin\theta_1 > n_2/n_1$).
- Mô hình hóa bài toán tìm đường đi ngắn nhất / nhanh nhất qua nhiều môi trường có vận tốc di chuyển khác nhau trong tối ưu hóa và trí tuệ nhân tạo.

## Câu hỏi ôn lại

Khi tia sáng đi từ môi trường có chiết suất nhỏ sang môi trường có chiết suất lớn hơn, góc khúc xạ lớn hơn hay nhỏ hơn góc tới?

<details><summary>Xem đáp án</summary>

Nhỏ hơn. Vì $n_2 > n_1$, từ $n_1\sin\theta_1 = n_2\sin\theta_2$ suy ra $\sin\theta_2 < \sin\theta_1 \implies \theta_2 < \theta_1$, tia sáng bị bẻ lệch về phía pháp tuyến.

</details>

## Thuật ngữ liên quan

- [Chiết suất](./chiet-suat.md)
- [Sóng &amp; pha](./song.md)
