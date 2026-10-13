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
\vec F&=q\vec v\times\vec B,\\
F&=|q|vB\sin\phi,\\
\vec F\cdot\vec v&=0.
\end{aligned}`),example:''},
 {note,title:'Đường sức từ biểu diễn trường và không chỉ hướng lực',bullets:['Tiếp tuyến của đường sức cho hướng từ trường tại điểm ấy.','Mật độ đường trong cùng bản đồ biểu thị tương đối độ mạnh của trường.','Đường sức không có nguồn hoặc điểm tận cùng. Các bản đồ nam châm khép qua cả bên trong nam châm.'],formula:d(String.raw`\oint\vec B\cdot d\vec A=0`),example:''},
 {note,title:'Dấu từ thông phụ thuộc pháp tuyến đã chọn',bullets:['Thành phần vuông góc mặt đóng góp vào từ thông.','Mặt kín dùng pháp tuyến hướng ra ngoài, mặt hở cần chọn một hướng nhất quán.','Công thức BA cosφ dùng mặt phẳng và từ trường đều trên mặt.'],formula:d(String.raw`\begin{aligned}
\Phi_B&=\int\vec B\cdot d\vec A,\\
\Phi_B&=BA\cos\phi,\\
1\,\mathrm{Wb}&=1\,\mathrm{T\cdot m^2}.
\end{aligned}`),example:''},
 {note,title:'Từ trường đều bẻ hướng hạt mà không đổi tốc độ',bullets:['Vận tốc vuông góc trường cho quỹ đạo tròn.','Thành phần song song trường giữ không đổi và tạo bước xoắn.','Các công thức dùng khối lượng không đổi trong mô hình không tương đối tính.'],formula:d(String.raw`\begin{aligned}
R&=\frac{mv_\perp}{|q|B},\\
\omega&=\frac{|q|B}{m},\\
T&=\frac{2\pi m}{|q|B},\\
p&=v_\parallel T.
\end{aligned}`),example:''},
 {note,title:'Bộ chọn vận tốc cân bằng hai lực',bullets:['Điện trường và từ trường được bố trí chéo nhau.','Chỉ vận tốc có hướng và độ lớn phù hợp mới đi thẳng qua vùng chọn.','Hạt nhanh hơn hoặc chậm hơn bị lệch theo các chiều khác nhau.'],formula:d(String.raw`\begin{aligned}
q\vec E+q\vec v\times\vec B&=0,\\
v&=E/B.
\end{aligned}`),example:''},
 {note,title:'Khối phổ dùng bán kính quỹ đạo để phân biệt hạt',bullets:['Sau bộ chọn vận tốc, các hạt có cùng tốc độ.','Trường phân tích bẻ quỹ đạo, bán kính phụ thuộc khối lượng trên độ lớn điện tích.','Hai bán kính khác nhau đưa các đồng vị đến các vị trí khác nhau.'],formula:d(String.raw`\begin{aligned}
