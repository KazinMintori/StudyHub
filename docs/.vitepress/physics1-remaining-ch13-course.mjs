export const physics1RemainingChapter13Parent={
  "chapter": 13,
  "topics": [
    {
      "slug": "dinh-luat-van-vat-hap-dan",
      "title": "Định luật vạn vật hấp dẫn Newton",
      "question": "Hai vật có khối lượng hút nhau như thế nào và lực tổng hợp được tính ra sao?",
      "source": "13.1",
      "file": "01-muc-01.md"
    },
    {
      "slug": "trong-luong",
      "title": "Trọng lượng",
      "question": "Trọng lượng và gia tốc trọng trường thay đổi theo thiên thể và độ cao như thế nào?",
      "source": "13.2",
      "file": "02-muc-02.md"
    },
    {
      "slug": "the-nang-hap-dan",
      "title": "Thế năng hấp dẫn",
      "question": "Tính công, cơ năng và tốc độ thoát thế nào khi lực hấp dẫn thay đổi theo khoảng cách?",
      "source": "13.3",
      "file": "03-muc-03.md"
    },
    {
      "slug": "chuyen-dong-ve-tinh",
      "title": "Chuyển động vệ tinh",
      "question": "Lực hấp dẫn xác định tốc độ, chu kỳ và cơ năng của vệ tinh trên quỹ đạo tròn ra sao?",
      "source": "13.4",
      "file": "04-muc-04.md"
    },
    {
      "slug": "cac-dinh-luat-kepler-va-chuyen-dong-hanh-tinh",
      "title": "Các định luật Kepler và chuyển động hành tinh",
      "question": "Hình học quỹ đạo, diện tích quét và chu kỳ liên hệ với các định luật Newton như thế nào?",
      "source": "13.5",
      "file": "05-muc-05.md"
    },
    {
      "slug": "phan-bo-khoi-luong-doi-xung-cau",
      "title": "Phân bố khối lượng đối xứng cầu",
      "question": "Vì sao vật đối xứng cầu có thể được thay bằng khối lượng ở tâm, và điều gì xảy ra bên trong vỏ cầu?",
      "source": "13.6",
      "file": "06-muc-06.md"
    },
    {
      "slug": "trong-luong-bieu-kien-va-su-quay-trai-dat",
      "title": "Trọng lượng biểu kiến và sự quay của Trái Đất",
      "question": "Vì sao số chỉ của cân khác lực hấp dẫn thật khi vật cùng quay với Trái Đất?",
      "source": "13.7",
      "file": "07-muc-07.md"
    },
    {
      "slug": "ho-den",
      "title": "Hố đen",
      "question": "Chân trời sự kiện có ý nghĩa gì và làm thế nào nhận biết hố đen qua chuyển động của vật lân cận?",
      "source": "13.8",
      "file": "08-muc-08.md"
    }
  ],
  "prerequisites": [
    "luc",
    "cong-nang-luong",
    "vector",
    "gia-toc-huong-tam",
    "momen-luc",
    "momen-dong-luong",
    "khoi-tam",
    "dao-ham",
    "tich-phan"
  ],
  "supportingConcepts": [
    "dinh-luat-van-vat-hap-dan",
    "the-nang-hap-dan",
    "toc-do-thoat",
    "quy-dao-ve-tinh",
    "dinh-luat-kepler",
    "luc-xuyen-tam",
    "dinh-ly-vo-cau",
    "trong-luong-bieu-kien",
    "ban-kinh-schwarzschild",
    "chan-troi-su-kien",
    "ho-den"
  ],
  "cheatsheet": {
    "summary": "Định nghĩa, tính chất, công thức và điều kiện của lực hấp dẫn, trọng lượng, thế năng, quỹ đạo, phân bố đối xứng cầu và hố đen.",
    "sections": [
      {
        "id": "newton-gravitation",
        "title": "Lực hấp dẫn",
        "badge": "13.1",
        "items": [
          {
            "name": "Định luật vạn vật hấp dẫn",
            "description": "Hai chất điểm có khối lượng dương hút nhau theo đường nối chúng. Với hai phân bố đối xứng cầu không chồng lấn, r là khoảng cách giữa hai tâm.",
            "formulaRows": [
              {
                "label": "Độ lớn lực",
                "formula": "$$\nF_g=\\frac{Gm_1m_2}{r^2}\n$$"
              }
            ],
            "variables": [
              "$m_1,m_2$: Khối lượng, đơn vị kg",
              "$r>0$: Khoảng cách, đơn vị m",
              "$G$: Hằng số hấp dẫn"
            ]
          },
          {
            "name": "Cặp lực trực đối",
            "description": "Hai lực đặt lên hai vật khác nhau, bằng nhau về độ lớn và ngược chiều.",
            "formulaRows": [
              {
                "label": "Định luật III Newton",
                "formula": "$$\n\\vec F_{1\\to2}=-\\vec F_{2\\to1}\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Chồng chất",
            "description": "Lực tổng hợp là tổng vector từng lực. Viết tường minh cho ba vật gây lực.",
            "formulaRows": [
              {
                "label": "Ba lực thành phần",
                "formula": "$$\n\\vec F=\\vec F_1+\\vec F_2+\\vec F_3\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Hằng số hấp dẫn",
            "description": "G không phải gia tốc trọng trường g. Giá trị dùng trong các phép tính là xấp xỉ ba chữ số có nghĩa.",
            "formulaRows": [
              {
                "label": "Giá trị theo SI",
                "formula": "$$\nG\\approx6{,}67\\times10^{-11}\\,\\mathrm{m^3/(kg\\,s^2)}\n$$"
              }
            ],
            "variables": []
          }
        ]
      },
      {
        "id": "weight",
        "title": "Trọng lượng và gia tốc trọng trường",
        "badge": "13.2",
        "items": [
          {
            "name": "Trọng lượng",
            "description": "Trọng lượng là tổng lực hấp dẫn tác dụng lên vật. Gần một thiên thể, dùng lực hút của thiên thể đó khi các ảnh hưởng khác không đáng kể.",
            "formulaRows": [
              {
                "label": "Độ lớn gần mặt thiên thể",
                "formula": "$$\nw=mg\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Ngoài thiên thể đối xứng cầu",
            "description": "Thiên thể trung tâm có khối lượng M. r đo từ tâm và nằm ngoài vật. g là độ lớn gia tốc hấp dẫn do thiên thể đó.",
            "formulaRows": [
              {
                "label": "Trọng lượng",
                "formula": "$$\nw=\\frac{GMm}{r^2}\n$$"
              },
              {
                "label": "Gia tốc trọng trường",
                "formula": "$$\ng=\\frac{GM}{r^2}\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Tại bề mặt",
            "description": "Thiên thể đối xứng cầu có bán kính R.",
            "formulaRows": [
              {
                "label": "Gia tốc bề mặt",
                "formula": "$$\ng_0=\\frac{GM}{R^2}\n$$"
              },
              {
                "label": "Khối lượng thiên thể",
                "formula": "$$\nM=\\frac{g_0R^2}{G}\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Theo độ cao",
            "description": "Vị trí nằm ở độ cao h trên bề mặt, nên r=R+h. Khối lượng của vật thử không thay đổi.",
            "formulaRows": [
              {
                "label": "Gia tốc ở độ cao h",
                "formula": "$$\ng(h)=\\frac{GM}{(R+h)^2}\n$$"
              },
              {
                "label": "Tỉ số trọng lượng",
                "formula": "$$\n\\frac{w(h)}{w(0)}=\\left(\\frac R{R+h}\\right)^2\n$$"
              }
            ],
            "variables": []
          }
        ]
      },
      {
        "id": "gravitational-potential",
        "title": "Thế năng và tốc độ thoát",
        "badge": "13.3",
        "items": [
          {
            "name": "Thành phần lực bán kính",
            "description": "Chiều dương bán kính hướng ra ngoài thiên thể đối xứng cầu.",
            "formulaRows": [
              {
                "label": "Lực có dấu",
                "formula": "$$\nF_r=-\\frac{GMm}{r^2}\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Thế năng hấp dẫn",
            "description": "Thế năng của hệ hai vật, với mốc bằng không ở vô cực. Công thức dùng cho chất điểm hoặc tương tác bên ngoài phù hợp của phân bố đối xứng cầu.",
            "formulaRows": [
              {
                "label": "Thế năng",
                "formula": "$$\nU=-\\frac{GMm}{r}\n$$"
              },
              {
                "label": "Công của lực hấp dẫn",
                "formula": "$$\nW_g=U_1-U_2\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Công theo hai khoảng cách",
            "description": "Hai trạng thái nằm ngoài thiên thể. Công hấp dẫn không phụ thuộc đường đi.",
            "formulaRows": [
              {
                "label": "Công từ r1 tới r2",
                "formula": "$$\nW_g=GMm\\left(\\frac1{r_2}-\\frac1{r_1}\\right)\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Bảo toàn cơ năng",
            "description": "Động năng K của vật được phóng được tính trong hệ thiên thể trung tâm đứng yên. Vật nhẹ hơn nhiều thiên thể. Chỉ lực hấp dẫn thực hiện công trong mô hình đang xét.",
            "formulaRows": [
              {
                "label": "Cơ năng",
                "formula": "$$\nE=K+U\n$$"
              },
              {
                "label": "Giữa hai trạng thái",
                "formula": "$$\nK_1+U_1=K_2+U_2\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Xấp xỉ gần mặt đất",
            "description": "Độ cao thay đổi nhỏ so với bán kính thiên thể và g có thể coi không đổi. Mốc cộng của thế năng được chọn phù hợp.",
            "formulaRows": [
              {
                "label": "Thế năng gần mặt đất",
                "formula": "$$\nU=mgy\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Tốc độ thoát",
            "description": "Coi thiên thể trung tâm đứng yên và vật được phóng có khối lượng nhỏ hơn nhiều khối lượng thiên thể. Tốc độ nhỏ nhất để ra xa vô hạn với tốc độ cuối bằng không. Bỏ qua lực cản, các vật khác và năng lượng được cấp thêm trên đường đi.",
            "formulaRows": [
              {
                "label": "Tại khoảng cách r",
                "formula": "$$\nv_{\\mathrm{esc}}=\\sqrt{\\frac{2GM}{r}}\n$$"
              },
              {
                "label": "Từ bề mặt",
                "formula": "$$\nv_{\\mathrm{esc}}=\\sqrt{2g_0R}\n$$"
              }
            ],
            "variables": []
          }
        ]
      },
      {
        "id": "circular-orbit",
        "title": "Quỹ đạo tròn",
        "badge": "13.4",
        "items": [
          {
            "name": "Tốc độ và gia tốc",
            "description": "Chỉ lực hút của thiên thể khối lượng M chi phối chuyển động. Vật trung tâm được coi đứng yên và quỹ đạo có bán kính r.",
            "formulaRows": [
              {
                "label": "Tốc độ tròn",
                "formula": "$$\nv=\\sqrt{\\frac{GM}{r}}\n$$"
              },
              {
                "label": "Gia tốc hướng tâm",
                "formula": "$$\na_r=\\frac{v^2}{r}=\\frac{GM}{r^2}\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Chu kỳ",
            "description": "T là thời gian đi hết một vòng trên quỹ đạo tròn.",
            "formulaRows": [
              {
                "label": "Chu kỳ từ tốc độ",
                "formula": "$$\nT=\\frac{2\\pi r}{v}\n$$"
              },
              {
                "label": "Chu kỳ theo bán kính",
                "formula": "$$\nT=2\\pi\\sqrt{\\frac{r^3}{GM}}\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Năng lượng quỹ đạo tròn",
            "description": "Thế năng dùng mốc vô cực. Các quan hệ K,U,E dưới đây dành riêng cho quỹ đạo tròn.",
            "formulaRows": [
              {
                "label": "Động năng",
                "formula": "$$\nK=\\frac{GMm}{2r}\n$$"
              },
              {
                "label": "Thế năng",
                "formula": "$$\nU=-\\frac{GMm}{r}\n$$"
              },
              {
                "label": "Cơ năng",
                "formula": "$$\nE=-\\frac{GMm}{2r}\n$$"
              },
              {
                "label": "Quan hệ năng lượng",
                "formula": "$$\nK=-E,\\qquad U=2E\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Tốc độ thoát và tốc độ tròn",
            "description": "Coi thiên thể trung tâm đứng yên và vật được phóng có khối lượng nhỏ hơn nhiều khối lượng thiên thể. So sánh tại cùng khoảng cách r quanh cùng thiên thể.",
            "formulaRows": [
              {
                "label": "Tỉ số",
                "formula": "$$\nv_{\\mathrm{esc}}=\\sqrt2\\,v_{\\mathrm{circ}}\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Không trọng lượng biểu kiến",
            "description": "Khi người và tàu cùng rơi tự do chỉ dưới tác dụng hấp dẫn, không cần lực từ sàn để giữ người đứng yên tương đối với tàu. Lực hấp dẫn vẫn có thể rất lớn.",
            "formulaRows": [],
            "variables": []
          }
        ]
      },
      {
        "id": "kepler",
        "title": "Các định luật Kepler",
        "badge": "13.5",
        "items": [
          {
            "name": "Ellipse và độ lệch tâm",
            "description": "Mặt Trời nằm tại một tiêu điểm. a là bán trục lớn, e là độ lệch tâm. e=0 cho đường tròn, 0<e<1 cho ellipse không tròn.",
            "formulaRows": [
              {
                "label": "Miền độ lệch tâm",
                "formula": "$$\n0\\le e<1\n$$"
              },
              {
                "label": "Tổng khoảng cách tới tiêu điểm",
                "formula": "$$\nSP+S'P=2a\n$$"
              },
              {
                "label": "Khoảng cận nhật",
                "formula": "$$\nr_{\\mathrm p}=a(1-e)\n$$"
              },
              {
                "label": "Khoảng viễn nhật",
                "formula": "$$\nr_{\\mathrm a}=a(1+e)\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Định luật diện tích",
            "description": "Đường nối từ thiên thể trung tâm tới vật quét các diện tích bằng nhau trong những khoảng thời gian bằng nhau. Áp dụng khi mômen động lượng quanh tâm bảo toàn.",
            "formulaRows": [
              {
                "label": "Vận tốc diện tích",
                "formula": "$$\n\\frac{dA}{dt}=\\frac12r^2\\frac{d\\theta}{dt}\n$$"
              },
              {
                "label": "Theo vận tốc tiếp tuyến",
                "formula": "$$\n\\frac{dA}{dt}=\\frac12rv\\sin\\phi\n$$"
              },
              {
                "label": "Theo mômen động lượng",
                "formula": "$$\n\\frac{dA}{dt}=\\frac L{2m}\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Lực xuyên tâm",
            "description": "Lực luôn dọc đường nối chất điểm với một điểm cố định. Mômen lực quanh điểm đó bằng không, nên vector mômen động lượng bảo toàn.",
            "formulaRows": [
              {
                "label": "Mômen lực",
                "formula": "$$\n\\vec\\tau=\\vec r\\times\\vec F=\\vec0\n$$"
              },
              {
                "label": "Mômen động lượng",
                "formula": "$$\n\\frac{d\\vec L}{dt}=\\vec0\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Định luật chu kỳ",
            "description": "Quỹ đạo liên kết quanh thiên thể trung tâm có khối lượng M lớn hơn nhiều khối lượng vật quay. Chu kỳ phụ thuộc bán trục lớn, không phụ thuộc riêng độ lệch tâm.",
            "formulaRows": [
              {
                "label": "Chu kỳ ellipse",
                "formula": "$$\nT=2\\pi\\sqrt{\\frac{a^3}{GM}}\n$$"
              },
              {
                "label": "Hai vật cùng thiên thể trung tâm",
                "formula": "$$\n\\frac{T_1}{T_2}=\\left(\\frac{a_1}{a_2}\\right)^{3/2}\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Tốc độ ở hai điểm đặc biệt",
            "description": "Trong quỹ đạo ellipse hấp dẫn liên kết, tốc độ lớn nhất tại cận nhật và nhỏ nhất tại viễn nhật. Ở hai điểm này vận tốc vuông góc bán kính.",
            "formulaRows": [
              {
                "label": "Bảo toàn mômen động lượng tại hai điểm",
                "formula": "$$\nr_{\\mathrm p}v_{\\mathrm p}=r_{\\mathrm a}v_{\\mathrm a}\n$$"
              }
            ],
            "variables": []
          }
        ]
      },
      {
        "id": "spherical-shell",
        "title": "Đối xứng cầu và vỏ cầu",
        "badge": "13.6",
        "items": [
          {
            "name": "Bên ngoài phân bố đối xứng cầu",
            "description": "Chất điểm ở bên ngoài vật đối xứng cầu tổng khối lượng M. r tính từ tâm.",
            "formulaRows": [
              {
                "label": "Thế năng",
                "formula": "$$\nU=-\\frac{GMm}{r}\n$$"
              },
              {
                "label": "Lực bán kính",
                "formula": "$$\nF_r=-\\frac{GMm}{r^2}\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Bên trong vỏ cầu mỏng đồng nhất",
            "description": "Vỏ bán kính R, khối lượng M phân bố đều trên mặt. Chất điểm ở r<R. Thế năng dùng mốc vô cực.",
            "formulaRows": [
              {
                "label": "Thế năng không đổi",
                "formula": "$$\nU=-\\frac{GMm}{R}\n$$"
              },
              {
                "label": "Hợp lực",
                "formula": "$$\n\\vec F=\\vec0\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Bên trong vật đối xứng cầu",
            "description": "M(r) là khối lượng nằm trong bán kính r. Các vỏ ngoài r không gây hợp lực lên vật thử bên trong.",
            "formulaRows": [
              {
                "label": "Độ lớn lực tại r>0",
                "formula": "$$\nF_g=\\frac{GM(r)m}{r^2}\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Quả cầu mật độ đồng nhất",
            "description": "Vật cầu bán kính R, tổng khối lượng M. Biểu thức áp dụng r≤R, và lực tại tâm bằng không theo đối xứng.",
            "formulaRows": [
              {
                "label": "Khối lượng bên trong",
                "formula": "$$\nM(r)=M\\frac{r^3}{R^3}\n$$"
              },
              {
                "label": "Độ lớn lực",
                "formula": "$$\nF_g=\\frac{GMm}{R^3}\\,r\n$$"
              },
              {
                "label": "Theo tọa độ có dấu qua tâm",
                "formula": "$$\nF_x=-\\frac{GMm}{R^3}\\,x\n$$"
              }
            ],
            "variables": []
          }
        ]
      },
      {
        "id": "apparent-weight",
        "title": "Trọng lượng biểu kiến và sự quay",
        "badge": "13.7",
        "items": [
          {
            "name": "Định nghĩa",
            "description": "F là lực do cân tác dụng lên vật. Trọng lượng biểu kiến có độ lớn bằng số chỉ cân và vector ngược hướng lực cân.",
            "formulaRows": [
              {
                "label": "Vector trọng lượng biểu kiến",
                "formula": "$$\n\\vec w=-\\vec F\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Trên xích đạo",
            "description": "Trái Đất được coi hình cầu, quay đều. w0 là trọng lượng hấp dẫn thật và v là tốc độ xích đạo.",
            "formulaRows": [
              {
                "label": "Trọng lượng biểu kiến",
                "formula": "$$\nw=w_0-\\frac{mv^2}{R_E}\n$$"
              },
              {
                "label": "Gia tốc hiệu dụng",
                "formula": "$$\ng=g_0-\\frac{v^2}{R_E}\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Vĩ độ bất kỳ",
            "description": "Gia tốc hướng tâm arad hướng về trục quay. Hệ thức là vector, không thay bằng hiệu hai độ lớn khi các vector không cùng phương.",
            "formulaRows": [
              {
                "label": "Quan hệ vector",
                "formula": "$$\n\\vec w=\\vec w_0-m\\vec a_{\\mathrm{rad}}\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Tại cực",
            "description": "Trong mô hình hình cầu, bán kính chuyển động quanh trục bằng không ở hai cực, nên số chỉ cân bằng trọng lượng thật.",
            "formulaRows": [
              {
                "label": "Độ lớn tại cực",
                "formula": "$$\nw=w_0\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Tốc độ xích đạo",
            "description": "Dùng chu kỳ quay đối với các sao xa, tức ngày thiên văn, khi tính gia tốc hướng tâm.",
            "formulaRows": [
              {
                "label": "Tốc độ",
                "formula": "$$\nv=\\frac{2\\pi R_E}{T_{\\mathrm{rot}}}\n$$"
              },
              {
                "label": "Ngày thiên văn",
                "formula": "$$\nT_{\\mathrm{rot}}\\approx86164\\,\\mathrm s\n$$"
              }
            ],
            "variables": []
          }
        ]
      },
      {
        "id": "black-holes",
        "title": "Hố đen và chân trời sự kiện",
        "badge": "13.8",
        "items": [
          {
            "name": "Tốc độ thoát theo mật độ trung bình",
            "description": "Coi thiên thể trung tâm đứng yên và vật được phóng có khối lượng nhỏ hơn nhiều khối lượng thiên thể. Trong mô hình Newton bên ngoài một thiên thể hình cầu, với khối lượng riêng trung bình rho và bán kính R.",
            "formulaRows": [
              {
                "label": "Khối lượng theo thể tích",
                "formula": "$$\nM=\\frac{4\\pi}{3}\\bar\\rho R^3\n$$"
              },
              {
                "label": "Tốc độ thoát",
                "formula": "$$\nv_{\\mathrm{esc}}=R\\sqrt{\\frac{8\\pi G\\bar\\rho}{3}}\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Bán kính Schwarzschild",
            "description": "Mô hình hố đen đối xứng cầu, không quay và không tích điện. Đây là kết quả của thuyết tương đối rộng.",
            "formulaRows": [
              {
                "label": "Bán kính chân trời",
                "formula": "$$\nR_S=\\frac{2GM}{c^2}\n$$"
              }
            ],
            "variables": [
              "$c$: Tốc độ ánh sáng trong chân không, đơn vị m/s"
            ]
          },
          {
            "name": "Chân trời sự kiện",
            "description": "Ranh giới nhân quả bao quanh vùng không thể truyền tín hiệu ra ngoài. Với mô hình Schwarzschild, chân trời là mặt cầu bán kính RS. Ánh sáng quan sát từ đĩa bồi tụ phát ra trước khi vật chất đi vào chân trời.",
            "formulaRows": [],
            "variables": []
          },
          {
            "name": "Khối lượng từ quỹ đạo sao",
            "description": "Trong mô hình Kepler chi phối bởi một vật trung tâm, chu kỳ T và bán trục lớn a của sao lân cận xác định khối lượng trung tâm.",
            "formulaRows": [
              {
                "label": "Khối lượng suy từ quỹ đạo",
                "formula": "$$\nM=\\frac{4\\pi^2a^3}{GT^2}\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Dấu hiệu quan sát",
            "description": "Chuyển động của vật lân cận, bức xạ từ đĩa bồi tụ ngoài chân trời và sóng hấp dẫn có thể cung cấp thông tin về hố đen. Dịch đỏ hấp dẫn và giãn thời gian gần chân trời thuộc mô tả tương đối rộng.",
            "formulaRows": [],
            "variables": []
          }
        ]
      }
    ]
  }
}
