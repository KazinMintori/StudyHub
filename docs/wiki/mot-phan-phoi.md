---
title: "Mốt của phân phối xác suất"
wikiTerm: mot-phan-phoi
prev: False
next: False
---

# Mốt của phân phối xác suất

Mốt của biến ngẫu nhiên rời rạc là giá trị có khối lượng xác suất lớn nhất. Một phân phối có thể có nhiều mốt. Mốt mô tả vị trí có xác suất tập trung lớn nhất, còn kỳ vọng là trung bình có trọng số của các giá trị.

<WikiUsage />

## Giải thích kỹ thuật

Với bảng phân phối gồm các giá trị $x_i$ và khối lượng $p_i$, tập các mốt gồm những $x_i$ có $p_i$ đạt giá trị lớn nhất. Với phân phối nhị thức có $0<p<1$, đặt $m=(n+1)p$. Nếu $m$ không nguyên, mốt là phần nguyên của $m$. Nếu $m$ nguyên, hai mốt là $m-1,m$.

Với Poisson có tham số nguyên dương, hai mốt cũng kề nhau. Các quy tắc phải giữ điều kiện tham số và miền giá trị. Xem [Phân phối xác suất rời rạc](/xac-suat-thong-ke/bai-giang/11-phan-phoi-xac-suat).

## Ví dụ

Nếu các giá trị 0, 1, 2 có xác suất 0,2, 0,5, 0,3 thì mốt duy nhất là 1. Phân phối đều trên một tập hữu hạn có mọi giá trị trong tập là mốt.

## Khi nào cần dùng?

Xác định kết quả riêng lẻ có khả năng cao nhất và phân biệt với giá trị trung bình.

## Câu hỏi ôn lại

Hai giá trị cùng đạt khối lượng lớn nhất có tạo hai mốt không?

<details><summary>Xem đáp án</summary>

Có. Cần giữ cả hai, thay vì chọn một giá trị tùy ý.

</details>

## Thuật ngữ liên quan

- [Biến ngẫu nhiên](./bien-ngau-nhien.md)
- [Kỳ vọng](./ky-vong.md)
- [Hàm phân phối tích lũy](./ham-phan-phoi-tich-luy.md)
