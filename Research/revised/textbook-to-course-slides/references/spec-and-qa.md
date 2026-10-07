# Bản đặc tả, nguồn và nghiệm thu

Đọc trước khi khóa nội dung hoặc bàn giao. Dùng một bộ hồ sơ đủ cho phạm vi, có thể gộp bảng thay vì tạo hàng chục file.

## 1. Hồ sơ tối thiểu

Với bài mới hoặc khóa học:

- Cấu hình, hồ sơ người học và mục tiêu.
- Chỉ mục nguồn, sổ bao phủ và danh mục hình.
- Thuật ngữ / ký hiệu đã chọn và phụ thuộc cần học.
- Bản đặc tả slide cùng nội dung chính xác, hình, ghi chú và nguồn.
- Báo cáo kiểm tra, phần chưa kiểm chứng và trạng thái tiếp tục nếu còn bài sau.

Với sửa một đoạn nhỏ, giữ phạm vi đã được giao và ghi phần thay đổi; không dựng lại toàn bộ khóa học chỉ để đủ thủ tục.

ID nguồn ổn định trong lần xử lý: SRC-B01-C02-S03-U007. ID slide có thể dùng L01-S001 khi tạo lần đầu. Sau khi sửa, giữ ID cũ; slide chèn có thể dùng L01-S003a hoặc một ID duy nhất khác. Thứ tự hiển thị được lưu riêng trong mảng slides.

LECTURE_TITLE_FORMAT là mặc định tương thích bản cũ. Nếu cần Việt hóa toàn bộ hoặc đặt theo buổi / học phần, dùng yêu cầu của người dùng. Tiêu đề môn và bài học phải thể hiện đúng phạm vi.

## 2. Đặc tả JSON cho script đi kèm

Dùng JSON thuần UTF-8. Các trường chính:

~~~json
{
  "skill_version": "6.1.0",
  "config": {
    "target_language": "vi-VN",
    "delivery_mode": "live-with-study-companion",
    "assumed_term_ids": []
  },
  "lectures": [
    {"id": "L01", "title": "Lecture 1: Xác suất có điều kiện", "session_minutes": 45}
  ],
  "source_units": [
    {
      "id": "SRC-01",
      "location": "Tên tài liệu, mục 2.1, trang in 8 / PDF 10",
      "priority": "essential",
      "treatment": "core",
      "slide_ids": ["L01-S001"],
      "reason": ""
    }
  ],
  "source_visuals": [],
  "glossary": [
    {"id": "TERM-B", "canonical": "Biến cố B"}
  ],
  "slides": [
    {
      "id": "L01-S001",
      "lecture_id": "L01",
      "layer": "core",
      "role": "explanation",
      "title": "Biết B xảy ra làm thay đổi nhóm đang xét",
      "learning_goal": "Xác định đúng nhóm làm mẫu số.",
      "source_unit_ids": ["SRC-01"],
      "prerequisite_slide_ids": [],
      "introduced_term_ids": ["TERM-B"],
      "used_term_ids": ["TERM-B"],
      "body": [
        {"type": "text", "text": "Khi biết B đã xảy ra, ta chỉ xét các kết quả thuộc B.", "provenance": "source-adaptation", "source_unit_ids": ["SRC-01"]}
      ],
      "visuals": [],
      "speaker_notes": "Nhắc người học chỉ ra nhóm B trong bảng ở trang kế tiếp.",
      "next_bridge": "Trong nhóm B, phần nào cũng thuộc A?",
      "estimated_minutes": 1.0
    }
  ]
}
~~~

Ví dụ này minh họa cấu trúc, chưa phải một bài học hoàn chỉnh.

Với phiên bản 6.1, có thể lưu `teaching_plan` cho cụm nội dung và `study_text` cho đoạn note tự học của slide. `study_note_ref` trỏ file + mục được giao cho người học. Bản 6.0 có thể dùng tên cũ `teaching_contract`; đọc nó như kế hoạch giảng, không hiển thị tên trường cho sinh viên và không cần đổi key trong artifact cũ. Ba phần body, speaker_notes và study_text dùng giọng khác nhau nhưng giữ cùng giả thiết, dữ kiện và kết luận. Khi đổi một phần, đối chiếu hai phần còn lại. Những trường này là mở rộng tùy chọn; audit_spec.py hiện chỉ kiểm tra cấu trúc cũ, không xác nhận note đã được tạo hoặc liên kết đến mục thật. Kiểm tra file/địa chỉ và nội dung trước bàn giao. review_teaching_text.py rà cả study_text hoặc study_note dạng chuỗi nếu có.

Các giá trị chuẩn:

