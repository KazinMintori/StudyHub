---
title: "Quy hoạch nửa xác định (SDP)"
wikiTerm: quy-hoach-nua-xac-dinh
prev: false
next: false
---

# Quy hoạch nửa xác định (SDP)

SDP cực tiểu một hàm tuyến tính với ràng buộc bất đẳng thức ma trận tuyến tính, tức một ma trận đối xứng phụ thuộc affine vào x phải nửa xác định dương hoặc nửa xác định âm. Miền khả thi lồi nhưng có thể có biên cong. SDP chứa LP, QP và SOCP như trường hợp riêng.

<WikiUsage />

## Giải thích kỹ thuật

**Dạng chuẩn.** Tương tự LP, SDP dạng chuẩn cực tiểu $\operatorname{tr}(CX)$ với $\operatorname{tr}(A_iX) = b_i$ và $X \succeq 0$. Nhiều LMI và bất đẳng thức tuyến tính gộp được thành một LMI khối chéo. Một LMI chéo là một hệ bất đẳng thức tuyến tính.

**Ví dụ.** Ma trận tương quan của ba biến phải nửa xác định dương. Giữ $\rho_{23} = c$, tập các cặp $(\rho_{12}, \rho_{13})$ hợp lệ là ellipse $\rho_{12}^2 + \rho_{13}^2 - 2c\rho_{12}\rho_{13} \le 1 - c^2$. Cực tiểu trị riêng lớn nhất $\lambda_{\max}(A(x))$ là SDP: cực tiểu $t$ với $tI - A(x) \succeq 0$. Nguồn: Convex Optimization, §4.6.

## Ví dụ

Với $\rho_{12} = \rho_{23} = 0.8$, điều kiện ma trận tương quan nửa xác định dương buộc $\rho_{13} \in [0.28, 1]$.

## Khi nào cần dùng?

Cực tiểu trị riêng lớn nhất hay chuẩn phổ của ma trận, ma trận tương quan hợp lệ, điều khiển, nới lỏng bài toán tổ hợp.

## Câu hỏi ôn lại

Ràng buộc $X \succeq 0$ có nghĩa là mọi phần tử của X không âm không?

<details><summary>Xem đáp án</summary>

Không. Nó nghĩa là $v^TXv \ge 0$ với mọi v. Một ma trận có phần tử âm vẫn có thể nửa xác định dương, và ngược lại.

</details>

## Thuật ngữ liên quan

- [Ma trận nửa xác định dương](./ma-tran-psd.md)
- [Phần bù Schur](./phan-bu-schur.md)
- [Bất đẳng thức tổng quát](./bat-dang-thuc-tong-quat.md)
