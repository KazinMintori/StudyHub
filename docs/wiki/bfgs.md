---
title: "BFGS"
wikiTerm: bfgs
prev: false
next: false
---

# BFGS

BFGS cập nhật một xấp xỉ Hessian hoặc Hessian nghịch đảo từ độ dời s và thay đổi gradient y. Điều kiện yᵀs>0 giúp giữ tính dương xác định của xấp xỉ nghịch đảo khi trạng thái trước đã dương xác định.

<WikiUsage />

## Giải thích kỹ thuật

**Cập nhật secant hạng thấp.** Đặt $s_k=x_{k+1}-x_k$, $y_k=g_{k+1}-g_k$, $\rho_k=1/(y_k^Ts_k)$. BFGS nghịch đảo cập nhật $M_k$ sao cho $M_{k+1}y_k=s_k$. Khi $M_k\succ0$ và $y_k^Ts_k>0$, ma trận mới vẫn dương xác định.

L-BFGS không lưu toàn bộ ma trận mà giữ một số cặp $(s,y)$ gần đây và dùng đệ quy hai vòng để tính hướng. Với gradient lô nhỏ, nhiễu trong $y$ có thể làm điều kiện độ cong khó thỏa. Nguồn: Deep Learning, §8.6 và Udell, Quasi-Newton Methods.

## Ví dụ

Nếu s=(1,0), y=(2,0), một xấp xỉ nghịch đảo phù hợp theo hướng này phải gửi y về s.

## Khi nào cần dùng?

Tạo hướng gần Newton mà không tính Hessian thật ở mỗi bước.

## Tự kiểm tra

Khi yᵀs≤0, có nên dùng nguyên công thức chia cho yᵀs không?

<details><summary>Xem đáp án</summary>

Không. Điều kiện độ cong đã hỏng; phần cài đặt phải bỏ hoặc sửa cập nhật.

</details>

## Thuật ngữ liên quan

- [Gradient](./gradient.md)
- [Hessian](./hessian.md)
- [Tìm kiếm đường và backtracking](./tim-kiem-duong.md)
