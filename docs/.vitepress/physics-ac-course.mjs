const note='11-dong-dien-xoay-chieu'
const display=s=>'$$\n'+s+'\n$$'
const slide=(title,bullets,formula='')=>({note,title,bullets,formula})
export const acTopics=[{title:'Pha, đáp ứng và năng lượng của mạch xoay chiều',topics:[
 {slug:'gian-do-pha-hieu-dung',title:'Giản đồ pha và giá trị hiệu dụng',question:'Một vector quay biểu diễn dòng hình sin và giá trị hiệu dụng ra sao?',source:'31.1'},
 {slug:'dien-tro-dien-khang',title:'Điện trở và điện kháng',question:'Vì sao điện trở, cuộn cảm và tụ có quan hệ pha khác nhau?',source:'31.2'},
 {slug:'mach-rlc-noi-tiep',title:'Mạch RLC nối tiếp có nguồn',question:'Cộng các điện áp lệch pha để tìm trở kháng như thế nào?',source:'31.3'},
 {slug:'cong-suat-xoay-chieu',title:'Công suất và hệ số công suất',question:'Điện áp và dòng lệch pha làm công suất trung bình thay đổi ra sao?',source:'31.4'},
 {slug:'cong-huong',title:'Cộng hưởng trong mạch xoay chiều',question:'Tần số nào cho dòng lớn nhất và điện trở làm đổi đỉnh thế nào?',source:'31.5'},
 {slug:'may-bien-ap',title:'Máy biến áp',question:'Hai cuộn ghép từ đổi điện áp, dòng và điện trở nhìn từ nguồn ra sao?',source:'31.6'}
]}]
export const acSlides=[
 slide('Vector pha biến dao động hình sin thành hình chiếu',[
  'Độ dài vector bằng biên độ và tốc độ quay bằng tần số góc.',
  'Hình chiếu ngang cho giá trị tức thời khi dùng cosin.',
  'Vector pha biểu diễn biên độ và pha, không chỉ một hướng vật lý trong không gian.'
 ],display('\\begin{aligned}&i=I\\cos\\omega t\\\\&\\omega=2\\pi f.\\end{aligned}')),
 slide('Trung bình, trung bình chỉnh lưu và hiệu dụng khác nhau',[
  'Dòng hình sin có trung bình bằng không qua một số nguyên chu kỳ.',
  'Chỉnh lưu toàn sóng giữ dấu dòng qua điện kế cùng chiều.',
  'Giá trị hiệu dụng được lấy bằng căn của trung bình bình phương.'
 ],display('\\begin{aligned}&I_{\\mathrm{rav}}=\\frac2\\pi I\\\\&I_{\\mathrm{rms}}=\\frac I{\\sqrt2}\\\\&V_{\\mathrm{rms}}=\\frac V{\\sqrt2}.\\end{aligned}')),
 slide('Điện trở giữ điện áp và dòng cùng pha',[
  'Định luật Ohm liên hệ các giá trị tức thời trên điện trở thuần.',
  'Các cực đại, cực tiểu và điểm bằng không xuất hiện cùng lúc.',
  'Tỉ số biên độ cũng bằng điện trở.'
 ],display('\\begin{aligned}&v_R=iR\\\\&V_R=IR.\\end{aligned}')),
 slide('Cuộn cảm làm điện áp sớm dòng một phần tư chu kỳ',[
  'Điện áp cuộn theo quy ước thụ động phụ thuộc đạo hàm dòng.',
  'Cảm kháng tăng theo tần số và điện cảm.',
  'Quan hệ giữa biên độ không thay thế được quan hệ tức thời.'
 ],display('\\begin{aligned}&v_L=L\\frac{di}{dt}\\\\&X_L=\\omega L\\\\&V_L=IX_L.\\end{aligned}')),
 slide('Tụ làm điện áp trễ dòng một phần tư chu kỳ',[
  'Dòng là điện dung nhân tốc độ thay đổi điện áp.',
  'Dung kháng giảm khi tần số hoặc điện dung tăng.',
  'Dòng dẫn không xuyên qua điện môi, nhưng dòng điện dịch duy trì sự liên tục.'
 ],display('\\begin{aligned}&i=C\\frac{dv_C}{dt}\\\\&X_C=\\frac1{\\omega C}\\\\&V_C=IX_C.\\end{aligned}')),
 slide('RLC nối tiếp cần cộng vector điện áp',[
  'Dòng tức thời như nhau trên mọi phần tử nối tiếp.',
  'Điện áp cuộn cảm và tụ ngược pha, nên điện kháng tổng là hiệu hai điện kháng.',
  'Biên độ nguồn là độ lớn tổng vector, còn các điện áp tức thời cộng đại số.'
 ],display('\\begin{aligned}&X=X_L-X_C\\\\&Z=\\sqrt{R^2+X^2}\\\\&V=IZ.\\end{aligned}')),
 slide('Góc pha phụ thuộc dấu điện kháng tổng',[
  'Chọn dòng làm mốc, góc pha dương nghĩa điện áp nguồn sớm dòng.',
  'Cảm kháng lớn hơn dung kháng cho góc dương, còn dung kháng lớn hơn cho góc âm.',
  'Các tỉ số điện áp và dòng giữ nguyên khi đồng loạt dùng hiệu dụng.'
 ],display('\\begin{aligned}&\\tan\\phi=\\frac{X_L-X_C}{R}\\\\&v=V\\cos(\\omega t+\\phi)\\\\&V_{\\mathrm{rms}}=I_{\\mathrm{rms}}Z.\\end{aligned}')),
 slide('Công suất trung bình nhận thành phần điện áp cùng pha',[
  'Điện trở tiêu tán năng lượng theo cả hai chiều dòng.',
  'Cuộn cảm và tụ lý tưởng nhận rồi trả năng lượng, với công suất trung bình bằng không.',
  'Trong RLC nối tiếp, toàn bộ công suất nhận ròng được tiêu tán trên điện trở.'
 ],display('\\begin{aligned}&p=vi\\\\&P_{\\mathrm{av}}=\\frac12VI\\cos\\phi\\\\&\\quad=V_{\\mathrm{rms}}I_{\\mathrm{rms}}\\cos\\phi.\\end{aligned}')),
 slide('Hệ số công suất thấp làm dòng đường dây lớn hơn',[
  'Với cùng điện áp và công suất trung bình, hệ số công suất nhỏ đòi hỏi dòng lớn.',
  'Dòng lớn tăng tổn hao nhiệt trên đường dây.',
  'Tụ song song có thể bù thành phần dòng trễ của tải cảm.'
 ],display('\\begin{aligned}&\\cos\\phi=\\frac RZ\\\\&I_{\\mathrm{rms}}=\\frac{P_{\\mathrm{av}}}{V_{\\mathrm{rms}}\\cos\\phi}.\\end{aligned}')),
 slide('Cộng hưởng dòng xảy ra khi hai điện kháng bằng nhau',[
  'Giữ biên độ nguồn cố định và R dương, dòng lớn nhất khi trở kháng nhỏ nhất.',
  'Tại cộng hưởng, điện áp cuộn và tụ triệt tiêu tức thời, còn nguồn cùng pha dòng.',
  'Điện trở nhỏ tạo đỉnh cao và hẹp hơn, còn vị trí đỉnh do L,C quyết định.'
 ],display('\\begin{aligned}&\\omega_0=\\frac1{\\sqrt{LC}}\\\\&X_L=X_C\\\\&Z_{\\min}=R\\\\&I_{\\max}=\\frac VR.\\end{aligned}')),
 slide('Máy biến áp đổi điện áp và dòng, giữ công suất lý tưởng',[
  'Hai cuộn cùng nhận từ thông biến thiên trong lõi.',
  'Tỉ số điện áp bằng tỉ số số vòng khi bỏ qua sụt áp và từ thông rò.',
  'Với tải thuần trở và dòng từ hóa được bỏ qua, tăng áp đi kèm giảm dòng.'
 ],display('\\begin{aligned}&\\frac{V_2}{V_1}=\\frac{N_2}{N_1}\\\\&V_1I_1=V_2I_2\\\\&R_{\\mathrm{nhìn}}=R\\left(\\frac{N_1}{N_2}\\right)^2.\\end{aligned}'))
]
export const acCheatsheet={title:'Cheatsheet: Dòng điện xoay chiều',lead:'Định nghĩa, tính chất và công thức của đại lượng hình sin, điện kháng, trở kháng, công suất, cộng hưởng và máy biến áp.',sections:[
 {id:'phasor-rms',title:'Đại lượng hình sin và hiệu dụng',items:[
  {name:'Giá trị tức thời và tần số',formula:display('\\begin{aligned}&i=I\\cos\\omega t\\\\&v=V\\cos(\\omega t+\\phi)\\\\&\\omega=2\\pi f\\\\&T=1/f.\\end{aligned}'),description:'I,V là biên độ, φ là pha điện áp so với dòng. Vector pha quay ngược chiều kim đồng hồ, hình chiếu ngang cho giá trị tức thời.',variables:['$i,I$: Dòng tức thời, biên độ ($\\mathrm A$).','$v,V$: Điện áp tức thời, biên độ ($\\mathrm V$).','$t,T$: Thời gian, chu kỳ ($\\mathrm s$).','$\\omega$: Tần số góc ($\\mathrm{rad/s}$).','$f$: Tần số ($\\mathrm{Hz}$).','$\\phi$: Góc pha ($\\mathrm{rad}$).']},
  {name:'Định nghĩa hiệu dụng',formula:display('\\begin{aligned}&I_{\\mathrm{rms}}=\\sqrt{\\overline{i^2}}\\\\&V_{\\mathrm{rms}}=\\sqrt{\\overline{v^2}}.\\end{aligned}'),description:'Dấu gạch ngang là trung bình qua chu kỳ. Hiệu dụng không âm và khác trung bình chỉnh lưu.'},
  {name:'Dạng sóng hình sin',formula:display('\\begin{aligned}&\\overline i=0\\\\&I_{\\mathrm{rav}}=\\frac2\\pi I\\\\&I_{\\mathrm{rms}}=\\frac I{\\sqrt2}\\\\&V_{\\mathrm{rms}}=\\frac V{\\sqrt2}.\\end{aligned}'),description:'Hình sin không có thành phần một chiều. Irav là trung bình sau chỉnh lưu toàn sóng.'}
 ]},
 {id:'reactance',title:'Điện trở, cảm kháng và dung kháng',items:[
  {name:'Điện trở thuần',formula:display('\\begin{aligned}&v_R=iR\\\\&V_R=IR\\\\&\\phi_R=0.\\end{aligned}'),description:'Điện áp cùng pha dòng. R không phụ thuộc tần số trong mô hình lý tưởng.',variables:['$R$: Điện trở ($\\Omega$).']},
  {name:'Cuộn cảm thuần',formula:display('\\begin{aligned}&v_L=L\\frac{di}{dt}\\\\&X_L=\\omega L\\\\&V_L=IX_L\\\\&\\phi_L=+\\pi/2.\\end{aligned}'),description:'Quy ước điện áp thụ động, dòng đi vào đầu được chọn điện thế dương. Điện áp sớm dòng 90 độ, bỏ qua điện trở cuộn.',variables:['$L$: Điện cảm ($\\mathrm H$).','$X_L$: Cảm kháng ($\\Omega$).']},
  {name:'Tụ điện thuần',formula:display('\\begin{aligned}&q=Cv_C\\\\&i=C\\frac{dv_C}{dt}\\\\&X_C=\\frac1{\\omega C}\\\\&V_C=IX_C\\\\&\\phi_C=-\\pi/2.\\end{aligned}'),description:'C không đổi, điện áp trễ dòng 90 độ. Quan hệ hình sin không chứa điện tích một chiều.',variables:['$C$: Điện dung ($\\mathrm F$).','$q$: Điện tích bản được chọn ($\\mathrm C$).','$X_C$: Dung kháng ($\\Omega$).']},
  {name:'Giới hạn tần số',formula:display('\\begin{aligned}&\\omega\\to0:\\ X_L\\to0\\\\&\\qquad X_C\\to\\infty\\\\&\\omega\\to\\infty:\\ X_L\\to\\infty\\\\&\\qquad X_C\\to0.\\end{aligned}'),description:'L,C dương không đổi. Giới hạn một chiều là trạng thái ổn định.'}
 ]},
 {id:'series',title:'Mạch RLC nối tiếp và pha',items:[
  {name:'Kirchhoff và biên độ nguồn',formula:display('\\begin{aligned}&v=v_R+v_L+v_C\\\\&V^2=V_R^2+(V_L-V_C)^2.\\end{aligned}'),description:'Dòng tức thời như nhau trên mọi phần tử nối tiếp. Biên độ được cộng bằng vector pha.'},
  {name:'Trở kháng nối tiếp',formula:display('\\begin{aligned}&X=X_L-X_C\\\\&\\quad=\\omega L-\\frac1{\\omega C}\\\\&Z=\\sqrt{R^2+X^2}\\\\&V=IZ\\\\&V_{\\mathrm{rms}}=I_{\\mathrm{rms}}Z.\\end{aligned}'),description:'RLC nối tiếp lý tưởng ở một tần số dương. Dùng đồng nhất biên độ hoặc hiệu dụng.',variables:['$X,Z$: Điện kháng tổng, độ lớn trở kháng ($\\Omega$).']},
  {name:'Góc pha và hệ số công suất',formula:display('\\begin{aligned}&\\tan\\phi=X/R\\\\&\\cos\\phi=R/Z.\\end{aligned}'),description:'R dương. X dương cho điện áp sớm dòng, X âm cho điện áp trễ dòng. Góc nằm giữa âm và dương π/2.'},
  {name:'Bỏ một phần tử',formula:display('\\begin{aligned}&R=0\\\\&L=0\\\\&X_C=0\\quad(C\\to\\infty).\\end{aligned}'),description:'Lần lượt ứng với bỏ điện trở, bỏ cuộn cảm, nối tắt vị trí tụ. Bỏ tụ nối tiếp không tương đương C bằng không.'}
 ]},
 {id:'power',title:'Công suất và năng lượng',items:[
  {name:'Công suất tức thời và trung bình',formula:display('\\begin{aligned}&p=vi\\\\&P_{\\mathrm{av}}=\\frac12VI\\cos\\phi\\\\&\\quad=V_{\\mathrm{rms}}I_{\\mathrm{rms}}\\cos\\phi.\\end{aligned}'),description:'Điện áp và dòng hình sin cùng tần số. Công suất dương khi mạch nhận năng lượng, âm khi trả năng lượng.',variables:['$p,P_{\\mathrm{av}}$: Công suất tức thời, trung bình ($\\mathrm W$).','$\\cos\\phi$: Hệ số công suất (không thứ nguyên).']},
  {name:'Điện trở thuần',formula:display('\\begin{aligned}&P_R=I_{\\mathrm{rms}}^2R\\\\&\\quad=V_{R,\\mathrm{rms}}^2/R\\\\&\\quad=V_{R,\\mathrm{rms}}I_{\\mathrm{rms}}\\\\&p_{\\max}=VI\\\\&\\quad=2P_R.\\end{aligned}'),description:'Điện áp và dòng điện trở thuần hình sin, cùng pha. Công suất tức thời không âm.'},
  {name:'Phần tử tích trữ lý tưởng',formula:display('\\begin{aligned}&\\overline{p_L}=0,\\quad\\overline{p_C}=0\\\\&U_L=Li^2/2\\\\&U_C=Cv_C^2/2.\\end{aligned}'),description:'Trạng thái hình sin ổn định, trung bình qua chu kỳ. Năng lượng được nhận và trả, không tiêu tán.',variables:['$U_L,U_C$: Năng lượng từ trường, điện trường ($\\mathrm J$).']},
  {name:'RLC và tổn hao đường dây',formula:display('\\begin{aligned}&P_{\\mathrm{av}}=I_{\\mathrm{rms}}^2R\\\\&P_{\\mathrm{dây}}=I_{\\mathrm{rms}}^2R_{\\mathrm{dây}}.\\end{aligned}'),description:'RLC nối tiếp có cuộn cảm và tụ lý tưởng. Rdây là điện trở đường dây. Hệ số công suất thấp làm dòng cần thiết lớn hơn ở cùng công suất và điện áp.'}
 ]},
 {id:'resonance',title:'Cộng hưởng dòng nối tiếp',items:[
  {name:'Tần số và điều kiện',formula:display('\\begin{aligned}&\\omega_0=1/\\sqrt{LC}\\\\&f_0=1/(2\\pi\\sqrt{LC})\\\\&X_L=X_C.\\end{aligned}'),description:'L,C,R dương. Giữ biên độ nguồn cố định và xét cực đại biên độ dòng.',variables:['$\\omega_0,f_0$: Tần số góc ($\\mathrm{rad/s}$), tần số cộng hưởng ($\\mathrm{Hz}$).']},
  {name:'Tại cộng hưởng',formula:display('\\begin{aligned}&Z_{\\min}=R\\\\&I_{\\max}=V/R\\\\&\\phi=0\\\\&v_L+v_C=0\\\\&v_R=v.\\end{aligned}'),description:'Điện áp cuộn và tụ bằng nhau về biên độ, ngược pha. Từng điện áp có thể lớn hơn điện áp nguồn.'},
  {name:'Đường đáp ứng',formula:display('\\begin{aligned}&I(\\omega)=V/Z(\\omega)\\\\&Z(\\omega)=\\sqrt{R^2+X(\\omega)^2}\\\\&X(\\omega)=X_L-X_C.\\end{aligned}'),description:'Điện trở nhỏ cho đỉnh cao, hẹp hơn. Vị trí đỉnh dòng do L,C quyết định.'}
 ]},
 {id:'transformer',title:'Máy biến áp lý tưởng',items:[
  {name:'Faraday và tỉ số vòng',formula:display('\\begin{aligned}&\\mathcal E_1=-N_1\\frac{d\\Phi_B}{dt}\\\\&\\mathcal E_2=-N_2\\frac{d\\Phi_B}{dt}\\\\&V_2/V_1=N_2/N_1.\\end{aligned}'),description:'Cùng từ thông mỗi vòng, bỏ qua điện trở cuộn và từ thông rò. Điện áp cùng là biên độ hoặc cùng là hiệu dụng.',variables:['$N_1,N_2$: Số vòng sơ cấp, thứ cấp (không thứ nguyên).','$\\Phi_B$: Từ thông mỗi vòng ($\\mathrm{Wb}$).','$\\mathcal E_1,\\mathcal E_2$: Suất điện động ($\\mathrm V$).']},
  {name:'Dòng và công suất',formula:display('\\begin{aligned}&V_1I_1=V_2I_2\\\\&I_2/I_1=N_1/N_2.\\end{aligned}'),description:'Máy không tổn hao, bỏ qua dòng từ hóa không tải, tải thuần trở. Tăng áp giảm dòng, tần số không đổi.',variables:['$V_1,V_2$: Điện áp sơ cấp, thứ cấp ($\\mathrm V$).','$I_1,I_2$: Dòng sơ cấp, thứ cấp ($\\mathrm A$).']},
  {name:'Điện trở nhìn từ sơ cấp',formula:display('\\begin{aligned}&R_{\\mathrm{nhìn}}=V_1/I_1\\\\&\\quad=R(N_1/N_2)^2.\\end{aligned}'),description:'R là điện trở tải ở thứ cấp, máy lý tưởng.',variables:['$R_{\\mathrm{nhìn}}$: Điện trở tải quy đổi về sơ cấp ($\\Omega$).']}
 ]}
]}
