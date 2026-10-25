export const physics1RemainingChapter14Parent={
  "chapter": 14,
  "topics": [
    {
      "slug": "mo-ta-dao-dong",
      "title": "Mô tả dao động",
      "question": "Biên độ, chu kỳ và tần số mô tả một dao động như thế nào?",
      "source": "14.1",
      "file": "01-muc-01.md"
    },
    {
      "slug": "dao-dong-dieu-hoa",
      "title": "Dao động điều hòa",
      "question": "Lực phục hồi tuyến tính xác định li độ, vận tốc và gia tốc ra sao?",
      "source": "14.2",
      "file": "02-muc-02.md"
    },
    {
      "slug": "co-nang-dao-dong-dieu-hoa",
      "title": "Cơ năng trong dao động điều hòa",
      "question": "Cơ năng và li độ liên hệ với tốc độ, biên độ như thế nào?",
      "source": "14.3",
      "file": "03-muc-03.md"
    },
    {
      "slug": "ung-dung-dao-dong-dieu-hoa",
      "title": "Các ứng dụng của dao động điều hòa",
      "question": "Lò xo đứng, dao động xoắn và tương tác phân tử cùng dẫn tới mô hình điều hòa ra sao?",
      "source": "14.4",
      "file": "04-muc-04.md"
    },
    {
      "slug": "con-lac-don",
      "title": "Con lắc đơn",
      "question": "Khi nào con lắc đơn gần điều hòa và chu kỳ thay đổi theo biên độ thế nào?",
      "source": "14.5",
      "file": "05-muc-05.md"
    },
    {
      "slug": "con-lac-vat-ly",
      "title": "Con lắc vật lý",
      "question": "Phân bố khối lượng và trục treo quyết định chu kỳ của vật quay ra sao?",
      "source": "14.6",
      "file": "06-muc-06.md"
    },
    {
      "slug": "dao-dong-tat-dan",
      "title": "Dao động tắt dần",
      "question": "Lực cản làm giảm cơ năng và phân chia các chế độ chuyển động thế nào?",
      "source": "14.7",
      "file": "07-muc-07.md"
    },
    {
      "slug": "dao-dong-cuong-buc-va-cong-huong",
      "title": "Dao động cưỡng bức và cộng hưởng",
      "question": "Ngoại lực tuần hoàn và độ cản quyết định biên độ đáp ứng ra sao?",
      "source": "14.8",
      "file": "08-muc-08.md"
    }
  ],
  "prerequisites": [
    "luc",
    "cong-nang-luong",
    "bao-toan-co-nang",
    "gia-toc-huong-tam",
    "momen-luc",
    "momen-quan-tinh",
    "dao-ham",
    "dong-luong-vat-ly"
  ],
  "supportingConcepts": [
    "dao-dong-dieu-hoa",
    "dao-dong-tat-dan",
    "cong-huong-co-hoc",
    "can-bang-co-hoc",
    "luc-can-tuyen-tinh",
    "khoi-luong-rut-gon",
    "chu-ky-va-tan-so-dao-dong",
    "tan-so-goc-dao-dong",
    "pha-dao-dong-co-hoc",
    "dao-dong-dieu-hoa-goc",
    "con-lac-don",
    "con-lac-vat-ly",
    "dao-dong-cuong-buc",
    "tat-dan-toi-han"
  ],
  "cheatsheet": {
    "summary": "Định nghĩa, tính chất, công thức và điều kiện của dao động điều hòa, các con lắc, tắt dần và cộng hưởng.",
    "sections": [
      {
        "id": "periodic-description",
        "title": "Mô tả dao động",
        "badge": "14.1",
        "items": [
          {
            "name": "Chuyển động tuần hoàn",
            "description": "Chuyển động lặp lại sau chu kỳ $T$. Các hệ dao động phục hồi đang xét có cân bằng bền và chuyển động qua lại quanh vị trí cân bằng.",
            "formulaRows": [
              {
                "label": "Chu kỳ và tần số",
                "formula": "$$\nf=\\frac1T,\\qquad T=\\frac1f\n$$"
              }
            ],
            "variables": [
              "$T>0$: Chu kỳ, đơn vị s",
              "$f>0$: Tần số, đơn vị Hz"
            ]
          },
          {
            "name": "Tần số góc",
            "description": "Tần số góc bằng hai pi lần tần số, có đơn vị rad/s. Tần số có đơn vị Hz.",
            "formulaRows": [
              {
                "label": "Quan hệ",
                "formula": "$$\n\\omega=2\\pi f=\\frac{2\\pi}{T}\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Biên độ",
            "description": "Biên độ $A$ là độ lớn li độ cực đại. Trong dao động qua lại đối xứng, hành trình giữa hai biên dài $2A$ và mất nửa chu kỳ.",
            "formulaRows": [
              {
                "label": "Giới hạn li độ",
                "formula": "$$\n|x|\\le A\n$$"
              }
            ],
            "variables": []
          }
        ]
      },
      {
        "id": "simple-harmonic",
        "title": "Dao động điều hòa",
        "badge": "14.2",
        "items": [
          {
            "name": "Lực phục hồi tuyến tính",
            "description": "Hợp lực theo trục dao động bằng $-kx$, với $m>0$, $k>0$ và không có tiêu tán.",
            "formulaRows": [
              {
                "label": "Lực",
                "formula": "$$\nF_x=-kx\n$$"
              },
              {
                "label": "Gia tốc",
                "formula": "$$\na_x=-\\frac kmx=-\\omega^2x\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Tần số của lò xo–vật",
            "description": "Lò xo lý tưởng có khối lượng bỏ qua. Với cùng $m,k$, tần số và chu kỳ không phụ thuộc biên độ.",
            "formulaRows": [
              {
                "label": "Tần số góc",
                "formula": "$$\n\\omega=\\sqrt{\\frac km}\n$$"
              },
              {
                "label": "Tần số",
                "formula": "$$\nf=\\frac1{2\\pi}\\sqrt{\\frac km}\n$$"
              },
              {
                "label": "Chu kỳ",
                "formula": "$$\nT=2\\pi\\sqrt{\\frac mk}\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Li độ và pha",
            "description": "Biên độ $A$ và pha ban đầu $\\phi$ do điều kiện đầu xác định. Pha tại thời điểm $t$ là $\\omega t+\\phi$.",
            "formulaRows": [
              {
                "label": "Li độ",
                "formula": "$$\nx=A\\cos(\\omega t+\\phi)\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Vận tốc và gia tốc",
            "description": "Vận tốc và gia tốc là các đạo hàm theo thời gian của li độ.",
            "formulaRows": [
              {
                "label": "Vận tốc",
                "formula": "$$\nv_x=-\\omega A\\sin(\\omega t+\\phi)\n$$"
              },
              {
                "label": "Gia tốc",
                "formula": "$$\na_x=-\\omega^2A\\cos(\\omega t+\\phi)\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Điều kiện đầu",
            "description": "Ký hiệu $x_0,v_0$ lần lượt là li độ và thành phần vận tốc tại thời điểm không. Biên độ không âm.",
            "formulaRows": [
              {
                "label": "Vị trí đầu",
                "formula": "$$\nx_0=A\\cos\\phi\n$$"
              },
              {
                "label": "Vận tốc đầu",
                "formula": "$$\nv_0=-\\omega A\\sin\\phi\n$$"
              },
              {
                "label": "Biên độ",
                "formula": "$$\nA=\\sqrt{x_0^2+\\frac{v_0^2}{\\omega^2}}\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Pha theo góc phần tư",
            "description": "Với $A>0$, pha phù hợp cả vị trí và vận tốc đầu. Các pha khác nhau bởi bội nguyên của $2\\pi$ tương đương. Khi $A=0$, pha không có giá trị vật lý duy nhất.",
            "formulaRows": [
              {
                "label": "Pha đầu",
                "formula": "$$\n\\phi=\\operatorname{atan2}(-v_0/\\omega,x_0)\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Các độ lớn cực đại",
            "description": "Tốc độ và độ lớn gia tốc đạt cực đại lần lượt tại cân bằng và tại hai biên của dao động điều hòa không cản.",
            "formulaRows": [
              {
                "label": "Tốc độ lớn nhất",
                "formula": "$$\nv_{\\max}=\\omega A\n$$"
              },
              {
                "label": "Gia tốc lớn nhất",
                "formula": "$$\n|a_x|_{\\max}=\\omega^2A\n$$"
              }
            ],
            "variables": []
          }
        ]
      },
      {
        "id": "oscillation-energy",
        "title": "Cơ năng dao động điều hòa",
        "badge": "14.3",
        "items": [
          {
            "name": "Cơ năng bảo toàn",
            "description": "Lò xo lý tưởng, không có công của lực tiêu tán, với mốc thế năng tại cân bằng.",
            "formulaRows": [
              {
                "label": "Tổng năng lượng",
                "formula": "$$\nE=\\frac12mv_x^2+\\frac12kx^2\n$$"
              },
              {
                "label": "Theo biên độ",
                "formula": "$$\nE=\\frac12kA^2\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Năng lượng theo li độ",
            "description": "Ký hiệu $K,U$ lần lượt là động năng và thế năng đàn hồi. Miền chuyển động là $|x|\\le A$.",
            "formulaRows": [
              {
                "label": "Thế năng",
                "formula": "$$\nU=\\frac12kx^2\n$$"
              },
              {
                "label": "Động năng",
                "formula": "$$\nK=\\frac12k(A^2-x^2)\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Vận tốc theo li độ",
            "description": "Dấu của vận tốc phụ thuộc chiều chuyển động tại li độ đang xét.",
            "formulaRows": [
              {
                "label": "Hai nhánh vận tốc",
                "formula": "$$\nv_x=\\pm\\omega\\sqrt{A^2-x^2}\n$$"
              }
            ],
            "variables": []
          }
        ]
      },
      {
        "id": "shm-applications",
        "title": "Các mô hình điều hòa",
        "badge": "14.4",
        "items": [
          {
            "name": "Lò xo thẳng đứng",
            "description": "Li độ $x$ đo từ vị trí cân bằng có trọng lực. Độ dãn tĩnh là $\\Delta l$. Trọng lực dịch vị trí cân bằng nhưng không đổi tần số khi $m,k$ giữ nguyên.",
            "formulaRows": [
              {
                "label": "Cân bằng tĩnh",
                "formula": "$$\nk\\Delta l=mg\n$$"
              },
              {
                "label": "Tần số góc",
                "formula": "$$\n\\omega=\\sqrt{\\frac km}\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Dao động xoắn",
            "description": "Góc tính bằng radian, $\\kappa>0$ là hằng số xoắn và $I$ là mômen quán tính quanh trục dao động.",
            "formulaRows": [
              {
                "label": "Mômen phục hồi",
                "formula": "$$\n\\tau_z=-\\kappa\\theta\n$$"
              },
              {
                "label": "Tần số góc",
                "formula": "$$\n\\omega=\\sqrt{\\frac\\kappa I}\n$$"
              },
              {
                "label": "Chu kỳ",
                "formula": "$$\nT=2\\pi\\sqrt{\\frac I\\kappa}\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Thế năng tương tác phân tử",
            "description": "Mô hình van der Waals có $U_0>0$, khoảng cách cân bằng $R_0$. Biến $u$ là tỷ số khoảng cách không thứ nguyên.",
            "formulaRows": [
              {
                "label": "Biến không thứ nguyên",
                "formula": "$$\nu=\\frac{R_0}{r}\n$$"
              },
              {
                "label": "Thế năng",
                "formula": "$$\nU=U_0(u^{12}-2u^6)\n$$"
              },
              {
                "label": "Lực bán kính",
                "formula": "$$\nF_r=\\frac{12U_0}{R_0}(u^{13}-u^7)\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Dao động nhỏ của phân tử",
            "description": "Độ lệch $x=r-R_0$ thỏa $|x|\\ll R_0$. Độ cứng hiệu dụng là độ cong thế năng tại cân bằng. Khi cả hai hạt tự do, tần số tương đối dùng khối lượng rút gọn $\\mu$.",
            "formulaRows": [
              {
                "label": "Lực tuyến tính",
                "formula": "$$\nF_r\\approx-k_{\\mathrm{eff}}x\n$$"
              },
              {
                "label": "Độ cứng hiệu dụng",
                "formula": "$$\nk_{\\mathrm{eff}}=\\frac{72U_0}{R_0^2}\n$$"
              },
              {
                "label": "Khối lượng rút gọn",
                "formula": "$$\n\\mu=\\frac{m_1m_2}{m_1+m_2}\n$$"
              },
              {
                "label": "Tần số góc tương đối",
                "formula": "$$\n\\omega=\\sqrt{\\frac{k_{\\mathrm{eff}}}{\\mu}}\n$$"
              }
            ],
            "variables": []
          }
        ]
      },
      {
        "id": "simple-pendulum",
        "title": "Con lắc đơn",
        "badge": "14.5",
        "items": [
          {
            "name": "Lực tiếp tuyến",
            "description": "Chất điểm treo bằng dây không khối lượng, không dãn, dài $L$. Dây còn căng và góc $\\theta$ đo từ phương thẳng đứng xuống.",
            "formulaRows": [
              {
                "label": "Tọa độ dọc cung",
                "formula": "$$\nx=L\\theta\n$$"
              },
              {
                "label": "Lực chính xác",
                "formula": "$$\nF_\\theta=-mg\\sin\\theta\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Giới hạn góc nhỏ",
            "description": "Với góc nhỏ tính bằng radian, $\\sin\\theta\\approx\\theta$ và chuyển động gần điều hòa.",
            "formulaRows": [
              {
                "label": "Lực tuyến tính",
                "formula": "$$\nF_\\theta\\approx-\\frac{mg}{L}x\n$$"
              },
              {
                "label": "Tần số góc",
                "formula": "$$\n\\omega=\\sqrt{\\frac gL}\n$$"
              },
              {
                "label": "Chu kỳ",
                "formula": "$$\nT_0=2\\pi\\sqrt{\\frac Lg}\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Hiệu chỉnh biên độ hữu hạn",
            "description": "Biên độ góc thỏa $0\\le\\Theta<\\pi$. Ký hiệu $T_0$ là chu kỳ góc nhỏ. Chuỗi dưới đây biểu diễn chu kỳ với hai hệ số hiệu chỉnh đầu.",
            "formulaRows": [
              {
                "label": "Biến biên độ",
                "formula": "$$\nq=\\sin\\frac\\Theta2\n$$"
              },
              {
                "label": "Hệ số thứ nhất",
                "formula": "$$\nc_1=\\frac{1^2}{2^2}=\\frac14\n$$"
              },
              {
                "label": "Hệ số thứ hai",
                "formula": "$$\nc_2=\\frac{1^2\\cdot3^2}{2^2\\cdot4^2}=\\frac9{64}\n$$"
              },
              {
                "label": "Chu kỳ hữu hạn",
                "formula": "$$\n\\frac{T}{T_0}=1+c_1q^2+c_2q^4+\\cdots\n$$"
              }
            ],
            "variables": []
          }
        ]
      },
      {
        "id": "physical-pendulum",
        "title": "Con lắc vật lý",
        "badge": "14.6",
        "items": [
          {
            "name": "Mômen phục hồi",
            "description": "Vật rắn quay quanh trục không ma sát. Ở cân bằng bền, trọng tâm ở dưới trục một đoạn $d>0$. Mômen quán tính $I$ lấy quanh trục treo.",
            "formulaRows": [
              {
                "label": "Mômen",
                "formula": "$$\n\\tau_z=-mgd\\sin\\theta\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Dao động góc nhỏ",
            "description": "Góc nhỏ tính bằng radian, trường trọng lực gần đều và mômen quán tính quanh trục không đổi.",
            "formulaRows": [
              {
                "label": "Tần số góc",
                "formula": "$$\n\\omega=\\sqrt{\\frac{mgd}{I}}\n$$"
              },
              {
                "label": "Chu kỳ",
                "formula": "$$\nT=2\\pi\\sqrt{\\frac{I}{mgd}}\n$$"
              },
              {
                "label": "Mômen từ chu kỳ",
                "formula": "$$\nI=mgd\\left(\\frac{T}{2\\pi}\\right)^2\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Thanh đồng nhất treo đầu",
            "description": "Thanh dài $L$, khối lượng $m$, dao động góc nhỏ quanh trục qua đầu, vuông góc thanh.",
            "formulaRows": [
              {
                "label": "Mômen quán tính",
                "formula": "$$\nI=\\frac13mL^2\n$$"
              },
              {
                "label": "Khoảng cách trọng tâm",
                "formula": "$$\nd=\\frac L2\n$$"
              },
              {
                "label": "Chu kỳ",
                "formula": "$$\nT=2\\pi\\sqrt{\\frac{2L}{3g}}\n$$"
              }
            ],
            "variables": []
          }
        ]
      },
      {
        "id": "damped-motion",
        "title": "Tắt dần do lực cản tuyến tính",
        "badge": "14.7",
        "items": [
          {
            "name": "Phương trình có cản",
            "description": "Khối lượng và độ cứng dương, hệ số cản không âm. Lực cản tuyến tính ngược chiều vận tốc.",
            "formulaRows": [
              {
                "label": "Lực cản",
                "formula": "$$\nF_d=-bv_x\n$$"
              },
              {
                "label": "Phương trình",
                "formula": "$$\nm\\ddot x+b\\dot x+kx=0\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Dưới tới hạn",
            "description": "Hệ số cản thỏa $0<b<2\\sqrt{km}$. Đặt $\\omega_0=\\sqrt{k/m}$. Các hằng số $A,\\phi$ do điều kiện đầu xác định.",
            "formulaRows": [
              {
                "label": "Hệ số suy giảm",
                "formula": "$$\n\\beta=\\frac{b}{2m}\n$$"
              },
              {
                "label": "Li độ",
                "formula": "$$\nx=Ae^{-\\beta t}\\cos(\\omega't+\\phi)\n$$"
              },
              {
                "label": "Tần số góc có cản",
                "formula": "$$\n\\omega'=\\sqrt{\\omega_0^2-\\beta^2}\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Tới hạn và quá tới hạn",
            "description": "Tới hạn khi $b=b_c$, quá tới hạn khi $b>b_c$. Vật bị lệch rồi thả từ nghỉ trở về mà không dao động qua lại trong hai chế độ này.",
            "formulaRows": [
              {
                "label": "Ngưỡng tới hạn",
                "formula": "$$\nb_c=2\\sqrt{km}\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Mất cơ năng",
            "description": "Tốc độ biến thiên cơ năng bằng công suất lực cản và không dương. Cơ năng tức thời không giảm với tốc độ đều.",
            "formulaRows": [
              {
                "label": "Công suất cản",
                "formula": "$$\n\\frac{dE}{dt}=-bv_x^2\\le0\n$$"
              }
            ],
            "variables": []
          }
        ]
      },
      {
        "id": "forced-resonance",
        "title": "Dao động cưỡng bức và cộng hưởng",
        "badge": "14.8",
        "items": [
          {
            "name": "Ngoại lực và đáp ứng",
            "description": "Ngoại lực hình sin tác dụng lên hệ tuyến tính có $b>0$. Sau khi quá độ tắt, tần số góc đáp ứng bằng $\\omega_d$.",
            "formulaRows": [
              {
                "label": "Lực cưỡng bức",
                "formula": "$$\nF(t)=F_{\\max}\\cos\\omega_dt\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Biên độ ổn định",
            "description": "Công thức cho trạng thái ổn định của hệ tuyến tính có cản, với biên độ lực $F_{\\max}$ và tần số góc cưỡng bức $\\omega_d$.",
            "formulaRows": [
              {
                "label": "Độ lệch động lực",
                "formula": "$$\n\\delta=k-m\\omega_d^2\n$$"
              },
              {
                "label": "Biên độ",
                "formula": "$$\nA=\\frac{F_{\\max}}{\\sqrt{\\delta^2+b^2\\omega_d^2}}\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Đỉnh biên độ li độ",
            "description": "Đỉnh tại tần số dương chỉ tồn tại khi $b<\\sqrt{2km}$. Tần số đỉnh gần tần số riêng không cản khi cản yếu.",
            "formulaRows": [
              {
                "label": "Tần số đỉnh",
                "formula": "$$\n\\omega_r=\\sqrt{\\frac km-\\frac{b^2}{2m^2}}\n$$"
              },
              {
                "label": "Điều kiện có đỉnh dương",
                "formula": "$$\nb<\\sqrt{2km}\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Tại tần số riêng và tại không",
            "description": "Đặt $\\omega_0=\\sqrt{k/m}$. Tại tần số cưỡng bức không, lực là hằng số và đáp ứng cuối là độ lệch cân bằng tĩnh.",
            "formulaRows": [
              {
                "label": "Tại tần số riêng không cản",
                "formula": "$$\nA(\\omega_0)=\\frac{F_{\\max}}{b\\omega_0}\n$$"
              },
              {
                "label": "Giới hạn tĩnh",
                "formula": "$$\nA(0)=\\frac{F_{\\max}}k\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "So sánh độ cản",
            "description": "Với cùng biên độ lực, khối lượng, độ cứng và tần số cưỡng bức dương, ít cản hơn cho biên độ lớn hơn. Tại tần số không, các biên độ bằng nhau. Hệ không cản được kích thích đúng tần số riêng không có biên độ ổn định hữu hạn.",
            "formulaRows": [],
            "variables": []
          }
        ]
      }
    ]
  },
  "topicReferences": {
    "14.5": [
      {
        "title": "BIPM: Lịch sử định nghĩa giây",
        "url": "https://www.bipm.org/en/history-si/second"
      }
    ],
    "14.8": [
      {
        "title": "Cornell University College of Veterinary Medicine: Cơ chế thải nhiệt ở chó",
        "url": "https://www.vet.cornell.edu/departments-centers-and-institutes/riney-canine-health-center/canine-health-topics/summer-heat-safety-tips-dogs"
      }
    ]
  }
}
