---
title: "Gradient liên hợp"
wikiTerm: gradient-lien-hop
prev: false
next: false
---

# Gradient liên hợp

Gradient liên hợp tuyến tính là thuật toán lặp để giải hệ Hz=b khi H đối xứng dương xác định. Nó tạo các hướng liên hợp theo H và chỉ cần phép nhân H với vector, nên có thể tránh lưu một Hessian dày.

<WikiUsage />

## Giải thích kỹ thuật

**Các hướng liên hợp theo ma trận.** Với $H\succ0$, hai hướng $p_i,p_j$ liên hợp khi $p_i^THp_j=0$. CG xây các hướng như vậy từ phần dư $r=b-Hz$, nhờ đó trong số học chính xác giải hệ $n$ chiều sau nhiều nhất $n$ bước.

Trong số học máy, tính trực giao liên hợp bị ảnh hưởng bởi làm tròn; tiền điều kiện có thể cải thiện tốc độ. CG tuyến tính giải hệ SPD khác với CG phi tuyến dùng tìm kiếm đường cho một hàm tổng quát. Nguồn: Shewchuk, An Introduction to the Conjugate Gradient Method, §8.

## Ví dụ

Với H=diag(1,2), b=(1,1), nghiệm của Hz=b là z=(1,1/2).

## Khi nào cần dùng?

Giải gần đúng hệ Newton lớn hoặc hệ SPD.

## Tự kiểm tra

Có thể áp dụng trực tiếp công thức CG tuyến tính khi Hessian bất định không?

<details><summary>Xem đáp án</summary>

Không. Giả thiết SPD phải được bảo đảm hoặc xử lý bằng phương pháp khác.

</details>

## Thuật ngữ liên quan

- [Hessian](./hessian.md)
- [Hệ phương trình tuyến tính](./he-phuong-trinh.md)
- [BFGS](./bfgs.md)
