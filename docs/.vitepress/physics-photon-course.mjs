export const photonCheatsheet={
  "title": "Cheatsheet: Photon",
  "description": "Định nghĩa, tính chất, điều kiện và công thức về photon, quang điện, tia X, Compton và bất định.",
  "sections": [
    {
      "id": "photon",
      "title": "Năng lượng, động lượng và đơn vị",
      "items": [
        {
          "name": "Photon trong chân không",
          "description": "Lượng tử bức xạ điện từ có khối lượng nghỉ bằng không. Động lượng hướng theo chiều truyền.",
          "formula": "$$\n\\begin{aligned}E&=hf=hc/\\lambda\\\\p&=E/c=h/\\lambda.\\end{aligned}\n$$",
          "variables": [
            "$E$: Năng lượng (J).",
            "$p$: Động lượng (kg·m/s).",
            "$f$: Tần số (Hz).",
            "$\\lambda$: Bước sóng trong chân không (m)."
          ]
        },
        {
          "name": "Hằng số Planck",
          "description": "Giá trị SI chính xác và hằng số rút gọn.",
          "formula": "$$\n\\begin{aligned}h&=6{,}62607015\\times10^{-34}\\,\\mathrm{J\\,s}\\\\\\hbar&=h/(2\\pi).\\end{aligned}\n$$",
          "variables": []
        },
        {
          "name": "Electronvolt",
          "description": "Đơn vị năng lượng của electron qua độ tăng điện thế một vôn.",
          "formula": "$$\n1\\,\\mathrm{eV}\\approx1{,}602\\times10^{-19}\\,\\mathrm J.\n$$",
          "variables": []
        },
        {
          "name": "Suất phát photon và mật độ thông lượng photon",
          "description": "Nguồn đơn sắc có công suất quang học P, hoặc chùm có cường độ I. Suất phát đếm số photon mỗi giây. F là số photon qua một đơn vị diện tích mỗi giây.",
          "formula": "$$\n\\begin{aligned}\\dot N&=P/(hf)\\\\F&=I/(hf).\\end{aligned}\n$$",
          "variables": [
            "$\\dot N$: Số photon phát ra mỗi giây (s⁻¹).",
            "$F$: Số photon qua một đơn vị diện tích mỗi giây (m⁻²·s⁻¹).",
            "$P$: Công suất quang học (W).",
            "$I$: Cường độ chùm sáng (W/m²).",
            "$h$: Hằng số Planck (J·s).",
            "$f$: Tần số ánh sáng (Hz)."
          ]
        }
      ]
    },
    {
      "id": "photoelectric",
      "title": "Quang điện và ngưỡng",
      "items": [
        {
          "name": "Công thoát và phương trình Einstein",
          "description": "φ là năng lượng tối thiểu đưa electron khỏi bề mặt. Phương trình áp dụng cho quang điện một photon với hf không nhỏ hơn φ.",
          "formula": "$$\nK_{\\max}=hf-\\phi.\n$$",
          "variables": []
        },
        {
          "name": "Thế hãm",
          "description": "V₀ là độ lớn điện áp ngược. Anôt có điện thế V_AC=−V₀ so với catôt tại ngưỡng tắt dòng. Bỏ qua ảnh hưởng tiếp xúc giữa vật liệu điện cực.",
          "formula": "$$\n\\begin{aligned}K_{\\max}&=eV_0\\\\V_0&=(h/e)f-\\phi/e.\\end{aligned}\n$$",
          "variables": []
        },
        {
          "name": "Tần số và bước sóng ngưỡng",
          "description": "Có thể phát electron với động năng không âm khi f≥f₀, tương đương λ≤λ₀. Công thoát phụ thuộc bề mặt.",
          "formula": "$$\n\\begin{aligned}f_0&=\\phi/h\\\\\\lambda_0&=hc/\\phi.\\end{aligned}\n$$",
          "variables": []
        },
        {
          "name": "Dòng quang điện bão hòa",
          "description": "η là số electron thu được trên một photon tới trong mô hình tuyến tính. Ở cùng tần số và η, dòng tỷ lệ công suất.",
          "formula": "$$\ni_{\\rm sat}=e\\eta\\dot N.\n$$",
          "variables": []
        }
      ]
    },
    {
      "id": "xray",
      "title": "Phát tia X",
      "items": [
        {
          "name": "Bức xạ hãm",
          "description": "Electron ban đầu có động năng không đáng kể, được gia tốc qua độ tăng điện thế V_AC. Một photon nhận toàn bộ động năng thì đạt năng lượng cực đại.",
          "formula": "$$\n\\begin{aligned}E_{\\max}&=eV_{AC}\\\\f_{\\max}&=eV_{AC}/h\\\\\\lambda_{\\min}&=hc/(eV_{AC}).\\end{aligned}\n$$",
          "variables": []
        },
        {
          "name": "Phổ liên tục và vạch đặc trưng",
          "description": "Bức xạ hãm cho phổ liên tục với bước sóng không nhỏ hơn λ_min. Các chuyển mức nguyên tử của bia tạo các vạch đặc trưng chồng lên phổ liên tục.",
          "formula": "$$\nE_\\gamma=E_i-E_f.\n$$",
          "variables": []
        }
      ]
    },
    {
      "id": "compton",
      "title": "Tán xạ Compton",
      "items": [
        {
          "name": "Độ dịch bước sóng",
          "description": "Electron tự do ban đầu đứng yên, khối lượng nghỉ m. φ là góc photon tán xạ so với photon tới, không phải công thoát.",
          "formula": "$$\n\\begin{aligned}\\lambda_C&=h/(mc)\\\\\\lambda'-\\lambda&=\\lambda_C(1-\\cos\\varphi).\\end{aligned}\n$$",
          "variables": []
        },
        {
          "name": "Miền độ dịch",
          "description": "Photon đi thẳng không dịch bước sóng. Photon tán xạ ngược đạt độ dịch lớn nhất.",
          "formula": "$$\n0\\le\\lambda'-\\lambda\\le2\\lambda_C.\n$$",
          "variables": []
        },
        {
          "name": "Năng lượng và động lượng electron",
          "description": "Hệ cô lập bảo toàn cả năng lượng lẫn động lượng. Electron ban đầu đứng yên.",
          "formula": "$$\n\\begin{aligned}K_e&=hc/\\lambda-hc/\\lambda'\\\\\\vec p_e&=\\vec p-\\vec p'.\\end{aligned}\n$$",
          "variables": []
        }
      ]
    },
    {
      "id": "pairs",
      "title": "Tạo cặp và hủy cặp",
      "items": [
        {
          "name": "Tạo electron–positron",
          "description": "Một photon phải tương tác với hạt nhân hoặc vật khác nhận giật lùi. Hai hạt mới mỗi hạt có khối lượng nghỉ m. Bia hữu hạn cần thêm năng lượng giật lùi.",
          "formula": "$$\nE_\\gamma\\ge2mc^2.\n$$",
          "variables": []
        },
        {
          "name": "Hủy cặp hai photon",
          "description": "Trong hệ khối tâm, electron và positron có tổng động lượng bằng không. Hai photon cuối có cùng năng lượng và ngược hướng.",
          "formula": "$$\n\\begin{aligned}E_{\\gamma1}&=E_{\\gamma2}=\\gamma mc^2\\\\\\vec p_{\\gamma1}+\\vec p_{\\gamma2}&=\\vec0.\\end{aligned}\n$$",
          "variables": []
        }
      ]
    },
    {
      "id": "probability",
      "title": "Tính sóng và xác suất",
      "items": [
        {
          "name": "Phân bố phát hiện photon",
          "description": "Cường độ tỷ lệ số photon trung bình trên một đơn vị diện tích trong một đơn vị thời gian, với ánh sáng đơn sắc.",
          "formula": "$$\nI=Fhf.\n$$",
          "variables": []
        },
        {
          "name": "Cực tiểu nhiễu xạ một khe",
          "description": "Miền Fraunhofer, khe rộng a. Các bậc tối là m=±1,±2,…, ứng với xác suất phát hiện bằng không trong mô hình lý tưởng.",
          "formula": "$$\na\\sin\\theta=m\\lambda.\n$$",
          "variables": []
        },
        {
          "name": "Số sóng và tần số góc",
          "description": "Sóng phẳng truyền theo +x. Điện trường phân cực theo y có biên độ A.",
          "formula": "$$\n\\begin{aligned}k&=2\\pi/\\lambda\\\\\\omega&=2\\pi f\\\\p_x&=\\hbar k\\\\E&=\\hbar\\omega.\\end{aligned}\n$$",
          "variables": []
        }
      ]
    },
    {
      "id": "uncertainty",
      "title": "Nguyên lý bất định",
      "items": [
        {
          "name": "Vị trí và động lượng liên hợp",
          "description": "Δx, Δpₓ là độ bất định của cùng trạng thái theo cùng một trục. Có các quan hệ tương ứng cho y và z.",
          "formula": "$$\n\\Delta x\\,\\Delta p_x\\ge\\hbar/2.\n$$",
          "variables": []
        },
        {
          "name": "Năng lượng và thời gian",
          "description": "Δt là khoảng tồn tại hoặc thang thời gian đặc trưng đang xét. Cần thống nhất ý nghĩa và quy ước độ rộng năng lượng ΔE.",
          "formula": "$$\n\\Delta t\\,\\Delta E\\ge\\hbar/2.\n$$",
          "variables": []
        },
        {
          "name": "Xung photon và độ rộng phổ",
          "description": "Với cùng quy ước độ rộng và E=hf, xung ngắn đi cùng độ rộng tần số lớn. Không đồng nhất thời gian xung với chu kỳ.",
          "formula": "$$\n\\begin{aligned}\\Delta E&=h\\Delta f\\\\\\Delta f\\,\\Delta t&\\ge1/(4\\pi).\\end{aligned}\n$$",
          "variables": []
        }
      ]
    }
  ]
}

