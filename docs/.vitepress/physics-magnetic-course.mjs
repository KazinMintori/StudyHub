const note='07-tu-truong-luc-tu'
const d=tex=>'$$\n'+tex+'\n$$'
export const magneticTopics=[
 {title:'Từ trường và cách biểu diễn',topics:[
  {slug:'tu-tinh',title:'Từ tính',question:'Vì sao nam châm có hai cực và tương tác từ gắn với điện tích chuyển động?',source:'27.1'},
  {slug:'tu-truong',title:'Từ trường',question:'Vận tốc và dấu điện tích quyết định lực từ như thế nào?',source:'27.2'},
  {slug:'duong-suc-tu-thong',title:'Đường sức từ và từ thông',question:'Bản đồ đường sức và từ thông cho biết những gì về từ trường?',source:'27.3'}]},
 {title:'Chuyển động của hạt mang điện',topics:[
  {slug:'chuyen-dong-hat',title:'Chuyển động trong từ trường',question:'Khi nào hạt đi theo đường tròn hoặc đường xoắn ốc?',source:'27.4'},
  {slug:'ung-dung-hat',title:'Ứng dụng chuyển động của hạt',question:'Trường chéo nhau chọn vận tốc và phân biệt khối lượng hạt ra sao?',source:'27.5'}]},
 {title:'Dòng điện, vòng dây và thiết bị',topics:[
  {slug:'luc-len-day',title:'Lực từ lên dây dẫn',question:'Lực vi mô lên hạt tải trở thành lực lên cả dây như thế nào?',source:'27.6'},
  {slug:'vong-day-mo-men',title:'Lực và mômen lên vòng dây',question:'Vì sao tổng lực có thể bằng không nhưng vòng vẫn quay?',source:'27.7'},
  {slug:'dong-co-dien',title:'Động cơ điện một chiều',question:'Cổ góp và suất phản điện động quyết định chiều quay và công suất ra sao?',source:'27.8'},
  {slug:'hall',title:'Hiệu ứng Hall',question:'Điện áp ngang giúp suy dấu và mật độ hạt tải như thế nào?',source:'27.9'}]}
]
export const magneticSlides=[
 {note,title:'Từ tính gắn với các điện tích chuyển động',bullets:['Hai cực cùng tên đẩy nhau, hai cực khác tên hút nhau.','Chia một nam châm thành các phần tạo các nam châm nhỏ có hai cực.','Dòng điện tạo từ trường, còn từ trường tác dụng lên điện tích đang chuyển động.'],formula:'',example:''},
 {note,title:'Lực từ có hướng vuông góc vận tốc và trường',bullets:['Dấu điện tích quyết định chiều lực so với tích có hướng.','Vận tốc song song hoặc ngược song song trường cho lực bằng không.','Lực từ không sinh công lên hạt vì vuông góc vận tốc tức thời.'],formula:d(String.raw`\begin{aligned}
&\vec F = q\vec v\times\vec B,\\
&F = |q|vB\sin\phi,\\
&\vec F\cdot\vec v = 0.
\end{aligned}`),example:''},
 {note,title:'Đường sức từ biểu diễn trường và không chỉ hướng lực',bullets:['Tiếp tuyến của đường sức cho hướng từ trường tại điểm ấy.','Mật độ đường trong cùng bản đồ biểu thị tương đối độ mạnh của trường.','Đường sức không có nguồn hoặc điểm tận cùng. Các bản đồ nam châm khép qua cả bên trong nam châm.'],formula:d(String.raw`\oint\vec B\cdot d\vec A=0`),example:''},
 {note,title:'Dấu từ thông phụ thuộc pháp tuyến đã chọn',bullets:['Thành phần vuông góc mặt đóng góp vào từ thông.','Mặt kín dùng pháp tuyến hướng ra ngoài, mặt hở cần chọn một hướng nhất quán.','Công thức BA cosφ dùng mặt phẳng và từ trường đều trên mặt.'],formula:d(String.raw`\begin{aligned}
&\Phi_B = \int\vec B\cdot d\vec A,\\
&\Phi_B = BA\cos\phi,\\
&1\,\mathrm{Wb} = 1\,\mathrm{T\cdot m^2}.
\end{aligned}`),example:''},
 {note,title:'Từ trường đều bẻ hướng hạt mà không đổi tốc độ',bullets:['Vận tốc vuông góc trường cho quỹ đạo tròn.','Thành phần song song trường giữ không đổi và tạo bước xoắn.','Các công thức dùng khối lượng không đổi trong mô hình không tương đối tính.'],formula:d(String.raw`\begin{aligned}
&R = \frac{mv_\perp}{|q|B},\\
&\omega = \frac{|q|B}{m},\\
&T = \frac{2\pi m}{|q|B},\\
&p = v_\parallel T.
\end{aligned}`),example:''},
 {note,title:'Bộ chọn vận tốc cân bằng hai lực',bullets:['Điện trường và từ trường được bố trí chéo nhau.','Chỉ vận tốc có hướng và độ lớn phù hợp mới đi thẳng qua vùng chọn.','Hạt nhanh hơn hoặc chậm hơn bị lệch theo các chiều khác nhau.'],formula:d(String.raw`\begin{aligned}
&q\vec E+q\vec v\times\vec B = 0,\\
&v = E/B.
\end{aligned}`),example:''},
 {note,title:'Khối phổ dùng bán kính quỹ đạo để phân biệt hạt',bullets:['Sau bộ chọn vận tốc, các hạt có cùng tốc độ.','Trường phân tích bẻ quỹ đạo, bán kính phụ thuộc khối lượng trên độ lớn điện tích.','Hai bán kính khác nhau đưa các đồng vị đến các vị trí khác nhau.'],formula:d(String.raw`\begin{aligned}
&R = \frac{mv}{|q|B'},\\
&\frac m{|q|} = \frac{BB'R}{E}.
\end{aligned}`),example:''},
 {note,title:'Dòng điện trong dây chịu tổng lực của các hạt tải',bullets:['Vector chiều dài của dây hướng theo dòng quy ước.','Dây thẳng trong trường đều có thể dùng lực của cả đoạn.','Dây cong hoặc trường không đều cần cộng vector lực từng phần tử.'],formula:d(String.raw`\begin{aligned}
&\vec F = I\vec l\times\vec B,\\
&d\vec F = I\,d\vec l\times\vec B.
\end{aligned}`),example:''},
 {note,title:'Vòng dây trong trường đều có thể chịu mômen',bullets:['Các lực trên vòng kín triệt tiêu tổng, nhưng các đường tác dụng khác nhau có thể tạo mômen.','Quy tắc bàn tay phải cho hướng mômen từ theo chiều dòng.','Cuộn N vòng cùng hình học và hướng làm mômen từ tăng N lần.'],formula:d(String.raw`\begin{aligned}
&\vec\mu = NI\vec A,\\
&\vec\tau = \vec\mu\times\vec B.
\end{aligned}`),example:''},
 {note,title:'Năng lượng thấp nhất khi mômen từ cùng hướng trường',bullets:['Góc được tính giữa mômen từ và từ trường.','Cùng chiều là cân bằng bền, ngược chiều là cân bằng không bền.','Trong trường không đều, vòng còn có thể chịu lực tổng hướng về hoặc ra xa vùng trường mạnh.'],formula:d(String.raw`\begin{aligned}
&U = -\vec\mu\cdot\vec B,\\
&U = -\mu B\cos\phi.
\end{aligned}`),example:''},
 {note,title:'Động cơ chuyển điện năng thành cơ năng',bullets:['Cổ góp đổi chiều dòng trong vòng sau nửa vòng quay để duy trì chiều mômen.','Suất phản điện động tăng theo tốc độ khi cấu hình và từ trường giữ nguyên.','Rôto dừng làm suất phản điện động mất đi, nên dòng tăng mạnh trong mô hình nguồn và điện trở cố định.'],formula:d(String.raw`\begin{aligned}
&V_{ab} = \mathcal E+Ir,\\
&P_{\mathrm{in}} = V_{ab}I,\\
&P_{\mathrm{mech}} = \mathcal EI,\\
&P_r = I^2r.
\end{aligned}`),example:''},
 {note,title:'Hiệu ứng Hall tách điện tích theo phương ngang',bullets:['Lực từ dồn hạt tải về một mép và tạo điện trường ngang.','Ở cân bằng, lực điện ngang chống lại lực từ.','Cực tính Hall cho dấu hạt tải, còn độ lớn giúp suy mật độ trong mô hình thích hợp.'],formula:d(String.raw`\begin{aligned}
&E_z = -v_xB_y,\\
&J_x = nqv_x,\\
&nq = -\frac{J_xB_y}{E_z}.
\end{aligned}`),example:''}
]
export const magneticCheatsheet={summary:'Định nghĩa, tính chất và công thức của lực từ, từ thông, chuyển động hạt, vòng dây, động cơ và hiệu ứng Hall.',sections:[
 {id:'field-force',title:'Từ trường và lực từ',items:[
  {name:'Lực lên một hạt mang điện',formula:d(String.raw`\begin{aligned}
&\vec F = q\vec v\times\vec B,\\
&F = |q|vB\sin\phi,\\
&\vec F\cdot\vec v = 0.
\end{aligned}`),variables:[
   String.raw`$\vec F$: Vector lực từ tác dụng lên hạt mang điện chuyển động ($\mathrm{N}$)`,
   String.raw`$q$: Điện tích của hạt mang điện ($\mathrm{C}$)`,
   String.raw`$\vec v$: Vector vận tốc của hạt mang điện ($\mathrm{m/s}$)`,
   String.raw`$\vec B$: Vector cảm ứng từ của từ trường ($\mathrm{T}$ - Tesla)`,
   String.raw`$\phi$: Góc hợp bởi vector vận tốc $\vec v$ và vector cảm ứng từ $\vec B$ ($\mathrm{rad}$ hoặc độ)`
  ],description:'φ là góc giữa vận tốc và từ trường. Lực đổi chiều khi đổi dấu q hoặc đảo một trong hai vector. Lực từ không sinh công lên hạt và không làm thay đổi động năng nếu là lực duy nhất.'},
  {name:'Các thành phần lực và đơn vị',formula:d(String.raw`\begin{aligned}
&F_x = q(v_yB_z-v_zB_y),\\
&F_y = q(v_zB_x-v_xB_z),\\
&F_z = q(v_xB_y-v_yB_x),\\
&1\,\mathrm T = 1\,\mathrm{N/(A\cdot m)}.
\end{aligned}`),variables:[
   String.raw`$F_x, F_y, F_z$: Các thành phần hình chiếu của lực từ theo ba trục tọa độ ($\mathrm{N}$)`,
   String.raw`$v_x, v_y, v_z$: Các thành phần vận tốc của hạt ($\mathrm{m/s}$)`,
   String.raw`$B_x, B_y, B_z$: Các thành phần vector cảm ứng từ ($\mathrm{T}$)`,
   String.raw`$1\,\mathrm{T}$: Đơn vị cảm ứng từ Tesla ($1\,\mathrm{T} = 1\,\mathrm{N/(A\cdot m)}$)`
  ],description:'Dùng hệ trục thuận tay phải. Thành phần có dấu, khác độ lớn lực không âm. Tesla là đơn vị từ trường.'}]},
 {id:'flux',title:'Từ thông và định luật Gauss cho từ trường',items:[
  {name:'Từ thông qua mặt phẳng',formula:d(String.raw`\begin{aligned}
&\Phi_B = \int\vec B\cdot d\vec A,\\
&\Phi_B = BA\cos\phi,\\
&1\,\mathrm{Wb} = 1\,\mathrm{T\cdot m^2}.
\end{aligned}`),variables:[
   String.raw`$\Phi_B$: Từ thông gửi qua diện tích bề mặt ($\mathrm{Wb}$ - Weber)`,
   String.raw`$B$: Độ lớn cảm ứng từ của từ trường đều ($\mathrm{T}$)`,
   String.raw`$A$: Diện tích của mặt phẳng nhận từ thông ($\mathrm{m^2}$)`,
   String.raw`$\phi$: Góc hợp bởi vector cảm ứng từ $\vec B$ và vector pháp tuyến của mặt ($\mathrm{rad}$ hoặc độ)`,
   String.raw`$1\,\mathrm{Wb}$: Đơn vị từ thông Weber ($1\,\mathrm{Wb} = 1\,\mathrm{T\cdot m^2}$)`
  ],description:'Mặt phẳng, B đều trên mặt, φ là góc giữa B và pháp tuyến mặt. Đơn vị là weber (Wb).'},
  {name:'Gauss cho từ trường',formula:d(String.raw`\oint\vec B\cdot d\vec A=0`),variables:[
   String.raw`$\vec B$: Vector cảm ứng từ của từ trường ($\mathrm{T}$)`,
   String.raw`$d\vec A$: Vector vi phân diện tích hướng ra ngoài mặt kín ($\mathrm{m^2}$)`
  ],description:'Mặt kín bất kỳ. Không tồn tại đơn cực từ cô lập. Các đường sức từ khép kín.'}]},
 {id:'circular-helical',title:'Chuyển động của hạt mang điện trong B đều',items:[
  {name:'Quỹ đạo tròn trong mặt phẳng vuông góc',formula:d(String.raw`\begin{aligned}
&R = \frac{mv}{|q|B},\\
&\omega = \frac{|q|B}{m},\\
&f = \frac{\omega}{2\pi}=\frac{|q|B}{2\pi m},\\
&T = \frac{2\pi}{\omega}=\frac{2\pi m}{|q|B}.
\end{aligned}`),variables:[
   String.raw`$R$: Bán kính quỹ đạo tròn của hạt trong từ trường đều ($\mathrm{m}$)`,
   String.raw`$m$: Khối lượng của hạt mang điện ($\mathrm{kg}$)`,
   String.raw`$v$: Tốc độ chuyển động của hạt trong mặt phẳng vuông góc với $\vec B$ ($\mathrm{m/s}$)`,
   String.raw`$\omega$: Tần số góc cyclotron của chuyển động xoay ($\mathrm{rad/s}$)`,
   String.raw`$T$: Chu kỳ quay một vòng của hạt ($\mathrm{s}$)`
  ],description:'Vận tốc ban đầu vuông góc với B. Chu kỳ và tần số không phụ thuộc tốc độ hay bán kính trong gần đúng không tương đối tính.'},
  {name:'Quỹ đạo xoắn ốc',formula:d(String.raw`\begin{aligned}
&v_\parallel = v\cos\phi,\quad v_\perp=v\sin\phi,\\
&R = \frac{mv_\perp}{|q|B},\\
&p = v_\parallel T = \frac{2\pi m v_\parallel}{|q|B}.
\end{aligned}`),variables:[
   String.raw`$v_\parallel$: Thành phần vận tốc song song với từ trường ($\mathrm{m/s}$)`,
   String.raw`$v_\perp$: Thành phần vận tốc vuông góc với từ trường ($\mathrm{m/s}$)`,
   String.raw`$p$: Bước của đường xoắn ốc dọc theo phương từ trường ($\mathrm{m}$)`
  ],description:'Vận tốc lập góc φ với B. Chuyển động gồm quay tròn bán kính R và tịnh tiến đều vận tốc v_song song dọc theo B.'}]},
 {id:'crossed-fields',title:'Trường chéo nhau và khối phổ',items:[
  {name:'Bộ chọn vận tốc',formula:d(String.raw`\begin{aligned}
&q\vec E+q\vec v\times\vec B = 0,\\
&v = \frac{E}{B}.
\end{aligned}`),variables:[
   String.raw`$v$: Tốc độ của hạt đi thẳng không bị lệch qua bộ chọn vận tốc ($\mathrm{m/s}$)`,
   String.raw`$E$: Cường độ điện trường giữa hai bản cực ($\mathrm{V/m}$)`,
   String.raw`$B$: Độ lớn cảm ứng từ của từ trường vuông góc với điện trường ($\mathrm{T}$)`
  ],description:'Điện trường E và từ trường B vuông góc nhau. Chỉ hạt có tốc độ v = E/B mới đi thẳng không bị lệch.'},
  {name:'Khối phổ sau bộ chọn vận tốc',formula:d(String.raw`\begin{aligned}
&R = \frac{mv}{|q|B'},\\
&\frac{m}{|q|} = \frac{BB'R}{E}.
\end{aligned}`),variables:[
   String.raw`$m/|q|$: Tỉ số giữa khối lượng và độ lớn điện tích của ion ($\mathrm{kg/C}$)`,
   String.raw`$R$: Bán kính quỹ đạo lệch của chùm ion trong buồng phân tích ($\mathrm{m}$)`,
   String.raw`$B'$: Cảm ứng từ trong buồng phân tích khối lượng ($\mathrm{T}$)`,
   String.raw`$B$: Cảm ứng từ trong buồng chọn vận tốc ($\mathrm{T}$)`
  ],description:'B là trường trong bộ chọn vận tốc, B\' là trường trong buồng phân tích. Phân tách các đồng vị theo bán kính R.'},
  {name:'Tỉ số điện tích và khối lượng của electron',formula:d(String.raw`\frac{e}{m} = \frac{E^2}{2VB^2}`),variables:[
   String.raw`$e/m$: Tỉ số độ lớn điện tích trên khối lượng của electron ($\mathrm{C/kg}$)`,
   String.raw`$V$: Hiệu điện thế gia tốc chùm electron ban đầu ($\mathrm{V}$)`
  ],description:'Thí nghiệm Thomson đo tỉ số e/m bằng cách kết hợp hiệu điện thế gia tốc V, điện trường E và từ trường B.'}]},
 {id:'current-force',title:'Lực từ lên dây dẫn',items:[
  {name:'Dây thẳng và phần tử dây',formula:d(String.raw`\begin{aligned}
&\vec F = I\vec l\times\vec B,\\
&F = IlB\sin\phi,\\
&d\vec F = I\,d\vec l\times\vec B.
\end{aligned}`),variables:[
   String.raw`$\vec F$: Vector lực từ tác dụng lên toàn đoạn dây thẳng ($\mathrm{N}$)`,
   String.raw`$I$: Cường độ dòng điện chạy trong dây dẫn ($\mathrm{A}$)`,
   String.raw`$\vec l$: Vector chiều dài đoạn dây dẫn có hướng theo chiều dòng điện ($\mathrm{m}$)`,
   String.raw`$d\vec l$: Vector phần tử độ dài vi phân dọc theo dây dẫn ($\mathrm{m}$)`,
   String.raw`$\phi$: Góc hợp bởi hướng dòng điện trong dây và vector cảm ứng từ $\vec B$ ($\mathrm{rad}$ hoặc độ)`
  ],description:'l là vector dài theo chiều dòng điện. B đều. Dây cong hoặc B không đều tích phân dF dọc theo dây.'},
  {name:'Dây cong hoặc trường không đều',formula:d(String.raw`\vec F=\int I\,d\vec l\times\vec B`),variables:[
   String.raw`$\vec F$: Tổng hợp lực từ tác dụng lên toàn bộ sợi dây cong ($\mathrm{N}$)`
  ],description:'Tích phân vector dọc theo toàn bộ chiều dài sợi dây. Vòng dây phẳng kín trong B đều có tổng lực bằng không.'}]},
 {id:'magnetic-dipole',title:'Vòng dây và mômen từ',items:[
  {name:'Mômen từ của vòng phẳng và cuộn',formula:d(String.raw`\begin{aligned}
&\vec\mu = I\vec A,\\
&\vec\mu = NI\vec A,\\
&\mu = NIA.
\end{aligned}`),variables:[
   String.raw`$\vec\mu$: Vector mômen từ của khung dây hoặc cuộn dây ($\mathrm{A\cdot m^2}$ hoặc $\mathrm{J/T}$)`,
   String.raw`$N$: Số vòng dây quấn cùng chiều (Không có đơn vị)`,
   String.raw`$I$: Cường độ dòng điện chạy trong khung dây ($\mathrm{A}$)`,
   String.raw`$\vec A$: Vector diện tích khung dây hướng theo quy tắc bàn tay phải ($\mathrm{m^2}$)`
  ],description:'N vòng, dòng I, diện tích A. Hướng của vector A xác định theo quy tắc nắm tay phải theo chiều dòng điện.'},
  {name:'Mômen lực',formula:d(String.raw`\begin{aligned}
&\vec\tau = \vec\mu\times\vec B,\\
&\tau = \mu B\sin\phi.
\end{aligned}`),variables:[
   String.raw`$\vec\tau$: Vector mômen lực từ làm quay khung dây ($\mathrm{N\cdot m}$)`,
   String.raw`$\phi$: Góc hợp bởi vector mômen từ $\vec\mu$ và vector cảm ứng từ $\vec B$ ($\mathrm{rad}$ hoặc độ)`
  ],description:'B đều. Mômen lực có xu hướng quay vòng sao cho μ cùng hướng với B.'}]},
 {id:'dipole-energy',title:'Thế năng lưỡng cực từ',items:[
  {name:'Thế năng và các vị trí cân bằng',formula:d(String.raw`\begin{aligned}
&U = -\vec\mu\cdot\vec B,\\
&U = -\mu B\cos\phi.
\end{aligned}`),variables:[
   String.raw`$U$: Thế năng tĩnh từ của lưỡng cực trong từ trường đều ($\mathrm{J}$)`,
   String.raw`$\mu$: Độ lớn mômen từ của lưỡng cực ($\mathrm{A\cdot m^2}$)`
  ],description:'φ = 0 (μ cùng hướng B): U_min = −μB, cân bằng bền. φ = π (μ ngược hướng B): U_max = +μB, cân bằng không bền.'},
  {name:'Công khi đổi hướng',formula:d(String.raw`\begin{aligned}&W_{\mathrm{ngoai}}=U_2-U_1\\&\quad=-\mu B(\cos\phi_2-\cos\phi_1).\end{aligned}`),variables:[
   String.raw`$W_{\mathrm{ngoai}}$: Ngoại công cần thực hiện để quay chậm lưỡng cực từ góc $\phi_1$ sang $\phi_2$ ($\mathrm{J}$)`
  ],description:'Công của ngoại lực làm quay lưỡng cực chậm từ góc φ₁ sang φ₂.'}]},
 {id:'dc-motor',title:'Động cơ điện một chiều',items:[
  {name:'Điện áp và công suất trong mô hình nối tiếp',formulaRows:[
   {label:'Điện áp hai cực khi rôto quay',formula:d(String.raw`V_{ab}=\mathcal E+Ir`)},
   {label:'Dòng điện qua phần ứng',formula:d(String.raw`I=\frac{V_{ab}-\mathcal E}{r}`)},
   {label:'Công suất điện tiêu thụ',formula:d(String.raw`P_{\mathrm{in}}=V_{ab}I`)},
   {label:'Công suất cơ sinh ra',formula:d(String.raw`P_{\mathrm{mech}}=\mathcal EI`)},
   {label:'Hao phí nhiệt trên cuộn dây',formula:d(String.raw`P_r=I^2r`)}
  ],variables:[
   String.raw`$V_{ab}$: Điện áp cung cấp từ nguồn vào hai đầu động cơ ($\mathrm{V}$)`,
   String.raw`$\mathcal E$: Suất phản điện động cảm ứng sinh ra khi rôto quay ($\mathrm{V}$)`,
   String.raw`$I$: Cường độ dòng điện qua cuộn dây phần ứng ($\mathrm{A}$)`,
   String.raw`$r$: Điện trở thuần của cuộn dây phần ứng ($\Omega$)`,
   String.raw`$P_{\mathrm{mech}}$: Công suất cơ học hữu ích do động cơ sinh ra ($\mathrm{W}$)`
  ],description:'ℰ là suất phản điện động tỉ lệ với tốc độ quay. Cổ góp đổi chiều dòng sau mỗi nửa vòng để mômen quay luôn cùng chiều.'},
  {name:'Rôto dừng trong mô hình nguồn cố định',formula:d(String.raw`\begin{aligned}
&\mathcal E_{\mathrm{dung}} = 0,\\
&I_{\mathrm{dung}} = \frac{V_{ab}}{r},\\
&P_{\mathrm{dung}} = I_{\mathrm{dung}}^2r.
\end{aligned}`),variables:[
   String.raw`$I_{\mathrm{dung}}$: Dòng điện khởi động hoặc khi rôto bị kẹt cứng ($I_{\mathrm{dung}} \gg I_{\mathrm{danh\ muc}}$) ($\mathrm{A}$)`
  ],description:'Khi mới khởi động hoặc khi bị kẹt rôto, ℰ = 0, dòng điện qua cuộn dây rất lớn, dễ gây cháy nếu không có bảo vệ.'}]},
 {id:'hall',title:'Hiệu ứng Hall',items:[
  {name:'Cân bằng ngang và mật độ hạt tải',formula:d(String.raw`\begin{aligned}
&qE_z + qv_xB_y = 0,\\
&E_z = -v_xB_y,\\
&J_x = nqv_x,\\
&nq = -\frac{J_xB_y}{E_z}.
\end{aligned}`),variables:[
   String.raw`$E_z$: Điện trường Hall đo theo phương ngang vuông góc ($\mathrm{V/m}$)`,
   String.raw`$v_x$: Vận tốc trôi định hướng của các hạt mang điện ($\mathrm{m/s}$)`,
   String.raw`$B_y$: Cảm ứng từ theo phương vuông góc với bản dải mẫu ($\mathrm{T}$)`,
   String.raw`$J_x$: Mật độ dòng điện dọc theo chiều dài của dải dẫn ($\mathrm{A/m^2}$)`,
   String.raw`$n$: Mật độ hạt tải điện trên một đơn vị thể tích ($\mathrm{m^{-3}}$)`
  ],description:'Lực từ cân bằng lực điện theo phương ngang. Dấu của Ez cho biết dấu của hạt tải (electron mang điện âm cho Ez ngược chiều so với hạt dương).'},
  {name:'Độ lớn điện áp Hall của dải dẫn',formula:d(String.raw`V_H=\frac{IB}{n|q|d}`),variables:[
   String.raw`$V_H$: Hiệu điện thế Hall đo giữa hai mép đối diện của dải mẫu ($\mathrm{V}$)`,
   String.raw`$I$: Cường độ dòng điện chạy dọc dải mẫu dẫn ($\mathrm{A}$)`,
   String.raw`$B$: Cảm ứng từ vuông góc với mặt phẳng dải mẫu ($\mathrm{T}$)`,
   String.raw`$d$: Chiều dày của dải mẫu theo phương của từ trường ($\mathrm{m}$)`
  ],description:'d là bề dày của dải theo phương từ trường B. Điện áp Hall tỉ lệ thuận với dòng I và trường B, tỉ lệ nghịch với mật độ hạt tải n.'}]}
]}
