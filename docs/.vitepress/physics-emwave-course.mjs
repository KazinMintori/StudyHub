const note='12-song-dien-tu'
const display=s=>'$$\n'+s+'\n$$'
const slide=(title,bullets,formula)=>({note,title,bullets,formula})
export const emWaveTopics=[{title:'Trường, năng lượng và sự phản xạ của sóng điện từ',topics:[
 {slug:'maxwell-song-dien-tu',title:'Maxwell và nguồn sóng điện từ',question:'Vì sao hai trường biến thiên có thể truyền trong chân không?',source:'32.1'},
 {slug:'song-phang-van-toc-anh-sang',title:'Sóng phẳng và tốc độ ánh sáng',question:'Các phương trình trường quyết định tốc độ và hướng truyền như thế nào?',source:'32.2'},
 {slug:'song-hinh-sin',title:'Sóng hình sin và môi trường vật chất',question:'Biên độ, pha, bước sóng và vật liệu liên hệ ra sao?',source:'32.3'},
 {slug:'nang-luong-dong-luong',title:'Năng lượng, động lượng và áp suất bức xạ',question:'Sóng mang công suất và tạo lực lên vật nhận như thế nào?',source:'32.4'},
 {slug:'song-dung-dien-tu',title:'Sóng đứng và hốc cộng hưởng',question:'Phản xạ tạo nút, bụng và các tần số riêng nào?',source:'32.5'}
]}]
export const emWaveSlides=[
 slide('Trường biến thiên liên hệ hai phía của điện từ',[
  'Faraday liên hệ từ thông biến thiên với điện trường có lưu thông.',
  'Ampère–Maxwell kể cả dòng điện dịch khi điện trường biến thiên.',
  'Điện tích chuyển động có gia tốc có thể phát bức xạ. Sóng truyền được qua chân không.'
 ],display('\\begin{aligned}&\\oint\\vec E\\cdot d\\vec l=-\\frac{d\\Phi_B}{dt}\\\\&\\oint\\vec B\\cdot d\\vec l\\\\&=\\mu_0\\left(i_C+\\varepsilon_0\\frac{d\\Phi_E}{dt}\\right).\\end{aligned}')),
 slide('Một sóng phẳng chạy có hai trường ngang',[
  'Các trường đồng đều trên mỗi mặt phẳng vuông góc hướng truyền.',
  'Điện trường, từ trường và hướng truyền tạo bộ ba vuông góc.',
  'Tích có hướng của hai trường xác định hướng dòng năng lượng.'
 ],display('\\begin{aligned}&\\vec E\\cdot\\vec B=0\\\\&E=cB\\\\&\\vec S=\\frac1{\\mu_0}\\vec E\\times\\vec B.\\end{aligned}')),
 slide('Tốc độ ánh sáng xuất hiện từ hằng số điện và từ',[
  'Faraday và Ampère–Maxwell cùng phải thỏa cho một mặt sóng.',
  'Hai quan hệ biên độ quyết định tốc độ trong chân không.',
  'Trường biến thiên không truyền tức thời.'
 ],display('\\begin{aligned}&E=cB\\\\&B=\\varepsilon_0\\mu_0cE\\\\&c=\\frac1{\\sqrt{\\varepsilon_0\\mu_0}}.\\end{aligned}')),
 slide('Hàm sóng giữ cả dấu pha và hướng trường',[
  'Pha kx−ωt truyền theo+x, còn kx+ωt truyền theo−x.',
  'Khi đổi hướng truyền, phải đổi quan hệ hướng giữa E và B.',
  'Trong sóng chạy hình sin, hai trường cùng pha.'
 ],display('\\begin{aligned}&\\omega=ck\\\\&k=2\\pi/\\lambda\\\\&f=c/\\lambda\\\\&E_{\\max}=cB_{\\max}.\\end{aligned}')),
 slide('Phổ điện từ là một họ sóng với nhiều thang bước sóng',[
  'Radio, vi ba, hồng ngoại, ánh sáng nhìn thấy, tử ngoại, tia X và gamma cùng có bản chất điện từ.',
  'Tần số và bước sóng thay đổi, nhưng tốc độ chân không là c.',
  'Phân cực mô tả hướng dao động ngang của điện trường.'
 ],display('f\\lambda=c.')),
 slide('Vật liệu đổi tốc độ và bước sóng',[
  'Tại mặt phân cách đứng yên, tần số được giữ.',
  'Hằng số vật liệu phải xét ở tần số của sóng.',
  'Công thức dưới dùng mô hình tuyến tính, đồng nhất, đẳng hướng, không tán sắc và không tổn hao.'
 ],display('\\begin{aligned}&v=\\frac c{\\sqrt{\\varepsilon_r\\mu_r}}\\\\&\\lambda=v/f\\\\&n=c/v\\\\&E_{\\max}=vB_{\\max}.\\end{aligned}')),
 slide('Cường độ liên hệ công suất với biên độ trường',[
  'Vector Poynting cho dòng năng lượng tức thời theo hướng.',
  'Cường độ sóng chạy là độ lớn vector Poynting sau khi lấy trung bình.',
  'Biên độ phải bình phương. Giá trị hiệu dụng đã chứa hệ số trung bình của sóng hình sin.'
 ],display('\\begin{aligned}&I=|\\langle\\vec S\\rangle|\\\\&I=\\frac12\\varepsilon_0cE_{\\max}^2\\\\&I=\\frac c{2\\mu_0}B_{\\max}^2.\\end{aligned}')),
 slide('Động lượng của ánh sáng tạo áp suất',[
  'Hấp thụ nhận động lượng tới, còn phản xạ ngược chiều nhận gấp đôi.',
  'Các công thức áp suất này xét sóng tới vuông góc.',
  'Công suất có thể đáng kể trong khi lực rất nhỏ vì chia cho tốc độ ánh sáng.'
 ],display('\\begin{aligned}&\\vec g=\\vec S/c^2\\\\&p_{\\mathrm a}=I/c\\\\&p_{\\mathrm r}=2I/c\\\\&F=pA.\\end{aligned}')),
 slide('Sóng đứng vẫn chứa năng lượng dù dòng trung bình triệt tiêu',[
  'Hai sóng chạy bằng nhau đi ngược chiều tạo sóng đứng.',
  'Hai trường vuông pha theo thời gian, nút điện là bụng từ và ngược lại.',
  'Trung bình vector Poynting bằng không. Trung bình độ lớn của nó có thể khác không.'
 ],display('\\begin{aligned}&S_x=S_0\\sin(2kx)\\sin(2\\omega t)\\\\&\\langle S_x\\rangle=0\\\\&S_0=E_{\\max}B_{\\max}/\\mu_0.\\end{aligned}')),
 slide('Hai tường dẫn chọn các mode của hốc',[
  'Hai tường là nút điện trường tiếp tuyến trong mô hình dẫn lý tưởng.',
  'Mỗi nửa bước sóng chứa một bụng điện trường.',
  'Đo khoảng cách bụng và biết tần số cho phép suy tốc độ.'
 ],display('\\begin{aligned}&L=n\\lambda_n/2\\\\&\\lambda_n=2L/n\\\\&f_n=nc/(2L)\\\\&n=1,2,3,\\ldots.\\end{aligned}'))
]
export const emWaveCheatsheet={title:'Cheatsheet: Sóng điện từ',lead:'Định nghĩa, tính chất, công thức và điều kiện của sóng phẳng, sóng hình sin, dòng năng lượng, áp suất bức xạ và sóng đứng.',sections:[
 {id:'maxwell',title:'Maxwell trong chân không',items:[
  {name:'Hai định luật Gauss',formula:display('\\begin{aligned}&\\oint\\vec E\\cdot d\\vec A=Q_{\\mathrm{enc}}/\\varepsilon_0\\\\&\\oint\\vec B\\cdot d\\vec A=0.\\end{aligned}'),description:'Tích phân trên mặt kín, pháp tuyến hướng ra ngoài.',variables:['$\\vec E$: Điện trường ($\\mathrm{V/m}$).','$\\vec B$: Cảm ứng từ ($\\mathrm T$).','$Q_{\\mathrm{enc}}$: Điện tích trong mặt kín ($\\mathrm C$).','$\\varepsilon_0$: Hằng số điện ($\\mathrm{F/m}$).','$d\\vec A$: Vector diện tích ($\\mathrm{m^2}$).']},
  {name:'Hai định luật lưu thông',formula:display('\\begin{aligned}&\\oint\\vec E\\cdot d\\vec l=-d\\Phi_B/dt\\\\&\\oint\\vec B\\cdot d\\vec l\\\\&=\\mu_0(i_C+\\varepsilon_0d\\Phi_E/dt).\\end{aligned}'),description:'Đường kín đứng yên. Chiều đường và pháp tuyến mặt căng liên hệ bằng quy tắc bàn tay phải.',variables:['$\\Phi_B$: Từ thông ($\\mathrm{Wb}$).','$\\Phi_E$: Thông lượng điện trường ($\\mathrm{V\\,m}$).','$i_C$: Dòng dẫn xuyên mặt ($\\mathrm A$).','$\\mu_0$: Hằng số từ ($\\mathrm{H/m}$).','$t$: Thời gian ($\\mathrm s$).']}
 ]},
 {id:'plane',title:'Sóng phẳng chạy trong chân không',items:[
  {name:'Vận tốc và quan hệ hai trường',formula:display('\\begin{aligned}&c=1/\\sqrt{\\varepsilon_0\\mu_0}\\\\&E=cB\\\\&\\vec E\\perp\\vec B\\\\&\\vec E,\\vec B\\perp\\vec k.\\end{aligned}'),description:'Một sóng phẳng chạy duy nhất trong chân không. Các trường đồng đều trên mặt phẳng vuông góc hướng truyền. Không áp dụng E=cB cho một sóng đứng tổng.',variables:['$c$: Tốc độ ánh sáng chân không ($\\mathrm{m/s}$).','$\\vec k$: Vector sóng, hướng truyền, độ lớn k ($\\mathrm{rad/m}$).']},
  {name:'Tần số, bước sóng và số sóng',formula:display('\\begin{aligned}&f\\lambda=c\\\\&\\omega=2\\pi f\\\\&k=2\\pi/\\lambda\\\\&\\omega=ck.\\end{aligned}'),description:'Hình sin trong chân không. Phân cực thẳng nghĩa điện trường dao động theo một phương ngang cố định.',variables:['$f$: Tần số ($\\mathrm{Hz}$).','$\\lambda$: Bước sóng ($\\mathrm m$).','$\\omega$: Tần số góc ($\\mathrm{rad/s}$).','$k$: Số sóng ($\\mathrm{rad/m}$).']}
 ]},
 {id:'sinusoid-medium',title:'Pha và môi trường',items:[
  {name:'Truyền theo+x hoặc−x',formula:display('\\begin{aligned}&\\theta_+=kx-\\omega t\\\\&E_y=E_{\\max}\\cos\\theta_+\\\\&B_z=B_{\\max}\\cos\\theta_+\\\\&\\theta_-=kx+\\omega t\\\\&E_y=E_{\\max}\\cos\\theta_-\\\\&B_z=-B_{\\max}\\cos\\theta_-.\\end{aligned}'),description:'Chọn điện trường dọc y. Biên độ Emax,Bmax dương và Emax=cBmax.',variables:['$E_{\\max}$: Biên độ điện trường ($\\mathrm{V/m}$).','$B_{\\max}$: Biên độ từ trường ($\\mathrm T$).','$\\theta_+,\\theta_-$: Pha ($\\mathrm{rad}$).']},
  {name:'Tốc độ trong vật liệu',formula:display('\\begin{aligned}&v=1/\\sqrt{\\varepsilon\\mu}\\\\&v=c/\\sqrt{\\varepsilon_r\\mu_r}\\\\&n=c/v\\\\&\\lambda=v/f\\\\&E_{\\max}=vB_{\\max}.\\end{aligned}'),description:'Mô hình tuyến tính, đồng nhất, đẳng hướng, không tán sắc và không tổn hao ở tần số xét. Mặt phân cách đứng yên giữ tần số.',variables:['$v$: Tốc độ pha ($\\mathrm{m/s}$).','$\\varepsilon,\\mu$: Điện thẩm ($\\mathrm{F/m}$), từ thẩm ($\\mathrm{H/m}$).','$\\varepsilon_r,\\mu_r,n$: Hệ số tương đối, chiết suất (không thứ nguyên).']}
 ]},
 {id:'energy-flow',title:'Năng lượng và cường độ',items:[
  {name:'Mật độ năng lượng',formula:display('\\begin{aligned}&u_E=\\varepsilon_0E^2/2\\\\&u_B=B^2/(2\\mu_0)\\\\&u=u_E+u_B.\\end{aligned}'),description:'Trường trong chân không. Với một sóng phẳng chạy, uE=uB và u=ε0E²=B²/μ0.',variables:['$u,u_E,u_B$: Mật độ năng lượng ($\\mathrm{J/m^3}$).']},
  {name:'Vector Poynting',formula:display('\\begin{aligned}&\\vec S=\\vec E\\times\\vec B/\\mu_0\\\\&P=\\int_A\\vec S\\cdot d\\vec A.\\end{aligned}'),description:'Công suất qua mặt định hướng A. Trong chân không, vector S biểu thị hướng và độ lớn dòng năng lượng tức thời.',variables:['$\\vec S$: Dòng năng lượng trên diện tích ($\\mathrm{W/m^2}$).','$P$: Công suất ($\\mathrm W$).','$A$: Diện tích ($\\mathrm{m^2}$).']},
  {name:'Cường độ sóng hình sin',formula:display('\\begin{aligned}&I=|\\langle\\vec S\\rangle|\\\\&I=E_{\\max}B_{\\max}/(2\\mu_0)\\\\&I=\\varepsilon_0cE_{\\max}^2/2\\\\&I=cB_{\\max}^2/(2\\mu_0)\\\\&I=\\varepsilon_0cE_{\\mathrm{rms}}^2.\\end{aligned}'),description:'Một sóng phẳng chạy trong chân không. Dấu ngoặc là trung bình chu kỳ, Erms=Emax/√2. Độ lớn của trung bình vector khác trung bình độ lớn khi vector đổi chiều.',variables:['$I$: Cường độ bức xạ ($\\mathrm{W/m^2}$).','$E_{\\mathrm{rms}}$: Điện trường hiệu dụng ($\\mathrm{V/m}$).']},
  {name:'Phân bố công suất',formula:display('\\begin{aligned}&I=P/(4\\pi r^2)\\\\&I_{\\mathrm{bán\\,cầu}}=P/(2\\pi r^2)\\\\&I_{\\mathrm{chùm}}=P/A.\\end{aligned}'),description:'Lần lượt là nguồn điểm đẳng hướng toàn không gian, nguồn đều trong bán cầu và chùm đều trên tiết diện. Bỏ qua hấp thụ trên đường truyền.',variables:['$r$: Khoảng cách đến nguồn ($\\mathrm m$).']}
 ]},
 {id:'momentum',title:'Động lượng và áp suất bức xạ',items:[
  {name:'Mật độ và tốc độ truyền động lượng',formula:display('\\begin{aligned}&\\vec g=\\vec S/c^2\\\\&\\frac1A\\frac{dp}{dt}=S/c.\\end{aligned}'),description:'Sóng chạy trong chân không, diện tích vuông góc hướng truyền. p ở đây là động lượng.',variables:['$\\vec g$: Mật độ động lượng ($\\mathrm{kg\\,m^{-2}\\,s^{-1}}$).','$p$: Động lượng ($\\mathrm{kg\\,m/s}$).']},
  {name:'Hấp thụ và phản xạ',formula:display('\\begin{aligned}&p_{\\mathrm a}=I/c\\\\&p_{\\mathrm r}=2I/c\\\\&F=p_{\\mathrm{rad}}A.\\end{aligned}'),description:'Tới vuông góc, hấp thụ hoàn toàn hoặc phản xạ ngược hoàn toàn. Áp suất là trung bình theo thời gian.',variables:['$p_{\\mathrm a},p_{\\mathrm r},p_{\\mathrm{rad}}$: Áp suất ($\\mathrm{Pa}$).','$F$: Lực ($\\mathrm N$).']}
 ]},
 {id:'standing',title:'Sóng đứng và hốc cộng hưởng',items:[
  {name:'Hai trường của sóng đứng',formula:display('\\begin{aligned}&E_y=-2E_0\\sin(kx)\\sin(\\omega t)\\\\&B_z=-2B_0\\cos(kx)\\cos(\\omega t)\\\\&E_0=cB_0.\\end{aligned}'),description:'Tường phản xạ lý tưởng tại x=0, sóng tới từ+x theo−x. E0,B0 là biên độ của mỗi sóng thành phần, không phải biên độ tổng tại bụng.',variables:['$x$: Vị trí ($\\mathrm m$).','$E_0,B_0$: Biên độ sóng thành phần ($\\mathrm{V/m}$, $\\mathrm T$).']},
  {name:'Nút và bụng',formula:display('\\begin{aligned}&x_E=n\\lambda/2\\\\&x_B=(2n+1)\\lambda/4\\\\&n=0,1,2,\\ldots.\\end{aligned}'),description:'xE là nút điện trường, xB là nút từ trường. Nút của trường này là bụng của trường kia. Hai trường vuông pha theo thời gian.'},
  {name:'Dòng năng lượng trong sóng đứng',formula:display('\\begin{aligned}&S_0=E_0B_0/\\mu_0\\\\&S_x=S_0\\sin(2kx)\\sin(2\\omega t)\\\\&\\langle S_x\\rangle=0.\\end{aligned}'),description:'Sóng đứng lý tưởng do hai sóng bằng nhau ngược chiều. Mật độ năng lượng vẫn có thể dương, dòng tức thời có thể đổi chiều.'},
  {name:'Các mode giữa hai tường',formula:display('\\begin{aligned}&L=n\\lambda_n/2\\\\&\\lambda_n=2L/n\\\\&f_n=nc/(2L)\\\\&n=1,2,3,\\ldots.\\end{aligned}'),description:'Hốc một chiều dài L, hai tường là nút điện trường tiếp tuyến. Mỗi mode n có n mặt bụng điện trường giữa hai tường.',variables:['$L$: Khoảng cách hai tường ($\\mathrm m$).','$n$: Số mode nguyên dương (không thứ nguyên).']}
 ]}
]}
