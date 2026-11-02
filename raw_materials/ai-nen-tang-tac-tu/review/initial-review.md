# Ghi nhận rà soát ban đầu

Phạm vi hiện tại: Chỉ chương 5 và 15. Mọi bản nháp chương khác ở worktree AGY được giữ lại và không đưa lên web.

## Nguồn và kiểm toán

- `source/manifest.json`: URL, tiêu đề, số từ và SHA-256 của từng trang nguồn.
- `scripts/content/fetch-artint3e.py`: Lưu lại HTML, giữ TeX từ MathML `alttext`, trích xuất văn bản. HTML là nguồn quyết định khi bảng/công thức trong bản trích xuất chưa rõ.
- `scripts/verification/audit-artint-coverage.py`: Phát hiện nguồn chưa có đích, ví dụ đánh số bị thiếu và trang ngắn bất thường. Không chứng nhận đúng nghĩa bằng số từ.
- `review/verify_logic.py`: Kiểm độc lập phép tương đương mệnh đề xác định, ví dụ Horn 5.17/5.18, phép thế/hợp nhất 15.15/15.16 và thứ tự lượng từ. Đã chạy thành công.

## Mục đã đọc đối chiếu

- 5.1: Đã đối chiếu cú pháp, thứ tự ưu tiên theo quy ước nguồn, bảng chân trị, hai diễn giải của Ví dụ 5.1, cơ sở tri thức của Ví dụ 5.2, điều kiện mô hình dự định. Giữ rõ `KB không suy ra g` không đồng nghĩa `KB suy ra phủ định g`.
- 5.2: Đã đối chiếu biến chỉ báo, câu tuyển, phép mã hóa CSP, bảy câu tuyển exactly-one cho miền bốn giá trị và năm câu tuyển bổ sung cho bất đẳng thức. Cần sửa cách gọi literal thành biến chỉ báo trong bản nháp AGY. Literal là nguyên tử hoặc phủ định nguyên tử, hai khái niệm không đồng nhất.

## Các lỗi phải xử lý sau khi nhận bản nháp

- Các công thức nối nhiều tên nguyên tử dài ở 5.1/5.2 phải được trình bày lại phù hợp điện thoại, không thu nhỏ chữ hoặc giấu phần tràn.
- Không giữ tài liệu tham khảo được thêm từ trí nhớ nếu chưa đọc/kiểm được mối liên hệ. Mỗi trang cần liên kết trực tiếp tới đúng mục sách gốc.
- Giao diện AGY ban đầu đã gán sai mục lục sách. Chỉ tích hợp sau khi sửa đúng chương 5/15 và loại bỏ liên kết tới chương chưa có.
- Không đưa metadata xác nhận quyền dịch hay thông báo triển khai vào luồng học tập. Giữ ghi công tác giả và nguồn rõ ràng.
- 15.3: Bản nháp thiếu các ví dụ được đánh số 15.6, 15.7, 15.9, thiếu giải thích công thức mở khi chưa gán giá trị cho biến tự do. Hai dòng `KB không kéo theo ...: Sai` cần sửa thành lời khẳng định chính xác rằng quan hệ không kéo theo là đúng, hoặc bỏ nhãn đúng/sai mơ hồ.
- 15.5: Cần phục hồi đầy đủ các Ví dụ 15.17, 15.19, 15.20 và các điều kiện phạm vi biến.
- 15.2: Dùng thống nhất “diễn giải dự định” và “bản thể học hình thức”. Tính đúng đắn của kết luận không đòi hỏi thủ tục chứng minh phải đầy đủ.
- 5.3: Ví dụ 5.13 phải nói hai nguyên tử suy ra được là c và g, không nói đó là hai hệ quả logic duy nhất. Các hằng đúng và công thức hợp vẫn là hệ quả khác.

## Kiểm tra nền trước khi tích hợp

`test_tools.py`: 38 kiểm tra công cụ đạt, một kiểm tra toàn kho hiện có thất bại do bốn bài Biểu diễn tri thức cũ được đánh dấu ready nhưng không còn slide. Kiểm tra này chạy với repo tại vị trí skill, không phải bản dịch mới. Chưa sửa nội dung học phần khác.

Chưa kiểm chứng trọn chương hoặc giao diện bản phát hành. Trạng thái này sẽ cập nhật sau khi nhận đủ nội dung.

## Cập nhật sau tích hợp

Các lỗi thuật ngữ và ví dụ nêu trên đã được sửa trong nhánh tích hợp. Kiểm tra 28 trang nguồn có đích, đủ 80 ví dụ được đánh số. Bản ghi tự động không thay cho đánh giá ngữ nghĩa. Có 48 kiểm tra danh mục/tiến độ đạt và kiểm chứng Python riêng. Còn chờ CI full và xác nhận Pages. Sau khi xuất bản hai chương phải tạm dừng theo yêu cầu người dùng.
