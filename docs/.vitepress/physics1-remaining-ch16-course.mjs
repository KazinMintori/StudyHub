export const physics1RemainingChapter16Parent={
  "chapter": 16,
  "topics": [
    {
      "slug": "song-am",
      "title": "Sóng âm",
      "question": "Li độ phần tử và biến thiên áp suất mô tả cùng một sóng âm như thế nào?",
      "source": "16.1",
      "file": "01-muc-01.md"
    },
    {
      "slug": "toc-do-truyen-am",
      "title": "Tốc độ truyền âm",
      "question": "Cơ tính, khối lượng riêng và nhiệt độ quyết định tốc độ truyền ra sao?",
      "source": "16.2",
      "file": "02-muc-02.md"
    },
    {
      "slug": "cuong-do-va-muc-cuong-do-am",
      "title": "Cường độ và mức cường độ âm",
      "question": "Biên độ áp suất, biên độ li độ và decibel liên hệ như thế nào?",
      "source": "16.3",
      "file": "03-muc-03.md"
    },
    {
      "slug": "song-am-dung-va-cac-dang-rieng",
      "title": "Sóng âm dừng và các dạng dao động riêng",
      "question": "Điều kiện đầu ống chọn tần số và các nút, bụng của đại lượng nào?",
      "source": "16.4",
      "file": "04-muc-04.md"
    },
    {
      "slug": "cong-huong-am",
      "title": "Cộng hưởng âm",
      "question": "Vì sao một cột khí hoặc dây đàn có thể rung mạnh do nguồn âm bên ngoài?",
      "source": "16.5",
      "file": "05-muc-05.md"
    },
    {
      "slug": "giao-thoa-song-am",
      "title": "Giao thoa sóng âm",
      "question": "Pha và hiệu đường đi tạo các vùng âm mạnh, yếu như thế nào?",
      "source": "16.6",
      "file": "06-muc-06.md"
    },
    {
      "slug": "phach",
      "title": "Phách",
      "question": "Hai tần số gần nhau tạo nhịp lớn nhỏ với tần số nào?",
      "source": "16.7",
      "file": "07-muc-07.md"
    },
    {
      "slug": "hieu-ung-doppler",
      "title": "Hiệu ứng Doppler",
      "question": "Chuyển động của nguồn, người nghe và môi trường làm đổi tần số nhận thế nào?",
      "source": "16.8",
      "file": "08-muc-08.md"
    },
    {
      "slug": "song-xung-kich",
      "title": "Sóng xung kích",
      "question": "Nguồn vượt âm tạo mặt nón và tiếng nổ tại người nghe như thế nào?",
      "source": "16.9",
      "file": "09-muc-09.md"
    }
  ],
  "prerequisites": [
    "cong-suat-co-hoc",
    "dong-luong-vat-ly",
    "modun-khoi",
    "modun-young",
    "ap-suat-tuyet-doi-va-ap-suat-du",
    "dao-dong-cuong-buc",
    "cong-huong-co-hoc",
    "song-co-hoc",
    "ham-song-co-hoc",
    "buoc-song-co-hoc",
    "so-song",
    "chong-chat-song-tuyen-tinh",
    "cuong-do-song-co",
    "dao-ham-rieng"
  ],
  "supportingConcepts": [
    "song-am",
    "ap-suat-am",
    "toc-do-truyen-am",
    "cuong-do-am",
    "muc-cuong-do-am",
    "cao-do-am",
    "am-sac",
    "song-dung-trong-cot-khi",
    "cong-huong-am",
    "phach",
    "hieu-ung-doppler-am",
    "doppler-dien-tu",
    "song-xung-kich",
    "so-mach",
    "tieng-no-vuot-am",
    "nut-va-bung-song",
    "hoa-am-va-am-boi"
  ],
  "cheatsheet": {
    "summary": "Định nghĩa, tính chất, công thức, đơn vị và điều kiện của sóng âm, cường độ, cột khí, giao thoa, phách, Doppler và xung kích.",
    "sections": [
      {
        "id": "sound-wave-description",
        "title": "Sóng âm và áp suất",
        "badge": "16.1",
        "items": [
          {
            "name": "Sóng âm dọc",
            "description": "Trong chất lưu, dao động phần tử song song phương truyền. x là tọa độ cân bằng, y là li độ dọc, A là biên độ li độ.",
            "formulaRows": [
              {
                "label": "Li độ hình sin",
                "formula": "$$\ny=A\\cos(kx-\\omega t)\n$$"
              },
              {
                "label": "Số sóng",
                "formula": "$$\nk=\\frac{2\\pi}{\\lambda}\n$$"
              },
              {
                "label": "Tần số góc",
                "formula": "$$\n\\omega=2\\pi f\n$$"
              }
            ],
            "variables": [
              "$A$: Biên độ li độ, đơn vị m",
              "$k$: Số sóng, đơn vị rad/m",
              "$\\omega$: Tần số góc, đơn vị rad/s"
            ]
          },
          {
            "name": "Biến dạng và áp suất âm",
            "description": "p là áp suất dư so với cân bằng, B>0 là môđun khối. Biến dạng thể tích nhỏ và chuyển động dọc một chiều.",
            "formulaRows": [
              {
                "label": "Biến dạng thể tích",
                "formula": "$$\n\\frac{dV}{V}=\\frac{\\partial y}{\\partial x}\n$$"
              },
              {
                "label": "Áp suất âm",
                "formula": "$$\np=-B\\frac{\\partial y}{\\partial x}\n$$"
              }
            ],
            "variables": [
              "$p$: Áp suất âm, đơn vị Pa",
              "$B$: Môđun khối, đơn vị Pa"
            ]
          },
          {
            "name": "Biên độ áp suất",
            "description": "Với sóng hình sin, p và y lệch pha một phần tư chu kỳ tại cùng vị trí. Biên độ áp suất không phải li độ phần tử.",
            "formulaRows": [
              {
                "label": "Áp suất hình sin",
                "formula": "$$\np=BkA\\sin(kx-\\omega t)\n$$"
              },
              {
                "label": "Biên độ áp suất",
                "formula": "$$\np_{\\max}=BkA\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Cao độ và âm sắc",
            "description": "Cao độ liên hệ chủ yếu với tần số. Âm sắc phụ thuộc thành phần họa âm và sự hình thành, suy giảm âm. Độ to không đồng nghĩa cao độ. Hạ âm dưới khoảng 20 Hz, miền nghe thường khoảng 20–20000 Hz, siêu âm trên miền ấy.",
            "formulaRows": [],
            "variables": []
          }
        ]
      },
      {
        "id": "sound-propagation-speed",
        "title": "Tốc độ truyền âm",
        "badge": "16.2",
        "items": [
          {
            "name": "Sóng dọc trong chất lưu",
            "description": "Mô hình biến dạng nhỏ, môi trường gần đồng nhất, rho>0. Độ phục hồi thể tích so với quán tính quyết định tốc độ.",
            "formulaRows": [
              {
                "label": "Tốc độ âm",
                "formula": "$$\nv=\\sqrt{\\frac B\\rho}\n$$"
              },
              {
                "label": "Môđun từ tốc độ",
                "formula": "$$\nB=\\rho v^2\n$$"
              }
            ],
            "variables": [
              "$v$: Tốc độ truyền, đơn vị m/s",
              "$\\rho$: Khối lượng riêng, đơn vị kg/m³"
            ]
          },
          {
            "name": "Sóng dọc trong thanh",
            "description": "Thanh đàn hồi tuyến tính, biến dạng ngang tự do. Y là môđun Young. Không phải công thức chung cho mọi sóng trong khối rắn.",
            "formulaRows": [
              {
                "label": "Tốc độ trong thanh",
                "formula": "$$\nv=\\sqrt{\\frac Y\\rho}\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Khí lý tưởng",
            "description": "Nén giãn âm gần đoạn nhiệt. Nhiệt độ tuyệt đối T, khối lượng mol M và tỷ số nhiệt dung gamma xác định tốc độ. Với cùng loại khí, không coi áp suất là yếu tố độc lập khi lấy B/rho.",
            "formulaRows": [
              {
                "label": "Môđun đoạn nhiệt",
                "formula": "$$\nB=\\gamma p_0\n$$"
              },
              {
                "label": "Tốc độ âm",
                "formula": "$$\nv=\\sqrt{\\frac{\\gamma RT}{M}}\n$$"
              },
              {
                "label": "Tỷ số nhiệt dung",
                "formula": "$$\n\\gamma=\\frac{C_P}{C_V}\n$$"
              }
            ],
            "variables": [
              "$T$: Nhiệt độ tuyệt đối, đơn vị K",
              "$M$: Khối lượng mol, đơn vị kg/mol",
              "$R$: Hằng số khí, đơn vị J/(mol·K)"
            ]
          },
          {
            "name": "Quan hệ bước sóng và tần số",
            "description": "f>0 và tốc độ pha v trong môi trường đang xét. Khi qua mặt phân cách đứng yên, tần số giữ nguyên còn bước sóng có thể đổi.",
            "formulaRows": [
              {
                "label": "Bước sóng",
                "formula": "$$\n\\lambda=\\frac vf\n$$"
              }
            ],
            "variables": []
          }
        ]
      },
      {
        "id": "acoustic-intensity",
        "title": "Cường độ và mức cường độ âm",
        "badge": "16.3",
        "items": [
          {
            "name": "Cường độ âm chạy",
            "description": "Công suất trung bình trên diện tích vuông góc phương truyền. Công thức theo A hoặc pmax dùng cho sóng hình sin chạy trong chất lưu.",
            "formulaRows": [
              {
                "label": "Theo biên độ li độ",
                "formula": "$$\nI=\\frac12\\rho v\\omega^2A^2\n$$"
              },
              {
                "label": "Theo biên độ áp suất",
                "formula": "$$\nI=\\frac{p_{\\max}^2}{2\\rho v}\n$$"
              },
              {
                "label": "Dạng theo môđun",
                "formula": "$$\nI=\\frac{p_{\\max}^2}{2\\sqrt{\\rho B}}\n$$"
              }
            ],
            "variables": [
              "$I$: Cường độ, đơn vị W/m²"
            ]
          },
          {
            "name": "Tỷ lệ biên độ",
            "description": "Cùng môi trường và cùng tần số, cường độ tỷ lệ bình phương biên độ li độ hoặc áp suất. Với I cố định, biên độ li độ tỷ lệ nghịch tần số.",
            "formulaRows": [
              {
                "label": "Áp suất từ cường độ",
                "formula": "$$\np_{\\max}=\\sqrt{2\\rho vI}\n$$"
              },
              {
                "label": "Li độ từ cường độ",
                "formula": "$$\nA=\\frac1\\omega\\sqrt{\\frac{2I}{\\rho v}}\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Nguồn điểm tỏa đều",
            "description": "Công suất trung bình P không bị hấp thụ. Nguồn tỏa toàn mặt cầu dùng diện tích $4\\pi r^2$. Tỏa đều trên bán cầu dùng $2\\pi r^2$.",
            "formulaRows": [
              {
                "label": "Toàn mặt cầu",
                "formula": "$$\nI=\\frac{P}{4\\pi r^2}\n$$"
              },
              {
                "label": "Trên bán cầu",
                "formula": "$$\nI=\\frac{P}{2\\pi r^2}\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Mức cường độ âm",
            "description": "Cường độ tham chiếu $I_0=10^{-12}\\,\\mathrm{W/m^2}$. Logarit cơ số 10, đối số là tỷ số không thứ nguyên. Đơn vị mức là dB.",
            "formulaRows": [
              {
                "label": "Định nghĩa mức",
                "formula": "$$\n\\beta=(10\\,\\mathrm{dB})\\log_{10}\\frac I{I_0}\n$$"
              },
              {
                "label": "Đổi chênh mức",
                "formula": "$$\n\\frac{I_2}{I_1}=10^{\\Delta\\beta/(10\\,\\mathrm{dB})}\n$$"
              }
            ],
            "variables": []
          }
        ]
      },
      {
        "id": "air-column-standing",
        "title": "Sóng âm dừng và các dạng riêng",
        "badge": "16.4",
        "items": [
          {
            "name": "Điều kiện biên cột khí",
            "description": "Đầu kín là nút li độ, bụng áp suất. Đầu hở gần là bụng li độ, nút áp suất. Nút/bụng phải chỉ rõ đại lượng.",
            "formulaRows": [],
            "variables": []
          },
          {
            "name": "Khoảng cách nút và bụng",
            "description": "Trong sóng dừng một chiều hình sin, hai nút kế tiếp hoặc hai bụng kế tiếp cách $\\lambda/2$. Nút và bụng kề nhau cách $\\lambda/4$.",
            "formulaRows": [
              {
                "label": "Hai nút kề",
                "formula": "$$\nd_{NN}=\\frac\\lambda2\n$$"
              },
              {
                "label": "Nút và bụng kề",
                "formula": "$$\nd_{NA}=\\frac\\lambda4\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Ống hở hai đầu",
            "description": "Cột khí đều dài hiệu dụng L, bỏ hiệu chỉnh đầu ống. n=1,2,3,… là mọi số nguyên dương.",
            "formulaRows": [
              {
                "label": "Bước sóng riêng",
                "formula": "$$\n\\lambda_n=\\frac{2L}{n}\n$$"
              },
              {
                "label": "Tần số riêng",
                "formula": "$$\nf_n=\\frac{nv}{2L}\n$$"
              },
              {
                "label": "Tần số cơ bản",
                "formula": "$$\nf_1=\\frac v{2L}\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Ống kín một đầu",
            "description": "Cột khí đều dài hiệu dụng L, một đầu kín và đầu kia hở. n=1,3,5,… chỉ nhận số nguyên dương lẻ.",
            "formulaRows": [
              {
                "label": "Bước sóng riêng",
                "formula": "$$\n\\lambda_n=\\frac{4L}{n}\n$$"
              },
              {
                "label": "Tần số riêng",
                "formula": "$$\nf_n=\\frac{nv}{4L}\n$$"
              },
              {
                "label": "Tần số cơ bản",
                "formula": "$$\nf_1=\\frac v{4L}\n$$"
              }
            ],
            "variables": []
          }
        ]
      },
      {
        "id": "sound-resonance",
        "title": "Cộng hưởng âm",
        "badge": "16.5",
        "items": [
          {
            "name": "Cộng hưởng có cản",
            "description": "Đáp ứng tăng mạnh khi tần số kích thích gần một tần số riêng. Đỉnh phụ thuộc hình học, độ cản và đại lượng đáp ứng. Cản yếu cho đỉnh gần tần số riêng không cản.",
            "formulaRows": [],
            "variables": []
          },
          {
            "name": "Tần số và bước sóng ở cộng hưởng",
            "description": "Hai hệ ghép cộng hưởng có thể cùng tần số nhưng khác bước sóng vì tốc độ truyền khác nhau.",
            "formulaRows": [
              {
                "label": "Cùng tần số",
                "formula": "$$\nf_a=f_b\n$$"
              },
              {
                "label": "Tỷ số bước sóng",
                "formula": "$$\n\\frac{\\lambda_a}{\\lambda_b}=\\frac{v_a}{v_b}\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Cấp và mất năng lượng",
            "description": "Ở trạng thái ổn định có cản, công suất trung bình nhận cân bằng công suất tiêu tán. Hệ lý tưởng không cản kích thích đúng tần số riêng không có biên độ ổn định hữu hạn.",
            "formulaRows": [],
            "variables": []
          }
        ]
      },
      {
        "id": "acoustic-interference",
        "title": "Giao thoa sóng âm",
        "badge": "16.6",
        "items": [
          {
            "name": "Hiệu đường đi",
            "description": "Hai nguồn cùng tần số, cùng pha ban đầu. Pha tới phụ thuộc chênh đường truyền. Nguồn lệch pha ban đầu cần tính thêm độ lệch ấy.",
            "formulaRows": [
              {
                "label": "Độ chênh đường đi",
                "formula": "$$\nd=|r_2-r_1|\n$$"
              },
              {
                "label": "Độ lệch pha do đường truyền",
                "formula": "$$\n\\Delta\\phi=\\frac{2\\pi d}{\\lambda}\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Tăng cường",
            "description": "Hai nguồn cùng pha và cùng tần số. n=0,1,2,… là số nguyên không âm.",
            "formulaRows": [
              {
                "label": "Điều kiện đường đi",
                "formula": "$$\nd=n\\lambda\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Triệt tiêu",
            "description": "Hai nguồn cùng pha và cùng tần số. n=1,3,5,… là số nguyên dương lẻ. Triệt tiêu áp suất hoàn toàn còn cần biên độ tới bằng nhau.",
            "formulaRows": [
              {
                "label": "Điều kiện đường đi",
                "formula": "$$\nd=\\frac{n\\lambda}{2}\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Giới hạn của sự triệt tiêu",
            "description": "Năng lượng được phân bố lại, không biến mất. Với hai sóng tới không song song, tổng áp suất bằng không không tự làm tổng vector li độ bằng không.",
            "formulaRows": [],
            "variables": []
          }
        ]
      },
      {
        "id": "acoustic-beats",
        "title": "Phách",
        "badge": "16.7",
        "items": [
          {
            "name": "Tần số phách",
            "description": "Hai âm gần tần số tạo nhịp lớn nhỏ. Pha ban đầu không đổi khoảng cách giữa hai cực đại bao liên tiếp.",
            "formulaRows": [
              {
                "label": "Tần số nhịp",
                "formula": "$$\nf_{\\mathrm{ph}}=|f_a-f_b|\n$$"
              },
              {
                "label": "Chu kỳ nhịp",
                "formula": "$$\nT_{\\mathrm{ph}}=\\frac1{|f_a-f_b|}\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Dao động nhanh và bao biên",
            "description": "Hai dao động có cùng biên độ A. Đặt $\\Delta f=f_a-f_b$ và $\\bar f=(f_a+f_b)/2$. Với pha đầu đối nhau, $h=\\pi\\Delta f\\,t$ và $g=2\\pi\\bar f\\,t$.",
            "formulaRows": [
              {
                "label": "Tần số trung bình",
                "formula": "$$\n\\bar f=\\frac{f_a+f_b}{2}\n$$"
              },
              {
                "label": "Dao động tổng",
                "formula": "$$\ny=2A\\sin h\\cos g\n$$"
              },
              {
                "label": "Biên độ bao",
                "formula": "$$\nA_{\\mathrm{bao}}=2A|\\sin h|\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Thông tin từ nhịp phách",
            "description": "Biết một tần số và tần số phách chỉ cho hai khả năng cao hơn hoặc thấp hơn. Phách khác âm hiệu có thể xuất hiện do đáp ứng phi tuyến.",
            "formulaRows": [],
            "variables": []
          }
        ]
      },
      {
        "id": "sound-doppler",
        "title": "Hiệu ứng Doppler",
        "badge": "16.8",
        "items": [
          {
            "name": "Quy ước Doppler âm",
            "description": "Nguồn S và người nghe L chuyển động dọc đường nối, vận tốc đo so với môi trường. Chiều dương từ L tới S. Xét miền dưới tốc độ âm, v>0.",
            "formulaRows": [
              {
                "label": "Tần số nhận",
                "formula": "$$\nf_L=\\frac{v+v_L}{v+v_S}f_S\n$$"
              }
            ],
            "variables": [
              "$v_L$: Thành phần vận tốc người nghe, đơn vị m/s",
              "$v_S$: Thành phần vận tốc nguồn, đơn vị m/s"
            ]
          },
          {
            "name": "Người nghe chuyển động",
            "description": "Nguồn đứng yên đối với môi trường. Người nghe tiến về nguồn có $v_L>0$, ra xa có $v_L<0$.",
            "formulaRows": [
              {
                "label": "Tần số nhận",
                "formula": "$$\nf_L=\\left(1+\\frac{v_L}{v}\\right)f_S\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Bước sóng do nguồn chuyển động",
            "description": "u>0 là tốc độ nguồn đối với môi trường, u<v. Phía trước và phía sau được xác định theo chiều nguồn chuyển động.",
            "formulaRows": [
              {
                "label": "Phía trước",
                "formula": "$$\n\\lambda_{\\mathrm{trước}}=\\frac{v-u}{f_S}\n$$"
              },
              {
                "label": "Phía sau",
                "formula": "$$\n\\lambda_{\\mathrm{sau}}=\\frac{v+u}{f_S}\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Âm phản xạ",
            "description": "Bề mặt nhận sóng ở lượt tới, rồi là nguồn ở lượt phản xạ. Tần số phát lại trong hệ bề mặt bằng tần số bề mặt nhận. Cần hai lần đổi vai nguồn/người nghe.",
            "formulaRows": [],
            "variables": []
          },
          {
            "name": "Doppler điện từ dọc phương",
            "description": "Trong chân không, c không đổi và $|u|<c$. Vận tốc nguồn trong hệ máy thu đứng yên là u, dương khi ra xa và âm khi tiến tới. Tần số $f_S$ đo trong hệ nghỉ nguồn.",
            "formulaRows": [
              {
                "label": "Tần số máy thu",
                "formula": "$$\nf_R=\\sqrt{\\frac{c-u}{c+u}}f_S\n$$"
              }
            ],
            "variables": []
          }
        ]
      },
      {
        "id": "acoustic-shock",
        "title": "Sóng xung kích và số Mach",
        "badge": "16.9",
        "items": [
          {
            "name": "Số Mach",
            "description": "Tốc độ vật $v_S$ đo so với môi trường, tốc độ âm $v>0$. Vượt âm ứng với $M>1$.",
            "formulaRows": [
              {
                "label": "Định nghĩa",
                "formula": "$$\nM=\\frac{v_S}{v}\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Góc nón Mach",
            "description": "Nguồn chuyển động đều vượt âm trong môi trường đồng nhất. Góc $\\alpha$ giữa một đường sinh nón và phương vận tốc là nửa góc mở nón.",
            "formulaRows": [
              {
                "label": "Góc nón",
                "formula": "$$\n\\sin\\alpha=\\frac v{v_S}=\\frac1M\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Tiếng nổ vượt âm",
            "description": "Tiếng nổ xuất hiện khi mặt xung kích đi qua người nghe. Vật tạo xung kích liên tục khi còn vượt âm, không chỉ lúc vừa vượt Mach 1 hoặc chỉ khi động cơ phát tiếng. Công thức Doppler phía trước nguồn dưới âm không được kéo dài sang nguồn vượt âm.",
            "formulaRows": [],
            "variables": []
          }
        ]
      }
    ]
  },
  "topicReferences": {
    "16.1": [
      {
        "title": "NIH NIDCD: Các xương truyền âm trong tai giữa",
        "url": "https://www.nidcd.nih.gov/health/otosclerosis"
      },
      {
        "title": "NIH NIDCD: Tác động của âm mạnh tới thính giác",
        "url": "https://www.nidcd.nih.gov/health/noise-induced-hearing-loss"
      }
    ],
    "16.3": [
      {
        "title": "NIH NIDCD: Cường độ và thời gian phơi nhiễm tiếng ồn",
        "url": "https://www.nidcd.nih.gov/health/noise-induced-hearing-loss"
      }
    ],
    "16.9": [
      {
        "title": "NASA: Thế hệ máy bay X-1 đầu tiên",
        "url": "https://www.nasa.gov/aeronautics/first-generation-x-1/"
      },
      {
        "title": "NASA: Chuyến bay vượt âm của X-1",
        "url": "https://www.nasa.gov/history/x1/"
      }
    ]
  }
}
