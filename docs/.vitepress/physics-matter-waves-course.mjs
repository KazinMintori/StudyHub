export const matterWavesCheatsheet={
  "title": "Cheatsheet: Tính sóng của hạt",
  "description": "Định nghĩa, tính chất, điều kiện và công thức của sóng vật chất, nguyên tử, laser, bức xạ nhiệt và bất định.",
  "sections": [
    {
      "id": "matter",
      "title": "Sóng vật chất",
      "items": [
        {
          "name": "Bước sóng de Broglie",
          "description": "Hạt tự do có độ lớn động lượng $p$. Với hạt chậm, $p\\approx mv$. Ở tốc độ lớn dùng động lượng tương đối tính.",
          "formula": "$$\n\\lambda=h/p.\n$$",
          "variables": []
        },
        {
          "name": "Tần số sóng hạt tự do",
          "description": "E là năng lượng toàn phần theo mô tả tương đối tính. Hạt có khối lượng nghỉ khác không không tuân theo $E=pc$ hoặc $f=c/\\lambda$ của photon.",
          "formula": "$$\n\\begin{aligned}E&=hf\\\\E^2&=(mc^2)^2+(pc)^2.\\end{aligned}\n$$",
          "variables": []
        },
        {
          "name": "Gia tốc electron chậm từ nghỉ",
          "description": "$V_{ba}>0$ là độ tăng điện thế electron đi qua, e là độ lớn điện tích. Bỏ động năng ban đầu và dùng gần đúng phi tương đối tính.",
          "formula": "$$\n\\begin{aligned}K&=eV_{ba}\\\\p&=\\sqrt{2meV_{ba}}\\\\\\lambda&=h/\\sqrt{2meV_{ba}}.\\end{aligned}\n$$",
          "variables": []
        },
        {
          "name": "Cực đại của các sóng tán xạ cùng pha",
          "description": "Trong bố trí một hàng nguyên tử được chiếu với pha tới bằng nhau, d là khoảng cách giữa các tâm tán xạ. m là số nguyên và góc θ theo hình học bố trí đang xét.",
          "formula": "$$\nd\\sin\\theta=m\\lambda.\n$$",
          "variables": []
        }
      ]
    },
    {
      "id": "nucleus",
      "title": "Mô hình hạt nhân và mức năng lượng",
      "items": [
        {
          "name": "Tiếp cận trực diện hạt nhân nặng",
          "description": "Hạt nhân coi như đứng yên, thế năng ở vô cực bằng không. q và Q cùng dấu. $K_0$ là động năng của hạt tới ở xa.",
          "formula": "$$\nr_{\\min}=\\frac{qQ}{4\\pi\\epsilon_0K_0}.\n$$",
          "variables": []
        },
        {
          "name": "Chuyển mức phát photon",
          "description": "$E_i>E_f$. Năng lượng photon bằng chênh lệch mức, bỏ qua động năng giật lùi của nguyên tử khi nhỏ.",
          "formula": "$$\nhf=hc/\\lambda=E_i-E_f.\n$$",
          "variables": []
        },
        {
          "name": "Hấp thụ cộng hưởng",
          "description": "$E_f>E_i$. Photon phải phù hợp chênh lệch năng lượng của chuyển mức được phép. Cần nêu độ rộng vạch khi vượt mô hình mức sắc.",
          "formula": "$$\nhf=E_f-E_i.\n$$",
          "variables": []
        }
      ]
    },
    {
      "id": "bohr",
      "title": "Mô hình Bohr",
      "items": [
        {
          "name": "Lượng tử hóa mômen động lượng",
          "description": "Quỹ đạo tròn trong mô hình Bohr, hạt nhân cố định. n là số nguyên dương.",
          "formula": "$$\nL_n=mv_nr_n=n\\hbar.\n$$",
          "variables": []
        },
        {
          "name": "Điều kiện vòng sóng",
          "description": "Chu vi quỹ đạo chứa n bước sóng de Broglie. Đây là cách diễn giải bán cổ điển, không phải quỹ đạo thật của trạng thái lượng tử.",
          "formula": "$$\n2\\pi r_n=n\\lambda_n.\n$$",
          "variables": []
        },
        {
          "name": "Bán kính và tốc độ của hydrogen",
          "description": "$a_0$ là bán kính Bohr. Mô hình hạt nhân cố định và electron phi tương đối tính.",
          "formula": "$$\n\\begin{aligned}r_n&=n^2a_0\\\\a_0&=\\epsilon_0h^2/(\\pi me^2)\\\\v_n&=e^2/(2\\epsilon_0nh).\\end{aligned}\n$$",
          "variables": []
        },
        {
          "name": "Động năng, thế năng và cơ năng",
          "description": "Mốc thế năng là electron và hạt nhân ở xa nhau vô hạn. $E_n$ là cơ năng liên kết, không gồm năng lượng nghỉ.",
          "formula": "$$\n\\begin{aligned}K_n&=hcR/n^2\\\\U_n&=-2K_n\\\\E_n&=-K_n=U_n/2.\\end{aligned}\n$$",
          "variables": []
        }
      ]
    },
    {
      "id": "spectra",
      "title": "Phổ và hiệu chỉnh khối lượng",
      "items": [
        {
          "name": "Bước sóng chuyển mức hydrogen",
          "description": "$n_U>n_L$ là hai số nguyên dương. R là hằng số Rydberg phù hợp với khối lượng hạt nhân đang xét.",
          "formula": "$$\n\\frac1\\lambda=R\\left(\\frac1{n_L^2}-\\frac1{n_U^2}\\right).\n$$",
          "variables": []
        },
        {
          "name": "Hằng số Rydberg",
          "description": "Công thức hạt nhân cố định dùng khối lượng electron m. Hiệu chỉnh chuyển động hạt nhân dùng khối lượng rút gọn tương ứng.",
          "formula": "$$\nR=\\frac{me^4}{8\\epsilon_0^2h^3c}.\n$$",
          "variables": []
        },
        {
          "name": "Ion hóa từ mức n",
          "description": "Năng lượng tối thiểu đưa electron từ mức liên kết n ra vô cực với động năng cuối bằng không.",
          "formula": "$$\nE_{\\rm ion}=-E_n.\n$$",
          "variables": []
        },
        {
          "name": "Khối lượng rút gọn",
          "description": "Mô hình hai vật chuyển động quanh khối tâm. μ thay khối lượng electron trong các hệ thức tương ứng của Bohr.",
          "formula": "$$\n\\mu=\\frac{mM}{m+M}.\n$$",
          "variables": []
        },
        {
          "name": "Nguyên tử dạng hydrogen",
          "description": "Hệ chỉ có một electron, điện tích hạt nhân $+Ze$. Bỏ sai khác khối lượng rút gọn khi so cùng các hằng số mốc $a_0$ và R.",
          "formula": "$$\n\\begin{aligned}r_n&=n^2a_0/Z\\\\E_n&=-Z^2hcR/n^2.\\end{aligned}\n$$",
          "variables": []
        }
      ]
    },
    {
      "id": "laser",
      "title": "Phát xạ kích thích và laser",
      "items": [
        {
          "name": "Photon kích thích chuyển mức",
          "description": "Nguyên tử đã ở trạng thái cao. Photon tới thuộc mode phù hợp kích thích phát thêm photon có cùng tần số, hướng, pha và phân cực trong mô tả đang dùng.",
          "formula": "$$\nhf=E_u-E_l.\n$$",
          "variables": []
        },
        {
          "name": "Phân bố Boltzmann theo trạng thái",
          "description": "Hai trạng thái riêng biệt ở cân bằng nhiệt, nhiệt độ tuyệt đối T>0. Nếu cộng nhiều trạng thái cùng năng lượng thành một mức, phải tính hệ số suy biến.",
          "formula": "$$\n\\frac{n_u}{n_l}=e^{-(E_u-E_l)/(kT)}.\n$$",
          "variables": []
        },
        {
          "name": "Đảo lộn mật độ cư trú",
          "description": "Số nguyên tử cư trú ở trạng thái trên lớn hơn số nguyên tử ở trạng thái dưới của chuyển mức laser. Đây là tình trạng không cân bằng cần được duy trì bằng bơm năng lượng.",
          "formula": "$$\nn_u>n_l.\n$$",
          "variables": []
        }
      ]
    },
    {
      "id": "thermal",
      "title": "Bức xạ vật đen",
      "items": [
        {
          "name": "Vật đen",
          "description": "Vật hấp thụ toàn bộ bức xạ tới ở mọi bước sóng. Ở cân bằng nhiệt, vật đen là vật phát xạ lý tưởng có độ phát xạ bằng một.",
          "formula": "",
          "variables": []
        },
        {
          "name": "Stefan–Boltzmann",
          "description": "I là công suất phát trên một đơn vị diện tích của vật đen, đơn vị $\\mathrm{W/m^2}$. T đo bằng kelvin.",
          "formula": "$$\n\\begin{aligned}\nI&=\\int_0^\\infty I(\\lambda)\\,d\\lambda\\\\\n&=\\sigma T^4.\n\\end{aligned}\n$$",
          "variables": []
        },
        {
          "name": "Hằng số Stefan–Boltzmann",
          "description": "$k$ là hằng số Boltzmann, $h$ là hằng số Planck và $c$ là tốc độ ánh sáng. Giá trị SI của $\\sigma$ xấp xỉ $5{,}6704\\times10^{-8}$, với đơn vị $\\mathrm{W/(m^2K^4)}$.",
          "formula": "$$\n\\sigma=\\frac{2\\pi^5k^4}{15c^2h^3}.\n$$",
          "variables": []
        },
        {
          "name": "Suất phát xạ phổ theo bước sóng",
          "description": "Công suất phát trên một đơn vị diện tích và một đơn vị khoảng bước sóng. Khi bước sóng đo bằng mét, đơn vị của $I(\\lambda)$ là $\\mathrm{W/m^3}$.",
          "formula": "$$\ndI=I(\\lambda)\\,d\\lambda.\n$$",
          "variables": []
        },
        {
          "name": "Dịch chuyển Wien",
          "description": "$\\lambda_m$ là vị trí cực đại của suất phát xạ tính theo bước sóng, không phải cực đại khi đổi sang biến tần số.",
          "formula": "$$\n\\lambda_mT\\approx2{,}90\\times10^{-3}\\,\\mathrm{m\\,K}.\n$$",
          "variables": []
        },
        {
          "name": "Suất phát xạ phổ Planck",
          "description": "$\\lambda>0$, $T>0$, $x=hc/(\\lambda kT)$. $I(\\lambda)$ có đơn vị $\\mathrm{W/m^3}$ khi λ đo bằng mét.",
          "formula": "$$\nI(\\lambda)=\\frac{2\\pi hc^2}{\\lambda^5(e^x-1)}.\n$$",
          "variables": []
        },
        {
          "name": "Công suất trong một dải",
          "description": "$I_{\\rm band}$ đo bằng $\\mathrm{W/m^2}$. Khoảng đủ hẹp cho phép lấy giá trị ở trung điểm nhân độ rộng khoảng.",
          "formula": "$$\nI_{\\rm band}=\\int_{\\lambda_1}^{\\lambda_2}I(\\lambda)\\,d\\lambda.\n$$",
          "variables": []
        },
        {
          "name": "Lượng tử năng lượng của dao động tử Planck",
          "description": "Trong mô hình phát xạ đang xét, $n$ là số nguyên không âm. Các mức lần lượt là $0$, $hf$, $2hf$ và những bội nguyên tiếp theo.",
          "formula": "$$\nE_n=nhf.\n$$",
          "variables": []
        },
        {
          "name": "Giới hạn Rayleigh–Jeans",
          "description": "Giới hạn bước sóng dài của phân bố Planck, ứng với $hc/(\\lambda kT)\\ll1$.",
          "formula": "$$\nI(\\lambda)\\approx\\frac{2\\pi ckT}{\\lambda^4}.\n$$",
          "variables": []
        }
      ]
    },
    {
      "id": "uncertainty",
      "title": "Bất định của vật chất và vạch phổ",
      "items": [
        {
          "name": "Vị trí và động lượng",
          "description": "Hai độ lệch chuẩn thuộc cùng trạng thái và cùng trục liên hợp. Có các quan hệ tương ứng theo y và z.",
          "formula": "$$\n\\Delta x\\,\\Delta p_x\\ge\\hbar/2.\n$$",
          "variables": []
        },
        {
          "name": "Năng lượng và thời gian sống",
          "description": "Δt là thang thời gian đang xét. Phải xác định quy ước độ rộng ΔE và không đồng nhất nó với sai số đồng hồ.",
          "formula": "$$\n\\Delta t\\,\\Delta E\\ge\\hbar/2.\n$$",
          "variables": []
        },
        {
          "name": "Đổi độ rộng năng lượng sang bước sóng",
          "description": "Độ rộng nhỏ so với giá trị trung tâm, cùng quy ước độ rộng ở hai biến. Dấu của vi phân bỏ khi lấy độ lớn.",
          "formula": "$$\n\\frac{\\Delta\\lambda}{\\lambda}\\approx\\frac{\\Delta E}{E}.\n$$",
          "variables": []
        }
      ]
    }
  ]
}

