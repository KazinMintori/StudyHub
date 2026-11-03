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
  }
}

export const decisionWikiDetails = {
  "mdp": "Mô hình ra quyết định tuần tự gồm trạng thái, hành động, xác suất chuyển và phần thưởng. Phân phối bước tiếp theo chỉ phụ thuộc trạng thái và hành động hiện tại khi đã biết đủ thông tin trong trạng thái.\n\nRobot chọn đi lên nhưng có thể trượt sang hai bên. Mô hình phải ghi xác suất từng kết quả và cách nhận thưởng.\n\nBiết tọa độ đã đủ tính Markov cho robot có pin chưa?\n\nChưa đủ nếu mức pin ảnh hưởng bước chuyển hoặc hành động khả dụng. Có thể cần thêm mức pin vào trạng thái.",
  "chinh-sach-mdp": "Quy tắc chọn hành động theo trạng thái. Với chân trời hữu hạn, quy tắc có thể phụ thuộc thời gian còn lại. Trong MDP hữu hạn có thưởng bị chặn và chiết khấu nhỏ hơn 1, tồn tại chính sách tối ưu tất định không phụ thuộc thời điểm.\n\nỞ một ô lưới, chính sách chỉ định đi lên. Khi bị trượt sang ô khác, tác tử tra chính sách tại ô mới.\n\nMột dãy hành động có mô tả đủ chính sách không?\n\nTrong môi trường ngẫu nhiên, cần chỉ định hành động cả ở các trạng thái phát sinh do kết quả khác dự kiến.",
  "bellman": "Quan hệ đệ quy tách lợi ích thành thưởng tức thời và lợi ích tiếp tục. Với chính sách cố định ta lấy kỳ vọng theo hành động đó. Khi tối ưu, ta so sánh kỳ vọng của mọi hành động khả dụng.\n\nỞ lại nhận 1 và trở về chính nó. Với chiết khấu 0,9, giá trị của chính sách luôn ở lại thỏa v = 1 + 0,9v, nên v = 10.\n\nKhi tính kỳ vọng có nhân chiết khấu cho thưởng tức thời không?\n\nTrong quy ước thưởng trên cạnh hiện tại, thưởng đó có trọng số 1. Chiết khấu nhân với giá trị tiếp tục ở bước sau.",
  "ontology": "Đặc tả các lớp đối tượng, cá thể, quan hệ và tiên đề của một miền tri thức. Phân cấp lớp là một phần của ontology. Ngữ nghĩa của từng loại cạnh quyết định các suy luận được phép.\n\nBuster thuộc lớp Chó và Chó là lớp con của Thú thì Buster thuộc Thú. Cạnh một động cơ là bộ phận của ô tô cần quy tắc khác.\n\nCó thể dùng cùng một quy tắc cho mọi cạnh đồ thị không?\n\nPhải kiểm tra loại cạnh và tiên đề đi kèm. Quan hệ lớp con và quan hệ bộ phận mang nghĩa khác nhau.",
  "dau-cat-prolog": "Mục tiêu đặc biệt viết bằng dấu chấm than. Khi được thực thi, nó bỏ các lựa chọn thay thế của lời gọi vị từ hiện hành và các lựa chọn đã sinh bởi mục tiêu bên trái trong mệnh đề đó.\n\nTrong p(X) :- a(C), !, b(C,X), dấu cắt bỏ các cách chọn C khác của a/1. Các đáp án tiếp theo của b/2 vẫn có thể được tìm.\n\nDấu cắt có xóa lựa chọn của mọi lời gọi tổ tiên không?\n\nKhông. Phạm vi được xác định bởi lời gọi vị từ chứa dấu cắt."
}
