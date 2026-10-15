export const lesson = {
  "number": 2,
  "slug": "bai-02-tap-loi",
  "title": "Các bài toán tối ưu lồi",
  "prerequisites": [
    "tap-loi",
    "ham-loi",
    "chuan",
    "ma-tran-psd"
  ],
  "supportingConcepts": [
    "tham-so-toan-hoc",
    "mien-kha-thi",
    "epigraph",
    "he-phuong-trinh",
    "ma-tran",
    "noi-long-toi-uu",
    "infimum",
    "lagrangian"
  ],
  "status": "ready",
  "description": "Nhận diện LP, QP, SOCP, SDP và GP. Phân biệt cải dạng tương đương, xấp xỉ và nới lỏng.",
  "topicGroups": [
    {
      "title": "I. Biến đổi bài toán",
      "description": "Viết lại một bài toán mà không làm sai lời giải, và nhận ra lúc tính lồi bị cách viết che khuất.",
      "topics": [
        {
          "slug": "bai-toan-tuong-duong",
          "title": "Bài toán tương đương và các phép biến đổi cơ bản",
          "question": "Khi nào hai bài toán viết khác nhau lại cho cùng một lời giải, và phép biến đổi nào làm mất điều đó?",
          "source": "§4.1.3, §4.2.1"
        },
        {
          "slug": "khu-rang-buoc-va-toi-uu-tung-phan",
          "title": "Khử ràng buộc đẳng thức và tối ưu theo từng nhóm biến",
          "question": "Một ràng buộc đẳng thức tuyến tính có thể biến mất mà không mất thông tin nào không, và cái giá phải trả là gì?",
          "source": "§4.1.3, §4.2.4"
        },
        {
          "slug": "toi-uu-tua-loi",
          "title": "Hàm tựa lồi và phương pháp chia đôi",
          "question": "Nếu chỉ biết mọi tập mức dưới đều lồi, ta còn giải bài toán một cách đáng tin cậy được không?",
          "source": "§3.4, §4.2.5"
        }
      ]
    },
    {
      "title": "II. Quy hoạch tuyến tính",
      "description": "Lớp bài toán đơn giản nhất nhưng mô tả được rất nhiều mô hình, từ hình học tới xác suất.",
      "topics": [
        {
          "slug": "quy-hoach-tuyen-tinh",
          "title": "Quy hoạch tuyến tính: Các dạng viết và hình học của nghiệm",
          "question": "Vì sao mọi LP đều đưa được về cùng một dạng chuẩn, và nghiệm của nó nằm ở đâu trên đa diện?",
          "source": "§4.3"
        },
        {
          "slug": "mo-hinh-lp",
          "title": "Những bài toán trở thành LP",
          "question": "Tìm hình tròn lớn nhất nằm trong một đa giác nghe chẳng tuyến tính chút nào. Vì sao đó lại là một LP?",
          "source": "§4.3.1"
        },
        {
          "slug": "quy-hoach-phan-tuyen-tinh",
          "title": "Quy hoạch phân tuyến tính",
          "question": "Cực tiểu một tỉ số của hai hàm affine có khó hơn LP không?",
          "source": "§4.3.2"
        }
      ]
    },
    {
      "title": "III. Quy hoạch toàn phương và nón bậc hai",
      "description": "Khi mục tiêu hay ràng buộc cong lên, nghiệm rời khỏi các đỉnh và chuẩn Euclid xuất hiện.",
      "topics": [
        {
          "slug": "quy-hoach-toan-phuong",
          "title": "Quy hoạch toàn phương và QCQP",
          "question": "Khi mục tiêu cong như một cái bát, nghiệm còn nằm ở đỉnh của đa diện nữa không?",
          "source": "§4.4–4.4.1"
        },
        {
          "slug": "quy-hoach-non-bac-hai",
          "title": "Quy hoạch nón bậc hai và LP bền vững",
          "question": "Muốn một ràng buộc tuyến tính đúng với mọi tham số trong một vùng bất định, ta phải trả giá bằng hình dạng nào?",
          "source": "§4.4.2"
        }
      ]
    },
    {
      "title": "IV. Quy hoạch hình học",
      "description": "Những bài toán không lồi trong biến gốc nhưng trở thành lồi sau khi chuyển sang thang logarit.",
      "topics": [
        {
          "slug": "quy-hoach-hinh-hoc",
          "title": "Quy hoạch hình học",
          "question": "Một bài toán không lồi có thể trở thành lồi chỉ nhờ đổi sang thang logarit không?",
          "source": "§4.5"
        }
      ]
    },
    {
      "title": "V. Bất đẳng thức suy rộng và SDP",
      "description": "Thay thứ tự từng thành phần bằng thứ tự của các ma trận nửa xác định dương.",
      "topics": [
        {
          "slug": "bai-toan-dang-non-va-sdp",
          "title": "Bài toán dạng nón và quy hoạch nửa xác định",
          "question": "Thay \"mọi thành phần không âm\" bằng \"ma trận nửa xác định dương\", ta được lớp bài toán nào?",
          "source": "§4.6.1–4.6.2"
        },
        {
          "slug": "phan-bu-schur-va-bai-toan-tri-rieng",
          "title": "Phần bù Schur và các bài toán về trị riêng",
          "question": "Làm thế nào viết một ràng buộc phi tuyến như \"chuẩn phổ không vượt quá t\" thành một bất đẳng thức ma trận tuyến tính?",
          "source": "§4.6.3, §A.5.5"
        }
      ]
    },
    {
      "title": "VI. Tối ưu vector",
      "description": "Khi phải cân nhiều mục tiêu cùng lúc, câu trả lời là cả một đường đánh đổi chứ không phải một điểm.",
      "topics": [
        {
          "slug": "toi-uu-vector-va-danh-doi",
          "title": "Tối ưu vector, điểm Pareto và đường đánh đổi",
          "question": "Khi sai số nhỏ và tham số nhỏ là hai mục tiêu cùng lúc, thế nào là một lựa chọn tốt?",
          "source": "§4.7, §6.3"
        }
      ]
    },
    {
      "title": "VII. Xấp xỉ, khớp hàm và ước lượng thống kê",
      "description": "Tìm hàm xấp xỉ tối ưu, thiết kế bộ phát hiện và chặn xác suất rủi ro bằng tối ưu lồi.",
      "topics": [
        {
          "slug": "khop-ham-va-noi-suy",
          "title": "Khớp hàm, làm mượt spline và nội suy lồi",
          "question": "Làm thế nào tìm một hàm lồi khớp mượt mà với dữ liệu quan sát mà không làm mất tính lồi?",
          "source": "§6.5"
        },
        {
          "slug": "uoc-luong-phi-tham-so-va-kiem-dinh",
          "title": "Ước lượng phi tham số và thiết kế bộ phát hiện",
          "question": "Khi không biết dạng phân phối xác suất, làm sao thiết kế bộ phát hiện tối ưu qua LP?",
          "source": "§7.2–7.3"
        },
        {
          "slug": "can-chebyshev-va-chernoff",
          "title": "Cận xác suất Chebyshev, Chernoff và tối ưu hóa ma trận",
          "question": "Làm thế nào chặn trên xác suất đuôi và ngoại lai qua bài toán SDP và biến đổi Legendre?",
          "source": "§7.4"
        }
      ]
    },
    {
      "title": "VIII. Quy hoạch mặt bằng",
      "description": "Bài toán bố trí không gian hình học và tối ưu hóa diện tích qua quy hoạch hình học.",
      "topics": [
        {
          "slug": "quy-hoach-mat-bang",
          "title": "Quy hoạch mặt bằng và phân bổ không gian tối ưu",
          "question": "Làm thế nào tối ưu kích thước linh kiện và dây nối mà vẫn bảo toàn tỷ lệ khung hình?",
          "source": "§8.8"
        }
      ]
    },
    {
      "title": "IX. Thiết kế thí nghiệm và Hình học cực trị",
      "description": "Thiết kế thí nghiệm tối ưu Fisher, ellipsoid thể tích cực trị Loewner–John và bài toán định vị mạng lưới.",
      "topics": [
        {
          "slug": "thiet-ke-thi-nghiem-toi-uu",
          "title": "Thiết kế thí nghiệm tối ưu và Ma trận thông tin Fisher",
          "question": "Làm thế nào phân bổ ngân sách đo lường để ma trận thông tin Fisher đạt chất lượng cao nhất qua SDP?",
          "source": "§7.5"
        },
        {
          "slug": "ellipsoid-cuc-tri-va-tam-hinh-hoc",
          "title": "Ellipsoid thể tích cực trị và Các điểm tâm hình học",
          "question": "Làm sao tìm ellipsoid bao ngoài nhỏ nhất hoặc quả cầu nội tiếp lớn nhất của một đa diện qua LP và log-det?",
          "source": "§8.4–8.5"
        },
        {
          "slug": "bai-toan-dinh-vi-va-mang-luoi",
          "title": "Bài toán định vị, đặt vị trí và tối ưu hóa mạng lưới",
          "question": "Làm thế nào bố trí tọa độ các nút mạng để cực tiểu hóa tổng chi phí dây nối qua SOCP và giải hệ Laplacian?",
          "source": "§8.7"
        }
      ]
    }
  ]
}
