---
title: "Quy hoạch tuyến tính (LP)"
wikiTerm: quy-hoach-tuyen-tinh
prev: false
next: false
---

# Quy hoạch tuyến tính (LP)

Bài toán cực tiểu hoặc cực đại một hàm affine với các ràng buộc bất đẳng thức và đẳng thức affine, chẳng hạn $\min c^Tx$ với $Gx \preceq h$, $Ax = b$. Miền khả thi là một đa diện. Khi đa diện có đỉnh và giá trị tối ưu hữu hạn, có một nghiệm là đỉnh. Mọi LP đều đưa được về dạng chuẩn $\min c^Tx$ với $Ax = b$, $x \succeq 0$.

<WikiUsage />

## Giải thích kỹ thuật

**Hình học.** Tập mức của $c^Tx$ là những siêu phẳng vuông góc với $c$, và nghiệm là điểm của đa diện xa nhất theo hướng $-c$. Có bốn khả năng: Nghiệm duy nhất tại đỉnh, cả một mặt là tập nghiệm, không bị chặn dưới khi đa diện kéo dài theo một hướng $r$ có $c^Tr < 0$, hoặc bất khả thi.

**Chuyển về dạng chuẩn.** Thêm biến bù $s \succeq 0$ cho mỗi bất đẳng thức và viết mỗi biến tự do thành $x^+ - x^-$ với $x^+, x^- \succeq 0$. Nhiều bài toán không trông tuyến tính cũng là LP: Tâm Chebyshev, cực tiểu hàm tuyến tính từng khúc, cận chặt cho kỳ vọng khi chỉ biết vài thông tin tuyến tính về phân phối, và quy hoạch phân tuyến tính sau một phép đổi biến. Nguồn: Convex Optimization, §4.3.

## Ví dụ

Tìm hình tròn lớn nhất nằm trong một đa giác, tức tâm Chebyshev, là một LP với ba biến: Hai tọa độ của tâm và bán kính.

## Khi nào cần dùng?

Lập kế hoạch, phân bổ, khớp dữ liệu theo chuẩn $\ell_1$ hoặc $\ell_\infty$, và làm bài toán con trong nhiều thuật toán.

## Câu hỏi ôn lại

Một LP có thể có đúng hai nghiệm tối ưu không?

<details><summary>Xem đáp án</summary>

Không. Tập nghiệm của một bài toán lồi là tập lồi, nên một LP có không, một, hoặc vô số nghiệm.

</details>

## Thuật ngữ liên quan

- [Đa diện và đơn hình](./da-dien.md)
- [Nghiệm cơ sở của quy hoạch tuyến tính](./nghiem-co-so.md)
- [Quy hoạch toàn phương (QP và QCQP)](./quy-hoach-toan-phuong.md)
