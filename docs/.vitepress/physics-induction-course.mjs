const note='09-cam-ung-dien-tu'
const display=s=>`$$\n${s}\n$$`
export const inductionTopics=[{title:'Cảm ứng, trường biến thiên và vật liệu siêu dẫn',topics:[
 {slug:'thi-nghiem-cam-ung',title:'Thí nghiệm cảm ứng',question:'Những thay đổi nào làm cuộn dây xuất hiện dòng điện?',source:'29.1'},
 {slug:'dinh-luat-faraday',title:'Định luật Faraday',question:'Tốc độ biến thiên từ thông quyết định suất điện động ra sao?',source:'29.2'},
 {slug:'dinh-luat-lenz',title:'Định luật Lenz',question:'Dòng cảm ứng chống lại sự thay đổi nào?',source:'29.3'},
 {slug:'suat-dien-dong-chuyen-dong',title:'Suất điện động do chuyển động',question:'Lực từ phân bố lại điện tích trong vật dẫn chuyển động thế nào?',source:'29.4'},
 {slug:'dien-truong-cam-ung',title:'Điện trường cảm ứng',question:'Điều gì đẩy điện tích trong vòng dây đứng yên khi từ thông biến thiên?',source:'29.5'},
 {slug:'dong-dien-foucault',title:'Dòng điện Fu-cô',question:'Dòng điện khép kín trong khối kim loại tạo lực hãm và nhiệt thế nào?',source:'29.6'},
 {slug:'dong-dien-dich-maxwell',title:'Dòng điện dịch và phương trình Maxwell',question:'Điện trường biến thiên bổ sung nguồn từ trường như thế nào?',source:'29.7'},
 {slug:'sieu-dan',title:'Siêu dẫn',question:'Trạng thái không điện trở còn có những tính chất từ nào?',source:'29.8'}
]}]
export const inductionSlides=[
 {note,title:'Biến thiên từ thông là điều kiện gây cảm ứng',bullets:['Nam châm đứng yên gần cuộn dây không gây dòng cảm ứng ổn định.','Chuyển động tương đối, biến đổi dòng nguồn hoặc đổi hình dạng cuộn đều có thể làm từ thông biến thiên.','Suất điện động phụ thuộc tốc độ thay đổi, không phụ thuộc riêng giá trị từ thông.'],formula:display(String.raw`\Phi_B=\int_S\vec B\cdot d\vec A`)},
 {note,title:'Faraday gắn suất điện động với đạo hàm từ thông',bullets:['Chiều dương quanh vòng được gắn với pháp tuyến bằng quy tắc bàn tay phải.','N vòng nối tiếp có cùng từ thông cho suất điện động gấp N lần.','Mạch hở có thể có suất điện động dù không có dòng vòng.'],formula:display(String.raw`\mathcal E=-N\frac{d\Phi_B}{dt}`)},
 {note,title:'Dấu của Faraday phải đi cùng pháp tuyến đã chọn',bullets:['Từ thông dương tăng cho suất điện động âm.','Từ thông dương giảm cho suất điện động dương.','Chỉ sau khi chọn pháp tuyến mới đổi dấu thành chiều chạy quanh vòng.'],formula:display(String.raw`\Phi_B=BA\cos\phi`)},
 {note,title:'Cuộn quay tạo suất điện động hình sin',bullets:['Pháp tuyến quay đều làm góc với trường thay đổi tuyến tính theo thời gian.','Suất điện động cực đại khi từ thông đi qua không.','Cổ góp đổi nối điện mỗi nửa vòng để đầu ra giữ cùng dấu.'],formula:display(String.raw`\begin{aligned}&\Phi_B=BA\cos\omega t\\&\mathcal E=N\omega BA\sin\omega t.\end{aligned}`)},
 {note,title:'Lenz chống biến thiên từ thông',bullets:['Trường ngoài tăng thì dòng cảm ứng tạo trường ngược chiều trong vùng xét.','Trường ngoài giảm thì dòng cảm ứng có thể tạo trường cùng chiều.','Lực từ cản chuyển động sinh dòng, phù hợp bảo toàn năng lượng.'],formula:''},
 {note,title:'Thanh chuyển động tách điện tích bằng lực từ',bullets:['Điện tích dương chịu lực theo tích có hướng của vận tốc với từ trường.','Trong thanh cô lập, điện trường tăng đến khi cân bằng lực từ.','Công thức tích vBL cần thanh, vận tốc và trường vuông góc từng đôi.'],formula:display(String.raw`\begin{aligned}&\vec E=-\vec v\times\vec B\\&|\mathcal E|=vBL.\end{aligned}`)},
 {note,title:'Suất điện động chuyển động cần tích phân theo từng phần tử',bullets:['Vận tốc và trường được lấy tại mỗi phần tử của vật dẫn.','Biểu thức này mô tả phần suất điện động do vật dẫn chuyển động.','Dây đứng yên trong từ trường biến thiên cần xét điện trường cảm ứng.'],formula:display(String.raw`\mathcal E=\oint(\vec v\times\vec B)\cdot d\vec\ell`)},
 {note,title:'Điện trường cảm ứng có tuần hoàn khác không',bullets:['Đường tích phân được giữ cố định trong dạng Faraday cho điện trường.','Điện trường này không bảo toàn và tồn tại cả khi không có dây dẫn.','Đối xứng trụ làm điện trường tiếp tuyến với các đường tròn đồng tâm.'],formula:display(String.raw`\oint\vec E\cdot d\vec\ell=-\frac{d\Phi_B}{dt}`)},
 {note,title:'Dòng Fu-cô có thể hãm, nung nóng và tạo tín hiệu dò',bullets:['Các đường dòng khép kín trong chính khối vật dẫn.','Lực hãm chuyển cơ năng thành nhiệt.','Dòng Fu-cô trong lõi biến áp gây tổn hao cần giảm bằng cấu tạo lõi.'],formula:''},
 {note,title:'Dòng điện dịch làm Ampere nhất quán khi nạp tụ',bullets:['Hai mặt cùng đường biên phải cho cùng tích phân từ trường.','Dòng dẫn trong dây bằng dòng dịch tổng trong khe của tụ lý tưởng đang nạp.','Dòng dịch không đồng nhất với dòng dẫn xuyên điện môi.'],formula:display(String.raw`\begin{aligned}&i_D=\varepsilon\frac{d\Phi_E}{dt}\\&\oint\vec B\cdot d\vec\ell\\&\quad=\mu_0(i_C+i_D)_{\mathrm{encl}}.\end{aligned}`)},
 {note,title:'Maxwell liên hệ điện trường, từ trường và nguồn',bullets:['Hai định luật Gauss liên hệ thông lượng qua mặt kín với các nguồn.','Faraday và Ampere–Maxwell liên hệ tuần hoàn với các trường biến thiên.','Kết hợp lực Lorentz cho biết tác dụng của trường lên điện tích.'],formula:display(String.raw`\vec F=q(\vec E+\vec v\times\vec B)`)},
 {note,title:'Siêu dẫn bao gồm cả điện trở bằng không và hiệu ứng Meissner',bullets:['Chuyển pha cần nhiệt độ và trường ngoài phù hợp.','Meissner đẩy từ thông khỏi khối vật liệu trong trạng thái được xét.','Loại II có hai trường tới hạn, với miền hỗn hợp giữa hai ngưỡng.'],formula:display(String.raw`B_{c1}<B_0<B_{c2}`)}
]
export const inductionCheatsheet={
 summary:'Định nghĩa, tính chất, công thức và điều kiện của cảm ứng điện từ, các phương trình Maxwell và siêu dẫn.',
 sections:[
 {id:'flux-faraday',title:'Từ thông và Faraday',items:[
  {name:'Từ thông',formula:display(String.raw`\begin{aligned}&\Phi_B=\int_S\vec B\cdot d\vec A\\&\Phi_B=BA\cos\phi.\end{aligned}`),description:'Dạng thứ hai cần trường đều trên mặt phẳng. Góc φ đo giữa trường và pháp tuyến.',variables:[String.raw`$\Phi_B$: Từ thông ($\mathrm{Wb}$).`,String.raw`$\vec B$: Cảm ứng từ ($\mathrm T$).`,String.raw`$A$: Diện tích ($\mathrm{m^2}$).`,String.raw`$\phi$: Góc với pháp tuyến ($\mathrm{rad}$).`]},
  {name:'Định luật Faraday',formula:display(String.raw`\begin{aligned}&\mathcal E=-\frac{d\Phi_B}{dt}\\&\mathcal E_N=-N\frac{d\Phi_B}{dt}.\end{aligned}`),description:'N vòng nối tiếp có cùng từ thông. Chiều dương và pháp tuyến tuân theo quy tắc bàn tay phải.',variables:[String.raw`$\mathcal E$: Suất điện động ($\mathrm V$).`,String.raw`$t$: Thời gian ($\mathrm s$).`,String.raw`$N$: Số vòng (Không có đơn vị).`]},
  {name:'Giá trị trung bình và điện tích qua mạch',formula:display(String.raw`\begin{aligned}&\mathcal E_{\mathrm{av}}=-N\frac{\Delta\Phi_B}{\Delta t}\\&Q=-\frac{N\Delta\Phi_B}{R}.\end{aligned}`),description:'Điện tích đại số qua tiết diện với điện trở không đổi, bỏ qua tự cảm và các nguồn khác.',variables:[String.raw`$Q$: Điện tích đi qua ($\mathrm C$).`,String.raw`$R$: Điện trở toàn mạch ($\Omega$).`]}
 ]},
 {id:'lenz',title:'Định luật Lenz',items:[
  {name:'Chiều cảm ứng',description:'Hiệu ứng cảm ứng chống biến đổi đã gây ra nó. Trường cảm ứng chống biến thiên từ thông, không nhất thiết chống từ trường ngoài.'},
  {name:'Dòng trong mạch điện trở',formula:display(String.raw`I=\frac{\mathcal E}{R}`),description:'Dòng có dấu theo chiều đã chọn. Mạch hở có thể có suất điện động mà không có dòng vòng.',variables:[String.raw`$I$: Dòng điện ($\mathrm A$).`,String.raw`$\mathcal E$: Suất điện động ($\mathrm V$).`,String.raw`$R$: Điện trở ($\Omega$).`]}
 ]},
 {id:'generators',title:'Cuộn quay và máy phát',items:[
  {name:'Cuộn quay đều',formula:display(String.raw`\begin{aligned}&\Phi_B=BA\cos\omega t\\&\mathcal E=N\omega BA\sin\omega t\\&\mathcal E_0=N\omega BA\\&f=\frac\omega{2\pi}.\end{aligned}`),description:'Trục quay vuông góc trường đều và pháp tuyến song song trường tại t = 0.',variables:[String.raw`$\omega$: Tốc độ góc ($\mathrm{rad/s}$).`,String.raw`$f$: Tần số ($\mathrm{Hz}$).`,String.raw`$\mathcal E_0$: Biên độ suất điện động ($\mathrm V$).`]},
  {name:'Suất điện động chỉnh lưu trung bình',formula:display(String.raw`\mathcal E_{\mathrm{av}}=\frac{2N\omega BA}{\pi}`),description:'Giá trị trung bình của sóng sin được đổi dấu âm thành dương nhờ cổ góp lý tưởng.'}
 ]},
 {id:'motional',title:'Suất điện động do chuyển động',items:[
  {name:'Thanh dẫn cô lập',formula:display(String.raw`\begin{aligned}&\vec E=-\vec v\times\vec B\\&|\Delta V|=vBL.\end{aligned}`),description:'Dạng tích vBL cần ba phương vuông góc từng đôi. Điện trường cân bằng được xét sau khi điện tích đã phân bố lại.',variables:[String.raw`$\vec E$: Điện trường ($\mathrm{V/m}$).`,String.raw`$\vec v$: Vận tốc thanh ($\mathrm{m/s}$).`,String.raw`$L$: Chiều dài thanh ($\mathrm m$).`,String.raw`$\Delta V$: Hiệu điện thế hai đầu ($\mathrm V$).`]},
  {name:'Biểu thức tích phân chuyển động',formula:display(String.raw`\mathcal E=\oint(\vec v\times\vec B)\cdot d\vec\ell`),description:'Vận tốc là vận tốc từng phần tử vật dẫn. Biểu thức chỉ tính phần suất điện động do chuyển động trong trường.',variables:[String.raw`$d\vec\ell$: Vector phần tử dây theo chiều tích phân ($\mathrm m$).`]},
  {name:'Thanh quay và đĩa Faraday',formula:display(String.raw`|\mathcal E|=\frac12\omega BR^2`),description:'Tích phân theo bán kính từ trục đến R, với trường đều vuông góc mặt quay.',variables:[String.raw`$R$: Bán kính đĩa hoặc chiều dài thanh quay quanh đầu ($\mathrm m$).`]},
  {name:'Lực cản và công suất thanh trượt',formula:display(String.raw`\begin{aligned}&I=\frac{BLv}{R}\\&F_B=\frac{B^2L^2v}{R}\\&P=F_Bv=I^2R.\end{aligned}`),description:'Mạch điện trở kín, chuyển động vuông góc trường đều, bỏ qua ma sát và tự cảm.',variables:[String.raw`$F_B$: Lực cản từ ($\mathrm N$).`,String.raw`$P$: Công suất ($\mathrm W$).`]}
 ]},
 {id:'induced-electric',title:'Điện trường cảm ứng',items:[
  {name:'Faraday cho đường đứng yên',formula:display(String.raw`\oint\vec E\cdot d\vec\ell=-\frac{d\Phi_B}{dt}`),description:'Điện trường cảm ứng không bảo toàn, không mô tả chỉ bằng thế điện vô hướng và tồn tại cả khi không có vật dẫn.'},
  {name:'Đối xứng tròn',formula:display(String.raw`E=\frac1{2\pi r}\left|\frac{d\Phi_B}{dt}\right|`),description:'Điện trường tiếp tuyến và có cùng độ lớn trên đường tròn. Từ thông dùng đúng vùng có từ trường.',variables:[String.raw`$r$: Bán kính đường tích phân ($\mathrm m$).`]},
  {name:'Quanh ống dây dài',formula:display(String.raw`\begin{aligned}&E_{\mathrm{trong}}=\frac r2\left|\frac{dB}{dt}\right|\\&E_{\mathrm{ngoài}}=\frac{a^2}{2r}\left|\frac{dB}{dt}\right|.\end{aligned}`),description:'Ống bán kính a, trường trong gần đều và trường ngoài được bỏ qua. Dùng dòng trên đường tròn đồng tâm ở xa hai đầu.',variables:[String.raw`$a$: Bán kính ống dây ($\mathrm m$).`]}
 ]},
 {id:'eddy',title:'Dòng điện Fu-cô',items:[
  {name:'Dòng khép kín trong vật dẫn',description:'Dòng cảm ứng tuần hoàn trong khối vật dẫn khi từ thông biến thiên. Lực từ chống chuyển động gây cảm ứng. Tổn hao nhiệt có công suất I²R.'}
 ]},
 {id:'displacement-maxwell',title:'Dòng điện dịch và Maxwell',items:[
  {name:'Dòng điện dịch',formula:display(String.raw`\begin{aligned}&i_D=\varepsilon\frac{d\Phi_E}{dt}\\&j_D=\varepsilon\frac{dE}{dt}.\end{aligned}`),description:'Dạng mật độ dùng điện trường đều, cùng phương. Điện thẩm không đổi trong mô hình tuyến tính.',variables:[String.raw`$i_D$: Dòng dịch ($\mathrm A$).`,String.raw`$j_D$: Mật độ dòng dịch ($\mathrm{A/m^2}$).`,String.raw`$\varepsilon$: Điện thẩm ($\mathrm{F/m}$).`,String.raw`$\Phi_E$: Thông lượng điện ($\mathrm{V\,m}$).`]},
  {name:'Gauss cho điện trường',formula:display(String.raw`\oint\vec E\cdot d\vec A=\frac{Q_{\mathrm{encl}}}{\varepsilon_0}`),description:'Mặt tích phân kín, dạng chân không. Điện tích bao gồm toàn bộ điện tích bên trong mặt.',variables:[String.raw`$Q_{\mathrm{encl}}$: Điện tích được bao ($\mathrm C$).`,String.raw`$\varepsilon_0$: Điện thẩm chân không ($\mathrm{F/m}$).`]},
  {name:'Gauss cho từ trường',formula:display(String.raw`\oint\vec B\cdot d\vec A=0`),description:'Thông lượng từ qua mọi mặt kín bằng không trong điện từ học không có đơn cực từ.'},
  {name:'Faraday',formula:display(String.raw`\oint\vec E\cdot d\vec\ell=-\frac{d\Phi_B}{dt}`),description:'Đường tích phân đứng yên, thông lượng qua mặt có đường biên là đường ấy.'},
  {name:'Ampere–Maxwell',formula:display(String.raw`\begin{aligned}&\oint\vec B\cdot d\vec\ell\\&\quad=\mu_0(i_C)_{\mathrm{encl}}\\&\quad+\mu_0\varepsilon_0\frac{d\Phi_E}{dt}.\end{aligned}`),description:'Dạng chân không với đường tích phân cố định. Dòng dẫn và thông lượng điện được tính trên cùng mặt.',variables:[String.raw`$i_C$: Dòng dẫn ($\mathrm A$).`,String.raw`$\mu_0$: Độ từ thẩm chân không ($\mathrm{T\,m/A}$).`]},
  {name:'Lực Lorentz',formula:display(String.raw`\vec F=q(\vec E+\vec v\times\vec B)`),description:'Lực điện từ lên điện tích điểm đang chuyển động.',variables:[String.raw`$\vec F$: Lực ($\mathrm N$).`,String.raw`$q$: Điện tích có dấu ($\mathrm C$).`]}
 ]},
 {id:'superconductivity',title:'Siêu dẫn',items:[
  {name:'Pha siêu dẫn và Meissner',formula:display(String.raw`\begin{aligned}&R=0\\&\vec B_{\mathrm{khối}}=0.\end{aligned}`),description:'Điện trở bằng không và từ thông bị đẩy khỏi khối trong trạng thái Meissner, ngoài tầng bề mặt mỏng. Cần nhiệt độ và trường ngoài dưới các ngưỡng phù hợp.'},
  {name:'Hai ngưỡng của siêu dẫn loại II',formula:display(String.raw`B_{c1}<B_0<B_{c2}`),description:'Miền hỗn hợp có các sợi chứa từ thông giữa phần vật liệu còn siêu dẫn. Trên Bc2, vật liệu chuyển sang pha thường.',variables:[String.raw`$B_0$: Trường ngoài ($\mathrm T$).`,String.raw`$B_{c1},B_{c2}$: Hai trường tới hạn ($\mathrm T$).`,String.raw`$T_c$: Nhiệt độ tới hạn ($\mathrm K$).`]}
 ]}
 ]
}
