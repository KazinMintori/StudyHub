const math=tex=>'$$\n'+tex+'\n$$'
const item=(name,description,formula='')=>({name,description,formula,variables:[]})
const note='22-chat-ran-ban-dan'
const slide=(title,bullets,formula='')=>({title,bullets,formula,note})

export const moleculesCheatsheet={
  title:'Cheatsheet: Phân tử và vật chất ngưng tụ',
  description:'Định nghĩa, tính chất, điều kiện và công thức về liên kết, phổ phân tử, tinh thể, electron và bán dẫn.',
  sections:[
    {id:'bonds',title:'Liên kết phân tử',items:[
      item('Liên kết ion','Tương tác giữa các ion trái dấu được tạo bởi sự chuyển electron. Năng lượng tạo ion và lực đẩy ở khoảng cách ngắn đều thuộc cân bằng năng lượng.'),
      item('Liên kết cộng hóa trị','Các nguyên tử chia sẻ electron trong trạng thái phân tử. Phân bố electron và tính đối xứng của trạng thái quyết định tính định hướng của liên kết.'),
      item('Liên kết van der Waals và hydro','Tương tác lưỡng cực thường trực hoặc cảm ứng tạo liên kết van der Waals. Liên kết hydro gắn với nguyên tử hydro liên kết phân cực và tương tác với một nguyên tử nhận thích hợp.'),
      item('Thế Coulomb của hai ion','q₁ và q₂ là điện tích điểm, r là khoảng cách. Mốc thế năng ở vô cực.',math('U(r)=\\frac{q_1q_2}{4\\pi\\varepsilon_0r}')),
      item('Điều kiện cân bằng bền','Thế năng khả vi theo tọa độ khoảng cách. Điều kiện đạo hàm bậc hai dương là điều kiện đủ cho cực tiểu nghiêm ngặt.',math("\\begin{aligned}&U'(r_0)=0\\\\&U''(r_0)>0\\end{aligned}")),
    ]},
    {id:'spectra',title:'Phổ quay và dao động',items:[
      item('Khối lượng rút gọn','Hai nguyên tử có khối lượng m₁ và m₂. Khoảng cách cân bằng giữa các hạt nhân là r₀.',math('\\mu=\\frac{m_1m_2}{m_1+m_2}')),
      item('Mômen quán tính phân tử hai nguyên tử','Trục qua khối tâm và vuông góc với đường nối hai hạt nhân. Mô hình rotor cứng giữ r₀ không đổi.',math('I=\\mu r_0^2')),
      item('Năng lượng quay','Số lượng tử quay ℓ nhận các giá trị 0, 1, 2, … trong mô hình rotor cứng.',math('E_\\ell=\\frac{\\ell(\\ell+1)\\hbar^2}{2I}')),
      item('Quy tắc chọn lọc quay','Chuyển mức lưỡng cực điện của phân tử có mômen lưỡng cực thích hợp. Độ biến thiên số lượng tử quay bằng một đơn vị.',math('\\Delta\\ell=\\pm1')),
      item('Tần số dao động','Gần khoảng cách cân bằng, k′ là hằng số lực và μ là khối lượng rút gọn.',math("\\omega=\\sqrt{\\frac{k'}{\\mu}}")),
      item('Năng lượng dao động','Mô hình dao động tử điều hòa. Số lượng tử n nhận các giá trị 0, 1, 2, …',math('E_n=(n+\\tfrac12)\\hbar\\omega')),
      item('Phổ dao động và quay','Năng lượng gần đúng bằng tổng phần dao động và phần quay. Chuyển mức phát một photon có Δn = −1 và Δℓ = ±1 trong gần đúng lưỡng cực điều hòa.',math('E_{n\\ell}=E_n+E_\\ell')),
      item('Năng lượng và bước sóng photon','Năng lượng trạng thái đầu và cuối phải kể cả phần quay lẫn phần dao động. Chuyển mức phát xạ có năng lượng đầu cao hơn năng lượng cuối.',math('\\begin{aligned}&E_\\gamma=E_i-E_f,\\\\&\\lambda=hc/E_\\gamma.\\end{aligned}')),
    ]},
    {id:'crystals',title:'Tinh thể và dải năng lượng',items:[
      item('Mạng và nhóm nguyên tử cơ sở','Mạng mô tả tính tuần hoàn tịnh tiến. Đặt cùng một nhóm nguyên tử cơ sở tại mỗi điểm mạng tạo nên cấu trúc tinh thể.'),
      item('Các kiểu tinh thể','Các cấu trúc lập phương đơn giản, lập phương tâm khối và lập phương tâm mặt khác nhau ở vị trí các điểm mạng. Cấu trúc kim cương còn chứa nhóm nguyên tử cơ sở.'),
      item('Dải năng lượng','Tập rất nhiều mức gần nhau hình thành khi các trạng thái nguyên tử tương tác trong chất rắn.'),
      item('Vùng cấm','Khoảng năng lượng không có trạng thái electron khối trong mô hình dải lý tưởng. Eᶜ và Eᵛ là mép dưới dải dẫn và mép trên dải hóa trị.',math('E_g=E_c-E_v')),
      item('Dẫn điện theo cấu trúc dải','Dải điền một phần hoặc các dải chồng lấn cho phép electron đáp ứng điện trường bằng các trạng thái còn trống gần năng lượng đang có. Vùng cấm và mức điền quyết định tính cách điện hoặc bán dẫn.'),
      item('Chuỗi ion một chiều','Các điện tích ±e xen kẽ và cách đều a. C là thang Coulomb. U₊ là tương tác với một phía, còn Uₜ là tương tác của ion đánh dấu với cả hai phía. Năng lượng toàn chuỗi còn có hệ số chia đôi để tránh đếm lặp cặp.',math('\\begin{aligned}&C=e^2/(4\\pi\\varepsilon_0),\\\\&U_+=-C\\ln2/a,\\\\&U_t=2U_+.\\end{aligned}')),
    ]},
    {id:'free-electrons',title:'Mô hình electron tự do',items:[
      item('Giả thiết electron tự do','Electron phi tương đối tính trong thể tích V, thế bên trong gần như không đổi, rào bề mặt giam electron. Sự điền trạng thái tuân nguyên lý Pauli.'),
      item('Năng lượng hộp lập phương','K là tổng bình phương ba số lượng tử nguyên dương. Đặt E₀ = h²/(8mL²).',math('\\begin{aligned}&K=n_x^2+n_y^2+n_z^2\\\\&E=KE_0\\end{aligned}')),
      item('Mật độ trạng thái','g(E)dE là số trạng thái một electron, kể cả hai spin, trong khoảng năng lượng từ E đến E+dE. Với electron tự do ba chiều, g(E) tỉ lệ V√E.',math('g(E)=C V\\sqrt E')),
      item('Hệ số của mật độ trạng thái','m là khối lượng electron. Công thức dùng năng lượng và thể tích trong hệ đơn vị nhất quán.',math('C=\\frac{(2m)^{3/2}}{2\\pi^2\\hbar^3}')),
      item('Phân bố Fermi–Dirac','f(E) là xác suất chiếm một trạng thái, T > 0. Eᶠ là thế hóa học, thường gọi mức Fermi trong mô tả này.',math('f(E)=\\frac1{e^{(E-E_F)/(kT)}+1}')),
      item('Số electron theo năng lượng','g(E) đếm trạng thái, f(E) là xác suất chiếm. Hai đại lượng có ý nghĩa khác nhau.',math('dN=g(E)f(E)\\,dE')),
      item('Năng lượng Fermi ở không độ tuyệt đối','n = N/V là mật độ electron tự do, gồm cả hai hướng spin. Mô hình phi tương đối tính.',math('E_{F0}=\\frac{\\hbar^2}{2m}(3\\pi^2 n)^{2/3}')),
      item('Tốc độ Fermi','Động năng tại mặt Fermi bằng Eᶠ₀ trong mô hình electron tự do.',math('v_F=\\sqrt{\\frac{2E_{F0}}m}')),
      item('Động năng trung bình ở không độ tuyệt đối','Khí electron tự do ba chiều điền đầy trạng thái từ đáy dải đến Eᶠ₀.',math('\\overline E=\\frac35E_{F0}')),
      item('Đếm electron ở không độ tuyệt đối','g(E) kể cả hai trạng thái spin và được tính cho toàn thể tích. Các trạng thái dưới Eᶠ₀ được điền đầy.',math('N=\\int_0^{E_{F0}}g(E)\\,dE')),
      item('Nhiệt dung mol của electron dẫn','Gần đúng nhiệt độ thấp so với nhiệt độ Fermi, với một electron dẫn trên mỗi nguyên tử. R là hằng số khí mol.',math('C_{V,e}=\\frac{\\pi^2 kT}{2E_{F0}}R')),
    ]},
    {id:'semiconductors',title:'Bán dẫn và pha tạp',items:[
      item('Electron và lỗ trống','Lỗ trống là trạng thái thiếu electron trong dải hóa trị gần đầy, có thể mô tả như hạt tải mang điện dương. Nó không phải một proton chuyển động trong mạng.'),
      item('Bán dẫn thuần','Kích thích nhiệt hoặc ánh sáng tạo electron dải dẫn và lỗ trống dải hóa trị. Trong mô hình cân bằng không pha tạp, hai mật độ bằng nhau.'),
      item('Pha tạp loại n','Tạp chất cho cung cấp electron dẫn. Các ion cho đã ion hóa mang điện dương và gần như cố định trong mạng.'),
      item('Pha tạp loại p','Tạp chất nhận nhận electron và tạo lỗ trống. Các ion nhận đã ion hóa mang điện âm và gần như cố định trong mạng.'),
      item('Xác suất tại đáy dải dẫn','Với mức Fermi ở giữa vùng cấm và T > 0, độ chênh năng lượng từ mức Fermi tới đáy dải dẫn bằng Eᵍ/2.',math('f(E_c)=\\frac1{e^{E_g/(2kT)}+1}')),
    ]},
    {id:'junction',title:'Tiếp giáp và thiết bị bán dẫn',items:[
      item('Vùng nghèo của tiếp giáp p–n','Khuếch tán và tái hợp làm giảm hạt tải di động gần tiếp giáp, để lại ion pha tạp. Trường nội và rào thế hình thành từ điện tích không gian.'),
      item('Phân cực thuận và nghịch','Phía p dương hơn phía n là phân cực thuận, làm giảm rào thế. Phân cực nghịch làm tăng rào trong mô hình tiếp giáp.'),
      item('Đặc tuyến diode lý tưởng','V dương theo chiều phân cực thuận, Iₛ là dòng bão hòa ngược và T > 0. Bỏ qua đánh thủng và các hiệu chỉnh cấu trúc thực.',math('I=I_s(e^{eV/(kT)}-1)')),
      item('Diode phát quang và quang điện','Tái hợp electron–lỗ trống có thể phát photon. Hấp thụ photon có thể tạo cặp electron–lỗ trống. Hiệu suất còn phụ thuộc cấu trúc vật liệu.'),
      item('Transistor','Điện áp hoặc dòng điều khiển làm biến đổi dòng trong cấu trúc bán dẫn. Hoạt động cụ thể phụ thuộc transistor tiếp giáp hay transistor hiệu ứng trường.'),
    ]},
    {id:'superconductivity',title:'Siêu dẫn',items:[
      item('Trạng thái siêu dẫn','Dưới nhiệt độ tới hạn và trong miền dòng, từ trường cho phép, vật liệu có điện trở một chiều bằng không và thể hiện đáp ứng từ đặc trưng của siêu dẫn.'),
      item('Cặp Cooper','Trong mô tả BCS thông thường, tương tác hiệu dụng qua dao động mạng có thể ghép hai electron thành cặp tương quan. Trạng thái tập thể có khe năng lượng kích thích.'),
    ]},
  ],
}

