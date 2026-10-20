---
title: "Xác suất có điều kiện"
wikiTerm: xac-suat-co-dieu-kien
prev: False
next: False
---

# Xác suất có điều kiện

P(A|B) là xác suất A khi biết B đã xảy ra. Với $P(B)>0$, $P(A|B)=\frac{P(A\cap B)}{P(B)}$: Thu hẹp miền xét về B rồi tính phần của A trong miền đó. P(A|B) nhìn chung khác P(B|A).

<WikiUsage />

## Giải thích kỹ thuật

Với $P(B)>0$, xác suất có điều kiện được xác định bởi

$$
P(A\mid B)=\frac{P(A\cap B)}{P(B)}.
$$

Công thức Bayes đổi chiều điều kiện nhưng vẫn phải giữ xác suất ban đầu của A.

$$
P(A\mid B)=\frac{P(B\mid A)P(A)}{P(B)}.
$$

Đặt $q=P(B\mid A)$, $r=P(B\mid A^c)$ và $p=P(A)$ khi cả hai điều kiện có xác suất dương. Khi ấy, công thức xác suất toàn phần viết gọn thành

$$
P(B)=qp+r(1-p).
$$

Mẫu số bao gồm cả hai cách để B xảy ra. Đảo chiều điều kiện mà giữ nguyên giá trị xác suất sẽ cho kết quả sai nói chung.

## Ví dụ

Trong 100 người có 20 người đeo kính, trong đó 8 người học lớp X. P(lớp X | đeo kính)=$\frac{8}{20}=0.4$.

## Khi nào cần dùng?

Đọc định lý Bayes, mạng Bayes và suy luận từ quan sát.

## Câu hỏi ôn lại

Nếu $P(A\cap B)=0.1$, $P(B)=0.5$ thì P(A|B) bằng bao nhiêu?

<details><summary>Xem đáp án</summary>

0.2.

</details>

## Thuật ngữ liên quan

- [Không gian mẫu](./khong-gian-mau.md)
- [Độc lập](./doc-lap.md)
- [Biến ngẫu nhiên](./bien-ngau-nhien.md)
