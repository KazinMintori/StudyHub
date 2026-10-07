# Hoàn thiện hai skill: tầng thuật ngữ EN–VI

Cập nhật ngày **07/10/2026** theo phần góp ý mới. Source hiện tại ở `Research/revised`; gói mới là **textbook-passage-explainer 2.1.0** và **textbook-to-course-slides 6.1.0**. Các ZIP gốc, v2/v6 và output thử trước được giữ nguyên để đối chiếu.

| Tài nguyên | Mở / tải |
| --- | --- |
| Skill giải thích và note mới nhất | [textbook-passage-explainer-v2.1.zip](textbook-passage-explainer-v2.1.zip) |
| Skill slide mới nhất | [textbook-to-course-slides-v6.1.zip](textbook-to-course-slides-v6.1.zip) |
| Source skill note | [SKILL.md](revised/textbook-passage-explainer/SKILL.md) |
| Source skill slide | [SKILL.md](revised/textbook-to-course-slides/SKILL.md) |
| Căn cứ thuật ngữ và giới hạn | [terminology-research.md](revised/textbook-passage-explainer/references/terminology-research.md) |
| Bộ nhớ thuật ngữ | [terminology-memory.json](revised/textbook-passage-explainer/references/terminology-memory.json) |
| Ví dụ tương phản tự viết | [translation-examples.jsonl](revised/textbook-passage-explainer/references/translation-examples.jsonl) |
| Kết quả giảng thử | [checks-and-limits.md](evaluation/terminology-forward/checks-and-limits.md) |

## Nội dung đã tích hợp

Hai skill giữ cải tiến từ lượt trước: prompt riêng cho từng loại nội dung, chỉ đúng bước dùng giả thiết, tách chữ slide–lời giảng–note và phản hồi theo bài làm. Phần mới xử lý cách dịch đúng từ điển nhưng sai nghĩa chuyên ngành.

Đã thêm bước **hiểu phát biểu → chọn thuật ngữ theo lĩnh vực → viết câu kỹ thuật → chuyển sang lời giảng → so lại nghĩa**. Lượt sửa giọng và lượt kiểm tra nghĩa được tách rõ. Một câu trôi chảy không đủ để xác nhận không mất điều kiện, lượng từ hoặc dấu.

Đã đổi nhãn nội bộ gượng “hợp đồng nội dung” thành “yêu cầu cho phần nội dung” hoặc “kế hoạch giảng”. Artifact mới dùng `teaching_plan`; key `teaching_contract` của bản cũ vẫn được đọc như metadata, không phải nhãn xuất hiện trong bài học. Đổi tên nội bộ khác với sửa contraction mapping: trong lý thuyết điểm bất động, từ đó chỉ ánh xạ co. “Hợp đồng” trong câu về ký kết vẫn được giữ đúng nghĩa.

## Bộ nhớ thuật ngữ và dữ liệu ví dụ

Có **15 mục khái niệm** ở ba lĩnh vực `optimization`, `fixed-point`, `tensor-algebra`, và **10 ví dụ tự viết** theo ba mức: thuật ngữ, câu, mạch giảng. Mỗi mục lưu cách gọi được chọn, biến thể, nghĩa phải giữ, lời giảng mẫu và nguồn/trạng thái kiểm chứng. Không chỉ lưu một cặp từ EN–VI.

Ví dụ lưu `literal_bad`, `technical_vi`, `lecture_vi`, nguyên nhân cần sửa và các phần phải giữ. Đây không phải corpus thu từ giảng viên hoặc dữ liệu đã dùng fine-tune. [training-and-evaluation.md](revised/textbook-passage-explainer/references/training-and-evaluation.md) hướng dẫn thu corpus có nguồn, tách tập kiểm tra, đánh giá nghĩa trước giọng và chuyển định dạng khi có yêu cầu huấn luyện thật.

