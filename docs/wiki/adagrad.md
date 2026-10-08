---
title: "AdaGrad"
wikiTerm: adagrad
prev: false
next: false
---

# AdaGrad

AdaGrad cộng dồn bình phương gradient theo từng tọa độ rồi chia bước cập nhật cho căn của tổng đó. Tọa độ đã nhận nhiều gradient lớn sẽ có bước hiệu dụng nhỏ dần vì trạng thái vẫn giữ đóng góp của các bước cũ.

<WikiUsage />

## Giải thích kỹ thuật

**Tốc độ hiệu dụng theo tọa độ.** Với $s_t=s_{t-1}+g_t\odot g_t$, bước dùng $g_t/(\sqrt{s_t}+\varepsilon)$ theo từng phần tử. Các tọa độ có tổng bình phương lớn nhận bước nhỏ hơn. Vị trí của $\varepsilon$ phải được giữ khi so công thức và thư viện.

Vì $s_t$ không giảm, tốc độ hiệu dụng có thể nhỏ dần rất mạnh trong bài dài. Đây là cơ chế, không phải kết luận AdaGrad luôn kém. Nguồn: Duchi, Hazan & Singer (2011), Adaptive Subgradient Methods.

## Ví dụ

Với gradient 2 rồi 2, tổng bình phương lần lượt là 4 và 8.

## Khi nào cần dùng?

Tự điều chỉnh thang cập nhật theo từng tọa độ, nhất là khi gradient thưa.

## Tự kiểm tra

AdaGrad có quên ảnh hưởng của gradient rất cũ không?

<details><summary>Xem đáp án</summary>

Không. Tổng bình phương chỉ tăng theo thời gian.

</details>

## Thuật ngữ liên quan

- [Gradient ngẫu nhiên và SGD](./gradient-ngau-nhien.md)
- [RMSProp](./rmsprop.md)
- [Adam](./adam.md)
