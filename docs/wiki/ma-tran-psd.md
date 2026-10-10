---
title: "Ma trận nửa xác định dương"
wikiTerm: ma-tran-psd
prev: false
next: false
---

# Ma trận nửa xác định dương

Ma trận đối xứng thực P là nửa xác định dương (PSD), viết $P\succeq 0$, nếu $v^{T}Pv\ge 0$ với mọi vector v. P dương xác định (PD) nếu $v^{T}Pv>0$ với mọi v khác 0. Dấu từng phần tử không quyết định PSD.

<WikiUsage />

## Giải thích kỹ thuật

Với $P=P^T$, điều kiện $P\succeq0$ tương đương mọi trị riêng của $P$ không âm. Điều kiện $P\succ0$ tương đương mọi trị riêng dương. Ký hiệu $P\succeq Q$ nghĩa là $P-Q$ PSD, khác so sánh từng phần tử.

Ví dụ ma trận $\begin{bmatrix}1&-1\\-1&1\end{bmatrix}$ là PSD dù có phần tử âm, vì dạng toàn phương là $(v_1-v_2)^2 \ge 0$. Với tích $A^TA$, tính PD đòi hỏi các cột của $A$ độc lập tuyến tính, tức phương trình $Av=0$ chỉ có nghiệm duy nhất $v=0$. Nguồn: Convex Optimization, §A.5.2 và §2.2.5.

## Ví dụ

Ma trận

$$P=\begin{bmatrix}1&2\\2&1\end{bmatrix}$$

không PSD: Với $v=(1,-1)^T$, ta được $v^TPv=-2$. Ngược lại, $A^TA$ luôn PSD vì $v^TA^TAv=\|Av\|_2^2\ge0$.

## Khi nào cần dùng?

Kiểm Hessian và ràng buộc ma trận. Nhận biết khi nào hệ Newton có hướng giảm.

## Tự kiểm tra

Ma trận diag(1,0) là PSD hay PD?

<details><summary>Xem đáp án</summary>

PSD, không PD: Với $v=(0,1)$ khác 0, dạng toàn phương bằng 0.

</details>

## Thuật ngữ liên quan

- [Ma trận](./ma-tran.md)
- [Trị riêng &amp; vector riêng](./tri-rieng.md)
- [Hessian](./hessian.md)
