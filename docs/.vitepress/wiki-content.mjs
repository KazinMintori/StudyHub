import { physicsConceptIds, physicsWikiDetails, physicsWikiConnections } from './physics-foundations.mjs'
import { formatWikiMath } from '../../scripts/wiki-math.mjs'
import { concepts } from './concepts.mjs'

import { mathAiWikiDetails } from './math-ai-foundations.mjs'
export const wikiGroups = [
  { id:'optimization', name:'Tối ưu hóa', ids:['hessian','ma-tran-psd','he-phuong-trinh','binh-phuong-toi-thieu','tham-so-toan-hoc','tap-loi','ham-loi','mien-kha-thi','infimum','epigraph','noi-long-toi-uu','lagrangian','ham-doi-ngau','doi-ngau-manh','dieu-kien-slater','kkt','tap-affine','noi-tuong-doi','non-loi','sieu-phang','ellipsoid','da-dien','non-doi-ngau','sieu-phang-phan-tach','bat-dang-thuc-tong-quat','tap-muc-duoi','bat-dang-thuc-jensen','log-sum-exp','cuc-tieu-cuc-bo','phep-chieu','bai-toan-tuong-duong','ham-tua-loi','quy-hoach-tuyen-tinh','quy-hoach-toan-phuong','quy-hoach-non-bac-hai','quy-hoach-nua-xac-dinh','quy-hoach-hinh-hoc','phan-bu-schur','toi-uu-pareto','dieu-chuan'] },
  { id:'optimization-algorithms', name:'Thuật toán tối ưu', ids:['tim-kiem-duong','tu-tuong-hop','gradient-ngau-nhien','momentum-nesterov','adagrad','rmsprop','adam','gradient-lien-hop','bfgs'] },
  { id:'planning', name:'Quy hoạch', ids:['nghiem-co-so','quy-hoach-dong'] },
  { id:'discrete-math', name:'Logic & toán rời rạc', ids:['tap-hop','ham-so','menh-de','luong-tu','quy-nap','to-hop','quan-he'] },
  { id:'algorithms', name:'Giải thuật & cấu trúc dữ liệu', ids:['do-thi','cay','trang-thai','hang-doi','ngan-xep','hang-doi-uu-tien','do-phuc-tap','heuristic','mang','con-tro','de-quy','bam'] },
  { id:'mathematics', name:'Đại số & giải tích', ids:['vector','ma-tran','tich-vo-huong','chuan','gioi-han','do-thi-ham-so','dao-ham','dao-ham-rieng','gradient','tich-phan','quy-tac-chuoi','tri-rieng','to-hop-loi'] },
  { id:'probability', name:'Xác suất & thống kê', ids:['khong-gian-mau','xac-suat-co-dieu-kien','doc-lap','bien-ngau-nhien','ky-vong','phuong-sai','phan-phoi-gauss','ma-tran-hiep-phuong-sai','likelihood','mau-tong-the','thong-ke-mo-ta','suy-rong-thong-ke','ket-luan-nhan-qua','du-doan-thong-ke'] },
  { id:'programming', name:'Python & dữ liệu', ids:['bien-kieu','list','dictionary','ham-lap-trinh','tham-so-lap-trinh','vong-lap','chi-muc','vector-hoa','broadcasting','gia-tri-thieu'] },
  { id:'physics', name:'Cơ học, nhiệt, điện từ và lượng tử', ids:['dien-tich','luc','cong-nang-luong','dien-the','thong-luong','don-vi','song',...physicsConceptIds] },
  { id:'distributed', name:'Tính toán phân tán', ids:['khoa-gia-tri','phan-tan','ket-hop'] }
]

export const courseWikiScopes = {
  'vat-ly-1':['physics','mathematics','probability'],
  'toan-cho-ai':['optimization','optimization-algorithms','planning','mathematics','probability','discrete-math','algorithms'],
  'xu-ly-du-lieu':['programming','probability','mathematics','discrete-math'],
  'xac-suat-thong-ke':['probability','mathematics','discrete-math'],
  'vat-ly-2':['physics','mathematics','probability'],
  'bieu-dien-tri-thuc':['discrete-math','algorithms','probability','mathematics'],
  'giai-thuat-du-lieu':['distributed','algorithms','mathematics','probability','programming'],
  dsa:['algorithms','discrete-math','programming','mathematics'],
  'discrete-math':['discrete-math','algorithms','mathematics']
}

export function conceptField(id) {
  const group = wikiGroups.find(group => group.ids.includes(id))
  return group ? { id: group.id, name: group.name } : { id: 'other', name: 'Khái niệm liên ngành' }
}

