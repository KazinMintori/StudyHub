---
title: "Điều chuẩn: ridge và lasso"
wikiTerm: dieu-chuan
prev: false
next: false
---

# Điều chuẩn: ridge và lasso

Điều chuẩn thêm vào hàm mục tiêu một số hạng phạt độ lớn của tham số. Ridge, hay điều chuẩn Tikhonov, cực tiểu $\|Ax - b\|_2^2 + \mu\|x\|_2^2$ và có nghiệm $(A^TA + \mu I)^{-1}A^Tb$, luôn tồn tại và duy nhất khi $\mu > 0$. Lasso dùng $\mu\|x\|_1$ thay cho $\mu\|x\|_2^2$ và cho nghiệm có thành phần bằng đúng 0. Cả hai là vô hướng hóa của một bài toán hai mục tiêu giữa sai số và độ lớn tham số.

<WikiUsage />

## Giải thích kỹ thuật

**Đường đánh đổi.** Khi $\mu$ chạy từ 0 tới vô hạn, nghiệm ridge $x(\mu)$ đi từ nghiệm bình phương tối thiểu chuẩn nhỏ nhất $A^\dagger b$ về 0, và vạch ra đường đánh đổi giữa $\|Ax - b\|_2^2$ và $\|x\|_2^2$. Chuẩn $\ell_1$ là một xấp xỉ lồi của số thành phần khác 0, vốn không phải hàm tựa lồi, nên lasso được dùng như một cách chọn đặc trưng.

**Biến thể.** Điều chuẩn trơn $\|\Delta x\|_2^2$ với $\Delta$ là toán tử sai phân phạt độ cong thay vì độ lớn. Trọng số $\mu$ cần được chọn bằng một tiêu chí ngoài bài toán, chẳng hạn sai số trên dữ liệu kiểm định. Nguồn: Convex Optimization, §6.3 và §4.7.6.

## Ví dụ

Với cùng dữ liệu, ridge làm các hệ số co dần về 0, còn lasso đưa một hệ số về đúng 0 khi trọng số vượt một ngưỡng.

## Khi nào cần dùng?

Chống quá khớp, ổn định hệ phương trình gần suy biến, chọn đặc trưng.

## Câu hỏi ôn lại

Lasso cho nghiệm thưa còn ridge thì không. Hình học nào giải thích điều đó?

<details><summary>Xem đáp án</summary>

Quả cầu chuẩn $\ell_1$ có các đỉnh nằm trên các trục, nên đường mức của sai số thường chạm nó tại một đỉnh, nơi một tọa độ bằng 0.

</details>

## Thuật ngữ liên quan

- [Bình phương tối thiểu](./binh-phuong-toi-thieu.md)
- [Tối ưu vector và điểm Pareto](./toi-uu-pareto.md)
- [Quy hoạch toàn phương (QP và QCQP)](./quy-hoach-toan-phuong.md)
