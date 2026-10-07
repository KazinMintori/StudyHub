# Kiểm thử hành vi của bộ skill giảng dạy

Dùng khi sửa skill, đổi model hoặc kiểm tra một bài giảng mới có giữ được hành vi mong muốn không. Đây là bộ tình huống đánh giá; ghi rõ tình huống nào đã thực sự chạy, với output thật, nguồn, phiên bản skill và lỗi quan sát được. Không đối chiếu từng chữ với một “đáp án vàng”: output khác vẫn đạt nếu giữ bất biến, giải thích đúng và có nhiệm vụ học phù hợp.

Ba nhóm:

- **S01–S12**: hành vi riêng của StudyHub (trang bài giảng, catalog, Wiki, giọng trên site). Bắt đầu từ đây khi sửa `studyhub-lecture`.
- **T01–T27**: thiết kế bài, slide, hình, thuật ngữ (kế thừa textbook-to-course-slides 6.1).
- **B01–B14**: giảng một đoạn trong chat và phản hồi bài làm (kế thừa textbook-passage-explainer 2.1; dùng cho skill `textbook-passage-explainer`).

Phần kiểm tra tự động của script nằm ở `scripts/tests/test_tools.py`; chạy `python3 -I .claude/skills/studyhub-lecture/scripts/tests/test_tools.py` từ gốc repo.

## S. Tình huống StudyHub

| Mã | Yêu cầu / vật liệu | Hành vi cần thấy | Hành vi làm trượt |
| --- | --- | --- | --- |
| S01 | Soạn bài từ `raw_materials/<môn>/…` có một đoạn trích danh nhân trong nguồn nháp | Bỏ hoặc dẫn đúng nguồn câu nói; mở bài bằng câu hỏi của bài học | Giữ đoạn trích gán cho nhân vật mà không có nguồn; bịa năm, tên sách |
| S02 | Bài có định nghĩa, ví dụ, bẫy dễ nhầm và bài tập | `::: example` cho ví dụ có lời giải; `::: exercise` + `::: solution` gập; `::: warning` chỉ cho ngộ nhận cụ thể có ví dụ | Hộp “Bản chất”, “Bẫy thi cử cực kỳ phổ biến”; đáp án nằm cùng hộp với đề; lý do thiết yếu chỉ trong hộp gập |
| S03 | Thêm một bài mới cho môn có `parts` | Frontmatter khớp catalog; slug có trong `lessons` và `parts`; có slide `note` trỏ đúng; `check_lecture.mjs` 0 lỗi; `npm run ci:build` exit 0 | Quên `parts` (bài không có trong sidebar); đặt `ready` khi chưa có slide; viết H1 trong Notes |
| S04 | Bài dùng một khái niệm nền chưa có trong Wiki | Thêm đủ concepts + wikiGroups + wikiDetails + `docs/wiki/<id>.md`; chuỗi trong concepts là văn bản thuần có ví dụ và câu tự kiểm | Chỉ thêm id vào prerequisites; viết `$…$` trong concepts; alias quá chung làm gắn link khắp nơi |
| S05 | Notes nói “hội tụ khi 0 < η < 1 với f(x)=x²”; viết Slides | Slide giữ điều kiện cạnh kết luận, công thức Unicode | Slide rút thành “Gradient Descent luôn hội tụ”; LaTeX `\eta` lọt vào chuỗi slide |
| S06 | Ví dụ số trong Notes (ví dụ PageRank một vòng: A=3/8, B=C=D=5/24) | Số được tính lại bằng code trước khi ghi; tổng kiểm bằng 1 | Đột biến 5/24 → 1/4 không bị phát hiện vì chỉ “đọc lại” |
| S07 | Sửa (revise) một bài đã `ready` có người học đánh dấu tiến độ | Giữ slug, id thuật ngữ, địa chỉ mục cũ nếu có thể; báo phần đã đổi | Đổi slug hoặc id Wiki làm mất tiến độ và link ngược |
| S08 | Bài cho người mới biết đạo hàm; người soạn thêm “model soup”, “lifting”, ký hiệu chuẩn chưa dạy | Giải thích ngay, đưa vào prerequisites, hoặc bỏ | Thuật ngữ phụ tạo tiên quyết mới không được nhận ra |
| S09 | Chế độ review trên một bài hiện có | Báo theo mức chặn / cần sửa / lựa chọn, có file:dòng và cách sửa; không sửa file | Chấm điểm phần trăm; sửa luôn khi chưa được yêu cầu; gọi lựa chọn trình bày là lỗi |
| S10 | Bài thực hành Python/NumPy/pandas | Code trong bài chạy được; output in trong bài khớp output thật; nêu phiên bản thư viện khi hành vi phụ thuộc phiên bản | Output tự viết không chạy thử; dùng API đã bỏ |
| S11 | Nguồn PDF có trang OCR lỗi ký hiệu (“P(B) ? 0”) | Ghi chỗ mơ hồ, đối chiếu ảnh trang nếu có, không đoán | Giảng như chắc chắn ký tự là “>” |
| S12 | Một chương dài gấp ba một bài bình thường | Đề xuất tách bài theo điểm kết thúc nhiệm vụ học, nói rõ phần chuyển sang bài sau | Nén bằng cách xóa điều kiện, bước suy luận hoặc ví dụ |
| S13 | Notes dày thuật ngữ, người học muốn xem nhanh rồi mới quyết định mở Wiki | Thuật ngữ khó có `concepts` ngắn và `wikiDetails` sâu; bấm/tap mở ghi chú nhanh có ví dụ và nút sang Wiki; dùng được bằng bàn phím, Escape đóng, mobile không tràn màn hình | Nhấp thuật ngữ lập tức đẩy người học khỏi Notes; chỉ hoạt động khi hover; nhồi công thức dài vào tooltip; thêm mọi thuật ngữ Wiki vào prerequisites |

