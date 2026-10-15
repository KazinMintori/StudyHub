export const relativityCheatsheet={
  "title": "Cheatsheet: Thuyết tương đối",
  "description": "Định nghĩa, tính chất, điều kiện và công thức của thuyết tương đối.",
  "sections": [
    {
      "id": "postulates",
      "title": "Tiên đề và hệ số Lorentz",
      "items": [
        {
          "name": "Hai tiên đề",
          "description": "Định luật vật lý cùng dạng trong mọi hệ quán tính. Tốc độ ánh sáng trong chân không bất biến và độc lập vận tốc nguồn.",
          "formula": "$$\nc=299\\,792\\,458\\,\\mathrm{m/s}.\n$$",
          "variables": []
        },
        {
          "name": "Hệ số Lorentz",
          "description": "Miền vận tốc tương đối nhỏ hơn c. Hệ số không nhỏ hơn một.",
          "formula": "$$\n\\begin{aligned}\\beta&=u/c\\\\\\gamma&=1/\\sqrt{1-\\beta^2}\\\\0&\\le\\beta<1.\\end{aligned}\n$$",
          "variables": []
        }
      ]
    },
    {
      "id": "measurements",
      "title": "Thời gian và chiều dài",
      "items": [
        {
          "name": "Thời gian riêng",
          "description": "Hai sự kiện cùng một vị trí trong hệ đo thời gian riêng. Khoảng thời gian trong hệ khác chuyển động tương đối dài hơn.",
          "formula": "$$\n\\Delta t=\\gamma\\Delta t_0.\n$$",
          "variables": [
            "$\\Delta t,\\Delta t_0$: Khoảng thời gian (s)."
          ]
        },
        {
          "name": "Độ dài riêng và co dọc",
          "description": "Độ dài riêng thuộc hệ nghỉ vật. Các đầu phải được đo đồng thời trong hệ đang xét. Kích thước vuông góc vận tốc không đổi.",
          "formula": "$$\nl=l_0/\\gamma.\n$$",
          "variables": [
            "$l,l_0$: Chiều dài dọc chuyển động (m)."
          ]
        }
      ]
    },
    {
      "id": "coordinates",
      "title": "Tọa độ Lorentz và khoảng sự kiện",
      "items": [
        {
          "name": "Biến đổi thuận",
          "description": "S′ chuyển động theo +x với vận tốc u. Các trục song song và hai gốc trùng tại t=t′=0.",
          "formula": "$$\n\\begin{aligned}x'&=\\gamma(x-ut)\\\\y'&=y\\\\z'&=z\\\\t'&=\\gamma(t-ux/c^2).\\end{aligned}\n$$",
          "variables": []
        },
        {
          "name": "Biến đổi ngược",
          "description": "Cùng quy ước hai hệ như phép thuận.",
          "formula": "$$\n\\begin{aligned}x&=\\gamma(x'+ut')\\\\t&=\\gamma(t'+ux'/c^2).\\end{aligned}\n$$",
          "variables": []
        },
        {
          "name": "Hiệu tọa độ sự kiện",
          "description": "Hiệu thời gian và vị trí thuộc cùng cặp sự kiện. Khoảng không thời gian một chiều là bất biến.",
          "formula": "$$\n\\begin{aligned}\\Delta t'&=\\gamma(\\Delta t-u\\Delta x/c^2)\\\\J&=c^2\\Delta t^2-\\Delta x^2\\\\J&=c^2\\Delta t'^2-\\Delta x'^2.\\end{aligned}\n$$",
          "variables": []
        }
      ]
    },
    {
      "id": "velocities",
      "title": "Vận tốc và Doppler",
      "items": [
        {
          "name": "Vận tốc một chiều",
          "description": "u là vận tốc hệ S′ đối với S. v và v′ là vận tốc cùng vật trong hai hệ.",
          "formula": "$$\n\\begin{aligned}v'&=\\frac{v-u}{1-uv/c^2}\\\\v&=\\frac{v'+u}{1+uv'/c^2}.\\end{aligned}\n$$",
          "variables": []
        },
        {
          "name": "Doppler dọc khi tiến lại gần",
          "description": "f₀ là tần số trong hệ nghỉ nguồn, u là độ lớn tốc độ tương đối.",
          "formula": "$$\nf=f_0\\sqrt{\\frac{c+u}{c-u}}.\n$$",
          "variables": [
            "$f,f_0$: Tần số (Hz)."
          ]
        },
        {
          "name": "Doppler dọc khi rời xa",
          "description": "u dương, nhỏ hơn c. Tần số thu thấp hơn tần số riêng.",
          "formula": "$$\nf=f_0\\sqrt{\\frac{c-u}{c+u}}.\n$$",
          "variables": []
        },
        {
          "name": "Giới hạn dịch tần nhỏ",
          "description": "Tiến lại gần, với u/c nhỏ hơn nhiều so với một. Độ dịch là Δf=f−f₀.",
          "formula": "$$\n\\Delta f/f_0\\approx u/c.\n$$",
          "variables": []
        },
        {
          "name": "Doppler ngang",
          "description": "Phương truyền của photon vuông góc vận tốc nguồn tại sự kiện phát, xét trong hệ người thu.",
          "formula": "$$\nf=f_0/\\gamma.\n$$",
          "variables": []
        }
      ]
    },
    {
      "id": "dynamics",
      "title": "Động lượng và lực",
      "items": [
        {
          "name": "Động lượng",
          "description": "m là khối lượng nghỉ. Hệ số Lorentz ở đây tính theo tốc độ v của hạt trong hệ xét.",
          "formula": "$$\n\\vec p=\\gamma m\\vec v.\n$$",
          "variables": [
            "$p$: Động lượng (kg m/s).",
            "$m$: Khối lượng nghỉ (kg)."
          ]
        },
        {
          "name": "Lực và gia tốc",
          "description": "Phân tích dọc và vuông góc vận tốc tại thời điểm xét.",
          "formula": "$$\n\\begin{aligned}\\vec F&=d\\vec p/dt\\\\F_\\parallel&=\\gamma^3ma_\\parallel\\\\F_\\perp&=\\gamma ma_\\perp.\\end{aligned}\n$$",
          "variables": []
        },
        {
          "name": "Chuyển động tròn đều",
          "description": "R là bán kính quỹ đạo. Lực hướng tâm vuông góc vận tốc và không sinh công.",
          "formula": "$$\nF=\\gamma mv^2/R.\n$$",
          "variables": []
        }
      ]
    },
    {
      "id": "energy",
      "title": "Công và năng lượng",
      "items": [
        {
          "name": "Năng lượng nghỉ, động năng và toàn phần",
          "description": "m bất biến, gamma tính theo tốc độ hạt. Năng lượng toàn phần gồm động năng và năng lượng nghỉ.",
          "formula": "$$\n\\begin{aligned}E_0&=mc^2\\\\K&=(\\gamma-1)mc^2\\\\E&=K+E_0=\\gamma mc^2.\\end{aligned}\n$$",
          "variables": [
            "$E_0,K,E$: Năng lượng (J)."
          ]
        },
        {
          "name": "Hệ thức năng lượng–động lượng",
          "description": "p là độ lớn động lượng. Hạt không khối lượng có năng lượng dương thỏa E=pc.",
          "formula": "$$\nE^2=(mc^2)^2+(pc)^2.\n$$",
          "variables": []
        },
        {
          "name": "Công và gia tốc điện",
          "description": "Công hợp lực bằng biến thiên động năng. Công lực điện của điện tích q liên hệ với độ tăng điện thế ΔV.",
          "formula": "$$\n\\begin{aligned}W&=\\Delta K\\\\\\Delta K&=-q\\Delta V.\\end{aligned}\n$$",
          "variables": []
        },
        {
          "name": "Giới hạn Newton",
          "description": "Tốc độ hạt nhỏ so với c.",
          "formula": "$$\n\\begin{aligned}p&\\approx mv\\\\K&\\approx mv^2/2.\\end{aligned}\n$$",
          "variables": []
        }
      ]
    },
    {
      "id": "general",
      "title": "Nguyên lý tương ứng và tương đương",
      "items": [
        {
          "name": "Nguyên lý tương ứng",
          "description": "Lý thuyết mở rộng tái tạo dự đoán cũ trong miền mà dự đoán ấy đã được xác nhận.",
          "formula": "",
          "variables": []
        },
        {
          "name": "Nguyên lý tương đương",
          "description": "Các phép thử cục bộ thích hợp trong trọng trường đều và hệ gia tốc tương ứng cho kết quả tương đương. Tính cục bộ loại trừ việc đồng nhất trường thủy triều trên miền lớn với gia tốc đều.",
          "formula": "",
          "variables": []
        }
      ]
    }
  ]
}

