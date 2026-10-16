const term = (name, aliases, definition, example, use, question, answer) => ({
  name, aliases: [...new Set([name, name.toLocaleLowerCase('vi'), ...aliases])],
  definition, example, use, question, answer
})

export const atomicStructureConcepts = {
  'phuong-trinh-schrodinger-ba-chieu': term(
    'Phương trình Schrödinger ba chiều', ['phương trình Schrödinger trong ba chiều'],
    'Phương trình mô tả trạng thái lượng tử theo ba tọa độ. Với khối lượng không đổi, toán tử động năng chứa tổng các đạo hàm bậc hai theo x, y và z.',
    'Trong hộp lập phương, nghiệm tách thành tích ba hàm một chiều khi thế năng và điều kiện biên cho phép tách biến.',
    'Tìm trạng thái dừng, mức năng lượng và phân bố xác suất của hệ có cấu trúc không gian.',
    'Có thể giữ nguyên đạo hàm theo x và chỉ đổi tên hàm sóng thành hàm ba biến không?',
    'Không. Động năng phải kể đủ ba phương. Bỏ các đạo hàm còn lại làm thay đổi bài toán vật lý.'
  ),
  'hat-trong-hop-ba-chieu': term(
    'Hạt trong hộp ba chiều', ['hộp lượng tử ba chiều', 'giếng thế hộp ba chiều'],
    'Mô hình hạt bị giới hạn trong một hộp có thành thế vô hạn. Ba số lượng tử nguyên dương xác định các dạng sóng đứng theo ba trục.',
    'Trong hộp lập phương, các bộ (2,1,1), (1,2,1) và (1,1,2) có cùng năng lượng nhưng là ba trạng thái không gian khác nhau.',
    'Phân tích điều kiện biên, xác suất trong một miền và suy biến do đối xứng hình học.',
    'Bộ có một số lượng tử bằng 0 có phải trạng thái năng lượng thấp nhất không?',
    'Không. Nhân tử sin theo trục đó triệt tiêu ở mọi điểm, làm toàn hàm sóng bằng 0 và không chuẩn hóa được.'
  ),
  'suy-bien-muc-nang-luong': term(
    'Suy biến mức năng lượng', ['suy biến năng lượng', 'độ suy biến'],
    'Một mức năng lượng suy biến khi có nhiều trạng thái riêng độc lập cùng có năng lượng đó. Độ suy biến là số trạng thái độc lập tương ứng.',
    'Ba bộ số lượng tử hoán vị của (2,1,1) tạo độ suy biến không gian bằng 3 trong hộp lập phương.',
    'Đếm trạng thái, phân biệt mức với trạng thái và phân tích sự tách mức khi đối xứng thay đổi.',
    'Ba cách viết cùng một trạng thái chỉ khác pha chung có làm độ suy biến bằng 3 không?',
    'Không. Các trạng thái suy biến phải độc lập. Nhân cùng một hàm sóng với pha chung không tạo trạng thái độc lập mới.'
  ),
  'so-luong-tu-nguyen-tu': term(
    'Số lượng tử nguyên tử', ['bốn số lượng tử', 'bộ số lượng tử nguyên tử'],
    'Trong mô hình trường xuyên tâm, các số $n$, $\\ell$, $m_\\ell$ và $m_s$ mô tả trạng thái một electron. Miền giá trị của chúng có ràng buộc, không được chọn độc lập tùy ý.',
    "Với n = 2, số $\\ell$ chỉ có thể là 0 hoặc 1. Khi $\\ell=1$, $m_\\ell$ nhận −1, 0 hoặc 1.",
    'Xác định trạng thái được phép, độ suy biến, hình chiếu mômen và cấu hình electron.',
    "Bộ n = 2, $\\ell=2$ có được phép không?",
    "Không. Phải có $0\\le\\ell\\le n-1$, nên n = 2 chỉ cho $\\ell=0$ hoặc 1."
  ),
  'orbital-nguyen-tu': term(
    'Orbital nguyên tử', ['orbital', 'obitan nguyên tử'],
    'Trạng thái không gian một electron trong mô hình nguyên tử. Orbital không phải một đường quỹ đạo cổ điển và chưa bao gồm lựa chọn spin.',
    'Một orbital 1s có thể chứa hai electron với hai giá trị spin đối nhau, nhưng không chứa ba electron.',
    'Mô tả phân bố xác suất không gian và phân biệt orbital với trạng thái đầy đủ có spin.',
    'Hình dạng orbital có cho biết electron chạy trên đường nào không?',
    'Không. Đồ thị biểu diễn hàm sóng, mật độ hoặc mặt mức xác suất, tùy cách dựng. Nó không xác định một quỹ đạo chuyển động.'
  ),
  'phan-bo-xac-suat-ban-kinh': term(
    'Phân bố xác suất bán kính', ['phân bố bán kính', 'mật độ xác suất xuyên tâm'],
    'Hàm $P(r)$ được định nghĩa sao cho $P(r)\\,dr$ là xác suất trong vỏ cầu từ r đến r + dr. Nó đã kể yếu tố thể tích và khác mật độ theo thể tích.',
    'Ở trạng thái hydro 1s, mật độ theo thể tích lớn nhất tại hạt nhân, nhưng xác suất theo bán kính đạt cực đại ở một bán kính khác 0.',
    'Tính xác suất trong vỏ cầu và xác định bán kính có mật độ xác suất bán kính lớn nhất.',
    'Mật độ tại tâm lớn nhất có nghĩa xác suất trong một vỏ cầu sát tâm lớn nhất không?',
    'Không. Thể tích vỏ cầu tỉ lệ với $r^2\\,dr$ và tiến về 0 ở tâm. Cần nhân yếu tố hình học trước khi so sánh.'
  ),
  'momen-dong-luong-quy-dao': term(
    'Mômen động lượng quỹ đạo lượng tử', ['mômen quỹ đạo', 'mômen động lượng orbital'],
    "Mômen động lượng gắn với phần không gian của trạng thái. Độ lớn và một hình chiếu có các giá trị lượng tử hóa do $\\ell$ và $m_\\ell$ xác định.",
    "Khi $\\ell=1$, độ lớn bằng $\\sqrt2\\hbar$, còn hình chiếu lên z có ba giá trị −$\\hbar$, 0 và $\\hbar$.",
    'Phân tích trạng thái nguyên tử, mômen từ quỹ đạo và hiệu ứng Zeeman.',
    "Khi $m_\\ell=0$, mômen quỹ đạo có nhất thiết bằng 0 không?",
    "Không. $m_\\ell=0$ chỉ cho hình chiếu lên z bằng 0. Độ lớn còn phụ thuộc $\\ell$ và có thể khác 0."
  ),
  'luong-tu-hoa-khong-gian': term(
    'Lượng tử hóa không gian', ['lượng tử hóa hình chiếu mômen'],
    'Với độ lớn mômen động lượng cho trước, phép đo một hình chiếu chỉ cho các giá trị rời rạc. Không được đồng thời gán ba thành phần như một vector cổ điển xác định.',
    "Với $\\ell=2$, hình chiếu lên trục z có năm giá trị, trong khi độ lớn mômen giữ nguyên.",
    'Đọc sơ đồ mômen quỹ đạo và giải thích sự tách trạng thái trong từ trường.',
    'Đổi hướng trục đo có tạo ra một tập giá trị liên tục không?',
    'Không. Dọc theo trục mới vẫn có cùng tập trị riêng rời rạc, nhưng xác suất các kết quả phụ thuộc trạng thái đã chuẩn bị.'
  ),
  'hieu-ung-zeeman': term(
    'Hiệu ứng Zeeman', ['sự tách mức Zeeman', 'sự tách vạch Zeeman'],
    'Sự dịch hoặc tách mức năng lượng và vạch phổ do tương tác giữa mômen từ nguyên tử với từ trường ngoài.',
    "Khi chỉ xét mômen quỹ đạo, độ dịch năng lượng trong từ trường hướng z tỉ lệ với $m_\\ell$ và độ lớn B.",
    'Phân tích ảnh hưởng của từ trường lên phổ nguyên tử và phân biệt đóng góp quỹ đạo với spin.',
    "Có 2$\\ell$ + 1 mức con có bảo đảm quan sát đúng 2$\\ell$ + 1 vạch không?",
    'Không. Vạch phát ra phụ thuộc cả hai mức tham gia, điều kiện chọn và khả năng phân giải. Số mức con không tự động bằng số vạch.'
  ),
  'magneton-bohr': term(
    'Magneton Bohr', ['magneton Bohr μB'],
    "Thang mômen từ của electron, bằng e $\\hbar$ chia cho hai lần khối lượng electron. Đơn vị là joule trên tesla.",
    "Độ dịch Zeeman quỹ đạo của một trạng thái bằng $m_\\ell$ lần magneton Bohr nhân với B trong mô hình đang xét.",
    'Tính mômen từ electron, độ tách mức và tần số cộng hưởng.',
    'Magneton Bohr có phải đơn vị năng lượng không?',
    'Không. Nó có đơn vị mômen từ. Nhân với từ trường mới cho một năng lượng.'
  ),
  'spin-luong-tu': term(
    'Spin lượng tử', ['spin electron', 'spin nội tại electron', 'spin 1/2'],
    'Mômen động lượng nội tại của hạt. Electron có số lượng tử spin bằng 1/2, nên phép đo hình chiếu cho một trong hai giá trị đối nhau.',
    "Hai trạng thái có hình chiếu spin lên z bằng cộng hoặc trừ $\\hbar/2$.",
    'Phân tích Stern–Gerlach, cấu hình electron, cộng hưởng spin và phép đo trạng thái hai mức.',
    'Với electron, hai kết quả hình chiếu có nghĩa vector spin chỉ có thể nằm đúng trên hoặc dưới trục z không?',
    "Không. Hình chiếu có hai trị riêng nhưng độ lớn spin bằng $\\sqrt3\\hbar/2$. Mô hình vector cổ điển xác định mọi thành phần không áp dụng."
  ),
  'thi-nghiem-stern-gerlach': term(
    'Thí nghiệm Stern–Gerlach', ['Stern–Gerlach'],
    'Thí nghiệm cho chùm nguyên tử đi qua từ trường không đều để các trạng thái mômen từ khác nhau chịu lực và lệch theo các hướng rời rạc.',
    'Chùm nguyên tử thích hợp có mômen chủ yếu do một electron chưa ghép đôi có thể tách thành hai nhánh.',
    'Kiểm tra lượng tử hóa hình chiếu mômen và chuẩn bị trạng thái theo một trục đo.',
    'Từ trường đều có tạo sự tách vị trí tương tự không?',
    'Không. Cần gradient từ trường để có lực tịnh tiến phụ thuộc hình chiếu mômen. Từ trường đều có thể tạo mômen lực nhưng không cho lực gradient đó.'
  ),
  'tuong-tac-spin-quy-dao': term(
    'Tương tác spin–quỹ đạo', ['ghép spin–quỹ đạo', 'liên kết spin–quỹ đạo'],
    'Tương tác giữa mômen từ spin với từ trường hiệu dụng gắn với chuyển động tương đối của electron và hạt nhân. Nó góp phần tạo cấu trúc tinh tế của phổ.',
    "Hai trạng thái có cùng n và $\\ell$ nhưng khác số lượng tử tổng j có thể có năng lượng hơi khác nhau.",
    'Phân tích cấu trúc đôi vạch phổ và phân biệt các mức có tổng mômen khác nhau.',
    "Mọi trường hợp $\\ell$ đều có hai giá trị $j=\\ell\\pm1/2$ không?",
    "Không. Với $\\ell=0$ chỉ có j = 1/2. Nhánh $\\ell-1/2$ chỉ tồn tại khi $\\ell$ ít nhất bằng 1."
  ),
  'nguyen-ly-pauli': term(
    'Nguyên lý loại trừ Pauli', ['nguyên lý Pauli', 'loại trừ Pauli'],
    'Các fermion giống nhau không cùng chiếm một trạng thái một hạt. Trong mô hình nguyên tử, không có hai electron có cùng cả bốn số lượng tử.',
    'Một orbital chứa tối đa hai electron có spin đối nhau. Phân lớp s có hai trạng thái kể spin, còn phân lớp p có sáu.',
    'Lập cấu hình electron, đếm trạng thái và giải thích tính chất tuần hoàn của các nguyên tố.',
    "Hai electron có cùng ba số n, $\\ell$ và $m_\\ell$ có luôn vi phạm Pauli không?",
    'Không. Chúng được phép có cùng orbital nếu hai số ms khác nhau. Nếu cả bốn số giống nhau thì trạng thái bị loại.'
  ),
  'cau-hinh-electron': term(
    'Cấu hình electron', ['cấu hình electron nguyên tử'],
    'Cách phân bố electron vào các trạng thái hoặc phân lớp của nguyên tử dưới ràng buộc Pauli và trật tự năng lượng thích hợp.',
    'Ký hiệu $1s^2\\,2s^1$ cho biết liti có hai electron trong phân lớp 1s và một electron trong phân lớp 2s.',
    'Liên hệ cấu trúc nguyên tử với bảng tuần hoàn, ion hóa và phản ứng hóa học.',
    'Có thể dùng thứ tự năng lượng của hydro cho mọi nguyên tử nhiều electron không?',
    "Không. Tương tác và che chắn làm năng lượng phụ thuộc cả n và $\\ell$. Các phân lớp cùng n không còn nhất thiết đồng năng lượng."
  ),
  'che-chan-dien-tich-hat-nhan': term(
    'Che chắn điện tích hạt nhân', ['điện tích hạt nhân hiệu dụng', 'điện tích hiệu dụng Zeff'],
    'Sự giảm tác dụng hút của hạt nhân lên một electron do các electron còn lại. Điện tích hiệu dụng là tham số gần đúng của trạng thái đang xét.',
    'Electron ngoài cùng của kim loại kiềm chịu trường hút yếu hơn nhiều so với trường của hạt nhân trần.',
    'Ước lượng năng lượng liên kết, xu hướng ion hóa và sự phụ thuộc năng lượng vào phân lớp.',
    'Một nguyên tử có nhất thiết chỉ có một giá trị Zeff dùng cho mọi electron không?',
    'Không. Mức xuyên sâu và phân bố không gian khác nhau khiến giá trị hiệu dụng phụ thuộc trạng thái. Cần nêu mô hình dùng để suy ra nó.'
  ),
  'pho-tia-x-dac-trung': term(
    'Phổ tia X đặc trưng', ['tia X đặc trưng', 'vạch Kα', 'vạch Kβ'],
    'Các vạch tia X do electron chuyển xuống lỗ trống ở mức bên trong nguyên tử. Năng lượng photon bằng hiệu năng lượng hai trạng thái tham gia.',
    'Vạch Kα gắn với chuyển xuống lớp K từ lớp L, còn Kβ gắn với chuyển xuống lớp K từ lớp M.',
    'Nhận diện nguyên tố và khảo sát cấu trúc các mức sâu của nguyên tử.',
    'Tăng điện áp ống tia X có liên tục dời vị trí mọi vạch đặc trưng không?',
    'Không trong mô hình mục tiêu cố định đang xét. Điện áp quyết định khả năng kích thích và nền hãm, còn vị trí các vạch đặc trưng chủ yếu do mức năng lượng của nguyên tố.'
  ),
  'dinh-luat-moseley': term(
    'Định luật Moseley', ['quan hệ Moseley'],
    'Quan hệ gần đúng giữa căn bậc hai tần số tia X đặc trưng và số hiệu nguyên tử, sau khi kể che chắn thích hợp.',
    'Với vạch Kα trong mô hình che chắn đơn giản, tần số tỉ lệ với bình phương Z − 1.',
    'Ước lượng tần số vạch đặc trưng hoặc suy ra số hiệu nguyên tử từ quang phổ.',
    'Có thể dùng cùng hệ số Kα cho mọi họ vạch tia X không?',
    'Không. Hệ số và tham số che chắn phụ thuộc họ chuyển mức. Phải xác định vạch đang xét trước khi thay số.'
  ),
  'roi-luong-tu': term(
    'Rối lượng tử', ['trạng thái rối', 'vướng víu lượng tử'],
    'Với trạng thái thuần, rối là tính chất không thể biểu diễn trạng thái toàn hệ thành tích các trạng thái riêng. Các phép đo có thể có tương quan phụ thuộc cơ sở đo.',
    'Trạng thái spin singlet cho kết quả đối nhau khi đo hai spin theo cùng một trục, nhưng từng kết quả riêng vẫn ngẫu nhiên.',
    'Phân tích tương quan lượng tử, phép đo có điều kiện và tài nguyên cho xử lý thông tin lượng tử.',
    'Tương quan đối nhau khi đo cùng một trục có tự nó chứng minh rối lượng tử không?',
    'Không. Một hỗn hợp cổ điển cũng có thể tạo tương quan trong một cơ sở. Cần xét trạng thái hoặc các phép đo thích hợp theo nhiều cơ sở.'
  ),
  'qubit': term(
    'Qubit', ['bit lượng tử'],
    'Hệ lượng tử có hai trạng thái cơ sở trực chuẩn. Trạng thái thuần là tổ hợp tuyến tính chuẩn hóa của hai trạng thái cơ sở đó.',
    'Phép đo trong cơ sở 0 và 1 cho một trong hai kết quả, với xác suất là bình phương môđun của biên độ tương ứng.',
    'Mô tả cổng lượng tử, chồng chập và rối trong tính toán lượng tử.',
    'Một qubit chồng chập có cho phép đọc đồng thời vô hạn bit cổ điển không?',
    'Không. Mỗi phép đo trong cơ sở đã chọn cho một kết quả. Muốn suy ra tham số trạng thái cần nhiều lần chuẩn bị và đo.'
  ),
}

