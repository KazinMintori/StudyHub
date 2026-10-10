---
title: "Đa diện và đơn hình"
wikiTerm: da-dien
prev: false
next: false
---

# Đa diện và đơn hình

Đa diện là tập nghiệm của hữu hạn bất đẳng thức và đẳng thức tuyến tính, $\{x : Ax \preceq b,\ Cx = d\}$, tức giao của hữu hạn nửa không gian và siêu phẳng. Đơn hình là bao lồi của các điểm độc lập affine, chẳng hạn đơn hình xác suất $\{x \succeq 0 : x_1 + \cdots + x_n = 1\}$.

<WikiUsage />

## Giải thích kỹ thuật

**Hai cách mô tả.** Một đa diện bị chặn có thể mô tả bằng các bất đẳng thức, tức giao của nửa không gian, hoặc bằng các đỉnh, tức bao lồi của hữu hạn điểm. Hai cách mô tả có thể chênh lệch rất lớn về kích thước: Khối lập phương trong $\mathbb R^n$ có $2n$ mặt nhưng $2^n$ đỉnh.

**Đơn hình xác suất.** Mỗi điểm của đơn hình xác suất là một phân phối trên $n$ kết quả, và các đỉnh là những phân phối chắc chắn. Đầu ra softmax của một bộ phân loại luôn nằm trong nội tương đối của đơn hình này. Nguồn: Convex Optimization, §2.2.4.

## Ví dụ

Tam giác $\{x \in \mathbb R^2 : x \succeq 0,\ x_1 + x_2 \le 1\}$ vừa là đa diện vừa là đơn hình, với ba đỉnh $(0, 0)$, $(1, 0)$ và $(0, 1)$.

## Khi nào cần dùng?

Miền khả thi của quy hoạch tuyến tính và tập các phân phối xác suất rời rạc.

## Câu hỏi ôn lại

Hình tròn có phải đa diện không?

<details><summary>Xem đáp án</summary>

Không. Hình tròn là giao của vô số nửa không gian và không viết được bằng hữu hạn bất đẳng thức tuyến tính.

</details>

## Thuật ngữ liên quan

- [Siêu phẳng và nửa không gian](./sieu-phang.md)
- [Tập lồi](./tap-loi.md)
- [Nghiệm cơ sở của quy hoạch tuyến tính](./nghiem-co-so.md)
