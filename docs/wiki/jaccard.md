---
title: "Độ tương đồng Jaccard"
wikiTerm: jaccard
prev: False
next: False
---

# Độ tương đồng Jaccard

Với hai tập có hợp khác rỗng, độ tương đồng Jaccard là kích thước giao chia kích thước hợp. Giá trị nằm từ 0 đến 1. Hai tập cùng rỗng cần một quy ước riêng, chẳng hạn gán độ tương đồng bằng 1.

<WikiUsage />

## Giải thích kỹ thuật

Đặt $c=|A\cap B|$ là số phần tử chung và $u=|A\cup B|$ là số phần tử thuộc ít nhất một tập. Khi $u>0$, độ tương đồng là $J(A,B)=c/u$. Khoảng cách Jaccard là $d_J(A,B)=1-J(A,B)$.

Nếu dùng quy ước $J(\varnothing,\varnothing)=1$, khoảng cách giữa hai tập rỗng bằng 0. Với một tập rỗng và một tập khác rỗng, độ tương đồng bằng 0. Jaccard so sánh tập đã biểu diễn, không trực tiếp đo nghĩa văn bản hoặc chứng minh quan hệ sao chép.

## Ví dụ

Hai tập {a, b, c, d} và {b, c, d, e} có giao gồm 3 phần tử, hợp gồm 5 phần tử, nên độ tương đồng bằng 3/5.

## Khi nào cần dùng?

So sánh độ trùng của hai tập shingle, tập từ hoặc tập mục.

## Câu hỏi ôn lại

Jaccard bằng 1 có chứng minh hai văn bản gốc giống hệt nhau không?

<details><summary>Xem đáp án</summary>

Không. Nó chứng minh hai tập biểu diễn bằng nhau. Phép biểu diễn có thể đã bỏ mất thông tin của văn bản gốc.

</details>

## Thuật ngữ liên quan

- [Shingling](./shingling.md)
- [MinHash](./minhash.md)
- [Băm nhạy cảm cục bộ](./lsh.md)
