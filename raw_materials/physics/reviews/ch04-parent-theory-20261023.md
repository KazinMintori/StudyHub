# Rà soát lý thuyết chương 4

Phạm vi: Phần mở đầu, sáu mục 4.1–4.6 và tổng kết, trang in 100–121 của tài liệu nguồn. Phần bài tập cuối chương đang được soạn riêng và chưa được chứng nhận hoàn tất.

## Đối chiếu nội dung

- Mở đầu: Sáu mục tiêu, kiến thức ôn lại và câu hỏi người nâng tạ với đầy đủ các phương án.
- Mục 4.1: Tương tác tiếp xúc và từ xa, lực là vector, tổng hợp lực, các thành phần, bảng 4.1, ví dụ 4.1 và tự kiểm 4.1.
- Mục 4.2: Quán tính, điều kiện cân bằng, hai ví dụ 4.2–4.3, hệ quán tính và biến đổi vận tốc giữa hai hệ, tự kiểm 4.2.
- Mục 4.3: Quan hệ giữa lực, khối lượng và gia tốc, đơn vị lực và bảng 4.2, dạng vector và thành phần, điều kiện áp dụng, ví dụ 4.4–4.5, ứng dụng tai trong và xe máy, tự kiểm 4.3.
- Mục 4.4: Phân biệt khối lượng và trọng lượng, biến thiên trọng trường, cân so sánh khối lượng, ví dụ 4.6–4.7, tự kiểm 4.4.
- Mục 4.5: Cặp lực tương tác, lời giải câu hỏi nâng tạ, các ví dụ 4.8–4.11, dây có khối lượng và dây lý tưởng, tự kiểm 4.5.
- Mục 4.6: Chọn vật, phân biệt lực tác dụng lên vật và lực do vật tác dụng, sơ đồ riêng cho mỗi vật, ba ứng dụng vận động, tự kiểm 4.6.
- Tổng kết: Năm nhóm kiến thức với năm hình tổng kết.

## Hình ảnh

Đã đối chiếu trực quan 29 hình đánh số, ảnh mở đầu, hai ảnh ứng dụng và năm hình tổng kết. Tổng cộng 37 ảnh cắt trực tiếp từ PDF, có tọa độ tái tạo trong `scripts/prepare-physics1-remaining-04-parent-assets.py`. Phép so sánh raster độc lập khớp cả 37 ảnh. Mép dưới hình 4.22 đã được mở rộng để giữ trọn nhãn trọng lượng trên Mặt Trăng.

Chú thích tiếng Việt và các cặp nhãn tiếng Việt/tiếng Anh được khai báo trong `physics1-remaining-04-parent-image-annotations.mjs`.

## Tính toán và hiệu đính

`verify_chapter04_parent_opening.py` tính lại các thành phần lực, góc phần tư, gia tốc, lực hãm, trọng lượng và đổi đơn vị. Ví dụ 4.1 nói rõ việc dùng các thành phần đã làm tròn. Lỗi số học của ví dụ 4.7 được ghi riêng trong `chapter-04-source-errata.md`. Dữ kiện đề bài được giữ, kết quả được sửa thành 2500 kg và −7,32 m/s².

## Kiểm tra tích hợp

- Kiểm tra bài giảng: Một trang chương và sáu trang chủ đề, không lỗi hoặc cảnh báo cấu trúc.
- Trình duyệt: Sáu chủ đề ở các chiều rộng 320, 375 và 1440 px, mở mọi khối lời giải. Cả 18 trường hợp không tràn trang, không công thức vượt khung, không ảnh hỏng và không lỗi MathJax.
- Cheatsheet: Chỉ định nghĩa, tính chất, điều kiện áp dụng và công thức. Đã nối đồng thời bộ nạp máy khách và registry máy chủ. Phép đo riêng gồm 20 công thức hiển thị và hai công thức nội dòng đạt giới hạn chiều rộng.
- Kiểm thử hồi quy liên quan đến bộ nạp cheatsheet và biên dịch công thức: Đã chạy thành công.

Trạng thái: Lý thuyết đã soạn và kiểm tra. Chưa chuyển toàn bộ chương sang sẵn sàng vì còn chờ bài tập cuối chương và lượt kiểm tra tích hợp cuối cùng. Không chạy build toàn cục tại máy người dùng.
