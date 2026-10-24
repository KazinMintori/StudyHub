export const physics1RemainingChapter5Parent={
  "chapter": 5,
  "topics": [
    {
      "slug": "can-bang-chat-diem-dinh-luat-1",
      "title": "Sử dụng định luật I Newton: Chất điểm cân bằng",
      "question": "Làm thế nào xác định lực khi vật đứng yên hoặc chuyển động thẳng đều?",
      "source": "5.1",
      "file": "01-muc-01.md"
    },
    {
      "slug": "dong-luc-hoc-chat-diem-dinh-luat-2",
      "title": "Sử dụng định luật II Newton: Động lực học chất điểm",
      "question": "Phân tích lực và gia tốc của một hoặc nhiều vật bằng cách nào?",
      "source": "5.2",
      "file": "02-muc-02.md"
    },
    {
      "slug": "luc-ma-sat-va-luc-can",
      "title": "Lực ma sát và lực cản chất lưu",
      "question": "Điều kiện tiếp xúc và vận tốc tương đối quyết định ma sát, lực cản ra sao?",
      "source": "5.3",
      "file": "03-muc-03.md"
    },
    {
      "slug": "dong-luc-hoc-chuyen-dong-tron",
      "title": "Động lực học chuyển động tròn",
      "question": "Các lực thực tế tạo thành phần hướng tâm như thế nào?",
      "source": "5.4",
      "file": "04-muc-04.md"
    },
    {
      "slug": "cac-luc-co-ban-trong-tu-nhien",
      "title": "Các tương tác cơ bản của tự nhiên",
      "question": "Bốn tương tác cơ bản có những tính chất chủ yếu gì?",
      "source": "5.5",
      "file": "05-muc-05.md"
    }
  ],
  "prerequisites": [
    "vector",
    "thanh-phan-vector",
    "luc",
    "he-quy-chieu-quan-tinh",
    "gia-toc",
    "gia-toc-huong-tam"
  ],
  "supportingConcepts": [
    "luc-phap-tuyen",
    "ma-sat-nghi",
    "ma-sat-truot",
    "can-bang-co-hoc",
    "dao-ham",
    "tich-phan"
  ],
  "cheatsheet": {
    "summary": "Định nghĩa, tính chất, điều kiện áp dụng và công thức về cân bằng, động lực học, ma sát, lực cản, chuyển động tròn và các tương tác cơ bản.",
    "sections": [
      {
        "id": "equilibrium",
        "title": "Cân bằng chất điểm",
        "badge": "5.1",
        "items": [
          {
            "name": "Điều kiện cân bằng",
            "description": "Áp dụng trong hệ quy chiếu quán tính. Vật đứng yên hoặc có vector vận tốc không đổi.",
            "formulaRows": [
              {
                "label": "Tổng ngoại lực",
                "formula": "$$\n\\sum\\vec F=\\vec0\n$$"
              },
              {
                "label": "Theo hai phương độc lập",
                "formula": "$$\n\\begin{aligned}&\\sum F_x=0,\\\\&\\sum F_y=0.\\end{aligned}\n$$"
              }
            ],
            "variables": [
              "$\\vec F$: Ngoại lực tác dụng lên vật (N)."
            ]
          },
          {
            "name": "Dây nhẹ và ròng rọc lý tưởng",
            "description": "Dây có khối lượng không đáng kể, ròng rọc lý tưởng và dây còn căng. Hai lực căng có cùng độ lớn.",
            "formulaRows": [
              {
                "label": "Lực căng",
                "formula": "$$\nT_1=T_2\n$$"
              }
            ],
            "variables": [
              "$T$: Độ lớn lực căng (N)."
            ]
          },
          {
            "name": "Cân bằng trên mặt nghiêng",
            "description": "Cáp song song mặt nghiêng, không có ma sát. Góc nghiêng là α.",
            "formulaRows": [
              {
                "label": "Lực căng cáp",
                "formula": "$$\nT=w\\sin\\alpha\n$$"
              },
              {
                "label": "Lực pháp tuyến",
                "formula": "$$\nn=w\\cos\\alpha\n$$"
              }
            ],
            "variables": [
              "$w=mg$: Trọng lượng (N)."
            ]
          }
        ]
      },
      {
        "id": "dynamics",
        "title": "Động lực học và trọng lượng biểu kiến",
        "badge": "5.2",
        "items": [
          {
            "name": "Định luật II Newton",
            "description": "Khối lượng không đổi và hệ quy chiếu quán tính.",
            "formulaRows": [
              {
                "label": "Dạng vector",
                "formula": "$$\n\\sum\\vec F=m\\vec a\n$$"
              },
              {
                "label": "Theo hai phương",
                "formula": "$$\n\\begin{aligned}&\\sum F_x=ma_x,\\\\&\\sum F_y=ma_y.\\end{aligned}\n$$"
              }
            ],
            "variables": [
              "$m$: Khối lượng (kg).",
              "$\\vec a$: Gia tốc (m/s²)."
            ]
          },
          {
            "name": "Trọng lượng biểu kiến",
            "description": "Trong thang máy, trục dương thẳng đứng hướng lên. Người và cân cùng gia tốc, vẫn tiếp xúc.",
            "formulaRows": [
              {
                "label": "Số chỉ cân",
                "formula": "$$\nn=m(g+a_y)\n$$"
              },
              {
                "label": "Rơi tự do",
                "formula": "$$\na_y=-g\\implies n=0\n$$"
              }
            ],
            "variables": [
              "$n$: Lực pháp tuyến của cân (N).",
              "$a_y$: Gia tốc thẳng đứng của người (m/s²)."
            ]
          },
          {
            "name": "Hai vật nối dây qua ròng rọc",
            "description": "Vật m₁ trên bàn ngang không ma sát, vật m₂ treo thẳng đứng. Dây nhẹ, không dãn và ròng rọc lý tưởng.",
            "formulaRows": [
              {
                "label": "Độ lớn gia tốc",
                "formula": "$$\na=\\frac{m_2g}{m_1+m_2}\n$$"
              },
              {
                "label": "Lực căng",
                "formula": "$$\nT=\\frac{m_1m_2g}{m_1+m_2}\n$$"
              }
            ],
            "variables": []
          }
        ]
      },
      {
        "id": "friction",
        "title": "Ma sát và lực cản chất lưu",
        "badge": "5.3",
        "items": [
          {
            "name": "Ma sát trượt",
            "description": "Ngược chiều trượt tương đối. Quan hệ gần đúng giữa độ lớn ma sát và độ lớn pháp tuyến.",
            "formulaRows": [
              {
                "label": "Độ lớn",
                "formula": "$$\nf_k=\\mu_kn\n$$"
              }
            ],
            "variables": [
              "$\\mu_k$: Hệ số ma sát trượt, không có đơn vị."
            ]
          },
          {
            "name": "Ma sát nghỉ",
            "description": "Chống xu hướng trượt tương đối. Chỉ đạt cực đại khi sắp trượt, còn giá trị thực tế được xác định bằng phương trình lực.",
            "formulaRows": [
              {
                "label": "Miền giá trị",
                "formula": "$$\n0\\le f_s\\le\\mu_sn\n$$"
              },
              {
                "label": "Giới hạn",
                "formula": "$$\n(f_s)_{\\max}=\\mu_sn\n$$"
              }
            ],
            "variables": [
              "$\\mu_s$: Hệ số ma sát nghỉ, không có đơn vị."
            ]
          },
          {
            "name": "Ma sát lăn",
            "description": "Lực kéo ngang để lăn đều trên mặt phẳng ngang chia cho lực pháp tuyến.",
            "formulaRows": [
              {
                "label": "Hệ số",
                "formula": "$$\n\\mu_r=\\frac{F_{\\mathrm{keo}}}{n}\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Ma sát trên mặt nghiêng",
            "description": "Lấy chiều dương xuống dốc. Vật đang trượt và hệ số ma sát trượt không đổi.",
            "formulaRows": [
              {
                "label": "Trượt đều xuống",
                "formula": "$$\n\\tan\\alpha=\\mu_k\n$$"
              },
              {
                "label": "Gia tốc khi trượt xuống",
                "formula": "$$\na_x=g(\\sin\\alpha-\\mu_k\\cos\\alpha)\n$$"
              },
              {
                "label": "Gia tốc khi trượt lên",
                "formula": "$$\na_x=g(\\sin\\alpha+\\mu_k\\cos\\alpha)\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Mô hình lực cản",
            "description": "Lực cản ngược chiều vận tốc của vật đối với chất lưu.",
            "formulaRows": [
              {
                "label": "Vật nhỏ, tốc độ thấp",
                "formula": "$$\nf=kv\n$$"
              },
              {
                "label": "Mô hình cản bậc hai",
                "formula": "$$\nf=Dv^2\n$$"
              }
            ],
            "variables": [
              "$k$: Hệ số cản tuyến tính (kg/s).",
              "$D$: Hệ số cản bậc hai (kg/m)."
            ]
          },
          {
            "name": "Tốc độ giới hạn khi rơi",
            "description": "Bỏ qua lực đẩy nổi, trọng lực cân bằng lực cản ở giới hạn.",
            "formulaRows": [
              {
                "label": "Cản tuyến tính",
                "formula": "$$\nv_t=\\frac{mg}{k}\n$$"
              },
              {
                "label": "Cản bậc hai",
                "formula": "$$\nv_t=\\sqrt{\\frac{mg}{D}}\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Rơi từ nghỉ với cản tuyến tính",
            "description": "Trục y hướng xuống, y(0)=0 và vᵧ(0)=0. Các hệ số và g không đổi.",
            "formulaRows": [
              {
                "label": "Vận tốc",
                "formula": "$$\nv_y=v_t(1-e^{-kt/m})\n$$"
              },
              {
                "label": "Gia tốc",
                "formula": "$$\na_y=ge^{-kt/m}\n$$"
              },
              {
                "label": "Tọa độ",
                "formula": "$$\ny=v_tt-\\frac{mv_t}{k}(1-e^{-kt/m})\n$$"
              }
            ],
            "variables": []
          }
        ]
      },
      {
        "id": "circular",
        "title": "Động lực học chuyển động tròn",
        "badge": "5.4",
        "items": [
          {
            "name": "Gia tốc và hợp lực hướng tâm",
            "description": "Trong chuyển động tròn đều, vận tốc tiếp tuyến, gia tốc và hợp lực hướng vào tâm.",
            "formulaRows": [
              {
                "label": "Gia tốc",
                "formula": "$$\na_{\\mathrm{rad}}=\\frac{v^2}{R}\n$$"
              },
              {
                "label": "Chu kỳ",
                "formula": "$$\nT=\\frac{2\\pi R}{v}\n$$"
              },
              {
                "label": "Theo chu kỳ",
                "formula": "$$\na_{\\mathrm{rad}}=\\frac{4\\pi^2R}{T^2}\n$$"
              },
              {
                "label": "Hợp lực",
                "formula": "$$\nF_{\\mathrm{net}}=\\frac{mv^2}{R}\n$$"
              }
            ],
            "variables": [
              "$R$: Bán kính (m).",
              "$T$: Chu kỳ (s)."
            ]
          },
          {
            "name": "Con lắc nón",
            "description": "Dây dài L tạo góc β với phương thẳng đứng. Quả nặng chuyển động tròn đều trong mặt phẳng ngang, 0<β<90°.",
            "formulaRows": [
              {
                "label": "Bán kính",
                "formula": "$$\nR=L\\sin\\beta\n$$"
              },
              {
                "label": "Lực căng dây",
                "formula": "$$\nF=\\frac{mg}{\\cos\\beta}\n$$"
              },
              {
                "label": "Chu kỳ",
                "formula": "$$\nT=2\\pi\\sqrt{\\frac{L\\cos\\beta}{g}}\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Ô tô trên đường cua phẳng",
            "description": "Ma sát nghỉ cung cấp gia tốc hướng tâm, không có lực đứng khác ngoài trọng lực và pháp tuyến.",
            "formulaRows": [
              {
                "label": "Tốc độ giới hạn không trượt",
                "formula": "$$\nv_{\\max}=\\sqrt{\\mu_sgR}\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Khúc cua nghiêng không cần ma sát",
            "description": "Góc β của mặt đường so với phương ngang, tại tốc độ thiết kế v và bán kính R.",
            "formulaRows": [
              {
                "label": "Góc nghiêng",
                "formula": "$$\n\\tan\\beta=\\frac{v^2}{gR}\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Vòng đu quay thẳng đứng",
            "description": "Tốc độ không đổi, ghế luôn thẳng đứng. Công thức chỉ xét ghế đỡ từ dưới tại đỉnh và đáy.",
            "formulaRows": [
              {
                "label": "Lực ghế ở đỉnh",
                "formula": "$$\nn_T=m\\left(g-\\frac{v^2}{R}\\right)\n$$"
              },
              {
                "label": "Lực ghế ở đáy",
                "formula": "$$\nn_B=m\\left(g+\\frac{v^2}{R}\\right)\n$$"
              }
            ],
            "variables": [
              "$n_T\\ge0$: Điều kiện tiếp xúc với ghế khi không có lực giữ bổ sung."
            ]
          }
        ]
      },
      {
        "id": "fundamental",
        "title": "Các tương tác cơ bản",
        "badge": "5.5",
        "items": [
          {
            "name": "Hấp dẫn",
            "description": "Lực hút giữa các khối lượng, giữ các thiên thể và góp phần tạo cấu trúc thiên văn.",
            "formulaRows": [],
            "variables": []
          },
          {
            "name": "Điện từ",
            "description": "Gồm lực điện và lực từ. Các lực tiếp xúc giữa những vật thông thường có nguồn gốc điện từ.",
            "formulaRows": [],
            "variables": []
          },
          {
            "name": "Tương tác mạnh",
            "description": "Trong bối cảnh hạt nhân, liên kết proton và neutron. Phạm vi ngắn, thắng lực đẩy điện trong các hạt nhân bền.",
            "formulaRows": [],
            "variables": []
          },
          {
            "name": "Tương tác yếu",
            "description": "Phạm vi rất ngắn. Gây ra phân rã beta và có vai trò trong định tuổi carbon phóng xạ.",
            "formulaRows": [],
            "variables": []
          }
        ]
      }
    ]
  }
}