Bất biến chung cho mọi tình huống S: không bịa nguồn/trích dẫn/số liệu; mọi số đã tính lại; Notes tự học được mà không cần giảng viên; Slides không chứa khẳng định Notes không có.

### Đột biến tích hợp tự động

`scripts/tests/test_tools.py` dựng một repo thu nhỏ rồi cố tình làm hỏng để chắc `check_lecture.mjs` bắt được: frontmatter lệch catalog, prerequisite không có trong concepts/wikiGroups/wikiDetails/Wiki, bài `ready` không có slide, slug thiếu trong `parts`, hình không tồn tại, container không đóng, H1 trong Notes, LaTeX trong chuỗi slide hoặc concepts. Đột biến về kiến thức, giọng và hình vẫn cần người/agent đọc output thật.

## T. Thiết kế bài, slide, hình

| Mã | Yêu cầu / vật liệu | Hành vi cần thấy | Hành vi làm trượt |
| --- | --- | --- | --- |
| T01 | Người mới học xác suất có điều kiện, nguồn có P(B) > 0 | Xác định nhóm B, giải thích mẫu số, giữ điều kiện, một bài đọc bảng | Chỉ nêu công thức hoặc “chuẩn hóa giao” |
| T02 | Dạy bất đẳng thức và phép chia hai vế với biến x | Nêu dấu của x trước khi chia, trường hợp x = 0 và x < 0 khi cần | Chia mà không xét điều kiện |
| T03 | Kỳ vọng của biến ngẫu nhiên nhận -1 và 1 đồng xác suất | Tính E[X] = 0 và cho thấy kỳ vọng không nhất thiết là giá trị được nhận | Gọi 0 là giá trị thường gặp nhất |
| T04 | Dạy một hàm với “asset”, “support” hoặc từ quen có nghĩa chuyên môn | Dùng nghĩa theo môn và giải thích tại chỗ | Dịch theo nghĩa đời thường sai hoặc dùng English cho sang |
| T05 | Định lý, giả thiết và một chứng minh có bước quyết định | Giữ giả thiết, phân biệt trực giác với chứng minh, giải thích bước khó | “Dễ thấy” thay lập luận |
| T06 | Một đoạn văn có hai cách đọc với chứng cứ khác nhau | Cho thấy văn bản và bước nối chứng cứ tới mỗi cách đọc | Ép thành định lý / công thức hoặc dựng đối lập yếu |
| T07 | Hình nguồn nhiều bảng nhỏ, trục và legend; yêu cầu Việt hóa | Giữ các phần cần đọc, lưu nguồn, dịch / vẽ lại được đối chiếu | Crop bỏ legend, sửa dữ liệu hoặc thay bằng icon |
| T08 | Một buổi 45 phút và một chương nhiều ý khó | Tính thời gian hoạt động, ưu tiên mục tiêu, ghi phần học thêm / chia buổi | Gộp 100 slide rồi gọi là một buổi phù hợp |
| T09 | Sinh viên đã thành thạo phần tiên quyết, cần bài nâng cao | Giảm lời nhắc thừa, tập trung vấn đề mới | Giảng lại từ đầu theo nghi thức |
| T10 | Tài liệu tự học về một cơ chế cần nhiều bước | Có cầu nối và lời giải truy cập được, không phụ thuộc lời nói trong lớp | Ghi chú giảng viên chứa toàn bộ lý do |
| T11 | Hai đối tượng cần so sánh trên cùng thang | Hình cho thấy khác biệt, nhãn và thang rõ, không chỉ dựa vào màu | Hai hình khác thang không báo hoặc ba thẻ giống nhau |
| T12 | Người dùng yêu cầu giữ văn phong sinh động và dùng dấu câu hợp lý | Giữ ẩn dụ có giới hạn, câu đủ nghĩa, tránh khẩu hiệu | Xóa mọi câu hỏi / dấu câu hoặc thêm khẩu hiệu mới |
| T13 | Chèn một slide và chuyển vị trí đáp án trong đặc tả | Giữ ID, cập nhật liên kết và trang lời giải | Hash đổi được gọi là lỗi hoặc đáp án trỏ trang cũ |
| T14 | Không có renderer trong môi trường | Tạo đặc tả và báo phần chưa render / chưa kiểm chứng | Tuyên bố đã QA thị giác |
| T15 | Sơ đồ hình vuông có nhãn cạnh a/b và đường chỉ dẫn | Mỗi nhãn nối đúng cạnh bằng đường đo hoặc dấu ngoặc nhìn rõ trên hình đã render | Nhãn nằm trong vùng tô, leader dừng giữa hình, hoặc người xem có thể gán cho cạnh khác |
| T16 | Một paragraph vừa diễn giải câu nguồn vừa thêm giả định của giảng viên | Tách ranh giới, gắn nguồn cho phần diễn giải và lý do sư phạm cho phần thêm | Gắn cả paragraph vào ID của sách rồi gọi toàn bộ nội dung là từ nguồn |

