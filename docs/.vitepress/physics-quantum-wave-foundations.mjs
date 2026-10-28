const term = (name, aliases, definition, example, use, question, answer) => ({
  name, aliases: [...new Set([name, name.toLocaleLowerCase('vi'), ...aliases])],
  definition, example, use, question, answer
})

export const quantumWaveConcepts = {
  'ham-song-luong-tu': term(
    'Hàm sóng lượng tử', ['hàm sóng'],
    'Hàm phức mô tả trạng thái của hệ trong một biểu diễn. Với một hạt một chiều, $|\\Psi(x,t)|^2$ là mật độ xác suất vị trí khi trạng thái được chuẩn hóa.',
    'Hai hàm sóng khác nhau bởi một pha chung không đổi cho cùng phân bố xác suất vị trí.',
    'Mô tả trạng thái, tính xác suất và xác định sự tiến triển theo phương trình Schrödinger.',
    'Hàm sóng bằng số phức có khiến xác suất cũng là số phức không?',
    'Không. Xác suất được tính từ bình phương môđun rồi tích phân trên miền, nên là số thực không âm.'
  ),
  'mat-do-xac-suat-luong-tu': term(
    'Mật độ xác suất lượng tử', ['mật độ xác suất vị trí', 'quy tắc Born'],
    'Trong biểu diễn vị trí một chiều, mật độ $\\rho=|\\Psi|^2$ cho xác suất trên một khoảng thông qua tích phân. Mật độ không phải xác suất tại một điểm.',
    'Một vùng hẹp quanh bụng sóng thường có xác suất lớn hơn vùng cùng độ rộng quanh một nút.',
    'Đọc đồ thị hàm sóng và tính xác suất phát hiện hạt trong một miền.',
    'Nếu mật độ ở một điểm khác không, xác suất của đúng điểm ấy có nhất thiết khác không?',
    'Không. Với phân bố vị trí liên tục, một điểm đơn lẻ có độ rộng bằng không và xác suất bằng không. Mật độ khác không nói về xác suất trên các khoảng lân cận.'
  ),
  'chuan-hoa-ham-song': term(
    'Chuẩn hóa hàm sóng', ['chuẩn hóa hàm sóng'],
    'Chọn hệ số của một hàm sóng chuẩn hóa được sao cho tích phân bình phương môđun trên toàn miền bằng một.',
    'Hàm sin của hạt trong hộp cần một hệ số phụ thuộc chiều rộng hộp, không có biên độ tùy ý như một dây rung cổ điển.',
    'Xác định hằng số biên độ để các tích phân cho xác suất tuyệt đối.',
    'Một sóng phẳng kéo dài vô hạn có chuẩn hóa theo tích phân thông thường trên toàn trục được không?',
    'Không. Bình phương môđun không giảm ở vô cực nên tích phân phân kỳ. Cần gói sóng chuẩn hóa được hoặc một quy ước chuẩn hóa suy rộng phù hợp.'
  ),
  'so-phuc-trong-ham-song': term(
    'Số phức trong hàm sóng', ['môđun hàm sóng', 'liên hợp phức của hàm sóng'],
    'Nếu $z=a+ib$, liên hợp là $z^*=a-ib$ và bình phương môđun là $|z|^2=z^*z=a^2+b^2$. Không dùng bình phương đại số $z^2$ để tính mật độ xác suất.',
    'Pha chung không đổi môđun, nhưng thay đổi pha tương đối giữa hai thành phần có thể đổi giao thoa.',
    'Khai triển hàm sóng, lấy liên hợp và tính những số hạng giao thoa.',
    'Có thể bỏ phần ảo rồi chỉ bình phương phần thực của hàm sóng không?',
    'Không. Làm vậy bỏ một phần của bình phương môđun và có thể làm sai cả chuẩn hóa lẫn phân bố xác suất.'
  ),
  'phuong-trinh-schrodinger': term(
    'Phương trình Schrödinger', ['phương trình Schrödinger'],
    'Phương trình xác định sự tiến triển của trạng thái lượng tử phi tương đối tính. Với thế năng không phụ thuộc thời gian, nghiệm trạng thái riêng năng lượng còn thỏa một phương trình không phụ thuộc thời gian.',
    'Đặt hàm sin vào phương trình bên trong hộp chưa đủ. Nghiệm còn phải thỏa điều kiện tại hai vách.',
    'Tìm hàm sóng, năng lượng và sự thay đổi theo thời gian trong mô hình đã xác định.',
    'Mọi hàm thỏa phương trình vi phân đều là trạng thái vật lý được phép hay không?',
    'Không. Còn phải xét miền, điều kiện biên, tính chuẩn hóa và những giả thiết của Hamiltonian.'
  ),
  'chong-chap-ham-song': term(
    'Chồng chập hàm sóng', ['nguyên lý chồng chập lượng tử', 'chồng chập lượng tử'],
    'Với cùng một phương trình Schrödinger tuyến tính, tổ hợp tuyến tính của các nghiệm cũng là nghiệm. Phải tính bình phương môđun của tổng biên độ để tìm xác suất.',
    'Tổng của hai trạng thái có năng lượng khác nhau có thể có mật độ xác suất dao động theo thời gian.',
    'Giải thích giao thoa, tạo gói sóng và mô tả các trạng thái không có năng lượng xác định.',
    'Mật độ của một chồng chập có luôn bằng tổng các mật độ thành phần không?',
    'Không. Nói chung có các số hạng giao thoa, phụ thuộc pha tương đối.'
  ),
  'goi-song-luong-tu': term(
    'Gói sóng lượng tử', ['gói sóng lượng tử', 'gói sóng'],
    'Chồng chập nhiều thành phần sóng tạo biên độ tập trung trong một miền không gian. Gói chuẩn hóa được có phân bố động lượng và có thể biến dạng theo thời gian.',
    'Một electron tương đối định xứ cần nhiều số sóng, thay vì chỉ một sóng phẳng kéo dài khắp không gian.',
    'Liên hệ vị trí, phổ động lượng, vận tốc nhóm và sự phân tán của một hạt tự do.',
    'Chồng hai sóng phẳng đã tạo một gói chuẩn hóa được trên toàn trục chưa?',
    'Chưa. Hai sóng cho những dải giao thoa lặp lại vô hạn. Muốn một gói định xứ chuẩn hóa được, cần dạng chồng chập thích hợp.'
  ),
  'trang-thai-dung-luong-tu': term(
    'Trạng thái dừng lượng tử', ['trạng thái dừng', 'trạng thái riêng năng lượng'],
    'Trạng thái có năng lượng xác định trong một Hamiltonian không phụ thuộc thời gian. Hàm sóng chỉ thay đổi theo một pha chung theo thời gian nên mật độ xác suất vị trí không đổi.',
    'Mật độ của một mức riêng trong hộp giữ nguyên theo thời gian, dù không thể diễn giải hạt như đứng yên tại một tọa độ.',
    'Phân biệt năng lượng xác định với chồng chập nhiều mức và với chuyển động đứng yên cổ điển.',
    'Trạng thái dừng có bắt buộc là trạng thái có động lượng xác định không?',
    'Không. Trạng thái riêng năng lượng trong một thế năng không đồng nhất thường không phải trạng thái riêng động lượng.'
  ),
  'dieu-kien-bien-ham-song': term(
    'Điều kiện biên của hàm sóng', ['điều kiện biên của hàm sóng', 'nối hàm sóng'],
    'Những yêu cầu tại biên và vô cực mà nghiệm vật lý phải thỏa. Với khối lượng không đổi và bước thế năng hữu hạn, hàm sóng cùng đạo hàm bậc nhất nối liên tục.',
    'Hộp vô hạn đặt hàm sóng bằng không tại vách. Giếng hữu hạn cần nối với những đuôi hàm mũ bên ngoài.',
    'Chọn nghiệm được phép, loại nghiệm phân kỳ và xác định phổ năng lượng.',
    'Có được áp cùng điều kiện nối đạo hàm cho bước thế hữu hạn và vách vô hạn không?',
    'Không. Vách vô hạn là một giới hạn kỳ dị. Phải dùng điều kiện giam giữ của mô hình, không suy ra tính liên tục đạo hàm qua vách theo quy tắc hữu hạn.'
  ),
  'hat-trong-hop-luong-tu': term(
    'Hạt trong hộp lượng tử', ['hạt trong hộp', 'giếng thế vô hạn'],
    'Mô hình hạt phi tương đối tính bị giới hạn trong một khoảng bởi hai vách thế năng vô hạn. Các hàm riêng bên trong là sóng sin có nút tại hai vách.',
    'Thu hẹp hộp làm các mức năng lượng và khoảng cách giữa chúng tăng.',
    'Khảo sát lượng tử hóa do giam giữ, chuẩn hóa và xác suất vị trí.',
    'Vì sao không chọn số lượng tử bằng không cho mức thấp nhất?',
    'Nghiệm sin với số lượng tử bằng không là hàm bằng không trên toàn miền và không chuẩn hóa được. Mức thấp nhất có số lượng tử bằng một.'
  ),
  'gieng-the-huu-han': term(
    'Giếng thế hữu hạn', ['giếng thế hữu hạn', 'giếng thế vuông hữu hạn'],
    'Miền thế năng thấp được bao quanh bởi các miền thế năng cao hơn một lượng hữu hạn. Trạng thái liên kết có hàm sóng thâm nhập ra ngoài giếng rồi giảm dần.',
    'Giếng hữu hạn cùng rộng với hộp vô hạn có các mức liên kết thấp hơn nếu dùng cùng mốc thế năng tại đáy.',
    'Mô hình hóa sự giam giữ electron, tính năng lượng liên kết và phân tích đuôi xác suất.',
    'Một giếng vuông hữu hạn một chiều rất nông có nhất thiết không giữ được trạng thái nào?',
    'Không. Giếng hút vuông một chiều với độ rộng và độ sâu dương luôn có ít nhất một trạng thái liên kết. Đuôi hàm sóng dài hơn khi liên kết yếu.'
  ),
  'trang-thai-lien-ket-luong-tu': term(
    'Trạng thái liên kết lượng tử', ['trạng thái liên kết'],
    'Trạng thái chuẩn hóa được bị giam giữ bởi thế năng, với năng lượng dưới ngưỡng thoát của bài toán. Xác suất có thể kéo dài sang những miền bị cấm cổ điển.',
    'Electron trong giếng hữu hạn có đuôi xác suất bên ngoài nhưng vẫn là trạng thái liên kết nếu năng lượng chưa đạt ngưỡng thoát.',
    'Phân biệt phổ rời rạc của trạng thái liên kết với phổ tán xạ trên ngưỡng.',
    'Có một phần hàm sóng ngoài giếng có đồng nghĩa hạt đã thoát hẳn không?',
    'Không. Trạng thái liên kết giảm ở vô cực và vẫn chuẩn hóa được. Đuôi bên ngoài không phải một dòng thoát không ngừng.'
  ),
  'xuyen-ham-luong-tu': term(
    'Xuyên hầm lượng tử', ['xuyên hầm', 'hàng rào thế'],
    'Sự truyền qua một hàng rào thế với năng lượng thấp hơn đỉnh hàng rào. Hàm sóng không triệt tiêu trong vùng bị cấm cổ điển và có thể nối sang phía bên kia.',
    'Dòng điện STM phụ thuộc nhạy vào khoảng cách giữa đầu dò và mẫu vì khoảng ấy là bề rộng hàng rào.',
    'Giải thích truyền qua màng mỏng, tiếp giáp Josephson, phân rã alpha và các quá trình truyền electron.',
    'Xuyên hầm có đòi hỏi hạt mất cơ năng để đục qua hàng rào tĩnh không?',
    'Không. Trong thế năng tĩnh của mô hình tán xạ, cơ năng được bảo toàn. Công thức gần đúng cho hệ số truyền cần được dùng đúng miền áp dụng.'
  ),
  'dao-dong-tu-dieu-hoa-luong-tu': term(
    'Dao động tử điều hòa lượng tử', ['dao động tử điều hòa lượng tử', 'dao động tử lượng tử'],
    'Hệ một chiều có thế năng parabol, lực phục hồi tỉ lệ với độ lệch. Các mức năng lượng cách đều, bắt đầu từ một nửa lượng tử năng lượng dao động.',
    'Dao động nhỏ của một nguyên tử quanh vị trí cân bằng trong tinh thể có thể được xấp xỉ bằng mô hình này.',
    'Tính mức dao động, phổ hồng ngoại, hàm Gaussian cơ bản và sự tương ứng cổ điển.',
    'Năng lượng thấp nhất có bằng không như một hạt cổ điển đứng yên ở cân bằng không?',
    'Không. Năng lượng cơ bản bằng $\\hbar\\omega/2$, với mốc thế năng tại đáy parabol bằng không.'
  ),
  'nang-luong-diem-khong': term(
    'Năng lượng điểm không', ['năng lượng điểm không'],
    'Năng lượng còn lại của trạng thái cơ bản trong một hệ lượng tử, với mốc năng lượng đã chọn rõ. Trong dao động tử điều hòa, mức cơ bản nằm cao hơn đáy thế năng.',
    'Hạt trong hộp và dao động tử đều không có trạng thái vật lý vừa bị giam giữ vừa có động năng và thế năng đồng thời bằng không.',
    'Giải thích giới hạn của mô tả cổ điển về trạng thái nghỉ và tính năng lượng cơ bản.',
    'Thay đổi gốc thế năng có làm thay đổi các khoảng cách mức không?',
    'Không. Cộng cùng một hằng số vào mọi mức chỉ đổi mốc. Ý nghĩa ở đây là độ cao của mức cơ bản so với đáy thế năng đã chọn.'
  ),
  'phep-do-luong-tu': term(
    'Phép đo lượng tử', ['phép đo lượng tử', 'suy sụp hàm sóng'],
    'Quá trình tạo kết quả đo và tương quan với dụng cụ. Trong mô hình phép chiếu lý tưởng, kết quả có xác suất theo trạng thái chuẩn bị và trạng thái có điều kiện được cập nhật theo kết quả.',
    'Chồng chập hai mức năng lượng có thể cho một trong hai mức khi đo, dù giá trị kỳ vọng nằm giữa chúng.',
    'Phân biệt kết quả từng lần, phân bố thống kê và trạng thái sau phép đo.',
    'Giá trị kỳ vọng có bắt buộc là một kết quả có thể thu được trong từng lần đo không?',
    'Không. Giá trị kỳ vọng là trung bình thống kê, có thể nằm giữa các giá trị riêng rời rạc.'
  ),
  'cham-luong-tu': term(
    'Chấm lượng tử', ['chấm lượng tử', 'quantum dot'],
    'Cấu trúc đủ nhỏ để sự giam giữ làm xuất hiện những hiệu ứng lượng tử rõ rệt. Trong mô hình hạt bị giam giữ, kích thước ảnh hưởng các mức năng lượng và màu phát quang.',
    'Hạt bán dẫn nhỏ hơn có thể phát photon bước sóng ngắn hơn khi kích thước nhỏ làm khoảng cách mức lớn hơn.',
    'Liên hệ mô hình giếng thế với huỳnh quang và việc điều chỉnh phổ bằng kích thước.',
    'Có thể suy ra kích thước chỉ từ màu mà bỏ qua vật liệu và cấu trúc của chấm không?',
    'Không. Khối lượng hiệu dụng, hình dạng, độ giam giữ và vật liệu cũng ảnh hưởng các mức năng lượng.'
  ),
  'kinh-hien-vi-quet-xuyen-ham': term(
    'Kính hiển vi quét xuyên hầm', ['kính hiển vi quét xuyên hầm', 'STM'],
    'Thiết bị khảo sát bề mặt bằng dòng electron xuyên hầm giữa một đầu dò dẫn điện rất nhọn và mẫu đặt rất gần nhau.',
    'Chế độ dòng không đổi thay đổi độ cao mũi dò trong khi quét ngang để lập bản đồ tín hiệu bề mặt.',
    'Hiểu ảnh bề mặt ở quy mô nguyên tử và độ nhạy của xuyên hầm đối với khoảng cách.',
    'Ảnh STM có phải lúc nào cũng là hình học thuần túy của các quả cầu nguyên tử không?',
    'Không. Tín hiệu phụ thuộc cấu trúc điện tử, điều kiện điện áp và trạng thái đầu dò, ngoài khoảng cách hình học.'
  ),
}

