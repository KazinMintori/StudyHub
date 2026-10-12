const note='02-dien-the'
const d=tex=>'$$\n'+tex+'\n$$'
export const potentialTopics=[
 {title:'Thế năng và điện thế',topics:[
  {slug:'the-nang-dien',title:'Thế năng điện',question:'Công lực điện và năng lượng của hệ liên hệ như thế nào?',source:'23.1'},
  {slug:'dien-the',title:'Điện thế và hiệu điện thế',question:'Đại lượng nào thuộc trường và đại lượng nào còn phụ thuộc điện tích thử?',source:'23.2'}]},
 {title:'Tính toán và hình học điện thế',topics:[
  {slug:'tinh-dien-the',title:'Tính điện thế của các phân bố nguồn',question:'Tìm điện thế của cầu, vòng, thanh và hai bản như thế nào?',source:'23.3'},
  {slug:'mat-dang-the',title:'Mặt đẳng thế và vật dẫn',question:'Vì sao đường sức vuông góc mặt đẳng thế?',source:'23.4'},
  {slug:'gradient-dien-the',title:'Gradient điện thế',question:'Từ hàm điện thế suy ra từng thành phần điện trường ra sao?',source:'23.5'}]}
]
export const potentialSlides=[
 {note,title:'Công lực điện làm thế năng giảm',bullets:['Trường tĩnh điện là trường thế. Công giữa hai điểm không phụ thuộc đường đi.','Thế năng thuộc hệ các điện tích và phụ thuộc mốc được chọn.','Nếu chỉ lực điện sinh công thì động năng cộng thế năng được bảo toàn.'],formula:d(String.raw`\begin{aligned}
W_{a\to b}&=U_a-U_b,\\
K_a+U_a&=K_b+U_b.
\end{aligned}`),example:''},
 {note,title:'Thế năng nhiều nguồn đếm mỗi cặp một lần',bullets:['Với hai nguồn điểm, thế năng có dấu của tích điện tích.','Công thêm một nguồn vào hệ chỉ tính các cặp liên quan nguồn mới.','Mốc bằng không khi mọi nguồn ở xa vô hạn phù hợp hệ nguồn hữu hạn.'],formula:d(String.raw`\begin{aligned}
U_{123}&=kq_1q_2/r_{12}\\
&\quad+kq_1q_3/r_{13}+kq_2q_3/r_{23}.
\end{aligned}`),example:''},
 {note,title:'Điện thế tách ảnh hưởng của điện tích thử',bullets:['Điện thế là thế năng trên mỗi đơn vị điện tích thử.','Hiệu điện thế cho công lực điện trên mỗi coulomb.','Điện thế cao không luôn tương ứng thế năng cao vì điện tích thử có thể âm.'],formula:d(String.raw`\begin{aligned}
V&=U/q_0,\\
W_{a\to b}&=q_0(V_a-V_b),\\
1\,\mathrm V&=1\,\mathrm{J/C}.
\end{aligned}`),example:''},
 {note,title:'Cộng điện thế bằng tổng đại số hoặc tích phân',bullets:['Điện thế là vô hướng, nên cộng phần đóng góp có dấu.','Phân bố liên tục được chia thành các phần dq.','Nguồn kéo dài vô hạn thường cần mốc hữu hạn thay cho vô hạn.'],formula:d(String.raw`\begin{aligned}
V&=k\int dq/r,\\
V_a-V_b&=\int_a^b\vec E\cdot d\vec\ell.
\end{aligned}`),example:''},
 {note,title:'Mặt đẳng thế vuông góc điện trường',bullets:['Dịch chuyển trên mặt đẳng thế không làm lực điện sinh công.','Tại điểm trường khác không, trường vuông góc mặt đẳng thế.','Vật dẫn cân bằng và hốc kín không có nguồn riêng là miền đẳng thế.'],formula:d(String.raw`dV=-\vec E\cdot d\vec\ell`),example:''},
 {note,title:'Gradient cho trường từ hàm điện thế',bullets:['Lấy âm đạo hàm riêng theo mỗi tọa độ để có thành phần trường.','Trường hướng về phía điện thế giảm nhanh nhất.','Cộng một hằng số vào điện thế không thay đổi điện trường.'],formula:d(String.raw`\begin{aligned}
E_x&=-\partial V/\partial x,\\
E_y&=-\partial V/\partial y,\\
E_z&=-\partial V/\partial z,\\
\vec E&=-\nabla V.
\end{aligned}`),example:''}
]
export const potentialCheatsheet={summary:'Định nghĩa, tính chất và công thức của thế năng điện, điện thế, mặt đẳng thế và gradient.',sections:[
 {id:'energy',title:'Thế năng và công',items:[
  {name:'Trường tĩnh điện và bảo toàn cơ năng',formulaRows:[
   {label:'Công lực điện',formula:d(String.raw`\begin{aligned}
W_{a\to b}&=U_a-U_b\\
&=-\Delta U
\end{aligned}`)},
   {label:'Công lực ngoài khi chuyển động chậm',formula:d(String.raw`W_{\mathrm{ngoài}}=\Delta U`)},
   {label:'Cơ năng khi chỉ lực thế sinh công',formula:d(String.raw`K_a+U_a=K_b+U_b`)}
  ],description:'Lực điện trong trường tĩnh là lực thế. Công ngoài chậm có động năng không đổi. Bảo toàn cơ năng khi chỉ lực thế sinh công.'},
  {name:'Hai điện tích điểm',formula:d(String.raw`U=kqq_0/r`),description:'r là khoảng cách hai nguồn, k = 1/(4πε₀). Mốc thế năng bằng không ở khoảng cách vô hạn. Tích qq₀ được giữ dấu.'},
  {name:'Ba điện tích và tổng các cặp',formula:d(String.raw`\begin{aligned}
U_{123}&=kq_1q_2/r_{12}\\
&\quad+kq_1q_3/r_{13}\\
&\quad+kq_2q_3/r_{23},\\
U&=k\sum_{i=1}^{n-1}\sum_{j=i+1}^{n}
\frac{q_iq_j}{r_{ij}}.
\end{aligned}`),description:'i chạy từ 1 đến n − 1, j từ i + 1 đến n. Mỗi cặp xuất hiện một lần. Mốc ứng với mọi điện tích ở xa vô hạn.'}]},
 {id:'potential',title:'Điện thế và hiệu điện thế',items:[
  {name:'Định nghĩa và đơn vị',formulaRows:[
   {label:'Điện thế',formula:d(String.raw`V=U/q_0`)},
   {label:'Hiệu điện thế',formula:d(String.raw`V_a-V_b=W_{a\to b}/q_0`)},
   {label:'Đơn vị điện thế',formula:d(String.raw`1\,\mathrm V=1\,\mathrm{J/C}`)},
   {label:'Đơn vị điện trường',formula:d(String.raw`1\,\mathrm{V/m}=1\,\mathrm{N/C}`)}
  ],description:'q₀ là điện tích thử khác không, đủ nhỏ để không làm đổi phân bố nguồn. Chỉ hiệu điện thế có ý nghĩa độc lập với mốc.'},
  {name:'Công, động năng và electron-volt',formula:d(String.raw`\begin{aligned}
W_{a\to b}&=q_0(V_a-V_b),\\
\Delta K&=-q_0\Delta V,\\
1\,\mathrm{eV}&=1.602176634\\
&\quad\times10^{-19}\,\mathrm J.
\end{aligned}`),description:'Công thức động năng áp dụng khi chỉ lực điện sinh công. Electron-volt là đơn vị năng lượng, bằng năng lượng một điện tích có độ lớn e nhận qua hiệu điện thế có độ lớn 1 V.'},
  {name:'Nguồn điểm và nhiều nguồn',formula:d(String.raw`\begin{aligned}
V&=kq/r,\\
V_{123}&=kq_1/r_1+kq_2/r_2\\
&\quad+kq_3/r_3,\\
V&=k\sum_{i=1}^{n}q_i/r_i.
\end{aligned}`),description:'Mốc ở vô hạn với hệ nguồn hữu hạn. Tổng có dấu. i chạy qua n nguồn, rᵢ là khoảng cách từ nguồn i tới điểm khảo sát.'},
  {name:'Phân bố liên tục',formulaRows:[
   {label:'Điện thế của toàn nguồn',formula:d(String.raw`V=k\int dq/r`)},
   {label:'Phần tử nguồn theo chiều dài',formula:d(String.raw`dq=\lambda\,d\ell`)},
   {label:'Phần tử nguồn trên mặt',formula:d(String.raw`dq=\sigma\,dA`)},
   {label:'Phần tử nguồn trong thể tích',formula:d(String.raw`dq=\rho\,d\mathcal V`)}
  ],description:'r đo từ từng phần nguồn tới điểm khảo sát. λ, σ, ρ là mật độ dài, mặt, thể tích. Chọn công thức dq theo hình học nguồn.'}]},
 {id:'field',title:'Điện thế và điện trường',items:[
  {name:'Tích phân dọc đường',formula:d(String.raw`\begin{aligned}
V_a-V_b&=\int_a^b\vec E\cdot d\vec\ell,\\
dV&=-\vec E\cdot d\vec\ell,\\
\Delta V&=-\vec E\cdot\Delta\vec r.
\end{aligned}`),description:'Hai công thức đầu áp dụng trường tĩnh. Công thức cuối cần trường đều trên đường đi. Đường tích phân tránh điểm kỳ dị của mô hình nguồn.'},
  {name:'Mặt đẳng thế và vật dẫn',formula:'',description:'Điện thế không đổi trên mặt đẳng thế. Trường vuông góc mặt tại điểm trường khác không. Toàn vật dẫn cân bằng tĩnh điện đẳng thế. Hốc kín không có nguồn riêng có cùng thế với thành hốc và trường bằng không.'},
  {name:'Gradient trong tọa độ Descartes',formula:d(String.raw`\begin{aligned}
E_x&=-\partial V/\partial x,\\
E_y&=-\partial V/\partial y,\\
E_z&=-\partial V/\partial z,\\
\nabla V&=\hat{\mathbf i}\,\partial V/\partial x\\
&\quad+\hat{\mathbf j}\,\partial V/\partial y\\
&\quad+\hat{\mathbf k}\,\partial V/\partial z,\\
\vec E&=-\nabla V.
\end{aligned}`),description:'Cần V khả vi trong vùng khảo sát. Gradient hướng tăng thế nhanh nhất, điện trường hướng ngược lại. Đổi mốc bằng hằng số không đổi trường.'}]},
 {id:'sources',title:'Các phân bố đối xứng',items:[
  {name:'Cầu dẫn và vỏ cầu đều',formulaRows:[
   {label:'Ngoài cầu, r ≥ R',formula:d(String.raw`V(r)=kQ/r`)},
   {label:'Trong cầu, r ≤ R',formula:d(String.raw`V(r)=kQ/R`)}
  ],description:'Cầu dẫn cô lập đối xứng hoặc vỏ cầu mỏng tích điện đều, bán kính R. Mốc ở vô hạn. Không áp dụng công thức trong cho cầu cách điện đều theo thể tích.'},
  {name:'Cầu cách điện đều theo thể tích',formulaRows:[
   {label:'Ngoài cầu và trên mặt, r ≥ R',formula:d(String.raw`V(r)=kQ/r`)},
   {label:'Trong cầu, r ≤ R',formula:d(String.raw`V(r)=\frac{kQ}{2R}(3-r^2/R^2)`)}
  ],description:'Q đều trong thể tích cầu bán kính R. Mốc ở vô hạn. Điện thế và thành phần trường liên tục tại R.'},
  {name:'Vòng đều trên trục',formula:d(String.raw`\begin{aligned}
V(x)&=kQ/\sqrt{x^2+a^2},\\
E_x&=kQx/(x^2+a^2)^{3/2}.
\end{aligned}`),description:'a là bán kính vòng, x đo dọc trục từ tâm. Mốc ở vô hạn. Công thức điện thế trên trục không cho phép lấy đạo hàm theo tọa độ ngoài trục.'},
  {name:'Thanh đều, điểm trên đường trung trực',formulaRows:[
   {label:'Khoảng cách s từ điểm khảo sát đến mỗi đầu thanh',formula:d(String.raw`s=\sqrt{x^2+a^2}`)},
   {label:'Điện thế tại điểm khảo sát',formula:d(String.raw`V(x)=\frac{kQ}{2a}\ln\frac{s+a}{s-a}`)}
  ],description:'Thanh dài 2a, x là khoảng cách vuông góc đến tâm, x khác không. s là khoảng cách tới mỗi đầu thanh, không phải một tọa độ độc lập. Mốc ở vô hạn.'},
  {name:'Dây vô hạn và hai bản',formulaRows:[
   {label:'Hiệu điện thế của dây vô hạn',formula:d(String.raw`\Delta V=2k\lambda\ln(r_2/r_1)`)},
   {label:'Thứ tự hai điểm trong hiệu điện thế',formula:d(String.raw`\Delta V=V(r_1)-V(r_2)`)},
   {label:'Điện thế giữa hai bản, trường đều',formula:d(String.raw`V(y)=V(0)-E_y y`)}
  ],description:'Dây thẳng vô hạn có r₁, r₂ dương, không dùng mốc vô hạn. Hai bản lớn song song dùng trường đều trong khe khi bỏ hiệu ứng mép.'}]}
]}