export const relativitySlides=[
  {
    "note": "17-thuyet-tuong-doi",
    "title": "Hai tiên đề đặt giới hạn cho mô tả chuyển động",
    "bullets": [
      "Các định luật vật lý có cùng dạng trong mọi hệ quán tính.",
      "Ánh sáng trong chân không có cùng tốc độ trong các hệ ấy.",
      "Vận tốc nguồn không được cộng theo Galileo vào tốc độ ánh sáng."
    ],
    "formula": "$$\nc=299\\,792\\,458\\,\\mathrm{m/s}.\n$$"
  },
  {
    "note": "17-thuyet-tuong-doi",
    "title": "Đồng thời phụ thuộc hệ ở những vị trí khác nhau",
    "bullets": [
      "Hai hệ phải gán tọa độ cho cùng những sự kiện.",
      "Đồng hồ được đồng bộ riêng trong từng hệ quán tính.",
      "Hai sự kiện trùng cả vị trí và thời điểm vẫn trùng nhau trong mọi hệ."
    ],
    "formula": "$$\n\\begin{aligned}\\Delta t&=0\\\\\\Delta t'&=-\\gamma u\\Delta x/c^2.\\end{aligned}\n$$"
  },
  {
    "note": "17-thuyet-tuong-doi",
    "title": "Thời gian riêng gắn với hai sự kiện cùng vị trí",
    "bullets": [
      "Đồng hồ có mặt ở cả hai sự kiện đo thời gian riêng.",
      "Trong hệ mà đồng hồ chuyển động, khoảng thời gian giữa cùng hai sự kiện dài hơn.",
      "Thời gian sự kiện đã phân biệt với thời gian ánh sáng đến mắt."
    ],
    "formula": "$$\n\\begin{aligned}\\gamma&=1/\\sqrt{1-u^2/c^2}\\\\\\Delta t&=\\gamma\\Delta t_0.\\end{aligned}\n$$"
  },
  {
    "note": "17-thuyet-tuong-doi",
    "title": "Chiều dài cần đo hai đầu đồng thời trong hệ đang xét",
    "bullets": [
      "Độ dài riêng thuộc hệ nghỉ của vật.",
      "Chỉ kích thước dọc vận tốc tương đối bị co.",
      "Ảnh nhìn thấy còn phụ thuộc thời gian truyền ánh sáng."
    ],
    "formula": "$$\nl=l_0/\\gamma.\n$$"
  },
  {
    "note": "17-thuyet-tuong-doi",
    "title": "Lorentz trộn tọa độ không gian với thời gian",
    "bullets": [
      "Hệ có dấu phẩy chuyển động theo chiều dương với tốc độ u.",
      "Hai gốc trùng nhau tại thời điểm cả hai đồng hồ bằng không.",
      "Đổi hệ ngược bằng cách đổi dấu u và hoán đổi dấu phẩy."
    ],
    "formula": "$$\n\\begin{aligned}x'&=\\gamma(x-ut)\\\\t'&=\\gamma(t-ux/c^2).\\end{aligned}\n$$"
  },
  {
    "note": "17-thuyet-tuong-doi",
    "title": "Phép cộng vận tốc giữ ánh sáng ở tốc độ c",
    "bullets": [
      "Phân biệt vận tốc vật với vận tốc tương đối của hai hệ.",
      "Chuyển động một chiều dùng cùng quy ước trục ở cả hai hệ.",
      "Vật dưới tốc độ ánh sáng trong một hệ vẫn dưới giới hạn ấy trong hệ kia."
    ],
    "formula": "$$\nv'_x=\\frac{v_x-u}{1-uv_x/c^2}.\n$$"
  },
  {
    "note": "17-thuyet-tuong-doi",
    "title": "Doppler đổi tần số và bước sóng đồng thời",
    "bullets": [
      "Nguồn tiến lại gần cho tần số cao hơn trong cấu hình dọc đường nhìn.",
      "Rời xa dùng dấu tốc độ ngược trong hệ số Doppler.",
      "Công thức Doppler âm không thay thế công thức ánh sáng trong chân không."
    ],
    "formula": "$$\nf=f_0\\sqrt{\\frac{c+u}{c-u}}.\n$$"
  },
  {
    "note": "17-thuyet-tuong-doi",
    "title": "Động lượng có thêm hệ số Lorentz của hạt",
    "bullets": [
      "Khối lượng trong công thức là khối lượng nghỉ.",
      "Động lượng cùng hướng vận tốc và trở về gần đúng Newton ở tốc độ nhỏ.",
      "Ở gần c, động lượng tăng mạnh trong khi tốc độ chỉ tăng ít."
    ],
    "formula": "$$\n\\vec p=\\gamma m\\vec v.\n$$"
  },
  {
    "note": "17-thuyet-tuong-doi",
    "title": "Gia tốc không luôn cùng hướng hợp lực",
    "bullets": [
      "Lực dọc vận tốc làm đổi cả hệ số Lorentz và tốc độ.",
      "Lực ngang vận tốc đổi hướng động lượng với hệ số khác.",
      "Trong chuyển động tròn đều, lực hướng tâm không sinh công."
    ],
    "formula": "$$\n\\begin{aligned}F_\\parallel&=\\gamma^3ma_\\parallel\\\\F_\\perp&=\\gamma ma_\\perp.\\end{aligned}\n$$"
  },
  {
    "note": "17-thuyet-tuong-doi",
    "title": "Động năng là phần năng lượng ngoài năng lượng nghỉ",
    "bullets": [
      "Không đồng nhất động năng với năng lượng toàn phần.",
      "Năng lượng nghỉ vẫn có khi hạt đứng yên.",
      "Giới hạn tốc độ nhỏ cho động năng Newton."
    ],
    "formula": "$$\n\\begin{aligned}K&=(\\gamma-1)mc^2\\\\E&=K+mc^2.\\end{aligned}\n$$"
  },
  {
    "note": "17-thuyet-tuong-doi",
    "title": "Tạo hạt phải bảo toàn cả năng lượng và động lượng",
    "bullets": [
      "Tổng khối lượng nghỉ riêng lẻ có thể thay đổi trong phản ứng.",
      "Năng lượng toàn phần của hệ cô lập vẫn bảo toàn.",
      "Hai chùm đối đầu giảm năng lượng dành cho chuyển động khối tâm."
    ],
    "formula": "$$\nE^2=(mc^2)^2+(pc)^2.\n$$"
  },
  {
    "note": "17-thuyet-tuong-doi",
    "title": "Hấp dẫn đòi hỏi mở rộng mô tả hệ quy chiếu",
    "bullets": [
      "Cơ học Newton là giới hạn tương ứng ở tốc độ nhỏ.",
      "Nguyên lý tương đương so các phép thử cục bộ trong trọng trường và hệ gia tốc.",
      "Định vị vệ tinh cần hiệu chỉnh cả chuyển động lẫn hấp dẫn."
    ],
    "formula": "$$\nE_0=mc^2.\n$$"
  }
]