export const quantumWaveWikiDetails = {
  'ham-song-luong-tu': 'Hàm sóng trong biểu diễn vị trí gán một biên độ phức cho mỗi tọa độ. Biên độ không phải là độ dịch chuyển của một môi trường cơ học. Những dự đoán quan sát được được rút ra bằng các quy tắc về toán tử và xác suất.\n\nTrong một chiều, mật độ xác suất bằng $\\rho=\\Psi^*\\Psi$. Nếu trạng thái chuẩn hóa được, tích phân mật độ trên toàn miền bằng một. Pha chung không đổi không làm thay đổi dự đoán, nhưng pha tương đối giữa các thành phần có thể tạo hoặc triệt giao thoa.\n\nHàm sóng của một hạt có spin còn cần thông tin spin. Mô hình vô hướng ở đây dùng cho những tình huống một chiều chưa xét bậc tự do đó.',
  'mat-do-xac-suat-luong-tu': 'Một khoảng nhỏ quanh một điểm có xác suất xấp xỉ bằng mật độ tại điểm ấy nhân độ rộng khoảng. Công thức chính xác cho miền từ a đến b là tích phân mật độ trên miền ấy:\n\n$$\nP_{[a,b]}=\\int_a^b\\rho(x,t)\\,dx.\n$$\n\nTrong một chiều, mật độ có đơn vị nghịch đảo chiều dài. Nó có thể lớn hơn một theo giá trị số mà vẫn hợp lý, vì chỉ tích phân xác suất mới phải nằm từ không đến một.\n\nTại một nút, mật độ bằng không. Với mọi điểm đơn lẻ của phân bố liên tục, xác suất vẫn bằng không dù điểm đó có phải nút hay không. Cần so sánh các miền có độ rộng xác định.',
  'chuan-hoa-ham-song': 'Nếu một nghiệm chưa chuẩn hóa là f và bình phương môđun của nó có tích phân hữu hạn khác không, ta chọn hệ số C để hàm $\\psi=Cf$ có chuẩn bằng một. Điều kiện dùng toàn bộ miền mà trạng thái có thể xuất hiện, kể cả các đuôi của giếng hữu hạn.\n\n$$\n|C|^2\\int |f(x)|^2\\,dx=1.\n$$\n\nPhép chuẩn hóa không ấn định pha chung của C. Có thể chọn C thực dương khi pha ấy không cần thiết.\n\nKhông phải nghiệm nào cũng có chuẩn hữu hạn. Sóng phẳng trên toàn trục và hàm bằng không không thể được chuẩn hóa theo cách thông thường, vì tích phân lần lượt phân kỳ hoặc bằng không.',
  'so-phuc-trong-ham-song': 'Số i thỏa $i^2=-1$. Lấy liên hợp phức làm đổi dấu phần ảo và đổi $e^{i\\theta}$ thành $e^{-i\\theta}$. Bình phương môđun được tính bằng tích với liên hợp, vì vậy luôn là số thực không âm.\n\nCông thức Euler nối mô tả mũ với hai thành phần thực:\n\n$$\ne^{i\\theta}=\\cos\\theta+i\\sin\\theta.\n$$\n\nVới tổng hai biên độ, nhân tổng với liên hợp của tổng sẽ tạo các số hạng chéo. Những số hạng này mô tả giao thoa và biến mất chỉ trong những điều kiện cụ thể, không được tự ý bỏ.\n\nPhần thực và phần ảo riêng lẻ phụ thuộc quy ước pha. Đại lượng xác suất phải được xây dựng từ cả hàm phức.',
  'phuong-trinh-schrodinger': 'Trong mô hình một hạt phi tương đối tính, Hamiltonian chứa động năng và thế năng. Nếu thế năng không phụ thuộc thời gian, hàm riêng năng lượng thỏa phương trình sau, với các đạo hàm theo tọa độ:\n\n$$\n-\\frac{\\hbar^2}{2m}\\psi^{\\prime\\prime}+U\\psi=E\\psi.\n$$\n\nNăng lượng E ở đây dùng mốc của cơ năng phi tương đối tính, không tự động cộng thêm năng lượng nghỉ. Điều kiện tại biên và ở vô cực quyết định những nghiệm nào được chấp nhận.\n\nMột nghiệm riêng năng lượng nhận thêm pha $e^{-iEt/\\hbar}$ khi tiến triển theo thời gian. Tổ hợp nhiều nghiệm riêng vẫn thỏa phương trình phụ thuộc thời gian, nhưng nói chung không còn một năng lượng xác định.',
  'chong-chap-ham-song': 'Xét hai nghiệm của cùng một phương trình, $\\Psi_1$ và $\\Psi_2$. Với hệ số không phụ thuộc tọa độ và thời gian, một trạng thái chồng chập có dạng\n\n$$\n\\Psi=C\\Psi_1+D\\Psi_2.\n$$\n\nNhân với liên hợp sẽ cho các phần riêng cùng phần giao thoa. Vì vậy, cộng biên độ trước rồi bình phương môđun khác với cộng sẵn hai xác suất.\n\nNếu các trạng thái thành phần trực chuẩn, điều kiện chuẩn hóa của tổng trở thành $|C|^2+|D|^2=1$. Nếu chúng không trực giao, phải giữ cả tích chéo trong phép chuẩn hóa. Pha tương đối có thể thay đổi phân bố vị trí ngay cả khi độ lớn các hệ số giữ nguyên.',
  'goi-song-luong-tu': 'Một sóng phẳng có số sóng xác định trải khắp không gian. Muốn định xứ hạt, ta chồng những thành phần có nhiều số sóng với biên độ và pha thích hợp. Hai sóng riêng lẻ tạo nhịp giao thoa lặp lại, còn một gói định xứ đòi phổ thành phần thích hợp.\n\nVới hạt tự do phi tương đối tính, tần số góc phụ thuộc bình phương số sóng. Vận tốc nhóm của một gói hẹp phổ là\n\n$$\nv_g=\\frac{d\\omega}{dk}=\\frac{\\hbar k}{m}.\n$$\n\nCác thành phần có vận tốc nhóm khác nhau làm gói có thể giãn theo thời gian. Vị trí tập trung của gói và bước sóng của các gợn bên trong là hai đặc trưng khác nhau. Không đồng nhất vận tốc pha với tốc độ của hạt.',
  'trang-thai-dung-luong-tu': 'Với Hamiltonian không phụ thuộc thời gian, trạng thái riêng năng lượng có dạng\n\n$$\n\\Psi(x,t)=\\psi(x)e^{-iEt/\\hbar}.\n$$\n\nThừa số thời gian có môđun bằng một. Vì vậy, mật độ vị trí không đổi dù hàm sóng phức vẫn thay đổi pha. Từ “dừng” mô tả sự bất biến của phân bố, không khẳng định một quỹ đạo hạt đứng yên.\n\nCác trạng thái riêng năng lượng suy biến có thể được chồng chập mà vẫn có cùng năng lượng. Trái lại, chồng những năng lượng khác nhau thường tạo các số hạng giao thoa phụ thuộc thời gian. Năng lượng xác định cũng không đủ để suy ra động lượng xác định khi thế năng phụ thuộc vị trí.',
  'dieu-kien-bien-ham-song': 'Phương trình vi phân cho nhiều nghiệm toán học. Điều kiện biên và tính chuẩn hóa chọn nghiệm vật lý trong mô hình cụ thể.\n\nTại một bước thế năng hữu hạn, với khối lượng không đổi và không có thế kỳ dị, hàm sóng và đạo hàm bậc nhất liên tục. Trong miền thế năng không đổi nhưng cao hơn năng lượng liên kết, nghiệm có dạng mũ. Phải loại phần tăng không giới hạn khi đi ra vô cực.\n\nVách vô hạn buộc hàm sóng bằng không tại vách. Không được tiếp tục dùng điều kiện liên tục đạo hàm qua vách như với một bước hữu hạn. Một nghiệm thỏa phương trình trong lòng giếng vẫn có thể bị loại vì không thỏa điều kiện biên.',
  'hat-trong-hop-luong-tu': 'Trong đoạn từ không đến L, thế năng bằng không. Hai vách vô hạn đặt nút hàm sóng ở hai đầu, nên chỉ những sóng có số nguyên nửa bước sóng vừa trong hộp được phép tồn tại.\n\n$$\nE_n=\\frac{n^2\\pi^2\\hbar^2}{2mL^2}.\n$$\n\nSố lượng tử bắt đầu từ một. Năng lượng cơ bản khác không, còn các khoảng cách mức tăng khi số lượng tử tăng. Với cùng mức, tăng khối lượng hoặc chiều rộng làm năng lượng giảm.\n\nMật độ xác suất là bình phương của hàm sin đã chuẩn hóa. Nó không đồng đều như phân bố thời gian của một hạt cổ điển chuyển động tự do giữa hai vách. Ở số lượng tử lớn, so sánh với cổ điển cần xét trung bình trên nhiều gợn.',
  'gieng-the-huu-han': 'Chọn thế năng tại đáy bằng không và ngoài giếng bằng U₀. Trạng thái liên kết có năng lượng nằm giữa đáy và ngưỡng thoát. Trong giếng, nghiệm là tổ hợp sin và cos. Ngoài giếng, nó giảm theo hàm mũ.\n\nCác mức được tìm bằng cách nối hàm cùng đạo hàm tại hai biên. Không có công thức bình phương số nguyên đơn giản như giếng vô hạn. Số trạng thái liên kết là hữu hạn và phụ thuộc cả độ sâu, chiều rộng lẫn khối lượng.\n\nKhi mức tiến gần ngưỡng U₀ từ dưới, hằng số suy giảm ngoài giếng giảm, nên đuôi xác suất dài hơn. Trong giếng hút vuông một chiều, một trạng thái liên kết vẫn tồn tại với độ sâu dương dù rất nhỏ. Kết luận này không được áp cho mọi hình học ba chiều.',
  'trang-thai-lien-ket-luong-tu': 'Một trạng thái liên kết có chuẩn hữu hạn và xác suất không lan ra vô cực theo kiểu một sóng tán xạ tới. Trong giếng hữu hạn có thế ngoài bằng U₀, năng lượng liên kết nằm dưới U₀.\n\nPhần năng lượng nhỏ nhất cần cung cấp để tới ngưỡng thoát là\n\n$$\nE_{\\rm thoat}=U_0-E.\n$$\n\nCông thức cần cùng mốc năng lượng cho E và U₀. Nếu chọn mốc tại bên ngoài, năng lượng trạng thái liên kết thường âm. Năng lượng âm khi ấy biểu thị liên kết, không phải một động năng đo được âm.\n\nĐuôi hàm sóng trong miền bị cấm cổ điển là một phần của trạng thái và góp vào chuẩn hóa. Không được đồng nhất xác suất ngoài miệng giếng với một hạt đã được ion hóa.',
  'xuyen-ham-luong-tu': "Xét hạt có khối lượng m trong mô hình một chiều phi tương đối tính. Hàng rào thế chữ nhật cao $U_0$, rộng L. Chọn thế năng bằng không ở hai phía ngoài hàng rào và xét năng lượng $0<E<U_0$. Bên trong hàng rào, nghiệm chứa các hàm mũ. Điều kiện liên tục của hàm sóng và đạo hàm ở hai mép xác định hệ số truyền qua T.\n\nHằng số suy giảm là\n\n$$\n\\kappa=\\frac{\\sqrt{2m(U_0-E)}}{\\hbar}.\n$$\n\nỞ đây $\\hbar$ là hằng số Planck rút gọn. Hằng số $\\kappa$ có đơn vị nghịch đảo mét khi dùng đơn vị SI. Tích $\\kappa L$ không có đơn vị.\n\nTrong giới hạn hàng rào đủ mờ đục, với $\\kappa L\\gg1$ và xác suất truyền nhỏ,\n\n$$\nT\\approx Ge^{-2\\kappa L}.\n$$\n\nHệ số không có đơn vị G được xác định bởi tỉ số năng lượng:\n\n$$\nG=16\\frac{E}{U_0}\\left(1-\\frac{E}{U_0}\\right).\n$$\n\nG là hệ số đứng trước hàm mũ, không phải một xác suất riêng. Bởi bề rộng L và hằng số suy giảm nằm trong số mũ, thay đổi nhỏ về bề rộng có thể làm hệ số truyền thay đổi nhiều bậc.\n\nPhần truyền qua và phần phản xạ là các khả năng của kết quả đo, không phải bằng chứng một hạt electron bị chẻ thành hai mảnh. Với thế tĩnh, mô hình bảo toàn cơ năng và không mô tả sự tiêu hao khi hạt “đục” qua vách.",
  'dao-dong-tu-dieu-hoa-luong-tu': 'Thế năng có dạng parabol $U=k^{\\prime}x^2/2$, với hằng số lực dương. Tần số góc là $\\omega=\\sqrt{k^{\\prime}/m}$. Năng lượng các trạng thái riêng bằng\n\n$$\nE_n=\\left(n+\\frac12\\right)\\hbar\\omega.\n$$\n\nỞ đây số lượng tử bắt đầu từ không. Trạng thái cơ bản là Gaussian, còn các trạng thái cao hơn là đa thức Hermite nhân Gaussian. Điều kiện giảm ở hai phía vô cực chọn các năng lượng được phép.\n\nMọi mức liền nhau cách đều. Hàm sóng kéo ra ngoài biên độ cổ điển có cùng năng lượng. Khi số lượng tử lớn, mật độ xác suất sau khi làm trơn các gợn tiến gần phân bố cổ điển. Với thế năng thực chỉ gần parabol, các dự đoán này áp dụng cho dao động đủ nhỏ.',
  'nang-luong-diem-khong': 'Năng lượng điểm không cần được gắn với một mốc và một Hamiltonian xác định. Với dao động tử có đáy parabol bằng không,\n\n$$\nE_0=\\frac12\\hbar\\omega.\n$$\n\nTrạng thái này không phải một hạt cổ điển nằm im ở cân bằng. Phân bố Gaussian còn có độ phân tán vị trí và động lượng, với tích độ lệch chuẩn bằng $\\hbar/2$.\n\nDịch mọi mức bởi cùng một hằng số không thay đổi chênh lệch mức hoặc năng lượng photon chuyển mức. Điều mang ý nghĩa trong ví dụ là năng lượng cơ bản cao hơn đáy thế năng, chứ không phải một giá trị tuyệt đối độc lập với mọi quy ước.',
  'phep-do-luong-tu': 'Trong mô hình đo lý tưởng một đại lượng, các giá trị riêng là những kết quả được phép. Hệ chuẩn bị trong chồng chập các trạng thái riêng tương ứng cho xác suất theo bình phương độ lớn của các hệ số, sau khi chuẩn hóa.\n\nNếu chồng hai mức năng lượng trực chuẩn, mỗi lần đo cho một mức. Giá trị kỳ vọng là trung bình của nhiều lần chuẩn bị và đo, không phải một năng lượng trung gian bắt buộc của từng hạt.\n\nPhép đo lý tưởng trên một trạng thái riêng phù hợp có thể giữ nguyên trạng thái. Đối với dụng cụ thực, còn phải xét tương tác và điều kiện biên. Việc khai triển một sóng đứng thành hai sóng chạy không đủ chứng minh mọi cách đo động lượng đều có đúng hai kết quả.',
  'cham-luong-tu': 'Sự giam giữ trong cấu trúc bán dẫn rất nhỏ làm phổ mức phụ thuộc kích thước. Mô hình hộp dự đoán năng lượng tỉ lệ nghịch bình phương chiều dài đặc trưng, khi khối lượng hiệu dụng và hình dạng được giữ cố định.\n\nChiếu ánh sáng có thể kích thích electron. Khi hệ chuyển về mức thấp hơn, photon phát ra mang chênh lệch năng lượng, tạo huỳnh quang. Hạt nhỏ hơn thường có khoảng cách mức lớn hơn trong mô hình này, nên phát bước sóng ngắn hơn.\n\nĐây là mô hình giam giữ để hiểu xu hướng. Cấu trúc thực còn có hình dạng, vật liệu, thế giam giữ và tương tác giữa các hạt. Vì thế, màu không phải một phép đo kích thước phổ quát nếu thiếu thông tin về hệ.',
  'kinh-hien-vi-quet-xuyen-ham': 'Đầu dò dẫn điện rất nhọn được đặt cách mẫu dẫn điện một khe cực nhỏ. Khi có điện áp phù hợp, electron có thể xuyên qua khe và tạo dòng điện.\n\nỞ chế độ dòng không đổi, đầu dò quét theo hai phương ngang còn bộ điều khiển điều chỉnh độ cao để giữ dòng. Tập hợp các độ cao qua nhiều đường quét cho một bản đồ tín hiệu bề mặt.\n\nVì dòng xuyên hầm phụ thuộc theo hàm mũ vào khoảng cách, thiết bị cần điều khiển vị trí chính xác và cách ly rung động. Tín hiệu còn nhạy với cấu trúc điện tử và điện áp. Do đó, phải phân biệt bản đồ tín hiệu STM với một phép chụp hình học thuần túy của những nguyên tử dạng quả cầu.',
}

