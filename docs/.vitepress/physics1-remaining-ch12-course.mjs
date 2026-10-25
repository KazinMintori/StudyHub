export const physics1RemainingChapter12Parent={
  "chapter": 12,
  "topics": [
    {
      "slug": "chat-khi-chat-long-va-khoi-luong-rieng",
      "title": "Chất khí, chất lỏng và khối lượng riêng",
      "question": "Vì sao cùng một thể tích nhưng chất khí, chất lỏng và chất rắn có khối lượng khác nhau?",
      "source": "12.1",
      "file": "01-muc-01.md"
    },
    {
      "slug": "ap-suat-trong-chat-luu",
      "title": "Áp suất trong chất lưu",
      "question": "Áp suất thay đổi theo độ sâu như thế nào và các dụng cụ đo áp suất hoạt động ra sao?",
      "source": "12.2",
      "file": "02-muc-02.md"
    },
    {
      "slug": "luc-day-archimedes-va-suc-cang-be-mat",
      "title": "Lực đẩy Archimedes và sức căng bề mặt",
      "question": "Lực nào giữ vật nổi trong chất lưu, và vì sao một vật đặc hơn nước vẫn có thể nằm trên mặt nước?",
      "source": "12.3",
      "file": "03-muc-03.md"
    },
    {
      "slug": "dong-chay-chat-luu",
      "title": "Dòng chảy chất lưu",
      "question": "Bảo toàn khối lượng liên hệ tiết diện, khối lượng riêng và tốc độ của dòng chảy như thế nào?",
      "source": "12.4",
      "file": "04-muc-04.md"
    },
    {
      "slug": "phuong-trinh-bernoulli",
      "title": "Phương trình Bernoulli",
      "question": "Công của áp lực làm thay đổi tốc độ và độ cao của chất lưu như thế nào?",
      "source": "12.5",
      "file": "05-muc-05.md"
    },
    {
      "slug": "do-nhot-va-chay-roi",
      "title": "Độ nhớt và chảy rối",
      "question": "Khi ma sát bên trong chất lưu và những nhiễu loạn dòng chảy trở nên đáng kể, mô hình lý tưởng thay đổi ra sao?",
      "source": "12.6",
      "file": "06-muc-06.md"
    }
  ],
  "prerequisites": [
    "luc",
    "cong-nang-luong",
    "don-vi",
    "dao-ham"
  ],
  "supportingConcepts": [
    "khoi-luong-rieng",
    "ty-khoi",
    "ap-suat-chat-luu",
    "nguyen-ly-pascal",
    "ap-suat-tuyet-doi-va-ap-suat-du",
    "luc-day-archimedes",
    "suc-cang-be-mat",
    "chat-luu-ly-tuong",
    "duong-dong-chat-luu",
    "phuong-trinh-lien-tuc",
    "phuong-trinh-bernoulli",
    "do-nhot-chat-luu",
    "chay-tang-va-chay-roi",
    "dong-nhot-trong-ong-tru",
    "ong-dong-chat-luu",
    "duong-di-phan-tu-chat-luu",
    "luu-luong-chat-luu"
  ],
  "cheatsheet": {
    "summary": "Định nghĩa, tính chất, công thức, đơn vị và điều kiện của khối lượng riêng, áp suất, lực nổi, dòng chảy lý tưởng, độ nhớt và chảy rối.",
    "sections": [
      {
        "id": "density",
        "title": "Chất khí, chất lỏng và khối lượng riêng",
        "badge": "12.1",
        "items": [
          {
            "name": "Chất lưu",
            "description": "Chất lưu có thể chảy và thay đổi hình dạng. Chất khí và chất lỏng đều là chất lưu. Chất lỏng có lực liên kết phân tử đủ mạnh để giữ thể tích gần như không đổi trong những điều kiện thông thường.",
            "formulaRows": [],
            "variables": []
          },
          {
            "name": "Khối lượng riêng",
            "description": "Vật liệu đồng nhất có cùng khối lượng riêng tại mọi điểm. Với vật không đồng nhất, tỉ số khối lượng toàn vật và thể tích toàn vật là khối lượng riêng trung bình.",
            "formulaRows": [
              {
                "label": "Vật liệu đồng nhất",
                "formula": "$$\n\\rho=\\frac mV\n$$"
              },
              {
                "label": "Giá trị trung bình",
                "formula": "$$\n\\bar\\rho=\\frac{m_{\\mathrm{tot}}}{V_{\\mathrm{tot}}}\n$$"
              }
            ],
            "variables": [
              "$\\rho$: Khối lượng riêng, đơn vị kg/m³",
              "$m$: Khối lượng, đơn vị kg",
              "$V$: Thể tích, đơn vị m³"
            ]
          },
          {
            "name": "Đơn vị khối lượng riêng",
            "description": "Đơn vị SI là kilogram trên mét khối. Giá trị bằng gram trên centimet khối được đổi sang SI bằng hệ số một nghìn.",
            "formulaRows": [
              {
                "label": "Đổi đơn vị",
                "formula": "$$\n1\\,\\mathrm{g/cm^3}=10^3\\,\\mathrm{kg/m^3}\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Tỉ khối",
            "description": "Tỉ khối là tỉ số khối lượng riêng của vật liệu và khối lượng riêng của nước ở 4,0 °C. Đại lượng này không có đơn vị.",
            "formulaRows": [
              {
                "label": "Định nghĩa",
                "formula": "$$\nd=\\frac{\\rho}{\\rho_{\\mathrm w}}\n$$"
              },
              {
                "label": "Khối lượng riêng tham chiếu",
                "formula": "$$\n\\rho_{\\mathrm w}\\approx10^3\\,\\mathrm{kg/m^3}\n$$"
              }
            ],
            "variables": [
              "$d$: Tỉ khối",
              "$\\rho_{\\mathrm w}$: Khối lượng riêng của nước ở 4,0 °C"
            ]
          },
          {
            "name": "Sự phụ thuộc trạng thái",
            "description": "Khối lượng riêng phụ thuộc nhiệt độ, áp suất và cấu tạo vật liệu. Khối lượng riêng trung bình của một vật rỗng tính cả phần thể tích rỗng thuộc vật.",
            "formulaRows": [],
            "variables": []
          }
        ]
      },
      {
        "id": "pressure",
        "title": "Áp suất và cân bằng chất lưu",
        "badge": "12.2",
        "items": [
          {
            "name": "Áp suất tại một điểm",
            "description": "Áp suất là đại lượng vô hướng. Trong chất lưu đứng yên, áp lực tác dụng vuông góc với mặt tiếp xúc. Hai phía của một mặt nhỏ trong chất lưu cân bằng chịu lực bằng nhau về độ lớn và ngược chiều.",
            "formulaRows": [
              {
                "label": "Định nghĩa cục bộ",
                "formula": "$$\np=\\frac{dF_\\perp}{dA}\n$$"
              }
            ],
            "variables": [
              "$p$: Áp suất, đơn vị Pa",
              "$dF_\\perp$: Độ lớn lực pháp tuyến trên mặt nhỏ, đơn vị N",
              "$dA$: Diện tích mặt nhỏ, đơn vị m²"
            ]
          },
          {
            "name": "Áp suất đều trên mặt phẳng",
            "description": "Khi áp suất bằng nhau trên toàn bộ mặt phẳng đang xét, độ lớn áp lực ở một phía bằng tích áp suất và diện tích.",
            "formulaRows": [
              {
                "label": "Định nghĩa với áp suất đều",
                "formula": "$$\np=\\frac{F_\\perp}{A}\n$$"
              },
              {
                "label": "Áp lực",
                "formula": "$$\nF_\\perp=pA\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Đơn vị áp suất",
            "description": "Pascal là đơn vị SI. Atmosphere tiêu chuẩn được định nghĩa bằng 101325 Pa. Bar và millibar là các đơn vị áp suất.",
            "formulaRows": [
              {
                "label": "Pascal",
                "formula": "$$\n1\\,\\mathrm{Pa}=1\\,\\mathrm{N/m^2}\n$$"
              },
              {
                "label": "Atmosphere tiêu chuẩn",
                "formula": "$$\n1\\,\\mathrm{atm}=101325\\,\\mathrm{Pa}\n$$"
              },
              {
                "label": "Bar",
                "formula": "$$\n1\\,\\mathrm{bar}=10^5\\,\\mathrm{Pa}\n$$"
              },
              {
                "label": "Millibar",
                "formula": "$$\n1\\,\\mathrm{mbar}=100\\,\\mathrm{Pa}\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Phương trình thủy tĩnh",
            "description": "Chất lưu đứng yên trong trường trọng lực. Trục y hướng lên và g là độ lớn gia tốc trọng trường. Công thức hiệu áp suất dưới đây dùng khối lượng riêng và g không đổi trên đoạn xét.",
            "formulaRows": [
              {
                "label": "Dạng vi phân",
                "formula": "$$\n\\frac{dp}{dy}=-\\rho g\n$$"
              },
              {
                "label": "Giữa hai cao độ",
                "formula": "$$\np_2-p_1=-\\rho g(y_2-y_1)\n$$"
              }
            ],
            "variables": [
              "$y$: Cao độ, đơn vị m",
              "$g>0$: Gia tốc trọng trường, đơn vị m/s²"
            ]
          },
          {
            "name": "Áp suất theo độ sâu",
            "description": "Với chất lưu có khối lượng riêng không đổi và mặt chuẩn chịu áp suất p₀, áp suất tăng theo độ sâu. Hai điểm cùng cao độ trong cùng chất lưu liên thông đứng yên có áp suất bằng nhau, bỏ qua hiệu ứng bề mặt.",
            "formulaRows": [
              {
                "label": "Tại độ sâu h",
                "formula": "$$\np=p_0+\\rho gh\n$$"
              }
            ],
            "variables": [
              "$h\\ge0$: Độ sâu dưới mặt chuẩn, đơn vị m",
              "$p_0$: Áp suất tại mặt chuẩn"
            ]
          },
          {
            "name": "Nguyên lý Pascal",
            "description": "Độ tăng áp suất tác dụng lên chất lưu kín được truyền nguyên vẹn tới mọi phần chất lưu và thành bình trong mô hình cân bằng với khối lượng riêng không đổi.",
            "formulaRows": [
              {
                "label": "Độ tăng áp suất",
                "formula": "$$\n\\Delta p=\\Delta p_0\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Máy nâng thủy lực",
            "description": "Hai pít-tông ở cùng cao độ, bỏ qua các hiệu chỉnh do khối lượng pít-tông và ma sát. Các lực F₁, F₂ tương ứng với cùng phần áp suất tăng thêm.",
            "formulaRows": [
              {
                "label": "Cùng áp suất tăng thêm",
                "formula": "$$\n\\frac{F_1}{A_1}=\\frac{F_2}{A_2}\n$$"
              },
              {
                "label": "Tỉ số lực",
                "formula": "$$\nF_2=\\frac{A_2}{A_1}F_1\n$$"
              }
            ],
            "variables": [
              "$A_1,A_2$: Diện tích hai pít-tông, đơn vị m²"
            ]
          },
          {
            "name": "Áp suất tuyệt đối và áp suất dư",
            "description": "Áp suất dư là hiệu giữa áp suất tuyệt đối và áp suất khí quyển tại nơi đo. Áp suất dư có thể âm khi áp suất bên trong thấp hơn áp suất khí quyển.",
            "formulaRows": [
              {
                "label": "Áp suất dư",
                "formula": "$$\np_{\\mathrm g}=p-p_{\\mathrm{atm}}\n$$"
              },
              {
                "label": "Áp suất tuyệt đối",
                "formula": "$$\np=p_{\\mathrm{atm}}+p_{\\mathrm g}\n$$"
              }
            ],
            "variables": [
              "$p$: Áp suất tuyệt đối",
              "$p_{\\mathrm g}$: Áp suất dư",
              "$p_{\\mathrm{atm}}$: Áp suất khí quyển"
            ]
          },
          {
            "name": "Áp kế ống hở",
            "description": "Hai nhánh chứa cùng chất lỏng đứng yên. Mặt thoáng nhánh hở chịu áp suất khí quyển. Hiệu cao độ h có dấu theo thứ tự y₂−y₁.",
            "formulaRows": [
              {
                "label": "Cân bằng tại cùng cao độ",
                "formula": "$$\np+\\rho gy_1=p_{\\mathrm{atm}}+\\rho gy_2\n$$"
              },
              {
                "label": "Chênh cao",
                "formula": "$$\nh=y_2-y_1\n$$"
              },
              {
                "label": "Áp suất dư",
                "formula": "$$\np_{\\mathrm g}=\\rho gh\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Khí áp kế thủy ngân",
            "description": "Phía trên cột thủy ngân gần chân không. Bỏ qua áp suất hơi ở đỉnh cột, áp suất khí quyển bằng áp suất do cột thủy ngân cao h gây ra.",
            "formulaRows": [
              {
                "label": "Áp suất khí quyển",
                "formula": "$$\np_{\\mathrm{atm}}=\\rho_{\\mathrm{Hg}}gh\n$$"
              },
              {
                "label": "Millimet thủy ngân",
                "formula": "$$\n1\\,\\mathrm{mmHg}\\approx133{,}3\\,\\mathrm{Pa}\n$$"
              }
            ],
            "variables": []
          }
        ]
      },
      {
        "id": "buoyancy-surface",
        "title": "Lực nổi và sức căng bề mặt",
        "badge": "12.3",
        "items": [
          {
            "name": "Nguyên lý Archimedes",
            "description": "Lực đẩy hướng lên bằng trọng lượng phần chất lưu bị vật chiếm chỗ. Với chất lưu có khối lượng riêng không đổi trong trường trọng lực đều, đường tác dụng đi qua trọng tâm phần chất lưu bị chiếm chỗ.",
            "formulaRows": [
              {
                "label": "Lực đẩy",
                "formula": "$$\nB=\\rho_{\\mathrm f}gV_{\\mathrm d}\n$$"
              }
            ],
            "variables": [
              "$B$: Độ lớn lực đẩy, đơn vị N",
              "$\\rho_{\\mathrm f}$: Khối lượng riêng chất lưu",
              "$V_{\\mathrm d}$: Thể tích chất lưu bị chiếm chỗ, đơn vị m³"
            ]
          },
          {
            "name": "Vật nổi cân bằng",
            "description": "Khi chỉ trọng lực và lực đẩy tác dụng lên vật, lực đẩy bằng trọng lượng. Tỉ lệ thể tích chìm dưới đây bỏ qua lực nổi của không khí và dùng khối lượng riêng trung bình của toàn vật.",
            "formulaRows": [
              {
                "label": "Cân bằng lực",
                "formula": "$$\nB=mg\n$$"
              },
              {
                "label": "Phần thể tích chìm",
                "formula": "$$\n\\frac{V_{\\mathrm d}}V=\\frac{\\bar\\rho}{\\rho_{\\mathrm f}}\n$$"
              }
            ],
            "variables": [
              "$V$: Thể tích toàn vật",
              "$\\bar\\rho$: Khối lượng riêng trung bình của toàn vật"
            ]
          },
          {
            "name": "Vật được treo trong chất lưu",
            "description": "Với dây căng kéo thẳng lên và vật cân bằng, lực căng bằng trọng lượng trừ lực đẩy. Biểu thức áp dụng khi lực căng không âm. Nếu lực đẩy lớn hơn trọng lượng, dây phía trên không thể giữ vật bằng lực căng.",
            "formulaRows": [
              {
                "label": "Lực căng dây",
                "formula": "$$\nT=mg-B\n$$"
              },
              {
                "label": "Điều kiện dây kéo lên",
                "formula": "$$\nT\\ge0\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Phù kế",
            "description": "Phù kế tự nổi cân bằng. Cùng một phù kế chiếm chỗ thể tích chất lỏng lớn hơn khi khối lượng riêng chất lỏng nhỏ hơn.",
            "formulaRows": [],
            "variables": []
          },
          {
            "name": "Sức căng bề mặt",
            "description": "Lực hút giữa các phân tử khiến bề mặt chất lỏng có xu hướng giảm diện tích và chống lại sự kéo giãn. Hiệu ứng này đáng kể với các lượng chất lỏng nhỏ khi lực bề mặt chi phối. Nước nóng và xà phòng làm giảm sức căng bề mặt trong tình huống giặt rửa được xét.",
            "formulaRows": [],
            "variables": []
          },
          {
            "name": "Tỉ số diện tích trên thể tích của hình cầu",
            "description": "Với cùng hình dạng cầu, tỉ số diện tích trên thể tích tăng khi bán kính giảm. Hình cầu có diện tích nhỏ nhất trong các hình khối có cùng thể tích.",
            "formulaRows": [
              {
                "label": "Diện tích mặt cầu",
                "formula": "$$\nA=4\\pi r^2\n$$"
              },
              {
                "label": "Thể tích khối cầu",
                "formula": "$$\nV=\\frac{4\\pi r^3}{3}\n$$"
              },
              {
                "label": "Tỉ số diện tích trên thể tích",
                "formula": "$$\n\\frac AV=\\frac3r\n$$"
              }
            ],
            "variables": [
              "$r>0$: Bán kính hình cầu, đơn vị m"
            ]
          }
        ]
      },
      {
        "id": "fluid-flow",
        "title": "Dòng chảy và phương trình liên tục",
        "badge": "12.4",
        "items": [
          {
            "name": "Chất lưu lý tưởng",
            "description": "Mô hình chất lưu không nén được và không có ma sát bên trong. Bỏ qua ứng suất nhớt khi tác dụng của chúng nhỏ so với lực áp suất và trọng lực.",
            "formulaRows": [],
            "variables": []
          },
          {
            "name": "Dòng ổn định, đường dòng và ống dòng",
            "description": "Trong dòng ổn định, trường vận tốc tại mỗi vị trí cố định không đổi theo thời gian. Tiếp tuyến đường dòng cùng hướng vận tốc tức thời. Đường đi của phần tử trùng đường dòng trong dòng ổn định. Chất lưu không đi xuyên qua thành bên của ống dòng.",
            "formulaRows": [],
            "variables": []
          },
          {
            "name": "Phương trình liên tục cho chất lưu không nén được",
            "description": "Dòng ổn định, cùng một ống dòng không có nguồn cấp hoặc nhánh hút qua thành bên. Khối lượng riêng không đổi. Các tốc độ là đều trên tiết diện hoặc được hiểu là giá trị trung bình phù hợp.",
            "formulaRows": [
              {
                "label": "Bảo toàn lưu lượng thể tích",
                "formula": "$$\nA_1v_1=A_2v_2\n$$"
              }
            ],
            "variables": [
              "$A_i$: Diện tích tiết diện i, đơn vị m²",
              "$v_i$: Tốc độ dòng tại tiết diện i, đơn vị m/s"
            ]
          },
          {
            "name": "Lưu lượng thể tích",
            "description": "Lưu lượng thể tích là thể tích đi qua một tiết diện trong một đơn vị thời gian. Công thức Av dùng tốc độ trung bình theo tiết diện nếu vận tốc không đều.",
            "formulaRows": [
              {
                "label": "Định nghĩa",
                "formula": "$$\nQ=\\frac{dV}{dt}\n$$"
              },
              {
                "label": "Qua tiết diện",
                "formula": "$$\nQ=Av\n$$"
              }
            ],
            "variables": [
              "$Q$: Lưu lượng thể tích, đơn vị m³/s"
            ]
          },
          {
            "name": "Lưu lượng khối lượng",
            "description": "Dòng ổn định bảo toàn lưu lượng khối lượng. Chất lưu nén được có thể thay đổi khối lượng riêng và lưu lượng thể tích giữa các tiết diện.",
            "formulaRows": [
              {
                "label": "Định nghĩa lưu lượng khối lượng",
                "formula": "$$\n\\dot m=\\rho Av=\\rho Q\n$$"
              },
              {
                "label": "Hai tiết diện",
                "formula": "$$\n\\rho_1A_1v_1=\\rho_2A_2v_2\n$$"
              }
            ],
            "variables": [
              "$\\dot m$: Lưu lượng khối lượng, đơn vị kg/s"
            ]
          },
          {
            "name": "Chảy tầng và chảy rối",
            "description": "Chảy tầng có các phần chất lưu trượt êm tương đối. Chảy rối có chuyển động bất quy tắc, các xoáy và trường vận tốc biến đổi theo thời gian trong mô tả của chương.",
            "formulaRows": [],
            "variables": []
          }
        ]
      },
      {
        "id": "bernoulli",
        "title": "Phương trình Bernoulli",
        "badge": "12.5",
        "items": [
          {
            "name": "Điều kiện Bernoulli",
            "description": "Dòng ổn định, chất lưu không nén được, bỏ qua nhớt và tổn hao cơ năng. Hai điểm thuộc cùng một đường dòng hoặc ống dòng được mô hình hóa. Không có công bơm hay tuabin giữa hai điểm trong dạng phương trình đang xét.",
            "formulaRows": [],
            "variables": []
          },
          {
            "name": "Đại lượng Bernoulli",
            "description": "Tổng áp suất, thế năng trọng trường trên thể tích và động năng trên thể tích không đổi dọc đường dòng dưới các điều kiện Bernoulli. Mỗi số hạng có đơn vị Pa.",
            "formulaRows": [
              {
                "label": "Hai tiết diện trên cùng đường dòng",
                "formula": "$$\n\\begin{aligned}\n&p_1+\\rho gy_1+\\frac12\\rho v_1^2=C,\\\\\n&p_2+\\rho gy_2+\\frac12\\rho v_2^2=C.\n\\end{aligned}\n$$"
              },
              {
                "label": "Dọc đường dòng",
                "formula": "$$\np+\\rho gy+\\frac12\\rho v^2=C\n$$"
              }
            ],
            "variables": [
              "$C$: Hằng số Bernoulli của đường dòng",
              "$y_i$: Cao độ, cùng một mốc cho hai điểm"
            ]
          },
          {
            "name": "Công của lực áp suất",
            "description": "Trong cùng thời gian, thể tích dV đi vào và đi ra ống dòng không nén được bằng nhau. Công áp suất ở đầu vào dương, ở đầu ra âm theo chiều dòng.",
            "formulaRows": [
              {
                "label": "Thể tích qua hai đầu",
                "formula": "$$\ndV=A_1ds_1=A_2ds_2\n$$"
              },
              {
                "label": "Công tại đầu vào",
                "formula": "$$\ndW_1=p_1dV\n$$"
              },
              {
                "label": "Công tại đầu ra",
                "formula": "$$\ndW_2=-p_2dV\n$$"
              },
              {
                "label": "Tổng công áp suất",
                "formula": "$$\ndW=(p_1-p_2)dV\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Biến thiên cơ năng của dòng",
            "description": "Trong phép so sánh hai trạng thái của dòng ổn định, phần thể tích chung không đổi cơ năng. Với phần chất lưu được thay thế có khối lượng ρdV, công áp suất bằng biến thiên động năng và thế năng.",
            "formulaRows": [
              {
                "label": "Biến thiên động năng",
                "formula": "$$\ndK=\\frac{\\rho dV}{2}(v_2^2-v_1^2)\n$$"
              },
              {
                "label": "Biến thiên thế năng",
                "formula": "$$\ndU=\\rho g\\,dV(y_2-y_1)\n$$"
              },
              {
                "label": "Quan hệ công và năng lượng",
                "formula": "$$\ndW=dK+dU\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Hiệu áp suất, tốc độ và cao độ",
            "description": "Hai điểm thỏa các điều kiện Bernoulli. Đặt Δ(v²)=v₂²−v₁² và Δy=y₂−y₁.",
            "formulaRows": [
              {
                "label": "Dạng hiệu",
                "formula": "$$\np_1-p_2=\\frac\\rho2\\Delta(v^2)+\\rho g\\Delta y\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Hai điểm cùng độ cao",
            "description": "Dưới các điều kiện Bernoulli, điểm có tốc độ lớn hơn có áp suất nhỏ hơn khi hai điểm ở cùng cao độ trên dòng đang xét.",
            "formulaRows": [
              {
                "label": "Quan hệ áp suất và tốc độ",
                "formula": "$$\np_1-p_2=\\frac\\rho2(v_2^2-v_1^2)\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Giới hạn thủy tĩnh",
            "description": "Khi chất lưu đứng yên, các số hạng động năng bằng không. Phương trình Bernoulli trở về hệ thức thủy tĩnh.",
            "formulaRows": [
              {
                "label": "Chất lưu đứng yên",
                "formula": "$$\np_2-p_1=-\\rho g(y_2-y_1)\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Tốc độ thoát từ bình chứa lớn",
            "description": "Mặt thoáng có diện tích lớn hơn nhiều tiết diện lỗ, nên tốc độ hạ mặt thoáng không đáng kể. Chất lỏng chảy ra khí quyển qua lỗ ở độ sâu h. Áp suất dư trên mặt thoáng là p_g. Mô hình lý tưởng áp dụng khi biểu thức dưới căn không âm.",
            "formulaRows": [
              {
                "label": "Tốc độ thoát",
                "formula": "$$\nv=\\sqrt{\\frac{2p_{\\mathrm g}}\\rho+2gh}\n$$"
              },
              {
                "label": "Lưu lượng qua lỗ",
                "formula": "$$\nQ=A_2v\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Định lý Torricelli",
            "description": "Bình chứa lớn và lỗ thoát cùng chịu áp suất khí quyển, bỏ qua nhớt và coi dòng gần ổn định tại độ sâu đang xét.",
            "formulaRows": [
              {
                "label": "Tốc độ thoát",
                "formula": "$$\nv=\\sqrt{2gh}\n$$"
              },
              {
                "label": "Lưu lượng",
                "formula": "$$\nQ=A_2\\sqrt{2gh}\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Ống đo Venturi",
            "description": "Dòng lý tưởng ổn định trong ống nằm ngang. Hai ống đo hở chứa cùng chất lỏng đang chảy. Tiết diện đầu A₁ lớn hơn tiết diện cổ A₂ và h là độ chênh hai cột chất lỏng.",
            "formulaRows": [
              {
                "label": "Tỉ số tiết diện",
                "formula": "$$\n\\alpha=\\frac{A_1}{A_2}>1\n$$"
              },
              {
                "label": "Chênh áp đo được",
                "formula": "$$\np_1-p_2=\\rho gh\n$$"
              },
              {
                "label": "Tốc độ tại tiết diện lớn",
                "formula": "$$\nv_1=\\sqrt{\\frac{2gh}{\\alpha^2-1}}\n$$"
              }
            ],
            "variables": []
          }
        ]
      },
      {
        "id": "viscosity-turbulence",
        "title": "Độ nhớt và chảy rối",
        "badge": "12.6",
        "items": [
          {
            "name": "Độ nhớt",
            "description": "Độ nhớt đặc trưng ma sát bên trong chất lưu. Lực nhớt chống lại chuyển động tương đối giữa những phần chất lưu. Ở các chất được xét, độ nhớt tăng theo nhiệt độ đối với khí và giảm theo nhiệt độ đối với chất lỏng.",
            "formulaRows": [],
            "variables": []
          },
          {
            "name": "Lớp biên sát bề mặt rắn",
            "description": "Chất lưu nhớt có xu hướng bám bề mặt rắn. Gần bề mặt, tốc độ tương đối của chất lưu so với bề mặt nhỏ. Trong mô hình không trượt ở thành ống, tốc độ tương đối bằng không.",
            "formulaRows": [
              {
                "label": "Thành ống đứng yên",
                "formula": "$$\nv(R)=0\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Chảy tầng nhớt trong ống trụ",
            "description": "Trong ống trụ dài, dòng tầng có độ lớn vận tốc theo bán kính dạng parabol. Tốc độ lớn nhất trên trục ống và bằng không tại thành. Cần chênh áp theo chiều dòng để duy trì lưu lượng.",
            "formulaRows": [],
            "variables": []
          },
          {
            "name": "Chênh áp duy trì dòng nhớt",
            "description": "Với cùng chất lưu, trạng thái nhiệt độ và lưu lượng thể tích trong dòng tầng qua ống trụ dài, chênh áp tỉ lệ chiều dài ống và nghịch đảo lũy thừa bậc bốn bán kính trong.",
            "formulaRows": [
              {
                "label": "Quan hệ tỉ lệ",
                "formula": "$$\n\\Delta p\\propto\\frac L{R^4}\n$$"
              },
              {
                "label": "Đổi bán kính, giữ chiều dài",
                "formula": "$$\n\\frac{\\Delta p'}{\\Delta p}=\\left(\\frac R{R'}\\right)^4\n$$"
              }
            ],
            "variables": [
              "$\\Delta p>0$: Chênh áp từ đầu vào đến đầu ra",
              "$L$: Chiều dài ống, đơn vị m",
              "$R$: Bán kính trong của ống, đơn vị m"
            ]
          },
          {
            "name": "Sự hình thành chảy rối",
            "description": "Khả năng xuất hiện chảy rối phụ thuộc tốc độ, độ nhớt, hình dạng biên và nhiễu loạn. Trong mô hình đang xét, nhiễu nhỏ tắt dần ở dòng tầng ổn định nhưng phát triển khi dòng mất ổn định. Không có một tốc độ tới hạn chung cho mọi chất lưu và mọi ống.",
            "formulaRows": [],
            "variables": []
          },
          {
            "name": "Phạm vi của mô hình dòng lý tưởng",
            "description": "Ma sát nhớt và chảy rối có thể ảnh hưởng mạnh tới dòng quanh vật và lực do chất lưu gây ra, kể cả khi chất lưu có độ nhớt nhỏ. Dạng Bernoulli không tổn hao không mô tả được đầy đủ các vùng dòng nhớt hoặc rối đáng kể.",
            "formulaRows": [],
            "variables": []
          }
        ]
      }
    ]
  },
  "topicReferences": {
    "12.2": [
      {
        "title": "Công bố chung của Trung Quốc và Nepal về độ cao đỉnh Everest (08/12/2020)",
        "url": "https://www.fmprc.gov.cn/mfa_eng/gjhdq_665435/2675_665437/2752_663508/2754_663512/202406/t20240607_11411566.html"
      }
    ]
  }
}
