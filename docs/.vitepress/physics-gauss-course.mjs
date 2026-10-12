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
 {note,title:'Gauss đếm điện tích tổng được bao',bullets:['Điện tích được cộng với dấu.','Trường trong tích phân là trường của cả nguồn trong và ngoài.','Nguồn ngoài không đóng góp điện thông tổng qua mặt kín.'],formula:d(String.raw`\begin{aligned}
\Phi_E&=\oint\vec E\cdot d\vec A\\
&=\frac{Q_{\mathrm{trong}}}{\varepsilon_0}.
\end{aligned}`),example:''},
 {note,title:'Đối xứng của nguồn quyết định mặt Gauss',bullets:['Đối xứng cầu dùng cầu đồng tâm. Đối xứng trụ dùng trụ đồng trục.','Đối xứng phẳng dùng hai đáy song song mặt nguồn.','Điện thông không không buộc điện trường không.'],formula:'',example:''},
 {note,title:'Cầu dẫn và cầu cách điện đều có trường trong khác nhau',bullets:['Trong vật liệu dẫn cân bằng, trường bằng không.','Trong cầu cách điện đều theo thể tích, trường tăng tuyến tính theo bán kính.','Trường ngoài của hai phân bố cầu cùng tổng điện tích giống nhau.'],formula:d(String.raw`\begin{aligned}
E_{\mathrm{trong}}&=\frac{k|Q|r}{R^3},\quad r<R,\\
E_{\mathrm{ngoài}}&=\frac{k|Q|}{r^2},\quad r>R.
\end{aligned}`),example:''},
 {note,title:'Vật dẫn che chắn nhờ điện tích tái phân bố',bullets:['Nguồn q trong hốc tạo tổng −q trên thành hốc.','Vật dẫn cô lập có tổng qC thì mặt ngoài mang qC + q.','Ngay ngoài mặt dẫn, trường vuông góc mặt.'],formula:d(String.raw`\begin{aligned}
Q_{\mathrm{trong}}&=-q,\\
Q_{\mathrm{ngoài}}&=q_C+q,\\
E_\perp&=\frac{\sigma}{\varepsilon_0}.
\end{aligned}`),example:''}
]
export const gaussCheatsheet={summary:'Định nghĩa, tính chất và công thức của điện thông, Gauss và vật dẫn cân bằng tĩnh điện.',sections:[
 {id:'flux',title:'Điện thông',items:[
  {name:'Mặt phẳng, trường đều',formula:d(String.raw`\begin{aligned}
\vec A&=A\hat{\mathbf n},\\
\Phi_E&=EA\cos\varphi\\
&=\vec E\cdot\vec A.
\end{aligned}`),description:'φ là góc với pháp tuyến. Đơn vị điện thông là N m²/C. Mặt kín chọn pháp tuyến ra ngoài.'},
  {name:'Mặt bất kỳ',formula:d(String.raw`\begin{aligned}
\Phi_E&=\int_A E_\perp\,dA\\
&=\int_A\vec E\cdot d\vec A.
\end{aligned}`),description:'Trường và vector diện tích được xét tại từng điểm mặt.'}]},
 {id:'gauss',title:'Định luật Gauss',items:[
  {name:'Điện tích được bao và điện thông',formula:d(String.raw`\begin{aligned}
Q_{\mathrm{trong}}&=q_1+q_2+\cdots+q_n\\
&=\sum_{i=1}^{n}q_i,\\
\Phi_E&=\oint\vec E\cdot d\vec A\\
&=\frac{Q_{\mathrm{trong}}}{\varepsilon_0}.
\end{aligned}`),description:'i chạy từ 1 đến n qua các nguồn bên trong. Trường là trường tổng. Nguồn ngoài cho điện thông tổng bằng không. Điện thông không không buộc trường không.'}]},
 {id:'symmetry',title:'Nguồn đối xứng',items:[
  {name:'Cầu và dây dài',formula:d(String.raw`\begin{aligned}
E_r&=\frac{kQ_{\mathrm{trong}}(r)}{r^2},\\
E_{r,\mathrm{dây}}&=\frac{\lambda}{2\pi\varepsilon_0r}.
\end{aligned}`),description:'Cầu dùng mặt cầu đồng tâm. Dây vô hạn và trụ dài dùng mặt trụ đồng trục.'},
  {name:'Nguồn đều trong thể tích',formula:d(String.raw`\begin{aligned}
E_{r,\mathrm{cầu}}&=\frac{\rho r}{3\varepsilon_0},\\
E_{r,\mathrm{trụ}}&=\frac{\rho r}{2\varepsilon_0}.
\end{aligned}`),description:'Các biểu thức trong vật cách điện có mật độ thể tích đều. Bên ngoài dùng toàn điện tích hoặc mật độ dài được bao.'},
  {name:'Mặt vô hạn và hai bản đối diện',formula:d(String.raw`\begin{aligned}
E_{\mathrm{mặt}}&=\frac{|\sigma|}{2\varepsilon_0},\\
E_{\mathrm{giữa\ bản}}&=\frac{|\sigma|}{\varepsilon_0}.
\end{aligned}`),description:'Một mặt đều cho trường hai phía. Hai bản dẫn lớn song song trái dấu cho trường giữa từ dương đến âm và trường ngoài bằng không trong mô hình vô hạn.'}]},
 {id:'conductor',title:'Vật dẫn và hốc',items:[
  {name:'Cân bằng tĩnh điện',formula:d(String.raw`\begin{aligned}
\vec E_{\mathrm{vật\ liệu}}&=0,\\
Q_{\mathrm{mặt\ trong}}&=-q,\\
Q_{\mathrm{mặt\ ngoài}}&=q_C+q,\\
E_\perp&=\frac{\sigma}{\varepsilon_0}.
\end{aligned}`),description:'q là tổng nguồn riêng trong hốc, qC là tổng điện tích vật dẫn cô lập. Nối đất cho phép trao đổi điện tích. Trường ngay ngoài vuông góc mặt dẫn. Hốc kín không chứa nguồn được che chắn khỏi trường ngoài.'}]}
]}
