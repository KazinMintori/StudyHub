---
title: "Momentum và Nesterov"
wikiTerm: momentum-nesterov
prev: false
next: false
---

# Momentum và Nesterov

Momentum cộng gradient mới với một phần vận tốc cũ để tạo độ dời. Nesterov dùng cùng ý tưởng nhưng tính gradient tại điểm nhìn trước $\theta +\mu v$. Hai công thức chỉ so được khi quy ước dấu và cách định nghĩa vận tốc được giữ nhất quán.

<WikiUsage />

## Giải thích kỹ thuật

**Trạng thái và quy ước dấu.** Một quy ước thường dùng là $v_{t+1}=\mu v_t-\eta g_t$, $\theta_{t+1}=\theta_t+v_{t+1}$. Nesterov thay $g_t=\nabla J(\theta_t)$ bằng gradient tại $\theta_t+\mu v_t$. Tài liệu khác có thể lưu trung bình gradient thay vì độ dời, nên công thức trông khác nhưng mô tả cùng họ phương pháp.

Khi tái lập kết quả, cần lưu cả $v$, tham số, bộ đếm và quy tắc lấy lô. Khởi động lại với cùng $\theta$ nhưng mất $v$ không phải tiếp tục đúng trạng thái. Nguồn: Deep Learning, §8.3.2–8.3.3.

## Ví dụ

Nếu $\theta =0$, $v=0$, gradient −1 và $\eta =0$,1 thì bước momentum đầu cho $v=0$,1 và $\theta$ mới bằng 0,1.

## Khi nào cần dùng?

Giảm dao động và tích lũy hướng cập nhật trong huấn luyện.

## Tự kiểm tra

Điểm khác nhau chính giữa momentum chuẩn và Nesterov trong bài là gì?

<details><summary>Xem đáp án</summary>

Nesterov tính gradient tại điểm nhìn trước, không phải tại $\theta$ hiện tại.

</details>

## Thuật ngữ liên quan

- [Gradient ngẫu nhiên và SGD](./gradient-ngau-nhien.md)
- [Gradient](./gradient.md)
- [Adam](./adam.md)
