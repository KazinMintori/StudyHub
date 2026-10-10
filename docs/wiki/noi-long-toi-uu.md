---
title: "Nới lỏng bài toán"
wikiTerm: noi-long-toi-uu
prev: false
next: false
---

# Nới lỏng bài toán

Nới lỏng mở rộng miền khả thi hoặc bỏ bớt điều kiện để tạo một bài dễ hơn. Với bài cực tiểu và cùng hàm mục tiêu, giá trị của bài nới lỏng là cận dưới. Tuy nhiên, nghiệm của bài nới lỏng chưa chắc hợp lệ cho bài gốc.

<WikiUsage />

## Giải thích kỹ thuật

**Chiều của cận phụ thuộc min hay max.** Nếu $C\subseteq\widetilde C$, thì với bài min, $\inf_{x\in\widetilde C}f(x)\le\inf_{x\in C}f(x)$. Với bài max, chiều đảo lại. Đây là quan hệ tập hợp, không cần hai bài đều lồi.

Nới lỏng thường đi cùng một phép thu hồi nghiệm: Làm tròn, chiếu hoặc một quy tắc gần đúng khác. Giá trị nới lỏng cho cận. Giá trị của ứng viên khả thi cho cận phía còn lại. Chỉ khi hai cận gặp nhau mới có chứng nhận tối ưu. Nguồn: Convex Optimization, §4.1 và các ví dụ về nới lỏng trong §5.1.2.

## Ví dụ

Thay $x\in \{0,1\}$ bằng $0\le x\le 1$ cho phép thêm các giá trị như $x=0$,4.

## Khi nào cần dùng?

Tạo cận tối ưu và thiết kế thuật toán xấp xỉ cho bài rời rạc hoặc khó.

## Tự kiểm tra

Nghiệm tối ưu của bài nới lỏng có luôn là nghiệm của bài gốc không?

<details><summary>Xem đáp án</summary>

Không. Phải kiểm lại các ràng buộc đã được nới.

</details>

## Thuật ngữ liên quan

- [Điểm và miền khả thi](./mien-kha-thi.md)
- [Infimum](./infimum.md)
- [Đối ngẫu mạnh và khoảng cách đối ngẫu](./doi-ngau-manh.md)
