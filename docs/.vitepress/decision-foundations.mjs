export const decisionConcepts = {
  "mdp": {
    "name": "Quá trình quyết định Markov",
    "aliases": [
      "MDP",
      "quá trình quyết định Markov"
    ],
    "definition": "Mô hình ra quyết định tuần tự gồm trạng thái, hành động, xác suất chuyển và phần thưởng. Phân phối bước tiếp theo chỉ phụ thuộc trạng thái và hành động hiện tại khi đã biết đủ thông tin trong trạng thái.",
    "example": "Robot chọn đi lên nhưng có thể trượt sang hai bên. Mô hình phải ghi xác suất từng kết quả và cách nhận thưởng.",
    "use": "Mô hình hóa bài toán có kết quả hành động ngẫu nhiên trước khi tính chính sách.",
    "question": "Biết tọa độ đã đủ tính Markov cho robot có pin chưa?",
    "answer": "Chưa đủ nếu mức pin ảnh hưởng bước chuyển hoặc hành động khả dụng. Có thể cần thêm mức pin vào trạng thái."
  },
  "chinh-sach-mdp": {
    "name": "Chính sách trong MDP",
    "aliases": [
      "chính sách tối ưu",
      "chính sách MDP"
    ],
    "definition": "Quy tắc chọn hành động theo trạng thái. Với chân trời hữu hạn, quy tắc có thể phụ thuộc thời gian còn lại. Trong MDP hữu hạn có thưởng bị chặn và chiết khấu nhỏ hơn 1, tồn tại chính sách tối ưu tất định không phụ thuộc thời điểm.",
    "example": "Ở một ô lưới, chính sách chỉ định đi lên. Khi bị trượt sang ô khác, tác tử tra chính sách tại ô mới.",
    "use": "Mô tả cách hành động sau mọi kết quả có thể gặp.",
    "question": "Một dãy hành động có mô tả đủ chính sách không?",
    "answer": "Trong môi trường ngẫu nhiên, cần chỉ định hành động cả ở các trạng thái phát sinh do kết quả khác dự kiến."
  },
  "bellman": {
    "name": "Phương trình Bellman",
    "aliases": [
      "phương trình Bellman",
      "cập nhật Bellman"
    ],
    "definition": "Quan hệ đệ quy tách lợi ích thành thưởng tức thời và lợi ích tiếp tục. Với chính sách cố định ta lấy kỳ vọng theo hành động đó. Khi tối ưu, ta so sánh kỳ vọng của mọi hành động khả dụng.",
    "example": "Ở lại nhận 1 và trở về chính nó. Với chiết khấu 0,9, giá trị của chính sách luôn ở lại thỏa v = 1 + 0,9v, nên v = 10.",
    "use": "Đánh giá chính sách, lặp giá trị và cải tiến chính sách.",
    "question": "Khi tính kỳ vọng có nhân chiết khấu cho thưởng tức thời không?",
    "answer": "Trong quy ước thưởng trên cạnh hiện tại, thưởng đó có trọng số 1. Chiết khấu nhân với giá trị tiếp tục ở bước sau."
  },
  "ontology": {
    "name": "Ontology",
    "aliases": [
      "bản thể học",
      "ontology"
    ],
    "definition": "Đặc tả các lớp đối tượng, cá thể, quan hệ và tiên đề của một miền tri thức. Phân cấp lớp là một phần của ontology. Ngữ nghĩa của từng loại cạnh quyết định các suy luận được phép.",
    "example": "Buster thuộc lớp Chó và Chó là lớp con của Thú thì Buster thuộc Thú. Cạnh một động cơ là bộ phận của ô tô cần quy tắc khác.",
    "use": "Thiết kế cơ sở tri thức có loại quan hệ và ràng buộc rõ ràng.",
    "question": "Có thể dùng cùng một quy tắc cho mọi cạnh đồ thị không?",
    "answer": "Phải kiểm tra loại cạnh và tiên đề đi kèm. Quan hệ lớp con và quan hệ bộ phận mang nghĩa khác nhau."
  },
  "dau-cat-prolog": {
    "name": "Dấu cắt trong Prolog",
    "aliases": [
      "dấu cắt",
      "cut trong Prolog"
    ],
    "definition": "Mục tiêu đặc biệt viết bằng dấu chấm than. Khi được thực thi, nó bỏ các lựa chọn thay thế của lời gọi vị từ hiện hành và các lựa chọn đã sinh bởi mục tiêu bên trái trong mệnh đề đó.",
    "example": "Trong p(X) :- a(C), !, b(C,X), dấu cắt bỏ các cách chọn C khác của a/1. Các đáp án tiếp theo của b/2 vẫn có thể được tìm.",
    "use": "Đọc phạm vi quay lui và kiểm tra một dấu cắt có làm thay đổi tập câu trả lời không.",
    "question": "Dấu cắt có xóa lựa chọn của mọi lời gọi tổ tiên không?",
    "answer": "Không. Phạm vi được xác định bởi lời gọi vị từ chứa dấu cắt."
  },
  "naive-bayes": {
    "name": "Naive Bayes",
    "aliases": [
      "Bayes ngây thơ"
    ],
    "definition": "Mô hình phân lớp sinh dùng giả thiết các đặc trưng độc lập có điều kiện khi đã biết nhãn. Điểm mỗi nhãn bằng tiên nghiệm nhân với các likelihood thành phần.",
    "example": "Hai từ có thể tương quan trong toàn tập dữ liệu dù độc lập sau khi biết nhãn.",
    "use": "Đọc mô hình, kiểm tra giả thiết và theo dõi ví dụ tính toán.",
    "question": "Giả thiết độc lập được áp dụng trước hay sau khi biết nhãn?",
    "answer": "Sau khi biết nhãn."
  },
  "lam-tron-laplace": {
    "name": "Làm trơn Laplace",
    "aliases": [
      "làm trơn Laplace"
    ],
    "definition": "Ước lượng xác suất bằng cách cộng số đếm giả cho mọi giá trị trong miền. Khi cộng alpha cho K giá trị, mẫu số tăng alpha nhân K.",
    "example": "Ba số đếm 3, 2, 0 thành 4, 3, 1 khi alpha bằng 1.",
    "use": "Đọc mô hình, kiểm tra giả thiết và theo dõi ví dụ tính toán.",
    "question": "Vì sao mẫu số phải tăng cho tất cả giá trị?",
    "answer": "Để các xác suất sau làm trơn vẫn cộng thành 1."
  },
  "perceptron": {
    "name": "Perceptron",
    "aliases": [
      "Perceptron"
    ],
    "definition": "Bộ phân lớp tuyến tính cập nhật trọng số theo mẫu bị phân loại sai. Định lý hội tụ yêu cầu dữ liệu phân tách tuyến tính và quy tắc cập nhật phù hợp.",
    "example": "AND có thể tách tuyến tính, XOR không thể tách bằng một đường thẳng.",
    "use": "Đọc mô hình, kiểm tra giả thiết và theo dõi ví dụ tính toán.",
    "question": "Có bảo đảm hội tụ trên XOR không?",
    "answer": "Một Perceptron tuyến tính không có đường phân chia thực hiện đúng bảng XOR."
  },
  "lan-truyen-nguoc": {
    "name": "Lan truyền ngược",
    "aliases": [
      "backpropagation",
      "lan truyền ngược"
    ],
    "definition": "Thuật toán tính gradient của mất mát theo tham số bằng quy tắc chuỗi, truyền đạo hàm từ đầu ra về các phép tính trước đó.",
    "example": "Gradient ở nút ẩn dùng các trọng số của cùng lượt lan truyền thuận trước khi cập nhật.",
    "use": "Đọc mô hình, kiểm tra giả thiết và theo dõi ví dụ tính toán.",
    "question": "Vì sao cần giữ trọng số cũ khi tính gradient tầng ẩn?",
    "answer": "Để các đạo hàm cùng mô tả hàm mất mát tại một bộ tham số."
  },
  "tich-chap-cnn": {
    "name": "Tích chập trong CNN",
    "aliases": [
      "tích chập CNN"
    ],
    "definition": "Phép áp dụng cùng bộ lọc lên các vùng cục bộ của đầu vào. Trong các thư viện học sâu, phép tính thường là tương quan chéo, dùng bộ lọc theo thứ tự được lưu.",
    "example": "Một bộ lọc hai chiều trượt qua ảnh cho một bản đồ đặc trưng.",
    "use": "Đọc mô hình, kiểm tra giả thiết và theo dõi ví dụ tính toán.",
    "question": "Vì sao chia sẻ trọng số giảm số tham số?",
    "answer": "Mọi vị trí không gian sử dụng lại cùng bộ lọc."
  },
  "attention": {
    "name": "Attention",
    "aliases": [
      "scaled dot-product attention"
    ],
    "definition": "Phép kết hợp các vector giá trị bằng trọng số tính từ độ phù hợp giữa truy vấn và các khóa. Softmax chuẩn hóa điểm trên các vị trí được phép.",
    "example": "Mặt nạ nhân quả bỏ đóng góp của những vị trí tương lai.",
    "use": "Đọc mô hình, kiểm tra giả thiết và theo dõi ví dụ tính toán.",
    "question": "Sau khi che vị trí thứ hai trong ví dụ hai khóa, trọng số của nó bằng bao nhiêu?",
    "answer": "Bằng 0."
  },
  "td-learning": {
    "name": "Học sai số thời gian",
    "aliases": [
      "TD(0)",
      "học sai số thời gian"
    ],
    "definition": "Phương pháp cập nhật giá trị từ thưởng một bước cộng với giá trị ước lượng ở trạng thái kế tiếp. Mục tiêu sử dụng chính ước lượng đang học.",
    "example": "TD có thể cập nhật trước khi một đoạn trải nghiệm kết thúc.",
    "use": "Đọc mô hình, kiểm tra giả thiết và theo dõi ví dụ tính toán.",
    "question": "Giá trị tiếp tục tại trạng thái kết thúc bằng bao nhiêu trong quy ước kết thúc?",
    "answer": "Bằng 0."
  },
  "q-learning": {
    "name": "Q-learning",
    "aliases": [
      "Q-learning"
    ],
    "definition": "Thuật toán cập nhật giá trị hành động theo mục tiêu gồm thưởng một bước và giá trị lớn nhất của các hành động ở trạng thái kế tiếp.",
    "example": "Hành động tạo dữ liệu có thể ngẫu nhiên trong khi mục tiêu cập nhật vẫn tham lam.",
    "use": "Đọc mô hình, kiểm tra giả thiết và theo dõi ví dụ tính toán.",
    "question": "Điểm nào làm Q-learning là off-policy?",
    "answer": "Mục tiêu dùng hành động tham lam dù hành động được thực hiện có thể theo chính sách khác."
  }
}

