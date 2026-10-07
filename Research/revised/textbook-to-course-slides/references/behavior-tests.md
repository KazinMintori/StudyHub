# Kiểm thử hành vi: skill có sửa được lỗi thực tế không?

Dùng khi sửa skill, đổi model hoặc chọn renderer. Đây là bộ tình huống đánh giá, không phải tuyên bố chúng đã được một model khác chạy.

Một lượt kiểm thử nên có yêu cầu, đoạn nguồn đủ, kiến thức đầu vào, output thực và lỗi quan sát được. Có thể chạy trong thư mục tạm. Không cần tạo cả khóa học để kiểm tra một lỗi cục bộ.

## 1. Các tình huống hồi quy

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

## 2. Ví dụ kiểm thử hoàn chỉnh: xác suất có điều kiện

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

## 3. Thử cố tình làm hỏng

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

## 4. Cách đánh giá hai phiên bản skill

Giữ cùng yêu cầu, nguồn, người học, thời lượng và công cụ. Lưu output mỗi phiên bản. Đối chiếu:

- Lỗi kiến thức và nguồn.
- Số và vị trí bước nhảy cần thiết.
- Nhiệm vụ học cùng chất lượng phản hồi.
- Câu khó đọc còn tồn tại.
- Hình không biểu diễn đúng ý hoặc khó đọc.
- Việc bàn giao và báo giới hạn có trung thực không.

Nếu có người học thật, so sánh câu trả lời giải thích và khả năng vận dụng trong tình huống mới. Ghi rõ nhóm, nhiệm vụ và giới hạn khảo sát; cảm giác “đẹp hơn” chưa đủ.

Đánh giá độc lập cần output không bị dẫn dắt bởi kết luận của người soạn. Nếu chỉ tự rà, gọi đúng là tự rà. Khi một lỗi mới xuất hiện, sửa quy tắc liên quan và thêm tình huống hồi quy; không thêm lệnh cấm rộng cho mọi bài.

## 5. Hồi quy phiên bản 6

- **T17 / Giả thiết tại bước dùng:** dùng nguồn tự viết về f: R^n -> R khả vi, lồi và bất đẳng thức bậc nhất. Tạo cụm slide, lời giảng và note cho người biết đạo hàm. Đầu ra phải chỉ đúng bước dùng tính lồi và gradient bằng 0; không thay chứng minh bằng câu “tính lồi đảm bảo”.
- **T18 / Cùng ý, ba giọng:** note phải đọc độc lập, slide giữ điều kiện cạnh kết luận, lời giảng mở câu hỏi của người học. Chỉ đổi bố cục của cùng một paragraph dài sang ba file là chưa đạt.
- **T19 / Không nối sai hai nội dung:** nguồn gồm gradient descent không ràng buộc và nhân tử của ràng buộc đẳng thức. Không ghép thành phương pháp có ràng buộc mới. Phân biệt gradient, hướng và độ dời; không hứa hội tụ với mọi bước dương.
- **T20 / Hợp đồng theo môn:** với tư liệu có hai cách đọc, chọn nhiệm vụ interpretation và dùng chứng cứ. Không thêm gradient, định lý hoặc phản ví dụ chỉ vì các ví dụ giọng trong gói có toán.
- **T21 / Công cụ có giới hạn:** prompt compiler chỉ khởi tạo, language review chỉ gợi ý, audit_spec chỉ cấu trúc. Không báo “professor-quality passed” vì các script trả 0.
- **T22 / Thuật ngữ phụ:** người học chỉ biết đạo hàm. Nếu ví dụ mới dùng “affine”, chuẩn hoặc phép toán chưa được dạy, giải thích nghĩa cần dùng hoặc chọn ví dụ đơn giản hơn. Note không mở thêm một chứng minh phụ khiến câu hỏi chính bị mất; giảm tải vẫn giữ miền và lượng từ của kết luận nguồn.

Đọc professor-voice.md, content-prompts.md và teaching-review.md để biết hành vi mới. Các tình huống này chưa được mặc định coi là đã chạy.

## 6. Hồi quy thuật ngữ phiên bản 6.1

- **T23:** nguồn contraction mapping và tensor contraction ở hai cụm. Chọn nghĩa theo cụm/lĩnh vực, giữ hệ số chung q<1 của ánh xạ co và chỉ số tổng của tensor; không biến cả hai thành một “phép co khoảng cách”.
- **T23b:** minh họa trace phải có cặp chỉ số trên/dưới phù hợp hoặc metric/quy ước đã nêu. Không dùng ma trận số như bằng chứng tự động rằng mọi phép co của tensor hình học đều giữ nghĩa.
- **T24:** slide feasible point/set phải giữ “khả thi”, thỏa mọi ràng buộc và chưa khẳng định tối ưu. Không thay thuật ngữ chuẩn chỉ để nghe đời thường.
- **T25:** slide và note về equality multiplier phải nhất quán việc ν=0 được phép về dấu. Lời giảng “âm hoặc dương” không đủ nếu đang mô tả đầy đủ miền.
- **T26:** active tại x không buộc multiplier>0; dùng cùng glossary ở mọi tầng. “Bước dương đủ nhỏ” không bị renderer hoặc editor rút thành “mọi bước dương”.
- **T27:** prompt compiler phải dùng dữ liệu tra cứu cục bộ, không tự thay bản nguồn. Domain mâu thuẫn/còn mơ hồ được báo, không giấu bằng một lựa chọn. Key cũ teaching_contract vẫn đọc được; tên nội bộ không xuất hiện trên màn hình học.
