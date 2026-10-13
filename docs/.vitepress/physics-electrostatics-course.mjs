const note='01-dien-truong-coulomb'
export const electrostaticsSlides=[
 {note,title:'Điện tích được bảo toàn và lượng tử hóa',bullets:['Điện tích cùng dấu đẩy nhau, trái dấu hút nhau.','Tổng đại số điện tích trong hệ kín giữ nguyên.','Phân cực không bắt buộc làm tổng điện tích khác không.'],formula:'$$\nQ=ne,\\quad n\\in\\mathbb Z\n$$',example:''},
 {note,title:'Lực Coulomb được cộng theo vector',bullets:['Nguồn điểm được dùng khi kích thước nguồn nhỏ so với khoảng cách.','Trong chân không, độ lớn lực tỷ lệ tích độ lớn điện tích và nghịch đảo bình phương khoảng cách.','Hai lực của một cặp bằng nhau về độ lớn và ngược chiều.'],formula:'$$\nF=\\frac{k|q_1q_2|}{r^2}\n$$',example:''},
 {note,title:'Điện trường khác lực lên điện tích thử',bullets:['Trường của nguồn tồn tại dù không đặt điện tích thử tại điểm khảo sát.','Nguồn thử dương chịu lực cùng chiều trường, nguồn thử âm chịu lực ngược chiều.','Vector đơn vị trong trường nguồn điểm hướng từ nguồn đến điểm khảo sát.'],formula:'$$\n\\begin{aligned}&\n\\vec F_0 = q_0\\vec E,\\\\&\n\\vec E = \\frac{kq}{r^2}\\hat{\\mathbf r}.\n\\end{aligned}\n$$',example:''},
 {note,title:'Đối xứng giúp cộng trường liên tục',bullets:['Các trường thành phần đều được tính tại cùng điểm.','Chia nguồn liên tục thành phần nhỏ rồi tích phân vector trường.','Cận tích phân phủ toàn nguồn và không đếm một phần nguồn hai lần.'],formula:'$$\n\\begin{aligned}&\n\\vec E = \\vec E_1+\\vec E_2+\\cdots+\\vec E_n\\\\&\n = \\sum_{i=1}^{n}\\vec E_i.\n\\end{aligned}\n$$',example:''},
 {note,title:'Đường sức biểu diễn hướng điện trường',bullets:['Tiếp tuyến đường sức cùng hướng trường tại mỗi điểm.','Các đường không cắt nhau, mật độ đường biểu diễn độ mạnh tương đối của trường.','Đường sức nhìn chung khác quỹ đạo của hạt mang điện.'],formula:'',example:''},
 {note,title:'Lưỡng cực có thể quay khi hợp lực bằng không',bullets:['Mômen lưỡng cực hướng từ âm đến dương.','Trong trường đều, hai lực bù nhau nhưng có thể tạo mômen.','Cùng chiều trường là cân bằng bền, ngược chiều là không bền.'],formula:'$$\n\\begin{aligned}&\np = qd,\\\\&\n\\vec\\tau = \\vec p\\times\\vec E,\\\\&\nU = -\\vec p\\cdot\\vec E.\n\\end{aligned}\n$$',example:''}
]