export const photonSlides=[
  {
    "note": "18-photon",
    "title": "Tần số quyết định năng lượng từng photon",
    "bullets": [
      "Photon có năng lượng và động lượng dù khối lượng nghỉ bằng không.",
      "Cường độ cùng tần số tăng nghĩa là số photon tăng.",
      "Sóng vô tuyến và tia gamma đều tuân theo hệ thức photon."
    ],
    "formula": "$$\n\\begin{aligned}E&=hf\\\\p&=h/\\lambda.\\end{aligned}\n$$"
  },
  {
    "note": "18-photon",
    "title": "Thế hãm đo động năng cực đại",
    "bullets": [
      "Điện áp ngược làm cản electron quang điện.",
      "Tại ngưỡng tắt dòng, ngay cả electron nhanh nhất cũng không đến được anôt.",
      "V₀ là độ lớn dương của thế hãm."
    ],
    "formula": "$$\nK_{\\max}=eV_0.\n$$"
  },
  {
    "note": "18-photon",
    "title": "Ngưỡng quang điện phụ thuộc vật liệu",
    "bullets": [
      "Một photon truyền trọn năng lượng cho một electron trong mô hình đang xét.",
      "Công thoát lớn hơn làm động năng cực đại nhỏ hơn ở cùng tần số.",
      "Tăng cường độ dưới ngưỡng không thay thế năng lượng còn thiếu của từng photon."
    ],
    "formula": "$$\n\\begin{aligned}K_{\\max}&=hf-\\phi\\\\f_0&=\\phi/h.\\end{aligned}\n$$"
  },
  {
    "note": "18-photon",
    "title": "Đường thẳng thế hãm cho công thoát và hằng số Planck",
    "bullets": [
      "Đổi bước sóng sang tần số trước khi dựng đồ thị.",
      "Độ dốc bằng h/e và tung độ gốc bằng −φ/e.",
      "Công thoát nhạy với tạp chất bề mặt."
    ],
    "formula": "$$\nV_0=(h/e)f-\\phi/e.\n$$"
  },
  {
    "note": "18-photon",
    "title": "Bước sóng ngắn nhất của tia X do điện áp quyết định",
    "bullets": [
      "Electron được gia tốc rồi phát bức xạ hãm khi gặp bia.",
      "Photon mạnh nhất nhận toàn bộ động năng của một electron.",
      "Tăng tốc độ electron tới ở cùng điện áp làm tăng cường độ mà không đổi bước sóng cắt."
    ],
    "formula": "$$\n\\lambda_{\\min}=hc/(eV_{AC}).\n$$"
  },
  {
    "note": "18-photon",
    "title": "Compton cần bảo toàn cả năng lượng lẫn động lượng",
    "bullets": [
      "Công thức chuẩn xét electron tự do ban đầu đứng yên.",
      "Photon cuối có thể đổi hướng và truyền năng lượng cho electron.",
      "Phổ có thành phần dịch và không dịch liên quan mức liên kết của electron."
    ],
    "formula": "$$\n\\lambda'-\\lambda=\\frac h{mc}(1-\\cos\\varphi).\n$$"
  },
  {
    "note": "18-photon",
    "title": "Tạo cặp một photon cần một vật nhận giật lùi",
    "bullets": [
      "Tổng năng lượng nghỉ của cặp bằng 2mc².",
      "Một photon tự do trong chân không không thể tự tạo cặp này.",
      "Bảo toàn động lượng làm ngưỡng thực với bia hữu hạn cao hơn mốc năng lượng nghỉ."
    ],
    "formula": "$$\nE_\\gamma\\ge2mc^2.\n$$"
  },
  {
    "note": "18-photon",
    "title": "Hủy cặp hai photon đối xứng trong hệ khối tâm",
    "bullets": [
      "Electron và positron có động lượng ban đầu đối nhau.",
      "Hai photon cuối cùng năng lượng và bay ngược chiều.",
      "Năng lượng mỗi photon gồm cả phần năng lượng nghỉ và động năng của một hạt ban đầu."
    ],
    "formula": "$$\nE_\\gamma=\\gamma mc^2.\n$$"
  },
  {
    "note": "18-photon",
    "title": "Các photon riêng lẻ vẫn tạo phân bố nhiễu xạ",
    "bullets": [
      "Mỗi photon tạo một sự kiện phát hiện riêng lẻ.",
      "Sau nhiều sự kiện, cường độ cho phân bố xác suất.",
      "Vân tối lý tưởng có xác suất phát hiện bằng không."
    ],
    "formula": "$$\na\\sin\\theta=m\\lambda.\n$$"
  },
  {
    "note": "18-photon",
    "title": "Giới hạn bất định không phải lỗi dụng cụ",
    "bullets": [
      "Định xứ photon qua khe làm phân bố động lượng ngang rộng ra.",
      "Quan hệ xét vị trí và động lượng liên hợp của cùng trạng thái.",
      "Tăng độ tinh vi của thiết bị không loại bỏ giới hạn này."
    ],
    "formula": "$$\n\\Delta x\\,\\Delta p_x\\ge\\hbar/2.\n$$"
  },
  {
    "note": "18-photon",
    "title": "Sóng có động lượng xác định trải rộng trong không gian",
    "bullets": [
      "Sóng sin đơn sắc kéo dài có số sóng xác định.",
      "Chồng các thành phần khác nhau tạo miền biên độ tập trung hơn.",
      "Phân bố động lượng rộng hơn đi cùng định xứ tốt hơn."
    ],
    "formula": "$$\np_x=\\hbar k.\n$$"
  },
  {
    "note": "18-photon",
    "title": "Xung ánh sáng ngắn đòi hỏi phổ rộng",
    "bullets": [
      "Năng lượng và tần số của photon liên hệ qua h.",
      "Thời gian xung ngắn không đồng nghĩa chu kỳ sóng ngắn.",
      "Ý nghĩa của độ rộng năng lượng và thời gian phải được xác định khi dùng bất định."
    ],
    "formula": "$$\n\\Delta t\\,\\Delta E\\ge\\hbar/2.\n$$"
  }
]

export const photonTopics=[
  {
    "title": "Hấp thụ và phát photon",
    "topics": [
      {
        "slug": "quang-dien",
        "title": "Hiệu ứng quang điện và photon",
        "question": "Vì sao tăng cường độ không thay được tần số ngưỡng?",
        "source": "38.1"
      },
      {
        "slug": "phat-tia-x",
        "title": "Phát tia X và bức xạ hãm",
        "question": "Điện áp gia tốc giới hạn bước sóng tia X như thế nào?",
        "source": "38.2"
      }
    ]
  },
  {
    "title": "Tán xạ, xác suất và bất định",
    "topics": [
      {
        "slug": "compton-tao-cap",
        "title": "Compton, tạo cặp và hủy cặp",
        "question": "Photon chuyển năng lượng và động lượng cho vật chất bằng cách nào?",
        "source": "38.3"
      },
      {
        "slug": "luong-tinh-bat-dinh",
        "title": "Lưỡng tính sóng–hạt và nguyên lý bất định",
        "question": "Vì sao các sự kiện photon riêng lẻ tạo nên phân bố nhiễu xạ?",
        "source": "38.4"
      }
    ]
  }
]
