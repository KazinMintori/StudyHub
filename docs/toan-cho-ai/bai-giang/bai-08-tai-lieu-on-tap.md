---
course: toan-cho-ai
lecture: bai-08-tai-lieu-on-tap
section: lecture
title: "Ôn luyện: Từ nền tảng đến thuật toán"
prerequisites: ["ham-so", "dao-ham", "tap-hop"]
lessonStatus: ready
description: "Toàn bộ nội dung bốn buổi ôn tập, từ mô hình tối ưu và hồi quy đến KKT, đối ngẫu, tính lồi, Taylor, gradient và backtracking."
---

Muốn giải một bài tối ưu, ta phải làm được ba việc liên tiếp: Viết đúng bài toán, tìm một ứng viên và chứng minh ứng viên ấy tốt đến mức nào. Bốn buổi ôn tập đi hết mạch này. Hồi quy đưa dữ liệu về một mục tiêu cụ thể, tính lồi và KKT giúp chứng nhận nghiệm, còn Taylor dẫn đến thuật toán tìm nghiệm bằng các bước lặp.

Nội dung được sắp thành bốn phần ôn luyện theo quan hệ kiến thức cần học trước. Mỗi chủ đề giữ các định nghĩa, công thức, ví dụ và bài tập, đồng thời mở những bước biến đổi cần thiết để có thể tự học.

## 1. Các chủ đề ôn luyện

<TopicMap />

## 2. Mạch học và liên hệ

Ôn luyện 1 bắt đầu từ vector, chuẩn và ma trận. Sau khi biết dạng toàn phương và tính xác định dương, ta mới học gradient, Hessian và điều kiện cực trị. Vì vậy ký hiệu PSD trong điều kiện bậc hai đã có ý nghĩa cụ thể.

Ôn luyện 2 dùng nền tảng ấy để học tập lồi và hàm lồi, rồi chứng minh kết luận tối ưu toàn cục. Sau đó mới áp dụng vào hồi quy, hai bài LP và bài toán có cos. Phương trình chuẩn và chứng nhận Hessian lúc này đều dựa trên kiến thức đã học.

Ôn luyện 3 giải quyết ràng buộc bằng Lagrangian, KKT và đối ngẫu. Tính đủ của KKT dùng trực tiếp tính lồi ở phần trước. Ví dụ theo tham số và hai bài tập cuối giúp phân biệt chứng nhận lồi với điều kiện cần trong bài phi lồi.

Ôn luyện 4 đưa các đạo hàm vào thuật toán. Quy tắc chuỗi tính sự thay đổi dọc một đường đi, Taylor giải thích hướng giảm, còn backtracking quyết định bước đi cụ thể. Ví dụ cuối theo dõi đủ hai vòng lặp đến nghiệm.

## 3. Bài tập tự luyện

::: exercise Chọn công cụ phù hợp
Với mỗi tình huống sau, nêu phép kiểm cần làm trước khi kết luận tối ưu.

1. Một hệ số hồi quy thỏa phương trình chuẩn.
2. Một điểm thỏa KKT của bài toán có mục tiêu bậc ba.
3. Một hướng có tích vô hướng âm với gradient nhưng bước đầy đủ làm mục tiêu tăng.
:::

::: solution
1. Bình phương tối thiểu là bài toán lồi, nên phương trình chuẩn đủ để tối ưu. Muốn khẳng định hệ số duy nhất phải kiểm hạng cột của ma trận thiết kế.
2. KKT chỉ cho ứng viên khi chưa có tính lồi. Cần kiểm giá trị mục tiêu, điều kiện bậc hai hoặc tìm cận dưới toàn cục.
3. Hướng giảm bảo đảm giảm với bước dương đủ nhỏ. Cần thu bước, chẳng hạn bằng backtracking Armijo, rồi kiểm bất đẳng thức giảm đủ.
:::

## 4. Kết quả cần tự tái hiện

- Lập ma trận thiết kế có hệ số chặn và suy ra phương trình chuẩn từ điều kiện vuông góc của phần dư.
- Giải hai bài LP bằng đường mức, ghi đủ đỉnh và giá trị mục tiêu.
- Viết đủ hệ KKT, xét dấu nhân tử và giải bài có tham số ở cả hai miền.
- Tính hai hàm đối ngẫu mẫu và giải thích tại sao giá trị gốc bằng giá trị đối ngẫu.
- Chứng minh cực tiểu địa phương của bài toán lồi là toàn cục.
- Tính gradient, Hessian và nghiệm của bài có cos.
- Suy ra Taylor nhiều biến từ hàm một biến dọc đường và tái hiện bảng backtracking.

Phần lời giải chi tiết, điều kiện áp dụng và hiệu chỉnh công thức được ghi ngay ở chủ đề tương ứng. Mọi phép tính số học và giải tích đều được kiểm tra và tái lập chuẩn xác.
