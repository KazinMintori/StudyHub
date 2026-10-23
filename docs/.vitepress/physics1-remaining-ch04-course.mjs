export const physics1RemainingChapter4Parent={
  "chapter": 4,
  "prerequisites": [
    "vector",
    "thanh-phan-vector",
    "gia-toc"
  ],
  "supportingConcepts": [
    "luc",
    "he-quy-chieu-quan-tinh",
    "luc-phap-tuyen",
    "ma-sat-nghi",
    "ma-sat-truot",
    "don-vi",
    "dao-ham",
    "tich-phan"
  ],
  "topics": [
    {
      "slug": "luc-va-tuong-tac",
      "title": "Lực và tương tác",
      "question": "Làm thế nào mô tả và tổng hợp các lực tác dụng lên một vật?",
      "source": "4.1",
      "file": "parent-01-luc-va-tuong-tac.md"
    },
    {
      "slug": "dinh-luat-thu-nhat-newton",
      "title": "Định luật thứ nhất của Newton",
      "question": "Khi tổng ngoại lực bằng không, vật có thể chuyển động như thế nào?",
      "source": "4.2",
      "file": "parent-02-dinh-luat-thu-nhat.md"
    },
    {
      "slug": "dinh-luat-thu-hai-newton",
      "title": "Định luật thứ hai của Newton",
      "question": "Tổng ngoại lực và khối lượng xác định gia tốc ra sao?",
      "source": "4.3",
      "file": "parent-03-dinh-luat-thu-hai.md"
    },
    {
      "slug": "khoi-luong-va-trong-luong",
      "title": "Khối lượng và trọng lượng",
      "question": "Vì sao khối lượng không đổi khi chuyển nơi nhưng trọng lượng có thể đổi?",
      "source": "4.4",
      "file": "parent-04-khoi-luong-trong-luong.md"
    },
    {
      "slug": "dinh-luat-thu-ba-newton",
      "title": "Định luật thứ ba của Newton",
      "question": "Hai lực tương tác bằng nhau có làm hợp lực lên mỗi vật bằng không không?",
      "source": "4.5",
      "file": "parent-05-dinh-luat-thu-ba.md"
    },
    {
      "slug": "so-do-luc",
      "title": "Sơ đồ lực",
      "question": "Những lực nào được đưa vào sơ đồ của vật đã chọn?",
      "source": "4.6",
      "file": "parent-06-so-do-luc.md"
    }
  ],
  "cheatsheet": {
    "summary": "Định nghĩa lực, hợp lực, khối lượng, trọng lượng, hệ quán tính và ba định luật Newton cùng điều kiện áp dụng.",
    "sections": [
      {
        "id": "force",
        "title": "Lực và hợp lực",
        "badge": "4.1",
        "items": [
          {
            "name": "Lực",
            "description": "Đại lượng vector định lượng tương tác. Lực pháp tuyến vuông góc mặt tiếp xúc, ma sát song song mặt tiếp xúc, lực căng kéo dọc dây. Trọng lực có thể tác dụng không qua tiếp xúc.",
            "formulaRows": [],
            "variables": []
          },
          {
            "name": "Hợp lực",
            "description": "Tổng vector của mọi ngoại lực tác dụng lên cùng vật. Tổng thành phần theo mỗi trục được tính đại số, giữ đúng dấu.",
            "formulaRows": [
              {
                "label": "Ba lực",
                "formula": "$$\n\\vec R=\\vec F_1+\\vec F_2+\\vec F_3\n$$"
              },
              {
                "label": "Tổng n lực",
                "formula": "$$\n\\vec R=\\sum_{i=1}^{n}\\vec F_i\n$$"
              },
              {
                "label": "Thành phần x",
                "formula": "$$\nR_x=\\sum_{i=1}^{n}F_{ix}\n$$"
              },
              {
                "label": "Thành phần y",
                "formula": "$$\nR_y=\\sum_{i=1}^{n}F_{iy}\n$$"
              },
              {
                "label": "Độ lớn trong mặt phẳng",
                "formula": "$$\nR=\\sqrt{R_x^2+R_y^2}\n$$"
              },
              {
                "label": "Góc hướng, xét thêm góc phần tư",
                "formula": "$$\n\\tan\\theta=R_y/R_x\n$$"
              }
            ],
            "variables": []
          }
        ]
      },
      {
        "id": "inertia",
        "title": "Hệ quán tính và định luật thứ nhất",
        "badge": "4.2",
        "items": [
          {
            "name": "Hệ quy chiếu quán tính",
            "description": "Hệ mà định luật thứ nhất đúng. Một hệ chuyển động tịnh tiến với vận tốc không đổi so với một hệ quán tính cũng là hệ quán tính.",
            "formulaRows": [],
            "variables": []
          },
          {
            "name": "Cân bằng của chất điểm",
            "description": "Vận tốc không đổi, có thể bằng không, khi tổng ngoại lực bằng không. Điều kiện này không tự thay thế điều kiện cân bằng quay của vật rắn.",
            "formulaRows": [
              {
                "label": "Điều kiện lực",
                "formula": "$$\n\\sum_{i=1}^{n}\\vec F_i=\\vec0\n$$"
              },
              {
                "label": "Gia tốc",
                "formula": "$$\n\\vec a=\\vec0\n$$"
              }
            ],
            "variables": []
          }
        ]
      },
      {
        "id": "dynamics",
        "title": "Khối lượng và định luật thứ hai",
        "badge": "4.3",
        "items": [
          {
            "name": "Khối lượng quán tính",
            "description": "Đại lượng đo quán tính, có tính cộng trong cơ học Newton. Cùng một hợp lực tạo gia tốc tỉ lệ nghịch khối lượng.",
            "formulaRows": [
              {
                "label": "Cùng hợp lực",
                "formula": "$$\nm_2/m_1=a_1/a_2\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Định luật thứ hai",
            "description": "Dạng dưới đây áp dụng trong hệ quán tính khi khối lượng vật hoặc hệ không đổi. Chỉ ngoại lực lên hệ đã chọn được đưa vào tổng.",
            "formulaRows": [
              {
                "label": "Dạng vector",
                "formula": "$$\n\\sum_{i=1}^{n}\\vec F_i=m\\vec a\n$$"
              },
              {
                "label": "Thành phần x",
                "formula": "$$\n\\sum F_x=ma_x\n$$"
              },
              {
                "label": "Thành phần y",
                "formula": "$$\n\\sum F_y=ma_y\n$$"
              },
              {
                "label": "Thành phần z",
                "formula": "$$\n\\sum F_z=ma_z\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Đơn vị lực",
            "description": "Trong hệ SI, khối lượng dùng kilôgam và gia tốc dùng mét trên giây bình phương.",
            "formulaRows": [
              {
                "label": "Newton",
                "formula": "$$\n1\\,\\mathrm N=1\\,\\mathrm{kg\\cdot m/s^2}\n$$"
              },
              {
                "label": "Dyne",
                "formula": "$$\n1\\,\\mathrm{dyn}=10^{-5}\\,\\mathrm N\n$$"
              },
              {
                "label": "Pound lực",
                "formula": "$$\n1\\,\\mathrm{lb}=4{,}448221615260\\,\\mathrm N\n$$"
              }
            ],
            "variables": []
          }
        ]
      },
      {
        "id": "weight",
        "title": "Trọng lượng",
        "badge": "4.4",
        "items": [
          {
            "name": "Trọng lượng",
            "description": "Lực hấp dẫn tác dụng lên vật. Giá trị phụ thuộc trường trọng lực tại vị trí vật, còn khối lượng không đổi khi chỉ chuyển vật đến nơi khác.",
            "formulaRows": [
              {
                "label": "Độ lớn",
                "formula": "$$\nw=mg\n$$"
              },
              {
                "label": "Dạng vector",
                "formula": "$$\n\\vec w=m\\vec g\n$$"
              },
              {
                "label": "Khối lượng từ trọng lượng",
                "formula": "$$\nm=w/g\n$$"
              }
            ],
            "variables": [
              "$g$: Độ lớn gia tốc trọng trường, luôn dương.",
              "$w$: Độ lớn trọng lượng, đo bằng newton."
            ]
          }
        ]
      },
      {
        "id": "interaction",
        "title": "Cặp lực tương tác và sơ đồ lực",
        "badge": "4.5–4.6",
        "items": [
          {
            "name": "Định luật thứ ba",
            "description": "Hai lực của cùng tương tác có cùng độ lớn, ngược hướng và tác dụng lên hai vật khác nhau. Ký hiệu A/B chỉ lực do A tác dụng lên B.",
            "formulaRows": [
              {
                "label": "Quan hệ cặp lực",
                "formula": "$$\n\\vec F_{A/B}=-\\vec F_{B/A}\n$$"
              }
            ],
            "variables": []
          },
          {
            "name": "Lực căng dây",
            "description": "Trong mô hình dây thẳng không khối lượng, chỉ chịu các lực dọc dây ở hai đầu, lực căng ở hai đầu bằng nhau. Kết quả cũng đúng cho dây cân bằng khi không có lực phân bố dọc dây.",
            "formulaRows": [],
            "variables": []
          },
          {
            "name": "Sơ đồ lực",
            "description": "Biểu diễn riêng mọi ngoại lực tác dụng lên vật đã chọn. Không đưa lực vật tác dụng lên môi trường vào sơ đồ ấy. Các vật khác nhau có sơ đồ riêng.",
            "formulaRows": [],
            "variables": []
          }
        ]
      }
    ]
  },
  "openingFile": "parent-00-mo-dau.md",
  "summaryFile": "parent-17-tom-tat.md",
  "answerFile": "parent-18-dap-so-luyen-tap.md"
}
