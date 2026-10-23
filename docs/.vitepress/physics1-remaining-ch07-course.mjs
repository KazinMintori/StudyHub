export const physics1RemainingChapter7Parent={
  "chapter": 7,
  "topics": [
    {
      "slug": "the-nang-trong-truong",
      "title": "Thế năng trọng trường",
      "question": "Thế năng trọng trường được định nghĩa thế nào và khi nào cơ năng được bảo toàn trong chuyển động thẳng đứng?",
      "source": "7.1",
      "file": "01-muc-01.md"
    },
    {
      "slug": "the-nang-dan-hoi",
      "title": "Thế năng đàn hồi",
      "question": "Năng lượng tích trữ trong lò xo biến dạng phụ thuộc vào độ biến dạng ra sao?",
      "source": "7.2",
      "file": "02-muc-02.md"
    },
    {
      "slug": "luc-bao-toan-va-khong-bao-toan",
      "title": "Lực bảo toàn và lực không bảo toàn",
      "question": "Dấu hiệu phân biệt lực bảo toàn với lực không bảo toàn và định luật bảo toàn năng lượng tổng quát là gì?",
      "source": "7.3",
      "file": "03-muc-03.md"
    },
    {
      "slug": "luc-va-the-nang",
      "title": "Lực và thế năng",
      "question": "Làm thế nào xác định lực tác dụng khi biết hàm thế năng của hệ?",
      "source": "7.4",
      "file": "04-muc-04.md"
    },
    {
      "slug": "do-thi-nang-luong",
      "title": "Đồ thị năng lượng",
      "question": "Đồ thị thế năng cho biết gì về giới hạn chuyển động và các vị trí cân bằng bền, không bền?",
      "source": "7.5",
      "file": "05-muc-05.md"
    }
  ],
  "prerequisites": [
    "luc",
    "cong-nang-luong",
    "dao-ham",
    "tich-phan"
  ],
  "supportingConcepts": [
    "can-bang-co-hoc",
    "gia-toc",
    "vector"
  ],
  "cheatsheet": {
    "summary": "Định nghĩa, tính chất, công thức và điều kiện về thế năng, cơ năng, lực bảo toàn và đồ thị năng lượng. Dùng chỉ số g cho trọng trường, e cho đàn hồi và o cho công của các lực khác.",
    "sections": [
      {
        "id": "gravitational-potential",
        "title": "Thế năng trọng trường",
        "badge": "7.1",
        "items": [
          {
            "name": "Thế năng gần mặt đất",
            "description": "Trong miền gia tốc trọng trường không đổi, trục y hướng lên. Thế năng của hệ vật–Trái Đất phụ thuộc mốc, còn hiệu thế năng không phụ thuộc hằng số cộng.",
            "formulaRows": [
              {
                "label": "Thế năng",
                "formula": "$$\nU_g=mgy\n$$"
              },
              {
                "label": "Độ biến thiên",
                "formula": "$$\n\\Delta U_g=U_{g,2}-U_{g,1}\n$$"
              },
              {
                "label": "Công trọng lực",
                "formula": "$$\nW_g=-\\Delta U_g\n$$"
              }
            ],
            "variables": [
              "$m$: Khối lượng, đơn vị kg",
              "$g$: Gia tốc trọng trường, đơn vị m/s²",
              "$y$: Độ cao so với mốc, đơn vị m"
            ]
          },
          {
            "name": "Cơ năng",
            "description": "Động năng và thế năng phải được tính trong cùng hệ quy chiếu và theo cùng quy ước mốc.",
            "formulaRows": [
              {
                "label": "Cơ năng tại trạng thái i",
                "formula": "$$\nE_i=K_i+U_{g,i}\n$$"
              },
              {
                "label": "Chỉ trọng lực sinh công",
                "formula": "$$\nE_1=E_2\n$$"
              },
              {
                "label": "Lực khác sinh công",
                "formula": "$$\nW_o=E_2-E_1\n$$"
              }
            ],
            "variables": []
          }
        ]
      },
      {
        "id": "elastic-potential",
        "title": "Thế năng đàn hồi",
        "badge": "7.2",
        "items": [
          {
            "name": "Lò xo lý tưởng",
            "description": "Định luật Hooke trong miền tuyến tính, x tính từ chiều dài tự nhiên. Chọn thế năng bằng không khi lò xo không biến dạng.",
            "formulaRows": [
              {
                "label": "Lực lò xo",
                "formula": "$$\nF_x=-kx\n$$"
              },
              {
                "label": "Thế năng đàn hồi",
                "formula": "$$\nU_e=\\frac12kx^2\n$$"
              },
              {
                "label": "Công của lò xo",
                "formula": "$$\nW_e=-\\Delta U_e\n$$"
              }
            ],
            "variables": [
              "$k$: Độ cứng, đơn vị N/m",
              "$x$: Độ dãn hoặc nén có dấu, đơn vị m"
            ]
          },
          {
            "name": "Cân bằng năng lượng",
            "description": "Bỏ qua động năng lò xo khi khối lượng lò xo nhỏ so với vật. Công của lực khác bằng độ biến thiên cơ năng.",
            "formulaRows": [
              {
                "label": "Tổng thế năng",
                "formula": "$$\nU=U_g+U_e\n$$"
              },
              {
                "label": "Cơ năng",
                "formula": "$$\nE=K+U\n$$"
              },
              {
                "label": "Phương trình năng lượng",
                "formula": "$$\nK_1+U_1+W_o=K_2+U_2\n$$"
              },
              {
                "label": "Nếu chỉ trọng lực và đàn hồi sinh công",
                "formula": "$$\nW_o=0\\implies E_1=E_2\n$$"
              }
            ],
            "variables": []
          }
        ]
      },
      {
        "id": "conservative-forces",
        "title": "Lực bảo toàn và nội năng",
        "badge": "7.3",
        "items": [
          {
            "name": "Lực bảo toàn",
            "description": "Công giữa hai điểm không phụ thuộc đường đi, tương đương công trên mọi đường kín trong miền xét bằng không. Có thể biểu diễn công bằng độ giảm thế năng.",
            "formulaRows": [
              {
                "label": "Công trên đường kín",
                "formula": "$$\n\\oint\\vec F\\cdot d\\vec l=0\n$$"
              },
              {
                "label": "Công giữa hai điểm",
                "formula": "$$\nW_{1\\to2}=U_1-U_2\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Ma sát trượt trên mặt cố định",
            "description": "Với lực ma sát có độ lớn không đổi, công ma sát trên vật là âm. Khi hệ chỉ chuyển hóa cơ năng thành nội năng và không trao đổi năng lượng ra ngoài, tổng các dạng năng lượng được bảo toàn.",
            "formulaRows": [
              {
                "label": "Công ma sát",
                "formula": "$$\nW_f=-f_ks\n$$"
              },
              {
                "label": "Bảo toàn năng lượng",
                "formula": "$$\n\\Delta K+\\Delta U+\\Delta U_{\\mathrm{int}}=0\n$$"
              },
              {
                "label": "Chuyển hóa cơ năng thành nội năng",
                "formula": "$$\n\\Delta U_{\\mathrm{int}}=-\\Delta E\n$$"
              }
            ],
            "variables": [
              "$s$: Quãng đường trượt tương đối trên mặt cố định",
              "$U_{\\mathrm{int}}$: Nội năng của toàn hệ gồm các vật tiếp xúc"
            ]
          }
        ]
      },
      {
        "id": "force-potential",
        "title": "Lực và thế năng",
        "badge": "7.4",
        "items": [
          {
            "name": "Một chiều",
            "description": "Lực phụ thuộc độ dốc thế năng, không phụ thuộc dấu hoặc hằng số cộng của thế năng.",
            "formulaRows": [
              {
                "label": "Thành phần lực",
                "formula": "$$\nF_x=-\\frac{dU}{dx}\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Ba chiều",
            "description": "Mỗi đạo hàm riêng giữ các tọa độ còn lại cố định. Gradient hướng tăng thế năng nhanh nhất tại điểm xét, lực bảo toàn hướng ngược lại.",
            "formulaRows": [
              {
                "label": "Thành phần x",
                "formula": "$$\nF_x=-\\frac{\\partial U}{\\partial x}\n$$"
              },
              {
                "label": "Thành phần y",
                "formula": "$$\nF_y=-\\frac{\\partial U}{\\partial y}\n$$"
              },
              {
                "label": "Thành phần z",
                "formula": "$$\nF_z=-\\frac{\\partial U}{\\partial z}\n$$"
              },
              {
                "label": "Dạng vector",
                "formula": "$$\n\\vec F=-\\vec\\nabla U\n$$"
              }
            ],
            "variables": []
          }
        ]
      },
      {
        "id": "energy-diagrams",
        "title": "Đồ thị năng lượng và cân bằng",
        "badge": "7.5",
        "items": [
          {
            "name": "Miền chuyển động và điểm đổi chiều",
            "description": "Với cơ năng bảo toàn, chuyển động chỉ xảy ra trong miền động năng không âm. Tại một biên miền có lực khác không, vận tốc bằng không rồi đổi chiều.",
            "formulaRows": [
              {
                "label": "Động năng",
                "formula": "$$\nK=E-U(x)\n$$"
              },
              {
                "label": "Miền được phép",
                "formula": "$$\nU(x)\\le E\n$$"
              },
              {
                "label": "Điểm dừng tức thời",
                "formula": "$$\nK=0\\iff U(x)=E\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Phân loại cân bằng",
            "description": "Trong một chiều, cân bằng bền ở cực tiểu địa phương và không bền ở cực đại. Dấu đạo hàm bậc hai là điều kiện đủ tại điểm dừng không suy biến. Khi đạo hàm bậc hai bằng không, phải xét thêm hình dạng của thế năng.",
            "formulaRows": [
              {
                "label": "Vị trí cân bằng",
                "formula": "$$\nF_x=0\\iff U'(x)=0\n$$"
              },
              {
                "label": "Đủ để cân bằng bền tại điểm dừng",
                "formula": "$$\nU''(x)>0\n$$"
              },
              {
                "label": "Đủ để cân bằng không bền tại điểm dừng",
                "formula": "$$\nU''(x)<0\n$$"
              }
            ],
            "variables": []
          }
        ]
      }
    ]
  }
}
