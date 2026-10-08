---
title: "Tổ hợp & giai thừa"
wikiTerm: to-hop
prev: false
next: false
---

# Tổ hợp & giai thừa

Giai thừa $n!=1\cdot2\cdots n$, với $0!=1$. Chọn $k$ phần tử từ $n$ phần tử phân biệt, không xét thứ tự, có $\binom nk=\frac{n!}{k!(n-k)!}$ cách. Nếu xét thứ tự hoặc cho phép lặp thì phải dùng mô hình đếm khác.

<WikiUsage />

## Giải thích kỹ thuật

**Đếm theo mô hình.** Chọn k từ n không xét thứ tự, không lặp dùng C(n,k). Chọn có thứ tự, không lặp dùng $\frac{n!}{(n-k)!}$. Nếu chọn có thứ tự và có lặp, mỗi vị trí có n lựa chọn, nên có $n^k$ dãy.

Trước khi áp dụng, nêu rõ các đối tượng có phân biệt không, thứ tự có quan trọng không và có được lặp không.

## Ví dụ

Chọn 2 người từ 4 người có $C(4,2)=6$ nhóm.

## Khi nào cần dùng?

Thiết lập xác suất rời rạc và phân phối nhị thức.

## Tự kiểm tra

C(3,1) bằng bao nhiêu?

<details><summary>Xem đáp án</summary>

3.

</details>

## Thuật ngữ liên quan

- [Quan hệ](./quan-he.md)
- [Quy nạp toán học](./quy-nap.md)
- [Tập hợp](./tap-hop.md)
