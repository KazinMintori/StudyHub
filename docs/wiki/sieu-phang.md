---
title: "Siêu phẳng và nửa không gian"
wikiTerm: sieu-phang
prev: false
next: false
---

# Siêu phẳng và nửa không gian

Siêu phẳng là tập $\{x : a^T x = b\}$ với $a \ne 0$, còn nửa không gian là $\{x : a^T x \le b\}$. Vector a là pháp tuyến: nó vuông góc với siêu phẳng và chỉ về phía $a^T x$ tăng.

<WikiUsage />

## Giải thích kỹ thuật

**Hình học của a và b.** Siêu phẳng gồm các điểm có cùng tích vô hướng với $a$, nên là một tập mức của hàm tuyến tính $a^T x$. Khoảng cách từ gốc tới siêu phẳng là $|b| / \|a\|_2$. Đổi $b$ thì siêu phẳng tịnh tiến song song, đổi $a$ thì nó xoay.

**Vai trò trong tối ưu.** Mỗi ràng buộc tuyến tính là một nửa không gian, và đa diện là giao của hữu hạn nửa không gian. Định lý siêu phẳng phân tách nói rằng hai tập lồi rời nhau luôn được một siêu phẳng tách ra, nền tảng của các chứng nhận tối ưu và của đối ngẫu. Nguồn: Convex Optimization, §2.2.1 và §2.5.

## Ví dụ

Với $a = (1, 2)$ và $b = 4$, điểm $(0, 2)$ nằm trên siêu phẳng, còn $(1, 1)$ cho $a^T x = 3 \le 4$ nên thuộc nửa không gian.

## Khi nào cần dùng?

Viết ràng buộc tuyến tính, đọc ranh giới quyết định của bộ phân loại tuyến tính và chứng nhận nghiệm tối ưu.

## Câu hỏi ôn lại

Nửa không gian có phải tập affine không?

<details><summary>Xem đáp án</summary>

Không. Nó lồi, nhưng đường thẳng qua hai điểm có giá trị $a^T x$ khác nhau sẽ đi ra khỏi nửa không gian.

</details>

## Thuật ngữ liên quan

- [Tích vô hướng](./tich-vo-huong.md)
- [Siêu phẳng phân tách và siêu phẳng tựa](./sieu-phang-phan-tach.md)
- [Đa diện và đơn hình](./da-dien.md)
