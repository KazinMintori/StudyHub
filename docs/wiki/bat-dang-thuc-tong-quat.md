---
title: "Bất đẳng thức tổng quát"
wikiTerm: bat-dang-thuc-tong-quat
prev: false
next: false
---

# Bất đẳng thức tổng quát

Với nón chính quy K, viết $x \preceq_K y$ khi $y - x \in K$. Nón chính quy là nón lồi, đóng, có phần trong khác rỗng và không chứa trọn đường thẳng nào. Thứ tự này thường không toàn phần, nên một tập có thể có nhiều phần tử tối thiểu mà không có phần tử nhỏ nhất.

<WikiUsage />

## Giải thích kỹ thuật

**Thứ tự từng thành phần và thứ tự ma trận.** Với $K = \mathbb R^n_+$, quan hệ $\preceq_K$ là so sánh từng tọa độ. Với $K = \mathbb S^n_+$, $X \preceq Y$ nghĩa là $Y - X$ nửa xác định dương, tức so sánh theo mọi dạng toàn phương chứ không theo từng phần tử.

**Pareto.** Trong tối ưu nhiều mục tiêu, các phương án tối ưu Pareto là các phần tử tối thiểu của tập vector chi phí đạt được theo thứ tự từng thành phần. Cực tiểu tổng có trọng số dương của các mục tiêu luôn cho một điểm Pareto, và khi bài toán lồi, mọi điểm Pareto đều tìm được theo cách này với một vector trọng số không âm khác 0. Nguồn: Convex Optimization, §2.4 và §2.6.3.

## Ví dụ

Với $K = \mathbb R^2_+$, hai điểm $(1, 3)$ và $(2, 2)$ không so sánh được, vì mỗi điểm nhỏ hơn điểm kia ở một tọa độ.

## Khi nào cần dùng?

So sánh vector chi phí của nhiều mục tiêu và so sánh ma trận theo thứ tự nửa xác định dương.

## Câu hỏi ôn lại

Phần tử tối thiểu khác phần tử nhỏ nhất thế nào?

<details><summary>Xem đáp án</summary>

Phần tử nhỏ nhất nhỏ hơn hoặc bằng mọi phần tử khác. Phần tử tối thiểu chỉ cần không có phần tử nào nhỏ hơn nó, và có thể không so sánh được với nhiều phần tử.

</details>

## Thuật ngữ liên quan

- [Nón lồi](./non-loi.md)
- [Nón đối ngẫu](./non-doi-ngau.md)
- [Ma trận nửa xác định dương](./ma-tran-psd.md)
