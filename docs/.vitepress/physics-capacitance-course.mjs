const note='04-tu-dien-dien-moi'
const d=tex=>'$$\n'+tex+'\n$$'
export const capacitanceTopics=[
 {title:'Cấu trúc, cách mắc và năng lượng',topics:[
  {slug:'tu-dien-dien-dung',title:'Tụ điện và điện dung',question:'Hình học của hai vật dẫn quyết định điện dung như thế nào?',source:'24.1'},
  {slug:'mac-tu-dien',title:'Tụ mắc nối tiếp và song song',question:'Đại lượng nào được giữ chung trong mỗi cách mắc?',source:'24.2'},
  {slug:'nang-luong-tu-dien',title:'Năng lượng của tụ và điện trường',question:'Công nạp điện được tích trữ ở đâu?',source:'24.3'}]},
 {title:'Điện môi và phân cực',topics:[
  {slug:'dien-moi',title:'Điện môi',question:'Vì sao thêm chất cách điện có thể làm điện dung tăng?',source:'24.4'},
  {slug:'mo-hinh-phan-tu',title:'Mô hình phân tử của điện tích cảm ứng',question:'Điện tích liên kết xuất hiện từ sự sắp xếp nào của các phân tử?',source:'24.5'},
  {slug:'gauss-trong-dien-moi',title:'Định luật Gauss trong điện môi',question:'Gauss đếm điện tích tự do và điện tích liên kết ra sao?',source:'24.6'}]}
]
export const capacitanceSlides=[
 {note,title:'Điện dung thuộc cấu hình của hai vật dẫn',bullets:['Điện tích Q là độ lớn trên từng bản. Tổng điện tích của hai bản ±Q bằng không.','Hiệu điện thế được lấy từ bản dương đến bản âm.','Với hình học và điện môi tuyến tính giữ nguyên, tăng Q làm V tăng cùng tỉ lệ.'],formula:d(String.raw`\begin{aligned}
C&=\frac{Q}{V_{ab}},\\
1\,\mathrm F&=1\,\mathrm{C/V}.
\end{aligned}`),example:''},
 {note,title:'Tìm điện dung bằng trường và hiệu điện thế',bullets:['Giả sử hai vật dẫn mang ±Q, dùng đối xứng tìm điện trường.','Tích phân trường từ bản dương đến bản âm để tính hiệu điện thế.','Trong tụ phẳng, chỉ bỏ hiệu ứng mép khi khe nhỏ so với kích thước bản.'],formula:d(String.raw`\begin{aligned}
V_{ab}&=\int_a^b\vec E\cdot d\vec\ell,\\
C_0&=\frac{\varepsilon_0 A}{d}.
\end{aligned}`),example:''},
 {note,title:'Nối tiếp giữ cùng điện tích, song song giữ cùng điện áp',bullets:['Chuỗi tụ bắt đầu chưa nạp có các nút giữa trung hòa và cô lập.','Ở chuỗi ấy, độ lớn điện tích trên mọi tụ bằng nhau và các điện áp cộng.','Các nhánh song song nối cùng hai nút nên có cùng điện áp.'],formula:d(String.raw`\begin{aligned}
\frac1{C_s}&=\frac1{C_1}+\frac1{C_2}+\frac1{C_3},\\
C_p&=C_1+C_2+C_3.
\end{aligned}`),example:''},
 {note,title:'Công nạp tích trữ thành năng lượng điện trường',bullets:['Điện áp tăng dần trong quá trình nạp nên công không bằng Q nhân điện áp cuối.','Ba biểu thức năng lượng là các cách viết tương đương cho tụ tuyến tính.','Năng lượng điện trường và thế năng của tụ là cùng một năng lượng.'],formula:d(String.raw`\begin{aligned}
U&=\frac{Q^2}{2C}=\frac12 CV^2,\\
U&=\frac12 QV,\\
u_0&=\frac12\varepsilon_0 E^2.
\end{aligned}`),example:''},
 {note,title:'Điện môi tăng điện dung nhờ sự phân cực',bullets:['Điện tích liên kết trên mặt điện môi tạo trường chống lại trường của các bản.','Điện môi tuyến tính đồng nhất lấp toàn khe làm điện dung tăng K lần.','Giữ điện tích tự do thì trường và điện áp giảm K lần.'],formula:d(String.raw`\begin{aligned}
\varepsilon&=K\varepsilon_0,\\
C&=KC_0,\\
E&=E_0/K,\quad Q=Q_0.
\end{aligned}`),example:''},
 {note,title:'Phân cực ở mức phân tử không làm điện tích chảy tự do',bullets:['Phân tử không phân cực bị tách tương đối các tâm điện tích trong trường.','Phân tử phân cực có lưỡng cực thường trực và chịu mômen định hướng.','Trong vật liệu trung hòa, các điện tích liên kết trong thể tích có thể bù nhau, còn ở mặt ngoài thì không.'],formula:d(String.raw`\begin{aligned}
\vec\tau&=\vec p\times\vec E,\\
U_{\mathrm{dipole}}&=-\vec p\cdot\vec E.
\end{aligned}`),example:''},
 {note,title:'Điều kiện nối nguồn quyết định năng lượng sau khi thêm điện môi',bullets:['Ngắt nguồn giữ điện tích tự do, vì các bản không trao đổi điện tích với nguồn.','Giữ nguồn lý tưởng thì điện áp giữ nguyên và nguồn chuyển thêm điện tích.','Độ bền điện môi đặt giới hạn trường mà mô hình cách điện còn dùng được.'],formula:d(String.raw`\begin{aligned}
U_Q&=U_0/K,\quad Q=Q_0,\\
U_V&=KU_0,\quad V=V_0.
\end{aligned}`),example:''},
 {note,title:'Gauss cải biên chỉ đếm điện tích tự do',bullets:['Điện trường thực đã bao gồm tác dụng của điện tích tự do và điện tích liên kết.','Dạng cải biên giữ K trong tích phân nếu vật liệu thay đổi trên mặt Gauss.','Mật độ năng lượng trong điện môi dùng điện trường thực và độ điện thẩm của vật liệu.'],formula:d(String.raw`\begin{aligned}
\oint_S K\vec E\cdot d\vec A&=\frac{Q_{\mathrm{free}}}{\varepsilon_0},\\
u&=\frac12\varepsilon E^2.
\end{aligned}`),example:''}
]
export const capacitanceCheatsheet={summary:'Định nghĩa, tính chất và công thức của tụ điện, mạng tụ, năng lượng và điện môi.',sections:[
 {id:'definition',title:'Điện dung và hình học',items:[
  {name:'Định nghĩa điện dung',formulaRows:[
   {label:'Điện dung của hai vật dẫn mang ±Q',formula:d(String.raw`C=\frac{Q}{V_{ab}}`)},
   {label:'Đơn vị SI',formula:d(String.raw`1\,\mathrm F=1\,\mathrm{C/V}`)}
  ],description:'Q là độ lớn điện tích trên một bản, V_ab là điện thế bản dương trừ điện thế bản âm. Tỉ số không đổi khi hình học và đáp ứng điện môi tuyến tính giữ nguyên.'},
  {name:'Tụ phẳng, tụ cầu và tụ trụ',formulaRows:[
   {label:'Hai bản phẳng, chân không',formula:d(String.raw`C_0=\frac{\varepsilon_0 A}{d}`)},
   {label:'Hai mặt cầu đồng tâm, a < b',formula:d(String.raw`C_0=4\pi\varepsilon_0\frac{ab}{b-a}`)},
   {label:'Cầu cô lập bán kính R, mốc ở vô hạn',formula:d(String.raw`C_0=4\pi\varepsilon_0 R`)},
   {label:'Hai trụ đồng trục dài L, a < b',formula:d(String.raw`C_0=\frac{2\pi\varepsilon_0L}{\ln(b/a)}`)}
  ],description:'Tụ phẳng bỏ hiệu ứng mép khi d nhỏ so với kích thước bản. Tụ trụ bỏ hiệu ứng ở hai đầu khi chiều dài đủ lớn. a,b là bán kính hai mặt dẫn đối diện. Điện môi đồng nhất lấp toàn khe làm mỗi điện dung tăng K lần.'}]},
 {id:'network',title:'Mạng tụ',items:[
  {name:'Nối tiếp',formula:d(String.raw`\begin{aligned}
\frac1{C_s}&=\frac1{C_1}+\frac1{C_2}+\frac1{C_3},\\
\frac1{C_s}&=\sum_{i=1}^{n}\frac1{C_i},\\
V&=V_1+V_2+\cdots+V_n,\\
Q_1&=Q_2=\cdots=Q_n.
\end{aligned}`),description:'Chỉ số i chạy từ 1 đến n. Quy tắc cùng độ lớn điện tích dùng cho các nút trung gian trung hòa, cô lập. Điện dung tương đương nhỏ hơn từng điện dung thành phần dương.'},
  {name:'Song song',formula:d(String.raw`\begin{aligned}
C_p&=C_1+C_2+C_3,\\
C_p&=\sum_{i=1}^{n}C_i,\\
Q&=Q_1+Q_2+\cdots+Q_n,\\
V_1&=V_2=\cdots=V_n.
\end{aligned}`),description:'Chỉ số i chạy từ 1 đến n. Các tụ nối cùng hai nút. Q là tổng điện tích trên các bản nối cùng một cực, không phải tổng đại số điện tích cả hai phía của mạng.'},
  {name:'Hai tụ',formulaRows:[
   {label:'Điện dung nối tiếp',formula:d(String.raw`C_s=\frac{C_1C_2}{C_1+C_2}`)},
   {label:'Điện dung song song',formula:d(String.raw`C_p=C_1+C_2`)}
  ],description:'C₁,C₂ dương. Trong chuỗi có nút giữa trung hòa, điện áp tỉ lệ nghịch điện dung và điện tích trên hai tụ có cùng độ lớn.'}]},
 {id:'energy',title:'Năng lượng và lực',items:[
  {name:'Tụ tuyến tính',formulaRows:[
   {label:'Theo điện tích và điện dung',formula:d(String.raw`U=\frac{Q^2}{2C}`)},
   {label:'Theo điện áp và điện dung',formula:d(String.raw`U=\frac12 CV^2`)},
   {label:'Theo điện tích và điện áp',formula:d(String.raw`U=\frac12 QV`)}
  ],description:'Các công thức biểu diễn cùng một năng lượng. Công nạp thuận nghịch từ trạng thái không tích điện bằng U. Khi nối lại các tụ đã nạp, điện tích của từng nhóm vật dẫn cô lập được bảo toàn, còn năng lượng điện trường có thể chuyển sang nhiệt và bức xạ.'},
  {name:'Mật độ năng lượng',formulaRows:[
   {label:'Chân không',formula:d(String.raw`u_0=\frac12\varepsilon_0 E^2`)},
   {label:'Điện môi tuyến tính đẳng hướng',formula:d(String.raw`u=\frac12\varepsilon E^2`)},
   {label:'Năng lượng trong một vùng không gian',formula:d(String.raw`U=\int_{\mathcal V}u\,d\mathcal V`)}
  ],description:'u đo bằng J/m³. E là trường thực tại từng điểm. Với trường đều trong khe tụ phẳng, U = uAd.'},
  {name:'Lực hút giữa hai bản tụ phẳng',formulaRows:[
   {label:'Độ lớn lực hút, bỏ hiệu ứng mép',formula:d(String.raw`F=\frac{Q^2}{2\varepsilon A}`)},
   {label:'Áp suất điện lên bản',formula:d(String.raw`\frac{F}{A}=\frac12\varepsilon E^2`)}
  ],description:'Điện môi đồng nhất tuyến tính lấp toàn khe, hai bản đối diện có cùng diện tích A. E là trường tổng trong khe, còn lực lên một bản do trường của bản kia gây ra.'}]},
 {id:'dielectric',title:'Điện môi và giới hạn cách điện',items:[
  {name:'Hằng số điện môi và độ điện thẩm',formula:d(String.raw`\begin{aligned}
K&=C/C_0,\\
\varepsilon&=K\varepsilon_0,\\
C&=\varepsilon A/d.
\end{aligned}`),description:'K không có đơn vị, ε có đơn vị F/m. Quan hệ C = KC₀ cần điện môi tuyến tính đồng nhất lấp toàn vùng giữa các vật dẫn. Công thức cuối dùng cho tụ phẳng bỏ hiệu ứng mép.'},
  {name:'Tụ cô lập, điện môi lấp toàn khe',formula:d(String.raw`\begin{aligned}
Q&=Q_0,\\
E&=E_0/K,\\
V&=V_0/K,\\
U&=U_0/K.
\end{aligned}`),description:'Các bản đã ngắt nguồn và không rò điện. Hình học giữ nguyên, C = KC₀.'},
  {name:'Tụ giữ nối nguồn điện áp',formula:d(String.raw`\begin{aligned}
V&=V_0,\\
E&=E_0,\\
Q&=KQ_0,\\
U&=KU_0.
\end{aligned}`),description:'Nguồn lý tưởng giữ điện áp. Điện môi lấp toàn khe, hình học giữ nguyên. E = V/d áp dụng vùng gần đều của tụ phẳng.'},
  {name:'Điện tích liên kết trên mặt',formula:d(String.raw`\begin{aligned}
Q_i&=Q(1-1/K),\\
\sigma_i&=\sigma(1-1/K).
\end{aligned}`),description:'Các ký hiệu là độ lớn trong mô hình hai bản phẳng. Q và σ là điện tích tự do và mật độ tự do thực sau khi thêm điện môi. Mặt điện môi gần bản dương có điện tích liên kết âm, mặt còn lại mang dương.'},
  {name:'Độ bền điện môi',formula:d(String.raw`\begin{aligned}
E&<E_{\mathrm{bd}},\\
V_{\max}&=E_{\mathrm{bd}}d.
\end{aligned}`),description:'E_bd là ngưỡng đánh thủng, đo bằng V/m. Công thức điện áp dùng trường đều. Hằng số điện môi K và độ bền điện môi là hai đại lượng khác nhau.'}]},
 {id:'gauss',title:'Gauss và mô hình phân tử',items:[
  {name:'Gauss viết theo điện tích tự do',formulaRows:[
   {label:'Dạng có K',formula:d(String.raw`\oint_S K\vec E\cdot d\vec A=\frac{Q_{\mathrm{free}}}{\varepsilon_0}`)},
   {label:'Dạng có độ điện thẩm',formula:d(String.raw`\oint_S\varepsilon\vec E\cdot d\vec A=Q_{\mathrm{free}}`)}
  ],description:'S kín, vector diện tích hướng ra ngoài. Điện trường là trường thực, vế phải chỉ đếm điện tích tự do. Giữ K hoặc ε trong tích phân nếu chúng thay đổi trên mặt.'},
  {name:'Gauss viết theo toàn bộ điện tích',formula:d(String.raw`\begin{aligned}
\oint_S\vec E\cdot d\vec A&=\frac{Q_{\mathrm{total}}}{\varepsilon_0},\\
Q_{\mathrm{total}}&=Q_{\mathrm{free}}+Q_{\mathrm{bound}}.
\end{aligned}`),description:'Điện tích liên kết được cộng với dấu. Không đồng thời dùng ε thay ε₀ và cộng điện tích liên kết ở vế phải của dạng cải biên.'},
  {name:'Lưỡng cực phân tử trong trường',formula:d(String.raw`\begin{aligned}
\vec\tau&=\vec p\times\vec E,\\
U&=-\vec p\cdot\vec E.
\end{aligned}`),description:'Mômen lưỡng cực hướng từ điện tích âm sang điện tích dương. Phân tử phân cực có lưỡng cực thường trực, phân tử không phân cực có thể bị cảm ứng lưỡng cực. Chuyển động nhiệt cản sự định hướng.'}]}
]}
