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
&C = \frac{Q}{V_{ab}},\\
&1\,\mathrm F = 1\,\mathrm{C/V}.
\end{aligned}`),example:''},
 {note,title:'Tìm điện dung bằng trường và hiệu điện thế',bullets:['Giả sử hai vật dẫn mang ±Q, dùng đối xứng tìm điện trường.','Tích phân trường từ bản dương đến bản âm để tính hiệu điện thế.','Trong tụ phẳng, chỉ bỏ hiệu ứng mép khi khe nhỏ so với kích thước bản.'],formula:d(String.raw`\begin{aligned}
&V_{ab} = \int_a^b\vec E\cdot d\vec\ell,\\
&C_0 = \frac{\varepsilon_0 A}{d}.
\end{aligned}`),example:''},
 {note,title:'Nối tiếp giữ cùng điện tích, song song giữ cùng điện áp',bullets:['Chuỗi tụ bắt đầu chưa nạp có các nút giữa trung hòa và cô lập.','Ở chuỗi ấy, độ lớn điện tích trên mọi tụ bằng nhau và các điện áp cộng.','Các nhánh song song nối cùng hai nút nên có cùng điện áp.'],formula:d(String.raw`\begin{aligned}
&\frac1{C_s} = \frac1{C_1}+\frac1{C_2}+\frac1{C_3},\\
&C_p = C_1+C_2+C_3.
\end{aligned}`),example:''},
 {note,title:'Công nạp tích trữ thành năng lượng điện trường',bullets:['Điện áp tăng dần trong quá trình nạp nên công không bằng Q nhân điện áp cuối.','Ba biểu thức năng lượng là các cách viết tương đương cho tụ tuyến tính.','Năng lượng điện trường và thế năng của tụ là cùng một năng lượng.'],formula:d(String.raw`\begin{aligned}
&U = \frac{Q^2}{2C}=\frac12 CV^2,\\
&U = \frac12 QV,\\
&u_0 = \frac12\varepsilon_0 E^2.
\end{aligned}`),example:''},
 {note,title:'Điện môi tăng điện dung nhờ sự phân cực',bullets:['Điện tích liên kết trên mặt điện môi tạo trường chống lại trường của các bản.','Điện môi tuyến tính đồng nhất lấp toàn khe làm điện dung tăng K lần.','Giữ điện tích tự do thì trường và điện áp giảm K lần.'],formula:d(String.raw`\begin{aligned}
&\varepsilon = K\varepsilon_0,\\
&C = KC_0,\\
&E = E_0/K,\quad Q=Q_0.
\end{aligned}`),example:''},
 {note,title:'Phân cực ở mức phân tử không làm điện tích chảy tự do',bullets:['Phân tử không phân cực bị tách tương đối các tâm điện tích trong trường.','Phân tử phân cực có lưỡng cực thường trực và chịu mômen định hướng.','Trong vật liệu trung hòa, các điện tích liên kết trong thể tích có thể bù nhau, còn ở mặt ngoài thì không.'],formula:d(String.raw`\begin{aligned}
&\vec\tau = \vec p\times\vec E,\\
&U_{\mathrm{dipole}} = -\vec p\cdot\vec E.
\end{aligned}`),example:''},
 {note,title:'Điều kiện nối nguồn quyết định năng lượng sau khi thêm điện môi',bullets:['Ngắt nguồn giữ điện tích tự do, vì các bản không trao đổi điện tích với nguồn.','Giữ nguồn lý tưởng thì điện áp giữ nguyên và nguồn chuyển thêm điện tích.','Độ bền điện môi đặt giới hạn trường mà mô hình cách điện còn dùng được.'],formula:d(String.raw`\begin{aligned}
&U_Q = U_0/K,\quad Q=Q_0,\\
&U_V = KU_0,\quad V=V_0.
\end{aligned}`),example:''},
 {note,title:'Gauss cải biên chỉ đếm điện tích tự do',bullets:['Điện trường thực đã bao gồm tác dụng của điện tích tự do và điện tích liên kết.','Dạng cải biên giữ K trong tích phân nếu vật liệu thay đổi trên mặt Gauss.','Mật độ năng lượng trong điện môi dùng điện trường thực và độ điện thẩm của vật liệu.'],formula:d(String.raw`\begin{aligned}
