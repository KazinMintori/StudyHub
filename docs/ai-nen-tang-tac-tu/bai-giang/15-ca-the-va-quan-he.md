---
course: ai-nen-tang-tac-tu
lecture: 15-ca-the-va-quan-he
section: lecture
title: "Cá thể và quan hệ"
prerequisites: []
lessonStatus: ready
description: "Biểu diễn tri thức và suy luận logic dựa trên cá thể, quan hệ, ngôn ngữ Datalog, hợp nhất, ký hiệu hàm và các ứng dụng trong xử lý ngôn ngữ tự nhiên."
---

> *Thế giới thực tồn tại với cấu trúc thực sự. Chương trình của tâm trí con người đã được trui rèn qua quá trình tương tác rộng lớn với thế giới này, vì vậy nó chứa đựng những đoạn mã phản chiếu cấu trúc của thế giới và biết cách khai thác cấu trúc ấy. Đoạn mã này chứa các biểu diễn về những đối tượng thực trong thế giới và đại diện cho các tương tác giữa các đối tượng thực. Đoạn mã chủ yếu mang tính mô-đun..., với các mô-đun chuyên xử lý những loại đối tượng khác nhau và các mô-đun tổng quát hóa trên nhiều loại đối tượng.... Các mô-đun tương tác theo những cách thức phản ánh thế giới thực và đưa ra những dự đoán chính xác về cách thức thế giới tiến hóa....*
>
> *Bạn khai thác cấu trúc của thế giới để đưa ra quyết định và thực hiện hành động. Nơi bạn vạch ra ranh giới giữa các phạm trù, điều gì cấu thành nên một đối tượng đơn lẻ hoặc một lớp đối tượng đối với bạn, đều do chương trình tâm trí bạn quyết định thông qua phân loại. Phép phân loại này không hề ngẫu nhiên mà phản ánh một sự mô tả cô đọng về thế giới, và đặc biệt là một sự mô tả hữu ích cho việc khai thác cấu trúc của thế giới.*
>
> — Eric B. Baum (2004, tr. 169–170)

Chương học này tập trung vào phương pháp biểu diễn các cá thể (sự vật, thực thể, đối tượng) và những mối quan hệ giữa chúng. Như Baum đã chỉ ra, thế giới thực chứa đựng các đối tượng, và việc biểu diễn cô đọng các đối tượng cùng những quan hệ giữa chúng sẽ giúp quá trình suy luận trở nên khả thi về mặt tính toán. Những biểu diễn quan hệ như vậy cô đọng hơn rất nhiều so với việc chỉ sử dụng thuần túy các đặc trưng (features). Chương này xem xét các biểu diễn logic hình thức và cung cấp những ví dụ chi tiết về cách áp dụng biểu diễn này vào giao diện ngôn ngữ tự nhiên truy vấn cơ sở dữ liệu.

## Mục tiêu học tập

Sau khi hoàn thành chương học này, người học có thể:

