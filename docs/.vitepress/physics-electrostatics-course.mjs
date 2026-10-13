const note='01-dien-truong-coulomb'
export const electrostaticsSlides=[
 {note,title:'Điện tích được bảo toàn và lượng tử hóa',bullets:['Điện tích cùng dấu đẩy nhau, trái dấu hút nhau.','Tổng đại số điện tích trong hệ kín giữ nguyên.','Phân cực không bắt buộc làm tổng điện tích khác không.'],formula:'$$\nQ=ne,\\quad n\\in\\mathbb Z\n$$',example:''},
 {note,title:'Lực Coulomb được cộng theo vector',bullets:['Nguồn điểm được dùng khi kích thước nguồn nhỏ so với khoảng cách.','Trong chân không, độ lớn lực tỷ lệ tích độ lớn điện tích và nghịch đảo bình phương khoảng cách.','Hai lực của một cặp bằng nhau về độ lớn và ngược chiều.'],formula:'$$\nF=\\frac{k|q_1q_2|}{r^2}\n$$',example:''},
 {note,title:'Điện trường khác lực lên điện tích thử',bullets:['Trường của nguồn tồn tại dù không đặt điện tích thử tại điểm khảo sát.','Nguồn thử dương chịu lực cùng chiều trường, nguồn thử âm chịu lực ngược chiều.','Vector đơn vị trong trường nguồn điểm hướng từ nguồn đến điểm khảo sát.'],formula:'$$\n\\begin{aligned}&\n\\vec F_0 = q_0\\vec E,\\\\&\n\\vec E = \\frac{kq}{r^2}\\hat{\\mathbf r}.\n\\end{aligned}\n$$',example:''},
 {note,title:'Đối xứng giúp cộng trường liên tục',bullets:['Các trường thành phần đều được tính tại cùng điểm.','Chia nguồn liên tục thành phần nhỏ rồi tích phân vector trường.','Cận tích phân phủ toàn nguồn và không đếm một phần nguồn hai lần.'],formula:'$$\n\\begin{aligned}&\\vec E=\\vec E_1+\\vec E_2\\\\&\\quad+\\cdots+\\vec E_n\\\\&\\quad=\\sum_{i=1}^{n}\\vec E_i.\\end{aligned}\n$$',example:''},
 {note,title:'Đường sức biểu diễn hướng điện trường',bullets:['Tiếp tuyến đường sức cùng hướng trường tại mỗi điểm.','Các đường không cắt nhau, mật độ đường biểu diễn độ mạnh tương đối của trường.','Đường sức nhìn chung khác quỹ đạo của hạt mang điện.'],formula:'',example:''},
 {note,title:'Lưỡng cực có thể quay khi hợp lực bằng không',bullets:['Mômen lưỡng cực hướng từ âm đến dương.','Trong trường đều, hai lực bù nhau nhưng có thể tạo mômen.','Cùng chiều trường là cân bằng bền, ngược chiều là không bền.'],formula:'$$\n\\begin{aligned}&\np = qd,\\\\&\n\\vec\\tau = \\vec p\\times\\vec E,\\\\&\nU = -\\vec p\\cdot\\vec E.\n\\end{aligned}\n$$',example:''}
]

