---
title: "Ma trận hiệp phương sai"
wikiTerm: ma-tran-hiep-phuong-sai
prev: false
next: false
---

# Ma trận hiệp phương sai

Ma trận hiệp phương sai của vector ngẫu nhiên ghi phương sai trên đường chéo và hiệp phương sai giữa hai thành phần ở ngoài đường chéo. Nó đối xứng và nửa xác định dương. Hiệp phương sai bằng 0 không tự suy ra độc lập.

<WikiUsage />

## Giải thích kỹ thuật

**Định nghĩa từ độ lệch quanh kỳ vọng.** Với vector ngẫu nhiên $X$, $\Sigma=E[(X-E[X])(X-E[X])^T]$ khi moment bậc hai tồn tại. Vì $v^T\Sigma v=\operatorname{Var}(v^TX)\ge0$, $\Sigma$ luôn PSD.

Phần tử $\Sigma_{ij}=\operatorname{Cov}(X_i,X_j)$ đo biến thiên tuyến tính cùng nhau. Chuẩn hóa cho ma trận tương quan với đường chéo bằng 1 khi các phương sai dương. Hiệp phương sai bằng 0 chỉ nói không tương quan tuyến tính; nhìn chung chưa đủ để kết luận độc lập. Nguồn: Convex Optimization, §A.2 và §7.1.

## Ví dụ

Nếu X=Y nhận −1 hoặc 1 với xác suất bằng nhau thì Var(X)=Var(Y)=Cov(X,Y)=1.

## Khi nào cần dùng?

Mô tả nhiễu tương quan, phân phối Gauss nhiều chiều và độ bất định.

## Tự kiểm tra

Phần tử đường chéo thứ i của ma trận hiệp phương sai là gì?

<details><summary>Xem đáp án</summary>

Là phương sai của thành phần thứ i.

</details>

## Thuật ngữ liên quan

- [Phương sai](./phuong-sai.md)
- [Ma trận nửa xác định dương](./ma-tran-psd.md)
- [Phân phối Gauss](./phan-phoi-gauss.md)