&\oint_S K\vec E\cdot d\vec A = \frac{Q_{\mathrm{free}}}{\varepsilon_0},\\
&u = \frac12\varepsilon E^2.
\end{aligned}`),example:''}
]
export const capacitanceCheatsheet={summary:'Định nghĩa, tính chất và công thức của tụ điện, mạng tụ, năng lượng và điện môi.',sections:[
 {id:'definition',title:'Điện dung và hình học',items:[
  {name:'Định nghĩa điện dung',formulaRows:[
   {label:'Điện dung của hai vật dẫn mang ±Q',formula:d(String.raw`C=\frac{Q}{V_{ab}}`)},
   {label:'Đơn vị SI',formula:d(String.raw`1\,\mathrm F=1\,\mathrm{C/V}`)}
  ],variables:[
   String.raw`$C$: Điện dung của tụ điện gồm hai vật dẫn mang điện tích đối xứng ($\mathrm{F}$ - Farad)`,
   String.raw`$Q$: Độ lớn điện tích trên mỗi bản tụ ($\mathrm{C}$)`,
   String.raw`$V_{ab}$: Hiệu điện thế giữa bản dương và bản âm ($V_a - V_b$) ($\mathrm{V}$)`,
   String.raw`$1\,\mathrm{F}$: Đơn vị điện dung Farad ($1\,\mathrm{F} = 1\,\mathrm{C/V}$)`
  ],description:'Q là độ lớn điện tích trên một bản, V_ab là điện thế bản dương trừ điện thế bản âm. Tỉ số không đổi khi hình học và đáp ứng điện môi tuyến tính giữ nguyên.'},
  {name:'Tụ phẳng, tụ cầu và tụ trụ',formulaRows:[
   {label:'Hai bản phẳng, chân không',formula:d(String.raw`C_0=\frac{\varepsilon_0 A}{d}`)},
   {label:'Hai mặt cầu đồng tâm, a < b',formula:d(String.raw`C_0=4\pi\varepsilon_0\frac{ab}{b-a}`)},
   {label:'Cầu cô lập bán kính R, mốc ở vô hạn',formula:d(String.raw`C_0=4\pi\varepsilon_0 R`)},
   {label:'Hai trụ đồng trục dài L, a < b',formula:d(String.raw`C_0=\frac{2\pi\varepsilon_0L}{\ln(b/a)}`)}
  ],variables:[
   String.raw`$C_0$: Điện dung của tụ điện khi khe giữa hai bản là chân không ($\mathrm{F}$)`,
   String.raw`$A$: Diện tích đối diện của mỗi bản tụ phẳng ($\mathrm{m^2}$)`,
   String.raw`$d$: Khoảng cách giữa hai bản tụ phẳng ($\mathrm{m}$)`,
   String.raw`$a, b$: Bán kính của mặt dẫn bên trong và bên ngoài ($a < b$) ($\mathrm{m}$)`,
   String.raw`$R$: Bán kính của quả cầu dẫn cô lập trong không gian ($\mathrm{m}$)`,
   String.raw`$L$: Chiều dài của hai ống dẫn hình trụ đồng trục ($L \gg b$) ($\mathrm{m}$)`
  ],description:'Tụ phẳng bỏ hiệu ứng mép khi d nhỏ so với kích thước bản. Tụ trụ bỏ hiệu ứng ở hai đầu khi chiều dài đủ lớn. a,b là bán kính hai mặt dẫn đối diện. Điện môi đồng nhất lấp toàn khe làm mỗi điện dung tăng K lần.'}]},
 {id:'network',title:'Mạng tụ',items:[
  {name:'Nối tiếp',formula:d(String.raw`\begin{aligned}
&\frac1{C_s} = \frac1{C_1}+\frac1{C_2}+\frac1{C_3},\\
&\frac1{C_s} = \sum_{i=1}^{n}\frac1{C_i},\\
&V = V_1+V_2+\cdots+V_n,\\
&Q_1 = Q_2=\cdots=Q_n.
\end{aligned}`),variables:[
   String.raw`$C_s$: Điện dung tương đương của bộ tụ ghép nối tiếp ($\mathrm{F}$)`,
   String.raw`$C_i$: Điện dung của tụ điện thành phần thứ $i$ ($\mathrm{F}$)`,
   String.raw`$V$: Hiệu điện thế tổng đặt vào hai đầu bộ tụ nối tiếp ($\mathrm{V}$)`,
   String.raw`$V_i$: Hiệu điện thế trên từng tụ thành phần ($\mathrm{V}$)`,
   String.raw`$Q_i$: Độ lớn điện tích tích lũy trên mỗi tụ thành phần ($\mathrm{C}$)`
  ],description:'Chỉ số i chạy từ 1 đến n. Quy tắc cùng độ lớn điện tích dùng cho các nút trung gian trung hòa, cô lập. Điện dung tương đương nhỏ hơn từng điện dung thành phần dương.'},
  {name:'Song song',formula:d(String.raw`\begin{aligned}
