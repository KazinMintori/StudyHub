export const physics1RemainingChapter15Parent={
  "chapter": 15,
  "topics": [
    {
      "slug": "cac-loai-song-co",
      "title": "Các loại sóng cơ",
      "question": "Sóng truyền đi trong khi từng phần tử môi trường chuyển động như thế nào?",
      "source": "15.1",
      "file": "01-muc-01.md"
    },
    {
      "slug": "song-tuan-hoan",
      "title": "Sóng tuần hoàn",
      "question": "Bước sóng, chu kỳ và tần số xác định tốc độ truyền ra sao?",
      "source": "15.2",
      "file": "02-muc-02.md"
    },
    {
      "slug": "ham-song",
      "title": "Hàm sóng",
      "question": "Làm thế nào mô tả dạng sóng và dao động của từng phần tử bằng một hàm?",
      "source": "15.3",
      "file": "03-muc-03.md"
    },
    {
      "slug": "toc-do-song-tren-day",
      "title": "Tốc độ sóng ngang trên dây",
      "question": "Lực căng và quán tính của dây quyết định tốc độ truyền thế nào?",
      "source": "15.4",
      "file": "04-muc-04.md"
    },
    {
      "slug": "nang-luong-trong-chuyen-dong-song",
      "title": "Năng lượng trong chuyển động sóng",
      "question": "Biên độ, tần số và khoảng cách ảnh hưởng công suất và cường độ ra sao?",
      "source": "15.5",
      "file": "05-muc-05.md"
    },
    {
      "slug": "giao-thoa-dieu-kien-bien-va-chong-chat",
      "title": "Giao thoa, điều kiện biên và chồng chất",
      "question": "Vì sao sóng phản xạ có thể đảo dấu, và hai sóng chồng nhau được cộng thế nào?",
      "source": "15.6",
      "file": "06-muc-06.md"
    },
    {
      "slug": "song-dung-tren-day",
      "title": "Sóng dừng trên dây",
      "question": "Hai sóng chạy ngược chiều tạo nút, bụng và chuyển động tại chỗ ra sao?",
      "source": "15.7",
      "file": "07-muc-07.md"
    },
    {
      "slug": "cac-dang-dao-dong-rieng-cua-day",
      "title": "Các dạng dao động riêng của dây",
      "question": "Hai đầu cố định chọn những tần số nào và vì sao dây đàn tạo nhiều họa âm?",
      "source": "15.8",
      "file": "08-muc-08.md"
    }
  ],
  "prerequisites": [
    "dao-dong-dieu-hoa",
    "luc",
    "cong-nang-luong",
    "dao-ham",
    "dong-luong-vat-ly"
  ],
  "supportingConcepts": [
    "song-co-hoc",
    "buoc-song-co-hoc",
    "so-song",
    "ham-song-co-hoc",
    "toc-do-song-ngang-tren-day",
    "cong-suat-song-co",
    "cuong-do-song-co",
    "chong-chat-song-tuyen-tinh",
    "dieu-kien-bien-cua-day",
    "song-dung-co-hoc",
    "nut-va-bung-song",
    "dang-dao-dong-rieng-cua-day",
    "hoa-am-va-am-boi",
    "phan-tich-hoa-am-cua-day",
    "pha-song",
    "giao-thoa-song",
    "dao-ham-rieng"
  ],
  "cheatsheet": {
    "summary": "Định nghĩa, tính chất, công thức và điều kiện của sóng cơ, sóng trên dây, công suất, chồng chất, sóng dừng và các dạng dao động riêng.",
    "sections": [
      {
        "id": "mechanical-waves",
        "title": "Các loại sóng cơ",
        "badge": "15.1",
        "items": [
          {
            "name": "Sóng cơ",
            "description": "Nhiễu loạn truyền trong môi trường vật chất. Tốc độ truyền nhiễu loạn khác vận tốc dao động của từng phần tử môi trường.",
            "formulaRows": [],
            "variables": []
          },
          {
            "name": "Sóng ngang và sóng dọc",
            "description": "Sóng ngang có phương dao động vuông góc chiều truyền. Sóng dọc có phương dao động cùng phương chiều truyền. Một chuyển động sóng có thể chứa cả hai thành phần.",
            "formulaRows": [],
            "variables": []
          },
          {
            "name": "Truyền năng lượng",
            "description": "Sóng cơ truyền năng lượng nhờ tương tác giữa các phần môi trường. Trong mô hình dao động tuyến tính đang xét, phần tử dao động quanh vị trí cân bằng, còn hình dạng nhiễu loạn truyền đi.",
            "formulaRows": [],
            "variables": []
          }
        ]
      },
      {
        "id": "periodic-waves",
        "title": "Sóng tuần hoàn",
        "badge": "15.2",
        "items": [
          {
            "name": "Chu kỳ và tần số",
            "description": "Chu kỳ là thời gian chuyển động lặp lại, còn tần số là số chu kỳ trong một đơn vị thời gian.",
            "formulaRows": [
              {
                "label": "Quan hệ",
                "formula": "$$\nf=\\frac1T,\\qquad \\omega=2\\pi f\n$$"
              }
            ],
            "variables": [
              "$T$: Đơn vị s",
              "$f$: Đơn vị Hz",
              "$\\omega$: Đơn vị rad/s"
            ]
          },
          {
            "name": "Bước sóng",
            "description": "Khoảng cách giữa hai điểm liên tiếp cùng pha của sóng tuần hoàn, chẳng hạn hai đỉnh kề nhau. Trong một chu kỳ, dạng sóng chạy một bước sóng.",
            "formulaRows": [
              {
                "label": "Tốc độ truyền",
                "formula": "$$\nv=\\frac\\lambda T=\\lambda f\n$$"
              }
            ],
            "variables": [
              "$\\lambda$: Đơn vị m",
              "$v$: Đơn vị m/s"
            ]
          },
          {
            "name": "Môi trường không tán sắc",
            "description": "Khi tốc độ truyền chỉ do các tính chất cơ học cố định của môi trường quyết định, tăng tần số làm giảm bước sóng theo cùng tỷ lệ nghịch. Tính độc lập với tần số này là giả thiết của các mô hình trong chương.",
            "formulaRows": [],
            "variables": []
          }
        ]
      },
      {
        "id": "wave-functions",
        "title": "Hàm sóng hình sin",
        "badge": "15.3",
        "items": [
          {
            "name": "Nguồn điều hòa tại gốc",
            "description": "Chọn gốc thời gian khi nguồn có li độ dương cực đại.",
            "formulaRows": [
              {
                "label": "Hàm nguồn",
                "formula": "$$\ny(0,t)=A\\cos\\omega t\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Hàm sóng truyền theo chiều dương",
            "description": "Với hàm $y(x,t)$, pha $kx-\\omega t$ không đổi trên các vị trí chuyển về phía x tăng. Ba cách viết dưới đây tương đương, với y là cùng hàm li độ.",
            "formulaRows": [
              {
                "label": "Theo thời gian truyền",
                "formula": "$$\ny=A\\cos\\!\\left[\\omega\\left(\\frac xv-t\\right)\\right]\n$$"
              },
              {
                "label": "Theo bước sóng và chu kỳ",
                "formula": "$$\ny=A\\cos\\!\\left[2\\pi\\left(\\frac x\\lambda-\\frac tT\\right)\\right]\n$$"
              },
              {
                "label": "Theo số sóng",
                "formula": "$$\ny=A\\cos(kx-\\omega t)\n$$"
              }
            ],
            "variables": [
              "$A\\ge0$: Biên độ li độ, đơn vị m"
            ]
          },
          {
            "name": "Số sóng và tần số góc",
            "description": "Số sóng là tốc độ biến thiên pha theo vị trí. Tần số góc là độ biến thiên pha theo thời gian tại một vị trí.",
            "formulaRows": [
              {
                "label": "Số sóng",
                "formula": "$$\nk=\\frac{2\\pi}\\lambda\n$$"
              },
              {
                "label": "Quan hệ tốc độ",
                "formula": "$$\n\\omega=vk\n$$"
              }
            ],
            "variables": [
              "$k$: Đơn vị rad/m"
            ]
          },
          {
            "name": "Sóng truyền theo chiều âm",
            "description": "Dấu cộng giữa $kx$ và $\\omega t$ ứng với chiều truyền âm khi k và tần số góc đều dương.",
            "formulaRows": [
              {
                "label": "Hàm sóng",
                "formula": "$$\ny=A\\cos(kx+\\omega t)\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Vận tốc và gia tốc phần tử",
            "description": "Lấy đạo hàm theo thời gian ở vị trí cân bằng x cố định. Với sóng truyền theo chiều dương, đặt $\\theta=kx-\\omega t$.",
            "formulaRows": [
              {
                "label": "Vận tốc phần tử",
                "formula": "$$\nv_y=\\frac{\\partial y}{\\partial t}=\\omega A\\sin\\theta\n$$"
              },
              {
                "label": "Gia tốc phần tử",
                "formula": "$$\na_y=-\\omega^2A\\cos\\theta=-\\omega^2y\n$$"
              },
              {
                "label": "Độ cong tức thời",
                "formula": "$$\n\\frac{\\partial^2y}{\\partial x^2}=-k^2y\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Phương trình sóng tuyến tính",
            "description": "Tốc độ truyền v không đổi. Phương trình liên hệ độ cong không gian với gia tốc phần tử.",
            "formulaRows": [
              {
                "label": "Phương trình",
                "formula": "$$\n\\frac{\\partial^2y}{\\partial x^2}=\\frac1{v^2}\\frac{\\partial^2y}{\\partial t^2}\n$$"
              }
            ],
            "variables": []
          }
        ]
      },
      {
        "id": "string-dynamics",
        "title": "Tốc độ sóng trên dây",
        "badge": "15.4",
        "items": [
          {
            "name": "Khối lượng riêng dài",
            "description": "Khối lượng trên một đơn vị chiều dài. Với dây đồng nhất, tổng khối lượng bằng $\\mu L$.",
            "formulaRows": [
              {
                "label": "Định nghĩa",
                "formula": "$$\n\\mu=\\frac mL\n$$"
              }
            ],
            "variables": [
              "$\\mu$: Đơn vị kg/m"
            ]
          },
          {
            "name": "Xung lượng của phần dây",
            "description": "Với phần dây ban đầu đứng yên được cuốn vào chuyển động ngang trong thời gian t, khối lượng tham gia là $\\mu vt$.",
            "formulaRows": [
              {
                "label": "Xung lượng",
                "formula": "$$\nF_yt=mv_y\n$$"
              },
              {
                "label": "Khối lượng tham gia",
                "formula": "$$\nm=\\mu vt\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Tốc độ sóng ngang trên dây",
            "description": "Dây mềm đồng nhất, lực căng gần đều, độ dốc và dao động ngang nhỏ. Khối lượng riêng dài giữ vai trò quán tính, còn lực căng giữ vai trò phục hồi.",
            "formulaRows": [
              {
                "label": "Tốc độ truyền",
                "formula": "$$\nv=\\sqrt{\\frac F\\mu}\n$$"
              },
              {
                "label": "Phương trình động lực học",
                "formula": "$$\n\\frac{\\partial^2y}{\\partial x^2}=\\frac\\mu F\\frac{\\partial^2y}{\\partial t^2}\n$$"
              }
            ],
            "variables": [
              "$F>0$: Lực căng, đơn vị N"
            ]
          },
          {
            "name": "Phụ thuộc tính chất dây",
            "description": "Với $\\mu$ không đổi, tốc độ tỉ lệ căn lực căng. Với lực căng không đổi, tốc độ tỉ lệ nghịch căn khối lượng riêng dài.",
            "formulaRows": [
              {
                "label": "Các tỷ lệ",
                "formula": "$$\nv\\propto\\sqrt F,\\qquad v\\propto\\frac1{\\sqrt\\mu}\n$$"
              }
            ],
            "variables": []
          }
        ]
      },
      {
        "id": "wave-power",
        "title": "Năng lượng và cường độ",
        "badge": "15.5",
        "items": [
          {
            "name": "Lực và công suất qua một điểm",
            "description": "Xét lực của phần dây bên trái lên phần bên phải. Công suất dương quy ước năng lượng truyền theo chiều x tăng.",
            "formulaRows": [
              {
                "label": "Thành phần lực",
                "formula": "$$\nF_y=-F\\frac{\\partial y}{\\partial x}\n$$"
              },
              {
                "label": "Công suất",
                "formula": "$$\nP=-F\\frac{\\partial y}{\\partial x}\\frac{\\partial y}{\\partial t}\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Công suất sóng chạy hình sin",
            "description": "Với sóng chạy theo chiều dương, đặt $\\theta=kx-\\omega t$ và viết P cho $P(x,t)$. Công suất tức thời không âm trong trường hợp một sóng chạy này.",
            "formulaRows": [
              {
                "label": "Dạng theo số sóng",
                "formula": "$$\nP=Fk\\omega A^2\\sin^2\\theta\n$$"
              },
              {
                "label": "Dạng theo tính chất dây",
                "formula": "$$\nP=\\sqrt{\\mu F}\\,\\omega^2A^2\\sin^2\\theta\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Công suất cực đại và trung bình",
            "description": "Trung bình trên một số nguyên chu kỳ. Với cùng dây và cùng lực căng, công suất trung bình tỉ lệ $A^2f^2$, trong đó A là biên độ li độ.",
            "formulaRows": [
              {
                "label": "Cực đại",
                "formula": "$$\nP_{\\max}=\\sqrt{\\mu F}\\,\\omega^2A^2\n$$"
              },
              {
                "label": "Trung bình",
                "formula": "$$\nP_{\\mathrm{tb}}=\\frac12\\sqrt{\\mu F}\\,\\omega^2A^2\n$$"
              },
              {
                "label": "Quan hệ",
                "formula": "$$\nP_{\\mathrm{tb}}=\\frac{P_{\\max}}2\n$$"
              }
            ],
            "variables": [
              "$P$: Đơn vị W"
            ]
          },
          {
            "name": "Cường độ sóng",
            "description": "Công suất trung bình truyền qua một đơn vị diện tích S vuông góc chiều truyền. Công thức thương dưới đây áp dụng khi cường độ đều trên S.",
            "formulaRows": [
              {
                "label": "Định nghĩa",
                "formula": "$$\nI=\\frac{P_{\\mathrm{tb}}}{S}\n$$"
              }
            ],
            "variables": [
              "$I$: Đơn vị $\\mathrm{W/m^2}$"
            ]
          },
          {
            "name": "Nguồn phát đều mọi hướng",
            "description": "Không có hấp thụ hay tổn thất công suất giữa các mặt cầu và bỏ qua phản xạ. P là công suất trung bình nguồn.",
            "formulaRows": [
              {
                "label": "Cường độ trên mặt cầu",
                "formula": "$$\nI=\\frac P{4\\pi r^2}\n$$"
              },
              {
                "label": "Định luật nghịch đảo bình phương",
                "formula": "$$\n\\frac{I_1}{I_2}=\\frac{r_2^2}{r_1^2}\n$$"
              }
            ],
            "variables": []
          }
        ]
      },
      {
        "id": "reflection-superposition",
        "title": "Phản xạ và chồng chất",
        "badge": "15.6",
        "items": [
          {
            "name": "Đầu cố định",
            "description": "Li độ đầu dây bằng không ở mọi thời điểm. Sóng phản xạ lý tưởng đảo dấu li độ so với sóng tới.",
            "formulaRows": [
              {
                "label": "Biên tại gốc",
                "formula": "$$\ny(0,t)=0\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Đầu tự do lý tưởng",
            "description": "Vòng nhẹ không ma sát không nhận lực theo phương dao động từ giá đỡ. Độ dốc tại đầu tự do bằng không, và sóng phản xạ không đảo dấu.",
            "formulaRows": [
              {
                "label": "Biên tại gốc",
                "formula": "$$\n\\left.\\frac{\\partial y}{\\partial x}\\right|_{x=0}=0\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Chồng chất tuyến tính",
            "description": "Li độ tổng tại cùng vị trí và thời điểm bằng tổng đại số các li độ thành phần. Cần phương trình sóng và điều kiện biên tuyến tính.",
            "formulaRows": [
              {
                "label": "Hai sóng",
                "formula": "$$\ny(x,t)=y_1(x,t)+y_2(x,t)\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Giao thoa tăng cường và triệt tiêu",
            "description": "Cộng hai li độ cùng dấu làm tăng độ lớn li độ tổng. Hai li độ trái dấu bù nhau một phần hoặc toàn phần. Sau khi hai xung vượt qua nhau trong môi trường tuyến tính lý tưởng, từng xung tiếp tục truyền với dạng riêng.",
            "formulaRows": [],
            "variables": []
          }
        ]
      },
      {
        "id": "standing-wave",
        "title": "Sóng dừng",
        "badge": "15.7",
        "items": [
          {
            "name": "Hai sóng chạy ngược chiều",
            "description": "Hai sóng cùng $A,\\omega,k$, với quan hệ pha thỏa đầu cố định ở gốc.",
            "formulaRows": [
              {
                "label": "Sóng tới",
                "formula": "$$\ny_1=-A\\cos(kx+\\omega t)\n$$"
              },
              {
                "label": "Sóng phản xạ",
                "formula": "$$\ny_2=A\\cos(kx-\\omega t)\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Hàm sóng dừng",
            "description": "Viết y cho li độ y(x,t). Biên độ tại một điểm là độ lớn thừa số không gian. Các điểm trong cùng một bó dao động cùng pha.",
            "formulaRows": [
              {
                "label": "Hàm sóng",
                "formula": "$$\ny=A_{\\mathrm{SW}}\\sin kx\\sin\\omega t\n$$"
              },
              {
                "label": "Biên độ tại bụng",
                "formula": "$$\nA_{\\mathrm{SW}}=2A\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Nút và bụng",
            "description": "Nút luôn đứng yên. Bụng có biên độ lớn nhất và nằm giữa hai nút. Nút đếm bằng n=0,1,2,... từ đầu cố định.",
            "formulaRows": [
              {
                "label": "Vị trí nút",
                "formula": "$$\nx_n=\\frac{n\\lambda}2\n$$"
              },
              {
                "label": "Hai nút hoặc hai bụng kề",
                "formula": "$$\nd=\\frac\\lambda2\n$$"
              },
              {
                "label": "Nút và bụng kề",
                "formula": "$$\nd=\\frac\\lambda4\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Năng lượng sóng dừng lý tưởng",
            "description": "Có trao đổi năng lượng cục bộ theo thời gian, nhưng không có truyền năng lượng trung bình qua một điểm. Công suất tức thời không bắt buộc bằng không ở mọi điểm.",
            "formulaRows": [
              {
                "label": "Công suất trung bình",
                "formula": "$$\nP_{\\mathrm{tb}}=0\n$$"
              }
            ],
            "variables": []
          }
        ]
      },
      {
        "id": "normal-modes",
        "title": "Dạng riêng và họa âm",
        "badge": "15.8",
        "items": [
          {
            "name": "Hai đầu cố định",
            "description": "Chiều dài chứa một, hai, ba,... nửa bước sóng. Chỉ số n chạy qua các số nguyên dương.",
            "formulaRows": [
              {
                "label": "Điều kiện bước sóng",
                "formula": "$$\nL=n\\frac\\lambda2\n$$"
              },
              {
                "label": "Bước sóng dạng thứ n",
                "formula": "$$\n\\lambda_n=\\frac{2L}n\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Tần số cơ bản và họa âm",
            "description": "Tần số riêng của dây mềm lý tưởng là $f_1$, $2f_1$, $3f_1$, v.v. với $n=1,2,3,\\ldots$. Mỗi dạng có cùng tần số tại mọi điểm, nhưng biên độ có thể khác nhau.",
            "formulaRows": [
              {
                "label": "Tần số cơ bản",
                "formula": "$$\nf_1=\\frac v{2L}\n$$"
              },
              {
                "label": "Tần số họa âm",
                "formula": "$$\nf_n=\\frac{nv}{2L}=nf_1\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Hàm của dạng riêng",
            "description": "Viết y_n cho y_n(x,t). Hai đầu x=0 và x=L đều là nút. Pha thời gian có thể thay đổi theo điều kiện đầu.",
            "formulaRows": [
              {
                "label": "Hàm li độ",
                "formula": "$$\ny_n=A_{\\mathrm{SW}}\\sin k_nx\\sin\\omega_nt\n$$"
              },
              {
                "label": "Số sóng riêng",
                "formula": "$$\nk_n=\\frac{n\\pi}L\n$$"
              },
              {
                "label": "Tần số góc riêng",
                "formula": "$$\n\\omega_n=2\\pi f_n\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Họa âm và âm bồi",
            "description": "Họa âm thứ nhất là âm cơ bản. Họa âm thứ hai là âm bồi thứ nhất. Âm bồi thứ hai là họa âm thứ ba.",
            "formulaRows": [],
            "variables": []
          },
          {
            "name": "Tần số cơ bản theo tính chất dây",
            "description": "Trong mô hình dây mềm đồng nhất, căng gần đều và dao động ngang nhỏ, tần số giảm khi tăng chiều dài hoặc khối lượng riêng dài, tăng khi tăng lực căng.",
            "formulaRows": [
              {
                "label": "Công thức",
                "formula": "$$\nf_1=\\frac1{2L}\\sqrt{\\frac F\\mu}\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Chồng các dạng riêng",
            "description": "Với cùng $x,t$, các thành phần $Y_1,Y_2,Y_3,\\ldots$ đóng góp li độ bằng phép cộng đại số. Đây là ý nghĩa của khai triển Fourier trong chuyển động dây.",
            "formulaRows": [
              {
                "label": "Khai triển",
                "formula": "$$\ny=Y_1+Y_2+Y_3+\\cdots\n$$"
              },
              {
                "label": "Ký hiệu tổng",
                "formula": "$$\ny=\\sum_{n=1}^{\\infty}Y_n\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Sóng âm do dây tạo ra",
            "description": "Tần số kích thích được giữ khi dây làm không khí dao động. Bước sóng đổi nếu tốc độ truyền trong hai môi trường khác nhau.",
            "formulaRows": [
              {
                "label": "Tần số",
                "formula": "$$\nf_{\\mathrm{âm}}=f_{\\mathrm{dây}}\n$$"
              },
              {
                "label": "Tỷ số bước sóng",
                "formula": "$$\n\\frac{\\lambda_{\\mathrm{âm}}}{\\lambda_{\\mathrm{dây}}}=\\frac{v_{\\mathrm{âm}}}{v_{\\mathrm{dây}}}\n$$"
              }
            ],
            "variables": []
          }
        ]
      }
    ]
  }
}
