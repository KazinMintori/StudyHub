const note='14-quang-hinh-hoc'
const display=s=>'$$\n'+s+'\n$$'
const slide=(title,bullets,formula)=>({note,title,bullets,formula:display(formula)})
export const geometricOpticsTopics=[{title:'Tạo ảnh và dụng cụ quang học',topics:[
 {slug:'guong-phang',title:'Vật, ảnh và gương phẳng',question:'Ảnh nằm ở đâu khi các tia phản xạ chỉ có vẻ xuất phát từ một điểm?',source:'34.1'},
 {slug:'guong-cau',title:'Gương cầu và phép dựng ảnh',question:'Độ cong của gương quyết định vị trí, chiều và kích thước ảnh như thế nào?',source:'34.2'},
 {slug:'khuc-xa-mat-cau',title:'Khúc xạ tại mặt cầu và độ sâu biểu kiến',question:'Vì sao một mặt khúc xạ có thể hội tụ tia hoặc làm vật có vẻ ở gần hơn?',source:'34.3'},
 {slug:'thau-kinh-mong',title:'Thấu kính mỏng và hệ nhiều kính',question:'Hai mặt khúc xạ phối hợp tạo ảnh ra sao, và khi nào ảnh trước trở thành vật ảo?',source:'34.4'},
 {slug:'may-anh',title:'Máy ảnh, khẩu độ và ống kính zoom',question:'Tiêu cự, khẩu độ và màn trập điều khiển khung hình cùng độ phơi sáng như thế nào?',source:'34.5'},
 {slug:'mat',title:'Mắt, điều tiết và kính hiệu chỉnh',question:'Vì sao ảnh phải nằm trên võng mạc và kính bổ trợ tạo ảnh ở đâu?',source:'34.6'},
 {slug:'kinh-lup',title:'Kính lúp và bội giác góc',question:'Ảnh ở vô cực vẫn có góc trông hữu hạn như thế nào?',source:'34.7'},
 {slug:'kinh-hien-vi-thien-van',title:'Kính hiển vi và kính thiên văn',question:'Vì sao vật kính hiển vi cần tiêu cự ngắn, còn vật kính thiên văn cần tiêu cự dài?',source:'34.8'}
]}]
export const geometricOpticsSlides=[
 slide('Ảnh thật và ảnh ảo được phân biệt bằng đường tia',[
  'Ảnh thật là nơi các tia đi ra hội tụ. Ảnh ảo là giao điểm của các đường kéo dài ngược chiều.',
  'Khoảng vật dương ở phía ánh sáng tới, khoảng ảnh dương ở phía ánh sáng ra.',
  'Gương phẳng tạo ảnh ảo đối xứng qua mặt gương của một vật thật.'
 ],String.raw`\begin{aligned}s^\prime&=-s\\m&=y^\prime/y=1.\end{aligned}`),
 slide('Gần đúng cận trục cho một ảnh điểm xác định',[
  'Các tia gần trục tạo góc nhỏ. Có thể thay sin và tan bằng góc tính bằng radian.',
  'Các tia biên của gương cầu không cùng hội tụ với tia cận trục, gây quang sai cầu.',
  'Gương parabol hội tụ chính xác chùm song song trục tại một tiêu điểm.'
 ],String.raw`\sin\theta\approx\tan\theta\approx\theta.`),
 slide('Gương cầu dùng bán kính và tiêu cự có dấu',[
  'Gương lõm có tiêu cự dương, còn gương lồi có tiêu cự âm.',
  'Vật thật trong tiêu cự gương lõm tạo ảnh ảo phóng đại cùng chiều.',
  'Gương lồi tạo ảnh ảo cùng chiều và thu nhỏ của vật thật.'
 ],String.raw`\begin{aligned}f&=R/2\\\frac1s+\frac1{s^\prime}&=\frac1f\\m&=-s^\prime/s.\end{aligned}`),
 slide('Mặt khúc xạ phụ thuộc độ chênh chiết suất',[
  'Tâm cong ở phía ánh sáng đi ra cho bán kính dương.',
  'Khoảng ảnh dương biểu thị hội tụ thật trong môi trường sau mặt phân cách.',
  'Mặt phẳng là giới hạn bán kính vô cực và giữ nguyên kích thước ngang của ảnh cận trục.'
 ],String.raw`\begin{aligned}\frac{n_a}s+\frac{n_b}{s^\prime}&=\frac{n_b-n_a}R\\m&=-\frac{n_as^\prime}{n_bs}.\end{aligned}`),
 slide('Hai mặt thấu kính phối hợp thành một tiêu cự',[
  'Kính mỏng cho phép bỏ qua bề dày so với khoảng vật và ảnh.',
  'Kính trong không khí có tiêu cự xác định bởi chiết suất và hai bán kính có dấu.',
  'Hai tiêu cự ở hai phía bằng nhau khi hai môi trường ngoài giống nhau.'
 ],String.raw`\begin{aligned}&\frac1f=(n-1)\\&\quad\times\left(\frac1{R_1}-\frac1{R_2}\right)\\&\frac1s+\frac1{s^\prime}=\frac1f.\end{aligned}`),
 slide('Hệ nhiều phần tử cần đổi mốc ở từng bước',[
  'Tìm ảnh của phần tử đầu trước khi xét phần tử sau.',
  'Ảnh dự kiến nằm sau kính thứ hai là vật ảo của kính đó.',
  'Phóng đại toàn hệ là tích các phóng đại có dấu, nên hai lần đảo chiều có thể cho ảnh cuối cùng chiều.'
 ],String.raw`\begin{aligned}s_2&=d-s^\prime_1\\m&=m_1m_2.\end{aligned}`),
 slide('Tiêu cự máy ảnh quyết định kích thước ảnh và góc trông',[
  'Tiêu cự dài cho ảnh lớn và góc trông hẹp trên cùng bề mặt ghi nhận.',
  'Vật ở gần hơn cần khoảng kính–cảm biến lớn hơn để ảnh nét.',
  'Ống kính zoom thay đổi tiêu cự bằng chuyển động tương đối của các nhóm kính.'
 ],String.raw`\begin{aligned}s^\prime&=\frac{fs}{s-f}\\m&=-s^\prime/s.\end{aligned}`),
 slide('Chỉ số f nối khẩu độ với độ phơi sáng',[
  'Chỉ số f bằng tiêu cự chia đường kính khẩu độ.',
  'Cùng cảnh và điều kiện quang học, cường độ ảnh tỉ lệ nghịch bình phương chỉ số f.',
  'Mỗi nấc khẩu danh định đổi cường độ khoảng hai lần. Giữ độ phơi sáng cần bù bằng thời gian.'
 ],String.raw`\begin{aligned}N&=f/D\\I&\propto1/N^2\\H&\propto\Delta t/N^2.\end{aligned}`),
 slide('Mắt điều tiết tiêu cự để giữ ảnh trên võng mạc',[
  'Giác mạc gây phần lớn khúc xạ vì độ chênh chiết suất với không khí lớn.',
  'Cơ thể mi co làm thể thủy tinh cong hơn, giảm tiêu cự khi nhìn gần.',
  'Kính phân kỳ hiệu chỉnh nhìn xa của mắt cận, kính hội tụ hỗ trợ nhìn gần khi cần ảnh ảo xa hơn.'
 ],String.raw`P=1/f.`),
 slide('Bội giác góc khác độ phóng đại ngang',[
  'Kích thước góc quyết định kích thước ảnh trên võng mạc.',
  'Kính lúp cho vật ở tiêu điểm để ảnh ở vô cực và mắt không cần điều tiết.',
  'So với nhìn trực tiếp ở khoảng quy ước 25cm, bội giác tăng khi tiêu cự kính lúp giảm.'
 ],String.raw`\begin{aligned}M&=\theta^\prime/\theta\\M&=\frac{25\,\mathrm{cm}}f.\end{aligned}`),
 slide('Kính hiển vi phóng đại qua hai giai đoạn',[
  'Vật kính tiêu cự ngắn tạo ảnh thật phóng đại và ngược chiều.',
  'Thị kính dùng ảnh trung gian làm vật cho kính lúp. Ảnh cuối vẫn ngược chiều vật đầu.',
  'Công thức gần đúng dùng vật gần tiêu điểm vật kính và ảnh cuối ở vô cực.'
 ],String.raw`|M|\approx\frac{(25\,\mathrm{cm})s^\prime_1}{f_1f_2}.`),
 slide('Kính thiên văn tăng góc trông của vật rất xa',[
  'Vật kính tạo ảnh thật thu nhỏ của thiên thể, rồi thị kính phóng đại góc của ảnh đó.',
  'Hai kính hội tụ ngắm chừng ở vô cực cách nhau tổng hai tiêu cự.',
  'Gương lõm làm vật kính tránh quang sai sắc. Các gương phụ đưa ảnh tới thiết bị quan sát hoặc cảm biến.'
 ],String.raw`\begin{aligned}M&=-f_1/f_2\\L&=f_1+f_2.\end{aligned}`)
]
export const geometricOpticsCheatsheet={title:'Cheatsheet: Quang hình học',lead:'Định nghĩa, tính chất, công thức, điều kiện áp dụng và ký hiệu của hệ tạo ảnh cùng dụng cụ quang học.',sections:[
 {id:'signs',title:'Vật, ảnh và dấu',items:[
  {name:'Ảnh thật, ảnh ảo',description:'Ảnh thật là giao điểm của các tia đi ra. Ảnh ảo là giao điểm của các đường kéo dài ngược chiều các tia đi ra.'},
  {name:'Quy ước dấu',description:'s dương ở phía ánh sáng tới. s′ dương ở phía ánh sáng ra. R dương khi tâm cong ở phía ánh sáng ra. m dương cho ảnh cùng chiều, âm cho ảnh ngược chiều.',variables:[String.raw`$s,s^\prime,R,f$: Các khoảng có dấu, cùng đơn vị độ dài.`,String.raw`$y,y^\prime$: Chiều cao có dấu.`,'$m$: Phóng đại ngang, không thứ nguyên.']},
  {name:'Gần đúng cận trục',formula:display(String.raw`\sin\theta\approx\tan\theta\approx\theta.`),description:'Tia gần trục và góc nhỏ, với θ tính bằng radian. Quang sai cầu là sự không đồng nhất vị trí hội tụ của các tia ngoài miền cận trục.'}
 ]},
 {id:'mirrors',title:'Gương phẳng và gương cầu',items:[
  {name:'Gương phẳng',formula:display(String.raw`\begin{aligned}s^\prime&=-s\\m&=1.\end{aligned}`),description:'Vật thật cho ảnh ảo cùng chiều, cùng kích thước, đối xứng qua mặt gương.'},
  {name:'Gương cầu',formula:display(String.raw`\begin{aligned}f&=R/2\\\frac1s+\frac1{s^\prime}&=\frac1f\\m&=-s^\prime/s.\end{aligned}`),description:'Gần đúng cận trục. Gương lõm có R và f dương, gương lồi có R và f âm.'}
 ]},
 {id:'refraction',title:'Một mặt khúc xạ',items:[
  {name:'Mặt cầu khúc xạ',formula:display(String.raw`\begin{aligned}\frac{n_a}s+\frac{n_b}{s^\prime}&=\frac{n_b-n_a}R\\m&=-\frac{n_as^\prime}{n_bs}.\end{aligned}`),description:'Tia cận trục truyền từ môi trường a sang b.',variables:['$n_a,n_b$: Chiết suất trước và sau mặt, không thứ nguyên.']},
  {name:'Mặt phẳng khúc xạ',formula:display(String.raw`\begin{aligned}s^\prime&=-\frac{n_b}{n_a}s\\m&=1.\end{aligned}`),description:'Giới hạn R vô cực. Với vật thật, ảnh ảo cùng chiều và giữ nguyên kích thước ngang trong gần đúng cận trục.'}
 ]},
 {id:'lenses',title:'Thấu kính mỏng',items:[
  {name:'Tạo ảnh qua kính mỏng',formula:display(String.raw`\begin{aligned}\frac1s+\frac1{s^\prime}&=\frac1f\\m&=-s^\prime/s.\end{aligned}`),description:'Hai môi trường ngoài giống nhau, bề dày kính được bỏ qua. Kính hội tụ có f dương, kính phân kỳ có f âm.'},
  {name:'Công thức chế tạo trong không khí',formula:display(String.raw`\frac1f=(n-1)\left(\frac1{R_1}-\frac1{R_2}\right).`),description:'R1 và R2 có dấu theo chiều truyền. n là chiết suất kính, không thứ nguyên.'},
  {name:'Công thức chế tạo trong môi trường',formula:display(String.raw`\begin{aligned}\frac1f&=\left(\frac{n_g}{n_l}-1\right)\\&\quad\times\left(\frac1{R_1}-\frac1{R_2}\right).\end{aligned}`),description:'Kính chiết suất ng ngập hoàn toàn trong môi trường đồng nhất chiết suất nl ở cả hai phía.'}
 ]},
 {id:'systems',title:'Hệ hai phần tử',items:[
  {name:'Hai thấu kính cách nhau',formula:display(String.raw`\begin{aligned}s_2&=d-s^\prime_1\\m&=m_1m_2.\end{aligned}`),description:'Hai kính đồng trục, ánh sáng truyền cùng chiều qua cả hai. d là khoảng hai kính. Mỗi khoảng vật, ảnh đo từ kính tương ứng.'},
  {name:'Hai kính mỏng sát nhau',formula:display(String.raw`\frac1f=\frac1{f_1}+\frac1{f_2}.`),description:'Bỏ qua bề dày và khoảng cách hai kính. Dùng tiêu cự có dấu và cùng đơn vị.'}
 ]},
 {id:'camera',title:'Máy ảnh',items:[
  {name:'Chỉ số f và độ phơi sáng',formula:display(String.raw`\begin{aligned}N&=f/D\\I&\propto1/N^2\\H&\propto\Delta t/N^2.\end{aligned}`),description:'Cùng cảnh và điều kiện truyền sáng, trong mô hình tạo ảnh đang xét.',variables:['$N$: Chỉ số f, không thứ nguyên.','$D$: Đường kính khẩu độ, cùng đơn vị với f.',String.raw`$I$: Cường độ tại ảnh ($\mathrm{W/m^2}$).`,String.raw`$H$: Năng lượng tới trên đơn vị diện tích ($\mathrm{J/m^2}$).`,String.raw`$\Delta t$: Thời gian phơi sáng ($\mathrm s$).`]}
 ]},
 {id:'eye',title:'Mắt và kính hiệu chỉnh',items:[
  {name:'Điều tiết và các điểm giới hạn',description:'Điều tiết là đổi hình dạng, tiêu cự thể thủy tinh để ảnh vẫn nằm trên võng mạc. Cực cận và cực viễn là điểm gần nhất, xa nhất nhìn rõ. Mắt bình thường có cực viễn ở vô cực.'},
  {name:'Độ tụ',formula:display(String.raw`\begin{aligned}P&=1/f\\1\,\mathrm D&=1\,\mathrm{m^{-1}}.\end{aligned}`),description:'f phải tính bằng mét. P dương cho kính hội tụ, âm cho kính phân kỳ.'},
  {name:'Hiệu chỉnh trong mô hình quang học',description:'Cận thị nhìn xa cần kính phân kỳ tạo ảnh ảo ở cực viễn. Viễn thị hoặc lão thị nhìn gần dùng kính hội tụ tạo ảnh ảo tại hoặc xa hơn cực cận. Loạn thị có độ tụ khác nhau theo các phương và dùng kính có mặt trụ thích hợp.'}
 ]},
 {id:'magnifier',title:'Kính lúp',items:[
  {name:'Bội giác góc',formula:display(String.raw`\begin{aligned}M&=\theta^\prime/\theta\\M&=\frac{25\,\mathrm{cm}}f.\end{aligned}`),description:'Dòng hai dùng góc nhỏ, vật ở tiêu điểm và ảnh ở vô cực. Góc tham chiếu là góc của vật nhìn bằng mắt trần từ25cm.',variables:['$M$: Bội giác góc, không thứ nguyên.',String.raw`$\theta,\theta^\prime$: Góc nhìn trực tiếp và qua dụng cụ, cùng đơn vị.`]}
 ]},
 {id:'microscope',title:'Kính hiển vi',items:[
  {name:'Vật kính và toàn hệ',formula:display(String.raw`\begin{aligned}m_1&=-s^\prime_1/s_1\\|M|&\approx\frac{(25\,\mathrm{cm})s^\prime_1}{f_1f_2}.\end{aligned}`),description:'Gần đúng s1≈f1 và ảnh cuối ở vô cực. f1,f2 là tiêu cự vật kính, thị kính. s′1 là khoảng ảnh vật kính. Các độ dài cùng đơn vị với25cm. Ảnh cuối ngược chiều.'}
 ]},
 {id:'telescope',title:'Kính thiên văn',items:[
  {name:'Hệ hai kính hội tụ',formula:display(String.raw`\begin{aligned}M&=-f_1/f_2\\L&=f_1+f_2.\end{aligned}`),description:'Vật và ảnh cuối ở vô cực. f1 là tiêu cự vật kính, f2 là tiêu cự thị kính, L là khoảng hai kính. Dấu âm biểu thị ảnh ngược chiều.'},
  {name:'Kính Galilei',formula:display(String.raw`\begin{aligned}f_1&>0,\quad f_2<0\\M&=-f_1/f_2>0\\L&=f_1-|f_2|.\end{aligned}`),description:'Thị kính phân kỳ, ngắm chừng ở vô cực. Ảnh cuối cùng chiều. Điều kiện chiều dài dương đòi hỏi f1>|f2|.'}
 ]}
]}
