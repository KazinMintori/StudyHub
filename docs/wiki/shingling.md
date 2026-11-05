---
title: "Shingling"
wikiTerm: shingling
prev: False
next: False
---

# Shingling

Cách biểu diễn văn bản bằng tập các đoạn liên tiếp có cùng độ dài, tính theo ký tự hoặc từ đã quy định. Chuẩn hóa văn bản và chọn đơn vị phải được thực hiện nhất quán trước khi lập tập. Dạng tập không giữ số lần lặp của một đoạn.

<WikiUsage />

## Giải thích kỹ thuật

Trước khi lập shingle, phải xác định chuẩn Unicode, cách xử lý chữ hoa, dấu câu, khoảng trắng và việc tách từ. Mỗi lựa chọn thay đổi bài toán tương đồng. Không có một độ dài shingle phù hợp với mọi loại tài liệu.

Biểu diễn tập chỉ ghi nhận một đoạn có xuất hiện hay không. Nếu cần dùng tần suất thì phải thay cả mô hình biểu diễn lẫn độ đo tương ứng. Khi văn bản ngắn hơn độ dài shingle, tập nhận được rỗng. Trường hợp này cần được xử lý trước khi tạo chữ ký MinHash.

## Ví dụ

Với shingle 2 ký tự, văn bản ababa cho tập {ab, ba}. Đoạn ab xuất hiện hai lần nhưng chỉ có một phần tử trong tập.

## Khi nào cần dùng?

Biểu diễn các mẫu cục bộ để so sánh tài liệu gần trùng.

## Câu hỏi ôn lại

Hai văn bản có cùng tập shingle có nhất thiết là cùng chuỗi không?

<details><summary>Xem đáp án</summary>

Không. Phép lập tập có thể làm mất tần suất và thông tin về thứ tự tổng thể.

</details>

## Thuật ngữ liên quan

- [Độ tương đồng Jaccard](./jaccard.md)
- [MinHash](./minhash.md)