1. **Hiểu rõ vai trò của cấu trúc quan hệ**: Nắm vững lý do tại sao biểu diễn dựa trên cá thể và quan hệ lại tự nhiên, cô đọng và linh hoạt vượt trội so với biểu diễn bằng biến/đặc trưng mệnh đề.
2. **Làm chủ ngữ nghĩa hình thức của logic vị từ**: Nắm vững khái niệm miền cá thể ($\mathcal{D}$), phép gán hằng số và hàm ($\phi$), phép gán chân lý vị từ ($\pi$), diễn giải ($I$), giá trị chân lý của các công thức chứa lượng từ với mọi ($\forall$) và tồn tại ($\exists$).
3. **Thành thạo ngôn ngữ luật Datalog**: Viết và giải thích các câu tuyển xác định (definite clauses), sự kiện (facts), luật suy diễn (rules), câu hỏi truy vấn (queries) và bản chất của nguyên tử không biến (ground atom).
4. **Hiểu sâu cơ chế chứng minh và phép thế**: Nắm vững thuật toán suy diễn tiến (bottom-up proof procedure), suy diễn lùi (top-down proof procedure), phép thế ($\theta$), hợp nhất tổng quát nhất (most general unifier — MGU) và giải thuật đồng nhất hóa (unification).
5. **Vận dụng ký hiệu hàm và cấu trúc dữ liệu**: Biểu diễn các cấu trúc phức hợp, danh sách, cây đệ quy và số tự nhiên Peano mà không bị giới hạn trong miền hữu hạn.
6. **Ứng dụng vào phân tích cú pháp ngôn ngữ tự nhiên**: Xây dựng văn phạm mệnh đề xác định (Definite Clause Grammar — DCG) để phân tích câu, dịch câu hỏi tự nhiên thành truy vấn logic đối với cơ sở dữ liệu.
7. **Nắm vững quan hệ đẳng thức và giả định tri thức đầy đủ**: Hiểu tiên đề đẳng thức, giả định tên duy nhất (UNA), bao đóng Clark (Clark's completion) và phủ định như một sự thất bại (negation-as-failure).

<TopicMap />

## Bản đồ chương học

Chương học được tổ chức thành 13 chủ đề chi tiết, bao quát trọn vẹn lý thuyết và ứng dụng:

- **15.1 Khai thác cấu trúc quan hệ**: Động lực chuyển từ biểu diễn đặc trưng sang cá thể và quan hệ; các ưu thế cốt lõi của biểu diễn quan hệ.
- **15.2 Ký hiệu và ngữ nghĩa**: Vai trò của biểu tượng trong việc gọi tên cá thể và quan hệ; bản thể học hình thức; sự độc lập giữa cú pháp hình thức và thực tại thế giới.
- **15.3 Logic vị từ**: Cú pháp và ngữ nghĩa hình thức; diễn giải, phép gán biến, lượng từ $\forall$ và $\exists$; đếm số lượng diễn giải khả dĩ; công thức mở và biến tự do.
- **15.4 Datalog: Ngôn ngữ luật quan hệ**: Cú pháp các câu tuyển xác định quan hệ; sự kiện, luật và truy vấn; cấu trúc biến và hằng.
- **15.5 Chứng minh và phép thế**: Suy luận tiến và mô hình cực tiểu; suy luận lùi dựa trên phân giải SLD; phép hợp nhất (unification) và thuật toán MGU.
- **15.6 Ký hiệu hàm và cấu trúc dữ liệu**: Mở rộng Datalog với ký hiệu hàm; biểu diễn danh sách, cây và số học; tính đầy đủ Turing; logic bậc một và bậc hai; cơ chế occurs check.
- **15.7 Ứng dụng trong ngôn ngữ tự nhiên**: Văn phạm phi ngữ cảnh dưới dạng logic tuyển; văn phạm mệnh đề xác định (DCG) và danh sách sai phân; giao diện hỏi đáp cơ sở dữ liệu; so sánh khách quan với các mô hình ngôn ngữ lớn (LLM).
- **15.8 Đẳng thức**: Ngữ nghĩa của dấu bằng ($=$); tiên đề tương đương và thay thế; giả định tên duy nhất (Unique Names Assumption); thủ tục suy diễn với cơ chế trì hoãn bất đẳng thức.
- **15.9 Giả định tri thức đầy đủ**: Giả định thế giới đóng; dạng chuẩn Clark và bao đóng Clark; phủ định như một sự thất bại (NAF); xử lý biến tự do gây tắc nghẽn (floundering).
- **15.10 Tác động xã hội**: Ứng dụng thực tế của lập trình logic: Trình kiểm tra kiểu bytecode của máy ảo Java (JVM), phân tích manh mối Jeopardy! của siêu máy tính IBM Watson, và chu trình thực nghiệm tự động của nhà khoa học robot Adam.
- **15.11 Ôn tập**: Tổng kết 8 luận điểm cốt lõi của chương.
- **15.12 Tài liệu tham khảo và đọc thêm**: Chỉ mục các công trình kinh điển và giáo trình chuyên sâu về Datalog, lập trình logic, ngữ nghĩa bao đóng Clark và ngôn ngữ học tính toán.
- **15.13 Bài tập**: Hệ thống 15 bài tập tự luyện toàn diện từ giáo trình gốc kèm lời giải chi tiết giúp củng cố kiến thức.

## Tài liệu tham khảo

- Poole, D. L., & Mackworth, A. K. (2023). *Artificial Intelligence: Foundations of Computational Agents* (3rd ed.). Cambridge University Press. Bản điện tử: [https://artint.info/3e/html/ArtInt3e.Ch15.html](https://artint.info/3e/html/ArtInt3e.Ch15.html).
- Baum, E. B. (2004). *What Is Thought?* MIT Press, Cambridge, MA, pp. 169–170.
- Clark, K. L. (1978). Negation as failure. In H. Gallaire & J. Minker (Eds.), *Logic and Data Bases* (pp. 293–322). Plenum Press.
- Lloyd, J. W. (1987). *Foundations of Logic Programming* (2nd ed.). Springer-Verlag.
- Pereira, F. C. N., & Shieber, S. M. (2002). *Prolog and Natural-Language Analysis* (Digital ed.). CSLI Publications.
