const note='05-dong-dien-dien-tro'
const d=tex=>'$$\n'+tex+'\n$$'
export const currentTopics=[
 {title:'Dòng điện và tính chất vật liệu',topics:[
  {slug:'dong-dien',title:'Dòng điện',question:'Chuyển động ngẫu nhiên và vận tốc trôi tạo dòng như thế nào?',source:'25.1'},
  {slug:'dien-tro-suat',title:'Điện trở suất',question:'Vật liệu và nhiệt độ ảnh hưởng đến mật độ dòng ra sao?',source:'25.2'},
  {slug:'dien-tro',title:'Điện trở',question:'Từ điện trở suất và hình học suy điện trở của một mẫu như thế nào?',source:'25.3'}]},
 {title:'Nguồn điện, năng lượng và mô hình vi mô',topics:[
  {slug:'suat-dien-dong',title:'Suất điện động và mạch điện',question:'Nguồn duy trì dòng và điện áp hai cực như thế nào?',source:'25.4'},
  {slug:'nang-luong-cong-suat',title:'Năng lượng và công suất trong mạch',question:'Dòng và điện áp cho biết phần tử nhận hay cấp năng lượng ra sao?',source:'25.5'},
  {slug:'dan-dien-kim-loai',title:'Mô hình dẫn điện trong kim loại',question:'Tán xạ electron liên hệ với điện trở suất như thế nào?',source:'25.6'}]}
]
export const currentSlides=[
 {note,title:'Dòng điện đo điện lượng chuyển qua tiết diện',bullets:['Dòng là đại lượng vô hướng. Chiều quy ước theo điện tích dương.','Electron trôi ngược chiều dòng quy ước trong kim loại.','Dòng ổn định trong một vòng không bị bóng đèn hoặc điện trở tiêu thụ.'],formula:d(String.raw`\begin{aligned}
I&=\frac{dQ}{dt},\\
1\,\mathrm A&=1\,\mathrm{C/s}.
\end{aligned}`),example:''},
 {note,title:'Mật độ dòng điện giữ thông tin về hướng',bullets:['Chuyển động ngẫu nhiên không tạo dòng thuần. Độ trôi nhỏ tạo dòng.','Cùng một dòng qua dây to và dây nhỏ có thể cho mật độ dòng khác nhau.','Điện tích âm và vận tốc trôi ngược trường vẫn cho mật độ dòng cùng chiều trường.'],formula:d(String.raw`\begin{aligned}
I&=n|q|v_dA,\\
J&=I/A,\\
\vec J&=nq\vec v_d.
\end{aligned}`),example:''},
 {note,title:'Điện trở suất thuộc vật liệu và điều kiện khảo sát',bullets:['Độ dẫn điện là nghịch đảo điện trở suất.','Vật liệu Ohm có điện trở suất không đổi theo độ lớn trường trong miền xét.','Hệ số nhiệt cần dùng trong khoảng nhiệt độ mà gần đúng tuyến tính còn phù hợp.'],formula:d(String.raw`\begin{aligned}
\rho&=E/J,\\
\sigma&=1/\rho,\\
\rho(T)&\approx\rho_0[1+\alpha(T-T_0)].
\end{aligned}`),example:''},
 {note,title:'Điện trở còn phụ thuộc chiều dài và tiết diện',bullets:['Dây đồng nhất, tiết diện đều có điện trở tỉ lệ chiều dài và nghịch tiết diện.','Định nghĩa R = V/I không tự khẳng định định luật Ohm.','Muốn V tỉ lệ I phải giữ R không đổi trong điều kiện khảo sát.'],formula:d(String.raw`\begin{aligned}
R&=\frac{\rho L}{A},\\
V&=IR,\\
1\,\Omega&=1\,\mathrm{V/A}.
\end{aligned}`),example:''},
 {note,title:'Suất điện động là năng lượng trên mỗi coulomb',bullets:['Nguồn dùng tác động không tĩnh điện đưa điện tích lên điện thế cao.','Suất điện động có đơn vị volt và không phải lực cơ học.','Nguồn thực có điện trở trong, nên điện áp hai cực phụ thuộc tải.'],formula:d(String.raw`\begin{aligned}
V_{ab}&=\mathcal E-Ir,\\
I&=\frac{\mathcal E}{R+r}.
\end{aligned}`),example:''},
 {note,title:'Mắc dụng cụ đo làm thay đổi mạch nếu chọn sai vị trí',bullets:['Ampe kế lý tưởng có điện trở bằng không, mắc nối tiếp.','Vôn kế lý tưởng có điện trở vô hạn, mắc song song giữa hai điểm cần đo.','Mạch hở và ngắn mạch có điện áp, dòng điện rất khác nhau.'],formula:d(String.raw`\begin{aligned}
I_{\mathrm{oc}}&=0,\\
V_{\mathrm{oc}}&=\mathcal E,\\
I_{\mathrm{sc}}&=\mathcal E/r,\\
V_{\mathrm{sc}}&=0.
\end{aligned}`),example:''},
 {note,title:'Công suất có dấu phân biệt nhận và cấp năng lượng',bullets:['Dòng đi vào đầu a cho công suất nhận bằng (Va − Vb)I.','Điện trở nhận điện năng rồi chuyển hóa thành nhiệt hoặc các dạng khác.','Nguồn phát điện có phần chuyển hóa và phần hao trong điện trở trong.'],formula:d(String.raw`\begin{aligned}
P&=V_{ab}I,\\
P_R&=I^2R,\\
P_{\mathrm{ra}}&=\mathcal EI-I^2r.
\end{aligned}`),example:''},
 {note,title:'Tán xạ liên hệ vận tốc trôi với điện trở suất',bullets:['Mô hình cổ điển dùng thời gian tự do trung bình giữa các va chạm.','Độ trôi có hướng rất nhỏ so với chuyển động ngẫu nhiên.','Mô hình dự đoán điện trở suất không đổi theo trường khi n và τ không đổi theo trường.'],formula:d(String.raw`\begin{aligned}
\vec v_d&=\frac{q\tau}{m}\vec E,\\
\rho&=\frac{m}{ne^2\tau}.
\end{aligned}`),example:''}
]
export const currentCheatsheet={summary:'Định nghĩa, tính chất và công thức của dòng điện, vật liệu dẫn, nguồn điện và công suất.',sections:[
 {id:'current',title:'Dòng điện và mật độ dòng',items:[
  {name:'Định nghĩa và đơn vị dòng điện',formulaRows:[
   {label:'Dòng qua một tiết diện',formula:d(String.raw`I=\frac{dQ}{dt}`)},
   {label:'Dòng không đổi trong khoảng Δt',formula:d(String.raw`\Delta Q=I\Delta t`)},
   {label:'Đơn vị SI',formula:d(String.raw`1\,\mathrm A=1\,\mathrm{C/s}`)}
  ],description:'Dòng điện là vô hướng. Chiều quy ước theo dòng điện tích dương. Dòng ổn định trong một vòng không có nhánh có cùng giá trị tại mọi tiết diện.'},
  {name:'Một loại hạt tải, dòng đều qua tiết diện',formula:d(String.raw`\begin{aligned}
I&=n|q|v_dA,\\
J&=I/A=n|q|v_d,\\
\vec J&=nq\vec v_d.
\end{aligned}`),description:'n là số hạt tải trên một đơn vị thể tích, q có dấu, v_d là độ lớn vận tốc trôi. A là tiết diện vuông góc hướng trôi. Đơn vị J là A/m². Electron có q = −e và trôi ngược điện trường.'},
  {name:'Nhiều loại hạt tải',formula:d(String.raw`\begin{aligned}
\vec J&=\vec J_1+\vec J_2+\cdots+\vec J_N,\\
\vec J_i&=n_iq_i\vec v_{di},\\
\vec J&=\sum_{i=1}^{N}\vec J_i.
\end{aligned}`),description:'Chỉ số i chạy từ 1 đến N qua các loại hạt tải. Điện tích âm và dương chuyển động ngược nhau có thể đóng góp mật độ dòng cùng chiều. Các vector thành phần được cộng tại cùng vị trí.'}]},
 {id:'material',title:'Điện trở suất và độ dẫn điện',items:[
  {name:'Định nghĩa và định luật Ohm vi mô',formulaRows:[
   {label:'Điện trở suất',formula:d(String.raw`\rho=E/J`)},
   {label:'Độ dẫn điện',formula:d(String.raw`\sigma=1/\rho`)},
   {label:'Quan hệ vector trong vật liệu đẳng hướng',formula:d(String.raw`\vec E=\rho\vec J`)}
  ],description:'ρ có đơn vị Ω·m, σ có đơn vị S/m. Vật liệu Ohm có ρ không phụ thuộc độ lớn điện trường trong miền đang xét. ρ còn phụ thuộc nhiệt độ và trạng thái vật liệu.'},
  {name:'Gần đúng phụ thuộc nhiệt độ',formula:d(String.raw`\begin{aligned}
\rho(T)&\approx\rho_0[1+\alpha(T-T_0)],\\
R(T)&\approx R_0[1+\alpha(T-T_0)].
\end{aligned}`),description:'Dùng gần đúng tuyến tính trong khoảng nhiệt độ phù hợp. Công thức R cần bỏ được giãn nở hình học. α có đơn vị nghịch độ C hoặc nghịch kelvin. Kim loại thông thường có α dương, một số vật liệu có α âm.'},
  {name:'Siêu dẫn',formula:d(String.raw`\rho=0,\quad T<T_c`),description:'T_c là nhiệt độ tới hạn trong điều kiện siêu dẫn được xét. Dòng đã thiết lập trong vòng siêu dẫn có thể tồn tại khi không có trường duy trì. Kết luận không áp dụng vô điều kiện cho mọi vật liệu hoặc mọi trường ngoài.'}]},
 {id:'resistance',title:'Điện trở và hình học',items:[
  {name:'Định nghĩa và mẫu trụ đồng nhất',formulaRows:[
   {label:'Tỉ số điện áp và dòng khác không',formula:d(String.raw`R=V/I`)},
   {label:'Dây có tiết diện đều',formula:d(String.raw`R=\rho L/A`)},
   {label:'Đơn vị SI',formula:d(String.raw`1\,\Omega=1\,\mathrm{V/A}`)}
  ],description:'R thuộc mẫu vật, ρ thuộc vật liệu và điều kiện khảo sát. Công thức hình học cần dòng phân bố đều, ρ đồng nhất và tiết diện A không đổi dọc L.'},
  {name:'Quan hệ dòng, trường và điện áp',formula:d(String.raw`\begin{aligned}
V&=EL,\\
J&=I/A,\\
V&=IR.
\end{aligned}`),description:'V = EL dùng trường dọc dây không đổi. J = I/A dùng mật độ dòng đều trên tiết diện. V tỉ lệ I chỉ khi R không đổi trong miền khảo sát, kể cả điều kiện nhiệt độ.'}]},
 {id:'source',title:'Nguồn điện và dụng cụ đo',items:[
  {name:'Suất điện động và nguồn đang phát dòng',formulaRows:[
   {label:'Công của tác động không tĩnh điện trên điện tích q',formula:d(String.raw`W_n=q\mathcal E`)},
   {label:'Nguồn lý tưởng, r = 0',formula:d(String.raw`V_{ab}=\mathcal E`)},
   {label:'Nguồn thực, dòng đi ra cực dương',formula:d(String.raw`V_{ab}=\mathcal E-Ir`)},
   {label:'Nguồn nối một điện trở ngoài R',formula:d(String.raw`I=\frac{\mathcal E}{R+r}`)}
  ],description:'ℰ có đơn vị volt và là năng lượng trên mỗi coulomb do tác động không tĩnh điện cung cấp. r là điện trở trong, R là tải ngoài. Nguồn có suất điện động cố định không đồng nghĩa dòng cung cấp cố định.'},
  {name:'Nguồn đang được nạp',formula:d(String.raw`V_{ab}=\mathcal E+Ir`),description:'I là độ lớn dòng đi vào cực dương của pin. Điện áp đưa vào phải cung cấp cả phần tích trữ hóa năng và sụt áp trong điện trở trong.'},
  {name:'Mạch hở và ngắn mạch',formula:d(String.raw`\begin{aligned}
I_{\mathrm{oc}}&=0,\\
V_{\mathrm{oc}}&=\mathcal E,\\
I_{\mathrm{sc}}&=\mathcal E/r,\\
V_{\mathrm{sc}}&=0.
\end{aligned}`),description:'oc ký hiệu mạch hở, sc ký hiệu ngắn mạch lý tưởng. Ngắn mạch dùng điện trở ngoài bằng không, r khác không. Mô hình ℰ,r không đổi có thể không còn phù hợp khi nguồn nóng hoặc biến đổi mạnh.'},
  {name:'Vôn kế và ampe kế lý tưởng',formula:'',description:'Vôn kế lý tưởng có điện trở vô hạn, mắc song song giữa hai điểm cần đo. Ampe kế lý tưởng có điện trở bằng không, mắc nối tiếp. Đổi chỗ các phần tử trong cùng vòng nối tiếp không đổi dòng. Dụng cụ lý tưởng mắc sai có thể làm hở hoặc ngắn mạch.'}]},
 {id:'energy',title:'Năng lượng và công suất',items:[
  {name:'Phần tử mạch với quy ước dòng vào đầu a',formula:d(String.raw`\begin{aligned}
V_{ab}&=V_a-V_b,\\
P&=V_{ab}I,\\
W_{\mathrm{in}}&=P\Delta t.
\end{aligned}`),description:'P dương khi phần tử nhận điện năng, âm khi cấp điện năng. W_in là năng lượng điện nhận bởi phần tử trong khoảng Δt, với P giữ không đổi. Điện năng được đo bằng joule hoặc kilowatt-giờ, 1 kWh = 3,60 MJ.'},
  {name:'Điện trở nhận công suất',formulaRows:[
   {label:'Theo dòng và điện áp',formula:d(String.raw`P_R=VI`)},
   {label:'Theo dòng và điện trở',formula:d(String.raw`P_R=I^2R`)},
   {label:'Theo điện áp và điện trở',formula:d(String.raw`P_R=V^2/R`)}
  ],description:'R dương và V, I được lấy theo quy ước thu năng lượng của điện trở. Khi so hai trạng thái phải xác định nguồn giữ điện áp, dòng hay suất điện động của một nguồn thực.'},
  {name:'Công suất của nguồn thực',formulaRows:[
   {label:'Chuyển hóa hóa năng khi phóng',formula:d(String.raw`P_{\mathcal E}=\mathcal EI`)},
   {label:'Tổn hao nhiệt trong nguồn',formula:d(String.raw`P_r=I^2r`)},
   {label:'Công suất điện ra mạch ngoài',formula:d(String.raw`P_{\mathrm{ra}}=\mathcal EI-I^2r`)},
   {label:'Công suất điện vào khi nạp',formula:d(String.raw`P_{\mathrm{in}}=\mathcal EI+I^2r`)}
  ],description:'I là độ lớn dòng trong chế độ tương ứng. Tổn hao I²r có ở cả nạp và phóng. Công suất ra bằng công suất tải trong mô hình dây nối không có điện trở.'}]},
 {id:'microscopic',title:'Mô hình dẫn điện trong kim loại',items:[
  {name:'Vận tốc trôi và điện trở suất',formula:d(String.raw`\begin{aligned}
\vec v_d&=\frac{q\tau}{m}\vec E,\\
\vec J&=\frac{nq^2\tau}{m}\vec E,\\
\rho&=\frac{m}{ne^2\tau}.
\end{aligned}`),description:'Mô hình cổ điển gần đúng dùng τ là thời gian tự do trung bình, m là khối lượng electron, q = −e. Electron trôi ngược trường nhưng J cùng chiều trường. Giữ n,τ độc lập với E cho quan hệ Ohm. Nhiệt độ ảnh hưởng đến tán xạ và mật độ hạt tải.'}]}
]}