&C_p = C_1+C_2+C_3,\\
&C_p = \sum_{i=1}^{n}C_i,\\
&Q = Q_1+Q_2+\cdots+Q_n,\\
&V_1 = V_2=\cdots=V_n.
\end{aligned}`),variables:[
   String.raw`$C_p$: Điện dung tương đương của bộ tụ ghép song song ($\mathrm{F}$)`,
   String.raw`$Q$: Tổng điện tích trên các bản cùng cực của bộ tụ song song ($\mathrm{C}$)`,
   String.raw`$V$: Hiệu điện thế chung giữa hai nút của các nhánh song song ($\mathrm{V}$)`
  ],description:'Chỉ số i chạy từ 1 đến n. Các tụ nối cùng hai nút. Q là tổng điện tích trên các bản nối cùng một cực, không phải tổng đại số điện tích cả hai phía của mạng.'},
  {name:'Hai tụ',formulaRows:[
   {label:'Điện dung nối tiếp',formula:d(String.raw`C_s=\frac{C_1C_2}{C_1+C_2}`)},
   {label:'Điện dung song song',formula:d(String.raw`C_p=C_1+C_2`)}
  ],variables:[
   String.raw`$C_s$: Điện dung tương đương khi mắc nối tiếp hai tụ điện $C_1$ và $C_2$ ($\mathrm{F}$)`,
   String.raw`$C_p$: Điện dung tương đương khi mắc song song hai tụ điện $C_1$ và $C_2$ ($\mathrm{F}$)`
  ],description:'C₁,C₂ dương. Trong chuỗi có nút giữa trung hòa, điện áp tỉ lệ nghịch điện dung và điện tích trên hai tụ có cùng độ lớn.'}]},
 {id:'energy',title:'Năng lượng và lực',items:[
  {name:'Tụ tuyến tính',formulaRows:[
   {label:'Theo điện tích và điện dung',formula:d(String.raw`U=\frac{Q^2}{2C}`)},
   {label:'Theo điện dung và điện áp',formula:d(String.raw`U=\tfrac12 CV^2`)},
   {label:'Theo điện tích và điện áp',formula:d(String.raw`U=\tfrac12 QV`)}
  ],variables:[
   String.raw`$U$: Năng lượng tĩnh điện tích lũy trong tụ điện ($\mathrm{J}$)`,
   String.raw`$Q$: Điện tích của bản tụ điện ($\mathrm{C}$)`,
   String.raw`$C$: Điện dung của tụ điện ($\mathrm{F}$)`,
   String.raw`$V$: Hiệu điện thế giữa hai bản tụ điện ($\mathrm{V}$)`
  ],description:'Ba công thức cho cùng kết quả khi quan hệ Q = CV tuyến tính. Năng lượng tính bằng joule.'},
  {name:'Mật độ năng lượng',formulaRows:[
   {label:'Trong chân không',formula:d(String.raw`u_0=\tfrac12\varepsilon_0 E^2`)},
   {label:'Trong điện môi tuyến tính',formula:d(String.raw`u=\tfrac12\varepsilon E^2`)},
   {label:'Theo hằng số điện môi',formula:d(String.raw`u=\tfrac12 K\varepsilon_0 E^2`)}
  ],variables:[
   String.raw`$u_0$: Mật độ năng lượng điện trường trong chân không ($\mathrm{J/m^3}$)`,
   String.raw`$u$: Mật độ năng lượng điện trường trong chất điện môi ($\mathrm{J/m^3}$)`,
   String.raw`$E$: Cường độ điện trường thực tế tại vị trí khảo sát ($\mathrm{V/m}$ hoặc $\mathrm{N/C}$)`,
   String.raw`$\varepsilon$: Độ điện thẩm tuyệt đối của chất điện môi ($\mathrm{F/m}$)`,
   String.raw`$K$: Hằng số điện môi tương đối (Không có đơn vị)`
  ],description:'Mật độ năng lượng đo bằng J/m³. Trường thực tế trong điện môi đã bao gồm tác dụng của điện tích liên kết.'},
  {name:'Lực hút giữa hai bản tụ phẳng',formulaRows:[
   {label:'Theo điện tích',formula:d(String.raw`F=\frac{Q^2}{2\varepsilon_0 A}`)},
   {label:'Theo điện trường trong khe',formula:d(String.raw`F=\tfrac12\varepsilon_0 E^2 A`)}
  ],variables:[
   String.raw`$F$: Độ lớn lực hút tĩnh điện giữa hai bản tụ phẳng mang điện trái dấu ($\mathrm{N}$)`,
   String.raw`$Q$: Độ lớn điện tích trên mỗi bản tụ phẳng ($\mathrm{C}$)`,
   String.raw`$A$: Diện tích đối diện của bản tụ phẳng ($\mathrm{m^2}$)`,
   String.raw`$E$: Cường độ điện trường trong khe giữa hai bản tụ phẳng ($\mathrm{V/m}$)`
  ],description:'Hệ số 1/2 xuất hiện vì mỗi bản chỉ nằm trong trường do bản kia tạo ra, bằng E/2. Giữ Q cố định, lực không đổi theo khoảng cách khi bỏ hiệu ứng mép.'}]},
 {id:'dielectric',title:'Điện môi và giới hạn cách điện',items:[
  {name:'Hằng số điện môi và độ điện thẩm',formula:d(String.raw`\begin{aligned}
