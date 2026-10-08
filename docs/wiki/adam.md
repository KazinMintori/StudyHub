---
title: "Adam"
wikiTerm: adam
prev: false
next: false
---

# Adam

Adam theo dõi trung bình mũ của gradient và của bình phương gradient, rồi hiệu chỉnh ảnh hưởng của việc khởi tạo hai trạng thái bằng 0. Phép chia và căn được thực hiện theo từng tọa độ.

<WikiUsage />

## Giải thích kỹ thuật

**Hai trung bình mũ và hiệu chỉnh đầu quá trình.** Adam dùng $m_t$ cho gradient có dấu, $v_t$ cho bình phương gradient, rồi chia lần lượt cho $1-\beta_1^t$ và $1-\beta_2^t$. Với gradient hằng, phép chia loại đúng hệ số thiếu do khởi tạo 0.

Hiệu chỉnh này không có nghĩa mọi $\widehat m_t$ đều là ước lượng không chệch của gradient tại tham số hiện tại trong một quá trình học thay đổi. Trạng thái của bộ tối ưu gồm $m,v,t$. Nếu tệp lưu thiếu một phần trạng thái thì bước tiếp theo sẽ thay đổi. Nguồn: Kingma & Ba, Adam, Algorithm 1.

## Ví dụ

Với $g_1=2$, $\beta_1=0{,}9$, $\beta_2=0{,}999$, ta được $m_1=0{,}2$, $v_1=0{,}004$. Sau hiệu chỉnh: $\hat m_1=2$, $\hat v_1=4$.

## Khi nào cần dùng?

Huấn luyện mô hình với tốc độ học thích nghi theo tọa độ.

## Tự kiểm tra

Có thể thay trung bình bình phương gradient bằng bình phương trung bình gradient không?

<details><summary>Xem đáp án</summary>

Không. Gradient 2 và −2 có trung bình 0 nhưng trung bình bình phương bằng 4.

</details>

## Thuật ngữ liên quan

- [Gradient ngẫu nhiên và SGD](./gradient-ngau-nhien.md)
- [Momentum và Nesterov](./momentum-nesterov.md)
- [RMSProp](./rmsprop.md)
