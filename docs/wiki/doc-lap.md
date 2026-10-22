---
title: "Độc lập"
wikiTerm: doc-lap
prev: false
next: false
---

# Độc lập

Biết lần tung đồng xu đầu tiên có kết quả ngửa không làm thay đổi mô hình xác suất của lần tung thứ hai, nếu hai lần tung được giả thiết độc lập. **Độc lập** là một quan hệ trong mô hình, không phải kết luận từ việc hai sự kiện trông khác nhau.

<WikiUsage />

## Giải thích kỹ thuật

Hai biến cố $A,B$ độc lập khi:

$$
P(A\cap B)=P(A)P(B).
$$

Khi $P(B)>0$, điều này tương đương $P(A\mid B)=P(A)$. Định nghĩa bằng tích xác suất vẫn dùng được khi xác suất một biến cố bằng 0.

Hai biến cố loại trừ nhau và có xác suất dương không độc lập. Nếu không thể cùng xảy ra, xác suất giao bằng 0, còn tích hai xác suất là số dương.

Với nhiều biến cố, độc lập từng đôi chưa đủ để suy ra độc lập đồng thời. Cần kiểm tra giao của mọi nhóm thích hợp. Tương tự, hai biến ngẫu nhiên có hiệp phương sai bằng 0 chưa chắc độc lập.

## Ví dụ có lời giải

Tung hai đồng xu cân bằng, độc lập. Gọi $A$ là “lần đầu ngửa”, $B$ là “lần sau ngửa”, $C$ là “hai lần giống nhau”.

Mỗi biến cố có xác suất $1/2$. Giao của từng cặp có xác suất $1/4$, đúng bằng tích hai xác suất. Tuy nhiên:

$$
P(A\cap B\cap C)=1/4\ne1/8.
$$

Ba biến cố không độc lập đồng thời. Ví dụ này cho thấy vì sao kiểm tra từng cặp chưa đủ.

Với một lần tung xúc xắc, biến cố “ra 1” và “ra 2” loại trừ nhau. Biết biến cố thứ nhất xảy ra làm xác suất biến cố thứ hai thành 0, nên chúng không độc lập.

## Câu hỏi ôn lại

Giả sử $P(A)=1/3$, $P(B)=1/2$ và $P(A\cap B)=1/6$. Hai biến cố có độc lập không?

::: details Xem lời giải
Có, vì $P(A)P(B)=1/6$ bằng xác suất giao. Vì $P(B)>0$, cũng có thể kiểm tra $P(A\mid B)=(1/6)/(1/2)=1/3$.
:::

## Đọc tiếp

- [Xác suất có điều kiện](./xac-suat-co-dieu-kien.md)
- [Biến ngẫu nhiên](./bien-ngau-nhien.md)
- [Hiệp phương sai](./hiep-phuong-sai.md)

## Tài liệu tham khảo

- [OpenStax, Introductory Statistics 2e, Independent and Mutually Exclusive Events](https://openstax.org/books/introductory-statistics-2e/pages/3-2-independent-and-mutually-exclusive-events).
