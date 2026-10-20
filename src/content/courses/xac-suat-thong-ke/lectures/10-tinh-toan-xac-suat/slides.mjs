export const slides = [
  {
    "note": "10-tinh-toan-xac-suat",
    "title": "Xác suất có điều kiện",
    "bullets": [
      "Đo lường xác suất xảy ra của biến cố A khi biết trước biến cố B đã xảy ra.",
      "Thu hẹp không gian mẫu ban đầu về tập kết quả B.",
      "Chỉ xác định khi điều kiện B có xác suất xảy ra lớn hơn 0.",
      "Điều kiện xác định: P(B) > 0."
    ],
    "formula": "$$\nP(A\\mid B)=\\frac{P(A\\cap B)}{P(B)}.\n$$",
    "example": "Xác suất rút được quân Át khi biết trước đó đã rút trúng một lá bài màu đỏ."
  },
  {
    "note": "10-tinh-toan-xac-suat",
    "title": "Quy tắc nhân và tính độc lập thống kê",
    "bullets": [
      "Hai biến cố A và B độc lập khi việc B xảy ra không thay đổi xác suất của A.",
      "Khi độc lập, xác suất đồng thời bằng tích hai xác suất riêng rẽ.",
      "Phân biệt rõ độc lập thống kê với xung khắc hình học.",
      "Đẳng thức trên là tiêu chuẩn độc lập của hai biến cố."
    ],
    "formula": "$$\nP(A\\cap B)=P(A)P(B).\n$$",
    "example": "Tung hai con xúc xắc độc lập: Xác suất cùng xuất hiện mặt 6 bằng (1/6) x (1/6) = 1/36."
  },
  {
    "note": "10-tinh-toan-xac-suat",
    "title": "Định lý Bayes và công thức xác suất toàn phần",
    "bullets": [
      "Công thức xác suất toàn phần phân tích biến cố theo hệ phân hoạch đầy đủ.",
      "Định lý Bayes cập nhật xác suất tiên nghiệm thành xác suất hậu nghiệm khi có bằng chứng mới.",
      "Cốt lõi cho suy luận xác suất trong y khoa và học máy.",
      "Các B₁,…,Bₘ tạo thành một phân hoạch hữu hạn. Điều kiện: P(A) > 0 và mỗi xác suất có điều kiện được sử dụng phải xác định."
    ],
    "formula": "$$\n\\begin{aligned}&q_j=P(A\\mid B_j)P(B_j),\\\\&P(A)=q_1+\\dots+q_m,\\\\&P(B_i\\mid A)=q_i/P(A).\\end{aligned}\n$$",
    "example": "Cập nhật xác suất mắc bệnh sau khi nhận kết quả xét nghiệm dương tính trong tầm soát y tế."
  }
]
