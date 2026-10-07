---
title: "RMSProp"
wikiTerm: rmsprop
prev: false
next: false
---

# RMSProp

RMSProp theo dõi trung bình mũ của bình phương gradient thay vì cộng dồn từ đầu. Trọng số của quá khứ xa giảm theo lũy thừa của β. Trạng thái này là moment bậc hai không tâm, không phải phương sai đã trừ trung bình.

<WikiUsage />

## Giải thích kỹ thuật

**Trung bình mũ của bình phương.** $v_t=\beta v_{t-1}+(1-\beta)g_t^2$ gán trọng số $(1-\beta)\beta^k$ cho bình phương gradient cách $k$ bước. Tổng các trọng số quan sát được ở đầu quá trình nhỏ hơn 1 nếu khởi tạo bằng 0.

Công thức RMSProp trong tài liệu và thư viện có thể khác ở vị trí epsilon, phần momentum bổ sung hoặc biến thể có tâm. Cần đối chiếu đúng công thức trước khi so từng con số. Nguồn: Deep Learning, §8.5.2.

## Ví dụ

Với v₀=0, g₁=2, β=0,9: v₁=0,9·0+0,1·4=0,4.

## Khi nào cần dùng?

Điều chỉnh bước từng tọa độ mà vẫn giảm ảnh hưởng của lịch sử xa.

## Tự kiểm tra

Nếu gradient hiện tại bằng 0 thì trạng thái v có về 0 ngay không?

<details><summary>Xem đáp án</summary>

Không, trừ trường hợp β=0 hoặc trạng thái trước đã bằng 0.

</details>

## Thuật ngữ liên quan

- [AdaGrad](./adagrad.md)
- [Adam](./adam.md)
- [Phương sai](./phuong-sai.md)
