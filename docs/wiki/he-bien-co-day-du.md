---
title: "Hệ đầy đủ các biến cố"
wikiTerm: he-bien-co-day-du
prev: False
next: False
---

# Hệ đầy đủ các biến cố

Hệ đầy đủ là một họ biến cố đôi một xung khắc và có hợp bằng toàn bộ không gian mẫu. Mỗi kết quả thuộc đúng một nhánh. Khi dùng xác suất có điều kiện theo từng nhánh, chỉ sử dụng nhánh có xác suất dương.

<WikiUsage />

## Giải thích kỹ thuật

Với $B_1,\ldots,B_m$ tạo thành hệ đầy đủ và mỗi nhánh có xác suất dương, đặt $q_i=P(B_i)P(A\mid B_i)$. Khi đó:

$$
P(A)=q_1+q_2+\cdots+q_m.
$$

Các đóng góp không đếm trùng vì các nhánh rời nhau. Nếu $P(A)>0$, hậu nghiệm ở nhánh $i$ bằng $q_i/P(A)$. Xem [Tính toán xác suất](/xac-suat-thong-ke/bai-giang/10-tinh-toan-xac-suat).

## Ví dụ

Ba nguồn gia công giày ở Việt Nam, Trung Quốc và Indonesia tạo thành hệ đầy đủ khi mỗi đôi thuộc đúng một nguồn và kho chỉ gồm ba nguồn đó.

## Khi nào cần dùng?

Chia bài toán thành các nhánh để dùng xác suất toàn phần và công thức Bayes.

## Câu hỏi ôn lại

Chỉ có hợp bằng không gian mẫu đã đủ để là hệ đầy đủ chưa?

<details><summary>Xem đáp án</summary>

Chưa. Các nhánh còn phải đôi một xung khắc để mỗi kết quả được đếm đúng một lần.

</details>

## Thuật ngữ liên quan

- [Không gian mẫu](./khong-gian-mau.md)
- [Xác suất có điều kiện](./xac-suat-co-dieu-kien.md)
- [Độc lập](./doc-lap.md)
