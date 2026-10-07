# Kiểm thử thực tế: notes-forward

Ngày thực hiện: 2026-10-07. Đây là một lượt áp dụng skill vào ba yêu cầu độc lập, dùng các nguồn thử nghiệm và bài làm do yêu cầu kiểm thử cung cấp.

## Output đã tạo

- `01-convexity-chat.md`: lời giảng tiếng Việt cho người đã biết đạo hàm.
- `02-convexity-study-note.md`: note Markdown độc lập của yêu cầu 1.
- `03-literature-chat.md`: lời giảng phân tích văn bản cho người học lần đầu, theo yêu cầu 2.
- `04-probability-feedback.md`: phản hồi ngắn vào bài làm, theo yêu cầu 3.

Mỗi file trên là nội dung phản hồi thực tế được soạn trong lượt này. File này là nhận xét về phạm vi công việc, không phải phản hồi giảng bài.

## Tài liệu đã đọc

Chỉ đọc `Research/revised/textbook-passage-explainer/SKILL.md` cùng bốn reference cần dùng: `professor-voice.md`, `content-prompts.md`, `pedagogy.md` và `teaching-review.md`. Không đọc output đánh giá của agent khác, `prompt-research` hoặc `behavior-tests`. Không sửa skill hoặc website.

## Nhận xét về nội dung và giới hạn

Yêu cầu 1 đã được xử lý thành lời giảng và note riêng. Bản soạn giữ miền R^n, tính khả vi, tính lồi và lượng từ “mọi”; mở bước lấy giới hạn để suy ra cận dưới, rồi thay gradient bằng 0 để chứng minh cực tiểu toàn cục. Ví dụ và các giới hạn bổ sung được nhận diện là phần do người giải thích thêm. Note có phần nền về gradient vì người học chỉ xác nhận đã biết đạo hàm, chưa xác nhận kiến thức nhiều biến.

Yêu cầu 2 dùng những hành động và thông tin thực sự xuất hiện trong đoạn làm chứng cứ. Các nhận xét về chờ đợi và không gian riêng tư được viết như cách đọc có thể có. Bản soạn không xác định nội dung thư hoặc động cơ nhân vật. Chưa có văn bản trước và sau để kiểm tra các cách đọc ấy trong toàn tác phẩm.

Yêu cầu 3 giữ tử số người học đã chọn đúng và sửa mẫu số từ 100 sang 40. Phản hồi phân biệt xác suất có điều kiện với xác suất giao, rồi cho người học thử lại việc chọn mẫu số. Chưa nhận được câu trả lời cho câu hỏi thử lại.

Tôi đã tự rà ký hiệu, điều kiện, suy luận, phép tính và cách diễn đạt; đây là tự rà của cùng người soạn. Không chạy script lint hay thực hiện đánh giá độc lập. Không có người học thật tham gia, không có dữ liệu trước/sau hoặc bài chuyển giao được người học hoàn thành. Các output chỉ cho phép xem xét việc áp dụng hướng dẫn trên ba trường hợp; chúng không chứng minh hiệu quả học tập, mức hiểu hoặc mức thành thạo của người học, cũng không xác nhận độ tin cậy trên các môn và tình huống khác.