&K = C/C_0,\\
&\varepsilon = K\varepsilon_0.
\end{aligned}`),variables:[
   String.raw`$K$: Hằng số điện môi tương đối của chất cách điện ($K \ge 1$) (Không có đơn vị)`,
   String.raw`$C$: Điện dung của tụ khi lấp đầy chất điện môi ($\mathrm{F}$)`,
   String.raw`$C_0$: Điện dung của tụ khi ở trong chân không ($\mathrm{F}$)`,
   String.raw`$\varepsilon$: Độ điện thẩm của môi trường điện môi ($\mathrm{F/m}$)`
  ],description:'K không có đơn vị, K ≥ 1. Chân không có K = 1. ε₀ là hằng số điện.'},
  {name:'Tụ cô lập, điện môi lấp toàn khe',formula:d(String.raw`\begin{aligned}
&Q = Q_0,\\
&V = V_0/K,\\
&E = E_0/K,\\
&U = U_0/K.
\end{aligned}`),variables:[
   String.raw`$Q$: Điện tích tự do trên bản tụ cô lập ($Q = Q_0$) ($\mathrm{C}$)`,
   String.raw`$V$: Hiệu điện thế giữa hai bản sau khi chèn điện môi ($\mathrm{V}$)`,
   String.raw`$V_0$: Hiệu điện thế ban đầu khi chưa có điện môi ($\mathrm{V}$)`,
   String.raw`$E$: Điện trường sau khi chèn điện môi ($\mathrm{V/m}$)`,
   String.raw`$E_0$: Điện trường ban đầu trong chân không ($\mathrm{V/m}$)`,
   String.raw`$U$: Năng lượng tĩnh điện sau khi chèn điện môi ($U = U_0/K$) ($\mathrm{J}$)`
  ],description:'Không có dòng điện ra vào các bản nên điện tích tự do giữ nguyên. Thế năng giảm do lực hút của tụ kéo tấm điện môi vào khe.'},
  {name:'Tụ giữ nối nguồn điện áp',formula:d(String.raw`\begin{aligned}
&V = V_0,\\
&Q = KQ_0,\\
&E = E_0,\\
&U = KU_0.
\end{aligned}`),variables:[
   String.raw`$V$: Hiệu điện thế hai bản tụ được giữ cố định bởi nguồn điện ($V = V_0$) ($\mathrm{V}$)`,
   String.raw`$Q$: Điện tích tự do sau khi chèn điện môi ($Q = KQ_0$) ($\mathrm{C}$)`,
   String.raw`$U$: Năng lượng tích trữ sau khi chèn điện môi ($U = KU_0$) ($\mathrm{J}$)`
  ],description:'Nguồn lý tưởng duy trì điện áp. Điện tích và năng lượng tăng K lần. Nguồn cung cấp năng lượng gấp đôi phần năng lượng tăng thêm của tụ.'},
  {name:'Điện tích liên kết trên mặt',formula:d(String.raw`\begin{aligned}
