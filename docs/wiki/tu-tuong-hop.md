---
title: "Hàm tự tương hợp (self-concordant)"
wikiTerm: tu-tuong-hop
prev: false
next: false
---

# Hàm tự tương hợp (self-concordant)

Tự tương hợp là điều kiện khống chế tốc độ thay đổi của đạo hàm bậc hai bằng chính thang độ cong hiện tại. Điều kiện này giúp phân tích bước Newton; nó không phải tên khác của tính lồi.

<WikiUsage />

## Giải thích kỹ thuật

**Định nghĩa theo mọi đường.** Trong một chiều, chuẩn tự tương hợp dùng $|f\prime\prime\prime(x)|\le2[f\prime\prime(x)]^{3/2}$. Trong nhiều chiều, áp dụng điều kiện ấy cho $t\mapsto f(x+tv)$ với mọi $x,v$ sao cho đường nằm trong miền.

Điều kiện bất biến affine thích hợp này kiểm soát mức Hessian đổi trong chuẩn cục bộ, nhờ đó Newton decrement có thể quyết định khi nào bước Newton đầy đủ an toàn. Các hằng số và bảo đảm vòng lặp cần đúng phiên bản định nghĩa đang dùng. Nguồn: Convex Optimization, §9.6.

## Ví dụ

f(x)=−log x trên x>0 thỏa |f‴(x)|=2[f″(x)]³ᐟ²=2/x³.

## Khi nào cần dùng?

Phân tích Newton cho hàm barrier và các bài tối ưu lồi.

## Tự kiểm tra

Mọi hàm lồi có tự tương hợp không?

<details><summary>Xem đáp án</summary>

Không. Tự tương hợp là một giả thiết bổ sung.

</details>

## Thuật ngữ liên quan

- [Hessian](./hessian.md)
- [Tìm kiếm đường và backtracking](./tim-kiem-duong.md)
- [Điều kiện KKT](./kkt.md)
