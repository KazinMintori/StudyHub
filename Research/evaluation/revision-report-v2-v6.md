# Hai skill giảng dạy: bản sửa ngày 07/10/2026

Đã tạo `textbook-passage-explainer` phiên bản **2.0.0** và `textbook-to-course-slides` phiên bản **6.0.0**. Bản gốc trong hai ZIP được giữ nguyên. Các bản mới là skill cùng công cụ hỗ trợ, chưa phải ứng dụng giảng dạy tự chạy hoặc một model đã được huấn luyện lại.

| Kết quả | File |
| --- | --- |
| Gói giải thích giáo trình và note | [textbook-passage-explainer-v2.zip](textbook-passage-explainer-v2.zip) |
| Gói slide bài giảng | [textbook-to-course-slides-v6.zip](textbook-to-course-slides-v6.zip) |
| Source skill giải thích/note | [SKILL.md](revised/textbook-passage-explainer/SKILL.md) |
| Source skill slide | [SKILL.md](revised/textbook-to-course-slides/SKILL.md) |
| Note mẫu sau khi sửa theo phản hồi mô phỏng | [06-revised-study-note.md](evaluation/notes-forward/06-revised-study-note.md) |
| Bài thử với ba giọng, 8 slide / 12 phút | [study-note.md](evaluation/slides-forward/study-note.md) |
| Đặc tả của bài thử | [course-spec.json](evaluation/slides-forward/course-spec.json) |

## Vấn đề được xử lý

Hai bản cũ đã có quy tắc tốt về nguồn, giả thiết, độ bao phủ và kiểm tra hình. Điểm yếu là “viết tự nhiên” vẫn chủ yếu được mô tả bằng nguyên tắc, chưa có nhiệm vụ riêng cho từng loại nội dung và chưa tách đủ rõ giọng slide, lời giảng và note. Skill giải thích cũng chủ yếu xử lý đoạn trong chat, chưa có chế độ note tự học rõ ràng.

Phản hồi đính kèm được dùng làm dữ liệu thiết kế: “gradient tại điểm hiện hành”, “chứng minh và vị trí dùng giả thiết”, câu ghép mô hình–điều kiện dừng–cập nhật–quy ước dấu, danh từ hóa và kết luận làm mất câu hỏi của người học. Mỗi lỗi được chuyển thành một cách sửa có điều kiện và một tiêu chí kiểm tra nghĩa. Không chỉ đổi từ gượng sang từ đồng nghĩa.

## Các thay đổi chính

**Hợp đồng cho từng đơn vị nội dung.** AI phải xác định câu hỏi cần trả lời, mục tiêu quan sát được, kiến thức đã biết, bước cần mở và các phần phải giữ. Có nhiệm vụ riêng cho định nghĩa, định lý, suy diễn, thuật toán, chứng cứ thực nghiệm, diễn giải văn bản và luyện tập. Một đơn vị có thể trải qua nhiều slide; một đoạn có thể cần nhiều nhiệm vụ. Đoạn ngắn không phải xuất hồ sơ nội bộ.

**Ba giọng từ cùng một nội dung.** Chữ trên slide giữ phát biểu và điều kiện; lời giảng dẫn qua chỗ vướng; note tự học chứa đủ lý do để đọc độc lập. Ghi chú riêng của giảng viên không thay note giao cho người học. Bản slide cho phép lưu `study_text`, `study_note_ref` và `teaching_contract`, đồng thời nêu rõ validator cũ chưa xác nhận các trường mở rộng này.

**Giả thiết tại đúng bước dùng.** Thay “tính lồi đảm bảo tối ưu” bằng bất đẳng thức mà tính lồi cho phép, rồi chỉ bước gradient bằng 0 làm số hạng tuyến tính biến mất. Giữ miền, lượng từ và giới hạn của phản ví dụ. Với thuật toán, phân biệt gradient, hướng cập nhật, độ dài bước và độ dời.

**Lượt sửa ngôn ngữ riêng.** `professor-voice.md` có ví dụ cùng ý trong lời giảng và note, bản sửa các cụm gượng và cách đọc thành tiếng theo đúng đầu ra. Câu ngắn, câu hỏi và khoảng dừng được dùng khi có nhiệm vụ; không rải khẩu ngữ để diễn giọng người. Thuật ngữ chuẩn và trích dẫn được bảo vệ.