- priority: essential, important, supporting, optional.
- treatment: core, appendix, notes, omitted.
- layer: core, appendix.
- body.type: text, equation, code, table, quote. Nội dung thực tương ứng là text, latex, code, rows, text + attribution.
- Mỗi source_unit có location, treatment, slide_ids. Phần ngoài tuyến chính có reason. treatment notes có note_ref trỏ đến file + mục thật.
- Mỗi source_visual có id, location, treatment, slide_ids, reason nếu ở ngoài tuyến chính; khi dùng phải có original_asset_ref. treatment notes có note_ref.
- Mỗi visual trên slide có id, kind (source hoặc supplementary), claim và asset_ref. Hình nguồn có source_visual_id và preservation (original hoặc faithful-redraw). Bản vẽ lại có verification_note; hình supplementary có provenance.
- Mỗi body block có provenance là source-adaptation hoặc pedagogical-addition và có trường source_unit_ids. source-adaptation phải liên kết ít nhất một đơn vị nguồn đã gán cho slide. pedagogical-addition cần rationale; nếu nó minh họa một khái niệm nguồn, gắn source_unit_ids liên quan; chỉ để mảng rỗng khi nội dung thật sự độc lập với nguồn. Đơn vị nguồn của block phải là tập con của source_unit_ids ở slide.
- Nếu một block trộn ý được nguồn khẳng định với nhận định hoặc ví dụ mới, tách block để giữ ranh giới nguồn. Công thức suy ra từ nguồn gắn các đơn vị nguồn làm tiền đề; script vẫn không kiểm tra phép suy ra.
- Checkpoint metadata có provenance và source_unit_ids; pedagogical-addition cần provenance_rationale. Gắn đơn vị nguồn liên quan khi câu hỏi / lời giải kiểm tra kiến thức cụ thể; chỉ để mảng rỗng khi nhiệm vụ không kiểm tra nội dung nguồn.
- Lưu bổ sung loại dữ liệu, đơn vị, thông số crop, hình học, alt text và provenance nếu cần; không ép những trường không liên quan.

Với checkpoint, lưu prompt, answer, rationale, anticipated_error, feedback, answer_placement, provenance và source_unit_ids. Nếu provenance là pedagogical-addition, ghi provenance_rationale. Giá trị answer_placement là next_slide, after_response hoặc notes. Với next_slide, thêm answer_slide_id và hiển thị lời giải trên slide kế tiếp trong cùng tuyến và bài. Với notes, lưu lời giải vào speaker_notes hoặc tài liệu có note_ref. Trong self-study, đáp án chỉ ở ghi chú giảng viên bị coi là chưa cung cấp.

Phần answer lưu trong đặc tả là metadata. Renderer không tự đưa nó lên cùng trang câu hỏi. Câu hỏi tự học phải có tiêu chí đúng / sai hoặc rubric khi không có một đáp án duy nhất.

session_minutes có thể null. Khi có, estimated_minutes phải tính cả thời gian hoạt động, đọc hình và chờ câu trả lời. Báo quá tải theo tổng ước lượng, không theo số slide.

Không bịa vị trí nguồn hoặc file asset để qua script. Nếu chưa tìm / dựng được, để rõ trạng thái còn mở trong báo cáo và chưa bàn giao như sản phẩm hoàn tất.

## 3. Tính tái lập có phạm vi

Phân biệt:

1. **Tái lập đầu ra đã khóa:** cùng đặc tả, asset, renderer và font sẽ giúp tái tạo bản đã chọn.
2. **Đồng nhất các model khi soạn lần đầu:** skill một mình không bảo đảm cùng lời văn, chia bài hoặc lựa chọn minh họa.
3. **Đồng nhất byte / pixel:** còn phụ thuộc phiên bản công cụ, metadata, font, engine toán và môi trường.

Mặc định cho phép lựa chọn sư phạm có lý do rồi khóa bản chọn. Không coi mọi khác biệt giữa hai cách giảng đúng là lỗi.

Nếu người dùng cần strict, khóa cấu hình, thứ tự, nội dung, ví dụ, hình, layout và công cụ sau giai đoạn soạn. Đừng hứa strict từ một yêu cầu mơ hồ chưa có bản đặc tả chuẩn.

Lưu phiên bản, hash nguồn / đặc tả / asset nếu môi trường hỗ trợ. Script audit_spec.py cung cấp hash JSON chuẩn hóa của đặc tả; hash đó không chứng minh nội dung đúng hoặc output PDF giống nhau.

## 4. Kiểm tra tự động được gì?

Chạy từ thư mục skill hoặc dùng đường dẫn đầy đủ:

~~~text
python scripts/audit_spec.py course-spec.json
python scripts/audit_spec.py course-spec.json --asset-root path-to-course
~~~

Script dùng thư viện chuẩn Python. Nó kiểm tra:

- ID trùng, liên kết nguồn–slide sai hoặc không khớp hai chiều.
- Nội dung thiết yếu vắng khỏi tuyến chính.
- Nội dung / hình chuyển ra ngoài tuyến chính thiếu lý do hoặc địa chỉ ghi chú.
- Thuật ngữ được dùng trước khi ghi nhận giới thiệu, trừ danh sách đã biết.
- Provenance thiếu, đơn vị nguồn chưa tồn tại, hoặc block source-adaptation / bổ sung mâu thuẫn với map ở slide.
- Phụ thuộc slide về sau hoặc từ tuyến chính trỏ vào phụ lục.
- Checkpoint thiếu lời giải, lý do, phản hồi; vị trí đáp án không phù hợp tự học.
- Hình thiếu mục đích, asset, liên kết gốc; bản vẽ lại thiếu ghi chú đối chiếu.
- Trường nội dung không hợp lệ, bài thiếu ước lượng khi có thời lượng, tổng thời gian vượt buổi.
- Khi có asset-root: asset nội bộ thiếu hoặc nằm ngoài thư mục được chỉ định.

