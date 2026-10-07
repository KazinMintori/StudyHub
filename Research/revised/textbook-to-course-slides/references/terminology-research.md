# Căn cứ cho tầng thuật ngữ EN–VI

Khảo sát ngày 07/10/2026. Bản này bổ sung cho [prompt-research.md](prompt-research.md), dùng [translation-vi.md](translation-vi.md) để quyết định cách soạn. Không coi lời tư vấn trong file người dùng dán là bằng chứng đã huấn luyện hoặc đã đo hiệu quả.

## Cách gọi được đối chiếu

| Cách gọi | Chứng cứ đã xem | Phạm vi kết luận |
| --- | --- | --- |
| Ánh xạ co | [Bài báo HCMUE](https://journal.hcmue.edu.vn/index.php/hcmuejos/article/view/3961): nhan đề/tóm tắt Việt trong chỉ mục, nhan đề Anh contraction mappings ở trang bài báo | Có chứng cứ dùng tên này trong nghiên cứu toán tiếng Việt; không là tiêu chuẩn quốc gia duy nhất. |
| Điểm khả thi, tập/miền khả thi | [Bài báo Đại học Cần Thơ](https://ctujsvn.ctu.edu.vn/index.php/ctujsvn/article/download/4457/4174/9846): bản PDF, trang in 92–93 | Cách gọi chuyên ngành có chứng cứ; “khả thi” không phải từ cần né vì nghe hành chính. |
| Phép co tensor | [Đề cương TN545 Đại học Cần Thơ](https://cns.ctu.edu.vn/images/upload/daotao/decuong/TN545.pdf): mục 6, PDF trang 2 | Cách gọi có trong chương trình đào tạo; đề cương không cung cấp định nghĩa đầy đủ của mọi loại phép co. |
| Phép cộng theo trục ghép trong tích tensor | [NumPy tensordot](https://numpy.org/doc/stable/reference/generated/numpy.tensordot.html): mô tả axes và phần Notes | Nguồn kỹ thuật cho phép toán trên mảng; không là bằng chứng cách dịch tiếng Việt hoặc mọi phép co của hình học tensor. |
| Ghép chỉ số trên/dưới trong tensor hình học | [Lecture Notes Differential Geometry, mục 2.6](https://math.berkeley.edu/~ltomczak/notes/Mich2022/DG_Notes.pdf), cùng [Knill, Tensor Analysis](https://people.math.harvard.edu/~knill/teaching/math109_1995/geometry.pdf) về tensor (1,1) của ánh xạ tuyến tính | Tổng chỉ số phải theo loại tensor/cấu trúc đã cho; trace của tensor hỗn hợp là ví dụ, không coi tổng đường chéo của tensor covariant bất kỳ là bất biến. |

Bản định nghĩa ánh xạ co và các giả thiết của Banach được thấy trong văn bản chỉ mục của [bài báo Hàng hải, trang 81](https://scholar.dlu.edu.vn/thuvienso/bitstream/DLU123456789/127194/1/41639-1333-137963-1-10-20191203.pdf). Lần này không tải được PDF đầy đủ; ghi rõ mức truy cập trong bộ nhớ. Bất đẳng thức và ví dụ trong gói tự viết, không chép nguyên văn bài báo.

Các khái niệm tối ưu tham khảo [Boyd & Vandenberghe](https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf) đã đọc ở lượt nghiên cứu trước; lần truy cập hiện tại bị lỗi. Không dùng nguồn tiếng Anh này để gán mọi bản dịch do dự án chọn là cách gọi Việt đã được xác nhận. Tên cho active constraint được để phụ thuộc glossary môn, kèm điều kiện g_i(x)=0 thay vì coi tên gọi là đủ để giải thích.

## Các điều chỉnh so với đề xuất dán vào

- “Có thể âm hoặc dương” nghe tự nhiên nhưng chưa mô tả hết miền không giới hạn dấu: phải giữ khả năng bằng 0 khi đang giải thích miền.
- “Khoảng cách nhỏ đi” chưa thay được định nghĩa ánh xạ co: giữ một hệ số chung q với 0 ≤ q < 1 cho mọi cặp điểm. Nếu giảng Banach, còn cần không gian đầy đủ, khác rỗng và ánh xạ từ không gian vào chính nó.
- Lời giảng chọn hướng giảm không bảo đảm giảm với mọi bước dương. Khi nguồn nói sufficiently small, giữ “đủ nhỏ”.
- Không ghép stationarity với “tạo hướng cập nhật” nếu chưa có bài toán con xác định hướng. Câu tự nhiên hơn vẫn có thể sai về phương pháp.
- Không cấm “hợp đồng” trong mọi ngữ cảnh, không cấm tên active constraint của một giáo trình chỉ vì không trùng tên dự án chọn.
- Lượt soạn thử chọn đúng nghĩa tensor contraction nhưng ví dụ ma trận chưa xác định loại chỉ số. Đã bổ sung kiểm tra giả định của ví dụ và chọn A^i_j cho trace; đúng thuật ngữ vẫn chưa đủ chứng minh ví dụ đúng.
- RAG và fine-tuning là lựa chọn triển khai, không phải kết quả đã có. Tra cứu trong gói là tra cụm có domain, chưa có embedding/model và không tự phân tích nghĩa. Không khẳng định lượng dữ liệu cố định sẽ đủ huấn luyện.

## Tài nguyên thực tế trong gói

15 mục khái niệm ở ba lĩnh vực (`fixed-point`, `tensor-algebra`, `optimization`) và 10 ví dụ tự viết ở các mức thuật ngữ, câu và mạch giảng. Mục nào chỉ là lựa chọn biên tập được ghi rõ. [training-and-evaluation.md](training-and-evaluation.md) hướng dẫn cách bổ sung corpus có nguồn, split kiểm tra và đánh giá nghĩa trước giọng. Không đưa tập kiểm tra vào nguồn ví dụ truy xuất; lọc câu trùng chính xác trong script chưa thể ngăn mọi biến thể tương đương.

Các kiểm tra và lượt giảng thử có output thực nằm trong folder evaluation của dự án, ngoài gói skill. Chúng kiểm tra một số tình huống; chưa có người học thật hoặc một model được fine-tune trên dữ liệu này.
