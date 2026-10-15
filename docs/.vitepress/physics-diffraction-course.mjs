export const diffractionTopics=[
  {
    "title": "Từ khẩu độ tới cấu trúc và hình ảnh",
    "topics": [
      {
        "slug": "nhieu-xa-fresnel-fraunhofer",
        "title": "Nhiễu xạ Fresnel và Fraunhofer",
        "question": "Khi nào cần xét độ cong mặt sóng?",
        "source": "36.1"
      },
      {
        "slug": "nhieu-xa-mot-khe",
        "title": "Nhiễu xạ qua một khe",
        "question": "Vì sao một khe vẫn tạo được các vân tối?",
        "source": "36.2"
      },
      {
        "slug": "cuong-do-nhieu-xa-mot-khe",
        "title": "Cường độ nhiễu xạ một khe",
        "question": "Tổng các sóng từ toàn khe cho phân bố cường độ nào?",
        "source": "36.3"
      },
      {
        "slug": "nhieu-khe",
        "title": "Hệ nhiều khe",
        "question": "Bao nhiễu xạ và pha giữa các khe phối hợp thế nào?",
        "source": "36.4"
      },
      {
        "slug": "cach-tu-nhieu-xa",
        "title": "Cách tử nhiễu xạ",
        "question": "Vì sao nhiều khe giúp đo và phân giải bước sóng?",
        "source": "36.5"
      },
      {
        "slug": "nhieu-xa-tia-x",
        "title": "Nhiễu xạ tia X",
        "question": "Góc Bragg cho biết khoảng mặt mạng ra sao?",
        "source": "36.6"
      },
      {
        "slug": "khau-do-tron-phan-giai",
        "title": "Khẩu độ tròn và phân giải",
        "question": "Vì sao phóng to ảnh chưa chắc thấy thêm chi tiết?",
        "source": "36.7"
      },
      {
        "slug": "anh-toan-ky",
        "title": "Ảnh toàn ký",
        "question": "Ghi hệ vân như thế nào để tái tạo mặt sóng ba chiều?",
        "source": "36.8"
      }
    ]
  }
]

