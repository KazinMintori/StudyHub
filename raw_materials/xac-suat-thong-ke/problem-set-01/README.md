# Hồ sơ biên soạn Problem Set 01

Nguồn đầu vào là tài liệu PDF tám trang tại [liên kết người dùng cung cấp](https://drive.google.com/file/d/15rh4mjFss-2plGRAI7zVQEquqy7lztYm/view). Bản PDF giữ cục bộ trong `source.pdf` theo quy tắc bỏ qua PDF của kho. `source.txt` là bản trích xuất để đối chiếu.

Phạm vi đưa lên trang gồm sáu mục tiêu và mười bài tập. Không đưa trang bìa, thông tin đơn vị, giảng viên, mã môn, đầu trang, chân trang hay các nhãn nguồn vào nội dung học tập.

| Phần | Bài | Số câu hỏi | Nội dung |
| --- | --- | --- | --- |
| A | 1 | 6 | Số máy gặp sự cố và tỷ lệ |
| A | 2 | 8 | Tỷ lệ từng nhóm và tỷ lệ gộp |
| A | 3 | 8 | Phép đo lặp và trọng số |
| A | 4 | 7 | Bảng liên hợp và thông tin mất khi gộp |
| B | 5 | 6 | Thứ tự thời gian và kết luận nhân quả |
| B | 6 | 6 | Chiều tác động, yếu tố chung và suy rộng |
| B | 7 | 7 | Tự nguyện tham gia và điều kiện hoàn thành |
| C | 8 | 6 | Loại biến và kiểu lưu trữ |
| C | 9 | 7 | Đọc cấu trúc Palmer Penguins bằng pandas |
| C | 10 | 9 | Đơn vị quốc gia theo năm và đo lặp |

Lời giải cùng giải thích công cụ được bổ sung để người mới tự học. Những mô tả nghiên cứu trong bài 5–7 được giữ ở dạng tình huống bài tập, không bổ sung khẳng định về một nghiên cứu cụ thể hay lời khuyên sức khỏe.

## Biên tập và đối chiếu Antigravity

Antigravity được gọi qua MCP để đọc văn bản nguồn, áp dụng các nguyên tắc của skill `studyhub-lecture` và viết lại mục tiêu cùng cả mười bài. Có một lần gọi ban đầu và hai lần điều chỉnh, đều giữ chế độ không bỏ qua quyền.

Lần đầu bị từ chối quyền chạy lệnh trong chế độ nền. Lần điều chỉnh thứ nhất vượt giới hạn độ dài dòng lệnh Windows. Lần cuối đã tạo bản viết đầy đủ nhưng cầu nối lỗi khi trả kết quả. Nội dung Markdown đã được khôi phục từ bản ghi chỉ đọc của chính phiên đó, không gọi thêm tác vụ.

`antigravity-draft.md` giữ nguyên bản viết khôi phục để đối chiếu. Codex đọc toàn bộ mục tiêu và câu hỏi trong bản này, đối chiếu lại với PDF, rồi rút gọn và sửa trước khi đưa lên trang. Bản cuối giữ các phân biệt về số máy và số sự kiện, trọng số, đo lặp, kiểu lưu trữ và đơn vị quốc gia theo năm.

Những điểm cần sửa trong bản thảo gồm công thức chứa văn xuôi quá dài, cách gọi loại biến thành thang đo, giả thiết tự thêm về địa điểm nghiên cứu và một số kết luận diễn đạt quá mạnh. Bản trên trang giữ đúng dữ kiện gốc, dùng lời giải ngắn, tách văn xuôi khỏi công thức và kiểm tra riêng đầu ra Python.

## Tái lập kết quả

Chạy từ thư mục gốc dự án, với pandas và matplotlib đã cài:

```sh
python -X utf8 -I raw_materials/xac-suat-thong-ke/problem-set-01/verify.py
python -I docs/public/materials/xac-suat-thong-ke/problem-set-01/penguins.py
```

`verify.py` kiểm các tỷ lệ, trọng số, trung bình và bảng đếm bằng phân số chính xác. Script đọc bản CSV đi kèm, kiểm kích thước và dữ liệu, rồi tạo ảnh năm hàng đầu thành ba nhóm cột. `verification.json` ghi phiên bản pandas và mã SHA-256 của CSV. `python-output.txt` giữ bốn đầu ra của mã tải về.

CSV được tải từ [kho Palmer Penguins](https://github.com/allisonhorst/palmerpenguins/blob/main/inst/extdata/penguins.csv). Dữ liệu được phát hành theo CC0, xem [trang dự án](https://allisonhorst.github.io/palmerpenguins/).