export function resolveConceptForCourse(ids, courseId) {
  const unique = [...new Set(ids)]
  if (!courseId) return unique.length === 1 ? unique[0] : null
  const scopes = courseWikiScopes[courseId] || []
  return unique
    .map(id => ({ id, rank: scopes.indexOf(conceptField(id).id) }))
    .filter(item => item.rank >= 0)
    .sort((a, b) => a.rank - b.rank)[0]?.id || null
}
const connections = {
  ...physicsWikiConnections,
  'thong-ke-mo-ta':['mau-tong-the','suy-rong-thong-ke'],
  'suy-rong-thong-ke':['mau-tong-the','thong-ke-mo-ta','ket-luan-nhan-qua'],
  'ket-luan-nhan-qua':['thong-ke-mo-ta','du-doan-thong-ke'],
  'du-doan-thong-ke':['thong-ke-mo-ta','suy-rong-thong-ke','ket-luan-nhan-qua'],
  'tap-affine':['tap-loi', 'he-phuong-trinh', 'vector'],
  'noi-tuong-doi':['tap-affine', 'tap-loi', 'dieu-kien-slater'],
  'non-loi':['tap-loi', 'ma-tran-psd', 'non-doi-ngau'],
  'sieu-phang':['tich-vo-huong', 'sieu-phang-phan-tach', 'da-dien'],
  'ellipsoid':['ma-tran-psd', 'tri-rieng', 'phan-phoi-gauss'],
  'da-dien':['sieu-phang', 'tap-loi', 'nghiem-co-so'],
  'non-doi-ngau':['non-loi', 'bat-dang-thuc-tong-quat', 'ham-doi-ngau'],
  'sieu-phang-phan-tach':['sieu-phang', 'tap-loi', 'epigraph'],
  'bat-dang-thuc-tong-quat':['non-loi', 'non-doi-ngau', 'ma-tran-psd'],
  'tap-muc-duoi':['ham-loi', 'epigraph', 'tap-loi'],
  'bat-dang-thuc-jensen':['ham-loi', 'ky-vong', 'phuong-sai'],
  'log-sum-exp':['ham-loi', 'hessian', 'phuong-sai'],
  'cuc-tieu-cuc-bo':['ham-loi', 'mien-kha-thi', 'gradient'],
  'phep-chieu':['tap-loi', 'gradient', 'chuan'],
  'bai-toan-tuong-duong':['epigraph', 'mien-kha-thi', 'ham-loi'],
  'ham-tua-loi':['tap-muc-duoi', 'ham-loi', 'quy-hoach-tuyen-tinh'],
  'quy-hoach-tuyen-tinh':['da-dien', 'nghiem-co-so', 'quy-hoach-toan-phuong'],
  'quy-hoach-toan-phuong':['quy-hoach-tuyen-tinh', 'ma-tran-psd', 'binh-phuong-toi-thieu'],
  'quy-hoach-non-bac-hai':['non-loi', 'quy-hoach-toan-phuong', 'quy-hoach-nua-xac-dinh'],
  'quy-hoach-nua-xac-dinh':['ma-tran-psd', 'phan-bu-schur', 'bat-dang-thuc-tong-quat'],
  'quy-hoach-hinh-hoc':['log-sum-exp', 'bai-toan-tuong-duong', 'ham-loi'],
  'phan-bu-schur':['ma-tran-psd', 'quy-hoach-nua-xac-dinh', 'quy-hoach-non-bac-hai'],
  'toi-uu-pareto':['non-doi-ngau', 'sieu-phang-phan-tach', 'dieu-chuan'],
  'dieu-chuan':['binh-phuong-toi-thieu', 'toi-uu-pareto', 'quy-hoach-toan-phuong'],
  hessian:['gradient','ma-tran-psd','tri-rieng','ma-tran'],
  'ma-tran-psd':['ma-tran','tri-rieng','hessian'],
  'he-phuong-trinh':['ma-tran','vector','hessian'],
  'tap-loi':['to-hop-loi','ham-loi','tap-hop'],
  'ham-loi':['tap-loi','gradient','hessian'],
  kkt:['gradient','ham-loi','he-phuong-trinh'],
  'binh-phuong-toi-thieu':['ma-tran','gradient','phan-phoi-gauss','likelihood'],
  'tham-so-toan-hoc':['ham-so','gradient','mien-kha-thi'],
  'phan-phoi-gauss':['ky-vong','phuong-sai','ma-tran-hiep-phuong-sai','likelihood'],
  'ma-tran-hiep-phuong-sai':['phuong-sai','ma-tran-psd','phan-phoi-gauss'],
  likelihood:['phan-phoi-gauss','binh-phuong-toi-thieu','xac-suat-co-dieu-kien'],
  'mien-kha-thi':['tap-loi','infimum','kkt'],
  infimum:['mien-kha-thi','noi-long-toi-uu','ham-doi-ngau'],
  epigraph:['ham-loi','tap-loi','noi-long-toi-uu'],
  'noi-long-toi-uu':['mien-kha-thi','infimum','doi-ngau-manh'],
  lagrangian:['mien-kha-thi','ham-doi-ngau','kkt'],
  'ham-doi-ngau':['lagrangian','doi-ngau-manh','dieu-kien-slater'],
  'doi-ngau-manh':['ham-doi-ngau','dieu-kien-slater','kkt'],
  'dieu-kien-slater':['tap-loi','doi-ngau-manh','kkt'],
  'tim-kiem-duong':['gradient','hessian','tu-tuong-hop'],
  'tu-tuong-hop':['hessian','tim-kiem-duong','kkt'],
  'gradient-ngau-nhien':['gradient','ky-vong','phuong-sai','momentum-nesterov'],
  'momentum-nesterov':['gradient-ngau-nhien','gradient','adam'],
  adagrad:['gradient-ngau-nhien','rmsprop','adam'],
  rmsprop:['adagrad','adam','phuong-sai'],
  adam:['gradient-ngau-nhien','momentum-nesterov','rmsprop'],
  'gradient-lien-hop':['hessian','he-phuong-trinh','bfgs'],
  bfgs:['gradient','hessian','tim-kiem-duong'],
  'nghiem-co-so':['he-phuong-trinh','tap-loi','mien-kha-thi'],
  'quy-hoach-dong':['do-thi','trang-thai','nghiem-co-so'],
  gradient:['dao-ham-rieng','vector','dao-ham','chuan','dien-the'],
  'dao-ham-rieng':['dao-ham','gradient','quy-tac-chuoi','ham-so'],
  'dao-ham':['gioi-han','ham-so','gradient','tich-phan','quy-tac-chuoi'],
  'do-thi-ham-so':['ham-so','dao-ham','ham-loi','epigraph'],
  'dien-the':['cong-nang-luong','dien-tich','gradient','tich-phan'],
  'do-thi':['cay','trang-thai','hang-doi','ngan-xep'],
  heuristic:['trang-thai','hang-doi-uu-tien','do-thi','do-phuc-tap'],
  'de-quy':['ngan-xep','quy-nap','cay','do-phuc-tap'],
  'hang-doi':['ngan-xep','do-thi','trang-thai'],
  'ngan-xep':['hang-doi','de-quy','cay'],
  'hang-doi-uu-tien':['hang-doi','heuristic','do-phuc-tap'],
  broadcasting:['mang','vector-hoa','ma-tran','chi-muc'],
  'vector-hoa':['mang','broadcasting','vong-lap','bien-kieu'],
  'dictionary':['bam','khoa-gia-tri','list'],
  'tham-so-lap-trinh':['ham-lap-trinh','bien-kieu','list'],
  'phan-tan':['khoa-gia-tri','ket-hop','do-phuc-tap','bam'],
  'khoa-gia-tri':['dictionary','bam','phan-tan'],
  'ket-hop':['phan-tan','ham-lap-trinh','ky-vong'],
  'xac-suat-co-dieu-kien':['khong-gian-mau','doc-lap','bien-ngau-nhien'],
  'phuong-sai':['ky-vong','bien-ngau-nhien','mau-tong-the'],
  'ky-vong':['bien-ngau-nhien','phuong-sai','tich-phan'],
  'thong-luong':['tich-vo-huong','tich-phan','dien-tich','vector'],
  'cong-nang-luong':['luc','tich-vo-huong','dien-the'],
  'to-hop-loi':['vector','tap-hop','ham-so'],
  'tri-rieng':['ma-tran','vector','chuan']
}
export function relatedConcepts(id) {
  if(connections[id])return connections[id]
  const group=wikiGroups.find(group=>group.ids.includes(id))
  const index=group.ids.indexOf(id)
  return [...new Set([group.ids[(index+1)%group.ids.length],group.ids[(index+group.ids.length-1)%group.ids.length],group.ids[0]])].filter(other=>other!==id)
}
export const wikiDetails = {
  ...physicsWikiDetails,
  ...mathAiWikiDetails,
  'thong-ke-mo-ta':'**Giữ đúng phạm vi quan sát.** Khi một khảo sát có 10 người trả lời và 7 người chưa từng lập trình, tỷ lệ trong nhóm trả lời là $7/10=70\\%$. Đây là ví dụ giả định. Một câu mô tả đúng phải nói rõ mẫu số ứng với nhóm đã trả lời. Thay nhóm ấy bằng toàn trường là một bước suy rộng cần căn cứ riêng.\n\nMô tả không chỉ gồm phép tính: bảng, biểu đồ và lời văn đều có thể mô tả dữ liệu.',
  'suy-rong-thong-ke':'**Tập đối tượng trong kết luận rộng hơn tập đã quan sát.** Cùng con số 70%, câu về người trả lời khảo sát là mô tả, còn câu về toàn bộ sinh viên của trường là suy rộng. Muốn đánh giá kết luận sau, cần biết cách chọn mẫu, nhóm nào có cơ hội tham gia và ai được mời nhưng không trả lời.\n\nMột mẫu lớn vẫn có thể khác tổng thể một cách có hệ thống. Nhận diện phát biểu là suy rộng không chứng minh rằng bước suy rộng hợp lệ, và cũng không có nghĩa mọi bước suy rộng đều sai.',
  'ket-luan-nhan-qua':'**Phân biệt quan sát với can thiệp.** Nếu người tham gia câu lạc bộ có điểm cao hơn, dữ liệu mô tả khác biệt giữa các nhóm. Để nói việc tham gia làm điểm tăng, cần căn cứ về tác động của thay đổi này, thay vì chỉ dựa vào khác biệt đã thấy. Những người tham gia có thể đã có nhiều kinh nghiệm hơn từ trước.\n\nThí nghiệm ngẫu nhiên có đối chứng phân người tham gia ngẫu nhiên vào các nhóm để so sánh nhóm nhận can thiệp với nhóm đối chứng. Cách phân nhóm giúp hạn chế việc khác biệt có sẵn quyết định ai nhận can thiệp. Kết luận vẫn cần đi cùng thiết kế, cách đo và phạm vi nghiên cứu.',
  'du-doan-thong-ke':'**Đã biết thông tin đầu vào, chưa biết giá trị cần đoán.** Dùng kinh nghiệm lập trình để đoán điểm bài thực hành chưa công bố là dự đoán, dù bài đã được chấm. Dự đoán không bắt buộc phải nói về tương lai.\n\nKhả năng dự đoán và khả năng giải thích nhân quả là hai vấn đề khác nhau. Một thông tin có thể giúp đoán kết quả mà không phải yếu tố có thể can thiệp để tạo ra kết quả ấy.',
  'tap-hop':'**Quan hệ giữa các tập.** A là tập con của B khi mọi phần tử của A cũng thuộc B, ký hiệu A ⊆ B. Hai tập bằng nhau khi chúng chứa cùng các phần tử, không phụ thuộc thứ tự viết. Khi dùng phép bù, phải nêu tập vũ trụ đang xét.\n\nĐừng nhầm phần tử x với tập chỉ chứa x: x và {x} là hai đối tượng khác nhau. Khái niệm tập hợp được dùng để định nghĩa quan hệ, miền xác định của hàm số và không gian mẫu.',
  'ham-so':"**Đơn ánh, toàn ánh và hàm ngược.** Đơn ánh nghĩa là hai đầu vào khác nhau cho hai đầu ra khác nhau. Toàn ánh lên tập B nghĩa là mọi phần tử của B đều là đầu ra của ít nhất một đầu vào. Song ánh thỏa cả hai và có hàm ngược trên B.\n\nVí dụ $f(x)=x^{2}$ trên số thực không đơn ánh vì $f(2)=f(-2)$. Thu hẹp miền về $x\\ge 0$ làm hàm đơn ánh. Luôn nêu miền xét trước khi kết luận về hàm số.",
  'menh-de':"**Bảng chân trị.** Có thể liệt kê mọi tổ hợp đúng/sai của các mệnh đề thành phần để kiểm tra một biểu thức. Với n biến Boolean, bảng có $2^n$ dòng. Hai biểu thức tương đương khi có cùng giá trị ở mọi dòng.\n\nLuật De Morgan: $\\neg (p\\land q)$ tương đương $\\neg p\\lor \\neg q$. $\\neg (p\\lor q)$ tương đương $\\neg p\\land \\neg q$. Phép kéo theo $p\\to q$ tương đương $\\neg p\\lor q$, không tương đương $q\\to p$.",
  'luong-tu':"**Thứ tự lượng từ có thể đổi ý nghĩa.** $\\forall x\\exists y P(x,y)$ cho phép chọn y khác nhau theo từng x. $\\exists y\\forall x P(x,y)$ yêu cầu một y duy nhất dùng được cho mọi x.\n\nVí dụ “mọi sinh viên có một người hướng dẫn” không đồng nghĩa “có một người hướng dẫn tất cả sinh viên”. Khi phủ định lượng từ, đổi loại lượng từ và phủ định vị từ bên trong.",
  'quy-nap':"**Giả thiết quy nạp không phải kết luận đã chứng minh.** Nó chỉ được dùng trong bước suy diễn để đi từ k tới $k+1$. Quy nạp mạnh cho phép giả sử mọi trường hợp từ $n_{0}$ đến k đúng.\n\nCách này hữu ích với đệ quy có nhiều bài toán con. Trước khi áp dụng, kiểm tra mọi bài toán con đều nhỏ hơn bài toán hiện tại và các trường hợp cơ sở đã đủ.",
  'do-thi':"**Biểu diễn đồ thị.** Danh sách kề lưu láng giềng của từng đỉnh và thường cần $O(|V|+|E|)$ bộ nhớ. Ma trận kề dùng bảng |$V|\\times |V|$, thuận tiện kiểm tra cạnh nhưng cần $O(|V|^{2})$ bộ nhớ.\n\nBFS và DFS duyệt danh sách kề trong $O(|V|+|E|)$ nếu mỗi đỉnh chỉ được xử lý một lần. Một đường đi ngắn nhất theo số cạnh có thể khác đường có tổng trọng số nhỏ nhất.",
  cay:'**Chiều cao và thứ tự.** Chiều cao đo đường dài nhất từ gốc tới lá theo quy ước đã chọn. Với cây nhị phân tìm kiếm có khóa phân biệt, mọi khóa bên trái nhỏ hơn khóa gốc và bên phải lớn hơn. Quy tắc này phải đúng ở mọi cây con.\n\nCây nhị phân thông thường không bắt buộc có quy tắc tìm kiếm. Cây lệch có chiều cao gần n, nên các thao tác phụ thuộc chiều cao có thể tốn O(n).',
  'trang-thai':'**Đủ thông tin cho tương lai.** Hai lịch sử khác nhau có thể gom thành cùng trạng thái nếu chúng cho cùng các hành động hợp lệ, chi phí và kết quả tương lai liên quan. Nếu lịch sử làm thay đổi lựa chọn tiếp theo, phải đưa thông tin đó vào trạng thái.\n\nTrong tìm kiếm trên đồ thị, nút thường chứa trạng thái cùng đường đi, nút cha và chi phí đã đi. So sánh trạng thái để tránh lặp khác với lưu nút để tái tạo lời giải.',
  'hang-doi':'**Chi phí cài đặt.** Hàng đợi có thể dùng danh sách liên kết hoặc vùng nhớ vòng. Trong mô hình thích hợp, thêm cuối và lấy đầu đều tốn O(1). Xóa phần tử đầu của một mảng bằng cách dịch toàn bộ phần còn lại có thể tốn O(n).\n\nĐây là lý do cần phân biệt cấu trúc trừu tượng hàng đợi với một cách cài đặt cụ thể. Quy tắc FIFO quyết định thứ tự duyệt BFS.',
  'ngan-xep':'**Ngăn xếp lời gọi.** Khi hàm A gọi B, thông tin để tiếp tục A được giữ lại. B hoàn tất trước khi A tiếp tục, phù hợp thứ tự LIFO. Với đệ quy, mỗi lời gọi thường tạo một khung ngăn xếp mới.\n\nNgăn xếp trừu tượng không tự bảo đảm chương trình kết thúc. Điều kiện dừng của thuật toán phải được kiểm tra riêng.',
  'hang-doi-uu-tien':"**Heap không phải danh sách đã sắp xếp hoàn toàn.** Min-heap giữ khóa của nút cha không lớn hơn khóa của các con. Do đó phần tử nhỏ nhất ở gốc. Các nút ở những nhánh khác nhau không nhất thiết có thứ tự.\n\nLấy phần tử ưu tiên thường tốn O(log n), đọc phần tử nhỏ nhất thường tốn O(1). Khi cùng một trạng thái có chi phí tốt hơn, thuật toán phải cập nhật khóa hoặc xử lý bản ghi cũ phù hợp.",
  'do-phuc-tap':"**Big-O, Θ và Ω.** O là chặn trên tiệm cận. Ω là chặn dưới. Θ là chặn trên và dưới cùng bậc. Một thuật toán Θ(n) cũng thuộc $O(n^{2})$, nhưng $O(n^{2})$ là mô tả kém chặt hơn.\n\nPhải phân biệt thời gian, bộ nhớ và mô hình tính toán. O(n) không tự nghĩa là “trường hợp xấu nhất”: trường hợp đang xét cần được nêu riêng.",
  heuristic:"**Điều kiện tối ưu của A*.** Với h(goal)=0, admissible yêu cầu h không vượt chi phí tối ưu còn lại. Consistent yêu cầu $h(n)\\le c(n,n')+h(n')$ cho mỗi cạnh. Consistency giúp f không giảm dọc đường đi và cho phép đóng trạng thái thuận lợi hơn trong graph search.\n\nNếu chỉ có admissibility, một số cách cài đặt graph search phải cho phép mở lại trạng thái để giữ bảo đảm tối ưu. Một heuristic nhanh nhưng ước lượng quá cao có thể làm mất bảo đảm đó.",
  mang:'**Địa chỉ và kích thước phần tử.** Trong mảng liên tiếp, địa chỉ phần tử i bằng địa chỉ đầu cộng i lần kích thước phần tử. Công thức giải thích truy cập trực tiếp O(1), nhưng không áp dụng nguyên dạng cho mọi đối tượng dãy.\n\nMảng nhiều chiều cần shape và strides để biết cách ánh xạ chỉ mục sang bộ nhớ. Thêm phần tử giữa một mảng liên tiếp có thể phải dịch dữ liệu.',
  'con-tro':'**Sở hữu dữ liệu và vòng đời.** Con trỏ hay tham chiếu có thể cho phép nhiều tên truy cập cùng vùng dữ liệu. Cần biết ai quản lý bộ nhớ và dữ liệu còn hợp lệ bao lâu. Trong ngôn ngữ có quản lý bộ nhớ thủ công, dùng địa chỉ sau khi giải phóng là lỗi.\n\nTrong Python hoặc NumPy, tác động dễ thấy hơn là thay đổi dữ liệu dùng chung: view có thể làm mảng gốc thay đổi, trong khi copy độc lập không làm vậy.',
  'de-quy':'**Hai yêu cầu kết thúc.** Có ít nhất một trường hợp cơ sở, và mọi nhánh lời gọi phải tiến về trường hợp cơ sở. Một hàm có câu lệnh dừng nhưng nhánh khác gọi lại với cùng tham số vẫn có thể không kết thúc.\n\nĐể phân tích, viết quan hệ truy hồi của số bước và độ sâu ngăn xếp. Chứng minh bằng quy nạp thường đi cùng cấu trúc đệ quy.',
  vector:"**Thành phần phụ thuộc cơ sở.** Cùng một vector hình học có thể có bộ tọa độ khác nhau trong hai hệ cơ sở. Việc cộng và nhân vô hướng cần thống nhất cơ sở và số chiều.\n\nVector đơn vị có chuẩn bằng 1. Chuẩn hóa $v\\ne 0$ bằng $\\frac{v}{\\|v\\|}$. Không thể chuẩn hóa vector không bằng phép chia này. Vector nhiều chiều cũng có thể chỉ biểu diễn đặc trưng dữ liệu, không nhất thiết là một mũi tên trong không gian vật lý.",
  'ma-tran':"**Điều kiện nhân và thứ tự.** Nếu A có kích thước $m\\times n$ và B có kích thước $n\\times p$ thì AB có kích thước $m\\times p$, với mỗi phần tử là tích vô hướng của một hàng của A và một cột của B. Nhìn chung AB khác BA. Đôi khi BA còn không xác định.\n\nMa trận chuyển vị $A^{T}$ đổi hàng thành cột. Ma trận vuông khả nghịch có A⁻¹ sao cho $A^{-1}A=AA^{-1}=I$. Không phải mọi ma trận vuông đều khả nghịch.",
  'tich-vo-huong':"**Góc, chiếu và dấu.** Tích vô hướng dương khi góc nhỏ hơn 90°, âm khi góc lớn hơn 90°, bằng 0 khi hai vector khác 0 vuông góc. Hình chiếu vô hướng của u lên hướng đơn vị n là $u\\cdot n$.\n\nĐiều này xuất hiện trong công của lực và thông lượng: chỉ thành phần cùng hướng độ dời hoặc pháp tuyến mới đóng góp. Công thức góc cần hai vector khác 0.",
  chuan:"**Các chuẩn thường gặp.** Với vector $x=(x_1,\\ldots,x_n)$, chuẩn 1 cộng độ lớn của từng thành phần:\n\n$$\\|x\\|_1=|x_1|+\\cdots+|x_n|=\\sum_{i=1}^n|x_i|.$$\n\nChuẩn Euclid cộng các bình phương trước khi lấy căn:\n\n$$\\|x\\|_2=\\sqrt{x_1^2+\\cdots+x_n^2}=\\sqrt{\\sum_{i=1}^n x_i^2}.$$\n\nChỉ số $i$ chạy từ 1 đến $n$, qua tất cả thành phần của vector. Chuẩn vô cùng lấy độ lớn lớn nhất: $\\|x\\|_\\infty=\\max\\{|x_1|,\\ldots,|x_n|\\}$. Mỗi chuẩn tạo một cách đo khoảng cách $d(x,y)=\\|x-y\\|$.\n\nChuẩn thỏa bất đẳng thức tam giác và tính đồng nhất $\\|\\alpha x\\|=|\\alpha|\\|x\\|$. Đừng nhầm chuẩn vector với chuẩn hóa dữ liệu theo trung bình và độ lệch chuẩn.",
  'gioi-han':"**Một phía và liên tục.** Giới hạn hai phía tại a tồn tại khi giới hạn từ trái và từ phải cùng tồn tại và bằng nhau. Hàm liên tục tại a cần f(a) xác định và bằng giới hạn.\n\nHàm dấu có hai giới hạn khác nhau tại 0 nên không có giới hạn hai phía ở đó. Một hàm liên tục chưa chắc khả vi. $f(x)=|x|$ liên tục nhưng không có đạo hàm tại 0.",
  'dao-ham':"**Định nghĩa kỹ thuật.** Với hàm một biến:\n\n$$f\\prime(x)=\\lim_{h\\to0}\\frac{f(x+h)-f(x)}{h}.$$\n\nĐạo hàm tại x tồn tại khi giới hạn hữu hạn này tồn tại. Với $f(x)=|x|$ tại $x=0$, hệ số góc từ trái là −1, từ phải là 1 nên đạo hàm không tồn tại. Một điểm có đạo hàm bằng 0 chưa chắc là cực tiểu: $f(x)=x^{3}$ tại 0 là ví dụ.",
  'do-thi-ham-so':"**Đồ thị là một tập hợp.** Với $f:\\mathbb R^n\\to\\mathbb R$, đồ thị là $\\{(x,f(x)) : x\\in\\operatorname{dom} f\\}$, một tập con của $\\mathbb R^{n+1}$. Nhìn hàm như một tập hợp cho phép dùng hình học của tập hợp: hàm lồi khi đồ thị nằm dưới mọi dây cung nối hai điểm của nó, và khi khả vi thì tiếp tuyến hay siêu phẳng tiếp xúc tại mọi điểm nằm dưới đồ thị.\n\n**Đồ thị, epigraph và đường mức.** Epigraph $\\{(x,t): f(x)\\le t\\}$ gồm đồ thị và mọi điểm nằm phía trên nó. Hàm lồi khi và chỉ khi epigraph là tập lồi, trong khi bản thân đồ thị của một hàm lồi không affine thì không lồi: đồ thị của $x^2$ chứa $(-1,1)$ và $(1,1)$ nhưng không chứa trung điểm $(0,1)$. Đường mức $\\{x: f(x)=\\alpha\\}$ là hình chiếu xuống mặt phẳng nằm ngang của giao giữa đồ thị và mặt phẳng độ cao $\\alpha$, nên các đường mức là cách vẽ đồ thị của hàm hai biến trên giấy.\n\n**Không nhầm với đồ thị trong lý thuyết đồ thị.** Cùng là chữ “đồ thị”, nhưng trong lý thuyết đồ thị và trong học sâu (đồ thị tính toán), từ này chỉ một cấu trúc gồm đỉnh và cạnh, hoàn toàn khác đồ thị của một hàm số.",
  'dao-ham-rieng':"**Giữ biến khác không đổi.** $\\frac{\\partial f}{\\partial x}$ được tính bằng cách dịch x và giữ y, z… cố định. Với $f(x,y)=x^{2}y$, ta có $\\frac{\\partial f}{\\partial x}=2xy$ và $\\frac{\\partial f}{\\partial y}=x^{2}$.\n\nCó các đạo hàm riêng tại một điểm chưa tự bảo đảm hàm khả vi tại điểm đó. Điều kiện đủ thường dùng là các đạo hàm riêng liên tục trong một lân cận. Gradient tập hợp các đạo hàm riêng thành một vector.",
  gradient:"**Công thức và xấp xỉ cục bộ.** Với hàm khả vi f: $\\mathbb R^{n}\\to \\mathbb R$, gradient là:\n\n$$\\nabla f(x)=\\left(\\frac{\\partial f}{\\partial x_1},\\ldots,\\frac{\\partial f}{\\partial x_n}\\right).$$\n\nVới độ dời nhỏ $\\Delta x$, ta có $f(x+\\Delta x)\\approx f(x)+\\nabla f(x)\\cdot \\Delta x$. Đạo hàm theo hướng đơn vị u bằng $\\nabla f(x)\\cdot u$, lớn nhất khi u cùng hướng gradient nếu gradient khác 0. Khi gradient bằng 0, không có một hướng tăng nhanh nhất được xác định từ công thức này.\n\n**Gradient Descent** cập nhật x mới=x cũ−η∇f(x cũ). Hướng giảm là thông tin cục bộ. Bước $\\eta$ quá dài vẫn có thể làm f tăng. Với $f(x)=x^{2}$, x mới=$(1-2\\eta )x$ cũ: $0<\\eta <1$ làm |x| giảm, $\\eta =1$ làm đổi dấu giữ độ lớn, $\\eta >1$ có thể gây phân kỳ.",
  'tich-phan':"**Tích phân có dấu và đổi cận.** Đổi thứ tự cận làm đổi dấu. Nếu f âm trên một khoảng, phần đóng góp tích phân ở đó âm. Diện tích hình học cần xét |f|.\n\nĐịnh lý cơ bản của giải tích nối tích phân với đạo hàm: khi F là nguyên hàm phù hợp của f, $\\int_a^b f(x)\\,dx=F(b)-F(a)$. Với phân phối liên tục, tổng mật độ trên toàn miền phải bằng 1.",
  'quy-tac-chuoi':"**Nhiều đường phụ thuộc.** Nếu $z=f(x(t),y(t))$, $\\frac{dz}{dt}=\\frac{\\partial f}{\\partial x}\\frac{dx}{dt}+\\frac{\\partial f}{\\partial y}\\frac{dy}{dt}$. Mỗi đường từ t tới z đóng góp một tích các đạo hàm trên đường đó.\n\nTrong lan truyền ngược, đồ thị tính toán tổ chức những phép nhân và cộng này. Bỏ sót một nhánh phụ thuộc làm gradient sai dù công thức ở các nhánh khác đúng.",
  'tri-rieng':"**Cách tìm trị riêng.** Từ $Av=\\lambda v$ suy ra $(A-\\lambda I)v=0$. Để có nghiệm $v\\ne 0$ trong hữu hạn chiều, ma trận $A-\\lambda I$ phải suy biến. Do đó $\\det(A-\\lambda I)=0$.\n\nTrị riêng có thể là số phức với ma trận thực. Ma trận đối xứng thực có trị riêng thực và một cơ sở vector riêng trực chuẩn. Không phải mọi ma trận đều có đủ vector riêng độc lập để chéo hóa.",
  'to-hop-loi':"**Nhiều điểm và điều kiện trọng số.** Với $k$ điểm $x_1,\\ldots,x_k$, một tổ hợp lồi có dạng đầy đủ\n\n$$z=\\lambda_1x_1+\\lambda_2x_2+\\cdots+\\lambda_kx_k.$$\n\nMỗi trọng số không âm và tổng trọng số bằng 1:\n\n$$\\lambda_1+\\lambda_2+\\cdots+\\lambda_k=1,\\qquad\\lambda_i\\ge0.$$\n\nViết gọn bằng ký hiệu tổng:\n\n$$z=\\sum_{i=1}^k\\lambda_i x_i,\\qquad\\sum_{i=1}^k\\lambda_i=1.$$\n\nChỉ số $i$ chạy từ 1 đến $k$, qua các điểm đã chọn. Sau khi phạm vi đã rõ, $\\sum_i\\lambda_i=1$ là cách viết tắt cùng điều kiện. Tài liệu có thể dùng $\\theta_i$ thay cho $\\lambda_i$. Cả hai đều là tên của trọng số. Bao lồi là tập tất cả tổ hợp lồi của các điểm đã cho.\n\nVới hai điểm, điều kiện tạo đúng đoạn nối. Nếu bỏ điều kiện không âm nhưng vẫn giữ tổng bằng 1, ta có tổ hợp affine có thể nằm ngoài đoạn. Đây là sự khác nhau cần nhớ khi đọc tập lồi.",
  'khong-gian-mau':"**Đồng khả năng là một giả định.** Chia số kết quả thuận lợi cho tổng số kết quả chỉ đúng khi mọi kết quả cơ bản có cùng xác suất. Với đồng xu lệch, hai kết quả ngửa/sấp không nhất thiết mỗi kết quả xác suất $\\frac{1}{2}$.\n\nKhi tung nhiều lần, chọn kết quả cơ bản đủ chi tiết. Đếm “0,1,2 mặt ngửa” như ba kết quả đồng khả năng là sai: trường hợp một mặt ngửa có hai cách xảy ra.",
  'xac-suat-co-dieu-kien':"**Định nghĩa và Bayes.** Với $P(B)>0$:\n\n$$P(A\\mid B)=\\frac{P(A\\cap B)}{P(B)},qquad P(A\\mid B)=\\frac{P(B\\mid A)P(A)}{P(B)}.$$\n\nMẫu số P(B) bao gồm mọi cách B xảy ra, không chỉ trường hợp A đúng. Nếu A và phần bù của A chia hết miền xét, P(B)=P(B|A)P(A)+P(B|không A)P(không A). Đảo nhầm hai chiều điều kiện hoặc bỏ tỷ lệ ban đầu là hai lỗi phổ biến.",
  'doc-lap':"**Độc lập từng đôi khác độc lập toàn bộ.** Với nhiều biến cố, yêu cầu từng cặp độc lập chưa đủ để kết luận mọi nhóm đều có xác suất giao bằng tích xác suất. Cần kiểm tra định nghĩa phù hợp với số biến cố.\n\nĐộc lập cũng không đồng nghĩa không tương quan trong mọi trường hợp. Với biến có phương sai hữu hạn, độc lập kéo theo hiệp phương sai bằng 0. Chiều ngược lại nhìn chung không đúng.",
  'bien-ngau-nhien':"**X là hàm, x là giá trị.** Biến ngẫu nhiên X ánh xạ kết quả $\\omega$ trong không gian mẫu thành số $X(\\omega )$. PMF cho $P(X=x)$ với biến rời rạc. Mật độ PDF cho phép tính xác suất trên khoảng với biến liên tục.\n\nHàm phân phối tích lũy $F(x)=P(X\\le x)$ dùng cho cả hai. Mật độ tại một điểm không phải xác suất tại điểm. Với biến liên tục có mật độ, $P(X=x)=0$.",
  'ky-vong':"**Tồn tại và tuyến tính.** Kỳ vọng cần được kiểm tra tồn tại theo mô hình đang dùng. Với biến liên tục có mật độ, $\\mathbb E[X]=\\int x f(x)\\,dx$ khi tích phân thích hợp tồn tại. Một phân phối có thể không có kỳ vọng hữu hạn.\n\n$\\mathbb E[aX+bY]=aE[X]+bE[Y]$ không cần X,Y độc lập khi các kỳ vọng tồn tại. Nhưng $\\mathbb E[XY]=\\mathbb E[X]\\mathbb E[Y]$ thường cần thêm điều kiện, như độc lập và khả tích thích hợp.",
  'phuong-sai':"**Công thức kỹ thuật.** Với moment bậc hai hữu hạn:\n\n$$\\operatorname{Var}(X)=E[(X-E[X])^2]=E[X^2]-E[X]^2.$$\n\nVới hai biến, $\\operatorname{Var}(X+Y)=\\operatorname{Var}(X)+\\operatorname{Var}(Y)+2Cov(X,Y)$. Độc lập và các moment hữu hạn cho $\\operatorname{Cov}=0$. Phương sai có đơn vị bình phương của dữ liệu. Độ lệch chuẩn có cùng đơn vị với dữ liệu. Đừng nhầm phương sai tổng thể với ước lượng phương sai mẫu chia $n-1$.",
  'to-hop':"**Đếm theo mô hình.** Chọn k từ n không xét thứ tự, không lặp dùng C(n,k). Chọn có thứ tự, không lặp dùng $\\frac{n!}{(n-k)!}$. Nếu chọn có thứ tự và có lặp, mỗi vị trí có n lựa chọn, nên có $n^k$ dãy.\n\nTrước khi áp dụng, nêu rõ các đối tượng có phân biệt không, thứ tự có quan trọng không và có được lặp không.",
  'mau-tong-the':'**Ước lượng có sai số lấy mẫu.** Hai mẫu khác nhau từ cùng tổng thể có thể cho trung bình khác nhau. Độ bất định này khác với sai lệch hệ thống do cách chọn mẫu.\n\nCỡ mẫu lớn giúp giảm nhiều dạng sai số ngẫu nhiên nhưng không tự sửa thiên lệch chọn mẫu. Các công thức khoảng tin cậy và kiểm định phải đi cùng giả định về cách lấy mẫu và phân phối.',
  'bien-kieu':"**Giá trị và cách lưu.** Trong Python, tên biến tham chiếu tới đối tượng. Có thể gán lại tên đó cho đối tượng khác kiểu. NumPy dtype mô tả biểu diễn cố định như int32, float64, ảnh hưởng miền giá trị và độ chính xác.\n\nMột phép toán đúng về đại số có thể tràn số nguyên cố định hoặc làm tròn số thực. Kiểm tra kiểu dữ liệu trước khi kết luận từ kết quả tính.",
  list:"**Mutable và aliasing.** List có thể thay đổi tại chỗ. Gán `b = a` khiến hai tên dùng chung đối tượng, còn `b = a.copy()` tạo một list mới. Đây chỉ là sao chép nông, vì vậy các đối tượng lồng bên trong vẫn có thể dùng chung.\n\nSo sánh `a is b` kiểm tra hai tên có trỏ đến cùng đối tượng hay không, còn `a == b` so sánh giá trị. List khác mảng NumPy về quy tắc tính toán theo từng phần tử.",
  dictionary:'**Hashable và tra cứu.** Dictionary dùng khóa hashable, nghĩa là phù hợp với yêu cầu băm và so sánh bằng nhau. List thông thường không hashable nên không thể dùng trực tiếp làm khóa.\n\nTra cứu thường có chi phí trung bình gần O(1) trong mô hình phù hợp, nhưng không phải mọi trường hợp đều bảo đảm như vậy. Khóa giống nhau ghi đè giá trị trước thay vì tạo khóa thứ hai.',
  'ham-lap-trinh':'**Tham số có thể dùng chung đối tượng.** Truyền list vào một hàm rồi sửa list tại chỗ có thể làm dữ liệu của bên gọi thay đổi. Gán lại tên tham số bên trong hàm thường không gán lại tên ở bên gọi.\n\nHàm có tác động phụ khác hàm chỉ trả kết quả. Đọc kiểu đầu vào, kết quả trả về và điều gì bị thay đổi để dùng hàm chính xác.',
  'tham-so-lap-trinh':"**Tên trong định nghĩa, giá trị trong lời gọi.** Với `def f(x, scale=1)`, `x` và `scale` là tham số. Trong `f(data, scale=2)`, `data` và `2` là đối số. Tham số mặc định được dùng khi lời gọi không truyền giá trị tương ứng.\n\nKhi gọi hàm, Python dùng cơ chế chia sẻ đối tượng. Nếu đối số là list và hàm sửa list tại chỗ, bên gọi có thể quan sát thay đổi. Đây là cơ chế của lời gọi hàm. Nó không liên quan đến “tham số mô hình” trong một bài toán tối ưu.",
  'vong-lap':"**Bất biến và kết thúc.** Bất biến vòng lặp là điều đúng trước và sau mỗi lần lặp, giúp chứng minh kết quả. Cần thêm đại lượng giảm hoặc miền hữu hạn để giải thích tại sao vòng lặp dừng.\n\nDừng đúng không đồng nghĩa kết quả đúng. Với while, kiểm tra cả việc khởi tạo, điều kiện và cập nhật biến. Nếu bỏ bước cập nhật, vòng lặp có thể không kết thúc.",
  'chi-muc':"**Nhãn và vị trí không giống nhau.** pandas loc theo nhãn, iloc theo vị trí. Hai giá trị cùng là số nguyên vẫn có thể được hiểu theo hai cách khác nhau. Một lát cắt loc thường gồm nhãn cuối, còn iloc không gồm vị trí cuối.\n\nNumPy basic slicing thường tạo view dùng chung dữ liệu, còn advanced indexing thường tạo copy. Đọc quy tắc của đối tượng cụ thể thay vì suy từ cú pháp dấu ngoặc.",
  'vector-hoa':'**Tốc độ không phải tiêu chí duy nhất.** Phép toán trên mảng có thể chuyển vòng lặp sang mã tối ưu bên dưới, nhưng vẫn phải thực hiện công việc. Các mảng tạm có thể làm tăng bộ nhớ và đọc/ghi.\n\nVector hóa đúng cần giữ ý nghĩa trục, shape và dtype. Kiểm tra đầu ra trên ví dụ nhỏ trước khi thay toàn bộ vòng lặp bằng một biểu thức mảng.',
  broadcasting:"**Quy tắc tương thích.** So các kích thước từ trục cuối. Hai trục tương thích khi bằng nhau hoặc có một bên bằng 1. Trục thiếu được coi như kích thước 1.\n\n$(3,2)+(2,)$ cho (3,2). $(3,2)+(3,)$ không tương thích. Muốn cộng một giá trị riêng cho từng hàng, đổi vector shape (3,) thành (3,1). Việc mở rộng là quy tắc tính toán, không nhất thiết sao chép cả dữ liệu đầu vào.",
  'gia-tri-thieu':'**NaN không bằng chính nó.** So sánh NaN==NaN cho false trong số thực IEEE thông thường. Dùng chức năng isna/isnan phù hợp thay vì kiểm tra bằng nhau. pandas còn có các dạng biểu diễn thiếu khác tùy kiểu dữ liệu.\n\nBỏ giá trị thiếu hoặc điền giá trị thay thế đều có thể thay đổi thống kê. Phải biết cơ chế thiếu và mục tiêu phân tích trước khi chọn phương án.',
  'dien-tich':"**Nguồn và điện tích thử.** Điện tích nguồn tạo điện trường. Điện tích thử được dùng để mô tả lực tại điểm xét. Định nghĩa E dùng điện tích thử dương đủ nhỏ để không làm thay đổi phân bố nguồn trong mô hình.\n\nCộng điện tích là cộng đại số theo dấu, còn cộng điện trường là cộng vector. Hệ có tổng điện tích bằng 0 vẫn có thể tạo điện trường khác 0.",
  luc:'**Cộng vector và hệ quy chiếu.** Trong cơ học Newton với khối lượng không đổi, tổng lực bằng ma trong hệ quy chiếu quán tính. Từng lực có thể khác 0 dù tổng lực bằng 0.\n\nLực điện qE đổi chiều khi q đổi dấu. Lực từ qv×B vuông góc với vận tốc nên lực từ riêng không sinh công trong mô hình này.',
  'cong-nang-luong':"**Tích phân đường.** Khi lực thay đổi, công được tính bởi $W=\\int\\mathbf F\\cdot d\\mathbf l$, không chỉ lấy một giá trị lực nhân độ dài quãng đường. Với lực thế, W từ A tới B bằng $U(A)-U(B)$, độc lập đường đi.\n\nThế năng phụ thuộc mốc chọn, nhưng hiệu thế năng và công có ý nghĩa trực tiếp. Trong tĩnh điện, $U=qV$, nên $W=q(V_A-V_B)$.",
  'dien-the':"**Quan hệ cục bộ với trường.** Trong tĩnh điện:\n\n$$V_B-V_A=-\\int_A^B\\mathbf E\\cdot d\\mathbf l,qquad\\mathbf E=-\\nabla V.$$\n\nV là vô hướng, E là vector. $V=0$ tại một điểm không kéo theo $E=0$ vì gradient đo biến thiên không gian của V. Trong vật dẫn liên thông ở cân bằng tĩnh điện, $E=0$ trong lòng và V không đổi. Với trường biến thiên theo thời gian, cần mô hình rộng hơn để mô tả đầy đủ điện trường.",
  'thong-luong':"**Hướng của diện tích.** Vector diện tích bằng pháp tuyến đơn vị nhân phần tử diện tích. Mặt kín dùng pháp tuyến hướng ra ngoài, còn khi đổi hướng pháp tuyến thì thông lượng đổi dấu.\n\nThông lượng tổng bằng 0 không kéo theo trường bằng 0 từng điểm. Với trường đều qua hộp kín, phần đi vào và đi ra có thể bù nhau. Định luật Gauss liên hệ thông lượng kín với điện tích bên trong.",
  'don-vi':"**Kiểm tra thứ nguyên.** Hai vế công thức phải có cùng thứ nguyên. Phép cộng cũng cần các hạng cùng thứ nguyên, nhưng hệ số có thể mang đơn vị để làm biểu thức hợp lệ.\n\nTrong $V(x)=ax^{2}+bx$, nếu V tính bằng volt và x bằng mét thì a có đơn vị $V/m^{2}$, b có đơn vị $V/m$. Kiểm tra thứ nguyên giúp bắt lỗi nhưng chưa bảo đảm một công thức đúng về hệ số hoặc mô hình.",
  song:"**Pha của sóng điều hòa.** Một mô hình thường dùng là $y(x,t)=A \\cos(kx-\\omega t+\\varphi _{0})$, với $k=\\frac{2\\pi}{\\lambda}$ và $\\omega =2\\pi f$. Dấu trong pha quyết định hướng truyền theo quy ước tọa độ.\n\nCùng tần số chưa đủ để luôn tăng cường: cần xét độ lệch pha tại vị trí đang quan sát. Hai sóng ngược pha chỉ triệt tiêu hoàn toàn nếu biên độ bằng nhau.",
  'khoa-gia-tri':"**Gom theo khóa khác ghi đè.** Luồng MapReduce có thể chứa nhiều cặp cùng khóa. Shuffle gom tất cả giá trị cho khóa đó. Không chỉ giữ giá trị cuối như khi gán nhiều lần vào cùng khóa dictionary.\n\nChọn khóa quyết định cách chia nhóm và lượng dữ liệu trên từng máy. Khóa phổ biến quá mức có thể làm mất cân bằng tải.",
  bam:'**Va chạm cần xử lý.** Bảng băm phải có cách phân biệt các khóa rơi vào cùng vùng, chẳng hạn liên kết danh sách hoặc tìm vị trí khác. Một hash hữu hạn không thể đảm bảo không va chạm cho miền đầu vào vô hạn.\n\nHàm băm dùng để chia phân vùng không tự đáp ứng yêu cầu bảo mật. Kiểm tra mục đích, phân bố dữ liệu và chi phí tính trước khi lựa chọn.',
  'phan-tan':'**Thời gian và lỗi.** Thời gian của một pha đồng bộ thường bị quyết định bởi tác vụ hoàn thành chậm nhất, không phải trung bình. Chi phí truyền gồm độ trễ khởi tạo và lượng dữ liệu chia băng thông.\n\nThiết kế cần tính khả năng máy lỗi, xử lý lặp và tái lập kết quả. Thêm máy có thể giảm tính toán cục bộ nhưng tăng truyền, nên không bảo đảm tăng tốc tuyến tính.',
  'ket-hop':"**Gom cục bộ cần giữ đủ thông tin.** Tính kết hợp cho phép đổi cách nhóm, còn tính giao hoán cho phép đổi thứ tự. Nối chuỗi kết hợp nhưng không giao hoán. Khi tính trên máy, làm tròn số thực có thể phá kết hợp chính xác của phép cộng.\n\nMuốn tính trung bình phân tán, gửi cặp (tổng,số lượng), cộng hai thành phần rồi chia ở cuối. Trung bình các trung bình không giữ đủ thông tin nếu kích thước nhóm khác nhau.",
  'quan-he':"**Tương đương và thứ tự.** Quan hệ tương đương phản xạ, đối xứng và bắc cầu. Nó chia tập thành các lớp tương đương. Quan hệ thứ tự bộ phận phản xạ, phản đối xứng và bắc cầu.\n\nĐối xứng và phản đối xứng là hai tính chất khác nhau, không phải phủ định đơn giản của nhau. Quan hệ bằng nhau vừa đối xứng vừa phản đối xứng."
}
const htmlEscape = text=>text.replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;')
function createBaseWikiArticle(id) {
  const term=concepts[id], related=relatedConcepts(id)
  return `---\ntitle: ${JSON.stringify(term.name)}\nwikiTerm: ${id}\nprev: false\nnext: false\n---\n\n# ${term.name}\n\n${formatWikiMath(term.definition)}\n\n<WikiUsage />\n\n## Giải thích kỹ thuật\n\n${term.notation ? formatWikiMath(term.notation) + '\n\n' : ''}${formatWikiMath(wikiDetails[id])}\n\n## Ví dụ\n\n${formatWikiMath(term.example)}\n\n## Khi nào cần dùng?\n\n${formatWikiMath(term.use)}\n\n## Câu hỏi ôn lại\n\n${formatWikiMath(term.question)}\n\n<details><summary>Xem đáp án</summary>\n\n${formatWikiMath(term.answer)}\n\n</details>\n\n## Thuật ngữ liên quan\n\n${related.map(other=>`- [${htmlEscape(concepts[other].name)}](./${other}.md)`).join('\n')}\n`
}

const referenceTerms = new Set(['thong-ke-mo-ta', 'suy-rong-thong-ke', 'ket-luan-nhan-qua', 'du-doan-thong-ke'])
export function createWikiArticle(id) {
  const article = createBaseWikiArticle(id)
  if (!referenceTerms.has(id)) return article
  return article + '\n## Tài liệu tham khảo\n\n- Stat 20, UC Berkeley. [Understanding the World with Data](https://stat20.berkeley.edu/spring-2026/1-questions-and-data/01-understanding-the-world/notes.html), mục “Types of Claims”. Các định nghĩa chuyển thể được chia sẻ theo [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).\n'
}
