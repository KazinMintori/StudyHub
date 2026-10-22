---
title: "Hiệp phương sai"
wikiTerm: hiep-phuong-sai
prev: False
next: False
---

# Hiệp phương sai

Hiệp phương sai đo trung bình tích hai độ lệch khỏi kỳ vọng. Với hai biến có moment bậc hai hữu hạn, độc lập kéo theo hiệp phương sai bằng 0. Chiều ngược lại không đúng nói chung.

<WikiUsage />

## Giải thích kỹ thuật

Với các moment bậc hai hữu hạn, đặt $\mu_X=E(X)$ và $\mu_Y=E(Y)$. Hai độ lệch được ký hiệu là:

$$
\begin{aligned}
U&=X-\mu_X,\\
V&=Y-\mu_Y.
\end{aligned}
$$

Hiệp phương sai là kỳ vọng của tích hai độ lệch:

$$
\operatorname{Cov}(X,Y)=E[UV].
$$

Giá trị bằng 0 chỉ loại bỏ liên hệ tuyến tính đo bằng đại lượng này. Nếu cả hai phương sai dương, chia hiệp phương sai cho tích hai độ lệch chuẩn cho hệ số tương quan. Cộng hằng số không đổi hiệp phương sai, còn đổi dấu một biến làm đổi dấu hiệp phương sai.

Xem [Hiệp phương sai và kỳ vọng có điều kiện](/xac-suat-thong-ke/bai-giang/32-hiep-phuong-sai-va-ky-vong-co-dieu-kien).

## Ví dụ

Nếu X nhận đều các giá trị -1, 0, 1 và Y là bình phương của X, hiệp phương sai bằng 0 nhưng Y vẫn do X xác định.

## Khi nào cần dùng?

Tính phương sai của tổng các biến phụ thuộc và phân biệt phụ thuộc với liên hệ tuyến tính.

## Câu hỏi ôn lại

Không tương quan có bảo đảm độc lập không?

<details><summary>Xem đáp án</summary>

Không. Ví dụ X đối xứng quanh 0 và Y là bình phương của X cho một phản ví dụ.

</details>

## Thuật ngữ liên quan

- [Phương sai](./phuong-sai.md)
- [Phân phối đồng thời](./phan-phoi-dong-thoi.md)
- [Ma trận hiệp phương sai](./ma-tran-hiep-phuong-sai.md)
