# Khung một trang Notes như giảng viên viết

Đọc khi soạn hoặc sửa Notes. Đây là khung mặc định cho một buổi học 60–120 phút đọc–làm, không phải mẫu phải điền đủ ô. Bài Python thực hành, bài định lý và bài đọc tư liệu sẽ có tỉ lệ các phần khác nhau. Ví dụ minh họa dưới đây do người soạn skill viết; không chép vào bài nếu không khớp nguồn.

Bài tham chiếu tốt trong repo: `docs/giai-thuat-du-lieu/bai-giang/bai-03-pagerank-mo-hinh-va-tinh-toan.md` — một ví dụ nhỏ tính tay chạy xuyên suốt, mỗi bước có lý do, bài tập gắn trang nguồn, lời giải gập, nguồn cụ thể đến mục và trang.

## 1. Mạch của trang

| Phần | Việc nó phải làm | Dấu hiệu đạt |
| --- | --- | --- |
| Đoạn mở (không H1) | Nêu bài toán/câu hỏi có thật mà bài trả lời; nối với bài trước; nói người học sẽ làm được gì và cần biết gì trước | Một sinh viên đọc xong biết vì sao phải học bài này và mình đã đủ nền chưa |
| `## 1.` Vấn đề cụ thể | Đặt một trường hợp nhỏ có số/đối tượng thật; cho người học thử dự đoán hoặc thử cách ngây thơ | Cách ngây thơ thất bại ở chỗ chỉ ra được, tạo nhu cầu cho khái niệm mới |
| `## 2…n.` Các cụm khái niệm | Mỗi cụm: Phát biểu chính xác → cơ chế/lý do → ví dụ có lời giải → ranh giới áp dụng → một câu tự kiểm | Không còn bước nhảy mà người học mục tiêu phải tự đoán |
| Thực hành (khi môn có thao tác) | Code chạy được, truy vết trạng thái, hoặc quy trình tính tay đầy đủ | Người học tự làm lại được trên đầu vào khác |
| `## Bài tập tự luyện` | 3–6 bài tăng dần: Nhận diện → tính → giải thích → chuyển giao; mỗi bài `::: exercise` + `::: hint` (tùy) + `::: solution` | Lời giải có lý do từng bước, không chỉ đáp số; ghi nguồn bài nếu lấy từ giáo trình |
| `## Tóm tắt` | Trả lời câu hỏi mở đầu; liệt kê điều đã làm được, kèm điều kiện | Mỗi dòng kiểm tra được, không phải khẩu hiệu |
| `## Nguồn và đọc thêm` | Tài liệu thật, đến chương/mục/trang; tách nguồn của bài với đọc thêm | Người học mở được và tìm đúng chỗ |

Số mục H2 theo nội dung, không theo mẫu. Đánh số H2 (`## 1.`) khi bài dài để dễ tham chiếu; `(dùng mục lục của VitePress)` cho bài trên khoảng 300 dòng.

## 2. Cụm khái niệm: Đơn vị giảng chính

Một cụm trả lời **một** câu hỏi của người học. Trình tự thường dùng (đổi khi nội dung đòi hỏi):

1. **Câu hỏi dẫn.** Một câu nói rõ người học đang thiếu gì: “Một vòng chia điểm chưa xử lý trang không có liên kết ra. Điểm của trang đó đi đâu?”
2. **Phát biểu chính xác.** Định nghĩa/định lý/thuật toán đủ giả thiết, miền, lượng từ. Có thể in đậm **tên** khái niệm ở lần định nghĩa; không in đậm cả câu.
3. **Mở bước.** Bước mà chuyên gia làm tự động nhưng người mới chưa: Vì sao chọn phép biến đổi này, giả thiết nào được dùng ở dòng nào, ký hiệu nào đang chỉ cái gì. Xem content-prompts.md theo loại nội dung.
4. **Ví dụ có lời giải** trên đối tượng chạy xuyên suốt nếu có. Tính số thật; kiểm bằng code trước khi ghi.
5. **Ranh giới.** Bỏ một giả thiết thì điều gì gãy? Trường hợp biên nào cần xét? Chỉ dùng phản ví dụ khi nó làm rõ đúng giả thiết đó, và nói nó chứng minh tới đâu.
6. **Tự kiểm.** Một câu hỏi chẩn đoán đúng chỗ dễ sai, đáp án gập.

Không phải cụm nào cũng cần đủ sáu bước. Một khái niệm nhỏ có thể chỉ là một câu định nghĩa và một ví dụ.

## 3. Hộp (container): Mỗi loại một nhiệm vụ

