const math=tex=>'$$\n'+tex+'\n$$'
const note='23-vat-ly-hat-nhan'
const slide=(title,bullets,formula='')=>({title,bullets,formula,note})
const item=(name,description,formula='')=>({name,description,formula,variables:[]})

export const nuclearTopics=[
 {title:'Cấu trúc, liên kết và sự phân rã',topics:[
  {slug:'tinh-chat-hat-nhan',title:'Các tính chất của hạt nhân',question:'Kích thước, khối lượng và mômen từ mô tả hạt nhân như thế nào?',source:'43.1'},
  {slug:'nang-luong-lien-ket',title:'Năng lượng liên kết và cấu trúc hạt nhân',question:'Độ hụt khối cho biết gì về năng lượng và độ bền liên kết?',source:'43.2'},
  {slug:'on-dinh-va-phong-xa',title:'Độ bền và các dạng phóng xạ',question:'Hạt nhân đổi thành phần và năng lượng qua những kênh nào?',source:'43.3'},
  {slug:'hoat-do-va-chu-ky-ban-ra',title:'Hoạt độ và chu kỳ bán rã',question:'Làm thế nào suy số hạt nhân và tuổi mẫu từ hoạt độ?',source:'43.4'},
 ]},
 {title:'Bức xạ và các phản ứng hạt nhân',topics:[
  {slug:'tac-dung-sinh-hoc',title:'Tác dụng sinh học và ứng dụng của bức xạ',question:'Vì sao hoạt độ, liều hấp thụ và liều tương đương là các đại lượng khác nhau?',source:'43.5'},
  {slug:'phan-ung-hat-nhan',title:'Năng lượng và ngưỡng phản ứng hạt nhân',question:'Vì sao năng lượng phản ứng chưa đủ xác định ngưỡng trong phòng thí nghiệm?',source:'43.6'},
  {slug:'phan-hach',title:'Phân hạch và phản ứng dây chuyền',question:'Các neutron nối nhiều phản ứng phân hạch với nhau ra sao?',source:'43.7'},
  {slug:'nhiet-hach',title:'Nhiệt hạch và năng lượng của các sao',question:'Hai hạt nhân mang điện dương đến gần nhau và giải phóng năng lượng bằng cách nào?',source:'43.8'},
 ]},
]

