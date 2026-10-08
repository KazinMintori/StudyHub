---
title: "Quy hoạch toàn phương (QP và QCQP)"
wikiTerm: quy-hoach-toan-phuong
prev: false
next: false
---

# Quy hoạch toàn phương (QP và QCQP)

QP cực tiểu một hàm toàn phương $\tfrac12 x^TPx + q^Tx + r$ với $P \succeq 0$ trên một đa diện. QCQP cho phép thêm các ràng buộc toàn phương lồi. Khác với LP, nghiệm của QP có thể nằm bên trong hoặc giữa một cạnh của đa diện. Khi thiếu điều kiện $P \succeq 0$, bài toán không lồi và nói chung rất khó.

<WikiUsage />

## Giải thích kỹ thuật

**Lồng nhau.** LP là QP với $P = 0$, QP là QCQP khi mọi ràng buộc toàn phương suy biến thành tuyến tính. Khi $P \succ 0$, nghiệm nếu có là duy nhất.

**Ví dụ của sách.** Bình phương tối thiểu có cận cho từng biến, khoảng cách giữa hai đa diện, phương sai lớn nhất của một biến ngẫu nhiên khi chỉ biết một phần phân phối, LP có chi phí ngẫu nhiên với chi phí tính đến rủi ro $\bar c^Tx + \gamma x^T\Sigma x$, và danh mục Markowitz cực tiểu $x^T\Sigma x$ với lợi suất tối thiểu. Nguồn: Convex Optimization, §4.4 và §4.4.1.

## Ví dụ

Khoảng cách giữa hai đa diện là giá trị tối ưu của một QP cực tiểu $\|x_1 - x_2\|_2^2$, với $x_1$ và $x_2$ lần lượt thuộc hai đa diện.

## Khi nào cần dùng?

Bình phương tối thiểu có ràng buộc, danh mục đầu tư Markowitz, phép chiếu lên đa diện.

## Câu hỏi ôn lại

Kẹp từng thành phần của nghiệm bình phương tối thiểu vào một hình hộp có cho nghiệm của QP có ràng buộc hộp không?

<details><summary>Xem đáp án</summary>

Nói chung không, trừ khi $A^TA$ chéo. Khi các biến tương quan với nhau, phải giải QP.

</details>

## Thuật ngữ liên quan

- [Quy hoạch tuyến tính (LP)](./quy-hoach-tuyen-tinh.md)
- [Ma trận nửa xác định dương](./ma-tran-psd.md)
- [Bình phương tối thiểu](./binh-phuong-toi-thieu.md)
