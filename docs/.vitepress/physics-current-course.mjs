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
&I = \frac{dQ}{dt},\\
&1\,\mathrm A = 1\,\mathrm{C/s}.
\end{aligned}`),example:''},
 {note,title:'Mật độ dòng điện giữ thông tin về hướng',bullets:['Chuyển động ngẫu nhiên không tạo dòng thuần. Độ trôi nhỏ tạo dòng.','Cùng một dòng qua dây to và dây nhỏ có thể cho mật độ dòng khác nhau.','Điện tích âm và vận tốc trôi ngược trường vẫn cho mật độ dòng cùng chiều trường.'],formula:d(String.raw`\begin{aligned}
&I = n|q|v_dA,\\
&J = I/A,\\
&\vec J = nq\vec v_d.
\end{aligned}`),example:''},
 {note,title:'Điện trở suất thuộc vật liệu và điều kiện khảo sát',bullets:['Độ dẫn điện là nghịch đảo điện trở suất.','Vật liệu Ohm có điện trở suất không đổi theo độ lớn trường trong miền xét.','Hệ số nhiệt cần dùng trong khoảng nhiệt độ mà gần đúng tuyến tính còn phù hợp.'],formula:d(String.raw`\begin{aligned}
&\rho = E/J,\\
&\sigma = 1/\rho,\\
&\rho(T) \approx \rho_0[1+\alpha(T-T_0)].
\end{aligned}`),example:''},
 {note,title:'Điện trở còn phụ thuộc chiều dài và tiết diện',bullets:['Dây đồng nhất, tiết diện đều có điện trở tỉ lệ chiều dài và nghịch tiết diện.','Định nghĩa R = V/I không tự khẳng định định luật Ohm.','Muốn V tỉ lệ I phải giữ R không đổi trong điều kiện khảo sát.'],formula:d(String.raw`\begin{aligned}
&R = \frac{\rho L}{A},\\
&V = IR,\\
&1\,\Omega = 1\,\mathrm{V/A}.
\end{aligned}`),example:''},
 {note,title:'Suất điện động là năng lượng trên mỗi coulomb',bullets:['Nguồn dùng tác động không tĩnh điện đưa điện tích lên điện thế cao.','Suất điện động có đơn vị volt và không phải lực cơ học.','Nguồn thực có điện trở trong, nên điện áp hai cực phụ thuộc tải.'],formula:d(String.raw`\begin{aligned}
&V_{ab} = \mathcal E-Ir,\\
&I = \frac{\mathcal E}{R+r}.
\end{aligned}`),example:''},
 {note,title:'Mắc dụng cụ đo làm thay đổi mạch nếu chọn sai vị trí',bullets:['Ampe kế lý tưởng có điện trở bằng không, mắc nối tiếp.','Vôn kế lý tưởng có điện trở vô hạn, mắc song song giữa hai điểm cần đo.','Mạch hở và ngắn mạch có điện áp, dòng điện rất khác nhau.'],formula:d(String.raw`\begin{aligned}
&I_{\mathrm{oc}} = 0,\\
&V_{\mathrm{oc}} = \mathcal E,\\
&I_{\mathrm{sc}} = \mathcal E/r,\\
&V_{\mathrm{sc}} = 0.
\end{aligned}`),example:''},
 {note,title:'Công suất có dấu phân biệt nhận và cấp năng lượng',bullets:['Dòng đi vào đầu a cho công suất nhận bằng (Va − Vb)I.','Điện trở nhận điện năng rồi chuyển hóa thành nhiệt hoặc các dạng khác.','Nguồn phát điện có phần chuyển hóa và phần hao trong điện trở trong.'],formula:d(String.raw`\begin{aligned}
