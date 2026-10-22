export const wikiJourneys = [
  { id: 'geometry', title: 'Một phép biến đổi làm thay đổi điều gì?', description: 'Đi từ mũi tên trên mặt phẳng đến ma trận, tích vô hướng và độ dài.', tone: 'lam', ids: ['vector', 'ma-tran', 'tich-vo-huong', 'chuan', 'tri-rieng'] },
  { id: 'optimization', title: 'Làm thế nào để đi xuống mà không đi lạc?', description: 'Độ dốc, độ cong và giả thiết bảo đảm nghiệm tối ưu.', tone: 'tim', ids: ['dao-ham', 'gradient', 'hessian', 'tap-loi', 'ham-loi'] },
  { id: 'uncertainty', title: 'Bằng chứng mới thay đổi dự đoán ra sao?', description: 'Điều kiện, độc lập, trung bình và mức phân tán là những câu hỏi khác nhau.', tone: 'hong', ids: ['xac-suat-co-dieu-kien', 'doc-lap', 'bien-ngau-nhien', 'ky-vong', 'phuong-sai'] },
  { id: 'algorithms', title: 'Chọn cách lưu để chọn cách giải', description: 'Ngăn xếp, hàng đợi, đồ thị và chi phí của một thao tác.', tone: 'ngoc', ids: ['ngan-xep', 'hang-doi', 'do-thi', 'cay', 'do-phuc-tap'] }
]
export const wikiPeople = [
  { id: 'ada-lovelace', name: 'Ada Lovelace', initials: 'AL', year: '1843', field: 'Lập trình & ký hiệu', idea: 'Một cỗ máy có thể thao tác với ký hiệu theo quy tắc, vượt ra ngoài việc tính số.', related: ['ham-lap-trinh', 'vong-lap', 'trang-thai'], source: 'https://www.computerhistory.org/babbage/adalovelace/' },
  { id: 'alan-turing', name: 'Alan Turing', initials: 'AT', year: '1936', field: 'Tính toán & thuật toán', idea: 'Mô tả chính xác phép tính để nhìn thấy cả khả năng lẫn giới hạn của thuật toán.', related: ['trang-thai', 'ham-lap-trinh', 'do-phuc-tap'], source: 'https://turingarchive.kings.cam.ac.uk/about-alan-turing' },
  { id: 'claude-shannon', name: 'Claude Shannon', initials: 'CS', year: '1948', field: 'Thông tin & xác suất', idea: 'Đo độ bất định để nghiên cứu mã hóa và truyền thông một cách định lượng.', related: ['xac-suat-co-dieu-kien', 'ky-vong', 'bien-ngau-nhien'], source: 'https://www.nokia.com/bell-labs/publications-and-media/publications/a-mathematical-theory-of-communication/' },
  { id: 'thomas-bayes', name: 'Thomas Bayes', initials: 'TB', year: '1763', field: 'Suy luận xác suất', idea: 'Phân biệt xác suất của bằng chứng khi biết giả thuyết với xác suất của giả thuyết khi biết bằng chứng.', related: ['xac-suat-co-dieu-kien', 'likelihood', 'doc-lap'], source: 'https://www.gtfp.cs.rhul.ac.uk/pulskamp/Bayes/bayesessay-rjp.pdf' },
  { id: 'isaac-newton', name: 'Isaac Newton', initials: 'IN', year: '1687', field: 'Cơ học & giải tích', idea: 'Liên hệ sự thay đổi chuyển động với lực, rồi kiểm tra mô hình bằng giả thiết và đơn vị.', related: ['luc', 'dao-ham', 'cong-nang-luong'], source: 'https://www.newtonproject.ox.ac.uk/his-life-and-work-at-a-glance' },
  { id: 'emmy-noether', name: 'Emmy Noether', initials: 'EN', year: '1918', field: 'Đối xứng & bảo toàn', idea: 'Đối xứng liên tục của tác dụng dẫn đến đại lượng bảo toàn, dưới các giả thiết của định lý.', related: ['cong-nang-luong', 'luc', 'dao-ham'], source: 'https://arxiv.org/abs/physics/9807044' }
]
export const peopleForConcept = id => wikiPeople.filter(person => person.related.includes(id))

// Connections follow the ideas developed in the articles, rather than list order.
export const atlasConnections = {
  vector: ['ma-tran', 'tich-vo-huong', 'chuan'],
  'ma-tran': ['vector', 'he-phuong-trinh', 'tri-rieng'],
  'tich-vo-huong': ['vector', 'chuan', 'cong-nang-luong'],
  chuan: ['vector', 'tich-vo-huong', 'ham-loi'],
  'dao-ham': ['gioi-han', 'dao-ham-rieng', 'gradient', 'quy-tac-chuoi'],
  gradient: ['dao-ham-rieng', 'tich-vo-huong', 'hessian'],
  hessian: ['gradient', 'ma-tran-psd', 'ham-loi'],
  'tap-loi': ['to-hop-loi', 'ham-loi', 'phep-chieu'],
  'ham-loi': ['tap-loi', 'gradient', 'hessian', 'bat-dang-thuc-jensen'],
  'xac-suat-co-dieu-kien': ['doc-lap', 'likelihood', 'bien-ngau-nhien'],
  'doc-lap': ['xac-suat-co-dieu-kien', 'bien-ngau-nhien', 'ma-tran-hiep-phuong-sai'],
  'ky-vong': ['bien-ngau-nhien', 'phuong-sai', 'tich-phan'],
  'phuong-sai': ['ky-vong', 'phan-phoi-gauss', 'ma-tran-hiep-phuong-sai'],
  'ngan-xep': ['hang-doi', 'de-quy', 'do-thi'],
  'hang-doi': ['ngan-xep', 'do-thi', 'hang-doi-uu-tien'],
  'do-thi': ['cay', 'hang-doi', 'ngan-xep'],
  cay: ['do-thi', 'de-quy', 'hang-doi'],
  bam: ['dictionary', 'khoa-gia-tri', 'do-phuc-tap']
}
