# Cách áp dụng nghiên cứu prompt

Phần thuật ngữ bổ sung ở phiên bản 2.1/6.1: Đọc [terminology-research.md](terminology-research.md) để biết chứng cứ dùng từ EN–VI, các chỗ đã hiệu chỉnh và giới hạn dữ liệu.

Kiểm tra ngày 07/10/2026. Kho được đọc tại commit `7d3f248962d1dca209d59e033524bcb86c2b26b8`. Các prompt và ví dụ tiếng Việt mới trong gói là thiết kế của dự án; không chép nguyên văn sách hướng dẫn của prompts.chat.

## Những gì lấy từ prompts.chat

- [Anatomy of Effective Prompt](https://github.com/f/prompts.chat/blob/7d3f248962d1dca209d59e033524bcb86c2b26b8/src/content/book/02-anatomy-of-effective-prompt.mdx): Vai trò, bối cảnh, nhiệm vụ, ràng buộc, định dạng và ví dụ. Áp dụng thành kế hoạch giảng cho từng đơn vị nguồn; không yêu cầu mọi prompt ngắn phải có đủ trường.
- [Few-Shot Learning](https://github.com/f/prompts.chat/blob/7d3f248962d1dca209d59e033524bcb86c2b26b8/src/content/book/07-few-shot-learning.mdx): Dùng ví dụ đầu vào–đầu ra để làm rõ giọng và ranh giới. Áp dụng bằng ví dụ cùng ý nhưng khác giọng, cùng bản sửa có lý do; không thêm tiểu sử hoặc bắt chước cá nhân cụ thể.
- [Prompt Chaining](https://github.com/f/prompts.chat/blob/7d3f248962d1dca209d59e033524bcb86c2b26b8/src/content/book/11-prompt-chaining.mdx): Chia việc phức tạp thành các lượt với đầu ra dùng được ở lượt sau. Áp dụng vào nguồn, thiết kế, soạn, sửa giọng, kiểm tra nghĩa và dựng; không mặc định nhiều lượt luôn tốt hơn.
- [Education and Learning](https://github.com/f/prompts.chat/blob/7d3f248962d1dca209d59e033524bcb86c2b26b8/src/content/book/20-education-learning.mdx): Bối cảnh người học, phản hồi và điều chỉnh nhiệm vụ theo câu trả lời. Áp dụng khi người dùng muốn đối thoại; không áp dụng yêu cầu chỉ hỏi, không cho đáp án trong chế độ giải thích trực tiếp.
- [prompts.csv](https://github.com/f/prompts.chat/blob/7d3f248962d1dca209d59e033524bcb86c2b26b8/prompts.csv): Đã đọc các mục Math Teacher, Educational Content Creator, Academician và Socratic Method. Chúng định hướng vai trò nhưng chưa quy định đủ giả thiết, bước chứng minh và giọng tiếng Việt; gói này bổ sung các kế hoạch giảng nội dung cụ thể.

Đây là tham khảo kỹ thuật thiết kế prompt, không phải bằng chứng thực nghiệm rằng gói mới dạy tốt như giáo sư. Không dùng sở thích “visual/theoretical” trong prompt tham khảo để gán người học vào một learning style cố định.

## Cơ sở sư phạm dùng thêm

[CMU Teaching Principles](https://www.cmu.edu/teaching/principles/teaching.html) hướng dẫn liên kết mục tiêu–hoạt động–đánh giá, nhận ra bước chuyên gia thường bỏ qua và điều chỉnh theo phản hồi. Thiết kế ở đây mở đúng bước quyết định và kiểm tra việc người học làm được, thay vì chỉ dùng giọng có vẻ chuyên gia.

[IES Practice Guide](https://ies.ed.gov/ncee/wwc/PracticeGuide/1) phân mức bằng chứng: Ví dụ xen giải bài, đồ họa kèm lời và nối cụ thể–trừu tượng ở mức moderate; câu hỏi giải thích sâu và quiz để gặp lại nội dung ở mức strong. Mức bằng chứng của từng khuyến nghị không tự truyền sang prompt hoặc ví dụ mới.

Ví dụ tối ưu được đối chiếu với [Boyd & Vandenberghe, Convex Optimization](https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf), mục 3.1.3 (điều kiện bậc nhất) và 4.2.3 (điều kiện tối ưu). Các đoạn ví dụ trong gói tự viết; không phải trích nguyên văn. Giới hạn ví dụ ở bài toán không ràng buộc trên R^n để không vô tình tuyên bố mọi nghiệm có ràng buộc phải có gradient bằng 0.

## Vì sao không dùng một blacklist tuyệt đối

Cách nói gượng trong phản hồi của người dùng là dữ liệu thiết kế của dự án, không phải một corpus thống kê tiếng Việt. Gói dùng chúng làm cảnh báo theo ngữ cảnh, bảo vệ thuật ngữ chuẩn và trích dẫn. Script tìm vị trí để con người/model biên tập, không tự thay từ hoặc đo “tính người”.

## Công nghệ được chọn theo lỗi cần sửa

- Python thư viện chuẩn cho khởi tạo prompt và rà dấu hiệu: Chạy offline, không cần khóa API.
- Tính toán/mã/đồ thị xác định khi bài học cần kiểm chứng: Chọn SymPy, NumPy, runtime của môn hoặc công cụ tương đương nếu có; không cài chúng chỉ để làm lời giảng hấp dẫn.
- Renderer PDF/PPTX/HTML theo môi trường và định dạng đã yêu cầu. Bản đặc tả chưa được render không được gọi là bộ slide hoàn chỉnh.
- Không cần fine-tuning, kho vector, MCP hay API ngoài cho việc sửa giọng. Chỉ bổ sung khi có nhu cầu dữ liệu hoặc khối lượng thực tế và kiểm tra tác dụng bằng output.