&P = V_{ab}I,\\
&P_R = I^2R,\\
&P_{\mathrm{ra}} = \mathcal EI-I^2r.
\end{aligned}`),example:''},
 {note,title:'Tán xạ liên hệ vận tốc trôi với điện trở suất',bullets:['Mô hình cổ điển dùng thời gian tự do trung bình giữa các va chạm.','Độ trôi có hướng rất nhỏ so với chuyển động ngẫu nhiên.','Mô hình dự đoán điện trở suất không đổi theo trường khi n và τ không đổi theo trường.'],formula:d(String.raw`\begin{aligned}
&\vec v_d = \frac{q\tau}{m}\vec E,\\
&\rho = \frac{m}{ne^2\tau}.
\end{aligned}`),example:''}
]
export const currentCheatsheet={summary:'Định nghĩa, tính chất và công thức của dòng điện, vật liệu dẫn, nguồn điện và công suất.',sections:[
 {id:'current',title:'Dòng điện và mật độ dòng',items:[
  {name:'Định nghĩa và đơn vị dòng điện',formulaRows:[
   {label:'Dòng qua một tiết diện',formula:d(String.raw`I=\frac{dQ}{dt}`)},
   {label:'Dòng không đổi trong khoảng Δt',formula:d(String.raw`\Delta Q=I\Delta t`)},
   {label:'Đơn vị SI',formula:d(String.raw`1\,\mathrm A=1\,\mathrm{C/s}`)}
  ],variables:[
   String.raw`$I$: Cường độ dòng điện tức thời qua tiết diện dây dẫn ($\mathrm{A}$ - Ampere)`,
   String.raw`$dQ$: Điện lượng dịch chuyển qua tiết diện trong thời gian vi phân $dt$ ($\mathrm{C}$)`,
   String.raw`$\Delta Q$: Tổng điện lượng dịch chuyển trong khoảng thời gian $\Delta t$ ($\mathrm{C}$)`,
   String.raw`$\Delta t$: Khoảng thời gian dòng điện chạy qua ($\mathrm{s}$)`
  ],description:'Dòng điện là vô hướng. Chiều quy ước theo dòng điện tích dương. Dòng ổn định trong một vòng không có nhánh có cùng giá trị tại mọi tiết diện.'},
  {name:'Một loại hạt tải, dòng đều qua tiết diện',formula:d(String.raw`\begin{aligned}
&I = n|q|v_dA,\\
&J = I/A=n|q|v_d,\\
&\vec J = nq\vec v_d.
\end{aligned}`),variables:[
   String.raw`$I$: Cường độ dòng điện qua toàn bộ tiết diện dây dẫn ($\mathrm{A}$)`,
   String.raw`$n$: Mật độ hạt mang điện trên một đơn vị thể tích dây dẫn ($\mathrm{m^{-3}}$)`,
   String.raw`$q$: Điện tích của mỗi hạt tải điện ($\mathrm{C}$)`,
   String.raw`$v_d$: Tốc độ trôi định hướng của các hạt mang điện ($\mathrm{m/s}$)`,
   String.raw`$A$: Diện tích tiết diện ngang của dây dẫn ($\mathrm{m^2}$)`,
   String.raw`$J$: Độ lớn mật độ dòng điện ($J = I/A$) ($\mathrm{A/m^2}$)`,
   String.raw`$\vec J$: Vector mật độ dòng điện ($\mathrm{A/m^2}$)`
  ],description:'n là số hạt tải trên một đơn vị thể tích, q có dấu, v_d là độ lớn vận tốc trôi. A là tiết diện vuông góc hướng trôi. Đơn vị J là A/m². Electron có q = −e và trôi ngược điện trường.'},
  {name:'Nhiều loại hạt tải',formula:d(String.raw`\begin{aligned}