export const diffractionSlides=[
  {
    "note": "16-nhieu-xa",
    "title": "Nhiễu xạ là chồng chất các phần mặt sóng",
    "bullets": [
      "Mỗi phần của khẩu độ đóng góp một sóng thứ cấp.",
      "Fraunhofer dùng các hướng gần song song ở miền xa hoặc tiêu diện.",
      "Fresnel cần giữ độ cong mặt sóng khi hình học còn ở miền gần."
    ],
    "formula": "$$\nE_P=E_1+E_2.\n$$"
  },
  {
    "note": "16-nhieu-xa",
    "title": "Cực tiểu khe đơn cần triệt tiêu toàn khe",
    "bullets": [
      "Hai nửa khe có thể ghép thành các cặp ngược pha ở cực tiểu đầu.",
      "Bậc không khác không phân biệt cực tiểu với tâm cực đại.",
      "Khe càng hẹp, góc mở trung tâm càng lớn."
    ],
    "formula": "$$\n\\begin{aligned}a\\sin\\theta_m&=m\\lambda\\\\m&=\\pm1,\\pm2,\\ldots.\\end{aligned}\n$$"
  },
  {
    "note": "16-nhieu-xa",
    "title": "Cường độ khe đơn không giảm tuyến tính",
    "bullets": [
      "Đối số là nửa độ lệch pha giữa hai mép khe.",
      "Tại tâm, dùng giới hạn để được cường độ cực đại.",
      "Các cực đại phụ được tìm từ phương trình tang bằng đối số."
    ],
    "formula": "$$\n\\begin{aligned}\\gamma&=\\pi a\\sin\\theta/\\lambda\\\\I&=I_0(\\sin\\gamma/\\gamma)^2.\\end{aligned}\n$$"
  },
  {
    "note": "16-nhieu-xa",
    "title": "Vị trí trên màn cần phân biệt sin và tang",
    "bullets": [
      "Điều kiện pha dùng sin của góc.",
      "Tọa độ trên màn phẳng dùng tang của góc.",
      "Công thức bề rộng tỉ lệ nghịch khe cần góc nhỏ."
    ],
    "formula": "$$\n\\begin{aligned}y_m&=R\\tan\\theta_m\\\\y_m&\\approx Rm\\lambda/a.\\end{aligned}\n$$"
  },
  {
    "note": "16-nhieu-xa",
    "title": "Vân giao thoa nằm trong bao nhiễu xạ",
    "bullets": [
      "Khoảng tâm khe quyết định nhịp của thừa số giao thoa.",
      "Bề rộng mỗi khe quyết định bao nhiễu xạ.",
      "Một bậc bị khuyết khi cực đại giao thoa trùng cực tiểu của bao."
    ],
    "formula": "$$\n\\begin{aligned}d\\sin\\theta&=m_i\\lambda\\\\a\\sin\\theta&=m_d\\lambda\\\\m_i&=(d/a)m_d.\\end{aligned}\n$$"
  },
  {
    "note": "16-nhieu-xa",
    "title": "Nhiều khe cho cực đại chính hẹp",
    "bullets": [
      "Vị trí cực đại chính giữ cùng điều kiện pha giữa các khe kề nhau.",
      "Có N trừ một cực tiểu giữa hai cực đại chính.",
      "Bề rộng theo pha tỉ lệ nghịch số khe khi các đóng góp cùng biên độ."
    ],
    "formula": "$$\n\\begin{aligned}I_{\\max}&=N^2I_s\\\\\\Delta\\phi&=4\\pi/N.\\end{aligned}\n$$"
  },
  {
    "note": "16-nhieu-xa",
    "title": "Cách tử tách bước sóng theo góc",
    "bullets": [
      "Ở tới vuông góc, cực đại có hiệu đường đi nguyên bước sóng.",
      "Bước sóng dài hơn lệch nhiều hơn trên cùng phía và cùng bậc.",
      "Bậc cao có thể chồng phổ với những bậc khác."
    ],
    "formula": "$$\nd\\sin\\theta_m=m\\lambda.\n$$"
  },
  {
    "note": "16-nhieu-xa",
    "title": "Năng suất phân giải phổ phụ thuộc số khe",
    "bullets": [
      "Hai vạch vừa phân giải khi đỉnh một vạch trùng cực tiểu đầu của vạch kia.",
      "Số khe được chiếu sáng và bậc phổ cùng làm tăng độ phân giải.",
      "Điều kiện góc tồn tại vẫn giới hạn các bậc dùng được."
    ],
    "formula": "$$\n\\mathcal R=\\lambda/\\Delta\\lambda=mN.\n$$"
  },
  {
    "note": "16-nhieu-xa",
    "title": "Bragg dùng góc với mặt mạng",
    "bullets": [
      "Các nguyên tử trong mỗi mặt tán xạ kết hợp theo hướng phản xạ.",
      "Hai mặt mạng liên tiếp tạo thêm cả đường vào và đường ra.",
      "Dùng bước sóng trong môi trường của mạng tán xạ."
    ],
    "formula": "$$\n\\begin{aligned}2d\\sin\\theta&=m\\lambda\\\\m&=1,2,3,\\ldots.\\end{aligned}\n$$"
  },
  {
    "note": "16-nhieu-xa",
    "title": "Khẩu độ tròn tạo đĩa Airy và giới hạn chi tiết",
    "bullets": [
      "Một vật điểm cho ảnh có bề rộng hữu hạn.",
      "Tiêu chuẩn Rayleigh so độ tách hai ảnh với vòng tối đầu.",
      "Khẩu độ lớn hơn và bước sóng ngắn hơn giảm giới hạn góc."
    ],
    "formula": "$$\n\\sin\\theta_R=1{,}22\\lambda/D.\n$$"
  },
  {
    "note": "16-nhieu-xa",
    "title": "Ảnh toàn ký tái tạo sóng hội tụ và phân kỳ",
    "bullets": [
      "Chùm vật và chùm chuẩn cùng ghi hệ vân trên phim.",
      "Chiếu chùm thích hợp lên bản ghi có thể tạo ảnh thật và ảnh ảo.",
      "Quan hệ pha và độ ổn định cơ học phải được giữ trong lúc ghi."
    ],
    "formula": "$$\n\\begin{aligned}b_m-b_0&=m\\lambda\\\\r_m^2&=2m\\lambda b_0+m^2\\lambda^2.\\end{aligned}\n$$"
  }
]

