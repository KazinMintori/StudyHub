export const interferenceTopics=[
  {
    "title": "Giao thoa từ nguồn kết hợp đến phép đo",
    "topics": [
      {
        "slug": "giao-thoa-nguon-ket-hop",
        "title": "Giao thoa và nguồn kết hợp",
        "question": "Vì sao cùng tần số chưa đủ để giữ một hệ vân ổn định?",
        "source": "35.1"
      },
      {
        "slug": "giao-thoa-hai-nguon",
        "title": "Giao thoa ánh sáng từ hai nguồn",
        "question": "Hiệu đường đi quyết định hướng sáng và tối như thế nào?",
        "source": "35.2"
      },
      {
        "slug": "cuong-do-giao-thoa",
        "title": "Cường độ trong hệ vân",
        "question": "Cộng điện trường như thế nào để tính cường độ ở mọi điểm?",
        "source": "35.3"
      },
      {
        "slug": "giao-thoa-mang-mong",
        "title": "Giao thoa ở màng mỏng",
        "question": "Dấu pha phản xạ và đường đi trong màng phối hợp tạo màu ra sao?",
        "source": "35.4"
      },
      {
        "slug": "giao-thoa-ke-michelson",
        "title": "Giao thoa kế Michelson",
        "question": "Vì sao đếm vân có thể đo được dịch chuyển rất nhỏ?",
        "source": "35.5"
      }
    ]
  }
]