export const nuclearSlides=[
 slide('Hạt nhân có mật độ gần như không đổi',[
  'Hạt nhân gồm Z proton và N neutron, với số khối A = Z + N.',
  'Mô hình bán kính tỉ lệ căn bậc ba số khối dẫn đến thể tích gần tỉ lệ với số nucleon.',
  'Đồng vị có cùng Z nhưng khác N. Khối lượng nguyên tử trung hòa còn gồm electron.',
 ],math('R=R_0A^{1/3}')),
 slide('Mômen từ nối spin với cộng hưởng',[
  'Thành phần mômen từ theo từ trường nhận các giá trị lượng tử hóa.',
  'Hai hướng spin của proton có năng lượng khác nhau trong từ trường ngoài.',
  'Photon cộng hưởng trao đổi đúng hiệu năng lượng giữa các mức.',
 ],math('U=-\\boldsymbol\\mu\\cdot\\mathbf B')),
 slide('Năng lượng liên kết là phần giảm của năng lượng nghỉ',[
  'Tách hoàn toàn hạt nhân liên kết thành các nucleon tự do cần cung cấp năng lượng.',
  'Khi dùng khối lượng nguyên tử trung hòa, phải cân bằng số electron ở hai vế.',
  'Năng lượng liên kết trung bình không đồng nhất với năng lượng tách một nucleon cụ thể.',
 ],math('E_B=\\Delta M c^2')),
 slide('Các mô hình nhấn mạnh những tính chất khác nhau',[
  'Mô hình giọt chất lỏng kể tương tác ngắn hạn, bề mặt, lực đẩy điện và sự ghép đôi.',
  'Mô hình vỏ mô tả sự điền các trạng thái nucleon trong thế hiệu dụng.',
  'Năng lượng liên kết lớn trên mỗi nucleon không bảo đảm mọi kênh biến đổi đều bị cấm.',
 ]),
 slide('Các kênh phân rã có dấu hiệu bảo toàn riêng',[
  'Phát alpha làm giảm số khối bốn đơn vị và số proton hai đơn vị.',
  'Beta trừ, beta cộng và bắt electron đổi một neutron hoặc proton trong hạt nhân.',
  'Phát gamma thuần túy hạ mức năng lượng mà không đổi số proton và neutron.',
 ]),
 slide('Khối lượng nguyên tử quyết định ngưỡng beta',[
  'Beta trừ có năng lượng khả dụng từ chênh lệch khối lượng nguyên tử mẹ và con.',
  'Đặt ΔM là khối lượng nguyên tử mẹ trừ khối lượng nguyên tử con. Beta cộng còn cần ngân sách năng lượng nghỉ của hai electron.',
  'Bắt electron có thể xảy ra khi beta cộng bị cấm về năng lượng.',
 ],math('Q_+=(\\Delta M-2m_e)c^2')),
 slide('Hoạt độ là số phân rã trong một đơn vị thời gian',[
  'Với một đồng vị, hằng số phân rã không đổi và không có nguồn bổ sung, số hạt nhân giảm theo hàm mũ.',
  'Hoạt độ bằng hằng số phân rã nhân số hạt nhân còn lại.',
  'Becquerel đo số phân rã mỗi giây, không đo năng lượng hấp thụ trong mô.',
 ],math('\\mathcal A=\\lambda N')),
 slide('Chu kỳ bán rã và tuổi mẫu có vai trò khác nhau',[
  'Chu kỳ bán rã mô tả thời gian giảm một nửa trong cùng mô hình suy giảm.',
  'Thời gian sống trung bình là nghịch đảo hằng số phân rã.',
  'Định tuổi cần hoạt độ ban đầu phù hợp và giả thiết về trao đổi đồng vị của mẫu.',
 ],math('t=\\lambda^{-1}\\ln(\\mathcal A_0/\\mathcal A)')),
 slide('Năng lượng và loại bức xạ cùng ảnh hưởng tác dụng sinh học',[
  'Liều hấp thụ là năng lượng truyền cho vật chất trên mỗi đơn vị khối lượng.',
  'Liều tương đương còn kể hệ số hiệu quả sinh học trong mô hình đang dùng.',
  'Khả năng xuyên sâu, đường phơi nhiễm và mô nhận bức xạ là những yếu tố cần phân biệt.',
 ],math('D=E_{\\rm abs}/m')),
 slide('Ngưỡng phản ứng phải kể động lượng',[
  'Q dương biểu thị phần giảm của tổng năng lượng nghỉ, còn Q âm cần năng lượng cung cấp.',
  'Với bia đứng yên, một phần động năng thuộc chuyển động chung của khối tâm.',
  'Hạt mang điện còn gặp hàng rào Coulomb. Xuyên ngầm phân biệt hàng rào cổ điển với một cấm đoán tuyệt đối.',
 ],math('K_{\\rm cm}=\\frac{M}{M+m}K')),
 slide('Phân hạch có thể tạo phản ứng dây chuyền',[
  'Các neutron sinh ra có thể kích thích những phân hạch tiếp theo.',
  'Chất làm chậm và thanh điều khiển thực hiện các nhiệm vụ khác nhau.',
  'Sản phẩm phân hạch tiếp tục phân rã sau khi dừng dây chuyền, nên vẫn sinh nhiệt.',
 ],math('P=\\dot N_f E_f')),
 slide('Nhiệt hạch phụ thuộc năng lượng liên kết và hàng rào',[
  'Ghép những hạt nhân đủ nhẹ có thể làm giảm tổng khối lượng nghỉ và giải phóng năng lượng.',
  'Trong các sao, phân bố động năng và xuyên ngầm cùng tham gia quyết định xác suất phản ứng.',
  'Chuỗi proton–proton tạo heli. Ghép hai hạt nhân bất kỳ không luôn là phản ứng tỏa năng lượng.',
 ]),
]