&\vec J = \vec J_1+\vec J_2+\cdots+\vec J_N,\\
&\vec J_i = n_iq_i\vec v_{di},\\
&\vec J = \sum_{i=1}^{N}\vec J_i.
\end{aligned}`),variables:[
   String.raw`$\vec J$: Vector mật độ dòng điện tổng hợp của tất cả các loại hạt tải ($\mathrm{A/m^2}$)`,
   String.raw`$\vec J_i$: Vector mật độ dòng điện do loại hạt thứ $i$ đóng góp ($\mathrm{A/m^2}$)`,
   String.raw`$n_i$: Mật độ hạt loại thứ $i$ trên một đơn vị thể tích ($\mathrm{m^{-3}}$)`,
   String.raw`$\vec v_{di}$: Vector vận tốc trôi định hướng của loại hạt thứ $i$ ($\mathrm{m/s}$)`
  ],description:'Chỉ số i chạy từ 1 đến N qua các loại hạt tải. Điện tích âm và dương chuyển động ngược nhau có thể đóng góp mật độ dòng cùng chiều. Các vector thành phần được cộng tại cùng vị trí.'}]},
 {id:'material',title:'Điện trở suất và độ dẫn điện',items:[
  {name:'Định nghĩa và định luật Ohm vi mô',formulaRows:[
   {label:'Điện trở suất',formula:d(String.raw`\rho=E/J`)},
   {label:'Độ dẫn điện',formula:d(String.raw`\sigma=1/\rho`)},
   {label:'Quan hệ vector trong vật liệu đẳng hướng',formula:d(String.raw`\vec E=\rho\vec J`)}
  ],variables:[
   String.raw`$\rho$: Điện trở suất của vật liệu dẫn điện ($\Omega\cdot\mathrm{m}$)`,
   String.raw`$E$: Cường độ điện trường bên trong vật dẫn ($\mathrm{V/m}$)`,
   String.raw`$J$: Mật độ dòng điện sinh ra bởi điện trường đó ($\mathrm{A/m^2}$)`,
   String.raw`$\sigma$: Độ dẫn điện riêng của vật liệu ($1/\rho$) ($\mathrm{S/m}$ hoặc $(\Omega\cdot\mathrm{m})^{-1}$)`,
   String.raw`$\vec E$: Vector cường độ điện trường trong vật liệu ($\mathrm{V/m}$)`
  ],description:'ρ có đơn vị Ω·m, σ có đơn vị S/m. Vật liệu Ohm có ρ không phụ thuộc độ lớn điện trường trong miền đang xét. ρ còn phụ thuộc nhiệt độ và trạng thái vật liệu.'},
  {name:'Gần đúng phụ thuộc nhiệt độ',formula:d(String.raw`\begin{aligned}