export const interferenceSlides=[
  {
    "note": "15-giao-thoa",
    "title": "Chồng chất cộng trường trước khi tính cường độ",
    "bullets": [
      "Mỗi điểm nhận tổng các đóng góp tức thời của những sóng chồng lên nhau.",
      "Với ánh sáng, cộng các thành phần điện trường theo cùng phương.",
      "Cường độ là trung bình của bình phương trường, nên có số hạng phụ thuộc pha."
    ],
    "formula": "$$\nE_{\\rm net}(t)=E_1(t)+E_2(t).\n$$"
  },
  {
    "note": "15-giao-thoa",
    "title": "Nguồn kết hợp giữ quan hệ pha ổn định",
    "bullets": [
      "Hai nguồn đơn sắc cùng tần số có pha tương đối không đổi là nguồn kết hợp.",
      "Nguồn kết hợp có thể lệch pha ban đầu. Đồng pha là một trường hợp riêng.",
      "Chia một nguồn thành hai đường giúp các thay đổi pha chung không phá pha tương đối."
    ],
    "formula": "$$\n\\phi=\\frac{2\\pi\\Delta r}{\\lambda}+\\phi_0.\n$$"
  },
  {
    "note": "15-giao-thoa",
    "title": "Hiệu đường đi chọn các đường cực trị",
    "bullets": [
      "Với hai nguồn đồng pha, hiệu đường đi nguyên bước sóng cho tăng cường.",
      "Hiệu đường đi bán nguyên bước sóng cho triệt giảm.",
      "Triệt tiêu hoàn toàn còn cần hai biên độ tại điểm xét bằng nhau."
    ],
    "formula": "$$\n\\begin{aligned}\\Delta r_{\\max}&=m\\lambda\\\\\\Delta r_{\\min}&=(m+1/2)\\lambda\\\\m&\\in\\mathbb Z.\\end{aligned}\n$$"
  },
  {
    "note": "15-giao-thoa",
    "title": "Màn xa cho hiệu đường đi theo sin góc",
    "bullets": [
      "Khi khoảng quan sát lớn hơn nhiều khoảng nguồn, hai đường tia gần song song.",
      "Góc đo với đường trung trực hai nguồn.",
      "Miền của sin giới hạn những bậc sáng và tối có thể xuất hiện."
    ],
    "formula": "$$\n\\begin{aligned}\\Delta r&\\approx d\\sin\\theta\\\\|\\sin\\theta|&\\le1.\\end{aligned}\n$$"
  },
  {
    "note": "15-giao-thoa",
    "title": "Khoảng vân đều là gần đúng ở góc nhỏ",
    "bullets": [
      "Gần tâm có thể lấy sin và tang gần bằng góc theo radian.",
      "Vị trí vân sáng tỉ lệ bậc, bước sóng và khoảng tới màn.",
      "Ra xa tâm cần giữ riêng sin trong điều kiện pha và tang trong tọa độ màn."
    ],
    "formula": "$$\n\\begin{aligned}y_m&\\approx m\\lambda R/d\\\\\\Delta y&\\approx\\lambda R/d\\\\y&=R\\tan\\theta.\\end{aligned}\n$$"
  },
  {
    "note": "15-giao-thoa",
    "title": "Giản đồ pha cho biên độ tổng",
    "bullets": [
      "Hai vectơ pha cùng quay, có góc cố định bằng pha tương đối.",
      "Biên độ tổng của hai sóng bằng nhau phụ thuộc cos của nửa pha.",
      "Cường độ cực đại của cả hai nguồn bằng bốn lần cường độ một nguồn riêng."
    ],
    "formula": "$$\n\\begin{aligned}E_P&=2E|\\cos(\\phi/2)|\\\\I&=I_0\\cos^2(\\phi/2).\\end{aligned}\n$$"
  },
  {
    "note": "15-giao-thoa",
    "title": "Pha phản xạ cần xét ở từng mặt",
    "bullets": [
      "Phản xạ từ chiết suất nhỏ sang lớn đổi pha nửa chu kỳ.",
      "Phản xạ theo chiều ngược lại không có lần đổi pha ấy trong mô hình tới vuông góc.",
      "Hai lần đổi pha giống nhau không gây chênh pha tương đối."
    ],
    "formula": "$$\nr=\\frac{n_a-n_b}{n_a+n_b}.\n$$"
  },
  {
    "note": "15-giao-thoa",
    "title": "Màng mỏng phối hợp pha truyền và pha phản xạ",
    "bullets": [
      "Tia từ mặt dưới đi thêm hai lần bề dày màng ở gần pháp tuyến.",
      "Dùng bước sóng chân không thì quang lộ thêm là hai lần chiết suất nhân bề dày.",
      "Một lần đảo pha phản xạ tương đối làm các điều kiện sáng và tối đổi vai trò."
    ],
    "formula": "$$\n\\begin{aligned}\\phi&=4\\pi nt/\\lambda_0+\\phi_r\\\\\\phi_{\\max}&=2m\\pi\\\\\\phi_{\\min}&=(2m+1)\\pi.\\end{aligned}\n$$"
  },
  {
    "note": "15-giao-thoa",
    "title": "Bề dày biến thiên tạo các dạng vân",
    "bullets": [
      "Màng nêm có bề dày gần tuyến tính theo vị trí và tạo các vân thẳng.",
      "Mặt cầu gần tiếp xúc mặt phẳng tạo các vòng Newton.",
      "Các lớp phủ điều khiển phản xạ bằng quan hệ pha giữa các đường truyền."
    ],
    "formula": "$$\n\\begin{aligned}t(x)&\\approx\\alpha x\\\\t(r)&\\approx r^2/(2R_c).\\end{aligned}\n$$"
  },
  {
    "note": "15-giao-thoa",
    "title": "Michelson biến độ dời gương thành số vân",
    "bullets": [
      "Bộ chia chùm tạo hai đường rồi tái hợp. Bản bù cân bằng bề dày kính hai đường.",
      "Gương dịch làm đường đi hai lượt thay đổi gấp đôi độ dời trong không khí.",
      "Biết bước sóng có thể đo khoảng cách bằng đếm vân, hoặc dùng độ dời đã biết để suy bước sóng."
    ],
    "formula": "$$\n\\begin{aligned}2y&=N\\lambda\\\\\\lambda&=2y/N.\\end{aligned}\n$$"
  }
]

