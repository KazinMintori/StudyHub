export const lessons = [
  {
    "number": 7,
    "slug": "07-hoc-may-co-giam-sat",
    "title": "Học máy có giám sát",
    "prerequisites": [],
    "supportingConcepts": [],
    "status": "ready",
    "lessonStatus": "ready",
    "description": "Mô hình hóa bài toán học có giám sát, hàm mất mát và đánh giá dự đoán, cây quyết định, hồi quy tuyến tính, hồi quy logistic, hiện tượng quá khớp, điều chuẩn và các mô hình kết hợp.",
    "topicGroups": [
      {
        "title": "Các chủ đề trong chương",
        "topics": [
          {
            "slug": "7-1-cac-van-de-cot-loi-trong-hoc-may",
            "title": "7.1 Các vấn đề cốt lõi trong học máy",
            "question": "Những thành phần cơ bản của một bài toán học máy là gì và tại sao thiên kiến quy nạp lại là điều tất yếu?"
          },
          {
            "slug": "7-2-hoc-co-giam-sat-va-danh-gia-du-doan",
            "title": "7.2 Nền tảng học có giám sát và đánh giá dự đoán",
            "question": "Làm thế nào để đo lường độ chính xác của dự đoán qua các hàm mất mát L0, L1, L2, mất mát logarit và ma trận nhầm lẫn?"
          },
          {
            "slug": "7-3-cac-mo-hinh-co-ban-cho-hoc-co-giam-sat",
            "title": "7.3 Các mô hình cơ bản cho học có giám sát",
            "question": "Cơ chế xây dựng cây quyết định qua entropy, hồi quy tuyến tính và hồi quy logistic hoạt động như thế nào?"
          },
          {
            "slug": "7-4-qua-khop-va-kiem-soat-do-phuc-tap",
            "title": "7.4 Quá khớp và kiểm soát độ phức tạp",
            "question": "Hiện tượng quá khớp là gì và làm thế nào để kiểm soát độ phức tạp mô hình bằng điều chuẩn L1, L2 và kiểm định chéo?"
          },
          {
            "slug": "7-5-cac-mo-hinh-ket-hop",
            "title": "7.5 Các mô hình kết hợp",
            "question": "Tại sao việc kết hợp nhiều mô hình (Bagging, Random Forest, GBDT) lại vượt trội hơn một mô hình đơn lẻ?"
          },
          {
            "slug": "7-6-cac-gioi-han-cua-hoc-co-giam-sat",
            "title": "7.6 Các giới hạn của học có giám sát",
            "question": "Những giả định ngầm định nào của học có giám sát dễ bị phá vỡ trong thế giới thực?"
          },
          {
            "slug": "7-7-tac-dong-xa-hoi",
            "title": "7.7 Tác động xã hội và đạo đức của học máy",
            "question": "Các hệ thống học máy đối mặt với những thách thức đạo đức, công bằng và quyền riêng tư nào?"
          },
          {
            "slug": "7-8-on-tap",
            "title": "7.8 Ôn tập và tổng kết chương",
            "question": "Làm thế nào để hệ thống hóa và lựa chọn mô hình học máy phù hợp nhất cho bài toán thực tế?"
          },
          {
            "slug": "7-9-tai-lieu-tham-khao-va-doc-them",
            "title": "7.9 Tài liệu tham khảo và đọc thêm",
            "question": "Các ý tưởng lớn của học máy có giám sát đã phát triển và định hình qua lịch sử như thế nào?"
          },
          {
            "slug": "7-10-bai-tap",
            "title": "7.10 Bài tập và lời giải chi tiết",
            "question": "Phương pháp giải quyết các bài toán tối ưu hàm mất mát, entropy, gradient descent và tham số hóa đặc trưng?"
          }
        ]
      }
    ]
  }
]

export const slides = [
  {
    "title": "Bản chất của học máy và thiên kiến quy nạp",
    "bullets": [
      "Học máy nhằm mô hình hóa cơ chế sinh dữ liệu của thế giới để cải thiện hành vi tác tử, không dừng lại ở việc khớp dữ liệu thuần túy.",
      "Thiên kiến quy nạp (inductive bias) là tập hợp các giả thiết tiên nghiệm bắt buộc phải có để tác tử có thể suy diễn và khái quát hóa trên các mẫu chưa thấy."
    ],
    "note": "07-hoc-may-co-giam-sat",
    "formula": "",
    "example": ""
  },
  {
    "title": "Hàm mất mát và điểm dự đoán tối ưu",
    "bullets": [
      "Hàm mất mát L0 (0-1) tối ưu tại Yếu vị (Mode); mất mát L1 (sai số tuyệt đối) tối ưu tại Trung vị (Median); mất mát L2 (bình phương) tối ưu tại Kỳ vọng (Mean).",
      "Đánh giá phân loại nhị phân dựa trên ma trận nhầm lẫn (Precision, Recall, F1) và diện tích dưới đường cong ROC (AUC)."
    ],
    "note": "07-hoc-may-co-giam-sat",
    "formula": "",
    "example": ""
  },
  {
    "title": "Cây quyết định và Entropy thông tin",
    "bullets": [
      "Cây quyết định phân chia không gian đặc trưng bằng các lát cắt trực giao; nút trong kiểm tra điều kiện, nút lá chứa dự đoán.",
      "Độ lợi thông tin (Information Gain) đo lường lượng giảm độ hỗn loạn Entropy của Shannon, định hướng thuật toán tham lam chọn phép phân tách tốt nhất."
    ],
    "note": "07-hoc-may-co-giam-sat",
    "formula": "",
    "example": ""
  },
  {
    "title": "Quá khớp và Kiểm soát độ phức tạp",
    "bullets": [
      "Quá khớp xuất hiện khi mô hình ghi nhớ nhiễu của tập huấn luyện, làm tăng sai số kiểm thử theo quy luật đánh đổi chệch - phương sai.",
      "Điều chuẩn L2 (Ridge) thu hẹp trọng số; điều chuẩn L1 (Lasso) tạo tính thưa và chọn đặc trưng; kiểm định chéo k-lớp giúp chọn siêu tham số tối ưu."
    ],
    "note": "07-hoc-may-co-giam-sat",
    "formula": "",
    "example": ""
  },
  {
    "title": "Mô hình kết hợp và Cây tăng cường Gradient (GBDT)",
    "bullets": [
      "Đóng bao (Bagging) và Rừng ngẫu nhiên huấn luyện các cây song song để triệt tiêu phương sai; Boosting huấn luyện tuần tự để giảm độ chệch.",
      "GBDT tối ưu hóa hàm mất mát tùy ý bằng hạ gradient trên phần dư, là công cụ thống trị tuyệt đối trên dữ liệu bảng có cấu trúc."
    ],
    "note": "07-hoc-may-co-giam-sat",
    "formula": "",
    "example": ""
  }
]
