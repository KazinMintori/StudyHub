---
title: "Tập lồi"
wikiTerm: tap-loi
prev: false
next: false
---

# Tập lồi

Tập C là lồi khi với mọi x,y thuộc C và mọi $\theta$ trong [0,1], điểm $\theta x+(1-\theta )y$ vẫn thuộc C. Điều kiện phải đúng với mọi đoạn nối. Thử vài điểm chỉ minh họa, không chứng minh tính lồi.

<WikiUsage />

## Giải thích kỹ thuật

Tập lồi giữ các tổ hợp có trọng số không âm và tổng bằng 1. Tập affine chỉ đòi tổng trọng số bằng 1, nên cho phép trọng số âm. Nó chứa cả đường thẳng qua hai điểm.

Giao các tập lồi là lồi. Ảnh và ảnh ngược qua ánh xạ affine giữ tính lồi, kể cả khi ánh xạ không khả nghịch. Chuẩn, nửa không gian và đa diện là các cách mô tả miền lồi. Nguồn: Convex Optimization, §2.1–2.3.

## Ví dụ

Hình tròn đặc là tập lồi, trong khi đường tròn không lồi vì trung điểm của hai điểm đối diện là tâm và không nằm trên đường tròn.

## Khi nào cần dùng?

Nhận diện miền khả thi và dùng tính chất tối ưu cục bộ của bài toán lồi.

## Tự kiểm tra

Hợp của hai tập lồi có luôn lồi không?

<details><summary>Xem đáp án</summary>

Không. $[-2,-1]$ hợp [1,2] bỏ mất trung điểm 0 của −1 và 1.

</details>

## Thuật ngữ liên quan

- [Tổ hợp lồi](./to-hop-loi.md)
- [Hàm lồi](./ham-loi.md)
- [Tập hợp](./tap-hop.md)