export const moleculesSlides=[
  slide('Liên kết cần một cân bằng năng lượng',[
    'Sự tạo ion có chi phí năng lượng, còn tương tác giữa ion trái dấu làm giảm năng lượng.',
    'Lực đẩy ở khoảng cách ngắn ngăn các hạt nhân tiến sát vô hạn và tạo khoảng cách cân bằng.',
    'Liên kết cộng hóa trị và các tương tác lưỡng cực có cơ chế phân bố electron khác nhau.',
  ],math('U(r)=\\frac{q_1q_2}{4\\pi\\varepsilon_0r}')),
  slide('Phổ quay cho biết mômen quán tính',[
    'Phân tử hai nguyên tử được xem như rotor cứng quanh khối tâm.',
    'Khối lượng rút gọn và độ dài liên kết quyết định mômen quán tính.',
    'Chuyển mức lưỡng cực quay có độ biến thiên số lượng tử bằng một đơn vị.',
  ],math('E_\\ell=\\frac{\\ell(\\ell+1)\\hbar^2}{2I}')),
  slide('Dao động có năng lượng điểm không',[
    'Gần khoảng cách cân bằng, thế năng có thể xấp xỉ bằng một parabol.',
    'Số lượng tử dao động bắt đầu từ không nhưng năng lượng thấp nhất khác không.',
    'Photon dao động–quay nhận hiệu năng lượng của cả hai dạng chuyển động.',
  ],math('E_n=(n+\\tfrac12)\\hbar\\omega')),
  slide('Mạng tinh thể và nhóm cơ sở có vai trò khác nhau',[
    'Mạng mô tả các phép tịnh tiến lặp lại cấu trúc.',
    'Nhóm cơ sở quy định những nguyên tử đặt ở mỗi điểm mạng.',
    'Liên kết ion, cộng hóa trị, phân tử và kim loại tạo các tính chất vật liệu khác nhau.',
  ]),
  slide('Trạng thái còn trống quyết định đáp ứng điện',[
    'Tương tác giữa các nguyên tử tạo thành các dải mức năng lượng rất gần nhau.',
    'Electron chỉ có thể chuyển sang một trạng thái được phép còn trống.',
    'Dải điền một phần và vùng cấm phân biệt chất dẫn, bán dẫn và cách điện.',
  ],math('E_g=E_c-E_v')),
  slide('Mật độ trạng thái đếm chỗ cho electron',[
    'Mỗi trạng thái không gian trong hộp chứa tối đa hai electron ngược spin.',
    'Trong mô hình ba chiều, số trạng thái trong một khoảng năng lượng được mô tả bởi g(E).',
    'Phải phân biệt số trạng thái với số electron thực sự chiếm các trạng thái ấy.',
  ],math('dN=g(E)f(E)\\,dE')),
  slide('Fermi–Dirac xác định xác suất chiếm',[
    'Ở nhiệt độ dương, xác suất chiếm giảm liên tục theo năng lượng.',
    'Tại mức Fermi, xác suất bằng một nửa.',
    'Ở nhiệt độ thấp, các trạng thái sâu dưới mức Fermi gần như đầy và các trạng thái cao hơn gần như trống.',
  ],math('f(E)=\\frac1{e^{(E-E_F)/(kT)}+1}')),
  slide('Không độ tuyệt đối vẫn còn động năng',[
    'Nguyên lý Pauli buộc electron điền nhiều trạng thái không gian khác nhau.',
    'Electron không cùng dồn vào trạng thái động năng thấp nhất.',
    'Trong khí electron tự do ba chiều, động năng trung bình bằng ba phần năm năng lượng Fermi.',
  ],math('\\overline E=\\frac35E_{F0}')),
  slide('Pha tạp thay đổi hạt tải chiếm ưu thế',[
    'Tạp chất cho tạo electron dẫn và ion cho dương.',
    'Tạp chất nhận tạo lỗ trống và ion nhận âm.',
    'Pha tạp không đồng nghĩa toàn mẫu có điện tích tổng cộng khác không.',
  ]),
  slide('Tiếp giáp tạo một rào thế nội',[
    'Khuếch tán và tái hợp để lại điện tích ion trong vùng nghèo.',
    'Phân cực thuận giảm rào, còn phân cực nghịch tăng rào.',
    'Đặc tuyến diode lý tưởng mô tả dòng trong miền chưa có đánh thủng.',
  ],math('I=I_s(e^{eV/(kT)}-1)')),
  slide('Electron–lỗ trống nối quang học với điện học',[
    'Tái hợp có thể tạo bức xạ trong diode phát quang.',
    'Hấp thụ photon có thể tạo hạt tải trong quang diode hoặc pin mặt trời.',
    'Transistor điều khiển dòng nhờ cấu trúc tiếp giáp hoặc điện trường cổng.',
  ]),
  slide('Siêu dẫn là một trạng thái tập thể',[
    'Trạng thái siêu dẫn tồn tại dưới những điều kiện tới hạn của nhiệt độ, từ trường và dòng điện.',
    'Mô hình BCS mô tả sự ghép cặp electron nhờ tương tác hiệu dụng liên quan đến mạng.',
    'Khe năng lượng và tính tập thể phân biệt siêu dẫn với việc chỉ giảm tán xạ thông thường.',
  ]),
]