**Note và phản hồi theo bằng chứng.** Skill giải thích thêm chế độ `study-note` và `interactive`. Khi người học sai, sửa bước sai đầu tiên, giữ phần họ đã làm đúng và đổi biểu diễn khi cần. Không ép Socratic khi họ yêu cầu lời giải trực tiếp; không ghi thành thạo chỉ vì họ nói “hiểu rồi”.

**Không tạo tiên quyết mới ngoài ý định.** Một lỗi trong lượt thử là thêm “affine”, ký hiệu chuẩn và chứng minh nhiều biến dù người học chỉ biết đạo hàm. Đã thêm hướng dẫn rà thuật ngữ phụ, ưu tiên ví dụ nhỏ trong nền đã biết và tình huống hồi quy B08/T22. Bản note sửa chuyển sang một biến rồi nối trở lại R^n, giữ kết luận nguồn.

## Cách tham khảo prompts.chat

Đã đọc kho tại commit `7d3f248962d1dca209d59e033524bcb86c2b26b8`, gồm các mục Math Teacher, Educational Content Creator, Academician, Socratic Method và các chương hướng dẫn prompt. Áp dụng:

- Vai trò, bối cảnh, nhiệm vụ, ràng buộc, định dạng và ví dụ vào hợp đồng nội dung. [Anatomy of Effective Prompt](https://github.com/f/prompts.chat/blob/7d3f248962d1dca209d59e033524bcb86c2b26b8/src/content/book/02-anatomy-of-effective-prompt.mdx).
- Ví dụ đầu vào–đầu ra để làm rõ giọng, thay vì chỉ yêu cầu “viết như người”. [Few-Shot Learning](https://github.com/f/prompts.chat/blob/7d3f248962d1dca209d59e033524bcb86c2b26b8/src/content/book/07-few-shot-learning.mdx).
- Tách đọc nguồn, thiết kế, soạn, sửa giọng, kiểm tra nghĩa và dựng; kiểm tra kết quả quan trọng giữa các lượt. [Prompt Chaining](https://github.com/f/prompts.chat/blob/7d3f248962d1dca209d59e033524bcb86c2b26b8/src/content/book/11-prompt-chaining.mdx).

Các prompt và ví dụ tiếng Việt trong gói được viết mới. Tham khảo prompting không được coi là bằng chứng khoa học về hiệu quả giảng dạy. Phần mở bước chuyên gia thường bỏ qua dựa thêm trên [CMU Teaching Principles](https://www.cmu.edu/teaching/principles/teaching.html); việc dùng ví dụ, biểu diễn và câu hỏi giải thích có tham khảo mức bằng chứng trong [IES Practice Guide](https://ies.ed.gov/ncee/wwc/PracticeGuide/1). Ví dụ tính lồi được đối chiếu với [Boyd & Vandenberghe](https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf), mục 3.1.3 và 4.2.3. Chi tiết ánh xạ và giới hạn nằm trong `references/prompt-research.md` của mỗi gói.

## Công cụ sử dụng được

Mỗi gói có hai script Python dùng thư viện chuẩn, không cần API hoặc mạng:

- `build_teaching_prompt.py`: nhận JSON của một đơn vị nguồn, kiểm tra trường cần thiết và tạo prompt có nhiệm vụ theo loại nội dung, dạng đầu ra và hướng dẫn giọng. Nó không tự hiểu sách hay gọi model.
- `review_teaching_text.py`: chỉ vị trí cụm gượng, câu có khả năng quá tải và mẫu mở câu lặp. Đọc được Markdown hoặc đặc tả slide, gồm `study_text`; không tự sửa hoặc đo “tính người”.

Gói slide giữ `audit_spec.py` hiện hữu để kiểm tra cấu trúc và các liên kết nguồn. Hai gói độc lập, có đủ reference riêng; không cần cài gói còn lại để đọc các hướng dẫn chung.

Ví dụ chạy từ thư mục một skill sau khi giải nén:

```text
python scripts/build_teaching_prompt.py references/prompt-input.example.json --output prompt.txt
python scripts/review_teaching_text.py note.md --output language-review.json
```

Trong phiên AI có skill, yêu cầu có thể là:

```text
Dùng $textbook-passage-explainer giảng đoạn nguồn này cho người đã biết đạo hàm, rồi viết note tự học. Chỉ rõ bước dùng từng giả thiết.

Dùng $textbook-to-course-slides tạo bài 45 phút từ phần nguồn này, có slide, lời giảng và note tự học. Giữ nguồn, ký hiệu và điều kiện nhất quán.
```

Đã thêm `agents/openai.yaml` vào mỗi gói với tên hiển thị, prompt gợi ý và khả năng chọn tự động. Chưa sao chép các bản này vào thư mục skill cá nhân; source đang ở `Research/revised` theo phạm vi yêu cầu.

## Kiểm tra thực sự đã chạy

| Phép kiểm | Kết quả và giới hạn |
| --- | --- |
| `quick_validate.py` trên hai skill | Cả hai hợp lệ. Chạy UTF-8; PyYAML chỉ phục vụ validator, nằm ngoài gói phân phối. |
| `verify_tools.py` | 10 bài kiểm tra đạt: 56 tổ hợp loại nội dung/dạng đầu ra trên hai gói; đầu vào sai; bảo toàn dữ liệu nguồn; Unicode; bỏ code/trích dẫn khi nhận diện được; CLI; reference; hồi quy nguồn/asset/ID/thời lượng. |
| Mẫu đặc tả cũ với asset thật | 0 lỗi, 0 cảnh báo. Các đột biến nguồn thiếu, asset thiếu, ID trùng và quá thời lượng được phát hiện. |
| Lượt soạn thử skill giải thích | Một agent nhận yêu cầu và nguồn, không được cho đáp án mong đợi: giải thích tính lồi + note, phân tích văn học và phản hồi mẫu số xác suất. Output thật được giữ trong `notes-forward`. |
| Lượt sửa theo phản hồi mô phỏng | Giảm thuật ngữ phụ và ví dụ nhiều biến; output mới lưu riêng, output cũ giữ nguyên. Đây là lượt sửa, không phải một thử nghiệm độc lập mới. |
| Lượt soạn thử skill slide | Một agent khác tạo 8 slide/12 phút ở mức đặc tả, lời giảng và note. Audit: 0 lỗi, 0 cảnh báo. Phép tính x₁=3/2, x₂=9/4 và trường hợp α=2 được kiểm tra bằng Fraction; các phần trong đặc tả và note được đối chiếu. |
| Rà dấu hiệu ngôn ngữ | Không có cảnh báo trên note sửa và đặc tả slide thử. Kết quả này không chứng minh tiếng Việt hay sư phạm đã đạt; lượt đọc thủ công vẫn cần. |
| ZIP phân phối | Kiểm tra CRC, danh sách file và hash từng file khớp source. Mỗi ZIP chứa một thư mục gốc skill; không chứa cache hay thư viện kiểm tra. |

[tool-validation.json](evaluation/tool-validation.json) lưu lệnh, exit code và output thực. [package-manifest.json](evaluation/package-manifest.json) lưu hash, file thêm/sửa và đối chiếu với hai ZIP gốc. Script kiểm tra có thể chạy lại trong `Research/evaluation`.

## Phần chưa được chứng minh

Chưa có sinh viên thật, bài kiểm tra chuyển giao hoặc dữ liệu trước/sau; không tuyên bố chất lượng giảng ngang một giáo sư trên mọi môn. Các lượt agent kiểm tra khả năng áp dụng hướng dẫn, không thay đánh giá trong lớp.

Bài slide thử được yêu cầu chỉ tạo đặc tả và note. Chưa render PDF/PPTX, chưa kiểm tra bố cục, font/glyph, overflow hay khả năng đọc trên bản chiếu. Những yêu cầu render và nhìn từng trang vẫn được giữ trong skill cho lần tạo bộ slide thật. Chưa chạy thử một giáo trình đầy đủ hoặc nhiều model khác nhau.

Thay đổi hoàn tất trong hai skill và vùng đánh giá; nội dung website StudyHub không được sửa. Kết quả hướng tới hành vi của người giảng giỏi: giải thích đúng, chỉ được lý do, thấy bước người học thiếu và sửa theo phản hồi. Những điểm này cần tiếp tục được đánh giá bằng bài làm thực của người học.