export const matterWavesSlides=[
  {
    "note": "19-song-vat-chat",
    "title": "Động lượng quyết định bước sóng vật chất",
    "bullets": [
      "Electron, neutron và những hạt khác có thể nhiễu xạ.",
      "Dùng động lượng phù hợp miền tốc độ.",
      "Không thay quan hệ năng lượng của hạt có khối lượng bằng E=pc."
    ],
    "formula": "$$\n\\lambda=h/p.\n$$"
  },
  {
    "note": "19-song-vat-chat",
    "title": "Thí nghiệm nhiễu xạ nối hai mô tả",
    "bullets": [
      "Hiệu điện thế gia tốc xác định động năng electron.",
      "Cực đại nhiễu xạ cho phép xác định bước sóng độc lập.",
      "Sự phù hợp kiểm tra giả thuyết de Broglie."
    ],
    "formula": "$$\n\\lambda=h/\\sqrt{2meV_{ba}}.\n$$"
  },
  {
    "note": "19-song-vat-chat",
    "title": "Hạt nhân tập trung khối lượng và điện tích dương",
    "bullets": [
      "Phần lớn hạt alpha qua lá vàng chỉ lệch ít.",
      "Một số lệch góc lớn đòi hỏi lực đẩy mạnh trong vùng rất nhỏ.",
      "Bài toán trực diện với bia nặng dùng bảo toàn cơ năng."
    ],
    "formula": "$$\nK_0=qQ/(4\\pi\\epsilon_0r_{\\min}).\n$$"
  },
  {
    "note": "19-song-vat-chat",
    "title": "Phổ vạch phản ánh mức năng lượng nguyên tử",
    "bullets": [
      "Phát photon làm nguyên tử chuyển xuống mức thấp.",
      "Hấp thụ photon cần mức cuối phù hợp.",
      "Phổ hấp thụ còn phụ thuộc các mức ban đầu có nguyên tử cư trú."
    ],
    "formula": "$$\nhf=E_i-E_f.\n$$"
  },
  {
    "note": "19-song-vat-chat",
    "title": "Quỹ đạo Bohr là một mô hình lượng tử hóa bán cổ điển",
    "bullets": [
      "Chỉ một số mômen động lượng và bán kính được phép trong mô hình.",
      "Điều kiện vòng sóng cho cách diễn giải lượng tử hóa.",
      "Nguyên lý bất định đặt giới hạn cho mô tả quỹ đạo xác định."
    ],
    "formula": "$$\n\\begin{aligned}L_n&=n\\hbar\\\\2\\pi r_n&=n\\lambda_n.\\end{aligned}\n$$"
  },
  {
    "note": "19-song-vat-chat",
    "title": "Năng lượng liên kết âm với mốc ion hóa bằng không",
    "bullets": [
      "Động năng dương, thế năng âm và cơ năng âm.",
      "Ion hóa cần cung cấp ít nhất độ lớn cơ năng ban đầu.",
      "Photon chuyển mức mang chênh lệch cơ năng."
    ],
    "formula": "$$\nE_n=-hcR/n^2.\n$$"
  },
  {
    "note": "19-song-vat-chat",
    "title": "Hạt nhân chuyển động tạo hiệu chỉnh phổ",
    "bullets": [
      "Electron và hạt nhân cùng chuyển động quanh khối tâm.",
      "Khối lượng rút gọn hiệu chỉnh các dự đoán của mô hình.",
      "Đồng vị khác khối lượng hạt nhân có các vạch hơi lệch nhau."
    ],
    "formula": "$$\n\\mu=mM/(m+M).\n$$"
  },
  {
    "note": "19-song-vat-chat",
    "title": "Laser cần phát xạ kích thích và đảo lộn mật độ",
    "bullets": [
      "Photon tới kích thích nguyên tử đã được kích thích.",
      "Bơm giữ hệ ngoài cân bằng nhiệt.",
      "Laser bốn mức đảo lộn giữa hai mức của chuyển mức laser, không đòi mức trên đông hơn mức cơ bản."
    ],
    "formula": "$$\nn_u>n_l.\n$$"
  },
  {
    "note": "19-song-vat-chat",
    "title": "Phổ vật đen cần hai đại lượng khác nhau",
    "bullets": [
      "Cường độ toàn phần là công suất trên diện tích.",
      "Suất phát xạ phổ còn tính trên mỗi khoảng bước sóng.",
      "Lấy tích phân phổ mới thu được cường độ toàn phần."
    ],
    "formula": "$$\nI=\\int_0^\\infty I(\\lambda)\\,d\\lambda.\n$$"
  },
  {
    "note": "19-song-vat-chat",
    "title": "Nhiệt độ tăng làm đỉnh phổ cao hơn và dịch về bước sóng ngắn",
    "bullets": [
      "Tổng công suất trên diện tích tăng theo lũy thừa bốn.",
      "Vị trí đỉnh theo bước sóng tuân theo Wien.",
      "Màu tổng hợp không chỉ là màu của bước sóng đỉnh."
    ],
    "formula": "$$\n\\begin{aligned}I&=\\sigma T^4\\\\\\lambda_mT&\\approx2{,}90\\times10^{-3}\\,\\mathrm{m\\,K}.\\end{aligned}\n$$"
  },
  {
    "note": "19-song-vat-chat",
    "title": "Lượng tử hóa khắc phục tai biến tử ngoại",
    "bullets": [
      "Rayleigh dùng năng lượng trung bình kT cho mọi mode.",
      "Khoảng năng lượng hf lớn làm trạng thái kích thích khó được cư trú.",
      "Định luật Planck trở về giới hạn cổ điển ở bước sóng dài."
    ],
    "formula": "$$\nN_1/N_0=e^{-hf/(kT)}.\n$$"
  },
  {
    "note": "19-song-vat-chat",
    "title": "Vật chất có cùng các giới hạn bất định với photon",
    "bullets": [
      "Từng electron riêng lẻ vẫn tích lũy thành vân giao thoa.",
      "Giam hạt trong vùng nhỏ hơn làm cận động lượng tăng.",
      "Thời gian sống ngắn đi cùng thang độ rộng năng lượng lớn hơn."
    ],
    "formula": "$$\n\\begin{aligned}\\Delta x\\,\\Delta p_x&\\ge\\hbar/2\\\\\\Delta t\\,\\Delta E&\\ge\\hbar/2.\\end{aligned}\n$$"
  }
]