&\rho(T) \approx \rho_0[1+\alpha(T-T_0)],\\
&R(T) \approx R_0[1+\alpha(T-T_0)].
\end{aligned}`),variables:[
   String.raw`$\rho(T)$: Điện trở suất của vật liệu ở nhiệt độ $T$ ($\Omega\cdot\mathrm{m}$)`,
   String.raw`$\rho_0$: Điện trở suất của vật liệu ở nhiệt độ chuẩn $T_0$ ($\Omega\cdot\mathrm{m}$)`,
   String.raw`$R(T)$: Điện trở của mẫu vật dẫn ở nhiệt độ $T$ ($\Omega$)`,
   String.raw`$R_0$: Điện trở của mẫu vật dẫn ở nhiệt độ chuẩn $T_0$ ($\Omega$)`,
   String.raw`$\alpha$: Hệ số nhiệt điện trở của vật liệu ($\mathrm{K^{-1}}$ hoặc $\mathrm{^\circ C^{-1}}$)`,
   String.raw`$T - T_0$: Độ chênh lệch nhiệt độ so với mốc chuẩn ($\mathrm{K}$ hoặc $\mathrm{^\circ C}$)`
  ],description:'Dùng gần đúng tuyến tính trong khoảng nhiệt độ phù hợp. Công thức R cần bỏ được giãn nở hình học. α có đơn vị nghịch độ C hoặc nghịch kelvin. Kim loại thông thường có α dương, một số vật liệu có α âm.'},
  {name:'Siêu dẫn',formula:d(String.raw`\rho=0,\quad T<T_c`),variables:[
   String.raw`$\rho$: Điện trở suất của vật liệu siêu dẫn ở trạng thái siêu dẫn ($\rho = 0$) ($\Omega\cdot\mathrm{m}$)`,
   String.raw`$T_c$: Nhiệt độ chuyển pha tới hạn của vật liệu siêu dẫn ($\mathrm{K}$)`
  ],description:'T_c là nhiệt độ tới hạn trong điều kiện siêu dẫn được xét. Dòng đã thiết lập trong vòng siêu dẫn có thể tồn tại khi không có trường duy trì. Kết luận không áp dụng vô điều kiện cho mọi vật liệu hoặc mọi trường ngoài.'}]},
 {id:'resistance',title:'Điện trở và hình học',items:[
  {name:'Định nghĩa và mẫu trụ đồng nhất',formulaRows:[
   {label:'Định nghĩa điện trở',formula:d(String.raw`R=V/I`)},
   {label:'Dây đồng nhất tiết diện A, dài L',formula:d(String.raw`R=\frac{\rho L}{A}`)},
   {label:'Đơn vị ohm',formula:d(String.raw`1\,\Omega=1\,\mathrm{V/A}`)}
  ],variables:[
   String.raw`$R$: Điện trở của vật dẫn hình trụ đồng nhất ($\Omega$ - Ohm)`,
   String.raw`$\rho$: Điện trở suất của vật liệu làm dây dẫn ($\Omega\cdot\mathrm{m}$)`,
   String.raw`$L$: Chiều dài của dây dẫn hình trụ ($\mathrm{m}$)`,
   String.raw`$A$: Diện tích tiết diện ngang đều của dây dẫn ($\mathrm{m^2}$)`,
   String.raw`$V$: Hiệu điện thế đặt vào hai đầu đoạn mạch ($V = IR$) ($\mathrm{V}$)`,
   String.raw`$I$: Cường độ dòng điện chạy qua điện trở ($\mathrm{A}$)`
  ],description:'R đo bằng ohm. Định nghĩa R = V/I áp dụng cho mọi phần tử hai đầu cực. Công thức hình học áp dụng cho dòng chạy đều song song trục mẫu.'},
  {name:'Quan hệ dòng, trường và điện áp',formula:d(String.raw`\begin{aligned}
