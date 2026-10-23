export const physics1RemainingChapter3Parent={
  "chapter": 3,
  "topics": [
    {
      "slug": "vector-vi-tri-va-van-toc",
      "title": "Vector vị trí và vector vận tốc",
      "question": "Làm thế nào xác định vị trí và chiều chuyển động của chất điểm trong không gian?",
      "source": "3.1",
      "file": "01-muc-01.md"
    },
    {
      "slug": "vector-gia-toc",
      "title": "Vector gia tốc",
      "question": "Vì sao vật chuyển động với tốc độ không đổi trên đường cong vẫn có gia tốc?",
      "source": "3.2",
      "file": "02-muc-02.md"
    },
    {
      "slug": "chuyen-dong-nem",
      "title": "Chuyển động ném",
      "question": "Các chuyển động theo phương ngang và phương thẳng đứng độc lập với nhau thế nào?",
      "source": "3.3",
      "file": "03-muc-03.md"
    },
    {
      "slug": "chuyen-dong-tron",
      "title": "Chuyển động tròn",
      "question": "Điều gì quyết định độ lớn và phương hướng của gia tốc trong chuyển động tròn?",
      "source": "3.4",
      "file": "04-muc-04.md"
    },
    {
      "slug": "van-toc-tuong-doi",
      "title": "Vận tốc tương đối",
      "question": "Làm thế nào liên hệ kết quả đo vận tốc giữa các hệ quy chiếu chuyển động đối với nhau?",
      "source": "3.5",
      "file": "05-muc-05.md"
    }
  ],
  "prerequisites": [
    "vector",
    "thanh-phan-vector",
    "dao-ham",
    "gia-toc"
  ],
  "supportingConcepts": [
    "vector-vi-tri",
    "gia-toc-huong-tam",
    "chuyen-dong-nem",
    "van-toc-tuong-doi",
    "van-toc-vat-ly",
    "toc-do-chuyen-dong"
  ],
  "cheatsheet": {
    "summary": "Bảng tra cứu công thức cốt lõi về vector vị trí, vận tốc, gia tốc, chuyển động ném, chuyển động tròn và biến đổi vận tốc tương đối trong không gian hai và ba chiều.",
    "sections": [
      {
        "id": "vector-dong-hoc",
        "title": "Vector vị trí, vận tốc và gia tốc",
        "badge": "Cơ bản",
        "items": [
          {
            "name": "Vector vị trí",
            "description": "Định nghĩa vị trí chất điểm trong hệ tọa độ Descartes ba chiều.",
            "formulaRows": [
              {
                "label": "Vector vị trí",
                "formula": "$$\n\\vec{r} = x\\hat{i} + y\\hat{j} + z\\hat{k}\n$$"
              }
            ],
            "variables": [
              "$\\vec{r}$: Vector vị trí",
              "$x, y, z$: Tọa độ Descartes",
              "$\\hat{i}, \\hat{j}, \\hat{k}$: Vector đơn vị"
            ]
          },
          {
            "name": "Vector vận tốc trung bình và tức thời",
            "description": "Vận tốc trung bình cùng hướng với độ dời. vận tốc tức thời tiếp tuyến với quỹ đạo.",
            "formulaRows": [
              {
                "label": "Vận tốc trung bình",
                "formula": "$$\n\\vec{v}_{\\mathrm{tb}} = \\frac{\\Delta \\vec{r}}{\\Delta t}\n$$"
              },
              {
                "label": "Vận tốc tức thời",
                "formula": "$$\n\\vec{v} = \\frac{d\\vec{r}}{dt}\n$$"
              }
            ],
            "variables": [
              "$\\Delta \\vec{r}$: Vector độ dời",
              "$\\Delta t$: Khoảng thời gian",
              "$\\vec{v}$: Vận tốc tức thời"
            ]
          },
          {
            "name": "Thành phần và độ lớn vận tốc trong mặt phẳng",
            "description": "Phân tích vận tốc thành hai thành phần vuông góc $v_x$ và $v_y$.",
            "formulaRows": [
              {
                "label": "Thành phần vận tốc",
                "formula": "$$\nv_x = \\frac{dx}{dt}, \\quad v_y = \\frac{dy}{dt}\n$$"
              },
              {
                "label": "Độ lớn vận tốc",
                "formula": "$$\nv = \\sqrt{v_x^2 + v_y^2}\n$$"
              },
              {
                "label": "Hướng vận tốc",
                "formula": "$$\n\\tan\\alpha = \\frac{v_y}{v_x}\n$$"
              }
            ],
            "variables": [
              "$v$: Tốc độ tức thời",
              "$\\alpha$: Góc nghiêng so với trục +x"
            ]
          },
          {
            "name": "Vector gia tốc trung bình và tức thời",
            "description": "Gia tốc mô tả tốc độ biến thiên của vector vận tốc theo thời gian.",
            "formulaRows": [
              {
                "label": "Gia tốc trung bình",
                "formula": "$$\n\\vec{a}_{\\mathrm{tb}} = \\frac{\\Delta \\vec{v}}{\\Delta t}\n$$"
              },
              {
                "label": "Gia tốc tức thời",
                "formula": "$$\n\\vec{a} = \\frac{d\\vec{v}}{dt}\n$$"
              }
            ],
            "variables": [
              "$\\vec{a}$: Vector gia tốc tức thời",
              "$\\Delta \\vec{v}$: Độ biến thiên vận tốc"
            ]
          },
          {
            "name": "Thành phần gia tốc tiếp tuyến và pháp tuyến",
            "description": "Thành phần tiếp tuyến làm đổi tốc độ. thành phần pháp tuyến làm đổi phương chuyển động.",
            "formulaRows": [
              {
                "label": "Gia tốc tiếp tuyến",
                "formula": "$$\na_{\\parallel} = \\frac{d|\\vec{v}|}{dt}\n$$"
              },
              {
                "label": "Gia tốc pháp tuyến",
                "formula": "$$\na_{\\perp} = \\frac{v^2}{R}\n$$"
              },
              {
                "label": "Độ lớn gia tốc toàn phần",
                "formula": "$$\na = \\sqrt{a_{\\parallel}^2 + a_{\\perp}^2}\n$$"
              }
            ],
            "variables": [
              "$a_{\\parallel}$: Gia tốc tiếp tuyến",
              "$a_{\\perp}$: Gia tốc pháp tuyến",
              "$R$: Bán kính cong quỹ đạo"
            ]
          }
        ]
      },
      {
        "id": "chuyen-dong-nem",
        "title": "Chuyển động ném trong mặt phẳng",
        "badge": "Trọng tâm",
        "items": [
          {
            "name": "Phương trình chuyển động ném lý tưởng",
            "description": "Bỏ qua sức cản không khí, gia tốc ngang triệt tiêu và gia tốc đứng hướng xuống với độ lớn g.",
            "formulaRows": [
              {
                "label": "Gia tốc",
                "formula": "$$\na_x = 0, \\quad a_y = -g\n$$"
              },
              {
                "label": "Vận tốc theo thời gian",
                "formula": "$$\n\\begin{aligned} v_x &= v_0\\cos\\alpha_0 \\\\ v_y &= v_0\\sin\\alpha_0 - gt \\end{aligned}\n$$"
              },
              {
                "label": "Tọa độ theo thời gian",
                "formula": "$$\n\\begin{aligned} x &= (v_0\\cos\\alpha_0)t \\\\ y &= (v_0\\sin\\alpha_0)t - \\frac{1}{2}gt^2 \\end{aligned}\n$$"
              }
            ],
            "variables": [
              "$v_0$: Tốc độ ban đầu",
              "$\\alpha_0$: Góc ném ban đầu",
              "$g$: Gia tốc rơi tự do"
            ]
          },
          {
            "name": "Quỹ đạo parabol",
            "description": "Gốc tại điểm ném, vận tốc ngang khác không. Đặt b và c như dưới đây để viết phương trình quỹ đạo.",
            "formulaRows": [
              {
                "label": "Hệ số b",
                "formula": "$$\nb=\\tan\\alpha_0\n$$"
              },
              {
                "label": "Hệ số c",
                "formula": "$$\nc=\\frac{g}{2v_0^2\\cos^2\\alpha_0}\n$$"
              },
              {
                "label": "Quỹ đạo",
                "formula": "$$\ny=bx-cx^2\n$$"
              }
            ],
            "variables": [
              "$y(x)$: Tọa độ đứng theo tọa độ ngang"
            ]
          },
          {
            "name": "Tầm bay xa và độ cao cực đại trên mặt bằng phẳng",
            "description": "Áp dụng khi điểm rơi có cùng cao độ với điểm ném ban đầu ($y = 0$).",
            "formulaRows": [
              {
                "label": "Thời gian bay",
                "formula": "$$\nt_{\\mathrm{bay}} = \\frac{2v_0\\sin\\alpha_0}{g}\n$$"
              },
              {
                "label": "Độ cao cực đại",
                "formula": "$$\nh_{\\max} = \\frac{v_0^2\\sin^2\\alpha_0}{2g}\n$$"
              },
              {
                "label": "Tầm bay xa",
                "formula": "$$\nR = \\frac{v_0^2\\sin(2\\alpha_0)}{g}\n$$"
              }
            ],
            "variables": [
              "$h_{\\max}$: Độ cao đỉnh quỹ đạo",
              "$R$: Tầm bay xa ngang",
              "$\\alpha_0 = 45^\\circ$: Cho tầm xa cực đại"
            ]
          }
        ]
      },
      {
        "id": "chuyen-dong-tron",
        "title": "Chuyển động tròn đều và không đều",
        "badge": "Chu kỳ & Gia tốc",
        "items": [
          {
            "name": "Chuyển động tròn đều",
            "description": "Chất điểm đi trên đường tròn bán kính R với tốc độ không đổi v.",
            "formulaRows": [
              {
                "label": "Liên hệ tốc độ và chu kỳ",
                "formula": "$$\nv = \\frac{2\\pi R}{T}\n$$"
              },
              {
                "label": "Gia tốc hướng tâm theo v",
                "formula": "$$\na_{\\mathrm{rad}} = \\frac{v^2}{R}\n$$"
              },
              {
                "label": "Gia tốc hướng tâm theo T",
                "formula": "$$\na_{\\mathrm{rad}} = \\frac{4\\pi^2 R}{T^2}\n$$"
              }
            ],
            "variables": [
              "$R$: Bán kính quỹ đạo tròn",
              "$T$: Chu kỳ quay",
              "$a_{\\mathrm{rad}}$: Gia tốc hướng tâm"
            ]
          },
          {
            "name": "Chuyển động tròn không đều",
            "description": "Tốc độ thay đổi theo thời gian, gia tốc gồm cả thành phần hướng tâm và tiếp tuyến.",
            "formulaRows": [
              {
                "label": "Gia tốc tiếp tuyến",
                "formula": "$$\na_{\\mathrm{tan}} = \\frac{dv}{dt}\n$$"
              },
              {
                "label": "Gia tốc hướng tâm",
                "formula": "$$\na_{\\mathrm{rad}} = \\frac{v^2}{R}\n$$"
              },
              {
                "label": "Độ lớn gia tốc",
                "formula": "$$\na = \\sqrt{a_{\\mathrm{rad}}^2 + a_{\\mathrm{tan}}^2}\n$$"
              }
            ],
            "variables": [
              "$a_{\\mathrm{tan}}$: Gia tốc tiếp tuyến",
              "$a$: Gia tốc toàn phần"
            ]
          }
        ]
      },
      {
        "id": "van-toc-tuong-doi",
        "title": "Vận tốc tương đối (Phép biến đổi Galilei)",
        "badge": "Hệ quy chiếu",
        "items": [
          {
            "name": "Vận tốc tương đối một chiều",
            "description": "Quy tắc cộng vận tốc dọc theo một đường thẳng.",
            "formulaRows": [
              {
                "label": "Biến đổi Galilei một chiều",
                "formula": "$$\nv_{P/A}=v_{P/B}+v_{B/A}\n$$"
              }
            ],
            "variables": [
              "$v_{P/A; x}$: Vận tốc của P đối với A",
              "$v_{P/B; x}$: Vận tốc của P đối với B",
              "$v_{B/A; x}$: Vận tốc của B đối với A"
            ]
          },
          {
            "name": "Vận tốc tương đối trong không gian hai và ba chiều",
            "description": "Quy tắc cộng vector vận tốc giữa các hệ quy chiếu chuyển động tịnh tiến.",
            "formulaRows": [
              {
                "label": "Biến đổi Galilei dạng vector",
                "formula": "$$\n\\vec{v}_{P/A} = \\vec{v}_{P/B} + \\vec{v}_{B/A}\n$$"
              },
              {
                "label": "Hệ thức đảo chiều hệ quy chiếu",
                "formula": "$$\n\\vec{v}_{A/B} = -\\vec{v}_{B/A}\n$$"
              }
            ],
            "variables": [
              "$\\vec{v}_{P/A}$: Vector vận tốc của P đối với A",
              "$\\vec{v}_{P/B}$: Vector vận tốc của P đối với B",
              "$\\vec{v}_{B/A}$: Vector vận tốc của B đối với A"
            ]
          }
        ]
      }
    ]
  }
}
