---
title: "Tính toán phân tán"
wikiTerm: phan-tan
prev: false
next: false
---

# Tính toán phân tán

Tính toán phân tán chia công việc và dữ liệu cho nhiều máy liên lạc qua mạng. Tổng thời gian gồm tính toán, truyền dữ liệu và đồng bộ. Một máy chậm hoặc phân vùng dữ liệu không đều có thể quyết định thời gian của cả pha; thêm máy không bảo đảm nhanh hơn tương ứng.

<WikiUsage />

## Giải thích kỹ thuật

**Thời gian và lỗi.** Thời gian của một pha đồng bộ thường bị quyết định bởi tác vụ hoàn thành chậm nhất, không phải trung bình. Chi phí truyền gồm độ trễ khởi tạo và lượng dữ liệu chia băng thông.

Thiết kế cần tính khả năng máy lỗi, xử lý lặp và tái lập kết quả. Thêm máy có thể giảm tính toán cục bộ nhưng tăng truyền, nên không bảo đảm tăng tốc tuyến tính.

## Ví dụ

Chia 1000 dòng cho 4 máy rồi cộng kết quả: cần cả chi phí chia dữ liệu, tính tổng từng máy và gom kết quả.

## Khi nào cần dùng?

Hiểu MapReduce, mô hình chi phí và lỗi máy.

## Tự kiểm tra

Thêm gấp đôi số máy có luôn giảm một nửa thời gian không?

<details><summary>Xem đáp án</summary>

Không. Truyền dữ liệu, đồng bộ và mất cân bằng có thể chiếm phần lớn thời gian.

</details>

## Thuật ngữ liên quan

- [Cặp khóa–giá trị](./khoa-gia-tri.md)
- [Tính kết hợp &amp; giao hoán](./ket-hop.md)
- [Độ phức tạp](./do-phuc-tap.md)
- [Hàm băm](./bam.md)
