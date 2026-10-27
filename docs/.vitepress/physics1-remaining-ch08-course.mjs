export const physics1RemainingChapter8Parent={
  "chapter": 8,
  "topics": [
    {
      "slug": "dong-luong-va-xung-luong",
      "title": "Động lượng và xung lượng",
      "question": "Động lượng của một chất điểm được định nghĩa như thế nào và xung lượng của hợp lực tác dụng làm thay đổi động lượng ra sao?",
      "source": "8.1",
      "file": "01-muc-01.md"
    },
    {
      "slug": "dinh-luat-bao-toan-dong-luong",
      "title": "Định luật bảo toàn động lượng",
      "question": "Trong những điều kiện nào thì tổng động lượng của một hệ chất điểm được bảo toàn và nguyên lý này áp dụng ra sao cho chuyển động nhiều chiều?",
      "source": "8.2",
      "file": "02-muc-02.md"
    },
    {
      "slug": "bao-toan-dong-luong-va-va-cham",
      "title": "Bảo toàn động lượng và va chạm",
      "question": "Sự khác biệt về mặt cơ chế và năng lượng giữa va chạm đàn hồi, va chạm không đàn hồi và va chạm hoàn toàn mềm là gì?",
      "source": "8.3",
      "file": "03-muc-03.md"
    },
    {
      "slug": "va-cham-dan-hoi",
      "title": "Va chạm đàn hồi",
      "question": "Trong va chạm đàn hồi một chiều và hai chiều, các phương trình bảo toàn động lượng và bảo toàn động năng liên hệ với nhau như thế nào?",
      "source": "8.4",
      "file": "04-muc-04.md"
    },
    {
      "slug": "khoi-tam",
      "title": "Khối tâm",
      "question": "Khối tâm của một hệ chất điểm được xác định ra sao và hợp ngoại lực chi phối gia tốc của khối tâm theo quy luật nào?",
      "source": "8.5",
      "file": "05-muc-05.md"
    },
    {
      "slug": "chuyen-dong-phan-luc-ten-lua",
      "title": "Chuyển động phản lực của tên lửa",
      "question": "Phương trình chuyển động phản lực của tên lửa được thiết lập như thế nào khi khối lượng của tên lửa liên tục giảm theo thời gian?",
      "source": "8.6",
      "file": "06-muc-06.md"
    }
  ],
  "prerequisites": [
    "vector",
    "luc",
    "he-quy-chieu-quan-tinh",
    "van-toc-tuong-doi",
    "cong-nang-luong"
  ],
  "supportingConcepts": [
    "dong-luong-vat-ly",
    "khoi-tam",
    "va-cham-dan-hoi"
  ],
  "cheatsheet": {
    "summary": "Định nghĩa, tính chất, công thức và điều kiện của động lượng, xung lượng, va chạm, khối tâm và chuyển động phản lực. Các vận tốc và động lượng được tính trong cùng hệ quy chiếu quán tính.",
    "sections": [
      {
        "id": "momentum-impulse",
        "title": "Động lượng và xung lượng",
        "badge": "8.1",
        "items": [
          {
            "name": "Động lượng chất điểm",
            "description": "Trong cơ học Newton, động lượng là vector cùng hướng vận tốc khi khối lượng dương. Khối lượng chất điểm không đổi trong dạng định luật Newton dưới đây.",
            "formulaRows": [
              {
                "label": "Động lượng",
                "formula": "$$\n\\vec p=m\\vec v\n$$"
              },
              {
                "label": "Theo trục x",
                "formula": "$$\np_x=mv_x\n$$"
              },
              {
                "label": "Theo trục y",
                "formula": "$$\np_y=mv_y\n$$"
              },
              {
                "label": "Theo trục z",
                "formula": "$$\np_z=mv_z\n$$"
              },
              {
                "label": "Hợp lực",
                "formula": "$$\n\\vec F_{\\mathrm{net}}=\\frac{d\\vec p}{dt}\n$$"
              }
            ],
            "variables": [
              "$\\vec p$: Động lượng, đơn vị kg·m/s",
              "$m$: Khối lượng, đơn vị kg"
            ]
          },
          {
            "name": "Xung lượng của hợp lực",
            "description": "Xung lượng trong một khoảng thời gian bằng độ biến thiên động lượng. Với hợp lực biến đổi, phải dùng tích phân hoặc lực trung bình.",
            "formulaRows": [
              {
                "label": "Hợp lực không đổi",
                "formula": "$$\n\\vec J=\\vec F_{\\mathrm{net}}\\Delta t\n$$"
              },
              {
                "label": "Hợp lực biến đổi",
                "formula": "$$\n\\vec J=\\int_{t_1}^{t_2}\\vec F_{\\mathrm{net}}\\,dt\n$$"
              },
              {
                "label": "Định lý xung lượng–động lượng",
                "formula": "$$\n\\vec J=\\vec p_2-\\vec p_1\n$$"
              },
              {
                "label": "Lực trung bình",
                "formula": "$$\n\\vec F_{\\mathrm{av}}=\\frac{\\vec J}{\\Delta t}\n$$"
              }
            ],
            "variables": [
              "$\\vec J$: Xung lượng, đơn vị N·s, tương đương kg·m/s",
              "$\\Delta t=t_2-t_1$: Khoảng thời gian tác dụng"
            ]
          }
        ]
      },
      {
        "id": "momentum-conservation",
        "title": "Bảo toàn động lượng",
        "badge": "8.2",
        "items": [
          {
            "name": "Tổng động lượng",
            "description": "Với hệ hữu hạn n chất điểm có khối lượng không đổi, nội lực tuân theo định luật III Newton triệt tiêu từng đôi khi cộng toàn hệ.",
            "formulaRows": [
              {
                "label": "Tổng động lượng",
                "formula": "$$\n\\vec P=\\sum_{i=1}^{n}\\vec p_i\n$$"
              },
              {
                "label": "Dạng khai triển",
                "formula": "$$\n\\vec P=\\vec p_1+\\vec p_2+\\dots+\\vec p_n\n$$"
              },
              {
                "label": "Tốc độ biến thiên",
                "formula": "$$\n\\frac{d\\vec P}{dt}=\\vec F_{\\mathrm{ext}}\n$$"
              },
              {
                "label": "Điều kiện bảo toàn",
                "formula": "$$\n\\vec F_{\\mathrm{ext}}=\\vec0\\implies\\vec P_2=\\vec P_1\n$$"
              }
            ],
            "variables": [
              "Các chỉ số i từ 1 đến n: Những chất điểm trong hệ"
            ]
          },
          {
            "name": "Bảo toàn theo từng phương",
            "description": "Một thành phần tổng động lượng được bảo toàn nếu thành phần hợp ngoại lực tương ứng bằng không. Trong va chạm ngắn, có thể dùng gần đúng khi xung lượng ngoại lực không đáng kể.",
            "formulaRows": [
              {
                "label": "Theo trục x",
                "formula": "$$\nF_{\\mathrm{ext},x}=0\\implies P_{2x}=P_{1x}\n$$"
              },
              {
                "label": "Xung lượng ngoại lực",
                "formula": "$$\n\\Delta\\vec P=\\int_{t_1}^{t_2}\\vec F_{\\mathrm{ext}}\\,dt\n$$"
              }
            ],
            "variables": []
          }
        ]
      },
      {
        "id": "collision-types",
        "title": "Các dạng va chạm",
        "badge": "8.3",
        "items": [
          {
            "name": "Đàn hồi và không đàn hồi",
            "description": "Trong hệ không nhận xung lượng ngoại lực đáng kể, động lượng được bảo toàn. Va chạm đàn hồi còn bảo toàn tổng động năng. Trong va chạm tiêu tán thông thường, tổng động năng giảm.",
            "formulaRows": [
              {
                "label": "Đàn hồi",
                "formula": "$$\nK_2=K_1\n$$"
              },
              {
                "label": "Không đàn hồi có tiêu tán",
                "formula": "$$\nK_2<K_1\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Hoàn toàn không đàn hồi",
            "description": "Hai vật dính vào nhau sau va chạm nên có cùng vận tốc cuối. Tổng động lượng được bảo toàn khi bỏ qua xung lượng ngoại lực.",
            "formulaRows": [
              {
                "label": "Vận tốc chung",
                "formula": "$$\n\\vec V=\\frac{m_A\\vec v_{A1}+m_B\\vec v_{B1}}{m_A+m_B}\n$$"
              },
              {
                "label": "Tỉ số động năng khi B ban đầu đứng yên",
                "formula": "$$\n\\frac{K_2}{K_1}=\\frac{m_A}{m_A+m_B}\n$$"
              }
            ],
            "variables": [
              "$m_A,m_B>0$: Khối lượng hai vật",
              "$K_1>0$: Tổng động năng trước va chạm",
              "$K_2$: Tổng động năng sau va chạm"
            ]
          }
        ]
      },
      {
        "id": "elastic-collisions",
        "title": "Va chạm đàn hồi",
        "badge": "8.4",
        "items": [
          {
            "name": "Một chiều",
            "description": "Trong va chạm đàn hồi một chiều, vận tốc tương đối sau va chạm đổi dấu so với trước va chạm. Hai công thức theo tỉ số khối lượng dưới đây chỉ áp dụng khi B ban đầu đứng yên.",
            "formulaRows": [
              {
                "label": "Vận tốc tương đối",
                "formula": "$$\nv_{B2}-v_{A2}=-(v_{B1}-v_{A1})\n$$"
              },
              {
                "label": "Vận tốc A khi B ban đầu đứng yên",
                "formula": "$$\nv_{A2}=\\frac{m_A-m_B}{m_A+m_B}v_{A1}\n$$"
              },
              {
                "label": "Vận tốc B khi B ban đầu đứng yên",
                "formula": "$$\nv_{B2}=\\frac{2m_A}{m_A+m_B}v_{A1}\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Hai chiều",
            "description": "Cần đồng thời bảo toàn hai thành phần động lượng và tổng động năng. Muốn xác định bốn thành phần vận tốc cuối, cần thêm dữ kiện, chẳng hạn hướng hoặc độ lớn một vận tốc. Trong hệ hai vật bảo toàn động lượng, điều kiện đàn hồi tương đương với bảo toàn độ lớn vận tốc tương đối.",
            "formulaRows": [
              {
                "label": "Theo trục x",
                "formula": "$$\nP_{1x}=P_{2x}\n$$"
              },
              {
                "label": "Theo trục y",
                "formula": "$$\nP_{1y}=P_{2y}\n$$"
              },
              {
                "label": "Động năng",
                "formula": "$$\nK_1=K_2\n$$"
              },
              {
                "label": "Độ lớn vận tốc tương đối",
                "formula": "$$\n\\|\\vec v_{B2}-\\vec v_{A2}\\|=\\|\\vec v_{B1}-\\vec v_{A1}\\|\n$$"
              }
            ],
            "variables": []
          }
        ]
      },
      {
        "id": "center-of-mass",
        "title": "Khối tâm",
        "badge": "8.5",
        "items": [
          {
            "name": "Vị trí khối tâm",
            "description": "Khối tâm là trung bình vị trí có trọng số khối lượng. Với vật có khối lượng phân bố đối xứng, khối tâm nằm tại tâm hoặc trên trục đối xứng tương ứng và có thể ở ngoài phần vật chất.",
            "formulaRows": [
              {
                "label": "Tổng khối lượng",
                "formula": "$$\nM=\\sum_{i=1}^{n}m_i\n$$"
              },
              {
                "label": "Dạng khai triển khối lượng",
                "formula": "$$\nM=m_1+m_2+\\dots+m_n\n$$"
              },
              {
                "label": "Vị trí vector",
                "formula": "$$\n\\vec r_{\\mathrm{cm}}=\\frac1M\\sum_{i=1}^{n}m_i\\vec r_i\n$$"
              },
              {
                "label": "Hoành độ",
                "formula": "$$\nx_{\\mathrm{cm}}=\\frac1M\\sum_{i=1}^{n}m_ix_i\n$$"
              },
              {
                "label": "Tung độ",
                "formula": "$$\ny_{\\mathrm{cm}}=\\frac1M\\sum_{i=1}^{n}m_iy_i\n$$"
              },
              {
                "label": "Cao độ",
                "formula": "$$\nz_{\\mathrm{cm}}=\\frac1M\\sum_{i=1}^{n}m_iz_i\n$$"
              }
            ],
            "variables": [
              "Chỉ số cm: Khối tâm",
              "Các chỉ số i từ 1 đến n: Những phần tử của hệ",
              "$M>0$: Tổng khối lượng không đổi của hệ"
            ]
          },
          {
            "name": "Chuyển động khối tâm",
            "description": "Với tổng khối lượng không đổi, tổng động lượng bằng khối lượng toàn hệ nhân vận tốc khối tâm. Chỉ ngoại lực làm thay đổi chuyển động khối tâm.",
            "formulaRows": [
              {
                "label": "Tổng động lượng",
                "formula": "$$\n\\vec P=M\\vec v_{\\mathrm{cm}}\n$$"
              },
              {
                "label": "Gia tốc khối tâm",
                "formula": "$$\nM\\vec a_{\\mathrm{cm}}=\\vec F_{\\mathrm{ext}}\n$$"
              },
              {
                "label": "Không có hợp ngoại lực",
                "formula": "$$\n\\vec F_{\\mathrm{ext}}=\\vec0\\implies\\vec a_{\\mathrm{cm}}=\\vec0\n$$"
              }
            ],
            "variables": []
          }
        ]
      },
      {
        "id": "rocket-propulsion",
        "title": "Phản lực tên lửa",
        "badge": "8.6",
        "items": [
          {
            "name": "Lực đẩy và gia tốc",
            "description": "Tên lửa phụt khí về phía sau với tốc độ tương đối dương u. Khối lượng tức thời m giảm. Các công thức gia tốc và vận tốc dưới đây bỏ qua ngoại lực trọng trường và lực cản.",
            "formulaRows": [
              {
                "label": "Lực đẩy",
                "formula": "$$\nF=-u\\frac{dm}{dt}\n$$"
              },
              {
                "label": "Gia tốc",
                "formula": "$$\na=-\\frac um\\frac{dm}{dt}\n$$"
              },
              {
                "label": "Độ tăng vận tốc khi u không đổi",
                "formula": "$$\nv-v_0=u\\ln\\frac{m_0}{m}\n$$"
              },
              {
                "label": "Vận tốc khí trong hệ quy chiếu quan sát",
                "formula": "$$\nv_{\\mathrm{fuel}}=v-u\n$$"
              }
            ],
            "variables": [
              "$u$: Tốc độ phụt khí đối với tên lửa, tương ứng v_ex",
              "$dm/dt<0$: Tốc độ biến thiên khối lượng tên lửa",
              "$m_0$: Khối lượng ban đầu, gồm cả nhiên liệu",
              "$0<m\\le m_0$: Khối lượng còn lại dương"
            ]
          }
        ]
      }
    ]
  }
}
