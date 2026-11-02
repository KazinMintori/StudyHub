---
title: "Dạng chuẩn CNF"
wikiTerm: dang-chuan-cnf
prev: false
next: false
---

# Dạng chuẩn CNF

Dạng chuẩn hội là một phép hội giữa các clause, trong đó mỗi clause là một phép tuyển của các literal. Literal là ký hiệu nguyên tử hoặc phủ định của nó.

<WikiUsage />

## Giải thích kỹ thuật

Công thức logic mệnh đề có thể chuyển về CNF tương đương bằng cách khử kéo theo và tương đương, đưa phủ định sát ký hiệu nguyên tử, rồi phân phối tuyển qua hội.

Clause chứa cả một literal và phủ định của nó luôn đúng, nên có thể bỏ khỏi phép hội. Clause rỗng biểu diễn Sai. Tập clause rỗng không chứa ràng buộc nào nên biểu diễn Đúng.

Phân phối trực tiếp có thể làm kích thước công thức tăng theo hàm mũ. Dùng biến phụ có thể giữ kích thước nhỏ hơn, nhưng phải phân biệt bảo toàn tính thỏa được với tương đương dưới mọi phép gán cho các biến phụ.

## Ví dụ

$$
(P\lor\neg Q)\land(R\lor P)
$$

Đây là hội của hai clause tuyển.

## Đọc tiếp

[Tương đương logic và dạng chuẩn CNF](/bieu-dien-tri-thuc/bai-giang/07-logic-menh-de/tuong-duong-va-cnf.md).