Các kiểm tra này dựa trên những gì người soạn khai báo. “introduced_term_ids” không chứng minh định nghĩa đã viết tốt. “verification_note” không chứng minh người soạn đã đối chiếu thật. Script không tự xác nhận sự tự nhiên, tính đúng kiến thức, nguồn OCR, quyền dùng hình hoặc chất lượng layout.

Exit code 0: không có lỗi cấu trúc được script phát hiện. Exit code 1: có lỗi cần sửa. Exit code 2: đầu vào không đọc được hoặc JSON / cấu trúc top-level không hợp lệ. Warnings còn lại phải được xem xét. Không đặt tên kết quả là “pedagogy passed”.

## 5. Kiểm tra thủ công theo bằng chứng

| Cửa kiểm tra | Việc làm | Bằng chứng cần giữ |
| --- | --- | --- |
| Nguồn và logic | Đối chiếu phát biểu, điều kiện, phép tính, chứng cứ và hình | Vị trí nguồn, phép tính độc lập khi cần, lỗi đã sửa |
| Người mới học | Theo từng bước với đúng kiến thức đầu vào | Chỗ thiếu cầu nối, lời giải hoặc nhãn và bản sửa |
| Biên và phản biện | Thử điều kiện biên, lập luận đối lập phù hợp | Trường hợp được thử, kết luận được giới hạn |
| Ngôn ngữ | Đọc lời giảng liên tục và cùng hình | Các câu yếu cùng nguyên nhân, ý được bảo vệ |
| Visual | Xem contact sheet và từng trang render | Phiên bản render, trang lỗi và ảnh kiểm tra |
| Bao phủ và bàn giao | So sánh sổ nguồn, file thật và tuyến học | Phần ở đâu, liên kết hoạt động, giới hạn còn lại |

Một người hoặc model có thể đổi góc nhìn để rà soát, nhưng không được mô tả các lượt tự rà là đánh giá độc lập. Nếu có đánh giá độc lập được phép, cung cấp yêu cầu và nguồn thật; ghi rõ ai / công cụ nào đã chạy và phạm vi.

Không yêu cầu công bố toàn bộ suy nghĩ nội bộ. Giữ quyết định ngắn, bằng chứng và lỗi có thể kiểm tra.

## 6. Mức độ lỗi và sửa theo nguyên nhân

- **Chặn:** sai kiến thức / nguồn, mất giả thiết, thiếu cầu nối thiết yếu, nguồn không khớp, chữ hoặc hình không đọc được. Sửa trước khi bàn giao.
- **Cần sửa:** câu khó đọc, bước giải thích dư hoặc thiếu, nhịp bố cục máy móc, màu dùng sai vai trò. Sửa phần bị ảnh hưởng và xem lại.
- **Lựa chọn:** một trong nhiều cách trình bày hợp lý. Dùng bối cảnh và ưu tiên người dùng; không biến thành lỗi chỉ vì khác mẫu.

Nguồn gắn cho cả block có thể chỉ ra đoạn sách liên quan, không khẳng định rằng từng chữ là trích dẫn. Chỉ ghi trích dẫn nguyên văn khi đó thực sự là câu trích; giữ nguyên chữ và attribution.

Ví dụ: nếu không hiểu mẫu số, thêm thao tác chọn nhóm và hình thể hiện nhóm đó. Đổi “chuẩn hóa” thành “điều chỉnh” mà vẫn thiếu thao tác không sửa được nguyên nhân.

Một lượt sửa có thể tác động tới slide sau: đổi thuật ngữ cần rà toàn cụm, tách slide cần sửa phụ thuộc và vị trí đáp án, đổi thang đồ thị cần đối chiếu những trang so sánh.

Sau các kiểm tra cần thiết, dừng khi các lỗi chặn đã hết và phần giới hạn được mô tả đúng. Nếu vẫn còn một vấn đề sau hai lượt sửa tập trung, đổi phương án ở phần đó hoặc báo rõ hạn chế; không lặp toàn bộ quy trình vô hạn.

## 7. Phiếu nghiệm thu ngắn

Ghi theo sự kiện thực:

~~~text
Phạm vi đã xử lý:
Người học và kiến thức đầu vào đã giả định:
Tuyến chính / tài liệu học / ghi chú:
Nguồn và phép tính đã đối chiếu:
Script đã chạy, exit code, errors / warnings:
Output đã render và trang đã xem:
Lỗi chặn còn mở:
Hạn chế chưa kiểm chứng:
~~~

Không dùng điểm phần trăm “hết AI slop” hoặc điểm chất lượng không có cách đo. Khi có sinh viên thật, thu câu trả lời và bài làm theo mục tiêu; đó mới là bằng chứng hiệu quả học tập.