&V = EL,\\
&I = JA,\\
&E = \rho J.
\end{aligned}`),variables:[
   String.raw`$V$: Hiệu điện thế giữa hai đầu mẫu dây dẫn đồng nhất ($\mathrm{V}$)`,
   String.raw`$E$: Cường độ điện trường dọc theo chiều dài dây dẫn ($E = V/L$) ($\mathrm{V/m}$)`,
   String.raw`$J$: Mật độ dòng điện trong dây dẫn ($J = I/A$) ($\mathrm{A/m^2}$)`
  ],description:'Ba quan hệ này nối mô hình vĩ mô với mô hình vi mô của đoạn dây đồng nhất mang dòng đều.'}]},
 {id:'source',title:'Nguồn điện và dụng cụ đo',items:[
  {name:'Suất điện động và nguồn đang phát dòng',formulaRows:[
   {label:'Điện áp hai cực khi phát dòng I',formula:d(String.raw`V_{ab}=\mathcal E-Ir`)},
   {label:'Dòng trong mạch kín một vòng với tải R',formula:d(String.raw`I=\frac{\mathcal E}{R+r}`)},
   {label:'Định nghĩa suất điện động',formula:d(String.raw`\mathcal E=\frac{dW_{\mathrm{nguon}}}{dQ}`)},
   {label:'Đơn vị suất điện động',formula:d(String.raw`1\,\mathrm V=1\,\mathrm{J/C}`)}
  ],variables:[
   String.raw`$V_{ab}$: Hiệu điện thế đo giữa hai cực dương và âm của nguồn phát ($\mathrm{V}$)`,
   String.raw`$\mathcal E$: Suất điện động của nguồn điện ($\mathrm{V}$)`,
   String.raw`$I$: Cường độ dòng điện do nguồn phát ra mạch ngoài ($\mathrm{A}$)`,
   String.raw`$r$: Điện trở trong của nguồn điện ($\Omega$)`,
   String.raw`$R$: Điện trở tương đương của tải ngoài nối vào nguồn ($\Omega$)`
  ],description:'a là cực dương, b là cực âm. Dòng đi ra từ cực dương khi nguồn phát. r là điện trở trong.'},
  {name:'Nguồn đang được nạp',formula:d(String.raw`V_{ab}=\mathcal E+Ir`),variables:[
   String.raw`$V_{ab}$: Điện áp cần đặt vào hai cực của nguồn để nạp điện ($V_{ab} > \mathcal E$) ($\mathrm{V}$)`,
   String.raw`$\mathcal E$: Suất điện động của nguồn đang được nạp ($\mathrm{V}$)`,
   String.raw`$I$: Cường độ dòng nạp đi vào cực dương của nguồn ($\mathrm{A}$)`,
   String.raw`$r$: Điện trở trong của nguồn điện ($\Omega$)`
  ],description:'Dòng đi vào cực dương từ mạch ngoài. Điện áp hai cực lớn hơn suất điện động.'},
  {name:'Mạch hở và ngắn mạch',formula:d(String.raw`\begin{aligned}