| Hộp | Dùng cho | Không dùng cho |
| --- | --- | --- |
| `::: example` | Ví dụ có lời giải liền mạch | Đề bài bắt người học tự làm |
| `::: proof` / `::: derivation` | Chứng minh đầy đủ hoặc khai triển dài mà mạch chính chỉ cần kết quả + ý tưởng | Bước quyết định mà người học cần để hiểu kết luận — bước đó phải nằm ngoài hộp gập |
| `::: exercise` → `::: hint` → `::: solution` | Bài tự làm, gợi ý tăng dần, lời giải gập | Câu hỏi tu từ |
| `::: tip` | Một câu hỏi để tự trả lời trước khi đọc tiếp — và đáp án nằm trong `<details>` hoặc ngay đoạn sau | Lời khuyên học tập chung chung |
| `::: warning` | Một ngộ nhận cụ thể có thể xảy ra, kèm ví dụ cho thấy vì sao sai và cách đúng | “Bẫy thi cử cực kỳ phổ biến” không có căn cứ |
| `::: info` | Bối cảnh/ghi chú bên lề không cần cho mạch chính | Nội dung cốt lõi (sẽ bị đọc lướt) |
| `::: danger` | Lỗi làm hỏng dữ liệu/kết quả thật (code xóa dữ liệu, chia cho 0 trong thuật toán) | Nhấn mạnh cảm xúc |

Nếu bỏ một hộp mà bài mất nội dung thiết yếu, nội dung đó không nên nằm trong hộp. Tối đa khoảng một hộp cảnh báo cho mỗi cụm; nhiều hơn là dấu hiệu cảnh báo đang thay giải thích.

## 4. Những lỗi đã thấy trong bài thật của site và cách sửa

Các câu “cần sửa” dưới đây là bản diễn đạt lại kiểu lỗi, không trích nguyên văn.

| Kiểu lỗi | Vì sao hại | Cách làm đúng |
| --- | --- | --- |
| Đoạn trích mở đầu gán cho một nhà khoa học (“X đã nghĩ vậy khi viết…”) mà không có nguồn câu nói | Bịa trích dẫn; người học có thể trích lại | Bỏ, hoặc dẫn câu thật kèm nguồn kiểm được. Mở bài bằng câu hỏi của chính bài học tốt hơn |
| Hộp “Bản chất: …” chứa câu khái quát hoa mỹ | Nhãn hứa sâu sắc nhưng nội dung là khẳng định không chứng minh | Thay bằng câu hỏi cụ thể mà khái niệm trả lời, rồi trả lời |
| “Bẫy thi cử cực kỳ phổ biến”, “học sinh hay nhầm” | Khẳng định tần suất không có dữ liệu | “Một cách đọc dễ nhầm là…”, kèm ví dụ hai trường hợp |
| In đậm năm cụm trong một đoạn | Không còn gì nổi bật; đọc như quảng cáo | In đậm tên khái niệm khi định nghĩa, hoặc một điều kiện quyết định. Còn lại dùng câu |
| “Đây chính là…”, “cực kỳ hữu ích”, “then chốt” | Đánh giá thay vì giải thích | Nói tác dụng: “Bước này đưa ràng buộc chuẩn về dạng nón, nên dùng được kết quả của mục 2.3” |
| Ẩn dụ chủ đạo (“dây thun”, “di chuyển an toàn”) không có chỗ dừng | Người học suy rộng ẩn dụ | Nêu ánh xạ và chỗ ẩn dụ ngừng đúng |
| Bảng/thuật ngữ tiếng Anh xen giữa câu Việt (“model soup”, “lifting”) không giải thích | Tạo tiên quyết mới | Giải thích ngay hoặc bỏ nếu không phục vụ mục tiêu |
| Kết luận đặt trước lý do, lý do nằm trong hộp gập | Người đọc lướt chỉ nhận khẩu hiệu | Lý do thiết yếu nằm trong mạch chính |

## 5. Ví dụ xuyên suốt

Chọn **một** đối tượng nhỏ, tính tay được, dùng lại qua các cụm (đồ thị bốn trang trong PageRank; bảng 100 người trong xác suất có điều kiện; mảng 3×4 trong NumPy). Mỗi lần quay lại, chỉ thay đổi đúng một yếu tố đang học. Khi đổi đối tượng, nói vì sao.

Mọi con số trong ví dụ, bài tập và lời giải phải được tính lại bằng code (Python `fractions.Fraction` cho phân số, NumPy cho ma trận) trước khi ghi. Không đặt số trông như thống kê thật làm người học tưởng là chứng cứ; không ghi các chú thích thừa như "dữ liệu giả định", "thông tin giả định" vào bài.

