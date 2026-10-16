const math=tex=>'$$\n'+tex+'\n$$'
const note='24-hat-co-ban-vu-tru'
const slide=(title,bullets,formula='')=>({title,bullets,formula,note})
const item=(name,description,formula='')=>({name,description,formula,variables:[]})
export const particlesCosmologyTopics=[
 {title:'Hạt, tương tác và các mô hình cấu trúc',topics:[
  {slug:'lich-su-hat-co-ban',title:'Các hạt cơ bản và quá trình khám phá',question:'Hạt mới và phản hạt đã thay đổi bức tranh về vật chất ra sao?',source:'44.1'},
  {slug:'may-gia-toc-va-detector',title:'Máy gia tốc và thiết bị ghi nhận hạt',question:'Năng lượng chùm tới trở thành năng lượng tạo hạt như thế nào?',source:'44.2'},
  {slug:'hat-va-tuong-tac',title:'Phân loại hạt và các tương tác',question:'Những đại lượng bảo toàn cho phép hoặc loại trừ một phản ứng ra sao?',source:'44.3'},
  {slug:'quark-va-gluon',title:'Quark, gluon và cấu trúc hadron',question:'Điện tích, số baryon và độ lạ xác định thành phần quark như thế nào?',source:'44.4'},
  {slug:'mo-hinh-chuan',title:'Mô hình chuẩn và các giới hạn',question:'Sự thống nhất điện yếu và trường Higgs giải thích những điều gì?',source:'44.5'},
 ]},
 {title:'Sự giãn nở và lịch sử vũ trụ',topics:[
  {slug:'vu-tru-gian-no',title:'Vũ trụ giãn nở',question:'Dịch chuyển đỏ và phép đo khoảng cách cho biết gì về sự giãn nở?',source:'44.6'},
  {slug:'khoi-dau-thoi-gian',title:'Vũ trụ sơ khai và khởi đầu thời gian',question:'Vật lý hạt nối với bức xạ nền và sự hình thành nguyên tố ra sao?',source:'44.7'},
 ]},
]
export const particlesCosmologySlides=[
 slide('Phản hạt mở rộng khái niệm về vật chất',[
  'Hạt và phản hạt tương ứng có cùng khối lượng, còn những điện tích thích hợp có dấu đối nhau.',
  'Tạo cặp và hủy cặp phải đồng thời bảo toàn năng lượng và động lượng.',
  'Một photon tự do không thể một mình tạo một cặp hạt tự do trong chân không.',
 ],math('E_{\\rm rest}=2m_ec^2')),
 slide('Hạt ảo thuộc mô tả tương tác',[
  'Hạt ảo là thành phần trung gian trong phép mô tả lượng tử, không phải một hạt tự do được quan sát riêng.',
  'Bảo toàn năng lượng và động lượng vẫn được áp dụng.',
  'Thế Yukawa có thang tầm tác dụng liên hệ với khối lượng hạt truyền tương tác trong mô hình hiệu dụng.',
 ],math('r_0\\sim\\frac{\\hbar}{mc}')),
 slide('Cyclotron dùng chuyển động tròn trong từ trường',[
  'Trong gần đúng phi tương đối tính, độ lớn điện tích và từ trường quyết định tần số quay.',
  'Dấu điện tích quyết định chiều quay. Bán kính tăng khi động lượng tăng.',
  'Khi hiệu ứng tương đối tính đáng kể, không thể giữ nguyên công thức tần số không phụ thuộc năng lượng.',
 ],math('f=\\frac{|q|B}{2\\pi m}')),
 slide('Năng lượng khối tâm quyết định khả năng tạo hạt',[
  'Một phần năng lượng trong thí nghiệm bia cố định gắn với chuyển động chung của hệ.',
  'Hai chùm có động lượng bằng nhau và ngược hướng đưa hệ phòng thí nghiệm về hệ khối tâm.',
  'Tại ngưỡng tạo các hạt có khối lượng, sản phẩm không còn động năng tương đối trong hệ khối tâm.',
 ],math('E_{\\rm cm}^2=E_{\\rm tot}^2-p_{\\rm tot}^2c^2')),
 slide('Các quy tắc chọn lọc phải được xét đồng thời',[
  'Điện tích và năng lượng đủ chưa bảo đảm phản ứng xảy ra.',
  'Số baryon và số lepton được dùng cùng những điều kiện của mô hình phản ứng đang xét.',
  'Độ lạ được bảo toàn trong tương tác mạnh và điện từ nhưng có thể thay đổi trong tương tác yếu.',
 ]),
 slide('Quark giải thích điện tích của hadron',[
  'Trong mô hình thành phần hóa trị thông thường, baryon gồm ba quark và meson gồm quark với phản quark.',
  'Điện tích, số baryon và các số lượng tử mùi được cộng đại số.',
  'Proton có thành phần uud, còn neutron có thành phần udd.',
 ]),
 slide('Gluon và màu mô tả tương tác mạnh',[
  'Màu là tên một điện tích lượng tử, khác màu sắc quang học.',
  'Gluon truyền tương tác và có thể làm thay đổi trạng thái màu của quark.',
  'Hadron quan sát được có cấu trúc trạng thái trung hòa màu phù hợp mô hình.',
 ]),
 slide('Mô hình chuẩn có phạm vi và giới hạn',[
  'Quark, lepton và các hạt truyền tương tác tổ chức các phản ứng trong mô hình chuẩn.',
  'Thống nhất điện yếu nối tương tác điện từ với tương tác yếu, còn trường Higgs có vai trò trong cơ chế tạo khối lượng.',
  'Hấp dẫn lượng tử, vật chất tối và nhiều câu hỏi về vũ trụ vẫn cần những mô tả bổ sung.',
 ]),
 slide('Dịch chuyển đỏ là một tỉ số bước sóng',[
  'So sánh cùng một vạch phổ ở nguồn và ở phép đo để xác định độ dịch chuyển đỏ.',
  'Công thức Doppler tương đối tính thuộc mô hình chuyển động tương đối thích hợp.',
  'Dịch chuyển đỏ vũ trụ còn gắn trực tiếp với sự thay đổi hệ số tỉ lệ trong khi photon truyền đi.',
 ],math('1+z=\\frac{\\lambda_o}{\\lambda_e}')),
 slide('Định luật Hubble nối vận tốc lùi với khoảng cách',[
  'Quan hệ Hubble tại một thời điểm cần nêu loại khoảng cách và miền mô hình.',
  'Nghịch đảo Hubble cho một thang thời gian, không tự cho tuổi chính xác của mọi mô hình vũ trụ.',
  'Mật độ tới hạn và các tham số thành phần giúp mô tả động lực giãn nở.',
 ],math('v=H_0r')),
 slide('Vũ trụ sơ khai nguội đi khi giãn nở',[
  'Những thời kỳ tương tác và tạo hạt được phân biệt bằng các thang nhiệt độ, năng lượng và thời gian.',
  'Tổng hợp hạt nhân sơ khai tạo các nguyên tố nhẹ, khác với sự hình thành nguyên tử trung hòa muộn hơn.',
  'Khi mật độ electron tự do giảm, photon có thể truyền xa và lưu lại thông tin về lần tán xạ cuối.',
 ]),
 slide('Bức xạ nền nối nhiệt độ với sự giãn nở',[
  'Bức xạ nền có phổ gần vật đen và bước sóng tăng theo hệ số tỉ lệ của vũ trụ.',
  'Trong mô hình giãn nở đoạn nhiệt đang xét, nhiệt độ bức xạ giảm theo nghịch đảo hệ số tỉ lệ.',
  'Các giả thuyết về lạm phát và bất đối xứng vật chất cần được phân biệt với các dữ kiện quan sát.',
 ],math('T\\propto a^{-1}')),
]
export const particlesCosmologyCheatsheet={
 title:'Cheatsheet: Vật lý hạt và vũ trụ học',
 description:'Định nghĩa, tính chất, điều kiện và công thức về hạt, tương tác, động học tương đối tính và giãn nở vũ trụ.',
 sections:[
  {id:'particles',title:'Hạt và phản hạt',items:[
   item('Phản hạt','Hạt tương ứng có cùng khối lượng và spin, còn các điện tích cộng tính thích hợp trái dấu. Một số hạt trung hòa là phản hạt của chính mình.'),
   item('Ngân sách tạo cặp electron–positron','Năng lượng nghỉ của cặp, chưa thay thế điều kiện động lượng hoặc hiệu chỉnh giật lùi của môi trường.',math('E_{\\rm rest}=2m_ec^2')),
   item('Hủy cặp gần trạng thái nghỉ','Electron và positron có tổng động lượng bằng không, hủy thành hai photon. Hai photon có năng lượng bằng nhau và động lượng ngược chiều.',math('E_\\gamma=m_ec^2')),
   item('Hạt ảo','Thành phần trung gian trong mô tả tương tác lượng tử, không cần thỏa hệ thức năng lượng–động lượng của một hạt tự do thực. Không tạo ngoại lệ cho bảo toàn năng lượng và động lượng.'),
   item('Thế Yukawa','f² là thang cường độ, r₀ là tham số tầm tác dụng. Mô hình lực hạt nhân hiệu dụng.',math('U(r)=-f^2\\frac{e^{-r/r_0}}r')),
   item('Thang tầm tác dụng','Quan hệ bậc độ lớn giữa tham số Yukawa và khối lượng hạt truyền tương tác, không phải thời gian sống đo được của một hạt ảo.',math('r_0\\sim\\frac{\\hbar}{mc}')),
  ]},
  {id:'accelerators',title:'Máy gia tốc và năng lượng khả dụng',items:[
   item('Bán kính quỹ đạo từ','Chuyển động vuông góc từ trường đều. p là độ lớn động lượng tương đối tính, q khác không.',math('r=\\frac{p}{|q|B}')),
   item('Tần số cyclotron','Gần đúng phi tương đối tính, trường đều và chuyển động vuông góc trường.',math('f=\\frac{|q|B}{2\\pi m}')),
   item('Động năng cực đại cyclotron','R là bán kính quỹ đạo lớn nhất, bỏ qua hiệu chỉnh tương đối tính và tổn hao.',math('K_{\\max}=\\frac{q^2B^2R^2}{2m}')),
   item('Năng lượng khối tâm','Etot và ptot là năng lượng cùng động lượng toàn hệ trong cùng một hệ quy chiếu.',math('E_{\\rm cm}^2=E_{\\rm tot}^2-p_{\\rm tot}^2c^2')),
   item('Va chạm bia cố định','Hạt tới và bia có cùng khối lượng m. Đặt ε = mc², E là năng lượng toàn phần hạt tới. Bia ban đầu đứng yên.',math('E_{\\rm cm}^2=2\\epsilon(E+\\epsilon)')),
   item('Va chạm hai chùm cân bằng','Hai chùm có cùng năng lượng toàn phần E và động lượng bằng nhau, ngược hướng.',math('E_{\\rm cm}=2E')),
   item('Ngưỡng tạo sản phẩm có khối lượng','Trong hệ khối tâm tại ngưỡng động học, sản phẩm không có động năng tương đối. Các điều kiện bảo toàn khác vẫn phải thỏa.'),
  ]},
  {id:'classification',title:'Phân loại và số lượng tử',items:[
   item('Fermion và boson','Fermion có spin bán nguyên, boson có spin nguyên. Phân loại này khác với việc phân biệt hạt cơ bản và hạt cấu tạo.'),
   item('Lepton và hadron','Lepton không chịu tương tác mạnh. Hadron chịu tương tác mạnh và có cấu trúc quark, gồm các baryon và meson thông thường.'),
   item('Số baryon','Quark có B = 1/3, phản quark có B = −1/3. Baryon thông thường có B = 1, phản baryon có B = −1, meson có B = 0.'),
   item('Số lepton','Lepton và phản lepton mang dấu đối nhau. Các phép xét từng họ cần nêu phạm vi mô hình, đặc biệt khi có sự trộn và dao động neutrino.'),
   item('Độ lạ','Quark s có S = −1, phản quark s có S = 1. Độ lạ được bảo toàn trong tương tác mạnh và điện từ, còn có thể thay đổi trong tương tác yếu.'),
   item('Cộng số lượng tử','Điện tích, số baryon và các số lượng tử mùi là tổng đại số của các thành phần. Phải dùng đúng dấu cho phản hạt.'),
  ]},
  {id:'standard-model',title:'Quark, gluon và mô hình chuẩn',items:[
   item('Sáu mùi quark','u, c, t có điện tích +2e/3. d, s, b có điện tích −e/3. Mỗi quark có spin một phần hai.'),
   item('Baryon và meson hóa trị','Trong mô hình thông thường đang xét, baryon gồm ba quark, phản baryon gồm ba phản quark, meson gồm quark và phản quark.'),
   item('Màu và gluon','Màu là điện tích của tương tác mạnh. Gluon truyền tương tác và mang cấu trúc màu, khác với màu quang học.'),
   item('Tương tác điện yếu','Mô tả thống nhất tương tác điện từ và tương tác yếu. Photon, W⁺, W⁻ và Z⁰ là các hạt truyền tương tác tương ứng.'),
   item('Cơ chế Higgs','Giá trị nền của trường Higgs có vai trò trong cơ chế khối lượng của các hạt cơ bản. Không đồng nhất khối lượng mọi vật với tổng khối lượng nghỉ các quark hóa trị.'),
   item('Các giới hạn của mô hình chuẩn','Mô hình chuẩn của hạt khác với mô hình vũ trụ học. Một mô tả đầy đủ của hấp dẫn lượng tử, vật chất tối và bất đối xứng vật chất vẫn cần các thành phần hoặc lý thuyết bổ sung.'),
  ]},
  {id:'redshift',title:'Dịch chuyển đỏ và định luật Hubble',items:[
   item('Độ dịch chuyển đỏ','λo là bước sóng quan sát, λe là bước sóng phát của cùng vạch phổ.',math('1+z=\\frac{\\lambda_o}{\\lambda_e}')),
   item('Doppler dọc đường ngắm','Nguồn và người quan sát có chuyển động tương đối trong mô hình Doppler đặc biệt. β = v/c dương khi lùi xa.',math('1+z=\\sqrt{\\frac{1+\\beta}{1-\\beta}}')),
   item('Suy tốc độ Doppler','Đặt s = 1 + z. Quan hệ thuộc mô hình Doppler trên, không phải một công thức vận tốc toàn cục cho mọi dịch chuyển đỏ vũ trụ.',math('\\beta=\\frac{s^2-1}{s^2+1}')),
   item('Định luật Hubble','Tại thời điểm hiện tại của mô hình giãn nở đồng nhất, v tỉ lệ với khoảng cách riêng r phù hợp. H₀ là tham số Hubble tại thời điểm ấy.',math('v=H_0r')),
   item('Thang thời gian Hubble','Nghịch đảo tham số Hubble là một thang thời gian. Đồng nhất với tuổi vũ trụ chỉ thuộc mô hình giãn nở tuyến tính thích hợp.',math('t_H=H_0^{-1}')),
   item('Tham số Hubble theo thời gian','a là hệ số tỉ lệ. Dấu chấm là đạo hàm theo thời gian vũ trụ.',math('H=\\frac{\\dot a}a')),
  ]},
  {id:'cosmology',title:'Mật độ, bức xạ và lịch sử vũ trụ',items:[
   item('Mật độ tới hạn','H là tham số Hubble, G là hằng số hấp dẫn. Phải xét trong mô hình vũ trụ học với các thành phần và giả thiết hình học thích hợp.',math('\\rho_c=\\frac{3H^2}{8\\pi G}')),
   item('Vật chất tối và năng lượng tối','Vật chất tối góp vào hấp dẫn và sự hình thành cấu trúc. Năng lượng tối mô tả thành phần gắn với động lực giãn nở gia tốc trong mô hình. Hai khái niệm không đồng nhất.'),
   item('Dịch chuyển đỏ vũ trụ','ao và ae là hệ số tỉ lệ ở lúc quan sát và phát. Photon truyền cùng mô hình giãn nở.',math('1+z=\\frac{a_o}{a_e}')),
   item('Năng lượng photon quan sát','Ee là năng lượng lúc phát, Eo là năng lượng lúc quan sát. Cùng mô hình dịch chuyển đỏ.',math('E_o=\\frac{E_e}{1+z}')),
   item('Nhiệt độ bức xạ','Bức xạ vật đen giãn nở đoạn nhiệt trong mô hình đang xét. Hệ số tỉ lệ a không có thứ nguyên theo quy ước chuẩn hóa.',math('Ta=\\mathrm{const}')),
   item('Năng lượng nhiệt cổ điển','Động năng tịnh tiến trung bình của một hạt khí lý tưởng cổ điển ba chiều, phi tương đối tính. Không áp dụng nguyên dạng cho mọi photon hay hạt tương đối tính.',math('\\overline K=\\frac32kT')),
   item('Độ dài Planck','Kết hợp tốc độ ánh sáng, hấp dẫn và hằng số Planck rút gọn thành một thang độ dài, không tự xác định lịch sử trước thời Planck.',math('\\ell_P=\\sqrt{\\frac{\\hbar G}{c^3}}')),
   item('Thời gian Planck','Thời gian ánh sáng truyền một độ dài Planck.',math('t_P=\\ell_P/c')),
   item('Tổng hợp hạt nhân sơ khai','Sự hình thành các hạt nhân nhẹ trong vũ trụ sớm, khác với quá trình electron kết hợp với hạt nhân tạo nguyên tử trung hòa muộn hơn.'),
   item('Bức xạ nền vi sóng vũ trụ','Bức xạ gần phổ vật đen lưu thông tin về lần tán xạ cuối khi vũ trụ chuyển sang trong suốt với photon trong mô hình tái kết hợp.'),
   item('Lạm phát vũ trụ','Giai đoạn giãn nở gia tốc rất sớm trong một họ mô hình nhằm giải thích các đặc điểm quan sát được. Chi tiết cơ chế không được đồng nhất với dữ kiện đã được xác nhận trực tiếp.'),
  ]},
 ],
}
