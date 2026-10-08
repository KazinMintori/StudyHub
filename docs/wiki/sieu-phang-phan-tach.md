---
title: "Siêu phẳng phân tách và siêu phẳng tựa"
wikiTerm: sieu-phang-phan-tach
prev: false
next: false
---

# Siêu phẳng phân tách và siêu phẳng tựa

Hai tập lồi rời nhau luôn có một siêu phẳng phân tách: tồn tại $a \ne 0$ và b với $a^T x \le b$ trên tập này và $a^T x \ge b$ trên tập kia. Siêu phẳng tựa của tập C tại điểm biên $x_0$ là siêu phẳng đi qua $x_0$ sao cho C nằm trọn một phía.

<WikiUsage />

## Giải thích kỹ thuật

**Định lý.** Nếu $C$ và $D$ lồi, rời nhau thì tồn tại $a \ne 0$ và $b$ với $a^T x \le b$ trên $C$ và $a^T x \ge b$ trên $D$. Phân tách chặt cần thêm giả thiết, chẳng hạn $C$ đóng và $D$ compact.

**Siêu phẳng tựa và tiếp tuyến.** Mọi điểm biên của một tập lồi có ít nhất một siêu phẳng tựa. Với hàm lồi khả vi, tiếp tuyến tại $x$ là siêu phẳng tựa của epigraph tại $(x, f(x))$. Tại nghiệm của bài toán lồi, siêu phẳng vuông góc với gradient tựa vào miền khả thi.

**Học máy.** Hai lớp dữ liệu phân biệt được bằng một siêu phẳng khi và chỉ khi bao lồi của chúng rời nhau, và lề lớn nhất bằng nửa khoảng cách giữa hai bao lồi. Nguồn: Convex Optimization, §2.5 và §8.6.1.

## Ví dụ

Hai hình tròn bán kính 1 có tâm $(-2, 0)$ và $(2, 0)$ được đường thẳng $x_1 = 0$ phân tách. Đường thẳng $x_2 = 0$ thì không phân tách được chúng.

## Khi nào cần dùng?

Chứng minh các định lý lựa chọn và đối ngẫu, và hiểu bộ phân loại tuyến tính.

## Câu hỏi ôn lại

Hai tập không lồi rời nhau có luôn phân tách được bằng một siêu phẳng không?

<details><summary>Xem đáp án</summary>

Không. Một hình tròn và một vành khăn bao quanh nó rời nhau nhưng không siêu phẳng nào tách được.

</details>

## Thuật ngữ liên quan

- [Siêu phẳng và nửa không gian](./sieu-phang.md)
- [Tập lồi](./tap-loi.md)
- [Epigraph](./epigraph.md)