export const electrostaticsCheatsheet={
  summary:'Các định nghĩa, tính chất và công thức của chương Điện tích và điện trường.',
  sections:[
    {id:'charge',title:'Điện tích',items:[
      {name:'Bảo toàn và lượng tử hóa',formulaRows:[
        {label:'Tổng điện tích trong hệ kín được bảo toàn',formula:'$$\nQ_{\\mathrm{tong}}=Q_0\n$$'},
        {label:'Điện tích của vật cô lập được lượng tử hóa',formula:'$$\nQ=ne,\\quad n\\in\\mathbb Z\n$$'},
        {label:'Độ lớn điện tích cơ bản, chính xác theo định nghĩa',formula:'$$\n\\begin{aligned}&\ne = 1.602176634\\\\&\n \\quad\\times10^{-19}\\,\\mathrm C.\n\\end{aligned}\n$$'}
      ],variables:[
        String.raw`$Q_{\mathrm{tong}}$: Tổng đại số điện tích trong một hệ kín ($\mathrm{C}$)`,
        String.raw`$Q$: Điện tích của vật cô lập mang điện ($\mathrm{C}$)`,
        String.raw`$n$: Số nguyên lượng tử hóa điện tích (Không có đơn vị)`,
        String.raw`$e$: Độ lớn điện tích nguyên tố ($\approx 1{,}602\times10^{-19}\,\mathrm{C}$)`
      ],description:'Điện tích cùng dấu đẩy nhau, trái dấu hút nhau. Vật dẫn cho điện tích dễ di chuyển, vật cách điện thì không. Phân cực không bắt buộc tạo điện tích tổng khác không.'}
    ]},
    {id:'force-field',title:'Lực điện và điện trường',items:[
      {name:'Hai điện tích điểm trong chân không',formula:'$$\n\\begin{aligned}&\nF = k\\frac{|q_1q_2|}{r^2},\\\\&\nk = \\frac1{4\\pi\\varepsilon_0}.\n\\end{aligned}\n$$',variables:[
        String.raw`$F$: Độ lớn lực tĩnh điện Coulomb giữa hai điện tích điểm ($\mathrm{N}$)`,
        String.raw`$q_1, q_2$: Điện tích của hai hạt mang điện ($\mathrm{C}$)`,
        String.raw`$r$: Khoảng cách giữa hai điện tích điểm ($\mathrm{m}$)`,
        String.raw`$k$: Hằng số tĩnh điện Coulomb ($\approx 8{,}99\times10^9\,\mathrm{N\cdot m^2/C^2}$)`,
        String.raw`$\varepsilon_0$: Hằng số điện môi chân không ($\approx 8{,}854\times10^{-12}\,\mathrm{F/m}$)`
      ],description:'r là khoảng cách dương giữa nguồn. Lực nằm trên đường nối hai nguồn. Hai lực của một cặp tuân theo định luật III Newton.'},
      {name:'Trường và lực lên điện tích điểm',formula:'$$\n\\begin{aligned}&\n\\vec E = \\frac{\\vec F_0}{q_0},\\quad q_0\\ne0,\\\\&\n\\vec F_0 = q_0\\vec E,\\\\&\n\\vec E_{\\mathrm{point}} = k\\frac q{r^2}\\hat{\\mathbf r}.\n\\end{aligned}\n$$',variables:[
        String.raw`$\vec E$: Vector cường độ điện trường ($\mathrm{N/C}$ hoặc $\mathrm{V/m}$)`,
        String.raw`$\vec F_0$: Vector lực điện tác dụng lên điện tích thử ($\mathrm{N}$)`,
        String.raw`$q_0$: Điện tích thử đặt tại điểm khảo sát ($\mathrm{C}$)`,
        String.raw`$q$: Điện tích nguồn tạo ra điện trường ($\mathrm{C}$)`,
        String.raw`$\hat{\mathbf r}$: Vector đơn vị hướng từ điện tích nguồn tới điểm khảo sát (Không có đơn vị)`
      ],description:'Vector đơn vị hướng từ nguồn đến điểm trường. Đơn vị trường là N/C. Nguồn dương tạo trường ra xa, nguồn âm tạo trường hướng về. Trường trong vật liệu dẫn ở cân bằng tĩnh điện bằng không.'}
    ]},
    {id:'distribution',title:'Chồng chất và mật độ điện tích',items:[
      {name:'Các nguồn rời rạc',formula:'$$\n\\begin{aligned}&\\vec E=\\vec E_1+\\vec E_2\\\\&\\quad+\\cdots+\\vec E_n\\\\&\\quad=\\sum_{i=1}^{n}\\vec E_i.\\end{aligned}\n$$',variables:[
        String.raw`$\vec E$: Vector cường độ điện trường tổng hợp ($\mathrm{N/C}$)`,
        String.raw`$\vec E_i$: Điện trường do điện tích nguồn thứ $i$ sinh ra tại điểm khảo sát ($\mathrm{N/C}$)`
      ],description:'Các thành phần đều được tính tại cùng điểm khảo sát, trong đó chỉ số i chạy từ 1 đến n qua các nguồn.'},
      {name:'Nguồn liên tục',formula:'$$\n\\begin{aligned}&\ndq = \\lambda\\,d\\ell,\\\\&\ndq = \\sigma\\,dA,\\\\&\ndq = \\rho\\,dV,\\\\&\nd\\vec E = k\\frac{dq}{r^2}\\hat{\\mathbf r},\\\\&\n\\vec E = \\int_{\\mathrm{src}}d\\vec E.\n\\end{aligned}\n$$',variables:[
        String.raw`$dq$: Phần tử điện tích vi phân của nguồn ($\mathrm{C}$)`,
        String.raw`$\lambda$: Mật độ điện tích dài ($\mathrm{C/m}$)`,
        String.raw`$\sigma$: Mật độ điện tích mặt ($\mathrm{C/m^2}$)`,
        String.raw`$\rho$: Mật độ điện tích thể tích ($\mathrm{C/m^3}$)`,
        String.raw`$d\vec E$: Điện trường vi phân do phần tử $dq$ gây ra ($\mathrm{N/C}$)`
      ],description:'Mật độ dài đo bằng C/m, mật độ mặt bằng C/m² và mật độ thể tích bằng C/m³.'}
    ]},
    {id:'standard-fields',title:'Các phân bố điện tích đều',items:[
      {name:'Trên trục vòng bán kính a',formula:'$$\n\\begin{aligned}&\nE_x = \\frac{kQx}{(x^2+a^2)^{3/2}},\\\\&\n\\vec E = E_x\\hat{\\mathbf i}.\n\\end{aligned}\n$$',variables:[
        String.raw`$E_x$: Thành phần điện trường dọc theo trục đối xứng của vòng dây ($\mathrm{N/C}$)`,
        String.raw`$Q$: Tổng điện tích phân bố đều trên vòng dây tròn ($\mathrm{C}$)`,
        String.raw`$a$: Bán kính của vòng dây tròn mang điện ($\mathrm{m}$)`,
        String.raw`$x$: Khoảng cách trên trục đo từ tâm vòng dây đến điểm khảo sát ($\mathrm{m}$)`
      ],description:'x đo từ tâm theo trục vòng. Trường tại tâm bằng không. Ở xa vòng, trường gần như nguồn điểm.'},
      {name:'Trên trung trực đoạn dây dài 2a',formula:'$$\n\\begin{aligned}&\nE_x = \\frac{kQ}{x\\sqrt{x^2+a^2}},\\\\&\n\\vec E = E_x\\hat{\\mathbf i},\\quad x>0.\n\\end{aligned}\n$$',variables:[
        String.raw`$E_x$: Điện trường trên đường trung trực của đoạn dây thẳng ($\mathrm{N/C}$)`,
        String.raw`$Q$: Tổng điện tích phân bố đều trên đoạn dây ($\mathrm{C}$)`,
        String.raw`$a$: Nửa chiều dài của đoạn dây thẳng mang điện ($\mathrm{m}$)`,
        String.raw`$x$: Khoảng cách vuông góc từ điểm khảo sát đến tâm đoạn dây ($x > 0$) ($\mathrm{m}$)`
      ],description:'Q phân bố đều từ y = −a đến y = +a. Thành phần y triệt tiêu.'},
      {name:'Dây vô hạn và mặt phẳng vô hạn',formula:'$$\n\\begin{aligned}&\nE_{\\mathrm{wire}} = \\frac{|\\lambda|}{2\\pi\\varepsilon_0r},\\\\&\nE_{\\mathrm{sheet}} = \\frac{|\\sigma|}{2\\varepsilon_0}.\n\\end{aligned}\n$$',variables:[
        String.raw`$E_{\mathrm{wire}}$: Điện trường quanh dây dẫn thẳng dài vô hạn ($\mathrm{N/C}$)`,
        String.raw`$E_{\mathrm{sheet}}$: Điện trường gần mặt phẳng rộng vô hạn mang điện đều ($\mathrm{N/C}$)`,
        String.raw`$|\lambda|$: Độ lớn mật độ điện tích dài của dây thẳng ($\mathrm{C/m}$)`,
        String.raw`$|\sigma|$: Độ lớn mật độ điện tích mặt của tấm phẳng ($\mathrm{C/m^2}$)`,
        String.raw`$r$: Khoảng cách vuông góc từ điểm khảo sát đến dây dẫn ($\mathrm{m}$)`
      ],description:'Trường vuông góc nguồn, ra xa nếu mật độ dương và hướng về nếu mật độ âm.'},
      {name:'Trên trục đĩa bán kính R',formula:'$$\n\\begin{aligned}&\nE_x = \\frac{\\sigma}{2\\varepsilon_0}\\\\&\n \\quad-\\frac{\\sigma x}{2\\varepsilon_0\\sqrt{x^2+R^2}},\\\\&\nx >0.\n\\end{aligned}\n$$',variables:[
        String.raw`$E_x$: Điện trường trên trục vuông góc đi qua tâm đĩa tròn mang điện ($\mathrm{N/C}$)`,
        String.raw`$\sigma$: Mật độ điện tích mặt phân bố đều trên đĩa ($\mathrm{C/m^2}$)`,
        String.raw`$R$: Bán kính của đĩa tròn mang điện ($\mathrm{m}$)`,
        String.raw`$x$: Khoảng cách từ tâm đĩa đến điểm khảo sát dọc theo trục ($x > 0$) ($\mathrm{m}$)`
      ],description:'Mật độ mặt đều. Hai mặt vô hạn song song trái dấu có trường giữa bản bằng $\\frac{|\\sigma|}{\\varepsilon_0}$, trường ngoài bằng không.'}
    ]},
    {id:'dipole',title:'Lưỡng cực trong trường đều',items:[
      {name:'Mômen, mômen lực và thế năng',formula:'$$\n\\begin{aligned}&\np = qd,\\\\&\n\\vec\\tau = \\vec p\\times\\vec E,\\\\&\n\\tau = pE\\sin\\varphi,\\\\&\nU = -pE\\cos\\varphi.\n\\end{aligned}\n$$',variables:[
        String.raw`$p$: Độ lớn mômen lưỡng cực điện ($p = qd$) ($\mathrm{C\cdot m}$)`,
        String.raw`$d$: Khoảng cách giữa hai điện tích trái dấu của lưỡng cực ($\mathrm{m}$)`,
        String.raw`$\vec\tau$: Vector mômen lực tác dụng lên lưỡng cực điện ($\mathrm{N\cdot m}$)`,
        String.raw`$U$: Thế năng tĩnh điện của lưỡng cực trong điện trường đều ($\mathrm{J}$)`,
        String.raw`$\varphi$: Góc hợp bởi vector $\vec p$ và vector $\vec E$ ($\mathrm{rad}$ hoặc độ)`
      ],description:'q dương, vector mômen hướng từ âm đến dương. Trong trường đều, hợp lực bằng không. Cùng chiều trường là cân bằng bền, ngược chiều là không bền.'},
      {name:'Trường xa trên trục',formula:'$$\nE\\approx\\frac{2kp}{r^3},\\quad r\\gg d\n$$',variables:[
        String.raw`$E$: Độ lớn điện trường trên trục lưỡng cực ở khoảng cách xa ($\mathrm{N/C}$)`,
        String.raw`$p$: Mômen lưỡng cực điện ($\mathrm{C\cdot m}$)`,
        String.raw`$r$: Khoảng cách từ tâm lưỡng cực đến điểm khảo sát ($r \gg d$) ($\mathrm{m}$)`
      ],description:'Trường lưỡng cực ở xa giảm theo nghịch đảo lập phương khoảng cách. Đường sức tiếp tuyến với điện trường, không phải quỹ đạo chung của hạt.'}
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
