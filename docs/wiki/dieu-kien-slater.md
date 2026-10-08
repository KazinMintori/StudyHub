---
title: "Điều kiện Slater"
wikiTerm: dieu-kien-slater
prev: false
next: false
---

# Điều kiện Slater

Trong một bài lồi, Slater yêu cầu có một điểm thuộc nội tương đối của miền, thỏa các đẳng thức và thỏa chặt các bất đẳng thức phi affine. Đây là điều kiện đủ thường dùng để có đối ngẫu mạnh, không phải điều kiện cần trong mọi bài.

<WikiUsage />

## Giải thích kỹ thuật

**Nội tương đối tránh loại nhầm miền thấp chiều.** Nếu miền chung nằm trên một không gian affine thấp chiều, nội thông thường có thể rỗng dù bài toán hoàn toàn hợp lệ. Slater dùng $\operatorname{relint}D$ để xét phần trong theo bao affine của miền.

Với bài lồi, tồn tại điểm thỏa chặt các bất đẳng thức phi affine và thỏa đẳng thức là điều kiện đủ cho đối ngẫu mạnh. Các bất đẳng thức affine có một phiên bản điều kiện yếu hơn. Slater không phải tiêu chuẩn duy nhất và không phải điều kiện cần. Nguồn: Convex Optimization, §2.1.3 và §5.2.3.

## Ví dụ

Với ràng buộc $x\le 1$ trên miền số thực, $x=0$ là điểm thỏa chặt vì $0<1$.

## Khi nào cần dùng?

Biết khi nào có thể dùng nhân tử đối ngẫu và KKT như điều kiện cần.

## Tự kiểm tra

Không tìm được điểm Slater có chứng minh đối ngẫu mạnh sai không?

<details><summary>Xem đáp án</summary>

Không. Slater là điều kiện đủ, nên việc không thỏa Slater chưa bác bỏ đối ngẫu mạnh.

</details>

## Thuật ngữ liên quan

- [Tập lồi](./tap-loi.md)
- [Đối ngẫu mạnh và khoảng cách đối ngẫu](./doi-ngau-manh.md)
- [Điều kiện KKT](./kkt.md)