export const diffractionCheatsheet={
  "title": "Nhiễu xạ",
  "description": "Định nghĩa, tính chất và công thức của khe đơn, nhiều khe, cách tử, tinh thể, khẩu độ tròn và ảnh toàn ký.",
  "sections": [
    {
      "id": "regimes",
      "title": "Miền gần và miền xa",
      "items": [
        {
          "name": "Fresnel",
          "description": "Nguồn hoặc điểm quan sát tương đối gần khẩu độ. Độ cong mặt sóng phải được giữ trong phép tính pha."
        },
        {
          "name": "Fraunhofer",
          "description": "Sóng tới và các đường từ khẩu độ tới điểm xét được coi gần song song. Có thể thực hiện trong tiêu diện thấu kính."
        }
      ]
    },
    {
      "id": "single-slit",
      "title": "Khe đơn",
      "items": [
        {
          "name": "Cực tiểu",
          "description": "Khe chiếu đều, sóng tới phẳng, quan sát Fraunhofer. Loại bậc không và giữ miền của sin.",
          "formula": "$$\n\\begin{aligned}a\\sin\\theta_m&=m\\lambda\\\\m&=\\pm1,\\pm2,\\ldots.\\end{aligned}\n$$",
          "variables": [
            "$a,\\lambda$: Bề rộng khe và bước sóng ($\\mathrm m$).",
            "$\\theta_m$: Góc so với trục ban đầu."
          ]
        },
        {
          "name": "Vị trí và bề rộng trung tâm",
          "description": "Dòng đầu là hình học màn phẳng. Hai dòng sau cần góc nhỏ và miền xa.",
          "formula": "$$\n\\begin{aligned}y_m&=R\\tan\\theta_m\\\\y_m&\\approx m\\lambda R/a\\\\W_0&\\approx2\\lambda R/a.\\end{aligned}\n$$"
        },
        {
          "name": "Cường độ",
          "description": "Chuẩn $I_0$ là đỉnh trung tâm. Tại đối số bằng không, dùng giới hạn bằng một.",
          "formula": "$$\n\\begin{aligned}\\gamma&=\\pi a\\sin\\theta/\\lambda\\\\I&=I_0(\\sin\\gamma/\\gamma)^2.\\end{aligned}\n$$"
        },
        {
          "name": "Cực đại phụ",
          "description": "Các nghiệm dương khác không nằm ngoài cực đại trung tâm. Các cực tiểu có đối số là bội nguyên khác không của pi.",
          "formula": "$$\n\\tan\\gamma=\\gamma.\n$$"
        }
      ]
    },
    {
      "id": "two-slits",
      "title": "Hai khe rộng và bậc khuyết",
      "items": [
        {
          "name": "Cường độ hai khe giống nhau",
          "description": "Các khe kết hợp đồng pha. $I_0$ là cường độ đỉnh của toàn hệ. $S$ mô tả bao khe đơn, $C$ mô tả pha giữa hai tâm.",
          "formula": "$$\n\\begin{aligned}\\gamma&=\\pi a\\sin\\theta/\\lambda\\\\S&=\\sin\\gamma/\\gamma\\\\C&=\\cos(\\pi d\\sin\\theta/\\lambda)\\\\I&=I_0S^2C^2.\\end{aligned}\n$$"
        },
        {
          "name": "Điều kiện bậc khuyết",
          "description": "Bậc nhiễu xạ $m_d$ khác không. Cả hai bậc đều nguyên và các hướng phải tồn tại.",
          "formula": "$$\n\\begin{aligned}d\\sin\\theta&=m_i\\lambda\\\\a\\sin\\theta&=m_d\\lambda\\\\m_i&=(d/a)m_d.\\end{aligned}\n$$"
        }
      ]
    },
    {
      "id": "many-slits",
      "title": "N khe và cách tử",
      "items": [
        {
          "name": "Cực đại chính",
          "description": "N khe giống nhau, kết hợp, đồng pha, cách tâm đều d. $I_s$ là cường độ của một khe riêng.",
          "formula": "$$\n\\begin{aligned}d\\sin\\theta_m&=m\\lambda\\\\m&=0,\\pm1,\\pm2,\\ldots\\\\I_{\\max}&=N^2I_s.\\end{aligned}\n$$"
        },
        {
          "name": "Phân bố nhiều khe",
          "description": "Miền xa, bỏ qua biến thiên bao của một khe. Tại pha là bội hai pi, dùng giới hạn thay dạng không trên không.",
          "formula": "$$\n\\begin{aligned}\\phi&=2\\pi d\\sin\\theta/\\lambda\\\\A&=\\frac{\\sin(N\\phi/2)}{\\sin(\\phi/2)}\\\\I&=I_sA^2.\\end{aligned}\n$$"
        },
        {
          "name": "Cực tiểu và bề rộng",
          "description": "Giữa hai cực đại chính có N trừ một cực tiểu. Bề rộng pha là khoảng giữa hai cực tiểu sát đỉnh.",
          "formula": "$$\n\\begin{aligned}\\phi_q&=2\\pi q/N\\\\q&=1,2,\\ldots,N-1\\\\\\Delta\\phi&=4\\pi/N.\\end{aligned}\n$$"
        },
        {
          "name": "Phân giải phổ",
          "description": "N là số khe được chiếu sáng. m là bậc phổ dương đang dùng. Đây là tiêu chuẩn hai đỉnh phổ, khác độ phân giải ảnh.",
          "formula": "$$\n\\mathcal R=\\lambda/\\Delta\\lambda=mN.\n$$"
        }
      ]
    },
    {
      "id": "crystal",
      "title": "Nhiễu xạ tinh thể",
      "items": [
        {
          "name": "Điều kiện Bragg",
          "description": "Góc đo với mặt mạng. d là khoảng hai mặt trong họ đang xét. Dùng bước sóng trong môi trường.",
          "formula": "$$\n\\begin{aligned}2d\\sin\\theta&=m\\lambda\\\\m&=1,2,3,\\ldots\\\\m\\lambda&\\le2d.\\end{aligned}\n$$"
        }
      ]
    },
    {
      "id": "circular",
      "title": "Khẩu độ tròn và ảnh",
      "items": [
        {
          "name": "Các vòng tối",
          "description": "D là đường kính khẩu độ. Các góc là bán kính góc tính từ tâm.",
          "formula": "$$\n\\begin{aligned}\\sin\\theta_1&=1{,}22\\lambda/D\\\\\\sin\\theta_2&=2{,}23\\lambda/D\\\\\\sin\\theta_3&=3{,}24\\lambda/D.\\end{aligned}\n$$"
        },
        {
          "name": "Tiêu chuẩn Rayleigh",
          "description": "Hai điểm vừa được phân giải khi độ tách góc bằng bán kính góc vòng tối đầu. Công thức tuyến tính cần góc nhỏ.",
          "formula": "$$\n\\begin{aligned}\\sin\\theta_R&=1{,}22\\lambda/D\\\\s_{\\min}&\\approx R\\theta_R.\\end{aligned}\n$$"
        },
        {
          "name": "Đĩa Airy trên tiêu diện",
          "description": "Nguồn ở xa, khẩu độ tròn, gần đúng góc nhỏ. f là tiêu cự, N là chỉ số khẩu độ.",
          "formula": "$$\n\\begin{aligned}\\rho_1&\\approx1{,}22\\lambda f/D\\\\N&=f/D\\\\\\rho_1&\\approx1{,}22\\lambda N.\\end{aligned}\n$$"
        }
      ]
    },
    {
      "id": "hologram",
      "title": "Ảnh toàn ký",
      "items": [
        {
          "name": "Các vành ghi một điểm",
          "description": "Sóng chuẩn phẳng tới vuông góc và cùng pha tại tâm với sóng cầu. b₀ là khoảng từ điểm tới phim, rₘ là bán kính vành.",
          "formula": "$$\n\\begin{aligned}b_m-b_0&=m\\lambda\\\\r_m^2&=2m\\lambda b_0+m^2\\lambda^2.\\end{aligned}\n$$"
        },
        {
          "name": "Gần đúng cận trục",
          "description": "Cần $m\\lambda\\ll b_0$. Đổi bước sóng tái tạo làm đổi vị trí trục trong mô hình sóng chuẩn phẳng.",
          "formula": "$$\nr_m\\approx\\sqrt{2m\\lambda b_0}.\n$$"
        }
      ]
    }
  ]
}
