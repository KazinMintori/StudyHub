const note='03-dinh-luat-gauss'
const d=tex=>'$$\n'+tex+'\n$$'
export const gaussTopics=[
 {title:'Điện tích và điện thông',topics:[
  {slug:'dien-tich-dien-thong',title:'Điện tích và điện thông',question:'Trường bên ngoài cho biết gì về điện tích bên trong?',source:'22.1'},
  {slug:'tinh-dien-thong',title:'Tính điện thông',question:'Diện tích, pháp tuyến và trường đi vào tích phân như thế nào?',source:'22.2'}]},
 {title:'Định luật và các cấu hình đối xứng',topics:[
  {slug:'dinh-luat-gauss',title:'Định luật Gauss',question:'Vì sao điện thông tổng chỉ phụ thuộc điện tích được bao?',source:'22.3'},
  {slug:'ung-dung-gauss',title:'Áp dụng định luật Gauss',question:'Chọn mặt Gauss thế nào để tìm điện trường?',source:'22.4'}]},
 {title:'Điện tích trên vật dẫn',topics:[
  {slug:'dien-tich-vat-dan',title:'Điện tích và che chắn tĩnh điện trên vật dẫn',question:'Điện tích mặt trong, mặt ngoài và trường trong hốc liên hệ thế nào?',source:'22.5'}]}
]
export const gaussSlides=[
 {note,title:'Điện thông dùng thành phần trường theo pháp tuyến',bullets:['Với mặt phẳng trong trường đều, điện thông bằng tích vô hướng của trường và vector diện tích.','Góc được đo với pháp tuyến. Trường song song mặt cho điện thông bằng không.','Mặt kín luôn chọn pháp tuyến ra ngoài.'],formula:d(String.raw`\Phi_E=EA\cos\varphi`),example:''},
 {note,title:'Mặt cong hoặc trường không đều cần tích phân mặt',bullets:['Tính trường và pháp tuyến tại từng phần mặt nhỏ.','Cộng các tích vô hướng có dấu để được điện thông tổng.','Chỉ đưa E ra ngoài tích phân khi độ lớn ấy không đổi trên phần mặt đang xét.'],formula:d(String.raw`\Phi_E=\int_A\vec E\cdot d\vec A`),example:''},
 {note,title:'Gauss đếm điện tích tổng được bao',bullets:['Điện tích được cộng với dấu.','Trường trong tích phân là trường của cả nguồn trong và ngoài.','Nguồn ngoài không đóng góp điện thông tổng qua mặt kín.'],formula:d(String.raw`\Phi_E = \oint\vec E\cdot d\vec A = \frac{Q_{\mathrm{trong}}}{\varepsilon_0}`),example:''},
 {note,title:'Đối xứng của nguồn quyết định mặt Gauss',bullets:['Đối xứng cầu dùng cầu đồng tâm. Đối xứng trụ dùng trụ đồng trục.','Đối xứng phẳng dùng hai đáy song song mặt nguồn.','Điện thông không không buộc điện trường không.'],formula:'',example:''},
 {note,title:'Cầu dẫn và cầu cách điện đều có trường trong khác nhau',bullets:['Trong vật liệu dẫn cân bằng, trường bằng không.','Trong cầu cách điện đều theo thể tích, trường tăng tuyến tính theo bán kính.','Trường ngoài của hai phân bố cầu cùng tổng điện tích giống nhau.'],formula:d(String.raw`\begin{aligned}
&E_{\mathrm{trong}} = \frac{k|Q|r}{R^3},\quad r<R,\\
&E_{\mathrm{ngoai}} = \frac{k|Q|}{r^2},\quad r>R.
\end{aligned}`),example:''},
 {note,title:'Vật dẫn che chắn nhờ điện tích tái phân bố',bullets:['Nguồn q trong hốc tạo tổng −q trên thành hốc.','Vật dẫn cô lập có tổng qC thì mặt ngoài mang qC + q.','Ngay ngoài mặt dẫn, trường vuông góc mặt.'],formula:d(String.raw`\begin{aligned}
&Q_{\mathrm{trong}} = -q,\\
&Q_{\mathrm{ngoai}} = q_C+q,\\
&E_\perp = \frac{\sigma}{\varepsilon_0}.
\end{aligned}`),example:''}
]
export const gaussCheatsheet={summary:'Định nghĩa, tính chất và công thức của điện thông, Gauss và vật dẫn cân bằng tĩnh điện.',sections:[
 {id:'flux',title:'Điện thông',items:[
  {name:'Mặt phẳng, trường đều',formula:d(String.raw`\begin{aligned}
&\vec A = A\hat{\mathbf n},\\
&\Phi_E = EA\cos\varphi = \vec E\cdot\vec A.
\end{aligned}`),variables:[
   String.raw`$\Phi_E$: Điện thông gửi qua bề mặt phẳng $A$ ($\mathrm{N\cdot m^2/C}$ hoặc $\mathrm{V\cdot m}$)`,
   String.raw`$E$: Cường độ điện trường đều ($\mathrm{V/m}$ hoặc $\mathrm{N/C}$)`,
   String.raw`$A$: Diện tích của bề mặt phẳng ($\mathrm{m^2}$)`,
   String.raw`$\hat{\mathbf n}$: Vector pháp tuyến đơn vị của mặt phẳng (Không có đơn vị)`,
   String.raw`$\varphi$: Góc hợp bởi vector điện trường $\vec E$ và vector pháp tuyến $\hat{\mathbf n}$ ($\mathrm{rad}$ hoặc độ)`
  ],description:'φ là góc với pháp tuyến. Đơn vị điện thông là N m²/C. Mặt kín chọn pháp tuyến ra ngoài.'},
  {name:'Mặt bất kỳ',formula:d(String.raw`\Phi_E = \int_A E_\perp\,dA = \int_A\vec E\cdot d\vec A`),variables:[
   String.raw`$\Phi_E$: Điện thông toàn phần gửi qua mặt cong $A$ ($\mathrm{V\cdot m}$)`,
   String.raw`$E_\perp$: Thành phần của điện trường vuông góc với vi phân diện tích $dA$ ($\mathrm{V/m}$)`,
   String.raw`$d\vec A$: Vector vi phân diện tích ($d\vec A = dA\,\hat{\mathbf n}$) ($\mathrm{m^2}$)`
  ],description:'Trường và vector diện tích được xét tại từng điểm mặt.'}]},
 {id:'gauss',title:'Định luật Gauss',items:[
  {name:'Điện tích được bao và điện thông',formula:d(String.raw`\begin{aligned}
&Q_{\mathrm{trong}} = \sum_{i=1}^{n}q_i,\\
&\Phi_E = \oint\vec E\cdot d\vec A = \frac{Q_{\mathrm{trong}}}{\varepsilon_0}.
\end{aligned}`),variables:[
   String.raw`$\Phi_E$: Điện thông toàn phần qua mặt kín Gauss bất kỳ ($\mathrm{V\cdot m}$)`,
   String.raw`$Q_{\mathrm{trong}}$: Tổng đại số điện tích thực nằm bên trong mặt kín Gauss ($\mathrm{C}$)`,
   String.raw`$q_i$: Điện tích thành phần thứ $i$ nằm trong mặt kín ($\mathrm{C}$)`,
   String.raw`$\varepsilon_0$: Hằng số điện môi chân không ($\approx 8{,}854\times10^{-12}\,\mathrm{F/m}$)`
  ],description:'i chạy từ 1 đến n qua các nguồn bên trong. Trường là trường tổng. Nguồn ngoài cho điện thông tổng bằng không. Điện thông không không buộc trường không.'}]},
 {id:'symmetry',title:'Nguồn đối xứng',items:[
  {name:'Cầu và dây dài',formula:d(String.raw`\begin{aligned}
&E_r = \frac{kQ_{\mathrm{trong}}(r)}{r^2},\\
&E_{r,\mathrm{wire}} = \frac{\lambda}{2\pi\varepsilon_0r}.
\end{aligned}`),variables:[
   String.raw`$E_r$: Cường độ điện trường theo phương bán kính của phân bố đối xứng cầu ($\mathrm{V/m}$)`,
   String.raw`$Q_{\mathrm{trong}}(r)$: Tổng điện tích nằm bên trong mặt cầu bán kính $r$ ($\mathrm{C}$)`,
   String.raw`$E_{r,\mathrm{wire}}$: Cường độ điện trường quanh dây dẫn thẳng dài vô hạn ($\mathrm{V/m}$)`,
   String.raw`$\lambda$: Mật độ điện tích dài của dây dẫn ($\mathrm{C/m}$)`,
   String.raw`$r$: Khoảng cách từ tâm hoặc trục đối xứng đến điểm khảo sát ($\mathrm{m}$)`
  ],description:'Cầu dùng mặt cầu đồng tâm. Dây vô hạn và trụ dài dùng mặt trụ đồng trục.'},
  {name:'Nguồn đều trong thể tích',formula:d(String.raw`\begin{aligned}
&E_{r,\mathrm{sphere}} = \frac{\rho r}{3\varepsilon_0},\\
&E_{r,\mathrm{cylinder}} = \frac{\rho r}{2\varepsilon_0}.
\end{aligned}`),variables:[
   String.raw`$E_{r,\mathrm{sphere}}$: Điện trường bên trong khối cầu cách điện tích điện đều ($r \le R$) ($\mathrm{V/m}$)`,
   String.raw`$E_{r,\mathrm{cylinder}}$: Điện trường bên trong khối trụ cách điện tích điện đều ($r \le R$) ($\mathrm{V/m}$)`,
   String.raw`$\rho$: Mật độ điện tích thể tích không đổi ($\mathrm{C/m^3}$)`,
   String.raw`$r$: Khoảng cách từ tâm cầu hoặc trục trụ đến điểm khảo sát ($\mathrm{m}$)`
  ],description:'Các biểu thức trong vật cách điện có mật độ thể tích đều. Bên ngoài dùng toàn điện tích hoặc mật độ dài được bao.'},
  {name:'Mặt vô hạn và hai bản đối diện',formula:d(String.raw`\begin{aligned}
&E_{\mathrm{sheet}} = \frac{|\sigma|}{2\varepsilon_0},\\
&E_{\mathrm{khe}} = \frac{|\sigma|}{\varepsilon_0}.
\end{aligned}`),variables:[
   String.raw`$E_{\mathrm{sheet}}$: Cường độ điện trường do một mặt phẳng rộng vô hạn mang điện đều sinh ra ($\mathrm{V/m}$)`,
   String.raw`$E_{\mathrm{khe}}$: Điện trường trong khe giữa hai bản dẫn song song tích điện trái dấu ($\mathrm{V/m}$)`,
   String.raw`$|\sigma|$: Độ lớn mật độ điện tích mặt trên bản dẫn ($\mathrm{C/m^2}$)`
  ],description:'Một mặt đều cho trường hai phía. Hai bản dẫn lớn song song trái dấu cho trường giữa từ dương đến âm và trường ngoài bằng không trong mô hình vô hạn.'}]},
 {id:'conductor',title:'Vật dẫn và hốc',items:[
  {name:'Cân bằng tĩnh điện',formula:d(String.raw`\begin{aligned}
&\vec E_{\mathrm{trong}} = 0,\\
&Q_{\mathrm{trong}} = -q,\\
&Q_{\mathrm{ngoai}} = q_C+q,\\
&E_\perp = \frac{\sigma}{\varepsilon_0}.
\end{aligned}`),variables:[
   String.raw`$\vec E_{\mathrm{trong}}$: Điện trường bên trong khối vật liệu dẫn cân bằng tĩnh điện ($\mathrm{V/m}$)`,
   String.raw`$Q_{\mathrm{trong}}$: Tổng điện tích cảm ứng trên thành hốc kín mang điện ($\mathrm{C}$)`,
   String.raw`$q$: Điện tích của nguồn riêng đặt cô lập bên trong hốc ($\mathrm{C}$)`,
   String.raw`$Q_{\mathrm{ngoai}}$: Tổng điện tích trên bề mặt ngoài của vật dẫn ($\mathrm{C}$)`,
   String.raw`$q_C$: Tổng điện tích ban đầu của vật dẫn cô lập ($\mathrm{C}$)`,
   String.raw`$E_\perp$: Điện trường ngay sát mặt ngoài vật dẫn vuông góc với bề mặt ($\mathrm{V/m}$)`,
   String.raw`$\sigma$: Mật độ điện tích mặt tại vị trí khảo sát trên mặt vật dẫn ($\mathrm{C/m^2}$)`
  ],description:'q là tổng nguồn riêng trong hốc, qC là tổng điện tích vật dẫn cô lập. Nối đất cho phép trao đổi điện tích. Trường ngay ngoài vuông góc mặt dẫn. Hốc kín không chứa nguồn được che chắn khỏi trường ngoài.'}]}
]}
