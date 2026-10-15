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
| `## Bài tập tự luyện` | 3–6 bài tăng dần: Nhận diện → tính → giải thích → chuyển giao; mỗi bài `::: exercise` + `::: hint` (tùy) + `::: solution` | Lời giải có lý do từng bước, giải thích bản chất tường minh, không chỉ đưa ra đáp số đơn thuần |
| `## Tóm tắt` | Trả lời câu hỏi mở đầu; liệt kê điều đã làm được, kèm điều kiện | Mỗi dòng kiểm tra được, không phải khẩu hiệu |
| `## Tài liệu tham khảo` | Danh mục tài liệu tham khảo chuẩn mực theo quy chuẩn học thuật | Người học tra cứu và mở rộng |

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

## 6. Chủ quyền bài giảng và tính xác thực học thuật

- Bài giảng của StudyHub là giáo trình độc lập, hoàn chỉnh của chính người giảng viên. Tuyệt đối không để bài giảng mang tính chất sổ tay trích dẫn hay đối chiếu sách thụ động. Nghiêm cấm các câu và cụm từ: “Nội dung lấy từ giáo trình…”, “Lấy từ slide của môn…”, “Bài tập lấy từ sách…”, “Ví dụ do người soạn thêm, không gán cho tác giả giáo trình…”, “Ảnh lấy từ sách”, “Hình trong sách”, “Dữ liệu này từ…”, “Theo sách…”, “Nguyên tác…”, “Bản dịch của…”.
- Mọi tư liệu, hình ảnh, ví dụ, bài tập phải trở thành một phần tự nhiên của bài giảng (“Hình 1.1: …”, “Xét bài toán thực tế sau: …”, “Quan sát đồ thị chuyển trạng thái…”). Mọi bài giảng là một thực thể tri thức độc lập, hoàn chỉnh, tự chịu trách nhiệm về mặt học thuật và sư phạm.
- Không thêm sự kiện lịch sử, năm tháng, tên nhà khoa học, số liệu thực tế hoặc câu trích nếu chưa kiểm chứng được nguồn. Nếu cần, tra cứu và kiểm chứng nguồn gốc chuẩn xác; nếu không kiểm chứng được, kiên quyết lược bỏ.
- Mục cuối bài luôn đặt tên là `## Tài liệu tham khảo` theo đúng quy chuẩn học thuật chuẩn mực, không phân bua “do người soạn bổ sung”.

## 7. Độ dài và mật độ

Đủ để người học tự theo được mà không có giảng viên, không hơn. Bài hiện có trên site dài khoảng 250–900 dòng Markdown. Phần lý thuyết nặng nên tách thành nhiều bài theo điểm kết thúc một nhiệm vụ học, không theo số trang sách. Một đoạn văn thường 2–5 câu; một câu một bước tư duy chính.

## 8. Sau Notes: Chiếu sang Slides và Kiến thức nền

- **Slides catalog** (xem repo-format.md mục 4): Một slide cho mỗi cụm chính, cùng thứ tự; giữ điều kiện cạnh kết luận; công thức Unicode; ví dụ số lấy từ Notes. Đọc từng bullet và tìm câu tương ứng trong Notes. Nếu không có thì sửa slide hoặc sửa Notes.
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

<Đoạn mở: Câu hỏi của bài, nối với bài trước, sau bài học làm được gì, cần biết gì trước.>

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

### Bài 1: <Tiêu đề bài tập>

::: exercise
<Đề bài.>
:::

::: hint
<Gợi ý không lộ đáp án.>
:::

::: solution
<Lời giải đủ lý do và tính toán chính xác.>
:::

## <n+1>. Tóm tắt

<Trả lời câu hỏi mở đầu; điều làm được, kèm điều kiện.>

## <n+2>. Tài liệu tham khảo

- <Tác giả, *Tên sách*, Nhà xuất bản.>
```

Đổi `lessonStatus` sang `ready` chỉ khi các phần đã đầy đủ và catalog đã có slide.


## Quy tắc giao diện Mực tím trên giấy vở

- Notes là tab mặc định; thứ tự Notes, Slides, Kiến thức nền. Địa chỉ cũ `#bai-tap` chuyển về Notes. Bài tập môn ở cuối Notes.
- Không chèn mục lục trong Markdown: VitePress có mục lục bên phải và trên điện thoại.
- Tiêu đề viết bằng chữ; không đặt công thức trong heading vì mục lục làm mất ký hiệu.
- Công thức trong Notes và Wiki dùng `$…$`; chữ tiếng Việt nằm ngoài công thức.
- Màu lấy từ `docs/.vitepress/theme/tokens.css`. SVG nội tuyến dùng biến token; SVG tĩnh dùng bảng màu sáng và đặt trên giấy trắng khi tối.
- Chữ SVG tối thiểu 14 đơn vị; chữ trong hình không dưới 12 đơn vị.
- **Chuẩn mực toán học & Quy tắc ngắt dòng (Math Standards & Line-Breaking Rules)**:
  - Tuyệt đối không để phát sinh thanh cuộn ngang (scrollbar) trên bất kỳ công thức nào, ở mọi kích thước màn hình và trong mọi khung hộp (`::: info`, `::: details`).
  - **Chỉ ngắt dòng tại dấu quan hệ, cấm nhảy xuống dòng khi chưa đến dấu bằng**:
    - Với công thức dài hoặc chuỗi biến đổi nhiều bước: Chỉ được bẻ dòng bằng `\begin{aligned}...\end{aligned}`, ngắt dòng bằng `\\` tại dấu bằng ($=$), bất đẳng thức ($\le, \ge, <, >$), xấp xỉ ($\approx$) hoặc suy luận ($\implies, \iff$) và căn lề bằng `&=`, `&\le`, v.v.
    - **Tuyệt đối CẤM nhảy xuống dòng khi chưa đến dấu bằng**: Cấm ngắt dòng giữa chừng tại các toán tử cộng, trừ ($+$, $-$) hay nhân, chia ($\times, \cdot$) làm rớt số hạng xuống dòng tiếp theo kiểu $\dots + R_2 \\ + R_3$. Mọi số hạng trong cùng một vế của biểu thức phải nằm liền mạch trên cùng một dòng.
    - **Cấm ngắt dòng ngay sau dấu bằng**: Tuyệt đối không viết `A = \\ B`, không ngắt dòng đẩy toàn bộ vế phải xuống dưới.
  - **Không lạm dụng `aligned` bẻ gãy công thức ngắn**:
    - Nếu một công thức hoặc phương trình vừa vặn trên một dòng (ví dụ: $R_{\mathrm{eq}} = R_1 + R_2 + R_3$ hay $\frac{1}{R_{\mathrm{eq}}} = \frac{1}{R_1} + \frac{1}{R_2} + \frac{1}{R_3}$ hay $R_{\mathrm{eq}} = \frac{R_1 R_2}{R_1 + R_2}$): Bắt buộc giữ nguyên trên 1 dòng đơn giản trong `$$...$$`. Tuyệt đối không bọc vào `\begin{aligned}` rồi ngắt vụn thành các dòng ngắn cụt cỡn ở giữa trang.
    - Chỉ dùng `\begin{aligned}` khi có chuỗi biến đổi nhiều bước qua dấu bằng hoặc hệ nhiều phương trình.
