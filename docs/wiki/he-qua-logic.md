---
title: "Hệ quả logic"
wikiTerm: he-qua-logic
prev: false
next: false
---

# Hệ quả logic

Một câu truy vấn là hệ quả logic của cơ sở tri thức khi mọi mô hình làm cơ sở tri thức đúng cũng làm truy vấn đúng.

<WikiUsage />

## Giải thích kỹ thuật

Ký hiệu $M(KB)$ là tập mô hình của cơ sở tri thức và $M(q)$ là tập mô hình của truy vấn. Điều kiện hệ quả là

$$
M(KB)\subseteq M(q).
$$

Nếu có một phép gán làm KB đúng nhưng q sai, phép gán đó là phản mô hình. Không có phản mô hình tương đương với việc KB cùng phủ định q không thỏa được.

Nếu KB đã mâu thuẫn, nó không có mô hình và mọi câu đều là hệ quả theo logic cổ điển. Vì vậy cần báo riêng tính nhất quán. Không suy ra được một câu không đồng nghĩa suy ra được phủ định của nó.

## Ví dụ

Từ sự thực P và luật P kéo theo Q, mọi mô hình của tri thức đều làm Q đúng. Vì vậy Q là hệ quả logic.

## Đọc tiếp

[Hệ quả logic và kiểm chứng mô hình](/bieu-dien-tri-thuc/bai-giang/07-logic-menh-de/he-qua-va-mo-hinh.md).
