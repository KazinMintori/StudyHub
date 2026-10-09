---
title: "Khoảng tứ phân vị"
wikiTerm: khoang-tu-phan-vi
prev: false
next: false
---

# Khoảng tứ phân vị

Khoảng tứ phân vị là chênh lệch giữa phân vị 75% và phân vị 25%. Cách nội suy phân vị cần được chỉ rõ khi các quy tắc cho kết quả khác nhau.

<WikiUsage />

## Giải thích kỹ thuật

Gọi hai tứ phân vị là Q1 và Q3; IQR bằng Q3 trừ Q1. Hàng rào tham khảo nằm ở Q1 trừ 1.5 IQR và Q3 cộng 1.5 IQR. Râu boxplot theo quy tắc này kết thúc tại quan sát xa nhất vẫn trong hàng rào, không nhất thiết tại chính giá trị hàng rào.

Tra cứu kỹ thuật: [Matplotlib boxplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.boxplot.html).

## Ví dụ

Dãy 10, 12, 14, 16, 100 theo nội suy tuyến tính có Q1 bằng 12, Q3 bằng 16 và IQR bằng 4.

## Khi nào cần dùng?

Mô tả độ phân tán và dựng hàng rào để kiểm ngoại lai.

## Câu hỏi ôn lại

Với Q1 bằng 12 và Q3 bằng 16, hàng rào trên theo 1.5 IQR bằng bao nhiêu?

<details><summary>Xem đáp án</summary>

22; đây là ngưỡng gắn cờ, không phải kết luận dữ liệu sai.

</details>

## Thuật ngữ liên quan

- [Histogram](./histogram.md)
- [Ngoại lai](./ngoai-lai.md)
- [Biến &amp; kiểu dữ liệu](./bien-kieu.md)