export const matterWavesTopics=[
  {
    "title": "Tính sóng và cấu trúc nguyên tử",
    "topics": [
      {
        "slug": "song-electron",
        "title": "Sóng electron và kính hiển vi electron",
        "question": "Làm thế nào đo được bước sóng của một hạt?",
        "source": "39.1"
      },
      {
        "slug": "nguyen-tu-hat-nhan-pho",
        "title": "Hạt nhân nguyên tử và quang phổ",
        "question": "Tán xạ và phổ ánh sáng cho biết gì về nguyên tử?",
        "source": "39.2"
      }
    ]
  },
  {
    "title": "Mức năng lượng và laser",
    "topics": [
      {
        "slug": "muc-nang-luong-bohr",
        "title": "Mức năng lượng và mô hình Bohr",
        "question": "Vì sao chỉ có một số bước sóng được phát hoặc hấp thụ?",
        "source": "39.3"
      },
      {
        "slug": "laser",
        "title": "Laser và phát xạ kích thích",
        "question": "Làm thế nào tạo một chùm sáng kết hợp bằng nhiều nguyên tử?",
        "source": "39.4"
      }
    ]
  },
  {
    "title": "Phổ nhiệt và bất định",
    "topics": [
      {
        "slug": "pho-lien-tuc",
        "title": "Phổ liên tục và bức xạ vật đen",
        "question": "Vì sao vật nóng phát một dải bước sóng và đổi màu khi nhiệt độ tăng?",
        "source": "39.5"
      },
      {
        "slug": "bat-dinh-vat-chat",
        "title": "Nguyên lý bất định đối với vật chất",
        "question": "Tính sóng thay đổi mô tả electron trong nguyên tử như thế nào?",
        "source": "39.6"
      }
    ]
  }
]
