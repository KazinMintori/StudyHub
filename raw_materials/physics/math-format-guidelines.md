# Quy tắc trình bày công thức vật lý

- Quan hệ độc lập trong Cheatsheet dùng `formulaRows`, mỗi dòng có nhãn và công thức. Giả thiết dài đặt ở nhãn hoặc phần mô tả, không dồn thành chỉ số tiếng Việt dài.
- Các bước của cùng một phép suy diễn dùng `aligned`, căn dấu bằng. Không tách riêng một vế trái rất ngắn thành một dòng khi cả quan hệ đủ chỗ.
- Không nối nhiều dấu bằng kèm kết quả số dài trên cùng dòng trong hộp hẹp. Giữ biểu thức giải tích và giá trị số ở các bước kế tiếp.
- Số hiệu công thức của môn vật lý do `static-math-plugin.mjs` đưa ra ngoài SVG. Trên điện thoại số nằm dưới, bên phải. Không bẻ nội dung chỉ để dành chỗ cho số hiệu.
- Không thu nhỏ công thức đến khó đọc hoặc cắt phần vượt khung. Khi cần ký hiệu phụ, phải định nghĩa rõ và giữ biểu thức tương đương đầy đủ.
- Kiểm tra bề rộng khung thật, không chỉ bề rộng màn hình. Khung lời giải và thẻ tra cứu đều có lề trong.
- Chạy `verify-physics-responsive-layout.mjs` để đổi cùng trang từ máy tính sang điện thoại và ngược lại, sau đó đọc ảnh kết quả. Kiểm tra không tràn là cần thiết nhưng chưa đủ để chứng nhận dễ đọc.