&I_{\mathrm{oc}} = 0,\quad V_{\mathrm{oc}}=\mathcal E,\\
&I_{\mathrm{sc}} = \mathcal E/r,\quad V_{\mathrm{sc}}=0.
\end{aligned}`),variables:[
   String.raw`$I_{\mathrm{oc}}$: Cường độ dòng điện khi mạch hở ($I_{\mathrm{oc}} = 0$) ($\mathrm{A}$)`,
   String.raw`$V_{\mathrm{oc}}$: Điện áp hai cực khi mạch hở, đúng bằng suất điện động ($V_{\mathrm{oc}} = \mathcal E$) ($\mathrm{V}$)`,
   String.raw`$I_{\mathrm{sc}}$: Dòng điện ngắn mạch (đoản mạch) cực đại ($I_{\mathrm{sc}} = \mathcal E/r$) ($\mathrm{A}$)`,
   String.raw`$V_{\mathrm{sc}}$: Điện áp giữa hai cực khi bị ngắn mạch trực tiếp ($V_{\mathrm{sc}} = 0$) ($\mathrm{V}$)`
  ],description:'Mạch hở không có dòng. Ngắn mạch nối trực tiếp hai cực bằng dây dẫn có điện trở coi như bằng không.'},
  {name:'Vôn kế và ampe kế lý tưởng',formula:'',description:'Vôn kế lý tưởng có điện trở vô hạn, mắc song song hai điểm cần đo. Ampe kế lý tưởng có điện trở bằng không, mắc nối tiếp trên nhánh cần đo.'}]},
 {id:'power',title:'Năng lượng và công suất',items:[
  {name:'Phần tử mạch với quy ước dòng vào đầu a',formula:d(String.raw`P=V_{ab}I`),variables:[
   String.raw`$P$: Công suất điện tiêu thụ hoặc truyền qua phần tử mạch ($\mathrm{W}$ - Watt)`,
   String.raw`$V_{ab}$: Hiệu điện thế giữa điểm vào $a$ và điểm ra $b$ ($V_a - V_b$) ($\mathrm{V}$)`,
   String.raw`$I$: Cường độ dòng điện chạy qua phần tử từ $a$ sang $b$ ($\mathrm{A}$)`
  ],description:'P > 0: phần tử nhận năng lượng điện. P < 0: phần tử cấp năng lượng điện cho mạch ngoài.'},
  {name:'Điện trở nhận công suất',formulaRows:[
   {label:'Theo điện áp và dòng',formula:d(String.raw`P_R=VI`)},
   {label:'Theo dòng và điện trở',formula:d(String.raw`P_R=I^2R`)},
   {label:'Theo điện áp và điện trở',formula:d(String.raw`P_R=\frac{V^2}{R}`)}
  ],variables:[
   String.raw`$P_R$: Công suất tỏa nhiệt Jun–Lenxơ trên điện trở thuần ($\mathrm{W}$)`,
   String.raw`$I$: Dòng điện qua điện trở ($\mathrm{A}$)`,
   String.raw`$R$: Điện trở của phần tử mạch ($\Omega$)`,
   String.raw`$V$: Điện áp rơi trên điện trở ($\mathrm{V}$)`
  ],description:'Điện trở thuần luôn nhận điện năng và chuyển hóa hoàn toàn thành nhiệt.'},
  {name:'Công suất của nguồn thực',formulaRows:[
   {label:'Công suất nguồn sinh ra',formula:d(String.raw`P_{\mathrm{hoa}}=\mathcal EI`)},
   {label:'Hao phí trong điện trở trong',formula:d(String.raw`P_r=I^2r`)},
   {label:'Công suất ra tải khi phát',formula:d(String.raw`P_{\mathrm{ra}}=\mathcal EI-I^2r`)},
   {label:'Công suất nhận khi nạp',formula:d(String.raw`P_{\mathrm{nap}}=\mathcal EI+I^2r`)}
  ],variables:[
   String.raw`$P_{\mathrm{hoa}}$: Công suất biến đổi hóa năng thành điện năng trong nguồn ($P_{\mathrm{hoa}} = \mathcal EI$) ($\mathrm{W}$)`,
   String.raw`$P_{\mathrm{ra}}$: Công suất có ích cung cấp cho mạch ngoài ($P_{\mathrm{ra}} = V_{ab}I$) ($\mathrm{W}$)`,
   String.raw`$P_r$: Công suất hao phí do tỏa nhiệt trên điện trở trong ($P_r = I^2r$) ($\mathrm{W}$)`
  ],description:'Khi phát dòng, công suất ra tải nhỏ hơn công suất nguồn do hao phí trên r. Khi nạp, nguồn nhận thêm phần nhiệt hao phí.'}]},
 {id:'microscopic',title:'Mô hình dẫn điện trong kim loại',items:[
  {name:'Vận tốc trôi và điện trở suất',formula:d(String.raw`\begin{aligned}
&\vec v_d = \frac{q\tau}{m}\vec E,\\
&\rho = \frac{m}{ne^2\tau}.
\end{aligned}`),variables:[
   String.raw`$\vec v_d$: Vector vận tốc trôi định hướng của electron trong kim loại ($\mathrm{m/s}$)`,
   String.raw`$\tau$: Thời gian tự do trung bình giữa hai va chạm tán xạ liên tiếp ($\mathrm{s}$)`,
   String.raw`$m$: Khối lượng nghỉ của hạt electron ($\approx 9{,}109\times10^{-31}\,\mathrm{kg}$)`,
   String.raw`$e$: Độ lớn điện tích nguyên tố của electron ($\approx 1{,}602\times10^{-19}\,\mathrm{C}$)`,
   String.raw`$n$: Mật độ hạt electron tự do trên một mét khối kim loại ($\mathrm{m^{-3}}$)`,
   String.raw`$\rho$: Điện trở suất suy ra từ mô hình dẫn điện vi mô ($\Omega\cdot\mathrm{m}$)`
  ],description:'τ là thời gian tự do trung bình giữa hai va chạm, m là khối lượng electron, e là độ lớn điện tích cơ bản.'}]}
]}