R&=\frac{mv}{|q|B'},\\
\frac m{|q|}&=\frac{BB'R}{E}.
\end{aligned}`),example:''},
 {note,title:'Dòng điện trong dây chịu tổng lực của các hạt tải',bullets:['Vector chiều dài của dây hướng theo dòng quy ước.','Dây thẳng trong trường đều có thể dùng lực của cả đoạn.','Dây cong hoặc trường không đều cần cộng vector lực từng phần tử.'],formula:d(String.raw`\begin{aligned}
\vec F&=I\vec l\times\vec B,\\
d\vec F&=I\,d\vec l\times\vec B.
\end{aligned}`),example:''},
 {note,title:'Vòng dây trong trường đều có thể chịu mômen',bullets:['Các lực trên vòng kín triệt tiêu tổng, nhưng các đường tác dụng khác nhau có thể tạo mômen.','Quy tắc bàn tay phải cho hướng mômen từ theo chiều dòng.','Cuộn N vòng cùng hình học và hướng làm mômen từ tăng N lần.'],formula:d(String.raw`\begin{aligned}
\vec\mu&=NI\vec A,\\
\vec\tau&=\vec\mu\times\vec B.
\end{aligned}`),example:''},
 {note,title:'Năng lượng thấp nhất khi mômen từ cùng hướng trường',bullets:['Góc được tính giữa mômen từ và từ trường.','Cùng chiều là cân bằng bền, ngược chiều là cân bằng không bền.','Trong trường không đều, vòng còn có thể chịu lực tổng hướng về hoặc ra xa vùng trường mạnh.'],formula:d(String.raw`\begin{aligned}
U&=-\vec\mu\cdot\vec B,\\
U&=-\mu B\cos\phi.
\end{aligned}`),example:''},
 {note,title:'Động cơ chuyển điện năng thành cơ năng',bullets:['Cổ góp đổi chiều dòng trong vòng sau nửa vòng quay để duy trì chiều mômen.','Suất phản điện động tăng theo tốc độ khi cấu hình và từ trường giữ nguyên.','Rôto dừng làm suất phản điện động mất đi, nên dòng tăng mạnh trong mô hình nguồn và điện trở cố định.'],formula:d(String.raw`\begin{aligned}
V_{ab}&=\mathcal E+Ir,\\
P_{\mathrm{in}}&=V_{ab}I,\\
P_{\mathrm{mech}}&=\mathcal EI,\\
P_r&=I^2r.
\end{aligned}`),example:''},
 {note,title:'Hiệu ứng Hall tách điện tích theo phương ngang',bullets:['Lực từ dồn hạt tải về một mép và tạo điện trường ngang.','Ở cân bằng, lực điện ngang chống lại lực từ.','Cực tính Hall cho dấu hạt tải, còn độ lớn giúp suy mật độ trong mô hình thích hợp.'],formula:d(String.raw`\begin{aligned}
E_z&=-v_xB_y,\\
J_x&=nqv_x,\\
nq&=-\frac{J_xB_y}{E_z}.
\end{aligned}`),example:''}
]
export const magneticCheatsheet={summary:'Định nghĩa, tính chất và công thức của lực từ, từ thông, chuyển động hạt, vòng dây, động cơ và hiệu ứng Hall.',sections:[
 {id:'field-force',title:'Từ trường và lực từ',items:[
  {name:'Lực lên một hạt mang điện',formula:d(String.raw`\begin{aligned}
\vec F&=q\vec v\times\vec B,\\
F&=|q|vB\sin\phi,\\
\vec F\cdot\vec v&=0.
\end{aligned}`),description:'φ là góc giữa vận tốc và từ trường. Lực đổi chiều khi đổi dấu q hoặc đảo một trong hai vector. Lực từ không sinh công lên hạt và không làm thay đổi động năng nếu là lực duy nhất.'},
  {name:'Các thành phần lực và đơn vị',formula:d(String.raw`\begin{aligned}
F_x&=q(v_yB_z-v_zB_y),\\
F_y&=q(v_zB_x-v_xB_z),\\
F_z&=q(v_xB_y-v_yB_x),\\
1\,\mathrm T&=1\,\mathrm{N/(A\cdot m)}.
\end{aligned}`),description:'Dùng hệ trục thuận tay phải. Thành phần có dấu, khác độ lớn lực không âm. Tesla là đơn vị từ trường.'}]},
 {id:'flux',title:'Đường sức và từ thông',items:[
  {name:'Từ thông',formulaRows:[
   {label:'Một phần tử mặt',formula:d(String.raw`d\Phi_B=\vec B\cdot d\vec A`)},
   {label:'Mặt bất kỳ, trường có thể không đều',formula:d(String.raw`\Phi_B=\int\vec B\cdot d\vec A`)},
   {label:'Mặt phẳng trong trường đều',formula:d(String.raw`\Phi_B=BA\cos\phi`)},
   {label:'Đơn vị weber',formula:d(String.raw`1\,\mathrm{Wb}=1\,\mathrm{T\cdot m^2}`)}
  ],description:'φ là góc với pháp tuyến. Mặt hở cần chọn phía dương. Đổi pháp tuyến đảo dấu từ thông. Đường sức tiếp tuyến với B, không chỉ hướng lực lên hạt bất kỳ.'},
  {name:'Định luật Gauss đối với từ trường',formula:d(String.raw`\oint\vec B\cdot d\vec A=0`),description:'Áp dụng cho mặt kín, vector diện tích hướng ra ngoài. Không có nguồn hoặc điểm tận cùng của đường sức. Từ thông tổng bằng không không buộc B bằng không tại từng điểm.'}]},
 {id:'particle-motion',title:'Chuyển động trong từ trường đều',items:[
  {name:'Quỹ đạo tròn và đường xoắn ốc',formulaRows:[
   {label:'Bán kính từ thành phần vận tốc vuông góc',formula:d(String.raw`R=\frac{mv_\perp}{|q|B}`)},
   {label:'Tần số góc',formula:d(String.raw`\omega=|q|B/m`)},
   {label:'Chu kỳ',formula:d(String.raw`T=\frac{2\pi m}{|q|B}`)},
   {label:'Bước xoắn',formula:d(String.raw`p=v_\parallel T`)}
  ],description:'Hạt không tương đối tính, trường đều và chỉ có lực từ. v_⊥ và v_∥ là các thành phần tốc độ vuông góc và song song trường. Khi v_∥ bằng không, quỹ đạo là đường tròn.'},
  {name:'Lực hướng tâm và công suất lực từ',formula:d(String.raw`\begin{aligned}
|q|v_\perp B&=\frac{mv_\perp^2}{R},\\
P_F&=\vec F\cdot\vec v=0.
\end{aligned}`),description:'Lực từ thay đổi hướng vận tốc. Tốc độ và động năng giữ không đổi khi không có lực khác sinh công.'}]},
 {id:'particle-applications',title:'Trường chéo nhau và khối phổ',items:[
  {name:'Bộ chọn vận tốc',formula:d(String.raw`\begin{aligned}
\vec E+\vec v\times\vec B&=0,\\
v&=E/B.
\end{aligned}`),description:'q khác không. Công thức độ lớn dùng vận tốc vuông góc cả điện trường và từ trường, với chiều để hai lực đối nhau.'},
  {name:'Khối phổ sau bộ chọn vận tốc',formula:d(String.raw`\begin{aligned}
R&=\frac{mv}{|q|B'},\\
\frac m{|q|}&=\frac{BB'R}{E}.
\end{aligned}`),description:'B thuộc vùng chọn vận tốc, B′ thuộc vùng phân tích. Hạt có cùng tốc độ v = E/B. Trường phân tích vuông góc vận tốc và mô hình không tương đối tính.'},
  {name:'Tỉ số điện tích và khối lượng của electron',formula:d(String.raw`\begin{aligned}
\frac12mv^2&=eV,\\
v&=E/B,\\
\frac em&=\frac{E^2}{2VB^2}.
\end{aligned}`),description:'e là độ lớn điện tích electron. Electron được gia tốc từ nghỉ qua độ lớn hiệu điện thế V rồi qua vùng trường chéo nhau không bị lệch. Dùng mô hình không tương đối tính.'}]},
 {id:'wire-force',title:'Lực từ lên dây dẫn',items:[
  {name:'Dây thẳng và phần tử dây',formula:d(String.raw`\begin{aligned}
\vec F&=I\vec l\times\vec B,\\
F&=IlB\sin\phi,\\
d\vec F&=I\,d\vec l\times\vec B.
\end{aligned}`),description:'Vector chiều dài và phần tử dây hướng theo dòng quy ước. Công thức cả đoạn dùng dây thẳng trong trường đều. I là đại lượng vô hướng.'},
  {name:'Dây cong hoặc trường không đều',formula:d(String.raw`\vec F=\int I\,d\vec l\times\vec B`),description:'Lấy từ trường tại từng phần tử và cộng vector. Với dòng không đổi trong trường đều, lực cả dây phụ thuộc vector nối đầu vào và đầu ra. Vòng kín trong trường đều có tổng lực bằng không.'}]},
 {id:'dipole-torque',title:'Vòng dây và mômen từ',items:[
  {name:'Mômen từ của vòng phẳng và cuộn',formula:d(String.raw`\begin{aligned}
\vec\mu_1&=I\vec A,\\
\vec\mu_N&=NI\vec A.
\end{aligned}`),description:'Vector diện tích hướng theo quy tắc bàn tay phải khi khum ngón theo chiều dòng. Cuộn N vòng dùng các vòng cùng diện tích và hướng. Đơn vị mômen từ là A·m².'},
  {name:'Mômen lực',formula:d(String.raw`\begin{aligned}
\vec\tau&=\vec\mu\times\vec B,\\
\tau&=\mu B\sin\phi,\\
\tau_N&=NIAB\sin\phi.
\end{aligned}`),description:'φ là góc giữa mômen từ và trường. Trong trường đều, tổng lực vòng kín bằng không nhưng mômen có thể khác không. Mômen từ không phải mômen lực.'}]},
 {id:'dipole-energy',title:'Thế năng lưỡng cực từ',items:[
  {name:'Thế năng và các vị trí cân bằng',formula:d(String.raw`\begin{aligned}
U&=-\vec\mu\cdot\vec B\\
&=-\mu B\cos\phi,\\
U_{\min}&=-\mu B,\\
U_{\max}&=+\mu B.
\end{aligned}`),description:'Mốc U = 0 khi mômen vuông góc trường. Cùng chiều là cân bằng bền, ngược chiều là cân bằng không bền. Dùng mômen từ và trường giữ độ lớn cố định khi xét góc.'},
  {name:'Công khi đổi hướng',formula:d(String.raw`\begin{aligned}
\Delta U&=-\mu B\cos\phi_f\\
&\quad+\mu B\cos\phi_i,\\
W_B&=-\Delta U.
\end{aligned}`),description:'Dùng trường không đổi và cùng độ lớn mômen từ. Công của mômen từ bằng âm biến thiên thế năng theo quy ước đã chọn.'}]},
 {id:'motor',title:'Động cơ điện một chiều',items:[
  {name:'Điện áp và công suất trong mô hình nối tiếp',formulaRows:[
   {label:'Điện áp hai cực',formula:d(String.raw`V_{ab}=\mathcal E+Ir`)},
   {label:'Công suất điện vào',formula:d(String.raw`P_{\mathrm{in}}=V_{ab}I`)},
   {label:'Công suất nhiệt trong cuộn',formula:d(String.raw`P_r=I^2r`)},
   {label:'Công suất cơ phát triển',formula:d(String.raw`P_{\mathrm{mech}}=\mathcal EI`)},
   {label:'Hiệu suất khi chỉ có tổn hao điện trở',formula:d(String.raw`\eta=\frac{\mathcal E}{V_{ab}}`)}
  ],description:'r là tổng điện trở của mạch động cơ nối tiếp. ℰ là suất phản điện động. Công suất cơ và hiệu suất ở đây bỏ qua các tổn hao khác.'},
  {name:'Rôto dừng trong mô hình nguồn cố định',formula:d(String.raw`\begin{aligned}
\mathcal E&=0,\\
I_{\mathrm{stall}}&=V_{ab}/r.
\end{aligned}`),description:'Suất phản điện động tỉ lệ tốc độ khi từ trường và cấu hình giữ nguyên. Cổ góp đảo dòng trong rôto để duy trì chiều mômen trong cấu hình động cơ đã xét.'}]},
 {id:'hall',title:'Hiệu ứng Hall',items:[
  {name:'Cân bằng ngang và mật độ hạt tải',formula:d(String.raw`\begin{aligned}
E_z&=-v_xB_y,\\
J_x&=nqv_x,\\
nq&=-\frac{J_xB_y}{E_z}.
\end{aligned}`),description:'Các thành phần có dấu theo cùng hệ trục. q âm cho electron, dương cho hạt tải dương. Dùng một loại hạt tải trong mô hình phù hợp. Điện áp Hall có cực tính phụ thuộc dấu hạt tải.'},
  {name:'Độ lớn điện áp Hall của dải dẫn',formula:d(String.raw`|V_H|=\frac{IB}{n|q|t}`),description:'Dòng và trường vuông góc, t là bề dày mẫu theo phương từ trường. Cân bằng lực ngang trong trạng thái ổn định. Quan hệ không tự mô tả đầy đủ vật liệu có nhiều loại hạt tải hoặc hiệu ứng lượng tử đáng kể.'}]}
]}
