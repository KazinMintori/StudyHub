---
title: "Dictionary"
wikiTerm: dictionary
prev: false
next: false
---

# Dictionary

Dictionary ánh xạ khóa tới giá trị. Khóa cần hashable và là duy nhất; gán lại cùng một khóa thay giá trị cũ. Dùng d[key] khi chắc chắn khóa có mặt, hoặc d.get(key, mặc_định) khi khóa có thể thiếu.

## Giải thích kỹ thuật

**Hashable và tra cứu.** Dictionary dùng khóa hashable, nghĩa là phù hợp với yêu cầu băm và so sánh bằng nhau. List thông thường không hashable nên không thể dùng trực tiếp làm khóa.

Tra cứu thường có chi phí trung bình gần O(1) trong mô hình phù hợp, nhưng không phải mọi trường hợp đều bảo đảm như vậy. Khóa giống nhau ghi đè giá trị trước thay vì tạo khóa thứ hai.

## Ví dụ

d={"ten":"An", "diem":8}; d["diem"] cho 8, d.get("tuoi",0) cho 0.

## Khi nào cần dùng?

Hiểu dữ liệu có nhãn, cấu hình và nhóm theo khóa.

## Tự kiểm tra

Gán d["x"]=1 rồi d["x"]=2 tạo một hay hai khóa x?

<details><summary>Xem đáp án</summary>

Một khóa x, có giá trị cuối là 2.

</details>

## Thuật ngữ liên quan

- [Hàm băm](./bam.md)
- [Cặp khóa–giá trị](./khoa-gia-tri.md)
- [List](./list.md)
