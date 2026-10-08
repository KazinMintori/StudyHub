---
title: "Quy hoạch nón bậc hai (SOCP)"
wikiTerm: quy-hoach-non-bac-hai
prev: false
next: false
---

# Quy hoạch nón bậc hai (SOCP)

SOCP cực tiểu một hàm tuyến tính với các ràng buộc $\|A_ix + b_i\|_2 \le c_i^Tx + d_i$, mỗi ràng buộc đòi một vector phụ thuộc affine vào x nằm trong nón bậc hai. SOCP chứa LP và QCQP như trường hợp riêng, và xuất hiện tự nhiên khi dữ liệu bất định, như trong LP bền vững và ràng buộc xác suất với hệ số Gauss.

<WikiUsage />

## Giải thích kỹ thuật

**Từ bất định tới chuẩn.** Nếu $a$ chỉ được biết nằm trong ellipsoid $\{\bar a + Pu : \|u\|_2 \le 1\}$, thì $\sup a^Tx = \bar a^Tx + \|P^Tx\|_2$ theo bất đẳng thức Cauchy–Schwarz, nên ràng buộc bền vững là một ràng buộc nón bậc hai. Nếu $a$ là Gauss với trung bình $\bar a$ và hiệp phương sai $\Sigma$, ràng buộc $\operatorname{prob}(a^Tx \le b) \ge \eta$ tương đương $\bar a^Tx + \Phi^{-1}(\eta)\|\Sigma^{1/2}x\|_2 \le b$, lồi khi $\eta \ge \tfrac12$.

**Ràng buộc hyperbolic.** Với $y, z \ge 0$, điều kiện $x^Tx \le yz$ tương đương $\|(2x, y - z)\|_2 \le y + z$. Nguồn: Convex Optimization, §4.4.2 và bài tập 4.26.

## Ví dụ

Ràng buộc $a^Tx \le b$ đúng với mọi $a$ trong hình cầu tâm $\bar a$ bán kính $\rho$ tương đương với $\bar a^Tx + \rho\|x\|_2 \le b$.

## Khi nào cần dùng?

Tối ưu bền vững, ràng buộc xác suất, các bài toán chứa chuẩn Euclid.

## Câu hỏi ôn lại

Có được bình phương hai vế của $\|Ax + b\|_2 \le c^Tx + d$ không?

<details><summary>Xem đáp án</summary>

Chỉ khi giữ thêm điều kiện $c^Tx + d \ge 0$. Bình phương vô điều kiện có thể thêm nghiệm sai và làm mất dạng lồi.

</details>

## Thuật ngữ liên quan

- [Nón lồi](./non-loi.md)
- [Quy hoạch toàn phương (QP và QCQP)](./quy-hoach-toan-phuong.md)
- [Quy hoạch nửa xác định (SDP)](./quy-hoach-nua-xac-dinh.md)
