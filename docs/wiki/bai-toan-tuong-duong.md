---
title: "Bài toán tương đương"
wikiTerm: bai-toan-tuong-duong
prev: false
next: false
---

# Bài toán tương đương

Hai bài toán tối ưu tương đương nếu từ một nghiệm của bài toán này dễ dàng tìm được một nghiệm của bài toán kia, và ngược lại. Các phép biến đổi thường gặp là đổi biến một-một, bọc hàm mục tiêu trong một hàm tăng ngặt, thêm biến bù, chuyển sang dạng epigraph và khử ràng buộc đẳng thức. Tương đương giữ nghiệm nhưng có thể làm thay đổi giá trị tối ưu, tính khả vi hay tính lồi.

<WikiUsage />

## Giải thích kỹ thuật

**Định nghĩa không hình thức.** Sách gọi hai bài toán là tương đương khi nghiệm của bài toán này cho ngay nghiệm của bài toán kia, và nói rõ một định nghĩa hình thức tuy có thể đưa ra nhưng không giúp hiểu thêm. Phép co giãn hàm mục tiêu và ràng buộc bởi hằng số dương là ví dụ đơn giản nhất.

**Giữ nghiệm khác giữ tính lồi.** Khử ràng buộc đẳng thức tuyến tính, thêm biến cùng ràng buộc đẳng thức tuyến tính, dạng epigraph và cực tiểu theo một nhóm biến đều giữ tính lồi. Biến bù chỉ giữ tính lồi với bất đẳng thức affine. Đổi biến không affine có thể tạo ra hoặc làm mất tính lồi, chẳng hạn đặt $\sigma = e^s$ làm âm log-likelihood Gauss trở nên lồi, còn đặt $x = z^2$ có thể sinh ra điểm dừng giả. Nguồn: Convex Optimization, §4.1.3 và §4.2.4.

## Ví dụ

Cực tiểu $\|Ax - b\|_2$ và cực tiểu $\|Ax - b\|_2^2$ có cùng nghiệm, nhưng hàm thứ hai khả vi ở mọi nơi.

## Khi nào cần dùng?

Đưa một bài toán về dạng mà bộ giải chấp nhận và làm tính lồi hiện ra.

## Câu hỏi ôn lại

Thêm biến bù cho ràng buộc $x^2 \le 1$ có giữ được dạng chuẩn lồi không?

<details><summary>Xem đáp án</summary>

Không. Ràng buộc mới $x^2 + s = 1$ là đẳng thức phi affine, nên bài toán vẫn tương đương nhưng không còn ở dạng chuẩn lồi.

</details>

## Thuật ngữ liên quan

- [Epigraph](./epigraph.md)
- [Điểm và miền khả thi](./mien-kha-thi.md)
- [Hàm lồi](./ham-loi.md)
