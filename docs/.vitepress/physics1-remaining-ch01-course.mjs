export const physics1RemainingChapter1Parent={
  "chapter": 1,
  "topics": [
    {
      "slug": "ban-chat-vat-ly",
      "title": "Bản chất của vật lý",
      "question": "Lý thuyết vật lý được hình thành và kiểm chứng qua thực nghiệm như thế nào?",
      "source": "1.1",
      "file": "01-ban-chat-vat-ly.md"
    },
    {
      "slug": "giai-bai-toan-vat-ly",
      "title": "Giải bài toán vật lý",
      "question": "Quy trình bốn bước I SEE và phương pháp mô hình lý tưởng hóa vận hành ra sao?",
      "source": "1.2",
      "file": "02-giai-bai-toan.md"
    },
    {
      "slug": "chuan-va-don-vi",
      "title": "Chuẩn đo lường và hệ đơn vị SI",
      "question": "Giây, mét, kilôgam và các tiền tố đơn vị được xác định, sử dụng như thế nào?",
      "source": "1.3",
      "file": "03-chuan-va-don-vi.md"
    },
    {
      "slug": "su-dung-doi-don-vi",
      "title": "Sử dụng và đổi đơn vị",
      "question": "Tính nhất quán thứ nguyên và phương pháp hệ số đổi đơn vị được áp dụng ra sao?",
      "source": "1.4",
      "file": "04-su-dung-doi-don-vi.md"
    },
    {
      "slug": "do-bat-dinh-chu-so",
      "title": "Độ bất định và chữ số có nghĩa",
      "question": "Quy tắc xác định chữ số có nghĩa trong phép tính nhân, chia, cộng, trừ là gì?",
      "source": "1.5",
      "file": "05-do-bat-dinh-chu-so.md"
    },
    {
      "slug": "uoc-luong-bac-do-lon",
      "title": "Ước lượng và bậc độ lớn",
      "question": "Làm thế nào để ước lượng gần đúng theo bậc độ lớn khi thiếu dữ liệu chính xác?",
      "source": "1.6",
      "file": "06-uoc-luong.md"
    },
    {
      "slug": "vector-va-phep-cong-vector",
      "title": "Vector và phép cộng vector",
      "question": "Phép cộng và trừ vector theo phương pháp hình học tuân theo những định luật nào?",
      "source": "1.7",
      "file": "07-vector-cong-vector.md"
    },
    {
      "slug": "thanh-phan-vector",
      "title": "Thành phần của vector",
      "question": "Làm thế nào xác định, cộng và nhân các thành phần của vector?",
      "source": "1.8",
      "file": "08-thanh-phan-vector.md"
    },
    {
      "slug": "vector-don-vi",
      "title": "Vector đơn vị",
      "question": "Hệ vector đơn vị trực chuẩn biểu diễn các vector trong không gian như thế nào?",
      "source": "1.9",
      "file": "09-vector-don-vi.md"
    },
    {
      "slug": "cac-phep-nhan-vector",
      "title": "Các phép nhân vector",
      "question": "Sự khác biệt về định nghĩa và ý nghĩa hình học giữa tích vô hướng và tích có hướng là gì?",
      "source": "1.10",
      "file": "10-tich-vector.md"
    }
  ],
  "prerequisites": [],
  "supportingConcepts": [
    "don-vi",
    "vector",
    "thanh-phan-vector",
    "tich-vo-huong",
    "tich-co-huong"
  ],
  "cheatsheet": {
    "summary": "Định nghĩa, tính chất và công thức về đơn vị, độ bất định, chữ số có nghĩa, thành phần vector và hai phép nhân vector.",
    "sections": [
      {
        "id": "units",
        "title": "Đại lượng vật lý và đơn vị",
        "badge": "1.1–1.4",
        "items": [
          {
            "name": "Đại lượng vật lý và đơn vị",
            "description": "Một giá trị đo gồm con số và đơn vị. Đơn vị dẫn xuất được lập từ các đơn vị cơ bản. Trong cơ học, các đơn vị cơ bản là mét, kilôgam và giây.",
            "formulaRows": [],
            "variables": []
          },
          {
            "name": "Các chuẩn SI",
            "description": "Giây dựa trên bức xạ của nguyên tử cesium-133. Mét được xác định từ tốc độ ánh sáng. Kilôgam dựa trên hằng số Planck.",
            "formulaRows": [
              {
                "label": "Tần số bức xạ cesium-133",
                "formula": "$$\nf_{\\mathrm{Cs}}=9\\,192\\,631\\,770\\,\\mathrm{Hz}\n$$"
              },
              {
                "label": "Tốc độ ánh sáng trong chân không",
                "formula": "$$\nc=299\\,792\\,458\\,\\mathrm{m/s}\n$$"
              },
              {
                "label": "Hằng số Planck, đơn vị J·s",
                "formula": "$$\nh=6{,}62607015\\times10^{-34}\\,\\mathrm{J\\,s}\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Tiền tố độ dài",
            "description": "Các hệ số thập phân là chính xác.",
            "formulaRows": [
              {
                "label": "Kilômét",
                "formula": "$$\n1\\,\\mathrm{km}=10^3\\,\\mathrm m\n$$"
              },
              {
                "label": "Centimét",
                "formula": "$$\n1\\,\\mathrm{cm}=10^{-2}\\,\\mathrm m\n$$"
              },
              {
                "label": "Milimét",
                "formula": "$$\n1\\,\\mathrm{mm}=10^{-3}\\,\\mathrm m\n$$"
              },
              {
                "label": "Micrômét",
                "formula": "$$\n1\\,\\mu\\mathrm m=10^{-6}\\,\\mathrm m\n$$"
              },
              {
                "label": "Nanômét",
                "formula": "$$\n1\\,\\mathrm{nm}=10^{-9}\\,\\mathrm m\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Đổi đơn vị",
            "description": "Nhân giá trị với một hệ số đổi đơn vị bằng một. Đơn vị cũng được nhân, chia và khử như các thừa số đại số.",
            "formulaRows": [
              {
                "label": "Inch và centimét",
                "formula": "$$\n1\\,\\mathrm{in}=2{,}54\\,\\mathrm{cm}\n$$"
              },
              {
                "label": "Pound lực và newton",
                "formula": "$$\n1\\,\\mathrm{lbf}=4{,}448221615260\\,\\mathrm N\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Tính nhất quán thứ nguyên",
            "description": "Các số hạng được cộng và hai vế của phương trình phải có thứ nguyên phù hợp. Nhất quán thứ nguyên là điều kiện cần, chưa đủ để chứng minh phương trình đúng.",
            "formulaRows": [],
            "variables": []
          }
        ]
      },
      {
        "id": "measurement",
        "title": "Độ bất định, chữ số có nghĩa và ước lượng",
        "badge": "1.5–1.6",
        "items": [
          {
            "name": "Độ bất định tương đối",
            "description": "Với giá trị đo khác không, độ bất định tương đối bằng độ bất định tuyệt đối chia độ lớn giá trị đo.",
            "formulaRows": [
              {
                "label": "Độ bất định tương đối",
                "formula": "$$\n\\varepsilon_r=\\frac{\\Delta x}{|x|}\n$$"
              },
              {
                "label": "Biểu diễn theo phần trăm",
                "formula": "$$\n\\varepsilon_{\\%}=100\\varepsilon_r\\%\n$$"
              }
            ],
            "variables": [
              "$\\Delta x$: Độ bất định tuyệt đối, cùng đơn vị với $x$."
            ]
          },
          {
            "name": "Nhân và chia",
            "description": "Kết quả giữ số chữ số có nghĩa bằng số chữ số có nghĩa ít nhất trong các dữ kiện đo tham gia phép tính.",
            "formulaRows": [],
            "variables": []
          },
          {
            "name": "Cộng và trừ",
            "description": "Kết quả làm tròn tới hàng thập phân kém chính xác nhất của các số hạng. Đây là quy tắc về hàng thập phân, khác quy tắc cho phép nhân và chia.",
            "formulaRows": [],
            "variables": []
          },
          {
            "name": "Chữ số chính xác và làm tròn",
            "description": "Hệ số đổi đơn vị chính xác không giới hạn số chữ số có nghĩa. Giữ thêm chữ số ở các bước trung gian và làm tròn kết quả cuối.",
            "formulaRows": [],
            "variables": []
          },
          {
            "name": "Độ chụm và độ đúng",
            "description": "Độ chụm mô tả mức gần nhau của các kết quả đo lặp. Độ đúng mô tả mức phù hợp với giá trị được chấp nhận. Các phép đo có thể chụm mà vẫn sai lệch có hệ thống.",
            "formulaRows": [],
            "variables": []
          },
          {
            "name": "Ước lượng bậc độ lớn",
            "description": "Dùng những giá trị gần đúng và mô hình đơn giản để xác định quy mô của một đại lượng. Kết quả có thể hữu ích dù không có nhiều chữ số chính xác.",
            "formulaRows": [],
            "variables": []
          }
        ]
      },
      {
        "id": "vectors",
        "title": "Vector và thành phần",
        "badge": "1.7–1.9",
        "items": [
          {
            "name": "Vô hướng và vector",
            "description": "Đại lượng vô hướng có giá trị số. Vector có độ lớn và hướng. Vector bằng không có độ lớn bằng không và không có hướng xác định.",
            "formulaRows": [
              {
                "label": "Độ lớn",
                "formula": "$$\nA=\\|\\vec A\\|\\ge0\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Cộng, trừ và nhân với số",
            "description": "Cộng vector theo quy tắc nối đuôi vào đầu hoặc quy tắc hình bình hành. Nhân với số âm đảo hướng, còn độ lớn được nhân với trị tuyệt đối của số ấy.",
            "formulaRows": [
              {
                "label": "Giao hoán",
                "formula": "$$\n\\vec A+\\vec B=\\vec B+\\vec A\n$$"
              },
              {
                "label": "Kết hợp",
                "formula": "$$\n(\\vec A+\\vec B)+\\vec C=\\vec A+(\\vec B+\\vec C)\n$$"
              },
              {
                "label": "Phép trừ",
                "formula": "$$\n\\vec A-\\vec B=\\vec A+(-\\vec B)\n$$"
              },
              {
                "label": "Nhân với số c",
                "formula": "$$\n\\|c\\vec A\\|=|c|A\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Các thành phần",
            "description": "Trong mặt phẳng, θ đo từ trục +x về phía +y theo chiều ngược kim đồng hồ. Các thành phần là đại lượng đại số, không phải vector.",
            "formulaRows": [
              {
                "label": "Thành phần ngang",
                "formula": "$$\nA_x=A\\cos\\theta\n$$"
              },
              {
                "label": "Thành phần đứng",
                "formula": "$$\nA_y=A\\sin\\theta\n$$"
              },
              {
                "label": "Độ lớn trong không gian",
                "formula": "$$\nA=\\sqrt{A_x^2+A_y^2+A_z^2}\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Góc từ các thành phần",
            "description": "Công thức tang chỉ dùng khi Aₓ khác không. Phải chọn góc phần tư theo dấu cả hai thành phần. Nếu Aₓ=0 thì hướng nằm trên trục y. Nếu cả hai bằng không thì hướng không xác định.",
            "formulaRows": [
              {
                "label": "Aₓ khác không",
                "formula": "$$\n\\tan\\theta=\\frac{A_y}{A_x}\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Cộng theo thành phần",
            "description": "Thành phần tổng bằng tổng các thành phần tương ứng. Ví dụ ba vector được viết tường minh như sau.",
            "formulaRows": [
              {
                "label": "Hợp của ba vector",
                "formula": "$$\n\\vec R=\\vec A+\\vec B+\\vec C\n$$"
              },
              {
                "label": "Các thành phần",
                "formula": "$$\n\\begin{aligned}&R_x=A_x+B_x+C_x,\\\\&R_y=A_y+B_y+C_y,\\\\&R_z=A_z+B_z+C_z.\\end{aligned}\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Vector đơn vị",
            "description": "Có độ lớn bằng một và không mang đơn vị đo. Các vector đơn vị i, j, k hướng theo ba trục tọa độ dương.",
            "formulaRows": [
              {
                "label": "Biểu diễn vector",
                "formula": "$$\n\\vec A=A_x\\hat i+A_y\\hat j+A_z\\hat k\n$$"
              },
              {
                "label": "Độ lớn vector đơn vị",
                "formula": "$$\n\\|\\hat i\\|=\\|\\hat j\\|=\\|\\hat k\\|=1\n$$"
              }
            ],
            "variables": []
          }
        ]
      },
      {
        "id": "products",
        "title": "Các phép nhân vector",
        "badge": "1.10",
        "items": [
          {
            "name": "Tích vô hướng",
            "description": "Kết quả là một đại lượng vô hướng. Với hai vector khác không, φ là góc giữa chúng trong khoảng từ 0° đến 180°. Ký hiệu S là tích vô hướng của hai vector.",
            "formulaRows": [
              {
                "label": "Định nghĩa",
                "formula": "$$\n\\vec A\\cdot\\vec B=AB\\cos\\varphi\n$$"
              },
              {
                "label": "Theo thành phần",
                "formula": "$$\nS=A_xB_x+A_yB_y+A_zB_z\n$$"
              },
              {
                "label": "Góc khi A,B khác không",
                "formula": "$$\n\\cos\\varphi=\\frac{\\vec A\\cdot\\vec B}{AB}\n$$"
              },
              {
                "label": "Giao hoán",
                "formula": "$$\n\\vec A\\cdot\\vec B=\\vec B\\cdot\\vec A\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Tích có hướng",
            "description": "Với hai vector không cùng phương và khác không, kết quả vuông góc mặt phẳng của chúng, hướng theo quy tắc bàn tay phải. Nếu cùng phương hoặc có vector không, kết quả là vector không.",
            "formulaRows": [
              {
                "label": "Độ lớn",
                "formula": "$$\nC=AB\\sin\\varphi\n$$"
              },
              {
                "label": "Phản giao hoán",
                "formula": "$$\n\\vec A\\times\\vec B=-\\vec B\\times\\vec A\n$$"
              },
              {
                "label": "Đặt vector kết quả",
                "formula": "$$\n\\vec C=\\vec A\\times\\vec B\n$$"
              },
              {
                "label": "Thành phần trong hệ tọa độ thuận",
                "formula": "$$\n\\begin{aligned}&C_x=A_yB_z-A_zB_y,\\\\&C_y=A_zB_x-A_xB_z,\\\\&C_z=A_xB_y-A_yB_x.\\end{aligned}\n$$"
              }
            ],
            "variables": []
          }
        ]
      }
    ]
  }
}
