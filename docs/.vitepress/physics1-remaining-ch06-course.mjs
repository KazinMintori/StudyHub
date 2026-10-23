export const physics1RemainingChapter6Parent={
  "chapter": 6,
  "topics": [
    {
      "slug": "cong-co-hoc",
      "title": "Công cơ học",
      "question": "Làm thế nào để đo lường tác dụng truyền năng lượng của một lực khi làm vật dịch chuyển?",
      "source": "6.1",
      "file": "01-muc-01.md"
    },
    {
      "slug": "dong-nang-va-dinh-ly-cong-dong-nang",
      "title": "Động năng và định lý công–động năng",
      "question": "Công toàn phần tác dụng lên chất điểm làm thay đổi trạng thái chuyển động của nó như thế nào?",
      "source": "6.2",
      "file": "02-muc-02.md"
    },
    {
      "slug": "cong-va-nang-luong-voi-luc-bien-doi",
      "title": "Công và năng lượng với lực biến đổi",
      "question": "Tính công thế nào khi lực thay đổi theo tọa độ hoặc tác dụng dọc theo một quỹ đạo cong?",
      "source": "6.3",
      "file": "03-muc-03.md"
    },
    {
      "slug": "cong-suat",
      "title": "Công suất",
      "question": "Tốc độ sinh công hoặc tiêu thụ năng lượng theo thời gian được định lượng ra sao?",
      "source": "6.4",
      "file": "04-muc-04.md"
    }
  ],
  "prerequisites": [
    "vector",
    "luc",
    "tich-vo-huong",
    "dao-ham",
    "tich-phan"
  ],
  "supportingConcepts": [
    "cong-nang-luong"
  ],
  "cheatsheet": {
    "summary": "Chương 6 thiết lập nền tảng công cơ học, động năng, định lý công–động năng cho cả lực không đổi và lực biến đổi, cùng với khái niệm công suất.",
    "sections": [
      {
        "id": "work-constant-force",
        "title": "Công của lực không đổi",
        "badge": "6.1",
        "items": [
          {
            "name": "Định nghĩa công cơ học",
            "description": "Áp dụng cho lực không đổi tác dụng lên chất điểm chuyển động thẳng với độ dời xác định.",
            "formulaRows": [
              {
                "label": "Công của lực không đổi",
                "formula": "$$\nW = \\vec F \\cdot \\vec s = Fs\\cos\\phi\n$$"
              },
              {
                "label": "Theo thành phần tiếp tuyến",
                "formula": "$$\nW = F_{\\parallel}s = (F\\cos\\phi)s\n$$"
              }
            ],
            "variables": [
              "$W$: Công cơ học (J)",
              "$F$: Độ lớn lực tác dụng (N)",
              "$s$: Quãng đường dịch chuyển (m)",
              "$\\phi$: Góc hợp bởi hướng lực và hướng độ dời"
            ]
          },
          {
            "name": "Dấu và ý nghĩa của công",
            "description": "Với lực không đổi có độ lớn dương và độ dời khác không, dấu của công bằng dấu cosin góc giữa lực và độ dời.",
            "formulaRows": [
              {
                "label": "Góc giữa hai vector",
                "formula": "$$\n0\\le\\phi\\le\\pi\n$$"
              },
              {
                "label": "Công dương",
                "formula": "$$\nW>0\\iff\\cos\\phi>0\n$$"
              },
              {
                "label": "Công bằng không",
                "formula": "$$\nW=0\\iff\\cos\\phi=0\n$$"
              },
              {
                "label": "Công âm",
                "formula": "$$\nW<0\\iff\\cos\\phi<0\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Tổng công tác dụng lên chất điểm",
            "description": "Tổng công bằng tổng đại số công của các lực. Với các lực không đổi trên cùng độ dời thẳng, có thể tính bằng hợp lực.",
            "formulaRows": [
              {
                "label": "Cộng công của n lực",
                "formula": "$$\nW_{\\mathrm{tot}}=\\sum_{i=1}^{n}W_i\n$$"
              },
              {
                "label": "Công của hợp lực không đổi",
                "formula": "$$\nW_{\\mathrm{tot}}=\\vec F_{\\mathrm{net}}\\cdot\\vec s\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Đơn vị công và năng lượng",
            "description": "Trong SI, công và động năng cùng đo bằng joule.",
            "formulaRows": [
              {
                "label": "Joule",
                "formula": "$$\n1\\,\\mathrm J=1\\,\\mathrm{N\\cdot m}\n$$"
              },
              {
                "label": "Foot-pound",
                "formula": "$$\n1\\,\\mathrm{ft\\cdot lb}=1{,}356\\,\\mathrm J\n$$"
              }
            ],
            "variables": []
          }
        ]
      },
      {
        "id": "kinetic-energy-theorem",
        "title": "Động năng và định lý công–động năng",
        "badge": "6.2",
        "items": [
          {
            "name": "Động năng của chất điểm",
            "description": "Năng lượng chuyển động của chất điểm khối lượng dương, không đổi trong cơ học Newton. Động năng không âm và phụ thuộc hệ quy chiếu.",
            "formulaRows": [
              {
                "label": "Động năng",
                "formula": "$$\nK = \\frac{1}{2}mv^2\n$$"
              }
            ],
            "variables": [
              "$K$: Động năng (J)",
              "$m$: Khối lượng chất điểm (kg)",
              "$v$: Tốc độ chuyển động (m/s)"
            ]
          },
          {
            "name": "Định lý công–động năng",
            "description": "Độ biến thiên động năng của chất điểm bằng tổng công của tất cả các ngoại lực tác dụng lên nó trong hệ quy chiếu quán tính.",
            "formulaRows": [
              {
                "label": "Định lý công–động năng",
                "formula": "$$\nW_{\\mathrm{tot}} = K_2 - K_1 = \\Delta K\n$$"
              }
            ],
            "variables": []
          }
        ]
      },
      {
        "id": "varying-force-work",
        "title": "Công của lực biến đổi và chuyển động cong",
        "badge": "6.3",
        "items": [
          {
            "name": "Lực biến đổi một chiều",
            "description": "Chất điểm chuyển động thẳng dọc theo trục x từ vị trí x1 đến x2 dưới tác dụng của lực biến đổi Fx(x).",
            "formulaRows": [
              {
                "label": "Tích phân công một chiều",
                "formula": "$$\nW = \\int_{x_1}^{x_2} F_x\\,dx\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Lực đàn hồi của lò xo lý tưởng",
            "description": "Định luật Hooke trong miền biến dạng tuyến tính. Độ biến dạng x tính từ chiều dài tự nhiên. Lực ngoài kx giữ cân bằng đầu lò xo hoặc kéo, nén chậm.",
            "formulaRows": [
              {
                "label": "Lực phục hồi của lò xo",
                "formula": "$$\nF_x = -kx\n$$"
              },
              {
                "label": "Lực kéo ngoài tác dụng vào lò xo",
                "formula": "$$\nF_{\\mathrm{ext}} = kx\n$$"
              }
            ],
            "variables": [
              "$k$: Độ cứng của lò xo (N/m)",
              "$x$: Độ dãn hoặc nén của lò xo (m)"
            ]
          },
          {
            "name": "Công biến dạng lò xo",
            "description": "Công của lực ngoài khi biến dạng chậm lò xo lý tưởng. Công của lò xo lên vật chuyển động có dấu ngược lại.",
            "formulaRows": [
              {
                "label": "Kéo từ trạng thái tự nhiên (x = 0 đến X)",
                "formula": "$$\nW = \\frac{1}{2}kX^2\n$$"
              },
              {
                "label": "Biến dạng từ x1 đến x2",
                "formula": "$$\nW = \\frac{1}{2}kx_2^2 - \\frac{1}{2}kx_1^2\n$$"
              },
              {
                "label": "Công do lò xo thực hiện",
                "formula": "$$\nW_{\\mathrm{lx}}=\\frac{k}{2}(x_1^2-x_2^2)\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Công trên quỹ đạo cong ba chiều",
            "description": "Công trên một đường đi xác định là tích phân của thành phần lực theo tiếp tuyến, lấy theo chiều chuyển động.",
            "formulaRows": [
              {
                "label": "Công vi phân",
                "formula": "$$\ndW=\\vec F\\cdot d\\vec l\n$$"
              },
              {
                "label": "Tích phân đường",
                "formula": "$$\nW=\\int_{P_1}^{P_2}\\vec F\\cdot d\\vec l\n$$"
              },
              {
                "label": "Thành phần tiếp tuyến",
                "formula": "$$\nW=\\int_{P_1}^{P_2}F\\cos\\phi\\,dl\n$$"
              }
            ],
            "variables": []
          }
        ]
      },
      {
        "id": "power",
        "title": "Công suất",
        "badge": "6.4",
        "items": [
          {
            "name": "Công suất trung bình và tức thời",
            "description": "Đại lượng vô hướng đặc trưng cho tốc độ thực hiện công hoặc tốc độ truyền năng lượng theo thời gian.",
            "formulaRows": [
              {
                "label": "Công suất trung bình",
                "formula": "$$\nP_{\\mathrm{av}} = \\frac{\\Delta W}{\\Delta t}\n$$"
              },
              {
                "label": "Công suất tức thời",
                "formula": "$$\nP = \\frac{dW}{dt}\n$$"
              },
              {
                "label": "Liên hệ giữa lực và vận tốc",
                "formula": "$$\nP = \\vec F \\cdot \\vec v\n$$"
              },
              {
                "label": "Dạng thành phần tiếp tuyến",
                "formula": "$$\nP=F_{\\parallel}v\n$$"
              }
            ],
            "variables": [
              "$P$: Công suất (W)",
              "$\\Delta W$: Công thực hiện trong khoảng thời gian Delta t (J)",
              "$\\vec v$: Vector vận tốc tức thời (m/s)"
            ]
          },
          {
            "name": "Đơn vị công suất và chuyển đổi",
            "description": "Watt là đơn vị công suất, mã lực là đơn vị công suất ngoài SI. Kilowatt-giờ là đơn vị năng lượng.",
            "formulaRows": [
              {
                "label": "Định nghĩa watt",
                "formula": "$$\n1\\,\\mathrm{W} = 1\\,\\mathrm{J/s} = 1\\,\\mathrm{N\\cdot m/s}\n$$"
              },
              {
                "label": "Mã lực",
                "formula": "$$\n1\\,\\mathrm{hp} = 746\\,\\mathrm{W} = 0{,}746\\,\\mathrm{kW}\n$$"
              },
              {
                "label": "Kilowatt-giờ",
                "formula": "$$\n1\\,\\mathrm{kWh} = 3{,}60\\times 10^6\\,\\mathrm{J}\n$$"
              }
            ],
            "variables": []
          }
        ]
      }
    ]
  }
}
