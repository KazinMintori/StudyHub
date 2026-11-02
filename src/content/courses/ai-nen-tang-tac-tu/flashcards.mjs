const course = 'ai-nen-tang-tac-tu'
const logic = '05-menh-de-va-suy-dien'
const relations = '15-ca-the-va-quan-he'

export const flashcards = [
  { course, lesson: logic, q: 'Hệ quả logic và một thủ tục suy diễn khác nhau thế nào?', a: 'Hệ quả logic là quan hệ ngữ nghĩa: Kết luận đúng trong mọi mô hình của cơ sở tri thức. Thủ tục suy diễn là cách thao tác trên biểu thức để tìm chứng minh. Tính đúng đắn bảo đảm kết luận tìm được là hệ quả logic; tính đầy đủ bảo đảm tìm được mọi hệ quả trong phạm vi đã nêu.' },
  { course, lesson: logic, q: 'Một mệnh đề xác định gồm những thành phần nào?', a: 'Gồm một nguyên tử ở đầu và một hội các nguyên tử ở thân, đọc là đầu đúng nếu mọi nguyên tử trong thân đúng. Thân rỗng tạo thành một sự kiện. Mệnh đề tương đương một tuyển chứa đúng một literal dương.' },
  { course, lesson: logic, q: 'Không chứng minh được một nguyên tử có đồng nghĩa với chứng minh phủ định của nó không?', a: 'Không. Trong ngữ nghĩa thông thường, một nguyên tử có thể đúng ở mô hình này và sai ở mô hình khác. Muốn dùng sự thất bại của chứng minh để kết luận phủ định, phải nêu rõ giả định tri thức đầy đủ và các điều kiện của thủ tục tìm kiếm.' },
  { course, lesson: logic, q: 'Suy luận chẩn đoán bằng giả thuyết cần thỏa điều kiện nào?', a: 'Các giả thuyết cùng với tri thức nền phải giải thích được quan sát và không dẫn đến mâu thuẫn. Tính tối thiểu thường được xét theo quan hệ bao hàm tập hợp, không tự động có nghĩa là ít giả thuyết nhất.' },
  { course, lesson: relations, q: 'Hằng ký hiệu và cá thể mà nó biểu thị có phải cùng một đối tượng không?', a: 'Không. Hằng là một ký hiệu của ngôn ngữ. Phép diễn giải ánh xạ hằng đó tới một cá thể trong miền. Hai hằng khác nhau vẫn có thể biểu thị cùng một cá thể nếu không giả định tên duy nhất.' },
  { course, lesson: relations, q: 'Một biểu thức không biến (ground) có đặc điểm gì?', a: 'Biểu thức không chứa biến logic. Một thể hiện không biến thu được bằng cách thay nhất quán mọi biến trong biểu thức bằng các hạng không biến.' },
  { course, lesson: relations, q: 'Phép thế tác động thế nào khi một biến xuất hiện nhiều lần?', a: 'Mọi lần xuất hiện của biến đó đều được thay bằng cùng một hạng. Phép áp dụng là đồng thời, không tự động áp dụng lại phép thế bên trong hạng vừa thay vào.' },
  { course, lesson: relations, q: 'Một phép hợp nhất tổng quát nhất bảo đảm điều gì?', a: 'Nó làm hai biểu thức trở nên giống hệt nhau và giữ lại mức tổng quát lớn nhất. Mọi phép hợp nhất khác đều có thể thu được bằng cách áp dụng thêm một phép thế vào kết quả tổng quát nhất, trong phạm vi các biến đang xét.' }
]
