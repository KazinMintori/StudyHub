const note='13-truyen-anh-sang'
const display=s=>'$$\n'+s+'\n$$'
const slide=(title,bullets,formula)=>({note,title,bullets,formula})
export const opticsTopics=[{title:'Bản chất, đường truyền và trạng thái phân cực của ánh sáng',topics:[
 {slug:'ban-chat-anh-sang',title:'Bản chất ánh sáng, mặt sóng và tia',question:'Khi nào dùng mô hình sóng, hạt hay tia để mô tả ánh sáng?',source:'33.1'},
 {slug:'phan-xa-khuc-xa',title:'Phản xạ, khúc xạ và bước sóng',question:'Tia đổi hướng như thế nào khi gặp một mặt phân cách?',source:'33.2'},
 {slug:'phan-xa-toan-phan',title:'Phản xạ toàn phần và dẫn sáng',question:'Điều kiện nào giữ ánh sáng trong lăng kính hoặc sợi quang?',source:'33.3'},
 {slug:'tan-sac',title:'Tán sắc, lăng kính và cầu vồng',question:'Vì sao các màu đi theo những hướng khác nhau?',source:'33.4'},
 {slug:'phan-cuc',title:'Phân cực và tương tác với vật liệu',question:'Phương dao động điện trường quyết định ánh sáng truyền qua và phản xạ ra sao?',source:'33.5'},
 {slug:'tan-xa-anh-sang',title:'Tán xạ và màu sắc bầu trời',question:'Vì sao trời xanh, mây trắng và Mặt Trời đỏ lúc gần chân trời?',source:'33.6'},
 {slug:'nguyen-ly-huygens',title:'Nguyên lý Huygens',question:'Có thể suy đường tia từ sự tiến của mặt sóng như thế nào?',source:'33.7'}
]}]
export const opticsSlides=[
 slide('Mô hình của ánh sáng phụ thuộc hiện tượng',[
  'Ánh sáng là sóng điện từ. Sự truyền được mô tả bằng mô hình sóng.',
  'Phát xạ và hấp thụ bộc lộ tính chất hạt. Mô hình tia dùng trong quang hình học.',
  'Mặt sóng có cùng pha. Trong môi trường đồng nhất đẳng hướng, tia thẳng và vuông góc mặt sóng.'
 ],display('\\begin{aligned}&c=299\\,792\\,458\\,\\mathrm{m/s}\\\\&v=c/n\\\\&\\lambda=\\lambda_0/n.\\end{aligned}')),
 slide('Phản xạ và khúc xạ dùng góc với pháp tuyến',[
  'Tia tới, phản xạ, khúc xạ và pháp tuyến cùng nằm trong mặt phẳng tới.',
  'Mặt nhẵn tạo phản xạ gương, còn mặt nhám phân bố ánh sáng ra nhiều hướng.',
  'Tại mặt phân cách đứng yên, tần số không đổi. Đi vào chiết suất lớn hơn làm góc khúc xạ nhỏ hơn nếu tới xiên.'
 ],display('\\begin{aligned}&\\theta_r=\\theta_a\\\\&n_a\\sin\\theta_a=n_b\\sin\\theta_b\\\\&f_a=f_b.\\end{aligned}')),
 slide('Phản xạ toàn phần cần đúng cả môi trường và góc',[
  'Chỉ có ngưỡng khi ánh sáng đi từ chiết suất lớn sang chiết suất nhỏ.',
  'Tại ngưỡng, tia khúc xạ có hướng dọc mặt phân cách.',
  'Lăng kính và sợi quang dẫn sáng nhờ các lần phản xạ thỏa điều kiện. Uốn quá gắt có thể làm tia rò ra.'
 ],display('\\begin{aligned}&n_a>n_b\\\\&\\sin\\theta_c=n_b/n_a\\\\&\\theta_a>\\theta_c.\\end{aligned}')),
 slide('Tán sắc biến ánh sáng trắng thành các hướng màu',[
  'Trong vật liệu, chiết suất có thể phụ thuộc bước sóng chân không.',
  'Ở miền tán sắc chuẩn, tia tím thường có chiết suất lớn hơn tia đỏ.',
  'Qua lăng kính, hai lần khúc xạ tách các màu vì góc lệch phụ thuộc chiết suất.'
 ],display('\\begin{aligned}&n=n(\\lambda_0)\\\\&n_{\\rm tím}>n_{\\rm đỏ}\\\\&v_{\\rm tím}<v_{\\rm đỏ}.\\end{aligned}')),
 slide('Cầu vồng là vành tập trung tia quanh điểm đối nhật',[
  'Cầu vồng bậc một có hai lần khúc xạ và một lần phản xạ nội.',
  'Đỏ ở vòng ngoài khoảng 42,5 độ, tím ở vòng trong khoảng 40,8 độ.',
  'Bậc hai có hai phản xạ nội, mờ hơn và đảo thứ tự màu. Bán kính góc đỏ khoảng 50,1 độ, tím khoảng 53,2 độ.'
 ],display('\\begin{aligned}&\\Delta_1=\\pi+2i-4r\\\\&\\Delta_2=2\\pi+2i-6r\\\\&\\sin i=n\\sin r.\\end{aligned}')),
 slide('Kính phân cực truyền một phép chiếu điện trường',[
  'Phương phân cực được định nghĩa bằng điện trường, vuông góc hướng truyền.',
  'Kính lý tưởng truyền thành phần dọc trục và chặn thành phần vuông góc.',
  'Malus áp dụng cho ánh sáng tới đã phân cực thẳng. Ánh sáng chưa phân cực qua kính đầu còn một nửa cường độ.'
 ],display('\\begin{aligned}&E_{\\rm out}=E_{\\rm in}\\cos\\phi\\\\&I_{\\rm out}=I_{\\rm in}\\cos^2\\phi.\\end{aligned}')),
 slide('Brewster gắn phân cực với hình học phản xạ',[
  'Ở góc Brewster, tia phản xạ và tia khúc xạ vuông góc.',
  'Thành phần p nằm trong mặt phẳng tới không phản xạ. Thành phần s vẫn có thể phản xạ.',
  'Với chùm tự nhiên, ánh sáng phản xạ vì thế phân cực s. Dùng mô hình điện môi trong suốt không từ tính.'
 ],display('\\begin{aligned}&\\tan\\theta_p=n_b/n_a\\\\&\\theta_p+\\theta_b=90^\\circ.\\end{aligned}')),
 slide('Pha tương đối phân biệt thẳng, tròn và elip',[
  'Hai thành phần vuông góc cùng pha hoặc ngược pha tạo phân cực thẳng.',
  'Bằng biên độ và lệch pha một phần tư chu kỳ tạo phân cực tròn.',
  'Các trường hợp không suy biến còn lại tạo elip. Lưỡng chiết làm hai thành phần tích lũy pha khác nhau.'
 ],display('\\begin{aligned}&E_y=A\\cos\\psi\\\\&E_z=B\\cos(\\psi+\\delta)\\\\&|\\delta|=\\pi/2,\\quad A=B.\\end{aligned}')),
 slide('Bản trễ pha cần cả chiều dày và hướng trục',[
  'Hai phương riêng có hai chiết suất, nên độ trễ pha phụ thuộc chiều dày.',
  'Bản phần tư sóng đổi thẳng thành tròn khi hai thành phần tới bằng biên độ.',
  'Quang đàn hồi dùng lưỡng chiết do ứng suất. Kính ba chiều và màn hình tinh thể lỏng điều khiển trạng thái phân cực.'
 ],display('\\begin{aligned}&\\Delta\\phi=\\frac{2\\pi(n_1-n_2)d}{\\lambda_0}\\\\&d_{\\min}=\\frac{\\lambda_0}{4|n_1-n_2|}.\\end{aligned}')),
 slide('Tán xạ làm đổi màu và trạng thái phân cực',[
  'Điện trường tới làm điện tích phân tử dao động rồi bức xạ theo các hướng khác.',
  'Bước sóng ngắn bị tán xạ mạnh hơn trong mô hình Rayleigh. Chùm trực tiếp đi xa vì thế thiên về đỏ.',
  'Ở góc 90 độ, tán xạ một lần lý tưởng có thể phân cực hoàn toàn. Tán xạ nhiều lần trong mây không giữ kết luận đơn giản ấy.'
 ],display('I_{\\rm sc}\\propto1/\\lambda^4.')),
 slide('Huygens dựng mặt sóng trước khi suy đường tia',[
  'Mỗi điểm trên mặt sóng là nguồn sóng thứ cấp. Dùng cùng một khoảng thời gian để dựng mặt mới.',
  'Các bán kính bằng nhau trong cùng môi trường cho góc phản xạ bằng góc tới.',
  'Hai tốc độ khác nhau tại mặt phân cách làm mặt sóng quay, dẫn đến Snell. Biến đổi tốc độ theo độ cao tạo đường tia cong và ảo ảnh.'
 ],display('\\begin{aligned}&r_a=v_at,\\quad r_b=v_bt\\\\&\\frac{\\sin\\theta_a}{\\sin\\theta_b}=\\frac{v_a}{v_b}\\\\&n_a\\sin\\theta_a=n_b\\sin\\theta_b.\\end{aligned}'))
]
export const opticsCheatsheet={title:'Cheatsheet: Bản chất và sự truyền ánh sáng',lead:'Định nghĩa, tính chất và công thức về mặt sóng, phản xạ, khúc xạ, dẫn sáng, tán sắc, phân cực và tán xạ.',sections:[
 {id:'light',title:'Mặt sóng, tia và môi trường',items:[
  {name:'Ánh sáng, mặt sóng và tia',description:'Ánh sáng là sóng điện từ và thể hiện tính chất hạt khi phát xạ, hấp thụ. Mặt sóng gồm các điểm lân cận cùng pha. Trong môi trường đồng nhất, đẳng hướng, tia thẳng và vuông góc mặt sóng.'},
  {name:'Chiết suất, bước sóng và tần số',formula:display('\\begin{aligned}&n=c/v\\\\&\\lambda=\\lambda_0/n\\\\&f=v/\\lambda=c/\\lambda_0.\\end{aligned}'),description:'Tại mặt phân cách đứng yên, tần số giữ nguyên. Tốc độ trong định nghĩa n là tốc độ pha.',variables:['$n$: Chiết suất (không thứ nguyên).','$c,v$: Tốc độ trong chân không và vật liệu ($\\mathrm{m/s}$).','$\\lambda_0,\\lambda$: Bước sóng chân không và trong vật liệu ($\\mathrm m$).','$f$: Tần số ($\\mathrm{Hz}$).']}
 ]},
 {id:'interfaces',title:'Phản xạ và khúc xạ',items:[
  {name:'Định luật phản xạ',formula:display('\\theta_r=\\theta_a.'),description:'Các góc đo với pháp tuyến tại điểm tới. Tia tới, tia phản xạ và pháp tuyến đồng phẳng. Phản xạ gương có hướng xác định trên mặt nhẵn.',variables:['$\\theta_a,\\theta_r$: Góc tới và phản xạ ($\\mathrm{rad}$ hoặc độ).']},
  {name:'Định luật Snell',formula:display('\\begin{aligned}&n_a\\sin\\theta_a=n_b\\sin\\theta_b\\\\&\\frac{\\sin\\theta_a}{\\sin\\theta_b}=\\frac{v_a}{v_b}.\\end{aligned}'),description:'Tia tới, khúc xạ và pháp tuyến cùng nằm trong mặt phẳng tới. Các môi trường trong suốt, đẳng hướng trong mô hình tia.',variables:['$n_a,n_b$: Chiết suất hai môi trường.','$\\theta_b$: Góc khúc xạ đo với pháp tuyến.','$v_a,v_b$: Tốc độ pha ($\\mathrm{m/s}$).']}
 ]},
 {id:'tir',title:'Phản xạ toàn phần',items:[
  {name:'Góc giới hạn',formula:display('\\begin{aligned}&n_a>n_b\\\\&\\sin\\theta_c=n_b/n_a\\\\&\\theta_a>\\theta_c.\\end{aligned}'),description:'Tại ngưỡng θc, tia khúc xạ có hướng tiếp tuyến mặt. Vượt ngưỡng, không có tia khúc xạ chạy trong môi trường thứ hai. Mô hình mặt phân cách không hấp thụ phản xạ toàn bộ công suất pháp tuyến.'},
  {name:'Sợi quang lõi và vỏ',formula:display('\\begin{aligned}&\\sin\\theta_c=n_2/n_1\\\\&\\mathrm{NA}=n_0\\sin\\theta_i\\\\&\\mathrm{NA}=\\sqrt{n_1^2-n_2^2}.\\end{aligned}'),description:'Lõi trụ n1>n2, đầu phẳng vuông góc trục. θi là nửa góc thu nhận của tia trong mặt phẳng chứa trục ở ngưỡng phản xạ.',variables:['$n_0,n_1,n_2$: Chiết suất ngoài, lõi và vỏ.','$\\mathrm{NA}$: Khẩu độ số (không thứ nguyên).']}
 ]},
 {id:'dispersion',title:'Tán sắc và cầu vồng',items:[
  {name:'Tán sắc chuẩn',formula:display('\\begin{aligned}&n=n(\\lambda_0)\\\\&dn/d\\lambda_0<0.\\end{aligned}'),description:'Trong miền tán sắc chuẩn, bước sóng chân không tăng thì chiết suất giảm. Chiết suất phụ thuộc tần số kéo theo tốc độ pha phụ thuộc tần số.'},
  {name:'Góc dừng của tia qua giọt cầu',formula:display('\\begin{aligned}&\\sin i=n\\sin r\\\\&\\Delta_1=\\pi+2i-4r\\\\&\\cos^2i_1=(n^2-1)/3\\\\&\\Delta_2=2\\pi+2i-6r\\\\&\\cos^2i_2=(n^2-1)/8.\\end{aligned}'),description:'Một hoặc hai phản xạ nội, với hai lần khúc xạ. Δ là tổng góc đổi hướng có hướng, tính bằng radian. Bán kính góc quanh điểm đối nhật là π−Δ1 cho bậc một và Δ2−π cho bậc hai.',variables:['$i,r$: Góc tới ngoài và khúc xạ trong nước.','$i_1,i_2$: Góc tới tại đó góc lệch dừng.','$n$: Chiết suất nước, lấy chiết suất không khí bằng 1.']}
 ]},
 {id:'polarizers',title:'Phân cực thẳng và kính phân cực',items:[
  {name:'Phương phân cực',description:'Phương phân cực của sóng điện từ được quy ước bằng phương điện trường. Phân cực thẳng có điện trường dọc một phương ngang cố định. Ánh sáng chưa phân cực không có phương ngang ưu tiên khi lấy trung bình.'},
  {name:'Malus và ánh sáng chưa phân cực',formula:display('\\begin{aligned}&E_{\\rm out}=E_{\\rm in}\\cos\\phi\\\\&I_{\\rm out}=I_{\\rm in}\\cos^2\\phi\\\\&I_{\\rm unpol,out}=I_{\\rm unpol,in}/2.\\end{aligned}'),description:'Hai dòng đầu dùng cho đầu vào phân cực thẳng. Dòng cuối dùng cho đầu vào chưa phân cực. Kính lý tưởng, φ là góc với trục truyền.',variables:['$E$: Biên độ điện trường ($\\mathrm{V/m}$).','$I$: Cường độ ($\\mathrm{W/m^2}$).','$\\phi$: Góc giữa phương phân cực tới và trục kính.']},
  {name:'Chùm phân cực một phần',formula:display('\\begin{aligned}&I(\\alpha)=I_u/2\\\\&\\qquad+I_p\\cos^2(\\alpha-\\theta).\\end{aligned}'),description:'Hai thành phần không kết hợp: Phần chưa phân cực có cường độ Iu, phần phân cực thẳng có cường độ Ip và phương θ. α là góc trục kính cùng hệ quy chiếu góc.'},
  {name:'Góc Brewster',formula:display('\\begin{aligned}&\\tan\\theta_p=n_b/n_a\\\\&\\theta_p+\\theta_b=\\pi/2.\\end{aligned}'),description:'Hai điện môi trong suốt không từ tính có chiết suất khác nhau. Tại θp, thành phần p trong mặt phẳng tới không phản xạ. Ánh sáng tự nhiên phản xạ phân cực s, vuông góc mặt phẳng tới.'}
 ]},
 {id:'phase-polarization',title:'Phân cực tròn, elip và lưỡng chiết',items:[
  {name:'Hai thành phần ngang',formula:display('\\begin{aligned}&E_y=A\\cos\\psi\\\\&E_z=B\\cos(\\psi+\\delta).\\end{aligned}'),description:'A,B khác không. δ là bội nguyên của π cho phân cực thẳng. A=B và δ=±π/2 modulo 2π cho phân cực tròn. Các trường hợp không suy biến còn lại cho elip.',variables:['$A,B$: Biên độ hai thành phần ($\\mathrm{V/m}$).','$\\psi,\\delta$: Pha và độ lệch pha ($\\mathrm{rad}$).']},
  {name:'Độ trễ pha và bản phần tư sóng',formula:display('\\begin{aligned}&\\Delta\\phi=\\frac{2\\pi(n_1-n_2)d}{\\lambda_0}\\\\&d_{\\min}=\\frac{\\lambda_0}{4|n_1-n_2|}.\\end{aligned}'),description:'Hai trục phân cực riêng, bản đồng nhất. dmin cho độ trễ một phần tư chu kỳ. Chuyển phân cực thẳng thành tròn cần hai thành phần tới bằng biên độ, tức phương tới nghiêng 45 độ so với hai trục.',variables:['$n_1,n_2$: Hai chiết suất riêng.','$d$: Chiều dày bản ($\\mathrm m$).']},
  {name:'Tâm sai elip',formula:display('e=\\sqrt{1-b^2/a^2}.'),description:'a≥b>0 là bán trục lớn và nhỏ của quỹ tích điện trường. Trong cùng môi trường, bình phương tỉ số biên độ bằng tỉ số cường độ của hai thành phần theo trục elip.'}
 ]},
 {id:'scattering',title:'Tán xạ ánh sáng',items:[
  {name:'Quy luật Rayleigh',formula:display('\\begin{aligned}&I_{\\rm sc}\\propto\\lambda^{-4}\\\\&\\frac{I_1}{I_2}=\\left(\\frac{\\lambda_2}{\\lambda_1}\\right)^4.\\end{aligned}'),description:'Đối tượng tán xạ nhỏ so với bước sóng. So sánh cùng cường độ tới, số đối tượng và hình học. Trong tán xạ một lần lý tưởng ở góc 90 độ, chùm tới chưa phân cực tạo ánh sáng tán xạ phân cực thẳng.'}
 ]},
 {id:'huygens',title:'Nguyên lý Huygens',items:[
  {name:'Sóng thứ cấp và mặt sóng mới',formula:display('\\begin{aligned}&r=vt\\\\&\\frac{\\sin\\theta_a}{\\sin\\theta_b}=\\frac{v_a}{v_b}\\\\&n_a\\sin\\theta_a=n_b\\sin\\theta_b.\\end{aligned}'),description:'Mỗi điểm mặt sóng là nguồn sóng thứ cấp. Bao tiếp tuyến theo chiều truyền tại cùng thời gian tạo mặt sóng mới. Trong môi trường đồng nhất, sóng thứ cấp có bán kính vt.',variables:['$r$: Bán kính sóng thứ cấp ($\\mathrm m$).','$t$: Khoảng thời gian dựng mặt sóng mới ($\\mathrm s$).']}
 ]}
]}