export const moleculesTopics=[
  {title:'Liên kết, phổ và cấu trúc vật chất',topics:[
    {slug:'lien-ket-phan-tu',title:'Các loại liên kết phân tử',question:'Điều gì giữ các nguyên tử thành phân tử?',source:'42.1'},
    {slug:'pho-phan-tu',title:'Phổ quay và dao động phân tử',question:'Photon cho biết gì về chuyển động của các hạt nhân?',source:'42.2'},
    {slug:'cau-truc-chat-ran',title:'Cấu trúc và liên kết trong chất rắn',question:'Mạng và nhóm cơ sở tạo cấu trúc tinh thể như thế nào?',source:'42.3'},
    {slug:'dai-nang-luong',title:'Dải năng lượng trong chất rắn',question:'Vì sao cùng có electron mà các vật liệu dẫn điện khác nhau?',source:'42.4'},
  ]},
  {title:'Electron, bán dẫn và siêu dẫn',topics:[
    {slug:'mo-hinh-electron-tu-do',title:'Mô hình electron tự do',question:'Pauli quyết định sự điền trạng thái trong kim loại ra sao?',source:'42.5'},
    {slug:'chat-ban-dan',title:'Bán dẫn thuần và pha tạp',question:'Electron và lỗ trống hình thành bằng những cơ chế nào?',source:'42.6'},
    {slug:'thiet-bi-ban-dan',title:'Tiếp giáp và thiết bị bán dẫn',question:'Rào thế nội tạo đặc tuyến và khả năng điều khiển dòng như thế nào?',source:'42.7'},
    {slug:'sieu-dan',title:'Trạng thái siêu dẫn',question:'Vì sao trạng thái ghép cặp có thể dẫn tới điện trở bằng không?',source:'42.8'},
  ]},
]