export const interferenceCheatsheet={
  "title": "Cheatsheet: Giao thoa",
  "lead": "Định nghĩa, tính chất, công thức, điều kiện và ký hiệu của giao thoa hai nguồn, màng mỏng và giao thoa kế.",
  "sections": [
    {
      "id": "coherence",
      "title": "Chồng chất và kết hợp",
      "items": [
        {
          "name": "Chồng chất hai sóng",
          "description": "Cộng các trường tức thời theo cùng thành phần. Với âm, đại lượng cộng có thể là biến thiên áp suất. Cường độ được tính sau khi cộng trường.",
          "formula": "$$\nE_{\\rm net}(t)=E_1(t)+E_2(t).\n$$"
        },
        {
          "name": "Nguồn kết hợp",
          "description": "Hai nguồn đơn sắc cùng tần số có pha tương đối xác định và không đổi trong thời gian quan sát. Đồng pha là trường hợp pha nguồn bằng0 modulo một vòng."
        }
      ]
    },
    {
      "id": "paths",
      "title": "Hiệu đường đi và pha",
      "items": [
        {
          "name": "Pha do truyền",
          "description": "Cùng môi trường đồng nhất, với quy ước hiệu pha và hiệu đường đi nhất quán.",
          "formula": "$$\n\\begin{aligned}k&=2\\pi/\\lambda\\\\\\phi&=k(r_2-r_1)+\\phi_0.\\end{aligned}\n$$",
          "variables": [
            "$r_1,r_2,\\lambda$: Đường đi và bước sóng trong môi trường ($\\mathrm m$).",
            "$k$: Số sóng ($\\mathrm{rad/m}$).",
            "$\\phi,\\phi_0$: Pha tổng và pha nguồn ($\\mathrm{rad}$)."
          ]
        },
        {
          "name": "Cực trị của hai nguồn đồng pha",
          "description": "Pha cực trị không đòi hỏi biên độ bằng nhau. Triệt tiêu hoàn toàn tại cực tiểu cần biên độ bằng nhau và phân cực thích hợp.",
          "formula": "$$\n\\begin{aligned}\\Delta r_{\\max}&=m\\lambda\\\\\\Delta r_{\\min}&=(m+1/2)\\lambda\\\\m&\\in\\mathbb Z.\\end{aligned}\n$$"
        }
      ]
    },
    {
      "id": "double-slit",
      "title": "Hai nguồn và màn",
      "items": [
        {
          "name": "Quan sát xa",
          "description": "Khoảng quan sát lớn hơn nhiều khoảng nguồn. Nguồn đồng pha. Chỉ giữ bậc cho $|\\sin\\theta|\\le1$.",
          "formula": "$$\n\\begin{aligned}&\\Delta r\\approx d\\sin\\theta\\\\&d\\sin\\theta_{\\max}=m\\lambda\\\\&d\\sin\\theta_{\\min}=(m+1/2)\\lambda.\\end{aligned}\n$$",
          "variables": [
            "$d$: Khoảng nguồn ($\\mathrm m$).",
            "$\\theta$: Góc với đường trung trực ($\\mathrm{rad}$ hoặc độ)."
          ]
        },
        {
          "name": "Vị trí và khoảng vân gần tâm",
          "description": "Hai dòng đầu cần góc nhỏ, màn xa và hai khe hẹp. Dòng cuối là tọa độ màn phẳng.",
          "formula": "$$\n\\begin{aligned}y_m&\\approx m\\lambda R/d\\\\\\Delta y&\\approx\\lambda R/d\\\\y&=R\\tan\\theta.\\end{aligned}\n$$",
          "variables": [
            "$R$: Khoảng mặt phẳng nguồn tới màn ($\\mathrm m$).",
            "$y_m,\\Delta y$: Tọa độ và khoảng vân ($\\mathrm m$)."
          ]
        }
      ]
    },
    {
      "id": "intensity",
      "title": "Biên độ và cường độ",
      "items": [
        {
          "name": "Hai biên độ bằng nhau",
          "description": "Hai sóng cùng tần số, phân cực song song. $I_0$ là cường độ cực đại của cả hai sóng, bằng bốn lần cường độ một sóng riêng khi hai đóng góp bằng nhau.",
          "formula": "$$\n\\begin{aligned}E_P&=2E|\\cos(\\phi/2)|\\\\I&=I_0\\cos^2(\\phi/2).\\end{aligned}\n$$",
          "variables": [
            "$E,E_P$: Biên độ điện trường riêng và tổng ($\\mathrm{V/m}$).",
            "$I,I_0$: Cường độ tại điểm và cực đại ($\\mathrm{W/m^2}$)."
          ]
        },
        {
          "name": "Cường độ sóng điện từ trong không khí",
          "description": "Sóng hình sin trong chân không hoặc gần đúng không khí. $E_P$ là biên độ cực đại, khác giá trị hiệu dụng.",
          "formula": "$$\nI=\\frac12\\epsilon_0cE_P^2.\n$$"
        }
      ]
    },
    {
      "id": "reflection",
      "title": "Phản xạ và dấu pha",
      "items": [
        {
          "name": "Hệ số phản xạ điện trường",
          "description": "Tới vuông góc, hai điện môi trong suốt không từ tính. $r$ âm khi $n_b>n_a$, tương ứng đổi pha pi. $r$ dương khi $n_b<n_a$.",
          "formula": "$$\nr=\\frac{E_r}{E_i}=\\frac{n_a-n_b}{n_a+n_b}.\n$$",
          "variables": [
            "$n_a,n_b$: Chiết suất môi trường tới và sau mặt phân cách.",
            "$r$: Hệ số biên độ, không thứ nguyên."
          ]
        },
        {
          "name": "Bước sóng trong màng",
          "description": "Tần số không đổi tại mặt phân cách đứng yên. $\\lambda_0$ là bước sóng chân không, $\\lambda$ là bước sóng trong màng chiết suất n.",
          "formula": "$$\n\\lambda=\\lambda_0/n.\n$$"
        }
      ]
    },
    {
      "id": "film",
      "title": "Màng mỏng tới gần vuông góc",
      "items": [
        {
          "name": "Không chênh pha phản xạ",
          "description": "Hai phản xạ cùng đổi pha hoặc cùng không đổi pha. m nguyên không âm, có loại bậc 0 khi bài yêu cầu bề dày khác 0 hoặc bước sóng hữu hạn.",
          "formula": "$$\n\\begin{aligned}2nt_{\\max R}&=m\\lambda_0\\\\2nt_{\\min R}&=(m+1/2)\\lambda_0.\\end{aligned}\n$$"
        },
        {
          "name": "Chênh pha phản xạ nửa chu kỳ",
          "description": "Chỉ một trong hai phản xạ đổi pha pi. Điều kiện cực trị theo pha, còn triệt tiêu hoàn toàn phụ thuộc biên độ.",
          "formula": "$$\n\\begin{aligned}2nt_{\\max R}&=(m+1/2)\\lambda_0\\\\2nt_{\\min R}&=m\\lambda_0.\\end{aligned}\n$$"
        },
        {
          "name": "Màng nêm và vòng Newton",
          "description": "Màng nêm góc α nhỏ. Công thức cuối cho khe giữa mặt cầu và mặt phẳng, với r nhỏ so với bán kính cong Rc.",
          "formula": "$$\n\\begin{aligned}&t(x)\\approx\\alpha x\\\\&\\Delta x\\approx\\lambda_0/(2n\\alpha)\\\\&t(r)\\approx r^2/(2R_c).\\end{aligned}\n$$",
          "variables": [
            "$t,x,r,R_c$: Các độ dài ($\\mathrm m$).",
            "$\\alpha$: Góc nêm nhỏ ($\\mathrm{rad}$)."
          ]
        }
      ]
    },
    {
      "id": "michelson",
      "title": "Giao thoa kế Michelson",
      "items": [
        {
          "name": "Độ dời gương và số vân",
          "description": "Ánh sáng đi tới gương rồi trở lại trong không khí. N là số vân qua đường chuẩn khi quang lộ thay đổi, không thứ nguyên.",
          "formula": "$$\n\\begin{aligned}2y&=N\\lambda\\\\y&=N\\lambda/2.\\end{aligned}\n$$",
          "variables": [
            "$y,\\lambda$: Độ dời gương và bước sóng ($\\mathrm m$)."
          ]
        },
        {
          "name": "Vai trò bản bù",
          "description": "Bản bù làm hai chùm đi qua cùng bề dày kính trong bố trí cân bằng. Đổi chiết suất hoặc bề dày bản làm đổi quang lộ và hệ vân."
        }
      ]
    }
  ]
}
