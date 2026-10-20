export const slides = [
  {
    "note": "07-tom-tat-lien-he-bien-so",
    "title": "Hệ số tương quan Pearson",
    "bullets": [
      "Đo lường mức độ gắn kết tuyến tính giữa hai biến định lượng.",
      "Giá trị r nằm trong đoạn [-1, 1], là đại lượng không có đơn vị đo.",
      "Bảo toàn giá trị dưới phép đổi thang đo dương, nhưng đổi dấu khi nhân số âm."
    ],
    "formula": "$$\nr = \\frac{1}{n-1} \\sum_{i=1}^n z_{x_i} z_{y_i}\n$$",
    "example": "Hệ số tương quan r = -0,8979 giữa tỷ lệ nghèo đói và tỷ lệ tốt nghiệp trung học."
  },
  {
    "note": "07-tom-tat-lien-he-bien-so",
    "title": "Đường hồi quy bình phương tối thiểu",
    "bullets": [
      "Xác định đường thẳng tối ưu giảm thiểu tổng bình phương phần dư.",
      "Hệ số độ dốc b1 phản ánh thay đổi kỳ vọng của y khi x tăng một đơn vị.",
      "Hệ số chặn b0 là điểm neo toán học khi x nhận giá trị bằng 0."
    ],
    "formula": "$$\n\\begin{aligned}b_1&=r\\frac{s_y}{s_x},\\\\b_0&=\\bar y-b_1\\bar x.\\end{aligned}\n$$",
    "example": "Phương trình hồi quy tốt nghiệp theo nghèo đói: $\\hat{y} = 96{,}2022 - 0{,}8979 x$."
  },
  {
    "note": "07-tom-tat-lien-he-bien-so",
    "title": "Phần dư và ranh giới suy luận tương quan",
    "bullets": [
      "Phần dư e_i là hiệu số giữa giá trị thực tế y_i và giá trị dự báo y_hat_i.",
      "Tương quan mẫu r = 0 không chứng minh được tính độc lập hay rho = 0 ở tổng thể.",
      "Tương quan tuyến tính không đồng nghĩa với quan hệ nhân quả."
    ],
    "formula": "$$\ne_i = y_i - \\hat{y}_i\n$$",
    "example": "Bang California có tỷ lệ thực tế 81,1%, dự báo 84,71%, phần dư tương ứng là -3,61%."
  }
]