&\sigma_i = \sigma(1-1/K),\\
&Q_i = Q(1-1/K).
\end{aligned}`),variables:[
   String.raw`$\sigma_i$: Mật độ mặt của điện tích cảm ứng liên kết trên bề mặt điện môi ($\mathrm{C/m^2}$)`,
   String.raw`$\sigma$: Mật độ mặt của điện tích tự do trên bản cực dẫn điện ($\mathrm{C/m^2}$)`,
   String.raw`$Q_i$: Tổng điện tích cảm ứng liên kết xuất hiện trên bề mặt điện môi ($\mathrm{C}$)`,
   String.raw`$Q$: Tổng điện tích tự do trên bản cực tụ điện ($\mathrm{C}$)`
  ],description:'σ là mật độ điện tích tự do trên bản dẫn, σᵢ là mật độ điện tích liên kết trên mặt điện môi. Điện môi tuyến tính đồng nhất trong trường đều.'},
  {name:'Độ bền điện môi',formula:d(String.raw`E_{\mathrm{max}}=\frac{V_{\mathrm{max}}}{d}`),variables:[
   String.raw`$E_{\mathrm{max}}$: Độ bền điện môi, tức điện trường đánh thủng cực đại của chất cách điện ($\mathrm{V/m}$)`,
   String.raw`$V_{\mathrm{max}}$: Hiệu điện thế cực đại đặt vào tụ trước khi bị đánh thủng ($\mathrm{V}$)`,
   String.raw`$d$: Khoảng cách giữa hai bản tụ phẳng ($\mathrm{m}$)`
  ],description:'V_max là điện áp đánh thủng, E_max là độ bền điện môi của vật liệu. Tụ phẳng trường đều.'}]},
 {id:'gauss-bound',title:'Gauss và mô hình phân tử',items:[
  {name:'Gauss viết theo điện tích tự do',formulaRows:[
   {label:'Dạng tích phân',formula:d(String.raw`\oint_S K\vec E\cdot d\vec A=\frac{Q_{\mathrm{free},\mathrm{encl}}}{\varepsilon_0}`)},
   {label:'Điện môi đồng nhất phủ toàn mặt',formula:d(String.raw`\oint_S \vec E\cdot d\vec A=\frac{Q_{\mathrm{free},\mathrm{encl}}}{K\varepsilon_0}`)}
  ],variables:[
   String.raw`$K$: Hằng số điện môi của môi trường xuyên qua mặt Gauss (Không có đơn vị)`,
   String.raw`$\vec E$: Vector cường độ điện trường thực tế tại điểm lấy tích phân ($\mathrm{V/m}$)`,
   String.raw`$Q_{\mathrm{free},\mathrm{encl}}$: Tổng điện tích tự do được bao bởi mặt kín Gauss ($\mathrm{C}$)`
  ],description:'Điện tích liên kết đã được gộp vào vế trái qua K. Không cộng lại điện tích liên kết vào vế phải khi dùng dạng này.'},
  {name:'Gauss viết theo toàn bộ điện tích',formula:d(String.raw`\oint_S\vec E\cdot d\vec A=\frac{Q_{\mathrm{free}}+Q_{\mathrm{bound}}}{\varepsilon_0}`),variables:[
   String.raw`$Q_{\mathrm{free}}$: Tổng đại số điện tích tự do bên trong mặt kín ($\mathrm{C}$)`,
   String.raw`$Q_{\mathrm{bound}}$: Tổng đại số điện tích cảm ứng liên kết phân cực bên trong mặt kín ($\mathrm{C}$)`
  ],description:'Dạng Gauss gốc của chương 22. Điện trường E là trường thực tế tạo bởi cả hai loại điện tích.'},
  {name:'Lưỡng cực phân tử trong trường',formula:d(String.raw`\begin{aligned}
&\vec\tau = \vec p\times\vec E,\\
&U = -\vec p\cdot\vec E.
\end{aligned}`),variables:[
   String.raw`$\vec\tau$: Vector mômen lực làm quay phân tử phân cực ($\mathrm{N\cdot m}$)`,
   String.raw`$\vec p$: Vector mômen lưỡng cực điện của phân tử chất điện môi ($\mathrm{C\cdot m}$)`,
   String.raw`$U$: Thế năng định hướng của lưỡng cực phân tử trong điện trường ($\mathrm{J}$)`
  ],description:'Mômen lực quay các lưỡng cực về hướng trường ngoài. Nhiệt độ chống lại sự định hướng có trật tự.'}]}
]}