### Ví dụ kiểm thử hoàn chỉnh: xác suất có điều kiện

Đoạn nguồn thử nghiệm sau được tự viết để tránh phụ thuộc giáo trình chưa cung cấp:

> Với P(B) > 0, xác suất có điều kiện được định nghĩa bởi P(A|B) = P(A ∩ B) / P(B). Khi đã biết B xảy ra, ta giới hạn nhóm kết quả được xét vào B. Trong một nhóm 100 người, có 40 người tham gia câu lạc bộ B. Trong số 40 người đó, có 10 người cũng thuộc nhóm A.

Yêu cầu: viết và dựng một cụm slide tiếng Việt cho sinh viên đã biết tỉ lệ, chưa học xác suất có điều kiện. Giúp họ giải thích mẫu số và tính kết quả. Có một kiểm tra ngộ nhận, cho người học suy nghĩ trước đáp án.

Các bất biến cần giữ:

- P(B) > 0.
- 10 người thuộc cả A và B.
- Trong ví dụ, P(A|B) = 10/40 = 0,25; không phải 10/100.
- Không kết luận P(A) từ các dữ kiện trên.
- Hình phải phân biệt nhóm 100 và nhóm 40; không vẽ diện tích ngẫu nhiên như dữ liệu thật.
- Không thêm độc lập giữa A và B.

Một tuyến mẫu phù hợp: thấy bảng 100 người → biết điều kiện chọn nhóm 40 → tính phần 10 trong nhóm 40 → nối với công thức → sửa lỗi dùng 100 làm mẫu số → lời giải.

Đây là một phương án. Một output khác vẫn đạt nếu giữ bất biến, giải thích đúng và có nhiệm vụ phù hợp. Không đối chiếu từng chữ với “đáp án vàng”.

[sample-course-spec.json](sample-course-spec.json) minh họa đặc tả hợp lệ cho tuyến này, với dữ liệu giả định và các hình SVG đi kèm. Nó là vật liệu kiểm thử, không phải một khóa học đã nghiệm thu trên sinh viên.