export const decisionWikiDetails = {
  "mdp": "Mô hình ra quyết định tuần tự gồm trạng thái, hành động, xác suất chuyển và phần thưởng. Phân phối bước tiếp theo chỉ phụ thuộc trạng thái và hành động hiện tại khi đã biết đủ thông tin trong trạng thái.\n\nRobot chọn đi lên nhưng có thể trượt sang hai bên. Mô hình phải ghi xác suất từng kết quả và cách nhận thưởng.\n\nBiết tọa độ đã đủ tính Markov cho robot có pin chưa?\n\nChưa đủ nếu mức pin ảnh hưởng bước chuyển hoặc hành động khả dụng. Có thể cần thêm mức pin vào trạng thái.",
  "chinh-sach-mdp": "Quy tắc chọn hành động theo trạng thái. Với chân trời hữu hạn, quy tắc có thể phụ thuộc thời gian còn lại. Trong MDP hữu hạn có thưởng bị chặn và chiết khấu nhỏ hơn 1, tồn tại chính sách tối ưu tất định không phụ thuộc thời điểm.\n\nỞ một ô lưới, chính sách chỉ định đi lên. Khi bị trượt sang ô khác, tác tử tra chính sách tại ô mới.\n\nMột dãy hành động có mô tả đủ chính sách không?\n\nTrong môi trường ngẫu nhiên, cần chỉ định hành động cả ở các trạng thái phát sinh do kết quả khác dự kiến.",
  "bellman": "Quan hệ đệ quy tách lợi ích thành thưởng tức thời và lợi ích tiếp tục. Với chính sách cố định ta lấy kỳ vọng theo hành động đó. Khi tối ưu, ta so sánh kỳ vọng của mọi hành động khả dụng.\n\nỞ lại nhận 1 và trở về chính nó. Với chiết khấu 0,9, giá trị của chính sách luôn ở lại thỏa v = 1 + 0,9v, nên v = 10.\n\nKhi tính kỳ vọng có nhân chiết khấu cho thưởng tức thời không?\n\nTrong quy ước thưởng trên cạnh hiện tại, thưởng đó có trọng số 1. Chiết khấu nhân với giá trị tiếp tục ở bước sau.",
  "ontology": "Đặc tả các lớp đối tượng, cá thể, quan hệ và tiên đề của một miền tri thức. Phân cấp lớp là một phần của ontology. Ngữ nghĩa của từng loại cạnh quyết định các suy luận được phép.\n\nBuster thuộc lớp Chó và Chó là lớp con của Thú thì Buster thuộc Thú. Cạnh một động cơ là bộ phận của ô tô cần quy tắc khác.\n\nCó thể dùng cùng một quy tắc cho mọi cạnh đồ thị không?\n\nPhải kiểm tra loại cạnh và tiên đề đi kèm. Quan hệ lớp con và quan hệ bộ phận mang nghĩa khác nhau.",
  "dau-cat-prolog": "Mục tiêu đặc biệt viết bằng dấu chấm than. Khi được thực thi, nó bỏ các lựa chọn thay thế của lời gọi vị từ hiện hành và các lựa chọn đã sinh bởi mục tiêu bên trái trong mệnh đề đó.\n\nTrong p(X) :- a(C), !, b(C,X), dấu cắt bỏ các cách chọn C khác của a/1. Các đáp án tiếp theo của b/2 vẫn có thể được tìm.\n\nDấu cắt có xóa lựa chọn của mọi lời gọi tổ tiên không?\n\nKhông. Phạm vi được xác định bởi lời gọi vị từ chứa dấu cắt.",
  "naive-bayes": "Mô hình phân lớp sinh dùng giả thiết các đặc trưng độc lập có điều kiện khi đã biết nhãn. Điểm mỗi nhãn bằng tiên nghiệm nhân với các likelihood thành phần.\n\nHai từ có thể tương quan trong toàn tập dữ liệu dù độc lập sau khi biết nhãn.\n\nGiả thiết độc lập được áp dụng trước hay sau khi biết nhãn?\n\nSau khi biết nhãn.",
  "lam-tron-laplace": "Ước lượng xác suất bằng cách cộng số đếm giả cho mọi giá trị trong miền. Khi cộng alpha cho K giá trị, mẫu số tăng alpha nhân K.\n\nBa số đếm 3, 2, 0 thành 4, 3, 1 khi alpha bằng 1.\n\nVì sao mẫu số phải tăng cho tất cả giá trị?\n\nĐể các xác suất sau làm trơn vẫn cộng thành 1.",
  "perceptron": "Bộ phân lớp tuyến tính cập nhật trọng số theo mẫu bị phân loại sai. Định lý hội tụ yêu cầu dữ liệu phân tách tuyến tính và quy tắc cập nhật phù hợp.\n\nAND có thể tách tuyến tính, XOR không thể tách bằng một đường thẳng.\n\nCó bảo đảm hội tụ trên XOR không?\n\nMột Perceptron tuyến tính không có đường phân chia thực hiện đúng bảng XOR.",
  "lan-truyen-nguoc": "Thuật toán tính gradient của mất mát theo tham số bằng quy tắc chuỗi, truyền đạo hàm từ đầu ra về các phép tính trước đó.\n\nGradient ở nút ẩn dùng các trọng số của cùng lượt lan truyền thuận trước khi cập nhật.\n\nVì sao cần giữ trọng số cũ khi tính gradient tầng ẩn?\n\nĐể các đạo hàm cùng mô tả hàm mất mát tại một bộ tham số.",
  "tich-chap-cnn": "Phép áp dụng cùng bộ lọc lên các vùng cục bộ của đầu vào. Trong các thư viện học sâu, phép tính thường là tương quan chéo, dùng bộ lọc theo thứ tự được lưu.\n\nMột bộ lọc hai chiều trượt qua ảnh cho một bản đồ đặc trưng.\n\nVì sao chia sẻ trọng số giảm số tham số?\n\nMọi vị trí không gian sử dụng lại cùng bộ lọc.",
  "attention": "Phép kết hợp các vector giá trị bằng trọng số tính từ độ phù hợp giữa truy vấn và các khóa. Softmax chuẩn hóa điểm trên các vị trí được phép.\n\nMặt nạ nhân quả bỏ đóng góp của những vị trí tương lai.\n\nSau khi che vị trí thứ hai trong ví dụ hai khóa, trọng số của nó bằng bao nhiêu?\n\nBằng 0.",
  "td-learning": "Phương pháp cập nhật giá trị từ thưởng một bước cộng với giá trị ước lượng ở trạng thái kế tiếp. Mục tiêu sử dụng chính ước lượng đang học.\n\nTD có thể cập nhật trước khi một đoạn trải nghiệm kết thúc.\n\nGiá trị tiếp tục tại trạng thái kết thúc bằng bao nhiêu trong quy ước kết thúc?\n\nBằng 0.",
  "q-learning": "Thuật toán cập nhật giá trị hành động theo mục tiêu gồm thưởng một bước và giá trị lớn nhất của các hành động ở trạng thái kế tiếp.\n\nHành động tạo dữ liệu có thể ngẫu nhiên trong khi mục tiêu cập nhật vẫn tham lam.\n\nĐiểm nào làm Q-learning là off-policy?\n\nMục tiêu dùng hành động tham lam dù hành động được thực hiện có thể theo chính sách khác."
}
