---
title: "Bài tập Cơ sở toán cho AI"
description: "Bài tập nhận diện, tính toán và giải thích của tám lecture, kèm lời giải theo bước."
---

# Bài tập Cơ sở toán cho AI

Mỗi Notes có ba bài tự luyện với lời giải gập ngay sau đề. Bắt đầu bằng bài tính trực tiếp, rồi bài giải thích hoặc đổi điều kiện. Chỉ mở lời giải sau khi đã thử; nếu sai, tìm phép suy ra đầu tiên không hợp lệ trước khi so đáp số cuối.

| Lecture | Thao tác luyện | Mở bộ bài |
| --- | --- | --- |
| 00 | Dự đoán, phần dư, gradient, thiếu hạng | [Bài tập nền tảng](./bai-giang/bai-00-on-tap-nen-tang.md#bai-tap-tu-luyen) |
| 01 | Chứng minh tập lồi, phân biệt miền và hàm, nghiệm tại biên | [Bài tập tính lồi](./bai-giang/bai-01-nhap-mon-toi-uu.md#bai-tap-tu-luyen) |
| 02 | Nhận dạng, biến phụ, cận từ nới lỏng | [Bài tập mô hình](./bai-giang/bai-02-tap-loi.md#bai-tap-tu-luyen) |
| 03 | Hàm đối ngẫu, bù trừ, nhân tử | [Bài tập đối ngẫu](./bai-giang/bai-03-doi-ngau-lagrange.md#bai-tap-tu-luyen) |
| 04 | Khoảng bước, hướng Newton, phần dư KKT | [Bài tập thuật toán](./bai-giang/bai-04-gradient-newton.md#bai-tap-tu-luyen) |
| 05 | Lô nhỏ, momentum, phương sai Glorot | [Bài tập huấn luyện](./bai-giang/bai-05-toi-uu-huan-luyen.md#bai-tap-tu-luyen) |
| 06 | Moment, hiệu chỉnh và hệ có số hạng chéo | [Bài tập optimizer](./bai-giang/bai-06-phuong-phap-thich-nghi.md#bai-tap-tu-luyen) |
| 07 | Cơ sở LP, cập nhật Bellman, trạng thái đủ thông tin | [Bài tập LP và DP](./bai-giang/bai-07-quy-hoach-tuyen-tinh-va-dong.md#bai-tap-tu-luyen) |

## Một bài nối các lecture

::: exercise Hồi quy có giới hạn
Với dữ liệu $A=(1,2,3)^T$, $b=(1,2,2)^T$, giải $\min_w\tfrac12\|Aw-b\|_2^2$ với $w\le1/2$. Hãy lập mô hình, chứng minh lồi, tính nghiệm và nhân tử, rồi giải thích vì sao dừng theo gradient bằng 0 sẽ sai.
:::
::: solution
Biến là $w$; dữ liệu là $A,b$; ràng buộc $w-1/2\le0$. Mục tiêu $7w^2-11w+9/2$ có Hessian 14 dương, miền là nửa không gian. Nghiệm không ràng buộc $11/14$ không khả thi. Trên miền hợp lệ, đạo hàm âm nên nghiệm tại $1/2$, giá trị $3/4$.

KKT: khả thi gốc, $\lambda=4\ge0$, bù trừ $4(1/2-1/2)=0$, dừng $14(1/2)-11+4=0$. Đây là chứng nhận toàn cục của bài lồi. Gradient mục tiêu tại nghiệm là $-4$, nên tiêu chí gradient bằng 0 của bài không ràng buộc không phù hợp.
:::

Các bài tập đều tự biên soạn dựa trên nguồn được ghi trong từng Notes; không sao chép bộ bài tập của trang chỉ mục môn.