export const relativityTopics=[
  {
    "title": "Không gian, thời gian và phép đo",
    "topics": [
      {
        "slug": "bat-bien-dinh-luat",
        "title": "Tính bất biến của định luật vật lý",
        "question": "Hai hệ quán tính có thể dùng những định luật khác nhau không?",
        "source": "37.1"
      },
      {
        "slug": "tinh-tuong-doi-dong-thoi",
        "title": "Tính tương đối của đồng thời",
        "question": "Vì sao hai sự kiện đồng thời trong một hệ lại không đồng thời trong hệ khác?",
        "source": "37.2"
      },
      {
        "slug": "gian-thoi-gian",
        "title": "Giãn thời gian và thời gian riêng",
        "question": "Đồng hồ chuyển động chạy chậm được xác định bằng phép đo nào?",
        "source": "37.3"
      },
      {
        "slug": "co-chieu-dai",
        "title": "Co chiều dài và hình dạng quan sát",
        "question": "Đo đồng thời hai đầu vật khác với chụp ảnh vật như thế nào?",
        "source": "37.4"
      },
      {
        "slug": "bien-doi-lorentz",
        "title": "Biến đổi Lorentz",
        "question": "Cùng một sự kiện và cùng một chuyển động có tọa độ nào trong hai hệ?",
        "source": "37.5"
      },
      {
        "slug": "doppler-dien-tu",
        "title": "Doppler của sóng điện từ",
        "question": "Tần số đổi thế nào trong khi tốc độ ánh sáng vẫn bằng c?",
        "source": "37.6"
      }
    ]
  },
  {
    "title": "Động lực học, năng lượng và hấp dẫn",
    "topics": [
      {
        "slug": "dong-luong-tuong-doi",
        "title": "Động lượng và lực tương đối tính",
        "question": "Vì sao lực dọc và lực ngang cho các hệ số gia tốc khác nhau?",
        "source": "37.7"
      },
      {
        "slug": "cong-nang-luong-tuong-doi",
        "title": "Công và năng lượng tương đối tính",
        "question": "Động năng, năng lượng nghỉ và năng lượng toàn phần liên hệ thế nào?",
        "source": "37.8"
      },
      {
        "slug": "newton-va-tuong-doi-rong",
        "title": "Cơ học Newton và thuyết tương đối rộng",
        "question": "Nguyên lý tương ứng và nguyên lý tương đương nói gì?",
        "source": "37.9"
      }
    ]
  }
]