Các cách gọi “ánh xạ co”, “điểm/tập/miền khả thi” và “phép co tensor” có chứng cứ dùng trong nguồn học thuật tiếng Việt. [Bài báo HCMUE](https://journal.hcmue.edu.vn/index.php/hcmuejos/article/view/3961), [bài báo Đại học Cần Thơ](https://ctujsvn.ctu.edu.vn/index.php/ctujsvn/article/download/4457/4174/9846), [đề cương TN545](https://cns.ctu.edu.vn/images/upload/daotao/decuong/TN545.pdf).

Các cách diễn đạt do dự án chọn, như “gradient tại x_k” hoặc tên active constraint, được phân biệt với chứng cứ dùng từ đã xem. Tên của giáo trình/người dùng được ưu tiên khi phù hợp khái niệm. Không gọi một cách dịch là chuẩn duy nhất của Việt Nam từ một nguồn.

## Các hiệu chỉnh về nghĩa

- `free in sign` bao gồm **số 0**. Khi giải thích đầy đủ miền, viết “âm, bằng 0 hoặc dương”. Được phép về dấu chưa có nghĩa một giá trị là nhân tử tại nghiệm.
- `contraction mapping` khác `tensor contraction`. Ánh xạ co giữ cùng một hệ số q với **0 ≤ q < 1** cho mọi cặp điểm; phép co tensor giữ chỉ số và miền tổng.
- `feasible` được diễn đạt bằng “khả thi” trong tối ưu; phải thỏa **mọi** ràng buộc, chưa có nghĩa tối ưu.
- `active constraint` là đẳng thức tại điểm đang xét, không buộc nhân tử dương/khác 0. Tên gọi theo glossary môn.
- `descent direction` và “sufficiently small positive steps” phải giữ “đủ nhỏ”, không thành mọi bước dương. Điều kiện dừng không tự tạo hướng cập nhật nếu chưa có mô hình bài toán con.
- Ví dụ tensor mới phải nêu loại chỉ số/cấu trúc. Lượt thử chọn đúng thuật ngữ nhưng ví dụ trace chưa nêu loại tensor; đã bổ sung quy tắc dùng cặp chỉ số trên/dưới phù hợp, chẳng hạn A^i_j, hoặc metric đã cho. Nguồn kỹ thuật: [Differential Geometry, mục 2.6](https://math.berkeley.edu/~ltomczak/notes/Mich2022/DG_Notes.pdf), [Knill, Tensor Analysis](https://people.math.harvard.edu/~knill/teaching/math109_1995/geometry.pdf).

## Công cụ đã nối vào prompt

`build_teaching_prompt.py` hiện tự gọi **retrieve_terminology.py** để lấy vài mục và ví dụ liên quan. Tra cứu ưu tiên cụm dài trước khi lọc domain: “tensor contraction” không bị rút còn “contraction” rồi áp nghĩa ánh xạ co. Từ đứng riêng có nhiều nghĩa được giữ ở trạng thái cần ngữ cảnh; domain mâu thuẫn được báo. Nếu không có domain, ứng viên tìm thấy vẫn cần được rà theo môn.

Đây là tra cứu cụm cục bộ bằng Python thư viện chuẩn, không cần mạng hay khóa API. Nó không tự dịch, không thay bản nguồn, không có embedding và không chứng nhận tương đương nghĩa. Script loại ví dụ có câu nguồn trùng chính xác; chia tập theo khái niệm/nguồn vẫn cần để tránh rò rỉ các biến thể tương đương.

`review_teaching_text.py` thêm cảnh báo theo ngữ cảnh cho “ánh xạ hợp đồng”, “hợp đồng tensor”, “biến miễn phí”, “điều kiện tính dừng” và nhãn nội bộ gượng. Không cấm từ “hợp đồng” nói chung hoặc tên ràng buộc đã được giáo trình định nghĩa.

Chạy từ thư mục skill sau khi giải nén:

```text
python scripts/retrieve_terminology.py --input source.txt --domain optimization --output terms.json
python scripts/build_teaching_prompt.py references/prompt-input.example.json --output prompt.txt
python scripts/review_teaching_text.py note.md --output language-review.json
```

Thiếu Python thì dùng hướng dẫn và tra JSON trực tiếp. Hai gói độc lập, mỗi gói chứa đủ reference/script. Chưa cài bản mới vào thư mục skill cá nhân; source và ZIP nằm trong Research theo phạm vi yêu cầu.

## Kiểm tra thực sự đã chạy

- **17 bài kiểm tra tự động đạt**, gồm các kiểm tra cũ và kiểm tra mới về hai nghĩa contraction, cụm dài/nhỏ, domain sai/thiếu, Unicode, tránh sửa contract của thỏa thuận, loại ví dụ trùng câu nguồn và nối tra cứu vào compiler.
- **Hai skill qua quick_validate.py.** Compiler hai gói chạy được; mẫu đặc tả slide với asset vẫn hợp lệ. [Lệnh và kết quả](evaluation/tool-validation.json) lưu exit code và output thực.
- **Một lượt soạn độc lập** nhận skill và sáu yêu cầu mới, không được cho đáp án mong đợi. [Output A–F](evaluation/terminology-forward/checks-and-limits.md) giữ hệ số co, giải điểm bất động, tính khả thi, số 0, nhân tử của ràng buộc chặt và nghĩa chưa xác định của contraction. Ví dụ tensor được rà và [sửa riêng sau review](evaluation/terminology-forward/B-revised.md), giữ bản đầu.
- ZIP mới được kiểm tra CRC, danh sách và hash từng file khớp source. [Manifest](evaluation/package-manifest-v2.1-v6.1.json) ghi nội dung gói; không chứa cache hoặc thư viện phục vụ validator.

Các yêu cầu render và nhìn từng trang được giữ trong skill slide. Đợt này tập trung nghiên cứu và tích hợp thuật ngữ, chưa tạo deck mới để QA hình thức. Chưa có dữ liệu sinh viên thật hoặc training job; không tuyên bố bộ ví dụ nhỏ đã làm model đạt chất lượng giáo sư. Nội dung website StudyHub không được sửa.
