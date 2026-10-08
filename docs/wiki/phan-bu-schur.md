---
title: "Phần bù Schur"
wikiTerm: phan-bu-schur
prev: false
next: false
---

# Phần bù Schur

Với một ma trận đối xứng chia khối gồm các khối $A$, $B$, $B^T$, $C$ với $A$ khả nghịch, phần bù Schur của A là $S = C - B^TA^{-1}B$. Khi $A \succ 0$, ma trận khối nửa xác định dương khi và chỉ khi S nửa xác định dương. S cũng là giá trị nhỏ nhất của dạng toàn phương của ma trận khối theo khối biến thứ nhất.

<WikiUsage />

## Giải thích kỹ thuật

**Ma trận khối.** Với $X = \begin{bmatrix} A & B \\ B^T & C \end{bmatrix}$ và $A \succ 0$, giá trị nhỏ nhất theo $u$ của dạng toàn phương tại $(u, v)$ là $v^TSv$, đạt tại $u = -A^{-1}Bv$. Từ đó $X \succ 0 \iff A \succ 0,\ S \succ 0$, và nếu $A \succ 0$ thì $X \succeq 0 \iff S \succeq 0$. Ngoài ra $\det X = \det A \det S$.

**Ứng dụng.** Viết thành LMI các ràng buộc $x^Tx/y \le t$, $\|u\|_2 \le t$ và chuẩn phổ $\|A(x)\|_2 \le t$, nhờ đó mọi SOCP là SDP. Nguồn: Convex Optimization, §A.5.5 và §4.6.3.

## Ví dụ

Ràng buộc $\|u\|_2 \le t$ tương đương với việc ma trận khối có khối trên trái $tI$, cột $u$ và góc dưới phải $t$ nửa xác định dương.

## Khi nào cần dùng?

Viết ràng buộc phi tuyến thành bất đẳng thức ma trận tuyến tính, khử một khối biến trong hàm toàn phương.

## Câu hỏi ôn lại

Ma trận có hàng (2, 1) và (1, 1) có dương xác định không?

<details><summary>Xem đáp án</summary>

Có. Phần bù Schur của phần tử 2 là $1 - \tfrac12 = \tfrac12 > 0$, và phần tử 2 dương.

</details>

## Thuật ngữ liên quan

- [Ma trận nửa xác định dương](./ma-tran-psd.md)
- [Quy hoạch nửa xác định (SDP)](./quy-hoach-nua-xac-dinh.md)
- [Quy hoạch nón bậc hai (SOCP)](./quy-hoach-non-bac-hai.md)
