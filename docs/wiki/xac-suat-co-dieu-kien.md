---
title: "Xác suất có điều kiện"
wikiTerm: xac-suat-co-dieu-kien
prev: false
next: false
---

# Xác suất có điều kiện

P(A|B) là xác suất A khi biết B đã xảy ra. Với P(B)>0, P(A|B)=P(A∩B)/P(B): thu hẹp miền xét về B rồi tính phần của A trong miền đó. P(A|B) nhìn chung khác P(B|A).

## Giải thích kỹ thuật

**Định nghĩa và Bayes.** Với P(B)>0:

$$P(A\mid B)=\frac{P(A\cap B)}{P(B)},qquad P(A\mid B)=\frac{P(B\mid A)P(A)}{P(B)}.$$

Mẫu số P(B) bao gồm mọi cách B xảy ra, không chỉ trường hợp A đúng. Nếu A và phần bù của A chia hết miền xét, P(B)=P(B|A)P(A)+P(B|không A)P(không A). Đảo nhầm hai chiều điều kiện hoặc bỏ tỷ lệ ban đầu là hai lỗi phổ biến.

## Ví dụ

Trong 100 người có 20 người đeo kính; 8 trong số đó học lớp X. P(lớp X | đeo kính)=8/20=0.4.

## Khi nào cần dùng?

Đọc định lý Bayes, mạng Bayes và suy luận từ quan sát.

## Tự kiểm tra

Nếu P(A∩B)=0.1, P(B)=0.5 thì P(A|B) bằng bao nhiêu?

<details><summary>Xem đáp án</summary>

0.2.

</details>

## Thuật ngữ liên quan

- [Không gian mẫu](./khong-gian-mau.md)
- [Độc lập](./doc-lap.md)
- [Biến ngẫu nhiên](./bien-ngau-nhien.md)