## 6. Nguồn và ranh giới “sách nói / bài giảng thêm”

- Nội dung lấy từ giáo trình/slide của môn: Ghi nguồn ở cuối bài, và ghi tại chỗ khi dùng hình, bài tập hay số liệu cụ thể (“Bài 1 — MMDS 5.1.1, tr. 187”).
- Ví dụ, ẩn dụ, ứng dụng AI do người soạn thêm: Ghi nhận được bằng lời (“Ví dụ thêm:”, “Một cách hình dung:”). Không gán cho tác giả giáo trình.
- Không thêm sự kiện lịch sử, năm tháng, tên nhà khoa học, số liệu thực tế hoặc câu trích nếu chưa kiểm chứng được nguồn. Nếu cần, tra cứu và dẫn link; nếu không kiểm được, bỏ.
- Không chép nguyên đoạn dài từ giáo trình; diễn đạt lại và giải thích.

## 7. Độ dài và mật độ

Đủ để người học tự theo được mà không có giảng viên, không hơn. Bài hiện có trên site dài khoảng 250–900 dòng Markdown. Phần lý thuyết nặng nên tách thành nhiều bài theo điểm kết thúc một nhiệm vụ học, không theo số trang sách. Một đoạn văn thường 2–5 câu; một câu một bước tư duy chính.

## 8. Sau Notes: Chiếu sang Slides và Kiến thức nền

- **Slides catalog** (xem repo-format.md mục 4): Một slide cho mỗi cụm chính, cùng thứ tự; giữ điều kiện cạnh kết luận; công thức Unicode; ví dụ số lấy từ Notes. Đọc từng bullet và tìm câu tương ứng trong Notes — không có thì sửa slide hoặc sửa Notes.
- **Kiến thức nền**: Liệt kê khái niệm Notes dùng mà không dạy lại. Rà các thuật ngữ phụ người soạn vừa thêm (affine, chuẩn, ma trận thưa…): Hoặc dạy trong Notes, hoặc đưa vào prerequisites, hoặc bỏ.

## 9. Khung Markdown khởi đầu

```markdown
---
course: <course-id>
lecture: <slug>
section: lecture
title: "<Tên bài như trong catalog>"
prerequisites: ["<id>", "<id>"]
lessonStatus: draft
description: "<Phạm vi bài trong một câu.>"
---

<Đoạn mở: câu hỏi của bài, nối với bài trước, sau bài học làm được gì, cần biết gì trước.>

(dùng mục lục của VitePress)

## 1. <Vấn đề cụ thể>

<Trường hợp nhỏ có số thật. Thử cách ngây thơ; chỉ ra chỗ nó không đủ.>

::: tip Thử trước khi đọc tiếp
<Một câu hỏi dự đoán.>
:::

<details><summary>Đáp án</summary>

<Đáp án và lý do.>

</details>

## 2. <Khái niệm/kết quả thứ nhất>

<Câu hỏi dẫn. Phát biểu chính xác. Mở bước. Ranh giới.>

::: example <Tên ví dụ>
<Dữ kiện → bước → kết quả → kiểm tra hợp lý.>
:::

## <n>. Bài tập tự luyện

### Bài 1 — <nguồn nếu có>

::: exercise
<Đề.>
:::

::: hint
<Gợi ý không lộ đáp án.>
:::

::: solution
<Lời giải đủ lý do.>
:::

## <n+1>. Tóm tắt

<Trả lời câu hỏi mở đầu; điều làm được, kèm điều kiện.>

## <n+2>. Nguồn và đọc thêm

- <Tác giả, *Tên sách*, ấn bản — chương/mục/trang.>
```

Đổi `lessonStatus` sang `ready` chỉ khi các phần đã đầy đủ và catalog đã có slide.


## Quy tắc giao diện Mực tím trên giấy vở

- Notes là tab mặc định; thứ tự Notes, Slides, Kiến thức nền. Địa chỉ cũ `#bai-tap` chuyển về Notes. Bài tập môn ở cuối Notes.
- Không chèn mục lục trong Markdown: VitePress có mục lục bên phải và trên điện thoại.
- Tiêu đề viết bằng chữ; không đặt công thức trong heading vì mục lục làm mất ký hiệu.
- Công thức trong Notes và Wiki dùng `$…$`; chữ tiếng Việt nằm ngoài công thức.
- Màu lấy từ `docs/.vitepress/theme/tokens.css`. SVG nội tuyến dùng biến token; SVG tĩnh dùng bảng màu sáng và đặt trên giấy trắng khi tối.
- Chữ SVG tối thiểu 14 đơn vị; chữ trong hình không dưới 12 đơn vị.
