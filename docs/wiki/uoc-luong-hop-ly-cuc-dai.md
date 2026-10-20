---
title: "Ước lượng hợp lý cực đại"
wikiTerm: uoc-luong-hop-ly-cuc-dai
prev: False
next: False
---

# Ước lượng hợp lý cực đại

Ước lượng hợp lý cực đại chọn giá trị tham số làm hàm hợp lý của dữ liệu quan sát đạt lớn nhất trong miền tham số. Phải kiểm tra biên miền, điểm cực trị và sự tồn tại của cực đại.

<WikiUsage />

## Giải thích kỹ thuật

Hàm hợp lý xem dữ liệu đã quan sát là cố định và tham số là biến số cần tối ưu. Giá trị hàm hợp lý không phải xác suất của tham số. Với mẫu độc lập, hàm hợp lý là tích các khối lượng xác suất hoặc mật độ tại từng quan sát.

Logarit thường chuyển tích thành tổng và giữ nguyên vị trí cực đại khi hàm hợp lý dương. Nếu miền hỗ trợ phụ thuộc tham số, phải giữ điều kiện hỗ trợ khi tối ưu. MLE không mặc nhiên không chệch hoặc có phân phối chuẩn ở mọi cỡ mẫu.

Xem [Ước lượng điểm, mômen và hợp lý cực đại](/xac-suat-thong-ke/bai-giang/37-uoc-luong-diem-momen-va-hop-ly-cuc-dai).

## Ví dụ

Với 3 lần thành công trong 4 phép thử Bernoulli độc lập, ước lượng hợp lý cực đại của xác suất thành công bằng 3/4.

## Khi nào cần dùng?

Ước lượng tham số từ một mô hình xác suất được phát biểu rõ.

## Câu hỏi ôn lại

Nghiệm đạo hàm log hợp lý bằng 0 có luôn là MLE không?

<details><summary>Xem đáp án</summary>

Không. Có thể đó là cực tiểu, điểm yên ngựa, hoặc cực đại thực sự nằm ở biên miền tham số.

</details>

## Thuật ngữ liên quan

- [Likelihood](./likelihood.md)
- [Thông tin Fisher](./thong-tin-fisher.md)
- [Ước lượng không chệch](./uoc-luong-khong-chech.md)
