export const predicateConcepts = {
  "vi-tu": {
    "name": "Vị từ",
    "aliases": [
      "Ký hiệu vị từ",
      "Quan hệ vị từ",
      "Predicate symbol",
      "vị từ",
      "predicate"
    ],
    "definition": "Ký hiệu cú pháp có số ngôi cố định biểu thị một quan hệ hoặc thuộc tính trên các đối tượng của miền diễn giải, trả về giá trị chân lý Đúng hoặc Sai.",
    "example": "Ký hiệu vị từ $Student(x)$ biểu diễn thuộc tính sinh viên, $Brother(x, y)$ biểu diễn quan hệ hai ngôi giữa hai cá thể.",
    "use": "Được dùng để xây dựng các công thức nguyên tử, phát biểu các sự kiện và luật ràng buộc trong cơ sở tri thức.",
    "question": "Ký hiệu vị từ khác ký hiệu hàm như thế nào về mặt cú pháp và ngữ nghĩa?",
    "answer": "Ký hiệu hàm nhận các hạng thức làm đối số và ánh xạ sang một đối tượng trong miền, đóng vai trò tạo nên hạng thức. Ký hiệu vị từ nhận các hạng thức làm đối số và ánh xạ sang giá trị chân lý Đúng hoặc Sai, đóng vai trò tạo nên công thức."
  },
  "luong-tu-thu-tu": {
    "name": "Thứ tự lượng từ",
    "aliases": [
      "Hoán vị lượng từ",
      "Thứ tự lượng từ hỗn hợp",
      "Quantifier order"
    ],
    "definition": "Trình tự sắp xếp giữa các lượng từ phổ dụng và lượng từ tồn tại trong một công thức logic, quyết định phạm vi phụ thuộc và giá trị chân lý của câu.",
    "example": "Câu $\\exists x \\forall y L(x, y)$ khẳng định một người yêu tất cả mọi người, kéo theo $\\forall y \\exists x L(x, y)$ là mỗi người đều được ai đó yêu, nhưng chiều ngược lại không đúng.",
    "use": "Được dùng để phân biệt chính xác mức độ phụ thuộc giữa các biến trong các định lý toán học và quy tắc nghiệp vụ phức tạp.",
    "question": "Khi nào việc hoán đổi vị trí của hai lượng từ liền kề không làm thay đổi giá trị chân lý?",
    "answer": "Việc hoán vị không làm thay đổi giá trị chân lý khi hai lượng từ đứng cạnh nhau thuộc cùng một loại, tức là cùng là lượng từ phổ dụng hoặc cùng là lượng từ tồn tại. Nếu hai lượng từ khác loại đứng cạnh nhau, việc hoán vị có thể làm thay đổi hoàn toàn giá trị chân lý của câu."
  },
  "dong-nhat-hoa": {
    "name": "Đồng nhất hóa và MGU",
    "aliases": [
      "Unification",
      "MGU",
      "Occurs check",
      "Đồng nhất hóa",
      "hợp nhất cú pháp"
    ],
    "definition": "Quá trình tìm kiếm phép thế tổng quát nhất (MGU) làm cho hai biểu thức vị từ giống hệt nhau về mặt cú pháp, đi kèm bước kiểm tra xuất hiện để ngăn chặn chu trình vô hạn trong đại số hạng thức hữu hạn.",
    "example": "Hai nguyên tử $P(x,a)$ và $P(b,y)$ hợp nhất bằng phép thế $x\\mapsto b$, $y\\mapsto a$.",
    "use": "Được sử dụng làm hạt nhân so khớp trong suy luận tiến, suy luận lùi SLD và nguyên lý hợp giải vị từ.",
    "question": "Tại sao phép hợp nhất đòi hỏi bước kiểm tra xuất hiện ngay cả khi hai biểu thức có vẻ tương thích về mặt ký hiệu?",
    "answer": "Vì nếu một biến được gán bằng một hạng thức phức hợp chứa chính nó, việc giải tham chiếu sẽ tạo ra chu trình vô hạn không thể tồn tại trong đại số hạng thức hữu hạn."
  },
  "skolem-hoa": {
    "name": "Skolem hóa và Bảo toàn tính thỏa được",
    "aliases": [
      "Skolemization",
      "Hàm Skolem",
      "Hằng số Skolem",
      "Equisatisfiability"
    ],
    "definition": "Kỹ thuật loại bỏ lượng từ tồn tại bằng cách thay thế biến tồn tại bằng một hằng số mới hoặc một hàm mới phụ thuộc vào các biến phổ dụng bao ngoài, bảo toàn tính thỏa được của cơ sở tri thức.",
    "example": "Từ $\\forall x\\exists y\\,R(x,y)$ chuyển thành $\\forall x\\,R(x,f(x))$ với ký hiệu hàm mới $f$.",
    "use": "Được sử dụng trong bước chuẩn hóa cơ sở tri thức trước khi đưa về dạng chuẩn mệnh đề phục vụ thuật toán hợp giải.",
    "question": "Tại sao Skolem hóa chỉ bảo toàn tính thỏa được mà không bảo toàn tính tương đương logic trong cùng ngôn ngữ ban đầu?",
    "answer": "Vì ký hiệu Skolem là một ký hiệu mới được bổ sung vào ngôn ngữ, và công thức gốc không áp đặt bất kỳ diễn giải ngữ nghĩa bắt buộc nào lên ký hiệu mới này trong các mô hình ban đầu."
  }
}
export const predicateWikiDetails = {
  "vi-tu": "Trong logic vị từ bậc một, ký hiệu vị từ $P$ có số ngôi $k$ được diễn giải ngữ nghĩa thông qua mô hình $M = (D, I)$ thành một quan hệ cụ thể $I(P) \\subseteq D^k$. Một công thức nguyên tử $P(t_1, \\dots, t_k)$ nhận giá trị Đúng khi bộ đối tượng được tham chiếu bởi các hạng thức thuộc về tập quan hệ $I(P)$. Nếu $k = 1$, vị từ biểu diễn một thuộc tính đơn lẻ của đối tượng. Nếu $k \\ge 2$, vị từ biểu diễn mối quan hệ qua lại giữa nhiều đối tượng.",
  "luong-tu-thu-tu": "Khi xét hai lượng từ khác loại liền kề, công thức dạng $\\exists x \\forall y P(x, y)$ có tính ràng buộc chặt chẽ hơn nhiều so với $\\forall y \\exists x P(x, y)$. Trong công thức đầu tiên, đối tượng $x$ được chọn trước và cố định làm nhân chứng chung cho toàn bộ các phần tử $y$. Trong công thức thứ hai, với mỗi giá trị của $y$, chúng ta được phép chọn một giá trị $x$ phụ thuộc riêng vào $y$. Phản mô hình sử dụng quan hệ đồng nhất trên miền hai phần tử kiểm chứng rõ ràng rằng chiều suy diễn ngược lại không hợp lệ.",
  "dong-nhat-hoa": "Thuật toán hợp nhất vận hành trên cây cú pháp của hai biểu thức. Trong quá trình duyệt, khi gặp một biến chưa được gán, thuật toán phải xác minh xem biến đó có nằm trong hạng thức đối ứng hay không.\n\nNếu biến xuất hiện trong hạng thức, việc gán giá trị sẽ dẫn đến một cấu trúc đệ quy vô hạn trong đại số hạng thức hữu hạn. Quá trình kiểm tra xuất hiện cần được thực hiện đệ quy trên toàn bộ cấu trúc sau khi đã giải tham chiếu các biến đã biết trong phép thế hiện thời.\n\nĐộ phức tạp tính toán của thuật toán phụ thuộc vào cách biểu diễn cấu trúc dữ liệu và việc tối ưu hóa các bước kiểm tra chu trình.",
  "skolem-hoa": "Skolem hóa là một bước thiết yếu trong quy trình chuẩn hóa mệnh đề CNF cho logic vị từ bậc một. Khi một biến tồn tại nằm trong phạm vi của một hoặc nhiều biến phổ dụng, đối tượng được khẳng định tồn tại có thể thay đổi tùy thuộc vào giá trị của các biến phổ dụng đó.\n\nViệc sử dụng hàm Skolem ghi nhận chính xác mối quan hệ phụ thuộc hàm này. Những xuất hiện bắt nguồn từ cùng một biến tồn tại dùng chung ký hiệu Skolem sau khi phân phối phép tuyển trên phép hội. Các lượng từ tồn tại độc lập cần được gán ký hiệu nhân chứng mới riêng."
}