const block=tex=>'$$\n'+tex+'\n$$'
const detail=(...paragraphs)=>paragraphs.join('\n\n')

export const atomicStructureWikiDetails = {
  'phuong-trinh-schrodinger-ba-chieu': detail(
    'Chọn một mô hình một hạt phi tương đối tính có khối lượng không đổi. Trong ba chiều, động năng có ba đóng góp tương ứng với ba phương độc lập. Vì thế toán tử động năng chứa toán tử Laplace.',
    block('\\begin{aligned}\\nabla^2\\psi&=\\psi_{xx}+\\psi_{yy}+\\psi_{zz},\\\\\\psi_{xx}&=\\frac{\\partial^2\\psi}{\\partial x^2}.\\end{aligned}'),
    'Hai đạo hàm theo y và z được định nghĩa tương tự. Khi thế năng không phụ thuộc thời gian, nghiệm riêng năng lượng thỏa phương trình sau.',
    block('-\\frac{\\hbar^2}{2m}\\nabla^2\\psi+U\\psi=E\\psi.'),
    'Miền không gian, điều kiện tại biên và điều kiện ở vô cực chọn những nghiệm có ý nghĩa vật lý. Nghiệm đại số của phương trình vi phân chưa đủ nếu không thỏa các điều kiện ấy. Với hàm sóng đã chuẩn hóa, xác suất trong một miền được tính bằng tích phân bình phương môđun theo thể tích.'
  ),
  'hat-trong-hop-ba-chieu': detail(
    'Xét hộp lập phương cạnh L, đáy thế bằng không và thành vô hạn. Hàm sóng phải triệt tiêu ở sáu mặt. Vì ba phương tách được, ta viết hàm riêng thành tích ba nghiệm một chiều.',
    block('\\psi(x,y,z)=X(x)Y(y)Z(z).'),
    'Mỗi nhân tử là một sóng sin có nút ở hai thành tương ứng. Ba số lượng tử đều bắt đầu từ 1. Nếu một số bằng 0, một nhân tử và do đó toàn hàm sóng đều triệt tiêu.',
    block('\\begin{aligned}N&=n_x^2+n_y^2+n_z^2,\\\\E&=\\frac{N\\pi^2\\hbar^2}{2mL^2}.\\end{aligned}'),
    'Xác suất trong một miền chữ nhật được tính bằng tích các tích phân một chiều khi trạng thái đang xét là nghiệm tích. Điều này không cho phép thay xác suất bằng tỉ lệ thể tích, vì mật độ lượng tử nói chung không đều. Với tổ hợp các trạng thái suy biến, phải tính bình phương môđun của toàn tổ hợp trước.'
  ),
  'suy-bien-muc-nang-luong': detail(
    'Phân biệt một mức năng lượng với một trạng thái. Mức là một trị riêng của Hamilton. Trong không gian các nghiệm ứng với trị riêng ấy, có thể có nhiều trạng thái độc lập.',
    'Trong hộp lập phương, ba bộ (2,1,1), (1,2,1) và (1,1,2) đều cho tổng bình phương bằng 6. Các hàm sóng tương ứng trực giao và có cùng năng lượng, nên độ suy biến không gian của mức đó bằng 3.',
    'Một tổ hợp tuyến tính của các trạng thái trong cùng không gian suy biến vẫn là trạng thái riêng năng lượng. Tuy nhiên, số tổ hợp có thể viết không phải độ suy biến. Độ suy biến là số phần tử độc lập của một cơ sở.',
    'Đối xứng hình học hoặc động lực học có thể gây suy biến. Thay đổi hình dạng hộp hay đặt từ trường có thể phá đối xứng và làm tách mức. Khi đếm, cần nói rõ có kể spin, cấu trúc tinh tế hoặc từ trường hay chưa.'
  ),
  'so-luong-tu-nguyen-tu': detail(
    "Trong nguyên tử hydro ở mô hình Coulomb phi tương đối tính, ba số lượng tử không gian là n, $\\ell$ và $m_\\ell$. Spin thêm số m_s. Các miền không gian được chọn bởi tính chuẩn hóa, điều kiện tại gốc và tính đơn trị theo góc.",
    block('\\begin{aligned}&n=1,2,3,\\dots,\\\\&\\ell=0,1,\\dots,n-1,\\\\&m_\\ell=-\\ell,\\dots,\\ell.\\end{aligned}'),
    "Với mỗi orbital không gian, electron có hai giá trị hình chiếu spin. Không được chọn $\\ell$ độc lập với n hoặc chọn $m_\\ell$ vượt quá $\\ell$. Chẳng hạn, n = 2 không cho phép $\\ell=2$.",
    'Trong hydro ở gần đúng này, năng lượng chỉ phụ thuộc n. Những số còn lại vẫn phân biệt trạng thái. Trong nguyên tử nhiều electron, che chắn và tương tác làm năng lượng phụ thuộc thêm vào phân lớp và các đặc trưng khác.'
  ),
  'orbital-nguyen-tu': detail(
    "Một orbital mô tả phần không gian của trạng thái một electron. Trong trường xuyên tâm, orbital thường được phân loại bằng n, $\\ell$ và $m_\\ell$. Các chữ s, p, d và f lần lượt tương ứng với $\\ell$ bằng 0, 1, 2 và 3.",
    'Hình ảnh orbital phải được đọc theo chú thích. Một hình có thể là đồ thị hàm sóng, lát cắt của mật độ hoặc mặt bao một tỉ lệ xác suất. Chúng không có cùng ý nghĩa và đều khác một đường chuyển động của electron.',
    'Spin chưa nằm trong khái niệm orbital không gian này. Hai electron có thể cùng chiếm một orbital nếu chúng có spin đối nhau. Thêm electron thứ ba vào đúng orbital đó vi phạm nguyên lý loại trừ.',
    'Hình dạng orbital phản ánh đối xứng và cấu trúc nút của hàm sóng. Nó hỗ trợ phân tích liên kết và tương tác, nhưng không cấp cho electron một vị trí cùng vận tốc xác định tại mọi thời điểm.'
  ),
  'phan-bo-xac-suat-ban-kinh': detail(
    'Mật độ theo thể tích cho xác suất trong một phần tử không gian. Nếu chỉ quan tâm khoảng cách tới hạt nhân, phải cộng xác suất qua mọi hướng trên cùng một vỏ cầu.',
    'Với hàm sóng không phụ thuộc góc, chẳng hạn trạng thái hydro 1s, mật độ theo bán kính là:',
    block('P(r)=4\\pi r^2|\\psi(r)|^2.'),
    'Nếu tách hàm sóng thành phần xuyên tâm R và phần góc đã chuẩn hóa, công thức tổng quát tương ứng là:',
    block('P(r)=r^2|R(r)|^2.'),
    'Xác suất trong khoảng bán kính bằng tích phân của P theo r, không phải diện tích dưới đồ thị bình phương môđun theo r khi thiếu yếu tố thể tích. Với 1s, mật độ theo thể tích lớn nhất tại tâm nhưng P bằng 0 ở tâm và đạt cực đại tại r = a.'
  ),
  'momen-dong-luong-quy-dao': detail(
    "Trong trường xuyên tâm, có thể chọn trạng thái có độ lớn mômen quỹ đạo và một hình chiếu xác định. Hai số lượng tử $\\ell$ và $m_\\ell$ cho:",
    block('\\begin{aligned}L&=\\sqrt{\\ell(\\ell+1)}\\,\\hbar,\\\\L_z&=m_\\ell\\hbar.\\end{aligned}'),
    "Với $\\ell=1$, độ lớn là $\\sqrt2\\hbar$, còn hình chiếu nhận ba giá trị. Hình chiếu bằng không không làm độ lớn bằng không.",
    'Sơ đồ vector lượng tử có ích để theo dõi độ lớn và một hình chiếu, nhưng không được diễn giải như một vector cổ điển có đồng thời ba thành phần xác định. Các thành phần mômen theo các trục khác nhau không đồng thời có giá trị sắc nét trong trạng thái tổng quát.',
    'Tên quỹ đạo chỉ phân biệt đóng góp do phần không gian với spin nội tại. Nó không khẳng định electron chuyển động trên một quỹ đạo Bohr cụ thể.'
  ),
  'luong-tu-hoa-khong-gian': detail(
    "Chọn một trục đo z. Với số lượng tử mômen $\\ell$, phép đo hình chiếu có các kết quả $m_\\ell$ $\\hbar$. Có đúng 2$\\ell$ + 1 giá trị từ −$\\ell$ đến $\\ell$.",
    'Nếu đổi trục đo, tập trị riêng vẫn có dạng rời rạc tương ứng. Điều thay đổi là cách trạng thái đã chuẩn bị được khai triển trong cơ sở mới, nên xác suất các kết quả có thể thay đổi.',
    'Không được hiểu lượng tử hóa không gian là sự ưu tiên tuyệt đối của một trục trong tự nhiên. Trục được chọn bởi dụng cụ đo hoặc bởi từ trường ngoài.',
    'Thí nghiệm Stern–Gerlach biến sự khác biệt của mômen từ thành độ lệch của các nhánh chùm nguyên tử. Để có lực tách, trường phải không đều trong không gian.'
  ),
  'hieu-ung-zeeman': detail(
    'Mômen từ tương tác với từ trường qua năng lượng âm của tích vô hướng. Khi chỉ xét mômen quỹ đạo của electron và chọn B theo dương trục z:',
    block('\\begin{aligned}\\mu_z&=-m_\\ell\\mu_{\\rm B},\\\\U&=-\\mu_zB=m_\\ell\\mu_{\\rm B}B.\\end{aligned}'),
    "Những trạng thái vốn cùng năng lượng nhưng khác $m_\\ell$ có thể dịch lên hoặc xuống khác nhau. Dấu của độ dịch phải được suy từ điện tích electron âm, không được suy chỉ từ chiều của mômen động lượng.",
    'Phổ quan sát là tập các hiệu năng lượng của những chuyển mức được phép. Vì vậy, số mức con không tự động bằng số vạch. Cần xét cả hai mức và điều kiện chọn.',
    "Khi kể spin và tương tác spin–quỹ đạo, mô tả mức con thay đổi. Công thức chỉ dùng $m_\\ell$ ở trên là một mô hình cụ thể, không phải biểu thức đầy đủ cho mọi từ trường và mọi nguyên tử."
  ),
  'magneton-bohr': detail(
    'Magneton Bohr được định nghĩa từ độ lớn điện tích electron, khối lượng electron và hằng số Planck rút gọn:',
    block('\\mu_{\\rm B}=\\frac{e\\hbar}{2m_e}.'),
    'Giá trị gần đúng là $9{,}274\\times10^{-24}\\,\\mathrm{J/T}$. Đây là một thang mômen từ. Năng lượng tương tác xuất hiện khi nhân mômen thích hợp với độ lớn từ trường.',
    "Mômen từ quỹ đạo của electron có hình chiếu bằng −$m_\\ell$ lần magneton Bohr. Mômen spin có thêm hệ số g gần bằng 2, nên cần phân biệt hai đóng góp.",
    'Magneton Bohr không phải một mômen luôn có cùng hướng hoặc độ lớn với mọi electron trong nguyên tử. Các trạng thái và cách cộng mômen quyết định mômen toàn hệ.'
  ),
  'spin-luong-tu': detail(
    'Spin là mômen động lượng nội tại của hạt. Với số lượng tử spin s, độ lớn và một hình chiếu có dạng:',
    block('\\begin{aligned}S&=\\sqrt{s(s+1)}\\,\\hbar,\\\\S_z&=m_s\\hbar.\\end{aligned}'),
    "Số m_s chạy từ −s đến s theo bước 1. Electron có s = 1/2, nên hai giá trị hình chiếu là cộng hoặc trừ $\\hbar/2$. Độ lớn spin electron là $\\sqrt3\\hbar/2$, không bằng độ lớn một hình chiếu.",
    'Các trạng thái spin theo các trục đo khác nhau là những cơ sở khác nhau. Một trạng thái có hình chiếu z xác định không vì thế có đồng thời hình chiếu x xác định.',
    'Không mô tả spin như sự quay của một quả cầu vật chất electron. Khái niệm đó không giải thích đúng các trị riêng, phép đo và mômen từ nội tại.'
  ),
  'thi-nghiem-stern-gerlach': detail(
    'Cho chùm nguyên tử trung hòa thích hợp đi qua một vùng từ trường có gradient. Các trạng thái mômen từ chịu lực khác nhau và tạo những nhánh phân biệt trên màn.',
    block('F_z\\approx\\mu_z\\frac{\\partial B_z}{\\partial z}.'),
    'Công thức diễn tả cơ chế lực gradient trong điều kiện mômen được định hướng thích hợp. Từ trường đều có thể tạo mômen lực và sự tiến động, nhưng không tạo lực gradient cần cho phép tách vị trí này.',
    'Dùng nguyên tử trung hòa giúp tránh lực Lorentz lớn lên điện tích tổng làm lẫn cơ chế tách. Không thể thay bằng một chùm ion trong cùng bố trí mà coi mọi quỹ đạo lệch chỉ do spin.',
    'Phép tách và chọn một nhánh cũng là cách chuẩn bị trạng thái theo một trục. Đo tiếp theo một trục khác cần khai triển trạng thái trong cơ sở tương ứng, không gán sẵn mọi hình chiếu.'
  ),
  'tuong-tac-spin-quy-dao': detail(
    'Chuyển động tương đối của electron và hạt nhân tạo cách mô tả một từ trường hiệu dụng tác dụng lên mômen từ spin. Khi xử lý nhất quán, đóng góp này gắn với tương tác giữa spin và mômen quỹ đạo.',
    block('\\mathbf J=\\mathbf L+\\mathbf S.'),
    "Với electron, các giá trị tổng j là $\\ell+1/2$ và $\\ell-1/2$, trừ trường hợp $\\ell=0$ chỉ có j = 1/2. Những trạng thái cùng n và $\\ell$ nhưng khác j có thể bị tách năng lượng.",
    'Cấu trúc tinh tế của hydro còn có các hiệu chỉnh tương đối tính. Không quy mọi tách mức nhỏ cho riêng một cơ chế hoặc dùng một từ trường ngoài tùy ý thay cho tương tác nội tại.',
    'Khi so sánh bước sóng hai vạch rất gần nhau, cần lấy hiệu năng lượng photon bằng hc nhân hiệu hai nghịch đảo bước sóng. Hiệu bước sóng không tỉ lệ trực tiếp với hiệu năng lượng nếu bỏ mẫu số.'
  ),
  'nguyen-ly-pauli': detail(
    "Nguyên lý loại trừ áp dụng cho fermion giống nhau. Electron là fermion. Trong mô hình trạng thái một electron của nguyên tử, hai electron không thể có cùng cả n, $\\ell$, $m_\\ell$ và m_s.",
    "Một orbital không gian cố định n, $\\ell$ và $m_\\ell$ còn hai lựa chọn spin, nên chứa tối đa hai electron. Phân lớp s có một orbital và chứa tối đa hai electron. Phân lớp p có ba orbital và chứa tối đa sáu electron.",
    'Với lớp $n=2$, số trạng thái kể spin bằng $2+6=8$. Tổng quát, phân lớp $\\ell$ có $2(2\\ell+1)$ trạng thái kể spin, và lớp chính n có $2n^2$ trạng thái.',
    'Việc đếm sức chứa không tự xác định thứ tự năng lượng trong nguyên tử nhiều electron. Cần thêm tương tác, che chắn và cấu trúc mức. Với trạng thái nhiều fermion, toàn hàm sóng phải có tính đối xứng lẻ dưới hoán đổi hai hạt, kể cả các biến spin.'
  ),
  'cau-hinh-electron': detail(
    'Cấu hình electron ghi cách electron chiếm các phân lớp. Chỉ số trên cho số electron trong phân lớp, không phải số lượng tử mới. Chẳng hạn, cấu hình liti là:',
    block('1s^2\\,2s^1.'),
    'Trạng thái cơ bản được tìm bằng cách lấp đầy các trạng thái dưới ràng buộc Pauli và trật tự năng lượng thích hợp. Trong nguyên tử nhiều electron, các phân lớp cùng số n không nhất thiết có cùng năng lượng.',
    'Không được suy cấu hình chỉ từ thứ tự n tăng. Các phân lớp của những lớp khác nhau có thể xen kẽ năng lượng, và có những ngoại lệ cần xét theo cấu trúc cụ thể.',
    'Phải giữ phân biệt nguyên tử trung hòa với ion. Số electron và thứ tự mất electron khi ion hóa là những thông tin riêng của tình huống đang xét, không thể đổi cấu hình bằng một quy tắc điền ngược máy móc.'
  ),
  'che-chan-dien-tich-hat-nhan': detail(
    'Mỗi electron chịu hút của hạt nhân và đẩy của các electron còn lại. Trong gần đúng trường xuyên tâm, ta mô tả tác dụng tổng hợp bằng một thế trung bình đối xứng tâm.',
    'Điện tích hiệu dụng gắn với một trạng thái có thể được ước lượng từ năng lượng liên kết theo:',
    block('E_n\\approx-\\frac{Z_{\\rm eff}^2}{n^2}E_{\\rm H}.'),
    'Ở đây E_H gần bằng 13,6 eV. Công thức là một mô hình gần đúng, không làm nguyên tử nhiều electron trở thành một hệ Coulomb chính xác với cùng Z_eff cho mọi trạng thái.',
    'Những orbital có độ xuyên sâu khác nhau lấy mẫu các miền thế khác nhau. Vì thế, năng lượng và điện tích hiệu dụng phụ thuộc phân lớp. Khi suy từ năng lượng ion hóa theo mol, phải đổi sang năng lượng của một electron trước khi áp dụng.'
  ),
  'pho-tia-x-dac-trung': detail(
    'Khi lấy đi một electron ở mức sâu, nguyên tử có một lỗ trống. Electron ở mức cao hơn có thể chuyển xuống và phát photon mang hiệu năng lượng hai mức.',
    block('\\begin{aligned}E_\\gamma&=E_i-E_f,\\\\\\lambda&=\\frac{hc}{E_\\gamma}.\\end{aligned}'),
    'Các chuyển xuống lớp K từ lớp L và M tương ứng với các họ Kα và Kβ. Cần biết mức đầu, mức cuối và nguyên tố, không chỉ biết điện áp gia tốc electron trong ống phát.',
    'Nền tia X liên tục do bức xạ hãm là một cơ chế khác. Năng lượng cực đại của nền liên tục bị giới hạn bởi năng lượng electron tới, còn các vạch đặc trưng phản ánh cấu trúc mức của mục tiêu.',
    'Có lỗ trống cũng chưa bảo đảm mọi hiệu năng lượng hình thức đều cho một vạch phát xạ mạnh. Điều kiện chọn, xác suất chuyển mức và các cơ chế cạnh tranh quyết định phổ quan sát.'
  ),
  'dinh-luat-moseley': detail(
    'Trong mô hình đơn giản cho vạch Kα, electron chuyển từ lớp L xuống một lỗ trống ở lớp K. Electron còn lại trong lớp K che chắn gần một đơn vị điện tích hạt nhân.',
    block('\\begin{aligned}C&\\approx2{,}48\\times10^{15}\\,\\mathrm{Hz},\\\\f&\\approx C(Z-1)^2.\\end{aligned}'),
    'Vì vậy đồ thị căn bậc hai tần số theo số hiệu nguyên tử gần một đường thẳng. Độ dốc và giao điểm được diễn giải trong mô hình che chắn, không phải như một định luật chính xác cho mọi nguyên tố và mọi vạch.',
    'Muốn nhận diện nguyên tố, cần xác định đúng họ vạch và đổi bước sóng thành tần số trước. Nếu dùng năng lượng photon, phải kể h khi nối với tần số.',
    'Các họ Kβ hoặc L có mức đầu và cuối khác, nên không dùng nguyên hệ số Kα. Việc mở rộng ngoài mô hình đơn giản còn cần hiệu chỉnh che chắn và tương đối tính.'
  ),
  'roi-luong-tu': detail(
    'Với hai hệ phân biệt được theo các phương tiện đo thích hợp, một trạng thái thuần tách được nếu viết thành tích hai trạng thái riêng. Nếu không thể làm như vậy, trạng thái là rối.',
    'Một tổ hợp mạch lạc của hai cấu hình không giống hỗn hợp cổ điển chỉ gán xác suất cho từng cấu hình. Pha tương đối có thể làm khác các tương quan khi đổi cơ sở đo.',
    'Trạng thái spin singlet cho kết quả đối nhau khi đo theo cùng một trục. Tuy nhiên, riêng tương quan ở một trục không đủ loại mọi mô hình hỗn hợp cổ điển. Cần xét cấu trúc trạng thái hoặc những phép đo theo các trục thích hợp.',
    'Kết quả riêng lẻ vẫn có thể ngẫu nhiên. Việc chọn phép đo ở một phía không cho phép điều khiển kết quả phía kia để truyền thông tin nhanh hơn ánh sáng. Tương quan có điều kiện được xác định khi ghép và so sánh kết quả đo.'
  ),
  'qubit': detail(
    'Chọn hai trạng thái cơ sở trực chuẩn, ký hiệu 0 và 1. Một trạng thái thuần của qubit có dạng:',
    block('\\begin{aligned}|\\psi\\rangle&=a|0\\rangle+b|1\\rangle,\\\\|a|^2+|b|^2&=1.\\end{aligned}'),
    'Nếu đo trong cơ sở đó, xác suất hai kết quả lần lượt là bình phương môđun của a và b. Pha chung không quan sát được trong các xác suất, còn pha tương đối có thể ảnh hưởng kết quả khi đổi cơ sở.',
    'Một phép đo không trả lại đồng thời cả hai biên độ phức. Muốn xác định trạng thái cần nhiều hệ được chuẩn bị giống nhau và những phép đo thích hợp.',
    'Nhiều qubit có thể ở trạng thái rối. Khả năng xử lý thông tin phụ thuộc cách điều khiển biên độ và giao thoa, không phải quyền đọc ngay mọi cấu hình cơ sở bằng một lần đo.'
  ),
}

