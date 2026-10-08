---
title: "Gradient ngẫu nhiên và SGD"
wikiTerm: gradient-ngau-nhien
prev: false
next: false
---

# Gradient ngẫu nhiên và SGD

Gradient lô nhỏ là trung bình gradient trên một mẫu dữ liệu được chọn theo quy tắc cụ thể. Nó có thể không chệch so với gradient toàn bộ dữ liệu nhưng vẫn dao động ở từng bước. SGD cập nhật tham số bằng ước lượng này.

<WikiUsage />

## Giải thích kỹ thuật

**Không chệch cần một mô hình lấy mẫu.** Nếu chỉ số $I$ được lấy đều và độc lập trên $\{1,\ldots,N\}$ khi $\theta$ đang cố định, thì $E[\nabla\ell_I(\theta)\mid\theta]=\nabla J(\theta)$. Trung bình $B$ mẫu độc lập giảm phương sai từng tọa độ theo hệ số $1/B$.

Xáo trộn rồi duyệt hết một epoch, lấy mẫu không hoàn lại và lấy mẫu có trọng số là những quy trình khác. Công thức kỳ vọng và phương sai phải được viết theo đúng quy tắc đó. Gradient nhỏ của một lô không phải điều kiện dừng đáng tin cậy cho toàn bộ dữ liệu. Nguồn: Deep Learning, §8.1 và §8.3.

## Ví dụ

Hai gradient mẫu 0 và −2 có trung bình −1. Trong khi đó, lấy riêng một mẫu cho gradient 0 hoặc −2.

## Khi nào cần dùng?

Huấn luyện mô hình khi gradient toàn bộ dữ liệu quá tốn kém.

## Tự kiểm tra

Gradient lô nhỏ không chệch có bảo đảm loss toàn bộ giảm ở từng bước không?

<details><summary>Xem đáp án</summary>

Không. Tính không chệch là phát biểu về kỳ vọng, không phải từng lần lấy mẫu.

</details>

## Thuật ngữ liên quan

- [Gradient](./gradient.md)
- [Kỳ vọng](./ky-vong.md)
- [Phương sai](./phuong-sai.md)
- [Momentum và Nesterov](./momentum-nesterov.md)