### Thử cố tình làm hỏng (deck)

Sao chép mẫu vào thư mục tạm rồi sửa từng lỗi riêng:

1. Bỏ điều kiện P(B) > 0 khỏi lời giảng: kiểm tra nội dung thủ công phải tìm ra.
2. Dùng mẫu số 100: kiểm tra tính đúng phải tìm ra.
3. Chuyển định nghĩa thiết yếu hoàn toàn sang phụ lục: script phải báo.
4. Cho TERM-CONDITIONAL xuất hiện trước slide giới thiệu: script phải báo.
5. Bỏ lý do đáp án hoặc link hình: script phải báo.
6. Đổi hình để số người / tập bị sai, vẫn giữ trường claim đúng: script có thể không báo; QA hình phải tìm ra.
7. Tạo chữ 10 pt trong hình SVG: kiểm tra hình phải tìm ra dù mọi ID hợp lệ.
8. Dùng từ ngữ trừu tượng khó hiểu nhưng không sai trường dữ liệu: kiểm tra tiếng Việt phải tìm ra.

Chạy các đột biến cấu trúc có thể tự động, còn các đột biến kiến thức và hình thức cần kiểm tra output thật. Không gộp chúng thành một điểm phần trăm.

### Cách đánh giá hai phiên bản skill

Giữ cùng yêu cầu, nguồn, người học, thời lượng và công cụ. Lưu output mỗi phiên bản. Đối chiếu:

- Lỗi kiến thức và nguồn.
- Số và vị trí bước nhảy cần thiết.
- Nhiệm vụ học cùng chất lượng phản hồi.
- Câu khó đọc còn tồn tại.
- Hình không biểu diễn đúng ý hoặc khó đọc.
- Việc bàn giao và báo giới hạn có trung thực không.

Nếu có người học thật, so sánh câu trả lời giải thích và khả năng vận dụng trong tình huống mới. Ghi rõ nhóm, nhiệm vụ và giới hạn khảo sát; cảm giác “đẹp hơn” chưa đủ.

Đánh giá độc lập cần output không bị dẫn dắt bởi kết luận của người soạn. Nếu chỉ tự rà, gọi đúng là tự rà. Khi một lỗi mới xuất hiện, sửa quy tắc liên quan và thêm tình huống hồi quy; không thêm lệnh cấm rộng cho mọi bài.

### Hồi quy phiên bản 6

- **T17 / Giả thiết tại bước dùng:** dùng nguồn tự viết về f: R^n -> R khả vi, lồi và bất đẳng thức bậc nhất. Tạo cụm slide, lời giảng và note cho người biết đạo hàm. Đầu ra phải chỉ đúng bước dùng tính lồi và gradient bằng 0; không thay chứng minh bằng câu “tính lồi đảm bảo”.
- **T18 / Cùng ý, ba giọng:** note phải đọc độc lập, slide giữ điều kiện cạnh kết luận, lời giảng mở câu hỏi của người học. Chỉ đổi bố cục của cùng một paragraph dài sang ba file là chưa đạt.
- **T19 / Không nối sai hai nội dung:** nguồn gồm gradient descent không ràng buộc và nhân tử của ràng buộc đẳng thức. Không ghép thành phương pháp có ràng buộc mới. Phân biệt gradient, hướng và độ dời; không hứa hội tụ với mọi bước dương.
- **T20 / Kế hoạch giảng theo môn:** với tư liệu có hai cách đọc, chọn nhiệm vụ interpretation và dùng chứng cứ. Không thêm gradient, định lý hoặc phản ví dụ chỉ vì các ví dụ giọng trong gói có toán.
- **T21 / Công cụ có giới hạn:** prompt compiler chỉ khởi tạo, language review chỉ gợi ý, audit_spec chỉ cấu trúc. Không báo “professor-quality passed” vì các script trả 0.
- **T22 / Thuật ngữ phụ:** người học chỉ biết đạo hàm. Nếu ví dụ mới dùng “affine”, chuẩn hoặc phép toán chưa được dạy, giải thích nghĩa cần dùng hoặc chọn ví dụ đơn giản hơn. Note không mở thêm một chứng minh phụ khiến câu hỏi chính bị mất; giảm tải vẫn giữ miền và lượng từ của kết luận nguồn.

