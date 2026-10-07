# Dữ liệu học cách diễn đạt và cách đánh giá

Đây là hướng dẫn phát triển skill và corpus, không phải tuyên bố đã fine-tune. Gói hiện dùng tra cứu cục bộ, ví dụ tương phản và kiểm tra nghĩa. Không gửi dữ liệu hoặc tạo training job bên ngoài nếu người dùng chưa yêu cầu.

## Dữ liệu theo ba mức

| Mức | Đơn vị | Điều cần có |
| --- | --- | --- |
| Thuật ngữ | Một khái niệm trong lĩnh vực cụ thể | Cách gọi, định nghĩa, biến thể, ví dụ, xuất xứ và trạng thái kiểm chứng |
| Câu | Cùng ý bằng tiếng Anh và các giọng Việt | Bản kỹ thuật, lời giảng, bản cần sửa và nguyên nhân; nghĩa phải giữ |
| Mạch giảng | Một đoạn với các bước nối | Câu hỏi người học, nền đã biết, lập luận, bước dùng giả thiết, giới hạn và phản hồi |

[translation-examples.jsonl](translation-examples.jsonl) là bộ ví dụ nhỏ do dự án viết, không phải corpus thu từ lớp học hoặc dữ liệu đủ để huấn luyện một model. Các trường là định dạng nội bộ, không phải payload API của nhà cung cấp. Mỗi record có `source_en`, `context`, `literal_bad`, `technical_vi`, `lecture_vi`, `term_ids`, `why_bad`, `meaning_that_must_be_preserved`, `provenance`, `review_status` và `split`.

Tên `literal_bad` là bản cần sửa trong ngữ cảnh đó: có thể sai nghĩa hoặc chỉ gượng. `why_bad` phải phân biệt hai trường hợp. Câu Việt trôi chảy nhưng sai toán không được chọn làm đáp án tốt. Không tạo cặp preference từ ví dụ “tìm hướng cập nhật bằng điều kiện dừng” khi chưa có mô hình bài toán con cho phép thao tác đó.

## Khi thu corpus thật

Chọn giáo trình EN và VI cùng lĩnh vực, note và lời giải của giảng viên với quyền sử dụng phù hợp. Lưu URL/ấn bản/vị trí và tên cách gọi trong khóa học. Không giả vờ hai đoạn tương ứng hoàn toàn chỉ vì cùng chủ đề. Khi chỉ có tương ứng về khái niệm, ghi đó là ví dụ diễn đạt, không phải parallel sentence.

Người am hiểu môn kiểm tra nghĩa; người biên tập kiểm tra giọng. Không dùng mức tự tin hoặc số lượng sample như bằng chứng đúng. Giữ cả trường hợp có nhiều bản dịch hợp lệ, trường hợp cần ngữ cảnh và thuật ngữ chuẩn nghe không đời thường như “khả thi”.

## Đánh giá trước khi tăng công nghệ

Tách tập kiểm tra theo khái niệm/nguồn trước khi truy xuất ví dụ; không đưa bản Việt của chính câu kiểm tra vào prompt. Dùng các câu mới, đổi ký hiệu, số, miền và giọng. Khóa bộ ví dụ truy xuất khi so hai phiên bản.

Ghi số lỗi quan sát được và vị trí, tách bốn nhóm:

1. Chọn sai nghĩa hoặc thuật ngữ; bỏ qua yêu cầu dùng tên của giáo trình.
2. Mất điều kiện, phủ định, lượng từ, số 0 hoặc biến câu cần thành đủ.
3. Câu gượng, đối tượng mơ hồ hoặc mạch giải thích thiếu bước.
4. Truy xuất sai lĩnh vực, bỏ qua mơ hồ hoặc rò đáp án tập kiểm tra.

Đánh giá nghĩa là điều kiện trước để so độ tự nhiên. Không cộng điểm giọng tốt để bù lỗi toán. Nếu dùng preference, chỉ ghép các bản đã qua kiểm tra nghĩa; cặp câu sai để chẩn đoán cần được ghi rõ nhiệm vụ, không đưa vào huấn luyện phong cách như hai đáp án cùng đúng.

Không khẳng định một số lượng cố định như vài nghìn sample chắc chắn tốt hơn corpus lớn. Thử prompting/tra cứu trước, xem lỗi còn lại, rồi mới quyết định có cần huấn luyện. Nếu người dùng thật sự yêu cầu fine-tune, phải xác định model, API và định dạng đang hỗ trợ; chuyển dữ liệu nội bộ sau khi kiểm tra tài liệu chính thức hiện hành. Không có training job hay khóa API nào trong gói này.

## Mở rộng thuật ngữ mà không làm lệch nghĩa

Thêm ID ổn định, lĩnh vực, cụm EN, mô tả khái niệm, cách gọi VI, biến thể, phần phải giữ và nguồn cho mục mới. Phân biệt bằng chứng dùng thuật ngữ tiếng Việt với nguồn khái niệm tiếng Anh; chưa xác nhận thì ghi đúng trạng thái. Không dán nhãn “chuẩn Việt Nam” khi chỉ do AI đề xuất.

Sửa mục đã có cần kiểm tra các caller và ví dụ theo ID. Chạy các kiểm tra tra cứu domain, từ đứng riêng, Unicode, quan hệ cụm dài–ngắn và input hỏng; so lại prompt thật. `retrieve_terminology.py` chỉ tra từ/cụm trong kho, không xác nhận cách dùng ở mọi tài liệu.
