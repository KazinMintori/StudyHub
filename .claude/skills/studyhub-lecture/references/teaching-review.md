# Kiểm tra lời giảng và phản hồi khi người học chưa hiểu

Đọc khi tạo note, một phần giải thích khó hoặc khi người học nói “chưa hiểu”. Không biến mọi trả lời ngắn thành một hồ sơ QA.

## Note phải tự đứng được

Note không phải bản chép bullet slide hoặc bản ghi lời nói. Giữ phát biểu hình thức, lý do, các bước quyết định và ví dụ có lời giải. Dùng câu hỏi làm tiêu đề khi nó giúp tra cứu, nhưng trả lời câu hỏi trong phần đó. Ký hiệu phải có nghĩa; hình phải có số/ID, chú giải và lời chỉ rõ điều cần nhìn. Không dựa vào thao tác chỉ tay của giảng viên.

Với bộ slide kèm note, đối chiếu từng cụm: Cùng giả thiết, ký hiệu, số liệu, kết luận và phiên bản. Note có thể giải thích dài hơn; không được lén sửa một định lý mà slide vẫn ghi bản cũ. Ghi chú riêng của giảng viên không thay note giao cho sinh viên.

## Khi người học đáp lại

Chỉ dùng nhánh tương tác khi người dùng muốn học đối thoại hoặc đã gửi bài làm. Nếu họ yêu cầu giải thích trực tiếp, cung cấp lời giải trước; không ép họ trả lời chẩn đoán mới được giảng.

| Quan sát thật | Phản hồi tiếp theo |
| --- | --- |
| Đúng và có lý do | Chỉ ra điều họ đã làm đúng; thử chuyển giao hoặc bỏ bớt hỗ trợ |
| Đúng đáp số nhưng thiếu lý do | Hỏi đúng một bước cần giải thích, hoặc giải thích nếu họ đang cần lời giải trực tiếp |
| Đúng một phần | Giữ phần đúng, xác định khoảng trống và bổ sung cầu nối ở đó |
| Sai | Tìm bước sai đầu tiên trong bài làm, minh họa bằng trường hợp nhỏ, rồi cho thử lại bước đó |
| Không trả lời hoặc chỉ nói “hiểu rồi” | Chưa đủ bằng chứng thành thạo; không tự nâng mức hoặc ghi “đã nắm vững” |

Không trả lời “hãy đọc lại” hoặc lặp nguyên đoạn cũ. Thử đổi biểu diễn: Số cụ thể thay ký hiệu, truy vết thay mô tả, hai trường hợp đối chiếu thay định nghĩa. Sau đó nối trở lại phát biểu hình thức. Gợi ý tăng dần nếu người học muốn tự giải; đưa lời giải đầy đủ khi họ yêu cầu.

Nếu ghi trạng thái để học tiếp, chỉ ghi điều người học thực sự đã thể hiện: Mục đang học, bước họ làm được, lỗi quan sát được, ký hiệu và bài tiếp theo. Tách giả định khỏi chứng cứ. Không tự lưu dữ liệu cá nhân hoặc bật dịch vụ theo dõi bên ngoài.

## Kiểm tra bằng một “người học mới” có nền cụ thể

Tạm chỉ cho phép kiến thức đã xác nhận và phần đã dạy. Tại mỗi bước, hỏi người học lấy đâu ra thuật ngữ hoặc phép suy ra này. Đánh dấu khoảng trống rồi sửa. Đây là tự rà theo góc nhìn khác, không gọi là thử nghiệm độc lập hay kết quả học của sinh viên.

Kiểm tra cả thuật ngữ phụ do người giảng vừa thêm, không chỉ thuật ngữ trong sách. Chẳng hạn, nếu người học mới biết đạo hàm, gọi một biểu thức là “hàm affine” hoặc dùng ký hiệu chuẩn \(\|x\|\) mà chưa giải thích sẽ tạo khoảng trống mới. Có thể chỉ dùng biểu thức cụ thể hoặc giải thích ngay nghĩa cần dùng. Chọn ví dụ nhỏ trong nền đã biết trước khi mở sang nhiều biến hoặc thêm một chứng minh phụ. Chỉ mở rộng khi điều đó giải quyết mục tiêu đang học; kiểm tra ví dụ không có nghĩa phải dạy cả lý thuyết đứng sau nó.

Rà tiếp theo ba câu:

- Nếu bỏ một giả thiết, kết luận còn đúng không? Chỉ cần thử điều kiện đáng nghi, không sinh phản ví dụ theo nghi thức.
- Người học có thể làm một bước mới tương tự không? Ví dụ đã giải chỉ chứng minh người giảng biết làm.
- Sau lượt sửa ngôn ngữ, có thay đổi “mọi”, “một”, “có thể”, “khi và chỉ khi”, dấu hoặc miền không?

Với bài dài, lưu lỗi, bằng chứng và sửa ở đâu. Không dùng điểm “professor-like” thay bằng chứng. Chỉ báo kiểm tra nguồn, tính toán, chạy mã hoặc render nếu đã thực hiện thật.

## Dấu hiệu cần xem lại bằng script

`scripts/review_teaching_text.py` đọc Markdown/văn bản hoặc JSON đặc tả slide. Nó chỉ báo vị trí cụm gượng, câu quá tải theo heuristic và mẫu mở câu lặp. Nó bỏ code fence, blockquote và không lint excerpt nguồn trong JSON. Nó không thể tìm tất cả trích dẫn trong văn xuôi; người biên tập phải xem ngữ cảnh.

```text
python scripts/review_teaching_text.py note.md --output language-review.json
python scripts/review_teaching_text.py course-spec.json --output language-review.json
```

Mọi kết quả đều là đề nghị xem lại; exit 0 nghĩa là đã chạy, không có nghĩa lời giảng đã đạt. Script không tự thay chữ, không kiểm tra toán, không nhận dạng AI, không hiểu người học. Thiếu cảnh báo vẫn phải rà nghĩa và bước nối. Với output ngôn ngữ khác tiếng Việt, không áp dụng từ điển này như chuẩn bản địa.