Đọc professor-voice.md, content-prompts.md và teaching-review.md để biết hành vi mới. Các tình huống này chưa được mặc định coi là đã chạy.

### Hồi quy thuật ngữ phiên bản 6.1

- **T23:** nguồn contraction mapping và tensor contraction ở hai cụm. Chọn nghĩa theo cụm/lĩnh vực, giữ hệ số chung q<1 của ánh xạ co và chỉ số tổng của tensor; không biến cả hai thành một “phép co khoảng cách”.
- **T23b:** minh họa trace phải có cặp chỉ số trên/dưới phù hợp hoặc metric/quy ước đã nêu. Không dùng ma trận số như bằng chứng tự động rằng mọi phép co của tensor hình học đều giữ nghĩa.
- **T24:** slide feasible point/set phải giữ “khả thi”, thỏa mọi ràng buộc và chưa khẳng định tối ưu. Không thay thuật ngữ chuẩn chỉ để nghe đời thường.
- **T25:** slide và note về equality multiplier phải nhất quán việc ν=0 được phép về dấu. Lời giảng “âm hoặc dương” không đủ nếu đang mô tả đầy đủ miền.
- **T26:** active tại x không buộc multiplier>0; dùng cùng glossary ở mọi tầng. “Bước dương đủ nhỏ” không bị renderer hoặc editor rút thành “mọi bước dương”.
- **T27:** prompt compiler phải dùng dữ liệu tra cứu cục bộ, không tự thay bản nguồn. Domain mâu thuẫn/còn mơ hồ được báo, không giấu bằng một lựa chọn. Key cũ teaching_contract vẫn đọc được; tên nội bộ không xuất hiện trên màn hình học.

## B. Giảng một đoạn và phản hồi bài làm

### B01 — Điểm dừng và tính lồi

Nguồn tự viết: “Cho f: R^n -> R khả vi và lồi. Với mọi x,y, f(y) >= f(x) + grad f(x)^T(y-x). Nếu grad f(x*) = 0, x* là cực tiểu toàn cục.”

Yêu cầu: giảng trong chat cho người biết đạo hàm nhưng chưa học tối ưu lồi. Giữ miền và tính khả vi; chỉ đúng bất đẳng thức dùng tính lồi và bước dùng gradient bằng 0. Nếu thêm -x^2, tính đạo hàm và chỉ kết luận đúng phạm vi phản ví dụ. Không thay lập luận bằng “tính lồi đảm bảo”.

### B02 — Chuyển thành note

Dùng cùng nguồn B01, yêu cầu note Markdown tự học. Note phải có nghĩa ký hiệu, lập luận đầy đủ và đọc được độc lập; không dùng “ở chỗ này” với đối tượng không tồn tại. So slide/note nếu có cặp, không nhét một kiểu giọng vào cả hai.

### B03 — Thuật toán và quy ước dấu

Nguồn tự viết: “Gradient descent dùng x_(k+1)=x_k-alpha_k grad f(x_k), alpha_k>0. Với ràng buộc đẳng thức h(x)=0, L(x,nu)=f(x)+nu h(x), nu không bị giới hạn dấu.”

Yêu cầu: giải thích hai đoạn, không tự nối thành thuật toán tối ưu có ràng buộc. Nếu dùng f(x)=(x-3)^2, x_0=0, alpha=1/4, bước đầu phải ra x_1=1.5. Phân biệt gradient, hướng -gradient và độ dời. Không hứa giảm/hội tụ với mọi alpha>0; không coi gradient của L bằng 0 là đủ tối ưu nếu thiếu điều kiện.

### B04 — Phản hồi có bằng chứng

Người học viết: “10 trong 40 người thuộc nhóm B cũng thuộc A, nên P(A|B)=10/100.” Phản hồi phải tìm sai mẫu số và giải thích điều kiện chọn nhóm. Không kết luận họ không biết chia; không gọi họ thành thạo chỉ vì sau đó nói “hiểu rồi”. Nếu họ muốn lời giải trực tiếp, không bắt trả lời thêm mới cho đáp án.

### B05 — Diễn giải văn bản

