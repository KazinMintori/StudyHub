---
title: "Điểm và miền khả thi"
wikiTerm: mien-kha-thi
prev: false
next: false
---

# Điểm và miền khả thi

Điểm khả thi là một lựa chọn thỏa đồng thời mọi ràng buộc và thuộc miền xác định của các hàm. Miền khả thi là tập tất cả các điểm như vậy. Khả thi chỉ nói điểm hợp lệ, chưa nói điểm đó tối ưu.

<WikiUsage />

## Giải thích kỹ thuật

**Khả thi được kiểm trước tối ưu.** Với bài có miền chung $D$, bất đẳng thức $f_i(x)\le0$ và đẳng thức $h_j(x)=0$, miền khả thi là $D\cap\bigcap_i\{x:f_i(x)\le0\}\cap\bigcap_j\{x:h_j(x)=0\}$. Chỉ cần một điều kiện sai là điểm không khả thi.

Miền khả thi rỗng làm bài toán vô nghiệm. Miền khác rỗng nhưng không đóng hoặc không bị chặn có thể khiến infimum không đạt. Vì thế “tìm được một giá trị mục tiêu nhỏ” và “tìm được một nghiệm của bài toán” là hai phát biểu khác nhau. Nguồn: Convex Optimization, §4.1.

## Ví dụ

Trong bài min (x−2)² với x≤1, x=0 và x=1 đều khả thi; x=2 không khả thi dù cho mục tiêu bằng 0.

## Khi nào cần dùng?

Kiểm tra một nghiệm trước khi so giá trị mục tiêu hoặc áp dụng KKT.

## Tự kiểm tra

Một điểm có giá trị mục tiêu nhỏ nhưng vi phạm một ràng buộc có phải nghiệm khả thi không?

<details><summary>Xem đáp án</summary>

Không. Điểm phải thỏa tất cả ràng buộc.

</details>

## Thuật ngữ liên quan

- [Tập lồi](./tap-loi.md)
- [Infimum](./infimum.md)
- [Điều kiện KKT](./kkt.md)
