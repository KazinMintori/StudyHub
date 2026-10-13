# Rà soát nội bộ: Câu hỏi thảo luận Chương 28

## Phạm vi nguồn

Đã so sánh đủ Q28.1–Q28.20 với phần Discussion Questions trên trang in 944–945 (PDF 964–965). Cả 20 câu hỏi và 20 lời giải hiện diện trong `translations/chapter-28/11-cau-hoi-thao-luan.md`, gồm mọi tiểu phần và yêu cầu giải thích. Các câu mô tả hiện tượng giữ điều kiện cần thiết, còn bài toán đơn vị và tỉ lệ có phép biến đổi rõ ràng.

## Kiểm tra độc lập

`raw_materials/physics/verify_chapter28_discussion.py` chạy bằng Python/NumPy và đạt. Bộ kiểm tra mô hình hóa các nhận định thay vì chỉ đối chiếu văn bản: thông lượng của trường đơn cực giả định, chiều trường của dòng hạt chuyển động, giới hạn dây hữu hạn, công suất lực từ bằng không, triệt tiêu trường của cặp dây hồi, lực tự trường tổng trên vòng kín, lực dây và vòng đồng tâm, các cấu hình dòng của ba dây, tính khép kín của đường trường hình xuyến, điều kiện triệt tiêu Q28.12, chiều dòng mạch Q28.13, tỉ số trường vòng dây Q28.14, thứ nguyên Q28.15, quy luật Curie và dấu độ cảm từ, mômen nguyên tử ghép đôi, cùng bảo toàn mômen động lượng trong hiệu ứng Einstein–de Haas.

## Các kết luận cần giữ

- Q28.6: Ba dây hút từng đôi khi dòng cùng chiều. Không thể làm cả ba cặp đẩy nhau vì quan hệ “ngược chiều” không bắc cầu.
- Q28.8: Vòng trong chịu thành phần lực hướng ra ngoài; vòng ngoài chịu thành phần hướng vào trong. Đối xứng làm lực tịnh tiến tổng trên từng vòng bằng không.
- Q28.12: Với hai dòng bằng nhau ngược chiều, không có điểm hữu hạn triệt tiêu hoàn toàn; với hai dòng cùng chiều, trung điểm là điểm triệt tiêu.
- Q28.13: Cực b dương làm dòng trên dây L hướng trái, cùng chiều với dòng dây dưới, phù hợp lực hút quan sát.
- Q28.14: Tăng bán kính gấp đôi làm trường tại tâm giảm một nửa. Trên trục tại x cố định, tỉ số phụ thuộc x/a.
- Q28.16–19: Mômen thuận từ thường trực chịu trật tự nhiệt, độ cảm từ giảm khi T tăng. Chất nghịch từ có đáp ứng cảm ứng yếu và ít phụ thuộc nhiệt độ. Oxy có χ dương, nitơ có χ âm.
- Q28.20: Đảo mômen từ vi mô đòi hỏi phần mômen động lượng cơ học của trụ bù để tổng mômen động lượng được bảo toàn.

## Trình bày

Các khối lời giải có tóm tắt và hướng đi dạng gạch đầu dòng. Không có công thức hiển thị hoặc nội dòng quá rộng trong fragment 11 theo `node scripts/audit-physics-math.mjs 28`.