Nguồn tự viết: “Nhân vật khép cửa rồi đặt lá thư chưa mở dưới ngọn đèn. Đoạn văn không cho biết nội dung thư.” Yêu cầu giảng ý nghĩa chi tiết. Phải dùng chứng cứ và nêu mức chắc chắn; không bịa nội dung thư hoặc ý tác giả. Không ép định lý, công thức và phản ví dụ lên văn học.

### B06 — Nguồn thiếu / mơ hồ

Nguồn: “Chia hai vế cho x để suy ra …”, không cho dấu của x. Yêu cầu giải thích phép chia bất đẳng thức. Phải nói điều kiện thiếu, xét dấu khi cần; không đoán x>0. Trong OCR “P(B) ? 0”, không mặc định ký tự ? là > rồi ghi như nguồn chắc chắn.

### B07 — Biên tập giọng có bảo toàn nghĩa

Yêu cầu sửa câu “Bài 04 áp dụng thao tác lập mô hình và giải điều kiện dừng để tạo bước đi; phần đẳng thức dùng nu hoặc eta tự do dấu.” Nguồn không xác định bước cập nhật. Sửa giọng phải tách nhiệm vụ và giữ quy ước dấu; không khẳng định giải điều kiện dừng tự tạo hướng cập nhật. Nêu chỗ cần ngữ cảnh thay vì sửa câu gượng thành một câu tự nhiên nhưng sai.

Đạt khi không còn lỗi nghĩa/nguồn hoặc bước nối thiết yếu, giọng đúng đầu ra và phần chưa kiểm chứng được ghi đúng. Kết quả thử bằng model chưa chứng minh người học thật hiểu.

### B08 — Thuật ngữ phụ và sửa sau phản hồi

Người học chỉ biết đạo hàm. Bản giải thích thêm “hàm affine”, ký hiệu chuẩn và chứng minh ví dụ nhiều biến khiến họ phải học thêm để hiểu kết luận. Khi họ phản hồi điều đó, giảm phần phụ, dùng ví dụ một biến và nối rõ về ký hiệu tổng quát. Giữ miền R^n và lượng từ mọi y; không biến việc giảm tải thành xóa nội dung nguồn. Đây là tình huống hồi quy từ một output soạn thử, chưa phải dữ liệu lớp học.

### B09–B14 — Nghĩa chuyên ngành và bản dịch

- **B09:** nguồn EN cho T:X->X và d(Tx,Ty)≤q d(x,y) với 0≤q<1. Dùng “ánh xạ co” theo môn, giữ cùng q/mọi cặp điểm; không đổi q<1 thành q≤1. Nếu tuyên bố tồn tại điểm bất động, kiểm tra thêm các giả thiết.
- **B10:** nguồn tensor contraction có chỉ số ghép. Dùng “phép co tensor”, không thêm tính chất giảm khoảng cách. Từ contraction đứng riêng không có lĩnh vực thì giữ các nghĩa có điều kiện hoặc hỏi đúng thông tin thiếu.
- **B10b:** ví dụ trace phải nêu cặp chỉ số hợp lệ, chẳng hạn tổng A^i_i của tensor (1,1), hoặc metric/cấu trúc tương ứng. Không gọi tổng A_ii của tensor covariant tùy ý là bất biến mà chưa có điều kiện. Đây là hồi quy từ output soạn thử.
- **B11:** nguồn feasible point. Giữ “điểm khả thi”, miền và mọi ràng buộc; không đổi thành tối ưu hoặc loại từ “khả thi” để viết đời thường.
- **B12:** equality multiplier unrestricted in sign. Bản Việt phải giữ khả năng bằng 0, không áp điều kiện của nhân tử bất đẳng thức hoặc gọi giá trị được phép là nghiệm đã tìm được.
- **B13:** active constraint tại một điểm với g_i(x)=0. Không suy multiplier phải dương/khác 0; tên gọi ưu tiên glossary của môn. Hợp đồng trong câu về thỏa thuận không bị sửa thành ánh xạ co.
- **B14:** ∇f(x)^T d<0 và “sufficiently small positive steps”. Giữ “đủ nhỏ”, không giảng thành mọi bước dương. Sau khi sửa lời văn phải rà lại dấu, lượng từ và miền.

Tập ví dụ JSONL phục vụ prompting không phải đáp án vàng cho các bài kiểm tra. Đổi ký hiệu, ví dụ và cấu trúc câu khi đánh giá; không truy xuất bản Việt của chính câu kiểm tra.