// Definitions, properties and formulas only. No exercises or verification text.
export const electrostaticsCheatsheet={
  summary:'Các định nghĩa, tính chất và công thức của chương Điện tích và điện trường.',
  sections:[
    {id:'charge',title:'Điện tích',items:[
      {name:'Bảo toàn và lượng tử hóa',formulaRows:[
        {label:'Tổng điện tích trong hệ kín được bảo toàn',formula:'$$\nQ_{\\mathrm{tong}}=Q_0\n$$'},
        {label:'Điện tích của vật cô lập được lượng tử hóa',formula:'$$\nQ=ne,\\quad n\\in\\mathbb Z\n$$'},
        {label:'Độ lớn điện tích cơ bản, chính xác theo định nghĩa',formula:'$$\n\\begin{aligned}&\ne = 1.602176634\\\\&\n \\quad\\times10^{-19}\\,\\mathrm C.\n\\end{aligned}\n$$'}
      ],description:'Điện tích cùng dấu đẩy nhau, trái dấu hút nhau. Vật dẫn cho điện tích dễ di chuyển, vật cách điện thì không. Phân cực không bắt buộc tạo điện tích tổng khác không.'}
    ]},
    {id:'force-field',title:'Lực điện và điện trường',items:[
      {name:'Hai điện tích điểm trong chân không',formula:'$$\n\\begin{aligned}&\nF = k\\frac{|q_1q_2|}{r^2},\\\\&\nk = \\frac1{4\\pi\\varepsilon_0}.\n\\end{aligned}\n$$',description:'r là khoảng cách dương giữa nguồn. Lực nằm trên đường nối hai nguồn. Hai lực của một cặp tuân theo định luật III Newton.'},
      {name:'Trường và lực lên điện tích điểm',formula:'$$\n\\begin{aligned}&\n\\vec E = \\frac{\\vec F_0}{q_0},\\quad q_0\\ne0,\\\\&\n\\vec F_0 = q_0\\vec E,\\\\&\n\\vec E_{\\mathrm{point}} = k\\frac q{r^2}\\hat{\\mathbf r}.\n\\end{aligned}\n$$',description:'Vector đơn vị hướng từ nguồn đến điểm trường. Đơn vị trường là N/C. Nguồn dương tạo trường ra xa, nguồn âm tạo trường hướng về. Trường trong vật liệu dẫn ở cân bằng tĩnh điện bằng không.'}
    ]},
    {id:'distribution',title:'Chồng chất và mật độ điện tích',items:[
      {name:'Các nguồn rời rạc',formula:'$$\n\\begin{aligned}&\n\\vec E = \\vec E_1+\\vec E_2+\\cdots+\\vec E_n\\\\&\n = \\sum_{i=1}^{n}\\vec E_i.\n\\end{aligned}\n$$',description:'Các thành phần đều được tính tại cùng điểm khảo sát, trong đó chỉ số i chạy từ 1 đến n qua các nguồn.'},
      {name:'Nguồn liên tục',formula:'$$\n\\begin{aligned}&\ndq = \\lambda\\,d\\ell,\\\\&\ndq = \\sigma\\,dA,\\\\&\ndq = \\rho\\,dV,\\\\&\nd\\vec E = k\\frac{dq}{r^2}\\hat{\\mathbf r},\\\\&\n\\vec E = \\int_{\\mathrm{src}}d\\vec E.\n\\end{aligned}\n$$',description:'Mật độ dài đo bằng C/m, mật độ mặt bằng C/m² và mật độ thể tích bằng C/m³.'}
    ]},
    {id:'standard-fields',title:'Các phân bố điện tích đều',items:[
      {name:'Trên trục vòng bán kính a',formula:'$$\n\\begin{aligned}&\nE_x = \\frac{kQx}{(x^2+a^2)^{3/2}},\\\\&\n\\vec E = E_x\\hat{\\mathbf i}.\n\\end{aligned}\n$$',description:'x đo từ tâm theo trục vòng. Trường tại tâm bằng không. Ở xa vòng, trường gần như nguồn điểm.'},
      {name:'Trên trung trực đoạn dây dài 2a',formula:'$$\n\\begin{aligned}&\nE_x = \\frac{kQ}{x\\sqrt{x^2+a^2}},\\\\&\n\\vec E = E_x\\hat{\\mathbf i},\\quad x>0.\n\\end{aligned}\n$$',description:'Q phân bố đều từ y = −a đến y = +a. Thành phần y triệt tiêu.'},
      {name:'Dây vô hạn và mặt phẳng vô hạn',formula:'$$\n\\begin{aligned}&\nE_{\\mathrm{wire}} = \\frac{|\\lambda|}{2\\pi\\varepsilon_0r},\\\\&\nE_{\\mathrm{sheet}} = \\frac{|\\sigma|}{2\\varepsilon_0}.\n\\end{aligned}\n$$',description:'Trường vuông góc nguồn, ra xa nếu mật độ dương và hướng về nếu mật độ âm.'},
      {name:'Trên trục đĩa bán kính R',formula:'$$\n\\begin{aligned}&\nE_x = \\frac{\\sigma}{2\\varepsilon_0}\\\\&\n \\quad-\\frac{\\sigma x}{2\\varepsilon_0\\sqrt{x^2+R^2}},\\\\&\nx >0.\n\\end{aligned}\n$$',description:'Mật độ mặt đều. Hai mặt vô hạn song song trái dấu có trường giữa bản bằng $\\frac{|\\sigma|}{\\varepsilon_0}$, trường ngoài bằng không.'}
    ]},
    {id:'dipole',title:'Lưỡng cực trong trường đều',items:[
      {name:'Mômen, mômen lực và thế năng',formula:'$$\n\\begin{aligned}&\np = qd,\\\\&\n\\vec\\tau = \\vec p\\times\\vec E,\\\\&\n\\tau = pE\\sin\\varphi,\\\\&\nU = -pE\\cos\\varphi.\n\\end{aligned}\n$$',description:'q dương, vector mômen hướng từ âm đến dương. Trong trường đều, hợp lực bằng không. Cùng chiều trường là cân bằng bền, ngược chiều là không bền.'},
      {name:'Trường xa trên trục',formula:'$$\nE\\approx\\frac{2kp}{r^3},\\quad r\\gg d\n$$',description:'Trường lưỡng cực ở xa giảm theo nghịch đảo lập phương khoảng cách. Đường sức tiếp tuyến với điện trường, không phải quỹ đạo chung của hạt.'}
    ]}
  ]
}

export const electrostaticsTopics=[
  {title:'Điện tích và sự nhiễm điện',topics:[
    {slug:'dien-tich',title:'Điện tích và cấu tạo vật chất',question:'Điện tích được trao đổi, bảo toàn và lượng tử hóa như thế nào?',source:'21.1'},
    {slug:'vat-dan-cach-dien',title:'Vật dẫn, vật cách điện và sự nhiễm điện',question:'Vì sao một vật mang điện có thể hút vật trung hòa?',source:'21.2'}
  ]},
  {title:'Lực điện và điện trường',topics:[
    {slug:'dinh-luat-coulomb',title:'Định luật Coulomb và chồng chất lực',question:'Làm thế nào xác định đúng độ lớn và hướng tổng lực?',source:'21.3'},
    {slug:'dien-truong-luc-dien',title:'Điện trường và lực điện',question:'Điện trường của nguồn khác lực lên điện tích thử ở đâu?',source:'21.4'},
    {slug:'tinh-dien-truong',title:'Tính trường của các phân bố điện tích',question:'Đối xứng và tích phân giúp cộng trường liên tục như thế nào?',source:'21.5'}
  ]},
  {title:'Hướng trường và lưỡng cực',topics:[
    {slug:'duong-suc-dien',title:'Đường sức điện',question:'Đường sức cho biết hướng và độ lớn trường như thế nào?',source:'21.6'},
    {slug:'luong-cuc-dien',title:'Lưỡng cực điện',question:'Vì sao lưỡng cực quay trong trường đều dù hợp lực bằng không?',source:'21.7'}
  ]}
]