export const atomicStructureWikiConnections = {
  'phuong-trinh-schrodinger-ba-chieu':['phuong-trinh-schrodinger','hat-trong-hop-ba-chieu','chuan-hoa-ham-song'],
  'hat-trong-hop-ba-chieu':['dieu-kien-bien-ham-song','suy-bien-muc-nang-luong','nguyen-ly-pauli'],
  'suy-bien-muc-nang-luong':['hat-trong-hop-ba-chieu','so-luong-tu-nguyen-tu','hieu-ung-zeeman'],
  'so-luong-tu-nguyen-tu':['orbital-nguyen-tu','momen-dong-luong-quy-dao','spin-luong-tu'],
  'orbital-nguyen-tu':['so-luong-tu-nguyen-tu','phan-bo-xac-suat-ban-kinh','cau-hinh-electron'],
  'phan-bo-xac-suat-ban-kinh':['mat-do-xac-suat-luong-tu','orbital-nguyen-tu','tich-phan'],
  'momen-dong-luong-quy-dao':['so-luong-tu-nguyen-tu','luong-tu-hoa-khong-gian','magneton-bohr'],
  'luong-tu-hoa-khong-gian':['momen-dong-luong-quy-dao','thi-nghiem-stern-gerlach','spin-luong-tu'],
  'hieu-ung-zeeman':['magneton-bohr','momen-dong-luong-quy-dao','tuong-tac-spin-quy-dao'],
  'magneton-bohr':['hieu-ung-zeeman','spin-luong-tu','tu-truong'],
  'spin-luong-tu':['thi-nghiem-stern-gerlach','nguyen-ly-pauli','luong-tu-hoa-khong-gian'],
  'thi-nghiem-stern-gerlach':['spin-luong-tu','magneton-bohr','phep-do-luong-tu'],
  'tuong-tac-spin-quy-dao':['momen-dong-luong-quy-dao','spin-luong-tu','hieu-ung-zeeman'],
  'nguyen-ly-pauli':['spin-luong-tu','cau-hinh-electron','suy-bien-muc-nang-luong'],
  'cau-hinh-electron':['nguyen-ly-pauli','orbital-nguyen-tu','che-chan-dien-tich-hat-nhan'],
  'che-chan-dien-tich-hat-nhan':['cau-hinh-electron','so-luong-tu-nguyen-tu','pho-tia-x-dac-trung'],
  'pho-tia-x-dac-trung':['photon','dinh-luat-moseley','che-chan-dien-tich-hat-nhan'],
  'dinh-luat-moseley':['pho-tia-x-dac-trung','photon','cau-hinh-electron'],
  'roi-luong-tu':['chong-chap-ham-song','phep-do-luong-tu','qubit'],
  'qubit':['roi-luong-tu','so-phuc-trong-ham-song','phep-do-luong-tu'],
}
