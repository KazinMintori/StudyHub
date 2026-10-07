---
title: "Lộ trình Cơ sở toán cho AI"
description: "Tám lecture, điểm dừng tự kiểm và nguồn sách của từng phần."
---

# Lộ trình Cơ sở toán cho AI

Mỗi lecture có Notes để học mới, Slides để nhớ lại và Kiến thức nền để ôn công cụ cần dùng. Đọc Notes theo từng cụm, trả lời câu tự kiểm trước khi mở đáp án. Nếu mắc ở một phép tính, quay sang nền của phép tính ấy rồi trở lại đúng ví dụ; không cần đọc hết Wiki trước khi bắt đầu.

| Lecture | Bắt đầu từ câu hỏi | Điều nên tự làm được trước khi đi tiếp |
| --- | --- | --- |
| [00. Nền tảng](../bai-giang/bai-00-on-tap-nen-tang.md) | Đổi tham số thì dự đoán và loss đổi thế nào? | Tính $Aw$, phần dư, gradient; giải thích giả định Gauss. |
| [01. Tối ưu, tập lồi, hàm lồi](../bai-giang/bai-01-nhap-mon-toi-uu.md) | Vì sao một ứng viên có thể được chứng nhận toàn cục? | Dùng đoạn nối, dây cung và điều kiện bậc nhất có đúng giả thiết. |
| [02. Bài toán lồi](../bai-giang/bai-02-tap-loi.md) | Biểu diễn nào làm cấu trúc lồi hiện rõ? | Kiểm dấu, đẳng thức, PSD; chứng minh hai chiều cải dạng. |
| [03. Đối ngẫu](../bai-giang/bai-03-doi-ngau-lagrange.md) | Cận dưới tốt nhất đang cách ứng viên bao xa? | Tính $g$, kiểm Slater và đủ các nhóm KKT. |
| [04. Gradient và Newton](../bai-giang/bai-04-gradient-newton.md) | Đi theo hướng nào, với bước bao lớn? | Thu nhỏ bước, giải hệ Newton, kiểm phần dư đẳng thức. |
| [05. Huấn luyện](../bai-giang/bai-05-toi-uu-huan-luyen.md) | Có thể dùng ít dữ liệu hơn ở mỗi bước không? | Tính gradient lô nhỏ, vận tốc và điểm nhìn trước. |
| [06. Phương pháp thích nghi](../bai-giang/bai-06-phuong-phap-thich-nghi.md) | Mỗi tọa độ có nên dùng cùng một thang cập nhật? | Tính moment, hiệu chỉnh bước và phân biệt với Hessian. |
| [07. LP và quy hoạch động](../bai-giang/bai-07-quy-hoach-tuyen-tinh-va-dong.md) | Hình học hay phần còn lại giúp tránh liệt kê nghiệm? | Tìm cơ sở khả thi và tính Bellman từ cuối về đầu. |

## Chia một lecture thành các lượt đọc

Với Lecture 01, có thể dừng sau mô hình; lượt tiếp theo chỉ đọc tập và hàm lồi; lượt cuối mới chứng nhận tối ưu. Với Lecture 04, chạy gradient/backtracking trước, rồi mới đọc Newton và đẳng thức. Với Lecture 06, tính đủ một tọa độ Adam trước khi đi sang CG/BFGS. Những điểm dừng này dựa vào nhiệm vụ đã hoàn thành, không đặt thời lượng chung cho mọi người.

Trước mỗi lượt, thử nhớ lại một kết quả cần dùng từ bài trước. Sau lượt, giải ít nhất một bài mà chưa xem lời giải. Slides phục vụ ôn lại kết quả đã được giải thích trong Notes; chúng không thay những bước chứng minh.

## Nguồn nội dung và cấu trúc

Nguồn chính là bản local *Convex Optimization* của Boyd & Vandenberghe trong `toan-cho-ai/docs`. Chương 1–5 cung cấp lý thuyết; chương 9–10 cung cấp thuật toán; phụ lục A cung cấp nền. *Introduction to Linear Optimization* là reference cho hình học LP. *Probabilistic Graphical Models* là reference cho xác suất; bản scan không đọc chắc không được dùng để suy đoán nội dung.

Lecture 05–06 bổ sung nguồn chính thức *Deep Learning* chương 8, bài báo AdaGrad, Adam và Glorot. Mỗi Notes ghi mục nguồn cụ thể. Các ví dụ số tự đặt và chương trình minh họa được tách rõ khỏi ví dụ hoặc hình nguyên bản của tác giả.

Tên và thứ tự Lecture 00–07 theo [chỉ mục học phần 2026–2027](https://courses.iaidev.com/math-4-AI/2627-1/). Chỉ mục này chỉ dùng cho cấu trúc thanh lecture; không dùng Notes, Slides hay bài tập của trang làm nguồn nội dung.

## Tra cứu bổ sung

- [Hình học tập lồi](../doc-them/hinh-hoc-tap-loi.md) khi cần ellipsoid, nón, phối cảnh hoặc thứ tự Pareto.
- [Hessian](/wiki/hessian.md), [PSD](/wiki/ma-tran-psd.md), [KKT](/wiki/kkt.md) để ôn điều kiện ngay trước khi dùng.
- [Bài tập theo lecture](../bai-tap.md).