export const quantumWaveWikiConnections = {
  'ham-song-luong-tu': ['mat-do-xac-suat-luong-tu', 'so-phuc-trong-ham-song', 'phuong-trinh-schrodinger'],
  'mat-do-xac-suat-luong-tu': ['ham-song-luong-tu', 'chuan-hoa-ham-song', 'tich-phan'],
  'chuan-hoa-ham-song': ['mat-do-xac-suat-luong-tu', 'hat-trong-hop-luong-tu', 'gieng-the-huu-han'],
  'so-phuc-trong-ham-song': ['ham-song-luong-tu', 'chong-chap-ham-song', 'mat-do-xac-suat-luong-tu'],
  'phuong-trinh-schrodinger': ['dieu-kien-bien-ham-song', 'trang-thai-dung-luong-tu', 'cong-nang-luong'],
  'chong-chap-ham-song': ['so-phuc-trong-ham-song', 'goi-song-luong-tu', 'phep-do-luong-tu'],
  'goi-song-luong-tu': ['chong-chap-ham-song', 'buoc-song-de-broglie', 'phuong-trinh-schrodinger'],
  'trang-thai-dung-luong-tu': ['phuong-trinh-schrodinger', 'chong-chap-ham-song', 'phep-do-luong-tu'],
  'dieu-kien-bien-ham-song': ['phuong-trinh-schrodinger', 'hat-trong-hop-luong-tu', 'gieng-the-huu-han'],
  'hat-trong-hop-luong-tu': ['chuan-hoa-ham-song', 'dieu-kien-bien-ham-song', 'nang-luong-diem-khong'],
  'gieng-the-huu-han': ['trang-thai-lien-ket-luong-tu', 'dieu-kien-bien-ham-song', 'xuyen-ham-luong-tu'],
  'trang-thai-lien-ket-luong-tu': ['gieng-the-huu-han', 'chuan-hoa-ham-song', 'cong-nang-luong'],
  'xuyen-ham-luong-tu': ['gieng-the-huu-han', 'trang-thai-lien-ket-luong-tu', 'kinh-hien-vi-quet-xuyen-ham'],
  'dao-dong-tu-dieu-hoa-luong-tu': ['dao-dong-dieu-hoa', 'nang-luong-diem-khong', 'trang-thai-dung-luong-tu'],
  'nang-luong-diem-khong': ['dao-dong-tu-dieu-hoa-luong-tu', 'hat-trong-hop-luong-tu', 'phuong-trinh-schrodinger'],
  'phep-do-luong-tu': ['chong-chap-ham-song', 'trang-thai-dung-luong-tu', 'mat-do-xac-suat-luong-tu'],
  'cham-luong-tu': ['hat-trong-hop-luong-tu', 'gieng-the-huu-han', 'photon'],
  'kinh-hien-vi-quet-xuyen-ham': ['xuyen-ham-luong-tu', 'dong-dien', 'cham-luong-tu'],
}
