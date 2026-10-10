---
title: "Nón đối ngẫu"
wikiTerm: non-doi-ngau
prev: false
next: false
---

# Nón đối ngẫu

Nón đối ngẫu của tập K là $K^* = \{y : y^T x \ge 0 \text{ với mọi } x \in K\}$, gồm các vector tạo góc không quá $90^\circ$ với mọi phần tử của K. Nó luôn là một nón lồi đóng, kể cả khi K không lồi.

<WikiUsage />

## Giải thích kỹ thuật

**Hình học.** Mỗi $y \in K^*$ xác định một nửa không gian $\{x : y^T x \ge 0\}$ có biên đi qua gốc và chứa trọn $K$. Nếu $K$ là nón lồi đóng thì $K^{**} = K$, và nếu $K$ là nón chính quy thì $K^*$ cũng vậy.

**Các nón tự đối ngẫu.** $\mathbb R^n_+$, nón bậc hai và nón ma trận nửa xác định dương đều tự đối ngẫu. Đối ngẫu của nón chuẩn ứng với chuẩn đối ngẫu, chẳng hạn nón $\ell_1$ và nón $\ell_\infty$ là đối ngẫu của nhau.

**Vô hướng hóa.** Cực tiểu $\lambda^T z$ trên một tập với $\lambda$ thuộc phần trong của $K^*$ cho một phần tử tối thiểu theo thứ tự sinh bởi $K$. Nguồn: Convex Optimization, §2.6.

## Ví dụ

Nón $\mathbb R^2_+$ là nón tự đối ngẫu, bởi vì $y^T x \ge 0$ với mọi $x \succeq 0$ khi và chỉ khi $y \succeq 0$.

## Khi nào cần dùng?

Chọn trọng số hợp lệ khi vô hướng hóa nhiều mục tiêu, và làm nhân tử Lagrange cho ràng buộc nón.

## Câu hỏi ôn lại

Nón đối ngẫu của toàn không gian $\mathbb R^n$ là gì?

<details><summary>Xem đáp án</summary>

Chỉ gồm vector 0, vì $y^T x \ge 0$ với mọi x buộc $y = 0$.

</details>

## Thuật ngữ liên quan

- [Nón lồi](./non-loi.md)
- [Bất đẳng thức tổng quát](./bat-dang-thuc-tong-quat.md)
- [Hàm đối ngẫu Lagrange](./ham-doi-ngau.md)
