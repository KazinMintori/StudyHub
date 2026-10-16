---
title: "Qubit"
wikiTerm: "qubit"
prev: false
next: false
---

# Qubit

Hệ lượng tử có hai trạng thái cơ sở trực chuẩn. Trạng thái thuần là tổ hợp tuyến tính chuẩn hóa của hai trạng thái cơ sở đó.

<WikiUsage />

## Giải thích kỹ thuật

Chọn hai trạng thái cơ sở trực chuẩn, ký hiệu 0 và 1. Một trạng thái thuần của qubit có dạng:

$$
\begin{aligned}|\psi\rangle&=a|0\rangle+b|1\rangle,\\|a|^2+|b|^2&=1.\end{aligned}
$$

Nếu đo trong cơ sở đó, xác suất hai kết quả lần lượt là bình phương môđun của a và b. Pha chung không quan sát được trong các xác suất, còn pha tương đối có thể ảnh hưởng kết quả khi đổi cơ sở.

Một phép đo không trả lại đồng thời cả hai biên độ phức. Muốn xác định trạng thái cần nhiều hệ được chuẩn bị giống nhau và những phép đo thích hợp.

Nhiều qubit có thể ở trạng thái rối. Khả năng xử lý thông tin phụ thuộc cách điều khiển biên độ và giao thoa, không phải quyền đọc ngay mọi cấu hình cơ sở bằng một lần đo.

## Ví dụ

Phép đo trong cơ sở 0 và 1 cho một trong hai kết quả, với xác suất là bình phương môđun của biên độ tương ứng.

## Khi nào cần dùng?

Mô tả cổng lượng tử, chồng chập và rối trong tính toán lượng tử.

## Câu hỏi ôn lại

Một qubit chồng chập có cho phép đọc đồng thời vô hạn bit cổ điển không?

<details><summary>Xem đáp án</summary>

Không. Mỗi phép đo trong cơ sở đã chọn cho một kết quả. Muốn suy ra tham số trạng thái cần nhiều lần chuẩn bị và đo.

</details>

## Thuật ngữ liên quan

- [Rối lượng tử](./roi-luong-tu.md)
- [Số phức trong hàm sóng](./so-phuc-trong-ham-song.md)
- [Phép đo lượng tử](./phep-do-luong-tu.md)

## Tài liệu tham khảo

Young & Freedman, *University Physics with Modern Physics*, ấn bản 15, chương 41, trang 1360–1398.