export const nuclearCheatsheet={
 title:'Cheatsheet: Vật lý hạt nhân',
 description:'Định nghĩa, tính chất, điều kiện và công thức về hạt nhân, phóng xạ và phản ứng hạt nhân.',
 sections:[
  {id:'nuclear-properties',title:'Thành phần, kích thước và mômen từ',items:[
   item('Nuclide và đồng vị','Nuclide xác định bởi Z và N. Z là số proton, N là số neutron. Các đồng vị có cùng Z nhưng khác N.',math('A=Z+N')),
   item('Bán kính hạt nhân','Mô hình cầu gần đúng cho phần lớn hạt nhân. A là số nucleon, R₀ xấp xỉ 1,2 fm.',math('R=R_0A^{1/3}')),
   item('Mật độ hạt nhân','Dùng m xấp xỉ A mᵤ và V = 4πR³/3 trong mô hình bán kính trên. Mật độ gần như không phụ thuộc A.',math('\\rho\\approx\\frac{3m_u}{4\\pi R_0^3}')),
   item('Đơn vị khối lượng nguyên tử','Một phần mười hai khối lượng nguyên tử carbon-12 trung hòa, ở trạng thái cơ bản và đứng yên.',math('1\\,\\mathrm u\\approx931{,}5\\,\\mathrm{MeV}/c^2')),
   item('Magneton hạt nhân','e là độ lớn điện tích electron, mₚ là khối lượng proton.',math('\\mu_n=\\frac{e\\hbar}{2m_p}')),
   item('Năng lượng trong từ trường','μ là mômen từ hạt nhân và B là từ trường ngoài.',math('U=-\\boldsymbol\\mu\\cdot\\mathbf B')),
   item('Photon cộng hưởng','Trạng thái đầu và cuối có độ chênh năng lượng ΔE. Với hai hướng mômen có thành phần ±μz, độ chênh bằng 2|μz|B.',math('hf=|\\Delta E|')),
  ]},
  {id:'binding',title:'Độ hụt khối và liên kết',items:[
   item('Khối lượng các thành phần tự do','Mᴴ là khối lượng nguyên tử hydro trung hòa, mₙ là khối lượng neutron. F cân bằng số electron với nguyên tử trung hòa có Z proton.',math('F=ZM_H+Nm_n')),
   item('Độ hụt khối','M là khối lượng nguyên tử trung hòa tương ứng. Bỏ qua hiệu chỉnh chênh lệch năng lượng liên kết electron ở độ chính xác đang xét.',math('\\Delta M=F-M')),
   item('Năng lượng liên kết','Năng lượng cần để tách hoàn toàn các nucleon về trạng thái tự do đứng yên.',math('E_B=\\Delta Mc^2')),
   item('Năng lượng liên kết trung bình','Trung bình trên tất cả A nucleon, khác năng lượng tách một nucleon riêng lẻ.',math('\\overline E_B=E_B/A')),
   item('Mô hình giọt chất lỏng','Tổng năm đóng góp thể tích, bề mặt, Coulomb, bất đối xứng và ghép đôi. G₁ gom hai đóng góp đầu, G₂ gom ba đóng góp còn lại. Các đóng góp đều đã mang dấu tương ứng.',math('\\begin{aligned}&G_1=E_V+E_S\\\\&G_2=E_C+E_A+E_P\\\\&E_B=G_1+G_2\\end{aligned}')),
   item('Thể tích và bề mặt','Các hệ số có đơn vị MeV. C₁ = 15,75 và C₂ = 17,80 trong bộ tham số đang dùng.',math('\\begin{aligned}&E_V=C_1A\\\\&E_S=-C_2A^{2/3}\\end{aligned}')),
   item('Coulomb và bất đối xứng','C₃ = 0,7100 MeV và C₄ = 23,69 MeV. Các số hạng làm giảm năng lượng liên kết.',math('\\begin{aligned}&E_C=-C_3\\frac{Z(Z-1)}{A^{1/3}}\\\\&E_A=-C_4\\frac{(A-2Z)^2}{A}\\end{aligned}')),
   item('Ghép đôi','C₅ = 39 MeV. Dấu cộng cho Z và N chẵn, dấu trừ cho cả hai lẻ. Với A lẻ, đóng góp bằng không.',math('E_P=\\pm C_5A^{-4/3}')),
   item('Mô hình vỏ','Các nucleon điền các trạng thái lượng tử của thế hiệu dụng. Những số proton hoặc neutron ứng với vỏ kín có tính bền liên kết đặc biệt.'),
  ]},
  {id:'decay-channels',title:'Các kênh phân rã',items:[
   item('Phân rã alpha','Hạt phát ra là hạt nhân heli-4. Z giảm 2, N giảm 2 và A giảm 4.'),
   item('Phân rã beta trừ','Một neutron chuyển thành proton, phát electron và phản neutrino electron. Z tăng 1, N giảm 1, A giữ nguyên.',math('n\\to p+e^-+\\bar\\nu_e')),
   item('Phân rã beta cộng','Một proton trong hạt nhân chuyển thành neutron, phát positron và neutrino electron. Z giảm 1 và A giữ nguyên.',math('p\\to n+e^++\\nu_e')),
   item('Bắt electron','Hạt nhân bắt một electron nguyên tử. Một proton chuyển thành neutron và phát neutrino electron.',math('p+e^-\\to n+\\nu_e')),
   item('Phân rã gamma','Hạ mức năng lượng của hạt nhân bằng phát photon. Trong chuyển mức gamma thuần túy, Z và N không đổi.'),
   item('Năng lượng phân rã theo khối lượng nguyên tử','$M_i$ và $M_f$ là khối lượng nguyên tử trung hòa mẹ và con. Q₋, Q₊ và QEC lần lượt ứng với beta trừ, beta cộng và bắt electron, trước các hiệu chỉnh liên kết electron thích hợp.',math('\\begin{aligned}&Q_-=(M_i-M_f)c^2\\\\&Q_+=(M_i-M_f-2m_e)c^2\\\\&Q_{\\rm EC}\\approx(M_i-M_f)c^2\\end{aligned}')),
   item('Điều kiện năng lượng','Một kênh phân rã tự phát cần đủ năng lượng nghỉ khả dụng cho các sản phẩm. Điều kiện năng lượng không thay thế các định luật bảo toàn khác.'),
  ]},
  {id:'activity',title:'Hoạt độ và thời gian phân rã',items:[
   item('Định luật phân rã','Một đồng vị có λ không đổi, không có nguồn bổ sung hạt nhân. N₀ là số hạt nhân ở t = 0. N(t) là giá trị trung bình thống kê.',math('N(t)=N_0e^{-\\lambda t}')),
   item('Hoạt độ','Số phân rã trung bình trong một đơn vị thời gian. A viết kiểu chữ riêng để phân biệt với số khối.',math('\\mathcal A=-\\frac{dN}{dt}=\\lambda N')),
   item('Becquerel và curie','Becquerel là một phân rã mỗi giây. Curie được định nghĩa bằng 3,70 × 10¹⁰ Bq.',math('1\\,\\mathrm{Ci}=3{,}70\\times10^{10}\\,\\mathrm{Bq}')),
   item('Chu kỳ bán rã','Thời gian để số hạt nhân hoặc hoạt độ giảm một nửa trong cùng mô hình.',math('T_{1/2}=\\frac{\\ln2}{\\lambda}')),
   item('Thời gian sống trung bình','Trung bình thời gian sống đối với phân bố mũ. Cũng là thời gian để số hạt nhân giảm theo hệ số e.',math('\\tau=\\frac1\\lambda=\\frac{T_{1/2}}{\\ln2}')),
   item('Định tuổi từ hoạt độ','Mẫu không trao đổi hay nhận thêm đồng vị sau mốc ban đầu. Hoạt độ ban đầu phải được xác định cho cùng lượng vật chất phù hợp.',math('t=\\frac1\\lambda\\ln\\frac{\\mathcal A_0}{\\mathcal A}')),
  ]},
  {id:'radiation',title:'Các đại lượng liều bức xạ',items:[
   item('Liều hấp thụ','Eabs là năng lượng truyền cho phần vật chất có khối lượng m. Gray bằng joule trên kilogram.',math('D=E_{\\rm abs}/m')),
   item('Gray và rad','Đơn vị đo liều hấp thụ, không phải đơn vị hoạt độ.',math('1\\,\\mathrm{rad}=0{,}01\\,\\mathrm{Gy}')),
   item('Liều tương đương trong mô hình RBE','H là liều tương đương, D là liều hấp thụ. RBE mô tả hiệu quả sinh học tương đối của loại bức xạ trong mô và năng lượng đang xét, với đơn vị chuyển đổi nhất quán.',math('H=\\mathrm{RBE}\\,D')),
   item('Sievert và rem','Đơn vị liều tương đương. Hệ số RBE được dùng theo Sv/Gy hoặc rem/rad trong phép quy đổi tương ứng.',math('1\\,\\mathrm{rem}=0{,}01\\,\\mathrm{Sv}')),
  ]},
  {id:'reactions',title:'Năng lượng và ngưỡng phản ứng',items:[
   item('Năng lượng phản ứng','ΔM là tổng khối lượng ban đầu trừ tổng khối lượng cuối. Các khối lượng phải cân bằng số electron nếu dùng khối lượng nguyên tử.',math('Q=\\Delta Mc^2')),
   item('Tỏa năng lượng và thu năng lượng','Q > 0 làm tăng tổng động năng khả dụng. Q < 0 đòi hỏi cung cấp động năng. Động lượng, điện tích và các đại lượng bảo toàn khác vẫn phải thỏa mãn.'),
   item('Động năng khối tâm','Hạt tới có khối lượng m và động năng K, bia có khối lượng M đứng yên. Gần đúng phi tương đối tính.',math('K_{\\rm cm}=\\frac{M}{M+m}K')),
   item('Ngưỡng động năng trong phòng thí nghiệm','Phản ứng thu năng lượng, bia đứng yên và gần đúng phi tương đối tính. Bỏ qua điều kiện bổ sung của hàng rào thế.',math('K_{\\rm th}\\approx-(1+m/M)Q')),
   item('Hàng rào Coulomb','Hai hạt nhân mang điện Z₁e và Z₂e, cách nhau r trong gần đúng đối xứng cầu. Tương tác hạt nhân và xuyên ngầm còn cần xét khi mô tả phản ứng.',math('U_C=\\frac{Z_1Z_2e^2}{4\\pi\\varepsilon_0r}')),
  ]},
  {id:'fission-fusion',title:'Phân hạch và nhiệt hạch',items:[
   item('Phân hạch','Hạt nhân nặng tách thành các mảnh nhẹ hơn, có thể kèm neutron và bức xạ. Tổng năng lượng liên kết tăng tương ứng với tổng năng lượng nghỉ giảm.'),
   item('Phản ứng dây chuyền','Neutron của phản ứng trước kích thích các phân hạch tiếp theo. Khả năng tự duy trì phụ thuộc cả sinh neutron lẫn hấp thụ và thất thoát.'),
   item('Công suất phản ứng','Nf chấm là số phản ứng mỗi giây, Ef là năng lượng hữu ích theo mô hình mỗi phản ứng. Không đồng nhất công suất nhiệt với công suất điện.',math('P=\\dot N_fE_f')),
   item('Nhiệt phân rã','Các sản phẩm phóng xạ còn sinh nhiệt sau khi phản ứng dây chuyền đã dừng.'),
   item('Nhiệt hạch','Các hạt nhân nhẹ kết hợp thành hạt nhân lớn hơn. Q phụ thuộc chênh lệch khối lượng, còn tốc độ phụ thuộc hàng rào, động năng và xuyên ngầm.'),
   item('Chuỗi proton–proton','Qua các phản ứng trung gian, bốn proton tạo một hạt nhân heli-4, hai positron và hai neutrino electron. Cân bằng năng lượng còn phải kể sự hủy cặp của positron và năng lượng neutrino mang đi.'),
  ]},
 ],
}
